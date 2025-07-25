import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_291 = relay.var("var_291", dtype = "uint16", shape = (15, 1, 7))#candidate|291|(15, 1, 7)|var|uint16
var_292 = relay.var("var_292", dtype = "uint16", shape = (15, 3, 7))#candidate|292|(15, 3, 7)|var|uint16
bop_293 = relay.bitwise_and(var_291.astype('uint16'), var_292.astype('uint16')) # shape=(15, 3, 7)
uop_299 = relay.exp(var_291.astype('float32')) # shape=(15, 1, 7)
output = relay.Tuple([bop_293,uop_299,])
output2 = relay.Tuple([bop_293,uop_299,])
func_307 = relay.Function([var_291,var_292,], output)
mod['func_307'] = func_307
mod = relay.transform.InferType()(mod)
var_308 = relay.var("var_308", dtype = "uint16", shape = (15, 1, 7))#candidate|308|(15, 1, 7)|var|uint16
var_309 = relay.var("var_309", dtype = "uint16", shape = (15, 3, 7))#candidate|309|(15, 3, 7)|var|uint16
output = func_307(var_308,var_309,)
func_310 = relay.Function([var_308,var_309,], output)
mutated_mod['func_310'] = func_310
mutated_mod = relay.transform.InferType()(mutated_mod)
const_487 = relay.const([[[-1.028613,-7.174865,3.757567],[2.055176,-8.719723,8.848504],[-1.569226,-7.408189,-1.299016],[0.395959,-8.069633,4.724528],[-3.419184,-9.667709,6.291375],[1.268670,6.991038,0.887090],[-2.331836,-0.273062,-5.613350],[-9.335941,-6.013673,2.625782],[2.898057,5.087588,-3.325640],[5.977925,-7.484532,-5.757930],[9.251445,3.309352,1.838059],[4.559854,1.115755,-0.104448],[-4.024775,-7.300894,6.290148],[9.412246,-0.597451,-1.321391],[7.657676,4.824980,5.903482],[-2.207634,-5.406014,-6.311082]],[[-2.613420,0.758769,7.614116],[-5.389297,6.418196,-6.985266],[-1.390398,4.204083,-5.337259],[9.477394,-8.404403,2.734991],[-8.078155,-1.315161,-8.379702],[-8.118141,1.373875,-9.787336],[-8.205900,-6.099892,-2.463660],[-8.133225,-0.508983,3.411784],[-8.884882,-2.210394,-5.755892],[-8.064225,6.192009,9.338400],[8.025273,4.970888,6.544003],[-0.061041,-8.146017,9.347250],[3.379081,5.681409,-0.286114],[0.509577,8.313204,2.300285],[8.934361,-8.705718,-7.741244],[-5.466892,5.020578,-6.739485]],[[-5.319307,-5.949489,3.861060],[7.784057,-7.638345,-1.875458],[1.329152,7.025490,-2.787856],[-4.836256,-7.580430,-5.018690],[-5.231594,5.470911,-7.624484],[0.125249,-9.946509,8.630586],[7.207917,-1.776055,0.841099],[-7.846212,-5.147916,8.466164],[-7.717334,5.556059,-7.707959],[-7.697882,-6.526476,2.236612],[6.957266,1.608170,-9.410824],[-2.893824,5.952530,1.968127],[0.852117,-2.822671,9.258375],[-1.227688,2.434923,3.935384],[-1.347897,3.025017,6.203251],[2.502115,4.724383,-6.835049]],[[-2.939359,6.456200,5.083239],[-3.738918,0.351885,5.580339],[9.669008,-8.852922,6.504334],[-5.501731,2.834173,-7.251981],[-8.230145,-0.138628,7.970686],[-9.904571,7.049052,6.543257],[-1.729121,2.539132,-9.259675],[2.527128,7.525039,6.824991],[0.492875,-1.431174,7.912264],[1.688493,-5.826665,2.338613],[-2.502312,1.152386,7.873950],[-4.065601,5.144317,6.223899],[-5.059604,6.771163,0.946895],[-6.932022,-1.274817,7.044891],[-8.389674,-4.460580,-2.446932],[-4.567626,5.440334,-0.199729]],[[-9.287217,-8.726766,1.876033],[-1.065376,-0.316463,2.514570],[-4.913637,-6.216000,-3.578063],[-1.880783,-7.311046,0.785057],[-9.337616,5.090021,-3.780017],[-9.343924,4.230580,-7.719920],[2.462021,-6.463974,-5.767782],[3.008678,-2.406419,1.834475],[2.072716,3.837622,-6.816578],[1.691574,-8.000003,-5.578608],[-5.025000,6.320447,-1.645097],[-8.638689,-6.484906,4.310378],[-3.103152,5.453504,0.263048],[7.287356,-3.155599,-5.665069],[-5.884082,5.732465,6.076666],[9.817024,6.253982,9.606997]]], dtype = "float32")#candidate|487|(5, 16, 3)|const|float32
uop_488 = relay.exp(const_487.astype('float32')) # shape=(5, 16, 3)
uop_491 = relay.log(const_487.astype('float64')) # shape=(5, 16, 3)
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
const_511 = relay.const([-1,6,8,-7,-3,-9,2,-2,1,10,1,-10,10,-7,5,-3,-3,-4,-2,1,3,6,1,-10,1,2,-10,8,-4,-8,3,5,10,-6,-2,10,6,-3,-1,9,3,-3,-6,2,7,8,3,3,-5,-8,5,-2,-3,8,-8,-5,8,3,-10,-5,6,5,9,5,-9,2,-2,-5,-9,-8,-9,7,2,5,-6,-8,-4,-4,-1,8,3,-3,6,1,-2,4,5,-3,3,8,6,2,9,4,4,-1,4,3,4,5,6,-9,1,7,-8], dtype = "uint16")#candidate|511|(105,)|const|uint16
const_512 = relay.const([-2,-8,8,2,-6,10,-1,-9,-8,2,4,-2,-1,-10,5,7,-6,-8,-6,8,-5,1,-1,10,-5,-5,2,-5,-8,6,-8,-1,-7,-1,-9,-7,9,-8,-8,-2,-9,-1,4,-7,-1,-6,-5,5,5,-9,7,7,-1,6,3,2,5,-4,7,3,-4,7,7,-3,10,-7,7,-2,-8,10,8,-5,5,-6,-3,-2,-2,-8,3,-1,5,-9,-1,3,-1,5,4,6,1,2,1,-3,-3,1,-2,8,-2,8,-9,-7,3,-2,1,-6,10,-8,-2,-3,10,10,10,-9,-6,-10,-7,7,-8,-7,-7,-3,1,-5,2,7,-5,6,-6,10,2,-8,4,9,4,-10,8,-5,7,-1,1,-3,-4,2,3,-3,9,-4,-7,-4,10,10,-1,9,7,7,6,2,8,-10,-5,6,4,-8,4,2,8,-5,8,-7,4,3,-3,-9,-1,3,-2,2,2,5,-2,1,-8,8,-10,1,6,-3,-10,-1,-1,-7,-5,7,8,3,-8,7,1,-3,10,-3,9,7,-8,10,-3,2,-7,5,-2,5,-1,7,-10,2,-4,10,1,-3,-8,-10,-4,-8,1,6,2,-3,-6,4,1,-7,1,10,-5,-4,-10,3,-7,4,-6,3,-2,10,7,3,2,-4,-7,8,9,-2,-4,-2,-6,1,7,-10,10,-8,-6,6,-10,2,7,9,1,5,-6,6,-3,6,1,-8,7,-8,6,-2,4,-4,-5,-7,4,-2,10,4,5,1,7,-6,5,9,6,6,7,-3,2,-7,-3,-9,-6,-4,5,8,-7,8,6,3,-9,4,-10,-6,-6,-1,3,1,2], dtype = "uint16")#candidate|512|(315,)|const|uint16
call_510 = relay.TupleGetItem(func_307_call(relay.reshape(const_511.astype('uint16'), [15, 1, 7]), relay.reshape(const_512.astype('uint16'), [15, 3, 7]), ), 0)
call_513 = relay.TupleGetItem(func_310_call(relay.reshape(const_511.astype('uint16'), [15, 1, 7]), relay.reshape(const_512.astype('uint16'), [15, 3, 7]), ), 0)
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
call_528 = relay.TupleGetItem(func_307_call(relay.reshape(const_511.astype('uint16'), [15, 1, 7]), relay.reshape(call_510.astype('uint16'), [15, 3, 7]), ), 0)
call_529 = relay.TupleGetItem(func_310_call(relay.reshape(const_511.astype('uint16'), [15, 1, 7]), relay.reshape(call_510.astype('uint16'), [15, 3, 7]), ), 0)
uop_533 = relay.log2(uop_491.astype('float64')) # shape=(5, 16, 3)
output = relay.Tuple([uop_488,call_510,const_511,const_512,call_528,uop_533,])
output2 = relay.Tuple([uop_488,call_513,const_511,const_512,call_529,uop_533,])
func_537 = relay.Function([], output)
mod['func_537'] = func_537
mod = relay.transform.InferType()(mod)
output = func_537()
func_538 = relay.Function([], output)
mutated_mod['func_538'] = func_538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_563 = relay.TupleGetItem(func_537_call(), 2)
call_564 = relay.TupleGetItem(func_538_call(), 2)
output = call_563
output2 = call_564
func_575 = relay.Function([], output)
mod['func_575'] = func_575
mod = relay.transform.InferType()(mod)
output = func_575()
func_576 = relay.Function([], output)
mutated_mod['func_576'] = func_576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_586 = func_575_call()
call_587 = func_575_call()
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_603 = func_575_call()
call_604 = func_575_call()
output = relay.Tuple([call_586,call_603,])
output2 = relay.Tuple([call_587,call_604,])
func_608 = relay.Function([], output)
mod['func_608'] = func_608
mod = relay.transform.InferType()(mod)
output = func_608()
func_609 = relay.Function([], output)
mutated_mod['func_609'] = func_609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_615 = relay.TupleGetItem(func_537_call(), 5)
call_616 = relay.TupleGetItem(func_538_call(), 5)
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_620 = relay.TupleGetItem(func_608_call(), 0)
call_621 = relay.TupleGetItem(func_609_call(), 0)
const_622 = relay.const([-10,-9,3,3,3,-9,-10,-5,-9,10,-1,-7,-6,-3,-2,8,4,-10,-3,8,-2,4,-2,-7,-8,-3,2,3,7,-3,-5,-2,10,-5,-4,9,-2,1,4,4,-3,-10,-1,4,-10,-10,10,5,3,-3,7,-6,-6,2,3,1,-5,4,3,7,-5,-10,8,-4,-9,1,-10,-2,3,6,10,-5,-6,2,-7,5,-5,-8,4,5,1,-7,2,-9,3,-3,1,-7,-9,10,-9,7,-2,8,-6,-9,-8,10,-4,-7,2,-10,-9,4,8], dtype = "uint16")#candidate|622|(105,)|const|uint16
bop_623 = relay.bitwise_or(call_620.astype('uint64'), relay.reshape(const_622.astype('uint64'), relay.shape_of(call_620))) # shape=(105,)
bop_626 = relay.bitwise_or(call_621.astype('uint64'), relay.reshape(const_622.astype('uint64'), relay.shape_of(call_621))) # shape=(105,)
output = relay.Tuple([call_615,bop_623,])
output2 = relay.Tuple([call_616,bop_626,])
func_638 = relay.Function([], output)
mod['func_638'] = func_638
mod = relay.transform.InferType()(mod)
output = func_638()
func_639 = relay.Function([], output)
mutated_mod['func_639'] = func_639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_680 = relay.var("var_680", dtype = "float32", shape = (3, 15, 6))#candidate|680|(3, 15, 6)|var|float32
uop_681 = relay.cos(var_680.astype('float32')) # shape=(3, 15, 6)
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
var_688 = relay.var("var_688", dtype = "uint16", shape = (1, 105))#candidate|688|(1, 105)|var|uint16
const_689 = relay.const([8,10,7,2,8,-5,9,9,-1,5,8,1,6,-4,-9,-9,-4,-4,1,-1,4,-2,-4,-8,-1,4,-2,-3,-8,-3,7,6,9,4,-6,10,1,-2,10,1,-5,-5,10,5,6,-7,-10,-4,-2,10,5,7,-10,2,-9,5,10,10,7,-9,3,-6,10,-1,-10,10,3,-1,6,-4,10,10,-9,-1,-8,-9,-8,-6,-7,-3,-10,-4,2,-5,-3,-5,10,3,8,4,-6,-6,10,-5,1,-5,2,-3,9,5,8,-6,-7,-6,5,-10,-4,5,10,-10,1,1,9,10,-1,1,-4,8,6,-8,-7,-9,-9,-5,-8,2,-2,-3,-7,8,-7,-9,-6,4,-4,-10,-3,2,-7,2,1,5,9,4,-10,-5,-1,-7,3,6,6,-8,7,4,4,9,2,-9,-1,-8,-5,-9,-9,-3,10,2,7,8,10,2,-9,-9,7,3,-1,1,4,-4,6,7,-9,5,-1,-4,4,4,6,-6,1,3,8,10,3,7,3,9,-5,10,7,6,9,-7,-3,-10,-10,-8,8,-2,-4,-4,3,1,-8,-5,-6,-8,-2,1,-8,10,5,-8,-8,6,9,2,-1,-3,3,-6,10,-5,-9,-8,9,-8,-7,-9,-9,10,-3,4,-3,-5,-7,-7,-4,-1,-9,3,8,2,10,-10,-6,-10,3,7,3,4,4,8,2,-5,10,-8,-1,-4,4,1,6,-3,7,5,-3,-9,10,6,-9,-4,-9,9,-5,-3,7,-2,-7,-2,-4,-2,7,5,1,1,2,-2,10,-3,2,-7,-9,-6,4,9,-6,-9,4,-10,5,8,-1,-8,-10,7,4], dtype = "uint16")#candidate|689|(315,)|const|uint16
call_687 = relay.TupleGetItem(func_307_call(relay.reshape(var_688.astype('uint16'), [15, 1, 7]), relay.reshape(const_689.astype('uint16'), [15, 3, 7]), ), 0)
call_690 = relay.TupleGetItem(func_310_call(relay.reshape(var_688.astype('uint16'), [15, 1, 7]), relay.reshape(const_689.astype('uint16'), [15, 3, 7]), ), 0)
output = relay.Tuple([uop_681,call_687,var_688,const_689,])
output2 = relay.Tuple([uop_681,call_690,var_688,const_689,])
func_691 = relay.Function([var_680,var_688,], output)
mod['func_691'] = func_691
mod = relay.transform.InferType()(mod)
mutated_mod['func_691'] = func_691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mutated_mod.get_global_var('func_691')
var_693 = relay.var("var_693", dtype = "float32", shape = (3, 15, 6))#candidate|693|(3, 15, 6)|var|float32
var_694 = relay.var("var_694", dtype = "uint16", shape = (1, 105))#candidate|694|(1, 105)|var|uint16
call_692 = func_691_call(var_693,var_694,)
output = call_692
func_695 = relay.Function([var_693,var_694,], output)
mutated_mod['func_695'] = func_695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_700 = relay.var("var_700", dtype = "float64", shape = (12, 15, 8))#candidate|700|(12, 15, 8)|var|float64
uop_701 = relay.log2(var_700.astype('float64')) # shape=(12, 15, 8)
bop_704 = relay.subtract(uop_701.astype('int8'), relay.reshape(var_700.astype('int8'), relay.shape_of(uop_701))) # shape=(12, 15, 8)
output = relay.Tuple([bop_704,])
output2 = relay.Tuple([bop_704,])
func_709 = relay.Function([var_700,], output)
mod['func_709'] = func_709
mod = relay.transform.InferType()(mod)
var_710 = relay.var("var_710", dtype = "float64", shape = (12, 15, 8))#candidate|710|(12, 15, 8)|var|float64
output = func_709(var_710)
func_711 = relay.Function([var_710], output)
mutated_mod['func_711'] = func_711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_715 = func_575_call()
call_716 = func_575_call()
output = call_715
output2 = call_716
func_719 = relay.Function([], output)
mod['func_719'] = func_719
mod = relay.transform.InferType()(mod)
mutated_mod['func_719'] = func_719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mutated_mod.get_global_var('func_719')
call_720 = func_719_call()
output = call_720
func_721 = relay.Function([], output)
mutated_mod['func_721'] = func_721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mod.get_global_var('func_638')
func_639_call = mutated_mod.get_global_var('func_639')
call_791 = relay.TupleGetItem(func_638_call(), 1)
call_792 = relay.TupleGetItem(func_639_call(), 1)
output = relay.Tuple([call_791,])
output2 = relay.Tuple([call_792,])
func_793 = relay.Function([], output)
mod['func_793'] = func_793
mod = relay.transform.InferType()(mod)
output = func_793()
func_794 = relay.Function([], output)
mutated_mod['func_794'] = func_794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_795 = func_575_call()
call_796 = func_575_call()
uop_807 = relay.erf(call_795.astype('float32')) # shape=(105,)
uop_809 = relay.erf(call_796.astype('float32')) # shape=(105,)
var_855 = relay.var("var_855", dtype = "uint16", shape = (105,))#candidate|855|(105,)|var|uint16
bop_856 = relay.floor_divide(call_795.astype('float32'), relay.reshape(var_855.astype('float32'), relay.shape_of(call_795))) # shape=(105,)
bop_859 = relay.floor_divide(call_796.astype('float32'), relay.reshape(var_855.astype('float32'), relay.shape_of(call_796))) # shape=(105,)
output = relay.Tuple([uop_807,bop_856,])
output2 = relay.Tuple([uop_809,bop_859,])
func_865 = relay.Function([var_855,], output)
mod['func_865'] = func_865
mod = relay.transform.InferType()(mod)
mutated_mod['func_865'] = func_865
mutated_mod = relay.transform.InferType()(mutated_mod)
var_866 = relay.var("var_866", dtype = "uint16", shape = (105,))#candidate|866|(105,)|var|uint16
func_865_call = mutated_mod.get_global_var('func_865')
call_867 = func_865_call(var_866)
output = call_867
func_868 = relay.Function([var_866], output)
mutated_mod['func_868'] = func_868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_870 = func_719_call()
call_871 = func_719_call()
output = call_870
output2 = call_871
func_891 = relay.Function([], output)
mod['func_891'] = func_891
mod = relay.transform.InferType()(mod)
output = func_891()
func_892 = relay.Function([], output)
mutated_mod['func_892'] = func_892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_891_call = mod.get_global_var('func_891')
func_892_call = mutated_mod.get_global_var('func_892')
call_916 = func_891_call()
call_917 = func_891_call()
output = call_916
output2 = call_917
func_927 = relay.Function([], output)
mod['func_927'] = func_927
mod = relay.transform.InferType()(mod)
mutated_mod['func_927'] = func_927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_927_call = mutated_mod.get_global_var('func_927')
call_928 = func_927_call()
output = call_928
func_929 = relay.Function([], output)
mutated_mod['func_929'] = func_929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mod.get_global_var('func_793')
func_794_call = mutated_mod.get_global_var('func_794')
call_941 = relay.TupleGetItem(func_793_call(), 0)
call_942 = relay.TupleGetItem(func_794_call(), 0)
uop_946 = relay.log(call_941.astype('float32')) # shape=(105,)
uop_948 = relay.log(call_942.astype('float32')) # shape=(105,)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_962 = func_575_call()
call_963 = func_575_call()
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
var_965 = relay.var("var_965", dtype = "float64", shape = (720, 2))#candidate|965|(720, 2)|var|float64
call_964 = relay.TupleGetItem(func_709_call(relay.reshape(var_965.astype('float64'), [12, 15, 8])), 0)
call_966 = relay.TupleGetItem(func_711_call(relay.reshape(var_965.astype('float64'), [12, 15, 8])), 0)
uop_978 = relay.cos(var_965.astype('float64')) # shape=(720, 2)
output = relay.Tuple([uop_946,call_962,call_964,uop_978,])
output2 = relay.Tuple([uop_948,call_963,call_966,uop_978,])
func_980 = relay.Function([var_965,], output)
mod['func_980'] = func_980
mod = relay.transform.InferType()(mod)
mutated_mod['func_980'] = func_980
mutated_mod = relay.transform.InferType()(mutated_mod)
var_981 = relay.var("var_981", dtype = "float64", shape = (720, 2))#candidate|981|(720, 2)|var|float64
func_980_call = mutated_mod.get_global_var('func_980')
call_982 = func_980_call(var_981)
output = call_982
func_983 = relay.Function([var_981], output)
mutated_mod['func_983'] = func_983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mod.get_global_var('func_793')
func_794_call = mutated_mod.get_global_var('func_794')
call_1095 = relay.TupleGetItem(func_793_call(), 0)
call_1096 = relay.TupleGetItem(func_794_call(), 0)
output = call_1095
output2 = call_1096
func_1097 = relay.Function([], output)
mod['func_1097'] = func_1097
mod = relay.transform.InferType()(mod)
output = func_1097()
func_1098 = relay.Function([], output)
mutated_mod['func_1098'] = func_1098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1128 = relay.var("var_1128", dtype = "bool", shape = (6, 16, 9))#candidate|1128|(6, 16, 9)|var|bool
const_1129 = relay.const([[[False,True,True,True,False,False,False,True,False],[True,False,True,True,False,False,False,True,True],[False,False,True,True,False,True,True,True,False],[False,True,True,False,True,False,True,False,False],[False,False,True,False,False,False,True,True,False],[True,False,False,True,False,False,False,True,False],[True,False,True,True,True,False,False,True,True],[False,True,False,True,True,False,False,True,False],[False,True,False,True,False,False,True,True,False],[True,False,True,True,True,True,False,True,False],[False,True,False,True,False,True,True,True,False],[False,True,True,False,False,False,False,True,True],[False,False,False,False,True,False,True,False,False],[True,False,True,True,False,False,True,True,False],[False,True,True,False,True,True,False,True,True],[False,False,False,True,False,False,False,True,True]],[[False,False,True,False,True,True,True,True,True],[False,False,False,False,True,True,False,True,False],[True,True,False,False,False,False,False,True,False],[False,True,True,True,False,False,False,False,True],[True,False,False,False,False,True,False,False,False],[False,False,True,False,True,True,False,True,True],[False,True,False,True,True,False,False,False,False],[False,False,False,False,True,False,False,True,False],[True,False,True,True,False,True,True,False,True],[False,True,False,True,True,False,True,False,True],[True,True,False,True,True,False,False,True,False],[False,False,True,True,True,True,False,True,True],[True,False,False,False,False,True,True,True,False],[True,False,True,False,False,False,False,True,True],[True,True,True,True,False,True,False,True,False],[False,True,True,True,False,True,True,True,True]],[[False,False,False,True,True,True,False,True,True],[False,False,False,True,True,False,False,False,False],[True,False,True,False,False,False,True,False,False],[True,True,True,False,False,True,True,True,False],[False,True,False,True,True,False,True,False,True],[True,True,True,True,False,True,False,False,False],[False,False,False,True,True,True,False,True,True],[False,False,False,False,False,True,False,True,False],[False,True,True,True,False,False,False,False,False],[False,False,True,False,True,True,False,False,False],[True,False,True,True,False,False,True,True,False],[True,True,False,True,False,True,False,True,True],[False,False,True,True,False,False,False,False,True],[True,False,True,True,True,True,False,False,False],[False,False,True,True,True,False,True,False,False],[False,True,False,True,True,False,True,False,False]],[[True,False,False,False,True,False,True,False,True],[False,True,False,False,True,False,True,False,True],[False,True,True,False,True,False,False,True,False],[False,False,False,False,True,True,False,True,False],[False,False,True,False,False,False,False,True,True],[False,False,False,True,False,True,False,True,True],[True,True,False,True,False,False,True,False,True],[False,True,False,True,True,False,False,True,False],[False,True,True,True,True,False,True,False,False],[True,True,True,False,False,True,False,True,True],[False,False,True,True,True,False,True,False,False],[True,False,True,True,False,True,True,True,False],[True,True,True,True,False,False,True,False,False],[False,False,True,True,False,True,False,True,False],[True,False,False,True,True,False,False,False,False],[True,True,False,False,False,True,True,False,True]],[[True,True,True,True,True,True,False,False,True],[True,False,False,False,True,False,False,False,True],[True,True,True,True,False,True,True,False,True],[False,True,True,True,False,False,False,True,True],[True,True,True,False,True,False,False,True,True],[False,True,False,True,False,True,True,False,True],[False,True,False,True,False,True,True,True,False],[True,False,True,True,True,True,False,False,False],[False,False,True,False,True,False,False,False,True],[True,True,True,False,True,False,False,True,False],[False,False,False,False,True,False,True,False,True],[False,True,True,False,True,False,True,True,True],[False,True,True,True,False,True,False,True,False],[False,True,True,True,True,True,True,True,True],[True,True,True,False,True,False,False,False,False],[False,True,True,True,True,True,False,False,True]],[[True,False,False,False,True,False,True,False,True],[True,True,True,False,False,False,True,False,True],[False,False,True,False,False,True,True,True,False],[False,False,True,False,True,True,False,True,False],[False,True,False,False,False,True,True,False,True],[True,True,False,False,True,False,False,True,True],[True,True,False,True,True,False,False,True,False],[False,False,True,False,False,False,True,False,False],[False,True,False,False,False,False,False,True,True],[False,True,True,True,False,False,False,True,True],[False,False,True,False,False,True,False,False,True],[False,True,False,True,False,True,True,False,False],[True,False,True,True,False,False,False,False,False],[False,False,True,True,False,True,False,True,True],[True,True,False,True,True,True,True,False,True],[False,False,True,False,True,True,True,False,False]]], dtype = "bool")#candidate|1129|(6, 16, 9)|const|bool
bop_1130 = relay.logical_or(var_1128.astype('bool'), relay.reshape(const_1129.astype('bool'), relay.shape_of(var_1128))) # shape=(6, 16, 9)
uop_1139 = relay.acosh(const_1129.astype('float64')) # shape=(6, 16, 9)
uop_1141 = relay.asin(uop_1139.astype('float64')) # shape=(6, 16, 9)
output = relay.Tuple([bop_1130,uop_1141,])
output2 = relay.Tuple([bop_1130,uop_1141,])
func_1143 = relay.Function([var_1128,], output)
mod['func_1143'] = func_1143
mod = relay.transform.InferType()(mod)
var_1144 = relay.var("var_1144", dtype = "bool", shape = (6, 16, 9))#candidate|1144|(6, 16, 9)|var|bool
output = func_1143(var_1144)
func_1145 = relay.Function([var_1144], output)
mutated_mod['func_1145'] = func_1145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_1171 = relay.TupleGetItem(func_537_call(), 3)
call_1172 = relay.TupleGetItem(func_538_call(), 3)
uop_1175 = relay.sigmoid(call_1171.astype('float32')) # shape=(315,)
uop_1177 = relay.sigmoid(call_1172.astype('float32')) # shape=(315,)
output = relay.Tuple([uop_1175,])
output2 = relay.Tuple([uop_1177,])
func_1186 = relay.Function([], output)
mod['func_1186'] = func_1186
mod = relay.transform.InferType()(mod)
mutated_mod['func_1186'] = func_1186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mutated_mod.get_global_var('func_1186')
call_1187 = func_1186_call()
output = call_1187
func_1188 = relay.Function([], output)
mutated_mod['func_1188'] = func_1188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_1191 = relay.TupleGetItem(func_537_call(), 3)
call_1192 = relay.TupleGetItem(func_538_call(), 3)
output = call_1191
output2 = call_1192
func_1195 = relay.Function([], output)
mod['func_1195'] = func_1195
mod = relay.transform.InferType()(mod)
output = func_1195()
func_1196 = relay.Function([], output)
mutated_mod['func_1196'] = func_1196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_1217 = func_575_call()
call_1218 = func_575_call()
output = call_1217
output2 = call_1218
func_1232 = relay.Function([], output)
mod['func_1232'] = func_1232
mod = relay.transform.InferType()(mod)
mutated_mod['func_1232'] = func_1232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mutated_mod.get_global_var('func_1232')
call_1233 = func_1232_call()
output = call_1233
func_1234 = relay.Function([], output)
mutated_mod['func_1234'] = func_1234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_1250 = func_927_call()
call_1251 = func_927_call()
output = relay.Tuple([call_1250,])
output2 = relay.Tuple([call_1251,])
func_1286 = relay.Function([], output)
mod['func_1286'] = func_1286
mod = relay.transform.InferType()(mod)
mutated_mod['func_1286'] = func_1286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mutated_mod.get_global_var('func_1286')
call_1287 = func_1286_call()
output = call_1287
func_1288 = relay.Function([], output)
mutated_mod['func_1288'] = func_1288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_1295 = func_719_call()
call_1296 = func_719_call()
func_1143_call = mod.get_global_var('func_1143')
func_1145_call = mutated_mod.get_global_var('func_1145')
var_1301 = relay.var("var_1301", dtype = "bool", shape = (432, 2))#candidate|1301|(432, 2)|var|bool
call_1300 = relay.TupleGetItem(func_1143_call(relay.reshape(var_1301.astype('bool'), [6, 16, 9])), 1)
call_1302 = relay.TupleGetItem(func_1145_call(relay.reshape(var_1301.astype('bool'), [6, 16, 9])), 1)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_1312 = relay.TupleGetItem(func_537_call(), 4)
call_1313 = relay.TupleGetItem(func_538_call(), 4)
output = relay.Tuple([call_1295,call_1300,var_1301,call_1312,])
output2 = relay.Tuple([call_1296,call_1302,var_1301,call_1313,])
func_1318 = relay.Function([var_1301,], output)
mod['func_1318'] = func_1318
mod = relay.transform.InferType()(mod)
var_1319 = relay.var("var_1319", dtype = "bool", shape = (432, 2))#candidate|1319|(432, 2)|var|bool
output = func_1318(var_1319)
func_1320 = relay.Function([var_1319], output)
mutated_mod['func_1320'] = func_1320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_1324 = relay.TupleGetItem(func_608_call(), 0)
call_1325 = relay.TupleGetItem(func_609_call(), 0)
uop_1331 = relay.sqrt(call_1324.astype('float64')) # shape=(105,)
uop_1333 = relay.sqrt(call_1325.astype('float64')) # shape=(105,)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1339 = func_1097_call()
call_1340 = func_1097_call()
func_1286_call = mod.get_global_var('func_1286')
func_1288_call = mutated_mod.get_global_var('func_1288')
call_1350 = relay.TupleGetItem(func_1286_call(), 0)
call_1351 = relay.TupleGetItem(func_1288_call(), 0)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_1354 = func_1232_call()
call_1355 = func_1232_call()
output = relay.Tuple([uop_1331,call_1339,call_1350,call_1354,])
output2 = relay.Tuple([uop_1333,call_1340,call_1351,call_1355,])
func_1359 = relay.Function([], output)
mod['func_1359'] = func_1359
mod = relay.transform.InferType()(mod)
mutated_mod['func_1359'] = func_1359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1359_call = mutated_mod.get_global_var('func_1359')
call_1360 = func_1359_call()
output = call_1360
func_1361 = relay.Function([], output)
mutated_mod['func_1361'] = func_1361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_1379 = relay.TupleGetItem(func_1186_call(), 0)
call_1380 = relay.TupleGetItem(func_1188_call(), 0)
output = relay.Tuple([call_1379,])
output2 = relay.Tuple([call_1380,])
func_1394 = relay.Function([], output)
mod['func_1394'] = func_1394
mod = relay.transform.InferType()(mod)
mutated_mod['func_1394'] = func_1394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mutated_mod.get_global_var('func_1394')
call_1395 = func_1394_call()
output = call_1395
func_1396 = relay.Function([], output)
mutated_mod['func_1396'] = func_1396
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1419 = relay.var("var_1419", dtype = "bool", shape = (9, 16))#candidate|1419|(9, 16)|var|bool
var_1420 = relay.var("var_1420", dtype = "bool", shape = (9, 16))#candidate|1420|(9, 16)|var|bool
bop_1421 = relay.logical_or(var_1419.astype('bool'), relay.reshape(var_1420.astype('bool'), relay.shape_of(var_1419))) # shape=(9, 16)
output = bop_1421
output2 = bop_1421
func_1438 = relay.Function([var_1419,var_1420,], output)
mod['func_1438'] = func_1438
mod = relay.transform.InferType()(mod)
var_1439 = relay.var("var_1439", dtype = "bool", shape = (9, 16))#candidate|1439|(9, 16)|var|bool
var_1440 = relay.var("var_1440", dtype = "bool", shape = (9, 16))#candidate|1440|(9, 16)|var|bool
output = func_1438(var_1439,var_1440,)
func_1441 = relay.Function([var_1439,var_1440,], output)
mutated_mod['func_1441'] = func_1441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1195_call = mod.get_global_var('func_1195')
func_1196_call = mutated_mod.get_global_var('func_1196')
call_1479 = func_1195_call()
call_1480 = func_1195_call()
var_1492 = relay.var("var_1492", dtype = "uint16", shape = (315,))#candidate|1492|(315,)|var|uint16
bop_1493 = relay.divide(call_1479.astype('float32'), relay.reshape(var_1492.astype('float32'), relay.shape_of(call_1479))) # shape=(315,)
bop_1496 = relay.divide(call_1480.astype('float32'), relay.reshape(var_1492.astype('float32'), relay.shape_of(call_1480))) # shape=(315,)
output = bop_1493
output2 = bop_1496
func_1500 = relay.Function([var_1492,], output)
mod['func_1500'] = func_1500
mod = relay.transform.InferType()(mod)
mutated_mod['func_1500'] = func_1500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1501 = relay.var("var_1501", dtype = "uint16", shape = (315,))#candidate|1501|(315,)|var|uint16
func_1500_call = mutated_mod.get_global_var('func_1500')
call_1502 = func_1500_call(var_1501)
output = call_1502
func_1503 = relay.Function([var_1501], output)
mutated_mod['func_1503'] = func_1503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_1530 = func_927_call()
call_1531 = func_927_call()
output = relay.Tuple([call_1530,])
output2 = relay.Tuple([call_1531,])
func_1532 = relay.Function([], output)
mod['func_1532'] = func_1532
mod = relay.transform.InferType()(mod)
output = func_1532()
func_1533 = relay.Function([], output)
mutated_mod['func_1533'] = func_1533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1359_call = mod.get_global_var('func_1359')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_1548 = relay.TupleGetItem(func_1359_call(), 3)
call_1549 = relay.TupleGetItem(func_1361_call(), 3)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
var_1557 = relay.var("var_1557", dtype = "float64", shape = (1440,))#candidate|1557|(1440,)|var|float64
call_1556 = relay.TupleGetItem(func_709_call(relay.reshape(var_1557.astype('float64'), [12, 15, 8])), 0)
call_1558 = relay.TupleGetItem(func_711_call(relay.reshape(var_1557.astype('float64'), [12, 15, 8])), 0)
output = relay.Tuple([call_1548,call_1556,var_1557,])
output2 = relay.Tuple([call_1549,call_1558,var_1557,])
func_1559 = relay.Function([var_1557,], output)
mod['func_1559'] = func_1559
mod = relay.transform.InferType()(mod)
mutated_mod['func_1559'] = func_1559
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1560 = relay.var("var_1560", dtype = "float64", shape = (1440,))#candidate|1560|(1440,)|var|float64
func_1559_call = mutated_mod.get_global_var('func_1559')
call_1561 = func_1559_call(var_1560)
output = call_1561
func_1562 = relay.Function([var_1560], output)
mutated_mod['func_1562'] = func_1562
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1578 = relay.const([[[3,-2,1,4,3,-10,-10,-3,4],[-10,10,-8,7,7,9,3,-8,-3],[-1,4,6,-4,-8,1,-1,-1,-8],[-5,4,-1,2,3,1,8,6,3],[-4,8,-3,4,-1,4,-5,2,-1]],[[-10,-9,2,2,9,1,-10,10,-5],[-7,9,-5,9,2,-7,6,-7,-4],[-4,-10,-4,6,4,-2,-1,1,10],[2,5,-1,-8,-2,4,3,-2,-1],[-4,10,5,8,-2,-7,-4,-10,-3]],[[-3,-1,-6,-3,-1,4,1,8,-7],[-1,8,-3,-6,4,-5,-8,-7,-5],[2,-6,1,4,9,3,-3,-10,-10],[6,1,1,-6,-4,7,-10,7,3],[-9,2,-7,5,-9,-2,9,4,-7]],[[-5,3,-10,1,3,-7,8,3,3],[4,1,2,-4,-3,-10,-1,-7,-4],[-9,6,-3,-6,6,-2,1,-4,1],[8,-8,4,-3,-1,-1,7,10,-10],[4,-5,-9,-9,4,5,-1,3,-5]],[[-7,1,-1,3,-2,1,7,2,-6],[-10,1,10,9,10,3,6,6,-8],[-2,4,3,8,1,-3,-10,3,4],[7,9,7,3,-1,-3,-7,-9,6],[6,-5,3,7,-8,-5,6,-10,-1]],[[4,-10,-4,-6,-5,2,1,7,-7],[2,6,-4,6,4,2,3,-1,5],[-4,-4,7,10,4,-2,10,4,-7],[6,8,-1,7,-10,-5,-2,5,-7],[2,10,7,-6,9,-10,10,-2,-7]],[[-1,-5,3,-8,-6,-2,5,2,-9],[-7,-3,-7,-3,-10,7,5,4,-1],[-7,-5,-1,-10,1,10,-9,7,3],[7,-2,10,6,7,5,-8,-6,9],[-2,-4,9,4,-2,9,6,-3,3]]], dtype = "uint32")#candidate|1578|(7, 5, 9)|const|uint32
var_1579 = relay.var("var_1579", dtype = "uint32", shape = (7, 5, 9))#candidate|1579|(7, 5, 9)|var|uint32
bop_1580 = relay.maximum(const_1578.astype('uint32'), relay.reshape(var_1579.astype('uint32'), relay.shape_of(const_1578))) # shape=(7, 5, 9)
bop_1584 = relay.bitwise_xor(bop_1580.astype('uint16'), relay.reshape(const_1578.astype('uint16'), relay.shape_of(bop_1580))) # shape=(7, 5, 9)
bop_1611 = relay.power(bop_1584.astype('float32'), relay.reshape(var_1579.astype('float32'), relay.shape_of(bop_1584))) # shape=(7, 5, 9)
output = relay.Tuple([bop_1611,])
output2 = relay.Tuple([bop_1611,])
func_1617 = relay.Function([var_1579,], output)
mod['func_1617'] = func_1617
mod = relay.transform.InferType()(mod)
mutated_mod['func_1617'] = func_1617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1618 = relay.var("var_1618", dtype = "uint32", shape = (7, 5, 9))#candidate|1618|(7, 5, 9)|var|uint32
func_1617_call = mutated_mod.get_global_var('func_1617')
call_1619 = func_1617_call(var_1618)
output = call_1619
func_1620 = relay.Function([var_1618], output)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_1673 = func_927_call()
call_1674 = func_927_call()
output = relay.Tuple([call_1673,])
output2 = relay.Tuple([call_1674,])
func_1685 = relay.Function([], output)
mod['func_1685'] = func_1685
mod = relay.transform.InferType()(mod)
mutated_mod['func_1685'] = func_1685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1685_call = mutated_mod.get_global_var('func_1685')
call_1686 = func_1685_call()
output = call_1686
func_1687 = relay.Function([], output)
mutated_mod['func_1687'] = func_1687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_1690 = relay.TupleGetItem(func_608_call(), 1)
call_1691 = relay.TupleGetItem(func_609_call(), 1)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
const_1712 = relay.const([2.251594,2.244607,-7.138872,-6.377787,7.964465,1.146564,-2.510675,9.673798,4.228420,-3.110985,1.230943,-9.026283,-0.463967,7.252848,0.362684,2.532741,3.926317,5.839088,-7.951829,7.885245,9.558973,1.765154,-0.215505,1.798678,-0.266099,-3.682837,-7.090931,2.187525,2.030282,6.252446,9.108007,6.533608,5.455584,3.404767,-4.108423,-3.361414,0.307780,0.588007,-7.588529,-8.876389,-7.683493,-6.795325,7.777956,4.286983,-8.254827,3.043098,-6.994733,3.126881,7.740247,0.389222,7.067268,-8.841914,-4.916649,-5.874689,-5.031140,6.417707,1.690491,-0.618907,8.926461,5.995700,-7.927540,-8.276117,8.421717,-9.196057,-1.014529,4.671664,2.240518,-3.710799,3.834387,-3.231965,0.926122,1.859077,8.771610,4.034454,7.867621,0.757186,-6.905029,-4.036932,6.444086,-5.868727,7.496103,0.043441,0.876037,-5.177616,-1.701554,5.792145,-0.807554,-7.464427,-9.762919,0.483164,6.516189,8.703259,-2.281569,1.496942,-8.886629,9.802052,2.399231,4.307536,-5.524502,-7.021693,-4.535170,7.895590,-4.959245,1.160388,0.097014,-9.537748,8.231398,-6.272661,-8.497179,8.298529,-2.004116,-5.634170,8.211319,-8.104922,6.258616,-0.809002,-3.288806,-6.271705,9.007654,0.411427,-2.331194,0.630278,4.678886,9.529202,-4.173368,5.388979,0.474660,-4.729601,0.834933,4.709784,9.451108,-0.573723,8.777833,-6.448075,-7.649777,9.875776,-2.834957,-2.488621,1.286037,7.274532,-2.111279,-1.950056,-1.338290,-9.074439,2.459396,-2.146135,7.580683,6.126671,3.929408,-6.531298,1.056015,7.268365,-7.016744,-5.313380,0.737566,0.788385,-1.778973,-3.845994,7.800977,-7.198684,-4.551662,5.170736,5.439871,-8.689359,0.337282,5.677305,-0.002565,-5.379623,-5.175172,-9.400823,-5.761245,-4.829006,0.253996,7.196227,8.267361,-3.852272,-8.218375,-4.462868,-0.190913,-3.211138,9.180940,-2.536447,-5.819392,-1.607216,7.282986,2.735393,0.926149,-0.789647,-7.959026,1.030653,4.617833,6.868860,2.189231,-9.153422,-6.359485,3.666963,-1.255949,9.477520,-5.763374,1.176266,5.645697,4.189587,-4.470185,4.241711,4.583916,1.898482,-0.638065,-1.012281,-7.858052,0.574238,-9.192936,-3.202311,9.498952,9.913414,6.742922,9.903245,3.191842,2.228674,7.183822,-2.818884,1.781939,3.336802,-5.962569,-1.369412,-0.220767,0.693588,-2.405428,0.895561,-5.639277,-0.576606,-9.535849,-7.890048,-7.721289,2.525961,-6.583703,7.020362,6.402845,-5.405841,-1.913337,-8.969371,-1.383715,1.722984,3.026519,-3.370850,-3.867317,-9.495399,2.871016,-6.192043,-3.517670,9.213638,-7.735626,5.824975,2.869297,9.541574,-7.474338,0.528871,-9.049000,1.579908,5.710090,7.662165,-1.378127,-1.898117,-0.308940,-5.135755,0.879545,1.125455,-1.470331,8.457283,-5.170508,8.585635,5.625375,-2.239816,-9.840698,6.262838,0.665601,0.954509,-2.314821,4.780057,-5.258232,-3.520246,9.335985,2.186762,-9.010508,-8.219519,-8.930802,8.819003,-0.253670,4.867465,6.712937,-2.775458,2.756771,2.914043,-7.222963,-7.776894,-5.462335,-2.617168,-6.535037,8.828593,-0.026402,-9.776130,6.861159,-9.116746,1.320419,-9.154202,1.387868,2.040964,-6.468846,-5.518439,-2.301229,-3.638108,6.169863,-0.489097,-7.321739,-7.565812,6.111007,6.727788,-3.105869,-3.254505,6.462432,7.764381,-2.165945,2.328201,2.276600,0.740628,-5.269217,-1.735211,-5.678316,-0.645641,-6.033212,3.242079,5.062956,-9.621812,7.914181,4.429521,-6.235735,0.635047,1.878639,8.671310,-9.171047,-1.613442,-1.137440,9.147275,-6.424249,-0.293036,-5.425053,-1.040153,-7.338512,-0.398941,-4.530396,3.726399,-0.906681,5.178781,9.406127,-6.845173,9.107110,4.110332,5.243571,-1.901701,-4.726157,-1.438949,-1.901619,-9.412449,9.542373,-9.205270,-1.531501,-2.692152,-9.885742,-5.795914,2.455979,-5.265260,-9.443032,-9.184168,-6.545615,7.356586,0.849041,2.193207,-4.763335,8.430342,-9.130397,0.395251,0.459370,5.842735,4.876072,1.797549,-7.273890,8.943699,2.345251,-7.478357,-3.899955,-1.334841,2.317763,-5.561551,4.793297,-1.556334,1.952777,-7.081949,7.199450,1.549127,-9.125986,6.632464,-8.799505,9.686603,2.995358,2.383960,6.490822,7.403176,6.197513,-1.081082,6.340122,1.017503,3.830975,8.192360,1.487760,8.880590,-5.732145,8.570943,-8.490286,-2.711064,-0.998854,5.435240,-5.433534,5.428183,-8.900125,-3.620759,-7.169077,5.717480,-7.853049,-6.491527,4.550074,7.325344,7.283743,-1.740418,0.733190,7.993457,-4.019156,2.059805,3.542786,-4.730799,-7.044602,-1.855646,-6.767885,-2.645921,-0.291643,5.204139,1.998387,8.686602,8.590583,-0.660349,4.753312,-7.932254,-6.429875,-9.165524,-7.660533,-0.619602,1.757113,7.041173,-6.373548,-3.487123,0.492691,-6.014931,-5.742761,4.378928,5.825744,-7.445754,5.497529,-1.448244,-0.114756,1.306648,2.528278,-5.838811,-9.826430,3.293070,6.274660,-7.390256,3.457204,6.055852,-4.336519,2.628208,-7.501832,-4.287938,-6.998948,-5.755779,7.394011,-1.306796,5.486340,-1.197643,-1.206055,-9.005381,2.987919,-2.183898,6.479069,7.526065,-7.780919,4.504482,-8.266723,-9.362155,-5.172056,-3.047386,2.815495,-9.533500,2.211211,-1.357388,-3.305171,9.240747,2.404909,-3.688727,-0.611065,5.827084,-3.547252,0.378264,-3.805934,-0.553114,-2.965914,2.359367,4.271714,-9.915847,-7.771445,-1.715784,4.946710,-5.915865,-4.736055,6.027668,-5.659813,1.645777,4.049598,-8.979401,3.365524,-2.698878,9.468131,8.074222,-5.148552,3.833915,-4.727694,9.157244,2.592416,3.508511,7.397878,-3.490458,8.511383,-2.562791,4.958311,-5.976287,4.576332,-2.552667,-6.739693,4.195976,-3.229422,7.917497,7.839368,-8.254806,0.014450,-4.200966,0.711497,-3.071707,-9.228090,3.569491,5.460129,-7.818971,0.979124,2.096517,-9.999418,-3.923024,5.118084,-8.128507,-1.874036,-9.948606,-6.154602,-4.540963,7.148979,-9.338963,-1.368119,8.984439,7.747640,-7.341286,0.636458,4.574229,5.209529,-6.045589,2.486053,3.277172,4.990016,8.112638,-0.476041,2.304254,4.893629,7.295027,-0.140810,1.328119,8.123402,-3.507827,-3.553448,-1.666892,3.884661,-1.426681,8.030844,-9.064445,0.035191,-4.725069,-3.679427,-3.811356,2.886445,3.967512,-4.020626,-1.794789,-1.586745,-2.622287,-0.948645,-1.813970,7.658787,-3.249567,-6.668273,-5.998908,0.684570,4.358981,-7.187727,3.465218,-5.666714,9.566193,7.005747,-1.861781,-0.558782,-5.614125,4.874565,-6.602252,-7.492841,-8.750637,-1.772419,-7.712832,7.480566,1.504816,8.840580,-7.258618,9.654257,9.203376,2.307476,-3.743100,-5.778875,-5.233794,-9.760800,1.062205,6.559996,8.429890,-1.069395,6.061294,-6.582783,3.313118,5.730265,9.888166,-7.821466,-1.697427,-7.142579,4.006989,0.136676,-9.555500,9.364348,-4.669319,5.284258,-2.424351,-3.717808,-2.783054,-8.652610,-4.138276,1.419641,-3.633952,-0.696007,2.676856,8.085966,-2.294596,-3.047534,-6.763206,-2.695176,-7.838393,6.062832,7.794951,7.341847,-2.913320,7.952318,9.547735,-7.226542,-1.946153,-7.919037,1.488720,8.989142,9.910399,-5.944939,9.554131,-4.741307,4.775720,-9.828881,6.347215,-2.337880,6.460157,2.570497,-3.580699,-9.739227,-5.777048,-2.383447,-9.905960,2.399156,1.360541,-6.777932,-3.533835,-2.211183,-3.820737,-3.860922,-1.986186,9.719849,7.638987,6.962095,-6.784808,-9.903572,-8.115067,-3.027148,-4.868768,-0.871495,2.257927,-6.394049,-5.315504,4.445789,5.745804,-6.961775,-3.487735,8.287626,-8.316720,5.397305,-2.166779,-5.539846,-4.315762,-1.993865,-8.180469,-0.634704,4.869070,-7.897232,-6.321241,-5.812958,4.148019,1.862237,-7.569120,2.012183,7.334526,1.609630,9.874377,6.447592,-0.375175,-2.978195,-5.807263,-8.357703,-0.447112,8.245090,2.248685,-7.313282,3.446805,-9.900003,1.651596,-2.205500,6.236826,-1.038009,7.743778,-9.940079,3.495532,7.910314,-5.269906,0.488637,-8.144615,4.214247,-3.807416,-5.005681,3.443069,5.388245,3.095751,-8.809324,7.966492,0.252528,-2.956564,-7.587617,-8.960954,1.496811,-6.801454,0.470215,-6.029858,-3.725411,1.053402,-9.402937,8.468402,6.257335,3.911030,3.890494,-2.640658,-8.046464,3.335047,0.061523,-1.750266,-4.720589,2.688311,0.044614,-0.897995,5.991567,-6.401106,-7.666036,3.340727,-9.548211,5.171389,-6.812038,-0.044465,-1.270524,7.386590,-4.798958,6.849290,-1.770906,-4.475156,-1.601334,9.211389,-2.935572,8.157554,-0.915735,-1.015936,5.562219,-8.271171,-7.258589,-8.211793,-3.192803,-4.436013,5.618804,3.146014,-5.440664,1.998830,-2.618577,-5.080792,3.099099,-1.411484,0.603634,-3.728761,-5.237104,-8.319425,-1.096317,-9.882179,-3.926341,3.092265,-8.965975,-5.081811,-6.276517,0.298345,-4.598724,-9.116008,6.908265,8.819999,1.246349,2.302283,5.101110,-0.467669,6.949346,-3.702514,8.588694,3.727319,7.643994,0.388323,-4.144478,-8.615114,-8.745243,-0.887561,2.066726,-6.128816,6.518959,5.508264,9.154607,-6.430624,-4.397530,2.363168,-8.019098,6.548363,-7.261665,-3.716226,2.387975,5.541542,8.902597,6.774269,-4.599553,7.017086,4.396229,-1.632343,1.881792,2.165893,1.193574,7.385829,-0.556699,7.431932,3.136528,4.189189,7.439527,1.041862,-1.687381,3.251797,-3.948175,-6.639509,6.732785,3.804270,-9.203907,-2.409505,0.162969,9.748999,-7.945284,-3.728315,-8.267913,-9.740811,-0.989048,-6.903712,-1.897588,4.269409,5.320071,0.899713,-5.128384,2.268357,7.523494,6.810343,5.526724,-8.071319,0.052234,-0.845793,-1.653775,0.475595,-9.881433,9.029692,-4.617633,1.889567,5.657845,-4.709519,9.576102,-0.415726,-2.294548,1.519349,-0.592416,7.676757,-4.191473,-8.809338,4.318620,-5.321701,8.375279,-7.892549,-5.627475,5.828936,-1.090610,-0.878137,3.068126,2.754701,-3.767577,-0.083816,-1.978208,-7.874951,5.500928,-9.374985,0.996942,-6.528464,-4.647460,-5.796178,-7.272295,-5.985338,7.608043,4.713512,4.767568,-0.066097,7.749422,5.606535,4.122859,3.323725,-5.167769,1.687532,-9.057092,-1.996228,-4.678023,2.516538,0.456499,-4.642060,-2.553836,7.775481,-6.355673,1.041414,-9.438737,8.457334,2.297859,-8.133225,-3.600775,2.685584,8.356969,-5.322487,-4.462689,2.597288,1.366777,-6.440456,3.195695,-3.772747,-1.674762,5.160386,-5.258085,-4.716843,9.580386,5.894708,-3.460782,-6.778074,-4.041089,4.537648,3.174781,-4.565607,-3.312779,-0.755778,3.487298,1.118236,5.488418,-6.320608,-5.686229,2.499759,-1.475220,5.559690,2.665184,-6.910301,-7.097593,-7.642286,-3.399442,1.993355,5.354602,-1.794838,-2.624018,-2.280206,8.501606,9.457832,5.629158,0.868823,3.764719,-3.647883,5.388386,-0.202605,2.746350,8.688633,-4.487719,-3.002256,-7.321675,-7.205361,4.316590,-9.749561,0.477172,-9.596026,-0.561912,-7.254059,-3.182733,-4.745984,-8.446895,-5.346442,8.784894,2.888916,-3.178789,-1.123033,7.262148,9.891404,7.945771,2.511154,3.429583,-7.374176,0.106493,9.736884,9.721834,8.968753,-9.876124,2.777993,2.167694,4.948159,7.676917,3.193189,-0.947710,7.485732,-2.130173,7.897563,-1.949964,-1.279601,-5.903227,9.248650,8.939166,8.357780,-0.618104,-9.925623,-9.417920,2.243557,2.604236,-9.862483,5.661305,3.898352,-5.874079,3.824918,-2.887359,-5.079015,8.719521,1.908504,6.071029,6.789733,7.297096,9.065129,3.826269,9.025072,0.245992,0.313327,1.455591,1.797028,8.302611,-2.177856,-3.418014,-8.413345,6.727977,-5.627220,9.700704,-8.755657,0.151213,-7.336200,6.312438,0.249656,9.088793,8.374726,-2.415772,-4.860195,-4.131643,9.020023,8.171411,-7.495059,4.508385,4.226736,-5.539274,-6.875178,-0.473913,0.299655,-0.230712,-1.818942,4.326905,1.335521,-1.851679,7.320884,-5.251229,6.657875,-7.875926,-3.146112,8.084455,-6.854378,-8.699241,1.874300,6.883931,-6.193604,-6.636677,4.522570,-8.233489,5.151183,-6.939897,8.061530,3.283189,6.022648,4.215784,-4.665558,0.734183,-6.250985,0.092070,-5.208344,-3.191582,-6.876659,-1.932674,-3.115349,-7.762652,8.775542,-3.940022,-3.203080,-1.738184,-7.435341,1.777006,-9.831702,6.309470,-7.215444,-5.106336,-7.118988,4.713197,2.064751,-0.428717,5.218081,5.047031,-9.367729,3.569464,-2.226012,-4.687750,7.261262,1.302294,-6.480670,1.184896,1.175199,-4.065311,-4.774539,-8.655292,2.155072,-4.932786,-8.524524,8.992943,2.006201,1.061889,-3.010295,-3.052572,1.397897,3.766437,0.153842,6.572669,0.396684,-4.964330,6.998279,3.430693,9.080889,2.637716,-2.519871,-1.516914,-2.004546,7.129487,6.018534,-7.404372,7.183697,3.004925,-7.019828,9.013554,-8.519485,-9.712739,-8.038790,-9.786467,1.877439,4.309702,-3.549097,5.988204,9.522298,-0.603004,3.290969,-8.623380,-7.359139,5.790078,-4.980740,-8.335362,-4.849463,-1.734746,4.439251,-1.157571,2.129624,-5.278949,-3.215174,-1.653930,-3.112020,-8.963143,0.149939,-3.622301,-8.470170,0.264325,-7.487473,0.260599,-1.357676,7.898065,-9.298616,-3.615713,-7.649146,-6.197311,-3.778197,-8.659079,9.377094,-7.813952,2.778155,-0.842718,-8.257475,-6.771633,-2.774526,7.850020,-6.316377,-5.118418,1.284214,-7.406093,9.893314,-3.122725,1.159125,-2.629269,0.396348,4.035232,9.101593,3.263780,3.384633,-7.963099,3.806840,-5.890340,-6.502258,5.377178,7.159964,5.766711,-8.364074,4.151384,5.802213,-3.300955,-7.192547,5.037738,9.538655,-6.190891,6.750413,-2.223242,-3.757327,-2.356031,2.172999,-3.046489,4.378976,7.495397,9.540251,4.980005,-8.178888,-8.824124,8.195988,-3.227459,-5.673996,-6.509884,8.532582,-0.547453,7.867859,3.245585,-7.980859,-5.158222,9.914288,4.605016,-5.858466,6.862462,-3.428401,4.590104,-2.333201,0.072334,-8.238895,-0.402227,-1.556603,-4.117580,9.320578,8.824219,2.823406,1.080901,1.454176,-2.480816,3.385675,5.585007,5.091849,7.603779,-0.264488,-1.168993,-7.938633,9.162163,1.869085,3.209423,2.426040,4.595830,-1.370404,4.749015,1.076341,9.676118,-4.042314,0.048275,9.897302,6.876733,8.498170,2.050372,-7.928280,-2.343791,-1.746063,-2.078712,-7.355082,-5.609667,-6.008241,9.725269,9.870281,-7.402856,2.054478,4.449134,-3.409200,-5.711021,-5.102531,-9.984982,-8.858375,9.094924,-4.885568,-5.876612,1.418144,9.070080,5.535877,7.077021,6.348333,-0.720253,3.945557,8.375147,-6.921085,8.997722,0.468181,6.476006,7.724184,-9.680221,-3.293866,-3.887318,-7.010660,9.520583,-6.680900,-3.861725,-2.920922,-0.464840,5.086449,3.373833,-2.505473,-7.713265,-9.107321,4.099718,-8.923083,7.660390,7.455536,-1.775316,1.514621,3.873443,8.790877,4.337084,-0.642550,8.439627,-2.459466,4.840206,-0.266995,-9.836802,9.987166,-1.666449,-0.558544,-7.280080,2.755955,7.956465,-7.524049,9.150681,-4.778982,2.378240,-3.773214,-2.239467,4.414205,5.985898,-0.467675,3.077756,-0.186878,9.178433,1.887818,-2.249165,8.739269,-3.511114,-6.264422], dtype = "float64")#candidate|1712|(1440,)|const|float64
call_1711 = relay.TupleGetItem(func_709_call(relay.reshape(const_1712.astype('float64'), [12, 15, 8])), 0)
call_1713 = relay.TupleGetItem(func_711_call(relay.reshape(const_1712.astype('float64'), [12, 15, 8])), 0)
func_1532_call = mod.get_global_var('func_1532')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_1715 = relay.TupleGetItem(func_1532_call(), 0)
call_1716 = relay.TupleGetItem(func_1533_call(), 0)
output = relay.Tuple([call_1690,call_1711,const_1712,call_1715,])
output2 = relay.Tuple([call_1691,call_1713,const_1712,call_1716,])
func_1719 = relay.Function([], output)
mod['func_1719'] = func_1719
mod = relay.transform.InferType()(mod)
mutated_mod['func_1719'] = func_1719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1719_call = mutated_mod.get_global_var('func_1719')
call_1720 = func_1719_call()
output = call_1720
func_1721 = relay.Function([], output)
mutated_mod['func_1721'] = func_1721
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1795 = relay.var("var_1795", dtype = "float32", shape = (3, 5, 8))#candidate|1795|(3, 5, 8)|var|float32
var_1796 = relay.var("var_1796", dtype = "float32", shape = (3, 5, 8))#candidate|1796|(3, 5, 8)|var|float32
bop_1797 = relay.floor_divide(var_1795.astype('float32'), relay.reshape(var_1796.astype('float32'), relay.shape_of(var_1795))) # shape=(3, 5, 8)
output = bop_1797
output2 = bop_1797
func_1800 = relay.Function([var_1795,var_1796,], output)
mod['func_1800'] = func_1800
mod = relay.transform.InferType()(mod)
mutated_mod['func_1800'] = func_1800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1800_call = mutated_mod.get_global_var('func_1800')
var_1802 = relay.var("var_1802", dtype = "float32", shape = (3, 5, 8))#candidate|1802|(3, 5, 8)|var|float32
var_1803 = relay.var("var_1803", dtype = "float32", shape = (3, 5, 8))#candidate|1803|(3, 5, 8)|var|float32
call_1801 = func_1800_call(var_1802,var_1803,)
output = call_1801
func_1804 = relay.Function([var_1802,var_1803,], output)
mutated_mod['func_1804'] = func_1804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mod.get_global_var('func_793')
func_794_call = mutated_mod.get_global_var('func_794')
call_1817 = relay.TupleGetItem(func_793_call(), 0)
call_1818 = relay.TupleGetItem(func_794_call(), 0)
const_1821 = relay.const([-4,-7,-9,9,10,4,-2,-4,10,2,7,-6,3,-2,1,4,5,4,-6,-3,-6,2,1,-10,-10,-5,-8,-5,-4,-3,-5,10,2,-3,8,-5,-4,-10,-2,8,-3,-8,3,-3,8,-3,4,-2,-9,5,2,10,6,1,-2,-8,1,7,7,2,-5,10,-8,6,-9,7,-10,7,8,-1,-8,-5,-5,4,10,9,1,-5,-4,-10,-3,-6,3,8,-3,10,-10,-4,-9,10,4,-5,1,-6,4,-9,1,9,-1,5,-9,-9,2,-5,2], dtype = "uint64")#candidate|1821|(105,)|const|uint64
bop_1822 = relay.maximum(call_1817.astype('int32'), relay.reshape(const_1821.astype('int32'), relay.shape_of(call_1817))) # shape=(105,)
bop_1825 = relay.maximum(call_1818.astype('int32'), relay.reshape(const_1821.astype('int32'), relay.shape_of(call_1818))) # shape=(105,)
output = relay.Tuple([bop_1822,])
output2 = relay.Tuple([bop_1825,])
func_1835 = relay.Function([], output)
mod['func_1835'] = func_1835
mod = relay.transform.InferType()(mod)
output = func_1835()
func_1836 = relay.Function([], output)
mutated_mod['func_1836'] = func_1836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_1860 = func_927_call()
call_1861 = func_927_call()
output = relay.Tuple([call_1860,])
output2 = relay.Tuple([call_1861,])
func_1866 = relay.Function([], output)
mod['func_1866'] = func_1866
mod = relay.transform.InferType()(mod)
output = func_1866()
func_1867 = relay.Function([], output)
mutated_mod['func_1867'] = func_1867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1195_call = mod.get_global_var('func_1195')
func_1196_call = mutated_mod.get_global_var('func_1196')
call_1868 = func_1195_call()
call_1869 = func_1195_call()
uop_1872 = relay.exp(call_1868.astype('float32')) # shape=(315,)
uop_1874 = relay.exp(call_1869.astype('float32')) # shape=(315,)
output = uop_1872
output2 = uop_1874
func_1879 = relay.Function([], output)
mod['func_1879'] = func_1879
mod = relay.transform.InferType()(mod)
output = func_1879()
func_1880 = relay.Function([], output)
mutated_mod['func_1880'] = func_1880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1186_call = mod.get_global_var('func_1186')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_1916 = relay.TupleGetItem(func_1186_call(), 0)
call_1917 = relay.TupleGetItem(func_1188_call(), 0)
uop_1926 = relay.log10(call_1916.astype('float32')) # shape=(315,)
uop_1928 = relay.log10(call_1917.astype('float32')) # shape=(315,)
uop_1929 = relay.acos(uop_1926.astype('float64')) # shape=(315,)
uop_1931 = relay.acos(uop_1928.astype('float64')) # shape=(315,)
func_980_call = mod.get_global_var('func_980')
func_983_call = mutated_mod.get_global_var('func_983')
const_1940 = relay.const([[9.565135,8.152014,-4.137928,-3.517239,8.486956,-9.933348,-3.553544,-6.748991,-0.660015,-2.282651,-5.586353,-3.679540,-1.316531,-5.345026,8.429862,5.522136,-9.277512,4.399705,7.331476,-3.789751,3.221365,6.975761,0.591412,-1.822454,-1.148538,-5.802575,-0.550356,-9.076623,7.146455,6.016516,8.824905,1.517899,9.079385,-4.006083,-8.027863,-4.986891,0.660972,7.113532,7.366246,-9.712618,-2.327932,7.053849,-7.152407,1.336947,-7.384311,-6.831671,-2.444217,4.232042,-1.657650,-4.330385,-0.563000,-3.267189,-7.666970,1.266620,-5.538878,9.977171,-5.602500,6.572038,-4.796718,-7.515600,-7.055306,-2.837584,-4.036380,-6.357936,7.344534,6.240955,7.959412,-2.205236,-6.283261,-6.598448,0.081345,8.958478],[-8.259246,-7.130057,-7.816013,9.657640,9.225560,9.050533,7.212123,2.012326,-4.487329,-3.269349,-1.335526,3.408107,-5.911704,2.002194,3.047896,-0.615355,-4.318919,8.335870,9.145420,2.241418,-3.725024,2.965372,-9.462396,2.243979,8.328184,3.594869,-4.692185,-8.191249,-7.998593,-7.433499,2.637114,3.419892,-5.529320,-5.562584,7.894691,-4.223769,-6.058375,0.339604,-1.408682,7.867307,-5.563745,-7.864033,7.029660,-8.829230,-2.630738,9.701817,2.943601,3.898727,7.430320,3.314126,3.076271,2.183305,6.470032,0.627069,8.928810,-3.008241,5.350317,-2.503544,1.956919,-3.019911,3.630363,3.648142,-8.371814,-7.786923,-9.705144,-3.286121,-4.587189,7.182499,-6.642754,5.273010,5.094096,2.974572],[-5.402707,4.867570,-6.003442,-1.829601,-9.247082,-6.667380,-2.135605,-3.457001,0.403345,8.085512,-5.094664,2.945402,0.977245,-6.655635,-4.044281,3.439490,3.070327,5.738238,-7.554901,-1.869967,3.771417,1.974552,8.004894,6.930299,-8.522488,-5.444894,4.961847,3.753581,4.218924,-8.482052,1.564887,-7.846973,-1.497936,9.304325,5.159012,6.376855,-7.670535,3.737147,3.491073,-5.819903,3.644847,-2.148593,3.879643,2.318950,-1.955594,-6.266780,4.237999,-0.359314,-8.871612,-5.130602,7.030596,0.739434,-2.039099,-6.726732,0.850172,9.739254,9.710654,1.705918,0.066904,7.631876,-9.128735,3.015565,9.073885,-0.895693,0.597573,8.933715,-3.902339,6.599516,2.035712,-0.928342,-1.688659,2.996129],[-4.863157,-5.238795,1.960912,8.391809,-6.481813,6.233195,-4.318521,9.988140,-3.210602,6.355873,7.734608,4.219968,-1.721486,4.860871,2.446174,-8.856504,-0.658107,9.280906,4.997692,0.904655,-3.537393,1.506386,-6.104912,-9.224885,2.020234,-8.152250,-8.490077,-2.206274,1.661189,-7.516094,-3.550528,-3.847710,6.062518,5.359456,-0.329094,-4.338526,8.247870,-7.491961,1.014714,0.970123,-3.058062,6.207455,3.028361,0.223675,-0.119670,-4.559547,-8.955352,8.334288,-4.065542,-1.210796,4.170739,5.911070,-5.552196,8.957261,6.305880,4.892685,-2.409468,-8.241608,-6.887334,-0.941379,9.085762,6.394091,-2.933868,-4.159606,4.083029,4.648831,1.644294,-8.996950,-6.539129,8.651989,-7.642897,0.126673],[-9.641746,-7.133435,4.920600,7.289118,9.437615,1.668550,2.615167,0.951215,-1.622783,4.831242,4.106648,-6.044524,3.803697,9.092501,-8.683085,-4.693511,2.796793,7.350187,-8.210441,6.146909,4.612979,6.992538,-1.327567,-2.650227,7.461700,1.689861,4.448359,1.127528,8.820459,-2.052249,8.314589,-5.751441,2.746578,-8.190085,-0.941788,-3.274044,-6.383633,-1.117174,-9.348059,0.323509,5.837774,-8.277635,-6.295096,0.764567,1.433384,6.521362,3.277831,2.501000,7.606694,-7.071098,3.508076,-8.433632,-4.498381,1.845692,4.688651,-5.938102,9.021555,9.327896,-4.285096,1.261390,-1.725934,7.652493,8.833546,-7.447542,-9.593561,-9.625188,6.636397,0.845517,-5.901892,-1.441133,9.819001,-3.984952],[-8.506229,1.281200,-6.449704,-7.966606,5.860344,-3.211292,-7.632851,-4.099508,9.294946,-1.984576,1.180915,-6.950255,-8.465770,7.894295,-5.505595,-6.154321,2.632748,6.205929,8.861905,-3.419153,8.286349,0.281442,2.858494,-3.900528,-4.399842,-5.860222,-5.593024,1.288581,5.831921,6.153969,-2.686967,-7.960060,3.311772,-2.772163,9.141926,8.965869,3.564975,-5.618548,-3.978548,-4.107795,-2.189654,-8.932573,0.814566,0.518215,-7.750789,-6.403138,0.160428,-1.895300,6.669703,2.101799,8.032310,1.944836,4.849485,-0.487325,7.676840,-8.424608,1.505796,-8.916666,3.732735,5.698344,-0.457966,-9.858170,3.926689,-1.276907,2.098876,5.928770,9.389385,-8.422844,5.901944,-9.988405,2.151269,-3.486100],[-4.109368,8.359334,-7.363765,4.601942,2.848142,-2.703642,4.476367,6.197790,-2.471236,1.982941,6.710789,-5.285379,-8.288214,3.074132,-0.108967,-6.991024,3.750071,-8.092560,4.835832,-1.519767,9.721816,1.269671,-0.543972,-9.618111,4.891448,-2.434742,0.583778,3.595983,1.794253,8.782008,-5.642337,-2.559365,7.783561,-0.331859,4.138369,0.468772,0.778319,5.835747,8.613853,6.319081,6.174926,-2.398364,-5.004720,8.323513,-0.992696,4.484345,-9.008923,-5.694629,-7.034748,-1.000294,-9.548860,5.901365,-8.998767,2.505427,-6.037220,6.355504,-5.711765,-2.712109,9.801904,-6.493215,-7.374568,2.486675,-8.512307,-9.510422,-2.243002,-3.980459,5.063672,-2.268417,-3.101745,2.414315,-2.930260,-6.959715],[-4.057906,-0.283785,-6.494838,-4.486321,-6.311212,-5.763434,8.814644,-0.926409,4.163928,-6.587345,-6.411973,1.420129,-8.389402,5.025446,9.690989,7.107416,-5.339484,8.298156,0.263218,1.947870,6.179691,-6.341930,-4.005217,-1.050466,5.370897,-2.999783,-1.916909,-0.582733,9.611832,6.961502,3.289009,-7.122176,-9.524937,5.821622,2.852187,-7.669929,-3.997822,-9.310013,0.274775,-6.633514,2.471326,-3.996762,-4.715511,0.609731,-1.969187,-8.225857,9.288779,5.883882,7.186814,0.422222,9.537328,6.012096,-6.774494,-5.902357,3.940567,-7.943412,-5.547857,-0.736241,0.155473,-0.430157,-6.121452,-0.251278,9.333540,-9.805345,-5.541197,-2.782837,2.431130,3.127870,5.173537,9.044690,-8.986604,2.117222],[-0.903011,-3.297532,1.966907,9.943506,3.425440,-6.525340,6.234367,4.261238,-4.536370,5.706987,-0.371344,-7.975175,-9.608967,-7.337684,6.170446,4.634208,5.317915,-0.753560,-5.971320,-9.177774,8.101880,1.797520,8.726858,-9.302566,-9.209593,5.105683,-1.066550,-3.823262,1.064713,0.133734,-7.327010,-3.811911,-5.274177,7.903905,-9.503603,2.058705,-2.266190,-5.358674,1.135440,9.701152,-6.100679,-3.296399,-1.514394,-9.960405,5.582667,4.676684,-8.716274,0.959656,-5.088043,-6.904927,3.493719,-4.724942,-9.397689,6.511471,8.393572,8.529763,-2.279289,-2.079450,-6.267685,-3.824874,-3.681764,4.295040,-8.976276,-7.272537,8.920500,9.867999,-4.930654,-3.028221,6.607032,-7.971717,9.342864,-1.587100],[-6.599665,-9.655764,3.895415,-7.079435,-9.886634,0.363526,1.619967,5.118390,-7.384864,1.961375,-5.973316,3.764840,3.255584,-7.625175,9.263121,-7.039529,6.182975,-6.372831,-4.804922,1.610370,-6.327747,3.561290,-0.174072,2.951523,9.549568,8.111196,-1.989824,9.266627,-0.806041,-6.534212,9.132641,6.255434,-0.276591,0.612384,5.482472,7.209350,1.193403,3.895663,-4.321444,-7.739708,2.433828,7.823432,-5.424709,0.862578,9.050353,-6.103952,5.866710,4.598527,3.818768,-6.411698,2.551555,5.872533,-9.466430,-5.068483,6.086843,-1.903085,-8.038226,-8.756544,3.985106,-5.668946,-6.822927,9.630759,-3.597089,1.469082,9.719460,-2.847218,4.307004,-2.215947,-5.108472,-4.946550,6.559053,-9.389441],[0.931549,3.889623,1.222229,5.531513,-4.697320,0.453967,1.869788,2.924383,-8.616517,-4.035440,0.403601,1.604333,9.080824,4.509393,-7.568463,8.624844,-7.128211,-7.758443,-6.386197,8.405001,-5.165592,6.382594,1.050447,2.816833,0.410854,-8.462564,-1.441148,-9.947752,3.029359,-8.743403,-3.137990,4.328398,-1.803479,-1.822772,2.990996,-8.215015,-1.038693,-8.200156,-0.281339,2.689341,5.807527,-0.407910,1.591355,0.901893,-0.124278,-5.827015,3.471010,6.917708,-7.393903,-9.144996,-6.792178,7.464607,5.809304,-4.603360,2.597396,9.043764,4.763064,-6.431578,-7.255787,-6.747722,-0.642624,3.677808,-4.230612,1.422487,-3.886015,3.729227,-5.477494,6.164611,-2.680917,6.504600,2.595975,-8.515716],[-8.184059,6.313542,-1.096066,2.354117,1.261431,4.803255,-3.630018,-0.562931,-6.282187,8.176153,-3.995433,-0.686962,-7.308458,4.802575,-1.674818,4.286281,-9.076906,-3.857796,-3.093250,0.729234,-6.008115,9.221593,-4.208589,-7.411997,3.845203,5.942525,-9.711128,-3.463075,-7.683980,9.425257,0.991235,6.407583,1.391058,4.155130,-3.613497,8.622499,9.506114,4.377131,-5.159208,-6.683433,2.065711,-0.865025,-8.386937,-9.352736,-5.062097,2.400033,-8.601967,3.997311,-4.218989,0.405183,-5.555250,-2.488122,-5.227268,4.447371,6.686807,-5.720963,4.906757,-7.395195,-6.595766,-2.586605,-2.693506,-9.857104,9.303920,0.183407,-4.754895,-8.235422,3.689271,-2.552843,-6.636953,3.839687,-9.142257,-6.964578],[-7.876440,2.829056,1.722473,4.047225,9.872376,5.955346,9.405087,8.550072,4.975849,-4.571729,-8.510706,-5.807570,-5.475673,-4.827213,-2.072283,6.908735,5.154914,4.911906,-4.152538,1.033504,-2.365805,-7.630879,5.839270,-2.951775,1.658661,2.030354,2.844057,-1.095607,2.013469,-9.940320,2.827056,-9.921000,-3.891918,-9.359997,-1.808535,9.846426,-9.773838,5.648963,7.171962,-2.903338,-7.155289,-0.934691,-2.833858,-6.084798,1.443202,0.058385,-6.672087,7.609888,7.602408,6.788000,4.212084,-0.977693,3.900819,4.078155,7.812535,4.726386,-2.410203,-0.769304,7.023408,-2.433887,5.709667,0.467941,-7.586106,8.736544,-2.533587,8.932391,0.129971,8.499833,8.290391,0.301054,9.892688,5.416117],[-6.692882,-9.819078,-3.349165,-7.596959,-4.897187,2.108077,-9.462204,-3.977839,5.285492,5.433618,5.666273,1.065706,7.318372,-6.337041,-6.216644,-3.792008,5.958150,-9.746786,-6.812692,9.506775,-7.937231,0.318145,5.640195,-8.316803,8.275414,2.091324,-4.296321,-7.699130,8.276457,-3.829470,-6.426341,-5.722121,1.147326,7.667812,7.777771,-8.116634,3.373618,2.708888,5.565561,6.165367,0.372819,-1.224445,-3.098200,2.889024,2.430738,4.720602,7.360322,6.585112,-2.171935,-1.159894,6.953335,6.481120,-9.690662,-0.714869,-9.706175,-9.625803,-6.952670,-7.852318,6.827435,3.538651,2.450920,-6.422182,-9.579672,-8.983133,-2.201773,4.212327,6.144292,-9.101295,9.488457,-7.372649,8.107050,4.923440],[4.356018,-1.506442,5.893096,0.440167,-9.154635,0.874467,1.326357,3.891854,-8.992709,4.774314,0.218087,8.021128,-4.256327,8.279827,1.378202,-1.349282,-2.348236,4.352853,-6.652218,-3.336955,6.414893,3.169382,4.391602,-7.501645,0.583597,-9.128589,-9.918835,1.126607,3.207449,-9.330572,2.463062,1.262273,6.745970,-3.826831,1.496287,-0.379864,-0.869635,0.116178,-5.520586,-2.342902,4.117419,-8.339763,-7.946987,2.801849,-7.960624,-8.342459,-8.714358,9.303487,4.053303,0.786970,0.686796,3.818326,6.478860,2.250074,-0.780916,-4.986457,-6.823560,7.693368,-7.334767,-7.812800,-3.866297,2.811160,-6.765101,-6.496766,-0.902835,-2.935405,6.350991,1.946890,-2.617049,-6.154460,-0.527808,8.112555],[-8.816304,-7.871821,1.503479,5.120630,4.196333,-7.515762,-9.109164,9.312427,-5.701226,-6.109800,2.781143,-8.140632,-1.428328,5.150637,5.386193,-3.703206,7.315219,1.186719,1.672909,9.784881,1.939585,5.397708,-3.460803,-3.969800,-2.674284,4.799812,-2.272913,-4.332238,-8.570334,-2.066485,-2.782191,8.826885,7.843464,-6.922510,-0.638272,3.718846,2.000479,5.181008,-5.839672,-8.044010,-5.180298,-1.563358,7.932302,2.593771,-2.631154,-6.218784,-2.378240,4.024921,-1.284950,9.216630,3.621315,-7.102631,1.964652,-7.882100,2.268367,-0.893198,-3.223689,-5.668590,5.657488,-0.614239,7.197554,-3.515461,-8.813974,0.964597,0.661599,2.789233,-8.073905,3.903436,7.008460,8.905879,-7.507252,-3.924689],[-4.791516,0.397325,5.099276,-9.730924,-8.128009,-1.200764,-3.388059,0.923302,-3.436097,-6.892901,-3.838116,-1.205909,1.080557,-6.978792,-0.643456,4.499630,7.386773,-5.755019,-4.075179,-7.973353,-5.689889,6.618989,-1.747949,-4.972131,-3.004927,8.408640,7.255411,-7.643653,5.539650,-0.159710,-7.309304,3.369694,-8.239358,-8.132441,-8.334565,5.733886,1.805976,8.259159,1.277942,9.505147,-7.134232,-5.032832,-0.038938,-9.465194,8.076429,1.199910,-0.278277,-2.040830,1.421518,9.835793,1.034009,-2.970753,-6.735155,-7.247110,0.270839,9.131491,3.239904,3.093278,-9.252240,1.554979,6.046952,6.917984,9.954289,-8.664733,-0.496589,-0.651777,7.163760,3.447973,-4.624224,4.370851,1.577010,2.552678],[3.579897,-8.718697,0.833251,0.095107,7.809440,-6.728303,-6.753040,5.924000,5.341723,-8.871901,-1.657295,-9.174832,-4.214888,-9.822877,-1.656320,-1.550673,9.348045,7.915647,-1.267720,5.892597,-7.884220,3.464214,-3.084421,5.804878,-1.435966,-0.406629,2.021801,-9.172874,2.924600,1.731179,-8.777745,1.969818,9.229066,-9.169839,1.679587,3.074421,-4.786966,6.223693,0.561934,-0.561244,-0.939449,-7.470001,0.516886,2.115189,9.566343,-6.186236,-9.760669,7.522843,-0.965499,-3.015826,0.455802,4.773389,-4.339652,6.913169,-0.559612,1.591412,-2.784312,-0.601037,-2.837339,-9.008945,9.576179,-1.436537,-6.614671,1.971951,8.465676,1.339091,9.027646,-5.192534,4.332554,0.507091,3.298950,-8.352789],[-0.348808,0.661469,3.075055,-7.122216,-5.461309,-6.966099,1.678228,-8.825294,8.889504,2.303718,-5.519426,-7.336695,9.726802,2.599301,3.895350,5.347972,2.583760,-4.416929,-4.987490,9.012160,5.747169,-9.475947,3.278143,-1.103081,-5.781632,4.042944,3.942064,-1.305519,4.795834,-1.753943,0.933092,-5.746390,-2.488928,6.733605,4.672964,-0.086641,0.314284,4.156701,0.490156,9.655674,-4.226935,-1.216630,5.506797,-9.606912,5.502870,5.104017,-2.593239,2.112605,-2.166507,-3.897133,1.114939,2.176121,8.465010,4.905138,-9.778371,-8.991762,6.804752,-2.337699,9.977087,9.584131,8.841390,8.197647,-2.600939,6.652076,-4.100052,-0.637172,-6.764740,-9.385172,2.216661,-2.211464,-8.640104,-3.541828],[1.932103,-1.974622,9.764391,1.731434,-0.216529,7.250130,6.997455,-9.003888,-3.499063,3.213911,-4.123472,-8.031960,2.445124,7.722079,5.582678,9.381089,-1.999096,4.942013,1.994220,7.902893,2.524581,-8.750179,7.718794,-5.928651,-3.984911,-6.914222,8.133724,-0.278637,2.659116,9.719282,5.489931,6.707652,-4.757305,6.067547,-5.871971,-8.670046,5.516738,-4.103260,7.685735,-7.614063,7.244932,-1.586367,7.991911,5.954619,-5.988796,2.519890,-4.852150,3.057073,8.903228,-4.441654,5.203293,-4.567182,-9.041657,0.334463,6.374599,3.684589,-0.562033,-5.064714,-9.696017,-2.253606,-1.663058,-1.275004,1.861549,0.879635,-0.587223,-2.925824,-8.801659,8.284995,7.221337,-2.931399,-1.441908,5.601344]], dtype = "float64")#candidate|1940|(20, 72)|const|float64
call_1939 = relay.TupleGetItem(func_980_call(relay.reshape(const_1940.astype('float64'), [720, 2])), 3)
call_1941 = relay.TupleGetItem(func_983_call(relay.reshape(const_1940.astype('float64'), [720, 2])), 3)
bop_1949 = relay.logical_and(uop_1929.astype('bool'), relay.reshape(call_1916.astype('bool'), relay.shape_of(uop_1929))) # shape=(315,)
bop_1952 = relay.logical_and(uop_1931.astype('bool'), relay.reshape(call_1917.astype('bool'), relay.shape_of(uop_1931))) # shape=(315,)
uop_1956 = relay.cosh(uop_1926.astype('float64')) # shape=(315,)
uop_1958 = relay.cosh(uop_1928.astype('float64')) # shape=(315,)
func_1500_call = mod.get_global_var('func_1500')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_1961 = func_1500_call(relay.reshape(bop_1949.astype('uint16'), [315,]))
call_1962 = func_1500_call(relay.reshape(bop_1949.astype('uint16'), [315,]))
uop_1966 = relay.log(uop_1956.astype('float32')) # shape=(315,)
uop_1968 = relay.log(uop_1958.astype('float32')) # shape=(315,)
func_980_call = mod.get_global_var('func_980')
func_983_call = mutated_mod.get_global_var('func_983')
call_1970 = relay.TupleGetItem(func_980_call(relay.reshape(call_1939.astype('float64'), [720, 2])), 0)
call_1971 = relay.TupleGetItem(func_983_call(relay.reshape(call_1939.astype('float64'), [720, 2])), 0)
output = relay.Tuple([call_1939,const_1940,bop_1949,call_1961,uop_1966,call_1970,])
output2 = relay.Tuple([call_1941,const_1940,bop_1952,call_1962,uop_1968,call_1971,])
func_1972 = relay.Function([], output)
mod['func_1972'] = func_1972
mod = relay.transform.InferType()(mod)
output = func_1972()
func_1973 = relay.Function([], output)
mutated_mod['func_1973'] = func_1973
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2031 = relay.const([[[3.263868,-0.181758],[-0.945400,-6.157402],[1.759508,-6.134551]],[[4.135685,3.433804],[-1.661410,8.313027],[3.341952,6.036953]],[[-9.538343,9.438964],[-2.045792,7.958762],[-6.981825,-5.562053]],[[-9.061185,4.553818],[-1.833124,-0.301391],[1.737416,4.569276]],[[-8.048595,7.597790],[6.015231,-9.433593],[8.963946,-0.896752]],[[-9.279963,3.702572],[9.266661,-1.232320],[-5.910658,9.693452]],[[6.404839,-2.850401],[5.645912,-9.795970],[-7.587454,6.932789]],[[4.734902,-3.693404],[9.246844,-5.899007],[-9.246382,4.282074]],[[5.692523,-0.807748],[8.174603,-9.351773],[9.945221,0.659137]]], dtype = "float64")#candidate|2031|(9, 3, 2)|const|float64
const_2032 = relay.const([[[-5.837961,4.362576],[8.319610,-7.559138],[2.581462,-8.838238]],[[9.608530,5.153324],[5.180765,-0.796174],[-9.936440,0.169660]],[[-8.168538,0.469167],[-0.930540,-5.576292],[5.477997,-8.661303]],[[-0.420657,-0.800831],[0.570371,3.925362],[9.090145,0.635111]],[[-4.986765,-5.604367],[7.315194,2.930469],[-0.887969,4.620403]],[[8.472307,-5.087794],[9.370530,8.583531],[6.935677,3.347734]],[[6.094369,9.518739],[4.605547,6.692647],[4.969224,-8.792607]],[[2.712537,-9.100493],[-4.193484,-7.242574],[7.282355,-5.097494]],[[-1.017445,-2.678575],[9.935006,-5.575339],[8.122307,-0.162799]]], dtype = "float64")#candidate|2032|(9, 3, 2)|const|float64
bop_2033 = relay.divide(const_2031.astype('float64'), relay.reshape(const_2032.astype('float64'), relay.shape_of(const_2031))) # shape=(9, 3, 2)
bop_2036 = relay.minimum(const_2031.astype('uint32'), relay.reshape(bop_2033.astype('uint32'), relay.shape_of(const_2031))) # shape=(9, 3, 2)
uop_2040 = relay.asin(const_2032.astype('float64')) # shape=(9, 3, 2)
func_638_call = mod.get_global_var('func_638')
func_639_call = mutated_mod.get_global_var('func_639')
call_2042 = relay.TupleGetItem(func_638_call(), 1)
call_2043 = relay.TupleGetItem(func_639_call(), 1)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_2045 = relay.TupleGetItem(func_1972_call(), 0)
call_2046 = relay.TupleGetItem(func_1973_call(), 0)
output = relay.Tuple([bop_2036,uop_2040,call_2042,call_2045,])
output2 = relay.Tuple([bop_2036,uop_2040,call_2043,call_2046,])
func_2049 = relay.Function([], output)
mod['func_2049'] = func_2049
mod = relay.transform.InferType()(mod)
output = func_2049()
func_2050 = relay.Function([], output)
mutated_mod['func_2050'] = func_2050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_2070 = func_1879_call()
call_2071 = func_1879_call()
func_2049_call = mod.get_global_var('func_2049')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_2080 = relay.TupleGetItem(func_2049_call(), 0)
call_2081 = relay.TupleGetItem(func_2050_call(), 0)
func_980_call = mod.get_global_var('func_980')
func_983_call = mutated_mod.get_global_var('func_983')
var_2103 = relay.var("var_2103", dtype = "float64", shape = (1440, 1))#candidate|2103|(1440, 1)|var|float64
call_2102 = relay.TupleGetItem(func_980_call(relay.reshape(var_2103.astype('float64'), [720, 2])), 3)
call_2104 = relay.TupleGetItem(func_983_call(relay.reshape(var_2103.astype('float64'), [720, 2])), 3)
output = relay.Tuple([call_2070,call_2080,call_2102,var_2103,])
output2 = relay.Tuple([call_2071,call_2081,call_2104,var_2103,])
func_2105 = relay.Function([var_2103,], output)
mod['func_2105'] = func_2105
mod = relay.transform.InferType()(mod)
mutated_mod['func_2105'] = func_2105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2106 = relay.var("var_2106", dtype = "float64", shape = (1440, 1))#candidate|2106|(1440, 1)|var|float64
func_2105_call = mutated_mod.get_global_var('func_2105')
call_2107 = func_2105_call(var_2106)
output = call_2107
func_2108 = relay.Function([var_2106], output)
mutated_mod['func_2108'] = func_2108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1685_call = mod.get_global_var('func_1685')
func_1687_call = mutated_mod.get_global_var('func_1687')
call_2127 = relay.TupleGetItem(func_1685_call(), 0)
call_2128 = relay.TupleGetItem(func_1687_call(), 0)
func_2049_call = mod.get_global_var('func_2049')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_2129 = relay.TupleGetItem(func_2049_call(), 3)
call_2130 = relay.TupleGetItem(func_2050_call(), 3)
func_2049_call = mod.get_global_var('func_2049')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_2131 = relay.TupleGetItem(func_2049_call(), 1)
call_2132 = relay.TupleGetItem(func_2050_call(), 1)
var_2146 = relay.var("var_2146", dtype = "float64", shape = (9, 3, 2))#candidate|2146|(9, 3, 2)|var|float64
bop_2147 = relay.logical_or(call_2131.astype('bool'), relay.reshape(var_2146.astype('bool'), relay.shape_of(call_2131))) # shape=(9, 3, 2)
bop_2150 = relay.logical_or(call_2132.astype('bool'), relay.reshape(var_2146.astype('bool'), relay.shape_of(call_2132))) # shape=(9, 3, 2)
func_980_call = mod.get_global_var('func_980')
func_983_call = mutated_mod.get_global_var('func_983')
call_2159 = relay.TupleGetItem(func_980_call(relay.reshape(call_2129.astype('float64'), [720, 2])), 0)
call_2160 = relay.TupleGetItem(func_983_call(relay.reshape(call_2129.astype('float64'), [720, 2])), 0)
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_2168 = relay.TupleGetItem(func_1394_call(), 0)
call_2169 = relay.TupleGetItem(func_1396_call(), 0)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_2178 = func_575_call()
call_2179 = func_575_call()
func_1195_call = mod.get_global_var('func_1195')
func_1196_call = mutated_mod.get_global_var('func_1196')
call_2182 = func_1195_call()
call_2183 = func_1195_call()
func_1318_call = mod.get_global_var('func_1318')
func_1320_call = mutated_mod.get_global_var('func_1320')
const_2185 = relay.const([[False,False,True,True,False,False,True,True],[False,True,True,True,True,False,False,True],[False,True,True,True,True,False,True,True],[True,True,False,False,True,True,False,False],[True,True,True,False,True,False,True,False],[True,False,True,False,False,True,True,True],[False,True,False,False,True,True,True,False],[False,False,False,False,True,False,False,True],[False,True,True,True,False,False,True,True],[False,False,False,True,True,True,False,False],[False,False,False,False,True,True,False,True],[True,True,True,True,True,True,False,True],[True,True,True,True,True,False,False,True],[True,False,False,False,False,False,False,False],[False,False,False,True,False,True,True,True],[False,False,False,True,False,False,True,True],[True,False,False,False,False,False,False,True],[True,False,False,True,True,False,True,True],[True,False,True,True,True,False,False,True],[False,True,False,False,True,True,True,True],[True,True,True,False,False,True,True,True],[False,True,False,True,False,True,False,True],[True,True,False,False,True,False,True,False],[True,False,False,True,True,False,False,True],[True,True,True,True,True,False,False,True],[False,False,False,False,False,False,True,True],[False,True,False,True,True,True,True,True],[True,False,False,True,False,False,False,True],[True,True,True,False,True,True,True,True],[False,True,True,False,False,False,True,False],[True,True,True,True,True,True,False,False],[True,False,True,True,False,True,False,True],[False,True,False,False,True,True,True,True],[True,True,True,True,True,False,True,True],[False,False,False,True,True,False,True,False],[False,True,True,False,False,False,True,True],[True,True,True,False,True,False,True,False],[True,False,True,True,True,False,False,True],[False,False,False,False,False,True,False,False],[False,False,False,True,False,True,False,True],[True,True,False,False,True,True,False,True],[False,True,False,True,True,False,False,True],[False,False,True,False,True,False,False,False],[False,False,True,False,True,True,True,False],[False,True,False,True,True,False,False,True],[True,False,False,False,False,False,False,False],[False,True,False,True,True,False,True,True],[False,False,True,False,True,True,False,True],[False,True,True,True,True,True,False,True],[False,False,True,False,False,True,True,False],[True,True,False,False,False,True,False,False],[False,True,False,True,False,True,True,True],[False,False,False,True,True,True,False,True],[True,False,False,False,True,True,False,False],[False,False,True,False,False,True,True,False],[False,True,True,True,False,False,False,False],[False,False,False,False,True,False,True,True],[False,True,True,False,False,True,False,True],[False,True,True,False,False,False,False,True],[False,True,False,False,False,False,True,False],[False,True,False,False,True,False,True,False],[True,False,False,False,True,False,True,True],[False,False,True,False,True,True,True,True],[True,True,True,True,True,False,True,False],[True,False,False,True,False,True,True,True],[True,True,True,False,True,False,False,True],[True,True,False,False,True,True,True,False],[True,False,True,False,True,False,False,False],[False,False,True,False,True,False,False,False],[True,True,True,True,False,True,False,True],[False,False,True,True,False,False,True,True],[False,False,True,True,True,False,False,True],[False,True,False,False,False,False,False,True],[True,True,False,True,False,True,False,True],[True,True,False,True,True,False,False,False],[False,False,True,True,False,True,True,False],[True,True,False,True,True,True,False,False],[False,True,False,True,False,False,False,True],[False,False,True,True,False,True,True,True],[True,True,False,True,False,True,False,True],[False,False,False,True,True,True,False,False],[False,False,True,False,False,True,True,False],[True,False,False,False,False,True,True,True],[False,True,True,True,True,True,False,True],[True,True,True,True,False,True,True,False],[True,False,False,True,True,True,False,False],[False,False,False,False,True,True,True,False],[True,False,True,False,True,True,True,True],[False,False,False,False,True,True,False,False],[True,False,False,False,False,False,False,False],[False,True,False,True,False,True,True,True],[False,False,True,True,False,True,False,False],[True,False,True,True,True,True,True,False],[False,True,False,False,True,True,False,True],[False,False,True,False,True,False,False,True],[True,True,True,True,False,True,True,False],[False,False,True,True,False,False,False,False],[False,False,False,True,True,False,True,True],[False,False,False,True,False,False,True,True],[True,False,False,False,True,False,False,True],[False,True,True,False,True,True,False,True],[True,False,True,True,False,False,False,False],[False,False,False,False,False,True,False,False],[True,False,False,False,False,False,False,True],[True,True,True,False,False,False,False,True],[False,True,False,True,True,True,True,True],[True,True,True,False,False,True,False,True],[False,False,False,False,False,False,True,True]], dtype = "bool")#candidate|2185|(108, 8)|const|bool
call_2184 = relay.TupleGetItem(func_1318_call(relay.reshape(const_2185.astype('bool'), [432, 2])), 1)
call_2186 = relay.TupleGetItem(func_1320_call(relay.reshape(const_2185.astype('bool'), [432, 2])), 1)
const_2188 = relay.const([[[-8.615875,5.292707,8.744390,0.650879,-7.136863,-1.106929,8.379873,-4.334692,9.067694],[-5.373674,-3.141990,-0.520511,-3.533741,-5.033010,-7.005339,6.898759,-4.966013,-6.095788],[-1.538533,4.447271,6.681301,2.486350,0.956478,-2.939694,-5.587647,-7.637017,4.187922],[-1.096097,9.359785,-1.834183,-3.814535,-0.274613,-4.428407,-6.921604,5.080453,6.690098],[-8.603720,1.506802,3.692127,-5.860510,-7.236401,-1.295191,4.459547,-2.607412,-8.779729],[1.341961,-3.533172,2.563198,-9.014942,0.361292,-6.025698,2.858276,-0.786905,-4.303004],[-0.510571,4.190707,5.715718,-5.315768,-7.209670,4.298363,6.128814,-0.305929,6.106230],[-5.625187,4.293725,2.231884,4.317835,-9.110048,2.506224,4.093350,7.952420,-8.390007],[-6.026385,-4.941818,3.896238,9.023182,-5.092556,-4.623528,-8.287762,5.585052,0.533460],[1.217958,3.642562,-9.721291,-5.552792,5.791752,-0.973161,-8.023715,-2.510754,-9.252052],[3.429983,5.446564,7.329587,3.135389,-0.579979,3.044589,1.371397,-4.182417,9.027811],[8.709672,-5.252582,1.713954,-9.145863,-4.123933,-1.504235,5.995694,-6.135106,8.235851],[-7.035677,1.675290,-3.039072,-9.087908,9.819344,-1.484153,9.653170,-3.352664,-9.448365],[9.450739,-7.325860,-4.407739,-5.867409,-0.646834,-7.864217,-8.878656,-7.960409,1.400974],[-7.140192,-0.254864,4.938260,-6.250123,-6.853078,-9.929635,4.504813,6.746809,1.564609],[-6.906039,9.424110,9.483089,1.236193,5.300769,2.878710,-5.749236,-5.982466,-8.564096]],[[4.651636,0.919135,9.431213,3.797223,1.979742,-7.513629,-1.240939,-4.289747,0.065064],[6.206969,8.265557,-7.237960,4.007561,-5.158607,3.433888,0.993188,-1.373501,-0.086234],[8.506415,-9.722259,4.228425,3.747513,3.808643,8.482004,5.105029,6.940477,5.246143],[-3.090843,-0.019508,0.909482,7.914154,6.411438,9.233956,8.509857,2.673138,6.550442],[4.487525,-7.512737,-2.633510,4.066961,-7.005208,-1.531803,7.145337,-8.531464,2.354976],[2.761609,2.370449,-8.334805,5.108081,8.107708,2.379478,9.675785,1.229809,-4.057075],[9.259651,-5.696932,-1.991926,-4.349995,8.757454,-6.083580,-0.414380,4.773262,-3.700741],[-4.793427,7.537692,-5.315559,-2.073545,3.080059,5.950873,4.294842,-3.175392,-5.748573],[-6.222457,-3.677921,9.522642,-5.512138,-1.678590,2.077638,-3.195255,-3.977801,6.899711],[-6.398445,-2.479243,-6.844332,6.068366,5.574309,8.733306,1.025438,-9.935750,3.563966],[-5.125539,6.088949,9.170290,8.427856,-7.342279,0.476432,-8.478584,0.866821,-3.108669],[-6.224198,0.034356,5.896916,3.158451,-7.685034,-7.543105,4.100851,2.257410,2.310250],[-5.592746,-4.315643,8.453560,-3.187201,-0.555992,-8.424822,6.686158,-8.491742,-6.080135],[4.034405,-5.169997,3.614233,6.605925,1.060390,9.529755,8.474522,3.615580,-3.255643],[-7.844347,-0.201509,-5.159062,0.674978,7.191426,-9.883216,6.853743,0.116532,3.402432],[-4.194188,-0.808528,-6.167391,-5.924170,3.225221,8.256120,-6.028205,-3.634295,-9.008396]],[[-8.727989,0.110061,-3.357372,0.503245,4.990988,1.479336,-4.807823,-9.828495,-3.768559],[-1.145227,-8.013115,-3.592123,-6.372026,2.511874,-0.664677,6.893103,3.397559,-2.469765],[4.382844,7.472238,9.567623,7.177213,-7.395035,-9.248649,-7.235175,-1.782964,-6.142028],[6.983070,5.954054,0.789280,-7.820097,-6.053765,3.365527,7.972821,1.849519,-6.422504],[-7.675763,-0.226197,4.860723,3.528929,7.960635,-6.558920,-8.814075,-7.595949,7.289321],[1.743998,5.937455,4.236467,1.747942,1.732917,-2.047801,8.652145,7.322189,9.951982],[-2.904510,2.088041,-8.010341,1.825695,7.360669,5.157965,1.030354,-7.369914,-7.135023],[-1.856152,3.182826,-5.043120,5.048214,-2.382427,4.272533,4.434371,-7.931225,-6.471794],[-4.819831,8.975955,6.047640,-9.991785,-8.270504,3.456982,6.758752,-5.594078,3.220187],[-2.936503,-5.709041,-0.158042,-6.373086,8.785661,-4.697959,-7.477617,4.347486,-7.927451],[-0.245411,0.709653,0.842859,0.017802,-3.917479,5.553263,4.650450,-5.863142,-9.504258],[7.726334,-7.677953,6.704240,-3.164214,-3.680206,-9.399965,0.944731,4.143099,1.547193],[0.746497,0.933289,-7.171189,-1.468499,-4.090422,1.845070,8.775701,-4.440720,2.750832],[-2.124286,7.507289,9.556731,9.960381,-6.706081,8.785370,5.495148,-5.221581,4.316282],[-2.248377,-0.020253,-9.728221,9.755380,0.446416,-7.053570,-9.506225,-6.174068,3.445322],[1.933193,-2.177705,1.728575,4.337850,4.376449,-7.513683,-0.336290,-3.752889,2.502995]],[[-8.160999,-1.272115,-5.703446,-5.079324,3.026647,-5.376126,-9.679330,1.791477,4.435853],[-9.361230,7.410891,6.410044,-2.876433,-9.167208,-5.835719,-6.322411,5.905539,-6.190463],[2.703142,-6.117771,-5.468738,8.368805,-3.097216,3.314550,6.097515,-5.159402,3.795938],[-4.400624,3.334735,-8.245219,0.361608,-5.596886,9.947821,-5.316633,5.717939,5.889474],[-2.643486,-9.623739,6.871928,-2.819972,4.747803,-4.653968,-4.936231,9.818464,9.277432],[-5.470105,-7.960723,3.788081,8.497762,-4.130551,-6.149915,-0.207927,-9.332471,4.581469],[2.661301,-6.889150,-0.164968,0.536881,-5.976804,-4.946549,1.634170,-9.862324,2.280681],[8.105327,8.561103,6.518863,-3.038914,-7.603913,-6.549757,-6.310752,-3.614503,8.144038],[3.825966,6.481845,9.886065,-1.902994,-6.964706,-9.157170,-0.476202,8.670192,1.197342],[-1.427218,-5.187558,-7.771963,-9.003395,-1.608101,0.086137,-0.975996,4.564899,-3.515159],[9.443571,5.479523,7.160552,-5.296296,8.064614,-0.513591,-3.488501,-6.899340,0.051249],[-0.497250,-0.877391,-9.323114,-8.642707,-6.428925,5.615234,-3.244196,4.242147,-3.505053],[0.035226,1.324984,-9.550756,7.981322,-6.381559,-8.924012,-0.179192,1.879439,8.095031],[-4.896270,-3.992214,4.363660,-8.468288,7.462309,9.929872,-7.298920,-5.218869,-5.070684],[4.705852,1.237654,4.446045,-3.489224,-5.868627,-2.469772,1.214391,1.051427,-5.071579],[0.975309,-9.860764,-9.230302,2.499261,-5.856173,-2.648663,-2.269739,-3.081721,5.664302]],[[9.579949,6.384880,-7.779941,-8.348466,9.047590,3.494735,-5.605575,-7.238325,8.850458],[8.784956,6.275084,-0.510251,-6.389344,-3.324808,0.572800,-5.755028,7.500249,-6.347314],[-9.515909,3.865705,7.599481,7.002601,-1.051378,-8.537709,-1.084819,-7.694507,-1.020096],[-2.771355,9.417239,7.910890,-7.558613,-3.706161,-4.679935,8.889411,8.357778,-3.352154],[-6.971299,-1.284937,0.848497,-7.520284,-5.383520,3.411523,-2.490196,4.123944,-0.426878],[-0.517394,5.815352,-5.960474,1.604855,-7.351800,4.515148,0.760407,-5.190672,-4.669362],[5.222288,9.812780,3.553593,-5.493977,-9.071578,2.778052,-6.163813,-1.723012,-0.413165],[7.529139,-0.144606,-6.031626,-0.230964,1.688966,-1.022966,-6.611367,9.979311,4.190040],[9.597132,-4.527404,-6.795029,-2.143462,5.294598,-5.411376,-9.017876,0.725528,6.040643],[-1.704343,-1.233358,-5.508355,9.114947,-4.117737,-9.657424,0.818103,2.948059,-7.783970],[2.113098,-5.603608,5.404028,0.128857,5.778113,-1.784149,-8.652046,-2.236537,1.856710],[0.288720,-0.598464,1.257900,-9.109152,-1.734640,-0.128809,2.708939,5.433250,-3.541286],[-9.936309,-9.767022,-5.843787,-9.220670,3.057042,3.977289,8.896665,8.925880,-4.289830],[-7.167095,3.907071,-1.415774,7.561977,-4.074558,-4.389445,6.749853,-6.567697,-9.109402],[3.743187,2.323372,9.070870,5.519922,-6.627714,-8.759471,5.850719,0.928158,7.670040],[-8.043148,9.177692,-1.915570,9.641850,-0.431559,0.295013,-9.015019,2.175255,-8.045279]],[[6.571495,6.266866,-0.973150,-2.812361,-2.283977,0.828626,-1.770121,9.887603,-4.713878],[3.187654,9.845614,2.518882,-8.354631,6.605348,3.805674,-1.668588,5.219231,-9.500561],[-5.439499,6.264408,-1.296334,-6.866592,-7.125820,-2.387504,7.739141,-4.763135,4.075742],[-7.212760,-1.743978,3.425835,4.781109,-2.260070,4.018282,-2.590230,5.250113,4.287066],[-6.576121,-6.905178,3.684038,6.905451,-9.858913,4.061368,5.578037,3.881114,-1.247042],[-8.015712,1.308138,-8.322946,5.279405,-5.075466,2.041480,4.072633,2.768194,-0.495726],[-2.955787,-1.949708,-8.185530,3.956790,5.176067,3.708526,1.920591,0.786709,-1.818590],[-5.329036,-7.367877,-8.424062,-9.935098,-3.917603,-2.221562,-4.181499,-3.563850,7.923020],[-8.676776,8.954935,-8.271548,1.961793,-7.860622,-9.625039,6.494255,-0.456604,7.564105],[2.707872,-9.479302,4.065916,-2.523198,-1.821954,-3.186269,8.019106,-9.530786,-3.913254],[1.888989,-0.407978,-2.409959,-2.170052,1.057648,-1.525077,-8.050768,-7.541167,5.652594],[2.873044,4.345511,-4.594500,3.066871,9.508245,-1.018648,-4.809174,5.276246,5.760295],[4.552323,9.599790,5.094361,1.447926,3.513019,-6.174198,-5.222775,2.644222,6.409148],[0.398917,5.264085,-3.099294,3.061898,-8.822306,-2.040414,-9.681959,3.714088,-9.270870],[9.113779,-7.075279,-5.037266,2.592665,-3.091388,-8.212152,6.013354,4.752506,-1.991955],[-5.386608,-4.349663,5.466625,1.152961,0.574849,4.805475,0.387265,5.364194,-4.836000]]], dtype = "float64")#candidate|2188|(6, 16, 9)|const|float64
bop_2189 = relay.right_shift(call_2184.astype('int16'), relay.reshape(const_2188.astype('int16'), relay.shape_of(call_2184))) # shape=(6, 16, 9)
bop_2192 = relay.right_shift(call_2186.astype('int16'), relay.reshape(const_2188.astype('int16'), relay.shape_of(call_2186))) # shape=(6, 16, 9)
func_1617_call = mod.get_global_var('func_1617')
func_1620_call = mutated_mod.get_global_var('func_1620')
call_2205 = relay.TupleGetItem(func_1617_call(relay.reshape(call_2182.astype('uint32'), [7, 5, 9])), 0)
call_2206 = relay.TupleGetItem(func_1620_call(relay.reshape(call_2182.astype('uint32'), [7, 5, 9])), 0)
uop_2208 = relay.asin(call_2205.astype('float64')) # shape=(7, 5, 9)
uop_2210 = relay.asin(call_2206.astype('float64')) # shape=(7, 5, 9)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_2216 = func_927_call()
call_2217 = func_927_call()
output = relay.Tuple([call_2127,call_2129,bop_2147,call_2159,call_2168,call_2178,call_2182,const_2185,bop_2189,uop_2208,call_2216,])
output2 = relay.Tuple([call_2128,call_2130,bop_2150,call_2160,call_2169,call_2179,call_2183,const_2185,bop_2192,uop_2210,call_2217,])
func_2220 = relay.Function([var_2146,], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
var_2221 = relay.var("var_2221", dtype = "float64", shape = (9, 3, 2))#candidate|2221|(9, 3, 2)|var|float64
output = func_2220(var_2221)
func_2222 = relay.Function([var_2221], output)
mutated_mod['func_2222'] = func_2222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2226 = relay.var("var_2226", dtype = "float32", shape = (5, 11, 13))#candidate|2226|(5, 11, 13)|var|float32
uop_2227 = relay.log10(var_2226.astype('float32')) # shape=(5, 11, 13)
bop_2236 = relay.floor_divide(uop_2227.astype('float32'), relay.reshape(var_2226.astype('float32'), relay.shape_of(uop_2227))) # shape=(5, 11, 13)
uop_2240 = relay.asin(bop_2236.astype('float64')) # shape=(5, 11, 13)
bop_2243 = relay.greater_equal(uop_2240.astype('bool'), relay.reshape(bop_2236.astype('bool'), relay.shape_of(uop_2240))) # shape=(5, 11, 13)
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_2265 = relay.TupleGetItem(func_1866_call(), 0)
call_2266 = relay.TupleGetItem(func_1867_call(), 0)
uop_2276 = relay.atanh(bop_2243.astype('float64')) # shape=(5, 11, 13)
uop_2281 = relay.sin(uop_2240.astype('float32')) # shape=(5, 11, 13)
uop_2286 = relay.tan(uop_2276.astype('float32')) # shape=(5, 11, 13)
bop_2294 = relay.right_shift(uop_2281.astype('int16'), relay.reshape(uop_2240.astype('int16'), relay.shape_of(uop_2281))) # shape=(5, 11, 13)
bop_2316 = relay.bitwise_xor(bop_2236.astype('uint8'), relay.reshape(var_2226.astype('uint8'), relay.shape_of(bop_2236))) # shape=(5, 11, 13)
bop_2325 = relay.logical_xor(uop_2286.astype('int8'), relay.reshape(uop_2281.astype('int8'), relay.shape_of(uop_2286))) # shape=(5, 11, 13)
uop_2338 = relay.acosh(var_2226.astype('float64')) # shape=(5, 11, 13)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_2343 = func_1097_call()
call_2344 = func_1097_call()
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_2358 = func_719_call()
call_2359 = func_719_call()
uop_2360 = relay.atan(bop_2325.astype('float32')) # shape=(5, 11, 13)
output = relay.Tuple([call_2265,bop_2294,bop_2316,uop_2338,call_2343,call_2358,uop_2360,])
output2 = relay.Tuple([call_2266,bop_2294,bop_2316,uop_2338,call_2344,call_2359,uop_2360,])
func_2363 = relay.Function([var_2226,], output)
mod['func_2363'] = func_2363
mod = relay.transform.InferType()(mod)
var_2364 = relay.var("var_2364", dtype = "float32", shape = (5, 11, 13))#candidate|2364|(5, 11, 13)|var|float32
output = func_2363(var_2364)
func_2365 = relay.Function([var_2364], output)
mutated_mod['func_2365'] = func_2365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1685_call = mod.get_global_var('func_1685')
func_1687_call = mutated_mod.get_global_var('func_1687')
call_2384 = relay.TupleGetItem(func_1685_call(), 0)
call_2385 = relay.TupleGetItem(func_1687_call(), 0)
uop_2395 = relay.log2(call_2384.astype('float32')) # shape=(105,)
uop_2397 = relay.log2(call_2385.astype('float32')) # shape=(105,)
output = relay.Tuple([uop_2395,])
output2 = relay.Tuple([uop_2397,])
func_2409 = relay.Function([], output)
mod['func_2409'] = func_2409
mod = relay.transform.InferType()(mod)
mutated_mod['func_2409'] = func_2409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2409_call = mutated_mod.get_global_var('func_2409')
call_2410 = func_2409_call()
output = call_2410
func_2411 = relay.Function([], output)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_2419 = func_1879_call()
call_2420 = func_1879_call()
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_2423 = relay.TupleGetItem(func_608_call(), 0)
call_2424 = relay.TupleGetItem(func_609_call(), 0)
output = relay.Tuple([call_2419,call_2423,])
output2 = relay.Tuple([call_2420,call_2424,])
func_2437 = relay.Function([], output)
mod['func_2437'] = func_2437
mod = relay.transform.InferType()(mod)
mutated_mod['func_2437'] = func_2437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2437_call = mutated_mod.get_global_var('func_2437')
call_2438 = func_2437_call()
output = call_2438
func_2439 = relay.Function([], output)
mutated_mod['func_2439'] = func_2439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_2444 = relay.TupleGetItem(func_1394_call(), 0)
call_2445 = relay.TupleGetItem(func_1396_call(), 0)
output = call_2444
output2 = call_2445
func_2465 = relay.Function([], output)
mod['func_2465'] = func_2465
mod = relay.transform.InferType()(mod)
output = func_2465()
func_2466 = relay.Function([], output)
mutated_mod['func_2466'] = func_2466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mod.get_global_var('func_638')
func_639_call = mutated_mod.get_global_var('func_639')
call_2482 = relay.TupleGetItem(func_638_call(), 0)
call_2483 = relay.TupleGetItem(func_639_call(), 0)
var_2487 = relay.var("var_2487", dtype = "float64", shape = (5, 16, 3))#candidate|2487|(5, 16, 3)|var|float64
bop_2488 = relay.divide(call_2482.astype('float32'), relay.reshape(var_2487.astype('float32'), relay.shape_of(call_2482))) # shape=(5, 16, 3)
bop_2491 = relay.divide(call_2483.astype('float32'), relay.reshape(var_2487.astype('float32'), relay.shape_of(call_2483))) # shape=(5, 16, 3)
output = bop_2488
output2 = bop_2491
func_2494 = relay.Function([var_2487,], output)
mod['func_2494'] = func_2494
mod = relay.transform.InferType()(mod)
var_2495 = relay.var("var_2495", dtype = "float64", shape = (5, 16, 3))#candidate|2495|(5, 16, 3)|var|float64
output = func_2494(var_2495)
func_2496 = relay.Function([var_2495], output)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1359_call = mod.get_global_var('func_1359')
func_1361_call = mutated_mod.get_global_var('func_1361')
call_2518 = relay.TupleGetItem(func_1359_call(), 2)
call_2519 = relay.TupleGetItem(func_1361_call(), 2)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_2522 = func_1232_call()
call_2523 = func_1232_call()
func_1617_call = mod.get_global_var('func_1617')
func_1620_call = mutated_mod.get_global_var('func_1620')
const_2530 = relay.const([[3,3,-6,-9,-6,3,-2,-4,-7,-8,3,-8,-3,-6,8,-8,-7,10,-1,-4,-3,-7,-6,-4,10,-7,-7,-5,7,3,-3,-8,-9,-8,5,-9,8,7,-5,-8,-3,9,9,-2,5,-4,6,1,-8,8,-10,6,-3,2,4,-4,-5,8,-6,2,8,10,-8,3,-9,-1,-10,-4,2,2,8,-4,8,6,-4,5,-2,10,-5,8,-6,10,-8,10,2,9,-9,-2,-6,-10,5,-6,2,9,-9,-9,5,-2,6,4,-5,10,5,10,8,-4,9,2,-6,-7,9,1,-7,-9,-4,-3,-8,-4,4,-6,5,-7,-2,6,-1,2,-8,6,-3,-10,-7,-9,-5,8,6,-2,-6,7,-10,-3,-5,3,-7,1,-3,8,-4,-5,-9,-10,8,5,-1,-1,5,-1,10,-4,-2,-8,5,-5,2,-10,4,5,-2,-8,-5,3,7,-8,10,6,6,9,10,10,3,-3,10,8,10,-6,-7,5,-4,10,5,-10,-10,2,-10,-1,4,9,-6,7,-5,3,1,7,-8,-3,-5,-6,9,-4,-10,-3,3,-10,9,4,-10,7,4,-7,10,-7,-3,9,-9,-3,2,-5,6,-3,-5,-2,-6,4,-2,2,3,9,2,-7,3,-4,-4,9,6,-8,10,6,8,6,3,3,7,1,2,-4,8,9,7,-3,-1,-6,10,7,-3,9,10,3,4,9,-4,2,-9,3,10,-10,6,1,7,-3,10,-8,3,-8,-7,-4,9,10,-6,5,8,6,1,-7,5,3,-3,-6,2,7,10,-10,-7,7,5,1,7,-5,-7,1,6,9,-4,-8,-8,8,8]], dtype = "uint32")#candidate|2530|(1, 315)|const|uint32
call_2529 = relay.TupleGetItem(func_1617_call(relay.reshape(const_2530.astype('uint32'), [7, 5, 9])), 0)
call_2531 = relay.TupleGetItem(func_1620_call(relay.reshape(const_2530.astype('uint32'), [7, 5, 9])), 0)
func_793_call = mod.get_global_var('func_793')
func_794_call = mutated_mod.get_global_var('func_794')
call_2541 = relay.TupleGetItem(func_793_call(), 0)
call_2542 = relay.TupleGetItem(func_794_call(), 0)
output = relay.Tuple([call_2518,call_2522,call_2529,const_2530,call_2541,])
output2 = relay.Tuple([call_2519,call_2523,call_2531,const_2530,call_2542,])
func_2548 = relay.Function([], output)
mod['func_2548'] = func_2548
mod = relay.transform.InferType()(mod)
output = func_2548()
func_2549 = relay.Function([], output)
mutated_mod['func_2549'] = func_2549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1532_call = mod.get_global_var('func_1532')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_2562 = relay.TupleGetItem(func_1532_call(), 0)
call_2563 = relay.TupleGetItem(func_1533_call(), 0)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_2578 = func_1097_call()
call_2579 = func_1097_call()
output = relay.Tuple([call_2562,call_2578,])
output2 = relay.Tuple([call_2563,call_2579,])
func_2580 = relay.Function([], output)
mod['func_2580'] = func_2580
mod = relay.transform.InferType()(mod)
output = func_2580()
func_2581 = relay.Function([], output)
mutated_mod['func_2581'] = func_2581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_891_call = mod.get_global_var('func_891')
func_892_call = mutated_mod.get_global_var('func_892')
call_2626 = func_891_call()
call_2627 = func_891_call()
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_2641 = relay.TupleGetItem(func_608_call(), 0)
call_2642 = relay.TupleGetItem(func_609_call(), 0)
func_1186_call = mod.get_global_var('func_1186')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_2647 = relay.TupleGetItem(func_1186_call(), 0)
call_2648 = relay.TupleGetItem(func_1188_call(), 0)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_2668 = relay.TupleGetItem(func_1972_call(), 2)
call_2669 = relay.TupleGetItem(func_1973_call(), 2)
output = relay.Tuple([call_2626,call_2641,call_2647,call_2668,])
output2 = relay.Tuple([call_2627,call_2642,call_2648,call_2669,])
func_2674 = relay.Function([], output)
mod['func_2674'] = func_2674
mod = relay.transform.InferType()(mod)
output = func_2674()
func_2675 = relay.Function([], output)
mutated_mod['func_2675'] = func_2675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_2733 = relay.TupleGetItem(func_1866_call(), 0)
call_2734 = relay.TupleGetItem(func_1867_call(), 0)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_2738 = func_1097_call()
call_2739 = func_1097_call()
func_1800_call = mod.get_global_var('func_1800')
func_1804_call = mutated_mod.get_global_var('func_1804')
const_2758 = relay.const([6.216315,-6.995793,-6.717834,4.041593,-4.519140,7.051467,-6.510342,-3.529470,-6.419918,-3.535604,8.751843,-6.899209,-8.973092,9.549463,-1.642230,8.512489,0.214583,8.806174,-1.464701,-3.456983,-3.419185,-5.327361,-0.222491,2.993991,-6.410971,-9.776474,-7.255922,8.224012,-6.214896,-2.993441,-2.054987,0.971503,0.408555,0.562101,3.539211,-2.414289,1.001749,-7.343536,8.142606,-7.390449,8.922950,-2.871457,7.382007,-3.522453,-0.933920,-8.440454,-2.813054,-6.791480,-1.446799,-6.321466,6.505741,-3.330032,1.977471,-2.053505,-1.836164,-4.107018,0.073458,9.523557,-6.988856,5.826885,-8.105540,1.668232,3.528026,9.172221,3.829821,8.282258,-3.072638,9.044375,-7.849331,9.685246,-1.940391,-5.278819,-8.334130,-9.582254,-7.325488,3.305183,5.161877,5.897179,-4.430473,2.062131,-7.339096,-9.901782,-2.899910,2.100674,8.192277,5.978352,-7.668651,-5.279577,-5.459446,-4.287672,-5.279190,4.815979,-0.258667,-8.026585,2.108634,6.638404,-0.581633,4.920473,5.203205,4.030146,2.721136,8.105604,-2.458308,-7.168439,-3.581178,4.600656,-1.373129,3.047198,-0.214429,8.027525,1.037069,5.394309,-5.663818,-5.949245,7.546702,-8.091192,-0.100593,2.836492,4.639058,1.794807], dtype = "float32")#candidate|2758|(120,)|const|float32
call_2757 = func_1800_call(relay.reshape(const_2758.astype('float32'), [3, 5, 8]), relay.reshape(const_2758.astype('float32'), [3, 5, 8]), )
call_2759 = func_1800_call(relay.reshape(const_2758.astype('float32'), [3, 5, 8]), relay.reshape(const_2758.astype('float32'), [3, 5, 8]), )
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_2762 = relay.TupleGetItem(func_1866_call(), 0)
call_2763 = relay.TupleGetItem(func_1867_call(), 0)
output = relay.Tuple([call_2733,call_2738,call_2757,const_2758,call_2762,])
output2 = relay.Tuple([call_2734,call_2739,call_2759,const_2758,call_2763,])
func_2771 = relay.Function([], output)
mod['func_2771'] = func_2771
mod = relay.transform.InferType()(mod)
output = func_2771()
func_2772 = relay.Function([], output)
mutated_mod['func_2772'] = func_2772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2771_call = mod.get_global_var('func_2771')
func_2772_call = mutated_mod.get_global_var('func_2772')
call_2790 = relay.TupleGetItem(func_2771_call(), 1)
call_2791 = relay.TupleGetItem(func_2772_call(), 1)
func_891_call = mod.get_global_var('func_891')
func_892_call = mutated_mod.get_global_var('func_892')
call_2809 = func_891_call()
call_2810 = func_891_call()
func_1719_call = mod.get_global_var('func_1719')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_2814 = relay.TupleGetItem(func_1719_call(), 0)
call_2815 = relay.TupleGetItem(func_1721_call(), 0)
func_2771_call = mod.get_global_var('func_2771')
func_2772_call = mutated_mod.get_global_var('func_2772')
call_2824 = relay.TupleGetItem(func_2771_call(), 4)
call_2825 = relay.TupleGetItem(func_2772_call(), 4)
output = relay.Tuple([call_2790,call_2809,call_2814,call_2824,])
output2 = relay.Tuple([call_2791,call_2810,call_2815,call_2825,])
func_2834 = relay.Function([], output)
mod['func_2834'] = func_2834
mod = relay.transform.InferType()(mod)
output = func_2834()
func_2835 = relay.Function([], output)
mutated_mod['func_2835'] = func_2835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1394_call = mod.get_global_var('func_1394')
func_1396_call = mutated_mod.get_global_var('func_1396')
call_2882 = relay.TupleGetItem(func_1394_call(), 0)
call_2883 = relay.TupleGetItem(func_1396_call(), 0)
output = call_2882
output2 = call_2883
func_2890 = relay.Function([], output)
mod['func_2890'] = func_2890
mod = relay.transform.InferType()(mod)
output = func_2890()
func_2891 = relay.Function([], output)
mutated_mod['func_2891'] = func_2891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2465_call = mod.get_global_var('func_2465')
func_2466_call = mutated_mod.get_global_var('func_2466')
call_2953 = func_2465_call()
call_2954 = func_2465_call()
output = call_2953
output2 = call_2954
func_2956 = relay.Function([], output)
mod['func_2956'] = func_2956
mod = relay.transform.InferType()(mod)
output = func_2956()
func_2957 = relay.Function([], output)
mutated_mod['func_2957'] = func_2957
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3034 = relay.var("var_3034", dtype = "uint32", shape = (16, 3, 16))#candidate|3034|(16, 3, 16)|var|uint32
var_3035 = relay.var("var_3035", dtype = "uint32", shape = (16, 3, 16))#candidate|3035|(16, 3, 16)|var|uint32
bop_3036 = relay.right_shift(var_3034.astype('uint32'), relay.reshape(var_3035.astype('uint32'), relay.shape_of(var_3034))) # shape=(16, 3, 16)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_3044 = relay.TupleGetItem(func_1972_call(), 5)
call_3045 = relay.TupleGetItem(func_1973_call(), 5)
bop_3056 = relay.multiply(bop_3036.astype('uint16'), relay.reshape(var_3034.astype('uint16'), relay.shape_of(bop_3036))) # shape=(16, 3, 16)
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_3059 = relay.TupleGetItem(func_608_call(), 0)
call_3060 = relay.TupleGetItem(func_609_call(), 0)
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
const_3067 = relay.const([4,5,9,-10,1,2,6,-10,-6,1,6,-5,-3,-7,7,-7,10,-8,2,-7,-1,4,1,-10,-10,6,-10,7,5,2,4,4,1,-2,1,-6,8,-4,6,5,-4,-2,-4,-8,6,3,-9,-5,3,3,-7,-10,9,-6,-5,2,4,6,6,-8,-3,-4,2,-3,7,10,-7,8,2,2,5,-9,-2,8,8,-2,-9,-5,6,-7,-6,-6,7,8,6,-9,7,-1,-4,7,-4,-4,7,-5,7,-7,-9,5,-5,-7,6,5,7,-2,-2,4,-8,-1,8,-10,-8,-8,-8,-4,8,7,9,-7,5,-9,6,4,-2,1,-3,-6,5,-9,-9,-7,4,10,3,4,-7,-6,-6,9,9,9,2,-2,-1,2,-4,8,-3,5,-8,-8,2,7,8,8,-9,-9,4,8,4,7,10,-8,-6,1,-2,10,-4,-1,-5,10,-6,5,-2,-7,-4,6,10,7,9,-1,-8,4,-7,4,4,8,-3,-9,-5,-3,1,-2,-3,10,-6,2,1,8,3,-4,6,-6,-4,-3,-1,7,-6,-6,8,1,-6,-2,1,9,-9,-8,2,5,-10,4,-7,-5,1,-1,7,7,-5,2,-6,-9,-3,-2,-2,2,5,3,-10,4,2,-2,-5,4,-5,-7,9,-8,4,1,4,8,-3,3,9,-7,-1,2,10,-10,-2,6,5,-6,-3,-5,-2,10,3,-9,9,5,-6,7,-3,-1,-6,-8,2,-9,3,-3,6,10,-7,2,-8,-7,4,-10,-1,-1,9,-7,5,7,-10,3,-6,-5,-6,8,-6,6,-8,-8,-7,-7,10,9,-10,3,7,-7,-9,-5,-9], dtype = "uint16")#candidate|3067|(315,)|const|uint16
call_3066 = relay.TupleGetItem(func_307_call(relay.reshape(call_3059.astype('uint16'), [15, 1, 7]), relay.reshape(const_3067.astype('uint16'), [15, 3, 7]), ), 1)
call_3068 = relay.TupleGetItem(func_310_call(relay.reshape(call_3059.astype('uint16'), [15, 1, 7]), relay.reshape(const_3067.astype('uint16'), [15, 3, 7]), ), 1)
func_1532_call = mod.get_global_var('func_1532')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_3095 = relay.TupleGetItem(func_1532_call(), 0)
call_3096 = relay.TupleGetItem(func_1533_call(), 0)
output = relay.Tuple([call_3044,bop_3056,call_3059,call_3066,const_3067,call_3095,])
output2 = relay.Tuple([call_3045,bop_3056,call_3060,call_3068,const_3067,call_3096,])
func_3102 = relay.Function([var_3034,var_3035,], output)
mod['func_3102'] = func_3102
mod = relay.transform.InferType()(mod)
var_3103 = relay.var("var_3103", dtype = "uint32", shape = (16, 3, 16))#candidate|3103|(16, 3, 16)|var|uint32
var_3104 = relay.var("var_3104", dtype = "uint32", shape = (16, 3, 16))#candidate|3104|(16, 3, 16)|var|uint32
output = func_3102(var_3103,var_3104,)
func_3105 = relay.Function([var_3103,var_3104,], output)
mutated_mod['func_3105'] = func_3105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_3107 = relay.TupleGetItem(func_2548_call(), 4)
call_3108 = relay.TupleGetItem(func_2549_call(), 4)
output = call_3107
output2 = call_3108
func_3117 = relay.Function([], output)
mod['func_3117'] = func_3117
mod = relay.transform.InferType()(mod)
mutated_mod['func_3117'] = func_3117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3117_call = mutated_mod.get_global_var('func_3117')
call_3118 = func_3117_call()
output = call_3118
func_3119 = relay.Function([], output)
mutated_mod['func_3119'] = func_3119
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3150 = relay.var("var_3150", dtype = "uint8", shape = (4, 11, 10))#candidate|3150|(4, 11, 10)|var|uint8
var_3151 = relay.var("var_3151", dtype = "uint8", shape = (4, 11, 10))#candidate|3151|(4, 11, 10)|var|uint8
bop_3152 = relay.equal(var_3150.astype('bool'), relay.reshape(var_3151.astype('bool'), relay.shape_of(var_3150))) # shape=(4, 11, 10)
bop_3159 = relay.not_equal(var_3151.astype('bool'), relay.reshape(var_3150.astype('bool'), relay.shape_of(var_3151))) # shape=(4, 11, 10)
output = relay.Tuple([bop_3152,bop_3159,])
output2 = relay.Tuple([bop_3152,bop_3159,])
func_3163 = relay.Function([var_3150,var_3151,], output)
mod['func_3163'] = func_3163
mod = relay.transform.InferType()(mod)
mutated_mod['func_3163'] = func_3163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3163_call = mutated_mod.get_global_var('func_3163')
var_3165 = relay.var("var_3165", dtype = "uint8", shape = (4, 11, 10))#candidate|3165|(4, 11, 10)|var|uint8
var_3166 = relay.var("var_3166", dtype = "uint8", shape = (4, 11, 10))#candidate|3166|(4, 11, 10)|var|uint8
call_3164 = func_3163_call(var_3165,var_3166,)
output = call_3164
func_3167 = relay.Function([var_3165,var_3166,], output)
mutated_mod['func_3167'] = func_3167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1286_call = mod.get_global_var('func_1286')
func_1288_call = mutated_mod.get_global_var('func_1288')
call_3179 = relay.TupleGetItem(func_1286_call(), 0)
call_3180 = relay.TupleGetItem(func_1288_call(), 0)
output = call_3179
output2 = call_3180
func_3194 = relay.Function([], output)
mod['func_3194'] = func_3194
mod = relay.transform.InferType()(mod)
mutated_mod['func_3194'] = func_3194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3194_call = mutated_mod.get_global_var('func_3194')
call_3195 = func_3194_call()
output = call_3195
func_3196 = relay.Function([], output)
mutated_mod['func_3196'] = func_3196
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3209 = relay.var("var_3209", dtype = "float64", shape = (10, 13, 16))#candidate|3209|(10, 13, 16)|var|float64
uop_3210 = relay.erf(var_3209.astype('float64')) # shape=(10, 13, 16)
uop_3212 = relay.cosh(var_3209.astype('float32')) # shape=(10, 13, 16)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_3215 = func_927_call()
call_3216 = func_927_call()
bop_3238 = relay.logical_or(uop_3210.astype('bool'), relay.reshape(uop_3212.astype('bool'), relay.shape_of(uop_3210))) # shape=(10, 13, 16)
uop_3249 = relay.tan(var_3209.astype('float64')) # shape=(10, 13, 16)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_3258 = relay.TupleGetItem(func_1972_call(), 5)
call_3259 = relay.TupleGetItem(func_1973_call(), 5)
output = relay.Tuple([call_3215,bop_3238,uop_3249,call_3258,])
output2 = relay.Tuple([call_3216,bop_3238,uop_3249,call_3259,])
func_3262 = relay.Function([var_3209,], output)
mod['func_3262'] = func_3262
mod = relay.transform.InferType()(mod)
var_3263 = relay.var("var_3263", dtype = "float64", shape = (10, 13, 16))#candidate|3263|(10, 13, 16)|var|float64
output = func_3262(var_3263)
func_3264 = relay.Function([var_3263], output)
mutated_mod['func_3264'] = func_3264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2437_call = mod.get_global_var('func_2437')
func_2439_call = mutated_mod.get_global_var('func_2439')
call_3300 = relay.TupleGetItem(func_2437_call(), 1)
call_3301 = relay.TupleGetItem(func_2439_call(), 1)
func_2890_call = mod.get_global_var('func_2890')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_3303 = func_2890_call()
call_3304 = func_2890_call()
output = relay.Tuple([call_3300,call_3303,])
output2 = relay.Tuple([call_3301,call_3304,])
func_3307 = relay.Function([], output)
mod['func_3307'] = func_3307
mod = relay.transform.InferType()(mod)
output = func_3307()
func_3308 = relay.Function([], output)
mutated_mod['func_3308'] = func_3308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_3320 = func_719_call()
call_3321 = func_719_call()
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_3333 = relay.TupleGetItem(func_1866_call(), 0)
call_3334 = relay.TupleGetItem(func_1867_call(), 0)
output = relay.Tuple([call_3320,call_3333,])
output2 = relay.Tuple([call_3321,call_3334,])
func_3337 = relay.Function([], output)
mod['func_3337'] = func_3337
mod = relay.transform.InferType()(mod)
output = func_3337()
func_3338 = relay.Function([], output)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_3357 = func_1879_call()
call_3358 = func_1879_call()
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_3359 = relay.TupleGetItem(func_1972_call(), 1)
call_3360 = relay.TupleGetItem(func_1973_call(), 1)
output = relay.Tuple([call_3357,call_3359,])
output2 = relay.Tuple([call_3358,call_3360,])
func_3395 = relay.Function([], output)
mod['func_3395'] = func_3395
mod = relay.transform.InferType()(mod)
output = func_3395()
func_3396 = relay.Function([], output)
mutated_mod['func_3396'] = func_3396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_3405 = relay.TupleGetItem(func_1866_call(), 0)
call_3406 = relay.TupleGetItem(func_1867_call(), 0)
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_3414 = func_1879_call()
call_3415 = func_1879_call()
output = relay.Tuple([call_3405,call_3414,])
output2 = relay.Tuple([call_3406,call_3415,])
func_3416 = relay.Function([], output)
mod['func_3416'] = func_3416
mod = relay.transform.InferType()(mod)
mutated_mod['func_3416'] = func_3416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3416_call = mutated_mod.get_global_var('func_3416')
call_3417 = func_3416_call()
output = call_3417
func_3418 = relay.Function([], output)
mutated_mod['func_3418'] = func_3418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2437_call = mod.get_global_var('func_2437')
func_2439_call = mutated_mod.get_global_var('func_2439')
call_3441 = relay.TupleGetItem(func_2437_call(), 0)
call_3442 = relay.TupleGetItem(func_2439_call(), 0)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
var_3447 = relay.var("var_3447", dtype = "float64", shape = (2, 720))#candidate|3447|(2, 720)|var|float64
call_3446 = relay.TupleGetItem(func_709_call(relay.reshape(var_3447.astype('float64'), [12, 15, 8])), 0)
call_3448 = relay.TupleGetItem(func_711_call(relay.reshape(var_3447.astype('float64'), [12, 15, 8])), 0)
output = relay.Tuple([call_3441,call_3446,var_3447,])
output2 = relay.Tuple([call_3442,call_3448,var_3447,])
func_3449 = relay.Function([var_3447,], output)
mod['func_3449'] = func_3449
mod = relay.transform.InferType()(mod)
var_3450 = relay.var("var_3450", dtype = "float64", shape = (2, 720))#candidate|3450|(2, 720)|var|float64
output = func_3449(var_3450)
func_3451 = relay.Function([var_3450], output)
mutated_mod['func_3451'] = func_3451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_3507 = relay.TupleGetItem(func_1972_call(), 1)
call_3508 = relay.TupleGetItem(func_1973_call(), 1)
output = relay.Tuple([call_3507,])
output2 = relay.Tuple([call_3508,])
func_3514 = relay.Function([], output)
mod['func_3514'] = func_3514
mod = relay.transform.InferType()(mod)
output = func_3514()
func_3515 = relay.Function([], output)
mutated_mod['func_3515'] = func_3515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_3536 = func_1097_call()
call_3537 = func_1097_call()
func_3194_call = mod.get_global_var('func_3194')
func_3196_call = mutated_mod.get_global_var('func_3196')
call_3550 = func_3194_call()
call_3551 = func_3194_call()
output = relay.Tuple([call_3536,call_3550,])
output2 = relay.Tuple([call_3537,call_3551,])
func_3559 = relay.Function([], output)
mod['func_3559'] = func_3559
mod = relay.transform.InferType()(mod)
mutated_mod['func_3559'] = func_3559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3559_call = mutated_mod.get_global_var('func_3559')
call_3560 = func_3559_call()
output = call_3560
func_3561 = relay.Function([], output)
mutated_mod['func_3561'] = func_3561
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3607 = relay.var("var_3607", dtype = "uint16", shape = (3, 4, 8))#candidate|3607|(3, 4, 8)|var|uint16
var_3608 = relay.var("var_3608", dtype = "uint16", shape = (3, 4, 8))#candidate|3608|(3, 4, 8)|var|uint16
bop_3609 = relay.bitwise_xor(var_3607.astype('uint16'), relay.reshape(var_3608.astype('uint16'), relay.shape_of(var_3607))) # shape=(3, 4, 8)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_3614 = func_1097_call()
call_3615 = func_1097_call()
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_3628 = func_719_call()
call_3629 = func_719_call()
output = relay.Tuple([bop_3609,call_3614,call_3628,])
output2 = relay.Tuple([bop_3609,call_3615,call_3629,])
func_3648 = relay.Function([var_3607,var_3608,], output)
mod['func_3648'] = func_3648
mod = relay.transform.InferType()(mod)
mutated_mod['func_3648'] = func_3648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3648_call = mutated_mod.get_global_var('func_3648')
var_3650 = relay.var("var_3650", dtype = "uint16", shape = (3, 4, 8))#candidate|3650|(3, 4, 8)|var|uint16
var_3651 = relay.var("var_3651", dtype = "uint16", shape = (3, 4, 8))#candidate|3651|(3, 4, 8)|var|uint16
call_3649 = func_3648_call(var_3650,var_3651,)
output = call_3649
func_3652 = relay.Function([var_3650,var_3651,], output)
mutated_mod['func_3652'] = func_3652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mod.get_global_var('func_3514')
func_3515_call = mutated_mod.get_global_var('func_3515')
call_3664 = relay.TupleGetItem(func_3514_call(), 0)
call_3665 = relay.TupleGetItem(func_3515_call(), 0)
output = call_3664
output2 = call_3665
func_3666 = relay.Function([], output)
mod['func_3666'] = func_3666
mod = relay.transform.InferType()(mod)
output = func_3666()
func_3667 = relay.Function([], output)
mutated_mod['func_3667'] = func_3667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3666_call = mod.get_global_var('func_3666')
func_3667_call = mutated_mod.get_global_var('func_3667')
call_3692 = func_3666_call()
call_3693 = func_3666_call()
output = relay.Tuple([call_3692,])
output2 = relay.Tuple([call_3693,])
func_3698 = relay.Function([], output)
mod['func_3698'] = func_3698
mod = relay.transform.InferType()(mod)
mutated_mod['func_3698'] = func_3698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3698_call = mutated_mod.get_global_var('func_3698')
call_3699 = func_3698_call()
output = call_3699
func_3700 = relay.Function([], output)
mutated_mod['func_3700'] = func_3700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_3867 = func_1879_call()
call_3868 = func_1879_call()
var_3869 = relay.var("var_3869", dtype = "float32", shape = (315,))#candidate|3869|(315,)|var|float32
bop_3870 = relay.logical_xor(call_3867.astype('uint64'), relay.reshape(var_3869.astype('uint64'), relay.shape_of(call_3867))) # shape=(315,)
bop_3873 = relay.logical_xor(call_3868.astype('uint64'), relay.reshape(var_3869.astype('uint64'), relay.shape_of(call_3868))) # shape=(315,)
bop_3881 = relay.not_equal(call_3867.astype('bool'), relay.reshape(var_3869.astype('bool'), relay.shape_of(call_3867))) # shape=(315,)
bop_3884 = relay.not_equal(call_3868.astype('bool'), relay.reshape(var_3869.astype('bool'), relay.shape_of(call_3868))) # shape=(315,)
func_1532_call = mod.get_global_var('func_1532')
func_1533_call = mutated_mod.get_global_var('func_1533')
call_3885 = relay.TupleGetItem(func_1532_call(), 0)
call_3886 = relay.TupleGetItem(func_1533_call(), 0)
bop_3887 = relay.multiply(call_3867.astype('float64'), relay.reshape(var_3869.astype('float64'), relay.shape_of(call_3867))) # shape=(315,)
bop_3890 = relay.multiply(call_3868.astype('float64'), relay.reshape(var_3869.astype('float64'), relay.shape_of(call_3868))) # shape=(315,)
var_3891 = relay.var("var_3891", dtype = "float32", shape = (315,))#candidate|3891|(315,)|var|float32
bop_3892 = relay.floor_mod(call_3867.astype('float64'), relay.reshape(var_3891.astype('float64'), relay.shape_of(call_3867))) # shape=(315,)
bop_3895 = relay.floor_mod(call_3868.astype('float64'), relay.reshape(var_3891.astype('float64'), relay.shape_of(call_3868))) # shape=(315,)
output = relay.Tuple([bop_3870,bop_3881,call_3885,bop_3887,bop_3892,])
output2 = relay.Tuple([bop_3873,bop_3884,call_3886,bop_3890,bop_3895,])
func_3911 = relay.Function([var_3869,var_3891,], output)
mod['func_3911'] = func_3911
mod = relay.transform.InferType()(mod)
var_3912 = relay.var("var_3912", dtype = "float32", shape = (315,))#candidate|3912|(315,)|var|float32
var_3913 = relay.var("var_3913", dtype = "float32", shape = (315,))#candidate|3913|(315,)|var|float32
output = func_3911(var_3912,var_3913,)
func_3914 = relay.Function([var_3912,var_3913,], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_3953 = relay.TupleGetItem(func_2409_call(), 0)
call_3954 = relay.TupleGetItem(func_2411_call(), 0)
output = call_3953
output2 = call_3954
func_3963 = relay.Function([], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
output = func_3963()
func_3964 = relay.Function([], output)
mutated_mod['func_3964'] = func_3964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_3997 = func_1097_call()
call_3998 = func_1097_call()
output = relay.Tuple([call_3997,])
output2 = relay.Tuple([call_3998,])
func_4020 = relay.Function([], output)
mod['func_4020'] = func_4020
mod = relay.transform.InferType()(mod)
output = func_4020()
func_4021 = relay.Function([], output)
mutated_mod['func_4021'] = func_4021
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4068 = relay.const([[[5.339503,-1.080631,8.366160,9.863861,0.277707,4.045212,-2.026713,-1.684878,4.269687,4.124774,-5.151667],[8.342674,6.406076,2.129119,6.369843,-1.824985,1.780468,8.865177,-2.765887,4.714806,8.107455,4.244975],[-5.938376,8.412566,-9.458804,-2.458576,-5.472432,7.381608,-0.026710,-6.674367,8.848956,-9.463031,3.500404],[-1.824728,4.894321,8.944080,-2.874172,-0.357418,-4.866171,-7.801832,-6.399139,-4.648706,2.504703,-5.389399],[-3.455974,5.335341,3.170675,-1.077604,8.004570,5.476906,-1.877252,-1.267266,6.665239,9.024781,-8.518422],[0.308914,5.869893,2.974403,6.466351,-6.466569,0.539031,-4.964846,-3.839704,9.482322,6.674935,-9.218819],[-5.572012,-7.429418,4.450962,3.228367,-1.387685,-6.368049,-1.632061,-7.170828,7.802135,3.891032,-7.542404],[-5.222783,-7.517432,5.026726,-6.867222,3.186229,-4.151572,-2.597391,-0.496673,9.593166,-9.235152,-2.514854],[5.629550,5.069945,2.673311,3.680579,-9.145301,-0.979206,-2.097010,-4.987669,8.389176,5.234115,2.926908],[3.004080,8.449046,-5.211492,-9.806264,2.439528,7.547747,9.692335,7.845956,7.199926,-0.033776,4.316930],[6.664661,5.891451,9.609713,-9.078583,-2.816592,-6.959742,-0.473783,-8.092573,1.823527,-0.419754,-7.091506],[-6.595264,6.407119,6.893074,7.676879,-5.967350,-8.213498,-3.539244,-8.504634,-5.870878,-8.707684,-3.811690],[-9.956428,-3.334835,-1.378755,-4.647122,-3.987789,3.300794,-1.479409,8.459852,7.653991,-3.318120,6.527129]],[[2.404555,1.849154,-9.342653,8.906482,-4.352511,5.251928,1.463321,-9.020385,-4.531555,-7.571163,-8.951294],[-1.609718,5.102819,7.898029,5.105774,-3.715136,-9.331083,6.243892,2.820092,2.712139,-4.910079,-9.922529],[9.784012,3.547747,9.197473,5.039089,9.590777,2.694460,0.861168,-6.618087,6.798200,2.929059,6.884297],[8.474144,9.358416,-5.171556,4.711978,-9.027495,7.712152,9.798412,3.926287,-0.738060,-1.455922,9.359116],[-7.718674,3.593821,-2.343944,3.191723,2.185619,9.113516,-4.197113,-4.556902,-9.727887,-8.157379,-2.138151],[8.086190,-3.992716,-9.614288,3.902182,-7.039112,-5.775262,-5.989434,-0.850940,-0.286329,-4.862910,9.873859],[1.006849,-4.645035,-2.093437,-2.442777,-0.241051,-0.518421,7.978844,-6.578581,0.942241,1.433498,-9.805746],[-5.992379,1.901945,-7.024167,-1.587454,-5.162095,4.941378,-8.178071,8.375152,-2.697770,-7.123383,-3.748957],[-7.835339,-1.462772,5.521745,0.508831,8.852434,7.294207,-5.824421,-5.719922,9.480103,-0.778373,-4.071237],[-0.545504,4.385824,2.496933,0.396771,-3.481057,-8.292593,4.575658,-2.426567,9.935537,2.699463,-1.680277],[-9.070011,-7.218452,-4.455773,-5.182845,2.301148,-0.276636,-2.282985,-6.678177,-8.364112,3.757245,-0.757406],[-5.790423,3.347477,-7.771825,-7.003938,-9.821720,-5.224265,-4.373997,8.387105,2.916697,4.334985,-0.598205],[3.221082,-7.492561,9.159445,9.873930,-7.889093,-7.784646,9.281637,-9.875223,9.652693,3.157258,-3.531252]],[[-4.947116,-6.027499,-0.597080,-6.972387,6.645432,-6.843040,2.667957,1.111764,8.541515,-1.986698,9.265420],[-5.656777,-2.801843,-8.947497,7.493810,9.302680,4.753280,8.224467,-2.706150,-0.852870,-7.837534,3.311497],[-6.090273,-0.381130,-5.892731,5.682611,-8.125314,-3.003830,9.287017,-7.504895,2.898248,8.182298,-5.881150],[-7.600267,-8.006684,-1.241604,2.017284,-5.912660,0.543129,5.562385,9.983402,0.934136,7.090496,-0.779485],[0.673033,6.321857,2.727240,7.944479,-3.452525,-0.045954,-6.313556,9.616848,-9.724571,9.134862,-9.060716],[0.292637,7.912808,7.821674,-5.639748,6.819006,4.352775,-1.227594,7.393619,-9.252532,-3.973360,-6.785959],[9.097094,-3.218097,0.068749,2.876350,9.461954,-6.542949,-7.539996,2.805382,3.620595,-0.314631,9.989100],[7.485190,-7.539591,-6.006340,-3.234374,7.524445,-4.755536,0.202390,5.284412,1.721210,-1.985705,4.538784],[-9.029457,4.914537,8.043684,-0.440882,8.425129,-3.950425,0.417488,-2.107454,8.234537,0.296059,5.593261],[-5.694117,-4.770103,9.597317,3.873690,9.447267,6.637493,2.466713,-2.002519,-3.065213,-4.729446,5.779149],[7.468776,1.331919,4.870035,4.418911,-0.376354,6.108012,3.705120,9.547995,3.721219,-0.336160,0.091218],[2.601695,2.285713,4.201147,-4.824281,9.710343,-5.391258,4.815266,-2.839546,9.307690,-5.300839,9.792041],[5.586895,-0.947815,3.991335,-2.248907,-8.162973,-8.740630,7.431539,0.716973,-9.428635,2.352744,-9.380533]],[[-1.333697,4.776857,4.279639,-7.765576,-5.835282,0.285444,-9.197111,2.363738,5.518271,-0.593764,-1.735130],[-9.002108,-0.959831,-4.222965,1.641155,-7.607032,1.891891,4.908208,1.308675,9.221492,-0.034931,-2.716405],[0.616912,5.853388,2.860268,-6.134361,1.624955,-6.341122,3.938948,5.720492,2.179559,-3.347879,-9.616731],[6.478083,3.217739,0.103838,6.179200,-8.139651,7.220344,8.798181,-8.072172,-1.778693,-9.335429,8.110821],[-8.776167,2.880983,-2.268987,-9.192833,0.815713,-6.838345,6.368978,-7.559042,0.136950,2.390370,-7.136294],[4.598289,5.795655,-4.865350,-8.916663,1.424908,3.464215,-1.549862,6.068414,-3.804316,-8.882190,9.387036],[-8.024307,-2.272919,2.873508,-2.248351,4.109274,-7.876065,-7.247862,-4.012082,-9.104658,7.176132,-6.470691],[3.601116,-5.961827,2.686918,-5.771123,-1.369524,-6.992255,-5.257247,6.721674,-5.401307,-9.691056,4.962152],[6.742949,-6.951858,3.745590,1.623175,5.816147,8.601979,-4.417590,5.297442,-7.865400,8.108461,-4.392006],[-4.187620,2.671007,-6.731517,9.106439,-3.880495,-1.069539,-4.289715,-0.859998,3.915302,-1.155485,4.188961],[6.662279,8.471194,0.965165,7.247638,-7.006880,8.539614,-9.838196,2.661008,2.327955,-9.418496,-1.328314],[1.448287,1.806074,8.240313,-2.704462,-2.031802,2.066608,3.813016,6.182356,-4.983438,-6.335327,8.964109],[-4.765465,-9.336204,-2.273123,5.493636,9.845736,7.353143,6.537057,-9.432741,5.703417,-1.854311,-6.257356]],[[0.699971,-0.171340,2.756407,0.956215,8.960121,4.586310,9.220387,-8.889650,4.276472,-1.234347,-5.272373],[8.011689,1.328294,-1.398317,3.183855,8.286993,-5.990612,-7.060869,-3.285323,-1.838613,0.823076,4.407852],[6.478112,1.751602,4.139429,3.352134,-0.642085,-0.203182,2.219409,6.827121,4.101630,-6.340586,-1.138973],[0.962676,-5.689635,-4.530075,4.371981,7.151792,7.359164,4.086186,-9.858763,6.564896,6.076231,-0.391811],[-5.039596,1.746692,-8.886296,9.547555,6.641823,3.718742,-5.063919,8.657929,2.262365,-6.253877,-1.057873],[2.785714,-7.427582,5.725900,-2.634008,-9.407909,6.800075,-2.219263,3.639765,-3.529518,-3.801774,6.132849],[8.167288,-5.226530,0.825563,8.433047,8.805694,-4.341260,0.656080,2.284487,2.703516,-7.898331,-1.301260],[-8.399875,-5.259243,-2.588637,-4.127203,1.676471,-4.647616,-0.141789,-1.093251,6.501118,-8.164239,7.534520],[1.294772,9.744581,1.040067,7.208510,-1.894663,9.257219,-8.909820,8.262659,3.679157,-7.647452,-9.054786],[1.643170,6.639284,-5.490158,-9.732440,1.636054,3.551701,-8.229082,4.260811,-6.721955,1.695197,-9.881597],[9.725066,-5.519717,3.815462,-2.479403,8.474195,-2.423434,7.095773,-5.290134,4.993678,2.882835,-4.518436],[0.880898,-2.501193,1.548232,6.804584,9.078356,3.616121,-8.644174,3.579126,7.969961,-8.575784,6.785831],[-6.465944,-8.931378,2.917801,-8.619526,5.898375,6.762483,1.330832,-7.312396,7.816927,1.537894,3.862599]],[[8.567483,8.671631,-6.291415,-9.053201,7.739071,1.264214,-2.604742,1.913731,9.236970,-2.091547,-3.462999],[6.905691,7.180020,8.212454,-7.273507,-5.106099,4.472149,-2.690247,6.747545,7.176748,4.092784,-8.121721],[0.370397,9.040991,0.669697,-5.773318,7.157305,-4.088344,-9.247113,-1.434774,-5.821185,-2.693046,-0.400250],[5.935609,0.420851,-1.711167,-6.024350,5.507463,-7.729378,-4.611116,-1.489333,-5.764207,-5.028069,-6.426249],[-8.346826,3.248190,1.458001,-1.099464,-9.407820,-2.761991,-0.198142,5.076666,1.898251,-4.331455,0.133672],[8.266115,7.640313,7.210835,-1.452528,-7.112804,-4.772842,-7.339665,9.105796,2.724504,-4.377646,-1.798265],[-7.096638,9.966501,-5.322162,-4.381225,-1.635650,3.496361,3.825065,-1.880588,4.683097,-9.401170,-7.726820],[7.909065,1.274764,-8.942577,-3.486198,-7.911411,-5.540755,5.705294,2.853372,-3.397388,5.234833,-1.160491],[-6.467332,8.569321,7.989361,-3.350639,-1.758432,-8.614411,-5.037790,2.163229,8.347993,-2.448542,-1.948830],[-6.468151,8.065455,7.380796,-6.974675,7.444029,-7.097930,-6.147144,-6.454019,-8.280955,4.511039,-0.563676],[7.659565,-9.495244,5.340535,-9.613792,-3.560257,1.728063,7.809505,8.774203,-8.694358,-6.560006,7.176719],[8.600546,0.448105,-9.253301,-3.227987,4.043900,-7.201983,-2.512863,-2.203378,8.545784,3.073336,-3.575434],[-9.098439,-1.821016,-0.039657,7.799138,-7.032474,7.525484,-7.571837,-0.322124,-0.418229,-6.424028,9.826336]],[[-4.833689,6.327434,4.841016,-6.098629,6.882958,1.462771,-0.381608,8.695966,4.055908,-2.983992,8.420068],[-6.274009,4.573187,6.971493,3.527148,-7.397830,-8.974478,-4.455164,-5.207686,0.740712,2.708255,4.127823],[-6.699566,5.239601,-9.611209,-7.791525,7.902656,3.212049,3.631119,-8.313660,-1.011692,-1.035738,4.423793],[-8.467003,-6.589041,8.372909,-6.171166,5.630702,7.276371,-7.385311,-8.470607,-2.296343,7.837129,-9.134826],[-2.943787,5.578111,6.989040,-6.945496,-7.236272,-8.192291,-5.696880,-9.471532,-3.899623,-9.106486,1.770034],[-1.872130,8.897642,6.852051,-8.211264,-4.298537,-0.231598,3.161962,2.133415,-8.336457,-6.783881,-3.238502],[6.384114,9.506642,-8.711738,6.147423,-7.504980,9.862497,-3.633903,-2.021438,-1.556910,-3.722398,3.551701],[-4.677645,3.998336,-8.334578,3.687731,-1.470716,-2.141727,5.312688,7.522776,-1.761125,-2.882209,-5.915504],[-7.265255,0.709717,9.663863,3.754143,-7.407595,8.660825,1.289434,8.153100,9.256701,9.594566,-9.401791],[-8.180111,5.184053,3.259249,3.227882,3.479962,8.788323,-5.760827,-1.870038,4.922466,-4.776308,-2.052215],[-4.018496,-8.994549,3.230420,2.922241,-8.553719,-2.902182,-4.749126,5.257949,2.342016,5.356020,-4.016059],[1.809535,-5.901982,9.476195,0.873927,-3.768594,9.188924,2.318862,-6.856655,-6.898758,6.204527,-1.265369],[7.718008,6.354920,-4.438408,1.090244,-4.197459,7.591770,5.825939,3.659495,-0.019587,-9.169202,7.601418]],[[0.289902,3.260807,-4.731858,-9.802164,-8.686693,4.510941,-5.181090,6.713632,-5.656459,-2.179347,-5.138589],[-2.149093,-9.648204,9.658101,-1.407467,0.132189,-0.181626,-1.706978,7.553848,7.448819,-0.367007,0.321118],[5.040731,-0.621296,-8.782578,9.667045,-1.517029,8.275552,7.271656,8.937122,5.266944,0.794649,3.690380],[-8.499017,-4.297959,8.292997,-8.715051,2.632777,3.561939,1.421662,-0.045541,-3.992877,-1.662803,7.850794],[-6.972759,-0.290050,9.294897,8.280238,1.351042,1.384923,9.639228,-2.868836,2.969274,4.487836,4.148114],[9.655131,-6.885720,-3.309461,6.192120,-8.787931,-1.556056,5.829549,-5.275595,9.070027,-7.177922,9.252213],[7.372536,-9.645583,3.293894,5.994561,-8.844038,-2.429347,-2.320886,-7.471735,-7.541619,3.752822,9.545861],[1.862083,6.302487,1.331491,4.758303,6.393059,-9.322162,-2.448188,-8.277228,-1.472428,-2.044874,0.232753],[7.693065,-6.139486,-8.346599,-5.084611,-3.928761,4.250066,-5.461937,0.895576,4.792940,-4.091182,-2.365576],[9.906174,-8.541144,-3.716531,-1.104165,9.055040,8.111743,5.265189,8.302719,1.919260,7.514118,2.861359],[5.044326,-5.636853,-8.855588,-2.353863,3.201025,4.761781,2.547583,-1.172240,5.428254,5.973087,9.305855],[-3.227470,-4.772043,-8.003730,-3.274512,-4.761140,-6.199088,-1.876073,4.384766,-9.057303,-5.362646,9.718820],[7.020463,2.742038,8.541897,8.827876,2.584616,-8.176705,1.769339,-2.685030,-4.363807,4.923898,2.940258]]], dtype = "float64")#candidate|4068|(8, 13, 11)|const|float64
uop_4069 = relay.log10(const_4068.astype('float64')) # shape=(8, 13, 11)
output = relay.Tuple([uop_4069,])
output2 = relay.Tuple([uop_4069,])
func_4079 = relay.Function([], output)
mod['func_4079'] = func_4079
mod = relay.transform.InferType()(mod)
mutated_mod['func_4079'] = func_4079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4079_call = mutated_mod.get_global_var('func_4079')
call_4080 = func_4079_call()
output = call_4080
func_4081 = relay.Function([], output)
mutated_mod['func_4081'] = func_4081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_4089 = func_1232_call()
call_4090 = func_1232_call()
var_4094 = relay.var("var_4094", dtype = "uint16", shape = (105,))#candidate|4094|(105,)|var|uint16
bop_4095 = relay.equal(call_4089.astype('bool'), relay.reshape(var_4094.astype('bool'), relay.shape_of(call_4089))) # shape=(105,)
bop_4098 = relay.equal(call_4090.astype('bool'), relay.reshape(var_4094.astype('bool'), relay.shape_of(call_4090))) # shape=(105,)
output = bop_4095
output2 = bop_4098
func_4100 = relay.Function([var_4094,], output)
mod['func_4100'] = func_4100
mod = relay.transform.InferType()(mod)
mutated_mod['func_4100'] = func_4100
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4101 = relay.var("var_4101", dtype = "uint16", shape = (105,))#candidate|4101|(105,)|var|uint16
func_4100_call = mutated_mod.get_global_var('func_4100')
call_4102 = func_4100_call(var_4101)
output = call_4102
func_4103 = relay.Function([var_4101], output)
mutated_mod['func_4103'] = func_4103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_4133 = relay.TupleGetItem(func_2548_call(), 1)
call_4134 = relay.TupleGetItem(func_2549_call(), 1)
output = relay.Tuple([call_4133,])
output2 = relay.Tuple([call_4134,])
func_4145 = relay.Function([], output)
mod['func_4145'] = func_4145
mod = relay.transform.InferType()(mod)
output = func_4145()
func_4146 = relay.Function([], output)
mutated_mod['func_4146'] = func_4146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3307_call = mod.get_global_var('func_3307')
func_3308_call = mutated_mod.get_global_var('func_3308')
call_4151 = relay.TupleGetItem(func_3307_call(), 1)
call_4152 = relay.TupleGetItem(func_3308_call(), 1)
output = call_4151
output2 = call_4152
func_4154 = relay.Function([], output)
mod['func_4154'] = func_4154
mod = relay.transform.InferType()(mod)
mutated_mod['func_4154'] = func_4154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mutated_mod.get_global_var('func_4154')
call_4155 = func_4154_call()
output = call_4155
func_4156 = relay.Function([], output)
mutated_mod['func_4156'] = func_4156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_638_call = mod.get_global_var('func_638')
func_639_call = mutated_mod.get_global_var('func_639')
call_4181 = relay.TupleGetItem(func_638_call(), 1)
call_4182 = relay.TupleGetItem(func_639_call(), 1)
output = relay.Tuple([call_4181,])
output2 = relay.Tuple([call_4182,])
func_4188 = relay.Function([], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
mutated_mod['func_4188'] = func_4188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mutated_mod.get_global_var('func_4188')
call_4189 = func_4188_call()
output = call_4189
func_4190 = relay.Function([], output)
mutated_mod['func_4190'] = func_4190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_4191 = func_719_call()
call_4192 = func_719_call()
output = relay.Tuple([call_4191,])
output2 = relay.Tuple([call_4192,])
func_4193 = relay.Function([], output)
mod['func_4193'] = func_4193
mod = relay.transform.InferType()(mod)
output = func_4193()
func_4194 = relay.Function([], output)
mutated_mod['func_4194'] = func_4194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4020_call = mod.get_global_var('func_4020')
func_4021_call = mutated_mod.get_global_var('func_4021')
call_4218 = relay.TupleGetItem(func_4020_call(), 0)
call_4219 = relay.TupleGetItem(func_4021_call(), 0)
func_2105_call = mod.get_global_var('func_2105')
func_2108_call = mutated_mod.get_global_var('func_2108')
const_4231 = relay.const([-4.216454,8.411481,-4.508832,-4.776787,5.066972,6.101054,-9.613120,-0.544483,-1.697577,-8.876493,-0.482515,3.516680,3.893347,6.983437,-2.005499,3.914071,-9.350296,-7.863563,8.385480,-2.167983,8.294242,-6.019426,-9.668370,-5.434708,5.858751,3.923705,-9.358144,-1.596742,-0.464279,-5.665083,-8.415565,9.967822,4.560632,2.396670,-0.752220,3.660328,1.637020,-4.352930,1.303551,-5.856029,4.882701,-7.299055,-7.111012,3.359456,-4.735771,-8.897362,0.024201,0.488717,2.744479,1.019739,-5.448379,8.517223,-2.533221,-1.852762,-7.581462,-5.791318,-0.321098,-4.286285,-5.524668,5.655418,7.103443,2.570862,8.462583,3.827180,3.337501,3.780587,-3.866059,-5.884424,-2.991538,-7.280935,5.929301,-5.733354,6.703737,7.658230,-6.285833,-2.931830,-4.168595,-3.635116,-9.027970,-7.146028,-0.630289,-1.913672,-5.705537,8.654827,6.850954,-7.873460,-8.692317,-4.169613,8.653043,0.190156,3.397470,0.061628,8.978736,0.653165,-9.797184,-6.209721,9.945502,5.891346,5.563278,-2.266817,-9.473542,5.801351,4.521884,-5.181485,5.657059,-6.952548,7.979109,-1.756634,5.380442,-2.216202,9.916045,-6.929680,9.748797,0.637187,-3.006965,8.075905,-6.886264,-4.689460,9.033525,-1.711616,-4.991922,6.155742,-9.060300,2.505274,5.785593,2.861444,-0.996841,-1.716273,4.286834,-3.510787,3.925220,-6.036826,-5.656680,-1.982298,3.550387,9.511867,7.263399,3.493773,-3.246850,-3.530093,0.939335,8.608589,3.255771,4.707534,6.157367,1.264960,-3.100741,-8.215074,-9.176347,-5.367727,0.933645,9.718182,-6.980562,-8.830043,1.156185,-1.335405,7.779108,-1.300026,5.344841,5.764516,0.578397,-5.671434,3.282684,5.302060,1.383816,1.373461,4.092971,7.517294,-0.524456,-5.968778,-8.083984,-6.836687,-3.608255,4.975678,-4.999821,-7.610347,0.157302,5.649888,0.992654,-9.336951,-7.376907,5.200140,-2.438785,3.250447,1.429232,5.480308,9.741916,9.690255,-5.999444,5.058154,3.888365,0.405342,-2.112353,4.208202,6.502180,-3.846048,-5.461821,4.850608,3.514532,6.949400,-5.145104,-1.937429,-0.345522,-9.869722,-4.898841,3.442435,7.233393,-6.608195,-2.333314,-5.075281,2.036283,6.209302,-0.560972,8.629777,-3.477186,-1.628968,4.341202,-3.657902,-9.792465,-8.665691,-0.273757,8.011610,-6.343965,-4.025327,6.065733,-0.348104,1.715628,-9.232940,-4.715931,0.280587,-9.871977,-2.277455,8.693897,0.836783,3.514100,-5.289219,-6.456994,1.792842,-3.359147,5.780792,-1.992939,-7.736730,1.358299,-8.838977,-9.890940,-8.490197,3.205305,-4.039507,7.591507,4.126044,-4.637229,7.903084,2.730650,4.345120,-2.870788,2.018760,1.607271,-3.413605,8.249730,-1.311544,8.679255,-8.654191,4.192115,5.122169,8.969439,8.537737,-3.520400,-6.872504,-3.001056,9.747614,-3.205835,1.620568,8.325234,-8.179744,-4.050987,-6.153067,-0.926040,9.588216,-0.015519,-1.277467,1.447131,6.475454,-0.604674,3.946272,3.957808,0.286909,2.313067,3.021001,7.353225,3.865718,8.357458,9.462164,4.387966,9.312994,5.715935,5.938810,-1.294899,-8.148912,-0.308671,7.338155,7.630590,1.819507,6.556228,3.867819,-1.918343,5.517184,-2.363125,4.453023,9.229495,0.297019,2.905268,2.569004,0.855651,-0.763132,2.136329,-6.618255,7.765065,4.379652,-2.286235,2.568060,-0.084912,-9.494117,8.772635,-5.704602,1.889605,1.322985,-6.788252,-0.749104,-8.091591,3.119072,-2.238116,-2.472886,5.968933,-2.533561,-2.556109,-1.216683,-1.740084,-6.933103,7.416885,-9.626153,-0.936876,6.253140,-7.730570,6.262577,-0.842384,-4.057110,-7.046307,-3.856210,9.970694,2.263194,-7.205841,-3.545741,5.669423,-0.217529,8.848162,2.723718,-8.603722,-1.913906,-4.517329,-4.273289,-3.118130,4.983631,5.830004,-8.831150,-0.509186,0.550122,9.291696,-8.566461,-9.290578,1.146926,6.079528,9.999437,0.160679,9.643433,3.199731,9.204695,-4.355523,-9.830512,-7.088758,-8.346052,1.944252,-4.671587,6.458613,1.784022,2.678919,9.693061,0.970532,9.954412,-4.054385,-7.771944,-0.009386,8.245490,-3.048135,-8.089410,-2.682848,6.456482,-9.272968,2.278832,-4.504546,5.912088,4.482307,4.976509,-8.652364,-8.904636,6.650920,-5.918555,-1.238404,-8.262998,-7.272853,6.434226,-6.458995,-4.664875,-3.465184,-2.374691,-5.776908,5.301010,4.367554,-9.063544,7.124495,-8.178220,7.869856,-6.945793,2.283899,-6.549331,9.462693,-4.695695,-4.590457,0.229322,-2.784566,-6.459807,4.084636,0.690794,-9.888601,-7.116673,-6.547825,-2.243293,-9.991907,1.979612,0.108361,8.723919,7.235013,-2.526810,-5.251591,6.474737,-7.158502,2.817622,3.401105,-4.545716,-2.886692,1.168568,3.066730,-2.834853,-1.356665,3.977255,6.737024,-9.190682,4.387370,-5.797120,-0.060135,-0.438145,5.276030,4.893381,-2.482526,-7.137628,-8.592482,9.274954,3.420106,4.879779,5.087285,-5.174566,8.022346,-5.107824,9.409732,-7.115151,-1.354793,-7.925768,-1.338169,-9.817399,3.276889,0.876452,-9.829001,-5.509438,-4.751356,7.595578,-3.242403,-8.011581,-3.919760,-2.605848,-1.224964,-1.833674,-1.943961,-8.966638,-2.036513,5.362763,-0.965420,8.530035,-1.508051,-4.896039,-3.912671,-1.583030,6.213923,-7.006813,8.553213,-1.699007,-5.598726,-2.405181,8.063599,6.209894,4.430551,-0.295141,-9.792384,-1.466800,4.250829,2.216733,-0.327164,-2.300382,4.842912,-3.055941,-3.163033,-5.776266,1.505426,6.042452,4.246408,-9.116474,8.831943,-9.767225,-2.412625,-8.703224,-1.718303,1.575798,-5.012615,-7.447509,2.179432,-0.901422,3.070398,-4.294422,-2.543074,-1.433342,-5.513300,-4.705651,5.154107,3.982886,-0.354032,9.783118,-1.949964,7.720099,-8.630101,-1.141523,-8.181265,5.421617,6.844467,-6.889691,5.533436,8.473803,0.070022,-0.364098,1.424963,8.986656,7.796048,-7.129935,6.863666,-9.309807,0.512092,1.103559,-2.841982,-0.308325,-8.517659,9.001905,7.396450,-9.855522,-0.337998,5.026599,-1.156963,2.283127,4.023451,0.407668,-7.423812,-9.040701,-1.080681,4.220453,1.872173,-1.532886,5.314956,1.431384,2.318706,4.426658,-6.992386,8.167075,6.202361,2.611602,-1.023066,-6.307573,-8.095073,-7.056383,-4.745313,8.323646,1.800596,-3.550384,9.378173,6.086083,8.261451,8.708022,5.382359,-2.781368,2.553042,2.310789,3.281228,-8.307123,0.706062,-2.591344,7.438533,0.319722,-2.669612,3.887656,5.706313,-0.486851,6.969057,7.543735,-2.931313,-9.585685,1.986079,4.301949,7.274812,-2.482960,-6.043090,-9.565128,7.689295,4.011965,4.515512,9.787040,0.240782,0.340066,9.629798,-0.927761,7.139781,-7.938804,-7.528929,9.361242,6.991262,-5.242110,-5.707543,7.116829,-2.204888,6.152833,5.092003,9.796595,-4.863760,-0.342913,6.017876,1.320078,8.490580,3.224667,7.459821,1.344886,-5.718299,0.080634,-4.307855,-1.243785,3.542553,9.262672,8.129058,7.839662,7.819687,8.749299,-8.132377,0.961676,-7.996835,-9.130303,0.145627,8.808922,3.620195,3.705335,1.627076,1.046049,5.046460,-3.958812,0.314460,3.245128,8.427151,4.009807,6.891616,1.008023,8.156888,-5.856843,1.229354,-5.620660,-8.539435,-1.297606,-7.863463,-2.600610,-2.337478,-0.344711,-9.836048,4.651042,-2.684166,-1.446014,2.739010,-6.617485,8.712033,-7.075339,-2.123000,6.809410,-5.965005,-3.174968,7.041908,-9.995343,3.041247,5.861899,-7.060358,9.809141,1.145591,1.489050,1.131789,1.664469,-9.884095,4.886574,7.754833,3.837987,8.000512,-7.963317,-5.624895,-6.741555,0.994624,6.864322,-0.231152,-1.983041,-9.702967,6.118080,1.371140,-8.173311,-4.233855,-4.562235,7.851635,0.790407,-7.600597,3.913627,-8.553998,-2.286037,-3.535217,-4.693367,6.967089,-6.569038,-6.208715,9.408058,1.358303,8.294978,-0.346830,7.446834,4.561835,-0.823095,-9.461705,-5.374136,0.958018,-9.595200,-4.429369,0.169700,8.213371,-9.912706,2.035507,-1.506554,1.764463,-7.769748,1.614163,5.841297,-4.925478,-5.659386,-5.052682,1.731858,-8.677655,6.758146,-5.650796,-9.356585,-2.043476,5.756725,-3.821506,-0.256558,6.988610,2.911261,-7.984802,7.980278,-5.920651,0.307221,-0.028636,0.559719,-2.605991,-2.575025,8.208027,7.416002,9.460694,7.419150,-3.818967,7.706257,-5.169904,-2.511968,-4.396114,7.306762,-3.391648,4.736105,7.413753,1.011336,8.755356,4.199806,-6.756175,-3.430475,0.325460,2.489124,-7.942681,-5.481991,-9.262391,6.934508,-5.092696,1.444788,-2.224004,-1.225510,7.443612,2.367946,0.455961,3.688655,0.828979,7.333217,4.899005,-7.195639,9.874165,-0.596301,-1.227031,-5.392415,-3.808274,5.747800,-9.813363,7.316837,4.366182,-3.584092,3.745770,-4.967825,-5.662318,9.559416,-3.534731,0.237086,-5.145358,3.068385,4.939747,-7.558967,-8.886572,-4.855230,7.879372,-8.217166,6.539468,7.789945,5.287664,5.979342,1.277954,9.759717,1.782144,7.273893,9.918761,-2.459475,0.343452,-1.377399,-6.769085,-8.025613,-6.420097,-5.896170,-8.192861,-4.170513,0.891600,9.948937,8.696712,-0.391297,7.548553,-9.658210,2.447827,4.204794,1.830230,-6.841081,1.444546,3.540313,7.242791,4.818778,9.382994,9.000528,8.764213,8.906953,-3.445072,4.745296,-2.658710,-2.323597,-3.768286,-6.087184,7.520647,0.972714,6.889129,8.820635,-2.120354,-2.606629,-3.322373,-8.484571,-7.407015,-5.097542,-4.873357,-3.835593,-3.224843,-4.754675,6.621163,-1.443165,3.834783,9.785561,1.614803,9.549473,7.983833,7.753664,-7.634971,9.615712,-7.213570,5.489633,-7.310454,7.970534,-9.268711,0.519378,-7.212895,-5.252555,-1.117310,-3.854651,-1.472102,0.548619,-9.057446,-9.519688,6.487117,4.612518,9.318843,-7.867711,6.211535,-1.069569,4.779782,1.023446,-2.586778,9.694310,8.312834,-5.325059,8.258450,7.087536,-9.072033,-3.610187,2.426874,9.178235,-8.381549,-4.672797,4.302581,6.774268,8.464626,-3.237081,0.291089,-2.618989,-8.413679,-7.193407,-8.676862,5.239544,0.551507,-8.251805,2.953665,-4.935866,9.524757,2.305307,7.373620,9.877370,5.529067,-7.619266,9.737926,5.896119,2.507820,-1.498313,1.309495,0.057488,2.913401,-4.673802,7.644744,4.215697,3.522323,-8.982314,9.323818,8.662219,4.400258,5.951954,-3.701398,-7.115408,5.358331,-0.270761,-4.837343,2.861243,8.090890,4.155926,-5.096232,-4.183244,5.885337,3.030766,-0.942706,-0.182444,-9.154817,4.354044,-0.349129,7.824263,-0.036978,6.583172,2.560046,-5.696932,-1.257572,2.450512,-1.056462,-9.770762,-3.138551,3.083378,6.713170,4.443923,4.613746,-6.927614,-6.808572,1.490613,6.627059,-9.917346,-0.635467,-4.607205,-6.351084,6.677792,3.042191,-6.167604,5.479544,-9.827967,5.981695,2.150302,-6.522665,2.024750,7.335136,7.030383,8.434546,1.268271,4.408259,-5.953033,4.139079,-2.853246,1.935065,3.097715,-1.727430,3.736111,6.110799,7.967871,3.688674,-2.314120,5.172246,9.569328,7.029574,-7.953394,-4.085362,-3.280448,6.047666,-4.138639,-1.320073,1.642277,-8.630917,-8.609160,4.559506,1.979536,-4.988644,3.670165,-4.961902,-1.719661,4.627746,-0.399908,3.765394,-8.674721,1.220552,-6.444606,-4.175264,1.741932,-6.458171,-9.978751,8.806036,-7.342354,1.380298,3.278342,2.855590,-3.951039,3.285145,-1.904844,2.646551,0.491292,-1.163377,-9.927372,6.613585,5.262236,-4.768316,-1.181340,1.545648,5.907985,-7.099563,-8.907955,6.173230,2.275783,4.370610,9.042962,-6.879882,-4.388182,-5.585320,1.243538,-1.695692,-2.137697,-4.649952,-6.010040,9.779533,-3.928717,-8.947802,8.929302,7.793747,-3.137372,5.995185,-6.160914,-4.420271,-7.119803,8.378351,9.177054,-7.548918,-2.390147,-7.074010,-1.487310,8.679506,3.530987,-1.288217,1.119213,5.230615,-8.991700,5.496064,-4.758302,8.755609,7.660968,-7.725174,-5.876731,-8.379001,5.471638,6.241893,-7.202445,5.991859,9.228838,4.751948,2.198961,-8.245618,5.437303,-4.292081,-8.423304,-4.205846,2.545226,-8.510314,6.415899,-6.337987,0.188029,-3.124197,-2.334755,9.913522,0.198227,-7.417483,-5.824911,3.411299,5.438398,7.907841,8.941806,2.620261,2.238569,8.218389,-4.342114,3.555805,3.532481,7.581902,9.251720,3.542763,7.876090,-3.546893,0.164714,3.274947,6.565574,-9.420354,-8.428855,8.840074,2.783011,-2.357286,9.169167,0.803574,-6.178222,-6.912954,8.429439,-4.223825,-1.165189,-1.307386,-1.466927,-3.897768,0.330516,3.273889,-6.264025,6.752094,7.241034,9.390791,6.548620,4.324405,3.781417,-8.289639,-4.718477,-1.974738,4.112395,-1.048142,-7.818401,0.696573,0.621881,-4.583340,-6.790407,7.062655,2.144504,-1.809969,1.010115,-2.663650,4.209486,1.946418,-2.437877,-7.351261,8.546619,6.537414,1.788676,2.655760,9.827951,-1.796720,7.136474,0.314334,-4.649782,0.797029,-6.944075,8.298240,-0.353974,9.928570,-4.489369,-5.558506,-9.070680,6.191199,4.884218,-3.261847,-9.317152,-3.406286,-5.066596,1.319146,8.615444,-3.930633,-2.182017,4.191143,-8.312048,2.401764,3.985883,-9.859134,-5.194876,4.500081,-8.756892,-9.474886,5.393093,-7.886297,9.125447,-8.828263,8.663017,-6.266230,-0.171926,-9.699019,-3.555213,4.120198,-0.860479,7.505777,-6.403883,-0.857338,-5.511912,9.179006,8.755374,5.304658,4.186385,8.224038,-3.997652,7.870438,8.727274,0.135077,6.074188,7.910702,6.451828,-4.567139,-1.161719,-1.683275,-6.170899,-2.256388,-0.348179,-0.789100,5.460297,-0.060935,4.826015,5.376453,0.901220,-3.388732,9.991123,-2.384755,-5.382256,-2.816586,7.758395,0.107886,4.767826,1.530027,7.209188,3.045213,9.357347,-5.551752,5.193350,-8.838412,-0.245349,-7.355047,-3.693393,-2.128945,2.026209,8.764003,-1.117211,-8.706913,-2.208031,8.840394,1.697913,0.284276,-3.530428,2.240892,9.955411,-1.992105,-9.121141,9.410595,-7.263475,1.061005,5.356909,-6.561355,7.550514,6.824347,7.782069,8.892676,9.947889,5.253106,-9.704143,-3.766550,-1.872136,-5.981044,1.382109,-2.625969,6.102474,7.065005,-3.909863,-3.529521,8.133987,-7.300405,-6.108286,2.014606,-8.776524,4.515264,-1.271871,-9.560230,8.031863,8.713457,-2.671248,-6.723950,-8.076965,-5.572567,4.469100,-2.504345,-3.199500,6.343653,1.142122,5.163695,-4.759732,-2.829621,-7.449527,4.717137,2.224630,-4.585061,-9.540806,-7.980078,-6.662851,-0.516916,6.796991,-5.848888,1.916232,7.871185,5.175766,-0.096086,8.357600,-8.462437,3.992628,8.260285,-9.754432,-2.853188,-0.573007,6.063079,-4.457917,0.409574,2.031172,3.007721,9.994747,0.580453,4.700289,-2.962509,-3.750831,-8.054544,6.690454,5.936035,4.451474,-3.707409,-0.545859,7.467480,2.445108,-3.629796,-9.699179,8.402162,-3.470941,-3.001499,-4.562995,3.937276,4.725774,-0.801536,7.185057,4.615242,-4.522337,2.535878,6.500297,9.810101,2.565886,9.377228,8.692726,1.371836,8.359560,-8.072433,0.755033,5.214560,8.193498,0.563669,5.626239,-8.297031,-6.914785,-5.731654,-7.055444,7.796186,5.596123], dtype = "float64")#candidate|4231|(1440,)|const|float64
call_4230 = relay.TupleGetItem(func_2105_call(relay.reshape(const_4231.astype('float64'), [1440, 1])), 2)
call_4232 = relay.TupleGetItem(func_2108_call(relay.reshape(const_4231.astype('float64'), [1440, 1])), 2)
output = relay.Tuple([call_4218,call_4230,const_4231,])
output2 = relay.Tuple([call_4219,call_4232,const_4231,])
func_4235 = relay.Function([], output)
mod['func_4235'] = func_4235
mod = relay.transform.InferType()(mod)
mutated_mod['func_4235'] = func_4235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4235_call = mutated_mod.get_global_var('func_4235')
call_4236 = func_4235_call()
output = call_4236
func_4237 = relay.Function([], output)
mutated_mod['func_4237'] = func_4237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mod.get_global_var('func_793')
func_794_call = mutated_mod.get_global_var('func_794')
call_4282 = relay.TupleGetItem(func_793_call(), 0)
call_4283 = relay.TupleGetItem(func_794_call(), 0)
func_4188_call = mod.get_global_var('func_4188')
func_4190_call = mutated_mod.get_global_var('func_4190')
call_4314 = relay.TupleGetItem(func_4188_call(), 0)
call_4315 = relay.TupleGetItem(func_4190_call(), 0)
output = relay.Tuple([call_4282,call_4314,])
output2 = relay.Tuple([call_4283,call_4315,])
func_4328 = relay.Function([], output)
mod['func_4328'] = func_4328
mod = relay.transform.InferType()(mod)
mutated_mod['func_4328'] = func_4328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4328_call = mutated_mod.get_global_var('func_4328')
call_4329 = func_4328_call()
output = call_4329
func_4330 = relay.Function([], output)
mutated_mod['func_4330'] = func_4330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_4331 = relay.TupleGetItem(func_537_call(), 0)
call_4332 = relay.TupleGetItem(func_538_call(), 0)
var_4333 = relay.var("var_4333", dtype = "float32", shape = (5, 16, 3))#candidate|4333|(5, 16, 3)|var|float32
bop_4334 = relay.greater(call_4331.astype('bool'), relay.reshape(var_4333.astype('bool'), relay.shape_of(call_4331))) # shape=(5, 16, 3)
bop_4337 = relay.greater(call_4332.astype('bool'), relay.reshape(var_4333.astype('bool'), relay.shape_of(call_4332))) # shape=(5, 16, 3)
func_3117_call = mod.get_global_var('func_3117')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_4341 = func_3117_call()
call_4342 = func_3117_call()
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_4343 = relay.TupleGetItem(func_1866_call(), 0)
call_4344 = relay.TupleGetItem(func_1867_call(), 0)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_4354 = func_1097_call()
call_4355 = func_1097_call()
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_4374 = func_927_call()
call_4375 = func_927_call()
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_4380 = relay.TupleGetItem(func_1972_call(), 3)
call_4381 = relay.TupleGetItem(func_1973_call(), 3)
output = relay.Tuple([bop_4334,call_4341,call_4343,call_4354,call_4374,call_4380,])
output2 = relay.Tuple([bop_4337,call_4342,call_4344,call_4355,call_4375,call_4381,])
func_4390 = relay.Function([var_4333,], output)
mod['func_4390'] = func_4390
mod = relay.transform.InferType()(mod)
var_4391 = relay.var("var_4391", dtype = "float32", shape = (5, 16, 3))#candidate|4391|(5, 16, 3)|var|float32
output = func_4390(var_4391)
func_4392 = relay.Function([var_4391], output)
mutated_mod['func_4392'] = func_4392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4079_call = mod.get_global_var('func_4079')
func_4081_call = mutated_mod.get_global_var('func_4081')
call_4471 = relay.TupleGetItem(func_4079_call(), 0)
call_4472 = relay.TupleGetItem(func_4081_call(), 0)
output = call_4471
output2 = call_4472
func_4475 = relay.Function([], output)
mod['func_4475'] = func_4475
mod = relay.transform.InferType()(mod)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4475_call = mutated_mod.get_global_var('func_4475')
call_4476 = func_4475_call()
output = call_4476
func_4477 = relay.Function([], output)
mutated_mod['func_4477'] = func_4477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_4478 = relay.TupleGetItem(func_2409_call(), 0)
call_4479 = relay.TupleGetItem(func_2411_call(), 0)
output = relay.Tuple([call_4478,])
output2 = relay.Tuple([call_4479,])
func_4485 = relay.Function([], output)
mod['func_4485'] = func_4485
mod = relay.transform.InferType()(mod)
mutated_mod['func_4485'] = func_4485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4485_call = mutated_mod.get_global_var('func_4485')
call_4486 = func_4485_call()
output = call_4486
func_4487 = relay.Function([], output)
mutated_mod['func_4487'] = func_4487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2437_call = mod.get_global_var('func_2437')
func_2439_call = mutated_mod.get_global_var('func_2439')
call_4503 = relay.TupleGetItem(func_2437_call(), 0)
call_4504 = relay.TupleGetItem(func_2439_call(), 0)
output = call_4503
output2 = call_4504
func_4507 = relay.Function([], output)
mod['func_4507'] = func_4507
mod = relay.transform.InferType()(mod)
mutated_mod['func_4507'] = func_4507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4507_call = mutated_mod.get_global_var('func_4507')
call_4508 = func_4507_call()
output = call_4508
func_4509 = relay.Function([], output)
mutated_mod['func_4509'] = func_4509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_537_call = mod.get_global_var('func_537')
func_538_call = mutated_mod.get_global_var('func_538')
call_4520 = relay.TupleGetItem(func_537_call(), 0)
call_4521 = relay.TupleGetItem(func_538_call(), 0)
var_4527 = relay.var("var_4527", dtype = "float32", shape = (5, 16, 3))#candidate|4527|(5, 16, 3)|var|float32
bop_4528 = relay.equal(call_4520.astype('bool'), relay.reshape(var_4527.astype('bool'), relay.shape_of(call_4520))) # shape=(5, 16, 3)
bop_4531 = relay.equal(call_4521.astype('bool'), relay.reshape(var_4527.astype('bool'), relay.shape_of(call_4521))) # shape=(5, 16, 3)
func_4485_call = mod.get_global_var('func_4485')
func_4487_call = mutated_mod.get_global_var('func_4487')
call_4536 = relay.TupleGetItem(func_4485_call(), 0)
call_4537 = relay.TupleGetItem(func_4487_call(), 0)
func_4100_call = mod.get_global_var('func_4100')
func_4103_call = mutated_mod.get_global_var('func_4103')
call_4545 = func_4100_call(relay.reshape(call_4536.astype('uint16'), [105,]))
call_4546 = func_4100_call(relay.reshape(call_4536.astype('uint16'), [105,]))
func_4328_call = mod.get_global_var('func_4328')
func_4330_call = mutated_mod.get_global_var('func_4330')
call_4547 = relay.TupleGetItem(func_4328_call(), 0)
call_4548 = relay.TupleGetItem(func_4330_call(), 0)
func_1286_call = mod.get_global_var('func_1286')
func_1288_call = mutated_mod.get_global_var('func_1288')
call_4549 = relay.TupleGetItem(func_1286_call(), 0)
call_4550 = relay.TupleGetItem(func_1288_call(), 0)
output = relay.Tuple([bop_4528,call_4536,call_4545,call_4547,call_4549,])
output2 = relay.Tuple([bop_4531,call_4537,call_4546,call_4548,call_4550,])
func_4552 = relay.Function([var_4527,], output)
mod['func_4552'] = func_4552
mod = relay.transform.InferType()(mod)
var_4553 = relay.var("var_4553", dtype = "float32", shape = (5, 16, 3))#candidate|4553|(5, 16, 3)|var|float32
output = func_4552(var_4553)
func_4554 = relay.Function([var_4553], output)
mutated_mod['func_4554'] = func_4554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mod.get_global_var('func_3514')
func_3515_call = mutated_mod.get_global_var('func_3515')
call_4558 = relay.TupleGetItem(func_3514_call(), 0)
call_4559 = relay.TupleGetItem(func_3515_call(), 0)
func_3559_call = mod.get_global_var('func_3559')
func_3561_call = mutated_mod.get_global_var('func_3561')
call_4561 = relay.TupleGetItem(func_3559_call(), 1)
call_4562 = relay.TupleGetItem(func_3561_call(), 1)
uop_4564 = relay.cosh(call_4558.astype('float32')) # shape=(20, 72)
uop_4566 = relay.cosh(call_4559.astype('float32')) # shape=(20, 72)
output = relay.Tuple([call_4561,uop_4564,])
output2 = relay.Tuple([call_4562,uop_4566,])
func_4567 = relay.Function([], output)
mod['func_4567'] = func_4567
mod = relay.transform.InferType()(mod)
output = func_4567()
func_4568 = relay.Function([], output)
mutated_mod['func_4568'] = func_4568
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4625 = relay.const([[[-8,-7,1],[-6,-7,5],[-1,-9,-3],[6,-1,-4],[3,5,-9],[-2,-9,9],[-2,7,9],[-9,7,3]],[[4,-4,2],[-3,-2,-5],[-7,7,-7],[8,-3,-9],[10,-7,9],[-7,-9,-7],[-8,6,-9],[2,9,3]],[[-10,-7,7],[7,5,2],[-4,-6,9],[4,6,-1],[2,-2,-5],[-8,8,-9],[-1,-2,-2],[2,-3,-1]],[[-4,4,-6],[6,8,-10],[6,9,-5],[-9,-5,-5],[-5,-5,7],[-3,-10,2],[9,3,-5],[2,2,5]],[[10,-4,-5],[3,9,-8],[-3,-9,7],[-8,-7,-6],[5,6,-9],[-7,-5,5],[-3,1,6],[8,2,2]],[[-7,10,3],[-8,5,-8],[-5,3,-7],[1,7,-9],[3,2,-5],[9,-5,7],[4,-8,9],[3,-2,-5]],[[7,8,8],[-6,-7,8],[-3,7,5],[-7,1,-10],[-5,4,3],[8,-5,-3],[6,-6,8],[-8,-3,10]],[[-8,9,-6],[10,5,-9],[-5,-8,5],[-5,-1,-5],[-7,3,-5],[9,1,3],[-10,7,8],[4,4,6]],[[-3,2,4],[-4,-8,2],[-9,-7,3],[-8,-6,8],[2,9,-2],[-7,6,9],[-5,-8,10],[-6,-2,-1]]], dtype = "uint64")#candidate|4625|(9, 8, 3)|const|uint64
var_4626 = relay.var("var_4626", dtype = "uint64", shape = (9, 8, 3))#candidate|4626|(9, 8, 3)|var|uint64
bop_4627 = relay.multiply(const_4625.astype('uint64'), relay.reshape(var_4626.astype('uint64'), relay.shape_of(const_4625))) # shape=(9, 8, 3)
output = relay.Tuple([bop_4627,])
output2 = relay.Tuple([bop_4627,])
func_4632 = relay.Function([var_4626,], output)
mod['func_4632'] = func_4632
mod = relay.transform.InferType()(mod)
mutated_mod['func_4632'] = func_4632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4633 = relay.var("var_4633", dtype = "uint64", shape = (9, 8, 3))#candidate|4633|(9, 8, 3)|var|uint64
func_4632_call = mutated_mod.get_global_var('func_4632')
call_4634 = func_4632_call(var_4633)
output = call_4634
func_4635 = relay.Function([var_4633], output)
mutated_mod['func_4635'] = func_4635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_4637 = func_575_call()
call_4638 = func_575_call()
output = call_4637
output2 = call_4638
func_4641 = relay.Function([], output)
mod['func_4641'] = func_4641
mod = relay.transform.InferType()(mod)
output = func_4641()
func_4642 = relay.Function([], output)
mutated_mod['func_4642'] = func_4642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3337_call = mod.get_global_var('func_3337')
func_3338_call = mutated_mod.get_global_var('func_3338')
call_4651 = relay.TupleGetItem(func_3337_call(), 1)
call_4652 = relay.TupleGetItem(func_3338_call(), 1)
output = call_4651
output2 = call_4652
func_4664 = relay.Function([], output)
mod['func_4664'] = func_4664
mod = relay.transform.InferType()(mod)
output = func_4664()
func_4665 = relay.Function([], output)
mutated_mod['func_4665'] = func_4665
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4680 = relay.var("var_4680", dtype = "int8", shape = (15, 9, 4))#candidate|4680|(15, 9, 4)|var|int8
const_4681 = relay.const([[[9,-1,-3,-8],[-9,5,-6,6],[-7,-8,1,-9],[-3,2,-8,-7],[8,-4,1,1],[10,5,9,8],[10,10,-1,2],[2,9,-4,8],[6,-3,1,1]],[[10,-1,-7,8],[-6,-9,-9,-10],[6,-2,-10,4],[-2,5,1,-7],[1,-1,-9,-8],[-7,-10,9,-1],[1,-7,4,7],[10,-9,9,1],[6,-2,3,9]],[[-6,-8,1,10],[-5,-1,10,-6],[1,1,-3,-3],[8,-5,-5,1],[-3,4,10,-4],[-3,-5,6,-5],[-7,8,-3,-3],[6,10,-10,1],[-1,7,-3,6]],[[9,-10,3,1],[-4,-1,10,5],[-2,7,7,-7],[-5,10,7,-3],[-7,9,-8,1],[-9,-8,8,5],[10,2,-10,-8],[3,-4,-5,-7],[9,4,6,9]],[[10,4,-3,-10],[3,-2,10,9],[-9,-6,-9,7],[-8,-7,-8,10],[4,-8,5,1],[9,-2,-5,-4],[5,1,2,-3],[-8,-5,-7,-4],[10,-9,9,4]],[[3,-9,-8,-7],[5,-8,5,-9],[2,-9,8,-1],[7,-5,9,-6],[-7,5,2,-10],[-7,5,-10,4],[8,-2,-1,7],[4,-6,-3,-7],[9,-8,3,9]],[[-6,1,9,-9],[-3,3,7,-9],[4,-4,-10,-9],[-3,2,-7,-6],[-5,1,4,-1],[3,10,4,1],[-7,-6,5,5],[-4,-4,8,-4],[-6,-9,6,-9]],[[3,-1,1,6],[-8,-4,-8,1],[-8,5,-2,10],[-5,-2,6,10],[-1,8,-4,9],[-7,-4,-1,-8],[-9,-4,-3,1],[-3,9,-6,-9],[-1,-8,-1,8]],[[9,-4,-7,9],[7,-9,8,-10],[-4,-10,-7,7],[8,-4,4,9],[-4,-6,-9,-8],[-8,9,-10,-7],[-8,-7,6,5],[-1,4,-1,-1],[-8,-7,-1,3]],[[4,5,1,-10],[-7,-3,1,10],[7,9,9,-6],[-8,3,-9,-9],[10,-9,-4,-1],[-6,-7,-2,-8],[10,-8,1,5],[-6,1,9,-2],[-5,-2,-10,3]],[[7,2,6,-8],[-9,-7,-2,-4],[-3,6,6,-2],[9,-2,-7,4],[3,-3,7,-7],[-10,9,-7,2],[7,-3,-8,-5],[-1,5,-10,-1],[-6,-3,-8,1]],[[5,3,2,-3],[3,-5,-10,-7],[7,-8,4,1],[-8,5,7,5],[4,5,3,-7],[3,-9,-2,6],[10,-6,7,-4],[-4,-10,-3,-4],[-5,6,-8,-6]],[[5,-5,-4,8],[-9,6,-4,9],[-9,10,8,-2],[-4,2,-1,2],[-6,5,-10,-1],[7,-2,-10,-10],[4,5,-5,-6],[5,-2,8,2],[-1,-3,-2,-1]],[[-4,2,6,6],[-4,-3,-10,-10],[8,-1,6,-10],[2,9,8,5],[-2,9,-8,1],[6,3,-4,-10],[4,9,-7,-8],[-4,3,8,-5],[6,2,9,-6]],[[-9,2,3,-6],[-3,9,-5,9],[8,1,-3,-8],[-10,-10,6,-5],[-6,-10,1,6],[-10,6,-3,-5],[8,-7,-2,-7],[-9,-3,-7,-2],[7,4,8,2]]], dtype = "int8")#candidate|4681|(15, 9, 4)|const|int8
bop_4682 = relay.multiply(var_4680.astype('int8'), relay.reshape(const_4681.astype('int8'), relay.shape_of(var_4680))) # shape=(15, 9, 4)
func_2834_call = mod.get_global_var('func_2834')
func_2835_call = mutated_mod.get_global_var('func_2835')
call_4685 = relay.TupleGetItem(func_2834_call(), 3)
call_4686 = relay.TupleGetItem(func_2835_call(), 3)
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_4708 = relay.TupleGetItem(func_2409_call(), 0)
call_4709 = relay.TupleGetItem(func_2411_call(), 0)
output = relay.Tuple([bop_4682,call_4685,call_4708,])
output2 = relay.Tuple([bop_4682,call_4686,call_4709,])
func_4712 = relay.Function([var_4680,], output)
mod['func_4712'] = func_4712
mod = relay.transform.InferType()(mod)
mutated_mod['func_4712'] = func_4712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4713 = relay.var("var_4713", dtype = "int8", shape = (15, 9, 4))#candidate|4713|(15, 9, 4)|var|int8
func_4712_call = mutated_mod.get_global_var('func_4712')
call_4714 = func_4712_call(var_4713)
output = call_4714
func_4715 = relay.Function([var_4713], output)
mutated_mod['func_4715'] = func_4715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_891_call = mod.get_global_var('func_891')
func_892_call = mutated_mod.get_global_var('func_892')
call_4717 = func_891_call()
call_4718 = func_891_call()
func_1835_call = mod.get_global_var('func_1835')
func_1836_call = mutated_mod.get_global_var('func_1836')
call_4727 = relay.TupleGetItem(func_1835_call(), 0)
call_4728 = relay.TupleGetItem(func_1836_call(), 0)
output = relay.Tuple([call_4717,call_4727,])
output2 = relay.Tuple([call_4718,call_4728,])
func_4729 = relay.Function([], output)
mod['func_4729'] = func_4729
mod = relay.transform.InferType()(mod)
output = func_4729()
func_4730 = relay.Function([], output)
mutated_mod['func_4730'] = func_4730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4641_call = mod.get_global_var('func_4641')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_4745 = func_4641_call()
call_4746 = func_4641_call()
func_2890_call = mod.get_global_var('func_2890')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_4770 = func_2890_call()
call_4771 = func_2890_call()
output = relay.Tuple([call_4745,call_4770,])
output2 = relay.Tuple([call_4746,call_4771,])
func_4784 = relay.Function([], output)
mod['func_4784'] = func_4784
mod = relay.transform.InferType()(mod)
output = func_4784()
func_4785 = relay.Function([], output)
mutated_mod['func_4785'] = func_4785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_4825 = relay.TupleGetItem(func_608_call(), 1)
call_4826 = relay.TupleGetItem(func_609_call(), 1)
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_4839 = relay.TupleGetItem(func_2409_call(), 0)
call_4840 = relay.TupleGetItem(func_2411_call(), 0)
func_2580_call = mod.get_global_var('func_2580')
func_2581_call = mutated_mod.get_global_var('func_2581')
call_4853 = relay.TupleGetItem(func_2580_call(), 1)
call_4854 = relay.TupleGetItem(func_2581_call(), 1)
output = relay.Tuple([call_4825,call_4839,call_4853,])
output2 = relay.Tuple([call_4826,call_4840,call_4854,])
func_4863 = relay.Function([], output)
mod['func_4863'] = func_4863
mod = relay.transform.InferType()(mod)
mutated_mod['func_4863'] = func_4863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4863_call = mutated_mod.get_global_var('func_4863')
call_4864 = func_4863_call()
output = call_4864
func_4865 = relay.Function([], output)
mutated_mod['func_4865'] = func_4865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2890_call = mod.get_global_var('func_2890')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_4911 = func_2890_call()
call_4912 = func_2890_call()
func_3449_call = mod.get_global_var('func_3449')
func_3451_call = mutated_mod.get_global_var('func_3451')
var_4919 = relay.var("var_4919", dtype = "float64", shape = (1440,))#candidate|4919|(1440,)|var|float64
call_4918 = relay.TupleGetItem(func_3449_call(relay.reshape(var_4919.astype('float64'), [2, 720])), 0)
call_4920 = relay.TupleGetItem(func_3451_call(relay.reshape(var_4919.astype('float64'), [2, 720])), 0)
output = relay.Tuple([call_4911,call_4918,var_4919,])
output2 = relay.Tuple([call_4912,call_4920,var_4919,])
func_4932 = relay.Function([var_4919,], output)
mod['func_4932'] = func_4932
mod = relay.transform.InferType()(mod)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4933 = relay.var("var_4933", dtype = "float64", shape = (1440,))#candidate|4933|(1440,)|var|float64
func_4932_call = mutated_mod.get_global_var('func_4932')
call_4934 = func_4932_call(var_4933)
output = call_4934
func_4935 = relay.Function([var_4933], output)
mutated_mod['func_4935'] = func_4935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_5033 = func_719_call()
call_5034 = func_719_call()
func_2674_call = mod.get_global_var('func_2674')
func_2675_call = mutated_mod.get_global_var('func_2675')
call_5044 = relay.TupleGetItem(func_2674_call(), 0)
call_5045 = relay.TupleGetItem(func_2675_call(), 0)
output = relay.Tuple([call_5033,call_5044,])
output2 = relay.Tuple([call_5034,call_5045,])
func_5046 = relay.Function([], output)
mod['func_5046'] = func_5046
mod = relay.transform.InferType()(mod)
mutated_mod['func_5046'] = func_5046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5046_call = mutated_mod.get_global_var('func_5046')
call_5047 = func_5046_call()
output = call_5047
func_5048 = relay.Function([], output)
mutated_mod['func_5048'] = func_5048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5062 = relay.var("var_5062", dtype = "float32", shape = (2, 10, 9))#candidate|5062|(2, 10, 9)|var|float32
uop_5063 = relay.erf(var_5062.astype('float32')) # shape=(2, 10, 9)
func_4632_call = mod.get_global_var('func_4632')
func_4635_call = mutated_mod.get_global_var('func_4635')
const_5068 = relay.const([[-2,-8,2,2,-4,-10,6,-7,-8,6,-6,8,9,-9,-3,-10,5,6,9,-1,2,-2,-3,9,-5,1,10,-7,3,10,2,1,-7,-5,6,-1,-7,-7,2,-2,-8,8,10,-9,-3,1,8,-3,8,3,-5,-4,-7,-3,-6,-6,5,6,-9,-10,-3,-8,-2,10,-8,-6,9,-5,1,-5,-2,5,5,3,-6,6,4,4,2,6,7,5,1,2,10,3,8,-9,9,7,-7,-9,-5,-6,7,9,3,-9,5,-10,-1,-9,3,4,-2,-9,1,9],[-1,5,7,1,9,8,-5,1,1,7,-7,-6,-1,7,3,10,-3,1,8,-3,3,-10,-10,-6,-8,7,-3,4,9,6,9,5,10,5,-7,-4,10,1,-3,-2,-8,-8,-3,-5,-6,-4,4,9,3,-1,-10,3,8,-9,8,4,10,9,4,6,2,7,9,-1,7,5,8,7,-9,-7,-10,5,2,-3,-5,-8,-1,6,-8,2,-10,5,2,-3,10,2,-8,-2,-8,-9,-6,-3,-2,4,-5,-7,3,2,-6,10,5,-8,6,5,6,10,-1,-6]], dtype = "uint64")#candidate|5068|(2, 108)|const|uint64
call_5067 = relay.TupleGetItem(func_4632_call(relay.reshape(const_5068.astype('uint64'), [9, 8, 3])), 0)
call_5069 = relay.TupleGetItem(func_4635_call(relay.reshape(const_5068.astype('uint64'), [9, 8, 3])), 0)
output = relay.Tuple([uop_5063,call_5067,const_5068,])
output2 = relay.Tuple([uop_5063,call_5069,const_5068,])
func_5073 = relay.Function([var_5062,], output)
mod['func_5073'] = func_5073
mod = relay.transform.InferType()(mod)
mutated_mod['func_5073'] = func_5073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5074 = relay.var("var_5074", dtype = "float32", shape = (2, 10, 9))#candidate|5074|(2, 10, 9)|var|float32
func_5073_call = mutated_mod.get_global_var('func_5073')
call_5075 = func_5073_call(var_5074)
output = call_5075
func_5076 = relay.Function([var_5074], output)
mutated_mod['func_5076'] = func_5076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_719_call = mod.get_global_var('func_719')
func_721_call = mutated_mod.get_global_var('func_721')
call_5092 = func_719_call()
call_5093 = func_719_call()
output = relay.Tuple([call_5092,])
output2 = relay.Tuple([call_5093,])
func_5095 = relay.Function([], output)
mod['func_5095'] = func_5095
mod = relay.transform.InferType()(mod)
output = func_5095()
func_5096 = relay.Function([], output)
mutated_mod['func_5096'] = func_5096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2049_call = mod.get_global_var('func_2049')
func_2050_call = mutated_mod.get_global_var('func_2050')
call_5129 = relay.TupleGetItem(func_2049_call(), 2)
call_5130 = relay.TupleGetItem(func_2050_call(), 2)
func_4475_call = mod.get_global_var('func_4475')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_5171 = func_4475_call()
call_5172 = func_4475_call()
func_2771_call = mod.get_global_var('func_2771')
func_2772_call = mutated_mod.get_global_var('func_2772')
call_5185 = relay.TupleGetItem(func_2771_call(), 0)
call_5186 = relay.TupleGetItem(func_2772_call(), 0)
bop_5187 = relay.add(call_5129.astype('float64'), relay.reshape(call_5185.astype('float64'), relay.shape_of(call_5129))) # shape=(105,)
bop_5190 = relay.add(call_5130.astype('float64'), relay.reshape(call_5186.astype('float64'), relay.shape_of(call_5130))) # shape=(105,)
output = relay.Tuple([call_5171,bop_5187,])
output2 = relay.Tuple([call_5172,bop_5190,])
func_5193 = relay.Function([], output)
mod['func_5193'] = func_5193
mod = relay.transform.InferType()(mod)
output = func_5193()
func_5194 = relay.Function([], output)
mutated_mod['func_5194'] = func_5194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3559_call = mod.get_global_var('func_3559')
func_3561_call = mutated_mod.get_global_var('func_3561')
call_5221 = relay.TupleGetItem(func_3559_call(), 0)
call_5222 = relay.TupleGetItem(func_3561_call(), 0)
func_638_call = mod.get_global_var('func_638')
func_639_call = mutated_mod.get_global_var('func_639')
call_5244 = relay.TupleGetItem(func_638_call(), 0)
call_5245 = relay.TupleGetItem(func_639_call(), 0)
output = relay.Tuple([call_5221,call_5244,])
output2 = relay.Tuple([call_5222,call_5245,])
func_5250 = relay.Function([], output)
mod['func_5250'] = func_5250
mod = relay.transform.InferType()(mod)
mutated_mod['func_5250'] = func_5250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5250_call = mutated_mod.get_global_var('func_5250')
call_5251 = func_5250_call()
output = call_5251
func_5252 = relay.Function([], output)
mutated_mod['func_5252'] = func_5252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mod.get_global_var('func_3963')
func_3964_call = mutated_mod.get_global_var('func_3964')
call_5291 = func_3963_call()
call_5292 = func_3963_call()
output = relay.Tuple([call_5291,])
output2 = relay.Tuple([call_5292,])
func_5295 = relay.Function([], output)
mod['func_5295'] = func_5295
mod = relay.transform.InferType()(mod)
output = func_5295()
func_5296 = relay.Function([], output)
mutated_mod['func_5296'] = func_5296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5304 = relay.var("var_5304", dtype = "int64", shape = (12, 15, 12))#candidate|5304|(12, 15, 12)|var|int64
var_5305 = relay.var("var_5305", dtype = "int64", shape = (12, 15, 12))#candidate|5305|(12, 15, 12)|var|int64
bop_5306 = relay.bitwise_and(var_5304.astype('int64'), relay.reshape(var_5305.astype('int64'), relay.shape_of(var_5304))) # shape=(12, 15, 12)
output = bop_5306
output2 = bop_5306
func_5309 = relay.Function([var_5304,var_5305,], output)
mod['func_5309'] = func_5309
mod = relay.transform.InferType()(mod)
var_5310 = relay.var("var_5310", dtype = "int64", shape = (12, 15, 12))#candidate|5310|(12, 15, 12)|var|int64
var_5311 = relay.var("var_5311", dtype = "int64", shape = (12, 15, 12))#candidate|5311|(12, 15, 12)|var|int64
output = func_5309(var_5310,var_5311,)
func_5312 = relay.Function([var_5310,var_5311,], output)
mutated_mod['func_5312'] = func_5312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4145_call = mod.get_global_var('func_4145')
func_4146_call = mutated_mod.get_global_var('func_4146')
call_5316 = relay.TupleGetItem(func_4145_call(), 0)
call_5317 = relay.TupleGetItem(func_4146_call(), 0)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_5333 = func_927_call()
call_5334 = func_927_call()
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_5339 = func_1879_call()
call_5340 = func_1879_call()
func_2956_call = mod.get_global_var('func_2956')
func_2957_call = mutated_mod.get_global_var('func_2957')
call_5343 = func_2956_call()
call_5344 = func_2956_call()
output = relay.Tuple([call_5316,call_5333,call_5339,call_5343,])
output2 = relay.Tuple([call_5317,call_5334,call_5340,call_5344,])
func_5348 = relay.Function([], output)
mod['func_5348'] = func_5348
mod = relay.transform.InferType()(mod)
mutated_mod['func_5348'] = func_5348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5348_call = mutated_mod.get_global_var('func_5348')
call_5349 = func_5348_call()
output = call_5349
func_5350 = relay.Function([], output)
mutated_mod['func_5350'] = func_5350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5366 = relay.var("var_5366", dtype = "float64", shape = (1, 10, 7))#candidate|5366|(1, 10, 7)|var|float64
var_5367 = relay.var("var_5367", dtype = "float64", shape = (10, 10, 7))#candidate|5367|(10, 10, 7)|var|float64
bop_5368 = relay.add(var_5366.astype('float64'), var_5367.astype('float64')) # shape=(10, 10, 7)
output = relay.Tuple([bop_5368,])
output2 = relay.Tuple([bop_5368,])
func_5373 = relay.Function([var_5366,var_5367,], output)
mod['func_5373'] = func_5373
mod = relay.transform.InferType()(mod)
mutated_mod['func_5373'] = func_5373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5373_call = mutated_mod.get_global_var('func_5373')
var_5375 = relay.var("var_5375", dtype = "float64", shape = (1, 10, 7))#candidate|5375|(1, 10, 7)|var|float64
var_5376 = relay.var("var_5376", dtype = "float64", shape = (10, 10, 7))#candidate|5376|(10, 10, 7)|var|float64
call_5374 = func_5373_call(var_5375,var_5376,)
output = call_5374
func_5377 = relay.Function([var_5375,var_5376,], output)
mutated_mod['func_5377'] = func_5377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4664_call = mod.get_global_var('func_4664')
func_4665_call = mutated_mod.get_global_var('func_4665')
call_5421 = func_4664_call()
call_5422 = func_4664_call()
output = relay.Tuple([call_5421,])
output2 = relay.Tuple([call_5422,])
func_5432 = relay.Function([], output)
mod['func_5432'] = func_5432
mod = relay.transform.InferType()(mod)
output = func_5432()
func_5433 = relay.Function([], output)
mutated_mod['func_5433'] = func_5433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4156_call = mutated_mod.get_global_var('func_4156')
call_5436 = func_4154_call()
call_5437 = func_4154_call()
const_5468 = relay.const([-0.760641,-6.489264,2.147551,9.289794,-9.581373,-1.580158,7.726912,-3.447812,-8.068581,-4.635239,-9.556479,9.831328,-2.920909,4.936230,9.136883,9.443692,-9.770899,9.336862,3.131661,-3.469293,-2.375062,9.062166,-4.740523,1.450297,-4.064322,9.398064,8.571790,-8.803960,-8.086607,-5.049354,2.351408,8.941088,-7.327260,0.020799,-5.592156,6.284922,5.321854,-5.542907,-0.931967,-3.724982,4.660050,2.362050,-4.629420,-0.288158,-1.541119,6.903865,-8.356123,7.837746,3.771052,-4.521683,-4.153158,-9.426101,-7.679319,-3.365336,-1.184283,0.752985,-9.594800,-1.483147,-1.722816,-6.261019,-3.541588,-9.478533,-7.425098,8.163303,9.494885,2.688590,1.501934,9.259026,-0.410135,2.839000,-4.930306,-0.363391,2.929442,-0.696644,3.750451,-3.089249,-4.991352,-0.969633,-3.787310,-5.963011,9.648910,-1.452023,6.694024,-0.829166,7.051577,-7.410097,-3.667716,-8.266561,2.151351,-2.929790,2.397312,-4.804890,9.010868,6.364291,-9.074922,5.823166,9.049533,4.919308,4.151824,7.966713,7.491852,5.785943,-7.218478,7.724660,-5.284149,4.778005,4.241508,0.773748,-3.764490,-2.899768,-6.914857,8.017669,6.721886,-2.876590,-7.171882,8.233544,8.459569,-0.709362,8.784187,8.571137,9.847587,3.314121,9.621559,7.679569,6.742954,-9.338542,-8.698495,-8.210782,-9.323702,-7.433584,-2.562639,-4.133070,-1.982754,6.828053,0.245671,2.435668,6.572957,5.011862,0.721900,1.711579,-8.112982,-9.092032,7.970538,2.688620,7.050782,-2.902179,1.149114,4.818687,3.004403,7.386188,-9.305751,0.585608,-9.890151,-3.425977,-0.141333,-4.115139,1.633183,2.338037,8.329764,6.847358,-2.559197,-1.967321,-0.584232,-9.496486,1.504459,-6.141070,-7.152721,9.674149,-8.312888,8.903836,9.056959,-5.981882,-3.850515,2.628999,-8.065702,9.775527,3.727002,-1.669336,5.959655,4.074797,1.815022,-8.915932,-1.076409,-2.932786,4.411299,9.610607,8.968832,-7.084880,6.287139,-0.922780,-4.168931,-7.437888,6.450930,1.779879,1.961344,5.461618,3.377925,4.750575,-0.196617,-3.418444,5.584852,-7.539124,2.185823,-4.287784,1.273694,-2.766253,-2.345038,8.479965,-1.121320,2.108824,3.072299,-3.897411,-4.019448,-6.651580,7.578141,8.257924,-7.803364,9.832301,-0.582777,-2.453533,-7.060737,9.460140,-8.735866,9.502598,2.660570,-0.945216,7.154995,3.417034,-6.800968,-2.693958,2.685415,-6.298562,-8.427212,8.982190,-7.138045,-1.458289,1.900684,9.480033,-7.772008,-2.000936,0.790928,-1.793065,6.346879,9.196980,-4.733327,6.005978,1.720606,7.286251,2.180071,-8.785853,1.633035,5.361999,-8.076352,-8.110846,8.279642,-4.372432,2.448860,3.325477,0.707944,4.430467,5.876072,3.323428,-7.522503,-6.772197,5.461444,9.509137,8.122564,0.929628,-7.926638,-9.915360,-5.347070,-5.543583,9.023535,-5.659943,-4.691428,-0.840916,-4.989280,-3.004355,3.982051,1.113739,0.804751,6.516173,6.898112,-7.857968,-4.998551,4.448409,-4.361584,-4.293284,9.016326,-3.993471,-3.160318,4.437704,-9.327418,-6.956942,-2.427596,-4.028854,-6.111267,-8.131123,5.674135,1.985445,9.701651,-2.511262,0.261187,-9.186988,-6.237445,-5.849233,8.723453,5.765611,-1.502314,3.015187,1.771311,-6.363525,1.397668,7.121225,-3.463126], dtype = "float32")#candidate|5468|(315,)|const|float32
bop_5469 = relay.subtract(call_5436.astype('int8'), relay.reshape(const_5468.astype('int8'), relay.shape_of(call_5436))) # shape=(315,)
bop_5472 = relay.subtract(call_5437.astype('int8'), relay.reshape(const_5468.astype('int8'), relay.shape_of(call_5437))) # shape=(315,)
func_4475_call = mod.get_global_var('func_4475')
func_4477_call = mutated_mod.get_global_var('func_4477')
call_5474 = func_4475_call()
call_5475 = func_4475_call()
output = relay.Tuple([bop_5469,call_5474,])
output2 = relay.Tuple([bop_5472,call_5475,])
func_5477 = relay.Function([], output)
mod['func_5477'] = func_5477
mod = relay.transform.InferType()(mod)
mutated_mod['func_5477'] = func_5477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5477_call = mutated_mod.get_global_var('func_5477')
call_5478 = func_5477_call()
output = call_5478
func_5479 = relay.Function([], output)
mutated_mod['func_5479'] = func_5479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3514_call = mod.get_global_var('func_3514')
func_3515_call = mutated_mod.get_global_var('func_3515')
call_5482 = relay.TupleGetItem(func_3514_call(), 0)
call_5483 = relay.TupleGetItem(func_3515_call(), 0)
output = relay.Tuple([call_5482,])
output2 = relay.Tuple([call_5483,])
func_5487 = relay.Function([], output)
mod['func_5487'] = func_5487
mod = relay.transform.InferType()(mod)
output = func_5487()
func_5488 = relay.Function([], output)
mutated_mod['func_5488'] = func_5488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3194_call = mod.get_global_var('func_3194')
func_3196_call = mutated_mod.get_global_var('func_3196')
call_5489 = func_3194_call()
call_5490 = func_3194_call()
func_1232_call = mod.get_global_var('func_1232')
func_1234_call = mutated_mod.get_global_var('func_1234')
call_5497 = func_1232_call()
call_5498 = func_1232_call()
output = relay.Tuple([call_5489,call_5497,])
output2 = relay.Tuple([call_5490,call_5498,])
func_5501 = relay.Function([], output)
mod['func_5501'] = func_5501
mod = relay.transform.InferType()(mod)
output = func_5501()
func_5502 = relay.Function([], output)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3395_call = mod.get_global_var('func_3395')
func_3396_call = mutated_mod.get_global_var('func_3396')
call_5508 = relay.TupleGetItem(func_3395_call(), 0)
call_5509 = relay.TupleGetItem(func_3396_call(), 0)
func_4712_call = mod.get_global_var('func_4712')
func_4715_call = mutated_mod.get_global_var('func_4715')
const_5512 = relay.const([[-8,-2,-8,4,-9,-9,-4,-1,10,2,-3,2,8,7,-3,-1,-5,6,1,9,-4,4,-7,-2,1,2,-3,-3,-10,6],[-5,-4,3,-6,-1,-6,-5,-3,-7,7,9,2,-4,2,-7,-7,9,-5,-1,-7,-7,-5,5,-5,3,10,3,-1,-1,3],[3,-2,-1,-3,9,-5,2,9,10,-10,5,-2,-4,-5,7,-4,-8,-1,5,-3,3,-1,2,4,5,6,8,10,10,-8],[5,-7,8,4,-3,6,-9,-3,-10,-4,5,-6,-7,-4,2,-5,-3,2,2,3,-6,-1,9,-7,-5,3,-10,-2,5,-5],[-9,8,3,-3,5,-10,6,-6,-7,3,4,3,-7,3,2,-3,-10,-3,8,-10,2,5,-1,-3,6,2,4,-5,10,-2],[-8,5,5,-1,-6,7,-8,5,3,-10,6,10,5,10,5,-10,-7,9,3,-5,10,6,-4,7,-1,-8,-9,8,6,-1],[-9,2,-6,-8,-10,7,-6,-7,-5,10,3,4,8,8,-9,-5,-4,4,9,-10,-6,-10,-9,3,-3,-2,2,-10,8,-4],[-1,-5,7,4,3,4,8,-10,-1,2,5,-2,-2,7,2,-8,2,5,-3,5,10,5,-5,6,-9,2,4,3,4,-5],[3,9,-9,5,3,9,-1,-3,9,-4,10,4,-10,2,-7,2,10,-5,6,-2,10,-4,4,-1,7,-3,3,-2,4,-1],[-1,-1,6,2,6,3,-3,-8,2,-2,-7,5,2,-7,1,9,10,-3,-4,8,-6,5,-6,8,6,-7,5,-7,1,-5],[-9,-2,-4,7,9,7,6,7,-9,-2,-3,10,-2,8,8,-4,10,9,-3,4,-2,7,5,10,7,10,10,1,-6,5],[-2,4,9,6,10,1,-10,-9,-10,-2,-2,10,-4,-6,-8,4,-4,-4,2,2,-1,-3,1,10,3,-10,-4,-7,-9,-9],[-5,-1,-3,-9,-6,-8,-4,-9,-5,6,-1,-10,-9,5,1,-9,7,5,-2,7,-5,-4,-6,-6,10,-6,10,-7,-7,9],[4,-6,5,-5,6,-6,6,2,2,2,9,2,8,-10,-2,2,-6,-9,10,9,-5,-8,4,-3,-9,-8,-5,-10,2,7],[-1,-1,7,-10,-3,4,-6,9,4,6,-6,-4,9,-3,5,6,-9,3,-5,5,-1,-6,-1,7,-6,9,-9,3,6,-10],[4,-7,1,8,-4,-7,-2,-4,-7,-10,-5,-5,3,-2,-3,-2,-8,-9,10,6,2,8,6,9,-2,8,-10,-2,2,4],[6,-2,4,3,1,-7,-3,-9,7,-4,-8,6,5,1,-2,3,-10,4,6,-7,7,8,-6,-8,-6,4,5,2,-10,9],[9,-1,7,-2,-1,8,10,9,-4,3,-9,3,-6,6,-1,7,-5,10,4,-2,2,4,-7,-10,-9,-10,9,-4,8,1]], dtype = "int8")#candidate|5512|(18, 30)|const|int8
call_5511 = relay.TupleGetItem(func_4712_call(relay.reshape(const_5512.astype('int8'), [15, 9, 4])), 2)
call_5513 = relay.TupleGetItem(func_4715_call(relay.reshape(const_5512.astype('int8'), [15, 9, 4])), 2)
func_1685_call = mod.get_global_var('func_1685')
func_1687_call = mutated_mod.get_global_var('func_1687')
call_5533 = relay.TupleGetItem(func_1685_call(), 0)
call_5534 = relay.TupleGetItem(func_1687_call(), 0)
var_5542 = relay.var("var_5542", dtype = "int8", shape = (18, 30))#candidate|5542|(18, 30)|var|int8
bop_5543 = relay.left_shift(const_5512.astype('int16'), relay.reshape(var_5542.astype('int16'), relay.shape_of(const_5512))) # shape=(18, 30)
func_5295_call = mod.get_global_var('func_5295')
func_5296_call = mutated_mod.get_global_var('func_5296')
call_5550 = relay.TupleGetItem(func_5295_call(), 0)
call_5551 = relay.TupleGetItem(func_5296_call(), 0)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_5552 = relay.TupleGetItem(func_2548_call(), 0)
call_5553 = relay.TupleGetItem(func_2549_call(), 0)
const_5561 = relay.const([[-4,-10,-4,-9,-7,2,-7,-3,4,7,7,-9,-1,8,-9,-1,4,4,-6,-1,-5,10,5,-10,-7,2,-1,3,-4,-10],[-6,7,-10,7,1,10,-2,-9,-4,-5,-10,-7,10,2,2,8,-1,-7,-4,-1,-4,-3,1,-1,-3,-8,-5,-3,-2,8],[5,4,-9,-10,-5,9,2,-6,-6,-8,5,-3,8,5,8,-5,-7,10,-10,-10,1,-6,3,-6,1,1,7,-6,7,8],[-5,8,-4,10,9,10,-1,-3,-10,-5,-10,-7,-10,5,-6,-5,-5,-1,-3,2,-2,2,-3,-10,-3,-4,-3,1,5,1],[8,-2,-8,4,5,5,-2,-1,-1,8,7,-6,-4,-4,-4,2,-10,9,-7,-1,-10,-10,-3,-7,-3,10,-6,10,5,1],[-8,5,7,-8,-8,-9,-7,-3,3,7,-7,-5,3,-5,7,2,-10,3,-3,-4,-2,-1,5,1,8,-3,5,9,3,-8],[1,8,-9,1,-4,2,9,6,1,-1,5,3,-1,-10,6,7,-10,-1,7,-10,6,-8,-7,-8,-4,-9,-2,-1,-5,-7],[8,10,-10,8,10,8,-10,-2,3,-9,-10,5,1,5,6,-6,-8,4,-5,5,8,3,2,-9,7,9,4,-9,10,10],[-10,10,-3,7,-5,-7,-6,5,6,-2,-1,10,4,10,-7,-8,7,4,10,-1,-4,2,-7,-7,-2,-7,9,-8,-1,5],[-9,3,-10,-7,8,7,-4,-1,7,-7,-6,-2,4,-8,-6,-2,-5,-2,-4,5,-9,-6,-5,-8,-5,-1,-9,-8,3,-7],[6,-6,6,5,-9,4,5,2,6,-2,5,4,8,-7,7,-10,5,5,5,3,-10,-3,6,-3,-5,5,-10,-4,-2,-9],[-6,3,4,7,10,3,-9,-5,2,-9,-4,-7,-5,3,3,-10,1,-2,-3,-6,1,3,6,4,9,-6,-8,-9,3,4],[-6,-7,-8,-3,10,-6,-9,-10,10,-4,5,-3,-3,10,6,4,-8,10,1,-1,-3,1,-7,-8,5,3,1,5,-10,-4],[10,-10,-10,-6,-6,-2,-1,2,6,-4,-1,10,-5,-10,1,1,1,-10,2,3,-3,6,10,4,7,6,5,1,-3,2],[4,-7,-5,-7,-3,2,7,-1,-5,2,1,9,2,-7,-1,-10,4,-10,-4,-5,-9,-4,4,-1,10,-2,-1,-8,-1,9],[4,6,7,-7,7,2,9,-2,3,4,9,4,-7,3,9,-9,-9,1,3,9,-9,5,8,1,-1,5,-2,-7,3,-6],[-2,-5,2,-9,3,-6,-10,8,-8,-9,5,8,5,6,-7,-10,9,-10,-1,-7,-6,5,-6,5,-4,-3,-8,-8,-10,1],[-9,6,6,9,4,10,-1,-7,-1,-8,-7,-6,6,10,-10,-5,1,7,7,5,-1,5,-1,6,-7,9,-9,-10,10,-1]], dtype = "int8")#candidate|5561|(18, 30)|const|int8
bop_5562 = relay.power(var_5542.astype('float64'), relay.reshape(const_5561.astype('float64'), relay.shape_of(var_5542))) # shape=(18, 30)
bop_5567 = relay.not_equal(const_5512.astype('bool'), relay.reshape(bop_5562.astype('bool'), relay.shape_of(const_5512))) # shape=(18, 30)
bop_5570 = relay.add(bop_5567.astype('uint64'), relay.reshape(var_5542.astype('uint64'), relay.shape_of(bop_5567))) # shape=(18, 30)
uop_5582 = relay.atan(var_5542.astype('float64')) # shape=(18, 30)
func_4641_call = mod.get_global_var('func_4641')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_5589 = func_4641_call()
call_5590 = func_4641_call()
uop_5593 = relay.log2(uop_5582.astype('float64')) # shape=(18, 30)
uop_5597 = relay.sinh(uop_5593.astype('float32')) # shape=(18, 30)
func_2890_call = mod.get_global_var('func_2890')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_5601 = func_2890_call()
call_5602 = func_2890_call()
output = relay.Tuple([call_5508,call_5511,call_5533,bop_5543,call_5550,call_5552,bop_5570,call_5589,uop_5597,call_5601,])
output2 = relay.Tuple([call_5509,call_5513,call_5534,bop_5543,call_5551,call_5553,bop_5570,call_5590,uop_5597,call_5602,])
func_5605 = relay.Function([var_5542,], output)
mod['func_5605'] = func_5605
mod = relay.transform.InferType()(mod)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5606 = relay.var("var_5606", dtype = "int8", shape = (18, 30))#candidate|5606|(18, 30)|var|int8
func_5605_call = mutated_mod.get_global_var('func_5605')
call_5607 = func_5605_call(var_5606)
output = call_5607
func_5608 = relay.Function([var_5606], output)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5624 = relay.var("var_5624", dtype = "uint8", shape = (14, 15, 15))#candidate|5624|(14, 15, 15)|var|uint8
var_5625 = relay.var("var_5625", dtype = "uint8", shape = (14, 15, 15))#candidate|5625|(14, 15, 15)|var|uint8
bop_5626 = relay.right_shift(var_5624.astype('uint8'), relay.reshape(var_5625.astype('uint8'), relay.shape_of(var_5624))) # shape=(14, 15, 15)
output = relay.Tuple([bop_5626,])
output2 = relay.Tuple([bop_5626,])
func_5629 = relay.Function([var_5624,var_5625,], output)
mod['func_5629'] = func_5629
mod = relay.transform.InferType()(mod)
mutated_mod['func_5629'] = func_5629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5629_call = mutated_mod.get_global_var('func_5629')
var_5631 = relay.var("var_5631", dtype = "uint8", shape = (14, 15, 15))#candidate|5631|(14, 15, 15)|var|uint8
var_5632 = relay.var("var_5632", dtype = "uint8", shape = (14, 15, 15))#candidate|5632|(14, 15, 15)|var|uint8
call_5630 = func_5629_call(var_5631,var_5632,)
output = call_5630
func_5633 = relay.Function([var_5631,var_5632,], output)
mutated_mod['func_5633'] = func_5633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5664 = relay.var("var_5664", dtype = "float32", shape = (11, 10, 2))#candidate|5664|(11, 10, 2)|var|float32
uop_5665 = relay.sin(var_5664.astype('float32')) # shape=(11, 10, 2)
uop_5674 = relay.sinh(uop_5665.astype('float64')) # shape=(11, 10, 2)
uop_5680 = relay.asin(uop_5674.astype('float32')) # shape=(11, 10, 2)
output = relay.Tuple([uop_5680,])
output2 = relay.Tuple([uop_5680,])
func_5684 = relay.Function([var_5664,], output)
mod['func_5684'] = func_5684
mod = relay.transform.InferType()(mod)
var_5685 = relay.var("var_5685", dtype = "float32", shape = (11, 10, 2))#candidate|5685|(11, 10, 2)|var|float32
output = func_5684(var_5685)
func_5686 = relay.Function([var_5685], output)
mutated_mod['func_5686'] = func_5686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1972_call = mod.get_global_var('func_1972')
func_1973_call = mutated_mod.get_global_var('func_1973')
call_5729 = relay.TupleGetItem(func_1972_call(), 1)
call_5730 = relay.TupleGetItem(func_1973_call(), 1)
output = relay.Tuple([call_5729,])
output2 = relay.Tuple([call_5730,])
func_5735 = relay.Function([], output)
mod['func_5735'] = func_5735
mod = relay.transform.InferType()(mod)
output = func_5735()
func_5736 = relay.Function([], output)
mutated_mod['func_5736'] = func_5736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5193_call = mod.get_global_var('func_5193')
func_5194_call = mutated_mod.get_global_var('func_5194')
call_5743 = relay.TupleGetItem(func_5193_call(), 1)
call_5744 = relay.TupleGetItem(func_5194_call(), 1)
func_3416_call = mod.get_global_var('func_3416')
func_3418_call = mutated_mod.get_global_var('func_3418')
call_5750 = relay.TupleGetItem(func_3416_call(), 0)
call_5751 = relay.TupleGetItem(func_3418_call(), 0)
var_5764 = relay.var("var_5764", dtype = "uint16", shape = (105,))#candidate|5764|(105,)|var|uint16
bop_5765 = relay.logical_and(call_5750.astype('bool'), relay.reshape(var_5764.astype('bool'), relay.shape_of(call_5750))) # shape=(105,)
bop_5768 = relay.logical_and(call_5751.astype('bool'), relay.reshape(var_5764.astype('bool'), relay.shape_of(call_5751))) # shape=(105,)
func_5373_call = mod.get_global_var('func_5373')
func_5377_call = mutated_mod.get_global_var('func_5377')
const_5774 = relay.const([3.095782,8.711952,-6.071661,7.630769,4.057605,-2.388617,2.402238,-3.539308,-7.197355,2.740167,8.657575,-7.310196,-8.081420,3.549407,-1.925292,-0.851553,9.799337,-2.318124,6.731148,8.331862,9.223389,5.496934,3.506878,-7.616900,-4.159213,-4.468496,-7.414869,5.428182,4.989906,5.567255,-9.759567,6.525222,8.923189,1.502197,-5.067538,2.782874,6.850893,-0.263800,0.084830,-5.893555,-1.317577,6.328692,3.346612,-8.853007,7.549697,3.969374,7.576874,1.594787,-9.673581,7.164423,3.170290,-0.856423,-5.772106,-1.167471,3.958817,2.256482,6.345364,-0.949762,-4.782429,9.150634,-1.655257,3.832831,9.684650,9.187299,8.077431,-4.883246,4.776457,7.662946,3.433581,3.360438], dtype = "float64")#candidate|5774|(70,)|const|float64
const_5775 = relay.const([9.298506,8.653934,-9.959770,8.287904,4.921833,-1.742142,-0.603452,-7.880564,7.790919,-7.878735,6.570641,-5.488707,1.004471,6.655480,-2.548868,5.334097,9.085387,2.994942,8.294554,-5.791915,7.817784,-2.374753,-2.767527,-6.459031,4.695085,1.027302,-5.812191,-2.416330,0.606569,-8.175524,-3.731289,-3.019934,6.205412,9.074622,-2.157709,3.493505,-0.239657,4.051489,5.702084,-2.863679,5.887046,9.465485,0.470181,0.796775,-3.209389,4.696398,-5.229209,-0.559431,5.262297,-5.349996,3.066983,-9.313801,9.139595,6.512142,1.075766,-0.078854,0.150987,-5.849288,2.895488,9.608222,-8.670105,-8.852136,-5.448356,-2.648154,-1.541454,-5.560073,-6.420509,6.350147,-2.567527,-9.689852,1.744737,-8.542658,4.031352,3.927239,1.630496,-8.468519,7.650101,-4.968439,5.548222,-9.748150,8.646051,1.066876,2.830285,-2.980635,1.158324,9.403750,7.214484,9.857433,-3.936671,7.619314,-1.731089,5.482276,-4.030304,5.481908,-9.411416,7.330577,-3.914460,-3.100130,9.121315,-5.938383,7.877381,4.437437,1.339666,1.797409,-2.259343,3.503838,-6.734774,-0.699577,-3.527414,-0.495232,9.737550,9.040074,6.469655,9.497541,-3.782303,7.882087,5.497735,-4.566135,-2.861834,3.918812,-9.740200,7.977251,1.459558,6.521384,1.349805,3.560488,8.748845,6.936719,-4.692463,4.119898,-5.898278,-4.388377,-6.366586,-8.451862,8.080581,8.567594,2.307638,-6.023393,-4.712084,-6.709293,-4.031329,4.098323,-6.613321,-5.512654,6.878059,3.598680,-7.750713,-6.308479,-3.250260,1.958989,-4.782967,5.342572,2.828091,-0.096606,7.813743,-7.780299,-6.443383,4.080417,-9.752433,9.086625,-2.221062,9.875144,2.789945,2.829739,-6.669993,8.758773,3.381103,-7.112311,-6.770621,-5.347291,-1.960799,0.005704,-1.300318,0.165927,-7.366373,0.423676,-0.937218,-2.426077,-3.161317,5.347874,-3.132280,9.766037,-8.034242,3.724144,-9.807850,-5.693002,-1.615884,-8.186854,0.246941,0.088210,-4.572840,-9.883638,2.083836,-1.693964,-1.655028,-2.366703,-0.612716,-3.906293,-6.129227,-3.511407,9.570702,6.797040,-3.907867,4.475721,8.533886,-0.563873,9.958653,-4.631043,0.705002,-0.988758,6.262150,-0.369136,-5.853094,-4.265568,-6.995015,0.160796,3.488927,1.054892,-8.849126,3.462281,1.201591,-7.775445,-5.791801,7.038830,5.440984,0.889838,7.494242,2.482983,-4.171588,-3.313999,-4.521124,8.226610,-4.328548,7.311764,2.939490,-6.068224,-4.295123,4.450707,-7.172778,-1.725219,-4.477294,-6.306730,-8.170136,3.432438,8.488780,8.591386,5.222525,4.919342,-1.116052,6.352875,-7.279371,-9.216632,-8.898375,2.423806,1.116953,-4.317579,-6.985336,9.692155,-6.760797,4.515251,-1.568402,6.027511,7.882027,5.508590,-1.361595,0.024538,-0.015960,4.967407,8.025124,2.453890,9.259269,-5.858264,-3.524553,-3.366159,-6.704778,-1.971619,-5.107082,5.825882,8.896069,5.496036,6.694011,-7.931274,3.140843,-5.050261,-3.619069,4.295904,0.373988,1.605029,2.523474,7.419431,-2.899672,-1.952632,8.078394,-3.294704,-8.404887,-9.363837,7.969387,9.322278,6.066228,6.381157,-6.690296,2.719951,0.133923,4.024195,-5.434999,-5.678012,9.573918,7.492807,-2.416926,2.329734,-6.491562,-3.013044,-6.457012,-9.235584,3.533906,4.306785,-6.885129,-5.320832,-5.328167,-1.065815,-0.362498,2.295465,3.448158,-4.871559,-8.298917,-8.611515,-6.553684,-7.939339,-0.698595,-1.225595,4.452708,8.922618,-2.684677,0.528540,-3.569348,6.191829,-4.476605,-4.970302,9.364482,-2.127417,-5.192129,-5.723554,8.019678,1.422036,1.846003,-6.081514,5.804199,-8.132775,5.367172,-7.974508,2.367241,-4.854781,-4.762719,8.622374,4.102388,-8.831275,-8.392246,-1.398243,3.869184,-0.417501,0.372765,2.081725,-1.568900,-0.795798,5.218125,6.551851,-9.955786,5.992489,-7.973189,7.921316,-5.747057,0.109393,-7.450676,-6.020798,7.290899,1.235250,4.379725,-7.449170,-2.668067,6.080340,6.437576,6.930491,-4.377661,1.976017,3.798567,1.991984,-7.018778,8.754468,-0.790476,-9.638172,-7.375701,8.913388,8.295588,0.983043,-8.460789,7.114101,-7.310085,-3.112841,2.821254,2.324669,-3.142427,-2.816679,-2.232619,2.855087,-7.338947,-6.943363,2.737778,-0.895117,0.334834,5.297180,5.194478,-2.079063,0.815845,-0.926111,-5.103635,5.426890,-5.434781,4.146750,3.313562,-2.503465,-1.754130,-3.760822,-3.046391,-2.434437,4.747664,8.549985,7.718439,-9.320457,-6.541918,1.228929,-2.546252,6.799401,6.822794,3.820965,-0.239014,-7.767278,8.285420,-0.762303,9.716147,5.176512,-2.357399,6.287111,-7.415273,-7.727013,5.409056,6.810630,0.655790,-2.310144,1.610455,4.879473,5.189377,0.740311,4.877177,-0.449052,-0.810103,4.965838,0.774584,-7.674277,-9.789304,-2.980871,2.862234,2.627176,3.678948,5.027923,-8.001524,-4.170847,-6.532977,-2.332362,1.137695,-4.774120,-7.819248,8.692896,7.346320,-7.828279,-2.567266,0.151163,-0.828601,-4.346867,-4.680067,3.954721,2.314495,5.679629,8.733627,4.145051,-6.815885,-2.833982,6.644707,-9.905650,-1.384267,-0.342358,-0.718110,-2.294158,-7.263898,-2.062170,-0.837405,1.732461,5.421923,1.873409,-9.239787,1.242472,-4.422626,-1.349930,6.127666,-8.470389,7.664990,4.698383,-4.213253,-9.477788,-1.675668,-3.396940,-7.274117,-6.481185,-6.117410,-6.519360,-2.562967,1.878500,-2.837456,-4.222136,1.431813,9.333204,8.453344,-5.882617,-1.381122,4.491470,3.164534,3.480299,1.180321,0.782861,0.047492,7.552641,4.625396,-8.539717,-9.112123,-7.809875,-5.801191,-7.294354,-5.475050,1.779919,7.910113,4.540440,-1.129872,1.466637,0.321378,8.374158,-7.490218,-3.185749,-7.682380,8.797254,-0.692466,-1.061970,7.024013,-7.868717,0.358136,-1.496150,-8.798442,0.548714,-1.647280,9.783919,1.343687,-6.971021,5.792922,9.488517,-1.218596,-7.257142,-9.730458,7.917317,4.735399,5.775800,3.479573,8.926622,-0.306724,2.015191,0.789234,-4.992720,7.226441,3.086544,8.846486,-9.812775,6.711821,-6.340341,4.555738,-1.530274,-0.003626,5.927893,8.317831,3.481282,7.426933,2.603845,7.456894,2.628013,-9.229178,7.065532,-9.537899,7.036194,-6.290426,3.089710,9.298596,-7.082567,-4.428126,-3.904178,1.789563,1.313108,-0.742492,0.652594,-1.525716,-4.982751,9.669588,-9.384627,-5.896924,-0.946164,-3.085126,-6.297868,6.948348,9.930514,7.075051,4.386702,6.937562,5.610322,6.699963,-1.269710,-1.251318,7.358497,-6.343006,3.053828,2.748679,-5.525314,6.327201,-5.046734,7.837755,-8.854540,9.177894,5.574580,-4.373139,-4.160820,-5.722565,2.722778,3.415007,-1.654663,6.367514,-5.914327,2.068258,-0.392937,-3.631986,4.965478,-5.771930,-9.252846,-7.540918,-8.723756,-4.944742,-9.047494,2.768905,5.620634,-1.642788,1.757192,4.133607,3.175000,-2.153949,-8.220013,-9.470426,-2.988352,4.904913,-6.313505,8.650278,8.032869,2.516614,-6.630399,4.049189,1.066270,6.824235,3.786250,1.736286,-8.877514,-6.201355,-8.159503,-2.024154,1.931672,6.678071,4.087900,9.456405,-4.552602,7.767118,2.407309,1.496701,-9.607692,7.114778,4.560674,-3.029523,-2.241592,-8.493961,6.138266,-7.818960,8.663335,-0.657600,-7.430165,1.611826,-0.736952,6.704133,1.583184,5.323903,5.856735], dtype = "float64")#candidate|5775|(700,)|const|float64
call_5773 = relay.TupleGetItem(func_5373_call(relay.reshape(const_5774.astype('float64'), [1, 10, 7]), relay.reshape(const_5775.astype('float64'), [10, 10, 7]), ), 0)
call_5776 = relay.TupleGetItem(func_5377_call(relay.reshape(const_5774.astype('float64'), [1, 10, 7]), relay.reshape(const_5775.astype('float64'), [10, 10, 7]), ), 0)
func_3648_call = mod.get_global_var('func_3648')
func_3652_call = mutated_mod.get_global_var('func_3652')
const_5810 = relay.const([-1,5,2,-2,-6,-3,1,8,1,-2,-4,-2,6,-9,-10,6,-9,1,7,-6,2,-3,-9,10,-2,-1,-5,-1,-8,9,5,9,-10,-5,8,9,-1,3,-5,2,-5,6,-7,-1,7,4,7,6,-6,4,2,-3,10,-5,-1,4,1,6,-9,6,6,10,5,-3,-8,-4,4,5,5,9,-8,-2,3,8,4,7,-4,-7,4,-8,1,-3,1,-7,8,4,8,-3,-5,-4,5,-1,10,-5,-2,-5], dtype = "uint16")#candidate|5810|(96,)|const|uint16
call_5809 = relay.TupleGetItem(func_3648_call(relay.reshape(const_5810.astype('uint16'), [3, 4, 8]), relay.reshape(const_5810.astype('uint16'), [3, 4, 8]), ), 0)
call_5811 = relay.TupleGetItem(func_3652_call(relay.reshape(const_5810.astype('uint16'), [3, 4, 8]), relay.reshape(const_5810.astype('uint16'), [3, 4, 8]), ), 0)
uop_5815 = relay.acosh(const_5775.astype('float32')) # shape=(700,)
var_5822 = relay.var("var_5822", dtype = "float32", shape = (700,))#candidate|5822|(700,)|var|float32
bop_5823 = relay.floor_mod(uop_5815.astype('float64'), relay.reshape(var_5822.astype('float64'), relay.shape_of(uop_5815))) # shape=(700,)
func_709_call = mod.get_global_var('func_709')
func_711_call = mutated_mod.get_global_var('func_711')
const_5832 = relay.const([-0.479534,-0.963265,-6.252933,-3.254146,4.115586,5.226210,2.780483,-5.444529,-4.435034,0.449021,9.058727,1.285019,-3.158260,-9.353832,2.380980,-4.071505,-4.114268,-1.280604,2.678806,0.402238,7.629340,1.565251,4.805381,-1.654252,-0.143206,-1.839491,-4.518533,-1.166695,8.906565,-1.764482,2.312159,-2.240145,2.161603,5.882900,8.027411,3.827699,4.324078,-4.743624,4.878919,-0.518681,-6.678568,9.449010,-2.599134,2.951792,-1.549950,-3.069770,3.985477,6.161298,5.298066,1.029597,-2.957995,5.118909,-2.674176,-5.401318,6.413459,1.507886,-3.608909,-6.891535,-0.116634,-6.926470,8.100865,-2.577030,6.997529,-0.150703,-1.887772,-1.117961,-8.504896,-2.015333,5.967369,-6.116399,6.645218,-1.598847,-1.899781,-5.533197,3.745286,-7.190156,0.887502,4.193751,-3.080263,-8.029742,4.814311,2.911974,-7.463355,-5.767212,2.337193,-6.650170,-2.904496,-7.025888,2.517128,2.759711,7.507241,-1.567827,2.965014,5.749222,1.775962,-8.809393,-9.705430,-2.190885,-1.698777,-7.805508,-0.883409,-8.040606,-2.127184,0.870387,-5.909435,-4.477489,-1.171910,-4.801592,-4.266480,-9.198501,2.299455,-0.354221,-8.235057,9.107458,-8.946236,-3.752299,-7.438715,1.855280,9.325257,6.774654,-8.609993,9.259996,-9.562495,-0.648897,-4.425408,-4.586996,4.246761,8.079562,7.826964,-3.325764,5.549748,-8.688808,-6.333654,-1.239297,5.493855,4.742556,3.436335,-8.162162,-3.456359,-1.990933,4.737679,2.719802,4.629934,0.742504,5.796936,-4.698969,-0.646464,-1.629065,7.358146,7.157531,-6.043574,-8.550420,4.037219,0.776592,3.356481,-3.767687,-3.518832,2.732239,4.799681,3.118732,5.150013,0.638678,-8.776980,-4.355770,-3.401239,-6.168027,-2.069362,-0.629304,-8.627817,5.199500,0.401737,-9.641771,1.712325,2.314985,-1.849089,9.039910,4.661917,-9.381380,9.568473,5.192819,-3.278973,-5.323084,-2.294494,-6.272034,8.830195,-6.524728,-0.113452,-4.086905,-0.590657,-8.995938,-4.545228,-2.603109,-9.858369,-1.579389,8.752137,3.792892,2.160592,-4.487576,-1.963176,-8.524333,1.637173,-8.503486,-0.587658,8.023001,-2.847503,7.480331,-6.260355,-3.719846,-5.981941,-9.553203,-0.738092,1.142340,1.467108,0.220986,6.619732,0.599935,-0.039982,-8.927881,5.640541,-5.916329,2.918431,-0.324467,0.682047,-2.435352,4.720567,-5.579462,-2.334916,-5.829113,7.303869,4.951443,3.760647,6.172767,-9.072931,-1.053129,-9.545904,8.549287,6.352846,5.239901,2.962613,-4.197020,-7.555158,-1.959138,9.226033,-8.163701,5.760893,7.935754,6.676337,-6.042419,-5.816409,1.577206,6.486278,-2.302138,-0.481334,-8.723266,7.969161,0.060377,4.860553,-5.630936,-3.986019,5.775495,-0.802135,-9.789401,-1.958787,9.318037,-8.028098,6.075058,1.553779,-7.695270,5.841527,9.289494,1.847665,-5.052684,3.849483,2.491671,3.690965,6.780675,3.640371,4.258542,-9.629057,-6.573178,1.314446,7.713117,4.322843,9.864999,-1.709287,0.207939,6.048014,-4.805679,-4.602327,-7.956887,-0.204208,1.915659,4.655646,4.210621,6.442786,-8.828499,7.242095,-8.786694,7.702591,7.894033,-7.262780,-6.454623,-8.556514,-3.459277,-9.077725,5.227266,-8.860888,4.139738,6.682149,-0.191645,-2.233957,-5.703923,-6.108765,7.607735,-3.349699,1.384004,8.012545,-6.003849,-1.937531,3.535259,2.229074,1.216027,9.272328,0.776796,-1.598598,-7.087330,8.039918,-4.869650,7.118079,5.539433,2.953451,-3.199689,-1.044306,-9.055833,-1.492799,-5.165416,-8.467675,1.699706,-9.680132,6.555864,-7.238187,0.499755,-3.229783,2.692933,4.620754,9.467923,1.337443,-9.190518,-4.595244,-5.407203,-1.691078,-1.698986,8.801224,-8.718952,-5.510047,-8.458438,9.870554,-7.516959,1.731305,6.177406,8.957995,8.813322,9.903636,-6.192806,8.794752,-0.163230,3.814215,-8.045557,-1.540216,-0.085787,-7.576366,-8.194230,6.460847,6.396587,-9.574001,6.293129,1.259792,9.885220,-0.544583,-8.606635,-2.703736,6.925124,1.056290,-8.040195,1.410949,2.102053,9.790494,4.345337,-7.604783,-3.707938,-1.547856,-3.046348,-9.366865,-1.117607,-9.963420,-0.180917,7.851792,-9.644007,-2.304223,-3.989398,-9.956226,1.138832,4.278463,-5.979942,-8.571354,3.249403,-7.897271,-8.608305,7.179206,-1.684631,-8.828634,-6.066371,-4.843133,-0.046541,-1.043748,-9.282741,-5.281592,-7.405360,0.676968,-9.838242,6.266682,-7.426255,5.123114,7.791743,3.113767,-1.240932,-0.567508,8.728080,-5.504207,5.256448,-5.998818,8.426551,-9.792682,5.996804,-6.871137,8.115467,3.332669,8.153340,-4.488350,4.998762,-2.588541,9.875864,-1.108691,-0.754358,2.314891,9.843503,1.038151,-2.692214,6.849422,0.604551,0.763281,9.019217,-7.712256,-7.048927,2.034942,-1.012518,5.610532,1.215412,-8.044122,-2.401350,1.648782,-0.843362,-1.628344,-5.022537,-3.793537,2.205775,-3.804210,-0.561362,-9.824063,-5.969264,-1.956173,9.309200,-1.186139,6.624965,-7.654383,-2.205747,-7.046170,6.751185,-6.288548,-9.657775,7.750244,-1.748745,-7.339668,7.217889,6.478317,6.008370,-2.323946,-1.131963,2.525950,-2.686657,0.694896,5.134988,0.256936,2.006976,9.701357,-2.324662,6.647798,-7.556148,4.562787,-9.117960,4.220290,-9.948465,1.531360,3.353495,-8.303698,-7.943325,-4.663655,5.248671,-8.342638,4.852363,-5.957833,2.858851,2.804199,-4.720149,9.694595,6.617228,-3.412361,-1.787419,-7.642036,-0.596278,0.882475,0.185834,-9.787169,3.915901,1.880655,-4.911331,-8.785865,6.664222,-9.516248,-7.022200,2.189302,-7.284123,0.562396,8.671948,-5.475874,7.814093,-7.831303,-1.858289,8.267428,-9.105852,-5.478725,9.238984,-7.581452,-8.956122,-8.299576,-5.902672,7.385066,4.205560,8.216061,-9.788367,-3.745942,-7.011032,-5.241511,9.319069,-1.229840,-0.580316,0.654991,-4.893425,2.328224,-1.901364,6.289563,5.321429,1.450365,-1.213282,7.307401,6.287530,-5.601321,-5.294896,-5.890246,-0.691802,6.545433,1.303857,-6.315000,-2.395545,7.184786,9.920422,7.211513,5.964198,9.532209,-8.792355,-7.941700,-5.960962,5.163992,-7.792587,8.430415,-0.020477,5.560432,0.789913,4.103605,5.768268,-7.907996,-3.647766,9.806703,-1.750985,4.590078,3.017624,-7.069543,-8.585013,2.414811,3.964094,7.972632,2.278793,-3.267221,5.928244,6.730335,-8.738645,4.219615,8.487625,-0.707574,-5.556382,-6.954881,1.248361,3.895909,-5.144337,-5.290355,5.229388,-3.823265,0.912696,5.286640,-8.907092,6.872424,-7.562793,9.204835,-2.038861,-2.504536,0.582029,-3.292514,9.751745,-7.120653,-6.996852,-7.235377,9.431017,6.027981,0.320616,6.606539,8.056225,-3.043811,8.387946,1.707608,5.752148,-1.606546,1.081168,3.657486,8.286738,-9.983734,1.343146,0.154200,6.373640,3.108340,-6.193507,5.467490,5.493108,7.320630,3.509097,-4.565593,-1.319049,-2.455109,-8.501534,3.232795,7.480046,3.004979,-2.203391,3.228933,8.861618,-5.605641,7.412713,8.774920,5.121318,-8.894615,-0.410897,3.953752,7.629162,-5.098079,2.523050,3.469893,8.061887,6.645514,-9.900750,-4.644516,7.172668,8.392121,-2.427516,-0.163624,8.158445,-4.793346,6.266946,9.280249,6.021328,-1.911954,7.899857,-0.886275,7.968529,-0.904864,-1.308296,6.222205,3.907710,5.994358,-8.805518,3.982799,-7.541300,3.777103,2.499747,-7.744852,-1.990029,1.786058,5.055841,-0.884454,-6.698401,-2.017394,0.912761,-8.536264,-6.788766,-0.101482,3.308588,-4.382164,-8.144270,-4.852429,-0.731287,-4.281592,1.091283,-9.156708,5.677778,4.835735,1.609521,0.823027,-2.957537,2.504557,6.620631,1.988359,3.793029,-0.128351,5.547978,7.903133,3.705154,-2.380965,-1.882051,1.065910,8.359808,9.278501,-9.679348,-8.709870,-3.178585,9.585675,7.434419,6.773002,9.875211,-3.854729,-0.810702,-7.649890,-7.989375,-2.630776,-0.457236,-3.814268,7.192990,-1.006362,-5.835467,-6.080292,2.980184,-1.354965,-6.677536,0.728812,5.804866,-0.692107,-3.521297,-7.702435,1.561540,7.078394,-2.244210,0.448369,0.772360,-9.586161,-7.496093,-5.305618,-4.438474,2.670850,-9.395951,-6.747694,-0.791838,8.928362,-7.446417,9.417979,2.002480,4.812171,8.357575,3.105330,-7.032554,-2.146531,-1.620482,-8.452058,-0.198116,7.858413,3.700159,-3.936555,-8.298487,-6.290625,4.302003,-5.659248,-3.437761,6.748207,-8.326782,-5.262227,-8.527918,-8.734561,4.522297,3.435850,-4.578145,9.157721,2.125888,8.065402,9.941666,-7.266483,-8.736070,4.301054,-1.962029,-5.644739,4.223012,3.159007,3.801876,-1.548222,6.861882,-2.372820,-4.028642,0.919743,-8.108910,9.750789,-9.666417,-7.935331,-4.813112,1.694996,-3.711293,-8.541353,-3.657556,3.566296,9.213450,-0.971307,-1.688259,-2.334061,-0.903054,-7.010307,-5.635935,9.030160,5.949151,7.903460,0.785188,-1.207033,-4.900571,-0.355621,-1.400404,9.081481,6.385256,-1.593882,-8.819055,7.367026,-0.344889,7.956724,2.635776,7.005604,8.336200,8.234613,3.450020,-7.673293,-7.690423,-7.279175,3.976882,-9.207674,-8.182455,-8.857691,7.726782,2.605683,4.287093,-0.960989,7.711883,8.197125,3.285510,-0.463435,-3.874613,-1.925780,2.624769,1.514977,-9.719264,8.973479,9.396044,-6.071910,8.515106,-0.318024,-9.932199,-5.907865,3.258207,-3.019412,-5.731081,7.011319,-1.336582,2.815740,2.974490,-3.199289,-1.064653,-7.475600,8.432031,-8.825899,-5.162592,5.783789,2.061231,9.627888,4.352668,9.979204,-9.894722,-8.845370,1.229675,-2.798165,-9.068872,-0.298852,-0.702904,-9.504984,1.795528,0.222280,-3.217545,5.463187,-4.046104,-9.024351,-4.612079,6.318453,-5.035314,9.980654,2.911792,-0.350996,-0.695426,-4.866853,6.733618,-7.205384,8.399634,8.953693,-9.272339,5.342460,0.051484,-6.848648,-7.945410,-1.011284,5.044647,-6.348369,0.946314,9.608331,5.105143,-5.481680,-1.909201,-5.144144,-2.035824,0.705581,-4.277357,3.341286,-9.191575,2.918209,1.522853,-9.695747,-2.886331,3.099373,8.098421,3.022106,-4.974833,-1.629425,7.294385,-7.736645,-6.096206,-1.440931,8.343829,-3.427405,-0.304732,-9.033064,1.660424,-1.153271,0.627072,0.049234,-4.394372,4.065656,-2.287090,-9.949960,-4.541464,-2.678048,-1.217162,8.949703,-7.128132,-6.436124,-4.705791,2.421916,6.557641,0.009682,4.196564,0.006819,5.428289,1.196846,-5.805645,2.895947,-8.937424,5.801104,0.266593,-2.647828,-4.100194,-8.231646,2.054883,-0.797714,7.574818,8.585842,-5.671729,8.116403,-3.011443,-2.113205,-5.277502,3.375807,5.983117,4.357786,-1.964450,-4.717603,-0.345481,2.796165,-1.888884,-2.570116,4.860392,6.951942,0.016864,3.953723,6.319598,-5.620618,-6.639335,-7.845678,1.283377,-4.479241,-0.849957,-1.027201,4.209819,-0.989741,-9.628294,3.822952,6.712918,6.458819,6.399033,-9.233031,-5.072182,-4.213643,-0.408031,-0.057483,6.511490,1.713057,-6.813402,-5.734070,3.474994,1.447057,-8.999065,9.960759,5.354510,-2.058381,-6.320210,5.627721,0.637470,7.507696,5.305292,5.395079,-7.505694,-7.115466,4.181002,-2.030782,7.661552,-2.364307,-9.343377,5.054347,-3.599507,4.222215,-8.791265,-4.130014,-8.733863,-1.950507,4.239079,-2.043293,-5.231229,-4.922814,-8.075426,0.779363,0.794859,2.359036,9.395723,6.765139,-0.795699,-7.969937,-3.117818,-4.845024,-0.525795,-8.575797,5.970770,8.080658,2.124444,2.702708,-3.015737,4.571118,-2.576882,-2.818909,-1.123581,9.790111,-8.533149,4.565757,-1.482802,6.356040,-9.259955,1.662172,8.933861,-3.343611,-9.273830,-2.206578,-0.750827,-5.275452,-4.337630,-5.189720,3.913285,4.308297,-0.105861,-8.525921,-2.744075,2.016505,0.794636,-8.375248,-6.075468,0.973613,-1.028238,7.956927,3.847209,3.296214,-9.217345,-1.565275,-3.624229,1.528606,6.039895,0.909238,-8.121905,-3.137882,4.953990,-3.731038,6.875956,9.891289,2.428735,-0.206142,-0.720954,-1.265940,-7.884936,-8.162680,-2.354353,5.508712,2.938845,1.259046,2.845055,6.676933,2.444332,-8.812077,2.423281,-4.436767,9.869216,-2.449029,7.265698,-6.918321,9.532149,-7.421623,4.687460,3.743511,-8.901919,-3.296121,7.347703,4.489390,4.424481,6.602420,7.163997,7.373042,1.366755,-9.760146,-9.409169,-3.328439,-7.842854,5.983262,-4.297633,-1.666537,9.678436,-6.688628,7.402727,2.376945,-2.517680,8.606468,5.803393,-9.997397,-1.070138,1.076380,6.753797,8.257699,-3.868785,1.190485,6.173561,9.868099,-3.836050,6.297506,3.245705,-2.085751,-5.891290,8.626258,-7.752630,-5.750655,3.153722,4.746567,1.223277,-4.777896,5.809492,-4.476466,0.134348,-8.587224,9.985641,9.948510,-2.050205,-2.991033,-8.703630,-9.680226,8.055482,6.880923,-1.711290,-7.778601,2.290258,5.539231,-3.661978,-6.313633,-6.117296,-7.956782,-9.528111,-5.359882,2.261581,4.797088,7.943618,5.683798,-6.351000,1.085328,7.747603,-7.806401,-2.199717,-4.658426,7.937170,-7.748149,3.341135,-8.095511,8.290115,-7.700078,7.237875,-4.230544,-0.501072,-9.000757,-7.398798,3.321160,9.382857,5.586486,-4.361914,-1.286269,-6.288822,8.462899,9.848688,2.024697,-4.932547,-4.697212,-5.676727,-6.425968,-8.875324,3.102980,-6.487176,-8.221906,5.912782,5.661211,0.575006,1.842645,2.303938,0.267458,-0.514854,1.666869,6.690619,5.312065,-9.174691,-7.335507,-1.078650,9.061089,-9.634969,-6.776555,9.428055,3.055343,9.260594,-4.945340,7.867798,-7.521733,1.117732,9.984938,1.473260,-1.809367,-3.820532,-3.742376,-4.235176,-2.861370,7.696628,-3.925757,-6.797315,-3.424580,0.200862,-1.040435,-8.932278,-3.499487,-3.966417,-3.492628,-4.787217,9.278737,4.137969,9.973050,-7.957736,4.148997,-5.884390,-7.277132,7.726795,6.672779,-5.995146,-9.578757,-8.637230,-7.347855,-2.561535,-9.187724,1.878499,4.099458,8.106342,-9.373790,-8.582053,3.730951,-2.802706,-8.671168,-1.571563,-3.587627,5.578950,-9.927646,3.942256,2.736727,7.744974,9.714198,1.997029,-7.167069,1.329450,-9.841966,-5.389719,3.863563,-3.326003,-5.306693,6.132669,2.352755,3.571808,-1.982761,-6.973213,-3.212030,6.404261,-5.666409,1.431741,4.821128,2.539900,-8.630641,3.894585,-2.692554,0.889125,6.642640,6.433605,-9.426474,-0.578776,-5.515154,-8.209865,-3.643630,-3.096803,-1.217380,8.621673,-2.847746,-5.414781,-9.318221,-7.892615,1.295603,-6.513332,-8.215938,9.506024,-3.864510,3.849122,-1.439926,-5.793808,6.892882,4.258079,-9.146639,7.641596,2.431783,5.337977,-0.278253,3.761133,-3.122188,-6.606234,2.742032,3.769823,0.551264,-2.152181,-2.505915,-0.155817,1.520709,7.277472,4.227634,6.262910,-9.840121,-9.519707,-8.616968,-9.175498,8.073722,-0.480184,-5.261367,2.041103,-5.059211,9.157455,-7.157495,2.059706,0.873980,9.990851,6.963861,-3.432410,7.772718,-6.099804,-3.129090,-8.490038,1.252372,-7.838599,-5.233042,2.313319,-2.261252,7.336973,5.258603,-4.501041,-9.365028,4.877678,-8.351482,0.034309,-7.022830,-7.589041,0.911483,7.623005,0.733625,-6.644705,5.183295,-7.241323], dtype = "float64")#candidate|5832|(1440,)|const|float64
call_5831 = relay.TupleGetItem(func_709_call(relay.reshape(const_5832.astype('float64'), [12, 15, 8])), 0)
call_5833 = relay.TupleGetItem(func_711_call(relay.reshape(const_5832.astype('float64'), [12, 15, 8])), 0)
func_4863_call = mod.get_global_var('func_4863')
func_4865_call = mutated_mod.get_global_var('func_4865')
call_5834 = relay.TupleGetItem(func_4863_call(), 1)
call_5835 = relay.TupleGetItem(func_4865_call(), 1)
func_2890_call = mod.get_global_var('func_2890')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_5839 = func_2890_call()
call_5840 = func_2890_call()
func_2956_call = mod.get_global_var('func_2956')
func_2957_call = mutated_mod.get_global_var('func_2957')
call_5845 = func_2956_call()
call_5846 = func_2956_call()
func_1879_call = mod.get_global_var('func_1879')
func_1880_call = mutated_mod.get_global_var('func_1880')
call_5859 = func_1879_call()
call_5860 = func_1879_call()
func_4641_call = mod.get_global_var('func_4641')
func_4642_call = mutated_mod.get_global_var('func_4642')
call_5863 = func_4641_call()
call_5864 = func_4641_call()
func_5193_call = mod.get_global_var('func_5193')
func_5194_call = mutated_mod.get_global_var('func_5194')
call_5871 = relay.TupleGetItem(func_5193_call(), 1)
call_5872 = relay.TupleGetItem(func_5194_call(), 1)
bop_5880 = relay.left_shift(bop_5823.astype('uint64'), relay.reshape(uop_5815.astype('uint64'), relay.shape_of(bop_5823))) # shape=(700,)
output = relay.Tuple([call_5743,bop_5765,call_5773,const_5774,call_5809,const_5810,call_5831,const_5832,call_5834,call_5839,call_5845,call_5859,call_5863,call_5871,bop_5880,])
output2 = relay.Tuple([call_5744,bop_5768,call_5776,const_5774,call_5811,const_5810,call_5833,const_5832,call_5835,call_5840,call_5846,call_5860,call_5864,call_5872,bop_5880,])
func_5894 = relay.Function([var_5764,var_5822,], output)
mod['func_5894'] = func_5894
mod = relay.transform.InferType()(mod)
var_5895 = relay.var("var_5895", dtype = "uint16", shape = (105,))#candidate|5895|(105,)|var|uint16
var_5896 = relay.var("var_5896", dtype = "float32", shape = (700,))#candidate|5896|(700,)|var|float32
output = func_5894(var_5895,var_5896,)
func_5897 = relay.Function([var_5895,var_5896,], output)
mutated_mod['func_5897'] = func_5897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5193_call = mod.get_global_var('func_5193')
func_5194_call = mutated_mod.get_global_var('func_5194')
call_5902 = relay.TupleGetItem(func_5193_call(), 0)
call_5903 = relay.TupleGetItem(func_5194_call(), 0)
var_5922 = relay.var("var_5922", dtype = "float64", shape = (8, 13, 11))#candidate|5922|(8, 13, 11)|var|float64
bop_5923 = relay.less_equal(call_5902.astype('bool'), relay.reshape(var_5922.astype('bool'), relay.shape_of(call_5902))) # shape=(8, 13, 11)
bop_5926 = relay.less_equal(call_5903.astype('bool'), relay.reshape(var_5922.astype('bool'), relay.shape_of(call_5903))) # shape=(8, 13, 11)
func_2834_call = mod.get_global_var('func_2834')
func_2835_call = mutated_mod.get_global_var('func_2835')
call_5927 = relay.TupleGetItem(func_2834_call(), 0)
call_5928 = relay.TupleGetItem(func_2835_call(), 0)
output = relay.Tuple([bop_5923,call_5927,])
output2 = relay.Tuple([bop_5926,call_5928,])
func_5944 = relay.Function([var_5922,], output)
mod['func_5944'] = func_5944
mod = relay.transform.InferType()(mod)
var_5945 = relay.var("var_5945", dtype = "float64", shape = (8, 13, 11))#candidate|5945|(8, 13, 11)|var|float64
output = func_5944(var_5945)
func_5946 = relay.Function([var_5945], output)
mutated_mod['func_5946'] = func_5946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1866_call = mod.get_global_var('func_1866')
func_1867_call = mutated_mod.get_global_var('func_1867')
call_5964 = relay.TupleGetItem(func_1866_call(), 0)
call_5965 = relay.TupleGetItem(func_1867_call(), 0)
output = call_5964
output2 = call_5965
func_5974 = relay.Function([], output)
mod['func_5974'] = func_5974
mod = relay.transform.InferType()(mod)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5974_call = mutated_mod.get_global_var('func_5974')
call_5975 = func_5974_call()
output = call_5975
func_5976 = relay.Function([], output)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2771_call = mod.get_global_var('func_2771')
func_2772_call = mutated_mod.get_global_var('func_2772')
call_6008 = relay.TupleGetItem(func_2771_call(), 0)
call_6009 = relay.TupleGetItem(func_2772_call(), 0)
func_1186_call = mod.get_global_var('func_1186')
func_1188_call = mutated_mod.get_global_var('func_1188')
call_6018 = relay.TupleGetItem(func_1186_call(), 0)
call_6019 = relay.TupleGetItem(func_1188_call(), 0)
output = relay.Tuple([call_6008,call_6018,])
output2 = relay.Tuple([call_6009,call_6019,])
func_6030 = relay.Function([], output)
mod['func_6030'] = func_6030
mod = relay.transform.InferType()(mod)
output = func_6030()
func_6031 = relay.Function([], output)
mutated_mod['func_6031'] = func_6031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4507_call = mod.get_global_var('func_4507')
func_4509_call = mutated_mod.get_global_var('func_4509')
call_6054 = func_4507_call()
call_6055 = func_4507_call()
var_6085 = relay.var("var_6085", dtype = "float32", shape = (315,))#candidate|6085|(315,)|var|float32
bop_6086 = relay.add(call_6054.astype('uint8'), relay.reshape(var_6085.astype('uint8'), relay.shape_of(call_6054))) # shape=(315,)
bop_6089 = relay.add(call_6055.astype('uint8'), relay.reshape(var_6085.astype('uint8'), relay.shape_of(call_6055))) # shape=(315,)
output = bop_6086
output2 = bop_6089
func_6090 = relay.Function([var_6085,], output)
mod['func_6090'] = func_6090
mod = relay.transform.InferType()(mod)
mutated_mod['func_6090'] = func_6090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6091 = relay.var("var_6091", dtype = "float32", shape = (315,))#candidate|6091|(315,)|var|float32
func_6090_call = mutated_mod.get_global_var('func_6090')
call_6092 = func_6090_call(var_6091)
output = call_6092
func_6093 = relay.Function([var_6091], output)
mutated_mod['func_6093'] = func_6093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_608_call = mod.get_global_var('func_608')
func_609_call = mutated_mod.get_global_var('func_609')
call_6112 = relay.TupleGetItem(func_608_call(), 0)
call_6113 = relay.TupleGetItem(func_609_call(), 0)
func_2771_call = mod.get_global_var('func_2771')
func_2772_call = mutated_mod.get_global_var('func_2772')
call_6124 = relay.TupleGetItem(func_2771_call(), 4)
call_6125 = relay.TupleGetItem(func_2772_call(), 4)
output = relay.Tuple([call_6112,call_6124,])
output2 = relay.Tuple([call_6113,call_6125,])
func_6143 = relay.Function([], output)
mod['func_6143'] = func_6143
mod = relay.transform.InferType()(mod)
output = func_6143()
func_6144 = relay.Function([], output)
mutated_mod['func_6144'] = func_6144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3337_call = mod.get_global_var('func_3337')
func_3338_call = mutated_mod.get_global_var('func_3338')
call_6186 = relay.TupleGetItem(func_3337_call(), 0)
call_6187 = relay.TupleGetItem(func_3338_call(), 0)
output = relay.Tuple([call_6186,])
output2 = relay.Tuple([call_6187,])
func_6225 = relay.Function([], output)
mod['func_6225'] = func_6225
mod = relay.transform.InferType()(mod)
output = func_6225()
func_6226 = relay.Function([], output)
mutated_mod['func_6226'] = func_6226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4188_call = mod.get_global_var('func_4188')
func_4190_call = mutated_mod.get_global_var('func_4190')
call_6248 = relay.TupleGetItem(func_4188_call(), 0)
call_6249 = relay.TupleGetItem(func_4190_call(), 0)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_6261 = func_927_call()
call_6262 = func_927_call()
func_575_call = mod.get_global_var('func_575')
func_576_call = mutated_mod.get_global_var('func_576')
call_6295 = func_575_call()
call_6296 = func_575_call()
func_2409_call = mod.get_global_var('func_2409')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_6317 = relay.TupleGetItem(func_2409_call(), 0)
call_6318 = relay.TupleGetItem(func_2411_call(), 0)
output = relay.Tuple([call_6248,call_6261,call_6295,call_6317,])
output2 = relay.Tuple([call_6249,call_6262,call_6296,call_6318,])
func_6320 = relay.Function([], output)
mod['func_6320'] = func_6320
mod = relay.transform.InferType()(mod)
mutated_mod['func_6320'] = func_6320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6320_call = mutated_mod.get_global_var('func_6320')
call_6321 = func_6320_call()
output = call_6321
func_6322 = relay.Function([], output)
mutated_mod['func_6322'] = func_6322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4328_call = mod.get_global_var('func_4328')
func_4330_call = mutated_mod.get_global_var('func_4330')
call_6326 = relay.TupleGetItem(func_4328_call(), 1)
call_6327 = relay.TupleGetItem(func_4330_call(), 1)
output = call_6326
output2 = call_6327
func_6328 = relay.Function([], output)
mod['func_6328'] = func_6328
mod = relay.transform.InferType()(mod)
mutated_mod['func_6328'] = func_6328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6328_call = mutated_mod.get_global_var('func_6328')
call_6329 = func_6328_call()
output = call_6329
func_6330 = relay.Function([], output)
mutated_mod['func_6330'] = func_6330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3963_call = mod.get_global_var('func_3963')
func_3964_call = mutated_mod.get_global_var('func_3964')
call_6355 = func_3963_call()
call_6356 = func_3963_call()
func_3963_call = mod.get_global_var('func_3963')
func_3964_call = mutated_mod.get_global_var('func_3964')
call_6359 = func_3963_call()
call_6360 = func_3963_call()
output = relay.Tuple([call_6355,call_6359,])
output2 = relay.Tuple([call_6356,call_6360,])
func_6361 = relay.Function([], output)
mod['func_6361'] = func_6361
mod = relay.transform.InferType()(mod)
output = func_6361()
func_6362 = relay.Function([], output)
mutated_mod['func_6362'] = func_6362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_793_call = mod.get_global_var('func_793')
func_794_call = mutated_mod.get_global_var('func_794')
call_6381 = relay.TupleGetItem(func_793_call(), 0)
call_6382 = relay.TupleGetItem(func_794_call(), 0)
output = call_6381
output2 = call_6382
func_6392 = relay.Function([], output)
mod['func_6392'] = func_6392
mod = relay.transform.InferType()(mod)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6392_call = mutated_mod.get_global_var('func_6392')
call_6393 = func_6392_call()
output = call_6393
func_6394 = relay.Function([], output)
mutated_mod['func_6394'] = func_6394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_891_call = mod.get_global_var('func_891')
func_892_call = mutated_mod.get_global_var('func_892')
call_6446 = func_891_call()
call_6447 = func_891_call()
output = relay.Tuple([call_6446,])
output2 = relay.Tuple([call_6447,])
func_6468 = relay.Function([], output)
mod['func_6468'] = func_6468
mod = relay.transform.InferType()(mod)
mutated_mod['func_6468'] = func_6468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6468_call = mutated_mod.get_global_var('func_6468')
call_6469 = func_6468_call()
output = call_6469
func_6470 = relay.Function([], output)
mutated_mod['func_6470'] = func_6470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2465_call = mod.get_global_var('func_2465')
func_2466_call = mutated_mod.get_global_var('func_2466')
call_6519 = func_2465_call()
call_6520 = func_2465_call()
uop_6555 = relay.cos(call_6519.astype('float64')) # shape=(315,)
uop_6557 = relay.cos(call_6520.astype('float64')) # shape=(315,)
output = relay.Tuple([uop_6555,])
output2 = relay.Tuple([uop_6557,])
func_6563 = relay.Function([], output)
mod['func_6563'] = func_6563
mod = relay.transform.InferType()(mod)
output = func_6563()
func_6564 = relay.Function([], output)
mutated_mod['func_6564'] = func_6564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6320_call = mod.get_global_var('func_6320')
func_6322_call = mutated_mod.get_global_var('func_6322')
call_6575 = relay.TupleGetItem(func_6320_call(), 3)
call_6576 = relay.TupleGetItem(func_6322_call(), 3)
func_6090_call = mod.get_global_var('func_6090')
func_6093_call = mutated_mod.get_global_var('func_6093')
var_6582 = relay.var("var_6582", dtype = "float32", shape = (315,))#candidate|6582|(315,)|var|float32
call_6581 = func_6090_call(relay.reshape(var_6582.astype('float32'), [315,]))
call_6583 = func_6090_call(relay.reshape(var_6582.astype('float32'), [315,]))
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_6593 = func_927_call()
call_6594 = func_927_call()
bop_6598 = relay.bitwise_or(call_6581.astype('int32'), relay.reshape(var_6582.astype('int32'), relay.shape_of(call_6581))) # shape=(315,)
bop_6601 = relay.bitwise_or(call_6583.astype('int32'), relay.reshape(var_6582.astype('int32'), relay.shape_of(call_6583))) # shape=(315,)
func_3117_call = mod.get_global_var('func_3117')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_6614 = func_3117_call()
call_6615 = func_3117_call()
uop_6629 = relay.tan(call_6581.astype('float64')) # shape=(315,)
uop_6631 = relay.tan(call_6583.astype('float64')) # shape=(315,)
func_1719_call = mod.get_global_var('func_1719')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_6642 = relay.TupleGetItem(func_1719_call(), 3)
call_6643 = relay.TupleGetItem(func_1721_call(), 3)
func_1835_call = mod.get_global_var('func_1835')
func_1836_call = mutated_mod.get_global_var('func_1836')
call_6652 = relay.TupleGetItem(func_1835_call(), 0)
call_6653 = relay.TupleGetItem(func_1836_call(), 0)
bop_6655 = relay.power(uop_6629.astype('float32'), relay.reshape(bop_6598.astype('float32'), relay.shape_of(uop_6629))) # shape=(315,)
bop_6658 = relay.power(uop_6631.astype('float32'), relay.reshape(bop_6601.astype('float32'), relay.shape_of(uop_6631))) # shape=(315,)
func_2494_call = mod.get_global_var('func_2494')
func_2496_call = mutated_mod.get_global_var('func_2496')
var_6667 = relay.var("var_6667", dtype = "float64", shape = (240,))#candidate|6667|(240,)|var|float64
call_6666 = func_2494_call(relay.reshape(var_6667.astype('float64'), [5, 16, 3]))
call_6668 = func_2494_call(relay.reshape(var_6667.astype('float64'), [5, 16, 3]))
output = relay.Tuple([call_6575,call_6593,call_6614,call_6642,call_6652,bop_6655,call_6666,var_6667,])
output2 = relay.Tuple([call_6576,call_6594,call_6615,call_6643,call_6653,bop_6658,call_6668,var_6667,])
func_6672 = relay.Function([var_6582,var_6667,], output)
mod['func_6672'] = func_6672
mod = relay.transform.InferType()(mod)
mutated_mod['func_6672'] = func_6672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6672_call = mutated_mod.get_global_var('func_6672')
var_6674 = relay.var("var_6674", dtype = "float32", shape = (315,))#candidate|6674|(315,)|var|float32
var_6675 = relay.var("var_6675", dtype = "float64", shape = (240,))#candidate|6675|(240,)|var|float64
call_6673 = func_6672_call(var_6674,var_6675,)
output = call_6673
func_6676 = relay.Function([var_6674,var_6675,], output)
mutated_mod['func_6676'] = func_6676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_927_call = mod.get_global_var('func_927')
func_929_call = mutated_mod.get_global_var('func_929')
call_6678 = func_927_call()
call_6679 = func_927_call()
output = call_6678
output2 = call_6679
func_6690 = relay.Function([], output)
mod['func_6690'] = func_6690
mod = relay.transform.InferType()(mod)
output = func_6690()
func_6691 = relay.Function([], output)
mutated_mod['func_6691'] = func_6691
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6704 = relay.const([[[8,-1,7,-8,2,-4,7,6,-1,-9],[5,10,10,-1,-1,-2,-10,-8,7,-3],[4,-9,1,10,-6,-2,8,8,-4,-2],[3,-1,-5,8,-7,-2,-8,3,8,1],[4,-6,-5,-2,-3,-1,-8,-9,-5,6],[10,4,1,-9,-3,-3,-4,-1,3,-8],[-8,7,5,-9,-5,-2,-5,4,8,-4],[-4,7,-8,-8,2,1,7,3,4,-2],[-7,5,-3,-9,-4,1,4,5,8,4],[9,9,-5,-8,6,-9,6,-6,-5,-1],[10,7,2,7,-5,-4,-8,10,7,2],[10,10,-7,5,3,-1,8,8,-9,-3],[-6,9,-2,-7,9,-4,-1,4,-3,10],[-5,-1,-8,-6,-4,1,8,3,-1,10]],[[-10,-10,1,8,3,9,8,4,9,-3],[2,4,-4,-1,7,-6,8,-7,9,4],[-3,3,-3,7,8,-6,2,10,8,4],[3,-4,7,3,-9,10,-9,3,-10,5],[-10,6,-4,-1,-8,-10,4,-3,5,7],[-10,-6,-9,-3,1,5,-3,-5,-7,-9],[-1,5,3,4,-3,-4,7,-4,-10,5],[6,-7,3,8,-8,7,6,-5,-10,-8],[10,-8,3,3,-8,7,8,-5,-5,3],[9,-5,3,-5,8,8,7,-5,5,-6],[-6,-6,-8,-7,1,-8,-3,-5,-4,-9],[-6,-2,-10,-3,-7,-7,1,-9,-4,2],[10,8,-5,-8,-5,-5,4,2,-6,-1],[2,-8,-1,2,5,5,-3,9,-5,-1]],[[3,-1,-3,3,8,4,9,-4,9,10],[-7,-9,7,10,-4,2,5,6,-6,1],[10,5,7,4,5,-2,-8,-5,-1,-6],[-4,-4,-4,10,7,6,-7,9,-2,2],[4,10,-6,-8,7,-2,4,1,6,10],[3,3,8,-3,-2,8,8,-1,-10,-3],[-2,-10,-3,-6,4,-2,-5,8,6,4],[6,-5,9,-1,4,-7,-9,5,-10,10],[-1,5,-9,9,-2,-5,-4,-5,8,-1],[-7,9,5,-7,6,-3,10,-3,8,-4],[7,-1,2,6,-9,10,-5,-4,-4,-9],[8,7,7,9,-4,-6,-4,3,-2,-4],[6,-8,5,-3,-3,-9,-2,1,6,7],[-2,-2,1,-2,2,5,-10,-9,5,1]],[[-4,-10,-7,-8,-10,-5,-9,1,-10,-2],[-7,-10,-9,1,1,-3,4,-3,-6,-4],[-7,9,5,3,-2,-10,1,-5,9,4],[10,6,1,-5,-2,3,9,3,-1,1],[-3,-2,1,3,-7,-3,-4,-1,10,-4],[-4,-10,-1,6,1,-7,10,-7,9,4],[-8,-3,6,1,-1,-8,4,-7,-1,6],[4,-6,-5,5,4,-1,6,7,9,8],[3,-4,-2,-1,-6,6,-4,-4,7,2],[1,-4,-9,-7,-10,-8,-10,1,5,-8],[-3,-3,-9,4,8,-7,-1,-6,-5,1],[-9,-8,3,-3,-3,3,5,1,-3,-2],[-2,2,2,-6,-10,-2,-9,-7,2,-3],[1,1,2,-2,8,7,-2,5,-6,3]],[[-1,-6,9,-3,5,8,-3,-4,2,1],[-9,-1,-9,7,9,-3,6,1,5,6],[1,8,4,9,9,9,-10,8,-9,7],[4,-8,-9,4,4,-6,6,1,9,10],[-1,5,-9,1,6,6,7,-10,5,-4],[6,6,-5,3,-8,-1,4,-2,-9,-1],[-2,4,-2,-8,8,8,2,-7,-2,3],[5,-2,-10,-2,-9,5,-9,-3,-3,10],[2,7,-1,-5,7,6,3,-1,-10,3],[5,3,7,4,6,5,-1,6,-9,6],[8,-5,8,6,-8,-9,7,6,-7,-5],[-6,3,-3,9,7,-5,9,-5,-6,9],[10,-7,-10,-10,-5,10,-3,7,9,7],[5,-2,-4,3,10,5,10,6,7,8]]], dtype = "uint64")#candidate|6704|(5, 14, 10)|const|uint64
var_6705 = relay.var("var_6705", dtype = "uint64", shape = (5, 14, 10))#candidate|6705|(5, 14, 10)|var|uint64
bop_6706 = relay.greater_equal(const_6704.astype('bool'), relay.reshape(var_6705.astype('bool'), relay.shape_of(const_6704))) # shape=(5, 14, 10)
func_4390_call = mod.get_global_var('func_4390')
func_4392_call = mutated_mod.get_global_var('func_4392')
var_6722 = relay.var("var_6722", dtype = "float32", shape = (240,))#candidate|6722|(240,)|var|float32
call_6721 = relay.TupleGetItem(func_4390_call(relay.reshape(var_6722.astype('float32'), [5, 16, 3])), 3)
call_6723 = relay.TupleGetItem(func_4392_call(relay.reshape(var_6722.astype('float32'), [5, 16, 3])), 3)
output = relay.Tuple([bop_6706,call_6721,var_6722,])
output2 = relay.Tuple([bop_6706,call_6723,var_6722,])
func_6742 = relay.Function([var_6705,var_6722,], output)
mod['func_6742'] = func_6742
mod = relay.transform.InferType()(mod)
var_6743 = relay.var("var_6743", dtype = "uint64", shape = (5, 14, 10))#candidate|6743|(5, 14, 10)|var|uint64
var_6744 = relay.var("var_6744", dtype = "float32", shape = (240,))#candidate|6744|(240,)|var|float32
output = func_6742(var_6743,var_6744,)
func_6745 = relay.Function([var_6743,var_6744,], output)
mutated_mod['func_6745'] = func_6745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6361_call = mod.get_global_var('func_6361')
func_6362_call = mutated_mod.get_global_var('func_6362')
call_6765 = relay.TupleGetItem(func_6361_call(), 1)
call_6766 = relay.TupleGetItem(func_6362_call(), 1)
func_5046_call = mod.get_global_var('func_5046')
func_5048_call = mutated_mod.get_global_var('func_5048')
call_6793 = relay.TupleGetItem(func_5046_call(), 0)
call_6794 = relay.TupleGetItem(func_5048_call(), 0)
func_1143_call = mod.get_global_var('func_1143')
func_1145_call = mutated_mod.get_global_var('func_1145')
const_6797 = relay.const([True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,True], dtype = "bool")#candidate|6797|(864,)|const|bool
call_6796 = relay.TupleGetItem(func_1143_call(relay.reshape(const_6797.astype('bool'), [6, 16, 9])), 0)
call_6798 = relay.TupleGetItem(func_1145_call(relay.reshape(const_6797.astype('bool'), [6, 16, 9])), 0)
bop_6800 = relay.bitwise_and(const_6797.astype('int8'), relay.reshape(call_6796.astype('int8'), relay.shape_of(const_6797))) # shape=(864,)
bop_6803 = relay.bitwise_and(const_6797.astype('int8'), relay.reshape(call_6798.astype('int8'), relay.shape_of(const_6797))) # shape=(864,)
bop_6821 = relay.equal(call_6796.astype('bool'), relay.reshape(const_6797.astype('bool'), relay.shape_of(call_6796))) # shape=(6, 16, 9)
bop_6824 = relay.equal(call_6798.astype('bool'), relay.reshape(const_6797.astype('bool'), relay.shape_of(call_6798))) # shape=(6, 16, 9)
output = relay.Tuple([call_6765,call_6793,bop_6800,bop_6821,])
output2 = relay.Tuple([call_6766,call_6794,bop_6803,bop_6824,])
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
