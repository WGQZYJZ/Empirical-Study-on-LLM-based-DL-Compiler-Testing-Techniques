import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_24 = relay.var("var_24", dtype = "bool", shape = (11, 10, 8))#candidate|24|(11, 10, 8)|var|bool
var_25 = relay.var("var_25", dtype = "bool", shape = (11, 10, 8))#candidate|25|(11, 10, 8)|var|bool
bop_26 = relay.logical_and(var_24.astype('bool'), relay.reshape(var_25.astype('bool'), relay.shape_of(var_24))) # shape=(11, 10, 8)
uop_49 = relay.exp(var_24.astype('float64')) # shape=(11, 10, 8)
output = relay.Tuple([bop_26,uop_49,])
output2 = relay.Tuple([bop_26,uop_49,])
func_54 = relay.Function([var_24,var_25,], output)
mod['func_54'] = func_54
mod = relay.transform.InferType()(mod)
var_55 = relay.var("var_55", dtype = "bool", shape = (11, 10, 8))#candidate|55|(11, 10, 8)|var|bool
var_56 = relay.var("var_56", dtype = "bool", shape = (11, 10, 8))#candidate|56|(11, 10, 8)|var|bool
output = func_54(var_55,var_56,)
func_57 = relay.Function([var_55,var_56,], output)
mutated_mod['func_57'] = func_57
mutated_mod = relay.transform.InferType()(mutated_mod)
const_181 = relay.const([[[9.677163,-4.501115,3.866891,5.850102,-7.017448,6.259523,-3.445607,3.786036,7.942796,-8.747982,-5.044265,-2.852209,4.321012,-5.241316,-4.726231]],[[-8.156653,1.184298,-9.121793,-6.146905,2.873906,6.783715,-3.966081,-2.146138,1.610333,0.242484,8.946948,-3.412846,-8.788732,1.667919,4.028165]],[[-3.522471,4.248617,-9.459303,-7.566304,-6.387036,7.485179,-0.894291,0.301778,-8.257755,6.382002,-9.428803,6.043000,-1.486321,7.376973,-0.292233]],[[8.318448,-4.766813,-2.109500,-6.242958,7.061489,8.481290,-3.790646,9.115594,-5.112998,-1.313879,9.817940,-7.162835,8.556173,-5.429172,-7.138674]],[[1.039948,6.890706,8.417091,4.372897,-2.079536,-0.837580,1.583399,-9.329661,-1.442874,-4.309273,-3.766016,-1.547463,9.104418,0.857063,-8.818909]],[[-8.129878,8.485682,8.448223,-8.768138,-2.748284,-6.459861,-3.088643,3.989159,-6.838466,0.170193,-0.658477,-6.963171,-6.567183,-5.219269,6.797977]],[[1.391925,8.322830,1.096714,1.799915,8.802277,-9.672314,-1.614506,9.331536,9.789463,-4.383084,0.190898,-2.446799,8.070868,6.192815,-5.887784]],[[-3.300340,-4.794734,-8.539878,-8.948604,1.383408,0.036274,8.854141,-4.506732,0.843896,-6.010662,-8.716805,-5.144595,3.454841,9.022600,-3.121592]],[[5.741769,-5.773224,-6.700769,0.542745,-8.929704,-3.514816,2.516754,-8.794312,-4.815462,5.053839,8.985250,-7.571527,3.751690,8.765435,-6.373534]],[[-7.392857,-0.301962,-4.986290,-0.954049,4.562292,-8.852436,-7.478785,-6.711801,-9.105265,9.965279,0.328256,4.365490,-4.701126,-2.193361,-5.992958]],[[3.076792,-0.351042,3.769365,-3.907901,0.826552,-9.558263,0.560796,1.786293,3.121707,4.400307,7.964097,3.944642,-1.857438,7.629689,0.659642]],[[-4.939261,1.073343,-7.512499,4.186244,-1.117709,8.083385,-5.353913,5.179862,-5.236414,1.598728,5.971006,-3.643041,-7.766593,9.781273,9.785528]],[[9.435790,5.656667,3.563178,4.275638,5.649530,3.017629,-2.224397,4.956206,7.978391,8.767796,7.338758,4.531777,3.474077,8.254784,-6.164784]],[[-4.450721,-3.222615,-1.984394,4.868446,-6.013421,8.768567,2.654995,2.747275,8.806103,-4.088156,-6.008013,-9.674699,-1.372090,8.560349,-1.746955]]], dtype = "float32")#candidate|181|(14, 1, 15)|const|float32
uop_182 = relay.sin(const_181.astype('float32')) # shape=(14, 1, 15)
output = relay.Tuple([uop_182,])
output2 = relay.Tuple([uop_182,])
func_188 = relay.Function([], output)
mod['func_188'] = func_188
mod = relay.transform.InferType()(mod)
output = func_188()
func_189 = relay.Function([], output)
mutated_mod['func_189'] = func_189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_198 = relay.TupleGetItem(func_188_call(), 0)
call_199 = relay.TupleGetItem(func_189_call(), 0)
output = relay.Tuple([call_198,])
output2 = relay.Tuple([call_199,])
func_209 = relay.Function([], output)
mod['func_209'] = func_209
mod = relay.transform.InferType()(mod)
output = func_209()
func_210 = relay.Function([], output)
mutated_mod['func_210'] = func_210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_236 = relay.TupleGetItem(func_188_call(), 0)
call_237 = relay.TupleGetItem(func_189_call(), 0)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_250 = relay.TupleGetItem(func_209_call(), 0)
call_251 = relay.TupleGetItem(func_210_call(), 0)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_261 = relay.TupleGetItem(func_209_call(), 0)
call_262 = relay.TupleGetItem(func_210_call(), 0)
bop_276 = relay.divide(call_250.astype('float32'), relay.reshape(call_261.astype('float32'), relay.shape_of(call_250))) # shape=(14, 1, 15)
bop_279 = relay.divide(call_251.astype('float32'), relay.reshape(call_262.astype('float32'), relay.shape_of(call_251))) # shape=(14, 1, 15)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_287 = relay.TupleGetItem(func_188_call(), 0)
call_288 = relay.TupleGetItem(func_189_call(), 0)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_295 = relay.TupleGetItem(func_209_call(), 0)
call_296 = relay.TupleGetItem(func_210_call(), 0)
output = relay.Tuple([call_236,bop_276,call_287,call_295,])
output2 = relay.Tuple([call_237,bop_279,call_288,call_296,])
func_303 = relay.Function([], output)
mod['func_303'] = func_303
mod = relay.transform.InferType()(mod)
output = func_303()
func_304 = relay.Function([], output)
mutated_mod['func_304'] = func_304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_330 = relay.TupleGetItem(func_303_call(), 0)
call_331 = relay.TupleGetItem(func_304_call(), 0)
output = call_330
output2 = call_331
func_335 = relay.Function([], output)
mod['func_335'] = func_335
mod = relay.transform.InferType()(mod)
output = func_335()
func_336 = relay.Function([], output)
mutated_mod['func_336'] = func_336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_372 = func_335_call()
call_373 = func_335_call()
output = call_372
output2 = call_373
func_388 = relay.Function([], output)
mod['func_388'] = func_388
mod = relay.transform.InferType()(mod)
mutated_mod['func_388'] = func_388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_388_call = mutated_mod.get_global_var('func_388')
call_389 = func_388_call()
output = call_389
func_390 = relay.Function([], output)
mutated_mod['func_390'] = func_390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_393 = func_335_call()
call_394 = func_335_call()
output = call_393
output2 = call_394
func_421 = relay.Function([], output)
mod['func_421'] = func_421
mod = relay.transform.InferType()(mod)
output = func_421()
func_422 = relay.Function([], output)
mutated_mod['func_422'] = func_422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_442 = relay.TupleGetItem(func_209_call(), 0)
call_443 = relay.TupleGetItem(func_210_call(), 0)
var_451 = relay.var("var_451", dtype = "float32", shape = (14, 8, 15))#candidate|451|(14, 8, 15)|var|float32
bop_452 = relay.minimum(call_442.astype('int8'), var_451.astype('int8')) # shape=(14, 8, 15)
bop_455 = relay.minimum(call_443.astype('int8'), var_451.astype('int8')) # shape=(14, 8, 15)
uop_457 = relay.acos(bop_452.astype('float64')) # shape=(14, 8, 15)
uop_459 = relay.acos(bop_455.astype('float64')) # shape=(14, 8, 15)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_462 = relay.TupleGetItem(func_303_call(), 2)
call_463 = relay.TupleGetItem(func_304_call(), 2)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_466 = relay.const([False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True], dtype = "bool")#candidate|466|(880,)|const|bool
call_465 = relay.TupleGetItem(func_54_call(relay.reshape(const_466.astype('bool'), [11, 10, 8]), relay.reshape(const_466.astype('bool'), [11, 10, 8]), ), 1)
call_467 = relay.TupleGetItem(func_57_call(relay.reshape(const_466.astype('bool'), [11, 10, 8]), relay.reshape(const_466.astype('bool'), [11, 10, 8]), ), 1)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_475 = func_421_call()
call_476 = func_421_call()
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_482 = func_421_call()
call_483 = func_421_call()
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_489 = relay.TupleGetItem(func_188_call(), 0)
call_490 = relay.TupleGetItem(func_189_call(), 0)
output = relay.Tuple([uop_457,call_462,call_465,const_466,call_475,call_482,call_489,])
output2 = relay.Tuple([uop_459,call_463,call_467,const_466,call_476,call_483,call_490,])
func_497 = relay.Function([var_451,], output)
mod['func_497'] = func_497
mod = relay.transform.InferType()(mod)
mutated_mod['func_497'] = func_497
mutated_mod = relay.transform.InferType()(mutated_mod)
var_498 = relay.var("var_498", dtype = "float32", shape = (14, 8, 15))#candidate|498|(14, 8, 15)|var|float32
func_497_call = mutated_mod.get_global_var('func_497')
call_499 = func_497_call(var_498)
output = call_499
func_500 = relay.Function([var_498], output)
mutated_mod['func_500'] = func_500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_543 = relay.TupleGetItem(func_303_call(), 0)
call_544 = relay.TupleGetItem(func_304_call(), 0)
output = call_543
output2 = call_544
func_579 = relay.Function([], output)
mod['func_579'] = func_579
mod = relay.transform.InferType()(mod)
output = func_579()
func_580 = relay.Function([], output)
mutated_mod['func_580'] = func_580
mutated_mod = relay.transform.InferType()(mutated_mod)
var_588 = relay.var("var_588", dtype = "float64", shape = (9, 4, 1))#candidate|588|(9, 4, 1)|var|float64
uop_589 = relay.erf(var_588.astype('float64')) # shape=(9, 4, 1)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_591 = relay.TupleGetItem(func_188_call(), 0)
call_592 = relay.TupleGetItem(func_189_call(), 0)
output = relay.Tuple([uop_589,call_591,])
output2 = relay.Tuple([uop_589,call_592,])
func_602 = relay.Function([var_588,], output)
mod['func_602'] = func_602
mod = relay.transform.InferType()(mod)
var_603 = relay.var("var_603", dtype = "float64", shape = (9, 4, 1))#candidate|603|(9, 4, 1)|var|float64
output = func_602(var_603)
func_604 = relay.Function([var_603], output)
mutated_mod['func_604'] = func_604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_626 = func_579_call()
call_627 = func_579_call()
output = call_626
output2 = call_627
func_630 = relay.Function([], output)
mod['func_630'] = func_630
mod = relay.transform.InferType()(mod)
output = func_630()
func_631 = relay.Function([], output)
mutated_mod['func_631'] = func_631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_646 = func_388_call()
call_647 = func_388_call()
uop_655 = relay.sigmoid(call_646.astype('float64')) # shape=(14, 1, 15)
uop_657 = relay.sigmoid(call_647.astype('float64')) # shape=(14, 1, 15)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_659 = func_579_call()
call_660 = func_579_call()
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_666 = func_388_call()
call_667 = func_388_call()
var_668 = relay.var("var_668", dtype = "float64", shape = (14, 16, 15))#candidate|668|(14, 16, 15)|var|float64
bop_669 = relay.subtract(uop_655.astype('float64'), var_668.astype('float64')) # shape=(14, 16, 15)
bop_672 = relay.subtract(uop_657.astype('float64'), var_668.astype('float64')) # shape=(14, 16, 15)
output = relay.Tuple([call_659,call_666,bop_669,])
output2 = relay.Tuple([call_660,call_667,bop_672,])
func_674 = relay.Function([var_668,], output)
mod['func_674'] = func_674
mod = relay.transform.InferType()(mod)
var_675 = relay.var("var_675", dtype = "float64", shape = (14, 16, 15))#candidate|675|(14, 16, 15)|var|float64
output = func_674(var_675)
func_676 = relay.Function([var_675], output)
mutated_mod['func_676'] = func_676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_780 = func_388_call()
call_781 = func_388_call()
output = call_780
output2 = call_781
func_782 = relay.Function([], output)
mod['func_782'] = func_782
mod = relay.transform.InferType()(mod)
mutated_mod['func_782'] = func_782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mutated_mod.get_global_var('func_782')
call_783 = func_782_call()
output = call_783
func_784 = relay.Function([], output)
mutated_mod['func_784'] = func_784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_810 = relay.TupleGetItem(func_303_call(), 0)
call_811 = relay.TupleGetItem(func_304_call(), 0)
var_826 = relay.var("var_826", dtype = "float32", shape = (14, 11, 15))#candidate|826|(14, 11, 15)|var|float32
bop_827 = relay.logical_and(call_810.astype('bool'), var_826.astype('bool')) # shape=(14, 11, 15)
bop_830 = relay.logical_and(call_811.astype('bool'), var_826.astype('bool')) # shape=(14, 11, 15)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
var_845 = relay.var("var_845", dtype = "bool", shape = (880,))#candidate|845|(880,)|var|bool
call_844 = relay.TupleGetItem(func_54_call(relay.reshape(var_845.astype('bool'), [11, 10, 8]), relay.reshape(var_845.astype('bool'), [11, 10, 8]), ), 1)
call_846 = relay.TupleGetItem(func_57_call(relay.reshape(var_845.astype('bool'), [11, 10, 8]), relay.reshape(var_845.astype('bool'), [11, 10, 8]), ), 1)
uop_851 = relay.cosh(bop_827.astype('float64')) # shape=(14, 11, 15)
uop_853 = relay.cosh(bop_830.astype('float64')) # shape=(14, 11, 15)
output = relay.Tuple([call_844,var_845,uop_851,])
output2 = relay.Tuple([call_846,var_845,uop_853,])
func_864 = relay.Function([var_826,var_845,], output)
mod['func_864'] = func_864
mod = relay.transform.InferType()(mod)
mutated_mod['func_864'] = func_864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_864_call = mutated_mod.get_global_var('func_864')
var_866 = relay.var("var_866", dtype = "float32", shape = (14, 11, 15))#candidate|866|(14, 11, 15)|var|float32
var_867 = relay.var("var_867", dtype = "bool", shape = (880,))#candidate|867|(880,)|var|bool
call_865 = func_864_call(var_866,var_867,)
output = call_865
func_868 = relay.Function([var_866,var_867,], output)
mutated_mod['func_868'] = func_868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_916 = relay.TupleGetItem(func_209_call(), 0)
call_917 = relay.TupleGetItem(func_210_call(), 0)
output = relay.Tuple([call_916,])
output2 = relay.Tuple([call_917,])
func_918 = relay.Function([], output)
mod['func_918'] = func_918
mod = relay.transform.InferType()(mod)
mutated_mod['func_918'] = func_918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mutated_mod.get_global_var('func_918')
call_919 = func_918_call()
output = call_919
func_920 = relay.Function([], output)
mutated_mod['func_920'] = func_920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_929 = func_421_call()
call_930 = func_421_call()
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_933 = relay.const([True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,False,True], dtype = "bool")#candidate|933|(880,)|const|bool
call_932 = relay.TupleGetItem(func_54_call(relay.reshape(const_933.astype('bool'), [11, 10, 8]), relay.reshape(const_933.astype('bool'), [11, 10, 8]), ), 1)
call_934 = relay.TupleGetItem(func_57_call(relay.reshape(const_933.astype('bool'), [11, 10, 8]), relay.reshape(const_933.astype('bool'), [11, 10, 8]), ), 1)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
const_938 = relay.const([0.717495,2.861434,-5.225424,-1.921401,1.962787,-3.206643,8.821686,2.939319,-1.062480,-5.168820,-0.071150,7.612933,9.277831,0.515690,-8.958394,4.770927,-4.004219,-4.357268,-7.380537,1.665039,3.914337,-6.511454,7.494261,-6.660887,4.549540,2.803075,7.313574,3.598772,-5.968565,9.246686,3.756794,-3.451487,-7.614732,3.130858,6.474318,-2.380507,-0.060315,-5.033927,-8.406935,2.019266,1.470743,3.088918,0.997785,0.740675,8.014484,-7.722699,-4.783598,-4.966493,6.780772,0.659634,-4.102520,4.423754,2.626471,-2.540229,2.373436,6.337976,-2.853154,8.972558,-4.049505,1.167607,-0.325638,-7.458774,7.210111,9.862711,-7.143472,3.455708,-6.178671,3.823388,-8.322976,-8.847879,6.818570,-9.656319,-1.031246,-4.534448,6.695775,9.243741,3.868412,-8.716588,-6.571244,-9.209183,-0.346923,-1.144983,-0.118314,-6.880095,0.802848,-9.451962,9.792137,0.362723,3.728955,-4.970654,7.806597,-3.107427,8.612553,5.473675,-6.855218,4.170023,-9.895350,2.791567,6.546938,4.932694,-5.667307,-5.845523,8.772367,-2.110691,3.448573,8.382318,-9.896126,3.303883,-0.163141,1.277310,-9.173275,9.709373,-1.983540,-9.586691,0.656481,4.898546,1.599128,5.440816,5.461113,8.187366,-9.152388,7.350441,-2.354368,-6.338091,-2.617835,1.611894,-9.606020,4.946553,-4.907741,1.636542,9.764700,0.708644,-3.619413,8.588675,-6.583987,-5.846699,8.423422,5.213711,-6.763612,-8.341508,-2.495303,-1.176556,3.755690,5.820040,4.112905,6.930557,3.919878,5.581516,8.062014,6.794861,-6.248393,-5.409179,-3.658447,9.242007,1.039357,9.168526,-2.010302,1.567096,9.835197,4.719998,5.218137,9.616487,3.598356,-0.330030,-8.704535,1.258573,7.395356,-1.890483,9.712989,-4.406076,-7.608730,-2.286113,8.890279,-3.879061,0.440878,4.059343,-1.090889,5.537695,-3.018520,-7.862450,-1.815455,1.345123,6.762710,2.634666,0.104660,4.740864,1.079846,-8.542898,2.608440,9.941405,-6.668876,0.915329,5.023986,5.662323,-2.950099,-3.232392,2.018778,-3.437609,-7.466893,0.016033,-1.967188,1.537450,3.469628,-0.270057,-7.784632,7.832176,6.692781,7.973383,6.482119,-8.801442,-5.073536,-4.670919,-4.751767,-5.746007,-3.840546,-6.461197,-7.080161,-4.114277,-8.063481,9.717427,-5.990632,5.141967,0.229177,4.290302,1.312011,3.553720,-6.739374,9.048069,-5.360113,0.935252,-5.952815,5.030802,0.579392,-6.325927,4.396347,-1.151318,-1.052521,1.964067,-5.087176,-7.515795,-2.037865,1.774280,-7.598304,5.829909,-6.327633,6.377887,-2.781588,-2.250582,4.853318,0.094668,-8.818971,-3.942718,-5.260522,-4.026060,-7.267587,-6.127731,-9.348011,-3.674020,6.416052,-6.591884,-1.246841,-1.007617,-8.201327,1.462043,3.320839,-8.494680,-3.352632,-2.878926,-5.382130,-3.729512,6.839364,1.351305,-9.769486,-7.667617,8.167532,-4.561225,7.866246,9.173604,9.063768,6.861083,8.617172,-3.238487,-0.308091,-4.447139,9.713014,-9.069044,-8.357091,3.441966,2.247372,-1.747824,-5.743045,-0.689307,7.391087,2.117159,-7.006762,0.608415,5.122413,-9.987245,-9.353457,-1.462189,2.042577,-2.328825,9.082449,-3.632024,-9.073488,5.915444,6.106122,-9.309376,0.527584,0.565749,-4.046605,-5.624184,-3.898147,5.249502,1.982617,1.704094,-2.561564,-0.852914,6.673730,-4.497054,5.221146,-6.203279,-5.510316,1.006306,-4.860781,4.968796,6.472756,-5.494741,-9.929664,-6.321383,-8.407575,-1.946617,-8.082192,-6.307188,-5.985205,9.809098,-2.039047,-5.040457,-4.252475,1.989719,8.456512,4.205723,-0.016244,-1.350474,4.132909,-4.887376,-5.740316,5.285593,-8.471727,-8.940266,-9.635277,-2.208981,4.168234,9.901602,5.094612,4.594322,-6.694938,6.791286,-8.067317,2.536078,2.875498,6.303361,6.463094,-0.587226,-2.877458,-3.335931,-1.327060,-0.125805,8.691986,6.312419,-0.076780,4.138971,2.123310,7.656461,3.256645,8.256546,-8.501862,-8.853643,1.740362,9.336848,-5.080385,4.721301,1.848910,-6.544336,7.034329,5.907655,-8.554338,-0.005525,8.807435,-9.556250,9.693314,4.625161,-2.555978,5.451152,-9.761300,-1.772113,-0.069573,3.000271,3.963807,-8.351677,7.298408,-3.798290,7.283539,0.350096,-5.900322,9.150148,-0.170145,8.211761,-2.883871,-4.021333,-9.160756,5.621228,-0.243377,-4.299758,8.296404,2.326554,-5.414724,-7.486475,-5.732184,-8.910213,0.941621,-2.252552,9.349838,6.643160,-1.968454,-8.959322,-4.121172,1.390188,3.890471,-8.590664,4.149969,4.004991,3.366450,1.740969,-1.767381,-1.319093,1.825547,6.106211,-3.271521,-0.776655,-9.253617,1.362940,9.425221,-5.605954,-4.103051,8.367277,-8.125181,6.313593,-8.038991,0.897673,5.923363,0.349998,5.686711,2.059771,9.740240,-2.572723,-4.152617,-1.143217,8.870961,-6.777863,6.299766,7.483976,9.294910,9.399318,2.332649,-3.038578,-7.882175,8.753790,-7.568246,3.467686,-6.821032,8.665595,-5.018449,-6.629483,-5.181728,2.593319,-5.463572,4.421650,-0.918423,-4.516703,-9.181407,-3.011746,-7.902186,-0.887793,-7.805978,-9.994667,7.541279,3.238892,4.381213,8.681859,5.175898,7.185299,5.337880,6.258381,2.024150,5.500647,-6.404504,-7.156936,5.546100,1.688505,-6.308883,5.563851,2.866661,1.004523,-1.303861,6.377376,-0.778775,-6.824386,2.909923,3.872694,1.201664,-5.551358,-7.969248,-9.946752,0.443104,4.905210,7.857879,-0.232094,4.022699,1.140013,-3.288790,2.835051,9.469593,1.690398,5.898182,9.636833,2.136249,-5.019862,-5.771799,-9.275303,-8.584948,9.093822,-8.310332,5.784578,-4.296527,2.484048,9.147021,0.711576,-3.376572,5.164946,4.299800,-1.304049,8.254713,-2.695880,0.989334,6.242703,-3.401651,6.960030,-3.715386,-7.900850,3.362816,-7.619371,0.612948,2.475732,-7.233226,9.706253,9.995792,-3.425111,4.884235,-5.549508,6.951322,-8.010526,5.988375,-3.183769,-6.684606,-0.201870,3.982623,-0.275560,-4.952678,-0.595530,2.340901,-4.465472,-2.720598,6.712512,4.590059,-4.374558,0.023722,-1.821689,8.415233,5.374854,8.065793,1.921066,-8.117029,6.471808,-8.037758,5.757991,-2.299587,-9.170887,-1.763947,-7.614614,-3.467134,1.706204,0.116782,-5.476093,-5.108254,5.531922,7.742737,-5.928946,-2.640353,-5.476861,-2.705483,-3.386324,2.028104,7.489040,-5.330619,5.302677,-5.918446,2.449529,-5.669597,-9.291831,2.624529,-6.159634,6.445284,-3.837121,2.397851,-9.221378,-4.440551,-0.142927,9.826494,5.553108,9.313058,-5.273910,7.311199,3.617205,7.496282,5.918325,2.282413,9.624729,-3.718787,0.053177,-6.594947,2.391283,-6.514345,-6.924198,2.516613,-8.895566,-1.878089,9.619752,-3.924735,1.285616,-4.700915,-3.648307,9.178569,-1.593565,2.372394,6.463448,8.198249,-8.569678,-7.550819,-0.834063,-4.676295,-2.771383,1.435433,2.099408,-8.668403,-7.030815,6.867303,3.001363,-4.351547,-5.496543,1.732108,-5.445613,8.049397,-8.236982,4.389029,2.945368,1.029194,8.647493,9.138355,-0.051482,0.553507,0.514457,9.275531,6.673498,-7.947099,4.814746,5.154805,7.583267,-2.750725,-9.251273,-8.063362,-9.059623,6.538430,-4.762714,-8.186806,5.337859,3.179997,-1.222330,7.805374,9.549718,7.298379,2.224633,-2.193033,0.945689,-8.801676,-2.088679,-9.295752,7.421494,-9.714905,-4.501338,-1.425351,4.395382,-9.501306,9.046672,4.653894,-7.914699,4.042759,-9.006305,-1.844092,3.404242,9.839456,5.676954,-2.651932,-5.471364,-1.485344,6.336240,-1.670537,5.491085,-7.149944,-2.585078,0.170327,-1.551223,-3.416103,-7.540940,2.667634,4.611616,7.386987,-6.657425,8.955061,5.057261,0.972825,3.069180,6.851527,2.943657,7.240001,4.813438,-5.437165,7.013908,-4.718609,7.913452,3.845962,5.595087,7.744962,-3.274362,-9.714909,-6.350935,-6.669919,0.439846,-2.742657,9.950729,-3.892076,-0.792377,9.804634,4.387793,2.003685,0.997260,5.471160,-4.124814,-6.063459,-4.766783,-0.264269,-3.909101,-1.142649,-6.244077,-0.596027,-0.331120,-7.848943,2.396947,-5.604735,-2.231825,2.127068,5.524850,-5.467207,6.145906,-4.770465,6.496910,7.233340,-0.481338,7.929610,-9.915142,-2.725847,-7.644303,-2.955907,-9.061698,-0.911774,-2.952187,-6.785316,-9.365656,8.349285,6.899046,3.677557,-9.684028,0.830118,-1.699196,7.485271,-7.107173,8.936569,1.815232,6.662817,5.845447,-3.742489,2.975496,6.213599,0.322982,-1.718499,-1.433592,2.349220,-5.980179,7.706711,6.536729,5.700818,4.075147,-8.279244,-3.027512,-1.113041,6.683876,-7.085546,-9.130677,-4.930179,-7.839024,-3.265907,2.041259,-6.166440,-4.865410,-3.533842,-8.115893,-6.992159,4.526459,-7.674442,-1.156029,4.706478,4.956951,-2.549205,6.640103,6.143477,4.876074,-5.194288,5.520847,-9.143687,1.856605,6.662825,4.099983,3.208386,-1.476011,-6.820802,-5.413454,-1.137814,5.746365,0.218125,-5.866933,1.303710,0.731958,-7.696527,-4.758665,-8.126869,0.125509,4.779471,3.980071,0.576670,0.834090,-4.347377,1.652521,1.962897,-0.138576,8.065054,-5.462480,-1.188469,4.581105,-2.423364,-8.357433,1.958325,6.216327,-7.817045,6.606315,-4.408840,3.908196,-2.992230,-2.021471,-7.476379,9.647772,1.243551,-0.944371,3.908750,-7.110295,8.780218,-2.311998,-8.369469,7.715175,9.173582,0.512763,7.697332,-4.386581,9.873810,-5.162919,5.668084,-0.225776,2.841293,3.863307,-2.160464,-8.456719,-3.245256,-2.302329,-0.875943,5.109952,-0.389793,-4.960520,4.539688,9.045087,7.548465,-7.245104,9.760683,0.611823,0.890067,0.113016,-2.946266,8.036874,4.087062,8.863623,-5.111275,2.090534,6.414762,-1.313434,-2.597624,-5.990531,8.817777,0.278618,8.783219,3.624599,7.296770,-1.636860,1.570402,-2.340027,4.269490,-4.570012,-3.182909,-1.256051,1.528279,-5.713019,-1.514189,7.731490,-2.409700,1.669648,5.600502,-8.115567,9.028520,-6.840516,4.695028,1.921696,2.026082,-8.907738,8.387345,8.083322,4.926039,8.492656,-9.828009,-2.583985,7.642217,-0.764730,-0.124679,1.161428,4.463749,-0.999669,-9.637861,1.187642,-1.579445,9.999344,-6.331494,-1.042770,-6.855238,-2.663899,5.406918,0.421075,-3.518218,9.221268,4.870872,-5.710182,6.097363,3.839468,4.992991,1.589691,-6.958371,0.005806,7.914222,-7.894827,5.562838,6.869292,6.367741,4.857161,-6.273299,2.219023,8.159633,9.190700,-5.320082,-9.051221,4.987761,8.576767,-4.316876,2.321391,7.355668,-3.615889,-8.988344,3.756160,-4.222795,2.767739,1.230324,-5.204737,-5.579481,0.380425,-1.165593,-7.692538,3.747227,0.138336,8.079525,-3.477492,4.569637,1.996166,-1.516526,1.596222,-7.899032,2.116934,6.265448,-0.773694,0.830374,0.995330,-3.293582,-8.497856,1.670616,4.960001,-1.744350,9.198723,-9.432148,1.367526,3.672393,-0.866825,1.077226,-1.510886,8.979962,-0.427569,-6.168475,9.211767,-3.079054,3.669402,4.674646,-2.182322,-2.514102,2.012703,-5.958803,6.508603,-3.810373,8.291683,7.812883,-4.397867,6.426871,-8.232670,-3.036740,-4.018197,7.177394,3.063526,-3.787192,-9.731588,3.515816,-9.615468,-1.432302,-7.574488,1.618928,-0.454177,0.105596,8.855418,8.636636,-1.741290,6.780460,-2.297679,-7.939140,-1.923008,2.256076,1.628780,-2.941035,4.918419,6.969919,6.233927,7.588973,-2.802137,7.553727,2.838859,2.870454,-0.527991,-0.102858,1.168359,-5.915880,-0.341102,-3.080535,9.021968,4.063147,5.485582,-2.607066,9.788293,-2.594623,-2.646658,9.413548,-3.266123,0.205095,-2.658609,-2.722925,7.517392,1.236991,-8.186239,4.483734,-8.989417,-1.147994,-2.210121,4.136886,6.496888,3.141043,7.013718,8.252178,1.347933,-2.918979,2.711483,8.608345,-6.681731,-8.397553,-6.901829,-2.608375,-4.094049,-1.681104,7.460130,-5.890118,9.740572,-0.353626,-4.519386,-0.107050,-7.246278,3.026317,2.163968,-9.482457,7.149787,5.828896,8.161484,4.779535,-0.802893,-6.186327,4.308174,-3.441692,-9.158279,3.719582,9.137139,-0.725729,-1.358659,3.559742,-2.212380,8.935841,-2.107191,4.454344,-1.139933,5.244241,-3.039663,-1.303143,-9.701739,-4.450080,8.223310,2.589926,0.040946,3.272330,-8.127206,-1.502695,-8.177470,-8.984851,-4.706508,-3.407496,-2.762465,8.037016,3.207558,-1.594502,5.645692,-8.631822,-3.582570,8.161832,8.064798,-1.562268,0.699364,-4.085017,-6.636105,-3.270733,-8.062798,-0.769618,-7.308252,8.629014,3.866071,8.539599,-4.300397,-1.173359,6.538402,2.052231,-7.756556,-7.131273,-5.375574,7.752653,-6.386585,1.259339,3.717751,6.320188,9.033059,5.150126,8.654653,8.205751,2.671116,-8.007976,2.297358,7.649456,2.330942,3.493333,5.173654,8.270303,-4.012559,-0.134002,-6.105219,3.636659,9.408614,-6.551133,2.297452,-0.038696,7.248583,-4.338047,-7.888851,-6.317222,0.443930,7.423889,2.448155,-3.450188,2.540903,2.962272,4.071980,-8.564271,6.635043,9.701554,-4.343829,7.867099,-3.817393,8.139721,-2.523975,2.032304,0.045488,-2.172778,7.331667,2.911852,4.815061,-1.648989,9.868733,8.941681,6.988645,-5.636322,0.858462,-3.517529,4.646654,-6.178824,8.722918,7.105894,3.702861,8.012581,8.163988,8.041445,2.639588,4.729520,-9.299417,-6.443386,3.974867,-9.177689,-8.919109,-4.917053,-3.979191,7.024684,-3.446258,-9.402738,-1.375732,-0.943872,-9.711608,0.156597,2.841944,7.334723,4.229997,-0.626946,-5.857568,3.353535,8.696208,-1.184792,3.162700,3.526827,-7.563641,6.517321,-4.967691,-8.615028,6.597377,-8.285335,-3.853536,8.054363,9.299872,-4.443359,-9.400276,9.242370,-5.659991,2.879003,7.222898,8.131307,-1.819473,0.174562,2.270308,-9.569733,2.905835,5.795039,-1.635505,6.165802,-1.025708,7.281014,-6.317098,-7.116120,-3.520976,-0.604956,8.997043,3.152147,-7.386558,-1.260965,3.837821,-8.430373,6.791811,-1.866072,-0.027509,-5.841713,-7.306568,1.056474,-9.482801,2.206615,8.636360,-0.783322,2.027816,2.837897,-8.015408,1.874938,-2.709383,-1.320605,-8.300759,7.710437,3.179004,2.620743,4.877913,-5.653269,0.822916,-1.316195,6.911114,3.673547,-6.117604,-8.684311,-4.215020,-4.160249,5.844758,-5.447751,-1.076721,1.654535,2.274840,1.700324,5.589512,-2.347001,7.092335,-3.716127,-1.463196,7.180880,-7.248954,9.635081,-4.124691,6.599818,5.086004,1.847547,5.907726,0.118009,4.053919,0.898725,-6.305590,2.201386,-8.288236,-3.478437,9.156212,2.733572,1.048586,-7.773939,5.807933,5.084182,-4.412712,-8.795596,0.526622,-1.694028,-8.407036,-7.447538,-0.567475,-4.933931,8.244967,1.647197,-1.198812,-0.454866,4.148203,5.117163,-5.592493,7.222798,3.907584,-4.128800,6.378718,-8.294305,-8.231584,-5.561358,-4.074631,3.404214,6.443237,6.387204,1.311673,3.694987,-6.265313,5.878380,-2.204099,3.979022,-4.407243,-7.128390,4.027563,9.225091,2.994996,-1.522432,-3.625838,8.520904,-5.789067,-1.653759,-6.574480,-9.702562,-9.149754,2.731419,2.933828,4.069323,-0.010294,0.687917,-7.061075,5.256982,1.576377,4.698308,8.585421,0.826976,7.904563,-3.269786,-5.622458,4.054872,-6.161895,5.563384,8.951400,-2.046072,-6.905576,9.261032,-7.142292,8.526888,-1.041184,-7.293993,0.618085,8.284320,4.547449,4.751258,1.216436,-8.380890,6.377166,0.185892,-1.778637,0.802870,7.538570,5.384304,5.628630,7.873847,-7.291848,-9.320907,-1.969258,-9.855499,8.718878,6.369372,-6.657777,-1.769570,5.414118,8.522965,4.676201,-8.992518,9.322054,4.714939,-6.886878,2.089303,-3.257366,9.240516,9.905190,-9.737364,3.147907,6.328383,9.568414,3.270171,8.659066,5.703849,3.127334,-3.754085,0.281071,-6.110353,-3.031531,-3.489173,9.380274,3.707626,-5.157924,1.943966,0.387734,7.869593,-6.662142,5.482136,1.256038,1.188490,4.665831,-1.473912,2.519480,-6.783692,-5.867753,-5.826592,-7.944224,-9.659374,2.359044,-9.357584,6.934960,6.195813,6.034075,0.420135,5.848959,8.277911,-3.284005,-9.250580,-1.763814,-0.293833,8.346946,-3.465863,-1.469998,-9.152477,-6.753835,4.295754,0.941416,-0.286964,6.267770,9.420941,-7.227825,4.851335,-8.839360,-5.056746,6.854986,0.198597,6.260259,-4.668348,0.192522,3.456851,-0.214831,8.048673,1.230690,-2.008483,7.238752,-2.622193,-5.365993,6.818188,2.025399,-4.421697,-2.661173,5.227385,6.198656,4.598824,3.544041,2.400422,5.144229,7.648635,-4.217756,-6.216175,8.354536,0.347675,-1.689923,2.013842,-2.572698,-0.929021,6.090650,-2.669411,-3.120242,7.032356,-2.937017,1.158007,7.195887,-6.753956,-6.324829,-0.039139,4.641381,6.334727,-1.782845,4.569906,-7.453247,1.557964,-1.188157,7.381100,9.387868,-0.858660,1.394194,-9.003064,-2.622484,-7.848883,8.904143,-6.423528,-8.132143,-5.982722,-7.922867,9.783904,-0.932215,9.958529,-9.256435,9.115763,2.502070,7.281524,1.892059,-5.845655,-1.054962,-0.511112,9.607298,8.920128,-2.784533,-8.812527,4.012141,-3.191502,-0.397827,-0.228390,-7.076680,-7.406575,3.519960,-1.263780,6.803200,-4.503726,5.946481,3.244795,-4.183434,-4.812460,5.880799,4.976100,-9.528797,-2.233178,3.707907,5.082868,-8.906186,-9.728702,0.010886,-6.890153,1.316549,-9.567417,8.772066,5.776153,-7.838038,-8.407074,-2.369211,4.616891,3.126225,1.814284,-0.043958,-8.456432,-1.587188,8.887340,6.332750,2.355447,-9.864573,4.454453,3.918787,7.298208,-5.017573,2.395202,-8.352478,7.316236,-9.308257,-0.507919,0.733096,6.968836,8.163478,5.372592,-4.650715,9.321394,0.008786,-5.876607,4.759976,-1.548027,-2.026104,-9.978638,-2.456299,-5.544793,-4.613508,-1.963604,-7.150595,-5.979197,-8.339718,-9.937034,-7.934072,5.905379,8.428410,-8.989527,-4.947567,-8.051086,7.551354,8.123486,7.721588,-5.642147,-4.020502,4.549133,6.082032,9.238075,-7.783370,-7.897033,0.512161,-9.565065,-1.242591,-5.055964,8.118902,4.287565,1.838236,0.199580,-5.680331,5.234054,-5.907427,8.395568,-7.512827,5.864649,7.157247,2.420262,0.523172,2.480493,-9.968594,-9.013900,-6.671782,-9.044469,-6.131724,-4.213713,-4.065283,-6.396569,0.220651,-4.595415,-2.850915,-0.945979,5.196552,-6.549365,9.488902,-2.045977,9.435587,5.803694,-9.514501,-3.002634,5.713800,-6.182231,-3.758117,-5.339508,-5.037437,0.625488,-7.711520,-2.265975,2.697197,1.541561,-8.698545,-4.710286,-0.380253,-3.834078,-7.317960,-0.266598,2.759228,8.524124,9.183063,2.275951,-5.467230,-6.712036,-3.828456,-5.842012,7.059084,-2.976071,-4.225142,-7.927073,1.406753,5.230657,3.302532,5.836218,-0.017582,-5.718931,4.752140,-6.984894,-1.430516,-2.167975,5.766348,-6.153953,-4.254145,0.220198,2.778202,-4.407444,-2.615912,-5.426421,9.968608,-8.884967,-7.892916,9.241158,6.871560,6.195095,-7.030591,-6.159243,5.013188,-4.069296,-8.145331,-9.647740,3.394975,-1.440104,-3.466471,4.817871,-4.291386,-3.035714,-9.771213,-8.757408,1.058059,4.734672,-0.358702,4.159619,-7.868385,9.356561,0.398483,8.548592,-8.665392,-1.328558,-1.529832,-3.355509,-3.028160,-4.062744,-6.137076,-1.635729,-8.736642,3.287292,3.084614,-2.265061,0.357591,-2.498387,1.870221,6.740605,4.470050,3.855834,-6.973227,7.233997,-2.390829,5.385260,-6.022806,-1.863699,-1.245271,1.492762,-6.799661,7.416667,-0.130093,3.162827,7.515120,1.361643,-9.327584,5.767455,9.475655,0.610846,-3.695987,-4.771177,-5.855337,2.619094,8.919745,6.568539,9.797097,1.815475,-3.020563,7.772551,9.450668,0.967625,9.213944,-2.479463,7.690855,-5.167089,1.130201,-6.318943,8.951770,-8.669052,4.752180,5.363374,-5.136482,-6.122507,0.752428,2.929133,-6.303403,-9.865714,6.602076,-9.610998,7.593619,-8.095061,-7.213806,-2.845675,-5.811185,-1.365388,-8.688620,-7.415325,-7.232696,-8.493778,8.968756,-3.483344,-7.397378,3.760639,-2.285501,-3.240464,6.292307,-4.453402,1.575707,1.057520,5.846528,7.078921,6.150922,-5.258100,-6.036680,1.954782,-9.126282,-6.271329,3.883960,-9.703398,8.963691,6.836812,4.442859,-5.255970,-3.191522,0.773993,4.136929,-3.852454,-0.485007,-3.074735,4.879527,-7.245069,-3.085792,-9.700785,0.241321,4.219311,1.913659,5.656650,-0.950685,4.460737,3.066636,-3.165876,-7.839869,-0.589960,4.741569,8.060552,-1.320284,5.726996,-8.040742,-8.132926,-9.794681,0.719680,-0.011141,7.906947,-2.812745,-1.187733,5.109998,9.969287,2.342619,-0.885388,-4.911344,6.951976,-3.650197,1.894448,-5.333964,-9.896900,3.579978,-0.555950,-7.352958,-1.321064,-3.873349,-5.589151,9.957163,8.996102,5.372804,-5.627717,-0.420515,7.280229,-3.185315,7.118348,-7.868549,7.735644,8.179759,-5.883011,5.047907,8.972122,6.592570,3.598182,6.963617,2.354428,5.563730,-4.003870,3.003229,-1.927292,8.125537,-6.745226,3.157470,5.033097,2.921569,-8.673207,0.986854,-3.578656,5.561211,6.747677,2.125180,-8.855833,-7.233861,-1.072872,-7.065704,8.344025,-7.807148,7.519475,-9.485015,5.392814,-9.935774,-4.542852,4.184912,-0.561896,2.528830,0.909306,-1.433705,2.765567,-3.608406,-5.580918,-5.160414,-6.071594,0.669745,-1.083605,8.877762,7.543549,7.536846,0.105747,9.331594,5.499898,9.252689,3.748554,-8.170007,6.921330,-2.801540,1.919983,8.567033,9.702326,-3.970837,-6.382785,7.656157,0.779990,-8.327027,7.407715,0.471434,-6.020778,7.225720,-2.569504,-1.118628,7.814650,-5.466584,1.531454,-6.242135,-1.965261,-7.294239,-9.700658,4.190057,-6.998165,-9.323707,8.097212,-1.075304,2.269426,3.616580,-8.220764,0.699021,-0.084037,-9.117411,0.139637,-9.831749,6.547137,3.077775,2.159903,-5.221999,-3.242521,8.781019,-3.733937,5.730423,-7.325052,5.031514,-2.196925,-6.931490,-9.448003,-1.113259,1.290166,-4.548354,3.111303,9.479320,-3.344634,-9.225163,-0.083369,-3.507163,5.997917,-0.969869,-2.455997,-3.349720,-8.952695,2.919434,-8.477670,9.804597,-5.278395,-3.043445,9.539377,-2.203398,2.033359,-0.806510,8.036162,-1.497958,-1.960125,-3.898486,9.032001,2.705710,9.934150,-4.087524,-3.479119,9.297911,5.717791,-0.596065,0.509783,-7.236322,3.210254,4.417984,6.260748,1.079153,-6.938075,-1.677620,6.126682,-8.152696,-5.872448,-4.260105,-2.163091,-2.300842,3.827034,-3.268473,2.474021,-7.188718,8.293610,0.691171,3.648014,-0.136478,-2.004866,8.737964,-7.696300,-7.100835,4.041416,0.946610,8.859902,8.435842,-9.648035,3.258409,3.777623,-3.050391,6.587580,1.819175,-0.014736,2.000113,5.240305,-9.390066,-1.001069,-1.997654,9.934655,7.871205,7.016735,-0.891229,-2.179751,-5.650146,1.121836,-9.708743,-9.061835,0.984943,9.928497,-4.240611,-8.819982,-3.368001,6.943604,-1.845247,-2.637650,7.415076,-7.419792,1.532145,-3.941905,-9.657176,-7.504531,-7.711060,2.525673,0.519632,-9.899613,7.488261,3.597019,6.989468,-6.170703,2.511869,9.435756,4.978746,-4.636717,-9.846914,-9.609568,-4.156125,4.394925,3.483110,2.565254,5.714990,-6.098265,-6.744084,-0.196858,7.074505,1.027380,3.170711,5.749883,-8.798727,0.126084,-9.773244,-7.082956,-5.434486,-7.921560,-4.360181,6.862040,4.228745,-2.896359,9.825614,-3.569874,4.228434,6.207956,-8.542130,9.285054,9.848767,-0.863683,-4.559761,-0.096747,-7.408524,0.549380,-1.298376,4.766877,-6.516849,5.838989,-6.653950,-5.725282,5.066739,1.909288,8.124805,2.179768,1.233331,-2.823910,-5.628188,2.889469,5.258643,4.040610,9.224523,-3.619081,-4.098029,3.168782,7.673545,-7.852819,5.359566,-0.383401,5.309820,8.401335,0.225143,-1.911687,9.591661,2.118089,-5.662949,-7.330661,2.175360,-1.332406,2.080570,-5.402243,6.845727,5.066945,-3.387611,0.702494,6.747349,0.815038,4.546283,-2.960939,7.143017,4.581907,-0.918636,3.789440,-9.512763,9.505991,8.474544,-7.383678,3.079958,7.513915,-9.689664,4.035847,-1.158458,-1.521964,-7.554723,-2.413869,-3.521147,-5.237602,3.753140,-8.160971,7.144710,7.178946,-4.339446,6.986203,-9.942683,2.559824,-4.843089,-4.269775,1.337189,-6.161710,-1.314805,0.283927,-0.139959,3.501229,6.267374,-0.742209,-9.179025,3.935298,5.726723,-1.038346,-2.830146,-7.489044,-7.966581,3.713624,-2.161965,7.560358,-5.285516,6.612753,-8.623201,-4.564823,7.077367,-3.998547,2.563987,-1.602849,5.191994,-4.572712,-1.422783,-5.437775,3.349397,4.075497,1.366449,-2.869359,4.915001,-2.604265,4.163887,-6.078287,2.530907,-4.969905,-2.160970,-6.752469,6.718192,2.648175,6.079030,-6.200201,6.736589,-9.547342,-0.657456,-3.063926,3.115589,-1.648988,-0.066980,2.591842,5.698810,-7.305029,-0.985088,4.036222,0.414024,1.199645,-9.472761,7.245301,7.074669,-8.712142,3.922355,-1.115980,-8.051335,9.795671,9.424886,-0.667107,-8.842097,-0.183259,7.919866,-7.956162,8.023791,-3.480977,2.275031,9.220688,5.174554,-4.222815,3.722620,2.822928,5.099226,-0.689092,1.486486,-6.691103,4.553984,-8.444569,-6.791071,0.817071,0.216388,-7.252621,6.636734,5.707485,3.273370,5.944226,-1.392545,-3.255133,0.272746,-1.354296,-1.542639,-2.659522,-2.010888,-5.065055,0.814098,-2.509060,6.693165,7.926686,-9.178646,-8.625824,0.259244,-3.161105,-3.157798,9.088730,9.954110,9.269608,-4.009556,0.874358,-1.783978,-2.960874,3.947640,-2.824096,9.721997,-0.955786,2.665261,4.900787,-3.861311,-0.930856,1.275028,0.759292,-9.952086,-5.862332,-9.674453,1.091605,5.437718,9.075013,-7.064766,-9.833001,2.515820,6.450118,1.273674,6.013660,4.407968,-1.773749,-7.210926,7.764484,-0.025084,8.521283,-3.019618,-9.838795,-9.125275,-3.612763,5.891120,-4.702033,8.435962,9.008466,6.108222,5.424336,5.788159,2.764514,9.693641,-1.021880,-1.691764,-1.310459,-3.121178,-0.310239,-2.132045,0.126553,3.218287,4.226481,1.527493,5.870689,6.145294,2.001800,5.659873,-7.097119,-8.029208,-9.215415,8.369500,8.830537,2.045372,-6.748295,-9.117096,-9.903157,-7.286608,6.119523,-7.011271,-6.249788,2.230157,-3.066764,-9.032548,1.951767,8.775376,7.956847,-9.449881,-5.365490,-2.231995,-1.008855,-3.683537,4.767411,-6.913957,9.880134,8.552393,-3.680046,4.293205,9.931315,-2.127605,-2.521387,8.124264,-1.938233,-0.867965,9.975453,4.342752,-8.480884,-9.909772,-4.508211,-2.401585,-1.991314,0.005391,-2.266113,6.240163,-3.071982,-8.701633,-6.583451,-0.703891,7.363991,7.292413,-1.611874,-8.147772,1.813250,-5.785214,9.558640,1.267937,-3.834150,8.917985,8.542817,5.661929,-5.422121,0.585815,0.399844,8.998849,-5.230424,8.367318,6.420601,9.288555,9.411210,4.805473,-9.219449,-6.064496,9.890664,6.430946,-3.396166,1.038662,-2.711235,5.691193,-7.613024,1.996294,-2.398078,9.468150,-0.538923,-5.266286,-3.294344,8.419442,-2.635017,-5.915908,9.650445,-4.812203,-3.332607,-4.086600,-9.886192,-2.200965,-5.742528,-3.819080,-3.796179,-9.790758,-2.911835,-8.274769,-7.117809,-7.500053,1.518727,0.985496,-3.991475,6.361145,7.904101,-9.433982,3.865339,-2.726349,-2.630382,-0.427279,2.653951,2.290861,8.450328,-9.393021,2.695059,-2.061736,4.777844,1.222733,-8.979726,-9.036373,-6.384172,4.602738,0.506738,3.119211,-9.212425,8.440690,1.494799,-4.346934,-8.637050,-4.196670,3.364111,1.534954,-2.505295,-0.776438,0.362367,-1.853516,7.862251,6.561170,-4.560282,-4.600017,9.066370,-1.875427,1.895009,6.791429,8.482380,0.109945,8.940394,-4.263879,-7.178100,-3.065646,3.197950,6.707255,-6.126112,-6.557443,-1.702106,-4.179786,-4.422069,-4.544255,2.742535,1.723077,6.669405,6.701275,2.062074,9.267714,-1.997427,9.841073,-7.431379,7.454222,-9.815880,5.526816,-7.184803,-8.471542,-6.522121,-9.623772,-5.784914,6.067998,3.783679,-9.647525,-0.334239,-6.545012,5.829433,-9.353828,-5.877513,1.776454,2.679057,5.949544,-8.900643,-9.673022,-5.883970,-2.281506,2.385384,7.621909,-3.417026,7.625975,1.843233,5.492773,-4.587843,-8.475111,8.246266,6.677213,6.398023,9.864832,-5.100752,-9.921529,-9.990298,1.738578,-9.380058,-5.321223,8.484421,8.845169,7.310390,5.340882,7.851059,2.819763,3.249790,8.051561,4.119587,-1.367562,5.589224,9.865829,1.860712,7.847606,4.548536,-5.976909,4.972713,8.318787,4.940992,-7.297359,-1.493848,3.682051,-6.480582,-1.288876,7.677057,2.643266,-6.469630,6.974516,-4.403834,1.289546,-5.012027,-8.654067,-0.188451,2.952521,-0.630302,-7.286804,8.989157,4.011371,-1.220726,9.750691,-0.094956,-3.919654,0.395493,9.619173,-3.516520,6.129614,-9.784748,8.615119,4.964153,-3.910524,-4.278436,8.788029,9.814377,-3.206916,-6.518984,1.111255,-8.457384,9.568844,3.080468,2.385841,-9.494110,4.796117,-2.897784,0.103553,9.224048,-1.986868,-8.609890,7.584105,-1.807274,5.841965,6.621312,0.174257,1.528271,-2.174538,0.579665,-7.396218,-7.446062,5.819993,-2.412385,2.632243,-6.432114,-0.736822,8.844084,-3.316418,7.693778,-1.760466,5.849487,-2.259364,1.564250,0.151113,2.802820,-6.335774,6.023709,-8.371489,-0.695668,4.036823,2.753590,8.477137,0.701885,-3.213482,1.682621,-3.590666,7.991056,0.116976,8.902504,1.796113,8.714024,-8.305748,8.203630,-7.056547,-9.987385,1.436421,5.902908,-1.306189,-0.161109,9.973450,-9.496216,-8.191855,4.208161,-7.044437,3.660495,2.387006,0.052245,4.113740,-6.396020,-0.143360,-4.133939,2.437957,-6.844006,-2.966657,-7.219598,-0.115003,2.439329,-6.459228,8.666925,4.645345,6.894095,7.441801,7.420880,0.683071,-4.469664,-1.324900,3.405544,5.187188,-7.462563,9.386972,2.768029,6.645563,-5.865665,6.367429,-3.476200,-5.559206,6.279316,-3.273357,9.597897,5.237871,4.421054,-6.816628,1.834739,-6.898012,8.316352,-5.090128,7.460552,-8.083353,-6.790228,7.709563,-4.659767,-5.242822,9.492685,-0.605269,-7.501917,9.891522,-7.639217,3.856909,4.500808,3.133027,0.405831,3.114341,6.071716,-3.512307,-4.276137,-5.529069,-6.678627,-4.757071,8.215444,-5.787325,-3.355266,7.046083,8.735195,-3.556051,-5.310975,3.221546,-2.482057,-5.535958,-6.615764,6.282937,8.815465,-2.633967,-9.756640,5.028338,2.826820,6.986550,4.444053,-7.322062,0.719007,4.332243,-9.849988,2.060237,-5.916792,-2.693460,9.253060,3.783262,9.111002,-7.720238,-1.898881,7.185979,9.227354,-4.852527,0.761331,5.942937,8.950976,-6.395153,2.859385,-0.058219,-7.970966,8.059789,-5.149117,-8.636873,-4.073438,7.067087,-8.036422,-1.084917,-4.532847,4.805213,-4.660468,-2.563797,6.465332,7.904187,9.665239,-1.096295,3.322173,2.419546,-4.624245,2.045622,-8.008022,-1.909353,-6.542253,-1.768223,3.746440,-8.067011,-4.175829,8.758449,-4.472239,-3.449984,9.991210,4.421345,-2.738503,-2.668640,-6.426540,4.125699,6.471806,8.610034,5.698166,-3.252850,8.903860,-9.516113,5.761704,-7.173754,-1.523037,6.022896,5.696347,-2.272332,9.241892,7.433611,2.022951,-3.496687,-1.409882,-8.777976,1.714116,-5.001206,4.945420,-8.455420,-0.874478,-3.776082,-6.620243,-7.219150,-9.805907,4.547617,-9.061066,8.446980,-6.087092,-4.676379,-0.750945,-0.251185,6.879174,-6.219878,0.444612,7.019317,2.704902,-3.836199,-2.799249,-0.131380,-9.623509,-5.390165,-3.528529,-6.465187,-9.368808,4.434780,1.476156,-2.535568,-2.035818,9.842796,-9.499673,3.758583,8.598987,7.959192,7.994060,-4.642095,1.120707,-4.154121,5.928012,-2.969040,4.049988,-8.619261,4.073261,4.299460,6.842045,3.421698,4.149116,-5.475457,7.327121,-7.255510,4.688562,-2.620776,-9.066993,-7.908540,0.751003,7.426224,-1.359337,6.549032,-0.884980,5.894025,6.240622,9.263419,4.233181,6.528694,5.623563,5.963901,0.747566,-4.345101,-3.892285,3.929805,8.478170,-6.842653,-9.674254,-7.883567,-1.731395,-2.353809,-2.504214,5.498656,0.839069,-7.260321,-2.963576,2.284539,5.631603,8.108639,-9.413179,7.435468,1.790920,8.639210,7.734195,0.970379,5.339602,-6.839073,7.659865,-3.655047,-4.775558,-5.130393,-4.393482,-4.808178,4.333888,-3.594635,-5.244737,0.697043,0.517461,2.346213,-9.653293,1.756585,4.593156,-3.187313,6.348387,4.795940,4.933095,-3.204033,-9.080380,-8.759235,6.973427,7.089465,-6.354742,0.222316,-7.875722,0.135851,2.879780,-4.124733,-0.616676,-2.362747,8.122766,4.230405,5.786784,5.280598,1.574059,4.832514,-6.355324,-9.914676,7.121223,-1.656325,3.188338,9.059795,-4.575588,5.983227,-1.949286,-1.969939,8.208773,-4.379368,-9.086423,-8.640259,4.661864,-3.136673,1.216635,4.476127,-0.046932,-4.773650,6.192158,6.465438,8.258150,-1.758984,-7.674251,-8.390669,-1.158448,-8.433782,-1.284645,-1.940883,-6.194432,2.559902,-3.871597,-3.872293,-5.647258,-5.865199,-1.967002,-7.492637,-2.004569,1.385755,3.623253,-7.288047,1.420772,-1.382742,-3.802445,9.448587,9.057915,-6.210399,9.458381,3.094807,4.700905,6.167481,1.496874,2.009365,-6.857006,-8.582517,-7.281177,-9.992736,3.007939,3.376335,2.663749,-1.431483,8.710340,-0.449609,9.434271,9.922736,9.829481,1.966098,-2.839997,-0.185718,4.669342,-8.615583,-6.487830,4.759262,-5.924320,5.149610,-7.034191,-9.497717,-4.724293,-8.477589,-9.518754,-6.249334,8.367748,-8.094226,-9.452908,-2.848928,7.641127,-4.720025,2.549395,4.519373,-0.954687,-8.307833,-4.009648,2.788904,9.252405,6.438312,9.723595,-3.387826,7.009411,-8.601266,6.029882,0.792815,1.605378,-8.877660,-5.408940,-1.454695,-6.152726,9.252529,-9.861591,8.047739,-4.852906,5.446679,-9.611336,-9.407797,1.616089,-0.070668,-5.517700,7.773174,5.491942,-1.227990,-6.991442,-2.790272,6.640919,1.665270,-8.994568,-5.476249,3.308541,-2.669879,5.549756,0.235036,0.477051,5.730049,-9.234083,-4.661460,5.694035,4.912731,7.251800,-8.671365,8.861370,-7.751293,5.913937,-1.334834,2.514159,-5.844119,-5.616187,4.479652,6.556742,0.130512,9.335966,8.031872,-9.162680,-0.668454,9.075816,4.594124,0.408666,-7.408474,-2.859888,6.339806,-4.163934,-1.354295,-8.214765,-6.858212,-6.952394,4.708120,9.931049,-9.078198,3.328065,-4.018058,-4.352045,0.632583,8.208715,-6.623897,-7.128293,8.762848,0.192020,3.756340,7.846489,-6.726498,1.333018,-9.058199,-1.990359,8.711835,4.745761,-5.943701,0.019044,6.986989,-0.551598,-1.450784,-8.855443,2.996419,4.414730,7.046312,-1.872663,-1.715970,9.927568,1.902654,-9.565011,9.292071,-2.283624,4.587169,6.079434,-4.138687,-6.373195,-0.974060,4.948855,-6.765101,7.794097,0.225479,5.778049,3.172985,-6.092711,0.319923,0.054873,7.895398,-1.140268,2.969898,8.652162,4.846411,-8.476822,-9.178563,2.777413,-8.673629,-9.338408,8.667433,-9.323827,-3.943740,9.738651,8.559639,-8.945619,-3.703457,0.596402,-3.956167,4.225130,-1.840351,-8.720362,9.430820,3.391421,-9.009667,-8.133726,-3.294507,-4.334981,3.472620,-4.800767,0.654602,1.116180,8.825872,7.130337,-2.176708,-8.978623,5.933867,7.567657,-3.983566,-7.041982,2.638216,-5.116049,8.416693,-7.030974,-1.610174,5.043023,-7.652313], dtype = "float64")#candidate|938|(3360,)|const|float64
call_937 = relay.TupleGetItem(func_674_call(relay.reshape(const_938.astype('float64'), [14, 16, 15])), 0)
call_939 = relay.TupleGetItem(func_676_call(relay.reshape(const_938.astype('float64'), [14, 16, 15])), 0)
output = relay.Tuple([call_929,call_932,const_933,call_937,const_938,])
output2 = relay.Tuple([call_930,call_934,const_933,call_939,const_938,])
func_947 = relay.Function([], output)
mod['func_947'] = func_947
mod = relay.transform.InferType()(mod)
mutated_mod['func_947'] = func_947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mutated_mod.get_global_var('func_947')
call_948 = func_947_call()
output = call_948
func_949 = relay.Function([], output)
mutated_mod['func_949'] = func_949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_969 = relay.TupleGetItem(func_918_call(), 0)
call_970 = relay.TupleGetItem(func_920_call(), 0)
output = call_969
output2 = call_970
func_971 = relay.Function([], output)
mod['func_971'] = func_971
mod = relay.transform.InferType()(mod)
mutated_mod['func_971'] = func_971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mutated_mod.get_global_var('func_971')
call_972 = func_971_call()
output = call_972
func_973 = relay.Function([], output)
mutated_mod['func_973'] = func_973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_979 = relay.var("var_979", dtype = "float64", shape = ())#candidate|979|()|var|float64
var_980 = relay.var("var_980", dtype = "float64", shape = (3, 11, 16))#candidate|980|(3, 11, 16)|var|float64
bop_981 = relay.divide(var_979.astype('float64'), var_980.astype('float64')) # shape=(3, 11, 16)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_999 = func_335_call()
call_1000 = func_335_call()
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
var_1002 = relay.var("var_1002", dtype = "float64", shape = (420, 8))#candidate|1002|(420, 8)|var|float64
call_1001 = relay.TupleGetItem(func_674_call(relay.reshape(var_1002.astype('float64'), [14, 16, 15])), 0)
call_1003 = relay.TupleGetItem(func_676_call(relay.reshape(var_1002.astype('float64'), [14, 16, 15])), 0)
output = relay.Tuple([bop_981,call_999,call_1001,var_1002,])
output2 = relay.Tuple([bop_981,call_1000,call_1003,var_1002,])
func_1004 = relay.Function([var_979,var_980,var_1002,], output)
mod['func_1004'] = func_1004
mod = relay.transform.InferType()(mod)
var_1005 = relay.var("var_1005", dtype = "float64", shape = ())#candidate|1005|()|var|float64
var_1006 = relay.var("var_1006", dtype = "float64", shape = (3, 11, 16))#candidate|1006|(3, 11, 16)|var|float64
var_1007 = relay.var("var_1007", dtype = "float64", shape = (420, 8))#candidate|1007|(420, 8)|var|float64
output = func_1004(var_1005,var_1006,var_1007,)
func_1008 = relay.Function([var_1005,var_1006,var_1007,], output)
mutated_mod['func_1008'] = func_1008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_1065 = relay.TupleGetItem(func_209_call(), 0)
call_1066 = relay.TupleGetItem(func_210_call(), 0)
output = call_1065
output2 = call_1066
func_1075 = relay.Function([], output)
mod['func_1075'] = func_1075
mod = relay.transform.InferType()(mod)
output = func_1075()
func_1076 = relay.Function([], output)
mutated_mod['func_1076'] = func_1076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_1148 = relay.TupleGetItem(func_918_call(), 0)
call_1149 = relay.TupleGetItem(func_920_call(), 0)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_1158 = func_579_call()
call_1159 = func_579_call()
output = relay.Tuple([call_1148,call_1158,])
output2 = relay.Tuple([call_1149,call_1159,])
func_1171 = relay.Function([], output)
mod['func_1171'] = func_1171
mod = relay.transform.InferType()(mod)
output = func_1171()
func_1172 = relay.Function([], output)
mutated_mod['func_1172'] = func_1172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_1200 = relay.TupleGetItem(func_209_call(), 0)
call_1201 = relay.TupleGetItem(func_210_call(), 0)
output = relay.Tuple([call_1200,])
output2 = relay.Tuple([call_1201,])
func_1202 = relay.Function([], output)
mod['func_1202'] = func_1202
mod = relay.transform.InferType()(mod)
mutated_mod['func_1202'] = func_1202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1202_call = mutated_mod.get_global_var('func_1202')
call_1203 = func_1202_call()
output = call_1203
func_1204 = relay.Function([], output)
mutated_mod['func_1204'] = func_1204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_1243 = func_388_call()
call_1244 = func_388_call()
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_1250 = relay.TupleGetItem(func_209_call(), 0)
call_1251 = relay.TupleGetItem(func_210_call(), 0)
func_1202_call = mod.get_global_var('func_1202')
func_1204_call = mutated_mod.get_global_var('func_1204')
call_1265 = relay.TupleGetItem(func_1202_call(), 0)
call_1266 = relay.TupleGetItem(func_1204_call(), 0)
output = relay.Tuple([call_1243,call_1250,call_1265,])
output2 = relay.Tuple([call_1244,call_1251,call_1266,])
func_1269 = relay.Function([], output)
mod['func_1269'] = func_1269
mod = relay.transform.InferType()(mod)
output = func_1269()
func_1270 = relay.Function([], output)
mutated_mod['func_1270'] = func_1270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_1431 = relay.TupleGetItem(func_947_call(), 1)
call_1432 = relay.TupleGetItem(func_949_call(), 1)
uop_1441 = relay.atan(call_1431.astype('float32')) # shape=(11, 10, 8)
uop_1443 = relay.atan(call_1432.astype('float32')) # shape=(11, 10, 8)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_1444 = relay.TupleGetItem(func_209_call(), 0)
call_1445 = relay.TupleGetItem(func_210_call(), 0)
output = relay.Tuple([uop_1441,call_1444,])
output2 = relay.Tuple([uop_1443,call_1445,])
func_1452 = relay.Function([], output)
mod['func_1452'] = func_1452
mod = relay.transform.InferType()(mod)
mutated_mod['func_1452'] = func_1452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mutated_mod.get_global_var('func_1452')
call_1453 = func_1452_call()
output = call_1453
func_1454 = relay.Function([], output)
mutated_mod['func_1454'] = func_1454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_1458 = relay.TupleGetItem(func_188_call(), 0)
call_1459 = relay.TupleGetItem(func_189_call(), 0)
var_1471 = relay.var("var_1471", dtype = "float32", shape = (14, 2, 15))#candidate|1471|(14, 2, 15)|var|float32
bop_1472 = relay.minimum(call_1458.astype('uint8'), var_1471.astype('uint8')) # shape=(14, 2, 15)
bop_1475 = relay.minimum(call_1459.astype('uint8'), var_1471.astype('uint8')) # shape=(14, 2, 15)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_1490 = relay.TupleGetItem(func_209_call(), 0)
call_1491 = relay.TupleGetItem(func_210_call(), 0)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_1492 = relay.TupleGetItem(func_1171_call(), 1)
call_1493 = relay.TupleGetItem(func_1172_call(), 1)
output = relay.Tuple([bop_1472,call_1490,call_1492,])
output2 = relay.Tuple([bop_1475,call_1491,call_1493,])
func_1495 = relay.Function([var_1471,], output)
mod['func_1495'] = func_1495
mod = relay.transform.InferType()(mod)
mutated_mod['func_1495'] = func_1495
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1496 = relay.var("var_1496", dtype = "float32", shape = (14, 2, 15))#candidate|1496|(14, 2, 15)|var|float32
func_1495_call = mutated_mod.get_global_var('func_1495')
call_1497 = func_1495_call(var_1496)
output = call_1497
func_1498 = relay.Function([var_1496], output)
mutated_mod['func_1498'] = func_1498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_1526 = relay.TupleGetItem(func_209_call(), 0)
call_1527 = relay.TupleGetItem(func_210_call(), 0)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1528 = func_971_call()
call_1529 = func_971_call()
output = relay.Tuple([call_1526,call_1528,])
output2 = relay.Tuple([call_1527,call_1529,])
func_1550 = relay.Function([], output)
mod['func_1550'] = func_1550
mod = relay.transform.InferType()(mod)
output = func_1550()
func_1551 = relay.Function([], output)
mutated_mod['func_1551'] = func_1551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1565 = func_971_call()
call_1566 = func_971_call()
var_1575 = relay.var("var_1575", dtype = "float32", shape = (14, 1, 15))#candidate|1575|(14, 1, 15)|var|float32
bop_1576 = relay.bitwise_and(call_1565.astype('uint64'), relay.reshape(var_1575.astype('uint64'), relay.shape_of(call_1565))) # shape=(14, 1, 15)
bop_1579 = relay.bitwise_and(call_1566.astype('uint64'), relay.reshape(var_1575.astype('uint64'), relay.shape_of(call_1566))) # shape=(14, 1, 15)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_1580 = func_421_call()
call_1581 = func_421_call()
uop_1582 = relay.sqrt(call_1580.astype('float32')) # shape=(14, 1, 15)
uop_1584 = relay.sqrt(call_1581.astype('float32')) # shape=(14, 1, 15)
output = relay.Tuple([bop_1576,uop_1582,])
output2 = relay.Tuple([bop_1579,uop_1584,])
func_1590 = relay.Function([var_1575,], output)
mod['func_1590'] = func_1590
mod = relay.transform.InferType()(mod)
var_1591 = relay.var("var_1591", dtype = "float32", shape = (14, 1, 15))#candidate|1591|(14, 1, 15)|var|float32
output = func_1590(var_1591)
func_1592 = relay.Function([var_1591], output)
mutated_mod['func_1592'] = func_1592
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1625 = relay.var("var_1625", dtype = "int64", shape = ())#candidate|1625|()|var|int64
const_1626 = relay.const([[[5,-6,9,-7,-3,3,4,-8,-4],[-7,2,-8,3,9,-8,-9,-10,-2]],[[-1,5,3,-5,5,-7,8,1,-3],[5,5,-9,-10,8,5,10,-2,-10]],[[-2,1,8,8,9,6,-8,-1,-4],[-6,1,8,-5,-4,5,1,10,-7]],[[-9,4,4,-1,10,-7,-4,-1,-6],[-3,-9,-9,2,2,-1,8,-1,9]]], dtype = "int64")#candidate|1626|(4, 2, 9)|const|int64
bop_1627 = relay.greater_equal(var_1625.astype('bool'), const_1626.astype('bool')) # shape=(4, 2, 9)
func_630_call = mod.get_global_var('func_630')
func_631_call = mutated_mod.get_global_var('func_631')
call_1637 = func_630_call()
call_1638 = func_630_call()
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
const_1642 = relay.const([0.588381,2.564015,-5.750751,-5.133568,5.230286,4.981979,0.353633,7.502936,-2.170378,6.342827,-9.569890,-5.736341,4.509831,2.027520,-3.950873,8.480604,2.001418,-1.838894,-1.839695,4.832667,-1.368425,4.022544,-8.504043,-5.900885,4.117689,-3.642279,8.707015,6.432678,-0.475744,7.135530,6.061634,-9.186167,-0.126874,-5.601632,4.287614,-3.921596], dtype = "float64")#candidate|1642|(36,)|const|float64
call_1641 = relay.TupleGetItem(func_602_call(relay.reshape(const_1642.astype('float64'), [9, 4, 1])), 1)
call_1643 = relay.TupleGetItem(func_604_call(relay.reshape(const_1642.astype('float64'), [9, 4, 1])), 1)
func_630_call = mod.get_global_var('func_630')
func_631_call = mutated_mod.get_global_var('func_631')
call_1644 = func_630_call()
call_1645 = func_630_call()
output = relay.Tuple([bop_1627,call_1637,call_1641,const_1642,call_1644,])
output2 = relay.Tuple([bop_1627,call_1638,call_1643,const_1642,call_1645,])
func_1646 = relay.Function([var_1625,], output)
mod['func_1646'] = func_1646
mod = relay.transform.InferType()(mod)
mutated_mod['func_1646'] = func_1646
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1647 = relay.var("var_1647", dtype = "int64", shape = ())#candidate|1647|()|var|int64
func_1646_call = mutated_mod.get_global_var('func_1646')
call_1648 = func_1646_call(var_1647)
output = call_1648
func_1649 = relay.Function([var_1647], output)
mutated_mod['func_1649'] = func_1649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_1739 = func_421_call()
call_1740 = func_421_call()
output = relay.Tuple([call_1739,])
output2 = relay.Tuple([call_1740,])
func_1743 = relay.Function([], output)
mod['func_1743'] = func_1743
mod = relay.transform.InferType()(mod)
output = func_1743()
func_1744 = relay.Function([], output)
mutated_mod['func_1744'] = func_1744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_1779 = func_971_call()
call_1780 = func_971_call()
output = call_1779
output2 = call_1780
func_1802 = relay.Function([], output)
mod['func_1802'] = func_1802
mod = relay.transform.InferType()(mod)
output = func_1802()
func_1803 = relay.Function([], output)
mutated_mod['func_1803'] = func_1803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mod.get_global_var('func_1743')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_1814 = relay.TupleGetItem(func_1743_call(), 0)
call_1815 = relay.TupleGetItem(func_1744_call(), 0)
output = relay.Tuple([call_1814,])
output2 = relay.Tuple([call_1815,])
func_1827 = relay.Function([], output)
mod['func_1827'] = func_1827
mod = relay.transform.InferType()(mod)
output = func_1827()
func_1828 = relay.Function([], output)
mutated_mod['func_1828'] = func_1828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_1854 = relay.TupleGetItem(func_947_call(), 3)
call_1855 = relay.TupleGetItem(func_949_call(), 3)
output = call_1854
output2 = call_1855
func_1860 = relay.Function([], output)
mod['func_1860'] = func_1860
mod = relay.transform.InferType()(mod)
mutated_mod['func_1860'] = func_1860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1860_call = mutated_mod.get_global_var('func_1860')
call_1861 = func_1860_call()
output = call_1861
func_1862 = relay.Function([], output)
mutated_mod['func_1862'] = func_1862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_1933 = relay.TupleGetItem(func_303_call(), 1)
call_1934 = relay.TupleGetItem(func_304_call(), 1)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_1954 = func_421_call()
call_1955 = func_421_call()
bop_1973 = relay.bitwise_xor(call_1954.astype('int8'), relay.reshape(call_1933.astype('int8'), relay.shape_of(call_1954))) # shape=(14, 1, 15)
bop_1976 = relay.bitwise_xor(call_1955.astype('int8'), relay.reshape(call_1934.astype('int8'), relay.shape_of(call_1955))) # shape=(14, 1, 15)
func_1743_call = mod.get_global_var('func_1743')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_1985 = relay.TupleGetItem(func_1743_call(), 0)
call_1986 = relay.TupleGetItem(func_1744_call(), 0)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_1999 = relay.TupleGetItem(func_303_call(), 1)
call_2000 = relay.TupleGetItem(func_304_call(), 1)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_2009 = func_971_call()
call_2010 = func_971_call()
uop_2020 = relay.log2(call_1933.astype('float32')) # shape=(14, 1, 15)
uop_2022 = relay.log2(call_1934.astype('float32')) # shape=(14, 1, 15)
output = relay.Tuple([bop_1973,call_1985,call_1999,call_2009,uop_2020,])
output2 = relay.Tuple([bop_1976,call_1986,call_2000,call_2010,uop_2022,])
func_2032 = relay.Function([], output)
mod['func_2032'] = func_2032
mod = relay.transform.InferType()(mod)
mutated_mod['func_2032'] = func_2032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2033 = func_2032_call()
output = call_2033
func_2034 = relay.Function([], output)
mutated_mod['func_2034'] = func_2034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1860_call = mod.get_global_var('func_1860')
func_1862_call = mutated_mod.get_global_var('func_1862')
call_2049 = func_1860_call()
call_2050 = func_1860_call()
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_2051 = func_388_call()
call_2052 = func_388_call()
output = relay.Tuple([call_2049,call_2051,])
output2 = relay.Tuple([call_2050,call_2052,])
func_2053 = relay.Function([], output)
mod['func_2053'] = func_2053
mod = relay.transform.InferType()(mod)
output = func_2053()
func_2054 = relay.Function([], output)
mutated_mod['func_2054'] = func_2054
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_2055 = relay.TupleGetItem(func_947_call(), 0)
call_2056 = relay.TupleGetItem(func_949_call(), 0)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
var_2058 = relay.var("var_2058", dtype = "float64", shape = (3360,))#candidate|2058|(3360,)|var|float64
call_2057 = relay.TupleGetItem(func_674_call(relay.reshape(var_2058.astype('float64'), [14, 16, 15])), 0)
call_2059 = relay.TupleGetItem(func_676_call(relay.reshape(var_2058.astype('float64'), [14, 16, 15])), 0)
func_1269_call = mod.get_global_var('func_1269')
func_1270_call = mutated_mod.get_global_var('func_1270')
call_2079 = relay.TupleGetItem(func_1269_call(), 0)
call_2080 = relay.TupleGetItem(func_1270_call(), 0)
uop_2087 = relay.atan(call_2079.astype('float32')) # shape=(14, 1, 15)
uop_2089 = relay.atan(call_2080.astype('float32')) # shape=(14, 1, 15)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
call_2091 = relay.TupleGetItem(func_674_call(relay.reshape(var_2058.astype('float64'), [14, 16, 15])), 2)
call_2092 = relay.TupleGetItem(func_676_call(relay.reshape(var_2058.astype('float64'), [14, 16, 15])), 2)
output = relay.Tuple([call_2055,call_2057,var_2058,uop_2087,call_2091,])
output2 = relay.Tuple([call_2056,call_2059,var_2058,uop_2089,call_2092,])
func_2098 = relay.Function([var_2058,], output)
mod['func_2098'] = func_2098
mod = relay.transform.InferType()(mod)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2099 = relay.var("var_2099", dtype = "float64", shape = (3360,))#candidate|2099|(3360,)|var|float64
func_2098_call = mutated_mod.get_global_var('func_2098')
call_2100 = func_2098_call(var_2099)
output = call_2100
func_2101 = relay.Function([var_2099], output)
mutated_mod['func_2101'] = func_2101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_2126 = func_579_call()
call_2127 = func_579_call()
func_1495_call = mod.get_global_var('func_1495')
func_1498_call = mutated_mod.get_global_var('func_1498')
var_2130 = relay.var("var_2130", dtype = "float32", shape = (420,))#candidate|2130|(420,)|var|float32
call_2129 = relay.TupleGetItem(func_1495_call(relay.reshape(var_2130.astype('float32'), [14, 2, 15])), 2)
call_2131 = relay.TupleGetItem(func_1498_call(relay.reshape(var_2130.astype('float32'), [14, 2, 15])), 2)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_2132 = relay.TupleGetItem(func_1590_call(relay.reshape(call_2126.astype('float32'), [14, 1, 15])), 0)
call_2133 = relay.TupleGetItem(func_1592_call(relay.reshape(call_2126.astype('float32'), [14, 1, 15])), 0)
output = relay.Tuple([call_2126,call_2129,var_2130,call_2132,])
output2 = relay.Tuple([call_2127,call_2131,var_2130,call_2133,])
func_2134 = relay.Function([var_2130,], output)
mod['func_2134'] = func_2134
mod = relay.transform.InferType()(mod)
mutated_mod['func_2134'] = func_2134
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2135 = relay.var("var_2135", dtype = "float32", shape = (420,))#candidate|2135|(420,)|var|float32
func_2134_call = mutated_mod.get_global_var('func_2134')
call_2136 = func_2134_call(var_2135)
output = call_2136
func_2137 = relay.Function([var_2135], output)
mutated_mod['func_2137'] = func_2137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2203 = relay.var("var_2203", dtype = "bool", shape = (7, 16, 5))#candidate|2203|(7, 16, 5)|var|bool
var_2204 = relay.var("var_2204", dtype = "bool", shape = (7, 16, 5))#candidate|2204|(7, 16, 5)|var|bool
bop_2205 = relay.logical_and(var_2203.astype('bool'), relay.reshape(var_2204.astype('bool'), relay.shape_of(var_2203))) # shape=(7, 16, 5)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_2208 = relay.TupleGetItem(func_918_call(), 0)
call_2209 = relay.TupleGetItem(func_920_call(), 0)
output = relay.Tuple([bop_2205,call_2208,])
output2 = relay.Tuple([bop_2205,call_2209,])
func_2249 = relay.Function([var_2203,var_2204,], output)
mod['func_2249'] = func_2249
mod = relay.transform.InferType()(mod)
mutated_mod['func_2249'] = func_2249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2249_call = mutated_mod.get_global_var('func_2249')
var_2251 = relay.var("var_2251", dtype = "bool", shape = (7, 16, 5))#candidate|2251|(7, 16, 5)|var|bool
var_2252 = relay.var("var_2252", dtype = "bool", shape = (7, 16, 5))#candidate|2252|(7, 16, 5)|var|bool
call_2250 = func_2249_call(var_2251,var_2252,)
output = call_2250
func_2253 = relay.Function([var_2251,var_2252,], output)
mutated_mod['func_2253'] = func_2253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_2266 = relay.TupleGetItem(func_918_call(), 0)
call_2267 = relay.TupleGetItem(func_920_call(), 0)
func_2053_call = mod.get_global_var('func_2053')
func_2054_call = mutated_mod.get_global_var('func_2054')
call_2274 = relay.TupleGetItem(func_2053_call(), 1)
call_2275 = relay.TupleGetItem(func_2054_call(), 1)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_2286 = relay.TupleGetItem(func_947_call(), 3)
call_2287 = relay.TupleGetItem(func_949_call(), 3)
func_497_call = mod.get_global_var('func_497')
func_500_call = mutated_mod.get_global_var('func_500')
var_2303 = relay.var("var_2303", dtype = "float32", shape = (1680,))#candidate|2303|(1680,)|var|float32
call_2302 = relay.TupleGetItem(func_497_call(relay.reshape(var_2303.astype('float32'), [14, 8, 15])), 5)
call_2304 = relay.TupleGetItem(func_500_call(relay.reshape(var_2303.astype('float32'), [14, 8, 15])), 5)
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_2311 = relay.TupleGetItem(func_303_call(), 3)
call_2312 = relay.TupleGetItem(func_304_call(), 3)
func_1452_call = mod.get_global_var('func_1452')
func_1454_call = mutated_mod.get_global_var('func_1454')
call_2314 = relay.TupleGetItem(func_1452_call(), 0)
call_2315 = relay.TupleGetItem(func_1454_call(), 0)
output = relay.Tuple([call_2266,call_2274,call_2286,call_2302,var_2303,call_2311,call_2314,])
output2 = relay.Tuple([call_2267,call_2275,call_2287,call_2304,var_2303,call_2312,call_2315,])
func_2318 = relay.Function([var_2303,], output)
mod['func_2318'] = func_2318
mod = relay.transform.InferType()(mod)
var_2319 = relay.var("var_2319", dtype = "float32", shape = (1680,))#candidate|2319|(1680,)|var|float32
output = func_2318(var_2319)
func_2320 = relay.Function([var_2319], output)
mutated_mod['func_2320'] = func_2320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mod.get_global_var('func_1452')
func_1454_call = mutated_mod.get_global_var('func_1454')
call_2325 = relay.TupleGetItem(func_1452_call(), 1)
call_2326 = relay.TupleGetItem(func_1454_call(), 1)
func_497_call = mod.get_global_var('func_497')
func_500_call = mutated_mod.get_global_var('func_500')
var_2332 = relay.var("var_2332", dtype = "float32", shape = (1680, 1))#candidate|2332|(1680, 1)|var|float32
call_2331 = relay.TupleGetItem(func_497_call(relay.reshape(var_2332.astype('float32'), [14, 8, 15])), 3)
call_2333 = relay.TupleGetItem(func_500_call(relay.reshape(var_2332.astype('float32'), [14, 8, 15])), 3)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_2334 = func_421_call()
call_2335 = func_421_call()
func_303_call = mod.get_global_var('func_303')
func_304_call = mutated_mod.get_global_var('func_304')
call_2338 = relay.TupleGetItem(func_303_call(), 3)
call_2339 = relay.TupleGetItem(func_304_call(), 3)
bop_2340 = relay.not_equal(call_2334.astype('bool'), var_2332.astype('bool')) # shape=(14, 1680, 15)
bop_2343 = relay.not_equal(call_2335.astype('bool'), var_2332.astype('bool')) # shape=(14, 1680, 15)
bop_2345 = relay.equal(call_2334.astype('bool'), bop_2340.astype('bool')) # shape=(14, 1680, 15)
bop_2348 = relay.equal(call_2335.astype('bool'), bop_2343.astype('bool')) # shape=(14, 1680, 15)
output = relay.Tuple([call_2325,call_2331,call_2338,bop_2345,])
output2 = relay.Tuple([call_2326,call_2333,call_2339,bop_2348,])
func_2374 = relay.Function([var_2332,], output)
mod['func_2374'] = func_2374
mod = relay.transform.InferType()(mod)
mutated_mod['func_2374'] = func_2374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2375 = relay.var("var_2375", dtype = "float32", shape = (1680, 1))#candidate|2375|(1680, 1)|var|float32
func_2374_call = mutated_mod.get_global_var('func_2374')
call_2376 = func_2374_call(var_2375)
output = call_2376
func_2377 = relay.Function([var_2375], output)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mod.get_global_var('func_1452')
func_1454_call = mutated_mod.get_global_var('func_1454')
call_2400 = relay.TupleGetItem(func_1452_call(), 1)
call_2401 = relay.TupleGetItem(func_1454_call(), 1)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_2410 = relay.TupleGetItem(func_188_call(), 0)
call_2411 = relay.TupleGetItem(func_189_call(), 0)
output = relay.Tuple([call_2400,call_2410,])
output2 = relay.Tuple([call_2401,call_2411,])
func_2421 = relay.Function([], output)
mod['func_2421'] = func_2421
mod = relay.transform.InferType()(mod)
output = func_2421()
func_2422 = relay.Function([], output)
mutated_mod['func_2422'] = func_2422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_2446 = func_782_call()
call_2447 = func_782_call()
output = relay.Tuple([call_2446,])
output2 = relay.Tuple([call_2447,])
func_2469 = relay.Function([], output)
mod['func_2469'] = func_2469
mod = relay.transform.InferType()(mod)
mutated_mod['func_2469'] = func_2469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2469_call = mutated_mod.get_global_var('func_2469')
call_2470 = func_2469_call()
output = call_2470
func_2471 = relay.Function([], output)
mutated_mod['func_2471'] = func_2471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1802_call = mod.get_global_var('func_1802')
func_1803_call = mutated_mod.get_global_var('func_1803')
call_2516 = func_1802_call()
call_2517 = func_1802_call()
func_1827_call = mod.get_global_var('func_1827')
func_1828_call = mutated_mod.get_global_var('func_1828')
call_2522 = relay.TupleGetItem(func_1827_call(), 0)
call_2523 = relay.TupleGetItem(func_1828_call(), 0)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_2538 = relay.const([[False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,False,False,False],[True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,True,False],[True,True,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,True,True],[False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True],[True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,False,False],[False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,False,False],[False,False,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,True,True],[True,False,False,True,False,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,True],[False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False],[True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False],[True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False],[False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False],[False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True],[True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False],[False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True],[False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True],[True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,True,True,True],[False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,True,False,True],[False,True,False,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,True],[True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False],[False,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False],[False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True],[False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True],[True,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True],[True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True],[True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False],[True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,True],[True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False],[True,False,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True],[False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True],[False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False],[True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True],[True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,True,False],[False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False],[False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False],[False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False],[True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True],[False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,True],[False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True],[False,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False]], dtype = "bool")#candidate|2538|(40, 22)|const|bool
call_2537 = relay.TupleGetItem(func_54_call(relay.reshape(const_2538.astype('bool'), [11, 10, 8]), relay.reshape(const_2538.astype('bool'), [11, 10, 8]), ), 1)
call_2539 = relay.TupleGetItem(func_57_call(relay.reshape(const_2538.astype('bool'), [11, 10, 8]), relay.reshape(const_2538.astype('bool'), [11, 10, 8]), ), 1)
output = relay.Tuple([call_2516,call_2522,call_2537,const_2538,])
output2 = relay.Tuple([call_2517,call_2523,call_2539,const_2538,])
func_2548 = relay.Function([], output)
mod['func_2548'] = func_2548
mod = relay.transform.InferType()(mod)
output = func_2548()
func_2549 = relay.Function([], output)
mutated_mod['func_2549'] = func_2549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_2593 = relay.TupleGetItem(func_918_call(), 0)
call_2594 = relay.TupleGetItem(func_920_call(), 0)
var_2611 = relay.var("var_2611", dtype = "float32", shape = (14, 12, 15))#candidate|2611|(14, 12, 15)|var|float32
bop_2612 = relay.equal(call_2593.astype('bool'), var_2611.astype('bool')) # shape=(14, 12, 15)
bop_2615 = relay.equal(call_2594.astype('bool'), var_2611.astype('bool')) # shape=(14, 12, 15)
func_2249_call = mod.get_global_var('func_2249')
func_2253_call = mutated_mod.get_global_var('func_2253')
const_2623 = relay.const([False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False], dtype = "bool")#candidate|2623|(560,)|const|bool
call_2622 = relay.TupleGetItem(func_2249_call(relay.reshape(const_2623.astype('bool'), [7, 16, 5]), relay.reshape(const_2623.astype('bool'), [7, 16, 5]), ), 0)
call_2624 = relay.TupleGetItem(func_2253_call(relay.reshape(const_2623.astype('bool'), [7, 16, 5]), relay.reshape(const_2623.astype('bool'), [7, 16, 5]), ), 0)
bop_2630 = relay.bitwise_xor(bop_2612.astype('int8'), relay.reshape(var_2611.astype('int8'), relay.shape_of(bop_2612))) # shape=(14, 12, 15)
bop_2633 = relay.bitwise_xor(bop_2615.astype('int8'), relay.reshape(var_2611.astype('int8'), relay.shape_of(bop_2615))) # shape=(14, 12, 15)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_2634 = func_579_call()
call_2635 = func_579_call()
uop_2636 = relay.cosh(var_2611.astype('float64')) # shape=(14, 12, 15)
func_2032_call = mod.get_global_var('func_2032')
func_2034_call = mutated_mod.get_global_var('func_2034')
call_2642 = relay.TupleGetItem(func_2032_call(), 3)
call_2643 = relay.TupleGetItem(func_2034_call(), 3)
output = relay.Tuple([call_2622,const_2623,bop_2630,call_2634,uop_2636,call_2642,])
output2 = relay.Tuple([call_2624,const_2623,bop_2633,call_2635,uop_2636,call_2643,])
func_2648 = relay.Function([var_2611,], output)
mod['func_2648'] = func_2648
mod = relay.transform.InferType()(mod)
var_2649 = relay.var("var_2649", dtype = "float32", shape = (14, 12, 15))#candidate|2649|(14, 12, 15)|var|float32
output = func_2648(var_2649)
func_2650 = relay.Function([var_2649], output)
mutated_mod['func_2650'] = func_2650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_2667 = relay.TupleGetItem(func_1171_call(), 1)
call_2668 = relay.TupleGetItem(func_1172_call(), 1)
output = relay.Tuple([call_2667,])
output2 = relay.Tuple([call_2668,])
func_2671 = relay.Function([], output)
mod['func_2671'] = func_2671
mod = relay.transform.InferType()(mod)
output = func_2671()
func_2672 = relay.Function([], output)
mutated_mod['func_2672'] = func_2672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_2673 = func_579_call()
call_2674 = func_579_call()
uop_2675 = relay.cos(call_2673.astype('float64')) # shape=(14, 1, 15)
uop_2677 = relay.cos(call_2674.astype('float64')) # shape=(14, 1, 15)
func_1827_call = mod.get_global_var('func_1827')
func_1828_call = mutated_mod.get_global_var('func_1828')
call_2680 = relay.TupleGetItem(func_1827_call(), 0)
call_2681 = relay.TupleGetItem(func_1828_call(), 0)
output = relay.Tuple([uop_2675,call_2680,])
output2 = relay.Tuple([uop_2677,call_2681,])
func_2688 = relay.Function([], output)
mod['func_2688'] = func_2688
mod = relay.transform.InferType()(mod)
mutated_mod['func_2688'] = func_2688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2688_call = mutated_mod.get_global_var('func_2688')
call_2689 = func_2688_call()
output = call_2689
func_2690 = relay.Function([], output)
mutated_mod['func_2690'] = func_2690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_2691 = relay.TupleGetItem(func_1550_call(), 0)
call_2692 = relay.TupleGetItem(func_1551_call(), 0)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_2693 = func_971_call()
call_2694 = func_971_call()
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_2720 = func_335_call()
call_2721 = func_335_call()
output = relay.Tuple([call_2691,call_2693,call_2720,])
output2 = relay.Tuple([call_2692,call_2694,call_2721,])
func_2726 = relay.Function([], output)
mod['func_2726'] = func_2726
mod = relay.transform.InferType()(mod)
output = func_2726()
func_2727 = relay.Function([], output)
mutated_mod['func_2727'] = func_2727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_2836 = func_388_call()
call_2837 = func_388_call()
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_2843 = func_971_call()
call_2844 = func_971_call()
func_1495_call = mod.get_global_var('func_1495')
func_1498_call = mutated_mod.get_global_var('func_1498')
var_2851 = relay.var("var_2851", dtype = "float32", shape = (420,))#candidate|2851|(420,)|var|float32
call_2850 = relay.TupleGetItem(func_1495_call(relay.reshape(var_2851.astype('float32'), [14, 2, 15])), 2)
call_2852 = relay.TupleGetItem(func_1498_call(relay.reshape(var_2851.astype('float32'), [14, 2, 15])), 2)
output = relay.Tuple([call_2836,call_2843,call_2850,var_2851,])
output2 = relay.Tuple([call_2837,call_2844,call_2852,var_2851,])
func_2853 = relay.Function([var_2851,], output)
mod['func_2853'] = func_2853
mod = relay.transform.InferType()(mod)
var_2854 = relay.var("var_2854", dtype = "float32", shape = (420,))#candidate|2854|(420,)|var|float32
output = func_2853(var_2854)
func_2855 = relay.Function([var_2854], output)
mutated_mod['func_2855'] = func_2855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_2930 = func_421_call()
call_2931 = func_421_call()
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_2946 = relay.TupleGetItem(func_1171_call(), 1)
call_2947 = relay.TupleGetItem(func_1172_call(), 1)
output = relay.Tuple([call_2930,call_2946,])
output2 = relay.Tuple([call_2931,call_2947,])
func_2949 = relay.Function([], output)
mod['func_2949'] = func_2949
mod = relay.transform.InferType()(mod)
mutated_mod['func_2949'] = func_2949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mutated_mod.get_global_var('func_2949')
call_2950 = func_2949_call()
output = call_2950
func_2951 = relay.Function([], output)
mutated_mod['func_2951'] = func_2951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3021 = func_1075_call()
call_3022 = func_1075_call()
func_864_call = mod.get_global_var('func_864')
func_868_call = mutated_mod.get_global_var('func_868')
const_3027 = relay.const([7.198894,4.369954,-9.108488,-2.281468,-2.569238,-6.319936,9.646689,-5.168824,-3.395954,-6.373691,-0.848250,-1.283024,0.479685,-6.810927,5.015547,-8.485739,-1.501602,8.024861,6.260415,-8.102600,-2.001556,-9.989893,-5.117281,8.003834,-0.889995,6.974963,1.881920,3.784128,-5.046879,-4.129466,-6.615412,-7.833704,-0.270384,0.605910,2.098392,5.753116,-0.707305,7.209625,-3.444668,5.622345,-1.122970,4.035430,-3.580526,3.406667,-4.216718,-5.211551,-1.024596,4.627296,7.085630,-3.460216,8.703971,-4.207868,-0.924894,-8.380757,5.944831,5.576348,-1.468409,5.539255,9.928547,1.866475,-4.131255,-8.746091,-4.561480,6.082021,-0.747786,0.784216,1.235494,7.869267,2.468859,-1.111418,7.702199,1.354009,-8.971227,5.380247,1.616091,-3.808854,-7.955422,-8.367366,-3.226109,-2.825271,1.698108,-2.689927,-8.696253,-0.805581,7.961600,-4.653306,-4.338248,-9.964528,-2.683552,3.607354,-4.139630,-6.964904,-4.857267,-7.142382,-1.754546,-1.336464,-2.007292,8.579022,-1.968587,-5.966235,-2.861740,9.275347,-8.424435,-9.710720,6.729170,-0.187597,8.249769,-6.215403,2.287387,-8.121863,-1.397695,-3.272236,-8.293689,0.887377,8.604060,-0.043742,-0.937278,5.570574,-7.125483,6.656880,3.589337,0.228018,-8.141857,-7.394776,-4.833760,-3.427862,1.366808,1.991777,-7.684776,9.663447,6.050250,1.133552,1.124970,-7.540739,-9.752455,8.343854,-6.169098,-0.453286,-0.135430,-5.681307,-3.686677,8.055159,1.124994,2.026824,5.883027,-4.777534,-9.356003,-6.103452,-9.792973,0.528938,1.952632,-7.122765,-0.299668,-6.293104,0.419421,0.965563,3.647718,-2.404241,-9.676002,-3.764099,-6.640169,-2.905225,1.356174,-3.152441,4.276289,-7.078609,-6.022699,-6.067549,-7.980607,5.043571,-5.898546,5.121590,-7.702280,-0.434665,5.775183,-9.840445,8.963104,-3.644014,-6.575332,-9.830558,6.392390,-3.663335,0.714056,-9.768957,7.616679,-4.735813,-6.420020,-5.788279,4.196033,6.446259,6.833373,-2.660512,-4.653078,0.718355,5.170010,5.236857,3.152234,-9.771725,-3.364233,-5.561181,-6.203920,2.042242,-5.329327,9.693549,8.563670,-5.891133,4.959050,6.635558,7.456141,-0.230972,2.220144,2.258184,9.286569,7.433386,-4.806269,0.581942,-4.054540,-4.871884,-2.488618,-1.288141,-2.740900,2.404947,5.024666,-4.528843,7.112160,4.433495,-1.639277,2.789117,-8.217504,2.222110,-4.434880,-2.162503,-1.807091,2.034280,-1.531980,-3.583409,-0.864241,-0.306836,-3.116438,2.456837,6.925029,-2.132427,1.722613,8.965514,0.711460,0.491366,-6.323194,-6.823168,-0.795381,0.514846,-2.724810,4.697934,8.483074,-0.398089,-3.659548,-1.940831,8.381455,9.985971,-0.493395,-5.471642,-0.083051,-7.345521,3.164346,5.660259,-1.107619,7.171833,-0.496772,-5.694520,-3.922177,8.865873,-4.602867,2.074441,4.209588,-5.525613,2.289972,0.994601,-8.738098,-4.680477,-5.075238,4.673559,6.524855,1.196579,-7.704224,9.747325,0.486413,3.067786,-6.175791,4.226861,-1.029589,-5.973358,-4.456024,5.943799,5.400267,0.630877,6.910038,-3.345419,8.594106,-4.543430,1.018673,-8.600174,-4.483065,-8.461560,-7.720093,-2.156618,-9.388166,9.637019,-3.297223,8.287740,-7.124565,-1.403241,-0.982928,-0.424556,-1.602371,7.009985,4.095060,-1.893679,7.477150,-9.430360,-1.134854,-0.564904,6.017091,-6.047733,-0.002492,0.423809,-3.706219,-0.213685,3.536249,-3.029623,1.451850,9.155707,3.015202,6.303168,0.628620,1.489375,-5.893094,-3.511631,2.773102,-4.394073,-1.286926,-4.835422,9.764970,3.833101,-8.568641,-3.511254,8.633965,-8.260013,-2.739207,-6.017023,0.732072,9.714890,2.229417,-4.316074,-2.605471,4.849984,-3.978639,6.006453,-6.277411,-8.439129,-3.563943,0.513963,6.542707,8.357834,0.207244,1.038960,4.353205,-6.792529,-6.868275,0.065875,6.008259,5.029476,-0.008561,1.329007,-0.220810,9.598717,9.984456,-7.474286,-5.131576,-5.201517,2.969229,9.763062,-4.062485,-3.314438,-9.765599,-1.199393,-9.930483,2.147174,-8.702620,0.865600,5.162736,-2.340669,7.172523,5.402815,-1.587307,4.759588,8.878727,-2.417504,4.397012,-4.894683,-4.662771,4.503968,-8.608005,0.402412,-0.700004,4.852317,-9.273725,-1.276403,8.103400,6.873290,5.251896,9.559543,4.603177,-2.726636,-7.957150,-7.805712,3.227876,3.302233,0.540137,9.075533,-2.538573,9.063605,-3.949153,-7.456043,7.771957,6.818518,1.342054,2.978487,-9.464707,2.980201,-9.495228,6.172491,1.186874,9.218141,4.452474,-0.340181,-9.081312,-0.873261,7.771185,-2.938068,5.778451,6.976082,-7.449735,1.752610,3.416011,-0.943230,6.085735,5.817566,-8.634010,0.187213,1.885057,8.526348,7.414019,-9.354177,1.482966,5.809593,-1.635932,2.298402,8.044341,4.161477,4.003821,-5.141191,0.697323,8.609422,-9.500267,-6.010289,2.523274,7.061317,7.485887,0.850400,-8.391918,7.267678,-6.027908,-4.919974,-2.461129,-7.432601,4.972933,-1.857506,-3.875411,-9.389941,-0.717563,0.243209,1.446454,-5.023826,-9.360326,3.217290,-0.557193,-2.775563,9.458872,-0.550656,-8.136592,1.209599,9.549670,0.988063,6.680789,-2.505059,-2.072993,1.305538,1.095146,-5.262771,-8.440352,-4.693554,4.470131,4.853539,6.020945,-4.459798,-9.540615,7.950229,2.160320,9.075868,2.787787,-1.197393,3.176950,1.534188,5.225314,1.019820,9.879354,-2.024553,-1.154756,8.598863,5.932424,2.589705,5.766544,5.541224,8.465647,1.955822,-9.421508,-8.663356,-5.860854,-8.125014,-5.101666,5.096496,-1.202351,-5.062773,8.280478,-4.709721,2.934900,-8.435325,3.691746,9.442022,-6.274857,4.238402,-0.840942,1.006312,6.314430,-3.759079,7.580321,3.743914,9.286695,-0.627871,3.781156,9.154870,-1.043787,4.371485,5.962561,2.583654,0.872025,-8.936968,-2.192539,-9.401023,-5.459535,7.886815,-9.927823,2.640669,-7.061771,-7.542046,-6.369669,-9.085784,0.394174,-7.555159,-7.969007,8.478794,-4.241878,9.155721,6.439849,-4.128960,-8.896247,7.154741,-2.375413,-9.822755,-7.028969,-9.862413,-6.915444,3.478008,-5.756673,-6.132049,3.276172,5.932053,-1.503079,9.797880,-8.108918,0.137551,7.967987,-2.979665,2.509037,4.785267,9.389783,-0.583141,-5.886917,-9.330445,-6.829108,-4.064575,-1.884364,1.251325,-2.637448,-8.052328,3.990155,-3.824988,-8.646956,-2.877021,7.726918,4.781384,-0.467814,2.319428,9.656550,0.348727,-4.493537,-5.697388,2.189937,3.389043,-6.458197,9.728862,1.407597,-7.349345,-4.545639,8.137577,-7.605787,-0.679414,1.285642,-2.308220,5.166954,-0.728797,0.409587,-0.395844,-1.684182,-3.649961,6.287531,-0.614569,7.674467,-6.002578,-0.460021,-1.177571,-7.908642,1.684443,-2.899092,0.710041,6.209269,2.791785,-4.684389,-1.907837,-3.429375,2.255928,-0.899836,-1.733629,-4.162539,4.539326,4.081121,-0.915448,-0.955048,0.549804,5.497943,0.456317,-9.559267,6.213630,-7.444799,6.294840,-6.030051,0.885906,4.904264,1.043024,-4.557386,-3.045699,-8.282492,-7.190835,-6.049541,0.582704,-0.069793,-9.579216,3.750241,7.282978,5.196790,-8.538675,9.836221,-8.897721,-1.886092,-2.338703,-6.151274,-3.579185,8.444179,-0.191214,-6.982726,3.337270,-1.885305,9.540134,4.460514,4.813031,7.288656,3.376123,3.735051,1.150250,2.444752,3.555011,-5.178314,-3.189123,-4.476563,9.369199,-6.848198,8.772845,9.850057,-2.065208,2.633353,2.845669,-5.349496,8.813717,2.016140,3.254962,-2.901860,-5.336024,-3.112106,9.143617,5.648568,4.184416,7.326236,-1.764868,6.994144,-5.198205,9.190822,7.994967,-3.563510,6.402046,-3.260374,-5.767534,2.545517,8.249540,5.518780,-2.970858,-3.904873,-5.805892,-0.407272,-3.912777,8.641398,-5.091729,-6.150198,-7.312113,-0.399833,-4.095069,-1.442064,-3.599572,-3.879348,6.392802,-0.060833,-6.203362,9.374151,-5.548756,-1.472243,0.595027,6.106028,-9.387849,-6.810442,-8.768154,-6.990740,6.525802,6.865350,2.152844,3.233167,9.324423,-2.114166,-6.797530,-8.138250,-6.682343,4.288493,7.678641,3.954194,8.385559,-7.252902,0.943785,-3.876280,-9.899509,-2.369469,5.100689,-0.954195,8.958956,3.732187,2.328003,-7.175573,-1.064392,5.224236,5.859092,2.216211,-2.946960,-9.394377,-1.682883,-9.397627,1.837963,-0.444765,9.190128,9.137890,-8.166974,-4.887965,7.479448,7.525241,8.890551,6.710969,7.700775,5.788214,-4.710094,6.536962,-3.457818,2.534900,-3.408670,7.139545,5.802860,-0.238128,1.141696,0.171594,-8.926743,-3.191899,9.625969,-4.903747,-8.054393,7.572405,2.610170,0.010206,-0.529921,3.582062,1.083316,-4.396151,-3.808319,-6.386487,-4.125862,-1.759761,-6.487769,-1.912820,-7.255221,-2.722965,-3.793309,7.531064,8.069368,6.904068,-6.822515,-1.483539,8.615624,-2.918846,-2.978195,0.793816,-2.771766,2.764409,-1.212455,-5.796456,-9.126119,6.368444,-3.919586,-8.985942,-3.103906,-3.433570,2.305221,-4.301533,8.596671,-9.266325,0.567404,-4.025211,6.224808,-1.243339,2.927653,-5.332924,0.372909,-0.420481,-3.976210,7.044294,3.667994,5.544429,1.372723,9.154052,-0.949928,-0.636806,-0.874326,5.007092,-8.310536,3.650153,3.519411,4.317566,-0.756659,-3.534103,-1.351753,3.995280,7.320117,-6.469503,-7.142390,-5.761288,8.785667,-0.167520,9.249932,0.954330,2.946909,-0.177715,-1.512578,4.586285,0.827939,-1.644747,-4.364782,6.337859,-5.846498,-2.384715,-5.023505,-9.364285,3.312213,0.551051,-8.400146,-2.702579,0.916540,-4.378582,-8.808703,-1.945061,-2.975411,6.846042,-3.581926,-4.475587,7.492495,1.187049,5.636759,8.118991,-4.810651,-4.824715,-4.354431,-0.401185,6.778581,2.687964,3.362032,7.569472,-5.756132,-8.389984,-4.397280,-0.379216,6.783413,9.963345,6.338244,6.574653,3.083958,-5.441291,-5.009343,8.862263,-9.214193,3.464468,2.750936,5.144468,7.703631,-7.670256,-5.391676,1.918572,8.733926,6.336968,-5.229990,-4.770148,-8.949979,8.647340,-7.718228,-5.938410,4.403035,-9.752239,-3.815833,5.177510,9.856508,5.799126,-4.756073,7.241001,9.642587,-9.552597,5.269062,8.966942,7.831596,-9.578212,-2.718451,-7.910969,-4.656926,-7.924407,-7.554426,-7.876267,6.577396,-8.074569,7.708834,5.651554,-9.657266,-4.897031,5.066064,2.137520,-7.539976,-1.999279,-3.028614,-6.199938,6.013942,5.101343,-2.576697,9.948868,-8.933106,4.431805,1.564116,-6.664124,-0.869081,4.377693,2.061988,5.984019,-4.902523,-9.026318,-0.383055,5.227446,2.698520,-1.994675,-3.445621,5.051696,5.256532,-2.698064,-8.426038,-1.633190,9.766344,-7.630168,-8.752209,-7.990268,5.152351,9.710702,-3.489558,6.368471,0.229547,7.631787,3.084263,-4.839875,-1.755171,5.277332,-2.431423,0.685777,3.650347,-7.734971,1.800491,-4.414565,2.767710,3.783110,-1.589015,3.216986,-7.015254,8.428103,7.397192,-7.648557,4.275606,-4.308399,3.303859,8.600860,6.281757,-4.897536,0.644395,4.157341,-4.793763,-8.112394,3.747316,-5.429814,-3.768788,9.768338,-7.098633,5.540067,1.813326,0.557985,-6.294429,8.490883,-1.479536,-3.321810,-0.633231,-0.750273,-3.431535,8.886303,-5.852410,0.220521,-0.798044,-7.786711,-5.089447,-7.808937,-8.470257,-5.937055,-2.870075,-1.789327,5.544970,-9.963670,5.899015,-6.539636,3.328316,9.040157,-0.930990,6.366637,-5.772413,7.701438,7.707850,-8.051572,7.537558,-0.407260,0.611300,-1.779987,-2.168204,-8.056164,7.895787,4.642692,7.884885,-2.821984,-9.772736,-1.994923,1.423155,0.971814,2.721849,-0.171719,9.766526,-7.887636,-7.703806,5.763354,-9.294108,-6.780148,5.706736,-2.499805,-4.909416,-1.037615,-5.557449,5.542784,-4.787937,6.601649,5.287306,-4.425559,-3.194454,5.576690,7.330787,7.947460,-1.868285,7.749871,-3.661129,-2.308156,-7.540103,2.804585,4.612862,-7.234878,3.207302,2.145679,-3.109980,4.560534,3.988378,1.184566,-9.230027,-4.798903,-6.688444,-1.061691,2.393466,2.956865,3.854872,9.949036,-6.899837,-4.538851,0.640361,-3.522446,9.877979,-7.539445,-0.913134,7.431684,4.468523,7.105752,0.837726,-9.025060,1.923639,-6.373886,-5.095993,5.307343,4.066176,-1.127410,-2.449987,-6.318284,0.663662,-8.272586,-2.966483,-0.249457,6.741091,9.134199,9.378126,5.811560,-5.219964,4.616189,5.664498,5.033664,-1.105344,7.167156,-5.566736,-3.719553,2.262609,7.996118,-6.746588,1.638704,0.657098,-6.317044,-8.708202,4.945148,3.317912,2.923627,-0.460841,2.905673,-3.144655,2.672937,1.053041,-5.180748,-9.880569,-6.532867,9.721210,-3.594748,4.902207,7.237217,-6.197011,-4.860424,8.389612,0.294022,-3.123573,-5.904210,7.545158,0.304137,2.824842,3.337322,3.110260,-9.614280,5.149645,5.374745,3.234486,-6.145467,-2.967548,4.866550,-3.515751,2.411117,-1.658482,-2.132396,8.982164,-2.334089,1.648405,-3.744973,2.279848,-7.150044,7.254651,5.231907,-0.583956,-3.188292,-2.041273,6.018087,-1.980479,6.623263,-7.710997,0.278688,6.724423,6.002080,5.627169,4.490440,-0.243413,-8.961328,-3.920728,5.171686,5.349512,2.888935,1.037939,9.429018,6.830311,-8.439435,-6.971239,9.315867,6.166090,-1.648690,-0.392206,-6.719784,8.287897,-6.556556,-5.451584,8.042308,9.008472,-8.325782,2.745054,6.618459,-6.187209,-3.033407,9.084786,6.979152,-7.697663,3.508089,4.315702,-3.956663,-4.630924,-3.142733,-7.051112,7.115948,-9.488779,-6.980411,7.968446,-8.341293,-3.627069,-0.808568,-8.382078,-9.653251,7.172315,6.463917,6.872135,-4.104131,-7.195086,2.792616,-5.296389,0.548489,-2.660549,-2.996211,4.234970,5.551986,5.144095,2.976619,6.806630,1.698410,4.812243,-8.993680,-2.342302,5.683432,4.883159,2.631153,2.070024,6.707076,-9.537936,9.592758,-3.525155,4.559719,-9.036426,-1.595051,8.812735,-3.722570,-2.174634,5.744669,1.099703,-5.048814,5.263296,-9.052688,-0.320295,-1.525091,8.943811,-9.905184,4.189415,-9.434801,-5.926346,0.024867,-9.885298,-9.266668,-7.103135,9.461616,-5.935432,5.275525,6.760690,-9.434817,4.108403,-8.671946,-0.516396,-2.443763,4.063880,5.472205,7.329075,1.648687,7.295988,4.969670,2.262541,7.618021,-0.384253,-0.267543,1.214507,2.974014,2.869872,9.631925,-9.535644,7.597908,-5.424702,6.612236,-9.067926,4.647913,-0.608782,0.091187,9.565872,-3.034984,7.784428,3.722374,4.056900,1.324754,0.241497,9.842226,2.498137,6.416018,5.128368,4.475505,0.953804,5.697973,8.210693,3.943124,-8.332330,-5.242179,-1.610773,-6.701551,-9.928877,8.701650,-9.295091,0.567293,9.423959,-8.288370,5.332966,-1.390513,-4.731341,0.745812,0.598027,4.157430,-9.967503,1.362613,8.110689,-5.872385,-8.158145,0.491445,-2.106444,-8.768446,2.256487,4.916365,-8.193300,9.626995,5.047969,1.808404,-1.201823,-6.433021,-9.331365,3.446220,2.053206,-7.938071,7.652944,8.119473,-9.735277,-4.386382,-7.216923,2.282183,8.542792,8.332162,4.972294,2.209982,9.844875,-1.538514,-7.364135,-9.826190,7.133520,6.935095,-5.566399,7.234004,-4.567103,3.966489,1.848842,4.057562,0.612801,8.161090,1.978889,-5.667442,3.452074,6.440508,2.987405,4.080795,-9.097698,2.905643,8.708094,7.289661,-7.168171,-9.071175,1.125081,4.504935,2.052988,8.802272,1.012534,9.369999,-3.950358,-0.831919,-3.000458,5.761602,-5.842520,-9.095142,4.286558,7.215333,-3.238413,1.805793,-1.496752,-6.631740,9.192576,-8.110147,-9.989659,8.071220,-5.439994,-4.259768,-5.108105,9.831436,-0.773274,-8.706331,-8.067736,-7.550602,-9.505972,-9.259815,-6.283579,-3.056968,4.819797,-1.249826,-1.632309,-0.393126,-5.336690,-8.575120,-0.790391,8.963766,5.846939,-1.666157,-9.524750,-9.818715,-8.785701,9.516901,5.136575,0.856813,-8.591480,-4.205576,3.950329,-8.595720,4.402168,-6.859943,-5.758138,9.083550,-5.044839,1.908030,-4.192000,7.048778,5.228429,8.961822,-0.731734,4.886410,-4.246398,1.338133,-5.124838,9.426493,-8.869593,-4.823743,-9.357751,-1.960602,6.090991,1.988898,7.447205,8.716138,5.620123,-5.606408,5.213899,-3.773760,4.275293,1.977462,3.655309,-9.662877,2.361727,1.395069,-7.804917,-4.614893,7.366131,4.673477,-6.123935,1.591807,0.286972,4.674049,2.458775,-7.353063,6.022663,1.779828,5.981417,9.660298,-1.121270,-2.120250,-4.267647,-8.225988,-0.708637,1.496475,-4.484287,-7.771079,-2.975060,-1.069666,0.426166,-7.926811,6.443926,-9.908374,8.376917,3.878681,-1.585669,-6.070787,-8.106051,-4.286732,-9.607956,7.243311,8.838537,-6.757474,8.828715,5.431587,-5.654868,4.744664,6.266915,-9.177276,8.886010,-6.153166,5.637461,0.831817,-5.813127,-3.394067,5.969179,0.994408,6.079340,-2.553563,7.266129,3.963678,0.059859,3.678100,-2.866648,-0.565405,2.645943,3.090747,3.456017,-1.017934,4.892017,2.787609,-5.618818,2.037287,-0.654592,-3.335460,5.597309,8.355404,-4.703257,-5.065273,-5.414908,0.410818,8.124636,-5.346068,5.007841,-3.427994,5.673400,8.940280,6.267698,3.969568,-6.216590,1.587452,-6.435839,-7.272068,5.796030,6.623125,9.760004,0.965146,-0.926422,-2.873070,-0.229692,-3.810492,-0.561957,7.359077,-5.590480,8.895447,-0.250574,-9.681903,-1.008446,3.089492,8.346472,1.924836,0.495740,-4.645624,8.866330,2.625331,5.131820,5.582721,9.126323,3.831219,-1.953997,-4.329088,6.461516,4.378354,-3.165698,9.275953,7.325495,-4.594426,1.844761,-8.749614,4.583021,-2.022380,5.478624,-0.110673,-6.948937,-6.700686,9.127373,7.122563,-6.014360,-3.882326,-2.553894,-1.379027,-6.652339,-5.320868,8.382706,-3.956061,2.454094,-9.334413,5.045233,8.137788,-0.530534,-5.948966,4.172787,0.681388,-6.561019,-8.605270,6.033075,-6.439816,6.741136,-1.780383,-6.343824,-2.208571,3.176446,-3.592917,0.566522,4.446521,-5.025525,8.847786,5.420097,0.883244,-9.073559,-3.968588,-4.963683,-8.663742,-4.766448,2.996204,1.377506,-0.379036,-5.239497,5.494956,-7.612194,0.484414,-3.197327,-6.416208,3.203340,2.707914,4.752745,-3.126744,5.674019,-5.794756,2.809886,-4.441601,1.720510,1.698580,6.444577,3.287983,1.983158,-1.474627,-4.503967,-4.350362,-1.807065,5.369523,2.207511,-7.177012,-8.234788,-8.702179,-7.925232,1.282818,1.955448,1.992274,4.511630,6.449273,5.647256,0.395428,-1.154264,-3.577410,7.837689,0.925469,2.695308,3.558787,-9.369692,3.718819,-7.134278,-2.263507,8.051975,6.432956,-3.721773,-5.449094,-3.405759,8.695290,5.759891,-6.149845,-9.960969,6.759980,1.560422,8.996448,7.483555,-8.771874,8.377812,4.474061,-0.589618,-9.564449,0.177670,-7.857846,-3.421915,3.291265,9.596965,-3.073638,9.379918,0.189933,5.139216,-1.950592,1.416198,-6.114516,8.375635,-2.568462,-6.089794,-2.078026,7.334162,-3.552511,0.861253,4.171093,8.028683,-4.233251,8.252442,2.993169,-2.387597,7.075232,-7.215643,1.808731,-5.772554,5.826413,-0.844669,-7.751195,-7.000889,8.249991,-7.113095,4.444569,-0.796669,-7.454203,2.292818,-0.195615,5.014453,-7.293125,-9.884105,0.194133,7.682291,6.287308,9.214333,5.763379,-4.359301,0.071454,7.235058,-0.437125,-5.119920,7.780475,-7.457235,6.627587,-4.733280,8.478910,5.008205,7.016164,2.627575,-3.800210,-7.097608,9.166033,-0.161446,-1.484633,9.227315,-8.688665,5.106646,5.191664,7.305398,-8.685207,-5.100649,-0.145029,-0.159273,-5.691051,1.794400,-9.190495,-4.374057,-1.495472,-8.601235,-9.305146,-0.092110,5.870564,9.518832,5.436266,-0.411071,-8.755032,-5.752163,-3.958280,-3.253784,-6.300022,-1.219726,8.763846,-6.146567,1.952029,-9.504301,-2.605160,-1.478429,7.587622,3.585574,9.168296,-4.184716,-1.297398,-9.329376,0.828822,-8.889019,-1.784833,4.014714,8.830516,-9.762248,-4.430696,7.375540,8.755173,9.797944,6.655944,2.408288,-3.783242,-2.136141,-8.963575,5.476686,3.117851,-1.698396,-8.287307,1.109435,3.599755,1.324264,3.341640,9.779738,-9.950417,3.666169,2.171668,-4.487695,-0.776859,-5.147526,-5.120301,-7.875186,8.851898,7.351112,-6.076036,-6.984570,-5.213995,-6.115762,-9.442867,-4.030806,-6.087698,-6.005602,1.984224,5.956677,6.776182,-8.541670,9.420754,6.143880,3.254601,1.491383,7.795228,-6.537678,1.963140,6.406086,-7.955346,-2.461295,7.309676,-9.817859,-5.049206,-0.619376,0.428496,7.743487,-7.430156,-7.484834,7.036230,6.822545,2.092525,7.378382,-3.301329,-2.775186,-5.108035,4.451498,3.721593,-1.329099,5.691699,1.437497,-8.178866,-1.133987,0.313543,-9.454021,-7.635892,2.079853,1.135371,-3.539307,-9.714784,-7.274191,4.114860,-4.631631,6.982284,-6.869819,-3.098515,-3.296361,-6.529247,1.741036,0.813893,4.146129,4.040921,6.532366,1.064040,6.227659,-1.660935,-5.406187,0.632290,-1.107850,-5.017365,-4.876651,-9.637208,7.094870,1.099599,-2.299477,-7.157559,-3.235922,-9.215165,0.604042,7.009336,3.344498,-2.227115,5.502467,4.572470,0.772140,4.661132,-4.732304,-1.139575,-3.395841,-7.744148,-5.241268,-7.916675,-6.279791,-4.152789,-7.538849,-5.743502,1.230858,-0.427715,7.491825,-7.187276,0.992061,-7.287810,4.575940,3.891681,-8.650189,-3.388221,-7.924239,3.793969,3.069444,-6.435225,3.318749,-4.255689,-6.471268,0.720302,-0.587464,-2.409514,3.743095,7.024503,0.777594,1.151201,-6.951111,-5.271793,-8.984787,4.797487,0.844427,-5.582866,6.003350,8.649057,7.192586,4.747302,-1.423863,3.579943,-0.388225,-6.188402,5.743799,7.990125,0.249250,-5.254560,4.367555,6.660044,-0.029996,1.122314,-6.535629,3.410407,6.220596,3.712347,-9.103081,-4.401294,8.245215,-6.060509,-6.902664,-9.966514,5.598932,6.680215,9.700711,3.105309,-6.651741,2.708322,8.119822,-5.437439,7.211424,-0.054799,-8.931185,-3.763237,5.119657,-7.126940,-8.798182,8.365836,-8.495495,-0.798783,4.059415,0.638297,-1.974271,8.912393,4.280276,-6.115180,9.536072,-4.041515,0.513019,-0.861258,7.076968,-7.183924,2.979085,7.783251,3.290984,9.268963,8.608468,-6.396157,7.750624,6.347137,-3.461065,2.711103,-2.896997,4.419535,-6.653083,-3.398648,1.537687,2.648329,-3.055167,-1.495738,-7.618716,-0.750996,-2.615952,3.568558,-5.150239,-1.563199,0.206037,2.128477,7.758675,3.098454,-7.253760,7.833149,1.013006,-9.843741,0.521885,7.699032,2.955165,1.191451,-0.573172,9.001127,9.074963,2.791390,-8.856308,-9.394569,-3.093288,1.571030,6.722315,-8.419231,-1.672987,-7.369428,8.597075,9.708261,0.527482,-2.693103,-6.992069,5.757821,0.524380,-3.501437,6.417108,2.563090,-2.942978,-8.777639,7.401451,-4.737670,1.822307,0.157733,-2.913568,5.858923,4.430754,-7.607066,-2.550967,0.243480,-9.381147,3.595002,-0.014761,4.912173,3.672999,-0.838600,-2.106033,-9.847975,3.676133,-4.380628,7.445710,6.768522,9.570808,-5.592454,3.672419,1.560543,6.868490,1.336481,8.058745,-9.481233,-2.676376,4.842938,-4.755601,7.691252,5.066283,5.536009,1.246115,9.199497,-0.552206,-8.096704,1.136582,-1.219803,-1.943890,-4.227033,-6.955016,7.742703,7.401627,-2.129459,-6.006742,5.388249,1.744716,-2.365474,-1.919954,-0.596166,2.708935,-7.067262,-5.344496,2.741128,6.348922,4.994176,8.256286,-4.989124,8.561723,-5.620201,-6.870622,-3.931913,-9.102918,7.753990,-9.957355,-2.754366,-3.583470,3.801625,2.182254,-7.002124,-2.792089,-0.946483,-1.533403,6.548007,1.975732,5.864630,8.217198,-3.328226,6.438550,-0.050558,9.851126,9.988958,-1.933468,-3.229213,-7.740043,-0.025478,-2.543918,-8.007100,6.445869,4.564748,7.807037,4.920755,-2.128032,-2.949699,2.093237,7.944231,9.909856,-2.637486,0.183064,0.482515,3.632677,0.513782,9.898439,-4.278449,5.894442,8.221931,9.931582,1.834687,-0.835158,3.382983,3.710933,-0.403153,3.182518,-2.415177,-8.277705,-2.280943,8.687643,8.822629,4.713090,0.742077,8.090015,3.894155,9.154450,-0.564220,8.184300,7.600904,1.012722,0.984716,3.675369,2.250341,-1.325819,5.768108,3.223569,-3.488030,8.117278,3.520119,-8.379447,0.777174,-7.736902,-6.601138,9.862919,-1.652292,6.035792], dtype = "float32")#candidate|3027|(2310,)|const|float32
const_3028 = relay.const([True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True], dtype = "bool")#candidate|3028|(880,)|const|bool
call_3026 = relay.TupleGetItem(func_864_call(relay.reshape(const_3027.astype('float32'), [14, 11, 15]), relay.reshape(const_3028.astype('bool'), [880,]), ), 0)
call_3029 = relay.TupleGetItem(func_868_call(relay.reshape(const_3027.astype('float32'), [14, 11, 15]), relay.reshape(const_3028.astype('bool'), [880,]), ), 0)
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_3031 = relay.TupleGetItem(func_1550_call(), 1)
call_3032 = relay.TupleGetItem(func_1551_call(), 1)
output = relay.Tuple([call_3021,call_3026,const_3027,const_3028,call_3031,])
output2 = relay.Tuple([call_3022,call_3029,const_3027,const_3028,call_3032,])
func_3055 = relay.Function([], output)
mod['func_3055'] = func_3055
mod = relay.transform.InferType()(mod)
mutated_mod['func_3055'] = func_3055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3055_call = mutated_mod.get_global_var('func_3055')
call_3056 = func_3055_call()
output = call_3056
func_3057 = relay.Function([], output)
mutated_mod['func_3057'] = func_3057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3055_call = mod.get_global_var('func_3055')
func_3057_call = mutated_mod.get_global_var('func_3057')
call_3091 = relay.TupleGetItem(func_3055_call(), 2)
call_3092 = relay.TupleGetItem(func_3057_call(), 2)
uop_3102 = relay.exp(call_3091.astype('float32')) # shape=(2310,)
uop_3104 = relay.exp(call_3092.astype('float32')) # shape=(2310,)
func_2726_call = mod.get_global_var('func_2726')
func_2727_call = mutated_mod.get_global_var('func_2727')
call_3119 = relay.TupleGetItem(func_2726_call(), 0)
call_3120 = relay.TupleGetItem(func_2727_call(), 0)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_3133 = func_335_call()
call_3134 = func_335_call()
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3136 = func_1075_call()
call_3137 = func_1075_call()
bop_3148 = relay.floor_divide(uop_3102.astype('float32'), relay.reshape(call_3091.astype('float32'), relay.shape_of(uop_3102))) # shape=(2310,)
bop_3151 = relay.floor_divide(uop_3104.astype('float32'), relay.reshape(call_3092.astype('float32'), relay.shape_of(uop_3104))) # shape=(2310,)
output = relay.Tuple([call_3119,call_3133,call_3136,bop_3148,])
output2 = relay.Tuple([call_3120,call_3134,call_3137,bop_3151,])
func_3162 = relay.Function([], output)
mod['func_3162'] = func_3162
mod = relay.transform.InferType()(mod)
output = func_3162()
func_3163 = relay.Function([], output)
mutated_mod['func_3163'] = func_3163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_3209 = func_579_call()
call_3210 = func_579_call()
output = relay.Tuple([call_3209,])
output2 = relay.Tuple([call_3210,])
func_3216 = relay.Function([], output)
mod['func_3216'] = func_3216
mod = relay.transform.InferType()(mod)
output = func_3216()
func_3217 = relay.Function([], output)
mutated_mod['func_3217'] = func_3217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_3229 = relay.TupleGetItem(func_947_call(), 0)
call_3230 = relay.TupleGetItem(func_949_call(), 0)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_3253 = relay.TupleGetItem(func_188_call(), 0)
call_3254 = relay.TupleGetItem(func_189_call(), 0)
output = relay.Tuple([call_3229,call_3253,])
output2 = relay.Tuple([call_3230,call_3254,])
func_3273 = relay.Function([], output)
mod['func_3273'] = func_3273
mod = relay.transform.InferType()(mod)
output = func_3273()
func_3274 = relay.Function([], output)
mutated_mod['func_3274'] = func_3274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_3382 = relay.TupleGetItem(func_1171_call(), 1)
call_3383 = relay.TupleGetItem(func_1172_call(), 1)
uop_3388 = relay.log10(call_3382.astype('float32')) # shape=(14, 1, 15)
uop_3390 = relay.log10(call_3383.astype('float32')) # shape=(14, 1, 15)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_3400 = relay.TupleGetItem(func_188_call(), 0)
call_3401 = relay.TupleGetItem(func_189_call(), 0)
func_3273_call = mod.get_global_var('func_3273')
func_3274_call = mutated_mod.get_global_var('func_3274')
call_3413 = relay.TupleGetItem(func_3273_call(), 0)
call_3414 = relay.TupleGetItem(func_3274_call(), 0)
func_2648_call = mod.get_global_var('func_2648')
func_2650_call = mutated_mod.get_global_var('func_2650')
const_3427 = relay.const([[9.701480,8.734842,3.778408,-3.344706,7.083947,5.100375,2.850507,9.996990,-7.954179,-1.926128,3.450542,-7.344707,-3.752247,1.263225,-6.534303,7.245649,-0.011216,-1.873945,-2.682887,-1.655907,-5.072421,1.203012,7.592540,0.791567,4.098263,-4.306811,5.104089,-1.651001,-3.221704,0.161236,2.134387,5.942024,3.380780,-2.631833,-0.591455,5.808312,-8.934063,-9.489248,3.550398,7.325751,1.966937,7.389667,-6.650172,0.070042,9.128472,6.141741,8.202874,5.942740,-9.770775,-4.005297,-5.113559,-3.103660,9.014254,-7.643114,-9.966000,2.570562,0.256013,3.635317,-1.058096,7.871093,4.619224,-8.208160,1.932662,5.602311,0.407832,-6.400528,4.220462,-1.186688,-3.776048,-2.297814,3.851283,-2.956397,-6.672722,-3.977535,-4.417431,1.622295,2.117248,-8.905265,3.348275,-2.562348,-0.869529,-1.680178,9.517144,-6.682521,-9.847117,5.446642,-1.955453,-6.064425,9.279095,2.600411,-6.993554,1.446699,-1.435516,-5.481634,1.482267,5.751118,-1.457871,2.281876,-3.298608,1.084165,-3.575950,-9.219350,-0.636534,-5.162572,-6.614754,-7.513834,-4.347707,-2.127413,9.372130,-1.209669,6.003448,-6.235895,3.799349,-6.913193,1.215648,-1.927665,-5.809095,-8.586055,-8.214961,-5.375832,-6.298022,8.025198,-5.954989,-1.030150,6.072885,-0.627369,-7.936965,-4.683017,-7.107657,7.679041,-2.556633,-1.269500,1.743744,1.205846,8.274817,-5.173514,-4.457600,-9.849792,5.376037,4.553618,0.976608,0.601128,-4.632647,9.293600,-6.294137,7.848151,2.813577,5.276403,-5.822133,-9.287488,-3.491352,-9.356263,-6.987430,3.487259,2.609137,-9.427957,-3.010934,-5.962577,2.877796,-3.119273,-5.658437,-8.112431,9.974335,-1.923082,3.259424,2.683718,6.898536,-4.480271,-7.886290,5.593545,-0.275950,-6.539903,-9.003858,-4.073083,-8.871373,0.043464,-2.954906,-0.011693,-7.289395,6.289526,7.432673,4.681582,-5.227391,9.864345,-2.635326,-3.958425,-9.596658,2.580677,9.087581,1.271452,-6.590348,2.117847,-9.925102,-6.869871,-3.362062,-1.789434,-3.261733,3.046284,-5.321180,6.917683,3.513819,7.984512,-6.848163,-1.942697,-3.039603,-3.613988,2.146062,7.812537,7.129113,-8.156305,-5.117269,-9.100956,-3.086526,5.646748,-4.418896,4.817463,2.966645,0.650944,-5.968481,0.419962,4.073960,6.371615,9.506600,4.266258,5.004057,2.872578,-1.289577,-8.625765,0.516569,6.544307,5.563756,7.958117,-0.064312,-8.348976,5.347082,0.515983,9.468084,0.901164,-4.498905,-6.274226,-6.476691,9.992399,9.374166,4.810162,2.933159,-9.655459,-5.527391,4.356770,-9.320974,8.723025,-1.952196,6.633244,9.992413,-8.835629,8.447463,8.600632,-3.813150,-5.282492,1.682064,-3.956359,8.202841,9.681425,4.344118,-4.139314,-6.236333,2.177807,-6.158750,6.087004,0.332283,6.230878,-1.802744,-5.658887,6.954642,-1.136963,-8.067740,-1.393806,8.717494,5.312362,-7.629007,-4.765246,0.318199,1.415331,-7.541815,-6.628863,1.357419,-8.735212,-4.630244,-8.709424,-6.157834,-8.034546,-5.508481,-3.131490,-8.392241,-8.411953,1.586895,-2.552744,-7.288741,-1.913844,-2.593713,-2.812572,9.444499,6.619842,0.916755,5.049560,-8.486173,-3.677947,-1.899670,-9.660680,8.747892,-3.187171,4.464527,2.475554,-8.502716,8.169878,-5.797431,-1.907987,-0.264787,-6.765046,-7.778420,0.592437,1.569757,1.904111,-2.680316,6.624581,-9.929693,-9.590765,-5.650841,3.372307,-7.239517,8.441705,-5.982888,-7.875848,5.186864,-4.749924,-0.697062,-4.099703,1.744894,-0.465189,8.753401,4.457025,2.101420,9.077695,-6.827229,-8.221715,7.539703,1.648900,-8.638896,0.422675,-9.872615,3.243426,3.777395,4.252804,4.730117,3.388328,5.343243,-8.707037,-0.570039,-9.121191,-4.851747,7.433161,-4.577728,7.536141,-7.502675,-1.733892,-4.420142,-8.026840,7.752653,-2.457727,6.866024,8.923261,7.218479,0.245351,6.033776,-8.580468,-1.639847,-7.914470,-3.573269,5.633679,-9.899163,-8.924725,8.922961,-8.846695,-4.492698,7.012257,-1.041529,-0.388959,-1.932233,-5.129279,4.645987,4.987437,-1.077382,-5.062655,6.784122,-8.013537,2.284462,-7.526134,0.966829,8.452788,-8.832242,1.673451,9.761310,-1.750094,5.314731,8.918930,1.138533,-1.917024,-3.063125,-0.562763,6.650558,9.756359,9.592017,7.425925,6.700301,-3.553827,-5.257032,-9.538455,5.898989,8.700868,1.113983,2.749461,-5.369616,0.490606,-8.149040,-0.779165,-0.405013,-4.492412,-4.346617,-5.905161,-2.013702,3.174945,-9.402857,-5.119552,-8.718377,-6.011593,0.420463,-1.656005,1.959740,-3.189386,7.029436,3.969605,6.018727,-3.735241,-7.407937,4.156272,7.718462,9.785113,-1.342635,-7.601738,0.687592,5.782546,-0.834797,-7.400502,4.157729,-8.806156,-3.207609,-1.175249,7.696498,3.922916,6.355611,7.946189,4.740154,-8.672657,-3.712780,-3.996103,7.456660,-5.677330,6.227582,0.198075,-9.956949,3.407663,-2.557194,-4.980191,-4.232656,5.448744,-9.451112,5.228316,7.607364,9.817918,-4.043102,7.565194,2.917387,6.965955,2.750052,9.231726,-6.157642,-5.992027,-6.975921,0.952838,-3.564648,-7.744871,3.910610,-9.023406,8.540835,-5.041620,3.157446,6.853399,-4.024975,3.757783,-1.653113,2.136489,5.421167,8.614787,-7.380441,5.100127,3.162080,3.671409,7.198463,7.081131,1.291810,-3.401931,6.582448,-5.610469,-0.012444,6.683412,-7.588957,-1.122374,-8.851476,-4.975788,-2.033327,3.504864,6.167481,-4.828649,-6.421088,-0.194216,0.402123,-6.385938,-6.553698,-0.944977,-3.635178,4.951071,-7.630600,2.049545,2.058168,3.118077,7.608373,5.240682,1.996148,9.545249,5.325181,-5.470754,-8.910847,-6.308552,0.561642,5.764997,-7.468796,-2.972139,-1.232536,-3.318168,0.419565,6.135940,-5.806962,-1.681906,-8.916458,-2.567061,1.743149,3.256744,8.555409,-1.972634,-8.536250,7.935999,8.400574,-9.092131,5.180436,9.417312,-2.349303,1.228430,-4.878116,8.537707,4.823316,-6.939782,-6.168929,-9.871796,8.395917,-8.269223,-4.421231,4.493722,8.641015,-8.854656,-0.430184,-0.875994,-8.342168,1.189874,4.419221,-5.934385,-8.251627,0.186725,-9.528697,8.621131,-9.296645,8.077408,4.154828,-2.013103,-1.519915,8.661005,0.246922,-1.579118,8.434906,-6.483369,-4.233216,6.508120,0.580346,2.707607,-4.593241,-9.210594,-8.145565,0.979239,-8.182570,-1.594760,-4.523934,7.147148,6.069171,-1.852877,5.774880,3.811707,1.025264,7.095254,3.166596,-5.402428,7.573243,6.111407,-4.844986,7.802030,-1.450020,-7.137210,2.677302,-2.117661,5.024198,9.378173,3.762080,-9.762231,4.962313,-2.528746,-0.104049,-8.398749,6.164679,0.904852,-5.625629,-1.668781,-9.117622,-5.974338,-8.527487,3.569067,0.817642,-8.687164,4.976146,8.464760,-8.243913,-7.683719,-2.907803,-5.884549,-0.087360,7.528965,-7.022146,0.196638,-5.583113,-2.971155,6.883471,-1.975069,-0.195203,4.604846,6.933232,-1.853844,-6.037800,-6.109085,5.620156,-0.460243,-2.200954,6.755428,9.324164,-4.704417,-7.849513,-0.305562,-2.367498,-4.892118,-2.166918,-5.976763,-9.430234,6.863804,8.553975,0.002051,4.749612,-8.525321,1.732080,-3.134968,2.516288,4.399420,-6.544396,0.146195,-5.278899,3.901321,5.413518,5.947699,4.380295,8.390741,-3.101122,1.077028,-7.063817,-8.923017,5.562753,4.220296,4.371597,-4.913779,-1.014453,-9.992870,6.918042,6.773975,2.313876,-1.839658,-8.106824,-4.616625,-5.452736,-7.769805,1.443469,0.859097,0.356458,1.914360,8.706200,-3.011129,7.804949,-1.249813,1.852099,-2.093632,-2.613081,7.511289,-3.120262,-8.032226,8.680423,3.472312,0.568943,-8.895724,4.824189,0.660273,4.003451,9.601756,-1.135098,-6.234297,9.536805,-4.971444,1.158410,-7.361885,0.354632,0.820067,0.313720,-0.173087,8.723284,-1.566180,-2.690431,0.741748,9.363628,9.821907,-6.652141,1.976851,-8.962390,-5.628768,9.396827,8.472307,7.870869,-5.964347,4.631234,1.288204,7.268461,-4.796394,7.758308,5.158048,-7.976536,-5.888294,-9.810687,-3.523749,6.995546,3.687127,-2.153571,-7.488144,0.974487,-2.379611,8.470911,5.620510,3.558236,-3.258062,8.240733,-9.952616,-0.090778,-2.809409,-9.394164,6.060936,3.703649,5.437096,0.754502,0.087719,-0.325058,-4.321414,7.082346,-7.495817,0.144067,5.902530,-7.693612,-9.028852,-1.442725,-1.284184,0.696751,8.054702,-2.519011,-0.328854,-4.804234,-4.254802,-0.507069,-1.952260,-9.117324,-6.248358,7.051582,-6.180598,9.374904,8.457033,1.936771,3.968577,9.960065,-2.880476,1.774314,-8.796684,-2.667390,-5.752050,2.187790,4.432924,0.559516,6.835949,6.432408,-0.320021,-0.577383,1.549957,8.031077,-5.296524,0.757568,-0.538293,-3.607452,-6.843526,7.478567,2.738461,6.838201,-2.604013,-3.063004,2.731654],[6.516531,3.382464,9.078086,-7.766326,9.042303,-8.595496,4.527752,9.939787,7.788056,-7.841344,-7.822849,7.462408,-5.842333,-8.162717,8.012817,9.885235,2.191849,-5.477005,0.921647,-3.152207,0.136521,1.434153,9.621366,-6.578624,-2.402731,-2.589609,-1.486066,-7.910163,0.224282,-2.026872,-7.179542,-4.965497,-2.959009,9.371207,5.751618,-6.055035,-0.859283,0.037806,-1.214005,-0.089563,-9.012694,7.563419,-6.949304,-7.863022,-4.450758,-9.007632,-4.789994,-5.986201,6.673345,-1.999022,5.483609,8.191049,-0.019615,-2.553214,7.293273,8.388142,5.738869,-9.966596,-3.101110,1.529811,6.281749,9.660492,-1.349851,-3.153426,9.317822,-5.237187,8.952301,-0.359929,-4.232101,-6.016776,1.414157,-8.434164,-7.125301,-9.373469,3.248127,2.734416,1.300447,-0.725542,3.976033,6.324171,3.738393,6.403835,-1.860819,-2.527536,-4.969944,-0.389795,-3.509478,-3.687592,2.800349,2.997471,5.313331,-9.564026,4.149334,-0.681522,5.041860,-1.119204,-0.913683,-0.741721,2.885348,8.944442,7.436967,-8.318766,-9.973108,5.586583,8.876708,-8.556372,9.751998,-7.541722,0.519189,2.693222,-3.856228,6.088606,-6.439358,3.961243,-6.093879,9.557412,-3.491359,8.836899,3.662436,9.410908,1.459722,3.818089,-4.972236,-8.915943,-6.294193,-1.917526,7.705315,1.544181,0.633249,5.091396,-9.482315,-9.457108,-6.589972,1.309784,-6.857201,1.758648,9.591794,-5.498636,-1.564680,3.012016,6.505634,8.809670,-5.032715,-5.480852,-5.712159,0.050585,-3.901770,0.918099,-6.092107,-1.348977,7.769190,-1.406867,-2.018178,-8.733432,2.634652,-4.497000,-1.613906,0.184696,-4.572281,-9.174811,-3.174599,8.562866,5.805064,9.864914,-7.982365,-6.832745,2.938035,-0.911092,-1.567817,-1.532494,-6.235633,-9.201362,1.065738,2.182065,3.433638,-2.660361,-8.594034,-5.514029,-1.574123,5.410941,-7.041361,3.533592,-5.627655,8.182859,-9.690587,9.076874,-2.377294,1.988548,0.599417,-1.858746,9.120429,-3.686942,-1.760304,3.371963,7.002378,3.433969,2.312303,7.900354,-1.003791,-3.999891,5.521551,-4.911978,0.330899,2.172252,-9.099705,9.816513,-0.769709,7.188568,-0.494126,4.107024,4.665511,2.227839,4.285532,6.698501,-8.465047,8.684588,3.164815,8.053861,7.117753,1.597150,-8.211766,4.964685,6.665939,-7.532115,-5.828049,7.525637,-0.132807,-3.711184,1.560139,-5.837626,7.864802,8.616595,3.661504,1.767175,7.302164,-9.624904,3.015258,-2.605999,0.294662,-4.783518,5.109706,4.560199,7.586436,4.952304,4.742192,-7.594253,7.993126,0.379017,-3.886152,-0.084202,-6.493444,-2.168199,-3.466707,-5.047673,6.462945,3.581769,-1.937336,-4.519723,-6.759404,-9.625566,7.513147,-7.592376,0.043187,7.222975,-9.925079,3.291811,1.027938,-0.032100,5.191459,6.257427,-9.166477,0.640435,0.368169,-2.714840,5.849088,-8.652039,0.984626,-5.240730,-3.671314,-7.389525,7.016554,1.906887,4.139931,-1.810633,-5.368101,2.099562,7.855407,6.476019,1.971126,-3.262420,1.666290,2.024915,-0.303544,1.131485,-3.052612,7.459089,2.342535,-9.526339,6.089157,6.479627,-3.424785,-8.829598,8.984377,-5.483042,9.974405,-8.374003,8.811523,1.662661,4.023037,6.329604,-6.008149,0.857370,1.089422,7.825783,-3.781143,7.091674,7.916942,-4.748493,0.045889,8.280465,-4.548385,0.855819,-6.502641,4.622880,2.790830,9.790241,0.928429,-4.434306,-5.560942,6.144129,-2.657567,7.571964,-4.065974,1.782227,-3.359912,-8.586703,-9.930404,8.298920,-3.755003,-5.181860,0.144631,-0.943413,-9.659020,6.959044,-1.465476,4.133623,6.347214,-5.785143,3.049809,-3.837005,9.916155,-8.712385,-4.449140,-4.087845,-8.699638,6.172044,-3.520155,-8.303306,-6.440519,9.835852,7.553263,8.504061,9.421272,-0.977889,6.044384,-4.392837,-3.647327,-6.340112,-3.514314,7.896890,8.370002,-4.928312,-8.456703,-9.611270,4.161059,9.454430,8.343698,3.608695,8.252505,1.490917,-8.315333,0.137585,-3.476631,-0.472928,-8.813223,9.139427,-6.324686,7.936026,-1.440612,2.823951,2.551586,-9.727782,6.683599,7.147904,-1.402981,-8.857114,-9.370906,2.337215,6.606910,-5.849879,2.666369,-7.913023,1.901511,4.282508,1.463011,0.272141,2.269297,1.240329,-3.925872,2.011073,2.073344,6.595967,5.316395,-8.297144,-7.021340,-2.742186,-1.740758,5.675314,-8.535667,-3.324537,8.323827,-7.549042,0.277698,-2.156835,-7.916593,-7.155483,2.976201,-6.326284,-2.794503,9.715455,9.198995,9.799388,-9.820606,4.195592,0.897306,3.429430,-9.408843,1.228123,0.908264,1.340289,-4.539496,-4.801045,1.846505,-4.482092,3.982146,0.950377,-3.728765,5.438901,9.692379,4.519597,-8.242189,-5.432997,2.432834,-2.623963,6.126010,-8.516742,-6.165482,7.876626,1.542143,1.694938,8.209962,6.907829,0.858830,3.075924,-2.265716,2.147605,5.119903,6.124645,-9.435345,6.500280,9.871086,3.529034,-5.840075,2.903890,-4.410895,6.315891,5.373444,3.457691,5.542434,-6.259590,-7.957729,-7.441757,6.748970,-3.597370,0.444851,9.933938,0.885050,-0.201059,6.605933,-5.239037,6.559001,2.968927,-8.871329,1.216974,0.735850,0.814790,-3.877249,8.794327,6.779272,0.260582,-3.365707,8.571973,2.656780,9.453115,-7.309587,-5.529525,5.611904,-3.611460,9.510111,1.289458,7.756655,-3.786251,-4.988973,0.508913,8.934069,0.958486,8.608149,8.303830,-4.985715,8.331871,-8.829672,-6.480108,-2.028834,-0.249853,0.842198,-3.268752,-7.246507,-3.121005,7.485660,2.287597,-9.456222,-0.434893,7.762936,-6.360909,-2.321266,-7.793021,1.111811,0.621277,-4.216749,2.458934,9.337581,-0.018006,-4.615513,3.092690,8.479126,-0.995878,3.886381,1.884115,1.111486,-7.363849,-0.697199,-0.270067,-0.093302,6.874947,7.086021,-3.444521,-9.383470,5.084247,5.130814,-2.344491,3.701588,-3.401932,8.690773,4.128275,3.154791,1.013113,0.934776,0.701029,1.560372,-4.031461,-4.508025,3.746510,5.438922,8.154098,5.646971,1.061662,8.741584,3.008619,-2.183119,9.973944,3.300523,8.247650,-2.125723,-9.867032,6.346015,0.222797,5.954178,-5.095801,4.004523,7.631869,-2.451167,0.087175,-9.988406,-6.548683,8.715878,-8.567080,-4.642521,2.039356,-4.503002,-5.136545,-4.254164,7.651765,7.186837,0.382150,-6.309990,6.588825,0.777417,-1.927076,-8.168333,-0.723375,-1.296524,-4.992766,-5.331587,7.462087,8.722650,-5.317994,3.676002,0.240162,-8.784836,8.209420,1.772398,0.044361,6.794024,-3.539659,-4.135034,-7.587196,2.136129,-5.876368,-2.899897,-0.334175,2.873919,-6.053896,2.440630,8.338747,-6.740513,-3.173979,-5.117331,-1.648259,2.688878,1.305285,-3.376449,-9.211177,-0.644640,3.338895,-8.892267,-3.294851,8.467175,7.601901,-1.923289,-7.606918,3.460493,-6.311892,-8.811894,-5.351606,3.564299,1.823453,3.129330,0.854939,-8.551107,-9.688016,-1.658875,0.496509,9.218611,-7.354325,7.372145,-6.260577,0.715549,-3.654175,-7.438824,6.356308,-2.276006,5.983036,-2.194483,9.338801,3.191878,-4.646258,-9.512265,6.729901,-6.362510,4.311467,-6.708934,-2.151327,-8.477044,8.475958,1.029866,-4.954034,-8.651133,7.479718,-8.737860,7.423571,3.323275,-8.296198,6.964045,0.802180,2.936276,-7.520900,7.380217,-6.314151,7.431370,-2.781453,-6.770513,8.635324,-1.721381,-7.999662,5.761967,-6.734396,6.734424,5.496578,1.818413,-3.309945,3.143952,-0.152717,1.180905,2.167270,9.234807,-4.240031,-2.845398,-9.942704,-5.385091,-5.635897,-2.695076,-4.968087,0.340239,0.040519,9.801453,7.793165,-7.668903,9.608064,-2.128497,-5.024313,-6.401969,-3.484596,-4.852477,5.048982,9.774866,8.705001,-1.906352,0.466293,0.101482,-5.399260,-8.050724,7.063050,-0.912130,-5.330758,7.190785,-1.732341,3.943059,4.781853,9.010120,6.088167,-3.905692,-0.707043,-4.663868,-2.537400,-4.637218,-3.139929,-0.019252,6.646002,-4.701493,-5.183640,6.167470,9.081901,6.919119,-4.296912,1.955641,6.159941,-8.204069,3.833674,1.656133,-3.576080,-0.946369,-5.731156,9.165648,4.374338,3.968622,3.324773,-7.611552,-3.321136,0.275019,-1.283211,-8.843090,-1.703003,-7.028312,4.049131,1.396981,0.467650,6.866835,7.179061,-3.789278,-2.108928,-8.083542,-6.538042,6.955020,-8.052740,9.070039,3.990272,-0.642671,4.530368,3.801570,-8.300072,-4.454603,5.957621,1.370108,-2.564711,5.311950,1.854535,3.223421,6.289027,-8.106517,4.944675,-1.328726,0.441732,3.868625,2.825525,-0.706282,6.816441,-2.737461,-1.518911,0.915239,6.977957,4.383061,-0.787760,-9.844199,0.931738,5.104215,-4.238468,-9.065364,-7.040283,-5.477957,-6.640405,9.320485,-7.786275,-2.915079,5.255345,1.416171,9.738687,-9.501280,5.771132,9.825538,1.117357],[-9.486587,-8.939900,-2.932251,-5.674472,6.344043,9.416925,-3.292513,-4.840242,-0.032967,5.891791,-7.186422,-4.753954,-4.817345,1.720802,6.543393,2.719328,-3.380509,-5.437943,-1.751922,-2.201944,7.572192,4.897995,5.055343,3.972372,8.172354,3.158580,3.980094,-9.370478,-9.840069,7.549389,3.577105,3.124115,-5.016863,-8.322498,-0.259606,-4.321106,-2.608163,4.124143,2.936079,5.499393,4.190268,-7.963170,-7.854698,7.047400,-0.611441,-0.214606,3.260607,-7.433578,1.317885,-1.483326,4.881942,-0.876118,-9.789104,5.852091,-3.229984,1.274712,2.758995,-3.879380,-5.623237,-3.454819,-1.237323,-5.534931,-6.698286,9.099779,0.144982,1.119881,0.909539,-0.681939,-7.735230,6.107019,-3.080849,-1.927953,8.669521,-6.278776,-0.219703,-0.856056,5.718532,-1.767303,4.091703,-0.545647,-4.461182,5.372543,1.874940,0.204009,1.792713,-6.534243,3.737457,-3.171359,7.387634,9.961864,2.929746,-7.219343,-8.577412,4.092107,-2.562102,2.962995,7.264665,-8.977935,-3.310588,-5.848381,1.802107,-5.318186,-0.494168,5.623800,6.342627,5.477461,-8.204712,5.206743,0.640700,9.134662,-0.017907,-7.069354,1.972297,-2.368944,-3.409933,-4.688656,0.449819,9.627827,6.485171,7.464854,5.674402,9.000352,-5.382170,-8.214752,6.519084,-1.636969,-5.803347,-1.105922,9.777599,-6.353050,5.112076,3.963478,6.531616,-8.987268,4.161319,4.219288,4.434908,6.379949,1.725325,1.790691,2.816161,3.485951,-7.275192,0.570046,-6.837844,2.812542,-9.513029,1.980739,4.629706,-7.155854,7.975050,1.485266,3.104215,7.843342,9.604910,8.342627,-9.119731,-1.016093,-6.218496,-0.914178,7.351224,7.113320,8.295931,1.342977,-0.310191,7.971096,2.448293,-9.146204,4.644419,-0.966917,-7.268657,9.549311,-2.844985,7.421091,-9.085719,1.119734,-8.442680,3.998255,2.221701,-5.006671,9.382949,-5.511587,4.350518,8.575973,-1.222080,4.358304,1.200446,3.830683,-0.555815,2.694919,-3.002995,3.013551,2.910104,-1.780168,4.166169,-4.414390,1.635794,-2.403259,-5.521908,4.696297,9.047024,2.745069,-7.584647,-6.896602,-6.207189,8.330406,-2.456002,4.469850,2.080787,1.250253,-7.191804,7.289162,-0.344558,-4.395718,7.605094,8.200345,-7.380980,-0.163470,6.894258,-9.554709,-4.484026,-7.184041,-6.671536,-3.472544,-0.063049,-6.857402,2.521751,-2.546141,7.979958,-3.298090,-6.586620,2.445365,8.500875,1.838730,-0.556490,-5.585460,3.581018,-2.360231,-0.759813,-6.332055,-5.543265,5.889800,-3.297740,2.101188,3.225255,4.673518,4.935242,-1.511587,-3.301227,8.236047,8.421511,8.098896,-2.733662,-6.540950,-9.945391,7.897257,-0.537719,-6.349216,-7.956599,-5.712277,-4.111659,-0.574065,1.393169,-4.978924,-8.055769,-9.828305,4.010127,8.605163,8.994340,-4.750238,-5.911169,-6.307398,-1.192751,4.955271,-9.097544,-5.198777,0.618745,-2.490337,-2.166173,-0.865691,-5.215063,-8.843944,-0.935351,-9.856580,-2.556139,9.675741,-7.977723,3.470483,9.784673,-5.720849,-1.268789,-4.125096,8.016109,-2.165396,8.413813,-2.448498,-5.774217,3.184424,-7.602515,-9.433295,-6.691464,3.459404,-3.145635,7.696869,-0.198665,4.282079,5.747469,-1.934663,8.629784,-9.051688,-9.295594,-8.313205,7.703871,2.050186,8.759040,-4.684379,-8.140393,1.173215,-5.317332,-9.556984,-9.481186,-4.790587,7.512674,-2.475629,9.187217,0.640113,1.733400,-4.255287,2.297425,7.270378,-3.498489,-8.357686,6.583381,1.651692,-2.170964,-4.165617,3.658321,-4.571191,-6.057145,9.618804,1.578687,6.493667,4.002064,-5.063750,2.815332,9.762226,1.686493,-4.199457,0.498016,5.244299,6.241342,-9.624486,-1.864650,9.556017,5.062626,-0.113585,3.063837,-6.245767,-1.275300,7.935196,-7.998147,4.111393,-1.603068,-9.135235,0.107799,-2.249933,-0.468731,5.289614,7.524961,9.087579,-6.073358,-2.544201,0.965890,-4.608942,4.057513,6.634705,-5.748267,7.318919,0.063350,7.646187,3.898748,4.841018,-1.224102,-5.826239,-0.187733,7.374367,-8.308045,-7.979855,-3.188220,6.302460,0.110341,3.073857,0.749743,-0.543420,-6.910505,2.693946,1.014524,3.824010,2.226391,-9.694000,0.368412,-1.657574,7.700246,3.823855,4.470002,3.000098,-3.011040,1.092900,6.350796,-4.373696,5.541769,-6.176081,-0.767055,-2.827592,4.570139,5.719486,-6.167094,-1.769193,0.460379,7.035141,-5.339051,3.487259,1.303368,-5.780564,-8.084850,1.298349,-6.627106,5.004407,4.812862,8.029168,-0.636618,-2.874372,-2.679991,-4.622958,-6.571320,0.392787,-0.125238,3.306423,7.530885,-0.579331,-0.612236,7.206090,5.248620,-0.256866,-4.598011,-9.058112,-7.970913,-0.638769,2.419787,-5.814344,-8.260493,2.209823,-7.624686,3.468087,-5.945383,-9.521250,9.790808,-8.211219,-9.188252,2.282704,-3.203245,3.850027,-0.746802,2.688590,-3.923159,-9.500675,6.995580,6.793881,-5.927022,8.326677,-0.063814,-6.913010,3.929431,1.914704,1.499486,9.374139,-4.813589,-2.829929,-3.210832,-8.598624,-7.217759,7.264026,-2.551175,9.199055,5.874909,-7.745587,-5.867267,9.823601,5.880288,4.681874,-8.194754,-8.000803,2.984120,0.271013,-0.510353,-3.426996,-9.856061,1.897242,-9.568641,-2.778010,9.900551,-4.669799,7.215756,-2.894840,-2.081653,3.463566,-3.355235,3.488405,-0.379577,1.804007,-2.274786,7.725519,0.987404,-3.028849,-1.818984,-6.040768,7.342616,3.630238,-0.573845,1.510913,-9.848574,8.752199,-7.848898,-4.792907,-1.146338,2.630993,-4.589327,7.389491,5.998300,7.158594,-9.299118,-5.463421,-3.247870,-3.722147,4.510305,0.393987,-1.575042,-9.506824,8.186854,-0.812350,-3.571482,8.709200,-2.118055,-5.674869,-0.244138,5.319444,4.903738,-4.980520,-6.627453,3.529627,-2.738428,8.386591,1.700606,2.470714,-5.252239,-2.076035,9.102082,4.067272,8.096279,-5.002480,-0.888411,-1.936278,6.322223,4.813283,-0.891233,9.773062,-3.990269,3.207838,-4.168998,-0.821603,-7.367791,4.205239,-9.258362,-6.792828,-1.954572,2.464890,-3.659930,1.057109,-7.727793,4.836691,5.359554,9.405217,5.516242,0.744265,1.125096,2.620003,9.164808,-7.527067,8.649914,4.683815,5.490787,-5.108063,-2.622459,8.148415,2.020785,0.589218,6.395120,-8.675251,-9.787906,-0.709940,9.589271,2.919981,-8.367655,6.769981,-9.495207,2.912275,7.491115,-6.541478,9.164868,9.758319,-0.831198,5.556728,0.748215,1.643059,-6.703329,-9.126655,8.944495,-6.262685,0.932960,6.067825,-5.447237,7.090563,5.157827,0.338552,5.825215,8.426232,-7.555878,5.793029,-9.928984,5.745871,-4.445221,-6.950920,6.463755,0.484663,-8.513697,9.014206,9.754391,6.602889,-1.543188,-7.174498,0.314616,9.083786,-7.016620,6.752412,1.531776,4.515123,-5.607311,1.377396,-1.700348,-5.299467,-3.905188,2.322936,-1.246460,-8.774668,-8.574257,-9.041616,-8.511197,5.406247,-3.054717,4.954658,7.746184,7.807887,-6.920557,8.035548,7.220179,-0.325958,0.539775,-2.192228,-8.845414,-4.090006,5.272244,-9.458344,8.582544,-6.081835,-2.720697,1.694944,4.620031,-6.180918,-0.966841,-7.081066,3.213290,5.027142,9.963024,8.231111,-7.634092,-1.518023,-4.410762,9.498673,-5.332357,-8.810091,3.348793,-7.000592,-9.935927,-3.535603,-0.928837,6.870499,8.591463,5.732137,-1.465035,-3.781865,-5.495843,-5.652652,6.604360,-0.484791,2.732880,3.031459,9.767837,0.808237,-3.201897,-6.877284,6.949273,-2.897171,-1.029442,0.987334,-3.270630,0.140987,-3.975737,-3.051130,7.421157,6.737260,2.645713,5.620698,-1.704785,-0.425256,-2.963557,7.021644,-2.293229,8.808029,5.804171,4.892441,-1.935274,7.405339,-1.311503,9.562964,-3.116945,3.784316,1.445849,-1.082025,5.566788,-6.217363,1.808665,9.712681,6.215298,-2.105369,8.298607,9.638199,-9.902790,-3.692574,-1.002839,-6.509866,-5.287556,-4.318712,-2.777664,9.028180,6.725420,-0.071084,-2.119551,5.819845,-1.209828,-4.052794,9.100280,7.362486,-7.662973,1.271350,4.877342,-6.519969,6.349578,7.472449,6.589455,5.236837,-4.085357,-0.332307,-6.831534,0.693295,2.701344,-2.665893,7.422018,5.127318,-6.815104,-2.849181,-3.588280,6.467756,9.134434,-4.687767,-6.797957,9.667620,7.472279,8.090699,2.101442,-3.134509,-6.428893,-8.372724,-1.814999,-7.474812,-1.835491,1.911401,6.435699,-1.089207,1.173462,2.622086,-3.999234,6.588120,-2.566003,0.604234,1.192072,7.421527,0.650481,8.136489,8.708912,-5.178928,-2.421613,-2.263304,-4.902231,-6.033145,2.892515,7.951406,-0.769616,5.912199,1.210362,3.247385,-3.261448,4.604297,-1.735363,-8.866257,-3.206082,0.278852,-0.521378,-8.332373,-7.965032,-5.466665,-6.511955,0.851305,-3.104302,-1.838307,-9.760782,-2.169952,-8.758852,-2.981859,-4.228876,-9.850530]], dtype = "float32")#candidate|3427|(3, 840)|const|float32
call_3426 = relay.TupleGetItem(func_2648_call(relay.reshape(const_3427.astype('float32'), [14, 12, 15])), 1)
call_3428 = relay.TupleGetItem(func_2650_call(relay.reshape(const_3427.astype('float32'), [14, 12, 15])), 1)
var_3429 = relay.var("var_3429", dtype = "float32", shape = (14, 8, 15))#candidate|3429|(14, 8, 15)|var|float32
bop_3430 = relay.right_shift(uop_3388.astype('int8'), var_3429.astype('int8')) # shape=(14, 8, 15)
bop_3433 = relay.right_shift(uop_3390.astype('int8'), var_3429.astype('int8')) # shape=(14, 8, 15)
var_3447 = relay.var("var_3447", dtype = "int8", shape = (14, 8, 15))#candidate|3447|(14, 8, 15)|var|int8
bop_3448 = relay.bitwise_xor(bop_3430.astype('uint16'), relay.reshape(var_3447.astype('uint16'), relay.shape_of(bop_3430))) # shape=(14, 8, 15)
bop_3451 = relay.bitwise_xor(bop_3433.astype('uint16'), relay.reshape(var_3447.astype('uint16'), relay.shape_of(bop_3433))) # shape=(14, 8, 15)
uop_3452 = relay.erf(var_3429.astype('float64')) # shape=(14, 8, 15)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
const_3461 = relay.const([6.956642,-9.805222,9.887786,-1.874008,-8.539483,2.869299,-7.529158,-3.740483,6.427504,-8.233658,-0.094298,-8.916039,-9.751901,6.971173,1.842969,-8.699274,1.829458,2.208905,-3.664956,4.236416,-4.214573,9.233611,-1.304998,-4.208106,3.677613,-8.523509,7.013424,-0.452446,5.393320,4.622423,-5.470724,0.006493,8.706182,9.858740,-2.080739,-7.101287,6.561942,5.520361,-8.989500,6.349729,6.593923,1.274404,-2.252376,-3.594894,7.849461,2.728912,0.242165,3.901659,6.658322,-7.929851,-6.438206,-8.905253,5.655643,5.483812,-9.434308,6.165954,-4.948937,-3.935614,-6.226994,4.515644,-5.702627,-4.839610,0.138428,-7.941818,-4.724509,1.951538,-3.583062,-7.262079,7.232200,7.690182,-5.994317,1.037729,4.791755,-6.830546,1.407984,4.962373,-9.017707,9.130054,-3.303540,-8.019441,6.533424,7.359846,-7.776395,5.560993,9.118419,2.899809,0.003577,-5.344428,-6.854703,9.768037,-5.917409,6.729338,-1.478582,9.800764,4.096961,8.442409,2.234449,-5.992512,-9.485586,2.199603,-4.804384,2.786742,-7.285002,-6.730849,-0.455259,-5.429541,-2.874015,5.684180,-8.665933,8.198962,3.824357,-2.487828,0.003125,-1.411378,-7.374697,4.431660,-5.982064,0.941863,0.401262,8.734124,1.301279,-9.766800,6.572529,-5.539217,-1.379059,7.900255,-9.364288,-2.161957,-7.194974,0.978384,6.907373,3.712603,0.526148,-3.344256,-4.639419,2.847962,0.340091,-2.299107,8.909292,-7.450052,-6.048036,5.961896,-0.097197,7.648526,-7.788243,7.788186,9.474005,9.866978,7.315557,7.388090,5.456596,4.625202,5.354969,-5.342262,-7.955213,-5.377279,-3.570599,7.072187,-8.906046,-8.204056,0.213919,-0.824449,-4.476813,-5.306129,4.306265,-6.833298,-3.174195,7.929225,7.411408,-8.343759,-5.163109,-9.434159,8.380413,1.452438,-9.083149,-3.751764,-7.645969,2.767784,3.901532,-1.868673,2.909423,1.204614,4.269132,7.673265,-6.859575,-9.318262,0.472504,-8.952309,0.779319,-7.862314,8.260199,4.800901,2.865282,-5.646479,-0.467138,8.471761,5.603651,6.688556,7.139647,5.108841,2.362933,-5.378400,9.386367,5.155436,6.494454,-4.048653,-7.058949,-2.998891,-0.646313,-6.425642,9.921493,4.837136,2.159214,6.754900,9.736604,-7.212861,9.581146,6.602693,3.724784,5.522730,-0.182827,5.324185,8.549315,-0.072111,0.033680,4.417216,-3.921624,1.978683,7.504149,-0.222474,-5.297115,8.706125,-6.625038,-0.373291,2.581769,-1.651258,8.899741,8.591946,2.965107,7.564883,-3.159888,5.675919,7.669602,-7.033049,-9.510122,8.436919,-1.382448,-2.663977,-0.134465,-0.174425,-7.789730,2.886244,7.468959,-7.467025,6.321561,4.829233,-4.154937,-7.697896,8.828320,7.547492,-9.971548,-3.782710,2.534440,0.081481,5.808021,-6.895283,-7.345906,-9.332528,-1.697405,-4.051717,-6.557873,9.275846,-0.755893,-1.394564,9.054859,4.336577,-4.903367,-5.700417,-3.034917,2.427636,8.420986,6.803709,-8.731173,8.361945,7.738480,-3.902099,8.238430,-0.306949,0.117854,-7.916001,-9.739422,-6.251109,3.333766,7.604112,-9.931953,-8.425558,-5.002275,0.212052,3.960650,2.791190,-3.527085,-5.952039,5.969934,-2.213274,3.704376,5.622293,-5.400512,-2.017835,-0.207660,-9.136708,4.396764,8.816321,-7.241711,-6.715130,3.032470,-3.938822,5.955618,-0.019038,-2.382927,4.285009,1.472429,3.407410,1.167492,9.903292,9.593812,-6.833955,-8.065256,-0.306310,6.189594,-8.837457,-4.335182,-2.299873,8.221401,6.744652,7.407495,9.712035,1.718138,8.850265,1.466741,3.954593,-7.861335,6.187778,4.645639,2.726524,-8.291525,1.519198,2.363094,-0.826638,-1.938944,-2.408489,-9.963939,-7.836627,-2.455769,-1.224425,1.591468,5.984171,-5.288484,-8.141461,-6.566410,-1.474659,-6.027857,-8.492789,2.439786,-1.826333,-9.997550,-3.229216,8.370461,-2.015111,-8.883581,1.504861,-7.682924,7.591567,4.971646,-5.622355,5.294323,-6.545234,4.203198,5.178213,9.821062,-9.210494,-5.552863,-2.093841,-1.242171,-5.313527,-5.372321,-7.755586,-9.913663,6.999296,6.558258,4.735823,-9.122125,-0.971814,-7.766477,-3.010960,-3.299860,1.207398,5.487485,-9.633371,9.944076,-1.867557,-8.686457,-8.579918,-4.963229,-4.594378,-2.212037,7.193717,7.272782,-5.734129,9.403452,3.754485,4.914592,5.280128,-6.063299,-4.167385,-7.636810,6.174282,5.347763,1.758009,4.279677,-9.001616,1.339195,-9.091172,9.150602,7.972196,-6.351613,-5.071365,7.749765,-9.749135,7.835732,8.296587,-9.023023,-9.359981,8.160338,1.988058,7.526577,-2.827907,1.431527,9.101028,8.323635,-9.543936,4.525701,6.373235,-2.226261,6.195739,5.306092,7.625614,9.517531,6.599628,6.019914,-7.108772,-1.841278,4.623403,3.557281,7.713393,3.890285,-9.221688,-3.836600,-5.511387,-3.529758,4.934956,-4.831075,6.406290,-4.029646,-3.005567,8.406754,5.489824,6.847425,-2.562217,4.540258,5.632583,9.070992,-7.587205,-3.588219,-1.398214,-1.914041,-7.095866,-5.342879,-5.890439,-0.111133,-4.100602,6.016286,-2.854098,-6.618965,-1.011562,-3.742977,5.029930,3.965747,8.116334,-4.379193,-2.711742,4.960186,0.200606,-5.673460,1.215051,5.317313,8.437602,7.767158,5.669400,-6.728558,3.799212,-1.137833,-6.714340,-2.030699,9.096117,5.511024,6.880750,-6.507176,-2.436189,1.863085,8.122133,0.612921,0.071114,-0.257218,-4.157268,-3.507876,1.052873,-1.724890,9.906775,-5.249585,4.865393,-0.513208,-1.385692,-5.516896,-5.919491,-7.413038,-0.348077,-1.693720,-6.196882,-9.324937,6.436773,1.131800,0.942322,-3.284194,-6.542727,3.921395,-4.080255,9.087941,-5.442429,1.681184,6.250989,1.553269,6.745340,4.521980,-6.761969,-3.719323,3.925132,7.492370,-7.315823,9.654871,-4.499368,-4.263730,-3.783371,4.143889,6.855788,0.233968,6.596735,-8.601430,-8.336921,-9.974279,-5.688509,-3.290251,-2.364178,-0.725546,5.767861,-7.161222,3.882926,-7.695982,-5.724239,-4.883871,-9.516182,-0.053501,-5.485095,-4.740071,-9.595354,-9.541267,-7.294399,-0.653612,-3.791686,6.191048,-4.787835,1.518594,-0.792702,-3.046459,5.768624,2.186928,-0.451136,7.960400,-4.326920,-8.284317,9.512062,1.241251,6.457217,-0.832584,6.256189,-7.704577,9.794556,3.051030,2.206926,-7.882228,-7.374364,6.389272,2.096929,-5.872202,-9.432243,5.897062,6.823540,2.118664,-9.937260,-5.680873,9.369996,-6.143889,-0.276049,1.071099,9.672360,-7.034299,8.631164,-7.534622,9.199891,-7.603951,3.799772,5.973279,9.920114,-3.686849,-6.283167,3.205614,5.960541,5.228973,3.526978,5.256431,-7.860706,-6.252382,1.922153,8.079947,9.306096,8.159961,8.918154,4.075301,9.350407,-5.678136,-4.314656,-3.658268,2.213179,2.609416,-7.875960,4.788745,0.366610,-9.201538,2.188926,6.266303,7.098799,1.034095,4.992241,2.456675,-3.841538,-8.631177,9.625561,-3.348628,-8.311084,8.906379,4.547731,-0.150592,7.933177,7.148500,-7.525185,8.539677,4.103423,-9.345090,-9.868957,-7.833075,7.035902,8.590292,3.652657,-9.922514,-2.096399,-8.366491,-2.600216,-5.323652,3.845358,-6.981269,-6.594379,0.266355,7.093579,-1.810326,-1.936702,-4.866898,6.648771,-8.035111,-5.402086,9.001316,5.860282,-6.000566,-6.994812,4.499460,-4.404986,1.397113,6.177715,3.506559,-1.279055,-8.635966,-2.936393,-3.679920,9.872291,-7.297605,9.991398,-2.341140,7.250098,3.403661,9.574659,8.264751,-0.283221,-8.158159,9.497402,-8.434515,1.178677,-5.706366,-5.342633,1.852539,-9.307185,8.460548,9.174577,-2.007308,-5.598797,-5.124013,-3.595199,8.908883,-9.413153,-6.938714,7.887487,7.344398,-6.531649,-0.164710,9.461230,-5.548345,1.990395,1.869573,6.717907,6.642328,9.151625,9.122814,1.987312,1.722294,-1.484326,-7.733386,-5.268627,-0.187614,8.248072,2.361964,-2.340987,-5.477543,9.111342,5.560177,3.965973,-5.171518,-8.330534,-9.742129,6.799073,-5.982403,-2.974104,0.329305,-1.938246,7.629122,3.970503,-5.239339,-2.286645,0.317731,9.611336,-4.527971,-8.449809,4.574081,-3.105245,-7.794838,5.133627,2.223300,9.506301,3.608314,-2.279981,-3.017100,7.117634,5.733015,9.169217,-5.583908,5.424986,-9.330813,7.118010,5.892523,7.630231,6.107969,-2.933369,-1.642883,-5.301588,8.395417,-4.704475,-5.819256,5.009830,0.935972,-4.599022,8.769680,-0.126945,3.238846,0.430653,8.779420,0.514000,-9.590812,4.128956,8.110539,-3.495521,-3.321048,-5.331957,-3.717056,7.434361,3.884764,2.612314,3.956809,-4.656939,-9.740079,9.995900,-0.382798,-7.811413,-9.297844,-4.458521,2.786533,7.746020,0.587933,-6.088266,6.302510,-8.430066,-0.495037,2.048470,3.490735,-7.841709,6.730962,-9.133771,-5.869854,-2.560147,-1.020836,7.745952,5.876827,-9.586456,-4.345908,8.432255,-6.606978,-7.976457,5.860201,-4.410080,8.583269,-2.395402,0.206629,9.049185,-3.642856,-3.628769,-5.484045,-7.989606,-7.438568,-5.004876,-9.183224,-8.471679,6.313865,4.401995,-3.207624,-3.224681,-2.124761,6.452768,4.251601,-6.147298,-6.058294,-9.522614,-6.405606,0.557303,1.980097,5.005204,6.056940,-5.545295,0.990227,0.508497,-9.394492,6.185028,0.499057,-6.800342,1.243348,-1.941761,3.703018,-2.369527,3.792757,5.951946,-4.141988,-0.055149,-6.456286,-7.496655,-2.022581,-9.115964,7.006034,-7.527668,-0.612431,9.587965,6.082516,0.757401,6.913827,-2.749006,5.466005,4.101253,-3.111934,9.492996,9.963383,-7.189699,-9.524470,-0.603668,6.475967,-4.174349,8.961803,3.817039,3.573756,1.595650,0.991364,3.863943,4.034356,-4.407998,6.001790,0.871332,5.737441,-4.690787,-0.733417,-9.417979,6.610227,4.293083,-1.133963,2.357055,0.991285,-3.967594,-3.372228,-2.934838,9.858972,-3.133970,-9.677382,9.602276,1.991891,7.352469,-5.032121,6.529406,-4.699999,-6.521959,-4.521453,-6.233928,-8.407420,-5.093948,1.108478,6.902588,2.242296,3.696096,4.879607,9.092530,-3.186555,-2.628050,-7.200708,0.028901,-4.940866,-4.232314,5.693892,-9.001935,0.057142,6.748687,7.382507,2.773805,-5.884024,7.978241,5.880360,-4.263413,9.872751,-8.355212,8.232114,5.708643,6.447662,-3.938362,-7.599623,1.830996,1.516103,-9.481077,0.541271,5.716699,-7.439857,7.348021,1.136282,-2.450028,-2.949740,6.138274,-3.456423,6.916395,-2.596843,-4.533188,-9.117978,-8.019217,-3.996435,0.341965,4.914563,7.299932,9.216487,0.514104,3.111043,6.531867,6.950950,1.423327,3.511319,3.185579,-9.621075,0.574442,1.551545,-5.315340,-6.971824,2.794987,-6.241854,-9.401940,9.237833,-7.055380,2.658212,-3.359704,-4.883774,-3.127699,-0.185670,9.824862,2.361545,-6.932184,6.377386,9.977816,-7.721839,4.555943,5.615749,-2.480103,9.154386,8.420637,-0.356385,0.830135,0.299376,9.749171,-7.218440,-3.449356,4.294184,-5.934561,5.075449,-5.733741,3.397410,-3.852337,8.037401,8.142569,-0.455206,9.988921,0.084655,9.392380,-4.522203,-0.836850,-0.553955,1.593815,2.204368,-4.010015,9.874954,-3.357339,-5.093946,4.067441,5.038056,-5.286226,-8.518974,0.507456,4.490900,-7.422204,2.064027,-8.284323,-0.346043,1.741799,8.307916,-3.586785,-6.181658,0.335564,-4.988164,2.840223,-7.346166,5.508033,4.828373,-2.371113,7.369097,8.937554,4.574443,-0.870036,5.647387,-4.568477,0.703658,5.041144,1.280381,-2.414866,0.152517,-9.819548,-5.868377,-4.454496,-9.535378,-7.340221,-4.613867,-1.312453,2.851579,3.272038,-5.832029,2.641410,-2.131783,5.895030,-4.011540,0.766678,9.365360,6.915781,4.949243,-0.206202,-4.011926,-9.735035,-9.552756,-4.380343,9.633242,-0.892311,9.703006,-2.385776,-5.541247,-1.144328,5.250212,-3.044855,1.091493,-4.066567,-1.305183,-3.670635,8.434372,4.822768,9.297837,2.190697,6.194219,-7.089775,-5.842898,-4.982067,-2.714209,5.142664,8.838717,6.434788,3.271982,6.838324,-3.838776,-5.761930,-0.090182,7.952683,8.532085,7.278029,-4.795811,-9.429435,-7.211453,6.202788,6.603578,-1.159924,-6.927618,4.005656,-8.101651,3.521493,-5.975638,-0.928698,3.128074,-1.629852,0.592472,1.288671,0.739296,-0.840036,2.889629,-7.871155,-4.384248,6.801286,-7.810459,-1.375620,0.829248,5.455041,5.145041,2.420229,2.478881,2.114109,9.550449,-4.247415,-4.383934,-9.217275,-2.167701,-2.992206,2.730504,-8.125222,-9.029735,-9.117828,-0.629119,8.595026,-4.913592,6.485695,-1.859397,-2.348034,8.181846,-4.065771,5.425908,8.578292,-9.147086,-6.308154,9.550531,7.748403,8.188860,-1.569760,-7.383445,9.164021,-4.543347,-3.852870,1.507913,-9.308926,-6.808230,5.624977,4.406270,8.921343,-4.054459,3.198116,-9.917508,-6.824881,9.346107,-5.757286,-2.136501,-9.776615,-2.610538,-5.248499,9.646623,-8.892293,3.054649,7.760184,1.565997,-7.794295,-7.447632,1.794114,1.681882,-6.456749,-6.376538,-3.249643,-9.276751,8.597079,5.476623,-6.930439,-3.452921,-4.931633,-4.827309,-0.228889,2.858978,-1.101329,8.269396,-0.433906,7.385803,7.306772,9.705772,-7.487900,-7.088126,-4.580718,3.754733,-1.782295,-1.777524,-4.532985,-6.907764,-3.800267,9.826963,3.506621,-8.973258,6.331417,-8.867810,-1.878863,-8.141941,4.757589,-1.165050,2.720080,-2.176855,-3.150129,-5.137039,-4.295213,9.289684,-9.401718,0.924109,0.007479,-5.944817,5.201005,4.496928,-0.442592,-2.012971,-0.082563,-0.059081,2.372416,5.920064,2.313850,-7.947621,-4.641794,-0.016692,-1.225582,-7.958172,7.289611,8.892071,1.473932,-8.262400,-8.571424,1.104387,-7.331341,-4.227696,4.263882,6.877840,-0.313744,-9.675419,7.411703,4.970156,-0.728022,-0.739479,-0.099006,-4.383805,-1.248699,-9.567520,0.519461,-5.071362,4.754069,1.427898,-7.397623,0.172666,-0.994095,-1.392477,-2.972449,-4.367402,5.233850,-0.520929,-9.862162,-8.774274,-4.574855,4.838036,-4.512935,9.012795,8.408408,-0.671630,4.323248,-2.074227,9.336970,0.838214,-5.392097,-7.833596,-7.616939,-5.876377,3.197238,-4.616898,0.766328,-7.469611,3.444134,4.685204,-4.279888,-2.530699,2.256004,-3.811091,3.208617,-8.332404,3.050084,-5.709148,8.546257,-1.825014,7.446453,-4.542851,-9.739152,-5.309524,-1.473485,-1.668711,-5.956515,-6.146098,0.402278,-8.551251,9.377944,5.189695,-4.161678,-7.481199,-9.786754,-2.642145,4.630535,-7.760642,0.717023,4.691778,-1.334425,6.906002,0.055179,-5.735816,-4.691294,7.599189,1.505846,-2.752781,-5.446531,6.855931,5.641282,-8.168291,3.964027,-4.429392,-7.131584,-6.826888,-6.916749,1.302399,-6.579375,-1.426468,-1.883105,-5.297571,-8.332747,6.019706,7.847076,4.600792,3.813830,-4.286239,-6.647264,9.448404,-6.764735,1.604831,1.496982,-3.331095,-8.524843,-2.818548,2.089274,-1.294543,5.055232,-0.310903,0.284117,0.971129,-1.885572,7.652474,3.673392,0.539592,-2.074184,-3.538842,9.972864,4.271427,3.688977,-2.781836,-2.961211,9.418455,5.729133,2.170329,7.190394,4.200110,-6.893189,0.395883,8.501881,6.698843,7.536542,-7.367994,0.883196,2.842844,3.797235,3.515802,-2.852250,-3.705006,-0.441208,-2.931837,-7.683227,5.767026,-3.946672,-5.870770,0.988362,-1.552688,3.220674,8.169276,-6.037786,-7.871196,1.379844,-4.984231,-0.565155,0.448586,-0.254148,-2.629558,3.275783,1.382743,-9.023604,5.725935,3.094128,9.617743,-3.996796,4.322432,5.222378,3.082496,5.735878,-0.353038,-0.959504,2.400448,-1.039209,5.801952,7.814998,2.373336,5.783022,-1.485508,-3.760523,5.383838,-0.692299,-5.188086,-2.505399,-8.218555,9.579072,5.019518,-4.554944,-0.617077,8.275507,-1.315283,-3.401695,-5.974170,4.713536,-0.024878,-3.595782,-5.118639,2.320430,-2.414373,-1.186302,5.516627,-6.785780,7.541957,1.572742,7.184102,-0.571392,-7.807614,4.514697,-5.892016,0.232483,7.508729,-6.238491,-2.629204,-2.562255,-4.748708,-4.979427,-2.192601,-5.825037,5.734609,0.484915,-0.733063,3.844112,-4.530229,-0.935963,5.279013,8.546606,8.368682,-1.737259,1.899490,0.181797,-4.155921,-3.531180,-7.742136,-0.278776,-1.913070,-2.690029,6.347713,2.741191,-8.079053,-6.984184,4.649549,-6.461087,-1.420592,1.547712,5.288578,8.811205,-2.705742,-1.520321,-2.815351,-0.352351,-5.004737,-8.989076,-5.436494,0.987692,9.929041,-5.214601,-8.004093,4.065708,-4.255838,-2.906308,1.322535,3.989985,0.243524,-8.136798,-7.229086,4.019463,6.058151,8.224688,0.780959,6.896551,-5.763386,-3.021768,-3.812054,0.068016,-3.075677,0.043971,8.890346,7.965741,-0.823671,7.425556,-9.229124,-1.040089,-3.721303,-1.262175,-1.223999,-6.471178,5.767990,5.065774,-6.045645,-2.522243,4.569758,4.779576,-0.209572,8.474325,-4.937976,-3.622908,0.582758,2.918503,-9.625444,-6.523725,9.430195,2.026604,5.831831,-0.159885,-2.429179,-7.953602,-7.411929,-5.264637,-2.034390,-1.107919,-1.157567,8.896372,8.820046,5.960077,-2.294573,-2.039655,-6.937193,2.715128,0.619447,-3.809336,-0.997857,2.361564,-3.788176,-1.319664,2.024035,7.097101,9.398797,-8.329116,3.438996,-9.058678,6.851092,7.464316,-0.672837,0.018091,9.276937,0.082178,-0.893214,-1.218229,1.747843,7.399693,9.701745,-3.283911,6.284966,0.889693,7.590699,1.596449,9.525412,-9.023225,3.755804,7.698840,4.082992,-3.781806,4.527023,-9.294115,7.155824,7.374731,0.869321,8.992423,-5.755880,7.781818,-9.739089,-0.258471,-1.184965,-7.154737,-4.180792,-5.539288,-0.734753,8.870710,5.543065,-9.059286,7.349688,-3.170609,-3.313176,-8.906295,-7.938817,-0.741986,-4.556059,-6.175551,2.241693,-7.902839,-4.913640,-0.328644,3.027951,-0.302563,3.986503,-0.137291,6.823064,4.095545,-1.575962,-2.203305,-4.439808,-8.426244,-7.223146,0.127122,7.306817,5.034037,-9.415187,-6.980783,-6.816621,-6.697549,-0.626343,-2.057847,2.782617,0.722190,2.982772,9.122566,-7.724051,-7.554564,-5.877288,-1.674076,8.678110,-9.753381,2.318882,-1.202053,8.244570,-2.057107,0.061067,4.584981,-3.443458,-6.496892,2.130981,6.828271,4.033154,-3.695397,9.019997,5.860662,-7.789207,-0.089723,4.414728,3.517787,-3.722093,-8.744877,1.283503,-4.921924,-6.254654,3.398948,-1.688504,5.546030,2.734805,-6.460614,-7.457876,2.398271,3.547308,8.116599,-2.497338,2.681514,-8.170276,-5.186830,-9.058727,8.309218,-5.255416,-4.781821,-6.671399,-6.210282,5.141426,-9.693708,4.234343,-6.753589,-9.207614,3.626529,7.056484,0.192088,-7.523805,6.809672,-8.731229,5.916476,1.691475,-8.853655,1.267788,8.856823,9.124941,-0.508000,-0.415968,3.346428,-8.965728,3.986759,9.470937,5.349812,0.396666,-4.142795,-7.296869,-6.526309,9.233740,7.600728,3.393772,9.881557,-1.524722,4.836291,0.394120,0.334345,3.166685,1.287680,5.436072,-9.800890,7.699070,6.822660,-5.759063,3.119758,-1.924818,-9.811266,-3.864460,-4.876768,-1.605462,2.620976,-4.443054,0.082351,6.006064,-3.603665,-7.196368,7.031274,-7.167274,2.557414,-9.105019,-3.601100,9.446199,2.012514,0.342919,-2.304475,2.694135,3.967102,2.957337,-3.192139,6.463967,4.089703,8.251992,3.469085,7.886457,0.692435,9.844141,-1.689461,-1.394223,-1.159200,0.318841,2.699373,-7.697380,-0.348569,-1.344272,4.754504,-3.067653,0.066438,5.109988,5.331324,1.816644,2.788836,-5.855709,4.045078,9.660004,-2.120067,-7.949717,6.877866,-6.153570,-1.564666,-2.943598,-9.691215,2.627715,1.358738,-8.712951,6.070194,2.649734,4.333119,2.294660,-8.481137,-5.824267,3.554096,1.191091,-7.494277,2.206728,-6.809006,-0.566575,-0.288378,-0.142866,-7.484407,-7.048211,-6.419007,-2.225740,5.059894,-6.610120,-2.119019,5.679418,1.788456,9.832515,-1.753277,8.832083,-8.315035,-8.038301,8.407137,-9.020405,3.627480,1.731699,-6.940451,4.084447,6.895250,-0.408151,9.911262,-2.655660,-0.482724,-4.419644,-4.752155,3.794503,7.529371,5.069654,-2.979502,-6.318274,-7.863182,8.593702,-1.488054,-7.026924,-6.199467,3.036633,-3.640747,-7.579739,1.028539,-4.297003,-5.910493,0.727561,5.029241,-6.105114,-5.697923,3.693567,7.712355,-8.515315,-7.617075,9.890564,1.050235,-9.460572,-5.706644,-8.683879,6.122071,4.555292,-5.787753,3.579895,5.824907,3.265677,-6.701198,-5.187707,6.645358,9.493060,-8.864243,-2.242775,-2.867726,1.218780,8.409111,-3.078208,-0.021110,9.472273,-1.409642,-1.721996,-1.711176,-5.204673,9.435029,-3.322932,3.955564,-7.203912,2.136487,4.510722,1.914903,-6.815997,-5.006961,5.122919,7.669302,0.514961,7.753783,9.546777,0.614779,-3.358018,1.628040,8.835790,6.230524,-2.485397,-3.157902,-8.324671,-4.874221,-4.765216,9.153696,-3.755257,-3.202006,7.327328,6.178932,-8.994144,-6.421000,1.819610,9.875254,-5.391468,-3.076252,8.653306,-1.242942,-2.375935,0.045280,5.494076,-5.199768,7.911385,0.136485,-5.892687,4.125013,7.093098,-4.202542,9.232308,8.449362,-2.620737,-3.651408,-8.317045,6.474187,-4.206993,0.421362,7.536784,8.937034,2.186000,1.783258,0.419217,-6.697017,-8.516294,-4.452054,-3.256199,2.691957,4.904184,8.589802,-1.078575,8.850903,5.956935,-6.567176,-8.736775,9.298224,-7.142029,-9.194948,0.209094,-0.131146,7.247723,-3.162234,-8.621729,-7.391148,0.644866,7.571565,-5.639126,-1.312734,-6.704187,-7.968338,-7.027579,-4.211147,3.945342,9.911694,8.721598,-3.796725,-5.407978,-6.970978,7.474346,-6.793394,-0.171555,-6.589013,-9.595270,-3.189026,-5.211714,-7.273683,-2.130105,6.090777,2.066180,5.788907,4.920809,0.578051,-9.058798,-4.356169,-1.696750,-1.321840,8.000380,5.585283,-1.272513,-7.703359,-5.919433,6.429312,4.006661,-2.749607,1.657750,5.869633,-2.526851,-8.743744,-2.411125,-2.402305,-1.286656,-1.659162,3.421166,8.986250,3.112538,-6.194168,-8.590210,1.576644,6.350645,-1.712013,5.122124,8.182907,-6.136465,-1.951667,-2.181535,9.983385,4.260068,-9.095735,5.942995,-4.478507,0.705456,1.764438,9.781341,8.851558,-2.298143,4.066796,2.421283,3.936615,9.576601,2.269841,-0.668062,-1.921490,-4.681987,9.817856,-0.987991,-7.460113,-2.306290,-6.180229,-1.949732,-8.270238,1.012802,-1.597840,-4.528037,7.988019,1.129628,-3.611516,1.448916,-9.190926,8.820734,-8.497580,2.764009,-9.633487,-6.112969,6.930487,-8.886812,4.577734,-6.565235,7.312255,-7.144101,-5.714608,7.422506,2.811492,9.784022,-7.196265,0.306224,-7.373140,8.038525,2.662283,4.681941,8.203785,-9.189986,-0.408695,-2.222772,-8.014406,-6.092248,0.889079,5.274191,-3.294325,-4.331218,7.262237,5.360148,-8.164222,-4.530396,-5.932135,0.854990,-1.759286,7.225559,-4.476680,-8.195044,-0.472469,7.325219,-5.233149,-9.840985,4.243010,4.652522,9.197388,-9.311774,1.366460,7.445242,2.292569,1.750327,-5.661984,-0.876711,8.570901,8.451663,6.634802,3.832447,9.293567,-4.366336,-3.524591,-6.207090,7.939139,5.229487,3.708957,-3.719121,6.270150,-1.986794,-5.891009,-9.243537,0.378653,4.198142,-5.187446,-0.815282,8.298116,-3.726012,-4.983344,8.673731,-6.938766,4.412562,2.819921,-5.223669,5.926661,-1.013501,5.900072,8.359730,8.981108,1.598031,7.618130,4.305440,-4.416293,-6.081817,-0.926980,-0.144187,1.571625,7.503169,-9.134394,2.409670,-0.993251,3.090109,4.088334,0.714733,-6.392659,-6.300545,-5.466046,-4.724056,-8.204848,-0.856555,-3.189106,5.102649,-5.027104,-4.589847,-5.043201,-1.408629,1.531097,-1.271660,6.236433,7.053702,-6.410244,6.317224,-1.795414,5.514090,9.935207,6.466855,8.042567,0.746515,7.997794,-0.025870,5.538253,7.367552,-1.152568,6.329679,8.212741,9.361931,5.068897,-1.606256,-6.270912,-1.839227,3.819750,6.540319,-0.426949,-5.529586,-2.017437,9.202838,-0.876570,2.386833,-3.574206,-1.211256,8.804980,4.299005,-0.705240,-7.973337,3.596373,-8.992652,4.587346,8.781463,-2.057159,2.862427,-6.219806,0.600349,8.792657,-8.165597,8.100430,6.220944,-9.613449,1.795020,5.057106,-9.812776,-9.822023,1.492627,-2.366650,3.032717,0.855579,-8.472771,7.160257,-0.698849,-3.639575,-0.545828,8.903276,-6.154768,-6.905541,-7.763249,-3.984552,1.362102,-8.353174,-7.013733,5.556487,6.729045,-0.119764,3.491590,4.244737,0.796983,-5.935450,-4.136808,3.578753,9.851023,-5.055223,6.529659,-3.462545,-6.543957,-5.058745,-3.162254,-6.197036,-6.427930,3.249643,5.254469,4.589151,-9.262541,-6.689313,1.403451,2.081637,-6.887785,-6.904370,-2.550957,-0.989923,2.174287,2.961163,-9.085085,-1.756187,6.636325,-9.397807,-5.493546,1.984096,3.906600,7.092098,9.915624,-7.629002,9.147973,-7.942176,1.033733,-4.914323,0.244737,-2.923523,3.456457,-5.676538,-7.437443,2.798769,-6.211281,3.190789,3.737378,-1.198767,-1.812997,-3.086103,8.889079,6.471521,2.210902,-8.839783,-6.771862,-4.018719,5.993916,-7.001623,-7.828992,-0.873749,-2.855090,-1.379683,9.228505,-1.502564,0.868996,6.063383,7.094512,-0.817069,-7.442087,0.927704,2.105048,-4.016709,-9.346355,7.789062,7.637045,2.968274,0.442591,8.296464,-8.113383,-7.061504,-1.420783,7.982512,0.479370,-3.973184,-1.573230,-1.437537,9.386051,-6.427960,5.029791,-7.752375,2.905329,-0.561857,-2.562152,8.818614,7.192324,-1.094526,1.998674,-2.303093,8.053157,-9.956922,-9.912938,-3.449531,-7.168194,-8.546448,-4.080536,-6.669530,-4.814124,-5.527717,-1.687390,-4.697068,-5.081224,4.249981,-4.357997,-7.900245,-1.030554,5.155906,3.798857,-0.629930,-2.532603,0.909475,-0.951132,-0.884728,-8.101767,1.649800,1.995187,-3.888209,-7.194421,8.651790,3.747970,9.960327,5.307867,5.430300,-6.706204,-6.474893,-9.948342,6.788369,8.372159,9.635926,-0.473222,-4.619245,-9.495649,7.820804,-1.961769,1.843555,-3.842103,6.968481,8.917975,-1.889350,-9.461999,-0.042967,-7.083391,5.790688,-8.887435,8.822498,7.288944,-1.171338,4.488570,4.740856,-1.640317,0.361462,2.126831,-4.391133,9.114555,-8.186017,8.806555,-8.880938,-5.502946,0.917538,8.550950,6.984792,-5.255387,-5.650626,-8.621405,7.891397,0.528340,1.487314,0.807645,7.903077,3.504798,7.248827,3.147048,-7.308138,6.411340,-7.169533,3.196181,-4.538490,7.602499,1.137080,-1.438018,-5.342865,3.847485,-0.025369,-9.517868,-8.020866,3.654127,-3.496091,7.043229,-0.369856,6.300551,1.788729,-0.528641,-9.743039,7.625446,9.063214,4.252848,9.322415,-7.498003,8.223163,5.411060,-0.967822,0.573141,1.299496,0.428452,-5.608709,-6.156570,3.561475,3.035384,-7.655481,4.486760,-5.976652,-9.296302,-4.096627,6.490670,2.663390,4.083817,1.868455,-5.410624,5.868405,-5.892565,-9.344918,-8.121684,5.895850,-7.493056,-2.385225,-3.274210,-4.374371,-7.774404,5.358521,-3.103599,-5.799979,-0.452318,0.160564,1.255464,-9.586559,-9.611128,-0.691442,2.721331,-4.830894,-2.164827,6.769545,8.918355,3.749551,-4.632525,1.140591,9.999034,-9.766941,7.915265,-3.387378,9.381356,-3.672921,-3.666666,-3.395521,-9.035694,5.197488,1.719052,6.703854,-4.033230,-0.722643,5.983673,2.122452,0.347801,-1.761921,9.666370,3.561207,-5.229031,-0.649626,9.632228,-8.793936,6.183854,-7.560682,-9.662148,8.900492,-5.372591,-9.116262,6.710710,-6.580476,1.442118,6.543375,4.338358,9.934597,-6.870930,-9.254408,-3.635148,-2.297909,-8.591302,-8.820047,-6.525293,5.622970,1.957907,9.182616,-2.203082,-0.316214,-8.058304,-6.152969,-8.888197,2.102127,-0.590724,-4.401946,-2.169327,-1.756323,5.883402,-2.895475,1.814837,-6.267926,8.113985,4.276425,8.124237,8.014012,-1.130981,-0.148526,-2.482442,8.879317,0.374647,9.007010,-2.088882,5.090293,9.083100,-4.176557,1.168948,2.769134,-5.992032,-3.613346,-2.428252,9.864559,-8.208484,-7.020827,-9.025649,6.033046,2.711501,5.636500,-2.580681,-0.288969,-2.252763,-8.869490,3.017750,-2.431809,4.567653,-8.433443,6.813114,-7.704182,7.196976,-6.442294,-4.044720,2.770840,-8.348984,-4.289169,3.907235,-4.680155,4.339013,-8.609948,6.651480,-7.939444,3.715290,-9.652899,-1.209205,-1.679854,7.088168,3.049492,-7.239847,-1.056599,-3.065149,-6.001414,8.668158,6.394955,6.917598,0.752162,3.284307,4.139372,-8.752027,8.422814,-0.937439,-5.100476,-1.203531,-3.944710,8.374115,7.402732,3.798621,9.794361,6.583646,7.318570,-3.207998,2.559208,-4.772347,3.954873,-6.368741,8.908883,-3.323586,3.265942,-1.646780,-3.005673,-4.550968,2.636915,4.490178,-4.345764,0.277086,8.162857,-2.739620,5.670339,-0.760206,-6.641229,8.040222,1.508684,4.437500,-9.386198,-7.021098,8.175312,0.355210,-2.068116,-9.006626,6.335947,-4.835755,5.642459,8.219203,8.287559,2.430423,-8.404682,-7.771023,5.892468,-7.983572,6.549900,-6.870209,0.096587,1.826669,-0.468293,-5.137325,5.112144,-3.072733,-8.843798,-6.628073,4.969202,2.603250,-4.637916,-1.624928,6.782322,-0.540489,6.340184,-4.374584,-1.773596,2.587489,0.978746,-7.631616,-7.332862,9.415963,-7.413349,7.230077,-3.629027,2.044955,-4.217653,-8.566559,3.721112,-3.439524,4.391770,8.751181,-8.603348,-6.998000,1.046402,-7.753521,3.935460,-5.869259,4.806228,-2.907491,-2.440900,4.733180,0.088198,-8.108773,-4.810695,1.736379,0.401060,0.429837,7.423065,3.292771,-4.997897,8.481389,-7.992170,0.576434,4.401054,1.863940,4.422276,-9.673501,-6.691765,9.692941,0.024420,-1.114547,-8.504066,-0.636357,3.795310,-4.143535,0.831276,1.711569,5.234662,-8.678070,-2.668255,-0.268052,-6.285661,-8.039828,4.614970,7.231086,0.244767,-1.759220,8.700436,8.033124,-5.914167,-4.824167,2.163598,9.711026,-0.317483,9.537582,3.763279,-6.170624,-3.377325,-6.270322,3.393115,-2.815767,1.205856,-0.151213,4.916525,0.073975,0.768737,-3.226122,-6.674127,6.709170,0.893569,5.574502,-6.342957,-1.721947,1.777218,-5.630687,-2.591065,3.860697,0.759583,-8.557359,6.368979,9.735659,4.892943,-2.580514,8.086201,-0.509061,-9.873454,-0.426118,8.798487,-0.053384,9.367170,0.791448,3.502804,-8.780593,-7.200848,-7.504092,-2.916957,-5.609412,8.882530,1.199895,-1.700352,1.056761,-8.298530,7.684312,-8.790996,-8.475843,3.885838,0.445972,-9.871314,4.251814,-3.086675,-1.952303,8.566663,-7.403490,2.194880,-3.309190,5.939641,7.604428,6.050165,6.917317,-7.984357,6.737840,-6.664214,-3.960499,-3.280894,5.244367,5.206898,-9.487718,6.664139,6.822291,-0.046599,-0.701539,9.179369,8.960164,7.754615,-5.977000,-9.096017,3.756511,-5.854287,6.012142,9.503392,0.917736,9.513181,-0.398103,-0.057596,0.458620,5.764755,-6.145689,8.091519,5.923288,0.568749,-1.084062,1.598826,-9.969391,-1.127028,8.443885,-2.229862,-8.322613,-5.421989,-8.465481,7.904726,6.166318,-7.436421,3.434137,-5.968794,-5.053306,3.736273,4.654946,-0.261313,-8.018212,-4.501614,-7.408005,2.524302,-0.447574,7.375824,-3.176701,-3.685495,3.630705,-0.967233,1.860095,9.691541,-5.642863,-7.779536,-3.783383,0.333884,9.538948,-0.620531,-6.934739,7.601386,2.724165,-7.646665,2.030780,8.531213,1.164112,1.859913,-3.571155,-7.858643,5.236607,7.452480,7.785540,3.233126,-4.812515,-4.888065,2.288235,3.475031,0.037858,-3.321695,-0.073095,0.032061,2.066267,-1.437531,-4.073857,-2.887687,-1.542846,2.110510,-2.513150,-8.816687,-8.896534,-0.504300,-3.524342,-3.854095,5.084512,-0.761468,-8.159473,4.428678,9.577846,-4.668585,-3.657627,2.860643,-2.354932,-1.525488,5.033470,6.413768,1.109864,2.429712,2.926745,7.735160,1.146012,-8.626938,-8.863139,9.373628,-2.995469,1.139288,8.739185,5.196906,9.603508,-6.248349,-0.573376,-1.647547,9.830604,-1.481448,9.004967,4.060279,8.604776,-6.191635,3.137967,3.166823,5.896202,-7.327540,-5.125593,-2.835753,5.412804,-5.055553,-7.718955,-6.236239,7.237704,-2.752914,-8.856514,9.475513,-3.027570,4.912431,5.793207,9.092140,4.062685,5.812993,5.418451,8.794078,9.203243,-1.711234,-3.585713,7.447046,6.288249,-4.707981,-2.537620,-6.930299,-0.063305,-9.347789,-8.134110,-0.162737,-7.824218,5.175291,-8.862906,-8.702399,8.808255,7.397501,9.328300,1.505905,1.578325,2.740125,6.384502,-6.955003,3.243790,4.804155,-1.810768,-3.384184,-5.634282,-2.018960,-3.933988,-3.206995,8.060712,-0.637347,-3.725276,-4.566100,4.667980,1.592676,0.484574,-5.057640,0.658181,-2.792411,-7.738782,-4.716551,9.490888,3.785883,6.469990,0.845391,5.771262,-4.288221,1.151824,5.092557,-9.749510,2.596379,-1.927760,-0.101242,1.372360,4.831400,5.572778,-8.005222,-8.194336,8.367206,6.030409,7.486291,-2.624226,9.118563,-5.387946,-5.415784,9.245074,-2.375777,-8.324881,0.050610,8.365381,0.134262,-4.851919,0.031391,2.400711,3.332021,1.184519,4.128324,-0.252249,5.607795,-0.270429,1.651871,8.612993,4.333119,-2.362012,-1.965506,-4.245283,1.790895,5.404151,7.521043,6.040652,-7.383184,7.090081,-5.709482,-2.275496,-1.441526,7.926175,-2.088635,0.042203,-5.017631,2.927299,-7.932776,-6.613229,-8.517799,-8.970114,-2.553539,-9.835099,6.607925,7.563634,2.445320,3.453089,-1.101145,8.812012,-1.579291,-2.822677,2.242085,0.192149,8.595895,5.674917,4.346916,-9.466792,9.078436,-5.353501,-3.249052,-4.124367,9.880206,-0.703868,-1.492422,2.021070,-1.708926,-2.328306,1.815690,3.559423,3.375637,-6.954928,9.114874,2.623750,-9.981656,8.164989,0.390453,-5.627381,4.222170,-0.861863,0.988243,-7.074056,5.164641,3.932618,-2.745643,-4.919221,8.696361,8.438932,5.083999,8.732816,-3.367840,-5.823720,-0.543225,6.436753,8.556082,8.796285,5.755234,9.447730,-5.061983,9.152535,7.931206,0.005202,-5.798686,7.128459,8.906009,4.788249,9.618972,7.489136,2.376404,-8.000205,-2.311812,8.826984,3.608280,-5.081031,8.271320,4.867267,9.677472,1.215029,3.107626,2.181165,1.076182,-2.741702,3.492889,-8.079070,-8.955851,5.709198,-8.519274,-4.628723,3.745753,-1.211323,-3.466052,-1.507906,-0.809793,-0.870849,-4.794228,-5.861238,-5.820216,5.981344,-4.902343,-8.025868,-6.330330,2.634275,-0.219502,-4.245000,-5.604659,-1.643314,-2.680131,6.129071,-7.876034,-5.569310,5.266351,-9.564878,-2.042658,2.085597,4.076081,4.940445,-5.229340,3.422948,0.010946,-1.803381,-1.785984,-8.980505,1.770803,3.878496,9.942686,2.495019,-9.939364,5.314050,8.453620,1.821476,-2.132213,-5.267889,9.274228,-0.147128,8.182265,-1.906030,6.574531,2.346425,-1.754579,3.442401,-3.029924,2.642176,-3.078199,6.074915,2.403049,9.365839,-1.864057,-6.372003,5.981026,-4.240184,-9.745863,-9.607353,2.046578,-1.718223,-7.370700,-9.203923,-2.493019,8.564246,-4.125422,-9.266133,8.714280,5.185881,3.218189,9.636157,-3.648160,-8.265228,-1.302572,0.656058,-7.239398,-4.907143,1.194936,8.862042,-9.910774,-5.932125,-7.279311,-8.091378,-2.275332,0.430753,-1.197088,-2.157307,-8.639292,9.512733,1.146803,-2.737176,-0.421472,-3.467212,0.917829,-1.947579,-8.327942,-1.542101,8.362894,-1.662330,5.128012,-2.966854,-0.882019,-0.929836,7.469019,-2.773123,-5.303935], dtype = "float64")#candidate|3461|(3360,)|const|float64
call_3460 = relay.TupleGetItem(func_674_call(relay.reshape(const_3461.astype('float64'), [14, 16, 15])), 0)
call_3462 = relay.TupleGetItem(func_676_call(relay.reshape(const_3461.astype('float64'), [14, 16, 15])), 0)
output = relay.Tuple([call_3400,call_3413,call_3426,const_3427,bop_3448,uop_3452,call_3460,const_3461,])
output2 = relay.Tuple([call_3401,call_3414,call_3428,const_3427,bop_3451,uop_3452,call_3462,const_3461,])
func_3480 = relay.Function([var_3429,var_3447,], output)
mod['func_3480'] = func_3480
mod = relay.transform.InferType()(mod)
var_3481 = relay.var("var_3481", dtype = "float32", shape = (14, 8, 15))#candidate|3481|(14, 8, 15)|var|float32
var_3482 = relay.var("var_3482", dtype = "int8", shape = (14, 8, 15))#candidate|3482|(14, 8, 15)|var|int8
output = func_3480(var_3481,var_3482,)
func_3483 = relay.Function([var_3481,var_3482,], output)
mutated_mod['func_3483'] = func_3483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mod.get_global_var('func_1743')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_3487 = relay.TupleGetItem(func_1743_call(), 0)
call_3488 = relay.TupleGetItem(func_1744_call(), 0)
const_3502 = relay.const([[[9.568946,-2.472380,-1.777421,-1.405245,7.621940,0.431613,-3.233872,-4.432702,-1.378498,-8.141950,1.901523,6.038959,7.942994,2.362489,-2.447820],[-5.020884,3.448982,-8.934420,-1.322577,7.969091,2.405784,7.487092,-1.993489,2.047439,0.779970,6.075910,-6.007640,9.720750,-7.935701,4.022412],[-0.943980,7.447296,-0.473929,8.958327,-1.765471,-6.241122,3.478212,-2.333625,8.077634,-0.500932,7.733491,-8.157814,-4.198373,4.466214,-0.017930],[-9.169724,-4.007645,-2.633761,3.734810,8.637621,-9.055547,7.424802,-9.413001,5.522932,6.221025,-8.805827,8.745767,-5.036590,-1.622024,6.762364],[-9.367635,7.979788,1.065581,4.901698,9.532829,-2.852130,-0.816731,-0.352249,1.254424,1.991239,7.627448,7.929564,-5.234185,2.901596,-2.071319],[1.596750,-0.394269,5.244339,-8.403534,-2.610298,-0.345588,-3.252529,-5.865800,0.687935,-5.596983,-0.693019,-4.718869,8.720769,6.577388,7.020318],[7.189247,1.117906,-2.339786,1.768791,4.695162,-6.092851,-5.927069,7.698474,4.554268,5.559547,7.617447,-7.712778,4.376683,-3.650610,-8.416581],[-0.879510,-3.920575,1.616627,7.981641,9.006350,-5.588335,-4.162126,-9.204872,2.697999,-1.855908,-4.979886,-0.142961,9.581666,-1.223240,-5.805647],[2.804789,-9.055231,-1.276618,-5.415999,-2.464390,8.724496,-2.095310,3.161982,0.744061,-7.913154,1.401829,5.707970,8.116279,-4.921125,-0.166948],[-4.537560,0.346704,7.618474,-8.508174,8.762662,5.810095,0.364063,-8.969142,8.379728,6.213723,7.927860,-0.236756,-3.574869,7.391499,7.708914],[-7.866268,-1.030240,-3.126394,3.222911,3.708976,2.343031,2.209183,-7.973971,6.154029,3.341758,-3.366785,-8.321539,2.434567,-3.593479,9.667524]],[[-2.949839,-9.994512,5.832287,-5.863776,9.028911,-7.639786,3.019558,-7.381182,1.462583,8.312761,-3.922500,-8.669997,-1.369619,-0.749591,-4.457565],[-1.212291,6.720663,3.205962,7.108634,9.289143,-1.122022,9.103968,-5.472237,4.134960,0.470160,-4.012703,-1.694824,-8.633707,3.165236,-1.839217],[-9.137215,-8.350027,0.945690,0.144960,-1.963732,6.396575,-3.753456,-1.708866,-6.187529,-3.536310,-3.605049,-0.873946,5.325371,0.306986,5.186434],[5.598569,-4.184332,4.552285,6.192426,-0.088815,1.713004,-5.850662,-4.852277,-1.142617,0.675296,-9.090574,-8.651880,-3.497570,-1.291070,-4.886917],[6.561003,6.830943,3.547328,8.950827,9.539760,-9.748728,-8.885187,-2.973189,0.544747,5.929559,-8.860488,-5.680811,-5.808787,-1.990737,-9.721955],[-2.606216,-4.879461,7.235942,-1.599462,9.272019,-9.096457,7.865888,-2.614719,0.491417,-6.679875,-6.634440,6.325905,7.078796,-7.851755,-5.326636],[-0.696367,-5.591761,-1.786265,1.912167,5.436317,4.601966,-2.789863,-3.088165,-5.623254,0.605855,-6.407737,1.963152,-4.435011,-7.282043,8.894944],[-6.796183,4.403099,-2.721868,-3.973274,3.373783,-1.238982,-9.226190,2.661276,-5.968167,-0.970224,-5.694092,1.008330,-1.227885,9.116144,-8.967750],[6.953022,-0.119900,-6.868476,1.624032,-8.838036,-6.683381,1.426918,-5.460956,2.403933,-8.152652,-5.135000,-8.095571,9.237828,3.101502,1.730647],[9.560453,-8.515979,-7.828334,-5.929724,-9.199272,-1.047279,-7.434006,9.600168,-1.556128,3.294040,-1.152002,1.400574,6.617171,-5.290447,8.759936],[0.660705,-0.108427,8.562206,-0.533957,-1.421186,-5.555473,5.228754,-5.941515,1.464452,1.861125,-4.422069,-8.583291,-4.009008,-6.685565,6.043304]],[[3.759948,-7.071191,-8.020464,-8.401864,3.857920,1.302018,9.608780,-2.951351,6.977046,-6.666057,-2.816483,8.490298,-7.915191,5.408660,-2.473641],[6.509976,0.684196,3.521548,2.950900,-5.913406,6.279225,-2.397019,-0.205072,-4.470394,1.249622,-4.922337,2.487341,-8.453373,1.978582,-8.325897],[-9.376211,6.266729,5.583886,-9.255294,-9.046747,-6.944071,-4.984783,-2.794663,2.303148,1.286036,6.245146,9.878673,9.059368,4.710718,3.093037],[-8.309467,5.361423,6.876980,-8.901325,0.334118,-2.962769,-7.084527,-9.342463,0.581048,-9.562692,-9.324768,-7.305690,-2.041588,-9.050481,-0.910701],[-4.493014,3.937504,3.972422,-3.316722,-8.310036,-7.987313,3.797685,-2.802715,-9.243906,-6.009852,-3.663826,-6.632853,-8.230881,-2.799803,-5.385230],[-7.151054,2.927488,-0.481132,-9.578868,-9.276706,-6.665895,5.823660,-0.827138,-8.605648,0.595016,1.833368,3.702066,-8.578742,-8.383663,-1.296786],[2.423624,2.439560,2.144908,7.186931,4.741096,-9.984025,3.117535,5.943954,2.951794,-3.283920,-9.910821,-1.483475,1.327568,1.086619,6.473771],[8.423599,-6.347694,9.743048,-7.238914,0.203313,2.349359,-5.969753,2.297516,-0.433807,3.479884,4.158652,-6.438871,7.362534,-3.139102,9.079067],[0.361021,8.737507,-4.913321,2.795688,6.918605,-7.412140,-3.009745,7.930411,-7.849579,5.251460,-7.477061,-4.282410,-3.800382,3.067957,-7.197666],[9.310413,6.395092,-6.301355,9.789189,-7.791506,-5.093694,7.024809,6.021435,5.432073,-3.456057,1.944065,5.265793,0.583127,-1.312617,4.331061],[-6.469467,-2.806943,0.812126,9.567304,-1.910206,7.541444,-8.769086,2.040748,-3.284944,2.169939,7.458910,4.232157,-7.376477,0.046923,7.805854]],[[-1.384440,2.593016,8.176862,9.233006,2.637259,5.202835,-9.040132,-0.729361,1.357735,-1.729989,0.323763,-4.095904,8.382648,-2.762711,6.437781],[7.685193,7.155657,-7.591248,2.453182,6.926130,9.100049,0.340236,-6.835920,3.404272,-3.110887,-2.650225,-0.829543,4.932301,-7.122506,-0.323659],[2.404553,5.928862,-8.956482,-3.363639,5.607121,-1.599662,-5.183984,-4.969233,4.091491,-9.788970,-9.840224,-8.404617,7.508801,-3.926432,8.773050],[7.152308,-7.797404,3.971840,-6.997699,-5.095264,9.427616,-1.452201,-4.110240,-7.911388,9.973236,-2.635724,3.193036,-3.924230,-5.050295,-7.923314],[8.350902,-0.422950,-8.073392,-4.830915,0.183659,-3.418910,6.600931,-3.065813,-2.711768,-7.785306,-9.132254,3.130173,8.202353,-3.830270,-3.387155],[3.109691,2.875469,3.350480,5.188542,-0.901640,-0.907217,7.637845,-1.305954,8.345239,-8.776705,-5.287579,-6.224140,-8.187932,5.254002,8.092963],[-7.454879,6.529127,7.739150,0.414892,-8.628368,3.762669,9.125075,-5.499198,4.934714,-6.235934,7.072895,-7.302517,-2.891356,5.876949,9.848699],[7.707817,8.199939,5.224705,7.531212,8.714530,3.461621,-1.848823,5.328419,-9.895982,-1.488516,-4.447359,0.647473,-3.765687,-2.304973,5.197753],[-5.036644,9.681688,2.957710,-0.714182,4.064303,-4.776677,9.105715,2.007762,0.201280,2.276489,-5.944468,-3.517988,-4.376225,1.140089,-7.200883],[-7.690240,7.998475,1.876740,5.836460,5.731861,7.885391,0.712150,-1.768843,-8.986165,-6.832631,-0.854766,7.022511,-3.068561,6.527179,-0.761763],[-1.764523,-5.334031,-6.288576,-7.448003,-5.235142,7.921572,1.652761,-2.283739,2.430742,4.116343,-6.220927,0.253446,-1.381012,5.475012,9.369009]],[[-6.216614,-3.688392,-0.319068,-7.394772,-9.976626,-6.858136,-5.337658,-3.375735,-8.691095,9.638672,1.006311,8.021524,-0.244730,-4.656979,7.549634],[5.950194,1.517265,-8.711083,5.203344,-0.141932,5.424092,5.028376,-6.081395,-0.603609,6.121288,1.955159,7.604457,3.812299,-4.306804,9.410470],[-5.561803,8.648911,7.884944,6.831205,-2.993201,-3.527701,-7.007514,-8.097587,-3.183049,1.091192,-2.941729,-7.349882,1.744393,7.639765,-5.541402],[5.937810,-2.845599,-7.096096,7.318421,-3.388843,-9.071853,1.361775,-5.708176,9.409964,4.510456,-5.832770,0.629615,9.176013,8.439085,1.287833],[-9.260117,-5.096162,9.870029,-7.316679,-4.348127,1.019928,7.268550,0.350315,-3.538202,-3.928710,-0.489413,1.969873,-8.023133,-7.315851,-1.391189],[5.221350,0.778975,6.897488,-0.285400,0.725173,-3.752847,2.631164,1.116472,1.438813,-1.962710,9.262173,-8.243778,-0.817688,-1.482546,-8.565475],[-0.004439,8.815301,7.857087,2.497065,-1.668696,-4.412122,9.061094,-6.760470,5.941288,-9.218897,-3.438108,-6.970094,-7.607267,1.476932,5.081651],[9.533087,4.230513,0.273551,1.313890,-9.260911,4.091192,-6.256248,9.027568,-1.731621,-2.435574,-7.995372,-7.256836,-9.203493,5.042375,0.010062],[4.940060,9.486890,2.897393,-0.026908,4.291638,-2.296714,4.732243,2.261904,-0.299427,8.294886,-3.995108,7.173304,-6.189033,1.772364,8.637356],[3.526308,-9.733066,5.721275,9.666434,-9.076291,-9.321480,-3.920363,-8.861291,-8.292742,5.462084,3.303061,3.959912,-5.594430,-9.844208,-7.427431],[6.584005,0.837350,-4.715736,9.303834,-8.157490,-0.563091,9.984050,-2.091855,-8.900818,-6.836408,9.157463,5.525606,-7.171455,-6.201397,2.358864]],[[-4.214165,-1.386143,-3.533393,-6.213850,7.300653,-9.168484,9.916113,-0.199286,9.122835,6.200577,-4.063340,0.630764,6.421187,8.572466,2.892541],[-1.860468,2.752369,2.305305,3.581908,-0.042987,-5.368276,-2.983204,-1.815436,0.223737,5.597269,4.107803,2.600379,0.187973,-8.461502,4.198286],[-6.525356,1.334900,-4.103851,6.409161,-9.916090,-5.655209,-5.700055,-9.296028,7.446182,-1.371856,-8.129915,-6.525551,0.585764,0.180925,5.443422],[7.112403,-9.003673,1.539258,7.315517,9.402734,-0.901400,-2.549228,-7.032343,8.923837,-0.988547,6.709304,5.563559,9.464667,9.671062,-0.499169],[3.143792,-4.039200,-3.822297,-4.513547,8.816781,5.469082,-8.926619,-8.488086,1.382007,-5.302402,-1.047727,-1.028288,-9.150710,-1.643963,-1.674413],[-0.161753,-2.305687,-6.609677,-3.447943,-3.775102,-9.854653,-1.531514,2.843020,2.252071,-9.083198,-1.830432,6.750757,8.072487,-4.020222,-9.804837],[-6.157630,-8.534328,5.434483,-7.515490,-9.527610,1.052958,-0.675873,9.135319,5.405146,-9.956724,-1.250308,-7.253438,-6.000164,5.827973,5.903212],[5.562550,-1.305134,-1.259221,-9.724896,-4.452061,0.270726,7.832777,6.020982,0.886610,-1.847949,-6.658877,-1.811656,-7.367840,-9.619705,-0.807026],[6.430789,-7.079564,7.568674,-4.441674,8.292612,-7.915611,-4.293511,-9.919008,-8.134076,-2.337379,-1.024433,-0.298920,0.594724,3.393215,-8.417823],[6.968208,8.830672,-6.180808,-9.031768,6.238882,1.233729,-4.008845,4.837175,4.919646,-3.786813,-5.780257,-5.423708,-4.412772,-9.319525,-5.056645],[7.308239,-9.422974,0.928715,4.646428,4.963385,4.012097,1.957195,2.836059,-2.034478,-4.147675,-4.233244,8.938985,7.151210,4.402313,2.731867]],[[0.585197,0.818810,-2.093905,-6.000359,2.543461,-2.992478,-0.881956,-3.860481,-2.058443,-8.188395,-2.853746,-6.680090,6.055028,8.657780,8.353624],[-8.901351,2.672267,-6.567650,-3.571216,0.583104,9.421014,-1.446846,3.687093,8.792445,-6.354333,1.229703,-2.900977,-2.962204,0.896736,-4.857670],[6.210235,7.966164,1.691973,-2.183077,-7.280643,3.577572,4.512726,1.765688,-7.960208,-4.295770,-8.063731,1.073580,1.609672,2.033004,8.577332],[3.839272,-7.515084,9.754161,4.606111,-5.604322,-1.106476,0.660003,3.345861,-8.063404,5.231162,-7.557650,-3.387987,-9.944070,-7.310952,1.207103],[-2.040179,-8.672522,3.765609,-5.368284,2.512351,8.415043,-9.736207,7.900363,8.895459,8.457042,-7.401522,2.462681,-0.855343,9.984095,4.209079],[-0.625731,4.417508,-9.057895,3.072612,1.053996,7.372748,-4.159007,4.596346,-7.944196,1.956804,9.856973,2.998428,9.617745,6.314042,-5.683226],[3.341648,-4.635074,4.138036,7.375734,3.588891,4.405930,6.198116,-7.166371,8.611410,-0.852194,-4.095339,3.304869,-6.547050,1.392711,2.730401],[-6.973865,1.181611,8.315643,4.145072,5.327815,-4.939046,-1.118553,-1.530547,-7.378230,4.656770,-6.460823,4.593800,0.307678,-2.817258,4.780495],[5.826775,-3.269254,-1.618783,7.251590,7.185867,-2.251389,-1.512371,0.110946,9.422810,-8.867649,-8.537984,-9.144412,-1.976536,5.482359,6.502935],[-9.965511,-5.933673,3.285303,0.471120,9.107445,4.064255,-3.375607,-8.819140,-7.912021,9.761121,-7.676946,7.857563,2.039723,-9.104607,6.996292],[3.819123,-0.460047,-3.548325,-2.088594,4.222970,-1.109385,9.649828,-6.699605,8.060314,7.376080,5.117999,-8.718694,8.892670,7.104850,4.457428]],[[3.985014,-6.896705,-8.629863,5.467477,-0.785472,-1.339421,1.035882,0.779143,2.604913,-7.902395,-7.877105,-2.440484,-6.337295,-2.869946,-9.638767],[-7.969288,1.710526,6.918319,-5.190659,-7.697574,5.618592,9.200225,0.756914,-7.124998,9.809485,2.177587,1.796379,6.472033,9.724797,1.807630],[4.120155,2.767031,-2.081351,-4.604427,1.966101,-2.576537,-7.003765,4.453537,-5.000409,-7.576708,-3.996620,5.298042,-0.020808,-1.685281,1.246455],[3.979719,1.641940,0.572262,5.039546,-3.109150,-3.148600,-5.257948,8.739774,-8.209745,3.236214,3.063011,2.965658,2.848861,5.829052,9.589747],[7.674005,2.851010,-1.219657,9.172553,6.489000,-2.405665,-7.819922,-2.732377,5.156450,3.879809,6.535476,-4.081386,-7.835420,-6.012737,9.482214],[-8.912206,-5.111552,-7.872813,-4.933402,6.761665,3.618992,0.369752,-4.346564,5.925243,0.374322,-0.112268,-4.672879,4.995151,4.293810,-6.362122],[8.525398,1.766934,7.337198,-3.420460,8.757910,1.816734,-6.625982,-9.960795,-4.359379,-1.244929,8.415988,-9.015361,9.423334,-6.259077,-1.518372],[-9.459372,9.202495,8.417417,5.165429,-8.817283,4.354862,5.198742,-8.599187,-9.766995,-5.157468,-7.658669,-7.385055,8.773448,-1.035546,-1.665738],[-5.610238,1.827264,-7.152143,-7.183660,-8.842752,4.212073,-4.519559,8.019007,-6.686250,3.605781,-3.388791,-7.111972,3.907292,3.963980,4.460796],[-0.671955,-8.041469,4.439990,-1.590304,-7.808638,-4.876715,8.126502,-3.275101,-3.168301,-6.825119,8.258740,1.949483,7.042451,3.708709,6.521420],[-4.771720,8.862126,3.769154,-5.972356,-0.199027,-2.848896,-2.445937,-3.681294,9.742858,1.927628,-2.748199,-8.120007,1.164980,-2.902057,-0.505887]],[[8.662419,8.654320,3.402724,-8.881762,3.770685,-2.032918,6.842101,2.990686,-7.287812,-2.447481,-5.867136,-8.252882,1.524401,5.326414,6.064146],[5.978367,-4.595131,9.663336,7.565648,4.332300,-0.455615,-6.268902,-9.513109,3.801046,-5.064034,7.451493,4.028683,-6.064077,2.671169,-1.855434],[2.004839,1.623270,2.208236,-7.614811,-4.697121,0.740681,5.417188,7.726082,0.236389,-9.852271,-7.231218,-5.482397,-5.038539,-2.284405,-2.802350],[-1.850649,-9.787389,-5.501698,-7.084878,-2.877221,-9.704809,4.173846,-9.149707,-8.458510,-9.198467,2.812743,-1.019658,-1.608400,-2.355028,-3.928192],[0.308427,1.933799,-1.066708,5.877888,-9.304206,-9.632831,9.053533,-8.465646,-2.197160,5.742034,-8.348725,2.614445,5.868951,7.011675,6.245813],[-6.376826,-0.307728,-6.628168,9.014407,1.721598,-1.839198,6.289506,7.013197,0.727447,-6.317463,-3.777100,1.152153,0.782268,9.449591,9.510475],[-2.513849,-6.565370,7.233663,8.163590,-8.206654,-7.095027,-9.215596,7.789996,7.058801,9.271546,8.646304,-5.152176,-0.524201,3.202885,-4.996598],[-0.284593,4.241390,4.141086,4.353142,1.240161,1.575619,-5.128676,8.910642,-1.122860,-9.426950,-8.746380,9.834133,6.581974,-8.052100,-5.189455],[2.751170,1.772400,1.691410,5.697068,-9.303408,-2.614024,-7.279200,3.178654,-4.878241,-1.220127,-7.929438,1.434206,-7.049314,8.048252,9.905430],[0.679879,-6.570933,4.209427,-0.197386,-8.766378,-5.956710,-0.733488,-9.483742,-5.408708,8.097840,3.566552,-1.772232,-4.804791,1.888743,2.875580],[4.655033,4.716168,-0.036185,7.361326,2.695474,2.866231,-3.007084,-2.443921,2.532602,-8.459384,-5.721365,-6.308880,-2.443334,9.794261,-8.402040]],[[-9.369644,7.735816,3.228700,0.984276,-3.533985,1.413397,-4.021278,-9.897680,-3.730196,0.427528,-7.216013,-2.692035,-8.851257,2.598515,1.023030],[3.234667,0.525747,6.934237,-3.479715,9.518549,-1.100720,-4.670707,7.417534,4.831540,-8.799975,-9.459356,-1.304810,-8.610334,7.687809,-5.015582],[2.222166,-6.493608,6.621979,-6.382853,-5.508370,-4.905334,-3.035917,6.934625,4.088344,8.435907,-3.949254,7.031077,-5.278413,6.597877,1.430744],[-1.103467,8.981735,-6.655055,3.741644,-9.772501,-6.080452,-8.511675,0.609029,-6.808447,-0.532771,6.508588,3.837282,-2.293917,-7.380105,2.058267],[4.453744,-1.698530,0.103099,1.646550,2.995735,-7.212360,7.844712,-3.667289,8.542316,6.691505,-7.479861,-5.699715,7.692389,-9.151949,-1.650745],[-9.066660,2.070700,3.681248,6.645277,9.524455,-0.738263,-2.625648,-7.316576,7.088211,-3.827905,-4.972059,3.401668,-2.572005,3.913354,-8.826700],[1.710750,2.191039,4.365647,3.600305,-2.386418,-6.102372,-6.955011,-2.638081,5.853303,-3.762460,-4.656655,3.064071,6.318680,0.791080,-8.428628],[1.028904,-4.577280,-4.070257,4.104821,-7.933849,6.176781,-7.926064,6.208450,-6.436672,-7.111195,-0.196047,9.334202,-6.229831,-5.016923,0.726623],[3.029090,-0.270506,-1.047943,-5.377344,-8.318508,3.570967,0.430161,5.784221,-4.888420,8.022772,7.582717,1.252361,9.884927,9.721152,0.897899],[-3.175009,7.097637,-9.929490,-3.249729,8.241085,7.029696,-8.079911,7.149519,-1.639049,9.235251,-7.184291,6.427138,-3.127454,-4.641270,-7.033669],[-6.709118,-8.777253,0.253757,2.208870,0.087349,-2.148362,8.866037,2.519095,4.875569,-4.456482,-5.424118,1.376679,5.562589,-1.913041,7.830336]],[[1.650875,-9.161992,-5.713819,8.057614,0.879616,-1.210830,8.043199,-9.135879,-1.971374,-0.276208,-5.360833,-9.444471,4.022478,2.216517,8.606311],[-6.925065,6.082585,-8.674110,5.741092,3.845294,9.541163,-1.196930,-0.675351,8.902320,-4.621512,7.037286,-5.646926,-4.086762,3.664829,-9.120671],[0.109690,-9.380851,4.386727,-1.646979,-6.309991,9.710862,6.426873,-9.543603,-2.392556,9.635326,-6.727277,1.831493,-1.999617,-4.759917,-1.119533],[-0.686149,2.408764,-3.416589,6.989169,7.679665,-4.047829,8.607848,6.848143,8.901669,-1.911156,-8.305038,-8.709170,9.618569,-7.199623,-8.241987],[-7.035814,-2.172611,0.411330,-5.025187,4.820586,-8.070733,-8.825381,4.417497,-2.564205,6.848730,7.749819,0.548343,-5.257669,-7.425492,-1.877566],[1.039458,3.764457,-0.917746,-4.112498,-9.786117,7.081029,2.416355,-1.041451,3.953030,-0.259837,8.653157,-5.440640,3.622720,-5.322360,9.339869],[-8.400894,0.232177,-1.803578,4.714325,6.775561,-2.983273,-6.939012,-8.764402,6.391878,3.920498,2.979503,6.623768,2.498516,-7.839067,1.732242],[-2.263735,-8.441668,7.519186,-9.235807,9.470522,-1.740440,-3.775039,9.229659,-7.195605,-3.569314,-6.892529,-1.384408,2.202480,-7.041362,2.665094],[-1.962983,-8.029571,-6.263203,5.426998,-4.244949,-7.509374,2.676933,3.320853,4.612722,2.309622,-3.559248,6.591142,7.154622,-1.777391,-0.935429],[6.772608,-5.143818,5.977635,-2.415169,0.633965,6.317469,8.141771,-7.805904,-9.600166,-7.838200,4.429331,6.424045,-5.040241,2.550006,1.871738],[-1.366223,-2.387808,-1.729829,5.216327,3.771629,3.235499,-3.401283,4.414584,5.837105,9.162219,2.494288,-6.258303,2.803806,9.162110,-1.250425]],[[6.933083,-6.379947,2.946009,3.737913,7.875841,5.286296,-6.292539,7.521092,-9.706293,3.989713,7.542210,-5.981844,5.638873,-3.762788,-7.885569],[8.074068,1.119065,-8.462519,-9.372533,-7.129713,-8.239435,-3.483630,6.396465,-9.395667,2.414963,2.815532,-9.848625,-8.482043,-2.094881,-1.740981],[6.810541,-8.503274,3.774085,6.424742,-7.615114,0.670627,8.727495,4.154537,-7.118035,-7.364530,7.916062,-0.490194,1.234842,-6.927402,1.736985],[1.517670,-9.548733,9.319721,-5.458899,-9.094807,-8.057161,8.974651,9.668739,1.523460,-5.384151,6.187390,7.624857,1.124793,7.846208,-1.896892],[-6.117725,7.300351,8.776437,5.298059,-7.258979,6.419498,3.222131,-8.820143,3.733676,-4.735980,-3.115201,-0.083493,8.804779,-4.635989,2.278178],[0.326719,-7.703086,-1.642587,-3.601610,8.040982,2.864237,9.246854,8.652077,-3.857726,4.549046,-0.231373,-4.901278,-0.634118,-8.329394,-8.502169],[5.556498,-8.074100,7.879341,-1.210846,-4.067308,-3.167480,-2.735071,-5.854043,0.971713,-5.212276,-8.384633,-7.298891,6.473638,-9.541617,-4.702919],[7.272732,9.885714,2.173666,2.948324,-0.641918,-8.354691,3.210505,-7.538368,-2.921457,-0.865470,2.889623,-5.384858,-8.305965,-7.522465,7.075298],[9.175683,-4.443140,-0.504148,5.475910,1.553672,5.101152,-3.050284,-7.042074,8.995090,9.994991,-7.951124,-8.813114,-1.171088,-7.513043,0.106652],[8.063634,5.921464,2.976395,-4.921512,5.133082,-1.781876,4.630655,5.965599,-1.421133,-3.136860,9.614587,-1.736369,4.561325,-7.863214,8.761185],[-3.624995,-2.321589,-9.738143,9.748452,3.855167,2.964558,-6.791795,-6.988803,-2.646205,-3.588250,-8.893685,7.562893,0.565542,-3.636137,0.551129]],[[5.777754,-7.561458,2.503014,-4.986079,4.417327,0.596104,9.759800,9.946542,9.982086,-3.305326,8.062758,1.235744,8.659143,7.882564,-9.830473],[1.597894,-6.411859,-5.765538,7.486257,3.068048,-2.381150,3.586042,-2.070240,8.219607,-9.954397,8.549096,9.052713,8.478653,6.606257,-8.116292],[4.376541,6.320650,6.321174,9.360963,-3.703246,-2.911505,6.451921,4.171635,-9.835043,6.296725,-9.677454,-9.271163,-3.518362,2.541893,8.918932],[1.933414,2.494101,-9.487921,-6.887931,0.110850,-6.341858,9.185939,7.009161,8.653490,-0.805178,1.183742,2.582104,-5.555863,4.050666,3.475037],[3.110173,7.412936,-2.698676,1.317004,4.891980,8.575203,-4.662493,7.017987,1.349591,-7.012079,0.441848,3.079288,0.058234,-3.711538,1.172807],[1.446475,8.054631,4.937452,7.122171,-5.044399,-4.731802,-3.006195,5.689686,-2.915790,6.758564,-7.033559,-7.053216,1.922171,3.282080,-5.923522],[-2.784112,0.664758,-1.859430,0.472460,9.177124,-5.121316,7.689949,0.870972,-3.874245,-1.719306,-3.338746,9.482937,-3.154744,-3.658766,-9.340417],[-5.804315,0.705422,-4.402889,-8.311344,1.597557,-8.470799,6.892011,-6.167954,-0.683807,3.708168,-4.323821,8.350489,-0.308708,8.350673,3.901109],[-3.655854,-9.173139,2.117136,5.795613,-6.452925,2.007063,0.680803,-0.868078,1.965833,-6.629878,5.579499,-8.164388,-2.126125,-8.937179,-5.790611],[-7.506664,5.232903,-9.543090,4.436040,2.437938,-5.541820,-8.297851,2.761550,4.921796,0.034377,8.854991,2.545634,3.341776,5.885207,3.130158],[1.961271,-0.905135,-3.235782,8.701920,-7.332970,3.782881,-0.812816,-4.227026,-6.652715,-5.573966,-2.608990,8.228303,-9.289383,8.947190,-5.103222]],[[6.856513,-1.053600,2.801728,-8.355378,5.236952,2.836620,0.738274,-5.829884,8.510575,8.810148,5.594589,-0.480330,5.604630,2.749985,-6.902845],[5.038211,-9.740042,0.274353,-1.445231,-6.010239,-7.959115,-2.363884,1.036658,-0.115021,-8.704743,9.875447,0.498086,-2.407976,-2.277147,4.530037],[6.456862,-7.151920,5.913450,0.475939,6.899299,5.713937,6.008452,7.048674,-6.650518,-0.660640,9.885533,-0.904462,3.647379,-6.078085,8.346050],[-6.621937,-2.002874,-5.163770,-3.459353,-0.977543,2.641934,0.106312,5.292647,-7.102195,-4.451176,-9.442925,-9.890396,-4.358168,2.554341,1.738323],[4.918530,-3.501936,-5.095837,8.742765,-4.204603,-7.459400,8.827757,8.023859,-5.913472,-1.589762,-2.325582,-0.044109,-4.828919,-4.270655,5.292541],[-7.223549,6.106985,3.314574,3.817326,-7.758102,-5.357652,2.823835,-1.708580,-2.042063,-2.493261,-5.663132,-7.827534,0.165792,4.548504,-2.457073],[3.455883,1.635731,8.509547,-6.844812,2.600079,6.253558,1.942577,8.976406,9.020714,-9.121825,6.670842,-2.188708,-9.844478,-3.285910,2.436000],[-2.365046,0.385755,8.818967,-4.363120,4.616705,-3.634187,2.608900,9.650828,8.737457,9.472281,0.183865,-4.944033,-1.366756,5.486246,6.479080],[5.530355,-1.700420,2.096136,-4.645467,3.587513,-8.179683,-5.459655,-3.943252,-3.615142,-2.696399,5.625347,-1.091012,0.317728,-8.776173,3.966002],[9.976876,-3.175397,5.562073,4.930454,1.732168,4.411817,-7.454783,-7.927415,-9.086150,-0.207165,-2.266928,-1.108701,-2.742331,2.643860,-8.632775],[-5.669054,5.654544,6.105832,-7.059344,-4.692879,-2.102598,2.905621,0.723916,3.325260,9.678660,-6.819415,5.542061,-8.311493,-6.349206,3.430734]]], dtype = "float32")#candidate|3502|(14, 11, 15)|const|float32
bop_3503 = relay.less_equal(call_3487.astype('bool'), const_3502.astype('bool')) # shape=(14, 11, 15)
bop_3506 = relay.less_equal(call_3488.astype('bool'), const_3502.astype('bool')) # shape=(14, 11, 15)
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_3512 = relay.TupleGetItem(func_3216_call(), 0)
call_3513 = relay.TupleGetItem(func_3217_call(), 0)
bop_3515 = relay.subtract(const_3502.astype('int16'), relay.reshape(bop_3503.astype('int16'), relay.shape_of(const_3502))) # shape=(14, 11, 15)
bop_3518 = relay.subtract(const_3502.astype('int16'), relay.reshape(bop_3506.astype('int16'), relay.shape_of(const_3502))) # shape=(14, 11, 15)
func_2726_call = mod.get_global_var('func_2726')
func_2727_call = mutated_mod.get_global_var('func_2727')
call_3519 = relay.TupleGetItem(func_2726_call(), 0)
call_3520 = relay.TupleGetItem(func_2727_call(), 0)
bop_3528 = relay.less_equal(call_3519.astype('bool'), relay.reshape(call_3512.astype('bool'), relay.shape_of(call_3519))) # shape=(14, 1, 15)
bop_3531 = relay.less_equal(call_3520.astype('bool'), relay.reshape(call_3513.astype('bool'), relay.shape_of(call_3520))) # shape=(14, 1, 15)
uop_3541 = relay.acosh(bop_3515.astype('float64')) # shape=(14, 11, 15)
uop_3543 = relay.acosh(bop_3518.astype('float64')) # shape=(14, 11, 15)
uop_3552 = relay.acos(bop_3528.astype('float64')) # shape=(14, 1, 15)
uop_3554 = relay.acos(bop_3531.astype('float64')) # shape=(14, 1, 15)
const_3576 = relay.const([[[8.542644,-4.860226,-1.061699,0.251755,3.012527,6.679780,0.467727,6.817655,-4.553760,-4.834394,1.184290,-3.217512,-5.395173,-4.004592,-1.597928],[7.963867,1.093253,8.329696,-3.592235,8.874438,1.805069,-1.157509,1.177816,6.743263,5.607955,6.000879,-8.063419,6.813192,-5.744293,-3.457017],[-3.011550,-3.230047,4.904442,5.888936,-6.299212,1.319978,8.381148,-2.691201,-4.556290,-6.915743,-1.372960,-3.080795,-6.720761,8.653348,-2.619130],[4.863959,8.053755,-0.612920,8.246023,-8.241104,1.917978,9.171045,-0.291319,0.109470,0.333269,-9.028984,-0.790493,-3.448962,-8.286019,6.841189],[-1.280516,2.345852,-1.453469,-3.695905,9.518871,-2.856532,4.984182,2.935612,0.026614,-7.761189,2.195814,-6.008766,9.868191,-6.116816,6.955243],[-4.681008,-0.328323,4.590628,-3.164385,-7.773621,1.757568,-2.187263,-6.792774,-4.852298,-8.340707,-7.056792,2.842210,6.635096,8.283087,-8.778234],[3.855375,-8.268402,2.740846,0.263043,-0.943005,8.011385,-1.171356,-5.463708,-3.717723,-7.341826,5.432838,-6.609410,-4.511247,5.535943,7.199013],[-7.140187,7.264225,-1.243568,-1.272664,-8.103292,6.371185,-3.957965,9.259943,-7.051992,2.937457,-5.446837,9.047494,2.871835,7.112857,3.371804],[4.375529,4.068670,0.366029,7.015064,1.874127,-8.454327,6.133675,-2.902809,8.446026,-2.411527,-0.625910,5.471677,5.406201,6.055719,4.590216],[0.860507,-5.897710,0.626736,-2.242391,3.957192,-1.045113,-8.507707,5.978143,-7.599294,2.389986,0.050556,-6.014574,7.800190,-8.460366,-0.282943],[-6.324783,-1.510726,-2.234701,-6.823947,-0.150056,2.896823,0.190974,-3.640706,-6.382830,6.955235,-2.646140,8.862486,4.992188,-1.495461,4.874139]],[[1.370040,5.049800,-0.018448,-3.439227,-7.431900,9.243651,2.361083,-8.857138,4.482239,5.263067,-7.630167,1.697845,-1.828342,9.034933,-3.268073],[7.700310,-7.756792,7.464152,-2.145350,7.487869,-9.154866,-1.152558,3.737932,-7.104419,-8.588565,2.572730,5.787659,-4.247234,8.853784,-6.461458],[7.938589,9.088179,-8.981942,-1.420412,-5.396468,-3.967677,-3.551013,1.768057,6.127151,-7.877058,2.495033,-3.164860,0.410114,-6.487867,-7.618169],[-6.286260,-4.368394,5.327617,7.154801,3.046771,3.038491,-7.605183,7.881895,7.998610,5.118564,-1.929690,4.987719,3.500428,0.250062,8.307692],[5.334490,8.052848,-0.149834,-6.326418,5.137014,2.983434,4.599427,-1.375990,5.003797,5.064523,-4.831989,4.392150,2.041449,-6.110862,-6.883231],[-5.352891,5.522637,2.335261,8.877334,6.902185,-0.455233,7.699342,2.893923,-7.643084,-3.854171,3.689801,4.333331,-9.191554,-1.263414,2.551901],[9.114856,-5.610749,-5.126004,-7.017996,8.639957,-4.164761,-3.886727,-8.265972,2.173364,2.297444,-0.344730,-5.726398,0.950397,-5.701764,9.114100],[3.258344,-9.871819,-9.230116,7.943542,-9.755532,-9.854873,-4.182612,-6.581641,-4.240042,8.903947,6.937410,4.370187,7.906046,1.041380,-5.976550],[-5.971063,8.825790,2.279850,4.759064,-3.644087,9.734295,-2.444379,4.002299,-8.900825,-2.904324,3.289030,-3.542132,-7.014556,-0.243612,4.914386],[-8.254962,-4.357697,-1.563888,7.443480,-0.498912,9.637235,3.006367,-7.557602,0.012946,-1.322254,-0.188852,3.251964,-9.472639,0.782289,6.816766],[6.599268,-7.085437,7.729357,3.228245,-8.781141,-2.991709,-5.300146,6.581752,7.729642,7.257195,-8.403957,2.512221,-1.516101,4.370633,-3.925101]],[[1.015941,9.253809,2.645412,-7.022595,1.198704,1.400440,6.995921,7.860104,-6.598608,4.254006,8.628184,2.910115,7.178557,-9.399590,6.198690],[-8.497063,9.252250,-0.485778,-3.669977,8.241044,3.892354,-1.114147,-8.559072,7.403615,-9.295773,2.258212,0.068493,-3.642903,-5.578349,3.579382],[-9.546297,-9.045053,1.235385,-4.134836,-3.767939,-4.351733,-6.610851,-9.121556,-7.000270,7.134676,-4.417290,-3.175693,-1.920476,-3.966834,-2.463182],[-1.583001,0.951075,-6.675349,-4.883279,6.587234,-8.210016,-5.986652,-0.574100,-0.119758,0.571118,6.964562,-1.459509,3.735033,-5.877965,2.786767],[6.440526,5.404880,9.961895,-7.621467,8.068620,-2.224499,5.909333,-4.838827,8.998508,-3.108316,7.743878,-2.801595,-6.045917,-6.326298,5.085586],[9.330459,0.983102,-6.198394,-1.300978,-8.577779,-8.590710,1.799208,-3.436376,7.868159,-6.921058,-0.767049,7.830950,7.906853,-5.094426,-1.915115],[-9.502103,-8.802744,0.795529,-3.567049,7.461182,5.952692,6.064775,1.652350,-9.245384,0.517000,2.523646,-1.926212,-7.427913,-3.140225,6.897487],[-7.261009,-8.286956,-2.111950,9.585664,2.286608,2.342012,-1.931287,3.104867,-9.673045,-6.499759,1.715364,1.331662,-1.807187,8.038242,-0.298839],[-6.090398,-0.652994,-4.899508,-9.352085,6.736170,-9.849662,-6.802163,7.386742,1.834260,1.829781,9.306841,0.905062,5.861513,-8.626508,-6.607937],[1.469600,-9.138051,5.444820,-1.720989,-2.866643,1.596671,5.658896,-8.406960,9.153579,-3.199991,5.520778,7.043074,0.847616,4.478617,-7.046181],[-2.537873,-7.535362,2.346533,2.058220,9.794624,-3.812237,3.745918,-0.995452,-9.685641,4.159870,-9.554084,2.118480,9.397743,-9.561405,-7.602042]],[[-8.547046,7.289586,1.019236,-5.340509,-0.101316,3.552517,-7.593361,-4.534361,-0.428360,-6.259464,-4.832954,-0.068515,3.599343,-6.091403,-0.451415],[-1.797120,7.680792,2.440272,-9.454468,-1.542022,9.709118,3.462043,-4.143733,-2.298933,6.411500,-7.876135,-4.902514,8.831385,-2.148698,6.112164],[-1.910399,6.227411,3.538311,5.808487,-2.678937,3.430563,3.498802,4.306162,-5.443807,-9.634610,-0.410672,4.021906,9.874432,-1.357406,-2.025515],[2.541794,7.603975,6.265385,5.148853,8.991513,-1.190305,-2.925324,0.318282,5.840619,9.155423,0.372329,-3.420992,-1.803895,9.457559,2.382666],[8.554653,0.332804,2.227901,1.758829,1.135909,-0.307626,3.935848,9.759777,-3.115696,8.462571,-8.378134,4.385354,5.354474,-6.826039,4.548409],[8.108043,-1.198062,1.096919,0.911545,1.238094,5.432434,-1.997597,-4.536611,-6.101513,-6.913943,-6.478828,-1.298936,9.137208,-5.842907,2.870314],[6.844991,-0.323586,3.742086,1.692245,-4.156522,4.399806,-4.266579,7.715158,6.740638,5.997620,9.281525,-5.971974,3.805433,8.192110,3.722014],[5.110400,2.249936,1.230516,-5.998910,9.721893,0.537089,-4.409285,-3.749986,-2.811367,4.030136,7.020391,6.867915,4.457036,1.464826,-5.385431],[5.258453,2.887219,8.531165,6.330475,3.076123,8.958188,8.556425,-1.686769,2.100695,6.094179,-9.345305,1.757918,-5.469334,1.655172,3.127381],[-0.993942,2.146451,-6.644959,-5.954450,-7.515340,-5.083270,-1.126338,-1.223184,-7.047144,0.679128,-5.582267,-1.573579,-8.410314,-8.070663,8.932901],[3.282171,-6.829121,1.161775,-7.540849,-3.344109,-3.226037,-9.264322,-3.420772,8.885340,-6.792156,-2.471844,4.610634,-8.934025,1.123180,3.648500]],[[-2.758177,4.476741,6.220373,8.440953,-8.715489,6.551648,7.742345,-8.416308,-1.088828,-9.206492,-8.036510,5.755244,4.737718,5.274775,4.333685],[5.643311,-0.683665,-5.997160,-8.857352,5.153122,-2.955757,3.746121,-5.090658,2.492169,2.559075,7.895724,3.395078,4.848660,-9.051531,7.473804],[2.234934,6.015753,3.605128,-3.203814,-6.242182,5.851950,-2.637765,-6.797532,-3.240922,3.960100,2.433652,3.082999,8.583224,2.396994,-4.498860],[1.673733,-8.075943,2.911702,5.718723,5.931237,6.308980,-2.529599,8.951994,-2.793185,-1.766851,0.721180,-8.862441,-3.290706,-3.409046,9.986551],[3.671532,-9.385391,3.967465,9.585294,4.967260,-2.186799,1.186533,-5.225358,5.001095,-5.657679,-3.345276,4.285473,0.365472,5.091267,-2.787417],[-9.872891,6.701396,5.325407,-7.048549,7.158662,1.792066,-0.471454,-8.007618,8.703529,5.048068,-6.383755,7.300773,-2.909412,4.180405,-8.267535],[-9.490846,2.800953,-9.661855,-7.929806,-5.635979,-0.222311,-1.998629,-9.254311,-6.400312,-1.719913,-9.638691,1.281790,4.758947,-2.597379,8.909413],[-8.439965,4.023591,-4.673591,-5.635246,-8.050731,-9.129967,-7.870434,4.273836,-9.217873,-6.441307,8.649135,1.704806,-4.872073,-3.783385,2.925256],[-7.058844,6.634664,-8.540941,9.255269,-4.317986,4.906202,-7.436831,8.638636,-7.713297,3.695850,9.401750,0.934259,-8.604950,5.839767,-9.011250],[-6.400916,-4.327367,-0.210020,8.137399,7.034414,8.777608,4.180805,-0.517087,2.594157,-2.121224,4.328631,5.133805,-4.530017,-2.654658,-8.554783],[-6.703776,1.226367,-9.995654,5.298749,4.569654,-0.031775,2.800152,9.964009,-5.562202,1.097345,6.175154,-8.902774,2.738212,-8.204509,-3.392711]],[[0.978365,-8.086141,6.839876,-1.840444,-0.710074,1.986912,9.996345,-0.885506,-9.053238,0.744995,8.984965,-5.684192,-2.438626,-6.102295,-9.008673],[8.560094,-4.042566,-1.256984,4.035674,-6.260355,5.678304,-9.568623,6.684645,2.338427,1.541645,3.858344,0.673450,8.986822,2.723944,0.265022],[-0.129542,2.342312,-1.932035,7.558179,0.531749,7.946094,7.299122,7.183888,4.370360,9.251122,3.662684,7.530574,-2.675415,-5.077075,1.216982],[0.734393,1.634432,-8.483580,1.593787,0.448568,4.302022,1.083380,-2.756424,6.916508,6.498046,-6.923429,4.602747,6.904991,-7.735068,-7.476477],[5.087569,-9.753682,-3.554428,-9.911553,-5.759794,-1.076602,5.323799,-5.415528,-0.075343,5.958834,-6.870041,8.154395,4.300357,-5.723997,-2.880004],[4.777772,-9.900764,-9.899316,-9.881857,-1.228272,-3.580613,1.916103,-4.278753,9.688266,3.387937,-0.514863,3.791624,-3.610551,6.367800,-8.735102],[0.529417,9.836316,7.925638,-7.372846,0.501687,-9.013930,-4.550104,8.145679,-0.728444,8.889829,3.612408,1.752389,3.866801,1.791079,-3.721930],[2.449411,-3.439535,-2.498118,-4.882452,6.911771,8.571512,-3.117708,4.986255,6.546992,-8.084349,-4.255776,-8.804095,-8.095657,9.709757,-6.549819],[-3.019510,1.490565,0.309192,-9.755932,-7.272156,5.182689,-8.193181,1.451529,2.491873,2.661973,-2.608757,3.520808,5.513432,-9.207750,4.898380],[5.199718,-1.158283,-3.791672,-2.068278,-8.578987,8.576417,-6.546133,1.214755,2.160653,-2.319655,-5.411250,-2.992637,-7.656533,-1.313378,-2.811031],[6.266394,6.762922,-0.951676,5.023662,-2.260550,-6.387991,2.912972,7.826751,-5.097691,7.995668,9.330160,4.515832,7.447874,-6.074025,9.065471]],[[-2.273298,-8.865433,-8.164740,0.576732,7.114386,9.406267,7.766554,-3.629141,3.588286,-7.031080,-8.697976,6.880068,8.543893,9.465056,-5.519760],[8.870971,2.685181,-6.807999,-6.770013,-1.525871,6.462692,1.352631,-0.150881,-8.049333,0.108145,0.753837,-9.335027,0.103206,3.233387,7.175016],[1.133816,-3.376518,-4.091324,0.416224,2.200858,-5.028594,5.067431,3.430665,-6.007343,-1.989181,-8.274980,9.952742,-8.087527,2.575749,9.394933],[4.888071,9.348479,9.787417,-2.757941,-2.087457,-5.895689,-3.751968,5.156422,-2.440784,0.566353,6.976962,-9.087522,4.599784,6.386930,-0.348906],[3.263119,-9.257610,-1.085994,6.353312,-2.421103,-3.730664,-9.149114,-6.900940,-0.244913,3.540840,8.760037,-1.755754,1.809438,-6.264364,-9.033689],[4.700107,-7.347346,-8.919260,-9.541677,2.933361,5.822391,4.978596,6.690394,2.512154,-4.951492,6.885976,8.168627,3.189330,9.418343,-0.929055],[7.251058,-6.668779,3.736896,-0.845571,-3.946644,-6.028095,8.711765,5.920529,6.623522,-6.811950,-9.853416,-2.373613,9.696462,-6.462709,3.376148],[-4.922242,8.244303,0.955336,7.579550,-8.900263,9.775235,-6.443000,-4.687277,8.233716,-7.858242,-3.294043,-6.457730,3.419377,-3.535822,-5.691660],[-6.159094,-7.939956,1.124648,-6.428529,6.685479,-4.827908,7.143632,4.225482,5.374063,1.592102,9.294635,-8.304858,-6.624823,6.681945,0.136161],[1.872534,3.216153,4.975646,8.566726,4.394446,-3.134937,1.137667,-3.055658,-8.166077,-2.728335,-4.908114,9.724031,8.154261,-3.209347,-5.141561],[-0.493237,6.727476,-6.310269,8.732248,-8.027569,-3.463318,-6.335637,-4.929763,7.750175,-3.486817,-8.107254,9.397187,5.582057,-6.394947,2.989347]],[[-2.790188,-7.347733,5.276539,-1.584514,-3.736312,-3.482928,-9.976173,-8.689114,6.629062,3.751664,7.964507,-1.261500,3.527584,3.839192,7.582178],[-0.637364,2.282062,6.978829,9.045754,5.396013,-6.093103,3.690370,-0.150961,4.336370,4.008238,-6.134381,9.407972,8.873839,-9.695549,-2.605228],[7.333815,6.288587,6.180883,-7.590481,6.793352,-4.673580,9.773542,-0.699425,6.660105,2.118463,-3.787559,-9.245936,9.011165,-8.975899,-1.076551],[0.468649,2.074275,-5.298695,-9.481115,-2.241501,-0.009509,3.417375,-5.231047,-8.728001,-7.577707,-0.846172,4.676841,-3.668752,-6.713022,-7.055960],[8.534797,-1.326520,4.569354,9.112279,4.896197,6.793053,-8.148046,3.797483,-4.732904,-1.041525,-2.785415,7.245709,9.920660,-3.942217,-8.665008],[9.567619,-5.343535,-2.032932,-2.005254,0.356848,1.352395,-7.514881,-4.965437,-0.168457,8.380526,0.139381,6.594051,1.547794,-1.420414,-0.642033],[-0.798571,-7.250419,-7.677989,-0.538574,-3.850018,-2.243063,-1.273349,9.020461,4.148175,9.150960,-2.555973,-8.994526,3.664647,4.252884,7.923147],[-9.724626,8.773080,-1.857996,-7.377551,-8.729023,1.686710,-1.022459,7.815763,-8.098462,-2.754216,3.036393,-8.814444,-6.922651,5.263743,4.395896],[-0.597223,1.967206,-1.539339,8.433262,-8.000825,1.029771,-5.215452,-2.561840,0.142501,-2.773904,-2.156942,-5.511785,0.309904,0.940619,-0.944397],[9.164986,-1.758852,-6.817441,3.930120,7.709878,-8.144470,6.575885,0.341423,-0.750989,-9.253503,-0.018478,3.148606,8.984166,1.344751,4.845312],[5.128634,-8.566321,9.974353,-2.342379,-9.418395,3.491986,-4.476732,-3.621444,-1.865072,-9.031309,5.748195,0.523214,1.477976,-0.141095,6.625608]],[[0.506241,-6.690993,1.188841,-6.915894,-3.347484,2.375056,6.765723,-3.180558,7.999253,2.243012,3.212830,-5.320079,8.795908,5.044039,7.887889],[1.195709,1.607516,-4.285967,-4.486969,-7.384273,-0.233439,-7.736433,5.781372,9.107918,1.805583,-9.287969,4.365237,2.821478,0.026686,-8.633164],[-9.322098,9.035179,-4.900241,-0.258875,-4.534113,7.677402,-6.977257,0.078786,5.127757,9.840254,1.009263,2.011492,-7.119183,3.933045,-6.962034],[-2.269974,6.359440,-6.600432,-3.228748,-8.974345,-5.947641,8.686349,5.867831,-4.123870,8.495176,1.156199,-5.708688,9.870841,-8.577547,-8.741714],[2.995654,9.243072,-4.811724,-4.189475,-9.919629,9.230364,-1.993130,8.612582,2.400726,-3.757927,3.281829,9.433532,7.576181,5.336298,2.751201],[-4.213505,-4.795663,-8.364937,0.330283,4.139511,6.598330,-1.548990,6.067486,-6.958375,-1.006039,3.202708,-2.736688,9.306931,-0.521123,0.439441],[-3.086188,-0.650752,5.400099,9.942519,9.484279,-2.187483,9.831151,-6.318961,8.135105,-0.985787,-6.344698,5.839171,-5.546021,-6.413656,0.193615],[4.838485,9.540996,6.040868,-3.988341,7.409213,9.662763,-6.491907,9.453709,-0.905170,5.307737,-7.691840,-4.123707,9.072979,-0.403617,2.250275],[1.459385,7.142436,-2.098025,-8.557018,6.730135,-7.376834,8.105534,1.656950,-9.170647,3.028617,-7.917041,0.734535,-7.695843,-1.994401,-3.912235],[-0.145752,-6.894353,-0.191836,-0.913799,7.352038,-2.213406,5.674408,-6.647278,-6.439100,-0.806668,7.444319,2.483343,8.707942,8.094635,-4.165593],[-3.817137,5.226627,-7.347159,0.268827,-8.104046,-3.971233,9.580280,6.142063,4.120385,-4.203967,6.569066,-9.129930,-6.970311,-9.526533,0.299965]],[[8.995023,-0.035690,-3.250131,-9.723415,0.660087,-4.346144,2.814014,1.442155,-1.249165,4.449167,-0.447815,-3.961037,2.708986,0.484411,-8.461126],[6.402794,-6.607313,-2.849953,-7.450661,-0.234350,-7.169262,-7.191317,-0.688126,-5.167036,-4.540891,9.350708,-5.697020,3.952519,-6.658540,-3.240811],[-5.282117,-9.089156,3.010925,0.993826,4.985065,2.214105,6.275251,-7.201727,-1.431494,-0.942019,-0.042083,6.771107,7.963047,-6.870864,6.253759],[-1.750425,-8.734069,-5.001973,9.274224,-3.976148,-1.240026,-7.271684,5.329196,1.210014,4.184118,-2.246724,-1.072859,8.363028,-6.205791,4.282427],[-8.062797,5.920048,1.122932,-6.639768,-7.516277,0.421479,-5.167189,-5.573333,-1.452310,0.462661,0.473012,1.524027,-3.946779,2.651036,9.796945],[-8.105206,-2.843860,-0.686287,-3.805668,-1.139890,7.776775,7.914497,-5.890940,6.952195,4.625213,-5.617516,-5.748806,-8.002975,-0.949166,-2.439021],[7.938124,8.757488,-6.571058,0.076358,-7.590963,9.252759,7.986261,-4.195472,-4.622351,3.391947,-2.948381,-5.435144,9.909589,2.630486,-5.149915],[7.582180,7.300047,1.717026,1.577128,-6.565442,8.978240,1.134701,-5.192395,-6.564602,-9.063652,-2.983900,0.857850,7.846736,-2.610836,5.306330],[-8.847994,-4.776609,9.969896,-7.508694,-7.597809,2.490111,-9.931332,-2.796192,-0.570407,-5.822240,-5.800360,4.233558,3.763073,8.995776,-7.865333],[1.730297,2.104552,-6.025245,2.486328,6.696255,9.859887,3.414564,-4.801747,-5.722937,-1.365157,0.162372,0.854796,2.941735,6.582015,-7.948298],[7.402185,4.607128,6.251097,4.652869,-2.249265,-7.095388,6.678043,8.624692,-1.822258,-4.103103,-4.683080,3.382764,7.627399,3.443560,7.056873]],[[-5.580392,2.783437,-7.683712,1.298590,8.178429,-9.560833,7.631429,-6.471854,7.562407,-5.366110,2.965296,4.135682,-7.703271,9.465520,-7.743458],[-8.221996,6.267783,-6.552095,-5.069358,-3.719367,0.064165,-4.815026,-9.717756,0.594479,8.717477,-3.367359,4.347392,2.118498,-2.923738,3.552815],[-7.004195,1.028145,1.305769,8.195472,3.115784,8.608283,-4.459298,9.463163,-6.647486,2.311761,-7.238580,3.115340,9.154729,5.265999,7.841192],[-4.770705,-3.923780,-3.632884,1.496759,-4.108974,0.526903,5.490246,3.038655,-4.503684,-3.807669,3.968566,6.110455,-0.659562,8.165299,-3.170919],[-4.369329,-5.261057,-4.638912,-8.920388,-8.323488,-9.090740,-3.670425,-7.250475,-0.764541,-5.782515,-5.093644,2.258528,-1.878471,-7.710818,-6.520027],[-8.556183,-5.620910,4.896170,9.746449,-2.739443,-3.092712,8.277714,2.020235,-6.816615,1.480438,-8.060115,-4.784303,5.456279,2.256731,5.720983],[3.084440,-0.857973,-5.791956,-6.238836,1.036653,-6.844230,-9.715016,-5.640526,0.182997,7.796621,6.998165,-0.746496,-6.318692,-9.258566,4.870943],[2.470456,-7.904420,-3.432258,0.507610,-2.036909,-5.548511,8.768490,7.588184,-4.779904,-2.657436,6.878974,3.366392,-4.316534,5.597463,1.654461],[-9.590707,6.743980,-1.137862,2.566183,5.817721,-5.290470,-8.994611,-2.100511,2.253772,-7.744620,-0.691015,-0.390686,9.237983,9.390345,5.745055],[-3.048970,6.982496,-1.690842,4.933812,-6.786574,-4.413413,-4.383544,-4.692215,-6.781522,2.561227,8.940821,-7.454495,8.564843,-1.704597,-5.664168],[7.317582,2.132864,9.111761,-7.050546,-8.246783,3.989459,0.091427,5.147646,-6.470084,-9.050889,9.441220,8.987821,1.278252,3.058868,-9.601872]],[[3.161153,-0.071010,-9.993528,6.039207,5.434511,0.872889,-6.159741,-0.109006,-9.001510,6.399876,3.464838,2.848601,-3.548988,8.444141,-8.772168],[9.084975,-1.631468,7.638561,1.073204,8.953082,-8.250684,6.162853,-4.126183,-1.082535,-7.385472,9.309222,-4.388193,6.573170,1.626509,7.043765],[-8.227948,9.890784,-2.969437,6.758011,8.781003,-7.770835,-7.223930,-2.064325,-5.882822,7.426927,-9.430757,-4.388056,8.538245,0.717752,-4.644761],[1.277360,-5.956954,0.878513,3.834944,-3.432410,-9.207343,-3.907320,4.585583,4.343846,5.214107,-9.037126,6.039797,1.192884,-2.913108,7.058614],[8.031196,9.308869,8.638241,-2.365829,-9.046546,-4.901907,-6.965202,0.816555,3.462514,0.390012,0.569351,2.716134,-6.598269,-6.049125,7.165015],[3.805482,-3.907844,-2.833723,-5.838422,-2.031433,-3.785222,9.416775,6.561458,-0.983159,4.310208,5.484748,0.069138,7.576077,5.809997,8.517559],[4.212007,0.964907,6.607898,5.249233,9.241740,-6.143042,-0.347459,-3.631915,-1.914331,9.826540,-2.823813,4.786984,5.246641,2.906294,-3.368740],[7.847114,4.826266,9.217094,2.409197,-5.749476,-9.302686,-8.409559,-7.530357,-6.881840,1.729066,-8.414459,-7.640154,5.416591,-2.255600,5.052602],[6.260161,-2.415868,3.600571,-5.639665,7.826397,0.555763,4.390300,-9.966334,-6.313269,0.114494,-3.581526,7.279805,4.935641,-8.335822,3.134297],[-4.726202,2.414865,-6.997217,-7.606018,6.781815,4.076434,4.996612,-6.127530,6.512885,-7.896137,-8.715269,-5.719814,0.580196,-7.801091,-4.106448],[0.586550,4.013511,9.554273,-7.023590,-4.390171,7.553151,-3.452900,-5.729683,2.347412,-6.804370,-9.484273,-5.074341,-1.809198,-8.063112,-2.333375]],[[8.464282,2.986092,-4.846371,-5.929959,-8.669482,-1.414496,-7.753976,-5.400891,8.652255,-0.532262,4.482948,-1.878588,-1.992837,-2.825359,9.200542],[2.779560,-9.802787,5.476510,2.633210,2.729911,-2.350860,-5.625479,9.327037,-2.378249,-4.674546,-3.405290,2.145812,8.914523,2.481317,0.999150],[-3.651273,6.637005,2.752221,4.547311,-0.615757,5.936832,-2.832218,-7.472570,-6.960442,-9.871453,0.394435,5.028247,9.192444,-9.293094,-3.310139],[-7.990144,-4.076270,8.198093,-0.162783,4.509178,-1.714795,-7.952038,-0.867743,-0.498202,4.612305,1.565751,6.421578,4.784443,5.759136,3.038463],[5.887906,8.285904,-6.052535,-1.249157,4.136294,6.084514,-3.745538,0.852074,-9.045161,7.361222,-1.208886,0.803432,9.211791,4.065294,-3.656225],[-7.635278,-7.422705,-0.278801,6.680720,7.134132,-6.155474,-2.987549,-9.866768,8.401025,4.603902,-3.822674,0.300975,1.176837,3.053149,4.720316],[0.242312,2.926018,0.663341,-8.351688,-6.579505,-9.085546,9.201512,3.526151,-2.324934,-0.354843,-7.654532,3.585530,-3.768978,-7.592608,4.570158],[-6.449865,-2.721514,-6.594700,1.509628,-8.842853,2.945067,-2.502166,3.156946,-8.860015,-0.569821,6.863425,-4.096709,-8.221348,3.270631,-6.256763],[-7.469351,4.490547,-9.474333,8.766623,6.600080,-6.021251,-5.910985,4.469848,-5.124850,3.543461,-3.664369,2.167266,5.228021,-1.930667,3.465694],[-2.817242,7.386753,-9.147294,3.058056,7.869253,5.101388,1.948321,-7.355371,7.694587,0.508957,7.957343,1.201891,-3.356632,-0.199850,9.610536],[4.049167,5.326747,1.497927,-0.453378,9.648318,8.419514,2.426351,-0.996324,4.637842,2.090759,-8.571412,9.811358,6.486390,2.882486,-6.766503]],[[3.635925,-3.699667,-9.357247,-8.667110,-6.603581,-9.541711,-4.665423,5.164176,2.290286,-7.649155,0.996690,7.939475,-5.952420,-7.867547,-5.017249],[-6.508043,-5.211743,-3.978753,5.836220,1.203597,9.571979,8.353814,-4.910856,-4.340765,-6.331820,-3.197494,-5.401806,-3.446695,-7.523507,-5.167795],[8.183119,4.804476,0.780906,-7.357857,-0.754863,-0.675894,7.321164,-0.331128,-7.819875,1.988877,3.001987,-1.071911,8.723524,1.272982,1.708129],[-2.264342,-4.149129,-4.878505,9.647377,-5.515369,1.694421,4.848597,0.082835,-8.151244,3.104932,-9.607019,2.989548,-7.883333,8.493981,-4.751203],[1.054628,7.403424,-9.315354,4.453180,-7.525724,-6.044853,-7.082030,-1.564542,2.793484,-5.169322,-4.408081,9.649350,7.998394,-5.957500,3.197127],[-0.630057,0.254142,1.160459,1.034011,7.144657,-3.077153,4.278756,-1.416182,-9.069351,-7.161690,-4.006262,0.715248,-9.046807,8.477651,9.371310],[-1.857002,8.544942,6.487833,0.173619,6.126920,-8.473988,-8.176950,-5.508615,1.717080,-0.664494,7.945398,-8.142622,1.574745,-5.333372,5.240120],[6.548905,9.919999,2.831019,8.034745,8.646780,-7.818815,1.658900,-8.266025,8.824233,-4.392004,3.900885,-6.819075,2.463750,9.995643,-7.170462],[1.778208,-6.456045,-2.374928,-1.560396,-2.654449,-7.247431,0.260236,-6.172761,4.900046,-8.339498,8.688511,-3.011600,1.145480,5.756555,2.880313],[-3.541959,-1.371450,0.892128,-9.999636,-1.531989,1.942152,7.459723,-4.625995,-0.132932,9.474452,-2.318130,1.909858,-3.065515,-6.605081,7.979605],[4.292291,-0.975086,-3.290660,-1.623772,1.646162,0.766616,2.970684,-5.999974,-2.776146,-9.672104,8.096302,0.362409,5.397536,0.118391,8.015198]]], dtype = "float64")#candidate|3576|(14, 11, 15)|const|float64
bop_3577 = relay.divide(uop_3541.astype('float32'), relay.reshape(const_3576.astype('float32'), relay.shape_of(uop_3541))) # shape=(14, 11, 15)
bop_3580 = relay.divide(uop_3543.astype('float32'), relay.reshape(const_3576.astype('float32'), relay.shape_of(uop_3543))) # shape=(14, 11, 15)
output = relay.Tuple([uop_3552,bop_3577,])
output2 = relay.Tuple([uop_3554,bop_3580,])
func_3585 = relay.Function([], output)
mod['func_3585'] = func_3585
mod = relay.transform.InferType()(mod)
output = func_3585()
func_3586 = relay.Function([], output)
mutated_mod['func_3586'] = func_3586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_3652 = relay.TupleGetItem(func_2548_call(), 2)
call_3653 = relay.TupleGetItem(func_2549_call(), 2)
func_2098_call = mod.get_global_var('func_2098')
func_2101_call = mutated_mod.get_global_var('func_2101')
const_3657 = relay.const([-6.016265,4.477010,6.119883,5.039067,9.843497,-6.869981,-4.317782,-8.475938,5.863701,4.763650,4.208776,-4.508014,-1.439871,-1.618309,2.185437,4.169081,8.670385,8.988690,8.174271,1.081467,-6.565384,2.480802,-9.632745,1.875223,-8.484540,-7.631326,3.614334,-5.373945,-8.265356,5.637746,8.594227,6.598676,6.284684,4.530233,8.459814,3.780141,9.077579,6.487201,7.694483,6.372269,5.804336,7.566835,-7.511579,5.629378,-9.074572,2.023551,5.111790,8.255634,5.468456,4.926031,9.272756,-3.871871,4.482913,8.406853,1.668331,-6.671025,-7.625017,4.629333,-9.604151,6.536115,-8.513489,-2.831602,4.904763,-2.357635,6.023704,2.869871,3.261711,4.480529,1.267698,4.055447,3.471372,-2.696574,3.428143,-4.373341,-9.794159,0.729573,-6.675497,-6.301423,6.869048,-7.584778,-0.303705,4.679252,-2.235242,-5.132053,1.591343,-4.862918,6.127305,-7.021247,-2.533690,-1.064810,-6.664160,3.664922,-1.934260,-4.992113,0.891355,-3.836444,7.501851,9.903058,-9.979031,6.956198,3.200500,-9.853482,-4.551615,9.523998,0.985491,2.579642,5.295716,2.414682,-2.492982,7.209708,-8.284649,2.186243,-5.009373,8.600575,-8.186883,-9.978531,-4.068927,1.404087,-1.943931,-3.615087,-6.103055,2.825133,-1.522556,3.204025,3.915095,-0.211380,-8.051978,2.545724,-3.788637,4.244255,4.063853,-1.480867,-6.670540,8.411457,3.642824,7.764962,9.102522,8.039738,5.370704,2.735467,-0.532597,-4.709346,0.675474,6.090222,7.973158,8.875399,-3.519216,-6.086369,7.199170,9.097405,6.117362,-6.741905,-5.611729,9.956728,4.865050,-8.633523,-9.622436,-1.932510,-1.310135,-2.224067,6.625916,-2.702867,1.177448,-6.538293,-7.253770,3.494760,-6.940777,3.819815,-7.061401,-7.598561,5.585245,2.599996,-0.560056,3.901394,3.030205,-0.627998,4.404885,-4.968965,0.762896,3.267594,5.940317,-0.524024,4.815203,-9.079895,-2.253957,5.156553,0.489952,0.548069,-5.790478,-7.458112,-8.075655,-2.456085,7.829599,0.854543,-1.668436,5.741543,9.337803,6.368305,2.566534,-8.150441,0.944385,1.434366,-1.236316,-6.653701,0.815799,-3.860020,6.908613,-5.684484,-1.496173,3.364778,-1.642511,-6.248038,-8.669308,-3.777307,8.152488,0.616036,-6.227982,0.918174,-1.785026,-7.984369,-1.645029,0.975403,5.487230,-5.414826,7.178356,-5.262874,-6.044158,-5.465849,1.076058,-7.876481,4.858681,2.539834,-4.727982,6.268001,-7.025219,7.480020,-6.662089,-8.182087,-7.978843,6.204557,-3.626369,0.154017,-2.789847,-5.603364,7.004063,-3.005433,-1.587882,-0.540297,-5.194814,4.505768,5.556435,4.890579,-7.176644,-1.738664,2.210478,-6.305113,4.079407,-5.892431,6.436951,2.742882,-9.133868,-1.462745,7.559457,1.303943,-8.641937,-8.627897,7.546245,8.125128,4.874202,-2.333972,-7.969834,7.103427,0.728458,5.652673,-4.612935,1.700808,7.963679,0.821481,-4.264535,-5.459474,-5.852648,7.778098,6.303470,5.384378,-0.151135,4.818559,-1.574979,-9.502266,-5.689732,1.030771,6.122460,4.209400,-8.439810,1.979434,-3.906292,1.465620,6.332423,-4.278406,9.817591,9.375515,-5.848291,-6.588438,4.469352,-3.155496,4.952474,-1.833027,-6.894958,8.798252,3.786421,6.014143,-7.284768,-9.054443,4.879364,-2.729848,-0.726566,-9.696408,-1.911907,9.973982,-2.243113,-9.167923,7.857040,-6.441431,-7.643738,-6.327038,-8.679582,7.670540,-1.109221,-4.888962,5.403371,9.134579,4.653803,-8.922662,-8.501229,7.425080,3.851515,-3.719525,3.503251,-7.438607,-0.084419,2.398938,-5.703973,-8.868692,-3.273850,9.930165,6.888885,9.993164,-8.362585,3.397650,3.879062,9.291704,-5.893343,-9.588503,-6.193427,4.366707,6.676183,-1.358444,-0.499628,6.066136,3.731643,-3.355884,3.331039,1.806193,6.901201,-0.243827,-7.511089,6.200393,-1.258724,-6.975553,-7.024481,5.413698,-0.040482,2.054217,-3.929086,4.984521,2.920621,3.553947,3.559323,8.278953,7.110344,7.058944,3.123554,-7.867761,-6.587241,2.977704,-1.488248,0.413285,-7.513420,0.898402,5.734469,-9.042199,-2.351615,5.313316,6.628509,-4.993375,-7.513914,-7.382758,-3.507350,1.489853,2.369141,5.324635,-0.287381,-3.507006,-3.295450,5.322204,-9.264326,-9.950796,5.353708,-7.506759,-4.693072,9.754609,-5.419431,1.693443,-7.391451,-4.899043,9.403904,-9.019222,-5.000778,-9.581427,-3.082195,-1.533099,9.324832,-0.959867,-5.853917,9.858066,3.337231,3.096710,-4.668986,3.969116,-2.522558,-0.595674,5.022351,1.938426,6.337655,-0.668073,8.137633,-1.676595,-7.373920,-3.802727,2.199927,7.533619,-9.862631,1.661931,2.668250,-4.558290,-6.616744,7.217760,6.639556,7.699942,-4.339884,-9.968036,-3.493504,8.971676,5.805501,6.920704,0.169568,-4.722430,4.407469,2.969746,-2.370753,-8.801739,-0.260685,-6.207750,-6.105279,6.553684,-8.419410,6.476116,-0.316204,7.362614,-6.345215,6.114372,5.825196,1.317641,4.847472,-8.638844,-7.996190,-1.342284,-5.725513,-4.903449,-6.728881,-1.039473,-2.690166,6.463226,-3.546999,-2.905454,5.111482,-0.652007,1.868770,5.579027,-6.176724,-9.857169,9.572414,-9.918731,-8.619885,-6.419156,-6.992141,9.920341,-9.911938,1.374166,0.787671,5.108147,7.072133,2.185569,-6.512557,8.265391,-3.845233,9.960916,-9.959910,-7.630062,0.301612,0.916624,5.848827,-4.811507,9.289784,-6.484347,7.510176,4.818993,2.177483,-3.312676,-1.972912,2.928598,5.726517,-6.525704,-1.566267,-3.211140,5.567500,0.115005,-7.170098,6.191969,8.408473,-3.243072,2.544370,-7.043153,3.721769,-2.637342,-4.207253,-7.423336,2.049114,-5.195601,1.884333,6.345534,-0.226852,8.503736,-5.601861,1.007954,-0.880992,-9.406984,0.523079,7.912786,8.592233,-0.887350,4.507541,-9.210556,3.983048,-9.713783,0.699438,-7.729031,-1.472947,7.037285,-6.901439,-8.284217,-5.645330,-0.895949,4.460198,-3.458767,-7.430379,0.870339,-2.047585,-1.451994,-8.623404,-1.555272,-2.633243,7.152845,7.778764,0.178797,8.938276,-5.624024,-3.972310,-0.900938,-8.084296,6.654163,8.593655,-4.304868,-4.121313,-0.902502,9.579960,-2.828180,8.386241,-2.271561,-9.323932,-8.522652,-2.398873,-7.083437,0.437508,-8.576140,7.097271,-4.100871,-7.502956,-7.275977,2.915784,0.429520,-2.403214,-1.187418,-7.142858,-8.537056,-9.821719,-4.997228,3.786251,-3.431734,9.874160,0.298168,-2.215042,-2.941815,-3.723019,5.184831,8.184850,9.037250,-6.989106,7.659083,-7.355801,-6.494832,-2.139826,9.639404,4.319009,-4.623411,6.504904,5.905224,-0.314023,-7.484315,8.895009,-6.507591,0.504515,-6.466803,-6.864062,-6.738191,8.821046,7.761932,3.316941,3.930031,-2.296569,-2.378418,5.576190,5.346604,7.665924,3.520793,4.718254,2.372827,8.705716,6.952541,2.032642,-3.627573,-6.098120,-0.587762,0.723180,-1.456468,6.600284,4.531078,-8.002326,-3.963060,-9.781447,-0.992308,-7.731574,-7.764426,1.286889,3.424981,2.137332,0.348368,9.716463,-4.197032,-4.539546,7.354882,4.454036,-8.985730,9.180891,6.020033,-7.871906,-0.037962,2.126189,-0.448066,-3.404174,5.350286,-1.519779,3.978645,-0.183038,-9.195339,-1.158275,-0.165370,-7.174244,6.784352,-2.209560,2.472157,7.993388,4.226517,7.442879,8.181584,2.457638,4.229700,-7.159768,1.040333,-6.974101,6.720604,9.617962,-9.888410,-4.487035,-3.495835,-8.216698,-8.920099,2.375919,-1.684751,3.747196,-2.176319,-3.508833,-3.238535,-1.717556,6.517068,9.747576,4.735237,4.030103,-4.014317,5.758040,-6.531234,4.536299,9.756021,-0.891814,4.814722,-1.426594,-2.820847,1.472533,8.172177,-1.876409,0.680649,5.444836,0.045199,-8.977783,-1.939648,-0.967172,-3.281088,4.046858,-6.525955,6.014365,-9.236938,3.359021,7.708937,1.532878,-6.411909,7.768077,-5.191795,-7.087468,7.757740,3.288875,-2.754663,-4.608283,3.005766,8.914429,2.703227,7.775593,-4.056488,-9.560134,-6.443905,-1.872158,-8.013469,-9.138676,-5.066137,-3.607373,7.422121,2.514003,0.968872,-8.295465,-3.234106,-1.801987,7.624970,8.138381,-0.742525,0.047903,9.997531,2.313651,2.985178,-1.491912,-7.670238,-4.796262,5.355026,6.089818,7.817144,8.609769,9.835420,-6.566775,-0.380725,-3.611573,9.696073,2.090168,0.876632,-5.394257,-1.288579,-8.600880,2.386010,-0.772789,1.271700,6.441724,-6.581127,-6.239962,-6.498203,-3.532527,-6.494370,3.221734,-7.483161,-2.605319,7.994263,-5.737991,-1.513279,-4.360405,1.244549,-1.623283,9.825280,-7.743239,-9.223151,4.666542,5.582016,3.417658,4.183989,0.730234,2.363495,0.096496,7.699959,-0.289129,5.757281,1.376546,-7.624975,1.722934,-0.281051,0.496860,-8.608744,5.720322,-6.949945,4.579811,-6.860119,6.456517,-4.183158,-0.404050,-9.487404,3.570168,-2.819841,8.622016,-0.918995,-6.900422,-4.370670,-3.745868,-5.384594,-5.286680,-0.775391,-8.284905,-3.529797,5.935504,4.275291,-2.525463,-6.395281,1.398607,3.948354,3.265653,6.351505,-9.433778,2.268085,-7.017729,-8.935481,-0.513135,-3.408721,2.961982,-5.239228,8.085520,7.433959,-3.989413,-3.150398,-0.149859,-7.134540,8.753821,9.085175,1.743872,-7.244475,-2.117784,-2.963904,-1.495570,-7.993676,3.367581,-4.546260,-8.014583,0.658543,7.951812,-0.131743,4.698879,-7.309984,-2.188809,-0.383504,-3.978777,5.840974,7.996700,-9.329141,-8.718376,-6.801086,8.670492,-1.146318,-9.456667,-8.612283,6.227537,5.642436,5.584611,-5.291406,6.501281,7.068503,6.983615,-0.604616,-2.963144,-9.486379,2.518964,6.774464,6.541854,-3.193575,3.571100,-4.259143,9.372927,4.056867,4.123903,-9.658516,-7.406269,-4.417613,-3.001927,-5.673782,7.698047,9.101510,9.217350,-0.851985,6.757017,-0.127507,5.727123,0.233646,-9.116350,-1.578092,-4.691398,-4.677142,-4.273935,4.538941,-8.620803,-7.706219,-0.943056,-6.345587,-9.763518,9.754696,-8.621488,-2.976734,-7.990489,-1.992238,-1.676754,-9.929786,-2.061975,1.527750,9.676227,1.674200,-5.824703,-2.257107,-7.802402,6.018122,5.932753,-2.058909,-3.159685,1.406079,-2.675150,-7.001308,-0.863708,-5.973295,9.630274,-0.260103,-6.217732,-7.038439,5.975816,6.701671,-1.139812,-3.496824,7.491915,3.982693,0.660252,-9.470529,-4.404482,-0.638852,3.129768,0.978852,-1.385228,-7.061313,-6.822106,7.854124,0.776107,0.068191,5.855820,4.269435,-5.418204,5.314779,9.003428,7.597161,-4.179960,8.659888,-3.612659,-1.631123,-2.447959,3.284912,-7.725699,-7.388929,-8.900699,9.411675,8.345380,-4.559233,3.670626,8.500305,-4.419765,-1.140734,-1.974233,-1.320891,7.800260,9.652276,3.365861,-9.373053,9.880175,6.820795,-6.701934,-5.941571,1.034633,8.837756,-1.855951,-9.118644,9.159729,1.449523,-8.545105,6.954644,-1.149924,2.967890,4.941725,0.290937,-2.896206,-8.610635,3.785839,-2.229495,-0.334266,7.782974,-5.358836,9.888162,6.407149,6.395838,-4.600125,9.245428,4.642917,4.375994,-2.046572,5.442015,3.759993,1.568769,-4.823524,-0.880166,6.166473,6.462477,4.305501,6.904384,2.475709,-7.542181,5.954748,5.922170,-5.878612,-9.805218,6.006959,4.647400,8.352938,-6.045924,-3.611925,-2.122314,-2.338608,4.981522,-9.340713,-1.895222,1.637077,-7.715139,-4.224722,5.033513,-7.941955,6.245960,1.658497,-7.885715,1.349167,1.041823,7.020778,6.158835,3.111698,3.203737,-1.715965,-2.532381,-4.417716,-6.155914,-9.674388,1.271867,9.164846,-2.240458,0.771581,-8.226947,9.814270,-3.388971,0.327775,6.733968,-6.970907,1.537047,-6.377903,-8.708359,-7.265919,-4.483807,-1.936374,9.598167,-2.939290,1.805999,-0.127104,6.629256,7.547906,6.884884,4.824944,5.530531,0.942195,-9.658804,-0.619033,0.549896,-0.275594,4.859628,4.153781,-4.763441,9.027997,-2.403288,7.612122,5.364229,5.685438,-8.822401,4.005702,1.417954,-8.198458,2.441851,-3.709612,1.696360,-1.605198,-4.191167,9.493035,7.282697,-6.218098,-3.247399,6.127666,-7.804653,-2.890600,-8.378882,-4.272972,2.792431,9.594618,-7.076534,6.835096,-7.325129,-0.346326,4.302084,-1.705492,-6.696203,-3.839507,-7.658846,6.025011,7.269643,7.939651,1.896948,9.545633,-8.445220,5.099194,-3.911955,-4.864775,-5.687252,9.355005,-4.856462,8.386060,-2.043411,-1.475447,6.644282,7.751849,2.481439,-3.984929,8.270090,2.750913,4.304270,-2.422007,9.508986,-1.212519,9.384163,-7.043084,4.099178,9.737328,6.397765,2.167067,0.559629,2.533862,0.384671,3.005029,0.589918,0.645199,-5.901481,9.212766,-1.187512,2.619427,4.848962,-3.201575,0.709644,7.785556,6.685953,-0.242803,1.669409,8.628043,1.031640,2.949318,-9.005187,9.534906,-2.415083,-1.374118,4.756942,5.211731,5.081253,5.658992,9.176015,-1.149104,5.243396,4.718434,-6.403929,-0.939870,7.226610,5.721572,-5.855865,-1.293301,7.378682,4.551590,5.008523,1.007871,-0.981197,1.829330,2.865544,-7.065613,-8.437137,-3.517914,2.614527,9.824541,-9.070694,-0.794062,6.081409,-7.393650,5.765145,8.146816,-7.041652,-3.065746,-1.260777,-0.394571,1.203449,-9.571238,-0.589700,-5.162621,9.088837,-5.075555,-7.011212,-0.211160,-1.061712,-0.266728,3.511733,-0.343273,4.383896,-0.818621,-8.108507,6.287057,-0.667757,-2.218533,-0.655267,-4.922423,-3.259339,-1.881035,2.461574,-0.948704,8.099940,1.456293,9.921465,-0.829285,-9.795339,-8.581105,4.005281,-9.010875,9.425983,-4.435726,-1.597843,-7.654760,8.461639,8.728901,9.078612,-8.811436,4.104912,8.591851,7.358784,2.921197,3.549103,5.447623,1.300889,-0.274437,-0.213502,7.619629,5.879600,4.288854,-2.416583,3.941425,-0.864763,-2.749558,1.628842,-7.143518,4.302611,8.018039,7.046496,2.225333,-0.943279,-6.416277,-9.031146,0.764276,3.420898,-5.435768,-4.765246,6.845974,-7.750554,-2.893956,-5.941331,-7.142446,-1.918292,-2.502002,-4.381606,-1.209267,2.422532,0.835895,-8.604346,0.194828,1.067897,3.005241,7.941732,4.363152,-8.487458,7.984602,-0.727217,-7.961706,4.745386,9.888591,-0.795940,7.958308,-6.081132,2.922209,6.024996,-1.654667,2.363073,-4.201919,-0.034512,-9.010456,7.409744,8.336474,9.477496,-7.289690,-7.026986,5.819043,-4.896847,-0.813488,5.565868,5.489091,-5.180847,-7.681369,-3.765780,-5.569931,-6.302527,2.472269,5.907541,0.524839,7.428444,4.770639,3.260864,-3.228765,3.682060,-5.264179,0.829963,-5.514676,4.851636,5.701652,7.281391,0.049307,-6.104882,-8.975604,4.850657,-8.081319,6.964188,3.085575,-9.065384,-6.471519,-3.735329,2.622977,8.267422,-9.772873,-5.063064,-4.391526,6.840449,0.007403,-6.301624,6.354655,5.185823,-0.091239,-2.563964,-7.005058,-9.548354,-5.116136,6.806198,-9.942474,2.367460,-6.100297,-2.413409,-4.266842,-8.010168,0.889552,4.912173,-6.182705,-0.011258,9.900829,-5.496056,-4.874929,9.901268,-5.240307,-0.992164,0.951783,4.175606,7.747259,-3.378593,5.838133,2.105467,9.891185,-8.040870,0.672625,4.094087,3.421141,-2.983170,-1.032662,-5.865987,2.682718,5.639286,0.120868,-3.600360,-4.308447,-7.889726,9.711945,-2.047739,-5.971017,-7.266222,9.068488,-9.465757,-4.279231,-1.581804,-8.159310,2.717792,5.601989,-5.338210,9.892205,2.719409,5.579267,9.332646,1.689094,-6.609550,-8.039746,-7.948177,-5.494551,-7.041666,0.450145,5.850017,-0.109426,3.827515,7.236617,-3.461439,-7.508207,-6.978674,6.689470,-8.676132,0.287466,-7.681806,-2.647831,9.471524,1.123513,5.199841,4.712859,0.483378,1.182469,5.369978,-1.328590,6.188178,-3.222117,5.813972,7.416430,-9.618620,-2.433899,1.514963,8.866562,0.602612,-8.757714,-5.006649,8.932638,9.036073,-4.990496,1.283025,-1.295559,-8.404932,-9.474180,-4.954628,6.381430,-7.052877,8.655497,-0.096605,-2.094452,-9.958482,-4.348929,-3.936200,-2.726160,-0.634968,2.286055,4.613684,-2.259279,-5.140497,1.008670,6.387158,0.728070,-8.247231,5.150571,-8.323470,-7.678926,-4.234527,5.269147,-7.331021,0.664254,-6.813163,-1.716197,-5.151174,2.361283,9.613193,-1.771921,-3.010686,-8.062616,-8.894954,7.738306,-9.698058,3.213027,3.620451,5.626211,-3.771345,-4.532538,9.036703,6.248760,-7.007856,-6.941018,5.650822,-4.326359,1.981403,2.677618,-2.716414,-1.529609,-9.745240,9.388920,-6.677926,-6.702347,7.497221,4.603530,3.162227,3.532678,-2.466460,-6.582518,-6.631877,3.036667,3.707838,2.769456,6.896583,-6.250624,-3.720298,8.207977,5.348764,8.255552,1.368988,6.515370,7.884575,-6.660404,2.746863,-6.164765,5.817121,8.226533,-8.358941,-7.832996,-7.066236,6.490765,-9.331174,8.670896,-0.924660,4.498484,4.854782,5.936595,4.674872,-8.786348,-4.198682,-7.361700,-5.338542,-5.510842,-6.866514,6.553129,-9.525157,6.947897,0.963400,-8.147921,-1.210536,4.577648,-4.950607,-8.000424,-7.619192,-3.663085,5.261893,-1.247655,-6.022694,-8.361863,1.941980,4.896451,2.942137,8.911488,8.851689,-5.649480,9.597626,-5.443041,-8.858377,2.755263,5.350880,8.617857,-4.941962,0.161768,9.504616,6.479553,1.621210,-1.609038,-5.875137,4.869526,1.633773,0.144077,-2.892503,-1.705425,-0.883304,6.879565,-6.976434,1.344164,7.899632,5.026962,-3.388856,2.017338,-0.181521,-4.175292,8.326489,-4.288564,-2.039773,5.151135,7.891048,2.715818,2.587752,-3.540621,-6.288895,-8.517590,-6.375084,-7.056910,8.894333,-3.268723,0.336105,-1.290154,-7.947141,0.278055,-2.005466,6.717332,-4.677495,9.327816,-8.491598,3.864051,7.228796,-6.408043,-9.245674,3.103929,-8.321561,1.438499,-1.216094,6.606487,-3.850382,0.515247,3.294457,7.659661,-9.728216,-5.213896,-7.761585,5.328253,5.519942,9.992490,-8.243937,0.058821,-4.138253,-3.933268,-0.978190,2.165286,-9.274609,6.009547,-9.286943,9.785914,-4.815703,1.998495,-3.511574,-1.534266,-0.106748,9.821022,-4.327443,8.817313,4.609523,-6.287033,2.189599,-3.255547,-3.171227,-5.083833,-0.354208,4.427108,0.173465,5.873009,7.194619,2.579627,6.824559,-5.104903,-0.717844,-4.261780,8.716450,6.897960,0.090160,-9.087568,-1.515116,-6.839221,0.079217,9.632611,-6.629484,-6.540437,-6.538036,1.553696,-5.925704,-1.102310,7.589807,-7.144910,4.941197,-0.509379,3.184630,-6.014450,2.439940,0.673732,7.969060,8.851936,7.614153,7.521963,6.032087,-8.857502,7.271618,-9.661885,4.049286,1.082877,8.882121,3.809741,1.352602,-3.872115,-9.474724,6.413437,-7.348136,4.668474,-8.745518,1.499131,8.901017,8.030716,-3.112422,-6.446931,-6.719606,-6.670055,3.869018,-9.558761,-4.200413,9.396106,-0.161043,-0.874947,7.251934,6.437749,-3.415573,0.829452,-7.174836,-3.590191,7.039303,-3.793559,3.442461,2.856745,8.071708,4.308389,-8.288698,-8.683961,0.950151,2.254126,5.839742,-1.621173,2.104639,1.801878,-5.524837,8.329664,-1.790604,4.083662,-3.080435,-2.978981,-1.406876,1.744010,-1.842751,-2.203386,-0.713677,-3.196336,-8.642969,-9.998228,0.267631,8.357063,8.382303,7.038720,-4.042607,6.289847,9.063185,-4.347751,4.910602,-5.518386,-2.855420,3.560833,-1.095890,-5.271417,-7.330740,-6.363031,-6.183937,6.221506,-0.719055,-4.632242,8.821128,-6.384032,1.700077,1.159649,-8.477234,0.804634,-9.923873,-7.497074,-5.441304,7.856750,5.779357,-3.525053,9.784791,8.245223,-7.400374,-2.152814,-9.582951,-9.022476,-3.629913,-4.058328,2.838573,4.158226,3.155627,-8.040847,-6.729694,-0.977948,-8.030917,8.984651,5.713909,3.754427,-9.681969,6.799435,-0.147759,1.367676,2.135218,-7.846287,3.700362,-3.480611,1.332227,-8.607566,-5.690401,7.481077,-4.640942,-2.186549,6.492470,2.005897,-4.721427,-7.854824,6.664721,8.574694,-5.087095,4.708091,0.017202,-8.199413,4.589937,-3.594560,9.205151,-6.267100,-3.012624,3.521308,-2.142861,-8.005050,-6.562585,-2.856392,-9.638582,-2.781474,5.752956,-1.029658,-2.964345,8.134207,1.878917,3.508968,6.962484,-3.411198,5.230205,2.026808,5.443860,-2.854505,6.944437,4.712944,-1.637573,-7.631041,9.908431,-7.814893,5.273842,2.230550,9.602523,6.637428,-1.239267,-0.322232,-6.459092,-8.738066,5.248235,4.841782,6.702880,-2.202612,-6.909474,1.882625,4.986917,0.893845,1.732328,-4.317815,-4.792638,0.485594,9.551394,-0.330378,6.712201,1.094612,1.027912,3.675355,4.416794,-6.961169,-0.647762,-1.849759,3.803001,-2.173395,-4.704084,3.893792,3.382398,-0.441990,-8.969948,-1.298548,9.204299,0.950922,-0.393262,1.643832,-7.989787,6.994833,7.258017,5.966570,-0.429574,7.267916,-1.007086,5.183750,3.667422,-5.967715,-7.888417,6.402706,3.498970,-4.226072,-3.315172,9.791850,0.982244,2.781625,-0.055566,8.920924,4.852632,-7.659609,9.676408,7.955932,7.935343,-6.171469,-3.776563,7.710330,-6.002246,3.113033,5.100639,-3.651601,7.103382,9.175202,-3.341257,-2.363004,2.807555,5.727379,-0.592855,2.489667,-6.110132,1.500555,2.390349,-6.687048,-8.670018,-7.056096,2.895522,-3.141380,0.934135,-8.198276,-2.840568,2.090952,6.323240,-8.094274,5.046758,3.899235,-0.250335,-7.830766,6.031671,8.997856,-8.351572,0.457071,-6.357808,-1.614455,4.794682,2.539649,-8.012877,3.439350,3.996633,9.275441,0.787805,5.425986,-1.580833,-8.321481,-2.517839,7.161411,5.190787,-7.455585,6.522649,6.335434,-4.642075,-2.178355,1.822637,-6.502972,-5.914019,8.190109,6.137652,7.674389,-8.152155,7.349539,1.847254,9.692298,-8.795160,8.869775,6.878227,-0.167732,3.411782,-2.391655,9.626689,-0.688912,-5.179752,2.274525,-3.969361,4.224929,-6.249233,5.581652,-5.483273,1.508929,3.311858,-9.732088,3.659022,-7.270430,9.230679,-7.154435,1.984356,-2.400609,-1.855595,8.897538,-4.587907,-1.386600,-9.308628,9.999002,-8.522111,3.525524,3.453620,-9.889898,-9.538183,5.736242,4.012748,-0.069555,-9.990966,1.528307,4.491909,1.094459,0.587055,-9.960921,-2.979766,-9.056772,-9.959207,-0.216745,9.837764,0.485464,4.494961,-8.306209,-8.014567,8.784419,4.446649,7.740665,-3.163634,6.007235,-8.395882,3.269004,0.045268,-5.010476,4.338625,3.280658,6.325624,-1.105222,5.698902,-7.210470,-0.102627,7.001868,-7.923630,-3.457710,8.081041,-1.708054,2.163973,-6.013600,-1.910505,2.675844,7.979130,-8.662294,7.002801,3.906641,4.614950,-3.139749,-1.706322,-4.390074,-0.155883,8.610718,-1.165197,-7.389473,9.558355,-5.741507,2.018736,9.511633,-5.935725,9.601039,-4.668389,-4.006314,-2.585198,3.197818,-1.835675,4.976525,-0.926371,7.115857,8.200088,8.574107,-3.625265,-8.118000,1.929618,4.082137,6.508225,9.831221,9.300960,-9.532123,-8.687481,-8.250367,8.520807,9.238350,-7.949313,-0.008295,-0.388635,-6.044833,9.758466,-2.399452,-6.556738,-4.647961,2.174393,-9.948671,2.172338,-4.143820,-3.862167,6.581467,8.966060,-7.029239,1.288621,5.036647,-8.616579,-2.414052,-5.292709,-8.945698,-0.399762,-7.032616,-7.497831,3.040354,0.331448,1.086107,-8.974473,9.884388,7.162469,-4.029976,-5.034122,4.728286,5.474785,-7.665306,-7.266360,5.340484,3.508446,-9.174454,-1.662410,-5.346444,-4.419643,9.480496,-5.944930,-2.345635,-9.531482,-3.453679,-7.948377,0.517082,4.245523,8.621650,-6.791707,0.157238,-3.457367,7.714096,3.794877,7.060138,8.969078,-5.187558,0.074223,-6.101121,0.126056,6.510172,-5.912104,-9.533275,-6.294579,5.867147,-1.004638,0.099090,7.008523,1.641203,-4.232395,-6.968477,6.522676,0.003246,2.981442,8.699148,-7.119082,-3.863302,4.436356,-6.622469,-9.634842,1.010768,-3.960158,1.098440,4.305104,-0.669572,8.234588,-7.888145,-0.806359,-8.009876,9.543015,-7.947159,-0.584291,-5.130779,4.513239,3.760154,-3.834574,-0.152764,3.796168,-6.625593,-9.357878,-0.487696,8.436259,8.971574,-9.804687,8.823248,1.201096,3.223107,-3.134029,9.445104,3.326578,2.852461,6.459332,-6.433603,-2.253201,-2.953474,-7.633712,-0.876008,6.498394,5.780760,3.491443,2.706808,-4.470979,-4.422974,-6.392383,9.811421,6.987924,4.294600,-9.698118,8.459040,4.316993,-0.810438,1.904304,3.244948,-8.005427,-8.829080,-5.882675,-6.639101,2.390952,6.523130,-8.989178,6.761836,-2.106959,8.318902,-8.385261,8.898864,-5.302796,9.665690,-9.308187,-9.195883,9.636713,8.628614,-4.822373,4.713767,-2.523787,2.304627,5.960060,-8.808269,6.885823,-9.991766,6.874929,0.547707,8.125074,2.573584,-7.266580,-1.605974,-4.303499,4.213766,4.655087,-3.849421,6.235339,8.748781,-8.538210,-1.669395,5.678202,-0.926125,-5.828981,-9.588114,-0.726464,-2.822156,1.561868,4.146165,-6.499563,-9.589320,7.830349,8.683904,-5.116125,7.505399,5.501252,-9.663397,-1.085816,9.305023,7.631863,5.390720,4.700251,-9.434271,-4.664090,-2.109613,-6.958951,2.347558,-9.020853,-4.167451,1.803055,2.727005,-6.690026,4.708322,-3.710765,3.261902,-1.658639,-9.413022,-2.639681,-3.802954,-2.190770,2.125682,3.393930,-4.361252,-8.776535,-3.006627,-7.360642,-5.043274,8.771643,4.088588,-1.916627,7.510721,6.568957,-4.023259,-8.673268,0.698956,5.662786,1.632805,3.079339,-2.119727,4.056721,3.578768,8.147734,-7.811135,4.967510,-3.859756,-4.071939,-0.550726,4.454034,-3.770229,8.093425,-9.420759,-9.747365,9.204962,6.700991,1.963875,-2.260299,-5.004716,-5.052095,-2.946591,2.536695,2.631579,7.978863,5.984812,-8.853653,-2.363619,1.873134,6.804759,7.175088,9.635644,-7.503419,0.545147,9.308371,-9.197483,-7.574685,4.751443,-3.109216,4.796504,-4.350592,-5.859562,-5.852777,-9.803241,-2.094890,-0.859540,-4.610951,-3.664782,-2.496488,6.915649,-8.128643,-0.954488,9.973088,-0.319482,-7.697801,9.236769,-4.273337,-9.229488,-7.854489,7.847999,-4.672533,-6.366038,3.180904,3.223519,-9.443073,-4.748545,9.393402,0.313798,-2.524088,-0.703121,-8.546999,-0.981188,9.800541,2.197411,1.422241,-5.997324,-8.620735,9.450051,-4.081490,-1.563862,2.079874,3.333976,2.522529,1.656403,-9.824764,-3.115872,7.645021,7.326075,2.759148,3.263172,4.864743,-3.582681,-0.266502,-0.062297,8.747099,-7.230082,0.242638,3.440975,-3.200538,-5.655420,-0.968858,5.572720,0.383264,-2.094911,-8.977665,-0.863545,-3.491008,6.946469,-5.781330,0.111815,-6.073875,-9.328856,8.815032,-2.674223,0.892468,-7.328585,-8.616283,0.716316,-1.749967,-8.681132,7.662557,6.156898,-9.752048,5.983741,-2.469433,-9.105453,-1.723509,-1.558876,-4.062632,9.761890,6.373634,7.280291,-0.597690,-5.381379,-1.653446,1.825224,0.207526,9.325477,4.504140,-0.115948,2.062612,7.522525,0.889610,6.342253,-5.763722,9.492345,-5.631174,0.868839,-0.190115,-1.589325,9.462456,-8.404717,-2.006272,-8.740177,-1.344834,6.834004,7.743480,4.698065,-3.051551,-1.647297,-7.317077,-5.991701,-6.475042,8.706669,6.835367,6.731604,5.173714,0.961689,-7.646302,0.321474,-5.078430,-6.379236,2.243353,7.684603,5.568081,9.539768,2.874007,-5.794941,3.041198,-6.557389,1.342976,2.579235,-6.778370,-3.002629,-8.561458,6.394679,-1.411591,-9.439279,-0.201846,2.403181,3.219045,0.820450,4.107012,-1.921969,7.681576,0.702619,1.653514,1.884693,-6.833833,-2.538322,5.120446,8.054195,7.928087,-4.320191,5.090645,7.092706,-3.135044,-0.661803,7.193690,-1.772431,2.387437,9.138905,6.518514,-1.377479,6.099967,-3.513955,2.692998,-1.418072,-8.590217,-5.984561,5.947613,-6.447603,-5.596699,2.433890,-8.995829,-1.215073,1.722476,-2.660897,-9.257301,-1.684414,8.832482,-4.160863,8.742823,8.285375,4.932315,4.214127,-7.280862,-7.503590,-2.354839,-3.405562,-5.430208,7.780042,-6.837548,-5.430138,-0.501250,-7.742384,1.915422,-4.228205,-2.788056,-6.408357,4.462767,-1.554734,-8.154550,-6.016248,-3.195653,0.280621,0.659746,-2.646504,-8.646747,-6.946351,-2.915803,-7.172796,-3.219546,-5.232018,-5.972491,-3.602223,-8.933442,7.270363,-6.332903,-6.881755,-9.725156,6.813384,-8.051957,-0.003912,-5.500545,9.064136,1.803689,-9.823958,1.250000,-5.216253,-1.276294,9.047661,3.715122,4.089609,6.360442,-6.902850,1.973861,0.881675,-7.843105,-7.403324,5.504482,1.853764,3.090797,-3.639473,-2.033372,-5.515400,4.726427,2.578782,0.743047,-5.103122,-8.413138,-1.829607,-6.558129,0.455762,0.760502,0.622142,-2.502513,-9.053375,1.512852,-3.883198,5.120507,-5.196631,-5.096583,-2.622016,-0.615435,-0.592543,4.686406,-8.366370,8.727698,-7.117631,8.892268,4.441824,-5.541269,4.745238,-0.002695,8.342873,-7.234385,-1.713547,-4.329634,-7.797365,-9.291263,9.007522,-8.975971,8.388628,-9.191696,-7.604441,-1.885390,4.284749,0.930482,-5.393187,-1.276803,-3.475380,6.371197,0.010047,9.047972,-7.884137,8.973002,7.992528,7.918979,4.298398,9.105917,4.680584,7.818019,-7.000974,6.881117,-9.353894,8.936154,-9.355218,1.807347,-1.400787,-3.798482,-1.154067,-8.381732,0.954041,1.337297,6.661090,-5.541757,-8.291311,6.715354,2.464727,4.783323,-5.806639,-6.027287,4.793281,4.677260,-9.621692,-1.444356,3.763904,-8.402984,-6.984462,4.949646,-4.463547,-2.125999,0.222444,-3.476480,-7.686650,-6.196697,-1.762830,6.096846,-4.596074,8.085314,-2.403179,-2.028294,-5.423030,-6.685857,-6.224588,0.993111,-3.546754,1.104283,4.252635,-8.894617,2.346864,1.947057,3.372235,9.838029,7.730085,-9.647302,-5.702642,9.868539,1.541565,0.435088,4.080761,7.546053,-4.395619,1.992646,-0.986354,1.207736,-1.916433,9.847201,1.009881,2.151760,3.224824,6.719639,-6.767468,-3.213297,-1.956197,8.106030,-3.612559,8.228121,9.094064,9.464284,-3.702895,1.562615,0.065301,-5.457118,8.851817,7.576559,1.039841,-1.259985,6.338807,-3.344364,-3.096417,2.191937,-4.047835,3.535823,4.996483,2.198201,0.356571,-9.283888,1.890229,-8.717546,-7.324738,3.414145,-5.143502,-9.436761,-6.598313,6.814272,-4.880121,-6.714986,-6.196641,1.150421,-7.305125,0.124319,6.167474,-4.007529,3.954122,-6.878188,-7.036071,6.331846,0.571355,-9.508042,-2.626265,6.227399,-0.648024,3.494562,9.953000,-6.935245,0.610949,-6.965516,6.178086,2.350990,9.516472,-4.697144,8.596779,-3.315336,3.025593,5.888895,-0.549645,7.987901,-9.486318,9.182127,6.977284,4.137601,-2.667519,1.496850,-5.439536,-3.884787,-4.604373,5.838774,-9.881629,9.681289,-8.669528,-1.418952,3.639095,1.590994,-2.734247,8.294237,-8.210748,0.799026,-9.932295,-9.784152,0.649135,-8.042889,1.362249,-0.951419,7.428006,-4.391807,-8.508558,9.462378,-7.484859,3.586454,7.049526,-3.926481,8.765063,-2.229421,-3.986310,-7.571702,9.511417,-8.292575,-5.154078,0.337254,-6.986176,6.308922,-2.371313,-8.707084,9.740606,3.545510,-8.633618,-7.164578,0.160985,-2.713512,2.855893,-8.858662,2.335377,1.355253,1.510616,-5.305211,-0.041859,-3.433302,-7.357111,1.974777,-5.149202,-5.376690,-8.635617,-7.082863,-5.404789,-7.374619,5.496637,-7.557521,9.026601,-6.734080,-1.760727,-6.473796,-2.361881,5.569153,6.072235,-9.025779,-7.012363,-8.711446,4.502193,-9.531611,4.556636,0.478584,0.478560,-8.104725,4.974582,6.239092,6.841483,7.096623,-0.774651,-2.027709,9.330742,4.905470,6.821426,4.896644,-5.675712,-5.243863,-5.734999,-7.295337,-0.145264,-0.537262,0.663314,0.887386,8.701433,-4.238486,-9.532967,7.762879,1.037125,7.351496,-0.696660,9.559935,-6.768812,3.571813,0.498344,9.052902,-1.350953,-8.673660,6.238444,-7.129803,-1.884285,3.129825,4.093947,-5.191176,7.289016,5.209789,-4.122078,3.266493,6.425563,4.238155,-7.123067,-0.303259,-0.021082,0.452773,-1.916234,-8.103603,-0.171873,1.543013,-7.863320,4.869566,1.835525,-8.936880,1.962287,5.977444,-0.939599,-5.347911,0.040272,3.114139,8.860216,4.344106,-2.283616,-3.545645,2.641554,-7.578401,9.198919,-3.587729,-1.385393,9.902569,-9.461808,-8.450408,7.663650,8.749280,1.755455,5.002951,4.543710,5.991439,-7.729592,2.512295,4.003380,-9.264885,5.404402,-4.274478,5.557289,0.507048,-3.695250,-4.198440,-4.279062,-9.047232,-8.000384,-5.389572,-4.255217,7.254060,1.778126,7.421109,-0.730879,-9.225310,-7.206816,4.354769,-4.642343,3.503149,0.420042,-6.997852,9.812132,0.758118,-1.879967,-0.703589,1.727092,-3.253905,-7.622429,-4.686513,5.826057,-0.495370,6.251836,8.741746,-5.486469,-1.192082,-1.705236,-9.607621,7.692797,8.554191,3.296402,-5.490836,2.910623,-7.331249,-1.339294,-7.600277,5.680588,4.568179,-5.866679,-0.693136,8.175153,-0.619865,8.525717,-5.163945,6.104984,5.834753,9.930133,2.613766,-7.562219,-6.381274,-6.624536,-5.371852,0.041108,-0.760292,-6.365537,-2.959384,5.353459,0.419888,8.978341,3.092969,6.598507,-2.031366,4.823124,7.865795,9.993572,-6.431531,-6.020178,8.107326,2.131083,2.570360,-5.653102,6.395438,0.403897,-6.487431,-1.451768,8.787846,-5.761924,-0.406128,1.196668,5.467693,4.510007,1.300045,-4.772342,4.647009,-0.014043,2.961243,1.580150,8.075449,4.429530,3.982496,8.459543,4.657287,-2.835888,3.379557,3.825521,-2.272101,3.202862,-0.588533,-1.847970,1.323193,4.031105,7.385218,9.832004,9.815711,6.435150,5.503362,9.556876,-9.746887,-0.014631,2.489343,3.362076,1.269661,9.587239,-8.989933,1.674181,9.020260,1.177906,0.887900,8.894078,8.495366,-9.320209,5.581715,-7.022841,7.219426,-1.631899,-3.326352,6.583053,-8.247946,-0.313608,-1.842269,-4.192670,-3.842253,1.285628,-1.061485,-3.716835,2.951287,-2.171195,-1.419336,-4.770929,-0.470868,-4.436238,-2.058359,-2.870987,7.543430,-4.103899,-5.567753,7.268521,-8.757568,5.043689,1.388346,-0.546406,-3.629335,3.978579,2.613553,-7.477867,-1.743266,5.975529,-0.851861,0.671337,-6.732041,-7.957859,-6.960321,8.666392,-4.499744,-8.086776,-9.413650,-8.643441,7.419569,3.963861,4.000045,-0.145481,-1.278016,1.857279,6.707288,-2.530026,-7.867726,5.633159,-6.970842,5.380785,8.334875,-2.091723,-5.160612,-1.749825,3.562565,8.295150,9.579420,-0.146091,2.255543,0.974824,6.441963,-0.284606,-8.965311,-9.602559,-2.735767,3.041420,1.571709,1.341788,-2.678110,-6.504295,9.519817,-0.548588,8.154570,-7.448740,-8.532232,-2.427828,-0.503356,8.948068,-2.376526,4.654383,8.100398,-8.516426,0.585149,2.404095,9.349162,3.228381,4.962491,9.294794,-5.238613,1.438626,6.069794,-2.795449,-2.200584,-4.861334,-8.504839,4.719700,-1.207338,-5.981309,5.840013,7.999646,4.002098,7.016743,9.860659,-3.521875,-1.058648,-4.449135,9.054595,5.052182,0.816444,-6.643057,-0.535921,0.427519,2.391637,-7.559701,3.519207,4.273032,-9.173289,7.840686,6.459209,1.464112,6.431417,-4.643080,7.313790,-3.963020,2.765953,-4.158080,-9.483747,3.503164,9.677688,-7.064262,8.450449,-7.631487,-4.589187,8.232199,2.488504,-2.297388,9.520450,8.430359,-7.565848,6.237773,-0.648483,7.105887,1.126734,-7.589145,-6.544833,-5.150039,-0.708759,5.811151,-8.238270,-1.201825,-0.958825,1.675834,1.321015,-5.540485,-9.437891,-0.044688,4.096754,-0.647566,-9.434892,7.828511,6.121436], dtype = "float64")#candidate|3657|(3360,)|const|float64
call_3656 = relay.TupleGetItem(func_2098_call(relay.reshape(const_3657.astype('float64'), [3360,])), 2)
call_3658 = relay.TupleGetItem(func_2101_call(relay.reshape(const_3657.astype('float64'), [3360,])), 2)
output = relay.Tuple([call_3652,call_3656,const_3657,])
output2 = relay.Tuple([call_3653,call_3658,const_3657,])
func_3663 = relay.Function([], output)
mod['func_3663'] = func_3663
mod = relay.transform.InferType()(mod)
output = func_3663()
func_3664 = relay.Function([], output)
mutated_mod['func_3664'] = func_3664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1827_call = mod.get_global_var('func_1827')
func_1828_call = mutated_mod.get_global_var('func_1828')
call_3682 = relay.TupleGetItem(func_1827_call(), 0)
call_3683 = relay.TupleGetItem(func_1828_call(), 0)
output = relay.Tuple([call_3682,])
output2 = relay.Tuple([call_3683,])
func_3689 = relay.Function([], output)
mod['func_3689'] = func_3689
mod = relay.transform.InferType()(mod)
mutated_mod['func_3689'] = func_3689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3689_call = mutated_mod.get_global_var('func_3689')
call_3690 = func_3689_call()
output = call_3690
func_3691 = relay.Function([], output)
mutated_mod['func_3691'] = func_3691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1827_call = mod.get_global_var('func_1827')
func_1828_call = mutated_mod.get_global_var('func_1828')
call_3700 = relay.TupleGetItem(func_1827_call(), 0)
call_3701 = relay.TupleGetItem(func_1828_call(), 0)
output = relay.Tuple([call_3700,])
output2 = relay.Tuple([call_3701,])
func_3705 = relay.Function([], output)
mod['func_3705'] = func_3705
mod = relay.transform.InferType()(mod)
mutated_mod['func_3705'] = func_3705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3705_call = mutated_mod.get_global_var('func_3705')
call_3706 = func_3705_call()
output = call_3706
func_3707 = relay.Function([], output)
mutated_mod['func_3707'] = func_3707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1860_call = mod.get_global_var('func_1860')
func_1862_call = mutated_mod.get_global_var('func_1862')
call_3736 = func_1860_call()
call_3737 = func_1860_call()
uop_3738 = relay.asinh(call_3736.astype('float64')) # shape=(14, 1, 15)
uop_3740 = relay.asinh(call_3737.astype('float64')) # shape=(14, 1, 15)
output = uop_3738
output2 = uop_3740
func_3745 = relay.Function([], output)
mod['func_3745'] = func_3745
mod = relay.transform.InferType()(mod)
output = func_3745()
func_3746 = relay.Function([], output)
mutated_mod['func_3746'] = func_3746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3273_call = mod.get_global_var('func_3273')
func_3274_call = mutated_mod.get_global_var('func_3274')
call_3747 = relay.TupleGetItem(func_3273_call(), 1)
call_3748 = relay.TupleGetItem(func_3274_call(), 1)
output = relay.Tuple([call_3747,])
output2 = relay.Tuple([call_3748,])
func_3749 = relay.Function([], output)
mod['func_3749'] = func_3749
mod = relay.transform.InferType()(mod)
output = func_3749()
func_3750 = relay.Function([], output)
mutated_mod['func_3750'] = func_3750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mod.get_global_var('func_1743')
func_1744_call = mutated_mod.get_global_var('func_1744')
call_3767 = relay.TupleGetItem(func_1743_call(), 0)
call_3768 = relay.TupleGetItem(func_1744_call(), 0)
func_2949_call = mod.get_global_var('func_2949')
func_2951_call = mutated_mod.get_global_var('func_2951')
call_3769 = relay.TupleGetItem(func_2949_call(), 0)
call_3770 = relay.TupleGetItem(func_2951_call(), 0)
func_971_call = mod.get_global_var('func_971')
func_973_call = mutated_mod.get_global_var('func_973')
call_3780 = func_971_call()
call_3781 = func_971_call()
func_2421_call = mod.get_global_var('func_2421')
func_2422_call = mutated_mod.get_global_var('func_2422')
call_3788 = relay.TupleGetItem(func_2421_call(), 0)
call_3789 = relay.TupleGetItem(func_2422_call(), 0)
output = relay.Tuple([call_3767,call_3769,call_3780,call_3788,])
output2 = relay.Tuple([call_3768,call_3770,call_3781,call_3789,])
func_3796 = relay.Function([], output)
mod['func_3796'] = func_3796
mod = relay.transform.InferType()(mod)
output = func_3796()
func_3797 = relay.Function([], output)
mutated_mod['func_3797'] = func_3797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2053_call = mod.get_global_var('func_2053')
func_2054_call = mutated_mod.get_global_var('func_2054')
call_3826 = relay.TupleGetItem(func_2053_call(), 1)
call_3827 = relay.TupleGetItem(func_2054_call(), 1)
output = call_3826
output2 = call_3827
func_3828 = relay.Function([], output)
mod['func_3828'] = func_3828
mod = relay.transform.InferType()(mod)
output = func_3828()
func_3829 = relay.Function([], output)
mutated_mod['func_3829'] = func_3829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_3906 = func_1075_call()
call_3907 = func_1075_call()
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_3912 = relay.TupleGetItem(func_209_call(), 0)
call_3913 = relay.TupleGetItem(func_210_call(), 0)
bop_3923 = relay.bitwise_or(call_3912.astype('int64'), relay.reshape(call_3906.astype('int64'), relay.shape_of(call_3912))) # shape=(14, 1, 15)
bop_3926 = relay.bitwise_or(call_3913.astype('int64'), relay.reshape(call_3907.astype('int64'), relay.shape_of(call_3913))) # shape=(14, 1, 15)
func_3663_call = mod.get_global_var('func_3663')
func_3664_call = mutated_mod.get_global_var('func_3664')
call_3930 = relay.TupleGetItem(func_3663_call(), 0)
call_3931 = relay.TupleGetItem(func_3664_call(), 0)
func_2374_call = mod.get_global_var('func_2374')
func_2377_call = mutated_mod.get_global_var('func_2377')
var_3939 = relay.var("var_3939", dtype = "float32", shape = (1680,))#candidate|3939|(1680,)|var|float32
call_3938 = relay.TupleGetItem(func_2374_call(relay.reshape(var_3939.astype('float32'), [1680, 1])), 0)
call_3940 = relay.TupleGetItem(func_2377_call(relay.reshape(var_3939.astype('float32'), [1680, 1])), 0)
output = relay.Tuple([bop_3923,call_3930,call_3938,var_3939,])
output2 = relay.Tuple([bop_3926,call_3931,call_3940,var_3939,])
func_3954 = relay.Function([var_3939,], output)
mod['func_3954'] = func_3954
mod = relay.transform.InferType()(mod)
mutated_mod['func_3954'] = func_3954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3955 = relay.var("var_3955", dtype = "float32", shape = (1680,))#candidate|3955|(1680,)|var|float32
func_3954_call = mutated_mod.get_global_var('func_3954')
call_3956 = func_3954_call(var_3955)
output = call_3956
func_3957 = relay.Function([var_3955], output)
mutated_mod['func_3957'] = func_3957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_4080 = relay.TupleGetItem(func_1550_call(), 0)
call_4081 = relay.TupleGetItem(func_1551_call(), 0)
output = relay.Tuple([call_4080,])
output2 = relay.Tuple([call_4081,])
func_4095 = relay.Function([], output)
mod['func_4095'] = func_4095
mod = relay.transform.InferType()(mod)
output = func_4095()
func_4096 = relay.Function([], output)
mutated_mod['func_4096'] = func_4096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_4124 = func_782_call()
call_4125 = func_782_call()
output = call_4124
output2 = call_4125
func_4126 = relay.Function([], output)
mod['func_4126'] = func_4126
mod = relay.transform.InferType()(mod)
output = func_4126()
func_4127 = relay.Function([], output)
mutated_mod['func_4127'] = func_4127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_4153 = func_421_call()
call_4154 = func_421_call()
output = call_4153
output2 = call_4154
func_4180 = relay.Function([], output)
mod['func_4180'] = func_4180
mod = relay.transform.InferType()(mod)
output = func_4180()
func_4181 = relay.Function([], output)
mutated_mod['func_4181'] = func_4181
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4238 = relay.var("var_4238", dtype = "int64", shape = ())#candidate|4238|()|var|int64
var_4239 = relay.var("var_4239", dtype = "int64", shape = (4, 7, 1))#candidate|4239|(4, 7, 1)|var|int64
bop_4240 = relay.bitwise_and(var_4238.astype('int64'), var_4239.astype('int64')) # shape=(4, 7, 1)
var_4245 = relay.var("var_4245", dtype = "int64", shape = (6, 7, 15))#candidate|4245|(6, 7, 15)|var|int64
bop_4246 = relay.logical_xor(var_4238.astype('uint32'), var_4245.astype('uint32')) # shape=(6, 7, 15)
output = relay.Tuple([bop_4240,bop_4246,])
output2 = relay.Tuple([bop_4240,bop_4246,])
func_4252 = relay.Function([var_4238,var_4239,var_4245,], output)
mod['func_4252'] = func_4252
mod = relay.transform.InferType()(mod)
var_4253 = relay.var("var_4253", dtype = "int64", shape = ())#candidate|4253|()|var|int64
var_4254 = relay.var("var_4254", dtype = "int64", shape = (4, 7, 1))#candidate|4254|(4, 7, 1)|var|int64
var_4255 = relay.var("var_4255", dtype = "int64", shape = (6, 7, 15))#candidate|4255|(6, 7, 15)|var|int64
output = func_4252(var_4253,var_4254,var_4255,)
func_4256 = relay.Function([var_4253,var_4254,var_4255,], output)
mutated_mod['func_4256'] = func_4256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_4311 = func_782_call()
call_4312 = func_782_call()
output = relay.Tuple([call_4311,])
output2 = relay.Tuple([call_4312,])
func_4315 = relay.Function([], output)
mod['func_4315'] = func_4315
mod = relay.transform.InferType()(mod)
mutated_mod['func_4315'] = func_4315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4315_call = mutated_mod.get_global_var('func_4315')
call_4316 = func_4315_call()
output = call_4316
func_4317 = relay.Function([], output)
mutated_mod['func_4317'] = func_4317
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4331 = relay.var("var_4331", dtype = "uint32", shape = (4, 15, 11))#candidate|4331|(4, 15, 11)|var|uint32
const_4332 = relay.const([[[-8,8,-8,10,9,-9,4,3,-10,-3,9],[6,-10,4,-2,-5,-10,2,2,-10,-9,10],[-6,-9,6,-1,3,-5,-4,8,-10,4,8],[7,-1,-8,8,4,-5,-2,6,-5,3,-3],[1,-2,-6,10,-4,3,6,8,3,9,4],[6,5,10,-3,4,4,-4,2,-4,1,-2],[3,10,-1,-2,10,-6,1,-10,8,-10,-8],[3,-6,-6,6,-5,-9,5,-4,8,6,9],[-9,2,3,-10,-6,-2,-1,1,-8,6,-1],[-9,7,1,1,-1,-8,-10,4,-1,2,-3],[2,10,-10,7,-9,-6,-4,-2,-6,-7,-7],[-3,-4,3,10,9,-2,1,-7,-3,9,-5],[-8,-7,-9,7,1,6,6,1,5,-9,-1],[9,1,2,-3,2,-3,4,-5,-7,2,-2],[-3,6,5,7,8,-1,7,-10,2,2,4]],[[7,-8,8,8,-10,-4,-10,-6,4,4,2],[1,-4,3,-10,1,-8,10,10,-5,10,1],[-8,-9,-8,10,-6,1,5,5,2,-1,-6],[-4,2,7,9,-3,4,9,-7,-1,9,-3],[7,-10,-6,9,5,-8,-3,8,-4,6,5],[9,4,4,-3,6,9,-1,6,-6,-3,7],[-3,7,5,7,-1,-1,8,6,4,-5,9],[-5,4,-7,10,-3,8,10,3,5,-4,9],[-10,7,-9,7,6,5,5,-9,6,8,1],[-1,-5,-8,-1,-5,2,-4,-2,-8,-3,10],[-7,-5,-10,10,10,6,6,-4,-3,-7,-1],[-5,-4,-3,8,-6,-2,-9,-3,4,8,9],[-5,10,-2,-2,-10,5,-2,2,4,6,-1],[10,3,7,5,-7,1,-8,-6,5,7,-1],[-10,10,3,10,10,9,-6,-7,4,-1,1]],[[5,2,-3,-2,10,7,6,6,3,-5,-9],[9,-2,-10,-6,-6,8,3,-9,-6,-6,10],[3,7,-2,-6,-3,-1,-8,10,1,8,-4],[-1,-7,3,-9,5,-9,-6,5,5,9,-5],[-4,4,2,5,3,10,-2,-3,-6,-3,-1],[7,2,-7,8,1,-8,-9,7,10,-1,-1],[-5,-4,-3,7,5,-3,6,10,-2,7,-6],[-2,-10,2,-5,6,7,1,8,-7,2,2],[8,1,10,1,2,-8,8,-6,5,2,-4],[4,-1,-5,-1,-8,-8,10,-6,-4,8,5],[-4,-10,-4,2,5,10,-9,8,3,-10,8],[-8,2,-5,6,8,-2,8,1,4,10,-6],[10,-8,2,3,-7,-4,-3,-1,10,8,8],[-6,9,-6,3,-7,-6,7,2,-7,10,-2],[-2,-3,-2,2,8,8,-7,6,6,6,-6]],[[-1,-2,-1,-4,9,-6,8,-5,6,10,1],[-8,-1,8,-8,8,-5,10,7,9,-9,8],[2,10,7,2,9,-4,-6,-6,9,6,6],[-1,1,9,-6,-9,-2,-6,9,6,-10,6],[3,2,8,7,5,7,10,8,-4,-4,-6],[-5,10,10,-4,-10,10,10,-4,-2,-4,7],[-6,8,1,-6,4,-9,5,-8,8,5,-2],[6,9,-4,-6,7,-5,-1,8,-1,-1,9],[-4,4,-7,-1,-1,4,4,4,-1,1,-5],[2,10,-6,-8,8,3,3,8,-8,9,-2],[4,-3,7,10,-6,5,-10,8,7,-9,5],[-2,-3,3,-4,7,1,2,-3,1,-5,-5],[9,-2,-7,-7,-2,-7,-9,1,7,1,7],[5,-6,-9,-3,7,-10,-8,-9,-1,-6,-7],[1,10,5,6,-5,-4,-9,3,9,-6,10]]], dtype = "uint32")#candidate|4332|(4, 15, 11)|const|uint32
bop_4333 = relay.bitwise_xor(var_4331.astype('uint32'), relay.reshape(const_4332.astype('uint32'), relay.shape_of(var_4331))) # shape=(4, 15, 11)
output = bop_4333
output2 = bop_4333
func_4339 = relay.Function([var_4331,], output)
mod['func_4339'] = func_4339
mod = relay.transform.InferType()(mod)
mutated_mod['func_4339'] = func_4339
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4340 = relay.var("var_4340", dtype = "uint32", shape = (4, 15, 11))#candidate|4340|(4, 15, 11)|var|uint32
func_4339_call = mutated_mod.get_global_var('func_4339')
call_4341 = func_4339_call(var_4340)
output = call_4341
func_4342 = relay.Function([var_4340], output)
mutated_mod['func_4342'] = func_4342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_4385 = func_782_call()
call_4386 = func_782_call()
func_4126_call = mod.get_global_var('func_4126')
func_4127_call = mutated_mod.get_global_var('func_4127')
call_4391 = func_4126_call()
call_4392 = func_4126_call()
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_4400 = relay.TupleGetItem(func_1550_call(), 0)
call_4401 = relay.TupleGetItem(func_1551_call(), 0)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_4402 = func_335_call()
call_4403 = func_335_call()
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
var_4405 = relay.var("var_4405", dtype = "float64", shape = (3360,))#candidate|4405|(3360,)|var|float64
call_4404 = relay.TupleGetItem(func_674_call(relay.reshape(var_4405.astype('float64'), [14, 16, 15])), 0)
call_4406 = relay.TupleGetItem(func_676_call(relay.reshape(var_4405.astype('float64'), [14, 16, 15])), 0)
bop_4422 = relay.logical_and(call_4400.astype('bool'), relay.reshape(call_4385.astype('bool'), relay.shape_of(call_4400))) # shape=(14, 1, 15)
bop_4425 = relay.logical_and(call_4401.astype('bool'), relay.reshape(call_4386.astype('bool'), relay.shape_of(call_4401))) # shape=(14, 1, 15)
bop_4442 = relay.maximum(call_4404.astype('int8'), relay.reshape(call_4402.astype('int8'), relay.shape_of(call_4404))) # shape=(14, 1, 15)
bop_4445 = relay.maximum(call_4406.astype('int8'), relay.reshape(call_4403.astype('int8'), relay.shape_of(call_4406))) # shape=(14, 1, 15)
func_2098_call = mod.get_global_var('func_2098')
func_2101_call = mutated_mod.get_global_var('func_2101')
call_4446 = relay.TupleGetItem(func_2098_call(relay.reshape(var_4405.astype('float64'), [3360,])), 0)
call_4447 = relay.TupleGetItem(func_2101_call(relay.reshape(var_4405.astype('float64'), [3360,])), 0)
output = relay.Tuple([call_4391,var_4405,bop_4422,bop_4442,call_4446,])
output2 = relay.Tuple([call_4392,var_4405,bop_4425,bop_4445,call_4447,])
func_4450 = relay.Function([var_4405,], output)
mod['func_4450'] = func_4450
mod = relay.transform.InferType()(mod)
var_4451 = relay.var("var_4451", dtype = "float64", shape = (3360,))#candidate|4451|(3360,)|var|float64
output = func_4450(var_4451)
func_4452 = relay.Function([var_4451], output)
mutated_mod['func_4452'] = func_4452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2688_call = mod.get_global_var('func_2688')
func_2690_call = mutated_mod.get_global_var('func_2690')
call_4530 = relay.TupleGetItem(func_2688_call(), 1)
call_4531 = relay.TupleGetItem(func_2690_call(), 1)
output = call_4530
output2 = call_4531
func_4553 = relay.Function([], output)
mod['func_4553'] = func_4553
mod = relay.transform.InferType()(mod)
output = func_4553()
func_4554 = relay.Function([], output)
mutated_mod['func_4554'] = func_4554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_4558 = func_335_call()
call_4559 = func_335_call()
func_497_call = mod.get_global_var('func_497')
func_500_call = mutated_mod.get_global_var('func_500')
var_4571 = relay.var("var_4571", dtype = "float32", shape = (1680,))#candidate|4571|(1680,)|var|float32
call_4570 = relay.TupleGetItem(func_497_call(relay.reshape(var_4571.astype('float32'), [14, 8, 15])), 1)
call_4572 = relay.TupleGetItem(func_500_call(relay.reshape(var_4571.astype('float32'), [14, 8, 15])), 1)
output = relay.Tuple([call_4558,call_4570,var_4571,])
output2 = relay.Tuple([call_4559,call_4572,var_4571,])
func_4579 = relay.Function([var_4571,], output)
mod['func_4579'] = func_4579
mod = relay.transform.InferType()(mod)
mutated_mod['func_4579'] = func_4579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4580 = relay.var("var_4580", dtype = "float32", shape = (1680,))#candidate|4580|(1680,)|var|float32
func_4579_call = mutated_mod.get_global_var('func_4579')
call_4581 = func_4579_call(var_4580)
output = call_4581
func_4582 = relay.Function([var_4580], output)
mutated_mod['func_4582'] = func_4582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_4620 = relay.TupleGetItem(func_1171_call(), 1)
call_4621 = relay.TupleGetItem(func_1172_call(), 1)
output = call_4620
output2 = call_4621
func_4622 = relay.Function([], output)
mod['func_4622'] = func_4622
mod = relay.transform.InferType()(mod)
output = func_4622()
func_4623 = relay.Function([], output)
mutated_mod['func_4623'] = func_4623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1269_call = mod.get_global_var('func_1269')
func_1270_call = mutated_mod.get_global_var('func_1270')
call_4691 = relay.TupleGetItem(func_1269_call(), 0)
call_4692 = relay.TupleGetItem(func_1270_call(), 0)
output = call_4691
output2 = call_4692
func_4722 = relay.Function([], output)
mod['func_4722'] = func_4722
mod = relay.transform.InferType()(mod)
mutated_mod['func_4722'] = func_4722
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4722_call = mutated_mod.get_global_var('func_4722')
call_4723 = func_4722_call()
output = call_4723
func_4724 = relay.Function([], output)
mutated_mod['func_4724'] = func_4724
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4736 = relay.var("var_4736", dtype = "float32", shape = (1, 12, 14))#candidate|4736|(1, 12, 14)|var|float32
uop_4737 = relay.cos(var_4736.astype('float32')) # shape=(1, 12, 14)
output = relay.Tuple([uop_4737,])
output2 = relay.Tuple([uop_4737,])
func_4740 = relay.Function([var_4736,], output)
mod['func_4740'] = func_4740
mod = relay.transform.InferType()(mod)
mutated_mod['func_4740'] = func_4740
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4741 = relay.var("var_4741", dtype = "float32", shape = (1, 12, 14))#candidate|4741|(1, 12, 14)|var|float32
func_4740_call = mutated_mod.get_global_var('func_4740')
call_4742 = func_4740_call(var_4741)
output = call_4742
func_4743 = relay.Function([var_4741], output)
mutated_mod['func_4743'] = func_4743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1269_call = mod.get_global_var('func_1269')
func_1270_call = mutated_mod.get_global_var('func_1270')
call_4755 = relay.TupleGetItem(func_1269_call(), 1)
call_4756 = relay.TupleGetItem(func_1270_call(), 1)
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_4762 = func_4180_call()
call_4763 = func_4180_call()
func_1075_call = mod.get_global_var('func_1075')
func_1076_call = mutated_mod.get_global_var('func_1076')
call_4770 = func_1075_call()
call_4771 = func_1075_call()
func_2853_call = mod.get_global_var('func_2853')
func_2855_call = mutated_mod.get_global_var('func_2855')
var_4775 = relay.var("var_4775", dtype = "float32", shape = (420,))#candidate|4775|(420,)|var|float32
call_4774 = relay.TupleGetItem(func_2853_call(relay.reshape(var_4775.astype('float32'), [420,])), 3)
call_4776 = relay.TupleGetItem(func_2855_call(relay.reshape(var_4775.astype('float32'), [420,])), 3)
output = relay.Tuple([call_4755,call_4762,call_4770,call_4774,var_4775,])
output2 = relay.Tuple([call_4756,call_4763,call_4771,call_4776,var_4775,])
func_4778 = relay.Function([var_4775,], output)
mod['func_4778'] = func_4778
mod = relay.transform.InferType()(mod)
var_4779 = relay.var("var_4779", dtype = "float32", shape = (420,))#candidate|4779|(420,)|var|float32
output = func_4778(var_4779)
func_4780 = relay.Function([var_4779], output)
mutated_mod['func_4780'] = func_4780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1860_call = mod.get_global_var('func_1860')
func_1862_call = mutated_mod.get_global_var('func_1862')
call_4864 = func_1860_call()
call_4865 = func_1860_call()
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_4879 = relay.TupleGetItem(func_1590_call(relay.reshape(call_4864.astype('float32'), [14, 1, 15])), 0)
call_4880 = relay.TupleGetItem(func_1592_call(relay.reshape(call_4864.astype('float32'), [14, 1, 15])), 0)
output = relay.Tuple([call_4864,call_4879,])
output2 = relay.Tuple([call_4865,call_4880,])
func_4898 = relay.Function([], output)
mod['func_4898'] = func_4898
mod = relay.transform.InferType()(mod)
mutated_mod['func_4898'] = func_4898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4898_call = mutated_mod.get_global_var('func_4898')
call_4899 = func_4898_call()
output = call_4899
func_4900 = relay.Function([], output)
mutated_mod['func_4900'] = func_4900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2688_call = mod.get_global_var('func_2688')
func_2690_call = mutated_mod.get_global_var('func_2690')
call_4928 = relay.TupleGetItem(func_2688_call(), 0)
call_4929 = relay.TupleGetItem(func_2690_call(), 0)
func_864_call = mod.get_global_var('func_864')
func_868_call = mutated_mod.get_global_var('func_868')
const_4939 = relay.const([7.652764,9.973324,9.023232,-3.512132,0.392002,5.079911,8.699714,-9.103620,-4.539361,8.094924,-1.814016,-1.782322,-7.814801,0.803863,8.873029,2.845210,-2.891268,5.651127,-0.271401,-3.875760,9.314460,-9.554333,-6.786345,-6.449942,-0.188865,2.892484,-7.308014,2.886659,-1.346107,-0.008946,1.862867,5.234999,-8.876946,7.001066,-0.389215,-5.251340,6.242924,-2.369881,8.278646,-7.767381,-8.943928,-0.431090,0.553132,8.301527,1.956772,1.736099,-7.187765,-5.566538,8.260241,9.513119,7.275143,2.722886,-3.909422,-3.347979,9.201519,1.471077,-2.025024,-0.938988,9.556274,4.928292,7.425862,-8.292788,3.794814,6.941546,-9.349950,-9.910559,-2.866324,2.882740,7.646130,5.547318,-0.525109,4.589963,-5.708143,5.634249,5.677388,-3.627463,5.896357,-5.135979,2.496740,-9.001820,-0.811263,1.497219,-7.071423,-0.080172,-9.464272,-8.788603,-9.336161,0.075240,8.104018,6.638992,-9.579489,-6.423121,-4.405551,-5.588824,-4.041837,8.412548,-2.326384,0.424709,4.956555,-7.787940,3.240873,5.476433,-5.085288,2.667918,8.566975,1.005255,-9.158523,7.272870,-1.263895,0.579863,-8.133223,-1.740986,5.669042,-6.152179,3.475972,6.253576,6.975963,-9.352734,6.105376,-2.374936,-3.303983,-9.131054,8.745179,3.579315,-1.792430,-1.266614,-0.248696,7.635531,-9.426946,-7.115460,-1.341942,6.473254,-2.752834,-9.542699,9.087487,-6.995378,-7.906369,-4.119489,2.311102,1.762568,-2.873317,-8.340439,-1.755855,9.201041,0.641289,-1.256169,0.934393,-2.300608,-0.852068,7.495362,9.615570,5.318523,5.136260,9.817088,-3.369165,-0.700421,-1.462488,3.399112,-7.248501,3.087337,-5.876341,3.149042,1.356136,-0.701120,-1.648029,9.487403,7.459251,3.141455,9.596552,0.974933,-5.975841,-0.990510,0.209916,4.769740,-8.153064,5.792095,7.270322,-3.163372,-4.337495,-1.012486,0.366354,-2.063290,-4.915632,0.787285,-4.873125,7.110406,-1.195533,2.600923,6.371818,7.187145,-3.555242,7.630178,5.029182,-5.509862,-8.387480,5.045182,9.944043,-6.265531,0.752225,1.944935,5.637857,-0.906849,-3.466748,6.974501,1.258544,-1.963025,6.794628,2.550731,1.773075,5.525398,-3.879797,5.437440,-8.899300,1.266484,8.304754,-5.629347,-6.434607,-7.278467,-4.104826,-8.721748,-5.279528,3.076695,-0.987307,2.450580,8.833426,6.677596,8.581811,6.882994,6.912553,5.122358,6.565513,4.845950,1.197923,-7.214669,5.835008,2.776551,1.684321,7.276085,5.318811,-5.179114,5.682933,-0.549884,-1.437474,2.291455,-5.845166,5.234362,-3.745666,7.974235,-4.236824,5.312853,0.093029,-7.230182,-1.001688,-4.568124,-8.181310,-4.078207,5.964124,-4.306767,-2.687253,5.796098,-7.305071,-1.967450,3.530245,-8.830698,7.873251,0.486193,-8.879409,-8.256504,3.902600,-7.089089,3.564618,-0.042638,8.644944,-6.858627,-8.179638,9.899786,-9.038859,1.982483,8.029295,-5.208132,7.483336,1.158719,0.301078,-3.562948,1.617774,-0.191629,3.242759,3.338836,7.702921,-4.607074,0.320111,-6.484529,6.198584,0.433834,-8.718687,-0.547272,4.147457,1.615233,9.280277,1.894945,6.994778,2.647892,-5.703762,5.409454,-5.661664,0.777118,8.205471,-8.485654,4.311248,-4.972344,9.953607,-4.097342,-4.516202,9.717643,3.866986,-6.076407,-0.562649,-9.412243,-0.320564,-2.642007,5.951025,-2.066045,3.726893,-1.836697,-1.011319,-1.636692,7.669093,-3.574177,5.087024,1.395861,6.767499,2.984613,1.186197,-6.127437,3.264880,-3.892283,1.893204,-3.744672,7.322184,9.456341,0.652950,0.273158,-1.040590,-4.279616,3.948503,4.084665,-7.574084,-1.962218,-6.512101,5.558564,4.364098,-6.941368,5.670738,-8.660696,7.666338,-8.487997,9.723623,7.629432,-7.022270,3.263760,8.930034,-1.391863,9.911806,6.446687,4.419820,-0.600801,8.854300,7.821377,2.507021,8.213641,-9.429612,6.141838,-4.942834,7.500463,-8.515865,-6.974006,6.448120,9.821937,-0.531251,-5.792062,-9.071418,-9.747379,-8.028152,-8.627256,4.783781,-4.605557,6.684445,-6.401059,5.405164,-4.287825,-2.500553,6.014166,6.522374,5.672315,-8.086740,-4.924802,-0.942538,-7.227676,-3.273870,-6.773856,-3.791479,8.066490,-0.702066,9.524298,-2.633237,9.740871,4.515837,-5.031568,-4.946212,-7.536743,-6.176939,8.598143,7.241396,5.445229,-4.168590,-6.636167,-0.302745,-2.503430,4.745823,-0.466947,-5.319546,-1.597298,6.003205,-8.851544,-2.485152,-9.302334,9.081653,1.433305,3.899661,8.236535,-4.546406,-6.903787,1.803786,8.612278,1.604364,-3.710249,-3.798122,3.633747,-6.050285,3.744931,-6.520087,9.264211,5.851808,-4.401617,3.118089,-1.699754,7.976358,-9.799040,2.224871,1.578992,-7.804447,-8.319657,7.988663,-9.067550,-7.238836,-4.041328,1.931540,-2.806373,5.141152,1.089537,-2.001991,-5.811566,-3.408492,0.437571,7.034737,-3.269018,-5.837742,-8.883863,-8.722760,3.516089,-5.866548,0.151606,0.554872,-1.760662,7.239827,5.668526,9.982868,6.923764,0.397511,1.450638,-0.856741,-0.391971,7.523607,-1.208249,6.751973,-8.351914,3.984520,5.999346,0.632030,9.321548,6.721043,7.705070,9.778745,-3.621637,9.335600,4.460477,-1.791022,-2.701546,-3.266982,3.441480,7.793933,0.472995,-5.769998,0.613581,-4.935907,-4.518901,-5.761004,-7.311272,-8.061986,-2.210478,-3.714426,5.474209,8.441594,-2.701682,-7.307629,5.144422,3.281644,8.345860,7.319452,-5.487330,2.497202,2.737389,-1.177459,2.113496,-3.793116,-1.104501,3.909273,1.495811,6.453713,-0.835752,-9.636354,3.596185,-2.427906,4.073463,-3.647895,5.583112,-4.385223,2.061972,-3.853801,0.359759,-9.846396,-4.074934,-9.373915,-8.982735,6.129999,9.375958,-4.872478,-9.560542,5.563999,-1.063153,4.568139,-0.335022,-2.064096,-7.262228,-6.379060,9.757837,7.916221,9.671459,-3.107509,2.899597,-6.095283,5.132720,-7.445325,-5.370619,3.835334,2.044228,-4.590621,-1.229558,3.149933,-6.615528,-6.431966,-7.597468,1.905399,0.735811,8.261624,5.665466,-8.525945,-6.765102,-8.662963,-3.752863,2.026824,-5.394992,6.628180,-0.698713,7.009787,5.367030,-4.222259,6.637331,2.344601,1.626461,-8.775109,-9.113891,6.993883,4.900057,0.036098,6.928273,1.020779,0.930450,-7.108060,6.614167,-4.584868,-3.434343,-0.297918,-4.095365,-9.339340,-1.407373,-4.972485,2.121449,2.896725,-2.441792,7.716909,9.400649,2.460884,5.290926,-5.166460,-3.221455,3.043833,2.132197,-5.676901,1.727360,-9.783899,7.892712,4.309799,-6.792689,7.691407,5.998410,7.918265,7.224031,7.166947,-4.006533,3.126702,-3.595096,5.890884,-7.706231,1.015529,5.479292,2.055409,5.934634,7.760347,9.279266,-3.600064,1.797989,1.577409,-5.007531,-7.172023,-8.336506,1.190697,-9.983757,0.068266,9.685284,0.704156,-0.505502,1.413651,7.590659,2.979870,-6.704649,5.323325,7.916734,-7.573060,-3.507591,4.022052,5.353676,2.138452,9.550430,-2.054784,-6.581143,8.515003,8.701337,-1.032322,-9.650672,4.881432,5.757975,-2.121630,-5.332761,-9.775556,2.588031,6.215649,3.945258,0.483626,3.473216,1.700291,4.460664,-1.089279,3.357046,8.471128,6.423572,-3.892850,1.041220,1.028384,-6.061045,-4.921303,2.750646,-7.392747,1.557677,-3.351772,2.028960,-9.655208,-8.211011,6.014952,4.575593,1.834796,-3.841518,6.903800,6.931830,7.368017,-0.802121,9.950670,5.677015,-6.612537,3.954405,-7.951067,-2.431583,3.023789,1.339742,6.597009,8.520184,5.805846,-9.621063,-1.308496,-3.067022,1.824251,9.450491,-3.209475,-1.183264,4.283960,2.833395,6.809334,-5.401181,3.586756,7.108929,-0.506191,7.673631,-8.618719,-5.662484,8.455958,-7.778974,-1.658621,-6.837025,0.263583,8.599214,-8.287026,-4.427082,6.821144,2.671613,-6.994986,5.895245,1.907653,0.341763,-3.320750,-6.162358,-1.089222,4.946707,8.246483,8.507018,-2.428659,2.429248,-0.614811,-5.368609,8.198245,-4.822867,1.045409,-8.802007,-3.127542,-7.817064,-8.951911,5.332454,-8.250182,8.236062,-6.532888,-8.993426,9.821630,1.166519,8.795716,5.713108,1.891773,-5.828239,8.848130,-2.018495,-3.046750,2.284777,9.255358,7.603595,4.399075,7.960062,-3.588459,-6.322036,-7.011321,6.192818,-9.096207,-3.759574,-8.996549,-8.061710,4.100227,7.269214,4.837684,-7.114996,3.779971,-6.358919,-8.939671,-0.884891,0.960253,5.236558,3.393582,4.067549,4.389954,4.880149,9.024188,-3.725873,-8.007766,-6.418333,-9.026300,2.379503,4.980184,-9.961860,4.573710,-2.874356,3.517095,-2.527709,-0.382021,-7.333769,6.904409,0.966495,3.166157,-0.084471,0.353659,-7.653526,2.433116,-3.298192,8.898297,2.210107,8.177915,-6.135527,0.286560,8.268584,-0.732789,2.857497,-1.137545,-4.584115,-3.903383,7.231193,-2.942595,6.914117,5.516844,-1.427605,-4.277018,-3.165983,8.471963,4.621678,2.560137,-2.407540,-3.646435,-4.392181,-7.417655,0.281649,4.869438,-1.880030,-2.241601,5.834966,6.074568,-4.484587,9.826995,-5.180956,7.170926,8.562592,-0.493339,5.687930,-0.022594,1.360989,-6.947720,3.644489,-7.586508,7.964571,-6.967398,-3.019926,-1.598658,3.060944,7.122444,-2.877987,9.569733,-4.629465,4.409592,0.291387,0.174818,-6.369428,9.424779,2.188625,-5.319135,-0.652162,4.070443,-9.894689,5.817726,-1.774351,3.798323,-5.762403,-6.024249,4.548906,-4.476744,6.219847,2.196103,5.848917,-7.616097,-5.153216,-1.355711,5.514921,-1.798888,7.571690,3.488291,-4.207611,4.444698,-8.495018,9.537500,7.038649,-7.575669,2.806519,7.538997,-1.702863,5.038678,-7.651045,6.511251,-1.485130,5.545441,2.503521,5.915846,-8.890733,-5.407347,-6.312558,-5.287504,8.365597,3.125898,-9.069589,-1.593425,-1.725688,-7.690607,7.774582,-4.254738,6.550171,8.887878,-5.924633,-5.237051,3.183686,1.645700,9.519323,-9.957787,-3.822074,1.403989,-5.605835,6.965740,-6.973920,1.625266,3.288293,9.190604,8.994934,-9.977321,9.601409,-7.625961,0.661082,-3.460058,9.340376,-6.308725,-1.146379,6.945033,0.872866,8.291234,-2.096908,1.496335,-8.965355,-5.098669,5.141150,-5.351944,3.619599,-3.714327,-3.994542,4.742447,4.280475,-7.963967,-4.085906,-7.406520,-8.169876,7.987958,-3.446703,6.638581,2.895272,-4.007292,-9.644936,4.702181,-7.887434,-7.088615,-2.014531,-5.218961,5.070879,-7.974534,-5.635259,8.082288,-3.460122,9.681560,8.931611,-7.652458,-2.325636,-9.981705,8.139538,9.731671,5.911798,-1.577747,9.468234,1.007714,1.280550,-4.837259,-1.782909,4.130422,-1.067947,3.613569,1.930222,-9.124386,-3.953800,-3.053345,-8.047041,3.911199,0.739266,-2.973110,0.881184,-4.539607,7.941516,-7.700726,-4.068466,-3.246649,9.067958,6.216292,6.390258,-8.473639,-4.345118,7.146237,-5.077132,-6.839082,8.687580,8.001057,-1.418086,4.156576,-8.935315,7.079872,8.839106,-1.993393,2.962453,7.798917,2.715010,-3.616217,-8.758244,3.953187,2.994265,6.144494,-0.253414,9.648088,-9.861820,-2.757099,-4.061260,7.128581,0.045997,-9.889985,7.479780,-8.056128,-3.209568,-5.824259,-5.177318,0.915331,0.463037,-1.389462,8.421510,-0.776560,8.980309,2.476375,-7.214009,9.855405,-8.572250,-2.930583,-2.975061,-2.974466,-6.789004,6.459238,-7.533513,-6.739469,0.285463,7.381570,-7.662224,-1.637197,-3.318548,3.524145,2.369263,9.750512,1.915065,5.490528,-3.486571,-8.901745,8.013831,3.902588,-1.215061,4.459863,3.873158,2.861240,4.353318,9.511441,3.876097,-8.858520,5.892515,-3.931109,-6.790570,-7.665431,3.906968,1.965178,5.746664,3.779703,-0.845339,8.151253,1.880351,1.360608,8.000772,2.062081,3.991625,0.159633,7.741144,1.533747,6.339528,-2.170464,-8.301994,6.295620,-2.044343,-0.105232,-9.950508,-0.795193,-3.220844,-2.115669,-2.004973,-6.015969,2.174675,5.111327,7.105140,-0.794321,-0.377262,2.699267,-2.475801,-5.422370,6.769355,8.653777,7.232024,-9.488289,1.963439,1.214078,-1.962962,-3.372938,6.385961,-2.177605,-2.833903,7.402805,0.701446,-2.933514,-6.201298,-4.495543,1.970536,5.289951,-6.363465,-8.512513,-2.062390,7.065630,6.996397,-9.664600,8.131804,9.094539,-9.943060,3.932511,5.628511,8.640435,-3.367466,-7.008551,-3.761683,-8.147429,2.508620,-4.691068,-1.164907,-6.569360,8.233506,-9.823073,9.486051,6.057792,9.315158,8.393244,-9.253354,-3.110301,-6.519737,-0.584679,-0.175700,9.527503,5.014030,6.963400,-3.241429,0.177051,-2.421190,-2.312975,7.594280,7.975016,-4.933688,5.418809,-8.441289,-9.487798,-2.356447,3.499721,1.847580,-3.365554,-5.556630,7.535868,0.213458,6.696228,-5.187757,5.438178,4.603599,-3.924595,3.655722,-2.136936,6.439596,0.773237,7.504918,-8.612559,7.731793,2.844819,-9.312684,-5.783133,5.565491,-7.122473,-5.523791,9.851236,-9.985096,5.074315,7.888584,2.147728,-8.644836,3.334695,1.751246,9.908068,-0.270798,2.983335,0.101383,2.855282,0.752272,-0.821293,5.279103,9.590259,-2.864443,-8.398628,-0.836790,-2.140096,-4.340046,-0.634560,-2.133551,-0.475102,-8.738149,6.640090,-1.424181,-9.146920,-2.195132,7.263383,-6.152858,-5.741622,4.118002,-5.549243,-1.582779,8.339601,-3.298543,6.814035,0.844726,-6.002594,9.274131,6.964720,-0.988387,2.383361,-0.669467,-7.651454,5.925337,6.663652,5.847763,-4.175757,7.314488,-2.484703,3.988640,-5.493670,-9.847715,-8.333361,-2.979961,0.219169,8.418703,-9.467925,6.805490,-1.942022,8.866146,4.132309,1.891778,-8.892699,8.933360,4.948432,-5.244145,7.298579,-5.908676,-7.819541,3.193037,5.343774,-7.161070,4.533402,-2.370144,-9.065976,1.207579,4.769271,6.854625,5.533520,-3.513776,2.007558,-0.090735,5.661128,-0.173863,-0.940745,9.090537,-0.061819,6.889310,1.783317,2.257467,8.266847,-3.796042,-5.048301,-1.233746,-1.768931,-5.787958,-1.789489,8.275407,8.995959,9.959874,2.887453,0.921328,1.945559,6.092530,-8.732173,-5.337907,-4.101538,-5.245839,6.605862,-4.539698,-6.588637,5.850560,-1.369692,-8.925767,0.052242,9.056502,4.655117,-1.044356,2.138571,1.703520,2.863404,5.566187,-6.976509,-8.516050,-7.017120,-0.711413,7.326157,2.531843,-6.327753,5.487265,-7.179262,-6.710138,7.752988,-1.138892,3.872887,-9.645831,4.938180,-8.036912,-0.706294,4.911535,2.351104,6.281659,-7.820561,-6.328415,-6.855321,-3.382205,-6.052219,-4.404922,1.147140,-4.082053,5.759972,9.142421,-6.597315,-6.405844,-9.572989,-7.244764,6.818960,-2.832707,-5.601428,-2.716188,-0.845080,4.372344,-7.603989,-0.843154,-1.103684,-3.283597,-4.479625,2.334341,4.450843,6.802369,7.162410,1.053239,7.797637,-0.029419,7.053105,-4.730931,0.218185,-1.789632,-0.305913,-0.606987,-6.896984,-9.231393,-5.434106,7.687186,8.529767,-8.147810,-3.828490,-5.220480,8.937133,-8.966084,3.880114,7.033308,-5.426351,-6.612718,-9.044312,-9.387262,6.111078,5.188950,-9.164508,5.729132,5.887763,-6.533482,-5.718488,6.511880,-5.169341,-1.886661,0.953816,-6.869322,3.538895,-6.589744,1.342676,-8.855062,2.725352,9.497124,3.328448,4.221228,-9.988737,-8.122394,-5.052942,-2.673088,0.159797,2.600728,-7.711447,6.555455,-4.139463,-7.919846,-9.761426,7.649448,-5.140554,3.660281,1.026054,8.816421,-2.241210,-8.039858,8.913769,5.784051,5.915489,6.990767,6.243621,-8.017398,-6.329750,7.006232,8.142151,-3.814283,1.333321,2.913936,1.608872,-0.523244,2.315065,-7.194318,-7.587133,6.472822,-1.875929,0.890947,4.262618,-9.107273,-8.499731,-0.295307,-2.555762,-7.383714,-1.847200,-1.725463,-4.672756,-3.434425,-9.518736,-1.374590,-1.748679,-2.324060,3.531664,-6.345987,3.603548,-4.763055,2.739097,-6.622438,-4.037747,8.200592,-8.505802,-6.055977,3.164716,-9.869036,1.088443,-7.474120,5.577062,9.604250,-2.266395,6.408360,-9.262760,-5.558534,0.832863,1.541057,3.127188,-6.273107,-4.080751,-3.843824,7.972700,8.676119,6.207908,9.051205,6.127037,5.190685,-5.841001,3.826644,3.391645,-0.145577,-0.070170,-8.712837,8.948385,-7.055193,7.332002,7.204483,7.554232,0.199821,-5.539182,7.268473,5.601445,1.573912,-5.189572,-2.728950,-2.512058,-4.726290,-7.529782,-9.304783,1.177669,-7.401149,0.381978,-4.804729,-5.424523,-8.102077,-1.382646,-7.799326,-3.325491,5.924907,0.127830,-6.228860,9.020079,-9.112483,7.570099,1.472865,6.597266,1.522502,8.323480,-3.375960,-1.811258,-5.001861,-9.958069,-1.998398,-6.549906,0.548913,-3.847673,-9.452278,-9.822187,5.046844,7.393396,7.839082,-3.379512,-6.128988,-7.674548,-2.171222,8.065326,7.196695,2.496562,-5.244203,8.477076,0.947916,-1.010073,3.620369,1.874138,-1.181504,9.899324,7.950912,7.324604,8.900483,-4.036498,-2.883090,-6.993901,-6.187992,6.141809,-8.565684,-0.314989,-0.243724,9.835075,-7.380831,5.996523,3.274300,-7.276766,-8.415302,-1.032184,2.405893,1.392191,-8.780966,4.337061,-9.340926,-9.181008,3.161482,-8.637510,7.597976,-2.796003,-4.122701,-5.684087,-1.583328,2.220578,-7.877791,3.029029,-0.735571,4.157633,-3.292439,9.537054,-3.487957,0.668232,0.987238,8.177899,2.027935,-3.031133,3.538697,-4.258355,5.513370,9.963632,5.279959,4.239749,8.818353,0.329069,0.307570,-0.648406,-5.304194,2.498264,-1.739261,-9.079155,-6.465141,8.024419,4.913948,-1.507785,9.006849,1.921309,-4.646684,4.701598,7.569710,9.218507,5.951558,-0.488771,-2.680320,2.350806,6.800612,-3.303134,-6.307074,6.421461,5.924727,-0.671117,2.915945,-8.334951,-9.753852,-1.291156,-3.967827,-8.347846,2.096291,1.167701,3.816742,-9.054408,-1.113497,-7.971451,8.746178,-5.080584,5.772657,6.545370,-0.564022,-9.702979,0.010254,2.220629,6.966355,-2.140108,-6.303286,-2.609443,-4.303687,-2.109003,6.584443,-8.583071,4.966420,-0.418837,5.728786,0.708676,5.395169,7.045345,-6.968642,-5.163649,-5.021165,5.809210,-9.979170,-7.929743,-6.661270,2.501564,-4.291908,-4.192485,-6.106078,-6.124498,1.161264,-8.495332,-2.077767,4.776794,-6.626638,-4.989011,-5.076350,5.457151,4.912462,-7.515915,9.335245,3.409400,2.038242,8.431632,-3.677016,3.489796,4.886116,-4.624513,7.115316,9.988254,8.587323,0.534747,4.413726,-0.243935,-2.986921,-6.612341,-3.737010,3.271931,-5.100963,-1.584524,0.782085,-8.368319,0.161315,-9.268413,-0.780636,-0.623279,2.512398,-8.491966,-9.292978,1.887384,6.221689,-0.092677,7.446461,3.521979,-9.084147,3.370384,5.873187,6.318146,-0.756528,-4.560450,7.129426,0.475194,-7.173040,1.990136,-8.246347,2.160592,-3.580180,-7.666447,-5.542587,4.696459,7.956889,-1.471950,-3.842716,1.396966,8.300404,-6.993648,-2.841032,5.749247,4.360567,9.193463,5.311364,4.323097,3.836240,4.525935,6.295048,-3.096189,5.409165,8.733803,-5.030654,3.745823,-4.390177,-9.390024,4.196962,3.236953,-6.569239,-9.719669,-7.892376,-9.744626,8.894329,2.967469,-0.472256,7.223417,-5.989732,-8.887446,7.732750,-0.690603,4.072265,-4.914022,-0.120936,5.841906,5.577715,-6.669689,4.841433,8.442644,-9.563167,4.384690,-7.634271,1.461819,9.295181,-1.830615,2.142826,9.484364,5.574317,6.801174,1.821011,1.467422,-9.525144,-0.197144,-4.760211,2.466668,-4.477419,4.594112,9.065397,7.209775,-0.413015,-1.778039,-4.135613,-6.115174,8.597576,8.349896,-2.465565,7.366526,-2.607240,-7.562553,8.962070,-2.042909,-4.158523,6.647238,-9.327889,0.765488,-6.913656,-4.858469,8.782839,-5.097241,-6.124652,7.483483,-5.025788,3.755245,5.332705,7.661021,3.592318,-4.019689,-7.490439,-0.945778,4.464234,3.156519,6.006929,-5.927916,3.876351,0.488428,5.644194,-2.005868,-5.134244,-2.543929,-7.613674,-7.405621,2.128402,2.237928,-9.487165,-9.684610,5.116513,8.696734,0.991419,5.419997,2.971959,-8.791649,-8.335704,-6.686137,1.861932,-2.917100,0.662130,9.176964,0.262065,-6.223708,-2.871360,5.558539,-8.442433,-0.127290,9.647933,-4.682328,1.888812,0.997761,-9.765530,-9.187067,-0.770006,6.790561,8.558081,7.627360,0.876943,3.223779,-1.161700,-0.464836,5.450811,8.067610,-9.986717,2.105996,-8.474904,2.327869,6.396801,-1.344254,-3.252722,2.224094,8.819276,4.965200,-0.237740,-0.234270,3.214306,7.242390,-6.296077,7.207256,6.403287,-7.989896,5.162704,-4.959837,1.404663,9.111306,-8.406193,4.784704,5.916104,-3.106728,5.816169,-9.171655,3.874593,-9.733584,-7.804515,1.912975,-7.462427,-4.281124,3.289919,-2.799023,7.901966,2.169897,-9.134442,5.709084,8.802580,8.558925,8.252934,7.349150,-2.599888,-8.133737,-8.725704,-0.504297,1.696378,-7.373076,1.886709,5.410607,-2.039556,-8.868627,4.601017,-8.777209,8.436305,-1.597053,-0.375425,-8.012679,6.807664,1.772586,-4.471608,-9.748723,-6.515829,-1.204012,-9.543553,6.183262,-1.709161,2.986272,0.881318,-7.887383,-0.155233,7.689584,5.059883,2.230164,-2.071886,-6.575270,-6.427517,-6.395894,1.520183,-0.957867,-6.872546,7.058547,8.324993,6.328428,-2.198458,7.047758,-3.165757,2.203660,-8.541831,-3.672691,-8.273274,9.665033,7.986628,0.638765,8.283363,-4.781033,2.084096,-5.600108,6.259028,-3.499570,-2.531101,-6.302064,-2.992896,-2.875916,-4.471613,-8.915543,0.590069,3.166617,8.923080,6.993267,-5.750607,1.598128,4.809207,-6.981858,4.639439,0.073574,-4.209948,-1.104460,4.802045,-8.953207,4.906897,-5.229092,-6.227810,1.447993,0.588200,-0.168299,6.799067,2.568466,-0.822803,0.376618,-5.422676,7.856736,-0.400381,-0.833508,-5.905432,2.914195,3.555642,-7.733776,2.772924,0.987634,-3.860180,-0.093896,5.859242,6.425762,6.593720,1.997286,4.914642,-1.513249,-5.523203,3.444335,2.020459,-8.904719,8.928593,6.188200,7.632473,0.173430,-0.886147,8.012912,3.032911,0.705075,3.388255,5.666141,3.332752,-9.362812,-0.126803,-7.118148,-4.646370,-7.107043,0.597659,-8.430952,-0.519901,1.470399,1.156122,8.204161,2.382807,5.846809,7.889172,6.369758,-0.779361,6.567991,6.663164,8.954630,-3.997189,6.802171,7.282645,-9.747367,9.367469,-6.570118,-1.923222,-4.171466,1.946517,-4.338799,-6.608584,3.665242,1.843804,0.501209,4.400232,-6.222758,-3.974938,6.028018,0.264204,3.036950,5.850168,1.009054,4.197862,3.913687,7.214078,-9.973331,8.646049,8.483617,-6.304082,-0.612684,1.752333,6.231395,-6.336428,3.101512,0.132944,0.563236,-3.348300,-4.720571,-6.825440,-5.053879,-2.401020,3.929194,1.278472,-5.908017,1.217174,3.078034,-1.539484,-9.744478,5.299699,-9.877453,-1.000138,-6.543726,5.867166,4.402822,-9.974484,9.295612,-6.576140,5.272440,6.206775,1.934768,-5.954373,4.652622,8.906864,4.833879,8.747635,9.360952,5.370044,8.325732,1.583382,-0.193621,-5.263273,-4.942827,-8.764744,-3.894401,7.062644,-9.645716,-0.097290,-3.372295,9.749354,7.366758,-2.995892,4.604474,-5.649217,-2.710859,2.397503,4.648893,-8.368455,-8.757770,3.570996,8.872624,-4.070543,-6.974406,4.035979,-5.620180,1.728880,-4.661766,6.519662,7.474801,-8.664134,2.328575,1.999114,1.351992,-3.644929,-1.377800,0.317762,-1.303931,-1.283653,-0.601567,-7.642201,-9.323599,-2.579563,7.518813,-5.141577,6.619726,-6.127714,-4.490167,-0.564122,0.339138,7.854571,-4.077564,9.440979,-6.305916,-9.014209,-5.716539,-7.708084,-1.455117,1.429073,-0.120481,-1.969808,-5.386440,-5.379611,-2.605006,-8.143225,4.461580,-9.488781,-9.800755,-2.367438,9.920219,-7.458203,6.578220,-5.163146,6.000918,1.172509,-7.143780,-3.892435,-8.202622,2.163636,2.885974,9.557681,-4.771116,-5.861146,9.281712,5.742240,4.984260,-3.271883,-7.734210,-1.839952,-2.952535,9.675739,-0.172466,3.786062,-8.781545,8.610567,9.422277,-2.094299,-1.826838,-7.026338,-5.797620,-1.096665,5.205754,-8.436392,-3.064519,-1.810299,2.736371,7.363091,1.486043,-8.286806,2.631885,1.217313,-8.650326,-0.169550,-4.113379,3.912936,6.384822,4.455524,-1.380650,-3.603367,-4.708436,-1.857123,5.808402,9.504339,-6.156394,-7.884857,-8.308693,-9.142032,-8.504614,6.758920,-7.985612,4.465939], dtype = "float32")#candidate|4939|(2310,)|const|float32
const_4940 = relay.const([True,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,False], dtype = "bool")#candidate|4940|(880,)|const|bool
call_4938 = relay.TupleGetItem(func_864_call(relay.reshape(const_4939.astype('float32'), [14, 11, 15]), relay.reshape(const_4940.astype('bool'), [880,]), ), 1)
call_4941 = relay.TupleGetItem(func_868_call(relay.reshape(const_4939.astype('float32'), [14, 11, 15]), relay.reshape(const_4940.astype('bool'), [880,]), ), 1)
output = relay.Tuple([call_4928,call_4938,const_4939,const_4940,])
output2 = relay.Tuple([call_4929,call_4941,const_4939,const_4940,])
func_4958 = relay.Function([], output)
mod['func_4958'] = func_4958
mod = relay.transform.InferType()(mod)
output = func_4958()
func_4959 = relay.Function([], output)
mutated_mod['func_4959'] = func_4959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3749_call = mod.get_global_var('func_3749')
func_3750_call = mutated_mod.get_global_var('func_3750')
call_4973 = relay.TupleGetItem(func_3749_call(), 0)
call_4974 = relay.TupleGetItem(func_3750_call(), 0)
func_1269_call = mod.get_global_var('func_1269')
func_1270_call = mutated_mod.get_global_var('func_1270')
call_4980 = relay.TupleGetItem(func_1269_call(), 0)
call_4981 = relay.TupleGetItem(func_1270_call(), 0)
func_1646_call = mod.get_global_var('func_1646')
func_1649_call = mutated_mod.get_global_var('func_1649')
var_4992 = relay.var("var_4992", dtype = "int64", shape = ())#candidate|4992|()|var|int64
call_4991 = relay.TupleGetItem(func_1646_call(relay.reshape(var_4992.astype('int64'), [])), 2)
call_4993 = relay.TupleGetItem(func_1649_call(relay.reshape(var_4992.astype('int64'), [])), 2)
output = relay.Tuple([call_4973,call_4980,call_4991,var_4992,])
output2 = relay.Tuple([call_4974,call_4981,call_4993,var_4992,])
func_5018 = relay.Function([var_4992,], output)
mod['func_5018'] = func_5018
mod = relay.transform.InferType()(mod)
var_5019 = relay.var("var_5019", dtype = "int64", shape = ())#candidate|5019|()|var|int64
output = func_5018(var_5019)
func_5020 = relay.Function([var_5019], output)
mutated_mod['func_5020'] = func_5020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2671_call = mod.get_global_var('func_2671')
func_2672_call = mutated_mod.get_global_var('func_2672')
call_5123 = relay.TupleGetItem(func_2671_call(), 0)
call_5124 = relay.TupleGetItem(func_2672_call(), 0)
output = call_5123
output2 = call_5124
func_5177 = relay.Function([], output)
mod['func_5177'] = func_5177
mod = relay.transform.InferType()(mod)
mutated_mod['func_5177'] = func_5177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5177_call = mutated_mod.get_global_var('func_5177')
call_5178 = func_5177_call()
output = call_5178
func_5179 = relay.Function([], output)
mutated_mod['func_5179'] = func_5179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3796_call = mod.get_global_var('func_3796')
func_3797_call = mutated_mod.get_global_var('func_3797')
call_5212 = relay.TupleGetItem(func_3796_call(), 2)
call_5213 = relay.TupleGetItem(func_3797_call(), 2)
const_5221 = relay.const([[[-2.997198,-0.499253,1.446078,-6.152244,5.052664,0.265409,3.841494,2.175398,2.990972,-6.212344,8.625271,-4.269402,-9.163902,-1.201879,-0.433910]],[[-4.139828,-5.094813,8.863291,5.473967,-0.223484,-9.485030,1.752250,6.953328,3.380351,-0.294600,-0.629242,8.461822,2.653858,-8.447144,4.887516]],[[0.039256,-8.686119,-0.315869,-8.927617,8.757442,-5.955720,-7.632459,2.522185,7.198148,-8.448260,-2.099185,4.091693,-0.988013,8.822119,1.228301]],[[0.150925,3.768546,-7.359521,1.326043,4.282738,4.719606,-8.045860,1.957715,-2.957058,-4.311277,7.673126,1.275651,-9.775340,0.883526,3.286425]],[[6.181469,-7.515000,-6.535035,-6.291325,2.204001,-0.926450,-4.123729,-5.946393,6.514567,-4.784204,-8.608279,-8.941424,-4.444623,7.656298,2.938526]],[[-7.807452,3.064623,8.449506,9.521253,-6.052988,1.062884,-1.152965,2.195616,4.869189,5.408142,7.125932,6.134647,5.892918,-4.915440,-9.174435]],[[4.579695,-1.845706,7.088025,-9.437023,-9.861322,5.518353,-9.554140,0.062535,-4.330788,-7.247122,-5.429307,8.994690,6.424482,2.612329,9.008134]],[[5.757336,1.354093,-9.717023,6.364704,4.266630,7.594655,9.745905,-3.888191,1.976566,-6.641062,-1.856137,8.403562,-9.760945,4.916471,7.394532]],[[1.602468,3.060730,-5.781409,1.042956,2.185735,3.112440,6.810863,-9.085333,6.273804,4.993663,8.360557,-7.410785,5.353391,1.306075,9.994629]],[[-7.623164,-7.547950,0.994683,4.312583,-4.094159,6.414157,0.608752,6.864738,9.623059,3.343010,-7.350997,-1.842893,-6.533771,2.357541,-4.388443]],[[-7.435091,-9.625198,2.559152,8.596820,-6.844782,6.348429,-9.591071,2.798802,-7.645120,-0.329283,8.733223,-5.273560,-3.691193,7.610211,-4.338276]],[[-1.477565,-7.512792,8.543040,-6.856451,-7.995842,8.445070,-4.146224,-9.616701,7.796257,-8.281914,9.363659,-4.112236,-1.243710,-7.442463,-5.897464]],[[1.570850,3.785134,0.683479,1.614127,3.094447,0.207141,4.590357,-2.929766,7.639036,-7.217345,-3.961462,3.068653,3.508651,9.586717,7.284853]],[[4.421481,-5.373003,8.534132,1.122148,7.571302,-3.485568,2.646449,-4.646980,-3.899315,7.581744,-5.142518,-8.005322,-2.430116,9.880324,5.942141]]], dtype = "float32")#candidate|5221|(14, 1, 15)|const|float32
bop_5222 = relay.logical_or(call_5212.astype('bool'), relay.reshape(const_5221.astype('bool'), relay.shape_of(call_5212))) # shape=(14, 1, 15)
bop_5225 = relay.logical_or(call_5213.astype('bool'), relay.reshape(const_5221.astype('bool'), relay.shape_of(call_5213))) # shape=(14, 1, 15)
func_2134_call = mod.get_global_var('func_2134')
func_2137_call = mutated_mod.get_global_var('func_2137')
var_5228 = relay.var("var_5228", dtype = "float32", shape = (420, 1))#candidate|5228|(420, 1)|var|float32
call_5227 = relay.TupleGetItem(func_2134_call(relay.reshape(var_5228.astype('float32'), [420,])), 1)
call_5229 = relay.TupleGetItem(func_2137_call(relay.reshape(var_5228.astype('float32'), [420,])), 1)
bop_5230 = relay.power(var_5228.astype('float32'), bop_5222.astype('float32')) # shape=(14, 420, 15)
bop_5233 = relay.power(var_5228.astype('float32'), bop_5225.astype('float32')) # shape=(14, 420, 15)
output = relay.Tuple([call_5227,bop_5230,])
output2 = relay.Tuple([call_5229,bop_5233,])
func_5263 = relay.Function([var_5228,], output)
mod['func_5263'] = func_5263
mod = relay.transform.InferType()(mod)
mutated_mod['func_5263'] = func_5263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5264 = relay.var("var_5264", dtype = "float32", shape = (420, 1))#candidate|5264|(420, 1)|var|float32
func_5263_call = mutated_mod.get_global_var('func_5263')
call_5265 = func_5263_call(var_5264)
output = call_5265
func_5266 = relay.Function([var_5264], output)
mutated_mod['func_5266'] = func_5266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_5313 = relay.TupleGetItem(func_918_call(), 0)
call_5314 = relay.TupleGetItem(func_920_call(), 0)
output = call_5313
output2 = call_5314
func_5320 = relay.Function([], output)
mod['func_5320'] = func_5320
mod = relay.transform.InferType()(mod)
mutated_mod['func_5320'] = func_5320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5320_call = mutated_mod.get_global_var('func_5320')
call_5321 = func_5320_call()
output = call_5321
func_5322 = relay.Function([], output)
mutated_mod['func_5322'] = func_5322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5349 = relay.var("var_5349", dtype = "float32", shape = (13, 7, 3))#candidate|5349|(13, 7, 3)|var|float32
var_5350 = relay.var("var_5350", dtype = "float32", shape = (13, 7, 3))#candidate|5350|(13, 7, 3)|var|float32
bop_5351 = relay.less(var_5349.astype('bool'), relay.reshape(var_5350.astype('bool'), relay.shape_of(var_5349))) # shape=(13, 7, 3)
bop_5354 = relay.minimum(bop_5351.astype('int16'), relay.reshape(var_5350.astype('int16'), relay.shape_of(bop_5351))) # shape=(13, 7, 3)
output = relay.Tuple([bop_5354,])
output2 = relay.Tuple([bop_5354,])
func_5357 = relay.Function([var_5349,var_5350,], output)
mod['func_5357'] = func_5357
mod = relay.transform.InferType()(mod)
mutated_mod['func_5357'] = func_5357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5357_call = mutated_mod.get_global_var('func_5357')
var_5359 = relay.var("var_5359", dtype = "float32", shape = (13, 7, 3))#candidate|5359|(13, 7, 3)|var|float32
var_5360 = relay.var("var_5360", dtype = "float32", shape = (13, 7, 3))#candidate|5360|(13, 7, 3)|var|float32
call_5358 = func_5357_call(var_5359,var_5360,)
output = call_5358
func_5361 = relay.Function([var_5359,var_5360,], output)
mutated_mod['func_5361'] = func_5361
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5378 = relay.const([[[-9.500564,-3.413600,6.898021,5.035004,5.814055,-2.615013,6.165789,-0.878228,6.712885,-3.332673,3.065600],[9.209375,-5.758940,-8.486449,9.798416,-2.010933,5.689460,-7.064633,8.446768,7.401394,5.343546,-7.047273],[-4.628270,-1.208315,3.678174,-7.684300,9.699424,-3.075439,3.441771,8.835753,-6.598438,-3.329575,7.320266],[-5.552582,-1.600725,9.185103,-9.899202,1.402110,-8.110052,-5.400762,-5.142625,-4.816465,-6.374302,4.799194]],[[3.364316,1.954334,-8.449787,7.031865,-6.497106,7.633809,7.796455,-0.524333,-3.805526,-2.866199,6.718450],[-2.452640,-4.219618,9.545368,4.576352,-0.641928,1.815864,-7.208570,-0.829595,1.848522,6.165114,1.074480],[8.947200,-8.269217,7.736303,0.228585,-9.099865,-7.027221,-7.645594,8.589410,-9.460511,9.472846,0.872572],[-6.443759,1.119988,-5.212351,-6.323787,-2.980678,3.938429,6.331463,5.146318,8.862213,-5.050426,-5.539895]],[[5.848131,-9.421755,-5.267074,-1.354987,1.288443,3.926307,-4.108748,2.751918,3.050365,5.119742,8.721888],[-4.273128,3.476311,-6.668248,7.039993,-1.399673,-6.985543,8.860936,-4.135517,2.180082,-0.711629,4.758735],[-2.449716,7.214432,-6.779446,3.171715,2.871372,-3.793637,6.775745,-3.418884,-4.659523,-8.146921,1.826160],[6.477391,4.993423,8.168753,4.930451,-7.599367,9.120758,1.603106,-1.179995,7.040421,-4.702698,-3.616471]],[[-3.789689,6.720579,-0.894938,-3.756919,7.948719,9.717149,-5.067342,-1.199486,6.495963,2.921039,-7.706383],[-4.493984,1.092606,-2.987754,-3.723745,-3.286676,0.245329,4.048604,0.327988,0.390457,5.095559,8.539212],[2.548426,7.924641,-5.496152,6.929952,0.916742,-7.702685,-3.857668,4.762008,5.708057,0.236678,5.730445],[-1.122709,-2.764013,6.454545,1.466946,7.195253,-6.368677,8.633307,-4.471189,5.571871,4.758101,-8.408381]]], dtype = "float64")#candidate|5378|(4, 4, 11)|const|float64
uop_5379 = relay.log(const_5378.astype('float64')) # shape=(4, 4, 11)
func_864_call = mod.get_global_var('func_864')
func_868_call = mutated_mod.get_global_var('func_868')
const_5396 = relay.const([1.802991,-4.481036,3.495894,-9.886390,-9.211557,-2.314076,1.634073,6.671182,7.900238,9.016663,-9.142075,0.115777,-8.427648,7.029948,-0.828302,-9.725585,-1.306750,2.436153,5.791958,4.374603,-8.740424,4.211787,-4.584733,-8.503918,9.433825,-6.688208,3.186455,7.713922,8.333851,3.246720,-6.308303,-1.174807,-1.873685,-5.718108,6.498197,1.545919,4.307940,8.900088,-4.958226,-2.047106,5.041640,7.286395,-3.318987,2.659680,3.286633,-3.545181,-3.522736,8.735945,-6.448768,-8.902154,7.973377,9.520179,-6.900603,-2.249687,5.410206,7.627979,2.206884,9.769941,2.147216,-9.470870,-3.237765,-7.888407,8.334838,1.306834,-7.835119,6.878949,-1.111485,-5.745920,-9.477346,3.931241,5.526964,-6.818800,9.116369,5.313700,-8.192298,5.021421,-3.458461,-0.856367,2.595943,2.657140,2.707735,2.545319,-4.043241,0.145720,-9.064695,-3.492000,7.150917,2.503906,-5.179350,9.579117,-7.934539,4.705084,3.958246,-6.245598,-4.062843,-6.848126,-9.501548,6.030103,9.579324,2.584354,8.129261,-1.887939,6.108036,9.404811,-9.247265,-6.010044,1.033253,0.667332,8.786386,-6.674795,4.477666,-7.613467,-6.997260,-5.898164,-0.644938,-5.947533,0.605500,-9.822468,-4.380596,9.276876,-1.778224,4.518499,6.909397,-3.797874,-2.084523,-2.889387,5.079724,6.180717,-6.521614,-7.672151,-0.841495,-3.641392,6.873738,-8.148698,-1.905212,-5.094319,7.371776,6.643505,-2.022675,-8.524534,-8.898302,-9.061896,0.798209,5.170105,-2.685664,-1.517166,-8.787143,-8.419562,7.020837,5.173592,-1.867714,-3.487461,2.973299,2.012714,-8.110964,-8.110578,-5.637242,-5.317618,4.481775,-3.901200,6.105319,-7.757100,1.873452,0.467853,9.437300,4.884040,-1.952828,2.121450,3.091935,1.043406,-9.916210,-2.036772,8.264760,-2.600593,-0.201121,-4.411360,1.638403,-9.798075,3.653121,5.200827,-7.923704,0.466390,2.329138,8.748404,3.613905,-5.323862,-6.287555,-3.424114,8.044425,-4.571080,2.099266,-2.312111,1.256057,-8.956103,-6.723600,0.163054,-4.495859,-4.611264,-9.973886,-4.453062,-3.340075,4.820598,7.023552,-3.380505,8.716341,-0.817318,7.281500,0.153396,1.407490,-5.162664,-1.350808,8.620091,-9.448902,-1.546301,7.325831,-1.908217,1.551332,-7.167664,8.223952,7.838795,-1.858786,-2.456718,-7.107063,-4.353389,2.834235,-5.180637,4.876997,-4.139475,2.030391,-1.110220,2.204021,-0.079833,-8.911928,0.095634,-3.285330,-8.912500,-6.571549,-8.064089,8.432305,8.488429,7.710873,-2.537649,0.058113,-4.765648,6.085628,3.123806,5.244743,3.710405,-8.564435,-3.960925,4.502295,7.804184,9.569297,3.003543,8.398214,7.453765,-4.158406,1.051234,-3.072843,-9.985577,-0.725409,-9.238648,0.106151,8.359993,-2.848079,-4.574018,0.006738,3.463525,-3.725754,3.240605,5.568826,-5.021092,-2.384370,8.408238,-5.663727,-3.575895,7.834414,-4.838831,-5.009926,1.239279,1.281162,-7.858978,2.425952,2.882234,-5.010559,4.371111,3.966537,0.401653,9.609932,-0.802844,-8.450819,-4.764359,3.152371,6.788589,8.763537,-9.432383,-9.557068,0.884046,2.479772,2.878655,3.540479,4.303816,2.841064,-9.632683,-2.802812,-4.031061,0.741988,-9.629523,5.529474,-7.846247,-9.321341,-3.540806,0.831861,8.261685,-3.956433,4.846742,3.191941,6.392146,3.749733,-9.690557,-2.774974,8.502695,6.218368,5.771036,7.650022,1.710782,-5.850302,-4.228530,4.889774,-0.201100,2.793831,6.092302,2.804396,3.200921,-5.624222,-1.367652,-5.813378,-2.753314,0.547703,-4.165663,2.684461,7.810963,6.192670,-6.278856,3.660289,6.562401,-7.254605,8.624721,3.474724,-0.980419,-6.631323,-3.125794,-6.499413,8.311450,-7.374733,-4.703766,1.175886,-3.722148,-4.459641,-0.885412,0.018186,-3.640009,-5.171502,6.681281,-8.124072,-5.956623,-6.075324,1.281989,7.938877,4.359147,-7.338896,-8.554061,2.222092,6.287634,2.453235,5.198071,8.275883,-1.965402,3.217639,8.523080,4.345471,6.126345,-0.512400,3.524301,2.178315,-1.774505,-8.476111,8.541901,0.452350,7.431143,-4.142645,1.117322,-2.528728,-4.757957,-8.989555,1.637124,6.198829,5.716088,3.187729,5.251515,1.019066,8.320295,-6.099827,0.043298,0.612894,-0.628491,1.236277,6.794865,3.305698,-5.666154,7.539839,-1.653669,-6.361491,-2.748217,-4.903005,-3.196507,8.156726,6.690581,-2.073339,9.320047,-3.642649,-8.897089,-7.346992,8.569656,3.159371,5.938851,-7.403336,8.423670,0.473480,-9.099989,6.546081,-0.846070,-7.882331,0.886728,-2.522703,-9.494610,-9.518417,1.506503,-4.241859,1.141785,-2.987680,-0.375155,-2.921141,4.406782,-1.929949,1.597798,-9.517971,-6.600758,0.323827,8.972646,6.336810,-5.591841,-0.363341,-6.829582,2.807931,-4.535480,-6.299864,-7.789904,-3.255261,-9.605603,5.693616,5.354838,7.914949,1.984976,3.030787,2.980748,-4.032879,-1.484447,7.865550,-7.355617,-9.392358,-8.913239,5.707649,2.010063,-4.196617,-1.929759,9.220916,6.808906,-4.443146,-5.286392,7.272165,-0.394944,0.245604,9.807553,5.197952,0.094751,-8.056136,-3.401256,-8.434128,-2.508952,8.260037,4.333218,-0.590462,-3.750030,0.676942,-8.357113,-7.695726,-1.412702,6.774298,-6.836649,6.842343,0.872267,6.374328,-7.869742,1.448723,-6.533933,5.164058,-2.040906,-7.624728,-1.779884,4.942604,-6.428674,9.557411,9.183319,-7.612723,8.852935,-2.750068,-9.782307,-6.532014,7.039985,5.860706,9.724161,9.075722,-5.933174,-4.530936,4.207386,3.881472,0.554283,5.208897,8.411288,-8.177990,8.387966,6.594071,-7.805055,-0.830909,-9.797044,9.164585,7.226964,4.747052,-1.576113,-7.588522,5.510118,4.624946,4.668974,7.182896,4.938845,9.037136,-5.930928,-3.666905,8.402985,9.431539,-5.329187,3.700306,1.476713,5.235131,-1.912079,-0.664565,8.381623,-3.958412,-0.422969,8.274883,0.108234,-6.942153,-7.498340,-2.668549,-2.934960,1.452991,-4.304322,-3.024028,9.700477,9.483746,7.184918,3.876448,0.617274,2.394039,5.486470,8.948774,-3.066199,8.484202,-9.054714,-6.597853,7.641656,9.542802,-7.341670,1.975755,0.540733,9.322279,-6.341484,3.343988,-3.249594,2.688711,-6.710868,-8.424877,5.843135,6.884627,2.635405,-0.233725,3.603492,-3.130573,4.618453,3.117215,-7.988523,9.929651,1.590660,-7.804507,-9.197415,2.677136,5.055394,8.477170,9.902166,-0.957292,-1.753052,0.930018,9.525649,2.431803,-7.512608,2.820223,5.978127,0.021064,-4.097301,-3.946383,-3.501593,0.534807,2.454624,-2.409534,6.193424,0.420401,2.516720,1.781993,-2.424772,8.933610,2.547379,0.723726,5.276101,0.662453,-4.889447,-7.331033,9.055160,-4.106122,-3.017505,-9.626059,-2.304865,6.679216,-1.848244,-5.125500,0.160636,0.394835,-6.207812,2.827314,-5.392360,5.693958,-9.999707,3.604228,2.093214,-2.507836,-5.608705,4.898484,-6.672962,-5.701983,7.467797,4.968351,-4.023786,0.504054,5.200780,-1.764798,8.433342,2.655929,-0.200884,-0.447266,-5.186479,4.052714,7.244264,4.109854,-0.873997,-5.477452,-7.411202,-1.773041,3.006331,-2.261651,4.080499,-0.083900,-2.643410,-9.451007,-7.722691,9.425468,-5.809750,4.637640,3.999186,2.931210,-3.801729,-9.405030,-8.806139,6.847442,-4.836064,-5.342908,-1.489147,6.281691,-1.016589,7.925138,-9.101158,-9.030585,-5.682133,-9.234258,-8.141265,7.001354,0.111151,-8.692181,-3.852088,1.214941,4.031148,-4.677718,-3.085758,-7.301624,-6.099662,9.072252,-2.879229,6.485281,6.834325,2.898324,4.070358,-5.084534,-1.319061,-1.242632,-1.749628,0.605416,-8.149307,-3.870613,4.778265,6.397373,-9.841757,-8.521315,-7.543259,7.699379,9.594606,-0.256291,3.452296,-5.480221,1.280725,4.163967,-6.461931,8.764920,-3.316106,-7.495372,-1.816336,6.634802,-6.840796,-3.119163,4.572365,5.279766,-3.890392,-5.710587,-0.040132,0.493569,4.811824,-4.423069,2.255634,-2.834353,7.167515,-8.773426,0.836389,-8.336972,5.844320,-6.476535,0.377631,-8.779385,0.444732,9.278711,0.180893,0.739196,8.899682,-6.077363,7.983930,6.655819,4.831698,6.778723,3.637601,3.472777,-8.588839,-4.473000,4.386173,4.229455,1.334945,-6.757584,2.191187,3.266305,7.175456,8.275006,2.595499,7.678548,-9.166394,7.603303,4.994680,3.169360,-4.928907,6.909859,-3.391399,1.650325,2.159629,-5.186637,4.454480,-8.374018,2.749013,-6.295406,-9.577617,-4.018244,-7.708151,-8.036999,-3.196171,9.075675,6.430657,-2.409811,7.318096,8.548854,3.705357,8.448087,-6.427737,-9.504826,6.843970,-1.802230,-9.292824,9.748327,-7.933069,-7.240242,8.979559,2.769101,-6.307641,-2.342584,3.253867,7.931983,2.212737,-8.361123,-7.753235,2.035649,4.894737,9.601979,-3.283995,-0.275488,-9.561359,8.571932,-5.502740,8.663017,-2.591290,-7.143203,5.946024,5.347702,-9.827755,-4.607892,-9.853976,-1.931563,4.865014,2.449881,-3.376289,-3.749584,8.044416,-5.231712,5.155601,-5.105352,2.703306,9.963379,-7.859027,3.234554,-2.526489,6.725669,-8.419434,-7.606104,9.310809,8.322094,9.257152,3.641002,-6.830300,-7.465970,6.437278,0.291366,8.551503,2.046301,8.192742,-7.411888,3.677131,-9.060817,-3.676997,0.351447,1.924234,5.775391,6.956967,0.293725,9.611709,9.445596,-5.749770,9.438044,4.983272,-1.417675,-6.526819,4.997971,-9.114005,6.928119,-8.121812,1.379936,3.092623,9.001767,4.433185,-2.320845,-6.720611,3.451218,6.137022,5.393809,9.930576,9.087311,-5.151529,2.798032,2.442111,8.809937,-4.031983,7.580709,-9.854335,-1.552213,9.913121,-9.335792,-5.430549,-4.303266,-3.781318,-0.735987,0.820017,6.928340,-9.760359,0.160981,5.941219,-0.187828,9.990585,-8.830275,-1.495490,9.694750,8.846495,4.121097,3.091313,4.603073,4.867330,0.833314,-9.481735,2.336673,-1.109840,-5.729158,7.566026,0.792588,-5.577335,-2.576093,-4.032534,-0.142311,5.965090,7.525120,4.350595,5.952490,-7.423649,-6.671292,4.895245,-5.886139,-4.921515,-4.791625,1.508864,-7.076392,7.240003,-3.803509,-5.827183,9.204975,-2.849484,-0.508017,-5.751260,9.864692,-5.449823,7.836827,9.927894,5.254903,-9.087717,1.511216,4.959497,5.425662,5.256014,-4.441001,-6.488465,0.840587,-8.730698,-3.091101,0.484638,-8.489321,9.169296,-3.445198,0.224475,-1.393843,9.471951,1.206715,3.477597,8.295131,-5.938800,-3.123066,8.191775,9.001857,4.375400,-9.643409,9.795733,8.693895,-4.315753,6.431850,6.662004,1.087094,-0.083554,-3.902728,4.140293,-7.686605,3.527892,-6.272928,-8.537323,0.111157,-5.445402,6.752041,-5.569367,-6.226815,-1.453569,-1.704250,-1.127996,-6.390802,-0.349527,-3.538420,-3.659384,5.618010,-2.185426,-0.542144,8.048160,-2.337321,-1.853372,-2.595037,-4.897382,5.172445,-8.923853,9.041168,-8.711586,6.089863,-7.363895,-4.409098,-5.374581,-2.614638,-1.860006,-0.229371,-6.495568,3.749132,-1.816394,6.355599,-4.949211,7.589635,-4.292736,7.858475,-6.260635,0.323634,8.911880,5.859303,1.705472,-1.488982,-3.704055,-9.647509,7.156641,0.629792,3.191704,7.821309,-0.813151,-9.209445,2.622754,9.573693,7.383429,-3.076214,-3.100076,-3.940008,8.155631,6.236271,2.206855,7.729172,8.665609,-5.556474,2.656194,5.839501,-7.732387,2.909372,3.627660,8.350187,8.537898,0.138773,8.923830,-0.425186,-4.343923,2.225665,5.184338,4.137543,5.062730,4.005552,7.310446,-3.729130,-3.863014,0.151261,-8.378356,-9.366724,-1.177743,-6.996361,-5.749644,-3.823680,-2.627131,-8.041372,-9.044415,9.105483,-0.296515,6.129094,6.775315,3.445654,0.508520,7.174136,-7.293772,2.326013,-4.653628,-3.678490,-2.472389,8.155885,-1.110950,-1.097293,3.768848,4.787004,-8.683921,0.636492,-7.128243,-8.315989,1.144965,-8.430818,7.572555,-9.106275,5.286742,-7.074639,-7.772707,-1.017747,-8.106057,4.891653,-9.775501,9.613928,6.310346,-5.720590,0.535382,2.407583,7.313802,-1.052874,-8.454715,-3.720596,-3.155059,8.088941,-9.267260,1.087068,1.625527,6.679352,8.748370,-9.919809,0.533326,7.434383,1.040573,-3.466879,-8.788407,-3.412421,5.655714,-5.611942,6.113795,-5.380109,6.875803,-5.106500,6.454537,6.735827,-1.011135,5.682664,-2.307460,8.658536,-9.325186,-4.574849,-8.763604,4.299945,3.773934,6.329585,9.866047,2.719896,-7.012902,9.463029,3.205761,-8.715723,0.280223,5.091994,-2.764966,1.150761,-8.434373,5.366852,-9.747394,2.992322,-7.357574,2.332575,-1.730619,2.787945,-3.971760,-8.971365,8.179294,-6.860812,2.060357,-6.701027,-3.337769,-4.754768,-8.268068,7.839236,-0.589666,-3.269338,-3.266348,-4.727718,-1.836695,7.676871,6.421655,-4.761430,-5.244028,5.414452,9.464669,-5.406599,5.342494,-8.697886,-6.431799,4.569213,-3.628718,-8.840898,8.621157,-3.519507,-7.467461,-6.139836,4.071337,-3.337949,4.211963,5.725484,4.800745,-6.682557,-0.083849,-9.276325,1.263502,1.659530,-7.669794,-0.770233,1.101147,7.994768,-9.858158,1.938100,1.684453,7.690002,2.267852,9.606268,-4.354874,8.479625,-0.233447,-2.523452,7.414316,-0.731108,1.220829,1.266607,6.602686,-2.044506,9.469810,9.644953,3.756335,3.212129,-2.647543,2.649005,2.996510,6.558697,4.424261,2.968621,-3.150815,-2.702305,-1.066375,-1.787503,-1.435784,4.087359,-2.259061,-2.960177,3.838029,-7.409931,-1.455544,6.355438,-2.232239,-8.049253,-0.606495,1.651542,5.400649,-8.427075,8.716984,8.286441,1.062117,4.039688,2.565288,8.047875,-5.457025,-1.534342,3.139923,-5.221379,2.344959,5.660846,-4.762513,-7.768041,-2.675654,9.196132,9.518843,-4.968545,6.224499,-1.864546,5.127291,4.018219,2.244322,8.031721,4.321586,-2.633230,-8.438199,-6.208585,-2.438170,-5.021633,1.741500,9.728202,-5.882115,6.966481,3.330465,-9.612417,8.086001,-8.581902,-3.545980,-2.725390,7.859651,-5.587661,-2.807193,-4.994341,4.895541,-5.239763,-8.098406,4.589126,2.363051,-4.169615,-8.898995,0.224057,3.544018,-2.483512,2.307941,6.450089,3.864003,-6.973338,9.239190,1.173959,5.285152,8.293307,5.388621,-5.991602,-1.346090,3.287191,-4.110652,-0.811767,4.686668,2.413240,7.289285,2.905314,-8.851961,2.003275,9.857922,-4.088726,-2.231476,-8.939898,-3.550958,-1.322511,-9.628138,8.541834,-7.281888,-8.121358,-7.112323,3.237157,-1.867087,-7.317911,-3.366254,-8.327980,-9.415693,0.252465,4.619967,-0.607917,-3.925517,-3.515401,3.337465,2.598182,1.365567,2.268800,6.950150,-1.995279,7.029742,-2.513665,-7.028950,6.293893,9.442681,6.314389,0.135538,-5.017676,-3.329271,-3.844789,-4.910623,6.956997,4.431746,5.335062,4.819749,-6.158466,6.915597,3.565292,-9.085900,-8.257002,3.877105,-1.580364,-9.486305,-9.347703,4.570520,-5.210843,4.134023,0.782833,-1.921607,2.745197,-5.783853,-4.402106,6.250938,5.528506,3.740689,7.276577,3.947298,1.229062,6.057872,-3.697575,-4.908053,-5.663215,8.021527,-3.451620,6.742212,8.442615,4.401833,5.746261,3.392505,-0.011540,-8.175288,1.144454,4.045521,3.390817,8.233408,4.931925,-5.483632,8.191481,-8.872977,1.784490,3.951234,6.727795,6.491273,1.673256,-7.558561,6.441991,-3.458595,-4.485393,9.612039,-3.217522,-8.566474,-4.138345,8.242267,-9.660107,2.778785,4.035502,-5.237471,2.115184,7.676040,1.395783,7.664960,5.848330,2.384279,9.754632,4.231576,7.991088,-8.137460,2.287942,8.054687,6.938275,4.697770,-3.579389,5.261617,2.085979,-4.690384,-7.756916,4.705491,1.669527,-5.022349,3.379942,-6.320853,3.381885,-6.288903,6.462421,-2.878428,-5.717081,9.906332,6.474124,6.033299,-3.684440,8.851641,5.079650,-4.455106,-6.084578,1.022536,-0.472935,-8.618874,-8.528688,-1.020384,5.727940,-0.075661,3.729073,-2.318497,4.073900,9.227100,1.684382,-6.754324,-3.100733,-5.987531,8.244900,-2.293668,1.954791,3.863143,-0.394108,0.921304,-8.207980,0.384821,-3.699631,2.079917,6.255626,7.305251,3.005132,0.919484,-7.881724,-2.256860,-9.820981,4.991079,-6.654811,2.326053,3.224663,-6.181002,3.496284,2.780336,2.977665,1.765451,3.426051,3.431008,-0.290271,-1.023477,-1.705564,6.720505,-6.877656,1.571900,2.937379,1.571457,4.902110,6.500692,6.705872,-0.898980,4.057079,-8.374492,-6.482392,4.641135,-9.964673,4.220050,0.001610,7.226055,-9.798218,-3.626912,-4.557199,-0.677644,2.217565,-8.261397,-2.915389,6.644785,-8.725373,-2.393930,6.601913,4.135418,-3.595719,3.790900,3.326091,1.843470,2.780264,-9.584393,8.638963,7.688299,-2.724923,5.659114,0.351697,-6.177509,-6.927161,-8.367385,-3.652167,-0.967011,7.224176,-4.067752,-6.740985,-3.120462,2.279120,5.039797,0.717865,7.343175,-0.453988,-6.838116,1.002391,7.016871,2.366708,-1.016580,-0.019559,-0.626178,-7.068144,-8.373100,-3.951467,-8.886913,0.505266,-3.841741,-3.225427,-4.557102,6.847753,-6.300208,8.901035,-3.383805,-3.095600,6.771867,8.658014,-2.243840,-2.756015,9.640025,5.385398,8.210827,7.942621,6.695080,0.328283,1.245264,-1.676714,-7.744385,9.182615,-0.726268,1.050219,-5.704404,-3.190465,-8.831682,-9.428057,3.788525,1.496796,-7.329665,9.407017,-2.395585,-6.855673,8.299360,-8.490080,-3.471434,-7.285005,4.066370,-9.090165,7.016580,-0.778092,-8.093179,1.686230,-9.223375,-5.197605,1.006836,-8.369892,-0.524001,8.814898,3.145903,4.989410,-1.428713,-0.589093,5.982549,3.330489,1.887957,-0.917174,-7.613017,-1.566631,-3.388250,-3.624009,-8.308146,-3.237103,5.731372,-7.570580,7.024370,-9.707359,7.427868,5.768124,-5.143909,5.837383,-1.751724,5.128151,8.963774,2.503582,-0.540258,-3.213562,-9.089643,2.727573,-0.914223,-1.515244,-7.088223,3.524889,2.211129,-5.932817,-7.686021,-8.645495,-9.158407,9.023981,7.603273,5.271002,-6.726326,-3.102713,-6.245454,-5.637053,9.656452,-2.447799,-7.567886,6.119083,-3.033889,6.662386,-6.858523,4.407695,0.784007,-0.871816,3.134055,-9.789334,2.803011,-3.708286,-8.953368,8.560307,1.364117,9.011584,4.544757,-3.396231,0.008867,-2.744009,4.905348,-4.647505,6.383922,8.409624,-4.224306,-5.222953,-1.255410,-7.542406,-8.004428,-1.940947,6.777991,8.004929,-7.209955,5.258361,7.854182,4.030825,8.926289,4.538462,5.345850,-1.983583,-9.878866,8.960928,6.510312,3.713685,0.656049,-8.352168,-8.484319,-9.795659,4.850740,-2.045138,2.672377,9.605973,9.405425,3.457302,0.660323,-8.704394,6.152594,-7.642825,5.213787,-1.718541,3.128209,-6.063524,-0.618010,-8.092526,-8.343700,-7.847163,8.744686,-4.744376,-8.476705,4.388223,0.721433,6.665578,2.299456,-8.430437,8.560482,-5.008145,9.959027,-0.173680,2.552743,7.194542,9.728438,9.202516,0.939705,5.006148,-6.376596,9.036330,1.660529,-9.578329,-6.411614,0.147527,9.335040,-5.350790,-2.790791,-0.606032,3.643884,6.811580,2.067914,7.905402,8.156600,-4.066135,9.667679,2.016814,-8.798671,-0.035233,-4.950574,-5.698385,7.885474,-5.918654,-4.612392,3.383219,-9.733505,-5.910933,8.762250,-9.289052,5.626514,-4.001525,-7.915862,1.464539,4.286280,9.444679,8.512927,8.983984,-6.760034,2.001188,-3.279122,0.719682,5.767328,-9.565085,2.348493,9.845357,3.332039,-0.375155,-1.390081,-4.400576,4.366804,1.230588,-8.920901,8.109250,7.744280,7.519229,3.558413,-7.662631,-4.744129,6.747602,-4.351898,-7.379849,9.775223,1.932314,-3.135137,3.413854,-5.617490,7.310086,-7.529251,6.464118,5.147634,4.721429,2.940439,4.264580,1.427160,-5.275795,-0.751643,7.909821,4.420114,2.157652,8.387749,7.948986,2.865074,-2.679515,4.745449,8.780013,-6.064767,7.191068,5.805046,7.357522,0.023114,-0.219956,1.561713,7.741067,-0.574057,-0.310331,-7.576405,8.827735,-2.707653,4.527145,-7.564733,-6.936708,3.955091,-3.317454,9.197994,6.850073,0.852316,-4.745462,-5.165380,2.616046,-4.095118,-7.151663,5.932250,-2.172889,6.640270,7.556836,0.506860,-8.952844,3.203501,8.916801,-0.704767,-5.724295,-1.434351,-0.247508,-8.583410,3.453491,-7.836142,8.060863,-1.463893,8.718958,9.049074,8.768048,3.531344,-9.525039,-9.005925,5.203376,-7.205233,0.923557,-7.899725,1.514232,3.063607,7.138937,-9.222171,-6.424299,-5.894844,-6.857919,-4.041504,-7.263893,0.137142,9.981264,-7.818812,2.859231,-8.723845,9.071073,-7.282324,2.654839,-8.457316,0.594071,-1.346036,2.358677,-0.509166,-0.494821,1.755756,-4.974985,9.514229,-4.028856,-3.076704,8.969561,-0.863547,9.125427,6.924934,9.446768,2.540755,6.854285,-4.815810,-6.453846,-1.513831,5.429351,-0.269411,4.046387,2.183215,6.114595,7.594959,-5.957256,-3.035608,-9.032552,2.073338,8.851530,0.869548,-6.748113,0.052540,-8.829756,4.991158,2.260785,1.134568,-1.848860,-4.262793,-1.998159,-0.926821,-3.219085,-6.322262,-5.167291,-9.251924,-6.989067,-8.115434,8.702703,3.719684,-2.690411,1.342608,-4.602557,-7.923703,-5.459374,3.203716,-5.554875,3.655422,-8.317608,2.671995,9.296101,-4.151096,4.301767,-7.020174,-2.962861,-8.155277,3.613905,-7.529553,-1.255586,-2.716806,5.319135,2.179254,1.142442,-0.750799,-9.137017,-0.766490,4.630916,6.487446,-0.123819,9.313660,-7.846421,9.515981,-0.051632,3.853226,-4.810024,2.932882,6.312236,8.531272,6.261509,-4.702854,9.724872,-0.634592,6.550450,-6.461354,5.581493,-3.514880,7.526946,8.466034,4.368345,3.024293,-1.227650,-3.251861,2.383676,-5.496860,8.154089,0.454824,-2.312768,-4.586122,9.712050,2.628140,-4.500138,-6.215019,8.550669,8.208897,2.957357,-2.339814,9.551732,9.984448,-3.815535,-0.363202,6.262572,-5.722587,0.113679,0.743151,7.015475,5.548457,0.850609,-5.766675,-7.899670,1.352032,-6.452962,7.249435,-2.257930,-0.788404,0.106736,5.405020,-0.276339,-1.831079,-8.305271,3.869414,-8.297412,0.791211,-3.735073,-2.208874,-6.042169,-0.726648,7.619653,-6.973869,2.273983,-3.921331,6.738711,3.790142,0.136925,0.441982,8.908928,-7.817403,-8.884988,2.844841,4.794668,0.359440,-0.666457,-0.623469,9.460967,1.344100,7.216333,6.044493,9.641848,2.715589,-7.044950,-6.573300,0.104414,6.203036,1.841319,-3.411781,-2.158965,-1.265491,-3.586537,-8.929791,0.733819,-3.415378,1.267550,-5.571001,-0.202922,-8.891851,-6.953044,-4.325114,8.310305,4.545601,7.311299,7.221300,6.070073,-3.394279,-1.628843,-0.030395,-3.285340,-3.794990,-5.620783,1.989129,-6.461321,-7.271336,-7.853203,-0.083297,-3.811869,-7.789465,-8.686552,-4.602110,5.456563,0.499028,2.323093,-4.171859,-7.083297,-4.732791,6.574603,2.189062,7.768921,-5.478638,-9.994357,5.381914,7.356531,-3.028804,6.283279,6.238076,8.611863,-7.364348,-1.447139,6.625669,2.918729,-2.887685,3.038344,3.918469,0.559273,-3.053803,-4.931882,-9.988840,-3.938559,1.888410,0.979323,-7.957765,1.067603,-4.702550,8.627607,-4.667494,7.747196,0.393544,-3.409627,7.738177,0.509056,-8.789380,5.979806,8.255809,1.619116,7.508752,9.044216,-7.202299,-9.022981,4.457717,-2.570247,-7.017621,-7.996182,-6.204544,-7.691856,-9.678340,2.585543,-2.375898,7.741991,-7.612520,-0.710330,-7.742368,-8.653884,1.577014,4.629189,-8.103374,-8.492150,4.821714,0.585339,-6.708770,8.636576,8.449761,3.767882,5.295389,2.401049,5.316840,4.152076,7.269669,-9.076932,-6.615191,2.683924,3.726573,4.596111,-4.402856,-9.167825,5.152368,2.363173,8.100307,-3.307277,-0.259235,-6.836072,4.416676,7.048995,5.205900,5.085526,5.168255,7.465653,8.439709,0.398594,4.062234,-0.152626,1.536444,7.795693,-8.326123,8.798594,3.409246,-2.778290,1.228844,0.093211,-0.712890,-1.706811,-8.327517,-6.944430,-0.633310,3.286924,-7.010307,-9.873303,-6.511493,-3.455674,6.778880,4.180871,6.321784,-6.388962,8.798115,-6.032241,-3.565799,1.518146,-5.467173,-1.479626,5.261898,-3.896426,1.633832,3.126083,-4.917540,-7.446188,7.733227,-3.479372,-2.184200,3.009605,-6.407191,6.535002,-0.873509,4.486643,-4.264163,2.039253,-5.216693,8.994978,6.602638,3.932755,-5.314793,5.924494,7.694443], dtype = "float32")#candidate|5396|(2310,)|const|float32
const_5397 = relay.const([[True,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False],[False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,True,True]], dtype = "bool")#candidate|5397|(2, 440)|const|bool
call_5395 = relay.TupleGetItem(func_864_call(relay.reshape(const_5396.astype('float32'), [14, 11, 15]), relay.reshape(const_5397.astype('bool'), [880,]), ), 2)
call_5398 = relay.TupleGetItem(func_868_call(relay.reshape(const_5396.astype('float32'), [14, 11, 15]), relay.reshape(const_5397.astype('bool'), [880,]), ), 2)
func_4315_call = mod.get_global_var('func_4315')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_5404 = relay.TupleGetItem(func_4315_call(), 0)
call_5405 = relay.TupleGetItem(func_4317_call(), 0)
func_421_call = mod.get_global_var('func_421')
func_422_call = mutated_mod.get_global_var('func_422')
call_5426 = func_421_call()
call_5427 = func_421_call()
output = relay.Tuple([uop_5379,call_5395,const_5396,const_5397,call_5404,call_5426,])
output2 = relay.Tuple([uop_5379,call_5398,const_5396,const_5397,call_5405,call_5427,])
func_5430 = relay.Function([], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
output = func_5430()
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3162_call = mod.get_global_var('func_3162')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_5438 = relay.TupleGetItem(func_3162_call(), 3)
call_5439 = relay.TupleGetItem(func_3163_call(), 3)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_5451 = relay.const([False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True], dtype = "bool")#candidate|5451|(880,)|const|bool
call_5450 = relay.TupleGetItem(func_54_call(relay.reshape(const_5451.astype('bool'), [11, 10, 8]), relay.reshape(const_5451.astype('bool'), [11, 10, 8]), ), 1)
call_5452 = relay.TupleGetItem(func_57_call(relay.reshape(const_5451.astype('bool'), [11, 10, 8]), relay.reshape(const_5451.astype('bool'), [11, 10, 8]), ), 1)
output = relay.Tuple([call_5438,call_5450,const_5451,])
output2 = relay.Tuple([call_5439,call_5452,const_5451,])
func_5455 = relay.Function([], output)
mod['func_5455'] = func_5455
mod = relay.transform.InferType()(mod)
mutated_mod['func_5455'] = func_5455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5455_call = mutated_mod.get_global_var('func_5455')
call_5456 = func_5455_call()
output = call_5456
func_5457 = relay.Function([], output)
mutated_mod['func_5457'] = func_5457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_5467 = relay.TupleGetItem(func_918_call(), 0)
call_5468 = relay.TupleGetItem(func_920_call(), 0)
func_4315_call = mod.get_global_var('func_4315')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_5474 = relay.TupleGetItem(func_4315_call(), 0)
call_5475 = relay.TupleGetItem(func_4317_call(), 0)
output = relay.Tuple([call_5467,call_5474,])
output2 = relay.Tuple([call_5468,call_5475,])
func_5496 = relay.Function([], output)
mod['func_5496'] = func_5496
mod = relay.transform.InferType()(mod)
output = func_5496()
func_5497 = relay.Function([], output)
mutated_mod['func_5497'] = func_5497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_5510 = relay.TupleGetItem(func_1550_call(), 0)
call_5511 = relay.TupleGetItem(func_1551_call(), 0)
func_2053_call = mod.get_global_var('func_2053')
func_2054_call = mutated_mod.get_global_var('func_2054')
call_5522 = relay.TupleGetItem(func_2053_call(), 0)
call_5523 = relay.TupleGetItem(func_2054_call(), 0)
output = relay.Tuple([call_5510,call_5522,])
output2 = relay.Tuple([call_5511,call_5523,])
func_5529 = relay.Function([], output)
mod['func_5529'] = func_5529
mod = relay.transform.InferType()(mod)
mutated_mod['func_5529'] = func_5529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5529_call = mutated_mod.get_global_var('func_5529')
call_5530 = func_5529_call()
output = call_5530
func_5531 = relay.Function([], output)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5601 = relay.const([[[1.278897,-3.077846,8.160382],[1.713979,-8.174895,2.917192],[-1.952038,6.657062,3.306215],[-9.562401,5.968318,-0.033685],[-1.643771,-7.601760,-4.650546],[-0.151369,-1.627209,6.546767]],[[0.068879,-3.762002,-3.278365],[-4.075214,-8.585537,-7.121921],[-3.274992,-1.499921,0.094142],[-3.506675,8.801670,1.693107],[-4.154954,9.638877,-2.294840],[-4.044836,5.381766,-5.227343]],[[-0.035663,3.898999,-1.232542],[5.883175,-4.255458,-1.093875],[-1.464033,9.504261,-4.144403],[0.207597,-6.946281,0.043562],[5.532803,-2.921529,-5.287155],[2.433634,6.544151,5.152270]],[[-2.945868,-7.218707,-3.841659],[-6.464093,3.420403,-1.127461],[8.264278,-7.045851,3.633815],[-2.009451,6.413072,7.348059],[4.043360,3.926104,1.501963],[9.620198,9.181868,-2.203928]],[[-6.230899,-1.020296,6.105769],[4.534120,5.864742,-2.369472],[-6.493254,2.019784,-3.477656],[3.417893,5.589370,-1.021407],[-2.148380,-7.331177,-6.478584],[8.703679,-5.518032,-8.795728]],[[6.328612,-4.102155,-0.807322],[3.574964,0.138296,-0.940221],[9.934454,-9.422922,-6.704474],[-3.582647,-9.676663,-7.911896],[4.826806,1.527892,-7.757540],[5.294059,-9.288405,-3.079607]],[[4.243162,0.794037,-8.328689],[-9.140194,7.793201,2.849820],[8.404944,-5.250528,-1.812740],[-2.343580,2.454665,0.167486],[-5.700897,6.791059,-0.048589],[2.494049,2.979645,9.785088]],[[-9.954483,9.311513,-7.367486],[-3.478364,-6.512089,3.873308],[7.038823,8.472156,3.204168],[-5.181706,2.670481,-2.775475],[3.085090,0.618856,-3.398414],[5.727578,-0.884812,7.168979]],[[5.532603,6.617426,-5.390343],[-3.511881,-7.290947,-8.984652],[5.780482,1.182299,-9.899239],[-1.641853,5.809023,-6.705994],[-5.685572,0.333957,6.114393],[8.671993,-5.012842,-4.313458]],[[4.138696,-8.384199,-5.941459],[-5.180745,-0.502734,8.549568],[5.689520,-8.744304,4.463941],[2.494545,-4.158811,6.132361],[0.593900,-7.119081,8.589890],[-1.097552,-1.110546,-1.183843]],[[-4.836098,-5.207099,8.031573],[3.744512,1.109369,9.442950],[2.023895,2.965446,1.440833],[6.752589,8.014333,-2.912269],[-8.405429,-0.387069,-2.067005],[-4.280578,1.843635,7.673940]]], dtype = "float64")#candidate|5601|(11, 6, 3)|const|float64
var_5602 = relay.var("var_5602", dtype = "float64", shape = (11, 6, 3))#candidate|5602|(11, 6, 3)|var|float64
bop_5603 = relay.floor_divide(const_5601.astype('float64'), relay.reshape(var_5602.astype('float64'), relay.shape_of(const_5601))) # shape=(11, 6, 3)
output = bop_5603
output2 = bop_5603
func_5617 = relay.Function([var_5602,], output)
mod['func_5617'] = func_5617
mod = relay.transform.InferType()(mod)
mutated_mod['func_5617'] = func_5617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5618 = relay.var("var_5618", dtype = "float64", shape = (11, 6, 3))#candidate|5618|(11, 6, 3)|var|float64
func_5617_call = mutated_mod.get_global_var('func_5617')
call_5619 = func_5617_call(var_5618)
output = call_5619
func_5620 = relay.Function([var_5618], output)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5648 = relay.var("var_5648", dtype = "int64", shape = (15, 7, 11))#candidate|5648|(15, 7, 11)|var|int64
var_5649 = relay.var("var_5649", dtype = "int64", shape = (15, 7, 11))#candidate|5649|(15, 7, 11)|var|int64
bop_5650 = relay.logical_xor(var_5648.astype('int64'), relay.reshape(var_5649.astype('int64'), relay.shape_of(var_5648))) # shape=(15, 7, 11)
uop_5653 = relay.acosh(bop_5650.astype('float32')) # shape=(15, 7, 11)
bop_5667 = relay.minimum(bop_5650.astype('uint32'), relay.reshape(uop_5653.astype('uint32'), relay.shape_of(bop_5650))) # shape=(15, 7, 11)
output = relay.Tuple([bop_5667,])
output2 = relay.Tuple([bop_5667,])
func_5670 = relay.Function([var_5648,var_5649,], output)
mod['func_5670'] = func_5670
mod = relay.transform.InferType()(mod)
var_5671 = relay.var("var_5671", dtype = "int64", shape = (15, 7, 11))#candidate|5671|(15, 7, 11)|var|int64
var_5672 = relay.var("var_5672", dtype = "int64", shape = (15, 7, 11))#candidate|5672|(15, 7, 11)|var|int64
output = func_5670(var_5671,var_5672,)
func_5673 = relay.Function([var_5671,var_5672,], output)
mutated_mod['func_5673'] = func_5673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3663_call = mod.get_global_var('func_3663')
func_3664_call = mutated_mod.get_global_var('func_3664')
call_5701 = relay.TupleGetItem(func_3663_call(), 1)
call_5702 = relay.TupleGetItem(func_3664_call(), 1)
func_4450_call = mod.get_global_var('func_4450')
func_4452_call = mutated_mod.get_global_var('func_4452')
call_5708 = relay.TupleGetItem(func_4450_call(relay.reshape(call_5701.astype('float64'), [3360,])), 2)
call_5709 = relay.TupleGetItem(func_4452_call(relay.reshape(call_5701.astype('float64'), [3360,])), 2)
func_3663_call = mod.get_global_var('func_3663')
func_3664_call = mutated_mod.get_global_var('func_3664')
call_5725 = relay.TupleGetItem(func_3663_call(), 0)
call_5726 = relay.TupleGetItem(func_3664_call(), 0)
output = relay.Tuple([call_5701,call_5708,call_5725,])
output2 = relay.Tuple([call_5702,call_5709,call_5726,])
func_5744 = relay.Function([], output)
mod['func_5744'] = func_5744
mod = relay.transform.InferType()(mod)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5744_call = mutated_mod.get_global_var('func_5744')
call_5745 = func_5744_call()
output = call_5745
func_5746 = relay.Function([], output)
mutated_mod['func_5746'] = func_5746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3055_call = mod.get_global_var('func_3055')
func_3057_call = mutated_mod.get_global_var('func_3057')
call_5758 = relay.TupleGetItem(func_3055_call(), 0)
call_5759 = relay.TupleGetItem(func_3057_call(), 0)
output = relay.Tuple([call_5758,])
output2 = relay.Tuple([call_5759,])
func_5774 = relay.Function([], output)
mod['func_5774'] = func_5774
mod = relay.transform.InferType()(mod)
mutated_mod['func_5774'] = func_5774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5774_call = mutated_mod.get_global_var('func_5774')
call_5775 = func_5774_call()
output = call_5775
func_5776 = relay.Function([], output)
mutated_mod['func_5776'] = func_5776
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5783 = relay.const([[[2.901011,3.422924,2.263618],[1.016057,-2.852183,5.436444],[-5.306186,-7.455815,-6.817596],[-8.934990,1.270882,-2.494325],[0.245759,-8.860231,-0.510563],[-1.687889,2.863810,9.491915],[6.447558,-0.499485,3.103286],[7.597490,0.922673,-6.218538],[6.613458,-7.610893,6.499825]]], dtype = "float64")#candidate|5783|(1, 9, 3)|const|float64
uop_5784 = relay.sqrt(const_5783.astype('float64')) # shape=(1, 9, 3)
uop_5793 = relay.cosh(uop_5784.astype('float32')) # shape=(1, 9, 3)
output = relay.Tuple([uop_5793,])
output2 = relay.Tuple([uop_5793,])
func_5798 = relay.Function([], output)
mod['func_5798'] = func_5798
mod = relay.transform.InferType()(mod)
output = func_5798()
func_5799 = relay.Function([], output)
mutated_mod['func_5799'] = func_5799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_630_call = mod.get_global_var('func_630')
func_631_call = mutated_mod.get_global_var('func_631')
call_5806 = func_630_call()
call_5807 = func_630_call()
func_602_call = mod.get_global_var('func_602')
func_604_call = mutated_mod.get_global_var('func_604')
const_5821 = relay.const([[-9.319279,-5.812275],[8.960418,-9.136054],[-4.023149,2.185617],[1.892325,1.391383],[-7.699600,-0.707100],[4.472264,-2.231737],[-9.540369,6.250875],[6.947094,-3.730526],[6.420661,-7.433805],[-2.211079,1.917180],[-6.619959,-4.505559],[6.504670,1.645590],[2.802799,9.170114],[9.771949,7.957653],[1.632778,-4.481543],[1.571333,-8.581361],[4.862564,3.797171],[-3.499315,-2.181450]], dtype = "float64")#candidate|5821|(18, 2)|const|float64
call_5820 = relay.TupleGetItem(func_602_call(relay.reshape(const_5821.astype('float64'), [9, 4, 1])), 0)
call_5822 = relay.TupleGetItem(func_604_call(relay.reshape(const_5821.astype('float64'), [9, 4, 1])), 0)
output = relay.Tuple([call_5806,call_5820,const_5821,])
output2 = relay.Tuple([call_5807,call_5822,const_5821,])
func_5827 = relay.Function([], output)
mod['func_5827'] = func_5827
mod = relay.transform.InferType()(mod)
mutated_mod['func_5827'] = func_5827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5827_call = mutated_mod.get_global_var('func_5827')
call_5828 = func_5827_call()
output = call_5828
func_5829 = relay.Function([], output)
mutated_mod['func_5829'] = func_5829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4553_call = mod.get_global_var('func_4553')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_5953 = func_4553_call()
call_5954 = func_4553_call()
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_5963 = relay.TupleGetItem(func_3216_call(), 0)
call_5964 = relay.TupleGetItem(func_3217_call(), 0)
output = relay.Tuple([call_5953,call_5963,])
output2 = relay.Tuple([call_5954,call_5964,])
func_5981 = relay.Function([], output)
mod['func_5981'] = func_5981
mod = relay.transform.InferType()(mod)
mutated_mod['func_5981'] = func_5981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5981_call = mutated_mod.get_global_var('func_5981')
call_5982 = func_5981_call()
output = call_5982
func_5983 = relay.Function([], output)
mutated_mod['func_5983'] = func_5983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2688_call = mod.get_global_var('func_2688')
func_2690_call = mutated_mod.get_global_var('func_2690')
call_6004 = relay.TupleGetItem(func_2688_call(), 1)
call_6005 = relay.TupleGetItem(func_2690_call(), 1)
output = call_6004
output2 = call_6005
func_6014 = relay.Function([], output)
mod['func_6014'] = func_6014
mod = relay.transform.InferType()(mod)
output = func_6014()
func_6015 = relay.Function([], output)
mutated_mod['func_6015'] = func_6015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3055_call = mod.get_global_var('func_3055')
func_3057_call = mutated_mod.get_global_var('func_3057')
call_6039 = relay.TupleGetItem(func_3055_call(), 0)
call_6040 = relay.TupleGetItem(func_3057_call(), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3057_call = mutated_mod.get_global_var('func_3057')
call_6051 = relay.TupleGetItem(func_3055_call(), 1)
call_6052 = relay.TupleGetItem(func_3057_call(), 1)
func_5774_call = mod.get_global_var('func_5774')
func_5776_call = mutated_mod.get_global_var('func_5776')
call_6062 = relay.TupleGetItem(func_5774_call(), 0)
call_6063 = relay.TupleGetItem(func_5776_call(), 0)
func_1860_call = mod.get_global_var('func_1860')
func_1862_call = mutated_mod.get_global_var('func_1862')
call_6065 = func_1860_call()
call_6066 = func_1860_call()
output = relay.Tuple([call_6039,call_6051,call_6062,call_6065,])
output2 = relay.Tuple([call_6040,call_6052,call_6063,call_6066,])
func_6079 = relay.Function([], output)
mod['func_6079'] = func_6079
mod = relay.transform.InferType()(mod)
mutated_mod['func_6079'] = func_6079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6079_call = mutated_mod.get_global_var('func_6079')
call_6080 = func_6079_call()
output = call_6080
func_6081 = relay.Function([], output)
mutated_mod['func_6081'] = func_6081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6014_call = mod.get_global_var('func_6014')
func_6015_call = mutated_mod.get_global_var('func_6015')
call_6107 = func_6014_call()
call_6108 = func_6014_call()
func_1452_call = mod.get_global_var('func_1452')
func_1454_call = mutated_mod.get_global_var('func_1454')
call_6119 = relay.TupleGetItem(func_1452_call(), 1)
call_6120 = relay.TupleGetItem(func_1454_call(), 1)
output = relay.Tuple([call_6107,call_6119,])
output2 = relay.Tuple([call_6108,call_6120,])
func_6127 = relay.Function([], output)
mod['func_6127'] = func_6127
mod = relay.transform.InferType()(mod)
output = func_6127()
func_6128 = relay.Function([], output)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_6140 = relay.TupleGetItem(func_918_call(), 0)
call_6141 = relay.TupleGetItem(func_920_call(), 0)
const_6142 = relay.const([[[6.070184,-8.167489,-3.308020,-6.396669,1.996135,-0.481579,6.637244,-0.436538,6.767020,-4.784249,6.055384,-7.920921,6.624691,-7.944504,-5.935347]],[[-5.762273,-3.962609,6.474167,3.349748,7.745396,7.167283,-3.139288,7.790286,7.432688,6.058889,-3.278956,7.167550,-2.585337,4.332218,9.147838]],[[-3.176876,-3.865798,-9.938897,-5.605586,1.432179,-8.094254,9.770785,-0.021568,5.133988,0.377144,1.698698,-0.342997,6.509233,3.207960,2.257964]],[[-3.587035,-9.839480,-8.487237,-7.981877,-0.182693,-5.775212,-3.204853,-4.002193,-8.733061,-6.953867,-7.684885,7.936942,-0.633781,6.485599,-1.728868]],[[-9.562253,4.201727,5.825967,1.102117,-9.599729,9.502017,-9.847045,-5.360939,-2.807533,9.694023,2.126374,-2.677944,-1.618971,1.115654,-1.371352]],[[-8.827610,-3.373837,-6.054828,4.149800,9.958011,2.167836,-9.789191,-4.807451,-5.715836,-7.478928,4.089138,-9.893170,-5.746005,0.495492,-0.730196]],[[6.861702,-5.778976,-8.987767,5.770062,5.899971,0.463087,-4.297583,-1.758141,3.448931,4.385485,-1.038032,0.298193,9.469960,6.870953,1.148333]],[[-5.251521,-6.633070,-9.658162,1.674562,-9.276296,-5.483282,-3.026479,-7.618852,6.844359,0.229848,9.026092,6.224515,-4.811678,-4.748659,4.088856]],[[-0.459137,8.585017,2.600522,5.469387,3.241635,2.436218,-2.545973,-2.576123,-8.102382,-4.577542,1.505786,-8.469658,-5.139854,1.644205,-6.303524]],[[-5.101603,-7.831340,-5.621955,2.472816,5.799035,8.107149,-9.519228,-1.180223,-0.951940,-2.255725,-4.188231,-4.958107,-5.893220,-1.438821,-6.163340]],[[2.897548,8.922729,-0.898020,4.809656,9.468574,-8.766351,3.542377,-2.872291,-2.528039,-6.776444,6.813327,-3.986130,1.355758,-6.789415,-5.035629]],[[0.567929,2.605337,5.965490,-7.142007,3.804351,0.711190,-6.434796,-9.992407,-2.468211,-2.211718,0.991095,-9.647966,5.951512,2.944912,3.748628]],[[-7.567347,7.184416,0.865668,2.474941,4.811661,1.104653,2.797242,0.098553,6.298580,-4.555594,-2.490926,7.537912,7.221167,0.588264,0.839001]],[[-2.714432,4.814923,9.543545,-0.563231,-1.012573,-2.446655,9.955396,2.208268,1.964682,-0.695858,-4.582106,-8.581740,9.551683,5.558862,-9.957210]]], dtype = "float32")#candidate|6142|(14, 1, 15)|const|float32
bop_6143 = relay.power(call_6140.astype('float32'), relay.reshape(const_6142.astype('float32'), relay.shape_of(call_6140))) # shape=(14, 1, 15)
bop_6146 = relay.power(call_6141.astype('float32'), relay.reshape(const_6142.astype('float32'), relay.shape_of(call_6141))) # shape=(14, 1, 15)
var_6171 = relay.var("var_6171", dtype = "float32", shape = (14, 15, 15))#candidate|6171|(14, 15, 15)|var|float32
bop_6172 = relay.multiply(const_6142.astype('uint8'), var_6171.astype('uint8')) # shape=(14, 15, 15)
output = relay.Tuple([bop_6143,bop_6172,])
output2 = relay.Tuple([bop_6146,bop_6172,])
func_6186 = relay.Function([var_6171,], output)
mod['func_6186'] = func_6186
mod = relay.transform.InferType()(mod)
mutated_mod['func_6186'] = func_6186
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6187 = relay.var("var_6187", dtype = "float32", shape = (14, 15, 15))#candidate|6187|(14, 15, 15)|var|float32
func_6186_call = mutated_mod.get_global_var('func_6186')
call_6188 = func_6186_call(var_6187)
output = call_6188
func_6189 = relay.Function([var_6187], output)
mutated_mod['func_6189'] = func_6189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3585_call = mod.get_global_var('func_3585')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_6261 = relay.TupleGetItem(func_3585_call(), 1)
call_6262 = relay.TupleGetItem(func_3586_call(), 1)
var_6264 = relay.var("var_6264", dtype = "float32", shape = (14, 11, 15))#candidate|6264|(14, 11, 15)|var|float32
bop_6265 = relay.left_shift(call_6261.astype('uint8'), relay.reshape(var_6264.astype('uint8'), relay.shape_of(call_6261))) # shape=(14, 11, 15)
bop_6268 = relay.left_shift(call_6262.astype('uint8'), relay.reshape(var_6264.astype('uint8'), relay.shape_of(call_6262))) # shape=(14, 11, 15)
output = relay.Tuple([bop_6265,])
output2 = relay.Tuple([bop_6268,])
func_6274 = relay.Function([var_6264,], output)
mod['func_6274'] = func_6274
mod = relay.transform.InferType()(mod)
mutated_mod['func_6274'] = func_6274
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6275 = relay.var("var_6275", dtype = "float32", shape = (14, 11, 15))#candidate|6275|(14, 11, 15)|var|float32
func_6274_call = mutated_mod.get_global_var('func_6274')
call_6276 = func_6274_call(var_6275)
output = call_6276
func_6277 = relay.Function([var_6275], output)
mutated_mod['func_6277'] = func_6277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2469_call = mod.get_global_var('func_2469')
func_2471_call = mutated_mod.get_global_var('func_2471')
call_6306 = relay.TupleGetItem(func_2469_call(), 0)
call_6307 = relay.TupleGetItem(func_2471_call(), 0)
output = relay.Tuple([call_6306,])
output2 = relay.Tuple([call_6307,])
func_6311 = relay.Function([], output)
mod['func_6311'] = func_6311
mod = relay.transform.InferType()(mod)
mutated_mod['func_6311'] = func_6311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6311_call = mutated_mod.get_global_var('func_6311')
call_6312 = func_6311_call()
output = call_6312
func_6313 = relay.Function([], output)
mutated_mod['func_6313'] = func_6313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4095_call = mod.get_global_var('func_4095')
func_4096_call = mutated_mod.get_global_var('func_4096')
call_6426 = relay.TupleGetItem(func_4095_call(), 0)
call_6427 = relay.TupleGetItem(func_4096_call(), 0)
output = relay.Tuple([call_6426,])
output2 = relay.Tuple([call_6427,])
func_6433 = relay.Function([], output)
mod['func_6433'] = func_6433
mod = relay.transform.InferType()(mod)
mutated_mod['func_6433'] = func_6433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6433_call = mutated_mod.get_global_var('func_6433')
call_6434 = func_6433_call()
output = call_6434
func_6435 = relay.Function([], output)
mutated_mod['func_6435'] = func_6435
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6493 = relay.const([[[7.751929,9.983375,5.598793,4.401608,4.690831],[-6.768377,8.883493,6.297502,-4.902528,-7.069521],[1.567160,-8.923994,9.414816,0.142031,-2.410172],[-7.158357,7.771188,-8.987409,-5.051094,9.567913],[3.319735,-5.483221,7.108400,6.229612,8.312967],[2.630260,-2.036873,4.532170,-6.086424,-0.221742]],[[9.754336,2.858557,-0.737149,6.577986,7.350589],[-0.501023,-0.652730,-5.973106,5.103519,-6.672357],[8.641010,4.292597,2.203555,3.248801,1.306307],[6.234415,-6.484268,3.728861,-5.730507,9.615533],[5.412680,-3.895856,-8.648818,-0.764630,4.944178],[-6.208687,-6.101599,-2.761272,-1.564691,9.386151]],[[-0.626248,-3.356327,9.724695,6.551757,-3.441623],[-0.298652,4.058186,-3.260255,5.990117,3.219975],[0.072962,5.490374,6.293315,7.919258,7.447185],[-9.272721,7.002126,-4.850367,-9.103342,7.022368],[-5.985619,0.424078,-5.970841,6.206653,-3.723311],[-0.920068,-2.738228,1.994990,-9.548016,7.160793]],[[4.720793,9.839314,-9.479496,-3.573374,1.819267],[1.355873,5.586200,4.389229,-6.567124,3.487825],[1.462914,-3.568776,3.769821,-2.265862,3.354560],[6.159947,4.990628,4.621092,-4.719780,-1.058889],[4.771331,9.125752,-7.627624,2.554153,9.034702],[2.843441,-7.190571,-6.364726,6.406343,0.745778]],[[-6.369441,-8.702726,0.440818,1.691277,6.734908],[-3.177762,5.666467,2.291987,-1.997462,3.234776],[0.279177,4.569232,-1.526820,7.338773,-2.489470],[-3.728040,1.992768,-2.828650,0.097386,-6.570907],[8.127842,3.658160,-8.942308,6.035962,8.880719],[-7.658362,0.169283,0.799777,8.790404,-2.065657]],[[6.372205,-8.859126,1.865111,-6.945968,-8.774029],[4.161126,5.568263,-7.801190,3.910954,-8.534308],[-9.560536,5.017895,-1.847004,-7.059845,4.744976],[5.648727,3.635379,5.721949,-3.456752,7.789115],[-4.764310,4.997822,-2.604062,9.802978,6.874725],[-9.974379,-1.780771,8.126255,-8.443579,-0.152479]],[[-6.377416,7.707619,2.601996,-6.939925,-0.867746],[-6.658168,-6.677702,-5.135378,4.057606,-1.724353],[3.446422,2.044859,-2.873257,9.274710,-4.807186],[-7.570988,7.544778,-3.264360,-6.701541,9.042463],[9.954476,7.096710,7.630626,-3.475249,9.147681],[6.227352,7.447241,-5.639806,2.659426,9.142154]],[[3.488422,6.591944,9.975932,4.392339,-9.293078],[-3.931654,-0.575263,-0.203173,5.390155,3.197344],[2.037807,7.299289,7.658261,4.306520,2.569263],[-0.553339,-4.060189,-4.810182,1.616111,-8.070924],[-2.550542,2.712631,-0.298443,-3.508675,-2.623375],[6.184820,-6.726428,6.639254,-9.854246,-9.661963]],[[8.233267,5.211134,-5.292885,3.526365,4.884187],[-2.925132,-5.050327,6.004916,0.547854,-7.455220],[0.387150,8.521980,-1.272759,2.685366,6.940219],[3.443697,-2.006238,6.471752,-9.372046,-7.508188],[-9.397697,9.612118,8.484193,4.907585,-6.387934],[-2.097578,6.412216,4.396421,-1.892929,7.934955]],[[-1.990583,-0.051641,3.332839,-4.238755,-1.293025],[3.840020,4.436872,0.552204,2.165889,3.172393],[-9.811992,3.881630,8.955024,-6.026543,5.428351],[-2.930543,-8.004323,-8.716350,-3.256928,3.743746],[-0.946523,3.702060,7.869604,-1.787574,9.137390],[-1.295952,2.145448,-1.907523,-7.351697,9.679843]],[[-1.849403,4.988124,-9.739772,-1.137397,-5.299023],[-6.098789,-3.496881,-8.246737,-3.746864,4.738448],[-6.472416,-5.778063,5.172839,8.918206,2.293257],[-7.499918,-3.361404,-9.730923,9.300824,3.981217],[-6.665424,-5.753973,2.531807,-9.545875,4.128598],[7.207491,9.243131,-9.368242,-4.040828,-2.716568]],[[-2.044344,0.351892,-4.086517,6.450834,-4.077271],[-2.599035,-3.079485,-5.420013,0.929662,-6.931425],[-2.085424,2.321510,2.530604,-9.082702,9.066253],[3.425900,7.301448,-4.964608,-4.081123,-1.851674],[-5.399689,5.330677,9.300554,-7.215742,-2.741749],[-6.634468,-5.731056,-7.096190,3.139663,-7.434777]],[[3.464409,-2.678878,-0.292571,-0.959288,-5.232810],[-0.182684,3.112454,-8.234355,5.001071,-4.316609],[9.115846,-1.847346,-6.041417,7.517868,8.598991],[-4.412433,3.021930,-2.943813,8.420180,-8.250125],[7.820326,-0.802323,-8.286462,3.079688,5.813379],[3.341133,-7.598968,-3.331766,-7.429745,-9.031015]]], dtype = "float32")#candidate|6493|(13, 6, 5)|const|float32
uop_6494 = relay.asinh(const_6493.astype('float32')) # shape=(13, 6, 5)
bop_6505 = relay.not_equal(const_6493.astype('bool'), relay.reshape(uop_6494.astype('bool'), relay.shape_of(const_6493))) # shape=(13, 6, 5)
const_6530 = relay.const([[[5.966766,-4.616520,6.370240,7.814800,-7.200903],[-5.730779,6.539229,4.864836,-5.145657,-6.499986],[-9.104381,7.944388,-4.591414,-6.733664,-5.824540],[-9.465893,7.523900,-7.123635,-1.477060,-1.431464],[-7.340637,-7.010271,7.740014,-0.793730,5.623859],[7.609180,7.654159,3.398028,0.460409,3.558026]],[[0.520333,-3.467209,-4.262902,-4.942655,-8.691345],[-8.009384,8.775493,4.256030,-3.215534,-7.355612],[-7.279005,-6.769647,-0.642456,4.131730,2.056020],[6.042563,-5.122875,3.125684,-3.496075,7.592411],[-5.441463,9.669786,2.444334,-8.019310,-6.294421],[0.921393,-6.439719,4.309080,3.293135,2.796774]],[[0.123637,2.929430,-8.406799,4.940797,-4.657714],[3.799965,-4.233054,-5.262832,4.889450,3.926781],[1.377368,-5.180914,-5.303758,-4.089990,-6.018625],[-5.361323,-2.752295,-1.541610,-4.899161,7.092329],[-6.756007,-7.822951,3.428136,-0.813059,5.559959],[0.425419,-4.679491,0.482833,7.283657,-8.051603]],[[0.741170,8.871233,4.059050,-5.901308,1.981384],[-9.452560,-9.323750,-4.296680,-5.225081,0.381104],[8.894788,-5.065902,-5.550620,-6.360018,-2.230247],[-1.166359,-1.725376,1.838841,6.408902,8.891142],[-7.326661,-8.558833,-9.438158,-5.277591,-6.523680],[4.088009,-4.415942,6.846133,4.199247,-2.398202]],[[6.069128,1.293218,0.464381,7.244334,-7.475328],[2.318988,-5.970022,7.018788,6.999235,9.663111],[7.383383,9.004767,3.357890,5.252589,-6.282286],[-9.916239,-2.495641,6.524770,-7.217012,-0.540429],[-4.121331,9.060232,5.663458,6.066612,4.005573],[-6.143069,3.136562,-2.127445,3.709979,6.108213]],[[-6.548347,7.675849,6.662248,-9.966007,7.878836],[-0.388502,-0.003894,-9.142607,3.140358,-3.838431],[1.475669,9.055743,-9.342233,1.129752,5.335522],[-9.523677,-8.980882,-6.808173,-2.091413,4.036030],[3.707051,6.600884,-6.831035,-4.845444,-0.614749],[-0.312045,0.350927,-4.624227,2.475618,8.308905]],[[5.379230,-4.268265,5.407212,6.610402,0.179928],[6.669828,3.850679,3.096942,8.239292,9.874232],[-0.911814,7.538521,5.522852,-8.810686,7.153885],[-5.594858,1.983332,-0.112717,8.037070,-0.791217],[-4.927806,-9.245956,7.373229,5.282225,4.055480],[-4.406078,-5.601832,6.782886,5.517123,2.400590]],[[-6.527687,3.231849,-5.584359,-7.254724,-0.107424],[8.881949,5.334572,-0.933613,9.643355,8.140176],[-6.112527,-1.155433,4.771745,-6.437562,2.475311],[2.735260,6.613488,6.690764,-8.050610,-0.175693],[7.265354,5.326203,1.820188,4.496661,-1.858461],[1.804418,-2.836282,2.191161,2.273875,-8.179232]],[[9.179019,-0.417721,5.258491,4.378296,-8.932575],[-0.745774,8.058069,-8.832984,1.373234,7.241082],[-6.048300,-2.627945,-7.131540,-0.826961,3.090392],[6.865098,-5.030718,-4.382473,1.652259,5.245913],[3.763664,0.121989,7.207697,8.152672,2.543444],[-9.831711,8.517316,-2.771375,2.300337,5.963719]],[[-1.076020,8.258083,2.022621,-6.846634,2.323214],[-9.474576,5.308489,3.942687,5.879408,4.694563],[6.217791,-6.805575,-9.624568,9.642260,0.357800],[-8.760002,9.312127,-9.109945,0.602770,8.753607],[-1.467222,8.453736,-7.884182,-8.908267,0.534178],[-3.279769,-5.535796,1.173373,-9.703630,-7.434667]],[[-5.486044,4.858007,-5.621465,-1.043980,-4.339544],[4.696888,1.563966,-7.954393,4.820159,9.602498],[-9.817260,-2.752556,-3.750119,2.774325,-9.620858],[-1.127443,-0.436608,-3.659574,3.706004,3.596879],[-7.239468,-7.176823,7.612211,0.243942,2.045057],[-4.625019,9.435919,-8.112395,-0.160885,-0.810696]],[[5.242758,4.114058,-0.245722,8.141393,-5.902406],[4.171584,8.633954,-2.995647,-3.691687,3.622904],[-6.246249,2.022507,-3.311506,4.621757,7.452557],[8.286085,-9.885595,-8.157696,-3.763987,-5.431990],[-5.003872,-6.748369,7.829762,4.353425,-7.801166],[-0.740527,-2.060686,-4.352248,8.327261,7.685365]],[[5.492655,-6.910397,-9.222096,-3.802619,-8.161789],[5.182536,-1.720569,-0.830853,9.251684,5.558561],[-3.046648,-2.898984,2.396973,-2.545554,0.699895],[7.293175,-0.186449,-3.575216,4.412380,-0.873785],[-9.244003,-2.187228,3.785650,-1.234210,-1.442717],[-0.884505,5.399826,2.776725,-3.388493,-2.342784]]], dtype = "float32")#candidate|6530|(13, 6, 5)|const|float32
bop_6531 = relay.divide(uop_6494.astype('float32'), relay.reshape(const_6530.astype('float32'), relay.shape_of(uop_6494))) # shape=(13, 6, 5)
func_1860_call = mod.get_global_var('func_1860')
func_1862_call = mutated_mod.get_global_var('func_1862')
call_6539 = func_1860_call()
call_6540 = func_1860_call()
uop_6544 = relay.cos(bop_6531.astype('float64')) # shape=(13, 6, 5)
func_3745_call = mod.get_global_var('func_3745')
func_3746_call = mutated_mod.get_global_var('func_3746')
call_6546 = func_3745_call()
call_6547 = func_3745_call()
output = relay.Tuple([bop_6505,call_6539,uop_6544,call_6546,])
output2 = relay.Tuple([bop_6505,call_6540,uop_6544,call_6547,])
func_6548 = relay.Function([], output)
mod['func_6548'] = func_6548
mod = relay.transform.InferType()(mod)
mutated_mod['func_6548'] = func_6548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6548_call = mutated_mod.get_global_var('func_6548')
call_6549 = func_6548_call()
output = call_6549
func_6550 = relay.Function([], output)
mutated_mod['func_6550'] = func_6550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_6574 = relay.TupleGetItem(func_1171_call(), 1)
call_6575 = relay.TupleGetItem(func_1172_call(), 1)
output = call_6574
output2 = call_6575
func_6578 = relay.Function([], output)
mod['func_6578'] = func_6578
mod = relay.transform.InferType()(mod)
mutated_mod['func_6578'] = func_6578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6578_call = mutated_mod.get_global_var('func_6578')
call_6579 = func_6578_call()
output = call_6579
func_6580 = relay.Function([], output)
mutated_mod['func_6580'] = func_6580
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6586 = relay.var("var_6586", dtype = "float64", shape = (12, 5, 16))#candidate|6586|(12, 5, 16)|var|float64
const_6587 = relay.const([[[1.647313,9.415533,-8.400925,8.495662,6.517900,-9.886550,5.049430,-6.661064,-3.300157,5.889315,-4.382054,-8.884894,-5.750867,0.123665,4.658621,6.516015],[-0.158234,-9.740549,-2.674364,4.723239,2.155350,8.625815,4.113379,5.157503,8.896847,-0.768940,1.152718,-7.870526,4.585584,-5.634332,-2.078653,-1.535313],[5.547717,-6.631840,-1.936697,9.692945,1.717440,5.987324,-0.864571,-7.345207,5.196070,3.000620,-4.330869,-4.551641,2.394575,-5.770701,9.842564,-8.659904],[4.743408,-2.283588,6.319852,1.661303,-9.981493,6.415810,-1.577420,5.945605,-8.216655,-7.672565,-5.629585,-0.822342,5.232918,2.023069,3.991011,0.320112],[-8.919944,8.514329,7.372489,9.966053,9.480748,-5.940318,-7.534280,3.560611,5.946193,2.350512,5.580133,3.678347,8.732542,9.679755,1.596451,4.715970]],[[-3.149260,1.484440,-3.643062,-6.115998,3.636629,2.153713,-3.556563,-9.530463,-8.026760,2.935274,5.690536,-4.404306,1.330463,-5.432396,4.812725,0.301794],[-7.645421,8.193913,7.993873,-6.261311,8.008975,-2.888170,-1.596785,7.961288,8.632044,-3.048154,7.407256,6.346671,-7.623154,7.625805,5.253742,-5.334408],[0.444418,-3.684277,7.834626,3.974825,-0.159414,-7.665391,-7.898381,1.495648,-7.634097,9.944754,8.158819,-8.385814,-4.427341,8.194506,-6.430040,4.567603],[5.955444,-9.838250,-8.365840,1.773577,-8.146692,9.374802,5.810464,-5.179581,5.489359,-4.761905,-5.660534,-8.570795,-0.096773,-3.977817,3.845842,2.844293],[-8.895551,0.973273,8.251466,6.216868,-3.320494,2.942965,-8.323541,4.128461,4.279149,-4.569498,3.835489,-4.726270,-5.586998,-2.875178,-6.147773,-6.736142]],[[-6.753176,5.420422,7.292969,8.837175,6.523441,7.409206,-4.376571,3.869070,-9.495133,7.383189,0.436854,-8.603252,-9.314180,4.821335,-1.395325,6.875422],[-5.518182,-1.786239,-1.159298,5.910116,-8.833139,8.026979,-6.340387,-4.084900,-0.805157,-8.462723,0.498619,1.000743,2.713478,-6.020339,-4.293785,-4.407299],[-5.565791,-7.731941,-1.934728,5.928017,3.774843,0.188043,4.352081,-8.836049,3.260404,7.949193,9.873305,9.790879,-3.471240,-9.318242,1.207025,3.150890],[-0.660152,-4.292425,9.658430,2.127323,-6.187456,-3.720933,5.472795,7.905767,6.243245,7.419600,5.291461,-2.257199,0.940485,1.599783,1.126783,-3.889772],[-6.228567,2.467098,-6.767079,-3.020484,8.517272,7.147872,-2.340984,-7.687551,4.538240,-5.260229,-9.228337,-0.071756,-0.687569,-1.930646,-1.569301,8.540371]],[[-9.283169,4.815472,4.901506,9.472171,-6.578221,7.095128,-9.571484,7.181764,-1.371919,-8.705510,-1.101738,-9.407326,-8.926210,-0.236049,3.961286,-2.036534],[-2.381416,5.860767,3.788108,5.932169,0.412371,-7.020266,-2.509439,4.904361,-2.902544,4.245073,4.539522,4.839054,-2.860111,-6.845515,0.277813,0.887005],[-6.300301,2.768320,-1.391287,-3.417964,-0.767335,3.326000,-3.882155,2.932021,-7.153464,3.930727,-3.053622,-1.692977,-1.073794,-9.285009,6.506755,-7.413612],[-9.043299,8.047680,-4.153032,-0.067362,1.938931,8.252867,0.604471,-5.754942,0.791438,6.701640,-4.171738,-6.565543,-1.990387,-4.251997,8.298148,-4.982396],[-9.404429,-7.152462,3.034926,8.138491,-8.103512,-8.209394,3.529069,9.284295,-6.926787,-2.740588,-0.601475,2.222787,-7.616647,-5.540484,-6.832273,7.742450]],[[3.903407,7.357938,5.947699,1.780955,6.629782,2.523967,-8.787162,5.777046,7.980237,3.389196,0.766631,-4.953891,-9.193506,1.624936,2.773820,1.816637],[-0.641104,5.542710,-7.081865,7.730494,-1.993404,-2.762691,5.014927,4.070823,-8.747764,8.705202,-8.267130,8.088448,-2.673650,7.898299,8.958698,-9.319558],[-3.008319,5.957286,-7.551828,-9.747498,6.815808,3.271905,9.316874,4.520742,7.050013,6.462103,6.221589,-9.775085,1.608827,1.444521,9.667898,-8.702765],[-4.440293,-3.864747,-1.362881,1.542854,2.783515,-8.587039,-2.150695,-9.342075,-4.726808,6.633004,-2.047133,-2.574045,7.792019,0.092996,6.985013,-0.513652],[2.160881,1.679194,-2.280964,-5.232955,7.929206,-5.776281,-5.997449,-1.086527,-4.936523,-1.236977,1.412950,-5.739257,7.083262,3.816774,0.336532,-1.138222]],[[-0.294916,-6.840872,-6.352804,2.277391,8.519589,9.418734,-5.177426,3.290688,4.303825,-0.877164,-1.380881,-7.961975,-5.114635,-9.895822,9.533591,-2.276028],[-6.281566,-7.271377,3.661826,7.238527,8.533779,9.139798,-3.538986,-0.542440,-8.588232,-9.489127,9.711021,-1.309342,2.189176,8.340802,6.623548,-9.541774],[-8.372340,8.796784,-9.715291,5.521542,4.841615,-0.112019,5.441201,-5.326951,7.550863,-8.694592,3.761290,-4.669454,3.452075,4.113927,5.945398,6.183802],[7.367042,-4.665682,6.682182,0.203644,-4.194441,-1.512608,8.915577,2.395616,8.155583,9.675802,0.070554,5.058986,-1.694480,8.211608,5.494196,7.454208],[3.963031,-7.829326,5.079100,-1.484396,5.730144,4.068861,9.688307,1.097583,-8.702766,0.120186,-9.955791,3.342363,1.033952,0.659532,3.057017,6.771458]],[[-1.401782,6.417961,-5.051355,3.222064,-4.281229,-6.912264,7.049205,-9.052536,-8.965566,3.057484,2.517425,1.780030,-8.032954,1.502165,-2.354188,-6.889226],[-8.471014,-2.923803,2.557600,3.221813,7.765187,8.420589,3.748698,-5.305846,6.229396,7.071244,-5.904285,-7.411858,0.918699,-7.697923,-1.674545,-3.033175],[-9.494155,6.121125,-9.773584,9.055391,-4.729584,-3.163238,8.456620,-2.041981,7.071215,8.274424,-3.910189,-5.207492,4.384197,3.955026,2.139641,-6.143187],[7.451738,-6.436985,-3.414076,8.181699,-5.895441,4.957371,-9.188283,7.890084,6.585381,-8.508766,-9.786514,9.336625,4.330898,8.386629,-8.612280,6.893655],[-3.511248,7.673292,1.914479,3.429061,-8.790719,1.532234,-7.285591,-6.880366,4.305709,-0.613154,1.393394,5.483324,-7.689959,-6.147305,9.495718,-1.723484]],[[0.722628,-5.979856,-2.687886,-1.018815,-3.277121,-2.817993,-6.930184,-1.590446,1.888210,6.455107,-5.537028,2.278659,-0.792398,6.680940,0.695604,7.192893],[4.803229,-8.701097,1.116261,9.905183,-6.113191,7.174295,-5.473062,7.396833,-5.672310,2.633538,0.678125,0.475683,-2.458093,9.744159,3.283349,-0.811284],[0.830519,-2.799344,2.691303,-0.748886,6.312081,7.798153,-2.276637,7.914368,7.787959,1.159381,-8.603275,-0.371931,-8.824448,-1.257197,-8.317509,-5.763128],[8.045615,5.204451,-8.071969,9.868563,1.555174,-7.367064,8.494477,-1.016187,-7.577645,5.816029,-0.733521,8.730481,-8.430809,-2.799107,-9.147786,-0.491014],[-9.264568,-7.175579,9.814056,-6.089304,-8.958217,-3.179984,2.107952,9.110364,3.355366,-7.390845,-9.259508,-3.968747,8.989939,-0.556094,5.081535,-1.963079]],[[-9.340698,2.182788,-5.869409,-3.000772,-4.632418,-7.094514,8.228998,6.413278,-0.671253,-4.229431,4.576778,2.880560,-0.509453,-4.547861,-6.724862,3.565853],[5.124223,6.085151,-8.548417,4.006246,-4.095040,-5.063055,9.569695,-7.419692,5.841924,-7.540751,5.006476,-3.617940,5.211496,-2.990922,3.839579,-4.225437],[-0.497424,-2.767165,5.976381,2.521871,5.758912,6.783884,2.948953,-4.735204,4.258905,8.361617,8.557053,-1.048169,-9.546094,-7.362317,-1.896027,-0.222920],[-2.009109,0.093253,-1.516365,-3.376986,5.199838,-4.252471,3.830807,2.418446,-8.064908,-5.392049,-8.178877,-3.438944,9.719696,-6.927011,-1.952270,-0.944455],[6.885607,-6.197244,-5.016627,7.499015,4.084559,-4.016651,9.397246,7.403062,-3.910176,5.818426,-3.119025,5.684826,-3.788588,1.800806,-9.499941,-5.859651]],[[6.983975,-0.886353,3.146675,4.939984,0.019345,8.493893,-6.234032,-3.175436,-1.295113,5.613225,-5.851469,-4.892667,6.447150,6.889940,9.884121,1.319462],[-9.958388,-4.230311,-9.372733,-1.357341,0.670132,-0.690455,-9.627715,-4.977552,-0.899497,8.373707,-9.391630,5.175240,8.358955,-4.534241,-5.783401,-4.188015],[9.056771,-1.437032,-4.156348,5.356305,1.131374,8.509997,4.821380,-7.056689,-9.831784,-0.765965,-6.372667,-7.758052,-8.518395,-8.681661,-9.936582,3.212224],[-3.855726,5.894925,2.812690,-0.630025,-9.032069,-9.935448,-7.118102,7.639491,6.675869,9.247846,-4.177693,5.778604,-7.046778,9.742538,-6.028818,-4.618745],[2.139392,-7.339645,4.967727,2.749051,-6.948447,1.181136,-3.504288,5.442611,-8.296801,9.679469,-5.334830,2.338707,7.137763,-4.187076,1.316789,-7.133182]],[[-3.193682,8.274296,4.461520,-9.457952,8.763138,-9.326392,-9.788818,9.044423,0.578859,3.625299,5.156666,-1.127756,-7.991380,0.862336,-6.227972,-0.281370],[-8.923352,-4.376573,-9.900197,0.506993,-9.531586,3.826645,-6.899890,2.277053,-6.377032,4.093970,4.708677,-4.861600,-1.242069,7.974295,8.945492,-5.428671],[-1.589762,4.779871,4.288404,-8.153098,0.402145,-6.483688,-8.952194,7.797740,3.994925,-3.672354,-0.518822,-2.828647,-3.194494,7.961792,7.873287,5.020170],[-6.325427,-0.793131,-6.354968,2.353982,-6.374854,4.807894,9.196014,9.586031,1.759190,1.709884,-5.088416,2.856584,-3.725280,-1.371481,-1.308260,1.289510],[6.817734,-4.096120,-6.298300,3.685658,5.601813,5.426603,9.933543,7.837663,-2.138730,-4.607308,-7.978130,-2.098795,1.362769,-3.350123,-4.747191,-7.005579]],[[0.718125,7.777771,7.696123,2.003150,3.967444,4.914045,6.065475,-5.465512,-0.868408,1.462312,-3.927039,5.911387,-1.483686,3.325525,7.588496,-0.547163],[-2.773961,-0.691294,-5.270294,-2.256026,-9.754475,-0.711732,3.326473,9.594570,-9.531361,-8.956038,-2.131921,-0.770312,-6.472323,-6.964161,9.141555,-9.992800],[-9.160332,3.825014,-7.326209,7.161941,-3.612099,7.864636,-4.830428,1.524014,1.087933,1.784948,3.906574,-7.133827,8.698032,5.697090,-3.282242,-2.491036],[-9.756900,9.064368,1.070792,3.380588,4.078060,4.461176,3.929635,-1.656620,9.008069,7.591913,3.016616,-8.569774,-0.941393,6.768413,6.811291,2.115738],[-4.164336,5.008268,5.339592,4.606636,7.998163,-3.710748,6.980429,2.852351,-4.144531,8.999857,-4.330549,-0.254796,3.221968,7.658234,6.436767,-1.771672]]], dtype = "float64")#candidate|6587|(12, 5, 16)|const|float64
bop_6588 = relay.power(var_6586.astype('float64'), relay.reshape(const_6587.astype('float64'), relay.shape_of(var_6586))) # shape=(12, 5, 16)
output = relay.Tuple([bop_6588,])
output2 = relay.Tuple([bop_6588,])
func_6594 = relay.Function([var_6586,], output)
mod['func_6594'] = func_6594
mod = relay.transform.InferType()(mod)
var_6595 = relay.var("var_6595", dtype = "float64", shape = (12, 5, 16))#candidate|6595|(12, 5, 16)|var|float64
output = func_6594(var_6595)
func_6596 = relay.Function([var_6595], output)
mutated_mod['func_6596'] = func_6596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_6598 = relay.TupleGetItem(func_918_call(), 0)
call_6599 = relay.TupleGetItem(func_920_call(), 0)
var_6611 = relay.var("var_6611", dtype = "float32", shape = (14, 12, 15))#candidate|6611|(14, 12, 15)|var|float32
bop_6612 = relay.not_equal(call_6598.astype('bool'), var_6611.astype('bool')) # shape=(14, 12, 15)
bop_6615 = relay.not_equal(call_6599.astype('bool'), var_6611.astype('bool')) # shape=(14, 12, 15)
var_6617 = relay.var("var_6617", dtype = "bool", shape = (14, 12, 15))#candidate|6617|(14, 12, 15)|var|bool
bop_6618 = relay.less(bop_6612.astype('bool'), relay.reshape(var_6617.astype('bool'), relay.shape_of(bop_6612))) # shape=(14, 12, 15)
bop_6621 = relay.less(bop_6615.astype('bool'), relay.reshape(var_6617.astype('bool'), relay.shape_of(bop_6615))) # shape=(14, 12, 15)
output = relay.Tuple([bop_6618,])
output2 = relay.Tuple([bop_6621,])
func_6624 = relay.Function([var_6611,var_6617,], output)
mod['func_6624'] = func_6624
mod = relay.transform.InferType()(mod)
var_6625 = relay.var("var_6625", dtype = "float32", shape = (14, 12, 15))#candidate|6625|(14, 12, 15)|var|float32
var_6626 = relay.var("var_6626", dtype = "bool", shape = (14, 12, 15))#candidate|6626|(14, 12, 15)|var|bool
output = func_6624(var_6625,var_6626,)
func_6627 = relay.Function([var_6625,var_6626,], output)
mutated_mod['func_6627'] = func_6627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6014_call = mod.get_global_var('func_6014')
func_6015_call = mutated_mod.get_global_var('func_6015')
call_6635 = func_6014_call()
call_6636 = func_6014_call()
output = call_6635
output2 = call_6636
func_6649 = relay.Function([], output)
mod['func_6649'] = func_6649
mod = relay.transform.InferType()(mod)
output = func_6649()
func_6650 = relay.Function([], output)
mutated_mod['func_6650'] = func_6650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6578_call = mod.get_global_var('func_6578')
func_6580_call = mutated_mod.get_global_var('func_6580')
call_6702 = func_6578_call()
call_6703 = func_6578_call()
output = relay.Tuple([call_6702,])
output2 = relay.Tuple([call_6703,])
func_6714 = relay.Function([], output)
mod['func_6714'] = func_6714
mod = relay.transform.InferType()(mod)
output = func_6714()
func_6715 = relay.Function([], output)
mutated_mod['func_6715'] = func_6715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6714_call = mod.get_global_var('func_6714')
func_6715_call = mutated_mod.get_global_var('func_6715')
call_6795 = relay.TupleGetItem(func_6714_call(), 0)
call_6796 = relay.TupleGetItem(func_6715_call(), 0)
func_2469_call = mod.get_global_var('func_2469')
func_2471_call = mutated_mod.get_global_var('func_2471')
call_6804 = relay.TupleGetItem(func_2469_call(), 0)
call_6805 = relay.TupleGetItem(func_2471_call(), 0)
output = relay.Tuple([call_6795,call_6804,])
output2 = relay.Tuple([call_6796,call_6805,])
func_6809 = relay.Function([], output)
mod['func_6809'] = func_6809
mod = relay.transform.InferType()(mod)
output = func_6809()
func_6810 = relay.Function([], output)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4553_call = mod.get_global_var('func_4553')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_6852 = func_4553_call()
call_6853 = func_4553_call()
func_2318_call = mod.get_global_var('func_2318')
func_2320_call = mutated_mod.get_global_var('func_2320')
var_6859 = relay.var("var_6859", dtype = "float32", shape = (1680,))#candidate|6859|(1680,)|var|float32
call_6858 = relay.TupleGetItem(func_2318_call(relay.reshape(var_6859.astype('float32'), [1680,])), 2)
call_6860 = relay.TupleGetItem(func_2320_call(relay.reshape(var_6859.astype('float32'), [1680,])), 2)
uop_6889 = relay.rsqrt(var_6859.astype('float64')) # shape=(1680,)
output = relay.Tuple([call_6852,call_6858,uop_6889,])
output2 = relay.Tuple([call_6853,call_6860,uop_6889,])
func_6904 = relay.Function([var_6859,], output)
mod['func_6904'] = func_6904
mod = relay.transform.InferType()(mod)
var_6905 = relay.var("var_6905", dtype = "float32", shape = (1680,))#candidate|6905|(1680,)|var|float32
output = func_6904(var_6905)
func_6906 = relay.Function([var_6905], output)
mutated_mod['func_6906'] = func_6906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_6945 = relay.TupleGetItem(func_1550_call(), 1)
call_6946 = relay.TupleGetItem(func_1551_call(), 1)
output = relay.Tuple([call_6945,])
output2 = relay.Tuple([call_6946,])
func_6958 = relay.Function([], output)
mod['func_6958'] = func_6958
mod = relay.transform.InferType()(mod)
mutated_mod['func_6958'] = func_6958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6958_call = mutated_mod.get_global_var('func_6958')
call_6959 = func_6958_call()
output = call_6959
func_6960 = relay.Function([], output)
mutated_mod['func_6960'] = func_6960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6958_call = mod.get_global_var('func_6958')
func_6960_call = mutated_mod.get_global_var('func_6960')
call_6992 = relay.TupleGetItem(func_6958_call(), 0)
call_6993 = relay.TupleGetItem(func_6960_call(), 0)
output = call_6992
output2 = call_6993
func_7008 = relay.Function([], output)
mod['func_7008'] = func_7008
mod = relay.transform.InferType()(mod)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7008_call = mutated_mod.get_global_var('func_7008')
call_7009 = func_7008_call()
output = call_7009
func_7010 = relay.Function([], output)
mutated_mod['func_7010'] = func_7010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2688_call = mod.get_global_var('func_2688')
func_2690_call = mutated_mod.get_global_var('func_2690')
call_7026 = relay.TupleGetItem(func_2688_call(), 0)
call_7027 = relay.TupleGetItem(func_2690_call(), 0)
output = call_7026
output2 = call_7027
func_7037 = relay.Function([], output)
mod['func_7037'] = func_7037
mod = relay.transform.InferType()(mod)
mutated_mod['func_7037'] = func_7037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mutated_mod.get_global_var('func_7037')
call_7038 = func_7037_call()
output = call_7038
func_7039 = relay.Function([], output)
mutated_mod['func_7039'] = func_7039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7037_call = mod.get_global_var('func_7037')
func_7039_call = mutated_mod.get_global_var('func_7039')
call_7063 = func_7037_call()
call_7064 = func_7037_call()
func_1827_call = mod.get_global_var('func_1827')
func_1828_call = mutated_mod.get_global_var('func_1828')
call_7068 = relay.TupleGetItem(func_1827_call(), 0)
call_7069 = relay.TupleGetItem(func_1828_call(), 0)
func_5617_call = mod.get_global_var('func_5617')
func_5620_call = mutated_mod.get_global_var('func_5620')
var_7071 = relay.var("var_7071", dtype = "float64", shape = (3, 66))#candidate|7071|(3, 66)|var|float64
call_7070 = func_5617_call(relay.reshape(var_7071.astype('float64'), [11, 6, 3]))
call_7072 = func_5617_call(relay.reshape(var_7071.astype('float64'), [11, 6, 3]))
var_7073 = relay.var("var_7073", dtype = "float64", shape = (3, 66))#candidate|7073|(3, 66)|var|float64
bop_7074 = relay.bitwise_xor(var_7071.astype('uint16'), relay.reshape(var_7073.astype('uint16'), relay.shape_of(var_7071))) # shape=(3, 66)
func_5529_call = mod.get_global_var('func_5529')
func_5531_call = mutated_mod.get_global_var('func_5531')
call_7078 = relay.TupleGetItem(func_5529_call(), 1)
call_7079 = relay.TupleGetItem(func_5531_call(), 1)
func_782_call = mod.get_global_var('func_782')
func_784_call = mutated_mod.get_global_var('func_784')
call_7082 = func_782_call()
call_7083 = func_782_call()
output = relay.Tuple([call_7063,call_7068,call_7070,bop_7074,call_7078,call_7082,])
output2 = relay.Tuple([call_7064,call_7069,call_7072,bop_7074,call_7079,call_7083,])
func_7087 = relay.Function([var_7071,var_7073,], output)
mod['func_7087'] = func_7087
mod = relay.transform.InferType()(mod)
mutated_mod['func_7087'] = func_7087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7087_call = mutated_mod.get_global_var('func_7087')
var_7089 = relay.var("var_7089", dtype = "float64", shape = (3, 66))#candidate|7089|(3, 66)|var|float64
var_7090 = relay.var("var_7090", dtype = "float64", shape = (3, 66))#candidate|7090|(3, 66)|var|float64
call_7088 = func_7087_call(var_7089,var_7090,)
output = call_7088
func_7091 = relay.Function([var_7089,var_7090,], output)
mutated_mod['func_7091'] = func_7091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7093 = relay.var("var_7093", dtype = "float32", shape = (4, 1, 12))#candidate|7093|(4, 1, 12)|var|float32
uop_7094 = relay.exp(var_7093.astype('float32')) # shape=(4, 1, 12)
output = relay.Tuple([uop_7094,])
output2 = relay.Tuple([uop_7094,])
func_7099 = relay.Function([var_7093,], output)
mod['func_7099'] = func_7099
mod = relay.transform.InferType()(mod)
var_7100 = relay.var("var_7100", dtype = "float32", shape = (4, 1, 12))#candidate|7100|(4, 1, 12)|var|float32
output = func_7099(var_7100)
func_7101 = relay.Function([var_7100], output)
mutated_mod['func_7101'] = func_7101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3585_call = mod.get_global_var('func_3585')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_7108 = relay.TupleGetItem(func_3585_call(), 1)
call_7109 = relay.TupleGetItem(func_3586_call(), 1)
func_2249_call = mod.get_global_var('func_2249')
func_2253_call = mutated_mod.get_global_var('func_2253')
const_7136 = relay.const([False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,True,True], dtype = "bool")#candidate|7136|(560,)|const|bool
call_7135 = relay.TupleGetItem(func_2249_call(relay.reshape(const_7136.astype('bool'), [7, 16, 5]), relay.reshape(const_7136.astype('bool'), [7, 16, 5]), ), 0)
call_7137 = relay.TupleGetItem(func_2253_call(relay.reshape(const_7136.astype('bool'), [7, 16, 5]), relay.reshape(const_7136.astype('bool'), [7, 16, 5]), ), 0)
uop_7157 = relay.sqrt(call_7108.astype('float32')) # shape=(14, 11, 15)
uop_7159 = relay.sqrt(call_7109.astype('float32')) # shape=(14, 11, 15)
func_5774_call = mod.get_global_var('func_5774')
func_5776_call = mutated_mod.get_global_var('func_5776')
call_7160 = relay.TupleGetItem(func_5774_call(), 0)
call_7161 = relay.TupleGetItem(func_5776_call(), 0)
func_6127_call = mod.get_global_var('func_6127')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_7164 = relay.TupleGetItem(func_6127_call(), 0)
call_7165 = relay.TupleGetItem(func_6128_call(), 0)
func_3162_call = mod.get_global_var('func_3162')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_7173 = relay.TupleGetItem(func_3162_call(), 1)
call_7174 = relay.TupleGetItem(func_3163_call(), 1)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_7181 = relay.TupleGetItem(func_1590_call(relay.reshape(call_7160.astype('float32'), [14, 1, 15])), 1)
call_7182 = relay.TupleGetItem(func_1592_call(relay.reshape(call_7160.astype('float32'), [14, 1, 15])), 1)
uop_7191 = relay.asin(uop_7157.astype('float64')) # shape=(14, 11, 15)
uop_7193 = relay.asin(uop_7159.astype('float64')) # shape=(14, 11, 15)
uop_7206 = relay.atanh(uop_7191.astype('float64')) # shape=(14, 11, 15)
uop_7208 = relay.atanh(uop_7193.astype('float64')) # shape=(14, 11, 15)
uop_7209 = relay.rsqrt(uop_7206.astype('float64')) # shape=(14, 11, 15)
uop_7211 = relay.rsqrt(uop_7208.astype('float64')) # shape=(14, 11, 15)
uop_7222 = relay.erf(uop_7209.astype('float32')) # shape=(14, 11, 15)
uop_7224 = relay.erf(uop_7211.astype('float32')) # shape=(14, 11, 15)
func_6578_call = mod.get_global_var('func_6578')
func_6580_call = mutated_mod.get_global_var('func_6580')
call_7243 = func_6578_call()
call_7244 = func_6578_call()
output = relay.Tuple([call_7135,const_7136,call_7160,call_7164,call_7173,call_7181,uop_7222,call_7243,])
output2 = relay.Tuple([call_7137,const_7136,call_7161,call_7165,call_7174,call_7182,uop_7224,call_7244,])
func_7255 = relay.Function([], output)
mod['func_7255'] = func_7255
mod = relay.transform.InferType()(mod)
output = func_7255()
func_7256 = relay.Function([], output)
mutated_mod['func_7256'] = func_7256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6311_call = mod.get_global_var('func_6311')
func_6313_call = mutated_mod.get_global_var('func_6313')
call_7298 = relay.TupleGetItem(func_6311_call(), 0)
call_7299 = relay.TupleGetItem(func_6313_call(), 0)
func_1860_call = mod.get_global_var('func_1860')
func_1862_call = mutated_mod.get_global_var('func_1862')
call_7322 = func_1860_call()
call_7323 = func_1860_call()
output = relay.Tuple([call_7298,call_7322,])
output2 = relay.Tuple([call_7299,call_7323,])
func_7328 = relay.Function([], output)
mod['func_7328'] = func_7328
mod = relay.transform.InferType()(mod)
mutated_mod['func_7328'] = func_7328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7328_call = mutated_mod.get_global_var('func_7328')
call_7329 = func_7328_call()
output = call_7329
func_7330 = relay.Function([], output)
mutated_mod['func_7330'] = func_7330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5320_call = mod.get_global_var('func_5320')
func_5322_call = mutated_mod.get_global_var('func_5322')
call_7359 = func_5320_call()
call_7360 = func_5320_call()
func_2134_call = mod.get_global_var('func_2134')
func_2137_call = mutated_mod.get_global_var('func_2137')
var_7362 = relay.var("var_7362", dtype = "float32", shape = (70, 6))#candidate|7362|(70, 6)|var|float32
call_7361 = relay.TupleGetItem(func_2134_call(relay.reshape(var_7362.astype('float32'), [420,])), 2)
call_7363 = relay.TupleGetItem(func_2137_call(relay.reshape(var_7362.astype('float32'), [420,])), 2)
bop_7365 = relay.multiply(var_7362.astype('uint16'), relay.reshape(call_7361.astype('uint16'), relay.shape_of(var_7362))) # shape=(70, 6)
bop_7368 = relay.multiply(var_7362.astype('uint16'), relay.reshape(call_7363.astype('uint16'), relay.shape_of(var_7362))) # shape=(70, 6)
var_7374 = relay.var("var_7374", dtype = "uint16", shape = (70, 6))#candidate|7374|(70, 6)|var|uint16
bop_7375 = relay.less(bop_7365.astype('bool'), relay.reshape(var_7374.astype('bool'), relay.shape_of(bop_7365))) # shape=(70, 6)
bop_7378 = relay.less(bop_7368.astype('bool'), relay.reshape(var_7374.astype('bool'), relay.shape_of(bop_7368))) # shape=(70, 6)
func_947_call = mod.get_global_var('func_947')
func_949_call = mutated_mod.get_global_var('func_949')
call_7395 = relay.TupleGetItem(func_947_call(), 2)
call_7396 = relay.TupleGetItem(func_949_call(), 2)
func_335_call = mod.get_global_var('func_335')
func_336_call = mutated_mod.get_global_var('func_336')
call_7398 = func_335_call()
call_7399 = func_335_call()
output = relay.Tuple([call_7359,bop_7375,call_7395,call_7398,])
output2 = relay.Tuple([call_7360,bop_7378,call_7396,call_7399,])
func_7403 = relay.Function([var_7362,var_7374,], output)
mod['func_7403'] = func_7403
mod = relay.transform.InferType()(mod)
mutated_mod['func_7403'] = func_7403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7403_call = mutated_mod.get_global_var('func_7403')
var_7405 = relay.var("var_7405", dtype = "float32", shape = (70, 6))#candidate|7405|(70, 6)|var|float32
var_7406 = relay.var("var_7406", dtype = "uint16", shape = (70, 6))#candidate|7406|(70, 6)|var|uint16
call_7404 = func_7403_call(var_7405,var_7406,)
output = call_7404
func_7407 = relay.Function([var_7405,var_7406,], output)
mutated_mod['func_7407'] = func_7407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6127_call = mod.get_global_var('func_6127')
func_6128_call = mutated_mod.get_global_var('func_6128')
call_7477 = relay.TupleGetItem(func_6127_call(), 0)
call_7478 = relay.TupleGetItem(func_6128_call(), 0)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_7487 = func_579_call()
call_7488 = func_579_call()
bop_7492 = relay.not_equal(call_7487.astype('bool'), relay.reshape(call_7477.astype('bool'), relay.shape_of(call_7487))) # shape=(14, 1, 15)
bop_7495 = relay.not_equal(call_7488.astype('bool'), relay.reshape(call_7478.astype('bool'), relay.shape_of(call_7488))) # shape=(14, 1, 15)
output = relay.Tuple([bop_7492,])
output2 = relay.Tuple([bop_7495,])
func_7498 = relay.Function([], output)
mod['func_7498'] = func_7498
mod = relay.transform.InferType()(mod)
mutated_mod['func_7498'] = func_7498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7498_call = mutated_mod.get_global_var('func_7498')
call_7499 = func_7498_call()
output = call_7499
func_7500 = relay.Function([], output)
mutated_mod['func_7500'] = func_7500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3585_call = mod.get_global_var('func_3585')
func_3586_call = mutated_mod.get_global_var('func_3586')
call_7525 = relay.TupleGetItem(func_3585_call(), 0)
call_7526 = relay.TupleGetItem(func_3586_call(), 0)
output = relay.Tuple([call_7525,])
output2 = relay.Tuple([call_7526,])
func_7533 = relay.Function([], output)
mod['func_7533'] = func_7533
mod = relay.transform.InferType()(mod)
output = func_7533()
func_7534 = relay.Function([], output)
mutated_mod['func_7534'] = func_7534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2951_call = mutated_mod.get_global_var('func_2951')
call_7593 = relay.TupleGetItem(func_2949_call(), 0)
call_7594 = relay.TupleGetItem(func_2951_call(), 0)
func_1004_call = mod.get_global_var('func_1004')
func_1008_call = mutated_mod.get_global_var('func_1008')
const_7601 = relay.const(-3.901850, dtype = "float64")#candidate|7601|()|const|float64
const_7602 = relay.const([1.998806,-8.757614,7.113285,2.153751,5.826639,5.603515,-2.171679,-1.193278,-1.237626,-6.474001,-1.214394,1.671311,-9.561688,2.463714,-4.272062,-3.725729,2.941057,7.523054,-8.570618,9.130511,-8.538294,-1.627460,-2.436154,-9.097322,-0.402186,-4.899937,-8.253299,0.681795,6.544747,-3.720788,8.556397,3.530962,1.158107,1.580104,-6.356183,3.670525,-1.190219,3.998387,-2.561410,1.394544,-3.552328,8.294636,0.804438,3.530888,1.531836,-4.361563,-7.394519,0.068973,6.006690,0.033782,5.321708,-4.595737,2.979152,7.242927,2.307709,-2.085401,-5.648694,-6.643375,-1.307236,0.819407,1.985931,8.744264,6.392160,-2.619865,1.691887,-9.419719,-8.534848,-0.086811,-2.712400,-6.154875,-9.464990,-8.717563,-0.993082,3.032284,-8.123266,9.777268,-1.449795,-3.583023,1.227072,-4.296356,-3.474988,-9.234461,5.006821,-9.513124,-4.893857,-7.642434,-2.606789,8.434126,4.308823,9.053479,2.342887,-0.084246,0.898661,-0.710811,0.361555,-5.377055,6.439435,-7.729913,7.443691,3.900016,4.833471,7.930449,-5.532210,6.671355,1.350892,2.104753,0.584227,-8.544492,-6.529956,6.406323,-3.396600,-8.319081,-5.140962,-0.125711,6.399704,2.797932,2.106121,-5.337234,-9.945220,-6.644333,7.690815,-8.924827,7.710445,3.768548,7.799921,4.678364,-5.377151,-9.499815,-5.312682,6.317393,-1.156367,7.569315,4.745169,3.356993,5.051631,5.039993,1.851213,5.388985,-5.065037,1.808420,3.062285,7.877746,-3.039650,2.159332,0.542448,-0.959653,3.257927,2.880596,-7.723596,-4.626485,-8.596944,-2.152070,-6.251756,-6.108165,-5.506820,-8.430947,-2.659192,-6.154282,9.910109,-9.922853,-7.640578,-3.138054,-6.522917,-6.240539,-1.273091,-3.019614,-0.999275,2.105648,-7.060241,7.386845,7.856947,-8.128867,-2.307045,-8.968155,-3.190601,-2.654593,5.486361,6.034871,-5.330937,-4.365983,-3.869580,-0.258122,1.614154,7.283813,5.302027,2.874783,5.857949,5.821473,-5.462112,6.437879,-0.923033,0.304292,3.683808,2.086882,-3.101175,-4.047281,-6.386362,5.496593,-3.293726,2.466696,8.578008,-3.066008,-7.209763,-4.190991,9.532309,-1.004433,9.087847,-9.784893,-9.262994,5.690379,2.991284,4.628992,-5.003735,-0.601374,-6.254864,-8.633594,-9.692521,-9.760863,-9.961265,8.749594,-8.258170,0.788849,3.879958,-9.103952,6.228252,-9.432742,-9.461638,-2.830483,-9.876414,4.203842,-9.954645,-2.746129,8.329010,-2.928699,-6.958256,5.403999,7.709770,-4.058889,-2.701625,-6.796810,-0.222040,5.117459,-0.606587,8.643866,-2.988830,7.672525,4.187293,5.916342,-1.652844,-8.532446,4.903168,-4.792361,5.790323,8.130630,0.191293,5.069654,-0.448089,-3.907759,3.512330,6.584344,3.230919,-7.123791,-6.835019,6.292630,0.037354,1.829057,8.533524,1.251022,3.828405,4.642003,-3.989783,-6.907833,7.400967,-3.515854,0.048119,-4.500412,-8.023874,6.385632,-6.705504,-6.751569,-5.078203,-0.561484,7.778203,-2.554904,-0.211945,3.729418,3.470691,2.221927,5.968347,9.333881,4.408670,5.548564,-9.934857,-2.778633,2.039983,6.581020,4.383351,6.523717,7.003993,5.819375,6.756354,0.883217,-2.659246,5.988103,-5.028656,-8.361548,-0.444219,1.451786,-0.912611,9.352545,-8.835266,-4.140666,-6.079037,-2.707114,2.806353,5.126977,9.471218,3.576800,4.194630,0.819030,1.567903,3.125167,0.186552,3.066420,6.265923,7.251805,5.159083,8.903216,7.688301,2.463731,7.975328,-3.592106,8.667968,-3.188771,-4.360694,-6.213933,-2.374584,-9.246188,4.595150,3.835323,-9.220685,-7.644438,-1.723794,-7.474710,-6.325368,1.123454,-9.733554,-8.599077,3.334415,3.812342,-4.163089,-5.815265,9.375008,-7.747800,-2.565269,8.937267,-1.991803,-7.789652,5.795655,-3.468979,-0.569047,0.612914,5.947407,9.348482,0.216128,9.488452,-0.570603,-8.114999,-4.530631,-0.048100,-1.631527,6.593167,-1.552207,-0.631108,-8.914435,9.363684,-0.889001,-6.796211,-9.680162,-3.106378,-2.058389,0.583230,7.934466,-3.154691,-1.875956,-9.628594,1.469272,0.686512,5.524718,5.336040,-2.221171,1.225549,-7.493240,5.377095,9.050962,-7.361886,8.151350,-2.946422,2.584508,-3.884708,-3.548135,-1.703532,-2.159263,6.057426,1.469095,-0.319022,6.235151,-4.032193,4.396427,-6.198545,-4.325813,-7.139527,-4.221103,-5.887449,3.817915,2.645510,-2.952308,0.352101,6.681634,-3.158344,-2.054054,-0.827726,-3.460169,0.722934,-6.770235,-7.272641,-3.900709,-8.015437,-4.704041,-0.819949,4.228218,2.307762,8.668853,1.967695,2.533061,-3.521074,-4.689233,9.698534,6.561742,-0.860061,-1.753078,-5.015603,0.658618,9.027432,-5.411887,8.069211,9.576396,6.881399,-5.403522,3.608610,-0.830155,6.097835,-0.334989,-0.846611,7.789778,-1.287657,1.008940,-0.120837,7.932770,-1.046345,0.259425,-7.649857,-7.364185,3.818450,-2.466471,-5.357813,-6.596588,3.952104,-3.497741,5.987339,-5.611029,3.411242,-1.943525,-6.094642,3.205489,9.417234,-3.635379,6.616625,2.811028,6.528974,5.923997,3.892394,7.520766,8.995212,-5.446582,3.458089,-8.596593,-8.783122,-6.643129,-8.427389,-1.101873,-0.429550,3.194554,8.436493,8.386804,-5.542472,1.211202,-8.676667,-3.753150,-4.171987,-6.923610,3.517217,4.369153,-3.509612,-4.612743,2.196599,-3.202980,-9.148055,-7.649721,8.822363,-8.293612,-8.699667,4.740697,5.333630,-3.795580,-4.298688,5.882895,6.895839,5.369196,4.959830,0.518339,-7.627145,-6.261875,8.540846,7.004061,-6.863329,8.369753,9.728788], dtype = "float64")#candidate|7602|(528,)|const|float64
var_7603 = relay.var("var_7603", dtype = "float64", shape = (3360,))#candidate|7603|(3360,)|var|float64
call_7600 = relay.TupleGetItem(func_1004_call(relay.reshape(const_7601.astype('float64'), []), relay.reshape(const_7602.astype('float64'), [3, 11, 16]), relay.reshape(var_7603.astype('float64'), [420, 8]), ), 3)
call_7604 = relay.TupleGetItem(func_1008_call(relay.reshape(const_7601.astype('float64'), []), relay.reshape(const_7602.astype('float64'), [3, 11, 16]), relay.reshape(var_7603.astype('float64'), [420, 8]), ), 3)
bop_7606 = relay.right_shift(var_7603.astype('uint64'), relay.reshape(call_7600.astype('uint64'), relay.shape_of(var_7603))) # shape=(3360,)
bop_7609 = relay.right_shift(var_7603.astype('uint64'), relay.reshape(call_7604.astype('uint64'), relay.shape_of(var_7603))) # shape=(3360,)
uop_7617 = relay.sin(call_7600.astype('float64')) # shape=(420, 8)
uop_7619 = relay.sin(call_7604.astype('float64')) # shape=(420, 8)
bop_7631 = relay.logical_and(uop_7617.astype('bool'), relay.reshape(call_7600.astype('bool'), relay.shape_of(uop_7617))) # shape=(420, 8)
bop_7634 = relay.logical_and(uop_7619.astype('bool'), relay.reshape(call_7604.astype('bool'), relay.shape_of(uop_7619))) # shape=(420, 8)
output = relay.Tuple([call_7593,const_7601,const_7602,bop_7606,bop_7631,])
output2 = relay.Tuple([call_7594,const_7601,const_7602,bop_7609,bop_7634,])
func_7639 = relay.Function([var_7603,], output)
mod['func_7639'] = func_7639
mod = relay.transform.InferType()(mod)
var_7640 = relay.var("var_7640", dtype = "float64", shape = (3360,))#candidate|7640|(3360,)|var|float64
output = func_7639(var_7640)
func_7641 = relay.Function([var_7640], output)
mutated_mod['func_7641'] = func_7641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3162_call = mod.get_global_var('func_3162')
func_3163_call = mutated_mod.get_global_var('func_3163')
call_7653 = relay.TupleGetItem(func_3162_call(), 3)
call_7654 = relay.TupleGetItem(func_3163_call(), 3)
func_4252_call = mod.get_global_var('func_4252')
func_4256_call = mutated_mod.get_global_var('func_4256')
const_7656 = relay.const(2, dtype = "int64")#candidate|7656|()|const|int64
const_7657 = relay.const([-6,-9,3,8,-5,4,-5,-4,-4,-9,-1,-3,-2,6,-1,-4,-7,-10,5,8,7,3,-6,10,1,-8,-4,1], dtype = "int64")#candidate|7657|(28,)|const|int64
var_7658 = relay.var("var_7658", dtype = "int64", shape = (210, 3))#candidate|7658|(210, 3)|var|int64
call_7655 = relay.TupleGetItem(func_4252_call(relay.reshape(const_7656.astype('int64'), []), relay.reshape(const_7657.astype('int64'), [4, 7, 1]), relay.reshape(var_7658.astype('int64'), [6, 7, 15]), ), 1)
call_7659 = relay.TupleGetItem(func_4256_call(relay.reshape(const_7656.astype('int64'), []), relay.reshape(const_7657.astype('int64'), [4, 7, 1]), relay.reshape(var_7658.astype('int64'), [6, 7, 15]), ), 1)
output = relay.Tuple([call_7653,call_7655,const_7656,const_7657,var_7658,])
output2 = relay.Tuple([call_7654,call_7659,const_7656,const_7657,var_7658,])
func_7665 = relay.Function([var_7658,], output)
mod['func_7665'] = func_7665
mod = relay.transform.InferType()(mod)
mutated_mod['func_7665'] = func_7665
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7666 = relay.var("var_7666", dtype = "int64", shape = (210, 3))#candidate|7666|(210, 3)|var|int64
func_7665_call = mutated_mod.get_global_var('func_7665')
call_7667 = func_7665_call(var_7666)
output = call_7667
func_7668 = relay.Function([var_7666], output)
mutated_mod['func_7668'] = func_7668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_579_call = mod.get_global_var('func_579')
func_580_call = mutated_mod.get_global_var('func_580')
call_7677 = func_579_call()
call_7678 = func_579_call()
func_4722_call = mod.get_global_var('func_4722')
func_4724_call = mutated_mod.get_global_var('func_4724')
call_7681 = func_4722_call()
call_7682 = func_4722_call()
output = relay.Tuple([call_7677,call_7681,])
output2 = relay.Tuple([call_7678,call_7682,])
func_7698 = relay.Function([], output)
mod['func_7698'] = func_7698
mod = relay.transform.InferType()(mod)
output = func_7698()
func_7699 = relay.Function([], output)
mutated_mod['func_7699'] = func_7699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7498_call = mod.get_global_var('func_7498')
func_7500_call = mutated_mod.get_global_var('func_7500')
call_7738 = relay.TupleGetItem(func_7498_call(), 0)
call_7739 = relay.TupleGetItem(func_7500_call(), 0)
func_4553_call = mod.get_global_var('func_4553')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_7740 = func_4553_call()
call_7741 = func_4553_call()
output = relay.Tuple([call_7738,call_7740,])
output2 = relay.Tuple([call_7739,call_7741,])
func_7750 = relay.Function([], output)
mod['func_7750'] = func_7750
mod = relay.transform.InferType()(mod)
output = func_7750()
func_7751 = relay.Function([], output)
mutated_mod['func_7751'] = func_7751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_7789 = relay.TupleGetItem(func_2548_call(), 0)
call_7790 = relay.TupleGetItem(func_2549_call(), 0)
output = call_7789
output2 = call_7790
func_7792 = relay.Function([], output)
mod['func_7792'] = func_7792
mod = relay.transform.InferType()(mod)
output = func_7792()
func_7793 = relay.Function([], output)
mutated_mod['func_7793'] = func_7793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2548_call = mod.get_global_var('func_2548')
func_2549_call = mutated_mod.get_global_var('func_2549')
call_7836 = relay.TupleGetItem(func_2548_call(), 3)
call_7837 = relay.TupleGetItem(func_2549_call(), 3)
const_7855 = relay.const([[True,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,True],[False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,True,False],[True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False],[True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,True],[True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False],[False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True],[False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False],[True,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,False,False,True,True],[True,True,False,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True],[True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True],[False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,False],[True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,True,True,True,False],[True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,True],[True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False],[False,True,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False],[False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True],[False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,True],[False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True],[False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True],[True,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,True,True],[False,False,True,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False],[True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True],[False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,True],[False,False,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True],[False,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,False,False,True,True,False],[False,True,False,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False],[True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False],[True,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True],[False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,True,True,True],[True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False],[False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True],[True,True,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False],[False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False],[True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,False,True],[True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True],[True,False,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True],[True,False,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True],[True,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True],[True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True],[False,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True]], dtype = "bool")#candidate|7855|(40, 22)|const|bool
bop_7856 = relay.bitwise_or(call_7836.astype('int16'), relay.reshape(const_7855.astype('int16'), relay.shape_of(call_7836))) # shape=(40, 22)
bop_7859 = relay.bitwise_or(call_7837.astype('int16'), relay.reshape(const_7855.astype('int16'), relay.shape_of(call_7837))) # shape=(40, 22)
bop_7871 = relay.logical_or(call_7836.astype('bool'), relay.reshape(const_7855.astype('bool'), relay.shape_of(call_7836))) # shape=(40, 22)
bop_7874 = relay.logical_or(call_7837.astype('bool'), relay.reshape(const_7855.astype('bool'), relay.shape_of(call_7837))) # shape=(40, 22)
output = relay.Tuple([bop_7856,bop_7871,])
output2 = relay.Tuple([bop_7859,bop_7874,])
func_7875 = relay.Function([], output)
mod['func_7875'] = func_7875
mod = relay.transform.InferType()(mod)
output = func_7875()
func_7876 = relay.Function([], output)
mutated_mod['func_7876'] = func_7876
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7906 = relay.const([[[-1.551490,-1.208340,-3.660493,2.108419,-3.742073]],[[7.775385,9.012556,-7.749580,6.011308,-9.618919]],[[-8.041091,-2.191085,-3.797111,-9.507344,-5.700986]],[[2.472000,3.931725,-4.476927,1.139681,-8.519613]],[[5.671812,-4.897729,4.054816,-8.046658,8.456392]],[[-2.196714,9.196892,7.568919,4.757014,5.298550]],[[8.272907,-4.186641,0.221782,-8.338943,-6.340268]],[[-2.805543,-3.247493,-4.242200,-1.689988,-0.390636]],[[1.911510,8.800886,9.219985,8.798063,-1.832333]],[[-7.653420,9.049011,-3.468607,0.665035,9.201782]],[[-3.710802,0.400495,-7.238094,-9.595308,-6.101887]],[[9.062681,-7.059128,-6.168052,5.565769,-5.426608]],[[6.290453,-9.362144,1.845482,8.610548,9.586707]]], dtype = "float32")#candidate|7906|(13, 1, 5)|const|float32
uop_7907 = relay.exp(const_7906.astype('float32')) # shape=(13, 1, 5)
output = relay.Tuple([uop_7907,])
output2 = relay.Tuple([uop_7907,])
func_7914 = relay.Function([], output)
mod['func_7914'] = func_7914
mod = relay.transform.InferType()(mod)
output = func_7914()
func_7915 = relay.Function([], output)
mutated_mod['func_7915'] = func_7915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_918_call = mod.get_global_var('func_918')
func_920_call = mutated_mod.get_global_var('func_920')
call_7948 = relay.TupleGetItem(func_918_call(), 0)
call_7949 = relay.TupleGetItem(func_920_call(), 0)
var_7961 = relay.var("var_7961", dtype = "float32", shape = (14, 11, 15))#candidate|7961|(14, 11, 15)|var|float32
bop_7962 = relay.bitwise_xor(call_7948.astype('uint32'), var_7961.astype('uint32')) # shape=(14, 11, 15)
bop_7965 = relay.bitwise_xor(call_7949.astype('uint32'), var_7961.astype('uint32')) # shape=(14, 11, 15)
output = relay.Tuple([bop_7962,])
output2 = relay.Tuple([bop_7965,])
func_7969 = relay.Function([var_7961,], output)
mod['func_7969'] = func_7969
mod = relay.transform.InferType()(mod)
mutated_mod['func_7969'] = func_7969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7970 = relay.var("var_7970", dtype = "float32", shape = (14, 11, 15))#candidate|7970|(14, 11, 15)|var|float32
func_7969_call = mutated_mod.get_global_var('func_7969')
call_7971 = func_7969_call(var_7970)
output = call_7971
func_7972 = relay.Function([var_7970], output)
mutated_mod['func_7972'] = func_7972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_8027 = func_4180_call()
call_8028 = func_4180_call()
output = relay.Tuple([call_8027,])
output2 = relay.Tuple([call_8028,])
func_8029 = relay.Function([], output)
mod['func_8029'] = func_8029
mod = relay.transform.InferType()(mod)
mutated_mod['func_8029'] = func_8029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8029_call = mutated_mod.get_global_var('func_8029')
call_8030 = func_8029_call()
output = call_8030
func_8031 = relay.Function([], output)
mutated_mod['func_8031'] = func_8031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3663_call = mod.get_global_var('func_3663')
func_3664_call = mutated_mod.get_global_var('func_3664')
call_8094 = relay.TupleGetItem(func_3663_call(), 2)
call_8095 = relay.TupleGetItem(func_3664_call(), 2)
output = relay.Tuple([call_8094,])
output2 = relay.Tuple([call_8095,])
func_8097 = relay.Function([], output)
mod['func_8097'] = func_8097
mod = relay.transform.InferType()(mod)
mutated_mod['func_8097'] = func_8097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8097_call = mutated_mod.get_global_var('func_8097')
call_8098 = func_8097_call()
output = call_8098
func_8099 = relay.Function([], output)
mutated_mod['func_8099'] = func_8099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4315_call = mod.get_global_var('func_4315')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_8146 = relay.TupleGetItem(func_4315_call(), 0)
call_8147 = relay.TupleGetItem(func_4317_call(), 0)
var_8152 = relay.var("var_8152", dtype = "float32", shape = (14, 13, 15))#candidate|8152|(14, 13, 15)|var|float32
bop_8153 = relay.mod(call_8146.astype('float64'), var_8152.astype('float64')) # shape=(14, 13, 15)
bop_8156 = relay.mod(call_8147.astype('float64'), var_8152.astype('float64')) # shape=(14, 13, 15)
uop_8162 = relay.rsqrt(bop_8153.astype('float64')) # shape=(14, 13, 15)
uop_8164 = relay.rsqrt(bop_8156.astype('float64')) # shape=(14, 13, 15)
output = uop_8162
output2 = uop_8164
func_8165 = relay.Function([var_8152,], output)
mod['func_8165'] = func_8165
mod = relay.transform.InferType()(mod)
mutated_mod['func_8165'] = func_8165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8166 = relay.var("var_8166", dtype = "float32", shape = (14, 13, 15))#candidate|8166|(14, 13, 15)|var|float32
func_8165_call = mutated_mod.get_global_var('func_8165')
call_8167 = func_8165_call(var_8166)
output = call_8167
func_8168 = relay.Function([var_8166], output)
mutated_mod['func_8168'] = func_8168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6079_call = mod.get_global_var('func_6079')
func_6081_call = mutated_mod.get_global_var('func_6081')
call_8180 = relay.TupleGetItem(func_6079_call(), 1)
call_8181 = relay.TupleGetItem(func_6081_call(), 1)
func_8165_call = mod.get_global_var('func_8165')
func_8168_call = mutated_mod.get_global_var('func_8168')
var_8203 = relay.var("var_8203", dtype = "float32", shape = (2730,))#candidate|8203|(2730,)|var|float32
call_8202 = func_8165_call(relay.reshape(var_8203.astype('float32'), [14, 13, 15]))
call_8204 = func_8165_call(relay.reshape(var_8203.astype('float32'), [14, 13, 15]))
func_3480_call = mod.get_global_var('func_3480')
func_3483_call = mutated_mod.get_global_var('func_3483')
var_8235 = relay.var("var_8235", dtype = "float32", shape = (1680,))#candidate|8235|(1680,)|var|float32
call_8234 = relay.TupleGetItem(func_3480_call(relay.reshape(var_8235.astype('float32'), [14, 8, 15]), relay.reshape(var_8235.astype('int8'), [14, 8, 15]), ), 1)
call_8236 = relay.TupleGetItem(func_3483_call(relay.reshape(var_8235.astype('float32'), [14, 8, 15]), relay.reshape(var_8235.astype('int8'), [14, 8, 15]), ), 1)
output = relay.Tuple([call_8180,call_8202,var_8203,call_8234,var_8235,])
output2 = relay.Tuple([call_8181,call_8204,var_8203,call_8236,var_8235,])
func_8264 = relay.Function([var_8203,var_8235,], output)
mod['func_8264'] = func_8264
mod = relay.transform.InferType()(mod)
var_8265 = relay.var("var_8265", dtype = "float32", shape = (2730,))#candidate|8265|(2730,)|var|float32
var_8266 = relay.var("var_8266", dtype = "float32", shape = (1680,))#candidate|8266|(1680,)|var|float32
output = func_8264(var_8265,var_8266,)
func_8267 = relay.Function([var_8265,var_8266,], output)
mutated_mod['func_8267'] = func_8267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3705_call = mod.get_global_var('func_3705')
func_3707_call = mutated_mod.get_global_var('func_3707')
call_8443 = relay.TupleGetItem(func_3705_call(), 0)
call_8444 = relay.TupleGetItem(func_3707_call(), 0)
func_4958_call = mod.get_global_var('func_4958')
func_4959_call = mutated_mod.get_global_var('func_4959')
call_8451 = relay.TupleGetItem(func_4958_call(), 2)
call_8452 = relay.TupleGetItem(func_4959_call(), 2)
output = relay.Tuple([call_8443,call_8451,])
output2 = relay.Tuple([call_8444,call_8452,])
func_8475 = relay.Function([], output)
mod['func_8475'] = func_8475
mod = relay.transform.InferType()(mod)
mutated_mod['func_8475'] = func_8475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8475_call = mutated_mod.get_global_var('func_8475')
call_8476 = func_8475_call()
output = call_8476
func_8477 = relay.Function([], output)
mutated_mod['func_8477'] = func_8477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_8514 = relay.TupleGetItem(func_188_call(), 0)
call_8515 = relay.TupleGetItem(func_189_call(), 0)
func_2688_call = mod.get_global_var('func_2688')
func_2690_call = mutated_mod.get_global_var('func_2690')
call_8521 = relay.TupleGetItem(func_2688_call(), 1)
call_8522 = relay.TupleGetItem(func_2690_call(), 1)
func_4095_call = mod.get_global_var('func_4095')
func_4096_call = mutated_mod.get_global_var('func_4096')
call_8524 = relay.TupleGetItem(func_4095_call(), 0)
call_8525 = relay.TupleGetItem(func_4096_call(), 0)
bop_8531 = relay.logical_xor(call_8524.astype('int32'), relay.reshape(call_8521.astype('int32'), relay.shape_of(call_8524))) # shape=(14, 1, 15)
bop_8534 = relay.logical_xor(call_8525.astype('int32'), relay.reshape(call_8522.astype('int32'), relay.shape_of(call_8525))) # shape=(14, 1, 15)
func_3705_call = mod.get_global_var('func_3705')
func_3707_call = mutated_mod.get_global_var('func_3707')
call_8539 = relay.TupleGetItem(func_3705_call(), 0)
call_8540 = relay.TupleGetItem(func_3707_call(), 0)
func_674_call = mod.get_global_var('func_674')
func_676_call = mutated_mod.get_global_var('func_676')
const_8548 = relay.const([-9.696769,-8.375299,7.881373,8.832863,8.635329,-2.453982,-4.455524,7.361754,9.130577,-7.504707,2.287534,-0.148728,-5.039919,2.183831,6.485789,9.186383,-5.225180,1.125683,-1.047652,8.791521,9.733793,5.654418,-6.681478,9.289306,-9.126671,-9.494748,-8.802297,1.679285,-0.594325,-6.629415,1.123981,-3.245727,1.951698,3.136211,-8.192327,-1.596313,-8.047345,2.671421,-3.240165,-6.259396,-7.632664,-4.246726,2.892731,-0.201149,-0.952544,-6.998663,-4.601770,2.670800,-4.009533,3.086076,1.598639,7.050472,6.994880,-3.359181,6.047894,6.341347,-4.238278,-2.927926,0.389791,0.809600,9.023241,-4.812228,-7.934009,7.509111,-9.102750,-4.775484,-2.855110,-2.098026,-7.936391,8.288315,6.807154,-9.115020,-8.945455,-3.383308,6.724900,5.831339,8.279456,-6.651478,-6.612221,-9.697756,-4.095706,-2.051189,-1.195054,4.613779,-2.231780,-6.101959,9.714131,5.767606,0.949474,8.678959,3.112418,3.171860,-0.843065,4.485950,-0.334925,-9.805486,-9.843951,6.907942,5.539311,6.695452,-9.860991,2.807324,-4.945863,5.203287,-7.853475,-8.133729,-6.361921,-6.522618,7.462350,4.591647,-2.041326,2.821559,-1.625163,0.508710,1.880420,3.200686,7.164056,7.573491,3.744857,9.529271,9.092744,-9.291194,-9.321883,9.475470,-9.144410,3.376600,-7.110545,5.307844,5.964656,-1.646142,3.763365,-3.306114,-6.782548,4.512797,4.442771,-5.879681,-6.928722,-6.331219,7.119863,9.166394,-6.930737,-2.456699,4.860169,5.957911,3.485963,2.196315,-0.279098,8.814462,4.238817,-7.983566,3.257638,3.514718,4.045757,-5.540140,7.815304,-6.649070,-1.563598,-9.354614,-9.853840,8.837836,0.660675,1.646887,-9.214801,6.843363,4.951520,-9.998661,-7.878338,-6.869086,2.474151,-5.010481,-0.217913,-6.461391,-0.983977,-5.003648,3.769328,-8.952379,-5.565698,-0.787746,-5.311853,-8.683079,5.365733,-4.582793,6.410692,-1.555727,-2.474082,1.598625,9.071329,7.348872,3.581254,1.931355,9.450574,3.943590,2.246923,4.540967,9.512974,5.180462,-5.449366,-6.164615,-2.993346,2.352735,-6.501153,-3.230648,-1.091678,7.672625,3.070458,-2.687346,-4.426441,4.309965,2.839919,9.177780,-1.253900,-3.091224,-1.830910,-5.162381,5.192012,0.373503,8.704048,7.525522,-4.365094,8.927146,4.233822,-4.910375,0.705083,9.829450,-9.151435,-5.306582,4.202444,-3.650395,6.552063,6.383299,-1.803862,-7.722446,-6.745282,3.891926,-4.090543,-0.043457,9.742172,4.362212,-0.104647,9.866009,9.827195,-9.102289,-4.707470,5.338025,6.559696,-6.108069,7.684715,1.691242,2.803900,-2.118022,2.920524,0.277687,-7.931749,-0.219303,-6.097020,7.177434,1.188645,-3.898535,-7.033371,2.400050,-3.539694,7.280601,0.930560,1.086489,-0.413653,-9.222239,7.566827,-6.888749,5.790808,-1.127571,-4.272478,1.550887,5.726112,-3.837637,6.483413,-6.795584,0.987856,-7.346203,-0.714427,2.101250,5.553598,5.956339,-4.150446,-8.816306,-6.997550,5.303313,9.973283,-1.798900,-6.705624,-6.098483,-9.102542,-0.362638,8.831063,-5.048063,-6.463131,-5.482642,-5.132957,-0.474693,1.311952,-9.683608,-1.357503,-2.110156,-2.294305,-0.277228,7.078776,1.910315,9.631373,-1.655084,-3.127687,4.018551,-6.230981,-9.599005,1.857224,1.006421,-3.243873,-7.383738,8.543091,-9.050878,0.802833,5.765099,1.481966,-8.722932,-9.914616,8.054231,-2.039369,8.793553,-3.543230,5.652859,9.506762,-2.868160,-3.232197,-2.378728,-8.237491,0.245944,4.156693,-9.012229,7.134614,-8.155489,2.107002,-0.406460,-2.115989,5.458452,-8.057878,-4.880047,5.538128,8.329924,9.751177,-6.068240,-3.912534,8.487593,-6.644733,-4.935132,-7.527497,4.683692,8.645548,6.951687,6.526935,-9.452631,4.347380,1.812420,-2.936057,-2.404544,-1.904736,0.657455,0.410152,5.301742,-5.155748,1.645203,-7.213996,9.719000,0.941058,5.939871,0.918897,-6.585931,-5.643322,9.452779,-3.752787,-3.606132,-0.693812,4.529194,-9.631800,2.661371,-0.041021,7.409605,0.761283,-9.056262,-4.996422,-9.507720,-8.889633,-1.331802,-9.445916,1.369593,-8.507453,-0.748296,6.029026,-0.574702,-7.378863,-8.588018,-7.180347,4.329122,-9.626243,-2.144186,9.022344,-1.347404,9.753135,-5.836869,4.700744,-7.933099,6.804139,-6.375626,-9.969131,-6.045490,5.402440,-5.664991,-6.185598,7.376364,8.858832,2.918765,-4.496826,-2.057504,7.800020,-4.018462,-7.229064,-8.620662,1.654726,-5.939150,8.634462,-5.972100,-2.452045,-6.258615,-2.250900,8.619221,-6.038754,-0.661738,4.020563,-2.927001,9.058271,2.483313,-6.308054,1.998136,-5.685023,0.402523,-1.040401,-8.911665,-4.672299,0.998946,1.057629,3.903002,-0.100816,-1.057562,-1.887754,-7.599246,8.713657,-1.046786,0.941709,0.321385,1.521716,7.332359,-6.198173,-6.774090,-0.037210,9.320261,2.002634,2.692365,-1.009781,7.717048,3.551807,-6.978306,7.984327,-7.642683,-3.757525,-7.693736,-9.670441,0.463796,-8.986812,-6.629752,-0.800714,-0.536356,-2.374904,9.820953,8.016549,9.002894,-3.802851,-5.138118,-1.587976,-6.696538,-0.382592,4.763997,-2.505522,-9.354173,-8.754691,6.628799,-6.678516,-9.157170,-5.859712,-7.881942,-8.046195,-9.594283,3.560435,-4.314331,8.419987,2.446872,-3.981854,-7.257153,1.390071,9.866944,9.031314,-9.550973,-4.424211,-4.640300,-7.367513,-6.774083,7.200444,0.672483,3.012376,-6.793286,-9.573498,1.883540,-7.709570,7.311388,-1.270957,-5.781785,-6.041543,8.965029,6.163554,1.666414,-3.204036,0.963378,-9.882231,1.008178,-2.985915,-6.314027,3.531137,4.922811,9.133077,4.983862,9.534722,-2.066053,6.484451,-8.152585,3.467602,-2.566426,-3.090579,0.084295,5.376689,-4.781366,0.478454,-9.772841,-8.597942,-6.038851,2.210578,2.710921,8.012112,-0.570513,-0.369371,-7.517247,-8.338978,3.922791,-9.961035,8.965106,8.378134,2.833968,-1.098335,9.181721,-7.236583,-0.262775,-1.767288,-7.255911,4.565860,-2.326650,-0.776501,-9.076502,7.464048,1.418758,-1.676645,2.279621,-7.369579,-0.680830,8.994974,-3.091832,-5.401911,0.047024,-3.670053,-7.296609,-6.049581,4.731350,6.112239,2.821397,-3.884652,-2.762090,3.444008,-7.941859,3.071733,-4.757849,6.666109,-2.007081,8.378497,-4.963814,6.956474,-2.388341,5.226385,-5.941095,4.469533,0.950309,-6.617370,-7.323603,-9.630906,-3.876356,-2.015856,-7.875048,1.671603,6.847624,-8.408449,-8.551942,-7.538642,9.998832,8.857839,3.310746,8.021156,-0.526208,-2.489766,9.323006,3.117173,-6.816710,-8.787197,6.996046,3.102708,-4.864473,-5.338312,-6.615402,3.428470,-5.427184,5.724327,4.250056,2.378379,0.843430,4.878932,-7.829335,-3.031631,-3.242238,6.197462,-1.468287,-3.475891,-0.439314,5.497533,2.169950,-8.091913,6.958825,5.105821,-4.027351,-0.536064,5.893304,-2.944830,1.330878,-9.115708,2.286994,0.377651,0.155601,-8.266625,7.457442,-0.792311,3.564920,-5.998893,-4.686847,8.670344,-5.818335,-9.823930,6.619543,6.418662,9.863536,-0.613500,8.560808,-8.224417,0.828961,-5.268834,4.352087,-3.705177,8.491512,1.239657,-5.008779,-2.821702,6.458894,-5.443838,5.683310,7.214685,-7.971102,6.552906,2.985295,-0.303499,8.506034,2.437936,6.627829,5.056768,8.435302,-9.282481,2.291525,-5.611715,-4.343796,-1.027363,2.254823,-2.458610,0.591570,9.740713,-8.179254,-3.308686,9.898216,-9.002955,2.686885,2.785076,-3.590666,-4.090689,2.364054,-2.819110,-0.034083,7.566477,-2.442506,6.545751,-4.209148,0.021014,-4.533265,-3.109131,9.536477,-6.149220,-2.899259,4.352345,4.482511,-9.394942,1.517703,-6.411382,1.231293,5.377490,-7.238183,-9.270375,0.401422,4.978664,5.690735,5.782124,-0.341889,4.109073,-9.999561,2.675764,-3.044723,-4.579029,0.633133,4.363015,-5.668226,-1.133426,6.166790,0.540520,-7.290057,-7.870407,-7.711381,6.499189,8.572236,4.161656,8.117410,-5.401135,9.923139,4.171495,8.407124,5.678692,6.535612,-0.404264,-2.931286,-1.289774,-7.437417,-0.511013,-0.427494,0.921401,-4.568192,4.326078,-0.235015,-1.810780,-9.068838,-0.688904,-4.493667,-8.063176,9.445353,6.359746,-7.108003,9.438388,-6.245615,-2.630523,2.603026,7.390119,-2.866207,0.741074,-1.520382,-5.032191,-0.299970,-7.026421,4.856930,-7.108446,-1.255142,-1.117602,1.767034,4.958560,-6.227506,8.303069,-9.666305,4.337720,5.255424,5.850859,-5.017951,3.000797,-0.936108,-1.436423,-4.909514,-9.633065,-5.159757,1.461877,-8.615292,1.791911,-4.606808,-2.728509,9.829024,-1.861739,2.227293,-9.790934,7.901750,-3.746963,-2.214785,3.043351,6.505577,9.417447,8.491651,-5.435439,4.094185,-4.111600,-7.620367,-9.269115,-8.581313,-6.251561,-7.222124,-5.017405,-9.884905,3.148325,3.190756,9.925573,2.349191,-0.879436,-8.059530,-0.876608,-0.940005,8.897129,-5.365949,7.228432,-7.978584,-3.273172,-1.310415,2.778305,7.198463,1.722012,4.910730,6.498943,0.518348,3.299597,-7.584105,-5.102379,-8.434196,6.122265,7.248985,-1.858224,9.014345,9.003787,2.561450,-1.866774,3.331738,8.974828,4.028691,7.097044,-1.973221,-7.567362,3.843290,1.866015,-6.928478,-4.230896,0.860144,-7.815598,6.402056,7.656543,-7.655848,9.566930,9.001316,-6.161264,6.107626,-0.429499,4.648563,7.209958,8.994412,-8.135141,1.467450,5.961041,0.774181,6.500046,8.539809,0.573153,3.034443,-4.125681,4.571138,6.196392,-9.225017,-9.254230,-3.878829,-6.576283,6.088144,8.313656,7.496420,0.634460,-7.839461,3.565799,8.894457,0.309943,6.725052,-9.142220,2.900136,-1.490372,2.006260,2.366303,-9.944518,9.651463,-1.936788,-1.968270,9.348957,1.911712,7.252428,-1.319488,6.869709,1.172848,5.700425,-2.163054,8.599430,-5.245993,4.380343,-6.658400,-3.679691,7.873299,-5.971697,-1.286187,-7.778753,-6.867195,4.818668,-6.027027,-5.935301,5.476351,2.823602,-0.392506,-0.909979,2.404851,-6.546108,6.992896,0.928364,-8.892270,0.747922,-5.014917,-5.869881,2.722020,5.648453,-9.438144,4.752030,3.574676,2.622596,8.324940,-8.524177,-9.415410,-0.846187,2.608936,-9.745642,6.271848,5.725750,5.305468,-3.065350,9.193243,3.609444,-9.065340,5.431885,8.516668,1.213109,6.328220,-8.893742,2.401696,4.844416,-6.860536,-1.039147,7.145260,1.262852,2.207035,9.989682,1.952529,-9.140100,6.435900,7.060924,7.449723,5.378090,1.749385,-6.135378,-7.629100,1.483941,0.327914,1.820148,5.513723,-9.760289,-2.764559,3.049010,-9.907841,9.549497,-3.931514,-8.009886,-4.269644,-5.319026,1.091247,-9.185421,-8.985372,0.553630,0.889501,2.278104,1.834931,6.206653,4.449680,-7.172281,-4.668705,-5.374832,-3.759531,-8.083332,-1.606248,-6.503127,2.931083,-2.111738,7.587282,-5.156997,-5.855644,8.827496,2.992957,0.717251,-7.184227,-7.154596,-5.278164,1.728098,4.889296,9.199889,-2.501272,-9.376990,-1.808219,6.714158,-6.800947,-3.605448,7.545837,-8.107556,-2.686741,-9.867460,1.272053,3.920977,4.751918,5.477567,3.287353,-7.798462,-3.349228,1.624647,8.546614,-4.368086,-0.984948,-2.856704,6.666009,-3.267050,4.487962,-6.023286,5.177284,-7.582128,-4.483121,-6.343891,-6.869630,9.990211,6.708629,7.468534,0.639422,-9.701167,-4.955629,-9.922401,8.917181,0.314402,1.326525,-0.386339,7.344551,4.991878,-2.046366,2.595893,-7.551894,6.232911,-3.221405,9.515145,2.507697,1.323980,-7.186838,5.015079,4.964317,-8.746442,-8.904999,0.423998,9.854585,0.536220,-1.760066,-3.640047,4.371627,-2.439731,-0.519526,9.846973,9.880857,5.332496,-6.841214,-7.452474,2.274311,-0.391060,5.924955,-6.129914,-2.429445,-5.964979,-1.186723,-0.246221,-9.175874,0.979477,-0.027121,-3.943689,-9.325981,4.500017,-5.212525,-0.843084,3.959937,7.826648,-1.780740,8.100609,0.375228,-2.779889,4.230057,5.405623,5.756795,-0.412607,-5.412231,-8.045935,5.618344,8.988833,2.384110,1.976431,3.593498,9.038699,-2.464081,-6.691212,-6.531246,-3.277381,7.273466,5.731561,-7.996667,-7.926346,1.428841,3.423201,3.264240,-2.157869,-1.129353,8.497318,6.171332,-5.054302,3.307848,2.292368,0.202546,0.257629,-1.697080,1.451933,6.952979,2.093630,-7.160519,0.731355,1.095288,-6.020216,2.790835,0.452291,-5.713282,0.467336,3.421781,7.917663,-2.060480,0.985265,-0.647371,4.728530,2.971745,-0.282290,-9.495769,5.532973,7.119011,7.631127,6.934888,3.254068,-2.940815,3.983891,-6.639518,-4.781296,-8.119706,5.438565,8.581779,-2.008078,6.789516,-9.010997,-1.503931,6.426683,-6.298075,-7.240901,-5.539477,3.215159,-9.227523,-2.191230,-1.315558,6.508534,-8.369713,3.789277,-9.233210,-4.969704,-4.668989,9.964906,-7.116916,-9.274595,3.899385,-8.777499,7.159307,8.865435,1.700943,-3.835132,-1.362946,-7.860372,-2.188997,-1.763613,2.786182,-3.721781,-7.631789,-2.599215,-2.701931,6.620081,2.496580,3.001849,9.696458,7.137432,-6.677581,-9.757716,7.329000,-9.827572,-3.111458,-2.427285,5.424992,1.796961,-9.713789,7.101854,3.856787,7.477485,-8.501810,4.786795,5.990341,-1.371625,-5.538902,-0.126463,1.981602,9.491826,-5.095811,3.546197,-3.840131,3.401752,-9.484794,5.730640,6.273346,7.145507,-0.698411,9.081681,8.435838,2.759130,9.179901,9.723583,-4.229050,-1.439207,3.360767,9.138786,3.804058,-3.566806,3.523492,8.808001,-9.581411,-8.898891,9.379394,-5.209094,-1.625713,-6.497032,-7.586160,-0.689637,-6.751567,1.439186,3.023250,7.107979,4.622853,-0.972331,0.443862,9.400682,-1.598274,-4.306665,1.091697,-4.781798,5.276174,8.854003,9.405820,-3.962628,8.090589,0.441495,-5.059879,3.879809,-5.252161,-1.751521,1.569647,-6.210713,-9.590420,4.573034,6.796032,7.338239,-8.932632,-1.279956,-4.947206,8.105250,-8.732466,-4.398966,6.846423,-6.463005,-3.124261,1.293947,-1.466763,4.436948,5.775425,0.384788,3.730767,8.971622,6.002589,6.626139,-2.824217,0.408038,9.203009,-9.511736,5.227609,-4.606433,4.950167,0.721855,6.839658,-4.651292,9.420785,-7.348784,-0.923075,-5.741750,1.280581,-5.073934,-0.681131,3.443304,4.431923,-6.070617,-7.143035,-7.620075,0.153907,-7.600565,3.236768,0.834542,-4.391849,0.300482,1.201466,-7.856798,7.473602,-2.270635,1.569717,9.094754,7.163698,7.916322,-0.395129,-8.727945,-5.996020,1.687446,9.903260,-3.931296,-3.863562,4.656622,-6.094632,-3.127537,-0.855672,0.340448,-7.449667,-0.167967,7.805724,-3.092413,-7.775985,0.507062,6.399171,-8.942592,3.064006,-4.256409,-8.804347,6.032741,7.371617,-1.598617,-6.221430,4.086006,-5.094419,0.974780,-9.618131,6.999024,-1.537438,1.471586,1.781381,-1.309193,-9.388003,-4.558465,-1.745526,5.051456,-8.790624,8.578770,-1.605671,5.133022,8.119153,-5.448541,-2.951807,-5.351823,-7.099645,-4.650925,4.662574,-2.691629,1.087315,-7.542092,-1.961906,-6.981718,3.528912,7.991061,-5.938589,-2.208772,3.946758,8.026710,-9.126560,-5.298317,6.498923,6.336263,-2.642268,1.199871,-0.655634,6.116031,4.983772,9.475082,-4.715838,-3.095026,-2.600737,-6.416028,7.532267,0.582480,1.656476,-3.896511,2.212420,9.000996,9.838358,8.531959,-0.457698,-8.848169,-7.352009,-2.028395,8.551652,-2.174020,8.116669,3.393732,-3.242599,-9.141972,2.171795,4.399923,-6.740193,-5.914925,1.249994,-9.561431,-3.988611,5.306871,-4.564493,4.394508,8.687892,6.473889,-9.978185,0.938486,-4.496684,-8.776572,3.144214,-1.718576,-5.334234,6.204938,-5.311266,3.644329,9.243727,-1.465513,-6.573729,7.427799,1.531591,-9.668932,7.980915,-4.521404,-8.104130,5.510629,-3.425244,7.019053,-9.625106,-5.941734,-6.533796,-3.500206,4.726923,-0.586386,-8.424246,0.083323,-9.147881,-1.050814,7.338658,6.796523,6.674892,7.879604,-9.699040,5.749136,-3.414461,-8.970839,5.656523,-4.031075,7.714241,7.460194,-3.648241,3.059351,-6.376081,-2.130074,-9.062698,7.975061,8.899078,-4.234060,-5.936363,-6.009762,5.569268,5.983937,8.731330,2.459489,-3.855376,8.824207,8.980743,-5.452975,-3.675598,-1.603527,-5.760616,-1.614378,-3.884263,-9.945679,-1.003836,5.709396,6.044677,6.341186,-9.821445,5.066483,8.198883,4.028924,6.269599,-3.043887,4.075436,-5.694051,1.206152,2.923068,5.729697,-1.390463,-8.071158,-0.771060,-1.022932,9.854170,-2.072930,-3.402848,3.869257,7.101278,9.406198,-1.890013,-0.653066,-4.890843,9.694832,1.799437,2.510943,6.432333,-4.004908,9.842903,2.498793,2.809046,9.064414,6.340847,-6.547433,9.708089,-8.521802,-1.950371,8.291331,-9.026699,-0.343135,5.786017,0.025124,4.692977,-3.723080,7.166697,8.803950,-7.939058,-2.442970,2.759506,-9.623071,-3.605239,-2.486979,6.748129,5.527857,4.789555,1.899418,-8.690940,8.304501,-6.462854,-2.424224,5.909595,0.398632,4.713085,7.201778,-9.771270,7.905157,-2.941310,3.012046,0.092840,-6.149480,-2.317351,-8.687152,-2.461152,-1.659545,7.415957,-9.246799,3.195702,-4.410208,6.658179,2.700507,7.813124,-7.497652,1.251989,7.884139,8.626300,8.696518,-3.597151,-3.004581,3.264256,8.913426,7.670359,9.926291,3.424888,5.136612,2.246524,-6.017185,-2.221387,-2.105260,-6.313369,-7.562203,3.207040,1.267224,1.926799,6.677180,3.285680,-3.454317,-3.242508,1.370485,8.731728,5.569806,8.347960,-1.346554,-7.866758,2.138173,-4.484057,-5.215908,9.225444,5.206514,2.566607,3.153723,-9.210705,-8.601422,6.244644,-9.645801,-9.102493,3.303087,-0.117661,0.002908,3.082249,3.933956,3.316034,9.933967,-9.085483,9.846688,5.998301,-0.561354,-5.976322,6.277198,-0.550506,7.515362,9.969119,-6.496992,-2.852425,-0.115112,2.877480,8.159203,-5.387866,5.538604,-6.388303,-6.622379,-0.330821,3.084563,0.870934,-6.947659,-3.348009,8.102154,2.254246,1.208305,7.044383,1.405346,-2.986299,0.878401,5.095004,4.585309,-1.673939,-8.028334,-3.208038,3.470540,-0.942251,7.424392,6.834423,-8.761398,-8.030395,-1.883894,0.568872,-1.830542,4.274499,-8.708147,7.619474,-4.711179,-9.582212,-4.382000,-3.030402,-2.573576,5.412927,5.962967,-2.939117,2.888004,-8.314231,5.703061,0.461258,9.526967,6.259328,-9.057835,3.743636,-7.629721,8.319544,-3.242133,4.018167,-7.674525,-2.253027,5.175237,8.187537,9.561807,2.831063,5.215787,4.431804,4.836462,1.006159,4.336431,-9.055932,-6.152590,-4.617612,0.755731,5.883128,-6.613905,8.482566,5.003462,8.501915,-5.071624,5.672421,8.416015,-4.107725,1.264246,-6.844738,-3.754219,8.613653,-0.207851,0.694792,0.791926,8.666767,-6.689870,9.310392,3.311851,0.341620,8.997653,-1.561605,5.299728,0.078196,-1.293426,9.331691,-9.322732,2.765707,-8.939703,-0.424768,0.901509,0.542944,0.453765,4.264577,9.942513,-4.858509,0.261489,-2.307950,-1.300046,-8.600952,4.712091,8.286394,-5.143502,6.194245,-9.320980,-3.139485,9.226809,9.523683,-5.267807,-4.953440,6.480305,1.124669,8.533433,3.045939,1.182289,-3.379227,7.464766,7.337496,-9.807137,-9.924835,-8.642969,-9.594012,2.646689,-8.077449,7.361699,2.103158,-5.041969,6.943957,-3.586477,0.698135,-0.822010,4.827613,1.256222,4.702064,5.005236,-4.439131,-0.481243,4.194258,5.452786,-1.229517,-5.632494,0.753720,-3.011252,-8.881400,-8.821762,-7.002272,2.928024,-5.748307,-5.130671,-9.864733,-3.909618,-1.425430,-0.879554,-7.341861,9.110965,-6.436664,-6.398668,-9.545277,-6.085668,-8.377009,-1.435077,-6.492070,-8.794702,2.507209,-1.406335,-3.278040,-4.134469,-0.204096,-9.071830,-5.237001,4.230834,-8.642270,2.091065,-2.582029,6.855606,-3.382420,1.840108,-8.589538,3.036737,0.265630,5.609123,-3.520289,-5.769285,-7.973614,3.502394,-6.431118,8.583647,2.202210,-9.858566,8.287641,-2.245890,5.698802,-2.181028,4.745900,1.177569,2.012847,-9.462182,2.714599,-2.166517,2.753630,-8.907806,-5.803416,-1.082326,-7.902336,3.993601,5.993826,6.972635,-2.253852,-0.600025,-7.482730,-0.855484,-3.326786,8.805759,4.400310,-0.433101,-3.999291,-7.929042,-2.732657,-5.959453,9.186599,-2.340623,6.853748,-5.101215,2.766900,5.374915,-8.636847,-1.312268,-5.756129,-6.090949,8.491114,-2.594354,-8.919039,5.028879,-4.459837,9.286484,7.961311,-8.600447,-3.017582,-2.195971,2.431113,9.173898,5.730312,-0.908069,0.848543,9.030119,0.076048,-4.880956,8.491501,8.299328,0.400113,2.997288,-8.425999,4.471356,-9.720694,9.507350,4.280030,-1.745711,-7.208069,-2.880395,5.975625,-1.311746,-7.934714,-7.538836,-6.856479,8.124186,7.750695,6.875525,-9.994724,-6.802140,-9.741499,-2.061945,-2.156227,8.795625,5.516529,-2.955681,6.032797,-0.677689,-0.525005,9.076228,-6.585927,-6.253735,-7.429785,7.713474,7.245106,4.957298,5.388475,9.807459,-5.112435,-7.288709,0.161190,0.315673,-5.779915,-4.706623,-6.709295,7.457734,-7.252317,-9.175563,3.569819,5.306270,6.966451,7.555587,-9.595202,-0.740932,4.743359,-3.106916,-6.880699,6.472568,9.832274,0.801168,-4.276162,-9.964801,-4.513179,2.651319,9.050255,-8.903219,2.009261,2.122014,1.576889,4.604619,2.415571,4.589298,8.791256,-5.607260,-3.178757,-2.289116,-2.732154,3.402182,-6.708369,0.168706,8.168128,-9.657614,6.106358,-8.472886,-0.965705,7.425528,8.811858,7.492515,0.984494,-9.561081,1.559725,-7.981611,1.508349,-4.166496,-5.815416,1.845694,-1.676072,2.667206,-9.339092,-1.150075,4.554857,-5.892977,-3.126869,9.758180,0.342232,5.646926,-2.871040,-2.398972,5.680044,7.073038,-6.022263,9.671432,6.783389,-3.110973,-3.566730,-2.855491,-1.565018,-3.194173,-9.567747,5.697392,1.890877,-7.369734,-1.400360,-6.386806,2.732712,-8.087611,-4.187601,-1.819176,-8.749155,4.293190,6.440526,-3.346506,-9.580026,-6.860655,-8.475613,-0.889939,-4.061550,3.490795,-7.342995,-3.050059,-9.989304,6.715110,-2.903744,-2.206187,6.867612,4.332051,9.337021,-5.495311,2.315332,-7.656878,-4.473636,8.012160,8.059875,-1.696812,-3.641182,9.474928,2.249835,-3.934049,4.739699,-4.040427,-8.564198,7.931473,1.065802,-0.999518,1.569439,-1.398928,4.272471,-0.393230,-6.404335,-5.401125,-1.601952,2.244091,7.866930,1.634223,-5.432281,0.294845,-5.306381,-1.565234,-7.665725,-7.670748,5.871619,-0.044579,-7.266950,0.404462,8.340073,-7.556333,-3.845846,3.391132,6.765145,-8.685749,-2.227480,-6.565665,-6.690017,-7.415281,1.118426,-4.202030,6.877431,-1.255261,-8.573297,-0.631059,8.708522,0.333209,2.879709,2.462477,3.373267,-5.879260,2.388606,-5.970873,-8.514439,7.198580,1.788096,-8.581081,-0.217601,6.800531,7.048556,-1.862851,-1.173822,-0.712144,-7.881760,-8.195063,7.674914,0.676622,4.043974,-8.148841,-6.606150,-8.264542,-6.597149,-2.527344,4.646010,0.334777,9.359388,2.766773,4.995646,6.688959,-1.251030,3.096749,0.079313,-7.996898,1.750139,-3.278350,-3.737272,4.274500,2.913644,7.898773,6.247209,6.470433,-7.371566,-5.269527,-5.144315,9.028800,5.320496,-6.861871,5.915885,-1.088104,-3.319390,-2.262783,9.872901,7.845683,8.432268,3.942356,3.326670,-7.694358,9.663651,5.466253,-6.722849,-3.411284,3.085362,-3.151918,-9.667554,5.178856,8.690799,2.278153,-8.645967,-4.470325,-6.950287,-9.271881,-8.623395,7.334342,-9.449092,-0.818357,-3.207827,-9.572661,0.258049,-1.737006,6.462082,-3.963845,-9.046164,9.761562,-4.528213,-6.021761,3.382223,-6.544411,3.190262,-4.158718,-9.337247,5.611155,0.896928,4.564859,-4.610198,-5.857231,3.864878,7.383140,3.209245,-1.090785,-6.019170,-4.705639,-3.533727,7.406884,-3.791563,7.202229,-4.647298,2.266915,-9.748416,6.243877,8.021514,8.127360,-3.675533,-3.503273,3.181828,-0.500189,1.383496,-5.026864,3.670314,-0.006734,1.063443,8.328132,-1.174107,5.048786,3.483240,5.660311,3.989232,1.809240,8.489306,4.875224,3.555251,-5.006094,-9.485114,-7.915332,6.167964,1.797224,-4.593150,-3.474305,-1.684665,4.362084,-5.708356,-7.051977,8.877160,-0.242026,3.561951,-2.288099,1.079936,2.428918,4.302834,5.482494,-7.776824,8.032176,7.251470,0.725437,0.230141,6.135093,-4.580320,5.816901,-5.047795,-8.955968,8.113753,-1.695763,-2.408345,-9.782801,9.009125,-2.419529,9.491962,-7.247535,0.175218,-3.415827,-1.626763,4.820648,5.837545,2.935982,-9.100726,3.565569,-0.815952,-2.763392,0.128826,-0.874677,-6.012777,1.524130,-9.068330,7.554418,3.336184,-4.025753,3.210934,-1.084938,1.100964,-0.124791,-7.735610,1.035876,4.529158,0.746160,9.145004,0.258974,-3.346686,5.152602,-8.434228,-5.154347,-0.607103,-4.742863,-7.265493,-6.872377,-3.947798,9.938938,-2.684335,9.771852,-6.235851,-5.485500,-9.913390,-6.092718,-2.793911,0.479530,-4.161662,3.228381,-0.208594,-9.713246,-6.545750,-1.780931,-6.724884,4.571965,5.496320,-1.806698,1.748213,8.966048,8.868661,-7.229619,6.216177,-8.540241,-2.730482,-8.256747,3.088948,1.482621,9.739232,-1.983643,-1.223556,-3.264399,-5.398802,1.264914,0.323018,0.372958,-3.823297,5.662203,3.504944,4.557362,5.821324,6.655866,2.306176,-4.091142,-8.977866,-1.858102,2.709316,-6.130291,5.272428,4.030725,-1.641016,0.110840,7.516889,-9.263366,7.848374,-7.130929,5.557249,1.601829,-9.199983,6.106598,7.930546,1.187531,-8.629938,-8.947240,-2.774129,4.097918,0.969829,7.656941,3.401194,1.949045,-5.862217,7.415832,5.889094,-2.765049,-4.984005,0.268014,7.703848,-0.117242,-3.931822,0.626945,6.373453,-6.429758,-3.599311,3.837726,2.620945,-3.305331,-0.535021,-0.644673,-5.891213,3.129395,-5.960046,-8.751273,-3.090834,-8.091930,-3.780934,7.694724,-5.877086,-7.101298,2.746293,-6.836183,-2.270909,-5.710849,-5.350971,4.930216,9.718723,8.531959,5.815022,9.828375,5.704846,-9.346984,-9.379329,3.625687,2.072782,5.288860,3.384334,-4.628649,-0.526486,-1.025109,9.888024,5.246042,-7.643907,-2.718929,0.753581,0.808669,9.412039,-4.087828,2.577284,-1.045582,5.482801,-7.454529,0.806057,-4.011871,4.712958,-5.315941,-1.478746,-6.942230,2.039802,-1.963366,-3.609848,6.691522,-7.232188,3.874258,9.657194,-9.632333,6.670085,0.360468,8.866841,-9.102525,-1.033156,5.632448,2.140448,4.456738,6.816076,6.155278,-4.428795,8.729811,-2.581111,-8.796914,5.735469,-5.464907,0.302499,6.357639,1.816792,-8.869702,4.123491,0.354114,6.045900,0.792565,-0.968950,-2.440198,7.318404,6.527748,4.578224,3.587639,6.214620,1.951833,7.538547,3.067672,8.621190,-6.236634,-2.256168,0.825325,-8.189107,-1.431877,0.683282,2.521634,-1.590939,-2.676083,9.303560,-4.171246,2.132864,2.570340,7.818655,4.573941,-4.930447,5.040870,5.316697,-9.374842,7.630182,3.512461,-5.988852,2.187152,5.379765,-0.378284,0.189176,9.531827,-7.477650,5.678933,-0.919243,-6.517009,-2.911534,3.695855,-3.823251,3.461423,-0.869612,-6.829366,-3.879087,1.934844,3.014906,-3.263829,7.844470,3.396206,-2.770172,3.302039,-7.671560,-5.515610,4.525815,-7.546282,4.922561,7.756050,-0.460504,-3.907455,1.257241,3.071345,0.127742,1.584698,0.558200,3.910840,8.435286,-7.169234,-6.939360,-0.300323,-1.823748,-0.072546,-0.034407,4.585760,6.589267,6.512307,-3.297964,-5.088543,-0.095037,-1.272727,-3.422814,-4.522637,-8.873193,4.500999,0.847386,-7.419158,8.900336,8.038046,-1.757077,-5.144115,4.627827,-7.134801,-2.653232,7.917107,-3.130645,2.912350,3.428346,-1.144152,-4.463165,0.997514,5.496026,-2.732563,-0.837815,-3.691177,-5.811947,-9.871597,0.352907,4.639578,9.137373,-8.506786,-5.027503,3.747819,7.048285,3.093866,9.091686,3.815169,-6.916414,3.714662,-7.998118,0.792878,0.428279,-2.974742,-5.801420,-8.057659,-5.131785,0.939106,-9.684062,0.918318,-3.258517,-1.503952,3.175831,-3.688377,4.890136,-0.399932,-2.330154,-2.975113,8.632216,-4.183231,0.402537,-2.045795,0.800543,-8.657412,-4.471528,-2.984070,3.277761,-8.040797,-9.273711,-9.034208,8.970696,7.400715,7.362154,7.585983,-2.530444,-2.726617,-7.152305,-3.043518,9.015147,-2.306035,-4.313192,-0.608955,5.974289,-3.453911,-3.103352,7.387048,8.586061,2.814057,-5.840311,4.444590,-3.411102,-9.520036,-1.574738,-2.473703,-0.198319,9.455833,6.392995,-5.510035,6.107919,2.419096,6.051051,3.653933,7.305445,4.162821,3.493230,2.086217,8.741178,-7.812996,-6.268234,2.729242,8.343060,6.507378,-6.485297,5.174813,-5.318507,6.757365,2.140839,-2.808938,1.126798,4.082854,-5.699158,-8.470149,-4.513138,-7.293869,-0.296072,9.029495,-9.202952,-8.875401,-5.260653,-3.648455,-9.281161,8.910693,-1.802538,3.181906,0.469060,-1.898868,0.496000,4.733394,-6.350879,-9.802241,6.736572,-0.914328,-5.552311,2.486785,6.320082,9.055457,2.723748,9.053263,-4.902642,-3.963673,6.285947,3.722556,1.668052,2.235023,-5.226008,-8.291269,6.621548,-9.599131,-5.590504,7.045613,5.553323,9.167242,2.229531,7.806125,2.585581,6.937819,-5.240228,0.996246,-7.690625,2.931281,-6.270953,-9.026185,7.338277,3.657987,-8.320224,3.072531,0.757912,0.284798,1.388691,-1.083925,-5.040786,-8.818818,5.389686,-9.618648,-9.111464,-0.395132,-0.307877,-9.034164,6.859959,7.068447,-4.299007,-0.710294,9.111117,-6.330712,-7.358535,-8.685607,0.041501,8.289699,-2.294387,-1.796803,-1.964349,-7.523547,4.702616,-3.727509,-9.598770,7.738185,-5.832344,8.779666,9.179746,-1.079033,-5.974536,-9.314721,7.536017,-4.129997,5.201448,-6.155155,-2.905475,-7.628639,-0.472772,-0.956762,-7.769856,5.830832,6.502958,7.398929,3.495300,-6.337035,-4.240534,4.534945,2.391292,9.984902,-8.404666,-3.020804,-6.832017,-4.763640,9.800580,-3.906918,-9.577923,-7.487464,-7.333234,-2.530257,2.547253,4.133176,2.618486,-5.378365,1.771392,-3.041756,8.494803,-6.310118,0.997539,-6.812390,4.220913,9.132706,1.466747,-6.250481,7.048730,1.034433,6.605612,-1.199403,8.355097,1.832642,-6.309968,-9.331541,-5.035340,-8.567636,1.020418,-1.982452,1.152304,9.802766,7.627082,-5.138900,-3.206611,-8.253984,-1.303461,6.121082,6.842345,-4.609974,-2.343661,6.470201,6.471931,-2.074487,1.069688,-8.649947,-3.219296,2.268910,1.163566,-3.806108,4.765884,1.353299,8.563783,0.619757,-3.011796,9.578250,-4.400370,9.002067,-3.811746,-9.720633,1.478170,-2.118339,-3.091954,7.702994,3.487146,-4.323775,-5.704145,-5.467758,-9.495077,-5.232099,-7.008831,0.535579,4.470766,-9.503089,-7.801668,7.330565,6.497155,-8.997282,6.886879,6.768751,0.921815,2.116080,-5.265492,-6.571384,6.163105,7.289869,-0.980966,-0.501623,5.154655,6.083816,2.759996,9.543126,-4.770475,3.992677,-9.799354,-0.639199,-8.168321,5.509260,8.115153,5.610129,4.704992,-9.649873,4.588734,1.623010,-5.267072,-4.251378,6.357507,-0.714060,2.276072,0.849372,0.573032,-4.771963,2.268675,-3.079251,2.359682,7.763849,-3.632702,-6.063586,-0.168621,-0.427271,-6.822769,-8.584802,8.829330,7.768128,-4.760868,-2.231616,-0.525650,8.609078,-4.097630,-0.637067,5.529612,-3.577086,-1.232450,1.315726,-2.176079,2.708213,4.987898,-5.152961,-6.037125,1.249305,-0.873085,-5.549704,-5.975924,-8.904133,1.740144,-7.162105,-0.451282,-0.119554,9.528602,1.195064,-7.632789,-9.231727,6.621596,-6.172403,-8.612629,-5.297510,4.371343,9.712947,0.426134,-6.176461,8.586799,0.805438,-0.441733,-2.859334,-3.068901,5.286533,-3.123544,-4.627040,3.421477,9.080425,-5.255860,-9.988050,9.334900,-1.332323,-2.351294,1.848703,0.361689,0.160394,8.173516,-1.784865,-4.693042,-1.020464,2.568547,-6.402256,4.672674,5.884512,3.900298,5.847165,6.089151,8.577641,-8.914702,1.426393,-6.442993,9.758053,-6.961293,2.392177,-5.397545,9.665840,-9.835950,-4.892495,-1.982046,6.072226,9.202156,-5.730306,-5.845909,-1.864318,-3.153096,7.492464,3.984430,-0.823998,-6.713646,-2.742546,9.842157,-2.913584,8.737124,2.984487,-8.585331,2.777978,9.395520,3.304613,-2.347351,9.279789,5.246239,4.680510,9.233836,5.127299,8.928015,-7.323807,7.348234,-9.961613,3.120282,-0.200210,-9.000335,-8.106435,5.859807,-8.100745,3.580717,3.783168,-6.895970,5.539638,-1.465971,2.573029,-4.295080,2.971656,-9.233166,-5.919603,6.361685,-1.162398,7.087436,-4.621044,-9.663325,-3.438876,-0.099655,-1.179423,-4.427581,-2.303692,-1.535902,-8.922321,-1.910217,4.450021,6.609112,-8.925809,-8.047381,-8.394745,6.654915,3.470183,6.759806,-0.209037,3.053576,-4.787013,-5.957096,-0.227097,-5.348012,-3.675996,-2.629951,-9.413895,3.108017,4.306079,0.303685,7.118928,-1.994433,-9.417492,-2.406318,7.602180,1.284355,6.231282,-5.950574,7.670555,-6.642890,0.054279,9.607782,-1.642855,3.913237,-0.223586,-6.819707,7.328738,-2.098912,-7.852406,-1.048483,-1.978554,-1.310755,-2.113196,-3.126331,6.152429,5.554847,8.431213,-1.853292,8.538385,1.229277,-8.488468,-8.296408,-8.621626,5.706914,7.106940,-5.855850,-7.682459,-1.371070,-9.977960,-1.960881,1.985336,-6.810325,-5.726944,5.275293,-1.766801,7.622115,-2.736056,4.737775,1.100352,1.188430,-1.389831,-9.670588,-8.677059,9.791540,2.460978,5.845723,1.367884,-2.752247,-3.904254,-4.675967,-7.022201,-0.481079,0.228577,-5.248087,-0.005836,9.781219,2.481074,6.819343,-1.492998,-5.850197,-6.249028,0.684027,-3.634990,8.261396,0.990247,8.900723,-0.008829,-2.744566,1.439031,-5.107537,-5.736912,5.811385,2.047865,-5.903728,7.655758,-5.197458,-6.661619,-6.323335,3.640127,5.485940,1.783873,-6.533848,-4.836683,7.632478,6.843346,-1.939317,3.811938,-9.227537,-1.694254,0.723483,4.321503,-5.060252,1.192804,-4.547341,-7.442859,5.826637,9.653437,9.843428,-7.356020,6.966401,-8.319508,6.447027,2.498224,7.430107,-0.297694,-3.451443,-7.372068,2.824384,4.229904,-9.664216,-4.749786,3.616320,0.812476,6.025050,9.959000,-3.316206,-3.925545,3.909519,7.098057,-9.229747,3.040470,6.268368,4.930531,4.791574,2.984643,-1.855598,3.529249,1.699766,5.590290,-0.931351,7.507729,-8.313826,5.969294,-5.644587,-2.702218,-8.493363,2.625798,7.136371,9.747331,3.337778,-3.086541,-3.025951,6.967488,6.868048,-5.269876,3.348089,-7.405393,-8.607692,4.353508,-2.442992,9.427712,-0.724668,-9.079982,6.293432,-7.645093,-0.750136,-8.761737,0.464580,-8.512391,-5.882684,-9.822817,6.108536,-6.159665,-9.496441,-1.239411,9.348223,-6.975692,-2.024034,-3.664648,-4.128621,-2.775431,7.754270,9.498820,-1.827617,6.409486,-1.131599,-7.101078,-7.479216,8.009338,-5.735303,3.705714,6.498461,0.964867,0.860838,2.174172,6.337557,-9.053529,2.554160,4.926864,-7.755170,-7.102292,-4.333335,-3.050503,4.819210,-5.055562,6.780679,-2.290557,4.929708,-7.609138,0.720582,-8.158503,1.222592,5.097475,-9.611350,-3.338178,-2.437770,0.455087,4.236053,8.055510,-6.138272,-4.039885,-9.789910,-3.598678,5.568221,-3.670760,2.895329,9.136419,6.295492,7.361703,4.391408,-4.384671,-3.972481], dtype = "float64")#candidate|8548|(3360,)|const|float64
call_8547 = relay.TupleGetItem(func_674_call(relay.reshape(const_8548.astype('float64'), [14, 16, 15])), 2)
call_8549 = relay.TupleGetItem(func_676_call(relay.reshape(const_8548.astype('float64'), [14, 16, 15])), 2)
output = relay.Tuple([call_8514,bop_8531,call_8539,call_8547,const_8548,])
output2 = relay.Tuple([call_8515,bop_8534,call_8540,call_8549,const_8548,])
func_8559 = relay.Function([], output)
mod['func_8559'] = func_8559
mod = relay.transform.InferType()(mod)
output = func_8559()
func_8560 = relay.Function([], output)
mutated_mod['func_8560'] = func_8560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7750_call = mod.get_global_var('func_7750')
func_7751_call = mutated_mod.get_global_var('func_7751')
call_8625 = relay.TupleGetItem(func_7750_call(), 0)
call_8626 = relay.TupleGetItem(func_7751_call(), 0)
func_7328_call = mod.get_global_var('func_7328')
func_7330_call = mutated_mod.get_global_var('func_7330')
call_8627 = relay.TupleGetItem(func_7328_call(), 0)
call_8628 = relay.TupleGetItem(func_7330_call(), 0)
func_5798_call = mod.get_global_var('func_5798')
func_5799_call = mutated_mod.get_global_var('func_5799')
call_8639 = relay.TupleGetItem(func_5798_call(), 0)
call_8640 = relay.TupleGetItem(func_5799_call(), 0)
func_5744_call = mod.get_global_var('func_5744')
func_5746_call = mutated_mod.get_global_var('func_5746')
call_8644 = relay.TupleGetItem(func_5744_call(), 1)
call_8645 = relay.TupleGetItem(func_5746_call(), 1)
func_5981_call = mod.get_global_var('func_5981')
func_5983_call = mutated_mod.get_global_var('func_5983')
call_8649 = relay.TupleGetItem(func_5981_call(), 0)
call_8650 = relay.TupleGetItem(func_5983_call(), 0)
func_2053_call = mod.get_global_var('func_2053')
func_2054_call = mutated_mod.get_global_var('func_2054')
call_8686 = relay.TupleGetItem(func_2053_call(), 0)
call_8687 = relay.TupleGetItem(func_2054_call(), 0)
output = relay.Tuple([call_8625,call_8627,call_8639,call_8644,call_8649,call_8686,])
output2 = relay.Tuple([call_8626,call_8628,call_8640,call_8645,call_8650,call_8687,])
func_8701 = relay.Function([], output)
mod['func_8701'] = func_8701
mod = relay.transform.InferType()(mod)
output = func_8701()
func_8702 = relay.Function([], output)
mutated_mod['func_8702'] = func_8702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_8735 = relay.TupleGetItem(func_209_call(), 0)
call_8736 = relay.TupleGetItem(func_210_call(), 0)
const_8752 = relay.const([[[8.506920,-2.724342,-5.987888,6.243262,4.606455,-8.371649,-0.165618,0.451415,-8.464096,-2.290634,-0.431855,-6.340238,3.358905,-9.704283,-9.636463],[-4.470008,4.758944,-2.928650,-1.517022,-7.474080,-5.651536,5.842401,2.794978,2.775045,-9.999036,1.880107,-1.951829,-0.094612,2.679663,9.556444],[-1.225823,-3.603761,-1.701307,-2.140976,-2.142996,7.059480,9.438624,-5.151868,7.826533,8.987509,9.756890,-8.534428,-8.220420,-6.092221,-3.738382],[8.482092,0.163052,-5.142423,0.952800,-1.258604,1.717628,-0.661232,-4.678440,-4.845483,9.417412,-8.965080,-6.693883,-4.309024,3.855087,-9.251991],[-2.352936,-1.525632,5.704438,-4.327534,2.870892,0.390159,-3.235142,-9.635125,-6.515528,-1.848176,-5.575382,-9.779380,0.410303,9.773499,5.099444],[-6.034248,8.790600,7.497472,-0.621248,2.125248,-2.251586,-1.321690,4.476863,-8.292403,9.420731,4.403608,7.731365,-6.846659,-8.386919,5.747520],[-0.965963,8.780502,-9.379691,-2.215543,-9.824676,7.540469,-6.870349,9.241208,-5.387193,1.385731,-7.359074,1.492567,6.662348,2.511150,8.605746],[6.386613,-6.853678,1.111480,-6.815273,8.526939,-0.803991,8.016476,6.347276,-3.519658,-8.821052,1.490186,-1.509972,-5.319968,0.920292,6.769804],[-4.667790,-8.145408,5.234711,-0.305859,1.572239,4.644580,-4.807858,7.529382,6.817623,2.327850,4.073781,9.563483,5.945336,4.554217,1.534110],[4.311776,-3.250950,-7.057432,7.206777,9.465332,7.614312,-6.158870,8.530182,8.627028,8.751471,1.005247,5.959877,-3.960857,-5.930041,8.521862],[-2.709898,-4.043210,-0.856903,3.448703,0.414188,2.828963,7.215890,-1.279295,9.604720,0.086087,-9.736083,3.330241,6.275672,-7.695260,-9.381169],[9.342215,-9.321508,6.076811,1.273444,-6.824572,7.878215,7.465534,-2.380700,1.988665,0.996057,-7.470510,8.721865,6.715339,-8.484793,0.731098],[-6.490229,3.279560,-0.704466,7.335139,6.832834,-3.805451,1.611526,9.164184,6.170565,0.498823,-6.334500,-3.893773,-2.137792,-8.552856,8.866887],[9.512491,0.377864,-5.301244,9.528279,7.039815,4.906140,0.692354,9.521130,-2.018988,3.685718,7.077566,-4.984923,-2.663813,0.283679,7.439993],[-7.900109,-5.356461,9.160840,4.177556,7.997899,-0.728791,-4.454563,1.352486,-0.141109,-6.197051,-7.492980,8.852683,4.326044,4.333788,7.623390],[7.282439,7.369682,7.566793,-9.022148,7.552139,5.035713,-4.971337,4.266417,1.384548,-7.434491,0.735743,2.373871,4.786077,-4.815943,5.836871]],[[9.916443,0.774071,6.421435,8.563877,3.496585,2.475574,-9.088741,-8.313130,3.101449,-0.707290,1.084233,-6.992472,-4.738240,3.917458,-4.084653],[-2.380868,1.021429,-0.776443,-0.625572,-2.607399,-0.470033,-2.054705,-1.866626,-0.434789,-5.815954,1.596569,4.023304,-8.347573,9.904766,-7.036166],[6.826425,6.404525,1.425011,0.129396,5.236185,3.102334,4.597014,9.294095,4.317789,9.771805,-7.248538,6.426990,1.853039,6.698139,-3.008804],[-7.407050,1.427277,-2.016266,-0.410095,-9.217832,-8.075226,1.468095,-8.629338,2.217826,5.279891,7.810267,7.406420,2.114470,5.796782,0.410736],[-2.108019,1.372899,3.235432,-9.093329,0.542810,7.420750,8.266348,5.419586,4.440078,1.857427,8.089488,-9.578121,7.543179,2.795736,4.938113],[-3.518036,2.032443,8.133907,-9.326634,-8.183996,-7.309988,7.739869,-9.971197,4.534567,5.555764,-1.321876,-7.456423,1.443595,-9.237016,-2.750623],[9.573157,-6.844063,-1.707312,3.070547,1.802252,-2.920948,7.422542,7.591279,-4.875206,-7.269593,6.043187,-1.528534,0.083262,-6.368625,4.496718],[5.884213,1.853414,5.303717,4.934674,-9.778274,-6.276471,7.696887,-4.624389,6.649634,0.178238,-5.792508,4.510107,-0.089826,-2.894726,-5.200161],[2.778510,-8.518708,2.794667,-4.246894,-0.220151,-1.943150,3.374847,6.960381,-5.470375,-3.540027,-0.834175,7.632657,-0.280497,-4.215639,-8.872608],[-4.026859,2.721908,-4.347772,-2.030739,0.946920,-3.789475,4.216769,3.548039,0.353533,9.921592,-7.425785,4.395346,1.825042,3.035142,-6.634258],[9.457067,-5.032126,-2.159595,2.112566,3.987192,6.921474,-3.928558,-5.906078,9.373018,-7.796606,7.974247,-5.131139,-1.076738,-5.297649,-6.880481],[6.983726,8.333074,-4.710188,-4.882598,-2.095121,-3.853518,6.248812,-5.721122,3.701139,-8.604626,1.349578,-2.438053,-5.338220,9.465195,-1.044406],[5.261305,4.233958,5.274538,-9.684449,-9.939941,-8.446552,9.327708,8.669775,2.184196,7.961278,-3.923005,5.769679,2.418260,1.688552,2.619985],[-7.099587,7.264989,7.044685,2.730205,7.594868,7.187901,-0.557994,7.178331,-3.336393,-3.576359,-6.021573,-9.636328,7.582162,4.591348,4.921871],[3.099765,-4.015982,6.718107,0.770740,8.377179,-7.377316,-5.845927,7.234090,8.626966,-1.512013,-3.079963,-2.474315,2.965084,-5.004138,4.870108],[7.935659,0.582340,6.209686,7.992804,8.636127,5.798539,6.256574,-9.512623,-6.195814,2.040568,-6.144791,1.977136,-0.478063,-5.091998,-3.724304]],[[-5.005233,-7.048236,8.762630,1.001608,5.353249,2.993686,-2.946630,-6.957694,-7.428247,-2.376058,-5.509689,3.657511,-0.768733,-1.088817,-1.770202],[-0.086107,-7.728486,-1.879210,-8.066075,-1.803297,-5.469905,2.202112,4.171041,8.799156,-2.907651,8.906229,-3.080873,-3.718425,-0.022127,-6.593755],[2.669231,-2.521167,6.343828,8.269845,-9.174049,9.193188,-2.161186,5.676869,1.476389,4.925274,6.041900,-1.544509,2.512293,-4.727164,8.201705],[-4.590438,5.080610,-6.954209,1.811099,-5.166652,4.389317,-8.014033,-0.757658,8.056557,-3.437173,1.490213,7.121083,-3.723697,1.953501,7.789562],[6.271043,1.123588,-3.598727,5.727759,-0.597744,0.091179,-8.865175,0.225613,6.619774,-1.442469,2.531608,6.705636,7.974957,5.905075,-8.101919],[2.421330,-0.906765,-0.141980,-5.644507,-4.348747,-9.590857,-6.077566,5.123329,0.961532,0.749033,-5.014956,-2.547111,9.279441,0.381345,-4.554570],[2.724415,0.453361,-3.227951,-7.846967,-8.679998,0.338276,-4.462530,5.041160,1.678445,8.853405,-4.734151,9.318749,4.081808,-1.438411,6.917887],[1.549854,-3.756048,-3.081979,-0.230868,6.287948,6.502085,7.467549,-0.595142,1.040441,-1.044821,-0.992501,2.421353,5.054393,5.678202,4.164676],[-0.426559,2.193963,-6.440955,2.625337,0.365345,8.772806,-5.828699,-4.538269,7.653814,-9.541524,-8.110591,-9.759544,6.463935,7.839333,5.287075],[0.386145,1.034583,-2.769631,7.898616,-8.547706,-5.788964,2.478003,3.252690,2.230921,-0.454775,-4.775501,1.730234,-0.450101,-0.048502,2.841177],[-4.025713,7.952798,7.707319,3.744609,0.854392,5.230480,7.049272,-7.793980,0.444401,0.499071,-1.531731,-3.691693,-6.849150,-0.461732,-4.766224],[-3.430117,-7.528723,-7.888119,2.693385,-1.681956,-9.555840,-2.248145,9.824376,-5.978539,6.581452,-3.645497,3.425248,8.674014,7.588936,-4.603961],[8.146066,-3.165846,-7.434248,7.270485,1.254824,-6.503450,-9.399061,8.538246,-3.103806,-1.491278,-3.376403,7.013600,2.826867,8.539254,-7.008022],[3.170696,6.025319,8.673759,-0.315017,1.936179,7.215986,2.636568,4.397960,3.931425,-0.740950,0.112938,-8.319279,-2.469525,2.141867,-0.823133],[3.046895,3.688101,5.992996,-1.515714,6.261640,1.172088,-4.161527,-0.142962,-0.917860,8.910229,0.871864,6.075332,9.877991,-0.807585,5.901412],[-2.901141,-7.383027,2.107179,-2.887118,7.172615,-6.429756,-5.784978,-1.800144,-0.675809,-8.249796,1.053451,-2.060552,5.141846,4.575891,-3.997527]],[[-6.191788,9.317861,-6.431986,7.959550,4.728025,-9.544729,4.920190,-3.765832,-7.397772,-0.765893,-3.026541,-4.719820,-6.650679,-3.439614,6.110040],[0.701138,4.512049,-9.982212,5.514993,-9.977212,8.652090,-0.504540,-0.968725,-3.689449,6.557621,9.854207,-0.070697,-8.915797,-6.133897,-8.696408],[9.280095,6.044988,6.204148,-1.925609,8.231486,1.695717,-1.897598,-4.143325,-7.029150,9.721561,0.745076,1.152461,-9.691257,2.391036,-6.488909],[0.691626,5.492686,-1.945232,-7.735303,0.074249,3.183266,-6.058880,0.415681,-6.768439,9.184691,5.740296,1.667738,4.327716,8.893727,-3.870403],[-5.109836,8.451997,-3.500063,-3.416426,2.358807,0.091014,-2.288065,-8.187296,-2.304142,0.183434,-6.885431,-5.100413,1.390112,8.974708,-4.834123],[-1.496971,3.646425,-8.340394,3.296411,0.915969,0.430819,-3.639568,-0.978998,8.345803,8.192339,3.897532,2.912535,0.941649,7.629765,3.087092],[-4.588539,-4.722941,-8.632474,-2.842089,-4.579990,-4.272218,-0.887090,7.059100,1.361088,9.264608,-3.263739,-5.691852,-9.281113,-6.812574,-7.233698],[-1.575501,-4.410266,8.496261,2.433635,-5.757707,6.114419,4.477192,1.362746,-2.133144,2.514150,-6.281705,-0.540863,-0.782732,-1.194475,-0.851809],[-2.639481,-0.994937,-4.788853,6.555052,8.213159,7.612759,-5.412126,-8.003362,7.723382,-3.269032,-1.658535,-1.510308,6.890124,8.086151,-2.899296],[8.819816,-1.316868,5.914785,7.852419,3.009680,-5.722144,6.130086,2.315046,7.785981,-0.230685,-9.979632,-6.301732,-7.056782,9.583278,8.166743],[2.270151,-3.359681,-4.066837,-3.464864,4.924507,-4.986625,-2.299376,-9.554130,2.518145,8.541247,-5.624551,-6.703669,-9.632911,-7.706703,0.087447],[7.532055,-2.640245,-5.386912,5.372161,-6.149649,-7.460383,3.271233,-1.091733,6.434940,9.534835,-9.215558,-1.818923,-0.911385,6.434199,-7.697123],[-3.659321,7.519677,0.034586,-4.823396,9.001065,8.019717,6.390974,-7.230489,6.628803,-4.675980,-8.731771,-9.084451,9.418416,-2.098744,1.589798],[0.023562,-1.142715,0.009954,7.804796,1.150664,-2.311017,-1.428811,8.810451,-5.227887,-9.966595,1.224765,8.885654,8.572813,-5.570828,3.505490],[-7.141362,5.706536,2.379658,6.103533,-4.457083,1.794721,2.688984,3.161336,6.726177,4.759400,-1.371453,-5.065872,-8.184046,-9.963013,9.753411],[9.731781,6.992077,0.203249,9.398083,2.741669,2.409001,-0.512007,-3.930225,6.342026,6.390282,-5.820109,1.701773,6.341574,-8.159795,-0.722926]],[[7.738482,-3.197241,-9.660640,-3.912292,-6.386408,-0.605579,-5.479960,-2.713873,-9.738073,-6.963462,3.466814,0.692979,-4.053895,-3.177559,-9.178689],[-5.273332,-9.755430,-4.531551,-9.519805,-6.426241,-7.164461,-6.685419,-9.949066,-3.896800,-1.083406,-6.443199,8.668214,-5.297008,4.054779,-3.535237],[7.995530,2.683069,1.091784,5.193901,-0.115694,-2.130196,-9.207391,-8.311862,-2.066338,2.832830,6.320712,-7.309513,6.356100,-6.428323,6.767176],[-1.966060,-8.059857,7.689763,-3.147136,3.275556,-9.624687,1.468459,4.322718,7.934988,-1.313861,-3.450303,8.984501,-8.810958,-9.873789,3.260531],[-2.750351,-1.795612,7.471146,-2.853131,-1.706260,4.681867,-8.913139,9.570345,-9.386464,9.388993,0.524713,-9.240803,-4.014159,1.274500,-6.407143],[-7.742275,2.476800,4.793918,-2.270410,-3.191706,0.758130,-2.996133,-1.809347,8.416141,-6.889031,-4.885042,2.509212,-0.769264,6.633996,-6.439667],[-5.108257,-8.180796,9.802293,3.063208,-0.058751,4.490932,0.929927,7.889037,7.229209,-7.995213,0.562192,-5.096528,2.182651,-3.567574,-0.974876],[-4.943500,6.474273,-4.272093,-3.937173,1.371258,2.823330,4.325048,-9.204916,4.566613,0.831535,4.900045,-1.144223,9.276347,4.396947,-1.584541],[-4.140738,-4.409779,-1.623237,4.060474,-0.748805,2.619588,5.016200,-1.199816,4.768483,2.679990,1.195270,3.956778,-3.544594,-7.769258,-4.429931],[-0.710496,9.032573,-0.193400,5.814736,0.076719,-0.899297,-6.888198,2.962381,5.933937,-7.080261,3.715344,-2.508368,2.376235,-1.544606,-2.750806],[-8.216809,0.046464,8.855361,3.672529,2.921574,9.264923,7.807778,4.636484,-2.578486,9.365585,-1.305756,9.162581,8.542914,4.862214,-6.707503],[-0.991145,-1.183958,-6.020347,-2.732874,0.235940,-9.892440,3.193115,-6.395993,-1.525329,-7.887525,8.311080,2.125732,3.503329,4.766413,-4.453453],[-5.016108,-7.053338,-0.572108,-2.735909,9.921891,1.416456,-7.929946,8.057740,9.704217,-4.992258,-3.862518,-5.030459,-4.120632,-7.836131,3.132295],[3.007124,-5.004151,-2.167951,-2.866082,8.199597,-2.474634,-2.197170,2.765342,6.559709,0.541455,-3.075266,8.840712,6.471329,-8.559119,6.474524],[-0.327858,5.061886,9.767149,-4.625365,9.933894,9.020542,-7.333509,-1.272068,8.688711,-4.598346,9.312978,-0.113975,-4.329521,-8.213359,-6.562914],[-7.909449,-7.138552,8.253009,9.519122,-3.074396,6.529401,2.675801,5.715876,5.768764,4.350646,9.950347,9.159344,-6.646128,-4.066362,-5.140586]],[[-0.537026,0.773372,2.043333,-2.136163,-3.585469,8.909977,-7.031448,9.490103,-9.278438,5.095935,3.941639,1.764412,-2.039030,-9.620134,-3.107803],[9.517810,2.011366,-8.968667,5.694427,6.472587,9.772890,7.479998,9.410165,7.858297,-8.212187,-7.386587,6.882311,-0.076384,7.238153,-8.149681],[9.073302,-7.621122,1.916387,6.757842,-8.458744,-7.315822,5.886620,6.594326,2.411239,9.431871,2.978802,5.519573,6.452975,9.440809,-2.406506],[-8.950665,9.223355,-5.077984,4.147478,-0.880239,-5.143320,3.008473,-3.145709,7.820836,5.411146,1.914786,-7.644100,-9.323325,-7.286121,-9.606249],[2.465950,8.856745,7.108027,6.021938,3.764635,-6.497349,7.121901,-2.133217,3.529323,5.998772,-5.538203,6.896262,5.540905,-1.546452,5.155858],[-3.679136,7.182462,-9.139344,6.328068,-9.804528,5.939571,-2.204414,-3.627296,-6.764972,-5.624043,8.629598,5.678076,2.184339,-7.005276,-1.117402],[-8.382049,-8.117360,-8.609916,1.765946,7.557319,6.528878,-5.732383,0.131596,-8.853131,-9.185324,1.769940,6.518169,6.863216,5.797556,-4.907601],[1.266195,-5.661744,-7.078674,-1.131213,-8.157975,2.586239,-6.730144,5.074729,4.277186,-4.500688,2.155882,8.092066,-2.644056,7.386224,-6.112306],[3.375330,4.669561,2.349502,3.229417,5.899226,4.204176,7.124541,-2.146086,1.324650,-6.234736,-3.762243,9.069974,-2.388041,-0.186685,8.735264],[5.368272,-9.703540,-2.087752,-9.947483,-6.285685,6.916970,4.078237,1.488943,-3.984032,7.366705,-1.737118,-6.844404,1.318759,2.305054,-4.036637],[-5.131417,-1.403153,-7.564563,-7.278029,-7.506989,-5.809244,7.119725,-8.170645,-0.143927,4.480818,7.132977,3.042444,-7.692675,-7.712738,-4.912920],[-7.756190,-9.245059,7.249820,-9.469496,4.989174,-1.272169,-2.486133,2.093112,5.823917,1.881622,9.132106,-6.898171,-7.913248,8.800343,2.796328],[-5.280409,-9.699996,-4.952272,4.019914,-6.297351,7.303860,8.515033,-6.316350,-2.443606,-2.238709,-1.545509,-5.537239,-4.848418,6.975239,9.835767],[1.136065,1.310032,-7.540047,5.329933,-2.172535,-1.489244,1.742226,0.509345,7.352965,5.093416,-1.847371,9.969707,-3.205352,0.582950,-5.743139],[-0.105282,-3.133411,0.681124,5.205217,2.605871,-0.198024,8.752857,7.231643,6.958789,-9.841055,-8.484690,5.190504,5.653962,8.431504,6.452728],[7.440220,4.468495,2.517262,-0.515611,7.603191,-5.113487,-9.425069,6.368409,5.510771,-4.802826,5.618753,-9.396409,-6.979143,5.182465,-2.136450]],[[4.537609,-8.041607,-2.285751,-1.385259,2.509662,-0.557405,1.473431,3.523083,-8.661755,-6.863071,9.851962,3.522642,-1.274061,8.670128,3.767859],[-6.685103,-4.610881,7.939421,7.330057,1.705219,4.146674,-6.836099,-6.815226,-8.712123,-7.146739,2.993769,-9.919609,9.555634,1.980988,-3.109784],[5.248954,8.595500,-0.688153,-4.345415,-8.962566,-1.765010,9.890844,8.062009,-6.300080,-2.751188,-8.679653,-9.170046,-6.904496,5.162472,8.086464],[-6.240012,-8.720207,-4.878967,-0.443401,-8.706581,-5.161572,-6.555203,-0.806782,-8.342282,9.286224,3.799632,-1.773505,6.326272,-4.120420,-6.367392],[-1.747479,-2.186145,0.364674,8.717126,0.806248,-5.676650,-2.671270,0.755355,-3.800597,-4.110518,-1.061175,8.971913,9.162081,9.393260,6.467003],[5.761061,-4.485142,9.532007,-7.849640,9.097890,-6.885742,-8.448194,-8.812834,3.613512,9.737218,1.189692,-0.336411,-4.911706,9.966458,9.512126],[-5.415724,-7.326138,-3.423310,-5.587720,3.287880,-6.110217,8.167457,-0.882389,-8.708798,6.523322,4.815067,7.560116,3.467373,-2.765338,3.556545],[-1.249937,-0.494195,-5.004996,-6.376356,-4.287873,-5.173355,9.287240,7.199458,7.399800,-5.050667,3.489406,3.951413,4.030459,-5.320043,1.828700],[4.250444,2.450643,1.409548,-1.126594,-4.208434,8.259924,8.577057,4.444070,-7.078580,-2.218393,3.311711,4.363868,-0.431684,6.348378,-5.231629],[-0.262452,-9.264832,1.702937,4.523948,6.741996,-9.046495,-1.222791,-3.090289,-3.421130,-4.502449,2.094960,-4.072972,9.315330,4.887132,-3.941609],[9.190102,6.206056,-5.923452,3.641027,-8.874627,-2.167687,9.934751,-8.510650,-8.589602,9.423211,6.511100,-4.971019,7.087709,-9.317178,-9.152612],[-1.366872,5.993110,-0.617778,-1.924238,5.982914,-5.270475,-3.623196,-5.352398,5.032677,8.164963,3.591937,4.066755,2.109741,8.839805,2.516125],[-3.619395,-2.752967,6.049969,3.829616,-0.940533,-9.825660,-6.225552,0.612596,5.521669,5.511953,0.753563,2.412757,-8.270627,2.924009,-0.093370],[-9.097488,-0.698833,-9.443397,0.170495,2.486104,-0.391077,-2.345415,-4.640893,6.459026,3.492082,1.378489,-2.377303,6.095030,7.537224,-4.338010],[-9.946781,-5.281125,8.205207,-4.300252,-9.209953,1.529164,-2.866309,-4.541504,8.118616,-1.571642,-3.166579,5.861778,6.803572,-8.171081,4.934345],[-9.039819,6.992464,-8.449968,-0.764669,7.022805,-7.969307,7.693780,-7.504051,-7.942013,-2.195064,-2.171438,-1.655784,2.574217,6.326965,-2.118291]],[[-5.851258,-9.590986,6.867134,1.180463,6.408571,-2.630749,4.637626,-0.864743,8.503632,1.234293,-8.325821,3.641699,5.697943,-5.378859,-7.101328],[4.341352,6.051071,-6.051738,-5.479830,-7.235318,-3.962102,6.275338,6.024156,3.016550,-3.095080,-4.315123,0.094794,7.881852,-2.067506,3.436373],[-0.807183,9.805905,-8.780089,-9.704782,5.707779,-9.212222,-5.556996,6.148273,-5.000338,-4.971469,3.314817,1.879379,-3.217488,7.248577,-7.253024],[1.048018,7.795930,-2.464207,-0.882403,-2.882403,-2.205156,7.119148,0.544588,-7.449501,-0.992361,-9.613946,8.727173,-1.249690,1.154324,-5.526389],[-8.492004,-7.667298,-2.069471,5.117866,-3.815802,2.627497,-2.965311,0.699851,0.773457,7.018881,-3.178561,-5.539256,9.880192,-6.194366,-2.437117],[-0.973082,-9.629783,5.386078,-6.466535,-3.020075,-9.787184,9.505950,-0.027407,-7.261038,-5.308638,2.840337,-6.709225,-5.500415,-6.970560,-4.559183],[2.025700,7.318933,3.106286,-2.383298,8.071661,-5.974096,-2.518907,9.396806,-8.737919,9.349557,6.164767,-7.652246,-7.153427,-9.500238,0.733144],[5.224631,7.901173,-9.324199,3.411386,-9.272758,9.149409,9.801434,-0.978827,3.494953,-5.240775,5.184537,2.880846,8.202473,-3.029441,5.930217],[-0.304246,-6.750702,1.014056,7.272020,-4.291464,-9.034000,-7.684398,7.826817,-8.380587,-4.595157,8.630768,-3.769543,3.078947,-1.720565,0.190594],[0.037135,4.336648,-8.991443,-3.844594,2.517942,9.863532,4.210651,2.119689,8.889408,8.107441,0.927154,7.781072,9.508662,2.589574,2.288311],[0.890623,8.477225,-0.608213,-2.690630,2.188618,7.484962,1.006161,-7.478667,-0.357898,-1.015117,7.001251,-1.209130,0.046626,0.223514,-9.969073],[-4.784552,7.830532,-2.764174,7.259104,6.832112,-4.228605,8.483908,6.199236,4.213228,3.026473,7.670779,6.310675,-1.269792,1.957835,6.817969],[-9.531692,-2.117922,8.790540,8.584421,1.620519,0.559531,-9.991701,1.271579,6.472477,6.451963,-7.379655,4.332917,-4.814392,-6.588569,-2.821060],[0.713124,1.595089,-6.009927,-7.805040,2.663132,-5.456230,-2.777956,-0.015889,-1.465411,-1.414916,-6.222128,-2.431710,-1.459673,7.315203,5.269384],[-7.382420,-1.184465,-4.912478,1.597460,2.743990,-4.257733,3.458020,-5.209228,-6.416827,6.270695,-7.261261,3.364852,-5.465495,0.653834,-3.188716],[3.453117,-7.883152,1.418139,-9.124408,4.603528,3.597285,-0.917927,-9.459838,-1.110527,1.171306,4.500251,-5.260741,6.670810,-4.158360,-2.675320]],[[2.664210,-0.230632,-7.445349,-3.158133,-4.414905,-0.359841,2.556163,-4.944379,0.746630,-0.469291,0.442698,-8.162218,-9.898657,-8.134891,-5.877127],[3.923818,-5.028230,4.079824,0.601773,0.470926,-9.624290,-9.656895,-6.555238,0.113192,9.900362,2.094878,-8.005625,-0.897327,4.313635,2.176349],[-5.802144,5.956669,-5.619284,8.184722,-9.947305,5.071659,-3.578051,-0.145382,7.322872,-4.003980,7.545655,7.329747,2.465619,-9.506640,-2.174651],[-8.947508,-3.267892,3.093092,8.086049,9.229139,0.371000,-4.843921,-7.051801,9.227833,-3.915642,-9.477198,6.279668,2.488564,-7.409511,4.276940],[-8.650290,2.048551,0.571623,6.631333,7.337408,-6.444133,-5.529998,-3.867583,7.831320,-7.221412,8.561148,2.497491,-3.554783,7.610865,-6.706707],[6.536808,-8.435063,6.305522,2.694157,-8.103854,2.666661,6.061608,3.234383,-4.816619,4.008723,4.107152,-9.164487,1.076902,2.430599,5.853501],[2.628095,-4.915664,6.944887,0.983685,5.925439,2.116764,-9.702029,-4.761058,-1.465370,-8.013731,9.434859,-6.314840,-8.089893,-3.037237,-6.904608],[2.674386,-5.790256,8.054673,-4.941388,-0.592877,3.161020,-8.055353,-8.906213,6.580056,-9.445402,8.035272,7.489896,2.434250,7.927060,-4.760392],[4.506031,-9.219482,0.009433,0.046399,-0.771633,5.259207,2.491545,-8.161229,-2.445481,-7.281016,6.818568,-0.757627,1.783871,0.342492,0.955143],[-2.285377,5.218080,-6.115392,-4.169582,-6.787308,1.197371,-7.929158,-0.898558,6.716467,3.613469,7.739394,5.595010,3.954618,5.982893,0.530070],[-1.800332,3.414258,-9.739033,9.874064,3.129338,-6.386391,5.045921,1.033097,1.892347,7.360651,-0.259472,6.126237,-1.561335,-1.816664,9.757946],[2.419264,1.143006,-2.566948,-7.092757,-8.269355,7.558897,6.330480,-7.213513,-5.738634,0.412178,-8.056364,-2.948100,5.117999,-9.479978,-2.086524],[9.439153,-6.002311,-0.407129,0.691513,-8.214311,-6.199068,-5.516985,-2.974206,-1.896360,-6.991992,-6.812682,3.917052,-1.422240,-0.990887,-5.584451],[6.871681,-8.612865,-0.521456,-7.712577,6.918160,-2.644927,-2.998416,7.941191,4.336026,-0.292471,3.837425,-5.249479,7.406329,6.056863,4.780476],[6.820293,-9.608582,-2.527850,-7.773234,-4.749211,7.463677,-8.818732,8.625532,2.828501,5.410262,-4.182319,-4.244091,-8.275305,6.153022,4.651319],[8.580530,4.377970,-4.350929,3.640886,-7.974477,7.847473,-8.336322,-6.712704,7.928245,-5.795174,0.182947,-3.183152,2.016519,1.144772,-5.766433]],[[4.811605,5.502917,9.964274,1.751189,5.490062,-2.371049,1.068664,-3.268880,-0.402981,4.800209,-4.037987,6.482332,0.137209,8.732273,-5.941785],[2.554957,-5.760020,-2.772761,8.244222,-6.043146,-0.253129,0.350234,1.241998,8.772258,1.569315,-5.143048,3.006261,-6.965024,-7.944532,1.903043],[-3.278969,-8.018770,-4.988136,-9.482040,-2.287829,-8.268007,-0.788658,2.563592,9.487262,7.330661,4.184429,-0.494860,-4.702761,3.385279,5.328745],[1.188272,-2.774018,-6.997673,-0.953271,-9.465249,8.293416,2.924278,-0.815157,7.064631,4.934971,-3.747138,-0.803080,2.916156,-6.900984,6.558716],[-9.716601,4.791830,-5.569287,9.674591,-4.671740,-6.812212,-9.835640,9.252258,-8.318992,-7.786309,-2.689778,-5.987007,0.246935,0.934958,3.772726],[4.315741,9.973889,-5.675661,-7.622422,-8.086708,1.606090,-2.045533,1.518660,-6.363349,-1.612883,3.228229,5.837418,3.519196,-0.007490,-9.777553],[8.016855,5.129813,-7.846117,7.057423,2.448458,-2.656554,-9.079199,-8.055740,-0.875634,7.684419,7.472575,8.505875,-6.571027,0.314384,6.878052],[-8.673221,-4.239517,3.512678,7.903168,5.400983,5.214197,6.540764,0.568981,8.074064,-2.910115,-8.839809,2.100603,4.249958,6.012276,-7.468135],[-8.279472,1.607566,-7.930797,-6.706302,1.636583,-8.208138,5.980267,-9.735446,9.578849,-0.815362,-7.161579,6.808847,9.201420,-2.515734,-5.698955],[6.064057,2.348368,1.655660,-0.816134,-8.957098,4.305942,-8.219722,-6.182365,8.298508,-1.834418,-4.801932,7.264948,-0.838089,-8.361850,1.803596],[-8.981322,3.254105,7.176879,2.746318,-7.539516,-4.073960,9.932488,-2.983738,6.139722,5.146131,-0.638541,2.667048,-5.897767,-8.505637,-9.509345],[5.109054,-3.639941,-0.348900,5.272666,6.276714,4.559894,6.541770,-9.847267,6.748367,-3.769436,0.899298,-8.584781,-0.520938,0.391386,5.902058],[-4.790619,-5.085898,1.278004,-4.894000,-6.631094,7.456564,3.281413,-2.440149,-5.716486,-5.957997,5.012240,1.855926,-9.825642,-5.076244,-3.387619],[2.484698,-7.819105,-1.561696,-1.094670,-3.923826,-0.958860,0.918691,-7.181493,-1.452178,6.666364,3.622817,-3.455489,-1.062064,-0.488090,-6.645916],[-5.408319,6.951296,1.069289,-5.660940,5.719782,9.025575,-1.323584,6.858276,-5.582445,-5.167063,-3.044436,-1.740357,-8.255127,9.030973,2.476952],[-5.381059,1.727796,-5.338105,7.298351,9.055019,2.404472,-2.837941,5.098495,8.635358,2.030760,0.992857,8.813765,5.766096,-4.744651,5.925598]],[[-6.691034,5.068936,4.234022,7.735350,-8.833219,7.822167,9.591194,-3.459190,-7.383446,-5.718724,9.415358,6.921590,-5.766310,-9.611621,-8.030271],[-8.430425,1.813504,-6.319481,-3.392044,3.055197,-3.803387,-1.459285,7.423842,-1.494378,-2.072015,2.674666,-0.817275,3.369066,2.060638,5.584224],[7.619825,2.333078,9.904455,9.689217,8.293341,2.454963,-9.326700,3.421652,-6.715316,2.707477,-4.722357,-5.150445,8.524601,3.960136,9.984884],[-1.649052,5.289774,-7.438679,-4.585250,-5.820310,-7.408731,5.429063,0.127802,-3.893034,0.021982,5.530185,2.956368,-3.477829,5.598092,9.446323],[6.668313,7.561199,9.649288,3.367848,0.918322,1.069314,7.863802,-7.508121,2.164259,-2.909052,-7.378506,1.741646,8.615557,8.670788,5.767427],[-5.695339,-2.855679,2.993083,7.569127,7.556404,-7.817888,-9.547208,-4.834576,8.459247,-4.946830,-2.785704,3.672164,-8.253456,3.237466,4.603814],[-1.463515,2.393136,6.857303,1.005900,-1.628412,7.764694,8.235362,-1.321780,4.978867,-5.041451,-1.868852,-1.770084,-0.189247,-9.575787,-4.176002],[-9.512761,8.373863,-6.804673,1.508892,6.813921,-4.577194,-2.993594,7.407396,8.384092,-2.067662,-6.324198,-9.669807,-1.951099,8.790462,2.293777],[-0.524330,-6.764658,6.726934,-0.721727,-1.296696,-3.833580,3.472198,6.919162,-4.364946,9.066080,-0.032964,3.371837,-3.025878,7.553822,-6.341912],[-3.663974,-1.949849,4.595360,5.426862,-0.165168,8.517090,-7.927932,-3.782781,2.536220,3.661563,0.806410,-7.773360,-3.755532,8.600219,-5.415745],[-6.935301,-2.534378,-7.917641,1.048202,-0.620393,0.596065,-3.170948,-4.308581,8.468500,1.010902,-6.490724,-5.397731,3.573071,4.359355,-1.735048],[2.711954,-6.886320,-6.821794,7.653193,-6.520134,5.118304,3.768884,-8.091262,-5.448393,-6.103509,-8.135676,8.055608,1.358699,0.214697,4.546156],[4.660888,3.679742,-7.770146,-2.756187,9.929293,2.104860,-0.950940,-1.109450,-6.994139,6.757079,5.394794,7.091054,-6.559888,7.810115,-2.396905],[-4.188117,4.196674,5.407355,7.233865,6.291143,7.269823,7.195961,-0.002698,-9.713819,9.243338,6.123593,5.372090,7.819665,6.909686,4.815996],[5.058817,1.565934,6.482495,-1.017490,-3.711821,0.452063,5.304838,-2.031529,9.859897,-5.154459,-7.242664,7.263284,5.152187,8.003845,5.021969],[-2.972525,-2.154192,-9.970258,-3.295736,-1.338354,-4.478238,-0.006625,4.060151,7.931239,1.348767,5.649131,3.194375,3.079514,0.623749,-9.838732]],[[-9.597827,0.332192,-3.263576,-1.563262,-5.359760,-1.193830,0.210989,-1.720505,9.980557,5.108069,-1.509432,-5.834538,4.463218,-9.550842,-3.012002],[7.979586,7.844076,-6.040844,-7.661985,-6.748186,4.473702,-2.856329,-7.500292,2.955104,-1.514088,-0.813816,2.937886,5.434721,3.756072,7.981187],[-2.523910,-1.747821,0.212572,5.916682,6.897486,7.893005,-3.169137,2.557636,-5.401477,-8.488680,7.343577,9.492530,5.446148,9.419580,-5.049573],[2.485884,-2.668948,-7.914381,-2.902010,5.779180,-0.426115,-8.408747,-7.882517,3.113855,5.922532,-2.380400,-2.958047,6.649618,-0.965457,-1.868311],[-3.433326,9.610532,4.312638,-6.566720,2.985784,-4.116703,-8.804531,5.269718,-3.442886,-2.814583,-9.102911,4.165260,-7.455161,9.586172,7.428094],[-2.710054,8.590754,-9.552534,6.639544,-2.352313,3.039700,-2.771038,7.735113,-9.281933,-0.960348,3.088649,5.327373,-3.339678,-1.498375,-0.155865],[4.357644,1.281268,-6.991537,-0.553936,-0.937121,0.340015,6.720229,-2.349556,8.539920,-3.920397,6.777407,-8.304893,-9.148908,-5.341220,-5.676683],[1.096105,6.444220,-9.542363,-2.604326,-8.986866,3.277612,-7.699707,0.052537,-8.023038,-7.581244,8.968834,-8.769461,-3.663982,-5.553147,1.270961],[-3.934259,-4.023014,3.773956,3.227055,3.594296,6.480884,4.649564,8.242844,-1.577315,2.243630,4.267861,-4.472062,3.821055,-0.689249,4.348279],[-4.850407,-1.131495,-3.533280,-5.906563,-6.136545,5.321554,-1.695150,4.481279,8.317562,1.867400,-5.257109,7.044078,5.462766,-1.891318,-5.645629],[9.676398,8.037878,-6.365469,-5.899743,5.013722,-0.513223,-5.775261,-4.150181,9.601322,8.777555,-7.858027,8.164239,-9.259016,-6.561846,-6.630303],[-1.221340,-1.256243,-7.953867,3.655989,7.206362,3.014966,9.146982,-5.584097,1.172660,-7.532966,2.202069,4.732194,-0.455410,2.200972,-8.889644],[-5.228292,3.023282,-8.526639,3.205375,-7.870685,-5.201880,-2.977025,8.680995,5.188459,-8.160431,4.312915,4.067847,-0.239059,-2.643471,-8.575016],[-5.671027,-9.985583,9.706925,2.185302,-9.821235,3.744357,4.478508,9.358977,1.363653,0.491865,-2.298355,8.967214,7.511109,3.979047,1.105602],[-1.499817,-2.448879,0.735406,2.214205,-8.262709,2.222062,1.792814,-7.270342,6.612996,6.131438,0.253529,-7.280886,3.681984,1.549807,6.276208],[4.301265,-7.889578,-8.908536,9.941471,-0.053838,-1.838993,-5.347336,-7.535721,-1.559601,-9.945262,-3.743563,5.915191,-0.959804,3.571243,8.612469]],[[-5.218789,-0.999957,4.631844,-1.134908,4.230763,-5.981783,-3.556806,1.147099,6.188167,0.580480,8.194649,-0.363460,-1.952652,-4.201196,-2.457737],[-9.464396,-3.835225,0.350678,-3.883597,-9.492156,-9.748325,2.766568,4.293446,1.579531,-6.214314,-0.705363,-1.331770,-1.198463,0.952906,-5.395891],[-6.965390,-7.444273,-3.918851,-7.073095,-3.043793,-6.813952,-3.966033,9.945542,-0.310121,-8.319551,6.785979,-4.416665,3.084364,-8.042917,9.939873],[-4.285517,-4.311359,-4.398120,-1.388167,3.073249,-9.068121,9.445480,8.506899,-5.174544,3.978124,-1.220283,-5.988979,6.072775,7.752284,-3.676667],[-9.480104,-7.470105,-9.872815,1.714575,-6.377733,4.743564,-1.311643,5.641017,3.868207,2.336626,-6.042656,-6.766220,8.220484,0.321526,1.184258],[4.416553,-3.709338,-5.704622,0.887314,-2.270106,-8.688132,-6.995403,-2.588966,-4.227097,6.725273,3.025609,6.536725,-9.936752,6.234542,0.516590],[-0.081087,-1.400749,5.061724,1.418473,3.372690,-8.099884,4.969487,-9.743966,-6.441755,1.858629,6.528090,8.598731,-7.797344,7.390237,0.610850],[2.815359,5.344623,4.937519,-3.251889,8.811603,-2.355298,-3.567205,-8.019587,2.117966,2.689881,8.994800,9.090190,-0.487011,-5.857651,9.714272],[-1.763098,0.226827,1.254110,-5.385229,3.227649,2.526473,9.284077,4.557693,-6.096141,-9.325199,-2.816254,-9.767879,7.392740,2.368324,-4.633810],[0.971386,8.547699,4.556673,0.376542,6.355438,1.381087,-7.279409,-4.539058,1.352886,6.949382,-3.238194,8.158543,0.538459,9.615567,-0.840752],[-9.339422,1.818056,1.142268,-1.369162,-9.909049,8.022297,-1.397170,6.657901,-0.532579,8.034589,-8.448325,8.606459,9.153734,-9.003146,4.230760],[-9.994196,5.932520,-5.901469,-4.905465,7.022914,-1.546453,5.644880,6.052325,6.126703,5.870818,2.950306,-5.067670,7.959204,9.785447,9.254020],[-7.080467,-7.045224,9.775379,-9.371251,8.408934,-8.497295,6.779090,-0.656661,-1.852738,-9.283009,3.129726,-0.830122,-2.807615,0.420201,0.573012],[-0.052978,-4.309852,6.226336,0.047502,-2.971266,-6.814243,-0.331676,-1.902244,-1.139361,-6.847481,-3.765259,-4.650303,-5.492048,-2.854580,-1.672349],[-6.120868,0.248366,-0.060472,-4.301266,1.636499,-6.700071,5.059501,4.508471,-8.912985,8.719096,-3.845583,-7.246494,-6.959152,9.011380,-7.684144],[-1.900520,-5.837414,5.168300,7.534784,6.310842,-0.402712,-0.283241,-4.342194,0.026400,7.992352,-8.851976,-7.486541,-8.047477,5.154634,5.987938]],[[4.320718,-2.040092,-4.321936,-4.201887,3.948016,-0.170974,-8.085096,3.313573,-6.644951,9.568212,4.634983,8.646794,-0.734945,-3.939558,0.442624],[4.957903,-0.752183,-9.304342,6.495444,-7.017457,-6.908014,6.399731,4.306194,-6.298129,8.428932,7.168002,9.983853,9.099970,-8.749765,5.451879],[2.752039,-5.452461,-9.077364,-4.348521,-0.365006,-2.984991,2.967471,6.130997,-5.381085,-6.530590,7.840932,9.194648,-5.749851,-2.379429,-7.245405],[-0.787041,-3.373491,4.061236,-0.471092,-7.092905,-1.484763,8.830541,-0.767427,-5.302090,-5.414426,8.069117,-0.248357,-8.263297,2.532656,5.288701],[-9.372373,1.300567,9.237670,5.155850,6.062298,-8.045064,-0.287156,1.934853,-1.384569,-7.561968,4.390669,-9.370982,-3.258843,-4.188222,8.284994],[6.282371,-6.790618,-0.666979,-0.891762,1.341555,8.340342,5.032699,0.299219,7.305067,9.789423,9.434807,4.978708,-3.906992,-9.951334,8.801145],[7.547754,-2.496762,1.841593,4.404140,-5.129738,7.504271,-3.787203,-9.240271,-4.474531,4.470829,9.551084,-8.571569,-8.045926,-6.096113,9.102225],[-4.583032,-4.662770,-3.614506,2.916159,2.943447,-6.082639,5.744648,-6.430458,6.526000,0.988828,-8.478909,4.652556,3.871748,5.449697,-8.051513],[1.828021,7.359503,1.218927,-2.694134,3.750192,2.462908,-0.986973,-2.476272,-0.546278,3.256132,-4.194821,-6.586624,-3.746351,5.787993,8.214906],[1.997309,-8.368495,-2.645354,-2.812145,-8.568361,1.301868,-1.197751,0.245062,-3.205856,-5.029230,5.455697,9.747848,-6.597537,-8.518116,9.614563],[9.925803,-9.377465,-6.319470,-7.084837,3.745251,-6.110025,-7.366459,6.892513,-7.163826,8.700888,4.114350,6.211015,-4.710093,1.225538,-4.289957],[-0.328708,3.041713,3.778839,3.710398,-2.110336,3.251051,1.644276,6.781313,0.731273,-4.605619,-4.088013,9.390191,-5.566824,0.065396,-0.503032],[0.583164,-5.740409,-0.531066,-3.744791,6.528694,-8.791456,4.565528,-2.249344,-0.504249,-1.236718,-5.419410,8.728782,3.254160,5.837144,3.746635],[-4.442123,-8.980065,9.221261,-6.934098,-0.968937,-4.848623,-1.909456,7.751854,5.785258,-8.520515,-2.545821,-7.518698,1.189279,-6.910236,2.364918],[-4.034841,-4.235257,-0.896583,0.187119,3.966129,-9.784566,8.849359,2.045979,7.726419,-2.035936,3.496813,-5.569246,-0.082323,2.752252,-1.322614],[-2.992544,-2.854061,7.307794,-8.173663,5.234338,-0.478523,-3.642246,2.108501,-9.740030,-0.274490,-9.773167,-3.519912,7.188881,-4.930921,7.116659]]], dtype = "float32")#candidate|8752|(14, 16, 15)|const|float32
bop_8753 = relay.bitwise_or(call_8735.astype('uint16'), const_8752.astype('uint16')) # shape=(14, 16, 15)
bop_8756 = relay.bitwise_or(call_8736.astype('uint16'), const_8752.astype('uint16')) # shape=(14, 16, 15)
output = bop_8753
output2 = bop_8756
func_8772 = relay.Function([], output)
mod['func_8772'] = func_8772
mod = relay.transform.InferType()(mod)
mutated_mod['func_8772'] = func_8772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8772_call = mutated_mod.get_global_var('func_8772')
call_8773 = func_8772_call()
output = call_8773
func_8774 = relay.Function([], output)
mutated_mod['func_8774'] = func_8774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6079_call = mod.get_global_var('func_6079')
func_6081_call = mutated_mod.get_global_var('func_6081')
call_8797 = relay.TupleGetItem(func_6079_call(), 3)
call_8798 = relay.TupleGetItem(func_6081_call(), 3)
var_8799 = relay.var("var_8799", dtype = "float32", shape = (14, 4, 15))#candidate|8799|(14, 4, 15)|var|float32
bop_8800 = relay.maximum(call_8797.astype('uint16'), var_8799.astype('uint16')) # shape=(14, 4, 15)
bop_8803 = relay.maximum(call_8798.astype('uint16'), var_8799.astype('uint16')) # shape=(14, 4, 15)
func_5177_call = mod.get_global_var('func_5177')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_8806 = func_5177_call()
call_8807 = func_5177_call()
output = relay.Tuple([bop_8800,call_8806,])
output2 = relay.Tuple([bop_8803,call_8807,])
func_8833 = relay.Function([var_8799,], output)
mod['func_8833'] = func_8833
mod = relay.transform.InferType()(mod)
var_8834 = relay.var("var_8834", dtype = "float32", shape = (14, 4, 15))#candidate|8834|(14, 4, 15)|var|float32
output = func_8833(var_8834)
func_8835 = relay.Function([var_8834], output)
mutated_mod['func_8835'] = func_8835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_188_call = mod.get_global_var('func_188')
func_189_call = mutated_mod.get_global_var('func_189')
call_8889 = relay.TupleGetItem(func_188_call(), 0)
call_8890 = relay.TupleGetItem(func_189_call(), 0)
func_3705_call = mod.get_global_var('func_3705')
func_3707_call = mutated_mod.get_global_var('func_3707')
call_8895 = relay.TupleGetItem(func_3705_call(), 0)
call_8896 = relay.TupleGetItem(func_3707_call(), 0)
output = relay.Tuple([call_8889,call_8895,])
output2 = relay.Tuple([call_8890,call_8896,])
func_8897 = relay.Function([], output)
mod['func_8897'] = func_8897
mod = relay.transform.InferType()(mod)
mutated_mod['func_8897'] = func_8897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8897_call = mutated_mod.get_global_var('func_8897')
call_8898 = func_8897_call()
output = call_8898
func_8899 = relay.Function([], output)
mutated_mod['func_8899'] = func_8899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7255_call = mod.get_global_var('func_7255')
func_7256_call = mutated_mod.get_global_var('func_7256')
call_8913 = relay.TupleGetItem(func_7255_call(), 0)
call_8914 = relay.TupleGetItem(func_7256_call(), 0)
func_2249_call = mod.get_global_var('func_2249')
func_2253_call = mutated_mod.get_global_var('func_2253')
call_8931 = relay.TupleGetItem(func_2249_call(relay.reshape(call_8913.astype('bool'), [7, 16, 5]), relay.reshape(call_8913.astype('bool'), [7, 16, 5]), ), 1)
call_8932 = relay.TupleGetItem(func_2253_call(relay.reshape(call_8913.astype('bool'), [7, 16, 5]), relay.reshape(call_8913.astype('bool'), [7, 16, 5]), ), 1)
func_1550_call = mod.get_global_var('func_1550')
func_1551_call = mutated_mod.get_global_var('func_1551')
call_8934 = relay.TupleGetItem(func_1550_call(), 1)
call_8935 = relay.TupleGetItem(func_1551_call(), 1)
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_8936 = func_4180_call()
call_8937 = func_4180_call()
output = relay.Tuple([call_8913,call_8931,call_8934,call_8936,])
output2 = relay.Tuple([call_8914,call_8932,call_8935,call_8937,])
func_8951 = relay.Function([], output)
mod['func_8951'] = func_8951
mod = relay.transform.InferType()(mod)
output = func_8951()
func_8952 = relay.Function([], output)
mutated_mod['func_8952'] = func_8952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3828_call = mod.get_global_var('func_3828')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_8973 = func_3828_call()
call_8974 = func_3828_call()
func_7087_call = mod.get_global_var('func_7087')
func_7091_call = mutated_mod.get_global_var('func_7091')
var_8983 = relay.var("var_8983", dtype = "float64", shape = (198,))#candidate|8983|(198,)|var|float64
call_8982 = relay.TupleGetItem(func_7087_call(relay.reshape(var_8983.astype('float64'), [3, 66]), relay.reshape(var_8983.astype('float64'), [3, 66]), ), 3)
call_8984 = relay.TupleGetItem(func_7091_call(relay.reshape(var_8983.astype('float64'), [3, 66]), relay.reshape(var_8983.astype('float64'), [3, 66]), ), 3)
func_2853_call = mod.get_global_var('func_2853')
func_2855_call = mutated_mod.get_global_var('func_2855')
var_9010 = relay.var("var_9010", dtype = "float32", shape = (10, 42))#candidate|9010|(10, 42)|var|float32
call_9009 = relay.TupleGetItem(func_2853_call(relay.reshape(var_9010.astype('float32'), [420,])), 2)
call_9011 = relay.TupleGetItem(func_2855_call(relay.reshape(var_9010.astype('float32'), [420,])), 2)
output = relay.Tuple([call_8973,call_8982,var_8983,call_9009,var_9010,])
output2 = relay.Tuple([call_8974,call_8984,var_8983,call_9011,var_9010,])
func_9026 = relay.Function([var_8983,var_9010,], output)
mod['func_9026'] = func_9026
mod = relay.transform.InferType()(mod)
var_9027 = relay.var("var_9027", dtype = "float64", shape = (198,))#candidate|9027|(198,)|var|float64
var_9028 = relay.var("var_9028", dtype = "float32", shape = (10, 42))#candidate|9028|(10, 42)|var|float32
output = func_9026(var_9027,var_9028,)
func_9029 = relay.Function([var_9027,var_9028,], output)
mutated_mod['func_9029'] = func_9029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7875_call = mod.get_global_var('func_7875')
func_7876_call = mutated_mod.get_global_var('func_7876')
call_9052 = relay.TupleGetItem(func_7875_call(), 0)
call_9053 = relay.TupleGetItem(func_7876_call(), 0)
uop_9054 = relay.atanh(call_9052.astype('float32')) # shape=(40, 22)
uop_9056 = relay.atanh(call_9053.astype('float32')) # shape=(40, 22)
func_2318_call = mod.get_global_var('func_2318')
func_2320_call = mutated_mod.get_global_var('func_2320')
const_9058 = relay.const([-5.573265,0.958613,-6.549822,1.790537,-3.839699,2.078962,-4.327554,2.402616,-7.297507,-2.607504,-6.354019,-2.964339,7.114423,4.591773,8.056117,9.293121,0.040696,-5.474507,1.150008,6.374890,1.070954,5.729429,5.558572,8.304833,-0.472113,7.386933,0.141933,-1.595984,7.834002,-1.563361,7.768256,-5.446622,-4.698167,-6.006382,6.037914,6.368514,-3.405496,-1.550249,-6.668300,2.441179,6.037348,6.709174,-5.623019,-7.621655,2.152061,7.063299,-5.742323,9.476987,-3.001758,5.850201,-1.714597,-9.021138,3.210361,-9.527173,2.681746,-1.145186,-7.086946,9.280606,7.540845,-1.542468,-2.063869,4.117013,-4.974431,-2.654122,-0.333634,-8.199133,-2.418494,-9.024132,7.928995,2.489547,-4.870483,5.111779,4.868972,-0.893911,-4.609610,-1.447001,-2.995648,-0.487115,-0.556154,8.207775,-6.939794,7.210461,1.473394,-0.690053,-8.003325,3.439024,0.674511,1.341503,6.568179,3.980386,2.532552,2.852135,3.818155,-8.160277,-0.517911,-2.853035,2.267669,2.708121,3.880707,7.149478,-9.700936,0.283664,3.848487,-7.564772,-6.400702,0.693497,3.328762,3.881410,-1.085672,9.597095,9.503723,3.912465,6.289503,0.249633,-1.529262,4.770663,8.114345,-2.372276,3.240620,-9.263502,-4.866418,4.709372,-5.568844,-7.109810,-0.040346,6.060899,8.628703,-6.023555,0.347873,-6.354004,-6.975836,-4.661906,-6.802094,9.757379,-8.113540,5.130558,5.459870,-6.912556,1.518553,-6.518696,-7.728135,5.562208,-4.737858,3.397298,-1.542243,3.467560,9.678285,-6.907289,-7.817077,0.798424,2.975147,7.551568,-5.099723,-6.188915,-7.072952,4.036204,-1.681926,-2.575726,4.427656,2.177218,3.944350,-7.688132,-4.947625,-8.549499,-6.312732,6.634920,-5.251411,-3.846545,0.120035,-1.231695,9.923307,-0.814842,7.779784,-0.138787,-6.298875,-7.666086,-0.555979,-8.025376,3.202974,8.969601,1.686310,-4.093834,1.841982,-0.836286,7.586162,-4.879612,-7.669025,0.326195,-9.773575,-7.403809,7.765396,-7.044574,-7.794823,-8.577425,-0.764127,9.684462,7.945252,2.122141,5.197792,8.045807,4.425100,6.398153,-1.260646,2.589088,3.156362,-5.048145,-3.374792,-6.607938,9.205493,-8.825905,9.754031,0.888953,6.123170,9.271380,-9.194276,-6.294090,3.176086,-1.705034,-4.163979,-0.978262,1.801097,-3.128425,8.325110,-1.465813,0.345955,-1.279331,7.759750,8.778870,1.037760,5.995914,6.124493,0.621068,6.764555,0.373659,1.003302,9.945781,-3.554978,-8.663905,8.886938,-7.340352,3.347855,4.775926,7.082771,-5.188878,9.971739,-5.246986,1.051918,5.152906,3.426562,-4.303242,-2.092144,-8.997239,1.707335,8.578840,1.852840,5.847944,-9.733069,0.368971,-4.698714,-5.816124,8.002715,-7.986389,-3.911213,-8.562511,-8.392245,-7.284248,-5.326424,1.287868,5.772747,-4.016878,6.890447,-9.784309,-3.842668,7.539286,6.038394,8.808824,-8.073380,5.630199,7.087438,5.453602,-2.199560,8.336234,-7.479618,-7.101439,8.942616,-2.147643,-6.372274,-8.811729,7.713212,9.803018,-1.345752,9.050809,0.276069,4.507129,-0.532699,-1.920827,6.239131,-0.423509,0.160144,1.883875,1.455134,9.741590,-1.415000,6.232901,3.201904,-5.533364,4.842327,-8.462731,-6.872469,8.094766,-7.085620,5.773242,9.507387,4.489944,-4.340360,7.767386,1.200299,-0.258596,5.612310,9.771734,-5.352150,-6.847893,4.169520,-2.314624,-0.399885,0.994024,-6.705379,-9.091364,-6.877925,-0.184246,0.494853,-5.696311,-0.919213,-4.498102,-7.263955,-9.221630,-4.545208,-0.513974,0.269923,1.537137,5.485811,4.650678,-5.370209,1.722542,0.311166,6.127570,-2.937567,5.635974,-9.966802,-0.861154,3.840010,-4.216199,8.128029,-5.339329,0.415047,-8.082091,-8.523722,-1.438412,-1.287345,3.843870,7.243253,-1.415643,-2.485147,-9.624453,1.396304,-6.811659,1.080726,-8.483667,3.487557,-5.515804,0.081802,1.765972,-5.464032,-8.889085,-0.585434,-6.409944,-1.441541,7.291054,5.798204,-8.369004,-1.719870,8.786965,3.412062,-8.471601,-4.103932,7.914178,9.969000,5.188782,0.449736,-8.525551,2.384126,7.179356,4.799177,2.771501,9.118261,-2.004976,-2.807799,4.517206,1.434120,-2.237562,-5.861600,1.647998,5.492302,3.391976,-2.363768,-3.083767,0.492675,-1.984520,-6.584169,6.315586,4.332392,5.285446,3.368223,4.539202,-9.318699,2.476675,8.212898,-8.291562,9.352126,2.592470,-0.271193,-6.408225,-4.575251,-0.771260,-9.854718,-6.831312,9.216435,5.633389,-8.445306,-8.419670,-1.449096,-4.595171,-3.188103,-9.989453,-2.749672,-1.717189,1.943428,-9.263710,4.266754,-5.059644,-8.118448,5.969914,-5.039671,6.827724,7.983100,9.596289,6.772871,6.839267,5.395781,5.231510,-1.092440,-5.863912,-6.120788,3.621601,7.874101,1.283082,-5.517751,-4.393149,0.610920,7.551804,6.261872,4.817743,-8.895361,-6.853247,-7.891260,-8.541527,1.021201,8.953433,3.344167,9.721060,-7.080806,3.370856,6.416643,-1.438983,6.426881,4.016726,-0.598102,5.368510,-5.392932,-0.028648,9.299063,5.731986,8.971846,3.706086,3.454312,-0.760816,9.169602,-2.423242,1.622237,-5.699885,-6.084212,5.870486,-5.604801,-7.199421,-9.997403,4.125154,7.355027,0.460290,3.072685,8.372133,5.516562,9.819153,4.116789,-7.788801,-8.452258,3.249105,-7.505169,2.906340,2.925803,7.137303,0.652730,-0.371431,5.077990,0.082777,-5.428697,7.636329,-8.852826,-1.219920,-5.774899,-4.992170,4.718141,-2.377463,-2.268501,-3.456245,3.698991,-3.617684,2.584363,2.155624,-9.883178,5.100591,8.413694,-2.379845,4.807945,-4.802001,4.934714,-4.416172,-7.055829,2.236302,2.497721,3.731848,3.606054,0.624266,-4.776961,-7.053330,6.824208,9.328840,-8.936693,9.061305,-9.421050,-7.781646,-8.587909,6.796836,8.220777,-2.504651,-7.052084,5.383884,4.419103,-3.267058,1.593893,-7.642488,1.556319,9.809645,3.337666,4.198235,-4.973395,-7.704961,9.967279,-1.970712,-4.840657,2.280121,-6.388739,-5.286730,3.246305,1.661176,9.587810,6.320535,8.091456,7.123746,7.278853,-5.633498,-4.694634,0.448858,-5.467450,-5.881705,-0.769939,-5.901150,-7.455347,-3.432016,8.959878,-5.256822,5.727883,9.578493,-5.488940,5.259216,-6.214818,-9.272723,-7.561217,-7.829257,6.167374,8.691171,-9.158432,-3.375129,8.643024,-1.990409,-5.018492,7.805009,-7.076717,-9.263882,8.504670,0.709558,2.389398,-5.935765,0.571365,1.628780,4.398786,-4.911449,-0.005915,-6.010296,3.101310,-8.184471,9.947057,1.257287,1.918913,5.124303,5.642479,-0.926372,-8.849240,7.420679,8.784636,-5.377238,5.629362,-7.881005,8.972084,1.978198,1.662549,-7.774565,-6.272119,-8.969353,5.774476,-0.557896,-6.611725,0.967024,-5.103144,-6.947562,9.592432,-7.527569,6.006891,-8.573249,-2.974363,5.003925,-7.983618,-3.354889,6.722540,-6.822573,-8.625000,-6.945291,7.976157,0.521873,-9.582459,8.140445,-6.118432,-6.440748,-6.843483,-2.265936,2.682115,-3.622247,7.217481,-6.512642,2.210221,6.024629,0.883640,3.035679,-8.545384,-3.278820,-3.206242,-4.364336,-1.436584,5.494501,-8.701478,3.693596,9.772534,1.676101,-6.674158,-9.302805,-6.249920,-7.040105,6.032444,-9.318321,-9.419626,-0.367341,-7.943163,-4.298828,1.437824,3.429840,7.048004,1.279843,-7.489255,-7.496929,-9.110947,-7.102938,-7.664812,0.244631,-6.964658,9.643347,-6.173233,-2.332062,1.185362,9.330239,-5.616936,-3.282576,6.970250,-0.066663,-4.115828,5.411137,3.834722,8.859396,-4.102014,9.870224,-6.298982,6.210244,-6.752981,0.951221,-2.846955,1.643004,2.245283,8.953708,8.579967,-0.171912,-7.819040,0.739343,3.206967,2.993899,8.271468,8.141776,-8.868832,-9.636562,-4.469047,-8.708388,3.202172,8.523786,4.520223,5.009461,-2.288973,-6.477351,9.780796,6.311071,-2.167276,-9.189685,4.639657,9.031849,6.993064,0.938991,9.179884,-5.401467,9.793401,3.405324,-7.534283,8.348427,-4.777247,8.768204,9.166745,-0.176277,-2.026332,4.328876,-4.487375,8.423830,1.797856,5.483126,-4.898292,1.733980,1.956045,-5.185099,5.661239,9.471936,2.558026,-0.974066,3.139850,-2.157631,5.041096,2.137871,-9.781753,9.410422,5.024766,-5.306613,0.135330,5.182490,-4.705654,-6.381607,-7.980252,8.698943,0.438946,-6.090171,-3.896557,-5.087270,2.531318,-7.396506,-2.500587,5.576584,-2.623762,6.257082,4.378565,2.310345,-3.946194,5.631212,7.918870,-1.695411,-9.996106,3.882335,0.010478,2.154951,7.461915,-2.545457,7.353297,-6.406956,4.393545,4.492510,-7.527208,-1.896601,1.246897,2.931005,-1.708050,0.439461,1.628698,7.565861,-4.378768,2.633426,-0.897550,1.299136,2.346965,-6.333026,4.666541,5.223898,-4.733689,-5.492438,1.574895,-7.032093,5.779949,2.508600,-1.715471,9.230300,7.957359,-2.514708,-8.891733,9.868546,3.619098,-3.900344,-5.098969,8.581568,4.035493,-4.352180,5.126606,-6.351787,-8.276360,3.397568,-7.338812,8.900612,5.413164,-5.811557,6.807317,7.501758,7.489250,4.247476,0.760287,-8.782693,-6.426927,-3.792333,8.659311,-5.886037,-9.271667,-9.839608,-4.153154,-3.064641,2.774447,1.993378,-8.921889,-0.531708,-8.030264,9.659026,-0.116533,-0.687392,-1.045796,-1.924843,8.912048,7.690877,3.720384,-4.867741,2.532878,0.360953,4.595027,2.041290,-6.861607,2.903616,8.957543,-3.024917,-2.897566,-0.010615,4.292613,-6.924550,2.470211,-6.927898,4.968916,-7.664305,6.090560,-1.459184,-2.703984,8.413556,7.106483,9.259630,3.214972,-1.759956,-7.337725,7.978743,5.284272,-3.831137,0.952069,6.027760,-8.837295,-3.315860,-1.712021,-9.171747,-9.509016,8.918507,5.238327,3.363101,-7.693433,-3.448778,-7.313818,0.945185,-6.304970,7.285491,-1.204577,-4.509659,-2.460363,3.521214,6.712952,-9.234702,6.450428,0.119508,-1.385185,9.558624,-7.945417,-2.258733,3.802329,3.914395,7.878921,-5.123752,3.824722,-6.480612,1.128914,-6.645690,-5.174039,-8.720316,-0.948002,-4.322863,-8.066120,-3.301678,6.164008,-1.229950,-1.291576,-0.836931,-5.370095,3.344996,-7.974471,0.231882,8.301771,-9.608303,-8.873591,7.318569,1.047647,-9.661528,-1.110567,-0.265846,8.630249,-3.264765,-7.304389,8.193176,7.355439,7.075803,5.181765,5.949141,-9.969260,-5.503144,6.207610,-1.939208,1.993421,-3.068400,2.423397,8.179942,6.302736,-4.395813,5.621554,-8.175446,-5.841662,-0.786866,9.003234,3.901475,8.638750,-3.113882,6.346705,6.826204,2.901257,-0.724468,9.728366,3.249477,-0.262032,-5.077580,-8.053473,-8.040008,-4.312243,-4.604257,2.795606,-7.571782,7.096431,7.817904,2.400331,2.425782,-2.057220,4.700169,2.079671,0.755719,-6.657389,5.830683,-1.118815,1.955257,-9.144846,-7.541208,3.413841,1.779723,-0.091076,-5.852568,1.311309,-8.456569,3.058546,0.466577,8.165249,-0.741381,1.095830,-3.087336,-5.144634,-4.076631,7.517328,-0.929624,9.035236,0.307811,-7.083380,9.736338,1.760628,1.459136,6.695496,4.295585,5.143934,-2.436509,-3.635982,3.504486,2.930956,1.870078,-2.264068,2.415177,2.130831,9.309362,-4.371635,-5.340530,5.669415,0.228065,-6.728086,5.696980,-3.081536,-9.538549,-9.291380,1.402789,-3.858153,-4.266249,-8.629324,-0.732590,-5.843265,6.535873,2.459026,-4.756332,-7.833364,0.190225,-5.792129,-9.827221,7.547893,4.080059,-9.082109,3.471224,-5.896741,-4.410267,9.738210,-3.024716,-5.206336,7.720369,5.779205,-0.676194,3.410304,2.242568,-8.584187,-4.859036,-3.373964,0.107132,1.541510,8.593462,-1.246901,-9.042748,1.961587,6.619661,6.538389,6.126914,-6.782560,-2.637719,5.389159,-8.835421,6.478574,2.575088,-7.285892,3.148415,0.925264,7.103610,-6.709167,-7.199564,9.392960,6.969919,-5.727562,8.012559,5.585514,-6.649759,2.171601,-6.974054,7.366749,1.307028,1.441354,7.549557,4.059740,-2.887303,5.623925,3.145884,4.444690,6.961713,1.564067,-8.169204,-9.445454,-7.797414,7.319933,-8.241486,-2.548224,8.587871,-6.875878,2.087134,2.173032,2.477214,-0.075603,6.971338,-7.454232,4.615358,-3.760386,-7.715572,-8.010677,-8.154354,6.505775,-6.606390,-2.240600,0.738620,5.769757,6.108274,1.140543,5.722304,6.039256,2.577194,1.949753,-9.981849,-7.372081,-3.432810,0.946615,7.549661,9.331847,-5.137751,0.076636,1.602172,-2.441378,0.018587,8.882047,8.184386,-5.356381,-2.201045,6.813346,9.126913,6.497648,-8.346676,-8.107436,-0.761967,-6.588269,-7.121782,-8.404113,-6.016676,-9.177601,-3.401452,-6.117050,-5.746189,-9.053555,-8.142431,5.658688,-0.356042,4.779756,6.972998,-3.083994,8.800398,4.058115,-3.249201,8.979195,-3.202799,-3.496134,-5.543373,3.725396,4.074455,9.649405,2.911024,7.695121,-7.889246,4.586222,9.768595,6.196154,-3.704829,-2.923596,-0.725298,9.574360,4.653083,-9.778458,-1.983053,-1.439649,1.650055,2.144249,9.573269,-6.947383,1.573052,8.732461,9.027867,5.893967,5.619234,-1.994851,-6.156204,4.559794,-9.384070,9.393651,6.684285,-1.932279,1.437992,4.328521,6.588606,-4.568802,7.185487,4.444790,-0.461642,-4.657563,-6.138340,-9.076749,-3.891062,-7.402799,5.970751,0.713694,4.870945,0.837970,3.580412,1.136019,7.763052,6.220778,-5.501983,6.047002,-8.264991,-9.300103,6.972873,4.024059,-8.951196,-8.206247,5.490378,-8.905062,0.310835,3.750861,4.144992,5.022785,2.617773,6.449996,0.287286,-6.270896,8.251521,-3.524586,9.523155,-6.407012,5.458259,7.567450,5.644012,-2.676703,-1.720514,5.130053,-9.322326,-2.553918,-1.373146,7.810474,-8.574354,5.985750,8.639101,-4.557940,0.695436,-1.293957,4.417646,4.395165,-0.749663,-6.373592,2.915797,-1.549375,-1.951649,4.684031,-9.049553,0.100069,5.132452,-9.286732,-4.062235,2.361069,-0.324413,4.875993,-5.369382,-0.900308,-2.085825,3.283713,-8.257879,9.163306,-9.387451,7.640454,-2.945679,5.549500,2.954709,-9.140068,1.702502,1.438869,5.050086,4.399708,9.987810,-9.863673,-6.603856,-8.458464,3.395060,-2.921709,-6.077944,9.534359,-5.476522,-3.914082,-5.307776,6.559390,5.586257,5.049033,1.932139,-0.258354,-9.089090,-1.947553,-4.043824,-4.997981,5.741354,7.448101,-5.473172,-1.003264,5.198439,9.078914,2.161172,3.829779,7.624789,9.236992,-1.777952,-6.731117,2.202346,0.964225,7.922741,1.813038,-3.282281,-2.433344,7.828805,2.294411,-3.308360,5.081762,-1.551783,-8.864416,8.101941,-1.979207,5.007013,7.877200,-1.052942,-4.990459,-7.478310,-8.021934,-1.247786,6.383303,7.543340,-0.829622,0.431084,0.599731,3.176174,-4.388275,1.164423,-6.393164,9.879950,1.077929,-6.962950,8.695551,-9.201375,-4.103005,-7.531206,-7.478105,-6.323500,8.427181,-1.849495,8.980367,-6.188054,9.683876,5.097592,-9.066701,9.694075,-4.943587,3.678935,-7.419528,8.918805,-5.543271,-2.830273,9.369076,-4.384101,4.193424,1.736523,-1.663632,-1.770343,8.805132,1.852929,-8.160934,-0.807694,-2.123215,-1.450079,8.002010,9.281585,7.663311,-4.741925,7.742826,-6.436224,-8.881593,1.909417,0.473679,-0.637901,9.532243,4.122541,-4.636670,-2.157291,3.949271,1.376587,-7.355618,1.841713,-0.981572,-5.289711,-5.446015,-8.833356,-7.339138,6.990050,5.669406,8.667037,9.784453,-3.602398,-4.495658,-0.061072,9.467856,-2.198841,6.015537,-0.954163,3.513324,6.022088,4.326107,-7.079077,5.383637,3.636215,6.960440,-3.267034,1.000120,-6.004307,9.959464,-7.085529,-6.027763,1.345392,-2.875871,-6.410527,-5.432445,5.326624,1.638785,-4.114943,4.860087,-1.869586,-2.256771,3.049991,3.683750,4.824903,-7.501067,-6.946273,-5.872773,-0.949994,1.755638,-9.352296,-9.824721,7.159704,-1.153656,7.767069,2.045462,-0.152805,-4.494917,-4.799452,-7.772179,-1.869148,9.961681,3.666961,-6.490092,-1.378307,-0.593563,-2.115838,-1.253044,6.403502,5.305962,-5.751474,-7.441644,-4.490951,-8.293014,-2.949788,-7.605698,0.005894,8.622745,6.394541,7.607531,4.816051,-6.939131,-1.419551,5.566693,0.844542,-6.208590,-8.348776,9.152128,3.277382,5.086598,-3.597368,9.550664,4.395008,-4.964801,-6.886104,-5.958644,-1.436671,4.074577,1.353893,-4.046368,2.403509,-4.238876,3.972984,-0.369988,4.133787,-0.355774,7.227965,0.972871,5.938119,0.556803,0.496060,2.150526,4.953922,9.615143,-4.709286,9.793478,-6.502712,3.468247,6.475801,1.465122,5.529228,-6.322614,7.164789,9.443834,-8.871535,-5.787456,-0.290286,3.584289,4.737138,-0.023659,-4.935316,9.358295,1.131045,-8.792773,8.761794,5.993508,2.980235,8.107773,7.154925,6.188539,-2.789161,-2.327501,-8.571148,-0.519533,-6.929462,6.536944,-3.494746,9.216915,2.800719,0.105147,8.728071,6.646002,-3.801381,5.730122,4.942991,3.181472,3.373522,-8.136622,7.061485,1.721409,8.884062,-4.168732,8.512016,4.817132,3.219061,2.141275,7.173952,-5.567760,-1.241582,0.309721,-2.854237,1.896742,-9.881192,6.092421,-6.921510,5.444075,6.266311,0.673782,-6.826390,8.416911,4.040098,-8.570148,0.062392,7.922655,7.073695,2.154307,2.140279,8.939476,-6.211981,-2.089498,1.754943,-6.191296,6.924047,4.428583,-0.720722,-1.929663,-9.699201,-3.689364,5.054502,6.381367,6.386587,-9.113941,2.625388,-7.456922,3.682840,-9.739804,9.031321,4.701313,-8.914302,-8.483873,-4.987042,7.170582,3.041537,-9.935872,3.170165,9.776822,3.595358,5.941777,8.631132,-8.920845,-9.585121,6.437699,-0.403399,2.083020,-0.757479,2.041089,-8.876461,4.962941,6.192553,-4.672070,9.850182,3.259729,8.543522], dtype = "float32")#candidate|9058|(1680,)|const|float32
call_9057 = relay.TupleGetItem(func_2318_call(relay.reshape(const_9058.astype('float32'), [1680,])), 1)
call_9059 = relay.TupleGetItem(func_2320_call(relay.reshape(const_9058.astype('float32'), [1680,])), 1)
bop_9060 = relay.subtract(uop_9054.astype('uint16'), relay.reshape(call_9052.astype('uint16'), relay.shape_of(uop_9054))) # shape=(40, 22)
bop_9063 = relay.subtract(uop_9056.astype('uint16'), relay.reshape(call_9053.astype('uint16'), relay.shape_of(uop_9056))) # shape=(40, 22)
output = relay.Tuple([call_9057,const_9058,bop_9060,])
output2 = relay.Tuple([call_9059,const_9058,bop_9063,])
func_9069 = relay.Function([], output)
mod['func_9069'] = func_9069
mod = relay.transform.InferType()(mod)
mutated_mod['func_9069'] = func_9069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9069_call = mutated_mod.get_global_var('func_9069')
call_9070 = func_9069_call()
output = call_9070
func_9071 = relay.Function([], output)
mutated_mod['func_9071'] = func_9071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_9084 = relay.TupleGetItem(func_3216_call(), 0)
call_9085 = relay.TupleGetItem(func_3217_call(), 0)
func_3954_call = mod.get_global_var('func_3954')
func_3957_call = mutated_mod.get_global_var('func_3957')
var_9111 = relay.var("var_9111", dtype = "float32", shape = (1680,))#candidate|9111|(1680,)|var|float32
call_9110 = relay.TupleGetItem(func_3954_call(relay.reshape(var_9111.astype('float32'), [1680,])), 3)
call_9112 = relay.TupleGetItem(func_3957_call(relay.reshape(var_9111.astype('float32'), [1680,])), 3)
output = relay.Tuple([call_9084,call_9110,var_9111,])
output2 = relay.Tuple([call_9085,call_9112,var_9111,])
func_9113 = relay.Function([var_9111,], output)
mod['func_9113'] = func_9113
mod = relay.transform.InferType()(mod)
var_9114 = relay.var("var_9114", dtype = "float32", shape = (1680,))#candidate|9114|(1680,)|var|float32
output = func_9113(var_9114)
func_9115 = relay.Function([var_9114], output)
mutated_mod['func_9115'] = func_9115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8701_call = mod.get_global_var('func_8701')
func_8702_call = mutated_mod.get_global_var('func_8702')
call_9119 = relay.TupleGetItem(func_8701_call(), 4)
call_9120 = relay.TupleGetItem(func_8702_call(), 4)
output = relay.Tuple([call_9119,])
output2 = relay.Tuple([call_9120,])
func_9121 = relay.Function([], output)
mod['func_9121'] = func_9121
mod = relay.transform.InferType()(mod)
mutated_mod['func_9121'] = func_9121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9121_call = mutated_mod.get_global_var('func_9121')
call_9122 = func_9121_call()
output = call_9122
func_9123 = relay.Function([], output)
mutated_mod['func_9123'] = func_9123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1452_call = mod.get_global_var('func_1452')
func_1454_call = mutated_mod.get_global_var('func_1454')
call_9196 = relay.TupleGetItem(func_1452_call(), 1)
call_9197 = relay.TupleGetItem(func_1454_call(), 1)
output = call_9196
output2 = call_9197
func_9200 = relay.Function([], output)
mod['func_9200'] = func_9200
mod = relay.transform.InferType()(mod)
mutated_mod['func_9200'] = func_9200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9200_call = mutated_mod.get_global_var('func_9200')
call_9201 = func_9200_call()
output = call_9201
func_9202 = relay.Function([], output)
mutated_mod['func_9202'] = func_9202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6578_call = mod.get_global_var('func_6578')
func_6580_call = mutated_mod.get_global_var('func_6580')
call_9228 = func_6578_call()
call_9229 = func_6578_call()
func_3705_call = mod.get_global_var('func_3705')
func_3707_call = mutated_mod.get_global_var('func_3707')
call_9244 = relay.TupleGetItem(func_3705_call(), 0)
call_9245 = relay.TupleGetItem(func_3707_call(), 0)
output = relay.Tuple([call_9228,call_9244,])
output2 = relay.Tuple([call_9229,call_9245,])
func_9248 = relay.Function([], output)
mod['func_9248'] = func_9248
mod = relay.transform.InferType()(mod)
output = func_9248()
func_9249 = relay.Function([], output)
mutated_mod['func_9249'] = func_9249
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9281 = relay.var("var_9281", dtype = "uint16", shape = (3, 13, 13))#candidate|9281|(3, 13, 13)|var|uint16
var_9282 = relay.var("var_9282", dtype = "uint16", shape = (3, 13, 13))#candidate|9282|(3, 13, 13)|var|uint16
bop_9283 = relay.right_shift(var_9281.astype('uint16'), relay.reshape(var_9282.astype('uint16'), relay.shape_of(var_9281))) # shape=(3, 13, 13)
output = relay.Tuple([bop_9283,])
output2 = relay.Tuple([bop_9283,])
func_9293 = relay.Function([var_9281,var_9282,], output)
mod['func_9293'] = func_9293
mod = relay.transform.InferType()(mod)
mutated_mod['func_9293'] = func_9293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9293_call = mutated_mod.get_global_var('func_9293')
var_9295 = relay.var("var_9295", dtype = "uint16", shape = (3, 13, 13))#candidate|9295|(3, 13, 13)|var|uint16
var_9296 = relay.var("var_9296", dtype = "uint16", shape = (3, 13, 13))#candidate|9296|(3, 13, 13)|var|uint16
call_9294 = func_9293_call(var_9295,var_9296,)
output = call_9294
func_9297 = relay.Function([var_9295,var_9296,], output)
mutated_mod['func_9297'] = func_9297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5798_call = mod.get_global_var('func_5798')
func_5799_call = mutated_mod.get_global_var('func_5799')
call_9316 = relay.TupleGetItem(func_5798_call(), 0)
call_9317 = relay.TupleGetItem(func_5799_call(), 0)
output = relay.Tuple([call_9316,])
output2 = relay.Tuple([call_9317,])
func_9318 = relay.Function([], output)
mod['func_9318'] = func_9318
mod = relay.transform.InferType()(mod)
mutated_mod['func_9318'] = func_9318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9318_call = mutated_mod.get_global_var('func_9318')
call_9319 = func_9318_call()
output = call_9319
func_9320 = relay.Function([], output)
mutated_mod['func_9320'] = func_9320
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9352 = relay.var("var_9352", dtype = "uint16", shape = (8, 2, 13))#candidate|9352|(8, 2, 13)|var|uint16
var_9353 = relay.var("var_9353", dtype = "uint16", shape = (8, 2, 13))#candidate|9353|(8, 2, 13)|var|uint16
bop_9354 = relay.less(var_9352.astype('bool'), relay.reshape(var_9353.astype('bool'), relay.shape_of(var_9352))) # shape=(8, 2, 13)
uop_9359 = relay.cosh(var_9353.astype('float32')) # shape=(8, 2, 13)
uop_9362 = relay.log2(uop_9359.astype('float32')) # shape=(8, 2, 13)
output = relay.Tuple([bop_9354,uop_9362,])
output2 = relay.Tuple([bop_9354,uop_9362,])
func_9365 = relay.Function([var_9352,var_9353,], output)
mod['func_9365'] = func_9365
mod = relay.transform.InferType()(mod)
mutated_mod['func_9365'] = func_9365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9365_call = mutated_mod.get_global_var('func_9365')
var_9367 = relay.var("var_9367", dtype = "uint16", shape = (8, 2, 13))#candidate|9367|(8, 2, 13)|var|uint16
var_9368 = relay.var("var_9368", dtype = "uint16", shape = (8, 2, 13))#candidate|9368|(8, 2, 13)|var|uint16
call_9366 = func_9365_call(var_9367,var_9368,)
output = call_9366
func_9369 = relay.Function([var_9367,var_9368,], output)
mutated_mod['func_9369'] = func_9369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_9457 = func_4180_call()
call_9458 = func_4180_call()
output = call_9457
output2 = call_9458
func_9464 = relay.Function([], output)
mod['func_9464'] = func_9464
mod = relay.transform.InferType()(mod)
output = func_9464()
func_9465 = relay.Function([], output)
mutated_mod['func_9465'] = func_9465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3828_call = mod.get_global_var('func_3828')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_9553 = func_3828_call()
call_9554 = func_3828_call()
var_9568 = relay.var("var_9568", dtype = "float32", shape = (14, 1, 15))#candidate|9568|(14, 1, 15)|var|float32
bop_9569 = relay.right_shift(call_9553.astype('int32'), relay.reshape(var_9568.astype('int32'), relay.shape_of(call_9553))) # shape=(14, 1, 15)
bop_9572 = relay.right_shift(call_9554.astype('int32'), relay.reshape(var_9568.astype('int32'), relay.shape_of(call_9554))) # shape=(14, 1, 15)
bop_9586 = relay.floor_divide(bop_9569.astype('float32'), relay.reshape(var_9568.astype('float32'), relay.shape_of(bop_9569))) # shape=(14, 1, 15)
bop_9589 = relay.floor_divide(bop_9572.astype('float32'), relay.reshape(var_9568.astype('float32'), relay.shape_of(bop_9572))) # shape=(14, 1, 15)
func_5177_call = mod.get_global_var('func_5177')
func_5179_call = mutated_mod.get_global_var('func_5179')
call_9590 = func_5177_call()
call_9591 = func_5177_call()
func_388_call = mod.get_global_var('func_388')
func_390_call = mutated_mod.get_global_var('func_390')
call_9612 = func_388_call()
call_9613 = func_388_call()
output = relay.Tuple([bop_9586,call_9590,call_9612,])
output2 = relay.Tuple([bop_9589,call_9591,call_9613,])
func_9614 = relay.Function([var_9568,], output)
mod['func_9614'] = func_9614
mod = relay.transform.InferType()(mod)
mutated_mod['func_9614'] = func_9614
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9615 = relay.var("var_9615", dtype = "float32", shape = (14, 1, 15))#candidate|9615|(14, 1, 15)|var|float32
func_9614_call = mutated_mod.get_global_var('func_9614')
call_9616 = func_9614_call(var_9615)
output = call_9616
func_9617 = relay.Function([var_9615], output)
mutated_mod['func_9617'] = func_9617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_209_call = mod.get_global_var('func_209')
func_210_call = mutated_mod.get_global_var('func_210')
call_9634 = relay.TupleGetItem(func_209_call(), 0)
call_9635 = relay.TupleGetItem(func_210_call(), 0)
output = relay.Tuple([call_9634,])
output2 = relay.Tuple([call_9635,])
func_9643 = relay.Function([], output)
mod['func_9643'] = func_9643
mod = relay.transform.InferType()(mod)
output = func_9643()
func_9644 = relay.Function([], output)
mutated_mod['func_9644'] = func_9644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5798_call = mod.get_global_var('func_5798')
func_5799_call = mutated_mod.get_global_var('func_5799')
call_9675 = relay.TupleGetItem(func_5798_call(), 0)
call_9676 = relay.TupleGetItem(func_5799_call(), 0)
func_2374_call = mod.get_global_var('func_2374')
func_2377_call = mutated_mod.get_global_var('func_2377')
const_9678 = relay.const([1.276396,0.163849,-5.197290,-7.412829,9.571818,2.949542,-3.196003,6.052683,-7.541905,9.109666,0.891723,3.223321,-8.598700,-0.476790,1.448813,-7.238091,2.129817,-5.768958,-7.213550,-3.792612,-9.546553,-5.096667,2.974841,1.298865,-7.509059,-8.619896,6.627453,-3.928854,-9.963740,3.577963,-7.779823,3.711735,-8.254927,6.844673,-9.620977,-2.479381,0.123145,5.737332,-5.492312,-0.108047,0.382515,-9.287108,-7.880301,0.136483,-1.050728,-0.030966,-9.381680,-1.151742,-1.797469,6.772945,-7.420873,5.441850,-3.870892,-8.010363,3.259987,-1.368369,7.196136,-1.550605,6.816576,7.440670,-3.763640,-3.165608,3.684799,4.537313,-0.766829,-5.360326,9.925004,-5.082838,3.511991,-9.942081,5.483202,3.480865,-6.962630,-2.489282,0.576257,9.186286,9.072559,-6.246546,-8.064719,-6.812559,9.542920,8.120749,-8.426113,-7.627927,8.691874,2.370493,4.593390,1.354742,-1.372528,6.651682,4.140838,1.853429,-1.809071,5.046599,-5.386310,4.695690,3.899020,-0.742521,-5.971259,5.675490,0.319430,-4.395691,2.121766,-6.873122,0.918791,-8.231216,-2.219318,-9.793920,2.184075,-8.621286,4.982567,6.678605,-6.513395,9.399637,7.610840,-3.448038,2.786640,6.281897,7.508480,-6.912128,-3.130138,4.800085,-2.545872,4.325340,-4.360995,8.566957,-7.949916,-5.115567,-9.463652,8.739185,-7.285432,7.475725,7.912975,-8.721543,-0.157373,1.441403,6.980658,-8.326035,-5.525491,-3.704770,9.191834,8.422971,-0.288333,-6.620851,9.468305,-8.451984,-0.637878,5.557303,3.661076,-5.823516,-6.924188,-6.063641,-3.139560,1.952043,-0.181318,8.667160,-3.527190,2.397266,-9.323560,7.025262,-4.631382,6.561467,8.484340,-2.381112,3.551710,9.606329,-3.182547,3.492039,-2.844594,-1.934004,-9.508083,-2.819661,-5.053218,-3.350804,1.167627,-7.549857,0.658232,-3.278468,-4.955926,1.089081,4.481910,0.154096,-4.250605,5.142972,2.496968,-6.130747,7.256406,-7.501229,-3.206063,8.367672,2.167666,3.204048,1.687121,5.639343,-0.157064,2.802795,1.103543,-3.356605,-7.737367,-9.850869,7.252490,3.309817,6.167997,-5.131179,-9.674080,-7.056053,2.649469,8.848582,1.861290,-3.203962,7.356120,-4.378249,-1.927081,4.093468,-3.156290,-9.254344,-8.604495,-1.840827,-3.570004,8.082103,-9.585188,-8.426975,-0.027130,5.879297,-4.562875,7.980881,9.508328,4.200635,-4.271940,-5.062113,-2.876258,-3.578388,8.384766,4.051396,7.815718,-2.667191,-7.781086,0.361285,-8.961096,-0.001911,-0.414779,8.669409,2.383655,4.388163,7.228953,-4.781221,1.662526,-1.586847,-2.037452,-6.992779,-0.030394,7.863710,6.973398,9.592146,2.105694,-6.471236,-9.179288,-2.872254,-1.296831,6.898412,7.434293,-8.926238,3.529561,7.576519,-9.899597,9.426914,4.267483,6.185500,-3.856637,-7.875171,-6.411554,7.146577,-2.585007,1.996204,-3.376008,-9.977087,-7.822789,-3.685691,6.638819,2.017548,7.969720,5.607782,-2.356384,3.843560,8.736581,-4.733646,-5.678355,-1.003659,1.865164,-0.214180,4.341372,-0.155182,9.560316,0.189547,-0.738013,-8.415112,8.117433,-7.505951,-0.077242,-8.620747,-2.999974,1.245775,9.201331,7.940511,9.134359,-1.303521,9.917165,6.443970,5.369373,1.294302,2.336932,3.889303,2.657375,-6.746734,8.903874,-6.720776,-9.479151,-7.811437,4.123904,-0.528411,9.394411,6.410871,9.632314,7.182233,1.762650,0.645114,-8.856317,-2.268563,-5.774041,5.444143,6.975219,4.933604,-6.491219,0.308880,-0.464172,-0.466105,-3.436267,-5.863583,-8.533827,-2.335967,-3.525134,6.723147,-6.663667,3.185140,-4.521989,-2.534517,-0.030961,2.828971,-8.709314,-6.041886,2.499662,-6.808726,0.734484,7.464480,8.922602,1.190920,9.857297,-7.586735,-3.988457,6.225271,3.469514,7.237555,4.482269,-9.219113,3.255013,-1.852290,0.555138,4.618476,0.713317,6.216897,-6.076656,5.516751,9.369067,-1.148579,2.919611,-3.582207,7.941039,-8.956581,9.196116,-4.223058,4.581255,2.869777,-4.767001,5.699448,2.972303,-2.678451,-4.661353,-4.826187,2.743186,1.516550,-2.291843,2.237431,8.937500,-1.781770,-9.887280,-9.421372,-2.720390,6.384234,-2.124979,-1.774371,3.744144,0.316248,-8.377497,2.884429,-6.166952,-1.724637,-2.556331,8.143872,3.814750,-4.520521,-1.610163,-7.895776,-9.489657,1.828177,-9.919592,5.626061,-7.623973,0.636124,-7.410784,7.238404,-2.056199,6.797691,4.490231,-2.473241,-1.986549,9.074450,1.398233,8.220974,0.481456,-0.878070,6.067239,3.764731,8.356528,-6.413182,4.533768,-1.595653,-3.927761,-6.749576,-8.043274,-7.938753,-4.968525,-1.391462,2.626484,3.117610,-8.491999,8.790595,0.385725,-3.911522,6.744994,-7.607880,-9.319160,-9.369021,-2.866515,-9.259832,-2.759617,-3.049694,-8.860940,-5.040458,-2.499897,-9.588171,-1.820158,-1.317278,-9.318648,-3.380396,-6.793431,-8.324756,0.251511,7.330786,-2.360899,2.664336,-0.516171,9.153640,-7.738909,1.625353,4.582429,8.196928,2.413254,-0.796366,-2.583631,8.397561,1.857444,6.713436,0.178038,4.877862,3.539419,-6.315154,-9.683364,-2.706135,4.112787,9.251899,-6.775652,-7.635413,0.368622,0.452132,9.014845,-8.225421,6.327536,-9.243926,-9.929542,-0.592864,-7.212594,5.429795,-6.246480,2.677010,2.748110,-2.580638,7.686591,4.895888,9.760121,7.565168,-7.663795,-7.773926,6.851628,-2.437482,-9.311879,7.558616,7.912112,9.628410,9.107196,3.454853,0.280157,-0.197644,7.274413,7.158325,-1.862040,3.015285,-5.380042,-6.624164,-3.262688,4.988851,6.066628,4.075807,-8.849930,-5.322186,0.311384,-5.375419,-5.308262,-6.583836,6.239902,-5.082812,-0.393041,-2.322592,7.439623,-2.995258,9.436017,-5.941920,9.975499,1.685513,-9.990344,6.146964,3.515639,4.352661,-1.800515,3.864365,0.139906,5.601698,-2.368881,8.017259,8.169861,7.001930,6.981283,1.587437,-4.486634,-0.043733,9.518180,-6.947668,-0.206620,-7.326051,9.466446,-3.558805,8.410155,-7.760352,7.333922,-9.397490,-7.412495,0.383566,5.259530,-2.484830,9.284491,3.640761,-6.451395,4.613192,9.214132,4.403201,-7.992400,9.502813,7.051300,0.516946,9.048802,5.469862,6.031234,-7.228097,-4.135232,-3.363468,5.321636,-7.864928,-7.585689,-6.101403,2.126311,-5.666519,1.117569,7.665088,-8.882870,6.684904,-9.635852,1.707162,1.634125,2.315369,-9.155817,6.904850,5.595294,6.203485,-5.667623,6.282733,2.764904,5.262836,5.184394,1.438686,1.065624,-9.017496,-5.510879,6.932060,2.210331,2.152022,2.485664,2.560100,-7.862951,-2.617065,2.617261,-9.724394,0.815494,1.537726,-3.321861,-7.420904,-4.464800,-0.021667,-2.191831,-8.592865,-5.318537,5.215349,4.270135,-0.083311,5.106806,-1.634517,-3.511532,1.363687,-7.432899,-0.106523,-7.516413,-0.751354,6.458870,3.150207,-7.137094,0.932005,4.682502,-0.920397,-3.636782,-6.473236,7.830115,-4.751632,6.080259,-1.058659,-2.505181,-0.892889,0.594169,1.893814,8.545709,7.163524,5.547558,-5.771668,9.060678,6.849555,7.949582,-9.575415,-1.131991,-3.809225,-7.588230,5.009707,-0.404505,8.573546,-1.395602,-4.441746,1.622669,1.530940,4.671149,4.018557,2.563120,-2.532136,-6.627683,2.635215,3.611236,-7.542009,-7.784665,-1.643100,-5.618657,4.235255,5.367787,-3.673915,3.349838,9.933752,-3.860651,9.325264,8.530381,-9.557591,-2.410397,-6.177272,-9.206054,-2.661104,-2.285516,9.752611,-7.349024,1.329352,-7.551479,3.396767,3.589651,-2.465689,1.642168,2.283160,3.330447,9.662630,-8.538380,3.998360,-7.162350,8.643616,9.589473,4.004588,1.251355,9.178969,2.163482,0.519991,3.465729,-0.456179,-6.877761,2.250248,6.375726,0.851475,-8.780227,-2.668912,-8.277224,3.041358,-5.210400,-8.060901,3.291273,-8.568600,-0.851288,9.265697,5.898305,-2.263832,-8.396408,-4.045814,-2.387427,2.085706,-1.076340,-7.638280,6.204878,-1.063574,-7.327427,-6.646786,-2.163455,-5.372147,-2.770261,-1.469389,9.556672,7.761563,-8.369874,-3.100524,-9.624167,2.323267,9.268458,0.854493,2.134995,0.986493,-1.101496,2.742917,-3.045123,9.838987,-0.573041,-5.631829,2.460744,5.652821,2.653612,-7.835668,3.541736,2.127717,2.563962,1.846667,-9.748907,2.447113,-1.009600,-8.023194,-4.976105,-4.387425,9.968361,7.571386,-5.467253,9.563022,-8.298419,4.440425,6.999387,-2.701631,-2.117984,-9.382534,-9.184979,4.857805,-9.912205,7.844861,-9.300543,1.645623,0.923579,-7.702681,2.752595,5.236072,4.456073,1.221466,5.713022,-1.475970,-3.257093,8.844024,-7.755867,5.815558,-7.884655,5.279409,-6.483245,-8.597916,7.431178,-2.082838,-1.076784,-3.080401,-1.892688,2.130237,-3.203116,9.590935,-3.175778,6.749152,-8.464326,7.228487,-1.171383,6.683768,-8.443874,-4.356251,-3.497744,-4.079682,-9.958720,-3.447580,9.607509,4.672418,7.728970,-3.581587,3.224044,-5.851174,-7.393256,-6.288702,9.260005,-2.479179,0.592604,4.420533,9.069804,9.957171,3.176373,-1.893610,2.706595,-2.584049,6.615774,-1.480067,-6.276874,-8.809312,-8.564194,6.637141,-5.533177,7.045165,-3.482442,7.350893,7.297009,-2.944762,-3.820292,5.694222,-6.518277,1.993626,-8.407014,-5.099083,-5.119137,2.044755,7.711409,-0.469984,-4.953057,5.474693,5.980509,-8.881992,1.427050,7.956140,-7.772973,4.507077,-7.335761,-0.444513,-4.930966,6.192736,8.525133,-6.317585,-6.038657,-8.318785,-0.681923,6.447922,-2.312151,-0.445547,-6.875783,7.711178,-8.299387,7.330359,9.388744,1.853530,-5.927718,2.078412,-6.457678,-4.974654,-3.335279,4.956297,7.253963,-9.227072,4.494015,8.485905,-7.807301,-1.078643,-3.894600,3.531865,6.701331,8.965259,-0.994632,2.370379,-2.800510,2.477587,-4.107958,-4.061071,4.489042,2.774118,3.574712,2.680611,3.073673,5.797777,5.018557,-3.285926,9.280084,2.490160,-0.428361,-8.162570,-3.033236,3.476419,0.976808,-7.442548,2.854564,3.700480,0.969818,-9.087984,-2.582255,-9.665461,2.707991,-5.094898,-6.473802,-5.554920,-6.453794,-0.665972,-7.696558,5.400914,7.287957,-5.828899,2.880193,3.116826,-9.994129,6.494372,6.671886,5.755864,-2.123492,-7.983447,5.999298,3.259505,0.016073,-2.860555,-6.984602,3.490755,-7.183478,-5.123167,0.474220,-7.811097,6.937910,-3.978041,8.203067,7.630162,1.070451,-1.277305,-5.903566,-6.852697,8.104397,4.848771,-3.035943,6.948082,4.492786,-1.747171,-4.672689,-5.335228,8.057827,-6.156121,-2.111792,-7.987098,4.101660,-5.254093,0.005245,-9.673976,-7.091894,-5.328109,-7.497997,5.979169,4.774255,1.815944,-3.959756,7.210403,-6.259588,-0.231547,-7.197474,3.865730,7.990904,9.265189,-3.645660,-5.902148,-5.671487,-6.284361,-7.455226,-7.948420,4.737385,8.685830,1.975705,2.607405,1.410072,8.200097,6.299304,9.600355,-8.552397,7.019062,-5.324186,7.257037,-3.925796,-8.513362,8.771465,-3.458730,-6.000607,-9.552628,-0.887579,9.453463,2.083083,5.876456,5.403614,-5.865877,-0.342039,7.790633,8.914627,1.781152,-4.803696,-1.986480,-1.081488,-5.434494,2.315517,-7.666844,1.598338,5.351217,-2.854227,5.646386,6.090987,-7.041440,3.905058,7.249216,-2.447925,-4.702635,-4.832739,3.861530,1.703536,1.726326,-8.084683,-5.528667,4.725329,5.771880,7.544278,-0.326233,-7.592697,-4.226636,-9.516417,-5.127580,-6.893134,6.396661,4.118692,4.594869,-8.757696,9.414361,-2.948021,-3.471891,8.476147,-2.971265,-2.378451,-3.401306,9.088782,-2.697868,-8.781944,-6.755036,0.628522,7.790919,-1.602329,7.600959,3.955582,-2.725276,0.619763,0.937455,-0.470413,9.599935,-9.919202,4.595568,-9.690029,5.417741,-8.707641,4.042951,8.433992,-1.490103,9.320250,6.720855,3.922674,-6.302611,-0.900249,2.593979,7.849556,-7.509190,-2.345662,1.609429,4.179231,5.463418,5.704750,-1.447634,8.393829,-0.621293,-0.407512,9.618168,6.125850,-2.808555,-4.303103,-5.553149,-6.569015,3.078954,-9.648574,9.067110,-1.709782,6.864813,2.753090,-5.380729,6.723903,3.665459,-8.725466,1.445388,7.527291,-6.777083,1.868265,9.347106,0.403820,7.604858,-6.268108,3.673515,4.844161,-8.429054,-3.128501,-9.082719,3.477196,-8.103480,-7.901599,-0.610217,9.536186,0.272205,6.130735,7.799764,-6.629225,6.189254,7.450587,3.551750,3.565985,-9.374764,-5.867258,3.570767,-3.565290,-2.538449,3.945682,-4.758234,1.805335,-5.063917,7.026286,6.203060,-1.274053,-4.785665,5.180880,-0.389802,4.442522,5.071379,3.363499,6.917723,-5.969714,2.900258,-9.941593,-7.380208,5.052506,2.237420,-0.727528,-8.306142,6.620212,7.523010,-7.176931,8.603626,-0.910704,-5.309656,-3.991674,0.905925,2.757042,-7.580087,8.560458,7.055913,6.361563,2.547617,8.372318,-0.180859,-6.107729,3.891947,-0.714445,-7.435143,2.483628,-5.989808,-1.344851,-6.394311,-2.573104,-5.908769,-5.966987,8.200630,-4.877775,5.246639,-5.620737,-6.835066,5.588677,-8.915519,-5.753055,-4.694190,8.682221,6.283771,9.372795,5.096105,5.784818,2.747155,7.345319,6.950753,9.349847,2.258145,2.046934,-3.941552,9.710021,-8.148576,0.339592,-9.804599,3.685870,-1.251318,3.407461,9.737581,3.427630,-8.392473,0.025036,-2.212878,5.864210,-5.770238,5.422742,1.293750,1.332590,2.722280,1.489373,3.905555,7.658861,6.930913,0.500364,2.337468,8.135930,0.087660,-3.001068,6.047462,0.102927,-4.414255,-5.656197,-3.868880,2.842514,-2.556027,4.038786,6.102422,7.183274,1.124843,9.673461,-5.341691,6.290258,3.864620,4.740747,4.806022,9.395154,-7.383262,2.547252,9.275426,-8.092328,8.461950,-7.632099,-4.334680,4.917238,-1.058064,1.783226,5.488850,2.039868,-6.063486,6.048916,3.212785,5.790219,-4.633196,-4.718576,7.200761,7.947908,-5.832320,5.227654,-6.465351,2.526027,-9.112718,7.720024,3.307224,-5.486101,7.170224,5.414072,-8.237298,-2.732691,9.245811,1.864209,4.449862,-9.005611,-1.301963,8.248832,-4.341252,2.920366,2.815324,9.556992,7.315246,-5.545420,6.087231,-0.999226,-3.641400,4.356284,5.602172,-4.661945,1.500866,4.711451,-4.038584,-5.272594,3.837861,7.085892,-4.896186,3.739496,9.631550,3.383474,9.931349,-8.205782,-7.580039,8.388279,-3.492930,9.699114,-0.904505,1.386606,2.569416,-4.562766,-9.174784,6.602577,-6.868375,-3.271087,-3.953381,-5.347402,4.142697,8.358183,-8.052021,-4.139685,-3.785281,9.662558,-2.309764,9.291431,-3.286085,-9.693317,-9.911985,-7.505765,-2.430806,-4.533651,-9.570817,-5.458063,5.033851,1.960858,-8.122710,0.892786,3.145418,-8.396983,4.591604,6.125158,3.228138,-9.142903,3.353328,-8.960554,-4.017446,-2.227014,5.989305,-8.178959,-3.322200,1.023788,5.442289,1.801273,3.868054,-4.019650,-5.124789,-9.934690,4.878493,3.019896,2.030171,-8.431956,-4.630398,-8.824205,9.786909,-2.466942,5.684148,2.608830,-1.360426,9.383070,-1.308440,1.446707,-8.915875,-4.686685,-8.321268,-6.111629,4.345786,9.886436,-1.054793,5.433958,1.149950,5.162051,7.317399,6.474060,-3.059772,2.104554,9.814154,0.993731,8.978360,3.206459,4.825627,9.375363,2.906410,-5.382025,4.937718,7.801521,9.349610,0.906395,9.310715,4.131037,4.771119,-6.634139,2.008765,-6.238973,6.873689,-1.359193,-5.763831,4.399057,7.821942,1.242813,-3.859306,1.189846,9.264278,-0.127051,9.892267,-5.420709,6.033466,0.588391,-4.114807,4.438280,-1.508286,-3.789834,0.222962,-3.052654,6.809141,4.365114,-0.771068,-7.278377,3.110268,9.705454,-1.060491,-3.905252,-8.174827,-2.157857,2.275325,0.341950,4.498594,-4.073094,4.642101,8.321538,-2.571324,-5.954710,2.139857,1.916744,-6.637221,-4.463458,-4.299704,-8.465461,-6.354030,-1.415095,-2.224449,2.451330,1.163473,-6.638520,-6.485554,-9.037089,1.561160,-4.084976,9.843442,2.487285,-0.611573,-9.763375,-5.212693,6.505321,6.047773,8.540109,3.444468,7.895531,-1.106662,-9.171360,-1.889240,-6.516543,7.354302,-3.546315,-9.067422,-3.591975,2.967651,7.673670,3.266047,3.851008,-7.177194,-4.974961,9.849971,1.145791,-8.061271,5.795962,-1.446932,-6.968556,-9.497016,-8.395131,-3.993435,9.775233,5.448374,-8.609080,4.015251,2.892954,-2.116218,-9.251873,5.383554,3.618658,7.056535,-5.887242,-2.822655,3.938238,-7.002634,4.381412,6.044807,-6.941618,-4.761333,6.166982,-9.279786,3.120171,7.538300,7.331610,5.966605,-1.884162,5.759470,-6.226761,2.641698,-9.844509,1.960907,-4.041639,-3.794212,9.146958,0.038316,-5.198154,6.700282,-3.804637,6.148359,-4.293103,5.599355,1.181428,2.303294,-8.241388,-8.111221,-5.989374,4.470983,-9.460375,-2.700905,-4.658537,-1.336295,5.060272,-0.423852,-7.442720,7.204406,0.771343,9.807236,7.815694,-1.804968,1.038477,-4.919693,2.460128,8.854795,4.673494,0.240235,1.448188,1.157447,-3.966089,7.777263,1.094694,1.212995,0.414961,-9.776910,2.030618,-2.542740,9.565345,7.449642,-0.250319,-2.237063,-4.226071,3.209475,3.726972,-6.794535,9.153155,6.129040,2.873968,2.989331,5.487052,8.127335,-3.856207,-4.434874,6.198170,-7.355115,-9.657717,7.366384,1.006917,-1.568336,5.434468,-0.858031,-8.173521,-0.156379,-0.943071,-1.801307,6.998851,-4.763719,-7.233907,6.002343,-0.189775,1.791221,-4.649297,3.735046,-0.324948,-3.238997,0.803855,-6.698666,-7.391520,4.522063,-6.751796,8.563087,9.014950,4.736952,-4.522240,1.134326,7.442141,8.772114,-9.625313,3.895058,-0.549260,-5.653005,-8.078343,-5.925053,1.504475,3.500954,8.555493,1.522841], dtype = "float32")#candidate|9678|(1680,)|const|float32
call_9677 = relay.TupleGetItem(func_2374_call(relay.reshape(const_9678.astype('float32'), [1680, 1])), 0)
call_9679 = relay.TupleGetItem(func_2377_call(relay.reshape(const_9678.astype('float32'), [1680, 1])), 0)
func_4778_call = mod.get_global_var('func_4778')
func_4780_call = mutated_mod.get_global_var('func_4780')
var_9694 = relay.var("var_9694", dtype = "float32", shape = (420,))#candidate|9694|(420,)|var|float32
call_9693 = relay.TupleGetItem(func_4778_call(relay.reshape(var_9694.astype('float32'), [420,])), 0)
call_9695 = relay.TupleGetItem(func_4780_call(relay.reshape(var_9694.astype('float32'), [420,])), 0)
func_1269_call = mod.get_global_var('func_1269')
func_1270_call = mutated_mod.get_global_var('func_1270')
call_9707 = relay.TupleGetItem(func_1269_call(), 2)
call_9708 = relay.TupleGetItem(func_1270_call(), 2)
func_5744_call = mod.get_global_var('func_5744')
func_5746_call = mutated_mod.get_global_var('func_5746')
call_9713 = relay.TupleGetItem(func_5744_call(), 2)
call_9714 = relay.TupleGetItem(func_5746_call(), 2)
bop_9728 = relay.greater_equal(call_9707.astype('bool'), relay.reshape(call_9693.astype('bool'), relay.shape_of(call_9707))) # shape=(14, 1, 15)
bop_9731 = relay.greater_equal(call_9708.astype('bool'), relay.reshape(call_9695.astype('bool'), relay.shape_of(call_9708))) # shape=(14, 1, 15)
output = relay.Tuple([call_9675,call_9677,const_9678,var_9694,call_9713,bop_9728,])
output2 = relay.Tuple([call_9676,call_9679,const_9678,var_9694,call_9714,bop_9731,])
F = relay.Function([var_9694,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9694,], output2)
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
