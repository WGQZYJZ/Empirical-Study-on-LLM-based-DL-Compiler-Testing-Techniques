import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_343 = relay.const([[[-5.544845,-1.285334,-7.333691],[2.299009,-5.464725,8.043714],[-4.544889,-6.712633,-4.998963],[4.582954,5.069779,0.680272],[2.159692,6.280266,6.605347],[-0.134585,9.223193,7.873041],[-4.773307,1.896375,-1.546689],[7.065491,9.339514,-1.311420],[1.119257,-8.964505,5.590732]],[[3.225175,-6.288261,8.783500],[7.101155,-9.840882,-4.160385],[-4.077829,-0.425797,-8.314300],[-1.012672,9.499164,8.237752],[8.400336,1.364743,8.462701],[4.983623,-7.199734,-0.645785],[-8.431341,9.679501,-5.335885],[-5.655248,-2.901459,-2.381771],[-8.449426,3.221193,-9.933628]],[[1.344420,7.754777,3.150752],[7.546330,3.782537,6.158640],[8.560324,5.030475,-5.969284],[7.568016,-0.967370,7.889415],[-1.664057,6.628644,6.913421],[-9.496881,6.094878,7.550021],[9.575266,-4.896726,-8.194583],[-5.216225,1.827594,-5.193889],[4.919085,-5.917701,-5.888381]],[[-4.072490,8.038342,-3.437901],[6.706297,6.753717,-3.000441],[5.378096,6.026152,6.899723],[3.565068,-4.599907,1.951086],[-6.494561,-4.071496,8.893024],[-0.919123,1.977755,4.707672],[-4.649080,-3.905897,-7.802770],[0.859261,-4.050617,6.104732],[-2.072498,6.864369,4.197976]],[[-5.194163,2.827299,-2.987131],[1.653656,-5.498688,6.880168],[-2.466068,-7.214470,1.356239],[9.647682,5.161971,-0.042966],[7.256637,3.556387,0.285535],[-5.373503,9.171438,-5.206386],[-6.647534,-6.412211,-0.474043],[-0.525014,-7.110533,9.250613],[3.325455,-1.405305,2.855213]],[[7.026350,3.451285,1.530015],[5.761469,-7.983245,-0.345011],[2.981545,-4.643677,2.009475],[1.607079,6.300584,5.191418],[6.236955,-8.866237,5.618962],[-1.858778,-8.289738,5.374846],[-5.580986,6.293738,0.920428],[6.500722,-7.615542,6.685515],[-5.477476,-1.246669,-4.946231]],[[8.395622,-1.649100,6.677556],[7.499021,3.552364,6.683466],[0.154002,2.175410,5.063952],[-9.646995,9.723630,-6.672868],[5.499818,7.201111,0.907443],[4.519186,-3.528697,-6.521411],[7.061444,3.794774,6.921227],[6.628846,8.031896,-2.932576],[-9.234992,2.182362,2.868235]],[[-8.077080,2.290197,-3.849823],[2.244649,2.938307,-8.935261],[2.252671,1.919876,-1.810419],[3.525972,2.348452,-7.862041],[3.607220,8.257727,4.082387],[4.813742,9.592612,1.800758],[3.561195,5.064344,-8.103032],[-6.568124,5.746796,1.141387],[-9.738091,2.893595,5.283267]],[[1.199876,-1.195727,2.172465],[-1.302690,5.836249,8.963514],[3.159651,1.445619,1.624230],[-9.622780,7.787391,2.542520],[8.490990,-8.893738,-8.146526],[6.718320,-8.614779,-6.636472],[5.851815,-7.471630,-5.795676],[6.836859,-8.096580,-5.902154],[7.922410,8.093324,-5.666312]],[[6.262494,1.666634,-4.617720],[1.916554,2.425394,-4.310291],[1.771463,-8.893241,-3.410398],[-0.615554,6.381589,5.676702],[-1.131808,-3.647180,0.694173],[5.975810,6.825156,-5.399180],[-0.231749,9.099666,-9.832947],[8.175764,9.797518,8.430226],[-5.406984,1.402505,3.857218]]], dtype = "float32")#candidate|343|(10, 9, 3)|const|float32
uop_344 = relay.sin(const_343.astype('float32')) # shape=(10, 9, 3)
output = uop_344
output2 = uop_344
func_373 = relay.Function([], output)
mod['func_373'] = func_373
mod = relay.transform.InferType()(mod)
output = func_373()
func_374 = relay.Function([], output)
mutated_mod['func_374'] = func_374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_398 = relay.var("var_398", dtype = "int8", shape = (4, 15, 4))#candidate|398|(4, 15, 4)|var|int8
var_399 = relay.var("var_399", dtype = "int8", shape = (4, 15, 4))#candidate|399|(4, 15, 4)|var|int8
bop_400 = relay.subtract(var_398.astype('int8'), relay.reshape(var_399.astype('int8'), relay.shape_of(var_398))) # shape=(4, 15, 4)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_403 = func_373_call()
call_404 = func_373_call()
output = relay.Tuple([bop_400,call_403,])
output2 = relay.Tuple([bop_400,call_404,])
func_405 = relay.Function([var_398,var_399,], output)
mod['func_405'] = func_405
mod = relay.transform.InferType()(mod)
mutated_mod['func_405'] = func_405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_405_call = mutated_mod.get_global_var('func_405')
var_407 = relay.var("var_407", dtype = "int8", shape = (4, 15, 4))#candidate|407|(4, 15, 4)|var|int8
var_408 = relay.var("var_408", dtype = "int8", shape = (4, 15, 4))#candidate|408|(4, 15, 4)|var|int8
call_406 = func_405_call(var_407,var_408,)
output = call_406
func_409 = relay.Function([var_407,var_408,], output)
mutated_mod['func_409'] = func_409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_411 = func_373_call()
call_412 = func_373_call()
uop_423 = relay.sigmoid(call_411.astype('float32')) # shape=(10, 9, 3)
uop_425 = relay.sigmoid(call_412.astype('float32')) # shape=(10, 9, 3)
output = uop_423
output2 = uop_425
func_429 = relay.Function([], output)
mod['func_429'] = func_429
mod = relay.transform.InferType()(mod)
output = func_429()
func_430 = relay.Function([], output)
mutated_mod['func_430'] = func_430
mutated_mod = relay.transform.InferType()(mutated_mod)
var_452 = relay.var("var_452", dtype = "uint32", shape = (1, 3, 14))#candidate|452|(1, 3, 14)|var|uint32
var_453 = relay.var("var_453", dtype = "uint32", shape = (3, 3, 14))#candidate|453|(3, 3, 14)|var|uint32
bop_454 = relay.greater_equal(var_452.astype('bool'), var_453.astype('bool')) # shape=(3, 3, 14)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_466 = func_373_call()
call_467 = func_373_call()
output = relay.Tuple([bop_454,call_466,])
output2 = relay.Tuple([bop_454,call_467,])
func_471 = relay.Function([var_452,var_453,], output)
mod['func_471'] = func_471
mod = relay.transform.InferType()(mod)
var_472 = relay.var("var_472", dtype = "uint32", shape = (1, 3, 14))#candidate|472|(1, 3, 14)|var|uint32
var_473 = relay.var("var_473", dtype = "uint32", shape = (3, 3, 14))#candidate|473|(3, 3, 14)|var|uint32
output = func_471(var_472,var_473,)
func_474 = relay.Function([var_472,var_473,], output)
mutated_mod['func_474'] = func_474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_518 = func_429_call()
call_519 = func_429_call()
func_471_call = mod.get_global_var('func_471')
func_474_call = mutated_mod.get_global_var('func_474')
const_523 = relay.const([-7,6,-6,1,9,3,9,-2,3,-9,3,-10,-3,-7,7,-4,-10,2,-5,9,-9,8,6,10,5,-2,7,-5,1,7,9,-6,-4,-5,3,10,6,-2,8,-4,1,-1], dtype = "uint32")#candidate|523|(42,)|const|uint32
var_524 = relay.var("var_524", dtype = "uint32", shape = (126,))#candidate|524|(126,)|var|uint32
call_522 = relay.TupleGetItem(func_471_call(relay.reshape(const_523.astype('uint32'), [1, 3, 14]), relay.reshape(var_524.astype('uint32'), [3, 3, 14]), ), 1)
call_525 = relay.TupleGetItem(func_474_call(relay.reshape(const_523.astype('uint32'), [1, 3, 14]), relay.reshape(var_524.astype('uint32'), [3, 3, 14]), ), 1)
uop_526 = relay.atan(call_518.astype('float32')) # shape=(10, 9, 3)
uop_528 = relay.atan(call_519.astype('float32')) # shape=(10, 9, 3)
output = relay.Tuple([call_522,const_523,var_524,uop_526,])
output2 = relay.Tuple([call_525,const_523,var_524,uop_528,])
func_530 = relay.Function([var_524,], output)
mod['func_530'] = func_530
mod = relay.transform.InferType()(mod)
mutated_mod['func_530'] = func_530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_531 = relay.var("var_531", dtype = "uint32", shape = (126,))#candidate|531|(126,)|var|uint32
func_530_call = mutated_mod.get_global_var('func_530')
call_532 = func_530_call(var_531)
output = call_532
func_533 = relay.Function([var_531], output)
mutated_mod['func_533'] = func_533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_535 = func_373_call()
call_536 = func_373_call()
uop_540 = relay.atanh(call_535.astype('float64')) # shape=(10, 9, 3)
uop_542 = relay.atanh(call_536.astype('float64')) # shape=(10, 9, 3)
output = uop_540
output2 = uop_542
func_553 = relay.Function([], output)
mod['func_553'] = func_553
mod = relay.transform.InferType()(mod)
mutated_mod['func_553'] = func_553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_553_call = mutated_mod.get_global_var('func_553')
call_554 = func_553_call()
output = call_554
func_555 = relay.Function([], output)
mutated_mod['func_555'] = func_555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_604 = func_373_call()
call_605 = func_373_call()
output = call_604
output2 = call_605
func_609 = relay.Function([], output)
mod['func_609'] = func_609
mod = relay.transform.InferType()(mod)
output = func_609()
func_610 = relay.Function([], output)
mutated_mod['func_610'] = func_610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_614 = func_609_call()
call_615 = func_609_call()
uop_621 = relay.log(call_614.astype('float64')) # shape=(10, 9, 3)
uop_623 = relay.log(call_615.astype('float64')) # shape=(10, 9, 3)
output = uop_621
output2 = uop_623
func_626 = relay.Function([], output)
mod['func_626'] = func_626
mod = relay.transform.InferType()(mod)
output = func_626()
func_627 = relay.Function([], output)
mutated_mod['func_627'] = func_627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_671 = func_373_call()
call_672 = func_373_call()
uop_673 = relay.asinh(call_671.astype('float32')) # shape=(10, 9, 3)
uop_675 = relay.asinh(call_672.astype('float32')) # shape=(10, 9, 3)
output = relay.Tuple([uop_673,])
output2 = relay.Tuple([uop_675,])
func_680 = relay.Function([], output)
mod['func_680'] = func_680
mod = relay.transform.InferType()(mod)
output = func_680()
func_681 = relay.Function([], output)
mutated_mod['func_681'] = func_681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_681_call = mutated_mod.get_global_var('func_681')
call_696 = relay.TupleGetItem(func_680_call(), 0)
call_697 = relay.TupleGetItem(func_681_call(), 0)
output = relay.Tuple([call_696,])
output2 = relay.Tuple([call_697,])
func_703 = relay.Function([], output)
mod['func_703'] = func_703
mod = relay.transform.InferType()(mod)
mutated_mod['func_703'] = func_703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_703_call = mutated_mod.get_global_var('func_703')
call_704 = func_703_call()
output = call_704
func_705 = relay.Function([], output)
mutated_mod['func_705'] = func_705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_626_call = mod.get_global_var('func_626')
func_627_call = mutated_mod.get_global_var('func_627')
call_721 = func_626_call()
call_722 = func_626_call()
output = call_721
output2 = call_722
func_736 = relay.Function([], output)
mod['func_736'] = func_736
mod = relay.transform.InferType()(mod)
mutated_mod['func_736'] = func_736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mutated_mod.get_global_var('func_736')
call_737 = func_736_call()
output = call_737
func_738 = relay.Function([], output)
mutated_mod['func_738'] = func_738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_749 = func_429_call()
call_750 = func_429_call()
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_757 = func_553_call()
call_758 = func_553_call()
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
var_762 = relay.var("var_762", dtype = "uint32", shape = (126,))#candidate|762|(126,)|var|uint32
call_761 = relay.TupleGetItem(func_530_call(relay.reshape(var_762.astype('uint32'), [126,])), 2)
call_763 = relay.TupleGetItem(func_533_call(relay.reshape(var_762.astype('uint32'), [126,])), 2)
const_773 = relay.const([-7,8,-10,2,-9,-2,7,-5,7,-5,3,3,5,-9,-4,-4,3,-2,7,5,-6,4,-6,-6,-7,10,-6,-8,-3,-3,1,-7,-1,9,4,-1,5,-2,4,-4,9,-9,-10,-6,-3,-1,8,1,8,-7,-6,-1,-6,1,-10,-1,8,-6,8,-1,-2,-5,10,-2,-8,1,9,-4,-4,5,10,5,-7,-6,4,5,-2,8,8,2,-1,9,-4,5,10,2,-7,7,1,-8,-3,-2,-7,8,-2,-1,-3,5,5,-3,-1,4,5,3,-7,2,-5,-4,7,-8,-2,2,-9,-1,8,-1,3,6,-7,4,1,3,-10,-8,8,-6], dtype = "uint32")#candidate|773|(126,)|const|uint32
bop_774 = relay.greater_equal(var_762.astype('bool'), relay.reshape(const_773.astype('bool'), relay.shape_of(var_762))) # shape=(126,)
bop_786 = relay.power(bop_774.astype('float32'), relay.reshape(var_762.astype('float32'), relay.shape_of(bop_774))) # shape=(126,)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_789 = func_609_call()
call_790 = func_609_call()
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_818 = func_609_call()
call_819 = func_609_call()
output = relay.Tuple([call_749,call_757,call_761,bop_786,call_789,call_818,])
output2 = relay.Tuple([call_750,call_758,call_763,bop_786,call_790,call_819,])
func_822 = relay.Function([var_762,], output)
mod['func_822'] = func_822
mod = relay.transform.InferType()(mod)
var_823 = relay.var("var_823", dtype = "uint32", shape = (126,))#candidate|823|(126,)|var|uint32
output = func_822(var_823)
func_824 = relay.Function([var_823], output)
mutated_mod['func_824'] = func_824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_878 = func_609_call()
call_879 = func_609_call()
output = call_878
output2 = call_879
func_882 = relay.Function([], output)
mod['func_882'] = func_882
mod = relay.transform.InferType()(mod)
output = func_882()
func_883 = relay.Function([], output)
mutated_mod['func_883'] = func_883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_917 = func_609_call()
call_918 = func_609_call()
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_952 = func_609_call()
call_953 = func_609_call()
uop_958 = relay.asin(call_952.astype('float32')) # shape=(10, 9, 3)
uop_960 = relay.asin(call_953.astype('float32')) # shape=(10, 9, 3)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_961 = relay.TupleGetItem(func_703_call(), 0)
call_962 = relay.TupleGetItem(func_705_call(), 0)
output = relay.Tuple([call_917,uop_958,call_961,])
output2 = relay.Tuple([call_918,uop_960,call_962,])
func_968 = relay.Function([], output)
mod['func_968'] = func_968
mod = relay.transform.InferType()(mod)
mutated_mod['func_968'] = func_968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_968_call = mutated_mod.get_global_var('func_968')
call_969 = func_968_call()
output = call_969
func_970 = relay.Function([], output)
mutated_mod['func_970'] = func_970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_1000 = func_429_call()
call_1001 = func_429_call()
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_1003 = relay.TupleGetItem(func_968_call(), 1)
call_1004 = relay.TupleGetItem(func_970_call(), 1)
bop_1007 = relay.minimum(call_1000.astype('uint64'), relay.reshape(call_1003.astype('uint64'), relay.shape_of(call_1000))) # shape=(10, 9, 3)
bop_1010 = relay.minimum(call_1001.astype('uint64'), relay.reshape(call_1004.astype('uint64'), relay.shape_of(call_1001))) # shape=(10, 9, 3)
bop_1017 = relay.greater_equal(call_1003.astype('bool'), relay.reshape(bop_1007.astype('bool'), relay.shape_of(call_1003))) # shape=(10, 9, 3)
bop_1020 = relay.greater_equal(call_1004.astype('bool'), relay.reshape(bop_1010.astype('bool'), relay.shape_of(call_1004))) # shape=(10, 9, 3)
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_1027 = relay.TupleGetItem(func_968_call(), 2)
call_1028 = relay.TupleGetItem(func_970_call(), 2)
uop_1038 = relay.exp(call_1027.astype('float32')) # shape=(10, 9, 3)
uop_1040 = relay.exp(call_1028.astype('float32')) # shape=(10, 9, 3)
func_626_call = mod.get_global_var('func_626')
func_627_call = mutated_mod.get_global_var('func_627')
call_1042 = func_626_call()
call_1043 = func_626_call()
output = relay.Tuple([bop_1017,uop_1038,call_1042,])
output2 = relay.Tuple([bop_1020,uop_1040,call_1043,])
func_1044 = relay.Function([], output)
mod['func_1044'] = func_1044
mod = relay.transform.InferType()(mod)
output = func_1044()
func_1045 = relay.Function([], output)
mutated_mod['func_1045'] = func_1045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_738_call = mutated_mod.get_global_var('func_738')
call_1065 = func_736_call()
call_1066 = func_736_call()
const_1067 = relay.const([[[3.418274,-6.300107,-4.338370],[-4.773883,-0.411460,-4.848031],[7.829450,-6.008953,-6.819293],[7.401594,-3.712223,-0.860029],[0.653129,-9.044002,-5.600102],[-5.600498,-6.792082,-9.399583],[-8.775007,-7.325733,2.927912],[6.305184,0.826128,-0.480921],[-8.629028,0.730887,-8.106822]],[[5.486071,8.524857,-4.421449],[4.748990,-1.246139,6.657253],[-5.713488,2.658355,7.975506],[2.358872,9.786792,-8.646937],[-5.489899,7.397481,5.402731],[-9.568955,5.541418,2.136134],[8.241405,3.219619,-5.398897],[-1.707039,-1.810191,1.854029],[-5.730322,-1.740808,0.456770]],[[7.602912,-0.883840,4.472908],[-1.542025,-7.039994,-6.440928],[-9.581349,-9.331859,0.558893],[-1.053285,1.166364,8.849314],[-1.836472,4.114044,-7.363612],[5.350146,-4.787475,-4.828309],[-2.891390,7.356350,2.020715],[-4.472125,0.018714,6.301353],[4.356977,-4.920361,-5.331542]],[[1.450764,3.207587,-3.192881],[8.331776,-6.730663,1.275615],[-4.300109,7.002604,-6.918017],[3.919456,-9.279406,4.861901],[1.963009,-5.837645,1.757437],[6.490948,2.141402,9.880495],[-4.663772,-6.327144,-9.573488],[-7.070121,6.804707,9.782833],[-5.996775,-3.383485,6.150437]],[[-2.027370,-7.601889,5.774040],[5.901047,-3.820022,8.842899],[-9.071085,-0.364315,-8.241221],[-9.191003,8.171581,2.356430],[6.102786,5.749961,-2.137381],[5.713790,5.210602,7.250939],[9.625315,-0.824911,-9.760206],[7.291132,9.936839,5.327703],[2.265865,-4.540720,4.588846]],[[8.922260,8.504946,-3.050537],[2.199925,-2.851245,8.217588],[8.854512,5.040757,-7.792120],[-4.022502,-7.152901,7.487379],[6.396377,-2.157089,-8.435591],[0.184787,-0.921792,-2.928231],[8.388830,5.366687,3.011820],[3.874907,3.091966,-3.247631],[-9.855532,-0.751406,-3.169779]],[[-8.602050,-2.768379,-5.760392],[-2.674851,-5.331609,-3.013540],[6.363591,-7.281120,-9.246324],[5.494929,2.234613,-9.930044],[-2.215182,-3.072476,2.027228],[0.011859,-8.949903,-8.461955],[-8.832859,4.764269,-2.222167],[5.457963,0.858319,-0.900427],[2.219169,1.473137,-0.173519]],[[-2.546164,8.572213,7.518055],[-2.422320,-9.207484,-1.647594],[2.542246,-6.060516,5.923372],[-7.448364,-1.399231,8.012163],[1.643680,0.531865,9.668674],[-4.976080,-4.493819,-5.515717],[0.377442,-0.609297,7.852570],[-5.970982,0.351881,5.981839],[3.113101,-1.845850,7.212308]],[[-6.566055,-4.900806,-8.162525],[-3.494897,-3.125131,-4.949894],[-5.666352,7.297077,5.684673],[-8.977323,8.280308,-6.033403],[-5.765830,-1.935345,-3.782585],[-4.099839,4.267522,-7.213541],[-5.099428,-3.589567,9.670421],[1.854769,-4.431366,9.319590],[-2.379947,-1.871263,7.913639]],[[-3.004414,-4.780314,-1.940688],[0.312924,-2.344156,-2.809897],[-9.983949,3.710333,2.351205],[9.186524,-2.787955,4.442427],[8.479691,3.062601,1.357848],[3.502357,3.999710,-2.608575],[-0.860397,-6.280148,-3.071956],[5.812707,-4.785482,-8.979502],[9.187567,-2.141841,0.850358]]], dtype = "float64")#candidate|1067|(10, 9, 3)|const|float64
bop_1068 = relay.equal(call_1065.astype('bool'), relay.reshape(const_1067.astype('bool'), relay.shape_of(call_1065))) # shape=(10, 9, 3)
bop_1071 = relay.equal(call_1066.astype('bool'), relay.reshape(const_1067.astype('bool'), relay.shape_of(call_1066))) # shape=(10, 9, 3)
func_882_call = mod.get_global_var('func_882')
func_883_call = mutated_mod.get_global_var('func_883')
call_1072 = func_882_call()
call_1073 = func_882_call()
output = relay.Tuple([bop_1068,call_1072,])
output2 = relay.Tuple([bop_1071,call_1073,])
func_1099 = relay.Function([], output)
mod['func_1099'] = func_1099
mod = relay.transform.InferType()(mod)
mutated_mod['func_1099'] = func_1099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1099_call = mutated_mod.get_global_var('func_1099')
call_1100 = func_1099_call()
output = call_1100
func_1101 = relay.Function([], output)
mutated_mod['func_1101'] = func_1101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_1105 = func_373_call()
call_1106 = func_373_call()
func_822_call = mod.get_global_var('func_822')
func_824_call = mutated_mod.get_global_var('func_824')
var_1124 = relay.var("var_1124", dtype = "uint32", shape = (126,))#candidate|1124|(126,)|var|uint32
call_1123 = relay.TupleGetItem(func_822_call(relay.reshape(var_1124.astype('uint32'), [126,])), 3)
call_1125 = relay.TupleGetItem(func_824_call(relay.reshape(var_1124.astype('uint32'), [126,])), 3)
func_471_call = mod.get_global_var('func_471')
func_474_call = mutated_mod.get_global_var('func_474')
const_1133 = relay.const([-3,1,-2,-10,3,5,-9,8,-1,6,7,2,6,-8,-3,7,1,3,-7,4,4,-1,-8,-10,5,8,2,2,10,-10,-4,-10,-5,10,-7,-9,6,5,8,-4,3,-3], dtype = "uint32")#candidate|1133|(42,)|const|uint32
call_1132 = relay.TupleGetItem(func_471_call(relay.reshape(const_1133.astype('uint32'), [1, 3, 14]), relay.reshape(call_1123.astype('uint32'), [3, 3, 14]), ), 1)
call_1134 = relay.TupleGetItem(func_474_call(relay.reshape(const_1133.astype('uint32'), [1, 3, 14]), relay.reshape(call_1123.astype('uint32'), [3, 3, 14]), ), 1)
func_626_call = mod.get_global_var('func_626')
func_627_call = mutated_mod.get_global_var('func_627')
call_1142 = func_626_call()
call_1143 = func_626_call()
output = relay.Tuple([call_1105,call_1123,var_1124,call_1132,const_1133,call_1142,])
output2 = relay.Tuple([call_1106,call_1125,var_1124,call_1134,const_1133,call_1143,])
func_1148 = relay.Function([var_1124,], output)
mod['func_1148'] = func_1148
mod = relay.transform.InferType()(mod)
var_1149 = relay.var("var_1149", dtype = "uint32", shape = (126,))#candidate|1149|(126,)|var|uint32
output = func_1148(var_1149)
func_1150 = relay.Function([var_1149], output)
mutated_mod['func_1150'] = func_1150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mod.get_global_var('func_882')
func_883_call = mutated_mod.get_global_var('func_883')
call_1169 = func_882_call()
call_1170 = func_882_call()
output = relay.Tuple([call_1169,])
output2 = relay.Tuple([call_1170,])
func_1173 = relay.Function([], output)
mod['func_1173'] = func_1173
mod = relay.transform.InferType()(mod)
output = func_1173()
func_1174 = relay.Function([], output)
mutated_mod['func_1174'] = func_1174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mod.get_global_var('func_882')
func_883_call = mutated_mod.get_global_var('func_883')
call_1201 = func_882_call()
call_1202 = func_882_call()
output = call_1201
output2 = call_1202
func_1207 = relay.Function([], output)
mod['func_1207'] = func_1207
mod = relay.transform.InferType()(mod)
output = func_1207()
func_1208 = relay.Function([], output)
mutated_mod['func_1208'] = func_1208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_1216 = relay.TupleGetItem(func_703_call(), 0)
call_1217 = relay.TupleGetItem(func_705_call(), 0)
func_1099_call = mod.get_global_var('func_1099')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_1218 = relay.TupleGetItem(func_1099_call(), 0)
call_1219 = relay.TupleGetItem(func_1101_call(), 0)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_1220 = relay.TupleGetItem(func_703_call(), 0)
call_1221 = relay.TupleGetItem(func_705_call(), 0)
output = relay.Tuple([call_1216,call_1218,call_1220,])
output2 = relay.Tuple([call_1217,call_1219,call_1221,])
func_1228 = relay.Function([], output)
mod['func_1228'] = func_1228
mod = relay.transform.InferType()(mod)
mutated_mod['func_1228'] = func_1228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1228_call = mutated_mod.get_global_var('func_1228')
call_1229 = func_1228_call()
output = call_1229
func_1230 = relay.Function([], output)
mutated_mod['func_1230'] = func_1230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1173_call = mod.get_global_var('func_1173')
func_1174_call = mutated_mod.get_global_var('func_1174')
call_1265 = relay.TupleGetItem(func_1173_call(), 0)
call_1266 = relay.TupleGetItem(func_1174_call(), 0)
var_1271 = relay.var("var_1271", dtype = "float32", shape = (10, 9, 3))#candidate|1271|(10, 9, 3)|var|float32
bop_1272 = relay.logical_or(call_1265.astype('bool'), relay.reshape(var_1271.astype('bool'), relay.shape_of(call_1265))) # shape=(10, 9, 3)
bop_1275 = relay.logical_or(call_1266.astype('bool'), relay.reshape(var_1271.astype('bool'), relay.shape_of(call_1266))) # shape=(10, 9, 3)
bop_1276 = relay.not_equal(call_1265.astype('bool'), relay.reshape(var_1271.astype('bool'), relay.shape_of(call_1265))) # shape=(10, 9, 3)
bop_1279 = relay.not_equal(call_1266.astype('bool'), relay.reshape(var_1271.astype('bool'), relay.shape_of(call_1266))) # shape=(10, 9, 3)
output = relay.Tuple([bop_1272,bop_1276,])
output2 = relay.Tuple([bop_1275,bop_1279,])
func_1292 = relay.Function([var_1271,], output)
mod['func_1292'] = func_1292
mod = relay.transform.InferType()(mod)
mutated_mod['func_1292'] = func_1292
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1293 = relay.var("var_1293", dtype = "float32", shape = (10, 9, 3))#candidate|1293|(10, 9, 3)|var|float32
func_1292_call = mutated_mod.get_global_var('func_1292')
call_1294 = func_1292_call(var_1293)
output = call_1294
func_1295 = relay.Function([var_1293], output)
mutated_mod['func_1295'] = func_1295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1099_call = mod.get_global_var('func_1099')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_1297 = relay.TupleGetItem(func_1099_call(), 1)
call_1298 = relay.TupleGetItem(func_1101_call(), 1)
func_405_call = mod.get_global_var('func_405')
func_409_call = mutated_mod.get_global_var('func_409')
const_1310 = relay.const([8,8,-2,-1,1,4,4,-9,-2,5,9,-2,10,3,-5,-3,8,8,8,-7,-1,-10,-6,6,-3,-4,10,-7,1,8,-2,10,-2,-2,-8,-1,1,-5,-4,2,1,2,-4,-4,8,-3,-2,-10,3,-7,10,-1,-3,5,7,-7,-3,-10,7,-2,-5,-5,9,-3,7,3,-10,-10,3,10,-3,6,5,5,-9,7,3,3,7,-4,6,4,4,-10,-9,4,-7,-10,-8,4,-3,3,1,7,2,4,1,-5,-2,-9,-5,-5,-7,7,-9,3,2,-9,4,2,-9,7,6,2,-6,1,8,-6,-10,-10,-5,-4,-1,-9,8,2,-10,5,10,4,-2,9,-10,5,-1,-2,8,-1,-6,3,-4,1,-3,-1,-6,10,9,-10,-8,2,7,-4,-7,-3,9,-9,2,-8,8,1,4,4,3,-6,-8,-10,2,2,-3,4,-3,-5,-3,-4,-4,-5,-6,-4,2,2,10,-4,8,-2,3,10,-9,10,2,2,-9,-4,5,-6,10,8,-9,-2,10,-7,2,-6,-4,2,4,-2,1,10,8,5,-5,9,7,1,7,-8,-7,7,-5,-9,-3,2,9,-9,9,4,-9,9,6,3,10,-10,8,-10,6,-3,-10,-2,8,-7], dtype = "int8")#candidate|1310|(240,)|const|int8
call_1309 = relay.TupleGetItem(func_405_call(relay.reshape(const_1310.astype('int8'), [4, 15, 4]), relay.reshape(const_1310.astype('int8'), [4, 15, 4]), ), 0)
call_1311 = relay.TupleGetItem(func_409_call(relay.reshape(const_1310.astype('int8'), [4, 15, 4]), relay.reshape(const_1310.astype('int8'), [4, 15, 4]), ), 0)
output = relay.Tuple([call_1297,call_1309,const_1310,])
output2 = relay.Tuple([call_1298,call_1311,const_1310,])
func_1316 = relay.Function([], output)
mod['func_1316'] = func_1316
mod = relay.transform.InferType()(mod)
mutated_mod['func_1316'] = func_1316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mutated_mod.get_global_var('func_1316')
call_1317 = func_1316_call()
output = call_1317
func_1318 = relay.Function([], output)
mutated_mod['func_1318'] = func_1318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_1365 = relay.TupleGetItem(func_1316_call(), 1)
call_1366 = relay.TupleGetItem(func_1318_call(), 1)
output = relay.Tuple([call_1365,])
output2 = relay.Tuple([call_1366,])
func_1370 = relay.Function([], output)
mod['func_1370'] = func_1370
mod = relay.transform.InferType()(mod)
output = func_1370()
func_1371 = relay.Function([], output)
mutated_mod['func_1371'] = func_1371
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1375 = relay.const([[[-8,5,6,9],[-1,1,-10,2],[-9,-2,-9,-5],[3,-6,3,-2],[-2,-6,-2,6],[-3,-9,-5,-10],[-6,-1,3,8],[7,2,7,3],[-8,8,4,-5],[2,10,9,-2],[-2,-7,-10,-10],[8,7,5,-7],[-8,5,10,9],[-6,-9,-8,-7],[5,-5,9,-4],[-7,-4,-10,5]],[[5,-2,-10,9],[1,-8,-1,7],[-8,-3,-8,-8],[7,-7,-3,8],[2,5,2,-5],[-3,2,-9,2],[-1,-8,1,6],[-8,-8,5,10],[-6,9,-10,1],[-9,-7,-3,-10],[3,5,-4,5],[-4,-2,9,-8],[9,-2,-2,-10],[7,-3,-6,5],[1,-5,-1,-6],[3,5,9,6]],[[-1,-7,-1,-5],[-6,-9,1,4],[-3,8,9,-2],[3,-6,-1,2],[-1,4,-6,2],[-7,-4,4,2],[-7,3,6,10],[-3,2,9,5],[-3,-3,5,-10],[-4,-1,-2,-6],[-3,7,-4,-9],[-5,10,-4,-3],[-3,-3,2,1],[10,4,4,1],[1,-7,6,6],[6,5,-1,7]],[[7,-2,-5,-4],[-4,-7,10,-6],[-5,-10,8,2],[1,3,6,-8],[2,-9,-3,-10],[-3,3,-4,-6],[1,-1,1,-4],[1,-6,9,-7],[4,-6,10,3],[-4,9,-5,-8],[-3,7,2,-8],[-9,9,10,9],[-5,10,2,1],[2,-3,-6,-7],[-9,7,-6,-6],[1,4,-5,-3]],[[7,-6,-1,-4],[-8,3,-9,-5],[5,-2,6,7],[-5,-7,6,-9],[-7,4,3,-2],[9,4,-6,-4],[2,-3,6,-6],[-2,1,6,3],[-6,-3,6,-7],[3,-3,-2,-9],[5,-3,-3,-1],[-5,-3,4,-6],[4,1,-9,5],[10,10,-6,-6],[-2,-1,-7,9],[7,-3,-7,-5]],[[-10,-3,5,-10],[7,-8,-10,2],[-1,-8,5,2],[-9,-7,6,9],[6,-7,-9,7],[9,-7,-8,-3],[-3,-1,10,2],[-10,8,-1,-6],[-9,10,-1,4],[-10,9,1,9],[4,-2,-5,6],[5,3,-10,-5],[-3,-9,-3,4],[-5,3,6,-1],[4,-7,-2,-4],[6,5,8,7]],[[6,-6,8,-4],[3,-10,-1,-3],[6,4,2,5],[9,6,-1,-9],[-6,7,2,-8],[9,6,-10,-5],[-9,-6,-10,1],[-2,-5,7,-9],[-6,8,6,-5],[-3,-4,-9,1],[9,1,8,-7],[8,-3,-7,-9],[-9,-2,-2,-1],[-9,-9,-6,-6],[-8,4,-8,8],[4,-2,-6,-3]],[[9,-1,4,9],[-6,10,9,-7],[-5,-4,-2,1],[-6,7,8,-6],[-7,10,-8,3],[-9,6,-10,-6],[-1,-8,-5,-9],[3,-2,5,-8],[6,2,-8,5],[-9,-5,3,-4],[2,-7,10,-7],[-1,-4,10,9],[-1,-7,7,6],[5,4,1,-2],[1,-1,7,-6],[8,5,1,3]],[[8,-10,-1,2],[8,-6,6,-3],[7,-8,1,-3],[3,8,-5,-7],[-10,-7,-5,-9],[-4,3,2,5],[-9,6,-4,-2],[8,-10,-2,5],[5,-3,8,3],[-6,2,-2,9],[-9,-5,5,-1],[-1,5,9,5],[1,-4,1,-3],[-4,7,3,1],[-3,6,-8,-9],[9,10,4,-3]],[[3,-4,-5,-1],[3,6,6,-7],[-6,4,-1,10],[-9,-9,6,-9],[-7,3,-1,10],[-4,9,6,8],[-10,-5,-7,10],[-5,-10,1,10],[-2,10,9,7],[-8,5,4,-5],[8,-5,5,3],[-4,-3,-10,-3],[-9,-8,-4,-4],[-3,6,4,2],[-1,9,2,-8],[-2,-1,7,7]]], dtype = "uint32")#candidate|1375|(10, 16, 4)|const|uint32
var_1376 = relay.var("var_1376", dtype = "uint32", shape = (10, 16, 4))#candidate|1376|(10, 16, 4)|var|uint32
bop_1377 = relay.maximum(const_1375.astype('uint32'), relay.reshape(var_1376.astype('uint32'), relay.shape_of(const_1375))) # shape=(10, 16, 4)
output = relay.Tuple([bop_1377,])
output2 = relay.Tuple([bop_1377,])
func_1383 = relay.Function([var_1376,], output)
mod['func_1383'] = func_1383
mod = relay.transform.InferType()(mod)
mutated_mod['func_1383'] = func_1383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1384 = relay.var("var_1384", dtype = "uint32", shape = (10, 16, 4))#candidate|1384|(10, 16, 4)|var|uint32
func_1383_call = mutated_mod.get_global_var('func_1383')
call_1385 = func_1383_call(var_1384)
output = call_1385
func_1386 = relay.Function([var_1384], output)
mutated_mod['func_1386'] = func_1386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1388 = relay.TupleGetItem(func_1370_call(), 0)
call_1389 = relay.TupleGetItem(func_1371_call(), 0)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1390 = relay.TupleGetItem(func_1370_call(), 0)
call_1391 = relay.TupleGetItem(func_1371_call(), 0)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_1395 = func_1207_call()
call_1396 = func_1207_call()
func_1383_call = mod.get_global_var('func_1383')
func_1386_call = mutated_mod.get_global_var('func_1386')
var_1422 = relay.var("var_1422", dtype = "uint32", shape = (640,))#candidate|1422|(640,)|var|uint32
call_1421 = relay.TupleGetItem(func_1383_call(relay.reshape(var_1422.astype('uint32'), [10, 16, 4])), 0)
call_1423 = relay.TupleGetItem(func_1386_call(relay.reshape(var_1422.astype('uint32'), [10, 16, 4])), 0)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_1431 = relay.TupleGetItem(func_1370_call(), 0)
call_1432 = relay.TupleGetItem(func_1371_call(), 0)
bop_1439 = relay.equal(call_1431.astype('bool'), relay.reshape(call_1388.astype('bool'), relay.shape_of(call_1431))) # shape=(4, 15, 4)
bop_1442 = relay.equal(call_1432.astype('bool'), relay.reshape(call_1389.astype('bool'), relay.shape_of(call_1432))) # shape=(4, 15, 4)
output = relay.Tuple([call_1390,call_1395,call_1421,var_1422,bop_1439,])
output2 = relay.Tuple([call_1391,call_1396,call_1423,var_1422,bop_1442,])
func_1450 = relay.Function([var_1422,], output)
mod['func_1450'] = func_1450
mod = relay.transform.InferType()(mod)
mutated_mod['func_1450'] = func_1450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1451 = relay.var("var_1451", dtype = "uint32", shape = (640,))#candidate|1451|(640,)|var|uint32
func_1450_call = mutated_mod.get_global_var('func_1450')
call_1452 = func_1450_call(var_1451)
output = call_1452
func_1453 = relay.Function([var_1451], output)
mutated_mod['func_1453'] = func_1453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_681_call = mutated_mod.get_global_var('func_681')
call_1568 = relay.TupleGetItem(func_680_call(), 0)
call_1569 = relay.TupleGetItem(func_681_call(), 0)
const_1571 = relay.const([[[-1.340152,7.598101,-1.182530],[-8.005616,3.194593,4.093457],[3.426858,-0.618441,8.082157],[2.075665,5.640757,-3.682231],[5.011819,-9.566385,-1.401946],[0.738696,-7.324643,7.900199],[3.983881,-6.033959,-4.609952],[-8.567727,8.595768,-8.121817],[-8.723119,6.745969,-4.174451]],[[7.393189,-1.540917,0.093828],[6.609766,7.246449,5.315186],[-5.281433,-5.717127,5.825941],[-4.341259,-3.852481,-7.346124],[2.609411,-4.495512,0.024597],[-4.882334,5.271093,-5.631077],[2.891564,5.824151,7.407423],[1.269767,-0.357378,5.658609],[-6.750055,9.657696,6.913158]],[[-3.499424,-0.623364,8.517866],[0.160108,-4.765951,-5.339638],[2.619534,-0.287831,-2.390736],[1.552811,2.737570,5.223708],[-9.810239,-6.551360,7.475525],[3.646503,-4.304979,-6.030409],[4.082373,8.402543,-8.113710],[2.916832,1.412728,8.171280],[6.615991,-7.386345,-8.306391]],[[5.641661,4.133838,-6.243322],[-5.511308,-5.943975,3.328988],[-9.330348,8.132303,-0.053560],[-5.765938,5.324079,4.795092],[5.502782,-4.746222,9.221196],[-4.539132,6.011188,-6.594893],[-7.822421,7.723858,-0.780317],[5.987916,-4.553129,-1.554615],[2.603452,-2.781047,3.406598]],[[7.401296,-0.097943,-4.994843],[-6.838081,6.095543,-1.358197],[1.311413,-1.256051,-6.450484],[2.193405,3.181959,-5.120478],[-7.037484,-6.457291,-6.935153],[-2.366056,2.265548,0.143646],[-4.395886,-8.026986,3.208320],[0.008654,8.784769,-1.843663],[-4.870305,3.941012,6.205074]],[[-2.005770,0.631423,-8.197685],[-6.944254,3.739214,9.665294],[2.521852,-0.255275,4.883067],[-6.450739,-4.113505,-2.102976],[0.684207,-6.080059,0.196823],[-8.673452,4.044770,-5.404427],[-7.010564,-6.507845,-5.378145],[-7.131094,5.977233,9.140630],[9.516402,-8.332363,3.014489]],[[-7.261213,9.078208,-4.992271],[-7.938965,-7.419801,-3.034887],[2.983602,3.744536,4.244292],[3.647875,0.530113,-3.690314],[-2.139740,5.655694,-9.445811],[5.677887,4.513067,6.392345],[7.520958,9.266958,-2.786295],[3.864507,-3.066776,8.023637],[-1.319544,6.430933,-6.198269]],[[4.618085,8.031568,5.155960],[9.467097,-9.060623,7.879654],[-2.038095,1.759722,9.130242],[-4.456977,2.568367,1.068701],[-7.307333,-2.561133,-2.460474],[2.211194,4.653704,-5.762373],[-6.754730,9.659488,-2.047723],[9.331321,-9.530437,-6.512175],[-1.891572,-4.793720,5.835420]],[[-0.013126,1.739148,-9.078341],[7.073306,7.531528,-5.028487],[5.708885,-9.882989,-5.564993],[-3.727023,0.950469,-6.882907],[-0.957169,-2.032925,4.291992],[-4.431329,6.494728,-2.028068],[4.178156,-6.062727,-0.481150],[-1.098061,1.648821,-6.997181],[-6.885564,0.354101,2.617484]],[[8.255974,-7.202988,-8.673798],[-6.510131,-6.483043,0.732518],[1.693073,-1.304325,6.393178],[-7.498370,6.197301,-3.788932],[0.941146,-9.587786,4.475809],[7.245034,5.425729,-3.270056],[3.149072,-9.704751,3.946359],[-1.409760,4.157654,-6.975216],[4.328441,-4.389013,-6.782713]]], dtype = "float32")#candidate|1571|(10, 9, 3)|const|float32
bop_1572 = relay.floor_divide(call_1568.astype('float64'), relay.reshape(const_1571.astype('float64'), relay.shape_of(call_1568))) # shape=(10, 9, 3)
bop_1575 = relay.floor_divide(call_1569.astype('float64'), relay.reshape(const_1571.astype('float64'), relay.shape_of(call_1569))) # shape=(10, 9, 3)
uop_1609 = relay.sinh(call_1568.astype('float64')) # shape=(10, 9, 3)
uop_1611 = relay.sinh(call_1569.astype('float64')) # shape=(10, 9, 3)
output = relay.Tuple([bop_1572,uop_1609,])
output2 = relay.Tuple([bop_1575,uop_1611,])
func_1614 = relay.Function([], output)
mod['func_1614'] = func_1614
mod = relay.transform.InferType()(mod)
output = func_1614()
func_1615 = relay.Function([], output)
mutated_mod['func_1615'] = func_1615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_1634 = func_609_call()
call_1635 = func_609_call()
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_1649 = relay.TupleGetItem(func_703_call(), 0)
call_1650 = relay.TupleGetItem(func_705_call(), 0)
output = relay.Tuple([call_1634,call_1649,])
output2 = relay.Tuple([call_1635,call_1650,])
func_1654 = relay.Function([], output)
mod['func_1654'] = func_1654
mod = relay.transform.InferType()(mod)
output = func_1654()
func_1655 = relay.Function([], output)
mutated_mod['func_1655'] = func_1655
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1750 = relay.const([[[-8,8,6,8,9,-1,-9,10],[10,1,-4,-9,9,1,7,-9],[8,-8,1,4,-5,10,3,-1],[-5,-8,9,-6,-9,8,8,-3],[-7,3,-1,7,-9,-8,-8,7],[5,-6,1,3,-1,-8,-10,-7],[5,6,-4,10,9,6,-10,5],[-8,-10,-3,9,-5,4,9,2],[-9,10,1,-7,-9,-10,-7,4],[3,4,-6,1,1,7,-5,6]]], dtype = "int16")#candidate|1750|(1, 10, 8)|const|int16
var_1751 = relay.var("var_1751", dtype = "int16", shape = (11, 10, 8))#candidate|1751|(11, 10, 8)|var|int16
bop_1752 = relay.right_shift(const_1750.astype('int16'), var_1751.astype('int16')) # shape=(11, 10, 8)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_1760 = func_373_call()
call_1761 = func_373_call()
output = relay.Tuple([bop_1752,call_1760,])
output2 = relay.Tuple([bop_1752,call_1761,])
func_1770 = relay.Function([var_1751,], output)
mod['func_1770'] = func_1770
mod = relay.transform.InferType()(mod)
mutated_mod['func_1770'] = func_1770
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1771 = relay.var("var_1771", dtype = "int16", shape = (11, 10, 8))#candidate|1771|(11, 10, 8)|var|int16
func_1770_call = mutated_mod.get_global_var('func_1770')
call_1772 = func_1770_call(var_1771)
output = call_1772
func_1773 = relay.Function([var_1771], output)
mutated_mod['func_1773'] = func_1773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_1887 = func_1207_call()
call_1888 = func_1207_call()
func_1099_call = mod.get_global_var('func_1099')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_1898 = relay.TupleGetItem(func_1099_call(), 0)
call_1899 = relay.TupleGetItem(func_1101_call(), 0)
uop_1909 = relay.rsqrt(call_1887.astype('float32')) # shape=(10, 9, 3)
uop_1911 = relay.rsqrt(call_1888.astype('float32')) # shape=(10, 9, 3)
uop_1914 = relay.cosh(uop_1909.astype('float64')) # shape=(10, 9, 3)
uop_1916 = relay.cosh(uop_1911.astype('float64')) # shape=(10, 9, 3)
func_1383_call = mod.get_global_var('func_1383')
func_1386_call = mutated_mod.get_global_var('func_1386')
const_1919 = relay.const([[-5,-2,-8,1],[2,-1,-4,9],[-6,4,10,-8],[-5,5,-4,-1],[-3,4,-4,9],[1,-2,-4,1],[-1,6,6,-6],[-8,10,9,3],[-6,5,1,5],[-6,9,8,-2],[4,2,3,1],[-10,-5,4,-1],[4,10,4,7],[2,1,-5,-1],[-2,1,1,-7],[6,-10,-10,3],[-10,9,-8,-3],[-4,2,-9,10],[-6,-5,6,-7],[-5,-5,1,9],[10,-3,-6,-1],[-3,10,8,1],[3,-10,-1,-1],[8,-3,3,8],[2,6,-10,-6],[1,-2,6,-2],[1,-7,-3,-9],[6,7,6,5],[-9,-3,7,1],[-7,-7,-6,3],[-3,2,-1,-4],[-2,6,-10,-3],[-1,7,10,-6],[-9,-10,-1,6],[3,7,-6,-1],[-6,6,8,-5],[10,7,-8,-6],[5,5,9,10],[-7,6,-10,4],[5,-1,3,-4],[-6,4,-3,2],[-6,-1,-8,9],[-8,1,-3,5],[8,3,-2,6],[-5,3,-9,-5],[1,10,-7,-7],[5,6,-4,5],[6,3,4,-5],[8,-8,-4,1],[-1,7,1,4],[1,-3,-10,4],[6,-4,-5,-1],[9,-9,2,-8],[-3,10,8,-10],[-5,-3,1,1],[-5,10,-3,4],[-10,-5,-4,-7],[8,1,-5,-5],[1,-5,5,2],[10,1,-2,-5],[9,9,3,-8],[-5,-6,-9,-9],[9,5,-10,6],[-10,3,-2,-8],[-10,-4,-3,3],[3,-6,-2,-5],[1,-7,-10,2],[9,-3,6,4],[8,-1,10,9],[-5,8,-2,-2],[-4,7,-3,-3],[4,5,-7,8],[-7,-6,-4,4],[10,9,-4,6],[-2,-3,1,7],[-2,-9,-1,4],[-7,9,-3,-1],[5,-6,2,9],[4,9,8,3],[8,8,-9,1],[1,7,3,9],[-9,8,-7,-5],[9,-6,-10,6],[1,9,-6,-7],[-2,-5,2,2],[-8,-3,7,6],[2,2,3,9],[-4,5,9,-1],[8,-6,1,-2],[-10,4,4,3],[1,5,-7,-9],[3,3,8,4],[1,6,10,10],[4,-7,-3,-2],[8,-10,4,-6],[-3,-10,4,-5],[-6,6,9,-5],[-10,-9,5,-7],[1,-7,-7,1],[-5,-1,4,5],[-8,-5,-7,-2],[-3,9,-4,-10],[-6,-7,4,-2],[-8,-8,-2,-2],[4,-9,-8,-1],[2,10,8,1],[10,6,-6,3],[-5,6,-3,-8],[-8,9,8,10],[10,7,1,-2],[6,5,10,5],[6,-1,-4,8],[-7,-9,-7,-4],[8,-4,9,-9],[8,6,9,-3],[7,-6,4,2],[-10,-6,-9,-3],[4,-7,7,-8],[8,-3,9,4],[2,6,3,-7],[10,-10,-6,5],[2,4,8,4],[-8,-2,3,-3],[-7,2,7,-3],[-5,-6,-5,2],[5,-7,-8,8],[8,-2,-8,-7],[-4,-5,8,-9],[-10,-5,-10,-2],[-3,-7,-8,4],[8,8,-1,-1],[3,7,3,-4],[3,-7,6,-7],[8,7,-10,3],[-9,4,-5,-8],[-2,-2,2,-7],[7,9,3,2],[1,-9,-2,-1],[-3,-4,1,-9],[-6,-5,6,5],[-5,-7,-10,10],[-8,-4,-1,-3],[9,5,7,2],[-4,2,-8,5],[1,4,9,-3],[-4,7,-2,-2],[-8,-1,-10,8],[10,5,-7,3],[-2,-9,2,-10],[-9,-4,7,-3],[4,10,7,-9],[8,-8,4,-4],[10,-9,-5,1],[-6,-6,10,10],[3,7,9,-10],[-1,3,10,4],[-9,2,-10,8],[7,-8,3,-10],[-7,-10,-4,5],[-7,-1,-6,-6]], dtype = "uint32")#candidate|1919|(160, 4)|const|uint32
call_1918 = relay.TupleGetItem(func_1383_call(relay.reshape(const_1919.astype('uint32'), [10, 16, 4])), 0)
call_1920 = relay.TupleGetItem(func_1386_call(relay.reshape(const_1919.astype('uint32'), [10, 16, 4])), 0)
uop_1921 = relay.tan(call_1898.astype('float32')) # shape=(10, 9, 3)
uop_1923 = relay.tan(call_1899.astype('float32')) # shape=(10, 9, 3)
bop_1936 = relay.logical_and(uop_1914.astype('bool'), relay.reshape(call_1898.astype('bool'), relay.shape_of(uop_1914))) # shape=(10, 9, 3)
bop_1939 = relay.logical_and(uop_1916.astype('bool'), relay.reshape(call_1899.astype('bool'), relay.shape_of(uop_1916))) # shape=(10, 9, 3)
output = relay.Tuple([call_1918,const_1919,uop_1921,bop_1936,])
output2 = relay.Tuple([call_1920,const_1919,uop_1923,bop_1939,])
func_1940 = relay.Function([], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
output = func_1940()
func_1941 = relay.Function([], output)
mutated_mod['func_1941'] = func_1941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_1964 = relay.TupleGetItem(func_1044_call(), 2)
call_1965 = relay.TupleGetItem(func_1045_call(), 2)
func_1450_call = mod.get_global_var('func_1450')
func_1453_call = mutated_mod.get_global_var('func_1453')
const_1974 = relay.const([-8,-3,-1,9,-1,2,6,9,8,1,-9,8,-6,-7,6,4,2,-6,10,-4,-10,-1,4,4,-1,2,9,-7,6,5,7,-7,5,-5,9,-8,-8,5,10,-6,8,10,-5,4,3,7,-9,1,10,-10,7,-9,-6,7,-8,6,8,-3,5,8,7,7,2,1,-6,-2,-7,-6,-5,-1,-5,-9,3,7,1,5,3,-5,10,8,5,6,10,8,-6,-10,-6,-5,-3,8,-10,-2,-2,1,-3,9,8,1,-9,5,8,8,4,-2,6,9,-2,2,-9,8,-9,-9,2,4,9,-9,-5,-10,8,4,-1,-1,-5,6,3,6,-1,-10,-5,6,-4,-2,10,7,-3,2,-7,6,6,-6,8,-1,-6,-3,5,-8,4,9,-9,4,9,-5,-10,8,5,-3,7,3,6,8,-7,10,4,7,-8,-7,-6,-3,5,2,-9,-6,-10,-2,7,8,6,-9,-9,-8,-7,6,-7,-2,2,4,-1,-8,1,7,-1,4,-3,10,9,-1,-2,2,5,4,9,7,-10,1,6,-9,-1,4,6,-7,1,1,-2,3,-8,3,6,-7,6,6,-4,-6,-10,10,-6,10,3,-3,6,-10,-4,4,-4,6,9,-1,9,-9,-2,4,3,7,7,1,-7,-10,6,1,-6,-2,-1,7,2,8,2,4,-5,-1,1,6,5,-1,1,-2,10,-10,-9,-10,3,-7,-1,-2,1,9,-7,4,-10,-4,-8,7,-2,-9,-6,-4,-9,5,1,6,-3,6,9,-4,4,3,-6,-9,9,-9,-7,7,-3,7,2,-8,8,8,5,-10,2,2,-4,-4,7,10,-6,1,9,-5,-1,7,8,-9,-9,-5,-2,9,-6,-1,-6,-8,-7,-4,-6,9,-2,9,4,-7,8,-4,-9,-8,-5,7,-9,-6,5,-5,8,2,-2,2,-10,-1,-10,-3,-7,1,2,-5,-6,-9,2,-4,8,8,7,-10,-8,-7,5,7,-1,-5,-8,-1,-3,7,-4,6,9,4,6,2,4,-2,7,4,-8,10,1,-4,4,2,2,-10,3,-6,-9,-3,-8,-5,-6,5,-7,-4,8,7,-9,10,8,-4,-5,10,-1,-8,-1,5,1,3,-7,-8,-5,7,-3,-5,6,-4,2,-6,8,-1,8,-6,10,-6,-6,-3,7,-5,6,3,-1,-4,10,5,5,-7,-4,9,2,-2,-10,-9,7,-1,-4,-7,-1,8,-1,9,9,-9,1,-8,5,-1,-8,-4,-4,10,-9,-5,-7,2,-5,6,-1,10,4,4,9,4,10,2,3,4,-8,2,1,7,-7,4,9,9,-2,-3,-10,8,-5,6,4,-9,8,-10,-3,8,4,-9,6,6,-1,-8,-8,-3,-9,-2,-8,5,-10,8,6,5,-8,2,-2,-1,-9,-6,-5,1,-9,-7,2,6,1,-5,-9,-6,5,-2,-6,10,2,-6,8,-1,10,7,-1,6,-6,-6,1,6,10,5,-1,-5,2,9,9,-8,-7,-3,-7,-10,-9,-9,-10,8,-3,8,-7,-8,-4,-8,7,4,-10,-4,-3,9,-1,-4,-3,1,-5,-9,-3,1,4,-2,5,8,-2,-4,5,9,-2,-6,-5,-1,7,-3,9,-10,3,-5,-10,8,5,7,3,-7,6,10,-2,2,-10,-2,8,1,7,-2,1,9,9,-6,-1,-7,-6,-10,7,8,6,-4,5,6], dtype = "uint32")#candidate|1974|(640,)|const|uint32
call_1973 = relay.TupleGetItem(func_1450_call(relay.reshape(const_1974.astype('uint32'), [640,])), 3)
call_1975 = relay.TupleGetItem(func_1453_call(relay.reshape(const_1974.astype('uint32'), [640,])), 3)
bop_1990 = relay.not_equal(call_1973.astype('bool'), relay.reshape(const_1974.astype('bool'), relay.shape_of(call_1973))) # shape=(640,)
bop_1993 = relay.not_equal(call_1975.astype('bool'), relay.reshape(const_1974.astype('bool'), relay.shape_of(call_1975))) # shape=(640,)
var_2013 = relay.var("var_2013", dtype = "uint32", shape = (640,))#candidate|2013|(640,)|var|uint32
bop_2014 = relay.minimum(call_1973.astype('int32'), relay.reshape(var_2013.astype('int32'), relay.shape_of(call_1973))) # shape=(640,)
bop_2017 = relay.minimum(call_1975.astype('int32'), relay.reshape(var_2013.astype('int32'), relay.shape_of(call_1975))) # shape=(640,)
output = relay.Tuple([call_1964,bop_1990,bop_2014,])
output2 = relay.Tuple([call_1965,bop_1993,bop_2017,])
func_2030 = relay.Function([var_2013,], output)
mod['func_2030'] = func_2030
mod = relay.transform.InferType()(mod)
mutated_mod['func_2030'] = func_2030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2031 = relay.var("var_2031", dtype = "uint32", shape = (640,))#candidate|2031|(640,)|var|uint32
func_2030_call = mutated_mod.get_global_var('func_2030')
call_2032 = func_2030_call(var_2031)
output = call_2032
func_2033 = relay.Function([var_2031], output)
mutated_mod['func_2033'] = func_2033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_2081 = func_429_call()
call_2082 = func_429_call()
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_2093 = func_553_call()
call_2094 = func_553_call()
bop_2097 = relay.divide(call_2081.astype('float32'), relay.reshape(call_2093.astype('float32'), relay.shape_of(call_2081))) # shape=(10, 9, 3)
bop_2100 = relay.divide(call_2082.astype('float32'), relay.reshape(call_2094.astype('float32'), relay.shape_of(call_2082))) # shape=(10, 9, 3)
output = bop_2097
output2 = bop_2100
func_2102 = relay.Function([], output)
mod['func_2102'] = func_2102
mod = relay.transform.InferType()(mod)
mutated_mod['func_2102'] = func_2102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2102_call = mutated_mod.get_global_var('func_2102')
call_2103 = func_2102_call()
output = call_2103
func_2104 = relay.Function([], output)
mutated_mod['func_2104'] = func_2104
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_738_call = mutated_mod.get_global_var('func_738')
call_2134 = func_736_call()
call_2135 = func_736_call()
var_2136 = relay.var("var_2136", dtype = "float64", shape = (10, 9, 3))#candidate|2136|(10, 9, 3)|var|float64
bop_2137 = relay.less(call_2134.astype('bool'), relay.reshape(var_2136.astype('bool'), relay.shape_of(call_2134))) # shape=(10, 9, 3)
bop_2140 = relay.less(call_2135.astype('bool'), relay.reshape(var_2136.astype('bool'), relay.shape_of(call_2135))) # shape=(10, 9, 3)
uop_2141 = relay.acosh(call_2134.astype('float32')) # shape=(10, 9, 3)
uop_2143 = relay.acosh(call_2135.astype('float32')) # shape=(10, 9, 3)
bop_2144 = relay.bitwise_and(uop_2141.astype('int32'), relay.reshape(bop_2137.astype('int32'), relay.shape_of(uop_2141))) # shape=(10, 9, 3)
bop_2147 = relay.bitwise_and(uop_2143.astype('int32'), relay.reshape(bop_2140.astype('int32'), relay.shape_of(uop_2143))) # shape=(10, 9, 3)
output = relay.Tuple([bop_2144,])
output2 = relay.Tuple([bop_2147,])
func_2179 = relay.Function([var_2136,], output)
mod['func_2179'] = func_2179
mod = relay.transform.InferType()(mod)
mutated_mod['func_2179'] = func_2179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2180 = relay.var("var_2180", dtype = "float64", shape = (10, 9, 3))#candidate|2180|(10, 9, 3)|var|float64
func_2179_call = mutated_mod.get_global_var('func_2179')
call_2181 = func_2179_call(var_2180)
output = call_2181
func_2182 = relay.Function([var_2180], output)
mutated_mod['func_2182'] = func_2182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_2238 = func_1207_call()
call_2239 = func_1207_call()
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
var_2248 = relay.var("var_2248", dtype = "uint32", shape = (126, 1))#candidate|2248|(126, 1)|var|uint32
call_2247 = relay.TupleGetItem(func_530_call(relay.reshape(var_2248.astype('uint32'), [126,])), 0)
call_2249 = relay.TupleGetItem(func_533_call(relay.reshape(var_2248.astype('uint32'), [126,])), 0)
var_2256 = relay.var("var_2256", dtype = "uint32", shape = (126, 12))#candidate|2256|(126, 12)|var|uint32
bop_2257 = relay.less_equal(var_2248.astype('bool'), var_2256.astype('bool')) # shape=(126, 12)
output = relay.Tuple([call_2238,call_2247,bop_2257,])
output2 = relay.Tuple([call_2239,call_2249,bop_2257,])
func_2260 = relay.Function([var_2248,var_2256,], output)
mod['func_2260'] = func_2260
mod = relay.transform.InferType()(mod)
mutated_mod['func_2260'] = func_2260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mutated_mod.get_global_var('func_2260')
var_2262 = relay.var("var_2262", dtype = "uint32", shape = (126, 1))#candidate|2262|(126, 1)|var|uint32
var_2263 = relay.var("var_2263", dtype = "uint32", shape = (126, 12))#candidate|2263|(126, 12)|var|uint32
call_2261 = func_2260_call(var_2262,var_2263,)
output = call_2261
func_2264 = relay.Function([var_2262,var_2263,], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2280 = relay.const([[[1.016711,-3.653366,-3.203263,6.425325,-3.188922,1.040486,2.794253,7.266547,0.783629,6.639573,3.720368,8.642245,2.236275,-6.158901,3.537938,-1.683568],[1.928539,2.265621,3.436271,9.263420,-1.317585,2.879160,-3.399394,-9.033369,-8.041191,8.841971,6.180453,1.400930,0.910480,2.766104,-0.714524,-7.115927],[-1.476531,0.429953,-2.059863,6.232462,3.059610,-4.293672,-4.817904,4.083436,-3.328976,-1.419715,-1.293283,-2.496694,5.626489,-9.550897,4.516672,3.980413],[-4.453940,-1.696125,4.833608,5.236938,-5.063552,-7.032873,-9.858757,5.310873,8.278619,9.466161,-9.879559,6.724851,8.837746,4.850073,-9.884111,-9.115883],[3.879114,6.223907,-6.142193,8.008443,-8.512105,8.304023,9.802039,5.964374,8.453850,-5.637913,2.623828,7.925267,7.541956,5.562203,-9.346046,-6.624460],[-8.296887,-7.450101,0.008240,3.420357,-8.273307,-7.795897,-8.480762,-1.776862,-0.160400,5.944616,-6.313030,-6.716061,2.794495,-4.536141,0.030194,4.536709],[-5.415733,7.585934,5.428687,-6.293489,6.953251,0.044308,-4.986345,0.866900,1.273708,-3.534549,-7.053831,2.542035,1.379912,6.617723,2.117944,-1.524382],[-3.295911,2.038787,1.245324,4.441680,-8.967823,-4.821825,-2.788896,-2.728437,-0.105043,-4.681459,7.533246,-4.180113,6.444199,-8.221116,-7.470012,-3.003774],[-5.065686,-1.318247,1.897305,-9.419442,-0.188827,9.649540,0.726297,-9.677436,-2.353817,-9.656448,2.114519,-4.386698,-1.774351,7.887770,-3.153214,5.678443]],[[2.085749,-1.586677,-3.619399,-1.485160,1.354482,1.081565,2.999258,-3.529823,-8.794444,-2.090928,8.506182,-7.313402,6.869292,-6.326765,-5.692136,-2.160730],[0.952957,-0.117181,9.433998,-5.555933,-2.082409,3.841442,-2.619440,-7.936259,-1.153707,-4.602447,4.675259,9.383183,-8.678750,-6.844728,-2.850976,-2.052326],[6.966738,8.973469,1.028426,2.249301,1.112038,-5.835993,-1.543378,0.803470,5.167249,-9.423875,-2.194615,2.896064,8.116297,5.142913,-8.339836,9.361958],[6.524581,-7.202968,7.271155,-8.522725,4.479730,-7.218367,3.937046,-8.967733,6.019216,-9.987089,4.472090,-9.437135,2.996742,-8.933318,5.967238,-3.793522],[-8.854541,9.804099,-2.420782,-8.040122,-3.981572,-6.286713,-7.582993,-3.424663,7.627266,-3.007967,-3.364826,-7.034924,-5.633363,4.460065,-6.992396,-5.040217],[2.081066,-8.400440,-6.323462,2.322148,8.667647,-9.040403,-7.969033,7.850303,8.647374,-0.190352,-1.727040,-8.038823,7.943811,-4.935377,6.965470,-4.783226],[4.472122,-0.695391,-7.974964,-4.984242,0.933306,7.412955,-3.724473,-7.706036,-6.492942,5.623573,8.501268,-3.096202,-9.480628,-4.906718,1.340783,-7.828211],[-6.511284,-4.528683,-5.741800,-8.851644,-0.175656,3.702470,6.312047,-3.579947,5.262264,-0.956930,9.062369,0.135585,-8.420663,4.580810,1.634335,-6.184358],[3.076103,-7.029891,3.270320,1.470610,-9.749405,-4.559886,-6.528189,-6.112654,4.922973,-5.471862,7.767524,-1.137147,-9.763129,7.548481,7.985469,2.332953]],[[4.761340,-9.338280,-5.457401,-0.651787,-6.013516,-8.879264,3.989641,-6.378239,-9.229189,-2.155130,3.609804,2.537597,-8.506288,6.485979,-0.365927,-8.923056],[-6.064009,-3.217994,9.589322,8.803232,-8.696180,-5.155472,-7.059569,-5.592109,-1.532812,-2.804156,7.428490,5.555698,8.780117,6.596571,3.918760,9.489213],[-1.217243,-6.823521,-5.858266,3.914874,-6.110002,-5.208413,2.893217,4.751708,1.847191,4.902606,2.709214,6.013413,4.511712,-7.365026,-4.240071,-1.092916],[5.164599,-2.002242,-2.489567,-0.825782,-1.008776,-2.629752,6.054956,1.776459,0.322914,7.086671,4.043985,6.362647,2.959373,8.212418,3.235838,-3.509756],[-3.655874,-9.089160,1.660229,4.313142,-2.503126,1.474659,3.537842,-7.001878,0.659187,3.840655,-3.191961,8.205762,-5.409747,-7.291213,-3.997461,1.158654],[8.375957,1.571096,-6.337944,-7.605931,-0.086737,7.792638,-2.804177,9.684452,6.426722,-8.120363,4.039965,-1.850456,-2.943450,-4.958191,6.817787,-2.653427],[8.454895,8.476466,-8.330993,-6.431357,5.890086,6.535523,-7.737767,4.301650,4.933046,8.936997,1.454853,9.801283,-9.997817,-1.395184,1.304344,2.528658],[2.486199,-7.558953,-5.113923,-9.080357,-4.182944,-4.500112,-7.802938,9.320838,4.513818,0.570273,-8.785417,0.557805,-9.641429,-4.070040,-4.721410,-4.166395],[0.407577,0.579957,-2.639140,6.160414,3.725732,5.528783,-3.800265,-0.723321,8.750679,-1.172651,-3.163032,2.972032,-5.250456,-6.860026,0.438127,-1.768270]],[[4.126592,-6.789066,5.485035,5.679974,4.300162,7.572447,6.151649,-7.516476,4.938946,-8.719430,-5.215567,-4.347514,4.896400,2.889972,4.295075,0.156540],[6.115480,-9.590183,-2.496779,-1.810883,-8.172824,4.703434,7.081689,0.808994,-8.421878,-0.623726,2.706786,0.565194,5.134689,4.392885,-9.439130,2.414779],[-2.230981,6.000653,3.092745,5.124653,8.851394,3.615259,-7.561409,2.238247,-6.096821,1.275094,-4.922639,7.438136,2.013160,-4.325995,7.634137,2.415237],[-7.347871,-2.520097,-1.018526,1.126354,-5.339296,-2.073561,1.891403,-1.984476,5.683340,7.924994,-7.788506,6.636381,0.486349,-5.816450,-1.653256,1.540865],[-3.859128,-1.086879,7.586535,-9.423640,4.912705,-9.191216,-3.647862,-8.409004,-5.325229,2.530653,-5.330999,-0.087419,-6.335325,5.199173,-2.404826,7.005071],[-9.693776,-7.541069,-0.498828,-2.604331,2.581425,-0.680507,3.034544,-7.233113,3.190538,-0.539715,-6.675094,0.667880,1.105664,3.061850,3.974836,-2.022968],[9.488859,5.225555,8.522434,8.984979,-9.769948,-5.567566,-7.412749,5.761029,-3.148407,-0.438337,-0.465263,-5.985204,-3.410959,-4.743982,-9.760785,7.016861],[1.805789,8.062775,-7.962740,8.264509,3.028020,-7.744892,-2.621934,6.215241,-4.909241,-8.212515,1.638840,-3.737111,-8.505809,-8.662603,-4.978535,-0.924239],[-5.738010,-9.935002,-4.778563,-5.363710,-4.452948,-6.994945,-9.012538,8.058312,2.948537,-8.790924,-9.503448,-0.533236,2.219960,-0.570858,-5.635400,1.398068]],[[-1.549525,-0.877503,6.572910,-7.256566,9.803441,4.192036,-7.571257,-4.010327,-3.710265,8.765568,-9.665851,7.340710,-2.311984,6.879639,2.665228,1.314235],[-6.413470,-0.938965,-9.341285,1.096354,7.761729,-7.608774,-8.163060,7.350880,3.138126,8.400855,-7.220252,2.262195,-4.123702,-4.601854,8.273062,-5.622989],[5.876161,4.304484,3.914618,3.761250,0.381602,4.896934,4.222207,-6.432236,4.862866,-3.421048,9.303290,-5.889008,-8.218959,7.391423,-0.016978,4.950017],[-9.767092,-5.540091,-1.619520,2.166263,3.754666,0.035514,4.388788,8.530002,8.663173,2.319859,4.802045,3.595388,-5.797534,5.539983,-0.163861,-1.248899],[3.550385,-6.243498,-0.568034,-6.509774,-6.267496,-3.460954,9.384762,-4.905661,2.832795,1.779993,6.981831,-6.856739,6.559422,4.356475,8.967022,2.446423],[-9.948634,-2.069911,6.237407,-6.110477,-5.531747,1.016601,-2.456467,-7.517927,5.740851,-8.409201,-7.520476,-2.546616,-9.184684,8.794790,2.648750,-7.479419],[3.321005,3.571329,9.184411,-7.276370,-7.051742,-5.646332,-5.426398,4.301261,-4.277525,-4.198380,-1.935233,3.466176,-8.245627,-8.854676,4.757364,6.824909],[0.666730,7.568006,-4.449770,-7.333731,4.184446,4.186024,-2.097612,-5.953849,-7.297551,7.980539,2.793936,6.515708,-6.891542,-0.673205,7.804316,-2.211932],[-0.665093,6.860727,6.876657,8.404240,-4.097082,-2.268732,6.296868,-2.162860,-0.176702,2.059506,-6.541175,4.294522,-7.589615,-6.458867,-0.394811,6.131376]],[[-8.100813,8.065043,-5.550858,-2.090436,-8.877230,3.709809,5.488424,0.412650,-3.976390,-9.623883,-8.970742,7.708499,6.569275,-0.725337,-6.800388,-5.381405],[-2.008473,-5.526106,-9.761764,-3.097797,-5.860073,4.187365,4.186342,9.423288,1.816111,-7.424432,0.452371,-6.977916,7.034751,-8.935840,-3.361191,-9.142405],[2.610955,-9.947125,5.679145,-6.043261,-9.640674,-8.221249,-0.635051,6.231551,7.492771,4.493315,8.696378,1.196906,-3.148060,-9.939146,-2.257814,-7.928957],[-4.776647,1.105628,4.183730,7.103275,1.979820,6.517308,6.424075,4.203228,-6.184440,4.431576,7.460676,-3.014512,4.759756,-8.697247,3.616188,0.068147],[3.918623,9.684992,-7.177764,6.547013,-2.822983,5.385802,7.138685,-7.512015,-1.186224,-8.088643,-7.854153,5.078318,5.456075,2.744932,-0.803134,-9.675383],[-7.807590,-6.019258,-6.191477,-0.625652,-3.490772,-7.997180,8.459602,6.446724,8.175543,9.756450,-3.702794,1.841560,-0.442706,-4.475983,8.545740,3.881602],[8.759349,-0.486602,1.524680,-2.559663,-1.927467,0.488810,-4.037107,9.638989,-2.609501,8.538266,-3.920964,2.427008,-1.012046,8.081085,-2.063457,6.524694],[9.674250,-7.877802,-2.700323,-3.191195,3.267400,-8.488251,8.240446,7.491807,-9.256342,-4.886605,7.996081,-4.987199,-5.591932,0.216869,-2.752721,-9.980107],[-0.729979,-3.585881,9.437990,-9.137577,-4.732164,-3.926518,-7.639963,-9.195052,4.514586,4.828197,-8.266241,-6.992193,-9.784247,9.927178,-7.749258,-1.608324]]], dtype = "float32")#candidate|2280|(6, 9, 16)|const|float32
var_2281 = relay.var("var_2281", dtype = "float32", shape = (6, 9, 16))#candidate|2281|(6, 9, 16)|var|float32
bop_2282 = relay.power(const_2280.astype('float32'), relay.reshape(var_2281.astype('float32'), relay.shape_of(const_2280))) # shape=(6, 9, 16)
output = relay.Tuple([bop_2282,])
output2 = relay.Tuple([bop_2282,])
func_2291 = relay.Function([var_2281,], output)
mod['func_2291'] = func_2291
mod = relay.transform.InferType()(mod)
mutated_mod['func_2291'] = func_2291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2292 = relay.var("var_2292", dtype = "float32", shape = (6, 9, 16))#candidate|2292|(6, 9, 16)|var|float32
func_2291_call = mutated_mod.get_global_var('func_2291')
call_2293 = func_2291_call(var_2292)
output = call_2293
func_2294 = relay.Function([var_2292], output)
mutated_mod['func_2294'] = func_2294
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2371 = relay.const([[[-5.596024,-8.624017,-5.749477,2.012457,-9.278167,7.430972,4.729181,9.982981,5.864544],[-7.332308,9.875441,-9.833237,-2.967433,7.014463,-7.987867,-0.307698,-3.869099,7.382328],[-0.738854,-9.267453,-9.285753,-9.992791,-8.409148,2.569597,5.693559,-9.659038,8.239502],[1.370293,-6.255581,7.638887,7.815311,1.681319,4.363743,-0.021368,6.023729,-3.732161],[-0.696086,5.763652,-7.012036,6.518748,-4.036900,3.262494,-4.586682,-5.917814,2.324387],[1.968099,4.573008,-9.660537,-2.741166,7.940546,6.386823,3.227763,-2.660667,-0.462604],[2.452159,6.445722,-8.230069,0.905559,1.795510,3.962455,-3.807736,-8.097966,6.225620],[-7.451406,3.649276,0.682911,7.177603,5.132404,1.016584,4.046928,1.765631,-0.554321]],[[3.833682,-6.752564,3.035448,4.007978,-4.964235,-2.948098,-9.457705,3.918462,-6.632908],[-8.662290,1.056655,5.231834,4.033901,-7.164661,4.733464,-7.701974,-0.878532,-7.148394],[-1.498049,6.387394,6.316327,-8.884433,-6.817030,8.845239,-6.624695,4.694347,0.527482],[-2.157925,4.319223,0.888718,-3.032099,0.955324,-5.552685,-0.376938,0.646772,-9.619365],[3.833010,-7.522143,-8.982155,-1.804037,9.535183,1.975396,1.181180,5.593960,-2.165351],[5.511699,5.363552,8.549151,-7.507247,-2.154493,-6.533649,-5.191281,-7.839568,0.842881],[7.696031,0.793881,9.631694,9.341406,1.053173,2.361096,-9.165574,-1.856282,5.102601],[6.361153,5.769333,8.381001,-2.367817,-4.467729,-8.389558,-6.094162,5.211906,-8.148850]],[[-2.588388,6.468612,8.539957,6.174961,-3.065797,4.152411,3.270846,4.469157,-5.656251],[-7.838640,7.099295,4.952600,7.979773,4.770531,-2.435091,8.164115,4.720706,-1.518773],[-7.489131,-9.014552,7.224434,-6.176119,8.902769,5.826297,8.671099,-1.242802,-1.205905],[-8.127405,1.228566,8.371597,-4.381293,-3.885211,9.739017,-5.888123,-8.853934,-5.871239],[-0.793774,0.885199,5.144419,0.944112,-8.663627,9.097069,-6.903799,-0.083208,0.102490],[0.632414,9.825887,9.464369,-4.246577,-7.310826,5.949236,-3.266371,5.349352,9.099665],[-9.620693,1.578186,-5.246942,-7.121871,7.367536,8.748888,-9.450391,-2.151434,-1.320124],[-8.401256,8.106499,-9.412873,-0.263362,-0.599420,-2.067380,-3.593056,-0.746680,0.114975]],[[-8.285942,1.742838,1.289249,-2.006909,6.912812,6.956138,-5.984563,-8.271011,-2.199191],[-9.899052,9.685314,-2.813463,-1.693774,0.432260,8.838713,-3.075370,-5.465383,6.608088],[-4.277241,7.991086,-3.387057,2.568499,-3.517259,-5.103533,-3.011638,3.898042,7.715480],[3.570753,-3.053186,-5.026325,-5.288391,6.238435,4.888412,-1.321843,-6.628694,8.721694],[-0.484888,-6.994197,2.963844,0.901785,1.092729,9.715668,-8.583375,6.717047,5.898191],[-0.623100,-4.081149,-7.115210,-4.140525,2.570107,-8.339122,6.697291,3.261119,-1.687985],[-7.555375,2.972513,-7.444004,-8.666957,7.141305,-9.632712,-0.272811,-4.477057,-3.568339],[-8.056962,4.302599,-8.083953,-0.230049,-8.389600,8.092329,-3.120638,-7.722543,3.878415]],[[3.181146,-2.684022,5.379192,1.498403,8.264952,-5.780128,7.878527,8.676033,-2.276752],[-3.213899,0.646054,7.874972,7.284951,6.447995,9.628145,7.092593,-4.940815,0.569930],[-9.035751,7.447586,5.193432,7.777862,-1.162712,0.668759,-7.476812,-5.632610,4.878911],[-7.830923,7.016878,-8.468664,4.237239,5.327928,3.380927,7.292544,-1.168380,-3.265796],[5.117796,-0.893186,-6.763243,-7.191791,4.411288,-0.307862,-3.392507,-9.553751,-8.314357],[-5.163583,-9.449894,-7.745590,5.821695,4.088527,-1.146579,7.609772,5.396864,-5.979005],[7.804180,7.919786,2.149576,9.850723,-2.657280,7.074561,1.758459,-1.018366,-4.786397],[8.920304,6.762605,0.985257,-4.294425,1.815179,-9.313755,5.066510,-2.605598,-2.650218]],[[3.345383,-3.539093,8.410935,-2.706739,7.754056,-6.175098,4.025121,9.944109,-0.648443],[4.118485,1.248047,4.042452,-3.423426,-5.460177,2.899913,-8.176878,-9.327311,-3.048348],[-8.393630,-5.260064,-4.339684,0.050781,9.263244,-4.070809,3.206942,-9.754029,-3.203474],[-5.916744,6.107753,3.070721,-6.865961,6.563411,-6.405439,-5.484057,-7.024673,9.343952],[-5.261052,4.878345,8.194013,1.581223,5.548913,-1.401431,4.445645,-3.145729,8.461020],[3.773354,9.166325,-6.148834,9.001309,-8.697337,-2.362167,-9.653161,9.079172,-0.744374],[7.945267,3.708587,3.713270,-4.171343,0.466248,9.316204,-7.690186,-9.854427,4.726734],[-1.046295,4.147305,1.116106,-7.044387,-8.176267,9.591034,-7.480894,9.569172,8.289633]],[[3.650482,3.172390,-2.946923,6.837770,-2.487799,-4.942062,3.081480,-3.620123,3.723346],[-6.031050,1.921717,2.646056,8.134152,4.607701,-0.276768,0.750355,-8.928214,-7.427646],[-4.905166,4.678225,2.595878,-8.625352,-0.631404,7.337742,-9.839145,9.423466,6.684196],[-0.172765,2.356147,7.581744,-6.691608,2.622106,6.672556,9.173864,-7.903821,-2.543233],[-3.892840,-6.862874,5.006238,2.588775,0.933679,3.213723,6.862505,8.998171,9.078569],[-1.050608,5.994493,-1.775613,4.527641,-5.761705,6.605682,7.359368,-2.672681,-3.275833],[-1.633377,5.640399,3.937349,-5.610469,8.262772,3.735463,-2.343023,-6.232690,0.239547],[-6.497252,0.568571,-8.840169,-1.813683,-0.410807,8.966726,-7.597376,-8.035955,7.009565]],[[8.083753,7.229202,8.230993,4.243310,-3.323906,-2.466267,4.561465,3.672331,4.744315],[4.456094,9.638978,-5.306991,-0.401716,-0.879686,9.262019,-4.460793,5.161527,9.761103],[-2.606575,-9.203424,-3.900252,8.893037,-2.207057,-0.071336,-6.908961,3.096198,-1.820745],[5.539828,-1.945336,8.812266,0.501030,-8.668026,8.661109,-6.828918,0.439939,0.973348],[9.362839,2.498151,1.639438,4.813970,9.126373,0.303764,7.870936,-3.500494,9.538870],[5.521688,-4.140368,7.544860,3.481535,0.400306,2.802667,-7.733405,7.226392,-6.003392],[-6.573102,0.549552,-1.695522,3.103370,2.399691,7.660929,9.462322,4.000318,1.007585],[-1.339263,-1.679014,1.268968,-1.042053,-1.986537,8.406049,-6.488483,6.094223,8.092775]],[[-7.670459,3.206895,-2.983615,-2.885062,2.268224,4.359058,5.666569,8.836570,-6.678838],[2.954801,-9.255777,-2.008996,-3.710864,3.402701,-0.605718,2.867296,3.258947,-1.576055],[5.179503,-9.618860,0.205968,0.774424,2.959813,-0.365795,0.418630,-9.266803,-4.207687],[5.280500,3.888561,-9.614692,9.120045,-3.625687,-2.644148,3.771258,-3.971730,-7.813037],[0.331155,-2.063063,-5.288231,-7.357728,-1.265671,4.666133,-0.196283,0.787832,-6.892809],[5.504464,9.001598,-5.716975,3.107340,1.741031,2.354484,8.400449,-2.040225,5.943242],[-7.223540,-9.226362,-4.479975,6.618175,3.594427,-6.727024,-7.058812,1.298799,-1.522949],[2.861106,6.304037,3.526463,-5.917951,-9.792467,-4.903903,0.141658,2.525951,7.147633]],[[-0.273918,-8.750518,7.594230,5.264249,0.780318,3.991580,-6.710832,6.347068,0.811670],[8.610675,1.725151,-3.233424,8.351244,-9.876941,-0.451515,1.628131,6.191750,-6.491907],[-3.772870,-9.739152,-0.408366,8.947396,1.552389,5.076703,0.692035,-2.166719,-3.608008],[-6.280534,5.172698,-4.528536,-3.245381,-6.980101,-4.736138,-5.491705,-6.697559,-7.375493],[-6.725953,2.751322,-8.672458,8.315445,3.174578,-2.425651,-0.293140,-6.787114,6.009769],[5.606398,-4.842462,2.979984,-7.383804,9.764455,5.663234,-8.908941,-7.302792,0.553140],[-3.559112,-0.344693,-1.886957,1.610020,-7.661848,-4.424814,-7.488199,8.435511,5.778693],[9.611480,9.856215,-6.532322,-6.083207,-2.469328,0.415467,2.880626,-7.993195,1.181242]],[[-9.468694,-2.653756,-1.129064,0.487435,-2.950138,7.904547,5.071515,-0.798842,-1.096252],[4.527340,1.331482,6.757248,4.430283,-4.060641,-3.820695,8.886445,-6.975493,9.541894],[-6.923998,2.074990,-3.213326,9.166436,-4.920903,-3.163858,-5.846163,1.439309,4.586554],[-0.720560,-1.740883,4.171354,8.464717,2.834743,-2.903042,-4.951358,1.540486,0.287015],[2.371215,-5.854181,-8.358297,-3.329013,-3.338818,-3.592073,-4.550594,1.093609,7.132792],[1.226638,3.913714,-2.786501,-0.450352,-5.509257,3.953973,1.197294,-9.993820,-0.356031],[-4.280896,-5.298219,-2.068034,-4.660878,8.445532,7.993104,-1.172398,4.279928,-1.753697],[0.628680,0.528501,-0.689347,-2.976421,7.711925,3.454480,0.988245,-9.520975,5.581135]],[[9.953876,0.030291,4.415250,8.332187,9.658135,6.816915,2.579511,-8.963317,-8.892654],[8.452124,-7.458685,-8.441286,-3.050573,0.203806,5.705627,9.705280,7.390344,8.130459],[-2.698766,-4.058967,-6.096239,2.599846,3.397805,-1.751757,-4.500213,-7.917965,-6.977841],[1.644584,-3.139853,9.744246,9.441389,-0.038395,3.924588,7.160116,6.297190,0.850129],[8.195867,2.107342,8.977258,-8.389667,6.282869,-5.047069,3.779256,-4.272174,3.299493],[4.592252,-7.581966,4.578112,-6.904708,1.160760,-0.233526,3.264414,3.072396,-1.554592],[-4.628483,0.898176,2.741125,1.066294,3.117860,1.052457,0.187963,2.511685,-3.560616],[7.960075,2.193365,-3.283512,1.930654,7.663210,-2.500165,2.245618,-5.242235,-1.128259]],[[6.437831,4.387263,5.016740,3.211429,5.625064,8.116674,0.571847,-6.156692,2.982262],[-4.638937,-8.532351,-1.413766,-5.592351,2.244303,-1.394415,-7.418816,1.737590,-0.767578],[-1.616888,2.886333,-0.197334,-7.217776,6.321939,-4.971317,9.880253,-6.155311,-4.964743],[6.774530,-4.472106,0.792958,-0.185284,-3.183719,9.311589,2.471800,-7.049422,-3.744062],[6.008697,-5.579971,7.591804,2.972666,-4.769353,1.915836,-2.341723,9.653819,7.630081],[0.710891,-3.887050,-3.131669,-1.531864,-8.148520,-0.957128,6.960984,4.782704,6.140535],[-9.846767,1.478968,-4.885945,4.199561,9.307394,7.348725,-2.980746,3.624626,7.956086],[-0.745528,1.239527,-6.945015,8.103279,9.587708,-3.667345,-7.019032,6.642815,5.460926]],[[-3.580644,1.754337,6.170195,-8.891022,0.977045,-7.205021,6.585517,9.494711,2.047562],[8.892970,6.683778,7.724918,2.923311,6.583429,-5.644005,-2.128889,6.067023,-5.796921],[-7.001398,-4.337457,-5.026285,-0.712424,-1.874246,-1.628474,-8.099240,-8.185300,-8.419703],[7.127207,8.958358,5.678409,2.150366,-8.771041,3.754904,1.255382,-7.473272,9.783356],[-5.903554,-1.901281,1.869185,5.501203,-7.658434,-6.472971,1.445465,-6.314838,-7.033312],[-6.033686,4.973531,-3.222191,-0.199602,6.315665,-0.151644,0.320709,-7.524006,0.085622],[9.621320,8.638008,-5.415435,-1.223565,9.588737,3.569753,-7.864909,5.380379,-2.553970],[-0.451151,9.468220,6.544745,7.347049,8.460587,8.522273,8.467491,2.354853,-8.229307]],[[-9.682766,8.207397,-3.413008,7.545001,1.671780,-0.836791,4.687036,-7.514373,-2.556234],[-7.778045,-2.390794,-5.051888,-7.284904,-3.691491,-1.286027,0.433872,-1.596788,8.375138],[3.605786,1.541006,6.261054,6.011813,6.296989,-4.650347,6.235053,2.142744,-6.098195],[8.033616,8.827000,-7.191841,5.201659,4.530543,-7.134203,-2.052124,4.754883,-3.805374],[2.907272,1.293113,1.708068,8.259061,-1.519539,6.246610,-0.984966,1.518095,-3.183102],[2.400109,-6.950525,9.495137,0.468908,-4.680647,-1.493149,-4.990093,-4.799389,-1.033924],[9.713186,9.769354,-0.786445,-3.973659,8.250261,-7.157271,0.916428,1.222333,-2.011425],[-5.282472,-5.611501,5.504530,-3.170663,6.752659,4.641376,-5.645058,9.260507,0.660577]]], dtype = "float64")#candidate|2371|(15, 8, 9)|const|float64
var_2372 = relay.var("var_2372", dtype = "float64", shape = (15, 8, 9))#candidate|2372|(15, 8, 9)|var|float64
bop_2373 = relay.power(const_2371.astype('float64'), relay.reshape(var_2372.astype('float64'), relay.shape_of(const_2371))) # shape=(15, 8, 9)
output = relay.Tuple([bop_2373,])
output2 = relay.Tuple([bop_2373,])
func_2376 = relay.Function([var_2372,], output)
mod['func_2376'] = func_2376
mod = relay.transform.InferType()(mod)
var_2377 = relay.var("var_2377", dtype = "float64", shape = (15, 8, 9))#candidate|2377|(15, 8, 9)|var|float64
output = func_2376(var_2377)
func_2378 = relay.Function([var_2377], output)
mutated_mod['func_2378'] = func_2378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1099_call = mod.get_global_var('func_1099')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_2390 = relay.TupleGetItem(func_1099_call(), 0)
call_2391 = relay.TupleGetItem(func_1101_call(), 0)
output = relay.Tuple([call_2390,])
output2 = relay.Tuple([call_2391,])
func_2400 = relay.Function([], output)
mod['func_2400'] = func_2400
mod = relay.transform.InferType()(mod)
mutated_mod['func_2400'] = func_2400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2400_call = mutated_mod.get_global_var('func_2400')
call_2401 = func_2400_call()
output = call_2401
func_2402 = relay.Function([], output)
mutated_mod['func_2402'] = func_2402
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2473 = relay.var("var_2473", dtype = "float64", shape = (5, 9, 7))#candidate|2473|(5, 9, 7)|var|float64
uop_2474 = relay.cos(var_2473.astype('float64')) # shape=(5, 9, 7)
output = relay.Tuple([uop_2474,])
output2 = relay.Tuple([uop_2474,])
func_2480 = relay.Function([var_2473,], output)
mod['func_2480'] = func_2480
mod = relay.transform.InferType()(mod)
var_2481 = relay.var("var_2481", dtype = "float64", shape = (5, 9, 7))#candidate|2481|(5, 9, 7)|var|float64
output = func_2480(var_2481)
func_2482 = relay.Function([var_2481], output)
mutated_mod['func_2482'] = func_2482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_2546 = relay.TupleGetItem(func_1044_call(), 0)
call_2547 = relay.TupleGetItem(func_1045_call(), 0)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_2564 = func_1207_call()
call_2565 = func_1207_call()
func_822_call = mod.get_global_var('func_822')
func_824_call = mutated_mod.get_global_var('func_824')
const_2578 = relay.const([[-4,-3,-10,-5,-8,1],[1,8,-4,2,-7,-9],[-9,-1,-9,-5,6,5],[5,-4,-7,7,-4,9],[1,-7,-2,-9,7,9],[9,-2,3,2,9,1],[2,6,-4,-3,-6,5],[9,8,-4,-4,10,9],[-5,-3,8,10,3,-3],[1,-4,-6,-7,-5,-3],[-4,3,4,9,-4,4],[8,9,2,-8,9,1],[3,2,-7,-6,-1,8],[2,7,-2,5,4,1],[7,8,1,3,1,1],[-10,10,-7,-9,6,4],[-6,7,-4,-4,8,-7],[3,-5,5,4,-3,9],[1,-9,-3,-4,-2,8],[7,-7,6,-6,-5,-5],[6,-6,-2,-9,2,-1]], dtype = "uint32")#candidate|2578|(21, 6)|const|uint32
call_2577 = relay.TupleGetItem(func_822_call(relay.reshape(const_2578.astype('uint32'), [126,])), 3)
call_2579 = relay.TupleGetItem(func_824_call(relay.reshape(const_2578.astype('uint32'), [126,])), 3)
output = relay.Tuple([call_2546,call_2564,call_2577,const_2578,])
output2 = relay.Tuple([call_2547,call_2565,call_2579,const_2578,])
func_2589 = relay.Function([], output)
mod['func_2589'] = func_2589
mod = relay.transform.InferType()(mod)
mutated_mod['func_2589'] = func_2589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mutated_mod.get_global_var('func_2589')
call_2590 = func_2589_call()
output = call_2590
func_2591 = relay.Function([], output)
mutated_mod['func_2591'] = func_2591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2591_call = mutated_mod.get_global_var('func_2591')
call_2618 = relay.TupleGetItem(func_2589_call(), 2)
call_2619 = relay.TupleGetItem(func_2591_call(), 2)
func_2179_call = mod.get_global_var('func_2179')
func_2182_call = mutated_mod.get_global_var('func_2182')
var_2624 = relay.var("var_2624", dtype = "float64", shape = (30, 9))#candidate|2624|(30, 9)|var|float64
call_2623 = relay.TupleGetItem(func_2179_call(relay.reshape(var_2624.astype('float64'), [10, 9, 3])), 0)
call_2625 = relay.TupleGetItem(func_2182_call(relay.reshape(var_2624.astype('float64'), [10, 9, 3])), 0)
uop_2646 = relay.sinh(var_2624.astype('float32')) # shape=(30, 9)
output = relay.Tuple([call_2618,call_2623,uop_2646,])
output2 = relay.Tuple([call_2619,call_2625,uop_2646,])
func_2649 = relay.Function([var_2624,], output)
mod['func_2649'] = func_2649
mod = relay.transform.InferType()(mod)
mutated_mod['func_2649'] = func_2649
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2650 = relay.var("var_2650", dtype = "float64", shape = (30, 9))#candidate|2650|(30, 9)|var|float64
func_2649_call = mutated_mod.get_global_var('func_2649')
call_2651 = func_2649_call(var_2650)
output = call_2651
func_2652 = relay.Function([var_2650], output)
mutated_mod['func_2652'] = func_2652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2102_call = mod.get_global_var('func_2102')
func_2104_call = mutated_mod.get_global_var('func_2104')
call_2864 = func_2102_call()
call_2865 = func_2102_call()
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_2876 = relay.TupleGetItem(func_703_call(), 0)
call_2877 = relay.TupleGetItem(func_705_call(), 0)
func_1173_call = mod.get_global_var('func_1173')
func_1174_call = mutated_mod.get_global_var('func_1174')
call_2890 = relay.TupleGetItem(func_1173_call(), 0)
call_2891 = relay.TupleGetItem(func_1174_call(), 0)
output = relay.Tuple([call_2864,call_2876,call_2890,])
output2 = relay.Tuple([call_2865,call_2877,call_2891,])
func_2893 = relay.Function([], output)
mod['func_2893'] = func_2893
mod = relay.transform.InferType()(mod)
output = func_2893()
func_2894 = relay.Function([], output)
mutated_mod['func_2894'] = func_2894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_2900 = relay.TupleGetItem(func_703_call(), 0)
call_2901 = relay.TupleGetItem(func_705_call(), 0)
const_2904 = relay.const([[[-3.357576,5.737884,8.170729],[0.903639,5.103628,0.865956],[-5.950118,-4.527327,4.808460],[-4.136675,-2.722427,-9.401376],[2.107843,-8.609926,-6.573941],[9.733627,6.413228,6.031530],[-7.380431,-8.865453,1.076866],[7.690279,3.560721,1.338573],[5.220321,1.298778,1.536746]],[[4.452572,3.948960,-4.669961],[-5.789973,-8.469789,-8.827726],[-2.460376,-9.900267,-1.451076],[6.507892,8.728049,-4.637508],[7.464424,-2.303550,3.404717],[-9.129535,-1.065748,-6.044932],[9.219247,-8.724705,7.543107],[-0.030794,-4.660735,-6.223720],[-9.824007,-2.794838,-2.321751]],[[-4.313885,9.581257,-2.885927],[7.240617,5.133239,-7.740013],[-2.172592,-1.561744,7.348804],[6.027411,-1.904029,-2.783443],[9.892673,-3.746932,-5.728417],[-8.719591,-3.583533,6.380895],[-8.750347,6.556736,-4.651211],[-5.783662,-1.033130,-1.733490],[-6.135645,5.958995,2.478004]],[[3.832155,-6.690583,-5.352312],[-4.609794,-7.165512,-8.892263],[8.894057,-7.295852,3.233985],[-4.525902,4.923931,-1.127036],[-2.850729,8.899395,6.527168],[0.682754,9.377088,-9.437375],[-0.599205,-6.945984,8.945694],[-6.200011,-2.642549,-9.511776],[6.971189,6.592088,8.502240]],[[-4.735108,-4.895015,7.684363],[-9.595710,-6.984631,-1.940824],[-3.280144,9.843413,1.852170],[8.630237,2.929371,-9.150982],[3.005564,-7.467194,-8.805147],[9.017801,3.687149,3.773493],[9.372991,6.055133,7.240974],[1.229251,-1.520000,3.247341],[7.718896,7.122517,-2.039799]],[[-3.734747,0.076798,-1.972605],[-9.585237,8.258576,5.163498],[-1.055424,-5.005710,-0.551069],[-9.425349,9.560460,-8.583922],[-5.708280,-1.294891,-7.337486],[-5.566296,-4.332133,0.391619],[4.821482,-7.686895,7.421666],[4.796025,6.562078,0.978286],[-4.299123,6.500608,-8.434977]],[[-9.063839,6.182883,-5.766864],[3.229395,4.863142,-2.330229],[-1.335406,-0.400923,-8.595687],[-2.721124,-0.588454,-9.756286],[8.642538,5.199925,-9.884342],[-4.368220,-5.609999,8.349091],[7.783818,5.573546,5.228320],[1.619797,-1.771578,-0.449333],[7.036019,-5.913619,-7.104398]],[[2.792089,7.146198,-7.374491],[-9.496434,-2.461564,3.670433],[5.006897,-1.990436,3.752474],[-6.141853,8.319141,-6.170262],[-1.976820,-5.594674,4.249793],[5.885189,-4.351788,8.303849],[-1.004520,7.718406,8.129770],[4.961070,8.468913,0.290812],[6.079713,7.633007,-4.809120]],[[-4.229922,3.207895,-9.387869],[-3.081083,1.016118,-0.275451],[5.711814,-2.409731,-1.713267],[4.686544,-8.026045,1.788056],[9.514449,-5.527147,-9.383366],[3.414657,9.847206,2.287294],[3.060464,3.510446,8.238781],[-4.411955,-3.051844,3.197311],[-4.492168,-6.959930,-0.389982]],[[-8.554710,-7.365179,-6.620507],[-0.253474,-6.717978,0.347756],[1.192375,2.495790,5.078474],[-0.808583,2.266778,9.878981],[8.515349,-4.287257,-9.761924],[-0.180819,-4.972108,0.694594],[9.925161,-9.097482,1.476066],[2.523501,4.038587,2.648227],[1.595916,-2.133727,7.451795]]], dtype = "float32")#candidate|2904|(10, 9, 3)|const|float32
bop_2905 = relay.less_equal(call_2900.astype('bool'), relay.reshape(const_2904.astype('bool'), relay.shape_of(call_2900))) # shape=(10, 9, 3)
bop_2908 = relay.less_equal(call_2901.astype('bool'), relay.reshape(const_2904.astype('bool'), relay.shape_of(call_2901))) # shape=(10, 9, 3)
func_2030_call = mod.get_global_var('func_2030')
func_2033_call = mutated_mod.get_global_var('func_2033')
var_2916 = relay.var("var_2916", dtype = "uint32", shape = (640,))#candidate|2916|(640,)|var|uint32
call_2915 = relay.TupleGetItem(func_2030_call(relay.reshape(var_2916.astype('uint32'), [640,])), 0)
call_2917 = relay.TupleGetItem(func_2033_call(relay.reshape(var_2916.astype('uint32'), [640,])), 0)
output = relay.Tuple([bop_2905,call_2915,var_2916,])
output2 = relay.Tuple([bop_2908,call_2917,var_2916,])
func_2918 = relay.Function([var_2916,], output)
mod['func_2918'] = func_2918
mod = relay.transform.InferType()(mod)
var_2919 = relay.var("var_2919", dtype = "uint32", shape = (640,))#candidate|2919|(640,)|var|uint32
output = func_2918(var_2919)
func_2920 = relay.Function([var_2919], output)
mutated_mod['func_2920'] = func_2920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_2964 = func_1207_call()
call_2965 = func_1207_call()
output = relay.Tuple([call_2964,])
output2 = relay.Tuple([call_2965,])
func_2968 = relay.Function([], output)
mod['func_2968'] = func_2968
mod = relay.transform.InferType()(mod)
output = func_2968()
func_2969 = relay.Function([], output)
mutated_mod['func_2969'] = func_2969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_2996 = relay.TupleGetItem(func_1316_call(), 2)
call_2997 = relay.TupleGetItem(func_1318_call(), 2)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_3016 = relay.TupleGetItem(func_1370_call(), 0)
call_3017 = relay.TupleGetItem(func_1371_call(), 0)
bop_3018 = relay.power(call_3016.astype('float64'), relay.reshape(call_2996.astype('float64'), relay.shape_of(call_3016))) # shape=(4, 15, 4)
bop_3021 = relay.power(call_3017.astype('float64'), relay.reshape(call_2997.astype('float64'), relay.shape_of(call_3017))) # shape=(4, 15, 4)
output = bop_3018
output2 = bop_3021
func_3027 = relay.Function([], output)
mod['func_3027'] = func_3027
mod = relay.transform.InferType()(mod)
mutated_mod['func_3027'] = func_3027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3027_call = mutated_mod.get_global_var('func_3027')
call_3028 = func_3027_call()
output = call_3028
func_3029 = relay.Function([], output)
mutated_mod['func_3029'] = func_3029
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3062 = relay.var("var_3062", dtype = "float64", shape = (8, 12, 15))#candidate|3062|(8, 12, 15)|var|float64
uop_3063 = relay.sin(var_3062.astype('float64')) # shape=(8, 12, 15)
output = relay.Tuple([uop_3063,])
output2 = relay.Tuple([uop_3063,])
func_3071 = relay.Function([var_3062,], output)
mod['func_3071'] = func_3071
mod = relay.transform.InferType()(mod)
var_3072 = relay.var("var_3072", dtype = "float64", shape = (8, 12, 15))#candidate|3072|(8, 12, 15)|var|float64
output = func_3071(var_3072)
func_3073 = relay.Function([var_3072], output)
mutated_mod['func_3073'] = func_3073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_3075 = relay.TupleGetItem(func_2968_call(), 0)
call_3076 = relay.TupleGetItem(func_2969_call(), 0)
func_1614_call = mod.get_global_var('func_1614')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_3085 = relay.TupleGetItem(func_1614_call(), 0)
call_3086 = relay.TupleGetItem(func_1615_call(), 0)
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_3099 = relay.TupleGetItem(func_968_call(), 0)
call_3100 = relay.TupleGetItem(func_970_call(), 0)
func_1770_call = mod.get_global_var('func_1770')
func_1773_call = mutated_mod.get_global_var('func_1773')
var_3126 = relay.var("var_3126", dtype = "int16", shape = (880,))#candidate|3126|(880,)|var|int16
call_3125 = relay.TupleGetItem(func_1770_call(relay.reshape(var_3126.astype('int16'), [11, 10, 8])), 0)
call_3127 = relay.TupleGetItem(func_1773_call(relay.reshape(var_3126.astype('int16'), [11, 10, 8])), 0)
output = relay.Tuple([call_3075,call_3085,call_3099,call_3125,var_3126,])
output2 = relay.Tuple([call_3076,call_3086,call_3100,call_3127,var_3126,])
func_3140 = relay.Function([var_3126,], output)
mod['func_3140'] = func_3140
mod = relay.transform.InferType()(mod)
var_3141 = relay.var("var_3141", dtype = "int16", shape = (880,))#candidate|3141|(880,)|var|int16
output = func_3140(var_3141)
func_3142 = relay.Function([var_3141], output)
mutated_mod['func_3142'] = func_3142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2400_call = mod.get_global_var('func_2400')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_3153 = relay.TupleGetItem(func_2400_call(), 0)
call_3154 = relay.TupleGetItem(func_2402_call(), 0)
func_471_call = mod.get_global_var('func_471')
func_474_call = mutated_mod.get_global_var('func_474')
const_3157 = relay.const([-5,-8,5,9,-1,-4,-2,-10,-5,-6,9,3,7,-9,3,-4,8,5,1,9,-6,-8,-4,-1,-5,-5,2,-6,-3,-7,-2,-5,2,4,-4,5,6,8,-10,-8,-7,-1], dtype = "uint32")#candidate|3157|(42,)|const|uint32
var_3158 = relay.var("var_3158", dtype = "uint32", shape = (126,))#candidate|3158|(126,)|var|uint32
call_3156 = relay.TupleGetItem(func_471_call(relay.reshape(const_3157.astype('uint32'), [1, 3, 14]), relay.reshape(var_3158.astype('uint32'), [3, 3, 14]), ), 0)
call_3159 = relay.TupleGetItem(func_474_call(relay.reshape(const_3157.astype('uint32'), [1, 3, 14]), relay.reshape(var_3158.astype('uint32'), [3, 3, 14]), ), 0)
bop_3164 = relay.logical_or(call_3156.astype('bool'), relay.reshape(var_3158.astype('bool'), relay.shape_of(call_3156))) # shape=(3, 3, 14)
bop_3167 = relay.logical_or(call_3159.astype('bool'), relay.reshape(var_3158.astype('bool'), relay.shape_of(call_3159))) # shape=(3, 3, 14)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_3168 = relay.TupleGetItem(func_1370_call(), 0)
call_3169 = relay.TupleGetItem(func_1371_call(), 0)
func_1383_call = mod.get_global_var('func_1383')
func_1386_call = mutated_mod.get_global_var('func_1386')
const_3174 = relay.const([-2,-3,-7,7,-5,-3,1,4,-9,2,-8,-4,10,-4,3,-2,4,-3,8,-6,-2,-8,9,2,-4,3,-3,7,-10,-10,2,1,-7,8,4,-8,3,9,1,9,8,-7,10,-6,7,-7,-8,-7,-3,-8,-1,3,-4,5,6,9,9,-4,-2,-1,-6,7,9,7,-1,6,3,5,6,5,5,7,-1,-2,3,1,-6,-1,4,-4,5,8,-3,-9,4,-4,-7,-4,-4,-1,-4,8,3,-4,9,4,9,-6,-7,-5,7,4,10,2,6,5,-6,-9,-2,7,-10,7,-5,4,-6,-6,8,-6,-8,6,-2,4,-4,8,-4,9,-6,-3,-9,-4,8,9,10,6,-4,3,-5,-3,-10,5,5,-7,-2,3,-9,-8,7,-5,-3,-6,-7,-2,-6,1,7,9,2,5,8,7,5,6,-3,10,4,-2,4,3,-10,-5,10,8,-10,8,-9,5,8,-7,-2,6,2,9,3,-8,-6,-9,9,-10,10,-6,3,-4,-5,-4,7,-5,2,-7,-5,8,-9,8,6,-6,-8,-5,6,-5,-10,7,1,-8,-5,-7,-1,-2,4,10,-9,-8,1,-9,-3,-7,3,2,-8,-6,7,-3,-10,3,-6,6,9,6,7,6,-10,-5,-9,-9,-1,-9,-8,-9,9,4,4,5,-2,-3,6,9,4,-1,4,9,-4,-4,-3,3,-4,9,7,-3,-5,-7,6,7,3,5,7,-1,-4,-5,7,-1,5,10,4,-10,-10,9,5,7,3,5,10,1,10,-1,6,-9,1,-2,5,-5,-10,-2,-4,3,3,-9,4,6,-6,1,10,2,1,8,7,-2,10,10,-3,1,-10,10,10,8,-5,-9,-10,8,-6,-9,10,8,3,5,-4,3,-7,-8,9,7,6,2,-7,-7,-5,-6,8,-8,-3,-9,9,10,7,7,5,-1,-9,5,3,9,-10,4,8,-1,5,9,-5,2,-7,7,2,-3,3,7,3,4,2,1,2,-2,-5,-10,7,10,10,8,-7,1,2,-6,5,-8,1,-4,3,-9,6,-9,-3,1,-8,7,1,-7,-7,7,6,6,5,10,7,-8,-3,10,-8,1,-9,5,-8,2,-9,7,4,-3,-5,-7,-4,-7,-4,3,5,9,-4,-3,-9,10,-6,1,10,7,7,-8,-10,8,-10,-5,-8,-9,9,7,-1,-5,-1,4,-2,-7,-8,-2,7,-2,2,4,-2,-10,-8,-10,-3,-3,3,8,-2,-6,9,9,-7,-7,-6,7,-5,-8,6,-10,-3,5,-2,-3,9,5,5,-6,-2,-9,3,6,-5,-8,4,-9,-1,-5,9,-7,7,-6,5,5,4,-8,2,-4,-10,-7,10,-1,2,4,-4,-10,5,3,8,9,-4,9,-1,-2,-5,5,-6,-6,4,10,3,9,5,-9,-10,7,7,9,-8,1,9,-9,-4,-5,-5,6,-4,7,7,-2,-8,10,-4,-1,1,8,-8,6,1,10,-6,-5,1,2,2,6,3,-3,-6,-3,-8,6,-7,-10,4,6,8,2,5,-9,8,-5,3,9,-4,-6,-3,-10,5,-9,-2,10,-6,1,-6,8,-8,-4,3,-8,-8,-1,7,3,1,-2,9,-5,6,-6,-6,6,-9,3,-6,1,7,4,1,-7,-1,7,3,-3,-6,1,5,-8,-8,8,-3,-9,-1,4,2,6,10,-1,5,-2], dtype = "uint32")#candidate|3174|(640,)|const|uint32
call_3173 = relay.TupleGetItem(func_1383_call(relay.reshape(const_3174.astype('uint32'), [10, 16, 4])), 0)
call_3175 = relay.TupleGetItem(func_1386_call(relay.reshape(const_3174.astype('uint32'), [10, 16, 4])), 0)
output = relay.Tuple([call_3153,const_3157,bop_3164,call_3168,call_3173,const_3174,])
output2 = relay.Tuple([call_3154,const_3157,bop_3167,call_3169,call_3175,const_3174,])
func_3178 = relay.Function([var_3158,], output)
mod['func_3178'] = func_3178
mod = relay.transform.InferType()(mod)
mutated_mod['func_3178'] = func_3178
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3179 = relay.var("var_3179", dtype = "uint32", shape = (126,))#candidate|3179|(126,)|var|uint32
func_3178_call = mutated_mod.get_global_var('func_3178')
call_3180 = func_3178_call(var_3179)
output = call_3180
func_3181 = relay.Function([var_3179], output)
mutated_mod['func_3181'] = func_3181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_3196 = relay.TupleGetItem(func_1370_call(), 0)
call_3197 = relay.TupleGetItem(func_1371_call(), 0)
func_1292_call = mod.get_global_var('func_1292')
func_1295_call = mutated_mod.get_global_var('func_1295')
const_3202 = relay.const([[-7.864295,5.080358,6.882080,3.928325,3.990759,-9.763670,-8.321384,-6.310059,-3.157743,6.839052,4.150950,-1.158192,-6.807360,2.803960,7.684745,-0.350241,-4.259819,2.239259,-6.808991,3.430260,-6.599535,8.512733,-6.847946,-5.337877,-0.621633,-4.639592,6.203742,-6.924482,-5.908460,-5.774799,-9.008363,4.533820,-0.415677,1.231024,-4.771934,-9.449775,-2.250401,7.098469,0.693858,2.523736,-0.565647,7.737349,-5.982278,0.597445,-7.809767,-2.455026,3.816028,1.743826,1.621711,-2.049683,5.561047,-5.300597,-2.329842,-7.948463,-2.699549,0.741690,1.560117,-8.521002,-2.967000,8.549757,0.895960,9.820219,6.037917,-6.941017,7.267874,-6.528887,3.062737,4.572743,3.516580,-9.448982,1.723864,-6.032923,-8.280204,4.988744,-2.660658,7.686923,-6.176915,-5.246323,0.837418,-6.854643,2.097918,1.042883,-5.537082,-3.431953,-6.772875,1.268525,-2.243812,3.959167,-0.201366,4.630875,3.300318,-2.799995,-8.369681,7.575332,3.006239,-1.418406,4.841933,1.443434,-2.919411,0.718409,-5.386307,9.318956,-5.694320,-4.733561,3.561289,8.187708,-9.072078,-0.606748,4.746075,7.873354,-3.829129,4.515455,4.370083,8.002586,1.296497,8.206192,6.949688,-6.486364,9.035704,-8.186018,5.178672,8.298678,9.547889,-2.824510,1.073911,5.927050,1.999815,1.625981,3.194930,5.723303,8.968357,7.055108,0.769842,-9.746605,-0.098434,1.288432,2.303549,9.703417,-1.461048,8.383267,4.906161,2.667620,9.302976,-3.410278,3.881386,9.705855,-9.153835,2.238530,7.354724,-3.081457,-4.484002,9.978725,-9.898947,-4.120087,-8.537827,-3.190777,-2.153913,-3.158621,8.028410,9.908304,-0.372875,1.638444,0.892845,-7.582166,3.482331,-0.926875,-2.714620,8.026984,-9.428276,-4.715681,2.050705,8.141433,-4.659069,1.461000,-4.168104,6.374968,-2.610972,8.855341,1.242139,-6.418523,-7.377153,5.164147,-6.105892,4.801704,-4.899557,1.906543,-1.927665,-1.891627,-7.266611,-0.157685,-3.373448,-5.121858,0.642964,-8.965442,6.696074,3.182812,4.308035,0.357400,5.605816,-9.298460,-9.869433,2.845081,-4.508917,8.253216,5.591608,6.997849,2.628975,-4.644487,7.304611,-2.228043,2.144212,-5.769804,-1.229629,-4.265002,-6.383661,3.308794,-2.361562,-5.000314,-6.174983,-5.760241,2.888948,5.348847,1.425603,8.806851,-8.716645,0.512062,6.551979,-4.586524,0.542355,9.704853,-6.142431,-6.315872,7.737042,4.305423,2.397411,-0.952374,-6.223214,6.908014,8.201461,-5.683760,-0.420355,-9.443560,-3.081126,1.214873,4.988910,0.929445,-4.530017,2.633687,-3.928782,2.348441,-6.588740,3.946221,-4.163822,-6.121505,8.284000,3.246632,-6.935779,-7.333734,2.896908,0.824604,-2.729551,-3.525435,-8.950125,2.622653,-1.971188,-1.607685,-4.471168,3.016687,2.562073,-3.797181]], dtype = "float32")#candidate|3202|(1, 270)|const|float32
call_3201 = relay.TupleGetItem(func_1292_call(relay.reshape(const_3202.astype('float32'), [10, 9, 3])), 0)
call_3203 = relay.TupleGetItem(func_1295_call(relay.reshape(const_3202.astype('float32'), [10, 9, 3])), 0)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_3213 = func_429_call()
call_3214 = func_429_call()
func_3178_call = mod.get_global_var('func_3178')
func_3181_call = mutated_mod.get_global_var('func_3181')
var_3216 = relay.var("var_3216", dtype = "uint32", shape = (126,))#candidate|3216|(126,)|var|uint32
call_3215 = relay.TupleGetItem(func_3178_call(relay.reshape(var_3216.astype('uint32'), [126,])), 5)
call_3217 = relay.TupleGetItem(func_3181_call(relay.reshape(var_3216.astype('uint32'), [126,])), 5)
bop_3221 = relay.add(call_3213.astype('int64'), relay.reshape(const_3202.astype('int64'), relay.shape_of(call_3213))) # shape=(10, 9, 3)
bop_3224 = relay.add(call_3214.astype('int64'), relay.reshape(const_3202.astype('int64'), relay.shape_of(call_3214))) # shape=(10, 9, 3)
output = relay.Tuple([call_3196,call_3201,call_3215,var_3216,bop_3221,])
output2 = relay.Tuple([call_3197,call_3203,call_3217,var_3216,bop_3224,])
func_3231 = relay.Function([var_3216,], output)
mod['func_3231'] = func_3231
mod = relay.transform.InferType()(mod)
var_3232 = relay.var("var_3232", dtype = "uint32", shape = (126,))#candidate|3232|(126,)|var|uint32
output = func_3231(var_3232)
func_3233 = relay.Function([var_3232], output)
mutated_mod['func_3233'] = func_3233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3244 = relay.var("var_3244", dtype = "float32", shape = (5, 16, 10))#candidate|3244|(5, 16, 10)|var|float32
var_3245 = relay.var("var_3245", dtype = "float32", shape = (5, 16, 10))#candidate|3245|(5, 16, 10)|var|float32
bop_3246 = relay.floor_divide(var_3244.astype('float32'), relay.reshape(var_3245.astype('float32'), relay.shape_of(var_3244))) # shape=(5, 16, 10)
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
var_3257 = relay.var("var_3257", dtype = "float32", shape = (864,))#candidate|3257|(864,)|var|float32
call_3256 = relay.TupleGetItem(func_2291_call(relay.reshape(var_3257.astype('float32'), [6, 9, 16])), 0)
call_3258 = relay.TupleGetItem(func_2294_call(relay.reshape(var_3257.astype('float32'), [6, 9, 16])), 0)
func_1383_call = mod.get_global_var('func_1383')
func_1386_call = mutated_mod.get_global_var('func_1386')
var_3266 = relay.var("var_3266", dtype = "uint32", shape = (640,))#candidate|3266|(640,)|var|uint32
call_3265 = relay.TupleGetItem(func_1383_call(relay.reshape(var_3266.astype('uint32'), [10, 16, 4])), 0)
call_3267 = relay.TupleGetItem(func_1386_call(relay.reshape(var_3266.astype('uint32'), [10, 16, 4])), 0)
func_1148_call = mod.get_global_var('func_1148')
func_1150_call = mutated_mod.get_global_var('func_1150')
var_3269 = relay.var("var_3269", dtype = "uint32", shape = (126,))#candidate|3269|(126,)|var|uint32
call_3268 = relay.TupleGetItem(func_1148_call(relay.reshape(var_3269.astype('uint32'), [126,])), 0)
call_3270 = relay.TupleGetItem(func_1150_call(relay.reshape(var_3269.astype('uint32'), [126,])), 0)
bop_3274 = relay.floor_divide(var_3266.astype('float64'), relay.reshape(call_3265.astype('float64'), relay.shape_of(var_3266))) # shape=(640,)
bop_3277 = relay.floor_divide(var_3266.astype('float64'), relay.reshape(call_3267.astype('float64'), relay.shape_of(var_3266))) # shape=(640,)
output = relay.Tuple([bop_3246,call_3256,var_3257,call_3268,var_3269,bop_3274,])
output2 = relay.Tuple([bop_3246,call_3258,var_3257,call_3270,var_3269,bop_3277,])
func_3280 = relay.Function([var_3244,var_3245,var_3257,var_3266,var_3269,], output)
mod['func_3280'] = func_3280
mod = relay.transform.InferType()(mod)
var_3281 = relay.var("var_3281", dtype = "float32", shape = (5, 16, 10))#candidate|3281|(5, 16, 10)|var|float32
var_3282 = relay.var("var_3282", dtype = "float32", shape = (5, 16, 10))#candidate|3282|(5, 16, 10)|var|float32
var_3283 = relay.var("var_3283", dtype = "float32", shape = (864,))#candidate|3283|(864,)|var|float32
var_3284 = relay.var("var_3284", dtype = "uint32", shape = (640,))#candidate|3284|(640,)|var|uint32
var_3285 = relay.var("var_3285", dtype = "uint32", shape = (126,))#candidate|3285|(126,)|var|uint32
output = func_3280(var_3281,var_3282,var_3283,var_3284,var_3285,)
func_3286 = relay.Function([var_3281,var_3282,var_3283,var_3284,var_3285,], output)
mutated_mod['func_3286'] = func_3286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_3328 = relay.TupleGetItem(func_1940_call(), 0)
call_3329 = relay.TupleGetItem(func_1941_call(), 0)
output = call_3328
output2 = call_3329
func_3342 = relay.Function([], output)
mod['func_3342'] = func_3342
mod = relay.transform.InferType()(mod)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3342_call = mutated_mod.get_global_var('func_3342')
call_3343 = func_3342_call()
output = call_3343
func_3344 = relay.Function([], output)
mutated_mod['func_3344'] = func_3344
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3411 = relay.var("var_3411", dtype = "float64", shape = (2, 15, 16))#candidate|3411|(2, 15, 16)|var|float64
uop_3412 = relay.asin(var_3411.astype('float64')) # shape=(2, 15, 16)
bop_3428 = relay.not_equal(var_3411.astype('bool'), relay.reshape(uop_3412.astype('bool'), relay.shape_of(var_3411))) # shape=(2, 15, 16)
func_2480_call = mod.get_global_var('func_2480')
func_2482_call = mutated_mod.get_global_var('func_2482')
const_3437 = relay.const([-3.607598,0.703435,2.588770,0.097913,2.157544,-5.067703,-9.602586,-6.641340,4.962340,-8.038250,-5.046466,1.372345,8.978472,1.027951,-7.626159,-9.975087,9.830646,-1.167601,7.623574,6.091112,2.788047,-1.098846,4.413084,9.122017,8.136239,-5.407715,1.526454,-7.811473,4.537348,3.599204,-6.916609,8.528772,-9.823699,-4.874812,6.363649,-0.415909,6.811106,-1.335489,3.475178,2.610160,6.306009,-5.508171,-5.723537,-2.718834,0.129653,5.591568,5.601120,3.350593,7.977798,4.647344,1.127371,1.133034,5.097733,1.736050,5.791943,5.522524,1.563188,5.653065,-0.738326,3.858904,-1.375479,-2.872863,1.746089,7.145362,9.625266,4.418666,-5.915094,-9.719813,-3.462515,-0.435665,-1.636014,4.642249,-2.716602,0.694388,-4.632326,-9.675297,-7.739059,-7.389082,-0.322118,-9.660429,-8.304220,8.946486,-9.409757,-5.876073,6.878416,-8.483151,9.792131,1.754906,-4.291896,-0.450790,-6.953141,3.386188,2.048998,-7.831909,6.421240,-5.709669,9.493297,-2.462548,1.818948,-0.550157,-9.209215,-0.741461,-6.005736,8.356791,1.407014,5.596726,-8.815483,-0.820747,-8.729844,5.261491,9.449045,-8.404466,4.325062,-3.201505,4.056025,-4.227082,8.753715,3.898211,-8.254873,-5.130595,1.498738,0.672017,7.611025,1.529661,2.304928,0.523928,-6.715745,7.004216,2.881076,-7.713499,-6.510961,-9.391850,-3.651384,-0.267643,-9.532439,-8.997164,-4.488822,0.509072,0.252186,-6.834312,3.330756,7.973329,9.629102,-6.132680,-5.673920,6.775662,5.047807,-4.649850,-4.850674,-1.944734,8.729010,-4.891549,9.139501,1.015517,-7.194633,8.167596,-6.076802,-4.657861,5.183001,-3.225515,4.093723,-7.060530,1.361979,-6.125449,1.364619,-9.708187,0.591197,9.791563,-6.771130,7.904539,-0.091374,-8.035221,5.887964,-0.157854,8.107964,-2.964538,-2.207167,1.035378,8.111115,8.585409,6.512858,-9.387875,-2.950525,8.929331,-4.622396,-8.967213,0.166322,5.108300,4.270035,7.194252,-8.055441,4.710486,-2.468348,-8.790125,0.758122,1.830150,4.056797,9.989066,2.983288,-1.826641,-7.045954,-1.459858,-7.330212,-5.264924,6.798687,-6.200514,-7.998062,-2.125369,0.694399,-4.521473,2.743187,6.877056,0.375555,-9.146832,1.352539,9.454111,3.919851,1.096141,4.349274,0.862518,4.868153,1.393793,-5.443319,-7.243070,-6.357981,-2.291425,-2.616042,2.847242,-4.750669,-0.958120,-0.953374,9.971167,1.940082,8.081656,1.757004,0.696049,4.128184,-5.451235,0.375341,3.298406,1.068750,8.631395,4.974358,-8.443728,-0.133347,5.990044,-0.844149,2.795946,4.792713,-2.594962,9.969189,1.395720,-5.618252,-3.128606,-0.095568,-2.698739,8.836728,-4.701635,-9.180378,8.089457,4.824978,1.835758,0.529653,-8.364835,-5.341242,2.934390,-7.426299,-6.420101,-5.708957,-2.840732,-0.057128,9.150353,-8.593294,-9.270743,-7.522638,-0.842976,-4.964642,2.297133,-7.637726,-0.696531,-0.822624,-7.200383,-9.006465,-5.122474,-1.909330,7.897028,2.091613,-0.825064,-4.707168,-2.796321,-1.935531,4.481139,-1.126932,9.570949,-4.158339,6.554259,3.315386,9.081175,-5.249662,7.408078,1.151748,0.038915,7.353653,-1.745302,-4.284811,-8.555719,5.010875,0.535277,-8.044076,-6.231128,-1.408556,4.513302,-6.259173,5.120381,-7.760372], dtype = "float64")#candidate|3437|(315,)|const|float64
call_3436 = relay.TupleGetItem(func_2480_call(relay.reshape(const_3437.astype('float64'), [5, 9, 7])), 0)
call_3438 = relay.TupleGetItem(func_2482_call(relay.reshape(const_3437.astype('float64'), [5, 9, 7])), 0)
output = relay.Tuple([bop_3428,call_3436,const_3437,])
output2 = relay.Tuple([bop_3428,call_3438,const_3437,])
func_3440 = relay.Function([var_3411,], output)
mod['func_3440'] = func_3440
mod = relay.transform.InferType()(mod)
mutated_mod['func_3440'] = func_3440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3441 = relay.var("var_3441", dtype = "float64", shape = (2, 15, 16))#candidate|3441|(2, 15, 16)|var|float64
func_3440_call = mutated_mod.get_global_var('func_3440')
call_3442 = func_3440_call(var_3441)
output = call_3442
func_3443 = relay.Function([var_3441], output)
mutated_mod['func_3443'] = func_3443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_736_call = mod.get_global_var('func_736')
func_738_call = mutated_mod.get_global_var('func_738')
call_3462 = func_736_call()
call_3463 = func_736_call()
var_3466 = relay.var("var_3466", dtype = "float64", shape = (10, 9, 3))#candidate|3466|(10, 9, 3)|var|float64
bop_3467 = relay.maximum(call_3462.astype('int64'), relay.reshape(var_3466.astype('int64'), relay.shape_of(call_3462))) # shape=(10, 9, 3)
bop_3470 = relay.maximum(call_3463.astype('int64'), relay.reshape(var_3466.astype('int64'), relay.shape_of(call_3463))) # shape=(10, 9, 3)
output = bop_3467
output2 = bop_3470
func_3472 = relay.Function([var_3466,], output)
mod['func_3472'] = func_3472
mod = relay.transform.InferType()(mod)
var_3473 = relay.var("var_3473", dtype = "float64", shape = (10, 9, 3))#candidate|3473|(10, 9, 3)|var|float64
output = func_3472(var_3473)
func_3474 = relay.Function([var_3473], output)
mutated_mod['func_3474'] = func_3474
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3537 = relay.var("var_3537", dtype = "float64", shape = ())#candidate|3537|()|var|float64
var_3538 = relay.var("var_3538", dtype = "float64", shape = (8, 5, 5))#candidate|3538|(8, 5, 5)|var|float64
bop_3539 = relay.divide(var_3537.astype('float64'), var_3538.astype('float64')) # shape=(8, 5, 5)
output = bop_3539
output2 = bop_3539
func_3542 = relay.Function([var_3537,var_3538,], output)
mod['func_3542'] = func_3542
mod = relay.transform.InferType()(mod)
mutated_mod['func_3542'] = func_3542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mutated_mod.get_global_var('func_3542')
var_3544 = relay.var("var_3544", dtype = "float64", shape = ())#candidate|3544|()|var|float64
var_3545 = relay.var("var_3545", dtype = "float64", shape = (8, 5, 5))#candidate|3545|(8, 5, 5)|var|float64
call_3543 = func_3542_call(var_3544,var_3545,)
output = call_3543
func_3546 = relay.Function([var_3544,var_3545,], output)
mutated_mod['func_3546'] = func_3546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_3558 = relay.TupleGetItem(func_1044_call(), 0)
call_3559 = relay.TupleGetItem(func_1045_call(), 0)
output = relay.Tuple([call_3558,])
output2 = relay.Tuple([call_3559,])
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
func_1044_call = mod.get_global_var('func_1044')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_3598 = relay.TupleGetItem(func_1044_call(), 0)
call_3599 = relay.TupleGetItem(func_1045_call(), 0)
output = relay.Tuple([call_3598,])
output2 = relay.Tuple([call_3599,])
func_3613 = relay.Function([], output)
mod['func_3613'] = func_3613
mod = relay.transform.InferType()(mod)
output = func_3613()
func_3614 = relay.Function([], output)
mutated_mod['func_3614'] = func_3614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_3694 = func_1207_call()
call_3695 = func_1207_call()
func_2260_call = mod.get_global_var('func_2260')
func_2264_call = mutated_mod.get_global_var('func_2264')
var_3706 = relay.var("var_3706", dtype = "uint32", shape = (63, 2))#candidate|3706|(63, 2)|var|uint32
var_3707 = relay.var("var_3707", dtype = "uint32", shape = (1512,))#candidate|3707|(1512,)|var|uint32
call_3705 = relay.TupleGetItem(func_2260_call(relay.reshape(var_3706.astype('uint32'), [126, 1]), relay.reshape(var_3707.astype('uint32'), [126, 12]), ), 2)
call_3708 = relay.TupleGetItem(func_2264_call(relay.reshape(var_3706.astype('uint32'), [126, 1]), relay.reshape(var_3707.astype('uint32'), [126, 12]), ), 2)
output = relay.Tuple([call_3694,call_3705,var_3706,var_3707,])
output2 = relay.Tuple([call_3695,call_3708,var_3706,var_3707,])
func_3721 = relay.Function([var_3706,var_3707,], output)
mod['func_3721'] = func_3721
mod = relay.transform.InferType()(mod)
var_3722 = relay.var("var_3722", dtype = "uint32", shape = (63, 2))#candidate|3722|(63, 2)|var|uint32
var_3723 = relay.var("var_3723", dtype = "uint32", shape = (1512,))#candidate|3723|(1512,)|var|uint32
output = func_3721(var_3722,var_3723,)
func_3724 = relay.Function([var_3722,var_3723,], output)
mutated_mod['func_3724'] = func_3724
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3732 = relay.const([[[6,-10,2,1,3,1,-8,-6,-4,10,1,-10,-10,1,-1,-7],[-10,-9,-7,10,-6,5,3,6,6,-1,-3,-9,6,-7,4,-5],[5,7,-4,1,-9,5,-10,9,-9,5,3,-5,8,7,7,4],[-4,3,-1,2,-5,-2,-8,-2,-3,-10,-5,-7,-8,2,-4,9],[-1,-10,7,10,6,6,3,2,-9,2,7,4,4,3,4,8]],[[4,-6,9,-4,10,-9,-10,-10,-5,-2,2,10,-1,3,-6,-1],[-10,-1,6,4,-5,-10,-5,-5,-3,-3,-10,2,-9,-9,8,5],[-8,7,-4,-10,3,6,-10,-8,-8,7,-7,1,4,9,9,-1],[2,1,-6,-5,-10,-9,-3,-3,-10,-1,9,-3,4,-4,5,4],[-1,3,7,-10,-10,7,-8,8,-1,6,-5,-1,-8,3,-10,3]],[[3,3,-4,5,2,1,2,-7,-8,-3,10,1,-10,-5,3,-4],[-2,4,-9,-3,-3,-10,-2,10,-10,5,6,1,-2,6,2,4],[8,1,-9,10,-9,-10,9,-2,-2,10,5,-4,6,4,2,2],[-8,-7,9,10,8,-10,-10,6,1,10,7,-3,-5,-1,-5,-9],[7,-9,-5,-6,-8,2,1,10,5,-8,-5,3,9,9,8,8]],[[-5,-4,5,7,-10,-1,-6,5,-10,-4,-5,5,3,-10,5,6],[5,2,2,5,-8,-3,7,6,2,-2,-8,-10,4,-10,8,-9],[-6,4,2,-1,8,-5,-3,-4,-4,1,5,1,-1,-8,-6,3],[2,1,-7,-4,-6,1,3,-4,2,-9,5,8,-10,7,7,-8],[-7,3,-1,10,10,-7,-5,-2,-6,-5,8,9,2,-5,-7,-8]],[[-2,-8,-1,-2,-10,-6,10,1,6,9,1,-3,5,2,3,-6],[-10,-9,3,-2,10,7,5,-8,-5,-8,-6,-9,-8,-2,-8,5],[-3,1,-6,8,-10,-6,4,-7,-10,5,-5,-8,3,6,-10,-1],[7,-10,4,9,-4,10,-10,5,3,7,-4,5,-6,-1,5,-1],[4,7,9,2,2,1,3,3,6,8,-6,-9,5,9,2,2]],[[1,-1,-7,4,-9,3,-1,-7,-8,-8,7,7,7,-2,5,-2],[5,-5,-8,-6,-5,8,9,4,-2,2,-4,-1,-2,-10,9,3],[7,10,8,4,-7,1,8,3,-2,1,-1,-6,7,2,-10,-2],[3,-4,-10,-8,1,-2,7,-10,8,4,4,-6,6,7,-3,2],[-2,8,-3,6,-6,-4,4,1,-3,-5,2,10,-7,3,7,-7]],[[2,-9,-4,8,5,-2,-5,-3,7,-7,-9,-9,3,8,7,-9],[3,-3,-2,6,2,4,-10,-8,-7,5,2,-2,-6,-7,8,-2],[-1,-7,-6,8,-10,5,-3,6,-8,4,7,-8,-10,5,-10,-8],[-2,4,5,-5,-6,4,5,-9,-3,6,-3,-4,-9,9,-8,10],[2,-7,8,4,4,3,-10,-6,-7,4,7,1,6,3,8,3]],[[7,-9,-4,1,10,1,8,2,8,-5,3,10,9,3,-7,9],[8,3,8,-2,-7,8,-10,3,6,2,-6,-9,8,-4,10,-10],[-9,2,6,8,7,-1,6,-5,-1,-4,-1,-4,4,-3,1,-5],[-10,-10,3,10,-3,6,-4,-2,10,-4,8,2,-7,-10,-2,-7],[-4,-7,-4,-6,9,-6,3,-1,-5,-7,-4,9,-6,8,-4,10]],[[-3,-4,5,3,9,10,9,-8,6,-7,4,2,5,-8,6,-6],[5,5,9,8,7,-4,9,1,5,8,6,-7,-1,-9,-3,5],[8,-7,-9,-6,3,5,2,-7,-5,-6,4,-3,8,-9,8,8],[7,-2,-2,-5,10,7,7,7,-7,-5,6,-4,-2,7,1,6],[3,-2,-8,-2,-6,-10,-10,-5,2,10,9,-4,8,-1,-1,7]],[[-6,-10,8,5,-8,-7,4,7,-5,3,10,-5,1,9,2,5],[-5,-6,-7,-8,-6,3,-10,-5,7,9,5,8,-9,-9,3,2],[-9,2,9,-10,7,-6,-6,-2,-9,2,4,-2,-7,7,-5,9],[-7,-1,-10,-5,4,4,4,-3,-6,9,-5,2,-1,1,7,-1],[8,3,1,-7,-9,7,6,6,-4,-9,-5,-8,-1,2,6,4]],[[-5,6,-5,3,3,-7,9,-8,-10,2,1,2,9,-9,7,-1],[-10,-10,-9,9,4,-10,1,6,8,-7,-7,10,-2,3,4,-6],[2,-9,1,-4,4,-8,5,-6,-3,9,-1,8,-9,5,-6,10],[-6,-8,5,-4,7,3,9,2,-2,3,-3,7,1,-7,-4,4],[4,-9,-5,7,6,-3,-1,6,-9,7,10,-4,-9,-10,6,4]],[[-8,-8,-7,-7,6,7,-7,1,10,8,3,2,10,4,8,5],[-3,2,-9,3,1,5,3,-5,-5,4,4,-9,-10,2,10,-7],[-2,5,10,-9,7,10,-3,4,10,5,6,10,-8,5,2,3],[10,5,5,2,1,4,9,-1,8,2,-1,-9,7,-7,7,-10],[9,9,-3,-7,-3,8,1,-8,5,-2,-4,-5,4,-7,5,9]],[[5,5,-9,4,-5,1,-2,-4,10,-5,-6,5,-4,2,2,-1],[-9,6,-3,9,1,-4,10,-1,-6,7,7,-6,4,2,1,-4],[-2,-10,9,2,1,6,-8,4,-1,9,-2,-1,-3,2,-6,6],[-7,4,-6,-9,-4,8,9,-7,-2,-2,-1,1,-6,10,1,2],[2,5,2,-7,-8,2,9,-10,8,-5,5,-7,-9,2,4,-8]],[[-10,8,-7,-10,-2,-2,2,1,-8,-10,-2,-3,-3,1,-1,-6],[3,2,-9,-5,-7,-1,3,-10,8,-3,9,1,2,-1,-2,5],[3,5,2,-2,-1,9,-6,-6,-10,-5,6,3,8,3,1,5],[-5,-5,-2,-9,1,-8,8,-1,2,9,10,8,-6,-7,-10,2],[-3,-4,5,10,3,2,2,2,-9,-6,5,-6,6,9,-4,-1]]], dtype = "uint32")#candidate|3732|(14, 5, 16)|const|uint32
const_3733 = relay.const([[[7,3,2,3,2,-4,-6,-5,-5,4,10,-2,3,-7,-9,10],[-8,-5,-4,10,4,-3,2,1,-2,5,8,-6,-5,3,-9,10],[-7,-8,5,6,-1,-4,-8,-10,9,-4,-3,7,5,-3,-4,-2],[10,-9,-7,8,6,10,-6,-4,-8,-1,7,10,-7,-6,8,1],[7,4,-7,-3,6,-6,-6,7,-7,4,6,7,6,6,1,-1]],[[9,4,2,10,-1,-8,5,10,4,7,5,-5,7,-5,1,9],[-5,-6,10,-5,-2,-9,-8,10,-2,-2,-3,10,-10,-8,-4,9],[-2,6,-2,-5,4,3,5,-6,2,-6,6,-5,-2,5,2,5],[2,-5,2,1,4,-10,9,5,-3,-8,-6,5,-8,4,-8,-3],[10,-7,8,10,3,-10,-7,6,6,1,1,-10,10,-8,-2,-1]],[[8,9,-5,5,-3,10,2,10,-4,-7,-8,-3,-2,-7,3,-1],[5,5,10,-5,7,-1,-5,-6,-1,-3,2,7,8,-10,-3,10],[-10,-7,-6,-1,10,-3,-2,-4,-2,6,-3,-9,9,10,8,-10],[-6,9,9,-7,2,4,9,-1,-2,-6,-9,6,4,-10,7,-3],[6,6,-9,-4,5,7,5,6,4,-2,6,-3,-5,5,4,4]],[[-7,3,3,9,5,-1,-3,-8,8,-1,10,-7,6,7,-9,10],[-3,-1,2,6,5,8,6,-6,7,-1,1,4,-1,9,-5,-3],[2,5,-4,-1,-10,-7,-6,1,10,2,1,9,8,9,7,-2],[-7,-4,9,10,-6,-6,-9,6,8,-1,4,10,-9,5,-2,-6],[-5,-10,8,4,6,-4,6,6,-8,2,8,5,-2,5,9,-10]],[[4,9,-9,-5,2,2,9,-1,-9,-2,6,6,10,-9,-5,-5],[1,2,-6,5,-6,3,8,-6,-8,4,6,1,1,6,3,6],[3,3,5,-7,-8,-8,-6,-3,-1,-8,7,4,3,8,1,-9],[-2,-4,-2,-9,1,5,2,-4,5,1,-3,-3,-4,4,3,-10],[6,5,4,6,-1,-5,-3,5,2,1,10,-4,5,10,1,-4]],[[-3,-5,-2,6,-4,-6,1,6,-7,9,-10,-2,10,4,1,6],[-8,-2,-4,4,3,-4,9,-8,-6,4,1,-3,-5,2,-5,-1],[-1,-3,-3,-2,5,1,-7,-2,7,1,1,10,-10,-3,3,8],[-7,1,-8,-6,-1,8,-7,1,6,5,7,-5,-10,-2,10,-8],[-2,9,-4,-2,-4,-2,-3,-9,6,-8,9,-2,10,3,5,-9]],[[2,7,-4,8,-9,1,3,3,-5,-4,4,5,-1,6,-10,3],[4,6,8,6,-4,3,10,-1,-9,-9,-3,7,-1,-2,-9,-2],[6,10,4,5,-4,7,4,-9,5,4,-2,-3,-5,5,1,-6],[5,-3,4,7,4,-4,-6,-1,-10,-10,-9,7,-10,-7,-8,-8],[-1,-2,-8,-2,6,3,10,-4,1,3,9,-6,-2,1,-8,-3]],[[-9,3,-7,-10,-3,-7,-8,-3,5,1,-6,4,-9,-8,-4,-5],[9,2,3,10,-6,-6,8,-3,5,-6,8,1,-2,2,1,1],[-5,5,-5,-1,4,3,-9,4,10,-7,9,-6,4,-9,7,-4],[-4,-8,7,-10,-1,2,1,3,7,10,5,-9,3,-5,-9,-3],[-1,-2,2,-9,6,4,9,-1,-7,-2,-6,-3,-10,-1,1,-10]],[[5,-1,5,-2,3,-2,-3,-9,-3,-3,4,10,-8,1,-5,4],[-4,-8,6,1,6,-4,-6,9,5,-8,10,1,9,9,-4,3],[-7,8,-1,-5,-4,-7,-3,10,10,7,8,-10,-9,-2,-2,-4],[7,6,-2,-6,1,7,-2,2,-6,4,6,-4,6,1,-2,9],[-6,9,6,-4,-1,-1,-9,6,3,-1,7,5,1,1,8,3]],[[5,-1,9,9,10,2,-4,-7,10,3,3,-1,3,-8,-2,-6],[4,7,5,-3,6,6,-6,7,1,5,8,-8,8,4,8,-6],[-7,6,-10,9,-6,6,-8,-10,-2,2,-3,-3,-8,-10,4,9],[-8,5,5,4,9,-5,-4,7,-10,-6,-1,3,-5,-6,-8,10],[1,5,-9,9,-10,8,-9,-10,6,-1,6,-6,6,9,8,-1]],[[-7,7,5,6,8,9,-9,-6,6,3,1,2,3,1,-3,10],[-9,7,-1,-9,-9,8,-7,4,-2,-5,6,2,9,3,-6,-3],[10,-8,3,1,6,-1,-4,8,1,10,-1,9,6,5,4,8],[7,6,3,-3,9,-4,6,10,5,5,2,7,5,-1,-9,-3],[-5,6,6,-9,-3,9,-2,7,9,-5,-5,3,4,8,-5,10]],[[10,9,7,-3,8,-10,-1,10,-8,-2,-7,4,9,7,-5,-5],[4,10,-2,2,5,2,8,5,-9,8,4,-7,3,8,-10,-2],[-4,8,5,6,3,-5,4,-6,7,-8,3,5,-1,4,3,-8],[8,5,-7,5,-10,10,10,-6,-7,9,10,-7,-6,-4,9,-8],[-7,2,3,-3,-10,9,-8,-1,9,-8,6,2,8,-1,-8,-6]],[[3,9,7,-10,-9,-1,6,-4,3,-4,7,1,1,-4,4,-4],[-10,-2,8,-4,-3,-4,6,-3,-9,-8,-6,4,4,6,10,2],[4,-6,7,9,-6,10,8,3,-2,-4,1,-6,9,-2,4,10],[-7,2,8,-6,4,-8,-9,2,3,10,5,10,9,-5,-5,3],[-1,10,6,-6,1,-5,-7,2,4,-6,9,4,-8,-1,4,-9]],[[-8,-4,2,-9,4,-3,-2,10,10,-4,2,7,7,-4,-3,-3],[9,-9,9,-8,-3,-5,8,10,3,-7,4,-4,-3,1,1,-8],[3,-5,-5,-5,-4,3,8,-9,7,-4,7,1,8,5,6,-2],[-9,1,-10,2,9,-5,9,5,-8,-7,1,-7,10,10,5,6],[1,-2,6,-6,-9,9,4,6,-5,1,2,4,-1,-7,8,-4]]], dtype = "uint32")#candidate|3733|(14, 5, 16)|const|uint32
bop_3734 = relay.not_equal(const_3732.astype('bool'), relay.reshape(const_3733.astype('bool'), relay.shape_of(const_3732))) # shape=(14, 5, 16)
uop_3739 = relay.log(bop_3734.astype('float64')) # shape=(14, 5, 16)
output = relay.Tuple([uop_3739,])
output2 = relay.Tuple([uop_3739,])
func_3741 = relay.Function([], output)
mod['func_3741'] = func_3741
mod = relay.transform.InferType()(mod)
mutated_mod['func_3741'] = func_3741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3741_call = mutated_mod.get_global_var('func_3741')
call_3742 = func_3741_call()
output = call_3742
func_3743 = relay.Function([], output)
mutated_mod['func_3743'] = func_3743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1228_call = mod.get_global_var('func_1228')
func_1230_call = mutated_mod.get_global_var('func_1230')
call_3749 = relay.TupleGetItem(func_1228_call(), 1)
call_3750 = relay.TupleGetItem(func_1230_call(), 1)
output = relay.Tuple([call_3749,])
output2 = relay.Tuple([call_3750,])
func_3770 = relay.Function([], output)
mod['func_3770'] = func_3770
mod = relay.transform.InferType()(mod)
mutated_mod['func_3770'] = func_3770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3770_call = mutated_mod.get_global_var('func_3770')
call_3771 = func_3770_call()
output = call_3771
func_3772 = relay.Function([], output)
mutated_mod['func_3772'] = func_3772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_681_call = mutated_mod.get_global_var('func_681')
call_3775 = relay.TupleGetItem(func_680_call(), 0)
call_3776 = relay.TupleGetItem(func_681_call(), 0)
output = call_3775
output2 = call_3776
func_3788 = relay.Function([], output)
mod['func_3788'] = func_3788
mod = relay.transform.InferType()(mod)
mutated_mod['func_3788'] = func_3788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3788_call = mutated_mod.get_global_var('func_3788')
call_3789 = func_3788_call()
output = call_3789
func_3790 = relay.Function([], output)
mutated_mod['func_3790'] = func_3790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_3793 = func_1207_call()
call_3794 = func_1207_call()
var_3805 = relay.var("var_3805", dtype = "float32", shape = (10, 9, 3))#candidate|3805|(10, 9, 3)|var|float32
bop_3806 = relay.subtract(call_3793.astype('uint32'), relay.reshape(var_3805.astype('uint32'), relay.shape_of(call_3793))) # shape=(10, 9, 3)
bop_3809 = relay.subtract(call_3794.astype('uint32'), relay.reshape(var_3805.astype('uint32'), relay.shape_of(call_3794))) # shape=(10, 9, 3)
func_3788_call = mod.get_global_var('func_3788')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_3813 = func_3788_call()
call_3814 = func_3788_call()
output = relay.Tuple([bop_3806,call_3813,])
output2 = relay.Tuple([bop_3809,call_3814,])
func_3817 = relay.Function([var_3805,], output)
mod['func_3817'] = func_3817
mod = relay.transform.InferType()(mod)
mutated_mod['func_3817'] = func_3817
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3818 = relay.var("var_3818", dtype = "float32", shape = (10, 9, 3))#candidate|3818|(10, 9, 3)|var|float32
func_3817_call = mutated_mod.get_global_var('func_3817')
call_3819 = func_3817_call(var_3818)
output = call_3819
func_3820 = relay.Function([var_3818], output)
mutated_mod['func_3820'] = func_3820
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3872 = relay.var("var_3872", dtype = "float64", shape = (1, 3, 3))#candidate|3872|(1, 3, 3)|var|float64
uop_3873 = relay.log2(var_3872.astype('float64')) # shape=(1, 3, 3)
uop_3882 = relay.cos(uop_3873.astype('float64')) # shape=(1, 3, 3)
func_3788_call = mod.get_global_var('func_3788')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_3886 = func_3788_call()
call_3887 = func_3788_call()
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_3888 = relay.TupleGetItem(func_968_call(), 2)
call_3889 = relay.TupleGetItem(func_970_call(), 2)
output = relay.Tuple([uop_3882,call_3886,call_3888,])
output2 = relay.Tuple([uop_3882,call_3887,call_3889,])
func_3891 = relay.Function([var_3872,], output)
mod['func_3891'] = func_3891
mod = relay.transform.InferType()(mod)
var_3892 = relay.var("var_3892", dtype = "float64", shape = (1, 3, 3))#candidate|3892|(1, 3, 3)|var|float64
output = func_3891(var_3892)
func_3893 = relay.Function([var_3892], output)
mutated_mod['func_3893'] = func_3893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1228_call = mod.get_global_var('func_1228')
func_1230_call = mutated_mod.get_global_var('func_1230')
call_3935 = relay.TupleGetItem(func_1228_call(), 1)
call_3936 = relay.TupleGetItem(func_1230_call(), 1)
output = call_3935
output2 = call_3936
func_3937 = relay.Function([], output)
mod['func_3937'] = func_3937
mod = relay.transform.InferType()(mod)
output = func_3937()
func_3938 = relay.Function([], output)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_3969 = func_609_call()
call_3970 = func_609_call()
func_3231_call = mod.get_global_var('func_3231')
func_3233_call = mutated_mod.get_global_var('func_3233')
const_3983 = relay.const([5,7,1,-1,7,3,-6,-1,1,-7,7,-7,-4,3,1,-5,4,-2,6,-1,-5,1,1,-8,-2,-1,2,-3,3,10,-10,2,-9,-2,-10,-5,7,-4,-8,3,7,10,4,-8,1,-2,-4,-8,1,-5,-3,3,8,10,-2,-7,1,-8,1,3,-5,7,-1,10,5,2,6,9,7,-2,-4,-7,4,-1,3,-9,9,6,10,-4,1,-6,1,3,-7,-8,1,8,-3,2,-1,4,6,-1,-8,-5,1,6,-7,2,3,4,5,9,1,6,4,-3,2,9,9,6,5,1,-2,-5,3,7,1,6,9,3,1,-4,-10,-2], dtype = "uint32")#candidate|3983|(126,)|const|uint32
call_3982 = relay.TupleGetItem(func_3231_call(relay.reshape(const_3983.astype('uint32'), [126,])), 0)
call_3984 = relay.TupleGetItem(func_3233_call(relay.reshape(const_3983.astype('uint32'), [126,])), 0)
func_882_call = mod.get_global_var('func_882')
func_883_call = mutated_mod.get_global_var('func_883')
call_3998 = func_882_call()
call_3999 = func_882_call()
func_2893_call = mod.get_global_var('func_2893')
func_2894_call = mutated_mod.get_global_var('func_2894')
call_4001 = relay.TupleGetItem(func_2893_call(), 0)
call_4002 = relay.TupleGetItem(func_2894_call(), 0)
func_3280_call = mod.get_global_var('func_3280')
func_3286_call = mutated_mod.get_global_var('func_3286')
var_4013 = relay.var("var_4013", dtype = "float32", shape = (800,))#candidate|4013|(800,)|var|float32
const_4014 = relay.const([[6.311151,6.306303,2.500220,-6.516310],[4.001447,-3.348815,-4.328709,-0.291829],[-8.264314,3.174935,-8.631839,-1.980451],[1.351127,5.578675,-1.349735,3.633282],[1.348280,5.713755,0.940532,-2.216204],[-4.368932,1.308340,-6.002916,1.361970],[5.824589,8.830779,8.791718,-1.723102],[-5.620783,-3.184364,1.407837,-8.687638],[-9.670087,8.477928,4.056145,-6.177122],[-5.823089,-4.328037,5.180999,-4.010832],[-2.642689,-9.734370,8.259546,-4.057192],[1.931301,-1.576115,5.510812,1.946081],[-4.457395,5.977986,-9.783873,5.437838],[3.440317,8.848471,-8.385724,8.354331],[-8.834294,-2.897895,-6.140294,7.760573],[2.769505,3.048715,-9.695632,8.088650],[0.774794,-5.375383,-5.982211,7.961894],[1.356423,9.785954,-8.653682,-6.184837],[-4.002184,-8.108009,-7.936945,-1.196363],[2.996211,-2.713316,4.808688,-6.006032],[-1.779507,-7.951596,-8.251791,4.832159],[8.846388,5.541548,6.483577,-2.580219],[-0.666710,5.010439,-9.954897,5.733349],[3.812499,2.578966,1.196960,1.790071],[-7.040786,-6.590576,0.549714,-2.477075],[-1.280155,-5.967650,9.777358,-5.855722],[9.271140,-3.003671,5.259896,7.591001],[5.977146,8.643651,-6.927165,2.095194],[2.055188,-9.277873,6.576062,3.564323],[-3.139795,8.465365,-4.605378,-9.127854],[1.732047,3.024019,-7.688087,5.731848],[3.492265,-9.099762,-4.633753,-1.257383],[2.810051,-9.807043,7.996173,1.640581],[-5.595730,9.608290,-9.127333,-2.638627],[8.360490,-7.845105,3.255691,8.814756],[1.333694,-4.254556,6.841682,4.732891],[2.126701,8.920764,8.047217,8.501853],[-7.906077,-5.842820,-1.081631,-5.031384],[-4.700484,3.265071,8.904319,-1.565149],[-2.130230,-2.029067,4.873438,-5.137150],[6.055342,4.574079,-9.450234,-6.420762],[4.787629,6.848406,-6.697375,9.697465],[6.671851,-2.685286,-6.986829,6.721040],[1.342880,-5.666682,0.668718,-8.066319],[7.942903,2.738561,-3.027422,-3.825854],[-8.553420,5.104083,5.415009,6.211640],[1.697176,1.085373,-8.948017,-8.211911],[-8.204293,-5.717324,7.633217,4.567238],[-4.838763,1.112772,-5.896935,-9.172354],[7.260472,9.309834,4.566558,1.426532],[-3.535815,-6.587120,9.359457,7.975056],[0.105145,7.942853,-0.934118,8.152411],[1.364521,7.991153,-2.933538,-5.739097],[7.724660,1.864012,-7.864246,5.913339],[4.170857,3.774775,-5.962519,0.598096],[-0.223728,-6.118458,7.743338,1.751492],[-1.177740,-6.596357,9.325142,1.435066],[6.165091,7.929263,8.025450,-4.237816],[-1.586398,-3.101227,-7.280479,-6.695965],[-8.444246,1.751781,2.450557,3.704855],[2.673557,-3.719327,-0.318947,3.799495],[-2.385714,-4.513942,4.650390,4.761286],[-1.898659,-1.984637,7.019962,-4.784002],[-6.566039,2.601535,-7.866287,4.746640],[-5.394751,-1.470850,6.826028,-5.471620],[-5.547669,-7.662814,-4.808950,1.617817],[4.321138,8.389857,2.290086,-8.398281],[-0.928255,8.639448,-3.236447,-7.437530],[-7.694555,-4.311746,4.442849,-1.778042],[0.236885,5.020822,-3.236713,-4.075732],[1.711491,-1.447797,4.953726,-3.886197],[-9.088768,0.938921,-2.057336,0.682570],[-4.668357,7.365940,0.068479,-1.714159],[-0.952686,-2.193151,-8.092215,-5.315701],[-0.056130,-0.093595,8.115114,7.857071],[-4.462622,3.677072,6.161433,-0.381810],[-7.588794,0.653953,9.588941,-0.854539],[7.102782,-5.344774,8.836498,7.716627],[2.755715,-5.453006,-3.968509,-9.296836],[-9.899137,-9.886305,-7.009890,2.248464],[-1.721045,-9.715211,-4.635914,9.591848],[0.625366,-3.856974,-8.921361,0.479174],[0.661941,-5.600270,0.028174,7.322173],[-1.175846,7.412905,-8.829103,7.273098],[3.026868,-7.900050,-8.904416,-3.586582],[6.937366,6.591974,-5.181653,6.520162],[-0.902956,-4.249304,-7.710226,5.080041],[2.342295,6.690366,0.083173,-0.166457],[1.700407,9.411301,-3.813468,8.007085],[-0.341743,2.580085,9.694605,-0.412452],[-5.888232,-8.672393,-3.912229,-6.910701],[-3.114804,4.763816,-0.560887,2.349726],[-8.986723,-8.596429,-3.136783,-8.366768],[-6.950707,8.779936,-0.688618,6.067595],[-2.898897,3.043708,1.866671,-7.653820],[-2.842734,0.448315,6.265833,-3.261008],[2.146673,-0.516204,-2.287912,-5.657761],[-1.257976,4.255345,-7.512597,-2.807023],[-8.823008,8.877866,3.334698,9.234195],[-3.399398,-3.557864,7.975094,2.665320],[6.946900,-5.571578,0.879630,-5.691369],[9.116187,-0.951470,-0.373850,-4.586238],[1.494565,-2.780616,-5.883209,-5.130858],[3.977742,-9.601069,9.973264,3.149769],[-2.116062,-7.615010,0.234372,6.733116],[-1.531259,-3.491205,-1.819638,5.734985],[-1.299700,-0.613227,-2.170228,9.318046],[-5.042972,-1.578998,-3.125460,-0.413904],[-3.315997,-8.785756,-6.407301,-3.771189],[8.545542,1.165216,1.825529,1.836658],[9.520630,-9.240872,-7.066241,1.947216],[-9.046499,-8.248802,0.205605,2.831522],[-6.980753,5.214806,2.792033,9.745152],[-1.891971,9.227069,-5.593252,-2.581413],[-5.934676,7.560182,-2.165812,6.134910],[-5.647928,8.848334,0.965858,4.420812],[-1.521874,-7.599451,-5.630430,0.669373],[-9.849597,9.052551,5.002861,-3.499897],[-5.591637,1.370999,-3.842249,3.092064],[-6.889007,4.540537,5.322900,2.441277],[3.578281,-5.065636,-7.622628,3.174090],[-1.628797,2.096749,-5.034440,9.642384],[9.621856,9.755494,-5.396192,-9.960950],[-5.708895,-6.510645,9.097859,9.344205],[2.695478,-1.440165,3.484660,-0.130009],[-5.673688,-6.184910,-9.490705,-5.534971],[-8.635848,9.446379,-5.310681,6.412042],[9.781512,3.147986,-2.671731,-0.435036],[-4.413371,2.939062,-8.044587,0.004291],[6.597666,3.239025,7.395229,0.836715],[6.143325,-4.594222,-0.765559,-4.812310],[1.131559,-0.553980,9.886828,9.724242],[-5.911202,9.591974,6.069844,9.793811],[-7.105241,-8.038940,-8.483667,9.899421],[-1.684991,-1.661701,-2.209325,8.751452],[-2.368279,8.515541,-9.262134,3.358145],[1.380004,2.352854,6.619331,4.227198],[3.813727,9.032270,4.613490,2.412024],[1.965114,-1.248356,9.198762,9.993003],[-6.583004,5.253753,-3.373185,1.228743],[9.895451,-3.143402,5.261271,8.838742],[5.065434,7.405584,7.563182,-7.834433],[-9.592721,-8.887020,-2.560544,2.675377],[-8.350694,0.025780,6.873584,-1.844174],[1.975653,3.570349,-4.693088,3.197061],[5.830407,-3.211894,-1.978076,9.624840],[-0.498323,-1.165749,-0.565514,4.060924],[-8.459747,7.227715,1.460650,-1.096693],[-2.894863,7.160891,-9.815099,-1.270944],[9.746386,0.798896,3.437974,-1.613319],[-1.543637,1.736820,-7.676248,-9.552919],[5.556123,-5.315723,1.857522,-1.953997],[-7.370529,0.243732,-3.618675,9.016362],[-6.218854,6.835480,2.035291,8.856100],[-4.873040,-1.103662,8.271758,4.720301],[-7.723549,0.562026,6.746006,7.036686],[-8.763379,-3.835554,-6.880201,-0.131096],[-6.985480,4.739852,-8.638618,-5.924565],[7.443002,2.807291,5.966596,1.027924],[3.357487,0.231967,-6.549151,-3.693468],[7.496619,-2.602811,-9.371695,4.728178],[-9.280653,9.955639,8.667986,-1.538972],[-4.282747,-1.487844,-0.228231,-0.745613],[-9.189947,-9.826248,-4.741976,9.900895],[-7.125839,-9.135747,1.083514,3.658031],[-4.324150,-8.630754,-1.895611,-3.357735],[-5.465377,-8.597414,-6.691382,-9.405904],[6.386443,-8.729414,-4.028295,2.695957],[4.678230,4.962763,7.324886,-0.078968],[4.934126,-3.164871,3.428636,0.669903],[9.859753,6.824426,-1.200438,-9.882112],[-4.050009,5.349718,6.310489,6.702119],[-1.714144,0.817639,-7.031166,9.521433],[-9.907428,1.815426,-7.038933,0.265866],[4.536749,-2.441592,0.743986,6.766897],[5.655744,-1.378003,0.746732,1.465801],[-0.190770,-9.903466,-4.162890,7.732276],[6.815966,1.857150,6.222628,1.637254],[2.141788,-4.798084,-6.043977,-0.256725],[-8.325004,-2.085549,6.871154,-0.569856],[-5.978280,-7.310576,-9.673723,3.508466],[-8.035042,-5.885767,-2.138961,-5.604282],[8.308597,-1.877371,-1.107674,0.585015],[8.257277,8.511246,8.397948,-3.081996],[-3.996026,-2.497879,-5.019155,-3.435998],[-9.935808,-2.447519,-3.146625,-6.464950],[9.851526,2.131960,-4.767668,5.224214],[2.551738,-2.805927,-3.240713,-1.261670],[7.348451,7.033802,1.105681,-2.634185],[-2.988594,-0.020893,-7.870775,-5.015747],[0.404455,7.532232,-5.791119,4.680400],[6.115921,-0.625777,-5.988058,-2.231717],[-4.060007,-5.984681,9.355285,8.351145],[1.366086,-2.804827,8.207110,-0.035914],[6.247658,-5.940712,-6.291917,9.455082],[7.344161,3.752694,-3.878504,4.452340],[9.986105,-4.833698,-0.470318,3.889872],[6.913429,0.721321,-0.224117,1.959159],[-9.422543,-4.101342,6.264110,-8.248983],[4.057374,8.069431,-3.584693,-9.288178],[-8.249496,-2.790982,3.387311,-5.797603],[-5.630870,2.661721,1.880383,-7.747122],[-5.006984,-2.876680,-0.545008,-3.003945],[-3.307933,2.511178,-0.998992,0.058138],[5.031244,7.508571,4.881355,7.507580],[-7.802833,-0.249976,-0.620037,7.063887],[5.233785,-5.171497,-6.396810,-6.509444],[-5.134335,1.906662,6.666895,5.375284],[5.605405,6.919637,5.296076,-6.178175],[6.523331,4.384635,5.446056,-4.604692],[1.479278,-4.990953,2.017608,-2.315170],[-2.976724,-6.244764,-0.239450,-3.178562],[1.707361,-5.906380,0.973694,-0.121340],[-3.591172,-9.694474,-6.117665,-4.308101],[7.892656,2.378642,7.791814,2.056123],[-9.851038,-3.704367,5.917113,-2.245266]], dtype = "float32")#candidate|4014|(216, 4)|const|float32
var_4015 = relay.var("var_4015", dtype = "uint32", shape = (640,))#candidate|4015|(640,)|var|uint32
call_4012 = relay.TupleGetItem(func_3280_call(relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(const_4014.astype('float32'), [864,]), relay.reshape(var_4015.astype('uint32'), [640,]), relay.reshape(const_3983.astype('uint32'), [126,]), ), 2)
call_4016 = relay.TupleGetItem(func_3286_call(relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(const_4014.astype('float32'), [864,]), relay.reshape(var_4015.astype('uint32'), [640,]), relay.reshape(const_3983.astype('uint32'), [126,]), ), 2)
func_3280_call = mod.get_global_var('func_3280')
func_3286_call = mutated_mod.get_global_var('func_3286')
call_4032 = relay.TupleGetItem(func_3280_call(relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(const_4014.astype('float32'), [864,]), relay.reshape(var_4015.astype('uint32'), [640,]), relay.reshape(const_3983.astype('uint32'), [126,]), ), 0)
call_4033 = relay.TupleGetItem(func_3286_call(relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(var_4013.astype('float32'), [5, 16, 10]), relay.reshape(const_4014.astype('float32'), [864,]), relay.reshape(var_4015.astype('uint32'), [640,]), relay.reshape(const_3983.astype('uint32'), [126,]), ), 0)
output = relay.Tuple([call_3969,call_3982,const_3983,call_3998,call_4001,call_4012,var_4013,const_4014,var_4015,call_4032,])
output2 = relay.Tuple([call_3970,call_3984,const_3983,call_3999,call_4002,call_4016,var_4013,const_4014,var_4015,call_4033,])
func_4052 = relay.Function([var_4013,var_4015,], output)
mod['func_4052'] = func_4052
mod = relay.transform.InferType()(mod)
var_4053 = relay.var("var_4053", dtype = "float32", shape = (800,))#candidate|4053|(800,)|var|float32
var_4054 = relay.var("var_4054", dtype = "uint32", shape = (640,))#candidate|4054|(640,)|var|uint32
output = func_4052(var_4053,var_4054,)
func_4055 = relay.Function([var_4053,var_4054,], output)
mutated_mod['func_4055'] = func_4055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2591_call = mutated_mod.get_global_var('func_2591')
call_4082 = relay.TupleGetItem(func_2589_call(), 1)
call_4083 = relay.TupleGetItem(func_2591_call(), 1)
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_4106 = relay.TupleGetItem(func_2968_call(), 0)
call_4107 = relay.TupleGetItem(func_2969_call(), 0)
func_3027_call = mod.get_global_var('func_3027')
func_3029_call = mutated_mod.get_global_var('func_3029')
call_4116 = func_3027_call()
call_4117 = func_3027_call()
bop_4119 = relay.logical_xor(call_4106.astype('int8'), relay.reshape(call_4082.astype('int8'), relay.shape_of(call_4106))) # shape=(10, 9, 3)
bop_4122 = relay.logical_xor(call_4107.astype('int8'), relay.reshape(call_4083.astype('int8'), relay.shape_of(call_4107))) # shape=(10, 9, 3)
output = relay.Tuple([call_4116,bop_4119,])
output2 = relay.Tuple([call_4117,bop_4122,])
func_4130 = relay.Function([], output)
mod['func_4130'] = func_4130
mod = relay.transform.InferType()(mod)
mutated_mod['func_4130'] = func_4130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mutated_mod.get_global_var('func_4130')
call_4131 = func_4130_call()
output = call_4131
func_4132 = relay.Function([], output)
mutated_mod['func_4132'] = func_4132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1173_call = mod.get_global_var('func_1173')
func_1174_call = mutated_mod.get_global_var('func_1174')
call_4133 = relay.TupleGetItem(func_1173_call(), 0)
call_4134 = relay.TupleGetItem(func_1174_call(), 0)
output = call_4133
output2 = call_4134
func_4162 = relay.Function([], output)
mod['func_4162'] = func_4162
mod = relay.transform.InferType()(mod)
mutated_mod['func_4162'] = func_4162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mutated_mod.get_global_var('func_4162')
call_4163 = func_4162_call()
output = call_4163
func_4164 = relay.Function([], output)
mutated_mod['func_4164'] = func_4164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_4173 = relay.TupleGetItem(func_1370_call(), 0)
call_4174 = relay.TupleGetItem(func_1371_call(), 0)
uop_4179 = relay.acosh(call_4173.astype('float32')) # shape=(4, 15, 4)
uop_4181 = relay.acosh(call_4174.astype('float32')) # shape=(4, 15, 4)
output = uop_4179
output2 = uop_4181
func_4183 = relay.Function([], output)
mod['func_4183'] = func_4183
mod = relay.transform.InferType()(mod)
output = func_4183()
func_4184 = relay.Function([], output)
mutated_mod['func_4184'] = func_4184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3741_call = mod.get_global_var('func_3741')
func_3743_call = mutated_mod.get_global_var('func_3743')
call_4237 = relay.TupleGetItem(func_3741_call(), 0)
call_4238 = relay.TupleGetItem(func_3743_call(), 0)
func_3231_call = mod.get_global_var('func_3231')
func_3233_call = mutated_mod.get_global_var('func_3233')
var_4240 = relay.var("var_4240", dtype = "uint32", shape = (126,))#candidate|4240|(126,)|var|uint32
call_4239 = relay.TupleGetItem(func_3231_call(relay.reshape(var_4240.astype('uint32'), [126,])), 0)
call_4241 = relay.TupleGetItem(func_3233_call(relay.reshape(var_4240.astype('uint32'), [126,])), 0)
func_4052_call = mod.get_global_var('func_4052')
func_4055_call = mutated_mod.get_global_var('func_4055')
var_4247 = relay.var("var_4247", dtype = "float32", shape = (800,))#candidate|4247|(800,)|var|float32
const_4248 = relay.const([[3,-2,8,8,3,-9,9,3,9,-1,-10,1,6,-6,7,10,7,-9,-5,-2,4,9,5,5,7,-6,7,-3,-5,-4,1,2,-5,7,-6,10,-8,-5,2,-6,-10,-8,-2,-9,-9,9,4,-10,-10,9,-5,10,-10,6,-7,-3,-7,-3,1,7,-5,-10,8,8],[-8,-6,9,-8,-10,-3,1,5,6,-8,-2,-6,1,-5,-7,-9,-1,-10,10,1,4,-9,1,-2,4,3,7,2,-7,-1,8,-3,-2,1,-3,-1,6,4,8,4,8,-9,-1,6,-5,-4,4,4,-10,-9,-9,10,2,5,-1,-3,8,-5,10,7,-8,-10,6,-10],[1,9,-10,7,2,4,-1,-4,9,-8,-3,-4,-5,3,8,-8,-3,-1,6,8,10,-5,1,9,-9,6,-3,-4,5,-2,3,6,-8,10,4,6,-2,-4,8,-10,4,2,-10,-8,4,-10,3,-4,2,7,-3,-2,1,7,-1,8,-7,-3,-7,-2,2,-9,-7,-5],[8,-6,4,8,-4,-5,-4,-8,-5,7,-3,-4,-10,-1,-7,-7,10,-8,1,-10,-2,10,9,-8,1,8,-4,-3,7,-1,-2,-1,-4,-9,-4,-10,3,6,-9,8,-10,6,-1,6,4,-4,8,1,2,-8,8,-7,-7,-4,-7,-6,1,9,-2,-9,6,5,7,-7],[7,-9,3,-5,-9,7,-3,3,9,-3,-8,-7,8,-10,7,5,-1,8,-10,-4,-6,-5,8,-1,9,-7,-10,3,8,2,9,1,2,5,6,3,4,9,5,8,5,2,2,3,9,7,-5,-1,8,10,-5,4,-10,-1,4,-8,-7,-6,8,-10,7,6,-4,8],[10,7,-1,-7,7,-6,9,2,6,6,-9,10,4,9,-2,-1,5,2,-3,8,8,9,-10,5,10,10,10,9,-6,1,5,2,3,9,10,-4,-1,-8,-5,-9,-6,6,8,9,4,-2,5,-1,6,2,7,-6,10,-1,9,-2,8,-3,5,-10,6,-10,-8,9],[2,1,9,10,-3,4,3,-7,4,-9,3,-8,3,-8,-10,6,8,1,-5,7,-2,-8,-7,-7,-6,-1,-8,-8,8,4,4,-8,-5,2,-10,8,9,8,-4,10,1,-8,10,-10,3,6,3,-2,5,-8,10,-6,3,-9,-8,6,-8,-10,2,9,-3,-5,-1,5],[-8,8,1,10,-7,-1,-6,6,-3,6,-6,5,10,-6,-6,6,5,5,-9,8,-4,2,-7,-5,5,-8,-6,2,2,8,10,5,9,1,-2,5,9,-7,-8,-7,-4,5,7,-8,7,8,-10,-3,2,7,5,2,-1,-10,-1,-3,-3,7,-8,-10,10,2,-2,9],[1,10,9,-9,10,1,-6,6,-3,-1,7,7,3,7,6,-1,-3,-2,2,-3,1,-4,8,-8,3,3,-3,5,-10,3,-8,5,-3,4,-8,-8,2,-10,9,5,-9,2,-1,-10,-1,8,-5,-3,-10,6,7,-9,-3,1,-8,6,7,1,-6,10,6,-9,1,-1],[-10,-10,-10,-5,-9,7,-5,5,10,1,-9,-5,8,-7,-5,-9,7,9,-10,10,-3,5,9,-3,7,7,4,2,4,-1,10,-4,-9,6,-9,9,5,-1,3,5,7,-6,4,3,7,-8,3,-6,5,4,-2,6,-4,-2,-3,6,9,-1,10,-10,7,6,10,-4]], dtype = "uint32")#candidate|4248|(10, 64)|const|uint32
call_4246 = relay.TupleGetItem(func_4052_call(relay.reshape(var_4247.astype('float32'), [800,]), relay.reshape(const_4248.astype('uint32'), [640,]), ), 4)
call_4249 = relay.TupleGetItem(func_4055_call(relay.reshape(var_4247.astype('float32'), [800,]), relay.reshape(const_4248.astype('uint32'), [640,]), ), 4)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_4258 = func_429_call()
call_4259 = func_429_call()
func_4052_call = mod.get_global_var('func_4052')
func_4055_call = mutated_mod.get_global_var('func_4055')
call_4270 = relay.TupleGetItem(func_4052_call(relay.reshape(var_4247.astype('float32'), [800,]), relay.reshape(const_4248.astype('uint32'), [640,]), ), 1)
call_4271 = relay.TupleGetItem(func_4055_call(relay.reshape(var_4247.astype('float32'), [800,]), relay.reshape(const_4248.astype('uint32'), [640,]), ), 1)
output = relay.Tuple([call_4237,call_4239,var_4240,call_4246,var_4247,const_4248,call_4258,call_4270,])
output2 = relay.Tuple([call_4238,call_4241,var_4240,call_4249,var_4247,const_4248,call_4259,call_4271,])
func_4272 = relay.Function([var_4240,var_4247,], output)
mod['func_4272'] = func_4272
mod = relay.transform.InferType()(mod)
var_4273 = relay.var("var_4273", dtype = "uint32", shape = (126,))#candidate|4273|(126,)|var|uint32
var_4274 = relay.var("var_4274", dtype = "float32", shape = (800,))#candidate|4274|(800,)|var|float32
output = func_4272(var_4273,var_4274,)
func_4275 = relay.Function([var_4273,var_4274,], output)
mutated_mod['func_4275'] = func_4275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_681_call = mutated_mod.get_global_var('func_681')
call_4319 = relay.TupleGetItem(func_680_call(), 0)
call_4320 = relay.TupleGetItem(func_681_call(), 0)
func_1148_call = mod.get_global_var('func_1148')
func_1150_call = mutated_mod.get_global_var('func_1150')
var_4361 = relay.var("var_4361", dtype = "uint32", shape = (126,))#candidate|4361|(126,)|var|uint32
call_4360 = relay.TupleGetItem(func_1148_call(relay.reshape(var_4361.astype('uint32'), [126,])), 0)
call_4362 = relay.TupleGetItem(func_1150_call(relay.reshape(var_4361.astype('uint32'), [126,])), 0)
output = relay.Tuple([call_4319,call_4360,var_4361,])
output2 = relay.Tuple([call_4320,call_4362,var_4361,])
func_4370 = relay.Function([var_4361,], output)
mod['func_4370'] = func_4370
mod = relay.transform.InferType()(mod)
var_4371 = relay.var("var_4371", dtype = "uint32", shape = (126,))#candidate|4371|(126,)|var|uint32
output = func_4370(var_4371)
func_4372 = relay.Function([var_4371], output)
mutated_mod['func_4372'] = func_4372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3027_call = mod.get_global_var('func_3027')
func_3029_call = mutated_mod.get_global_var('func_3029')
call_4397 = func_3027_call()
call_4398 = func_3027_call()
uop_4401 = relay.sin(call_4397.astype('float64')) # shape=(4, 15, 4)
uop_4403 = relay.sin(call_4398.astype('float64')) # shape=(4, 15, 4)
func_3613_call = mod.get_global_var('func_3613')
func_3614_call = mutated_mod.get_global_var('func_3614')
call_4405 = relay.TupleGetItem(func_3613_call(), 0)
call_4406 = relay.TupleGetItem(func_3614_call(), 0)
bop_4409 = relay.add(uop_4401.astype('float32'), relay.reshape(call_4397.astype('float32'), relay.shape_of(uop_4401))) # shape=(4, 15, 4)
bop_4412 = relay.add(uop_4403.astype('float32'), relay.reshape(call_4398.astype('float32'), relay.shape_of(uop_4403))) # shape=(4, 15, 4)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_4413 = relay.TupleGetItem(func_4130_call(), 1)
call_4414 = relay.TupleGetItem(func_4132_call(), 1)
func_626_call = mod.get_global_var('func_626')
func_627_call = mutated_mod.get_global_var('func_627')
call_4425 = func_626_call()
call_4426 = func_626_call()
output = relay.Tuple([call_4405,bop_4409,call_4413,call_4425,])
output2 = relay.Tuple([call_4406,bop_4412,call_4414,call_4426,])
func_4430 = relay.Function([], output)
mod['func_4430'] = func_4430
mod = relay.transform.InferType()(mod)
mutated_mod['func_4430'] = func_4430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4430_call = mutated_mod.get_global_var('func_4430')
call_4431 = func_4430_call()
output = call_4431
func_4432 = relay.Function([], output)
mutated_mod['func_4432'] = func_4432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_4498 = relay.TupleGetItem(func_703_call(), 0)
call_4499 = relay.TupleGetItem(func_705_call(), 0)
func_3440_call = mod.get_global_var('func_3440')
func_3443_call = mutated_mod.get_global_var('func_3443')
var_4506 = relay.var("var_4506", dtype = "float64", shape = (480,))#candidate|4506|(480,)|var|float64
call_4505 = relay.TupleGetItem(func_3440_call(relay.reshape(var_4506.astype('float64'), [2, 15, 16])), 2)
call_4507 = relay.TupleGetItem(func_3443_call(relay.reshape(var_4506.astype('float64'), [2, 15, 16])), 2)
func_4183_call = mod.get_global_var('func_4183')
func_4184_call = mutated_mod.get_global_var('func_4184')
call_4512 = func_4183_call()
call_4513 = func_4183_call()
output = relay.Tuple([call_4498,call_4505,var_4506,call_4512,])
output2 = relay.Tuple([call_4499,call_4507,var_4506,call_4513,])
func_4527 = relay.Function([var_4506,], output)
mod['func_4527'] = func_4527
mod = relay.transform.InferType()(mod)
var_4528 = relay.var("var_4528", dtype = "float64", shape = (480,))#candidate|4528|(480,)|var|float64
output = func_4527(var_4528)
func_4529 = relay.Function([var_4528], output)
mutated_mod['func_4529'] = func_4529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2591_call = mutated_mod.get_global_var('func_2591')
call_4537 = relay.TupleGetItem(func_2589_call(), 1)
call_4538 = relay.TupleGetItem(func_2591_call(), 1)
func_3440_call = mod.get_global_var('func_3440')
func_3443_call = mutated_mod.get_global_var('func_3443')
var_4546 = relay.var("var_4546", dtype = "float64", shape = (480,))#candidate|4546|(480,)|var|float64
call_4545 = relay.TupleGetItem(func_3440_call(relay.reshape(var_4546.astype('float64'), [2, 15, 16])), 2)
call_4547 = relay.TupleGetItem(func_3443_call(relay.reshape(var_4546.astype('float64'), [2, 15, 16])), 2)
func_2102_call = mod.get_global_var('func_2102')
func_2104_call = mutated_mod.get_global_var('func_2104')
call_4571 = func_2102_call()
call_4572 = func_2102_call()
output = relay.Tuple([call_4537,call_4545,var_4546,call_4571,])
output2 = relay.Tuple([call_4538,call_4547,var_4546,call_4572,])
func_4578 = relay.Function([var_4546,], output)
mod['func_4578'] = func_4578
mod = relay.transform.InferType()(mod)
var_4579 = relay.var("var_4579", dtype = "float64", shape = (480,))#candidate|4579|(480,)|var|float64
output = func_4578(var_4579)
func_4580 = relay.Function([var_4579], output)
mutated_mod['func_4580'] = func_4580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_4644 = func_609_call()
call_4645 = func_609_call()
func_3231_call = mod.get_global_var('func_3231')
func_3233_call = mutated_mod.get_global_var('func_3233')
const_4647 = relay.const([-9,-1,2,-6,-5,-7,10,10,4,1,-2,7,4,-6,-10,7,10,8,7,-10,-1,-9,-6,7,3,-9,-8,4,8,-3,4,10,9,5,-3,6,-4,5,8,-8,-1,-7,-5,2,-10,4,4,-6,-3,9,-8,10,-2,1,-8,-2,-6,-7,-9,-4,4,10,3,3,9,-2,8,8,-6,1,-8,2,-9,6,-7,-6,-10,9,4,-7,-3,-1,-10,3,10,9,-5,3,-9,-4,1,9,6,-5,1,7,-3,-7,9,-1,3,6,-3,4,8,-10,5,8,-9,-4,-7,6,-1,-2,-4,9,3,5,-4,7,4,9,-9,3,-2,-10], dtype = "uint32")#candidate|4647|(126,)|const|uint32
call_4646 = relay.TupleGetItem(func_3231_call(relay.reshape(const_4647.astype('uint32'), [126,])), 4)
call_4648 = relay.TupleGetItem(func_3233_call(relay.reshape(const_4647.astype('uint32'), [126,])), 4)
output = relay.Tuple([call_4644,call_4646,const_4647,])
output2 = relay.Tuple([call_4645,call_4648,const_4647,])
func_4660 = relay.Function([], output)
mod['func_4660'] = func_4660
mod = relay.transform.InferType()(mod)
mutated_mod['func_4660'] = func_4660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4660_call = mutated_mod.get_global_var('func_4660')
call_4661 = func_4660_call()
output = call_4661
func_4662 = relay.Function([], output)
mutated_mod['func_4662'] = func_4662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1228_call = mod.get_global_var('func_1228')
func_1230_call = mutated_mod.get_global_var('func_1230')
call_4663 = relay.TupleGetItem(func_1228_call(), 0)
call_4664 = relay.TupleGetItem(func_1230_call(), 0)
output = relay.Tuple([call_4663,])
output2 = relay.Tuple([call_4664,])
func_4689 = relay.Function([], output)
mod['func_4689'] = func_4689
mod = relay.transform.InferType()(mod)
output = func_4689()
func_4690 = relay.Function([], output)
mutated_mod['func_4690'] = func_4690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3770_call = mod.get_global_var('func_3770')
func_3772_call = mutated_mod.get_global_var('func_3772')
call_4711 = relay.TupleGetItem(func_3770_call(), 0)
call_4712 = relay.TupleGetItem(func_3772_call(), 0)
const_4715 = relay.const([[[True,True,True],[True,False,True],[False,True,False],[True,True,False],[True,False,False],[True,False,False],[False,True,True],[True,False,True],[False,True,False]],[[True,True,True],[True,False,False],[True,False,True],[False,False,False],[True,False,False],[True,True,False],[True,False,True],[False,False,False],[True,False,False]],[[False,False,False],[False,True,True],[True,True,False],[False,False,False],[True,False,False],[True,True,False],[True,True,True],[False,False,True],[True,False,False]],[[True,True,False],[True,False,False],[True,False,False],[True,False,True],[True,False,True],[True,True,True],[True,False,True],[False,False,False],[True,False,False]],[[True,True,True],[True,False,False],[True,True,False],[True,True,True],[True,False,True],[False,True,True],[True,False,False],[True,True,False],[False,True,False]],[[False,True,False],[False,False,True],[True,True,True],[False,False,True],[False,True,False],[True,True,False],[False,True,True],[True,True,True],[True,False,False]],[[False,False,False],[False,False,True],[True,False,True],[False,False,False],[False,False,False],[True,False,True],[True,False,False],[True,False,False],[False,False,True]],[[True,True,True],[True,True,True],[True,False,True],[False,True,True],[True,True,True],[True,True,True],[True,False,False],[True,True,False],[True,False,False]],[[True,False,False],[False,True,False],[True,True,True],[False,False,True],[True,True,False],[True,False,False],[False,False,True],[False,True,False],[False,False,True]],[[False,False,False],[False,True,False],[True,False,False],[True,True,True],[False,False,True],[False,True,False],[False,False,True],[False,True,True],[False,True,False]]], dtype = "bool")#candidate|4715|(10, 9, 3)|const|bool
bop_4716 = relay.bitwise_or(call_4711.astype('int8'), relay.reshape(const_4715.astype('int8'), relay.shape_of(call_4711))) # shape=(10, 9, 3)
bop_4719 = relay.bitwise_or(call_4712.astype('int8'), relay.reshape(const_4715.astype('int8'), relay.shape_of(call_4712))) # shape=(10, 9, 3)
output = bop_4716
output2 = bop_4719
func_4722 = relay.Function([], output)
mod['func_4722'] = func_4722
mod = relay.transform.InferType()(mod)
output = func_4722()
func_4723 = relay.Function([], output)
mutated_mod['func_4723'] = func_4723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4660_call = mod.get_global_var('func_4660')
func_4662_call = mutated_mod.get_global_var('func_4662')
call_4724 = relay.TupleGetItem(func_4660_call(), 2)
call_4725 = relay.TupleGetItem(func_4662_call(), 2)
output = call_4724
output2 = call_4725
func_4727 = relay.Function([], output)
mod['func_4727'] = func_4727
mod = relay.transform.InferType()(mod)
mutated_mod['func_4727'] = func_4727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4727_call = mutated_mod.get_global_var('func_4727')
call_4728 = func_4727_call()
output = call_4728
func_4729 = relay.Function([], output)
mutated_mod['func_4729'] = func_4729
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4732 = relay.const([[[-4.263756,1.008494,-2.076070,7.779939,2.533184,6.921516,7.548103,6.415256,-1.419830,9.741384,-4.185036,-5.041680,8.908208],[-7.558625,-2.717958,7.968762,1.329312,4.372747,1.703917,8.432769,-2.471159,-4.880599,-0.515520,9.113368,-7.091000,-6.258888],[-7.169891,6.184662,-7.033172,-4.041532,3.624667,-2.780126,-2.958224,-9.517394,-3.083789,-6.551642,-1.701190,-5.584377,-9.083420],[-1.565448,9.951717,8.804666,5.084515,8.372446,0.383433,6.437039,1.402947,1.034491,7.884464,6.424722,-0.379273,-0.411699],[-7.960333,4.021594,-7.732973,3.458661,-5.566424,3.852377,3.344111,-5.657568,-6.244221,4.273119,7.454240,-2.765858,8.753121],[-0.238852,9.691296,-6.919498,8.537479,5.936850,7.911590,1.927351,3.737124,-5.128063,-0.567352,0.887013,-6.267988,-8.354382],[-2.561100,-2.143333,9.838527,5.542377,4.212727,-0.155274,8.490267,-3.128855,1.157923,0.185728,-6.013082,1.286318,-8.640918],[4.900724,-6.885099,-6.656479,-8.526527,-6.379626,8.754934,2.819660,2.533963,5.008541,1.045474,-7.722471,-0.467462,7.442081],[0.041955,9.849610,-8.059888,-0.359767,-1.559132,3.075903,5.359952,-5.976197,6.639212,5.916845,-9.768047,9.496691,-2.680458],[-9.907302,2.860292,4.110515,-5.785663,-2.555398,8.744117,7.518081,5.135959,2.853673,-2.005320,7.543328,4.519140,4.704014],[-4.625507,9.837912,-5.446420,3.643135,4.004092,-0.075314,0.982586,-1.383031,9.676319,-6.760137,-2.754920,0.858906,-2.902355],[-9.350209,9.997810,4.012489,1.227570,-7.625777,-1.711481,1.996847,-2.920822,4.926200,7.295938,-6.568244,-6.385825,5.859794],[-6.990805,6.149474,-4.010542,-0.317841,3.489078,2.447894,-2.986124,-8.146145,1.364931,0.118566,3.293382,9.942541,-3.233080],[6.516358,-1.047721,-6.252910,9.419822,8.792097,1.869028,6.226706,6.805511,8.614393,-3.924034,-3.297469,-0.088456,6.742250],[7.427637,-2.207691,3.646989,-4.684635,-4.738683,-3.405651,-9.894493,7.975270,-4.241948,8.439836,4.781115,7.065865,-7.466523]],[[7.930792,8.712827,4.852524,1.646991,9.247152,1.945346,6.178575,-0.161387,-9.386126,6.675285,-0.659527,-3.700313,-6.444115],[6.010263,-6.811148,0.225851,-7.383832,-7.843970,0.002883,7.490300,-3.176985,-7.480256,-2.385216,-1.206059,-0.537673,1.693047],[5.098273,-3.055822,1.680957,7.071160,7.076345,-7.824970,-2.909787,2.563810,-2.667254,-0.798435,-2.473990,-8.282403,8.872831],[7.244845,3.305982,-1.711067,-2.883060,-1.386080,-2.235459,1.098179,-6.314755,2.080127,1.322672,8.644104,8.974321,-6.368633],[-2.070636,4.758172,0.941783,8.220673,6.422870,1.491616,-9.225593,2.201751,-1.661215,7.238173,-1.315589,5.017167,7.955725],[-4.534517,-5.211841,-5.094082,6.774944,-6.956130,-9.577485,9.748345,2.453291,-9.460257,-7.740124,0.688587,-3.353528,-2.142090],[1.528854,-6.404636,-0.669094,-9.034045,-6.875377,9.213401,-0.893618,-7.069686,-0.957901,-9.684297,3.043231,1.499753,-6.917721],[-7.939985,6.558009,-7.191538,-1.407822,-9.384481,3.948110,0.369038,8.659981,0.419395,-8.374969,9.619434,-1.498168,-3.044320],[-9.209022,4.785130,-1.370073,0.344501,-8.352129,1.828715,3.680413,4.475508,-5.813396,-6.706687,-7.008617,8.318447,6.849210],[2.874017,-9.406493,3.034660,8.547467,7.663578,-3.797497,-8.991295,-0.162918,0.710051,5.447748,-7.802075,7.158545,1.282967],[1.042026,-9.665638,3.808865,-9.374629,-9.757980,-3.163854,-3.361123,1.642532,0.355562,-0.135993,7.601673,2.344110,-2.947879],[-0.219475,-1.019654,6.202327,-4.273545,-4.369442,1.976360,9.561817,1.262664,-6.792492,-0.817005,-9.349118,6.329568,5.171971],[9.666994,3.557815,3.199441,9.763765,1.724998,8.469692,9.967791,-3.464296,-2.832426,-6.686197,5.891803,7.626609,-8.560609],[0.860503,-0.301282,0.407788,5.888726,-7.992752,-8.274102,-0.258140,-6.768582,-6.506125,-0.894619,9.205500,-1.185451,-6.384043],[-5.924221,0.205514,4.758050,-3.606909,-9.016749,5.103242,-0.601799,-6.925591,-0.384986,-5.407467,-4.987535,-0.206657,5.005236]],[[1.869701,1.064496,-1.603664,7.450466,-0.340363,-4.181578,3.562112,-0.137922,6.091771,-6.914377,-1.949919,-0.886963,8.278799],[4.590548,8.895743,0.363943,-3.883132,-4.495996,-6.338998,7.566538,2.821338,5.483099,-6.118335,0.450538,-2.290808,9.915909],[-9.822690,-7.697080,-0.808573,6.756558,-3.210657,-3.674039,9.078263,5.833806,-9.438104,6.463611,7.112242,-0.410877,-9.857166],[0.842297,7.180705,5.536135,-4.550859,-2.465523,2.150130,2.214875,-7.600667,1.513865,-6.248527,-7.806150,8.017715,-4.484388],[-4.707584,-6.985964,8.963501,-6.587861,-4.676533,-6.713345,4.287481,5.047044,2.327206,-3.895969,-3.886760,0.042928,6.450923],[3.072762,0.743131,0.649403,6.810152,8.432424,1.774373,6.885302,7.787474,-7.619419,-8.403309,-2.285632,-8.997599,-5.517779],[-6.488387,-2.502265,3.363335,-2.870180,9.327979,-8.371530,2.436147,4.798510,7.106175,-5.679140,4.314477,1.656407,-0.131577],[3.675955,7.176166,1.321741,4.876470,5.049676,5.210463,-1.721409,6.013052,3.012475,-5.734428,9.235742,-3.637979,-1.139503],[-9.660610,1.878468,7.662355,-0.581480,-1.583857,-0.410819,7.034739,-3.401675,2.572134,1.919662,-8.425969,3.905538,-4.003181],[-5.977085,-0.248456,-1.455346,6.724800,3.174883,-8.813489,0.505341,3.831676,-5.408835,9.348103,-8.684105,4.622890,1.918373],[-2.062073,-0.889843,2.021275,8.517021,-2.487418,-2.338125,-3.801513,-3.056492,8.435115,1.380446,-2.320284,0.440369,2.926294],[-7.114049,-3.035555,-9.398481,0.020495,4.345054,4.452945,-9.415406,-4.488840,9.814008,4.492335,4.725640,2.289333,2.392067],[-8.737413,8.840320,-7.434194,9.631429,2.524503,-2.359745,-0.525920,1.827689,-9.859433,4.096031,9.825225,5.707641,8.166615],[5.785338,-7.758189,-6.150898,-3.009950,-3.784364,1.292570,8.769557,0.788350,7.093845,2.534484,3.699727,2.482743,-5.570035],[-9.888797,4.495726,-5.497046,-9.957608,6.069698,9.161296,2.679105,8.672579,5.613512,7.282560,-7.461133,2.425944,-4.279073]],[[3.858526,5.413988,-0.939531,-1.354034,2.473776,-3.303350,2.864409,-1.208965,2.962592,-9.297505,9.225838,7.918166,-9.121225],[9.090151,4.203128,-6.673469,3.551830,-3.591016,6.950008,5.852935,9.211673,8.811481,-9.161128,-0.398563,2.262081,-2.088892],[-9.182667,9.053238,0.116780,-8.309230,-3.036745,1.791383,8.461778,8.404959,-6.078219,9.751325,7.126569,-2.786882,2.228276],[4.326055,4.628986,0.242985,-0.800213,-0.941788,0.001402,-7.395463,-5.719955,-9.881804,-2.857177,-4.114067,-7.042025,-8.087819],[-8.102561,4.101930,1.527103,-6.076434,-2.409039,6.268449,3.238316,-8.281808,-2.460058,-0.590933,4.487380,-9.244924,9.547604],[-5.099309,5.579344,5.339057,-2.138358,9.721935,9.784843,-7.960788,2.292555,-7.885230,-4.002630,2.016409,-0.268940,4.670303],[-1.966087,7.722403,-1.873207,-4.151342,-8.518039,-6.583506,-1.323528,2.217496,7.916282,-6.467577,2.824936,0.703077,6.049384],[-0.293688,1.207821,1.485343,-5.978222,0.652255,2.837320,-3.878420,9.612814,-3.747902,-3.538706,3.055679,9.211574,-0.541013],[0.329664,-1.147415,-1.410037,-8.430973,-8.441756,-9.442846,-9.975758,-3.631454,8.762573,4.443720,7.818820,-4.198370,9.195961],[2.425446,8.871127,0.539452,-7.214138,-7.971612,9.914544,-2.042499,-5.664207,-4.769387,-6.849295,-1.132955,3.972686,-2.275610],[1.384643,-2.561551,-7.998239,-1.883284,8.533049,-2.078713,5.548137,-5.158700,9.527591,6.220886,6.903495,-8.100825,-3.423468],[9.259318,9.475323,-9.633663,3.894765,9.382313,-0.734418,0.995979,-5.206636,4.402302,-3.712057,-0.690643,-1.132140,-2.243798],[4.927697,9.029192,1.966279,0.117761,-6.237322,-2.356279,-2.046604,-5.681183,7.329153,-1.112834,7.601087,5.519686,2.770702],[-0.365867,8.484418,-4.047081,1.272974,-8.957240,-6.277935,2.310040,6.198568,-4.929320,-9.957665,0.893141,3.467997,2.822722],[6.613019,-3.040572,-1.545469,9.569939,3.582606,-3.471763,4.632207,-8.392258,-9.051734,0.456184,1.774757,3.880119,-1.241152]]], dtype = "float32")#candidate|4732|(4, 15, 13)|const|float32
var_4733 = relay.var("var_4733", dtype = "float32", shape = (4, 15, 13))#candidate|4733|(4, 15, 13)|var|float32
bop_4734 = relay.floor_divide(const_4732.astype('float32'), relay.reshape(var_4733.astype('float32'), relay.shape_of(const_4732))) # shape=(4, 15, 13)
bop_4738 = relay.not_equal(const_4732.astype('bool'), relay.reshape(bop_4734.astype('bool'), relay.shape_of(const_4732))) # shape=(4, 15, 13)
output = relay.Tuple([bop_4738,])
output2 = relay.Tuple([bop_4738,])
func_4741 = relay.Function([var_4733,], output)
mod['func_4741'] = func_4741
mod = relay.transform.InferType()(mod)
var_4742 = relay.var("var_4742", dtype = "float32", shape = (4, 15, 13))#candidate|4742|(4, 15, 13)|var|float32
output = func_4741(var_4742)
func_4743 = relay.Function([var_4742], output)
mutated_mod['func_4743'] = func_4743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2893_call = mod.get_global_var('func_2893')
func_2894_call = mutated_mod.get_global_var('func_2894')
call_4748 = relay.TupleGetItem(func_2893_call(), 2)
call_4749 = relay.TupleGetItem(func_2894_call(), 2)
uop_4771 = relay.erf(call_4748.astype('float32')) # shape=(10, 9, 3)
uop_4773 = relay.erf(call_4749.astype('float32')) # shape=(10, 9, 3)
output = uop_4771
output2 = uop_4773
func_4782 = relay.Function([], output)
mod['func_4782'] = func_4782
mod = relay.transform.InferType()(mod)
output = func_4782()
func_4783 = relay.Function([], output)
mutated_mod['func_4783'] = func_4783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4782_call = mod.get_global_var('func_4782')
func_4783_call = mutated_mod.get_global_var('func_4783')
call_4801 = func_4782_call()
call_4802 = func_4782_call()
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_4808 = relay.TupleGetItem(func_1316_call(), 1)
call_4809 = relay.TupleGetItem(func_1318_call(), 1)
uop_4812 = relay.log2(call_4801.astype('float64')) # shape=(10, 9, 3)
uop_4814 = relay.log2(call_4802.astype('float64')) # shape=(10, 9, 3)
output = relay.Tuple([call_4808,uop_4812,])
output2 = relay.Tuple([call_4809,uop_4814,])
func_4823 = relay.Function([], output)
mod['func_4823'] = func_4823
mod = relay.transform.InferType()(mod)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mutated_mod.get_global_var('func_4823')
call_4824 = func_4823_call()
output = call_4824
func_4825 = relay.Function([], output)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4845 = relay.var("var_4845", dtype = "uint8", shape = (2, 3, 1))#candidate|4845|(2, 3, 1)|var|uint8
var_4846 = relay.var("var_4846", dtype = "uint8", shape = (2, 3, 9))#candidate|4846|(2, 3, 9)|var|uint8
bop_4847 = relay.bitwise_xor(var_4845.astype('uint8'), var_4846.astype('uint8')) # shape=(2, 3, 9)
uop_4858 = relay.sin(bop_4847.astype('float64')) # shape=(2, 3, 9)
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_4866 = relay.TupleGetItem(func_2968_call(), 0)
call_4867 = relay.TupleGetItem(func_2969_call(), 0)
bop_4877 = relay.less_equal(uop_4858.astype('bool'), relay.reshape(var_4846.astype('bool'), relay.shape_of(uop_4858))) # shape=(2, 3, 9)
var_4882 = relay.var("var_4882", dtype = "uint8", shape = (2, 3, 9))#candidate|4882|(2, 3, 9)|var|uint8
bop_4883 = relay.equal(var_4846.astype('bool'), relay.reshape(var_4882.astype('bool'), relay.shape_of(var_4846))) # shape=(2, 3, 9)
output = relay.Tuple([call_4866,bop_4877,bop_4883,])
output2 = relay.Tuple([call_4867,bop_4877,bop_4883,])
func_4888 = relay.Function([var_4845,var_4846,var_4882,], output)
mod['func_4888'] = func_4888
mod = relay.transform.InferType()(mod)
mutated_mod['func_4888'] = func_4888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4888_call = mutated_mod.get_global_var('func_4888')
var_4890 = relay.var("var_4890", dtype = "uint8", shape = (2, 3, 1))#candidate|4890|(2, 3, 1)|var|uint8
var_4891 = relay.var("var_4891", dtype = "uint8", shape = (2, 3, 9))#candidate|4891|(2, 3, 9)|var|uint8
var_4892 = relay.var("var_4892", dtype = "uint8", shape = (2, 3, 9))#candidate|4892|(2, 3, 9)|var|uint8
call_4889 = func_4888_call(var_4890,var_4891,var_4892,)
output = call_4889
func_4893 = relay.Function([var_4890,var_4891,var_4892,], output)
mutated_mod['func_4893'] = func_4893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2893_call = mod.get_global_var('func_2893')
func_2894_call = mutated_mod.get_global_var('func_2894')
call_5051 = relay.TupleGetItem(func_2893_call(), 2)
call_5052 = relay.TupleGetItem(func_2894_call(), 2)
func_429_call = mod.get_global_var('func_429')
func_430_call = mutated_mod.get_global_var('func_430')
call_5067 = func_429_call()
call_5068 = func_429_call()
output = relay.Tuple([call_5051,call_5067,])
output2 = relay.Tuple([call_5052,call_5068,])
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
func_3027_call = mod.get_global_var('func_3027')
func_3029_call = mutated_mod.get_global_var('func_3029')
call_5095 = func_3027_call()
call_5096 = func_3027_call()
output = relay.Tuple([call_5095,])
output2 = relay.Tuple([call_5096,])
func_5109 = relay.Function([], output)
mod['func_5109'] = func_5109
mod = relay.transform.InferType()(mod)
output = func_5109()
func_5110 = relay.Function([], output)
mutated_mod['func_5110'] = func_5110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5181 = relay.var("var_5181", dtype = "float64", shape = (11, 6, 12))#candidate|5181|(11, 6, 12)|var|float64
var_5182 = relay.var("var_5182", dtype = "float64", shape = (11, 6, 12))#candidate|5182|(11, 6, 12)|var|float64
bop_5183 = relay.divide(var_5181.astype('float64'), relay.reshape(var_5182.astype('float64'), relay.shape_of(var_5181))) # shape=(11, 6, 12)
func_4782_call = mod.get_global_var('func_4782')
func_4783_call = mutated_mod.get_global_var('func_4783')
call_5188 = func_4782_call()
call_5189 = func_4782_call()
func_4741_call = mod.get_global_var('func_4741')
func_4743_call = mutated_mod.get_global_var('func_4743')
const_5195 = relay.const([0.060149,-1.379458,-7.327705,3.659899,-9.930768,-3.828804,-2.233168,4.141151,-8.689305,1.744195,-5.096051,-6.149217,1.677363,-8.003894,0.508317,-2.380163,-3.394603,7.742687,-8.907426,-2.614169,-1.955920,0.705154,-8.791390,7.898399,-7.230848,9.536887,0.350095,-0.778835,8.470188,2.830497,-6.662971,3.439197,-4.518129,6.576901,0.663661,1.318821,-8.586579,8.540372,9.514350,-5.313868,7.566963,-2.484943,4.003857,-0.017961,-7.656428,6.776525,4.228355,4.396634,0.422152,-9.551865,-8.851246,-7.263924,4.091154,-1.755748,-4.380065,-3.835565,-2.642727,-4.609052,7.956910,4.407993,2.962585,-4.414195,3.778694,-8.208521,-6.687775,-1.052653,2.443101,-9.438964,-8.267820,3.366321,6.711059,-1.739023,0.674318,1.024364,3.787070,-2.057642,2.488022,-0.149809,-4.038248,3.044068,9.235818,-6.756133,1.134639,9.448061,8.432605,-6.571527,-6.392612,-6.255725,-1.062449,-4.347005,-4.396572,-6.430751,1.867513,9.713512,0.665655,4.406327,-6.595641,5.215837,-9.299495,7.165594,-2.420643,-2.478589,-6.658069,-9.359299,-4.903057,2.672600,9.431998,-1.827453,-9.360807,-3.970985,-6.056487,-4.200467,4.288118,-8.459502,8.194846,6.014599,-3.427360,-0.072075,6.611916,8.097522,-6.583577,-8.866179,-4.218205,-7.962055,-9.518644,-8.531121,-9.176064,2.139409,9.599226,5.010130,4.306281,-3.970547,-5.745975,3.760059,0.721209,9.403804,2.867374,0.337624,-7.485195,-1.952129,-6.809733,-5.309682,8.514223,6.181694,4.400247,6.731045,6.915909,-6.804423,2.847259,2.049647,-8.809697,-7.646460,9.558872,9.685258,6.474903,-0.288780,0.018162,6.049101,9.657920,6.969117,8.421824,8.238262,-6.218562,9.477936,5.623621,-2.755279,5.766810,4.483182,-4.080423,9.950384,-8.500665,5.759832,-8.530891,3.279762,9.945969,-4.981205,9.649885,-2.122744,-9.595253,5.021460,-7.289922,5.136507,-4.220333,-2.009024,-9.803686,4.051360,-0.788856,-8.743679,1.555854,-2.628259,-0.537070,2.863731,-1.286135,5.515657,9.448362,0.918775,-2.636248,-9.517471,3.664359,5.852589,-6.701971,9.727612,2.501657,7.959839,0.022385,-8.046479,-7.094987,3.009223,6.627746,5.287769,-3.136015,-7.555981,-9.546353,8.190347,-2.012962,5.615816,7.468313,2.780230,-1.205989,0.462171,-2.775730,9.227196,-2.069122,8.941432,9.213416,-5.605556,2.931340,-1.109595,3.492992,-2.903990,-4.111454,-9.336240,-9.702496,-6.695296,-8.302825,-6.446352,6.345208,-4.790364,-7.734023,3.931572,-6.280391,4.031049,7.139674,8.764277,-0.161986,-7.144144,5.624120,-3.843101,-2.591335,-6.260555,6.845715,5.777445,-7.183204,-5.803309,6.276850,-9.247976,4.302485,-8.478661,9.642233,-2.628010,4.412485,-0.011730,4.009301,-2.861448,-2.197644,7.165537,7.466630,-0.601831,-7.117352,-8.632685,9.605930,5.984003,7.122314,6.479437,-1.769586,-1.637322,-6.472501,-1.484893,2.587721,3.344796,-0.467569,0.648119,5.183475,9.185721,-4.115111,9.406777,0.132339,4.484981,-6.328600,9.168923,-0.769623,-5.797764,7.981668,-0.140842,8.893172,-5.680800,-2.542465,8.798178,3.496509,5.416517,7.159830,9.743374,-5.180464,1.743346,6.781380,8.039011,-5.352765,-4.046155,-6.094186,-4.481269,-7.836938,7.108733,7.913367,-4.522696,-6.768150,-4.708323,3.840765,-0.422860,-1.511657,-4.360417,-7.220305,0.442480,-5.364312,-1.852315,0.517709,-1.178811,1.964121,-7.516115,8.252836,-0.998030,8.310333,9.734513,-5.399477,-8.938898,0.361330,5.612540,-4.706395,-2.626741,-8.073958,7.620176,7.478453,-2.515168,-1.288090,2.355966,7.899374,3.089397,7.292237,8.899410,-6.386697,-8.872982,3.172523,1.834240,5.592933,-7.353216,5.389349,9.932327,5.315237,8.782015,-4.637131,3.994794,-3.350153,-2.982869,3.733659,-3.455487,2.486236,6.198344,-9.698927,-8.665213,-3.081875,9.665183,2.942696,0.091973,-1.911381,-2.270199,6.157363,6.259272,-9.998560,7.286519,0.498994,1.328652,1.328190,8.544752,9.792167,5.813545,-6.138038,0.188146,3.466284,5.099123,-5.803901,-4.773458,7.785957,9.576359,-8.398171,-4.457473,-7.761669,-7.651403,-0.783604,4.524312,-7.589308,-6.523820,-3.707097,-9.505499,-9.406345,9.977081,2.201752,-9.422803,4.541715,-8.293240,4.231448,-2.199431,-5.367766,0.627156,-3.119064,-6.478729,1.270219,-2.522955,7.007677,1.631223,-9.751497,-9.101200,-2.968401,-4.665664,-2.612643,4.625059,0.202446,-2.267024,0.407902,1.651488,-1.365525,-1.570092,-2.667771,4.938411,0.952584,6.102430,-1.311776,3.301322,-8.560369,-8.916901,-0.289191,-2.075155,2.624002,3.924102,-8.491901,1.238669,-0.046092,-1.794295,-0.159726,-5.241694,-2.420660,7.133586,3.577796,-1.461057,-6.300315,3.774980,-1.664097,1.283342,-4.947304,-7.621035,9.385116,7.751111,6.423034,-1.525874,-9.922231,0.794725,-3.347524,2.516973,3.896461,7.252086,-7.609970,-3.749787,0.788349,3.376770,-4.454993,-1.584679,4.504489,-3.706382,-0.919130,-4.226353,8.810166,9.244484,-4.799601,-8.591701,-6.234591,4.173981,-1.649026,-2.147777,6.761356,5.662376,8.398206,2.557122,8.584537,-7.357784,-5.360061,-3.464018,-7.448799,0.165092,-0.365807,2.524372,-4.302536,-6.219830,-8.694194,-5.195328,-6.117530,-1.384016,6.510312,-9.546879,0.645099,-9.320385,5.780619,5.058556,4.049573,-8.655946,-7.650892,-3.864600,-1.822577,0.934151,1.761121,0.453013,2.628257,-2.492251,7.616001,-1.419857,8.893835,5.201361,6.297024,-6.258077,2.959985,4.787701,-4.959232,-2.044097,-6.624271,-0.589120,4.635704,5.302777,8.744581,-2.570072,-0.001684,6.887544,3.644310,-0.780810,1.248414,0.361611,5.611281,9.597473,9.042230,-0.717496,7.797953,8.936611,-6.746039,-3.871630,-6.380012,5.331824,7.840922,-8.395388,7.675177,1.034429,-2.744662,6.016893,6.128502,4.451152,0.844922,-8.841926,-1.568302,0.570486,-7.447730,-1.860735,-4.145565,7.804547,-8.307216,9.222254,-2.977947,2.397103,6.022850,-9.038679,8.971711,3.439499,-7.339808,0.677904,-3.479519,8.575397,-6.340833,7.888329,0.995660,-8.328782,8.701221,1.106726,1.738573,-4.669493,-2.426597,9.561416,-6.146673,-8.389089,6.010866,-5.287110,-9.345187,-8.433389,6.539756,-1.855506,5.064448,7.353560,-2.366239,-6.111837,7.688065,-0.915153,-7.937879,6.225704,3.433504,9.729736,9.931016,-5.678921,8.946418,5.465575,-5.251083,-7.177043,-9.668288,-3.630681,-0.097540,-5.759844,4.073685,6.820780,4.757542,2.738345,-6.387487,0.856162,-8.883159,-9.561489,-0.275157,-6.555460,1.950790,-3.020955,-1.021093,-6.742158,-2.186761,-2.287810,7.519228,5.083026,-7.300635,2.267985,7.660838,0.499298,-3.713205,3.028527,5.842110,-4.437900,-5.217539,-7.321174,1.753371,-9.578549,-9.948450,-9.421501,-2.785013,-0.650805,-9.987216,-9.413330,-7.282784,4.389017,8.989277,7.917684,-5.703082,6.778725,4.574143,-1.238484,-5.605507,-4.076100,8.154191,-3.116294,-6.733707,3.820840,8.640484,-5.044784,6.992485,-4.244226,-7.721354,7.195674,3.433940,-9.465581,-4.735197,-1.488792,3.639381,5.083454,1.989872,-6.548732,-6.464388,-7.079844,5.498868,7.649513,-8.427884,1.746970,-0.170070,7.025856,7.385341,-6.310574,-3.248830,-1.681316,6.885440,2.431321,-2.251333,-2.671353,3.637180,-6.266322,3.637346,9.360460,2.313489,-4.778863,9.377842,-5.306657,4.523239,-1.581318,3.307457,9.340500,0.338185,7.964755,4.103754,-9.666305,-5.058514,2.894541,1.010261,0.740521,-2.635771,-4.226954,3.240007,-3.070640,4.878271,7.253250,-6.086128,9.965137,7.263922,7.509718,-4.987255,2.507860,-1.579829,-1.071370,5.393938,-3.735166,0.292836,0.995164,8.447583,-7.324986,-4.915777,8.152158,-2.513882,-4.414024,4.393116,-3.519745,-7.155736,-5.882425,1.951075,-1.375351,-8.692116,-6.172096,2.419209,3.608030,0.307838,4.580646,8.462172,-5.085401,4.180477,3.674376,-7.547127,-3.735973,6.034430,2.457191,5.339012,0.493541,4.756548,9.058258,0.740138,5.320894,-9.533463,-2.282919,-9.554122,-2.803640,-5.773608,-7.711332,4.979173,7.187799,-9.706221,4.538161,-4.782183,3.915416], dtype = "float32")#candidate|5195|(780,)|const|float32
call_5194 = relay.TupleGetItem(func_4741_call(relay.reshape(const_5195.astype('float32'), [4, 15, 13])), 0)
call_5196 = relay.TupleGetItem(func_4743_call(relay.reshape(const_5195.astype('float32'), [4, 15, 13])), 0)
func_4727_call = mod.get_global_var('func_4727')
func_4729_call = mutated_mod.get_global_var('func_4729')
call_5198 = func_4727_call()
call_5199 = func_4727_call()
func_2400_call = mod.get_global_var('func_2400')
func_2402_call = mutated_mod.get_global_var('func_2402')
call_5209 = relay.TupleGetItem(func_2400_call(), 0)
call_5210 = relay.TupleGetItem(func_2402_call(), 0)
bop_5222 = relay.logical_or(call_5194.astype('bool'), relay.reshape(const_5195.astype('bool'), relay.shape_of(call_5194))) # shape=(4, 15, 13)
bop_5225 = relay.logical_or(call_5196.astype('bool'), relay.reshape(const_5195.astype('bool'), relay.shape_of(call_5196))) # shape=(4, 15, 13)
func_2030_call = mod.get_global_var('func_2030')
func_2033_call = mutated_mod.get_global_var('func_2033')
const_5234 = relay.const([5,-2,2,-2,10,-3,1,-7,8,-6,-10,8,9,9,-2,-2,-8,7,8,4,-9,-1,1,-5,-9,-3,-8,-8,6,8,-6,6,5,-4,5,5,7,6,3,6,4,2,-10,-9,-8,6,-1,5,-8,-1,7,8,-1,1,-8,7,-4,-4,-1,-1,-3,-2,1,-10,-8,-1,6,-8,-6,2,-6,3,-10,-6,-1,-10,4,-9,-9,4,-10,2,-6,5,-1,-3,-6,9,-5,-8,2,3,10,-10,10,6,-1,-6,-1,9,7,-1,10,2,-6,6,-10,5,10,9,-1,10,5,1,8,-10,-1,10,4,9,-4,-8,-3,-4,-10,10,10,-5,5,-3,-5,-8,5,-8,-1,8,1,8,1,-4,7,-2,6,-3,3,-6,10,-5,-1,5,9,7,-1,5,-7,5,-4,10,-6,3,-9,-10,-2,-6,-7,6,6,7,8,-9,2,8,1,-6,-3,8,7,-2,10,-3,-9,-4,-10,-2,4,3,7,2,3,7,-8,-7,3,-5,9,2,4,-3,-7,-5,8,9,-3,-3,10,2,5,4,-1,10,6,6,-8,-6,-5,7,3,7,8,10,-10,-7,-2,-2,1,-2,4,7,-8,8,-6,-5,3,-4,-3,-9,9,-7,-9,5,-3,-7,5,-8,8,4,-10,-4,-2,4,-5,8,10,-6,-6,-1,7,3,-1,-3,-8,-5,-10,3,-7,7,1,7,-1,-2,-5,-4,-8,-4,-2,8,-6,10,1,-7,-2,4,2,-5,-6,9,-10,4,4,9,-5,-7,1,8,-1,-2,-3,-6,-10,7,-10,7,-3,-9,1,4,8,-8,9,3,-4,2,-3,-10,9,-9,8,-10,9,10,9,7,-5,6,-2,5,6,-3,6,-10,-3,-6,4,-9,-5,-4,-3,2,7,-2,-7,-5,4,1,-1,7,-9,2,8,10,-2,-6,5,-3,-5,1,3,4,6,-9,6,1,-8,-1,-6,-8,5,-1,3,5,10,10,6,1,7,8,-6,1,2,10,2,4,3,2,-1,4,6,5,5,-3,7,-8,-2,1,-10,2,1,1,-3,-2,3,8,-7,1,-10,-6,8,2,-2,4,5,4,-1,-10,10,-1,-7,2,1,-7,8,9,-7,7,-5,-1,-4,4,10,2,-7,4,-1,7,-8,4,-8,-5,6,-6,1,-9,2,2,1,-3,6,-4,2,10,6,9,7,-10,-3,1,-4,9,-8,-8,-5,-9,8,10,5,-1,4,-8,3,-3,4,10,-8,6,2,-7,6,-9,-9,6,1,-6,7,-5,2,7,-3,8,6,7,7,-6,-10,-7,6,-3,-9,1,3,-8,-5,2,10,9,-3,7,-10,1,9,-9,1,3,2,-8,3,9,1,-6,-5,-8,-3,8,-9,5,9,5,7,10,6,-4,5,7,-9,8,9,-10,-2,-8,-9,9,9,6,3,-7,7,8,-7,10,7,9,6,6,10,-7,9,5,-1,7,-10,-5,-8,-8,5,10,-6,5,8,9,9,7,3,7,-4,10,-1,-8,5,1,-6,3,1,5,3,-7,2,-10,5,-9,-4,-2,3,1,10,1,4,-9,1,-4,9,-7,-7,-8,-8,3,7,6,-7,-9,2,2,-3,3,-8,8,-2,10,6,4,-4,-6,4,2,-1,-8,-10,-1,3,7,-10,-9,-4,2,7,-3,-6,-4,3,4,7,-8], dtype = "uint32")#candidate|5234|(640,)|const|uint32
call_5233 = relay.TupleGetItem(func_2030_call(relay.reshape(const_5234.astype('uint32'), [640,])), 2)
call_5235 = relay.TupleGetItem(func_2033_call(relay.reshape(const_5234.astype('uint32'), [640,])), 2)
uop_5236 = relay.acosh(call_5198.astype('float32')) # shape=(126,)
uop_5238 = relay.acosh(call_5199.astype('float32')) # shape=(126,)
bop_5249 = relay.not_equal(var_5182.astype('bool'), relay.reshape(var_5181.astype('bool'), relay.shape_of(var_5182))) # shape=(11, 6, 12)
output = relay.Tuple([bop_5183,call_5188,call_5209,bop_5222,call_5233,const_5234,uop_5236,bop_5249,])
output2 = relay.Tuple([bop_5183,call_5189,call_5210,bop_5225,call_5235,const_5234,uop_5238,bop_5249,])
func_5255 = relay.Function([var_5181,var_5182,], output)
mod['func_5255'] = func_5255
mod = relay.transform.InferType()(mod)
var_5256 = relay.var("var_5256", dtype = "float64", shape = (11, 6, 12))#candidate|5256|(11, 6, 12)|var|float64
var_5257 = relay.var("var_5257", dtype = "float64", shape = (11, 6, 12))#candidate|5257|(11, 6, 12)|var|float64
output = func_5255(var_5256,var_5257,)
func_5258 = relay.Function([var_5256,var_5257,], output)
mutated_mod['func_5258'] = func_5258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mod.get_global_var('func_4823')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_5297 = relay.TupleGetItem(func_4823_call(), 1)
call_5298 = relay.TupleGetItem(func_4825_call(), 1)
func_1614_call = mod.get_global_var('func_1614')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_5305 = relay.TupleGetItem(func_1614_call(), 1)
call_5306 = relay.TupleGetItem(func_1615_call(), 1)
func_471_call = mod.get_global_var('func_471')
func_474_call = mutated_mod.get_global_var('func_474')
var_5309 = relay.var("var_5309", dtype = "uint32", shape = (42,))#candidate|5309|(42,)|var|uint32
const_5310 = relay.const([7,-9,-3,1,-7,3,-7,-4,-1,4,-4,-5,-7,-4,-7,4,-5,2,-3,-10,-7,2,7,2,-9,-5,3,1,-6,-8,-5,4,5,-10,10,-3,-4,-8,-1,6,1,4,-3,4,9,10,-6,6,10,-4,-5,-7,1,7,-8,-3,-6,4,1,9,-2,6,3,1,-7,6,-1,-2,-10,8,3,8,-8,1,8,1,-8,8,-10,-5,-6,-10,5,1,2,3,1,-7,2,2,7,-2,2,-4,-10,1,1,-5,5,2,-5,1,4,9,-5,10,4,-6,-3,-1,3,-1,3,-3,-1,-4,-9,4,-4,-1,-2,10,2,-4,-8,2], dtype = "uint32")#candidate|5310|(126,)|const|uint32
call_5308 = relay.TupleGetItem(func_471_call(relay.reshape(var_5309.astype('uint32'), [1, 3, 14]), relay.reshape(const_5310.astype('uint32'), [3, 3, 14]), ), 0)
call_5311 = relay.TupleGetItem(func_474_call(relay.reshape(var_5309.astype('uint32'), [1, 3, 14]), relay.reshape(const_5310.astype('uint32'), [3, 3, 14]), ), 0)
bop_5317 = relay.equal(const_5310.astype('bool'), relay.reshape(call_5308.astype('bool'), relay.shape_of(const_5310))) # shape=(126,)
bop_5320 = relay.equal(const_5310.astype('bool'), relay.reshape(call_5311.astype('bool'), relay.shape_of(const_5310))) # shape=(126,)
func_4183_call = mod.get_global_var('func_4183')
func_4184_call = mutated_mod.get_global_var('func_4184')
call_5326 = func_4183_call()
call_5327 = func_4183_call()
func_3440_call = mod.get_global_var('func_3440')
func_3443_call = mutated_mod.get_global_var('func_3443')
const_5358 = relay.const([-8.140856,-9.704181,8.747390,-7.491855,-9.856537,-5.898852,8.188078,3.749174,5.032019,1.270154,6.700042,-5.499071,-0.628389,-2.625874,-1.868936,-0.117242,2.415092,-8.498334,-9.862765,-5.060514,5.785855,6.902667,4.653871,9.017001,1.147165,-4.539886,7.223872,0.384673,-3.199620,3.307602,9.471831,5.246621,-8.882840,6.247404,9.659843,9.636497,8.463639,1.016049,8.947794,4.245858,-1.758028,8.250900,-0.427821,0.416161,6.939971,-9.308648,-8.945439,5.935543,8.289712,-4.554121,2.510943,4.245454,-8.144877,9.331386,5.828966,-4.093219,-8.338273,2.844149,-1.726532,-2.937939,6.760609,-7.005081,-0.478884,-4.913276,9.008495,-0.953733,-7.270349,8.263346,3.578875,-6.956357,2.739233,-5.464252,4.619102,-6.010517,-9.996158,1.695294,9.456772,5.049818,7.759369,5.394470,-8.698798,4.823261,-7.019726,6.380409,7.867361,-7.479013,7.381129,8.266966,3.693058,-1.924447,-3.687421,3.246864,-4.767990,3.388329,5.823369,-4.380479,0.588480,-3.862212,-5.192825,1.511243,-2.093663,-4.671970,-5.509429,-7.319730,7.926537,9.639318,-8.889281,-3.788906,6.021500,-7.747038,-1.992333,7.588745,2.151720,5.198982,6.875669,1.723006,2.808789,0.205083,2.467758,1.987770,3.558747,-3.108880,6.730210,-0.467837,2.821395,4.933462,6.110802,2.095432,7.409899,-0.046320,9.460781,-9.435857,7.100963,-1.656073,4.341251,3.938677,-5.259898,-7.982605,-5.210713,-5.572190,9.220388,-5.651001,-9.686770,8.037893,-5.491864,3.043316,-4.789057,-9.971205,6.524542,-8.045742,-9.505365,7.696813,-7.344433,8.060400,-5.374905,-9.546963,8.854977,-2.421471,-3.126630,7.913365,8.753660,-9.761445,-0.847361,8.866513,2.968594,-6.217011,-8.747016,-0.368653,5.462448,5.105199,9.735382,-6.960233,-3.362811,1.711374,-0.896564,-5.337199,1.986981,2.467035,2.541732,6.371000,9.705546,8.910277,-9.878573,-4.246273,1.486018,1.724691,1.795154,5.105546,6.058222,-0.049502,-4.601624,1.489257,7.412584,8.037299,-3.322223,9.521104,2.935258,2.472565,-8.553825,7.620931,4.933869,-1.629215,-5.249893,9.825685,-3.138191,-4.526585,-5.581749,-7.232012,-0.636395,-8.461472,1.967975,-7.087457,-7.157159,-3.469322,7.550351,-1.450275,-9.296800,8.312427,6.156202,-8.346538,-5.180024,-4.236225,2.932946,-2.704342,-7.480457,-8.622149,-1.932752,-3.172583,-5.964435,2.338754,4.428362,-9.094857,9.005016,-3.863396,-0.131285,-7.975378,4.761921,9.949968,-1.236605,1.480345,2.856788,-4.791954,-0.442662,-2.914388,9.528657,7.321957,-6.791150,-7.393837,5.329386,-7.918236,-4.211504,4.570202,4.494742,-9.539060,-8.147097,-2.395235,3.638782,-8.088615,-6.928169,-5.841661,-0.960246,-1.372615,3.037785,-1.765214,7.778621,0.260847,-3.948820,-3.968861,9.008209,4.674508,-4.619027,1.139039,-8.046138,0.534681,7.280063,-2.824559,5.740703,-7.698708,8.775532,-6.428574,1.825865,-5.574498,-5.999171,4.974739,6.833983,3.534471,-7.882846,3.882790,-9.920129,9.200512,-7.635131,-0.303510,-6.121998,5.914176,8.422793,0.136670,6.631841,-5.101375,-8.755390,1.585497,-3.555627,7.716358,-4.388986,6.867456,4.161773,-3.424737,-4.001348,-9.464321,2.044755,9.009054,9.243310,9.513578,-6.070820,-3.042193,3.463693,9.897173,-1.039888,-3.828158,5.690712,-2.909699,9.235358,6.701886,7.853651,-5.864874,0.116694,4.117927,-1.991749,6.923767,8.671515,2.719722,0.073229,-4.363132,7.080464,-9.682095,7.990225,-4.270031,9.621618,-0.758626,0.860584,7.224530,-9.319399,4.308768,8.895634,-9.064525,-5.499126,9.679320,-3.083608,9.193635,6.717750,-2.185489,-0.270518,0.515447,-5.991663,-4.419808,-5.831713,-6.010562,9.067427,-8.621369,-0.791121,2.105184,-0.391144,5.809838,-0.168913,7.050943,-7.038858,-0.101506,-5.933880,7.041548,-7.653992,-0.581247,7.592736,0.531618,-8.278458,-4.818956,-7.903301,0.409280,-7.557218,3.974425,2.654383,-3.369491,6.758288,3.774707,-3.391411,-3.932974,-7.431085,-5.866567,-1.742641,-3.490614,3.976320,8.061455,-5.907133,-8.435853,7.809939,-2.573425,-5.076637,2.981281,6.833298,0.694516,5.770094,-2.517482,-6.506828,2.152902,0.079747,5.267687,-1.356633,-6.063509,3.894736,-9.444158,6.575346,-6.167487,2.569518,2.313646,-3.506126,5.426231,-1.786055,4.419376,-4.523362,5.116450,3.681216,-4.946111,-1.876541,-9.720380,1.735925,-4.224323,4.664574,1.212429,-5.252240,-8.254981,8.566484,-1.437728,5.342145,5.836589,9.968157,0.685188,0.939124,-6.974934,7.425154,-8.073364,5.181624,5.781311,9.750664,-5.241180,1.477153,-3.616247,-2.981951,-1.768693,-1.488044,1.286608,7.180432,-8.474835,-2.980873,-5.531551,-4.593837,-8.676036,7.387484,-7.100537,-4.752782,1.946558,0.214838,5.304589,-5.566908,-4.630615,4.302927,-9.410900,-7.890457,0.656202,-2.092197,-7.427743,-4.642080,-2.148832,-6.365054,-7.177264,1.268468,-7.925010,1.057450,-6.826568,-7.093798,7.925877,-8.349971,-3.932204], dtype = "float64")#candidate|5358|(480,)|const|float64
call_5357 = relay.TupleGetItem(func_3440_call(relay.reshape(const_5358.astype('float64'), [2, 15, 16])), 2)
call_5359 = relay.TupleGetItem(func_3443_call(relay.reshape(const_5358.astype('float64'), [2, 15, 16])), 2)
func_3721_call = mod.get_global_var('func_3721')
func_3724_call = mutated_mod.get_global_var('func_3724')
var_5366 = relay.var("var_5366", dtype = "uint32", shape = (1512,))#candidate|5366|(1512,)|var|uint32
call_5365 = relay.TupleGetItem(func_3721_call(relay.reshape(bop_5317.astype('uint32'), [63, 2]), relay.reshape(var_5366.astype('uint32'), [1512,]), ), 1)
call_5367 = relay.TupleGetItem(func_3724_call(relay.reshape(bop_5317.astype('uint32'), [63, 2]), relay.reshape(var_5366.astype('uint32'), [1512,]), ), 1)
func_626_call = mod.get_global_var('func_626')
func_627_call = mutated_mod.get_global_var('func_627')
call_5370 = func_626_call()
call_5371 = func_626_call()
uop_5377 = relay.atan(var_5309.astype('float64')) # shape=(42,)
uop_5389 = relay.rsqrt(uop_5377.astype('float64')) # shape=(42,)
output = relay.Tuple([call_5297,call_5305,bop_5317,call_5326,call_5357,const_5358,call_5365,var_5366,call_5370,uop_5389,])
output2 = relay.Tuple([call_5298,call_5306,bop_5320,call_5327,call_5359,const_5358,call_5367,var_5366,call_5371,uop_5389,])
func_5391 = relay.Function([var_5309,var_5366,], output)
mod['func_5391'] = func_5391
mod = relay.transform.InferType()(mod)
var_5392 = relay.var("var_5392", dtype = "uint32", shape = (42,))#candidate|5392|(42,)|var|uint32
var_5393 = relay.var("var_5393", dtype = "uint32", shape = (1512,))#candidate|5393|(1512,)|var|uint32
output = func_5391(var_5392,var_5393,)
func_5394 = relay.Function([var_5392,var_5393,], output)
mutated_mod['func_5394'] = func_5394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_5415 = relay.TupleGetItem(func_703_call(), 0)
call_5416 = relay.TupleGetItem(func_705_call(), 0)
func_3937_call = mod.get_global_var('func_3937')
func_3938_call = mutated_mod.get_global_var('func_3938')
call_5422 = func_3937_call()
call_5423 = func_3937_call()
output = relay.Tuple([call_5415,call_5422,])
output2 = relay.Tuple([call_5416,call_5423,])
func_5433 = relay.Function([], output)
mod['func_5433'] = func_5433
mod = relay.transform.InferType()(mod)
output = func_5433()
func_5434 = relay.Function([], output)
mutated_mod['func_5434'] = func_5434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_5475 = func_553_call()
call_5476 = func_553_call()
output = relay.Tuple([call_5475,])
output2 = relay.Tuple([call_5476,])
func_5484 = relay.Function([], output)
mod['func_5484'] = func_5484
mod = relay.transform.InferType()(mod)
mutated_mod['func_5484'] = func_5484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5484_call = mutated_mod.get_global_var('func_5484')
call_5485 = func_5484_call()
output = call_5485
func_5486 = relay.Function([], output)
mutated_mod['func_5486'] = func_5486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4689_call = mod.get_global_var('func_4689')
func_4690_call = mutated_mod.get_global_var('func_4690')
call_5495 = relay.TupleGetItem(func_4689_call(), 0)
call_5496 = relay.TupleGetItem(func_4690_call(), 0)
output = call_5495
output2 = call_5496
func_5501 = relay.Function([], output)
mod['func_5501'] = func_5501
mod = relay.transform.InferType()(mod)
output = func_5501()
func_5502 = relay.Function([], output)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5501_call = mod.get_global_var('func_5501')
func_5502_call = mutated_mod.get_global_var('func_5502')
call_5539 = func_5501_call()
call_5540 = func_5501_call()
output = relay.Tuple([call_5539,])
output2 = relay.Tuple([call_5540,])
func_5557 = relay.Function([], output)
mod['func_5557'] = func_5557
mod = relay.transform.InferType()(mod)
output = func_5557()
func_5558 = relay.Function([], output)
mutated_mod['func_5558'] = func_5558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_5640 = relay.TupleGetItem(func_5109_call(), 0)
call_5641 = relay.TupleGetItem(func_5110_call(), 0)
var_5660 = relay.var("var_5660", dtype = "float64", shape = (4, 15, 4))#candidate|5660|(4, 15, 4)|var|float64
bop_5661 = relay.greater_equal(call_5640.astype('bool'), relay.reshape(var_5660.astype('bool'), relay.shape_of(call_5640))) # shape=(4, 15, 4)
bop_5664 = relay.greater_equal(call_5641.astype('bool'), relay.reshape(var_5660.astype('bool'), relay.shape_of(call_5641))) # shape=(4, 15, 4)
func_2260_call = mod.get_global_var('func_2260')
func_2264_call = mutated_mod.get_global_var('func_2264')
var_5672 = relay.var("var_5672", dtype = "uint32", shape = (126,))#candidate|5672|(126,)|var|uint32
var_5673 = relay.var("var_5673", dtype = "uint32", shape = (3, 504))#candidate|5673|(3, 504)|var|uint32
call_5671 = relay.TupleGetItem(func_2260_call(relay.reshape(var_5672.astype('uint32'), [126, 1]), relay.reshape(var_5673.astype('uint32'), [126, 12]), ), 1)
call_5674 = relay.TupleGetItem(func_2264_call(relay.reshape(var_5672.astype('uint32'), [126, 1]), relay.reshape(var_5673.astype('uint32'), [126, 12]), ), 1)
bop_5677 = relay.right_shift(call_5640.astype('int64'), relay.reshape(var_5660.astype('int64'), relay.shape_of(call_5640))) # shape=(4, 15, 4)
bop_5680 = relay.right_shift(call_5641.astype('int64'), relay.reshape(var_5660.astype('int64'), relay.shape_of(call_5641))) # shape=(4, 15, 4)
func_1940_call = mod.get_global_var('func_1940')
func_1941_call = mutated_mod.get_global_var('func_1941')
call_5687 = relay.TupleGetItem(func_1940_call(), 0)
call_5688 = relay.TupleGetItem(func_1941_call(), 0)
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_5692 = relay.TupleGetItem(func_968_call(), 0)
call_5693 = relay.TupleGetItem(func_970_call(), 0)
output = relay.Tuple([bop_5661,call_5671,var_5672,var_5673,bop_5677,call_5687,call_5692,])
output2 = relay.Tuple([bop_5664,call_5674,var_5672,var_5673,bop_5680,call_5688,call_5693,])
func_5696 = relay.Function([var_5660,var_5672,var_5673,], output)
mod['func_5696'] = func_5696
mod = relay.transform.InferType()(mod)
mutated_mod['func_5696'] = func_5696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5696_call = mutated_mod.get_global_var('func_5696')
var_5698 = relay.var("var_5698", dtype = "float64", shape = (4, 15, 4))#candidate|5698|(4, 15, 4)|var|float64
var_5699 = relay.var("var_5699", dtype = "uint32", shape = (126,))#candidate|5699|(126,)|var|uint32
var_5700 = relay.var("var_5700", dtype = "uint32", shape = (3, 504))#candidate|5700|(3, 504)|var|uint32
call_5697 = func_5696_call(var_5698,var_5699,var_5700,)
output = call_5697
func_5701 = relay.Function([var_5698,var_5699,var_5700,], output)
mutated_mod['func_5701'] = func_5701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_5725 = func_373_call()
call_5726 = func_373_call()
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_5727 = func_4162_call()
call_5728 = func_4162_call()
func_2649_call = mod.get_global_var('func_2649')
func_2652_call = mutated_mod.get_global_var('func_2652')
call_5752 = relay.TupleGetItem(func_2649_call(relay.reshape(call_5727.astype('float64'), [30, 9])), 2)
call_5753 = relay.TupleGetItem(func_2652_call(relay.reshape(call_5727.astype('float64'), [30, 9])), 2)
output = relay.Tuple([call_5725,call_5727,call_5752,])
output2 = relay.Tuple([call_5726,call_5728,call_5753,])
func_5755 = relay.Function([], output)
mod['func_5755'] = func_5755
mod = relay.transform.InferType()(mod)
output = func_5755()
func_5756 = relay.Function([], output)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5433_call = mod.get_global_var('func_5433')
func_5434_call = mutated_mod.get_global_var('func_5434')
call_5800 = relay.TupleGetItem(func_5433_call(), 0)
call_5801 = relay.TupleGetItem(func_5434_call(), 0)
func_3178_call = mod.get_global_var('func_3178')
func_3181_call = mutated_mod.get_global_var('func_3181')
const_5810 = relay.const([-6,1,-2,8,4,1,5,3,-10,-3,4,3,9,-9,10,6,-4,2,6,5,2,-3,3,6,6,8,-5,7,8,-10,-1,-8,5,-4,-4,8,-7,4,-7,-3,-10,-5,3,8,6,-2,6,4,2,10,-7,1,-1,5,-5,-3,9,-7,-9,-4,5,-2,7,-10,-5,2,-3,9,-10,-4,-1,8,-4,-2,2,-8,3,-7,9,7,10,-8,-4,8,1,9,-8,4,5,-7,-2,-5,-4,-5,-10,6,4,6,3,4,-6,6,1,10,-5,-5,1,-4,-2,9,-3,-3,-1,7,-1,-7,-5,4,4,3,10,-10,8,5,5,2], dtype = "uint32")#candidate|5810|(126,)|const|uint32
call_5809 = relay.TupleGetItem(func_3178_call(relay.reshape(const_5810.astype('uint32'), [126,])), 3)
call_5811 = relay.TupleGetItem(func_3181_call(relay.reshape(const_5810.astype('uint32'), [126,])), 3)
output = relay.Tuple([call_5800,call_5809,const_5810,])
output2 = relay.Tuple([call_5801,call_5811,const_5810,])
func_5812 = relay.Function([], output)
mod['func_5812'] = func_5812
mod = relay.transform.InferType()(mod)
output = func_5812()
func_5813 = relay.Function([], output)
mutated_mod['func_5813'] = func_5813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5876 = relay.var("var_5876", dtype = "float64", shape = (2, 12, 3))#candidate|5876|(2, 12, 3)|var|float64
var_5877 = relay.var("var_5877", dtype = "float64", shape = (2, 12, 3))#candidate|5877|(2, 12, 3)|var|float64
bop_5878 = relay.divide(var_5876.astype('float64'), relay.reshape(var_5877.astype('float64'), relay.shape_of(var_5876))) # shape=(2, 12, 3)
uop_5881 = relay.sin(var_5877.astype('float32')) # shape=(2, 12, 3)
output = relay.Tuple([bop_5878,uop_5881,])
output2 = relay.Tuple([bop_5878,uop_5881,])
func_5886 = relay.Function([var_5876,var_5877,], output)
mod['func_5886'] = func_5886
mod = relay.transform.InferType()(mod)
mutated_mod['func_5886'] = func_5886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5886_call = mutated_mod.get_global_var('func_5886')
var_5888 = relay.var("var_5888", dtype = "float64", shape = (2, 12, 3))#candidate|5888|(2, 12, 3)|var|float64
var_5889 = relay.var("var_5889", dtype = "float64", shape = (2, 12, 3))#candidate|5889|(2, 12, 3)|var|float64
call_5887 = func_5886_call(var_5888,var_5889,)
output = call_5887
func_5890 = relay.Function([var_5888,var_5889,], output)
mutated_mod['func_5890'] = func_5890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2591_call = mutated_mod.get_global_var('func_2591')
call_5905 = relay.TupleGetItem(func_2589_call(), 3)
call_5906 = relay.TupleGetItem(func_2591_call(), 3)
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_5910 = func_553_call()
call_5911 = func_553_call()
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_5912 = relay.TupleGetItem(func_2968_call(), 0)
call_5913 = relay.TupleGetItem(func_2969_call(), 0)
output = relay.Tuple([call_5905,call_5910,call_5912,])
output2 = relay.Tuple([call_5906,call_5911,call_5913,])
func_5918 = relay.Function([], output)
mod['func_5918'] = func_5918
mod = relay.transform.InferType()(mod)
output = func_5918()
func_5919 = relay.Function([], output)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3741_call = mod.get_global_var('func_3741')
func_3743_call = mutated_mod.get_global_var('func_3743')
call_5961 = relay.TupleGetItem(func_3741_call(), 0)
call_5962 = relay.TupleGetItem(func_3743_call(), 0)
func_3562_call = mod.get_global_var('func_3562')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_5970 = relay.TupleGetItem(func_3562_call(), 0)
call_5971 = relay.TupleGetItem(func_3564_call(), 0)
func_2649_call = mod.get_global_var('func_2649')
func_2652_call = mutated_mod.get_global_var('func_2652')
call_5985 = relay.TupleGetItem(func_2649_call(relay.reshape(call_5970.astype('float64'), [30, 9])), 0)
call_5986 = relay.TupleGetItem(func_2652_call(relay.reshape(call_5970.astype('float64'), [30, 9])), 0)
func_405_call = mod.get_global_var('func_405')
func_409_call = mutated_mod.get_global_var('func_409')
const_5998 = relay.const([[5],[10],[4],[-1],[-9],[9],[-1],[-7],[9],[-5],[-4],[6],[4],[-10],[10],[-9],[5],[-8],[-1],[-7],[-2],[-6],[-3],[-10],[-4],[-3],[-3],[-4],[5],[-10],[-6],[-9],[-8],[10],[-6],[2],[5],[-10],[4],[5],[6],[-6],[-6],[-8],[6],[5],[6],[-3],[-1],[-6],[1],[-2],[7],[-9],[2],[8],[-9],[-9],[-7],[-6],[-6],[7],[5],[8],[4],[-2],[1],[5],[5],[-10],[-7],[7],[5],[3],[-6],[4],[-1],[5],[2],[3],[-7],[-5],[8],[8],[-6],[-10],[-7],[1],[4],[3],[-4],[-3],[-10],[1],[2],[-2],[-9],[-7],[6],[8],[-4],[-5],[7],[4],[-9],[-3],[-3],[-7],[3],[-7],[-2],[-3],[-5],[-7],[8],[3],[6],[-4],[5],[6],[4],[-6],[-6],[-4],[-1],[-5],[9],[5],[10],[4],[-7],[-1],[-8],[-6],[4],[6],[9],[-7],[-7],[5],[1],[2],[-8],[3],[-6],[4],[-6],[6],[10],[7],[-2],[-4],[-7],[8],[-3],[1],[-3],[-3],[9],[-8],[2],[10],[-7],[-2],[-8],[2],[1],[3],[-8],[-1],[5],[4],[-4],[-10],[-10],[-10],[10],[-10],[4],[-5],[2],[2],[-5],[1],[-7],[-4],[-6],[-2],[-5],[5],[-9],[-10],[5],[-6],[-4],[3],[10],[9],[-10],[3],[-5],[-10],[7],[-3],[-4],[-8],[5],[4],[7],[-1],[2],[-7],[9],[10],[-6],[-7],[-1],[-4],[-2],[-9],[-9],[-9],[-4],[-6],[-2],[-4],[-1],[9],[-6],[-9],[3],[7],[-6],[-2],[-10],[-5],[9],[-3],[9],[-6]], dtype = "int8")#candidate|5998|(240, 1)|const|int8
call_5997 = relay.TupleGetItem(func_405_call(relay.reshape(const_5998.astype('int8'), [4, 15, 4]), relay.reshape(const_5998.astype('int8'), [4, 15, 4]), ), 0)
call_5999 = relay.TupleGetItem(func_409_call(relay.reshape(const_5998.astype('int8'), [4, 15, 4]), relay.reshape(const_5998.astype('int8'), [4, 15, 4]), ), 0)
output = relay.Tuple([call_5961,call_5970,call_5985,call_5997,const_5998,])
output2 = relay.Tuple([call_5962,call_5971,call_5986,call_5999,const_5998,])
func_6016 = relay.Function([], output)
mod['func_6016'] = func_6016
mod = relay.transform.InferType()(mod)
mutated_mod['func_6016'] = func_6016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6016_call = mutated_mod.get_global_var('func_6016')
call_6017 = func_6016_call()
output = call_6017
func_6018 = relay.Function([], output)
mutated_mod['func_6018'] = func_6018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4130_call = mod.get_global_var('func_4130')
func_4132_call = mutated_mod.get_global_var('func_4132')
call_6027 = relay.TupleGetItem(func_4130_call(), 0)
call_6028 = relay.TupleGetItem(func_4132_call(), 0)
output = relay.Tuple([call_6027,])
output2 = relay.Tuple([call_6028,])
func_6044 = relay.Function([], output)
mod['func_6044'] = func_6044
mod = relay.transform.InferType()(mod)
mutated_mod['func_6044'] = func_6044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6044_call = mutated_mod.get_global_var('func_6044')
call_6045 = func_6044_call()
output = call_6045
func_6046 = relay.Function([], output)
mutated_mod['func_6046'] = func_6046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1207_call = mod.get_global_var('func_1207')
func_1208_call = mutated_mod.get_global_var('func_1208')
call_6062 = func_1207_call()
call_6063 = func_1207_call()
func_5433_call = mod.get_global_var('func_5433')
func_5434_call = mutated_mod.get_global_var('func_5434')
call_6067 = relay.TupleGetItem(func_5433_call(), 0)
call_6068 = relay.TupleGetItem(func_5434_call(), 0)
output = relay.Tuple([call_6062,call_6067,])
output2 = relay.Tuple([call_6063,call_6068,])
func_6080 = relay.Function([], output)
mod['func_6080'] = func_6080
mod = relay.transform.InferType()(mod)
output = func_6080()
func_6081 = relay.Function([], output)
mutated_mod['func_6081'] = func_6081
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6095 = relay.const(3, dtype = "uint32")#candidate|6095|()|const|uint32
const_6096 = relay.const([[[-8,8,-10,-1,5,-7,5,2,10,-9]],[[6,-10,8,5,-3,-6,4,2,8,-8]],[[-3,10,5,-8,-9,-8,2,3,1,6]],[[6,7,-7,-3,4,7,-8,-5,-8,-10]],[[3,1,5,-7,-3,4,-6,-9,-10,7]],[[-4,1,-1,7,-3,-6,8,-2,-1,-3]],[[4,6,-8,1,7,-2,-2,5,9,-3]],[[-2,9,-6,4,1,-4,3,-5,2,9]],[[-5,2,-1,-3,10,5,4,-1,4,-8]],[[3,2,-1,-8,-6,-4,-7,-10,-5,1]],[[8,-9,-9,-1,-6,-9,-10,-6,1,-3]],[[1,10,6,-8,-3,-4,6,-3,4,9]],[[-2,2,3,-2,1,3,-5,-10,5,9]],[[9,-10,9,-10,-7,4,9,-3,3,7]]], dtype = "uint32")#candidate|6096|(14, 1, 10)|const|uint32
bop_6097 = relay.multiply(const_6095.astype('uint32'), const_6096.astype('uint32')) # shape=(14, 1, 10)
output = relay.Tuple([bop_6097,])
output2 = relay.Tuple([bop_6097,])
func_6101 = relay.Function([], output)
mod['func_6101'] = func_6101
mod = relay.transform.InferType()(mod)
mutated_mod['func_6101'] = func_6101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6101_call = mutated_mod.get_global_var('func_6101')
call_6102 = func_6101_call()
output = call_6102
func_6103 = relay.Function([], output)
mutated_mod['func_6103'] = func_6103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3937_call = mod.get_global_var('func_3937')
func_3938_call = mutated_mod.get_global_var('func_3938')
call_6168 = func_3937_call()
call_6169 = func_3937_call()
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_6193 = relay.TupleGetItem(func_703_call(), 0)
call_6194 = relay.TupleGetItem(func_705_call(), 0)
output = relay.Tuple([call_6168,call_6193,])
output2 = relay.Tuple([call_6169,call_6194,])
func_6207 = relay.Function([], output)
mod['func_6207'] = func_6207
mod = relay.transform.InferType()(mod)
output = func_6207()
func_6208 = relay.Function([], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mod.get_global_var('func_882')
func_883_call = mutated_mod.get_global_var('func_883')
call_6222 = func_882_call()
call_6223 = func_882_call()
func_373_call = mod.get_global_var('func_373')
func_374_call = mutated_mod.get_global_var('func_374')
call_6234 = func_373_call()
call_6235 = func_373_call()
output = relay.Tuple([call_6222,call_6234,])
output2 = relay.Tuple([call_6223,call_6235,])
func_6249 = relay.Function([], output)
mod['func_6249'] = func_6249
mod = relay.transform.InferType()(mod)
output = func_6249()
func_6250 = relay.Function([], output)
mutated_mod['func_6250'] = func_6250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2591_call = mutated_mod.get_global_var('func_2591')
call_6266 = relay.TupleGetItem(func_2589_call(), 1)
call_6267 = relay.TupleGetItem(func_2591_call(), 1)
func_2376_call = mod.get_global_var('func_2376')
func_2378_call = mutated_mod.get_global_var('func_2378')
const_6272 = relay.const([[-6.010027,-6.399916,-4.874018,-7.326009,6.551692,-7.109828,-8.742113,7.739562,8.543980,-8.671406,0.816587,2.322647,5.460264,4.474088,-0.318234,-3.072386,5.290717,-9.395156,-3.733773,0.789811,-3.342453,9.423198,-7.441285,4.189991,2.652651,0.088392,7.175408,6.968660,9.563032,1.445003,7.479015,5.680712,-0.850306,2.874144,-1.000107,-1.178228,-2.185061,3.956651,-8.006589,-6.392868,-2.962571,-0.964314,-1.017565,-4.555204,5.953539,3.151621,-5.737930,3.835169,-2.853139,9.227085,5.732956,2.807981,2.412876,-3.025327,-1.836314,1.724576,8.574308,-7.711830,6.039943,0.898277,-4.176373,-9.786495,6.617085,0.921163,-6.051057,-1.439512,-7.379664,7.428017,-8.812209,-6.172918,-0.705979,-6.103876,4.948947,2.614033,2.529617,7.396423,6.651597,-2.262970,5.063050,2.544467,-9.396521,-7.682810,4.842870,-1.581991,3.089514,-2.740377,5.699474,1.853375,-2.986545,7.029953,-2.510728,1.345298,-8.931236,-2.688557,-3.800450,7.936234,-2.190983,7.574878,9.433465,7.372427,-1.212230,-3.590630,-0.082499,0.568152,-2.490080,6.576446,5.510546,3.616992,-3.012496,-4.969686,9.407048,-7.947726,0.044720,2.209106,2.230695,8.350999,7.975594,0.705226,-0.970396,-0.805691,-1.398999,1.574963,-3.217152,9.920999,-8.652222,6.461430,-8.488327,8.643465,-9.955337,-6.441250,-0.636107,7.198464,-1.533558,0.543437,2.970826,0.973916,3.984615,-3.137120,3.691840,9.888060,8.279868,3.200620,-0.115364,4.278554,-9.771121,-8.145798,7.989744,-9.230778,0.904279,-9.438347,6.070338,-0.950264,-2.010273,-2.513818,-7.759496,-0.764669,7.672113,3.889313,-1.812350,-8.511458,2.823924,3.575521,-4.269830,-0.525200,-7.684873,1.089372,-4.053932,-4.175457,-6.542583,5.705350,-9.568201,-7.329829,3.293922,2.863998,-1.008292,-1.368340,0.067588,-1.686483,9.153692,4.896213],[-2.786488,3.686277,-3.123365,1.457470,0.123810,1.561709,-9.327534,0.226403,-2.936780,-9.278398,-0.166454,-2.420524,-9.917239,8.078519,1.879050,1.905602,7.259798,-0.742410,2.550977,-2.576088,-5.543949,-1.879035,1.374236,6.192389,4.623461,-7.725969,-9.374347,3.592792,-6.473223,5.714853,8.836264,4.852235,7.219945,-2.893568,6.087519,5.259429,-5.725296,4.985368,8.443249,5.702654,-7.495119,-5.746672,-5.095930,3.224692,6.670688,-0.930893,-6.280704,7.618846,-9.861098,-4.286063,8.503265,2.242085,7.881811,1.267847,0.070189,6.813599,7.863989,2.615760,9.095689,-4.648917,9.163758,9.038603,-1.086843,2.294645,-4.556341,-1.384854,-8.614312,-9.244309,-5.454757,-7.250727,-7.503563,2.779489,-5.181433,-6.325892,-3.561877,-4.618021,3.060555,4.161868,-3.606289,-7.513202,-6.903271,-9.668958,1.752161,-6.330043,6.241445,0.619362,7.589591,8.797554,3.794561,9.713863,-8.514189,0.171737,-5.700806,9.514217,-9.822345,2.842326,-2.440454,5.610306,-7.526629,-4.499737,-1.428541,-1.188080,-5.473063,6.675176,4.797631,9.483282,-6.639886,2.018361,4.358917,-4.611598,8.867863,-8.316154,7.783442,6.132638,-2.292639,4.341205,1.636863,-8.477566,9.356606,-2.291989,-1.341385,-6.081056,-0.003431,7.466269,-9.013826,3.357859,-2.953025,-2.176126,3.042680,2.743162,8.428922,2.835646,-2.810276,-4.601266,5.301730,-7.627262,5.368931,9.265888,7.242219,1.848440,-3.630069,1.936418,2.225753,-9.382816,0.916469,-4.028137,9.814671,1.356173,1.907914,8.703437,-6.959059,-4.397497,1.804773,-4.158489,9.183236,-1.910929,-7.435729,-1.139699,6.946931,7.404347,-1.243581,7.995279,5.072973,-1.720874,5.201426,6.690055,4.888546,3.615250,2.495512,4.660866,2.646303,-3.589613,9.124258,3.966744,-4.178676,2.655428,-8.275357,-0.693856,-9.260314,-9.519913],[-6.425101,2.869153,-6.097963,-9.896823,-4.235219,-6.199779,-7.899698,-2.398145,9.808654,-8.240339,-5.992907,-7.589949,6.332491,-9.912961,3.455134,7.851026,-4.103033,-0.975862,8.502494,6.266493,-5.511957,2.974673,-7.512660,2.839189,-8.384288,0.182482,8.211578,5.154639,-8.497895,-9.372315,4.655954,-1.066916,9.908818,-4.040933,2.001577,-0.244910,3.841935,-7.924175,5.770666,5.744682,-5.795653,-8.463937,-7.583620,-4.355106,2.611187,2.046846,-6.086583,5.515356,-3.504978,-6.027312,7.222607,7.431138,-2.105798,-1.081428,7.370708,0.747137,0.652509,-9.633243,-1.951305,-9.537521,8.440676,-7.065830,1.158022,1.212114,8.516736,-3.327458,1.491947,1.546746,5.910906,9.619022,4.377733,-2.294220,9.759894,-4.273259,3.005329,0.596810,-0.439891,-6.940365,7.366850,8.678159,8.852458,2.022890,-8.779602,8.632308,0.299020,-8.008335,3.263047,2.402705,9.955972,-4.915744,-5.942169,-9.677097,6.549961,7.872816,-9.604153,6.946117,-2.389530,-6.934406,7.408407,-5.233035,7.475070,0.725463,-0.498285,7.602000,9.422263,-0.739949,9.239752,-9.506101,-8.904464,-5.714307,3.659815,-5.027826,-3.183613,-9.433996,-1.958257,-4.027150,3.312157,2.973717,-7.949112,-3.210728,-3.122275,-0.639825,3.225778,0.077106,-6.153468,-9.870574,6.826180,4.012198,-2.999375,-0.001237,-7.814496,-6.619427,-5.961546,6.480632,-8.604247,-4.033784,0.563011,-1.847950,-2.726810,-1.580903,2.732569,-3.420613,9.921338,9.187582,5.831930,1.451277,-1.389889,9.121238,1.282915,-5.473793,-2.194302,-3.051928,7.098221,-1.973169,-2.707869,-5.218831,-8.799658,2.878183,-4.636653,3.242569,-1.248030,0.685532,-1.286010,2.275353,-1.660395,1.475103,6.404359,-9.982988,-1.354570,-5.023548,7.345374,5.326456,3.982703,4.758676,1.884904,6.827123,2.263050,-2.545321,7.851610,0.353222],[0.764456,4.211701,9.744237,2.333322,-8.468103,-9.253176,-6.636625,8.500836,-8.501835,5.962811,8.720773,8.070508,-5.366194,-2.662500,-5.273964,0.412081,-0.698990,-3.171354,-0.729401,-5.839262,5.979665,-7.859625,-1.274507,0.417530,-0.076155,-1.373153,0.051930,8.266866,4.445400,1.124349,0.898812,-7.558429,9.332921,2.310268,-3.216452,4.846633,7.926437,-9.363895,6.279664,-5.762940,-0.450520,-8.765813,4.237568,2.977685,3.445496,-0.090284,8.766844,7.853318,2.836852,-5.513557,-5.647771,5.044402,4.086290,9.887546,2.109905,4.440774,-1.141906,9.015447,2.541420,-2.135174,5.622319,2.821129,8.879666,-1.446492,-2.987299,7.516926,-9.653895,-9.584343,-2.841333,-7.257255,9.728978,8.016640,9.915512,0.105196,-7.560245,-2.903073,-8.735158,-0.015751,-1.883908,-7.681205,-7.795395,0.628933,-7.184362,-8.179043,5.251448,-9.531905,-1.349244,-5.758985,-6.582980,-8.007565,3.485290,1.589682,9.153408,-1.930002,-8.600908,-3.539515,-9.835441,2.641675,7.802943,3.530557,-2.105609,3.378124,8.628748,4.304987,-3.191688,-3.965789,-2.998807,3.526646,-4.252847,7.556053,9.728037,4.418565,0.032927,-9.296723,-8.201601,4.392184,-9.027935,-6.905524,-7.935066,4.435502,0.124177,-3.170729,7.833596,4.512150,5.127606,-6.779368,-4.482645,-1.467913,-7.413028,-4.200076,-1.327946,-4.991314,5.028364,1.862140,-1.761090,-2.907527,-9.176763,3.950799,-0.528308,7.842640,2.164761,-8.532972,9.486538,3.943628,-4.991278,0.994758,8.350517,8.326347,-8.111415,-0.458378,1.709474,-1.567110,2.559812,-3.144278,3.090317,-1.771725,8.579070,-1.331762,5.224073,3.801424,-1.248183,8.137273,-2.160143,-4.965714,5.024973,1.768044,2.508155,-4.605716,5.820537,-5.695652,0.390135,3.986706,-0.731875,2.329178,8.758380,2.551627,4.748653,7.672800,8.399147,-0.947089],[-5.963215,7.438408,-6.335490,-9.150663,-6.518027,-8.288682,0.068772,9.365044,4.009767,-8.723952,6.414201,-4.088628,-0.835895,-1.190339,2.341910,-1.752747,-5.157835,7.550813,3.549216,-2.608893,8.158114,0.062963,-6.101465,-0.186548,-4.822314,-2.821570,-7.477483,-1.230029,-5.097175,-5.033137,-9.502170,4.420272,-8.420855,6.118694,-0.715905,-2.556048,-7.545266,7.355242,-0.085689,-9.052036,-2.640499,-4.781050,-6.907028,6.751115,8.700173,-7.779114,-4.012287,-4.430290,3.464261,-8.819886,7.713657,4.192222,2.519898,-6.045118,-5.399585,-3.857618,3.038487,6.559085,1.263382,-1.869723,-5.113639,-3.077195,-3.166100,6.994688,-6.956786,0.278770,-2.711389,4.530738,1.160590,4.399722,7.835457,-1.607939,-0.859083,-2.332888,-2.035273,-4.689426,8.243677,5.986505,3.871024,7.030161,5.928573,8.221477,5.550720,0.958296,-8.037510,-5.214553,-6.101423,-1.540514,-9.202543,-0.987131,1.733088,7.276647,-8.999912,-4.913288,-9.360489,1.759298,9.781610,8.883376,-8.465328,1.882926,-5.522092,-4.137680,3.754641,9.361448,3.052152,-7.703994,0.453043,5.033102,3.322609,3.578840,-7.513026,3.234668,-5.649377,-9.793701,8.720747,6.319721,-1.119675,-3.580678,2.428649,8.709751,2.184257,1.069570,-2.438769,-7.976885,3.157673,1.885332,0.092636,2.698070,4.164515,-9.735128,9.899551,-9.942647,1.958915,1.255242,0.822070,1.433864,7.230279,7.987027,4.457280,8.701051,4.807079,-5.605861,8.427477,-1.121177,-3.644931,8.282690,5.314518,5.908542,-5.661791,0.167425,1.075826,-0.951672,8.983624,-2.233242,-0.935314,8.707636,-1.010277,-3.053876,2.828279,6.024354,8.606351,-2.601509,-3.420317,7.412595,-1.633254,-1.145397,0.658718,-1.784173,-0.183894,4.974220,-3.014679,5.480013,1.106242,-3.253510,-6.425544,-9.208304,-5.810302,-9.036313,-9.647491,5.212145],[-7.750521,-7.235824,5.451167,2.282826,-4.437707,-3.688020,0.249456,5.209095,2.195721,-5.349695,4.527878,2.159520,4.219815,4.851742,9.230245,-9.863616,-5.619782,1.771997,-4.494186,-2.702953,8.122238,0.133466,-8.571122,0.211784,2.983752,4.166117,-6.077835,-8.322820,7.729727,9.666621,6.097334,-0.568924,8.289380,4.126737,-2.879320,-5.980371,-7.721652,6.287221,-2.247429,-4.187787,-6.235633,6.321776,-9.553659,-9.521312,4.713181,-8.513987,7.974051,-9.081179,-8.700019,-3.121973,3.026304,-2.542747,4.075389,-2.479519,1.652025,5.449048,8.473549,-0.580633,-7.361197,4.158423,9.529444,-8.924993,-9.103187,1.652600,-9.209104,-0.131349,-3.005408,8.174466,-3.418559,3.083862,-2.319456,7.673954,2.059916,5.070381,-1.505618,4.080883,-9.802138,-3.557295,7.971420,6.880360,-1.569521,2.802965,7.860471,-2.863355,5.840623,8.162337,-5.050138,3.779786,-2.672404,7.077439,4.777775,-7.679006,0.657984,-1.915125,-6.187810,-6.051594,7.705455,2.880030,5.173221,-4.103314,-5.942272,-7.835268,-9.897328,-3.290901,8.233337,2.185914,4.948038,-4.362351,2.871896,5.104466,1.107182,-2.918272,4.150795,9.283695,9.817660,7.431200,0.153444,-0.418915,2.954642,-1.259138,-1.381867,1.679609,-9.656409,-2.247082,1.972586,8.173049,-7.523177,4.156999,-6.940516,-3.124862,8.332920,1.343389,5.487927,-3.516925,-1.312976,4.440368,2.420714,-7.667776,3.582759,1.065062,-5.488411,5.305816,-6.138712,9.673023,8.066709,-8.273161,5.023439,3.913771,1.100974,-1.000914,-5.019383,-7.876659,-2.869020,0.934935,-8.696903,-4.144911,-8.647349,3.235637,4.032559,3.806475,-4.185264,2.394730,7.222177,-8.482374,-5.304186,-7.473405,7.303828,-2.812607,-0.382056,3.362711,-1.255214,8.556457,8.405091,5.283084,3.743466,5.084194,-8.834703,-0.096322,2.795717,-9.736070]], dtype = "float64")#candidate|6272|(6, 180)|const|float64
call_6271 = relay.TupleGetItem(func_2376_call(relay.reshape(const_6272.astype('float64'), [15, 8, 9])), 0)
call_6273 = relay.TupleGetItem(func_2378_call(relay.reshape(const_6272.astype('float64'), [15, 8, 9])), 0)
bop_6275 = relay.not_equal(const_6272.astype('bool'), relay.reshape(call_6271.astype('bool'), relay.shape_of(const_6272))) # shape=(6, 180)
bop_6278 = relay.not_equal(const_6272.astype('bool'), relay.reshape(call_6273.astype('bool'), relay.shape_of(const_6272))) # shape=(6, 180)
func_3891_call = mod.get_global_var('func_3891')
func_3893_call = mutated_mod.get_global_var('func_3893')
const_6283 = relay.const([-8.233286,4.694187,2.173532,9.323844,-7.093851,9.463199,-3.774299,4.330620,-1.868210], dtype = "float64")#candidate|6283|(9,)|const|float64
call_6282 = relay.TupleGetItem(func_3891_call(relay.reshape(const_6283.astype('float64'), [1, 3, 3])), 2)
call_6284 = relay.TupleGetItem(func_3893_call(relay.reshape(const_6283.astype('float64'), [1, 3, 3])), 2)
uop_6286 = relay.log2(call_6271.astype('float64')) # shape=(15, 8, 9)
uop_6288 = relay.log2(call_6273.astype('float64')) # shape=(15, 8, 9)
output = relay.Tuple([call_6266,bop_6275,call_6282,const_6283,uop_6286,])
output2 = relay.Tuple([call_6267,bop_6278,call_6284,const_6283,uop_6288,])
func_6298 = relay.Function([], output)
mod['func_6298'] = func_6298
mod = relay.transform.InferType()(mod)
mutated_mod['func_6298'] = func_6298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6298_call = mutated_mod.get_global_var('func_6298')
call_6299 = func_6298_call()
output = call_6299
func_6300 = relay.Function([], output)
mutated_mod['func_6300'] = func_6300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_6306 = relay.TupleGetItem(func_5109_call(), 0)
call_6307 = relay.TupleGetItem(func_5110_call(), 0)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6310 = func_4162_call()
call_6311 = func_4162_call()
output = relay.Tuple([call_6306,call_6310,])
output2 = relay.Tuple([call_6307,call_6311,])
func_6314 = relay.Function([], output)
mod['func_6314'] = func_6314
mod = relay.transform.InferType()(mod)
mutated_mod['func_6314'] = func_6314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6314_call = mutated_mod.get_global_var('func_6314')
call_6315 = func_6314_call()
output = call_6315
func_6316 = relay.Function([], output)
mutated_mod['func_6316'] = func_6316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4430_call = mod.get_global_var('func_4430')
func_4432_call = mutated_mod.get_global_var('func_4432')
call_6397 = relay.TupleGetItem(func_4430_call(), 2)
call_6398 = relay.TupleGetItem(func_4432_call(), 2)
output = relay.Tuple([call_6397,])
output2 = relay.Tuple([call_6398,])
func_6405 = relay.Function([], output)
mod['func_6405'] = func_6405
mod = relay.transform.InferType()(mod)
output = func_6405()
func_6406 = relay.Function([], output)
mutated_mod['func_6406'] = func_6406
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6414 = relay.var("var_6414", dtype = "int16", shape = ())#candidate|6414|()|var|int16
var_6415 = relay.var("var_6415", dtype = "int16", shape = (5, 16, 1))#candidate|6415|(5, 16, 1)|var|int16
bop_6416 = relay.greater(var_6414.astype('bool'), var_6415.astype('bool')) # shape=(5, 16, 1)
func_1292_call = mod.get_global_var('func_1292')
func_1295_call = mutated_mod.get_global_var('func_1295')
const_6455 = relay.const([-6.196161,7.654325,0.344353,-6.052006,1.448747,-5.425170,-5.010795,-9.610059,5.940646,-6.770258,0.953534,-5.524204,4.683583,-2.850473,-4.107093,-0.439156,4.281066,-3.865520,-9.489424,-6.429959,-7.247842,-4.882829,7.863068,-3.719795,-2.161469,5.069926,-1.764469,7.840458,4.536803,6.593501,-3.273782,-1.900276,7.596381,-1.908874,-6.681257,1.544852,-9.160377,1.837948,9.175213,-0.490750,-8.763203,8.878003,2.858070,-1.013107,-3.850360,-0.885749,8.725478,-8.698529,9.010686,6.335760,-5.854797,-8.562493,-9.225256,-5.645666,7.982016,-5.981782,-5.378681,4.274346,-6.211087,1.764970,1.182439,6.791923,-5.310307,7.160102,-6.972567,8.636623,5.112085,9.496999,-3.213584,0.179794,-2.438999,6.390413,-2.654317,-7.489438,1.247748,6.602127,8.561426,7.744960,8.074631,9.690230,9.357722,-3.573968,2.349265,7.343869,9.301146,6.382786,-0.822441,-2.529366,1.002273,9.596563,-0.625540,5.747219,8.124920,-1.223308,9.811684,-1.060907,-2.993877,-7.925142,4.991216,2.534702,-1.337483,-5.205992,-2.416493,7.637491,-9.450954,-8.323625,-0.724222,-2.965533,-6.008406,-9.807851,2.077421,0.835768,4.294430,6.206506,5.694963,5.973117,2.118258,-8.981930,-8.667183,-2.687492,-8.678558,-7.248315,-2.246098,-3.349064,3.019164,4.315796,9.500813,-4.875368,-3.532394,2.480089,1.247032,5.119076,1.842504,-6.816808,-8.314766,-2.390614,7.172941,2.727827,9.217102,-6.386848,-5.294911,0.711187,-1.044590,-6.061454,6.957127,-9.662509,-7.133119,-1.344448,8.994614,3.920814,5.479662,-3.440863,-9.130807,-4.486505,2.077777,-7.228404,-6.178623,-7.825801,-2.290243,7.722976,-2.369267,-3.974940,-5.205877,-9.952041,1.090534,9.343201,7.480027,0.376948,7.793248,-1.580459,-3.189900,-7.856411,-5.917202,-5.843536,7.782652,2.414767,5.434213,-7.494768,-7.884714,-4.334541,-1.866499,-7.071372,9.195114,-6.550546,5.036185,-8.831029,4.223173,3.559502,3.483234,-5.351650,5.853480,-3.264092,2.778027,-2.931848,-9.804576,4.042816,-0.548856,-2.796586,3.972815,-1.031344,9.251252,0.744074,3.730984,3.997079,-3.461937,8.337667,8.342079,-1.615482,-1.268197,-9.325108,1.430733,-7.038138,5.048619,-4.015671,1.715322,5.108926,7.452149,4.809978,9.526004,4.471949,6.908885,-7.580287,-2.724628,8.189017,1.676529,6.884587,-1.254108,7.721136,3.511170,-8.545606,-9.654056,4.093948,-2.746652,7.017490,8.286012,0.453765,8.152045,8.788683,8.726114,2.169128,-7.054010,0.981333,-8.150559,-1.395281,-7.659804,-9.341480,6.048646,-9.975337,-4.297286,8.423485,-4.019035,-9.268618,-9.196736,-2.306459,2.529054,0.647937,-4.193757,-5.282797,7.467038,-6.308090,1.873500,-8.811015,4.913016,1.976006,-8.635256,7.395451,5.953772,9.674613,-5.134860,3.213867], dtype = "float32")#candidate|6455|(270,)|const|float32
call_6454 = relay.TupleGetItem(func_1292_call(relay.reshape(const_6455.astype('float32'), [10, 9, 3])), 0)
call_6456 = relay.TupleGetItem(func_1295_call(relay.reshape(const_6455.astype('float32'), [10, 9, 3])), 0)
func_4888_call = mod.get_global_var('func_4888')
func_4893_call = mutated_mod.get_global_var('func_4893')
const_6460 = relay.const([7,7,10,-4,-7,-1], dtype = "uint8")#candidate|6460|(6,)|const|uint8
var_6461 = relay.var("var_6461", dtype = "uint8", shape = (54,))#candidate|6461|(54,)|var|uint8
call_6459 = relay.TupleGetItem(func_4888_call(relay.reshape(const_6460.astype('uint8'), [2, 3, 1]), relay.reshape(var_6461.astype('uint8'), [2, 3, 9]), relay.reshape(var_6461.astype('uint8'), [2, 3, 9]), ), 2)
call_6462 = relay.TupleGetItem(func_4893_call(relay.reshape(const_6460.astype('uint8'), [2, 3, 1]), relay.reshape(var_6461.astype('uint8'), [2, 3, 9]), relay.reshape(var_6461.astype('uint8'), [2, 3, 9]), ), 2)
output = relay.Tuple([bop_6416,call_6454,const_6455,call_6459,const_6460,var_6461,])
output2 = relay.Tuple([bop_6416,call_6456,const_6455,call_6462,const_6460,var_6461,])
func_6469 = relay.Function([var_6414,var_6415,var_6461,], output)
mod['func_6469'] = func_6469
mod = relay.transform.InferType()(mod)
mutated_mod['func_6469'] = func_6469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6469_call = mutated_mod.get_global_var('func_6469')
var_6471 = relay.var("var_6471", dtype = "int16", shape = ())#candidate|6471|()|var|int16
var_6472 = relay.var("var_6472", dtype = "int16", shape = (5, 16, 1))#candidate|6472|(5, 16, 1)|var|int16
var_6473 = relay.var("var_6473", dtype = "uint8", shape = (54,))#candidate|6473|(54,)|var|uint8
call_6470 = func_6469_call(var_6471,var_6472,var_6473,)
output = call_6470
func_6474 = relay.Function([var_6471,var_6472,var_6473,], output)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_6498 = func_4162_call()
call_6499 = func_4162_call()
output = relay.Tuple([call_6498,])
output2 = relay.Tuple([call_6499,])
func_6518 = relay.Function([], output)
mod['func_6518'] = func_6518
mod = relay.transform.InferType()(mod)
output = func_6518()
func_6519 = relay.Function([], output)
mutated_mod['func_6519'] = func_6519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_6573 = func_553_call()
call_6574 = func_553_call()
func_5557_call = mod.get_global_var('func_5557')
func_5558_call = mutated_mod.get_global_var('func_5558')
call_6575 = relay.TupleGetItem(func_5557_call(), 0)
call_6576 = relay.TupleGetItem(func_5558_call(), 0)
output = relay.Tuple([call_6573,call_6575,])
output2 = relay.Tuple([call_6574,call_6576,])
func_6624 = relay.Function([], output)
mod['func_6624'] = func_6624
mod = relay.transform.InferType()(mod)
output = func_6624()
func_6625 = relay.Function([], output)
mutated_mod['func_6625'] = func_6625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_6741 = func_553_call()
call_6742 = func_553_call()
func_968_call = mod.get_global_var('func_968')
func_970_call = mutated_mod.get_global_var('func_970')
call_6746 = relay.TupleGetItem(func_968_call(), 0)
call_6747 = relay.TupleGetItem(func_970_call(), 0)
func_1316_call = mod.get_global_var('func_1316')
func_1318_call = mutated_mod.get_global_var('func_1318')
call_6754 = relay.TupleGetItem(func_1316_call(), 2)
call_6755 = relay.TupleGetItem(func_1318_call(), 2)
output = relay.Tuple([call_6741,call_6746,call_6754,])
output2 = relay.Tuple([call_6742,call_6747,call_6755,])
func_6759 = relay.Function([], output)
mod['func_6759'] = func_6759
mod = relay.transform.InferType()(mod)
output = func_6759()
func_6760 = relay.Function([], output)
mutated_mod['func_6760'] = func_6760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6773 = relay.var("var_6773", dtype = "float32", shape = (2, 8, 2))#candidate|6773|(2, 8, 2)|var|float32
uop_6774 = relay.sqrt(var_6773.astype('float32')) # shape=(2, 8, 2)
func_3817_call = mod.get_global_var('func_3817')
func_3820_call = mutated_mod.get_global_var('func_3820')
const_6777 = relay.const([5.273048,1.110400,0.378378,6.984426,-4.544782,-3.428216,8.150498,-6.492323,0.849354,-8.258291,1.572479,-1.570864,0.517449,-1.163769,1.702390,-8.416169,-8.115945,-9.906665,6.423517,-7.964791,4.088733,-8.262772,8.508742,3.307759,4.938639,5.342368,9.775741,0.294399,2.001314,5.845138,1.671073,-7.571196,-6.822165,2.079883,-3.093098,8.746005,-7.794180,-9.611380,-1.524876,0.597451,5.012779,2.101151,-2.248731,1.243454,-6.763749,-8.488138,5.205010,3.491111,-5.077280,5.801603,-3.797548,-3.335758,-3.127280,-0.635389,-1.456023,8.455855,0.753301,-8.218110,0.572898,8.780741,5.620350,7.021432,-9.004278,-6.868571,1.719334,1.021538,-1.693017,8.759517,-2.836059,0.536051,0.380221,-8.096013,2.205900,-3.335299,5.521165,-7.853200,-8.377563,1.353284,3.348492,1.153240,5.643490,-3.341629,-4.797266,-9.113193,-0.405127,-5.624642,-6.127258,-7.791537,5.460278,8.682892,-4.758144,5.518346,3.585153,-9.912663,-1.250163,-6.866305,-6.047862,5.728233,-3.412299,-4.299545,-3.240315,-4.117358,5.684564,-1.578487,5.832510,6.371225,-6.423044,-1.949952,4.046400,-1.334527,-6.707160,1.070079,3.626683,-2.115964,5.038077,-2.575452,9.674453,-2.284562,2.302878,8.807500,-7.225118,7.368214,-7.112438,3.281094,-6.737243,5.807510,-8.900796,9.379647,-6.509336,7.229222,-9.354011,3.748558,-2.383584,3.126310,-3.760197,-8.663450,5.357398,0.048565,-6.747790,-8.625763,-0.530197,5.340996,-7.515672,8.402275,-6.355833,-5.615573,-0.720263,-7.142576,-6.687393,8.445911,4.226014,4.166114,5.904897,-0.393899,1.720067,-2.414991,-3.438673,-6.486457,-8.390311,8.902232,-2.762364,-2.517736,6.712248,8.707776,-9.295496,1.109821,5.080611,-7.692427,7.773532,-7.263123,6.309429,5.256766,-9.015034,0.854057,2.185698,-6.145834,-2.325704,-1.701287,3.571634,2.262028,-9.603635,5.636193,-3.934644,-5.933218,-8.637851,-7.195908,5.947306,-2.757470,-8.439020,2.653929,-9.334425,2.132240,-9.651989,7.823706,-4.303889,7.984982,1.650739,-5.297924,-7.196619,3.697353,4.574051,7.679205,3.458664,-9.266306,7.432995,2.591163,1.315403,-3.455744,9.562234,-8.633572,4.092593,-3.845685,-3.752043,-1.968003,-3.163209,-2.078597,7.509507,-9.084586,4.012040,-1.010169,-2.613916,-5.583178,3.641251,8.989593,-0.144036,-1.105813,9.541897,-0.911459,9.563255,6.170961,9.748142,7.798276,1.401313,8.761607,-5.538986,6.362020,-6.472234,3.547594,-7.286662,-0.832373,-1.665297,-0.524611,4.329701,9.948989,9.186535,-4.874890,-8.581357,-0.883414,-2.536316,-7.947354,1.633401,5.843802,-6.692204,2.668604,-3.757298,8.372315,-6.943624,-5.633383,5.359342,-7.264549,-9.758837,5.253065,-8.955058,-8.406945,0.012638,-7.473962,-6.791548,-9.908151,-2.678661,-1.060207], dtype = "float32")#candidate|6777|(270,)|const|float32
call_6776 = relay.TupleGetItem(func_3817_call(relay.reshape(const_6777.astype('float32'), [10, 9, 3])), 0)
call_6778 = relay.TupleGetItem(func_3820_call(relay.reshape(const_6777.astype('float32'), [10, 9, 3])), 0)
func_4888_call = mod.get_global_var('func_4888')
func_4893_call = mutated_mod.get_global_var('func_4893')
const_6781 = relay.const([-2,7,-9,-2,7,6], dtype = "uint8")#candidate|6781|(6,)|const|uint8
const_6782 = relay.const([-6,6,-6,2,-8,7,-5,8,10,8,5,-10,-10,5,2,-6,10,10,-10,-7,-5,8,9,1,6,-9,-9,-8,-3,2,10,8,9,8,-10,10,1,-7,-4,10,-10,-10,5,7,-8,7,-6,-10,3,-6,2,10,4,4], dtype = "uint8")#candidate|6782|(54,)|const|uint8
call_6780 = relay.TupleGetItem(func_4888_call(relay.reshape(const_6781.astype('uint8'), [2, 3, 1]), relay.reshape(const_6782.astype('uint8'), [2, 3, 9]), relay.reshape(const_6782.astype('uint8'), [2, 3, 9]), ), 1)
call_6783 = relay.TupleGetItem(func_4893_call(relay.reshape(const_6781.astype('uint8'), [2, 3, 1]), relay.reshape(const_6782.astype('uint8'), [2, 3, 9]), relay.reshape(const_6782.astype('uint8'), [2, 3, 9]), ), 1)
output = relay.Tuple([uop_6774,call_6776,const_6777,call_6780,const_6781,const_6782,])
output2 = relay.Tuple([uop_6774,call_6778,const_6777,call_6783,const_6781,const_6782,])
func_6794 = relay.Function([var_6773,], output)
mod['func_6794'] = func_6794
mod = relay.transform.InferType()(mod)
var_6795 = relay.var("var_6795", dtype = "float32", shape = (2, 8, 2))#candidate|6795|(2, 8, 2)|var|float32
output = func_6794(var_6795)
func_6796 = relay.Function([var_6795], output)
mutated_mod['func_6796'] = func_6796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6298_call = mod.get_global_var('func_6298')
func_6300_call = mutated_mod.get_global_var('func_6300')
call_6828 = relay.TupleGetItem(func_6298_call(), 0)
call_6829 = relay.TupleGetItem(func_6300_call(), 0)
func_5886_call = mod.get_global_var('func_5886')
func_5890_call = mutated_mod.get_global_var('func_5890')
var_6835 = relay.var("var_6835", dtype = "float64", shape = (72,))#candidate|6835|(72,)|var|float64
call_6834 = relay.TupleGetItem(func_5886_call(relay.reshape(var_6835.astype('float64'), [2, 12, 3]), relay.reshape(var_6835.astype('float64'), [2, 12, 3]), ), 0)
call_6836 = relay.TupleGetItem(func_5890_call(relay.reshape(var_6835.astype('float64'), [2, 12, 3]), relay.reshape(var_6835.astype('float64'), [2, 12, 3]), ), 0)
uop_6849 = relay.atan(call_6834.astype('float64')) # shape=(2, 12, 3)
uop_6851 = relay.atan(call_6836.astype('float64')) # shape=(2, 12, 3)
func_2918_call = mod.get_global_var('func_2918')
func_2920_call = mutated_mod.get_global_var('func_2920')
var_6858 = relay.var("var_6858", dtype = "uint32", shape = (640,))#candidate|6858|(640,)|var|uint32
call_6857 = relay.TupleGetItem(func_2918_call(relay.reshape(var_6858.astype('uint32'), [640,])), 0)
call_6859 = relay.TupleGetItem(func_2920_call(relay.reshape(var_6858.astype('uint32'), [640,])), 0)
output = relay.Tuple([call_6828,var_6835,uop_6849,call_6857,var_6858,])
output2 = relay.Tuple([call_6829,var_6835,uop_6851,call_6859,var_6858,])
func_6865 = relay.Function([var_6835,var_6858,], output)
mod['func_6865'] = func_6865
mod = relay.transform.InferType()(mod)
mutated_mod['func_6865'] = func_6865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6865_call = mutated_mod.get_global_var('func_6865')
var_6867 = relay.var("var_6867", dtype = "float64", shape = (72,))#candidate|6867|(72,)|var|float64
var_6868 = relay.var("var_6868", dtype = "uint32", shape = (640,))#candidate|6868|(640,)|var|uint32
call_6866 = func_6865_call(var_6867,var_6868,)
output = call_6866
func_6869 = relay.Function([var_6867,var_6868,], output)
mutated_mod['func_6869'] = func_6869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3342_call = mod.get_global_var('func_3342')
func_3344_call = mutated_mod.get_global_var('func_3344')
call_6897 = func_3342_call()
call_6898 = func_3342_call()
output = relay.Tuple([call_6897,])
output2 = relay.Tuple([call_6898,])
func_6901 = relay.Function([], output)
mod['func_6901'] = func_6901
mod = relay.transform.InferType()(mod)
mutated_mod['func_6901'] = func_6901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6901_call = mutated_mod.get_global_var('func_6901')
call_6902 = func_6901_call()
output = call_6902
func_6903 = relay.Function([], output)
mutated_mod['func_6903'] = func_6903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6922 = relay.var("var_6922", dtype = "float32", shape = (10, 15, 2))#candidate|6922|(10, 15, 2)|var|float32
uop_6923 = relay.rsqrt(var_6922.astype('float32')) # shape=(10, 15, 2)
output = uop_6923
output2 = uop_6923
func_6927 = relay.Function([var_6922,], output)
mod['func_6927'] = func_6927
mod = relay.transform.InferType()(mod)
var_6928 = relay.var("var_6928", dtype = "float32", shape = (10, 15, 2))#candidate|6928|(10, 15, 2)|var|float32
output = func_6927(var_6928)
func_6929 = relay.Function([var_6928], output)
mutated_mod['func_6929'] = func_6929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6994 = relay.var("var_6994", dtype = "float64", shape = ())#candidate|6994|()|var|float64
var_6995 = relay.var("var_6995", dtype = "float64", shape = (3, 2, 9))#candidate|6995|(3, 2, 9)|var|float64
bop_6996 = relay.mod(var_6994.astype('float64'), var_6995.astype('float64')) # shape=(3, 2, 9)
uop_7001 = relay.rsqrt(bop_6996.astype('float32')) # shape=(3, 2, 9)
output = uop_7001
output2 = uop_7001
func_7003 = relay.Function([var_6994,var_6995,], output)
mod['func_7003'] = func_7003
mod = relay.transform.InferType()(mod)
var_7004 = relay.var("var_7004", dtype = "float64", shape = ())#candidate|7004|()|var|float64
var_7005 = relay.var("var_7005", dtype = "float64", shape = (3, 2, 9))#candidate|7005|(3, 2, 9)|var|float64
output = func_7003(var_7004,var_7005,)
func_7006 = relay.Function([var_7004,var_7005,], output)
mutated_mod['func_7006'] = func_7006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1099_call = mod.get_global_var('func_1099')
func_1101_call = mutated_mod.get_global_var('func_1101')
call_7013 = relay.TupleGetItem(func_1099_call(), 1)
call_7014 = relay.TupleGetItem(func_1101_call(), 1)
output = call_7013
output2 = call_7014
func_7056 = relay.Function([], output)
mod['func_7056'] = func_7056
mod = relay.transform.InferType()(mod)
mutated_mod['func_7056'] = func_7056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7056_call = mutated_mod.get_global_var('func_7056')
call_7057 = func_7056_call()
output = call_7057
func_7058 = relay.Function([], output)
mutated_mod['func_7058'] = func_7058
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7175 = relay.var("var_7175", dtype = "uint8", shape = (12, 16, 5))#candidate|7175|(12, 16, 5)|var|uint8
const_7176 = relay.const([[[2,-2,8,-3,3],[-3,-3,-6,10,-2],[3,1,-8,-6,-2],[4,2,8,3,7],[5,-6,2,3,-1],[-4,-4,-2,-9,-5],[-5,-4,-4,-9,2],[-4,7,-7,1,2],[-4,-10,-3,-1,1],[3,4,4,-8,8],[10,-8,3,7,3],[9,8,-8,-2,-3],[-6,10,2,9,-1],[-1,-10,-10,-2,6],[-6,5,-4,5,3],[-10,4,10,-6,-7]],[[7,-7,-5,-9,-4],[4,-9,4,-3,9],[4,-6,9,-4,6],[-1,-9,9,7,-3],[-2,9,-8,-7,1],[-9,-7,-5,3,-3],[-1,2,-7,6,-9],[-3,5,-4,-6,-4],[-9,3,-9,2,8],[-3,-2,-10,5,10],[-4,9,-8,2,4],[-10,10,6,-10,1],[6,8,8,6,4],[1,3,-7,1,-5],[-5,7,-8,5,5],[-7,-2,8,3,-5]],[[-2,-4,4,-5,1],[3,5,-9,5,5],[2,1,-7,3,-5],[-8,5,-3,3,6],[-8,-8,-9,7,5],[-3,4,-8,-5,2],[9,8,-3,-3,-10],[8,7,2,7,1],[-1,-8,10,-5,-8],[6,10,1,6,-8],[2,6,-6,-7,-8],[-6,5,-4,-9,-2],[10,4,4,1,-9],[10,-7,-1,7,-7],[-8,-3,-6,-10,8],[3,1,-5,-3,7]],[[-7,3,5,6,-4],[6,7,-5,-8,9],[-8,-3,-10,-6,-7],[6,1,-8,3,-8],[-9,9,6,9,10],[10,-8,8,3,2],[-8,6,8,-4,9],[6,-6,4,-10,6],[10,-9,-10,10,-1],[-5,-1,-8,2,9],[-6,9,-9,-4,9],[8,-7,-10,4,-10],[4,-5,6,-5,-7],[-2,-9,-5,-8,-9],[10,-6,4,3,8],[4,3,-7,3,9]],[[-6,3,4,6,-8],[6,-2,-4,-8,6],[-4,-8,-2,-8,-8],[-4,-8,2,4,1],[-10,-1,-1,1,-6],[7,-7,-9,-1,5],[1,-6,8,-10,-3],[-6,10,-5,2,2],[3,8,-4,1,3],[7,-7,3,-8,-10],[4,3,-3,4,-4],[-3,-6,9,9,7],[7,-6,-4,2,1],[-2,7,-8,-6,6],[-1,-9,4,-6,9],[7,-7,2,3,3]],[[5,-9,-1,-3,-1],[6,-9,-6,-4,-8],[-8,-3,-7,6,1],[3,5,8,-1,4],[9,-4,7,-5,-6],[6,-7,7,-3,5],[-2,-10,2,-4,1],[7,-10,-10,4,-9],[-8,2,-5,-1,-4],[4,5,-5,-4,-2],[-9,-4,-1,-7,2],[3,3,5,-8,10],[-1,10,-10,2,3],[10,-2,-10,-1,-8],[-5,10,8,-7,10],[-10,2,6,4,8]],[[6,9,2,-3,-8],[-5,1,2,1,-8],[7,-1,-8,2,8],[9,-8,2,-10,5],[5,1,-3,7,-2],[-4,-7,-1,5,6],[5,-7,-4,5,5],[3,9,-8,-9,-8],[-2,-2,-9,-3,-8],[10,-6,8,-8,-5],[-4,5,-2,-6,7],[-2,6,9,10,-2],[3,-2,8,9,5],[-1,2,-2,6,-5],[-4,4,-4,-7,-7],[3,-10,-6,-6,-4]],[[-9,-10,8,7,-2],[9,-1,7,-5,2],[-3,1,1,-2,4],[-8,9,-6,-3,-3],[7,-2,4,-6,4],[-3,2,-2,1,9],[-10,-10,6,7,9],[4,-3,-6,6,8],[-9,-10,-4,3,-6],[1,-9,4,9,5],[-3,-5,7,-3,-3],[-4,-1,5,-7,-1],[3,9,-4,-9,6],[10,5,6,-7,5],[-10,-2,5,6,-6],[-7,8,-2,8,-5]],[[7,4,1,4,-10],[7,9,-3,-7,-8],[-6,3,-8,-8,8],[3,-9,5,-6,9],[7,-8,-3,1,-1],[-4,-4,3,-4,10],[-4,-5,-7,-2,-1],[-1,-7,7,1,2],[8,1,5,-4,4],[-10,5,1,10,-7],[6,-1,8,-5,-9],[4,-4,-9,-10,-7],[7,5,3,-3,1],[3,-9,-2,-4,9],[5,1,8,-8,3],[3,3,9,3,-8]],[[-4,-4,5,4,-5],[3,6,-9,3,3],[3,3,5,1,-6],[4,9,-4,6,-6],[-1,-2,4,-1,1],[3,3,9,10,8],[8,-7,-10,1,-1],[8,7,-8,3,8],[-7,-7,10,8,7],[-7,8,2,-9,3],[-2,-9,-2,10,8],[9,-10,6,4,2],[-10,8,5,5,5],[-1,10,5,-8,-7],[-4,10,5,-4,9],[-4,-4,-8,-2,-2]],[[-10,5,-4,-4,-7],[7,-1,7,-4,-7],[-8,-4,3,1,3],[-4,8,-7,-4,-3],[5,-4,8,2,-4],[-4,2,-5,8,-10],[-1,7,8,10,-6],[4,-4,10,2,3],[-3,-6,-5,-9,7],[5,8,7,-8,9],[-3,-7,-1,-8,-9],[7,-8,-8,-4,-5],[8,10,3,-3,8],[7,3,6,-3,9],[7,-7,-10,7,1],[6,-3,-7,-8,9]],[[2,-5,4,-1,8],[-10,-7,-10,-9,1],[-9,3,-7,-10,3],[-9,5,-10,-7,-5],[-2,-2,1,5,8],[-2,-7,1,-7,7],[10,5,-1,-4,9],[-5,-6,1,10,-7],[-4,-9,6,-4,-3],[-3,8,8,-6,-8],[-4,5,4,7,-1],[-4,3,-7,3,2],[-4,-9,-4,2,3],[-4,-6,7,4,-2],[8,2,-9,-8,2],[-8,-4,9,-6,-9]]], dtype = "uint8")#candidate|7176|(12, 16, 5)|const|uint8
bop_7177 = relay.minimum(var_7175.astype('uint8'), relay.reshape(const_7176.astype('uint8'), relay.shape_of(var_7175))) # shape=(12, 16, 5)
bop_7194 = relay.bitwise_or(var_7175.astype('int8'), relay.reshape(const_7176.astype('int8'), relay.shape_of(var_7175))) # shape=(12, 16, 5)
output = relay.Tuple([bop_7177,bop_7194,])
output2 = relay.Tuple([bop_7177,bop_7194,])
func_7199 = relay.Function([var_7175,], output)
mod['func_7199'] = func_7199
mod = relay.transform.InferType()(mod)
var_7200 = relay.var("var_7200", dtype = "uint8", shape = (12, 16, 5))#candidate|7200|(12, 16, 5)|var|uint8
output = func_7199(var_7200)
func_7201 = relay.Function([var_7200], output)
mutated_mod['func_7201'] = func_7201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_553_call = mod.get_global_var('func_553')
func_555_call = mutated_mod.get_global_var('func_555')
call_7203 = func_553_call()
call_7204 = func_553_call()
func_471_call = mod.get_global_var('func_471')
func_474_call = mutated_mod.get_global_var('func_474')
var_7214 = relay.var("var_7214", dtype = "uint32", shape = (42, 1))#candidate|7214|(42, 1)|var|uint32
const_7215 = relay.const([7,-6,8,-1,-2,6,10,-1,-8,-7,-7,-5,-3,-5,-9,7,2,7,9,-2,10,6,-8,6,-7,-2,-2,-9,-7,3,-5,-9,4,-8,-5,-3,-10,7,-4,-3,-8,7,-1,8,-1,1,-1,-2,10,1,2,-2,-3,-10,4,9,-10,5,-1,9,-3,-7,-3,-3,-8,-8,-8,-3,-9,-9,-8,-6,-5,10,-3,-9,9,3,4,7,-10,-10,-7,-1,-8,1,1,4,8,3,3,8,-9,-6,-10,-2,-9,-1,9,-3,2,-3,-1,10,-1,3,-6,-5,-5,-7,3,-5,4,-9,8,10,-7,-5,-9,2,-8,5,-5,9,1,-4], dtype = "uint32")#candidate|7215|(126,)|const|uint32
call_7213 = relay.TupleGetItem(func_471_call(relay.reshape(var_7214.astype('uint32'), [1, 3, 14]), relay.reshape(const_7215.astype('uint32'), [3, 3, 14]), ), 1)
call_7216 = relay.TupleGetItem(func_474_call(relay.reshape(var_7214.astype('uint32'), [1, 3, 14]), relay.reshape(const_7215.astype('uint32'), [3, 3, 14]), ), 1)
bop_7217 = relay.greater(var_7214.astype('bool'), const_7215.astype('bool')) # shape=(42, 126)
uop_7223 = relay.log2(bop_7217.astype('float64')) # shape=(42, 126)
func_703_call = mod.get_global_var('func_703')
func_705_call = mutated_mod.get_global_var('func_705')
call_7225 = relay.TupleGetItem(func_703_call(), 0)
call_7226 = relay.TupleGetItem(func_705_call(), 0)
func_1383_call = mod.get_global_var('func_1383')
func_1386_call = mutated_mod.get_global_var('func_1386')
var_7228 = relay.var("var_7228", dtype = "uint32", shape = (1, 640))#candidate|7228|(1, 640)|var|uint32
call_7227 = relay.TupleGetItem(func_1383_call(relay.reshape(var_7228.astype('uint32'), [10, 16, 4])), 0)
call_7229 = relay.TupleGetItem(func_1386_call(relay.reshape(var_7228.astype('uint32'), [10, 16, 4])), 0)
bop_7239 = relay.bitwise_or(uop_7223.astype('uint64'), relay.reshape(bop_7217.astype('uint64'), relay.shape_of(uop_7223))) # shape=(42, 126)
output = relay.Tuple([call_7203,call_7213,call_7225,call_7227,var_7228,bop_7239,])
output2 = relay.Tuple([call_7204,call_7216,call_7226,call_7229,var_7228,bop_7239,])
func_7242 = relay.Function([var_7214,var_7228,], output)
mod['func_7242'] = func_7242
mod = relay.transform.InferType()(mod)
var_7243 = relay.var("var_7243", dtype = "uint32", shape = (42, 1))#candidate|7243|(42, 1)|var|uint32
var_7244 = relay.var("var_7244", dtype = "uint32", shape = (1, 640))#candidate|7244|(1, 640)|var|uint32
output = func_7242(var_7243,var_7244,)
func_7245 = relay.Function([var_7243,var_7244,], output)
mutated_mod['func_7245'] = func_7245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5557_call = mod.get_global_var('func_5557')
func_5558_call = mutated_mod.get_global_var('func_5558')
call_7260 = relay.TupleGetItem(func_5557_call(), 0)
call_7261 = relay.TupleGetItem(func_5558_call(), 0)
output = call_7260
output2 = call_7261
func_7288 = relay.Function([], output)
mod['func_7288'] = func_7288
mod = relay.transform.InferType()(mod)
output = func_7288()
func_7289 = relay.Function([], output)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_7293 = relay.TupleGetItem(func_5109_call(), 0)
call_7294 = relay.TupleGetItem(func_5110_call(), 0)
uop_7298 = relay.acos(call_7293.astype('float32')) # shape=(4, 15, 4)
uop_7300 = relay.acos(call_7294.astype('float32')) # shape=(4, 15, 4)
var_7306 = relay.var("var_7306", dtype = "float64", shape = (4, 15, 4))#candidate|7306|(4, 15, 4)|var|float64
bop_7307 = relay.less(call_7293.astype('bool'), relay.reshape(var_7306.astype('bool'), relay.shape_of(call_7293))) # shape=(4, 15, 4)
bop_7310 = relay.less(call_7294.astype('bool'), relay.reshape(var_7306.astype('bool'), relay.shape_of(call_7294))) # shape=(4, 15, 4)
func_2649_call = mod.get_global_var('func_2649')
func_2652_call = mutated_mod.get_global_var('func_2652')
var_7324 = relay.var("var_7324", dtype = "float64", shape = (270,))#candidate|7324|(270,)|var|float64
call_7323 = relay.TupleGetItem(func_2649_call(relay.reshape(var_7324.astype('float64'), [30, 9])), 2)
call_7325 = relay.TupleGetItem(func_2652_call(relay.reshape(var_7324.astype('float64'), [30, 9])), 2)
output = relay.Tuple([uop_7298,bop_7307,call_7323,var_7324,])
output2 = relay.Tuple([uop_7300,bop_7310,call_7325,var_7324,])
func_7333 = relay.Function([var_7306,var_7324,], output)
mod['func_7333'] = func_7333
mod = relay.transform.InferType()(mod)
var_7334 = relay.var("var_7334", dtype = "float64", shape = (4, 15, 4))#candidate|7334|(4, 15, 4)|var|float64
var_7335 = relay.var("var_7335", dtype = "float64", shape = (270,))#candidate|7335|(270,)|var|float64
output = func_7333(var_7334,var_7335,)
func_7336 = relay.Function([var_7334,var_7335,], output)
mutated_mod['func_7336'] = func_7336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3770_call = mod.get_global_var('func_3770')
func_3772_call = mutated_mod.get_global_var('func_3772')
call_7370 = relay.TupleGetItem(func_3770_call(), 0)
call_7371 = relay.TupleGetItem(func_3772_call(), 0)
func_5070_call = mod.get_global_var('func_5070')
func_5072_call = mutated_mod.get_global_var('func_5072')
call_7381 = relay.TupleGetItem(func_5070_call(), 1)
call_7382 = relay.TupleGetItem(func_5072_call(), 1)
output = relay.Tuple([call_7370,call_7381,])
output2 = relay.Tuple([call_7371,call_7382,])
func_7400 = relay.Function([], output)
mod['func_7400'] = func_7400
mod = relay.transform.InferType()(mod)
mutated_mod['func_7400'] = func_7400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7400_call = mutated_mod.get_global_var('func_7400')
call_7401 = func_7400_call()
output = call_7401
func_7402 = relay.Function([], output)
mutated_mod['func_7402'] = func_7402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6624_call = mod.get_global_var('func_6624')
func_6625_call = mutated_mod.get_global_var('func_6625')
call_7405 = relay.TupleGetItem(func_6624_call(), 0)
call_7406 = relay.TupleGetItem(func_6625_call(), 0)
func_1370_call = mod.get_global_var('func_1370')
func_1371_call = mutated_mod.get_global_var('func_1371')
call_7416 = relay.TupleGetItem(func_1370_call(), 0)
call_7417 = relay.TupleGetItem(func_1371_call(), 0)
output = relay.Tuple([call_7405,call_7416,])
output2 = relay.Tuple([call_7406,call_7417,])
func_7424 = relay.Function([], output)
mod['func_7424'] = func_7424
mod = relay.transform.InferType()(mod)
mutated_mod['func_7424'] = func_7424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7424_call = mutated_mod.get_global_var('func_7424')
call_7425 = func_7424_call()
output = call_7425
func_7426 = relay.Function([], output)
mutated_mod['func_7426'] = func_7426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6405_call = mod.get_global_var('func_6405')
func_6406_call = mutated_mod.get_global_var('func_6406')
call_7450 = relay.TupleGetItem(func_6405_call(), 0)
call_7451 = relay.TupleGetItem(func_6406_call(), 0)
output = call_7450
output2 = call_7451
func_7468 = relay.Function([], output)
mod['func_7468'] = func_7468
mod = relay.transform.InferType()(mod)
mutated_mod['func_7468'] = func_7468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mutated_mod.get_global_var('func_7468')
call_7469 = func_7468_call()
output = call_7469
func_7470 = relay.Function([], output)
mutated_mod['func_7470'] = func_7470
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7478 = relay.const([[[3.296012,-6.092754,6.608206,-3.495922,1.354655,-6.901976,-6.284288,-7.164531,-3.957827,3.283565,-5.191712]],[[-3.537936,-7.327539,-3.968549,2.861433,1.877751,9.995398,-4.921804,-0.585756,-7.381581,-3.299292,6.328984]]], dtype = "float64")#candidate|7478|(2, 1, 11)|const|float64
uop_7479 = relay.erf(const_7478.astype('float64')) # shape=(2, 1, 11)
var_7481 = relay.var("var_7481", dtype = "float64", shape = (2, 12, 11))#candidate|7481|(2, 12, 11)|var|float64
bop_7482 = relay.right_shift(uop_7479.astype('uint16'), var_7481.astype('uint16')) # shape=(2, 12, 11)
func_2291_call = mod.get_global_var('func_2291')
func_2294_call = mutated_mod.get_global_var('func_2294')
const_7490 = relay.const([[1.017537,8.479838,7.641871,-8.660146,-0.225869,-5.993226,-0.267606,-1.230511,-8.993226,8.184200,-2.953129,0.933171,-4.694059,6.462640,8.278397,1.569714,5.467253,-7.400442,6.143961,6.375383,9.981924,-6.063317,-6.366523,3.066007,8.008450,7.749070,8.253133,-5.255925,-5.843949,0.822128,5.500053,-2.003535,8.731300,-6.944611,8.075266,-3.875938,2.292115,-6.841420,7.390085,-8.490237,1.783887,4.001512,-7.633481,-6.903416,8.702626,-9.690544,-1.376034,-6.193782,-1.686918,-2.961791,-1.745650,-0.696184,0.254421,3.254404,-0.073080,-6.218262,5.545109,7.355521,3.438413,-6.842165,8.036345,-1.423186,4.425102,9.463547,5.334376,-2.657439,-4.659766,0.398659,9.198522,5.427620,-1.485580,7.492650],[2.850043,-6.355311,-0.576431,1.119861,7.901714,-7.391209,-6.578984,-4.849362,3.428203,9.608844,1.065996,-5.153937,3.495892,0.623952,3.454704,-0.559934,8.713540,2.155913,7.640527,5.562543,-7.617383,-9.593567,9.959754,-5.908210,0.963727,-4.958669,-0.800924,8.682417,-7.707698,-9.608772,-7.946947,-2.615952,2.018671,0.853353,7.339956,9.839519,-2.073754,-0.879163,5.801654,1.554925,4.437520,1.980938,-0.179006,1.268450,0.492290,-9.579634,-2.394562,3.221538,-6.613848,3.963645,9.352705,-1.096144,-1.850625,9.340588,4.869516,-8.160289,4.183370,8.058265,-8.910288,-7.854227,-7.155629,4.348304,-4.145599,-6.931861,-6.114591,-7.383186,-5.529448,8.406307,8.553528,-3.796417,3.896251,1.071258],[2.662151,-9.986537,-3.363909,6.007054,9.600885,4.984205,-2.339361,3.968343,5.326750,-8.423833,-5.347815,-1.918747,9.278817,-9.709611,4.259348,2.663697,-7.874382,1.774161,-7.638515,0.996581,4.434198,8.707583,-3.336497,-3.224508,-4.151501,-8.765389,8.238318,6.338418,9.103227,4.725272,0.083111,1.602439,7.747572,-5.276514,-1.747144,1.641682,8.898938,4.347852,5.592585,3.956048,-7.246388,-3.229641,2.340766,-7.972245,-8.088132,8.928584,-9.450137,1.663755,7.355725,-4.925028,-8.685947,-0.863949,-0.966285,6.080940,2.365643,-1.748151,-6.223101,2.285341,-7.330330,4.811116,-9.681057,-7.866709,2.728822,-9.607440,-5.494753,-2.494159,-3.808631,-8.640700,-1.715518,2.172911,-8.708129,-9.411511],[-6.109521,-8.960003,3.055278,4.592746,6.887341,4.766414,-5.926113,2.744322,-2.976802,9.820669,-2.405232,1.605989,4.990222,4.479887,-0.741493,7.566040,2.150639,7.821378,7.581915,-9.363202,9.093687,9.818159,2.485045,-9.451078,9.793568,5.297766,4.655246,-2.997636,5.193102,-3.509964,0.159003,-7.578377,-0.911067,-2.678510,0.761764,-0.043860,-6.630672,-2.241209,-0.368142,9.776303,-6.449178,-7.229638,6.516827,-0.503056,-2.824417,4.793602,-5.779507,-2.609593,0.285035,-7.503857,-3.976026,4.399739,2.574313,-1.400013,-6.574777,2.596216,-9.023941,-1.744327,-4.809274,-5.661364,-8.200417,0.123840,-3.268779,7.236065,-5.661059,-8.048740,-3.892455,4.197369,8.045382,0.035568,6.847715,-9.879629],[-4.197439,2.621992,9.628785,6.787499,7.934228,4.467147,6.017189,-6.794972,-4.600479,-9.380162,-0.315793,-3.254687,2.788892,-9.168994,-5.293465,0.287133,9.478967,-8.632510,-0.624320,-7.645181,-2.607705,0.007569,-6.370433,0.359992,-9.527518,8.801169,9.828334,-1.566203,-8.458015,4.139634,1.066208,7.686580,9.206831,-1.303986,-2.220659,-5.306177,-7.954157,-1.472823,5.609404,3.677627,3.228694,-4.676076,9.343768,3.881658,2.819660,-1.865462,5.469245,-8.498989,3.605334,9.168400,2.026550,-0.852762,1.655067,2.833777,-1.169979,6.915627,4.659291,-8.361506,-6.158198,-0.978837,-7.135216,0.961803,9.903095,3.439634,-3.412475,-9.111476,-5.014368,9.778334,3.533405,-0.997039,1.388582,3.064215],[0.728420,1.621069,8.879649,-0.321097,7.989670,-2.420756,6.829855,5.025377,-9.378830,2.274630,0.153297,-5.550968,7.698716,-2.033163,-6.009008,-1.183576,-2.996068,-3.088378,5.796300,7.705512,-5.676488,2.320278,0.624799,3.397688,-1.605330,-9.575829,6.560836,-8.430989,7.566415,8.288697,-9.430351,-2.971961,-8.546992,6.611509,8.635965,-8.126359,-1.739194,9.782657,-3.992120,1.559436,2.262171,-8.148223,-6.094965,-8.052111,-5.765780,-7.194822,5.957127,4.797711,9.535173,6.155673,9.060774,-6.547437,-9.180139,-6.657701,-9.088414,0.909956,6.695871,-5.591773,4.112001,-4.336619,-1.432930,-1.075664,6.630768,0.022493,-7.505687,0.429464,-9.033598,1.265197,2.391749,-8.732056,6.783987,1.623734],[1.985591,3.689836,-0.659717,-9.551743,-5.292797,-5.071502,-8.324967,-1.757492,7.845350,7.565369,0.202121,-1.068596,-3.789391,-8.108276,-7.753234,-2.468143,0.600191,-9.899921,4.637841,-4.479894,-8.659926,0.618775,1.560476,8.856272,5.046822,-3.092308,-5.484640,6.204308,9.903147,-9.994975,-9.187167,-1.244351,-8.867748,7.907661,8.043987,1.622504,7.858195,5.085884,-3.513942,0.226547,0.802382,-7.169588,-4.299529,-2.458674,1.519168,2.903645,9.467540,6.237683,7.039309,-4.735913,8.844610,-8.917918,-1.358631,8.643404,-3.147445,9.841240,-8.092557,9.707436,7.272443,9.534595,4.962841,-3.328688,-2.936753,-2.118727,0.973522,-7.904037,8.158290,2.580193,-3.883183,-0.270524,3.394559,-5.141583],[-0.969795,-6.288383,0.722216,-0.732920,-1.265021,-0.665069,2.660238,-2.772909,3.720781,0.260704,8.570652,-6.029491,0.646561,0.604400,-5.102717,-9.744436,7.351114,4.808077,-3.449145,7.291636,-7.139054,5.064915,9.018150,-8.367998,5.180600,3.758544,-4.622069,-4.079204,-6.732250,-9.348944,-8.005925,3.649047,5.887900,-2.237993,2.127046,6.298603,9.581914,2.397126,-2.100598,7.882556,3.753689,9.907626,9.759055,9.010642,5.501176,-2.525893,-4.829195,9.968840,-7.633975,-2.379467,-8.837960,-2.293485,-8.594617,-0.886049,6.946929,-3.486848,-9.312183,9.815263,-8.093103,2.437848,-7.055439,4.491516,-4.954620,1.273718,-9.601369,-2.461917,0.549895,3.478213,-1.053815,-0.342456,9.504931,-9.509847],[-8.663848,8.390888,-8.993988,-7.362376,3.478286,0.453736,3.192085,-5.858551,-9.905133,-9.168273,7.022995,-8.589245,7.123487,-1.135998,3.534885,-4.631721,-8.667560,-8.077769,-2.645782,8.523309,-3.230350,9.626170,7.571099,-4.364610,-2.001816,9.579405,-7.003245,8.121460,7.207971,-1.931654,-2.264167,-1.425451,9.049091,7.917299,-1.791432,0.868569,-8.324141,-1.231191,-6.745331,5.648831,0.850020,1.718595,-4.335787,6.941331,-2.876098,0.413904,-7.610875,4.324245,-3.417423,3.246639,1.909034,-9.928180,-1.525953,-9.479281,1.930940,2.801058,-6.317399,-9.328079,-7.488635,-6.067983,0.486561,5.497615,-2.688033,9.662784,-2.582980,6.805849,9.733124,4.821934,-8.442139,5.503805,6.163139,-1.481670],[6.235646,2.543147,-3.093369,-5.880238,8.076147,6.306384,-7.711225,-6.402851,7.691132,-9.826767,3.010848,-3.601439,4.533736,5.415276,2.208001,0.550992,-4.177273,-8.939420,-7.835866,6.415314,-2.207479,8.604753,4.762597,6.418989,0.673196,-5.593172,6.112372,-8.196946,-7.110036,-9.966017,1.945026,-5.550429,-8.111553,-1.751903,9.511537,-7.577258,-4.879870,-5.918841,3.105047,5.780563,1.338732,-6.561188,-3.579958,-8.181391,-4.778349,-2.958773,-3.874103,-4.457646,5.406383,9.742983,-8.376890,5.427708,-3.659226,-1.398000,2.370551,-6.707289,3.396903,-2.804476,-9.048111,-5.298999,5.858472,-5.662082,1.113765,-5.760608,-0.308727,2.602659,0.729366,8.386729,-7.485418,1.226273,4.475804,0.501720],[-5.050941,9.436327,-1.309374,-4.441301,-4.634304,1.788874,4.984117,4.480805,8.021965,-0.648630,1.197849,-3.843367,7.943318,8.521343,-7.709281,-7.301483,-5.584874,9.705501,7.731237,-2.814814,-3.253674,-7.677448,4.145756,1.980890,-2.801323,5.338040,-3.190755,-0.218513,-3.370432,-5.659242,-4.316405,5.476586,-9.025955,5.554974,-8.758891,-1.738574,4.955142,-2.548619,-1.769545,3.079733,2.923022,-7.070127,0.903552,-2.609597,-0.990803,-3.474101,7.979979,-7.094078,-0.775504,0.441409,7.475834,6.475659,-7.093271,-5.086106,-2.133231,-1.240646,-1.786298,9.606799,5.387403,4.804557,-0.131292,-1.487581,-4.486571,-1.717277,-4.317694,3.810436,0.781656,-5.689326,9.355190,-6.456967,-4.912428,7.162096],[0.471496,-7.475761,-9.676757,-9.845108,7.087924,-7.253664,3.345263,-7.889082,4.829314,-9.510386,7.711384,-7.954815,5.808539,-2.516307,8.382107,-0.403108,-3.352065,4.116018,2.559233,3.632607,-6.225901,-7.985182,-6.577073,3.828000,-7.094813,-5.902922,-9.500563,-9.457228,9.020070,-9.983704,1.409954,8.650654,7.210987,-7.860264,4.767968,-8.147752,-1.495471,0.141630,4.050450,-6.273962,-2.462425,9.560448,8.015226,-1.208457,-4.165497,-9.598897,-6.152037,4.686160,-2.387240,-1.786713,-6.329842,-1.858135,9.354050,6.534676,-3.790789,-4.057304,5.163495,-3.965738,-4.619719,4.804358,7.802527,-0.002370,-4.135191,7.647575,1.279530,-3.532465,-6.325939,-7.426985,-9.948159,0.410074,5.484823,-4.069436]], dtype = "float32")#candidate|7490|(12, 72)|const|float32
call_7489 = relay.TupleGetItem(func_2291_call(relay.reshape(const_7490.astype('float32'), [6, 9, 16])), 0)
call_7491 = relay.TupleGetItem(func_2294_call(relay.reshape(const_7490.astype('float32'), [6, 9, 16])), 0)
output = relay.Tuple([bop_7482,call_7489,const_7490,])
output2 = relay.Tuple([bop_7482,call_7491,const_7490,])
func_7493 = relay.Function([var_7481,], output)
mod['func_7493'] = func_7493
mod = relay.transform.InferType()(mod)
mutated_mod['func_7493'] = func_7493
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7494 = relay.var("var_7494", dtype = "float64", shape = (2, 12, 11))#candidate|7494|(2, 12, 11)|var|float64
func_7493_call = mutated_mod.get_global_var('func_7493')
call_7495 = func_7493_call(var_7494)
output = call_7495
func_7496 = relay.Function([var_7494], output)
mutated_mod['func_7496'] = func_7496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5109_call = mod.get_global_var('func_5109')
func_5110_call = mutated_mod.get_global_var('func_5110')
call_7500 = relay.TupleGetItem(func_5109_call(), 0)
call_7501 = relay.TupleGetItem(func_5110_call(), 0)
func_3440_call = mod.get_global_var('func_3440')
func_3443_call = mutated_mod.get_global_var('func_3443')
const_7505 = relay.const([1.916277,-1.825875,-3.671457,-9.106909,-4.062344,-4.004470,-1.909590,-9.340127,9.931378,-4.748416,-2.983335,-4.527069,-1.060377,5.550826,-5.708882,-0.601939,9.615701,-9.848978,2.965548,-7.456447,3.976768,-6.229183,-7.330040,-8.405145,-2.934701,-9.926206,4.939472,3.612107,-0.909314,5.674923,-5.909286,0.272985,-9.377141,4.581113,-5.262666,2.836849,1.919512,-9.033101,-3.398637,2.352031,2.878431,-1.169167,-6.740037,-2.601660,-8.703863,-3.482093,-9.886557,-8.628368,1.559735,-6.826968,2.227282,9.926176,-2.157523,-2.197399,2.700972,2.944759,4.056025,6.520743,1.048518,6.376276,8.170099,-1.639201,4.175853,-7.386702,-8.917684,-5.140218,-2.508386,-9.880238,9.836648,-5.781221,-7.219545,3.976136,9.411247,-9.409818,0.966752,-5.439411,7.192060,-0.438167,6.031440,3.059585,4.742806,0.870519,-2.505814,-2.527401,-2.889603,-0.713930,-4.294325,-1.644208,-4.847963,-2.803746,-8.009627,-4.947115,1.602023,-4.793146,8.611804,2.795319,-4.099762,-5.903128,-0.286359,-4.901624,1.316516,-2.315891,3.293538,6.988624,8.345589,3.018529,-4.451478,6.122997,-7.501259,-3.583369,2.312040,-7.041228,-0.805995,-1.440560,-3.513967,3.773338,5.725390,8.423291,4.758485,-3.359990,5.397106,-1.439549,2.980621,4.626148,-6.484052,8.926894,4.589723,5.593229,8.968332,7.676377,-5.393283,9.503407,-5.303654,-4.674821,-4.052847,-5.503319,-7.901605,4.361211,-3.863786,3.635018,4.267530,-9.489478,6.398849,-0.438863,-4.711899,-5.338296,5.059203,-4.932390,-9.754092,6.575480,-2.713836,-4.353383,-5.342146,-7.349777,7.114701,0.482928,6.612082,9.466278,4.289836,9.407559,1.552874,1.307212,3.639836,-9.664766,-7.210817,-1.495059,7.640995,-1.507183,9.123561,-6.005938,-3.876814,2.308478,-3.857935,-4.165714,-2.623004,3.601867,5.496172,-6.667306,-1.055932,3.943793,-0.816717,7.670174,-9.699383,-0.454576,7.855326,-9.861757,-5.910278,2.575265,1.266266,0.684811,4.137748,7.148294,9.418802,2.404477,9.581728,-7.356469,4.211970,8.417174,7.767975,4.979797,5.348704,6.200355,0.433940,-2.617067,-0.453929,-8.427790,-6.863366,9.268534,-5.641947,6.467765,9.237070,0.426809,-7.212136,-1.702724,-7.322340,-2.850465,-2.593411,-6.586249,-9.416160,-7.200516,-6.042518,-7.897873,-1.951634,-4.058353,-6.957316,-0.984463,8.936578,-7.191641,3.290147,-4.605426,-8.039616,2.814584,-0.836864,-6.440751,-8.826754,1.596290,-5.362457,0.289865,6.413340,3.911856,1.936615,3.728612,0.746970,-1.970577,4.820494,2.596949,3.240129,-4.892755,-2.098917,-3.301542,7.194117,9.276627,5.061851,-0.382629,-0.765782,2.937269,-2.048756,-3.878541,-1.146145,-4.141731,9.275530,-2.407546,-8.143355,-3.389746,3.526204,1.672568,4.914278,-2.936449,1.751973,8.938845,-4.906965,6.363304,-0.924456,9.544603,7.247099,-4.511108,6.855226,9.017067,1.758104,-8.348758,1.941170,6.401684,-9.536520,0.387237,-9.971232,4.856751,0.554742,1.321218,-1.968834,7.468967,-1.078741,0.027174,-1.881421,5.062975,-0.968690,-7.415405,6.453191,-9.359212,-0.509053,8.005443,9.909599,9.806307,-0.004899,-9.144661,7.638120,-0.925532,9.873024,3.762944,-9.801325,5.293402,-6.959879,-2.918095,2.702109,8.099023,9.923236,-3.925272,2.507950,4.121484,4.903576,6.570198,3.704623,-0.726832,8.143105,-4.996843,1.346929,-5.637644,-8.418661,3.147220,-1.123711,4.308152,-3.084229,-1.284825,6.222447,0.461023,9.158568,-7.456717,-9.632425,4.617122,-0.601054,0.988177,6.896943,-3.941323,2.194162,7.439823,-4.996452,9.088796,-4.565640,8.155802,0.217929,-3.675117,8.528056,-3.963081,-3.859613,1.405717,6.040510,-3.468665,-5.570885,-4.661686,-8.511889,8.486979,-5.490468,0.944210,-3.822795,0.653287,6.530338,-7.934786,-9.630908,-7.566370,-2.412419,9.722542,3.224531,-2.951831,-7.477128,9.934508,-0.461852,-8.219801,8.775768,-8.794032,-8.192764,7.153690,3.185572,-5.689527,-7.141752,-3.229858,-0.802683,4.797367,7.278470,8.290855,-5.764662,0.523712,-0.712740,-8.584244,8.941168,6.522117,-7.139934,-9.231870,3.580920,0.601554,8.102285,-8.656458,5.391827,0.955195,-2.836849,4.351698,3.422156,7.385480,-4.394320,5.284526,-5.317618,7.944576,-7.366081,3.941177,-9.313157,6.534703,-0.892881,7.107750,9.102370,6.782439,8.988080,1.591115,2.767798,-7.735875,-8.592853,3.959216,7.914693,0.083690,-2.766472,4.606782,4.391860,9.053358,-1.569969,3.618848,5.768418,7.018427,1.294856,-1.190139,-0.608989,-5.009024,-9.300450,1.113722,-5.044941,8.374558,5.038251,6.109670,-6.263711,6.968452,8.650805,-6.501870,2.054021,-5.240083,-5.981389,4.587530,8.631360,5.130049,3.285159,7.424144,1.117832,1.745622,8.239075,2.850373,7.245307,5.781395,-5.509768,3.440688,2.210434,-0.024721,-3.758632,-8.442661,-3.123474,-5.547316,7.425541,5.572882,-9.714517,5.430430,-3.024332,2.914399,2.045167,-3.370213,3.182838,2.139349], dtype = "float64")#candidate|7505|(480,)|const|float64
call_7504 = relay.TupleGetItem(func_3440_call(relay.reshape(const_7505.astype('float64'), [2, 15, 16])), 1)
call_7506 = relay.TupleGetItem(func_3443_call(relay.reshape(const_7505.astype('float64'), [2, 15, 16])), 1)
func_2179_call = mod.get_global_var('func_2179')
func_2182_call = mutated_mod.get_global_var('func_2182')
const_7526 = relay.const([[-7.580994],[5.242046],[3.404347],[0.372477],[7.978445],[-5.990784],[3.042858],[4.950370],[7.820223],[-0.784811],[-4.080486],[-7.919214],[-6.770387],[5.480210],[4.488719],[-8.968862],[-0.736788],[-1.237723],[-8.182399],[3.670571],[-1.914609],[3.979367],[-2.173368],[-9.648319],[-6.952137],[-9.936550],[2.098141],[3.747324],[-6.633431],[-1.731417],[-2.717399],[5.058348],[-5.070080],[-1.996071],[8.779796],[-6.024168],[8.761382],[3.655238],[-0.612804],[8.087690],[6.055652],[-6.659561],[-8.351750],[-6.702887],[-1.531010],[1.171214],[-1.662498],[-0.077942],[-7.021450],[4.063042],[-1.024709],[2.880602],[8.814758],[9.067076],[-7.809453],[-9.532221],[-8.266343],[-0.551083],[-3.124866],[4.467731],[3.759232],[-0.818483],[7.220495],[-4.287232],[2.111805],[1.607559],[8.217971],[-0.671598],[-9.824895],[8.533181],[-6.598571],[-0.169412],[-5.037209],[-3.174644],[9.071961],[6.688150],[-4.121619],[-8.856658],[-5.516388],[7.219342],[-7.624975],[-0.605813],[1.369964],[3.120336],[-7.199578],[-1.395874],[-6.173532],[-8.481632],[3.997481],[-4.293486],[-7.280789],[8.540247],[1.483068],[0.606692],[-5.362007],[1.534732],[8.040882],[-5.932248],[-1.222504],[-3.946463],[-5.803143],[-1.930716],[2.067154],[4.612633],[1.021372],[-1.054125],[-7.214518],[-1.019700],[4.203666],[3.013957],[-0.991471],[2.944257],[-2.434482],[-6.709912],[4.228001],[-9.834973],[1.760202],[-9.922849],[3.669612],[5.982710],[3.979552],[-8.875444],[1.384614],[9.872930],[-4.885444],[-9.998415],[-9.847772],[8.802815],[0.777741],[1.139873],[-1.660920],[6.690258],[-9.402853],[9.702894],[9.764584],[-3.201924],[-0.583427],[-9.673843],[7.870833],[-7.832295],[6.702633],[-2.963025],[-6.442955],[-8.341049],[8.115597],[-8.067475],[2.434401],[4.864120],[-8.464367],[4.429610],[3.377731],[-9.934836],[1.620724],[7.666395],[0.509037],[-3.017941],[-5.053582],[-7.888356],[-5.720145],[1.010564],[-4.118012],[-3.285114],[0.548127],[-8.066551],[-8.801118],[3.728406],[0.873226],[5.799572],[5.966956],[-1.814552],[-6.270279],[9.453783],[8.985186],[-7.654978],[-8.134868],[-9.342466],[4.684123],[4.304972],[-4.256824],[-2.095438],[7.054306],[8.441324],[-5.062464],[3.090066],[2.465179],[-0.548184],[2.162400],[9.226652],[4.577568],[-7.612850],[3.047363],[-8.164793],[0.004619],[1.446540],[4.299164],[-7.810786],[6.853550],[-3.817984],[-2.093953],[2.363456],[8.726093],[-5.328313],[6.687534],[1.515913],[5.305016],[0.195134],[-3.752090],[5.183419],[9.158299],[-6.828578],[9.581687],[7.585094],[-5.558098],[-6.197195],[-1.002567],[-3.545665],[4.001751],[-0.993499],[-9.191081],[6.201860],[0.942846],[-5.102235],[-9.878619],[-9.586117],[-1.214543],[2.200352],[1.440528],[8.549838],[-7.348094],[0.396905],[8.146444],[-5.142235],[-3.881896],[-5.333531],[-4.201318],[-0.634210],[-5.612589],[-0.710007],[-8.194518],[-1.138583],[7.015586],[-5.360065],[-6.532984],[-7.878911],[5.605254],[1.895594],[5.167623],[1.316038],[-3.863867],[9.899037],[1.541957],[4.793478],[-4.036539],[6.822154],[-2.268697],[-6.141312],[5.191244],[-2.194092],[-4.211313],[-9.449268],[-6.197105],[-5.186585],[6.106308],[7.061762],[6.039947],[-1.541962],[-2.954926],[-2.249286],[7.115840],[-8.752689]], dtype = "float64")#candidate|7526|(270, 1)|const|float64
call_7525 = relay.TupleGetItem(func_2179_call(relay.reshape(const_7526.astype('float64'), [10, 9, 3])), 0)
call_7527 = relay.TupleGetItem(func_2182_call(relay.reshape(const_7526.astype('float64'), [10, 9, 3])), 0)
output = relay.Tuple([call_7500,call_7504,const_7505,call_7525,const_7526,])
output2 = relay.Tuple([call_7501,call_7506,const_7505,call_7527,const_7526,])
func_7531 = relay.Function([], output)
mod['func_7531'] = func_7531
mod = relay.transform.InferType()(mod)
output = func_7531()
func_7532 = relay.Function([], output)
mutated_mod['func_7532'] = func_7532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6016_call = mod.get_global_var('func_6016')
func_6018_call = mutated_mod.get_global_var('func_6018')
call_7541 = relay.TupleGetItem(func_6016_call(), 2)
call_7542 = relay.TupleGetItem(func_6018_call(), 2)
output = call_7541
output2 = call_7542
func_7543 = relay.Function([], output)
mod['func_7543'] = func_7543
mod = relay.transform.InferType()(mod)
output = func_7543()
func_7544 = relay.Function([], output)
mutated_mod['func_7544'] = func_7544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7606 = relay.var("var_7606", dtype = "uint32", shape = (6, 4, 1))#candidate|7606|(6, 4, 1)|var|uint32
const_7607 = relay.const([[[5,-2,-9,3,3,-6,-9,-8,-6,9,-6,-4],[4,-7,-10,-2,-4,-10,-3,6,6,2,7,-6],[-6,4,8,4,-7,-8,-1,-2,5,7,6,-5],[-5,8,7,-6,9,-7,-5,8,10,-1,-6,-6]],[[-4,10,-6,4,2,-3,6,-3,9,-3,-9,-8],[-8,-3,-1,-9,2,7,-4,9,-3,-6,4,-7],[9,7,2,10,4,8,10,2,-7,-10,-2,-9],[-3,-5,4,8,-3,-3,10,-6,-7,-2,2,-1]],[[-5,-1,1,-3,5,-1,-1,6,6,8,5,2],[2,2,-8,-2,5,-1,5,3,1,3,-5,-3],[-10,-8,-8,-8,-4,4,-3,-6,-4,-7,10,-1],[3,10,-2,-8,-7,7,7,-8,6,-5,-10,9]],[[8,3,5,-7,-7,-6,-2,-1,-1,6,4,8],[-6,10,4,10,-7,-9,4,-3,-3,-9,-5,5],[9,-3,3,-2,4,5,-3,-9,-7,-7,4,-1],[10,5,-10,-1,-2,-1,-10,4,-7,4,-3,4]],[[-1,10,-10,-4,2,-6,-10,3,-3,-6,9,7],[-10,-8,3,-2,1,-2,4,-1,-7,-3,4,-8],[-10,10,-4,-5,-9,7,5,8,1,6,8,-6],[-4,2,4,-5,-2,-6,-3,1,4,-3,7,-4]],[[3,-6,7,6,10,9,7,10,8,-8,-7,-2],[8,1,-9,6,6,3,-5,-7,6,-8,-10,4],[4,-1,-4,-3,10,-10,2,-1,9,2,-10,8],[4,10,-4,-2,-8,-9,-7,5,-10,-6,-2,-1]]], dtype = "uint32")#candidate|7607|(6, 4, 12)|const|uint32
bop_7608 = relay.maximum(var_7606.astype('uint32'), const_7607.astype('uint32')) # shape=(6, 4, 12)
func_2893_call = mod.get_global_var('func_2893')
func_2894_call = mutated_mod.get_global_var('func_2894')
call_7617 = relay.TupleGetItem(func_2893_call(), 2)
call_7618 = relay.TupleGetItem(func_2894_call(), 2)
output = relay.Tuple([bop_7608,call_7617,])
output2 = relay.Tuple([bop_7608,call_7618,])
func_7621 = relay.Function([var_7606,], output)
mod['func_7621'] = func_7621
mod = relay.transform.InferType()(mod)
var_7622 = relay.var("var_7622", dtype = "uint32", shape = (6, 4, 1))#candidate|7622|(6, 4, 1)|var|uint32
output = func_7621(var_7622)
func_7623 = relay.Function([var_7622], output)
mutated_mod['func_7623'] = func_7623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4162_call = mod.get_global_var('func_4162')
func_4164_call = mutated_mod.get_global_var('func_4164')
call_7667 = func_4162_call()
call_7668 = func_4162_call()
output = call_7667
output2 = call_7668
func_7689 = relay.Function([], output)
mod['func_7689'] = func_7689
mod = relay.transform.InferType()(mod)
output = func_7689()
func_7690 = relay.Function([], output)
mutated_mod['func_7690'] = func_7690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4823_call = mod.get_global_var('func_4823')
func_4825_call = mutated_mod.get_global_var('func_4825')
call_7694 = relay.TupleGetItem(func_4823_call(), 1)
call_7695 = relay.TupleGetItem(func_4825_call(), 1)
output = relay.Tuple([call_7694,])
output2 = relay.Tuple([call_7695,])
func_7713 = relay.Function([], output)
mod['func_7713'] = func_7713
mod = relay.transform.InferType()(mod)
output = func_7713()
func_7714 = relay.Function([], output)
mutated_mod['func_7714'] = func_7714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7726 = relay.var("var_7726", dtype = "float64", shape = (1, 12, 1))#candidate|7726|(1, 12, 1)|var|float64
var_7727 = relay.var("var_7727", dtype = "float64", shape = (1, 12, 8))#candidate|7727|(1, 12, 8)|var|float64
bop_7728 = relay.divide(var_7726.astype('float64'), var_7727.astype('float64')) # shape=(1, 12, 8)
bop_7734 = relay.less_equal(var_7726.astype('bool'), var_7727.astype('bool')) # shape=(1, 12, 8)
func_6314_call = mod.get_global_var('func_6314')
func_6316_call = mutated_mod.get_global_var('func_6316')
call_7740 = relay.TupleGetItem(func_6314_call(), 0)
call_7741 = relay.TupleGetItem(func_6316_call(), 0)
uop_7751 = relay.log2(call_7740.astype('float64')) # shape=(4, 15, 4)
uop_7753 = relay.log2(call_7741.astype('float64')) # shape=(4, 15, 4)
func_7242_call = mod.get_global_var('func_7242')
func_7245_call = mutated_mod.get_global_var('func_7245')
var_7765 = relay.var("var_7765", dtype = "uint32", shape = (42,))#candidate|7765|(42,)|var|uint32
var_7766 = relay.var("var_7766", dtype = "uint32", shape = (640,))#candidate|7766|(640,)|var|uint32
call_7764 = relay.TupleGetItem(func_7242_call(relay.reshape(var_7765.astype('uint32'), [42, 1]), relay.reshape(var_7766.astype('uint32'), [1, 640]), ), 2)
call_7767 = relay.TupleGetItem(func_7245_call(relay.reshape(var_7765.astype('uint32'), [42, 1]), relay.reshape(var_7766.astype('uint32'), [1, 640]), ), 2)
var_7768 = relay.var("var_7768", dtype = "float64", shape = (3, 12, 8))#candidate|7768|(3, 12, 8)|var|float64
bop_7769 = relay.power(var_7727.astype('float32'), var_7768.astype('float32')) # shape=(3, 12, 8)
output = relay.Tuple([bop_7728,bop_7734,uop_7751,call_7764,var_7765,var_7766,bop_7769,])
output2 = relay.Tuple([bop_7728,bop_7734,uop_7753,call_7767,var_7765,var_7766,bop_7769,])
F = relay.Function([var_7726,var_7727,var_7765,var_7766,var_7768,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7726,var_7727,var_7765,var_7766,var_7768,], output2)
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
