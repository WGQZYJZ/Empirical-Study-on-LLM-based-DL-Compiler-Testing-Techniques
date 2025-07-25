import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_180 = relay.const([[[-8,-7,-5,-2,1,-8],[-9,-4,-8,-4,5,-4],[-7,-5,7,-4,-8,5]],[[-5,2,1,3,-7,-10],[7,5,9,4,4,-5],[-5,-5,-2,-8,9,5]],[[4,-1,-6,-5,-2,-8],[-10,1,2,-3,4,3],[10,5,3,-1,-1,-5]],[[-3,1,-9,-8,-1,-2],[-6,-3,-5,-8,-8,-4],[6,-6,-8,-3,1,6]]], dtype = "int8")#candidate|180|(4, 3, 6)|const|int8
var_181 = relay.var("var_181", dtype = "int8", shape = (4, 3, 6))#candidate|181|(4, 3, 6)|var|int8
bop_182 = relay.minimum(const_180.astype('int8'), relay.reshape(var_181.astype('int8'), relay.shape_of(const_180))) # shape=(4, 3, 6)
output = relay.Tuple([bop_182,])
output2 = relay.Tuple([bop_182,])
func_202 = relay.Function([var_181,], output)
mod['func_202'] = func_202
mod = relay.transform.InferType()(mod)
mutated_mod['func_202'] = func_202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_203 = relay.var("var_203", dtype = "int8", shape = (4, 3, 6))#candidate|203|(4, 3, 6)|var|int8
func_202_call = mutated_mod.get_global_var('func_202')
call_204 = func_202_call(var_203)
output = call_204
func_205 = relay.Function([var_203], output)
mutated_mod['func_205'] = func_205
mutated_mod = relay.transform.InferType()(mutated_mod)
const_207 = relay.const([[[9.183613,4.162676],[7.052758,7.673026]]], dtype = "float32")#candidate|207|(1, 2, 2)|const|float32
uop_208 = relay.sinh(const_207.astype('float32')) # shape=(1, 2, 2)
output = uop_208
output2 = uop_208
func_210 = relay.Function([], output)
mod['func_210'] = func_210
mod = relay.transform.InferType()(mod)
mutated_mod['func_210'] = func_210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mutated_mod.get_global_var('func_210')
call_211 = func_210_call()
output = call_211
func_212 = relay.Function([], output)
mutated_mod['func_212'] = func_212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_223 = func_210_call()
call_224 = func_210_call()
func_202_call = mod.get_global_var('func_202')
func_205_call = mutated_mod.get_global_var('func_205')
const_236 = relay.const([-4,-3,4,2,7,8,-8,-7,7,7,-5,6,4,7,9,-5,2,-3,10,-10,-1,-2,-1,5,-4,-9,5,-4,-1,4,4,4,9,-4,-3,9,-3,6,-1,-1,3,3,-5,7,-9,-7,4,9,-9,2,7,9,-2,3,3,-8,6,-4,-8,9,4,10,-7,1,4,-9,5,-1,10,2,-2,2], dtype = "int8")#candidate|236|(72,)|const|int8
call_235 = relay.TupleGetItem(func_202_call(relay.reshape(const_236.astype('int8'), [4, 3, 6])), 0)
call_237 = relay.TupleGetItem(func_205_call(relay.reshape(const_236.astype('int8'), [4, 3, 6])), 0)
output = relay.Tuple([call_223,call_235,const_236,])
output2 = relay.Tuple([call_224,call_237,const_236,])
func_245 = relay.Function([], output)
mod['func_245'] = func_245
mod = relay.transform.InferType()(mod)
output = func_245()
func_246 = relay.Function([], output)
mutated_mod['func_246'] = func_246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_271 = func_210_call()
call_272 = func_210_call()
const_281 = relay.const([[[-5.310996,4.401871],[-6.796451,-9.482072]],[[-3.153712,-2.792582],[-2.110592,9.990396]],[[-1.579276,-7.824256],[-7.796732,-9.059550]],[[-2.955345,0.591629],[1.739323,7.471310]]], dtype = "float32")#candidate|281|(4, 2, 2)|const|float32
bop_282 = relay.logical_xor(call_271.astype('uint16'), const_281.astype('uint16')) # shape=(4, 2, 2)
bop_285 = relay.logical_xor(call_272.astype('uint16'), const_281.astype('uint16')) # shape=(4, 2, 2)
output = relay.Tuple([bop_282,])
output2 = relay.Tuple([bop_285,])
func_290 = relay.Function([], output)
mod['func_290'] = func_290
mod = relay.transform.InferType()(mod)
output = func_290()
func_291 = relay.Function([], output)
mutated_mod['func_291'] = func_291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_310 = relay.TupleGetItem(func_290_call(), 0)
call_311 = relay.TupleGetItem(func_291_call(), 0)
output = relay.Tuple([call_310,])
output2 = relay.Tuple([call_311,])
func_314 = relay.Function([], output)
mod['func_314'] = func_314
mod = relay.transform.InferType()(mod)
output = func_314()
func_315 = relay.Function([], output)
mutated_mod['func_315'] = func_315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_373 = relay.TupleGetItem(func_314_call(), 0)
call_374 = relay.TupleGetItem(func_315_call(), 0)
const_378 = relay.const([[[-10,2],[-3,8]],[[-6,9],[4,5]],[[6,-9],[4,-6]],[[2,3],[-5,-3]]], dtype = "uint16")#candidate|378|(4, 2, 2)|const|uint16
bop_379 = relay.not_equal(call_373.astype('bool'), relay.reshape(const_378.astype('bool'), relay.shape_of(call_373))) # shape=(4, 2, 2)
bop_382 = relay.not_equal(call_374.astype('bool'), relay.reshape(const_378.astype('bool'), relay.shape_of(call_374))) # shape=(4, 2, 2)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_383 = func_210_call()
call_384 = func_210_call()
func_245_call = mod.get_global_var('func_245')
func_246_call = mutated_mod.get_global_var('func_246')
call_390 = relay.TupleGetItem(func_245_call(), 0)
call_391 = relay.TupleGetItem(func_246_call(), 0)
output = relay.Tuple([bop_379,call_383,call_390,])
output2 = relay.Tuple([bop_382,call_384,call_391,])
func_401 = relay.Function([], output)
mod['func_401'] = func_401
mod = relay.transform.InferType()(mod)
output = func_401()
func_402 = relay.Function([], output)
mutated_mod['func_402'] = func_402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_431 = relay.TupleGetItem(func_314_call(), 0)
call_432 = relay.TupleGetItem(func_315_call(), 0)
output = call_431
output2 = call_432
func_437 = relay.Function([], output)
mod['func_437'] = func_437
mod = relay.transform.InferType()(mod)
output = func_437()
func_438 = relay.Function([], output)
mutated_mod['func_438'] = func_438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_462 = func_210_call()
call_463 = func_210_call()
const_465 = relay.const([[[5.018979,3.334282],[-6.635259,-9.175061]],[[0.077504,9.037011],[6.378152,-0.381973]],[[-7.313209,1.042827],[5.837866,0.939089]],[[-5.066277,-1.314974],[8.764596,-5.648513]],[[-0.500056,9.932681],[9.537991,-4.140297]],[[-6.172500,4.139104],[0.102762,-9.301449]]], dtype = "float32")#candidate|465|(6, 2, 2)|const|float32
bop_466 = relay.left_shift(call_462.astype('int16'), const_465.astype('int16')) # shape=(6, 2, 2)
bop_469 = relay.left_shift(call_463.astype('int16'), const_465.astype('int16')) # shape=(6, 2, 2)
output = relay.Tuple([bop_466,])
output2 = relay.Tuple([bop_469,])
func_475 = relay.Function([], output)
mod['func_475'] = func_475
mod = relay.transform.InferType()(mod)
mutated_mod['func_475'] = func_475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_475_call = mutated_mod.get_global_var('func_475')
call_476 = func_475_call()
output = call_476
func_477 = relay.Function([], output)
mutated_mod['func_477'] = func_477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_528 = func_210_call()
call_529 = func_210_call()
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_544 = relay.TupleGetItem(func_401_call(), 1)
call_545 = relay.TupleGetItem(func_402_call(), 1)
output = relay.Tuple([call_528,call_544,])
output2 = relay.Tuple([call_529,call_545,])
func_547 = relay.Function([], output)
mod['func_547'] = func_547
mod = relay.transform.InferType()(mod)
output = func_547()
func_548 = relay.Function([], output)
mutated_mod['func_548'] = func_548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_588 = relay.TupleGetItem(func_290_call(), 0)
call_589 = relay.TupleGetItem(func_291_call(), 0)
output = call_588
output2 = call_589
func_590 = relay.Function([], output)
mod['func_590'] = func_590
mod = relay.transform.InferType()(mod)
mutated_mod['func_590'] = func_590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mutated_mod.get_global_var('func_590')
call_591 = func_590_call()
output = call_591
func_592 = relay.Function([], output)
mutated_mod['func_592'] = func_592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_598 = relay.TupleGetItem(func_290_call(), 0)
call_599 = relay.TupleGetItem(func_291_call(), 0)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_607 = relay.TupleGetItem(func_401_call(), 2)
call_608 = relay.TupleGetItem(func_402_call(), 2)
uop_613 = relay.log10(call_607.astype('float64')) # shape=(1, 2, 2)
uop_615 = relay.log10(call_608.astype('float64')) # shape=(1, 2, 2)
output = relay.Tuple([call_598,uop_613,])
output2 = relay.Tuple([call_599,uop_615,])
func_629 = relay.Function([], output)
mod['func_629'] = func_629
mod = relay.transform.InferType()(mod)
mutated_mod['func_629'] = func_629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_629_call = mutated_mod.get_global_var('func_629')
call_630 = func_629_call()
output = call_630
func_631 = relay.Function([], output)
mutated_mod['func_631'] = func_631
mutated_mod = relay.transform.InferType()(mutated_mod)
const_634 = relay.const(10, dtype = "int32")#candidate|634|()|const|int32
const_635 = relay.const([[[-1,1,-8,-1,6,-2,6,-3,10,-2,-9,8,-7,2],[5,8,-7,-1,7,7,-7,-10,-10,-5,7,7,-4,-5],[9,2,1,10,-2,4,-3,5,-1,5,10,-4,-7,-4],[-5,9,6,7,-5,7,10,-7,4,4,-6,9,-1,4],[3,9,7,-3,1,-2,9,-4,-1,-5,-4,2,-10,-8],[1,8,-10,-5,5,1,8,-4,5,7,2,2,-10,8],[3,-2,-9,-2,7,7,-5,-10,4,-9,4,4,9,4],[8,1,9,10,6,-7,9,-7,-2,7,-4,4,4,4],[2,3,9,5,-9,-7,9,10,-10,4,7,-8,10,9],[-8,7,10,-1,-6,-8,-3,2,9,-10,10,-10,5,-7]],[[2,9,8,3,6,10,2,6,5,7,-9,-4,3,5],[-4,3,8,-9,7,-8,-5,6,-8,-3,2,6,9,10],[4,9,10,7,3,-8,-5,5,7,-7,6,8,2,-7],[4,10,-5,-9,1,4,-9,6,7,5,-3,-8,4,6],[10,6,3,3,7,2,5,1,6,-9,9,8,-6,-2],[2,6,-1,7,10,-9,-1,4,7,-3,5,8,6,7],[-2,-4,-8,10,3,-1,-7,-10,3,8,1,5,-3,-9],[8,-1,-6,-9,-5,4,-6,3,-7,-4,8,4,-1,-5],[-1,3,2,-4,-1,5,-1,6,-3,-1,-3,-3,-6,2],[6,-4,-4,10,5,6,-8,1,-7,-7,7,3,4,1]],[[-4,1,-2,9,-4,-2,5,-4,-9,2,-2,-8,-10,9],[6,-6,-4,-10,-2,2,10,-4,4,-7,2,10,-10,-5],[9,2,5,-8,5,-7,1,-2,3,-5,3,-1,1,1],[10,-10,1,8,2,-4,8,-3,-1,9,2,-3,5,-1],[5,-8,9,6,3,-5,10,3,1,6,-2,5,8,-8],[2,-1,-3,-2,8,2,9,-8,7,8,9,7,10,7],[10,3,7,8,5,-4,-7,-8,-6,-7,10,-10,-3,2],[10,3,7,1,2,-7,9,-3,10,3,8,8,7,-6],[-6,6,-10,-6,-5,-2,-6,5,2,2,-9,-7,-6,2],[-6,6,9,-8,8,-5,-8,-1,7,2,4,-9,-10,10]],[[5,9,-2,-1,-6,-9,10,-9,-2,7,-6,7,2,3],[-4,7,-6,-9,3,9,-1,-6,-4,-3,5,4,-8,1],[8,-1,-8,-2,-7,3,4,-7,-2,-6,-8,-3,-9,-4],[7,-7,1,7,-8,-4,-1,3,2,-10,3,-1,7,3],[10,-2,-5,1,-9,-7,-9,-10,-9,8,4,-6,-6,-9],[-4,10,2,-10,-3,2,1,-6,2,3,-2,-5,-10,3],[-1,-10,7,-6,4,-3,-10,6,4,-2,-2,10,-7,-10],[5,3,-8,-8,3,-1,1,-1,-8,-4,10,1,-2,-6],[3,4,-1,-3,-9,1,6,-10,-5,9,9,10,-9,3],[-9,8,5,1,10,5,4,3,10,-6,-4,10,6,3]],[[10,-5,-7,2,-9,-9,4,8,10,5,-5,-4,-6,2],[-6,-7,3,5,7,3,8,-6,-6,10,8,-7,-8,1],[7,6,-10,-10,-7,4,-2,-1,-9,-5,-3,-2,-2,-5],[-1,-6,2,4,7,7,-10,-7,8,-3,4,3,-2,-10],[5,9,-2,2,9,5,1,9,5,-2,-5,-1,4,8],[-10,-4,-2,8,-8,-7,10,4,-6,-1,-10,-3,9,-5],[9,-2,-2,5,-9,-7,5,5,-5,-5,1,-1,10,-7],[-9,5,-6,6,-3,-3,4,-9,-3,6,-1,-1,8,5],[-8,-8,-7,-5,-10,-2,-2,3,-4,-8,-7,6,-7,2],[1,-5,2,-5,6,3,-1,-7,9,-10,4,-9,-4,9]],[[-4,-7,8,3,5,10,-6,-5,7,1,-4,6,-10,-9],[10,6,-6,-8,-4,6,-8,9,9,-2,-8,2,-3,9],[5,-8,5,8,4,6,8,-7,8,2,-4,6,7,-5],[6,4,4,-8,-3,-10,2,-6,10,7,-3,-7,-3,-8],[-9,-1,-9,-8,-6,-1,3,-9,-7,-5,10,7,1,2],[-5,4,-5,10,-1,-6,5,7,9,4,3,-5,1,8],[-3,8,1,1,9,10,2,-9,3,6,2,-8,-9,-7],[4,-2,6,-5,2,-6,9,-10,-4,-7,-5,-9,-3,3],[9,-2,-7,-9,6,3,10,-8,-5,-10,-9,6,-4,-2],[-1,8,-7,4,-5,-1,7,-9,-3,-7,-9,-7,-8,2]],[[-7,8,1,1,-6,-4,-8,-4,-8,5,1,-10,-3,-9],[-8,-2,5,-5,7,4,1,-6,2,-5,2,2,3,4],[-8,8,3,-3,1,-5,-3,2,7,-4,-8,1,-10,5],[-4,-1,1,-8,-9,-3,10,1,-6,-7,2,2,-2,-2],[-6,8,-6,-2,-8,3,1,10,-5,5,5,-4,5,7],[-9,-2,7,-4,-8,-2,-7,6,1,9,6,-7,8,-7],[7,2,4,10,-3,4,1,2,1,7,-3,-7,-2,1],[6,-3,-4,7,-9,9,3,7,-1,3,-6,-3,-9,-9],[5,-9,8,3,8,-1,-9,3,6,-6,-9,-7,1,4],[-10,-1,3,-7,-3,-4,-10,-10,-7,-1,-2,-10,-9,-4]],[[8,-2,-2,-5,-4,-9,-3,-10,10,-2,-2,10,3,5],[-10,2,-10,8,7,7,6,-8,9,-1,-7,-5,-9,5],[8,2,2,8,10,1,7,-1,-6,-1,-9,5,5,-9],[7,-6,5,-5,-4,8,-6,5,9,-8,7,9,10,-3],[3,1,5,7,5,-8,6,5,7,7,6,-10,-3,-8],[-4,-9,-5,9,8,-2,1,-4,-6,-8,8,8,1,8],[10,6,-9,2,-7,-5,-8,-10,7,-3,2,7,-7,8],[6,1,-2,-7,-3,-6,-10,7,-8,-7,10,9,3,6],[2,7,7,-3,4,1,-10,8,-6,10,-2,8,-8,6],[6,9,-5,7,4,-1,9,-4,9,-9,-8,8,5,-4]],[[6,4,3,9,2,7,5,2,2,-2,-9,5,-9,9],[-2,7,-6,-9,4,4,5,10,3,-3,-10,-5,4,-8],[4,7,4,-5,6,-7,3,6,7,7,10,3,5,-8],[-10,3,6,2,-5,10,1,2,1,4,-6,7,1,7],[-10,4,-3,-3,-7,1,-10,-3,-10,-6,5,-10,9,8],[-7,-5,-1,-4,5,5,10,6,-9,-2,-6,-2,8,-3],[-9,-8,-7,3,3,-2,7,-2,5,9,-9,-5,-1,5],[8,6,-8,-4,-9,-2,-6,-3,-4,-2,-5,3,3,-8],[-4,4,2,9,-6,4,4,10,-2,5,-7,3,9,3],[-5,-8,5,-10,4,6,6,7,-8,2,-7,-4,-3,6]]], dtype = "int32")#candidate|635|(9, 10, 14)|const|int32
bop_636 = relay.not_equal(const_634.astype('bool'), const_635.astype('bool')) # shape=(9, 10, 14)
output = relay.Tuple([bop_636,])
output2 = relay.Tuple([bop_636,])
func_643 = relay.Function([], output)
mod['func_643'] = func_643
mod = relay.transform.InferType()(mod)
mutated_mod['func_643'] = func_643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_643_call = mutated_mod.get_global_var('func_643')
call_644 = func_643_call()
output = call_644
func_645 = relay.Function([], output)
mutated_mod['func_645'] = func_645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_547_call = mod.get_global_var('func_547')
func_548_call = mutated_mod.get_global_var('func_548')
call_661 = relay.TupleGetItem(func_547_call(), 1)
call_662 = relay.TupleGetItem(func_548_call(), 1)
var_671 = relay.var("var_671", dtype = "float32", shape = (11, 2, 2))#candidate|671|(11, 2, 2)|var|float32
bop_672 = relay.less(call_661.astype('bool'), var_671.astype('bool')) # shape=(11, 2, 2)
bop_675 = relay.less(call_662.astype('bool'), var_671.astype('bool')) # shape=(11, 2, 2)
uop_678 = relay.cos(bop_672.astype('float64')) # shape=(11, 2, 2)
uop_680 = relay.cos(bop_675.astype('float64')) # shape=(11, 2, 2)
output = uop_678
output2 = uop_680
func_681 = relay.Function([var_671,], output)
mod['func_681'] = func_681
mod = relay.transform.InferType()(mod)
mutated_mod['func_681'] = func_681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_682 = relay.var("var_682", dtype = "float32", shape = (11, 2, 2))#candidate|682|(11, 2, 2)|var|float32
func_681_call = mutated_mod.get_global_var('func_681')
call_683 = func_681_call(var_682)
output = call_683
func_684 = relay.Function([var_682], output)
mutated_mod['func_684'] = func_684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mod.get_global_var('func_590')
func_592_call = mutated_mod.get_global_var('func_592')
call_709 = func_590_call()
call_710 = func_590_call()
func_437_call = mod.get_global_var('func_437')
func_438_call = mutated_mod.get_global_var('func_438')
call_732 = func_437_call()
call_733 = func_437_call()
output = relay.Tuple([call_709,call_732,])
output2 = relay.Tuple([call_710,call_733,])
func_738 = relay.Function([], output)
mod['func_738'] = func_738
mod = relay.transform.InferType()(mod)
output = func_738()
func_739 = relay.Function([], output)
mutated_mod['func_739'] = func_739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_751 = func_210_call()
call_752 = func_210_call()
func_643_call = mod.get_global_var('func_643')
func_645_call = mutated_mod.get_global_var('func_645')
call_758 = relay.TupleGetItem(func_643_call(), 0)
call_759 = relay.TupleGetItem(func_645_call(), 0)
output = relay.Tuple([call_751,call_758,])
output2 = relay.Tuple([call_752,call_759,])
func_782 = relay.Function([], output)
mod['func_782'] = func_782
mod = relay.transform.InferType()(mod)
output = func_782()
func_783 = relay.Function([], output)
mutated_mod['func_783'] = func_783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
call_790 = relay.TupleGetItem(func_475_call(), 0)
call_791 = relay.TupleGetItem(func_477_call(), 0)
func_643_call = mod.get_global_var('func_643')
func_645_call = mutated_mod.get_global_var('func_645')
call_794 = relay.TupleGetItem(func_643_call(), 0)
call_795 = relay.TupleGetItem(func_645_call(), 0)
var_804 = relay.var("var_804", dtype = "bool", shape = (9, 10, 14))#candidate|804|(9, 10, 14)|var|bool
bop_805 = relay.less(call_794.astype('bool'), relay.reshape(var_804.astype('bool'), relay.shape_of(call_794))) # shape=(9, 10, 14)
bop_808 = relay.less(call_795.astype('bool'), relay.reshape(var_804.astype('bool'), relay.shape_of(call_795))) # shape=(9, 10, 14)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_812 = relay.TupleGetItem(func_314_call(), 0)
call_813 = relay.TupleGetItem(func_315_call(), 0)
output = relay.Tuple([call_790,bop_805,call_812,])
output2 = relay.Tuple([call_791,bop_808,call_813,])
func_822 = relay.Function([var_804,], output)
mod['func_822'] = func_822
mod = relay.transform.InferType()(mod)
mutated_mod['func_822'] = func_822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_823 = relay.var("var_823", dtype = "bool", shape = (9, 10, 14))#candidate|823|(9, 10, 14)|var|bool
func_822_call = mutated_mod.get_global_var('func_822')
call_824 = func_822_call(var_823)
output = call_824
func_825 = relay.Function([var_823], output)
mutated_mod['func_825'] = func_825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_839 = relay.TupleGetItem(func_290_call(), 0)
call_840 = relay.TupleGetItem(func_291_call(), 0)
uop_845 = relay.rsqrt(call_839.astype('float64')) # shape=(4, 2, 2)
uop_847 = relay.rsqrt(call_840.astype('float64')) # shape=(4, 2, 2)
output = relay.Tuple([uop_845,])
output2 = relay.Tuple([uop_847,])
func_861 = relay.Function([], output)
mod['func_861'] = func_861
mod = relay.transform.InferType()(mod)
mutated_mod['func_861'] = func_861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mutated_mod.get_global_var('func_861')
call_862 = func_861_call()
output = call_862
func_863 = relay.Function([], output)
mutated_mod['func_863'] = func_863
mutated_mod = relay.transform.InferType()(mutated_mod)
const_873 = relay.const([[[-8.352757,-5.680091,-3.602180,4.818670,1.782589,-3.518407,-4.583227,0.554871],[4.478235,-6.307564,-3.257261,3.371000,2.148579,-7.541670,8.122307,6.539318],[0.566069,-0.989125,-4.494687,-6.788106,5.094329,3.704801,-4.519739,-1.337662],[9.050639,0.994425,0.058110,-4.273732,7.932268,8.712531,-0.906737,-3.938283],[-5.641560,9.381460,-1.394679,-3.837303,1.905897,5.513374,-4.108690,0.626653],[-2.579581,-3.462556,9.231680,-1.114985,1.969272,-1.932135,-1.192865,9.876693],[3.617904,-7.534506,-6.136842,8.103410,-0.504344,-1.696976,4.810805,-4.699808],[-8.650654,6.676449,-8.493025,-8.214254,6.145021,5.335813,1.875126,8.770883],[-5.875384,-5.025188,-0.582990,-2.634535,5.608386,-6.999558,-7.163722,-4.629005],[7.640639,2.001913,-2.797928,9.613830,-1.972978,1.913291,7.078157,-4.304762],[-5.705748,8.626632,3.879926,-4.076984,-3.603732,4.072586,0.482052,6.695238],[6.787614,-8.344955,8.037674,-9.763337,0.476954,6.989111,-7.945865,-0.366805]],[[5.516188,3.910143,1.476452,2.696215,-7.074243,-5.325191,-0.763220,-9.665041],[-4.690690,5.755181,-6.972461,7.317617,-9.452645,5.898164,7.994116,2.303792],[1.014732,4.151652,-6.565627,-0.849517,3.412471,9.321300,-5.069347,2.841101],[-9.782047,-6.177280,-1.055915,-1.386882,6.256483,0.182692,1.195938,7.139244],[-9.286433,4.774670,6.381169,6.855603,5.587102,-8.792618,4.294810,-3.459887],[3.740672,-4.702834,8.077580,-8.056582,-7.856937,1.341420,-8.032526,-7.080960],[4.590732,-6.432608,1.748246,0.514524,-2.324880,3.740762,3.166125,5.243514],[-1.282884,6.446646,0.711953,-8.247380,6.426486,6.236351,-1.110095,-9.962848],[-1.627648,-4.917721,6.424306,-5.216801,-6.063754,4.543855,0.535210,-5.431456],[-0.378145,7.480861,6.776533,-8.405568,2.825776,-2.518252,8.065602,5.829381],[5.819559,-9.980362,6.335952,-2.803206,-2.313140,-8.214799,0.593874,8.999805],[-1.771345,2.638193,1.069589,-1.439279,7.590285,-6.540945,-1.567292,-7.083724]],[[-4.152743,-8.765694,7.325905,8.871903,-4.190063,-4.841304,-0.633260,9.228238],[-6.343750,-0.606281,-7.456675,4.631576,6.562624,2.122910,1.161642,-0.272850],[-1.104924,-8.370038,6.885064,8.144535,7.109617,9.331231,3.715459,-7.069024],[6.054569,3.292497,3.930828,-3.483531,8.132863,-4.173420,7.111662,-4.812238],[4.159338,-3.414379,-6.922939,-3.456215,8.577821,5.848227,1.195649,-1.405133],[-2.293114,-1.883787,-2.002626,-3.731173,-4.941700,7.653428,2.203230,6.010372],[-3.322190,-8.931923,6.320170,-5.192397,-5.613042,-2.920553,3.518402,5.917005],[-9.531991,0.928945,-5.996747,-3.143074,0.259582,-4.255505,7.551800,0.221847],[5.548015,-1.674031,8.647459,2.438915,-8.338716,0.319206,0.972296,1.181592],[-8.472746,-9.047766,9.569031,-9.784055,-4.274607,9.361354,-0.693425,8.853766],[-2.291356,5.155228,-9.458370,-0.332245,-0.103993,-3.906240,-5.684827,4.748109],[2.590006,4.153885,9.283345,1.711649,-8.478861,2.064754,1.918013,9.172857]],[[4.966333,6.495561,3.307296,-6.390145,1.826218,2.191950,1.267891,7.222301],[1.131499,5.304145,-2.308147,-5.023293,2.775377,0.180218,0.255685,7.736411],[6.548983,-0.980083,-5.404025,-2.295664,-1.608285,9.144893,0.089140,-9.591729],[4.610986,9.338219,-1.574496,-7.100127,5.519078,-4.928842,-5.696387,9.793392],[6.019949,6.563862,0.324061,2.816114,1.105881,6.198524,4.671057,2.007489],[6.521354,-2.245243,1.272574,7.762327,8.424967,8.114944,2.194415,3.097746],[-9.369059,-2.441309,7.232220,2.979370,-8.817650,9.116894,-8.947509,-1.106197],[9.128263,8.162702,-9.978072,8.127575,8.276368,7.629792,-9.681694,1.486322],[0.939365,-5.773649,8.060467,-0.477657,-3.994109,-7.000356,-8.916948,-3.258308],[4.640507,-8.729862,-8.749669,1.768562,-9.057218,3.162178,-9.311944,-7.972590],[-9.521826,-3.275566,-2.807612,-2.487848,-1.454859,-0.754837,1.113909,-4.637344],[-4.898848,-0.611813,-8.826612,-2.853277,9.255000,7.460215,-7.243220,2.390169]],[[-0.758349,6.075326,-7.226419,8.012411,-5.910484,-0.084754,-4.005283,-8.870718],[5.196526,-2.106088,0.242283,5.743443,-6.703810,-3.484242,-6.473099,4.523761],[8.519564,9.386974,-1.708071,-2.849375,-9.515640,5.670558,4.882933,-3.408161],[-4.117385,-5.112262,6.369447,-6.149005,6.634066,6.857907,0.862285,-6.432838],[7.554724,-9.409972,5.170986,-0.097261,9.252978,-6.008152,5.663074,-3.174257],[2.925227,4.508145,-7.849689,-3.127081,-6.406745,1.353570,1.261740,-0.748192],[7.186253,-2.653572,6.271281,3.874605,-3.572311,9.083433,-4.917763,-7.669916],[2.733017,-8.025678,1.934242,5.576195,-0.952522,8.076427,-7.028614,-3.598043],[1.762010,-0.404188,6.828521,6.498363,-7.194916,-5.246733,-0.666490,-3.763709],[-3.027729,1.971995,-4.720265,-5.366886,8.976455,-6.212763,4.766217,-7.704373],[4.174877,-3.983964,-9.115356,1.481236,-4.549130,2.904437,-7.141676,-3.845156],[-0.813194,-2.218178,-3.790474,-1.979613,1.813675,-9.030276,1.345896,0.149169]],[[1.466395,-4.578023,2.136432,-0.653797,9.617199,0.848460,-5.372624,-3.178146],[9.696772,4.341309,8.465704,-6.088090,-9.547671,-8.971399,0.271432,-4.231334],[2.361514,-6.237780,-9.508132,-1.264163,-0.244465,9.244455,-6.546252,8.960084],[5.918126,8.533410,-8.029605,2.830538,-9.350120,6.378573,6.997287,8.577982],[-5.369320,2.251841,-9.169682,-0.555028,2.031669,8.176922,9.278896,-8.540209],[6.411148,-2.788183,7.329891,-4.656134,8.355279,0.225638,-7.637619,0.637218],[-4.261463,8.564313,-0.237242,0.234097,-8.207301,7.450148,1.853212,-1.981985],[-7.904906,2.629514,-3.031228,8.500142,2.277154,-5.867690,8.182234,-3.348273],[-8.430283,1.343570,0.785778,6.047095,4.599036,8.836086,-8.718953,-8.471369],[-6.978059,-8.962698,3.309657,-0.364890,-3.750664,-0.425080,-6.960723,8.945691],[2.777080,-3.919130,7.907509,-7.731418,-2.127771,1.574941,0.051239,5.451174],[8.907879,-2.462333,-9.161690,8.900179,4.374441,-1.861848,-0.197401,-4.839820]],[[-7.091127,-2.282530,-8.828318,7.879396,6.638508,2.059005,-5.335187,-0.940848],[-9.352870,-9.404446,-4.255028,9.454758,-2.956636,8.923094,4.509499,-9.422862],[-9.677281,6.195723,6.269401,-1.832831,-1.482908,3.227138,-9.468731,-5.866573],[-8.338842,6.327357,1.113083,-9.325669,3.465725,-9.618128,3.120746,-2.004089],[-6.524275,5.337748,-9.366312,-0.760568,3.056934,9.547572,4.276556,9.808712],[9.729920,-4.191489,4.015884,-7.064975,4.036132,-7.353943,0.034980,-9.562405],[-7.936802,7.060513,7.899412,5.067092,5.623746,1.985136,3.501793,-2.058707],[6.611713,8.458784,9.951448,3.923668,-5.547486,2.089995,4.955456,9.594584],[6.542649,-9.407805,-3.516920,-0.596274,0.458706,8.012679,-7.803931,3.301645],[-0.366101,-0.858564,-6.280348,-2.815052,5.882925,-1.545482,-5.158090,5.707524],[-2.534801,-7.339437,0.480772,-9.806874,-2.817550,3.440477,7.826991,3.584896],[6.247901,7.578243,2.958237,8.939097,4.208351,6.040734,3.364508,-5.985876]],[[8.720805,4.375887,6.584449,6.947350,2.710404,-9.536332,7.109895,-8.955323],[4.513358,-5.413021,-3.476529,-3.835939,7.637919,5.024170,-2.536424,-0.201542],[-8.081497,-1.159848,5.000706,-7.368615,8.231922,0.355246,-4.026103,1.437914],[2.591797,-0.525313,9.461479,6.160886,2.864908,-8.162538,-5.987437,4.049897],[-9.316993,-5.967901,3.136559,-8.422991,7.437400,9.233684,5.728624,-8.952125],[-6.895086,-5.067673,8.211030,-6.765824,-3.101430,-4.935122,5.936398,-2.782338],[9.875467,7.995507,6.627464,1.128048,1.718556,-2.021560,-8.330412,8.355672],[2.698077,-1.873190,3.451535,1.241701,6.446998,1.734041,8.712407,-7.662216],[-5.205262,3.636416,0.940990,7.987282,2.574270,-6.184687,-3.220193,-6.823788],[1.683981,-5.649792,0.341936,7.621756,1.273792,1.979393,-7.480157,9.211351],[6.758233,-9.439798,-9.883733,7.256175,9.394009,1.940090,4.273373,1.426273],[-2.390755,-1.918411,-4.657392,7.622504,-9.027293,-2.183034,-2.043230,8.908211]]], dtype = "float32")#candidate|873|(8, 12, 8)|const|float32
uop_874 = relay.asinh(const_873.astype('float32')) # shape=(8, 12, 8)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_881 = relay.TupleGetItem(func_401_call(), 1)
call_882 = relay.TupleGetItem(func_402_call(), 1)
func_629_call = mod.get_global_var('func_629')
func_631_call = mutated_mod.get_global_var('func_631')
call_893 = relay.TupleGetItem(func_629_call(), 0)
call_894 = relay.TupleGetItem(func_631_call(), 0)
output = relay.Tuple([uop_874,call_881,call_893,])
output2 = relay.Tuple([uop_874,call_882,call_894,])
func_898 = relay.Function([], output)
mod['func_898'] = func_898
mod = relay.transform.InferType()(mod)
output = func_898()
func_899 = relay.Function([], output)
mutated_mod['func_899'] = func_899
mutated_mod = relay.transform.InferType()(mutated_mod)
var_925 = relay.var("var_925", dtype = "float32", shape = (6, 15, 6))#candidate|925|(6, 15, 6)|var|float32
uop_926 = relay.asinh(var_925.astype('float32')) # shape=(6, 15, 6)
bop_928 = relay.left_shift(uop_926.astype('uint8'), relay.reshape(var_925.astype('uint8'), relay.shape_of(uop_926))) # shape=(6, 15, 6)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_933 = relay.TupleGetItem(func_401_call(), 2)
call_934 = relay.TupleGetItem(func_402_call(), 2)
output = relay.Tuple([bop_928,call_933,])
output2 = relay.Tuple([bop_928,call_934,])
func_941 = relay.Function([var_925,], output)
mod['func_941'] = func_941
mod = relay.transform.InferType()(mod)
var_942 = relay.var("var_942", dtype = "float32", shape = (6, 15, 6))#candidate|942|(6, 15, 6)|var|float32
output = func_941(var_942)
func_943 = relay.Function([var_942], output)
mutated_mod['func_943'] = func_943
mutated_mod = relay.transform.InferType()(mutated_mod)
var_959 = relay.var("var_959", dtype = "int16", shape = ())#candidate|959|()|var|int16
var_960 = relay.var("var_960", dtype = "int16", shape = (14, 5, 7))#candidate|960|(14, 5, 7)|var|int16
bop_961 = relay.bitwise_and(var_959.astype('int16'), var_960.astype('int16')) # shape=(14, 5, 7)
output = relay.Tuple([bop_961,])
output2 = relay.Tuple([bop_961,])
func_965 = relay.Function([var_959,var_960,], output)
mod['func_965'] = func_965
mod = relay.transform.InferType()(mod)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_965_call = mutated_mod.get_global_var('func_965')
var_967 = relay.var("var_967", dtype = "int16", shape = ())#candidate|967|()|var|int16
var_968 = relay.var("var_968", dtype = "int16", shape = (14, 5, 7))#candidate|968|(14, 5, 7)|var|int16
call_966 = func_965_call(var_967,var_968,)
output = call_966
func_969 = relay.Function([var_967,var_968,], output)
mutated_mod['func_969'] = func_969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_1061 = relay.TupleGetItem(func_314_call(), 0)
call_1062 = relay.TupleGetItem(func_315_call(), 0)
var_1071 = relay.var("var_1071", dtype = "uint16", shape = (4, 2, 2))#candidate|1071|(4, 2, 2)|var|uint16
bop_1072 = relay.left_shift(call_1061.astype('uint16'), relay.reshape(var_1071.astype('uint16'), relay.shape_of(call_1061))) # shape=(4, 2, 2)
bop_1075 = relay.left_shift(call_1062.astype('uint16'), relay.reshape(var_1071.astype('uint16'), relay.shape_of(call_1062))) # shape=(4, 2, 2)
output = relay.Tuple([bop_1072,])
output2 = relay.Tuple([bop_1075,])
func_1088 = relay.Function([var_1071,], output)
mod['func_1088'] = func_1088
mod = relay.transform.InferType()(mod)
mutated_mod['func_1088'] = func_1088
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1089 = relay.var("var_1089", dtype = "uint16", shape = (4, 2, 2))#candidate|1089|(4, 2, 2)|var|uint16
func_1088_call = mutated_mod.get_global_var('func_1088')
call_1090 = func_1088_call(var_1089)
output = call_1090
func_1091 = relay.Function([var_1089], output)
mutated_mod['func_1091'] = func_1091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mod.get_global_var('func_590')
func_592_call = mutated_mod.get_global_var('func_592')
call_1129 = func_590_call()
call_1130 = func_590_call()
output = relay.Tuple([call_1129,])
output2 = relay.Tuple([call_1130,])
func_1146 = relay.Function([], output)
mod['func_1146'] = func_1146
mod = relay.transform.InferType()(mod)
output = func_1146()
func_1147 = relay.Function([], output)
mutated_mod['func_1147'] = func_1147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1186 = relay.var("var_1186", dtype = "float32", shape = (15, 5, 11))#candidate|1186|(15, 5, 11)|var|float32
uop_1187 = relay.acos(var_1186.astype('float32')) # shape=(15, 5, 11)
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
call_1195 = relay.TupleGetItem(func_475_call(), 0)
call_1196 = relay.TupleGetItem(func_477_call(), 0)
output = relay.Tuple([uop_1187,call_1195,])
output2 = relay.Tuple([uop_1187,call_1196,])
func_1206 = relay.Function([var_1186,], output)
mod['func_1206'] = func_1206
mod = relay.transform.InferType()(mod)
var_1207 = relay.var("var_1207", dtype = "float32", shape = (15, 5, 11))#candidate|1207|(15, 5, 11)|var|float32
output = func_1206(var_1207)
func_1208 = relay.Function([var_1207], output)
mutated_mod['func_1208'] = func_1208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_1219 = func_210_call()
call_1220 = func_210_call()
func_898_call = mod.get_global_var('func_898')
func_899_call = mutated_mod.get_global_var('func_899')
call_1223 = relay.TupleGetItem(func_898_call(), 2)
call_1224 = relay.TupleGetItem(func_899_call(), 2)
uop_1237 = relay.sigmoid(call_1223.astype('float64')) # shape=(4, 2, 2)
uop_1239 = relay.sigmoid(call_1224.astype('float64')) # shape=(4, 2, 2)
func_547_call = mod.get_global_var('func_547')
func_548_call = mutated_mod.get_global_var('func_548')
call_1243 = relay.TupleGetItem(func_547_call(), 0)
call_1244 = relay.TupleGetItem(func_548_call(), 0)
func_738_call = mod.get_global_var('func_738')
func_739_call = mutated_mod.get_global_var('func_739')
call_1247 = relay.TupleGetItem(func_738_call(), 0)
call_1248 = relay.TupleGetItem(func_739_call(), 0)
func_965_call = mod.get_global_var('func_965')
func_969_call = mutated_mod.get_global_var('func_969')
const_1251 = relay.const(10, dtype = "int16")#candidate|1251|()|const|int16
var_1252 = relay.var("var_1252", dtype = "int16", shape = (490,))#candidate|1252|(490,)|var|int16
call_1250 = relay.TupleGetItem(func_965_call(relay.reshape(const_1251.astype('int16'), []), relay.reshape(var_1252.astype('int16'), [14, 5, 7]), ), 0)
call_1253 = relay.TupleGetItem(func_969_call(relay.reshape(const_1251.astype('int16'), []), relay.reshape(var_1252.astype('int16'), [14, 5, 7]), ), 0)
uop_1261 = relay.tan(var_1252.astype('float32')) # shape=(490,)
uop_1269 = relay.asinh(uop_1237.astype('float32')) # shape=(4, 2, 2)
uop_1271 = relay.asinh(uop_1239.astype('float32')) # shape=(4, 2, 2)
output = relay.Tuple([call_1219,call_1243,call_1247,call_1250,const_1251,uop_1261,uop_1269,])
output2 = relay.Tuple([call_1220,call_1244,call_1248,call_1253,const_1251,uop_1261,uop_1271,])
func_1274 = relay.Function([var_1252,], output)
mod['func_1274'] = func_1274
mod = relay.transform.InferType()(mod)
mutated_mod['func_1274'] = func_1274
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1275 = relay.var("var_1275", dtype = "int16", shape = (490,))#candidate|1275|(490,)|var|int16
func_1274_call = mutated_mod.get_global_var('func_1274')
call_1276 = func_1274_call(var_1275)
output = call_1276
func_1277 = relay.Function([var_1275], output)
mutated_mod['func_1277'] = func_1277
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1301 = relay.var("var_1301", dtype = "float64", shape = (10, 11, 1))#candidate|1301|(10, 11, 1)|var|float64
uop_1302 = relay.atanh(var_1301.astype('float64')) # shape=(10, 11, 1)
output = relay.Tuple([uop_1302,])
output2 = relay.Tuple([uop_1302,])
func_1306 = relay.Function([var_1301,], output)
mod['func_1306'] = func_1306
mod = relay.transform.InferType()(mod)
var_1307 = relay.var("var_1307", dtype = "float64", shape = (10, 11, 1))#candidate|1307|(10, 11, 1)|var|float64
output = func_1306(var_1307)
func_1308 = relay.Function([var_1307], output)
mutated_mod['func_1308'] = func_1308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mod.get_global_var('func_898')
func_899_call = mutated_mod.get_global_var('func_899')
call_1318 = relay.TupleGetItem(func_898_call(), 0)
call_1319 = relay.TupleGetItem(func_899_call(), 0)
output = call_1318
output2 = call_1319
func_1327 = relay.Function([], output)
mod['func_1327'] = func_1327
mod = relay.transform.InferType()(mod)
mutated_mod['func_1327'] = func_1327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mutated_mod.get_global_var('func_1327')
call_1328 = func_1327_call()
output = call_1328
func_1329 = relay.Function([], output)
mutated_mod['func_1329'] = func_1329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_1334 = relay.TupleGetItem(func_401_call(), 2)
call_1335 = relay.TupleGetItem(func_402_call(), 2)
func_898_call = mod.get_global_var('func_898')
func_899_call = mutated_mod.get_global_var('func_899')
call_1338 = relay.TupleGetItem(func_898_call(), 0)
call_1339 = relay.TupleGetItem(func_899_call(), 0)
func_965_call = mod.get_global_var('func_965')
func_969_call = mutated_mod.get_global_var('func_969')
var_1349 = relay.var("var_1349", dtype = "int16", shape = ())#candidate|1349|()|var|int16
var_1350 = relay.var("var_1350", dtype = "int16", shape = (490,))#candidate|1350|(490,)|var|int16
call_1348 = relay.TupleGetItem(func_965_call(relay.reshape(var_1349.astype('int16'), []), relay.reshape(var_1350.astype('int16'), [14, 5, 7]), ), 0)
call_1351 = relay.TupleGetItem(func_969_call(relay.reshape(var_1349.astype('int16'), []), relay.reshape(var_1350.astype('int16'), [14, 5, 7]), ), 0)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_1352 = relay.TupleGetItem(func_314_call(), 0)
call_1353 = relay.TupleGetItem(func_315_call(), 0)
output = relay.Tuple([call_1334,call_1338,call_1348,var_1349,var_1350,call_1352,])
output2 = relay.Tuple([call_1335,call_1339,call_1351,var_1349,var_1350,call_1353,])
func_1359 = relay.Function([var_1349,var_1350,], output)
mod['func_1359'] = func_1359
mod = relay.transform.InferType()(mod)
var_1360 = relay.var("var_1360", dtype = "int16", shape = ())#candidate|1360|()|var|int16
var_1361 = relay.var("var_1361", dtype = "int16", shape = (490,))#candidate|1361|(490,)|var|int16
output = func_1359(var_1360,var_1361,)
func_1362 = relay.Function([var_1360,var_1361,], output)
mutated_mod['func_1362'] = func_1362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1146_call = mod.get_global_var('func_1146')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_1369 = relay.TupleGetItem(func_1146_call(), 0)
call_1370 = relay.TupleGetItem(func_1147_call(), 0)
output = call_1369
output2 = call_1370
func_1378 = relay.Function([], output)
mod['func_1378'] = func_1378
mod = relay.transform.InferType()(mod)
output = func_1378()
func_1379 = relay.Function([], output)
mutated_mod['func_1379'] = func_1379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_629_call = mod.get_global_var('func_629')
func_631_call = mutated_mod.get_global_var('func_631')
call_1380 = relay.TupleGetItem(func_629_call(), 1)
call_1381 = relay.TupleGetItem(func_631_call(), 1)
var_1382 = relay.var("var_1382", dtype = "float64", shape = (7, 2, 2))#candidate|1382|(7, 2, 2)|var|float64
bop_1383 = relay.maximum(call_1380.astype('uint8'), var_1382.astype('uint8')) # shape=(7, 2, 2)
bop_1386 = relay.maximum(call_1381.astype('uint8'), var_1382.astype('uint8')) # shape=(7, 2, 2)
output = relay.Tuple([bop_1383,])
output2 = relay.Tuple([bop_1386,])
func_1387 = relay.Function([var_1382,], output)
mod['func_1387'] = func_1387
mod = relay.transform.InferType()(mod)
mutated_mod['func_1387'] = func_1387
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1388 = relay.var("var_1388", dtype = "float64", shape = (7, 2, 2))#candidate|1388|(7, 2, 2)|var|float64
func_1387_call = mutated_mod.get_global_var('func_1387')
call_1389 = func_1387_call(var_1388)
output = call_1389
func_1390 = relay.Function([var_1388], output)
mutated_mod['func_1390'] = func_1390
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1414 = relay.var("var_1414", dtype = "uint32", shape = (12, 7, 2))#candidate|1414|(12, 7, 2)|var|uint32
var_1415 = relay.var("var_1415", dtype = "uint32", shape = (12, 7, 2))#candidate|1415|(12, 7, 2)|var|uint32
bop_1416 = relay.less(var_1414.astype('bool'), relay.reshape(var_1415.astype('bool'), relay.shape_of(var_1414))) # shape=(12, 7, 2)
func_1387_call = mod.get_global_var('func_1387')
func_1390_call = mutated_mod.get_global_var('func_1390')
var_1420 = relay.var("var_1420", dtype = "float64", shape = (28,))#candidate|1420|(28,)|var|float64
call_1419 = relay.TupleGetItem(func_1387_call(relay.reshape(var_1420.astype('float64'), [7, 2, 2])), 0)
call_1421 = relay.TupleGetItem(func_1390_call(relay.reshape(var_1420.astype('float64'), [7, 2, 2])), 0)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_1422 = relay.TupleGetItem(func_401_call(), 0)
call_1423 = relay.TupleGetItem(func_402_call(), 0)
func_1306_call = mod.get_global_var('func_1306')
func_1308_call = mutated_mod.get_global_var('func_1308')
const_1429 = relay.const([8.439021,-6.479124,5.232379,0.869856,0.372257,-3.576990,0.896259,-4.275155,-6.696440,6.977631,3.817943,-0.020483,2.171875,-8.475229,-9.240069,-8.671002,-7.142984,3.239116,1.518625,-3.166458,-0.382397,-5.013461,-4.187692,-1.096252,7.044193,5.794916,-2.255406,8.141766,9.888579,5.750601,-7.944482,2.613398,-3.564548,-4.820536,-0.843389,2.779184,-6.079509,-0.441313,-6.404669,3.578958,-8.565979,-3.963908,-8.047048,7.767717,3.822938,-8.562812,-7.374054,7.645221,-5.666746,-0.508497,-7.744384,-9.423397,6.686439,7.437462,2.530228,4.453748,2.362990,3.008634,-6.133613,-7.242362,0.560601,6.455765,-2.218305,-3.491754,-5.973171,3.161278,-8.811512,5.518231,1.185997,4.776682,6.556098,-3.505590,7.268406,1.254382,-7.555258,7.758428,-7.112935,-4.031418,2.757488,5.848722,1.623749,1.510832,-6.826584,-4.922425,8.434860,2.707962,-4.565561,-7.439907,2.701844,3.648483,8.003604,2.057916,0.583169,-4.796400,-9.258572,5.195472,3.475854,-2.635210,1.857621,6.929157,-5.148595,-1.069680,-7.875562,-0.530477,-6.713372,-2.707423,7.486558,5.513796,6.442037,9.107857], dtype = "float64")#candidate|1429|(110,)|const|float64
call_1428 = relay.TupleGetItem(func_1306_call(relay.reshape(const_1429.astype('float64'), [10, 11, 1])), 0)
call_1430 = relay.TupleGetItem(func_1308_call(relay.reshape(const_1429.astype('float64'), [10, 11, 1])), 0)
func_1274_call = mod.get_global_var('func_1274')
func_1277_call = mutated_mod.get_global_var('func_1277')
const_1432 = relay.const([[-7],[1],[6],[9],[-4],[-7],[7],[2],[-8],[6],[-3],[7],[-5],[7],[2],[-8],[-6],[8],[-2],[-3],[9],[-7],[4],[4],[2],[-6],[-9],[2],[-5],[-3],[8],[5],[-10],[-10],[-1],[-9],[5],[-1],[-7],[-2],[6],[-5],[-3],[8],[6],[5],[3],[-2],[5],[7],[4],[-8],[-4],[-9],[3],[2],[-9],[4],[-4],[10],[-4],[-5],[-4],[-1],[-8],[-5],[-4],[3],[-2],[-9],[-4],[-6],[-5],[-7],[-7],[-8],[1],[-9],[2],[-2],[-6],[-5],[9],[-8],[-2],[6],[7],[-1],[6],[-1],[4],[-1],[7],[-7],[-10],[9],[5],[-8],[-2],[5],[-3],[-10],[-5],[-3],[10],[2],[-7],[10],[-5],[-1],[8],[-2],[-4],[7],[-5],[1],[-5],[8],[-3],[-9],[-5],[8],[5],[6],[-5],[-6],[-8],[7],[-7],[9],[-9],[1],[1],[-2],[-10],[-9],[5],[7],[-5],[2],[1],[-4],[6],[-1],[8],[-6],[10],[8],[9],[-8],[-4],[-4],[-4],[1],[-5],[9],[10],[-4],[-5],[-1],[7],[-7],[-9],[10],[9],[-6],[5],[-4],[-4],[-8],[7],[-6],[-9],[5],[-5],[4],[-8],[-9],[-7],[4],[9],[1],[-4],[4],[-7],[9],[-8],[-10],[5],[-10],[4],[4],[-6],[-8],[4],[-1],[3],[-8],[4],[-5],[4],[2],[8],[2],[9],[-6],[7],[-4],[5],[-6],[-7],[-1],[-8],[9],[2],[-10],[7],[2],[-7],[-9],[-6],[9],[4],[-6],[7],[-7],[10],[5],[8],[-9],[-8],[-9],[-2],[10],[-3],[6],[-5],[5],[-6],[10],[5],[-10],[-5],[3],[10],[4],[-3],[-5],[-1],[-4],[6],[-8],[-5],[-10],[-3],[6],[8],[-5],[10],[-8],[1],[8],[-4],[9],[-8],[4],[5],[4],[-2],[-10],[-7],[-7],[4],[-9],[1],[5],[-7],[8],[-8],[9],[-1],[9],[-2],[5],[9],[10],[-6],[10],[8],[-4],[-5],[3],[-4],[5],[7],[9],[4],[6],[-2],[1],[10],[7],[10],[-4],[5],[9],[7],[-3],[-4],[-4],[-2],[-1],[-10],[4],[1],[3],[-1],[-7],[-6],[-9],[-1],[2],[-2],[-8],[5],[9],[4],[6],[8],[5],[-7],[9],[7],[-9],[7],[5],[-8],[-5],[-3],[-9],[6],[8],[8],[3],[7],[-5],[4],[-2],[-10],[-5],[1],[-6],[-8],[3],[7],[-2],[2],[4],[-7],[5],[-4],[-8],[-4],[1],[-3],[4],[6],[-5],[2],[-6],[2],[1],[-9],[5],[1],[9],[2],[-6],[-10],[-2],[-3],[9],[6],[-4],[3],[-7],[-9],[10],[-1],[-5],[5],[-8],[3],[-3],[10],[8],[-2],[5],[-10],[-6],[10],[-2],[2],[-10],[-7],[7],[-10],[8],[8],[-8],[9],[-4],[-10],[10],[-7],[-7],[-10],[9],[-8],[-6],[3],[-6],[-6],[-8],[-10],[-5],[-10],[-1],[-5],[2],[-7],[-2],[-7],[2],[-7],[10],[-10],[4],[-5],[-4],[-7],[-5],[5],[7],[6],[3],[-10],[4],[-5],[3],[-5],[-3],[3],[2],[-8],[-2],[-3],[-1],[-2],[-10],[10],[4],[10],[7],[2],[-7],[-3],[3],[8],[4],[2],[-10],[-5],[-5],[9],[-5],[-1],[-9],[5],[-6],[6],[-6],[-6],[6],[4],[9],[-6],[-3],[1],[-7]], dtype = "int16")#candidate|1432|(490, 1)|const|int16
call_1431 = relay.TupleGetItem(func_1274_call(relay.reshape(const_1432.astype('int16'), [490,])), 5)
call_1433 = relay.TupleGetItem(func_1277_call(relay.reshape(const_1432.astype('int16'), [490,])), 5)
bop_1437 = relay.less_equal(call_1431.astype('bool'), call_1428.astype('bool')) # shape=(10, 11, 490)
bop_1440 = relay.less_equal(call_1433.astype('bool'), call_1430.astype('bool')) # shape=(10, 11, 490)
output = relay.Tuple([bop_1416,call_1419,var_1420,call_1422,const_1429,const_1432,bop_1437,])
output2 = relay.Tuple([bop_1416,call_1421,var_1420,call_1423,const_1429,const_1432,bop_1440,])
func_1450 = relay.Function([var_1414,var_1415,var_1420,], output)
mod['func_1450'] = func_1450
mod = relay.transform.InferType()(mod)
mutated_mod['func_1450'] = func_1450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1450_call = mutated_mod.get_global_var('func_1450')
var_1452 = relay.var("var_1452", dtype = "uint32", shape = (12, 7, 2))#candidate|1452|(12, 7, 2)|var|uint32
var_1453 = relay.var("var_1453", dtype = "uint32", shape = (12, 7, 2))#candidate|1453|(12, 7, 2)|var|uint32
var_1454 = relay.var("var_1454", dtype = "float64", shape = (28,))#candidate|1454|(28,)|var|float64
call_1451 = func_1450_call(var_1452,var_1453,var_1454,)
output = call_1451
func_1455 = relay.Function([var_1452,var_1453,var_1454,], output)
mutated_mod['func_1455'] = func_1455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_629_call = mod.get_global_var('func_629')
func_631_call = mutated_mod.get_global_var('func_631')
call_1615 = relay.TupleGetItem(func_629_call(), 0)
call_1616 = relay.TupleGetItem(func_631_call(), 0)
output = relay.Tuple([call_1615,])
output2 = relay.Tuple([call_1616,])
func_1636 = relay.Function([], output)
mod['func_1636'] = func_1636
mod = relay.transform.InferType()(mod)
mutated_mod['func_1636'] = func_1636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mutated_mod.get_global_var('func_1636')
call_1637 = func_1636_call()
output = call_1637
func_1638 = relay.Function([], output)
mutated_mod['func_1638'] = func_1638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1378_call = mod.get_global_var('func_1378')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_1639 = func_1378_call()
call_1640 = func_1378_call()
func_1088_call = mod.get_global_var('func_1088')
func_1091_call = mutated_mod.get_global_var('func_1091')
call_1646 = relay.TupleGetItem(func_1088_call(relay.reshape(call_1639.astype('uint16'), [4, 2, 2])), 0)
call_1647 = relay.TupleGetItem(func_1091_call(relay.reshape(call_1639.astype('uint16'), [4, 2, 2])), 0)
func_1088_call = mod.get_global_var('func_1088')
func_1091_call = mutated_mod.get_global_var('func_1091')
call_1658 = relay.TupleGetItem(func_1088_call(relay.reshape(call_1646.astype('uint16'), [4, 2, 2])), 0)
call_1659 = relay.TupleGetItem(func_1091_call(relay.reshape(call_1646.astype('uint16'), [4, 2, 2])), 0)
output = relay.Tuple([call_1639,call_1646,call_1658,])
output2 = relay.Tuple([call_1640,call_1647,call_1659,])
func_1661 = relay.Function([], output)
mod['func_1661'] = func_1661
mod = relay.transform.InferType()(mod)
mutated_mod['func_1661'] = func_1661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1661_call = mutated_mod.get_global_var('func_1661')
call_1662 = func_1661_call()
output = call_1662
func_1663 = relay.Function([], output)
mutated_mod['func_1663'] = func_1663
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1679 = relay.var("var_1679", dtype = "float32", shape = (15, 7, 10))#candidate|1679|(15, 7, 10)|var|float32
uop_1680 = relay.rsqrt(var_1679.astype('float32')) # shape=(15, 7, 10)
func_1306_call = mod.get_global_var('func_1306')
func_1308_call = mutated_mod.get_global_var('func_1308')
const_1685 = relay.const([9.932912,-4.041624,7.212032,-6.357111,-8.073511,0.185005,0.274588,-2.924274,5.616581,-6.872937,0.720504,7.246269,-5.851252,-1.535806,-8.983943,0.699559,4.259421,0.695466,6.242618,-3.319462,-2.501961,-2.592453,2.350410,0.103655,9.166238,-4.303304,1.020127,9.883954,-7.135176,1.614763,-5.640385,0.091922,-6.034133,-9.166113,-9.501929,-6.312387,-4.802024,-1.164819,3.941604,-1.614831,8.151400,2.256745,1.001043,7.485764,-0.120327,-6.761076,4.909541,-7.337583,-9.250214,2.075343,9.169921,-7.712252,-7.824390,6.198992,-2.632406,-2.759590,-4.145614,5.872472,-5.793756,-5.002368,7.053495,1.719884,-7.165958,7.104733,-1.383158,6.077164,-6.664211,-2.843721,7.331751,-3.397155,7.666581,9.035628,-8.488021,3.938270,6.922468,2.184554,8.691006,4.058681,6.506279,-0.392045,-5.515809,1.710667,5.013478,2.568543,-8.073386,8.376430,6.061138,2.369944,8.973859,-5.633531,-6.760031,4.381707,7.320551,4.276399,3.287531,-1.417471,-0.232652,-1.184990,3.819445,-9.164620,6.802539,-4.601753,-5.675687,-7.733080,-8.679429,7.856530,5.169344,-7.324217,8.852151,0.020212], dtype = "float64")#candidate|1685|(110,)|const|float64
call_1684 = relay.TupleGetItem(func_1306_call(relay.reshape(const_1685.astype('float64'), [10, 11, 1])), 0)
call_1686 = relay.TupleGetItem(func_1308_call(relay.reshape(const_1685.astype('float64'), [10, 11, 1])), 0)
output = relay.Tuple([uop_1680,call_1684,const_1685,])
output2 = relay.Tuple([uop_1680,call_1686,const_1685,])
func_1708 = relay.Function([var_1679,], output)
mod['func_1708'] = func_1708
mod = relay.transform.InferType()(mod)
var_1709 = relay.var("var_1709", dtype = "float32", shape = (15, 7, 10))#candidate|1709|(15, 7, 10)|var|float32
output = func_1708(var_1709)
func_1710 = relay.Function([var_1709], output)
mutated_mod['func_1710'] = func_1710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mod.get_global_var('func_898')
func_899_call = mutated_mod.get_global_var('func_899')
call_1819 = relay.TupleGetItem(func_898_call(), 0)
call_1820 = relay.TupleGetItem(func_899_call(), 0)
var_1828 = relay.var("var_1828", dtype = "float32", shape = (8, 12, 8))#candidate|1828|(8, 12, 8)|var|float32
bop_1829 = relay.minimum(call_1819.astype('int16'), relay.reshape(var_1828.astype('int16'), relay.shape_of(call_1819))) # shape=(8, 12, 8)
bop_1832 = relay.minimum(call_1820.astype('int16'), relay.reshape(var_1828.astype('int16'), relay.shape_of(call_1820))) # shape=(8, 12, 8)
output = relay.Tuple([bop_1829,])
output2 = relay.Tuple([bop_1832,])
func_1836 = relay.Function([var_1828,], output)
mod['func_1836'] = func_1836
mod = relay.transform.InferType()(mod)
mutated_mod['func_1836'] = func_1836
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1837 = relay.var("var_1837", dtype = "float32", shape = (8, 12, 8))#candidate|1837|(8, 12, 8)|var|float32
func_1836_call = mutated_mod.get_global_var('func_1836')
call_1838 = func_1836_call(var_1837)
output = call_1838
func_1839 = relay.Function([var_1837], output)
mutated_mod['func_1839'] = func_1839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_1847 = relay.TupleGetItem(func_290_call(), 0)
call_1848 = relay.TupleGetItem(func_291_call(), 0)
output = relay.Tuple([call_1847,])
output2 = relay.Tuple([call_1848,])
func_1849 = relay.Function([], output)
mod['func_1849'] = func_1849
mod = relay.transform.InferType()(mod)
output = func_1849()
func_1850 = relay.Function([], output)
mutated_mod['func_1850'] = func_1850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_437_call = mod.get_global_var('func_437')
func_438_call = mutated_mod.get_global_var('func_438')
call_1869 = func_437_call()
call_1870 = func_437_call()
func_1274_call = mod.get_global_var('func_1274')
func_1277_call = mutated_mod.get_global_var('func_1277')
const_1880 = relay.const([[-8,-9],[8,5],[-10,6],[-4,-7],[9,-6],[10,-1],[-6,7],[6,2],[-6,10],[8,3],[10,10],[-2,-3],[-1,-3],[-10,3],[7,-8],[3,-7],[-10,2],[4,10],[9,-8],[-4,-1],[-1,-5],[1,6],[6,-10],[-3,-8],[8,5],[-9,8],[4,8],[6,-3],[6,-7],[-6,6],[7,10],[5,-7],[10,-4],[6,9],[-9,-7],[6,1],[10,10],[1,9],[-10,-9],[9,-7],[-7,-1],[5,2],[5,-9],[1,-5],[-10,-8],[-1,-10],[-8,-7],[5,9],[6,-5],[-8,-5],[6,7],[5,-10],[-9,7],[-7,-10],[-6,-3],[10,2],[-2,7],[2,6],[-5,9],[7,7],[10,-3],[-1,-4],[-1,-9],[-9,-6],[-6,2],[6,-7],[-10,-5],[6,2],[-5,2],[1,6],[-3,2],[-4,4],[5,7],[5,-4],[-10,4],[10,1],[5,3],[9,6],[2,7],[-10,5],[8,-7],[-6,2],[2,2],[-5,7],[-8,4],[2,3],[-1,2],[-1,7],[9,-4],[6,2],[3,-8],[-9,-8],[9,-6],[3,-5],[-10,-4],[-3,10],[-4,8],[-2,6],[4,-6],[2,2],[6,-2],[-9,-3],[-3,-8],[7,-8],[-4,-1],[-7,-4],[4,6],[5,-9],[7,-10],[-8,3],[-10,-10],[1,-10],[-6,-1],[-9,-4],[6,10],[9,2],[1,-2],[5,-10],[8,-1],[-10,2],[-1,9],[-10,4],[-6,-5],[4,-10],[-9,3],[8,6],[5,-3],[-10,1],[9,-3],[6,3],[2,4],[7,-10],[-6,8],[-6,2],[-6,6],[-1,7],[-10,9],[8,5],[-1,-5],[-5,-3],[-7,7],[-9,-7],[-5,3],[2,5],[10,8],[-5,-9],[6,-5],[8,3],[2,1],[8,-8],[-2,8],[1,-8],[7,-1],[10,9],[4,6],[1,-1],[9,4],[-1,10],[-3,9],[-4,-5],[2,-3],[5,-10],[-5,5],[6,-1],[-8,-2],[-9,-4],[3,-6],[-8,-7],[-8,5],[-2,4],[-9,-3],[5,-10],[1,3],[6,-2],[-9,-7],[-9,9],[3,-1],[-7,2],[6,-3],[-1,5],[4,-2],[7,1],[-2,3],[1,9],[6,-8],[-6,10],[-8,-2],[-3,9],[-7,10],[-4,-10],[-7,8],[-6,1],[6,4],[-2,4],[7,-6],[-5,10],[7,7],[-10,10],[3,5],[-4,3],[8,3],[-4,-9],[-3,1],[-4,-3],[2,-4],[1,8],[-5,-5],[-1,-10],[6,10],[-10,-10],[6,2],[-4,-2],[-7,7],[-2,3],[-1,-8],[-5,-3],[2,2],[6,5],[-5,3],[4,-8],[-2,8],[-1,3],[9,6],[10,6],[5,-3],[4,-5],[5,-2],[1,-9],[-4,-9],[9,-7],[-3,-2],[-2,-4],[10,8],[-3,5],[-10,6],[-5,-4],[-3,-4],[-5,9],[-3,1],[-1,2],[10,5],[4,-3],[7,6],[6,2],[3,2]], dtype = "int16")#candidate|1880|(245, 2)|const|int16
call_1879 = relay.TupleGetItem(func_1274_call(relay.reshape(const_1880.astype('int16'), [490,])), 1)
call_1881 = relay.TupleGetItem(func_1277_call(relay.reshape(const_1880.astype('int16'), [490,])), 1)
output = relay.Tuple([call_1869,call_1879,const_1880,])
output2 = relay.Tuple([call_1870,call_1881,const_1880,])
func_1887 = relay.Function([], output)
mod['func_1887'] = func_1887
mod = relay.transform.InferType()(mod)
mutated_mod['func_1887'] = func_1887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1887_call = mutated_mod.get_global_var('func_1887')
call_1888 = func_1887_call()
output = call_1888
func_1889 = relay.Function([], output)
mutated_mod['func_1889'] = func_1889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_1926 = relay.TupleGetItem(func_401_call(), 1)
call_1927 = relay.TupleGetItem(func_402_call(), 1)
output = relay.Tuple([call_1926,])
output2 = relay.Tuple([call_1927,])
func_1929 = relay.Function([], output)
mod['func_1929'] = func_1929
mod = relay.transform.InferType()(mod)
mutated_mod['func_1929'] = func_1929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1929_call = mutated_mod.get_global_var('func_1929')
call_1930 = func_1929_call()
output = call_1930
func_1931 = relay.Function([], output)
mutated_mod['func_1931'] = func_1931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_547_call = mod.get_global_var('func_547')
func_548_call = mutated_mod.get_global_var('func_548')
call_1959 = relay.TupleGetItem(func_547_call(), 0)
call_1960 = relay.TupleGetItem(func_548_call(), 0)
func_1146_call = mod.get_global_var('func_1146')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_1961 = relay.TupleGetItem(func_1146_call(), 0)
call_1962 = relay.TupleGetItem(func_1147_call(), 0)
func_1387_call = mod.get_global_var('func_1387')
func_1390_call = mutated_mod.get_global_var('func_1390')
const_1964 = relay.const([[-7.504336,-7.391887],[6.225474,4.970388],[1.956001,5.625499],[5.099000,-8.685642],[-1.627164,-0.513130],[-5.028213,7.264681],[-4.552888,-2.391920],[2.166421,-0.624844],[6.754848,-3.463598],[6.152705,9.153332],[-0.852115,6.424173],[-6.309208,1.855011],[2.654311,8.563126],[4.758203,-4.422874]], dtype = "float64")#candidate|1964|(14, 2)|const|float64
call_1963 = relay.TupleGetItem(func_1387_call(relay.reshape(const_1964.astype('float64'), [7, 2, 2])), 0)
call_1965 = relay.TupleGetItem(func_1390_call(relay.reshape(const_1964.astype('float64'), [7, 2, 2])), 0)
func_1450_call = mod.get_global_var('func_1450')
func_1455_call = mutated_mod.get_global_var('func_1455')
var_1975 = relay.var("var_1975", dtype = "uint32", shape = (168,))#candidate|1975|(168,)|var|uint32
call_1974 = relay.TupleGetItem(func_1450_call(relay.reshape(var_1975.astype('uint32'), [12, 7, 2]), relay.reshape(var_1975.astype('uint32'), [12, 7, 2]), relay.reshape(call_1963.astype('float64'), [28,]), ), 0)
call_1976 = relay.TupleGetItem(func_1455_call(relay.reshape(var_1975.astype('uint32'), [12, 7, 2]), relay.reshape(var_1975.astype('uint32'), [12, 7, 2]), relay.reshape(call_1963.astype('float64'), [28,]), ), 0)
bop_1986 = relay.minimum(call_1959.astype('int16'), call_1963.astype('int16')) # shape=(7, 2, 2)
bop_1989 = relay.minimum(call_1960.astype('int16'), call_1965.astype('int16')) # shape=(7, 2, 2)
output = relay.Tuple([call_1961,const_1964,call_1974,var_1975,bop_1986,])
output2 = relay.Tuple([call_1962,const_1964,call_1976,var_1975,bop_1989,])
func_1990 = relay.Function([var_1975,], output)
mod['func_1990'] = func_1990
mod = relay.transform.InferType()(mod)
var_1991 = relay.var("var_1991", dtype = "uint32", shape = (168,))#candidate|1991|(168,)|var|uint32
output = func_1990(var_1991)
func_1992 = relay.Function([var_1991], output)
mutated_mod['func_1992'] = func_1992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_245_call = mod.get_global_var('func_245')
func_246_call = mutated_mod.get_global_var('func_246')
call_1999 = relay.TupleGetItem(func_245_call(), 2)
call_2000 = relay.TupleGetItem(func_246_call(), 2)
var_2003 = relay.var("var_2003", dtype = "int8", shape = (72,))#candidate|2003|(72,)|var|int8
bop_2004 = relay.greater(call_1999.astype('bool'), relay.reshape(var_2003.astype('bool'), relay.shape_of(call_1999))) # shape=(72,)
bop_2007 = relay.greater(call_2000.astype('bool'), relay.reshape(var_2003.astype('bool'), relay.shape_of(call_2000))) # shape=(72,)
func_590_call = mod.get_global_var('func_590')
func_592_call = mutated_mod.get_global_var('func_592')
call_2012 = func_590_call()
call_2013 = func_590_call()
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_2016 = func_1327_call()
call_2017 = func_1327_call()
var_2025 = relay.var("var_2025", dtype = "int8", shape = (72,))#candidate|2025|(72,)|var|int8
bop_2026 = relay.less(var_2003.astype('bool'), relay.reshape(var_2025.astype('bool'), relay.shape_of(var_2003))) # shape=(72,)
func_898_call = mod.get_global_var('func_898')
func_899_call = mutated_mod.get_global_var('func_899')
call_2033 = relay.TupleGetItem(func_898_call(), 2)
call_2034 = relay.TupleGetItem(func_899_call(), 2)
func_822_call = mod.get_global_var('func_822')
func_825_call = mutated_mod.get_global_var('func_825')
const_2039 = relay.const([[False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True],[False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True],[True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False]], dtype = "bool")#candidate|2039|(3, 420)|const|bool
call_2038 = relay.TupleGetItem(func_822_call(relay.reshape(const_2039.astype('bool'), [9, 10, 14])), 2)
call_2040 = relay.TupleGetItem(func_825_call(relay.reshape(const_2039.astype('bool'), [9, 10, 14])), 2)
output = relay.Tuple([bop_2004,call_2012,call_2016,bop_2026,call_2033,call_2038,const_2039,])
output2 = relay.Tuple([bop_2007,call_2013,call_2017,bop_2026,call_2034,call_2040,const_2039,])
func_2042 = relay.Function([var_2003,var_2025,], output)
mod['func_2042'] = func_2042
mod = relay.transform.InferType()(mod)
mutated_mod['func_2042'] = func_2042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2042_call = mutated_mod.get_global_var('func_2042')
var_2044 = relay.var("var_2044", dtype = "int8", shape = (72,))#candidate|2044|(72,)|var|int8
var_2045 = relay.var("var_2045", dtype = "int8", shape = (72,))#candidate|2045|(72,)|var|int8
call_2043 = func_2042_call(var_2044,var_2045,)
output = call_2043
func_2046 = relay.Function([var_2044,var_2045,], output)
mutated_mod['func_2046'] = func_2046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_2299 = relay.TupleGetItem(func_314_call(), 0)
call_2300 = relay.TupleGetItem(func_315_call(), 0)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
const_2308 = relay.const([-6.088108,-3.513118,6.337610,2.536710,1.469978,3.730522,9.686789,-1.050413,2.159179,9.696848,0.944912,-4.000936,6.971645,3.153062,7.676636,9.486149,5.677284,-3.695035,-6.444607,-0.474307,-5.287715,-2.117565,7.949693,-3.243125,-2.172678,-6.627583,-8.154576,0.124980,-3.087120,-8.110329,-4.878795,3.290861,3.974384,1.014660,-2.861675,7.094247,2.729330,-1.752168,-3.518370,-5.586250,-2.092592,2.166673,6.592533,-7.290673,1.423073,7.426764,-7.284990,-8.245507,-8.800308,0.404693,5.069494,-2.619608,2.751828,3.489557,1.348804,-8.654905,5.301767,5.947458,2.221022,-4.184587,-3.657734,-3.643422,9.429413,5.763282,-9.019681,-7.046053,8.230847,3.713404,5.628214,1.946780,-9.014386,-0.841895,0.776805,-4.336848,4.189404,3.082677,3.485477,-0.713303,-8.701970,-5.993547,5.782963,-7.332094,1.450077,4.864256,1.954153,-0.791152,-0.972201,6.648739,-5.220908,-5.369069,-4.698948,7.113424,-3.782174,-0.383331,7.640837,9.282780,3.329257,-6.198854,1.891933,9.640900,-2.578650,-6.512404,-9.501886,-9.814120,-2.936476,-7.466470,-4.080491,-3.473901,-1.814199,-6.889475,3.482364,-0.270879,0.509422,-3.204625,-7.193228,8.050886,5.792191,4.900163,7.115841,-8.232640,0.421884,8.822415,-1.396069,-0.693051,-8.652972,9.310417,-7.842655,3.013395,-9.963821,8.472666,3.550426,7.262963,-8.932527,8.634962,-7.301254,5.608069,-1.515278,8.245424,-5.783886,4.852184,-0.174209,9.841454,-0.238088,5.224141,-3.058388,8.878910,5.715357,-9.991431,-1.111818,-7.990192,5.743740,-7.084355,-2.144793,-6.065167,6.170314,9.672794,-9.731552,-8.999262,9.589022,3.047555,-4.595537,-9.872820,0.179732,-4.349147,-2.085448,-6.113457,-1.307806,0.500144,3.668257,-8.691838,-9.634098,-8.171921,-2.922982,2.307161,-2.914710,0.258570,-1.671042,3.872942,-9.534581,9.697953,-9.972128,-4.055771,-1.020460,1.451644,9.678731,-0.972188,9.027721,1.689226,5.950937,-6.900931,8.645644,1.047540,3.050325,-3.148549,-4.150988,-5.178534,0.136264,8.780994,-8.094930,2.106702,-3.236667,6.743112,8.304821,4.663664,-3.107465,-3.666363,2.855343,1.907024,-2.937662,-7.705348,2.561740,3.561484,2.306328,-0.063379,4.665550,-9.286125,6.791267,-5.801269,-7.911297,1.273609,7.981184,-6.173017,8.157147,6.362421,5.953270,-0.479358,-2.370416,-9.571579,4.034181,7.572764,-3.959200,-9.257833,-1.349370,-9.456138,2.718481,3.233485,-0.540610,6.712775,3.269510,0.115636,2.954243,3.838437,-2.946176,8.028454,-9.893363,-3.901064,-3.165845,-9.869693,6.419136,5.024347,-3.673466,2.036852,2.942995,6.731276,3.205597,2.694571,-3.873256,-0.097591,-0.063768,-1.630173,1.513292,-1.768946,-4.119453,-5.959575,9.169818,-3.300348,-2.463767,-1.417949,-3.678219,-4.008699,2.421423,-1.972875,-0.039767,-4.592671,1.499479,2.634243,8.805700,-8.265876,-2.505383,-4.320144,8.595240,2.858640,-2.232635,3.591482,0.574680,1.851080,6.277467,6.511547,-6.569676,0.046287,-8.242768,-8.123642,-2.220695,6.969726,9.315731,-5.904308,-7.414947,-8.102535,-8.912693,-2.993933,0.060428,-8.532740,0.364931,-1.950234,4.800174,5.514436,-7.328602,3.501608,3.940517,1.039726,-5.665022,4.589080,-7.591472,-1.994396,8.522160,-3.545683,-7.875577,6.499685,-3.061633,1.631994,2.983642,-4.115549,6.566243,-1.729572,-2.028202,8.582255,-1.686257,-2.630127,2.116192,0.086995,8.258141,3.702263,-7.487173,6.342061,7.206936,-1.854712,-6.363378,-3.869216,-4.797952,-7.605190,3.904078,-5.109570,-2.930075,-6.298375,9.643304,-8.834411,7.712099,-5.441482,-3.922941,2.901370,-1.979729,0.965347,-9.653965,-3.800185,-6.481060,3.168160,8.984957,1.029064,-3.221560,0.390248,9.956822,-7.566199,5.070733,-5.623933,4.961085,6.703633,3.994470,-3.466692,4.980224,8.958065,5.819273,7.914710,-0.282522,-0.627386,-4.957800,-4.668859,0.926027,-0.767105,0.076462,-0.209517,-8.732041,-9.788918,-5.726377,7.234406,-0.657940,-6.319786,-8.818566,-1.007057,-1.589417,6.362995,-6.164542,9.353070,0.497297,-4.784018,-6.671640,2.753477,6.037354,1.425296,-9.262244,6.848023,6.881406,-4.012232,2.587584,-4.038960,4.898716,-5.945259,7.253828,7.445547,6.853200,4.168288,-9.579588,8.546245,-2.601928,-8.426700,2.663410,9.403352,8.706440,-2.010806,-5.706861,-3.176925,5.639347,6.545924,-3.463580,8.314940,6.712750,-8.184128,8.330656,5.311124,-3.336250,-7.780390,3.992011,-9.865765,2.969502,6.802809,8.646051,9.076109,-2.616278,5.087719,0.110115,-4.486749,3.326402,-5.559937,-9.229209,-8.563262,5.031105,0.685453,3.290904,1.824463,-8.629609,-2.906195,1.800415,-0.728799,0.326474,-8.328409,-2.846649,1.078130,8.030572,-2.891441,8.559838,-1.576484,6.068345,4.851747,3.099974,8.244263,5.459661,9.308972,8.792065,-6.503142,0.785827,9.952863,8.259991,5.534928,1.776933,1.692543,8.462095,8.915016,6.947205,8.508030,-4.953949,-9.001398,-7.098758,-2.427415,-0.669665,-1.849893,9.236290,5.182230,-1.193068,-7.833180,7.016971,-5.212613,6.919871,7.756686,-6.070801,-4.103093,-4.801983,-7.623083,-5.660289,-8.217424,6.632353,2.608594,6.590935,-4.868011,6.004591,2.951502,-6.413477,0.638165,2.177757,-1.126709,7.808034,-0.275144,1.219387,7.135402,3.160394,-8.234960,-3.935303,-5.970538,9.467254,-9.280043,9.271508,1.834748,0.915411,3.113748,6.171648,0.235620,-3.447368,-3.086749,-6.516344,-2.354419,-2.447596,0.751216,-9.105191,-6.500872,-7.835976,-8.392358,-6.632314,3.335230,4.414742,-2.130905,-9.727355,4.133041], dtype = "float32")#candidate|2308|(540,)|const|float32
call_2307 = relay.TupleGetItem(func_941_call(relay.reshape(const_2308.astype('float32'), [6, 15, 6])), 0)
call_2309 = relay.TupleGetItem(func_943_call(relay.reshape(const_2308.astype('float32'), [6, 15, 6])), 0)
uop_2312 = relay.sqrt(call_2307.astype('float64')) # shape=(6, 15, 6)
uop_2314 = relay.sqrt(call_2309.astype('float64')) # shape=(6, 15, 6)
uop_2320 = relay.log2(uop_2312.astype('float64')) # shape=(6, 15, 6)
uop_2322 = relay.log2(uop_2314.astype('float64')) # shape=(6, 15, 6)
bop_2327 = relay.floor_divide(uop_2312.astype('float32'), relay.reshape(const_2308.astype('float32'), relay.shape_of(uop_2312))) # shape=(6, 15, 6)
bop_2330 = relay.floor_divide(uop_2314.astype('float32'), relay.reshape(const_2308.astype('float32'), relay.shape_of(uop_2314))) # shape=(6, 15, 6)
uop_2338 = relay.asin(bop_2327.astype('float32')) # shape=(6, 15, 6)
uop_2340 = relay.asin(bop_2330.astype('float32')) # shape=(6, 15, 6)
output = relay.Tuple([call_2299,uop_2320,uop_2338,])
output2 = relay.Tuple([call_2300,uop_2322,uop_2340,])
func_2342 = relay.Function([], output)
mod['func_2342'] = func_2342
mod = relay.transform.InferType()(mod)
mutated_mod['func_2342'] = func_2342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2342_call = mutated_mod.get_global_var('func_2342')
call_2343 = func_2342_call()
output = call_2343
func_2344 = relay.Function([], output)
mutated_mod['func_2344'] = func_2344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2342_call = mod.get_global_var('func_2342')
func_2344_call = mutated_mod.get_global_var('func_2344')
call_2372 = relay.TupleGetItem(func_2342_call(), 2)
call_2373 = relay.TupleGetItem(func_2344_call(), 2)
output = relay.Tuple([call_2372,])
output2 = relay.Tuple([call_2373,])
func_2379 = relay.Function([], output)
mod['func_2379'] = func_2379
mod = relay.transform.InferType()(mod)
output = func_2379()
func_2380 = relay.Function([], output)
mutated_mod['func_2380'] = func_2380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1378_call = mod.get_global_var('func_1378')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_2406 = func_1378_call()
call_2407 = func_1378_call()
output = relay.Tuple([call_2406,])
output2 = relay.Tuple([call_2407,])
func_2412 = relay.Function([], output)
mod['func_2412'] = func_2412
mod = relay.transform.InferType()(mod)
output = func_2412()
func_2413 = relay.Function([], output)
mutated_mod['func_2413'] = func_2413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1849_call = mod.get_global_var('func_1849')
func_1850_call = mutated_mod.get_global_var('func_1850')
call_2414 = relay.TupleGetItem(func_1849_call(), 0)
call_2415 = relay.TupleGetItem(func_1850_call(), 0)
output = call_2414
output2 = call_2415
func_2419 = relay.Function([], output)
mod['func_2419'] = func_2419
mod = relay.transform.InferType()(mod)
mutated_mod['func_2419'] = func_2419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mutated_mod.get_global_var('func_2419')
call_2420 = func_2419_call()
output = call_2420
func_2421 = relay.Function([], output)
mutated_mod['func_2421'] = func_2421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_590_call = mod.get_global_var('func_590')
func_592_call = mutated_mod.get_global_var('func_592')
call_2451 = func_590_call()
call_2452 = func_590_call()
var_2465 = relay.var("var_2465", dtype = "uint16", shape = (4, 2, 2))#candidate|2465|(4, 2, 2)|var|uint16
bop_2466 = relay.mod(call_2451.astype('float32'), relay.reshape(var_2465.astype('float32'), relay.shape_of(call_2451))) # shape=(4, 2, 2)
bop_2469 = relay.mod(call_2452.astype('float32'), relay.reshape(var_2465.astype('float32'), relay.shape_of(call_2452))) # shape=(4, 2, 2)
func_629_call = mod.get_global_var('func_629')
func_631_call = mutated_mod.get_global_var('func_631')
call_2484 = relay.TupleGetItem(func_629_call(), 1)
call_2485 = relay.TupleGetItem(func_631_call(), 1)
uop_2488 = relay.log(call_2451.astype('float64')) # shape=(4, 2, 2)
uop_2490 = relay.log(call_2452.astype('float64')) # shape=(4, 2, 2)
bop_2491 = relay.divide(uop_2488.astype('float32'), relay.reshape(bop_2466.astype('float32'), relay.shape_of(uop_2488))) # shape=(4, 2, 2)
bop_2494 = relay.divide(uop_2490.astype('float32'), relay.reshape(bop_2469.astype('float32'), relay.shape_of(uop_2490))) # shape=(4, 2, 2)
output = relay.Tuple([call_2484,bop_2491,])
output2 = relay.Tuple([call_2485,bop_2494,])
func_2496 = relay.Function([var_2465,], output)
mod['func_2496'] = func_2496
mod = relay.transform.InferType()(mod)
mutated_mod['func_2496'] = func_2496
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2497 = relay.var("var_2497", dtype = "uint16", shape = (4, 2, 2))#candidate|2497|(4, 2, 2)|var|uint16
func_2496_call = mutated_mod.get_global_var('func_2496')
call_2498 = func_2496_call(var_2497)
output = call_2498
func_2499 = relay.Function([var_2497], output)
mutated_mod['func_2499'] = func_2499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_437_call = mod.get_global_var('func_437')
func_438_call = mutated_mod.get_global_var('func_438')
call_2563 = func_437_call()
call_2564 = func_437_call()
uop_2568 = relay.log2(call_2563.astype('float64')) # shape=(4, 2, 2)
uop_2570 = relay.log2(call_2564.astype('float64')) # shape=(4, 2, 2)
output = uop_2568
output2 = uop_2570
func_2571 = relay.Function([], output)
mod['func_2571'] = func_2571
mod = relay.transform.InferType()(mod)
output = func_2571()
func_2572 = relay.Function([], output)
mutated_mod['func_2572'] = func_2572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mod.get_global_var('func_2412')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_2580 = relay.TupleGetItem(func_2412_call(), 0)
call_2581 = relay.TupleGetItem(func_2413_call(), 0)
var_2591 = relay.var("var_2591", dtype = "uint16", shape = (4, 2, 2))#candidate|2591|(4, 2, 2)|var|uint16
bop_2592 = relay.maximum(call_2580.astype('float64'), relay.reshape(var_2591.astype('float64'), relay.shape_of(call_2580))) # shape=(4, 2, 2)
bop_2595 = relay.maximum(call_2581.astype('float64'), relay.reshape(var_2591.astype('float64'), relay.shape_of(call_2581))) # shape=(4, 2, 2)
output = bop_2592
output2 = bop_2595
func_2598 = relay.Function([var_2591,], output)
mod['func_2598'] = func_2598
mod = relay.transform.InferType()(mod)
mutated_mod['func_2598'] = func_2598
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2599 = relay.var("var_2599", dtype = "uint16", shape = (4, 2, 2))#candidate|2599|(4, 2, 2)|var|uint16
func_2598_call = mutated_mod.get_global_var('func_2598')
call_2600 = func_2598_call(var_2599)
output = call_2600
func_2601 = relay.Function([var_2599], output)
mutated_mod['func_2601'] = func_2601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_2626 = relay.TupleGetItem(func_782_call(), 0)
call_2627 = relay.TupleGetItem(func_783_call(), 0)
output = relay.Tuple([call_2626,])
output2 = relay.Tuple([call_2627,])
func_2630 = relay.Function([], output)
mod['func_2630'] = func_2630
mod = relay.transform.InferType()(mod)
output = func_2630()
func_2631 = relay.Function([], output)
mutated_mod['func_2631'] = func_2631
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2834 = relay.const([[[-7.701403,-1.620381,3.465138,2.800171,-5.369556,-4.369307,-5.367057,8.661580,-0.439170,2.159192,-8.613811,-8.931661,0.577356],[-4.319264,1.261539,2.554410,-2.251539,9.529741,6.101665,-3.765810,-8.233688,-6.614592,6.729232,-1.663997,4.459147,-9.107373],[-4.096751,-2.549057,-9.725327,-8.359989,-7.903867,1.696635,4.375720,-0.007203,1.168936,-7.710557,2.558332,-3.099081,-0.498301],[-2.385925,0.892993,-5.531554,8.991048,3.063872,9.959387,7.581263,4.715443,-7.565342,2.206907,-8.483843,9.890423,-9.900527],[1.827122,-7.792527,-3.529182,-8.038186,0.707742,3.596578,5.371164,-3.503187,-3.880640,-0.775739,-3.918436,-9.607689,6.096470],[-9.575441,5.989689,3.711810,-4.248625,-6.882701,5.349068,-0.524741,4.882240,7.917780,-0.321085,9.464454,-0.836652,5.701747],[4.644733,-9.403245,-0.464413,0.904619,-0.330615,-3.085534,-6.428391,2.059481,3.241778,6.621946,8.120456,9.361714,-8.328779],[-6.376160,-6.923082,-3.949134,2.384717,-2.560482,7.913293,9.385542,1.755816,-5.499083,-3.275075,8.870283,6.127821,1.172798],[5.643950,7.546207,5.743727,-4.659792,3.080123,7.338614,-7.163675,-8.711541,-4.846700,1.222001,5.318304,4.129498,9.493630],[-4.920759,3.396224,9.363977,-1.666746,3.525164,-9.826487,-6.943762,-1.605688,-2.965400,1.649694,-5.645824,-2.119900,8.260747],[-1.043981,5.295844,5.725757,-7.573725,4.921228,-4.646332,-4.792850,-5.719879,4.389499,-3.797315,-6.024765,-3.716734,5.870849],[2.418554,-8.906600,-7.976774,-1.373598,-1.659408,6.681113,-2.905469,-3.780270,-9.931098,-2.853151,6.385901,7.738294,0.065835]]], dtype = "float32")#candidate|2834|(1, 12, 13)|const|float32
var_2835 = relay.var("var_2835", dtype = "float32", shape = (14, 12, 13))#candidate|2835|(14, 12, 13)|var|float32
bop_2836 = relay.power(const_2834.astype('float32'), var_2835.astype('float32')) # shape=(14, 12, 13)
output = bop_2836
output2 = bop_2836
func_2860 = relay.Function([var_2835,], output)
mod['func_2860'] = func_2860
mod = relay.transform.InferType()(mod)
mutated_mod['func_2860'] = func_2860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2861 = relay.var("var_2861", dtype = "float32", shape = (14, 12, 13))#candidate|2861|(14, 12, 13)|var|float32
func_2860_call = mutated_mod.get_global_var('func_2860')
call_2862 = func_2860_call(var_2861)
output = call_2862
func_2863 = relay.Function([var_2861], output)
mutated_mod['func_2863'] = func_2863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_2918 = relay.TupleGetItem(func_314_call(), 0)
call_2919 = relay.TupleGetItem(func_315_call(), 0)
output = call_2918
output2 = call_2919
func_2931 = relay.Function([], output)
mod['func_2931'] = func_2931
mod = relay.transform.InferType()(mod)
output = func_2931()
func_2932 = relay.Function([], output)
mutated_mod['func_2932'] = func_2932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_643_call = mod.get_global_var('func_643')
func_645_call = mutated_mod.get_global_var('func_645')
call_2998 = relay.TupleGetItem(func_643_call(), 0)
call_2999 = relay.TupleGetItem(func_645_call(), 0)
var_3008 = relay.var("var_3008", dtype = "bool", shape = (9, 10, 14))#candidate|3008|(9, 10, 14)|var|bool
bop_3009 = relay.logical_xor(call_2998.astype('int64'), relay.reshape(var_3008.astype('int64'), relay.shape_of(call_2998))) # shape=(9, 10, 14)
bop_3012 = relay.logical_xor(call_2999.astype('int64'), relay.reshape(var_3008.astype('int64'), relay.shape_of(call_2999))) # shape=(9, 10, 14)
func_2860_call = mod.get_global_var('func_2860')
func_2863_call = mutated_mod.get_global_var('func_2863')
var_3016 = relay.var("var_3016", dtype = "float32", shape = (2184,))#candidate|3016|(2184,)|var|float32
call_3015 = func_2860_call(relay.reshape(var_3016.astype('float32'), [14, 12, 13]))
call_3017 = func_2860_call(relay.reshape(var_3016.astype('float32'), [14, 12, 13]))
bop_3031 = relay.floor_mod(call_3015.astype('float32'), relay.reshape(var_3016.astype('float32'), relay.shape_of(call_3015))) # shape=(14, 12, 13)
bop_3034 = relay.floor_mod(call_3017.astype('float32'), relay.reshape(var_3016.astype('float32'), relay.shape_of(call_3017))) # shape=(14, 12, 13)
uop_3041 = relay.asin(bop_3009.astype('float64')) # shape=(9, 10, 14)
uop_3043 = relay.asin(bop_3012.astype('float64')) # shape=(9, 10, 14)
uop_3049 = relay.atanh(bop_3009.astype('float64')) # shape=(9, 10, 14)
uop_3051 = relay.atanh(bop_3012.astype('float64')) # shape=(9, 10, 14)
output = relay.Tuple([bop_3031,uop_3041,uop_3049,])
output2 = relay.Tuple([bop_3034,uop_3043,uop_3051,])
func_3068 = relay.Function([var_3008,var_3016,], output)
mod['func_3068'] = func_3068
mod = relay.transform.InferType()(mod)
mutated_mod['func_3068'] = func_3068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3068_call = mutated_mod.get_global_var('func_3068')
var_3070 = relay.var("var_3070", dtype = "bool", shape = (9, 10, 14))#candidate|3070|(9, 10, 14)|var|bool
var_3071 = relay.var("var_3071", dtype = "float32", shape = (2184,))#candidate|3071|(2184,)|var|float32
call_3069 = func_3068_call(var_3070,var_3071,)
output = call_3069
func_3072 = relay.Function([var_3070,var_3071,], output)
mutated_mod['func_3072'] = func_3072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_629_call = mod.get_global_var('func_629')
func_631_call = mutated_mod.get_global_var('func_631')
call_3215 = relay.TupleGetItem(func_629_call(), 1)
call_3216 = relay.TupleGetItem(func_631_call(), 1)
output = call_3215
output2 = call_3216
func_3217 = relay.Function([], output)
mod['func_3217'] = func_3217
mod = relay.transform.InferType()(mod)
output = func_3217()
func_3218 = relay.Function([], output)
mutated_mod['func_3218'] = func_3218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_3373 = relay.TupleGetItem(func_1636_call(), 0)
call_3374 = relay.TupleGetItem(func_1638_call(), 0)
func_738_call = mod.get_global_var('func_738')
func_739_call = mutated_mod.get_global_var('func_739')
call_3376 = relay.TupleGetItem(func_738_call(), 1)
call_3377 = relay.TupleGetItem(func_739_call(), 1)
var_3383 = relay.var("var_3383", dtype = "uint16", shape = (4, 2, 2))#candidate|3383|(4, 2, 2)|var|uint16
bop_3384 = relay.logical_or(call_3373.astype('bool'), relay.reshape(var_3383.astype('bool'), relay.shape_of(call_3373))) # shape=(4, 2, 2)
bop_3387 = relay.logical_or(call_3374.astype('bool'), relay.reshape(var_3383.astype('bool'), relay.shape_of(call_3374))) # shape=(4, 2, 2)
output = relay.Tuple([call_3376,bop_3384,])
output2 = relay.Tuple([call_3377,bop_3387,])
func_3407 = relay.Function([var_3383,], output)
mod['func_3407'] = func_3407
mod = relay.transform.InferType()(mod)
var_3408 = relay.var("var_3408", dtype = "uint16", shape = (4, 2, 2))#candidate|3408|(4, 2, 2)|var|uint16
output = func_3407(var_3408)
func_3409 = relay.Function([var_3408], output)
mutated_mod['func_3409'] = func_3409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2342_call = mod.get_global_var('func_2342')
func_2344_call = mutated_mod.get_global_var('func_2344')
call_3472 = relay.TupleGetItem(func_2342_call(), 2)
call_3473 = relay.TupleGetItem(func_2344_call(), 2)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_3477 = func_1327_call()
call_3478 = func_1327_call()
var_3488 = relay.var("var_3488", dtype = "float32", shape = (8, 12, 8))#candidate|3488|(8, 12, 8)|var|float32
bop_3489 = relay.greater_equal(call_3477.astype('bool'), relay.reshape(var_3488.astype('bool'), relay.shape_of(call_3477))) # shape=(8, 12, 8)
bop_3492 = relay.greater_equal(call_3478.astype('bool'), relay.reshape(var_3488.astype('bool'), relay.shape_of(call_3478))) # shape=(8, 12, 8)
func_822_call = mod.get_global_var('func_822')
func_825_call = mutated_mod.get_global_var('func_825')
const_3494 = relay.const([True,False,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,False,False], dtype = "bool")#candidate|3494|(1260,)|const|bool
call_3493 = relay.TupleGetItem(func_822_call(relay.reshape(const_3494.astype('bool'), [9, 10, 14])), 2)
call_3495 = relay.TupleGetItem(func_825_call(relay.reshape(const_3494.astype('bool'), [9, 10, 14])), 2)
func_782_call = mod.get_global_var('func_782')
func_783_call = mutated_mod.get_global_var('func_783')
call_3503 = relay.TupleGetItem(func_782_call(), 0)
call_3504 = relay.TupleGetItem(func_783_call(), 0)
output = relay.Tuple([call_3472,bop_3489,call_3493,const_3494,call_3503,])
output2 = relay.Tuple([call_3473,bop_3492,call_3495,const_3494,call_3504,])
func_3521 = relay.Function([var_3488,], output)
mod['func_3521'] = func_3521
mod = relay.transform.InferType()(mod)
mutated_mod['func_3521'] = func_3521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3522 = relay.var("var_3522", dtype = "float32", shape = (8, 12, 8))#candidate|3522|(8, 12, 8)|var|float32
func_3521_call = mutated_mod.get_global_var('func_3521')
call_3523 = func_3521_call(var_3522)
output = call_3523
func_3524 = relay.Function([var_3522], output)
mutated_mod['func_3524'] = func_3524
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3530 = relay.var("var_3530", dtype = "float64", shape = (12, 5, 14))#candidate|3530|(12, 5, 14)|var|float64
uop_3531 = relay.log(var_3530.astype('float64')) # shape=(12, 5, 14)
output = uop_3531
output2 = uop_3531
func_3534 = relay.Function([var_3530,], output)
mod['func_3534'] = func_3534
mod = relay.transform.InferType()(mod)
var_3535 = relay.var("var_3535", dtype = "float64", shape = (12, 5, 14))#candidate|3535|(12, 5, 14)|var|float64
output = func_3534(var_3535)
func_3536 = relay.Function([var_3535], output)
mutated_mod['func_3536'] = func_3536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3217_call = mod.get_global_var('func_3217')
func_3218_call = mutated_mod.get_global_var('func_3218')
call_3543 = func_3217_call()
call_3544 = func_3217_call()
func_2412_call = mod.get_global_var('func_2412')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_3545 = relay.TupleGetItem(func_2412_call(), 0)
call_3546 = relay.TupleGetItem(func_2413_call(), 0)
output = relay.Tuple([call_3543,call_3545,])
output2 = relay.Tuple([call_3544,call_3546,])
func_3563 = relay.Function([], output)
mod['func_3563'] = func_3563
mod = relay.transform.InferType()(mod)
output = func_3563()
func_3564 = relay.Function([], output)
mutated_mod['func_3564'] = func_3564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
call_3624 = relay.TupleGetItem(func_475_call(), 0)
call_3625 = relay.TupleGetItem(func_477_call(), 0)
output = relay.Tuple([call_3624,])
output2 = relay.Tuple([call_3625,])
func_3627 = relay.Function([], output)
mod['func_3627'] = func_3627
mod = relay.transform.InferType()(mod)
output = func_3627()
func_3628 = relay.Function([], output)
mutated_mod['func_3628'] = func_3628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2379_call = mod.get_global_var('func_2379')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_3642 = relay.TupleGetItem(func_2379_call(), 0)
call_3643 = relay.TupleGetItem(func_2380_call(), 0)
output = call_3642
output2 = call_3643
func_3644 = relay.Function([], output)
mod['func_3644'] = func_3644
mod = relay.transform.InferType()(mod)
output = func_3644()
func_3645 = relay.Function([], output)
mutated_mod['func_3645'] = func_3645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_3714 = relay.TupleGetItem(func_401_call(), 0)
call_3715 = relay.TupleGetItem(func_402_call(), 0)
func_3407_call = mod.get_global_var('func_3407')
func_3409_call = mutated_mod.get_global_var('func_3409')
call_3720 = relay.TupleGetItem(func_3407_call(relay.reshape(call_3714.astype('uint16'), [4, 2, 2])), 1)
call_3721 = relay.TupleGetItem(func_3409_call(relay.reshape(call_3714.astype('uint16'), [4, 2, 2])), 1)
uop_3722 = relay.sinh(call_3720.astype('float64')) # shape=(4, 2, 2)
uop_3724 = relay.sinh(call_3721.astype('float64')) # shape=(4, 2, 2)
output = relay.Tuple([call_3714,uop_3722,])
output2 = relay.Tuple([call_3715,uop_3724,])
func_3727 = relay.Function([], output)
mod['func_3727'] = func_3727
mod = relay.transform.InferType()(mod)
output = func_3727()
func_3728 = relay.Function([], output)
mutated_mod['func_3728'] = func_3728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mod.get_global_var('func_2412')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_3741 = relay.TupleGetItem(func_2412_call(), 0)
call_3742 = relay.TupleGetItem(func_2413_call(), 0)
func_1990_call = mod.get_global_var('func_1990')
func_1992_call = mutated_mod.get_global_var('func_1992')
var_3754 = relay.var("var_3754", dtype = "uint32", shape = (1, 168))#candidate|3754|(1, 168)|var|uint32
call_3753 = relay.TupleGetItem(func_1990_call(relay.reshape(var_3754.astype('uint32'), [168,])), 1)
call_3755 = relay.TupleGetItem(func_1992_call(relay.reshape(var_3754.astype('uint32'), [168,])), 1)
output = relay.Tuple([call_3741,call_3753,var_3754,])
output2 = relay.Tuple([call_3742,call_3755,var_3754,])
func_3762 = relay.Function([var_3754,], output)
mod['func_3762'] = func_3762
mod = relay.transform.InferType()(mod)
var_3763 = relay.var("var_3763", dtype = "uint32", shape = (1, 168))#candidate|3763|(1, 168)|var|uint32
output = func_3762(var_3763)
func_3764 = relay.Function([var_3763], output)
mutated_mod['func_3764'] = func_3764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3563_call = mod.get_global_var('func_3563')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_3809 = relay.TupleGetItem(func_3563_call(), 1)
call_3810 = relay.TupleGetItem(func_3564_call(), 1)
uop_3812 = relay.sqrt(call_3809.astype('float32')) # shape=(4, 2, 2)
uop_3814 = relay.sqrt(call_3810.astype('float32')) # shape=(4, 2, 2)
func_437_call = mod.get_global_var('func_437')
func_438_call = mutated_mod.get_global_var('func_438')
call_3818 = func_437_call()
call_3819 = func_437_call()
uop_3822 = relay.acos(call_3818.astype('float32')) # shape=(4, 2, 2)
uop_3824 = relay.acos(call_3819.astype('float32')) # shape=(4, 2, 2)
func_2931_call = mod.get_global_var('func_2931')
func_2932_call = mutated_mod.get_global_var('func_2932')
call_3836 = func_2931_call()
call_3837 = func_2931_call()
func_738_call = mod.get_global_var('func_738')
func_739_call = mutated_mod.get_global_var('func_739')
call_3838 = relay.TupleGetItem(func_738_call(), 1)
call_3839 = relay.TupleGetItem(func_739_call(), 1)
output = relay.Tuple([uop_3812,uop_3822,call_3836,call_3838,])
output2 = relay.Tuple([uop_3814,uop_3824,call_3837,call_3839,])
func_3841 = relay.Function([], output)
mod['func_3841'] = func_3841
mod = relay.transform.InferType()(mod)
output = func_3841()
func_3842 = relay.Function([], output)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3888 = relay.var("var_3888", dtype = "float64", shape = (1, 6, 13))#candidate|3888|(1, 6, 13)|var|float64
var_3889 = relay.var("var_3889", dtype = "float64", shape = (16, 6, 13))#candidate|3889|(16, 6, 13)|var|float64
bop_3890 = relay.power(var_3888.astype('float64'), var_3889.astype('float64')) # shape=(16, 6, 13)
func_3627_call = mod.get_global_var('func_3627')
func_3628_call = mutated_mod.get_global_var('func_3628')
call_3910 = relay.TupleGetItem(func_3627_call(), 0)
call_3911 = relay.TupleGetItem(func_3628_call(), 0)
func_1387_call = mod.get_global_var('func_1387')
func_1390_call = mutated_mod.get_global_var('func_1390')
var_3917 = relay.var("var_3917", dtype = "float64", shape = (28,))#candidate|3917|(28,)|var|float64
call_3916 = relay.TupleGetItem(func_1387_call(relay.reshape(var_3917.astype('float64'), [7, 2, 2])), 0)
call_3918 = relay.TupleGetItem(func_1390_call(relay.reshape(var_3917.astype('float64'), [7, 2, 2])), 0)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_3922 = relay.TupleGetItem(func_1636_call(), 0)
call_3923 = relay.TupleGetItem(func_1638_call(), 0)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
var_3927 = relay.var("var_3927", dtype = "float64", shape = (840, 1))#candidate|3927|(840, 1)|var|float64
call_3926 = func_3534_call(relay.reshape(var_3927.astype('float64'), [12, 5, 14]))
call_3928 = func_3534_call(relay.reshape(var_3927.astype('float64'), [12, 5, 14]))
output = relay.Tuple([bop_3890,call_3910,call_3916,var_3917,call_3922,call_3926,var_3927,])
output2 = relay.Tuple([bop_3890,call_3911,call_3918,var_3917,call_3923,call_3928,var_3927,])
func_3929 = relay.Function([var_3888,var_3889,var_3917,var_3927,], output)
mod['func_3929'] = func_3929
mod = relay.transform.InferType()(mod)
mutated_mod['func_3929'] = func_3929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3929_call = mutated_mod.get_global_var('func_3929')
var_3931 = relay.var("var_3931", dtype = "float64", shape = (1, 6, 13))#candidate|3931|(1, 6, 13)|var|float64
var_3932 = relay.var("var_3932", dtype = "float64", shape = (16, 6, 13))#candidate|3932|(16, 6, 13)|var|float64
var_3933 = relay.var("var_3933", dtype = "float64", shape = (28,))#candidate|3933|(28,)|var|float64
var_3934 = relay.var("var_3934", dtype = "float64", shape = (840, 1))#candidate|3934|(840, 1)|var|float64
call_3930 = func_3929_call(var_3931,var_3932,var_3933,var_3934,)
output = call_3930
func_3935 = relay.Function([var_3931,var_3932,var_3933,var_3934,], output)
mutated_mod['func_3935'] = func_3935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_3949 = func_2571_call()
call_3950 = func_2571_call()
output = relay.Tuple([call_3949,])
output2 = relay.Tuple([call_3950,])
func_3963 = relay.Function([], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
output = func_3963()
func_3964 = relay.Function([], output)
mutated_mod['func_3964'] = func_3964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_4031 = func_1327_call()
call_4032 = func_1327_call()
func_1088_call = mod.get_global_var('func_1088')
func_1091_call = mutated_mod.get_global_var('func_1091')
var_4039 = relay.var("var_4039", dtype = "uint16", shape = (16,))#candidate|4039|(16,)|var|uint16
call_4038 = relay.TupleGetItem(func_1088_call(relay.reshape(var_4039.astype('uint16'), [4, 2, 2])), 0)
call_4040 = relay.TupleGetItem(func_1091_call(relay.reshape(var_4039.astype('uint16'), [4, 2, 2])), 0)
output = relay.Tuple([call_4031,call_4038,var_4039,])
output2 = relay.Tuple([call_4032,call_4040,var_4039,])
func_4041 = relay.Function([var_4039,], output)
mod['func_4041'] = func_4041
mod = relay.transform.InferType()(mod)
mutated_mod['func_4041'] = func_4041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4042 = relay.var("var_4042", dtype = "uint16", shape = (16,))#candidate|4042|(16,)|var|uint16
func_4041_call = mutated_mod.get_global_var('func_4041')
call_4043 = func_4041_call(var_4042)
output = call_4043
func_4044 = relay.Function([var_4042], output)
mutated_mod['func_4044'] = func_4044
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4055 = relay.var("var_4055", dtype = "int32", shape = (12, 5, 9))#candidate|4055|(12, 5, 9)|var|int32
var_4056 = relay.var("var_4056", dtype = "int32", shape = (12, 5, 9))#candidate|4056|(12, 5, 9)|var|int32
bop_4057 = relay.subtract(var_4055.astype('int32'), relay.reshape(var_4056.astype('int32'), relay.shape_of(var_4055))) # shape=(12, 5, 9)
output = bop_4057
output2 = bop_4057
func_4064 = relay.Function([var_4055,var_4056,], output)
mod['func_4064'] = func_4064
mod = relay.transform.InferType()(mod)
mutated_mod['func_4064'] = func_4064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4064_call = mutated_mod.get_global_var('func_4064')
var_4066 = relay.var("var_4066", dtype = "int32", shape = (12, 5, 9))#candidate|4066|(12, 5, 9)|var|int32
var_4067 = relay.var("var_4067", dtype = "int32", shape = (12, 5, 9))#candidate|4067|(12, 5, 9)|var|int32
call_4065 = func_4064_call(var_4066,var_4067,)
output = call_4065
func_4068 = relay.Function([var_4066,var_4067,], output)
mutated_mod['func_4068'] = func_4068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_437_call = mod.get_global_var('func_437')
func_438_call = mutated_mod.get_global_var('func_438')
call_4092 = func_437_call()
call_4093 = func_437_call()
output = relay.Tuple([call_4092,])
output2 = relay.Tuple([call_4093,])
func_4105 = relay.Function([], output)
mod['func_4105'] = func_4105
mod = relay.transform.InferType()(mod)
output = func_4105()
func_4106 = relay.Function([], output)
mutated_mod['func_4106'] = func_4106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_4114 = func_210_call()
call_4115 = func_210_call()
output = relay.Tuple([call_4114,])
output2 = relay.Tuple([call_4115,])
func_4120 = relay.Function([], output)
mod['func_4120'] = func_4120
mod = relay.transform.InferType()(mod)
mutated_mod['func_4120'] = func_4120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4120_call = mutated_mod.get_global_var('func_4120')
call_4121 = func_4120_call()
output = call_4121
func_4122 = relay.Function([], output)
mutated_mod['func_4122'] = func_4122
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4139 = relay.const([[[-4.702031,-6.097281,-1.751884,3.179838]],[[5.992315,-9.519111,-5.642143,-8.955791]],[[-0.576425,-6.968309,-8.200795,-3.426864]],[[-9.231420,-6.384256,5.038669,1.143509]],[[-9.941583,-9.464333,-7.037122,8.843269]],[[-2.092916,1.638401,-5.806358,-5.503580]],[[-4.723416,0.974004,4.714685,1.644496]],[[1.399182,1.073877,5.886681,-7.727609]],[[-6.660845,1.061668,4.927160,4.455830]],[[-6.407161,-3.853254,-0.247110,1.442381]],[[5.572506,7.702650,1.426399,-4.147425]],[[-9.471043,9.882916,-1.923545,-2.630001]],[[-8.589616,-9.150214,-6.514566,3.681523]],[[-7.154847,7.161128,-7.772303,-2.313688]],[[3.565414,-0.785766,-4.111625,1.599944]],[[-6.210410,4.207273,-2.863135,-4.243029]]], dtype = "float32")#candidate|4139|(16, 1, 4)|const|float32
uop_4140 = relay.acos(const_4139.astype('float32')) # shape=(16, 1, 4)
var_4143 = relay.var("var_4143", dtype = "float32", shape = (16, 10, 4))#candidate|4143|(16, 10, 4)|var|float32
bop_4144 = relay.multiply(uop_4140.astype('float64'), var_4143.astype('float64')) # shape=(16, 10, 4)
output = relay.Tuple([bop_4144,])
output2 = relay.Tuple([bop_4144,])
func_4157 = relay.Function([var_4143,], output)
mod['func_4157'] = func_4157
mod = relay.transform.InferType()(mod)
var_4158 = relay.var("var_4158", dtype = "float32", shape = (16, 10, 4))#candidate|4158|(16, 10, 4)|var|float32
output = func_4157(var_4158)
func_4159 = relay.Function([var_4158], output)
mutated_mod['func_4159'] = func_4159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3627_call = mod.get_global_var('func_3627')
func_3628_call = mutated_mod.get_global_var('func_3628')
call_4161 = relay.TupleGetItem(func_3627_call(), 0)
call_4162 = relay.TupleGetItem(func_3628_call(), 0)
func_965_call = mod.get_global_var('func_965')
func_969_call = mutated_mod.get_global_var('func_969')
var_4166 = relay.var("var_4166", dtype = "int16", shape = ())#candidate|4166|()|var|int16
var_4167 = relay.var("var_4167", dtype = "int16", shape = (490,))#candidate|4167|(490,)|var|int16
call_4165 = relay.TupleGetItem(func_965_call(relay.reshape(var_4166.astype('int16'), []), relay.reshape(var_4167.astype('int16'), [14, 5, 7]), ), 0)
call_4168 = relay.TupleGetItem(func_969_call(relay.reshape(var_4166.astype('int16'), []), relay.reshape(var_4167.astype('int16'), [14, 5, 7]), ), 0)
uop_4170 = relay.sinh(var_4167.astype('float64')) # shape=(490,)
var_4187 = relay.var("var_4187", dtype = "float64", shape = (490,))#candidate|4187|(490,)|var|float64
bop_4188 = relay.right_shift(uop_4170.astype('uint8'), relay.reshape(var_4187.astype('uint8'), relay.shape_of(uop_4170))) # shape=(490,)
output = relay.Tuple([call_4161,call_4165,var_4166,bop_4188,])
output2 = relay.Tuple([call_4162,call_4168,var_4166,bop_4188,])
func_4192 = relay.Function([var_4166,var_4167,var_4187,], output)
mod['func_4192'] = func_4192
mod = relay.transform.InferType()(mod)
var_4193 = relay.var("var_4193", dtype = "int16", shape = ())#candidate|4193|()|var|int16
var_4194 = relay.var("var_4194", dtype = "int16", shape = (490,))#candidate|4194|(490,)|var|int16
var_4195 = relay.var("var_4195", dtype = "float64", shape = (490,))#candidate|4195|(490,)|var|float64
output = func_4192(var_4193,var_4194,var_4195,)
func_4196 = relay.Function([var_4193,var_4194,var_4195,], output)
mutated_mod['func_4196'] = func_4196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2630_call = mod.get_global_var('func_2630')
func_2631_call = mutated_mod.get_global_var('func_2631')
call_4198 = relay.TupleGetItem(func_2630_call(), 0)
call_4199 = relay.TupleGetItem(func_2631_call(), 0)
func_1378_call = mod.get_global_var('func_1378')
func_1379_call = mutated_mod.get_global_var('func_1379')
call_4208 = func_1378_call()
call_4209 = func_1378_call()
output = relay.Tuple([call_4198,call_4208,])
output2 = relay.Tuple([call_4199,call_4209,])
func_4211 = relay.Function([], output)
mod['func_4211'] = func_4211
mod = relay.transform.InferType()(mod)
output = func_4211()
func_4212 = relay.Function([], output)
mutated_mod['func_4212'] = func_4212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_4221 = relay.TupleGetItem(func_3841_call(), 3)
call_4222 = relay.TupleGetItem(func_3842_call(), 3)
output = relay.Tuple([call_4221,])
output2 = relay.Tuple([call_4222,])
func_4227 = relay.Function([], output)
mod['func_4227'] = func_4227
mod = relay.transform.InferType()(mod)
output = func_4227()
func_4228 = relay.Function([], output)
mutated_mod['func_4228'] = func_4228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_4239 = func_1327_call()
call_4240 = func_1327_call()
const_4241 = relay.const([[[0.513293,6.570148,-3.332225,3.286250,-2.351345,5.611557,8.283111,-1.030600],[9.758569,5.751269,7.619402,-7.067581,4.118138,8.082974,2.220193,-9.275347],[-4.549725,-2.138900,-1.948821,-1.054240,-8.069182,9.795457,9.842275,-3.671731],[1.416818,-6.064806,-3.007295,-8.623204,-4.304728,2.557799,-5.075094,-6.423673],[-3.200115,3.070899,-7.945426,5.693656,2.879911,-4.508656,8.868996,2.356995],[-3.963850,8.694986,-4.594353,-0.936143,5.004256,-3.918389,-9.144770,-4.448136],[-8.371591,2.323273,3.220655,5.210021,-6.580571,9.052653,-0.180265,-8.766646],[8.211377,8.457333,3.077832,-0.158293,-6.976612,-9.531406,-7.669820,8.379688],[-8.988429,0.543699,9.840968,-5.043163,0.783329,1.903331,-4.875081,-6.872234],[4.856133,-7.989621,-9.773133,3.799081,7.183449,7.910027,-0.560896,-5.443730],[1.262753,-5.575926,-2.416169,-9.138907,5.297251,-1.498691,3.538593,6.791101],[-2.492161,9.631924,-8.787747,1.871610,-0.488752,2.067352,3.275207,1.060862]],[[-1.859093,-4.666253,-7.874400,-0.552307,-9.163598,-2.429082,5.939987,1.542715],[2.468103,-0.618375,9.228126,7.191998,-7.528465,9.450697,5.560226,4.960034],[-3.984842,-7.948190,-4.361351,-2.653397,5.527546,2.084838,-9.437558,2.235038],[3.957375,-3.488391,7.151820,8.772409,-6.755000,-0.669202,6.721937,2.962284],[3.961056,6.742563,-0.966775,-0.196018,-0.743924,7.582656,-0.399982,-4.359516],[-2.149069,3.156273,-8.416217,-8.480632,2.696150,-8.835013,-0.233917,-3.721536],[-8.780562,7.807437,-4.053357,-7.991265,9.497627,3.109827,-4.600676,-0.655563],[-4.890207,2.594330,-7.959764,-9.318667,-4.293112,-8.173385,-1.589074,-2.096830],[-3.911993,-3.389981,3.419575,0.155599,-9.289231,1.007719,-1.113369,4.750570],[8.238491,-8.949491,-0.651623,8.776496,9.011484,9.603504,-4.257140,-0.413025],[-5.385415,9.482746,-1.121781,-6.599102,-4.470122,0.574222,1.701064,6.365377],[4.042703,-3.917928,-8.678594,-9.445936,-6.142030,-8.499995,7.389906,8.982539]],[[3.408381,-2.432676,-2.691869,-9.819345,-0.835216,1.087281,-2.576543,-2.088340],[-6.839096,-8.269845,-9.482792,8.111241,-3.918832,5.023548,-9.245521,3.494795],[-7.385157,5.974384,4.177548,1.278894,-1.344285,9.798352,3.540938,-9.704163],[6.042287,6.572691,-6.436354,-2.548822,-6.026720,-3.750159,-7.093678,-5.495774],[5.730634,3.576262,7.276861,-4.297347,-6.048168,-0.309476,9.681490,3.014248],[2.919692,-6.715761,0.706288,3.370064,6.242985,6.437389,4.430713,-7.661321],[3.668339,0.804788,-9.733049,-2.466219,-7.397811,-8.335944,-5.290659,-8.138675],[-5.080707,3.915852,0.491842,4.544563,-8.907772,-0.276309,-1.067212,7.922835],[7.392940,-8.127197,-3.090079,-4.101764,-8.621322,4.458076,-0.467378,-2.590545],[-1.688872,0.550687,-6.419984,-1.763390,2.819582,4.893442,3.391439,6.799296],[6.999753,-3.263203,7.755368,-1.052860,-1.511434,-5.577004,3.821021,8.135017],[-5.467441,8.624689,-1.918240,8.596024,0.605823,6.447136,8.455175,0.844531]],[[6.209869,9.157346,-9.512328,-5.070882,8.327352,0.093649,6.317414,-9.171747],[9.893761,1.586343,-1.889678,0.949504,0.308225,-4.741656,-8.932043,1.767604],[-4.173551,-5.015464,4.108197,0.145956,8.135097,6.478540,1.163192,-2.436033],[-0.725500,-2.114621,-4.299438,-3.644853,2.172448,1.132127,-8.085895,0.104104],[6.040522,9.216302,-4.744368,2.532794,1.807254,-3.785851,-6.647924,-9.229487],[-0.910533,7.591147,-8.898610,-3.516468,4.210922,1.612902,6.389124,-7.180715],[-0.981452,4.557977,-1.874834,-1.519081,6.935684,-5.890690,8.390701,-9.852101],[-1.422679,7.893918,3.555849,-5.280852,4.378820,-4.882847,-5.914147,4.261277],[-6.724278,0.998747,4.728162,9.899185,-5.545498,-4.086804,-3.862115,-2.463947],[6.879818,2.549554,3.038834,5.555695,-3.081402,2.898421,-2.643415,8.681111],[4.041834,6.108889,9.044988,-9.389266,-4.079872,3.610569,2.393401,8.595174],[5.400369,-8.420637,-1.176537,8.397927,6.242254,2.802854,3.388918,4.608056]],[[7.827078,6.418284,2.949329,1.741297,7.339842,-0.650667,-8.668081,5.220448],[-7.901547,-8.089377,9.574276,0.480834,8.314975,-3.076721,-7.227143,8.239601],[-9.665915,-2.004454,-2.679801,1.338810,-2.679864,2.037924,-5.415305,3.170521],[-1.422712,5.052057,0.671982,-9.856863,-0.793122,-6.247694,-3.336003,-5.290755],[-2.048666,-5.422486,-9.084177,-8.371753,7.825361,7.799380,-9.509486,4.611858],[4.739270,-8.606886,0.431941,6.479207,1.041933,-6.866484,9.592775,-7.941220],[9.813523,4.768230,6.940946,3.895872,1.066461,-6.879095,7.691481,-6.891681],[-6.370710,7.537023,0.332334,8.053316,-1.818109,3.081656,2.626229,-7.988041],[-6.613377,-3.175789,5.702006,5.661693,4.020990,8.424555,3.791400,2.013854],[-9.644174,2.761319,9.161710,2.285038,9.991143,0.218518,-6.944944,0.667529],[9.606596,-3.245539,0.238417,4.627947,2.190837,9.031263,-8.516691,8.185693],[-3.609961,9.382394,6.299280,6.482282,7.362433,5.602680,-3.725997,-5.132542]],[[0.460307,6.690949,-9.339357,7.333391,2.877813,-3.918311,5.263175,-1.741862],[2.026663,4.664514,-2.169145,1.817641,8.256966,-6.518734,9.861554,-6.033398],[9.648875,-3.914811,-6.201396,-2.905596,-1.385645,-2.381842,-4.467509,7.190441],[-6.011661,-2.117497,-5.170172,-2.248872,7.620335,3.269311,9.308771,2.569454],[1.881343,9.712367,3.556695,5.070694,-8.246794,4.869143,9.771468,-2.097571],[2.173310,-4.104207,-8.847990,9.448108,5.948057,4.516470,-3.359176,-6.617909],[-2.459140,-1.569330,2.208912,6.135763,5.559584,-1.079279,-1.472973,-0.688976],[7.040028,0.360191,6.254066,6.348746,1.235347,7.310615,1.760191,-1.263946],[3.141243,9.455560,-5.756639,1.863742,3.971544,-5.201039,-8.199975,1.821033],[-4.777792,-1.347278,-4.103546,-2.330515,-2.300119,0.705525,5.444993,7.920513],[-2.018920,7.288198,5.190512,-5.698331,-4.670509,-7.536315,3.801374,6.561940],[-5.971907,3.552219,2.537229,6.520888,-6.585404,-7.430284,-9.875035,-5.552018]],[[-6.157036,3.226885,-7.452754,1.559040,7.440394,-6.482061,5.544483,-4.511831],[2.952330,-7.959554,7.403347,-1.702504,9.693000,-5.798285,-2.886872,-3.915342],[-9.279219,-3.891953,-3.891298,-5.644422,-4.895899,-6.167503,-6.551324,7.447925],[3.734164,-8.077203,6.682406,-5.442541,2.133342,-8.494322,6.508836,0.246747],[2.382644,2.280034,6.669022,7.485279,-6.671373,8.951832,-5.686205,-2.541796],[3.988140,-6.076783,0.621238,6.138847,6.408982,-4.022656,-6.915781,3.807733],[6.003628,9.465898,-3.831242,-0.524394,9.090483,1.983305,5.057790,5.369173],[-1.197558,2.596984,-6.121714,9.235562,7.540531,-6.338047,6.744912,8.222497],[-6.349929,6.486715,6.276219,2.983419,8.638719,-1.173815,-0.465929,7.847075],[4.082246,-8.747244,1.658252,-2.914229,1.628192,4.071290,-5.574019,-5.057154],[8.958299,9.492379,4.205004,0.855960,6.705696,4.721685,5.309943,-1.853874],[-3.077198,-0.852938,-1.321877,-0.972227,-4.977749,-6.753168,-2.862823,6.930209]],[[-2.119819,-6.336694,-4.268017,1.038126,5.635348,5.020474,1.320711,9.424201],[7.744004,-6.437071,-3.322939,6.133813,-2.472981,8.708539,-4.273439,-9.690608],[7.109858,6.883520,5.751514,0.480578,6.011403,7.144095,8.857416,-9.710132],[0.369660,-3.873855,0.563102,-2.976151,-9.099115,-4.591720,-9.226070,9.090187],[9.924234,4.347823,3.328655,3.014670,-2.205045,-3.131964,-8.395079,-7.710599],[9.037206,9.821673,-7.373049,-8.600701,-2.984733,-9.146471,0.784385,-5.060940],[-7.755707,3.348162,2.103074,-2.102643,-1.208807,4.921098,-5.527472,-7.233628],[-0.982151,-4.277284,8.057235,3.153392,-8.127927,-2.494085,-4.453253,-6.882827],[1.176549,-2.687098,3.594531,-9.620515,3.700638,-1.190114,3.075143,1.046098],[-4.411906,-4.745493,-8.766019,8.075403,8.508000,8.559187,0.641470,-1.302218],[7.838801,8.068135,-5.554106,-4.160704,2.878978,2.980383,3.029747,-7.661862],[-9.537007,9.113631,5.845512,1.186703,3.473077,-7.571564,7.279812,8.132117]]], dtype = "float32")#candidate|4241|(8, 12, 8)|const|float32
bop_4242 = relay.subtract(call_4239.astype('float32'), relay.reshape(const_4241.astype('float32'), relay.shape_of(call_4239))) # shape=(8, 12, 8)
bop_4245 = relay.subtract(call_4240.astype('float32'), relay.reshape(const_4241.astype('float32'), relay.shape_of(call_4240))) # shape=(8, 12, 8)
func_965_call = mod.get_global_var('func_965')
func_969_call = mutated_mod.get_global_var('func_969')
const_4248 = relay.const(-4, dtype = "int16")#candidate|4248|()|const|int16
var_4249 = relay.var("var_4249", dtype = "int16", shape = (245, 2))#candidate|4249|(245, 2)|var|int16
call_4247 = relay.TupleGetItem(func_965_call(relay.reshape(const_4248.astype('int16'), []), relay.reshape(var_4249.astype('int16'), [14, 5, 7]), ), 0)
call_4250 = relay.TupleGetItem(func_969_call(relay.reshape(const_4248.astype('int16'), []), relay.reshape(var_4249.astype('int16'), [14, 5, 7]), ), 0)
output = relay.Tuple([bop_4242,call_4247,const_4248,var_4249,])
output2 = relay.Tuple([bop_4245,call_4250,const_4248,var_4249,])
func_4258 = relay.Function([var_4249,], output)
mod['func_4258'] = func_4258
mod = relay.transform.InferType()(mod)
var_4259 = relay.var("var_4259", dtype = "int16", shape = (245, 2))#candidate|4259|(245, 2)|var|int16
output = func_4258(var_4259)
func_4260 = relay.Function([var_4259], output)
mutated_mod['func_4260'] = func_4260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_4312 = relay.TupleGetItem(func_290_call(), 0)
call_4313 = relay.TupleGetItem(func_291_call(), 0)
output = call_4312
output2 = call_4313
func_4319 = relay.Function([], output)
mod['func_4319'] = func_4319
mod = relay.transform.InferType()(mod)
output = func_4319()
func_4320 = relay.Function([], output)
mutated_mod['func_4320'] = func_4320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_4366 = func_210_call()
call_4367 = func_210_call()
output = call_4366
output2 = call_4367
func_4373 = relay.Function([], output)
mod['func_4373'] = func_4373
mod = relay.transform.InferType()(mod)
output = func_4373()
func_4374 = relay.Function([], output)
mutated_mod['func_4374'] = func_4374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_4442 = relay.TupleGetItem(func_1636_call(), 0)
call_4443 = relay.TupleGetItem(func_1638_call(), 0)
output = call_4442
output2 = call_4443
func_4444 = relay.Function([], output)
mod['func_4444'] = func_4444
mod = relay.transform.InferType()(mod)
output = func_4444()
func_4445 = relay.Function([], output)
mutated_mod['func_4445'] = func_4445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1636_call = mod.get_global_var('func_1636')
func_1638_call = mutated_mod.get_global_var('func_1638')
call_4457 = relay.TupleGetItem(func_1636_call(), 0)
call_4458 = relay.TupleGetItem(func_1638_call(), 0)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_4461 = func_1327_call()
call_4462 = func_1327_call()
output = relay.Tuple([call_4457,call_4461,])
output2 = relay.Tuple([call_4458,call_4462,])
func_4477 = relay.Function([], output)
mod['func_4477'] = func_4477
mod = relay.transform.InferType()(mod)
output = func_4477()
func_4478 = relay.Function([], output)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1661_call = mod.get_global_var('func_1661')
func_1663_call = mutated_mod.get_global_var('func_1663')
call_4533 = relay.TupleGetItem(func_1661_call(), 2)
call_4534 = relay.TupleGetItem(func_1663_call(), 2)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_4540 = relay.TupleGetItem(func_290_call(), 0)
call_4541 = relay.TupleGetItem(func_291_call(), 0)
output = relay.Tuple([call_4533,call_4540,])
output2 = relay.Tuple([call_4534,call_4541,])
func_4543 = relay.Function([], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
output = func_4543()
func_4544 = relay.Function([], output)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3727_call = mod.get_global_var('func_3727')
func_3728_call = mutated_mod.get_global_var('func_3728')
call_4551 = relay.TupleGetItem(func_3727_call(), 0)
call_4552 = relay.TupleGetItem(func_3728_call(), 0)
func_4543_call = mod.get_global_var('func_4543')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_4561 = relay.TupleGetItem(func_4543_call(), 0)
call_4562 = relay.TupleGetItem(func_4544_call(), 0)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4563 = relay.TupleGetItem(func_4227_call(), 0)
call_4564 = relay.TupleGetItem(func_4228_call(), 0)
output = relay.Tuple([call_4551,call_4561,call_4563,])
output2 = relay.Tuple([call_4552,call_4562,call_4564,])
func_4587 = relay.Function([], output)
mod['func_4587'] = func_4587
mod = relay.transform.InferType()(mod)
output = func_4587()
func_4588 = relay.Function([], output)
mutated_mod['func_4588'] = func_4588
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4710 = relay.const([[[-6,10,6,5,-1,10,-3,-10,-9,-1,-4,10,1,8,-1],[-7,-2,2,-10,2,4,-1,-8,-10,-3,-5,-10,-1,-7,10],[-2,5,-2,9,-4,3,4,4,2,-7,3,-2,-9,3,1],[-3,10,6,5,-4,-8,-8,1,-2,-6,-8,3,1,2,-7],[1,8,8,-5,-9,3,-8,-8,2,1,-3,6,-10,9,5],[7,-7,-7,-8,9,3,-5,-4,-9,-4,-6,-1,4,-1,5],[8,4,-8,-10,5,-6,-3,7,-5,-6,7,8,4,1,-3],[-3,-2,-8,-10,-9,-10,-1,-5,4,5,10,2,3,-8,-5],[-3,-3,7,-7,2,10,-2,-6,-9,8,-10,7,-4,10,-5],[4,3,-4,1,-5,-7,2,6,-8,-8,-1,5,-10,10,-3],[-5,4,-6,-8,10,-9,-10,8,-1,-3,5,7,3,10,-9],[8,-2,2,1,-5,5,9,7,5,6,-6,3,-10,3,2],[5,-6,2,-4,-9,-3,-5,2,-10,7,-5,6,8,-6,7],[1,-6,8,-4,-1,1,7,-6,7,6,-1,-9,-8,-2,6],[-10,1,5,-6,-10,-1,-10,-9,7,-4,2,-1,10,-7,-4]],[[2,-3,10,10,6,2,3,8,-2,-1,-8,-10,3,-8,2],[7,-6,7,-8,-1,-7,4,6,-3,6,5,-7,1,-4,-2],[3,-2,-10,4,-4,-2,9,-10,-7,3,8,-5,2,-5,-9],[5,-6,10,6,4,10,-10,4,-3,-4,4,6,-7,9,9],[8,-1,-2,2,8,7,-2,6,8,8,-8,4,-4,-6,-2],[3,10,-6,-7,-2,6,3,-6,-3,10,8,4,4,4,2],[-9,-8,1,3,4,-4,-5,-8,8,7,5,-6,7,8,3],[7,-7,1,9,-7,-7,5,10,5,7,5,-5,-10,2,4],[-9,7,6,-5,10,-9,-5,-1,8,-2,-7,-6,8,5,-5],[7,-9,-10,-2,9,-7,3,3,-6,9,3,-4,8,-6,-6],[-3,-2,7,7,-7,3,5,3,-9,8,-6,4,1,-4,7],[5,-2,2,1,9,8,-9,6,-2,2,3,-2,-7,-10,-9],[10,-9,-4,-10,-4,2,-10,4,4,1,7,-1,-2,1,9],[1,7,2,4,-4,-2,8,-7,8,-10,7,-2,6,9,5],[9,-9,-7,6,2,10,8,6,4,-1,10,4,8,-5,7]]], dtype = "uint8")#candidate|4710|(2, 15, 15)|const|uint8
const_4711 = relay.const([[[-8,7,6,-10,-10,7,-2,-10,-9,-10,-5,7,-6,3,4],[1,-2,-5,-6,5,-8,1,-7,8,5,1,4,7,6,-6],[-4,2,5,-2,2,9,10,-9,-5,4,-6,-10,-5,-2,9],[-1,7,6,-3,-5,8,7,5,4,7,-10,7,3,8,-2],[5,9,1,4,-6,10,-2,-1,-7,7,-6,-4,8,4,-5],[5,2,-2,1,-8,4,10,-7,4,-9,5,-7,-6,-8,-3],[7,-3,-3,-3,-10,1,8,-1,-4,8,-6,-9,-4,10,-5],[7,2,-2,-4,7,-5,1,2,8,-6,9,9,-5,-3,7],[9,-2,3,-3,-9,4,-1,-7,4,8,10,-2,-7,4,-1],[10,4,-10,-5,7,-5,8,-3,-10,-10,8,8,-9,-6,-5],[-3,-8,6,-5,1,5,-2,-2,7,3,-2,7,1,-5,10],[-8,4,1,2,-2,-9,-8,1,-5,4,8,-1,6,-3,-2],[10,8,-4,5,-9,8,4,-9,8,5,-6,-9,-8,-10,3],[-3,-2,6,-2,-3,-10,6,-8,8,3,-9,-6,5,-1,-4],[6,9,8,3,8,8,-6,-1,3,2,5,-2,-10,-5,-1]],[[7,-8,-5,-4,6,-4,-10,-3,5,-4,-10,8,2,-1,1],[7,7,-6,2,1,-4,4,-7,6,-3,-9,-9,-6,-7,9],[-7,7,2,8,-5,-1,6,-2,-4,-5,9,7,4,-1,10],[-10,6,3,-5,9,-2,9,-8,2,-9,7,2,-8,-9,9],[10,-6,-9,2,10,3,4,1,-3,5,10,10,8,-10,10],[8,-1,6,-5,-5,4,8,-10,-1,2,2,8,7,3,-6],[-9,3,-9,9,9,-9,-1,-10,-8,3,7,-5,1,-4,1],[7,4,-9,9,7,3,-1,-6,7,-2,-3,10,-7,-10,-3],[-10,-1,10,-7,8,-9,1,7,-8,1,-5,-2,-2,5,-7],[3,1,-2,-1,-2,-3,2,-8,3,-3,8,9,-2,9,3],[6,-5,-9,9,-4,-1,-9,-10,3,-3,-8,-4,-2,-5,4],[7,3,10,-7,-2,-8,-9,-7,4,-2,6,-9,-6,7,-2],[-1,-4,10,-6,10,9,2,-5,-7,-9,-7,1,-5,8,10],[4,10,-6,1,9,-10,1,6,-1,6,-4,-6,10,-3,5],[10,-5,-9,-1,10,4,-10,-2,-3,-1,-2,2,1,-1,-8]]], dtype = "uint8")#candidate|4711|(2, 15, 15)|const|uint8
bop_4712 = relay.greater_equal(const_4710.astype('bool'), relay.reshape(const_4711.astype('bool'), relay.shape_of(const_4710))) # shape=(2, 15, 15)
func_2496_call = mod.get_global_var('func_2496')
func_2499_call = mutated_mod.get_global_var('func_2499')
const_4717 = relay.const([[4,-3,-6,2,2,-10,-2,8,9,-2,4,3,-1,1,1,-6]], dtype = "uint16")#candidate|4717|(1, 16)|const|uint16
call_4716 = relay.TupleGetItem(func_2496_call(relay.reshape(const_4717.astype('uint16'), [4, 2, 2])), 0)
call_4718 = relay.TupleGetItem(func_2499_call(relay.reshape(const_4717.astype('uint16'), [4, 2, 2])), 0)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4725 = relay.TupleGetItem(func_4227_call(), 0)
call_4726 = relay.TupleGetItem(func_4228_call(), 0)
func_4587_call = mod.get_global_var('func_4587')
func_4588_call = mutated_mod.get_global_var('func_4588')
call_4745 = relay.TupleGetItem(func_4587_call(), 0)
call_4746 = relay.TupleGetItem(func_4588_call(), 0)
func_2860_call = mod.get_global_var('func_2860')
func_2863_call = mutated_mod.get_global_var('func_2863')
var_4753 = relay.var("var_4753", dtype = "float32", shape = (2184,))#candidate|4753|(2184,)|var|float32
call_4752 = func_2860_call(relay.reshape(var_4753.astype('float32'), [14, 12, 13]))
call_4754 = func_2860_call(relay.reshape(var_4753.astype('float32'), [14, 12, 13]))
func_4105_call = mod.get_global_var('func_4105')
func_4106_call = mutated_mod.get_global_var('func_4106')
call_4757 = relay.TupleGetItem(func_4105_call(), 0)
call_4758 = relay.TupleGetItem(func_4106_call(), 0)
output = relay.Tuple([bop_4712,call_4716,const_4717,call_4725,call_4745,call_4752,var_4753,call_4757,])
output2 = relay.Tuple([bop_4712,call_4718,const_4717,call_4726,call_4746,call_4754,var_4753,call_4758,])
func_4760 = relay.Function([var_4753,], output)
mod['func_4760'] = func_4760
mod = relay.transform.InferType()(mod)
mutated_mod['func_4760'] = func_4760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4761 = relay.var("var_4761", dtype = "float32", shape = (2184,))#candidate|4761|(2184,)|var|float32
func_4760_call = mutated_mod.get_global_var('func_4760')
call_4762 = func_4760_call(var_4761)
output = call_4762
func_4763 = relay.Function([var_4761], output)
mutated_mod['func_4763'] = func_4763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_4777 = func_2571_call()
call_4778 = func_2571_call()
output = relay.Tuple([call_4777,])
output2 = relay.Tuple([call_4778,])
func_4783 = relay.Function([], output)
mod['func_4783'] = func_4783
mod = relay.transform.InferType()(mod)
output = func_4783()
func_4784 = relay.Function([], output)
mutated_mod['func_4784'] = func_4784
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4799 = relay.var("var_4799", dtype = "float64", shape = (1, 7, 7))#candidate|4799|(1, 7, 7)|var|float64
uop_4800 = relay.log2(var_4799.astype('float64')) # shape=(1, 7, 7)
func_4211_call = mod.get_global_var('func_4211')
func_4212_call = mutated_mod.get_global_var('func_4212')
call_4802 = relay.TupleGetItem(func_4211_call(), 1)
call_4803 = relay.TupleGetItem(func_4212_call(), 1)
bop_4817 = relay.subtract(uop_4800.astype('float64'), relay.reshape(var_4799.astype('float64'), relay.shape_of(uop_4800))) # shape=(1, 7, 7)
bop_4830 = relay.bitwise_and(bop_4817.astype('uint8'), relay.reshape(uop_4800.astype('uint8'), relay.shape_of(bop_4817))) # shape=(1, 7, 7)
bop_4835 = relay.add(bop_4817.astype('uint16'), relay.reshape(uop_4800.astype('uint16'), relay.shape_of(bop_4817))) # shape=(1, 7, 7)
func_1387_call = mod.get_global_var('func_1387')
func_1390_call = mutated_mod.get_global_var('func_1390')
const_4840 = relay.const([-5.400212,1.555279,-9.076710,6.057992,9.378237,5.299522,4.269257,1.787978,-0.203059,7.770154,6.073195,-7.664360,-7.398818,4.869740,-9.905034,-2.041789,0.951298,-8.964682,2.898923,6.303333,5.304738,-5.945829,1.474555,-1.717359,-2.639404,8.527136,-7.497179,-5.748314], dtype = "float64")#candidate|4840|(28,)|const|float64
call_4839 = relay.TupleGetItem(func_1387_call(relay.reshape(const_4840.astype('float64'), [7, 2, 2])), 0)
call_4841 = relay.TupleGetItem(func_1390_call(relay.reshape(const_4840.astype('float64'), [7, 2, 2])), 0)
uop_4842 = relay.tan(bop_4817.astype('float32')) # shape=(1, 7, 7)
output = relay.Tuple([call_4802,bop_4830,bop_4835,call_4839,const_4840,uop_4842,])
output2 = relay.Tuple([call_4803,bop_4830,bop_4835,call_4841,const_4840,uop_4842,])
func_4850 = relay.Function([var_4799,], output)
mod['func_4850'] = func_4850
mod = relay.transform.InferType()(mod)
var_4851 = relay.var("var_4851", dtype = "float64", shape = (1, 7, 7))#candidate|4851|(1, 7, 7)|var|float64
output = func_4850(var_4851)
func_4852 = relay.Function([var_4851], output)
mutated_mod['func_4852'] = func_4852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4477_call = mod.get_global_var('func_4477')
func_4478_call = mutated_mod.get_global_var('func_4478')
call_4857 = relay.TupleGetItem(func_4477_call(), 0)
call_4858 = relay.TupleGetItem(func_4478_call(), 0)
func_2419_call = mod.get_global_var('func_2419')
func_2421_call = mutated_mod.get_global_var('func_2421')
call_4867 = func_2419_call()
call_4868 = func_2419_call()
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
const_4872 = relay.const([-1.883180,-0.863220,-6.690204,-9.328127,-2.660901,2.694595,5.577482,-0.055461,-9.342052,-6.979797,-0.559291,-3.964463,-6.807102,4.459171,-0.534836,5.791203,2.453495,-1.947064,-5.727704,9.646814,0.463313,5.897526,1.239372,-3.672691,7.372631,-4.116647,1.318327,9.378578,-0.928444,4.732856,-5.280587,6.673084,-0.321965,0.072576,-3.495295,6.502570,-1.327522,-8.029571,-9.600101,2.720669,6.172567,6.825126,-5.755606,-4.415808,-7.818957,6.308375,1.008491,-8.587819,-7.077038,-5.962365,-8.648964,0.656964,-3.849459,-6.679913,-4.118710,-6.130446,-2.559810,-0.676816,2.919127,7.342516,-3.949164,-4.987005,8.528617,7.143475,-9.446526,9.703972,1.922999,9.184981,-6.875917,-8.507431,-0.718322,2.835738,8.216189,1.305025,-4.188650,-6.097501,-8.099786,-3.226042,3.059506,2.700134,7.428034,-0.395605,9.415515,3.282827,4.956100,-7.318623,-9.228694,-2.534379,2.304528,-4.400367,-8.668319,-5.900770,5.840799,6.217475,-1.951352,4.454234,3.385043,-6.883140,2.578042,-6.707861,-6.509414,-1.539109,-8.674793,-8.771499,1.843487,-7.443386,2.532945,-9.379275,7.804632,3.041635,-4.642215,-3.876112,-6.169388,5.542456,-2.970329,-8.133656,-3.046127,6.554093,-1.542059,1.804089,9.649671,9.811343,-5.014797,3.732789,2.744754,-9.216294,1.751840,5.059888,2.897790,-4.898633,1.796789,-3.907796,3.792407,-4.801846,9.807638,8.291354,6.069185,8.962917,-9.513500,-3.176726,1.774187,-3.988403,2.969928,-9.990667,-2.656688,-4.516251,-8.731910,7.737090,-1.510271,8.845435,8.513233,-4.936424,8.278610,2.176366,6.900697,-2.095564,-7.502838,8.016449,-6.283180,-9.233521,-3.790596,-3.011221,-1.310225,0.898428,-9.953611,-9.608831,5.622880,-0.882746,2.190529,0.752173,5.430759,8.683164,-4.063521,3.657907,2.325142,4.243585,-3.697458,-1.375416,0.484343,-0.250349,-0.976777,-4.434323,9.870019,-0.611412,-9.017765,9.213553,7.766912,9.792291,-8.786826,0.385587,-7.917011,1.779613,-2.427804,3.845045,6.590722,2.255202,2.225968,-9.487152,1.353885,9.676355,-0.192454,7.013453,1.031374,3.226904,-9.435910,6.089258,7.889389,3.764458,-5.061183,0.557615,-4.708986,3.510568,-1.020520,2.465341,9.200102,3.059493,7.513141,0.019973,8.088854,-6.152917,8.717221,0.044614,4.595278,1.306392,9.580339,2.524295,4.062359,1.366177,-2.942224,1.426990,5.389929,1.776223,-0.980274,-9.923401,8.484988,8.132806,-9.036523,3.698240,8.613901,-3.893484,-3.688162,4.723763,-9.686719,9.454699,8.544666,-4.369321,-6.859256,6.854995,2.153337,-1.968192,4.659300,0.018881,-2.008231,5.235761,6.578342,8.626543,0.961203,-9.117948,7.527384,7.310260,-3.280636,-6.262054,0.600695,0.743440,1.690411,-4.049229,3.309161,-7.265494,-2.276059,-9.244392,8.543842,0.824916,-6.205374,3.358428,-4.041465,-9.309505,-6.746019,7.501315,-2.844953,-8.069964,-2.834376,-2.446054,6.312635,-4.725722,-9.001124,4.454926,-6.198027,8.599572,-2.879420,-9.428254,5.267339,-0.452536,2.521059,8.589561,-4.637380,8.049363,-1.449321,9.222026,5.889044,-3.499930,-8.615028,2.910335,-1.458225,2.048740,7.145711,5.300332,-8.571303,2.558189,6.569134,2.195689,-2.488759,8.524677,1.729041,-5.516326,-2.207205,-4.154021,7.498805,1.630010,-6.468424,-0.064909,-0.250703,-2.152898,3.498786,0.600143,8.878571,1.293978,6.393990,-6.933959,0.224912,5.839361,3.384092,-2.545031,-1.693690,6.187907,-3.006192,-5.207555,7.446831,5.262596,-7.598864,-5.829725,5.075500,-9.501806,-9.700403,1.142295,8.071453,7.415923,5.144028,2.909746,9.741545,-4.660213,3.617375,-4.190294,-4.070998,5.331625,-3.059990,-8.896781,3.637545,4.975043,4.733305,4.934571,4.156011,-7.424402,-9.823638,-4.100563,-4.119319,9.390725,-1.865748,-9.510112,6.170843,3.487756,8.606386,-2.779133,-7.238353,-8.020738,-2.970160,0.979464,-1.551928,-6.119352,7.423391,-9.580979,-7.282242,1.238659,-5.104996,4.617237,-0.989002,8.163476,-3.578014,-3.215120,5.770565,-0.949021,0.162539,-3.988071,4.643673,-1.765278,8.389722,-4.563893,1.702437,-2.159027,-9.533880,9.551379,7.314141,-8.789787,-8.334998,-2.464502,-7.101904,-2.604974,-9.463466,2.357250,6.010198,2.585350,9.035975,-1.639510,0.494203,-7.904720,-4.516210,-0.048986,-0.943377,2.674825,-8.987338,1.381610,3.146432,-6.071240,-9.534791,9.820164,7.793920,-3.458728,4.197693,3.164198,-2.775441,-8.665914,-3.722204,-0.728527,5.224742,3.078350,1.241567,-7.822008,-9.540300,2.514689,6.428932,4.256607,8.387941,2.433556,-1.498211,8.028295,-0.843578,-4.091310,7.187173,7.378132,-1.983914,-1.608184,9.696182,-3.507452,3.113581,-0.697313,0.212919,6.488020,-1.901672,9.148220,-7.934040,6.537286,-0.235138,7.616529,-6.874622,-0.234186,1.772938,-1.596710,-7.851580,3.282750,-1.918492,-4.220517,8.907085,-4.575979,-8.097217,-6.930044,2.301113,2.178055,8.483481,5.648299,9.005817,0.821168,-9.739272,-8.548658,-3.462981,-7.164204,8.068320,-1.194770,-7.738905,-4.657741,-4.384398,4.038836,-4.846992,2.443082,0.777434,0.580205,6.862187,-5.171755,9.241651,-2.527532,-0.547944,-2.758942,5.062460,-9.762219,-3.166409,-8.456503,1.885461,-0.232706,-9.986105,-3.847416,-9.199195,-7.862756,-4.576346,7.100321,4.354949,2.997033,-6.674242,-0.740217,5.126879,5.224250,4.527526,-1.795550,-7.695118,4.405150,7.704961,-5.612851,6.761372,6.320407,3.195377,1.630304,-2.818242,-7.068105,5.706023,-2.677535,2.763282,-3.557180,4.957197,-7.158869,6.836616,-6.328363,0.458534,-6.568260], dtype = "float32")#candidate|4872|(540,)|const|float32
call_4871 = relay.TupleGetItem(func_941_call(relay.reshape(const_4872.astype('float32'), [6, 15, 6])), 1)
call_4873 = relay.TupleGetItem(func_943_call(relay.reshape(const_4872.astype('float32'), [6, 15, 6])), 1)
func_1836_call = mod.get_global_var('func_1836')
func_1839_call = mutated_mod.get_global_var('func_1839')
var_4890 = relay.var("var_4890", dtype = "float32", shape = (768, 1))#candidate|4890|(768, 1)|var|float32
call_4889 = relay.TupleGetItem(func_1836_call(relay.reshape(var_4890.astype('float32'), [8, 12, 8])), 0)
call_4891 = relay.TupleGetItem(func_1839_call(relay.reshape(var_4890.astype('float32'), [8, 12, 8])), 0)
bop_4892 = relay.bitwise_or(const_4872.astype('int8'), var_4890.astype('int8')) # shape=(768, 540)
output = relay.Tuple([call_4857,call_4867,call_4871,call_4889,bop_4892,])
output2 = relay.Tuple([call_4858,call_4868,call_4873,call_4891,bop_4892,])
func_4897 = relay.Function([var_4890,], output)
mod['func_4897'] = func_4897
mod = relay.transform.InferType()(mod)
var_4898 = relay.var("var_4898", dtype = "float32", shape = (768, 1))#candidate|4898|(768, 1)|var|float32
output = func_4897(var_4898)
func_4899 = relay.Function([var_4898], output)
mutated_mod['func_4899'] = func_4899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2571_call = mod.get_global_var('func_2571')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_4919 = func_2571_call()
call_4920 = func_2571_call()
func_4850_call = mod.get_global_var('func_4850')
func_4852_call = mutated_mod.get_global_var('func_4852')
var_4929 = relay.var("var_4929", dtype = "float64", shape = (49,))#candidate|4929|(49,)|var|float64
call_4928 = relay.TupleGetItem(func_4850_call(relay.reshape(var_4929.astype('float64'), [1, 7, 7])), 3)
call_4930 = relay.TupleGetItem(func_4852_call(relay.reshape(var_4929.astype('float64'), [1, 7, 7])), 3)
func_4373_call = mod.get_global_var('func_4373')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_4933 = func_4373_call()
call_4934 = func_4373_call()
bop_4936 = relay.not_equal(call_4933.astype('bool'), call_4928.astype('bool')) # shape=(7, 2, 2)
bop_4939 = relay.not_equal(call_4934.astype('bool'), call_4930.astype('bool')) # shape=(7, 2, 2)
func_4897_call = mod.get_global_var('func_4897')
func_4899_call = mutated_mod.get_global_var('func_4899')
var_4941 = relay.var("var_4941", dtype = "float32", shape = (768, 1))#candidate|4941|(768, 1)|var|float32
call_4940 = relay.TupleGetItem(func_4897_call(relay.reshape(var_4941.astype('float32'), [768, 1])), 0)
call_4942 = relay.TupleGetItem(func_4899_call(relay.reshape(var_4941.astype('float32'), [768, 1])), 0)
output = relay.Tuple([call_4919,var_4929,bop_4936,call_4940,var_4941,])
output2 = relay.Tuple([call_4920,var_4929,bop_4939,call_4942,var_4941,])
func_4943 = relay.Function([var_4929,var_4941,], output)
mod['func_4943'] = func_4943
mod = relay.transform.InferType()(mod)
mutated_mod['func_4943'] = func_4943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4943_call = mutated_mod.get_global_var('func_4943')
var_4945 = relay.var("var_4945", dtype = "float64", shape = (49,))#candidate|4945|(49,)|var|float64
var_4946 = relay.var("var_4946", dtype = "float32", shape = (768, 1))#candidate|4946|(768, 1)|var|float32
call_4944 = func_4943_call(var_4945,var_4946,)
output = call_4944
func_4947 = relay.Function([var_4945,var_4946,], output)
mutated_mod['func_4947'] = func_4947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4105_call = mod.get_global_var('func_4105')
func_4106_call = mutated_mod.get_global_var('func_4106')
call_4986 = relay.TupleGetItem(func_4105_call(), 0)
call_4987 = relay.TupleGetItem(func_4106_call(), 0)
output = relay.Tuple([call_4986,])
output2 = relay.Tuple([call_4987,])
func_4996 = relay.Function([], output)
mod['func_4996'] = func_4996
mod = relay.transform.InferType()(mod)
mutated_mod['func_4996'] = func_4996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4996_call = mutated_mod.get_global_var('func_4996')
call_4997 = func_4996_call()
output = call_4997
func_4998 = relay.Function([], output)
mutated_mod['func_4998'] = func_4998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1887_call = mod.get_global_var('func_1887')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_5032 = relay.TupleGetItem(func_1887_call(), 0)
call_5033 = relay.TupleGetItem(func_1889_call(), 0)
output = relay.Tuple([call_5032,])
output2 = relay.Tuple([call_5033,])
func_5043 = relay.Function([], output)
mod['func_5043'] = func_5043
mod = relay.transform.InferType()(mod)
mutated_mod['func_5043'] = func_5043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5043_call = mutated_mod.get_global_var('func_5043')
call_5044 = func_5043_call()
output = call_5044
func_5045 = relay.Function([], output)
mutated_mod['func_5045'] = func_5045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_629_call = mod.get_global_var('func_629')
func_631_call = mutated_mod.get_global_var('func_631')
call_5052 = relay.TupleGetItem(func_629_call(), 0)
call_5053 = relay.TupleGetItem(func_631_call(), 0)
output = relay.Tuple([call_5052,])
output2 = relay.Tuple([call_5053,])
func_5064 = relay.Function([], output)
mod['func_5064'] = func_5064
mod = relay.transform.InferType()(mod)
output = func_5064()
func_5065 = relay.Function([], output)
mutated_mod['func_5065'] = func_5065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1929_call = mod.get_global_var('func_1929')
func_1931_call = mutated_mod.get_global_var('func_1931')
call_5096 = relay.TupleGetItem(func_1929_call(), 0)
call_5097 = relay.TupleGetItem(func_1931_call(), 0)
output = call_5096
output2 = call_5097
func_5101 = relay.Function([], output)
mod['func_5101'] = func_5101
mod = relay.transform.InferType()(mod)
mutated_mod['func_5101'] = func_5101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5101_call = mutated_mod.get_global_var('func_5101')
call_5102 = func_5101_call()
output = call_5102
func_5103 = relay.Function([], output)
mutated_mod['func_5103'] = func_5103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5143 = relay.var("var_5143", dtype = "float32", shape = (6, 14, 4))#candidate|5143|(6, 14, 4)|var|float32
uop_5144 = relay.sigmoid(var_5143.astype('float32')) # shape=(6, 14, 4)
output = relay.Tuple([uop_5144,])
output2 = relay.Tuple([uop_5144,])
func_5148 = relay.Function([var_5143,], output)
mod['func_5148'] = func_5148
mod = relay.transform.InferType()(mod)
mutated_mod['func_5148'] = func_5148
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5149 = relay.var("var_5149", dtype = "float32", shape = (6, 14, 4))#candidate|5149|(6, 14, 4)|var|float32
func_5148_call = mutated_mod.get_global_var('func_5148')
call_5150 = func_5148_call(var_5149)
output = call_5150
func_5151 = relay.Function([var_5149], output)
mutated_mod['func_5151'] = func_5151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_314_call = mod.get_global_var('func_314')
func_315_call = mutated_mod.get_global_var('func_315')
call_5161 = relay.TupleGetItem(func_314_call(), 0)
call_5162 = relay.TupleGetItem(func_315_call(), 0)
output = relay.Tuple([call_5161,])
output2 = relay.Tuple([call_5162,])
func_5164 = relay.Function([], output)
mod['func_5164'] = func_5164
mod = relay.transform.InferType()(mod)
output = func_5164()
func_5165 = relay.Function([], output)
mutated_mod['func_5165'] = func_5165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5043_call = mod.get_global_var('func_5043')
func_5045_call = mutated_mod.get_global_var('func_5045')
call_5315 = relay.TupleGetItem(func_5043_call(), 0)
call_5316 = relay.TupleGetItem(func_5045_call(), 0)
func_1450_call = mod.get_global_var('func_1450')
func_1455_call = mutated_mod.get_global_var('func_1455')
var_5319 = relay.var("var_5319", dtype = "uint32", shape = (168,))#candidate|5319|(168,)|var|uint32
var_5320 = relay.var("var_5320", dtype = "float64", shape = (28,))#candidate|5320|(28,)|var|float64
call_5318 = relay.TupleGetItem(func_1450_call(relay.reshape(var_5319.astype('uint32'), [12, 7, 2]), relay.reshape(var_5319.astype('uint32'), [12, 7, 2]), relay.reshape(var_5320.astype('float64'), [28,]), ), 0)
call_5321 = relay.TupleGetItem(func_1455_call(relay.reshape(var_5319.astype('uint32'), [12, 7, 2]), relay.reshape(var_5319.astype('uint32'), [12, 7, 2]), relay.reshape(var_5320.astype('float64'), [28,]), ), 0)
func_681_call = mod.get_global_var('func_681')
func_684_call = mutated_mod.get_global_var('func_684')
var_5352 = relay.var("var_5352", dtype = "float32", shape = (22, 2))#candidate|5352|(22, 2)|var|float32
call_5351 = func_681_call(relay.reshape(var_5352.astype('float32'), [11, 2, 2]))
call_5353 = func_681_call(relay.reshape(var_5352.astype('float32'), [11, 2, 2]))
output = relay.Tuple([call_5315,call_5318,var_5319,var_5320,call_5351,var_5352,])
output2 = relay.Tuple([call_5316,call_5321,var_5319,var_5320,call_5353,var_5352,])
func_5354 = relay.Function([var_5319,var_5320,var_5352,], output)
mod['func_5354'] = func_5354
mod = relay.transform.InferType()(mod)
mutated_mod['func_5354'] = func_5354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5354_call = mutated_mod.get_global_var('func_5354')
var_5356 = relay.var("var_5356", dtype = "uint32", shape = (168,))#candidate|5356|(168,)|var|uint32
var_5357 = relay.var("var_5357", dtype = "float64", shape = (28,))#candidate|5357|(28,)|var|float64
var_5358 = relay.var("var_5358", dtype = "float32", shape = (22, 2))#candidate|5358|(22, 2)|var|float32
call_5355 = func_5354_call(var_5356,var_5357,var_5358,)
output = call_5355
func_5359 = relay.Function([var_5356,var_5357,var_5358,], output)
mutated_mod['func_5359'] = func_5359
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5390 = relay.var("var_5390", dtype = "int8", shape = (9, 12, 2))#candidate|5390|(9, 12, 2)|var|int8
var_5391 = relay.var("var_5391", dtype = "int8", shape = (9, 12, 2))#candidate|5391|(9, 12, 2)|var|int8
bop_5392 = relay.bitwise_or(var_5390.astype('int8'), relay.reshape(var_5391.astype('int8'), relay.shape_of(var_5390))) # shape=(9, 12, 2)
output = relay.Tuple([bop_5392,])
output2 = relay.Tuple([bop_5392,])
func_5395 = relay.Function([var_5390,var_5391,], output)
mod['func_5395'] = func_5395
mod = relay.transform.InferType()(mod)
mutated_mod['func_5395'] = func_5395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5395_call = mutated_mod.get_global_var('func_5395')
var_5397 = relay.var("var_5397", dtype = "int8", shape = (9, 12, 2))#candidate|5397|(9, 12, 2)|var|int8
var_5398 = relay.var("var_5398", dtype = "int8", shape = (9, 12, 2))#candidate|5398|(9, 12, 2)|var|int8
call_5396 = func_5395_call(var_5397,var_5398,)
output = call_5396
func_5399 = relay.Function([var_5397,var_5398,], output)
mutated_mod['func_5399'] = func_5399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5418 = relay.var("var_5418", dtype = "uint16", shape = (12, 4, 3))#candidate|5418|(12, 4, 3)|var|uint16
var_5419 = relay.var("var_5419", dtype = "uint16", shape = (12, 4, 3))#candidate|5419|(12, 4, 3)|var|uint16
bop_5420 = relay.bitwise_xor(var_5418.astype('uint16'), relay.reshape(var_5419.astype('uint16'), relay.shape_of(var_5418))) # shape=(12, 4, 3)
output = relay.Tuple([bop_5420,])
output2 = relay.Tuple([bop_5420,])
func_5430 = relay.Function([var_5418,var_5419,], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
var_5431 = relay.var("var_5431", dtype = "uint16", shape = (12, 4, 3))#candidate|5431|(12, 4, 3)|var|uint16
var_5432 = relay.var("var_5432", dtype = "uint16", shape = (12, 4, 3))#candidate|5432|(12, 4, 3)|var|uint16
output = func_5430(var_5431,var_5432,)
func_5433 = relay.Function([var_5431,var_5432,], output)
mutated_mod['func_5433'] = func_5433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2419_call = mod.get_global_var('func_2419')
func_2421_call = mutated_mod.get_global_var('func_2421')
call_5521 = func_2419_call()
call_5522 = func_2419_call()
uop_5526 = relay.log10(call_5521.astype('float32')) # shape=(4, 2, 2)
uop_5528 = relay.log10(call_5522.astype('float32')) # shape=(4, 2, 2)
output = relay.Tuple([uop_5526,])
output2 = relay.Tuple([uop_5528,])
func_5530 = relay.Function([], output)
mod['func_5530'] = func_5530
mod = relay.transform.InferType()(mod)
mutated_mod['func_5530'] = func_5530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5530_call = mutated_mod.get_global_var('func_5530')
call_5531 = func_5530_call()
output = call_5531
func_5532 = relay.Function([], output)
mutated_mod['func_5532'] = func_5532
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5550 = relay.var("var_5550", dtype = "float32", shape = (15, 12, 13))#candidate|5550|(15, 12, 13)|var|float32
uop_5551 = relay.asin(var_5550.astype('float32')) # shape=(15, 12, 13)
uop_5553 = relay.log2(uop_5551.astype('float32')) # shape=(15, 12, 13)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
const_5558 = relay.const([[8.872748],[3.036595],[-7.776789],[-4.671064],[-2.240835],[-5.714826],[-6.543114],[9.092628],[-9.865521],[-2.263319],[-9.046991],[-7.662057],[0.222216],[-8.874979],[-0.180805],[-2.671762],[-7.710518],[6.565554],[5.959638],[7.528238],[3.583945],[-0.938375],[-7.272753],[-7.826973],[0.937357],[-8.630124],[-4.497772],[2.244671],[-9.731841],[8.745664],[8.076380],[-6.905588],[-4.702532],[-7.770814],[-8.574632],[5.432553],[-1.931798],[2.954934],[0.789853],[3.588324],[-3.735474],[-6.388818],[-7.938213],[-7.325354],[9.500476],[7.458366],[-3.308687],[8.023882],[-8.601713],[-0.429689],[1.151948],[-0.928915],[-7.153486],[-0.106709],[5.354661],[-8.792221],[5.083164],[4.476901],[-7.796302],[-9.122392],[1.631187],[8.747732],[-0.364506],[-6.712236],[-1.130992],[9.872927],[7.348210],[2.918415],[3.902733],[7.446749],[-6.081892],[-8.679678],[6.570493],[1.796413],[-4.089321],[3.796341],[-6.718004],[7.087263],[4.132697],[7.080306],[-8.811860],[4.298412],[-7.149703],[5.286696],[-6.047348],[-2.155579],[0.491763],[-3.974912],[-2.112576],[-2.609392],[-7.439835],[2.900782],[-4.431487],[9.801033],[-4.047641],[-7.153377],[4.677360],[-2.934243],[-7.822430],[5.805164],[0.233856],[5.672791],[-5.015094],[9.684080],[-9.120613],[0.156825],[5.734755],[9.097982],[4.644625],[-5.231522],[8.496034],[7.517723],[-8.719521],[-1.613516],[1.112303],[-9.516642],[7.313953],[9.930727],[7.154214],[1.368044],[7.327991],[-4.926216],[5.379306],[-2.485184],[-7.616420],[-0.356060],[5.004482],[-4.191236],[-7.619250],[2.359029],[-9.415585],[-5.558368],[4.721888],[-7.240491],[-3.061090],[-3.150111],[-1.265978],[-6.025671],[-5.246548],[1.616140],[5.110185],[-8.322742],[3.639496],[8.310908],[4.000355],[4.388871],[-8.507744],[-9.407828],[-2.245184],[-2.870925],[-3.294917],[-2.876068],[-7.683489],[-6.552982],[2.576650],[3.176060],[5.759813],[-8.382456],[5.059238],[-1.421060],[-6.701334],[-4.094996],[2.096697],[-1.977621],[4.309263],[-6.191047],[-7.953183],[2.455113],[-2.477612],[6.213914],[4.757898],[-9.996509],[1.821452],[0.689152],[-0.709614],[6.362520],[2.258710],[2.666826],[-6.100225],[-4.991709],[1.941730],[4.928863],[2.791126],[-6.453051],[-7.850141],[-3.852896],[-3.619147],[9.974007],[6.286305],[-0.486370],[-8.316246],[-3.332723],[-5.690151],[4.246455],[3.528639],[-0.488391],[-0.877725],[-0.729240],[-0.930138],[0.800523],[4.205503],[-0.258565],[4.741226],[9.882731],[-5.995132],[-7.043745],[7.981180],[6.383151],[5.545810],[7.585341],[-1.393804],[9.127441],[0.174506],[8.445378],[-3.221870],[2.522080],[-0.999831],[7.866317],[8.009859],[-3.059993],[0.583292],[-2.576394],[9.435472],[-0.262517],[-8.819508],[1.530608],[6.399007],[-4.677800],[3.760285],[6.826085],[-3.439249],[3.079919],[-4.581947],[-8.251224],[0.167084],[-7.677209],[-8.773214],[7.329500],[-7.259832],[-1.614282],[9.701158],[2.351538],[-7.294438],[-0.962794],[6.043016],[3.386149],[-9.040994],[-5.438678],[6.793183],[-4.337612],[8.450969],[9.224679],[9.847535],[9.869507],[-4.223964],[0.338876],[-4.679927],[4.317170],[-6.880366],[-0.683378],[8.626626],[1.889818],[-5.971161],[-8.657012],[0.758239],[-2.441554],[7.207312],[-8.625256],[-8.920419],[-7.978649],[7.499035],[9.704572],[4.837001],[-9.569405],[-4.230048],[2.460255],[-9.416186],[9.948994],[9.232304],[-8.508382],[-9.291755],[3.096709],[7.628355],[-2.204950],[-1.373476],[-6.569238],[-5.001546],[2.985245],[-8.894422],[7.716522],[-2.064876],[-1.897060],[-6.968629],[6.805682],[-4.214433],[-8.385614],[-8.280308],[-2.571251],[8.142726],[4.334579],[-0.322086],[1.010250],[1.572392],[-1.169501],[-8.856976],[-3.058663],[-3.837568],[5.297579],[-2.321027],[-8.273124],[-9.502322],[0.143570],[1.756591],[-9.723438],[2.486306],[-6.186968],[-6.767340],[-6.424184],[-2.444285],[6.268788],[7.195131],[4.034378],[9.767430],[-6.883561],[2.215832],[-1.740576],[2.301820],[-8.070674],[2.793261],[5.904726],[-7.039638],[-6.580067],[9.845148],[4.383515],[0.871355],[-6.407446],[-1.968483],[7.169908],[-6.555085],[-8.902110],[-8.473108],[4.692360],[-5.391598],[-2.767087],[3.826022],[-6.744140],[6.759709],[-9.897226],[-6.423913],[-5.017267],[-6.686380],[-1.115562],[-2.452889],[-3.556126],[2.030408],[-5.317422],[0.801323],[5.729265],[9.215973],[-9.545713],[4.265506],[2.749398],[2.606955],[9.811221],[4.866510],[-2.115088],[-2.774199],[-3.433634],[-8.979325],[0.494783],[6.265780],[6.384438],[7.954655],[9.926496],[7.529760],[0.049138],[-7.567443],[2.528027],[-8.892461],[0.516911],[1.678421],[-1.376939],[-2.559429],[-1.405307],[9.809123],[-5.849057],[-4.838219],[-1.714962],[-6.088163],[-5.601835],[0.008904],[-0.261769],[-6.232306],[1.389861],[-3.404032],[-6.440304],[-2.836374],[2.582118],[-1.184905],[4.705577],[4.040702],[-0.461664],[-3.809722],[-5.007039],[-9.011964],[-6.438582],[-6.121763],[-4.994957],[-0.335251],[-8.399939],[-2.974883],[-4.377986],[6.679169],[-9.159047],[-5.479157],[2.831387],[9.139382],[4.345168],[-1.853911],[8.309649],[-4.362034],[-9.779334],[-6.432608],[-3.727553],[5.517759],[-3.673052],[8.142402],[-4.698058],[-7.422124],[-9.299434],[5.355005],[4.485123],[-6.222932],[-0.531671],[-1.598058],[9.194688],[2.680935],[9.144356],[-5.731701],[-9.979178],[-3.477182],[-7.622266],[-9.697309],[-4.576928],[2.697889],[7.197253],[5.835893],[7.073126],[1.064928],[-1.157481],[6.153662],[-4.357931],[-4.955026],[3.907837],[0.747861],[-0.795095],[-4.361840],[-0.367783],[5.262134],[5.374755],[2.746629],[0.950662],[1.455247],[-1.006857],[-5.605622],[-9.894967],[0.009427],[-7.630519],[3.376595],[-4.826118],[-2.606264],[-4.452322],[8.063546],[9.836263],[-0.371935],[2.822660],[3.180563],[-2.823219],[-9.299067],[1.348414],[1.464395],[-7.049263],[-9.524262],[-4.140205],[-4.880725],[8.634355],[9.037594],[2.229366],[-3.370374],[-4.599895],[-2.657541],[-9.178953],[-2.424162],[-4.114131],[-5.737283],[-7.035001],[-0.553864],[-3.314899],[7.356015],[-9.081747],[5.917917],[-1.821526],[5.396043],[-2.293358],[-9.931208],[-6.576596],[-5.251584],[-5.188320],[9.766834],[1.794726],[-2.022565],[-3.801949],[0.996075],[-6.027563],[9.786403],[-6.907766],[-7.637539],[-7.478932],[8.338048],[1.041016],[4.139886],[-4.702917],[-3.979459],[-0.772239],[1.665058],[2.005039],[0.118931],[-2.264341],[-4.331817],[-4.032606],[0.225872],[9.975897],[9.929695],[-1.312461],[-2.792542],[4.441188],[4.109573],[9.128079],[-2.335000],[-3.505507]], dtype = "float32")#candidate|5558|(540, 1)|const|float32
call_5557 = relay.TupleGetItem(func_941_call(relay.reshape(const_5558.astype('float32'), [6, 15, 6])), 1)
call_5559 = relay.TupleGetItem(func_943_call(relay.reshape(const_5558.astype('float32'), [6, 15, 6])), 1)
output = relay.Tuple([uop_5553,call_5557,const_5558,])
output2 = relay.Tuple([uop_5553,call_5559,const_5558,])
func_5568 = relay.Function([var_5550,], output)
mod['func_5568'] = func_5568
mod = relay.transform.InferType()(mod)
var_5569 = relay.var("var_5569", dtype = "float32", shape = (15, 12, 13))#candidate|5569|(15, 12, 13)|var|float32
output = func_5568(var_5569)
func_5570 = relay.Function([var_5569], output)
mutated_mod['func_5570'] = func_5570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5578 = relay.var("var_5578", dtype = "uint64", shape = ())#candidate|5578|()|var|uint64
var_5579 = relay.var("var_5579", dtype = "uint64", shape = (13, 1, 14))#candidate|5579|(13, 1, 14)|var|uint64
bop_5580 = relay.bitwise_or(var_5578.astype('uint64'), var_5579.astype('uint64')) # shape=(13, 1, 14)
func_4477_call = mod.get_global_var('func_4477')
func_4478_call = mutated_mod.get_global_var('func_4478')
call_5584 = relay.TupleGetItem(func_4477_call(), 1)
call_5585 = relay.TupleGetItem(func_4478_call(), 1)
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_5586 = func_210_call()
call_5587 = func_210_call()
output = relay.Tuple([bop_5580,call_5584,call_5586,])
output2 = relay.Tuple([bop_5580,call_5585,call_5587,])
func_5597 = relay.Function([var_5578,var_5579,], output)
mod['func_5597'] = func_5597
mod = relay.transform.InferType()(mod)
var_5598 = relay.var("var_5598", dtype = "uint64", shape = ())#candidate|5598|()|var|uint64
var_5599 = relay.var("var_5599", dtype = "uint64", shape = (13, 1, 14))#candidate|5599|(13, 1, 14)|var|uint64
output = func_5597(var_5598,var_5599,)
func_5600 = relay.Function([var_5598,var_5599,], output)
mutated_mod['func_5600'] = func_5600
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5609 = relay.var("var_5609", dtype = "uint64", shape = (7, 2, 16))#candidate|5609|(7, 2, 16)|var|uint64
var_5610 = relay.var("var_5610", dtype = "uint64", shape = (7, 2, 16))#candidate|5610|(7, 2, 16)|var|uint64
bop_5611 = relay.equal(var_5609.astype('bool'), relay.reshape(var_5610.astype('bool'), relay.shape_of(var_5609))) # shape=(7, 2, 16)
output = relay.Tuple([bop_5611,])
output2 = relay.Tuple([bop_5611,])
func_5615 = relay.Function([var_5609,var_5610,], output)
mod['func_5615'] = func_5615
mod = relay.transform.InferType()(mod)
mutated_mod['func_5615'] = func_5615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mutated_mod.get_global_var('func_5615')
var_5617 = relay.var("var_5617", dtype = "uint64", shape = (7, 2, 16))#candidate|5617|(7, 2, 16)|var|uint64
var_5618 = relay.var("var_5618", dtype = "uint64", shape = (7, 2, 16))#candidate|5618|(7, 2, 16)|var|uint64
call_5616 = func_5615_call(var_5617,var_5618,)
output = call_5616
func_5619 = relay.Function([var_5617,var_5618,], output)
mutated_mod['func_5619'] = func_5619
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5631 = relay.const([[[7,3,5,8,-3,-7,-1,-4]],[[-9,-1,1,7,-7,10,6,-4]],[[-9,5,-8,8,-9,10,8,-6]]], dtype = "int16")#candidate|5631|(3, 1, 8)|const|int16
var_5632 = relay.var("var_5632", dtype = "int16", shape = (3, 5, 8))#candidate|5632|(3, 5, 8)|var|int16
bop_5633 = relay.less_equal(const_5631.astype('bool'), var_5632.astype('bool')) # shape=(3, 5, 8)
func_4258_call = mod.get_global_var('func_4258')
func_4260_call = mutated_mod.get_global_var('func_4260')
var_5644 = relay.var("var_5644", dtype = "int16", shape = (490,))#candidate|5644|(490,)|var|int16
call_5643 = relay.TupleGetItem(func_4258_call(relay.reshape(var_5644.astype('int16'), [245, 2])), 3)
call_5645 = relay.TupleGetItem(func_4260_call(relay.reshape(var_5644.astype('int16'), [245, 2])), 3)
func_5164_call = mod.get_global_var('func_5164')
func_5165_call = mutated_mod.get_global_var('func_5165')
call_5647 = relay.TupleGetItem(func_5164_call(), 0)
call_5648 = relay.TupleGetItem(func_5165_call(), 0)
bop_5649 = relay.maximum(var_5644.astype('int16'), relay.reshape(call_5643.astype('int16'), relay.shape_of(var_5644))) # shape=(490,)
bop_5652 = relay.maximum(var_5644.astype('int16'), relay.reshape(call_5645.astype('int16'), relay.shape_of(var_5644))) # shape=(490,)
output = relay.Tuple([bop_5633,call_5647,bop_5649,])
output2 = relay.Tuple([bop_5633,call_5648,bop_5652,])
func_5662 = relay.Function([var_5632,var_5644,], output)
mod['func_5662'] = func_5662
mod = relay.transform.InferType()(mod)
var_5663 = relay.var("var_5663", dtype = "int16", shape = (3, 5, 8))#candidate|5663|(3, 5, 8)|var|int16
var_5664 = relay.var("var_5664", dtype = "int16", shape = (490,))#candidate|5664|(490,)|var|int16
output = func_5662(var_5663,var_5664,)
func_5665 = relay.Function([var_5663,var_5664,], output)
mutated_mod['func_5665'] = func_5665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5530_call = mod.get_global_var('func_5530')
func_5532_call = mutated_mod.get_global_var('func_5532')
call_5675 = relay.TupleGetItem(func_5530_call(), 0)
call_5676 = relay.TupleGetItem(func_5532_call(), 0)
func_401_call = mod.get_global_var('func_401')
func_402_call = mutated_mod.get_global_var('func_402')
call_5677 = relay.TupleGetItem(func_401_call(), 2)
call_5678 = relay.TupleGetItem(func_402_call(), 2)
output = relay.Tuple([call_5675,call_5677,])
output2 = relay.Tuple([call_5676,call_5678,])
func_5681 = relay.Function([], output)
mod['func_5681'] = func_5681
mod = relay.transform.InferType()(mod)
mutated_mod['func_5681'] = func_5681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5681_call = mutated_mod.get_global_var('func_5681')
call_5682 = func_5681_call()
output = call_5682
func_5683 = relay.Function([], output)
mutated_mod['func_5683'] = func_5683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4373_call = mod.get_global_var('func_4373')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_5716 = func_4373_call()
call_5717 = func_4373_call()
output = call_5716
output2 = call_5717
func_5723 = relay.Function([], output)
mod['func_5723'] = func_5723
mod = relay.transform.InferType()(mod)
mutated_mod['func_5723'] = func_5723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5723_call = mutated_mod.get_global_var('func_5723')
call_5724 = func_5723_call()
output = call_5724
func_5725 = relay.Function([], output)
mutated_mod['func_5725'] = func_5725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mod.get_global_var('func_4783')
func_4784_call = mutated_mod.get_global_var('func_4784')
call_5745 = relay.TupleGetItem(func_4783_call(), 0)
call_5746 = relay.TupleGetItem(func_4784_call(), 0)
output = call_5745
output2 = call_5746
func_5764 = relay.Function([], output)
mod['func_5764'] = func_5764
mod = relay.transform.InferType()(mod)
mutated_mod['func_5764'] = func_5764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5764_call = mutated_mod.get_global_var('func_5764')
call_5765 = func_5764_call()
output = call_5765
func_5766 = relay.Function([], output)
mutated_mod['func_5766'] = func_5766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5723_call = mod.get_global_var('func_5723')
func_5725_call = mutated_mod.get_global_var('func_5725')
call_5770 = func_5723_call()
call_5771 = func_5723_call()
uop_5780 = relay.asin(call_5770.astype('float32')) # shape=(1, 2, 2)
uop_5782 = relay.asin(call_5771.astype('float32')) # shape=(1, 2, 2)
bop_5791 = relay.maximum(call_5770.astype('uint64'), relay.reshape(uop_5780.astype('uint64'), relay.shape_of(call_5770))) # shape=(1, 2, 2)
bop_5794 = relay.maximum(call_5771.astype('uint64'), relay.reshape(uop_5782.astype('uint64'), relay.shape_of(call_5771))) # shape=(1, 2, 2)
func_4120_call = mod.get_global_var('func_4120')
func_4122_call = mutated_mod.get_global_var('func_4122')
call_5797 = relay.TupleGetItem(func_4120_call(), 0)
call_5798 = relay.TupleGetItem(func_4122_call(), 0)
func_3627_call = mod.get_global_var('func_3627')
func_3628_call = mutated_mod.get_global_var('func_3628')
call_5808 = relay.TupleGetItem(func_3627_call(), 0)
call_5809 = relay.TupleGetItem(func_3628_call(), 0)
func_5101_call = mod.get_global_var('func_5101')
func_5103_call = mutated_mod.get_global_var('func_5103')
call_5811 = func_5101_call()
call_5812 = func_5101_call()
func_5164_call = mod.get_global_var('func_5164')
func_5165_call = mutated_mod.get_global_var('func_5165')
call_5821 = relay.TupleGetItem(func_5164_call(), 0)
call_5822 = relay.TupleGetItem(func_5165_call(), 0)
func_5615_call = mod.get_global_var('func_5615')
func_5619_call = mutated_mod.get_global_var('func_5619')
const_5826 = relay.const([-5,-10,-8,4,-8,-3,-4,5,-2,10,-8,-4,-6,-5,1,4,4,4,3,-6,-2,8,-1,1,6,3,-4,8,-3,8,-6,-9,-6,-4,3,-2,2,1,4,7,5,-3,8,-9,-4,-7,9,3,-1,4,1,-8,-7,6,-3,3,-2,9,10,3,4,4,-5,9,-8,-1,1,1,10,-3,-10,-3,5,-4,-1,-8,-4,8,-1,-7,-2,-9,-8,4,10,1,4,-4,-7,3,-3,2,-3,-1,9,-5,-4,7,7,-2,-9,-6,-8,-3,9,10,6,1,2,6,-10,4,7,8,3,10,-4,4,-7,4,2,7,-7,9,-10,3,-10,-4,10,-3,-3,-6,9,8,8,9,-9,10,-5,-7,8,7,-9,-6,-6,-6,2,-7,-4,7,8,-4,2,-2,4,6,-9,9,3,-1,-4,7,8,7,8,6,9,2,3,-10,3,-9,8,-10,-3,1,7,3,3,-9,-1,-6,4,-2,4,-4,-8,7,10,9,10,3,8,-7,6,-4,3,-7,-10,4,1,-8,2,6,-5,-7,5,-4,-6,5,-7,8,1,-6,4,-4,9,-7,9,3,10,-1,-2,9], dtype = "uint64")#candidate|5826|(224,)|const|uint64
call_5825 = relay.TupleGetItem(func_5615_call(relay.reshape(const_5826.astype('uint64'), [7, 2, 16]), relay.reshape(const_5826.astype('uint64'), [7, 2, 16]), ), 0)
call_5827 = relay.TupleGetItem(func_5619_call(relay.reshape(const_5826.astype('uint64'), [7, 2, 16]), relay.reshape(const_5826.astype('uint64'), [7, 2, 16]), ), 0)
bop_5841 = relay.logical_xor(bop_5791.astype('uint64'), relay.reshape(uop_5780.astype('uint64'), relay.shape_of(bop_5791))) # shape=(1, 2, 2)
bop_5844 = relay.logical_xor(bop_5794.astype('uint64'), relay.reshape(uop_5782.astype('uint64'), relay.shape_of(bop_5794))) # shape=(1, 2, 2)
bop_5850 = relay.equal(call_5770.astype('bool'), relay.reshape(bop_5841.astype('bool'), relay.shape_of(call_5770))) # shape=(1, 2, 2)
bop_5853 = relay.equal(call_5771.astype('bool'), relay.reshape(bop_5844.astype('bool'), relay.shape_of(call_5771))) # shape=(1, 2, 2)
output = relay.Tuple([call_5797,call_5808,call_5811,call_5821,call_5825,const_5826,bop_5850,])
output2 = relay.Tuple([call_5798,call_5809,call_5812,call_5822,call_5827,const_5826,bop_5853,])
func_5854 = relay.Function([], output)
mod['func_5854'] = func_5854
mod = relay.transform.InferType()(mod)
mutated_mod['func_5854'] = func_5854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5854_call = mutated_mod.get_global_var('func_5854')
call_5855 = func_5854_call()
output = call_5855
func_5856 = relay.Function([], output)
mutated_mod['func_5856'] = func_5856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5862 = relay.var("var_5862", dtype = "float32", shape = (5, 11, 1))#candidate|5862|(5, 11, 1)|var|float32
uop_5863 = relay.sigmoid(var_5862.astype('float32')) # shape=(5, 11, 1)
output = relay.Tuple([uop_5863,])
output2 = relay.Tuple([uop_5863,])
func_5869 = relay.Function([var_5862,], output)
mod['func_5869'] = func_5869
mod = relay.transform.InferType()(mod)
mutated_mod['func_5869'] = func_5869
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5870 = relay.var("var_5870", dtype = "float32", shape = (5, 11, 1))#candidate|5870|(5, 11, 1)|var|float32
func_5869_call = mutated_mod.get_global_var('func_5869')
call_5871 = func_5869_call(var_5870)
output = call_5871
func_5872 = relay.Function([var_5870], output)
mutated_mod['func_5872'] = func_5872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4120_call = mod.get_global_var('func_4120')
func_4122_call = mutated_mod.get_global_var('func_4122')
call_5948 = relay.TupleGetItem(func_4120_call(), 0)
call_5949 = relay.TupleGetItem(func_4122_call(), 0)
uop_5981 = relay.exp(call_5948.astype('float32')) # shape=(1, 2, 2)
uop_5983 = relay.exp(call_5949.astype('float32')) # shape=(1, 2, 2)
var_6014 = relay.var("var_6014", dtype = "float32", shape = (14, 2, 2))#candidate|6014|(14, 2, 2)|var|float32
bop_6015 = relay.subtract(uop_5981.astype('uint16'), var_6014.astype('uint16')) # shape=(14, 2, 2)
bop_6018 = relay.subtract(uop_5983.astype('uint16'), var_6014.astype('uint16')) # shape=(14, 2, 2)
func_2419_call = mod.get_global_var('func_2419')
func_2421_call = mutated_mod.get_global_var('func_2421')
call_6020 = func_2419_call()
call_6021 = func_2419_call()
bop_6029 = relay.multiply(call_5948.astype('float32'), relay.reshape(uop_5981.astype('float32'), relay.shape_of(call_5948))) # shape=(1, 2, 2)
bop_6032 = relay.multiply(call_5949.astype('float32'), relay.reshape(uop_5983.astype('float32'), relay.shape_of(call_5949))) # shape=(1, 2, 2)
func_5395_call = mod.get_global_var('func_5395')
func_5399_call = mutated_mod.get_global_var('func_5399')
var_6037 = relay.var("var_6037", dtype = "int8", shape = (216,))#candidate|6037|(216,)|var|int8
call_6036 = relay.TupleGetItem(func_5395_call(relay.reshape(var_6037.astype('int8'), [9, 12, 2]), relay.reshape(var_6037.astype('int8'), [9, 12, 2]), ), 0)
call_6038 = relay.TupleGetItem(func_5399_call(relay.reshape(var_6037.astype('int8'), [9, 12, 2]), relay.reshape(var_6037.astype('int8'), [9, 12, 2]), ), 0)
bop_6043 = relay.floor_divide(uop_5981.astype('float64'), var_6014.astype('float64')) # shape=(14, 2, 2)
bop_6046 = relay.floor_divide(uop_5983.astype('float64'), var_6014.astype('float64')) # shape=(14, 2, 2)
output = relay.Tuple([bop_6015,call_6020,bop_6029,call_6036,var_6037,bop_6043,])
output2 = relay.Tuple([bop_6018,call_6021,bop_6032,call_6038,var_6037,bop_6046,])
func_6048 = relay.Function([var_6014,var_6037,], output)
mod['func_6048'] = func_6048
mod = relay.transform.InferType()(mod)
var_6049 = relay.var("var_6049", dtype = "float32", shape = (14, 2, 2))#candidate|6049|(14, 2, 2)|var|float32
var_6050 = relay.var("var_6050", dtype = "int8", shape = (216,))#candidate|6050|(216,)|var|int8
output = func_6048(var_6049,var_6050,)
func_6051 = relay.Function([var_6049,var_6050,], output)
mutated_mod['func_6051'] = func_6051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mod.get_global_var('func_2412')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_6059 = relay.TupleGetItem(func_2412_call(), 0)
call_6060 = relay.TupleGetItem(func_2413_call(), 0)
func_4760_call = mod.get_global_var('func_4760')
func_4763_call = mutated_mod.get_global_var('func_4763')
var_6073 = relay.var("var_6073", dtype = "float32", shape = (2184,))#candidate|6073|(2184,)|var|float32
call_6072 = relay.TupleGetItem(func_4760_call(relay.reshape(var_6073.astype('float32'), [2184,])), 2)
call_6074 = relay.TupleGetItem(func_4763_call(relay.reshape(var_6073.astype('float32'), [2184,])), 2)
bop_6109 = relay.minimum(call_6072.astype('int16'), relay.reshape(call_6059.astype('int16'), relay.shape_of(call_6072))) # shape=(1, 16)
bop_6112 = relay.minimum(call_6074.astype('int16'), relay.reshape(call_6060.astype('int16'), relay.shape_of(call_6074))) # shape=(1, 16)
output = relay.Tuple([var_6073,bop_6109,])
output2 = relay.Tuple([var_6073,bop_6112,])
func_6117 = relay.Function([var_6073,], output)
mod['func_6117'] = func_6117
mod = relay.transform.InferType()(mod)
mutated_mod['func_6117'] = func_6117
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6118 = relay.var("var_6118", dtype = "float32", shape = (2184,))#candidate|6118|(2184,)|var|float32
func_6117_call = mutated_mod.get_global_var('func_6117')
call_6119 = func_6117_call(var_6118)
output = call_6119
func_6120 = relay.Function([var_6118], output)
mutated_mod['func_6120'] = func_6120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4120_call = mod.get_global_var('func_4120')
func_4122_call = mutated_mod.get_global_var('func_4122')
call_6129 = relay.TupleGetItem(func_4120_call(), 0)
call_6130 = relay.TupleGetItem(func_4122_call(), 0)
output = call_6129
output2 = call_6130
func_6131 = relay.Function([], output)
mod['func_6131'] = func_6131
mod = relay.transform.InferType()(mod)
output = func_6131()
func_6132 = relay.Function([], output)
mutated_mod['func_6132'] = func_6132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1146_call = mod.get_global_var('func_1146')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_6237 = relay.TupleGetItem(func_1146_call(), 0)
call_6238 = relay.TupleGetItem(func_1147_call(), 0)
func_5662_call = mod.get_global_var('func_5662')
func_5665_call = mutated_mod.get_global_var('func_5665')
const_6248 = relay.const([7,1,7,9,9,-9,-7,4,-6,-4,9,-1,-3,-6,2,-4,1,3,3,9,6,-4,3,-2,4,9,-9,6,-7,7,-6,-10,-4,-4,-5,-10,-1,3,2,-4,-3,-10,1,-6,-8,2,4,10,7,5,-7,4,-1,3,-2,10,9,-2,7,1,-3,-3,4,-4,-7,4,6,-3,5,-10,4,6,3,-6,-6,-8,-9,-5,-4,6,10,7,-8,-2,-10,-1,4,10,3,-8,4,-9,8,-7,-5,-6,-5,-10,7,5,4,-4,3,-6,9,-5,-3,-7,10,-5,-9,1,-8,-8,-3,-2,10,7,-9,8], dtype = "int16")#candidate|6248|(120,)|const|int16
var_6249 = relay.var("var_6249", dtype = "int16", shape = (490,))#candidate|6249|(490,)|var|int16
call_6247 = relay.TupleGetItem(func_5662_call(relay.reshape(const_6248.astype('int16'), [3, 5, 8]), relay.reshape(var_6249.astype('int16'), [490,]), ), 2)
call_6250 = relay.TupleGetItem(func_5665_call(relay.reshape(const_6248.astype('int16'), [3, 5, 8]), relay.reshape(var_6249.astype('int16'), [490,]), ), 2)
func_4543_call = mod.get_global_var('func_4543')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_6265 = relay.TupleGetItem(func_4543_call(), 1)
call_6266 = relay.TupleGetItem(func_4544_call(), 1)
func_4120_call = mod.get_global_var('func_4120')
func_4122_call = mutated_mod.get_global_var('func_4122')
call_6275 = relay.TupleGetItem(func_4120_call(), 0)
call_6276 = relay.TupleGetItem(func_4122_call(), 0)
func_2598_call = mod.get_global_var('func_2598')
func_2601_call = mutated_mod.get_global_var('func_2601')
call_6288 = func_2598_call(relay.reshape(call_6265.astype('uint16'), [4, 2, 2]))
call_6289 = func_2598_call(relay.reshape(call_6265.astype('uint16'), [4, 2, 2]))
output = relay.Tuple([call_6237,call_6247,const_6248,var_6249,call_6265,call_6275,call_6288,])
output2 = relay.Tuple([call_6238,call_6250,const_6248,var_6249,call_6266,call_6276,call_6289,])
func_6299 = relay.Function([var_6249,], output)
mod['func_6299'] = func_6299
mod = relay.transform.InferType()(mod)
mutated_mod['func_6299'] = func_6299
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6300 = relay.var("var_6300", dtype = "int16", shape = (490,))#candidate|6300|(490,)|var|int16
func_6299_call = mutated_mod.get_global_var('func_6299')
call_6301 = func_6299_call(var_6300)
output = call_6301
func_6302 = relay.Function([var_6300], output)
mutated_mod['func_6302'] = func_6302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_6331 = relay.TupleGetItem(func_3841_call(), 0)
call_6332 = relay.TupleGetItem(func_3842_call(), 0)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_6359 = relay.TupleGetItem(func_3841_call(), 2)
call_6360 = relay.TupleGetItem(func_3842_call(), 2)
func_1359_call = mod.get_global_var('func_1359')
func_1362_call = mutated_mod.get_global_var('func_1362')
const_6375 = relay.const(4, dtype = "int16")#candidate|6375|()|const|int16
const_6376 = relay.const([5,-9,3,-5,-8,1,6,5,-1,5,-9,2,-7,-7,4,-5,-7,-1,-8,7,-3,7,2,-3,1,2,-2,-3,-3,-2,-8,6,-3,-6,-5,-8,-1,10,-7,4,-10,-9,-3,3,-5,-2,10,-8,7,4,7,2,7,3,4,-5,6,-5,6,-6,3,-4,8,-7,-6,-8,-3,2,2,-7,3,-9,5,9,-3,4,4,8,10,6,-6,-8,5,-10,-7,3,8,10,-5,-7,-3,4,-7,-9,8,2,2,-5,-1,-5,-4,10,-10,7,7,-6,3,10,-4,6,6,6,-9,6,5,-10,-10,1,1,5,-2,-10,1,-4,1,-7,-9,7,-1,1,4,5,4,-2,-5,-2,-8,-9,-4,-5,6,-6,-4,-4,5,3,7,-1,-5,5,-10,7,9,10,-1,-2,7,-4,8,8,-3,3,10,-2,-7,-6,-4,-8,9,10,-10,-8,8,-10,10,-10,-10,7,-6,-6,6,3,-3,6,-6,-1,-7,-5,-1,-3,-4,5,7,5,-1,-8,3,8,10,-7,10,-5,8,-2,-9,-1,-10,-9,6,-10,-5,3,-10,3,7,-10,-9,-4,7,8,-2,8,-5,9,-3,10,9,-7,8,-1,-1,10,6,-10,1,-8,9,5,5,7,2,7,5,-10,-5,8,4,7,-3,4,5,6,-9,9,-4,-3,6,-8,5,3,-1,-7,8,-6,1,4,-3,1,1,8,-6,2,3,2,7,8,-6,-4,9,5,9,7,8,-4,7,4,4,-7,5,-5,-7,-2,-7,7,-4,7,10,5,-3,-8,-2,-8,-10,3,4,-10,10,4,-6,-5,-1,-6,-8,8,-2,6,1,-10,6,-6,1,3,-8,1,6,-4,10,-8,3,-2,4,-8,-9,-6,4,-9,-8,8,-7,-9,7,-10,5,5,-5,2,-2,-4,3,-8,-2,3,9,-5,4,-1,-7,-8,-8,10,-2,3,-5,7,-5,-6,-3,-6,-2,-9,2,7,-1,-2,10,2,-6,-5,2,-8,6,3,-3,-2,-9,-1,-2,-10,3,-4,6,2,3,-3,-9,9,7,7,-10,-4,1,-9,4,-6,5,-8,7,5,7,-2,-10,-4,-4,6,-9,4,8,2,7,8,9,-5,6,-4,-7,-1,-9,6,5,9,4,3,1,5,5,-1,7,-9,-7,8,-9,-3,-4,-4,-10,-3,8,-8,3,-8,5,5,7,-7,-6,10,-5,-6,1,10,-2,-8,10,9,9,6,-7,8,-2,8,-1,7,-1,-7,-4,-6,1,-7,1,-8,5,4,2,6,8,-6,-2,7,8,8], dtype = "int16")#candidate|6376|(490,)|const|int16
call_6374 = relay.TupleGetItem(func_1359_call(relay.reshape(const_6375.astype('int16'), []), relay.reshape(const_6376.astype('int16'), [490,]), ), 1)
call_6377 = relay.TupleGetItem(func_1362_call(relay.reshape(const_6375.astype('int16'), []), relay.reshape(const_6376.astype('int16'), [490,]), ), 1)
output = relay.Tuple([call_6331,call_6359,call_6374,const_6375,const_6376,])
output2 = relay.Tuple([call_6332,call_6360,call_6377,const_6375,const_6376,])
func_6385 = relay.Function([], output)
mod['func_6385'] = func_6385
mod = relay.transform.InferType()(mod)
output = func_6385()
func_6386 = relay.Function([], output)
mutated_mod['func_6386'] = func_6386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1929_call = mod.get_global_var('func_1929')
func_1931_call = mutated_mod.get_global_var('func_1931')
call_6419 = relay.TupleGetItem(func_1929_call(), 0)
call_6420 = relay.TupleGetItem(func_1931_call(), 0)
output = call_6419
output2 = call_6420
func_6430 = relay.Function([], output)
mod['func_6430'] = func_6430
mod = relay.transform.InferType()(mod)
output = func_6430()
func_6431 = relay.Function([], output)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_863_call = mutated_mod.get_global_var('func_863')
call_6445 = relay.TupleGetItem(func_861_call(), 0)
call_6446 = relay.TupleGetItem(func_863_call(), 0)
output = call_6445
output2 = call_6446
func_6457 = relay.Function([], output)
mod['func_6457'] = func_6457
mod = relay.transform.InferType()(mod)
output = func_6457()
func_6458 = relay.Function([], output)
mutated_mod['func_6458'] = func_6458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mod.get_global_var('func_5164')
func_5165_call = mutated_mod.get_global_var('func_5165')
call_6472 = relay.TupleGetItem(func_5164_call(), 0)
call_6473 = relay.TupleGetItem(func_5165_call(), 0)
output = call_6472
output2 = call_6473
func_6476 = relay.Function([], output)
mod['func_6476'] = func_6476
mod = relay.transform.InferType()(mod)
mutated_mod['func_6476'] = func_6476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6476_call = mutated_mod.get_global_var('func_6476')
call_6477 = func_6476_call()
output = call_6477
func_6478 = relay.Function([], output)
mutated_mod['func_6478'] = func_6478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4587_call = mod.get_global_var('func_4587')
func_4588_call = mutated_mod.get_global_var('func_4588')
call_6544 = relay.TupleGetItem(func_4587_call(), 2)
call_6545 = relay.TupleGetItem(func_4588_call(), 2)
output = relay.Tuple([call_6544,])
output2 = relay.Tuple([call_6545,])
func_6555 = relay.Function([], output)
mod['func_6555'] = func_6555
mod = relay.transform.InferType()(mod)
output = func_6555()
func_6556 = relay.Function([], output)
mutated_mod['func_6556'] = func_6556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mod.get_global_var('func_4783')
func_4784_call = mutated_mod.get_global_var('func_4784')
call_6559 = relay.TupleGetItem(func_4783_call(), 0)
call_6560 = relay.TupleGetItem(func_4784_call(), 0)
func_5854_call = mod.get_global_var('func_5854')
func_5856_call = mutated_mod.get_global_var('func_5856')
call_6566 = relay.TupleGetItem(func_5854_call(), 0)
call_6567 = relay.TupleGetItem(func_5856_call(), 0)
output = relay.Tuple([call_6559,call_6566,])
output2 = relay.Tuple([call_6560,call_6567,])
func_6571 = relay.Function([], output)
mod['func_6571'] = func_6571
mod = relay.transform.InferType()(mod)
mutated_mod['func_6571'] = func_6571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6571_call = mutated_mod.get_global_var('func_6571')
call_6572 = func_6571_call()
output = call_6572
func_6573 = relay.Function([], output)
mutated_mod['func_6573'] = func_6573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6385_call = mod.get_global_var('func_6385')
func_6386_call = mutated_mod.get_global_var('func_6386')
call_6658 = relay.TupleGetItem(func_6385_call(), 2)
call_6659 = relay.TupleGetItem(func_6386_call(), 2)
output = call_6658
output2 = call_6659
func_6664 = relay.Function([], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
mutated_mod['func_6664'] = func_6664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6664_call = mutated_mod.get_global_var('func_6664')
call_6665 = func_6664_call()
output = call_6665
func_6666 = relay.Function([], output)
mutated_mod['func_6666'] = func_6666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4444_call = mod.get_global_var('func_4444')
func_4445_call = mutated_mod.get_global_var('func_4445')
call_6681 = func_4444_call()
call_6682 = func_4444_call()
func_4943_call = mod.get_global_var('func_4943')
func_4947_call = mutated_mod.get_global_var('func_4947')
var_6686 = relay.var("var_6686", dtype = "float64", shape = (49,))#candidate|6686|(49,)|var|float64
const_6687 = relay.const([0.325385,-9.274984,-4.971347,-8.937328,0.328702,4.207323,2.425479,6.305242,3.071031,-0.101740,4.296500,-7.833795,9.975639,-2.880357,-5.730397,-9.988718,7.571091,-6.414117,3.268529,-3.542927,-7.806322,-3.179405,-5.177825,-9.891649,-0.513648,4.777795,-1.162806,-7.288878,7.677168,8.530356,-2.055909,1.610121,-4.751189,-1.341379,0.895693,-6.093837,-7.340923,9.791218,-2.217794,-0.105803,-9.166816,-5.569545,6.432071,-7.775911,-4.867942,6.195970,7.087288,-4.248724,-5.074491,9.970800,0.395723,2.661261,8.721725,-9.901697,8.701090,-0.606262,-9.790121,-3.103840,5.159543,-7.049241,-5.748580,8.162975,7.336552,3.603457,-1.057403,0.528890,6.107733,5.081847,9.215921,-6.683653,2.185908,-6.664918,-3.230648,2.608973,3.002369,3.774128,8.723095,3.313043,-5.778964,-9.132422,-2.921531,-7.756272,3.813935,-7.574478,-6.943495,5.310415,4.402381,5.253560,-9.279999,-1.332241,9.605676,-8.976234,-5.198502,2.832444,-7.811371,8.377173,7.999557,-2.157936,1.571368,5.163402,-5.827410,0.205675,-8.220299,0.728892,-5.304197,-5.362163,7.457869,-6.036267,-2.298365,-2.097980,-7.907775,8.273706,6.667789,-5.116277,-0.823171,-6.512237,-4.787494,8.971109,1.403686,8.946979,-8.447781,8.731610,-4.604352,5.958353,9.879085,-8.982818,8.780669,7.155581,0.626769,8.837097,1.606216,-4.819246,-4.788601,-1.489511,-8.507896,6.074440,1.765667,-9.096136,-8.543570,-3.845393,2.847144,6.647373,4.589853,-3.346104,-8.956272,-4.815790,4.993678,1.709307,-3.908499,2.369612,-0.613279,7.996829,3.831204,6.786483,4.714863,7.934436,-6.586015,2.349000,6.285451,5.469036,-9.002944,0.296835,-8.769829,8.438597,-3.019452,-1.784896,3.624855,-4.295295,2.609005,-4.944306,-6.277901,-2.791110,8.158277,-9.762692,7.370135,-7.237762,6.894837,1.998731,6.724461,4.300064,-7.142556,-0.271669,6.242946,-8.424030,-9.444124,-2.432231,7.682793,-5.377403,-9.877875,9.108398,-0.435716,5.638346,-5.719003,2.036610,1.518140,3.287070,-2.456814,3.692966,3.173996,2.259339,8.327898,-2.660404,-6.104178,2.033653,1.005819,-4.606116,-1.047897,4.523313,-2.566027,-4.313857,6.107082,7.432555,3.792253,-2.480621,5.084342,1.798874,1.037713,2.887818,-6.082675,-6.774078,6.327041,9.579254,8.976988,-7.345702,8.978429,1.784445,2.514050,5.819883,-2.291913,6.543679,5.294662,-6.657651,-1.041472,-6.475023,-5.426503,-1.377339,4.338511,2.676629,-8.761278,-8.341769,9.363707,0.252164,1.192836,7.882619,-3.552778,7.275675,1.666595,-8.032756,0.773087,-4.885225,9.432290,3.136666,-7.493212,9.701323,1.850359,7.940799,-5.247628,4.051406,8.899998,3.299373,6.180359,7.018172,-4.435285,-7.329400,-3.421783,8.632411,2.757980,-9.267651,0.542826,-5.898413,4.712305,4.786369,-9.112479,7.258389,-6.234841,0.092499,9.708600,-0.352394,-5.245166,4.936607,-9.397692,7.739491,-2.628278,5.988177,7.960903,-6.725610,4.890548,-2.274168,-6.231363,7.065084,-3.502969,-7.560822,2.699744,5.581542,8.239864,-4.040429,6.385392,1.979668,2.985567,-3.348480,-6.022996,-1.034499,-9.010804,-8.201545,-7.385761,1.862609,-1.461617,6.073973,9.687467,-9.170023,9.335183,-0.915042,-0.348934,-7.998107,-1.733770,-8.326009,9.145851,4.459365,-8.552766,-2.122108,9.513989,2.891428,7.323313,-3.789458,-7.410722,6.147840,0.452490,-7.036712,0.484690,-7.753453,2.768195,1.866062,2.480456,9.340067,-3.399338,-9.929507,9.835080,0.358236,-3.726414,0.151117,-0.655956,5.542134,-0.248017,6.823810,-0.559084,-5.364442,6.944937,9.451168,-2.623894,-7.887996,-3.716434,-1.071881,-3.400881,7.346406,7.517567,9.724716,0.173772,-1.819288,0.996090,-4.211216,0.075605,8.455153,-6.564516,7.175785,0.516497,3.846072,-8.064958,-3.766220,6.367256,-5.424251,-7.831802,2.513520,-1.290274,-1.078711,4.428023,7.160223,6.592313,5.320448,4.341834,-7.792971,-2.250915,8.048913,0.052856,-9.185933,2.260509,-7.643489,-6.331901,5.408697,6.546894,-1.604469,-7.838422,0.077840,2.815247,0.700660,4.602928,7.760092,5.798340,-7.686638,-3.646857,-8.428959,6.570524,-9.540945,-6.481385,-4.623108,0.530169,-8.433954,3.079070,3.761187,0.695712,7.132807,-4.754302,-4.257209,0.801656,-0.895625,0.156301,5.015350,7.142999,8.328139,-1.403649,7.810867,-9.191367,9.035913,1.512751,-8.968646,-5.017429,4.536612,7.295799,-2.368937,7.235883,-1.416952,7.093792,2.742651,3.934675,-9.257627,3.237631,1.660346,-0.985588,6.255091,5.641731,-6.767796,1.624645,-8.034491,1.536010,-6.083712,-4.061474,-0.332168,-8.420059,-7.619016,-1.888577,5.686163,8.352568,8.389223,-1.338076,9.531509,3.699082,1.015239,-0.121305,0.383955,-0.488831,-8.385197,-8.890649,1.040680,-1.079672,4.871758,-1.977019,-7.549004,8.478088,6.805501,-0.711355,-5.498165,-4.530866,4.128766,8.243635,0.172197,-4.002546,-2.658700,-3.806473,0.843496,-0.025648,7.067142,-6.336063,-5.450838,7.314055,8.993164,-0.660365,9.730216,6.535424,8.065688,8.939459,-8.980469,-1.679026,5.105209,-5.008845,-0.092466,8.588356,-9.137727,7.126058,3.510685,-0.515776,0.853147,-4.061353,-7.040901,4.936822,8.817702,-9.996692,-4.796191,-8.818580,7.696322,-8.275054,2.424433,2.616285,2.021482,-9.130436,0.874732,5.941290,-8.246807,-3.506104,2.741047,-4.192045,-0.888524,2.817051,-9.166468,-6.769711,-8.012712,1.170030,-5.953351,6.812300,4.095405,3.310341,1.513518,0.548259,-8.650930,-4.233292,2.199053,-1.870193,0.038059,-0.635497,-8.420562,6.210989,-5.105946,-6.712914,1.062952,-6.807307,-1.562027,4.640760,3.483574,4.945702,-2.800026,7.400699,-5.155934,-1.822904,0.909238,8.917742,8.805501,8.432254,4.605258,0.838532,6.660866,-7.910845,6.601479,5.438295,-5.921267,-9.280464,-3.944143,2.886050,-8.997492,-1.712042,-9.673208,3.497305,-3.115313,3.643166,-4.147239,-0.691940,5.974683,7.758246,6.741200,9.741884,5.038396,-0.009654,1.800015,0.326054,4.874578,-8.010707,3.954878,-8.744655,-5.341213,-7.102876,-9.190734,-4.076495,5.341761,-3.393133,6.392242,-8.965739,2.215991,-4.565750,-4.438580,-5.614397,-7.651910,-1.367960,-6.748622,7.862859,-4.921443,-3.930007,7.510723,-5.766020,-9.783420,9.150436,-3.220968,4.843535,-0.817021,9.695326,1.990559,7.352796,-8.463891,8.640447,-9.908301,1.193266,-1.565377,9.761590,-0.845893,-4.868759,-9.490701,-3.173519,-7.853901,-8.797925,-4.781773,4.638821,-8.354369,4.283305,-7.883747,6.260068,9.384726,-3.482099,-0.506271,6.711128,3.863809,-2.882953,4.830098,6.982475,-0.063361,5.520385,3.535569,-6.199480,1.048483,-3.434099,-3.942502,-9.420502,-2.379178,-3.837603,-7.840287,5.108357,7.454915,2.870934,3.001821,-4.291675,-9.803139,-1.119140,5.903980,5.061013,-7.037134,-2.115358,-4.757662,-5.795809,2.316671,5.344119,0.235987,-8.817322,-6.746425,3.752298,-3.826119,1.237135,1.203257,-1.831167,-5.407675,6.892479,6.354750,-1.835209,-8.210624,-7.054692,2.120911,7.269799,-7.236642,4.994777,5.208737,-6.177510,1.939821,7.831602,4.882335,9.448689,1.424429,-8.586081,-8.938835,-8.367905,-2.048379,8.937422,5.677154,-2.032932,-6.812338,-1.187693,-1.051062,5.910342,3.614110,0.878068,-1.077657,-1.083417,0.351181,-3.910902,2.124474,8.146585,4.896056,2.449219,3.198795,-3.946158,-1.581761,-8.862567,-7.719097,-0.540479,-6.070119,-9.255195,-8.692875,-3.941027,-0.426398,2.819344,-1.102317,8.035099,8.760160,-6.867659,-9.972729,-8.243413,6.587418,4.622071,-5.684715,7.530931,7.353678,7.725280,0.537991,-6.373323,-8.231118,5.015083,-3.065640,-3.834627,-7.440141,-0.887369,-1.943625,8.334708,7.769251,3.620752,-5.215757,-5.189132,-4.192229,3.294188,-8.235421,8.437992,0.859469,5.458599,9.652802,-0.857689,-5.100646,-4.232138,5.466213,-2.952727,3.338681,4.843770,4.813562,6.110364,3.424927,7.758685,-5.449133], dtype = "float32")#candidate|6687|(768,)|const|float32
call_6685 = relay.TupleGetItem(func_4943_call(relay.reshape(var_6686.astype('float64'), [49,]), relay.reshape(const_6687.astype('float32'), [768, 1]), ), 0)
call_6688 = relay.TupleGetItem(func_4947_call(relay.reshape(var_6686.astype('float64'), [49,]), relay.reshape(const_6687.astype('float32'), [768, 1]), ), 0)
var_6689 = relay.var("var_6689", dtype = "float64", shape = (49,))#candidate|6689|(49,)|var|float64
bop_6690 = relay.equal(var_6686.astype('bool'), relay.reshape(var_6689.astype('bool'), relay.shape_of(var_6686))) # shape=(49,)
func_2860_call = mod.get_global_var('func_2860')
func_2863_call = mutated_mod.get_global_var('func_2863')
const_6695 = relay.const([[-3.100938,4.998722,7.059839,9.312824,0.544661,-4.718060,1.793384,1.626720,-0.345350,-7.396708,-1.742073,-0.262536,8.679244,-5.425835,6.400318,-2.994152,7.849283,-0.225161,-6.337031,-5.396351,-0.717575,-1.290915,-5.596070,-7.795960,-3.498495,-7.895212,2.455748,8.007128,0.056606,-7.689815,-5.249962,-9.146717,-1.312947,-9.849829,-2.493224,-2.121467,-8.100232,7.690416,3.964646,4.946973,-2.881034,-9.839710,9.873101,-2.297554,2.271320,1.550202,8.347988,9.790644,-3.542778,-4.151757,-4.535016,8.768980,-7.183182,-2.786814,0.957967,2.005115,1.329278,5.971257,-9.261089,9.137920,-2.233157,6.601465,-5.749410,7.904546,9.979256,-8.015595,-3.440898,-4.440134,-2.952592,-3.977668,-2.031526,7.513743,3.317926,-9.840252,-4.317809,8.530484,-1.531759,0.241969,-8.709441,-6.768718,-0.766129,5.264317,-9.979381,7.125784,-1.868296,-9.864724,-9.679791,5.958200,-3.285740,6.659747,4.276484,2.981552,9.860101,8.089726,5.627034,6.551923,-4.032335,6.907527,-3.509876,5.019271,-3.151804,-1.692544,8.118975,4.211709,9.249556,-3.497404,9.820817,2.644562,-1.729421,-9.177970,-5.076835,-5.238270,6.506852,4.745769,-1.441439,-7.613941,2.791948,2.944096,-2.821069,-8.157794,5.586078,1.565221,2.136963,-2.555873,2.860796,8.087081,-4.077305,-9.628815,2.056347,-5.857696,-0.350729,1.372765,1.920664,-9.999223,3.560784,3.931120,2.121215,3.170234,3.424371,6.335712,3.916574,-7.743964,-9.423069,7.697032,5.182488,8.750616,-2.302147,9.332949,-3.571680,-0.765834,-6.826766,-8.516896,-5.469935,-3.978528,0.385513,-1.249867,0.959043,3.350986,9.124086,1.883886,-1.722643,-7.660111,5.138559,-5.230662,3.865779,4.497498,-5.866387,7.163038,-8.166509,6.930371,2.663782,-3.259065,-9.954057,-5.011657,-3.302719,-5.949795,6.091150,2.822268,-2.495840,-2.308696,-2.685199,-4.131139,6.575087,2.928724,3.603624,-0.358250,-4.024901,2.632326,-6.811727,-8.009260,-9.880090,4.808081,1.894496,-9.598356,-2.085929,8.737971,9.630269,6.759148,-7.750530,-7.359845,2.414902,-9.117381,1.061603,4.073012,-1.906764,-6.209347,-5.470920,-8.344890,-1.310342,-4.915020,5.779492,-9.901600,0.939548,3.256924,-6.880773,5.351310,-7.563332,-6.009485,-6.586055,3.161729,5.520990,2.950753,3.281051,-3.588505,-1.701558,-6.149920,-2.475914,-1.081403,5.959306,6.667029,7.695352,5.794553,9.915154,6.388671,4.249525,-9.573409,-1.196033,6.911393,9.938685,-4.303957,-8.374127,1.942302,3.228333,-0.127441,0.196973,-7.629728,-3.498139,1.105245,8.106806,3.476203,3.632616,-9.751485,8.282974,-5.087330,0.599621,3.822976,9.179633,-8.345427,-7.016061,5.139815,2.101083,1.816616,-3.417338,7.786957,9.334337,-8.437535,-6.035103,3.793727,-9.826332,-5.270106,-8.250651,8.851067,-6.612051,-4.530047,-9.420721,-7.830094,2.534169,-1.730373,-1.341742,-4.376412,-5.968987,5.635342,0.243417,4.719886,-9.098299,3.823245,5.418506,-2.557344,-1.619419,-6.712703,3.430887,-8.444246,-0.853870,-2.161468,-0.816979,8.067103,5.022089,5.022683,8.942571,6.280705,-6.541368,-0.528436,7.210694,8.064136,2.803781,5.704590,4.670521,0.223874,-1.802777,-0.873846,-1.834332,2.435208,-2.168482,-2.046416,8.368377,2.429816,-9.448355,8.479259,9.437945,-9.557538,8.540984,5.844924,8.465141,-8.851106,-8.852118,9.737297,-5.628202,-4.851999,8.853656,-1.067951,-3.976324,2.788012,9.008573,0.495794,2.109084,1.079039,8.382911,6.021331,-1.918052,-5.524040,9.039144,4.572697,-3.491830,-2.212779,5.382037,9.873438,3.112298,-8.770067,9.071816,5.985362,1.628026,7.661226,1.270805,-5.084089,5.977234,-5.100751,-5.488975,-7.976056,4.615918,-8.675424,-7.410634,2.091814,-9.671330,-2.815242,2.679674,9.098015,0.861214,9.370464,4.116848,-9.415600,-6.266217,2.136062,-9.792068,3.745533,3.582157,-3.878556,3.645803,0.280167,-1.991097,-9.355570,7.314767,-8.643261,-5.634575,7.525748,8.646568,-1.389271,-7.067151,-1.519701,-3.328825,-1.323291,-0.170596,8.069809,-0.413719,1.511226,-7.711247,-6.928951,7.459692,-2.310594,-4.698481,-9.037255,3.756573,3.767842,-1.537694,5.540419,-7.451119,-2.818142,-2.882936,-1.989248,-4.577628,1.811237,8.375151,-3.543368,5.162667,7.514615,-0.035895,8.242951,-7.672545,4.154880,7.884378,6.202515,2.518822,-8.250254,7.624570,-8.868337,-5.242398,0.890805,-7.378018,9.246417,-0.326691,7.941091,-5.582818,4.081322,-4.156133,0.919781,5.610311,6.389953,5.902699,-2.039376,-8.835560,-1.960015,4.971688,3.316229,-2.702770,9.261663,8.740993,1.949194,6.519251,-8.526036,-1.807416,1.812948,9.494306,-8.813342,-1.953287,9.263135,7.128405,-0.664186,1.383818,-3.764409,-4.762023,3.865370,9.559953,1.776671,2.221139,-5.800933,5.077284,8.033816,-9.901256,4.274354,-5.506152,6.663152,9.568401,-5.680438,1.137295,-6.725461,-8.288795,1.637459,-4.549187,2.832672,2.891472,5.322096,4.718531,2.157014,-3.660526,6.816355,0.966407,1.377885,-5.535916,-1.590861,-2.382388,7.354735,-0.427322,-0.663668,5.899703,-0.342626,4.352905,3.209312,-0.187622,-2.700353,-2.542026,6.131359,1.048555,-4.852857,7.688616,7.723410,3.943659,-5.665656,-3.868137,-9.993783,-1.258860,-9.952076,4.802538,0.494475,-7.876845,-7.069753,9.256927,-0.934544,-3.300252,-5.682181,0.399349,-6.812310,-8.098394,-9.281066,6.492584,-2.758923,6.111535,-8.410447,-4.422447,-7.976093,3.693147,6.326921,4.066463,7.403616,-1.342014,0.112952,-9.863657,-2.898726,-4.664071,2.026732,-0.930340,-3.718708,-4.231180,-0.817261,-6.330633,7.961834,3.273003,-5.775105,-9.082215,6.560199,2.209593,2.249864,-9.721954,-1.565611,-5.981480,-4.848072,6.572435,1.556999,9.704763,-6.390782,-4.180559,-5.013742,6.318422,-0.325036,-2.990931,-0.621937,-2.435878,8.786383,-8.223460,-9.206810,3.520969,3.923318,3.605988,-6.135923,-8.239872,-7.965522,-3.871037,-7.762702,8.956534,-9.606837,-0.003491,3.200879,-4.782154,1.964472,-2.737088,6.808163,1.176391,-7.648415,3.709053,0.527978,8.264670,8.159640,-8.348758,4.577901,-4.585520,-6.746678,0.289572,-4.401158,-9.501745,-4.309268,7.765093,2.792949,-3.210990,6.432681,-0.209830,1.689780,-6.917119,-4.324144,-1.266771,-5.779645,0.494976,-5.843255,-8.905652,-8.971564,-3.710063,5.593411,-6.845722,-7.197494,-3.401373,4.241969,2.958326,-9.899344,4.593870,-5.290838,7.600187,-8.239907,1.516867,0.133979,5.418204,1.114151,-6.781385,1.361313,9.745739,1.299418,2.424792,-5.876292,3.432220,-5.200806,7.843328,-8.113594,4.905917,3.111943,7.426422,-6.649238,-9.755354,8.281491,-8.738047,-4.396672,-2.870425,9.866260,-1.880342,-2.447765,8.870157,-0.490095,-3.758942,4.677195,1.807654,-1.059388,5.198948,-6.926144,-5.351766,-0.998259,-2.146433,-0.717403,-1.877464,8.313601,-1.842227,-2.724470,-2.569912,-6.034627,5.096636,7.339375,4.544347,-7.504700,-3.151430,-5.218181,-8.813743,-2.381444,3.593952,8.181142,-3.164214,-5.191127,8.791031,-1.692552,2.576270,-7.634397,-3.423167,-6.388708,1.105769,-9.315797,1.900869,0.692539,0.438462,-4.792877,-2.267503,-0.631422,-7.211766,3.402514,1.696538,-8.448693,1.372364,-8.684348,-2.685341,8.294316,7.155634,9.928849,-1.328181,-3.034372,-2.287905,5.662035,-6.849666,-4.396083,-5.399701,-8.563682,1.834181,2.176695,6.617401,5.136049,-2.889206,-9.103473,-8.040821,-2.413822,-6.189509,7.022647,9.705635,6.219978,-3.141051,7.644296,-9.363330,8.836986,-7.703986,-1.341660,-3.591353,5.913297,-5.630008,-9.997566,1.164057,1.257164,1.938300,0.469824,8.528458,-2.492661,-9.615501,4.504474,-7.786253,-5.615647,8.304997,-3.411215,-1.510659,-6.607709,7.381986,-6.506098,3.341792,-4.170449,-6.429064,6.424370,2.606598,3.009029,4.518580,-2.106392,3.023078,-2.556211,5.012937,-9.763565,-7.083455,-7.598978,5.421026,2.427105,-6.071005,7.373414,5.296981,8.224387,6.103653,-7.704730,1.441638,-8.021605,1.548996,3.794867,2.470665,6.004812,-1.269575,-1.578934,-3.592686,-5.601490,7.020618,1.325762,-8.928469,8.707064,4.507908,8.513721,-3.546678,-0.137494,-0.870927,-9.819106,6.421807,-4.879030,6.156609,-5.988989,-9.430684,4.348176,-3.407067,-9.501080,9.421711,-4.100749,9.227518,8.778884,2.841547,2.975753,7.752023,-8.764321,4.119778,-1.000168,7.601964,-3.284533,4.033085,4.104738,-3.956804,-0.985519,-1.355722,2.079149,-1.500284,1.134513,-1.873695,-7.304859,6.849984,-8.855312,7.845855,2.428620,5.219330,-6.528684,9.991635,0.501499,4.682429,5.894027,-4.507427,1.093752,5.530121,4.235320,7.074791,8.531592,-6.360025,-9.295661,-6.814112,-4.626506,3.260905,-6.802533,-1.110756,5.529128,-9.881707,4.166672,3.852261,9.074688,-8.626790,-5.103829,-4.518114,-9.421406,9.300652,-5.878143,-8.262376,-4.407731,7.785405,0.705464,-1.416291,3.581268,1.502727,8.343018,8.800440,-6.279191,4.818529,-8.811054,-3.960761,-7.822116,4.344483,-0.003662,0.760557,8.452176,2.406226,5.425914,8.508680,-8.750106,7.061258,4.192671,3.213243,-5.271701,-4.074806,-1.141651,4.717281,5.345737,-9.471678,6.440900,-3.105992,-4.665857,2.772609,8.917787,9.388416,6.266046,0.584172,8.659362,-1.625015,-3.401454,-2.017643,-4.492975,0.695320,-0.572530,1.170961,-4.532755,2.977480,8.713075,-9.318293,0.871019,9.000721,-6.482755,-3.693198,9.720137,-4.124593,3.004572,-2.282636,-3.773930,4.054827,8.467273,-5.168025,-3.272287,1.647020,-5.987034,-6.723845,6.151766,9.461671,2.574476,5.689592,-7.423156,-4.785931,4.386871,7.519583,-6.448581,-2.269575,9.109389,9.604681,-3.600206,-0.859176,-6.027505,8.699936,-3.588504,-6.811563,-7.421375,-3.450227,5.705634,-1.598542,7.916065,-9.867148,3.398950,-1.860299,-4.353208,-7.192416,-8.223245,9.528800,-6.498490,-1.032469,2.210289,-1.401669,-9.846811,8.379686,0.893395,-0.626985,7.294164,-3.086359,-4.354925,-8.277556,0.036521,0.152482,6.234217,-2.934678,1.203902,-8.990567,1.403500,-9.115019,8.905685,3.944745,-0.257374,7.789617,9.358214,-1.739454,-1.410679,-5.400232,4.110355,1.988766,-7.064385,-1.453627,-3.878474,4.027868,8.147354,-2.393896,5.791950,4.620439,7.827683,2.968460,4.572639,-2.916431,-9.390737,9.294355,6.381280,-3.942350,-6.092861,7.041175,8.821743,6.220736,8.697496,5.325002,3.343708,-7.124425,-6.154899,9.952400,0.930576,0.933228,-6.212083,0.791797,-1.774165,-4.345376,3.413802,9.982511,-5.856263,8.399448,-8.094799,-9.199142,-4.290573,0.423975,-7.137246,-3.732682,-4.279775,-5.696963,-5.359626,-9.122183,1.438189,2.538191,8.785407,-2.192888,6.701123,8.219336,-8.187028,-5.372473,-6.626152,8.506271,-0.328928,-9.536613,-7.661618,-7.214112,-0.174833,5.900676,0.785218,-3.328493,8.859957,-6.099112,8.175289,0.427089,3.853085,-9.541885,1.279541,-0.085923,3.534807,-3.797231,7.728818,-0.508805,-7.891728,-4.417212,-7.787691,-3.713396,1.949088,9.328256,-5.027825,-0.410269,-2.184983,5.279750,4.690922,6.893401,-1.330900,-6.930961,-4.851699,9.580889,-8.012721,-7.198613,5.485806,-4.866887,8.752409,7.239099,-0.640894,4.145070,-2.098906,-2.254279,6.081694,-1.339945,-6.910996,7.099450,6.560641,0.315788,-1.976317],[-3.539077,-0.361673,-2.184060,-1.534165,3.889120,-4.517857,7.571252,0.420426,-7.577628,-7.760369,-3.885226,3.919080,9.579682,-0.925828,-1.576558,7.502016,-7.775004,1.214974,2.298549,-5.465490,4.937521,-1.212336,7.453237,-8.701015,-9.055802,-6.137145,9.463605,-5.577966,-3.180860,3.654738,-6.486550,-4.028416,-8.017010,9.104669,0.635724,-6.874284,-3.988028,-1.662710,-6.740048,7.410472,4.421403,2.844919,3.333430,1.974595,4.741537,-1.280842,1.404014,-6.213535,5.587018,-7.851580,-9.564645,7.666981,7.374920,-2.722962,-7.187132,-7.448724,-1.995927,3.739544,1.896704,5.204911,8.922942,-4.938047,-8.891431,1.773473,8.481394,8.263146,-4.363880,-5.725858,-0.608074,-9.150767,4.776238,-1.593610,-0.167430,0.336256,-8.427633,-7.602968,3.388233,7.326082,-5.271389,5.935234,-6.188047,0.424824,9.412243,-2.839261,-3.164477,-4.530983,9.526506,2.468210,-1.613723,0.661574,-1.193385,1.731124,5.053535,9.448541,9.743615,1.624479,1.490450,-8.289027,-9.012848,-6.779240,1.292703,-8.170786,8.795614,4.597801,4.446894,4.498229,-5.647245,7.898339,3.912477,8.223496,3.679170,-5.072739,2.010696,0.159024,8.925310,8.060536,-1.803930,7.672053,4.284157,-8.298259,4.447216,-6.056527,-4.873219,0.990664,6.692859,-2.060759,5.371209,5.906162,2.137022,7.966275,9.558963,-2.735403,-4.802433,7.910714,-4.559827,-8.509188,1.945570,9.273762,-3.679812,6.087365,-5.363915,-7.047409,-3.088508,-6.556991,-0.167272,-2.670183,-6.830654,-0.089936,-8.909962,9.376471,6.581798,9.776928,-0.165817,-2.810430,6.298532,-2.513380,2.108028,-6.390779,8.882190,6.461079,-1.201672,6.092914,-6.944700,0.470071,6.036595,9.527697,1.647183,-4.495487,-1.021060,-9.194240,-9.317572,5.410096,-2.875258,-7.844124,-7.897939,9.792269,3.743531,-9.611610,-8.145078,1.650897,-2.155922,-0.645484,6.025391,8.121036,8.649364,3.728046,3.024956,3.872751,-5.142233,5.716166,-7.666874,2.981274,2.815519,7.227276,-7.696505,4.399774,-7.908050,-9.795448,-3.769456,0.388851,7.602617,-9.643154,8.101142,-2.058673,3.700347,-0.387248,5.582411,2.914681,7.995123,-6.438641,0.055001,-8.701829,-8.462265,7.034235,4.396419,-6.499662,-4.466384,4.028925,6.011811,2.386187,6.581751,-4.404357,-8.702855,3.039737,-7.765845,2.717290,3.291789,3.349433,-5.326562,8.440761,0.796751,-2.893033,-7.407872,3.421636,-3.813667,-0.890230,9.657151,-8.779958,-1.158064,2.042468,7.119120,3.444053,6.818949,-3.928597,1.162170,4.847742,-3.967861,-1.387831,8.262674,-5.549326,4.396002,5.916669,6.591430,-0.367443,0.504423,-5.091202,-7.977029,2.458264,7.657701,3.094725,2.080639,5.682794,-4.415084,-9.153411,-4.169210,8.055390,7.205888,-5.106453,-9.101821,3.433871,-2.979347,7.103677,7.399317,-4.379259,-4.036498,2.629292,-4.283115,4.038098,4.760025,-9.402711,-3.590361,9.044348,-2.514417,-4.297845,-3.008531,-0.777661,-2.661005,7.490080,2.541498,-7.316265,3.566166,9.014096,-5.606319,-7.729606,1.641323,1.893629,2.202405,5.439676,-9.330809,-5.072872,0.445686,-6.009398,-6.832555,2.894354,6.218476,-8.374621,-4.362766,0.341749,-8.386216,-1.969490,-1.727018,-5.561395,-9.464161,-5.878697,4.182461,8.875327,1.421931,-0.773959,2.738057,4.430476,2.403569,0.031460,-1.279304,0.668357,-8.366776,-6.559655,5.445254,-7.011220,-6.774243,9.675659,-2.892627,0.834313,-4.276821,7.902758,0.315329,-1.321676,-7.431431,-2.028664,-7.243345,-8.424691,4.616457,-2.218044,6.160411,-2.247121,1.222338,2.093963,-4.707712,8.952233,9.062070,-7.822674,-8.161201,1.601094,-3.764206,6.369737,5.543855,-8.901453,-1.462255,-3.638609,0.779502,7.666029,-2.146688,-3.335218,8.637092,7.413407,8.966624,-3.501035,-5.429352,-6.118575,7.439380,-6.279850,6.312759,-0.673184,5.127361,9.478533,3.377378,0.389934,-6.262962,3.083681,4.948391,-4.970363,-8.744439,-6.740517,-6.321243,-5.271275,-8.967660,8.869406,6.344918,2.480123,-4.248300,8.876180,-5.652844,9.659826,5.478020,-7.701448,5.410110,5.312653,2.619569,-0.126363,-1.959521,-9.936372,5.028472,7.866179,8.850014,7.050225,2.943745,0.604426,4.677644,-3.201234,0.079361,-9.761594,6.762725,3.970882,8.129471,4.996895,-6.475401,9.583228,4.127231,-9.035251,7.688291,-7.002966,-6.572043,-0.050513,-5.830902,-5.995448,-3.758695,-3.875809,-6.444071,-8.410600,0.505114,-3.887484,4.530062,-8.933263,-8.806060,6.965083,-7.823405,-0.434721,-8.553344,8.222044,-8.257510,-9.832172,-7.897976,-6.467086,-2.137428,-3.995745,-5.557673,5.024382,-7.172838,-5.433487,-4.627408,8.865603,6.062661,-7.625118,-0.714196,-8.485874,7.004024,2.722399,7.764902,4.862281,2.383155,-4.549390,-6.165024,5.166999,7.686845,3.619829,-0.342154,-5.638803,-6.333865,0.117558,-9.500124,3.149615,-0.052715,0.608956,7.369978,-7.997046,5.185089,-4.258149,-2.573789,-0.395750,-2.351825,-3.443733,-7.305801,-9.906219,6.060602,-5.859232,-3.147477,1.208299,-6.874743,-9.737255,8.737684,-1.683438,3.346067,-9.390496,0.966020,5.462004,-5.572964,-6.170777,6.924800,-1.506854,-6.102556,-9.859344,-7.447653,2.438358,6.315647,-8.632272,-7.157801,5.131746,-8.156972,-7.420114,-4.296791,5.304831,8.094300,-9.837707,-4.407896,2.768249,7.088372,2.520499,0.399088,-1.499833,5.078574,-4.792582,-0.703682,3.679123,1.323925,-2.928761,-8.241619,4.949571,1.662768,-7.072378,-8.092352,-4.455325,0.955224,5.476851,-5.571604,9.684519,2.484895,-2.386624,2.899570,-4.809990,1.759343,4.693034,-5.195467,6.809865,-4.609027,3.621756,1.209964,-8.818170,-9.114043,4.966767,1.840756,-3.103361,-9.663824,-0.654289,-7.429354,7.046873,6.733681,6.165505,6.346711,9.769434,-4.003351,-9.692596,-7.155505,6.988801,-1.200283,-6.002839,0.582798,-0.918541,9.932162,-8.391519,5.131989,8.504187,-4.233438,-2.553471,2.853325,1.512732,7.138670,0.585027,-7.586203,-3.561486,8.313838,-9.377500,7.237864,0.937057,-8.694626,-7.798355,7.089579,-0.823037,3.948682,5.525443,1.710359,-8.145439,-7.549238,-5.089140,-3.784288,3.816454,4.296796,7.223852,2.302913,0.929763,-9.591179,3.240852,1.528770,7.160979,3.816658,4.876493,3.574735,4.849059,7.918869,-6.631736,-9.846723,-1.556232,6.404713,-5.312064,-7.473261,-7.017280,5.558979,-2.873034,-7.562714,2.651990,-3.390109,-7.062121,9.438532,3.916709,9.664180,-1.243366,6.185301,-2.449063,-7.908547,3.509395,-0.715250,2.933127,-5.947580,3.097354,6.617565,-2.132232,7.895705,8.840435,-1.710689,-3.544914,-7.544374,1.289535,7.999400,9.149893,-1.918387,-0.485266,-5.544267,-8.726285,9.007315,8.685774,6.682900,-9.597574,-7.650077,8.631216,-8.931948,2.090448,-4.818280,-0.321867,-3.888911,-1.686933,2.973628,0.147056,-6.707450,-3.137953,3.302466,7.985956,4.547616,-5.798745,8.289473,-2.331301,5.388285,8.877728,-4.190862,7.823468,9.961659,0.824457,-0.306574,-5.320531,-4.153755,-3.663438,6.504304,-5.935710,1.272923,-3.209648,-0.894802,-0.876827,-4.735407,-5.473642,1.934327,0.621064,9.651775,1.592891,-0.786211,-7.405003,-7.332697,-3.066939,-9.775036,-4.469370,3.848001,5.368982,8.524619,1.496943,1.081147,-3.699729,1.230856,6.646631,-8.650046,-6.313869,-8.599211,-9.465049,6.892849,-8.024362,2.423856,7.811742,-3.811174,0.749111,-0.392467,0.744676,-2.861595,3.690466,-3.985822,-7.331734,8.595322,0.464994,8.424284,3.858184,-5.134829,8.517189,-9.433305,1.916728,6.310444,3.734095,8.159238,7.312497,-1.281367,-1.529747,8.539589,-8.278907,6.169205,-7.273516,2.165658,-4.441868,-1.315942,9.082843,-1.547242,3.952810,2.218953,-9.634692,8.339524,-0.122084,-8.786282,-1.714121,7.392136,-7.481751,-1.461763,-0.137885,-2.321897,-3.000231,-6.056031,-5.829562,-1.216907,-2.585149,-2.902958,-1.871168,-4.537101,6.762118,4.995394,-5.609123,-0.590014,-2.673667,0.641530,-8.085901,5.089117,-7.422325,0.012941,-9.000119,-1.812065,0.300960,7.125865,3.677261,9.924914,-7.018918,-7.733878,8.058707,-4.354281,-7.853998,-5.960461,7.236247,5.195857,9.846079,-9.964043,-4.959881,-9.988914,7.614893,4.162909,1.431859,-7.949128,-1.301005,-9.885227,0.740715,0.559964,5.018916,5.578291,1.406723,-2.889945,6.776349,-1.375443,-5.714858,5.944632,0.489667,-0.739428,0.518034,-9.550838,7.968227,-8.582452,9.735167,-5.886614,2.476810,-3.036637,-5.961322,-6.950516,3.232290,2.143018,2.404883,-1.288962,-8.220704,-8.566128,3.770845,3.196927,7.958724,1.207700,6.462947,9.509170,7.073467,7.585233,2.391973,8.929473,-7.811719,-7.817079,-8.128121,-6.515533,7.497913,-7.776492,-6.529278,4.726733,3.324744,-9.810819,9.351268,-7.726193,9.240516,-4.975156,2.064241,-0.340634,5.053932,7.824702,0.098212,-9.944872,-4.383491,2.086822,-9.186624,1.763184,8.391886,-0.385694,3.467097,-7.883217,-2.300522,0.372323,-1.416926,1.914343,-0.540996,5.714965,1.190670,-7.374016,4.738376,-4.019215,3.044940,7.675110,8.574264,3.630566,-1.221132,-3.060275,-9.434077,-7.423674,6.012104,-2.629612,6.631863,6.128596,8.726462,-0.256576,0.583282,-3.726427,-6.376697,1.287814,5.675277,0.964116,-7.570423,-8.979990,9.143170,-1.648215,8.603198,8.765698,-3.294458,7.617200,-5.957214,-0.925046,-4.639378,-8.050330,2.544940,-2.602758,-4.252823,-6.691856,9.349835,-2.534467,-5.280148,0.907310,0.535737,-5.066864,6.188181,-2.109235,7.015714,7.368799,7.565286,2.437631,-8.200908,-4.979077,2.522757,0.908181,6.170950,0.487070,-3.750557,0.272821,2.019442,-4.738798,4.931789,2.181195,6.489970,-3.699317,-6.818793,3.372411,-2.699334,-1.234680,1.522244,-5.148551,4.553736,-1.918037,5.785048,0.806755,0.522775,9.758034,-1.579720,5.624739,-2.901228,2.667385,8.191008,9.247061,-3.810271,0.971863,0.383589,-3.558724,-3.845386,8.001891,6.589958,-6.633672,-3.691050,8.659893,-4.300385,-0.974853,6.449596,-9.729566,9.527260,-7.500339,4.218276,8.360117,5.603651,8.185705,-9.111323,7.423771,9.632234,-9.045062,-4.157630,9.640035,-2.783131,0.169362,9.899600,7.647950,8.429096,-1.347636,6.646154,3.860081,1.899455,-2.533021,7.263847,1.149607,-9.565296,-7.081200,-5.397756,2.895394,-6.319828,-5.997437,-6.442180,-3.199141,7.791879,-5.300723,-0.991562,6.647468,-3.659472,7.260627,-1.402035,4.590289,-9.187724,7.101265,2.903636,1.661475,4.405876,5.692338,0.634065,3.344152,-4.303403,-7.898668,0.553470,-7.048709,3.259398,-9.185213,4.012711,-8.150916,5.626050,-6.742719,3.790865,-7.554169,7.390569,-8.614261,0.351611,7.507905,-0.945666,-4.753010,6.285234,5.911225,-6.743411,-7.066887,2.292348,6.174332,-3.683034,8.365048,-6.223347,-8.830643,1.939196,-9.042183,-2.315991,-3.290777,0.147881,2.675773,-8.666221,-6.506055,-7.401002,-5.514454,3.013373,-9.636902,4.937431,8.335441,-4.934706,2.555516,4.126395,-5.422015,5.522874,-8.670284,-4.398308,0.390529,-5.712122,5.979628,1.671929,2.396935,-5.821838,-9.658446,4.890716,0.662214,-9.828327,-3.063586,-9.266636,0.487494,7.872706,2.994250,4.847004,-4.846621,-1.480304,-5.384688,9.482230,-8.769879,-3.735822,6.520090,8.092300,6.732499,1.819062,4.662358,-2.482727]], dtype = "float32")#candidate|6695|(2, 1092)|const|float32
call_6694 = func_2860_call(relay.reshape(const_6695.astype('float32'), [14, 12, 13]))
call_6696 = func_2860_call(relay.reshape(const_6695.astype('float32'), [14, 12, 13]))
output = relay.Tuple([call_6681,call_6685,const_6687,bop_6690,call_6694,const_6695,])
output2 = relay.Tuple([call_6682,call_6688,const_6687,bop_6690,call_6696,const_6695,])
func_6697 = relay.Function([var_6686,var_6689,], output)
mod['func_6697'] = func_6697
mod = relay.transform.InferType()(mod)
var_6698 = relay.var("var_6698", dtype = "float64", shape = (49,))#candidate|6698|(49,)|var|float64
var_6699 = relay.var("var_6699", dtype = "float64", shape = (49,))#candidate|6699|(49,)|var|float64
output = func_6697(var_6698,var_6699,)
func_6700 = relay.Function([var_6698,var_6699,], output)
mutated_mod['func_6700'] = func_6700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6702 = relay.var("var_6702", dtype = "bool", shape = (7, 12, 16))#candidate|6702|(7, 12, 16)|var|bool
const_6703 = relay.const([[[False,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True],[True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,False],[True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True],[True,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True],[False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True],[True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False],[False,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True],[False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,True],[False,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True],[True,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False],[False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True],[False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,False]],[[False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False],[True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True],[True,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False],[False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False],[False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True],[False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False],[True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True],[False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,False],[True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,True],[True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False],[True,False,False,True,False,False,False,True,False,False,False,True,False,True,True,False],[False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True]],[[False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True],[False,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True],[True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True],[False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False],[False,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False],[False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False],[False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True],[True,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True],[True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,True],[True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True],[True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False],[False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False]],[[True,False,True,False,True,False,True,False,False,False,True,False,True,False,False,True],[False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False],[True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True],[False,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False],[False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False],[True,True,False,True,False,True,True,False,True,True,True,False,False,False,False,True],[False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True],[True,True,False,True,False,False,False,True,True,True,True,True,False,False,False,False],[False,True,True,True,False,False,False,False,True,False,False,False,False,False,True,True],[True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True],[False,True,False,False,False,False,False,True,False,False,True,False,True,True,True,False],[True,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False]],[[False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,True],[True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False],[False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True],[False,False,True,True,False,False,False,True,True,False,True,True,False,True,True,False],[True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,False],[True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False],[False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True],[False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True],[False,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False],[True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,False],[False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False],[False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False]],[[False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False],[False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False],[True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,True],[True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False],[False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False],[True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True],[True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False],[False,False,True,True,True,False,False,True,False,True,True,True,False,False,False,True],[True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False],[False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True],[True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False],[False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True]],[[False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True],[False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True],[False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True],[False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False],[False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,False],[True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False],[False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True],[True,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True],[False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True],[True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,False],[True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True],[True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True]]], dtype = "bool")#candidate|6703|(7, 12, 16)|const|bool
bop_6704 = relay.logical_or(var_6702.astype('bool'), relay.reshape(const_6703.astype('bool'), relay.shape_of(var_6702))) # shape=(7, 12, 16)
output = relay.Tuple([bop_6704,])
output2 = relay.Tuple([bop_6704,])
func_6710 = relay.Function([var_6702,], output)
mod['func_6710'] = func_6710
mod = relay.transform.InferType()(mod)
mutated_mod['func_6710'] = func_6710
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6711 = relay.var("var_6711", dtype = "bool", shape = (7, 12, 16))#candidate|6711|(7, 12, 16)|var|bool
func_6710_call = mutated_mod.get_global_var('func_6710')
call_6712 = func_6710_call(var_6711)
output = call_6712
func_6713 = relay.Function([var_6711], output)
mutated_mod['func_6713'] = func_6713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_290_call = mod.get_global_var('func_290')
func_291_call = mutated_mod.get_global_var('func_291')
call_6732 = relay.TupleGetItem(func_290_call(), 0)
call_6733 = relay.TupleGetItem(func_291_call(), 0)
output = call_6732
output2 = call_6733
func_6737 = relay.Function([], output)
mod['func_6737'] = func_6737
mod = relay.transform.InferType()(mod)
mutated_mod['func_6737'] = func_6737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6737_call = mutated_mod.get_global_var('func_6737')
call_6738 = func_6737_call()
output = call_6738
func_6739 = relay.Function([], output)
mutated_mod['func_6739'] = func_6739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_245_call = mod.get_global_var('func_245')
func_246_call = mutated_mod.get_global_var('func_246')
call_6819 = relay.TupleGetItem(func_245_call(), 2)
call_6820 = relay.TupleGetItem(func_246_call(), 2)
func_2379_call = mod.get_global_var('func_2379')
func_2380_call = mutated_mod.get_global_var('func_2380')
call_6824 = relay.TupleGetItem(func_2379_call(), 0)
call_6825 = relay.TupleGetItem(func_2380_call(), 0)
func_5148_call = mod.get_global_var('func_5148')
func_5151_call = mutated_mod.get_global_var('func_5151')
const_6832 = relay.const([6.790063,-5.531431,1.711453,-3.904865,2.899659,-6.317732,-6.048706,4.569606,6.777167,-0.593436,3.373113,8.768102,-8.888269,-9.627654,-8.973074,-6.748641,3.407582,7.053727,-8.150303,-4.295164,-0.804572,-1.037243,3.173474,0.489166,9.713429,-4.323559,8.868654,8.236428,-6.531313,9.620084,-9.340873,-0.315174,-9.040032,-8.337886,-7.330315,0.172233,9.664348,4.448219,9.268405,8.531886,-4.898082,1.031965,5.772658,3.421657,-5.808571,6.705623,0.441360,-1.219019,9.048521,-3.253691,-3.662174,-8.012925,1.526291,-9.817832,-8.681391,1.314893,1.061885,-1.236537,4.522272,-6.702721,4.545635,1.508009,2.890993,-5.978034,-0.845411,-6.518061,-8.804934,0.809364,-4.828238,-8.563493,2.601856,2.038850,-9.471345,-8.595969,-1.647513,-9.663076,-7.381534,-5.253550,6.366454,-0.276355,1.621906,-5.875821,8.290995,-8.164942,1.554307,5.824221,-3.278503,8.109490,-4.364331,6.084200,-1.178156,-0.467903,7.742701,6.457485,-1.292287,-9.074132,-4.211059,5.525662,-5.938273,-2.155777,9.145740,9.852005,-8.970825,-9.178087,-9.398182,2.086607,3.901349,2.048864,-8.193141,-2.126117,-9.254077,9.645832,8.157363,-0.358030,-8.811836,-1.234116,-6.156109,2.567441,-5.234487,-3.608887,7.139416,-1.403883,6.300081,9.728260,-0.363645,-1.414383,6.391791,7.405963,0.576680,-1.171000,-1.101740,1.182043,-2.343134,-7.887757,-5.397701,6.108368,-8.232753,7.822783,7.454481,-9.947409,-9.576105,-0.016484,-7.400132,-5.287881,-1.587843,3.728492,2.251925,4.751281,0.518428,9.739853,-1.163960,-5.149554,-1.069687,8.333182,-1.425338,8.664450,-5.663980,-3.894811,6.052510,-4.269360,-1.242398,7.214513,-0.118407,7.615395,-9.678435,-1.870331,-3.420024,8.261979,-9.103964,-8.607706,-4.700206,9.948407,-0.102008,9.882417,-2.482776,8.282365,8.199770,2.155039,2.273386,-2.968276,9.027260,9.304006,8.291518,-9.640226,4.451349,-0.203129,-9.481231,-9.950064,-6.468958,-9.517828,-7.182053,2.379624,-2.399556,2.133119,3.930347,2.087300,-1.414226,-9.401442,-5.187108,3.926487,-8.102619,4.874297,2.650240,0.078300,-1.141487,1.381457,3.082303,-3.512940,9.333062,4.594006,9.444856,1.847572,7.433255,4.055149,-3.186329,9.242951,7.483907,2.824103,0.462919,-6.543723,-7.744297,-9.945609,-6.011103,-9.137663,-8.861557,-4.422433,-4.361300,-3.415462,-4.517750,3.201372,-6.428138,6.991748,-6.827493,1.388004,5.896980,0.371765,2.375385,3.549760,-7.392296,5.599315,9.992232,4.985883,6.360330,-1.264386,4.469022,-3.263128,-7.282004,0.536205,-7.149793,-2.846944,-5.132290,1.077987,1.610561,3.443606,-1.774437,2.799872,1.032554,-8.528239,-9.189538,-4.941415,-2.183012,7.740899,-4.358140,7.669174,2.914434,-8.519007,6.387746,8.982478,-8.781095,5.848937,2.456726,-9.270489,4.801835,5.658402,6.440251,7.443317,-0.583830,5.541994,-4.296394,3.069209,-6.542864,3.434788,-3.509338,5.257348,-7.604918,3.921623,7.584211,-3.150644,-6.152140,-4.609292,5.458439,-6.711771,-7.614241,-8.249906,-7.353716,5.559029,1.358642,1.174773,8.916836,-2.492107,8.597048,-4.551669,3.492468,0.561879,-7.608487,-6.637800,9.843714,-8.531841,-7.884449,-1.068618,-7.598135,2.657140,5.809113,8.620042,1.595521,-9.727397,-2.562841,1.299046,0.184804,6.403532,-0.483611,4.746969,-8.829736,-8.720785,-9.793775,-4.139281,-5.736539,-2.473066,-6.289712,-8.458079,6.002050,-5.072334,3.136951,3.515838,-0.295095,3.292642], dtype = "float32")#candidate|6832|(336,)|const|float32
call_6831 = relay.TupleGetItem(func_5148_call(relay.reshape(const_6832.astype('float32'), [6, 14, 4])), 0)
call_6833 = relay.TupleGetItem(func_5151_call(relay.reshape(const_6832.astype('float32'), [6, 14, 4])), 0)
var_6856 = relay.var("var_6856", dtype = "float32", shape = (6, 14, 4))#candidate|6856|(6, 14, 4)|var|float32
bop_6857 = relay.less(call_6831.astype('bool'), relay.reshape(var_6856.astype('bool'), relay.shape_of(call_6831))) # shape=(6, 14, 4)
bop_6860 = relay.less(call_6833.astype('bool'), relay.reshape(var_6856.astype('bool'), relay.shape_of(call_6833))) # shape=(6, 14, 4)
func_5723_call = mod.get_global_var('func_5723')
func_5725_call = mutated_mod.get_global_var('func_5725')
call_6861 = func_5723_call()
call_6862 = func_5723_call()
output = relay.Tuple([call_6819,call_6824,const_6832,bop_6857,call_6861,])
output2 = relay.Tuple([call_6820,call_6825,const_6832,bop_6860,call_6862,])
func_6870 = relay.Function([var_6856,], output)
mod['func_6870'] = func_6870
mod = relay.transform.InferType()(mod)
var_6871 = relay.var("var_6871", dtype = "float32", shape = (6, 14, 4))#candidate|6871|(6, 14, 4)|var|float32
output = func_6870(var_6871)
func_6872 = relay.Function([var_6871], output)
mutated_mod['func_6872'] = func_6872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1929_call = mod.get_global_var('func_1929')
func_1931_call = mutated_mod.get_global_var('func_1931')
call_6880 = relay.TupleGetItem(func_1929_call(), 0)
call_6881 = relay.TupleGetItem(func_1931_call(), 0)
var_6917 = relay.var("var_6917", dtype = "float32", shape = (15, 2, 2))#candidate|6917|(15, 2, 2)|var|float32
bop_6918 = relay.subtract(call_6880.astype('float64'), var_6917.astype('float64')) # shape=(15, 2, 2)
bop_6921 = relay.subtract(call_6881.astype('float64'), var_6917.astype('float64')) # shape=(15, 2, 2)
func_1661_call = mod.get_global_var('func_1661')
func_1663_call = mutated_mod.get_global_var('func_1663')
call_6926 = relay.TupleGetItem(func_1661_call(), 1)
call_6927 = relay.TupleGetItem(func_1663_call(), 1)
func_6048_call = mod.get_global_var('func_6048')
func_6051_call = mutated_mod.get_global_var('func_6051')
var_6929 = relay.var("var_6929", dtype = "float32", shape = (56,))#candidate|6929|(56,)|var|float32
var_6930 = relay.var("var_6930", dtype = "int8", shape = (216,))#candidate|6930|(216,)|var|int8
call_6928 = relay.TupleGetItem(func_6048_call(relay.reshape(var_6929.astype('float32'), [14, 2, 2]), relay.reshape(var_6930.astype('int8'), [216,]), ), 2)
call_6931 = relay.TupleGetItem(func_6051_call(relay.reshape(var_6929.astype('float32'), [14, 2, 2]), relay.reshape(var_6930.astype('int8'), [216,]), ), 2)
bop_6934 = relay.floor_mod(var_6917.astype('float32'), call_6880.astype('float32')) # shape=(15, 2, 2)
bop_6937 = relay.floor_mod(var_6917.astype('float32'), call_6881.astype('float32')) # shape=(15, 2, 2)
output = relay.Tuple([bop_6918,call_6926,call_6928,var_6929,var_6930,bop_6934,])
output2 = relay.Tuple([bop_6921,call_6927,call_6931,var_6929,var_6930,bop_6937,])
func_6972 = relay.Function([var_6917,var_6929,var_6930,], output)
mod['func_6972'] = func_6972
mod = relay.transform.InferType()(mod)
mutated_mod['func_6972'] = func_6972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6972_call = mutated_mod.get_global_var('func_6972')
var_6974 = relay.var("var_6974", dtype = "float32", shape = (15, 2, 2))#candidate|6974|(15, 2, 2)|var|float32
var_6975 = relay.var("var_6975", dtype = "float32", shape = (56,))#candidate|6975|(56,)|var|float32
var_6976 = relay.var("var_6976", dtype = "int8", shape = (216,))#candidate|6976|(216,)|var|int8
call_6973 = func_6972_call(var_6974,var_6975,var_6976,)
output = call_6973
func_6977 = relay.Function([var_6974,var_6975,var_6976,], output)
mutated_mod['func_6977'] = func_6977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6457_call = mod.get_global_var('func_6457')
func_6458_call = mutated_mod.get_global_var('func_6458')
call_6991 = func_6457_call()
call_6992 = func_6457_call()
func_5354_call = mod.get_global_var('func_5354')
func_5359_call = mutated_mod.get_global_var('func_5359')
var_7002 = relay.var("var_7002", dtype = "uint32", shape = (168,))#candidate|7002|(168,)|var|uint32
const_7003 = relay.const([7.051509,6.540669,-1.753437,6.288719,-8.308948,-6.012158,-8.025837,4.823139,1.426272,3.008290,1.951101,2.511264,-5.619168,-3.630305,-7.092087,8.315945,-5.221546,-5.778723,-6.477288,4.767780,-1.135114,-1.100349,7.320912,4.660336,9.046752,5.958273,-0.480277,-3.688184], dtype = "float64")#candidate|7003|(28,)|const|float64
var_7004 = relay.var("var_7004", dtype = "float32", shape = (44,))#candidate|7004|(44,)|var|float32
call_7001 = relay.TupleGetItem(func_5354_call(relay.reshape(var_7002.astype('uint32'), [168,]), relay.reshape(const_7003.astype('float64'), [28,]), relay.reshape(var_7004.astype('float32'), [22, 2]), ), 1)
call_7005 = relay.TupleGetItem(func_5359_call(relay.reshape(var_7002.astype('uint32'), [168,]), relay.reshape(const_7003.astype('float64'), [28,]), relay.reshape(var_7004.astype('float32'), [22, 2]), ), 1)
var_7026 = relay.var("var_7026", dtype = "uint32", shape = (168,))#candidate|7026|(168,)|var|uint32
bop_7027 = relay.less(var_7002.astype('bool'), relay.reshape(var_7026.astype('bool'), relay.shape_of(var_7002))) # shape=(168,)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
const_7040 = relay.const([1.557645,-0.565963,5.859988,-9.128600,1.300636,5.091231,9.098733,3.573397,2.104641,-0.881760,0.919233,-6.856367,-8.029221,3.339731,6.285149,0.754812,5.388605,4.371362,-0.255764,-2.179886,-4.894328,9.572813,-0.272388,-8.685855,-7.252528,-6.089325,-4.276479,-7.868254,7.055058,-2.445987,-3.643181,9.551712,9.538859,-4.473012,2.593895,6.753076,4.309938,4.470652,-8.685744,1.010076,-8.925508,-3.089796,1.584874,2.417437,-9.130540,0.124252,-1.350210,-3.060624,-8.696857,9.998316,3.475139,0.995045,-2.257038,0.910819,-6.832617,3.883171,-4.277354,3.788900,-6.002120,-4.898098,6.260895,7.782227,4.024649,2.504530,7.679983,6.051991,-6.791496,5.457436,9.634216,0.227995,4.880223,-8.836544,-4.951483,0.414658,6.572160,6.167544,-9.810137,-4.457868,-5.185732,6.596980,-1.034188,-3.525170,2.754270,1.933185,-8.751927,-9.633799,-4.219228,-8.338784,7.696044,5.427086,7.674122,7.696900,-5.939342,8.220692,0.867304,-9.408551,5.118459,-8.256735,-7.760427,6.456346,-9.291982,-1.234642,4.925160,1.024967,1.445907,9.706073,7.355731,-5.732721,-5.574511,-6.324313,-8.397981,8.994344,-8.781637,-8.345655,-0.622262,1.781926,0.324021,3.283842,-4.669127,4.815587,3.472371,3.752249,1.375732,-5.713296,2.135587,-2.487076,5.888952,-4.601339,4.329275,-9.271589,-4.216733,8.420304,-1.768268,-3.667546,7.665035,-8.042899,-8.673615,-1.026948,5.581772,2.296368,2.349174,-3.184387,-0.809631,-3.927784,8.243899,2.488854,4.537615,7.439513,5.690719,-8.408364,-1.846207,6.778541,-8.815791,-8.433198,7.675819,9.407166,2.883642,6.263202,-2.635218,-0.494258,4.695178,7.046485,-8.844543,-6.748387,0.258617,-6.024091,4.225722,-2.259991,6.746390,1.850771,8.638684,-6.747278,-8.848306,-9.524712,5.945749,-7.087049,-6.156592,5.431514,-9.788516,-4.189307,2.655887,7.967465,-0.900908,-8.716426,4.916302,-5.399436,-4.734709,3.448090,4.087697,4.699561,-8.300188,1.604387,-5.537185,4.163552,-7.713069,-5.108071,7.491981,-5.780559,3.272743,5.984888,-6.508410,3.027411,-6.458016,5.207219,-9.650287,4.033827,-1.639473,1.605275,5.099265,7.122507,-0.221718,9.062116,-2.451872,-8.802694,9.750943,-6.022715,8.634233,-0.602822,-5.473492,7.510349,1.446351,-7.337954,7.709909,-4.662856,-0.078046,-4.383389,6.426185,-8.002709,0.117036,9.666528,2.702882,-6.758466,-7.588916,-3.741764,-1.194903,0.989541,-4.320491,9.885780,-3.305707,7.782418,-0.805715,2.834375,4.318123,6.225641,-6.837091,5.123579,-9.366207,3.215161,1.701633,7.867769,9.549385,1.352353,-4.230998,-5.169981,-5.060925,-3.123543,0.305081,-1.387017,7.015793,-1.393765,-4.245313,6.843519,8.557788,3.374357,4.265090,6.748205,-3.549491,-1.744059,3.600517,8.664763,-2.048742,-4.894113,6.889635,2.589979,-3.010655,2.777841,8.404693,8.379595,1.945965,9.064470,-5.516987,9.882918,1.614322,5.793827,-3.675967,-4.694119,-1.404052,8.748375,5.119937,4.173289,-8.750336,8.949379,6.804110,-4.367284,0.658635,6.631569,-0.031816,-3.794810,9.949263,3.446273,-2.727320,-2.152270,-5.284414,4.731276,-3.445752,-9.091812,8.305871,9.031980,-6.796987,0.576589,9.026410,5.141126,0.896556,-3.133128,-6.128073,8.485258,0.381843,4.775220,2.932778,-0.237841,2.428983,-1.904279,-0.437106,-5.735307,7.561369,-7.337008,-3.233786,0.497460,-0.329772,-1.575370,6.282504,7.055536,-5.835923,-6.379423,7.661419,9.959254,7.751795,2.181504,9.770613,8.419663,4.817961,-0.060513,6.680923,-1.834736,5.516581,-7.308918,-4.415122,7.022270,2.694284,-5.636316,-0.704335,8.114775,8.875555,7.676339,-8.310258,8.861199,1.054672,-4.069372,4.351920,-2.269238,1.287989,0.404045,-2.745580,-4.853231,7.509920,5.433057,3.688433,2.149295,7.547002,5.623297,6.820976,-5.192077,-4.211193,-4.024892,3.173828,-1.303458,6.799192,-5.063267,8.818101,2.717303,4.700145,-7.347851,-4.807536,3.140592,2.195874,3.634383,8.795663,9.941414,-8.925733,-7.510196,-5.658590,2.757782,-8.626602,1.162075,-8.313086,-2.088125,9.196918,-7.086841,3.321164,-3.710402,7.930815,3.036119,1.838556,-7.557708,-0.384910,1.044846,-2.066428,8.238395,-1.187870,-1.079578,2.963745,-5.799148,3.207344,-1.763342,-6.382200,4.321854,8.638381,-1.836958,2.386015,-1.341154,3.754247,-3.680642,-4.004247,2.040062,5.460864,-5.792167,-5.207199,6.994729,9.096178,-3.603962,-5.775623,8.868883,8.079890,-9.903732,1.273658,-9.951159,-0.893061,-3.145468,-6.380271,8.121249,9.284651,4.867490,-0.287345,6.043957,-8.233033,3.688637,-7.326469,-8.560446,2.646886,-2.687272,-6.568733,0.489951,-8.047582,5.647337,2.652920,-1.461702,-0.586179,7.237097,-4.363025,3.623345,-9.431458,-0.717286,5.594389,-7.738922,7.417855,5.398407,-5.465594,2.692871,-9.196412,8.431307,1.665889,-9.387334,2.131124,5.845433,0.801535,8.321901,7.221897,-6.217851,-4.198976,5.409981,0.180999,2.201486,-7.247418,-3.471009,-9.846345,-5.144564,8.028845,0.534205,-4.760524,9.786492,0.805079,-4.294358,-4.271948,-7.981796,7.333190,-8.043518,-2.573261,-3.609881,-8.968698,-9.001675,4.363723,7.223983,7.307356,3.398760,5.418492,0.587929,7.404460,8.788556,-7.312965,7.504915,-1.141123,1.451352,6.891092,5.962461,-8.355225,-6.126085,-0.864096,6.964357,5.959671,-1.120829,6.108659,7.583045,9.236834,-5.104909,-2.695566,2.262302,1.381751,-9.908830,2.724539,3.956068,2.165666,2.010189,2.639764,6.709408,9.977858,8.437474,-8.965236,-8.522340,5.847741,8.217033,-1.651025,-3.443654,4.559238,-2.088896,-3.019172,6.263230,-1.099535,-7.674679,6.152883,-3.039452,5.493347,8.082341,-7.710804,2.578938,-5.625753,-3.861297,1.828024,-9.792454,7.001486,7.212413,-8.281457,7.344268,6.078853,-3.874180,8.914459,-3.945062,-3.661115,-3.016231,0.867014,3.510645,1.512946,-8.069293,-9.950902,1.221914,8.330739,-1.898503,4.498376,-5.869335,4.686241,9.559513,7.252207,5.957223,5.754118,5.421316,6.523031,-1.704057,-2.072514,7.234443,-0.757415,-4.257138,-0.916279,5.713586,-1.557045,-9.652669,1.204154,-4.228445,9.878073,-5.133926,-9.702776,8.973518,-4.280026,-4.623148,-8.895276,-9.477524,-7.080496,8.996531,1.607798,6.202071,-6.918786,5.526780,2.214606,9.485926,4.755098,-9.842441,6.539436,3.555600,7.092184,-4.138845,6.073170,-0.258595,3.000248,-3.704151,3.812808,-6.949071,-6.806733,5.966237,1.543980,-7.169882,-0.274357,-0.068319,9.018923,-5.509900,9.274752,-2.239643,0.815950,3.681464,-3.634368,7.752491,5.868559,-4.336567,6.118807,3.172654,-9.272381,5.965261,-5.601254,-4.503787,8.753758,5.185771,2.326617,5.978579,-0.823806,7.262926,4.912715,-3.011597,-0.625572,-0.352270,-8.953839,-7.769217,7.273105,-1.281054,-2.421544,1.546685,7.618846,-5.374749,7.325203,3.167976,-3.988951,-1.223156,1.244134,-2.928625,5.282817,4.599216,9.891568,-1.364274,6.143519,-8.679269,4.672157,9.395970,-4.366637,0.139661,4.286396,-2.893153,4.205838,2.043186,8.426018,-4.183202,-9.098133,5.790766,-6.594426,6.817550,-7.916911,7.025705,6.736577,-9.119253,-5.484834,7.961854,-3.843569,-5.176486,8.819375,-9.455508,6.113905,7.490045,-9.595067,9.298711,7.974816,-0.242039,5.980316,4.974291,-4.774538,-7.158070,-9.084650,-1.322161,8.960620,-1.129940,7.911058,-0.556307,-8.518948,-4.403541,-7.104880,0.981887,-2.686402,2.834879,7.403690,7.182784,-2.460631,-3.521561,7.103849,1.556488,5.652956,1.022153,-2.433041,-0.938924,-5.136333,2.359747,-5.678018,-8.899973,-7.290838,-1.453026,-9.042142,1.075590,-8.817269,4.178915,-5.299439,-6.033497,8.523640,-6.096464,9.318809,-8.077699,-1.447186,-8.047941,-5.690402,2.190715,-7.596760,-9.160429,2.728418,1.574922,1.299718,-9.552695,2.786822,-6.677236,-9.612256,-7.943336,4.200133,5.516772,-0.360979,-0.079395,-2.339506,0.944932,-3.569585,-2.553255,7.528443,7.776077,-1.419768,2.486937,-6.115616,-8.107613,-2.446184,7.569599,7.622206,2.990044,-7.157165,-1.283116,-3.632522,-1.229208,6.847838,-3.009153,-6.533949,-1.141569,1.447085,5.002288,9.227002,5.901837,-3.101869,3.872718,7.075000,-0.442528,-7.436611,2.068404,-4.111562,9.921599,-8.066019,8.285193,0.988279,3.526789,8.896434,3.271389,1.865778,-3.973757,0.744981,4.551150,4.380303,-0.772735,1.858200,-7.394616,8.574968,2.914577,9.765133,0.586900,-1.193516,-2.682966,9.546456,-7.077615,-8.630865,-4.210926,-0.196264,-2.958299,5.552674,-4.871888,-8.440222,8.819728,-8.913791,5.186355,6.688441,4.927749,-8.813539,7.261050,5.890114,-9.411808,-1.861850,1.301195], dtype = "float64")#candidate|7040|(840,)|const|float64
call_7039 = func_3534_call(relay.reshape(const_7040.astype('float64'), [12, 5, 14]))
call_7041 = func_3534_call(relay.reshape(const_7040.astype('float64'), [12, 5, 14]))
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
call_7044 = relay.TupleGetItem(func_475_call(), 0)
call_7045 = relay.TupleGetItem(func_477_call(), 0)
output = relay.Tuple([call_6991,call_7001,const_7003,var_7004,bop_7027,call_7039,const_7040,call_7044,])
output2 = relay.Tuple([call_6992,call_7005,const_7003,var_7004,bop_7027,call_7041,const_7040,call_7045,])
func_7080 = relay.Function([var_7002,var_7004,var_7026,], output)
mod['func_7080'] = func_7080
mod = relay.transform.InferType()(mod)
mutated_mod['func_7080'] = func_7080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7080_call = mutated_mod.get_global_var('func_7080')
var_7082 = relay.var("var_7082", dtype = "uint32", shape = (168,))#candidate|7082|(168,)|var|uint32
var_7083 = relay.var("var_7083", dtype = "float32", shape = (44,))#candidate|7083|(44,)|var|float32
var_7084 = relay.var("var_7084", dtype = "uint32", shape = (168,))#candidate|7084|(168,)|var|uint32
call_7081 = func_7080_call(var_7082,var_7083,var_7084,)
output = call_7081
func_7085 = relay.Function([var_7082,var_7083,var_7084,], output)
mutated_mod['func_7085'] = func_7085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4373_call = mod.get_global_var('func_4373')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_7103 = func_4373_call()
call_7104 = func_4373_call()
var_7114 = relay.var("var_7114", dtype = "float32", shape = (11, 2, 2))#candidate|7114|(11, 2, 2)|var|float32
bop_7115 = relay.greater(call_7103.astype('bool'), var_7114.astype('bool')) # shape=(11, 2, 2)
bop_7118 = relay.greater(call_7104.astype('bool'), var_7114.astype('bool')) # shape=(11, 2, 2)
output = relay.Tuple([bop_7115,])
output2 = relay.Tuple([bop_7118,])
func_7120 = relay.Function([var_7114,], output)
mod['func_7120'] = func_7120
mod = relay.transform.InferType()(mod)
var_7121 = relay.var("var_7121", dtype = "float32", shape = (11, 2, 2))#candidate|7121|(11, 2, 2)|var|float32
output = func_7120(var_7121)
func_7122 = relay.Function([var_7121], output)
mutated_mod['func_7122'] = func_7122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_643_call = mod.get_global_var('func_643')
func_645_call = mutated_mod.get_global_var('func_645')
call_7143 = relay.TupleGetItem(func_643_call(), 0)
call_7144 = relay.TupleGetItem(func_645_call(), 0)
output = call_7143
output2 = call_7144
func_7168 = relay.Function([], output)
mod['func_7168'] = func_7168
mod = relay.transform.InferType()(mod)
mutated_mod['func_7168'] = func_7168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7168_call = mutated_mod.get_global_var('func_7168')
call_7169 = func_7168_call()
output = call_7169
func_7170 = relay.Function([], output)
mutated_mod['func_7170'] = func_7170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5854_call = mod.get_global_var('func_5854')
func_5856_call = mutated_mod.get_global_var('func_5856')
call_7178 = relay.TupleGetItem(func_5854_call(), 3)
call_7179 = relay.TupleGetItem(func_5856_call(), 3)
output = relay.Tuple([call_7178,])
output2 = relay.Tuple([call_7179,])
func_7206 = relay.Function([], output)
mod['func_7206'] = func_7206
mod = relay.transform.InferType()(mod)
output = func_7206()
func_7207 = relay.Function([], output)
mutated_mod['func_7207'] = func_7207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4319_call = mod.get_global_var('func_4319')
func_4320_call = mutated_mod.get_global_var('func_4320')
call_7252 = func_4319_call()
call_7253 = func_4319_call()
func_210_call = mod.get_global_var('func_210')
func_212_call = mutated_mod.get_global_var('func_212')
call_7274 = func_210_call()
call_7275 = func_210_call()
func_5615_call = mod.get_global_var('func_5615')
func_5619_call = mutated_mod.get_global_var('func_5619')
const_7280 = relay.const([-8,5,-5,5,-6,4,8,-4,6,9,-9,-4,2,10,-6,7,3,-6,-7,-4,7,-8,1,-3,4,-1,-3,-6,6,-6,-5,8,5,8,7,6,2,-9,8,10,-6,-6,5,-3,-8,-5,9,2,-5,9,-2,6,-9,-7,-10,10,9,4,-8,6,3,-2,5,10,2,-4,2,-10,-6,1,-3,4,7,-9,3,2,7,10,-7,3,-10,6,6,5,3,10,7,10,-1,8,6,-2,5,6,4,1,-6,-6,-5,6,8,-3,-9,-8,4,4,9,5,-10,6,-10,-6,6,-7,-2,8,-9,5,-6,10,-3,1,10,4,7,-4,8,1,1,-4,3,4,-5,-1,4,-2,-6,6,9,8,1,10,1,3,1,4,1,5,-9,-6,6,9,-1,9,-9,5,-6,-1,-8,8,4,-3,-10,-3,-3,-3,9,2,-8,-9,6,9,8,-1,-4,6,-1,-5,5,1,6,-10,5,-6,-3,-2,-8,-2,-10,-3,-2,-2,-7,-3,2,-2,-7,7,4,-8,8,-7,2,-5,2,7,-6,-6,-6,5,2,-10,2,2,-9,-5,10,-5,3,5,5,-9,10,6], dtype = "uint64")#candidate|7280|(224,)|const|uint64
call_7279 = relay.TupleGetItem(func_5615_call(relay.reshape(const_7280.astype('uint64'), [7, 2, 16]), relay.reshape(const_7280.astype('uint64'), [7, 2, 16]), ), 0)
call_7281 = relay.TupleGetItem(func_5619_call(relay.reshape(const_7280.astype('uint64'), [7, 2, 16]), relay.reshape(const_7280.astype('uint64'), [7, 2, 16]), ), 0)
func_547_call = mod.get_global_var('func_547')
func_548_call = mutated_mod.get_global_var('func_548')
call_7294 = relay.TupleGetItem(func_547_call(), 0)
call_7295 = relay.TupleGetItem(func_548_call(), 0)
output = relay.Tuple([call_7252,call_7274,call_7279,const_7280,call_7294,])
output2 = relay.Tuple([call_7253,call_7275,call_7281,const_7280,call_7295,])
func_7306 = relay.Function([], output)
mod['func_7306'] = func_7306
mod = relay.transform.InferType()(mod)
output = func_7306()
func_7307 = relay.Function([], output)
mutated_mod['func_7307'] = func_7307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5530_call = mod.get_global_var('func_5530')
func_5532_call = mutated_mod.get_global_var('func_5532')
call_7308 = relay.TupleGetItem(func_5530_call(), 0)
call_7309 = relay.TupleGetItem(func_5532_call(), 0)
func_1708_call = mod.get_global_var('func_1708')
func_1710_call = mutated_mod.get_global_var('func_1710')
var_7314 = relay.var("var_7314", dtype = "float32", shape = (1050,))#candidate|7314|(1050,)|var|float32
call_7313 = relay.TupleGetItem(func_1708_call(relay.reshape(var_7314.astype('float32'), [15, 7, 10])), 0)
call_7315 = relay.TupleGetItem(func_1710_call(relay.reshape(var_7314.astype('float32'), [15, 7, 10])), 0)
func_6131_call = mod.get_global_var('func_6131')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_7326 = func_6131_call()
call_7327 = func_6131_call()
bop_7345 = relay.equal(var_7314.astype('bool'), relay.reshape(call_7313.astype('bool'), relay.shape_of(var_7314))) # shape=(1050,)
bop_7348 = relay.equal(var_7314.astype('bool'), relay.reshape(call_7315.astype('bool'), relay.shape_of(var_7314))) # shape=(1050,)
func_5597_call = mod.get_global_var('func_5597')
func_5600_call = mutated_mod.get_global_var('func_5600')
const_7350 = relay.const(-1, dtype = "uint64")#candidate|7350|()|const|uint64
var_7351 = relay.var("var_7351", dtype = "uint64", shape = (182,))#candidate|7351|(182,)|var|uint64
call_7349 = relay.TupleGetItem(func_5597_call(relay.reshape(const_7350.astype('uint64'), []), relay.reshape(var_7351.astype('uint64'), [13, 1, 14]), ), 1)
call_7352 = relay.TupleGetItem(func_5600_call(relay.reshape(const_7350.astype('uint64'), []), relay.reshape(var_7351.astype('uint64'), [13, 1, 14]), ), 1)
func_4064_call = mod.get_global_var('func_4064')
func_4068_call = mutated_mod.get_global_var('func_4068')
const_7357 = relay.const([-7,-7,-3,4,3,-9,-10,7,8,-7,-1,-3,10,1,-4,10,-9,10,9,7,-2,10,-1,-8,-6,-1,-8,3,2,1,-4,-5,-9,6,9,-9,-2,-2,7,-6,-7,-9,1,-4,-6,7,4,-5,-9,1,6,8,3,5,-10,-5,7,-3,-6,1,9,-1,2,-8,-9,-10,2,-5,7,-5,2,-3,5,-7,-2,2,6,4,1,10,2,-7,7,-9,3,-3,-5,-3,-2,-9,7,-6,7,3,-2,10,-5,6,10,-8,9,-7,8,5,10,-6,7,2,-2,4,9,7,2,10,1,4,-1,-6,-2,-3,-7,1,-3,-10,9,-10,-1,-6,2,-4,4,-5,-10,4,-4,-6,5,6,10,4,1,2,1,-4,2,8,-5,-2,7,-9,-2,3,2,-7,5,-4,3,10,-3,-9,-4,2,-3,6,-10,-3,10,2,-5,-4,10,9,-3,-9,5,1,8,-9,-8,3,8,10,1,-9,3,-5,3,-6,4,5,5,7,1,-6,-8,7,-2,5,-1,10,-10,-6,-10,1,10,-1,4,-10,-3,4,-3,9,-9,1,-3,-5,7,-7,-4,10,8,8,-1,-7,-5,8,-1,5,5,4,-8,-2,10,9,10,9,3,10,-8,-10,7,10,7,9,-1,10,10,4,1,-8,-5,9,-4,1,5,4,-9,9,10,-8,1,-10,-7,-2,8,-9,7,-10,-8,-5,-2,4,-3,-9,-3,2,4,6,8,8,-8,-8,7,-7,9,-6,1,4,5,5,-10,-1,-2,-4,6,6,-10,-10,2,-2,1,2,9,6,-7,3,1,-2,2,-3,9,-2,-4,8,2,-7,-9,3,-4,6,-1,1,-5,-4,8,-5,7,-5,-10,8,-2,-4,-5,1,-7,3,5,9,6,7,9,10,-1,-8,8,2,-1,5,3,-3,2,-8,9,-7,1,8,5,-7,-3,-9,10,-4,-10,-5,4,5,6,-3,3,2,3,5,10,-6,8,5,-7,-7,10,9,-1,-2,-8,-2,4,-6,-5,-6,-6,7,10,-1,5,-3,1,-10,8,9,-6,8,6,6,-6,6,7,-5,-7,3,4,8,-9,8,-10,-3,10,4,-5,7,5,5,-7,8,-5,-8,6,-6,2,-2,1,-9,-7,6,3,5,-7,1,-1,9,-9,-6,-1,-10,8,-7,7,9,9,8,-9,2,-3,9,2,-1,5,6,2,2,9,-9,5,10,3,8,1,5,4,2,-2,-7,-2,2,10,-4,-3,-7,10,4,7,3,-3,4,4,1,8,-2,10,6,10,-1,2,-3,5,-6,-1,-10,9,2,-1,9,1,-4,7,-3,8,2,-3,-4,6,1,-9,2,9,1,-6,-3,-2,-2,-5,-8,10,-6,-8,-1,8,-2,7,3,9,-7,-4,4,7,7,-10,6,-6,2,3,-8], dtype = "int32")#candidate|7357|(540,)|const|int32
call_7356 = func_4064_call(relay.reshape(const_7357.astype('int32'), [12, 5, 9]), relay.reshape(const_7357.astype('int32'), [12, 5, 9]), )
call_7358 = func_4064_call(relay.reshape(const_7357.astype('int32'), [12, 5, 9]), relay.reshape(const_7357.astype('int32'), [12, 5, 9]), )
bop_7373 = relay.floor_mod(call_7326.astype('float32'), const_7350.astype('float32')) # shape=(1, 2, 2)
bop_7376 = relay.floor_mod(call_7327.astype('float32'), const_7350.astype('float32')) # shape=(1, 2, 2)
func_4783_call = mod.get_global_var('func_4783')
func_4784_call = mutated_mod.get_global_var('func_4784')
call_7380 = relay.TupleGetItem(func_4783_call(), 0)
call_7381 = relay.TupleGetItem(func_4784_call(), 0)
output = relay.Tuple([call_7308,bop_7345,call_7349,var_7351,call_7356,const_7357,bop_7373,call_7380,])
output2 = relay.Tuple([call_7309,bop_7348,call_7352,var_7351,call_7358,const_7357,bop_7376,call_7381,])
func_7385 = relay.Function([var_7314,var_7351,], output)
mod['func_7385'] = func_7385
mod = relay.transform.InferType()(mod)
mutated_mod['func_7385'] = func_7385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7385_call = mutated_mod.get_global_var('func_7385')
var_7387 = relay.var("var_7387", dtype = "float32", shape = (1050,))#candidate|7387|(1050,)|var|float32
var_7388 = relay.var("var_7388", dtype = "uint64", shape = (182,))#candidate|7388|(182,)|var|uint64
call_7386 = func_7385_call(var_7387,var_7388,)
output = call_7386
func_7389 = relay.Function([var_7387,var_7388,], output)
mutated_mod['func_7389'] = func_7389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mod.get_global_var('func_4783')
func_4784_call = mutated_mod.get_global_var('func_4784')
call_7391 = relay.TupleGetItem(func_4783_call(), 0)
call_7392 = relay.TupleGetItem(func_4784_call(), 0)
func_1661_call = mod.get_global_var('func_1661')
func_1663_call = mutated_mod.get_global_var('func_1663')
call_7403 = relay.TupleGetItem(func_1661_call(), 1)
call_7404 = relay.TupleGetItem(func_1663_call(), 1)
func_437_call = mod.get_global_var('func_437')
func_438_call = mutated_mod.get_global_var('func_438')
call_7407 = func_437_call()
call_7408 = func_437_call()
output = relay.Tuple([call_7391,call_7403,call_7407,])
output2 = relay.Tuple([call_7392,call_7404,call_7408,])
func_7415 = relay.Function([], output)
mod['func_7415'] = func_7415
mod = relay.transform.InferType()(mod)
output = func_7415()
func_7416 = relay.Function([], output)
mutated_mod['func_7416'] = func_7416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_898_call = mod.get_global_var('func_898')
func_899_call = mutated_mod.get_global_var('func_899')
call_7460 = relay.TupleGetItem(func_898_call(), 1)
call_7461 = relay.TupleGetItem(func_899_call(), 1)
func_3407_call = mod.get_global_var('func_3407')
func_3409_call = mutated_mod.get_global_var('func_3409')
var_7468 = relay.var("var_7468", dtype = "uint16", shape = (1, 16))#candidate|7468|(1, 16)|var|uint16
call_7467 = relay.TupleGetItem(func_3407_call(relay.reshape(var_7468.astype('uint16'), [4, 2, 2])), 1)
call_7469 = relay.TupleGetItem(func_3409_call(relay.reshape(var_7468.astype('uint16'), [4, 2, 2])), 1)
func_4373_call = mod.get_global_var('func_4373')
func_4374_call = mutated_mod.get_global_var('func_4374')
call_7495 = func_4373_call()
call_7496 = func_4373_call()
func_4211_call = mod.get_global_var('func_4211')
func_4212_call = mutated_mod.get_global_var('func_4212')
call_7499 = relay.TupleGetItem(func_4211_call(), 1)
call_7500 = relay.TupleGetItem(func_4212_call(), 1)
func_1306_call = mod.get_global_var('func_1306')
func_1308_call = mutated_mod.get_global_var('func_1308')
const_7520 = relay.const([-3.862792,1.683059,8.776722,-2.729057,0.864365,-6.580750,5.407548,0.910889,-7.330668,8.825547,1.230572,-9.316538,-4.161059,9.402451,-9.308866,-4.658476,-6.140459,6.231943,-1.798622,-0.691842,-4.248780,0.968130,3.272403,-1.319032,-8.447136,5.258124,0.477910,8.022889,-3.626175,-3.195500,-0.561520,4.457755,-7.688948,1.782339,-3.813077,-9.988306,-2.508124,4.807153,9.347850,6.637692,5.661842,7.041589,8.581977,-6.726056,-2.087149,-3.258381,4.065184,9.374857,4.291477,-9.966296,3.498142,-1.548548,-5.399385,0.151585,5.916100,-9.664566,-6.517862,-0.719023,-7.435860,5.894269,5.129404,6.887709,8.393552,-3.626479,6.332483,1.450081,5.773608,-0.245478,7.868561,8.538793,7.346908,9.322733,-0.111926,2.574101,-1.782266,9.947893,-4.301613,-7.474762,1.007718,-3.305313,6.360758,6.984783,4.487541,2.533511,-7.078876,-4.295396,-6.228976,9.812535,6.568805,9.533710,3.655369,4.084638,2.158667,1.237620,-8.660020,-7.629569,0.576129,-6.711145,1.314593,9.639091,2.468362,1.507906,8.989568,-3.383177,6.403140,-4.377014,-9.909172,8.535294,6.202932,-8.116750], dtype = "float64")#candidate|7520|(110,)|const|float64
call_7519 = relay.TupleGetItem(func_1306_call(relay.reshape(const_7520.astype('float64'), [10, 11, 1])), 0)
call_7521 = relay.TupleGetItem(func_1308_call(relay.reshape(const_7520.astype('float64'), [10, 11, 1])), 0)
var_7522 = relay.var("var_7522", dtype = "float32", shape = (14, 2, 2))#candidate|7522|(14, 2, 2)|var|float32
bop_7523 = relay.add(call_7460.astype('uint16'), var_7522.astype('uint16')) # shape=(14, 2, 2)
bop_7526 = relay.add(call_7461.astype('uint16'), var_7522.astype('uint16')) # shape=(14, 2, 2)
output = relay.Tuple([call_7467,var_7468,call_7495,call_7499,call_7519,const_7520,bop_7523,])
output2 = relay.Tuple([call_7469,var_7468,call_7496,call_7500,call_7521,const_7520,bop_7526,])
func_7537 = relay.Function([var_7468,var_7522,], output)
mod['func_7537'] = func_7537
mod = relay.transform.InferType()(mod)
var_7538 = relay.var("var_7538", dtype = "uint16", shape = (1, 16))#candidate|7538|(1, 16)|var|uint16
var_7539 = relay.var("var_7539", dtype = "float32", shape = (14, 2, 2))#candidate|7539|(14, 2, 2)|var|float32
output = func_7537(var_7538,var_7539,)
func_7540 = relay.Function([var_7538,var_7539,], output)
mutated_mod['func_7540'] = func_7540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4477_call = mod.get_global_var('func_4477')
func_4478_call = mutated_mod.get_global_var('func_4478')
call_7548 = relay.TupleGetItem(func_4477_call(), 1)
call_7549 = relay.TupleGetItem(func_4478_call(), 1)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_7550 = relay.TupleGetItem(func_3841_call(), 1)
call_7551 = relay.TupleGetItem(func_3842_call(), 1)
output = relay.Tuple([call_7548,call_7550,])
output2 = relay.Tuple([call_7549,call_7551,])
func_7556 = relay.Function([], output)
mod['func_7556'] = func_7556
mod = relay.transform.InferType()(mod)
output = func_7556()
func_7557 = relay.Function([], output)
mutated_mod['func_7557'] = func_7557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4587_call = mod.get_global_var('func_4587')
func_4588_call = mutated_mod.get_global_var('func_4588')
call_7616 = relay.TupleGetItem(func_4587_call(), 2)
call_7617 = relay.TupleGetItem(func_4588_call(), 2)
var_7620 = relay.var("var_7620", dtype = "uint16", shape = (4, 2, 2))#candidate|7620|(4, 2, 2)|var|uint16
bop_7621 = relay.multiply(call_7616.astype('int8'), relay.reshape(var_7620.astype('int8'), relay.shape_of(call_7616))) # shape=(4, 2, 2)
bop_7624 = relay.multiply(call_7617.astype('int8'), relay.reshape(var_7620.astype('int8'), relay.shape_of(call_7617))) # shape=(4, 2, 2)
func_4897_call = mod.get_global_var('func_4897')
func_4899_call = mutated_mod.get_global_var('func_4899')
var_7627 = relay.var("var_7627", dtype = "float32", shape = (768,))#candidate|7627|(768,)|var|float32
call_7626 = relay.TupleGetItem(func_4897_call(relay.reshape(var_7627.astype('float32'), [768, 1])), 0)
call_7628 = relay.TupleGetItem(func_4899_call(relay.reshape(var_7627.astype('float32'), [768, 1])), 0)
output = relay.Tuple([bop_7621,call_7626,var_7627,])
output2 = relay.Tuple([bop_7624,call_7628,var_7627,])
func_7631 = relay.Function([var_7620,var_7627,], output)
mod['func_7631'] = func_7631
mod = relay.transform.InferType()(mod)
mutated_mod['func_7631'] = func_7631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7631_call = mutated_mod.get_global_var('func_7631')
var_7633 = relay.var("var_7633", dtype = "uint16", shape = (4, 2, 2))#candidate|7633|(4, 2, 2)|var|uint16
var_7634 = relay.var("var_7634", dtype = "float32", shape = (768,))#candidate|7634|(768,)|var|float32
call_7632 = func_7631_call(var_7633,var_7634,)
output = call_7632
func_7635 = relay.Function([var_7633,var_7634,], output)
mutated_mod['func_7635'] = func_7635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_7648 = relay.TupleGetItem(func_3841_call(), 3)
call_7649 = relay.TupleGetItem(func_3842_call(), 3)
func_5764_call = mod.get_global_var('func_5764')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_7654 = func_5764_call()
call_7655 = func_5764_call()
bop_7662 = relay.minimum(call_7648.astype('int64'), relay.reshape(call_7654.astype('int64'), relay.shape_of(call_7648))) # shape=(4, 2, 2)
bop_7665 = relay.minimum(call_7649.astype('int64'), relay.reshape(call_7655.astype('int64'), relay.shape_of(call_7649))) # shape=(4, 2, 2)
uop_7666 = relay.acosh(call_7648.astype('float32')) # shape=(4, 2, 2)
uop_7668 = relay.acosh(call_7649.astype('float32')) # shape=(4, 2, 2)
uop_7674 = relay.cosh(uop_7666.astype('float32')) # shape=(4, 2, 2)
uop_7676 = relay.cosh(uop_7668.astype('float32')) # shape=(4, 2, 2)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
const_7678 = relay.const([6.043786,4.734096,-6.379048,-4.106837,-3.299459,-2.199143,4.460576,-8.581766,5.231581,7.172114,4.742187,3.496477,5.896007,-6.573082,0.479380,7.590493,6.387216,7.297255,-7.478913,5.907815,0.893656,3.512014,-9.266513,-6.366983,-5.341362,0.639669,9.979106,7.952511,1.120724,6.494054,9.853989,5.105901,4.880545,3.199371,-0.560403,9.293418,-8.904031,-4.269639,-9.719193,9.469419,6.079993,-8.068853,5.198984,5.558561,2.589966,1.673672,-0.245076,7.018565,-5.213037,9.593517,8.258775,-7.969941,8.847130,4.544938,6.478254,-6.344433,4.485154,0.380918,-2.285363,3.288951,4.536499,2.455481,4.881087,-2.116623,2.223823,-7.223100,-4.675270,-6.409367,7.711148,9.304559,-4.285918,2.047852,-3.032397,3.685383,-5.934853,-3.984584,1.623283,7.485451,-8.673053,-1.981337,8.755172,-3.380266,3.246969,8.480765,-9.284564,6.599233,-2.967302,-9.368661,1.246400,5.932812,-6.296538,-9.757035,1.183150,-8.490401,0.328728,3.253776,8.673007,-7.538744,8.430978,-8.043303,-9.440586,-5.087866,-4.515913,3.661569,-2.643181,2.729227,-5.802385,6.597704,9.363949,3.869197,-8.421635,5.928025,-5.143435,8.271822,2.387902,-6.405698,2.653083,-2.909331,6.566191,-0.042799,9.772245,2.102769,0.528743,8.893398,-4.877826,3.360329,-8.062928,0.660942,-3.159721,-5.929945,-4.477614,8.922572,6.471579,9.672068,1.654204,7.637642,-9.761657,-5.555071,1.201960,-2.184242,-8.866073,-2.298136,5.553961,8.909482,-3.917412,1.123043,-8.444671,2.215753,2.750460,0.678162,-4.586643,7.761691,1.008335,-8.853289,3.489091,-2.933479,-1.799577,-5.474444,-9.916586,1.933902,7.177759,0.767608,2.506189,-3.844109,-7.764913,5.924125,-3.443296,2.677365,-6.245765,-5.408256,-3.823644,6.626730,9.345430,-3.272562,7.198360,0.113985,1.743333,1.953120,0.176398,1.580080,1.525484,-1.266770,5.198930,2.897865,9.404089,9.645843,-8.860699,-4.196285,5.571274,-2.418939,-2.022708,6.111931,-0.886651,-7.178221,-7.697778,7.299304,-7.794353,2.522140,6.252812,5.262466,-5.983351,2.540393,2.392290,3.918363,-9.941595,5.513004,1.360797,-9.658924,6.767821,1.901810,-9.312417,4.075380,-3.334430,-5.812340,3.255624,-9.268167,1.380798,0.290919,6.262297,1.438930,-5.686393,-8.550654,3.998550,2.274024,3.342227,8.039526,-8.913152,-3.499183,4.724159,-0.408227,-2.886547,4.573458,-4.951092,-7.439086,7.987537,-1.989059,-8.005885,2.738995,4.377175,2.815147,3.670116,7.532288,5.129943,-6.334308,-8.909545,-6.782588,5.542896,-4.276205,-2.127513,8.458015,-3.851401,1.329246,-1.869872,9.860699,6.798306,-9.082263,4.012276,-9.939868,7.305840,4.652714,-9.334481,-4.737054,2.537487,7.399510,9.599685,4.291663,-3.526046,-4.169927,6.021406,0.184327,-5.345323,7.422884,8.520529,1.363167,-4.036616,-9.410069,-1.978276,-2.443346,-6.651716,6.149377,-7.558829,0.488245,7.436197,4.405220,8.919967,3.833250,-6.099537,4.301872,6.611897,-6.509277,-9.344873,-0.572462,4.458334,-3.719707,-8.672923,5.169704,1.542922,-4.800963,8.670232,6.123643,-7.511760,-1.001715,-3.105262,-4.144687,-0.331820,7.922016,3.538766,1.073443,0.807712,-8.920590,7.417409,-3.299163,9.193760,9.326346,0.168345,3.789359,-2.167252,-5.836736,-5.761151,-1.275955,-3.431224,5.270835,6.182000,-0.400294,-5.099540,-4.267689,5.621538,-5.544596,5.769370,8.461476,0.754198,-4.212613,-4.184418,-6.698856,1.718243,-8.814159,-6.997287,-0.876734,-0.934665,-7.737532,1.968432,4.562178,-1.490113,9.205366,6.091014,-2.920532,-3.065554,-0.710054,3.219129,3.594971,3.802065,-9.145775,3.991735,5.141289,-5.890959,-8.188781,2.193538,-1.130899,-8.643258,8.247610,-9.848802,-8.708876,3.175545,0.798966,5.273069,9.731725,-3.148778,-3.795886,-1.244750,-6.584531,-0.429464,8.691533,-7.249013,8.005239,1.180272,-2.436187,-2.410398,-4.719212,-0.052304,-2.067501,-7.058998,-5.455640,-1.267943,-3.423225,1.801995,2.824394,-1.858637,7.519486,-8.672342,2.147647,5.386381,6.575053,-1.387513,9.999705,0.124226,-1.072515,-6.062098,2.692720,4.949718,5.316398,-4.141157,-3.420278,3.279068,2.222552,-1.639702,-3.269918,-7.020492,1.616394,8.154647,9.652534,2.343464,2.545671,0.832385,-1.943616,-4.598915,5.677600,-9.799436,1.163850,4.963182,6.881506,3.778048,8.250099,3.711365,-1.286227,-9.603660,2.302774,1.380024,5.254705,8.104947,-5.962426,3.911885,-1.555797,4.392215,-7.822248,-4.381140,8.502225,7.016912,-7.880164,2.531619,5.439173,-3.675017,0.008797,2.998057,-4.077704,-5.647482,8.473812,-3.540955,3.016474,7.438860,-5.761377,2.171979,-5.764706,3.176735,4.304467,2.804389,-3.446015,-1.981261,-7.640603,-6.362803,-9.896318,4.555466,-4.828145,-6.373225,1.792071,7.787002,1.414294,6.163968,2.941156,-5.236357,-9.749432,-6.431980,-1.804031,-2.668964,-7.593470,6.716817,-0.790204,-2.400226,4.689986,-6.945522,3.586718,-9.573825,6.078657,-2.575556,-3.615210,7.737358,-5.781950,6.549087,-7.277581,9.829472,-2.589517,-5.750938,4.063618,-2.563317,0.868719,-1.103690,-0.013018,5.321457,-9.169785,7.993967,5.887723,5.164347,-8.652534,-9.416914,0.516196,3.300493,-9.665075,-8.114358,9.789386,-3.764827,9.676094,5.886134,-8.289628,7.832444,-6.960098,0.064738,-6.043171,9.654808,-6.462489,4.983447,-7.140593,4.495279,-4.602369,-1.285514,-5.872260,-5.480789,5.899467,-6.834599,6.984816,3.179127,-4.796424,4.181417,8.593074,6.766742,-6.638304,6.957287,5.214576,2.607087,-3.629919,4.183587,5.327015,5.674329,7.900110,-6.069668,8.480848,-5.665138,-9.691204,-8.072790,9.105095,8.893741,5.183104,-7.351647,-3.681239,-4.700759,5.895970,9.304335,-2.454223,-3.264822,-3.977806,-1.617263,-3.173089,6.096678,-4.362656,-5.176550,9.306036,0.402549,7.520042,-2.124863,3.809913,-4.472569,-0.238967,0.622841,-1.375174,4.415098,-2.160663,4.314853,-5.139036,-8.595182,-2.526758,-7.892624,-5.128703,-5.457405,5.132121,6.367789,-5.869024,-1.660494,-3.258878,4.667782,3.446876,8.047111,-6.474802,-0.436418,-4.093696,3.547527,7.141352,-3.638068,8.698938,4.441272,0.084704,4.702266,2.340804,9.954967,-9.458918,-2.902646,2.342751,7.754114,-5.769388,-4.066208,-3.505814,-0.767221,-4.452650,-2.455052,2.575637,-9.554182,-3.311494,-9.488251,9.795909,7.012684,-8.829102,0.480881,-4.376999,6.018469,-3.007271,8.493275,6.571674,9.191593,-5.702651,0.904617,0.114791,0.100432,-9.241090,4.654357,0.750139,0.194490,3.862365,6.134388,9.602160,-9.559562,-7.985913,6.383296,0.302665,7.089000,-2.908529,-7.836145,0.467294,6.896097,0.876067,8.674671,-3.626587,2.544647,-0.755863,0.364528,0.899802,5.213745,9.184305,-6.912232,0.680387,-5.061429,-9.077236,-3.723421,-8.278371,3.003365,-5.863461,-5.414566,1.110067,-0.994397,-6.962776,-6.968229,-6.524067,-1.494406,-3.416684,-8.727971,-3.189616,4.323096,4.734294,-2.847581,9.245651,-4.513512,2.227056,-7.772890,-8.317393,-6.713883,-7.065481,-2.481511,-4.376769,-3.236046,4.696252,7.907557,-8.206550,9.390028,-6.107825,8.040529,0.002711,0.591465,5.756798,-0.032407,4.575544,-5.744625,2.344283,-7.352101,8.049555,-1.341658,2.681876,3.594435,-4.191495,-4.773810,-0.783495,-6.918137,9.270601,-8.996729,-5.853685,-0.634727,1.497897,6.789161,9.291182,6.999820,4.265899,-4.850822,5.662659,-0.709850,-2.819443,-5.045215,-6.735738,-6.449900,-5.326563,-6.121308,7.995255,-8.928510,-8.847384,0.775736,7.503542,-0.611090,-1.134232,-3.603805,-1.902739,2.055090,2.986532,-6.760804,1.019248,1.972864,1.877603,-8.310972,-7.582496,-9.899545,-9.565831,-2.711946,-6.168128,-6.618990,8.098793,-6.430199,5.173788,-3.950975,8.433083,2.574195,-4.646269,-5.326381,-7.157057,-8.069542,-6.664526,3.324293,2.378430,-8.769648,5.740973,-8.554790,1.981665,-2.067527,7.257424,6.338052,7.351662,0.642811,1.582595,-9.292312,-9.869093,-3.152492,5.964820,2.707428,-3.980011,-3.153447,7.271841,-8.401199,7.728300,0.125224,-1.044910,6.946265,1.813659,1.133181,-1.116270,6.132381,-0.262852,2.827656,9.177293,-7.227521,8.552367,5.544679,-0.156408,0.258434,3.022829,-5.724540,-0.069068,9.574857,-2.155957,-1.374473,-5.035563,5.667564,-3.550979,-5.377961,5.352897,3.790187,5.085745,3.821113,-0.794768,1.877823,-5.225237,0.264904,2.235889,-8.030204,2.225397,1.399556,-8.010532,6.810537,9.320644,8.865816,-7.363114,9.728553,1.927349,5.320976,-4.035243,0.552629,-8.343719,4.449129,-5.241506,0.043048,-0.363074,7.427121,3.263055,3.287565,9.013500,-4.456131,7.157299,5.613050,-2.935791], dtype = "float64")#candidate|7678|(840,)|const|float64
call_7677 = func_3534_call(relay.reshape(const_7678.astype('float64'), [12, 5, 14]))
call_7679 = func_3534_call(relay.reshape(const_7678.astype('float64'), [12, 5, 14]))
output = relay.Tuple([bop_7662,uop_7674,call_7677,const_7678,])
output2 = relay.Tuple([bop_7665,uop_7676,call_7679,const_7678,])
func_7691 = relay.Function([], output)
mod['func_7691'] = func_7691
mod = relay.transform.InferType()(mod)
output = func_7691()
func_7692 = relay.Function([], output)
mutated_mod['func_7692'] = func_7692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5530_call = mod.get_global_var('func_5530')
func_5532_call = mutated_mod.get_global_var('func_5532')
call_7716 = relay.TupleGetItem(func_5530_call(), 0)
call_7717 = relay.TupleGetItem(func_5532_call(), 0)
output = relay.Tuple([call_7716,])
output2 = relay.Tuple([call_7717,])
func_7727 = relay.Function([], output)
mod['func_7727'] = func_7727
mod = relay.transform.InferType()(mod)
output = func_7727()
func_7728 = relay.Function([], output)
mutated_mod['func_7728'] = func_7728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1849_call = mod.get_global_var('func_1849')
func_1850_call = mutated_mod.get_global_var('func_1850')
call_7729 = relay.TupleGetItem(func_1849_call(), 0)
call_7730 = relay.TupleGetItem(func_1850_call(), 0)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
const_7761 = relay.const([-9.955711,-5.734519,-6.237511,1.969217,-7.464125,5.996259,8.594510,-8.883518,-0.012455,-8.019529,-0.250349,-9.187449,4.832696,7.266784,8.280152,6.249327,1.258446,-4.061843,1.744113,-5.416570,-7.870929,-2.122464,2.600818,-4.680461,-2.477739,-5.432699,6.147856,-1.968696,-3.290995,-8.183956,-9.222331,4.142339,2.070842,6.570661,-9.742103,-0.360874,-4.585963,-9.514796,8.417021,6.721985,-7.626827,8.923578,-0.958590,-6.267237,7.988670,-5.812274,-8.379766,-1.807581,-8.887819,0.849177,7.107505,3.472273,-5.579380,1.871407,-8.508872,5.870580,4.990821,3.618803,-2.413966,-0.775017,-5.107598,2.715088,5.826099,-1.530267,1.412280,-1.092121,5.793951,-5.910930,5.957864,2.179138,5.857674,-3.272381,7.828605,-7.659028,-1.187752,-1.230688,-9.153664,5.021259,4.416326,2.665162,5.541223,6.365796,4.028451,-5.781025,-6.438193,8.184020,-9.572472,-8.908893,7.198796,4.155204,5.643385,-8.625464,5.159414,7.007022,8.625122,-9.565120,-3.399799,2.863804,6.570441,6.839957,4.306068,6.491078,-8.444747,-4.135514,1.678874,8.979234,8.898712,-9.713625,-6.041284,6.764706,-6.968974,-3.096200,2.326082,-2.880555,-2.630338,-9.390271,-6.776955,5.752992,1.540687,-8.444585,-9.672800,-0.522193,2.134695,-2.937492,-3.805600,7.549487,2.194010,-0.121081,8.951075,-0.500521,-8.858704,-2.601031,-6.911390,5.470180,4.262918,-3.709036,-0.397697,5.408950,4.845633,6.481441,3.158142,-2.589745,-4.370756,3.238266,-6.490947,2.569514,6.699545,7.520544,-5.790880,9.057675,8.192201,6.217723,-7.861063,0.506946,-5.347299,-0.671258,-6.914239,2.698233,2.138137,-1.153440,-5.420962,-1.670539,2.582691,7.757031,-9.568191,1.795618,4.734846,2.606094,0.122638,2.404664,6.086228,0.870078,2.733621,1.909658,-2.425181,-3.525199,7.915931,-8.026355,-5.264160,-9.690512,-3.131688,-7.541883,-4.142407,-4.750230,1.879146,-8.252976,1.069005,-6.776530,-8.308565,2.657275,8.077174,8.012639,-1.544313,-5.906279,5.937383,2.154279,-7.183971,9.930706,-7.798423,4.275751,-0.533726,-7.649090,9.335574,-6.522625,-4.867759,-6.176939,8.773156,2.579545,9.677235,-3.611621,-4.316719,2.547257,-4.343128,-6.995897,-4.401589,-5.033105,6.914076,-8.171570,3.629180,-5.485048,-0.714980,7.097351,-8.893046,9.120067,-1.970067,-0.759979,0.103044,-7.235327,3.896795,-0.039560,-0.685262,-5.987390,-5.252265,-5.273845,2.025919,5.145538,-9.294860,5.589433,4.996461,-4.566119,-4.457004,4.819044,-2.528538,0.187846,-4.500857,2.036208,-2.996061,-3.634490,-3.967017,-5.941930,6.685721,0.725976,6.533654,-4.720817,5.781740,-1.314345,8.407740,-9.440321,0.680317,6.986678,9.471888,-8.877047,-0.636304,-0.336407,-0.291760,-1.219764,7.323025,8.806491,-7.360237,6.256742,-7.443634,-5.148363,3.497030,-8.342021,-4.176086,-5.224432,-4.400938,-2.007408,9.687958,-3.081602,8.921046,4.205875,-5.721774,0.981592,-6.391007,6.833639,1.129568,7.018151,-7.847525,7.893648,1.478290,-1.966542,6.789073,0.235350,-2.355601,-0.334205,-8.812284,-6.846492,-3.038509,-2.763586,-6.134658,0.403058,3.794677,7.867636,-4.539529,-0.585231,-3.938474,-3.952045,3.913720,3.395009,1.885504,-5.372082,7.113425,-2.080829,-8.863184,5.458067,-8.699532,-5.383567,2.778393,3.346074,5.879037,7.365931,5.672646,9.868078,3.595401,-7.703436,-4.848492,7.976121,8.780687,5.281255,-3.433483,-7.150021,7.466849,-5.052113,-2.006227,4.890761,8.340608,-7.253861,-9.822113,-2.303274,-9.335436,-4.355937,6.433118,-3.394238,8.397782,-5.876331,-6.395930,5.849844,-2.417372,-9.308343,5.537891,-0.863529,0.397181,9.580744,-4.720520,6.453012,-1.809866,6.842977,1.603432,-5.809547,5.671786,-4.640744,-2.289291,4.041541,3.831314,5.522890,4.255698,-9.887328,-2.301796,-7.818780,9.450383,4.374680,6.772232,5.031039,7.370724,-5.230573,-9.876568,-5.088111,-5.042444,6.381134,-3.399629,-0.540393,-7.451866,-6.921719,7.564826,1.309400,-7.253896,-8.811246,3.037434,4.182786,-2.026423,1.675455,-1.593352,5.088524,-2.491674,8.593821,9.970262,-4.892144,-2.878056,7.671562,-0.504793,-9.971559,6.181734,-6.634442,-9.093951,0.017206,8.320570,0.683481,0.825602,-7.622149,-2.972988,-2.177401,-3.882748,5.641437,4.068784,-5.275640,-7.495965,-9.123517,5.288269,-9.849272,-1.279012,-2.534050,2.851916,-8.234477,-3.263415,-8.759492,-2.513002,5.732107,4.741062,5.468322,9.469139,-6.499561,-7.748013,6.138370,-1.645771,1.992730,-3.957347,-7.891124,8.032862,-4.381651,-0.770175,-9.940214,8.245798,3.150528,0.972668,4.932340,-3.660439,-5.048247,-7.466416,-2.670534,7.227489,-1.570571,-6.270515,9.594429,4.469780,7.084767,-5.450245,-0.336885,7.316770,5.243943,-4.029789,9.452804,-3.921249,0.203720,-3.437447,7.881443,2.431147,9.248155,8.081854,9.867481,-1.037989,-6.733427,4.262621,-4.894111,-7.231281,5.447465,-7.033089,1.793175,-8.027292,5.103578,-6.947616,-4.729209,-2.107593,3.812433,6.061771,-3.576242,-3.973726,-7.856705,6.088619,-3.902276,-3.772717,-4.226891,9.263241,-9.706702,-5.910638,-7.784474,-7.635425,-0.247406,-6.270894,-2.602795,4.624034,2.141052,4.470419,4.422639,-8.719676,-8.078160,4.257281,3.186590,-1.655922,-6.071932,1.970118,-6.481195,5.289722,3.622932,-4.448208,4.068312,-4.952813,6.860668,4.381981,6.524506,0.721388,-8.601287,-6.952442,6.741817,6.375596,-1.327123,-6.266387,0.857633,0.395054,5.274303,-0.107861,8.256565,5.529365,2.664975,3.267410,-9.133709,-0.446702,3.806837,-6.098441,-5.337431,-0.372136,-4.975175,2.600569,8.788973,-7.488510,-9.784633,4.972699,-7.805452,7.202740,4.781499,-5.838880,7.408416,1.465920,4.774517,0.330049,8.065562,-4.593351,-0.113847,8.980934,5.165060,-4.194865,0.256139,3.149686,-0.006070,9.620822,-9.637703,6.877472,-2.707802,-2.875233,-2.815566,2.425337,-0.507758,6.477877,1.145600,-4.808874,1.276374,5.708850,-7.800488,-5.878869,4.974327,5.566827,0.840305,1.867607,4.842902,6.461889,1.617359,1.792876,4.153449,-3.092367,-4.476776,1.016181,6.492827,-1.424113,0.756735,-0.874327,-9.311758,-4.830608,-9.119326,2.349808,-0.391171,6.386704,-2.631571,3.471329,3.468166,-4.149107,-2.302876,3.941292,-3.370813,4.806583,-1.293376,-6.872495,1.526549,-9.177017,-0.754297,1.850586,4.298416,-6.611738,-7.345219,1.525357,4.045024,4.328172,6.499475,0.582144,-4.150539,6.804506,-3.684692,1.544266,1.016662,0.284585,1.345407,-0.536495,0.594752,-1.470798,-9.897402,-8.182213,-1.089320,9.235696,-1.134640,1.407044,1.895803,-7.296897,2.821456,-6.684828,9.325584,-6.432872,-1.834323,5.353477,-4.834835,7.268620,2.125590,-0.104196,0.830256,2.602946,8.660217,-2.803890,-4.356314,-0.015356,-7.129696,-0.433691,5.690291,8.333993,3.414315,8.941401,-2.945916,-0.054010,-8.809658,5.798768,-6.574954,-3.745048,-7.877503,-4.486486,9.588591,-1.766758,1.792111,8.824047,3.691594,3.623107,-5.389007,-5.487673,3.707390,-0.701196,-6.385909,-0.471486,4.631344,-4.750016,7.660603,-6.482339,8.898550,3.679932,7.745312,9.492372,8.859363,7.580481,-6.389900,-1.224813,-9.391480,9.071658,7.434399,2.514350,-3.169726,-6.249461,-8.548914,-2.483412,8.538903,2.166481,4.043159,0.689972,2.493162,-1.927772,3.542389,7.847478,1.578326,-5.394820,-8.460970,2.939020,9.092159,3.909818,-9.277656,8.246472,0.894065,-2.376686,-7.812512,1.966080,-1.917877,7.785450,-2.094201,2.037285,5.872412,-2.661570,7.636421,7.253931,4.044054,5.853145,-7.816958,9.574987,8.635963,-1.029713,-0.316798,7.406289,6.132337,-3.448130,4.508527,-0.285201,9.578445,8.501735,-8.495361,2.899600,2.265636,-8.357368,9.366645,4.606693,9.205182,-2.535430,2.939786,1.383662,-0.048877,-5.217578,1.281182,4.657773,-0.945137,-6.083875,1.507445,-5.320222,-1.494047,-1.491455,2.337576,-4.922154,-5.121337,-1.284327,-1.305826,-5.368703,4.024006,-7.581353,8.690604,5.917840,-9.523963,3.569693,2.495063,-8.486712,-4.853759,1.157031,-9.144408,-6.640797,4.413075,-9.059666,-5.571404,-2.933258,-2.045579,8.425655,-6.927743,2.731368,-6.419253,-7.794660,-0.368812,4.957517,-2.864963,-7.439833,-1.962553,9.160527,9.256789,6.742282,-9.943886,7.988175,-6.463142,3.844879,4.863243,-3.611186,8.863731,6.444665,2.883189,-5.709741,-5.535031,1.709509,7.184366,-3.926021,-9.455903,8.921216,3.591174,5.595674,9.248418,6.930671,4.545403,-1.753365,-8.031219,9.003873,-2.569072,6.293837,-1.238338,3.013844,5.475373,3.012099,5.009543,1.226254,1.916411,-3.963689,7.350640,-1.245360,0.533246,1.142511,-5.732267], dtype = "float64")#candidate|7761|(840,)|const|float64
call_7760 = func_3534_call(relay.reshape(const_7761.astype('float64'), [12, 5, 14]))
call_7762 = func_3534_call(relay.reshape(const_7761.astype('float64'), [12, 5, 14]))
func_475_call = mod.get_global_var('func_475')
func_477_call = mutated_mod.get_global_var('func_477')
call_7763 = relay.TupleGetItem(func_475_call(), 0)
call_7764 = relay.TupleGetItem(func_477_call(), 0)
output = relay.Tuple([call_7729,call_7760,const_7761,call_7763,])
output2 = relay.Tuple([call_7730,call_7762,const_7761,call_7764,])
func_7774 = relay.Function([], output)
mod['func_7774'] = func_7774
mod = relay.transform.InferType()(mod)
output = func_7774()
func_7775 = relay.Function([], output)
mutated_mod['func_7775'] = func_7775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2342_call = mod.get_global_var('func_2342')
func_2344_call = mutated_mod.get_global_var('func_2344')
call_7807 = relay.TupleGetItem(func_2342_call(), 2)
call_7808 = relay.TupleGetItem(func_2344_call(), 2)
output = relay.Tuple([call_7807,])
output2 = relay.Tuple([call_7808,])
func_7811 = relay.Function([], output)
mod['func_7811'] = func_7811
mod = relay.transform.InferType()(mod)
output = func_7811()
func_7812 = relay.Function([], output)
mutated_mod['func_7812'] = func_7812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7727_call = mod.get_global_var('func_7727')
func_7728_call = mutated_mod.get_global_var('func_7728')
call_7830 = relay.TupleGetItem(func_7727_call(), 0)
call_7831 = relay.TupleGetItem(func_7728_call(), 0)
output = call_7830
output2 = call_7831
func_7832 = relay.Function([], output)
mod['func_7832'] = func_7832
mod = relay.transform.InferType()(mod)
mutated_mod['func_7832'] = func_7832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7832_call = mutated_mod.get_global_var('func_7832')
call_7833 = func_7832_call()
output = call_7833
func_7834 = relay.Function([], output)
mutated_mod['func_7834'] = func_7834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6664_call = mod.get_global_var('func_6664')
func_6666_call = mutated_mod.get_global_var('func_6666')
call_7848 = func_6664_call()
call_7849 = func_6664_call()
func_2598_call = mod.get_global_var('func_2598')
func_2601_call = mutated_mod.get_global_var('func_2601')
var_7856 = relay.var("var_7856", dtype = "uint16", shape = (16,))#candidate|7856|(16,)|var|uint16
call_7855 = func_2598_call(relay.reshape(var_7856.astype('uint16'), [4, 2, 2]))
call_7857 = func_2598_call(relay.reshape(var_7856.astype('uint16'), [4, 2, 2]))
output = relay.Tuple([call_7848,call_7855,var_7856,])
output2 = relay.Tuple([call_7849,call_7857,var_7856,])
func_7861 = relay.Function([var_7856,], output)
mod['func_7861'] = func_7861
mod = relay.transform.InferType()(mod)
var_7862 = relay.var("var_7862", dtype = "uint16", shape = (16,))#candidate|7862|(16,)|var|uint16
output = func_7861(var_7862)
func_7863 = relay.Function([var_7862], output)
mutated_mod['func_7863'] = func_7863
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7936 = relay.const([[[-6,-6,3,10,1,3,6,2],[-6,5,3,-9,2,-3,10,-4],[10,7,-5,7,-2,7,8,7],[-6,-9,10,6,-5,2,8,-4],[-7,-4,-7,10,3,-9,-7,-4],[-9,-1,-4,10,8,5,-9,6],[9,8,-3,7,-6,-7,-3,5],[8,10,5,-1,1,8,-6,-7],[4,-3,6,5,6,-4,-4,10],[6,-4,-7,3,1,-1,-8,2],[-4,1,2,-1,-7,-7,5,-5],[-5,-4,-1,4,10,9,-2,10]],[[-5,-5,8,-7,-2,-7,2,-9],[-8,1,2,3,1,-2,4,-10],[-4,6,-2,6,-7,-10,-5,-6],[-2,4,2,-7,-1,7,-2,4],[1,-9,-3,6,10,-7,-5,-7],[9,2,-1,6,8,9,10,8],[-3,6,-4,8,-2,-8,-9,5],[-8,-1,6,1,1,-7,-3,-4],[-2,6,5,-9,-8,-4,-1,5],[6,6,-3,7,9,5,-9,-2],[-9,8,-2,-3,-3,7,7,-1],[8,-6,-6,-5,7,9,-8,8]],[[9,5,4,-2,-6,8,3,-6],[-9,-1,5,2,-7,1,-3,-5],[6,6,8,4,-8,-7,2,-1],[-6,-7,-8,5,1,-3,5,-9],[-7,-9,-4,1,5,-3,1,-9],[-6,-8,-5,-2,-6,-3,10,-2],[-8,6,-3,-3,4,7,-8,2],[5,8,10,-8,-4,1,-4,5],[-3,-3,-7,-7,2,8,-2,-4],[8,-7,-4,9,8,2,-3,2],[-7,2,-1,6,-3,-3,-3,-2],[-1,-3,7,-2,2,-5,-2,-10]],[[-3,-4,-1,10,-3,1,-10,-8],[3,5,-3,-5,3,-9,8,-6],[2,-7,-10,-9,10,8,-2,-10],[-10,-6,-1,10,-10,3,-10,1],[8,-9,5,-1,7,-4,8,7],[-8,-4,4,5,5,-2,-6,1],[2,-2,7,3,-5,-6,-10,2],[5,-7,10,-1,-9,-3,7,-10],[-3,8,-6,-7,-8,3,-5,-6],[-2,7,4,-8,4,-1,-5,-2],[3,-10,2,1,10,8,2,-6],[-6,6,-3,-4,-4,-10,3,-9]],[[3,-9,-9,-3,-6,-6,4,3],[-7,9,-1,-6,7,6,-9,8],[6,-5,10,4,2,6,-4,-5],[8,-8,8,-8,4,-4,-10,-5],[4,9,-9,-1,5,-6,-8,9],[-6,7,-4,8,8,1,8,4],[5,5,-10,-4,6,5,2,10],[-10,-5,-1,-10,-6,-8,-6,-8],[8,4,2,3,9,-1,-2,2],[-9,4,-9,2,-7,4,5,-2],[-5,-2,-6,6,5,-8,-10,6],[-7,-1,7,6,8,-5,9,-7]],[[-6,3,4,-9,7,-3,-2,-8],[1,7,-7,-10,-10,7,6,6],[-2,6,-8,-4,-6,4,8,-9],[3,7,-9,-4,-5,10,4,-3],[-5,-2,-8,8,5,-4,-5,-4],[-8,-10,-9,8,5,3,-4,-4],[9,-1,-2,3,-2,2,1,-8],[6,-8,2,9,3,-7,-10,7],[-6,-8,-9,8,9,1,-8,1],[-6,-9,4,-6,-9,6,-5,-1],[-1,-1,-2,-2,-1,-3,9,-10],[-2,3,-6,2,3,7,9,9]],[[8,8,1,3,2,-8,7,-8],[-9,-4,2,-4,-4,-3,10,-2],[-3,10,-2,-3,-6,-7,-1,3],[-6,8,-3,-2,-3,9,-8,4],[3,3,-7,-2,-9,8,-2,1],[8,-5,-2,-7,2,2,4,1],[-10,-5,-1,1,-3,-2,-2,2],[-4,2,-4,3,-4,7,-1,-7],[1,1,6,3,-3,-6,-10,6],[7,-10,-6,8,9,7,-2,-2],[-6,-8,-5,2,8,4,8,9],[-9,-6,-3,-4,-8,4,-7,4]]], dtype = "int8")#candidate|7936|(7, 12, 8)|const|int8
const_7937 = relay.const([[[-3,-7,9,1,8,-5,8,6],[6,4,6,-8,-2,6,-3,10],[-5,9,3,-10,-10,10,4,7],[-10,10,8,-4,-7,10,7,-8],[-7,6,8,2,2,7,-10,8],[9,5,7,8,8,-6,10,-9],[10,8,3,10,-2,3,-3,-3],[8,10,5,-9,-7,-8,-8,5],[-2,10,3,-1,6,8,-5,-4],[6,8,3,4,6,-9,9,-4],[9,8,-5,6,3,3,-4,2],[-8,-3,10,2,-9,10,-7,1]],[[-2,7,-8,-9,8,10,6,3],[-2,6,4,-10,3,3,6,-5],[4,4,-6,6,4,5,6,3],[-6,2,10,-5,1,2,-5,-6],[8,3,-4,7,5,-7,2,10],[10,10,-3,-3,-6,-2,2,9],[9,-6,-3,2,-7,-8,8,8],[10,-9,4,7,-7,-10,8,-8],[5,1,-9,5,-1,-4,3,-8],[2,7,-3,6,7,8,-7,-2],[2,-10,6,6,10,-6,-2,7],[-6,-9,-1,9,-5,3,3,4]],[[-1,-8,-2,6,-4,5,9,-1],[-6,-3,7,7,9,4,7,9],[4,7,-10,6,-7,10,-2,-2],[3,-9,7,2,6,-10,-6,3],[6,6,6,10,2,9,4,4],[7,6,9,-2,6,10,-10,-1],[-6,4,8,5,-7,6,6,-7],[-5,-8,2,1,-3,1,-7,-2],[9,5,2,-7,-4,8,-7,2],[-9,8,2,1,-2,9,-5,4],[-6,9,-9,-7,-3,5,-10,-2],[7,2,9,5,6,-3,-4,2]],[[6,-8,-2,-9,9,-3,-1,10],[2,9,5,-5,7,-1,4,1],[-7,-6,1,3,1,9,-10,-4],[-10,8,-7,6,10,5,3,4],[4,-10,-7,-4,-9,-2,3,5],[-9,9,-3,-1,4,-7,-3,-6],[2,9,9,10,8,8,8,-5],[6,4,-10,-4,-3,1,3,1],[3,7,-5,9,8,7,3,-4],[7,-8,-3,3,-3,-9,2,-2],[-2,-9,3,-2,-7,9,-2,-1],[-1,6,-1,-9,3,-1,-10,4]],[[-1,8,-2,6,-9,1,10,-10],[1,6,-7,8,-2,9,-3,3],[5,-7,4,-8,10,4,-1,10],[2,-6,8,-1,5,6,2,-10],[-3,-5,10,-9,3,8,-8,8],[4,-1,7,7,-3,-8,2,-3],[4,-1,-1,3,-2,10,9,3],[1,6,-7,8,5,4,-5,-2],[7,3,2,4,7,7,3,1],[-4,-9,-1,-1,-6,-4,4,-2],[-1,-8,1,8,-9,5,-7,-3],[-3,-1,1,3,-9,-10,4,3]],[[-5,10,-7,5,5,6,-6,2],[3,-6,-7,4,5,-8,-4,-6],[-4,-6,-5,4,10,-4,1,6],[9,-10,10,-4,-8,5,7,-4],[8,-1,10,6,7,4,4,-4],[3,-3,8,7,-2,-9,-6,10],[-2,10,6,1,6,1,-7,-4],[9,-3,-5,-4,-5,-7,-5,-6],[6,8,-1,-5,-8,6,-3,6],[-8,-10,1,3,8,-6,5,-9],[-7,-4,10,3,8,-3,-10,7],[-10,-4,-1,-9,-4,-2,-9,1]],[[2,2,5,-7,-7,-7,1,-8],[1,4,-6,2,9,1,7,-4],[7,10,-3,8,9,-8,9,3],[-7,-1,3,-5,9,10,7,-4],[2,-8,-3,7,-2,-4,1,9],[8,3,5,-4,5,10,-10,6],[-10,-6,-1,-7,-8,-3,8,-8],[-4,-8,8,-5,7,-5,-2,6],[-7,7,5,-10,4,-1,5,-1],[-10,-10,-10,-3,2,4,1,8],[-2,8,10,10,1,-8,-1,-7],[-7,-1,-4,6,4,-2,9,7]]], dtype = "int8")#candidate|7937|(7, 12, 8)|const|int8
bop_7938 = relay.multiply(const_7936.astype('int8'), relay.reshape(const_7937.astype('int8'), relay.shape_of(const_7936))) # shape=(7, 12, 8)
output = bop_7938
output2 = bop_7938
func_7941 = relay.Function([], output)
mod['func_7941'] = func_7941
mod = relay.transform.InferType()(mod)
mutated_mod['func_7941'] = func_7941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7941_call = mutated_mod.get_global_var('func_7941')
call_7942 = func_7941_call()
output = call_7942
func_7943 = relay.Function([], output)
mutated_mod['func_7943'] = func_7943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6555_call = mod.get_global_var('func_6555')
func_6556_call = mutated_mod.get_global_var('func_6556')
call_7978 = relay.TupleGetItem(func_6555_call(), 0)
call_7979 = relay.TupleGetItem(func_6556_call(), 0)
func_5764_call = mod.get_global_var('func_5764')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_8008 = func_5764_call()
call_8009 = func_5764_call()
output = relay.Tuple([call_7978,call_8008,])
output2 = relay.Tuple([call_7979,call_8009,])
func_8026 = relay.Function([], output)
mod['func_8026'] = func_8026
mod = relay.transform.InferType()(mod)
mutated_mod['func_8026'] = func_8026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8026_call = mutated_mod.get_global_var('func_8026')
call_8027 = func_8026_call()
output = call_8027
func_8028 = relay.Function([], output)
mutated_mod['func_8028'] = func_8028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3563_call = mod.get_global_var('func_3563')
func_3564_call = mutated_mod.get_global_var('func_3564')
call_8045 = relay.TupleGetItem(func_3563_call(), 0)
call_8046 = relay.TupleGetItem(func_3564_call(), 0)
output = relay.Tuple([call_8045,])
output2 = relay.Tuple([call_8046,])
func_8061 = relay.Function([], output)
mod['func_8061'] = func_8061
mod = relay.transform.InferType()(mod)
mutated_mod['func_8061'] = func_8061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8061_call = mutated_mod.get_global_var('func_8061')
call_8062 = func_8061_call()
output = call_8062
func_8063 = relay.Function([], output)
mutated_mod['func_8063'] = func_8063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6737_call = mod.get_global_var('func_6737')
func_6739_call = mutated_mod.get_global_var('func_6739')
call_8067 = func_6737_call()
call_8068 = func_6737_call()
func_2042_call = mod.get_global_var('func_2042')
func_2046_call = mutated_mod.get_global_var('func_2046')
var_8073 = relay.var("var_8073", dtype = "int8", shape = (72,))#candidate|8073|(72,)|var|int8
call_8072 = relay.TupleGetItem(func_2042_call(relay.reshape(var_8073.astype('int8'), [72,]), relay.reshape(var_8073.astype('int8'), [72,]), ), 2)
call_8074 = relay.TupleGetItem(func_2046_call(relay.reshape(var_8073.astype('int8'), [72,]), relay.reshape(var_8073.astype('int8'), [72,]), ), 2)
output = relay.Tuple([call_8067,call_8072,var_8073,])
output2 = relay.Tuple([call_8068,call_8074,var_8073,])
func_8075 = relay.Function([var_8073,], output)
mod['func_8075'] = func_8075
mod = relay.transform.InferType()(mod)
var_8076 = relay.var("var_8076", dtype = "int8", shape = (72,))#candidate|8076|(72,)|var|int8
output = func_8075(var_8076)
func_8077 = relay.Function([var_8076], output)
mutated_mod['func_8077'] = func_8077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2630_call = mod.get_global_var('func_2630')
func_2631_call = mutated_mod.get_global_var('func_2631')
call_8085 = relay.TupleGetItem(func_2630_call(), 0)
call_8086 = relay.TupleGetItem(func_2631_call(), 0)
uop_8094 = relay.acosh(call_8085.astype('float64')) # shape=(1, 2, 2)
uop_8096 = relay.acosh(call_8086.astype('float64')) # shape=(1, 2, 2)
output = relay.Tuple([uop_8094,])
output2 = relay.Tuple([uop_8096,])
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
	relay.transform.Inline(),
	relay.transform.LambdaLift(),
	relay.transform.LazyGradientInit(),
	relay.transform.PartialEvaluate(),
	relay.transform.Legalize(),
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
