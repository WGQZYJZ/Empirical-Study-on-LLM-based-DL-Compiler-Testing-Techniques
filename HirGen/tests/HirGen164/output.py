import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_159 = relay.const(7, dtype = "uint32")#candidate|159|()|const|uint32
var_160 = relay.var("var_160", dtype = "uint32", shape = (6, 5, 7))#candidate|160|(6, 5, 7)|var|uint32
bop_161 = relay.bitwise_xor(const_159.astype('uint32'), var_160.astype('uint32')) # shape=(6, 5, 7)
output = bop_161
output2 = bop_161
func_168 = relay.Function([var_160,], output)
mod['func_168'] = func_168
mod = relay.transform.InferType()(mod)
var_169 = relay.var("var_169", dtype = "uint32", shape = (6, 5, 7))#candidate|169|(6, 5, 7)|var|uint32
output = func_168(var_169)
func_170 = relay.Function([var_169], output)
mutated_mod['func_170'] = func_170
mutated_mod = relay.transform.InferType()(mutated_mod)
const_178 = relay.const([[[-6,-7,4,-1,-6,6,-3,-4,8,6,5,-1,-9,6],[3,-3,4,1,7,4,-2,-1,-1,-3,10,-6,3,5],[-8,-9,6,-2,-2,-2,-7,-10,-9,2,-5,-9,-4,-9],[-10,-10,-9,1,-1,-8,8,-1,8,-3,-4,7,10,4],[10,-1,-10,-1,2,-4,5,-7,6,7,1,1,5,-5]],[[-5,-10,-2,7,4,1,-8,-10,-1,-7,6,10,-5,5],[10,-6,-8,-2,-7,-4,-5,-6,2,-7,4,-9,-9,2],[-10,4,6,7,-6,6,-7,2,-5,-6,-8,-1,10,-5],[-7,-5,-3,-8,-10,-4,-5,-8,1,6,-2,-7,7,3],[6,-6,-6,-1,-9,9,-6,-6,3,3,7,4,-2,-10]],[[-8,8,-2,6,-7,-6,-4,8,7,-10,7,6,5,-3],[-10,-7,5,-2,-10,-6,5,-3,-8,10,-4,-6,6,-5],[4,9,1,4,-9,-5,-7,8,-5,-1,-4,6,1,-9],[8,9,3,9,4,-4,-2,-4,1,10,-4,7,-2,-6],[-9,-4,-2,-10,-1,-3,-4,7,-5,6,-4,-2,-9,-8]],[[3,6,2,10,10,-1,9,-7,-8,-1,-7,10,5,-2],[2,5,-8,7,8,-4,-7,3,-6,1,5,10,2,5],[-2,2,-9,-9,-10,6,6,-8,2,1,2,-3,-5,-10],[3,-4,2,-10,7,-9,8,2,-5,6,-4,7,-8,-4],[5,2,9,6,-4,-4,8,5,-1,9,-1,-5,-2,4]],[[5,3,-2,-2,10,2,-6,6,-2,-1,2,-10,5,-10],[8,-6,-10,4,5,2,-4,1,5,-6,-10,1,-7,5],[-6,10,6,6,-7,9,6,7,-10,-2,6,3,4,-8],[-4,-2,7,-6,-10,-1,5,-8,5,-3,-4,9,4,7],[-5,7,-9,2,3,-7,10,-1,-9,-8,-4,9,-9,-1]],[[-10,8,-5,-7,-6,-8,-6,-3,4,3,-2,-8,-5,8],[7,6,-6,-3,1,-3,6,5,8,-10,3,8,6,6],[2,7,1,-7,8,-10,-9,-6,-6,-8,-1,9,-2,3],[-10,1,-3,3,10,5,-1,6,9,4,-5,10,-9,-1],[-5,-10,3,8,8,4,-3,-9,-3,4,-9,5,-9,7]],[[5,10,4,4,-1,-7,-8,-10,-7,7,4,-10,-8,-4],[-4,-8,10,-9,-9,-4,-9,-1,10,-8,-8,7,-4,2],[3,-10,8,-8,-5,-5,-1,-5,9,-7,-7,6,-10,7],[3,10,5,5,-8,-4,-9,9,7,10,2,-5,-2,4],[7,8,1,5,9,-1,-2,-2,-5,1,-7,-10,-6,-9]]], dtype = "uint64")#candidate|178|(7, 5, 14)|const|uint64
const_179 = relay.const([[[-5,3,9,9,7,-8,8,9,6,-10,-1,-6,3,-8],[5,4,-8,7,2,7,-2,8,-9,-3,-10,-3,-8,-2],[4,10,5,-1,-3,-10,4,6,2,-5,-5,-4,-5,-4],[6,4,5,9,-7,2,-1,-7,-10,3,9,3,-10,6],[5,-6,7,9,3,-9,2,-2,-4,10,-2,-7,2,-2]],[[8,6,10,-4,-4,-7,3,-7,9,-8,8,10,10,10],[9,4,2,1,-2,8,-8,-2,3,7,-9,-7,-4,9],[-4,8,1,-1,2,6,6,9,-9,8,10,-5,4,-8],[-7,-6,3,2,-8,10,6,-3,8,-10,-4,-10,-6,3],[-7,10,-7,-2,-10,6,-9,7,2,10,3,8,10,2]],[[-5,6,8,-3,-4,-5,3,-4,10,10,3,-4,1,6],[2,-5,-4,8,-1,-7,9,-1,5,-5,-7,7,-6,-8],[2,6,1,2,6,-9,2,2,-8,-4,-8,-8,-5,-5],[-3,-5,7,9,-5,-5,-1,-8,10,6,2,-1,-2,-5],[1,7,-3,10,-6,-9,-10,-1,-9,-7,8,-7,5,3]],[[6,-4,10,-2,6,4,-1,-2,-7,3,2,7,5,-2],[-3,-8,7,-7,-5,-1,-8,-4,7,-1,9,-2,-6,-2],[-4,-1,-1,7,5,4,-2,-3,-9,-1,-1,3,-8,10],[6,7,6,1,9,7,2,3,8,6,1,6,-4,3],[-3,-8,-6,-1,10,-2,-9,-2,2,-7,-9,10,2,5]],[[2,-8,10,-6,-8,9,-6,-9,-1,6,-4,6,5,7],[-9,-5,-10,-7,-8,7,7,-6,-10,-8,5,4,6,-7],[5,10,6,-6,8,-7,6,4,3,-6,4,1,9,-1],[7,-6,3,4,-1,6,-4,8,10,-3,10,3,5,-5],[1,-9,-7,-1,-1,10,7,-3,-2,1,1,-2,-5,-6]],[[10,7,1,-2,-1,9,-1,-3,-6,9,7,9,-8,-10],[-5,-5,2,-10,8,-3,6,10,-10,6,-3,-5,9,-10],[-4,-9,-9,-6,8,3,-8,6,8,-3,-3,8,6,-6],[-7,1,5,10,4,-4,-4,10,-5,7,-4,-4,9,-3],[-7,-9,3,8,8,3,-6,6,-8,-1,5,-6,6,6]],[[-6,-2,7,-7,-9,-8,3,-3,-10,8,-7,1,-4,-1],[-1,-8,7,7,-1,-2,-9,9,4,10,1,2,-4,-10],[-1,1,-9,6,10,7,8,-4,-2,7,-5,1,-5,-5],[-7,-7,7,10,-8,-3,-8,10,2,2,-6,-1,8,-8],[9,1,-10,4,-6,-5,-9,-3,-7,-6,8,4,-9,-7]]], dtype = "uint64")#candidate|179|(7, 5, 14)|const|uint64
bop_180 = relay.left_shift(const_178.astype('uint64'), relay.reshape(const_179.astype('uint64'), relay.shape_of(const_178))) # shape=(7, 5, 14)
output = bop_180
output2 = bop_180
func_194 = relay.Function([], output)
mod['func_194'] = func_194
mod = relay.transform.InferType()(mod)
output = func_194()
func_195 = relay.Function([], output)
mutated_mod['func_195'] = func_195
mutated_mod = relay.transform.InferType()(mutated_mod)
var_247 = relay.var("var_247", dtype = "float64", shape = (3, 5, 11))#candidate|247|(3, 5, 11)|var|float64
uop_248 = relay.exp(var_247.astype('float64')) # shape=(3, 5, 11)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_251 = func_194_call()
call_252 = func_194_call()
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
var_258 = relay.var("var_258", dtype = "uint32", shape = (210,))#candidate|258|(210,)|var|uint32
call_257 = func_168_call(relay.reshape(var_258.astype('uint32'), [6, 5, 7]))
call_259 = func_168_call(relay.reshape(var_258.astype('uint32'), [6, 5, 7]))
bop_264 = relay.less(call_257.astype('bool'), relay.reshape(var_258.astype('bool'), relay.shape_of(call_257))) # shape=(6, 5, 7)
bop_267 = relay.less(call_259.astype('bool'), relay.reshape(var_258.astype('bool'), relay.shape_of(call_259))) # shape=(6, 5, 7)
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
call_273 = func_168_call(relay.reshape(call_257.astype('uint32'), [6, 5, 7]))
call_274 = func_168_call(relay.reshape(call_257.astype('uint32'), [6, 5, 7]))
bop_275 = relay.add(uop_248.astype('int64'), relay.reshape(var_247.astype('int64'), relay.shape_of(uop_248))) # shape=(3, 5, 11)
output = relay.Tuple([call_251,bop_264,call_273,bop_275,])
output2 = relay.Tuple([call_252,bop_267,call_274,bop_275,])
func_279 = relay.Function([var_247,var_258,], output)
mod['func_279'] = func_279
mod = relay.transform.InferType()(mod)
mutated_mod['func_279'] = func_279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_279_call = mutated_mod.get_global_var('func_279')
var_281 = relay.var("var_281", dtype = "float64", shape = (3, 5, 11))#candidate|281|(3, 5, 11)|var|float64
var_282 = relay.var("var_282", dtype = "uint32", shape = (210,))#candidate|282|(210,)|var|uint32
call_280 = func_279_call(var_281,var_282,)
output = call_280
func_283 = relay.Function([var_281,var_282,], output)
mutated_mod['func_283'] = func_283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_310 = func_194_call()
call_311 = func_194_call()
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
var_317 = relay.var("var_317", dtype = "uint32", shape = (210,))#candidate|317|(210,)|var|uint32
call_316 = func_168_call(relay.reshape(var_317.astype('uint32'), [6, 5, 7]))
call_318 = func_168_call(relay.reshape(var_317.astype('uint32'), [6, 5, 7]))
uop_323 = relay.sin(call_316.astype('float64')) # shape=(6, 5, 7)
uop_325 = relay.sin(call_318.astype('float64')) # shape=(6, 5, 7)
output = relay.Tuple([call_310,var_317,uop_323,])
output2 = relay.Tuple([call_311,var_317,uop_325,])
func_340 = relay.Function([var_317,], output)
mod['func_340'] = func_340
mod = relay.transform.InferType()(mod)
mutated_mod['func_340'] = func_340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_341 = relay.var("var_341", dtype = "uint32", shape = (210,))#candidate|341|(210,)|var|uint32
func_340_call = mutated_mod.get_global_var('func_340')
call_342 = func_340_call(var_341)
output = call_342
func_343 = relay.Function([var_341], output)
mutated_mod['func_343'] = func_343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_493 = func_194_call()
call_494 = func_194_call()
output = call_493
output2 = call_494
func_500 = relay.Function([], output)
mod['func_500'] = func_500
mod = relay.transform.InferType()(mod)
mutated_mod['func_500'] = func_500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mutated_mod.get_global_var('func_500')
call_501 = func_500_call()
output = call_501
func_502 = relay.Function([], output)
mutated_mod['func_502'] = func_502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_531 = func_500_call()
call_532 = func_500_call()
var_535 = relay.var("var_535", dtype = "uint64", shape = (7, 5, 14))#candidate|535|(7, 5, 14)|var|uint64
bop_536 = relay.less(call_531.astype('bool'), relay.reshape(var_535.astype('bool'), relay.shape_of(call_531))) # shape=(7, 5, 14)
bop_539 = relay.less(call_532.astype('bool'), relay.reshape(var_535.astype('bool'), relay.shape_of(call_532))) # shape=(7, 5, 14)
output = relay.Tuple([bop_536,])
output2 = relay.Tuple([bop_539,])
func_547 = relay.Function([var_535,], output)
mod['func_547'] = func_547
mod = relay.transform.InferType()(mod)
var_548 = relay.var("var_548", dtype = "uint64", shape = (7, 5, 14))#candidate|548|(7, 5, 14)|var|uint64
output = func_547(var_548)
func_549 = relay.Function([var_548], output)
mutated_mod['func_549'] = func_549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_556 = func_500_call()
call_557 = func_500_call()
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_559 = func_500_call()
call_560 = func_500_call()
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_561 = func_500_call()
call_562 = func_500_call()
output = relay.Tuple([call_556,call_559,call_561,])
output2 = relay.Tuple([call_557,call_560,call_562,])
func_575 = relay.Function([], output)
mod['func_575'] = func_575
mod = relay.transform.InferType()(mod)
mutated_mod['func_575'] = func_575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mutated_mod.get_global_var('func_575')
call_576 = func_575_call()
output = call_576
func_577 = relay.Function([], output)
mutated_mod['func_577'] = func_577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_592 = func_194_call()
call_593 = func_194_call()
output = call_592
output2 = call_593
func_595 = relay.Function([], output)
mod['func_595'] = func_595
mod = relay.transform.InferType()(mod)
output = func_595()
func_596 = relay.Function([], output)
mutated_mod['func_596'] = func_596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_577_call = mutated_mod.get_global_var('func_577')
call_632 = relay.TupleGetItem(func_575_call(), 2)
call_633 = relay.TupleGetItem(func_577_call(), 2)
var_642 = relay.var("var_642", dtype = "uint64", shape = (7, 5, 14))#candidate|642|(7, 5, 14)|var|uint64
bop_643 = relay.right_shift(call_632.astype('int16'), relay.reshape(var_642.astype('int16'), relay.shape_of(call_632))) # shape=(7, 5, 14)
bop_646 = relay.right_shift(call_633.astype('int16'), relay.reshape(var_642.astype('int16'), relay.shape_of(call_633))) # shape=(7, 5, 14)
uop_654 = relay.erf(var_642.astype('float32')) # shape=(7, 5, 14)
uop_661 = relay.exp(uop_654.astype('float32')) # shape=(7, 5, 14)
output = relay.Tuple([bop_643,uop_661,])
output2 = relay.Tuple([bop_646,uop_661,])
func_664 = relay.Function([var_642,], output)
mod['func_664'] = func_664
mod = relay.transform.InferType()(mod)
mutated_mod['func_664'] = func_664
mutated_mod = relay.transform.InferType()(mutated_mod)
var_665 = relay.var("var_665", dtype = "uint64", shape = (7, 5, 14))#candidate|665|(7, 5, 14)|var|uint64
func_664_call = mutated_mod.get_global_var('func_664')
call_666 = func_664_call(var_665)
output = call_666
func_667 = relay.Function([var_665], output)
mutated_mod['func_667'] = func_667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_674 = func_595_call()
call_675 = func_595_call()
output = relay.Tuple([call_674,])
output2 = relay.Tuple([call_675,])
func_681 = relay.Function([], output)
mod['func_681'] = func_681
mod = relay.transform.InferType()(mod)
output = func_681()
func_682 = relay.Function([], output)
mutated_mod['func_682'] = func_682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_683 = func_194_call()
call_684 = func_194_call()
output = call_683
output2 = call_684
func_685 = relay.Function([], output)
mod['func_685'] = func_685
mod = relay.transform.InferType()(mod)
mutated_mod['func_685'] = func_685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mutated_mod.get_global_var('func_685')
call_686 = func_685_call()
output = call_686
func_687 = relay.Function([], output)
mutated_mod['func_687'] = func_687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_707 = func_194_call()
call_708 = func_194_call()
func_279_call = mod.get_global_var('func_279')
func_283_call = mutated_mod.get_global_var('func_283')
const_714 = relay.const([6.730304,5.723501,3.886958,8.811996,1.670694,-8.584897,0.733503,4.570929,8.840423,7.163311,-4.533582,-2.856403,-9.797713,-4.755925,9.716881,0.456518,1.503316,9.617404,-0.684349,-7.491665,7.723169,-9.623860,-0.906519,-1.546756,4.571646,6.165701,2.970097,9.961476,6.905453,0.680761,8.504965,1.262972,9.753011,1.163295,3.707133,9.803075,-2.867469,-9.824743,-8.026288,-6.699455,-4.045720,6.828166,-8.463897,8.127232,8.981157,-4.107458,7.232346,8.260479,7.280331,7.621895,6.633171,4.565813,-2.265831,-6.460201,-9.773690,-4.099015,-1.459966,2.853706,9.827811,-7.217780,1.719442,3.434564,5.727825,-6.381508,-5.773694,9.938826,-6.445419,5.303939,-1.156242,2.254048,4.272491,9.552439,-0.864532,-7.905502,1.821746,-4.320675,9.823808,-9.802783,-8.099973,4.001887,-3.525033,-2.971993,8.229145,9.361672,7.677587,1.450560,-6.340989,7.893622,3.354937,-3.439715,-5.244390,1.497557,5.201546,-4.919795,-1.193780,-1.573228,3.926316,-9.929558,-0.303947,-0.025445,-1.334608,-0.879388,2.639803,1.269881,6.200269,5.758582,-9.043822,-2.162426,-3.344381,-7.488088,-1.267109,3.794770,8.009219,1.066606,4.119188,-8.008542,3.470218,1.915485,-8.478206,1.532456,-7.302623,6.443369,9.362381,-5.373294,7.850619,1.026522,5.448772,3.803651,-9.740872,3.740315,-0.411011,7.768986,-5.000950,-9.471010,-7.295501,1.874868,7.529140,0.434013,-4.399368,-7.398017,-2.542434,7.299420,8.104757,8.242160,5.910867,7.445050,-2.005647,8.440420,5.773656,7.196157,7.315450,1.476315,9.889988,-7.001876,-3.108626,7.210441,-2.305013,0.856118,0.434102,9.715409,8.960771,2.726901,2.490151,-9.027132,-7.241589], dtype = "float64")#candidate|714|(165,)|const|float64
var_715 = relay.var("var_715", dtype = "uint32", shape = (210,))#candidate|715|(210,)|var|uint32
call_713 = relay.TupleGetItem(func_279_call(relay.reshape(const_714.astype('float64'), [3, 5, 11]), relay.reshape(var_715.astype('uint32'), [210,]), ), 3)
call_716 = relay.TupleGetItem(func_283_call(relay.reshape(const_714.astype('float64'), [3, 5, 11]), relay.reshape(var_715.astype('uint32'), [210,]), ), 3)
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
call_720 = relay.TupleGetItem(func_664_call(relay.reshape(call_707.astype('uint64'), [7, 5, 14])), 0)
call_721 = relay.TupleGetItem(func_667_call(relay.reshape(call_707.astype('uint64'), [7, 5, 14])), 0)
func_575_call = mod.get_global_var('func_575')
func_577_call = mutated_mod.get_global_var('func_577')
call_728 = relay.TupleGetItem(func_575_call(), 0)
call_729 = relay.TupleGetItem(func_577_call(), 0)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_734 = func_685_call()
call_735 = func_685_call()
bop_738 = relay.bitwise_xor(call_707.astype('int16'), relay.reshape(call_720.astype('int16'), relay.shape_of(call_707))) # shape=(7, 5, 14)
bop_741 = relay.bitwise_xor(call_708.astype('int16'), relay.reshape(call_721.astype('int16'), relay.shape_of(call_708))) # shape=(7, 5, 14)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_753 = func_595_call()
call_754 = func_595_call()
output = relay.Tuple([call_713,const_714,var_715,call_728,call_734,bop_738,call_753,])
output2 = relay.Tuple([call_716,const_714,var_715,call_729,call_735,bop_741,call_754,])
func_757 = relay.Function([var_715,], output)
mod['func_757'] = func_757
mod = relay.transform.InferType()(mod)
var_758 = relay.var("var_758", dtype = "uint32", shape = (210,))#candidate|758|(210,)|var|uint32
output = func_757(var_758)
func_759 = relay.Function([var_758], output)
mutated_mod['func_759'] = func_759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_769 = func_194_call()
call_770 = func_194_call()
var_773 = relay.var("var_773", dtype = "uint64", shape = (7, 5, 14))#candidate|773|(7, 5, 14)|var|uint64
bop_774 = relay.floor_divide(call_769.astype('float64'), relay.reshape(var_773.astype('float64'), relay.shape_of(call_769))) # shape=(7, 5, 14)
bop_777 = relay.floor_divide(call_770.astype('float64'), relay.reshape(var_773.astype('float64'), relay.shape_of(call_770))) # shape=(7, 5, 14)
output = relay.Tuple([bop_774,])
output2 = relay.Tuple([bop_777,])
func_778 = relay.Function([var_773,], output)
mod['func_778'] = func_778
mod = relay.transform.InferType()(mod)
var_779 = relay.var("var_779", dtype = "uint64", shape = (7, 5, 14))#candidate|779|(7, 5, 14)|var|uint64
output = func_778(var_779)
func_780 = relay.Function([var_779], output)
mutated_mod['func_780'] = func_780
mutated_mod = relay.transform.InferType()(mutated_mod)
var_821 = relay.var("var_821", dtype = "float32", shape = (5, 4, 10))#candidate|821|(5, 4, 10)|var|float32
uop_822 = relay.sinh(var_821.astype('float32')) # shape=(5, 4, 10)
output = relay.Tuple([uop_822,])
output2 = relay.Tuple([uop_822,])
func_843 = relay.Function([var_821,], output)
mod['func_843'] = func_843
mod = relay.transform.InferType()(mod)
mutated_mod['func_843'] = func_843
mutated_mod = relay.transform.InferType()(mutated_mod)
var_844 = relay.var("var_844", dtype = "float32", shape = (5, 4, 10))#candidate|844|(5, 4, 10)|var|float32
func_843_call = mutated_mod.get_global_var('func_843')
call_845 = func_843_call(var_844)
output = call_845
func_846 = relay.Function([var_844], output)
mutated_mod['func_846'] = func_846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_682_call = mutated_mod.get_global_var('func_682')
call_873 = relay.TupleGetItem(func_681_call(), 0)
call_874 = relay.TupleGetItem(func_682_call(), 0)
output = relay.Tuple([call_873,])
output2 = relay.Tuple([call_874,])
func_919 = relay.Function([], output)
mod['func_919'] = func_919
mod = relay.transform.InferType()(mod)
output = func_919()
func_920 = relay.Function([], output)
mutated_mod['func_920'] = func_920
mutated_mod = relay.transform.InferType()(mutated_mod)
var_951 = relay.var("var_951", dtype = "float64", shape = (11, 7, 1))#candidate|951|(11, 7, 1)|var|float64
const_952 = relay.const([[[3.781248,-4.847915,9.813856,2.313801,-9.407553,6.777515,2.645312,3.314197],[-5.058686,-3.575573,-3.880815,9.051357,-9.202225,-5.026839,-9.633020,-5.352646],[3.749209,-0.485413,-1.978124,2.852337,9.219321,3.941978,9.232522,4.171454],[-9.776263,-3.475811,7.582416,1.015287,3.423004,-1.773490,2.909074,2.258304],[-8.203795,0.760980,7.250288,4.945640,4.610561,8.364768,-9.013220,-2.490919],[-7.124636,4.215100,8.021611,8.886242,-4.786655,-4.630676,1.152437,7.909580],[7.201357,-6.871773,6.860142,0.099439,2.948517,-3.017834,1.051460,-7.980046]],[[6.101258,1.947257,-3.672246,5.258093,3.208717,-8.238391,3.474536,-7.278555],[-6.477279,8.002090,-6.267871,-7.448041,-1.443672,2.882116,-7.939807,7.525913],[9.186422,-1.259290,-4.922488,5.644004,0.038584,-9.228965,0.377827,1.355503],[9.593392,9.983937,-6.884283,9.331074,-0.922484,-8.888408,6.994186,-8.901021],[2.088558,-1.904703,-2.095019,3.730792,-9.945999,-1.851530,-5.725985,4.839370],[3.111837,3.172470,0.885176,-2.320704,-5.309615,-7.363869,-1.516075,-9.007505],[4.746087,1.856182,-6.995280,4.538189,-6.229043,-1.048712,8.374484,9.474123]],[[1.465178,-3.762501,8.928640,-4.004446,-7.999913,5.435400,-9.447805,-0.524835],[6.233038,2.055264,-6.401544,-4.388149,3.410935,3.835864,-0.776968,1.629354],[5.362633,-7.186238,-4.123101,-6.424144,7.443649,2.309526,-5.145987,6.076473],[-1.574271,6.788103,9.459111,6.184612,8.579037,-6.974079,0.568614,6.443615],[1.255241,-2.820109,-1.454042,-9.676865,-6.492247,3.666242,8.432505,-9.082833],[-4.293689,-2.209070,5.521093,-1.007919,-8.564501,2.756506,-1.209447,5.791023],[-1.674346,1.008732,-8.253860,1.572838,7.092464,3.046870,9.184043,-7.411224]],[[-9.722423,-2.425425,2.798365,-8.861260,7.056203,3.072791,-0.915873,3.563953],[-4.305628,3.806619,3.826812,-9.487221,-9.614690,7.118250,9.966672,7.278404],[4.476068,-2.398255,-4.806899,-8.249977,-7.102792,8.933251,-4.746025,6.835881],[9.690944,-9.363008,1.576380,4.694472,-3.092929,-6.661768,1.309940,8.425038],[2.767251,9.029776,-8.574999,7.999536,8.190497,6.314235,4.798189,6.349773],[-7.898875,2.589475,-6.522746,7.090343,-2.053250,-4.333422,9.860288,-0.647520],[9.942415,-6.444568,9.548813,-5.846759,-8.814500,2.818607,5.170811,-1.391560]],[[-9.222196,9.899777,-4.775873,4.558264,-1.682707,-2.899545,-7.853102,-2.420579],[-3.490255,2.229439,-4.736150,3.672799,-5.462702,8.964659,6.545323,7.068169],[4.556399,-4.604680,1.401159,-9.866423,5.982107,6.100949,8.210615,-7.948086],[-8.975730,-1.021798,9.630370,1.050722,-8.510918,4.078461,-4.861516,9.657728],[-3.665556,2.315067,2.031744,6.035652,7.489959,-4.995184,5.974985,-6.950563],[7.576825,-0.048442,-5.683374,-3.584076,-8.910769,-5.487385,-0.864997,8.610921],[2.725664,-5.558314,-1.797248,-7.644664,-5.405260,8.657268,7.624984,1.458990]],[[-3.271920,6.833732,2.406586,5.964359,-3.493641,-3.111435,5.190945,2.819521],[-2.149405,7.829296,4.507059,-1.906064,6.824464,2.750392,-4.506589,6.322690],[6.785154,9.188211,-9.578985,-5.638878,2.092915,7.145818,-9.271685,2.895642],[-7.615154,-6.817448,-3.958471,6.187016,-3.685357,-5.326011,5.663765,2.809361],[5.831478,3.929920,3.815008,-0.005187,-1.224236,7.537077,-4.939333,0.980210],[8.056496,-9.165193,9.012332,3.363821,4.322274,-2.868741,3.103880,1.825232],[-2.657489,-7.802550,-0.319787,-5.414292,-0.469538,-6.097683,0.270468,7.961314]],[[6.282143,-8.707148,1.006465,-9.870538,-7.151760,9.118236,-7.490103,-8.742408],[2.716221,-8.107394,3.419196,-9.858093,-2.970603,-0.370419,0.344442,-0.136667],[1.488051,8.414647,6.299226,1.793918,-9.285953,4.331834,2.724374,1.204426],[6.643210,3.563506,2.388120,-9.034776,-9.414831,7.002964,0.593396,-3.211837],[-1.801592,2.896664,9.269871,5.277901,-3.878649,-1.356137,-5.860376,-2.673794],[8.886707,-0.500891,-9.612510,-2.444843,4.102735,-2.294375,3.960414,-4.889077],[-6.082100,2.250495,-2.291014,0.364305,-7.423343,9.271216,2.431408,-0.130440]],[[1.825527,9.937204,2.209995,-6.131949,2.413387,8.741955,4.773757,6.080914],[-9.078700,1.059840,2.101088,3.222553,-3.558603,4.726208,-1.738792,-1.247711],[-9.024593,1.724928,6.155292,7.322059,-2.271268,0.606450,-0.979459,2.658283],[-5.064989,2.602336,1.745748,8.095643,1.868333,-6.413752,-5.159462,9.118089],[-7.229700,-9.749471,-2.432753,1.117565,3.757086,-8.865875,7.592111,-2.394979],[-1.438917,8.019758,-8.434571,7.883380,7.937492,1.128542,-8.392818,4.266223],[-3.041363,-0.163067,9.709241,5.833138,8.772962,-4.951081,-2.952973,-5.774977]],[[-4.341821,-3.843960,-5.104675,0.488408,7.036700,8.687254,4.348390,6.935770],[-1.928732,4.326140,3.238404,-6.808671,-7.463326,5.720250,1.091088,-5.603527],[9.837428,-3.558776,-3.714123,-4.738086,9.411584,-8.976290,-7.326293,-5.212002],[3.441622,-3.678091,-4.127276,9.735095,4.247340,0.383363,-1.054002,-2.239358],[1.557894,8.951066,-6.046496,9.688016,0.302970,9.455128,7.994459,3.513959],[3.331307,4.085608,-3.258795,-4.044258,3.137130,1.386354,6.167443,-9.388513],[-8.763608,4.305366,2.417898,-6.495239,-7.318328,-4.696559,5.895294,-0.687976]],[[2.328061,3.185081,4.487852,6.565738,7.667288,-6.151511,-5.985266,3.223127],[5.831738,-0.408933,-8.904908,1.116040,-2.392875,-7.675986,4.654354,-4.268818],[1.259061,3.400296,6.104070,5.599713,1.702406,-6.987117,-1.707544,-9.109693],[-2.207720,-3.299706,-2.887764,8.573405,4.979112,-0.645369,-4.126445,4.726220],[-9.558001,-4.519015,5.706957,8.329383,-7.362889,2.827648,0.129943,-3.918639],[-5.705777,-0.149972,-1.134152,7.759432,-6.409289,7.041843,-7.506064,-3.699911],[1.152520,-6.512459,-2.966033,1.316554,6.900494,-0.839730,-7.156659,-6.823282]],[[2.745607,3.631340,-6.273658,-0.781524,2.154743,-6.489238,-5.035741,-6.741019],[1.100016,7.077517,-2.684864,-9.576063,3.391929,1.298775,8.886201,-9.753388],[-8.027668,8.415639,-3.781674,0.690492,1.736201,2.269549,-4.263419,1.346292],[-8.300225,-7.664528,7.502744,4.754073,2.022885,-2.367072,-7.525286,4.368666],[5.240381,-1.696004,-8.817307,2.504263,2.953925,-6.877748,-3.199946,3.373566],[-7.981067,-6.577121,3.236945,-0.452270,-0.076714,8.477875,8.221972,3.521626],[3.334530,-9.249183,-3.071519,1.795274,-0.775712,3.182414,3.661152,1.961550]]], dtype = "float64")#candidate|952|(11, 7, 8)|const|float64
bop_953 = relay.divide(var_951.astype('float64'), const_952.astype('float64')) # shape=(11, 7, 8)
output = bop_953
output2 = bop_953
func_956 = relay.Function([var_951,], output)
mod['func_956'] = func_956
mod = relay.transform.InferType()(mod)
var_957 = relay.var("var_957", dtype = "float64", shape = (11, 7, 1))#candidate|957|(11, 7, 1)|var|float64
output = func_956(var_957)
func_958 = relay.Function([var_957], output)
mutated_mod['func_958'] = func_958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_963 = func_500_call()
call_964 = func_500_call()
output = relay.Tuple([call_963,])
output2 = relay.Tuple([call_964,])
func_965 = relay.Function([], output)
mod['func_965'] = func_965
mod = relay.transform.InferType()(mod)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mutated_mod.get_global_var('func_965')
call_966 = func_965_call()
output = call_966
func_967 = relay.Function([], output)
mutated_mod['func_967'] = func_967
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1032 = relay.var("var_1032", dtype = "float32", shape = (13, 5))#candidate|1032|(13, 5)|var|float32
uop_1033 = relay.tan(var_1032.astype('float32')) # shape=(13, 5)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_1040 = func_500_call()
call_1041 = func_500_call()
uop_1043 = relay.asinh(call_1040.astype('float32')) # shape=(7, 5, 14)
uop_1045 = relay.asinh(call_1041.astype('float32')) # shape=(7, 5, 14)
output = relay.Tuple([uop_1033,uop_1043,])
output2 = relay.Tuple([uop_1033,uop_1045,])
func_1047 = relay.Function([var_1032,], output)
mod['func_1047'] = func_1047
mod = relay.transform.InferType()(mod)
var_1048 = relay.var("var_1048", dtype = "float32", shape = (13, 5))#candidate|1048|(13, 5)|var|float32
output = func_1047(var_1048)
func_1049 = relay.Function([var_1048], output)
mutated_mod['func_1049'] = func_1049
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1083 = relay.var("var_1083", dtype = "uint64", shape = (7, 11, 2))#candidate|1083|(7, 11, 2)|var|uint64
const_1084 = relay.const([[[2,1],[-4,3],[6,3],[-2,-8],[7,4],[-2,2],[-9,10],[-9,-4],[-6,-5],[5,-6],[-9,-2]],[[-10,-3],[-8,-10],[-3,2],[3,2],[6,-2],[-2,-1],[-4,-7],[-8,3],[-3,4],[-5,-6],[7,10]],[[10,3],[-9,-6],[-4,9],[6,3],[9,3],[-4,5],[-9,8],[9,-7],[2,-2],[-9,-4],[-7,-2]],[[-9,10],[-1,-1],[-8,-4],[7,5],[2,4],[-6,-8],[7,7],[-5,9],[-4,-3],[2,9],[10,8]],[[-7,-3],[9,-6],[-4,-9],[6,-6],[-4,6],[-6,4],[3,-9],[-9,10],[2,-7],[-1,-3],[5,5]],[[-9,-2],[-10,3],[-7,3],[2,-3],[-8,7],[6,-10],[-6,1],[6,-5],[-1,-8],[-7,-4],[-7,6]],[[-10,10],[-4,8],[10,-9],[1,-10],[-8,-2],[1,-9],[-10,-5],[-1,-6],[-10,10],[3,3],[6,-10]]], dtype = "uint64")#candidate|1084|(7, 11, 2)|const|uint64
bop_1085 = relay.bitwise_or(var_1083.astype('uint64'), relay.reshape(const_1084.astype('uint64'), relay.shape_of(var_1083))) # shape=(7, 11, 2)
bop_1095 = relay.subtract(bop_1085.astype('uint64'), relay.reshape(const_1084.astype('uint64'), relay.shape_of(bop_1085))) # shape=(7, 11, 2)
uop_1104 = relay.asinh(bop_1085.astype('float64')) # shape=(7, 11, 2)
func_340_call = mod.get_global_var('func_340')
func_343_call = mutated_mod.get_global_var('func_343')
const_1111 = relay.const([[8,8,5,4,-6,6,7,-2,-3,8,-1,4,8,6,9,-7,-8,-9,-4,8,7,-8,4,-3,-8,9,-7,1,-10,7,2,10,-8,2,-3,-4,4,7,9,7,10,9,2,-3,4,4,6,8,3,6,2,-8,-1,6,-6,-9,10,-4,-5,-5,-6,7,-2,-6,8,-3,-3,9,-8,5,-10,10,10,2,-10,-8,-7,8,1,6,-9,10,-4,5,-3,-5,5,-3,-9,4,-2,-6,7,-10,-10,-8,9,-1,8,-4,8,-4,-7,10,3,-5,-4,6,7,-2,4,5,9,-6,-4,9,-2,-5,-1,-4,6,-9,-10,-4,1,-5,-7,10,-8,4,-1,-4,-6,-1,-3,-9,-4,-1,-3,3,-2,-1,-1,-4,9,1,-1,-2,-3,3,-8,4,1,6,2,-10,-2,-3,3,-1,5,4,-8,-2,9,-8,-6,-9,-10,2,8,6,4,10,7,10,5,8,2,6,-3,-8,-9,-9,4,10,-5,10,8,-7,-3,-6,2,-2,4,-6,2,-10,-1,-9,10,6,10,5,6,-2,10,7,-4,8]], dtype = "uint32")#candidate|1111|(1, 210)|const|uint32
call_1110 = relay.TupleGetItem(func_340_call(relay.reshape(const_1111.astype('uint32'), [210,])), 1)
call_1112 = relay.TupleGetItem(func_343_call(relay.reshape(const_1111.astype('uint32'), [210,])), 1)
output = relay.Tuple([bop_1095,uop_1104,call_1110,const_1111,])
output2 = relay.Tuple([bop_1095,uop_1104,call_1112,const_1111,])
func_1115 = relay.Function([var_1083,], output)
mod['func_1115'] = func_1115
mod = relay.transform.InferType()(mod)
var_1116 = relay.var("var_1116", dtype = "uint64", shape = (7, 11, 2))#candidate|1116|(7, 11, 2)|var|uint64
output = func_1115(var_1116)
func_1117 = relay.Function([var_1116], output)
mutated_mod['func_1117'] = func_1117
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1149 = relay.const([[[9.663475,-4.164251,-2.727290,-5.790181,7.562770,-3.961555,-3.602947,-5.426364,-0.044476,-1.309794]],[[-2.185642,-9.454663,-0.458391,2.202367,1.797119,5.709548,6.371002,-4.081486,9.718494,-8.297606]],[[-8.944641,-3.616349,1.178853,3.141669,-4.171174,-5.463628,-4.829507,3.451218,-9.252625,4.750563]],[[8.420593,-4.188851,3.307777,-4.498378,-9.920402,3.232080,6.799633,7.125156,-3.900055,-5.535823]],[[-3.956391,4.048511,-8.921013,-2.856336,-6.436212,-6.036318,-0.824353,-8.831303,-4.845771,-2.455213]],[[-9.623808,0.523661,4.364800,-7.427644,9.865875,6.619439,2.349945,-1.835896,8.971627,8.153693]],[[-7.661378,2.146446,-6.012602,-7.351851,-2.896432,0.529008,7.818859,1.727171,-5.415370,-8.525061]],[[-6.746139,3.668181,1.602430,6.797293,-5.287709,-3.857636,3.810942,-6.184969,4.676456,-3.863999]],[[2.918358,-0.534760,-2.632955,-0.431059,0.258128,-5.023298,-5.289173,-1.114189,3.396211,-1.838204]],[[-6.895728,-7.400374,-0.455453,8.794426,-9.555677,9.596298,-0.260533,-5.271744,5.186412,1.814928]],[[1.928316,1.903283,3.888850,7.529384,1.416541,3.117447,-8.257321,7.126162,-0.415352,6.834669]],[[-0.163361,-7.352951,-9.425141,3.999190,9.891719,3.522256,-6.837519,-4.837100,-5.955031,-9.447473]],[[1.293838,4.521692,-0.669566,-8.058763,8.277166,2.283215,2.141236,-2.186498,-7.641067,8.597693]],[[-6.696608,-1.074839,9.377483,3.935446,0.805382,-3.438113,9.062125,-5.573691,-8.485878,-3.538430]],[[-2.041181,-2.859787,5.621676,-0.610685,-7.711577,-3.094451,-6.892199,-4.469602,0.632908,1.198056]]], dtype = "float32")#candidate|1149|(15, 1, 10)|const|float32
uop_1150 = relay.erf(const_1149.astype('float32')) # shape=(15, 1, 10)
func_664_call = mod.get_global_var('func_664')
func_667_call = mutated_mod.get_global_var('func_667')
const_1159 = relay.const([[2,-4],[-5,-10],[-4,10],[-8,-5],[8,1],[4,-6],[10,3],[-1,4],[4,2],[9,-6],[3,-4],[-7,-9],[5,-3],[-1,-6],[-4,10],[5,7],[-2,-9],[-10,-3],[-3,6],[-8,-6],[-5,1],[-7,9],[-5,-7],[3,-2],[-4,5],[7,5],[-4,9],[5,4],[6,8],[-2,7],[5,10],[9,-4],[-2,-4],[-4,-9],[1,-10],[-5,6],[10,9],[10,9],[-1,5],[10,2],[6,-1],[7,1],[-7,-4],[-7,-8],[-4,-1],[2,-8],[-9,-2],[2,-1],[1,1],[1,6],[6,2],[2,-2],[-6,9],[-3,10],[1,2],[-5,-2],[-4,-4],[6,3],[-2,5],[7,-10],[-10,-9],[-5,-6],[-1,8],[1,2],[-2,2],[-8,7],[-2,-4],[10,1],[3,3],[-9,4],[9,-7],[3,-8],[8,4],[7,-6],[6,7],[7,3],[8,-10],[7,10],[-8,-8],[8,8],[8,-4],[3,-5],[3,4],[9,-10],[5,7],[-1,-10],[6,2],[6,2],[3,-8],[-7,7],[4,-7],[-1,4],[-4,10],[8,8],[9,-7],[-1,-10],[6,-1],[10,2],[9,1],[-8,-6],[7,-10],[9,8],[10,-5],[-6,-5],[3,-5],[6,-1],[9,-5],[-8,-9],[-10,-8],[9,-6],[-3,1],[-6,-2],[-4,1],[6,-7],[5,-10],[-6,6],[10,-2],[1,-9],[9,-4],[6,-3],[4,-2],[-8,-5],[-4,4],[6,3],[-7,6],[-5,4],[4,-8],[-7,3],[-6,4],[-6,5],[-4,10],[-2,-7],[-8,-8],[-7,-8],[2,1],[8,1],[-9,-6],[-3,-6],[1,-8],[-9,-1],[-7,1],[-1,3],[4,3],[6,-3],[-10,-3],[-1,10],[5,6],[-3,2],[-8,-2],[-9,-4],[-8,4],[-4,2],[-6,-7],[-4,-1],[-4,-4],[8,9],[-6,-6],[-7,-9],[-1,1],[-9,-9],[8,4],[-2,-4],[5,-5],[3,-8],[-4,-5],[5,6],[-6,-1],[-1,-2],[4,-2],[2,-3],[3,8],[2,4],[-10,-9],[-4,1],[5,7],[-10,-5],[-4,1],[3,10],[3,-2],[6,3],[7,-9],[8,-5],[1,8],[-8,6],[-10,-7],[-2,-8],[7,-10],[-8,-6],[-6,7],[6,8],[3,-9],[-7,-2],[-1,-1],[-6,-7],[-1,-5],[-1,-3],[8,2],[4,-1],[4,-8],[4,-9],[9,-9],[-10,-9],[5,-7],[8,5],[4,10],[-5,-2],[3,-1],[10,-6],[-1,5],[3,-2],[9,-7],[1,-3],[-9,-2],[-5,5],[-4,7],[-10,4],[-9,-3],[-2,-3],[4,10],[-3,-2],[-7,9],[9,-2],[-4,-9],[-3,6],[-2,4],[-3,7],[-8,3],[-9,6],[-9,9],[-2,-3],[9,1],[-4,6],[5,4],[-9,-5],[9,10],[3,3],[2,-10],[-3,1],[2,8],[10,-6],[3,2],[10,-9],[-5,6],[-5,-10],[2,-3]], dtype = "uint64")#candidate|1159|(245, 2)|const|uint64
call_1158 = relay.TupleGetItem(func_664_call(relay.reshape(const_1159.astype('uint64'), [7, 5, 14])), 1)
call_1160 = relay.TupleGetItem(func_667_call(relay.reshape(const_1159.astype('uint64'), [7, 5, 14])), 1)
uop_1178 = relay.cos(uop_1150.astype('float32')) # shape=(15, 1, 10)
output = relay.Tuple([call_1158,const_1159,uop_1178,])
output2 = relay.Tuple([call_1160,const_1159,uop_1178,])
func_1193 = relay.Function([], output)
mod['func_1193'] = func_1193
mod = relay.transform.InferType()(mod)
mutated_mod['func_1193'] = func_1193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1193_call = mutated_mod.get_global_var('func_1193')
call_1194 = func_1193_call()
output = call_1194
func_1195 = relay.Function([], output)
mutated_mod['func_1195'] = func_1195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_1201 = func_685_call()
call_1202 = func_685_call()
output = relay.Tuple([call_1201,])
output2 = relay.Tuple([call_1202,])
func_1205 = relay.Function([], output)
mod['func_1205'] = func_1205
mod = relay.transform.InferType()(mod)
output = func_1205()
func_1206 = relay.Function([], output)
mutated_mod['func_1206'] = func_1206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1193_call = mod.get_global_var('func_1193')
func_1195_call = mutated_mod.get_global_var('func_1195')
call_1228 = relay.TupleGetItem(func_1193_call(), 2)
call_1229 = relay.TupleGetItem(func_1195_call(), 2)
func_1047_call = mod.get_global_var('func_1047')
func_1049_call = mutated_mod.get_global_var('func_1049')
var_1234 = relay.var("var_1234", dtype = "float32", shape = (65,))#candidate|1234|(65,)|var|float32
call_1233 = relay.TupleGetItem(func_1047_call(relay.reshape(var_1234.astype('float32'), [13, 5])), 1)
call_1235 = relay.TupleGetItem(func_1049_call(relay.reshape(var_1234.astype('float32'), [13, 5])), 1)
func_1115_call = mod.get_global_var('func_1115')
func_1117_call = mutated_mod.get_global_var('func_1117')
const_1258 = relay.const([5,-1,-6,9,-7,-9,5,-2,1,6,5,-3,-2,-5,2,-3,3,-7,10,-6,-2,9,-6,-4,-8,-5,8,-8,-2,7,8,10,-5,-10,-2,-3,5,2,10,-10,-8,-1,-2,-7,1,10,-6,-1,-7,8,-1,-4,3,-10,3,3,-3,-10,-5,-1,10,6,-10,-9,-7,-6,7,5,-9,-5,4,-4,4,2,-10,6,2,10,-8,-1,-5,3,1,2,-4,-2,6,-3,-1,-2,10,5,-1,-6,-1,3,-5,7,-8,-6,9,9,6,-8,1,-10,-9,2,9,8,-4,7,1,7,-5,10,-3,-9,-4,-5,-6,-5,1,4,5,9,5,3,10,-3,-3,8,5,4,-4,-4,4,-3,7,5,9,3,2,10,-6,-6,8,-4,1,2,-6,6,-6,-5], dtype = "uint64")#candidate|1258|(154,)|const|uint64
call_1257 = relay.TupleGetItem(func_1115_call(relay.reshape(const_1258.astype('uint64'), [7, 11, 2])), 3)
call_1259 = relay.TupleGetItem(func_1117_call(relay.reshape(const_1258.astype('uint64'), [7, 11, 2])), 3)
func_1193_call = mod.get_global_var('func_1193')
func_1195_call = mutated_mod.get_global_var('func_1195')
call_1278 = relay.TupleGetItem(func_1193_call(), 0)
call_1279 = relay.TupleGetItem(func_1195_call(), 0)
bop_1284 = relay.equal(call_1233.astype('bool'), relay.reshape(call_1278.astype('bool'), relay.shape_of(call_1233))) # shape=(7, 5, 14)
bop_1287 = relay.equal(call_1235.astype('bool'), relay.reshape(call_1279.astype('bool'), relay.shape_of(call_1235))) # shape=(7, 5, 14)
func_575_call = mod.get_global_var('func_575')
func_577_call = mutated_mod.get_global_var('func_577')
call_1293 = relay.TupleGetItem(func_575_call(), 0)
call_1294 = relay.TupleGetItem(func_577_call(), 0)
func_956_call = mod.get_global_var('func_956')
func_958_call = mutated_mod.get_global_var('func_958')
const_1300 = relay.const([-1.754192,7.409625,-4.266870,1.344060,-3.507779,0.762807,9.494032,-9.784905,2.434192,0.944826,2.450957,-8.998996,7.160210,1.636069,9.930428,-7.045662,0.846222,3.432805,7.378633,-8.794139,1.471148,2.860978,3.026297,9.140623,2.494107,4.105064,9.789838,-8.096144,3.119819,-6.453671,-3.580518,-2.610212,-8.438195,9.620448,-5.211121,9.685283,5.954706,7.476484,-8.667163,7.996090,2.207570,-1.182315,4.422631,3.778647,7.186056,3.915606,8.507168,3.769010,7.705695,3.032141,-7.743217,6.230514,5.102435,3.360568,7.485698,9.638077,1.138682,-6.902154,6.083663,4.763303,0.545100,-2.791852,7.517269,-6.493143,3.021917,-6.637781,-1.620496,6.550654,-7.181859,-9.925248,-8.459807,-4.427909,6.257598,-3.834349,7.913064,8.377488,-4.631819], dtype = "float64")#candidate|1300|(77,)|const|float64
call_1299 = func_956_call(relay.reshape(const_1300.astype('float64'), [11, 7, 1]))
call_1301 = func_956_call(relay.reshape(const_1300.astype('float64'), [11, 7, 1]))
output = relay.Tuple([call_1228,var_1234,call_1257,const_1258,bop_1284,call_1293,call_1299,const_1300,])
output2 = relay.Tuple([call_1229,var_1234,call_1259,const_1258,bop_1287,call_1294,call_1301,const_1300,])
func_1307 = relay.Function([var_1234,], output)
mod['func_1307'] = func_1307
mod = relay.transform.InferType()(mod)
var_1308 = relay.var("var_1308", dtype = "float32", shape = (65,))#candidate|1308|(65,)|var|float32
output = func_1307(var_1308)
func_1309 = relay.Function([var_1308], output)
mutated_mod['func_1309'] = func_1309
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1313 = relay.var("var_1313", dtype = "uint16", shape = ())#candidate|1313|()|var|uint16
var_1314 = relay.var("var_1314", dtype = "uint16", shape = (15, 6, 14))#candidate|1314|(15, 6, 14)|var|uint16
bop_1315 = relay.not_equal(var_1313.astype('bool'), var_1314.astype('bool')) # shape=(15, 6, 14)
func_340_call = mod.get_global_var('func_340')
func_343_call = mutated_mod.get_global_var('func_343')
const_1321 = relay.const([-10,1,-4,-2,-1,-6,7,-7,6,7,-7,2,-5,-5,7,-10,-1,-6,-6,-1,-7,8,-10,2,-2,10,5,9,2,-7,-10,-6,2,7,10,6,7,-3,1,-5,-4,2,8,1,7,-1,-7,-9,8,-6,6,-6,-8,-1,4,-3,10,10,-7,2,-9,3,9,-4,10,3,-5,-10,-8,3,-9,-10,2,-9,-9,6,-3,3,-3,-6,8,-10,10,6,-2,-8,5,-2,-8,-7,1,2,-4,-5,-3,-9,-10,-5,-10,-8,2,-3,-4,6,-5,8,8,-1,8,-7,-7,-3,7,7,3,-10,-3,-3,-10,-10,2,5,9,-10,2,-7,6,-7,-10,-2,2,-5,7,-2,7,-5,8,-8,-8,4,-10,10,-1,-10,-1,-1,6,-6,5,1,-9,-10,-8,6,9,-7,-10,-6,4,-9,8,-8,5,-7,-3,2,-9,-9,-3,5,4,2,1,-3,3,1,-2,-8,-6,-9,5,3,6,-1,8,10,1,5,7,8,4,3,-2,-4,6,-9,7,-5,3,-9,-5,2,10,-8,9,-8,5,8,-4,6], dtype = "uint32")#candidate|1321|(210,)|const|uint32
call_1320 = relay.TupleGetItem(func_340_call(relay.reshape(const_1321.astype('uint32'), [210,])), 1)
call_1322 = relay.TupleGetItem(func_343_call(relay.reshape(const_1321.astype('uint32'), [210,])), 1)
output = relay.Tuple([bop_1315,call_1320,const_1321,])
output2 = relay.Tuple([bop_1315,call_1322,const_1321,])
func_1327 = relay.Function([var_1313,var_1314,], output)
mod['func_1327'] = func_1327
mod = relay.transform.InferType()(mod)
var_1328 = relay.var("var_1328", dtype = "uint16", shape = ())#candidate|1328|()|var|uint16
var_1329 = relay.var("var_1329", dtype = "uint16", shape = (15, 6, 14))#candidate|1329|(15, 6, 14)|var|uint16
output = func_1327(var_1328,var_1329,)
func_1330 = relay.Function([var_1328,var_1329,], output)
mutated_mod['func_1330'] = func_1330
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1360 = relay.var("var_1360", dtype = "uint32", shape = ())#candidate|1360|()|var|uint32
const_1361 = relay.const([[[3],[-5],[-9],[5],[-10],[-3],[6]],[[1],[6],[5],[-1],[5],[-6],[10]],[[-8],[-1],[9],[10],[-8],[-3],[-7]],[[-1],[10],[4],[-1],[3],[-7],[-1]],[[9],[-5],[6],[-9],[-4],[3],[4]],[[-2],[-4],[6],[5],[2],[-1],[10]],[[-3],[9],[2],[-8],[3],[-5],[4]],[[9],[-6],[1],[-6],[-6],[4],[-6]],[[2],[3],[7],[-5],[7],[9],[-1]],[[-7],[2],[3],[8],[8],[10],[2]],[[-1],[-1],[6],[-8],[5],[4],[-7]],[[1],[9],[2],[-3],[9],[-10],[5]],[[10],[-4],[-8],[6],[6],[-9],[-7]],[[4],[-7],[-1],[5],[8],[-10],[-1]]], dtype = "uint32")#candidate|1361|(14, 7, 1)|const|uint32
bop_1362 = relay.less_equal(var_1360.astype('bool'), const_1361.astype('bool')) # shape=(14, 7, 1)
func_919_call = mod.get_global_var('func_919')
func_920_call = mutated_mod.get_global_var('func_920')
call_1367 = relay.TupleGetItem(func_919_call(), 0)
call_1368 = relay.TupleGetItem(func_920_call(), 0)
func_778_call = mod.get_global_var('func_778')
func_780_call = mutated_mod.get_global_var('func_780')
call_1373 = relay.TupleGetItem(func_778_call(relay.reshape(call_1367.astype('uint64'), [7, 5, 14])), 0)
call_1374 = relay.TupleGetItem(func_780_call(relay.reshape(call_1367.astype('uint64'), [7, 5, 14])), 0)
output = relay.Tuple([bop_1362,call_1367,call_1373,])
output2 = relay.Tuple([bop_1362,call_1368,call_1374,])
func_1398 = relay.Function([var_1360,], output)
mod['func_1398'] = func_1398
mod = relay.transform.InferType()(mod)
mutated_mod['func_1398'] = func_1398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1399 = relay.var("var_1399", dtype = "uint32", shape = ())#candidate|1399|()|var|uint32
func_1398_call = mutated_mod.get_global_var('func_1398')
call_1400 = func_1398_call(var_1399)
output = call_1400
func_1401 = relay.Function([var_1399], output)
mutated_mod['func_1401'] = func_1401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_1438 = func_685_call()
call_1439 = func_685_call()
uop_1442 = relay.cosh(call_1438.astype('float32')) # shape=(7, 5, 14)
uop_1444 = relay.cosh(call_1439.astype('float32')) # shape=(7, 5, 14)
func_279_call = mod.get_global_var('func_279')
func_283_call = mutated_mod.get_global_var('func_283')
var_1450 = relay.var("var_1450", dtype = "float64", shape = (165,))#candidate|1450|(165,)|var|float64
var_1451 = relay.var("var_1451", dtype = "uint32", shape = (105, 2))#candidate|1451|(105, 2)|var|uint32
call_1449 = relay.TupleGetItem(func_279_call(relay.reshape(var_1450.astype('float64'), [3, 5, 11]), relay.reshape(var_1451.astype('uint32'), [210,]), ), 1)
call_1452 = relay.TupleGetItem(func_283_call(relay.reshape(var_1450.astype('float64'), [3, 5, 11]), relay.reshape(var_1451.astype('uint32'), [210,]), ), 1)
var_1454 = relay.var("var_1454", dtype = "float64", shape = (165,))#candidate|1454|(165,)|var|float64
bop_1455 = relay.logical_and(var_1450.astype('bool'), relay.reshape(var_1454.astype('bool'), relay.shape_of(var_1450))) # shape=(165,)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_1466 = func_194_call()
call_1467 = func_194_call()
var_1468 = relay.var("var_1468", dtype = "float32", shape = (7, 5, 14))#candidate|1468|(7, 5, 14)|var|float32
bop_1469 = relay.minimum(uop_1442.astype('uint16'), relay.reshape(var_1468.astype('uint16'), relay.shape_of(uop_1442))) # shape=(7, 5, 14)
bop_1472 = relay.minimum(uop_1444.astype('uint16'), relay.reshape(var_1468.astype('uint16'), relay.shape_of(uop_1444))) # shape=(7, 5, 14)
func_681_call = mod.get_global_var('func_681')
func_682_call = mutated_mod.get_global_var('func_682')
call_1478 = relay.TupleGetItem(func_681_call(), 0)
call_1479 = relay.TupleGetItem(func_682_call(), 0)
uop_1480 = relay.log(var_1468.astype('float32')) # shape=(7, 5, 14)
func_1047_call = mod.get_global_var('func_1047')
func_1049_call = mutated_mod.get_global_var('func_1049')
const_1483 = relay.const([3.017426,-2.233767,6.212214,-4.068077,1.791878,-3.132226,5.496029,0.512709,2.248668,-5.286196,0.726725,3.743419,4.737177,-0.995627,-3.908760,8.263032,1.910392,-3.380321,8.688841,-8.705300,-4.105417,-6.329359,-3.087676,-5.551178,6.436374,-5.554570,-9.197469,-0.577304,-5.640120,9.178088,-7.444250,-7.277497,-1.489787,-5.059997,8.582385,3.741940,-3.359022,1.354105,7.516737,-2.405113,-9.171966,-6.406924,-5.620446,-8.898789,8.406712,8.611223,9.672245,5.125470,1.629427,1.195801,-7.275358,-3.087649,-7.435419,7.732542,8.331028,-6.637675,-5.535119,2.646983,-4.884031,3.597546,8.961782,1.874731,-1.458658,-1.539711,9.090165], dtype = "float32")#candidate|1483|(65,)|const|float32
call_1482 = relay.TupleGetItem(func_1047_call(relay.reshape(const_1483.astype('float32'), [13, 5])), 0)
call_1484 = relay.TupleGetItem(func_1049_call(relay.reshape(const_1483.astype('float32'), [13, 5])), 0)
output = relay.Tuple([call_1449,var_1451,bop_1455,call_1466,bop_1469,call_1478,uop_1480,call_1482,const_1483,])
output2 = relay.Tuple([call_1452,var_1451,bop_1455,call_1467,bop_1472,call_1479,uop_1480,call_1484,const_1483,])
func_1494 = relay.Function([var_1450,var_1451,var_1454,var_1468,], output)
mod['func_1494'] = func_1494
mod = relay.transform.InferType()(mod)
mutated_mod['func_1494'] = func_1494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1494_call = mutated_mod.get_global_var('func_1494')
var_1496 = relay.var("var_1496", dtype = "float64", shape = (165,))#candidate|1496|(165,)|var|float64
var_1497 = relay.var("var_1497", dtype = "uint32", shape = (105, 2))#candidate|1497|(105, 2)|var|uint32
var_1498 = relay.var("var_1498", dtype = "float64", shape = (165,))#candidate|1498|(165,)|var|float64
var_1499 = relay.var("var_1499", dtype = "float32", shape = (7, 5, 14))#candidate|1499|(7, 5, 14)|var|float32
call_1495 = func_1494_call(var_1496,var_1497,var_1498,var_1499,)
output = call_1495
func_1500 = relay.Function([var_1496,var_1497,var_1498,var_1499,], output)
mutated_mod['func_1500'] = func_1500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1193_call = mod.get_global_var('func_1193')
func_1195_call = mutated_mod.get_global_var('func_1195')
call_1520 = relay.TupleGetItem(func_1193_call(), 2)
call_1521 = relay.TupleGetItem(func_1195_call(), 2)
output = relay.Tuple([call_1520,])
output2 = relay.Tuple([call_1521,])
func_1523 = relay.Function([], output)
mod['func_1523'] = func_1523
mod = relay.transform.InferType()(mod)
output = func_1523()
func_1524 = relay.Function([], output)
mutated_mod['func_1524'] = func_1524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_1566 = func_500_call()
call_1567 = func_500_call()
output = relay.Tuple([call_1566,])
output2 = relay.Tuple([call_1567,])
func_1571 = relay.Function([], output)
mod['func_1571'] = func_1571
mod = relay.transform.InferType()(mod)
output = func_1571()
func_1572 = relay.Function([], output)
mutated_mod['func_1572'] = func_1572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_577_call = mutated_mod.get_global_var('func_577')
call_1702 = relay.TupleGetItem(func_575_call(), 2)
call_1703 = relay.TupleGetItem(func_577_call(), 2)
output = call_1702
output2 = call_1703
func_1711 = relay.Function([], output)
mod['func_1711'] = func_1711
mod = relay.transform.InferType()(mod)
output = func_1711()
func_1712 = relay.Function([], output)
mutated_mod['func_1712'] = func_1712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_1817 = func_685_call()
call_1818 = func_685_call()
output = relay.Tuple([call_1817,])
output2 = relay.Tuple([call_1818,])
func_1820 = relay.Function([], output)
mod['func_1820'] = func_1820
mod = relay.transform.InferType()(mod)
mutated_mod['func_1820'] = func_1820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1820_call = mutated_mod.get_global_var('func_1820')
call_1821 = func_1820_call()
output = call_1821
func_1822 = relay.Function([], output)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1851 = relay.var("var_1851", dtype = "float32", shape = (1, 12, 5))#candidate|1851|(1, 12, 5)|var|float32
var_1852 = relay.var("var_1852", dtype = "float32", shape = (12, 12, 5))#candidate|1852|(12, 12, 5)|var|float32
bop_1853 = relay.power(var_1851.astype('float32'), var_1852.astype('float32')) # shape=(12, 12, 5)
bop_1858 = relay.logical_or(var_1851.astype('bool'), var_1852.astype('bool')) # shape=(12, 12, 5)
output = relay.Tuple([bop_1853,bop_1858,])
output2 = relay.Tuple([bop_1853,bop_1858,])
func_1878 = relay.Function([var_1851,var_1852,], output)
mod['func_1878'] = func_1878
mod = relay.transform.InferType()(mod)
mutated_mod['func_1878'] = func_1878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1878_call = mutated_mod.get_global_var('func_1878')
var_1880 = relay.var("var_1880", dtype = "float32", shape = (1, 12, 5))#candidate|1880|(1, 12, 5)|var|float32
var_1881 = relay.var("var_1881", dtype = "float32", shape = (12, 12, 5))#candidate|1881|(12, 12, 5)|var|float32
call_1879 = func_1878_call(var_1880,var_1881,)
output = call_1879
func_1882 = relay.Function([var_1880,var_1881,], output)
mutated_mod['func_1882'] = func_1882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_1887 = relay.TupleGetItem(func_1205_call(), 0)
call_1888 = relay.TupleGetItem(func_1206_call(), 0)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_1891 = func_500_call()
call_1892 = func_500_call()
func_279_call = mod.get_global_var('func_279')
func_283_call = mutated_mod.get_global_var('func_283')
var_1894 = relay.var("var_1894", dtype = "float64", shape = (165,))#candidate|1894|(165,)|var|float64
var_1895 = relay.var("var_1895", dtype = "uint32", shape = (210,))#candidate|1895|(210,)|var|uint32
call_1893 = relay.TupleGetItem(func_279_call(relay.reshape(var_1894.astype('float64'), [3, 5, 11]), relay.reshape(var_1895.astype('uint32'), [210,]), ), 1)
call_1896 = relay.TupleGetItem(func_283_call(relay.reshape(var_1894.astype('float64'), [3, 5, 11]), relay.reshape(var_1895.astype('uint32'), [210,]), ), 1)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_1897 = relay.TupleGetItem(func_965_call(), 0)
call_1898 = relay.TupleGetItem(func_967_call(), 0)
uop_1950 = relay.log2(var_1894.astype('float64')) # shape=(165,)
output = relay.Tuple([call_1887,call_1891,call_1893,var_1895,call_1897,uop_1950,])
output2 = relay.Tuple([call_1888,call_1892,call_1896,var_1895,call_1898,uop_1950,])
func_1952 = relay.Function([var_1894,var_1895,], output)
mod['func_1952'] = func_1952
mod = relay.transform.InferType()(mod)
mutated_mod['func_1952'] = func_1952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1952_call = mutated_mod.get_global_var('func_1952')
var_1954 = relay.var("var_1954", dtype = "float64", shape = (165,))#candidate|1954|(165,)|var|float64
var_1955 = relay.var("var_1955", dtype = "uint32", shape = (210,))#candidate|1955|(210,)|var|uint32
call_1953 = func_1952_call(var_1954,var_1955,)
output = call_1953
func_1956 = relay.Function([var_1954,var_1955,], output)
mutated_mod['func_1956'] = func_1956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1572_call = mutated_mod.get_global_var('func_1572')
call_1990 = relay.TupleGetItem(func_1571_call(), 0)
call_1991 = relay.TupleGetItem(func_1572_call(), 0)
output = relay.Tuple([call_1990,])
output2 = relay.Tuple([call_1991,])
func_1994 = relay.Function([], output)
mod['func_1994'] = func_1994
mod = relay.transform.InferType()(mod)
mutated_mod['func_1994'] = func_1994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1994_call = mutated_mod.get_global_var('func_1994')
call_1995 = func_1994_call()
output = call_1995
func_1996 = relay.Function([], output)
mutated_mod['func_1996'] = func_1996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_2011 = relay.TupleGetItem(func_1820_call(), 0)
call_2012 = relay.TupleGetItem(func_1822_call(), 0)
func_843_call = mod.get_global_var('func_843')
func_846_call = mutated_mod.get_global_var('func_846')
var_2018 = relay.var("var_2018", dtype = "float32", shape = (200, 1))#candidate|2018|(200, 1)|var|float32
call_2017 = relay.TupleGetItem(func_843_call(relay.reshape(var_2018.astype('float32'), [5, 4, 10])), 0)
call_2019 = relay.TupleGetItem(func_846_call(relay.reshape(var_2018.astype('float32'), [5, 4, 10])), 0)
output = relay.Tuple([call_2011,call_2017,var_2018,])
output2 = relay.Tuple([call_2012,call_2019,var_2018,])
func_2020 = relay.Function([var_2018,], output)
mod['func_2020'] = func_2020
mod = relay.transform.InferType()(mod)
mutated_mod['func_2020'] = func_2020
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2021 = relay.var("var_2021", dtype = "float32", shape = (200, 1))#candidate|2021|(200, 1)|var|float32
func_2020_call = mutated_mod.get_global_var('func_2020')
call_2022 = func_2020_call(var_2021)
output = call_2022
func_2023 = relay.Function([var_2021], output)
mutated_mod['func_2023'] = func_2023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2040 = relay.var("var_2040", dtype = "int8", shape = (9, 8, 10))#candidate|2040|(9, 8, 10)|var|int8
var_2041 = relay.var("var_2041", dtype = "int8", shape = (9, 8, 10))#candidate|2041|(9, 8, 10)|var|int8
bop_2042 = relay.not_equal(var_2040.astype('bool'), relay.reshape(var_2041.astype('bool'), relay.shape_of(var_2040))) # shape=(9, 8, 10)
func_1523_call = mod.get_global_var('func_1523')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_2046 = relay.TupleGetItem(func_1523_call(), 0)
call_2047 = relay.TupleGetItem(func_1524_call(), 0)
output = relay.Tuple([bop_2042,call_2046,])
output2 = relay.Tuple([bop_2042,call_2047,])
func_2050 = relay.Function([var_2040,var_2041,], output)
mod['func_2050'] = func_2050
mod = relay.transform.InferType()(mod)
var_2051 = relay.var("var_2051", dtype = "int8", shape = (9, 8, 10))#candidate|2051|(9, 8, 10)|var|int8
var_2052 = relay.var("var_2052", dtype = "int8", shape = (9, 8, 10))#candidate|2052|(9, 8, 10)|var|int8
output = func_2050(var_2051,var_2052,)
func_2053 = relay.Function([var_2051,var_2052,], output)
mutated_mod['func_2053'] = func_2053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_2104 = func_500_call()
call_2105 = func_500_call()
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
var_2108 = relay.var("var_2108", dtype = "uint32", shape = (210,))#candidate|2108|(210,)|var|uint32
call_2107 = func_168_call(relay.reshape(var_2108.astype('uint32'), [6, 5, 7]))
call_2109 = func_168_call(relay.reshape(var_2108.astype('uint32'), [6, 5, 7]))
func_1327_call = mod.get_global_var('func_1327')
func_1330_call = mutated_mod.get_global_var('func_1330')
const_2116 = relay.const(7, dtype = "uint16")#candidate|2116|()|const|uint16
const_2117 = relay.const([[-8,8,-2,1,6,3,6,4,4,2,2,-6,-5,10,-10,-1,7,4,-10,3,6,-4,9,-6,1,-9,-9,-5,-5,-8,9,-5,-1,-8,-5,1,-10,-2,4,-4,-7,-5,9,1,-6,8,2,-2,4,6,-4,9,-1,-4,8,-9,2,-1,5,-6,-5,-6,8,10,1,-1,4,-10,-10,1,6,-5,3,1,10,-8,-4,1,-4,3,-8,2,-4,-8,-9,-6,-6,-5,-9,-8,-6,5,5,-1,7,-4,-10,-9,-1,3,-4,6,10,-3,-10,7,9,7,7,3,-3,3,5,2,-8,5,5,-4,-3,-3,7,-10,-3,-2,-4,-8,-4,-4,2,-5,4,2,3,4,4,8,9,-10,4,7],[-9,-9,-6,3,3,-6,-10,-4,-6,-9,-6,-2,5,-9,5,1,1,-6,4,-2,-9,-4,9,-2,-6,3,-7,7,6,5,2,-5,5,-7,-1,8,9,9,-9,1,3,5,1,-4,-8,8,4,-10,-3,9,-7,-5,8,4,-6,-1,1,9,-8,8,-1,-3,-10,-3,1,8,-9,-4,-7,-2,-3,2,-9,-5,5,2,-10,8,-9,2,2,-7,4,-8,8,-6,3,7,10,-10,7,-8,8,-8,8,6,-1,3,-4,6,10,-7,1,-8,7,-5,-1,-5,10,7,-3,-10,-8,2,5,-6,-2,-10,6,-4,-8,-7,-2,8,-6,-2,8,7,-4,-7,-9,-5,-3,-5,-3,-2,-10,9,-1,-3],[-2,8,-6,7,4,-10,5,5,10,-9,-1,-5,-9,-10,-3,-9,-10,6,-2,8,7,10,-3,1,4,-10,10,5,-10,-10,-10,10,6,5,-9,7,-3,7,1,-1,8,2,-7,-7,-2,1,-6,3,5,1,3,9,6,-3,-3,-3,-8,-1,2,1,3,-7,3,2,-7,3,2,5,-7,4,-5,-3,4,7,1,1,1,2,7,3,6,4,-9,5,-1,8,-8,8,-6,-9,4,1,-7,1,-7,-9,-2,3,6,-9,-7,-3,-1,-6,-6,4,-4,-5,-7,8,-1,-1,10,8,9,2,-6,10,4,4,2,9,-4,8,3,7,3,-10,-1,-10,6,8,-5,-1,6,-2,-5,4,-7,1],[8,-5,8,-5,-2,1,5,1,-8,10,8,-2,-4,2,-1,-1,-5,-10,-2,3,-8,-1,4,4,4,7,7,-5,-8,-2,2,-7,-2,9,2,7,6,6,1,5,-3,5,4,2,-7,-10,-10,5,4,5,5,9,-3,5,-2,-7,-3,-6,4,-8,4,9,2,7,7,-3,5,8,-4,10,-3,2,1,2,10,6,5,8,-1,-7,-7,3,-2,-10,3,-4,-10,2,-8,9,-2,2,2,9,4,-2,-6,-3,-5,7,-6,2,-9,9,7,-5,-3,-10,-6,-8,5,-1,4,-9,10,5,-7,2,-1,5,-9,1,-7,6,-2,-6,-4,-9,-3,-7,6,-1,-1,1,3,4,-4,3,7,-9],[-4,5,-1,6,5,-9,9,4,-4,-4,8,-9,4,-8,-1,-10,-9,3,-1,6,-6,7,-6,5,-7,-6,-8,1,-9,5,-3,7,1,-6,2,-10,-8,4,-9,3,-10,1,6,-2,-1,8,-3,8,6,-6,-7,-7,-3,-8,-9,-8,-1,-9,-1,3,9,7,-6,-5,10,-3,8,-1,-10,-5,1,-10,-2,-9,-1,6,6,1,10,-6,-9,-7,-8,10,-9,-7,-8,-3,7,3,8,5,5,-8,3,-5,-3,-1,-3,9,6,4,-4,-2,1,-8,-9,3,-10,-10,6,-7,-10,-2,-9,-8,-8,9,-9,2,8,-9,2,2,-4,6,8,9,-2,-4,9,-6,-4,10,5,1,3,-2,-3,-8],[9,-5,7,-6,4,-10,3,1,-10,-9,4,-10,-2,-1,-9,2,-2,4,2,10,1,10,-5,-9,1,-10,10,1,2,-8,2,8,8,5,3,7,-5,-10,-7,7,-9,-6,-7,-4,10,10,4,6,-4,-4,-6,3,-10,-4,-3,9,-8,-2,10,3,-8,2,5,-3,-8,-5,10,8,10,6,-4,7,10,8,5,-9,-8,-4,8,-9,-4,3,-2,-3,6,8,-6,4,4,5,-7,4,-7,6,6,2,-10,6,-7,-8,10,-2,1,-2,10,-8,-4,-2,-1,-6,4,8,2,-9,1,-9,1,9,9,-1,-3,-6,9,7,6,8,-1,7,-8,-2,2,-2,-5,9,6,-3,-6,5,-6,-9],[8,-4,4,4,-8,1,-10,-4,-7,8,-2,-2,9,8,-4,10,4,10,-7,-10,-3,-4,-7,7,-3,7,4,-6,9,-10,2,-4,6,-4,10,-6,4,-5,10,5,5,-9,-3,3,10,6,3,-8,-6,2,6,-9,7,1,4,-9,10,-9,4,5,-5,-7,3,-9,-8,6,-8,6,9,-3,5,-3,3,-8,-3,-2,-5,9,2,8,-1,-6,7,4,-9,-10,-2,-9,-4,1,-1,-8,-2,4,-6,-6,7,6,3,-2,1,-1,3,-8,-7,6,4,4,-10,-9,-3,5,-8,3,-3,8,-5,6,8,-8,-7,-5,-6,-8,-7,5,4,9,-1,5,-5,9,-1,1,3,4,-4,2,8,-8],[-6,7,5,4,-6,1,4,-5,-4,-6,-6,6,1,-9,7,6,-2,-5,-6,-4,-10,8,-4,-10,-9,-7,7,6,3,-7,-3,-6,-3,-4,10,5,-3,-5,-6,-9,-1,2,2,-8,-3,7,-5,3,-4,8,6,-5,8,10,-6,1,-5,-7,-2,4,-7,3,4,1,4,-1,5,-1,-5,-9,10,-8,4,2,10,1,-6,9,-10,-5,2,-7,3,1,1,-1,-9,-5,-6,-9,2,-4,-4,-6,3,-3,1,-3,-1,4,-4,2,4,8,-6,-6,1,-5,-1,1,6,3,5,-10,10,-8,-9,-10,10,2,-9,4,-8,-4,4,5,1,-5,-3,3,-9,8,3,-10,9,1,-10,-5,8,7],[7,1,-1,-6,-1,8,2,-9,-5,10,-1,-10,-7,-1,-6,-8,2,3,-6,-8,8,9,1,4,7,9,-6,2,8,10,-2,9,10,9,-10,2,-2,-7,1,10,7,7,-10,9,-2,2,-1,-10,-10,4,-4,10,-9,1,-10,9,10,-3,7,-8,4,3,-10,4,-1,-2,7,3,8,-8,-2,-8,-5,3,-4,10,-3,-5,7,-5,-10,-3,8,6,9,6,3,4,-4,9,-1,10,-2,-7,4,7,-8,2,-6,1,4,-7,-1,2,-1,7,-10,6,-10,2,2,10,10,5,2,-3,5,-1,2,-2,-8,5,-6,1,1,-1,-5,-4,-5,-2,6,5,-5,8,2,10,-8,8,-3,9]], dtype = "uint16")#candidate|2117|(9, 140)|const|uint16
call_2115 = relay.TupleGetItem(func_1327_call(relay.reshape(const_2116.astype('uint16'), []), relay.reshape(const_2117.astype('uint16'), [15, 6, 14]), ), 0)
call_2118 = relay.TupleGetItem(func_1330_call(relay.reshape(const_2116.astype('uint16'), []), relay.reshape(const_2117.astype('uint16'), [15, 6, 14]), ), 0)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_2121 = func_194_call()
call_2122 = func_194_call()
bop_2153 = relay.logical_xor(call_2115.astype('uint16'), const_2116.astype('uint16')) # shape=(15, 6, 14)
bop_2156 = relay.logical_xor(call_2118.astype('uint16'), const_2116.astype('uint16')) # shape=(15, 6, 14)
uop_2165 = relay.sinh(call_2107.astype('float32')) # shape=(6, 5, 7)
uop_2167 = relay.sinh(call_2109.astype('float32')) # shape=(6, 5, 7)
var_2168 = relay.var("var_2168", dtype = "float32", shape = (6, 5, 7))#candidate|2168|(6, 5, 7)|var|float32
bop_2169 = relay.greater_equal(uop_2165.astype('bool'), relay.reshape(var_2168.astype('bool'), relay.shape_of(uop_2165))) # shape=(6, 5, 7)
bop_2172 = relay.greater_equal(uop_2167.astype('bool'), relay.reshape(var_2168.astype('bool'), relay.shape_of(uop_2167))) # shape=(6, 5, 7)
output = relay.Tuple([call_2104,var_2108,const_2117,call_2121,bop_2153,bop_2169,])
output2 = relay.Tuple([call_2105,var_2108,const_2117,call_2122,bop_2156,bop_2172,])
func_2180 = relay.Function([var_2108,var_2168,], output)
mod['func_2180'] = func_2180
mod = relay.transform.InferType()(mod)
mutated_mod['func_2180'] = func_2180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2180_call = mutated_mod.get_global_var('func_2180')
var_2182 = relay.var("var_2182", dtype = "uint32", shape = (210,))#candidate|2182|(210,)|var|uint32
var_2183 = relay.var("var_2183", dtype = "float32", shape = (6, 5, 7))#candidate|2183|(6, 5, 7)|var|float32
call_2181 = func_2180_call(var_2182,var_2183,)
output = call_2181
func_2184 = relay.Function([var_2182,var_2183,], output)
mutated_mod['func_2184'] = func_2184
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2239 = relay.var("var_2239", dtype = "float32", shape = (3, 4, 2))#candidate|2239|(3, 4, 2)|var|float32
var_2240 = relay.var("var_2240", dtype = "float32", shape = (3, 4, 2))#candidate|2240|(3, 4, 2)|var|float32
bop_2241 = relay.divide(var_2239.astype('float32'), relay.reshape(var_2240.astype('float32'), relay.shape_of(var_2239))) # shape=(3, 4, 2)
output = relay.Tuple([bop_2241,])
output2 = relay.Tuple([bop_2241,])
func_2247 = relay.Function([var_2239,var_2240,], output)
mod['func_2247'] = func_2247
mod = relay.transform.InferType()(mod)
var_2248 = relay.var("var_2248", dtype = "float32", shape = (3, 4, 2))#candidate|2248|(3, 4, 2)|var|float32
var_2249 = relay.var("var_2249", dtype = "float32", shape = (3, 4, 2))#candidate|2249|(3, 4, 2)|var|float32
output = func_2247(var_2248,var_2249,)
func_2250 = relay.Function([var_2248,var_2249,], output)
mutated_mod['func_2250'] = func_2250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1572_call = mutated_mod.get_global_var('func_1572')
call_2289 = relay.TupleGetItem(func_1571_call(), 0)
call_2290 = relay.TupleGetItem(func_1572_call(), 0)
output = relay.Tuple([call_2289,])
output2 = relay.Tuple([call_2290,])
func_2317 = relay.Function([], output)
mod['func_2317'] = func_2317
mod = relay.transform.InferType()(mod)
output = func_2317()
func_2318 = relay.Function([], output)
mutated_mod['func_2318'] = func_2318
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2324 = relay.var("var_2324", dtype = "float32", shape = (12, 10, 7))#candidate|2324|(12, 10, 7)|var|float32
var_2325 = relay.var("var_2325", dtype = "float32", shape = (12, 10, 7))#candidate|2325|(12, 10, 7)|var|float32
bop_2326 = relay.divide(var_2324.astype('float32'), relay.reshape(var_2325.astype('float32'), relay.shape_of(var_2324))) # shape=(12, 10, 7)
func_956_call = mod.get_global_var('func_956')
func_958_call = mutated_mod.get_global_var('func_958')
const_2330 = relay.const([[-7.176523,7.301453,0.344013,-0.085573,5.344936,1.018148,-2.212065,0.847608,-1.339304,0.640446,8.388574,-1.251694,-2.867123,-6.033619,-4.606963,-1.275333,-4.856539,1.616031,6.479624,1.558711,-6.613535,-7.987269,6.737350,9.948806,-4.400332,-1.929592,9.129617,5.789840,-7.384302,-4.166783,7.777764,8.573393,-6.991568,6.802113,8.507842,-9.454117,-8.344980,-5.648936,-9.179249,8.738989,-1.390939,-0.087496,-2.683712,2.753676,7.186921,-0.580870,-1.522860,9.856309,-8.074400,-7.932063,8.681256,-4.511748,-9.911447,-6.020990,-8.589314,1.642593,1.186926,-1.915062,-4.604388,-5.784159,2.144393,-4.501067,9.554021,-4.176104,-2.463539,7.236571,5.606601,2.366950,-4.471436,-2.490596,1.594417,-8.859140,-2.200887,8.901155,-8.418938,-4.051302,-5.570909]], dtype = "float64")#candidate|2330|(1, 77)|const|float64
call_2329 = func_956_call(relay.reshape(const_2330.astype('float64'), [11, 7, 1]))
call_2331 = func_956_call(relay.reshape(const_2330.astype('float64'), [11, 7, 1]))
uop_2332 = relay.log2(const_2330.astype('float32')) # shape=(1, 77)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_2339 = relay.TupleGetItem(func_2317_call(), 0)
call_2340 = relay.TupleGetItem(func_2318_call(), 0)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_2355 = relay.TupleGetItem(func_1994_call(), 0)
call_2356 = relay.TupleGetItem(func_1996_call(), 0)
bop_2372 = relay.greater(uop_2332.astype('bool'), relay.reshape(const_2330.astype('bool'), relay.shape_of(uop_2332))) # shape=(1, 77)
bop_2381 = relay.right_shift(uop_2332.astype('int32'), relay.reshape(const_2330.astype('int32'), relay.shape_of(uop_2332))) # shape=(1, 77)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_2386 = relay.TupleGetItem(func_1994_call(), 0)
call_2387 = relay.TupleGetItem(func_1996_call(), 0)
output = relay.Tuple([bop_2326,call_2329,call_2339,call_2355,bop_2372,bop_2381,call_2386,])
output2 = relay.Tuple([bop_2326,call_2331,call_2340,call_2356,bop_2372,bop_2381,call_2387,])
func_2388 = relay.Function([var_2324,var_2325,], output)
mod['func_2388'] = func_2388
mod = relay.transform.InferType()(mod)
var_2389 = relay.var("var_2389", dtype = "float32", shape = (12, 10, 7))#candidate|2389|(12, 10, 7)|var|float32
var_2390 = relay.var("var_2390", dtype = "float32", shape = (12, 10, 7))#candidate|2390|(12, 10, 7)|var|float32
output = func_2388(var_2389,var_2390,)
func_2391 = relay.Function([var_2389,var_2390,], output)
mutated_mod['func_2391'] = func_2391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_2403 = func_685_call()
call_2404 = func_685_call()
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_2419 = relay.TupleGetItem(func_1994_call(), 0)
call_2420 = relay.TupleGetItem(func_1996_call(), 0)
func_1571_call = mod.get_global_var('func_1571')
func_1572_call = mutated_mod.get_global_var('func_1572')
call_2421 = relay.TupleGetItem(func_1571_call(), 0)
call_2422 = relay.TupleGetItem(func_1572_call(), 0)
func_1115_call = mod.get_global_var('func_1115')
func_1117_call = mutated_mod.get_global_var('func_1117')
const_2425 = relay.const([6,-3,8,2,10,-8,-1,-5,3,2,2,-9,-2,-8,-6,9,5,-7,-4,6,-2,6,-3,4,-4,2,-4,-4,5,9,-1,3,2,8,9,-9,8,-6,-10,-7,-9,-10,-9,-1,-8,-6,-9,-4,9,7,4,8,-5,3,7,10,8,-10,6,-1,-10,-5,4,-9,9,-10,4,-7,6,-6,9,-10,-6,3,-10,10,1,-10,-3,9,-7,-7,1,-3,5,2,3,-2,-2,5,-9,-3,-10,-7,-4,-5,7,5,7,5,-5,-5,-8,-1,1,-2,1,-3,10,4,-6,6,-4,-9,9,2,-10,-4,3,7,-1,4,-8,-5,-9,-4,-9,-8,1,3,-3,4,1,10,-5,-5,9,10,-8,-6,3,2,10,2,-9,-3,-9,6,7,1,-4,-8,-10,10], dtype = "uint64")#candidate|2425|(154,)|const|uint64
call_2424 = relay.TupleGetItem(func_1115_call(relay.reshape(const_2425.astype('uint64'), [7, 11, 2])), 0)
call_2426 = relay.TupleGetItem(func_1117_call(relay.reshape(const_2425.astype('uint64'), [7, 11, 2])), 0)
output = relay.Tuple([call_2403,call_2419,call_2421,call_2424,const_2425,])
output2 = relay.Tuple([call_2404,call_2420,call_2422,call_2426,const_2425,])
func_2427 = relay.Function([], output)
mod['func_2427'] = func_2427
mod = relay.transform.InferType()(mod)
mutated_mod['func_2427'] = func_2427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2427_call = mutated_mod.get_global_var('func_2427')
call_2428 = func_2427_call()
output = call_2428
func_2429 = relay.Function([], output)
mutated_mod['func_2429'] = func_2429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2445 = relay.var("var_2445", dtype = "float64", shape = (16, 15, 7))#candidate|2445|(16, 15, 7)|var|float64
uop_2446 = relay.cosh(var_2445.astype('float64')) # shape=(16, 15, 7)
output = relay.Tuple([uop_2446,])
output2 = relay.Tuple([uop_2446,])
func_2455 = relay.Function([var_2445,], output)
mod['func_2455'] = func_2455
mod = relay.transform.InferType()(mod)
mutated_mod['func_2455'] = func_2455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2456 = relay.var("var_2456", dtype = "float64", shape = (16, 15, 7))#candidate|2456|(16, 15, 7)|var|float64
func_2455_call = mutated_mod.get_global_var('func_2455')
call_2457 = func_2455_call(var_2456)
output = call_2457
func_2458 = relay.Function([var_2456], output)
mutated_mod['func_2458'] = func_2458
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2471 = relay.var("var_2471", dtype = "float32", shape = (6, 15, 13))#candidate|2471|(6, 15, 13)|var|float32
uop_2472 = relay.sin(var_2471.astype('float32')) # shape=(6, 15, 13)
uop_2485 = relay.log2(uop_2472.astype('float32')) # shape=(6, 15, 13)
output = uop_2485
output2 = uop_2485
func_2499 = relay.Function([var_2471,], output)
mod['func_2499'] = func_2499
mod = relay.transform.InferType()(mod)
mutated_mod['func_2499'] = func_2499
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2500 = relay.var("var_2500", dtype = "float32", shape = (6, 15, 13))#candidate|2500|(6, 15, 13)|var|float32
func_2499_call = mutated_mod.get_global_var('func_2499')
call_2501 = func_2499_call(var_2500)
output = call_2501
func_2502 = relay.Function([var_2500], output)
mutated_mod['func_2502'] = func_2502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1711_call = mod.get_global_var('func_1711')
func_1712_call = mutated_mod.get_global_var('func_1712')
call_2546 = func_1711_call()
call_2547 = func_1711_call()
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_2550 = relay.TupleGetItem(func_1205_call(), 0)
call_2551 = relay.TupleGetItem(func_1206_call(), 0)
func_279_call = mod.get_global_var('func_279')
func_283_call = mutated_mod.get_global_var('func_283')
var_2553 = relay.var("var_2553", dtype = "float64", shape = (1, 165))#candidate|2553|(1, 165)|var|float64
const_2554 = relay.const([-4,2,-9,7,8,8,-6,-2,-5,-2,9,-3,-6,3,2,6,4,-10,-10,3,-1,-9,7,3,-4,-3,9,-5,8,-6,9,-8,1,-8,-5,10,-1,-10,-2,-10,-10,-1,-3,-3,-6,1,10,-10,5,1,-8,5,-9,8,10,10,-5,6,-9,8,7,-3,-7,5,3,-4,-4,-10,4,4,8,-1,-9,10,7,5,7,10,-3,8,10,6,-8,6,-6,3,8,-6,4,-5,6,-6,8,-7,-8,8,4,1,2,-4,-2,2,-5,-7,8,2,3,-5,2,3,-6,10,-7,-3,-10,7,8,-4,-2,1,-4,-2,-1,-8,-10,2,4,-7,3,-1,-9,-7,-10,9,1,-9,-3,9,-1,-6,8,8,-10,-2,-7,7,3,-2,-2,-6,10,-7,-8,6,3,-10,-10,4,3,4,-1,5,-3,-9,-5,10,-2,-10,-3,-2,10,9,2,1,-1,7,-6,-8,-9,-5,-3,2,2,-8,8,-1,-3,8,6,-1,4,9,-10,10,3,6,2,3,-7,9,10,4,2,1,1,5,1,7,2,-3], dtype = "uint32")#candidate|2554|(210,)|const|uint32
call_2552 = relay.TupleGetItem(func_279_call(relay.reshape(var_2553.astype('float64'), [3, 5, 11]), relay.reshape(const_2554.astype('uint32'), [210,]), ), 0)
call_2555 = relay.TupleGetItem(func_283_call(relay.reshape(var_2553.astype('float64'), [3, 5, 11]), relay.reshape(const_2554.astype('uint32'), [210,]), ), 0)
uop_2563 = relay.sin(var_2553.astype('float32')) # shape=(1, 165)
output = relay.Tuple([call_2546,call_2550,call_2552,const_2554,uop_2563,])
output2 = relay.Tuple([call_2547,call_2551,call_2555,const_2554,uop_2563,])
func_2566 = relay.Function([var_2553,], output)
mod['func_2566'] = func_2566
mod = relay.transform.InferType()(mod)
var_2567 = relay.var("var_2567", dtype = "float64", shape = (1, 165))#candidate|2567|(1, 165)|var|float64
output = func_2566(var_2567)
func_2568 = relay.Function([var_2567], output)
mutated_mod['func_2568'] = func_2568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2427_call = mod.get_global_var('func_2427')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_2577 = relay.TupleGetItem(func_2427_call(), 0)
call_2578 = relay.TupleGetItem(func_2429_call(), 0)
uop_2592 = relay.cos(call_2577.astype('float32')) # shape=(7, 5, 14)
uop_2594 = relay.cos(call_2578.astype('float32')) # shape=(7, 5, 14)
uop_2601 = relay.rsqrt(call_2577.astype('float32')) # shape=(7, 5, 14)
uop_2603 = relay.rsqrt(call_2578.astype('float32')) # shape=(7, 5, 14)
func_2180_call = mod.get_global_var('func_2180')
func_2184_call = mutated_mod.get_global_var('func_2184')
var_2605 = relay.var("var_2605", dtype = "uint32", shape = (210,))#candidate|2605|(210,)|var|uint32
call_2604 = relay.TupleGetItem(func_2180_call(relay.reshape(var_2605.astype('uint32'), [210,]), relay.reshape(var_2605.astype('float32'), [6, 5, 7]), ), 1)
call_2606 = relay.TupleGetItem(func_2184_call(relay.reshape(var_2605.astype('uint32'), [210,]), relay.reshape(var_2605.astype('float32'), [6, 5, 7]), ), 1)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_2607 = relay.TupleGetItem(func_1205_call(), 0)
call_2608 = relay.TupleGetItem(func_1206_call(), 0)
uop_2611 = relay.acosh(var_2605.astype('float64')) # shape=(210,)
output = relay.Tuple([uop_2592,uop_2601,call_2604,call_2607,uop_2611,])
output2 = relay.Tuple([uop_2594,uop_2603,call_2606,call_2608,uop_2611,])
func_2613 = relay.Function([var_2605,], output)
mod['func_2613'] = func_2613
mod = relay.transform.InferType()(mod)
mutated_mod['func_2613'] = func_2613
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2614 = relay.var("var_2614", dtype = "uint32", shape = (210,))#candidate|2614|(210,)|var|uint32
func_2613_call = mutated_mod.get_global_var('func_2613')
call_2615 = func_2613_call(var_2614)
output = call_2615
func_2616 = relay.Function([var_2614], output)
mutated_mod['func_2616'] = func_2616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_919_call = mod.get_global_var('func_919')
func_920_call = mutated_mod.get_global_var('func_920')
call_2618 = relay.TupleGetItem(func_919_call(), 0)
call_2619 = relay.TupleGetItem(func_920_call(), 0)
const_2623 = relay.const([[[9,-8,-3,10,-6,10,4,-5,-7,-10,1,-1,-5,6],[-8,-2,1,3,8,7,8,5,5,8,-6,-2,-4,-7],[-9,7,-4,-4,2,10,-3,-3,6,2,-7,-3,9,-7],[-10,1,9,-7,-8,7,-8,-9,4,3,9,3,-8,-8],[4,9,2,-3,8,2,-1,-8,-6,4,-9,3,-4,6]],[[1,-8,-9,-8,9,-2,1,6,4,5,-1,1,-5,7],[-1,1,7,8,8,-9,-5,-7,4,10,-5,8,-1,-5],[-3,8,-7,7,-10,-2,-9,9,-1,-2,-8,-10,5,-9],[9,7,-8,6,-5,1,-8,-8,-3,10,-1,-6,-3,2],[-6,-8,-6,-7,-9,-10,-7,-2,4,-9,4,9,-2,-4]],[[5,6,-8,-6,-9,-1,-7,-5,-1,-7,-6,10,-8,7],[7,-6,9,6,6,4,-5,6,-5,6,5,-1,-2,2],[3,1,-1,2,8,-9,-10,-2,9,8,-8,-10,-10,5],[-3,1,6,-5,8,9,7,-4,3,3,3,-6,6,3],[10,-7,5,-6,-9,-10,-8,4,-6,-2,4,1,-9,-8]],[[6,10,-1,6,6,-9,-4,-3,-7,-10,5,4,-9,9],[-1,-2,10,10,10,9,9,-2,-8,-5,-4,-10,9,10],[-8,-6,6,7,-2,9,-4,-10,8,-5,-7,-3,-9,9],[6,6,8,4,-3,-2,-9,-9,-1,5,-10,-6,-5,7],[-10,10,6,4,1,8,9,1,2,1,10,3,-8,-9]],[[5,-5,-10,5,-4,-10,4,-10,-9,-3,2,6,-9,2],[-7,-10,-4,-7,1,-2,10,-1,9,9,2,-9,-7,-4],[4,-6,8,-3,-3,9,-4,-3,1,9,3,8,-2,-10],[3,-7,-2,8,-1,2,-3,1,2,-2,-6,-4,8,8],[10,1,2,10,3,5,1,1,10,1,-6,8,-3,2]],[[-4,-3,8,8,6,-5,-8,-6,-10,4,8,4,8,5],[4,-5,8,5,-6,8,-10,10,5,-6,-10,9,-8,2],[-4,-9,6,9,4,2,4,9,-2,2,4,6,-10,3],[-5,4,-4,10,-7,-4,2,10,-3,-9,-9,-4,-3,-8],[-5,-1,-8,2,9,9,-10,8,8,-7,8,-6,9,9]],[[-2,6,-8,8,3,-5,3,-8,-9,-4,-6,-8,10,-1],[-5,2,-7,-7,-3,-8,-4,-9,-9,9,-5,4,7,-6],[-5,-6,7,-10,-4,9,1,-6,-2,-1,3,-10,-4,-2],[6,7,-6,2,1,-8,-10,-4,6,-5,4,1,5,-6],[6,1,7,-3,-1,6,8,6,-1,-8,-10,-5,-8,-2]]], dtype = "uint64")#candidate|2623|(7, 5, 14)|const|uint64
bop_2624 = relay.subtract(call_2618.astype('uint32'), relay.reshape(const_2623.astype('uint32'), relay.shape_of(call_2618))) # shape=(7, 5, 14)
bop_2627 = relay.subtract(call_2619.astype('uint32'), relay.reshape(const_2623.astype('uint32'), relay.shape_of(call_2619))) # shape=(7, 5, 14)
func_1398_call = mod.get_global_var('func_1398')
func_1401_call = mutated_mod.get_global_var('func_1401')
var_2630 = relay.var("var_2630", dtype = "uint32", shape = ())#candidate|2630|()|var|uint32
call_2629 = relay.TupleGetItem(func_1398_call(relay.reshape(var_2630.astype('uint32'), [])), 1)
call_2631 = relay.TupleGetItem(func_1401_call(relay.reshape(var_2630.astype('uint32'), [])), 1)
func_1193_call = mod.get_global_var('func_1193')
func_1195_call = mutated_mod.get_global_var('func_1195')
call_2632 = relay.TupleGetItem(func_1193_call(), 0)
call_2633 = relay.TupleGetItem(func_1195_call(), 0)
output = relay.Tuple([bop_2624,call_2629,var_2630,call_2632,])
output2 = relay.Tuple([bop_2627,call_2631,var_2630,call_2633,])
func_2638 = relay.Function([var_2630,], output)
mod['func_2638'] = func_2638
mod = relay.transform.InferType()(mod)
var_2639 = relay.var("var_2639", dtype = "uint32", shape = ())#candidate|2639|()|var|uint32
output = func_2638(var_2639)
func_2640 = relay.Function([var_2639], output)
mutated_mod['func_2640'] = func_2640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1711_call = mod.get_global_var('func_1711')
func_1712_call = mutated_mod.get_global_var('func_1712')
call_2645 = func_1711_call()
call_2646 = func_1711_call()
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_2654 = func_595_call()
call_2655 = func_595_call()
output = relay.Tuple([call_2645,call_2654,])
output2 = relay.Tuple([call_2646,call_2655,])
func_2661 = relay.Function([], output)
mod['func_2661'] = func_2661
mod = relay.transform.InferType()(mod)
output = func_2661()
func_2662 = relay.Function([], output)
mutated_mod['func_2662'] = func_2662
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2678 = relay.var("var_2678", dtype = "uint8", shape = ())#candidate|2678|()|var|uint8
var_2679 = relay.var("var_2679", dtype = "uint8", shape = (16, 6, 1))#candidate|2679|(16, 6, 1)|var|uint8
bop_2680 = relay.bitwise_or(var_2678.astype('uint8'), var_2679.astype('uint8')) # shape=(16, 6, 1)
bop_2690 = relay.logical_or(var_2679.astype('bool'), relay.reshape(bop_2680.astype('bool'), relay.shape_of(var_2679))) # shape=(16, 6, 1)
output = relay.Tuple([bop_2690,])
output2 = relay.Tuple([bop_2690,])
func_2693 = relay.Function([var_2678,var_2679,], output)
mod['func_2693'] = func_2693
mod = relay.transform.InferType()(mod)
mutated_mod['func_2693'] = func_2693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2693_call = mutated_mod.get_global_var('func_2693')
var_2695 = relay.var("var_2695", dtype = "uint8", shape = ())#candidate|2695|()|var|uint8
var_2696 = relay.var("var_2696", dtype = "uint8", shape = (16, 6, 1))#candidate|2696|(16, 6, 1)|var|uint8
call_2694 = func_2693_call(var_2695,var_2696,)
output = call_2694
func_2697 = relay.Function([var_2695,var_2696,], output)
mutated_mod['func_2697'] = func_2697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2427_call = mod.get_global_var('func_2427')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_2811 = relay.TupleGetItem(func_2427_call(), 1)
call_2812 = relay.TupleGetItem(func_2429_call(), 1)
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
const_2832 = relay.const([8,10,-3,-4,9,3,3,-1,-7,8,-9,-1,1,7,9,9,-3,-1,-1,3,6,6,-10,-8,3,9,6,-6,-1,-10,-10,8,-7,-10,-6,8,10,5,-10,-7,1,-8,9,-2,6,-1,-1,2,9,-6,-6,9,8,-6,-9,5,10,-4,9,9,10,-2,10,6,-5,-4,-7,-6,9,7,-4,7,-8,-1,9,-2,10,9,-7,9,9,2,-8,-3,8,-4,-4,6,-2,-9,-7,-1,5,6,4,4,1,-9,2,-6,4,5,-3,-2,-8,-7,1,3,-7,-10,6,-4,7,6,7,-4,-3,9,-9,-10,-3,3,6,-2,5,-6,5,8,7,-5,-5,5,9,-2,6,-7,-3,-3,-4,-4,6,-10,3,-4,9,3,8,1,-4,6,-7,7,3,2,6,8,7,-4,5,1,9,9,-3,-5,-3,7,5,-3,5,-8,1,-4,4,-1,5,-5,7,2,-4,7,9,9,-9,2,6,-4,8,7,5,2,-9,6,3,-6,-4,-4,8,-7,-4,2,1,-8,3,10,1,-1,9,8,5,8], dtype = "uint32")#candidate|2832|(210,)|const|uint32
call_2831 = func_168_call(relay.reshape(const_2832.astype('uint32'), [6, 5, 7]))
call_2833 = func_168_call(relay.reshape(const_2832.astype('uint32'), [6, 5, 7]))
output = relay.Tuple([call_2811,call_2831,const_2832,])
output2 = relay.Tuple([call_2812,call_2833,const_2832,])
func_2836 = relay.Function([], output)
mod['func_2836'] = func_2836
mod = relay.transform.InferType()(mod)
output = func_2836()
func_2837 = relay.Function([], output)
mutated_mod['func_2837'] = func_2837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_2846 = relay.TupleGetItem(func_1205_call(), 0)
call_2847 = relay.TupleGetItem(func_1206_call(), 0)
func_1878_call = mod.get_global_var('func_1878')
func_1882_call = mutated_mod.get_global_var('func_1882')
var_2866 = relay.var("var_2866", dtype = "float32", shape = (60,))#candidate|2866|(60,)|var|float32
var_2867 = relay.var("var_2867", dtype = "float32", shape = (720,))#candidate|2867|(720,)|var|float32
call_2865 = relay.TupleGetItem(func_1878_call(relay.reshape(var_2866.astype('float32'), [1, 12, 5]), relay.reshape(var_2867.astype('float32'), [12, 12, 5]), ), 1)
call_2868 = relay.TupleGetItem(func_1882_call(relay.reshape(var_2866.astype('float32'), [1, 12, 5]), relay.reshape(var_2867.astype('float32'), [12, 12, 5]), ), 1)
const_2872 = relay.const([[[-2,-7,1,4,5,-3,-10,-2,7,4,1,3,-4,6],[7,-5,10,-6,6,-6,-5,-8,2,-5,9,4,-9,-3],[-6,-5,4,3,-2,3,-8,-2,10,8,-9,10,2,-9],[1,-8,-1,-9,4,7,1,-7,10,2,9,-3,-4,-6],[7,9,-7,2,-1,5,2,-3,-3,-2,8,-7,3,-5]],[[1,3,-9,5,-1,-8,-7,-2,-4,-2,5,-3,5,2],[-8,-4,10,-6,-10,-7,-9,7,-5,-6,4,-7,1,2],[10,5,10,-6,7,-1,4,-1,-2,-8,9,-7,2,-2],[6,1,7,-1,-5,9,-10,10,6,-8,2,-5,-1,-4],[8,6,-9,9,2,4,8,9,2,5,-1,-8,10,3]],[[-8,4,2,-2,-6,-8,-3,-6,-6,1,6,-7,1,-1],[-3,-4,-1,8,10,-6,-1,7,-5,-4,-9,8,-5,2],[4,-8,-10,-7,3,-4,-7,1,5,1,2,10,4,-9],[-6,-4,-6,5,-5,7,-2,-10,3,7,1,7,-5,7],[6,-8,-8,-1,3,8,-2,7,-6,-3,10,7,9,-9]],[[1,-4,3,-9,2,-5,8,6,-8,4,-2,5,6,-5],[5,9,-9,5,5,-3,4,6,1,1,-3,-7,3,-6],[5,-4,-7,-10,-8,-8,-7,-1,-9,4,-7,1,-2,-6],[10,6,3,-8,4,7,-3,6,8,-2,6,-8,10,4],[8,7,-2,-3,-4,7,1,10,1,-3,-5,7,-8,4]],[[-4,10,-8,10,-1,-7,6,-2,8,-10,-10,-9,5,-6],[-10,-2,9,-4,10,-9,9,-5,7,-1,-1,-3,3,8],[7,4,6,-10,8,4,-10,-3,8,-3,7,-10,-6,-1],[-5,8,5,-9,-7,-6,5,-7,4,7,7,-4,5,-5],[7,1,-5,3,-2,-10,3,6,-7,-6,-2,-2,-2,-3]],[[2,-7,4,-2,8,8,10,-9,-6,-1,-9,-4,8,1],[-2,-7,2,3,4,6,1,-4,-4,3,9,10,1,-10],[-10,10,-5,6,3,-5,5,2,7,-8,-10,-8,-7,8],[4,8,9,8,7,3,-5,10,2,-7,-8,10,8,-5],[-6,-4,3,6,1,7,-8,-9,-1,-3,9,-3,-7,-4]],[[-9,-1,-4,-9,6,-8,-7,-5,5,8,-3,10,2,-10],[6,-7,3,-4,-10,3,-6,3,5,-10,1,8,-10,-7],[-4,3,-1,5,-8,-10,-9,6,-3,1,-6,10,-1,-3],[-9,-5,-7,2,-1,-1,-5,-9,5,2,-4,-8,5,2],[-8,-9,7,-9,4,-4,8,6,-8,10,2,-3,-4,-1]]], dtype = "uint64")#candidate|2872|(7, 5, 14)|const|uint64
bop_2873 = relay.bitwise_and(call_2846.astype('uint8'), relay.reshape(const_2872.astype('uint8'), relay.shape_of(call_2846))) # shape=(7, 5, 14)
bop_2876 = relay.bitwise_and(call_2847.astype('uint8'), relay.reshape(const_2872.astype('uint8'), relay.shape_of(call_2847))) # shape=(7, 5, 14)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_2877 = relay.TupleGetItem(func_1820_call(), 0)
call_2878 = relay.TupleGetItem(func_1822_call(), 0)
output = relay.Tuple([call_2865,var_2866,var_2867,bop_2873,call_2877,])
output2 = relay.Tuple([call_2868,var_2866,var_2867,bop_2876,call_2878,])
func_2908 = relay.Function([var_2866,var_2867,], output)
mod['func_2908'] = func_2908
mod = relay.transform.InferType()(mod)
var_2909 = relay.var("var_2909", dtype = "float32", shape = (60,))#candidate|2909|(60,)|var|float32
var_2910 = relay.var("var_2910", dtype = "float32", shape = (720,))#candidate|2910|(720,)|var|float32
output = func_2908(var_2909,var_2910,)
func_2911 = relay.Function([var_2909,var_2910,], output)
mutated_mod['func_2911'] = func_2911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_2931 = relay.TupleGetItem(func_1820_call(), 0)
call_2932 = relay.TupleGetItem(func_1822_call(), 0)
const_2938 = relay.const([[[-10,7,4,-2,-9,-6,-6,8,6,7,-10,4,-2,2],[-1,-9,3,-9,-1,6,9,-5,-4,10,1,-6,4,8],[3,9,9,4,-6,-9,-1,9,8,-4,-6,-2,2,9],[-10,-1,5,4,7,-7,9,4,-2,-2,6,5,-10,1],[7,-7,5,1,-7,-7,4,-9,-10,5,-5,-4,-2,-3]],[[8,-6,1,3,3,-9,10,5,8,7,9,3,8,5],[8,4,-1,2,-4,-2,-10,7,5,-4,-8,-4,-4,10],[-6,-3,4,-2,-8,1,-1,10,3,3,-9,-4,1,-3],[7,-8,2,-7,9,-3,4,-10,6,8,7,-9,10,5],[-3,6,-4,1,8,-2,7,-5,-9,6,6,7,5,10]],[[-1,-7,-3,-2,-9,-5,-1,5,4,1,-6,-1,10,6],[7,-3,10,3,-6,2,-10,-4,6,10,-1,7,5,10],[7,-5,1,-3,1,-6,-10,2,-7,-10,-6,-7,9,-4],[2,-4,-9,5,8,-3,-3,5,9,-3,2,9,4,-4],[-10,1,-2,2,3,-3,5,-9,-7,4,-2,10,2,3]],[[-7,-3,5,8,-7,9,8,-3,10,-5,-8,2,-8,5],[6,-10,-7,10,4,-1,8,5,4,1,1,2,5,-9],[-8,4,6,-5,-6,-7,4,-5,2,10,-7,-1,-9,6],[-6,-8,1,8,-8,2,-9,6,9,-6,1,-6,-9,5],[-1,-3,-7,-3,6,8,4,8,1,9,-5,-2,2,-3]],[[6,-10,-10,-3,-7,7,-6,7,-7,7,9,7,-10,-10],[-6,5,2,6,-2,1,5,-1,5,3,3,7,6,7],[4,10,2,-1,-3,-6,-7,-4,-5,5,5,1,10,9],[3,-3,3,8,-9,10,7,6,-5,10,5,1,5,-5],[9,2,4,-10,9,2,6,-9,-10,-8,-3,-6,-4,-6]],[[10,-6,9,-2,5,10,1,-1,6,9,-5,2,7,-4],[-6,2,6,-4,9,-8,9,10,9,-4,-3,2,3,-4],[1,-1,-10,2,2,1,-1,6,6,-9,-7,-2,7,-8],[8,-1,10,8,7,-8,-6,-10,7,-9,2,-7,-1,9],[5,-10,-9,-3,-5,3,-3,-2,-9,7,8,8,-2,-1]],[[8,-2,-7,-5,3,7,1,9,10,-2,-4,6,5,-4],[-3,-1,-2,3,5,-8,-7,4,7,-3,-7,-8,6,-2],[10,-9,8,-3,4,4,3,8,8,-10,-9,4,8,4],[-7,-6,-4,-9,6,7,-7,1,-2,10,3,9,-2,8],[6,-3,-10,-2,-5,-7,5,5,4,2,7,7,1,-3]]], dtype = "uint64")#candidate|2938|(7, 5, 14)|const|uint64
bop_2939 = relay.logical_xor(call_2931.astype('uint8'), relay.reshape(const_2938.astype('uint8'), relay.shape_of(call_2931))) # shape=(7, 5, 14)
bop_2942 = relay.logical_xor(call_2932.astype('uint8'), relay.reshape(const_2938.astype('uint8'), relay.shape_of(call_2932))) # shape=(7, 5, 14)
output = bop_2939
output2 = bop_2942
func_2954 = relay.Function([], output)
mod['func_2954'] = func_2954
mod = relay.transform.InferType()(mod)
mutated_mod['func_2954'] = func_2954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2954_call = mutated_mod.get_global_var('func_2954')
call_2955 = func_2954_call()
output = call_2955
func_2956 = relay.Function([], output)
mutated_mod['func_2956'] = func_2956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mod.get_global_var('func_1571')
func_1572_call = mutated_mod.get_global_var('func_1572')
call_2964 = relay.TupleGetItem(func_1571_call(), 0)
call_2965 = relay.TupleGetItem(func_1572_call(), 0)
output = call_2964
output2 = call_2965
func_2968 = relay.Function([], output)
mod['func_2968'] = func_2968
mod = relay.transform.InferType()(mod)
mutated_mod['func_2968'] = func_2968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mutated_mod.get_global_var('func_2968')
call_2969 = func_2968_call()
output = call_2969
func_2970 = relay.Function([], output)
mutated_mod['func_2970'] = func_2970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mod.get_global_var('func_2968')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_2978 = func_2968_call()
call_2979 = func_2968_call()
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_2981 = relay.TupleGetItem(func_1205_call(), 0)
call_2982 = relay.TupleGetItem(func_1206_call(), 0)
func_2968_call = mod.get_global_var('func_2968')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_2990 = func_2968_call()
call_2991 = func_2968_call()
uop_2995 = relay.sinh(call_2978.astype('float64')) # shape=(7, 5, 14)
uop_2997 = relay.sinh(call_2979.astype('float64')) # shape=(7, 5, 14)
output = relay.Tuple([call_2981,call_2990,uop_2995,])
output2 = relay.Tuple([call_2982,call_2991,uop_2997,])
func_2999 = relay.Function([], output)
mod['func_2999'] = func_2999
mod = relay.transform.InferType()(mod)
mutated_mod['func_2999'] = func_2999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2999_call = mutated_mod.get_global_var('func_2999')
call_3000 = func_2999_call()
output = call_3000
func_3001 = relay.Function([], output)
mutated_mod['func_3001'] = func_3001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mod.get_global_var('func_2836')
func_2837_call = mutated_mod.get_global_var('func_2837')
call_3049 = relay.TupleGetItem(func_2836_call(), 2)
call_3050 = relay.TupleGetItem(func_2837_call(), 2)
func_2247_call = mod.get_global_var('func_2247')
func_2250_call = mutated_mod.get_global_var('func_2250')
const_3068 = relay.const([4.682719,-7.010559,-4.800449,4.893525,-7.040402,-8.386012,-9.607312,1.469846,2.340836,3.179425,2.711820,-6.918363,4.326982,-0.159804,4.345602,-9.497511,-6.611167,-3.475423,9.503330,-3.949641,-9.542897,-4.883176,1.914506,5.405808], dtype = "float32")#candidate|3068|(24,)|const|float32
call_3067 = relay.TupleGetItem(func_2247_call(relay.reshape(const_3068.astype('float32'), [3, 4, 2]), relay.reshape(const_3068.astype('float32'), [3, 4, 2]), ), 0)
call_3069 = relay.TupleGetItem(func_2250_call(relay.reshape(const_3068.astype('float32'), [3, 4, 2]), relay.reshape(const_3068.astype('float32'), [3, 4, 2]), ), 0)
output = relay.Tuple([call_3049,call_3067,const_3068,])
output2 = relay.Tuple([call_3050,call_3069,const_3068,])
func_3073 = relay.Function([], output)
mod['func_3073'] = func_3073
mod = relay.transform.InferType()(mod)
mutated_mod['func_3073'] = func_3073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3073_call = mutated_mod.get_global_var('func_3073')
call_3074 = func_3073_call()
output = call_3074
func_3075 = relay.Function([], output)
mutated_mod['func_3075'] = func_3075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2427_call = mod.get_global_var('func_2427')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_3089 = relay.TupleGetItem(func_2427_call(), 3)
call_3090 = relay.TupleGetItem(func_2429_call(), 3)
const_3093 = relay.const([[[6,3],[3,7],[1,-9],[-4,5],[1,-3],[-10,2],[5,9],[4,9],[9,9],[9,5],[7,-10]],[[-2,-6],[-2,-5],[-3,-2],[7,-10],[-9,10],[-10,-1],[7,2],[3,-7],[-6,-5],[4,-3],[-8,-3]],[[-8,-5],[-3,-6],[-6,-3],[-6,-8],[-6,-1],[2,1],[7,10],[10,-10],[8,5],[10,4],[10,-10]],[[-2,-3],[-7,-1],[10,4],[-7,-3],[-10,5],[-8,-9],[2,4],[-1,-8],[5,3],[6,1],[-7,3]],[[1,-1],[9,-7],[6,5],[9,10],[6,-7],[7,-4],[-4,-9],[2,-7],[10,-2],[-5,7],[-6,9]],[[-2,7],[5,10],[4,7],[1,-10],[-9,-3],[-6,7],[-5,1],[7,-7],[9,8],[8,7],[3,1]],[[-9,-4],[8,7],[-4,5],[9,1],[8,-6],[1,-10],[-3,2],[-3,10],[6,2],[3,7],[-4,-7]]], dtype = "uint64")#candidate|3093|(7, 11, 2)|const|uint64
bop_3094 = relay.divide(call_3089.astype('float64'), relay.reshape(const_3093.astype('float64'), relay.shape_of(call_3089))) # shape=(7, 11, 2)
bop_3097 = relay.divide(call_3090.astype('float64'), relay.reshape(const_3093.astype('float64'), relay.shape_of(call_3090))) # shape=(7, 11, 2)
func_2247_call = mod.get_global_var('func_2247')
func_2250_call = mutated_mod.get_global_var('func_2250')
const_3111 = relay.const([[3.775869,3.475401,6.747378,6.469869,6.200787,5.990203,3.148207,-6.632443,9.828363,-7.978157,-5.068817,3.499251],[-8.179773,2.394963,5.896771,5.163052,4.678440,6.114506,9.542517,1.984377,1.736556,-6.278067,7.696767,-0.560407]], dtype = "float32")#candidate|3111|(2, 12)|const|float32
call_3110 = relay.TupleGetItem(func_2247_call(relay.reshape(const_3111.astype('float32'), [3, 4, 2]), relay.reshape(const_3111.astype('float32'), [3, 4, 2]), ), 0)
call_3112 = relay.TupleGetItem(func_2250_call(relay.reshape(const_3111.astype('float32'), [3, 4, 2]), relay.reshape(const_3111.astype('float32'), [3, 4, 2]), ), 0)
func_1571_call = mod.get_global_var('func_1571')
func_1572_call = mutated_mod.get_global_var('func_1572')
call_3113 = relay.TupleGetItem(func_1571_call(), 0)
call_3114 = relay.TupleGetItem(func_1572_call(), 0)
output = relay.Tuple([bop_3094,call_3110,const_3111,call_3113,])
output2 = relay.Tuple([bop_3097,call_3112,const_3111,call_3114,])
func_3121 = relay.Function([], output)
mod['func_3121'] = func_3121
mod = relay.transform.InferType()(mod)
mutated_mod['func_3121'] = func_3121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mutated_mod.get_global_var('func_3121')
call_3122 = func_3121_call()
output = call_3122
func_3123 = relay.Function([], output)
mutated_mod['func_3123'] = func_3123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_919_call = mod.get_global_var('func_919')
func_920_call = mutated_mod.get_global_var('func_920')
call_3137 = relay.TupleGetItem(func_919_call(), 0)
call_3138 = relay.TupleGetItem(func_920_call(), 0)
func_2836_call = mod.get_global_var('func_2836')
func_2837_call = mutated_mod.get_global_var('func_2837')
call_3146 = relay.TupleGetItem(func_2836_call(), 0)
call_3147 = relay.TupleGetItem(func_2837_call(), 0)
output = relay.Tuple([call_3137,call_3146,])
output2 = relay.Tuple([call_3138,call_3147,])
func_3150 = relay.Function([], output)
mod['func_3150'] = func_3150
mod = relay.transform.InferType()(mod)
mutated_mod['func_3150'] = func_3150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3150_call = mutated_mod.get_global_var('func_3150')
call_3151 = func_3150_call()
output = call_3151
func_3152 = relay.Function([], output)
mutated_mod['func_3152'] = func_3152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_3177 = relay.TupleGetItem(func_965_call(), 0)
call_3178 = relay.TupleGetItem(func_967_call(), 0)
func_3150_call = mod.get_global_var('func_3150')
func_3152_call = mutated_mod.get_global_var('func_3152')
call_3180 = relay.TupleGetItem(func_3150_call(), 1)
call_3181 = relay.TupleGetItem(func_3152_call(), 1)
func_2566_call = mod.get_global_var('func_2566')
func_2568_call = mutated_mod.get_global_var('func_2568')
const_3188 = relay.const([-6.998643,6.343223,-1.391428,3.522350,8.207620,8.729841,9.081615,-5.887359,6.647196,-7.797826,9.677663,3.473169,-8.245829,6.644964,8.697792,-0.127757,1.966548,-8.365358,-3.791745,8.098934,-4.833049,-9.094257,-1.146076,1.585714,6.258856,-4.056278,0.679102,-1.677210,-6.664323,8.062614,-0.475045,9.928873,1.832493,-5.402261,7.986542,4.242491,-5.937582,0.872986,1.244580,-1.885976,-8.610307,7.024514,-1.654171,3.760856,9.974470,6.088644,2.496431,2.590140,-6.889486,-8.702195,9.554497,6.583965,5.943359,5.167098,1.828704,0.930737,-7.591064,9.620931,-2.759964,5.617921,-7.130052,-7.926094,1.670772,-7.057808,1.009581,0.454732,3.519594,-9.051652,-2.092339,0.265663,-8.237078,0.315637,6.325247,8.021502,-6.024231,-1.906098,4.398657,-3.194102,-6.400989,7.445415,5.892135,0.835396,8.538460,-6.642059,3.397090,-3.542109,-9.327691,-3.649399,-2.192695,-8.615993,-5.349604,1.501020,9.893173,-5.437906,6.743058,6.008076,-5.678409,9.986891,-5.643081,7.616761,0.090176,5.729735,-5.228641,1.201949,-6.871966,4.329990,-8.740902,-8.682369,-9.538174,-6.217290,-8.324352,-6.041327,-7.210534,7.322034,2.433127,-0.874952,-9.793170,5.393573,2.880372,2.193584,-1.076084,-8.868745,-1.418638,-1.070658,6.811705,-4.763486,-2.445240,-6.046355,-1.918457,5.365455,4.675486,-3.640075,-3.434963,-4.416609,-8.178908,7.955535,-7.300316,-9.363654,-2.939856,9.464447,8.671130,-7.155740,-7.818208,-7.983238,-2.984182,0.677717,4.448938,2.118079,2.931794,2.210665,1.561804,-6.591746,-0.370785,-3.037194,4.296899,-4.801197,7.779237,-4.165672,9.432497,-1.776781,-1.096294,9.837036,5.931084,4.922017,-1.357257], dtype = "float64")#candidate|3188|(165,)|const|float64
call_3187 = relay.TupleGetItem(func_2566_call(relay.reshape(const_3188.astype('float64'), [1, 165])), 3)
call_3189 = relay.TupleGetItem(func_2568_call(relay.reshape(const_3188.astype('float64'), [1, 165])), 3)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_3202 = relay.TupleGetItem(func_1205_call(), 0)
call_3203 = relay.TupleGetItem(func_1206_call(), 0)
output = relay.Tuple([call_3177,call_3180,call_3187,const_3188,call_3202,])
output2 = relay.Tuple([call_3178,call_3181,call_3189,const_3188,call_3203,])
func_3210 = relay.Function([], output)
mod['func_3210'] = func_3210
mod = relay.transform.InferType()(mod)
mutated_mod['func_3210'] = func_3210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3210_call = mutated_mod.get_global_var('func_3210')
call_3211 = func_3210_call()
output = call_3211
func_3212 = relay.Function([], output)
mutated_mod['func_3212'] = func_3212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_577_call = mutated_mod.get_global_var('func_577')
call_3229 = relay.TupleGetItem(func_575_call(), 0)
call_3230 = relay.TupleGetItem(func_577_call(), 0)
output = relay.Tuple([call_3229,])
output2 = relay.Tuple([call_3230,])
func_3236 = relay.Function([], output)
mod['func_3236'] = func_3236
mod = relay.transform.InferType()(mod)
mutated_mod['func_3236'] = func_3236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mutated_mod.get_global_var('func_3236')
call_3237 = func_3236_call()
output = call_3237
func_3238 = relay.Function([], output)
mutated_mod['func_3238'] = func_3238
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3299 = relay.const(-9, dtype = "uint16")#candidate|3299|()|const|uint16
var_3300 = relay.var("var_3300", dtype = "uint16", shape = (5, 6, 5))#candidate|3300|(5, 6, 5)|var|uint16
bop_3301 = relay.not_equal(const_3299.astype('bool'), var_3300.astype('bool')) # shape=(5, 6, 5)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_3307 = relay.TupleGetItem(func_1820_call(), 0)
call_3308 = relay.TupleGetItem(func_1822_call(), 0)
bop_3337 = relay.bitwise_or(bop_3301.astype('int64'), relay.reshape(var_3300.astype('int64'), relay.shape_of(bop_3301))) # shape=(5, 6, 5)
bop_3351 = relay.maximum(call_3307.astype('uint16'), const_3299.astype('uint16')) # shape=(7, 5, 14)
bop_3354 = relay.maximum(call_3308.astype('uint16'), const_3299.astype('uint16')) # shape=(7, 5, 14)
var_3355 = relay.var("var_3355", dtype = "int64", shape = (5, 6, 5))#candidate|3355|(5, 6, 5)|var|int64
bop_3356 = relay.bitwise_xor(bop_3337.astype('int64'), relay.reshape(var_3355.astype('int64'), relay.shape_of(bop_3337))) # shape=(5, 6, 5)
output = relay.Tuple([bop_3351,bop_3356,])
output2 = relay.Tuple([bop_3354,bop_3356,])
func_3361 = relay.Function([var_3300,var_3355,], output)
mod['func_3361'] = func_3361
mod = relay.transform.InferType()(mod)
var_3362 = relay.var("var_3362", dtype = "uint16", shape = (5, 6, 5))#candidate|3362|(5, 6, 5)|var|uint16
var_3363 = relay.var("var_3363", dtype = "int64", shape = (5, 6, 5))#candidate|3363|(5, 6, 5)|var|int64
output = func_3361(var_3362,var_3363,)
func_3364 = relay.Function([var_3362,var_3363,], output)
mutated_mod['func_3364'] = func_3364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3383 = relay.var("var_3383", dtype = "int16", shape = (2, 5, 1))#candidate|3383|(2, 5, 1)|var|int16
var_3384 = relay.var("var_3384", dtype = "int16", shape = (2, 5, 2))#candidate|3384|(2, 5, 2)|var|int16
bop_3385 = relay.multiply(var_3383.astype('int16'), var_3384.astype('int16')) # shape=(2, 5, 2)
output = bop_3385
output2 = bop_3385
func_3394 = relay.Function([var_3383,var_3384,], output)
mod['func_3394'] = func_3394
mod = relay.transform.InferType()(mod)
mutated_mod['func_3394'] = func_3394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3394_call = mutated_mod.get_global_var('func_3394')
var_3396 = relay.var("var_3396", dtype = "int16", shape = (2, 5, 1))#candidate|3396|(2, 5, 1)|var|int16
var_3397 = relay.var("var_3397", dtype = "int16", shape = (2, 5, 2))#candidate|3397|(2, 5, 2)|var|int16
call_3395 = func_3394_call(var_3396,var_3397,)
output = call_3395
func_3398 = relay.Function([var_3396,var_3397,], output)
mutated_mod['func_3398'] = func_3398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_3419 = relay.TupleGetItem(func_965_call(), 0)
call_3420 = relay.TupleGetItem(func_967_call(), 0)
output = call_3419
output2 = call_3420
func_3440 = relay.Function([], output)
mod['func_3440'] = func_3440
mod = relay.transform.InferType()(mod)
output = func_3440()
func_3441 = relay.Function([], output)
mutated_mod['func_3441'] = func_3441
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3552 = relay.const([[[-1.857866,6.282223,2.136874,-1.025811,4.638060,4.854003,-3.903803,7.490713,0.343506,0.466297,-6.811856,0.556131,-7.400659,5.148271,-4.620886,-9.874267],[3.392859,-4.816666,-6.437131,1.644430,-6.009272,8.150879,-7.642595,-0.209648,2.119129,2.181629,3.776495,1.303113,6.302709,-9.677650,-1.172802,-3.079721],[1.620092,-6.641595,3.611830,0.767440,-1.921047,-9.558669,-9.691007,-6.677732,-3.195699,3.014460,-2.397101,-2.274056,8.670156,-1.382343,4.087131,2.992013],[3.619326,-0.715902,6.523225,-7.428968,6.684966,-8.986968,-4.139741,8.171564,-6.925219,-6.339564,-3.603348,-7.529489,-3.267485,4.305652,0.483249,-7.884427],[-0.103115,3.602697,-3.702122,5.966272,-7.481516,3.559985,-2.608390,3.628876,7.291846,-4.343021,-8.978131,6.958322,8.512411,6.021178,6.682709,3.760307]]], dtype = "float32")#candidate|3552|(1, 5, 16)|const|float32
var_3553 = relay.var("var_3553", dtype = "float32", shape = (4, 5, 16))#candidate|3553|(4, 5, 16)|var|float32
bop_3554 = relay.divide(const_3552.astype('float32'), var_3553.astype('float32')) # shape=(4, 5, 16)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_3557 = relay.TupleGetItem(func_3121_call(), 0)
call_3558 = relay.TupleGetItem(func_3123_call(), 0)
var_3567 = relay.var("var_3567", dtype = "float64", shape = (7, 11, 2))#candidate|3567|(7, 11, 2)|var|float64
bop_3568 = relay.bitwise_and(call_3557.astype('int8'), relay.reshape(var_3567.astype('int8'), relay.shape_of(call_3557))) # shape=(7, 11, 2)
bop_3571 = relay.bitwise_and(call_3558.astype('int8'), relay.reshape(var_3567.astype('int8'), relay.shape_of(call_3558))) # shape=(7, 11, 2)
output = relay.Tuple([bop_3554,bop_3568,])
output2 = relay.Tuple([bop_3554,bop_3571,])
func_3574 = relay.Function([var_3553,var_3567,], output)
mod['func_3574'] = func_3574
mod = relay.transform.InferType()(mod)
mutated_mod['func_3574'] = func_3574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3574_call = mutated_mod.get_global_var('func_3574')
var_3576 = relay.var("var_3576", dtype = "float32", shape = (4, 5, 16))#candidate|3576|(4, 5, 16)|var|float32
var_3577 = relay.var("var_3577", dtype = "float64", shape = (7, 11, 2))#candidate|3577|(7, 11, 2)|var|float64
call_3575 = func_3574_call(var_3576,var_3577,)
output = call_3575
func_3578 = relay.Function([var_3576,var_3577,], output)
mutated_mod['func_3578'] = func_3578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_3620 = relay.TupleGetItem(func_3236_call(), 0)
call_3621 = relay.TupleGetItem(func_3238_call(), 0)
output = call_3620
output2 = call_3621
func_3637 = relay.Function([], output)
mod['func_3637'] = func_3637
mod = relay.transform.InferType()(mod)
output = func_3637()
func_3638 = relay.Function([], output)
mutated_mod['func_3638'] = func_3638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_3698 = relay.TupleGetItem(func_1994_call(), 0)
call_3699 = relay.TupleGetItem(func_1996_call(), 0)
output = call_3698
output2 = call_3699
func_3717 = relay.Function([], output)
mod['func_3717'] = func_3717
mod = relay.transform.InferType()(mod)
mutated_mod['func_3717'] = func_3717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3717_call = mutated_mod.get_global_var('func_3717')
call_3718 = func_3717_call()
output = call_3718
func_3719 = relay.Function([], output)
mutated_mod['func_3719'] = func_3719
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3795 = relay.var("var_3795", dtype = "float64", shape = (7, 9, 8))#candidate|3795|(7, 9, 8)|var|float64
uop_3796 = relay.asin(var_3795.astype('float64')) # shape=(7, 9, 8)
var_3798 = relay.var("var_3798", dtype = "float64", shape = (7, 9, 8))#candidate|3798|(7, 9, 8)|var|float64
bop_3799 = relay.greater_equal(uop_3796.astype('bool'), relay.reshape(var_3798.astype('bool'), relay.shape_of(uop_3796))) # shape=(7, 9, 8)
bop_3806 = relay.subtract(bop_3799.astype('int8'), relay.reshape(var_3795.astype('int8'), relay.shape_of(bop_3799))) # shape=(7, 9, 8)
output = relay.Tuple([bop_3806,])
output2 = relay.Tuple([bop_3806,])
func_3843 = relay.Function([var_3795,var_3798,], output)
mod['func_3843'] = func_3843
mod = relay.transform.InferType()(mod)
mutated_mod['func_3843'] = func_3843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3843_call = mutated_mod.get_global_var('func_3843')
var_3845 = relay.var("var_3845", dtype = "float64", shape = (7, 9, 8))#candidate|3845|(7, 9, 8)|var|float64
var_3846 = relay.var("var_3846", dtype = "float64", shape = (7, 9, 8))#candidate|3846|(7, 9, 8)|var|float64
call_3844 = func_3843_call(var_3845,var_3846,)
output = call_3844
func_3847 = relay.Function([var_3845,var_3846,], output)
mutated_mod['func_3847'] = func_3847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3717_call = mod.get_global_var('func_3717')
func_3719_call = mutated_mod.get_global_var('func_3719')
call_3939 = func_3717_call()
call_3940 = func_3717_call()
const_3960 = relay.const([[[-10,10,8,2,-7,-1,-8,8,-3,-6,-1,9,-9,-4],[-5,4,2,3,-9,5,-9,8,-5,-9,-9,-9,8,-6],[7,3,9,-9,3,-2,8,6,-4,-5,1,7,-1,-10],[-6,-7,-8,-9,10,-7,2,5,7,-9,8,-9,-10,-8],[-7,-9,7,-10,-6,2,-6,9,10,-10,-5,-9,-3,-3]],[[9,5,2,-10,9,5,-8,-3,8,4,6,-7,5,6],[-4,-2,-10,8,-10,-4,6,-8,8,1,-3,-4,-9,10],[4,-1,-4,-3,1,-10,-10,1,4,2,-1,8,8,-3],[-2,10,-8,6,7,10,-1,-8,-7,-6,-10,-4,1,-5],[3,-5,-10,3,-9,3,10,-1,-6,-3,10,3,-10,-1]],[[9,10,-5,-9,2,-6,-2,-7,4,5,-9,-2,-10,8],[-2,-10,6,-4,-5,-5,-6,-7,2,3,4,-6,8,1],[-3,-7,6,5,-7,3,4,10,1,-8,-3,-8,9,-9],[4,-5,7,-1,9,-6,-8,10,-7,2,2,-2,1,4],[-6,8,-5,6,-5,6,6,2,-1,4,7,-7,-5,3]],[[-10,7,2,-5,-10,-8,9,-1,-5,7,-7,5,6,-10],[2,-9,2,8,3,10,4,10,-1,-6,-6,-6,5,-7],[-5,4,-4,-10,8,2,-3,9,-10,1,-2,2,2,-10],[-9,-10,6,2,6,6,-3,-9,1,-4,-7,-6,5,-6],[6,-6,5,-9,-7,-10,-6,8,7,6,3,2,-6,-8]],[[6,8,10,-7,7,7,-1,-8,5,4,5,-3,9,-8],[-4,4,10,2,-5,6,-8,-7,-10,-6,2,9,10,-6],[7,-6,2,-1,-3,6,-5,-9,5,-2,10,2,-7,-9],[-4,8,1,-2,-3,7,7,3,6,-5,-7,-8,6,-10],[2,2,4,-7,3,8,-2,3,8,3,7,3,-6,2]],[[2,5,-1,9,-6,-4,8,6,-7,-1,-4,-9,2,-6],[4,10,-9,-9,1,-10,6,5,-6,-6,-9,-9,1,5],[-1,-2,8,8,-9,2,5,-9,7,-5,-5,7,-7,-9],[6,2,3,-10,-7,10,7,6,-5,-5,8,-5,-10,-1],[1,-7,-3,2,-2,9,-3,3,-3,2,-5,10,6,10]],[[-8,-6,10,3,10,-9,2,-10,-1,4,6,-1,4,4],[-7,-9,5,1,7,-9,1,-9,-8,-7,6,2,-1,10],[-6,-7,-1,5,2,-1,2,-7,-8,6,-9,-4,6,6],[-2,-3,3,1,-6,1,-4,8,10,9,-6,-3,-7,10],[6,-1,4,-7,5,2,4,-1,6,4,-7,-6,-7,-9]]], dtype = "uint64")#candidate|3960|(7, 5, 14)|const|uint64
bop_3961 = relay.greater_equal(call_3939.astype('bool'), relay.reshape(const_3960.astype('bool'), relay.shape_of(call_3939))) # shape=(7, 5, 14)
bop_3964 = relay.greater_equal(call_3940.astype('bool'), relay.reshape(const_3960.astype('bool'), relay.shape_of(call_3940))) # shape=(7, 5, 14)
func_2050_call = mod.get_global_var('func_2050')
func_2053_call = mutated_mod.get_global_var('func_2053')
var_3985 = relay.var("var_3985", dtype = "int8", shape = (720,))#candidate|3985|(720,)|var|int8
call_3984 = relay.TupleGetItem(func_2050_call(relay.reshape(var_3985.astype('int8'), [9, 8, 10]), relay.reshape(var_3985.astype('int8'), [9, 8, 10]), ), 1)
call_3986 = relay.TupleGetItem(func_2053_call(relay.reshape(var_3985.astype('int8'), [9, 8, 10]), relay.reshape(var_3985.astype('int8'), [9, 8, 10]), ), 1)
uop_4002 = relay.sigmoid(bop_3961.astype('float64')) # shape=(7, 5, 14)
uop_4004 = relay.sigmoid(bop_3964.astype('float64')) # shape=(7, 5, 14)
output = relay.Tuple([call_3984,var_3985,uop_4002,])
output2 = relay.Tuple([call_3986,var_3985,uop_4004,])
func_4010 = relay.Function([var_3985,], output)
mod['func_4010'] = func_4010
mod = relay.transform.InferType()(mod)
mutated_mod['func_4010'] = func_4010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4011 = relay.var("var_4011", dtype = "int8", shape = (720,))#candidate|4011|(720,)|var|int8
func_4010_call = mutated_mod.get_global_var('func_4010')
call_4012 = func_4010_call(var_4011)
output = call_4012
func_4013 = relay.Function([var_4011], output)
mutated_mod['func_4013'] = func_4013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_575_call = mod.get_global_var('func_575')
func_577_call = mutated_mod.get_global_var('func_577')
call_4015 = relay.TupleGetItem(func_575_call(), 1)
call_4016 = relay.TupleGetItem(func_577_call(), 1)
output = relay.Tuple([call_4015,])
output2 = relay.Tuple([call_4016,])
func_4020 = relay.Function([], output)
mod['func_4020'] = func_4020
mod = relay.transform.InferType()(mod)
output = func_4020()
func_4021 = relay.Function([], output)
mutated_mod['func_4021'] = func_4021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4020_call = mod.get_global_var('func_4020')
func_4021_call = mutated_mod.get_global_var('func_4021')
call_4029 = relay.TupleGetItem(func_4020_call(), 0)
call_4030 = relay.TupleGetItem(func_4021_call(), 0)
func_2566_call = mod.get_global_var('func_2566')
func_2568_call = mutated_mod.get_global_var('func_2568')
const_4035 = relay.const([[6.523358,-5.424727,-8.943674,2.753666,7.038242,-3.730172,6.180740,-9.165073,-9.465738,0.922098,-9.437977,-2.969405,3.157805,4.055960,-4.922248],[-8.287948,2.097671,-2.585128,2.749817,-1.989777,2.311441,-3.560641,3.090532,5.092324,-5.672443,8.692862,-0.451947,-7.577208,9.235388,5.111113],[4.494545,7.227863,-4.121628,-5.193488,-6.870123,-0.877541,9.760822,-1.761965,1.598711,9.748692,-3.155219,-6.141048,-6.685320,6.669095,-6.488288],[-6.433209,-1.807695,-7.737707,9.096534,-8.332752,-4.605311,5.015838,-0.421072,-4.008427,-7.799019,9.754436,-6.688595,8.268688,-7.701372,6.526224],[7.232572,-6.087750,8.366148,-7.419744,8.006803,-7.594611,2.805874,-7.962000,9.511519,-5.273797,-1.201655,2.367710,6.400862,7.416654,0.970150],[4.690526,-8.161856,-8.733217,-3.600846,4.471725,3.395185,2.284987,9.829313,-5.193718,4.563492,-7.814780,-8.255420,-9.280450,-6.252902,3.775803],[-6.789048,-2.464577,-0.804388,8.809207,4.341469,5.926502,-5.166913,-1.356220,-0.495079,0.512635,9.958861,3.098689,3.928047,2.527215,2.143926],[7.683270,0.996935,4.808922,-2.079884,2.067992,8.512503,-4.588746,2.801079,6.827421,-8.810696,9.294475,5.771648,7.503231,9.890530,-9.805412],[-0.146669,-5.077333,-6.125847,4.683712,-5.103469,-0.366312,5.355601,-5.319954,4.620883,-5.565005,-2.582026,4.313213,-9.696321,-8.003585,-0.964902],[0.180778,-9.172950,-0.141494,9.190724,2.544756,-7.507134,9.421266,-5.607177,9.555208,6.249565,6.660141,8.652268,4.978815,-2.342602,7.151573],[8.052996,1.615458,2.250372,-0.918507,8.261035,-9.512918,5.453785,-0.014444,5.311880,-5.496986,8.442082,-9.453141,-5.686160,1.734519,8.021528]], dtype = "float64")#candidate|4035|(11, 15)|const|float64
call_4034 = relay.TupleGetItem(func_2566_call(relay.reshape(const_4035.astype('float64'), [1, 165])), 2)
call_4036 = relay.TupleGetItem(func_2568_call(relay.reshape(const_4035.astype('float64'), [1, 165])), 2)
uop_4043 = relay.sin(call_4029.astype('float64')) # shape=(7, 5, 14)
uop_4045 = relay.sin(call_4030.astype('float64')) # shape=(7, 5, 14)
output = relay.Tuple([call_4034,const_4035,uop_4043,])
output2 = relay.Tuple([call_4036,const_4035,uop_4045,])
func_4056 = relay.Function([], output)
mod['func_4056'] = func_4056
mod = relay.transform.InferType()(mod)
mutated_mod['func_4056'] = func_4056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4056_call = mutated_mod.get_global_var('func_4056')
call_4057 = func_4056_call()
output = call_4057
func_4058 = relay.Function([], output)
mutated_mod['func_4058'] = func_4058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_4065 = relay.TupleGetItem(func_1820_call(), 0)
call_4066 = relay.TupleGetItem(func_1822_call(), 0)
func_2388_call = mod.get_global_var('func_2388')
func_2391_call = mutated_mod.get_global_var('func_2391')
var_4075 = relay.var("var_4075", dtype = "float32", shape = (2, 420))#candidate|4075|(2, 420)|var|float32
call_4074 = relay.TupleGetItem(func_2388_call(relay.reshape(var_4075.astype('float32'), [12, 10, 7]), relay.reshape(var_4075.astype('float32'), [12, 10, 7]), ), 0)
call_4076 = relay.TupleGetItem(func_2391_call(relay.reshape(var_4075.astype('float32'), [12, 10, 7]), relay.reshape(var_4075.astype('float32'), [12, 10, 7]), ), 0)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_4077 = func_595_call()
call_4078 = func_595_call()
var_4091 = relay.var("var_4091", dtype = "float32", shape = (12, 10, 7))#candidate|4091|(12, 10, 7)|var|float32
bop_4092 = relay.floor_mod(call_4074.astype('float64'), relay.reshape(var_4091.astype('float64'), relay.shape_of(call_4074))) # shape=(12, 10, 7)
bop_4095 = relay.floor_mod(call_4076.astype('float64'), relay.reshape(var_4091.astype('float64'), relay.shape_of(call_4076))) # shape=(12, 10, 7)
output = relay.Tuple([call_4065,var_4075,call_4077,bop_4092,])
output2 = relay.Tuple([call_4066,var_4075,call_4078,bop_4095,])
func_4104 = relay.Function([var_4075,var_4091,], output)
mod['func_4104'] = func_4104
mod = relay.transform.InferType()(mod)
var_4105 = relay.var("var_4105", dtype = "float32", shape = (2, 420))#candidate|4105|(2, 420)|var|float32
var_4106 = relay.var("var_4106", dtype = "float32", shape = (12, 10, 7))#candidate|4106|(12, 10, 7)|var|float32
output = func_4104(var_4105,var_4106,)
func_4107 = relay.Function([var_4105,var_4106,], output)
mutated_mod['func_4107'] = func_4107
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4109 = relay.var("var_4109", dtype = "float64", shape = (16, 6, 11))#candidate|4109|(16, 6, 11)|var|float64
uop_4110 = relay.cosh(var_4109.astype('float64')) # shape=(16, 6, 11)
func_3394_call = mod.get_global_var('func_3394')
func_3398_call = mutated_mod.get_global_var('func_3398')
var_4115 = relay.var("var_4115", dtype = "int16", shape = (10,))#candidate|4115|(10,)|var|int16
const_4116 = relay.const([[-6],[10],[-5],[-8],[10],[-10],[6],[-3],[-1],[3],[-9],[7],[-9],[6],[6],[1],[-8],[3],[-2],[10]], dtype = "int16")#candidate|4116|(20, 1)|const|int16
call_4114 = func_3394_call(relay.reshape(var_4115.astype('int16'), [2, 5, 1]), relay.reshape(const_4116.astype('int16'), [2, 5, 2]), )
call_4117 = func_3394_call(relay.reshape(var_4115.astype('int16'), [2, 5, 1]), relay.reshape(const_4116.astype('int16'), [2, 5, 2]), )
func_3440_call = mod.get_global_var('func_3440')
func_3441_call = mutated_mod.get_global_var('func_3441')
call_4130 = func_3440_call()
call_4131 = func_3440_call()
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_4132 = func_500_call()
call_4133 = func_500_call()
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
var_4139 = relay.var("var_4139", dtype = "uint32", shape = (35, 6))#candidate|4139|(35, 6)|var|uint32
call_4138 = func_168_call(relay.reshape(var_4139.astype('uint32'), [6, 5, 7]))
call_4140 = func_168_call(relay.reshape(var_4139.astype('uint32'), [6, 5, 7]))
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_4142 = func_194_call()
call_4143 = func_194_call()
func_2566_call = mod.get_global_var('func_2566')
func_2568_call = mutated_mod.get_global_var('func_2568')
var_4154 = relay.var("var_4154", dtype = "float64", shape = (33, 5))#candidate|4154|(33, 5)|var|float64
call_4153 = relay.TupleGetItem(func_2566_call(relay.reshape(var_4154.astype('float64'), [1, 165])), 2)
call_4155 = relay.TupleGetItem(func_2568_call(relay.reshape(var_4154.astype('float64'), [1, 165])), 2)
func_685_call = mod.get_global_var('func_685')
func_687_call = mutated_mod.get_global_var('func_687')
call_4156 = func_685_call()
call_4157 = func_685_call()
bop_4158 = relay.logical_or(call_4153.astype('bool'), relay.reshape(call_4156.astype('bool'), relay.shape_of(call_4153))) # shape=(7, 5, 14)
bop_4161 = relay.logical_or(call_4155.astype('bool'), relay.reshape(call_4157.astype('bool'), relay.shape_of(call_4155))) # shape=(7, 5, 14)
uop_4167 = relay.exp(uop_4110.astype('float64')) # shape=(16, 6, 11)
bop_4179 = relay.add(uop_4167.astype('uint64'), relay.reshape(uop_4110.astype('uint64'), relay.shape_of(uop_4167))) # shape=(16, 6, 11)
func_279_call = mod.get_global_var('func_279')
func_283_call = mutated_mod.get_global_var('func_283')
call_4189 = relay.TupleGetItem(func_279_call(relay.reshape(var_4154.astype('float64'), [3, 5, 11]), relay.reshape(var_4139.astype('uint32'), [210,]), ), 0)
call_4190 = relay.TupleGetItem(func_283_call(relay.reshape(var_4154.astype('float64'), [3, 5, 11]), relay.reshape(var_4139.astype('uint32'), [210,]), ), 0)
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_4192 = func_500_call()
call_4193 = func_500_call()
bop_4196 = relay.maximum(uop_4110.astype('float32'), relay.reshape(var_4109.astype('float32'), relay.shape_of(uop_4110))) # shape=(16, 6, 11)
bop_4199 = relay.floor_divide(uop_4167.astype('float32'), relay.reshape(uop_4110.astype('float32'), relay.shape_of(uop_4167))) # shape=(16, 6, 11)
func_2661_call = mod.get_global_var('func_2661')
func_2662_call = mutated_mod.get_global_var('func_2662')
call_4203 = relay.TupleGetItem(func_2661_call(), 0)
call_4204 = relay.TupleGetItem(func_2662_call(), 0)
bop_4210 = relay.bitwise_xor(bop_4199.astype('uint8'), relay.reshape(bop_4179.astype('uint8'), relay.shape_of(bop_4199))) # shape=(16, 6, 11)
output = relay.Tuple([call_4114,var_4115,const_4116,call_4130,call_4132,call_4138,var_4139,call_4142,var_4154,bop_4158,call_4189,call_4192,bop_4196,call_4203,bop_4210,])
output2 = relay.Tuple([call_4117,var_4115,const_4116,call_4131,call_4133,call_4140,var_4139,call_4143,var_4154,bop_4161,call_4190,call_4193,bop_4196,call_4204,bop_4210,])
func_4216 = relay.Function([var_4109,var_4115,var_4139,var_4154,], output)
mod['func_4216'] = func_4216
mod = relay.transform.InferType()(mod)
mutated_mod['func_4216'] = func_4216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4216_call = mutated_mod.get_global_var('func_4216')
var_4218 = relay.var("var_4218", dtype = "float64", shape = (16, 6, 11))#candidate|4218|(16, 6, 11)|var|float64
var_4219 = relay.var("var_4219", dtype = "int16", shape = (10,))#candidate|4219|(10,)|var|int16
var_4220 = relay.var("var_4220", dtype = "uint32", shape = (35, 6))#candidate|4220|(35, 6)|var|uint32
var_4221 = relay.var("var_4221", dtype = "float64", shape = (33, 5))#candidate|4221|(33, 5)|var|float64
call_4217 = func_4216_call(var_4218,var_4219,var_4220,var_4221,)
output = call_4217
func_4222 = relay.Function([var_4218,var_4219,var_4220,var_4221,], output)
mutated_mod['func_4222'] = func_4222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
call_4315 = relay.TupleGetItem(func_2999_call(), 1)
call_4316 = relay.TupleGetItem(func_3001_call(), 1)
uop_4354 = relay.acosh(call_4315.astype('float64')) # shape=(7, 5, 14)
uop_4356 = relay.acosh(call_4316.astype('float64')) # shape=(7, 5, 14)
output = uop_4354
output2 = uop_4356
func_4376 = relay.Function([], output)
mod['func_4376'] = func_4376
mod = relay.transform.InferType()(mod)
mutated_mod['func_4376'] = func_4376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4376_call = mutated_mod.get_global_var('func_4376')
call_4377 = func_4376_call()
output = call_4377
func_4378 = relay.Function([], output)
mutated_mod['func_4378'] = func_4378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3150_call = mod.get_global_var('func_3150')
func_3152_call = mutated_mod.get_global_var('func_3152')
call_4379 = relay.TupleGetItem(func_3150_call(), 0)
call_4380 = relay.TupleGetItem(func_3152_call(), 0)
output = relay.Tuple([call_4379,])
output2 = relay.Tuple([call_4380,])
func_4383 = relay.Function([], output)
mod['func_4383'] = func_4383
mod = relay.transform.InferType()(mod)
mutated_mod['func_4383'] = func_4383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4383_call = mutated_mod.get_global_var('func_4383')
call_4384 = func_4383_call()
output = call_4384
func_4385 = relay.Function([], output)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4056_call = mod.get_global_var('func_4056')
func_4058_call = mutated_mod.get_global_var('func_4058')
call_4488 = relay.TupleGetItem(func_4056_call(), 2)
call_4489 = relay.TupleGetItem(func_4058_call(), 2)
output = relay.Tuple([call_4488,])
output2 = relay.Tuple([call_4489,])
func_4496 = relay.Function([], output)
mod['func_4496'] = func_4496
mod = relay.transform.InferType()(mod)
mutated_mod['func_4496'] = func_4496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4496_call = mutated_mod.get_global_var('func_4496')
call_4497 = func_4496_call()
output = call_4497
func_4498 = relay.Function([], output)
mutated_mod['func_4498'] = func_4498
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4514 = relay.const([[[-1,2,-5],[6,1,-9],[-1,-5,5],[-4,9,-9],[5,-5,7],[5,-9,9],[6,-5,7],[8,-3,10]],[[1,2,-7],[-8,-7,3],[9,3,7],[-1,7,9],[-9,3,-4],[-2,4,4],[5,8,-6],[-7,1,2]],[[-1,-10,-8],[2,10,3],[-8,-8,9],[6,3,-9],[4,-6,5],[4,3,-2],[-5,-2,10],[10,8,-10]],[[9,4,-9],[2,6,-2],[-10,-7,-10],[-5,3,-3],[-1,-9,-8],[-10,7,10],[-5,-1,2],[4,-10,4]],[[7,-9,7],[5,3,-8],[5,10,2],[-7,-4,-9],[-2,10,-3],[-3,4,-3],[4,-10,2],[-9,-8,6]],[[-1,-8,-1],[-1,10,-6],[8,5,3],[-2,6,1],[-1,-4,9],[8,4,5],[3,-10,-9],[-5,-8,-8]],[[8,6,-3],[-1,-9,-3],[4,-10,-7],[6,3,2],[4,9,-10],[5,-9,2],[-9,-6,8],[9,-1,4]],[[4,-8,6],[8,-1,-4],[-6,-9,-9],[6,-5,-6],[-2,-9,-6],[2,1,-8],[2,-6,5],[-4,-8,-5]],[[-5,5,-3],[-5,8,9],[4,-5,-1],[-1,8,-6],[9,3,2],[-4,-1,6],[-2,3,2],[-3,3,-1]],[[-10,9,-2],[-1,4,8],[-6,-2,-3],[-2,-9,2],[-7,8,-4],[6,3,-2],[-2,-8,10],[2,-10,2]],[[-1,8,-7],[1,-7,4],[2,-7,-9],[2,3,6],[5,9,10],[-1,-4,-3],[9,-7,-7],[-10,-2,3]],[[-8,-3,-4],[6,6,-7],[9,-9,6],[5,10,-2],[4,-5,2],[8,-5,-3],[-9,-10,-6],[-3,-4,-9]]], dtype = "int16")#candidate|4514|(12, 8, 3)|const|int16
var_4515 = relay.var("var_4515", dtype = "int16", shape = (12, 8, 3))#candidate|4515|(12, 8, 3)|var|int16
bop_4516 = relay.equal(const_4514.astype('bool'), relay.reshape(var_4515.astype('bool'), relay.shape_of(const_4514))) # shape=(12, 8, 3)
output = relay.Tuple([bop_4516,])
output2 = relay.Tuple([bop_4516,])
func_4520 = relay.Function([var_4515,], output)
mod['func_4520'] = func_4520
mod = relay.transform.InferType()(mod)
mutated_mod['func_4520'] = func_4520
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4521 = relay.var("var_4521", dtype = "int16", shape = (12, 8, 3))#candidate|4521|(12, 8, 3)|var|int16
func_4520_call = mutated_mod.get_global_var('func_4520')
call_4522 = func_4520_call(var_4521)
output = call_4522
func_4523 = relay.Function([var_4521], output)
mutated_mod['func_4523'] = func_4523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2427_call = mod.get_global_var('func_2427')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_4555 = relay.TupleGetItem(func_2427_call(), 3)
call_4556 = relay.TupleGetItem(func_2429_call(), 3)
func_2836_call = mod.get_global_var('func_2836')
func_2837_call = mutated_mod.get_global_var('func_2837')
call_4564 = relay.TupleGetItem(func_2836_call(), 2)
call_4565 = relay.TupleGetItem(func_2837_call(), 2)
uop_4574 = relay.atanh(call_4555.astype('float32')) # shape=(7, 11, 2)
uop_4576 = relay.atanh(call_4556.astype('float32')) # shape=(7, 11, 2)
output = relay.Tuple([call_4564,uop_4574,])
output2 = relay.Tuple([call_4565,uop_4576,])
func_4604 = relay.Function([], output)
mod['func_4604'] = func_4604
mod = relay.transform.InferType()(mod)
mutated_mod['func_4604'] = func_4604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mutated_mod.get_global_var('func_4604')
call_4605 = func_4604_call()
output = call_4605
func_4606 = relay.Function([], output)
mutated_mod['func_4606'] = func_4606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1193_call = mod.get_global_var('func_1193')
func_1195_call = mutated_mod.get_global_var('func_1195')
call_4621 = relay.TupleGetItem(func_1193_call(), 2)
call_4622 = relay.TupleGetItem(func_1195_call(), 2)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_4630 = relay.TupleGetItem(func_1205_call(), 0)
call_4631 = relay.TupleGetItem(func_1206_call(), 0)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_4641 = relay.TupleGetItem(func_1205_call(), 0)
call_4642 = relay.TupleGetItem(func_1206_call(), 0)
output = relay.Tuple([call_4621,call_4630,call_4641,])
output2 = relay.Tuple([call_4622,call_4631,call_4642,])
func_4651 = relay.Function([], output)
mod['func_4651'] = func_4651
mod = relay.transform.InferType()(mod)
output = func_4651()
func_4652 = relay.Function([], output)
mutated_mod['func_4652'] = func_4652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_4656 = relay.TupleGetItem(func_1820_call(), 0)
call_4657 = relay.TupleGetItem(func_1822_call(), 0)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_4675 = relay.TupleGetItem(func_1994_call(), 0)
call_4676 = relay.TupleGetItem(func_1996_call(), 0)
func_2661_call = mod.get_global_var('func_2661')
func_2662_call = mutated_mod.get_global_var('func_2662')
call_4677 = relay.TupleGetItem(func_2661_call(), 1)
call_4678 = relay.TupleGetItem(func_2662_call(), 1)
output = relay.Tuple([call_4656,call_4675,call_4677,])
output2 = relay.Tuple([call_4657,call_4676,call_4678,])
func_4680 = relay.Function([], output)
mod['func_4680'] = func_4680
mod = relay.transform.InferType()(mod)
mutated_mod['func_4680'] = func_4680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4680_call = mutated_mod.get_global_var('func_4680')
call_4681 = func_4680_call()
output = call_4681
func_4682 = relay.Function([], output)
mutated_mod['func_4682'] = func_4682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3637_call = mod.get_global_var('func_3637')
func_3638_call = mutated_mod.get_global_var('func_3638')
call_4710 = func_3637_call()
call_4711 = func_3637_call()
output = relay.Tuple([call_4710,])
output2 = relay.Tuple([call_4711,])
func_4713 = relay.Function([], output)
mod['func_4713'] = func_4713
mod = relay.transform.InferType()(mod)
output = func_4713()
func_4714 = relay.Function([], output)
mutated_mod['func_4714'] = func_4714
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4723 = relay.var("var_4723", dtype = "int8", shape = (11, 1, 8))#candidate|4723|(11, 1, 8)|var|int8
var_4724 = relay.var("var_4724", dtype = "int8", shape = (11, 1, 8))#candidate|4724|(11, 1, 8)|var|int8
bop_4725 = relay.maximum(var_4723.astype('int8'), relay.reshape(var_4724.astype('int8'), relay.shape_of(var_4723))) # shape=(11, 1, 8)
const_4737 = relay.const([[[1,5,-8,5,1,8,-9,-2],[9,-5,4,-7,2,1,1,-3],[4,10,-2,6,5,5,-7,2],[-4,6,-5,-10,5,10,-5,-10],[-3,-1,-7,8,2,-6,2,-6],[5,6,-5,8,10,-7,10,-6],[-10,-8,5,-9,-1,6,6,-2]],[[2,-2,6,6,-7,5,-10,10],[7,7,6,-6,2,2,4,1],[-4,2,3,10,-10,-9,5,2],[-9,-1,-4,4,1,-6,-2,10],[9,7,-1,-4,-1,3,6,7],[4,-2,7,8,2,2,2,9],[7,3,-5,10,4,4,-1,-5]],[[9,5,3,-3,-7,10,-8,-1],[7,2,5,-7,-7,6,2,-1],[1,4,-9,-1,-1,-6,-2,-3],[-2,-10,-8,3,8,1,3,8],[10,-9,8,-5,-3,-9,9,3],[-8,8,9,-1,-3,8,6,1],[9,-5,2,-7,5,9,5,-5]],[[4,-9,5,10,2,-3,6,-4],[-5,-2,-3,3,3,1,-3,-3],[8,-10,3,10,-1,-4,10,-10],[9,4,-10,-7,9,3,4,1],[-7,6,4,-5,-10,10,7,5],[-1,-5,5,4,-1,8,-2,-9],[1,-10,3,9,-4,-3,8,-6]],[[-10,4,4,9,-4,3,5,8],[9,-10,3,8,-8,-8,-3,-7],[-5,6,8,9,4,1,-7,-5],[7,1,-5,-7,9,9,-2,-5],[-7,10,-8,-1,-10,4,-9,4],[-4,-6,-3,2,-10,6,-7,-9],[-3,4,-8,6,5,-7,-8,-10]],[[7,3,-9,-4,8,-1,10,-1],[-8,6,10,-6,-3,9,4,-8],[-5,9,-8,5,4,10,5,-8],[-8,1,-8,3,7,-5,-3,-10],[-3,-4,-3,-6,-4,-2,2,4],[-4,-10,-1,4,-6,9,-1,10],[9,7,-5,-10,3,-10,9,5]],[[-8,-8,9,-8,-2,-4,5,8],[-8,-9,-10,-3,-8,6,-6,5],[-7,4,-6,10,-7,-4,8,10],[7,-8,6,-7,-4,-6,-7,4],[-5,-9,9,10,4,2,-5,8],[10,10,9,2,2,4,8,-5],[-6,-3,-6,3,-6,1,-7,-5]],[[7,3,-3,-7,-3,-4,9,-4],[-4,10,-2,9,9,-9,-9,3],[10,-1,-3,7,1,8,3,-5],[-3,-6,-9,2,6,-4,8,2],[7,8,-2,-7,8,-3,9,7],[-2,-6,-9,10,-10,2,-4,-3],[-8,3,7,4,-5,-6,4,8]],[[-8,8,-3,-5,-5,-10,-3,-1],[7,10,-2,-1,1,5,1,-3],[10,-8,-2,-7,-2,-5,1,4],[8,3,-8,10,10,-5,1,-9],[9,-3,10,7,6,-5,-6,6],[-4,-5,-3,-10,-8,-5,-2,9],[2,4,3,-4,-3,-9,-9,-4]],[[-4,-3,-2,2,-9,1,9,-5],[-4,-5,-2,8,-9,6,-2,10],[7,-4,8,1,1,9,1,-3],[2,-4,8,-10,8,4,4,7],[7,2,-7,3,4,10,-5,-2],[2,1,-7,4,7,-7,-1,-4],[-6,-6,-9,3,-10,-9,-7,-3]],[[-9,8,7,3,-1,5,-5,-2],[5,-3,6,8,-8,-2,9,3],[-2,-4,-4,-3,7,7,-6,2],[5,-4,3,9,-10,-6,8,7],[-2,-1,9,-1,1,-8,-7,6],[6,-4,-3,-10,-4,2,-8,2],[-1,6,6,-6,-5,1,3,-5]]], dtype = "int8")#candidate|4737|(11, 7, 8)|const|int8
bop_4738 = relay.subtract(bop_4725.astype('uint32'), const_4737.astype('uint32')) # shape=(11, 7, 8)
output = relay.Tuple([bop_4738,])
output2 = relay.Tuple([bop_4738,])
func_4757 = relay.Function([var_4723,var_4724,], output)
mod['func_4757'] = func_4757
mod = relay.transform.InferType()(mod)
var_4758 = relay.var("var_4758", dtype = "int8", shape = (11, 1, 8))#candidate|4758|(11, 1, 8)|var|int8
var_4759 = relay.var("var_4759", dtype = "int8", shape = (11, 1, 8))#candidate|4759|(11, 1, 8)|var|int8
output = func_4757(var_4758,var_4759,)
func_4760 = relay.Function([var_4758,var_4759,], output)
mutated_mod['func_4760'] = func_4760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_4816 = func_595_call()
call_4817 = func_595_call()
func_681_call = mod.get_global_var('func_681')
func_682_call = mutated_mod.get_global_var('func_682')
call_4818 = relay.TupleGetItem(func_681_call(), 0)
call_4819 = relay.TupleGetItem(func_682_call(), 0)
output = relay.Tuple([call_4816,call_4818,])
output2 = relay.Tuple([call_4817,call_4819,])
func_4821 = relay.Function([], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
mutated_mod['func_4821'] = func_4821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mutated_mod.get_global_var('func_4821')
call_4822 = func_4821_call()
output = call_4822
func_4823 = relay.Function([], output)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_4824 = relay.TupleGetItem(func_4821_call(), 1)
call_4825 = relay.TupleGetItem(func_4823_call(), 1)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_4872 = relay.TupleGetItem(func_3236_call(), 0)
call_4873 = relay.TupleGetItem(func_3238_call(), 0)
output = relay.Tuple([call_4824,call_4872,])
output2 = relay.Tuple([call_4825,call_4873,])
func_4880 = relay.Function([], output)
mod['func_4880'] = func_4880
mod = relay.transform.InferType()(mod)
output = func_4880()
func_4881 = relay.Function([], output)
mutated_mod['func_4881'] = func_4881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_919_call = mod.get_global_var('func_919')
func_920_call = mutated_mod.get_global_var('func_920')
call_4940 = relay.TupleGetItem(func_919_call(), 0)
call_4941 = relay.TupleGetItem(func_920_call(), 0)
func_340_call = mod.get_global_var('func_340')
func_343_call = mutated_mod.get_global_var('func_343')
var_4944 = relay.var("var_4944", dtype = "uint32", shape = (210,))#candidate|4944|(210,)|var|uint32
call_4943 = relay.TupleGetItem(func_340_call(relay.reshape(var_4944.astype('uint32'), [210,])), 2)
call_4945 = relay.TupleGetItem(func_343_call(relay.reshape(var_4944.astype('uint32'), [210,])), 2)
output = relay.Tuple([call_4940,call_4943,var_4944,])
output2 = relay.Tuple([call_4941,call_4945,var_4944,])
func_4947 = relay.Function([var_4944,], output)
mod['func_4947'] = func_4947
mod = relay.transform.InferType()(mod)
mutated_mod['func_4947'] = func_4947
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4948 = relay.var("var_4948", dtype = "uint32", shape = (210,))#candidate|4948|(210,)|var|uint32
func_4947_call = mutated_mod.get_global_var('func_4947')
call_4949 = func_4947_call(var_4948)
output = call_4949
func_4950 = relay.Function([var_4948], output)
mutated_mod['func_4950'] = func_4950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_194_call = mod.get_global_var('func_194')
func_195_call = mutated_mod.get_global_var('func_195')
call_4958 = func_194_call()
call_4959 = func_194_call()
func_340_call = mod.get_global_var('func_340')
func_343_call = mutated_mod.get_global_var('func_343')
const_4961 = relay.const([6,-9,-6,1,4,-9,1,9,10,7,2,4,2,6,-9,-10,-1,-9,9,-6,-5,3,10,-6,-4,8,6,3,5,6,4,-1,3,5,-8,-9,5,9,-6,6,7,-7,9,2,9,7,4,-10,8,10,-4,10,-3,-5,-3,10,-8,-4,-6,10,-4,1,-7,-6,-6,-2,5,10,-1,6,7,-6,4,-9,-6,-10,-7,10,-1,8,5,8,10,-8,4,-4,2,5,10,8,4,-10,-8,5,-9,7,-1,-3,-4,3,-7,-8,-9,-6,-8,8,-4,-2,-9,4,-8,-1,7,-3,7,8,6,-4,10,5,8,-9,-2,-7,-6,10,-1,6,-6,-8,6,6,1,-7,2,8,-7,-4,-5,-9,-9,6,9,7,-2,8,-10,-10,-6,3,-2,10,7,-6,5,5,4,6,-5,9,-10,7,-3,3,7,9,-7,9,-3,6,2,-3,-5,10,-4,1,-7,-5,5,-8,-4,-2,-6,-4,-7,8,-4,-8,2,2,8,-1,2,-3,-2,1,-10,6,3,-4,2,2,4,8,-7,-3,4,7,-10,2], dtype = "uint32")#candidate|4961|(210,)|const|uint32
call_4960 = relay.TupleGetItem(func_340_call(relay.reshape(const_4961.astype('uint32'), [210,])), 2)
call_4962 = relay.TupleGetItem(func_343_call(relay.reshape(const_4961.astype('uint32'), [210,])), 2)
output = relay.Tuple([call_4958,call_4960,const_4961,])
output2 = relay.Tuple([call_4959,call_4962,const_4961,])
func_4963 = relay.Function([], output)
mod['func_4963'] = func_4963
mod = relay.transform.InferType()(mod)
mutated_mod['func_4963'] = func_4963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4963_call = mutated_mod.get_global_var('func_4963')
call_4964 = func_4963_call()
output = call_4964
func_4965 = relay.Function([], output)
mutated_mod['func_4965'] = func_4965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3717_call = mod.get_global_var('func_3717')
func_3719_call = mutated_mod.get_global_var('func_3719')
call_5095 = func_3717_call()
call_5096 = func_3717_call()
output = relay.Tuple([call_5095,])
output2 = relay.Tuple([call_5096,])
func_5116 = relay.Function([], output)
mod['func_5116'] = func_5116
mod = relay.transform.InferType()(mod)
output = func_5116()
func_5117 = relay.Function([], output)
mutated_mod['func_5117'] = func_5117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5121 = relay.var("var_5121", dtype = "int8", shape = (14, 16, 2))#candidate|5121|(14, 16, 2)|var|int8
const_5122 = relay.const([[[-8,-6],[-4,10],[-3,4],[-3,-10],[8,10],[6,-4],[-3,-7],[-3,-10],[10,8],[5,5],[6,-1],[8,-6],[3,-8],[-9,3],[-3,6],[-1,-6]],[[2,-6],[6,8],[3,-3],[-1,9],[4,4],[-10,-5],[7,-8],[8,9],[10,1],[-7,7],[8,-2],[10,-4],[9,-6],[-5,1],[-2,10],[4,4]],[[-5,1],[-1,3],[-10,-8],[-6,-3],[-10,-3],[1,5],[-4,-5],[-4,-2],[1,-10],[-2,4],[10,2],[-4,-1],[5,-9],[10,10],[-9,-2],[-4,-2]],[[8,9],[-5,-3],[7,-10],[-2,5],[-7,-6],[8,-8],[-2,8],[5,-3],[1,4],[-7,2],[-2,-4],[5,6],[4,6],[-9,-7],[-7,9],[6,-6]],[[5,5],[-6,-3],[3,-5],[-7,-10],[-2,-2],[-3,1],[5,-3],[-1,-10],[-6,6],[3,-2],[-9,5],[-7,-6],[1,9],[-9,5],[10,5],[-6,8]],[[9,6],[7,8],[-3,1],[-6,-1],[7,3],[10,-9],[8,4],[8,-6],[7,-1],[-9,2],[2,4],[-2,-6],[-6,-6],[7,-9],[-1,8],[6,-8]],[[-5,-9],[8,8],[7,-9],[-8,-10],[4,-1],[3,-7],[-4,6],[9,4],[5,-10],[-7,4],[-2,-2],[7,-3],[10,-3],[3,-1],[-7,6],[3,1]],[[3,10],[4,3],[6,-4],[-9,-6],[-10,-4],[-1,9],[-2,-3],[5,2],[9,-10],[-7,-7],[-10,5],[-10,8],[10,-3],[9,-8],[-7,5],[-6,1]],[[-10,-8],[-6,9],[10,5],[7,-9],[7,9],[-6,-6],[-1,-6],[-1,-4],[-10,9],[9,-1],[-4,-8],[2,-9],[1,-5],[-8,-3],[-4,-5],[8,6]],[[-2,-5],[5,-2],[4,1],[9,-7],[9,-9],[-4,7],[3,-3],[-1,-10],[-5,6],[1,-8],[-7,-5],[8,-9],[3,-5],[2,5],[4,-6],[-10,-10]],[[1,5],[-3,9],[2,8],[-5,7],[7,-4],[-6,2],[-10,6],[5,5],[1,10],[-2,8],[4,-4],[-5,6],[6,10],[-3,-1],[3,3],[5,-5]],[[-9,-4],[5,-7],[-10,-7],[-3,-8],[7,1],[10,-4],[-1,-10],[6,-3],[-10,6],[-9,-4],[3,7],[-6,-4],[-2,-2],[-7,5],[3,4],[-3,-4]],[[6,-8],[-4,-5],[4,4],[-6,5],[-3,10],[3,-8],[1,8],[9,-6],[-4,1],[7,-7],[-7,-2],[-9,-8],[-4,-10],[4,-5],[-10,-8],[7,-5]],[[10,-10],[-1,9],[6,-10],[10,7],[8,3],[7,-8],[3,7],[2,10],[7,9],[7,-5],[-1,9],[-5,-5],[6,-5],[-4,-2],[-1,-8],[1,4]]], dtype = "int8")#candidate|5122|(14, 16, 2)|const|int8
bop_5123 = relay.less(var_5121.astype('bool'), relay.reshape(const_5122.astype('bool'), relay.shape_of(var_5121))) # shape=(14, 16, 2)
bop_5129 = relay.logical_or(var_5121.astype('bool'), relay.reshape(const_5122.astype('bool'), relay.shape_of(var_5121))) # shape=(14, 16, 2)
func_1398_call = mod.get_global_var('func_1398')
func_1401_call = mutated_mod.get_global_var('func_1401')
var_5136 = relay.var("var_5136", dtype = "uint32", shape = ())#candidate|5136|()|var|uint32
call_5135 = relay.TupleGetItem(func_1398_call(relay.reshape(var_5136.astype('uint32'), [])), 1)
call_5137 = relay.TupleGetItem(func_1401_call(relay.reshape(var_5136.astype('uint32'), [])), 1)
func_4020_call = mod.get_global_var('func_4020')
func_4021_call = mutated_mod.get_global_var('func_4021')
call_5144 = relay.TupleGetItem(func_4020_call(), 0)
call_5145 = relay.TupleGetItem(func_4021_call(), 0)
output = relay.Tuple([bop_5123,bop_5129,call_5135,var_5136,call_5144,])
output2 = relay.Tuple([bop_5123,bop_5129,call_5137,var_5136,call_5145,])
func_5150 = relay.Function([var_5121,var_5136,], output)
mod['func_5150'] = func_5150
mod = relay.transform.InferType()(mod)
mutated_mod['func_5150'] = func_5150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5150_call = mutated_mod.get_global_var('func_5150')
var_5152 = relay.var("var_5152", dtype = "int8", shape = (14, 16, 2))#candidate|5152|(14, 16, 2)|var|int8
var_5153 = relay.var("var_5153", dtype = "uint32", shape = ())#candidate|5153|()|var|uint32
call_5151 = func_5150_call(var_5152,var_5153,)
output = call_5151
func_5154 = relay.Function([var_5152,var_5153,], output)
mutated_mod['func_5154'] = func_5154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_5187 = func_595_call()
call_5188 = func_595_call()
var_5192 = relay.var("var_5192", dtype = "uint64", shape = (7, 5, 14))#candidate|5192|(7, 5, 14)|var|uint64
bop_5193 = relay.multiply(call_5187.astype('uint16'), relay.reshape(var_5192.astype('uint16'), relay.shape_of(call_5187))) # shape=(7, 5, 14)
bop_5196 = relay.multiply(call_5188.astype('uint16'), relay.reshape(var_5192.astype('uint16'), relay.shape_of(call_5188))) # shape=(7, 5, 14)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_5200 = relay.TupleGetItem(func_1820_call(), 0)
call_5201 = relay.TupleGetItem(func_1822_call(), 0)
output = relay.Tuple([bop_5193,call_5200,])
output2 = relay.Tuple([bop_5196,call_5201,])
func_5203 = relay.Function([var_5192,], output)
mod['func_5203'] = func_5203
mod = relay.transform.InferType()(mod)
mutated_mod['func_5203'] = func_5203
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5204 = relay.var("var_5204", dtype = "uint64", shape = (7, 5, 14))#candidate|5204|(7, 5, 14)|var|uint64
func_5203_call = mutated_mod.get_global_var('func_5203')
call_5205 = func_5203_call(var_5204)
output = call_5205
func_5206 = relay.Function([var_5204], output)
mutated_mod['func_5206'] = func_5206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3717_call = mod.get_global_var('func_3717')
func_3719_call = mutated_mod.get_global_var('func_3719')
call_5246 = func_3717_call()
call_5247 = func_3717_call()
var_5275 = relay.var("var_5275", dtype = "uint64", shape = (7, 5, 14))#candidate|5275|(7, 5, 14)|var|uint64
bop_5276 = relay.bitwise_or(call_5246.astype('int64'), relay.reshape(var_5275.astype('int64'), relay.shape_of(call_5246))) # shape=(7, 5, 14)
bop_5279 = relay.bitwise_or(call_5247.astype('int64'), relay.reshape(var_5275.astype('int64'), relay.shape_of(call_5247))) # shape=(7, 5, 14)
func_1205_call = mod.get_global_var('func_1205')
func_1206_call = mutated_mod.get_global_var('func_1206')
call_5299 = relay.TupleGetItem(func_1205_call(), 0)
call_5300 = relay.TupleGetItem(func_1206_call(), 0)
func_3073_call = mod.get_global_var('func_3073')
func_3075_call = mutated_mod.get_global_var('func_3075')
call_5307 = relay.TupleGetItem(func_3073_call(), 0)
call_5308 = relay.TupleGetItem(func_3075_call(), 0)
output = relay.Tuple([bop_5276,call_5299,call_5307,])
output2 = relay.Tuple([bop_5279,call_5300,call_5308,])
func_5332 = relay.Function([var_5275,], output)
mod['func_5332'] = func_5332
mod = relay.transform.InferType()(mod)
mutated_mod['func_5332'] = func_5332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5333 = relay.var("var_5333", dtype = "uint64", shape = (7, 5, 14))#candidate|5333|(7, 5, 14)|var|uint64
func_5332_call = mutated_mod.get_global_var('func_5332')
call_5334 = func_5332_call(var_5333)
output = call_5334
func_5335 = relay.Function([var_5333], output)
mutated_mod['func_5335'] = func_5335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4020_call = mod.get_global_var('func_4020')
func_4021_call = mutated_mod.get_global_var('func_4021')
call_5337 = relay.TupleGetItem(func_4020_call(), 0)
call_5338 = relay.TupleGetItem(func_4021_call(), 0)
func_3361_call = mod.get_global_var('func_3361')
func_3364_call = mutated_mod.get_global_var('func_3364')
var_5352 = relay.var("var_5352", dtype = "uint16", shape = (25, 6))#candidate|5352|(25, 6)|var|uint16
call_5351 = relay.TupleGetItem(func_3361_call(relay.reshape(var_5352.astype('uint16'), [5, 6, 5]), relay.reshape(var_5352.astype('int64'), [5, 6, 5]), ), 1)
call_5353 = relay.TupleGetItem(func_3364_call(relay.reshape(var_5352.astype('uint16'), [5, 6, 5]), relay.reshape(var_5352.astype('int64'), [5, 6, 5]), ), 1)
func_3150_call = mod.get_global_var('func_3150')
func_3152_call = mutated_mod.get_global_var('func_3152')
call_5355 = relay.TupleGetItem(func_3150_call(), 0)
call_5356 = relay.TupleGetItem(func_3152_call(), 0)
output = relay.Tuple([call_5337,call_5351,var_5352,call_5355,])
output2 = relay.Tuple([call_5338,call_5353,var_5352,call_5356,])
func_5372 = relay.Function([var_5352,], output)
mod['func_5372'] = func_5372
mod = relay.transform.InferType()(mod)
var_5373 = relay.var("var_5373", dtype = "uint16", shape = (25, 6))#candidate|5373|(25, 6)|var|uint16
output = func_5372(var_5373)
func_5374 = relay.Function([var_5373], output)
mutated_mod['func_5374'] = func_5374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_5418 = relay.TupleGetItem(func_3236_call(), 0)
call_5419 = relay.TupleGetItem(func_3238_call(), 0)
output = relay.Tuple([call_5418,])
output2 = relay.Tuple([call_5419,])
func_5424 = relay.Function([], output)
mod['func_5424'] = func_5424
mod = relay.transform.InferType()(mod)
mutated_mod['func_5424'] = func_5424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5424_call = mutated_mod.get_global_var('func_5424')
call_5425 = func_5424_call()
output = call_5425
func_5426 = relay.Function([], output)
mutated_mod['func_5426'] = func_5426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_5430 = relay.TupleGetItem(func_1994_call(), 0)
call_5431 = relay.TupleGetItem(func_1996_call(), 0)
output = call_5430
output2 = call_5431
func_5467 = relay.Function([], output)
mod['func_5467'] = func_5467
mod = relay.transform.InferType()(mod)
output = func_5467()
func_5468 = relay.Function([], output)
mutated_mod['func_5468'] = func_5468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mod.get_global_var('func_2968')
func_2970_call = mutated_mod.get_global_var('func_2970')
call_5486 = func_2968_call()
call_5487 = func_2968_call()
func_4947_call = mod.get_global_var('func_4947')
func_4950_call = mutated_mod.get_global_var('func_4950')
const_5495 = relay.const([[-9,-7],[1,4],[6,4],[6,10],[2,-9],[-5,10],[-2,6],[-8,6],[-9,6],[6,1],[-5,-7],[-7,-10],[-3,1],[3,9],[6,7],[-6,-1],[-7,-6],[8,-6],[-2,-4],[1,1],[-5,2],[-8,5],[6,7],[-6,-8],[-7,7],[-10,8],[5,-5],[8,-10],[10,10],[3,-1],[-9,1],[-9,2],[3,-3],[2,7],[3,-6],[9,3],[10,-9],[-1,1],[1,9],[3,7],[-1,-9],[2,-2],[9,8],[-6,9],[-4,-8],[-9,9],[1,9],[7,9],[6,3],[-5,3],[-5,-4],[-1,8],[1,2],[-2,-3],[9,8],[10,6],[-7,-2],[-3,8],[7,10],[5,3],[3,10],[-8,-10],[-5,-3],[-8,-10],[7,9],[8,-10],[7,3],[10,-10],[3,8],[-2,-6],[-1,-1],[5,5],[-3,2],[2,-6],[-3,-3],[-5,6],[2,7],[4,-1],[2,5],[-3,-1],[-7,-10],[6,7],[5,2],[2,5],[-2,8],[-8,1],[2,9],[-8,-4],[3,3],[-7,9],[-2,-1],[-9,-8],[1,-6],[-8,-8],[5,-6],[6,-10],[-3,10],[-3,2],[-4,-10],[9,3],[-8,8],[-6,-6],[2,7],[-1,10],[-8,-4]], dtype = "uint32")#candidate|5495|(105, 2)|const|uint32
call_5494 = relay.TupleGetItem(func_4947_call(relay.reshape(const_5495.astype('uint32'), [210,])), 0)
call_5496 = relay.TupleGetItem(func_4950_call(relay.reshape(const_5495.astype('uint32'), [210,])), 0)
func_1523_call = mod.get_global_var('func_1523')
func_1524_call = mutated_mod.get_global_var('func_1524')
call_5504 = relay.TupleGetItem(func_1523_call(), 0)
call_5505 = relay.TupleGetItem(func_1524_call(), 0)
var_5508 = relay.var("var_5508", dtype = "uint32", shape = (105, 2))#candidate|5508|(105, 2)|var|uint32
bop_5509 = relay.subtract(const_5495.astype('int32'), relay.reshape(var_5508.astype('int32'), relay.shape_of(const_5495))) # shape=(105, 2)
output = relay.Tuple([call_5486,call_5494,call_5504,bop_5509,])
output2 = relay.Tuple([call_5487,call_5496,call_5505,bop_5509,])
func_5512 = relay.Function([var_5508,], output)
mod['func_5512'] = func_5512
mod = relay.transform.InferType()(mod)
var_5513 = relay.var("var_5513", dtype = "uint32", shape = (105, 2))#candidate|5513|(105, 2)|var|uint32
output = func_5512(var_5513)
func_5514 = relay.Function([var_5513], output)
mutated_mod['func_5514'] = func_5514
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5529 = relay.const([[[6,-4],[2,6],[-5,5],[-4,-3],[-4,-6]],[[-2,-5],[-3,-5],[-10,-6],[-8,-7],[6,10]],[[-6,5],[1,-9],[-10,-3],[-7,1],[1,10]],[[-6,-8],[-7,-5],[-10,6],[-9,-8],[-8,-5]],[[-9,3],[9,7],[7,-3],[-4,-7],[8,5]],[[8,6],[2,-10],[-8,-1],[3,4],[-5,6]],[[-8,6],[2,2],[7,9],[-7,-5],[-8,1]],[[1,-4],[5,8],[9,-3],[3,-9],[-3,6]],[[-6,-9],[2,4],[-10,6],[9,6],[8,-4]],[[-10,-3],[6,-9],[-3,-1],[1,-4],[4,1]],[[-6,-7],[-4,9],[-9,-8],[9,3],[5,6]],[[-6,-9],[-7,-8],[-4,6],[5,-5],[6,-1]],[[-6,-5],[2,4],[-9,-7],[7,2],[2,6]],[[-8,-6],[-8,1],[4,1],[1,-8],[-2,-10]],[[1,6],[5,2],[7,-3],[-2,9],[7,-4]]], dtype = "uint8")#candidate|5529|(15, 5, 2)|const|uint8
var_5530 = relay.var("var_5530", dtype = "uint8", shape = (15, 5, 2))#candidate|5530|(15, 5, 2)|var|uint8
bop_5531 = relay.right_shift(const_5529.astype('uint8'), relay.reshape(var_5530.astype('uint8'), relay.shape_of(const_5529))) # shape=(15, 5, 2)
output = bop_5531
output2 = bop_5531
func_5543 = relay.Function([var_5530,], output)
mod['func_5543'] = func_5543
mod = relay.transform.InferType()(mod)
var_5544 = relay.var("var_5544", dtype = "uint8", shape = (15, 5, 2))#candidate|5544|(15, 5, 2)|var|uint8
output = func_5543(var_5544)
func_5545 = relay.Function([var_5544], output)
mutated_mod['func_5545'] = func_5545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2954_call = mod.get_global_var('func_2954')
func_2956_call = mutated_mod.get_global_var('func_2956')
call_5547 = func_2954_call()
call_5548 = func_2954_call()
output = relay.Tuple([call_5547,])
output2 = relay.Tuple([call_5548,])
func_5551 = relay.Function([], output)
mod['func_5551'] = func_5551
mod = relay.transform.InferType()(mod)
output = func_5551()
func_5552 = relay.Function([], output)
mutated_mod['func_5552'] = func_5552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5592 = relay.var("var_5592", dtype = "int16", shape = (16, 12, 5))#candidate|5592|(16, 12, 5)|var|int16
const_5593 = relay.const([[[2,-2,5,-4,10],[-2,4,5,1,-7],[6,-1,-1,-7,-10],[5,-10,-8,9,-9],[7,-6,-7,6,1],[-3,1,-9,-5,-9],[7,-5,-1,3,-7],[10,4,-5,-7,1],[4,4,-9,8,-9],[7,1,4,6,-1],[-8,9,9,4,-4],[-3,-8,2,1,-1]],[[6,-8,-9,8,-10],[2,-2,-1,-4,-6],[-8,7,-5,5,-10],[6,-4,5,-9,-1],[-4,6,-6,8,9],[-10,-4,-7,7,-6],[-6,-5,9,4,-4],[4,1,-7,-6,-9],[-10,4,-6,-4,-2],[-2,-3,9,-10,1],[-1,4,-6,9,8],[6,6,2,10,-7]],[[-6,-1,9,-2,-6],[-2,7,-8,-9,-4],[-2,-4,10,-2,-2],[5,9,7,-7,-6],[-4,-9,-8,-4,4],[5,8,-8,-5,-1],[9,-5,1,8,-2],[2,-5,-7,-9,-2],[-10,-3,-6,9,1],[-8,-5,9,-4,-7],[-1,2,-1,1,-9],[7,1,8,-2,9]],[[-4,-2,-8,8,-5],[-8,-3,4,-9,-7],[9,-6,5,8,-10],[9,-1,-4,1,3],[-6,-4,-3,-6,-3],[-1,-9,5,-2,1],[9,5,-2,-1,10],[3,-6,6,5,-2],[-4,-3,1,-9,2],[-2,-2,10,-5,-9],[6,-2,8,4,1],[-4,-10,-10,-6,1]],[[-8,8,7,4,-1],[-8,4,1,-7,5],[-2,4,5,-10,-2],[-10,1,8,8,-1],[-6,7,-8,-4,-7],[2,-8,-9,10,-8],[10,3,-6,3,-5],[-4,-3,3,-1,-6],[-7,-8,-7,-2,8],[-9,7,-2,-5,6],[1,-2,-1,6,5],[-10,2,-7,-5,-6]],[[-8,1,-9,8,-10],[-3,-2,-5,-4,-5],[-5,-1,-3,4,9],[10,6,-3,-6,6],[-5,9,8,10,-7],[2,2,-8,2,-2],[3,10,-3,2,-6],[-9,9,-8,-2,-10],[-5,-10,6,1,-2],[-10,-5,4,-5,-9],[-5,2,4,5,-8],[6,7,-10,6,10]],[[-4,-2,-3,7,3],[9,-4,-3,10,-8],[-3,4,2,3,-7],[5,5,10,-6,-6],[-5,-8,-5,-1,1],[3,-4,5,1,6],[-5,9,10,10,6],[-6,2,-4,-5,1],[-4,9,3,6,4],[-2,-4,-8,10,-2],[-3,-9,-10,-1,-8],[8,-1,2,1,-8]],[[1,-3,-10,-9,9],[7,10,9,1,-3],[-4,-2,10,-9,-5],[7,4,1,2,-4],[-3,-5,1,1,3],[2,8,4,-10,-2],[-7,-3,10,-7,-5],[-5,2,-1,3,-6],[7,8,1,-7,3],[8,-8,-3,4,-3],[8,7,-10,-4,10],[1,-7,-7,1,1]],[[-1,3,1,-8,-5],[6,-10,5,1,3],[1,-1,5,9,9],[-9,1,10,8,-1],[-10,8,9,-10,-5],[2,-8,-4,-8,-6],[-3,9,-7,-9,8],[9,4,10,1,4],[2,1,8,3,-8],[-4,4,-8,2,-9],[5,8,5,5,-7],[-1,-6,7,10,1]],[[-8,3,-6,-6,-6],[9,-1,5,5,2],[-10,9,7,-1,7],[-9,4,-9,-2,-1],[8,-2,-6,-4,6],[1,3,5,7,9],[7,-8,-9,-3,2],[9,-3,8,7,-8],[-2,-2,-2,-4,-2],[-4,-10,-2,-1,-10],[-1,10,10,-1,2],[4,2,-6,1,-3]],[[3,-2,2,-10,8],[-4,8,1,4,9],[-5,9,-6,-2,-4],[-10,4,10,3,-9],[-1,-10,-10,1,6],[9,2,9,-4,-7],[-7,7,-8,-9,8],[-5,-4,-10,-7,8],[10,7,7,9,8],[-2,-4,8,6,4],[9,3,-4,8,3],[-7,5,-6,-7,-4]],[[3,-9,4,7,-7],[4,-2,-9,-9,8],[-3,6,6,-10,6],[-9,9,4,-7,3],[-5,10,-3,4,6],[-7,-6,8,-4,-6],[-4,1,-4,7,7],[-7,-9,10,8,6],[-5,-4,6,2,10],[-2,2,8,-8,9],[-6,-8,7,-7,-1],[8,3,-4,6,9]],[[-3,-2,4,-2,6],[-8,10,-9,3,2],[8,9,-6,2,-10],[-7,4,7,-9,10],[2,10,-3,9,-7],[-3,2,10,-6,7],[-5,-8,-6,-9,-4],[10,7,8,-1,10],[-7,-4,-5,-7,7],[5,-2,3,8,1],[-10,-7,-5,9,-3],[5,-9,1,3,3]],[[5,4,-2,3,10],[3,-9,7,7,-9],[4,-10,-2,9,10],[9,-1,-3,1,-5],[2,-1,8,4,-7],[-4,8,5,7,-7],[-5,4,-9,-1,5],[-1,1,9,-3,3],[-7,-10,4,-4,9],[-10,8,-10,-3,7],[-6,4,-4,5,7],[7,8,10,5,3]],[[-7,-8,-8,-4,-9],[8,1,3,6,-5],[7,-8,1,4,-6],[-10,9,10,6,8],[-6,3,8,-5,3],[9,1,-4,9,-8],[7,8,4,3,3],[-7,8,6,-7,2],[10,1,-1,6,5],[5,-2,9,-10,-7],[-6,1,8,1,10],[-5,-7,4,3,9]],[[5,-1,-6,4,3],[-10,8,2,-1,-9],[-8,-1,-1,4,8],[4,-7,10,-5,9],[6,6,1,7,-3],[-2,3,8,2,-9],[-7,-4,8,-10,-8],[1,-10,-7,-7,4],[-5,2,10,3,4],[-2,5,-7,-10,5],[8,2,-5,9,-5],[1,-9,-7,3,-3]]], dtype = "int16")#candidate|5593|(16, 12, 5)|const|int16
bop_5594 = relay.bitwise_and(var_5592.astype('int16'), relay.reshape(const_5593.astype('int16'), relay.shape_of(var_5592))) # shape=(16, 12, 5)
func_168_call = mod.get_global_var('func_168')
func_170_call = mutated_mod.get_global_var('func_170')
var_5601 = relay.var("var_5601", dtype = "uint32", shape = (210,))#candidate|5601|(210,)|var|uint32
call_5600 = func_168_call(relay.reshape(var_5601.astype('uint32'), [6, 5, 7]))
call_5602 = func_168_call(relay.reshape(var_5601.astype('uint32'), [6, 5, 7]))
output = relay.Tuple([bop_5594,call_5600,var_5601,])
output2 = relay.Tuple([bop_5594,call_5602,var_5601,])
func_5608 = relay.Function([var_5592,var_5601,], output)
mod['func_5608'] = func_5608
mod = relay.transform.InferType()(mod)
mutated_mod['func_5608'] = func_5608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5608_call = mutated_mod.get_global_var('func_5608')
var_5610 = relay.var("var_5610", dtype = "int16", shape = (16, 12, 5))#candidate|5610|(16, 12, 5)|var|int16
var_5611 = relay.var("var_5611", dtype = "uint32", shape = (210,))#candidate|5611|(210,)|var|uint32
call_5609 = func_5608_call(var_5610,var_5611,)
output = call_5609
func_5612 = relay.Function([var_5610,var_5611,], output)
mutated_mod['func_5612'] = func_5612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3440_call = mod.get_global_var('func_3440')
func_3441_call = mutated_mod.get_global_var('func_3441')
call_5644 = func_3440_call()
call_5645 = func_3440_call()
uop_5648 = relay.log10(call_5644.astype('float32')) # shape=(7, 5, 14)
uop_5650 = relay.log10(call_5645.astype('float32')) # shape=(7, 5, 14)
uop_5660 = relay.atanh(uop_5648.astype('float64')) # shape=(7, 5, 14)
uop_5662 = relay.atanh(uop_5650.astype('float64')) # shape=(7, 5, 14)
func_778_call = mod.get_global_var('func_778')
func_780_call = mutated_mod.get_global_var('func_780')
call_5664 = relay.TupleGetItem(func_778_call(relay.reshape(uop_5660.astype('uint64'), [7, 5, 14])), 0)
call_5665 = relay.TupleGetItem(func_780_call(relay.reshape(uop_5660.astype('uint64'), [7, 5, 14])), 0)
output = relay.Tuple([uop_5660,call_5664,])
output2 = relay.Tuple([uop_5662,call_5665,])
func_5691 = relay.Function([], output)
mod['func_5691'] = func_5691
mod = relay.transform.InferType()(mod)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5691_call = mutated_mod.get_global_var('func_5691')
call_5692 = func_5691_call()
output = call_5692
func_5693 = relay.Function([], output)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5702 = relay.const([[[8,2,4,2,-2,6,2],[-8,9,-5,-6,-6,5,-9],[-3,-4,-4,8,-2,-6,1],[-4,6,-7,7,-4,7,9],[-8,-4,9,-1,-6,-10,9],[1,-8,3,6,10,2,-6]],[[6,2,6,-4,-5,7,-5],[-8,-3,-4,-5,-4,7,-4],[-10,7,-10,1,-4,-2,-1],[10,7,10,-8,-10,3,4],[2,6,-10,7,1,-7,-2],[-4,9,-10,-4,6,-7,5]],[[-4,8,8,-7,7,10,1],[-3,-6,7,2,10,8,-8],[-6,-4,5,-6,8,-1,5],[-4,-9,-1,-7,8,6,7],[-8,10,9,2,-8,7,2],[-4,1,3,-9,7,-3,-5]],[[-5,-4,9,-4,-7,-4,-7],[-4,1,5,-8,-4,-5,2],[5,6,4,-2,-3,1,7],[9,-6,-2,-1,-9,-7,7],[-3,7,-8,8,2,-5,8],[-5,3,6,6,-8,-7,7]]], dtype = "uint64")#candidate|5702|(4, 6, 7)|const|uint64
var_5703 = relay.var("var_5703", dtype = "uint64", shape = (4, 6, 7))#candidate|5703|(4, 6, 7)|var|uint64
bop_5704 = relay.right_shift(const_5702.astype('uint64'), relay.reshape(var_5703.astype('uint64'), relay.shape_of(const_5702))) # shape=(4, 6, 7)
output = bop_5704
output2 = bop_5704
func_5716 = relay.Function([var_5703,], output)
mod['func_5716'] = func_5716
mod = relay.transform.InferType()(mod)
mutated_mod['func_5716'] = func_5716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5717 = relay.var("var_5717", dtype = "uint64", shape = (4, 6, 7))#candidate|5717|(4, 6, 7)|var|uint64
func_5716_call = mutated_mod.get_global_var('func_5716')
call_5718 = func_5716_call(var_5717)
output = call_5718
func_5719 = relay.Function([var_5717], output)
mutated_mod['func_5719'] = func_5719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mod.get_global_var('func_4604')
func_4606_call = mutated_mod.get_global_var('func_4606')
call_5743 = relay.TupleGetItem(func_4604_call(), 0)
call_5744 = relay.TupleGetItem(func_4606_call(), 0)
output = call_5743
output2 = call_5744
func_5753 = relay.Function([], output)
mod['func_5753'] = func_5753
mod = relay.transform.InferType()(mod)
output = func_5753()
func_5754 = relay.Function([], output)
mutated_mod['func_5754'] = func_5754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mod.get_global_var('func_2836')
func_2837_call = mutated_mod.get_global_var('func_2837')
call_5760 = relay.TupleGetItem(func_2836_call(), 2)
call_5761 = relay.TupleGetItem(func_2837_call(), 2)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_5763 = relay.TupleGetItem(func_1994_call(), 0)
call_5764 = relay.TupleGetItem(func_1996_call(), 0)
var_5767 = relay.var("var_5767", dtype = "uint64", shape = (7, 5, 14))#candidate|5767|(7, 5, 14)|var|uint64
bop_5768 = relay.not_equal(call_5763.astype('bool'), relay.reshape(var_5767.astype('bool'), relay.shape_of(call_5763))) # shape=(7, 5, 14)
bop_5771 = relay.not_equal(call_5764.astype('bool'), relay.reshape(var_5767.astype('bool'), relay.shape_of(call_5764))) # shape=(7, 5, 14)
const_5774 = relay.const([3,-9,2,-2,9,-7,-4,9,-5,5,6,-7,-7,-5,-2,-10,-10,1,-10,-10,-2,-4,-6,-6,-6,2,-8,-8,-3,4,5,-2,3,-8,-6,-2,7,-7,-10,4,5,-9,5,10,2,5,7,4,-1,-3,-1,7,2,9,-10,-8,-10,-8,6,-3,1,8,5,8,-4,-3,5,-1,6,8,6,1,-7,-9,6,-1,-9,-6,1,-10,-6,-10,-5,-7,2,8,-5,3,7,-5,5,-3,7,1,-5,2,4,-2,4,9,-9,5,-6,-6,-10,8,-8,-10,-2,2,-1,-9,-8,-3,2,-2,1,-7,-6,1,-5,-3,-10,8,3,-9,6,-1,-1,-9,-8,-6,-8,7,-5,2,-7,-10,10,-9,8,9,-6,-8,-5,-1,-10,4,-9,4,7,-3,2,1,1,-5,8,5,-6,-2,-2,4,10,-9,-8,3,8,-10,-9,-2,-1,-1,3,-2,1,-10,6,6,-3,-5,8,6,3,-8,-9,5,9,8,4,-1,-5,-1,-4,-9,1,-9,1,9,-3,8,-7,-1,-9,-8,-10,-9,7,-10,-6,-9], dtype = "uint32")#candidate|5774|(210,)|const|uint32
bop_5775 = relay.minimum(call_5760.astype('int16'), relay.reshape(const_5774.astype('int16'), relay.shape_of(call_5760))) # shape=(210,)
bop_5778 = relay.minimum(call_5761.astype('int16'), relay.reshape(const_5774.astype('int16'), relay.shape_of(call_5761))) # shape=(210,)
func_2180_call = mod.get_global_var('func_2180')
func_2184_call = mutated_mod.get_global_var('func_2184')
call_5808 = relay.TupleGetItem(func_2180_call(relay.reshape(call_5760.astype('uint32'), [210,]), relay.reshape(const_5774.astype('float32'), [6, 5, 7]), ), 4)
call_5809 = relay.TupleGetItem(func_2184_call(relay.reshape(call_5760.astype('uint32'), [210,]), relay.reshape(const_5774.astype('float32'), [6, 5, 7]), ), 4)
output = relay.Tuple([bop_5768,bop_5775,call_5808,])
output2 = relay.Tuple([bop_5771,bop_5778,call_5809,])
func_5814 = relay.Function([var_5767,], output)
mod['func_5814'] = func_5814
mod = relay.transform.InferType()(mod)
mutated_mod['func_5814'] = func_5814
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5815 = relay.var("var_5815", dtype = "uint64", shape = (7, 5, 14))#candidate|5815|(7, 5, 14)|var|uint64
func_5814_call = mutated_mod.get_global_var('func_5814')
call_5816 = func_5814_call(var_5815)
output = call_5816
func_5817 = relay.Function([var_5815], output)
mutated_mod['func_5817'] = func_5817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mod.get_global_var('func_965')
func_967_call = mutated_mod.get_global_var('func_967')
call_5845 = relay.TupleGetItem(func_965_call(), 0)
call_5846 = relay.TupleGetItem(func_967_call(), 0)
var_5851 = relay.var("var_5851", dtype = "uint64", shape = (7, 5, 14))#candidate|5851|(7, 5, 14)|var|uint64
bop_5852 = relay.greater(call_5845.astype('bool'), relay.reshape(var_5851.astype('bool'), relay.shape_of(call_5845))) # shape=(7, 5, 14)
bop_5855 = relay.greater(call_5846.astype('bool'), relay.reshape(var_5851.astype('bool'), relay.shape_of(call_5846))) # shape=(7, 5, 14)
func_5608_call = mod.get_global_var('func_5608')
func_5612_call = mutated_mod.get_global_var('func_5612')
var_5857 = relay.var("var_5857", dtype = "int16", shape = (960,))#candidate|5857|(960,)|var|int16
var_5858 = relay.var("var_5858", dtype = "uint32", shape = (210,))#candidate|5858|(210,)|var|uint32
call_5856 = relay.TupleGetItem(func_5608_call(relay.reshape(var_5857.astype('int16'), [16, 12, 5]), relay.reshape(var_5858.astype('uint32'), [210,]), ), 0)
call_5859 = relay.TupleGetItem(func_5612_call(relay.reshape(var_5857.astype('int16'), [16, 12, 5]), relay.reshape(var_5858.astype('uint32'), [210,]), ), 0)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
call_5861 = relay.TupleGetItem(func_2999_call(), 0)
call_5862 = relay.TupleGetItem(func_3001_call(), 0)
output = relay.Tuple([bop_5852,call_5856,var_5857,var_5858,call_5861,])
output2 = relay.Tuple([bop_5855,call_5859,var_5857,var_5858,call_5862,])
func_5866 = relay.Function([var_5851,var_5857,var_5858,], output)
mod['func_5866'] = func_5866
mod = relay.transform.InferType()(mod)
mutated_mod['func_5866'] = func_5866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5866_call = mutated_mod.get_global_var('func_5866')
var_5868 = relay.var("var_5868", dtype = "uint64", shape = (7, 5, 14))#candidate|5868|(7, 5, 14)|var|uint64
var_5869 = relay.var("var_5869", dtype = "int16", shape = (960,))#candidate|5869|(960,)|var|int16
var_5870 = relay.var("var_5870", dtype = "uint32", shape = (210,))#candidate|5870|(210,)|var|uint32
call_5867 = func_5866_call(var_5868,var_5869,var_5870,)
output = call_5867
func_5871 = relay.Function([var_5868,var_5869,var_5870,], output)
mutated_mod['func_5871'] = func_5871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3121_call = mod.get_global_var('func_3121')
func_3123_call = mutated_mod.get_global_var('func_3123')
call_5974 = relay.TupleGetItem(func_3121_call(), 0)
call_5975 = relay.TupleGetItem(func_3123_call(), 0)
func_1307_call = mod.get_global_var('func_1307')
func_1309_call = mutated_mod.get_global_var('func_1309')
const_5986 = relay.const([-2.183997,6.074945,4.280608,9.835563,-4.065740,7.776638,-1.925896,4.186067,1.689106,-3.554110,-1.336184,0.565624,-6.812714,-0.641142,-1.435424,-6.167569,6.458204,1.076438,6.723670,5.483528,2.358103,9.905314,-6.359868,2.810455,-5.936369,-1.300180,8.189434,-1.324188,5.592405,-3.232520,1.853851,0.773102,-3.711834,8.999000,4.385041,0.247528,8.310293,-4.866750,9.144489,0.726020,9.620587,0.420994,3.489488,-8.670453,-4.975929,-2.796050,-9.604907,-6.898142,-7.907713,-0.048977,-1.341805,-0.566693,-7.354466,-6.688967,-8.738032,5.357655,5.814377,5.251125,1.509622,1.352556,-3.240828,1.042045,7.991496,1.599868,4.939315], dtype = "float32")#candidate|5986|(65,)|const|float32
call_5985 = relay.TupleGetItem(func_1307_call(relay.reshape(const_5986.astype('float32'), [65,])), 7)
call_5987 = relay.TupleGetItem(func_1309_call(relay.reshape(const_5986.astype('float32'), [65,])), 7)
output = relay.Tuple([call_5974,call_5985,const_5986,])
output2 = relay.Tuple([call_5975,call_5987,const_5986,])
func_5990 = relay.Function([], output)
mod['func_5990'] = func_5990
mod = relay.transform.InferType()(mod)
mutated_mod['func_5990'] = func_5990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mutated_mod.get_global_var('func_5990')
call_5991 = func_5990_call()
output = call_5991
func_5992 = relay.Function([], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2661_call = mod.get_global_var('func_2661')
func_2662_call = mutated_mod.get_global_var('func_2662')
call_6004 = relay.TupleGetItem(func_2661_call(), 1)
call_6005 = relay.TupleGetItem(func_2662_call(), 1)
func_1878_call = mod.get_global_var('func_1878')
func_1882_call = mutated_mod.get_global_var('func_1882')
var_6013 = relay.var("var_6013", dtype = "float32", shape = (60, 1))#candidate|6013|(60, 1)|var|float32
const_6014 = relay.const([3.429469,-3.860108,-4.602344,9.135767,-4.674556,8.057328,7.587811,-3.787533,-2.018756,5.726759,5.684798,-2.254847,1.996355,2.373372,9.961138,8.891265,-8.468404,-1.273525,-7.590394,3.504490,3.111154,5.531883,8.533027,7.175105,-0.082818,5.933395,-8.540618,3.875419,3.108576,-4.465073,-4.987386,-8.355083,-4.438799,5.937865,-3.903997,2.457160,1.907159,6.097764,-2.755877,-2.248024,7.517375,-1.392403,9.159562,-9.651824,-2.256436,-3.629683,-1.287708,0.259560,4.844703,-0.525379,6.614474,-1.423234,-4.017360,1.167689,-9.412982,4.329957,-3.104291,0.617652,-1.046376,-8.280829,6.464387,1.974779,1.259363,-5.940712,-6.250136,3.550645,-7.477269,-7.363950,7.121609,5.267332,-1.423257,7.131231,-4.690815,-2.159036,-2.437895,9.219139,4.302389,-9.233550,5.934319,-6.385381,0.876247,-8.775382,0.945256,-5.882384,-4.878851,-4.400213,-0.333295,4.243539,-5.440162,1.807795,3.100904,-5.896079,-8.093738,3.819518,5.860790,4.856392,3.565757,-4.552643,-5.999791,5.655107,-6.518296,9.622019,-9.464363,0.111144,4.031954,4.068425,1.149051,0.266312,-7.447312,-0.377419,-7.366596,-5.467926,3.103420,-9.966118,2.221216,-0.454701,4.275491,9.391830,6.176495,7.201343,6.856066,0.297717,-1.259273,-0.287699,2.412259,7.588988,-7.921787,-2.414182,-8.353243,-4.422341,-1.898624,-7.402095,-7.146130,3.654798,-0.249240,-4.877311,-1.997864,3.200264,8.557223,3.503248,-2.504196,-1.171642,1.669506,-1.652840,-7.183816,2.149059,5.555241,-7.076638,8.498623,4.673244,-1.563535,-2.709062,3.918345,-8.826784,1.120576,-5.184445,-2.015885,7.950619,3.297211,1.638618,-8.881334,-8.598293,-7.739367,5.720676,8.325244,-6.854363,5.158379,-5.283399,-6.959019,8.529266,-4.151020,9.655546,-0.414485,-4.554586,-5.290605,5.773020,3.988800,-6.400500,1.343276,6.142650,6.933981,-1.515060,-7.318864,5.113691,1.894292,1.592600,-5.950357,-2.842143,8.404165,-0.394695,8.909256,-6.677917,-0.761257,-7.870583,-9.426790,-1.055979,6.211147,-2.232118,1.277605,-0.601103,-7.430095,-6.615667,-9.390730,-3.432935,-1.568302,0.290448,-8.936506,-6.384897,4.337965,-7.670756,-5.615844,9.075315,-0.492693,-8.549556,9.096340,-0.350107,-4.053954,6.884808,-8.843014,-6.413413,-9.303058,-1.283924,2.134359,0.044802,2.475952,-6.961214,-4.626905,-7.608584,-9.982947,-5.048323,4.561496,0.760781,-9.566229,9.979502,-4.216980,4.445801,5.204629,-8.704377,-1.413840,8.942167,6.584244,4.930069,2.799746,-0.171344,-9.519719,-2.773433,-1.942881,6.251310,-4.911040,7.798147,-7.163279,1.163992,-8.114391,-3.592019,-6.235494,-6.657154,-3.576298,2.088882,4.548678,2.326605,2.260558,-9.227415,8.914081,-5.818907,-2.611509,6.242556,-2.033186,-8.195793,-5.974339,1.138435,8.907175,-3.802002,5.476867,5.334441,-1.991827,6.476047,-0.708654,1.037012,3.935668,1.413205,2.646882,8.014822,-9.060280,-6.403192,-0.301827,3.480577,7.904161,4.092972,5.828595,-2.887276,3.743589,7.191070,2.783164,-4.480484,-0.130219,-7.372797,-9.421544,9.452147,3.488772,5.784581,9.937068,3.233667,-9.224048,-9.253431,-7.499607,8.162544,-6.913629,4.233453,2.486555,-1.486711,-7.083934,8.569325,-8.617945,8.662373,-5.016711,-9.444096,7.868627,0.847043,-0.059567,1.242569,-6.218189,7.655654,-6.924506,-7.583268,-6.739078,7.999084,3.319810,3.293146,-3.847377,3.644569,1.483596,-9.537892,-2.076792,-3.997662,5.366952,8.287842,8.674287,-8.148380,5.110929,0.189753,-2.156213,-7.360740,-2.550423,7.732718,-8.372356,8.806279,-3.530253,-7.844042,6.026731,-8.011969,8.083907,-9.916358,-6.650751,-9.841170,8.075460,2.921328,-9.053344,2.126203,5.310219,9.692487,-9.301711,7.856199,2.212084,5.748368,-7.985239,2.591579,8.720645,-2.699988,7.479253,3.677626,2.715265,-6.562428,1.041137,-0.971805,-7.603454,-3.514747,-6.581106,-6.410428,-1.168502,0.609975,3.353513,-4.763437,-8.959895,-2.137205,0.542782,6.693493,-3.920438,-3.536999,6.930864,-7.529406,8.049833,-4.135232,-8.866510,6.821721,-1.229191,5.877465,3.421519,-5.539880,8.516769,7.662102,7.974373,2.665906,-8.369877,6.035922,-3.354488,-9.001124,-1.889661,0.318074,6.721363,3.157007,7.213914,2.531290,-1.232854,0.241215,-3.266572,-4.259009,3.088163,5.006811,-8.387225,5.664420,-8.814903,-1.115975,6.582147,0.387690,-4.653883,-7.649997,8.136732,-1.352370,-9.806767,4.149122,8.306591,-7.659678,2.903291,-7.747301,-9.695588,-0.266755,6.355254,3.444915,8.732493,5.127505,-0.133061,5.963092,0.972272,8.650775,5.822380,-9.600878,1.245924,1.605189,-5.672428,-3.069857,-2.399787,7.360722,0.661961,-2.941636,3.134366,-6.496635,0.212439,-1.118370,7.504563,-4.196989,-3.032087,8.415016,3.645206,1.822290,6.785971,-6.004869,-7.351914,1.010303,1.841086,-3.844484,-7.893844,-8.877110,2.489407,-7.471479,-1.497216,9.012050,-8.308693,-7.390460,-3.616361,7.035814,7.693575,4.347356,-8.031883,9.387748,-1.116223,-6.739394,-2.661379,-7.187264,2.485688,9.261129,-8.113638,1.214579,3.150180,-2.871600,1.112109,2.045243,-2.802025,-2.654558,-8.786962,-3.781728,-3.805560,2.223540,1.658423,-5.230744,-7.081294,-5.811185,-3.060188,4.371041,-0.075855,4.582018,-4.713455,-7.788618,0.429054,8.305680,7.394670,-1.927395,-1.855823,-8.580482,-4.940926,4.472210,-0.456185,8.981886,9.483339,7.500857,-1.403878,2.245210,9.048602,6.351811,-4.997809,-0.887940,-6.923760,0.805598,-2.275335,-0.037121,-7.788781,-2.984885,-1.985235,-6.934464,-8.527645,8.282263,-2.103588,8.053113,-9.490472,0.048522,9.836568,-0.104020,-9.628698,1.283652,-3.927548,1.441983,8.000192,3.659919,6.830077,0.187479,8.134155,5.828381,4.154506,-8.272863,2.910116,-5.268953,3.919483,8.938525,3.883524,5.610444,-1.537328,-9.739987,-7.905618,3.607105,4.594416,8.909340,7.355549,5.279463,-0.319925,6.066147,4.568411,-3.523878,-2.788018,-3.768636,-1.042099,5.625500,4.673600,-3.410143,-3.829891,2.385647,-5.083191,-9.241583,3.145628,-9.881707,7.737992,-1.099348,-6.365058,-5.630837,-3.329478,-4.686325,-2.791486,4.935898,6.063480,2.568123,-1.659610,-3.719887,4.928789,-3.482549,-8.219157,-2.522479,-7.693407,-8.618592,-4.676485,-1.584604,4.600261,3.526012,-9.805241,5.823709,2.765787,2.802857,-9.996451,-3.048507,1.610049,-6.368298,-7.616732,7.271724,5.538852,7.870247,-8.107783,-1.691070,-8.378997,9.646684,1.790529,-2.994455,8.414002,-0.033583,9.993754,-0.966048,7.543735,-4.901267,0.835134,7.222085,3.255155,-2.528651,-2.524177,-3.344895,6.803030,0.901311,-8.834947,2.982462,-9.946806,7.374898,-1.609253,-0.050796,8.350753,1.618678,-2.906719,1.902398,1.195177,-9.322677,2.632745,-9.441681,-4.558400,8.622150,-6.387203,8.793068,-4.062696,-7.338563,-2.032183,-3.466781,-9.839869,-6.383329,-5.243216,-8.299986,-3.928546,6.990019,3.146134,-6.655321,-2.526784,5.544493,-4.698178,4.628716,9.233336,3.138791,-1.961678,5.023030,-0.408520,6.944444,-7.469190,-5.878568,-7.283635,-6.387635,-6.388633,-8.273031,-4.946587,3.152128,-2.509352,8.876241,-3.288801,8.877886,-7.307085,0.872760,-4.407529,-0.335662,5.801552,2.363114,-4.016337,1.349603,-0.344758,1.442283,6.166391,4.077931,3.561557,-3.736589,-1.737279,-9.446696,-9.461027,3.913901,5.721149,7.007530,-0.177410,-7.382460,-6.538815,7.797562,7.083637,4.634872], dtype = "float32")#candidate|6014|(720,)|const|float32
call_6012 = relay.TupleGetItem(func_1878_call(relay.reshape(var_6013.astype('float32'), [1, 12, 5]), relay.reshape(const_6014.astype('float32'), [12, 12, 5]), ), 0)
call_6015 = relay.TupleGetItem(func_1882_call(relay.reshape(var_6013.astype('float32'), [1, 12, 5]), relay.reshape(const_6014.astype('float32'), [12, 12, 5]), ), 0)
output = relay.Tuple([call_6004,call_6012,var_6013,const_6014,])
output2 = relay.Tuple([call_6005,call_6015,var_6013,const_6014,])
func_6054 = relay.Function([var_6013,], output)
mod['func_6054'] = func_6054
mod = relay.transform.InferType()(mod)
mutated_mod['func_6054'] = func_6054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6055 = relay.var("var_6055", dtype = "float32", shape = (60, 1))#candidate|6055|(60, 1)|var|float32
func_6054_call = mutated_mod.get_global_var('func_6054')
call_6056 = func_6054_call(var_6055)
output = call_6056
func_6057 = relay.Function([var_6055], output)
mutated_mod['func_6057'] = func_6057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_682_call = mutated_mod.get_global_var('func_682')
call_6066 = relay.TupleGetItem(func_681_call(), 0)
call_6067 = relay.TupleGetItem(func_682_call(), 0)
func_3394_call = mod.get_global_var('func_3394')
func_3398_call = mutated_mod.get_global_var('func_3398')
var_6095 = relay.var("var_6095", dtype = "int16", shape = (10,))#candidate|6095|(10,)|var|int16
var_6096 = relay.var("var_6096", dtype = "int16", shape = (20,))#candidate|6096|(20,)|var|int16
call_6094 = func_3394_call(relay.reshape(var_6095.astype('int16'), [2, 5, 1]), relay.reshape(var_6096.astype('int16'), [2, 5, 2]), )
call_6097 = func_3394_call(relay.reshape(var_6095.astype('int16'), [2, 5, 1]), relay.reshape(var_6096.astype('int16'), [2, 5, 2]), )
func_2693_call = mod.get_global_var('func_2693')
func_2697_call = mutated_mod.get_global_var('func_2697')
const_6104 = relay.const(4, dtype = "uint8")#candidate|6104|()|const|uint8
var_6105 = relay.var("var_6105", dtype = "uint8", shape = (96,))#candidate|6105|(96,)|var|uint8
call_6103 = relay.TupleGetItem(func_2693_call(relay.reshape(const_6104.astype('uint8'), []), relay.reshape(var_6105.astype('uint8'), [16, 6, 1]), ), 0)
call_6106 = relay.TupleGetItem(func_2697_call(relay.reshape(const_6104.astype('uint8'), []), relay.reshape(var_6105.astype('uint8'), [16, 6, 1]), ), 0)
func_5814_call = mod.get_global_var('func_5814')
func_5817_call = mutated_mod.get_global_var('func_5817')
call_6112 = relay.TupleGetItem(func_5814_call(relay.reshape(call_6066.astype('uint64'), [7, 5, 14])), 1)
call_6113 = relay.TupleGetItem(func_5817_call(relay.reshape(call_6066.astype('uint64'), [7, 5, 14])), 1)
output = relay.Tuple([call_6066,call_6094,var_6095,var_6096,call_6103,const_6104,var_6105,call_6112,])
output2 = relay.Tuple([call_6067,call_6097,var_6095,var_6096,call_6106,const_6104,var_6105,call_6113,])
func_6127 = relay.Function([var_6095,var_6096,var_6105,], output)
mod['func_6127'] = func_6127
mod = relay.transform.InferType()(mod)
mutated_mod['func_6127'] = func_6127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6127_call = mutated_mod.get_global_var('func_6127')
var_6129 = relay.var("var_6129", dtype = "int16", shape = (10,))#candidate|6129|(10,)|var|int16
var_6130 = relay.var("var_6130", dtype = "int16", shape = (20,))#candidate|6130|(20,)|var|int16
var_6131 = relay.var("var_6131", dtype = "uint8", shape = (96,))#candidate|6131|(96,)|var|uint8
call_6128 = func_6127_call(var_6129,var_6130,var_6131,)
output = call_6128
func_6132 = relay.Function([var_6129,var_6130,var_6131,], output)
mutated_mod['func_6132'] = func_6132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mod.get_global_var('func_2836')
func_2837_call = mutated_mod.get_global_var('func_2837')
call_6140 = relay.TupleGetItem(func_2836_call(), 1)
call_6141 = relay.TupleGetItem(func_2837_call(), 1)
output = call_6140
output2 = call_6141
func_6145 = relay.Function([], output)
mod['func_6145'] = func_6145
mod = relay.transform.InferType()(mod)
mutated_mod['func_6145'] = func_6145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6145_call = mutated_mod.get_global_var('func_6145')
call_6146 = func_6145_call()
output = call_6146
func_6147 = relay.Function([], output)
mutated_mod['func_6147'] = func_6147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6145_call = mod.get_global_var('func_6145')
func_6147_call = mutated_mod.get_global_var('func_6147')
call_6196 = func_6145_call()
call_6197 = func_6145_call()
output = call_6196
output2 = call_6197
func_6206 = relay.Function([], output)
mod['func_6206'] = func_6206
mod = relay.transform.InferType()(mod)
mutated_mod['func_6206'] = func_6206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6206_call = mutated_mod.get_global_var('func_6206')
call_6207 = func_6206_call()
output = call_6207
func_6208 = relay.Function([], output)
mutated_mod['func_6208'] = func_6208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2427_call = mod.get_global_var('func_2427')
func_2429_call = mutated_mod.get_global_var('func_2429')
call_6285 = relay.TupleGetItem(func_2427_call(), 3)
call_6286 = relay.TupleGetItem(func_2429_call(), 3)
func_5543_call = mod.get_global_var('func_5543')
func_5545_call = mutated_mod.get_global_var('func_5545')
var_6328 = relay.var("var_6328", dtype = "uint8", shape = (150,))#candidate|6328|(150,)|var|uint8
call_6327 = func_5543_call(relay.reshape(var_6328.astype('uint8'), [15, 5, 2]))
call_6329 = func_5543_call(relay.reshape(var_6328.astype('uint8'), [15, 5, 2]))
var_6334 = relay.var("var_6334", dtype = "uint64", shape = (7, 11, 2))#candidate|6334|(7, 11, 2)|var|uint64
bop_6335 = relay.right_shift(call_6285.astype('int32'), relay.reshape(var_6334.astype('int32'), relay.shape_of(call_6285))) # shape=(7, 11, 2)
bop_6338 = relay.right_shift(call_6286.astype('int32'), relay.reshape(var_6334.astype('int32'), relay.shape_of(call_6286))) # shape=(7, 11, 2)
output = relay.Tuple([call_6327,var_6328,bop_6335,])
output2 = relay.Tuple([call_6329,var_6328,bop_6338,])
func_6345 = relay.Function([var_6328,var_6334,], output)
mod['func_6345'] = func_6345
mod = relay.transform.InferType()(mod)
mutated_mod['func_6345'] = func_6345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6345_call = mutated_mod.get_global_var('func_6345')
var_6347 = relay.var("var_6347", dtype = "uint8", shape = (150,))#candidate|6347|(150,)|var|uint8
var_6348 = relay.var("var_6348", dtype = "uint64", shape = (7, 11, 2))#candidate|6348|(7, 11, 2)|var|uint64
call_6346 = func_6345_call(var_6347,var_6348,)
output = call_6346
func_6349 = relay.Function([var_6347,var_6348,], output)
mutated_mod['func_6349'] = func_6349
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2954_call = mod.get_global_var('func_2954')
func_2956_call = mutated_mod.get_global_var('func_2956')
call_6384 = func_2954_call()
call_6385 = func_2954_call()
func_500_call = mod.get_global_var('func_500')
func_502_call = mutated_mod.get_global_var('func_502')
call_6390 = func_500_call()
call_6391 = func_500_call()
output = relay.Tuple([call_6384,call_6390,])
output2 = relay.Tuple([call_6385,call_6391,])
func_6393 = relay.Function([], output)
mod['func_6393'] = func_6393
mod = relay.transform.InferType()(mod)
output = func_6393()
func_6394 = relay.Function([], output)
mutated_mod['func_6394'] = func_6394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1711_call = mod.get_global_var('func_1711')
func_1712_call = mutated_mod.get_global_var('func_1712')
call_6424 = func_1711_call()
call_6425 = func_1711_call()
var_6454 = relay.var("var_6454", dtype = "uint64", shape = (7, 5, 14))#candidate|6454|(7, 5, 14)|var|uint64
bop_6455 = relay.less_equal(call_6424.astype('bool'), relay.reshape(var_6454.astype('bool'), relay.shape_of(call_6424))) # shape=(7, 5, 14)
bop_6458 = relay.less_equal(call_6425.astype('bool'), relay.reshape(var_6454.astype('bool'), relay.shape_of(call_6425))) # shape=(7, 5, 14)
output = relay.Tuple([bop_6455,])
output2 = relay.Tuple([bop_6458,])
func_6464 = relay.Function([var_6454,], output)
mod['func_6464'] = func_6464
mod = relay.transform.InferType()(mod)
mutated_mod['func_6464'] = func_6464
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6465 = relay.var("var_6465", dtype = "uint64", shape = (7, 5, 14))#candidate|6465|(7, 5, 14)|var|uint64
func_6464_call = mutated_mod.get_global_var('func_6464')
call_6466 = func_6464_call(var_6465)
output = call_6466
func_6467 = relay.Function([var_6465], output)
mutated_mod['func_6467'] = func_6467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2317_call = mod.get_global_var('func_2317')
func_2318_call = mutated_mod.get_global_var('func_2318')
call_6496 = relay.TupleGetItem(func_2317_call(), 0)
call_6497 = relay.TupleGetItem(func_2318_call(), 0)
output = call_6496
output2 = call_6497
func_6500 = relay.Function([], output)
mod['func_6500'] = func_6500
mod = relay.transform.InferType()(mod)
output = func_6500()
func_6501 = relay.Function([], output)
mutated_mod['func_6501'] = func_6501
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4376_call = mod.get_global_var('func_4376')
func_4378_call = mutated_mod.get_global_var('func_4378')
call_6519 = func_4376_call()
call_6520 = func_4376_call()
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_6523 = relay.TupleGetItem(func_1994_call(), 0)
call_6524 = relay.TupleGetItem(func_1996_call(), 0)
func_3361_call = mod.get_global_var('func_3361')
func_3364_call = mutated_mod.get_global_var('func_3364')
const_6526 = relay.const([-9,-2,1,9,4,-8,-8,3,-10,9,-7,4,3,1,-10,6,5,6,1,1,-3,2,-4,9,2,-7,4,-8,-1,2,-9,3,-8,10,-6,5,-2,1,1,-9,6,3,-9,-7,-10,-2,-9,3,-3,7,5,-9,8,-4,-7,-4,-3,3,8,10,10,6,-6,7,3,-9,5,-7,7,1,-8,-1,2,1,-5,-7,-3,-6,-4,-8,-6,-5,-6,-5,-8,1,1,-7,5,2,-10,-4,-4,4,3,4,1,-4,4,4,-6,-9,6,-2,5,10,7,-10,4,8,6,-9,-1,-5,-10,6,3,-7,-1,-7,-6,-2,1,-3,-6,2,-1,10,-2,7,-4,-2,-10,4,-1,-8,10,-10,-3,-5,4,-10,10,8,-5,-6,10,5,-10,-1], dtype = "uint16")#candidate|6526|(150,)|const|uint16
call_6525 = relay.TupleGetItem(func_3361_call(relay.reshape(const_6526.astype('uint16'), [5, 6, 5]), relay.reshape(const_6526.astype('int64'), [5, 6, 5]), ), 1)
call_6527 = relay.TupleGetItem(func_3364_call(relay.reshape(const_6526.astype('uint16'), [5, 6, 5]), relay.reshape(const_6526.astype('int64'), [5, 6, 5]), ), 1)
func_1952_call = mod.get_global_var('func_1952')
func_1956_call = mutated_mod.get_global_var('func_1956')
var_6529 = relay.var("var_6529", dtype = "float64", shape = (165,))#candidate|6529|(165,)|var|float64
var_6530 = relay.var("var_6530", dtype = "uint32", shape = (210,))#candidate|6530|(210,)|var|uint32
call_6528 = relay.TupleGetItem(func_1952_call(relay.reshape(var_6529.astype('float64'), [165,]), relay.reshape(var_6530.astype('uint32'), [210,]), ), 0)
call_6531 = relay.TupleGetItem(func_1956_call(relay.reshape(var_6529.astype('float64'), [165,]), relay.reshape(var_6530.astype('uint32'), [210,]), ), 0)
func_956_call = mod.get_global_var('func_956')
func_958_call = mutated_mod.get_global_var('func_958')
var_6538 = relay.var("var_6538", dtype = "float64", shape = (77, 1))#candidate|6538|(77, 1)|var|float64
call_6537 = func_956_call(relay.reshape(var_6538.astype('float64'), [11, 7, 1]))
call_6539 = func_956_call(relay.reshape(var_6538.astype('float64'), [11, 7, 1]))
func_4376_call = mod.get_global_var('func_4376')
func_4378_call = mutated_mod.get_global_var('func_4378')
call_6540 = func_4376_call()
call_6541 = func_4376_call()
func_1571_call = mod.get_global_var('func_1571')
func_1572_call = mutated_mod.get_global_var('func_1572')
call_6543 = relay.TupleGetItem(func_1571_call(), 0)
call_6544 = relay.TupleGetItem(func_1572_call(), 0)
output = relay.Tuple([call_6519,call_6523,call_6525,const_6526,call_6528,var_6529,var_6530,call_6537,var_6538,call_6540,call_6543,])
output2 = relay.Tuple([call_6520,call_6524,call_6527,const_6526,call_6531,var_6529,var_6530,call_6539,var_6538,call_6541,call_6544,])
func_6552 = relay.Function([var_6529,var_6530,var_6538,], output)
mod['func_6552'] = func_6552
mod = relay.transform.InferType()(mod)
mutated_mod['func_6552'] = func_6552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6552_call = mutated_mod.get_global_var('func_6552')
var_6554 = relay.var("var_6554", dtype = "float64", shape = (165,))#candidate|6554|(165,)|var|float64
var_6555 = relay.var("var_6555", dtype = "uint32", shape = (210,))#candidate|6555|(210,)|var|uint32
var_6556 = relay.var("var_6556", dtype = "float64", shape = (77, 1))#candidate|6556|(77, 1)|var|float64
call_6553 = func_6552_call(var_6554,var_6555,var_6556,)
output = call_6553
func_6557 = relay.Function([var_6554,var_6555,var_6556,], output)
mutated_mod['func_6557'] = func_6557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1994_call = mod.get_global_var('func_1994')
func_1996_call = mutated_mod.get_global_var('func_1996')
call_6559 = relay.TupleGetItem(func_1994_call(), 0)
call_6560 = relay.TupleGetItem(func_1996_call(), 0)
func_340_call = mod.get_global_var('func_340')
func_343_call = mutated_mod.get_global_var('func_343')
var_6567 = relay.var("var_6567", dtype = "uint32", shape = (210,))#candidate|6567|(210,)|var|uint32
call_6566 = relay.TupleGetItem(func_340_call(relay.reshape(var_6567.astype('uint32'), [210,])), 0)
call_6568 = relay.TupleGetItem(func_343_call(relay.reshape(var_6567.astype('uint32'), [210,])), 0)
func_6393_call = mod.get_global_var('func_6393')
func_6394_call = mutated_mod.get_global_var('func_6394')
call_6575 = relay.TupleGetItem(func_6393_call(), 0)
call_6576 = relay.TupleGetItem(func_6394_call(), 0)
output = relay.Tuple([call_6559,call_6566,var_6567,call_6575,])
output2 = relay.Tuple([call_6560,call_6568,var_6567,call_6576,])
func_6630 = relay.Function([var_6567,], output)
mod['func_6630'] = func_6630
mod = relay.transform.InferType()(mod)
var_6631 = relay.var("var_6631", dtype = "uint32", shape = (210,))#candidate|6631|(210,)|var|uint32
output = func_6630(var_6631)
func_6632 = relay.Function([var_6631], output)
mutated_mod['func_6632'] = func_6632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6656 = relay.var("var_6656", dtype = "int16", shape = (10, 5, 14))#candidate|6656|(10, 5, 14)|var|int16
var_6657 = relay.var("var_6657", dtype = "int16", shape = (10, 5, 14))#candidate|6657|(10, 5, 14)|var|int16
bop_6658 = relay.bitwise_or(var_6656.astype('int16'), relay.reshape(var_6657.astype('int16'), relay.shape_of(var_6656))) # shape=(10, 5, 14)
output = bop_6658
output2 = bop_6658
func_6664 = relay.Function([var_6656,var_6657,], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
var_6665 = relay.var("var_6665", dtype = "int16", shape = (10, 5, 14))#candidate|6665|(10, 5, 14)|var|int16
var_6666 = relay.var("var_6666", dtype = "int16", shape = (10, 5, 14))#candidate|6666|(10, 5, 14)|var|int16
output = func_6664(var_6665,var_6666,)
func_6667 = relay.Function([var_6665,var_6666,], output)
mutated_mod['func_6667'] = func_6667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
call_6679 = relay.TupleGetItem(func_2999_call(), 0)
call_6680 = relay.TupleGetItem(func_3001_call(), 0)
func_3843_call = mod.get_global_var('func_3843')
func_3847_call = mutated_mod.get_global_var('func_3847')
const_6706 = relay.const([8.082489,-6.334935,6.142501,-4.849494,-0.424636,-7.229013,-1.742189,-6.973122,-1.176576,-2.283752,6.926435,0.637952,9.565769,-5.498549,-7.931919,-9.824461,-2.433979,6.890318,3.737140,2.318503,-1.958763,-7.632509,-3.563392,7.446331,-4.394755,-3.585994,4.985680,-6.382690,-6.632803,7.214712,-5.819147,-8.095697,9.951369,3.082900,3.491396,-8.871581,-1.647154,-4.344658,0.367514,9.873408,-2.228256,-7.255999,7.708771,-9.748490,4.615707,3.450509,5.086437,9.406842,5.815797,4.676822,7.565389,-5.010960,-4.991433,5.197143,-7.338606,-9.723708,-8.197679,-1.620668,8.974204,4.828403,3.191113,-9.582752,-6.977439,6.324501,-3.255572,-8.941444,-8.058128,-5.617325,8.935478,-3.817943,-6.731023,-0.101302,2.740796,2.953702,-9.228230,-2.890515,9.346466,-0.744619,-4.289832,9.576593,8.801097,-0.111956,-8.301651,-3.470118,-1.056317,-6.653991,5.583978,8.562157,4.480868,9.425804,3.402612,3.666729,9.828621,-1.158846,9.065909,-2.881930,5.528984,-0.450670,3.842739,-6.574972,-1.683329,3.808889,7.832281,-0.705309,9.698105,-3.131506,9.762419,9.939289,-2.934295,-0.084200,0.193070,-8.886194,-5.109993,-6.578629,2.537605,5.960407,2.514443,-2.431497,-3.557530,-9.732359,-0.714526,-0.299481,-8.168533,-1.147513,-8.766292,4.811115,-9.115350,-2.249881,-6.923422,-5.213777,0.822916,4.849475,-4.941954,-9.391091,0.671422,-3.343355,4.828774,1.897757,-9.568199,-9.798676,9.574470,-8.670162,5.673867,-7.454927,-0.332216,-1.506222,-8.401495,-4.540009,7.497473,7.808897,1.980626,-5.380044,9.142012,2.479612,-4.060964,-7.587622,8.415408,3.141309,3.408533,-0.351936,-7.229325,-6.512571,4.075690,-7.796568,6.173578,1.399945,6.431131,3.499868,5.841017,4.043945,2.392173,8.232089,-8.971350,9.245917,-9.363452,0.878187,-2.349763,-1.008316,2.189333,-8.511010,-6.497858,0.921827,-5.066961,-2.080786,6.953903,7.456491,9.701739,9.719511,6.863747,-0.556275,4.012511,-6.217302,9.627877,3.856834,4.852067,1.339206,5.210159,-8.314604,5.042034,3.978713,-4.787665,8.675335,-8.768830,5.878343,-0.664251,0.455098,-9.064072,8.526287,-1.394378,-5.737799,9.035820,-7.113991,-6.076319,-2.478693,8.457853,0.656139,-1.351042,-2.860254,2.309984,-3.424710,0.170001,1.329065,1.297911,0.068439,8.501794,-7.324928,7.086839,0.521247,8.358773,0.923120,-5.764270,-5.232847,-5.570454,2.065469,-3.371582,4.444144,4.559055,1.720991,9.041001,4.790775,-3.070691,7.617847,-1.035363,-2.645625,-2.337078,-7.672870,-9.388269,5.118175,0.253078,-4.693847,-0.304714,9.923377,1.209275,2.703958,8.283608,7.297382,-3.935020,6.778174,-3.844768,-8.976221,-7.337262,4.618568,6.837266,6.676176,5.450320,-2.448170,1.240884,6.406965,9.067633,7.805457,2.672793,-1.080809,-9.101299,-9.641970,2.571128,7.506573,-6.419839,-2.013561,-7.966643,-4.912736,-8.891847,7.813681,5.208555,-4.523798,1.232871,6.239404,-2.182807,-5.731341,-3.193114,4.936390,0.727823,8.582040,0.134069,8.297262,9.096668,3.789150,8.546446,0.877963,-4.551113,1.757012,8.888834,-8.540385,-0.772735,-2.582710,-1.100195,8.516497,6.948152,9.576509,-8.606387,-2.471645,-0.256259,3.737015,-2.185547,-9.418134,-0.475193,5.825341,6.778747,-0.046424,-8.577524,-3.691537,-7.466101,7.195197,-9.100418,2.372705,1.268165,-5.117518,3.670715,5.590557,-1.516027,-6.777096,0.656274,-7.912656,-3.532589,3.827318,-4.468485,3.313409,2.670595,-5.755137,8.886957,-4.682343,3.557394,-9.598327,6.790805,-4.981780,-6.615305,-6.570050,-9.973749,-0.274895,7.058675,-0.221665,4.482620,9.588702,-0.823930,-3.562490,2.165689,-7.699980,4.876078,9.722179,0.767875,-0.705400,0.119664,7.948276,1.095420,-6.176056,1.597241,-7.620727,-5.519405,1.556661,9.248067,-1.393315,7.326785,5.701115,8.425575,1.099919,3.915261,-9.972555,-8.643480,-0.893425,7.373827,1.850048,1.060523,9.100506,4.961273,-1.996017,-2.114576,6.746164,-4.827650,-4.297446,3.322160,-1.632516,8.648789,6.695235,-3.883640,-6.212816,-0.784000,2.266763,1.746042,8.117606,9.762346,-4.244064,-5.766797,3.741639,-4.192778,2.033091,5.549994,-6.492748,-8.790535,0.181206,-4.294644,4.943057,8.777492,-4.697722,8.209291,3.606134,-2.463428,4.671557,7.009174,9.966092,-6.473601,6.676748,-2.312752,2.291978,-6.343910,3.024615,-5.597056,5.285334,1.331201,-4.855110,-5.161466,-6.795696,4.492935,4.058463,-8.389546,4.120733,9.755211,5.859662,-8.178271,4.880408,4.861726,3.958308,9.610519,6.809317,0.775394,5.920537,3.562539,-3.157476,6.397895,2.119133,-7.796697,5.824788,4.682549,8.746970,3.103715,-4.594982,2.825871,-4.162898,4.944070,-3.798016,8.312692,-4.976923,5.571551,-9.054172,-9.350816,-7.480385,-6.891551,6.671415,-0.239897,9.139734,6.719128,-1.396037,-2.565906,4.760915,-5.663925,-8.699115,3.777268,-7.680465,8.971469,-9.479857,-1.724466,-6.262880,-8.682979,1.694090,-4.463694,-3.544814,-4.475681,-1.117996,1.156190,-1.469781,6.314355,2.585683,5.253451,6.090671,-4.246998,1.722749,8.376737,8.231929,6.204765,-6.102266,-4.310125,2.451498,-0.126163,1.475112,4.104300,3.578528], dtype = "float64")#candidate|6706|(504,)|const|float64
call_6705 = relay.TupleGetItem(func_3843_call(relay.reshape(const_6706.astype('float64'), [7, 9, 8]), relay.reshape(const_6706.astype('float64'), [7, 9, 8]), ), 0)
call_6707 = relay.TupleGetItem(func_3847_call(relay.reshape(const_6706.astype('float64'), [7, 9, 8]), relay.reshape(const_6706.astype('float64'), [7, 9, 8]), ), 0)
output = relay.Tuple([call_6679,call_6705,const_6706,])
output2 = relay.Tuple([call_6680,call_6707,const_6706,])
func_6709 = relay.Function([], output)
mod['func_6709'] = func_6709
mod = relay.transform.InferType()(mod)
output = func_6709()
func_6710 = relay.Function([], output)
mutated_mod['func_6710'] = func_6710
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6711 = relay.var("var_6711", dtype = "float32", shape = (13, 16, 7))#candidate|6711|(13, 16, 7)|var|float32
uop_6712 = relay.asinh(var_6711.astype('float32')) # shape=(13, 16, 7)
output = relay.Tuple([uop_6712,])
output2 = relay.Tuple([uop_6712,])
func_6714 = relay.Function([var_6711,], output)
mod['func_6714'] = func_6714
mod = relay.transform.InferType()(mod)
var_6715 = relay.var("var_6715", dtype = "float32", shape = (13, 16, 7))#candidate|6715|(13, 16, 7)|var|float32
output = func_6714(var_6715)
func_6716 = relay.Function([var_6715], output)
mutated_mod['func_6716'] = func_6716
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6721 = relay.const([[[-8.537568,-6.695077,0.981799,-6.380511,-2.828440,-4.444331,8.222602,-4.006067,1.612891,5.026744,1.778085,-8.236237,-3.430467,8.251512,9.194060,-8.688558]],[[9.981653,-2.057258,1.014890,7.313207,8.065810,-0.800548,-3.718268,-8.746248,-9.985783,1.820425,4.012859,8.565110,8.544740,-4.937158,7.937880,-4.213952]],[[3.883549,5.483851,0.117790,0.575802,5.526022,3.300941,-6.396074,3.696063,5.656807,-2.308801,-2.797712,3.861349,4.360360,-9.518492,-9.752975,6.352778]],[[1.224178,-0.319764,8.973077,9.199942,-5.380386,-0.218861,-8.103525,5.544740,-3.627924,-2.074528,0.509824,-5.764949,-4.541097,-1.989449,0.114226,-5.166091]],[[-5.704717,8.063876,-6.335431,-9.037246,0.774490,1.758368,9.467590,2.220492,1.685239,-5.531892,2.133567,2.494151,-1.670797,-8.748105,3.034846,-3.322910]],[[-9.826517,0.313102,7.967488,5.715752,-4.362068,-0.869677,5.451124,8.677546,-0.321341,-2.186475,-0.006587,0.349563,0.618057,-0.234234,-6.015919,-1.481702]],[[-3.697540,-1.148990,-6.495859,-8.466668,-7.875565,-5.329895,-0.504654,-5.228314,4.123786,4.021398,-5.926735,-8.840279,-4.424864,-2.894768,-9.687779,4.411613]],[[-4.011348,-8.059093,8.628460,4.850660,7.528242,-8.278305,2.807314,-1.031338,4.564373,-3.146351,-6.320117,4.973198,8.664538,-8.985450,-9.016774,-9.487124]],[[0.679175,4.857297,2.206270,-4.505962,-6.791387,7.727354,-7.840555,3.571154,1.818791,8.202656,-1.414412,-1.378061,1.638069,1.531182,9.843028,-7.453794]],[[-2.222332,6.391231,7.782541,6.467327,-7.841008,5.364276,-8.709108,-4.686432,9.497215,-0.522308,-3.200394,6.915122,0.065639,-2.528322,1.358336,7.385549]],[[-8.654558,8.683684,-8.726105,-6.004377,8.133460,9.073038,-5.944545,9.124553,-3.358100,7.929044,2.067172,-6.829239,-2.751125,8.097798,7.159637,2.617315]],[[6.490062,3.657641,6.547188,5.717381,-4.254207,2.451135,-1.353134,-1.130319,-2.996854,-6.669184,-5.227582,-9.453087,4.197715,-4.781942,-7.743513,-9.102673]],[[4.440185,5.631739,7.269676,5.434177,-8.492588,-6.161462,-8.953492,5.253164,0.395202,-8.837581,-6.151371,-9.812632,-8.684374,-9.929257,-7.377422,-0.842090]]], dtype = "float32")#candidate|6721|(13, 1, 16)|const|float32
uop_6722 = relay.log(const_6721.astype('float32')) # shape=(13, 1, 16)
output = relay.Tuple([uop_6722,])
output2 = relay.Tuple([uop_6722,])
func_6729 = relay.Function([], output)
mod['func_6729'] = func_6729
mod = relay.transform.InferType()(mod)
mutated_mod['func_6729'] = func_6729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6729_call = mutated_mod.get_global_var('func_6729')
call_6730 = func_6729_call()
output = call_6730
func_6731 = relay.Function([], output)
mutated_mod['func_6731'] = func_6731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6777 = relay.var("var_6777", dtype = "int32", shape = ())#candidate|6777|()|var|int32
var_6778 = relay.var("var_6778", dtype = "int32", shape = (15, 2, 2))#candidate|6778|(15, 2, 2)|var|int32
bop_6779 = relay.greater(var_6777.astype('bool'), var_6778.astype('bool')) # shape=(15, 2, 2)
output = bop_6779
output2 = bop_6779
func_6782 = relay.Function([var_6777,var_6778,], output)
mod['func_6782'] = func_6782
mod = relay.transform.InferType()(mod)
var_6783 = relay.var("var_6783", dtype = "int32", shape = ())#candidate|6783|()|var|int32
var_6784 = relay.var("var_6784", dtype = "int32", shape = (15, 2, 2))#candidate|6784|(15, 2, 2)|var|int32
output = func_6782(var_6783,var_6784,)
func_6785 = relay.Function([var_6783,var_6784,], output)
mutated_mod['func_6785'] = func_6785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2954_call = mod.get_global_var('func_2954')
func_2956_call = mutated_mod.get_global_var('func_2956')
call_6791 = func_2954_call()
call_6792 = func_2954_call()
output = call_6791
output2 = call_6792
func_6821 = relay.Function([], output)
mod['func_6821'] = func_6821
mod = relay.transform.InferType()(mod)
output = func_6821()
func_6822 = relay.Function([], output)
mutated_mod['func_6822'] = func_6822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1820_call = mod.get_global_var('func_1820')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_6840 = relay.TupleGetItem(func_1820_call(), 0)
call_6841 = relay.TupleGetItem(func_1822_call(), 0)
func_2388_call = mod.get_global_var('func_2388')
func_2391_call = mutated_mod.get_global_var('func_2391')
var_6852 = relay.var("var_6852", dtype = "float32", shape = (840,))#candidate|6852|(840,)|var|float32
call_6851 = relay.TupleGetItem(func_2388_call(relay.reshape(var_6852.astype('float32'), [12, 10, 7]), relay.reshape(var_6852.astype('float32'), [12, 10, 7]), ), 6)
call_6853 = relay.TupleGetItem(func_2391_call(relay.reshape(var_6852.astype('float32'), [12, 10, 7]), relay.reshape(var_6852.astype('float32'), [12, 10, 7]), ), 6)
func_5332_call = mod.get_global_var('func_5332')
func_5335_call = mutated_mod.get_global_var('func_5335')
call_6858 = relay.TupleGetItem(func_5332_call(relay.reshape(call_6851.astype('uint64'), [7, 5, 14])), 0)
call_6859 = relay.TupleGetItem(func_5335_call(relay.reshape(call_6851.astype('uint64'), [7, 5, 14])), 0)
output = relay.Tuple([call_6840,call_6851,var_6852,call_6858,])
output2 = relay.Tuple([call_6841,call_6853,var_6852,call_6859,])
func_6864 = relay.Function([var_6852,], output)
mod['func_6864'] = func_6864
mod = relay.transform.InferType()(mod)
var_6865 = relay.var("var_6865", dtype = "float32", shape = (840,))#candidate|6865|(840,)|var|float32
output = func_6864(var_6865)
func_6866 = relay.Function([var_6865], output)
mutated_mod['func_6866'] = func_6866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4963_call = mod.get_global_var('func_4963')
func_4965_call = mutated_mod.get_global_var('func_4965')
call_6881 = relay.TupleGetItem(func_4963_call(), 2)
call_6882 = relay.TupleGetItem(func_4965_call(), 2)
func_2999_call = mod.get_global_var('func_2999')
func_3001_call = mutated_mod.get_global_var('func_3001')
call_6917 = relay.TupleGetItem(func_2999_call(), 1)
call_6918 = relay.TupleGetItem(func_3001_call(), 1)
output = relay.Tuple([call_6881,call_6917,])
output2 = relay.Tuple([call_6882,call_6918,])
func_6933 = relay.Function([], output)
mod['func_6933'] = func_6933
mod = relay.transform.InferType()(mod)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6933_call = mutated_mod.get_global_var('func_6933')
call_6934 = func_6933_call()
output = call_6934
func_6935 = relay.Function([], output)
mutated_mod['func_6935'] = func_6935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6972 = relay.var("var_6972", dtype = "float32", shape = (11, 10))#candidate|6972|(11, 10)|var|float32
uop_6973 = relay.tan(var_6972.astype('float32')) # shape=(11, 10)
output = uop_6973
output2 = uop_6973
F = relay.Function([var_6972,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_6972,], output2)
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
