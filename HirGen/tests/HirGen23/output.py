import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_40 = relay.var("var_40", dtype = "float32", shape = (13, 1))#candidate|40|(13, 1)|var|float32
uop_41 = relay.asinh(var_40.astype('float32')) # shape=(13, 1)
output = relay.Tuple([uop_41,])
output2 = relay.Tuple([uop_41,])
func_68 = relay.Function([var_40,], output)
mod['func_68'] = func_68
mod = relay.transform.InferType()(mod)
mutated_mod['func_68'] = func_68
mutated_mod = relay.transform.InferType()(mutated_mod)
var_69 = relay.var("var_69", dtype = "float32", shape = (13, 1))#candidate|69|(13, 1)|var|float32
func_68_call = mutated_mod.get_global_var('func_68')
call_70 = func_68_call(var_69)
output = call_70
func_71 = relay.Function([var_69], output)
mutated_mod['func_71'] = func_71
mutated_mod = relay.transform.InferType()(mutated_mod)
var_346 = relay.var("var_346", dtype = "uint16", shape = ())#candidate|346|()|var|uint16
var_347 = relay.var("var_347", dtype = "uint16", shape = (6, 12, 1))#candidate|347|(6, 12, 1)|var|uint16
bop_348 = relay.right_shift(var_346.astype('uint16'), var_347.astype('uint16')) # shape=(6, 12, 1)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
var_353 = relay.var("var_353", dtype = "float32", shape = (13,))#candidate|353|(13,)|var|float32
call_352 = relay.TupleGetItem(func_68_call(relay.reshape(var_353.astype('float32'), [13, 1])), 0)
call_354 = relay.TupleGetItem(func_71_call(relay.reshape(var_353.astype('float32'), [13, 1])), 0)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
call_362 = relay.TupleGetItem(func_68_call(relay.reshape(call_352.astype('float32'), [13, 1])), 0)
call_363 = relay.TupleGetItem(func_71_call(relay.reshape(call_352.astype('float32'), [13, 1])), 0)
output = relay.Tuple([bop_348,call_352,var_353,call_362,])
output2 = relay.Tuple([bop_348,call_354,var_353,call_363,])
func_375 = relay.Function([var_346,var_347,var_353,], output)
mod['func_375'] = func_375
mod = relay.transform.InferType()(mod)
var_376 = relay.var("var_376", dtype = "uint16", shape = ())#candidate|376|()|var|uint16
var_377 = relay.var("var_377", dtype = "uint16", shape = (6, 12, 1))#candidate|377|(6, 12, 1)|var|uint16
var_378 = relay.var("var_378", dtype = "float32", shape = (13,))#candidate|378|(13,)|var|float32
output = func_375(var_376,var_377,var_378,)
func_379 = relay.Function([var_376,var_377,var_378,], output)
mutated_mod['func_379'] = func_379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_438 = relay.var("var_438", dtype = "uint16", shape = ())#candidate|438|()|var|uint16
var_439 = relay.var("var_439", dtype = "uint16", shape = (9, 13, 6))#candidate|439|(9, 13, 6)|var|uint16
bop_440 = relay.less_equal(var_438.astype('bool'), var_439.astype('bool')) # shape=(9, 13, 6)
output = relay.Tuple([bop_440,])
output2 = relay.Tuple([bop_440,])
func_452 = relay.Function([var_438,var_439,], output)
mod['func_452'] = func_452
mod = relay.transform.InferType()(mod)
var_453 = relay.var("var_453", dtype = "uint16", shape = ())#candidate|453|()|var|uint16
var_454 = relay.var("var_454", dtype = "uint16", shape = (9, 13, 6))#candidate|454|(9, 13, 6)|var|uint16
output = func_452(var_453,var_454,)
func_455 = relay.Function([var_453,var_454,], output)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_513 = relay.var("var_513", dtype = "bool", shape = (11, 2, 4))#candidate|513|(11, 2, 4)|var|bool
var_514 = relay.var("var_514", dtype = "bool", shape = (11, 2, 4))#candidate|514|(11, 2, 4)|var|bool
bop_515 = relay.logical_and(var_513.astype('bool'), relay.reshape(var_514.astype('bool'), relay.shape_of(var_513))) # shape=(11, 2, 4)
func_375_call = mod.get_global_var('func_375')
func_379_call = mutated_mod.get_global_var('func_379')
var_521 = relay.var("var_521", dtype = "uint16", shape = ())#candidate|521|()|var|uint16
const_522 = relay.const([-7,2,5,-2,1,-5,4,2,-9,7,-6,-2,10,-4,-6,-2,1,4,7,-8,-1,-5,-7,5,1,-9,2,8,9,-10,1,6,6,-8,6,-3,9,2,-9,9,-10,9,-10,-4,8,-1,-8,1,-7,-6,4,-1,-1,8,3,-10,-8,5,-5,-4,-2,4,-2,-3,5,-5,3,4,9,4,9,-5], dtype = "uint16")#candidate|522|(72,)|const|uint16
var_523 = relay.var("var_523", dtype = "float32", shape = (13,))#candidate|523|(13,)|var|float32
call_520 = relay.TupleGetItem(func_375_call(relay.reshape(var_521.astype('uint16'), []), relay.reshape(const_522.astype('uint16'), [6, 12, 1]), relay.reshape(var_523.astype('float32'), [13,]), ), 2)
call_524 = relay.TupleGetItem(func_379_call(relay.reshape(var_521.astype('uint16'), []), relay.reshape(const_522.astype('uint16'), [6, 12, 1]), relay.reshape(var_523.astype('float32'), [13,]), ), 2)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
call_528 = relay.TupleGetItem(func_68_call(relay.reshape(var_523.astype('float32'), [13, 1])), 0)
call_529 = relay.TupleGetItem(func_71_call(relay.reshape(var_523.astype('float32'), [13, 1])), 0)
output = relay.Tuple([bop_515,call_520,var_521,const_522,var_523,call_528,])
output2 = relay.Tuple([bop_515,call_524,var_521,const_522,var_523,call_529,])
func_530 = relay.Function([var_513,var_514,var_521,var_523,], output)
mod['func_530'] = func_530
mod = relay.transform.InferType()(mod)
var_531 = relay.var("var_531", dtype = "bool", shape = (11, 2, 4))#candidate|531|(11, 2, 4)|var|bool
var_532 = relay.var("var_532", dtype = "bool", shape = (11, 2, 4))#candidate|532|(11, 2, 4)|var|bool
var_533 = relay.var("var_533", dtype = "uint16", shape = ())#candidate|533|()|var|uint16
var_534 = relay.var("var_534", dtype = "float32", shape = (13,))#candidate|534|(13,)|var|float32
output = func_530(var_531,var_532,var_533,var_534,)
func_535 = relay.Function([var_531,var_532,var_533,var_534,], output)
mutated_mod['func_535'] = func_535
mutated_mod = relay.transform.InferType()(mutated_mod)
const_590 = relay.const([[[-6,-7,-9,10,1,10,5,7,5,6,6]],[[-6,8,1,-6,7,7,6,10,10,7,-1]],[[3,6,4,6,2,4,-1,-1,1,10,10]],[[4,10,-1,-3,-1,2,8,1,-7,-3,-4]],[[-4,-3,3,-3,-9,-4,10,-8,-8,1,8]],[[8,-1,-4,-6,1,3,4,-7,-10,-5,-7]]], dtype = "int32")#candidate|590|(6, 1, 11)|const|int32
var_591 = relay.var("var_591", dtype = "int32", shape = (6, 8, 11))#candidate|591|(6, 8, 11)|var|int32
bop_592 = relay.less(const_590.astype('bool'), var_591.astype('bool')) # shape=(6, 8, 11)
bop_598 = relay.logical_and(const_590.astype('bool'), bop_592.astype('bool')) # shape=(6, 8, 11)
output = bop_598
output2 = bop_598
func_606 = relay.Function([var_591,], output)
mod['func_606'] = func_606
mod = relay.transform.InferType()(mod)
var_607 = relay.var("var_607", dtype = "int32", shape = (6, 8, 11))#candidate|607|(6, 8, 11)|var|int32
output = func_606(var_607)
func_608 = relay.Function([var_607], output)
mutated_mod['func_608'] = func_608
mutated_mod = relay.transform.InferType()(mutated_mod)
const_651 = relay.const([[[7.218944,-1.278538,-4.107961,9.136047,-8.468702,-0.502384,-8.063311,7.439414,3.830446],[-7.709280,0.762959,4.412255,9.657622,-8.449449,7.972075,-9.985351,2.187021,-3.290089],[2.762913,-4.401156,1.402186,-3.095322,9.834092,3.656603,-7.879789,-5.369532,-0.678275]],[[-5.442969,-7.820485,-1.935390,-0.859635,7.032740,0.342783,9.620452,6.677112,9.851056],[7.391687,-3.125108,9.138291,2.956431,8.687242,3.744884,7.533412,-9.851012,-2.434924],[4.832814,3.600613,8.804741,-4.768504,3.483244,-0.324760,-3.667777,-1.734575,-7.509048]],[[7.379116,9.396390,1.532396,-0.350172,-2.725209,0.897278,-2.475279,6.681808,7.547916],[-9.047533,-5.967716,3.719144,-9.569704,-7.642286,-0.112680,7.357980,-3.070359,1.020538],[3.158852,4.437576,-5.351165,7.986664,3.181193,-7.238366,4.926340,8.784461,-4.013965]],[[-7.889237,-3.671522,-1.147353,1.875800,-3.556406,-5.592753,8.907541,-6.665079,-0.511508],[7.636556,2.799739,-4.837875,4.949118,-1.593813,5.759661,2.832623,-4.060094,-8.062681],[3.188576,-3.277381,-0.717913,6.847538,-4.030103,-1.089364,-2.805390,-2.828898,-9.355044]],[[7.966304,-5.619231,-8.773831,-2.162989,0.323769,-2.888964,3.912578,2.180168,9.031873],[4.781188,-6.236846,-1.018072,-0.581248,-0.713243,-9.960812,3.921322,4.808979,-8.831186],[-0.546039,3.438936,2.552495,0.892144,3.152774,-8.481846,-1.054893,8.442765,3.015999]],[[6.693437,-6.229293,3.046111,9.386033,-1.218389,-9.928252,-8.171644,-3.541976,8.337053],[4.311181,-0.696905,3.342991,-5.496305,-5.204130,-3.427285,2.590681,3.104095,-6.501733],[9.647689,-1.921534,-7.312605,-0.853964,1.674497,-0.738688,-7.078555,0.456369,1.096201]],[[1.996013,6.563944,3.580544,6.769909,1.314075,4.624684,9.956706,6.711966,-0.635222],[3.535108,0.438695,8.316469,9.457894,8.054361,1.194553,4.711941,-4.378477,-7.378861],[3.289199,6.943530,5.864999,-3.360406,8.006810,-3.088084,2.412117,-2.717346,-4.323919]],[[-1.430265,2.611920,-5.448547,-5.477695,3.547656,-9.566341,9.269866,7.962634,2.694087],[0.339807,-1.332591,0.855125,-9.633563,-6.233834,9.482720,3.143032,-6.004097,-8.307907],[1.199068,-1.176057,0.345608,-5.454082,-5.470937,4.024402,-4.936646,7.765889,0.726650]],[[0.851295,5.451335,-4.031518,-4.646374,0.993013,-4.246387,-8.402978,-0.395330,-1.248457],[2.923335,-5.391591,1.015248,4.613434,-9.019547,-7.102364,-5.268998,-0.834982,7.883955],[-1.740233,-0.330423,-8.193913,2.578325,-4.300752,8.990599,-0.088541,4.374887,9.703086]],[[-3.584767,2.792630,9.811945,6.765347,6.817517,-8.452957,-3.975131,3.155609,-4.856351],[-1.811049,-6.806659,2.321880,2.644344,-6.854220,1.007225,4.892486,0.985468,-1.397385],[-1.003260,-5.382418,1.236290,-9.207910,1.795946,-0.713506,3.284416,-7.379389,2.257484]],[[-3.824047,9.046293,-7.101251,-8.008794,-9.583092,-7.102911,-4.818668,-0.557077,-0.610537],[3.111126,-7.295427,-6.604696,-3.153871,3.230779,7.083686,9.561607,2.348851,1.846939],[0.637775,-3.739075,8.134950,-6.629876,1.824144,-8.332163,1.372696,3.690462,-2.750434]],[[-6.747861,7.892534,8.586042,9.019042,-3.284412,2.089788,-8.248370,3.960987,1.702519],[3.130255,3.693071,-9.718069,-6.328485,7.155451,3.098677,-6.922681,9.362447,8.817003],[-4.113748,3.677575,-4.797973,-7.140701,3.469381,7.494766,-2.702252,-6.162845,5.797309]],[[7.169093,-2.377554,1.021107,1.430952,-4.762052,-8.111808,0.022842,-9.377789,8.922970],[-0.737847,2.126084,-4.646446,-3.303956,5.541815,-9.937748,7.208458,-2.648930,-6.874966],[-1.512712,0.455920,-4.737506,-7.023774,3.070891,-6.609815,5.147789,-8.630083,-5.256578]],[[8.481450,-0.542171,-5.313115,-4.166067,-2.660296,3.383431,-7.117869,-2.938939,-5.552970],[2.340672,5.965483,2.745198,-1.984989,-3.811219,7.234470,9.112658,1.764262,5.705138],[-6.615820,7.654424,2.394061,1.256753,-1.163060,7.277030,0.118263,-1.450743,6.646157]],[[-9.293398,-8.097360,8.924563,-5.352776,3.198780,-8.007380,3.302794,-4.763480,0.376772],[4.049379,1.551510,2.946741,3.189650,-6.012861,1.492590,5.593560,7.922107,-5.092652],[-5.482572,6.534155,-2.310210,-1.877296,-7.418305,-1.811478,-7.892718,-6.995097,-8.670661]]], dtype = "float32")#candidate|651|(15, 3, 9)|const|float32
uop_652 = relay.tan(const_651.astype('float32')) # shape=(15, 3, 9)
uop_662 = relay.sinh(const_651.astype('float32')) # shape=(15, 3, 9)
bop_677 = relay.add(const_651.astype('uint16'), relay.reshape(uop_652.astype('uint16'), relay.shape_of(const_651))) # shape=(15, 3, 9)
output = relay.Tuple([uop_662,bop_677,])
output2 = relay.Tuple([uop_662,bop_677,])
func_680 = relay.Function([], output)
mod['func_680'] = func_680
mod = relay.transform.InferType()(mod)
mutated_mod['func_680'] = func_680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mutated_mod.get_global_var('func_680')
call_681 = func_680_call()
output = call_681
func_682 = relay.Function([], output)
mutated_mod['func_682'] = func_682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_686 = relay.TupleGetItem(func_680_call(), 0)
call_687 = relay.TupleGetItem(func_682_call(), 0)
var_693 = relay.var("var_693", dtype = "float32", shape = (15, 3, 9))#candidate|693|(15, 3, 9)|var|float32
bop_694 = relay.subtract(call_686.astype('int16'), relay.reshape(var_693.astype('int16'), relay.shape_of(call_686))) # shape=(15, 3, 9)
bop_697 = relay.subtract(call_687.astype('int16'), relay.reshape(var_693.astype('int16'), relay.shape_of(call_687))) # shape=(15, 3, 9)
uop_710 = relay.asinh(bop_694.astype('float32')) # shape=(15, 3, 9)
uop_712 = relay.asinh(bop_697.astype('float32')) # shape=(15, 3, 9)
func_530_call = mod.get_global_var('func_530')
func_535_call = mutated_mod.get_global_var('func_535')
const_715 = relay.const([False,False,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True], dtype = "bool")#candidate|715|(88,)|const|bool
const_716 = relay.const(-7, dtype = "uint16")#candidate|716|()|const|uint16
const_717 = relay.const([2.937310,3.778946,-8.174619,6.105008,9.103834,2.116420,3.972095,-7.809539,1.711950,2.054868,-0.757411,1.448730,6.091348], dtype = "float32")#candidate|717|(13,)|const|float32
call_714 = relay.TupleGetItem(func_530_call(relay.reshape(const_715.astype('bool'), [11, 2, 4]), relay.reshape(const_715.astype('bool'), [11, 2, 4]), relay.reshape(const_716.astype('uint16'), []), relay.reshape(const_717.astype('float32'), [13,]), ), 2)
call_718 = relay.TupleGetItem(func_535_call(relay.reshape(const_715.astype('bool'), [11, 2, 4]), relay.reshape(const_715.astype('bool'), [11, 2, 4]), relay.reshape(const_716.astype('uint16'), []), relay.reshape(const_717.astype('float32'), [13,]), ), 2)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_732 = relay.TupleGetItem(func_680_call(), 1)
call_733 = relay.TupleGetItem(func_682_call(), 1)
output = relay.Tuple([uop_710,call_714,const_715,const_716,const_717,call_732,])
output2 = relay.Tuple([uop_712,call_718,const_715,const_716,const_717,call_733,])
func_743 = relay.Function([var_693,], output)
mod['func_743'] = func_743
mod = relay.transform.InferType()(mod)
mutated_mod['func_743'] = func_743
mutated_mod = relay.transform.InferType()(mutated_mod)
var_744 = relay.var("var_744", dtype = "float32", shape = (15, 3, 9))#candidate|744|(15, 3, 9)|var|float32
func_743_call = mutated_mod.get_global_var('func_743')
call_745 = func_743_call(var_744)
output = call_745
func_746 = relay.Function([var_744], output)
mutated_mod['func_746'] = func_746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_791 = relay.TupleGetItem(func_680_call(), 1)
call_792 = relay.TupleGetItem(func_682_call(), 1)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
const_798 = relay.const([-5,7,2,8,10,5,10,-6,-6,3,-4,5,-7,5,4,-1,10,7,-7,5,5,-5,10,7,10,1,1,8,-4,5,4,8,-5,7,-2,-1,-10,3,6,7,10,-2,5,-10,-4,8,-2,-3,3,-10,10,-3,6,10,4,1,-9,-4,2,3,8,3,10,-6,6,10,-7,-6,-7,-6,8,-6,10,-9,-5,-6,4,2,7,-8,5,-1,-9,7,5,-10,1,-10,-9,3,3,-6,1,10,-7,3,6,-4,10,2,5,10,1,6,3,3,-9,3,-6,-9,1,3,-5,2,-10,-5,-10,10,-9,9,-8,-7,1,10,-3,8,-3,1,10,5,2,5,-7,3,-5,-5,5,1,-2,-3,10,-8,2,10,5,-4,-7,8,5,-7,4,-3,-6,4,7,-10,9,-9,7,7,-9,10,-9,10,-10,4,1,-2,4,-2,5,8,-9,-9,10,-10,-6,-5,-9,-8,-1,2,2,6,1,-4,1,-4,-9,-9,-8,8,-7,10,-7,4,3,-10,9,-8,6,-9,-4,-7,4,3,-5,8,3,8,8,-6,8,-5,-3,-5,5,-6,-7,-5,1,4,9,7,-2,10,9,-1,3,1,-9,7,-2,-6,-7,9,6,-1,-7,-7,-3,9,6,-8,5,6,-8,9,-5,-9,5,8,3,-6,-10,-9,1,-5,-7,-5,2,8,2,10,-4,10,8,1,-7,-10,-10,-10,-7,6,-9,8,-2,-3,-6,4,3,9,9,-3,-7,-5,-1,5,-1,-4,4,4,-6,10,2,-2,-7,-8,-1,5,3,-2,-7,4,2,10,8,1,3,-8,7,-9,2,-1,8,10,5,8,1,-10,10,8,-4,-5,-10,1,2,-2,-9,7,8,-1,-1,5,-2,6,4,3,-3,-6,-9,10,9,10,-4,7,6,5,6,-9,4,2,9,8,2,-7,-1,6,9,-7,-5,-5,2,-6,9,-1,-3,2,8,4,-4,-5,-7,2,-9,1,5,2,-7,8,-6,-10,1,10,2,1,6,8,9,1,2,1,-9,5,-3,-1,-3,7,1,-3,-3,8,10,-5,7,-6,-8,-6,-10,-1,5,2,-1,2,-8,6,1,3,9,2,-3,-6,-5,-8,-5,-8,2,-8,8,-6,7,10,-5,1,2,-1,2,-8,10,-2,8,5,9,-3,-7,5,-3,4,-9,-4,-8,8,4,7,-5,-9,2,-2,-9,-9,-6,-2,1,-10,9,-3,-1,-7,10,-7,6,7,1,-8,-4,9,-3,-10,-5,7,4,-10,-5,-8,-2,10,-2,-7,-6,-5,4,-10,-3,3,9,-1,-2,-6,10,3,-10,4,-2,6,6,8,-5,6,9,5,9,-10,9,-9,-1,-2,7,-6,-7,-9,-4,-10,5,7,5,-1,8,-9], dtype = "int32")#candidate|798|(528,)|const|int32
call_797 = func_606_call(relay.reshape(const_798.astype('int32'), [6, 8, 11]))
call_799 = func_606_call(relay.reshape(const_798.astype('int32'), [6, 8, 11]))
output = relay.Tuple([call_791,call_797,const_798,])
output2 = relay.Tuple([call_792,call_799,const_798,])
func_813 = relay.Function([], output)
mod['func_813'] = func_813
mod = relay.transform.InferType()(mod)
mutated_mod['func_813'] = func_813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mutated_mod.get_global_var('func_813')
call_814 = func_813_call()
output = call_814
func_815 = relay.Function([], output)
mutated_mod['func_815'] = func_815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_936 = relay.TupleGetItem(func_813_call(), 2)
call_937 = relay.TupleGetItem(func_815_call(), 2)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
var_941 = relay.var("var_941", dtype = "float32", shape = (13,))#candidate|941|(13,)|var|float32
call_940 = relay.TupleGetItem(func_68_call(relay.reshape(var_941.astype('float32'), [13, 1])), 0)
call_942 = relay.TupleGetItem(func_71_call(relay.reshape(var_941.astype('float32'), [13, 1])), 0)
output = relay.Tuple([call_936,call_940,var_941,])
output2 = relay.Tuple([call_937,call_942,var_941,])
func_946 = relay.Function([var_941,], output)
mod['func_946'] = func_946
mod = relay.transform.InferType()(mod)
var_947 = relay.var("var_947", dtype = "float32", shape = (13,))#candidate|947|(13,)|var|float32
output = func_946(var_947)
func_948 = relay.Function([var_947], output)
mutated_mod['func_948'] = func_948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_968 = relay.TupleGetItem(func_813_call(), 1)
call_969 = relay.TupleGetItem(func_815_call(), 1)
uop_977 = relay.exp(call_968.astype('float64')) # shape=(6, 8, 11)
uop_979 = relay.exp(call_969.astype('float64')) # shape=(6, 8, 11)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_982 = func_606_call(relay.reshape(call_968.astype('int32'), [6, 8, 11]))
call_983 = func_606_call(relay.reshape(call_968.astype('int32'), [6, 8, 11]))
output = relay.Tuple([uop_977,call_982,])
output2 = relay.Tuple([uop_979,call_983,])
func_988 = relay.Function([], output)
mod['func_988'] = func_988
mod = relay.transform.InferType()(mod)
mutated_mod['func_988'] = func_988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mutated_mod.get_global_var('func_988')
call_989 = func_988_call()
output = call_989
func_990 = relay.Function([], output)
mutated_mod['func_990'] = func_990
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1011 = relay.const([[[4],[5],[-9],[4],[-8],[1],[7],[8]],[[-3],[10],[10],[10],[6],[-2],[-5],[-7]],[[3],[10],[4],[4],[-5],[5],[8],[-9]]], dtype = "uint8")#candidate|1011|(3, 8, 1)|const|uint8
var_1012 = relay.var("var_1012", dtype = "uint8", shape = (3, 8, 4))#candidate|1012|(3, 8, 4)|var|uint8
bop_1013 = relay.greater_equal(const_1011.astype('bool'), var_1012.astype('bool')) # shape=(3, 8, 4)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
const_1025 = relay.const([-7.261389,-1.759781,6.820184,-1.505545,8.165793,3.956470,2.560744,8.208313,-1.862063,0.255911,6.157475,5.637434,3.525159], dtype = "float32")#candidate|1025|(13,)|const|float32
call_1024 = relay.TupleGetItem(func_68_call(relay.reshape(const_1025.astype('float32'), [13, 1])), 0)
call_1026 = relay.TupleGetItem(func_71_call(relay.reshape(const_1025.astype('float32'), [13, 1])), 0)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_1032 = relay.TupleGetItem(func_988_call(), 1)
call_1033 = relay.TupleGetItem(func_990_call(), 1)
output = relay.Tuple([bop_1013,call_1024,const_1025,call_1032,])
output2 = relay.Tuple([bop_1013,call_1026,const_1025,call_1033,])
func_1042 = relay.Function([var_1012,], output)
mod['func_1042'] = func_1042
mod = relay.transform.InferType()(mod)
mutated_mod['func_1042'] = func_1042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1043 = relay.var("var_1043", dtype = "uint8", shape = (3, 8, 4))#candidate|1043|(3, 8, 4)|var|uint8
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1044 = func_1042_call(var_1043)
output = call_1044
func_1045 = relay.Function([var_1043], output)
mutated_mod['func_1045'] = func_1045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_1061 = relay.TupleGetItem(func_680_call(), 0)
call_1062 = relay.TupleGetItem(func_682_call(), 0)
var_1068 = relay.var("var_1068", dtype = "float32", shape = (15, 3, 9))#candidate|1068|(15, 3, 9)|var|float32
bop_1069 = relay.not_equal(call_1061.astype('bool'), relay.reshape(var_1068.astype('bool'), relay.shape_of(call_1061))) # shape=(15, 3, 9)
bop_1072 = relay.not_equal(call_1062.astype('bool'), relay.reshape(var_1068.astype('bool'), relay.shape_of(call_1062))) # shape=(15, 3, 9)
uop_1095 = relay.cosh(var_1068.astype('float64')) # shape=(15, 3, 9)
output = relay.Tuple([bop_1069,uop_1095,])
output2 = relay.Tuple([bop_1072,uop_1095,])
func_1097 = relay.Function([var_1068,], output)
mod['func_1097'] = func_1097
mod = relay.transform.InferType()(mod)
var_1098 = relay.var("var_1098", dtype = "float32", shape = (15, 3, 9))#candidate|1098|(15, 3, 9)|var|float32
output = func_1097(var_1098)
func_1099 = relay.Function([var_1098], output)
mutated_mod['func_1099'] = func_1099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_1118 = relay.TupleGetItem(func_988_call(), 0)
call_1119 = relay.TupleGetItem(func_990_call(), 0)
output = relay.Tuple([call_1118,])
output2 = relay.Tuple([call_1119,])
func_1123 = relay.Function([], output)
mod['func_1123'] = func_1123
mod = relay.transform.InferType()(mod)
mutated_mod['func_1123'] = func_1123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1123_call = mutated_mod.get_global_var('func_1123')
call_1124 = func_1123_call()
output = call_1124
func_1125 = relay.Function([], output)
mutated_mod['func_1125'] = func_1125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_1147 = relay.TupleGetItem(func_813_call(), 2)
call_1148 = relay.TupleGetItem(func_815_call(), 2)
func_606_call = mod.get_global_var('func_606')
func_608_call = mutated_mod.get_global_var('func_608')
call_1152 = func_606_call(relay.reshape(call_1147.astype('int32'), [6, 8, 11]))
call_1153 = func_606_call(relay.reshape(call_1147.astype('int32'), [6, 8, 11]))
func_452_call = mod.get_global_var('func_452')
func_455_call = mutated_mod.get_global_var('func_455')
const_1156 = relay.const(7, dtype = "uint16")#candidate|1156|()|const|uint16
var_1157 = relay.var("var_1157", dtype = "uint16", shape = (1, 702))#candidate|1157|(1, 702)|var|uint16
call_1155 = relay.TupleGetItem(func_452_call(relay.reshape(const_1156.astype('uint16'), []), relay.reshape(var_1157.astype('uint16'), [9, 13, 6]), ), 0)
call_1158 = relay.TupleGetItem(func_455_call(relay.reshape(const_1156.astype('uint16'), []), relay.reshape(var_1157.astype('uint16'), [9, 13, 6]), ), 0)
var_1159 = relay.var("var_1159", dtype = "bool", shape = (6, 8, 11))#candidate|1159|(6, 8, 11)|var|bool
bop_1160 = relay.minimum(call_1152.astype('uint16'), relay.reshape(var_1159.astype('uint16'), relay.shape_of(call_1152))) # shape=(6, 8, 11)
bop_1163 = relay.minimum(call_1153.astype('uint16'), relay.reshape(var_1159.astype('uint16'), relay.shape_of(call_1153))) # shape=(6, 8, 11)
bop_1169 = relay.divide(const_1156.astype('float32'), var_1159.astype('float32')) # shape=(6, 8, 11)
func_743_call = mod.get_global_var('func_743')
func_746_call = mutated_mod.get_global_var('func_746')
var_1173 = relay.var("var_1173", dtype = "float32", shape = (405,))#candidate|1173|(405,)|var|float32
call_1172 = relay.TupleGetItem(func_743_call(relay.reshape(var_1173.astype('float32'), [15, 3, 9])), 0)
call_1174 = relay.TupleGetItem(func_746_call(relay.reshape(var_1173.astype('float32'), [15, 3, 9])), 0)
func_1123_call = mod.get_global_var('func_1123')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_1197 = relay.TupleGetItem(func_1123_call(), 0)
call_1198 = relay.TupleGetItem(func_1125_call(), 0)
uop_1199 = relay.acos(call_1172.astype('float32')) # shape=(15, 3, 9)
uop_1201 = relay.acos(call_1174.astype('float32')) # shape=(15, 3, 9)
func_530_call = mod.get_global_var('func_530')
func_535_call = mutated_mod.get_global_var('func_535')
var_1206 = relay.var("var_1206", dtype = "bool", shape = (88,))#candidate|1206|(88,)|var|bool
var_1207 = relay.var("var_1207", dtype = "float32", shape = (13,))#candidate|1207|(13,)|var|float32
call_1205 = relay.TupleGetItem(func_530_call(relay.reshape(var_1206.astype('bool'), [11, 2, 4]), relay.reshape(var_1206.astype('bool'), [11, 2, 4]), relay.reshape(const_1156.astype('uint16'), []), relay.reshape(var_1207.astype('float32'), [13,]), ), 5)
call_1208 = relay.TupleGetItem(func_535_call(relay.reshape(var_1206.astype('bool'), [11, 2, 4]), relay.reshape(var_1206.astype('bool'), [11, 2, 4]), relay.reshape(const_1156.astype('uint16'), []), relay.reshape(var_1207.astype('float32'), [13,]), ), 5)
output = relay.Tuple([call_1147,call_1155,var_1157,bop_1160,bop_1169,var_1173,call_1197,uop_1199,call_1205,var_1206,var_1207,])
output2 = relay.Tuple([call_1148,call_1158,var_1157,bop_1163,bop_1169,var_1173,call_1198,uop_1201,call_1208,var_1206,var_1207,])
func_1218 = relay.Function([var_1157,var_1159,var_1173,var_1206,var_1207,], output)
mod['func_1218'] = func_1218
mod = relay.transform.InferType()(mod)
mutated_mod['func_1218'] = func_1218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1218_call = mutated_mod.get_global_var('func_1218')
var_1220 = relay.var("var_1220", dtype = "uint16", shape = (1, 702))#candidate|1220|(1, 702)|var|uint16
var_1221 = relay.var("var_1221", dtype = "bool", shape = (6, 8, 11))#candidate|1221|(6, 8, 11)|var|bool
var_1222 = relay.var("var_1222", dtype = "float32", shape = (405,))#candidate|1222|(405,)|var|float32
var_1223 = relay.var("var_1223", dtype = "bool", shape = (88,))#candidate|1223|(88,)|var|bool
var_1224 = relay.var("var_1224", dtype = "float32", shape = (13,))#candidate|1224|(13,)|var|float32
call_1219 = func_1218_call(var_1220,var_1221,var_1222,var_1223,var_1224,)
output = call_1219
func_1225 = relay.Function([var_1220,var_1221,var_1222,var_1223,var_1224,], output)
mutated_mod['func_1225'] = func_1225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_1287 = relay.TupleGetItem(func_680_call(), 1)
call_1288 = relay.TupleGetItem(func_682_call(), 1)
output = call_1287
output2 = call_1288
func_1291 = relay.Function([], output)
mod['func_1291'] = func_1291
mod = relay.transform.InferType()(mod)
output = func_1291()
func_1292 = relay.Function([], output)
mutated_mod['func_1292'] = func_1292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_1313 = relay.TupleGetItem(func_680_call(), 0)
call_1314 = relay.TupleGetItem(func_682_call(), 0)
var_1319 = relay.var("var_1319", dtype = "float32", shape = (15, 3, 9))#candidate|1319|(15, 3, 9)|var|float32
bop_1320 = relay.right_shift(call_1313.astype('uint16'), relay.reshape(var_1319.astype('uint16'), relay.shape_of(call_1313))) # shape=(15, 3, 9)
bop_1323 = relay.right_shift(call_1314.astype('uint16'), relay.reshape(var_1319.astype('uint16'), relay.shape_of(call_1314))) # shape=(15, 3, 9)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_1335 = relay.TupleGetItem(func_813_call(), 2)
call_1336 = relay.TupleGetItem(func_815_call(), 2)
output = relay.Tuple([bop_1320,call_1335,])
output2 = relay.Tuple([bop_1323,call_1336,])
func_1337 = relay.Function([var_1319,], output)
mod['func_1337'] = func_1337
mod = relay.transform.InferType()(mod)
mutated_mod['func_1337'] = func_1337
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1338 = relay.var("var_1338", dtype = "float32", shape = (15, 3, 9))#candidate|1338|(15, 3, 9)|var|float32
func_1337_call = mutated_mod.get_global_var('func_1337')
call_1339 = func_1337_call(var_1338)
output = call_1339
func_1340 = relay.Function([var_1338], output)
mutated_mod['func_1340'] = func_1340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1123_call = mod.get_global_var('func_1123')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_1357 = relay.TupleGetItem(func_1123_call(), 0)
call_1358 = relay.TupleGetItem(func_1125_call(), 0)
func_1042_call = mod.get_global_var('func_1042')
func_1045_call = mutated_mod.get_global_var('func_1045')
const_1363 = relay.const([5,-8,-10,7,3,-4,-2,6,-4,-6,5,-2,-1,3,-9,3,-10,8,-3,10,4,7,-2,-2,9,-1,-10,-7,-7,2,-7,-9,-4,-6,6,3,1,8,2,10,-7,-8,-5,7,9,9,2,2,-6,5,6,2,9,-1,-7,6,3,3,3,9,9,8,5,-9,2,-3,-1,6,-4,-3,-9,6,-3,9,9,7,-7,9,-9,-4,-10,9,-1,-3,3,7,3,5,10,-3,3,7,7,3,2,-6], dtype = "uint8")#candidate|1363|(96,)|const|uint8
call_1362 = relay.TupleGetItem(func_1042_call(relay.reshape(const_1363.astype('uint8'), [3, 8, 4])), 3)
call_1364 = relay.TupleGetItem(func_1045_call(relay.reshape(const_1363.astype('uint8'), [3, 8, 4])), 3)
uop_1374 = relay.sin(call_1357.astype('float32')) # shape=(6, 8, 11)
uop_1376 = relay.sin(call_1358.astype('float32')) # shape=(6, 8, 11)
output = relay.Tuple([call_1362,const_1363,uop_1374,])
output2 = relay.Tuple([call_1364,const_1363,uop_1376,])
func_1377 = relay.Function([], output)
mod['func_1377'] = func_1377
mod = relay.transform.InferType()(mod)
mutated_mod['func_1377'] = func_1377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1377_call = mutated_mod.get_global_var('func_1377')
call_1378 = func_1377_call()
output = call_1378
func_1379 = relay.Function([], output)
mutated_mod['func_1379'] = func_1379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_1403 = relay.TupleGetItem(func_813_call(), 1)
call_1404 = relay.TupleGetItem(func_815_call(), 1)
uop_1405 = relay.log(call_1403.astype('float32')) # shape=(6, 8, 11)
uop_1407 = relay.log(call_1404.astype('float32')) # shape=(6, 8, 11)
bop_1409 = relay.not_equal(uop_1405.astype('bool'), relay.reshape(call_1403.astype('bool'), relay.shape_of(uop_1405))) # shape=(6, 8, 11)
bop_1412 = relay.not_equal(uop_1407.astype('bool'), relay.reshape(call_1404.astype('bool'), relay.shape_of(uop_1407))) # shape=(6, 8, 11)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_1416 = relay.TupleGetItem(func_680_call(), 1)
call_1417 = relay.TupleGetItem(func_682_call(), 1)
bop_1426 = relay.floor_mod(uop_1405.astype('float64'), relay.reshape(call_1403.astype('float64'), relay.shape_of(uop_1405))) # shape=(6, 8, 11)
bop_1429 = relay.floor_mod(uop_1407.astype('float64'), relay.reshape(call_1404.astype('float64'), relay.shape_of(uop_1407))) # shape=(6, 8, 11)
uop_1430 = relay.cosh(uop_1405.astype('float32')) # shape=(6, 8, 11)
uop_1432 = relay.cosh(uop_1407.astype('float32')) # shape=(6, 8, 11)
uop_1441 = relay.asinh(uop_1430.astype('float32')) # shape=(6, 8, 11)
uop_1443 = relay.asinh(uop_1432.astype('float32')) # shape=(6, 8, 11)
uop_1445 = relay.log2(uop_1441.astype('float32')) # shape=(6, 8, 11)
uop_1447 = relay.log2(uop_1443.astype('float32')) # shape=(6, 8, 11)
bop_1449 = relay.right_shift(uop_1445.astype('uint8'), relay.reshape(uop_1430.astype('uint8'), relay.shape_of(uop_1445))) # shape=(6, 8, 11)
bop_1452 = relay.right_shift(uop_1447.astype('uint8'), relay.reshape(uop_1432.astype('uint8'), relay.shape_of(uop_1447))) # shape=(6, 8, 11)
output = relay.Tuple([bop_1409,call_1416,bop_1426,bop_1449,])
output2 = relay.Tuple([bop_1412,call_1417,bop_1429,bop_1452,])
func_1459 = relay.Function([], output)
mod['func_1459'] = func_1459
mod = relay.transform.InferType()(mod)
output = func_1459()
func_1460 = relay.Function([], output)
mutated_mod['func_1460'] = func_1460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mod.get_global_var('func_1459')
func_1460_call = mutated_mod.get_global_var('func_1460')
call_1498 = relay.TupleGetItem(func_1459_call(), 2)
call_1499 = relay.TupleGetItem(func_1460_call(), 2)
output = call_1498
output2 = call_1499
func_1502 = relay.Function([], output)
mod['func_1502'] = func_1502
mod = relay.transform.InferType()(mod)
output = func_1502()
func_1503 = relay.Function([], output)
mutated_mod['func_1503'] = func_1503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_1569 = relay.TupleGetItem(func_813_call(), 1)
call_1570 = relay.TupleGetItem(func_815_call(), 1)
output = call_1569
output2 = call_1570
func_1571 = relay.Function([], output)
mod['func_1571'] = func_1571
mod = relay.transform.InferType()(mod)
mutated_mod['func_1571'] = func_1571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mutated_mod.get_global_var('func_1571')
call_1572 = func_1571_call()
output = call_1572
func_1573 = relay.Function([], output)
mutated_mod['func_1573'] = func_1573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1377_call = mod.get_global_var('func_1377')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_1581 = relay.TupleGetItem(func_1377_call(), 1)
call_1582 = relay.TupleGetItem(func_1379_call(), 1)
var_1612 = relay.var("var_1612", dtype = "uint8", shape = (96,))#candidate|1612|(96,)|var|uint8
bop_1613 = relay.floor_divide(call_1581.astype('float32'), relay.reshape(var_1612.astype('float32'), relay.shape_of(call_1581))) # shape=(96,)
bop_1616 = relay.floor_divide(call_1582.astype('float32'), relay.reshape(var_1612.astype('float32'), relay.shape_of(call_1582))) # shape=(96,)
output = relay.Tuple([bop_1613,])
output2 = relay.Tuple([bop_1616,])
func_1632 = relay.Function([var_1612,], output)
mod['func_1632'] = func_1632
mod = relay.transform.InferType()(mod)
mutated_mod['func_1632'] = func_1632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1633 = relay.var("var_1633", dtype = "uint8", shape = (96,))#candidate|1633|(96,)|var|uint8
func_1632_call = mutated_mod.get_global_var('func_1632')
call_1634 = func_1632_call(var_1633)
output = call_1634
func_1635 = relay.Function([var_1633], output)
mutated_mod['func_1635'] = func_1635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_1654 = func_1291_call()
call_1655 = func_1291_call()
output = relay.Tuple([call_1654,])
output2 = relay.Tuple([call_1655,])
func_1666 = relay.Function([], output)
mod['func_1666'] = func_1666
mod = relay.transform.InferType()(mod)
output = func_1666()
func_1667 = relay.Function([], output)
mutated_mod['func_1667'] = func_1667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_1685 = func_1502_call()
call_1686 = func_1502_call()
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_1706 = relay.TupleGetItem(func_988_call(), 1)
call_1707 = relay.TupleGetItem(func_990_call(), 1)
output = relay.Tuple([call_1685,call_1706,])
output2 = relay.Tuple([call_1686,call_1707,])
func_1717 = relay.Function([], output)
mod['func_1717'] = func_1717
mod = relay.transform.InferType()(mod)
output = func_1717()
func_1718 = relay.Function([], output)
mutated_mod['func_1718'] = func_1718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_1722 = relay.TupleGetItem(func_1717_call(), 0)
call_1723 = relay.TupleGetItem(func_1718_call(), 0)
output = relay.Tuple([call_1722,])
output2 = relay.Tuple([call_1723,])
func_1729 = relay.Function([], output)
mod['func_1729'] = func_1729
mod = relay.transform.InferType()(mod)
output = func_1729()
func_1730 = relay.Function([], output)
mutated_mod['func_1730'] = func_1730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_1774 = relay.TupleGetItem(func_1666_call(), 0)
call_1775 = relay.TupleGetItem(func_1667_call(), 0)
func_1042_call = mod.get_global_var('func_1042')
func_1045_call = mutated_mod.get_global_var('func_1045')
var_1785 = relay.var("var_1785", dtype = "uint8", shape = (96,))#candidate|1785|(96,)|var|uint8
call_1784 = relay.TupleGetItem(func_1042_call(relay.reshape(var_1785.astype('uint8'), [3, 8, 4])), 0)
call_1786 = relay.TupleGetItem(func_1045_call(relay.reshape(var_1785.astype('uint8'), [3, 8, 4])), 0)
func_1729_call = mod.get_global_var('func_1729')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_1791 = relay.TupleGetItem(func_1729_call(), 0)
call_1792 = relay.TupleGetItem(func_1730_call(), 0)
output = relay.Tuple([call_1774,call_1784,var_1785,call_1791,])
output2 = relay.Tuple([call_1775,call_1786,var_1785,call_1792,])
func_1796 = relay.Function([var_1785,], output)
mod['func_1796'] = func_1796
mod = relay.transform.InferType()(mod)
var_1797 = relay.var("var_1797", dtype = "uint8", shape = (96,))#candidate|1797|(96,)|var|uint8
output = func_1796(var_1797)
func_1798 = relay.Function([var_1797], output)
mutated_mod['func_1798'] = func_1798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1459_call = mod.get_global_var('func_1459')
func_1460_call = mutated_mod.get_global_var('func_1460')
call_1811 = relay.TupleGetItem(func_1459_call(), 2)
call_1812 = relay.TupleGetItem(func_1460_call(), 2)
var_1815 = relay.var("var_1815", dtype = "float64", shape = (6, 8, 11))#candidate|1815|(6, 8, 11)|var|float64
bop_1816 = relay.logical_or(call_1811.astype('bool'), relay.reshape(var_1815.astype('bool'), relay.shape_of(call_1811))) # shape=(6, 8, 11)
bop_1819 = relay.logical_or(call_1812.astype('bool'), relay.reshape(var_1815.astype('bool'), relay.shape_of(call_1812))) # shape=(6, 8, 11)
func_946_call = mod.get_global_var('func_946')
func_948_call = mutated_mod.get_global_var('func_948')
var_1826 = relay.var("var_1826", dtype = "float32", shape = (1, 13))#candidate|1826|(1, 13)|var|float32
call_1825 = relay.TupleGetItem(func_946_call(relay.reshape(var_1826.astype('float32'), [13,])), 1)
call_1827 = relay.TupleGetItem(func_948_call(relay.reshape(var_1826.astype('float32'), [13,])), 1)
output = relay.Tuple([bop_1816,call_1825,var_1826,])
output2 = relay.Tuple([bop_1819,call_1827,var_1826,])
func_1833 = relay.Function([var_1815,var_1826,], output)
mod['func_1833'] = func_1833
mod = relay.transform.InferType()(mod)
mutated_mod['func_1833'] = func_1833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1833_call = mutated_mod.get_global_var('func_1833')
var_1835 = relay.var("var_1835", dtype = "float64", shape = (6, 8, 11))#candidate|1835|(6, 8, 11)|var|float64
var_1836 = relay.var("var_1836", dtype = "float32", shape = (1, 13))#candidate|1836|(1, 13)|var|float32
call_1834 = func_1833_call(var_1835,var_1836,)
output = call_1834
func_1837 = relay.Function([var_1835,var_1836,], output)
mutated_mod['func_1837'] = func_1837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1729_call = mod.get_global_var('func_1729')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_1852 = relay.TupleGetItem(func_1729_call(), 0)
call_1853 = relay.TupleGetItem(func_1730_call(), 0)
output = call_1852
output2 = call_1853
func_1859 = relay.Function([], output)
mod['func_1859'] = func_1859
mod = relay.transform.InferType()(mod)
output = func_1859()
func_1860 = relay.Function([], output)
mutated_mod['func_1860'] = func_1860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_1879 = func_1502_call()
call_1880 = func_1502_call()
func_1632_call = mod.get_global_var('func_1632')
func_1635_call = mutated_mod.get_global_var('func_1635')
var_1885 = relay.var("var_1885", dtype = "uint8", shape = (96,))#candidate|1885|(96,)|var|uint8
call_1884 = relay.TupleGetItem(func_1632_call(relay.reshape(var_1885.astype('uint8'), [96,])), 0)
call_1886 = relay.TupleGetItem(func_1635_call(relay.reshape(var_1885.astype('uint8'), [96,])), 0)
uop_1897 = relay.atan(var_1885.astype('float32')) # shape=(96,)
output = relay.Tuple([call_1879,call_1884,uop_1897,])
output2 = relay.Tuple([call_1880,call_1886,uop_1897,])
func_1900 = relay.Function([var_1885,], output)
mod['func_1900'] = func_1900
mod = relay.transform.InferType()(mod)
var_1901 = relay.var("var_1901", dtype = "uint8", shape = (96,))#candidate|1901|(96,)|var|uint8
output = func_1900(var_1901)
func_1902 = relay.Function([var_1901], output)
mutated_mod['func_1902'] = func_1902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_1916 = relay.TupleGetItem(func_1717_call(), 1)
call_1917 = relay.TupleGetItem(func_1718_call(), 1)
uop_1919 = relay.rsqrt(call_1916.astype('float32')) # shape=(6, 8, 11)
uop_1921 = relay.rsqrt(call_1917.astype('float32')) # shape=(6, 8, 11)
output = relay.Tuple([uop_1919,])
output2 = relay.Tuple([uop_1921,])
func_1923 = relay.Function([], output)
mod['func_1923'] = func_1923
mod = relay.transform.InferType()(mod)
mutated_mod['func_1923'] = func_1923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1923_call = mutated_mod.get_global_var('func_1923')
call_1924 = func_1923_call()
output = call_1924
func_1925 = relay.Function([], output)
mutated_mod['func_1925'] = func_1925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2002 = relay.var("var_2002", dtype = "float32", shape = (5, 15, 11))#candidate|2002|(5, 15, 11)|var|float32
var_2003 = relay.var("var_2003", dtype = "float32", shape = (5, 15, 11))#candidate|2003|(5, 15, 11)|var|float32
bop_2004 = relay.maximum(var_2002.astype('float32'), relay.reshape(var_2003.astype('float32'), relay.shape_of(var_2002))) # shape=(5, 15, 11)
func_1123_call = mod.get_global_var('func_1123')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_2009 = relay.TupleGetItem(func_1123_call(), 0)
call_2010 = relay.TupleGetItem(func_1125_call(), 0)
func_743_call = mod.get_global_var('func_743')
func_746_call = mutated_mod.get_global_var('func_746')
var_2019 = relay.var("var_2019", dtype = "float32", shape = (405,))#candidate|2019|(405,)|var|float32
call_2018 = relay.TupleGetItem(func_743_call(relay.reshape(var_2019.astype('float32'), [15, 3, 9])), 3)
call_2020 = relay.TupleGetItem(func_746_call(relay.reshape(var_2019.astype('float32'), [15, 3, 9])), 3)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_2023 = relay.TupleGetItem(func_680_call(), 0)
call_2024 = relay.TupleGetItem(func_682_call(), 0)
output = relay.Tuple([bop_2004,call_2009,call_2018,var_2019,call_2023,])
output2 = relay.Tuple([bop_2004,call_2010,call_2020,var_2019,call_2024,])
func_2037 = relay.Function([var_2002,var_2003,var_2019,], output)
mod['func_2037'] = func_2037
mod = relay.transform.InferType()(mod)
var_2038 = relay.var("var_2038", dtype = "float32", shape = (5, 15, 11))#candidate|2038|(5, 15, 11)|var|float32
var_2039 = relay.var("var_2039", dtype = "float32", shape = (5, 15, 11))#candidate|2039|(5, 15, 11)|var|float32
var_2040 = relay.var("var_2040", dtype = "float32", shape = (405,))#candidate|2040|(405,)|var|float32
output = func_2037(var_2038,var_2039,var_2040,)
func_2041 = relay.Function([var_2038,var_2039,var_2040,], output)
mutated_mod['func_2041'] = func_2041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_2119 = relay.TupleGetItem(func_988_call(), 0)
call_2120 = relay.TupleGetItem(func_990_call(), 0)
output = relay.Tuple([call_2119,])
output2 = relay.Tuple([call_2120,])
func_2123 = relay.Function([], output)
mod['func_2123'] = func_2123
mod = relay.transform.InferType()(mod)
output = func_2123()
func_2124 = relay.Function([], output)
mutated_mod['func_2124'] = func_2124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1123_call = mod.get_global_var('func_1123')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_2130 = relay.TupleGetItem(func_1123_call(), 0)
call_2131 = relay.TupleGetItem(func_1125_call(), 0)
func_2037_call = mod.get_global_var('func_2037')
func_2041_call = mutated_mod.get_global_var('func_2041')
const_2152 = relay.const([8.570501,-2.579176,0.133842,-4.427974,-5.059658,5.144387,-2.628674,2.396949,-6.688855,-7.127646,-5.377226,5.294029,-2.729729,3.265577,5.543590,-0.993825,6.081515,4.976747,-5.762904,-6.989334,-1.073612,-1.198547,-6.790461,2.956278,-4.085053,1.438923,5.268709,-9.722549,3.450060,0.809118,1.897164,6.448030,8.675798,4.980125,-2.043853,-6.353931,9.304997,-7.949190,-9.695284,3.820203,3.703094,-2.958936,2.154977,-7.526527,-0.961562,9.709385,5.914172,-7.484584,-6.737406,0.495301,9.343309,5.664683,-4.685245,-3.682941,5.804113,1.036255,-8.936282,8.525900,-6.862280,-8.965001,-9.106567,-0.921969,-0.267453,-9.955082,-4.255939,-0.509355,8.861498,-8.742553,9.467002,-3.992566,-6.062591,5.744142,1.010941,0.306920,-5.247602,-9.459362,2.593707,9.944132,5.212385,-3.550945,9.495736,-6.893190,5.802606,-6.940255,3.796443,2.946502,-3.659023,4.024607,-2.729044,7.050803,-6.063981,4.200601,-9.868584,-9.164148,-7.622183,9.132590,3.488756,-7.350579,-4.907497,6.146576,6.587798,-2.163845,8.061152,-6.158376,-8.449374,-8.130799,3.967846,-4.443796,-7.516462,-2.700106,-1.312823,-6.865631,8.600359,-9.510564,3.631652,2.961874,-4.253856,-1.502289,7.732549,6.474398,-4.676612,2.840305,6.062542,4.058872,-0.304590,-6.252030,4.778519,-0.329155,0.124537,1.495412,-5.899689,-0.361088,-5.978355,-1.254039,8.511379,9.156624,5.786233,9.587240,-1.061451,2.246519,-5.502445,3.527762,-4.329574,-0.859227,-6.997425,3.775223,1.342656,-0.004501,-2.434304,2.662428,-9.067546,-0.602367,8.191653,2.801855,-7.811843,-5.040997,-6.993889,8.386717,9.573721,3.306925,9.506102,-8.518921,-3.789245,-7.430671,7.641424,-3.493061,-6.855061,-3.131767,-4.469548,2.817910,-7.727027,-0.076725,-8.279187,8.690456,0.861639,4.399757,6.074932,2.007820,-6.735210,5.913359,-8.124755,-7.126216,-7.277639,-0.283720,-0.151025,3.319501,-0.147060,6.405661,6.197356,-7.000793,4.486473,1.531877,-5.541873,-3.310273,-7.037559,-5.011158,7.159319,4.811679,8.389455,7.889106,-2.215795,-4.835036,-3.896237,6.111541,9.471390,-2.709897,6.887963,4.838603,8.753397,4.445177,6.422614,-1.071396,-1.102360,-2.409308,4.703901,9.615657,3.170438,-0.600555,9.032867,7.040499,-0.004600,-5.645247,-6.527127,6.448331,6.034669,3.632096,-9.517046,-6.355210,-8.278514,3.445430,-4.040375,0.729992,-1.928123,3.903001,0.848971,-0.637957,-6.399944,1.584559,5.432414,-1.649764,0.690546,8.015543,8.357252,-8.958768,5.156419,-5.687835,-5.100878,7.556035,2.367947,6.245661,3.407324,-8.964213,-6.562444,-8.574447,-0.887208,-5.197251,1.241477,-5.993609,9.536318,-8.488357,-1.237910,-3.576607,-9.157905,0.209376,-0.628997,-1.640395,0.122482,-2.520138,-5.887549,3.575142,1.118394,1.180965,9.514032,-2.584710,-1.419012,8.063002,9.541481,-4.690098,0.243205,1.818702,-7.401104,-7.293355,9.255973,1.012011,8.416024,-8.146694,-7.864502,0.742457,0.896858,0.305335,-6.546498,-1.448035,-4.981641,1.814270,8.070455,-5.901440,-7.785500,0.013339,5.199885,-5.367139,5.185816,1.756914,-3.258054,0.788591,-0.067205,4.234053,-1.439424,-5.779681,-2.119918,-4.661299,0.570214,0.124602,6.756823,6.456553,6.422932,-6.717052,-4.997081,9.983806,-9.221119,7.058243,2.874058,-4.723713,-5.834863,-1.737171,-1.078642,-2.318634,4.797215,-8.791840,-9.030496,9.528740,8.716132,-9.186899,-1.435200,-9.191472,8.907648,1.173204,-1.097962,-7.734742,1.948439,-7.416479,9.482696,3.980110,-1.948176,-3.922426,1.071075,9.516040,9.087161,-3.383565,3.039073,-9.455161,-1.472695,3.912272,7.434265,-5.539395,-7.963486,4.582880,1.738364,2.517661,-4.628000,1.822919,5.399749,-4.297653,-1.218654,-9.268395,4.082227,-8.531594,4.134747,-6.651392,7.464272,7.972610,2.699708,-9.363792,4.892521,6.334854,9.887419,1.193585,3.895494,7.109119,-8.533223,9.941512,-3.494504,-5.921317,8.370435,6.669693,0.442879,-5.044604,8.420704,0.371470,-6.889588,-3.950451,7.489406,7.911770,0.702797,5.911962,-5.927826,1.282048,-4.506807,-0.867140,-4.605921,1.242320,-7.552464,5.520750,-9.039277,-7.542103,1.147213,-8.633955,-9.763294,8.638009,-9.367665,-3.164152,9.903476,6.481001,8.130159,7.516064,0.445321,0.717285,-8.399706,5.564796,4.063623,-8.821154,-6.492477,-0.887212,-5.039266,-2.704063,-0.502602,0.907581,-5.725207,2.485993,7.942813,-1.097070,3.230030,-1.550399,-7.244971,-4.226334,-9.113314,-2.911824,0.131777,4.822148,-5.709733,-2.993227,-2.148433,-1.178918,0.749090,-1.696482,-6.828931,6.989255,-3.685369,8.597290,-6.372484,2.726732,-2.790499,2.900148,-8.843860,8.906925,6.586447,9.465443,-3.941759,-9.091635,1.160514,-0.844211,8.399873,-4.841302,4.970971,-3.301767,4.283828,-6.599401,2.694115,-4.123495,6.930429,-8.187275,8.829500,-0.024926,6.282943,5.142953,-6.162612,-1.743685,-5.772325,9.801762,2.996157,4.166399,8.458930,-6.715859,4.252607,-1.710732,6.544409,4.355518,-0.982332,-1.857764,4.272742,6.111404,3.131101,4.782762,-8.302197,1.499104,1.803089,-0.285480,4.821728,6.699650,7.751636,4.959298,4.805531,-0.831037,-4.223738,6.339158,-5.901559,3.840171,7.817305,2.045817,-1.026660,2.059927,6.803159,-6.284204,-9.540167,-3.185666,-6.042906,-5.497213,-1.008230,5.481861,5.683094,-8.391549,4.400246,4.787002,0.418941,-6.367262,-7.055940,7.270997,-7.909296,-8.659537,3.977517,-6.423006,-7.421961,7.984891,9.964030,2.968957,-3.507589,9.012498,-0.007502,-4.465998,5.614192,8.056127,-3.940656,-2.814242,-1.499925,7.013370,7.182594,8.530136,7.791113,-3.679038,-6.210920,4.507188,-0.022790,-5.703184,-5.193229,-9.899273,-4.901970,9.681229,-9.441682,5.363105,-7.667864,-6.448181,-5.216672,3.133678,4.465812,1.379589,0.008163,-2.621818,1.055557,-2.597029,3.666870,4.436667,-4.804183,-6.841706,-2.150362,-2.990284,-7.805052,-5.192407,-1.271390,-5.089656,-5.090251,4.551458,8.605906,1.438930,0.638323,-2.128596,-8.438648,-5.723387,-4.141821,3.718264,-3.998463,7.828914,-2.447404,7.038841,9.451098,-9.134187,0.213858,2.046508,5.094266,2.274386,0.236627,1.206441,-3.276764,-6.496500,-4.880394,0.733982,7.020271,-4.569064,7.132424,7.815784,8.873979,-6.351387,5.613161,2.293322,-0.100905,1.595170,-7.400522,4.784459,-2.160943,2.522297,4.710050,0.140624,7.998438,-9.501204,-8.923509,6.074995,-5.206392,-1.854665,-7.751088,-9.716492,6.537244,-3.970780,8.681624,-4.758536,3.598302,-0.393545,-5.557055,-6.449954,8.087369,-3.804892,-9.892770,-3.797073,1.358809,-1.751757,-5.565407,-8.411719,7.562117,-1.792048,-4.727958,-4.203792,-0.677039,-0.615236,7.980541,8.281719,-3.330879,-1.369041,6.564069,5.113068,8.122408,-3.757998,-0.045393,7.481105,3.789999,-6.785461,-4.264129,-2.177617,-1.680129,-4.724648,1.179240,-9.179915,5.830762,-6.417876,5.300481,-4.894422,7.882822,5.749240,1.107222,8.088454,-1.783627,0.624175,1.727211,5.859151,-0.754628,6.425642,8.337126,7.361958,-5.339625,-6.849532,2.776959,-6.394434,5.981579,2.643042,3.312486,-0.096617,-4.660807,-2.989729,3.279925,8.736712,9.350974,9.718441,3.729160,-0.895195,-4.635536,9.083138,9.616615,-2.833628,8.558478,6.664946,2.769198,-1.005410,1.692759,7.317192,8.660269,4.755225,9.998597,9.902389,9.314932,-0.213498,-9.573949,-0.334615,8.337847,4.722753,-5.667150,3.089449,-3.043965,3.366890,2.500329,-4.263713,-7.466304,7.424301,-2.881283,-5.916938,-9.110255,4.572397,-2.445856,-4.833758,-7.282097,7.971225,9.014115,-5.501105,-2.688184,3.027841,-0.864205,-8.568201,2.928019,-7.494975,7.239976,-6.341431,9.786059,-7.232037,4.112767,-8.169618,-2.733464,-5.896373,-6.567091,8.413292,-6.811321,-4.508953,-0.063517,5.538473,4.778108,2.549493,-1.440945,-6.920928,1.120528,-5.930287,-2.780354,9.595864,-9.373353,-4.677738,-2.665258,9.133838,-2.490469,-7.621080,0.489108,4.991252,2.594614,2.897407,-6.415809,-6.447463,-1.683369,-1.116063,4.475425,-8.020475,1.984305,-9.373262,-7.582656,-9.335801,-0.983762,-4.493358,9.999598,-6.898833,-2.385473,-7.176339,1.452698,6.828959,4.572238,-4.432654,2.948982,-1.972640,0.058077,-2.739329,7.791109,8.879668,2.478527,5.411427,4.118858,-9.309021,6.538004,-6.178052,3.316393,-7.198729,0.783749,3.906861,3.280972,7.313442,-3.297577,1.712142,-5.947433,0.363494,-1.218584,-5.908265,-0.413002,7.116187,-7.351236,9.117528,8.153205], dtype = "float32")#candidate|2152|(825,)|const|float32
var_2153 = relay.var("var_2153", dtype = "float32", shape = (405,))#candidate|2153|(405,)|var|float32
call_2151 = relay.TupleGetItem(func_2037_call(relay.reshape(const_2152.astype('float32'), [5, 15, 11]), relay.reshape(const_2152.astype('float32'), [5, 15, 11]), relay.reshape(var_2153.astype('float32'), [405,]), ), 2)
call_2154 = relay.TupleGetItem(func_2041_call(relay.reshape(const_2152.astype('float32'), [5, 15, 11]), relay.reshape(const_2152.astype('float32'), [5, 15, 11]), relay.reshape(var_2153.astype('float32'), [405,]), ), 2)
func_1097_call = mod.get_global_var('func_1097')
func_1099_call = mutated_mod.get_global_var('func_1099')
call_2160 = relay.TupleGetItem(func_1097_call(relay.reshape(var_2153.astype('float32'), [15, 3, 9])), 0)
call_2161 = relay.TupleGetItem(func_1099_call(relay.reshape(var_2153.astype('float32'), [15, 3, 9])), 0)
output = relay.Tuple([call_2130,call_2151,const_2152,var_2153,call_2160,])
output2 = relay.Tuple([call_2131,call_2154,const_2152,var_2153,call_2161,])
func_2165 = relay.Function([var_2153,], output)
mod['func_2165'] = func_2165
mod = relay.transform.InferType()(mod)
var_2166 = relay.var("var_2166", dtype = "float32", shape = (405,))#candidate|2166|(405,)|var|float32
output = func_2165(var_2166)
func_2167 = relay.Function([var_2166], output)
mutated_mod['func_2167'] = func_2167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_2195 = func_1291_call()
call_2196 = func_1291_call()
func_1097_call = mod.get_global_var('func_1097')
func_1099_call = mutated_mod.get_global_var('func_1099')
call_2200 = relay.TupleGetItem(func_1097_call(relay.reshape(call_2195.astype('float32'), [15, 3, 9])), 1)
call_2201 = relay.TupleGetItem(func_1099_call(relay.reshape(call_2195.astype('float32'), [15, 3, 9])), 1)
var_2205 = relay.var("var_2205", dtype = "float64", shape = (15, 3, 9))#candidate|2205|(15, 3, 9)|var|float64
bop_2206 = relay.minimum(call_2200.astype('uint64'), relay.reshape(var_2205.astype('uint64'), relay.shape_of(call_2200))) # shape=(15, 3, 9)
bop_2209 = relay.minimum(call_2201.astype('uint64'), relay.reshape(var_2205.astype('uint64'), relay.shape_of(call_2201))) # shape=(15, 3, 9)
output = relay.Tuple([call_2195,bop_2206,])
output2 = relay.Tuple([call_2196,bop_2209,])
func_2224 = relay.Function([var_2205,], output)
mod['func_2224'] = func_2224
mod = relay.transform.InferType()(mod)
mutated_mod['func_2224'] = func_2224
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2225 = relay.var("var_2225", dtype = "float64", shape = (15, 3, 9))#candidate|2225|(15, 3, 9)|var|float64
func_2224_call = mutated_mod.get_global_var('func_2224')
call_2226 = func_2224_call(var_2225)
output = call_2226
func_2227 = relay.Function([var_2225], output)
mutated_mod['func_2227'] = func_2227
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2233 = relay.var("var_2233", dtype = "bool", shape = (4, 8, 1))#candidate|2233|(4, 8, 1)|var|bool
var_2234 = relay.var("var_2234", dtype = "bool", shape = (4, 8, 2))#candidate|2234|(4, 8, 2)|var|bool
bop_2235 = relay.logical_and(var_2233.astype('bool'), var_2234.astype('bool')) # shape=(4, 8, 2)
func_1218_call = mod.get_global_var('func_1218')
func_1225_call = mutated_mod.get_global_var('func_1225')
var_2244 = relay.var("var_2244", dtype = "uint16", shape = (702,))#candidate|2244|(702,)|var|uint16
var_2245 = relay.var("var_2245", dtype = "bool", shape = (528,))#candidate|2245|(528,)|var|bool
var_2246 = relay.var("var_2246", dtype = "float32", shape = (405,))#candidate|2246|(405,)|var|float32
const_2247 = relay.const([False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,True], dtype = "bool")#candidate|2247|(88,)|const|bool
var_2248 = relay.var("var_2248", dtype = "float32", shape = (13,))#candidate|2248|(13,)|var|float32
call_2243 = relay.TupleGetItem(func_1218_call(relay.reshape(var_2244.astype('uint16'), [1, 702]), relay.reshape(var_2245.astype('bool'), [6, 8, 11]), relay.reshape(var_2246.astype('float32'), [405,]), relay.reshape(const_2247.astype('bool'), [88,]), relay.reshape(var_2248.astype('float32'), [13,]), ), 9)
call_2249 = relay.TupleGetItem(func_1225_call(relay.reshape(var_2244.astype('uint16'), [1, 702]), relay.reshape(var_2245.astype('bool'), [6, 8, 11]), relay.reshape(var_2246.astype('float32'), [405,]), relay.reshape(const_2247.astype('bool'), [88,]), relay.reshape(var_2248.astype('float32'), [13,]), ), 9)
func_1833_call = mod.get_global_var('func_1833')
func_1837_call = mutated_mod.get_global_var('func_1837')
call_2257 = relay.TupleGetItem(func_1833_call(relay.reshape(var_2245.astype('float64'), [6, 8, 11]), relay.reshape(var_2248.astype('float32'), [1, 13]), ), 1)
call_2258 = relay.TupleGetItem(func_1837_call(relay.reshape(var_2245.astype('float64'), [6, 8, 11]), relay.reshape(var_2248.astype('float32'), [1, 13]), ), 1)
bop_2261 = relay.left_shift(var_2233.astype('uint64'), const_2247.astype('uint64')) # shape=(4, 8, 88)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_2271 = relay.TupleGetItem(func_2123_call(), 0)
call_2272 = relay.TupleGetItem(func_2124_call(), 0)
uop_2281 = relay.sigmoid(var_2233.astype('float32')) # shape=(4, 8, 1)
output = relay.Tuple([bop_2235,call_2243,var_2244,var_2245,var_2246,var_2248,call_2257,bop_2261,call_2271,uop_2281,])
output2 = relay.Tuple([bop_2235,call_2249,var_2244,var_2245,var_2246,var_2248,call_2258,bop_2261,call_2272,uop_2281,])
func_2284 = relay.Function([var_2233,var_2234,var_2244,var_2245,var_2246,var_2248,], output)
mod['func_2284'] = func_2284
mod = relay.transform.InferType()(mod)
mutated_mod['func_2284'] = func_2284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2284_call = mutated_mod.get_global_var('func_2284')
var_2286 = relay.var("var_2286", dtype = "bool", shape = (4, 8, 1))#candidate|2286|(4, 8, 1)|var|bool
var_2287 = relay.var("var_2287", dtype = "bool", shape = (4, 8, 2))#candidate|2287|(4, 8, 2)|var|bool
var_2288 = relay.var("var_2288", dtype = "uint16", shape = (702,))#candidate|2288|(702,)|var|uint16
var_2289 = relay.var("var_2289", dtype = "bool", shape = (528,))#candidate|2289|(528,)|var|bool
var_2290 = relay.var("var_2290", dtype = "float32", shape = (405,))#candidate|2290|(405,)|var|float32
var_2291 = relay.var("var_2291", dtype = "float32", shape = (13,))#candidate|2291|(13,)|var|float32
call_2285 = func_2284_call(var_2286,var_2287,var_2288,var_2289,var_2290,var_2291,)
output = call_2285
func_2292 = relay.Function([var_2286,var_2287,var_2288,var_2289,var_2290,var_2291,], output)
mutated_mod['func_2292'] = func_2292
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2318 = relay.const(2, dtype = "int16")#candidate|2318|()|const|int16
var_2319 = relay.var("var_2319", dtype = "int16", shape = (4, 6, 8))#candidate|2319|(4, 6, 8)|var|int16
bop_2320 = relay.bitwise_or(const_2318.astype('int16'), var_2319.astype('int16')) # shape=(4, 6, 8)
uop_2324 = relay.cosh(bop_2320.astype('float32')) # shape=(4, 6, 8)
output = relay.Tuple([uop_2324,])
output2 = relay.Tuple([uop_2324,])
func_2329 = relay.Function([var_2319,], output)
mod['func_2329'] = func_2329
mod = relay.transform.InferType()(mod)
var_2330 = relay.var("var_2330", dtype = "int16", shape = (4, 6, 8))#candidate|2330|(4, 6, 8)|var|int16
output = func_2329(var_2330)
func_2331 = relay.Function([var_2330], output)
mutated_mod['func_2331'] = func_2331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_2361 = func_1291_call()
call_2362 = func_1291_call()
output = relay.Tuple([call_2361,])
output2 = relay.Tuple([call_2362,])
func_2364 = relay.Function([], output)
mod['func_2364'] = func_2364
mod = relay.transform.InferType()(mod)
output = func_2364()
func_2365 = relay.Function([], output)
mutated_mod['func_2365'] = func_2365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_2411 = func_1291_call()
call_2412 = func_1291_call()
output = relay.Tuple([call_2411,])
output2 = relay.Tuple([call_2412,])
func_2419 = relay.Function([], output)
mod['func_2419'] = func_2419
mod = relay.transform.InferType()(mod)
output = func_2419()
func_2420 = relay.Function([], output)
mutated_mod['func_2420'] = func_2420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1377_call = mod.get_global_var('func_1377')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_2437 = relay.TupleGetItem(func_1377_call(), 2)
call_2438 = relay.TupleGetItem(func_1379_call(), 2)
output = call_2437
output2 = call_2438
func_2451 = relay.Function([], output)
mod['func_2451'] = func_2451
mod = relay.transform.InferType()(mod)
output = func_2451()
func_2452 = relay.Function([], output)
mutated_mod['func_2452'] = func_2452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_2453 = func_1291_call()
call_2454 = func_1291_call()
func_2165_call = mod.get_global_var('func_2165')
func_2167_call = mutated_mod.get_global_var('func_2167')
call_2480 = relay.TupleGetItem(func_2165_call(relay.reshape(call_2453.astype('float32'), [405,])), 2)
call_2481 = relay.TupleGetItem(func_2167_call(relay.reshape(call_2453.astype('float32'), [405,])), 2)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_2484 = relay.TupleGetItem(func_813_call(), 2)
call_2485 = relay.TupleGetItem(func_815_call(), 2)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_2513 = relay.TupleGetItem(func_988_call(), 0)
call_2514 = relay.TupleGetItem(func_990_call(), 0)
func_1900_call = mod.get_global_var('func_1900')
func_1902_call = mutated_mod.get_global_var('func_1902')
const_2518 = relay.const([[10,8,7,6,-1,5,10,8,7,-3,-1,1,-4,8,1,-1,-3,-8,6,-2,-6,8,7,2],[-5,10,-7,-8,5,7,4,-4,-6,9,-8,-10,8,-2,8,-10,9,1,-2,-1,4,3,-5,-7],[3,4,7,-8,3,-3,-6,-6,-4,2,-5,-4,-10,-7,8,-7,-9,2,8,4,-10,4,1,-10],[6,-4,-7,-8,-7,-6,-8,-6,6,5,-6,7,6,-1,-1,4,4,-6,8,2,10,10,2,7]], dtype = "uint8")#candidate|2518|(4, 24)|const|uint8
call_2517 = relay.TupleGetItem(func_1900_call(relay.reshape(const_2518.astype('uint8'), [96,])), 1)
call_2519 = relay.TupleGetItem(func_1902_call(relay.reshape(const_2518.astype('uint8'), [96,])), 1)
uop_2521 = relay.sigmoid(call_2480.astype('float64')) # shape=(825,)
uop_2523 = relay.sigmoid(call_2481.astype('float64')) # shape=(825,)
uop_2526 = relay.acos(uop_2521.astype('float64')) # shape=(825,)
uop_2528 = relay.acos(uop_2523.astype('float64')) # shape=(825,)
func_1377_call = mod.get_global_var('func_1377')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_2532 = relay.TupleGetItem(func_1377_call(), 0)
call_2533 = relay.TupleGetItem(func_1379_call(), 0)
var_2534 = relay.var("var_2534", dtype = "bool", shape = (6, 8, 11))#candidate|2534|(6, 8, 11)|var|bool
bop_2535 = relay.bitwise_or(call_2532.astype('uint64'), relay.reshape(var_2534.astype('uint64'), relay.shape_of(call_2532))) # shape=(6, 8, 11)
bop_2538 = relay.bitwise_or(call_2533.astype('uint64'), relay.reshape(var_2534.astype('uint64'), relay.shape_of(call_2533))) # shape=(6, 8, 11)
output = relay.Tuple([call_2453,call_2484,call_2513,call_2517,const_2518,uop_2526,bop_2535,])
output2 = relay.Tuple([call_2454,call_2485,call_2514,call_2519,const_2518,uop_2528,bop_2538,])
func_2541 = relay.Function([var_2534,], output)
mod['func_2541'] = func_2541
mod = relay.transform.InferType()(mod)
mutated_mod['func_2541'] = func_2541
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2542 = relay.var("var_2542", dtype = "bool", shape = (6, 8, 11))#candidate|2542|(6, 8, 11)|var|bool
func_2541_call = mutated_mod.get_global_var('func_2541')
call_2543 = func_2541_call(var_2542)
output = call_2543
func_2544 = relay.Function([var_2542], output)
mutated_mod['func_2544'] = func_2544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_2546 = relay.TupleGetItem(func_813_call(), 2)
call_2547 = relay.TupleGetItem(func_815_call(), 2)
func_375_call = mod.get_global_var('func_375')
func_379_call = mutated_mod.get_global_var('func_379')
const_2555 = relay.const(5, dtype = "uint16")#candidate|2555|()|const|uint16
var_2556 = relay.var("var_2556", dtype = "uint16", shape = (72,))#candidate|2556|(72,)|var|uint16
var_2557 = relay.var("var_2557", dtype = "float32", shape = (13,))#candidate|2557|(13,)|var|float32
call_2554 = relay.TupleGetItem(func_375_call(relay.reshape(const_2555.astype('uint16'), []), relay.reshape(var_2556.astype('uint16'), [6, 12, 1]), relay.reshape(var_2557.astype('float32'), [13,]), ), 2)
call_2558 = relay.TupleGetItem(func_379_call(relay.reshape(const_2555.astype('uint16'), []), relay.reshape(var_2556.astype('uint16'), [6, 12, 1]), relay.reshape(var_2557.astype('float32'), [13,]), ), 2)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_2560 = relay.TupleGetItem(func_813_call(), 1)
call_2561 = relay.TupleGetItem(func_815_call(), 1)
uop_2568 = relay.log10(var_2556.astype('float64')) # shape=(72,)
func_946_call = mod.get_global_var('func_946')
func_948_call = mutated_mod.get_global_var('func_948')
call_2573 = relay.TupleGetItem(func_946_call(relay.reshape(call_2554.astype('float32'), [13,])), 1)
call_2574 = relay.TupleGetItem(func_948_call(relay.reshape(call_2554.astype('float32'), [13,])), 1)
output = relay.Tuple([call_2546,call_2554,const_2555,var_2557,call_2560,uop_2568,call_2573,])
output2 = relay.Tuple([call_2547,call_2558,const_2555,var_2557,call_2561,uop_2568,call_2574,])
func_2575 = relay.Function([var_2556,var_2557,], output)
mod['func_2575'] = func_2575
mod = relay.transform.InferType()(mod)
var_2576 = relay.var("var_2576", dtype = "uint16", shape = (72,))#candidate|2576|(72,)|var|uint16
var_2577 = relay.var("var_2577", dtype = "float32", shape = (13,))#candidate|2577|(13,)|var|float32
output = func_2575(var_2576,var_2577,)
func_2578 = relay.Function([var_2576,var_2577,], output)
mutated_mod['func_2578'] = func_2578
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2598 = relay.var("var_2598", dtype = "float32", shape = (6, 3, 3))#candidate|2598|(6, 3, 3)|var|float32
uop_2599 = relay.sigmoid(var_2598.astype('float32')) # shape=(6, 3, 3)
uop_2614 = relay.rsqrt(uop_2599.astype('float32')) # shape=(6, 3, 3)
output = uop_2614
output2 = uop_2614
func_2618 = relay.Function([var_2598,], output)
mod['func_2618'] = func_2618
mod = relay.transform.InferType()(mod)
var_2619 = relay.var("var_2619", dtype = "float32", shape = (6, 3, 3))#candidate|2619|(6, 3, 3)|var|float32
output = func_2618(var_2619)
func_2620 = relay.Function([var_2619], output)
mutated_mod['func_2620'] = func_2620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_2630 = relay.TupleGetItem(func_2123_call(), 0)
call_2631 = relay.TupleGetItem(func_2124_call(), 0)
uop_2632 = relay.acosh(call_2630.astype('float64')) # shape=(6, 8, 11)
uop_2634 = relay.acosh(call_2631.astype('float64')) # shape=(6, 8, 11)
output = uop_2632
output2 = uop_2634
func_2648 = relay.Function([], output)
mod['func_2648'] = func_2648
mod = relay.transform.InferType()(mod)
output = func_2648()
func_2649 = relay.Function([], output)
mutated_mod['func_2649'] = func_2649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_2737 = func_1291_call()
call_2738 = func_1291_call()
uop_2742 = relay.log(call_2737.astype('float64')) # shape=(15, 3, 9)
uop_2744 = relay.log(call_2738.astype('float64')) # shape=(15, 3, 9)
uop_2749 = relay.sigmoid(uop_2742.astype('float64')) # shape=(15, 3, 9)
uop_2751 = relay.sigmoid(uop_2744.astype('float64')) # shape=(15, 3, 9)
func_1923_call = mod.get_global_var('func_1923')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_2771 = relay.TupleGetItem(func_1923_call(), 0)
call_2772 = relay.TupleGetItem(func_1925_call(), 0)
output = relay.Tuple([uop_2749,call_2771,])
output2 = relay.Tuple([uop_2751,call_2772,])
func_2777 = relay.Function([], output)
mod['func_2777'] = func_2777
mod = relay.transform.InferType()(mod)
output = func_2777()
func_2778 = relay.Function([], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2365_call = mutated_mod.get_global_var('func_2365')
call_2848 = relay.TupleGetItem(func_2364_call(), 0)
call_2849 = relay.TupleGetItem(func_2365_call(), 0)
func_946_call = mod.get_global_var('func_946')
func_948_call = mutated_mod.get_global_var('func_948')
var_2859 = relay.var("var_2859", dtype = "float32", shape = (13,))#candidate|2859|(13,)|var|float32
call_2858 = relay.TupleGetItem(func_946_call(relay.reshape(var_2859.astype('float32'), [13,])), 0)
call_2860 = relay.TupleGetItem(func_948_call(relay.reshape(var_2859.astype('float32'), [13,])), 0)
var_2861 = relay.var("var_2861", dtype = "uint16", shape = (15, 3, 9))#candidate|2861|(15, 3, 9)|var|uint16
bop_2862 = relay.mod(call_2848.astype('float64'), relay.reshape(var_2861.astype('float64'), relay.shape_of(call_2848))) # shape=(15, 3, 9)
bop_2865 = relay.mod(call_2849.astype('float64'), relay.reshape(var_2861.astype('float64'), relay.shape_of(call_2849))) # shape=(15, 3, 9)
uop_2880 = relay.sin(var_2861.astype('float64')) # shape=(15, 3, 9)
output = relay.Tuple([call_2858,var_2859,bop_2862,uop_2880,])
output2 = relay.Tuple([call_2860,var_2859,bop_2865,uop_2880,])
func_2886 = relay.Function([var_2859,var_2861,], output)
mod['func_2886'] = func_2886
mod = relay.transform.InferType()(mod)
mutated_mod['func_2886'] = func_2886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2886_call = mutated_mod.get_global_var('func_2886')
var_2888 = relay.var("var_2888", dtype = "float32", shape = (13,))#candidate|2888|(13,)|var|float32
var_2889 = relay.var("var_2889", dtype = "uint16", shape = (15, 3, 9))#candidate|2889|(15, 3, 9)|var|uint16
call_2887 = func_2886_call(var_2888,var_2889,)
output = call_2887
func_2890 = relay.Function([var_2888,var_2889,], output)
mutated_mod['func_2890'] = func_2890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1860_call = mutated_mod.get_global_var('func_1860')
call_2900 = func_1859_call()
call_2901 = func_1859_call()
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_2918 = func_1571_call()
call_2919 = func_1571_call()
func_2575_call = mod.get_global_var('func_2575')
func_2578_call = mutated_mod.get_global_var('func_2578')
var_2924 = relay.var("var_2924", dtype = "uint16", shape = (72,))#candidate|2924|(72,)|var|uint16
const_2925 = relay.const([4.638597,-8.698793,8.964669,-4.897236,1.027934,8.467393,-1.371571,-0.945602,1.802504,5.181409,-7.047279,5.298906,-9.952549], dtype = "float32")#candidate|2925|(13,)|const|float32
call_2923 = relay.TupleGetItem(func_2575_call(relay.reshape(var_2924.astype('uint16'), [72,]), relay.reshape(const_2925.astype('float32'), [13,]), ), 1)
call_2926 = relay.TupleGetItem(func_2578_call(relay.reshape(var_2924.astype('uint16'), [72,]), relay.reshape(const_2925.astype('float32'), [13,]), ), 1)
func_2224_call = mod.get_global_var('func_2224')
func_2227_call = mutated_mod.get_global_var('func_2227')
var_2945 = relay.var("var_2945", dtype = "float64", shape = (405,))#candidate|2945|(405,)|var|float64
call_2944 = relay.TupleGetItem(func_2224_call(relay.reshape(var_2945.astype('float64'), [15, 3, 9])), 0)
call_2946 = relay.TupleGetItem(func_2227_call(relay.reshape(var_2945.astype('float64'), [15, 3, 9])), 0)
bop_2957 = relay.less_equal(call_2918.astype('bool'), relay.reshape(call_2900.astype('bool'), relay.shape_of(call_2918))) # shape=(6, 8, 11)
bop_2960 = relay.less_equal(call_2919.astype('bool'), relay.reshape(call_2901.astype('bool'), relay.shape_of(call_2919))) # shape=(6, 8, 11)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_2964 = relay.TupleGetItem(func_2123_call(), 0)
call_2965 = relay.TupleGetItem(func_2124_call(), 0)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_2980 = relay.TupleGetItem(func_1717_call(), 0)
call_2981 = relay.TupleGetItem(func_1718_call(), 0)
output = relay.Tuple([call_2923,var_2924,const_2925,call_2944,var_2945,bop_2957,call_2964,call_2980,])
output2 = relay.Tuple([call_2926,var_2924,const_2925,call_2946,var_2945,bop_2960,call_2965,call_2981,])
func_2987 = relay.Function([var_2924,var_2945,], output)
mod['func_2987'] = func_2987
mod = relay.transform.InferType()(mod)
mutated_mod['func_2987'] = func_2987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2987_call = mutated_mod.get_global_var('func_2987')
var_2989 = relay.var("var_2989", dtype = "uint16", shape = (72,))#candidate|2989|(72,)|var|uint16
var_2990 = relay.var("var_2990", dtype = "float64", shape = (405,))#candidate|2990|(405,)|var|float64
call_2988 = func_2987_call(var_2989,var_2990,)
output = call_2988
func_2991 = relay.Function([var_2989,var_2990,], output)
mutated_mod['func_2991'] = func_2991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2451_call = mod.get_global_var('func_2451')
func_2452_call = mutated_mod.get_global_var('func_2452')
call_3109 = func_2451_call()
call_3110 = func_2451_call()
output = relay.Tuple([call_3109,])
output2 = relay.Tuple([call_3110,])
func_3119 = relay.Function([], output)
mod['func_3119'] = func_3119
mod = relay.transform.InferType()(mod)
mutated_mod['func_3119'] = func_3119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3119_call = mutated_mod.get_global_var('func_3119')
call_3120 = func_3119_call()
output = call_3120
func_3121 = relay.Function([], output)
mutated_mod['func_3121'] = func_3121
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3231 = relay.var("var_3231", dtype = "float32", shape = (15, 16))#candidate|3231|(15, 16)|var|float32
var_3232 = relay.var("var_3232", dtype = "float32", shape = (15, 16))#candidate|3232|(15, 16)|var|float32
bop_3233 = relay.floor_divide(var_3231.astype('float32'), relay.reshape(var_3232.astype('float32'), relay.shape_of(var_3231))) # shape=(15, 16)
output = relay.Tuple([bop_3233,])
output2 = relay.Tuple([bop_3233,])
func_3236 = relay.Function([var_3231,var_3232,], output)
mod['func_3236'] = func_3236
mod = relay.transform.InferType()(mod)
mutated_mod['func_3236'] = func_3236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mutated_mod.get_global_var('func_3236')
var_3238 = relay.var("var_3238", dtype = "float32", shape = (15, 16))#candidate|3238|(15, 16)|var|float32
var_3239 = relay.var("var_3239", dtype = "float32", shape = (15, 16))#candidate|3239|(15, 16)|var|float32
call_3237 = func_3236_call(var_3238,var_3239,)
output = call_3237
func_3240 = relay.Function([var_3238,var_3239,], output)
mutated_mod['func_3240'] = func_3240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_3285 = relay.TupleGetItem(func_680_call(), 0)
call_3286 = relay.TupleGetItem(func_682_call(), 0)
output = call_3285
output2 = call_3286
func_3316 = relay.Function([], output)
mod['func_3316'] = func_3316
mod = relay.transform.InferType()(mod)
mutated_mod['func_3316'] = func_3316
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mutated_mod.get_global_var('func_3316')
call_3317 = func_3316_call()
output = call_3317
func_3318 = relay.Function([], output)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3119_call = mod.get_global_var('func_3119')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_3333 = relay.TupleGetItem(func_3119_call(), 0)
call_3334 = relay.TupleGetItem(func_3121_call(), 0)
func_530_call = mod.get_global_var('func_530')
func_535_call = mutated_mod.get_global_var('func_535')
var_3338 = relay.var("var_3338", dtype = "bool", shape = (2, 44))#candidate|3338|(2, 44)|var|bool
var_3339 = relay.var("var_3339", dtype = "uint16", shape = ())#candidate|3339|()|var|uint16
const_3340 = relay.const([7.261149,-7.461575,-6.125972,3.008214,-5.871079,-9.304447,8.268709,2.585644,4.936670,-2.122685,-4.866921,3.595751,-1.023382], dtype = "float32")#candidate|3340|(13,)|const|float32
call_3337 = relay.TupleGetItem(func_530_call(relay.reshape(var_3338.astype('bool'), [11, 2, 4]), relay.reshape(var_3338.astype('bool'), [11, 2, 4]), relay.reshape(var_3339.astype('uint16'), []), relay.reshape(const_3340.astype('float32'), [13,]), ), 3)
call_3341 = relay.TupleGetItem(func_535_call(relay.reshape(var_3338.astype('bool'), [11, 2, 4]), relay.reshape(var_3338.astype('bool'), [11, 2, 4]), relay.reshape(var_3339.astype('uint16'), []), relay.reshape(const_3340.astype('float32'), [13,]), ), 3)
output = relay.Tuple([call_3333,call_3337,var_3338,var_3339,const_3340,])
output2 = relay.Tuple([call_3334,call_3341,var_3338,var_3339,const_3340,])
func_3348 = relay.Function([var_3338,var_3339,], output)
mod['func_3348'] = func_3348
mod = relay.transform.InferType()(mod)
mutated_mod['func_3348'] = func_3348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3348_call = mutated_mod.get_global_var('func_3348')
var_3350 = relay.var("var_3350", dtype = "bool", shape = (2, 44))#candidate|3350|(2, 44)|var|bool
var_3351 = relay.var("var_3351", dtype = "uint16", shape = ())#candidate|3351|()|var|uint16
call_3349 = func_3348_call(var_3350,var_3351,)
output = call_3349
func_3352 = relay.Function([var_3350,var_3351,], output)
mutated_mod['func_3352'] = func_3352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mod.get_global_var('func_2419')
func_2420_call = mutated_mod.get_global_var('func_2420')
call_3371 = relay.TupleGetItem(func_2419_call(), 0)
call_3372 = relay.TupleGetItem(func_2420_call(), 0)
output = call_3371
output2 = call_3372
func_3377 = relay.Function([], output)
mod['func_3377'] = func_3377
mod = relay.transform.InferType()(mod)
output = func_3377()
func_3378 = relay.Function([], output)
mutated_mod['func_3378'] = func_3378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mod.get_global_var('func_2419')
func_2420_call = mutated_mod.get_global_var('func_2420')
call_3406 = relay.TupleGetItem(func_2419_call(), 0)
call_3407 = relay.TupleGetItem(func_2420_call(), 0)
func_3348_call = mod.get_global_var('func_3348')
func_3352_call = mutated_mod.get_global_var('func_3352')
var_3413 = relay.var("var_3413", dtype = "bool", shape = (88,))#candidate|3413|(88,)|var|bool
var_3414 = relay.var("var_3414", dtype = "uint16", shape = ())#candidate|3414|()|var|uint16
call_3412 = relay.TupleGetItem(func_3348_call(relay.reshape(var_3413.astype('bool'), [2, 44]), relay.reshape(var_3414.astype('uint16'), []), ), 4)
call_3415 = relay.TupleGetItem(func_3352_call(relay.reshape(var_3413.astype('bool'), [2, 44]), relay.reshape(var_3414.astype('uint16'), []), ), 4)
output = relay.Tuple([call_3406,call_3412,var_3413,var_3414,])
output2 = relay.Tuple([call_3407,call_3415,var_3413,var_3414,])
func_3419 = relay.Function([var_3413,var_3414,], output)
mod['func_3419'] = func_3419
mod = relay.transform.InferType()(mod)
var_3420 = relay.var("var_3420", dtype = "bool", shape = (88,))#candidate|3420|(88,)|var|bool
var_3421 = relay.var("var_3421", dtype = "uint16", shape = ())#candidate|3421|()|var|uint16
output = func_3419(var_3420,var_3421,)
func_3422 = relay.Function([var_3420,var_3421,], output)
mutated_mod['func_3422'] = func_3422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_3457 = func_1502_call()
call_3458 = func_1502_call()
func_2165_call = mod.get_global_var('func_2165')
func_2167_call = mutated_mod.get_global_var('func_2167')
const_3467 = relay.const([-8.347834,-5.402327,-6.535837,8.044657,8.903773,1.070557,9.073239,-4.071840,-8.454218,3.506827,1.367471,3.776190,8.233873,-9.050944,0.694518,3.938564,-8.335156,8.184013,4.557453,-6.234484,7.611681,9.874707,4.133431,-0.275288,5.299325,-4.078496,5.887615,1.076817,6.336382,-7.642007,-2.651663,-2.457877,6.585641,4.901296,-4.565693,3.719439,-4.225876,9.064241,-6.448821,3.561567,0.118999,-1.505212,5.817016,2.702916,9.665266,7.222213,5.212058,-3.601939,9.957972,4.025171,1.723650,-4.111999,-5.446763,-4.212754,9.916832,-3.732492,0.198240,5.806979,6.806998,-1.100494,-7.015144,-4.952829,1.352125,-6.586996,-7.865280,6.616018,-3.775760,4.816613,3.773225,-2.745565,1.038469,5.658088,1.996260,-1.744630,0.633760,-9.428599,-0.395890,5.277305,8.377306,6.739765,7.141105,-9.592248,-9.215156,-0.785703,7.453080,-2.346954,-3.666586,7.264853,-0.328250,-0.127825,-4.560689,-7.440660,3.604705,5.035028,8.238236,-6.281077,6.929889,1.437707,9.682568,5.329861,-6.450160,6.603510,4.592466,-6.026060,-0.402762,0.957711,2.937169,-2.128992,9.118889,-0.607381,-2.010380,9.502039,2.476356,7.996260,2.957099,2.161390,-8.261345,-7.865187,5.052054,7.542150,0.265346,2.566536,-7.898913,6.165298,4.723258,9.005826,-6.079972,7.033560,6.197636,-2.938627,1.777524,-4.339326,7.292119,2.300246,2.499512,-1.350807,4.954115,-5.207049,3.579865,5.607328,9.534094,-8.254305,1.663052,3.125119,-0.121161,2.677543,8.628450,0.667463,-9.560117,2.340328,-6.126421,-6.900353,3.185771,8.458217,-1.113925,6.195044,8.412909,-5.431584,3.397700,6.329381,9.708884,4.870893,-9.029209,5.716610,4.135630,3.408904,7.859250,3.658063,-8.187992,5.381507,8.872484,-0.027508,1.143873,-4.508658,-4.688323,-7.352429,-7.968755,-9.871881,4.638843,-4.475876,-9.212352,-1.047150,6.645139,1.275518,-4.095956,9.790895,1.737346,3.223427,-3.571199,-8.151091,6.280652,-7.052039,-0.233079,7.780413,0.752038,8.021160,8.129251,9.198998,2.329451,-2.668229,0.079314,-7.418498,8.055453,3.010558,5.674574,-4.373066,2.082975,-2.966038,7.302817,9.865424,5.852665,-9.834621,-9.728939,-6.190030,-1.731412,5.908608,-8.756589,4.223951,0.312703,8.287115,-5.085239,-0.713600,-9.923662,6.594901,-2.235041,-9.303809,6.355233,-6.556204,-5.335352,-6.176808,7.008462,9.565703,8.197677,2.760058,1.706610,9.033204,-3.994699,4.807790,-9.884410,-1.016706,7.277627,9.827071,9.696391,-3.260483,-0.225203,8.372188,4.715331,7.582557,3.879163,6.714255,5.698728,-0.869113,-4.070542,-5.820810,-8.964095,3.574811,-8.826378,6.444447,-5.147350,4.126290,-7.207475,-0.548867,2.743255,-7.275445,-2.662132,-7.230919,-5.884374,1.324843,-7.190898,6.793446,-1.442192,7.157594,7.940340,4.855069,-2.216910,-3.537816,2.253707,-7.572475,-5.121187,2.247942,3.070660,-3.733163,-4.729806,-4.182202,-6.700376,7.843980,9.314341,9.609318,1.364041,-7.085671,3.494165,-5.410686,-5.765055,-4.922818,1.093128,2.380439,3.800027,-1.509436,-6.683759,-1.446705,4.931630,8.750567,-4.160262,2.799622,7.988379,-2.419379,1.092995,0.806091,5.819087,-1.504220,9.594815,9.849101,-6.678999,-5.471591,7.680868,4.910177,3.595390,4.439462,4.114460,9.976825,-9.110084,8.080433,4.391994,7.801992,-2.569327,6.225872,-0.673862,-1.441103,5.071400,3.489795,-4.707370,6.036656,6.514010,2.231635,1.858873,-7.084529,-9.825515,2.714701,-3.809309,3.941666,1.990025,2.976332,5.192219,-8.830257,-4.753757,4.012615,-6.440860,-5.667702,0.985082,-7.786184,9.088093,3.810676,-7.917633,9.583094,9.530174,-4.697688,6.602271,-2.173474,7.733152,1.385037,-4.642999,-1.421611,2.705616,0.583080,6.292973,-3.172072,-6.838343,-4.078089,-5.920171,7.442979,-8.115582,-2.417680,7.096169,8.003428,8.934439,7.084281,3.432098,-4.686585,-2.404447,-4.798115,9.539367,-0.987787,-8.760783,9.383063,-5.098634,-0.703443,-0.297845,9.414467,-5.642683,-9.764682,3.654622,6.354360,-7.470343,-4.198064,7.228931,-2.026275,5.093983,-8.798871,4.716622,-7.857957,9.318294,9.658844,-8.957410,2.933231,4.340891], dtype = "float32")#candidate|3467|(405,)|const|float32
call_3466 = relay.TupleGetItem(func_2165_call(relay.reshape(const_3467.astype('float32'), [405,])), 2)
call_3468 = relay.TupleGetItem(func_2167_call(relay.reshape(const_3467.astype('float32'), [405,])), 2)
output = relay.Tuple([call_3457,call_3466,const_3467,])
output2 = relay.Tuple([call_3458,call_3468,const_3467,])
func_3480 = relay.Function([], output)
mod['func_3480'] = func_3480
mod = relay.transform.InferType()(mod)
mutated_mod['func_3480'] = func_3480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3480_call = mutated_mod.get_global_var('func_3480')
call_3481 = func_3480_call()
output = call_3481
func_3482 = relay.Function([], output)
mutated_mod['func_3482'] = func_3482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_3497 = relay.TupleGetItem(func_813_call(), 1)
call_3498 = relay.TupleGetItem(func_815_call(), 1)
output = relay.Tuple([call_3497,])
output2 = relay.Tuple([call_3498,])
func_3516 = relay.Function([], output)
mod['func_3516'] = func_3516
mod = relay.transform.InferType()(mod)
mutated_mod['func_3516'] = func_3516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3516_call = mutated_mod.get_global_var('func_3516')
call_3517 = func_3516_call()
output = call_3517
func_3518 = relay.Function([], output)
mutated_mod['func_3518'] = func_3518
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3519 = relay.const(4, dtype = "int16")#candidate|3519|()|const|int16
var_3520 = relay.var("var_3520", dtype = "int16", shape = (9, 3, 16))#candidate|3520|(9, 3, 16)|var|int16
bop_3521 = relay.maximum(const_3519.astype('int16'), var_3520.astype('int16')) # shape=(9, 3, 16)
func_2284_call = mod.get_global_var('func_2284')
func_2292_call = mutated_mod.get_global_var('func_2292')
const_3528 = relay.const([False,True,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False], dtype = "bool")#candidate|3528|(32,)|const|bool
const_3529 = relay.const([False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False], dtype = "bool")#candidate|3529|(64,)|const|bool
var_3530 = relay.var("var_3530", dtype = "uint16", shape = (702,))#candidate|3530|(702,)|var|uint16
const_3531 = relay.const([True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,True], dtype = "bool")#candidate|3531|(528,)|const|bool
var_3532 = relay.var("var_3532", dtype = "float32", shape = (405,))#candidate|3532|(405,)|var|float32
const_3533 = relay.const([0.307717,-7.025651,4.098768,1.769980,-5.487128,9.409719,-4.297875,-7.166772,-6.886687,6.089376,7.152885,5.360249,-9.405246], dtype = "float32")#candidate|3533|(13,)|const|float32
call_3527 = relay.TupleGetItem(func_2284_call(relay.reshape(const_3528.astype('bool'), [4, 8, 1]), relay.reshape(const_3529.astype('bool'), [4, 8, 2]), relay.reshape(var_3530.astype('uint16'), [702,]), relay.reshape(const_3531.astype('bool'), [528,]), relay.reshape(var_3532.astype('float32'), [405,]), relay.reshape(const_3533.astype('float32'), [13,]), ), 1)
call_3534 = relay.TupleGetItem(func_2292_call(relay.reshape(const_3528.astype('bool'), [4, 8, 1]), relay.reshape(const_3529.astype('bool'), [4, 8, 2]), relay.reshape(var_3530.astype('uint16'), [702,]), relay.reshape(const_3531.astype('bool'), [528,]), relay.reshape(var_3532.astype('float32'), [405,]), relay.reshape(const_3533.astype('float32'), [13,]), ), 1)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_3539 = relay.TupleGetItem(func_1717_call(), 1)
call_3540 = relay.TupleGetItem(func_1718_call(), 1)
output = relay.Tuple([bop_3521,call_3527,const_3528,const_3529,var_3530,const_3531,var_3532,const_3533,call_3539,])
output2 = relay.Tuple([bop_3521,call_3534,const_3528,const_3529,var_3530,const_3531,var_3532,const_3533,call_3540,])
func_3559 = relay.Function([var_3520,var_3530,var_3532,], output)
mod['func_3559'] = func_3559
mod = relay.transform.InferType()(mod)
mutated_mod['func_3559'] = func_3559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3559_call = mutated_mod.get_global_var('func_3559')
var_3561 = relay.var("var_3561", dtype = "int16", shape = (9, 3, 16))#candidate|3561|(9, 3, 16)|var|int16
var_3562 = relay.var("var_3562", dtype = "uint16", shape = (702,))#candidate|3562|(702,)|var|uint16
var_3563 = relay.var("var_3563", dtype = "float32", shape = (405,))#candidate|3563|(405,)|var|float32
call_3560 = func_3559_call(var_3561,var_3562,var_3563,)
output = call_3560
func_3564 = relay.Function([var_3561,var_3562,var_3563,], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3592 = relay.const([[[3,-2,-5,-9],[-7,-2,-3,1],[-2,9,-6,1],[-4,-6,-7,8],[-10,-4,-1,-3],[-2,-7,4,3],[4,9,2,8],[10,-6,-6,6],[-7,3,5,-6],[-1,-4,-1,-2],[-8,-7,-10,-8],[-10,-1,9,4],[-10,-3,3,4],[4,-8,4,2],[-2,4,-3,-4],[9,3,5,-3]],[[4,-1,-9,10],[2,10,9,-10],[10,-3,-8,-10],[-4,-4,-10,-3],[-5,3,1,7],[3,-1,-1,3],[5,-6,3,-10],[9,-6,-9,7],[-5,-9,-6,-2],[-4,-1,-4,-8],[-10,-1,-2,-10],[5,2,-8,9],[9,-2,4,4],[-4,5,-9,6],[7,4,10,-10],[1,8,-1,5]],[[-3,-5,-8,7],[5,-2,4,6],[7,9,-4,-10],[-1,6,-5,1],[5,-7,6,7],[-5,-6,6,8],[-1,-9,-8,-2],[9,-10,-9,4],[-9,-9,6,-4],[4,10,3,-1],[9,-1,-3,5],[-1,8,-7,5],[7,1,-9,-4],[7,3,4,-6],[8,-9,2,-4],[-10,-2,7,3]],[[1,-7,10,-5],[7,-1,-4,5],[6,-2,7,-1],[8,-6,-1,1],[4,4,9,-3],[7,-1,-10,-2],[10,5,2,6],[9,7,10,4],[5,-8,-7,-5],[4,7,2,-2],[-5,-10,1,9],[8,10,5,2],[3,-8,-2,7],[9,-1,3,-1],[-8,-7,9,-1],[-5,6,4,-2]],[[9,-7,3,8],[8,-2,1,-1],[-6,-2,-6,1],[3,-1,-5,-3],[-3,5,6,9],[-3,9,2,-6],[10,-3,-8,-8],[-2,-7,-4,-3],[-5,-4,-4,-7],[1,2,5,6],[-4,2,5,-5],[10,6,-4,-2],[7,-10,-8,7],[-4,-7,-7,-6],[1,-6,-1,3],[-3,-7,8,-6]],[[5,8,-4,7],[6,-8,-6,-5],[-4,3,-2,-9],[7,-3,-5,-2],[6,6,-6,1],[8,6,-6,2],[4,7,4,-4],[-10,-6,8,7],[-7,-6,-7,-7],[-8,10,-6,4],[-2,9,-7,-6],[9,-3,-9,3],[-5,-9,7,9],[10,7,-6,7],[4,-3,-10,9],[1,8,-4,4]],[[-1,-2,-10,2],[-2,8,-4,5],[3,-10,-5,4],[-2,-3,-5,-6],[3,-5,-10,-3],[-9,-2,7,10],[5,3,-10,-7],[-1,-1,-9,-3],[6,7,4,-2],[-2,6,4,-7],[6,1,9,10],[-8,4,-7,-2],[-4,3,-9,-1],[-1,-8,10,4],[-7,4,2,-6],[5,10,7,-7]],[[2,-9,6,4],[6,2,9,-4],[2,-4,1,7],[-10,-10,-2,9],[8,5,-7,-9],[10,9,-7,8],[2,-6,-2,1],[-1,-10,-9,-4],[-5,10,9,5],[3,1,-8,1],[-10,2,-9,3],[-5,2,-10,-2],[-7,-8,-6,-6],[-10,10,5,-7],[10,7,4,9],[3,-3,8,-9]],[[-10,1,-2,4],[3,10,-7,5],[6,-7,3,10],[-7,-8,-10,2],[-6,5,-10,-9],[-5,5,4,9],[3,10,2,-4],[5,-8,9,-5],[2,2,-1,7],[2,7,-1,7],[4,1,-7,7],[-7,7,4,2],[3,8,-6,9],[-6,-3,-5,-4],[-8,-5,10,-9],[8,4,9,7]],[[-9,-6,-9,-3],[3,3,-6,7],[2,1,7,-8],[5,6,-9,5],[-8,-4,-8,-2],[-5,-9,2,7],[9,3,-9,8],[6,-9,8,4],[7,-3,-7,3],[9,-4,-7,2],[-10,-9,-9,-2],[-2,-9,-5,4],[-1,4,-1,-9],[-9,3,6,2],[-2,3,-8,8],[6,-10,-2,-2]],[[3,-2,-2,-7],[6,9,-5,7],[1,-3,-5,-1],[-10,-1,-7,-7],[8,9,2,3],[5,-9,-2,-2],[-6,-2,-5,1],[5,-2,-2,7],[8,-2,-1,10],[8,10,8,2],[6,5,8,1],[-6,10,-1,10],[2,-2,8,10],[-3,-3,-2,-5],[1,-10,-3,-4],[3,9,-10,3]],[[-2,4,-9,5],[5,-5,4,-5],[-9,4,5,3],[10,2,-2,2],[2,-3,10,-4],[-5,-2,-8,-4],[4,-9,3,-9],[-5,-5,-5,-8],[-2,-9,8,-7],[-10,-1,-8,5],[2,10,-7,10],[-9,-8,1,3],[-8,6,-6,8],[6,4,4,-7],[-5,-2,6,-4],[-9,1,-10,-3]],[[-7,-2,-6,8],[-10,5,4,-8],[8,3,4,-1],[2,2,6,-10],[-6,5,3,-3],[6,6,-9,8],[6,5,9,-10],[-10,2,-10,9],[5,8,-7,-2],[9,2,-4,-9],[-10,-8,-10,1],[-3,-6,-5,8],[10,9,-9,10],[-9,-7,-1,-3],[9,-3,2,-9],[-6,9,-9,-3]]], dtype = "int8")#candidate|3592|(13, 16, 4)|const|int8
const_3593 = relay.const([[[-2,5,4,1],[1,-7,-7,8],[-2,-2,6,1],[7,7,-6,3],[10,1,-1,1],[6,-3,-8,5],[-7,-4,-5,2],[-9,-9,6,4],[-1,3,7,-6],[-3,-8,-9,-2],[9,1,10,-8],[-4,3,-1,7],[2,-6,5,2],[10,-10,10,-5],[-7,3,-2,8],[9,6,-8,2]],[[5,7,-9,-10],[8,9,-4,-8],[-1,-10,-1,-8],[10,10,9,8],[-1,5,-5,-2],[5,-10,6,-1],[9,9,-10,10],[-1,7,-6,5],[1,1,5,6],[5,-10,-4,-7],[2,2,-2,-3],[-7,-6,-5,-4],[1,2,-1,7],[-4,4,-7,10],[-8,3,-9,5],[-7,10,-2,-8]],[[-10,-10,-9,-6],[1,3,-2,7],[-7,9,7,3],[7,-5,8,3],[-6,-8,9,9],[3,-9,-7,4],[-9,2,-9,1],[8,4,-1,-3],[-1,5,-6,-3],[8,-5,-10,-1],[-2,-6,-9,4],[5,1,-6,-7],[7,6,-8,-4],[2,-3,8,3],[10,10,6,-5],[3,-9,2,5]],[[-5,5,-1,2],[-6,-6,-1,-6],[-8,-10,-2,7],[3,-6,9,-8],[-6,10,2,1],[-6,-4,-5,10],[7,-10,-5,4],[-3,4,-4,8],[5,-7,1,5],[-6,6,7,5],[-6,-3,-1,8],[1,-8,2,5],[8,-4,-2,8],[-8,-9,10,9],[8,6,2,5],[-4,8,-1,-5]],[[7,-5,6,8],[8,9,1,6],[3,-1,6,8],[-9,9,-1,8],[-4,8,-6,6],[-4,-6,4,-4],[-3,-3,3,2],[8,-3,-6,9],[-3,9,-3,-5],[-1,-2,2,3],[-3,8,-8,7],[2,6,-10,-7],[4,-2,3,4],[8,-9,1,8],[8,1,6,3],[9,-5,6,2]],[[10,-7,-1,6],[-6,-2,7,-3],[7,3,2,-9],[-7,8,8,3],[3,-8,-10,6],[9,3,1,1],[9,-9,-9,-10],[5,-2,-9,1],[-5,-8,3,-1],[5,8,-1,2],[-2,9,-1,8],[10,-1,4,-10],[-10,4,-4,6],[10,-5,-3,-8],[-10,-4,9,-9],[3,7,1,-6]],[[8,4,6,3],[-4,-6,-5,-9],[3,-8,-7,-9],[-8,-8,4,9],[4,5,-3,-6],[7,3,-6,9],[-8,-2,-3,-7],[-7,-9,7,-4],[1,-2,6,-1],[-10,6,-9,-3],[-1,1,-6,-4],[-3,6,1,2],[-9,-6,2,9],[4,-6,-10,9],[6,5,8,8],[2,-3,6,-5]],[[-2,4,-8,6],[8,-4,-4,2],[-3,-3,8,-4],[9,-5,5,-2],[1,-10,8,-1],[-7,9,-8,-1],[-7,3,10,-6],[-5,4,1,4],[1,-10,-10,-9],[8,8,8,6],[-6,3,-6,-4],[9,10,3,1],[8,5,4,4],[-4,7,-2,9],[2,5,-10,1],[-5,1,-7,-2]],[[-6,4,2,10],[-10,10,-10,1],[3,-1,3,4],[5,7,-10,8],[7,3,-9,7],[-10,1,-10,-3],[6,-5,10,-6],[5,-8,2,8],[-7,1,6,3],[-9,-7,5,-9],[5,-10,5,9],[-1,4,2,-5],[5,-5,5,10],[-2,-10,-8,-10],[7,8,-9,-2],[6,6,-10,-9]],[[8,-7,-3,7],[-3,-6,10,-5],[-9,-6,2,1],[-4,9,9,-10],[-5,-1,5,6],[7,-10,-8,-3],[-8,5,9,-1],[2,-8,10,-9],[-4,-3,-10,-6],[1,-5,10,7],[-9,9,8,-10],[10,3,-3,-6],[7,-5,-8,-6],[-6,1,-9,4],[-1,-3,-3,-3],[-10,-6,1,1]],[[1,4,8,10],[1,1,-10,-7],[10,-1,-6,7],[-1,10,-4,9],[-8,7,-3,1],[10,5,9,-2],[5,-3,10,-6],[4,4,-6,5],[7,1,1,-5],[5,3,-3,4],[-10,6,8,2],[5,-10,-10,6],[-7,9,-10,10],[-6,9,10,5],[10,-2,3,-8],[10,3,3,7]],[[-8,-7,-1,-2],[-10,6,6,-1],[-5,5,-5,-8],[3,2,1,-5],[6,-7,-8,5],[10,7,-3,4],[-1,5,4,-10],[-7,4,-4,6],[10,8,-2,6],[-4,-10,3,-6],[3,-8,-7,3],[-3,-1,-5,-8],[2,-10,8,-8],[1,1,2,-6],[-1,1,5,1],[10,-4,10,-7]],[[-7,-7,-5,9],[-5,-7,2,-1],[8,-8,-5,-10],[2,9,7,4],[-6,-2,6,-4],[4,7,5,-8],[9,7,-6,2],[-4,-7,8,6],[2,5,-9,-10],[-10,-10,6,-9],[3,-2,4,6],[4,8,5,-6],[-10,-7,-9,4],[6,6,2,-9],[-3,4,3,-5],[3,9,-7,-7]]], dtype = "int8")#candidate|3593|(13, 16, 4)|const|int8
bop_3594 = relay.greater_equal(const_3592.astype('bool'), relay.reshape(const_3593.astype('bool'), relay.shape_of(const_3592))) # shape=(13, 16, 4)
output = relay.Tuple([bop_3594,])
output2 = relay.Tuple([bop_3594,])
func_3597 = relay.Function([], output)
mod['func_3597'] = func_3597
mod = relay.transform.InferType()(mod)
mutated_mod['func_3597'] = func_3597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3597_call = mutated_mod.get_global_var('func_3597')
call_3598 = func_3597_call()
output = call_3598
func_3599 = relay.Function([], output)
mutated_mod['func_3599'] = func_3599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3597_call = mod.get_global_var('func_3597')
func_3599_call = mutated_mod.get_global_var('func_3599')
call_3622 = relay.TupleGetItem(func_3597_call(), 0)
call_3623 = relay.TupleGetItem(func_3599_call(), 0)
var_3626 = relay.var("var_3626", dtype = "bool", shape = (13, 16, 4))#candidate|3626|(13, 16, 4)|var|bool
bop_3627 = relay.subtract(call_3622.astype('uint64'), relay.reshape(var_3626.astype('uint64'), relay.shape_of(call_3622))) # shape=(13, 16, 4)
bop_3630 = relay.subtract(call_3623.astype('uint64'), relay.reshape(var_3626.astype('uint64'), relay.shape_of(call_3623))) # shape=(13, 16, 4)
output = relay.Tuple([bop_3627,])
output2 = relay.Tuple([bop_3630,])
func_3631 = relay.Function([var_3626,], output)
mod['func_3631'] = func_3631
mod = relay.transform.InferType()(mod)
var_3632 = relay.var("var_3632", dtype = "bool", shape = (13, 16, 4))#candidate|3632|(13, 16, 4)|var|bool
output = func_3631(var_3632)
func_3633 = relay.Function([var_3632], output)
mutated_mod['func_3633'] = func_3633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_3652 = relay.TupleGetItem(func_680_call(), 0)
call_3653 = relay.TupleGetItem(func_682_call(), 0)
var_3655 = relay.var("var_3655", dtype = "float32", shape = (15, 3, 9))#candidate|3655|(15, 3, 9)|var|float32
bop_3656 = relay.bitwise_or(call_3652.astype('int8'), relay.reshape(var_3655.astype('int8'), relay.shape_of(call_3652))) # shape=(15, 3, 9)
bop_3659 = relay.bitwise_or(call_3653.astype('int8'), relay.reshape(var_3655.astype('int8'), relay.shape_of(call_3653))) # shape=(15, 3, 9)
bop_3664 = relay.maximum(bop_3656.astype('float32'), relay.reshape(var_3655.astype('float32'), relay.shape_of(bop_3656))) # shape=(15, 3, 9)
bop_3667 = relay.maximum(bop_3659.astype('float32'), relay.reshape(var_3655.astype('float32'), relay.shape_of(bop_3659))) # shape=(15, 3, 9)
func_2987_call = mod.get_global_var('func_2987')
func_2991_call = mutated_mod.get_global_var('func_2991')
const_3685 = relay.const([[10,-6],[6,3],[5,-8],[4,-9],[3,4],[6,-10],[-3,5],[-10,7],[-6,8],[-6,5],[4,10],[9,4],[7,-8],[7,1],[6,4],[-5,-7],[-2,5],[3,-3],[5,-7],[-5,6],[1,6],[-9,-2],[3,2],[-4,10],[-1,8],[-5,3],[4,-2],[-4,-10],[10,5],[-5,6],[-2,7],[-7,-6],[2,-4],[-2,-4],[-8,-5],[7,-7]], dtype = "uint16")#candidate|3685|(36, 2)|const|uint16
call_3684 = relay.TupleGetItem(func_2987_call(relay.reshape(const_3685.astype('uint16'), [72,]), relay.reshape(bop_3656.astype('float64'), [405,]), ), 4)
call_3686 = relay.TupleGetItem(func_2991_call(relay.reshape(const_3685.astype('uint16'), [72,]), relay.reshape(bop_3656.astype('float64'), [405,]), ), 4)
uop_3691 = relay.sigmoid(const_3685.astype('float64')) # shape=(36, 2)
uop_3693 = relay.erf(const_3685.astype('float32')) # shape=(36, 2)
uop_3700 = relay.sin(uop_3691.astype('float64')) # shape=(36, 2)
func_2284_call = mod.get_global_var('func_2284')
func_2292_call = mutated_mod.get_global_var('func_2292')
var_3708 = relay.var("var_3708", dtype = "bool", shape = (1, 32))#candidate|3708|(1, 32)|var|bool
const_3709 = relay.const([[False,False,True,False,True,True,True,True,False,True,True,True,False,True,False,True],[True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False],[True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False],[True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False]], dtype = "bool")#candidate|3709|(4, 16)|const|bool
const_3710 = relay.const([9,8,-3,-8,-6,10,6,-1,2,6,-9,6,-4,-5,-8,10,6,-9,-8,9,5,1,7,-2,7,2,4,7,-1,-4,7,-8,-3,-3,1,-4,-5,-10,9,3,9,-2,-3,10,1,3,-7,10,-8,-2,9,7,-2,-8,10,-9,-9,3,-1,-6,-8,-8,-1,-6,5,8,-3,10,4,8,-1,3,9,-2,1,-1,-10,-4,9,-2,8,-10,4,6,-8,-4,-1,-9,-4,-1,8,2,2,10,7,-8,1,8,8,5,-10,4,-5,4,-1,-2,6,8,-3,-9,-8,7,-5,-5,9,-8,9,10,3,1,8,5,-9,-2,-1,3,10,-9,5,7,-5,2,-4,-6,-8,-1,2,2,8,4,-5,-9,4,-9,5,2,-10,2,9,-1,6,-3,7,-10,9,6,-8,10,-6,-3,-6,9,-1,8,-10,7,2,-6,5,-5,9,-10,-8,-3,9,3,10,9,-4,1,7,-2,6,-7,-6,-5,6,4,-6,-8,2,10,5,3,-10,5,-10,8,7,-9,10,7,-1,-1,9,-2,3,3,3,9,-10,-1,-1,8,-4,10,3,1,-2,1,-2,-2,-6,2,3,-3,4,-7,4,-5,-4,-4,4,-3,6,8,10,2,7,5,5,-4,3,6,-7,-8,5,2,-7,-6,2,2,3,5,-8,-9,10,2,5,3,-8,-4,2,4,2,4,-3,-5,-8,6,3,-9,-9,8,-8,7,-1,10,-1,-5,-4,7,5,6,2,-1,7,8,10,1,7,5,3,3,2,6,-9,7,-5,-9,-5,10,8,-10,-3,8,3,10,-3,-9,-5,2,8,-7,-10,-9,-5,-9,-8,5,1,3,-9,9,10,-6,5,-8,-5,7,1,2,-7,-3,9,-6,1,4,6,9,-5,10,3,6,-3,5,9,2,-10,10,-10,2,8,1,-3,-10,5,10,-8,-8,-9,6,2,-3,2,-4,10,6,-1,-3,-7,-3,-5,-2,7,-5,-5,-4,9,-1,-1,-3,-10,10,-6,-6,-6,-7,1,-3,1,7,-8,-5,10,-8,-1,-3,-10,2,6,10,8,2,-9,10,-2,8,-9,5,-8,-2,3,-10,8,2,-2,7,-2,-9,-3,-2,5,-3,4,-6,2,-3,-3,10,5,-7,-4,6,3,-6,-4,1,10,-8,5,-7,1,-2,3,8,-3,6,1,-3,9,3,10,5,-2,-4,-6,-4,3,3,-7,5,-6,-9,-4,3,4,7,2,5,4,10,4,-8,9,2,-2,8,-7,5,9,-3,6,8,1,-1,-5,-6,5,6,7,10,3,5,4,1,2,8,-5,5,4,-2,8,-9,-4,-9,-1,10,8,5,-7,-7,2,8,-6,3,10,-8,-5,-5,10,-10,4,6,-5,-4,-7,3,8,7,4,-3,-3,-5,8,7,-4,10,9,10,8,8,6,-7,5,-10,3,-5,4,7,2,1,-3,3,-8,-7,8,-4,-1,1,-4,-6,4,-3,5,-10,4,-2,2,-10,-10,-7,-4,-3,1,-2,-4,-1,-4,-7,-4,6,8,-8,3,3,5,-2,-10,-6,10,7,8,4,-2,-9,-10,8,-4,8,-4,-3,-10,2,1,-2,-5,6,-7,-5,3,-7,10,-1,-4,2,-2,9,-9,4,6,-10,5,6,6,2,7,2,-7,-4,4,8,-2,-9,-5,-10,1,6,5,9,-5,-3,-10,-2,10,9,1,-1,4,3,-5,2,2,-1,10,-8,-10,-7,-6,9,-4,-9,6,9,9,9,6,7,9,-5,-7,6,-4,8,-4,5,5,-7,3,1,8,6,-3,-2,-5,3,-9,-1,-6,2,-6,-9,10,-4,-2,5,-4,5,-7,10,-3,-4], dtype = "uint16")#candidate|3710|(702,)|const|uint16
var_3711 = relay.var("var_3711", dtype = "bool", shape = (528,))#candidate|3711|(528,)|var|bool
const_3712 = relay.const([9.409482,0.603486,8.413963,-2.422159,9.442889,-0.194450,-0.454054,-9.461892,6.322476,8.822443,0.354776,-3.352041,4.727031], dtype = "float32")#candidate|3712|(13,)|const|float32
call_3707 = relay.TupleGetItem(func_2284_call(relay.reshape(var_3708.astype('bool'), [4, 8, 1]), relay.reshape(const_3709.astype('bool'), [4, 8, 2]), relay.reshape(const_3710.astype('uint16'), [702,]), relay.reshape(var_3711.astype('bool'), [528,]), relay.reshape(bop_3656.astype('float32'), [405,]), relay.reshape(const_3712.astype('float32'), [13,]), ), 1)
call_3713 = relay.TupleGetItem(func_2292_call(relay.reshape(var_3708.astype('bool'), [4, 8, 1]), relay.reshape(const_3709.astype('bool'), [4, 8, 2]), relay.reshape(const_3710.astype('uint16'), [702,]), relay.reshape(var_3711.astype('bool'), [528,]), relay.reshape(bop_3656.astype('float32'), [405,]), relay.reshape(const_3712.astype('float32'), [13,]), ), 1)
output = relay.Tuple([bop_3664,call_3684,uop_3693,uop_3700,call_3707,var_3708,const_3709,const_3710,var_3711,const_3712,])
output2 = relay.Tuple([bop_3667,call_3686,uop_3693,uop_3700,call_3713,var_3708,const_3709,const_3710,var_3711,const_3712,])
func_3723 = relay.Function([var_3655,var_3708,var_3711,], output)
mod['func_3723'] = func_3723
mod = relay.transform.InferType()(mod)
mutated_mod['func_3723'] = func_3723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3723_call = mutated_mod.get_global_var('func_3723')
var_3725 = relay.var("var_3725", dtype = "float32", shape = (15, 3, 9))#candidate|3725|(15, 3, 9)|var|float32
var_3726 = relay.var("var_3726", dtype = "bool", shape = (1, 32))#candidate|3726|(1, 32)|var|bool
var_3727 = relay.var("var_3727", dtype = "bool", shape = (528,))#candidate|3727|(528,)|var|bool
call_3724 = func_3723_call(var_3725,var_3726,var_3727,)
output = call_3724
func_3728 = relay.Function([var_3725,var_3726,var_3727,], output)
mutated_mod['func_3728'] = func_3728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_3784 = func_1502_call()
call_3785 = func_1502_call()
output = relay.Tuple([call_3784,])
output2 = relay.Tuple([call_3785,])
func_3808 = relay.Function([], output)
mod['func_3808'] = func_3808
mod = relay.transform.InferType()(mod)
mutated_mod['func_3808'] = func_3808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3808_call = mutated_mod.get_global_var('func_3808')
call_3809 = func_3808_call()
output = call_3809
func_3810 = relay.Function([], output)
mutated_mod['func_3810'] = func_3810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_3811 = relay.TupleGetItem(func_988_call(), 1)
call_3812 = relay.TupleGetItem(func_990_call(), 1)
func_1218_call = mod.get_global_var('func_1218')
func_1225_call = mutated_mod.get_global_var('func_1225')
var_3814 = relay.var("var_3814", dtype = "uint16", shape = (702,))#candidate|3814|(702,)|var|uint16
const_3815 = relay.const([4.316639,-1.805511,-7.719771,-5.300465,2.854306,-8.054888,1.683692,6.196265,7.353925,-0.341128,-4.727240,-3.549598,-6.215142,5.066826,1.510889,-0.485831,5.886527,-8.005603,1.510509,4.343358,6.858507,4.832681,-5.012168,-1.249867,-6.072502,-5.388573,0.673066,-2.157079,9.018081,8.471600,2.607552,0.347134,-8.794679,0.236619,-3.896807,8.473475,-6.520328,8.514545,2.490717,-3.433941,-4.483028,-4.869965,5.096816,8.824625,-1.454848,-9.780204,8.897473,-0.395450,1.503325,6.630984,-5.774948,4.947978,-0.667099,2.391509,-4.707002,2.909460,-8.504763,-7.597204,-7.915331,-1.300041,-3.291326,5.766981,-1.779208,2.205945,2.757683,-8.079787,1.183029,-7.845322,-4.601777,1.013382,8.867733,5.654425,-6.630219,0.546504,4.007608,-3.152108,-1.477254,4.912833,6.903094,-1.583523,-8.332584,2.346993,-8.502264,5.192006,5.646580,1.843591,8.762210,2.094401,-5.116700,4.710347,-9.427755,0.117737,4.849377,-8.063323,-3.968827,0.913549,8.621116,-1.467519,-4.399427,-5.328926,0.210279,-3.594893,-1.483536,-3.939148,-1.609977,-8.637567,9.139391,-3.947316,9.633328,-1.907928,9.081582,-1.177129,-9.622802,1.325958,-8.728432,-8.323529,3.706572,-7.973786,-8.691022,1.295337,-1.385191,-6.948283,4.708594,-4.096591,7.080141,-7.359817,-2.401738,5.665749,-2.571622,5.528778,-0.976900,-3.798841,-2.827180,5.721447,7.818759,-9.286754,-2.914167,-8.240790,0.722540,-4.026915,7.441786,9.843178,4.990783,-6.902808,2.429467,-8.577061,7.039546,-6.235941,-7.459358,3.863304,-9.102045,8.671891,-9.879404,-9.753113,2.927876,-4.363646,-3.238777,-9.043730,-2.845783,4.925097,4.918546,1.638190,-1.494257,-0.294958,8.378795,-8.232302,7.501464,-2.282037,1.249900,9.696942,-0.439361,1.707602,-8.382651,-2.020558,-3.654620,-4.442429,-3.100460,7.339512,9.194897,1.459781,5.091743,-3.275337,4.054453,-3.152306,-0.505355,0.430802,7.598543,0.030021,5.177321,-5.444149,1.001765,4.221170,-8.232352,-7.542421,-8.763135,-2.827574,9.509578,9.501215,3.611407,-8.541469,6.529294,-4.905830,-5.351121,-1.941791,-1.687031,-0.727901,-9.924129,2.148313,-0.663273,-1.924917,6.255591,-4.266487,-2.141631,4.107263,3.927898,9.523196,-1.252048,6.466411,8.951371,-6.717129,-6.470192,8.844386,-5.254188,0.624667,-4.325664,0.994767,-1.039681,-0.852033,8.270774,-7.550474,2.867955,-7.637806,-0.364041,1.401884,2.632193,5.668790,-8.644433,-1.860302,6.908776,7.906647,-6.768724,0.450458,-2.782137,9.831325,9.153748,-1.126358,6.807617,-6.684734,-7.675953,4.625309,5.325653,8.114864,2.333800,-5.644444,1.925592,-9.613590,5.564635,-2.251759,6.981816,3.840951,1.462275,-7.036897,-3.004597,-4.727137,-3.484666,5.212215,-8.529528,3.288820,-1.127766,-0.978578,8.173047,1.498401,-5.000759,-9.627591,1.857298,0.202776,2.086761,4.723396,-9.686303,-4.784110,4.693346,9.459065,-0.802900,6.354056,-8.850690,-7.449014,-0.144197,-4.064962,9.235378,2.762654,1.177751,7.960437,-7.430103,-6.531401,6.739911,9.771657,-2.126522,-9.051222,2.638961,-0.036570,-3.390939,0.608117,-4.014856,7.032338,-7.597743,4.223313,6.314407,-0.565943,0.583464,0.218078,7.190831,-4.661490,4.191144,-3.926629,-1.006647,-8.520892,8.515958,-3.254063,-0.141869,5.164816,-8.398745,-3.004654,2.135960,4.772109,0.318206,8.210911,4.058536,1.767614,8.845494,7.800125,-9.098053,-9.207578,1.404635,7.787942,-0.832731,-7.850386,1.817988,0.021854,2.650984,-3.883746,8.753518,8.784926,3.760517,7.863613,-1.775406,-7.085858,-3.815502,-4.934230,4.972731,3.759719,-1.092946,-4.599838,-3.830763,-5.664044,-5.227355,2.787815,7.416508,-6.378886,1.279898,0.410996,-7.452027,-9.327678,-2.770144,-9.533002,-6.591520,4.607107,4.413484,2.186006,6.489094,0.374839,-7.977311,5.757145,8.014594,-7.726984,9.491820,-2.815810,0.501832,5.607023,0.853006,-7.785811,1.299870,-6.515994,9.626645,4.643771,-9.862598,2.259423,8.347992,-3.213919,-8.329101,6.663892,-8.557056,-8.344907,-7.817693,9.254454,1.892158,5.145882,3.527730,-8.120297,6.633285,-3.429164,-8.288057,-0.512200,-0.022721,4.035708,3.066444], dtype = "float32")#candidate|3815|(405,)|const|float32
const_3816 = relay.const([[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False]], dtype = "bool")#candidate|3816|(88, 1)|const|bool
var_3817 = relay.var("var_3817", dtype = "float32", shape = (1, 13))#candidate|3817|(1, 13)|var|float32
call_3813 = relay.TupleGetItem(func_1218_call(relay.reshape(var_3814.astype('uint16'), [1, 702]), relay.reshape(call_3811.astype('bool'), [6, 8, 11]), relay.reshape(const_3815.astype('float32'), [405,]), relay.reshape(const_3816.astype('bool'), [88,]), relay.reshape(var_3817.astype('float32'), [13,]), ), 4)
call_3818 = relay.TupleGetItem(func_1225_call(relay.reshape(var_3814.astype('uint16'), [1, 702]), relay.reshape(call_3811.astype('bool'), [6, 8, 11]), relay.reshape(const_3815.astype('float32'), [405,]), relay.reshape(const_3816.astype('bool'), [88,]), relay.reshape(var_3817.astype('float32'), [13,]), ), 4)
func_743_call = mod.get_global_var('func_743')
func_746_call = mutated_mod.get_global_var('func_746')
call_3820 = relay.TupleGetItem(func_743_call(relay.reshape(const_3815.astype('float32'), [15, 3, 9])), 5)
call_3821 = relay.TupleGetItem(func_746_call(relay.reshape(const_3815.astype('float32'), [15, 3, 9])), 5)
output = relay.Tuple([call_3811,call_3813,var_3814,const_3815,const_3816,var_3817,call_3820,])
output2 = relay.Tuple([call_3812,call_3818,var_3814,const_3815,const_3816,var_3817,call_3821,])
func_3825 = relay.Function([var_3814,var_3817,], output)
mod['func_3825'] = func_3825
mod = relay.transform.InferType()(mod)
mutated_mod['func_3825'] = func_3825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3825_call = mutated_mod.get_global_var('func_3825')
var_3827 = relay.var("var_3827", dtype = "uint16", shape = (702,))#candidate|3827|(702,)|var|uint16
var_3828 = relay.var("var_3828", dtype = "float32", shape = (1, 13))#candidate|3828|(1, 13)|var|float32
call_3826 = func_3825_call(var_3827,var_3828,)
output = call_3826
func_3829 = relay.Function([var_3827,var_3828,], output)
mutated_mod['func_3829'] = func_3829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1729_call = mod.get_global_var('func_1729')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_3845 = relay.TupleGetItem(func_1729_call(), 0)
call_3846 = relay.TupleGetItem(func_1730_call(), 0)
uop_3848 = relay.log10(call_3845.astype('float32')) # shape=(6, 8, 11)
uop_3850 = relay.log10(call_3846.astype('float32')) # shape=(6, 8, 11)
output = uop_3848
output2 = uop_3850
func_3856 = relay.Function([], output)
mod['func_3856'] = func_3856
mod = relay.transform.InferType()(mod)
mutated_mod['func_3856'] = func_3856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3856_call = mutated_mod.get_global_var('func_3856')
call_3857 = func_3856_call()
output = call_3857
func_3858 = relay.Function([], output)
mutated_mod['func_3858'] = func_3858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_3943 = func_1291_call()
call_3944 = func_1291_call()
func_2419_call = mod.get_global_var('func_2419')
func_2420_call = mutated_mod.get_global_var('func_2420')
call_3947 = relay.TupleGetItem(func_2419_call(), 0)
call_3948 = relay.TupleGetItem(func_2420_call(), 0)
output = relay.Tuple([call_3943,call_3947,])
output2 = relay.Tuple([call_3944,call_3948,])
func_3951 = relay.Function([], output)
mod['func_3951'] = func_3951
mod = relay.transform.InferType()(mod)
mutated_mod['func_3951'] = func_3951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3951_call = mutated_mod.get_global_var('func_3951')
call_3952 = func_3951_call()
output = call_3952
func_3953 = relay.Function([], output)
mutated_mod['func_3953'] = func_3953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_3958 = func_1502_call()
call_3959 = func_1502_call()
output = relay.Tuple([call_3958,])
output2 = relay.Tuple([call_3959,])
func_3967 = relay.Function([], output)
mod['func_3967'] = func_3967
mod = relay.transform.InferType()(mod)
mutated_mod['func_3967'] = func_3967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3967_call = mutated_mod.get_global_var('func_3967')
call_3968 = func_3967_call()
output = call_3968
func_3969 = relay.Function([], output)
mutated_mod['func_3969'] = func_3969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1123_call = mod.get_global_var('func_1123')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_3981 = relay.TupleGetItem(func_1123_call(), 0)
call_3982 = relay.TupleGetItem(func_1125_call(), 0)
output = call_3981
output2 = call_3982
func_4028 = relay.Function([], output)
mod['func_4028'] = func_4028
mod = relay.transform.InferType()(mod)
output = func_4028()
func_4029 = relay.Function([], output)
mutated_mod['func_4029'] = func_4029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_4036 = relay.TupleGetItem(func_2777_call(), 0)
call_4037 = relay.TupleGetItem(func_2778_call(), 0)
func_1833_call = mod.get_global_var('func_1833')
func_1837_call = mutated_mod.get_global_var('func_1837')
const_4039 = relay.const([-1.829977,1.964488,6.152588,6.689815,-7.923819,-4.998415,-8.005934,-1.207643,9.333116,5.580278,5.002789,-8.345184,-7.144756,-9.378993,-8.195817,-8.469208,2.867863,7.079099,1.962502,7.307113,-1.878411,3.200730,-9.097513,-0.383279,-9.540428,-2.948657,0.156364,-3.464617,7.505196,7.280222,-3.208776,-2.044367,5.914115,-0.451908,-5.082846,9.443656,9.185519,6.635443,-6.415183,4.718547,-6.672850,-6.889172,6.637667,9.807189,-5.684324,-4.197362,7.179917,-7.533068,-6.578987,9.806530,-9.034018,-8.465151,6.771785,2.755283,6.283039,0.456507,6.681288,8.889444,-1.624820,0.045259,-6.963005,2.530193,3.139180,-7.832036,-0.780492,-9.461912,-5.351762,-0.579128,4.836828,5.115886,-0.261642,-7.594983,9.115085,-4.209706,-8.344659,-1.271974,8.517759,-6.480625,5.390618,3.065563,5.344445,5.754871,-1.994464,0.911737,2.984635,-1.036225,6.753696,9.265463,-3.649697,-7.314823,-3.865261,1.270061,-5.720809,-3.994363,0.742704,3.145136,2.988940,-9.040657,-0.014119,5.477451,2.084492,-7.150661,-7.973209,5.796077,3.273718,-5.641356,-4.927712,-6.480965,2.783849,-5.287357,-0.666278,3.135056,-0.822043,3.232200,-0.167472,1.659725,-8.117806,-4.546362,4.339018,1.347304,-9.435485,-6.177578,-4.606543,2.866559,4.049610,-0.246072,-6.251393,-6.708967,9.470766,5.471684,-7.690874,4.624570,-0.252669,-7.177312,1.668407,9.102421,4.787290,-0.815441,-5.869251,0.006999,-9.129473,2.850423,-8.221142,6.266321,6.838946,4.579401,5.776012,-1.897567,-9.282292,-1.397425,-6.145465,1.636041,2.078828,2.839121,-5.428658,-9.191304,-1.547321,0.155094,9.705904,3.467641,8.554797,-4.946123,4.633393,9.743665,2.992414,-1.032314,1.147127,4.392100,7.939650,-4.159968,-3.851658,-3.187523,-1.560728,1.322355,8.708932,-8.205220,9.074617,3.158355,4.393001,-9.812118,-4.864062,-4.420644,2.717771,2.221702,6.692294,-9.565210,-0.651855,-9.739490,-3.423532,-4.331510,-0.594876,-6.635237,0.396294,5.021589,-6.310695,-2.585036,-3.623828,-2.160469,-9.516902,-4.273160,4.819025,4.538775,-7.976981,-2.862019,1.211750,-8.023404,7.101334,3.840409,-0.106579,2.328823,1.991740,-6.697520,3.639578,3.089646,-6.920530,6.965763,-0.349460,7.967187,-2.075888,2.534605,-8.488390,-8.673977,-9.336195,-7.444975,-3.786694,-6.377091,6.011416,8.083453,0.058345,7.859424,-7.083870,-3.503763,5.077906,3.274715,4.825354,-9.832745,-2.925668,-7.188417,-7.048410,-4.002366,-7.880156,-4.141542,2.661634,-0.364977,-7.072693,-3.056891,-4.503840,9.097946,-8.823033,-5.192924,4.934551,6.403178,6.805493,8.683662,-8.163139,-6.726777,-8.020238,7.995341,-3.675227,-7.576432,4.604705,5.683509,9.176182,8.693121,-6.842302,-2.587306,-9.814075,1.294371,2.427744,-1.571659,-3.256562,-2.547269,0.619507,-1.029240,-1.641428,4.806361,5.243413,0.909581,2.591447,-5.167347,-9.066546,-3.955363,-0.635015,-6.958468,-8.555603,-4.045042,1.393624,8.567192,-8.293019,-8.113746,-4.305487,-5.916259,1.652756,5.634300,-3.777146,-5.835002,-7.828639,-1.355364,-3.184792,-3.739781,0.442095,-6.613274,8.575805,5.956520,2.300423,-5.686136,5.669609,-2.089769,2.161035,-9.690600,9.459939,-9.041350,1.152458,9.604663,-9.130285,-3.180840,-9.578421,-3.147819,-6.004810,6.972813,-5.070484,0.268953,-4.722989,-2.434323,1.671371,3.747256,4.584119,-6.003549,-4.692850,-6.244707,8.007080,-2.372303,0.322516,-7.512767,3.980390,-4.096671,2.695843,5.908028,8.458841,5.811083,-0.724763,0.890236,2.666952,-2.776329,3.078300,-9.297263,7.892020,-1.563586,7.958097,-3.271785,-5.758579,-4.140675,9.607703,9.816422,4.974276,4.641929,-6.528087,0.962762,4.780155,8.730710,2.782858,3.332639,0.048752,9.997062,-0.884129,3.812310,-5.793546,2.227154,5.642097,-4.951403,1.837643,6.417412,0.645177,9.350006,-6.504140,6.088687,-2.030593,9.737452,7.320113,1.361504,-3.887077,-6.568691,-8.475917,-0.281787,5.827705,1.262461,9.866154,-8.290623,8.894309,2.709728,-6.411025,2.362673,7.294628,-1.846895,-5.282626,8.994012,-3.938990,8.757651,6.828328,3.599811,2.639850,7.888273,3.160916,5.966866,-9.158616,-2.341648,8.034483,7.742145,-4.770512,8.096688,8.743538,-4.120571,1.196567,4.980191,2.092567,4.520702,0.407225,3.221266,-6.241118,9.683387,0.518334,4.890714,-2.822155,-8.442907,5.366600,1.751392,-0.848447,-5.564499,7.463811,-4.583509,-3.588527,5.166548,-0.830824,-1.877547,2.121019,2.608225,-4.832084,-2.715333,-5.793695,5.178816,-7.471362,-5.109295,-0.783302,-6.278288,-4.094427,3.142029,-1.445850,-8.366388,0.872384,4.935639,2.396819,-1.684811,-3.417914,-9.194123,0.941599,-7.420205,-2.593283,-2.524177,7.638481,-4.205154,8.600889,3.204516,9.004680,-3.190721,-1.783652,7.599790,0.702633,1.595856,-5.408277,-6.502885,-7.903788,-1.479543,5.238930,6.738478,5.234725,8.186697,8.715390,5.806664,-8.999203,-5.968314,3.768774,-9.133408,4.499962,-7.812760,4.937545,3.310683,0.035825,-3.028169,-5.871316,-4.845807,-2.524232,-1.295558,-5.158192,-9.367377,1.358196,9.227317,-5.404908,6.707348,-2.327769,-8.492172,-5.787069,5.605772,7.830668,8.823587,9.084654,5.590207,4.760784,-9.871466,6.490376,-0.325018,9.196049,-9.196592,-8.864886,6.080333,7.661562,-6.006013,3.948500,-8.326882,-7.449827,-3.537933,7.236858,6.429249,3.631547,-5.767797,-5.628570,1.601861,-5.205228,5.410652], dtype = "float64")#candidate|4039|(528,)|const|float64
var_4040 = relay.var("var_4040", dtype = "float32", shape = (13,))#candidate|4040|(13,)|var|float32
call_4038 = relay.TupleGetItem(func_1833_call(relay.reshape(const_4039.astype('float64'), [6, 8, 11]), relay.reshape(var_4040.astype('float32'), [1, 13]), ), 2)
call_4041 = relay.TupleGetItem(func_1837_call(relay.reshape(const_4039.astype('float64'), [6, 8, 11]), relay.reshape(var_4040.astype('float32'), [1, 13]), ), 2)
func_3825_call = mod.get_global_var('func_3825')
func_3829_call = mutated_mod.get_global_var('func_3829')
var_4078 = relay.var("var_4078", dtype = "uint16", shape = (702,))#candidate|4078|(702,)|var|uint16
call_4077 = relay.TupleGetItem(func_3825_call(relay.reshape(var_4078.astype('uint16'), [702,]), relay.reshape(var_4040.astype('float32'), [1, 13]), ), 2)
call_4079 = relay.TupleGetItem(func_3829_call(relay.reshape(var_4078.astype('uint16'), [702,]), relay.reshape(var_4040.astype('float32'), [1, 13]), ), 2)
output = relay.Tuple([call_4036,call_4038,const_4039,var_4040,call_4077,var_4078,])
output2 = relay.Tuple([call_4037,call_4041,const_4039,var_4040,call_4079,var_4078,])
func_4080 = relay.Function([var_4040,var_4078,], output)
mod['func_4080'] = func_4080
mod = relay.transform.InferType()(mod)
mutated_mod['func_4080'] = func_4080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4080_call = mutated_mod.get_global_var('func_4080')
var_4082 = relay.var("var_4082", dtype = "float32", shape = (13,))#candidate|4082|(13,)|var|float32
var_4083 = relay.var("var_4083", dtype = "uint16", shape = (702,))#candidate|4083|(702,)|var|uint16
call_4081 = func_4080_call(var_4082,var_4083,)
output = call_4081
func_4084 = relay.Function([var_4082,var_4083,], output)
mutated_mod['func_4084'] = func_4084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4123 = relay.var("var_4123", dtype = "float64", shape = (12, 9, 1))#candidate|4123|(12, 9, 1)|var|float64
uop_4124 = relay.asin(var_4123.astype('float64')) # shape=(12, 9, 1)
output = relay.Tuple([uop_4124,])
output2 = relay.Tuple([uop_4124,])
func_4129 = relay.Function([var_4123,], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
var_4130 = relay.var("var_4130", dtype = "float64", shape = (12, 9, 1))#candidate|4130|(12, 9, 1)|var|float64
output = func_4129(var_4130)
func_4131 = relay.Function([var_4130], output)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_4154 = relay.TupleGetItem(func_1666_call(), 0)
call_4155 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_4154,])
output2 = relay.Tuple([call_4155,])
func_4165 = relay.Function([], output)
mod['func_4165'] = func_4165
mod = relay.transform.InferType()(mod)
output = func_4165()
func_4166 = relay.Function([], output)
mutated_mod['func_4166'] = func_4166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_680_call = mod.get_global_var('func_680')
func_682_call = mutated_mod.get_global_var('func_682')
call_4194 = relay.TupleGetItem(func_680_call(), 1)
call_4195 = relay.TupleGetItem(func_682_call(), 1)
output = relay.Tuple([call_4194,])
output2 = relay.Tuple([call_4195,])
func_4198 = relay.Function([], output)
mod['func_4198'] = func_4198
mod = relay.transform.InferType()(mod)
output = func_4198()
func_4199 = relay.Function([], output)
mutated_mod['func_4199'] = func_4199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2123_call = mod.get_global_var('func_2123')
func_2124_call = mutated_mod.get_global_var('func_2124')
call_4264 = relay.TupleGetItem(func_2123_call(), 0)
call_4265 = relay.TupleGetItem(func_2124_call(), 0)
func_1337_call = mod.get_global_var('func_1337')
func_1340_call = mutated_mod.get_global_var('func_1340')
var_4270 = relay.var("var_4270", dtype = "float32", shape = (405,))#candidate|4270|(405,)|var|float32
call_4269 = relay.TupleGetItem(func_1337_call(relay.reshape(var_4270.astype('float32'), [15, 3, 9])), 1)
call_4271 = relay.TupleGetItem(func_1340_call(relay.reshape(var_4270.astype('float32'), [15, 3, 9])), 1)
func_1729_call = mod.get_global_var('func_1729')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_4280 = relay.TupleGetItem(func_1729_call(), 0)
call_4281 = relay.TupleGetItem(func_1730_call(), 0)
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_4283 = relay.TupleGetItem(func_813_call(), 2)
call_4284 = relay.TupleGetItem(func_815_call(), 2)
func_2451_call = mod.get_global_var('func_2451')
func_2452_call = mutated_mod.get_global_var('func_2452')
call_4333 = func_2451_call()
call_4334 = func_2451_call()
output = relay.Tuple([call_4264,call_4269,var_4270,call_4280,call_4283,call_4333,])
output2 = relay.Tuple([call_4265,call_4271,var_4270,call_4281,call_4284,call_4334,])
func_4335 = relay.Function([var_4270,], output)
mod['func_4335'] = func_4335
mod = relay.transform.InferType()(mod)
mutated_mod['func_4335'] = func_4335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4336 = relay.var("var_4336", dtype = "float32", shape = (405,))#candidate|4336|(405,)|var|float32
func_4335_call = mutated_mod.get_global_var('func_4335')
call_4337 = func_4335_call(var_4336)
output = call_4337
func_4338 = relay.Function([var_4336], output)
mutated_mod['func_4338'] = func_4338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3119_call = mod.get_global_var('func_3119')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_4361 = relay.TupleGetItem(func_3119_call(), 0)
call_4362 = relay.TupleGetItem(func_3121_call(), 0)
uop_4373 = relay.sqrt(call_4361.astype('float64')) # shape=(6, 8, 11)
uop_4375 = relay.sqrt(call_4362.astype('float64')) # shape=(6, 8, 11)
output = relay.Tuple([uop_4373,])
output2 = relay.Tuple([uop_4375,])
func_4387 = relay.Function([], output)
mod['func_4387'] = func_4387
mod = relay.transform.InferType()(mod)
mutated_mod['func_4387'] = func_4387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4387_call = mutated_mod.get_global_var('func_4387')
call_4388 = func_4387_call()
output = call_4388
func_4389 = relay.Function([], output)
mutated_mod['func_4389'] = func_4389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4198_call = mod.get_global_var('func_4198')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_4398 = relay.TupleGetItem(func_4198_call(), 0)
call_4399 = relay.TupleGetItem(func_4199_call(), 0)
func_2618_call = mod.get_global_var('func_2618')
func_2620_call = mutated_mod.get_global_var('func_2620')
const_4416 = relay.const([[-4.106484,-9.098288,-0.139511,-8.347367,-0.797355,-8.003560,9.839084,7.530267,7.570986,-5.896381,-3.935601,1.809584,-0.076417,-3.976286,8.224298,-6.038416,8.174678,5.478141],[-2.808912,-7.835469,0.017834,8.844977,-3.580203,2.275919,8.741228,6.652021,-6.133879,-0.194597,8.469847,-5.646803,6.226601,-6.700458,5.818120,-2.958721,1.377526,-8.706985],[-2.537340,0.737754,6.836369,-0.040157,-4.899676,-1.225805,-8.363445,-6.735182,3.744461,-0.892820,3.923695,7.522074,1.587557,3.052000,7.342394,7.758809,4.450168,-8.385753]], dtype = "float32")#candidate|4416|(3, 18)|const|float32
call_4415 = func_2618_call(relay.reshape(const_4416.astype('float32'), [6, 3, 3]))
call_4417 = func_2618_call(relay.reshape(const_4416.astype('float32'), [6, 3, 3]))
output = relay.Tuple([call_4398,call_4415,const_4416,])
output2 = relay.Tuple([call_4399,call_4417,const_4416,])
func_4419 = relay.Function([], output)
mod['func_4419'] = func_4419
mod = relay.transform.InferType()(mod)
mutated_mod['func_4419'] = func_4419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4419_call = mutated_mod.get_global_var('func_4419')
call_4420 = func_4419_call()
output = call_4420
func_4421 = relay.Function([], output)
mutated_mod['func_4421'] = func_4421
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4438 = relay.var("var_4438", dtype = "float32", shape = (3, 8))#candidate|4438|(3, 8)|var|float32
uop_4439 = relay.atanh(var_4438.astype('float32')) # shape=(3, 8)
output = uop_4439
output2 = uop_4439
func_4450 = relay.Function([var_4438,], output)
mod['func_4450'] = func_4450
mod = relay.transform.InferType()(mod)
mutated_mod['func_4450'] = func_4450
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4451 = relay.var("var_4451", dtype = "float32", shape = (3, 8))#candidate|4451|(3, 8)|var|float32
func_4450_call = mutated_mod.get_global_var('func_4450')
call_4452 = func_4450_call(var_4451)
output = call_4452
func_4453 = relay.Function([var_4451], output)
mutated_mod['func_4453'] = func_4453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3967_call = mod.get_global_var('func_3967')
func_3969_call = mutated_mod.get_global_var('func_3969')
call_4462 = relay.TupleGetItem(func_3967_call(), 0)
call_4463 = relay.TupleGetItem(func_3969_call(), 0)
output = call_4462
output2 = call_4463
func_4464 = relay.Function([], output)
mod['func_4464'] = func_4464
mod = relay.transform.InferType()(mod)
output = func_4464()
func_4465 = relay.Function([], output)
mutated_mod['func_4465'] = func_4465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_4510 = func_3316_call()
call_4511 = func_3316_call()
output = call_4510
output2 = call_4511
func_4517 = relay.Function([], output)
mod['func_4517'] = func_4517
mod = relay.transform.InferType()(mod)
mutated_mod['func_4517'] = func_4517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4517_call = mutated_mod.get_global_var('func_4517')
call_4518 = func_4517_call()
output = call_4518
func_4519 = relay.Function([], output)
mutated_mod['func_4519'] = func_4519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_4525 = func_1571_call()
call_4526 = func_1571_call()
output = relay.Tuple([call_4525,])
output2 = relay.Tuple([call_4526,])
func_4534 = relay.Function([], output)
mod['func_4534'] = func_4534
mod = relay.transform.InferType()(mod)
output = func_4534()
func_4535 = relay.Function([], output)
mutated_mod['func_4535'] = func_4535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_4579 = func_3316_call()
call_4580 = func_3316_call()
func_4464_call = mod.get_global_var('func_4464')
func_4465_call = mutated_mod.get_global_var('func_4465')
call_4612 = func_4464_call()
call_4613 = func_4464_call()
output = relay.Tuple([call_4579,call_4612,])
output2 = relay.Tuple([call_4580,call_4613,])
func_4633 = relay.Function([], output)
mod['func_4633'] = func_4633
mod = relay.transform.InferType()(mod)
output = func_4633()
func_4634 = relay.Function([], output)
mutated_mod['func_4634'] = func_4634
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4725 = relay.const([[[3,-9,3,-7,-5,-5,3,2],[-1,7,-8,4,3,2,7,-9],[-3,-9,4,3,9,10,7,-1],[4,4,5,8,5,-9,-2,-1],[1,-3,8,-6,-8,-8,-10,-1],[-9,8,5,1,4,10,-2,-2],[3,-8,1,-9,-2,-4,-7,7],[-2,-1,9,-4,-4,10,7,9],[-7,-2,-2,-7,-9,-5,10,2],[6,-8,5,-9,-8,7,1,5],[2,6,10,8,-8,4,4,-7],[-1,-5,-9,-5,3,2,7,-4],[7,-5,-5,6,6,9,-8,-10]]], dtype = "int64")#candidate|4725|(1, 13, 8)|const|int64
const_4726 = relay.const([[[5,-10,-9,-4,9,-2,-4,-10],[6,2,9,4,9,4,10,5],[-9,6,7,3,-3,6,-4,6],[4,-3,-9,-10,-6,-8,-2,-2],[7,1,9,-10,6,2,6,1],[-10,-4,-9,7,-9,-4,9,3],[5,10,5,8,9,3,-2,5],[9,10,4,-5,-4,3,4,-9],[-10,-5,-2,10,5,-5,8,-8],[1,-4,5,7,8,-5,6,1],[5,-2,-1,6,-6,4,5,10],[9,-1,3,6,-8,2,-4,-9],[-1,6,3,-9,-7,2,2,-7]],[[6,-7,-4,8,3,5,7,6],[4,1,4,-6,-10,2,-10,4],[7,-5,-6,2,-5,7,-10,1],[5,-3,1,-1,-10,4,1,6],[-1,8,3,7,6,1,8,-2],[-5,3,6,8,8,4,2,-7],[10,-10,-5,3,10,-9,-8,-3],[-6,1,-10,-6,1,-8,-1,-3],[2,5,10,-1,2,1,1,-4],[-10,-6,4,-1,-5,5,5,10],[5,7,1,-10,-7,4,-4,-4],[-3,-7,6,1,8,-9,8,-2],[-5,10,8,1,-10,-5,3,-1]],[[10,7,-5,-9,-8,5,10,-1],[-6,-10,-9,-2,-6,-3,6,9],[-3,4,-5,-2,1,-9,5,-3],[10,-7,-4,10,-6,1,9,10],[6,-10,4,6,-9,4,6,9],[3,-5,-7,-9,9,6,1,10],[7,10,3,-7,-2,8,-2,-2],[-5,4,-3,6,4,-2,10,-2],[-1,10,-8,-6,-2,6,1,1],[-8,-7,-7,-5,-7,-3,8,-5],[8,2,-4,6,-5,10,-4,-2],[-3,5,4,-10,-6,9,10,4],[-9,6,7,9,-8,-7,-9,5]],[[10,3,-2,8,-8,2,10,10],[2,-3,9,2,1,2,-10,4],[-8,5,-10,8,9,7,-7,9],[4,10,-3,3,-2,6,3,-10],[-4,1,-8,-3,-8,-6,-9,4],[-8,7,7,-7,-6,-8,2,-9],[5,-2,6,1,10,-9,-4,-4],[-9,4,-2,6,-4,6,4,-2],[-5,5,-4,5,6,2,-1,2],[7,8,7,-9,8,-6,-1,3],[-7,-7,-3,-4,10,-8,-2,1],[-4,-3,4,-3,7,5,10,-4],[-4,-7,-3,7,8,-4,-6,4]],[[-7,3,6,4,-5,-1,-6,-3],[6,-9,-2,-4,-4,3,-5,-1],[1,-6,10,-2,8,2,-8,6],[9,-5,-6,3,9,-7,2,-9],[-2,2,2,8,9,7,9,3],[1,-10,9,6,-1,2,-2,8],[3,-7,6,-8,7,4,1,5],[5,8,1,2,8,7,3,4],[-9,-5,-6,10,10,-1,-1,-2],[4,-10,5,-8,6,-3,-5,8],[-7,9,-8,9,4,1,-8,2],[5,8,-6,5,6,-10,4,-4],[-3,-6,-1,10,-9,-1,-4,-1]],[[-6,10,-7,-3,-4,3,3,1],[-10,8,6,-7,1,-3,8,5],[-5,8,-4,7,6,-6,-9,6],[5,-1,3,7,-3,-8,-6,-6],[2,5,5,-1,-3,-1,-5,-4],[-2,-3,-2,-1,-3,-7,-4,10],[-9,9,6,-6,-7,3,-5,-4],[9,-3,2,-7,5,-3,-9,2],[-7,-3,-2,-2,-7,3,-2,-10],[-8,4,-9,2,5,2,8,3],[6,6,4,-9,5,-4,10,-7],[-8,-8,-2,-2,6,4,-7,-7],[2,3,5,8,3,-6,5,-1]],[[6,4,10,6,8,-9,-6,10],[-2,-3,-2,-7,-2,-7,-6,-2],[10,10,-1,-5,8,-6,2,10],[6,3,4,-4,-2,-5,-1,-1],[-2,10,-9,4,9,-10,5,-7],[5,10,9,-8,-7,9,10,1],[-1,7,6,-7,-9,-7,9,7],[3,5,-3,1,4,8,-10,-5],[-9,-2,2,-1,-6,-7,-2,1],[2,-5,7,-5,-6,4,-3,6],[9,-7,7,4,-6,-10,-5,-4],[-7,2,-7,-4,9,10,6,3],[3,-8,10,6,5,8,9,9]],[[-3,1,-7,4,2,9,1,3],[4,6,5,1,10,-2,-1,4],[-1,5,-1,-5,4,-2,7,-9],[-9,4,7,-4,5,5,-6,-2],[-5,6,-8,10,6,-7,7,4],[2,-10,5,5,9,-10,2,-1],[-10,4,7,-2,-4,-5,-6,9],[-9,7,2,-6,6,5,9,-5],[-2,-9,-3,-1,1,-9,5,6],[-6,9,-7,-10,-2,-8,-2,10],[-4,-2,-1,5,9,8,2,9],[7,8,3,-6,5,-6,9,-1],[-6,-1,6,-8,9,-8,-1,1]],[[-2,-3,-8,-2,5,10,-7,-8],[-5,-9,-4,-5,-2,-4,-9,1],[5,-10,5,6,1,5,-8,-10],[-1,-6,-3,-7,-4,-8,-7,8],[-4,-3,-10,8,-6,1,5,8],[8,2,5,-8,10,3,6,-9],[8,7,2,1,-8,3,2,9],[3,5,1,-6,9,10,9,-6],[-1,6,8,-1,-8,10,-6,-1],[-10,-9,-10,-4,4,-6,3,-1],[5,-8,-5,-1,-5,-4,-10,2],[-3,-3,-5,4,10,4,4,-8],[5,3,-6,4,5,-2,2,7]],[[4,8,6,9,-2,9,-10,-4],[-4,-4,3,-2,3,5,10,1],[-1,-3,1,-5,5,-8,3,-10],[10,7,-10,-4,-3,-10,-1,6],[10,-1,3,3,-9,5,-6,9],[6,1,-3,3,-6,-10,4,10],[-7,-4,-6,10,-1,-7,7,2],[2,-3,8,4,7,-10,-1,-4],[1,1,-8,-3,4,-3,-8,8],[8,-8,5,2,-5,4,5,8],[-9,-3,10,3,8,8,-3,-7],[-8,-9,6,-7,-6,-8,-1,6],[5,-7,5,-10,-8,-10,-5,-3]],[[-3,-5,6,9,5,10,4,-7],[7,-6,6,7,6,-6,-8,5],[-3,-10,4,-8,9,-6,6,-3],[-9,-7,-7,-10,4,8,-7,3],[5,7,-7,10,-5,-10,-2,-5],[-4,-8,7,-5,-6,-2,8,-10],[-3,2,-2,-5,-9,-1,9,-1],[-8,-5,-9,-5,5,-5,-5,6],[4,7,8,-4,-8,-7,-10,-10],[-9,5,-9,-2,-10,-9,-4,4],[-1,-3,-4,6,-1,-6,1,-1],[-5,8,-9,-10,9,-5,-2,-2],[-1,-2,3,4,8,7,10,-10]]], dtype = "int64")#candidate|4726|(11, 13, 8)|const|int64
bop_4727 = relay.subtract(const_4725.astype('int64'), const_4726.astype('int64')) # shape=(11, 13, 8)
bop_4735 = relay.left_shift(const_4726.astype('uint8'), relay.reshape(bop_4727.astype('uint8'), relay.shape_of(const_4726))) # shape=(11, 13, 8)
output = bop_4735
output2 = bop_4735
func_4748 = relay.Function([], output)
mod['func_4748'] = func_4748
mod = relay.transform.InferType()(mod)
output = func_4748()
func_4749 = relay.Function([], output)
mutated_mod['func_4749'] = func_4749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4464_call = mod.get_global_var('func_4464')
func_4465_call = mutated_mod.get_global_var('func_4465')
call_4797 = func_4464_call()
call_4798 = func_4464_call()
func_1729_call = mod.get_global_var('func_1729')
func_1730_call = mutated_mod.get_global_var('func_1730')
call_4807 = relay.TupleGetItem(func_1729_call(), 0)
call_4808 = relay.TupleGetItem(func_1730_call(), 0)
func_1833_call = mod.get_global_var('func_1833')
func_1837_call = mutated_mod.get_global_var('func_1837')
const_4810 = relay.const([[3.464268],[3.813600],[9.981678],[-4.816569],[-4.843979],[-5.621710],[-5.562364],[5.434832],[4.052865],[-4.769312],[5.225990],[-0.391783],[-5.035783]], dtype = "float32")#candidate|4810|(13, 1)|const|float32
call_4809 = relay.TupleGetItem(func_1833_call(relay.reshape(call_4807.astype('float64'), [6, 8, 11]), relay.reshape(const_4810.astype('float32'), [1, 13]), ), 2)
call_4811 = relay.TupleGetItem(func_1837_call(relay.reshape(call_4807.astype('float64'), [6, 8, 11]), relay.reshape(const_4810.astype('float32'), [1, 13]), ), 2)
output = relay.Tuple([call_4797,call_4807,call_4809,const_4810,])
output2 = relay.Tuple([call_4798,call_4808,call_4811,const_4810,])
func_4818 = relay.Function([], output)
mod['func_4818'] = func_4818
mod = relay.transform.InferType()(mod)
mutated_mod['func_4818'] = func_4818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4818_call = mutated_mod.get_global_var('func_4818')
call_4819 = func_4818_call()
output = call_4819
func_4820 = relay.Function([], output)
mutated_mod['func_4820'] = func_4820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_4831 = relay.TupleGetItem(func_1666_call(), 0)
call_4832 = relay.TupleGetItem(func_1667_call(), 0)
output = call_4831
output2 = call_4832
func_4854 = relay.Function([], output)
mod['func_4854'] = func_4854
mod = relay.transform.InferType()(mod)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mutated_mod.get_global_var('func_4854')
call_4855 = func_4854_call()
output = call_4855
func_4856 = relay.Function([], output)
mutated_mod['func_4856'] = func_4856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1123_call = mod.get_global_var('func_1123')
func_1125_call = mutated_mod.get_global_var('func_1125')
call_4899 = relay.TupleGetItem(func_1123_call(), 0)
call_4900 = relay.TupleGetItem(func_1125_call(), 0)
output = relay.Tuple([call_4899,])
output2 = relay.Tuple([call_4900,])
func_4901 = relay.Function([], output)
mod['func_4901'] = func_4901
mod = relay.transform.InferType()(mod)
output = func_4901()
func_4902 = relay.Function([], output)
mutated_mod['func_4902'] = func_4902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4901_call = mod.get_global_var('func_4901')
func_4902_call = mutated_mod.get_global_var('func_4902')
call_4959 = relay.TupleGetItem(func_4901_call(), 0)
call_4960 = relay.TupleGetItem(func_4902_call(), 0)
uop_4970 = relay.atanh(call_4959.astype('float32')) # shape=(6, 8, 11)
uop_4972 = relay.atanh(call_4960.astype('float32')) # shape=(6, 8, 11)
output = relay.Tuple([uop_4970,])
output2 = relay.Tuple([uop_4972,])
func_4981 = relay.Function([], output)
mod['func_4981'] = func_4981
mod = relay.transform.InferType()(mod)
output = func_4981()
func_4982 = relay.Function([], output)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4633_call = mod.get_global_var('func_4633')
func_4634_call = mutated_mod.get_global_var('func_4634')
call_5023 = relay.TupleGetItem(func_4633_call(), 1)
call_5024 = relay.TupleGetItem(func_4634_call(), 1)
uop_5036 = relay.sigmoid(call_5023.astype('float64')) # shape=(6, 8, 11)
uop_5038 = relay.sigmoid(call_5024.astype('float64')) # shape=(6, 8, 11)
func_2987_call = mod.get_global_var('func_2987')
func_2991_call = mutated_mod.get_global_var('func_2991')
const_5044 = relay.const([6,-7,6,1,4,-5,-6,10,8,5,4,-3,-8,6,-7,-7,-10,4,-10,10,-6,3,-7,-1,-4,10,2,6,8,5,-8,10,1,-8,8,-6,-4,-6,1,-5,-6,4,-8,-9,-4,-2,1,2,6,2,7,-8,-7,1,4,5,-3,-9,1,5,-6,-8,1,-8,10,-2,-10,-10,-5,-4,-9,8], dtype = "uint16")#candidate|5044|(72,)|const|uint16
var_5045 = relay.var("var_5045", dtype = "float64", shape = (405,))#candidate|5045|(405,)|var|float64
call_5043 = relay.TupleGetItem(func_2987_call(relay.reshape(const_5044.astype('uint16'), [72,]), relay.reshape(var_5045.astype('float64'), [405,]), ), 1)
call_5046 = relay.TupleGetItem(func_2991_call(relay.reshape(const_5044.astype('uint16'), [72,]), relay.reshape(var_5045.astype('float64'), [405,]), ), 1)
func_3377_call = mod.get_global_var('func_3377')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_5047 = func_3377_call()
call_5048 = func_3377_call()
bop_5049 = relay.bitwise_xor(uop_5036.astype('int16'), relay.reshape(call_5023.astype('int16'), relay.shape_of(uop_5036))) # shape=(6, 8, 11)
bop_5052 = relay.bitwise_xor(uop_5038.astype('int16'), relay.reshape(call_5024.astype('int16'), relay.shape_of(uop_5038))) # shape=(6, 8, 11)
uop_5055 = relay.asin(uop_5036.astype('float64')) # shape=(6, 8, 11)
uop_5057 = relay.asin(uop_5038.astype('float64')) # shape=(6, 8, 11)
uop_5083 = relay.atan(uop_5055.astype('float64')) # shape=(6, 8, 11)
uop_5085 = relay.atan(uop_5057.astype('float64')) # shape=(6, 8, 11)
bop_5086 = relay.left_shift(uop_5083.astype('int8'), relay.reshape(uop_5055.astype('int8'), relay.shape_of(uop_5083))) # shape=(6, 8, 11)
bop_5089 = relay.left_shift(uop_5085.astype('int8'), relay.reshape(uop_5057.astype('int8'), relay.shape_of(uop_5085))) # shape=(6, 8, 11)
output = relay.Tuple([call_5043,const_5044,var_5045,call_5047,bop_5049,bop_5086,])
output2 = relay.Tuple([call_5046,const_5044,var_5045,call_5048,bop_5052,bop_5089,])
func_5091 = relay.Function([var_5045,], output)
mod['func_5091'] = func_5091
mod = relay.transform.InferType()(mod)
var_5092 = relay.var("var_5092", dtype = "float64", shape = (405,))#candidate|5092|(405,)|var|float64
output = func_5091(var_5092)
func_5093 = relay.Function([var_5092], output)
mutated_mod['func_5093'] = func_5093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1859_call = mod.get_global_var('func_1859')
func_1860_call = mutated_mod.get_global_var('func_1860')
call_5124 = func_1859_call()
call_5125 = func_1859_call()
output = relay.Tuple([call_5124,])
output2 = relay.Tuple([call_5125,])
func_5157 = relay.Function([], output)
mod['func_5157'] = func_5157
mod = relay.transform.InferType()(mod)
mutated_mod['func_5157'] = func_5157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5157_call = mutated_mod.get_global_var('func_5157')
call_5158 = func_5157_call()
output = call_5158
func_5159 = relay.Function([], output)
mutated_mod['func_5159'] = func_5159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4534_call = mod.get_global_var('func_4534')
func_4535_call = mutated_mod.get_global_var('func_4535')
call_5162 = relay.TupleGetItem(func_4534_call(), 0)
call_5163 = relay.TupleGetItem(func_4535_call(), 0)
output = call_5162
output2 = call_5163
func_5164 = relay.Function([], output)
mod['func_5164'] = func_5164
mod = relay.transform.InferType()(mod)
output = func_5164()
func_5165 = relay.Function([], output)
mutated_mod['func_5165'] = func_5165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_5225 = relay.TupleGetItem(func_2777_call(), 1)
call_5226 = relay.TupleGetItem(func_2778_call(), 1)
output = relay.Tuple([call_5225,])
output2 = relay.Tuple([call_5226,])
func_5244 = relay.Function([], output)
mod['func_5244'] = func_5244
mod = relay.transform.InferType()(mod)
output = func_5244()
func_5245 = relay.Function([], output)
mutated_mod['func_5245'] = func_5245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_5258 = relay.TupleGetItem(func_5157_call(), 0)
call_5259 = relay.TupleGetItem(func_5159_call(), 0)
var_5274 = relay.var("var_5274", dtype = "float64", shape = (6, 8, 11))#candidate|5274|(6, 8, 11)|var|float64
bop_5275 = relay.maximum(call_5258.astype('int32'), relay.reshape(var_5274.astype('int32'), relay.shape_of(call_5258))) # shape=(6, 8, 11)
bop_5278 = relay.maximum(call_5259.astype('int32'), relay.reshape(var_5274.astype('int32'), relay.shape_of(call_5259))) # shape=(6, 8, 11)
output = bop_5275
output2 = bop_5278
func_5284 = relay.Function([var_5274,], output)
mod['func_5284'] = func_5284
mod = relay.transform.InferType()(mod)
var_5285 = relay.var("var_5285", dtype = "float64", shape = (6, 8, 11))#candidate|5285|(6, 8, 11)|var|float64
output = func_5284(var_5285)
func_5286 = relay.Function([var_5285], output)
mutated_mod['func_5286'] = func_5286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3516_call = mod.get_global_var('func_3516')
func_3518_call = mutated_mod.get_global_var('func_3518')
call_5288 = relay.TupleGetItem(func_3516_call(), 0)
call_5289 = relay.TupleGetItem(func_3518_call(), 0)
func_4517_call = mod.get_global_var('func_4517')
func_4519_call = mutated_mod.get_global_var('func_4519')
call_5296 = func_4517_call()
call_5297 = func_4517_call()
func_3419_call = mod.get_global_var('func_3419')
func_3422_call = mutated_mod.get_global_var('func_3422')
const_5300 = relay.const([[True,False,False,False],[True,False,False,True],[False,False,False,False],[False,True,True,True],[True,True,False,False],[False,False,True,True],[False,False,False,False],[False,True,True,False],[True,True,False,True],[False,False,False,False],[True,False,False,True],[False,False,False,True],[True,False,True,True],[False,False,False,True],[False,True,True,False],[False,False,False,False],[True,False,True,True],[True,True,True,False],[True,False,True,True],[False,False,False,True],[False,True,False,True],[True,False,False,True]], dtype = "bool")#candidate|5300|(22, 4)|const|bool
var_5301 = relay.var("var_5301", dtype = "uint16", shape = ())#candidate|5301|()|var|uint16
call_5299 = relay.TupleGetItem(func_3419_call(relay.reshape(const_5300.astype('bool'), [88,]), relay.reshape(var_5301.astype('uint16'), []), ), 3)
call_5302 = relay.TupleGetItem(func_3422_call(relay.reshape(const_5300.astype('bool'), [88,]), relay.reshape(var_5301.astype('uint16'), []), ), 3)
output = relay.Tuple([call_5288,call_5296,call_5299,const_5300,var_5301,])
output2 = relay.Tuple([call_5289,call_5297,call_5302,const_5300,var_5301,])
func_5334 = relay.Function([var_5301,], output)
mod['func_5334'] = func_5334
mod = relay.transform.InferType()(mod)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5335 = relay.var("var_5335", dtype = "uint16", shape = ())#candidate|5335|()|var|uint16
func_5334_call = mutated_mod.get_global_var('func_5334')
call_5336 = func_5334_call(var_5335)
output = call_5336
func_5337 = relay.Function([var_5335], output)
mutated_mod['func_5337'] = func_5337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4633_call = mod.get_global_var('func_4633')
func_4634_call = mutated_mod.get_global_var('func_4634')
call_5356 = relay.TupleGetItem(func_4633_call(), 1)
call_5357 = relay.TupleGetItem(func_4634_call(), 1)
var_5362 = relay.var("var_5362", dtype = "float64", shape = (6, 8, 11))#candidate|5362|(6, 8, 11)|var|float64
bop_5363 = relay.logical_xor(call_5356.astype('uint32'), relay.reshape(var_5362.astype('uint32'), relay.shape_of(call_5356))) # shape=(6, 8, 11)
bop_5366 = relay.logical_xor(call_5357.astype('uint32'), relay.reshape(var_5362.astype('uint32'), relay.shape_of(call_5357))) # shape=(6, 8, 11)
output = bop_5363
output2 = bop_5366
func_5378 = relay.Function([var_5362,], output)
mod['func_5378'] = func_5378
mod = relay.transform.InferType()(mod)
mutated_mod['func_5378'] = func_5378
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5379 = relay.var("var_5379", dtype = "float64", shape = (6, 8, 11))#candidate|5379|(6, 8, 11)|var|float64
func_5378_call = mutated_mod.get_global_var('func_5378')
call_5380 = func_5378_call(var_5379)
output = call_5380
func_5381 = relay.Function([var_5379], output)
mutated_mod['func_5381'] = func_5381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mod.get_global_var('func_4854')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_5409 = func_4854_call()
call_5410 = func_4854_call()
output = relay.Tuple([call_5409,])
output2 = relay.Tuple([call_5410,])
func_5430 = relay.Function([], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
output = func_5430()
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3377_call = mod.get_global_var('func_3377')
func_3378_call = mutated_mod.get_global_var('func_3378')
call_5435 = func_3377_call()
call_5436 = func_3377_call()
const_5437 = relay.const([[[-3,4,3,5,7,-4,10,9,5],[9,6,-4,-3,1,-6,-5,5,-6],[-7,8,2,10,-9,3,-8,-4,6]],[[-5,6,8,8,10,3,4,7,-3],[-5,3,3,9,-8,8,-2,-3,-8],[10,-4,-3,-8,-6,-10,-6,-5,-10]],[[4,-10,10,-6,-2,1,-10,7,-1],[3,-9,4,2,-6,-8,-5,-4,5],[-4,8,-10,5,-10,-5,3,2,-9]],[[-3,6,-7,-4,7,7,5,4,5],[-4,3,-3,7,-10,-9,-5,9,-2],[8,-9,7,8,5,-5,6,-3,3]],[[9,5,7,8,8,5,-6,-7,7],[-8,6,-7,-8,-10,1,-8,-1,10],[8,-4,-9,-6,10,-1,9,-2,-5]],[[-6,9,3,-9,-10,3,-2,2,-7],[3,-8,-9,9,-8,-3,-9,5,6],[8,8,-8,10,4,-4,-2,4,-9]],[[7,-1,1,8,-4,8,1,-7,-3],[-2,5,-2,-6,-5,4,-5,1,8],[1,-2,10,-9,5,10,1,1,-9]],[[-2,-9,7,-10,-6,10,5,-1,8],[-6,-2,3,8,-5,1,-2,-1,1],[-6,-10,-3,6,2,6,1,-9,2]],[[-7,7,9,-8,-2,-4,6,-3,2],[-5,-4,8,-8,-2,1,8,-4,2],[4,8,10,6,-2,10,-5,-2,5]],[[8,10,10,-4,1,-5,5,6,5],[5,-10,2,-1,-9,5,5,-7,5],[-8,6,-1,4,-4,9,-6,3,-1]],[[8,-4,-5,8,4,6,-3,-2,-6],[1,9,10,-7,4,2,6,7,6],[-1,-3,2,-6,-4,5,1,9,3]],[[10,8,9,9,-2,7,10,4,3],[-5,-10,-7,-10,-3,8,10,8,-2],[-10,4,7,7,9,3,7,1,6]],[[6,-8,-4,-7,-6,4,1,9,3],[-7,3,4,-8,-3,-10,-8,-4,-7],[7,-7,-8,1,5,7,3,-8,1]],[[-2,5,-9,4,-1,-6,-1,2,-5],[8,-10,-3,-1,-10,-5,-3,10,-4],[-2,6,9,4,6,7,-6,7,-10]],[[-2,9,1,3,-2,-1,1,5,9],[-1,3,8,-9,6,10,-8,-8,4],[-10,-3,-7,-9,8,-6,-5,7,-6]]], dtype = "uint16")#candidate|5437|(15, 3, 9)|const|uint16
bop_5438 = relay.less(call_5435.astype('bool'), relay.reshape(const_5437.astype('bool'), relay.shape_of(call_5435))) # shape=(15, 3, 9)
bop_5441 = relay.less(call_5436.astype('bool'), relay.reshape(const_5437.astype('bool'), relay.shape_of(call_5436))) # shape=(15, 3, 9)
var_5453 = relay.var("var_5453", dtype = "uint16", shape = (15, 3, 9))#candidate|5453|(15, 3, 9)|var|uint16
bop_5454 = relay.logical_or(call_5435.astype('bool'), relay.reshape(var_5453.astype('bool'), relay.shape_of(call_5435))) # shape=(15, 3, 9)
bop_5457 = relay.logical_or(call_5436.astype('bool'), relay.reshape(var_5453.astype('bool'), relay.shape_of(call_5436))) # shape=(15, 3, 9)
func_4335_call = mod.get_global_var('func_4335')
func_4338_call = mutated_mod.get_global_var('func_4338')
call_5458 = relay.TupleGetItem(func_4335_call(relay.reshape(bop_5438.astype('float32'), [405,])), 1)
call_5459 = relay.TupleGetItem(func_4338_call(relay.reshape(bop_5438.astype('float32'), [405,])), 1)
uop_5472 = relay.atanh(call_5435.astype('float32')) # shape=(15, 3, 9)
uop_5474 = relay.atanh(call_5436.astype('float32')) # shape=(15, 3, 9)
output = relay.Tuple([bop_5438,bop_5454,call_5458,uop_5472,])
output2 = relay.Tuple([bop_5441,bop_5457,call_5459,uop_5474,])
func_5477 = relay.Function([var_5453,], output)
mod['func_5477'] = func_5477
mod = relay.transform.InferType()(mod)
var_5478 = relay.var("var_5478", dtype = "uint16", shape = (15, 3, 9))#candidate|5478|(15, 3, 9)|var|uint16
output = func_5477(var_5478)
func_5479 = relay.Function([var_5478], output)
mutated_mod['func_5479'] = func_5479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4818_call = mod.get_global_var('func_4818')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_5577 = relay.TupleGetItem(func_4818_call(), 0)
call_5578 = relay.TupleGetItem(func_4820_call(), 0)
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_5581 = relay.TupleGetItem(func_5157_call(), 0)
call_5582 = relay.TupleGetItem(func_5159_call(), 0)
output = relay.Tuple([call_5577,call_5581,])
output2 = relay.Tuple([call_5578,call_5582,])
func_5590 = relay.Function([], output)
mod['func_5590'] = func_5590
mod = relay.transform.InferType()(mod)
output = func_5590()
func_5591 = relay.Function([], output)
mutated_mod['func_5591'] = func_5591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1666_call = mod.get_global_var('func_1666')
func_1667_call = mutated_mod.get_global_var('func_1667')
call_5622 = relay.TupleGetItem(func_1666_call(), 0)
call_5623 = relay.TupleGetItem(func_1667_call(), 0)
output = relay.Tuple([call_5622,])
output2 = relay.Tuple([call_5623,])
func_5635 = relay.Function([], output)
mod['func_5635'] = func_5635
mod = relay.transform.InferType()(mod)
mutated_mod['func_5635'] = func_5635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5635_call = mutated_mod.get_global_var('func_5635')
call_5636 = func_5635_call()
output = call_5636
func_5637 = relay.Function([], output)
mutated_mod['func_5637'] = func_5637
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5727 = relay.const([[[-2.958390,-7.666654,-8.636585],[-5.135329,-9.368868,5.882598],[8.083067,-0.668906,3.777793],[-0.685866,7.294540,-0.684083],[-8.065775,6.936863,6.715688],[-0.796346,-8.788205,5.690520],[1.086542,-4.739035,8.522362],[6.188753,-9.917762,8.994802],[4.919122,-4.048650,-4.158090],[3.396297,-4.176031,0.175534],[7.188934,-5.927012,-0.338693],[5.713463,0.058863,3.367399],[6.980117,0.161209,-5.210299]],[[-6.280874,-5.113931,-9.513478],[0.567038,-5.035074,-4.628036],[3.651137,9.093719,6.719538],[-1.600799,2.409847,-0.627889],[-6.026265,-4.891181,-6.586800],[6.505164,-9.245246,9.054840],[-3.115931,-1.887243,9.824324],[-7.812231,7.078261,-1.550425],[-0.546119,0.742048,-1.721590],[-1.407829,7.665164,7.911093],[-5.613117,-6.251005,-4.515539],[8.599347,-8.051015,9.819034],[1.133044,5.346594,-0.716989]],[[8.539270,-4.218786,-9.136625],[3.623967,6.160747,7.669736],[-1.443148,8.103160,-0.393107],[-2.916121,7.603934,-5.039015],[-6.640216,-0.952679,-8.034056],[6.331109,2.875761,-1.041703],[0.731031,7.696643,-0.807457],[3.681495,-4.465794,-6.993845],[-2.346178,-7.204554,9.749542],[1.451540,-2.496055,7.553351],[-4.535539,1.716989,-2.216291],[7.186175,0.307888,1.908567],[-0.205315,-9.440113,5.591206]],[[0.670818,8.605447,5.408481],[-9.299889,3.642349,2.244884],[8.703910,9.655141,2.723827],[-6.301936,0.786640,4.040828],[-4.639106,2.404076,-6.934734],[9.485785,3.866534,-8.325496],[6.489533,6.303939,8.125086],[-0.126137,-4.189639,8.611486],[2.749920,-0.303745,7.827245],[1.524203,2.518575,-9.731089],[-4.083269,-5.454424,3.240791],[-9.301809,3.965532,5.693786],[-1.373154,-6.535831,7.325766]],[[9.763152,4.599766,-7.120073],[1.589193,-7.993542,-9.862658],[7.987397,-2.349002,-9.101029],[-5.535437,1.708821,-8.941105],[-1.171025,-3.456000,4.239591],[2.636640,-2.246559,8.781759],[1.632693,6.755965,6.402992],[1.499640,-0.246148,-4.497434],[2.296572,4.155190,0.585477],[6.478131,7.863465,-3.664950],[0.962853,6.085611,-7.322649],[-0.586134,0.509723,-7.547951],[-0.001491,1.782238,5.440655]],[[5.921631,-3.592029,3.122705],[9.085109,-9.942372,-2.213102],[4.636769,-3.247821,-9.413281],[5.804860,-7.771008,-0.331499],[-5.704967,-7.680847,6.719609],[6.014551,-7.716574,9.774887],[6.903786,-0.207819,0.940526],[-8.140895,1.750740,1.304668],[-4.287251,-3.963615,-7.268807],[6.407310,8.222808,-4.248325],[1.874894,-4.855706,-5.331908],[-5.851118,-7.421731,4.527336],[9.437602,-3.116676,-3.975265]],[[-8.347760,5.112014,0.818785],[1.006560,-4.501946,8.229366],[7.914394,-1.141345,-9.836214],[-3.211191,3.109185,-0.605163],[-9.113531,-9.788637,-1.318692],[9.477954,6.015919,6.778918],[-3.623958,3.070435,-5.109566],[7.597138,-6.679254,0.365535],[-2.205822,3.339313,-2.272656],[-6.298418,3.311308,4.416721],[7.612837,4.376140,0.102843],[-7.216164,3.909835,-0.934826],[-2.045581,-9.946887,-5.530134]],[[0.605234,5.188926,-5.611074],[-4.346321,-8.835132,8.538297],[0.146365,-2.787348,-6.754773],[-6.560020,3.267576,-8.835796],[5.314467,-9.691108,2.092596],[4.777357,5.110222,3.097015],[-9.627773,6.708982,-8.384750],[-8.488836,0.911034,-6.197129],[0.334705,-3.961694,-1.212188],[-7.888831,1.876868,0.741297],[8.914014,-5.206430,9.512703],[-5.833177,2.216329,6.608050],[8.607154,-5.176140,-7.157896]],[[-3.606849,3.859429,6.979453],[4.224998,3.421250,-0.392897],[-9.202918,4.155301,-6.581055],[-7.399506,-4.187418,-4.269399],[0.419753,8.034267,2.367498],[-6.538481,6.679438,-1.758737],[-2.431439,5.424614,3.386961],[-5.123690,9.864644,-0.267023],[9.238002,0.728608,-3.990525],[1.363988,5.849065,1.142385],[-8.156481,-8.833032,7.189777],[-5.488937,-9.195118,0.328810],[3.583255,8.639443,4.180757]],[[1.742768,6.099275,-2.298109],[-0.816514,3.824048,4.659127],[-8.742185,2.511090,0.576119],[-9.834787,-2.273409,0.436691],[-0.079236,8.666895,-5.789351],[5.875290,8.529401,-8.651865],[-1.948541,8.200634,-5.496986],[3.072844,7.233413,9.993168],[9.737602,-8.103064,-3.980891],[-7.729811,5.326782,6.347612],[-6.440745,8.684693,6.836563],[-2.572025,-8.524228,4.106269],[-0.259466,-3.752168,3.852260]],[[-5.435539,5.615401,-7.385587],[1.095560,-7.508001,5.069001],[-7.615547,-6.937538,2.081750],[5.000834,0.577348,-7.380153],[-8.151488,0.529932,-9.710929],[-8.016521,-3.635642,3.339779],[9.421433,8.220214,5.467371],[0.499684,-8.063729,0.449337],[0.358345,1.982123,9.295207],[-7.752963,-7.220349,-3.279425],[-1.574837,-8.480696,-9.317763],[-2.418678,-1.000388,9.687787],[-0.112005,0.906421,-7.964516]]], dtype = "float64")#candidate|5727|(11, 13, 3)|const|float64
var_5728 = relay.var("var_5728", dtype = "float64", shape = (11, 13, 3))#candidate|5728|(11, 13, 3)|var|float64
bop_5729 = relay.greater(const_5727.astype('bool'), relay.reshape(var_5728.astype('bool'), relay.shape_of(const_5727))) # shape=(11, 13, 3)
output = bop_5729
output2 = bop_5729
func_5732 = relay.Function([var_5728,], output)
mod['func_5732'] = func_5732
mod = relay.transform.InferType()(mod)
var_5733 = relay.var("var_5733", dtype = "float64", shape = (11, 13, 3))#candidate|5733|(11, 13, 3)|var|float64
output = func_5732(var_5733)
func_5734 = relay.Function([var_5733], output)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4748_call = mod.get_global_var('func_4748')
func_4749_call = mutated_mod.get_global_var('func_4749')
call_5749 = func_4748_call()
call_5750 = func_4748_call()
output = call_5749
output2 = call_5750
func_5756 = relay.Function([], output)
mod['func_5756'] = func_5756
mod = relay.transform.InferType()(mod)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5756_call = mutated_mod.get_global_var('func_5756')
call_5757 = func_5756_call()
output = call_5757
func_5758 = relay.Function([], output)
mutated_mod['func_5758'] = func_5758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3119_call = mod.get_global_var('func_3119')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_5866 = relay.TupleGetItem(func_3119_call(), 0)
call_5867 = relay.TupleGetItem(func_3121_call(), 0)
func_3597_call = mod.get_global_var('func_3597')
func_3599_call = mutated_mod.get_global_var('func_3599')
call_5877 = relay.TupleGetItem(func_3597_call(), 0)
call_5878 = relay.TupleGetItem(func_3599_call(), 0)
func_5590_call = mod.get_global_var('func_5590')
func_5591_call = mutated_mod.get_global_var('func_5591')
call_5884 = relay.TupleGetItem(func_5590_call(), 0)
call_5885 = relay.TupleGetItem(func_5591_call(), 0)
output = relay.Tuple([call_5866,call_5877,call_5884,])
output2 = relay.Tuple([call_5867,call_5878,call_5885,])
func_5892 = relay.Function([], output)
mod['func_5892'] = func_5892
mod = relay.transform.InferType()(mod)
output = func_5892()
func_5893 = relay.Function([], output)
mutated_mod['func_5893'] = func_5893
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5949 = relay.const([[[-2.730803,7.100180,4.576974,-6.683820,-9.614857,-4.030655,5.039875,3.226247,-9.633139,4.744001,9.744668,-9.244516,7.482900,5.317443,8.961104],[1.439359,-8.223329,-8.491441,-6.594677,9.582863,2.579066,-8.340667,-0.830318,-4.804412,-2.227799,-6.854634,-7.228362,9.555946,-2.325266,-7.032099],[4.042133,0.239657,-0.739971,-0.912731,-6.700314,1.624635,4.959241,-5.513082,3.068980,-3.567901,6.400773,6.693564,-6.811943,6.102933,4.441581],[-2.155600,6.018891,-5.937908,5.075894,-5.646339,-4.524699,4.065639,7.416679,5.969962,-8.820845,-7.220644,8.669208,7.073342,3.079623,-5.983365],[-7.933462,9.408943,-5.455692,2.156938,-3.815034,-4.944553,4.268433,3.955886,7.490437,6.807987,-7.943258,6.830901,0.563942,6.291154,7.683002],[-9.467105,-4.212385,2.774047,3.888553,-9.172589,7.298043,9.570715,-2.174068,3.074424,5.028180,-3.789376,4.805190,3.027578,-0.166903,6.241649],[-1.946528,-7.158206,7.516488,-3.899525,-8.940045,5.797215,6.338796,8.735165,6.463526,2.157014,5.963241,-7.830135,-8.392666,-0.948808,9.111019],[-3.092997,4.265550,-4.094921,4.771301,5.211287,-3.490823,8.985844,9.486885,6.345629,2.613005,-7.524760,-8.465638,2.272722,-4.824349,-2.660079],[5.494857,-8.009580,5.786102,-2.540792,0.243920,-0.030904,-8.435659,6.348243,-1.037763,-4.464607,1.384842,5.683361,2.437551,-5.096740,-1.172269],[6.529440,-2.098720,-2.676794,4.180985,-1.631305,-5.985838,-0.329147,-0.363536,5.019052,-8.232558,-3.550920,-0.921832,-9.873753,5.518224,9.890146],[2.841831,8.631886,-1.776935,5.840029,-5.013762,-2.707523,-8.692983,9.592750,-9.005736,-7.844855,-9.027007,1.217986,-0.373159,2.244034,-7.499711],[7.937527,4.977566,5.202817,-0.153833,3.185748,-0.779097,6.485094,-2.929912,1.158433,9.639387,-0.858395,1.934206,-3.556525,9.821572,2.118060],[1.789574,1.320210,0.958487,-7.695266,4.024276,9.197437,-8.415202,-8.737326,3.073286,3.337332,4.408869,9.263949,6.876616,-7.457333,9.483626],[7.543300,-7.958581,0.145549,3.341194,9.603869,-3.295893,3.286920,-3.384479,6.232619,4.528144,-6.075698,-8.067937,7.114442,-0.388884,-3.166290],[3.849129,-3.381986,-6.181483,-7.923635,6.052818,-8.506547,-0.849211,-8.093502,-1.046710,-7.619770,7.099713,-6.248122,-3.972939,7.488250,-4.600350],[-5.425543,1.256064,2.377334,6.726195,-0.090242,-1.348563,-5.534050,-5.557036,0.892419,-3.606753,-4.625200,-5.310290,-7.437621,6.354701,5.738803]],[[7.710690,8.531887,-3.214401,6.136917,-4.658593,5.058777,-9.231990,3.048463,-6.360329,0.184765,9.786141,-9.021045,2.237691,-9.630991,9.477139],[-2.792270,-2.002572,6.825147,-1.463232,-3.243963,-8.473855,1.532726,9.393282,9.400065,5.837142,-6.936564,3.140932,1.430187,8.951903,4.971596],[2.803892,-4.530926,8.075768,9.784573,-1.850907,9.521043,7.678903,0.438068,4.029466,-4.173128,-1.447724,9.038695,-7.390878,-8.247960,4.647919],[-9.113579,7.296113,-3.849453,-6.736058,-6.675750,8.472250,-6.874008,5.161455,3.421039,-2.747815,8.381457,-1.531194,-5.785410,8.282208,1.938194],[-3.316116,-5.451503,-0.713086,9.670653,-6.000789,3.635119,5.158286,-4.846933,5.964329,5.110524,8.364816,-8.112445,-2.502895,-8.324217,7.509101],[-0.040614,8.556520,3.582173,9.696933,6.214892,8.586484,0.972333,-9.580956,1.523303,5.294237,5.833781,6.031380,-7.215731,2.584061,-5.574386],[-8.571125,-6.505139,5.051050,8.629625,-1.246177,-5.310937,8.492707,-1.054141,4.905313,-5.662454,6.178369,7.492889,8.402388,-2.552485,4.940216],[-5.852292,5.981661,1.910988,-5.711203,3.397557,1.946679,-5.441343,2.385618,-6.469108,-2.899252,1.187252,2.274180,0.982356,-9.624175,9.096676],[-7.970634,-0.116797,-5.626362,-3.807170,-8.440773,-5.235150,0.386572,7.484012,2.287505,2.095177,-3.939463,6.067963,4.038465,-4.358563,-6.162187],[4.323558,9.619619,-6.991407,-3.254799,6.344941,-8.076977,-9.069224,-8.639255,-1.549194,-9.056594,-3.023765,-0.995119,-1.324564,-3.862930,-1.507669],[-3.938869,5.285025,2.069666,3.573445,-3.342254,-7.651349,-8.455190,-5.737301,-3.371978,5.347486,-4.501261,8.814000,8.284107,-5.776140,0.878111],[3.219454,7.329564,7.785777,-1.618665,-9.546691,5.731737,-6.494822,9.945205,4.464345,8.736217,-7.297182,-7.629165,9.502033,8.230625,0.683159],[-6.203750,-8.811994,2.682604,-4.918849,0.876538,-8.820148,1.576641,-7.059033,8.720688,9.396043,-7.508617,-8.179097,5.825248,6.548847,2.819374],[7.938031,5.578106,5.549876,-1.089002,-9.230553,-3.299728,-5.021687,5.348416,1.065109,-6.885567,-0.196903,-3.857568,6.630556,-3.342056,2.063922],[3.540068,9.730895,-6.462448,5.517280,-0.935510,-7.618892,-0.116213,-5.890143,-9.350474,-7.100535,-9.284827,9.186122,2.774831,0.348719,8.918491],[-6.062942,0.728200,5.685856,-5.548656,-5.943190,4.512288,-7.979835,-3.340579,6.542182,-8.131283,8.106318,-9.826650,5.718093,-9.929262,3.421739]],[[3.894069,-6.175234,1.634084,9.956377,7.013586,-6.891530,-9.237114,-5.129687,-0.864762,5.142165,-6.356486,5.083172,-3.796526,-5.864031,4.689823],[-7.430338,8.707018,-5.876982,9.956140,8.040690,7.589050,3.314622,-3.897523,-7.638295,7.648213,6.049980,5.001183,5.503124,2.217687,-4.548391],[0.546394,-5.228580,2.319836,-1.752625,-8.365308,2.743326,5.996648,9.321436,2.999182,-8.502619,-8.440855,-6.915273,9.173928,3.398110,7.774302],[6.282103,-1.173963,-8.590571,-6.706701,-7.067729,-6.326803,0.944400,-0.024603,0.940333,-8.851259,2.811901,6.968073,-0.074751,1.746965,4.925800],[3.346408,3.700221,-7.412524,-2.709735,-7.899127,4.351321,-4.209508,1.828490,-9.102732,-1.369071,-9.385985,6.385223,5.385934,-6.524360,2.447331],[-6.124791,4.803397,-9.657678,5.889681,-8.408841,-4.713202,-2.270626,-7.093957,2.920523,-9.933704,-5.161695,3.041436,-4.710352,4.235127,4.121558],[-6.674549,-2.973205,-3.208647,-0.105906,6.232918,5.076210,-2.765546,-2.772990,6.569187,6.306029,-2.775099,5.339299,5.102441,-6.151805,-8.829741],[8.845613,2.033509,-2.597942,3.538707,7.814678,-1.105640,-1.638146,-9.197465,9.978543,-5.658212,7.984145,-4.896086,8.925089,-9.810449,5.611956],[7.385165,-3.875167,-8.735512,-0.333034,1.732225,-7.489376,1.571633,-8.103778,8.203746,9.573321,1.639842,-5.156336,5.526666,2.605831,-8.970144],[4.680796,-3.802180,-8.162787,-6.418184,-8.985424,8.347451,9.505890,2.833810,-2.565257,-9.967694,-2.776430,3.390454,7.048508,-0.337122,-6.313877],[0.904497,4.866628,9.284772,-3.101608,-9.937249,2.611460,0.902366,-9.134626,0.410625,-4.699072,4.087666,5.128223,4.427499,5.985193,1.502953],[-2.555848,5.463353,-9.997068,-2.358703,5.286127,5.227938,-3.384511,4.528247,8.254473,3.228831,-8.583819,6.731918,0.284440,1.433046,-3.468203],[6.487338,8.879487,-1.796719,4.149827,8.364242,-9.632452,-9.791298,4.422300,9.883098,-9.961221,-4.886118,2.321732,-6.747237,7.746941,-7.998223],[-7.258406,-5.559334,-5.857418,-9.900077,9.253807,-6.569120,-1.239647,-8.856532,9.849130,0.573357,4.755627,-2.414760,5.146829,7.429139,-7.767426],[-8.035601,9.621701,6.753317,-8.339437,-0.835832,9.975877,0.616293,4.690244,2.662409,1.239337,-3.228956,8.268711,-7.507344,8.237438,9.228664],[3.691871,-0.677472,-4.409783,-9.766160,8.276453,3.441006,-1.380023,2.407397,-3.682272,-8.309183,6.629036,-7.925731,4.631440,5.276934,6.693007]],[[0.905441,-2.491125,9.802923,5.393117,4.591436,-6.909832,9.766945,7.130070,-1.903868,8.347061,-7.555814,3.350736,3.989874,4.677609,2.458789],[5.627504,5.456213,5.469400,5.767215,-5.996598,6.177272,6.809509,0.946208,5.181466,-6.025376,-4.141640,3.900137,-8.638125,3.686820,8.380591],[-9.813751,7.955743,0.806019,-5.648414,7.765937,0.390683,-5.377487,9.512287,-6.043644,7.171456,0.552545,9.161154,-3.025824,-6.061611,8.517448],[-6.061659,-5.884331,0.801208,-5.168362,-0.063673,-7.062215,8.394142,-7.308788,1.162331,4.775357,-3.020391,-3.037030,-4.897484,2.273818,-5.721989],[-2.882063,-6.823897,-2.541148,-3.631246,1.626186,-3.186722,6.261836,-0.895832,-5.904323,-3.318743,0.239575,8.137548,-9.745969,-8.615540,-3.851995],[-5.525782,5.937605,8.829309,-7.865865,2.874967,1.120366,1.123398,3.243723,-3.438434,3.548021,8.526454,9.937321,4.704395,-9.649826,6.251164],[-8.089088,-8.429756,-1.525889,-0.071868,1.067034,0.834593,2.576864,4.445231,-4.991588,8.907748,-5.639040,-7.405924,0.567551,3.372487,5.950158],[-0.767757,-8.312389,-1.676145,-7.573465,1.871363,-3.961640,-6.676908,-2.258390,-4.012408,-0.024357,-9.721693,-6.779422,-0.215153,-3.956307,-0.240504],[1.268121,-4.521075,3.040495,-5.341667,5.968144,5.031080,-0.359782,0.627597,-7.125847,-1.907280,8.727932,3.396969,1.836458,5.062795,-2.303349],[-5.228644,-8.670135,1.943482,5.983514,-0.249233,-9.806274,-5.933356,0.648197,1.745262,7.908449,-0.053264,-1.391971,-0.089835,-3.454301,-6.991786],[0.888846,-6.397137,6.931710,9.858910,7.766938,7.725161,-6.303909,2.768872,1.428537,6.748678,-6.252514,-6.194639,3.163907,-2.559140,-2.033292],[-8.050671,6.743143,-4.273967,3.689412,6.057577,4.308580,-8.237442,-3.468877,2.535921,-9.800093,-6.913740,4.909873,4.184804,-7.648691,-8.641891],[-9.497426,-4.592639,6.407752,-2.305071,2.248861,0.945395,-4.706836,-3.230140,9.147265,6.719324,-4.539475,-7.958456,-5.760753,-5.635435,-9.268557],[7.576838,-0.064364,-7.998893,-1.185771,-0.351656,3.641195,-0.215090,5.615191,-7.499901,2.451323,-5.947309,-3.496913,4.462363,-2.686249,0.399214],[-4.118878,-2.727096,-6.341266,-1.103730,7.641180,-4.396195,-8.536542,9.426416,7.157078,0.046259,9.949159,-7.362796,-0.785129,-3.459537,-2.079767],[5.785315,-3.966653,7.565415,6.785304,-5.821751,-6.450631,8.768683,0.008816,-0.489490,-6.460903,1.910583,0.440372,8.380650,1.706999,-8.003455]]], dtype = "float64")#candidate|5949|(4, 16, 15)|const|float64
uop_5950 = relay.log10(const_5949.astype('float64')) # shape=(4, 16, 15)
output = relay.Tuple([uop_5950,])
output2 = relay.Tuple([uop_5950,])
func_5953 = relay.Function([], output)
mod['func_5953'] = func_5953
mod = relay.transform.InferType()(mod)
mutated_mod['func_5953'] = func_5953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5953_call = mutated_mod.get_global_var('func_5953')
call_5954 = func_5953_call()
output = call_5954
func_5955 = relay.Function([], output)
mutated_mod['func_5955'] = func_5955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3597_call = mod.get_global_var('func_3597')
func_3599_call = mutated_mod.get_global_var('func_3599')
call_5967 = relay.TupleGetItem(func_3597_call(), 0)
call_5968 = relay.TupleGetItem(func_3599_call(), 0)
func_2987_call = mod.get_global_var('func_2987')
func_2991_call = mutated_mod.get_global_var('func_2991')
const_5976 = relay.const([10,-8,-2,-5,5,-2,-3,4,-3,6,5,-8,7,9,8,1,9,10,-8,-2,-8,9,7,-1,-2,-6,2,8,-6,5,-3,1,-6,7,6,8,2,-9,3,-3,-6,-4,5,-8,-10,-4,-7,-7,7,-6,-3,-9,4,-6,-8,5,-10,-10,10,-5,-3,5,3,5,-8,-3,7,-6,9,-9,-2,9], dtype = "uint16")#candidate|5976|(72,)|const|uint16
const_5977 = relay.const([[1.091823,3.284521,-5.801931,-0.047189,4.516449,1.376880,-6.615036,6.053018,5.194439],[6.052069,8.481942,-3.086962,-0.650082,0.666991,-9.023736,3.290965,3.126388,-2.619277],[-8.517907,6.345707,-8.593027,-4.037245,6.140134,-2.350025,-3.330566,-3.187493,-7.637636],[-4.216030,8.402171,1.011517,-8.394738,6.166402,6.996693,1.446511,-7.698574,9.244320],[-0.871318,8.323292,-9.203595,-6.090897,4.070301,-0.050699,4.769322,-6.357169,-0.610824],[-4.750901,3.086342,9.241039,0.421895,-6.820775,4.301621,8.691990,-4.274967,2.615602],[-2.573032,4.310563,9.410075,7.224728,-4.067997,6.824775,1.457809,4.522124,6.831752],[-2.561761,-3.981519,-3.125866,-7.108839,3.590800,-8.843635,1.724956,-8.779318,4.195701],[0.024983,6.105300,-0.042642,-6.296016,-6.775618,-9.814607,-0.562037,2.462567,-6.647776],[-6.722017,0.345267,2.401077,9.298974,-8.412930,8.498478,2.855296,-1.039562,-3.555041],[6.938223,-5.523547,4.948946,1.907983,2.839547,-3.272454,-4.640815,1.136360,-9.882763],[9.149415,1.202260,0.720615,9.745237,0.823910,6.930632,1.321691,7.198879,7.109824],[-3.904548,-6.740641,4.738317,6.979777,-9.117797,5.906590,3.770948,-0.694547,-5.775569],[8.106820,-8.996224,9.523428,6.580121,-2.299292,-3.259545,5.552452,-2.074806,0.583685],[-4.815179,2.869066,4.177699,6.646168,3.971466,4.127808,2.926499,-2.997674,-6.093536],[-2.856928,-3.142178,-7.302310,-5.033063,0.900942,5.359516,-4.496286,-5.147852,-4.893984],[-3.689536,-2.076044,2.493876,9.402358,6.801985,-7.896311,7.089958,1.654864,6.881523],[-1.041385,0.259618,-6.204012,-1.242527,-5.586818,-0.180050,-6.697589,-0.595057,0.557220],[7.450231,-2.109524,-2.357867,-7.458026,2.410969,0.966137,4.582830,-1.872929,0.950106],[0.813439,8.750058,-1.877345,3.936666,-6.071554,-7.362811,7.268126,-5.588856,-1.076527],[2.193308,-4.031633,-9.123575,6.215879,-3.463909,-6.491796,3.905509,7.442666,5.455586],[-4.390458,4.345298,-6.489930,-9.730187,1.284405,2.715581,2.311277,-6.759757,-2.368629],[4.165356,-7.394784,7.831383,-2.206889,-8.536792,-2.317589,2.713766,-7.825241,2.674202],[-0.590635,6.717238,5.730658,6.476325,2.334470,-8.439831,-0.901252,9.723049,9.699170],[3.586106,1.000710,-5.576514,0.985424,0.250703,-8.220394,-3.348399,-9.538739,-6.742044],[2.636875,1.396023,7.572852,-1.582312,8.157074,-7.284619,-7.226745,-1.590827,3.701622],[5.064209,4.532490,6.931052,-5.462879,-7.286708,4.014288,-6.615003,7.061854,7.355846],[4.741943,-7.062857,4.400257,-4.395096,3.822159,-6.105360,3.176123,1.863155,-9.668249],[-8.923679,7.175695,8.978553,6.204812,6.209627,1.566824,0.662243,-9.986216,-0.176434],[-0.496155,8.507116,4.290651,-9.640947,-8.401814,7.727416,-3.799402,0.004554,8.860051],[-0.554816,-4.258195,8.787273,-2.971946,-4.929969,-5.310849,8.177857,0.208388,-4.007669],[-8.616838,7.479808,8.496653,4.530141,-0.253234,4.442253,8.775408,-3.423631,5.342775],[-2.027259,-6.426578,-6.794095,4.397614,5.692730,-3.255006,0.336409,8.602371,7.339753],[-6.100915,-9.471353,7.687230,-5.249336,-2.874073,-4.548221,-6.697156,0.454926,-7.052625],[7.405000,8.180035,-4.289044,2.959510,-3.712889,9.028580,3.471825,-3.958460,-5.268524],[5.698392,9.771073,-1.872733,8.744451,-2.589773,0.632779,-1.646389,-4.326047,-3.684906],[8.847708,-8.744681,-2.639801,-9.329215,0.568617,7.658015,-2.332265,-3.392044,-0.369844],[-2.707340,6.068630,7.061403,5.652397,-2.263134,2.650656,-1.502889,-3.313980,9.585350],[-7.902562,-5.588969,-8.602309,-6.206026,-2.815983,-2.220184,3.382388,-1.713329,4.437128],[4.879679,9.090049,-4.267352,-0.669933,7.430299,-1.833849,7.188380,-8.186775,-6.746513],[-9.849177,-9.543545,-3.533527,8.599190,6.141207,-9.848227,3.439518,7.624967,8.364214],[-7.698555,-9.730583,-0.760854,-7.363827,-5.557550,6.033237,1.590945,8.535803,-2.249616],[1.534660,1.119773,5.673151,0.758906,7.688951,0.383128,8.347322,9.128020,-3.476094],[-7.004134,4.697994,7.820191,8.719253,-4.853951,-1.966346,-6.340536,6.967962,-2.514689],[-8.442786,0.660625,-1.088779,-9.671611,-5.529838,-9.798806,-1.703454,3.426902,8.258431]], dtype = "float64")#candidate|5977|(45, 9)|const|float64
call_5975 = relay.TupleGetItem(func_2987_call(relay.reshape(const_5976.astype('uint16'), [72,]), relay.reshape(const_5977.astype('float64'), [405,]), ), 0)
call_5978 = relay.TupleGetItem(func_2991_call(relay.reshape(const_5976.astype('uint16'), [72,]), relay.reshape(const_5977.astype('float64'), [405,]), ), 0)
func_3348_call = mod.get_global_var('func_3348')
func_3352_call = mutated_mod.get_global_var('func_3352')
const_6023 = relay.const([False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True], dtype = "bool")#candidate|6023|(88,)|const|bool
const_6024 = relay.const(2, dtype = "uint16")#candidate|6024|()|const|uint16
call_6022 = relay.TupleGetItem(func_3348_call(relay.reshape(const_6023.astype('bool'), [2, 44]), relay.reshape(const_6024.astype('uint16'), []), ), 0)
call_6025 = relay.TupleGetItem(func_3352_call(relay.reshape(const_6023.astype('bool'), [2, 44]), relay.reshape(const_6024.astype('uint16'), []), ), 0)
func_4419_call = mod.get_global_var('func_4419')
func_4421_call = mutated_mod.get_global_var('func_4421')
call_6030 = relay.TupleGetItem(func_4419_call(), 2)
call_6031 = relay.TupleGetItem(func_4421_call(), 2)
output = relay.Tuple([call_5967,call_5975,const_5976,const_5977,call_6022,const_6023,const_6024,call_6030,])
output2 = relay.Tuple([call_5968,call_5978,const_5976,const_5977,call_6025,const_6023,const_6024,call_6031,])
func_6037 = relay.Function([], output)
mod['func_6037'] = func_6037
mod = relay.transform.InferType()(mod)
mutated_mod['func_6037'] = func_6037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6037_call = mutated_mod.get_global_var('func_6037')
call_6038 = func_6037_call()
output = call_6038
func_6039 = relay.Function([], output)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6043 = relay.var("var_6043", dtype = "bool", shape = (4, 14, 5))#candidate|6043|(4, 14, 5)|var|bool
const_6044 = relay.const([[[True,True,True,True,False],[False,True,False,False,False],[False,True,True,True,False],[False,True,True,False,True],[True,True,False,True,True],[True,False,False,True,True],[True,False,False,False,False],[True,False,True,True,True],[False,False,False,True,True],[False,True,True,False,True],[False,True,False,False,False],[True,False,False,False,True],[True,True,False,False,True],[False,True,False,True,False]],[[True,True,False,True,True],[False,False,False,True,False],[False,True,True,False,True],[False,False,True,False,False],[True,False,True,True,False],[False,True,True,False,False],[True,True,False,False,True],[True,False,True,True,True],[True,True,False,False,False],[True,False,False,True,True],[False,False,True,True,True],[True,True,False,False,False],[False,True,True,False,True],[False,True,True,True,True]],[[False,False,False,False,True],[False,False,True,False,True],[False,False,True,True,True],[False,False,True,False,False],[True,False,False,False,True],[True,True,False,True,False],[True,True,True,False,False],[False,False,False,True,True],[True,False,True,False,True],[True,False,False,False,False],[False,True,False,False,True],[True,False,False,False,True],[True,True,False,False,True],[False,False,False,False,True]],[[True,True,True,False,True],[True,True,True,True,True],[True,True,False,False,False],[False,True,False,False,True],[True,True,True,True,True],[False,False,True,False,False],[True,True,False,False,False],[True,True,True,True,False],[True,False,False,True,False],[False,True,False,False,False],[True,True,True,False,False],[True,True,False,False,True],[True,True,True,True,False],[True,False,True,False,True]]], dtype = "bool")#candidate|6044|(4, 14, 5)|const|bool
bop_6045 = relay.logical_and(var_6043.astype('bool'), relay.reshape(const_6044.astype('bool'), relay.shape_of(var_6043))) # shape=(4, 14, 5)
uop_6055 = relay.sin(var_6043.astype('float64')) # shape=(4, 14, 5)
uop_6057 = relay.log10(bop_6045.astype('float64')) # shape=(4, 14, 5)
func_4080_call = mod.get_global_var('func_4080')
func_4084_call = mutated_mod.get_global_var('func_4084')
var_6066 = relay.var("var_6066", dtype = "float32", shape = (1, 13))#candidate|6066|(1, 13)|var|float32
const_6067 = relay.const([2,-8,1,-10,-2,2,-10,-1,-8,-5,6,-6,9,-9,1,6,5,2,7,3,-9,-5,1,-5,9,-3,8,-5,3,1,-5,7,-3,4,-1,7,3,10,-10,-2,4,1,-5,10,2,1,-10,-7,-9,3,9,3,-4,5,7,2,-5,5,1,7,7,-3,10,2,-1,1,-6,2,-7,-5,-6,-8,-10,-10,-10,-6,-7,-6,9,8,4,9,-6,-2,-10,9,-2,5,-4,4,-4,-1,-1,9,6,9,-9,-9,-1,-9,-6,5,7,-3,-6,3,9,-2,2,8,1,7,6,-4,-7,-8,-1,-2,-2,9,1,-8,5,-9,-1,4,-6,1,-7,1,-8,-8,1,-7,-4,-2,8,5,2,-2,-5,-7,9,3,5,-1,-4,-3,-8,7,-9,-7,3,-2,-8,-9,5,3,6,-2,-1,-5,4,9,10,-4,-9,8,4,6,-8,-4,3,-9,-5,-1,5,-3,-7,1,-10,-8,5,-10,8,3,-1,9,6,2,-8,-10,-10,-2,-7,4,-5,6,-8,10,-2,-2,-10,8,6,9,-4,6,4,-1,-10,-8,-9,6,-3,-5,-9,-2,5,-9,10,4,-9,-8,-8,-3,5,-3,8,-4,-6,-7,-4,-8,-9,-10,4,-10,2,-5,-6,9,10,8,1,-10,-10,4,6,-3,-10,3,-6,-7,1,-1,8,10,9,-5,-1,7,-2,7,6,4,-4,-10,-9,1,6,-9,-9,4,9,10,4,3,-2,-5,-10,-2,5,-5,8,-6,-7,1,-6,-5,4,-6,5,-2,10,3,6,8,-9,6,10,-4,-7,-2,9,7,-5,10,2,4,9,6,5,7,-7,-3,-6,-4,1,-5,5,4,5,-7,7,-3,-7,4,-2,-7,-5,-8,5,-2,-7,-9,-9,10,8,-2,-9,3,-5,9,7,8,4,3,-7,-8,-3,7,-1,-7,6,-3,-6,10,-1,-9,-5,-2,-3,10,3,-4,-4,-10,10,3,-9,-1,-1,6,-10,-4,-10,-5,5,-10,-3,5,-7,-2,4,-1,2,-8,2,8,-9,-10,1,1,-9,6,-7,-1,8,9,1,-7,-3,9,-10,-1,1,7,5,10,9,7,-7,-10,4,-8,-3,-7,9,4,-2,8,6,-5,-1,8,1,8,6,4,9,-2,-5,9,-4,3,7,9,-7,4,-3,10,8,1,-7,-3,-7,7,5,-5,-8,-6,2,-6,-2,-8,5,-9,7,-8,-7,9,3,5,3,-6,10,3,9,-2,-2,-8,-10,1,-10,-2,-7,10,-8,-9,-7,-9,8,3,-3,-8,7,3,4,-7,-10,-1,9,-8,-10,-7,3,6,-9,-9,-7,-9,-7,-4,-6,-5,-9,5,10,6,-2,7,-2,-7,3,5,-6,-4,7,-4,-10,-9,-5,-8,8,5,10,5,6,-7,1,10,-8,-10,4,-10,-1,5,3,-1,1,1,7,-5,10,-1,-4,8,-5,9,-10,-6,-7,-9,4,3,5,9,2,4,-6,10,-3,-3,7,-10,2,2,-6,-2,-2,-8,-9,-10,10,2,8,-7,-2,-3,-4,-8,6,-8,10,5,-2,-2,7,-1,-5,-3,7,-7,-2,-8,1,5,-3,-2,-2,6,9,7,9,2,-1,10,-7,-6,7,-7,7,8,6,6,8,-2,-9,2,6,-5,-1,6,-2,-8,6,7,-9,7,8,5,-5,-2,5,6,10,-2,-6,8,3,-7,1,-6,1,-8,-7,5,-2,-6,-3,-10,-4,3,-5,8,-6,8,-10,-10,10,-2,-2,6,-7,3,-7,-4,-7,2,9,9,6,-5,-4,9,-6,8,9,-4,-10,-8,-9,-9,9,-8,1,6,-9,-4,-7,-6,6,-2,9,3,10,8,2,-8,9,9], dtype = "uint16")#candidate|6067|(702,)|const|uint16
call_6065 = relay.TupleGetItem(func_4080_call(relay.reshape(var_6066.astype('float32'), [13,]), relay.reshape(const_6067.astype('uint16'), [702,]), ), 2)
call_6068 = relay.TupleGetItem(func_4084_call(relay.reshape(var_6066.astype('float32'), [13,]), relay.reshape(const_6067.astype('uint16'), [702,]), ), 2)
output = relay.Tuple([uop_6055,uop_6057,call_6065,var_6066,const_6067,])
output2 = relay.Tuple([uop_6055,uop_6057,call_6068,var_6066,const_6067,])
func_6072 = relay.Function([var_6043,var_6066,], output)
mod['func_6072'] = func_6072
mod = relay.transform.InferType()(mod)
var_6073 = relay.var("var_6073", dtype = "bool", shape = (4, 14, 5))#candidate|6073|(4, 14, 5)|var|bool
var_6074 = relay.var("var_6074", dtype = "float32", shape = (1, 13))#candidate|6074|(1, 13)|var|float32
output = func_6072(var_6073,var_6074,)
func_6075 = relay.Function([var_6073,var_6074,], output)
mutated_mod['func_6075'] = func_6075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4818_call = mod.get_global_var('func_4818')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_6105 = relay.TupleGetItem(func_4818_call(), 3)
call_6106 = relay.TupleGetItem(func_4820_call(), 3)
func_1337_call = mod.get_global_var('func_1337')
func_1340_call = mutated_mod.get_global_var('func_1340')
const_6124 = relay.const([-3.007605,2.593009,-7.789150,9.067152,-8.495427,-8.782680,2.201488,-6.998547,8.165099,-0.943729,-9.708642,5.785802,-0.659873,9.710321,4.951999,-0.788159,-1.792423,0.728529,-7.136891,4.309055,-2.298966,8.685381,-4.666975,8.623819,-0.490694,6.370074,-5.784410,-3.614709,6.554955,-3.434070,-2.964228,3.646212,3.371150,-2.582602,1.976647,-6.287796,5.890794,6.394646,0.945530,5.457327,-5.370712,8.028721,9.777062,1.333476,4.962482,9.538794,-8.394994,-1.293722,-8.702762,-5.046406,-9.924511,1.474494,-9.255575,1.968192,1.023056,8.293133,-4.808946,-4.905347,-4.743839,-0.373394,-7.091826,-7.477531,-7.799490,-0.500378,3.079120,-7.536734,0.171008,6.737620,-4.503986,1.060226,1.061618,-1.600270,6.830371,3.705702,-1.858205,-4.778128,0.264189,-0.487110,6.923764,-9.521007,9.538855,3.789275,-0.153635,-1.907592,7.404964,6.001751,-1.028377,-2.149968,-1.517215,2.405453,-6.121321,2.769517,-6.812095,2.784528,-5.425914,-7.253329,1.341544,-4.749754,-4.055248,-2.633445,6.680550,-8.634615,5.703637,6.740817,-7.135160,7.525981,-7.846885,7.283922,-4.655098,1.423961,-2.542414,-5.143875,9.277717,-9.413470,5.863828,7.637826,-7.114030,-0.299101,0.203689,4.775168,-8.129623,-1.176761,-3.017614,-5.602587,-7.984308,0.848873,3.022933,-1.271506,5.919480,0.385055,-6.239029,7.842531,-4.361121,-8.168807,2.262117,-2.557888,-2.330365,4.713852,-0.655351,4.558000,5.987965,0.388584,-2.430127,4.799589,-9.383361,-3.792240,1.096146,3.673810,5.597611,9.877883,-1.477002,9.197351,-4.667632,2.121252,-4.662796,-7.219010,2.145777,-6.825512,7.515641,4.898294,-3.962178,-9.808065,8.742581,-3.958278,-0.012371,-6.074612,6.588360,6.647713,-4.175363,-1.940911,-2.863364,-8.703366,-1.104679,8.066400,-6.915824,-1.196558,8.453895,-8.799176,-6.662204,2.380981,1.383826,1.194818,4.544723,-2.950578,4.387245,-8.554767,1.399069,-9.291627,-7.279889,-6.622777,-1.825763,9.026558,5.417962,9.219877,-5.039195,-8.069978,-2.028702,-8.935237,7.727496,8.102817,0.925482,-6.052977,-5.406332,9.158111,-4.093249,1.872909,-2.338198,-6.943587,-4.554002,7.277019,3.786064,-5.178468,-1.447714,9.273437,-4.399857,-6.752316,4.827730,-8.180254,3.973037,-7.697648,7.663329,2.393178,-6.930314,-0.781588,0.745131,-0.178173,8.145055,-0.750727,6.537806,2.531944,-7.881349,-0.287979,-9.724661,2.098671,-0.034804,-0.230731,2.057171,1.984489,4.492258,-2.717751,4.965191,7.951465,-1.917669,-7.456678,-8.659463,5.643452,-6.497090,-4.521168,-4.836381,-0.936540,9.090226,0.158246,-9.836353,-3.813453,-5.622191,-2.568739,5.103331,-2.732981,7.692738,-1.987490,7.719363,-7.600389,3.121785,-4.347503,-5.479059,-3.652028,1.394014,-2.002047,-1.206360,-7.546403,-1.470906,-1.577454,-4.353586,3.253802,-1.297654,5.603223,3.002889,4.402347,-2.192948,-6.864365,-6.759992,-8.519103,-8.854610,-9.378897,-1.057225,4.162959,0.101523,-9.355158,9.729483,-6.822896,1.255747,8.026211,5.245353,1.807306,-6.560975,9.385170,-2.862877,2.447021,-9.308657,3.361013,-3.053799,5.347163,1.778994,9.553774,6.771032,-4.980989,-9.403990,0.964241,-0.712089,0.117195,9.076530,8.475620,0.542788,-4.717905,-7.886949,-4.055210,2.381838,9.289291,7.930716,2.586617,-6.401334,-7.153399,0.311060,-6.208748,-5.281004,-4.223212,-1.600127,-9.131390,-7.372789,-1.499764,-9.926409,3.098132,-2.102195,-8.490185,-8.367775,3.936768,8.001278,8.875190,2.603022,-1.250863,8.250093,1.518781,2.987012,5.617972,7.926479,-0.626339,-9.164554,7.580274,-3.054496,5.324269,4.980035,0.058069,-3.047693,2.655316,1.834557,9.120002,-6.573101,-6.923063,-8.131298,-5.089667,5.064877,-4.951919,-4.083424,8.117402,9.762743,6.697973,7.300134,-5.595992,3.120015,2.136214,6.020920,-9.664717,-7.325270,0.732367,-5.772953,-1.949682,5.300060,-0.589169,-9.901747,-0.366608,-0.315175,-5.414724,0.529431,7.090676,-4.753245,8.620529,0.314553,2.440530,-4.161594,3.909274,-5.728737,2.562973,-8.943847,-2.223440,1.234961,-0.319480,-7.450269,0.175586,5.123470,9.719235,1.860158,-5.267259,-5.413603,-9.714717,-1.432368], dtype = "float32")#candidate|6124|(405,)|const|float32
call_6123 = relay.TupleGetItem(func_1337_call(relay.reshape(const_6124.astype('float32'), [15, 3, 9])), 0)
call_6125 = relay.TupleGetItem(func_1340_call(relay.reshape(const_6124.astype('float32'), [15, 3, 9])), 0)
output = relay.Tuple([call_6105,call_6123,const_6124,])
output2 = relay.Tuple([call_6106,call_6125,const_6124,])
func_6132 = relay.Function([], output)
mod['func_6132'] = func_6132
mod = relay.transform.InferType()(mod)
mutated_mod['func_6132'] = func_6132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6132_call = mutated_mod.get_global_var('func_6132')
call_6133 = func_6132_call()
output = call_6133
func_6134 = relay.Function([], output)
mutated_mod['func_6134'] = func_6134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4464_call = mod.get_global_var('func_4464')
func_4465_call = mutated_mod.get_global_var('func_4465')
call_6135 = func_4464_call()
call_6136 = func_4464_call()
func_1459_call = mod.get_global_var('func_1459')
func_1460_call = mutated_mod.get_global_var('func_1460')
call_6139 = relay.TupleGetItem(func_1459_call(), 3)
call_6140 = relay.TupleGetItem(func_1460_call(), 3)
output = relay.Tuple([call_6135,call_6139,])
output2 = relay.Tuple([call_6136,call_6140,])
func_6142 = relay.Function([], output)
mod['func_6142'] = func_6142
mod = relay.transform.InferType()(mod)
mutated_mod['func_6142'] = func_6142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6142_call = mutated_mod.get_global_var('func_6142')
call_6143 = func_6142_call()
output = call_6143
func_6144 = relay.Function([], output)
mutated_mod['func_6144'] = func_6144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6145 = relay.var("var_6145", dtype = "int16", shape = (1, 7))#candidate|6145|(1, 7)|var|int16
var_6146 = relay.var("var_6146", dtype = "int16", shape = (3, 7))#candidate|6146|(3, 7)|var|int16
bop_6147 = relay.greater_equal(var_6145.astype('bool'), var_6146.astype('bool')) # shape=(3, 7)
func_1859_call = mod.get_global_var('func_1859')
func_1860_call = mutated_mod.get_global_var('func_1860')
call_6168 = func_1859_call()
call_6169 = func_1859_call()
func_1042_call = mod.get_global_var('func_1042')
func_1045_call = mutated_mod.get_global_var('func_1045')
const_6182 = relay.const([-10,-2,10,-5,3,-2,-6,-3,8,-7,7,-10,1,4,-3,3,-7,6,-10,6,6,-8,-2,-1,-1,3,-10,-2,-4,6,-1,-1,-3,8,1,-9,-2,9,-10,-6,-1,-8,9,3,-8,3,7,8,4,-3,9,-9,-9,-9,-1,1,-2,-4,-10,-6,-3,8,6,9,-3,2,6,-7,2,-5,8,6,6,-3,-4,-7,-10,8,-10,-4,3,4,-1,-6,6,-7,-1,4,-2,4,-6,6,5,-3,-3,7], dtype = "uint8")#candidate|6182|(96,)|const|uint8
call_6181 = relay.TupleGetItem(func_1042_call(relay.reshape(const_6182.astype('uint8'), [3, 8, 4])), 0)
call_6183 = relay.TupleGetItem(func_1045_call(relay.reshape(const_6182.astype('uint8'), [3, 8, 4])), 0)
bop_6190 = relay.multiply(call_6181.astype('float64'), relay.reshape(const_6182.astype('float64'), relay.shape_of(call_6181))) # shape=(3, 8, 4)
bop_6193 = relay.multiply(call_6183.astype('float64'), relay.reshape(const_6182.astype('float64'), relay.shape_of(call_6183))) # shape=(3, 8, 4)
func_3236_call = mod.get_global_var('func_3236')
func_3240_call = mutated_mod.get_global_var('func_3240')
const_6202 = relay.const([-9.411412,-9.182423,-0.637010,2.352838,-7.806332,4.313978,8.824095,4.891611,1.284401,7.744236,-2.013474,2.649297,5.963448,7.018509,6.817140,1.089427,-7.623898,3.356997,-7.488937,-5.840714,8.694980,-0.852654,-9.075941,8.099068,-6.420041,-0.869314,6.373330,7.190598,0.719223,-1.645466,9.050983,2.103899,0.477331,-2.669783,5.571664,-8.441927,-2.626165,5.988295,-9.292493,6.553170,-9.306404,5.031971,7.712058,-2.652693,-3.907110,1.495080,-4.431093,3.466584,3.247777,-9.235586,-3.191218,-6.846199,6.356985,-6.612849,-5.410879,-1.998021,5.816662,-6.788092,-6.401483,9.930595,5.306246,-0.894204,9.335739,9.518849,2.465532,1.959704,-5.007400,-5.164358,-7.234786,9.146767,-7.170916,1.429057,-2.758432,-0.423742,-1.703037,3.706377,-3.400796,-6.189051,5.448452,7.048445,1.139124,-0.639660,-4.849879,2.408380,4.516640,6.859303,-3.861529,1.978968,-6.902809,2.263662,-9.699458,5.372492,-1.300316,-4.520080,9.620742,-9.693566,4.951305,3.822813,3.015327,-6.987352,5.560412,2.906968,-8.056953,-9.445658,-3.332588,1.321469,-6.539909,-3.989829,-7.674962,-9.230805,-5.878206,-3.068284,-9.252143,0.973207,-7.558922,-8.597980,5.760042,6.986124,1.328825,-8.908293,6.236093,-1.562671,-7.837056,-7.019926,6.992075,5.408974,5.653886,5.291458,5.807774,-7.281997,-6.890381,4.074567,-0.578916,8.887461,5.239919,6.246013,-2.269703,-6.222654,-1.164448,7.695601,-8.221923,0.357322,1.249727,9.446211,2.255643,-8.933697,-3.793135,4.115192,0.326288,-2.630883,1.045513,3.303207,0.995731,-3.303953,1.982540,-9.700571,-2.545993,6.946599,-0.858464,-4.924552,-6.344958,-4.834217,0.810659,0.430033,-8.284612,8.871790,-6.430516,4.432664,-5.756603,6.557680,-9.133884,2.988877,-8.941302,-6.553974,2.085127,-0.133179,4.294175,8.276171,4.856481,8.292419,-3.055986,4.325598,-7.203830,3.203857,-8.161453,-4.332737,-3.433408,-1.467997,-8.594645,2.402414,9.232478,-7.721417,-9.582845,5.790877,-3.282481,-3.710815,7.549442,0.445198,-6.175775,2.595143,-4.213980,4.923001,6.760339,0.670092,-6.226227,-0.962774,-0.048957,4.145475,-5.200442,-5.481405,8.256002,6.574458,-4.484308,-8.495864,3.289678,-6.103494,9.452914,-9.655066,6.717559,2.050862,0.874699,4.582495,-0.634051,-1.187258,-9.030792,4.755505,0.434757,-1.639704,-9.257713,9.695313,-5.592771,3.385259,1.278049,1.976134,8.937608,0.368965,-9.498145,-0.578165,9.767637,7.016015], dtype = "float32")#candidate|6202|(240,)|const|float32
call_6201 = relay.TupleGetItem(func_3236_call(relay.reshape(const_6202.astype('float32'), [15, 16]), relay.reshape(const_6202.astype('float32'), [15, 16]), ), 0)
call_6203 = relay.TupleGetItem(func_3240_call(relay.reshape(const_6202.astype('float32'), [15, 16]), relay.reshape(const_6202.astype('float32'), [15, 16]), ), 0)
output = relay.Tuple([bop_6147,call_6168,bop_6190,call_6201,const_6202,])
output2 = relay.Tuple([bop_6147,call_6169,bop_6193,call_6203,const_6202,])
func_6222 = relay.Function([var_6145,var_6146,], output)
mod['func_6222'] = func_6222
mod = relay.transform.InferType()(mod)
mutated_mod['func_6222'] = func_6222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6222_call = mutated_mod.get_global_var('func_6222')
var_6224 = relay.var("var_6224", dtype = "int16", shape = (1, 7))#candidate|6224|(1, 7)|var|int16
var_6225 = relay.var("var_6225", dtype = "int16", shape = (3, 7))#candidate|6225|(3, 7)|var|int16
call_6223 = func_6222_call(var_6224,var_6225,)
output = call_6223
func_6226 = relay.Function([var_6224,var_6225,], output)
mutated_mod['func_6226'] = func_6226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3808_call = mod.get_global_var('func_3808')
func_3810_call = mutated_mod.get_global_var('func_3810')
call_6260 = relay.TupleGetItem(func_3808_call(), 0)
call_6261 = relay.TupleGetItem(func_3810_call(), 0)
func_6132_call = mod.get_global_var('func_6132')
func_6134_call = mutated_mod.get_global_var('func_6134')
call_6282 = relay.TupleGetItem(func_6132_call(), 1)
call_6283 = relay.TupleGetItem(func_6134_call(), 1)
output = relay.Tuple([call_6260,call_6282,])
output2 = relay.Tuple([call_6261,call_6283,])
func_6296 = relay.Function([], output)
mod['func_6296'] = func_6296
mod = relay.transform.InferType()(mod)
output = func_6296()
func_6297 = relay.Function([], output)
mutated_mod['func_6297'] = func_6297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1717_call = mod.get_global_var('func_1717')
func_1718_call = mutated_mod.get_global_var('func_1718')
call_6300 = relay.TupleGetItem(func_1717_call(), 1)
call_6301 = relay.TupleGetItem(func_1718_call(), 1)
var_6311 = relay.var("var_6311", dtype = "bool", shape = (6, 8, 11))#candidate|6311|(6, 8, 11)|var|bool
bop_6312 = relay.subtract(call_6300.astype('int32'), relay.reshape(var_6311.astype('int32'), relay.shape_of(call_6300))) # shape=(6, 8, 11)
bop_6315 = relay.subtract(call_6301.astype('int32'), relay.reshape(var_6311.astype('int32'), relay.shape_of(call_6301))) # shape=(6, 8, 11)
output = bop_6312
output2 = bop_6315
func_6316 = relay.Function([var_6311,], output)
mod['func_6316'] = func_6316
mod = relay.transform.InferType()(mod)
mutated_mod['func_6316'] = func_6316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6317 = relay.var("var_6317", dtype = "bool", shape = (6, 8, 11))#candidate|6317|(6, 8, 11)|var|bool
func_6316_call = mutated_mod.get_global_var('func_6316')
call_6318 = func_6316_call(var_6317)
output = call_6318
func_6319 = relay.Function([var_6317], output)
mutated_mod['func_6319'] = func_6319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6037_call = mod.get_global_var('func_6037')
func_6039_call = mutated_mod.get_global_var('func_6039')
call_6341 = relay.TupleGetItem(func_6037_call(), 5)
call_6342 = relay.TupleGetItem(func_6039_call(), 5)
output = relay.Tuple([call_6341,])
output2 = relay.Tuple([call_6342,])
func_6367 = relay.Function([], output)
mod['func_6367'] = func_6367
mod = relay.transform.InferType()(mod)
output = func_6367()
func_6368 = relay.Function([], output)
mutated_mod['func_6368'] = func_6368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4166_call = mutated_mod.get_global_var('func_4166')
call_6412 = relay.TupleGetItem(func_4165_call(), 0)
call_6413 = relay.TupleGetItem(func_4166_call(), 0)
output = call_6412
output2 = call_6413
func_6422 = relay.Function([], output)
mod['func_6422'] = func_6422
mod = relay.transform.InferType()(mod)
mutated_mod['func_6422'] = func_6422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6422_call = mutated_mod.get_global_var('func_6422')
call_6423 = func_6422_call()
output = call_6423
func_6424 = relay.Function([], output)
mutated_mod['func_6424'] = func_6424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6451 = relay.var("var_6451", dtype = "float64", shape = (7, 9, 11))#candidate|6451|(7, 9, 11)|var|float64
uop_6452 = relay.sqrt(var_6451.astype('float64')) # shape=(7, 9, 11)
func_1337_call = mod.get_global_var('func_1337')
func_1340_call = mutated_mod.get_global_var('func_1340')
const_6457 = relay.const([[6.279538],[6.017010],[7.914704],[-8.209814],[4.199675],[0.087371],[8.603487],[-8.421874],[3.349569],[-1.406053],[7.396377],[0.802527],[3.717592],[-3.148157],[8.745410],[4.069249],[-8.014230],[6.402672],[2.613222],[-0.689368],[0.362763],[-1.601680],[-3.237351],[4.564439],[-1.268390],[1.709602],[-8.133909],[-3.337180],[7.096395],[8.722778],[6.391848],[7.298016],[9.470451],[-3.713310],[-3.765825],[-3.424130],[-6.659312],[9.155748],[2.825235],[6.184891],[-8.640196],[-1.399529],[9.692173],[-2.348786],[0.336844],[-1.346124],[-7.011908],[-5.938490],[-0.156563],[-9.330038],[3.450240],[-9.738133],[-6.817478],[0.681598],[-3.712828],[2.988610],[7.419214],[6.033569],[-4.620904],[6.733648],[-3.688570],[8.996711],[1.641068],[-2.379817],[-5.607995],[6.797134],[2.736743],[9.760367],[2.493670],[-2.481381],[0.842266],[-4.530903],[1.575024],[-8.930050],[7.324333],[9.458246],[0.719717],[-6.281383],[-1.959928],[-8.838149],[9.324081],[-4.415694],[1.957919],[-1.887600],[-6.288426],[-9.056469],[3.600149],[-1.483711],[-4.304842],[-9.733524],[-5.866709],[7.071865],[-0.347662],[7.179835],[6.551712],[5.637151],[9.728772],[6.727552],[-9.777096],[5.229194],[-4.241668],[-9.446783],[-7.181446],[-4.548825],[6.574774],[-9.561922],[-2.208673],[1.906684],[5.777957],[6.105497],[-3.862940],[3.852074],[2.475302],[-0.622881],[9.189060],[-9.305838],[0.181263],[9.199602],[-7.696928],[2.544245],[-9.361550],[1.378785],[8.708112],[-7.625994],[2.302366],[6.373981],[-3.764381],[2.734475],[-7.866674],[0.598468],[8.639257],[4.570347],[5.635977],[-3.047776],[9.530815],[0.956551],[1.589024],[-3.544365],[-4.826627],[6.057981],[3.695566],[9.646406],[-9.813984],[8.219041],[5.664619],[-0.025470],[-3.230263],[2.536378],[-7.289581],[0.700007],[0.525457],[9.865903],[-5.363815],[-2.062398],[-2.056123],[-8.172626],[-2.121832],[-6.707494],[2.415933],[7.454617],[-1.191824],[6.700493],[-6.222400],[-2.001273],[6.137581],[-0.258064],[3.128792],[9.673265],[2.816237],[-5.576726],[-5.197507],[9.716984],[-3.764639],[2.945098],[9.812475],[-0.556363],[-2.128344],[1.809454],[1.855701],[9.041893],[7.576744],[1.418549],[1.440804],[-7.838337],[-7.805370],[3.247595],[-2.199544],[-9.357237],[-6.891348],[-2.077167],[-1.420567],[7.274496],[-0.362947],[8.460652],[5.634731],[-6.996532],[-7.125660],[5.087758],[2.538432],[3.107765],[-0.528059],[-7.309883],[6.575302],[5.716154],[-5.845016],[-0.735848],[2.441711],[7.855296],[-5.359829],[3.264940],[1.049651],[-2.904633],[6.982175],[0.044475],[-0.891102],[4.233765],[5.968093],[4.668312],[-8.010907],[-4.994993],[-6.118038],[4.181429],[0.868250],[4.968079],[-7.215003],[1.049538],[5.576716],[7.937507],[6.930371],[2.780248],[7.783940],[-9.468742],[-7.709059],[-4.575936],[-2.593887],[7.385851],[8.500667],[-8.472165],[6.861093],[-4.514479],[-9.452509],[9.663568],[8.301888],[7.595662],[5.729510],[-0.782551],[7.288666],[-0.264684],[-6.526050],[-6.693686],[2.265468],[1.678856],[-3.730173],[1.030179],[-6.281308],[6.435483],[0.431293],[-3.213422],[-4.642317],[1.572053],[-3.663374],[-2.625298],[-1.840403],[2.647592],[5.233980],[-4.148466],[5.477651],[8.773437],[4.654348],[9.299703],[-1.905244],[4.730309],[5.745730],[9.274609],[1.941731],[3.530896],[-0.274571],[3.617662],[-3.392339],[-0.091564],[-1.888868],[9.016246],[-9.670277],[1.217052],[2.747506],[5.157024],[-2.772600],[-9.632493],[-9.607220],[6.109878],[-6.405895],[8.974017],[-9.676668],[-7.901309],[3.898119],[8.840254],[6.183648],[5.618475],[5.878584],[2.377543],[7.253704],[8.559318],[5.919644],[3.924147],[1.305109],[8.854378],[-1.357204],[-7.190853],[9.070081],[4.604932],[4.289697],[-4.526056],[1.718651],[2.215847],[4.080068],[-3.774545],[3.425720],[-9.962592],[6.920612],[0.037457],[-6.279980],[-3.357519],[9.219973],[0.303136],[8.497910],[-5.063225],[1.223738],[2.244227],[-1.159441],[-2.165719],[-9.981272],[9.868233],[-1.743942],[-4.846148],[9.252540],[-3.166073],[2.889864],[-7.549086],[7.594202],[3.345520],[9.611134],[-0.493460],[6.684082],[9.673847],[-0.053959],[0.039889],[-6.123913],[-9.295432],[-2.926004],[-0.357028],[-3.844356],[3.680299],[-5.830079],[2.631764],[3.907590],[-6.597137],[-4.383597],[-1.994920],[3.175114],[8.953267],[9.084430],[-1.052419],[4.082819],[-3.342868],[8.182193],[-1.044189],[1.576611],[5.220441],[0.047291],[8.258764],[-1.727959],[9.025520],[-2.183630],[-2.802934],[-1.422257],[3.601099],[-8.101037],[3.694851],[9.030837],[2.886349],[5.270214],[-1.078398],[6.517550],[-9.126489],[-2.168000],[7.036271],[5.835415],[9.411646],[-7.065580],[3.607137],[-3.529335],[-5.553255],[-9.968469],[-3.688391],[5.116815],[9.782889],[1.032623],[8.994198],[0.350390],[-8.032931],[-4.931882],[-1.905214],[-1.588582],[5.358160],[7.896274]], dtype = "float32")#candidate|6457|(405, 1)|const|float32
call_6456 = relay.TupleGetItem(func_1337_call(relay.reshape(const_6457.astype('float32'), [15, 3, 9])), 1)
call_6458 = relay.TupleGetItem(func_1340_call(relay.reshape(const_6457.astype('float32'), [15, 3, 9])), 1)
uop_6464 = relay.cosh(uop_6452.astype('float32')) # shape=(7, 9, 11)
output = relay.Tuple([call_6456,const_6457,uop_6464,])
output2 = relay.Tuple([call_6458,const_6457,uop_6464,])
func_6472 = relay.Function([var_6451,], output)
mod['func_6472'] = func_6472
mod = relay.transform.InferType()(mod)
var_6473 = relay.var("var_6473", dtype = "float64", shape = (7, 9, 11))#candidate|6473|(7, 9, 11)|var|float64
output = func_6472(var_6473)
func_6474 = relay.Function([var_6473], output)
mutated_mod['func_6474'] = func_6474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_6494 = func_1571_call()
call_6495 = func_1571_call()
func_4748_call = mod.get_global_var('func_4748')
func_4749_call = mutated_mod.get_global_var('func_4749')
call_6502 = func_4748_call()
call_6503 = func_4748_call()
output = relay.Tuple([call_6494,call_6502,])
output2 = relay.Tuple([call_6495,call_6503,])
func_6507 = relay.Function([], output)
mod['func_6507'] = func_6507
mod = relay.transform.InferType()(mod)
output = func_6507()
func_6508 = relay.Function([], output)
mutated_mod['func_6508'] = func_6508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mod.get_global_var('func_2419')
func_2420_call = mutated_mod.get_global_var('func_2420')
call_6511 = relay.TupleGetItem(func_2419_call(), 0)
call_6512 = relay.TupleGetItem(func_2420_call(), 0)
output = relay.Tuple([call_6511,])
output2 = relay.Tuple([call_6512,])
func_6540 = relay.Function([], output)
mod['func_6540'] = func_6540
mod = relay.transform.InferType()(mod)
mutated_mod['func_6540'] = func_6540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6540_call = mutated_mod.get_global_var('func_6540')
call_6541 = func_6540_call()
output = call_6541
func_6542 = relay.Function([], output)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4534_call = mod.get_global_var('func_4534')
func_4535_call = mutated_mod.get_global_var('func_4535')
call_6543 = relay.TupleGetItem(func_4534_call(), 0)
call_6544 = relay.TupleGetItem(func_4535_call(), 0)
output = relay.Tuple([call_6543,])
output2 = relay.Tuple([call_6544,])
func_6551 = relay.Function([], output)
mod['func_6551'] = func_6551
mod = relay.transform.InferType()(mod)
output = func_6551()
func_6552 = relay.Function([], output)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_6566 = func_1571_call()
call_6567 = func_1571_call()
output = call_6566
output2 = call_6567
func_6584 = relay.Function([], output)
mod['func_6584'] = func_6584
mod = relay.transform.InferType()(mod)
mutated_mod['func_6584'] = func_6584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6584_call = mutated_mod.get_global_var('func_6584')
call_6585 = func_6584_call()
output = call_6585
func_6586 = relay.Function([], output)
mutated_mod['func_6586'] = func_6586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4818_call = mod.get_global_var('func_4818')
func_4820_call = mutated_mod.get_global_var('func_4820')
call_6647 = relay.TupleGetItem(func_4818_call(), 2)
call_6648 = relay.TupleGetItem(func_4820_call(), 2)
func_4198_call = mod.get_global_var('func_4198')
func_4199_call = mutated_mod.get_global_var('func_4199')
call_6649 = relay.TupleGetItem(func_4198_call(), 0)
call_6650 = relay.TupleGetItem(func_4199_call(), 0)
output = relay.Tuple([call_6647,call_6649,])
output2 = relay.Tuple([call_6648,call_6650,])
func_6658 = relay.Function([], output)
mod['func_6658'] = func_6658
mod = relay.transform.InferType()(mod)
output = func_6658()
func_6659 = relay.Function([], output)
mutated_mod['func_6659'] = func_6659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4748_call = mod.get_global_var('func_4748')
func_4749_call = mutated_mod.get_global_var('func_4749')
call_6700 = func_4748_call()
call_6701 = func_4748_call()
func_2886_call = mod.get_global_var('func_2886')
func_2890_call = mutated_mod.get_global_var('func_2890')
var_6736 = relay.var("var_6736", dtype = "float32", shape = (13,))#candidate|6736|(13,)|var|float32
var_6737 = relay.var("var_6737", dtype = "uint16", shape = (405,))#candidate|6737|(405,)|var|uint16
call_6735 = relay.TupleGetItem(func_2886_call(relay.reshape(var_6736.astype('float32'), [13,]), relay.reshape(var_6737.astype('uint16'), [15, 3, 9]), ), 2)
call_6738 = relay.TupleGetItem(func_2890_call(relay.reshape(var_6736.astype('float32'), [13,]), relay.reshape(var_6737.astype('uint16'), [15, 3, 9]), ), 2)
output = relay.Tuple([call_6700,call_6735,var_6736,var_6737,])
output2 = relay.Tuple([call_6701,call_6738,var_6736,var_6737,])
func_6743 = relay.Function([var_6736,var_6737,], output)
mod['func_6743'] = func_6743
mod = relay.transform.InferType()(mod)
var_6744 = relay.var("var_6744", dtype = "float32", shape = (13,))#candidate|6744|(13,)|var|float32
var_6745 = relay.var("var_6745", dtype = "uint16", shape = (405,))#candidate|6745|(405,)|var|uint16
output = func_6743(var_6744,var_6745,)
func_6746 = relay.Function([var_6744,var_6745,], output)
mutated_mod['func_6746'] = func_6746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6540_call = mod.get_global_var('func_6540')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_6748 = relay.TupleGetItem(func_6540_call(), 0)
call_6749 = relay.TupleGetItem(func_6542_call(), 0)
func_4534_call = mod.get_global_var('func_4534')
func_4535_call = mutated_mod.get_global_var('func_4535')
call_6762 = relay.TupleGetItem(func_4534_call(), 0)
call_6763 = relay.TupleGetItem(func_4535_call(), 0)
func_4517_call = mod.get_global_var('func_4517')
func_4519_call = mutated_mod.get_global_var('func_4519')
call_6765 = func_4517_call()
call_6766 = func_4517_call()
output = relay.Tuple([call_6748,call_6762,call_6765,])
output2 = relay.Tuple([call_6749,call_6763,call_6766,])
func_6776 = relay.Function([], output)
mod['func_6776'] = func_6776
mod = relay.transform.InferType()(mod)
mutated_mod['func_6776'] = func_6776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6776_call = mutated_mod.get_global_var('func_6776')
call_6777 = func_6776_call()
output = call_6777
func_6778 = relay.Function([], output)
mutated_mod['func_6778'] = func_6778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4981_call = mod.get_global_var('func_4981')
func_4982_call = mutated_mod.get_global_var('func_4982')
call_6823 = relay.TupleGetItem(func_4981_call(), 0)
call_6824 = relay.TupleGetItem(func_4982_call(), 0)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_6825 = func_3316_call()
call_6826 = func_3316_call()
output = relay.Tuple([call_6823,call_6825,])
output2 = relay.Tuple([call_6824,call_6826,])
func_6831 = relay.Function([], output)
mod['func_6831'] = func_6831
mod = relay.transform.InferType()(mod)
output = func_6831()
func_6832 = relay.Function([], output)
mutated_mod['func_6832'] = func_6832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1291_call = mod.get_global_var('func_1291')
func_1292_call = mutated_mod.get_global_var('func_1292')
call_6853 = func_1291_call()
call_6854 = func_1291_call()
output = call_6853
output2 = call_6854
func_6861 = relay.Function([], output)
mod['func_6861'] = func_6861
mod = relay.transform.InferType()(mod)
mutated_mod['func_6861'] = func_6861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6861_call = mutated_mod.get_global_var('func_6861')
call_6862 = func_6861_call()
output = call_6862
func_6863 = relay.Function([], output)
mutated_mod['func_6863'] = func_6863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mod.get_global_var('func_2419')
func_2420_call = mutated_mod.get_global_var('func_2420')
call_6883 = relay.TupleGetItem(func_2419_call(), 0)
call_6884 = relay.TupleGetItem(func_2420_call(), 0)
func_1459_call = mod.get_global_var('func_1459')
func_1460_call = mutated_mod.get_global_var('func_1460')
call_6891 = relay.TupleGetItem(func_1459_call(), 2)
call_6892 = relay.TupleGetItem(func_1460_call(), 2)
output = relay.Tuple([call_6883,call_6891,])
output2 = relay.Tuple([call_6884,call_6892,])
func_6895 = relay.Function([], output)
mod['func_6895'] = func_6895
mod = relay.transform.InferType()(mod)
output = func_6895()
func_6896 = relay.Function([], output)
mutated_mod['func_6896'] = func_6896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4166_call = mutated_mod.get_global_var('func_4166')
call_6912 = relay.TupleGetItem(func_4165_call(), 0)
call_6913 = relay.TupleGetItem(func_4166_call(), 0)
func_3348_call = mod.get_global_var('func_3348')
func_3352_call = mutated_mod.get_global_var('func_3352')
const_6959 = relay.const([False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True], dtype = "bool")#candidate|6959|(88,)|const|bool
const_6960 = relay.const(-7, dtype = "uint16")#candidate|6960|()|const|uint16
call_6958 = relay.TupleGetItem(func_3348_call(relay.reshape(const_6959.astype('bool'), [2, 44]), relay.reshape(const_6960.astype('uint16'), []), ), 4)
call_6961 = relay.TupleGetItem(func_3352_call(relay.reshape(const_6959.astype('bool'), [2, 44]), relay.reshape(const_6960.astype('uint16'), []), ), 4)
output = relay.Tuple([call_6912,call_6958,const_6959,const_6960,])
output2 = relay.Tuple([call_6913,call_6961,const_6959,const_6960,])
func_6964 = relay.Function([], output)
mod['func_6964'] = func_6964
mod = relay.transform.InferType()(mod)
output = func_6964()
func_6965 = relay.Function([], output)
mutated_mod['func_6965'] = func_6965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4534_call = mod.get_global_var('func_4534')
func_4535_call = mutated_mod.get_global_var('func_4535')
call_6969 = relay.TupleGetItem(func_4534_call(), 0)
call_6970 = relay.TupleGetItem(func_4535_call(), 0)
func_68_call = mod.get_global_var('func_68')
func_71_call = mutated_mod.get_global_var('func_71')
const_6976 = relay.const([[-3.582158,-7.119638,-4.259459,-9.878109,6.073407,2.313265,-2.822449,5.652533,4.419875,5.916314,7.618682,6.807348,8.836375]], dtype = "float32")#candidate|6976|(1, 13)|const|float32
call_6975 = relay.TupleGetItem(func_68_call(relay.reshape(const_6976.astype('float32'), [13, 1])), 0)
call_6977 = relay.TupleGetItem(func_71_call(relay.reshape(const_6976.astype('float32'), [13, 1])), 0)
output = relay.Tuple([call_6969,call_6975,const_6976,])
output2 = relay.Tuple([call_6970,call_6977,const_6976,])
func_6978 = relay.Function([], output)
mod['func_6978'] = func_6978
mod = relay.transform.InferType()(mod)
output = func_6978()
func_6979 = relay.Function([], output)
mutated_mod['func_6979'] = func_6979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6986 = relay.var("var_6986", dtype = "uint8", shape = ())#candidate|6986|()|var|uint8
var_6987 = relay.var("var_6987", dtype = "uint8", shape = (1, 13))#candidate|6987|(1, 13)|var|uint8
bop_6988 = relay.add(var_6986.astype('uint8'), var_6987.astype('uint8')) # shape=(1, 13)
func_1923_call = mod.get_global_var('func_1923')
func_1925_call = mutated_mod.get_global_var('func_1925')
call_6996 = relay.TupleGetItem(func_1923_call(), 0)
call_6997 = relay.TupleGetItem(func_1925_call(), 0)
output = relay.Tuple([bop_6988,call_6996,])
output2 = relay.Tuple([bop_6988,call_6997,])
func_7001 = relay.Function([var_6986,var_6987,], output)
mod['func_7001'] = func_7001
mod = relay.transform.InferType()(mod)
var_7002 = relay.var("var_7002", dtype = "uint8", shape = ())#candidate|7002|()|var|uint8
var_7003 = relay.var("var_7003", dtype = "uint8", shape = (1, 13))#candidate|7003|(1, 13)|var|uint8
output = func_7001(var_7002,var_7003,)
func_7004 = relay.Function([var_7002,var_7003,], output)
mutated_mod['func_7004'] = func_7004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7033 = relay.var("var_7033", dtype = "float64", shape = (6, 7, 5))#candidate|7033|(6, 7, 5)|var|float64
const_7034 = relay.const([[[-6.448012,7.110600,8.444016,2.881084,9.406701],[-1.535021,4.345695,9.590778,6.341323,-7.352304],[8.589032,6.878044,-6.292653,-1.288439,-4.220394],[6.186860,-1.239199,7.456631,3.699820,-6.294431],[0.725578,-3.982106,5.410733,-2.588451,-1.748098],[-6.230669,-4.339610,4.068635,-6.485351,-2.931249],[4.350112,-4.941452,-9.782916,7.651332,-1.253963]],[[-7.165690,9.800130,-5.961735,5.958544,9.174334],[2.860606,2.636667,2.862272,4.086357,-0.118023],[7.990489,5.237679,-9.591232,5.372951,9.795078],[8.853533,9.135354,-9.404564,-0.438687,3.219126],[5.742514,6.535228,-3.300397,8.464378,2.225628],[4.370053,8.165703,-3.499032,6.106337,-4.223192],[2.524698,-0.788869,-3.175161,-1.926784,-5.312073]],[[-5.191834,-7.020182,-2.861342,-1.171802,-6.660046],[-5.191626,-9.073792,-6.956076,7.559652,-9.500556],[-3.753910,6.727056,8.135391,6.727142,-0.934806],[2.854308,-3.229721,9.073781,-1.932107,-6.529103],[2.265264,-2.495662,4.101842,-7.053523,-0.288982],[-9.146321,-9.718348,-7.498117,7.745605,9.007340],[8.650979,-9.074602,-7.849027,9.494236,2.471146]],[[-6.083305,-6.579548,1.852047,5.126022,-4.583367],[-2.304445,7.247706,-0.749150,-0.190151,8.924055],[-4.653755,-7.363717,-1.197602,-9.215061,2.916454],[-2.629398,-6.386672,7.150181,-7.994513,5.138503],[-8.392657,0.668791,-3.332642,9.640015,7.394139],[-8.569276,-1.189668,-2.951714,8.749103,-6.052250],[-4.502720,-4.548373,4.632877,-2.316888,5.932098]],[[-6.476827,-5.751945,9.660283,5.878731,2.843347],[6.818498,-2.119065,5.309548,0.911629,4.299625],[0.534863,-7.255396,-2.063098,1.992578,4.844752],[-2.640811,8.365330,7.248004,1.855905,5.760356],[5.502232,-3.131213,-6.612636,-8.105398,6.154001],[4.424025,4.343682,-5.149491,3.877209,7.201957],[-3.255900,-2.258303,-0.750995,-5.291280,9.366578]],[[-2.822358,1.334628,-8.082957,-6.593846,7.448300],[7.156272,3.816561,-9.627936,-2.472209,7.829779],[-8.528027,-9.530385,0.819706,-5.842516,-3.807878],[-5.788688,-7.973229,-8.403137,9.004323,1.672210],[-1.884081,-2.499565,3.361826,0.513599,-5.254774],[6.165712,0.409455,-7.029324,-5.515811,-7.860444],[-8.667283,-7.856481,-7.022104,3.659452,2.560265]]], dtype = "float64")#candidate|7034|(6, 7, 5)|const|float64
bop_7035 = relay.floor_mod(var_7033.astype('float64'), relay.reshape(const_7034.astype('float64'), relay.shape_of(var_7033))) # shape=(6, 7, 5)
output = bop_7035
output2 = bop_7035
func_7071 = relay.Function([var_7033,], output)
mod['func_7071'] = func_7071
mod = relay.transform.InferType()(mod)
mutated_mod['func_7071'] = func_7071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7072 = relay.var("var_7072", dtype = "float64", shape = (6, 7, 5))#candidate|7072|(6, 7, 5)|var|float64
func_7071_call = mutated_mod.get_global_var('func_7071')
call_7073 = func_7071_call(var_7072)
output = call_7073
func_7074 = relay.Function([var_7072], output)
mutated_mod['func_7074'] = func_7074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7109 = relay.var("var_7109", dtype = "bool", shape = (16, 11, 8))#candidate|7109|(16, 11, 8)|var|bool
var_7110 = relay.var("var_7110", dtype = "bool", shape = (16, 11, 8))#candidate|7110|(16, 11, 8)|var|bool
bop_7111 = relay.logical_and(var_7109.astype('bool'), relay.reshape(var_7110.astype('bool'), relay.shape_of(var_7109))) # shape=(16, 11, 8)
bop_7117 = relay.logical_or(bop_7111.astype('bool'), relay.reshape(var_7109.astype('bool'), relay.shape_of(bop_7111))) # shape=(16, 11, 8)
output = relay.Tuple([bop_7117,])
output2 = relay.Tuple([bop_7117,])
func_7123 = relay.Function([var_7109,var_7110,], output)
mod['func_7123'] = func_7123
mod = relay.transform.InferType()(mod)
var_7124 = relay.var("var_7124", dtype = "bool", shape = (16, 11, 8))#candidate|7124|(16, 11, 8)|var|bool
var_7125 = relay.var("var_7125", dtype = "bool", shape = (16, 11, 8))#candidate|7125|(16, 11, 8)|var|bool
output = func_7123(var_7124,var_7125,)
func_7126 = relay.Function([var_7124,var_7125,], output)
mutated_mod['func_7126'] = func_7126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mod.get_global_var('func_2419')
func_2420_call = mutated_mod.get_global_var('func_2420')
call_7128 = relay.TupleGetItem(func_2419_call(), 0)
call_7129 = relay.TupleGetItem(func_2420_call(), 0)
var_7141 = relay.var("var_7141", dtype = "uint16", shape = (15, 3, 9))#candidate|7141|(15, 3, 9)|var|uint16
bop_7142 = relay.logical_and(call_7128.astype('bool'), relay.reshape(var_7141.astype('bool'), relay.shape_of(call_7128))) # shape=(15, 3, 9)
bop_7145 = relay.logical_and(call_7129.astype('bool'), relay.reshape(var_7141.astype('bool'), relay.shape_of(call_7129))) # shape=(15, 3, 9)
output = bop_7142
output2 = bop_7145
func_7150 = relay.Function([var_7141,], output)
mod['func_7150'] = func_7150
mod = relay.transform.InferType()(mod)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7151 = relay.var("var_7151", dtype = "uint16", shape = (15, 3, 9))#candidate|7151|(15, 3, 9)|var|uint16
func_7150_call = mutated_mod.get_global_var('func_7150')
call_7152 = func_7150_call(var_7151)
output = call_7152
func_7153 = relay.Function([var_7151], output)
mutated_mod['func_7153'] = func_7153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5430_call = mod.get_global_var('func_5430')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_7184 = relay.TupleGetItem(func_5430_call(), 0)
call_7185 = relay.TupleGetItem(func_5431_call(), 0)
func_6964_call = mod.get_global_var('func_6964')
func_6965_call = mutated_mod.get_global_var('func_6965')
call_7193 = relay.TupleGetItem(func_6964_call(), 0)
call_7194 = relay.TupleGetItem(func_6965_call(), 0)
output = relay.Tuple([call_7184,call_7193,])
output2 = relay.Tuple([call_7185,call_7194,])
func_7205 = relay.Function([], output)
mod['func_7205'] = func_7205
mod = relay.transform.InferType()(mod)
output = func_7205()
func_7206 = relay.Function([], output)
mutated_mod['func_7206'] = func_7206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3951_call = mod.get_global_var('func_3951')
func_3953_call = mutated_mod.get_global_var('func_3953')
call_7217 = relay.TupleGetItem(func_3951_call(), 1)
call_7218 = relay.TupleGetItem(func_3953_call(), 1)
output = relay.Tuple([call_7217,])
output2 = relay.Tuple([call_7218,])
func_7224 = relay.Function([], output)
mod['func_7224'] = func_7224
mod = relay.transform.InferType()(mod)
mutated_mod['func_7224'] = func_7224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7224_call = mutated_mod.get_global_var('func_7224')
call_7225 = func_7224_call()
output = call_7225
func_7226 = relay.Function([], output)
mutated_mod['func_7226'] = func_7226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3316_call = mod.get_global_var('func_3316')
func_3318_call = mutated_mod.get_global_var('func_3318')
call_7292 = func_3316_call()
call_7293 = func_3316_call()
func_4387_call = mod.get_global_var('func_4387')
func_4389_call = mutated_mod.get_global_var('func_4389')
call_7304 = relay.TupleGetItem(func_4387_call(), 0)
call_7305 = relay.TupleGetItem(func_4389_call(), 0)
func_6142_call = mod.get_global_var('func_6142')
func_6144_call = mutated_mod.get_global_var('func_6144')
call_7308 = relay.TupleGetItem(func_6142_call(), 0)
call_7309 = relay.TupleGetItem(func_6144_call(), 0)
output = relay.Tuple([call_7292,call_7304,call_7308,])
output2 = relay.Tuple([call_7293,call_7305,call_7309,])
func_7310 = relay.Function([], output)
mod['func_7310'] = func_7310
mod = relay.transform.InferType()(mod)
output = func_7310()
func_7311 = relay.Function([], output)
mutated_mod['func_7311'] = func_7311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2777_call = mod.get_global_var('func_2777')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_7323 = relay.TupleGetItem(func_2777_call(), 1)
call_7324 = relay.TupleGetItem(func_2778_call(), 1)
var_7331 = relay.var("var_7331", dtype = "float32", shape = (6, 8, 11))#candidate|7331|(6, 8, 11)|var|float32
bop_7332 = relay.equal(call_7323.astype('bool'), relay.reshape(var_7331.astype('bool'), relay.shape_of(call_7323))) # shape=(6, 8, 11)
bop_7335 = relay.equal(call_7324.astype('bool'), relay.reshape(var_7331.astype('bool'), relay.shape_of(call_7324))) # shape=(6, 8, 11)
output = bop_7332
output2 = bop_7335
func_7340 = relay.Function([var_7331,], output)
mod['func_7340'] = func_7340
mod = relay.transform.InferType()(mod)
mutated_mod['func_7340'] = func_7340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7341 = relay.var("var_7341", dtype = "float32", shape = (6, 8, 11))#candidate|7341|(6, 8, 11)|var|float32
func_7340_call = mutated_mod.get_global_var('func_7340')
call_7342 = func_7340_call(var_7341)
output = call_7342
func_7343 = relay.Function([var_7341], output)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_7349 = relay.TupleGetItem(func_5157_call(), 0)
call_7350 = relay.TupleGetItem(func_5159_call(), 0)
var_7354 = relay.var("var_7354", dtype = "float64", shape = (6, 8, 11))#candidate|7354|(6, 8, 11)|var|float64
bop_7355 = relay.multiply(call_7349.astype('int8'), relay.reshape(var_7354.astype('int8'), relay.shape_of(call_7349))) # shape=(6, 8, 11)
bop_7358 = relay.multiply(call_7350.astype('int8'), relay.reshape(var_7354.astype('int8'), relay.shape_of(call_7350))) # shape=(6, 8, 11)
func_7071_call = mod.get_global_var('func_7071')
func_7074_call = mutated_mod.get_global_var('func_7074')
var_7360 = relay.var("var_7360", dtype = "float64", shape = (210,))#candidate|7360|(210,)|var|float64
call_7359 = func_7071_call(relay.reshape(var_7360.astype('float64'), [6, 7, 5]))
call_7361 = func_7071_call(relay.reshape(var_7360.astype('float64'), [6, 7, 5]))
func_813_call = mod.get_global_var('func_813')
func_815_call = mutated_mod.get_global_var('func_815')
call_7364 = relay.TupleGetItem(func_813_call(), 1)
call_7365 = relay.TupleGetItem(func_815_call(), 1)
func_5732_call = mod.get_global_var('func_5732')
func_5734_call = mutated_mod.get_global_var('func_5734')
const_7372 = relay.const([[0.090319],[-1.265838],[-6.645005],[-6.403705],[8.500903],[-4.790910],[9.714405],[-0.363465],[-7.108572],[-1.010073],[-3.609532],[8.205293],[6.800459],[1.777217],[-3.089248],[-5.413765],[-4.283724],[0.808728],[-8.478526],[4.601923],[-1.121744],[-1.264506],[5.349663],[-6.804587],[3.867473],[-6.406769],[8.861150],[9.615632],[-1.276139],[-1.413597],[-7.178906],[-8.151561],[3.018583],[-9.815210],[-5.292126],[1.123745],[9.679976],[-8.217035],[-1.728439],[-6.056189],[1.069958],[8.028469],[-4.899648],[6.799596],[-0.443826],[0.697760],[7.867354],[0.331742],[-6.572635],[-2.298096],[-9.472273],[3.193165],[-1.113085],[-6.702361],[8.481074],[-2.380868],[1.281695],[6.719565],[4.432902],[-4.108564],[-6.397741],[-2.283162],[-8.815969],[-2.876324],[7.282735],[0.835405],[-1.143513],[-1.200643],[-7.994059],[2.995700],[7.494062],[-3.776544],[7.432634],[8.592630],[6.624899],[-2.721733],[1.935011],[0.626460],[7.555026],[-8.138603],[-6.626943],[-8.444027],[1.451790],[7.877721],[3.313708],[8.488962],[7.154596],[-6.095099],[6.588789],[5.858039],[0.524217],[-2.719395],[-6.504102],[-3.292758],[7.444053],[3.519825],[-8.038591],[-4.666446],[-0.142653],[2.385352],[-6.405444],[-3.586982],[6.128301],[-3.788470],[-4.062078],[7.466555],[-2.866142],[9.184995],[0.240017],[-3.727833],[-3.635178],[-7.095002],[3.594416],[-7.861672],[9.057615],[6.613731],[-7.129884],[1.200114],[-7.048302],[-3.316050],[4.572750],[8.648507],[6.974539],[-6.846852],[-1.698872],[5.758787],[-0.117108],[-2.105479],[-2.786502],[1.880562],[-4.573153],[8.991060],[5.153562],[-9.652592],[4.329133],[-7.099114],[-0.198906],[-2.759265],[-6.134684],[-1.474314],[0.463203],[-9.047874],[-2.762525],[4.072721],[2.464991],[-1.398764],[3.269696],[3.789766],[-0.343521],[1.020556],[-5.287391],[-7.314092],[3.779747],[6.782218],[8.078412],[-2.251869],[9.138534],[7.182170],[6.339000],[0.143237],[8.464308],[8.692212],[5.210265],[0.474233],[-4.442000],[0.311067],[9.894303],[-2.286521],[-6.813776],[-1.641489],[6.320737],[-3.620857],[7.701865],[-1.715412],[-3.264342],[-5.498067],[6.690022],[7.520862],[-2.006178],[-4.475887],[5.636010],[9.736657],[9.454337],[9.323778],[9.609248],[-6.667193],[-7.721471],[-0.412440],[-3.278543],[3.986923],[-8.070190],[-8.701993],[2.318313],[-4.738365],[7.301040],[-9.726201],[6.912393],[7.285667],[6.373071],[-7.458272],[-9.776799],[-0.278680],[-5.859190],[4.949198],[5.589844],[1.742473],[-9.138672],[-5.161303],[2.583200],[2.695723],[9.574330],[9.175837],[3.726749],[-9.635115],[4.682743],[-7.858823],[6.067894],[4.038535],[6.135557],[-7.568333],[5.819009],[-4.857229],[0.591067],[3.847866],[5.674008],[4.655107],[-3.947734],[5.419859],[4.266595],[0.169475],[9.850326],[6.818544],[-0.902968],[-1.649716],[7.217282],[-0.825739],[-8.374605],[-2.645243],[8.183504],[8.275349],[-0.887619],[-5.403993],[6.513384],[-2.845957],[5.464250],[-4.118197],[4.876966],[4.710020],[-5.240712],[9.123709],[-4.786142],[-3.886310],[-4.017334],[-6.194875],[-0.323928],[1.211408],[9.563617],[5.944095],[2.335320],[5.752804],[4.017390],[4.698954],[1.724810],[-3.718826],[-0.390489],[6.204013],[-6.606758],[-0.767559],[-8.350163],[-9.590842],[-2.329194],[8.805937],[2.284443],[-5.199056],[0.357323],[9.124835],[9.151416],[7.741145],[1.835053],[-1.321934],[-4.581225],[-1.914502],[5.980212],[4.026038],[-3.476523],[-8.546551],[7.690582],[-8.948833],[2.281958],[-3.681191],[-6.504635],[9.585940],[-2.316266],[1.017886],[5.959580],[-6.503804],[1.236703],[-9.000864],[9.732507],[5.288190],[2.261643],[-5.002702],[9.353064],[-9.804443],[1.677295],[8.784807],[-6.246526],[-1.361151],[-4.756557],[8.521126],[5.589756],[3.184681],[-5.406240],[-0.488337],[0.799218],[5.303874],[8.701553],[-4.555972],[-9.704792],[7.389897],[3.226226],[-7.363241],[-5.295303],[-7.068804],[-7.172117],[-0.673913],[0.171571],[-6.025155],[4.530531],[6.394056],[-4.961186],[3.765620],[-3.545904],[5.840811],[-1.795297],[9.116594],[6.475198],[-4.998512],[-4.590854],[-0.882504],[-1.249994],[-7.814536],[-2.018760],[8.126567],[3.405825],[8.949935],[-6.840151],[-5.530880],[-6.105155],[4.313904],[-3.419832],[-9.784959],[-2.881432],[4.241691],[1.878036],[8.757915],[-5.382208],[-5.952643],[4.985354],[-6.862550],[-9.933925],[-9.159863],[0.742215],[-7.233037],[-0.754190],[-8.289789],[-3.099789],[9.235074],[9.100091],[1.838166],[-4.326243],[-5.032754],[-1.424105],[-0.850964],[1.771023],[8.224802],[-8.366777],[-8.541631],[-2.971890],[8.879952],[-3.914241],[3.508805],[-6.766874],[-1.975012],[-1.235984],[-2.756706],[-7.436649],[9.604543],[8.993758],[-6.001246],[0.039778],[1.769035],[-2.476951],[5.190733],[-0.486532],[0.105673],[-1.160050],[4.797325],[9.944588],[8.365749],[8.060943],[3.772904],[-6.081575],[-8.253007],[-1.198327],[-9.280942],[-3.869900],[8.006388],[3.987237],[5.790718],[6.066008],[5.665074],[-0.945404],[-1.414414],[-2.697746],[2.779342],[6.812226],[0.821697],[5.559525],[-9.424446],[2.439489],[0.234741],[-4.149582],[-3.387230],[6.122594],[6.193648],[-9.136621],[5.751373],[9.490179]], dtype = "float64")#candidate|7372|(429, 1)|const|float64
call_7371 = func_5732_call(relay.reshape(const_7372.astype('float64'), [11, 13, 3]))
call_7373 = func_5732_call(relay.reshape(const_7372.astype('float64'), [11, 13, 3]))
func_6037_call = mod.get_global_var('func_6037')
func_6039_call = mutated_mod.get_global_var('func_6039')
call_7376 = relay.TupleGetItem(func_6037_call(), 3)
call_7377 = relay.TupleGetItem(func_6039_call(), 3)
output = relay.Tuple([bop_7355,call_7359,var_7360,call_7364,call_7371,const_7372,call_7376,])
output2 = relay.Tuple([bop_7358,call_7361,var_7360,call_7365,call_7373,const_7372,call_7377,])
func_7386 = relay.Function([var_7354,var_7360,], output)
mod['func_7386'] = func_7386
mod = relay.transform.InferType()(mod)
mutated_mod['func_7386'] = func_7386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7386_call = mutated_mod.get_global_var('func_7386')
var_7388 = relay.var("var_7388", dtype = "float64", shape = (6, 8, 11))#candidate|7388|(6, 8, 11)|var|float64
var_7389 = relay.var("var_7389", dtype = "float64", shape = (210,))#candidate|7389|(210,)|var|float64
call_7387 = func_7386_call(var_7388,var_7389,)
output = call_7387
func_7390 = relay.Function([var_7388,var_7389,], output)
mutated_mod['func_7390'] = func_7390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5756_call = mod.get_global_var('func_5756')
func_5758_call = mutated_mod.get_global_var('func_5758')
call_7418 = func_5756_call()
call_7419 = func_5756_call()
output = call_7418
output2 = call_7419
func_7420 = relay.Function([], output)
mod['func_7420'] = func_7420
mod = relay.transform.InferType()(mod)
output = func_7420()
func_7421 = relay.Function([], output)
mutated_mod['func_7421'] = func_7421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5244_call = mod.get_global_var('func_5244')
func_5245_call = mutated_mod.get_global_var('func_5245')
call_7456 = relay.TupleGetItem(func_5244_call(), 0)
call_7457 = relay.TupleGetItem(func_5245_call(), 0)
func_5164_call = mod.get_global_var('func_5164')
func_5165_call = mutated_mod.get_global_var('func_5165')
call_7460 = func_5164_call()
call_7461 = func_5164_call()
output = relay.Tuple([call_7456,call_7460,])
output2 = relay.Tuple([call_7457,call_7461,])
func_7462 = relay.Function([], output)
mod['func_7462'] = func_7462
mod = relay.transform.InferType()(mod)
mutated_mod['func_7462'] = func_7462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7462_call = mutated_mod.get_global_var('func_7462')
call_7463 = func_7462_call()
output = call_7463
func_7464 = relay.Function([], output)
mutated_mod['func_7464'] = func_7464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7310_call = mod.get_global_var('func_7310')
func_7311_call = mutated_mod.get_global_var('func_7311')
call_7465 = relay.TupleGetItem(func_7310_call(), 2)
call_7466 = relay.TupleGetItem(func_7311_call(), 2)
output = call_7465
output2 = call_7466
func_7482 = relay.Function([], output)
mod['func_7482'] = func_7482
mod = relay.transform.InferType()(mod)
output = func_7482()
func_7483 = relay.Function([], output)
mutated_mod['func_7483'] = func_7483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2365_call = mutated_mod.get_global_var('func_2365')
call_7500 = relay.TupleGetItem(func_2364_call(), 0)
call_7501 = relay.TupleGetItem(func_2365_call(), 0)
func_3419_call = mod.get_global_var('func_3419')
func_3422_call = mutated_mod.get_global_var('func_3422')
var_7507 = relay.var("var_7507", dtype = "bool", shape = (88,))#candidate|7507|(88,)|var|bool
const_7508 = relay.const(10, dtype = "uint16")#candidate|7508|()|const|uint16
call_7506 = relay.TupleGetItem(func_3419_call(relay.reshape(var_7507.astype('bool'), [88,]), relay.reshape(const_7508.astype('uint16'), []), ), 3)
call_7509 = relay.TupleGetItem(func_3422_call(relay.reshape(var_7507.astype('bool'), [88,]), relay.reshape(const_7508.astype('uint16'), []), ), 3)
output = relay.Tuple([call_7500,call_7506,var_7507,const_7508,])
output2 = relay.Tuple([call_7501,call_7509,var_7507,const_7508,])
func_7514 = relay.Function([var_7507,], output)
mod['func_7514'] = func_7514
mod = relay.transform.InferType()(mod)
var_7515 = relay.var("var_7515", dtype = "bool", shape = (88,))#candidate|7515|(88,)|var|bool
output = func_7514(var_7515)
func_7516 = relay.Function([var_7515], output)
mutated_mod['func_7516'] = func_7516
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7569 = relay.var("var_7569", dtype = "float32", shape = (8, 1, 16))#candidate|7569|(8, 1, 16)|var|float32
uop_7570 = relay.atanh(var_7569.astype('float32')) # shape=(8, 1, 16)
func_6132_call = mod.get_global_var('func_6132')
func_6134_call = mutated_mod.get_global_var('func_6134')
call_7574 = relay.TupleGetItem(func_6132_call(), 1)
call_7575 = relay.TupleGetItem(func_6134_call(), 1)
func_1097_call = mod.get_global_var('func_1097')
func_1099_call = mutated_mod.get_global_var('func_1099')
call_7578 = relay.TupleGetItem(func_1097_call(relay.reshape(call_7574.astype('float32'), [15, 3, 9])), 1)
call_7579 = relay.TupleGetItem(func_1099_call(relay.reshape(call_7574.astype('float32'), [15, 3, 9])), 1)
func_530_call = mod.get_global_var('func_530')
func_535_call = mutated_mod.get_global_var('func_535')
var_7585 = relay.var("var_7585", dtype = "bool", shape = (88,))#candidate|7585|(88,)|var|bool
var_7586 = relay.var("var_7586", dtype = "uint16", shape = ())#candidate|7586|()|var|uint16
var_7587 = relay.var("var_7587", dtype = "float32", shape = (13, 1))#candidate|7587|(13, 1)|var|float32
call_7584 = relay.TupleGetItem(func_530_call(relay.reshape(var_7585.astype('bool'), [11, 2, 4]), relay.reshape(var_7585.astype('bool'), [11, 2, 4]), relay.reshape(var_7586.astype('uint16'), []), relay.reshape(var_7587.astype('float32'), [13,]), ), 1)
call_7588 = relay.TupleGetItem(func_535_call(relay.reshape(var_7585.astype('bool'), [11, 2, 4]), relay.reshape(var_7585.astype('bool'), [11, 2, 4]), relay.reshape(var_7586.astype('uint16'), []), relay.reshape(var_7587.astype('float32'), [13,]), ), 1)
output = relay.Tuple([uop_7570,call_7574,call_7578,call_7584,var_7585,var_7586,var_7587,])
output2 = relay.Tuple([uop_7570,call_7575,call_7579,call_7588,var_7585,var_7586,var_7587,])
func_7596 = relay.Function([var_7569,var_7585,var_7586,var_7587,], output)
mod['func_7596'] = func_7596
mod = relay.transform.InferType()(mod)
var_7597 = relay.var("var_7597", dtype = "float32", shape = (8, 1, 16))#candidate|7597|(8, 1, 16)|var|float32
var_7598 = relay.var("var_7598", dtype = "bool", shape = (88,))#candidate|7598|(88,)|var|bool
var_7599 = relay.var("var_7599", dtype = "uint16", shape = ())#candidate|7599|()|var|uint16
var_7600 = relay.var("var_7600", dtype = "float32", shape = (13, 1))#candidate|7600|(13, 1)|var|float32
output = func_7596(var_7597,var_7598,var_7599,var_7600,)
func_7601 = relay.Function([var_7597,var_7598,var_7599,var_7600,], output)
mutated_mod['func_7601'] = func_7601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3967_call = mod.get_global_var('func_3967')
func_3969_call = mutated_mod.get_global_var('func_3969')
call_7603 = relay.TupleGetItem(func_3967_call(), 0)
call_7604 = relay.TupleGetItem(func_3969_call(), 0)
func_2037_call = mod.get_global_var('func_2037')
func_2041_call = mutated_mod.get_global_var('func_2041')
const_7620 = relay.const([-1.328811,-2.029552,-5.323058,9.479618,4.777061,-8.790083,5.557618,-8.090634,-5.505666,-5.664211,-8.798959,1.308127,9.298531,6.328077,-1.641470,7.037568,1.330280,-0.990528,-7.345902,-2.371704,-6.484123,9.154364,-6.705175,3.168882,3.876219,9.258870,4.675088,-1.342264,-3.810150,1.801941,-4.653648,9.552863,-5.728913,3.005335,6.573905,3.810713,-9.253614,6.044382,-0.587699,-8.924056,-7.165472,8.198326,-8.940714,-3.288384,3.073917,0.220775,-3.332037,-6.120683,-4.070839,-3.819411,6.871092,0.459768,-7.061642,-4.110924,2.372909,0.139439,2.081186,-8.313843,-5.360834,-1.943414,-1.125504,7.040824,-1.967933,-7.387380,-2.951305,-2.828728,-2.409060,9.808348,-3.859335,0.460574,-3.102429,-3.100505,7.714810,3.270924,4.667675,7.356049,1.548147,3.821840,-5.423311,9.060386,-6.663772,7.196310,9.803541,9.802483,-7.905815,-8.968370,9.893294,-7.609540,5.963145,7.191597,3.245320,-8.271411,5.968925,-9.024262,4.914627,-6.484942,8.545162,-7.140930,0.364375,8.216652,-4.107385,-5.717334,-2.674830,-6.940871,9.791084,-7.126820,4.603292,6.050942,-6.573303,-6.566583,6.390170,7.305433,-7.667741,-2.089414,-4.010547,-2.643862,5.413845,-4.932404,5.701157,7.664354,-2.741629,-6.961559,-7.760105,9.092859,9.039211,9.877481,-2.648403,-3.943505,-4.006453,-6.707222,-2.159011,-6.390393,-2.925376,9.450102,0.370860,-6.055894,-7.322776,9.912556,-0.324428,-4.455038,5.216553,5.486338,-9.461589,-2.713690,-0.869194,6.644975,2.308373,-2.525241,8.614164,-9.616982,-4.569073,-9.942885,8.929814,4.174497,-4.166548,8.326168,3.755375,-3.687424,-7.539633,2.353482,7.524430,5.994611,-2.044314,-3.808040,2.380120,-9.164179,8.568171,1.997300,7.062865,5.297283,-3.229335,2.353173,1.158498,5.461750,-6.996073,-8.379806,-7.569729,4.573673,7.833247,-5.796784,-7.722645,-1.666175,4.983663,-0.679774,-7.839030,9.168203,-0.545384,3.019010,-2.148003,-2.955255,5.493574,-9.715304,-0.966151,-1.666691,-0.030088,2.430299,2.275988,-3.467312,0.617160,3.905883,-0.317353,-4.067877,3.369368,-1.742530,-2.975843,5.806512,5.283412,5.309469,6.919687,6.303237,-7.484573,-9.234393,-2.589330,5.411955,1.785782,-4.240442,9.475597,-7.009406,-2.731056,-4.343223,2.863409,-8.799358,4.872086,5.423654,2.989347,-8.212023,9.798873,7.695697,-5.104009,5.722110,-5.881961,8.949222,-1.647574,-4.684267,7.135817,5.860778,-1.629778,2.086913,-1.297944,-7.609567,-2.357447,5.564761,8.151479,0.839100,1.365914,1.413170,-2.275379,1.373212,6.404756,1.267969,-6.442504,9.243230,-1.074063,1.778425,5.324610,-2.438423,-9.387844,3.014798,4.013755,5.894824,0.584892,-4.516659,-8.257215,-3.812056,9.551192,-8.286772,7.517588,5.936391,-6.994231,-4.899747,-0.011254,6.917961,-2.520313,3.081599,-3.382150,2.631179,0.159624,7.572240,1.422850,5.203975,-9.301447,6.932960,-8.971189,4.417683,6.507873,-8.091464,3.244731,-0.054200,8.549355,9.742817,3.296190,3.442840,-5.149705,-1.403574,6.909602,-4.263458,4.372082,7.064851,-4.534867,-4.584255,-8.762386,-5.977935,5.015785,7.666212,-9.012789,-8.373718,7.268495,-5.742929,-8.871624,-5.290104,7.245005,8.339687,-0.980125,-1.865629,-3.404283,-4.941928,3.161964,-4.648185,1.803555,6.501988,-7.502850,7.451046,-5.282809,6.426992,-2.789213,-0.941057,-9.216372,-7.626213,-6.177680,-3.171761,-3.216424,0.661961,3.258932,-8.097601,2.555482,-7.828228,3.528598,-5.075314,9.410855,-7.244122,6.475250,9.427153,2.986862,-1.316239,-9.386933,-4.976860,5.628964,8.604213,4.345802,3.092326,2.443343,-5.263142,-6.977645,-7.803103,-0.937563,8.039540,6.904971,4.251163,3.029203,-3.478208,-2.579149,-5.631986,-6.500213,-1.453934,7.076598,6.409382,7.605246,9.037609,-8.851007,-7.942033,-5.038830,-9.334806,-3.546582,-3.774565,8.759849,-1.542896,0.559975,4.904032,-3.810024,9.125998,1.936463,-8.702737,-2.085665,-5.189585,-5.120140,2.201232,8.693473,-4.749108,-4.448764,4.170965,-7.727139,8.199006,-9.441383,7.948770,1.271078,-1.157446,9.494077,1.114535,-0.476458,-6.298528,-1.783319,7.729796,7.759116,-7.193688,0.675202,8.784842,5.854691,5.955318,3.630809,-0.037285,-2.826180,-3.235749,3.007355,6.226689,4.126138,-6.251868,-5.835045,3.951484,-9.003789,3.672574,4.526325,1.793180,5.300324,-7.895851,0.522587,2.612502,2.651061,-3.723343,-9.993677,-5.022183,1.093918,2.824110,8.804438,-4.941169,-8.641498,3.369570,-0.903231,-3.753337,4.659188,6.614795,5.951570,-5.758588,-3.714109,-3.757531,4.758045,-2.613286,0.278388,-7.695112,9.639577,-2.033686,-8.361615,7.976692,-4.004690,-0.612124,9.312553,7.403157,5.162466,1.137456,-9.006861,-4.313235,3.373818,-3.104491,-1.594731,9.361984,2.445704,-1.479891,3.237887,4.405590,0.764141,7.282906,8.176288,-0.572320,8.406471,-4.325815,1.678066,0.995500,2.946929,6.738768,-3.127412,7.371453,3.912349,7.280995,-2.836451,-6.923512,-9.018114,-0.954085,-9.503418,-4.451029,-4.546996,1.316991,2.785655,-1.605669,3.190115,0.610454,-7.746868,6.238888,-6.394121,-9.529699,7.570160,-8.339166,4.058234,6.412403,5.389433,1.891603,-0.321861,5.011473,9.710727,7.647681,-6.828016,-6.200501,3.351933,-4.571657,-6.643440,-6.792475,1.321302,8.354432,8.845542,2.625430,7.839630,0.083315,9.988020,4.960148,-9.490846,1.243560,0.721894,-4.425601,-5.736102,-3.110266,5.012132,-6.049659,-3.822876,1.739097,1.346462,-5.330962,2.465641,-9.212634,2.607392,2.747653,-8.495238,-1.372972,-7.397043,0.912668,0.741760,0.782377,-0.714901,5.278532,-6.910090,7.162601,7.671755,-8.765780,2.943535,-4.115322,-3.452127,-6.877611,-1.512693,8.041243,9.240865,0.927095,-1.704956,-8.829576,7.563307,7.529438,-8.167439,0.801903,5.273882,8.708886,-2.597677,1.315637,1.461114,-4.345220,-9.137915,2.126053,-8.252773,-8.862214,1.569635,5.959162,-9.033035,-0.224508,2.789826,0.594179,6.592242,9.436649,-7.220433,5.441147,7.419617,9.626948,2.642106,9.760928,-3.869597,-7.606971,-0.236019,-7.887734,2.866219,-7.189263,-2.363767,3.080386,-9.277681,2.928875,3.449307,-3.702418,-1.453904,-9.315068,-8.041555,3.550933,2.421485,3.863582,-8.233498,-3.528177,-5.237517,-7.533548,-5.096591,6.730520,2.139759,1.130457,0.302017,2.683563,-5.783148,8.201801,2.622856,0.680689,-1.022767,0.342979,-8.486593,-0.699941,-1.225492,2.493934,-0.237506,4.508735,4.435886,-7.687224,-4.685374,0.058853,6.260544,-6.094085,5.394794,8.050876,-0.012599,-6.163336,8.042478,5.831137,-9.240141,-3.432138,3.613250,-7.489577,4.997398,2.343435,-1.801982,-1.032132,2.642456,-4.142151,-8.766811,1.394814,-3.164731,5.137507,-5.344041,3.598341,1.960064,-1.038947,2.471637,7.258377,2.332463,9.346613,7.933854,-1.300050,-6.463537,-2.645235,-5.518055,8.017848,3.820471,-1.147906,0.785178,-1.231886,-9.987267,-8.529880,1.878810,-1.905976,-2.049484,-3.860358,3.156530,9.668982,-2.222590,-9.394389,9.024916,2.120363,-4.091715,-7.428405,-3.618694,-8.009610,5.407418,-7.897244,-7.368740,-9.048225,-2.638734,4.000006,7.163270,5.230740,-1.675672,-2.739427,1.468078,-6.846679,-6.859590,-3.837777,-9.788096,9.663459,3.606343,-3.034394,-3.420648,-9.453840,-6.949225,-9.642067,-4.591790,9.059308,5.620631,-4.193162,7.042317,-4.288946,-5.278151,-4.735219,4.877965,-3.566638,-8.450078,-4.181522,7.702680,0.987477,-3.030950,9.145960,-9.376462,1.668761,7.387674,-4.870981,7.036652,-9.085967,5.864300,-1.958598,-3.341872,1.282479,5.800798,7.085841,0.124294,-7.349660,-5.389332,-1.690695,-8.063567,-0.819901,-1.230821,1.078408,6.246088,4.413000,-3.960561,1.228203,-0.983161,2.967803,-8.875998,2.185931,-3.072571,-0.769084,2.471697,3.264055,-7.511595,1.773850,-0.978761,-0.135412,-7.058662,0.792939,4.347109,2.871215,5.172039,-5.492620,9.427001,7.258292,4.555162,-2.645686,8.434850,0.674031,3.524400,-2.327819,3.657167,2.464874,-6.938156,-7.474647,1.729146,9.216719,5.110610,4.344798,4.021450,-0.001138,-7.061952,-4.403863,-7.358628,8.623813,-5.799905,5.753366,3.876781,-6.199114,9.268713,4.748874,-3.823945,-3.432237,-7.177561,8.454600,-2.118281,1.747771,-1.814459,-1.887975,5.932116,2.767788,5.068246,9.062400,8.791439,-7.213017,-8.512629,-8.193089,1.061607,-7.396038,-1.858101,7.514684,5.352773,4.327769,-2.331475,-1.168077,9.526660,-9.474977,3.233925,9.960860,6.906894], dtype = "float32")#candidate|7620|(825,)|const|float32
var_7621 = relay.var("var_7621", dtype = "float32", shape = (405, 1))#candidate|7621|(405, 1)|var|float32
call_7619 = relay.TupleGetItem(func_2037_call(relay.reshape(const_7620.astype('float32'), [5, 15, 11]), relay.reshape(const_7620.astype('float32'), [5, 15, 11]), relay.reshape(var_7621.astype('float32'), [405,]), ), 1)
call_7622 = relay.TupleGetItem(func_2041_call(relay.reshape(const_7620.astype('float32'), [5, 15, 11]), relay.reshape(const_7620.astype('float32'), [5, 15, 11]), relay.reshape(var_7621.astype('float32'), [405,]), ), 1)
func_5157_call = mod.get_global_var('func_5157')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_7630 = relay.TupleGetItem(func_5157_call(), 0)
call_7631 = relay.TupleGetItem(func_5159_call(), 0)
output = relay.Tuple([call_7603,call_7619,const_7620,var_7621,call_7630,])
output2 = relay.Tuple([call_7604,call_7622,const_7620,var_7621,call_7631,])
func_7632 = relay.Function([var_7621,], output)
mod['func_7632'] = func_7632
mod = relay.transform.InferType()(mod)
mutated_mod['func_7632'] = func_7632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7633 = relay.var("var_7633", dtype = "float32", shape = (405, 1))#candidate|7633|(405, 1)|var|float32
func_7632_call = mutated_mod.get_global_var('func_7632')
call_7634 = func_7632_call(var_7633)
output = call_7634
func_7635 = relay.Function([var_7633], output)
mutated_mod['func_7635'] = func_7635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6296_call = mod.get_global_var('func_6296')
func_6297_call = mutated_mod.get_global_var('func_6297')
call_7649 = relay.TupleGetItem(func_6296_call(), 0)
call_7650 = relay.TupleGetItem(func_6297_call(), 0)
func_1097_call = mod.get_global_var('func_1097')
func_1099_call = mutated_mod.get_global_var('func_1099')
const_7665 = relay.const([-9.450872,8.260268,-3.254048,-7.845778,-4.969980,5.457199,5.793827,1.221529,9.480749,-8.195523,-7.813936,-7.697048,5.380268,3.965212,-7.176118,-7.745258,-4.573170,3.892515,-8.667638,6.192799,-9.456924,-2.897335,0.745039,-3.598494,-1.406745,3.939743,1.236034,-9.860005,-0.385174,9.023364,-2.338637,-2.637625,1.928044,9.113804,6.455652,-3.699035,9.328277,5.520406,-5.131218,4.042326,1.712275,1.511281,1.663266,9.690525,9.355523,-8.210807,-7.634330,-5.896801,7.491653,7.039081,-6.732576,-4.962903,-6.803247,9.914200,-0.270470,8.132327,5.736104,-5.794770,-6.408933,-3.884031,-6.890126,5.573688,8.904670,-4.776887,9.642118,-8.707837,7.194206,3.408998,-6.001840,-9.411826,-2.602894,-0.042404,-0.220008,-7.276189,-6.937149,-5.188672,8.996374,0.176221,4.436002,9.151165,2.464399,-0.304640,6.471205,-8.810018,-3.951815,-7.812710,5.509992,-8.047975,8.502973,-3.623805,-7.401352,-4.401771,6.701229,-0.998110,0.668682,7.740430,5.269896,9.735229,-6.964636,5.103063,-9.073887,1.225258,-3.558654,8.706023,-2.886553,-2.569611,-1.052860,-4.654271,-3.626687,-9.515887,3.734434,9.793337,6.584015,5.497805,-0.530778,1.502978,-9.180407,-2.713256,-5.953481,-6.279318,-6.141833,5.853195,8.621742,-9.881432,3.365736,9.063722,-3.107747,3.146681,7.946019,9.509191,2.069520,-8.049177,3.506058,0.629015,-4.810228,-2.802280,-7.067129,3.932245,-3.581037,1.498347,-7.447572,-1.922062,5.656631,-2.876557,-2.307697,2.294855,-1.068716,1.653561,-3.322859,-5.079074,-8.172074,1.552042,-4.153856,-9.792127,-2.485079,-8.886650,-0.879524,-7.629867,3.004190,-8.431749,-3.118815,8.668679,9.370515,2.265924,5.775590,-1.165756,-5.445508,-6.308187,-6.561536,6.088480,1.435776,1.722158,-7.430865,8.388889,-0.380040,0.228577,4.332516,-2.040671,4.365832,9.968190,4.156145,-0.203935,6.535121,-3.229714,2.978510,9.609618,-0.131018,-5.003507,-2.855358,-4.774145,4.750982,5.642172,-1.893398,9.610524,1.047579,3.462201,-5.736619,5.932943,-9.491232,1.454339,2.682577,-3.175164,5.394994,7.595404,9.434721,0.335647,0.207717,9.620206,-0.138376,-7.286695,2.907205,-0.405239,2.024791,-0.067510,0.454937,-0.820692,-1.349227,-7.184261,5.442721,7.573092,1.230478,-1.788083,3.126410,5.771523,-8.662044,-8.463642,4.877050,-4.516959,-8.036080,-6.287248,-2.056647,-9.906020,-6.425795,1.841041,-0.430378,-9.745845,1.672873,1.217850,-3.412187,-6.684321,-0.250065,7.922332,5.045255,-2.840537,-1.913099,2.956342,4.748861,1.321688,5.014180,-8.457043,0.593126,7.949960,8.666419,1.736096,3.529119,-1.891570,-9.188701,5.492560,3.513172,6.727971,4.525296,6.432411,9.068312,-9.341973,0.335684,-1.927126,2.186911,3.890380,-4.036738,-1.284019,-9.728157,1.838325,-9.298318,-1.659057,4.512488,5.466665,-1.989394,4.217203,7.838762,-0.358830,-0.796834,3.693285,2.655522,-4.315186,-4.511623,7.733143,-2.376700,2.846662,-9.947345,-4.592209,-4.032691,-8.705384,-7.595989,-8.863074,6.591967,-6.319236,8.834605,0.778482,-8.514585,7.286638,-4.830488,6.502964,5.171412,-0.127244,-6.689530,5.208474,-7.531127,-5.776085,-3.067777,2.517328,7.773067,2.550864,6.789773,7.704006,1.233466,-7.017270,-4.924655,-9.573362,5.134897,6.487534,2.765677,-0.084802,-6.673358,0.652232,7.717460,-3.122532,-2.650985,7.101682,-7.840286,-9.440236,4.528644,7.729824,-7.024978,-6.403871,-3.921940,-6.402385,-1.406685,-0.332265,2.140771,3.378973,-1.445188,5.235271,-2.585506,-1.530722,-3.618062,-5.258426,-2.784841,7.375877,4.533017,-5.686504,7.436680,7.776191,7.834415,-6.629182,3.457390,9.675614,3.531786,5.135898,1.744502,-4.963566,-3.742315,-3.223400,-7.269547,3.769233,8.396174,-0.089975,-3.297107,-3.987918,5.352541,-8.750844,8.551865,-6.235515,9.126493,-9.057650,2.036864,-4.955643,8.974577,-7.637701,-0.581812,7.954847,9.982255,-6.211830,3.539024,0.760999,1.134855,-5.518968,7.553965,3.142288,-4.274414,-3.074187,-9.768858,0.796184,2.040419,7.441997,7.791246,7.769424,-7.580470,7.999043,-2.664638,-9.279967,-1.553551,-6.592161,0.912859,-2.197746,4.659581], dtype = "float32")#candidate|7665|(405,)|const|float32
call_7664 = relay.TupleGetItem(func_1097_call(relay.reshape(const_7665.astype('float32'), [15, 3, 9])), 1)
call_7666 = relay.TupleGetItem(func_1099_call(relay.reshape(const_7665.astype('float32'), [15, 3, 9])), 1)
output = relay.Tuple([call_7649,call_7664,const_7665,])
output2 = relay.Tuple([call_7650,call_7666,const_7665,])
func_7671 = relay.Function([], output)
mod['func_7671'] = func_7671
mod = relay.transform.InferType()(mod)
output = func_7671()
func_7672 = relay.Function([], output)
mutated_mod['func_7672'] = func_7672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_988_call = mod.get_global_var('func_988')
func_990_call = mutated_mod.get_global_var('func_990')
call_7757 = relay.TupleGetItem(func_988_call(), 0)
call_7758 = relay.TupleGetItem(func_990_call(), 0)
func_6507_call = mod.get_global_var('func_6507')
func_6508_call = mutated_mod.get_global_var('func_6508')
call_7763 = relay.TupleGetItem(func_6507_call(), 1)
call_7764 = relay.TupleGetItem(func_6508_call(), 1)
uop_7767 = relay.acos(call_7763.astype('float64')) # shape=(11, 13, 8)
uop_7769 = relay.acos(call_7764.astype('float64')) # shape=(11, 13, 8)
func_1900_call = mod.get_global_var('func_1900')
func_1902_call = mutated_mod.get_global_var('func_1902')
const_7776 = relay.const([4,10,5,-3,9,-1,7,6,-3,-9,3,2,7,5,2,6,8,-1,9,-9,2,-3,3,-8,-10,9,-4,-1,-9,-6,6,6,-6,-8,-3,-5,-7,5,-10,8,9,-5,-10,-3,-5,-1,-1,-7,-6,-1,-10,-5,7,-6,-10,-8,4,3,2,-3,4,-7,1,-1,-9,-7,9,5,-9,-4,5,-9,5,-3,7,-5,-9,8,-8,-8,-9,5,4,-7,-1,3,3,7,5,7,5,7,-6,-4,1,-1], dtype = "uint8")#candidate|7776|(96,)|const|uint8
call_7775 = relay.TupleGetItem(func_1900_call(relay.reshape(const_7776.astype('uint8'), [96,])), 1)
call_7777 = relay.TupleGetItem(func_1902_call(relay.reshape(const_7776.astype('uint8'), [96,])), 1)
output = relay.Tuple([call_7757,uop_7767,call_7775,const_7776,])
output2 = relay.Tuple([call_7758,uop_7769,call_7777,const_7776,])
func_7788 = relay.Function([], output)
mod['func_7788'] = func_7788
mod = relay.transform.InferType()(mod)
mutated_mod['func_7788'] = func_7788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7788_call = mutated_mod.get_global_var('func_7788')
call_7789 = func_7788_call()
output = call_7789
func_7790 = relay.Function([], output)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7798 = relay.const([[[10,10,-2,1,3,-2,-10,-7,-3,-7]],[[-8,-4,-9,3,4,-1,3,-4,-10,-2]],[[-2,-4,-1,7,10,10,-6,4,-5,9]],[[4,-4,3,-1,4,8,8,-8,-2,2]],[[8,-1,-6,10,-10,1,-10,1,2,8]],[[5,-1,7,9,-4,-3,-3,-9,-9,-10]]], dtype = "int8")#candidate|7798|(6, 1, 10)|const|int8
var_7799 = relay.var("var_7799", dtype = "int8", shape = (6, 9, 10))#candidate|7799|(6, 9, 10)|var|int8
bop_7800 = relay.left_shift(const_7798.astype('int8'), var_7799.astype('int8')) # shape=(6, 9, 10)
uop_7808 = relay.log(bop_7800.astype('float32')) # shape=(6, 9, 10)
func_2364_call = mod.get_global_var('func_2364')
func_2365_call = mutated_mod.get_global_var('func_2365')
call_7819 = relay.TupleGetItem(func_2364_call(), 0)
call_7820 = relay.TupleGetItem(func_2365_call(), 0)
bop_7829 = relay.less_equal(uop_7808.astype('bool'), relay.reshape(bop_7800.astype('bool'), relay.shape_of(uop_7808))) # shape=(6, 9, 10)
func_2575_call = mod.get_global_var('func_2575')
func_2578_call = mutated_mod.get_global_var('func_2578')
var_7834 = relay.var("var_7834", dtype = "uint16", shape = (3, 24))#candidate|7834|(3, 24)|var|uint16
var_7835 = relay.var("var_7835", dtype = "float32", shape = (13,))#candidate|7835|(13,)|var|float32
call_7833 = relay.TupleGetItem(func_2575_call(relay.reshape(var_7834.astype('uint16'), [72,]), relay.reshape(var_7835.astype('float32'), [13,]), ), 6)
call_7836 = relay.TupleGetItem(func_2578_call(relay.reshape(var_7834.astype('uint16'), [72,]), relay.reshape(var_7835.astype('float32'), [13,]), ), 6)
bop_7843 = relay.add(uop_7808.astype('uint16'), relay.reshape(bop_7800.astype('uint16'), relay.shape_of(uop_7808))) # shape=(6, 9, 10)
func_6316_call = mod.get_global_var('func_6316')
func_6319_call = mutated_mod.get_global_var('func_6319')
const_7849 = relay.const([[False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True],[False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False],[True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False],[True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False],[False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True],[True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False],[False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,True,True],[False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,False],[False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True],[True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True],[True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,False,False,False],[True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True],[True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,True],[True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,False,True],[False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False],[True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False],[False,False,False,False,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True],[True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False],[False,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,True,True],[True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True],[False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True],[False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False],[True,False,False,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,False],[True,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True]], dtype = "bool")#candidate|7849|(24, 22)|const|bool
call_7848 = func_6316_call(relay.reshape(const_7849.astype('bool'), [6, 8, 11]))
call_7850 = func_6316_call(relay.reshape(const_7849.astype('bool'), [6, 8, 11]))
output = relay.Tuple([call_7819,bop_7829,call_7833,var_7834,var_7835,bop_7843,call_7848,const_7849,])
output2 = relay.Tuple([call_7820,bop_7829,call_7836,var_7834,var_7835,bop_7843,call_7850,const_7849,])
func_7865 = relay.Function([var_7799,var_7834,var_7835,], output)
mod['func_7865'] = func_7865
mod = relay.transform.InferType()(mod)
mutated_mod['func_7865'] = func_7865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7865_call = mutated_mod.get_global_var('func_7865')
var_7867 = relay.var("var_7867", dtype = "int8", shape = (6, 9, 10))#candidate|7867|(6, 9, 10)|var|int8
var_7868 = relay.var("var_7868", dtype = "uint16", shape = (3, 24))#candidate|7868|(3, 24)|var|uint16
var_7869 = relay.var("var_7869", dtype = "float32", shape = (13,))#candidate|7869|(13,)|var|float32
call_7866 = func_7865_call(var_7867,var_7868,var_7869,)
output = call_7866
func_7870 = relay.Function([var_7867,var_7868,var_7869,], output)
mutated_mod['func_7870'] = func_7870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6142_call = mod.get_global_var('func_6142')
func_6144_call = mutated_mod.get_global_var('func_6144')
call_7902 = relay.TupleGetItem(func_6142_call(), 1)
call_7903 = relay.TupleGetItem(func_6144_call(), 1)
func_1218_call = mod.get_global_var('func_1218')
func_1225_call = mutated_mod.get_global_var('func_1225')
const_7927 = relay.const([-4,7,-5,-1,8,-8,-10,-8,-3,-9,4,5,-4,-10,-3,-9,5,9,2,4,1,-8,-10,-9,3,-1,-8,2,1,-6,2,-3,3,6,1,-9,3,-5,-4,-4,-4,1,-3,-5,7,-3,7,6,8,-7,-4,-1,-2,2,3,-10,-2,9,5,4,-5,9,-10,2,-8,7,3,-1,-6,-10,8,6,-2,7,-10,9,7,7,-4,-5,8,-4,-10,8,7,-3,-10,7,5,-9,-7,10,8,-9,-6,7,-6,5,-8,-10,-10,2,-3,2,-4,-2,-1,5,10,4,-8,-10,-3,-10,9,-8,6,-9,-10,8,-3,-5,5,-4,3,2,10,-10,10,-4,2,8,-3,-9,-9,6,-9,6,2,2,-1,-1,-8,-4,10,7,-1,2,-5,6,7,-8,7,-2,-6,-6,-9,-10,7,5,-3,9,-9,-5,-1,-10,4,-7,-2,10,5,4,3,3,7,7,-10,3,9,-6,10,-9,4,5,-4,1,-1,5,1,5,-4,10,-1,7,-3,-10,-1,-9,-4,-8,-9,10,-7,5,-1,-8,5,2,4,-5,4,-2,-4,-9,-5,-7,-7,-4,1,2,10,-10,-1,10,-2,10,10,-3,3,3,9,2,-8,-8,-6,5,-2,10,7,-7,-2,-7,1,7,1,3,1,-6,4,9,6,-5,-9,2,-2,5,9,8,-1,5,-8,-4,6,7,-5,9,2,-2,8,5,4,-7,1,5,4,-7,-2,9,-10,9,7,-7,-3,-8,-2,2,2,-10,-7,-8,-7,-1,-6,7,1,1,4,-4,6,10,4,5,1,10,10,-9,1,-8,-2,-2,10,10,-1,3,-6,-5,-4,8,-6,7,6,-5,-8,3,7,-5,-1,5,1,1,-2,10,9,-5,-6,-2,-8,9,-9,10,-2,-7,1,-6,1,-2,4,-10,9,7,-8,8,-6,-4,1,-5,10,-5,1,3,-9,-6,4,5,1,-1,-10,7,-7,-5,6,1,-9,4,10,-3,-10,-1,4,10,-7,-6,-1,7,3,-6,9,4,-8,1,8,4,-2,4,10,-3,6,-7,2,5,-5,4,-2,5,9,-7,-9,-4,-7,-9,6,-5,-1,1,8,9,-9,-9,-5,3,8,10,-3,8,-7,-9,1,5,-10,-7,2,-2,-3,6,-3,2,10,-9,-10,-5,4,-10,-9,10,9,8,5,4,8,6,8,-3,3,1,8,10,1,-8,-5,2,6,-7,9,-9,-3,8,-4,-2,-4,-8,-1,4,-10,-2,3,-1,5,9,1,-9,-2,8,2,3,-2,-6,-1,5,-7,8,-3,8,-9,10,-7,-6,9,-7,3,7,-10,8,-5,5,-2,-3,-2,-4,10,-10,-6,7,8,6,-1,9,-8,-5,2,7,2,2,9,-4,-10,7,1,-3,6,-4,-4,10,-10,5,4,-5,-1,2,-2,10,-3,10,-9,-6,-4,-3,1,-10,-10,-2,-8,3,-5,9,5,9,-6,-5,4,1,-2,-8,-10,6,5,8,-5,1,8,-7,-9,3,7,-10,9,-1,-6,4,7,-9,7,6,-8,4,-8,1,9,-5,-1,-9,6,1,-1,1,-4,2,8,5,-4,-4,-10,-2,-8,-5,-1,9,-6,-1,-5,5,-3,-3,5,-4,7,-1,-2,3,-9,-9,3,-6,-10,4,-9,7,5,2,-7,9,4,-10,5,8,-2,-2,7,-3,-5,10,-7,-8,8,4,-6,-1,5,9,-5,-1,6,-1,1,7,3,4,6,-2,-9,2,-1,8,-6,-3,-5,-9,10,-1,-6,-9,-8,6,-4,-10,7,10,7,-4,-6,4,-3,-2,5,-4,-4,9,-7,-7,5,3,9,2,3,9,-10,1,-7,8,8,2,-6,-3], dtype = "uint16")#candidate|7927|(702,)|const|uint16
var_7928 = relay.var("var_7928", dtype = "float32", shape = (405,))#candidate|7928|(405,)|var|float32
var_7929 = relay.var("var_7929", dtype = "bool", shape = (1, 88))#candidate|7929|(1, 88)|var|bool
const_7930 = relay.const([[-0.616647],[2.899388],[-4.875225],[-1.556366],[0.263494],[-2.954830],[9.812505],[-4.488814],[-1.086300],[0.736459],[-7.255465],[-4.088367],[8.786734]], dtype = "float32")#candidate|7930|(13, 1)|const|float32
call_7926 = relay.TupleGetItem(func_1218_call(relay.reshape(const_7927.astype('uint16'), [1, 702]), relay.reshape(call_7902.astype('bool'), [6, 8, 11]), relay.reshape(var_7928.astype('float32'), [405,]), relay.reshape(var_7929.astype('bool'), [88,]), relay.reshape(const_7930.astype('float32'), [13,]), ), 1)
call_7931 = relay.TupleGetItem(func_1225_call(relay.reshape(const_7927.astype('uint16'), [1, 702]), relay.reshape(call_7902.astype('bool'), [6, 8, 11]), relay.reshape(var_7928.astype('float32'), [405,]), relay.reshape(var_7929.astype('bool'), [88,]), relay.reshape(const_7930.astype('float32'), [13,]), ), 1)
output = relay.Tuple([call_7902,call_7926,const_7927,var_7928,var_7929,const_7930,])
output2 = relay.Tuple([call_7903,call_7931,const_7927,var_7928,var_7929,const_7930,])
func_7932 = relay.Function([var_7928,var_7929,], output)
mod['func_7932'] = func_7932
mod = relay.transform.InferType()(mod)
mutated_mod['func_7932'] = func_7932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7932_call = mutated_mod.get_global_var('func_7932')
var_7934 = relay.var("var_7934", dtype = "float32", shape = (405,))#candidate|7934|(405,)|var|float32
var_7935 = relay.var("var_7935", dtype = "bool", shape = (1, 88))#candidate|7935|(1, 88)|var|bool
call_7933 = func_7932_call(var_7934,var_7935,)
output = call_7933
func_7936 = relay.Function([var_7934,var_7935,], output)
mutated_mod['func_7936'] = func_7936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5892_call = mod.get_global_var('func_5892')
func_5893_call = mutated_mod.get_global_var('func_5893')
call_7978 = relay.TupleGetItem(func_5892_call(), 1)
call_7979 = relay.TupleGetItem(func_5893_call(), 1)
func_5892_call = mod.get_global_var('func_5892')
func_5893_call = mutated_mod.get_global_var('func_5893')
call_7990 = relay.TupleGetItem(func_5892_call(), 2)
call_7991 = relay.TupleGetItem(func_5893_call(), 2)
output = relay.Tuple([call_7978,call_7990,])
output2 = relay.Tuple([call_7979,call_7991,])
func_7996 = relay.Function([], output)
mod['func_7996'] = func_7996
mod = relay.transform.InferType()(mod)
output = func_7996()
func_7997 = relay.Function([], output)
mutated_mod['func_7997'] = func_7997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5165_call = mutated_mod.get_global_var('func_5165')
call_7998 = func_5164_call()
call_7999 = func_5164_call()
output = relay.Tuple([call_7998,])
output2 = relay.Tuple([call_7999,])
func_8017 = relay.Function([], output)
mod['func_8017'] = func_8017
mod = relay.transform.InferType()(mod)
output = func_8017()
func_8018 = relay.Function([], output)
mutated_mod['func_8018'] = func_8018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8040 = relay.var("var_8040", dtype = "float32", shape = (7, 10, 12))#candidate|8040|(7, 10, 12)|var|float32
const_8041 = relay.const([[[3.202484,-4.990218,-9.206226,-8.065159,-2.204881,-4.982419,9.873471,6.831624,6.685548,0.499575,9.176124,3.791106],[4.506003,-0.679737,1.219309,3.477603,5.944011,4.780638,-3.189735,-7.502123,-3.959766,9.779536,-5.867055,3.828918],[-1.919749,3.028521,0.409783,3.361125,5.328559,5.390100,5.254965,8.911492,-5.636010,-0.777137,-3.265160,8.300503],[-8.385929,-1.485825,0.858217,-8.374452,6.989451,0.740656,7.609107,1.772382,-0.535422,6.109893,0.686466,-1.308703],[6.390118,5.326927,-9.854247,1.933456,6.849564,7.204148,6.200425,-6.737284,-1.713218,-3.133312,-3.301311,-1.338708],[-9.619201,-5.990084,-3.650675,5.646517,-6.353860,-2.665660,1.491636,8.166136,8.970296,1.761099,-6.171528,6.732982],[3.042879,-1.633729,1.877811,-6.041433,1.702445,-0.862660,-6.385435,8.620751,-5.408727,7.501664,3.194187,-9.003704],[6.987264,-8.365584,7.068801,-6.730657,2.177819,-1.784313,0.496859,-0.424538,9.994563,1.643500,-8.882564,-1.883404],[-9.316924,-0.174653,-9.668197,-2.664912,-7.298978,-7.525710,6.134787,-6.199205,9.268356,0.634132,1.960725,2.393436],[-1.627583,-8.188626,-1.783864,0.095670,-2.508488,-3.956425,-9.321608,3.997051,6.785281,-6.249512,-3.767849,5.303114]],[[8.781236,2.823207,-6.848380,-1.376604,1.530902,6.197813,1.475325,-5.757678,-5.583757,0.685597,6.772273,3.556046],[-7.897366,9.089036,-7.226370,-4.376106,-6.758839,6.879045,4.542327,2.045066,-0.751978,-6.146024,-1.242661,-5.816043],[0.417558,7.139109,-7.135090,-7.742801,0.366235,0.862965,-8.109550,0.316458,7.047169,-7.477819,-3.473699,3.900616],[-3.924820,1.480970,-3.448959,-9.520609,4.295725,8.703101,-3.581348,-2.608770,7.689743,-3.493940,9.575523,-2.925375],[-8.167801,1.493207,2.771291,8.694610,-6.392378,-4.295793,-3.069872,3.744796,-6.870242,6.893657,-9.827589,-4.635949],[-5.803919,9.380481,7.897641,-5.709139,-1.381579,-5.914036,4.648033,-6.372423,-9.017576,-3.083075,7.504456,-3.857301],[-7.085697,-1.986154,8.478024,2.088531,0.021093,-3.541515,-9.973228,-0.565078,-4.349052,-6.857329,2.997070,-5.054853],[7.795986,-8.394613,-8.974483,6.852435,9.738242,5.949662,-7.512370,-3.721301,7.692039,-2.321560,8.808003,7.240096],[-5.864490,8.268216,-0.498986,8.298495,0.849774,-3.171905,9.438324,-2.342266,5.445912,8.468102,-6.511613,-2.781162],[-8.789407,-6.500060,3.723405,-9.076437,8.926548,1.508901,9.970617,-8.473491,9.506922,-0.257710,-2.182170,2.949107]],[[-3.616641,4.085748,-0.616884,-9.011044,0.781555,-1.010663,-4.228354,-6.290078,7.779456,7.842806,-6.744097,2.602472],[-5.658655,-3.284508,-5.781705,9.557340,7.650149,-4.070311,-2.361192,-0.271881,0.154667,-8.238077,9.299299,4.510743],[6.625466,8.935617,-8.608017,3.249699,-3.452230,8.589200,2.567904,8.313576,-8.052389,-4.850067,8.762522,-3.523888],[9.017438,-6.595779,2.052036,2.603857,4.233527,-1.796165,4.791264,-7.488920,-3.284167,0.919851,-9.161051,-9.633154],[-0.852491,0.160206,3.805221,-8.051874,4.553747,-2.857859,-0.502318,3.237498,-6.647911,-7.687190,6.605562,-2.522275],[-6.440543,6.947328,-1.214337,8.980203,-9.992660,-1.084996,-5.538286,-5.055005,-4.181804,-4.668409,1.980163,-9.129827],[-7.032837,6.793082,3.969613,0.353085,9.316644,3.595422,-0.922374,-5.978311,9.415122,-7.621639,8.351520,2.754398],[1.680485,8.548425,2.851622,5.104690,-6.738784,2.091271,-7.938935,7.883212,0.503568,3.277872,-4.342555,-0.852009],[8.705147,3.341732,-8.748625,-2.440747,0.004935,-2.569391,0.723539,-6.598134,-2.252710,6.273941,-8.128725,3.810264],[0.523439,0.700544,-2.217049,-1.897304,-9.392788,1.470047,-6.026666,8.052060,7.257350,4.492172,0.170985,-6.765104]],[[1.085822,-9.124433,-8.459089,-0.568002,-7.573738,4.584312,8.249777,-0.926370,-5.268446,-0.522673,1.562976,-5.652951],[5.742947,8.197641,6.055295,7.548618,-6.764814,-6.392785,9.775963,-5.820878,-3.784185,-5.114256,9.845251,8.069105],[-7.878710,7.773114,6.914888,-9.803352,3.627129,0.731971,7.486032,2.836942,-7.392277,9.027003,-5.454657,-9.312285],[3.990499,0.361354,4.653392,-7.951554,-6.665306,-9.755974,4.759746,1.753072,-6.052562,6.836143,1.837832,5.314686],[-0.386545,5.407988,5.113439,1.163759,-3.874704,8.829155,-7.957141,-0.495359,8.280012,-6.440419,8.285726,4.058891],[9.443032,-4.475023,-5.197006,-6.340700,-5.669860,4.418446,9.223374,-5.926661,4.602922,-3.491991,-4.800436,4.488555],[5.766821,-9.036983,1.657590,-0.590851,4.287278,9.489006,9.524916,-2.477277,6.018912,3.949746,3.833405,-0.368146],[2.511446,-9.185822,1.414026,-6.757841,2.937247,-2.535395,-0.258630,9.697921,8.302837,6.815446,7.829122,-7.378124],[-5.251042,8.294411,9.806146,-0.364335,-8.224424,-7.428886,-0.264161,-9.451947,-3.002049,-0.511324,-2.334784,-4.459296],[-7.780732,-3.591058,2.712151,-4.300403,-7.140833,4.475903,-7.563435,-2.860717,-0.909929,-8.670120,3.641318,5.317814]],[[4.115845,8.120661,1.212967,7.055546,3.978785,8.829533,-3.556137,-9.098530,-1.984521,3.786247,-5.026740,6.155056],[-3.105722,6.968420,2.985223,1.590835,7.116894,-5.347970,-0.419257,-3.230450,1.238913,9.885924,-4.720148,-3.351811],[0.749444,5.155024,7.544697,1.374934,-7.820381,-8.637084,2.339363,7.662026,-6.571297,4.017093,5.080327,-5.190499],[-9.947837,8.770348,-3.622815,9.022889,0.248746,5.323518,7.392965,-9.833909,3.184057,2.639673,6.620385,8.603217],[-6.947602,-3.063299,2.671335,-2.965053,-2.778382,-9.967700,4.005992,8.606655,-4.989094,-4.335318,6.347916,4.746948],[2.453660,2.931375,9.713529,-9.972260,8.513349,-7.585409,4.277220,-1.003863,-9.443937,-8.819548,-4.913719,-0.916977],[-2.528311,5.600585,4.363731,8.858838,2.842110,4.801218,7.231228,2.428880,7.166719,1.405535,-0.691151,-8.411525],[-9.416829,6.031680,-9.059384,8.799140,-1.712625,-7.187944,-2.068491,-8.314855,-1.525169,-8.341805,4.526915,3.151650],[5.971491,9.332304,-4.882846,-6.389787,6.747668,-8.060392,6.791265,-3.518826,-0.941840,-1.268677,-0.215026,-4.039914],[-3.479319,4.120713,-4.388785,-5.245574,2.882857,-6.641617,-4.200683,6.136870,-1.707656,2.886794,8.482498,3.943906]],[[9.495142,-4.525786,-3.865964,-3.414440,-5.738287,-5.322264,-9.988290,-8.958857,-1.738006,-0.172080,-1.779205,-0.256662],[9.032873,-7.353761,-0.879488,-5.417928,7.030584,4.779056,3.606386,6.085249,2.277438,8.328656,-9.085587,-8.399151],[-3.074145,6.306880,-7.830119,9.781323,-0.657546,-6.506516,8.551637,-5.681813,-8.139256,-1.015663,7.466489,9.278133],[9.506182,7.108472,-9.883791,-3.695558,-8.744394,4.769197,-7.898199,-3.392349,2.713172,8.999215,6.499057,5.197945],[4.880457,6.413918,8.054297,-1.985194,9.729569,5.402749,6.095625,-0.800146,0.768434,-0.738875,-1.093685,-5.655461],[4.683267,-7.992152,3.381761,-5.376617,0.200351,-4.895475,-7.216262,1.124780,-8.585269,-2.650196,4.458864,7.812084],[-8.966283,-6.011881,-7.449304,-9.581787,-1.831928,-4.950225,9.846182,-8.465806,-1.411550,1.337752,9.833598,7.534342],[5.182827,6.111486,-8.644448,-6.613692,-8.064280,-8.084139,4.157632,7.763747,9.236108,-6.629526,-4.053955,-5.657934],[8.497347,-8.028488,-7.370792,-3.336460,4.884391,-2.208287,-8.295017,-1.173406,4.932289,2.149489,-4.432840,-0.126578],[-4.531033,-9.210099,-2.731449,7.685492,-2.420155,-2.832320,2.470906,9.588761,5.750656,9.561212,-2.685062,-6.997743]],[[-3.931937,-0.351253,-9.130073,-3.879187,7.215721,-7.418650,1.820967,7.821993,8.120947,3.883953,-8.349463,2.446628],[-5.109640,3.455029,-5.702805,1.184277,8.040329,2.154512,-7.593597,-4.008025,-4.055635,8.875794,1.538147,-7.153186],[6.234928,7.876433,-9.085696,2.089665,7.122875,3.369175,-6.527418,-7.910043,-8.361176,-2.314209,-4.693984,4.339471],[2.136987,-0.782209,0.636262,9.701532,-3.506534,3.662634,7.964506,-6.539158,9.514783,-1.999337,-4.261752,-4.076903],[1.487101,2.674038,9.066307,-2.776898,-6.573965,9.754503,5.864384,-4.415193,-9.715329,-6.563566,-4.649981,-7.244179],[-0.604283,3.270661,-6.001966,-2.897249,-2.084624,7.706757,-1.123484,-6.928694,-5.188708,-5.772916,-8.225874,-3.108963],[-9.807875,-1.407912,3.153861,2.562938,-4.742910,-7.807400,-8.405033,-0.381643,-9.695921,-9.163849,6.723124,8.549848],[9.747846,-4.588303,-7.460046,-8.662417,0.692514,7.043966,7.010119,5.791706,-8.947959,-5.715752,-7.768162,9.799099],[-1.477387,4.848770,5.071258,-8.909241,-3.448196,-9.558861,7.475078,-8.475078,-8.156216,8.999328,-4.703827,4.662671],[-1.614758,7.358432,-5.750643,6.930950,-6.132727,-5.213501,-4.135693,-0.543540,8.295949,4.911384,0.420020,-1.640044]]], dtype = "float32")#candidate|8041|(7, 10, 12)|const|float32
bop_8042 = relay.divide(var_8040.astype('float32'), relay.reshape(const_8041.astype('float32'), relay.shape_of(var_8040))) # shape=(7, 10, 12)
output = relay.Tuple([bop_8042,])
output2 = relay.Tuple([bop_8042,])
F = relay.Function([var_8040,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8040,], output2)
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
