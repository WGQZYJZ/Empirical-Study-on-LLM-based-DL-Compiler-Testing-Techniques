import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_265 = relay.var("var_265", dtype = "float64", shape = (6, 3, 4))#candidate|265|(6, 3, 4)|var|float64
uop_266 = relay.sinh(var_265.astype('float64')) # shape=(6, 3, 4)
output = uop_266
output2 = uop_266
func_286 = relay.Function([var_265,], output)
mod['func_286'] = func_286
mod = relay.transform.InferType()(mod)
var_287 = relay.var("var_287", dtype = "float64", shape = (6, 3, 4))#candidate|287|(6, 3, 4)|var|float64
output = func_286(var_287)
func_288 = relay.Function([var_287], output)
mutated_mod['func_288'] = func_288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_490 = relay.var("var_490", dtype = "uint32", shape = ())#candidate|490|()|var|uint32
var_491 = relay.var("var_491", dtype = "uint32", shape = (3, 7, 3))#candidate|491|(3, 7, 3)|var|uint32
bop_492 = relay.bitwise_xor(var_490.astype('uint32'), var_491.astype('uint32')) # shape=(3, 7, 3)
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
var_496 = relay.var("var_496", dtype = "float64", shape = (72,))#candidate|496|(72,)|var|float64
call_495 = func_286_call(relay.reshape(var_496.astype('float64'), [6, 3, 4]))
call_497 = func_286_call(relay.reshape(var_496.astype('float64'), [6, 3, 4]))
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
call_504 = func_286_call(relay.reshape(var_496.astype('float64'), [6, 3, 4]))
call_505 = func_286_call(relay.reshape(var_496.astype('float64'), [6, 3, 4]))
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
call_509 = func_286_call(relay.reshape(call_495.astype('float64'), [6, 3, 4]))
call_510 = func_286_call(relay.reshape(call_495.astype('float64'), [6, 3, 4]))
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
call_523 = func_286_call(relay.reshape(var_496.astype('float64'), [6, 3, 4]))
call_524 = func_286_call(relay.reshape(var_496.astype('float64'), [6, 3, 4]))
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
call_548 = func_286_call(relay.reshape(call_504.astype('float64'), [6, 3, 4]))
call_549 = func_286_call(relay.reshape(call_504.astype('float64'), [6, 3, 4]))
output = relay.Tuple([bop_492,call_495,var_496,call_504,call_509,call_523,call_548,])
output2 = relay.Tuple([bop_492,call_497,var_496,call_505,call_510,call_524,call_549,])
func_550 = relay.Function([var_490,var_491,var_496,], output)
mod['func_550'] = func_550
mod = relay.transform.InferType()(mod)
mutated_mod['func_550'] = func_550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_550_call = mutated_mod.get_global_var('func_550')
var_552 = relay.var("var_552", dtype = "uint32", shape = ())#candidate|552|()|var|uint32
var_553 = relay.var("var_553", dtype = "uint32", shape = (3, 7, 3))#candidate|553|(3, 7, 3)|var|uint32
var_554 = relay.var("var_554", dtype = "float64", shape = (72,))#candidate|554|(72,)|var|float64
call_551 = func_550_call(var_552,var_553,var_554,)
output = call_551
func_555 = relay.Function([var_552,var_553,var_554,], output)
mutated_mod['func_555'] = func_555
mutated_mod = relay.transform.InferType()(mutated_mod)
var_582 = relay.var("var_582", dtype = "int8", shape = ())#candidate|582|()|var|int8
const_583 = relay.const([[[-9],[8],[-10],[7],[-8],[-2],[8]]], dtype = "int8")#candidate|583|(1, 7, 1)|const|int8
bop_584 = relay.right_shift(var_582.astype('int8'), const_583.astype('int8')) # shape=(1, 7, 1)
bop_587 = relay.less_equal(var_582.astype('bool'), bop_584.astype('bool')) # shape=(1, 7, 1)
output = bop_587
output2 = bop_587
func_592 = relay.Function([var_582,], output)
mod['func_592'] = func_592
mod = relay.transform.InferType()(mod)
var_593 = relay.var("var_593", dtype = "int8", shape = ())#candidate|593|()|var|int8
output = func_592(var_593)
func_594 = relay.Function([var_593], output)
mutated_mod['func_594'] = func_594
mutated_mod = relay.transform.InferType()(mutated_mod)
var_679 = relay.var("var_679", dtype = "uint64", shape = (12, 5, 1))#candidate|679|(12, 5, 1)|var|uint64
const_680 = relay.const([[[-6],[3],[4],[-2],[7]],[[1],[1],[-9],[-2],[2]],[[7],[3],[-6],[5],[7]],[[3],[6],[-9],[-7],[-3]],[[6],[-6],[5],[-6],[10]],[[-10],[5],[-8],[-2],[8]],[[9],[-3],[9],[-5],[2]],[[3],[-3],[2],[4],[7]],[[-7],[1],[-10],[-5],[-2]],[[-4],[-6],[5],[-8],[2]],[[-10],[7],[-5],[5],[1]],[[3],[1],[-2],[-5],[-5]]], dtype = "uint64")#candidate|680|(12, 5, 1)|const|uint64
bop_681 = relay.maximum(var_679.astype('uint64'), relay.reshape(const_680.astype('uint64'), relay.shape_of(var_679))) # shape=(12, 5, 1)
func_550_call = mod.get_global_var('func_550')
func_555_call = mutated_mod.get_global_var('func_555')
const_694 = relay.const(-10, dtype = "uint32")#candidate|694|()|const|uint32
var_695 = relay.var("var_695", dtype = "uint32", shape = (7, 9))#candidate|695|(7, 9)|var|uint32
const_696 = relay.const([0.285529,-2.547972,-4.201449,2.362690,5.297276,1.482105,-2.716571,1.402593,5.833685,8.207990,8.192485,-7.497516,-5.581564,0.616411,3.781386,2.344237,-2.156068,-3.488919,0.735696,-5.940055,-0.578510,7.726653,6.010302,-2.069763,-9.410927,-0.796903,8.541420,6.863835,4.585017,-3.587148,-4.124224,-6.679383,5.623859,5.912746,-5.754714,-2.326947,0.523011,2.546182,-1.878118,-3.716113,-0.595125,1.546928,5.551746,2.811103,2.219484,-2.359873,2.125521,-3.916905,4.186416,-1.652975,1.112482,-8.862520,-3.417580,9.044993,0.342669,7.158759,9.691106,-3.964869,5.858255,2.321014,9.381205,-3.841757,-1.699355,4.774497,-7.835489,-1.435992,-5.265633,-2.177255,-3.181831,-1.186230,0.924083,9.436777], dtype = "float64")#candidate|696|(72,)|const|float64
call_693 = relay.TupleGetItem(func_550_call(relay.reshape(const_694.astype('uint32'), []), relay.reshape(var_695.astype('uint32'), [3, 7, 3]), relay.reshape(const_696.astype('float64'), [72,]), ), 0)
call_697 = relay.TupleGetItem(func_555_call(relay.reshape(const_694.astype('uint32'), []), relay.reshape(var_695.astype('uint32'), [3, 7, 3]), relay.reshape(const_696.astype('float64'), [72,]), ), 0)
output = relay.Tuple([bop_681,call_693,const_694,var_695,const_696,])
output2 = relay.Tuple([bop_681,call_697,const_694,var_695,const_696,])
func_708 = relay.Function([var_679,var_695,], output)
mod['func_708'] = func_708
mod = relay.transform.InferType()(mod)
mutated_mod['func_708'] = func_708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_708_call = mutated_mod.get_global_var('func_708')
var_710 = relay.var("var_710", dtype = "uint64", shape = (12, 5, 1))#candidate|710|(12, 5, 1)|var|uint64
var_711 = relay.var("var_711", dtype = "uint32", shape = (7, 9))#candidate|711|(7, 9)|var|uint32
call_709 = func_708_call(var_710,var_711,)
output = call_709
func_712 = relay.Function([var_710,var_711,], output)
mutated_mod['func_712'] = func_712
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2599 = relay.var("var_2599", dtype = "float32", shape = (10, 15, 16))#candidate|2599|(10, 15, 16)|var|float32
var_2600 = relay.var("var_2600", dtype = "float32", shape = (10, 15, 16))#candidate|2600|(10, 15, 16)|var|float32
bop_2601 = relay.greater_equal(var_2599.astype('bool'), relay.reshape(var_2600.astype('bool'), relay.shape_of(var_2599))) # shape=(10, 15, 16)
output = relay.Tuple([bop_2601,])
output2 = relay.Tuple([bop_2601,])
func_2616 = relay.Function([var_2599,var_2600,], output)
mod['func_2616'] = func_2616
mod = relay.transform.InferType()(mod)
mutated_mod['func_2616'] = func_2616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2616_call = mutated_mod.get_global_var('func_2616')
var_2618 = relay.var("var_2618", dtype = "float32", shape = (10, 15, 16))#candidate|2618|(10, 15, 16)|var|float32
var_2619 = relay.var("var_2619", dtype = "float32", shape = (10, 15, 16))#candidate|2619|(10, 15, 16)|var|float32
call_2617 = func_2616_call(var_2618,var_2619,)
output = call_2617
func_2620 = relay.Function([var_2618,var_2619,], output)
mutated_mod['func_2620'] = func_2620
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3130 = relay.var("var_3130", dtype = "float32", shape = (5, 10, 14))#candidate|3130|(5, 10, 14)|var|float32
uop_3131 = relay.exp(var_3130.astype('float32')) # shape=(5, 10, 14)
bop_3133 = relay.floor_divide(var_3130.astype('float32'), relay.reshape(uop_3131.astype('float32'), relay.shape_of(var_3130))) # shape=(5, 10, 14)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
var_3137 = relay.var("var_3137", dtype = "int8", shape = ())#candidate|3137|()|var|int8
call_3136 = func_592_call(relay.reshape(var_3137.astype('int8'), []))
call_3138 = func_592_call(relay.reshape(var_3137.astype('int8'), []))
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
var_3146 = relay.var("var_3146", dtype = "float32", shape = (2400,))#candidate|3146|(2400,)|var|float32
call_3145 = relay.TupleGetItem(func_2616_call(relay.reshape(var_3146.astype('float32'), [10, 15, 16]), relay.reshape(var_3146.astype('float32'), [10, 15, 16]), ), 0)
call_3147 = relay.TupleGetItem(func_2620_call(relay.reshape(var_3146.astype('float32'), [10, 15, 16]), relay.reshape(var_3146.astype('float32'), [10, 15, 16]), ), 0)
output = relay.Tuple([bop_3133,call_3136,var_3137,call_3145,var_3146,])
output2 = relay.Tuple([bop_3133,call_3138,var_3137,call_3147,var_3146,])
func_3151 = relay.Function([var_3130,var_3137,var_3146,], output)
mod['func_3151'] = func_3151
mod = relay.transform.InferType()(mod)
mutated_mod['func_3151'] = func_3151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3151_call = mutated_mod.get_global_var('func_3151')
var_3153 = relay.var("var_3153", dtype = "float32", shape = (5, 10, 14))#candidate|3153|(5, 10, 14)|var|float32
var_3154 = relay.var("var_3154", dtype = "int8", shape = ())#candidate|3154|()|var|int8
var_3155 = relay.var("var_3155", dtype = "float32", shape = (2400,))#candidate|3155|(2400,)|var|float32
call_3152 = func_3151_call(var_3153,var_3154,var_3155,)
output = call_3152
func_3156 = relay.Function([var_3153,var_3154,var_3155,], output)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3422 = relay.const([[[-7,-7,7,-7,7,3,-9,-9,3,-10,-7],[1,7,-9,7,6,-6,3,4,4,-9,5],[5,-4,8,-1,10,-6,-4,-6,5,-9,7],[-4,1,4,-8,5,-5,-2,-4,1,-8,3],[-2,-7,2,-7,7,10,9,5,5,1,-10]],[[6,-7,-9,3,-9,2,-1,-9,3,-10,-3],[1,8,-7,-7,-3,2,-9,7,5,-7,1],[3,-8,7,3,7,-5,9,6,-8,6,-9],[2,-7,3,6,-5,3,7,-1,7,4,5],[-3,-7,7,2,2,-3,3,-4,9,9,-3]],[[1,7,-2,-1,4,7,6,9,-2,-4,-10],[3,7,3,6,-2,-10,7,2,10,-2,9],[10,6,9,-1,8,-2,7,-10,-1,-10,-1],[-2,2,1,8,-2,10,-2,-9,-7,-6,3],[-4,4,3,-6,-10,-9,2,-6,2,9,-7]],[[10,-4,4,-3,3,8,-3,-3,7,-9,6],[6,2,-10,-9,-9,-5,-5,-3,6,8,-3],[-6,1,-10,2,4,7,-8,-4,-6,-8,-8],[-9,-3,-4,10,-3,-4,2,9,-9,3,-6],[5,-10,4,1,10,2,-7,-6,4,5,-6]],[[-3,2,7,-7,8,4,10,-5,2,3,1],[-8,8,6,3,2,-6,-5,-2,5,-4,-8],[-9,-7,8,-2,-9,8,6,1,-8,5,-9],[-9,5,-1,-5,3,-1,4,2,2,10,-9],[6,8,-6,9,3,8,-4,-7,7,-4,2]],[[-2,7,6,-4,6,8,3,6,9,4,5],[6,8,2,4,3,8,9,-1,-10,4,-10],[-10,-1,-6,-8,-4,3,-10,5,10,-1,1],[-4,-5,-9,10,6,-8,3,-3,-4,-5,-8],[-5,8,-2,-6,1,5,-4,-4,4,6,-6]],[[-5,-10,-3,-8,-10,3,-10,9,8,-8,5],[-7,-6,-9,-4,-3,-4,-10,10,10,-2,-9],[10,10,9,2,10,1,2,-2,4,5,-10],[7,-2,-1,-9,-9,-10,8,-9,-1,10,6],[-3,6,6,7,6,-8,-10,5,9,10,-2]],[[-7,7,-9,2,-8,-8,4,6,1,-5,2],[-6,-7,-10,-4,-3,3,-1,-8,-10,9,1],[-1,3,8,-9,-3,7,9,7,10,-4,-4],[5,-7,-8,-4,-10,-5,9,10,6,-4,-5],[10,6,-4,3,7,-9,7,-1,-6,8,-3]],[[-7,-4,10,5,10,-9,-7,1,10,2,-2],[-7,-9,-3,4,-1,-1,-1,-2,-6,6,-1],[8,-5,-9,8,-5,4,7,1,5,2,7],[-9,-2,3,10,-10,-5,-9,-1,6,3,2],[-1,-3,4,-4,-9,-4,-8,8,1,10,-3]],[[2,7,2,2,-4,-6,9,2,-5,-6,1],[-5,6,7,4,5,3,-6,6,8,10,6],[-6,-5,-1,-1,7,-1,10,10,-5,-9,-9],[-3,4,-4,5,-6,-10,5,1,4,-10,2],[-5,5,9,10,3,-2,5,1,-8,5,7]]], dtype = "int8")#candidate|3422|(10, 5, 11)|const|int8
var_3423 = relay.var("var_3423", dtype = "int8", shape = (10, 5, 11))#candidate|3423|(10, 5, 11)|var|int8
bop_3424 = relay.less(const_3422.astype('bool'), relay.reshape(var_3423.astype('bool'), relay.shape_of(const_3422))) # shape=(10, 5, 11)
output = relay.Tuple([bop_3424,])
output2 = relay.Tuple([bop_3424,])
func_3434 = relay.Function([var_3423,], output)
mod['func_3434'] = func_3434
mod = relay.transform.InferType()(mod)
mutated_mod['func_3434'] = func_3434
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3435 = relay.var("var_3435", dtype = "int8", shape = (10, 5, 11))#candidate|3435|(10, 5, 11)|var|int8
func_3434_call = mutated_mod.get_global_var('func_3434')
call_3436 = func_3434_call(var_3435)
output = call_3436
func_3437 = relay.Function([var_3435], output)
mutated_mod['func_3437'] = func_3437
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3439 = relay.var("var_3439", dtype = "float32", shape = (13, 6, 7))#candidate|3439|(13, 6, 7)|var|float32
uop_3440 = relay.erf(var_3439.astype('float32')) # shape=(13, 6, 7)
var_3449 = relay.var("var_3449", dtype = "float32", shape = (13, 6, 7))#candidate|3449|(13, 6, 7)|var|float32
bop_3450 = relay.floor_mod(uop_3440.astype('float32'), relay.reshape(var_3449.astype('float32'), relay.shape_of(uop_3440))) # shape=(13, 6, 7)
func_3151_call = mod.get_global_var('func_3151')
func_3156_call = mutated_mod.get_global_var('func_3156')
var_3454 = relay.var("var_3454", dtype = "float32", shape = (700,))#candidate|3454|(700,)|var|float32
var_3455 = relay.var("var_3455", dtype = "int8", shape = ())#candidate|3455|()|var|int8
var_3456 = relay.var("var_3456", dtype = "float32", shape = (2400,))#candidate|3456|(2400,)|var|float32
call_3453 = relay.TupleGetItem(func_3151_call(relay.reshape(var_3454.astype('float32'), [5, 10, 14]), relay.reshape(var_3455.astype('int8'), []), relay.reshape(var_3456.astype('float32'), [2400,]), ), 0)
call_3457 = relay.TupleGetItem(func_3156_call(relay.reshape(var_3454.astype('float32'), [5, 10, 14]), relay.reshape(var_3455.astype('int8'), []), relay.reshape(var_3456.astype('float32'), [2400,]), ), 0)
output = relay.Tuple([bop_3450,call_3453,var_3454,var_3455,var_3456,])
output2 = relay.Tuple([bop_3450,call_3457,var_3454,var_3455,var_3456,])
func_3463 = relay.Function([var_3439,var_3449,var_3454,var_3455,var_3456,], output)
mod['func_3463'] = func_3463
mod = relay.transform.InferType()(mod)
mutated_mod['func_3463'] = func_3463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mutated_mod.get_global_var('func_3463')
var_3465 = relay.var("var_3465", dtype = "float32", shape = (13, 6, 7))#candidate|3465|(13, 6, 7)|var|float32
var_3466 = relay.var("var_3466", dtype = "float32", shape = (13, 6, 7))#candidate|3466|(13, 6, 7)|var|float32
var_3467 = relay.var("var_3467", dtype = "float32", shape = (700,))#candidate|3467|(700,)|var|float32
var_3468 = relay.var("var_3468", dtype = "int8", shape = ())#candidate|3468|()|var|int8
var_3469 = relay.var("var_3469", dtype = "float32", shape = (2400,))#candidate|3469|(2400,)|var|float32
call_3464 = func_3463_call(var_3465,var_3466,var_3467,var_3468,var_3469,)
output = call_3464
func_3470 = relay.Function([var_3465,var_3466,var_3467,var_3468,var_3469,], output)
mutated_mod['func_3470'] = func_3470
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3656 = relay.var("var_3656", dtype = "float64", shape = (13, 6, 5))#candidate|3656|(13, 6, 5)|var|float64
uop_3657 = relay.atan(var_3656.astype('float64')) # shape=(13, 6, 5)
func_708_call = mod.get_global_var('func_708')
func_712_call = mutated_mod.get_global_var('func_712')
const_3670 = relay.const([4,3,9,10,-10,-3,-10,-7,-2,-6,3,4,10,6,-6,8,-8,9,9,-9,10,3,2,-1,-10,5,-2,3,-2,-1,3,-8,10,-8,-7,-10,-8,-7,1,-7,4,6,-3,-2,-9,3,2,-1,-1,3,-6,4,-8,-6,-8,3,5,10,8,4], dtype = "uint64")#candidate|3670|(60,)|const|uint64
var_3671 = relay.var("var_3671", dtype = "uint32", shape = (63,))#candidate|3671|(63,)|var|uint32
call_3669 = relay.TupleGetItem(func_708_call(relay.reshape(const_3670.astype('uint64'), [12, 5, 1]), relay.reshape(var_3671.astype('uint32'), [7, 9]), ), 1)
call_3672 = relay.TupleGetItem(func_712_call(relay.reshape(const_3670.astype('uint64'), [12, 5, 1]), relay.reshape(var_3671.astype('uint32'), [7, 9]), ), 1)
uop_3685 = relay.sin(uop_3657.astype('float64')) # shape=(13, 6, 5)
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
var_3692 = relay.var("var_3692", dtype = "float32", shape = (2400,))#candidate|3692|(2400,)|var|float32
call_3691 = relay.TupleGetItem(func_2616_call(relay.reshape(var_3692.astype('float32'), [10, 15, 16]), relay.reshape(var_3692.astype('float32'), [10, 15, 16]), ), 0)
call_3693 = relay.TupleGetItem(func_2620_call(relay.reshape(var_3692.astype('float32'), [10, 15, 16]), relay.reshape(var_3692.astype('float32'), [10, 15, 16]), ), 0)
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
call_3699 = relay.TupleGetItem(func_2616_call(relay.reshape(call_3691.astype('float32'), [10, 15, 16]), relay.reshape(var_3692.astype('float32'), [10, 15, 16]), ), 0)
call_3700 = relay.TupleGetItem(func_2620_call(relay.reshape(call_3691.astype('float32'), [10, 15, 16]), relay.reshape(var_3692.astype('float32'), [10, 15, 16]), ), 0)
output = relay.Tuple([call_3669,const_3670,var_3671,uop_3685,call_3691,var_3692,call_3699,])
output2 = relay.Tuple([call_3672,const_3670,var_3671,uop_3685,call_3693,var_3692,call_3700,])
func_3701 = relay.Function([var_3656,var_3671,var_3692,], output)
mod['func_3701'] = func_3701
mod = relay.transform.InferType()(mod)
mutated_mod['func_3701'] = func_3701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3701_call = mutated_mod.get_global_var('func_3701')
var_3703 = relay.var("var_3703", dtype = "float64", shape = (13, 6, 5))#candidate|3703|(13, 6, 5)|var|float64
var_3704 = relay.var("var_3704", dtype = "uint32", shape = (63,))#candidate|3704|(63,)|var|uint32
var_3705 = relay.var("var_3705", dtype = "float32", shape = (2400,))#candidate|3705|(2400,)|var|float32
call_3702 = func_3701_call(var_3703,var_3704,var_3705,)
output = call_3702
func_3706 = relay.Function([var_3703,var_3704,var_3705,], output)
mutated_mod['func_3706'] = func_3706
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4058 = relay.var("var_4058", dtype = "float64", shape = (14, 8, 8))#candidate|4058|(14, 8, 8)|var|float64
uop_4059 = relay.asin(var_4058.astype('float64')) # shape=(14, 8, 8)
func_708_call = mod.get_global_var('func_708')
func_712_call = mutated_mod.get_global_var('func_712')
const_4068 = relay.const([[6,-7,-1,8,-2,-4,5,-8,-8,2,-3,8,6,-9,9,8,-1,-8,-9,4],[7,10,5,10,2,3,-2,5,6,8,1,-1,-1,7,-7,1,-10,5,-10,-9],[1,-8,-4,-9,-8,8,-5,4,-9,-5,-1,-2,1,8,-4,-8,10,-8,-8,7]], dtype = "uint64")#candidate|4068|(3, 20)|const|uint64
const_4069 = relay.const([[1,10,5,-2,1,4,-3,2,-7,4,-1,-10,9,-2,3,-2,-3,-10,2,9,-3,-9,-7,-4,-1,-8,7,-9,5,1,-1,-2,-5,3,4,1,7,8,2,8,10,8,-3,4,-2,8,9,-8,-2,-10,-2,-6,2,5,-5,7,-1,3,-4,4,3,9,-9]], dtype = "uint32")#candidate|4069|(1, 63)|const|uint32
call_4067 = relay.TupleGetItem(func_708_call(relay.reshape(const_4068.astype('uint64'), [12, 5, 1]), relay.reshape(const_4069.astype('uint32'), [7, 9]), ), 4)
call_4070 = relay.TupleGetItem(func_712_call(relay.reshape(const_4068.astype('uint64'), [12, 5, 1]), relay.reshape(const_4069.astype('uint32'), [7, 9]), ), 4)
func_3463_call = mod.get_global_var('func_3463')
func_3470_call = mutated_mod.get_global_var('func_3470')
const_4073 = relay.const([5.366938,6.812980,-0.735080,-1.185874,2.159636,-4.872707,-2.447919,2.793292,-7.248946,-4.822801,4.521396,-3.288126,2.263021,-5.547450,2.719454,3.831015,-9.543338,7.581081,-0.133043,3.178318,-4.246649,4.919669,-2.635327,-3.109876,-1.071633,1.008434,7.705748,-9.160159,-5.842482,8.770102,9.417088,1.876895,7.923851,7.133216,-5.899530,7.720047,-3.590085,2.542106,-1.723529,3.349774,-9.439679,-0.775824,-3.638916,-2.845625,-1.316352,6.043559,9.314691,5.180060,3.551876,-9.345626,9.328102,-3.626034,-3.998837,3.295353,6.705048,3.687881,4.479225,9.180544,-6.064510,-6.508665,9.403356,3.312587,-4.769067,9.001223,4.012550,3.958598,-1.024379,-5.845324,-7.983778,6.855703,-4.501362,8.421761,-4.652449,3.056464,6.390008,3.351244,3.449788,8.868204,-2.962897,-5.069287,-3.339264,-5.635193,1.299606,1.647288,-8.389566,-3.216679,-6.499550,-2.338632,-6.330915,9.070699,-4.310033,3.747959,9.369874,6.208472,7.773666,8.730071,-5.826436,-3.391620,-1.787935,1.126010,-0.292576,3.355974,4.318822,-3.752702,-2.634732,3.668628,-1.546054,-3.003858,9.676018,5.396111,3.862544,-6.565926,7.547992,-3.126322,8.761943,-4.190926,8.316018,-4.594911,-6.412498,-8.691023,-7.117727,9.372069,-5.257348,4.926626,5.224639,2.640622,5.532293,-9.843251,-3.051940,8.638634,-5.453242,-6.108200,6.048828,0.631832,6.078243,-0.624756,4.883150,-6.986751,-2.846681,-5.632490,2.422168,-7.828115,4.844589,8.270636,9.568399,0.656919,-4.765569,0.948222,-5.560309,5.689037,2.425929,-0.765760,0.835544,-9.088628,-7.081145,-2.415301,-4.733405,-0.721535,9.270435,-0.979396,-4.464762,2.455202,3.161600,1.724510,0.780207,2.601092,-5.260294,9.997191,-5.688590,1.746915,-9.029228,-4.827867,3.483092,9.530965,-7.144116,3.663738,8.801328,-0.505315,-4.618000,3.919412,-9.205188,-9.150194,-0.408736,8.509204,3.982568,1.187313,-5.979081,5.179363,-0.909701,-9.226975,-9.084296,-1.655144,-5.951233,-5.112418,-9.747791,-2.999390,-2.922712,5.104308,2.897227,1.240946,-4.842447,-6.128855,8.468017,-0.344205,-6.538764,-9.141323,-0.738145,8.713398,9.239511,3.841839,6.030143,3.846439,-3.731170,-7.267770,3.038093,5.014720,-0.388316,-5.302504,3.789095,8.636544,3.856170,-9.336726,-3.562883,6.960808,4.697704,6.691905,-8.037288,-3.488381,-4.349178,-0.078622,-4.417177,7.347929,-0.926855,-2.677501,-4.583103,8.354796,-2.465536,6.368772,3.909545,-8.544152,-6.189477,5.643394,-0.368602,9.707067,-5.112026,-1.363581,4.794399,5.459994,5.871416,9.700725,-9.178152,-5.527349,-0.938641,6.906650,-8.094052,-1.629061,-9.187796,3.310515,4.550420,6.238917,5.976238,1.343151,3.729172,-6.169629,-4.404956,-5.608249,-4.957545,5.839218,-3.133094,2.846391,8.835053,3.633110,0.227707,-9.105377,-6.560625,3.884100,-6.531586,-4.633512,4.095050,-7.317989,8.207947,-5.813052,8.625573,-6.706421,5.376371,-3.521726,-4.959428,-3.900160,2.067306,-7.646645,-7.609230,6.677669,-1.921924,-6.072658,-5.823146,-5.128053,8.621409,3.466737,-9.114466,-1.039020,0.062493,-9.351123,1.231468,-5.817221,-9.403852,-1.894210,-2.368217,6.859680,1.544735,-8.158161,-4.466524,3.002204,-1.102135,4.682975,1.726870,-5.377062,-3.405911,-5.245088,9.464336,-8.801373,0.085091,-6.620284,-6.699766,1.032419,2.200229,0.663234,-6.171493,9.672858,-1.114249,5.978081,-2.951498,-7.298995,8.137610,-8.496633,9.664797,-3.980291,5.047610,-1.933744,-5.093089,-2.277868,-9.495878,3.110376,-7.864302,6.046908,8.602398,-9.093953,-8.426306,5.451515,2.190188,-7.631511,-7.357078,-0.200661,2.313488,-4.231610,-6.074869,8.226925,-4.680258,3.435070,2.370691,1.063556,8.323569,-9.762627,3.717922,9.467350,-8.026121,1.412196,-0.274788,-2.560998,7.266461,0.702021,1.922127,-9.631534,-6.384932,5.818473,-1.416444,-0.887754,-0.742817,2.195173,-9.417712,0.983791,-8.049451,-2.260031,-2.201075,-8.407053,3.675336,0.082555,-0.916685,-8.909336,5.609827,-5.379674,6.114893,3.521903,4.331650,4.079557,-6.640835,-7.835818,2.117486,1.610532,-7.540692,9.453082,-1.199544,-9.461667,-3.016950,0.213228,-0.347522,9.756740,-8.080167,-4.223282,5.372089,-5.708531,-5.505382,-4.793374,7.466495,9.289672,1.569481,4.252237,4.786856,-3.122399,-3.455574,5.246816,7.483365,-9.306099,3.347092,-5.826879,-6.927548,-2.242846,5.392173,3.325041,9.689998,-1.227984,6.058574,-3.819789,-1.412245,2.826275,-0.079437,1.154747,4.452277,7.463428,-9.927306,-4.909644,-8.103864,0.863562,1.231733,-8.861224,2.783586,-8.320214,-4.577804,3.082336,4.000858,-5.153666,4.521772,-8.439949,8.610192,-7.989086,9.244142,1.820827,1.920406,3.850193,8.668035,5.791562,1.870919,0.445889,-2.360690,-5.136095,7.358394,3.599624,-6.050121,-4.534998,-8.474799,-0.457682,6.227304,4.073671,-9.021741,0.543258,8.836911,7.240406,-7.519178,-0.454000,8.354075,1.215930,6.300021,-0.585113,-5.474332,-9.468798,7.822352,-0.681591,-5.104119,3.593968,-9.408330,-2.732030,-9.326268,-8.201240,-6.365730,2.985596,2.844375,8.626068,-6.658193,5.860155,-1.572868,3.442044,-4.359288,-9.648789,8.680382,1.205365,-4.208685,7.349937,3.870208,-6.376163,0.346155,-1.330402,-2.411357,8.144797,6.353655,1.512170,-6.431560,2.868146,-8.617499,0.361211,3.911432,3.012790,-9.468105,-7.474269,6.355111,-6.585120,6.080331,3.383787,-8.053098,-7.277958,7.215578,5.973076,-3.334119,-7.019316,-2.099247,-7.872152,3.675866,7.079754,4.624754,3.648053,-8.456006,5.195893,-0.317092,7.757125,2.752066,-9.486231,4.262226,2.644536], dtype = "float32")#candidate|4073|(546,)|const|float32
var_4074 = relay.var("var_4074", dtype = "float32", shape = (700,))#candidate|4074|(700,)|var|float32
const_4075 = relay.const(7, dtype = "int8")#candidate|4075|()|const|int8
var_4076 = relay.var("var_4076", dtype = "float32", shape = (2400,))#candidate|4076|(2400,)|var|float32
call_4072 = relay.TupleGetItem(func_3463_call(relay.reshape(const_4073.astype('float32'), [13, 6, 7]), relay.reshape(const_4073.astype('float32'), [13, 6, 7]), relay.reshape(var_4074.astype('float32'), [700,]), relay.reshape(const_4075.astype('int8'), []), relay.reshape(var_4076.astype('float32'), [2400,]), ), 0)
call_4077 = relay.TupleGetItem(func_3470_call(relay.reshape(const_4073.astype('float32'), [13, 6, 7]), relay.reshape(const_4073.astype('float32'), [13, 6, 7]), relay.reshape(var_4074.astype('float32'), [700,]), relay.reshape(const_4075.astype('int8'), []), relay.reshape(var_4076.astype('float32'), [2400,]), ), 0)
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
call_4081 = func_286_call(relay.reshape(call_4067.astype('float64'), [6, 3, 4]))
call_4082 = func_286_call(relay.reshape(call_4067.astype('float64'), [6, 3, 4]))
output = relay.Tuple([uop_4059,call_4067,const_4068,const_4069,call_4072,const_4073,var_4074,const_4075,var_4076,call_4081,])
output2 = relay.Tuple([uop_4059,call_4070,const_4068,const_4069,call_4077,const_4073,var_4074,const_4075,var_4076,call_4082,])
func_4093 = relay.Function([var_4058,var_4074,var_4076,], output)
mod['func_4093'] = func_4093
mod = relay.transform.InferType()(mod)
var_4094 = relay.var("var_4094", dtype = "float64", shape = (14, 8, 8))#candidate|4094|(14, 8, 8)|var|float64
var_4095 = relay.var("var_4095", dtype = "float32", shape = (700,))#candidate|4095|(700,)|var|float32
var_4096 = relay.var("var_4096", dtype = "float32", shape = (2400,))#candidate|4096|(2400,)|var|float32
output = func_4093(var_4094,var_4095,var_4096,)
func_4097 = relay.Function([var_4094,var_4095,var_4096,], output)
mutated_mod['func_4097'] = func_4097
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4286 = relay.var("var_4286", dtype = "float32", shape = (7, 10, 9))#candidate|4286|(7, 10, 9)|var|float32
uop_4287 = relay.tan(var_4286.astype('float32')) # shape=(7, 10, 9)
output = relay.Tuple([uop_4287,])
output2 = relay.Tuple([uop_4287,])
func_4293 = relay.Function([var_4286,], output)
mod['func_4293'] = func_4293
mod = relay.transform.InferType()(mod)
mutated_mod['func_4293'] = func_4293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4294 = relay.var("var_4294", dtype = "float32", shape = (7, 10, 9))#candidate|4294|(7, 10, 9)|var|float32
func_4293_call = mutated_mod.get_global_var('func_4293')
call_4295 = func_4293_call(var_4294)
output = call_4295
func_4296 = relay.Function([var_4294], output)
mutated_mod['func_4296'] = func_4296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5182 = relay.var("var_5182", dtype = "float64", shape = (14, 5, 5))#candidate|5182|(14, 5, 5)|var|float64
uop_5183 = relay.sin(var_5182.astype('float64')) # shape=(14, 5, 5)
uop_5187 = relay.tan(uop_5183.astype('float32')) # shape=(14, 5, 5)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
const_5212 = relay.const([4,-2,1,9,1,-2,5,8,-8,6,-5,6,-3,8,10,1,-7,-9,4,-6,8,-2,5,-8,8,-9,-9,8,-3,-7,10,-9,10,-3,-7,-1,-7,10,4,5,4,-6,-10,-4,3,-7,9,9,-5,-8,-3,9,-4,2,-9,-2,2,5,-4,-6,-10,1,-1,3,-5,10,7,-6,8,-9,-6,1,10,-1,-7,-3,-9,10,-7,6,1,-9,-5,9,4,2,10,-9,1,5,6,9,-6,-3,-10,-4,5,9,-10,-5,8,-6,3,9,5,6,-5,7,1,-4,-9,4,-4,5,-3,8,-8,-4,-2,-6,8,-8,-6,4,-5,10,1,-9,9,8,-6,5,-3,-4,-1,-1,4,-4,6,-8,8,-8,-2,-5,3,-2,2,-3,-6,1,9,8,3,4,10,4,-7,-9,9,9,7,-1,9,-5,2,6,-8,-7,-6,2,-10,-6,-9,8,-10,2,-8,-8,8,6,1,-3,6,-10,10,8,10,-9,-10,-9,-3,10,5,-10,3,-4,8,3,-9,6,-7,-9,8,-4,-4,1,-3,9,-2,2,7,-10,-7,-8,-8,-8,-9,-9,-5,-7,5,4,-2,-7,-2,-10,9,3,-4,2,5,4,7,1,6,10,-8,1,-9,-2,9,1,1,4,7,7,6,-8,-5,-4,8,4,10,4,6,-2,10,-5,-7,8,2,8,7,2,4,4,-2,8,6,1,9,-8,-7,10,9,10,3,1,5,-1,9,-2,4,3,1,-1,-7,9,-10,-10,9,10,7,2,-7,10,10,7,2,-1,3,-5,-9,-4,7,7,3,8,1,3,-6,-3,7,-8,9,-1,-3,3,-3,2,1,6,7,6,-5,-5,2,-5,6,-7,5,7,6,-2,7,9,-1,3,-8,-7,10,5,-10,2,-6,-2,10,-8,9,7,4,-5,-10,7,9,-2,6,2,8,3,-4,-6,4,3,6,9,-6,6,-3,4,5,-3,-5,-10,-1,-8,7,1,10,3,2,5,-6,-3,-2,-3,7,1,-2,-7,-3,2,-1,-1,7,-6,-8,8,-1,-3,10,-1,3,-8,-2,-10,2,-3,4,-5,-8,9,-3,9,8,9,7,2,2,7,-7,-9,10,5,5,-5,2,-10,3,-8,-3,-8,7,-2,-1,4,-7,-8,-4,9,2,4,-9,8,-6,-2,3,9,1,-10,-2,4,-5,4,-7,1,-10,3,1,-1,8,-8,-5,-1,-10,-1,-3,-2,7,-10,-1,-4,-5,-10,8,5,-5,7,10,6,-8,4,4,-4,10,-7,-4,-3,10,5,-3,4,-3,-9,8,5,-4,9,-3,-1,6,7,1,-9,1,6,4,3,-10,2,-10,6,-8,-4,-10,7,4,-6,-1,-3,10,-8,1,4,6,9,-5,-1,-10,5,1,5,-3,10,9,10,-7,4,2,9,-3,5,3,-10,-3,4,4,-1,2,5], dtype = "int8")#candidate|5212|(550,)|const|int8
call_5211 = relay.TupleGetItem(func_3434_call(relay.reshape(const_5212.astype('int8'), [10, 5, 11])), 0)
call_5213 = relay.TupleGetItem(func_3437_call(relay.reshape(const_5212.astype('int8'), [10, 5, 11])), 0)
output = relay.Tuple([uop_5187,call_5211,const_5212,])
output2 = relay.Tuple([uop_5187,call_5213,const_5212,])
func_5215 = relay.Function([var_5182,], output)
mod['func_5215'] = func_5215
mod = relay.transform.InferType()(mod)
var_5216 = relay.var("var_5216", dtype = "float64", shape = (14, 5, 5))#candidate|5216|(14, 5, 5)|var|float64
output = func_5215(var_5216)
func_5217 = relay.Function([var_5216], output)
mutated_mod['func_5217'] = func_5217
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5720 = relay.var("var_5720", dtype = "float32", shape = (15, 1, 7))#candidate|5720|(15, 1, 7)|var|float32
uop_5721 = relay.sigmoid(var_5720.astype('float32')) # shape=(15, 1, 7)
uop_5723 = relay.sqrt(uop_5721.astype('float32')) # shape=(15, 1, 7)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
const_5751 = relay.const([[-0.183043,4.812658,4.217727,-3.503406,-0.883797,-1.856703,6.956642,-2.124448,-0.577435,-5.157691],[2.528124,-7.005541,6.158308,-3.347367,-5.807561,9.686439,0.208519,-5.041827,-5.086148,6.694557],[-3.570524,5.754379,-8.816774,-7.793838,7.918805,4.308292,8.269857,-8.390115,2.209052,4.224288],[-0.992555,-2.540358,7.737766,2.026318,3.588028,-8.734596,-4.274412,6.110003,8.825579,2.223155],[-7.070422,-9.812619,-6.458944,3.893244,6.680495,2.550381,8.555810,4.854681,0.087369,1.444839],[1.531576,-6.351163,8.558160,-2.810754,-6.015365,-9.101460,-7.131688,-6.130758,9.338666,1.511645],[-5.109561,-1.292620,-3.159550,5.477262,-7.980553,0.231988,-2.186164,9.530207,7.505087,8.853717],[1.720554,0.427591,-3.294947,9.015045,6.768137,-6.545771,4.130809,3.347053,-3.927217,1.586369],[2.066927,9.204108,9.925556,-3.157918,-2.034903,-7.056934,2.205954,-2.251841,7.625016,2.909745],[-2.416491,7.110454,-2.819757,4.808697,9.253560,-3.900178,3.532486,-2.639895,-4.379130,-3.542241],[-9.087479,2.482596,-6.905825,0.279442,2.038827,-7.325397,-0.006735,3.152339,-3.504882,-9.762560],[-8.346790,3.451597,-8.271041,-8.010111,-1.906071,9.188725,9.271137,-1.316357,-6.299581,0.117863],[-3.850390,2.645573,5.147806,5.127191,-2.135168,7.751710,-8.535588,-5.573016,3.026448,-1.237106],[4.674519,-9.413355,-1.294858,-3.885670,2.142709,-5.212946,8.025751,-7.688170,-2.313742,5.731852],[4.997617,1.862654,5.972665,-4.522164,-3.552435,-7.551094,5.609826,-0.728360,8.863068,-4.399605],[9.606356,-6.694145,6.372780,1.255806,-2.944033,-4.961260,-7.539063,-3.356091,5.573773,-2.987876],[8.851226,-0.325593,1.484406,-1.439087,1.808299,9.098408,5.373304,-8.121115,6.503921,-6.706509],[-3.207702,6.111442,1.522103,-2.118699,6.517702,-8.076021,9.436622,5.003001,-5.213395,9.970690],[-0.174036,-1.361541,-4.121999,-0.167997,-0.645264,1.567132,9.289000,8.233744,-2.872978,-4.944251],[-5.144064,-9.517168,3.639866,7.479723,2.204912,5.159527,2.449950,2.874563,-1.645709,6.543215],[0.573805,9.796918,-8.496116,1.665068,-0.189176,-5.143446,-2.152647,-3.043668,-1.611801,8.497955],[-0.605277,7.870861,-5.327879,2.530548,2.545754,-6.690989,-9.191540,8.344070,-4.002420,1.925514],[-1.970395,-3.831239,0.318792,-6.863035,-3.890208,4.885703,1.667638,-2.298693,-0.917809,-8.546252],[2.950053,-7.155511,9.658059,-6.385071,-5.184210,-7.620239,6.245146,4.951168,-5.105962,-9.392079],[-5.858092,1.294172,-4.067127,4.762409,-7.604177,-8.470813,-2.680129,8.885477,1.711373,-1.435086],[2.178049,-0.987716,6.284756,5.763680,-7.663332,-7.652525,-4.604461,-6.247391,0.836012,4.500799],[4.368837,6.605589,-0.772766,3.064518,-7.076991,0.516573,8.258814,-1.809008,2.941372,-7.572059],[8.160804,-1.105541,-4.558241,9.274083,1.652775,6.888301,-5.216465,-7.852650,3.909831,-2.624960],[3.587919,-2.618402,-4.648292,2.952131,-9.480548,1.072723,-3.585477,0.333622,-8.728264,7.901365],[1.360500,-1.494109,6.671601,-6.478705,9.289790,1.977890,-8.133936,5.894527,-7.937433,3.187976],[-6.291876,2.007697,-9.357215,3.126926,6.615025,-8.489295,-2.825837,-2.734832,-8.360955,-0.957004],[-9.404058,-9.570027,8.706234,6.112947,6.182610,4.314306,8.735312,-3.522077,4.444089,-9.036718],[-2.789800,-3.860928,0.237969,5.572625,5.762831,2.648175,3.829764,1.071179,7.725104,-0.401552],[7.233080,-9.674359,-2.188818,-3.133155,0.810827,-1.191641,-4.216377,-5.313808,-2.655390,1.872114],[5.568114,6.352719,-0.700198,-6.139551,5.193973,-6.061944,-2.062779,0.567015,-9.674757,-3.678517]], dtype = "float64")#candidate|5751|(35, 10)|const|float64
call_5750 = relay.TupleGetItem(func_5215_call(relay.reshape(const_5751.astype('float64'), [14, 5, 5])), 0)
call_5752 = relay.TupleGetItem(func_5217_call(relay.reshape(const_5751.astype('float64'), [14, 5, 5])), 0)
output = relay.Tuple([uop_5723,call_5750,const_5751,])
output2 = relay.Tuple([uop_5723,call_5752,const_5751,])
func_5753 = relay.Function([var_5720,], output)
mod['func_5753'] = func_5753
mod = relay.transform.InferType()(mod)
mutated_mod['func_5753'] = func_5753
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5754 = relay.var("var_5754", dtype = "float32", shape = (15, 1, 7))#candidate|5754|(15, 1, 7)|var|float32
func_5753_call = mutated_mod.get_global_var('func_5753')
call_5755 = func_5753_call(var_5754)
output = call_5755
func_5756 = relay.Function([var_5754], output)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5885 = relay.var("var_5885", dtype = "uint32", shape = (14, 16, 4))#candidate|5885|(14, 16, 4)|var|uint32
const_5886 = relay.const([[[-4,-4,6,2],[9,2,10,-1],[3,3,-8,-1],[-4,-7,-1,-10],[5,-1,-1,-3],[-8,2,-4,2],[-9,-3,6,1],[6,-8,10,2],[-1,-8,-10,3],[-7,6,10,-7],[5,-7,2,2],[-5,-7,-6,10],[-3,-2,-9,-9],[-1,-8,-2,-9],[4,7,1,6],[-10,1,-3,5]],[[-9,-7,3,-7],[-2,5,-1,-3],[10,1,-1,-9],[3,9,3,1],[1,4,-5,-10],[5,1,10,1],[5,-3,-2,-7],[2,-10,-10,-9],[-9,6,-4,-9],[2,7,5,3],[-1,-6,9,-7],[-9,-8,-7,1],[1,-10,-6,8],[-10,-1,2,-4],[-2,-7,2,-2],[2,-10,-10,-7]],[[-10,6,7,-3],[8,1,-10,6],[-3,-3,-6,8],[6,8,-10,-6],[9,4,7,-2],[-1,-6,8,-5],[4,8,4,9],[5,-5,-10,5],[3,7,7,5],[-2,3,3,-3],[-7,-7,8,-8],[-3,9,-3,5],[4,-8,-1,2],[-7,3,4,-7],[8,1,-1,-10],[3,-10,-4,6]],[[4,2,8,9],[1,-7,2,8],[-9,-8,8,-7],[-5,-9,1,-8],[9,2,-4,-5],[7,-1,-6,-8],[6,7,2,-4],[2,-8,9,8],[6,7,3,6],[-6,8,6,8],[2,7,-1,2],[6,-6,8,3],[6,-5,-4,8],[9,-1,-1,-8],[-4,6,-8,9],[-2,9,9,-5]],[[1,-3,-2,4],[-6,-8,-2,8],[1,-1,6,-3],[5,6,3,10],[-3,9,-3,-7],[-8,3,-1,-5],[-9,-3,4,-1],[7,4,1,4],[-6,-7,5,-7],[-1,2,5,6],[2,9,5,-7],[-7,2,7,-2],[-8,4,-5,6],[-3,-7,6,4],[-3,5,3,2],[-5,8,10,-6]],[[8,-4,1,8],[10,6,-1,3],[-3,3,10,-4],[10,8,-3,-8],[4,-6,4,3],[-1,10,-9,-7],[-1,6,6,8],[-5,5,3,-9],[-7,-6,-8,7],[-7,-3,-9,-9],[-1,-2,7,2],[-8,-8,-4,10],[3,-4,-4,-2],[7,-9,8,-7],[-1,7,-10,-9],[-9,1,-5,5]],[[-8,9,-10,-5],[8,3,10,-6],[-8,-10,-1,-9],[6,-4,-3,-7],[9,-5,6,-8],[-3,-10,-1,-5],[-9,-9,4,1],[-8,-10,-3,1],[2,-1,-5,-5],[-9,1,-1,-1],[5,-1,6,10],[-8,-4,-7,4],[-9,10,-5,-4],[1,-6,-4,-3],[5,-8,7,-6],[8,7,-2,-9]],[[-8,-7,-5,7],[6,8,-8,-1],[-6,-7,-8,-9],[10,-4,-9,-7],[3,9,-7,-3],[10,5,4,-3],[8,3,-3,-4],[8,-7,-2,-3],[-10,-2,7,-10],[-9,-4,-4,3],[-9,7,1,-6],[9,6,-10,8],[-1,7,-8,-6],[-3,-1,-9,8],[-3,9,6,2],[9,-9,-9,8]],[[-7,-10,3,3],[-6,4,9,3],[-9,-5,-8,-2],[-7,7,-10,-7],[-2,-4,-5,-3],[-9,8,9,9],[6,4,-1,2],[-1,-5,3,-10],[1,10,-10,6],[-9,9,-6,7],[4,-5,-10,-2],[-3,4,1,3],[-7,-9,-7,10],[1,-6,-10,10],[-6,7,-1,9],[-8,-2,-6,-4]],[[-9,1,9,-9],[-1,-1,8,2],[-6,2,-2,1],[-3,-10,9,3],[8,-3,-5,1],[-7,-6,-4,1],[-9,-5,-1,10],[3,-4,-7,-2],[8,4,-8,-1],[7,-2,-6,-1],[5,8,4,1],[-2,-2,9,-4],[9,-2,6,2],[1,-6,-8,-3],[-3,-8,-9,-8],[1,9,-4,-8]],[[-4,-10,4,-6],[7,-1,9,5],[-5,2,-1,6],[-10,3,-2,7],[-3,-8,10,-3],[8,-1,10,-8],[2,-10,10,-6],[-2,4,-1,-2],[1,-5,-6,9],[2,10,7,-6],[9,3,-1,10],[7,-9,-7,5],[3,-9,8,-2],[8,-4,-1,6],[-8,9,-8,-5],[3,3,5,9]],[[8,8,8,8],[-1,2,3,-9],[-9,-10,-7,1],[-9,1,-4,3],[-10,10,8,-3],[10,-2,-5,4],[1,-2,1,8],[2,5,2,10],[6,10,-9,6],[10,2,8,1],[2,-8,9,-4],[-7,-8,4,1],[-9,-5,-5,8],[8,1,8,5],[-7,4,9,6],[-4,3,2,9]],[[6,-2,4,4],[-9,-7,-7,8],[3,10,7,-6],[-2,-10,-4,6],[2,10,-7,7],[-9,5,-5,2],[3,10,9,5],[-8,6,4,1],[-9,10,-7,-3],[1,4,9,6],[9,-3,3,-10],[3,-2,-9,10],[5,-5,9,9],[-4,-6,3,6],[-7,2,7,2],[9,6,8,-5]],[[8,-5,8,6],[9,4,3,3],[10,-3,-7,-8],[8,2,10,9],[7,-6,8,-6],[4,-8,-1,9],[4,8,-7,-8],[10,3,9,-1],[-5,-1,9,-9],[-9,-9,8,2],[10,-5,-8,-3],[3,10,9,-8],[6,-7,-9,7],[-5,-8,6,9],[2,4,7,8],[-5,-3,10,9]]], dtype = "uint32")#candidate|5886|(14, 16, 4)|const|uint32
bop_5887 = relay.not_equal(var_5885.astype('bool'), relay.reshape(const_5886.astype('bool'), relay.shape_of(var_5885))) # shape=(14, 16, 4)
output = relay.Tuple([bop_5887,])
output2 = relay.Tuple([bop_5887,])
func_5891 = relay.Function([var_5885,], output)
mod['func_5891'] = func_5891
mod = relay.transform.InferType()(mod)
mutated_mod['func_5891'] = func_5891
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5892 = relay.var("var_5892", dtype = "uint32", shape = (14, 16, 4))#candidate|5892|(14, 16, 4)|var|uint32
func_5891_call = mutated_mod.get_global_var('func_5891')
call_5893 = func_5891_call(var_5892)
output = call_5893
func_5894 = relay.Function([var_5892], output)
mutated_mod['func_5894'] = func_5894
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6000 = relay.var("var_6000", dtype = "uint16", shape = (16, 4, 16))#candidate|6000|(16, 4, 16)|var|uint16
var_6001 = relay.var("var_6001", dtype = "uint16", shape = (16, 4, 16))#candidate|6001|(16, 4, 16)|var|uint16
bop_6002 = relay.greater(var_6000.astype('bool'), relay.reshape(var_6001.astype('bool'), relay.shape_of(var_6000))) # shape=(16, 4, 16)
func_4293_call = mod.get_global_var('func_4293')
func_4296_call = mutated_mod.get_global_var('func_4296')
var_6010 = relay.var("var_6010", dtype = "float32", shape = (70, 9))#candidate|6010|(70, 9)|var|float32
call_6009 = relay.TupleGetItem(func_4293_call(relay.reshape(var_6010.astype('float32'), [7, 10, 9])), 0)
call_6011 = relay.TupleGetItem(func_4296_call(relay.reshape(var_6010.astype('float32'), [7, 10, 9])), 0)
var_6012 = relay.var("var_6012", dtype = "bool", shape = (16, 4, 16))#candidate|6012|(16, 4, 16)|var|bool
bop_6013 = relay.less_equal(bop_6002.astype('bool'), relay.reshape(var_6012.astype('bool'), relay.shape_of(bop_6002))) # shape=(16, 4, 16)
bop_6032 = relay.floor_mod(var_6010.astype('float64'), relay.reshape(call_6009.astype('float64'), relay.shape_of(var_6010))) # shape=(70, 9)
bop_6035 = relay.floor_mod(var_6010.astype('float64'), relay.reshape(call_6011.astype('float64'), relay.shape_of(var_6010))) # shape=(70, 9)
uop_6039 = relay.atan(var_6001.astype('float64')) # shape=(16, 4, 16)
bop_6048 = relay.bitwise_and(uop_6039.astype('int8'), relay.reshape(var_6012.astype('int8'), relay.shape_of(uop_6039))) # shape=(16, 4, 16)
output = relay.Tuple([bop_6013,bop_6032,bop_6048,])
output2 = relay.Tuple([bop_6013,bop_6035,bop_6048,])
func_6067 = relay.Function([var_6000,var_6001,var_6010,var_6012,], output)
mod['func_6067'] = func_6067
mod = relay.transform.InferType()(mod)
mutated_mod['func_6067'] = func_6067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6067_call = mutated_mod.get_global_var('func_6067')
var_6069 = relay.var("var_6069", dtype = "uint16", shape = (16, 4, 16))#candidate|6069|(16, 4, 16)|var|uint16
var_6070 = relay.var("var_6070", dtype = "uint16", shape = (16, 4, 16))#candidate|6070|(16, 4, 16)|var|uint16
var_6071 = relay.var("var_6071", dtype = "float32", shape = (70, 9))#candidate|6071|(70, 9)|var|float32
var_6072 = relay.var("var_6072", dtype = "bool", shape = (16, 4, 16))#candidate|6072|(16, 4, 16)|var|bool
call_6068 = func_6067_call(var_6069,var_6070,var_6071,var_6072,)
output = call_6068
func_6073 = relay.Function([var_6069,var_6070,var_6071,var_6072,], output)
mutated_mod['func_6073'] = func_6073
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6550 = relay.const([[[7,-7,-5,-8,-10,-6,-8,8,-7,10],[2,10,6,-10,3,6,-7,-4,10,1],[-5,-9,-3,2,-9,1,2,3,-1,8],[-7,4,9,-6,-4,-3,3,1,8,-4],[-8,2,-6,-7,6,-1,-2,-8,-6,2],[-1,-8,6,10,5,-2,-1,-2,-7,-6],[-6,7,3,-9,-2,-9,-5,-9,6,-4],[7,5,-10,7,-8,10,9,2,-5,-2],[-9,1,-8,4,2,-9,5,7,1,-3],[-6,-4,2,-8,4,-5,-1,-8,7,-4],[-3,-7,7,4,-9,-8,1,1,-8,2],[9,9,-4,-8,9,9,5,10,2,-3],[-2,10,-4,9,-10,-6,-6,8,1,2],[-7,2,9,-7,10,3,-10,-5,4,6],[5,-4,8,3,-7,9,-6,-10,-5,-5]],[[5,-6,1,-9,5,10,9,3,7,7],[8,7,-7,10,-4,-8,5,5,-7,-4],[2,-4,-9,10,-10,-7,3,6,-3,-3],[-1,7,6,3,-6,8,10,-1,-9,-4],[-10,-9,9,2,-2,-8,-7,-1,6,-8],[3,-2,-6,-2,6,3,-9,8,10,9],[-6,-6,-3,-9,3,3,1,-8,8,3],[-8,-9,-1,-4,-6,2,1,8,5,4],[3,3,-1,-3,3,-3,2,-9,-9,-3],[-7,9,-3,3,-4,-5,2,-3,8,-4],[-1,3,8,-8,6,-4,-8,-2,-1,8],[-2,2,-8,-9,-10,7,-9,-7,-2,-6],[10,-1,2,-9,8,8,-10,-4,-5,7],[5,9,4,-10,2,-5,5,-9,9,2],[7,9,-10,6,-7,1,6,-3,5,-7]],[[9,-9,7,-3,-8,-8,-5,-10,2,-10],[-10,-9,2,-7,7,-6,-7,5,3,-4],[3,3,9,-2,-1,9,7,8,-4,-8],[2,-1,7,2,-4,-8,-8,-6,6,1],[-2,1,-10,1,-5,-5,1,5,-2,5],[-5,4,5,2,7,1,4,1,10,-8],[-8,-1,10,6,-4,9,-5,-3,-10,4],[-10,1,4,10,3,-10,-2,2,6,6],[-1,9,8,8,7,-7,6,3,-9,5],[-2,5,-3,-7,-6,-1,10,5,-2,-7],[-7,-7,2,5,4,3,3,9,-8,-9],[1,-3,9,-10,3,1,-2,4,-10,-7],[-9,10,10,-9,6,-3,7,-10,4,-9],[-9,-10,1,-7,5,7,4,-5,7,-5],[2,-9,-3,-7,-1,7,-7,3,1,2]],[[3,9,7,2,-7,-6,-4,-10,-6,-6],[-1,8,-8,-9,10,6,-9,9,-8,-9],[-9,-8,1,-9,-2,5,8,5,-4,-6],[6,-6,-8,2,-9,4,5,10,-7,3],[6,7,9,1,-6,8,10,6,10,-5],[-10,-6,9,1,6,7,1,-7,8,6],[6,6,7,-5,2,5,-1,7,6,7],[-3,6,-10,6,1,-2,5,7,1,-8],[-4,-7,5,-4,-3,5,-7,9,3,5],[-5,-3,4,2,-3,-10,-7,-9,-2,-3],[4,-10,10,8,5,9,10,-10,-3,-10],[5,3,-9,-4,7,-4,9,4,3,3],[5,8,6,-10,2,-5,-3,1,-3,3],[-4,1,-2,1,8,3,-5,-9,-1,-2],[-2,-2,-5,9,5,8,-8,3,5,-7]],[[-7,6,-3,5,-5,-7,-3,-4,-1,8],[4,7,4,-3,-3,2,1,4,-3,8],[-7,7,-5,10,-5,-1,-2,-10,-8,7],[-3,1,-5,8,5,7,2,-2,8,-10],[-10,-9,-1,1,2,-1,5,9,-9,9],[4,8,2,10,1,3,2,4,-3,-5],[10,-1,9,4,-8,6,9,-5,-1,2],[-6,-3,-9,4,-9,8,-4,-2,-9,-3],[-1,7,2,-10,-7,-4,7,1,-4,7],[-3,-3,-2,-10,-5,-7,3,-4,-8,-7],[-1,9,-10,-4,-7,-10,-8,7,-9,-2],[-1,9,-5,-6,-1,9,4,10,10,8],[6,8,-10,5,-2,-6,-6,-5,-1,-7],[4,4,5,3,9,3,-9,1,-3,-3],[-1,-6,-5,1,3,-8,-3,-6,8,4]],[[-1,3,5,3,10,3,-4,-10,1,7],[-9,-1,-7,3,-6,-3,3,9,9,5],[6,3,-6,-1,4,9,2,10,-8,-5],[9,1,3,9,10,3,2,9,9,-3],[9,10,3,-1,2,-5,-5,2,-6,3],[-5,-3,-2,-2,-4,4,8,-3,4,4],[-3,7,-7,9,10,-1,-8,-9,-9,-9],[-8,4,-7,-1,-4,-6,-7,-6,-10,10],[-7,-4,-7,3,-5,-9,-7,3,4,4],[-10,-7,-3,-1,-10,-4,4,-1,-2,7],[1,4,-10,2,10,2,-8,7,3,-4],[-9,-1,-8,-3,1,2,5,9,-3,-9],[-9,-3,1,-8,-7,9,-3,-10,5,3],[-1,-7,1,2,-9,8,-2,-4,-2,9],[-9,7,1,4,1,3,4,-10,5,10]],[[-3,-1,1,9,-10,-3,7,10,9,3],[1,4,5,2,-6,-6,-1,7,4,5],[4,-2,10,-10,-6,-1,-10,-6,-8,9],[-9,6,-1,1,-9,-9,4,8,5,-3],[3,-2,8,10,-4,-10,3,4,9,1],[-10,2,4,-8,-8,-2,4,5,-1,7],[-3,10,-5,2,-8,1,-5,-3,-1,-8],[3,-9,3,10,1,9,6,-2,2,2],[-8,1,6,-2,7,5,9,9,-9,6],[-6,-6,2,3,1,-7,10,2,-2,-2],[-4,8,-10,5,-6,1,-4,8,4,-4],[-9,-6,7,-5,-2,-7,-4,10,-4,5],[-6,5,5,9,-5,6,4,-2,-10,1],[6,10,4,3,-7,-9,-7,4,-6,-1],[6,6,9,-2,-7,-3,-2,2,-7,6]],[[-3,8,1,-4,-4,9,-2,1,-3,2],[-7,-4,10,-7,-8,2,1,-3,-1,-9],[-2,7,3,5,3,9,-2,1,8,-10],[4,-10,-3,7,-2,1,7,7,-7,10],[-2,2,-2,10,4,8,4,-2,3,-1],[8,-8,-9,8,9,-8,7,-9,-6,10],[-8,5,-8,-1,8,5,-3,2,-8,-9],[-6,-10,-10,5,5,-3,6,9,7,-5],[1,3,-1,-7,5,5,-5,-6,3,9],[7,-5,4,-6,-3,7,1,9,5,10],[-1,1,2,-9,1,5,3,-2,3,9],[-9,3,6,-1,-7,3,7,-4,-3,4],[-4,-1,-10,-4,-1,10,-9,9,4,-8],[-10,-8,5,4,4,10,-8,5,-4,-10],[3,-6,-4,8,4,6,5,8,6,7]],[[-3,-10,-8,8,7,8,9,-10,8,10],[4,-5,-2,10,-9,1,-4,3,-7,5],[-1,4,8,3,-2,7,1,-6,4,-10],[-2,5,4,-9,8,-7,-8,9,2,1],[6,-1,-9,7,-2,-6,-10,2,8,-4],[-7,5,1,1,-7,9,-2,8,7,7],[-6,6,6,9,1,-10,6,2,-9,-1],[7,10,10,5,7,9,-6,9,-4,6],[2,2,3,-5,8,1,-6,9,2,3],[5,-3,6,-3,-8,4,6,10,-1,-2],[-1,-6,-5,-10,8,-6,-5,2,-9,-2],[3,-9,-1,8,3,10,-2,-8,-1,6],[4,-2,1,2,8,-10,-9,10,7,-3],[8,4,-10,-9,-3,-2,-8,-7,8,-2],[-5,-9,-1,-6,7,-9,-3,-6,-5,7]],[[1,6,4,8,-7,8,3,8,-6,-2],[-6,-9,6,-3,10,3,-9,-1,-4,-5],[-1,3,-10,-8,7,-1,-5,-1,6,5],[6,-7,7,-8,-9,2,-5,2,7,-4],[-3,7,-7,-8,6,3,1,7,-10,-1],[-7,6,9,7,-9,-2,10,-10,-10,2],[-4,-8,-4,5,9,2,-8,-7,-6,4],[-7,-8,4,4,6,9,-10,7,1,10],[5,-7,-8,-1,-9,10,9,-1,-5,8],[10,3,4,5,-1,7,-5,-10,-9,9],[-4,-1,8,8,8,9,1,9,-2,-5],[9,9,-6,-9,8,2,9,-6,7,2],[-8,-3,-3,-8,-9,7,5,-2,-5,-6],[2,-6,1,-10,4,4,-5,2,-3,4],[-3,8,9,9,-4,6,4,9,-1,-6]],[[2,-8,-10,6,3,3,-3,4,-2,3],[-9,-4,-10,-10,9,-8,9,8,8,-5],[6,-9,-1,-8,-5,1,-1,-6,-5,3],[-6,6,9,-7,10,10,-9,4,1,3],[4,-9,-10,-7,5,10,3,7,4,10],[5,1,-8,-4,-6,6,-4,6,-2,-8],[4,-6,-5,-8,-8,-2,-8,-7,-7,-7],[9,-2,8,6,2,-5,-1,3,6,7],[-10,7,2,-4,6,-2,5,-9,-4,1],[8,-2,8,8,-7,-10,-4,4,-2,6],[10,-4,-4,7,9,-3,5,7,-3,9],[-10,6,3,-1,-8,4,7,-6,10,-8],[-3,-5,8,-4,-9,-10,10,-4,-8,10],[3,8,10,10,7,-1,9,-1,-10,-10],[5,-9,-6,10,9,1,-3,-10,1,5]],[[8,-10,-3,-7,-5,-3,5,-7,-6,-6],[-6,5,-6,-2,-6,4,-2,4,5,-10],[8,-1,7,5,-5,-8,-10,8,-9,10],[7,1,10,7,-7,-6,-2,8,-4,-3],[-6,8,4,-1,-6,8,6,-3,5,10],[6,-6,2,8,-9,-5,-3,-10,-8,-2],[1,-8,-1,3,-2,9,8,8,1,8],[-8,6,7,-10,6,-1,-2,-6,-1,-9],[4,1,-5,-4,5,-8,-6,-6,-10,-7],[-8,7,-7,-3,2,1,1,-7,-1,3],[-4,10,-5,10,5,-2,-6,-5,2,1],[-1,1,4,-6,-1,-10,-2,-5,-9,10],[2,6,-3,-1,10,-2,-6,-1,-10,-7],[10,6,-10,-6,-5,2,2,-5,1,-3],[-2,2,-7,10,1,-10,5,-10,-8,3]],[[-5,-1,2,-4,-6,4,2,-5,8,-6],[-5,10,2,-6,-8,-4,-3,-4,2,8],[4,5,-9,-5,-8,-7,-9,4,1,-4],[10,-6,4,7,-7,-4,-10,-9,9,-7],[-6,1,-5,7,-6,7,-6,6,2,-5],[-10,-9,8,-9,-1,8,-3,1,4,6],[-8,6,3,-3,7,3,9,-8,-10,-7],[-7,8,-4,10,8,7,-6,-9,5,5],[4,-1,-9,-1,8,-2,3,-5,-1,-4],[-8,7,4,-4,-10,2,6,-6,-2,8],[6,-5,1,7,-4,3,2,7,-5,-8],[9,-8,3,3,-10,-5,10,7,-1,-3],[3,-10,-7,-4,7,7,10,-2,9,8],[6,-6,-7,-8,-7,-5,9,7,2,8],[1,-7,1,6,7,-9,-1,-9,-10,-7]],[[10,-7,-9,6,-6,-3,2,-2,1,4],[3,-3,8,3,1,-5,3,-9,-8,6],[-1,-3,-8,7,4,-7,5,-3,4,-3],[5,-5,9,5,-10,1,9,-6,2,6],[3,5,5,-10,-4,-5,10,9,5,9],[4,-1,-6,8,8,-4,-9,-8,-6,5],[-3,9,10,5,4,5,3,-1,-10,-9],[-4,1,3,-10,-10,-1,3,6,-9,-1],[4,3,9,-8,-4,9,-3,1,-10,7],[4,-10,-9,2,-7,3,6,-9,-9,-6],[-6,-10,5,-5,2,2,-1,3,-9,7],[8,7,7,1,-5,-8,-3,-9,8,3],[7,6,-8,-9,-5,-4,8,9,9,9],[10,-4,6,1,-7,-5,-10,4,1,-6],[10,1,3,-3,-3,-8,-2,6,-6,-1]]], dtype = "int32")#candidate|6550|(14, 15, 10)|const|int32
const_6551 = relay.const([[[7,10,-7,9,-5,-2,-9,10,3,-4],[3,-7,4,-1,-7,2,-7,1,-3,-3],[-7,5,-5,8,1,4,-1,8,-6,-6],[5,7,4,5,8,8,-4,5,-7,7],[6,1,-4,-3,-7,-5,10,-4,10,4],[9,7,-2,-3,7,9,3,3,9,10],[-8,8,-7,-4,2,-8,7,-6,-10,-2],[-1,10,-10,-3,-8,5,-8,-4,5,-3],[-4,-10,6,2,5,3,-6,9,-4,5],[5,-8,2,7,9,-4,9,-6,10,-3],[5,-10,-6,4,-1,-4,10,-9,-7,8],[4,-1,-6,10,-6,-8,8,1,-6,8],[6,8,-7,6,3,9,8,4,6,9],[-8,4,-6,4,10,3,-5,1,8,-5],[3,-2,-2,4,-10,-2,9,-6,9,-7]],[[3,4,-9,-1,2,9,10,6,-6,1],[-1,-6,-1,5,4,10,2,-7,-8,-9],[4,6,9,-7,-2,3,-3,4,-3,3],[-9,-7,6,-3,10,-5,-9,-8,4,-5],[6,-10,1,3,10,-3,1,-9,4,1],[3,-10,-8,-3,6,1,-10,-10,-2,6],[1,1,9,-6,4,-7,-5,1,7,-8],[-6,4,-9,-8,7,10,-1,-7,3,-3],[3,5,-9,3,-2,9,-1,3,-7,-8],[-5,2,1,8,7,10,3,9,-2,8],[-5,-2,-7,-6,-8,-1,-5,8,-4,-10],[8,-2,7,-3,-6,-5,-5,9,3,-8],[-10,-5,2,2,10,9,-6,-10,-2,4],[-1,9,5,10,3,-3,7,-1,3,-6],[-5,-2,-6,4,3,-8,-6,-10,4,10]],[[-8,-4,3,5,-9,9,-8,7,-1,-3],[-10,1,-7,8,3,-3,-3,9,2,-1],[6,5,9,7,-4,8,-1,-9,-2,-2],[-6,-9,1,6,9,-4,-5,9,2,6],[8,9,3,-10,6,-1,8,-3,5,2],[-5,10,-5,6,7,-3,-5,8,10,-4],[-1,-1,4,-8,3,6,-6,10,5,1],[7,1,-4,-10,7,1,1,-9,-7,-6],[8,-10,6,10,-7,7,2,-6,5,1],[1,1,7,7,-8,-4,-4,-5,-4,4],[-5,-5,-9,3,8,5,9,1,8,8],[10,-4,-6,-7,-3,4,-3,5,2,3],[4,-9,-6,9,-8,-9,10,-3,4,9],[-2,-7,3,-7,2,5,10,8,-2,-9],[5,9,3,10,-5,-9,3,1,10,9]],[[10,7,-7,5,4,-2,-3,-2,6,-6],[-2,-5,10,1,6,1,5,7,3,-1],[-5,3,5,-6,9,9,8,-6,-4,10],[6,-7,7,1,5,8,9,1,9,5],[9,7,10,8,8,-5,7,-5,5,8],[-10,-3,8,-2,-1,-2,1,-10,5,-4],[-5,-9,-2,-9,-10,10,-1,-10,-6,5],[7,8,9,10,5,8,4,2,-2,4],[6,-4,6,-8,-4,8,10,-1,5,2],[-5,9,8,5,2,1,-3,7,-7,-10],[7,2,7,8,-5,1,3,-7,-9,2],[-2,-9,8,-2,2,7,3,7,-5,1],[5,7,-10,-10,7,-2,3,-3,9,7],[9,-9,3,2,10,5,-3,-5,7,4],[5,2,-9,-10,-10,10,-1,2,6,2]],[[-5,-3,-7,3,-4,-7,-5,9,-4,10],[8,-3,-8,2,9,2,-9,4,5,-2],[-6,-10,-10,5,-9,-7,-5,-5,7,9],[-1,10,7,-8,3,3,-10,2,-3,-5],[-2,-3,-5,1,6,-8,2,7,-3,-4],[-6,8,2,-8,-7,-1,-5,5,3,-4],[8,5,1,1,-8,4,2,10,4,-2],[10,7,8,-7,-7,-1,4,-5,10,1],[-1,-4,9,-10,1,-1,5,-6,1,5],[8,-5,2,9,7,1,-7,2,6,-6],[-2,-8,8,-2,-1,8,-1,-2,-6,4],[-3,1,10,3,-3,-5,-7,-6,8,3],[-2,-9,-8,7,-1,7,-6,1,2,-1],[4,-2,10,-7,5,-8,-3,-4,-7,2],[2,2,-8,3,1,-4,10,8,-5,8]],[[7,9,-4,-10,1,-1,-1,-10,-7,8],[-7,-3,-10,8,-7,5,4,-1,-6,9],[3,10,-4,5,-3,9,7,10,-4,3],[3,-3,-2,5,-7,5,6,-6,-8,-4],[-5,-3,-5,-8,-1,8,8,3,10,-10],[-4,-7,-10,3,-5,1,9,10,8,1],[-10,-3,2,2,4,9,7,-10,-10,-7],[1,-4,-3,-2,-4,-10,4,7,-9,-10],[-1,3,-4,4,-8,-8,8,-7,8,-2],[2,1,5,-4,6,-9,2,4,-7,-1],[-9,5,-2,-2,2,5,8,-2,3,-9],[-1,-6,2,-10,-10,5,-1,-9,-3,-5],[7,-2,5,7,-1,7,-5,-4,4,-10],[-2,-4,-7,8,-5,6,-5,4,2,8],[-8,-5,1,-3,-1,1,-8,-10,9,-5]],[[-3,8,-7,7,-6,5,3,8,-1,-9],[2,8,7,2,-6,-2,-8,-6,-3,-6],[-10,-2,3,7,8,8,7,9,4,10],[10,10,10,-3,-10,1,-2,-5,2,-10],[-9,2,4,10,5,-1,-9,3,8,-4],[6,2,-8,-6,-10,-3,-7,-5,-8,-1],[2,-10,-5,-2,-2,3,2,8,2,-2],[-4,-1,10,4,-8,3,-8,-3,-9,-6],[-1,-8,6,-3,-4,1,10,9,-8,1],[9,-6,-8,-2,3,-7,8,-7,3,-1],[7,-5,5,-8,-6,-9,-5,-3,-5,2],[-2,-4,4,3,5,4,-9,8,2,7],[7,6,4,-4,4,-8,-5,-7,8,-8],[-5,3,-3,7,9,7,1,-7,-3,-3],[9,3,8,4,-1,8,-7,9,-4,-7]],[[-2,10,-8,-8,1,9,-5,-3,4,10],[10,-1,-9,-8,7,-5,-10,2,-5,10],[-2,-4,-9,3,-6,9,8,-4,-10,-9],[6,8,10,-5,-10,1,-1,-10,-3,6],[-5,5,6,-2,2,5,-7,5,3,-4],[-4,-7,-1,-5,-2,-4,-7,2,-10,10],[-8,-9,10,-4,-3,-7,5,-2,-3,-1],[-10,-1,5,10,8,9,-9,-2,-2,5],[7,4,8,-8,-5,-5,5,-3,9,-8],[-5,4,-5,4,-3,7,-3,-1,7,9],[10,8,-9,-6,4,7,10,5,8,-5],[10,-10,-10,-1,10,-2,5,-6,1,-5],[7,-4,3,-2,-9,-9,-8,-2,-10,7],[5,2,1,6,-9,5,-5,3,-10,-9],[2,10,9,-8,4,-10,-7,1,-8,10]],[[-10,-3,5,2,-1,-4,9,4,-5,6],[10,-10,-8,-4,10,6,-10,4,7,1],[-7,2,1,5,-8,7,6,-4,-10,3],[-4,-1,-1,10,-3,5,-5,7,3,-4],[-2,9,-10,-6,-3,2,9,-2,2,-8],[2,-6,-10,-5,-6,4,-9,8,5,-2],[5,8,1,4,-3,-8,-6,3,7,1],[-6,1,-9,7,-5,4,4,3,1,7],[-2,8,1,-3,1,4,-10,-5,6,-3],[-2,2,-9,9,4,4,5,3,-7,-4],[2,-8,-3,-1,6,1,-1,3,-7,9],[-2,-9,-7,1,-3,-2,3,7,-2,6],[-2,-7,-7,2,3,-7,-4,-2,-1,5],[-9,8,5,-9,-6,7,9,3,-4,-4],[-8,-4,9,5,8,-5,5,9,3,-8]],[[-3,8,-1,-10,8,4,4,8,1,-5],[-3,5,6,-7,2,-7,-2,-6,6,8],[9,7,9,1,1,10,-6,2,-9,-10],[-6,-5,-10,9,-7,9,10,-1,3,2],[8,10,9,8,2,-8,-5,-7,3,2],[-7,-6,-6,8,1,-5,-2,-4,6,-8],[10,-9,10,-3,-1,5,-7,-5,-9,2],[2,8,-2,-4,4,9,9,-10,-1,6],[-9,2,-1,9,-1,-10,10,-7,-10,-3],[7,10,-9,7,-5,-5,-1,10,-5,3],[-10,9,3,-4,-10,-9,8,-3,2,-8],[2,-1,10,6,-10,1,4,-2,7,9],[-5,-2,-10,2,4,8,3,10,1,-1],[7,-3,-2,-7,2,-4,-4,10,3,5],[1,-3,3,10,-1,6,-10,8,-5,1]],[[-1,-4,3,-1,7,-6,-7,7,-4,3],[7,-5,8,1,8,-1,-8,6,-3,10],[10,2,-6,-9,-5,6,-4,9,4,-5],[3,-1,-5,4,3,9,1,5,10,8],[8,5,6,-4,-3,3,9,7,-3,3],[7,1,5,7,-10,1,8,-2,10,-5],[6,-1,5,8,-10,-6,-5,9,5,-5],[9,-4,2,3,1,6,-7,-2,-6,-10],[3,5,5,8,-8,-6,9,-7,-6,-2],[8,6,-5,-6,3,9,-6,-6,6,2],[8,-4,7,-5,-2,4,5,5,-10,-2],[9,-9,-6,7,-10,10,6,-5,5,-8],[7,7,1,5,-3,4,-10,8,-9,-10],[3,-7,3,-1,-1,5,10,3,4,-3],[-5,-10,10,-1,-2,-10,-10,-1,10,-9]],[[-1,-1,8,10,-2,-8,10,3,5,-10],[4,1,8,7,6,-7,2,-5,1,-10],[-10,9,-6,1,6,-10,1,6,-5,-5],[9,-7,-1,-1,2,5,-2,2,-9,-1],[4,7,5,3,6,-3,10,-6,-2,3],[-10,6,7,10,-2,-2,4,-10,-5,-1],[2,8,1,3,2,-9,-8,-2,6,-2],[-5,-5,-4,-8,-9,-1,-10,-3,2,-8],[5,7,-6,-10,-3,9,7,-6,10,-1],[2,9,1,-7,-1,-9,4,-10,7,1],[4,-7,-5,-1,7,-3,4,-3,6,-7],[-2,-3,-4,-7,7,-10,-9,10,-2,-8],[-5,-9,4,3,9,9,8,-10,-9,3],[6,-4,2,8,7,4,8,10,-3,-6],[-4,-6,8,-5,4,2,-3,4,2,-3]],[[7,-10,1,8,2,-8,8,-1,9,-3],[5,-2,2,8,-7,5,-6,-8,-7,-3],[-10,-7,5,5,3,-9,-3,-9,-7,1],[5,8,2,-10,-4,-10,-4,-1,5,2],[-3,-8,-2,-3,3,-10,1,2,4,4],[5,-2,-3,5,-8,7,8,10,-4,8],[7,6,6,3,1,9,5,4,-4,-7],[-8,6,10,5,-10,-1,-10,7,6,5],[-1,-3,6,4,6,4,6,9,7,1],[-6,-6,-1,10,5,7,2,4,-9,7],[8,9,-1,-1,2,-6,4,3,-5,7],[10,7,5,-9,-10,8,-10,-3,5,9],[-3,6,-7,5,1,3,5,3,-1,-2],[3,-10,-9,3,-4,3,-7,7,7,-7],[3,10,-2,-7,9,6,3,4,7,-8]],[[-8,-10,-10,-3,8,-5,-2,10,10,-8],[9,1,-8,-4,2,7,4,7,6,-3],[1,-7,5,-6,-3,3,6,3,-1,-2],[10,-3,7,-10,-1,7,-1,5,-2,-10],[-3,8,-9,7,8,2,-7,2,-6,-8],[5,1,2,1,-4,8,6,-9,6,4],[3,2,1,-7,6,6,-1,-7,-10,6],[1,-3,9,-1,-8,-7,-1,3,4,-8],[5,2,-2,10,9,-8,-9,9,-3,-1],[5,3,8,7,6,-4,3,7,-7,7],[-3,10,8,-10,-10,-3,10,3,2,1],[9,-8,-1,8,-4,-8,2,8,7,-10],[-8,4,-8,7,-8,7,4,-10,10,5],[-2,10,-8,1,-8,-2,3,6,2,-1],[-10,8,4,8,-5,-10,5,1,10,-1]]], dtype = "int32")#candidate|6551|(14, 15, 10)|const|int32
bop_6552 = relay.bitwise_and(const_6550.astype('int32'), relay.reshape(const_6551.astype('int32'), relay.shape_of(const_6550))) # shape=(14, 15, 10)
bop_6555 = relay.logical_and(bop_6552.astype('bool'), relay.reshape(const_6551.astype('bool'), relay.shape_of(bop_6552))) # shape=(14, 15, 10)
uop_6575 = relay.asinh(const_6550.astype('float32')) # shape=(14, 15, 10)
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
const_6578 = relay.const([-3.329086,-8.027400,0.378070,8.462376,-6.257767,-3.970898,-1.498896,3.636477,5.466298,2.942573,-1.101293,-4.681264,8.433104,0.806298,-0.174391,5.557459,-3.257020,-6.506344,2.250235,2.344850,-5.227329,-3.478879,-2.428016,4.485409,-2.551102,4.443052,6.065642,6.355844,7.454104,7.857054,-3.231236,-3.723989,-4.884875,-0.989629,-5.406109,-4.303789,2.183417,6.790352,-2.511634,-8.407761,3.285226,-4.731826,6.426819,2.891928,-6.246832,-4.185562,-1.261490,1.280556,9.142033,-7.158001,1.665259,-4.464455,9.387476,5.241342,-8.243860,-7.746106,8.237315,-9.961348,5.617920,6.273671,-0.151044,-6.901899,-4.873926,-3.044228,9.312881,-4.124131,8.565109,0.862199,-5.353862,-3.543445,-7.100947,3.538917,9.187152,-3.393360,6.987219,-9.090294,9.249881,-1.123415,2.772278,5.136914,9.691202,7.465427,-7.254527,9.792820,6.176805,-6.972621,7.435992,-5.687691,5.008432,5.234746,-2.466973,3.016565,-4.436943,-3.279380,-1.526765,-2.245101,5.179109,-6.206310,-7.982782,-3.804393,5.500300,-4.915039,-6.000330,-3.541669,4.073490,9.852714,1.248503,-6.517618,-3.322109,9.201257,-6.104814,7.424348,-9.650198,-4.339379,7.873950,-6.884945,2.205794,4.776296,4.417956,1.107036,0.388223,5.139666,1.372534,-7.254667,-3.605098,-4.550642,2.653477,-2.089749,6.265440,9.537773,6.019431,-9.413922,-6.803635,5.185032,6.204883,-3.893402,2.412397,3.045179,8.105636,-3.521045,-0.309717,6.357340,-7.738752,4.007197,-9.970542,6.814214,-2.394434,-3.142009,5.235481,1.459317,-5.092183,-0.879783,3.032132,7.491960,5.064271,-5.216176,-2.001442,-7.893297,3.131363,7.253051,-2.849363,5.459016,-7.458672,6.933664,9.171082,-0.281302,-3.595930,1.737825,-5.710190,8.013603,0.139335,7.604624,5.058845,-8.909143,7.475750,-6.654386,-4.383634,5.103358,2.449844,6.700403,4.133308,-0.583794,-4.493825,5.248387,-3.761056,-5.290267,-9.631847,-8.420958,6.745164,-7.705930,-9.918342,-4.630834,-1.710498,9.491673,-3.607237,8.218736,-1.045902,-4.375428,5.629203,5.915178,-8.222530,1.018661,-3.718311,-5.060611,9.594015,-8.734273,6.478472,-8.181791,-9.112858,2.136614,-7.399140,-4.694566,-9.976192,9.776054,-6.268065,-6.892506,4.837775,1.302361,4.512487,5.599112,-2.394849,-0.769591,9.338144,-6.114415,-4.577786,-4.938289,-9.053893,4.275170,3.365350,-9.705295,7.282609,-4.168907,6.119509,-4.232876,0.212438,1.385861,-1.834245,3.932583,-3.056287,5.239283,9.719168,-3.355942,8.191589,8.157523,-4.152248,-7.700333,-5.278343,-9.293049,7.708102,-8.833787,0.349617,-2.793482,7.561914,5.685021,3.451889,-5.529598,-2.608475,-9.893291,-7.073931,5.627968,-6.487423,-9.584001,-8.695757,-6.184887,-5.406266,9.304848,-8.897827,2.634338,7.545908,6.888044,0.655055,-4.613613,-7.125727,8.185529,-0.865278,-1.760108,6.228398,1.083824,7.311247,3.518320,-6.131696,3.511986,-6.016204,-1.227268,0.290549,2.863598,0.215412,1.927486,-1.670302,-5.987391,6.244938,7.091025,4.193118,-9.554538,-0.280855,-5.656531,-8.757217,1.409387,-2.541428,8.830183,-0.943233,2.654239,-9.540464,2.479536,2.334505,3.808779,-7.132314,8.777155,8.698870,0.437562,8.132464,-3.310487,4.540209,5.542685,9.886654,-6.357265,4.875776,5.009931,-0.409687,-3.477071,-9.022190,-9.053266,1.751148,-0.289940,3.562482,-0.185681,-4.446815,7.108730,2.004289,1.044414,9.203808,-0.300788,9.914648,-3.845354,-3.742796,-4.036794,-9.480477,-1.097631,-7.986115,-2.772899,-3.463703,9.072524,8.583057,-5.797505,8.870939,0.338597,8.716986,2.930501,2.628809,-4.430543,-3.574043,-1.466082,6.532445,-0.664765,2.588766,-3.896307,-2.690943,-9.860235,-3.247390,-1.487197,2.859019,-7.030418,8.798910,5.633856,3.597285,-4.859666,-5.077858,-8.524874,4.206409,-5.652252,8.156241,-7.114425,-2.671884,1.553260,-5.076539,-5.008081,9.934255,-7.086331,-8.972517,7.265919,-5.354890,5.687251,-1.874493,-3.830426,5.123496,-0.964107,1.401599,-0.967506,-3.049107,-8.562859,6.982023,-3.486974,5.570303,5.886824,-2.108834,4.611260,-7.605096,-8.105114,-5.287513,2.073404,8.844869,-8.825581,-4.747685,-4.007381,-3.440599,2.803472,4.776109,-1.917462,3.056860,-0.047036,-0.938915,-2.162623,-9.005848,2.380963,3.846193,-8.627724,0.221051,-5.824798,1.535132,-6.513210,5.583550,1.216394,1.398872,-1.649892,8.206844,-8.619691,-2.041509,3.473314,9.210417,-5.898818,6.018582,5.288130,3.684773,-5.191142,-5.852189,3.247927,6.957152,-1.028641,-6.620656,7.999838,0.274949,-1.501650,-0.500666,6.872603,-8.723346,-8.471387,-7.593833,-2.852442,8.991964,8.521756,5.163234,-3.221926,1.657638,6.688334,4.148001,-0.065752,0.293638,-2.467244,-4.033707,2.015988,8.637462,-2.655056,-6.365972,-7.356778,9.473380,1.609303,-9.808750,2.071541,2.597053,4.018958,7.202980,8.233789,-1.140313,-1.202996,7.360920,-4.616386,-3.803375,2.797823,9.283530,-2.624032,8.481632,-7.777165,6.307866,6.475670,-4.379708,0.593130,-6.616180,-2.038296,7.031181,0.088630,1.086102,1.289457,-3.611926,-1.522278,-4.962805,0.461585,-5.739016,0.259352,7.850679,-7.520361,-3.226662,-1.779162,5.843847,9.664085,8.031582,8.676585,-9.219772,-0.206480,2.294754,0.442569,-0.865382,5.253044,-6.233350,-4.197657,-3.111058,2.209015,7.820139,3.734749,4.529267,9.427190,-8.144356,7.349514,8.298303,0.951596,-4.274372,6.193509,0.753957,3.322128,2.175796,-4.072456,3.571382,-0.864854,7.872480,1.980383,0.223967,6.598552,2.601126,-5.707781,6.557403,-1.205887,-2.312342,-2.054681,-4.194958,3.650124,7.591161,9.970421,-0.421142,2.022724,-9.828648,-3.717965,2.799867,0.437114,-5.406052,-5.582183,2.102317,1.759506,-9.524124,-9.604994,9.982405,-4.676296,4.239465,9.489036,-5.367082,5.410710,5.391993,-3.746881,8.724828,-3.167208,9.256270,2.787835,6.298487,3.809656,-6.025500,-2.875529,4.556462,0.724544,0.569033,-3.094289,9.231480,-0.267613,0.789277,-0.442908,-5.799796,-6.786952,5.258018,-7.907426,-5.799094,-3.932587,7.110476,3.584505,6.786102,8.495131,6.557984,-1.746013,7.695877,-8.831924,6.198721,-9.166276,0.755352,-7.912472,-3.401382,1.805364,-3.526478,-6.463905,-8.799602,-3.563097,-9.035242,-1.636172,-2.895435,-1.118013,0.619243,-4.247095,7.203510,-4.678570,-9.612315,9.352089,-7.060070,1.783874,-0.308445,-8.517456,9.783344,0.982367,0.973113,-3.836729,-0.227360,2.668975,9.139124,2.768107,-5.078828,9.811559,-0.268150,-0.035505,4.906077,4.414503,6.709258,-3.106849,-9.308734,-8.080227,-8.702528,3.087790,7.544257,-6.513330,7.281842,-1.314118,-1.937057,-9.625185,-5.535919,1.916646,-7.737529,-0.144988,-8.372642,9.254976,-2.508511,-3.383522,-1.761351,3.300116,1.778948,-0.873258,3.086288,-8.749777,-2.476232,-2.086111,0.255595,-2.090944,-0.972608,0.747432,0.230305,-6.379596,-9.815334,-5.946473,-9.105037,3.235539,-7.540834,-0.320604,-4.964019,7.306422,1.502155,5.865345,0.366418,0.776479,-9.099994,-4.699129,4.036315,0.445860,-4.713967,-2.744173,-1.522109,-0.862663,0.584607,-1.199407,7.509364,-1.924044,-4.661392,-7.894851,7.568235,3.403600,-1.295271,3.104474,-8.663450,-6.652263,9.850217,-2.991680,-6.388443,-8.189129,0.559168,8.344206,-5.019133,-7.356798,0.252784,-7.843161,-9.672483,9.246940,9.818314,-5.533895,4.883761,-0.577034,0.272230,-1.418942,8.632501,2.507925,-8.334526,-4.770093,-8.518335,3.798276,9.588024,-5.727505,8.067220,-2.303554,-4.311849,2.641710,0.326776,-8.178967,-9.565038,-5.967919,1.516775,-4.742352,-8.409879,-7.381988,6.055020,9.753775,3.412851,-4.438100,5.633303,-4.620241,2.140566,8.328612,3.965415,1.415718,6.406577,-3.910638,0.952587,-9.631742,4.992301,-6.484010,-4.360700,7.652204,9.276381,-1.104592,-8.171237,2.921349,-3.911058,9.278187,-1.972827,8.046718,-0.465909,9.273519,8.437829,-3.675134,-2.149738,2.720565,-3.245374,7.237830,6.254068,-9.358579,-5.207452,1.272766,-3.976869,-3.882923,-1.681294,-6.668622,2.950694,-0.817612,3.161799,7.702484,-8.357072,-4.905394,9.663695,-0.162678,-3.366595,0.205087,-1.460765,3.665655,2.523667,-0.483618,-3.646074,-9.175894,-2.504586,-2.826851,1.274663,4.202098,-3.145893,-4.481683,8.410380,-8.297753,7.725776,-5.758706,6.153079,2.712550,-7.228988,-6.464577,-3.515622,-4.911380,5.474008,6.911755,0.823837,-4.790738,-2.778940,6.376805,-1.973256,2.207235,0.766011,3.152605,-1.373822,9.177648,-5.312724,3.173261,6.051092,9.447656,-9.633536,3.422750,-4.827016,4.294664,5.457249,-5.590304,0.471790,6.518304,-0.131585,9.773991,9.721792,7.889618,-8.211891,6.191200,-0.004277,-7.289712,8.685186,-5.287244,-2.711087,-2.741431,6.705122,5.676799,7.184988,8.066722,3.164349,-1.667856,-0.301957,0.437164,-9.038403,-1.797929,4.582553,7.148881,-7.209226,-1.938011,3.326794,-4.278837,-9.645886,7.904280,6.046987,4.591060,2.955580,5.660323,5.826020,-7.546651,0.179428,-3.327546,-3.465972,4.351283,-8.870552,2.411898,6.336210,-2.249850,3.164050,5.601854,-0.965234,0.636282,-0.113045,2.142720,8.368041,5.028218,-2.764412,-2.462761,1.893688,-8.846613,6.258995,6.422356,9.064541,-1.908464,-0.304609,3.781899,-6.184092,-1.419626,-9.327674,-5.974158,-9.819142,-8.682999,-2.624392,2.840354,8.846335,5.580080,4.918697,7.772929,-2.089596,0.776528,1.254943,7.046032,4.371978,-2.575864,-1.153528,-8.754183,-6.629732,9.950072,2.380941,-8.135243,-8.970704,5.086598,-5.988503,8.853645,9.069864,6.346830,6.561433,-0.506633,5.376848,-8.564646,-0.010941,-6.467934,-9.281258,8.054405,-4.419580,-6.894176,8.330786,-0.605423,-5.583008,-8.440593,-0.201076,-2.382016,-0.624476,-3.146586,1.579233,6.850538,3.734031,-7.447216,-2.254171,8.118767,7.747369,9.112659,-6.084746,-2.719022,3.883956,-2.533176,6.106601,-6.963452,9.622761,3.529988,4.517970,-3.287439,-0.275873,-2.189022,-3.352405,3.656529,4.228065,-6.133017,-0.415681,-4.110188,7.964902,9.839727,4.288838,2.309831,-9.524158,3.062676,1.574279,3.663795,-4.952025,-0.654243,0.639066,-4.294503,1.905901,-6.236235,-8.738151,2.101871,4.876736,-2.817983,-3.051976,-7.985641,-5.598813,9.442532,9.649201,0.765448,-5.933140,5.491524,6.063729,8.890514,-3.976770,-7.700022,-7.968688,4.162247,-8.697389,7.061085,5.604098,2.359561,4.343140,0.556923,5.640940,7.013087,8.589727,-3.882447,-7.343853,8.733119,6.686343,7.376897,1.635381,-5.294229,-5.686479,2.460774,8.706674,3.207092,8.908061,0.844395,4.608798,-3.233846,3.545612,6.787742,-2.955895,5.785339,-3.225633,-2.889666,0.236503,2.733709,-6.267940,3.049987,-1.375983,-2.432259,5.059929,-7.140396,-0.832217,2.654509,3.109662,-9.202314,0.630191,-5.436705,-0.323600,-8.315137,4.791746,-1.904212,-7.685425,1.380135,-0.968572,-4.946281,8.026109,7.541970,2.190735,-0.311791,0.893585,2.092086,-4.266475,2.052228,-8.607998,-4.584796,1.090650,6.878354,-2.004367,-9.611165,-5.411811,-3.752325,-9.207861,-5.404763,9.751629,-3.295512,0.076867,9.735336,4.189913,-2.368800,-6.269646,6.742879,6.951596,7.054087,7.603087,9.735208,-4.105980,-6.181475,6.737207,1.621882,1.188169,0.459465,3.117164,-5.827168,0.255727,-2.690501,6.842478,-4.436051,-3.641770,-7.023020,0.591341,7.558533,5.908857,-8.433123,-6.864441,5.891913,-3.542131,-7.367175,-1.288808,-4.674979,-5.839258,6.601435,4.316676,-9.701398,-8.521626,9.760002,-8.335088,9.122571,-4.946335,-3.897726,5.884453,-4.214166,8.954171,9.536708,7.199050,4.584520,-6.528064,8.730605,-4.347319,6.134145,-7.283649,8.222219,-3.674437,0.517630,-3.322176,5.857412,0.255307,9.734734,7.073615,-4.743131,1.629673,-6.234092,9.929597,7.696781,8.231620,-0.012514,8.661338,4.696347,-5.972161,0.739160,-9.997540,6.959699,-6.065611,-3.652002,5.726548,2.800777,2.065489,4.957549,7.001155,-8.634150,2.638838,6.687265,-7.439840,-1.896824,6.642682,-8.945078,8.662134,2.622967,-0.207206,5.104808,1.113977,-8.511084,-5.896259,5.498776,-0.985658,-8.019603,-9.087925,3.686081,-5.245175,9.716355,5.112980,-7.236885,8.711321,-3.842162,2.116010,-2.345526,-5.535606,5.361716,-3.006644,8.269439,5.957971,-3.836135,1.157354,-8.796273,-3.725135,9.283693,6.869857,-7.961772,3.958893,6.371391,-4.160343,8.900109,-5.760069,4.409609,0.155535,-5.172676,-3.848085,-7.681981,-8.570976,-5.461402,6.361217,-8.730963,1.482399,5.178591,9.506276,6.341039,-0.195744,8.922080,-9.139244,9.383782,2.426176,-5.872551,4.819069,2.962974,5.524203,-7.698135,8.274734,-8.755794,2.777339,7.373994,-6.258664,-4.374851,-4.488404,5.394430,-0.843988,-7.166340,-3.455079,1.022342,-3.498553,1.049918,-3.849222,-6.829277,-5.638089,-2.517153,-5.852401,9.436729,9.263609,-5.185510,8.092054,-8.199136,-6.283502,5.224460,3.177062,-7.371670,8.395530,8.689325,1.516750,1.280587,-5.644568,5.425684,9.983229,7.687350,-9.253664,-4.454813,-2.252174,7.636552,-1.685861,3.477333,-5.053937,5.892562,-9.923055,4.889062,-2.091677,5.440119,1.070152,4.446797,0.226265,7.861461,-3.517899,9.586377,-2.071308,-3.696954,1.944523,-1.591071,5.587280,7.734386,-2.625943,-8.665813,4.465203,-9.234551,-4.411799,-9.821316,-8.048339,-5.645459,9.142692,2.524600,-9.422526,-1.703998,-4.581355,0.308192,-7.697555,9.936781,-0.041508,8.874264,2.888859,-9.903062,-2.875283,-3.422095,-2.915549,2.031116,-8.616491,1.502610,-2.858826,2.994445,-1.849151,1.335433,8.670060,7.894885,-7.022300,-5.073443,-3.040498,1.498239,0.616288,-9.621655,-3.111450,5.647000,-6.423845,-5.459679,3.389034,6.706268,-9.339397,-3.286297,0.067610,2.279982,7.120889,-1.972197,-3.837558,-9.857035,5.606085,9.035380,-0.748898,-1.114893,2.713357,-6.999348,-8.535432,-8.390223,-5.789965,5.375775,0.188045,0.678904,-8.898459,-7.850850,8.891683,-4.149301,0.790547,8.346372,-9.399474,4.100455,-4.608871,-8.490941,3.933694,7.917157,-1.052729,-1.556509,-9.002445,-2.842133,3.125731,2.381379,6.323089,0.639006,-4.402381,-2.751923,-9.820805,-3.399594,7.906609,-3.743862,-0.924639,-0.167823,-9.460289,-7.364969,-1.095404,3.492160,5.602675,3.687714,-6.232752,-4.496585,7.393837,3.501063,-1.134165,-1.124595,4.311735,-1.296800,-7.208931,-3.776743,3.650842,1.114036,0.635616,4.288651,-3.280424,2.720308,4.632052,7.618883,-3.267820,7.756909,-7.862079,9.592691,-5.645729,0.523088,-3.737521,7.215388,-9.778877,-3.727385,1.760808,5.606943,-7.248472,-7.012396,-5.178720,-7.528904,-4.408189,5.127146,1.243696,-1.752213,-4.708372,-7.692043,1.681731,1.747189,5.582031,9.893273,9.384111,-3.524028,3.177268,-5.013927,-4.008231,1.520095,-7.326220,5.177162,8.309099,2.267842,-5.577268,-1.221840,7.336607,6.803556,5.445353,1.110504,0.356287,-6.988862,-5.719526,-6.047579,2.448651,2.424066,-5.845149,5.415863,5.865149,-3.059417,0.332284,7.805950,-4.388013,4.342222,-9.765978,-2.766801,-9.144787,-3.117565,9.149662,7.070475,-2.152648,-6.643996,3.932914,-2.504637,-7.847786,-8.117400,-6.969336,-4.333342,1.073376,-2.598360,-4.464833,5.504031,-5.067335,4.740589,2.407688,-4.949552,-6.248738,-9.366490,1.703762,-5.498725,1.470663,4.985255,-9.093037,-5.145147,6.567651,8.393000,-5.406429,-9.447896,8.175907,-9.819067,-8.597896,-0.624796,-8.969434,-4.133509,-4.780468,3.457852,-4.322927,7.720077,2.519276,-7.310721,-2.024772,-5.476005,-7.783928,0.145700,6.898216,-2.288462,4.669582,-3.121345,-9.379152,7.978701,7.016354,-0.343938,9.751738,-3.898244,-9.313414,9.803789,5.039884,9.292753,-4.831612,0.804614,-6.347399,8.423595,-3.593021,1.349482,-2.674059,0.317291,-1.411418,9.056386,9.646479,-7.740071,-6.890095,6.226878,2.611103,-7.982657,6.818887,0.160489,6.894415,5.194182,-0.379805,-1.124189,0.588811,-2.499698,-1.435497,6.133458,-1.294811,9.236660,1.520989,-4.862780,4.067129,-5.819119,-0.981051,-2.881346,-5.955857,0.784493,1.721184,-4.010925,-7.182425,-3.982911,-9.377062,-2.050193,5.400831,-7.392895,-5.156301,2.432281,1.982963,4.561105,-8.722212,3.175196,3.368644,2.833755,1.351159,-8.031885,1.399137,-3.182171,-0.088158,-2.983362,-7.877942,1.439099,0.372981,-4.336491,-8.757912,-1.220397,6.357352,-4.327046,-0.321607,9.365959,6.396383,6.730920,-9.638550,-9.949173,9.644219,-8.280461,4.200266,-9.161109,5.525910,3.228146,-8.008788,-2.283836,-7.018332,7.298022,-2.709825,-7.315939,-3.510734,-2.535235,9.858181,5.661086,2.477889,-4.202843,1.839816,0.195001,3.109022,6.238285,-2.764799,6.721900,-3.827884,-2.061450,-7.021297,-7.994445,-1.943729,8.431968,3.262135,-9.248316,4.581187,-6.305218,-2.178623,6.064797,-1.956217,3.013106,-2.470428,4.556167,4.817491,0.679051,-3.973914,-1.151381,1.228403,-2.134039,3.574345,2.298272,2.937272,3.338815,-3.694049,7.252689,0.355696,6.415945,-0.467957,-2.440865,-6.127277,1.063578,0.305507,-2.119629,9.738552,-3.883311,5.135421,2.579354,6.408298,-6.057539,9.988286,-5.364006,7.911968,-2.083629,1.558549,9.417652,0.003132,-8.565192,1.684469,5.069686,-7.152032,7.954008,9.606000,-4.362883,6.741371,-2.539248,8.736735,-6.839432,0.448694,-0.315099,1.796210,-3.670408,-8.826989,-6.971436,9.398841,-7.408552,7.317980,-3.837066,7.923229,8.199778,4.761596,8.830976,-4.821789,7.848311,9.846113,-5.413790,-9.076336,4.356872,-1.054802,-4.995787,4.235704,1.063991,-2.225386,5.853718,-7.240987,-0.333073,4.745153,-7.443658,5.521266,3.437642,7.766137,-8.301195,-2.288273,-3.021645,7.379711,0.055950,-1.767036,8.466702,-4.378042,-0.933027,2.813403,-5.120590,-1.537734,-5.901242,9.122295,-3.153351,-7.207065,-4.899852,-6.239017,7.725987,4.771368,-4.440594,5.474539,-9.668327,3.352891,-7.784170,9.313270,2.324374,-7.284893,-7.087838,9.678495,-8.042694,9.119955,-0.647211,-1.337287,9.877823,-3.400493,6.095121,0.145787,8.296213,-0.047235,0.351685,5.254825,0.088125,-8.128799,4.361387,9.560683,0.656201,-8.580969,-3.573314,7.059910,-5.295678,-2.526029,8.846867,2.429619,-6.725076,0.102754,8.225060,-7.273408,-2.926666,-4.877696,-4.464861,8.607113,-9.389645,0.658651,-5.870769,-3.492653,9.090262,-6.615908,-5.729040,2.837663,7.581260,-8.428211,9.177475,-8.611650,-8.877127,0.772529,-9.667032,-4.885174,-0.043212,2.854622,1.401820,9.747096,-3.646082,5.275696,7.035310,5.139123,8.272450,-4.437246,-4.493668,-7.155040,9.806525,7.770434,2.388307,1.537297,-3.153829,-6.865634,-0.624616,-3.783479,-3.274705,-3.911640,-2.009509,-1.374801,1.770633,2.994360,0.150305,-3.813354,0.541642,-6.553582,-1.565842,3.172433,6.778718,-0.903766,0.616368,-5.422006,-0.209947,-6.191409,4.982043,6.086095,2.668369,-3.967427,-9.293680,4.121141,6.928064,-9.319443,8.940843,-1.735387,-5.487783,6.493766,5.826281,4.844999,-6.948013,-7.120418,-1.684045,-2.825470,-6.718674,6.318702,-0.135177,5.420151,-9.404093,0.850881,4.291840,-9.838701,-9.595204,9.743069,-6.114034,7.411456,-0.403197,-0.627973,4.186866,-1.187676,4.333981,2.484904,1.925985,0.924965,-5.497648,8.779433,-5.592021,8.104255,3.570439,-1.912658,6.657139,-3.052015,-4.167095,5.296236,-7.893096,0.942391,1.942893,5.818097,3.342555,-6.793289,9.566315,0.002697,-1.879871,-8.478676,-5.084339,0.090350,-5.552433,9.776488,-9.713424,1.637951,9.056365,-4.026110,8.836530,2.599865,4.915778,-5.814056,7.265433,-9.628614,3.384916,-1.463525,-1.706577,8.356801,8.370984,3.755897,3.277565,-4.175650,1.973512,2.301917,-6.900698,-9.623833,6.887367,-1.297505,-7.653085,-1.097356,7.891079,7.653595,-0.737990,3.868100,-7.946132,3.197640,2.072128,-9.630714,-2.325731,9.507766,-7.840713,-8.141196,-6.103235,-8.615353,-5.990184,-4.368682,6.459072,7.010739,8.802900,-3.925755,2.166368,9.053699,1.476030,9.394145,-2.976306,8.696943,-1.878565,-8.411302,-7.739304,-9.426707,9.165335,9.966314,-3.584837,-0.708096,9.078123,1.518326,-9.395264,0.030342,-3.992509,7.949459,1.176054,1.646835,3.616455,-5.464973,5.236229,-4.326804,-7.954234,8.543805,-5.929507,-1.374271,-9.082836,-2.950829,-8.568746,4.217403,-7.231676,5.549253,4.469742,-9.371391,-7.941774,-4.717493,5.024833,-0.086455,-5.784721,-7.884986,7.955304,-7.202407,9.932620,-0.969898,-4.453494,-1.555392,2.076900,-8.263238,7.328155,1.177649,-2.868268,5.567050,-0.262240,3.919333,6.949895,8.429396,-3.020917,5.785567,-3.289421,9.386289,8.815005,2.789823,-4.045472,3.947470,-4.972051,8.919132,-2.711216,-7.125938,7.068033,-8.370808,-4.109139,7.777593,8.150147,-5.347609,9.202356,9.845318,4.088751,0.973886,-2.095248,8.040500,6.289922,2.087920,5.750640,-1.494638,1.385930,-7.321760,-2.743440,-6.389777,-4.054279,6.027823,2.706868,-7.346440,8.378423,-1.505787,-9.876734,5.882864,-4.797999,5.556956,-2.530739,-7.544061,-6.037414,9.379456,7.459748,2.260066,-1.316210,9.275918,0.720550,8.172879,4.812056,-5.255165,5.522380,3.953196,6.501852,-0.107572,-9.305797,6.334091,6.582497,0.658405,3.321480,-1.594030,9.038855,5.658617,2.553170,1.511408,-3.829302,-7.582594,5.128143,4.320089,-7.894254,7.415859,6.131501,-8.093609,7.405380,6.067316,-8.246542,2.911347,3.409038,-2.633003,5.895899,0.152392,8.849228,8.103575,1.718299,5.289640,-4.699091,-9.691480,-9.245969,-7.520658,-1.438663,-8.894342,6.391081,-2.250863,-2.321255,1.284657,-3.310899,7.961712,-5.570600,3.709333,8.510481,-6.630718,4.002358,8.923304,6.246692,1.395788,2.348297,-6.798210,3.172201,9.555157,3.311675,1.172079,2.497177,6.251930,-6.226057,0.450605,-3.613444,6.262254,-4.924139,9.098189,4.476635,6.820410,-3.963394,0.045259,-3.880372,1.379790,-4.941026,-0.096572,1.463823,1.076965,-7.202350,5.285364,-8.454434,-5.032781,-6.675530,-0.346665,-4.078491,-8.876122,6.675100,9.051694,4.340679,1.516028,9.197465,1.928561,-9.262457,-5.299695,-5.828711,7.008424,6.470212,4.756605,2.277362,2.534824,-7.416387,-7.663919,1.301874,3.749959,-3.813646,-2.293562,-0.183372,-3.076457,0.624542,9.962658,-5.875075,-3.301563,-1.658758,6.956071,-0.675593,-3.983343,4.322520,-7.809116,-5.872417,2.693308,7.503685,-9.445655,3.963300,-2.758611,-6.591943,-6.440503,-3.344976,-2.452643,2.006598,-3.739028,-8.442673,-9.367036,1.432921,-0.430216,-1.374429,-2.805124,-0.439037,-9.598600,5.869440,-0.636022,-0.772338,-8.947075,4.160684,-1.850154,3.608432,-2.907226,8.045916,6.284697,-2.501609,-9.782131,0.215223,-7.736195,0.433072,3.469206,9.499696,-8.273983,6.802265,-1.792815,5.911308,3.628748,3.648491,-9.943559,-4.320561,2.002209,-6.783813,3.951210,-0.767298,3.729928,-0.168995,-2.776652,-0.019341,-9.600748,0.597391,-5.771710,3.906233,4.968924,-2.632108,3.342181,3.983009,7.595500,-6.249585,5.578001,-7.195340,-6.233325,-2.213489,-1.810370,-4.593129,-9.505157,7.386529,-5.754077,-4.094342,2.149700,-5.393573,4.844254,8.306091,5.992808,0.442307,-5.933194,4.404784,4.826458,5.132934,-8.809465,-7.866347,4.315924,5.794401,-7.223736,-5.007157,-2.829078,-9.262091,-7.876514,-7.890407,5.658242,1.254969,4.349153,-2.236985,-0.231935,-5.492231,3.858775,4.221642,-3.622439,6.931883,-2.060251,-2.824055,-5.111473,-0.853271,-1.344986,-1.129079,-4.328253,8.323591,-5.619934,-1.039582,6.518157,9.128104,8.421362,-7.453968,6.847650,-4.528029,3.279371,2.077836,8.759675,-9.696844,-8.921567,4.401473,-3.672451,7.042217,5.135744,6.847376,-4.967560,6.571889,2.110255,-7.989710,6.954538,-7.434276,9.109447,-5.574567,0.493733,9.528452,7.572594,2.463453,2.308906,-4.300178,-0.109106,-8.183105,-8.364135,5.627391,1.293823,1.987917,-3.579950,4.699879,1.610593,4.436424,-5.453816,-7.732568,4.925236,-2.200320,-2.950083,5.402961,-1.199699,-3.557087,-5.127685,7.461965,9.376645,-1.545267,-4.387884,3.410154,-3.798614,7.863073,1.053776,-9.335882,3.472187,-5.168056,-0.826247,-0.995178,3.553818,5.399671,-4.757797,4.323391,6.832297,-6.997266,7.152810,5.005820,-8.357051,-0.212244,6.055356,-6.271186,3.374792,-6.844217,3.690055,3.799964,7.346997,-5.364542,3.529236,5.389816,6.338213,-4.588673,-6.667362,-0.061887,-1.058303,-0.831687,-4.192785,-6.122371,0.684449,3.915591,-9.548450,2.726946,8.194618,8.215579,7.900140,-9.487066,-7.263858,1.670181,-2.343269,2.549173,0.233264,-1.699746,2.596975,3.542833,-2.943426,3.903471,7.893260,-2.564492,-4.255141,9.729974,4.908904,-9.966382,1.190077,-4.711029,-5.289517,-8.879604,2.959068,8.230185], dtype = "float32")#candidate|6578|(2400,)|const|float32
call_6577 = relay.TupleGetItem(func_2616_call(relay.reshape(const_6578.astype('float32'), [10, 15, 16]), relay.reshape(const_6578.astype('float32'), [10, 15, 16]), ), 0)
call_6579 = relay.TupleGetItem(func_2620_call(relay.reshape(const_6578.astype('float32'), [10, 15, 16]), relay.reshape(const_6578.astype('float32'), [10, 15, 16]), ), 0)
uop_6587 = relay.cosh(uop_6575.astype('float32')) # shape=(14, 15, 10)
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
var_6590 = relay.var("var_6590", dtype = "float64", shape = (72,))#candidate|6590|(72,)|var|float64
call_6589 = func_286_call(relay.reshape(var_6590.astype('float64'), [6, 3, 4]))
call_6591 = func_286_call(relay.reshape(var_6590.astype('float64'), [6, 3, 4]))
func_5753_call = mod.get_global_var('func_5753')
func_5756_call = mutated_mod.get_global_var('func_5756')
var_6595 = relay.var("var_6595", dtype = "float32", shape = (105,))#candidate|6595|(105,)|var|float32
call_6594 = relay.TupleGetItem(func_5753_call(relay.reshape(var_6595.astype('float32'), [15, 1, 7])), 1)
call_6596 = relay.TupleGetItem(func_5756_call(relay.reshape(var_6595.astype('float32'), [15, 1, 7])), 1)
bop_6598 = relay.greater(uop_6575.astype('bool'), relay.reshape(uop_6587.astype('bool'), relay.shape_of(uop_6575))) # shape=(14, 15, 10)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
call_6612 = relay.TupleGetItem(func_5215_call(relay.reshape(call_6594.astype('float64'), [14, 5, 5])), 1)
call_6613 = relay.TupleGetItem(func_5217_call(relay.reshape(call_6594.astype('float64'), [14, 5, 5])), 1)
output = relay.Tuple([bop_6555,call_6577,const_6578,call_6589,var_6590,call_6594,var_6595,bop_6598,call_6612,])
output2 = relay.Tuple([bop_6555,call_6579,const_6578,call_6591,var_6590,call_6596,var_6595,bop_6598,call_6613,])
func_6634 = relay.Function([var_6590,var_6595,], output)
mod['func_6634'] = func_6634
mod = relay.transform.InferType()(mod)
mutated_mod['func_6634'] = func_6634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6634_call = mutated_mod.get_global_var('func_6634')
var_6636 = relay.var("var_6636", dtype = "float64", shape = (72,))#candidate|6636|(72,)|var|float64
var_6637 = relay.var("var_6637", dtype = "float32", shape = (105,))#candidate|6637|(105,)|var|float32
call_6635 = func_6634_call(var_6636,var_6637,)
output = call_6635
func_6638 = relay.Function([var_6636,var_6637,], output)
mutated_mod['func_6638'] = func_6638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6800 = relay.var("var_6800", dtype = "float64", shape = (5, 5, 10))#candidate|6800|(5, 5, 10)|var|float64
uop_6801 = relay.erf(var_6800.astype('float64')) # shape=(5, 5, 10)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
var_6804 = relay.var("var_6804", dtype = "int8", shape = (550,))#candidate|6804|(550,)|var|int8
call_6803 = relay.TupleGetItem(func_3434_call(relay.reshape(var_6804.astype('int8'), [10, 5, 11])), 0)
call_6805 = relay.TupleGetItem(func_3437_call(relay.reshape(var_6804.astype('int8'), [10, 5, 11])), 0)
bop_6809 = relay.floor_mod(var_6800.astype('float64'), relay.reshape(uop_6801.astype('float64'), relay.shape_of(var_6800))) # shape=(5, 5, 10)
output = relay.Tuple([call_6803,var_6804,bop_6809,])
output2 = relay.Tuple([call_6805,var_6804,bop_6809,])
func_6813 = relay.Function([var_6800,var_6804,], output)
mod['func_6813'] = func_6813
mod = relay.transform.InferType()(mod)
var_6814 = relay.var("var_6814", dtype = "float64", shape = (5, 5, 10))#candidate|6814|(5, 5, 10)|var|float64
var_6815 = relay.var("var_6815", dtype = "int8", shape = (550,))#candidate|6815|(550,)|var|int8
output = func_6813(var_6814,var_6815,)
func_6816 = relay.Function([var_6814,var_6815,], output)
mutated_mod['func_6816'] = func_6816
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6911 = relay.var("var_6911", dtype = "float64", shape = ())#candidate|6911|()|var|float64
var_6912 = relay.var("var_6912", dtype = "float64", shape = (11, 1, 9))#candidate|6912|(11, 1, 9)|var|float64
bop_6913 = relay.mod(var_6911.astype('float64'), var_6912.astype('float64')) # shape=(11, 1, 9)
bop_6921 = relay.logical_or(var_6912.astype('bool'), var_6911.astype('bool')) # shape=(11, 1, 9)
var_6926 = relay.var("var_6926", dtype = "bool", shape = (11, 5, 9))#candidate|6926|(11, 5, 9)|var|bool
bop_6927 = relay.add(bop_6921.astype('uint64'), var_6926.astype('uint64')) # shape=(11, 5, 9)
output = relay.Tuple([bop_6913,bop_6927,])
output2 = relay.Tuple([bop_6913,bop_6927,])
func_6945 = relay.Function([var_6911,var_6912,var_6926,], output)
mod['func_6945'] = func_6945
mod = relay.transform.InferType()(mod)
var_6946 = relay.var("var_6946", dtype = "float64", shape = ())#candidate|6946|()|var|float64
var_6947 = relay.var("var_6947", dtype = "float64", shape = (11, 1, 9))#candidate|6947|(11, 1, 9)|var|float64
var_6948 = relay.var("var_6948", dtype = "bool", shape = (11, 5, 9))#candidate|6948|(11, 5, 9)|var|bool
output = func_6945(var_6946,var_6947,var_6948,)
func_6949 = relay.Function([var_6946,var_6947,var_6948,], output)
mutated_mod['func_6949'] = func_6949
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8364 = relay.var("var_8364", dtype = "int16", shape = (15, 1, 6))#candidate|8364|(15, 1, 6)|var|int16
const_8365 = relay.const([[[7,3,-5,-6,-2,-7],[-9,-10,9,-5,-8,-5],[4,3,2,7,3,5],[-3,-8,-10,-8,2,-10],[-1,-9,9,-4,-3,2],[10,7,1,1,6,9],[-6,7,-6,-10,1,6],[3,-3,-6,4,-8,9],[-4,3,2,6,-10,10],[9,5,-9,-9,8,9],[-1,-9,-3,-8,9,-8],[5,10,6,-3,10,-6],[8,9,9,1,-2,-9]],[[-7,3,8,6,5,9],[8,8,-2,4,10,-8],[-5,1,9,2,6,-3],[-9,8,-7,-9,10,2],[2,2,3,-10,-8,4],[2,-3,-5,3,-7,2],[-9,-10,8,1,-10,-1],[2,9,-4,-7,-1,5],[9,2,8,-2,2,-5],[4,10,8,4,3,-10],[-8,-3,9,7,-5,-4],[2,9,-7,-6,-10,-4],[-6,-8,4,7,-5,3]],[[8,4,8,6,5,5],[2,3,-8,2,-5,-4],[-8,-3,1,9,-7,-1],[-10,-6,-4,6,-2,10],[4,-5,-2,-10,-10,-5],[8,-8,-6,1,-8,10],[-7,8,5,-3,-7,10],[7,-2,-2,8,3,-6],[-9,-7,-3,6,5,-1],[-1,-9,-3,8,8,9],[-8,-1,-4,-4,-1,9],[9,-6,-1,-7,3,1],[-5,-6,-10,3,3,-1]],[[-1,2,-5,8,10,10],[-10,4,-3,9,-5,-10],[-1,4,-9,1,-1,3],[-5,2,4,-7,-9,10],[-7,9,-6,-8,6,-1],[9,6,-4,-6,10,4],[-9,10,1,1,9,-1],[-1,-3,1,3,-5,-9],[-7,-10,2,1,-5,1],[-9,6,-2,-4,-6,-1],[1,6,-4,5,-2,6],[-8,-7,-8,-1,-1,-6],[5,-8,-8,-7,-7,-5]],[[10,2,-6,5,-5,-9],[3,1,-8,-8,8,-4],[-9,5,8,6,-9,-9],[7,9,10,-7,7,-6],[-3,-9,-2,-7,-8,6],[-10,3,9,2,-7,7],[8,-10,-2,-3,-3,-5],[-7,-8,5,-10,-6,-6],[-6,10,1,3,-3,-4],[9,9,-10,-9,-9,4],[10,-10,-9,-1,7,10],[-1,7,6,-7,1,-9],[10,-9,-6,4,-9,4]],[[3,2,-9,7,-7,-3],[6,-10,-6,7,8,7],[-9,3,5,5,-5,7],[-3,-5,9,-3,-8,1],[1,-1,3,6,9,9],[9,4,-3,9,7,6],[1,-10,-10,4,10,2],[-5,7,-8,-8,2,-2],[-2,3,-4,-7,6,-6],[10,-10,7,-4,-2,4],[7,6,3,4,-8,7],[6,7,-1,10,4,2],[6,2,8,8,10,-5]],[[-4,10,-8,4,-3,7],[5,-7,-1,-8,8,-3],[-8,2,-6,2,-7,-2],[1,10,6,-10,-7,9],[8,5,1,-2,10,8],[-10,6,5,4,-3,-2],[4,-1,8,10,-1,-4],[4,1,10,10,2,-9],[5,2,10,6,-7,4],[6,3,-1,-10,-3,-7],[-2,2,4,-2,-5,-6],[10,8,8,3,7,3],[-5,1,6,2,6,4]],[[7,10,2,-6,5,-2],[-7,-8,2,-2,-4,4],[2,8,2,-1,-9,3],[-6,-6,5,5,2,8],[-3,-1,-5,7,-3,-9],[-10,-5,1,2,7,8],[5,-3,7,1,2,-8],[-8,-6,1,-7,-6,-10],[10,-4,-10,-8,8,-4],[-3,-4,8,3,9,1],[5,-3,-2,-7,4,9],[6,1,-9,8,9,-10],[-5,4,-4,-6,-3,-1]],[[-3,-7,-2,3,4,-3],[-6,-8,2,-1,-10,-3],[-10,-7,-1,9,-9,-10],[-5,-10,-4,3,-3,-4],[-8,3,2,4,6,-8],[-10,-10,-3,1,-1,6],[-5,7,9,-2,-10,5],[-3,-7,-10,8,10,-10],[-8,3,-3,7,8,-5],[-7,6,-4,-9,-1,5],[-1,-3,9,-6,-6,6],[-7,-9,-7,4,1,-1],[-2,-1,-9,6,7,1]],[[-5,-3,-5,10,2,-7],[-4,-4,4,2,-10,-8],[-9,-8,-6,-2,-7,1],[6,4,-3,-8,3,-3],[-9,-2,8,-7,6,3],[8,2,2,5,-7,5],[-1,6,-7,10,4,7],[2,8,1,2,7,-5],[9,7,1,9,-5,4],[4,9,6,1,-2,-7],[-2,-2,-5,10,-9,4],[-8,-9,-8,6,9,-3],[3,-4,-4,-8,2,-9]],[[-7,4,5,5,1,-10],[-9,2,-4,-2,8,10],[10,10,7,10,-8,1],[4,-9,-10,-3,-7,-6],[9,-8,7,-1,-7,1],[-10,-10,-7,4,-9,-4],[3,-1,-4,1,-6,-2],[-8,-1,6,9,-3,6],[3,9,6,4,-3,-2],[-1,-2,-4,1,-7,-7],[2,-9,-8,-5,7,-5],[-9,2,4,-1,-7,-2],[-7,-4,-5,7,8,4]],[[-3,9,3,10,-4,6],[-8,-3,-1,-7,9,-3],[2,-4,6,-6,-7,8],[8,-3,-2,-8,-9,-5],[-7,-7,4,1,-1,-6],[-4,-5,-7,4,3,-8],[8,7,-9,8,-7,-10],[-6,-6,-9,6,-5,6],[-6,-7,-8,5,-1,5],[-7,3,9,-4,8,2],[4,-1,-8,9,7,-4],[1,5,2,-9,3,2],[9,7,-7,7,8,10]],[[-4,2,7,8,-5,-7],[5,7,-1,-9,4,10],[-8,3,-4,4,4,-1],[3,-6,-4,-7,-10,-6],[1,1,-5,9,7,-9],[-6,1,10,10,5,2],[-10,10,-3,-1,6,-2],[-7,4,4,7,8,-10],[1,-2,8,8,4,8],[-6,4,4,-3,-10,5],[2,-5,-1,1,-7,-10],[10,10,8,3,-8,-6],[-4,1,5,9,-9,10]],[[-9,4,7,-8,-4,8],[8,-5,-8,-9,9,-8],[8,-4,2,-9,-6,-5],[-6,7,-5,3,-8,-2],[-1,-1,-2,5,-8,7],[2,9,8,10,-10,6],[-3,9,-1,-8,-1,-3],[9,1,8,7,5,-9],[-1,8,3,5,7,7],[-4,-8,-5,-7,2,2],[-9,1,5,8,-6,-7],[2,-7,7,-5,-9,7],[-6,10,2,8,-1,5]],[[7,-3,-2,4,-4,1],[6,-4,10,1,-6,6],[3,1,-2,-3,2,4],[6,-5,8,2,5,1],[5,-3,-2,-1,2,-10],[-8,3,-7,-1,-2,3],[-6,6,-1,7,8,9],[9,-5,-1,3,-6,-7],[-3,7,-7,-7,-7,4],[-1,-6,-1,9,6,-10],[8,4,10,-6,2,-8],[4,-3,2,9,-8,-4],[-1,-10,-8,-1,4,8]]], dtype = "int16")#candidate|8365|(15, 13, 6)|const|int16
bop_8366 = relay.left_shift(var_8364.astype('int16'), const_8365.astype('int16')) # shape=(15, 13, 6)
uop_8370 = relay.cosh(bop_8366.astype('float64')) # shape=(15, 13, 6)
uop_8380 = relay.log2(const_8365.astype('float64')) # shape=(15, 13, 6)
output = relay.Tuple([uop_8370,uop_8380,])
output2 = relay.Tuple([uop_8370,uop_8380,])
func_8389 = relay.Function([var_8364,], output)
mod['func_8389'] = func_8389
mod = relay.transform.InferType()(mod)
mutated_mod['func_8389'] = func_8389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8390 = relay.var("var_8390", dtype = "int16", shape = (15, 1, 6))#candidate|8390|(15, 1, 6)|var|int16
func_8389_call = mutated_mod.get_global_var('func_8389')
call_8391 = func_8389_call(var_8390)
output = call_8391
func_8392 = relay.Function([var_8390], output)
mutated_mod['func_8392'] = func_8392
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8550 = relay.var("var_8550", dtype = "int8", shape = (15, 2, 16))#candidate|8550|(15, 2, 16)|var|int8
var_8551 = relay.var("var_8551", dtype = "int8", shape = (15, 2, 16))#candidate|8551|(15, 2, 16)|var|int8
bop_8552 = relay.not_equal(var_8550.astype('bool'), relay.reshape(var_8551.astype('bool'), relay.shape_of(var_8550))) # shape=(15, 2, 16)
func_6067_call = mod.get_global_var('func_6067')
func_6073_call = mutated_mod.get_global_var('func_6073')
var_8557 = relay.var("var_8557", dtype = "uint16", shape = (1024,))#candidate|8557|(1024,)|var|uint16
const_8558 = relay.const([-1.286417,-2.884808,4.289757,4.038353,-9.481616,6.357104,4.806758,0.140537,3.992854,-8.151816,-5.716802,4.431996,-8.159061,-2.521643,-2.909111,2.527966,1.024080,7.441804,-8.530370,-1.516692,8.496796,-0.302797,7.937966,3.236282,4.897087,9.561046,3.705470,0.899671,-1.435102,1.109649,4.620398,-4.127700,-4.968342,4.041407,-6.476533,4.994820,-3.233525,-0.621234,7.736365,-4.195886,-0.429227,-6.336764,-3.233043,4.410280,8.169340,8.725344,7.397196,-0.174696,-2.434040,-2.503021,4.677049,-2.030516,5.397489,6.628283,9.992699,-6.338371,9.716885,2.117316,-3.472449,6.576768,2.875388,0.656943,-0.288121,-7.474168,5.224524,6.342612,-9.546094,-7.084487,4.852777,-8.482013,0.556167,-8.817079,1.713252,-4.411469,-2.568205,1.350048,4.104652,-5.873692,-4.780107,-4.398686,-4.769310,-9.501764,7.659173,-4.537675,8.074683,8.618329,5.045984,8.257752,8.039316,8.147126,4.807963,3.444258,9.983697,-0.015009,-3.580557,3.867420,1.414334,2.418198,6.601943,4.206871,-4.747662,9.834615,-7.206517,-7.761102,8.813344,6.211078,8.981727,9.425285,-7.399579,-6.769984,-7.697816,0.227558,-4.026737,-9.993550,9.187229,-1.213705,9.571482,8.470409,-1.947281,8.210077,4.667183,1.065270,-9.998491,7.667097,-1.825507,3.891272,-9.468301,-8.205589,-6.976929,-3.396465,-7.709505,8.517207,-6.550328,0.952286,4.248747,-4.095640,2.555092,7.243002,-0.357708,3.344869,-3.616463,1.949811,4.076750,8.298300,1.722646,1.348104,-6.256655,9.346139,-6.363234,-2.633887,1.200359,-7.686319,-2.532706,-0.902272,3.929876,3.965128,1.397942,-4.415910,9.207156,-1.170011,2.494446,-6.253518,-1.467470,-0.105601,6.089856,-5.530335,-8.426564,2.051738,-9.369403,1.002464,4.317815,-2.208300,-7.126412,-8.247835,-1.719018,-4.040515,-7.594562,-5.064347,-5.570647,9.387666,2.582855,-2.614876,9.245123,-3.831756,-7.386076,8.718039,-0.055825,-8.681729,-9.243109,-3.311676,7.494155,-6.371234,-1.493284,-6.923296,3.992522,-9.567894,-3.792959,-3.392731,-4.688693,5.829664,1.571702,8.312504,-6.918701,-8.030528,-4.015781,-4.340877,7.919857,3.628980,3.207554,-1.144188,-8.558951,3.330182,5.557827,-3.392073,-8.728642,-0.612014,-8.324716,9.342463,2.230918,3.134079,0.851114,1.619123,-4.589677,-8.778010,1.054311,-6.764898,5.799264,-1.853761,-5.364479,-8.647797,-4.130586,-0.810711,-1.978838,-2.410488,2.375215,8.476388,0.016330,4.452527,-4.212208,2.051585,-8.882110,9.866654,1.506222,-9.673118,-8.977381,-4.292625,-2.116735,0.214998,-6.195654,-3.054672,1.795839,-5.426725,6.701132,-0.466376,1.777505,8.583978,9.394609,7.962123,-4.340950,-2.739237,1.243250,0.197998,7.849302,-1.414903,-5.661690,6.064071,9.230066,-0.822544,2.063582,-6.663411,-2.182363,-7.071255,-9.657382,-7.590702,-9.060788,3.665914,0.863080,7.231493,0.956087,2.363842,-8.961615,1.324891,-9.054215,-5.623999,-9.642319,7.114203,-8.555157,-1.462558,4.920536,6.842524,-0.787936,8.960382,-4.070155,-4.467553,6.077835,5.680745,4.853143,7.675663,4.972657,2.654515,-3.791199,-2.264772,0.186309,2.037481,-0.462563,-1.161927,6.283798,-3.997157,-5.120881,9.780746,-2.337942,5.042462,9.041614,-5.795983,6.146874,-5.126696,-3.639426,-5.205516,0.808639,-5.802203,9.468364,-8.794404,7.478563,-1.949622,-9.427742,2.208784,-0.336462,-2.513836,8.805073,-1.222156,-8.022061,-0.132812,-9.099107,-2.381898,-6.700411,5.144050,6.701224,-6.619448,-4.172188,-9.375710,-0.504020,-5.600063,4.843197,-5.603727,7.519177,3.109287,6.447817,-7.102792,-3.578766,8.719986,0.990587,-9.034535,6.709149,8.655039,9.187486,-2.847605,0.334662,5.536784,0.031591,3.752268,-5.161652,-1.090760,-9.925761,1.733596,-4.621608,8.272705,7.765622,-0.825119,-2.918181,0.819083,-4.220469,5.991972,-1.890827,-0.219511,-7.042875,-2.401643,-2.803202,-3.015261,1.582941,4.637306,7.834593,8.565266,4.223363,7.352932,-6.824317,5.681352,-3.132520,-4.020658,1.714789,-6.565189,1.944863,2.620871,7.627402,-0.547910,5.893347,-3.042270,8.622936,-3.828650,-5.067872,-6.753721,-6.757851,6.016598,8.426392,4.295025,-2.533133,-4.768945,-8.046797,7.069410,-4.308212,-9.561410,0.272524,-2.194513,-7.850085,6.462010,-1.170244,1.620027,-5.550552,5.864057,6.057995,-9.753472,-3.922588,5.863937,-0.564242,-6.867059,-2.973463,1.789886,-7.592830,-3.089533,-2.083100,2.520210,-4.498423,9.119700,7.203707,-2.522920,3.459503,-9.881202,8.044009,-8.899956,-3.827991,-4.692722,8.391950,-6.560979,9.776761,-5.882546,0.956820,-7.629800,1.043711,-6.653578,-0.484716,5.741742,3.581012,4.253840,6.677087,0.504368,6.490155,-2.456949,8.133477,-0.858539,-1.089702,-3.302132,-2.917888,4.553553,-3.642827,-7.528235,-9.925738,-8.887573,9.026510,-8.095604,3.558690,-7.357773,-9.905755,0.255921,4.261253,-8.039312,-6.444780,7.555851,-2.780368,-3.938279,-5.997068,8.658913,-7.369416,7.381376,-3.940886,-0.070972,4.008535,-1.476977,-1.684360,1.833146,5.806586,4.564601,-0.695876,-4.206311,4.121650,1.340181,6.691621,-2.136193,-6.550335,1.992523,4.741413,-3.523417,-7.247619,-0.450508,-4.655118,-1.218931,-0.954702,9.614550,5.610821,5.637910,5.388572,-2.004581,7.610241,-7.680018,-2.428420,-6.713001,-8.249236,-3.611000,8.524321,8.854836,-1.268705,1.573470,6.943219,9.263172,-5.758273,3.451635,5.696823,-0.722896,-6.830714,-5.632355,-8.801939,-7.883481,0.401684,5.532102,-8.296731,-9.579126,7.038869,8.575367,6.007321,6.656664,9.598953,1.279696,-4.190806,1.634488,-2.478158,-9.473023,5.060837,9.290955,9.585251,1.917218,9.119745,6.587954,-3.870430,0.783932,4.064643,9.626805,9.986580,-2.037595,1.231952,-4.259486,7.599423,-9.633508,-1.566590,-3.240808,5.588055,0.177661,6.024452,0.982126,5.568811,4.329310,2.244278,7.545328,0.365956,-4.629062,1.424292,9.451925,0.417512,2.348566,4.644441,-8.107021,-4.709819,-1.490355,-0.831887,6.929410,-9.137334,-2.327090,9.419701,4.777332,6.692382,2.614880,-5.357596,-0.030045,7.852690,7.833001,6.457684,7.765255,0.626044,1.617443,7.364306,0.449213,-1.217031,0.186720,7.437059,-6.857071,-4.729560,-9.197231,-0.320290,7.045243,-6.640565,8.440464,-9.810707,5.014859,-1.602262,9.280236,5.461422,4.016484,-1.107134,-0.657224,3.403415,4.569183,-9.841865,9.176917,-2.367712,-7.498559,0.166026,-6.420307,-8.433151,-0.661695,-2.951770,-1.558041,-8.151979,1.234382], dtype = "float32")#candidate|8558|(630,)|const|float32
call_8556 = relay.TupleGetItem(func_6067_call(relay.reshape(var_8557.astype('uint16'), [16, 4, 16]), relay.reshape(var_8557.astype('uint16'), [16, 4, 16]), relay.reshape(const_8558.astype('float32'), [70, 9]), relay.reshape(var_8557.astype('bool'), [16, 4, 16]), ), 1)
call_8559 = relay.TupleGetItem(func_6073_call(relay.reshape(var_8557.astype('uint16'), [16, 4, 16]), relay.reshape(var_8557.astype('uint16'), [16, 4, 16]), relay.reshape(const_8558.astype('float32'), [70, 9]), relay.reshape(var_8557.astype('bool'), [16, 4, 16]), ), 1)
uop_8567 = relay.cosh(call_8556.astype('float64')) # shape=(70, 9)
uop_8569 = relay.cosh(call_8559.astype('float64')) # shape=(70, 9)
bop_8570 = relay.equal(uop_8567.astype('bool'), relay.reshape(const_8558.astype('bool'), relay.shape_of(uop_8567))) # shape=(70, 9)
bop_8573 = relay.equal(uop_8569.astype('bool'), relay.reshape(const_8558.astype('bool'), relay.shape_of(uop_8569))) # shape=(70, 9)
func_4293_call = mod.get_global_var('func_4293')
func_4296_call = mutated_mod.get_global_var('func_4296')
call_8578 = relay.TupleGetItem(func_4293_call(relay.reshape(const_8558.astype('float32'), [7, 10, 9])), 0)
call_8579 = relay.TupleGetItem(func_4296_call(relay.reshape(const_8558.astype('float32'), [7, 10, 9])), 0)
output = relay.Tuple([bop_8552,var_8557,bop_8570,call_8578,])
output2 = relay.Tuple([bop_8552,var_8557,bop_8573,call_8579,])
func_8582 = relay.Function([var_8550,var_8551,var_8557,], output)
mod['func_8582'] = func_8582
mod = relay.transform.InferType()(mod)
mutated_mod['func_8582'] = func_8582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8582_call = mutated_mod.get_global_var('func_8582')
var_8584 = relay.var("var_8584", dtype = "int8", shape = (15, 2, 16))#candidate|8584|(15, 2, 16)|var|int8
var_8585 = relay.var("var_8585", dtype = "int8", shape = (15, 2, 16))#candidate|8585|(15, 2, 16)|var|int8
var_8586 = relay.var("var_8586", dtype = "uint16", shape = (1024,))#candidate|8586|(1024,)|var|uint16
call_8583 = func_8582_call(var_8584,var_8585,var_8586,)
output = call_8583
func_8587 = relay.Function([var_8584,var_8585,var_8586,], output)
mutated_mod['func_8587'] = func_8587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9202 = relay.var("var_9202", dtype = "float32", shape = ())#candidate|9202|()|var|float32
var_9203 = relay.var("var_9203", dtype = "float32", shape = (11, 13, 10))#candidate|9203|(11, 13, 10)|var|float32
bop_9204 = relay.floor_divide(var_9202.astype('float32'), var_9203.astype('float32')) # shape=(11, 13, 10)
func_550_call = mod.get_global_var('func_550')
func_555_call = mutated_mod.get_global_var('func_555')
const_9217 = relay.const([4,7,3,6,7,-5,3,-10,3,-9,-1,9,-5,-1,4,-8,-2,-8,4,2,-9,-2,-5,7,8,-10,4,-8,-6,-1,1,-9,-4,-9,-10,2,10,-2,-6,6,4,-6,-7,5,-1,2,-6,4,-7,-10,6,4,8,2,4,-10,3,-5,8,4,8,3,8], dtype = "uint32")#candidate|9217|(63,)|const|uint32
var_9218 = relay.var("var_9218", dtype = "float64", shape = (72,))#candidate|9218|(72,)|var|float64
call_9216 = relay.TupleGetItem(func_550_call(relay.reshape(var_9202.astype('uint32'), []), relay.reshape(const_9217.astype('uint32'), [3, 7, 3]), relay.reshape(var_9218.astype('float64'), [72,]), ), 3)
call_9219 = relay.TupleGetItem(func_555_call(relay.reshape(var_9202.astype('uint32'), []), relay.reshape(const_9217.astype('uint32'), [3, 7, 3]), relay.reshape(var_9218.astype('float64'), [72,]), ), 3)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
const_9221 = relay.const([[5],[-9],[3],[-6],[2],[-7],[-2],[6],[-6],[3],[-10],[1],[-3],[6],[5],[7],[-5],[9],[-10],[9],[4],[8],[2],[-1],[10],[-2],[-2],[-10],[5],[9],[1],[10],[-2],[4],[-3],[5],[-10],[3],[-9],[-4],[6],[-1],[6],[5],[7],[-3],[-8],[4],[1],[-4],[-2],[2],[-2],[-6],[7],[9],[-6],[4],[-4],[-5],[-1],[-7],[1],[-8],[9],[9],[-9],[-5],[-5],[-1],[3],[-6],[2],[8],[8],[-5],[2],[-7],[3],[-7],[7],[6],[-4],[8],[-4],[-2],[1],[-5],[-9],[-7],[8],[6],[-3],[-3],[8],[1],[-6],[5],[9],[-1],[-2],[-1],[2],[-6],[-9],[-10],[6],[-7],[8],[-9],[1],[-4],[-8],[9],[2],[-4],[3],[-9],[-1],[8],[9],[-7],[3],[-8],[-7],[7],[-7],[-5],[10],[6],[-1],[6],[4],[-1],[-2],[5],[6],[-8],[9],[9],[-3],[3],[9],[-6],[-9],[-3],[-3],[-6],[-6],[-3],[5],[-10],[1],[9],[-4],[-5],[-9],[6],[4],[9],[4],[-8],[2],[-3],[-3],[7],[-4],[9],[4],[5],[-8],[-4],[9],[-5],[10],[8],[5],[-1],[2],[-5],[8],[-2],[-6],[-8],[-9],[-8],[-3],[4],[-2],[5],[-2],[-8],[-3],[-5],[-10],[-9],[-2],[-9],[-10],[-1],[-9],[-5],[-3],[4],[-7],[-9],[-6],[-9],[-3],[3],[7],[-2],[-10],[9],[9],[10],[3],[10],[-6],[3],[-5],[-6],[9],[-9],[10],[-6],[1],[5],[-10],[-3],[4],[-4],[-1],[-5],[1],[2],[-10],[9],[4],[4],[10],[-8],[-9],[-4],[7],[5],[-1],[10],[-5],[8],[-5],[-4],[-9],[-6],[10],[6],[9],[1],[-8],[4],[-2],[-9],[-10],[-4],[-8],[-3],[-5],[5],[1],[-6],[1],[-3],[5],[-8],[-10],[-8],[-1],[-5],[10],[8],[-4],[-8],[-9],[10],[6],[2],[-7],[8],[8],[-2],[-8],[1],[9],[-2],[5],[-6],[2],[-7],[-9],[-10],[-4],[-2],[7],[10],[-4],[4],[-5],[1],[8],[5],[-3],[4],[5],[8],[-10],[-8],[-3],[5],[10],[5],[-10],[-6],[-1],[10],[-10],[5],[-4],[-1],[-2],[-2],[9],[9],[10],[-2],[-1],[-4],[6],[-5],[7],[-6],[-8],[4],[-2],[2],[6],[-8],[-8],[9],[-3],[10],[-7],[-5],[4],[-8],[5],[2],[7],[-9],[3],[-4],[-7],[-5],[1],[3],[-2],[8],[-7],[2],[2],[6],[6],[-3],[4],[-3],[-3],[-7],[3],[-5],[6],[10],[3],[1],[10],[-3],[3],[-2],[-7],[-1],[6],[1],[5],[4],[-2],[4],[-9],[9],[-2],[-3],[-2],[-7],[-6],[-4],[-3],[-6],[-3],[2],[5],[-5],[5],[6],[-6],[7],[3],[-2],[-8],[2],[7],[9],[-2],[-3],[-3],[2],[1],[6],[9],[-1],[7],[2],[-9],[7],[-3],[-1],[4],[2],[-6],[9],[-10],[-9],[8],[-8],[-9],[1],[8],[-8],[-8],[-4],[5],[-1],[9],[2],[-8],[5],[4],[10],[1],[-1],[6],[6],[5],[-1],[-8],[-4],[-4],[1],[10],[-9],[8],[8],[-9],[-4],[-6],[-3],[-6],[4],[-3],[-4],[2],[6],[-5],[-9],[2],[-5],[3],[-2],[2],[5],[2],[-10],[-6],[-8],[1],[-2],[10],[-3],[6],[-9],[-2],[-1],[-8],[9],[1],[-7],[3],[9],[-4],[-10],[9],[-10],[-1],[3],[4],[8],[-4],[1],[1],[1],[-4],[-3],[8],[6],[-9],[6],[10],[8],[-10],[-1],[-2],[-2],[-9],[8],[3],[-2],[-10],[5],[8],[-9],[-10],[6],[3],[-3],[4],[-1],[4],[-3],[-6],[-3],[-2],[7],[-9],[-9]], dtype = "int8")#candidate|9221|(550, 1)|const|int8
call_9220 = relay.TupleGetItem(func_3434_call(relay.reshape(const_9221.astype('int8'), [10, 5, 11])), 0)
call_9222 = relay.TupleGetItem(func_3437_call(relay.reshape(const_9221.astype('int8'), [10, 5, 11])), 0)
output = relay.Tuple([bop_9204,call_9216,const_9217,var_9218,call_9220,const_9221,])
output2 = relay.Tuple([bop_9204,call_9219,const_9217,var_9218,call_9222,const_9221,])
func_9239 = relay.Function([var_9202,var_9203,var_9218,], output)
mod['func_9239'] = func_9239
mod = relay.transform.InferType()(mod)
var_9240 = relay.var("var_9240", dtype = "float32", shape = ())#candidate|9240|()|var|float32
var_9241 = relay.var("var_9241", dtype = "float32", shape = (11, 13, 10))#candidate|9241|(11, 13, 10)|var|float32
var_9242 = relay.var("var_9242", dtype = "float64", shape = (72,))#candidate|9242|(72,)|var|float64
output = func_9239(var_9240,var_9241,var_9242,)
func_9243 = relay.Function([var_9240,var_9241,var_9242,], output)
mutated_mod['func_9243'] = func_9243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9418 = relay.var("var_9418", dtype = "float32", shape = (5, 4, 8))#candidate|9418|(5, 4, 8)|var|float32
uop_9419 = relay.erf(var_9418.astype('float32')) # shape=(5, 4, 8)
var_9421 = relay.var("var_9421", dtype = "float32", shape = (5, 4, 8))#candidate|9421|(5, 4, 8)|var|float32
bop_9422 = relay.greater(uop_9419.astype('bool'), relay.reshape(var_9421.astype('bool'), relay.shape_of(uop_9419))) # shape=(5, 4, 8)
func_6813_call = mod.get_global_var('func_6813')
func_6816_call = mutated_mod.get_global_var('func_6816')
const_9434 = relay.const([8.687283,6.298524,0.017555,6.417874,5.999526,0.496910,6.536016,7.753258,3.667976,0.805295,5.742265,-8.420191,-4.946028,-5.247542,-7.619960,0.573802,4.517532,-0.887134,-8.330349,0.447872,-2.521561,-6.763452,7.573037,-7.852168,-8.465141,-2.638986,2.075203,-6.478851,3.503471,2.298470,3.686972,8.182308,8.474384,9.393619,0.313221,-1.300571,2.683507,-6.997282,-1.537506,9.440562,-9.171934,-9.680916,-7.987170,9.835012,3.157558,9.009950,6.437596,-9.700684,-7.059896,8.975000,-5.203696,2.699695,-9.215826,-5.035599,-7.162170,1.126058,6.110169,-2.097383,-5.379475,1.453259,0.233262,-2.670318,4.374696,7.533905,-2.800941,-0.926312,-9.637984,-8.370734,1.796508,-1.283725,-6.828826,-6.020326,2.476894,4.101783,-4.322225,-1.653294,0.506072,7.675138,4.553657,-5.539714,4.560626,-5.657512,-0.578644,-6.357309,-9.457629,7.259150,7.772607,-2.599581,5.068320,-4.840367,6.075747,3.683713,-6.877005,6.763402,0.679098,3.807916,-4.096787,5.293090,5.130380,-7.987414,-2.574862,-8.605151,9.903470,-6.959304,0.267583,9.091272,4.352308,9.040135,6.483293,1.698524,9.601938,4.605625,7.139663,-6.962185,-1.208169,-3.899905,5.102690,-8.657630,3.928587,1.625754,-2.200763,4.576081,2.146078,1.693967,-5.795520,7.288663,8.540571,1.508660,1.473911,8.705511,8.769762,-3.592670,4.150705,9.265109,-5.798338,1.270396,5.939874,-6.124346,5.265387,6.402195,3.921917,3.721613,3.448864,7.855939,0.127293,5.930174,-7.519376,5.003108,-9.874894,-7.583499,2.151974,7.114505,4.021005,9.699779,2.597845,-6.340410,1.155961,-8.735554,-3.128604,-1.481383,-5.338710,-7.286451,7.201067,-9.381794,3.800139,-7.395446,-2.094757,3.827826,-4.446793,6.714761,-5.063814,-5.790109,6.023871,-7.057939,-2.609071,1.214603,-9.819058,8.721357,0.038284,-1.165099,-5.563899,4.642333,-8.345837,-2.701390,7.308448,1.111678,9.604306,-4.590388,-0.313551,2.366412,8.851292,9.598827,-6.168253,5.110480,2.137710,-9.166660,4.467323,-8.592222,1.207774,-7.520609,-1.956085,-5.430147,4.087426,4.824873,6.335987,-8.772725,6.340175,2.846059,-2.717871,-8.060111,-3.143216,9.148808,-7.883583,9.612466,1.428023,0.825329,0.016098,4.400461,-6.411295,-6.614336,3.395881,-1.288126,3.459314,9.616937,-6.485033,3.292394,-5.791134,-1.637314,-2.063053,-5.835952,9.606769,-6.091381,0.075485,5.968602,-4.826673,-2.634312,-8.960606,-1.207551,-2.911413,5.734645,1.617626,2.092260,-8.003479,4.602599,6.448678,-3.710482,3.771247,-0.353129,-6.111410,-0.497575], dtype = "float64")#candidate|9434|(250,)|const|float64
const_9435 = relay.const([9,-3,-7,2,-6,-8,9,-9,-10,3,-10,5,5,-8,-6,-4,-9,1,-8,1,-10,-8,2,-1,8,-8,-10,-6,10,2,2,-10,-5,-7,4,8,5,-2,-3,9,-9,-2,9,-6,3,-2,5,6,-5,-2,10,-2,6,-2,-6,-2,8,-8,1,6,3,1,-10,-8,9,-3,-2,4,8,8,-10,1,-4,7,-2,-3,8,2,10,-4,-4,10,1,-5,-1,-5,5,9,4,9,8,8,6,6,2,9,-9,1,2,-3,2,3,3,-9,9,-10,9,-3,-9,-3,2,-8,-10,3,6,-6,-3,6,-3,10,2,-9,9,8,-2,1,-4,7,10,7,-5,6,1,3,-8,4,-2,-1,-6,10,-9,-3,2,8,-9,9,5,1,7,10,6,5,8,2,-4,-1,3,-9,-2,-6,1,5,1,2,2,5,-5,-10,8,-6,-4,7,-10,2,-3,-5,4,-10,7,-4,5,7,-2,2,8,-2,6,-10,6,-10,-10,5,6,10,-9,-10,-4,4,-5,5,6,-6,7,-1,-7,3,-6,1,4,-5,6,7,6,7,10,7,-7,10,-10,-6,2,4,8,9,-9,-6,2,6,-7,-9,2,4,-8,3,3,-7,-1,-2,8,-2,8,3,-3,5,-1,8,-10,-7,7,8,-1,7,-6,10,4,5,2,-1,-7,7,-1,-5,9,9,2,-6,-2,5,-3,4,-9,-7,-6,-7,7,5,9,8,2,4,7,-8,-4,-9,-10,-4,3,-9,2,-4,-10,-6,8,8,1,3,3,-7,4,4,8,-2,-9,-7,-7,-9,-9,7,-7,7,-7,6,-2,7,-8,2,8,4,-7,10,4,-4,-2,-2,5,1,-10,4,-9,-9,-1,-2,9,8,-8,1,-8,9,-5,1,8,2,8,-9,-6,-5,-1,9,4,5,6,6,-10,-5,3,5,-7,-9,-4,3,9,8,-6,2,-6,2,5,-5,-2,-2,-6,8,5,-10,8,-10,3,8,6,-9,-7,4,8,8,10,7,-6,-1,4,1,-5,10,-8,-7,-10,-5,-7,10,-8,7,8,-6,-3,-5,-8,-1,-7,3,3,8,-8,2,-3,3,1,-9,-8,-1,-2,7,5,5,3,5,-9,1,9,-5,6,-2,-9,-5,-8,7,-5,1,6,-1,-3,-5,3,-10,-9,-3,-2,-1,-9,-8,-5,8,1,1,7,-6,-2,3,-9,8,-5,-5,7,9,-4,-3,-4,-10,-4,4,-5,-10,-5,2,5,2,-10,-8,-4,-3,6,7,8,-8,-8,-4,5,4,6,-4,6,2,4,5,6,6,3,-3,1,-3,-4,-6,10,10,5,-10,1,-9,1,3,-1,1,-2,-4,8,4,4,-2,7,4,-8,-5,6,6,-7,7,7,1,-4,4,2,-5,-7,3,-3,-8,-1,1,-6,-5,7,-10,-1,6,3,9,-8,-2,-3,9,-3,-8], dtype = "int8")#candidate|9435|(550,)|const|int8
call_9433 = relay.TupleGetItem(func_6813_call(relay.reshape(const_9434.astype('float64'), [5, 5, 10]), relay.reshape(const_9435.astype('int8'), [550,]), ), 2)
call_9436 = relay.TupleGetItem(func_6816_call(relay.reshape(const_9434.astype('float64'), [5, 5, 10]), relay.reshape(const_9435.astype('int8'), [550,]), ), 2)
output = relay.Tuple([bop_9422,call_9433,const_9434,const_9435,])
output2 = relay.Tuple([bop_9422,call_9436,const_9434,const_9435,])
func_9438 = relay.Function([var_9418,var_9421,], output)
mod['func_9438'] = func_9438
mod = relay.transform.InferType()(mod)
var_9439 = relay.var("var_9439", dtype = "float32", shape = (5, 4, 8))#candidate|9439|(5, 4, 8)|var|float32
var_9440 = relay.var("var_9440", dtype = "float32", shape = (5, 4, 8))#candidate|9440|(5, 4, 8)|var|float32
output = func_9438(var_9439,var_9440,)
func_9441 = relay.Function([var_9439,var_9440,], output)
mutated_mod['func_9441'] = func_9441
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10094 = relay.const([[[-1.406703,-6.965860,-4.848533,-8.078367,3.132353,5.910004,3.065308,-2.157502,-5.809532],[-5.704942,2.482817,-6.731322,8.008655,-1.982632,-0.719473,-6.683291,1.639574,1.729380],[-5.158574,-5.567150,-9.648273,4.924404,0.921864,0.363268,-6.592839,-4.229634,-6.009030],[-1.400827,-7.357131,-6.614198,5.059440,0.191628,-4.763671,-1.421222,7.218679,-8.762832],[-0.226053,9.670983,-2.086984,-8.993145,-5.687199,-1.908852,6.066225,-0.579842,0.156549],[-7.135450,0.014355,-6.366245,-4.285558,8.368706,2.951247,7.312357,6.133472,9.173305],[1.072208,-9.078426,-8.085675,2.472690,5.037588,-7.225385,-9.970829,0.441994,-9.976081],[5.886495,2.330461,-0.086782,2.292770,-9.534767,2.084075,-2.846803,3.182530,-7.127207],[9.878606,9.530035,-0.557572,-1.951963,-4.802877,-8.492623,8.878434,9.370058,-3.203825]],[[1.027208,5.373933,-2.559751,-8.883518,-3.963336,1.265134,2.408751,-0.026288,-4.226934],[-7.209505,8.031022,-1.847234,-5.457253,-8.983384,-9.298961,5.558618,-4.082690,-1.046145],[1.265992,1.310042,-5.468053,9.820063,7.558382,2.272793,-6.823061,-2.857563,-1.471066],[5.958750,-0.318766,7.808072,6.369777,5.995639,1.599208,-3.692808,-8.637852,-5.249837],[5.900525,-1.572979,9.405353,-9.118575,-2.452967,-2.853063,9.193945,7.597672,9.864908],[5.159595,7.796810,-9.597915,-2.332427,-7.265301,-3.828311,1.924885,-9.698472,-2.660416],[8.228751,7.794452,-3.614166,6.848426,1.350929,9.627868,0.006315,8.574939,8.507775],[6.031619,7.679877,-6.185257,0.153919,4.018127,-5.075479,1.799592,-4.369647,4.523172],[-4.641361,-7.972138,4.677912,-5.370018,-6.417732,1.831616,2.237986,4.956577,-8.011424]],[[-3.024815,-6.842893,4.685999,-2.995719,-6.290295,4.849814,8.240847,-7.562227,-4.856699],[4.668256,-2.350834,-1.054228,-2.798234,4.964945,-0.221857,1.145126,9.896693,-8.363165],[-5.044731,5.044076,3.747110,-5.974591,8.514222,8.831026,-5.843916,-1.097906,-0.500352],[5.230789,8.500946,1.981892,-0.023684,-7.932649,-7.343712,6.195322,8.789199,0.904172],[2.093122,0.099355,5.185799,-8.768489,-0.643390,-0.134036,-4.713019,6.167376,-8.733687],[6.791602,9.886637,-4.072986,0.064499,0.072402,5.302479,6.087408,-6.474396,9.959591],[1.739962,-8.519445,-5.700984,1.334992,-5.080425,-0.120608,0.591927,0.688688,-8.385837],[-8.612702,2.339720,-3.562574,-1.885491,-1.222804,7.288712,-7.775199,7.677728,-6.107423],[-2.848060,-8.892935,-5.895642,1.216768,9.885442,-6.297685,7.189807,5.778689,-9.956479]],[[5.847816,7.225032,-6.456302,1.724521,-8.150073,2.448507,-3.844698,-6.359410,-3.371382],[-7.909728,-8.328031,-6.892847,2.276746,9.888034,8.129120,-3.433194,-9.569575,-0.151104],[-2.505083,-8.257104,-7.522237,2.522253,5.031331,-5.081592,-0.025548,1.298038,-5.216998],[-5.305688,0.231814,-8.387689,7.388877,1.365567,-0.984965,-2.483627,2.513955,4.067487],[-3.961025,7.800531,-1.614282,8.473284,-8.690921,5.874186,6.476727,-6.407368,2.489090],[3.505886,5.740007,1.385556,-2.690405,2.096327,-7.386176,1.352212,5.149664,-2.991292],[-8.335224,3.845217,-3.899546,7.670269,-0.191083,6.051390,-6.026375,-4.561361,1.884757],[-4.899757,-2.730796,-8.349660,-6.196851,4.951591,-8.648687,-1.639240,-6.135777,2.982942],[-0.466484,-5.265466,-9.688566,5.884252,-1.525306,-9.978832,0.344132,9.762783,-4.373700]],[[-9.314025,9.282804,4.835284,6.159988,0.161204,6.964672,-3.815906,6.131216,-4.053485],[-6.787118,8.214801,2.133805,2.462796,-7.841033,-0.138406,-9.067872,3.495790,1.016257],[1.785657,-5.600894,-5.425792,7.490954,-4.963812,8.335241,-9.492190,-0.837651,-0.283977],[3.148531,-4.881698,-5.036000,6.437131,5.475021,-6.062729,4.253063,1.351059,-4.514683],[2.092325,-8.464370,0.110753,-4.028885,-6.330169,8.027116,-9.833998,-0.084343,-9.606766],[-8.417095,2.925637,-1.131546,-1.266320,6.680568,-7.150039,1.400599,5.197031,3.493091],[6.990352,-6.829977,-2.699765,-3.088872,-6.183882,4.454742,7.707677,-6.109894,4.948008],[-2.094150,-8.522523,0.257871,-0.665807,-1.678511,-5.174428,-5.421626,4.926966,8.231439],[-9.658959,5.682128,-5.154341,9.622503,-6.653958,-5.777748,-0.956846,9.719050,-5.216285]],[[1.481652,9.372650,-3.909494,9.916129,7.284645,2.432284,-0.543339,-5.438703,4.997225],[-6.583604,-2.153841,-2.434595,-3.512344,5.337134,-2.364849,-9.202809,-5.243989,9.186020],[-2.583274,0.538533,-8.630719,-2.387035,-2.841736,-4.839619,-7.794919,-9.712387,8.419417],[3.140416,-7.786874,5.381905,9.450348,-2.996199,4.594650,-4.703171,0.715940,3.639233],[5.817266,-7.877883,-0.209139,3.125405,-4.221293,9.892697,-8.292981,7.376465,8.180065],[0.992123,3.637079,7.186769,-2.771940,-8.004757,6.021027,5.172123,3.341451,7.203021],[-7.936440,-3.976173,-3.799301,-0.781354,6.461148,6.945024,-9.573767,4.423284,7.020461],[-9.629572,-0.446454,9.519525,-1.693451,-7.693318,-7.178308,3.136569,-4.596830,2.900998],[0.338910,-2.082849,-0.155271,6.654539,-6.781690,-5.558082,7.152556,0.134190,0.667841]],[[-2.053410,3.625367,3.585714,-5.126541,-5.994564,7.415694,8.126857,0.366841,9.593992],[-5.393187,-1.996897,8.337641,-3.528129,5.084215,-0.163990,-3.391528,-4.086489,-0.629741],[9.372581,-7.645559,4.715366,-3.102930,-1.299874,-4.802513,1.511954,5.341086,-6.910715],[-5.611629,5.783381,-7.475490,-6.786876,-1.451467,9.138831,-3.990945,8.311794,-8.329088],[-6.032887,-3.462539,4.807146,-6.714364,9.344347,-2.321902,-7.142157,-2.389025,3.838026],[-0.343127,1.612665,-9.794659,0.641017,2.054791,-4.692625,3.407109,-5.627770,6.029930],[4.297368,-4.618076,0.540008,-1.638323,9.942831,-9.862123,2.223347,-7.941679,7.282326],[1.165767,-5.756380,-9.114449,2.177463,2.646005,0.247755,9.866632,0.360175,4.791614],[-5.091928,-4.029656,-2.724928,-8.641781,4.118457,-9.651958,-7.316570,0.887386,-4.652273]],[[2.542980,-1.174303,-6.749281,0.470210,-8.411149,8.448330,-4.093198,0.639786,-5.008258],[5.214878,4.464016,3.861414,4.551874,-8.157946,-5.249957,-4.397224,-9.201234,6.214368],[-7.640297,-9.939141,5.174706,-2.326877,7.833054,-5.755344,6.528778,7.390483,7.799120],[-0.418642,-3.601388,6.514831,-2.240246,-0.671624,-3.690051,3.795944,-7.231053,7.138476],[2.972219,5.917737,5.970851,-2.527118,7.216486,-3.160241,4.459817,-4.735792,1.481142],[-7.695700,2.892667,-4.424511,-2.247987,0.546161,2.571919,-7.244264,-4.211293,9.411145],[-3.584860,6.418658,0.938343,-5.019263,-5.585193,-3.628403,-3.849614,2.903608,7.601118],[-2.417670,5.155593,1.738198,-9.780263,-8.666377,2.775453,7.426140,9.423760,-0.521779],[-9.785930,9.652530,8.268227,-9.112806,6.944653,5.211135,5.724274,-9.867035,3.728318]],[[1.159574,-9.371323,9.579645,5.335635,9.916951,8.112290,-7.413758,-8.311381,-2.502753],[9.622086,3.036490,6.809714,-4.888238,-1.781954,7.378402,-0.057662,-1.303758,-8.129278],[-2.196951,-9.743370,1.743928,1.776782,7.975871,6.255585,5.436388,-6.963227,2.224733],[-8.797438,-0.395341,7.848934,-9.846458,-8.596236,-0.850022,-8.317354,-3.195722,-7.736630],[-8.485712,2.792840,1.154535,-7.682650,-3.021178,6.127944,-6.471213,9.875758,6.414221],[-9.452961,-6.379185,-3.486798,-6.804244,2.103138,8.605958,-8.407980,-8.558980,3.267197],[-7.137339,-4.950429,-2.277975,0.709939,0.358055,9.339000,0.238585,3.360494,-9.464763],[-0.895855,-2.843809,2.401700,6.190893,-1.110318,-0.643417,8.663302,0.321526,0.841230],[6.497765,-7.393218,6.462129,7.275772,5.368111,-1.367482,-0.254724,-0.003437,-1.608470]],[[-7.996388,7.942084,9.459623,-5.300263,1.541965,0.853602,0.659943,1.272577,9.402128],[9.564257,0.650064,7.976234,-7.340153,-5.484026,9.746932,7.837556,-3.842270,-1.710773],[-6.317968,-8.100303,-0.318081,-8.228534,-4.817783,7.094092,-6.691612,2.521722,2.742550],[2.811183,-3.581251,1.326189,-0.712093,-9.709052,1.132806,8.012526,0.802404,4.838643],[4.283104,-2.821886,4.583040,4.743116,-0.451148,9.601377,-2.442416,-2.502844,-8.880428],[-0.503691,-6.596659,6.004290,7.645535,0.201684,-9.474480,-7.701089,-5.033860,-8.969089],[-5.983928,3.575096,-3.595352,-4.109744,6.983422,9.838907,-2.212402,-5.930161,-1.570471],[3.497312,-2.247692,2.602765,0.937520,-3.035672,-9.130058,-2.011165,2.965804,5.076029],[-9.570740,-1.540324,-6.238638,-6.316413,7.428611,3.011071,-3.004218,2.268139,9.998229]],[[-2.294063,-2.852538,-2.292262,1.695631,2.392175,-9.736947,-7.156971,-5.930615,-9.696275],[-8.508157,-0.592778,-1.405230,-8.476272,-3.198890,1.619806,-3.357862,-0.587179,8.205289],[3.694678,0.040729,7.179704,6.819760,9.817148,-6.566290,5.027169,-2.174686,-6.275756],[5.354802,0.837454,-2.980713,-1.787763,-2.785916,2.306403,8.270693,-9.905978,3.949747],[8.309560,0.313065,-9.213976,-0.868452,4.384446,6.877818,1.732392,-2.112588,-5.564299],[-0.186767,4.919343,-1.151949,-8.171761,4.970499,-6.180019,-2.811628,4.369087,-9.078916],[9.436436,1.984658,1.703594,-7.415282,-1.783901,-8.677682,9.530527,6.274235,1.464347],[1.162470,5.295635,1.771838,5.136294,4.270501,2.495851,-3.366653,7.472245,8.108504],[5.330761,7.268145,-5.688086,-9.807005,-1.257807,-5.669562,5.905075,4.681502,-7.737403]],[[0.485706,-8.159041,9.535989,-6.771080,-4.532527,7.159160,5.600150,5.864620,-1.080609],[-5.317715,0.858025,-6.484164,-0.286584,7.071006,0.858647,-0.699939,1.832156,1.156609],[8.970143,6.620198,0.672333,2.828770,9.643707,-5.779501,2.294448,-9.907960,7.233508],[-9.766665,5.521885,-7.162922,-5.509852,0.184832,0.751811,-9.353551,-2.619353,1.004286],[-3.378168,-9.915114,6.934017,-7.606125,7.962918,-6.523675,0.208091,3.490833,-4.820871],[2.846642,-0.699558,1.320022,-2.887334,-1.105317,8.289230,-4.368155,8.307901,2.120642],[0.118302,1.783714,-2.121696,-4.540820,-2.281998,-9.356325,5.822839,6.578400,-2.030367],[9.135467,-5.688935,-8.169200,0.542735,-5.841631,1.084289,-8.691162,5.808329,-8.040096],[4.115850,9.975867,-2.420995,-6.978545,-2.436344,7.756363,-2.748355,1.804656,0.005923]],[[-4.778925,-9.289722,3.980221,-0.723955,0.929774,3.853227,-1.486489,-6.013718,-8.281917],[0.045744,-8.211457,8.112038,7.637084,-8.053893,-2.703861,-1.177280,5.491428,1.298547],[-0.093035,-3.965911,8.269113,9.921762,-9.131258,-9.008520,-5.448382,9.270482,1.319479],[4.633265,8.556274,4.426280,3.767213,-0.443150,-7.376738,1.252789,-2.986036,-8.098220],[8.770166,3.571511,8.716553,-9.361672,4.130585,-2.254612,-2.446857,6.801699,-1.539103],[-7.618142,-9.808161,-0.393488,-3.151550,-5.041536,2.202835,3.028891,-3.413719,-5.175269],[-9.023381,-6.772839,-1.681828,-3.679894,-2.436510,-2.545817,-0.687001,-3.900559,-0.621047],[0.111904,-9.824507,3.926824,2.417673,-6.121744,0.857653,3.721319,0.395173,0.382811],[5.838352,2.816156,-9.516844,-9.661839,-7.064291,2.692325,4.218265,0.708833,-5.523606]],[[9.598280,5.881574,-7.064903,-5.806297,-4.723256,5.116928,1.947455,1.972250,-9.086719],[1.726373,-6.286084,6.224085,-1.257343,7.918849,-8.726782,-9.956571,0.743238,2.039073],[-8.019627,1.846427,2.680448,-6.643782,8.680734,9.922115,0.510602,-5.349916,-9.267599],[-3.077540,-7.899731,4.310489,5.463395,-1.054024,1.879076,-6.906277,1.114065,5.509848],[-9.988872,-4.205784,9.202072,9.305897,-6.207838,2.405103,0.718122,1.378011,5.675419],[-3.310545,-1.637732,5.709589,-4.584545,4.205107,7.310482,0.592770,-4.781704,-0.506233],[6.373227,0.525021,3.440834,0.763967,-7.253333,0.082701,7.178517,-6.225483,-7.638324],[9.374457,-7.519701,7.883931,8.859156,8.017522,-2.109768,-7.529337,-5.239108,4.780068],[-0.834623,-3.675365,8.449196,-4.446585,-5.213324,-6.987512,-5.390744,5.649901,-2.600919]],[[-9.211726,1.226007,8.722760,8.837407,-8.069436,7.420231,-9.215271,-4.404494,-0.180125],[-3.502146,-9.826881,-0.909050,1.999996,-8.223420,4.432477,3.092532,5.813207,5.395722],[-9.758080,-3.127568,-1.481211,-0.986980,5.987744,-3.635371,-1.423011,-7.189527,6.489753],[4.667646,8.559536,5.881690,-7.746515,-8.893643,-3.315436,6.582613,6.816651,7.598151],[5.945572,-0.911782,-5.989708,0.289657,4.511241,2.777723,-4.248651,9.012858,-5.386419],[-1.557726,-6.561245,-9.487527,-7.354725,3.926256,9.263356,-5.072966,6.816163,8.431258],[8.702227,-2.798868,-8.656104,4.860769,8.403754,-7.548903,0.231165,-9.669157,-2.203399],[-8.699723,-7.356539,-9.273255,-1.184777,8.357164,8.395943,0.092520,1.760721,5.284832],[4.531035,-7.567876,5.553661,8.024665,6.198629,-9.412517,-8.632875,-9.197675,2.180173]]], dtype = "float32")#candidate|10094|(15, 9, 9)|const|float32
const_10095 = relay.const([[[8.799707,0.287079,2.818404,2.977017,-2.536958,2.586241,5.171179,-7.068630,-3.944602],[-5.815353,-6.696211,9.209205,5.614468,2.860754,-1.576662,5.594081,5.150954,-4.917540],[2.921552,6.830474,-5.403170,-6.637078,-9.247726,7.837112,-3.035643,-5.918257,-7.397041],[0.427938,-0.534909,-7.835838,5.003697,-9.807502,-0.879096,-7.024854,0.914382,-6.048693],[-9.185774,1.691054,6.920407,3.831175,-5.325767,-3.366609,-1.325685,8.092680,5.876556],[9.293048,7.539568,3.504557,0.581654,8.574022,-0.244562,-2.244996,-2.489838,9.513630],[-2.562031,6.165372,7.361134,-2.318876,-6.733329,-6.172750,8.452372,-5.998625,8.932349],[4.932260,5.908568,1.604572,-8.034007,-0.050889,-4.819064,-7.255823,7.580259,8.134211],[-3.707790,-3.932806,6.496639,-0.952692,-1.320067,1.414537,-8.130421,-2.883321,-6.636279]],[[0.381044,-0.090479,5.921215,-2.860741,8.872944,-5.254633,-3.261136,-1.477569,9.722062],[0.266959,4.917602,-4.864287,0.970712,8.575786,7.668062,-2.770519,-8.750137,-3.308546],[4.087483,1.628159,-2.947237,6.585539,-2.799396,2.460401,-3.650182,1.418384,1.178020],[-4.898405,8.161899,-3.060074,7.534488,6.232040,8.077633,-9.148782,-6.612762,-2.321703],[1.246012,4.538767,9.481140,2.480655,1.735173,3.722272,-1.487980,-5.507836,1.701673],[-7.983201,3.941729,-4.978308,-4.802131,2.392871,4.230248,0.081550,6.744159,-2.970343],[-9.675790,-8.996613,0.333075,-2.801663,-4.973241,1.609258,8.966105,-8.544282,7.087416],[-8.831940,9.853477,6.212122,4.811013,8.491487,5.643308,6.814490,4.736846,-8.374649],[-5.555282,9.134543,2.072508,-2.495819,-0.720744,7.618735,-3.074300,9.977112,2.575386]],[[-2.091640,-5.351750,1.283919,9.016139,8.889995,1.274289,6.788369,-4.688416,-1.523423],[8.642429,-4.050463,2.981672,-9.865589,2.025357,-5.800667,-6.606413,9.546021,-0.731625],[-9.075497,-2.339479,9.453082,1.038670,7.254430,5.562644,2.529191,-6.881175,-8.731199],[4.086155,5.288408,0.269715,3.578575,-1.007815,-5.239738,-9.587383,5.375355,-7.814992],[-0.341426,4.669197,8.214880,5.024173,-7.552255,-3.337488,3.558537,4.733195,9.879345],[-2.366056,-6.916744,9.273638,-4.962825,0.120963,-1.927507,-4.938224,-9.527623,-4.422603],[-8.666453,-3.083880,-7.947853,7.371577,5.185199,-4.132924,9.973761,0.103885,-2.750344],[-3.664997,-5.510925,-2.545661,9.689009,2.006670,-0.970182,8.230437,4.874475,8.297823],[7.070967,-1.692229,1.172079,8.860081,3.035156,-6.820234,1.098114,-2.424875,2.890254]],[[5.909513,2.193125,-9.067556,-9.031830,-1.302466,1.253322,9.746629,6.412370,7.789020],[8.354625,8.885572,-2.960431,-6.841886,9.317655,7.525598,2.564335,8.346105,-3.135073],[-0.796293,-2.431436,-0.533194,0.388908,-1.105431,0.158346,8.983173,-1.088677,-0.069125],[9.375915,-5.648910,7.009181,6.951737,-3.727134,-8.701460,-2.605729,-2.503214,1.176789],[-4.558775,-6.339894,7.550182,6.968744,-9.617816,-6.893054,-2.675164,9.026831,-3.624564],[-4.269807,6.972402,-4.647367,0.561389,9.379423,9.435562,5.363031,2.725360,-8.750885],[6.785879,2.238499,2.172758,-5.743850,9.858773,9.229744,2.669673,1.346504,-8.188004],[-6.393376,-7.169205,6.247763,-3.359863,-4.382073,1.000511,0.392058,-0.317980,-3.342049],[-2.330690,6.963147,3.422557,8.473486,-2.553304,0.486405,-2.504933,5.824703,9.807466]],[[2.765262,2.570193,4.917681,-6.029908,9.648030,-6.995692,3.319530,5.153286,-7.815984],[2.749063,6.499398,7.084319,-7.846558,-3.129348,-9.645728,9.567555,0.074836,4.491912],[7.674656,5.966414,-5.467179,-5.731249,-5.453883,-5.638396,-2.679264,-8.952464,-8.053258],[1.504238,-1.112407,-8.686261,3.771671,-3.119987,-4.254653,-6.578399,5.971660,-2.607989],[8.216945,1.009753,-2.266184,-6.431905,5.159180,-4.386324,-8.310662,3.736699,4.065844],[-2.360237,7.359161,-2.668602,-1.063298,5.501291,-8.243575,-3.088021,-8.763521,-2.511090],[9.914840,-8.399638,6.772630,-6.160464,-2.803891,-7.612864,7.758568,-6.131199,7.089795],[-5.575382,9.263337,-3.000658,-1.014365,3.331835,-6.853909,5.225010,1.321129,7.265573],[6.334636,-5.723222,8.590576,7.167296,7.349114,9.802218,-3.928575,9.132888,6.891032]],[[-4.888990,-3.836757,-8.812701,1.674840,-8.887264,8.142328,8.917105,-6.507280,-5.383701],[0.481601,-6.293538,-3.701613,1.730088,-9.392265,-3.475479,-5.075748,3.134595,6.908389],[-8.689505,1.273520,6.124713,-1.391385,5.710568,-9.948305,-5.336200,-3.920815,1.370188],[-2.682616,3.561529,5.455571,-2.527185,-3.622720,-3.289422,5.674247,-5.789963,2.012588],[-1.343887,8.728376,-1.500193,2.308314,4.249014,-2.440225,-2.461245,8.827166,6.449131],[-9.641115,7.785318,3.401100,-2.257334,-0.242240,2.476050,-9.863429,9.892683,-8.787497],[8.317297,-0.396596,0.469100,0.041386,4.828687,3.242501,0.276496,-2.586706,2.398413],[-6.952504,-8.854098,-1.010565,3.706347,2.654852,-4.578160,-1.280794,-0.505900,-4.297139],[7.313672,6.351367,6.557544,0.501449,-3.739899,1.994415,8.775139,5.203607,-8.227584]],[[-1.654255,-1.590580,-1.689702,0.150556,2.602559,8.624597,0.422411,9.256132,5.133863],[5.567770,-4.607905,-4.430616,9.134514,3.719047,1.645802,2.363527,3.942408,-0.675487],[-5.282216,3.248425,1.918623,-4.948326,6.203900,5.255869,-4.350002,-3.616006,5.371273],[-5.125072,-6.692270,1.986246,1.664046,4.279653,2.909120,-6.116733,9.564889,2.337491],[-2.825387,0.206013,2.100831,-4.139869,-7.007911,-1.615111,6.301036,-7.544161,6.220973],[4.035247,-3.359098,9.046880,-8.425485,-5.135117,3.894767,-8.375723,1.137780,-3.229261],[5.652019,-8.858771,9.984567,8.237867,2.751712,-5.380966,3.965243,5.043344,4.588840],[9.118070,-0.411256,4.648035,4.874958,0.720548,-2.700469,-4.442910,-2.300516,2.086659],[1.289427,-8.995879,-1.573593,5.822682,-0.953928,-9.289121,-2.778652,-8.055835,9.238049]],[[-2.100288,5.935689,6.258940,6.507163,1.695812,-9.114580,3.994054,0.033323,-1.817294],[6.671505,-0.136748,-7.662910,0.485038,-9.517916,2.024550,7.889571,4.164100,9.147777],[-0.868252,-4.859229,-8.338586,-2.330493,-6.728834,4.161124,-1.481177,4.991179,-1.672755],[6.759774,-7.655966,4.971752,9.596404,7.101549,-8.905443,0.341454,-9.418820,-0.077969],[-8.316690,-5.003398,9.377732,8.617512,-5.634888,-2.578105,-1.789021,-5.105212,8.451521],[-4.064589,6.642084,4.865692,-0.544953,-4.957622,-8.370105,3.330300,-2.645497,-1.483078],[7.172632,0.452279,-6.015329,-6.977688,7.456473,5.519360,7.727495,4.930529,3.190209],[-4.313825,1.254488,-0.353448,6.620946,-8.015438,-9.960261,8.850203,-2.556439,1.061828],[-0.914382,0.860936,4.026889,3.173655,-6.232492,1.669824,5.059495,8.883812,-1.314940]],[[0.496210,7.766829,8.871810,-4.016207,2.472890,3.911704,3.930314,-2.888587,6.208925],[8.573285,-9.777687,7.665230,5.091436,2.984290,9.255131,6.085495,-9.833014,-6.604073],[-7.148198,-0.619281,3.044673,-8.393740,-7.720027,9.014362,-6.597490,-8.495243,-1.923091],[-2.773368,-9.856238,-2.070504,-5.083757,-6.243974,-1.235824,-4.287810,9.967426,-6.000813],[1.010008,0.541415,-9.442017,0.626871,6.498084,9.346440,-8.202092,-8.681296,-0.290261],[-5.326777,-6.562665,2.722003,-9.075923,6.833697,-4.931044,-7.409627,-2.993699,6.150798],[0.132818,-9.676612,-0.110376,-9.211713,3.351428,-2.483350,-5.697076,-0.627741,4.053863],[9.168106,-5.322486,-5.981860,4.598037,-7.600616,-8.076203,-8.433673,-8.072563,4.872568],[-7.547825,2.391404,-2.426057,2.810189,2.415735,3.270414,9.303070,-9.645309,8.724232]],[[5.722625,6.337381,-6.095609,1.336383,8.994552,8.211590,9.209791,9.087032,-7.276363],[-1.520578,-9.375940,7.382620,-1.696878,-2.736125,-2.991471,8.330989,-1.077864,3.448010],[2.111680,0.798456,5.287143,0.761208,0.995795,3.107165,-3.546393,2.090982,0.298496],[-0.469953,-3.729841,-7.477726,-0.645412,-5.092193,2.623498,4.171565,-9.830620,2.416562],[-0.971574,-7.723649,4.957962,6.421695,6.698466,-4.348333,2.898119,5.762274,-8.253971],[9.896834,9.520159,4.986848,6.343389,9.210913,-8.628141,3.172157,9.063843,-7.407217],[-9.436153,-7.666733,-8.778452,-1.147968,6.332722,8.716060,-5.160161,-6.005887,-4.742489],[-1.198167,2.354092,-5.107173,-1.894282,-3.801463,6.720280,7.422733,-4.759016,-3.291445],[-0.659012,-1.655375,-2.151660,5.951170,-1.938835,-4.140549,-3.286196,1.140602,6.366613]],[[7.181908,4.838504,9.920239,-7.998345,-4.389309,0.471068,9.085306,-1.840793,5.282472],[-9.945066,8.392616,7.869797,4.342998,-2.724982,6.745662,-2.344178,6.893289,-4.291943],[3.288478,3.908021,3.959113,-5.138037,0.143232,-1.239592,2.180632,3.043188,-8.527343],[-3.997447,-5.810359,-8.158067,-0.662128,-8.619627,-9.536904,4.560136,2.363581,-3.160896],[1.500083,-5.926138,3.399257,8.139971,5.467140,1.419743,2.998200,9.402007,-4.829043],[6.427629,6.434896,-5.272259,-3.358947,7.102963,7.491997,-1.876502,-1.310481,6.141006],[-6.245364,-3.297901,7.462563,1.885906,2.997127,7.035616,-2.905872,3.582057,-8.986661],[3.256431,9.123638,7.538323,-2.706650,4.917395,-1.353299,-5.484794,1.235346,-4.525711],[-5.567462,-2.915403,-3.400987,6.754406,-6.322029,-6.312401,2.724602,-2.422183,-4.020857]],[[3.007108,4.138854,6.610256,5.181685,-1.334732,-1.251622,8.471687,-6.811073,3.149035],[7.603511,7.491292,4.271145,5.995253,-9.210437,2.893252,2.308132,1.552953,9.486337],[-7.185402,3.877033,0.742538,9.213649,-1.496932,-5.434383,-8.515342,1.166916,-4.336594],[-6.318762,2.284561,0.676215,9.672568,7.021825,3.217659,-0.473894,8.159968,4.103184],[9.999817,2.757395,-7.364596,1.416489,-2.962683,0.535475,7.397880,-5.988690,-0.545144],[5.103968,-2.703784,-1.357630,2.846067,0.260059,-9.940342,-9.261465,4.820197,-6.381976],[4.570334,-5.508268,-1.293864,-4.468885,5.322497,-3.350601,-1.488930,-8.968077,-2.411909],[6.272946,0.266144,-0.131136,2.981697,3.332848,-2.215448,-1.650802,-1.126434,3.151384],[-6.267141,-7.595571,-6.105930,8.111677,8.826759,6.649366,9.206617,7.822128,4.032254]],[[-7.697619,-6.584815,0.504259,7.558575,4.693817,2.322851,-9.627557,-5.922977,6.743707],[8.905067,-2.398314,-4.930470,-6.737034,-7.904545,-8.287686,5.118336,-2.991947,0.421327],[6.500817,7.034326,-5.484542,4.841860,4.410913,5.742262,8.094261,6.062034,9.762130],[9.013229,6.913825,-1.602677,-6.330991,7.238224,0.654815,-4.572252,1.875559,1.076601],[-5.707704,9.060304,3.319558,3.318166,1.421868,-9.043063,-6.378206,1.710670,0.051263],[-7.236997,4.283067,-7.887081,-9.684062,9.067159,-1.552055,5.980501,-9.736025,-7.781519],[6.327136,-3.369562,0.790891,-8.742899,-8.824631,9.168031,1.495716,3.470162,0.406854],[5.379536,0.772360,-2.015716,-5.963582,-2.529431,-6.190918,-0.120315,-8.331173,-7.249861],[5.235426,-0.466069,-4.702089,5.116313,2.839571,1.432982,-6.011988,-0.319276,2.719000]],[[6.575139,-3.759077,-1.251305,0.389531,-8.242127,6.330533,1.020354,9.201358,9.466178],[8.457997,9.271100,4.584666,-4.109763,-9.757239,4.262680,5.983149,4.353918,7.571313],[-1.683110,-5.878333,-0.360906,0.916899,-2.701048,0.222655,8.963394,-3.643165,4.525792],[1.083348,1.053083,-7.374628,1.892806,5.813625,7.236958,6.470386,9.007791,1.392722],[8.093475,9.078067,5.139269,2.357520,-1.792703,-4.037481,-9.182661,5.602314,1.309273],[-2.914017,9.706629,7.140379,-4.962272,-3.019427,-7.203980,-5.656108,-5.420574,1.703704],[-8.129635,-9.180103,-7.660467,4.489552,-5.047048,-5.449418,-7.264244,7.790649,-3.167943],[4.745675,8.509579,8.028930,6.697141,8.460226,2.184630,6.512782,-4.681782,-1.718021],[-2.907601,4.434331,-9.006759,-5.548886,-1.173703,-2.843046,-0.720498,-2.551449,6.725670]],[[4.797439,6.445372,3.759157,4.354103,-2.511366,-9.351323,-5.050211,-5.677744,-0.445649],[5.941992,-8.090902,-1.561660,9.605294,-8.813655,-6.006826,8.432814,-5.257804,-2.450788],[5.596598,-2.463902,7.772396,7.539020,-4.115185,0.368868,-0.438879,7.859890,1.440867],[-9.423549,5.212964,-5.901227,-0.942349,1.116850,-5.541378,-5.959621,-9.116105,4.415701],[-8.385029,4.605178,4.950096,6.944932,-0.605136,-1.668902,-0.087713,-1.686951,5.914615],[0.643722,-0.103599,-2.153702,-3.286341,-2.391247,0.055686,6.885621,-7.575008,-5.906291],[9.667516,-0.021256,6.852162,1.566427,6.281580,4.112837,-7.250698,-0.258794,4.198983],[0.279167,-9.921444,-5.930483,-0.726638,8.991701,7.153914,-3.065505,3.795239,-0.223181],[2.021043,-1.824715,4.167140,9.754753,-9.430321,-4.207616,-1.126842,6.585325,8.567620]]], dtype = "float32")#candidate|10095|(15, 9, 9)|const|float32
bop_10096 = relay.floor_divide(const_10094.astype('float32'), relay.reshape(const_10095.astype('float32'), relay.shape_of(const_10094))) # shape=(15, 9, 9)
output = bop_10096
output2 = bop_10096
func_10099 = relay.Function([], output)
mod['func_10099'] = func_10099
mod = relay.transform.InferType()(mod)
output = func_10099()
func_10100 = relay.Function([], output)
mutated_mod['func_10100'] = func_10100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_10135 = func_10099_call()
call_10136 = func_10099_call()
output = call_10135
output2 = call_10136
func_10137 = relay.Function([], output)
mod['func_10137'] = func_10137
mod = relay.transform.InferType()(mod)
mutated_mod['func_10137'] = func_10137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10137_call = mutated_mod.get_global_var('func_10137')
call_10138 = func_10137_call()
output = call_10138
func_10139 = relay.Function([], output)
mutated_mod['func_10139'] = func_10139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_10239 = func_10099_call()
call_10240 = func_10099_call()
output = call_10239
output2 = call_10240
func_10241 = relay.Function([], output)
mod['func_10241'] = func_10241
mod = relay.transform.InferType()(mod)
mutated_mod['func_10241'] = func_10241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10241_call = mutated_mod.get_global_var('func_10241')
call_10242 = func_10241_call()
output = call_10242
func_10243 = relay.Function([], output)
mutated_mod['func_10243'] = func_10243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_10280 = func_10099_call()
call_10281 = func_10099_call()
output = call_10280
output2 = call_10281
func_10305 = relay.Function([], output)
mod['func_10305'] = func_10305
mod = relay.transform.InferType()(mod)
output = func_10305()
func_10306 = relay.Function([], output)
mutated_mod['func_10306'] = func_10306
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10307 = relay.var("var_10307", dtype = "float32", shape = (13, 9, 5))#candidate|10307|(13, 9, 5)|var|float32
var_10308 = relay.var("var_10308", dtype = "float32", shape = (13, 9, 5))#candidate|10308|(13, 9, 5)|var|float32
bop_10309 = relay.greater_equal(var_10307.astype('bool'), relay.reshape(var_10308.astype('bool'), relay.shape_of(var_10307))) # shape=(13, 9, 5)
var_10323 = relay.var("var_10323", dtype = "float32", shape = (13, 9, 5))#candidate|10323|(13, 9, 5)|var|float32
bop_10324 = relay.divide(var_10307.astype('float64'), relay.reshape(var_10323.astype('float64'), relay.shape_of(var_10307))) # shape=(13, 9, 5)
func_10241_call = mod.get_global_var('func_10241')
func_10243_call = mutated_mod.get_global_var('func_10243')
call_10339 = func_10241_call()
call_10340 = func_10241_call()
bop_10342 = relay.minimum(bop_10324.astype('uint8'), relay.reshape(var_10308.astype('uint8'), relay.shape_of(bop_10324))) # shape=(13, 9, 5)
output = relay.Tuple([bop_10309,call_10339,bop_10342,])
output2 = relay.Tuple([bop_10309,call_10340,bop_10342,])
func_10348 = relay.Function([var_10307,var_10308,var_10323,], output)
mod['func_10348'] = func_10348
mod = relay.transform.InferType()(mod)
var_10349 = relay.var("var_10349", dtype = "float32", shape = (13, 9, 5))#candidate|10349|(13, 9, 5)|var|float32
var_10350 = relay.var("var_10350", dtype = "float32", shape = (13, 9, 5))#candidate|10350|(13, 9, 5)|var|float32
var_10351 = relay.var("var_10351", dtype = "float32", shape = (13, 9, 5))#candidate|10351|(13, 9, 5)|var|float32
output = func_10348(var_10349,var_10350,var_10351,)
func_10352 = relay.Function([var_10349,var_10350,var_10351,], output)
mutated_mod['func_10352'] = func_10352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10137_call = mod.get_global_var('func_10137')
func_10139_call = mutated_mod.get_global_var('func_10139')
call_10379 = func_10137_call()
call_10380 = func_10137_call()
output = relay.Tuple([call_10379,])
output2 = relay.Tuple([call_10380,])
func_10401 = relay.Function([], output)
mod['func_10401'] = func_10401
mod = relay.transform.InferType()(mod)
mutated_mod['func_10401'] = func_10401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mutated_mod.get_global_var('func_10401')
call_10402 = func_10401_call()
output = call_10402
func_10403 = relay.Function([], output)
mutated_mod['func_10403'] = func_10403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_10415 = relay.TupleGetItem(func_10401_call(), 0)
call_10416 = relay.TupleGetItem(func_10403_call(), 0)
uop_10419 = relay.sinh(call_10415.astype('float64')) # shape=(15, 9, 9)
uop_10421 = relay.sinh(call_10416.astype('float64')) # shape=(15, 9, 9)
output = relay.Tuple([uop_10419,])
output2 = relay.Tuple([uop_10421,])
func_10426 = relay.Function([], output)
mod['func_10426'] = func_10426
mod = relay.transform.InferType()(mod)
mutated_mod['func_10426'] = func_10426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10426_call = mutated_mod.get_global_var('func_10426')
call_10427 = func_10426_call()
output = call_10427
func_10428 = relay.Function([], output)
mutated_mod['func_10428'] = func_10428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_10435 = relay.TupleGetItem(func_10401_call(), 0)
call_10436 = relay.TupleGetItem(func_10403_call(), 0)
output = call_10435
output2 = call_10436
func_10450 = relay.Function([], output)
mod['func_10450'] = func_10450
mod = relay.transform.InferType()(mod)
output = func_10450()
func_10451 = relay.Function([], output)
mutated_mod['func_10451'] = func_10451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10426_call = mod.get_global_var('func_10426')
func_10428_call = mutated_mod.get_global_var('func_10428')
call_10474 = relay.TupleGetItem(func_10426_call(), 0)
call_10475 = relay.TupleGetItem(func_10428_call(), 0)
output = relay.Tuple([call_10474,])
output2 = relay.Tuple([call_10475,])
func_10485 = relay.Function([], output)
mod['func_10485'] = func_10485
mod = relay.transform.InferType()(mod)
output = func_10485()
func_10486 = relay.Function([], output)
mutated_mod['func_10486'] = func_10486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10529 = relay.var("var_10529", dtype = "float64", shape = (13, 2, 3))#candidate|10529|(13, 2, 3)|var|float64
uop_10530 = relay.log2(var_10529.astype('float64')) # shape=(13, 2, 3)
uop_10536 = relay.cosh(uop_10530.astype('float64')) # shape=(13, 2, 3)
output = uop_10536
output2 = uop_10536
func_10539 = relay.Function([var_10529,], output)
mod['func_10539'] = func_10539
mod = relay.transform.InferType()(mod)
var_10540 = relay.var("var_10540", dtype = "float64", shape = (13, 2, 3))#candidate|10540|(13, 2, 3)|var|float64
output = func_10539(var_10540)
func_10541 = relay.Function([var_10540], output)
mutated_mod['func_10541'] = func_10541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10305_call = mod.get_global_var('func_10305')
func_10306_call = mutated_mod.get_global_var('func_10306')
call_10551 = func_10305_call()
call_10552 = func_10305_call()
output = call_10551
output2 = call_10552
func_10556 = relay.Function([], output)
mod['func_10556'] = func_10556
mod = relay.transform.InferType()(mod)
mutated_mod['func_10556'] = func_10556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mutated_mod.get_global_var('func_10556')
call_10557 = func_10556_call()
output = call_10557
func_10558 = relay.Function([], output)
mutated_mod['func_10558'] = func_10558
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10624 = relay.var("var_10624", dtype = "float64", shape = (10, 14, 4))#candidate|10624|(10, 14, 4)|var|float64
uop_10625 = relay.sigmoid(var_10624.astype('float64')) # shape=(10, 14, 4)
output = uop_10625
output2 = uop_10625
func_10628 = relay.Function([var_10624,], output)
mod['func_10628'] = func_10628
mod = relay.transform.InferType()(mod)
var_10629 = relay.var("var_10629", dtype = "float64", shape = (10, 14, 4))#candidate|10629|(10, 14, 4)|var|float64
output = func_10628(var_10629)
func_10630 = relay.Function([var_10629], output)
mutated_mod['func_10630'] = func_10630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_10796 = relay.TupleGetItem(func_10401_call(), 0)
call_10797 = relay.TupleGetItem(func_10403_call(), 0)
func_4293_call = mod.get_global_var('func_4293')
func_4296_call = mutated_mod.get_global_var('func_4296')
const_10807 = relay.const([-2.861744,-3.508294,8.137116,-9.053167,0.661792,1.784238,-9.540004,3.040414,-1.463670,2.738001,2.693168,-4.548560,-5.737576,-5.270143,0.424283,-3.617689,0.624114,7.052904,8.903425,-0.495916,-0.871009,-9.644979,-6.053931,-6.628777,-4.964108,-3.050638,-9.974283,-2.346896,5.429974,-2.165256,9.237662,9.124226,9.879687,-7.542483,-1.958748,-5.008938,-0.136877,-0.131333,-6.860043,5.210368,-3.311805,0.093701,8.794480,9.604511,-5.772683,1.228185,1.326839,3.530398,4.754301,3.558093,-9.737602,3.420089,-8.408625,-2.481908,-2.037573,4.453491,1.331639,8.393001,1.335660,3.010682,-9.875233,7.877386,7.083791,-9.344325,-7.278410,4.473881,6.912500,-2.814213,-4.038604,0.710260,-7.546063,0.063700,1.189826,-5.809813,-0.103679,-7.559347,3.293185,-5.480358,-8.982436,6.199830,-6.307177,-1.741300,6.421493,0.411745,5.730025,-3.169347,0.415896,7.710922,-8.390023,9.079395,0.158616,6.945353,-3.349941,-0.196115,7.689884,3.025049,-7.090161,9.305568,-2.066152,8.516313,2.950876,-9.144445,1.268867,1.443418,1.654221,-7.014672,2.127892,9.334110,0.595122,-5.792125,-5.932397,-0.142679,3.443874,-6.404461,-9.087035,5.881224,-3.460468,9.841882,2.801137,6.448237,5.583862,-2.141774,-0.927756,-6.947119,3.081058,-6.380193,8.931955,-1.828238,-8.829138,-5.411335,-9.060558,0.369492,1.801625,-3.701818,0.257686,-1.888938,-9.301340,0.796823,-2.091264,-2.767386,9.084437,7.621650,-8.732851,2.773883,4.879947,6.400277,-3.298827,-0.059280,4.196320,-6.799463,-8.410355,-7.379957,7.205538,1.428863,9.495278,6.221670,-9.187252,2.188848,-5.201011,-2.737627,2.617395,9.895480,-2.146113,3.753670,1.164450,-1.880890,-4.961039,-1.128785,6.785655,-5.768751,4.770669,5.177660,-3.134640,-5.225617,9.736172,-0.067971,8.574420,-1.285833,0.786657,7.564718,-1.970601,4.849102,-8.475311,-2.473488,1.176588,8.440441,6.684491,2.854892,2.287577,-3.595410,-0.219291,0.236316,6.769953,5.336045,-5.225998,5.957923,-7.651216,6.808364,-5.184339,-9.436245,-0.677366,-8.065800,-2.295638,-4.457147,-3.554917,1.609241,4.816444,-2.931782,-7.342733,-4.228958,-1.312957,3.966147,-9.519792,-8.856942,3.297191,-6.155831,-8.137534,9.705896,-1.975602,-0.638869,-9.454362,9.616418,0.424457,-6.960801,3.773346,-8.367908,-8.975472,0.769338,-8.760549,9.608695,-4.496215,-6.234931,2.930767,-9.138725,2.563219,-7.384823,-8.956201,0.592840,5.447990,1.706022,-7.668443,-2.301287,-3.732299,2.766617,0.035827,-8.831264,6.031916,-7.148261,-0.168056,-9.537829,-4.104751,4.560085,5.482092,-8.167495,5.499636,7.826285,6.887174,-0.540286,8.994561,-1.496050,8.669158,0.470108,3.445921,6.599137,-5.675374,6.115628,-7.967960,5.683716,-7.880912,-6.749261,8.998116,2.449762,7.753043,-8.073586,-1.058522,-2.758344,6.819386,-9.753531,3.129318,-9.504550,2.350570,-6.815292,5.108194,7.079808,9.873547,3.216008,-4.613857,6.461895,-0.962005,-3.586524,0.029495,-5.511831,-1.780263,8.713097,-0.734904,4.558901,-3.191886,8.657552,0.459960,4.821151,-4.920888,-0.016920,6.042727,1.707593,7.401636,-4.250679,-5.897877,-0.321430,2.132438,-3.236288,1.617984,-5.951484,-1.881765,2.903850,-0.965842,-1.588294,6.314698,2.700728,0.504597,3.570882,9.528132,5.408163,-0.815559,-5.686607,5.774817,-3.968257,5.664852,-7.068530,-8.857896,0.158294,-9.988961,-5.860521,-5.548262,5.653933,-4.996789,3.856606,-3.689529,8.498708,-4.314379,8.505883,-8.342537,-0.278312,-7.975590,8.194901,2.598961,2.456273,8.083510,7.511989,-0.203150,2.669608,6.260046,-8.296351,5.023055,1.936510,5.799036,6.817213,-9.976288,6.407775,8.226122,7.254459,-7.542162,-8.133174,-2.452545,0.043813,-3.675268,1.680959,8.467278,-9.513846,1.876552,-1.701370,-2.439853,8.073006,-9.071753,7.077153,0.687238,-0.676297,2.397778,8.568954,-9.231470,-5.877533,3.857860,1.240072,2.230530,0.085717,6.419676,-1.605124,-2.762500,-9.520312,-4.343723,-7.565527,-5.324259,8.884537,9.914733,-1.022350,-2.929459,7.540698,-6.623477,-3.777160,-9.296331,0.007949,-3.704125,1.255674,8.779030,7.689253,3.446683,8.602785,-8.880503,4.794002,-9.855506,5.979789,3.917208,-6.516023,7.893716,0.435710,3.756979,5.387021,-9.702658,-0.932283,-8.502223,-4.625906,8.153553,-0.490881,-8.514365,2.475592,4.289759,1.052070,3.818454,-8.686565,6.285594,-4.057199,-4.449033,-8.420136,-7.113662,-1.317803,-9.933800,-3.022407,0.341269,6.682410,7.271098,-4.788708,7.534403,4.008866,6.008030,-4.874445,8.299807,3.259839,-9.268541,4.363506,-4.942296,-8.256152,-3.837918,-6.032465,1.665778,1.497884,0.968209,1.268923,-2.993976,3.401240,-5.756135,-1.132711,0.138478,-4.759980,8.515049,-0.748870,1.306127,-6.655717,-4.577869,6.794854,-0.522799,-8.267523,-6.822079,-7.493471,-8.960075,3.556791,8.128705,-7.679360,3.828951,2.215063,-7.879004,7.657697,-4.860303,5.526874,-4.900722,-3.065233,-3.893058,-6.267457,-5.255959,5.149315,4.114763,1.634209,-4.769281,3.012420,-8.781403,-5.284942,-4.572625,9.753230,8.128665,8.305226,2.264137,-6.878906,-1.151777,0.979870,5.088417,7.107767,3.963011,-7.061207,9.345861,5.736851,-3.413351,-8.762874,3.880311,4.759241,2.786763,4.491513,-7.019231,-7.181073,-6.797159,5.671956,-1.983924,-1.567823,2.964661,1.451846,-8.377512,7.381393,-2.584804,-3.622101,3.016831,-5.414286,-9.782804,0.746523,5.322129,-6.765197,5.425825,4.344480,-2.230368,4.434638,-0.878952,-2.516944,-0.269615,1.567806,-0.589818,-4.188220,5.342391,-3.643533,-8.005795,-9.809330,8.926558,-5.842260,-6.472945,-8.769831,9.097843,5.316217,-5.837293,7.398176,8.073591,6.462827,-4.431756,4.654816,-7.821027,7.545728,6.170008,-0.468514,-4.871178,-4.319423,-6.081035,-1.785968,-4.740675,-4.460151,8.104728,4.733281,-7.794626,-6.228411,6.749067,7.987771,4.915726,-5.704132,-4.465564,0.836918,5.139860,-7.434586,-0.322205,-5.849612,-1.170258,0.652622,-4.718324,-5.122186,3.827231,0.135900,-1.724457,-5.408337,3.563131,-0.911790,5.175650,0.607979,0.547693,3.522212,-4.154182,3.134353,-5.844081,-4.514027,9.807266,9.636485,-5.048447,3.074300,1.436715,-7.214700,6.169208,2.350946,2.296075,0.229861,-0.327610,-4.458294,-1.183187,1.296211,8.356092,2.203777,-2.965980,5.890696,8.770644,8.262205,3.249969,-4.773045,-3.244265,7.554453,-6.819047,7.585713,1.193970,0.199017,5.629229,-3.901087], dtype = "float32")#candidate|10807|(630,)|const|float32
call_10806 = relay.TupleGetItem(func_4293_call(relay.reshape(const_10807.astype('float32'), [7, 10, 9])), 0)
call_10808 = relay.TupleGetItem(func_4296_call(relay.reshape(const_10807.astype('float32'), [7, 10, 9])), 0)
func_6813_call = mod.get_global_var('func_6813')
func_6816_call = mutated_mod.get_global_var('func_6816')
const_10820 = relay.const([-4.463287,-5.463985,-5.010778,8.261911,-4.141095,4.949901,-8.168863,-5.280037,5.576494,-0.535890,-7.663255,-9.832280,-5.068349,-2.760583,-6.302619,-6.930897,0.710846,-8.214913,-4.376270,-8.640628,-6.064403,2.194787,-7.338188,-3.441051,-1.007637,8.801643,-6.265283,6.789256,7.346526,-0.379768,8.240245,-1.186878,6.565286,-7.210278,-3.829628,-0.331580,-8.252879,0.607684,9.326101,1.547530,0.211483,-3.006705,-6.225877,-7.657836,-2.582394,-5.150128,-2.202679,-9.963636,9.830188,1.333336,1.352111,-0.402085,1.110695,4.495710,9.252949,5.278713,1.899373,-5.716919,5.527202,8.651575,1.392173,0.250144,-7.540834,-1.919126,-2.979742,-3.873107,7.283565,9.884523,-3.216881,-1.858337,6.002849,-4.423074,3.651697,1.489350,-6.800525,-7.473375,-2.629944,5.511957,-8.128749,-7.721130,1.189881,-1.558235,-4.232346,-8.294727,-4.287519,-6.889071,-9.250978,3.616291,-0.545590,-2.978995,8.036727,-9.367649,-4.734669,9.902677,1.835971,1.664437,-6.986092,-6.743943,1.840991,1.572661,5.436226,-0.461103,3.066657,9.258416,-5.290089,-6.797471,1.696412,6.478151,-8.960438,-5.547629,-0.710610,-9.962242,1.679944,5.233727,7.840071,9.566921,8.284275,-3.839592,5.478990,-1.693841,8.952920,6.144276,6.956206,-7.165783,9.697424,-3.195304,-6.882863,-1.587463,4.403602,3.430927,3.914287,1.406623,-2.399927,2.447717,7.727970,1.583487,-3.607995,7.049216,2.926497,1.183897,-2.206374,-1.069511,-4.014151,5.181481,1.646174,3.221529,4.840992,0.262068,-8.491015,0.468778,-6.793385,4.772606,5.672351,-9.244600,-9.452802,-4.213217,0.345917,-2.268353,1.495643,5.992484,-2.702108,6.199204,5.673619,5.672555,7.174049,-9.344877,7.794430,-4.687181,-8.095875,4.625310,-7.658578,-3.162755,-4.916309,-5.861663,-3.230565,-7.994838,-2.267552,-2.642889,-8.412368,8.294279,-1.650943,2.477791,6.858163,-7.833253,1.544423,1.762963,3.576587,4.677332,-6.896373,-4.410195,-1.023004,0.966365,-9.650226,-8.915316,5.949088,0.096305,4.347417,1.015749,-0.950682,1.660416,0.879706,-1.523155,-4.165643,-1.519111,0.297017,0.379187,-7.838928,-1.361189,-1.184084,6.401635,-7.583095,8.964737,-8.871999,6.194345,-7.250845,-7.469894,0.226168,7.431620,-8.581876,-1.656870,-1.389069,8.085736,-1.134470,4.959153,2.487133,-8.197786,9.819276,9.096808,-0.336961,9.021441,0.965192,-5.489253,-8.730764,-6.761238,1.385346,-6.213180,-5.243884,-3.433127,3.749358,6.304919,0.795794,-2.537069,3.282124,-8.371309,-5.063762,1.464417,0.153608,-3.171730,0.331266,-4.180358], dtype = "float64")#candidate|10820|(250,)|const|float64
const_10821 = relay.const([-5,8,3,-9,-7,-9,-1,5,9,1,-6,-8,-10,-9,-10,-7,-7,-8,-2,-5,-5,-3,7,6,-7,4,9,-4,-1,-7,3,-5,-1,-3,1,-2,-4,-1,-5,9,-5,-9,-4,-5,-8,-5,6,-1,4,10,4,10,-10,-1,1,9,2,4,1,-3,2,9,-10,7,-6,9,-10,8,-1,7,8,8,5,7,1,-6,10,1,8,3,-6,6,1,-5,4,4,9,-3,4,-2,-2,8,-4,3,8,7,-8,9,8,4,8,-3,10,1,6,10,10,9,8,7,7,1,7,-7,-6,7,8,10,6,1,3,-7,9,8,-7,7,-8,-1,10,10,-8,-9,4,4,1,1,7,8,5,7,-8,10,-3,-1,-9,-1,5,-5,9,1,7,3,-2,-1,-4,3,-3,10,-3,2,-9,3,1,6,-9,10,-1,-9,-4,1,1,2,8,3,-10,-5,6,-6,6,-8,9,1,1,-4,-4,-2,1,-10,-3,-10,8,5,-3,-2,1,6,-10,-1,-8,-7,-9,7,3,9,-10,3,4,1,-7,6,3,-9,8,-3,6,-1,8,-7,5,9,6,-3,-9,6,7,3,2,4,-3,-8,-8,-6,-5,9,10,7,-1,-4,5,6,2,4,3,-5,7,-7,-10,-1,-5,-9,10,1,-6,-4,7,-3,-9,-2,-6,-1,10,-8,-1,9,3,5,4,7,-10,-1,10,5,-2,2,-8,3,-2,-2,1,-3,1,-8,-1,-5,7,-2,-9,-6,6,10,-2,-3,3,-9,7,9,-7,3,3,3,-3,6,-1,-4,10,-2,5,9,9,2,-8,-5,9,7,7,3,2,-3,-2,2,1,8,-9,5,5,-5,-10,9,10,3,-5,-7,-8,2,9,5,7,-7,-10,-6,10,7,-4,1,-4,1,-5,-6,1,4,-3,-10,-10,-9,-9,-5,-8,1,1,-8,-10,-2,-7,7,-8,8,8,4,-6,10,9,6,-10,-9,-1,-3,6,-4,-8,1,-2,9,-8,9,5,-1,5,-2,-4,-5,8,6,7,-6,-2,1,7,-1,-5,1,10,-4,7,1,9,-8,3,-2,3,5,7,7,-8,-1,1,-2,-1,-7,2,-2,3,7,-2,-6,7,2,9,-7,10,-7,9,-3,6,1,-9,9,10,7,7,1,-7,7,4,3,4,-6,-9,-3,8,-5,6,-8,1,10,-3,3,6,5,6,4,10,-4,9,-6,-1,4,6,-4,9,7,7,-1,-10,4,6,7,-10,-5,-8,5,-3,-7,-5,7,4,-6,-4,7,7,1,9,-9,10,-7,-6,-10,-5,7,-7,-4,10,4,-10,9,2,1,9,2,6,2,4,-1,10,-1,-4,-7,-8,8,4,5,7,-9,8,8,1,-5,3,-5,8,7,2,6,-9,-8,-10,-10,9,-3,-9,2,-2,-4,-7,-7,7,-4,-10,-9,-5,-3], dtype = "int8")#candidate|10821|(550,)|const|int8
call_10819 = relay.TupleGetItem(func_6813_call(relay.reshape(const_10820.astype('float64'), [5, 5, 10]), relay.reshape(const_10821.astype('int8'), [550,]), ), 1)
call_10822 = relay.TupleGetItem(func_6816_call(relay.reshape(const_10820.astype('float64'), [5, 5, 10]), relay.reshape(const_10821.astype('int8'), [550,]), ), 1)
func_550_call = mod.get_global_var('func_550')
func_555_call = mutated_mod.get_global_var('func_555')
var_10841 = relay.var("var_10841", dtype = "uint32", shape = ())#candidate|10841|()|var|uint32
const_10842 = relay.const([-2,-8,-9,-5,-9,10,-10,9,-7,-8,5,-1,9,-5,4,1,-5,2,-10,-8,10,3,9,5,9,6,-7,2,-8,10,-9,10,1,-7,-7,-2,-2,-8,10,-9,-7,3,-4,9,-4,-4,3,4,-5,7,-7,-2,-7,-2,-2,-6,-5,-2,-3,-1,-1,7,-10], dtype = "uint32")#candidate|10842|(63,)|const|uint32
const_10843 = relay.const([[8.930930,1.755037,4.588576,-2.477428,-8.105783,9.526922,-3.858874,0.048083,-6.993811,-2.176300,-4.117041,9.013319],[6.705323,0.913159,6.703981,-0.128975,-7.419881,7.009978,-9.880365,3.434954,1.438626,-2.373959,7.067409,-3.801925],[-7.895007,4.482836,3.943263,-4.654177,-6.748493,-2.255871,-4.008455,-1.253932,-3.079329,3.203179,-9.404550,-2.948095],[3.012634,5.254401,-4.847778,-2.436734,-4.978931,-9.059771,-8.252197,-9.686216,-1.465442,-3.194623,8.534574,-1.773767],[-0.429299,4.874063,-5.830914,-0.504895,-1.274097,6.938635,4.687507,2.111067,0.307421,1.073431,-8.471706,-8.275572],[5.821882,-6.239957,-7.832673,-8.847391,-0.841316,5.212041,6.407634,-8.137872,3.196961,3.123204,9.311395,6.303284]], dtype = "float64")#candidate|10843|(6, 12)|const|float64
call_10840 = relay.TupleGetItem(func_550_call(relay.reshape(var_10841.astype('uint32'), []), relay.reshape(const_10842.astype('uint32'), [3, 7, 3]), relay.reshape(const_10843.astype('float64'), [72,]), ), 0)
call_10844 = relay.TupleGetItem(func_555_call(relay.reshape(var_10841.astype('uint32'), []), relay.reshape(const_10842.astype('uint32'), [3, 7, 3]), relay.reshape(const_10843.astype('float64'), [72,]), ), 0)
func_10539_call = mod.get_global_var('func_10539')
func_10541_call = mutated_mod.get_global_var('func_10541')
const_10869 = relay.const([4.861520,-8.494621,1.946006,-9.660692,4.417423,-2.408866,5.117457,-9.723658,9.179800,-3.263505,-9.657151,-9.100915,-0.670955,6.158008,7.250524,1.184403,-3.418114,5.653706,7.375763,5.537445,1.667764,-4.150756,-5.238522,3.150157,6.964039,6.388828,-6.062963,8.189979,0.630975,-6.646643,-3.108672,9.237964,-6.733010,-5.129620,0.148218,-6.343510,-6.627785,5.677838,-3.239561,-1.315052,-5.353078,0.119161,9.064926,4.028915,9.100620,4.832931,1.611571,3.880272,6.530568,-9.944088,2.575178,6.788536,4.989302,-8.167050,-2.007933,6.058044,6.018496,9.186149,-4.413664,7.049795,2.164177,7.940888,6.680627,-8.934887,-0.653906,2.244729,5.151779,3.739642,2.847914,-3.571500,-4.657470,-7.482469,4.940133,-8.617732,7.018295,1.977135,1.340370,2.374456], dtype = "float64")#candidate|10869|(78,)|const|float64
call_10868 = func_10539_call(relay.reshape(const_10869.astype('float64'), [13, 2, 3]))
call_10870 = func_10539_call(relay.reshape(const_10869.astype('float64'), [13, 2, 3]))
output = relay.Tuple([call_10796,call_10806,const_10807,call_10819,const_10820,const_10821,call_10840,var_10841,const_10842,const_10843,call_10868,const_10869,])
output2 = relay.Tuple([call_10797,call_10808,const_10807,call_10822,const_10820,const_10821,call_10844,var_10841,const_10842,const_10843,call_10870,const_10869,])
func_10879 = relay.Function([var_10841,], output)
mod['func_10879'] = func_10879
mod = relay.transform.InferType()(mod)
mutated_mod['func_10879'] = func_10879
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10880 = relay.var("var_10880", dtype = "uint32", shape = ())#candidate|10880|()|var|uint32
func_10879_call = mutated_mod.get_global_var('func_10879')
call_10881 = func_10879_call(var_10880)
output = call_10881
func_10882 = relay.Function([var_10880], output)
mutated_mod['func_10882'] = func_10882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_10922 = func_10556_call()
call_10923 = func_10556_call()
output = relay.Tuple([call_10922,])
output2 = relay.Tuple([call_10923,])
func_10933 = relay.Function([], output)
mod['func_10933'] = func_10933
mod = relay.transform.InferType()(mod)
mutated_mod['func_10933'] = func_10933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mutated_mod.get_global_var('func_10933')
call_10934 = func_10933_call()
output = call_10934
func_10935 = relay.Function([], output)
mutated_mod['func_10935'] = func_10935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10426_call = mod.get_global_var('func_10426')
func_10428_call = mutated_mod.get_global_var('func_10428')
call_10936 = relay.TupleGetItem(func_10426_call(), 0)
call_10937 = relay.TupleGetItem(func_10428_call(), 0)
output = call_10936
output2 = call_10937
func_10945 = relay.Function([], output)
mod['func_10945'] = func_10945
mod = relay.transform.InferType()(mod)
output = func_10945()
func_10946 = relay.Function([], output)
mutated_mod['func_10946'] = func_10946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_11075 = relay.TupleGetItem(func_10485_call(), 0)
call_11076 = relay.TupleGetItem(func_10486_call(), 0)
output = call_11075
output2 = call_11076
func_11088 = relay.Function([], output)
mod['func_11088'] = func_11088
mod = relay.transform.InferType()(mod)
output = func_11088()
func_11089 = relay.Function([], output)
mutated_mod['func_11089'] = func_11089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11098 = relay.var("var_11098", dtype = "int16", shape = (14, 7, 13))#candidate|11098|(14, 7, 13)|var|int16
var_11099 = relay.var("var_11099", dtype = "int16", shape = (14, 7, 13))#candidate|11099|(14, 7, 13)|var|int16
bop_11100 = relay.less(var_11098.astype('bool'), relay.reshape(var_11099.astype('bool'), relay.shape_of(var_11098))) # shape=(14, 7, 13)
func_3701_call = mod.get_global_var('func_3701')
func_3706_call = mutated_mod.get_global_var('func_3706')
var_11105 = relay.var("var_11105", dtype = "float64", shape = (195, 2))#candidate|11105|(195, 2)|var|float64
var_11106 = relay.var("var_11106", dtype = "uint32", shape = (63,))#candidate|11106|(63,)|var|uint32
const_11107 = relay.const([-9.812584,-7.894459,-7.796119,-4.237634,4.657266,-5.873120,3.987519,-9.449389,-4.517240,9.032466,4.049479,-4.825890,6.467136,-3.349340,1.141127,-8.143236,7.272945,-7.706973,-9.628127,7.667708,0.723365,0.536965,6.316167,-4.408552,-5.318867,-6.045111,-6.345561,-2.086964,3.854206,-6.829101,2.605190,-7.870585,1.830467,4.664525,8.132365,3.346198,-4.717389,-9.986969,-5.274596,1.277331,-7.587370,8.216051,-1.437540,-4.758011,-1.443823,7.695886,4.390132,-3.686064,-3.229815,-5.116448,-1.077987,-4.940896,-3.245742,1.153368,-2.623019,3.875604,-8.030890,7.115585,-4.385853,-8.329718,-4.043550,5.786633,-0.885211,7.398215,8.945523,-1.787425,0.257743,-9.843878,6.792262,2.837860,-7.060472,-0.278747,5.021127,0.284000,8.168750,-9.072686,6.499443,4.316023,9.649724,4.834838,-6.415563,8.284077,-1.675371,6.960943,6.909791,0.491514,-7.055620,-3.373501,8.102379,6.426899,-0.590325,1.099063,4.538485,7.126693,2.026553,4.136307,-6.148703,1.016336,-5.790874,0.417946,9.008962,3.468506,-0.729454,6.120098,-7.259865,6.008767,-4.401361,-2.959450,7.365292,3.905120,-7.780313,2.975073,0.272839,-5.661277,8.110184,6.669879,-7.809560,-4.510961,-8.917549,5.188774,9.290690,6.567101,0.006414,3.882542,1.067766,3.116411,-8.695381,0.302807,7.209659,4.939038,7.050479,-0.862640,-5.119691,-2.214847,-4.843263,0.716040,-0.399260,-0.178303,-6.111635,2.909909,-6.674288,-6.118622,1.719937,-0.693521,2.025007,1.581997,-7.700162,-7.848275,4.548028,9.128268,-8.760983,1.572542,-1.664549,-9.361665,6.053175,-1.432139,-4.665836,-4.422074,-8.298494,2.165734,9.915302,-8.660448,-2.821678,-6.691075,-5.247509,9.183833,-7.917611,6.505136,-7.633198,3.917992,7.954740,1.099900,-0.834152,6.497635,-7.905086,-9.752600,-7.986539,6.261584,-6.300147,-2.019864,-5.530028,6.773114,-1.715881,7.037115,4.802644,-6.651643,-4.575115,-9.204457,-6.130874,-4.595339,-8.940153,-6.401415,4.538836,0.143970,2.714935,-2.120109,-8.691399,-7.737139,5.868906,1.627192,-7.694347,0.090524,-4.618099,-6.011502,-0.868618,3.897255,5.098101,2.733888,-3.790906,-0.469112,-0.114017,5.443237,4.003458,0.634306,9.975619,2.278247,-9.568740,-5.379092,-2.059186,2.567277,4.332285,-9.387819,-4.698176,-4.168676,-8.592119,-3.659628,7.180385,4.471216,9.590468,5.637769,-3.281217,4.269732,-9.813647,1.596252,-1.072041,3.549331,2.876843,-4.839613,7.983863,-7.929550,-9.634653,-1.635138,-9.007938,-5.372617,-1.536484,-2.011996,-8.772109,3.069565,-5.670438,7.779622,-6.034193,-7.067788,-4.569258,4.873042,4.816100,-2.182403,3.713471,-4.569320,-1.025531,3.602730,-5.531194,7.549981,5.801941,3.412272,4.611795,-2.371485,9.865377,-7.878310,-7.679312,0.021292,8.279362,2.059682,-3.889403,9.345700,-5.672885,3.555108,-2.323944,4.212433,-6.631001,6.088994,0.821726,4.850048,2.455362,6.474047,8.380997,4.106118,-8.956955,9.472837,-1.734711,9.671975,-9.708999,-1.020641,-8.034315,-9.930334,-7.526693,-2.531307,-3.667513,7.646742,1.370732,6.597477,2.551503,-7.488325,9.526286,2.693400,-8.348949,-1.115797,7.068535,5.331632,-1.814161,-5.720544,-3.745442,-7.521764,-4.584125,-2.171714,-9.985097,7.837422,-2.086720,9.625704,7.982290,-3.501719,-1.902590,-6.259652,8.764869,1.278505,-2.424928,-0.609927,-2.045516,5.128130,-7.583183,7.911472,3.382205,5.331831,-4.331548,2.812479,4.307351,7.896511,-7.847778,5.150996,6.180085,6.261427,8.478208,-3.154353,-7.156229,-0.037977,9.916639,-9.254471,-6.994391,1.878497,-4.637306,1.932030,-5.743698,1.721561,-3.221119,-8.550351,5.131755,3.780978,0.970432,9.317108,5.612039,0.064856,7.094572,0.413483,4.609592,-5.166508,4.891153,0.470764,-3.159374,-2.100745,7.665743,-4.997628,-5.666460,8.576337,-6.159320,-9.945150,9.453593,-4.641931,6.321364,-6.631697,-3.408932,-8.418780,-1.009724,5.765620,2.706186,-9.988690,-1.677561,7.603107,-1.787254,9.251483,1.631225,4.670015,1.549087,0.373709,0.525427,2.210881,-2.284290,-4.052562,0.531588,2.771145,3.460351,6.638795,0.611165,1.951127,-7.142883,-6.775738,-0.752548,-9.751069,3.591222,-3.516569,8.522878,3.094431,5.268754,5.173009,9.098771,4.105264,-1.664011,6.016503,-2.195407,2.462717,0.622937,-7.616360,6.037686,3.593555,2.000417,-7.238382,9.657699,-4.826733,7.447525,9.415191,7.213076,1.744774,3.852866,3.874204,2.659778,-9.455598,-4.211963,-1.378082,4.560840,-9.966346,6.352589,-3.331446,-6.771234,-0.337932,-5.942778,7.802257,-1.419492,7.686349,1.167441,2.925032,5.695691,7.461745,1.071170,-8.625639,4.966624,3.741717,2.796785,5.641218,-2.640559,9.468610,3.279183,-6.568339,9.870617,2.354413,-5.294318,-2.472951,2.055499,2.568108,1.868744,5.653317,8.075705,-9.796766,-1.497477,-2.856610,9.605495,8.637464,-5.148543,-9.247571,3.469750,-9.630880,8.606390,-5.598825,-6.585069,0.647258,4.892077,-9.372671,8.746147,3.659776,-3.319572,-2.954628,8.482181,-1.000004,-8.369861,8.134329,2.388735,6.758961,-2.942963,0.985190,-2.871614,1.605374,4.382335,-5.454311,-0.763224,9.810502,8.892802,-2.786144,6.810310,4.115143,8.980634,-7.700808,-3.453901,7.077123,4.789716,-4.010100,4.661796,7.563302,9.541545,5.348764,3.330593,4.897159,1.301765,9.743552,-3.674691,-2.768203,6.365341,-4.191662,-4.075840,7.334889,-6.570147,9.002981,7.804571,0.984754,-2.853011,-4.791730,9.808919,5.411840,1.070342,3.198278,6.089293,1.645602,-2.529068,-5.070102,-5.237284,-7.345125,7.195250,-0.083814,-7.798572,-5.158476,1.621635,-5.734767,-0.613242,6.070336,-3.260232,9.374902,-4.052270,7.161952,8.896310,3.883063,0.017530,-1.616055,-1.313395,3.474564,-8.732530,7.469591,-7.108689,-6.652086,7.027372,-7.701758,1.325091,3.066418,-6.727895,-2.278599,2.477110,8.986836,-8.387259,9.415692,2.705005,6.379753,-4.763611,9.580441,9.101936,9.806208,5.114011,-5.684445,-1.934992,-7.786930,-6.242248,-1.477680,-4.955317,-0.776591,6.569505,7.985567,-9.820336,5.528393,-5.606200,4.402195,-1.649432,-0.045110,-7.828441,-9.447648,5.546226,-9.939558,-3.653875,3.245575,-7.492616,9.712624,0.526378,-5.007561,0.811737,9.487126,-2.980675,2.063595,4.188089,-8.921165,8.574587,-2.732183,2.859956,-2.997142,8.197916,9.000639,-9.602671,-5.503281,0.451184,5.313896,-8.660632,-1.524731,-8.706803,6.853292,-4.273247,9.583065,5.750957,-6.548023,-9.195948,-2.922961,-9.448803,-4.406450,-5.917637,-8.425127,5.060986,-5.760648,-9.045247,9.687270,3.255963,5.739829,-4.963386,1.109883,-8.831787,4.713619,-1.458721,2.673124,9.333309,9.896693,-4.578094,5.058256,-7.627531,2.260469,7.213521,7.354933,3.625149,-0.025115,0.604705,5.190940,8.061493,9.510241,-5.028992,-5.766100,-7.421238,2.528669,2.545778,-9.046855,8.364525,9.941922,-8.203020,0.843583,7.361316,-7.954728,2.636832,-1.443423,-2.010621,-8.696629,-9.821680,-0.473666,6.923805,8.078563,-0.984273,-0.672229,6.572763,-9.215689,-2.367981,-0.347125,3.581081,-0.351023,-2.901851,0.066494,-0.078880,-0.105166,-6.293163,7.381842,-8.905311,0.655794,6.399735,-5.663387,6.847841,-1.336152,-3.100979,1.040262,3.605559,-2.141350,-5.583035,-9.114637,-6.120519,-2.855315,4.687903,-8.117345,-9.118660,5.742112,3.917846,1.040149,-9.560863,-7.600960,-9.570979,5.755772,2.431174,9.464274,1.651913,3.598480,-5.203413,3.863328,3.583927,-4.917787,2.061246,1.029839,3.144125,3.437252,2.620501,5.715920,3.438495,6.125890,-4.753667,-7.100649,3.517222,9.713946,6.396147,1.851883,-4.078050,9.947815,3.473417,-7.628900,4.248446,3.663334,3.272921,-6.094113,7.526259,-1.011833,-4.249732,0.383210,-0.252680,-4.360976,2.283954,-3.641679,5.835026,3.997933,1.695680,8.143794,7.049822,0.115932,8.929684,1.263988,8.366104,5.673852,4.912261,9.846868,6.467085,9.314851,-2.112473,1.882466,0.607027,-3.834162,-9.100571,0.120106,-2.829271,3.792913,-1.606378,-1.419529,-1.398878,-2.995188,0.867295,2.073892,5.472146,5.811817,-1.870831,6.098522,-4.139340,-0.826721,7.091504,-3.974695,-6.642660,-7.878355,5.806154,4.786843,-4.939851,8.432539,0.602308,-4.121465,1.315854,-5.913022,-5.940128,-2.275970,-5.406858,-3.081811,-9.445633,2.397447,-0.910504,-1.818386,4.808628,8.861504,5.289435,7.051102,5.834531,1.178966,9.180712,-2.698890,4.796014,-0.313361,-8.187117,4.261426,-1.966770,4.097084,-9.835954,-9.089469,8.764725,6.110949,-5.447955,-0.394577,7.148256,-2.314950,7.062558,-2.794107,3.006937,-7.339060,2.104488,1.396328,1.239757,-3.263160,-7.290330,3.206088,-0.127316,-2.520530,8.097876,-8.901022,-3.283722,7.562735,-2.741139,-4.901048,2.756670,8.249896,-8.618415,-7.592940,9.184682,-5.689886,6.904569,-9.410220,-1.337683,-2.791519,7.179928,-6.452263,1.599697,3.299548,-9.959483,-6.643938,3.097227,-9.222744,-2.276587,3.370571,-6.705538,6.144091,8.649174,9.402260,-9.609417,1.226403,7.335983,3.994580,2.631127,-4.987068,-7.794774,6.520631,-9.941598,0.698907,-3.396694,-6.089470,-1.132938,-7.345505,1.138012,-8.094728,6.710747,9.276815,5.338376,-9.185283,-9.780312,-4.920574,6.183028,-6.473270,-3.394669,-4.906525,-1.750681,1.806828,-2.148246,-3.153142,1.869002,9.727504,-2.650634,2.741651,2.872674,-9.200687,-6.961942,-9.101366,6.657118,1.027755,-2.240510,-7.038854,5.774403,-3.917101,-3.275240,9.959972,0.011530,-5.935620,-0.010933,6.948136,1.557876,5.012673,7.211026,4.500085,-0.200627,-4.000588,-0.258643,0.681715,-1.002422,8.806248,-2.634368,-5.590267,3.018482,2.987496,3.552979,6.382442,-5.614979,-1.682790,-8.232376,-4.773233,6.268889,-2.230267,-3.457946,5.363823,2.292777,8.172977,9.871329,9.202930,-0.549044,-3.986601,5.401495,6.399897,-8.404893,5.709009,1.090876,1.848712,-5.451630,6.826992,4.304676,9.524683,1.632971,-4.254426,2.547075,-7.947796,-4.820325,0.978166,-7.982467,-6.354905,-8.383698,-5.677822,8.688752,-2.628319,2.357348,-7.715301,-6.910921,5.753220,-4.816790,5.112457,4.044042,-2.679900,-4.553237,6.217394,-0.799978,-9.107823,-6.075164,-4.147000,-2.503678,4.736397,-0.526841,9.714827,-4.125363,6.539185,-7.053814,-7.009431,-2.805541,-0.452632,-0.937454,9.134583,0.827191,2.300780,-7.541461,4.644254,8.884594,-1.117876,9.628389,-3.914249,-8.677027,-9.594993,-2.877133,-3.315676,4.485522,-1.146944,1.887517,-5.826777,9.829222,-7.638847,-4.286195,-7.863650,-4.367614,8.664816,-7.452468,0.659114,8.978070,-6.588672,-2.345587,-2.617011,6.096868,6.649465,9.641874,7.073030,-8.789096,-2.831319,4.472947,-9.001804,-6.799485,2.657090,8.437682,4.971794,3.106026,1.934905,5.458538,3.211914,-3.194597,5.885003,3.422412,-4.774250,-1.225805,-5.052979,8.492878,5.671316,-9.481659,3.478530,-0.361378,2.066539,-5.325626,0.579202,-1.772086,-0.249870,-8.295096,-5.872356,-2.980445,9.267934,-5.331580,-0.695879,-3.634351,6.082919,7.682994,-6.781185,8.785221,3.069156,-7.942417,6.250123,6.993775,3.246673,5.029227,9.911484,-6.426632,-9.477552,-2.462868,6.311966,9.467346,-4.854663,1.572977,-2.365586,-6.837196,-2.485181,-0.189224,3.612991,3.819498,9.542035,3.652821,-7.217286,6.735058,-5.967603,6.109296,-2.512444,-4.383079,4.351460,-2.076076,-3.092540,1.293706,2.487675,7.862226,-1.359612,-8.267356,7.371252,-6.829480,5.471076,9.186426,-9.439911,3.196772,6.189795,5.667241,4.903125,-0.080307,-2.491088,-9.098034,5.093098,-5.823526,-7.649016,-6.724021,-0.922536,1.273353,-0.875856,2.136386,-0.310278,-1.058617,-5.565360,-0.280393,3.992520,-6.821939,7.833706,3.989511,-0.716984,-3.472978,-4.118061,-3.060959,1.746471,1.769834,-3.234072,-0.164447,4.910090,-3.985364,-7.758225,-3.332078,7.597916,8.594067,2.044090,-1.466183,2.045652,9.517532,0.715351,-2.082296,1.004265,-6.325647,9.829461,-4.880789,0.687831,-9.129689,-3.035234,0.180786,0.149567,-4.883131,-5.336601,-6.407518,9.111605,4.596851,-7.777542,9.791449,2.600280,7.053696,9.447478,-0.421501,1.402936,-8.398600,1.881652,7.287436,1.945795,5.980889,-0.127745,2.326178,2.045006,-5.447842,-0.355800,-0.581389,-2.303270,-1.062176,8.998465,-7.223748,-6.377455,-0.030937,3.354142,-1.874735,6.722630,-3.082558,-3.059062,8.554005,-0.986848,3.633946,-4.706109,7.990208,3.643531,-4.407353,-1.548758,9.168489,3.278551,-4.685062,-8.629855,1.745887,-4.619067,2.153505,4.747949,4.012166,5.056245,1.143090,-0.239617,-3.755161,-4.401339,-0.265888,4.571456,5.154687,-9.616585,7.224737,9.771128,-3.032028,-0.891461,-5.369653,5.583114,-4.078829,-2.951091,-0.372400,-8.347842,-8.443663,6.271265,6.935938,6.929109,0.173096,-2.677767,-3.188197,-3.743252,7.595646,-8.994820,-4.554090,9.870859,-8.393498,-8.342946,-1.643495,3.607234,-2.740574,-3.313030,-9.884084,-0.181574,4.556435,-8.497718,-6.210776,-2.838508,-7.920556,0.109483,-0.568193,6.568408,-9.077663,1.092254,-3.935226,-9.228580,4.305328,-2.408517,-8.579817,-9.168051,3.944230,8.298572,1.855565,0.448345,-7.660502,-7.352201,-5.781497,-7.123804,-6.527584,1.388546,-4.509817,6.492149,-7.220896,8.787171,-5.103938,-6.976091,5.867268,-9.235792,-7.881813,-3.466884,-8.315522,1.078600,-7.820182,-4.660923,-8.724707,3.053382,5.853589,-9.965829,-9.146431,-9.608992,8.741616,-8.646659,-3.622835,6.294268,-4.798497,4.306081,0.468566,9.288963,-3.340859,-3.117317,-4.158543,-4.102143,-7.877637,6.589527,-5.217631,5.255590,3.348384,-8.171807,-3.533775,-6.919921,4.633303,-2.770692,-2.876081,-3.721275,6.772152,0.864020,-3.315688,6.904415,8.131442,3.648910,-8.852412,4.943244,-4.448798,1.093814,-6.931632,-2.310010,5.724142,-1.785697,-6.641315,6.429399,1.809775,8.253157,-0.158121,-4.824112,-3.634760,3.835787,-6.833291,-9.096973,6.698044,-1.133062,9.142434,7.440936,9.589843,-9.825126,2.049267,0.116156,3.625266,-8.611886,3.134784,8.557640,6.516869,-6.162587,0.979048,-8.515881,-5.895204,-0.220125,0.333431,-6.177052,4.652372,8.211554,-6.341140,0.776602,3.796147,9.415971,-7.408814,-0.525389,-6.930075,-6.504534,9.839738,-5.678073,3.765868,9.762264,-0.091125,8.171925,6.838988,-4.872133,9.673523,2.346264,-0.634654,4.162953,2.079195,-7.625562,-3.698342,2.235145,8.318805,3.430044,1.845460,-6.793177,-4.287900,0.978834,-2.614583,-8.324189,-3.356003,-4.186836,-8.360838,6.063060,-7.933617,0.747412,-4.739243,-1.950646,-1.815820,-7.228983,0.613894,-1.556690,-4.148192,6.548575,1.596655,-6.887454,8.968534,-5.734727,-6.309825,8.171224,1.660510,4.545665,4.740060,-8.479325,5.541078,7.643284,4.789480,4.066406,-1.739278,-3.465915,-8.838720,4.207359,2.052618,9.755592,0.494363,-2.507951,-3.454592,5.184253,-9.722476,3.588055,-3.543267,-7.614951,-4.445226,-1.298081,-9.984330,9.225117,7.299346,-5.746563,-3.410497,7.839717,-5.401792,7.951653,2.045288,-8.783235,-8.081872,-8.346416,3.895134,-3.662724,-0.647957,-4.335357,2.308690,1.308840,-9.729328,1.694616,4.250133,-1.410319,5.500436,-9.020552,-7.326324,-0.916398,7.229860,-0.443101,4.905545,-7.457581,3.677653,-0.843084,-9.693998,5.611729,6.421233,-2.508628,5.174998,-4.184952,-5.395259,-4.109010,8.923722,5.878035,6.835079,1.821807,-3.934506,-9.291150,-1.593272,-1.898825,-6.327158,3.111729,-9.608673,-5.990817,8.874786,-4.703772,-3.952521,-4.449269,1.293352,-6.029564,9.103346,0.508767,9.847390,7.356149,-5.819091,0.837300,-9.743576,-4.644883,-9.750138,-8.132053,3.320970,6.364357,7.004180,-1.866053,6.348176,2.070415,-4.300439,-0.460384,-2.788551,-9.621301,4.553278,4.801537,-4.705453,-3.206745,6.415442,-0.813001,-3.392053,-9.983348,-1.598868,-1.440206,3.670222,-3.054758,9.430278,0.531716,8.571788,-5.501631,9.010281,-6.050460,-5.421874,-1.464431,6.240300,-9.918877,-7.466317,-3.467366,1.867537,-3.762152,-9.264026,3.961889,3.303811,-0.081306,-0.038700,5.079845,-8.633811,2.972075,8.311716,-6.609286,8.908838,-0.811344,6.136305,-6.075475,7.848559,7.462975,2.158921,0.696826,-3.255867,6.670385,5.972829,-3.542611,-5.228656,-3.983443,-9.773686,8.190927,0.723549,9.734090,-2.483935,-7.785561,2.721506,2.265795,-7.519105,2.677076,-5.782119,3.581271,-9.566252,-4.585420,3.388624,-1.908221,3.229499,4.734632,3.052971,-4.690718,-1.361222,1.045428,-6.216839,0.383263,-7.542112,6.864360,7.141935,-6.663113,7.281811,1.168928,2.686828,-4.192886,0.561176,5.520711,-3.232908,-3.437825,-5.930219,-8.978591,-4.614472,6.944947,4.018216,-8.509482,7.768483,-4.791589,3.763448,-2.777636,5.834785,9.848793,-4.744160,3.837402,-3.762617,-6.022184,9.730083,-4.520708,-9.538403,-7.955866,-6.582029,-4.555433,5.400363,-7.258556,-9.453539,8.988167,8.988509,-4.163838,-7.468023,3.558352,8.180147,3.293335,-3.493287,2.316438,-9.355557,-1.554261,-5.760759,-2.104736,6.854435,-0.688867,3.547745,7.629172,-3.972804,6.564569,2.301151,-2.375561,-1.863530,-3.239244,5.760804,5.339496,4.878837,-1.971962,-9.640895,-3.112039,-6.880411,-4.655480,-0.447669,-3.700035,0.201040,1.057457,-0.782754,-9.985723,-6.347333,-5.629086,-2.572246,8.216202,3.611260,2.606567,-1.292316,-8.160800,-4.270341,9.569395,-6.545844,2.032365,0.482372,7.770084,-2.304398,-8.273982,-7.598514,-0.396318,-9.697477,-0.329721,-9.584885,4.139216,5.443964,7.997795,-1.546970,3.853246,-1.836879,7.356895,3.736355,-7.694460,-0.639555,-1.726116,1.763976,4.053366,-8.423686,6.840280,5.868691,-3.259647,-4.336432,-2.359310,-5.909129,-8.173641,-8.793334,-5.438700,-3.390650,-9.963383,7.908291,2.724764,9.329665,-2.665204,-3.751991,-1.362558,-7.839629,0.891867,-7.370389,-8.439849,4.751033,-8.072778,-5.930760,4.832056,4.057221,3.427202,1.223505,8.703993,4.410409,-0.713494,8.168707,4.702096,6.868642,2.549033,-6.663549,-3.264593,-9.397175,4.325286,7.095697,2.041280,-0.317930,7.666798,1.739178,3.570383,-3.108372,-8.807826,-5.321114,-1.666349,-4.151902,-1.649939,1.283533,-8.646458,5.688240,-5.240184,9.949458,0.957763,-4.512187,8.624661,4.001256,-0.142637,-0.440563,3.142330,-1.167506,0.249466,0.020765,0.757105,-9.560205,-4.894821,2.165477,7.086862,-3.331992,2.900013,7.254470,-1.953938,9.737865,5.258677,-3.899156,-1.468022,-0.326433,0.640122,5.380570,-0.750682,9.269470,7.032583,7.012871,2.784279,5.234960,-0.806438,3.509486,2.186891,6.436781,-9.445290,-9.320853,-7.494603,-9.161917,-0.979367,-4.969843,-7.060457,-1.062732,-1.450833,-1.603373,4.556299,-7.235176,-8.033352,0.450478,-8.164677,-3.403674,-8.494784,-2.877519,4.722647,-1.911924,-9.356105,-5.602516,-8.320898,4.241628,-4.121311,-6.886031,1.158044,6.720242,-5.597111,-1.716485,0.250949,-8.818367,3.665462,-5.657010,6.869995,-8.258573,2.926984,-0.552769,5.572316,8.235175,8.899142,-1.127460,-8.432550,0.837242,-9.943871,-0.711819,-0.962779,7.586866,6.994455,1.775017,-5.787190,-0.847633,-7.693427,-1.251491,-4.796055,-5.268493,1.987229,7.033079,-5.459708,5.580920,-6.955937,7.516702,-9.783257,-2.335027,-5.209510,-7.626913,8.376990,7.161208,-7.546977,-7.670124,3.172311,-2.456161,0.545436,-2.159154,-5.748835,-2.644976,3.144693,-3.776600,-8.806782,9.243203,-9.020909,0.606387,5.817599,1.475456,-0.860568,-0.912156,-7.169825,2.255254,-9.021662,-1.989672,6.010617,2.404442,-3.339393,-8.277474,-3.823063,6.816665,6.411574,4.812881,3.804125,-5.478676,-5.442338,1.656001,-7.090737,-3.261659,7.660428,9.981258,0.119019,1.652318,-2.128110,-1.522908,-6.192112,7.895644,-2.037623,-6.615687,-2.462310,-1.292975,8.873371,8.310867,-6.832293,1.216347,-6.594545,-5.288413,3.542141,0.722166,3.347640,8.675553,-8.032948,4.485542,7.879046,-1.757463,8.920713,-6.117309,3.057406,-5.612375,8.001539,2.656206,-6.673690,3.394246,9.232513,-2.804523,-4.761266,-5.253866,-5.273851,1.967735,7.818146,0.652046,-7.595616,-5.759644,-5.047053,4.276092,-2.097972,5.895271,-3.893396,-3.517670,-6.856400,-0.856359,-6.831122,5.796965,2.320491,-5.589209,-8.164989,2.174830,2.884636,-5.466489,-5.279876,6.045471,-1.246160,4.542456,5.658392,0.846492,-4.688872,-0.691221,-6.250522,-4.708736,8.103918,9.734722,-8.423425,-4.201347,-7.602161,9.259760,8.361578,3.916358,-3.301829,-9.743247,-8.656315,1.121578,-0.151657,-7.823349,7.172583,-3.642789,4.104647,-0.555893,-8.954549,-4.073642,-7.096978,3.711195,-2.807197,3.818039,7.420280,0.394618,2.044513,3.644469,-7.555673,3.369429,-4.610369,-2.551576,0.048519,3.312760,-8.497558,-7.355155,-8.005695,-5.450895,-6.252350,3.879404,5.836004,7.416041,3.395245,-7.787662,-7.012153,0.691406,8.080810,7.387086,-4.325696,-7.188528,-6.922770,6.654644,-4.482290,2.572589,-0.341208,1.388144,7.665495,-6.625543,6.103982,1.977472,-3.873017,-2.834605,-0.343264,-5.223769,-1.035955,2.229190,2.838822,1.642315,-9.155215,-4.729613,0.489748,2.824719,4.532739,3.216537,-6.565984,-5.771586,4.979081,1.936098,-1.428268,8.335543,-9.032275,6.978556,2.462407,-5.852608,-3.817130,-5.137134,-1.150453,-5.254562,-6.243876,-7.107528,-8.739353,8.262751,1.395489,-3.786705,6.320764,-3.453180,-2.682959,7.849079,7.638285,-5.539920,3.081326,9.125777,-4.842077,4.949656,-7.886419,2.291235,-8.434232,-4.880733,5.651108,-1.526678,-4.640883,7.373993,-9.181492,5.713188,-0.499026,8.515597,-6.200095,6.271993,1.544315,4.443288,-8.151582,-1.257513,-1.738278,-0.394611,3.389357,-6.597211,2.934871,9.662145,-2.394707,2.349607,-2.419455,-3.944438,-0.419749,3.210791,-2.974181,2.183690,6.013349,-8.977628,-1.577901,-6.190781,9.007980,-8.860086,-0.083637,-5.509722,-8.107218,2.525925,8.125354,4.743988,1.088662,8.256908,-1.202856,-6.789552,-4.851438,3.855842,8.764303,4.100064,-9.422657,7.296920,0.453894,3.829022,-7.194104,-8.631474,9.304316,6.047371,-8.287016,-8.390653,7.035681,-1.561150,2.625923,-9.398837,8.077135,7.634711,3.639355,-3.223569,3.715219,-9.217412,-3.634211,8.157960,9.296182,-7.234765,0.635337,-5.610433,5.280170,-1.426558,-3.382131,4.858327,-7.806205,9.955548,-6.507085,-4.939595,3.389046,5.900631,3.457213,4.364890,9.741807,-5.715397,7.864730,2.621892,-4.991675,0.603842,-3.191353,-5.285697,-5.802001,7.761747,-3.125709,-5.364395,-0.064751,9.023562,-5.657760,-8.962536,6.225160,-1.368483,0.055143,9.865396,5.150468,-3.601115,-1.408964,4.967387,-6.016782,5.044802,-7.126609,9.727472,6.830713,0.556293,3.621409,2.474355,-3.019903,2.760537,7.655187,2.612263,-3.224285,-4.920261,2.847977,8.781774,-7.450361,-4.684741,-0.483585,-2.709026,-4.008686,4.357427,2.158407,-2.317554,-6.233529,-8.387776,4.202181,-2.257814,4.515424,-9.213029,-0.248447,0.847235,-2.456522,-2.312837,9.659544,-6.032700,-5.381486,3.259394,-3.767823,0.895275,-3.339601,-5.148251,-2.853894,0.726819,0.342538,-3.000312,2.303134,5.924653,8.203976,-0.399152,-2.145811,-8.796598,-4.302363,-5.176007,-3.844193,8.279909,2.229034,-8.706725,-9.068867,-8.832968,3.141286,-7.459369,-0.593698,-8.751586,7.818370,-5.727996,8.791933,-6.298896,-2.838303,-4.809072,-0.568445,3.280540,4.200686,1.863394,9.206634,5.605367,-8.088342,9.970279,6.153118,-1.706894,-2.219363,-1.529448,-4.136255,7.969512,-8.840127,7.922371,0.856484,-2.167291,-8.198851,1.562534,0.990648,-8.458291,-9.108742,-7.686823,8.761338,-5.429793,1.855691,0.504396,2.937962,6.659118,-6.029950,-9.611527,5.400254,-4.032490,1.205932,-9.809235,-0.896664,-6.685009,-7.519763,0.965336,-3.365076,-3.563069,-2.221973,4.768211,-0.734751,0.788418,5.388221,1.163934,0.560023,-4.566152,6.705526,3.007718,8.911554,-9.445897,2.323650,6.350602,3.488170,9.535888,6.085629,8.683011,7.709342,-3.463167,-2.789785,-3.926560,0.871711,-7.066218,5.074675,-0.252568,-1.021561,-0.366750,-9.099040,7.859586,6.238258,-8.452725,6.918550,0.557423,-7.192755,3.380810,6.801331,-2.375195,-8.627003,9.774703,8.492764,-2.604610,-2.590989,8.651258,-5.113156,-7.423752,4.256922,-1.148188,-7.285319,-5.038226,6.054353,3.287160,8.518034,9.225832,0.414311,4.448826,-8.724033,-9.817098,-7.173981,-8.853757,-3.495232,4.091283,1.172913,-9.449650,8.690347,-0.575716,-6.539884,8.395974,-5.849755,8.809961,2.087492,-2.178778,-8.989931,-4.054424,-1.028537,9.729107,0.958553,-0.656173,-9.850764,-8.594075,1.759808,-5.197326,-9.662270,9.119221,-6.615769,-0.544992,1.826731,6.187354,9.271738,3.969528,-5.369841,-6.402611,2.559210], dtype = "float32")#candidate|11107|(2400,)|const|float32
call_11104 = relay.TupleGetItem(func_3701_call(relay.reshape(var_11105.astype('float64'), [13, 6, 5]), relay.reshape(var_11106.astype('uint32'), [63,]), relay.reshape(const_11107.astype('float32'), [2400,]), ), 6)
call_11108 = relay.TupleGetItem(func_3706_call(relay.reshape(var_11105.astype('float64'), [13, 6, 5]), relay.reshape(var_11106.astype('uint32'), [63,]), relay.reshape(const_11107.astype('float32'), [2400,]), ), 6)
output = relay.Tuple([bop_11100,call_11104,var_11105,var_11106,const_11107,])
output2 = relay.Tuple([bop_11100,call_11108,var_11105,var_11106,const_11107,])
func_11127 = relay.Function([var_11098,var_11099,var_11105,var_11106,], output)
mod['func_11127'] = func_11127
mod = relay.transform.InferType()(mod)
mutated_mod['func_11127'] = func_11127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11127_call = mutated_mod.get_global_var('func_11127')
var_11129 = relay.var("var_11129", dtype = "int16", shape = (14, 7, 13))#candidate|11129|(14, 7, 13)|var|int16
var_11130 = relay.var("var_11130", dtype = "int16", shape = (14, 7, 13))#candidate|11130|(14, 7, 13)|var|int16
var_11131 = relay.var("var_11131", dtype = "float64", shape = (195, 2))#candidate|11131|(195, 2)|var|float64
var_11132 = relay.var("var_11132", dtype = "uint32", shape = (63,))#candidate|11132|(63,)|var|uint32
call_11128 = func_11127_call(var_11129,var_11130,var_11131,var_11132,)
output = call_11128
func_11133 = relay.Function([var_11129,var_11130,var_11131,var_11132,], output)
mutated_mod['func_11133'] = func_11133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_11189 = func_10099_call()
call_11190 = func_10099_call()
var_11191 = relay.var("var_11191", dtype = "float32", shape = (15, 9, 9))#candidate|11191|(15, 9, 9)|var|float32
bop_11192 = relay.equal(call_11189.astype('bool'), relay.reshape(var_11191.astype('bool'), relay.shape_of(call_11189))) # shape=(15, 9, 9)
bop_11195 = relay.equal(call_11190.astype('bool'), relay.reshape(var_11191.astype('bool'), relay.shape_of(call_11190))) # shape=(15, 9, 9)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
var_11205 = relay.var("var_11205", dtype = "int8", shape = (55, 10))#candidate|11205|(55, 10)|var|int8
call_11204 = relay.TupleGetItem(func_3434_call(relay.reshape(var_11205.astype('int8'), [10, 5, 11])), 0)
call_11206 = relay.TupleGetItem(func_3437_call(relay.reshape(var_11205.astype('int8'), [10, 5, 11])), 0)
output = relay.Tuple([bop_11192,call_11204,var_11205,])
output2 = relay.Tuple([bop_11195,call_11206,var_11205,])
func_11215 = relay.Function([var_11191,var_11205,], output)
mod['func_11215'] = func_11215
mod = relay.transform.InferType()(mod)
mutated_mod['func_11215'] = func_11215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11215_call = mutated_mod.get_global_var('func_11215')
var_11217 = relay.var("var_11217", dtype = "float32", shape = (15, 9, 9))#candidate|11217|(15, 9, 9)|var|float32
var_11218 = relay.var("var_11218", dtype = "int8", shape = (55, 10))#candidate|11218|(55, 10)|var|int8
call_11216 = func_11215_call(var_11217,var_11218,)
output = call_11216
func_11219 = relay.Function([var_11217,var_11218,], output)
mutated_mod['func_11219'] = func_11219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_11234 = relay.TupleGetItem(func_10401_call(), 0)
call_11235 = relay.TupleGetItem(func_10403_call(), 0)
output = relay.Tuple([call_11234,])
output2 = relay.Tuple([call_11235,])
func_11261 = relay.Function([], output)
mod['func_11261'] = func_11261
mod = relay.transform.InferType()(mod)
mutated_mod['func_11261'] = func_11261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11261_call = mutated_mod.get_global_var('func_11261')
call_11262 = func_11261_call()
output = call_11262
func_11263 = relay.Function([], output)
mutated_mod['func_11263'] = func_11263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10137_call = mod.get_global_var('func_10137')
func_10139_call = mutated_mod.get_global_var('func_10139')
call_11337 = func_10137_call()
call_11338 = func_10137_call()
func_10426_call = mod.get_global_var('func_10426')
func_10428_call = mutated_mod.get_global_var('func_10428')
call_11351 = relay.TupleGetItem(func_10426_call(), 0)
call_11352 = relay.TupleGetItem(func_10428_call(), 0)
bop_11362 = relay.logical_xor(call_11337.astype('int8'), relay.reshape(call_11351.astype('int8'), relay.shape_of(call_11337))) # shape=(15, 9, 9)
bop_11365 = relay.logical_xor(call_11338.astype('int8'), relay.reshape(call_11352.astype('int8'), relay.shape_of(call_11338))) # shape=(15, 9, 9)
func_10348_call = mod.get_global_var('func_10348')
func_10352_call = mutated_mod.get_global_var('func_10352')
const_11370 = relay.const([[-0.235900,2.437289,-3.296224,7.215991,9.166990,2.198371,-2.153560,6.488668,-7.162085],[-6.386366,-0.474504,9.473609,6.159487,-8.521876,6.482775,-0.046608,-4.753479,7.805440],[-9.214750,2.119539,-3.056934,0.600827,6.019053,-2.452929,8.154470,-0.797399,-9.687757],[1.787366,-0.069480,9.088635,-7.266547,2.686889,4.504457,-7.908370,6.742946,7.015406],[-9.548816,-7.779180,-2.158981,3.124828,8.320478,5.123457,-0.210854,5.033787,-3.211633],[-3.047689,-2.640601,2.656967,-4.135718,2.794675,5.447164,0.864171,-3.553450,7.153797],[-8.981121,-0.412055,-0.723035,-8.085928,3.549475,5.238409,-2.223628,-6.726775,8.507439],[7.352676,7.292721,0.854728,5.865070,8.796786,-5.382544,-1.303152,3.572729,-4.619456],[8.759203,-1.185932,9.987199,-5.916551,3.743504,-2.698947,0.093819,-7.334897,3.679155],[8.527091,2.300103,-0.260876,-3.918437,-5.788241,5.837856,6.851770,3.968786,7.226905],[-6.056098,8.975102,6.600779,-1.121484,7.459341,3.502240,3.825304,9.246936,2.570271],[-6.324134,4.800605,-3.756400,-2.989005,7.028715,2.596743,-7.578967,-4.196805,-0.708072],[7.740559,-2.712442,0.782318,7.849554,3.460046,0.730555,-5.655728,-7.939959,8.936719],[7.275784,-9.133959,2.536767,1.887646,9.086302,0.261429,2.911637,7.305199,1.392804],[-4.248095,3.184349,-8.918672,-0.501782,-9.898858,-0.378047,5.533412,8.533601,-2.736752],[-0.271736,-0.686716,1.496278,8.993672,7.671195,3.369215,9.334464,0.708452,8.381779],[-1.453176,0.366909,-7.521062,-7.980096,5.903349,5.263644,-1.525251,5.621967,-5.907767],[7.408601,-3.512025,-3.346750,3.362873,5.213599,-1.816243,-8.079927,-3.555566,0.794345],[5.540035,8.038707,-7.942280,-5.340773,-0.459432,0.504503,6.310371,-8.146440,6.013815],[7.463042,-1.824721,-9.640632,1.964938,7.642139,-4.654717,-3.305482,-9.365052,-2.303847],[-3.837445,-1.704634,-4.304054,9.906420,-4.794416,8.700882,-1.675758,-4.087393,3.190526],[4.941312,-5.772276,9.397662,-8.890621,-8.957487,5.009747,5.530195,-2.380445,-8.795869],[4.968498,-8.596213,5.780589,-5.660507,-8.309239,-2.891904,1.690482,-7.972758,5.215112],[-3.396629,2.131343,-8.228418,0.731702,-5.756506,0.958743,-0.504955,6.118826,-6.642964],[7.181513,-6.677872,-6.856592,9.368262,2.583454,5.529688,2.301913,-2.951529,-7.154379],[1.213511,-6.374695,5.963734,-2.731839,-6.563446,-9.673953,-3.073029,9.443199,7.977154],[-2.505266,8.585538,-7.885475,-1.292715,-5.790921,-7.519819,2.582659,-5.957072,-1.883159],[-2.268367,-2.797195,-4.195386,9.312358,-0.806739,3.987532,-2.676748,-1.840802,0.513313],[-3.557760,6.956535,-4.600589,-8.618683,9.714204,6.746491,-7.612913,7.099458,1.746313],[-3.454054,-9.746704,3.263971,-9.102771,8.381099,-7.425907,-6.915891,-1.421104,3.904919],[5.411748,9.292304,2.714394,-9.133062,-1.598739,-9.673153,6.936929,-5.705649,4.106673],[-4.786360,-9.978736,-8.340318,-9.456218,4.867683,-6.173555,-6.430146,-8.474864,5.968667],[-5.642401,-8.271765,6.895560,-9.224466,2.458292,-0.152534,3.018389,-5.789500,4.384191],[-9.700051,2.323783,-0.738819,-4.898740,-2.705414,-4.756133,-8.393772,5.679706,7.810558],[3.394581,-0.466461,5.791638,8.063571,1.400837,-3.929656,3.940875,-7.099592,-6.571328],[-3.700301,7.037407,-5.650288,-2.782647,3.848184,4.875530,-6.832883,-2.753317,4.861181],[-5.549271,-6.451891,-5.611958,-4.777891,7.530798,3.926948,0.887254,6.631799,-1.715663],[1.719573,-6.362651,-4.797878,6.895445,0.075613,1.788426,8.068542,0.252415,4.103886],[-5.395017,5.861318,8.040131,-7.051917,0.163017,4.607495,5.306425,-6.458433,5.457497],[9.564131,-8.902465,7.684356,7.538528,1.168062,-5.470444,-0.288736,-1.997797,0.621009],[-5.241439,-3.521281,2.938450,6.249615,-9.087198,-7.721514,5.913635,6.999492,-5.999115],[1.587783,9.279237,9.886885,-9.112759,2.644908,9.872693,-3.653370,-1.290283,3.625271],[-1.416511,-9.449730,2.032244,5.103712,-5.864018,-3.307040,8.094247,-2.423501,-4.293717],[-7.990527,2.321126,0.855104,-9.484731,5.497755,-0.420775,-0.404391,1.988547,-8.356027],[-9.079981,0.232475,-3.932449,8.928486,-9.616719,-6.162730,2.347187,4.284823,-7.116537],[-1.273428,-9.959700,1.002586,-5.239000,0.607187,-1.539968,-3.083595,3.593381,7.063039],[8.303223,7.199147,-2.918643,-5.380660,1.709820,1.728686,-2.878794,-7.871868,8.612124],[-8.159105,-3.546431,7.003569,9.468166,2.172014,-9.386459,-7.581380,8.870463,8.540219],[1.846688,-2.772865,7.396333,3.856894,8.141327,-4.684543,2.732635,-9.726372,-6.743874],[5.039551,-0.662599,8.380417,2.149627,-0.178707,0.297602,4.160975,-4.761216,1.446933],[0.114093,8.053299,0.141021,1.324004,-4.550208,-8.189658,0.918756,-3.589157,-2.308772],[-9.730981,5.649607,-3.207608,-3.793535,-3.528050,6.353674,-2.482545,-7.928839,6.695913],[2.271240,-0.127960,3.601070,3.395357,-5.210158,-4.377371,3.879946,3.156071,8.884656],[7.621010,0.901571,-6.571150,-7.218154,9.487278,3.877697,-4.394061,3.690079,-5.054549],[8.522036,7.065624,-3.468782,-0.478921,1.865094,-9.729102,5.815705,-2.484434,0.479491],[-7.072593,-0.815084,-4.744154,-8.761665,-4.437835,-9.227241,-2.618268,-9.249559,0.116056],[2.096728,-6.591306,7.281064,-5.943792,8.772943,4.256267,5.429945,-8.772781,1.122866],[1.860930,9.281973,4.015958,0.927815,1.714681,-7.572134,-3.200636,-0.565866,-6.004577],[3.722532,-1.282863,7.236717,-5.013778,8.186837,-1.867642,1.781510,1.038191,-2.097275],[-7.884602,-6.108312,2.860912,2.923113,2.001677,1.184881,3.262882,-9.707311,5.026144],[-5.106565,-9.700244,-2.361845,-2.462136,7.702859,-8.289247,8.822303,4.231943,-8.772374],[-0.960818,-1.851754,2.958295,7.910877,-5.582202,-1.254223,8.233704,0.708769,4.680521],[8.922357,-2.439483,6.237513,-5.887851,4.079290,-5.474629,-9.646545,9.596659,-2.632348],[-9.732482,-4.270625,9.382645,-2.690223,6.406922,5.327087,7.273197,-3.089951,6.534412],[-2.983789,-7.687769,8.150886,7.494690,0.701896,-1.299336,4.890926,6.346964,0.362975]], dtype = "float32")#candidate|11370|(65, 9)|const|float32
call_11369 = relay.TupleGetItem(func_10348_call(relay.reshape(const_11370.astype('float32'), [13, 9, 5]), relay.reshape(const_11370.astype('float32'), [13, 9, 5]), relay.reshape(const_11370.astype('float32'), [13, 9, 5]), ), 0)
call_11371 = relay.TupleGetItem(func_10352_call(relay.reshape(const_11370.astype('float32'), [13, 9, 5]), relay.reshape(const_11370.astype('float32'), [13, 9, 5]), relay.reshape(const_11370.astype('float32'), [13, 9, 5]), ), 0)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_11374 = relay.TupleGetItem(func_10401_call(), 0)
call_11375 = relay.TupleGetItem(func_10403_call(), 0)
func_11088_call = mod.get_global_var('func_11088')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_11395 = func_11088_call()
call_11396 = func_11088_call()
output = relay.Tuple([bop_11362,call_11369,const_11370,call_11374,call_11395,])
output2 = relay.Tuple([bop_11365,call_11371,const_11370,call_11375,call_11396,])
func_11409 = relay.Function([], output)
mod['func_11409'] = func_11409
mod = relay.transform.InferType()(mod)
output = func_11409()
func_11410 = relay.Function([], output)
mutated_mod['func_11410'] = func_11410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_11512 = relay.TupleGetItem(func_10933_call(), 0)
call_11513 = relay.TupleGetItem(func_10935_call(), 0)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
const_11517 = relay.const([-6,2,4,-5,-9,-10,7,-3,8,-6,7,-7,3,2,-5,-8,3,-6,7,9,8,-8,-9,-6,3,2,-2,-6,6,6,9,2,-3,9,2,9,7,-6,6,-5,-6,8,7,4,4,-3,-6,-6,-7,-1,3,10,-5,8,10,2,-10,7,-8,1,3,-6,-10,7,7,6,-8,-2,5,-6,-3,5,1,-3,5,1,-7,-8,-9,-4,-5,-10,9,5,2,-10,-10,-2,-7,1,6,-1,-9,2,5,8,-8,-2,10,10,-7,-9,-7,9,6,9,2,-7,-10,2,-4,-5,7,-9,5,1,2,-10,-10,5,8,8,-4,2,-3,-9,-5,9,-4,-10,-10,2,8,-2,-10,4,3,-10,8,-2,6,-10,-10,2,-1,-2,3,2,-5,-2,3,4,10,4,-6,1,-2,3,-3,-3,-9,-5,8,-6,4,-7,-5,-7,-5,-5,9,-2,-10,-2,-2,-7,-9,-3,-4,9,6,6,-9,6,-6,-6,8,8,7,-1,5,9,-2,3,1,3,2,-9,-4,6,6,7,-3,2,-6,-8,10,-7,10,-8,3,-10,-1,-5,-4,7,6,5,-2,9,7,9,5,-10,5,7,9,3,6,7,1,-1,-9,-8,3,-8,-5,8,10,-8,-3,-3,2,-4,-3,10,6,-3,-8,-5,8,-1,-10,-6,4,5,9,-2,3,-1,7,-10,-3,-8,-4,1,-8,-7,-1,9,7,5,-4,-6,4,-5,9,4,10,4,-6,-8,-7,-3,7,4,-9,-7,7,-2,-3,2,2,-5,-9,-8,3,-9,10,9,-5,-1,-3,9,-4,-10,10,10,-9,6,-5,1,10,-8,-4,-8,-3,5,-9,-5,7,-1,-9,-9,-7,6,-1,10,9,-2,9,3,-10,8,-3,6,10,9,10,10,4,1,-5,7,-1,8,-10,1,-1,1,2,6,-5,-3,-4,6,1,3,8,-1,-8,8,3,-8,-6,8,6,-2,-10,10,10,-2,-1,8,-5,-10,-1,9,-8,6,-5,4,10,-4,2,4,8,-4,1,2,-2,-8,-1,-7,-3,-2,1,2,3,4,10,1,4,-8,-9,10,1,6,-5,10,8,-10,10,-2,8,8,4,5,-5,4,1,7,1,5,-8,8,7,-7,-10,9,3,-5,9,4,2,9,-1,9,-2,2,1,6,-9,-6,9,8,-5,10,4,-9,3,2,-4,8,5,-6,3,6,-2,-3,-6,-5,-4,4,-1,6,10,-8,1,4,9,4,-9,-3,1,-6,-5,-9,-7,10,-7,-2,4,-5,5,1,-7,-5,5,1,-2,-2,-7,-9,-3,2,5,9,3,6,-1,-3,4,-5,6,5,-3,8,-8,-6,-5,-3,2,2,3,-5,-9,-3,8,1,5,3,-1,-10,7,-1,4,-5,-3,-4,-6,-1,9,7,-3,1,-2,-6,3,-3,-9,3,8,10,4,8,-4,5,4,-1], dtype = "int8")#candidate|11517|(550,)|const|int8
call_11516 = relay.TupleGetItem(func_3434_call(relay.reshape(const_11517.astype('int8'), [10, 5, 11])), 0)
call_11518 = relay.TupleGetItem(func_3437_call(relay.reshape(const_11517.astype('int8'), [10, 5, 11])), 0)
uop_11519 = relay.asinh(call_11512.astype('float64')) # shape=(15, 9, 9)
uop_11521 = relay.asinh(call_11513.astype('float64')) # shape=(15, 9, 9)
func_6945_call = mod.get_global_var('func_6945')
func_6949_call = mutated_mod.get_global_var('func_6949')
var_11528 = relay.var("var_11528", dtype = "float64", shape = ())#candidate|11528|()|var|float64
const_11529 = relay.const([-9.327176,-7.762008,-9.948093,-5.138987,8.696494,-0.658862,4.701611,-8.690351,8.537428,-5.168353,-0.676953,-2.276321,0.003598,6.073535,0.529977,0.997088,2.312231,9.564333,9.623553,6.138541,-9.836749,-5.499486,8.771733,-7.404487,-0.985383,9.443592,7.665605,4.015475,2.793779,-5.099613,2.000944,-0.313872,6.890308,7.356708,8.914506,3.052244,-1.679642,7.181046,-0.877532,1.078272,-6.577022,7.440352,-7.782605,-1.832952,-5.753723,4.685802,-8.180649,-0.039105,5.059006,-8.705956,-5.933221,-5.893750,-9.673846,-0.920512,-5.262674,4.274416,1.511700,-7.088135,0.004619,3.864024,2.866480,-0.643659,-0.289391,-4.730882,-9.067970,-2.629703,-0.062976,1.924172,1.741986,-6.002830,0.383954,-1.696527,-5.523406,3.299234,-4.400711,4.662674,2.167252,9.084224,-5.982155,8.625114,2.904671,-9.435569,5.383329,-0.649260,4.116733,-5.933031,-9.448962,6.468795,1.269914,-0.122498,4.387913,-2.537392,4.351676,-5.732019,4.882406,-0.640665,-3.319188,-0.241832,8.721660], dtype = "float64")#candidate|11529|(99,)|const|float64
var_11530 = relay.var("var_11530", dtype = "bool", shape = (495,))#candidate|11530|(495,)|var|bool
call_11527 = relay.TupleGetItem(func_6945_call(relay.reshape(var_11528.astype('float64'), []), relay.reshape(const_11529.astype('float64'), [11, 1, 9]), relay.reshape(var_11530.astype('bool'), [11, 5, 9]), ), 1)
call_11531 = relay.TupleGetItem(func_6949_call(relay.reshape(var_11528.astype('float64'), []), relay.reshape(const_11529.astype('float64'), [11, 1, 9]), relay.reshape(var_11530.astype('bool'), [11, 5, 9]), ), 1)
func_6945_call = mod.get_global_var('func_6945')
func_6949_call = mutated_mod.get_global_var('func_6949')
call_11534 = relay.TupleGetItem(func_6945_call(relay.reshape(var_11528.astype('float64'), []), relay.reshape(const_11529.astype('float64'), [11, 1, 9]), relay.reshape(var_11530.astype('bool'), [11, 5, 9]), ), 1)
call_11535 = relay.TupleGetItem(func_6949_call(relay.reshape(var_11528.astype('float64'), []), relay.reshape(const_11529.astype('float64'), [11, 1, 9]), relay.reshape(var_11530.astype('bool'), [11, 5, 9]), ), 1)
output = relay.Tuple([call_11516,const_11517,uop_11519,call_11527,var_11528,const_11529,var_11530,call_11534,])
output2 = relay.Tuple([call_11518,const_11517,uop_11521,call_11531,var_11528,const_11529,var_11530,call_11535,])
func_11542 = relay.Function([var_11528,var_11530,], output)
mod['func_11542'] = func_11542
mod = relay.transform.InferType()(mod)
var_11543 = relay.var("var_11543", dtype = "float64", shape = ())#candidate|11543|()|var|float64
var_11544 = relay.var("var_11544", dtype = "bool", shape = (495,))#candidate|11544|(495,)|var|bool
output = func_11542(var_11543,var_11544,)
func_11545 = relay.Function([var_11543,var_11544,], output)
mutated_mod['func_11545'] = func_11545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11261_call = mod.get_global_var('func_11261')
func_11263_call = mutated_mod.get_global_var('func_11263')
call_11550 = relay.TupleGetItem(func_11261_call(), 0)
call_11551 = relay.TupleGetItem(func_11263_call(), 0)
func_10628_call = mod.get_global_var('func_10628')
func_10630_call = mutated_mod.get_global_var('func_10630')
const_11559 = relay.const([2.633154,-0.931824,1.463864,-8.952297,-0.119142,-2.764165,-2.343313,5.467122,1.765966,5.365460,2.157091,-6.917676,-2.358028,-0.854470,-4.013119,-3.741252,-8.547546,2.840484,-3.727443,0.093464,4.876614,-8.794329,-2.659977,6.527539,3.432941,5.314087,-9.319114,-2.596984,4.350657,8.301322,0.831614,2.399004,-4.460164,8.680142,-9.181023,-4.424301,4.346992,-0.878557,-3.374596,7.709508,-5.425785,-2.730161,-6.151619,6.784113,-7.766247,6.797871,-1.075149,2.821808,2.701474,0.840826,8.537509,-8.623081,0.722952,-4.275481,-5.997847,3.369665,0.151665,-5.336072,1.114723,0.965949,-8.082335,5.632520,6.629424,7.724171,3.061210,4.054067,-8.897148,8.619784,-8.709108,-8.181474,4.781817,8.535268,1.239454,7.032623,4.939685,-6.692593,7.766437,-0.016115,-3.364162,-3.409095,-2.905754,-3.776019,7.404635,-4.104585,-1.291016,-3.841292,3.646534,-5.449459,8.515005,6.816802,-8.666871,-3.814718,8.739351,-6.718742,6.834861,9.304647,-0.643832,-5.594661,-3.324712,5.023248,7.758381,-5.674384,0.987377,-8.154892,-5.355772,9.527584,7.424843,8.524462,-1.387615,3.181775,-1.915299,-1.517389,-0.501193,-2.899840,4.651370,9.755840,4.719567,5.529288,-0.031427,-3.365155,5.511486,8.344516,2.529105,0.557329,7.600550,1.810829,-6.430866,-7.668673,9.455665,5.042038,4.876849,0.849981,-5.541949,3.654339,-3.254378,-7.271949,-9.924932,3.039902,-8.836374,7.867839,6.474163,3.509635,-9.265735,-7.059940,-5.053190,1.470013,5.704184,-5.619366,8.709788,-9.007068,7.162433,-2.508485,4.867050,-8.220172,-3.904458,9.300829,-3.336977,1.792177,-7.392997,-8.365231,7.002767,-1.413534,9.492339,4.411311,3.930120,-2.936548,-8.673518,-0.828450,-3.183489,4.929441,-6.828818,-4.231868,8.483642,-2.438041,-8.603574,-7.799802,-4.980770,-9.334243,9.351264,-1.713090,7.511705,-4.181433,4.048875,6.350789,3.827969,9.671935,4.769811,-1.166917,5.305790,0.878948,-6.658603,-4.545664,-2.210883,-0.872256,-8.567576,-3.839360,1.116818,2.475870,7.043498,3.782421,0.033309,7.144054,-2.682418,9.286568,-1.533090,1.379740,-1.665713,1.648799,-9.794883,-6.579405,-7.073460,5.700581,0.313100,5.004828,0.489782,7.981067,5.055533,-2.902960,4.003433,5.159829,-9.372147,-6.348809,-9.577488,5.933735,4.093102,2.211360,6.215332,6.341979,9.979105,6.747770,3.117638,3.853602,3.077813,2.325800,2.820334,-1.357143,3.329149,-4.065768,-0.952767,3.980819,-6.904445,-8.116548,4.615431,-7.171365,-1.757980,6.575431,6.141220,-0.506418,-5.875660,4.650373,-0.010934,5.007273,-2.935491,-4.618355,-4.007814,-4.625904,-6.546856,-3.529952,-8.389767,7.091545,-5.837845,8.529928,3.642541,9.533173,3.288840,-0.218581,-7.484255,9.669604,0.845195,-9.755348,2.560611,-7.427205,5.716116,6.573620,-5.247961,-0.170777,-9.783059,-1.814567,8.401537,1.371187,-4.212020,-2.264785,-0.360303,3.122368,6.812414,1.594974,-9.225775,9.395149,-1.714792,7.215335,0.152742,0.967056,4.111535,0.623490,9.477499,5.674897,-7.121688,5.609591,-9.769273,4.476973,-9.579323,-0.600242,-8.732067,-9.193359,3.293525,6.933389,4.535329,-1.533277,-9.372638,3.245403,-5.707291,5.986215,-2.584435,2.741893,7.892947,9.798360,3.550273,-0.503691,2.090566,-1.620425,1.425377,3.113062,3.912458,2.772704,0.397937,6.758196,-5.169848,9.080492,2.862029,8.079748,9.311372,-1.899852,-2.978840,-5.759631,0.553839,-7.861937,8.163872,6.534982,6.625855,-4.483876,7.303759,4.787000,9.147413,7.791306,5.218241,6.305270,7.209779,-5.971556,0.360348,5.061255,3.649041,2.828827,4.250634,7.492765,8.774722,4.260912,-1.972680,-1.901680,6.102888,-3.363672,-9.094878,3.820344,-4.572278,-7.665545,5.548860,-3.618835,4.037273,5.961099,9.862873,-6.039161,-2.946345,1.710680,-2.704319,-5.440860,1.010447,-7.990610,2.313054,9.663732,3.947257,9.070968,1.507645,-2.532223,6.388289,3.966045,-4.888679,7.606236,-6.811464,3.987026,6.306339,-5.191113,6.513713,-8.075678,1.037381,-2.496671,2.312420,9.492917,1.913202,-6.034670,5.814179,4.454210,5.254951,-4.850874,-9.155525,-7.067804,-1.151476,-3.194758,4.546923,-4.992738,5.120051,-5.914201,-1.861290,1.883159,0.771726,-6.383476,-2.032607,-9.435372,-5.772094,1.166061,2.782613,-6.099413,-0.248844,1.062432,-8.657257,-3.534399,-1.225692,-2.674022,-6.198216,-1.984047,2.825313,-9.808909,2.786107,4.052803,-4.580692,-4.989799,-9.042591,4.128155,5.113337,6.995910,-2.024584,1.203346,-4.054178,2.361632,-3.883568,-0.904425,-8.767800,9.099892,1.615177,9.067257,0.769254,3.330548,5.665554,-6.508190,5.500319,-6.750333,-5.244612,-6.955167,0.534662,7.839258,-8.232135,-1.774478,0.820847,-9.995668,-3.701023,-3.341836,0.908455,-2.492038,-1.775692,1.240339,-0.148732,4.936777,-4.797276,6.654930,5.772323,5.946888,-2.809596,-5.745243,4.905011,-5.104471,-3.782116,6.436609,6.346444,-3.057132,-0.423224,1.528354,2.353600,5.344233,2.602747,-8.294044,-8.854831,-6.787967,1.562338,-5.874460,4.342759,-1.077166,1.282883,1.179083,5.234387,-7.223022,6.717118,-0.601726,-0.930991,-9.595547,-0.935661,-5.336813,-8.383991,7.326035,4.914674,-4.404548,3.808476,-0.978665,-7.015373,6.390836,-8.521107,-2.496330,0.667086,-6.619101,-4.788212,6.838041,9.668526,0.194510,-6.827672,4.553043,-6.958573,-6.236143,6.487320,-1.759478,-4.716920,5.748788,9.632547,6.482282,1.766342,-6.111134,-0.699437,-8.979416,4.439153,-1.940145,4.495926,8.276816,7.193828,4.956415,0.469822,6.605787,0.505578,-1.131748,-7.664548,9.899046,4.002373,5.299660,-7.267288,-6.613699,-4.890993,6.590964,-6.437487,3.925656,8.466805,-0.626484,6.584015,-7.740874,2.720027,1.164179], dtype = "float64")#candidate|11559|(560,)|const|float64
call_11558 = func_10628_call(relay.reshape(const_11559.astype('float64'), [10, 14, 4]))
call_11560 = func_10628_call(relay.reshape(const_11559.astype('float64'), [10, 14, 4]))
output = relay.Tuple([call_11550,call_11558,const_11559,])
output2 = relay.Tuple([call_11551,call_11560,const_11559,])
func_11561 = relay.Function([], output)
mod['func_11561'] = func_11561
mod = relay.transform.InferType()(mod)
mutated_mod['func_11561'] = func_11561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11561_call = mutated_mod.get_global_var('func_11561')
call_11562 = func_11561_call()
output = call_11562
func_11563 = relay.Function([], output)
mutated_mod['func_11563'] = func_11563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_11566 = relay.TupleGetItem(func_10933_call(), 0)
call_11567 = relay.TupleGetItem(func_10935_call(), 0)
func_3701_call = mod.get_global_var('func_3701')
func_3706_call = mutated_mod.get_global_var('func_3706')
var_11584 = relay.var("var_11584", dtype = "float64", shape = (390,))#candidate|11584|(390,)|var|float64
var_11585 = relay.var("var_11585", dtype = "uint32", shape = (63,))#candidate|11585|(63,)|var|uint32
var_11586 = relay.var("var_11586", dtype = "float32", shape = (300, 8))#candidate|11586|(300, 8)|var|float32
call_11583 = relay.TupleGetItem(func_3701_call(relay.reshape(var_11584.astype('float64'), [13, 6, 5]), relay.reshape(var_11585.astype('uint32'), [63,]), relay.reshape(var_11586.astype('float32'), [2400,]), ), 2)
call_11587 = relay.TupleGetItem(func_3706_call(relay.reshape(var_11584.astype('float64'), [13, 6, 5]), relay.reshape(var_11585.astype('uint32'), [63,]), relay.reshape(var_11586.astype('float32'), [2400,]), ), 2)
uop_11594 = relay.asin(var_11586.astype('float32')) # shape=(300, 8)
bop_11596 = relay.logical_or(var_11586.astype('bool'), relay.reshape(uop_11594.astype('bool'), relay.shape_of(var_11586))) # shape=(300, 8)
output = relay.Tuple([call_11566,call_11583,var_11584,var_11585,bop_11596,])
output2 = relay.Tuple([call_11567,call_11587,var_11584,var_11585,bop_11596,])
func_11601 = relay.Function([var_11584,var_11585,var_11586,], output)
mod['func_11601'] = func_11601
mod = relay.transform.InferType()(mod)
var_11602 = relay.var("var_11602", dtype = "float64", shape = (390,))#candidate|11602|(390,)|var|float64
var_11603 = relay.var("var_11603", dtype = "uint32", shape = (63,))#candidate|11603|(63,)|var|uint32
var_11604 = relay.var("var_11604", dtype = "float32", shape = (300, 8))#candidate|11604|(300, 8)|var|float32
output = func_11601(var_11602,var_11603,var_11604,)
func_11605 = relay.Function([var_11602,var_11603,var_11604,], output)
mutated_mod['func_11605'] = func_11605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_11607 = relay.TupleGetItem(func_10933_call(), 0)
call_11608 = relay.TupleGetItem(func_10935_call(), 0)
var_11609 = relay.var("var_11609", dtype = "float32", shape = (15, 9, 9))#candidate|11609|(15, 9, 9)|var|float32
bop_11610 = relay.add(call_11607.astype('uint32'), relay.reshape(var_11609.astype('uint32'), relay.shape_of(call_11607))) # shape=(15, 9, 9)
bop_11613 = relay.add(call_11608.astype('uint32'), relay.reshape(var_11609.astype('uint32'), relay.shape_of(call_11608))) # shape=(15, 9, 9)
func_10305_call = mod.get_global_var('func_10305')
func_10306_call = mutated_mod.get_global_var('func_10306')
call_11617 = func_10305_call()
call_11618 = func_10305_call()
func_4293_call = mod.get_global_var('func_4293')
func_4296_call = mutated_mod.get_global_var('func_4296')
const_11620 = relay.const([1.036866,4.817229,-0.502830,0.940931,4.174547,0.518015,-6.204975,-3.137559,-5.537779,-2.068182,-0.871150,4.909168,8.304364,-2.165155,-9.573163,9.677305,-1.543493,4.233278,4.469664,2.070091,-5.894389,-5.594586,-7.469847,-9.682353,4.564795,6.578764,-9.414278,-3.343387,8.996896,-8.878131,-6.284599,4.669302,-2.535779,7.304646,6.839770,7.908957,0.521246,-8.980961,-8.144565,6.929876,7.513700,5.319728,1.470233,4.155898,-3.297018,-6.088446,2.134545,-0.991486,-9.150808,-6.306459,-4.341920,6.551537,4.343630,1.188285,4.677824,-0.993176,7.972924,-4.300200,7.059588,-1.076942,-8.501992,-4.305791,-3.207640,7.979150,-0.537281,0.026381,9.770333,2.779933,-1.356720,-5.135596,4.432234,2.204303,4.166078,7.900477,1.815494,-9.091718,-0.608998,-8.541909,7.233998,-5.243613,6.969974,8.136997,-9.151306,5.443987,9.560703,-2.883863,-1.354675,-1.915129,-0.210474,-5.067706,1.154245,3.427063,0.522262,-9.391845,0.200506,9.364203,-4.398027,-9.725411,9.548875,-1.165236,2.124582,3.973715,-4.834922,0.010265,8.570998,-2.545399,0.411737,-7.424763,0.283176,0.830973,5.379565,6.993161,3.665113,8.240833,-5.786366,-1.390937,-7.645277,7.086183,3.644617,4.482853,0.148174,1.047430,9.905722,9.123185,-3.665354,-0.088299,9.457707,-9.406133,8.357389,9.841428,7.566894,1.640970,0.263507,-6.765004,-9.575815,0.872500,2.042259,-0.256722,2.825349,-3.341092,-0.863852,0.516878,-4.180355,6.811315,1.613622,9.769525,-0.813981,3.341316,-6.105354,-8.329705,6.348150,-3.309658,-1.808004,-3.360111,-8.888840,2.282364,8.924844,7.361581,-3.014618,9.285501,1.762387,-8.959611,0.659201,-7.211197,9.245799,-8.819387,-9.307625,-8.870561,3.235975,-8.235911,2.387105,3.098055,2.567415,-2.440474,8.075920,2.310271,0.113791,-8.707309,3.897027,-6.677153,8.176026,-7.987772,8.874351,-2.554285,2.989937,-6.613071,-5.170608,8.438888,-5.194634,-0.002257,4.191352,0.572427,0.432165,5.862456,-2.686776,-4.822318,6.396707,6.798237,6.983353,2.741050,8.025586,3.743436,3.519629,1.122506,-8.436719,9.263168,6.388370,-5.779903,-0.778896,-9.739964,1.822556,-2.158929,1.355858,2.803164,5.963030,2.089695,9.662836,7.050571,4.459165,-5.478086,-5.190596,0.859497,-7.806734,-1.533669,6.909887,8.499175,7.281337,4.569413,-3.120729,3.754864,-7.710299,-1.256582,7.350541,-0.023859,-7.115974,3.225091,0.415069,-7.631050,-4.748702,-5.547707,9.959098,4.784468,-1.282668,8.295212,8.159865,-5.573455,2.834241,6.951700,-3.585714,2.904997,5.397079,8.144210,4.775583,-1.864770,8.979572,-8.466957,2.700041,2.080569,-2.561999,-5.986143,-0.251752,1.543132,9.695261,-2.508567,5.214946,-6.474133,-5.340069,9.102980,4.247857,-8.297473,-4.399929,-5.000476,-8.542419,2.521152,-0.027292,-4.106301,0.842542,9.032514,8.618404,-8.132438,7.663070,9.564596,6.876038,-4.173571,-7.981996,7.840495,1.805123,-9.404328,3.594657,-0.868116,3.982134,-7.791857,2.553894,8.880788,-7.995226,2.170422,-7.313875,4.831065,3.285193,2.841230,-5.790509,-3.774261,-6.531101,8.083764,2.854277,1.784793,9.827822,7.045626,7.346510,0.091875,-1.877518,-6.447753,9.742631,-0.080178,1.796955,-3.231780,-9.317159,2.057549,-1.213435,7.876137,-1.320820,-4.992513,-4.116322,-5.270843,5.090087,0.759199,-9.825844,-9.407529,-8.532521,-2.043948,-5.858090,5.981294,-4.319166,2.072302,-3.081833,-0.457621,-9.307413,-6.781747,-7.106501,-7.909357,-0.644012,0.145398,2.225619,-3.754319,8.730181,8.518850,7.653941,-7.985537,1.510027,-2.002759,-5.361693,2.506850,-1.913785,-3.248743,-5.255639,-0.938247,-0.768330,-6.788219,8.579819,4.854269,3.620746,7.846125,-1.978177,-6.023214,0.403319,1.486661,8.581742,-5.799836,-1.275765,-7.936390,-4.531084,2.698563,6.585172,-5.202611,-7.871693,0.616496,9.859889,-5.305979,-4.012035,3.322943,-7.361390,-6.534372,9.398618,8.126902,3.850744,9.781499,-6.927691,-1.813696,-9.424457,-9.322701,0.616055,-4.077864,-6.003876,-1.420892,-3.800504,1.634498,-3.997652,-2.318061,-1.030291,4.341827,-7.312369,7.448320,3.367420,-2.847666,3.206157,-7.879856,-1.896028,2.916168,8.467088,1.902000,8.122793,-6.464040,-4.545325,-6.757801,-6.094480,-3.621042,-6.810480,1.343257,-0.593563,2.262796,4.590347,-5.821757,-8.427900,-8.671061,3.769412,9.035920,-4.932974,-3.834391,4.917366,-4.875202,-8.679502,-9.180229,-1.534862,-5.921532,3.155711,-7.459909,0.295124,-7.411565,-7.636415,6.610336,-2.099817,1.525547,4.600649,-1.183343,-5.012315,-4.561244,1.046907,9.503952,6.913302,-4.253905,1.315931,2.594539,8.053839,-9.907062,-5.508388,7.472301,5.321121,-1.448284,-8.086531,2.936178,2.104797,8.839758,-1.127784,-7.481254,-6.381897,-5.590478,-6.690456,-0.351828,5.058961,4.578852,1.609256,-0.358227,9.773845,5.858861,5.122326,-3.797181,-3.725482,-6.735930,-7.690561,-8.469013,0.595374,-2.672561,-0.091384,-5.001032,-2.878147,-7.177593,-1.064118,-9.290914,3.802667,-2.993358,-4.312653,2.818232,-6.643676,0.979832,-6.219193,-3.569796,-4.839181,9.595435,6.029211,-3.266938,-8.860167,7.643885,1.022923,-4.776317,4.181513,-5.681944,-4.196540,1.115498,8.622210,1.894478,-8.868969,5.998399,1.988835,-2.539840,-4.227207,-9.470864,3.216810,-1.316741,3.925112,5.274382,1.585773,-5.663498,6.970881,-7.355303,-2.474251,-0.408156,5.872332,2.926040,2.979828,-7.318970,-7.259295,-7.513234,-3.920549,-6.003010,6.101983,3.337324,8.778965,-9.271554,4.789577,2.580925,5.221234,-9.974365,-8.997513,4.145336,4.582202,0.343897,-4.085374,1.072811,-6.522461,-6.821909,9.561033,-0.953414,2.206726,4.811037,-7.577009,-8.047114,2.653509,-7.441051,-6.915409,7.022296,5.340312,5.790513,-7.281931,4.659226,-1.657411,-1.842825,0.941057,7.768091,-4.166226,8.576703,5.988339,-0.955511,-5.902586,-0.431826,-5.547308,0.800894,7.897528,5.564484,9.393586,-3.666358,-9.949207,-1.094891,-5.002577,-6.655762,-7.687458,6.911114,4.715343,-1.436514,-5.722027,-2.080783,-8.868503,0.722986,-5.113946,0.095977,6.746144,5.912522,7.759427,7.277633,5.509441,-4.896767,7.975639,-7.017258,8.545439,-1.733064,8.952920,-2.916413,-5.358283,3.407138,-5.744380,1.914845,6.797713,2.477540,-3.388901,-4.232921,-6.048077,6.746536,-3.661927,-0.429791,3.819595,6.429104,8.376916,-3.503564,1.413374,-4.888666,5.253836,5.766640,-3.663339,0.661128,7.761812,3.681448], dtype = "float32")#candidate|11620|(630,)|const|float32
call_11619 = relay.TupleGetItem(func_4293_call(relay.reshape(const_11620.astype('float32'), [7, 10, 9])), 0)
call_11621 = relay.TupleGetItem(func_4296_call(relay.reshape(const_11620.astype('float32'), [7, 10, 9])), 0)
output = relay.Tuple([bop_11610,call_11617,call_11619,const_11620,])
output2 = relay.Tuple([bop_11613,call_11618,call_11621,const_11620,])
func_11633 = relay.Function([var_11609,], output)
mod['func_11633'] = func_11633
mod = relay.transform.InferType()(mod)
mutated_mod['func_11633'] = func_11633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11634 = relay.var("var_11634", dtype = "float32", shape = (15, 9, 9))#candidate|11634|(15, 9, 9)|var|float32
func_11633_call = mutated_mod.get_global_var('func_11633')
call_11635 = func_11633_call(var_11634)
output = call_11635
func_11636 = relay.Function([var_11634], output)
mutated_mod['func_11636'] = func_11636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_11726 = relay.TupleGetItem(func_10485_call(), 0)
call_11727 = relay.TupleGetItem(func_10486_call(), 0)
output = call_11726
output2 = call_11727
func_11738 = relay.Function([], output)
mod['func_11738'] = func_11738
mod = relay.transform.InferType()(mod)
output = func_11738()
func_11739 = relay.Function([], output)
mutated_mod['func_11739'] = func_11739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10137_call = mod.get_global_var('func_10137')
func_10139_call = mutated_mod.get_global_var('func_10139')
call_11778 = func_10137_call()
call_11779 = func_10137_call()
output = relay.Tuple([call_11778,])
output2 = relay.Tuple([call_11779,])
func_11780 = relay.Function([], output)
mod['func_11780'] = func_11780
mod = relay.transform.InferType()(mod)
mutated_mod['func_11780'] = func_11780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11780_call = mutated_mod.get_global_var('func_11780')
call_11781 = func_11780_call()
output = call_11781
func_11782 = relay.Function([], output)
mutated_mod['func_11782'] = func_11782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11561_call = mod.get_global_var('func_11561')
func_11563_call = mutated_mod.get_global_var('func_11563')
call_11786 = relay.TupleGetItem(func_11561_call(), 1)
call_11787 = relay.TupleGetItem(func_11563_call(), 1)
output = call_11786
output2 = call_11787
func_11796 = relay.Function([], output)
mod['func_11796'] = func_11796
mod = relay.transform.InferType()(mod)
output = func_11796()
func_11797 = relay.Function([], output)
mutated_mod['func_11797'] = func_11797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_11838 = relay.TupleGetItem(func_10401_call(), 0)
call_11839 = relay.TupleGetItem(func_10403_call(), 0)
uop_11846 = relay.sin(call_11838.astype('float64')) # shape=(15, 9, 9)
uop_11848 = relay.sin(call_11839.astype('float64')) # shape=(15, 9, 9)
func_10945_call = mod.get_global_var('func_10945')
func_10946_call = mutated_mod.get_global_var('func_10946')
call_11853 = func_10945_call()
call_11854 = func_10945_call()
output = relay.Tuple([uop_11846,call_11853,])
output2 = relay.Tuple([uop_11848,call_11854,])
func_11872 = relay.Function([], output)
mod['func_11872'] = func_11872
mod = relay.transform.InferType()(mod)
output = func_11872()
func_11873 = relay.Function([], output)
mutated_mod['func_11873'] = func_11873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_11906 = func_10099_call()
call_11907 = func_10099_call()
func_11780_call = mod.get_global_var('func_11780')
func_11782_call = mutated_mod.get_global_var('func_11782')
call_11924 = relay.TupleGetItem(func_11780_call(), 0)
call_11925 = relay.TupleGetItem(func_11782_call(), 0)
func_286_call = mod.get_global_var('func_286')
func_288_call = mutated_mod.get_global_var('func_288')
var_11930 = relay.var("var_11930", dtype = "float64", shape = (1, 72))#candidate|11930|(1, 72)|var|float64
call_11929 = func_286_call(relay.reshape(var_11930.astype('float64'), [6, 3, 4]))
call_11931 = func_286_call(relay.reshape(var_11930.astype('float64'), [6, 3, 4]))
output = relay.Tuple([call_11906,call_11924,call_11929,var_11930,])
output2 = relay.Tuple([call_11907,call_11925,call_11931,var_11930,])
func_11936 = relay.Function([var_11930,], output)
mod['func_11936'] = func_11936
mod = relay.transform.InferType()(mod)
mutated_mod['func_11936'] = func_11936
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11937 = relay.var("var_11937", dtype = "float64", shape = (1, 72))#candidate|11937|(1, 72)|var|float64
func_11936_call = mutated_mod.get_global_var('func_11936')
call_11938 = func_11936_call(var_11937)
output = call_11938
func_11939 = relay.Function([var_11937], output)
mutated_mod['func_11939'] = func_11939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_12023 = func_11738_call()
call_12024 = func_11738_call()
func_11542_call = mod.get_global_var('func_11542')
func_11545_call = mutated_mod.get_global_var('func_11545')
var_12038 = relay.var("var_12038", dtype = "float64", shape = ())#candidate|12038|()|var|float64
var_12039 = relay.var("var_12039", dtype = "bool", shape = (495,))#candidate|12039|(495,)|var|bool
call_12037 = relay.TupleGetItem(func_11542_call(relay.reshape(var_12038.astype('float64'), []), relay.reshape(var_12039.astype('bool'), [495,]), ), 0)
call_12040 = relay.TupleGetItem(func_11545_call(relay.reshape(var_12038.astype('float64'), []), relay.reshape(var_12039.astype('bool'), [495,]), ), 0)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_12084 = func_11738_call()
call_12085 = func_11738_call()
func_11261_call = mod.get_global_var('func_11261')
func_11263_call = mutated_mod.get_global_var('func_11263')
call_12086 = relay.TupleGetItem(func_11261_call(), 0)
call_12087 = relay.TupleGetItem(func_11263_call(), 0)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_12113 = func_10099_call()
call_12114 = func_10099_call()
output = relay.Tuple([call_12023,call_12037,var_12038,var_12039,call_12084,call_12086,call_12113,])
output2 = relay.Tuple([call_12024,call_12040,var_12038,var_12039,call_12085,call_12087,call_12114,])
func_12123 = relay.Function([var_12038,var_12039,], output)
mod['func_12123'] = func_12123
mod = relay.transform.InferType()(mod)
mutated_mod['func_12123'] = func_12123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12123_call = mutated_mod.get_global_var('func_12123')
var_12125 = relay.var("var_12125", dtype = "float64", shape = ())#candidate|12125|()|var|float64
var_12126 = relay.var("var_12126", dtype = "bool", shape = (495,))#candidate|12126|(495,)|var|bool
call_12124 = func_12123_call(var_12125,var_12126,)
output = call_12124
func_12127 = relay.Function([var_12125,var_12126,], output)
mutated_mod['func_12127'] = func_12127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_12145 = relay.TupleGetItem(func_10485_call(), 0)
call_12146 = relay.TupleGetItem(func_10486_call(), 0)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
var_12153 = relay.var("var_12153", dtype = "int8", shape = (275, 2))#candidate|12153|(275, 2)|var|int8
call_12152 = relay.TupleGetItem(func_3434_call(relay.reshape(var_12153.astype('int8'), [10, 5, 11])), 0)
call_12154 = relay.TupleGetItem(func_3437_call(relay.reshape(var_12153.astype('int8'), [10, 5, 11])), 0)
bop_12160 = relay.logical_and(var_12153.astype('bool'), relay.reshape(call_12152.astype('bool'), relay.shape_of(var_12153))) # shape=(275, 2)
bop_12163 = relay.logical_and(var_12153.astype('bool'), relay.reshape(call_12154.astype('bool'), relay.shape_of(var_12153))) # shape=(275, 2)
uop_12173 = relay.log2(call_12152.astype('float32')) # shape=(10, 5, 11)
uop_12175 = relay.log2(call_12154.astype('float32')) # shape=(10, 5, 11)
bop_12177 = relay.less_equal(uop_12173.astype('bool'), relay.reshape(call_12152.astype('bool'), relay.shape_of(uop_12173))) # shape=(10, 5, 11)
bop_12180 = relay.less_equal(uop_12175.astype('bool'), relay.reshape(call_12154.astype('bool'), relay.shape_of(uop_12175))) # shape=(10, 5, 11)
var_12188 = relay.var("var_12188", dtype = "int8", shape = (275, 2))#candidate|12188|(275, 2)|var|int8
bop_12189 = relay.multiply(var_12153.astype('uint8'), relay.reshape(var_12188.astype('uint8'), relay.shape_of(var_12153))) # shape=(275, 2)
uop_12193 = relay.atan(uop_12173.astype('float32')) # shape=(10, 5, 11)
uop_12195 = relay.atan(uop_12175.astype('float32')) # shape=(10, 5, 11)
output = relay.Tuple([call_12145,bop_12160,bop_12177,bop_12189,uop_12193,])
output2 = relay.Tuple([call_12146,bop_12163,bop_12180,bop_12189,uop_12195,])
func_12198 = relay.Function([var_12153,var_12188,], output)
mod['func_12198'] = func_12198
mod = relay.transform.InferType()(mod)
mutated_mod['func_12198'] = func_12198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12198_call = mutated_mod.get_global_var('func_12198')
var_12200 = relay.var("var_12200", dtype = "int8", shape = (275, 2))#candidate|12200|(275, 2)|var|int8
var_12201 = relay.var("var_12201", dtype = "int8", shape = (275, 2))#candidate|12201|(275, 2)|var|int8
call_12199 = func_12198_call(var_12200,var_12201,)
output = call_12199
func_12202 = relay.Function([var_12200,var_12201,], output)
mutated_mod['func_12202'] = func_12202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10241_call = mod.get_global_var('func_10241')
func_10243_call = mutated_mod.get_global_var('func_10243')
call_12215 = func_10241_call()
call_12216 = func_10241_call()
output = call_12215
output2 = call_12216
func_12225 = relay.Function([], output)
mod['func_12225'] = func_12225
mod = relay.transform.InferType()(mod)
output = func_12225()
func_12226 = relay.Function([], output)
mutated_mod['func_12226'] = func_12226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_12232 = relay.TupleGetItem(func_10485_call(), 0)
call_12233 = relay.TupleGetItem(func_10486_call(), 0)
output = relay.Tuple([call_12232,])
output2 = relay.Tuple([call_12233,])
func_12234 = relay.Function([], output)
mod['func_12234'] = func_12234
mod = relay.transform.InferType()(mod)
output = func_12234()
func_12235 = relay.Function([], output)
mutated_mod['func_12235'] = func_12235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10450_call = mod.get_global_var('func_10450')
func_10451_call = mutated_mod.get_global_var('func_10451')
call_12241 = func_10450_call()
call_12242 = func_10450_call()
uop_12243 = relay.log2(call_12241.astype('float64')) # shape=(15, 9, 9)
uop_12245 = relay.log2(call_12242.astype('float64')) # shape=(15, 9, 9)
func_11542_call = mod.get_global_var('func_11542')
func_11545_call = mutated_mod.get_global_var('func_11545')
const_12267 = relay.const(6.985194, dtype = "float64")#candidate|12267|()|const|float64
const_12268 = relay.const([False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False], dtype = "bool")#candidate|12268|(495,)|const|bool
call_12266 = relay.TupleGetItem(func_11542_call(relay.reshape(const_12267.astype('float64'), []), relay.reshape(const_12268.astype('bool'), [495,]), ), 1)
call_12269 = relay.TupleGetItem(func_11545_call(relay.reshape(const_12267.astype('float64'), []), relay.reshape(const_12268.astype('bool'), [495,]), ), 1)
output = relay.Tuple([uop_12243,call_12266,const_12267,const_12268,])
output2 = relay.Tuple([uop_12245,call_12269,const_12267,const_12268,])
func_12277 = relay.Function([], output)
mod['func_12277'] = func_12277
mod = relay.transform.InferType()(mod)
mutated_mod['func_12277'] = func_12277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mutated_mod.get_global_var('func_12277')
call_12278 = func_12277_call()
output = call_12278
func_12279 = relay.Function([], output)
mutated_mod['func_12279'] = func_12279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_12285 = relay.TupleGetItem(func_10485_call(), 0)
call_12286 = relay.TupleGetItem(func_10486_call(), 0)
output = relay.Tuple([call_12285,])
output2 = relay.Tuple([call_12286,])
func_12287 = relay.Function([], output)
mod['func_12287'] = func_12287
mod = relay.transform.InferType()(mod)
mutated_mod['func_12287'] = func_12287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12287_call = mutated_mod.get_global_var('func_12287')
call_12288 = func_12287_call()
output = call_12288
func_12289 = relay.Function([], output)
mutated_mod['func_12289'] = func_12289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mod.get_global_var('func_12277')
func_12279_call = mutated_mod.get_global_var('func_12279')
call_12322 = relay.TupleGetItem(func_12277_call(), 3)
call_12323 = relay.TupleGetItem(func_12279_call(), 3)
output = relay.Tuple([call_12322,])
output2 = relay.Tuple([call_12323,])
func_12334 = relay.Function([], output)
mod['func_12334'] = func_12334
mod = relay.transform.InferType()(mod)
mutated_mod['func_12334'] = func_12334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12334_call = mutated_mod.get_global_var('func_12334')
call_12335 = func_12334_call()
output = call_12335
func_12336 = relay.Function([], output)
mutated_mod['func_12336'] = func_12336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_12337 = relay.TupleGetItem(func_10401_call(), 0)
call_12338 = relay.TupleGetItem(func_10403_call(), 0)
output = relay.Tuple([call_12337,])
output2 = relay.Tuple([call_12338,])
func_12368 = relay.Function([], output)
mod['func_12368'] = func_12368
mod = relay.transform.InferType()(mod)
mutated_mod['func_12368'] = func_12368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12368_call = mutated_mod.get_global_var('func_12368')
call_12369 = func_12368_call()
output = call_12369
func_12370 = relay.Function([], output)
mutated_mod['func_12370'] = func_12370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12234_call = mod.get_global_var('func_12234')
func_12235_call = mutated_mod.get_global_var('func_12235')
call_12388 = relay.TupleGetItem(func_12234_call(), 0)
call_12389 = relay.TupleGetItem(func_12235_call(), 0)
output = call_12388
output2 = call_12389
func_12428 = relay.Function([], output)
mod['func_12428'] = func_12428
mod = relay.transform.InferType()(mod)
mutated_mod['func_12428'] = func_12428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12428_call = mutated_mod.get_global_var('func_12428')
call_12429 = func_12428_call()
output = call_12429
func_12430 = relay.Function([], output)
mutated_mod['func_12430'] = func_12430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_12450 = func_10556_call()
call_12451 = func_10556_call()
var_12456 = relay.var("var_12456", dtype = "float32", shape = (15, 9, 9))#candidate|12456|(15, 9, 9)|var|float32
bop_12457 = relay.mod(call_12450.astype('float64'), relay.reshape(var_12456.astype('float64'), relay.shape_of(call_12450))) # shape=(15, 9, 9)
bop_12460 = relay.mod(call_12451.astype('float64'), relay.reshape(var_12456.astype('float64'), relay.shape_of(call_12451))) # shape=(15, 9, 9)
output = bop_12457
output2 = bop_12460
func_12475 = relay.Function([var_12456,], output)
mod['func_12475'] = func_12475
mod = relay.transform.InferType()(mod)
mutated_mod['func_12475'] = func_12475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12476 = relay.var("var_12476", dtype = "float32", shape = (15, 9, 9))#candidate|12476|(15, 9, 9)|var|float32
func_12475_call = mutated_mod.get_global_var('func_12475')
call_12477 = func_12475_call(var_12476)
output = call_12477
func_12478 = relay.Function([var_12476], output)
mutated_mod['func_12478'] = func_12478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10401_call = mod.get_global_var('func_10401')
func_10403_call = mutated_mod.get_global_var('func_10403')
call_12552 = relay.TupleGetItem(func_10401_call(), 0)
call_12553 = relay.TupleGetItem(func_10403_call(), 0)
func_10305_call = mod.get_global_var('func_10305')
func_10306_call = mutated_mod.get_global_var('func_10306')
call_12554 = func_10305_call()
call_12555 = func_10305_call()
output = relay.Tuple([call_12552,call_12554,])
output2 = relay.Tuple([call_12553,call_12555,])
func_12567 = relay.Function([], output)
mod['func_12567'] = func_12567
mod = relay.transform.InferType()(mod)
output = func_12567()
func_12568 = relay.Function([], output)
mutated_mod['func_12568'] = func_12568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_12586 = func_11738_call()
call_12587 = func_11738_call()
func_6067_call = mod.get_global_var('func_6067')
func_6073_call = mutated_mod.get_global_var('func_6073')
var_12597 = relay.var("var_12597", dtype = "uint16", shape = (1024,))#candidate|12597|(1024,)|var|uint16
const_12598 = relay.const([7.003014,2.734670,-1.971611,-7.419634,0.442331,7.590362,-3.528155,-8.781620,-0.633498,-6.332457,-0.515428,-1.449780,3.841402,-8.799417,-9.227037,9.468545,-8.323348,-8.588928,1.821122,-2.194279,-9.633294,5.657852,4.344176,-4.870851,4.964481,4.304597,-5.622978,3.378515,-5.743481,-7.264477,8.040851,-7.558001,-2.583201,-4.504702,-4.695853,-4.834578,-5.871068,0.746312,-2.184682,0.103385,-8.448244,7.122895,-6.632323,-4.072088,-6.105329,-0.406632,-1.031083,-9.926765,0.981699,-0.410428,7.870137,5.046983,-2.800137,9.883766,-2.028704,0.067239,9.810427,4.538797,1.929441,-7.109326,8.025834,6.191672,-5.281386,-5.890728,-5.931185,4.264331,-1.695842,9.546641,4.690452,2.076813,-2.764661,-3.869176,2.224213,2.583960,9.256451,0.373054,-0.842989,-7.511574,-3.026411,8.936562,-1.685105,-2.009902,5.201895,7.537939,-2.033678,-0.015623,2.162012,-2.892807,3.989972,-5.240585,4.488399,9.774441,-3.941231,-4.185314,-1.948654,-6.752202,-1.013988,6.153229,-9.803294,-1.427664,8.944182,4.425613,7.617211,-1.406262,-1.079423,6.237450,-9.006597,3.929443,3.510275,2.628554,2.857512,-2.748207,-9.868301,7.694319,-9.617489,5.443195,5.663622,6.099800,-3.665604,3.234418,-4.944264,-6.841030,2.024533,6.147186,-4.796589,-3.333210,-8.236497,9.860877,1.110567,-3.067351,6.547281,3.748287,-8.831551,0.038290,-9.893461,6.687063,-4.034389,2.553461,-4.716427,-7.940123,7.990164,-6.446531,2.682814,-8.643077,4.158621,-4.789020,-0.370640,7.651597,-3.735450,8.743441,1.167604,1.672281,4.815492,0.425529,-3.657915,-0.003753,-9.026127,5.203141,-0.053120,-6.067831,-6.266240,-6.092682,9.145270,-7.938764,5.007226,-4.635034,-9.824941,-9.711918,3.032110,3.466936,4.847670,7.434825,8.669452,2.744538,1.540055,6.522986,-5.616385,-6.017978,0.658863,-9.696111,6.451413,2.476417,-4.253377,9.650372,8.939925,4.769374,-8.739488,-4.499281,-5.309136,5.963346,-0.710421,2.849267,4.828047,-0.326843,-3.364231,3.698032,7.457157,-9.076211,-5.887617,8.247192,-0.217720,-4.349743,-2.941417,-3.092862,-6.287430,-4.999113,-2.098741,5.254212,0.674932,-3.396005,-1.334752,2.893689,-2.809129,-4.473599,7.268910,-3.640244,-0.757262,-2.153185,-1.403786,9.833860,3.882222,0.949597,-0.652912,2.179125,-4.026357,5.303679,2.234314,-2.639130,-7.804735,-1.330190,6.624201,-5.546318,8.292928,-4.745746,9.637368,-9.262842,4.731984,5.559723,-5.112099,3.155482,-0.047756,-1.188298,-9.302518,-4.872465,4.652276,-2.186116,0.840089,-9.574991,-2.987755,-5.470727,1.590190,-9.961283,-9.889319,-6.920468,-7.142145,5.363173,-8.217214,-4.960461,1.651654,-0.364925,2.796454,3.309922,3.313938,8.810185,-9.350650,9.657179,-7.308729,-0.155321,1.020569,7.616133,-7.589945,8.273654,-0.735219,4.643089,-8.904368,-9.527675,7.406258,-8.812091,-7.052107,-3.869099,-4.774606,-0.332134,8.241838,3.885234,1.989784,-3.151290,-8.041164,-8.942824,6.971486,-8.248416,4.556370,4.157998,-0.311790,8.653333,2.676143,6.801948,-8.449225,-9.263993,-8.988254,-4.828632,-4.075722,1.697649,-0.772243,-9.617173,-9.970167,8.297958,0.481873,-3.330268,5.382743,-4.842032,9.645512,-9.337101,0.757468,3.417804,-6.234357,8.349229,-8.184096,0.304163,8.986089,-5.477517,-1.301041,5.100617,-9.952335,8.279239,-3.741483,-3.700758,2.477639,3.749689,8.613925,-2.100126,-7.698160,-6.461215,1.299569,-1.811619,0.949741,-8.048831,-6.577073,-5.105506,5.911287,-0.709045,8.199737,5.130914,0.848368,-3.786553,3.540143,2.014058,-0.520812,-8.800221,9.142809,-1.322216,8.516609,2.108625,9.114903,-1.456586,4.643062,-4.783511,9.079061,-8.134294,-4.438989,0.356950,9.309264,8.822153,-9.159746,6.431913,-3.025163,7.701866,-9.922244,-4.316613,-1.678155,-3.698292,4.747986,-8.058717,-2.968582,-7.465332,5.789488,-0.824070,-0.610281,4.392901,6.215740,-4.167692,-3.464382,7.354050,-8.947712,-2.504051,-0.404895,7.027873,4.703814,-6.165052,-0.909488,-9.572171,-2.718100,-3.726035,4.657408,-6.299315,7.263360,-0.896870,-6.351008,-2.100083,5.372894,4.476441,-7.433288,-5.470832,-9.782644,5.993051,3.935476,4.932398,0.262713,-5.420317,2.799272,9.924681,7.901902,-9.832682,-8.510511,9.732674,-4.175210,1.249317,1.941561,-7.646351,7.609820,-5.922286,-0.935491,-1.305337,6.993488,-9.842590,8.505593,9.015063,6.890913,-4.947985,1.552282,-5.976477,-3.828592,-9.437108,4.221962,-2.122222,-9.585942,0.353912,-6.590838,-6.558952,-1.619304,-4.805404,0.344567,-9.789715,6.748681,-3.176932,-4.993022,-8.065535,-5.617930,-0.909534,-6.245348,-6.518405,2.457388,5.307555,-6.261265,-0.199591,-2.021121,-6.203362,-7.423552,-5.619527,-7.031928,-1.043726,6.547996,2.749690,4.102003,5.157314,-8.598079,9.054801,5.786649,1.205816,-1.442477,-8.400770,-7.454670,-5.472420,-2.443535,0.092657,7.631836,4.615710,-7.995928,4.717487,2.614385,9.420591,-3.031599,4.412250,7.917973,6.002363,-5.519873,-6.978451,5.952907,-9.310066,-2.700456,-0.833696,6.411068,-7.356295,-3.033363,-6.682114,0.199376,-0.602232,-4.414788,2.413785,-6.871265,5.511450,2.474729,-9.211053,9.802661,-4.999027,-8.230148,8.533042,-8.224388,9.998543,2.024268,-8.315497,-1.159251,1.713618,7.586549,-3.386044,7.811270,-0.421226,-5.044027,7.165530,0.614346,2.675232,-6.609276,-8.243011,-3.104494,-5.095096,8.250056,-4.622980,6.572762,-3.909865,0.176068,-9.082504,-5.809869,6.320241,8.933792,-8.366054,-3.119407,-6.944968,0.032701,9.199901,7.996348,5.096607,1.248437,-4.469860,7.762908,7.040538,7.225325,-5.407086,-1.770061,-1.482851,-5.171337,4.335177,-9.047115,-2.840318,-4.692798,-2.369123,7.940574,-3.342724,5.085224,7.500706,7.229130,7.279259,-5.872441,-8.916427,3.005717,7.637058,-6.636694,-5.643003,-6.140113,-4.824887,8.576455,-1.580979,-0.724566,4.728830,7.806515,5.592304,0.107995,-1.771073,-8.803232,-0.427985,6.420409,0.168447,-2.863926,3.403104,-2.621429,2.786607,-8.566866,-9.210908,-2.593110,-2.036118,-9.899032,-6.508426,8.608719,-4.883505,-0.274953,3.000823,-1.715421,6.557739,6.803486,9.102670,-7.806107,8.607450,2.767848,9.650264,0.466285,2.980990,1.215886,3.760888,-9.778844,-0.231243,-1.345219,5.146703,4.502313,-5.074703,5.705346,-8.460403,-6.372962,-2.948583,-9.839044,-7.438087,1.323517,4.136748,6.561550,6.083823,-3.915528,-0.851910,-8.957745,5.245153,-0.366827,-4.389921,-8.427606,5.553004], dtype = "float32")#candidate|12598|(630,)|const|float32
call_12596 = relay.TupleGetItem(func_6067_call(relay.reshape(var_12597.astype('uint16'), [16, 4, 16]), relay.reshape(var_12597.astype('uint16'), [16, 4, 16]), relay.reshape(const_12598.astype('float32'), [70, 9]), relay.reshape(var_12597.astype('bool'), [16, 4, 16]), ), 1)
call_12599 = relay.TupleGetItem(func_6073_call(relay.reshape(var_12597.astype('uint16'), [16, 4, 16]), relay.reshape(var_12597.astype('uint16'), [16, 4, 16]), relay.reshape(const_12598.astype('float32'), [70, 9]), relay.reshape(var_12597.astype('bool'), [16, 4, 16]), ), 1)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_12600 = relay.TupleGetItem(func_10933_call(), 0)
call_12601 = relay.TupleGetItem(func_10935_call(), 0)
output = relay.Tuple([call_12586,call_12596,var_12597,const_12598,call_12600,])
output2 = relay.Tuple([call_12587,call_12599,var_12597,const_12598,call_12601,])
func_12602 = relay.Function([var_12597,], output)
mod['func_12602'] = func_12602
mod = relay.transform.InferType()(mod)
var_12603 = relay.var("var_12603", dtype = "uint16", shape = (1024,))#candidate|12603|(1024,)|var|uint16
output = func_12602(var_12603)
func_12604 = relay.Function([var_12603], output)
mutated_mod['func_12604'] = func_12604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_12661 = func_11738_call()
call_12662 = func_11738_call()
output = call_12661
output2 = call_12662
func_12665 = relay.Function([], output)
mod['func_12665'] = func_12665
mod = relay.transform.InferType()(mod)
output = func_12665()
func_12666 = relay.Function([], output)
mutated_mod['func_12666'] = func_12666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_12770 = func_10099_call()
call_12771 = func_10099_call()
output = call_12770
output2 = call_12771
func_12779 = relay.Function([], output)
mod['func_12779'] = func_12779
mod = relay.transform.InferType()(mod)
mutated_mod['func_12779'] = func_12779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12779_call = mutated_mod.get_global_var('func_12779')
call_12780 = func_12779_call()
output = call_12780
func_12781 = relay.Function([], output)
mutated_mod['func_12781'] = func_12781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11872_call = mod.get_global_var('func_11872')
func_11873_call = mutated_mod.get_global_var('func_11873')
call_12795 = relay.TupleGetItem(func_11872_call(), 1)
call_12796 = relay.TupleGetItem(func_11873_call(), 1)
output = relay.Tuple([call_12795,])
output2 = relay.Tuple([call_12796,])
func_12800 = relay.Function([], output)
mod['func_12800'] = func_12800
mod = relay.transform.InferType()(mod)
mutated_mod['func_12800'] = func_12800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12800_call = mutated_mod.get_global_var('func_12800')
call_12801 = func_12800_call()
output = call_12801
func_12802 = relay.Function([], output)
mutated_mod['func_12802'] = func_12802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_12832 = relay.TupleGetItem(func_10933_call(), 0)
call_12833 = relay.TupleGetItem(func_10935_call(), 0)
func_12198_call = mod.get_global_var('func_12198')
func_12202_call = mutated_mod.get_global_var('func_12202')
const_12845 = relay.const([[1,-8,-9,-7,-6,-7,-2,-3,10,-4],[-1,-8,-8,-8,-2,8,10,-10,-9,-6],[-1,7,5,-10,6,-4,9,-4,10,-8],[4,8,9,3,-6,2,3,1,-9,-5],[-4,-4,2,-2,9,5,-3,7,2,2],[8,-7,5,-9,6,-1,-4,5,-2,8],[-8,-5,7,-5,-10,9,2,9,2,2],[-3,-10,8,2,-4,-3,7,-5,10,5],[8,-9,8,8,7,9,4,8,-5,-4],[-3,3,-7,-6,8,-8,-3,-7,-9,2],[4,8,9,2,6,-6,4,-1,-10,9],[-6,6,-8,-2,-7,-2,4,-1,-4,8],[2,1,5,-9,6,-5,-5,-2,4,-9],[-6,6,-1,-4,1,-6,-8,-10,-6,-10],[-5,5,-5,-4,-10,-4,3,8,-6,-8],[-4,3,-1,5,-10,-10,-9,8,3,-7],[-2,-1,10,7,-2,6,-9,-10,-9,-8],[9,5,-4,-5,4,9,-10,1,10,7],[-4,7,-9,-6,1,9,-3,-1,-9,1],[6,-1,10,8,1,1,-8,3,-5,-6],[-4,-8,3,-3,6,6,-5,2,-9,3],[-6,7,3,1,-8,6,-4,-10,-6,9],[-8,7,4,-9,10,2,8,-9,-9,1],[-7,-9,3,-8,-4,-2,4,8,-1,-10],[10,-6,-1,-9,5,-6,-9,3,-6,-1],[-8,5,-4,-9,-9,-5,-10,7,-8,-10],[8,-5,-4,-9,1,-3,4,-2,-2,-5],[-9,9,-1,-9,-5,-2,-8,2,-7,-4],[-10,9,6,2,2,8,8,-1,6,-10],[10,5,-10,1,7,-6,-2,-9,-8,-6],[-10,4,-4,9,-4,10,-2,3,4,-9],[-9,6,-10,2,7,8,4,7,6,7],[-4,5,6,8,-2,-10,2,4,2,1],[4,9,3,8,-2,9,-6,4,2,1],[-8,7,-7,-1,-5,-8,-2,-10,3,-4],[5,-4,8,4,-9,8,-5,7,-3,9],[-1,-10,-6,-7,10,-5,-5,-7,-7,4],[3,-5,-6,10,-1,9,8,8,-2,4],[-6,-7,7,5,3,10,-3,6,-7,9],[7,-3,-9,-8,6,3,2,5,1,3],[-1,-2,10,-4,-4,7,2,6,-1,-4],[-10,-10,-6,10,-7,3,-8,4,5,-6],[-10,-2,-5,8,5,-2,9,-7,-7,4],[2,1,4,-9,-3,8,10,-10,8,-10],[7,10,-3,3,-4,5,-4,-7,2,-7],[-2,10,3,-4,7,-6,7,-2,-2,2],[4,3,2,8,7,2,-8,-1,4,6],[1,-6,9,-9,-3,-9,6,6,-2,-5],[8,8,10,1,-7,3,-10,-6,-7,9],[6,8,8,2,-6,10,-4,4,-10,-6],[-3,-6,-8,-9,9,-6,6,7,-5,3],[-7,9,-1,-3,-7,9,8,2,-8,-2],[1,-2,-1,10,-1,9,-7,-7,-1,-1],[-9,-10,-6,4,5,2,5,2,6,-10],[-4,3,7,-10,-10,7,-1,-8,-1,-2]], dtype = "int8")#candidate|12845|(55, 10)|const|int8
call_12844 = relay.TupleGetItem(func_12198_call(relay.reshape(const_12845.astype('int8'), [275, 2]), relay.reshape(const_12845.astype('int8'), [275, 2]), ), 3)
call_12846 = relay.TupleGetItem(func_12202_call(relay.reshape(const_12845.astype('int8'), [275, 2]), relay.reshape(const_12845.astype('int8'), [275, 2]), ), 3)
func_5215_call = mod.get_global_var('func_5215')
func_5217_call = mutated_mod.get_global_var('func_5217')
var_12848 = relay.var("var_12848", dtype = "float64", shape = (175, 2))#candidate|12848|(175, 2)|var|float64
call_12847 = relay.TupleGetItem(func_5215_call(relay.reshape(var_12848.astype('float64'), [14, 5, 5])), 1)
call_12849 = relay.TupleGetItem(func_5217_call(relay.reshape(var_12848.astype('float64'), [14, 5, 5])), 1)
func_12567_call = mod.get_global_var('func_12567')
func_12568_call = mutated_mod.get_global_var('func_12568')
call_12854 = relay.TupleGetItem(func_12567_call(), 1)
call_12855 = relay.TupleGetItem(func_12568_call(), 1)
output = relay.Tuple([call_12832,call_12844,const_12845,call_12847,var_12848,call_12854,])
output2 = relay.Tuple([call_12833,call_12846,const_12845,call_12849,var_12848,call_12855,])
func_12860 = relay.Function([var_12848,], output)
mod['func_12860'] = func_12860
mod = relay.transform.InferType()(mod)
var_12861 = relay.var("var_12861", dtype = "float64", shape = (175, 2))#candidate|12861|(175, 2)|var|float64
output = func_12860(var_12861)
func_12862 = relay.Function([var_12861], output)
mutated_mod['func_12862'] = func_12862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11261_call = mod.get_global_var('func_11261')
func_11263_call = mutated_mod.get_global_var('func_11263')
call_12867 = relay.TupleGetItem(func_11261_call(), 0)
call_12868 = relay.TupleGetItem(func_11263_call(), 0)
output = call_12867
output2 = call_12868
func_12870 = relay.Function([], output)
mod['func_12870'] = func_12870
mod = relay.transform.InferType()(mod)
output = func_12870()
func_12871 = relay.Function([], output)
mutated_mod['func_12871'] = func_12871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_12888 = relay.TupleGetItem(func_10485_call(), 0)
call_12889 = relay.TupleGetItem(func_10486_call(), 0)
output = relay.Tuple([call_12888,])
output2 = relay.Tuple([call_12889,])
func_12890 = relay.Function([], output)
mod['func_12890'] = func_12890
mod = relay.transform.InferType()(mod)
mutated_mod['func_12890'] = func_12890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12890_call = mutated_mod.get_global_var('func_12890')
call_12891 = func_12890_call()
output = call_12891
func_12892 = relay.Function([], output)
mutated_mod['func_12892'] = func_12892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10450_call = mod.get_global_var('func_10450')
func_10451_call = mutated_mod.get_global_var('func_10451')
call_12926 = func_10450_call()
call_12927 = func_10450_call()
func_10539_call = mod.get_global_var('func_10539')
func_10541_call = mutated_mod.get_global_var('func_10541')
var_12930 = relay.var("var_12930", dtype = "float64", shape = (78,))#candidate|12930|(78,)|var|float64
call_12929 = func_10539_call(relay.reshape(var_12930.astype('float64'), [13, 2, 3]))
call_12931 = func_10539_call(relay.reshape(var_12930.astype('float64'), [13, 2, 3]))
output = relay.Tuple([call_12926,call_12929,var_12930,])
output2 = relay.Tuple([call_12927,call_12931,var_12930,])
func_12935 = relay.Function([var_12930,], output)
mod['func_12935'] = func_12935
mod = relay.transform.InferType()(mod)
mutated_mod['func_12935'] = func_12935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12936 = relay.var("var_12936", dtype = "float64", shape = (78,))#candidate|12936|(78,)|var|float64
func_12935_call = mutated_mod.get_global_var('func_12935')
call_12937 = func_12935_call(var_12936)
output = call_12937
func_12938 = relay.Function([var_12936], output)
mutated_mod['func_12938'] = func_12938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12287_call = mod.get_global_var('func_12287')
func_12289_call = mutated_mod.get_global_var('func_12289')
call_12940 = relay.TupleGetItem(func_12287_call(), 0)
call_12941 = relay.TupleGetItem(func_12289_call(), 0)
func_12602_call = mod.get_global_var('func_12602')
func_12604_call = mutated_mod.get_global_var('func_12604')
const_12961 = relay.const([-9,-1,1,4,-9,-3,7,5,1,2,10,-4,-4,8,6,3,6,-10,5,6,8,8,-5,-5,-9,-2,2,-4,6,4,-3,-9,3,10,5,2,7,-9,5,9,-4,4,8,4,2,-5,-5,8,6,-7,-5,-4,-7,3,8,7,-4,10,1,-5,10,-9,-4,6,-4,1,-10,-10,-10,10,-8,2,9,5,3,-2,9,1,-6,-5,8,10,3,-8,6,10,4,-7,1,-3,-9,9,-4,-3,-7,-3,-4,-6,4,9,1,-3,1,-8,-1,9,5,9,-10,2,-1,-4,-9,-2,-4,4,-10,10,6,-4,-8,8,-2,-5,-9,10,1,5,-4,-4,9,4,4,3,-2,8,1,-5,4,5,-4,-3,7,-6,8,1,-7,-1,9,-4,2,-2,9,7,-5,7,5,8,-2,7,6,9,3,6,-3,-2,2,9,-1,-5,1,8,3,-10,-2,-3,6,-4,2,-10,10,-2,-6,-6,-9,3,-2,-6,9,-8,-6,9,-4,1,-3,-1,-3,-5,-3,-5,-1,-2,1,8,7,-1,8,5,3,8,-4,-8,3,7,-6,8,-3,10,2,6,-3,-2,-8,-3,-10,-8,-1,3,-2,9,5,5,10,5,-3,-3,9,5,2,-2,-8,-1,7,-2,6,-4,9,-10,5,2,6,2,1,-7,-5,9,9,4,-4,2,-8,-1,-6,-5,-4,-6,-2,-10,-8,-10,-5,-8,-7,-8,-1,-2,-7,-5,4,3,-8,-10,7,-5,-6,10,2,-4,2,-3,-2,-9,8,1,3,9,3,2,-9,7,-2,7,-4,-6,-4,-9,-3,-5,-2,10,10,-9,-1,5,9,-7,8,8,6,-10,4,7,8,8,-6,-7,10,-9,6,10,7,-6,-1,1,-10,-10,-10,10,6,-8,-6,1,9,-6,-6,-10,-4,-2,-3,-4,3,5,-8,-9,-3,-9,2,-7,-1,-5,9,-2,2,-10,6,-5,-6,10,7,2,-8,1,10,8,2,8,9,-6,3,-5,10,6,4,1,7,1,4,-3,1,6,7,7,-4,-6,-9,-6,4,-4,-7,-8,-10,-10,-1,9,-6,-5,8,8,7,9,-6,-4,6,-1,-6,-9,-9,1,4,2,-6,3,-1,6,-7,-1,-9,-5,6,7,-6,8,-9,-5,-10,3,4,-10,8,-2,-2,-8,-9,-3,9,-6,-10,10,3,2,-4,1,-2,-4,10,5,-8,-10,-8,-1,7,-3,2,-6,-1,-10,5,3,-6,-10,-3,-6,-10,8,-1,6,-6,7,-6,-3,-1,-2,-8,-6,3,1,-2,7,-5,-1,-5,6,-8,9,8,-1,-9,-7,-9,1,8,-8,-1,2,1,4,-10,7,-7,-2,-10,-4,-5,8,-4,5,-1,2,-9,9,8,8,-8,-6,1,8,10,-2,2,8,-9,8,8,-5,4,9,-9,-8,1,-2,3,-6,1,-7,-10,-1,-9,-2,-8,-4,-10,4,9,6,7,2,7,4,-8,3,7,-8,4,3,-4,6,-9,5,2,8,9,-3,10,6,-8,5,-4,2,-2,2,2,-1,-6,-1,-10,-2,-10,7,2,-7,6,-8,4,8,6,5,-8,1,5,-6,10,3,-3,-8,-6,7,-7,-2,-6,-1,2,2,-2,-6,2,9,-10,-2,5,-9,-4,-4,-3,6,-9,-4,10,-3,-7,-9,-10,3,-1,4,6,8,2,-3,-8,-6,5,-10,-6,-9,-1,-3,7,3,-10,3,-4,6,-2,-3,-9,7,-9,-8,9,7,6,-5,6,10,-6,-4,5,-8,-10,-5,-2,-2,9,-5,7,-10,-3,-5,-2,-7,-9,1,-2,9,2,10,8,4,-1,-8,2,-1,-5,-6,-1,-9,5,-4,-1,-8,1,-6,1,8,8,10,6,-8,10,-7,-8,-3,6,-1,-2,-9,-8,-2,4,1,-6,5,4,2,-7,9,7,10,1,2,10,-8,8,-9,10,6,1,-9,-3,3,1,-5,5,-4,7,-4,9,7,-2,10,6,-9,5,4,-10,-8,-10,-1,-8,-3,-3,2,-9,-7,-7,2,-1,10,10,6,2,4,8,-9,2,-1,-1,5,6,-8,9,6,-2,7,-4,-3,-6,-8,-2,-3,1,9,9,-9,-6,-9,8,6,-4,3,6,4,-2,-8,-1,9,7,1,2,2,-8,6,6,7,4,6,5,6,2,4,-7,5,-10,9,-6,-3,-1,10,10,-5,-7,-8,3,-2,10,-10,8,10,-2,2,-9,2,-6,7,-2,-2,-7,3,-4,7,-2,10,2,8,8,-2,8,9,8,10,2,9,2,-9,9,-2,-1,-1,-2,-9,-2,9,4,-2,6,10,-5,7,-1,6,2,-10,-2,-8,-1,-5,7,-1,-4,3,6,-9,-2,-10,3,-4,-6,10,5,-2,-4,-9,3,-1,-4,8,-8,3,-3,7,-1,-3,-5,-6,-10,9,7,4,-10,8,9,-4,-3,9,1,2,-6,10,-7,-4,-7,10,2,6,6,6,8,-4,-8,-6,8,-3,-4,-6,9,7,-4,10,8,-8,9,-2,5,-9,9,-3,5,1,-1,10,6,6,2,-8,1,7,-1,7,6,-10,-1,-2,-9,6,2,9,-3,10,2,-10,-5,5,7,-1,-9,-8,3,7,-6,3,-10,6,9,1,-5,6,-9,5,2,8,6,-2,-9,3,5,-3,-8,10,-6,-9,-3,10,-6,7,10,1,-3,-7,5,8,-5,5,-10,1], dtype = "uint16")#candidate|12961|(1024,)|const|uint16
call_12960 = relay.TupleGetItem(func_12602_call(relay.reshape(const_12961.astype('uint16'), [1024,])), 1)
call_12962 = relay.TupleGetItem(func_12604_call(relay.reshape(const_12961.astype('uint16'), [1024,])), 1)
uop_12968 = relay.rsqrt(call_12960.astype('float64')) # shape=(70, 9)
uop_12970 = relay.rsqrt(call_12962.astype('float64')) # shape=(70, 9)
output = relay.Tuple([call_12940,const_12961,uop_12968,])
output2 = relay.Tuple([call_12941,const_12961,uop_12970,])
func_12990 = relay.Function([], output)
mod['func_12990'] = func_12990
mod = relay.transform.InferType()(mod)
output = func_12990()
func_12991 = relay.Function([], output)
mutated_mod['func_12991'] = func_12991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10241_call = mod.get_global_var('func_10241')
func_10243_call = mutated_mod.get_global_var('func_10243')
call_12992 = func_10241_call()
call_12993 = func_10241_call()
output = call_12992
output2 = call_12993
func_12999 = relay.Function([], output)
mod['func_12999'] = func_12999
mod = relay.transform.InferType()(mod)
output = func_12999()
func_13000 = relay.Function([], output)
mutated_mod['func_13000'] = func_13000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_13029 = func_10556_call()
call_13030 = func_10556_call()
func_11542_call = mod.get_global_var('func_11542')
func_11545_call = mutated_mod.get_global_var('func_11545')
var_13039 = relay.var("var_13039", dtype = "float64", shape = ())#candidate|13039|()|var|float64
var_13040 = relay.var("var_13040", dtype = "bool", shape = (495,))#candidate|13040|(495,)|var|bool
call_13038 = relay.TupleGetItem(func_11542_call(relay.reshape(var_13039.astype('float64'), []), relay.reshape(var_13040.astype('bool'), [495,]), ), 4)
call_13041 = relay.TupleGetItem(func_11545_call(relay.reshape(var_13039.astype('float64'), []), relay.reshape(var_13040.astype('bool'), [495,]), ), 4)
output = relay.Tuple([call_13029,call_13038,var_13039,var_13040,])
output2 = relay.Tuple([call_13030,call_13041,var_13039,var_13040,])
func_13059 = relay.Function([var_13039,var_13040,], output)
mod['func_13059'] = func_13059
mod = relay.transform.InferType()(mod)
var_13060 = relay.var("var_13060", dtype = "float64", shape = ())#candidate|13060|()|var|float64
var_13061 = relay.var("var_13061", dtype = "bool", shape = (495,))#candidate|13061|(495,)|var|bool
output = func_13059(var_13060,var_13061,)
func_13062 = relay.Function([var_13060,var_13061,], output)
mutated_mod['func_13062'] = func_13062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11872_call = mod.get_global_var('func_11872')
func_11873_call = mutated_mod.get_global_var('func_11873')
call_13081 = relay.TupleGetItem(func_11872_call(), 1)
call_13082 = relay.TupleGetItem(func_11873_call(), 1)
output = call_13081
output2 = call_13082
func_13095 = relay.Function([], output)
mod['func_13095'] = func_13095
mod = relay.transform.InferType()(mod)
output = func_13095()
func_13096 = relay.Function([], output)
mutated_mod['func_13096'] = func_13096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12665_call = mod.get_global_var('func_12665')
func_12666_call = mutated_mod.get_global_var('func_12666')
call_13137 = func_12665_call()
call_13138 = func_12665_call()
func_12368_call = mod.get_global_var('func_12368')
func_12370_call = mutated_mod.get_global_var('func_12370')
call_13145 = relay.TupleGetItem(func_12368_call(), 0)
call_13146 = relay.TupleGetItem(func_12370_call(), 0)
func_12277_call = mod.get_global_var('func_12277')
func_12279_call = mutated_mod.get_global_var('func_12279')
call_13148 = relay.TupleGetItem(func_12277_call(), 1)
call_13149 = relay.TupleGetItem(func_12279_call(), 1)
output = relay.Tuple([call_13137,call_13145,call_13148,])
output2 = relay.Tuple([call_13138,call_13146,call_13149,])
func_13178 = relay.Function([], output)
mod['func_13178'] = func_13178
mod = relay.transform.InferType()(mod)
mutated_mod['func_13178'] = func_13178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13178_call = mutated_mod.get_global_var('func_13178')
call_13179 = func_13178_call()
output = call_13179
func_13180 = relay.Function([], output)
mutated_mod['func_13180'] = func_13180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_13227 = func_10556_call()
call_13228 = func_10556_call()
func_11780_call = mod.get_global_var('func_11780')
func_11782_call = mutated_mod.get_global_var('func_11782')
call_13243 = relay.TupleGetItem(func_11780_call(), 0)
call_13244 = relay.TupleGetItem(func_11782_call(), 0)
func_11561_call = mod.get_global_var('func_11561')
func_11563_call = mutated_mod.get_global_var('func_11563')
call_13249 = relay.TupleGetItem(func_11561_call(), 1)
call_13250 = relay.TupleGetItem(func_11563_call(), 1)
func_12602_call = mod.get_global_var('func_12602')
func_12604_call = mutated_mod.get_global_var('func_12604')
var_13253 = relay.var("var_13253", dtype = "uint16", shape = (1024,))#candidate|13253|(1024,)|var|uint16
call_13252 = relay.TupleGetItem(func_12602_call(relay.reshape(var_13253.astype('uint16'), [1024,])), 1)
call_13254 = relay.TupleGetItem(func_12604_call(relay.reshape(var_13253.astype('uint16'), [1024,])), 1)
output = relay.Tuple([call_13227,call_13243,call_13249,call_13252,var_13253,])
output2 = relay.Tuple([call_13228,call_13244,call_13250,call_13254,var_13253,])
func_13260 = relay.Function([var_13253,], output)
mod['func_13260'] = func_13260
mod = relay.transform.InferType()(mod)
mutated_mod['func_13260'] = func_13260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13261 = relay.var("var_13261", dtype = "uint16", shape = (1024,))#candidate|13261|(1024,)|var|uint16
func_13260_call = mutated_mod.get_global_var('func_13260')
call_13262 = func_13260_call(var_13261)
output = call_13262
func_13263 = relay.Function([var_13261], output)
mutated_mod['func_13263'] = func_13263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10305_call = mod.get_global_var('func_10305')
func_10306_call = mutated_mod.get_global_var('func_10306')
call_13265 = func_10305_call()
call_13266 = func_10305_call()
output = relay.Tuple([call_13265,])
output2 = relay.Tuple([call_13266,])
func_13273 = relay.Function([], output)
mod['func_13273'] = func_13273
mod = relay.transform.InferType()(mod)
output = func_13273()
func_13274 = relay.Function([], output)
mutated_mod['func_13274'] = func_13274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11796_call = mod.get_global_var('func_11796')
func_11797_call = mutated_mod.get_global_var('func_11797')
call_13302 = func_11796_call()
call_13303 = func_11796_call()
output = relay.Tuple([call_13302,])
output2 = relay.Tuple([call_13303,])
func_13318 = relay.Function([], output)
mod['func_13318'] = func_13318
mod = relay.transform.InferType()(mod)
output = func_13318()
func_13319 = relay.Function([], output)
mutated_mod['func_13319'] = func_13319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12890_call = mod.get_global_var('func_12890')
func_12892_call = mutated_mod.get_global_var('func_12892')
call_13363 = relay.TupleGetItem(func_12890_call(), 0)
call_13364 = relay.TupleGetItem(func_12892_call(), 0)
output = relay.Tuple([call_13363,])
output2 = relay.Tuple([call_13364,])
func_13365 = relay.Function([], output)
mod['func_13365'] = func_13365
mod = relay.transform.InferType()(mod)
output = func_13365()
func_13366 = relay.Function([], output)
mutated_mod['func_13366'] = func_13366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10305_call = mod.get_global_var('func_10305')
func_10306_call = mutated_mod.get_global_var('func_10306')
call_13367 = func_10305_call()
call_13368 = func_10305_call()
output = call_13367
output2 = call_13368
func_13380 = relay.Function([], output)
mod['func_13380'] = func_13380
mod = relay.transform.InferType()(mod)
mutated_mod['func_13380'] = func_13380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13380_call = mutated_mod.get_global_var('func_13380')
call_13381 = func_13380_call()
output = call_13381
func_13382 = relay.Function([], output)
mutated_mod['func_13382'] = func_13382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12779_call = mod.get_global_var('func_12779')
func_12781_call = mutated_mod.get_global_var('func_12781')
call_13410 = func_12779_call()
call_13411 = func_12779_call()
func_12198_call = mod.get_global_var('func_12198')
func_12202_call = mutated_mod.get_global_var('func_12202')
var_13413 = relay.var("var_13413", dtype = "int8", shape = (550,))#candidate|13413|(550,)|var|int8
call_13412 = relay.TupleGetItem(func_12198_call(relay.reshape(var_13413.astype('int8'), [275, 2]), relay.reshape(var_13413.astype('int8'), [275, 2]), ), 1)
call_13414 = relay.TupleGetItem(func_12202_call(relay.reshape(var_13413.astype('int8'), [275, 2]), relay.reshape(var_13413.astype('int8'), [275, 2]), ), 1)
output = relay.Tuple([call_13410,call_13412,var_13413,])
output2 = relay.Tuple([call_13411,call_13414,var_13413,])
func_13418 = relay.Function([var_13413,], output)
mod['func_13418'] = func_13418
mod = relay.transform.InferType()(mod)
var_13419 = relay.var("var_13419", dtype = "int8", shape = (550,))#candidate|13419|(550,)|var|int8
output = func_13418(var_13419)
func_13420 = relay.Function([var_13419], output)
mutated_mod['func_13420'] = func_13420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_13436 = relay.TupleGetItem(func_11409_call(), 2)
call_13437 = relay.TupleGetItem(func_11410_call(), 2)
output = relay.Tuple([call_13436,])
output2 = relay.Tuple([call_13437,])
func_13445 = relay.Function([], output)
mod['func_13445'] = func_13445
mod = relay.transform.InferType()(mod)
mutated_mod['func_13445'] = func_13445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13445_call = mutated_mod.get_global_var('func_13445')
call_13446 = func_13445_call()
output = call_13446
func_13447 = relay.Function([], output)
mutated_mod['func_13447'] = func_13447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12287_call = mod.get_global_var('func_12287')
func_12289_call = mutated_mod.get_global_var('func_12289')
call_13488 = relay.TupleGetItem(func_12287_call(), 0)
call_13489 = relay.TupleGetItem(func_12289_call(), 0)
func_12368_call = mod.get_global_var('func_12368')
func_12370_call = mutated_mod.get_global_var('func_12370')
call_13495 = relay.TupleGetItem(func_12368_call(), 0)
call_13496 = relay.TupleGetItem(func_12370_call(), 0)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_13498 = func_11738_call()
call_13499 = func_11738_call()
func_11872_call = mod.get_global_var('func_11872')
func_11873_call = mutated_mod.get_global_var('func_11873')
call_13506 = relay.TupleGetItem(func_11872_call(), 1)
call_13507 = relay.TupleGetItem(func_11873_call(), 1)
output = relay.Tuple([call_13488,call_13495,call_13498,call_13506,])
output2 = relay.Tuple([call_13489,call_13496,call_13499,call_13507,])
func_13512 = relay.Function([], output)
mod['func_13512'] = func_13512
mod = relay.transform.InferType()(mod)
mutated_mod['func_13512'] = func_13512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13512_call = mutated_mod.get_global_var('func_13512')
call_13513 = func_13512_call()
output = call_13513
func_13514 = relay.Function([], output)
mutated_mod['func_13514'] = func_13514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12567_call = mod.get_global_var('func_12567')
func_12568_call = mutated_mod.get_global_var('func_12568')
call_13526 = relay.TupleGetItem(func_12567_call(), 0)
call_13527 = relay.TupleGetItem(func_12568_call(), 0)
output = call_13526
output2 = call_13527
func_13534 = relay.Function([], output)
mod['func_13534'] = func_13534
mod = relay.transform.InferType()(mod)
mutated_mod['func_13534'] = func_13534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13534_call = mutated_mod.get_global_var('func_13534')
call_13535 = func_13534_call()
output = call_13535
func_13536 = relay.Function([], output)
mutated_mod['func_13536'] = func_13536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12368_call = mod.get_global_var('func_12368')
func_12370_call = mutated_mod.get_global_var('func_12370')
call_13592 = relay.TupleGetItem(func_12368_call(), 0)
call_13593 = relay.TupleGetItem(func_12370_call(), 0)
func_12990_call = mod.get_global_var('func_12990')
func_12991_call = mutated_mod.get_global_var('func_12991')
call_13612 = relay.TupleGetItem(func_12990_call(), 0)
call_13613 = relay.TupleGetItem(func_12991_call(), 0)
func_12123_call = mod.get_global_var('func_12123')
func_12127_call = mutated_mod.get_global_var('func_12127')
var_13636 = relay.var("var_13636", dtype = "float64", shape = ())#candidate|13636|()|var|float64
const_13637 = relay.const([True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,False], dtype = "bool")#candidate|13637|(495,)|const|bool
call_13635 = relay.TupleGetItem(func_12123_call(relay.reshape(var_13636.astype('float64'), []), relay.reshape(const_13637.astype('bool'), [495,]), ), 6)
call_13638 = relay.TupleGetItem(func_12127_call(relay.reshape(var_13636.astype('float64'), []), relay.reshape(const_13637.astype('bool'), [495,]), ), 6)
output = relay.Tuple([call_13592,call_13612,call_13635,var_13636,const_13637,])
output2 = relay.Tuple([call_13593,call_13613,call_13638,var_13636,const_13637,])
func_13643 = relay.Function([var_13636,], output)
mod['func_13643'] = func_13643
mod = relay.transform.InferType()(mod)
mutated_mod['func_13643'] = func_13643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13644 = relay.var("var_13644", dtype = "float64", shape = ())#candidate|13644|()|var|float64
func_13643_call = mutated_mod.get_global_var('func_13643')
call_13645 = func_13643_call(var_13644)
output = call_13645
func_13646 = relay.Function([var_13644], output)
mutated_mod['func_13646'] = func_13646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13445_call = mod.get_global_var('func_13445')
func_13447_call = mutated_mod.get_global_var('func_13447')
call_13662 = relay.TupleGetItem(func_13445_call(), 0)
call_13663 = relay.TupleGetItem(func_13447_call(), 0)
output = relay.Tuple([call_13662,])
output2 = relay.Tuple([call_13663,])
func_13692 = relay.Function([], output)
mod['func_13692'] = func_13692
mod = relay.transform.InferType()(mod)
mutated_mod['func_13692'] = func_13692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13692_call = mutated_mod.get_global_var('func_13692')
call_13693 = func_13692_call()
output = call_13693
func_13694 = relay.Function([], output)
mutated_mod['func_13694'] = func_13694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12990_call = mod.get_global_var('func_12990')
func_12991_call = mutated_mod.get_global_var('func_12991')
call_13722 = relay.TupleGetItem(func_12990_call(), 0)
call_13723 = relay.TupleGetItem(func_12991_call(), 0)
output = call_13722
output2 = call_13723
func_13739 = relay.Function([], output)
mod['func_13739'] = func_13739
mod = relay.transform.InferType()(mod)
output = func_13739()
func_13740 = relay.Function([], output)
mutated_mod['func_13740'] = func_13740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11796_call = mod.get_global_var('func_11796')
func_11797_call = mutated_mod.get_global_var('func_11797')
call_13743 = func_11796_call()
call_13744 = func_11796_call()
func_11601_call = mod.get_global_var('func_11601')
func_11605_call = mutated_mod.get_global_var('func_11605')
const_13755 = relay.const([[-4.292927],[1.147819],[0.140630],[0.993353],[-1.464193],[-4.807737],[-5.306074],[8.296498],[5.288327],[4.137731],[3.054103],[-7.982710],[-1.030305],[2.803377],[4.701396],[6.964448],[1.685835],[-8.594890],[5.022700],[9.737927],[5.363174],[-0.754291],[5.280201],[-9.780779],[9.668308],[7.493784],[-0.139570],[-1.345744],[2.420171],[5.417770],[-2.193519],[-5.885108],[5.465658],[-2.028026],[-0.075351],[-0.690802],[1.583609],[9.722740],[9.714792],[-2.214978],[1.179483],[2.657821],[7.163627],[-0.028055],[4.100419],[7.284472],[5.634373],[5.137985],[9.833134],[4.505463],[1.627410],[8.280744],[-7.649528],[2.824184],[-1.422788],[2.260311],[5.960254],[1.450330],[-3.455295],[7.123382],[2.583081],[1.980111],[-5.976479],[9.566838],[-0.396434],[-5.432707],[-0.050570],[-5.272001],[-7.596140],[-3.221499],[0.184958],[8.756642],[-8.310339],[-0.926436],[-7.386688],[-6.598063],[-6.042565],[-5.730036],[8.143334],[-5.121817],[-8.136189],[6.145237],[-8.762990],[-5.253329],[-7.723541],[8.859218],[-9.397078],[-3.251868],[6.271345],[9.256608],[6.609028],[7.004898],[6.194096],[-1.371837],[4.288324],[-9.011840],[3.871118],[8.787037],[3.352410],[2.159839],[-2.493073],[-9.756652],[3.148483],[-2.905775],[4.251407],[-2.417783],[6.611691],[-4.546369],[-6.857008],[3.659039],[-7.438673],[1.770116],[-7.266710],[0.260733],[-2.126837],[2.747280],[-5.453641],[0.978523],[-1.787913],[-3.041321],[1.540216],[-8.189174],[5.892358],[9.691411],[-6.535594],[8.185283],[-8.896948],[-8.911716],[0.381888],[9.932142],[-8.612472],[5.441574],[-9.511822],[-5.355797],[-3.716163],[-5.167829],[-5.118715],[-7.406079],[2.849195],[1.376233],[2.387845],[-1.451662],[9.258276],[-1.552980],[7.642348],[6.322175],[-4.573218],[-1.075947],[7.534417],[5.249118],[1.742264],[-1.039208],[0.254051],[2.692633],[-8.662988],[-4.926896],[-3.962815],[-9.147620],[7.298130],[-2.653665],[-4.268720],[1.847165],[-5.759783],[2.891854],[-0.455009],[9.046687],[-1.456167],[1.042861],[0.641438],[-1.633220],[5.429718],[8.025795],[-0.642298],[-7.142515],[-2.304075],[-9.192954],[-6.244219],[9.632432],[2.813242],[-6.913206],[1.946251],[6.861327],[3.792899],[4.021405],[-3.370498],[6.326407],[-4.161098],[2.374500],[-9.084443],[3.892357],[-7.519984],[8.653993],[0.751685],[-1.066708],[6.559054],[-8.086514],[-2.856018],[-8.636816],[3.706263],[-8.502228],[0.536109],[2.066734],[-0.514813],[-6.365477],[-9.869154],[9.297600],[1.917204],[9.622404],[9.296926],[6.729125],[5.769135],[-8.167738],[-4.078221],[8.565085],[-9.912828],[9.269421],[4.212068],[-7.965001],[0.365921],[-1.640079],[-6.149550],[-8.978965],[-9.329070],[-8.694668],[6.360823],[-0.079832],[7.322654],[3.065988],[2.774327],[7.954699],[-0.348580],[-6.998776],[-3.709651],[-7.318175],[9.882925],[0.046780],[-9.573197],[-0.824154],[-0.361422],[3.151225],[-0.326919],[-5.506110],[-7.010153],[1.002024],[-1.021045],[8.834831],[7.694823],[3.047910],[-4.304704],[2.613899],[-6.435519],[9.442271],[9.476285],[-0.199250],[-2.053931],[3.262474],[0.540065],[9.495448],[8.562561],[-0.949856],[0.615902],[2.515125],[0.322101],[-8.435608],[-7.211138],[9.771682],[5.411164],[4.663690],[-1.447411],[-7.157736],[5.195788],[-7.013125],[5.848162],[-7.364865],[-1.685998],[-3.647805],[8.762699],[7.908617],[-3.809675],[-6.419432],[8.837173],[-3.331833],[5.580345],[1.548483],[9.219055],[-8.049895],[-9.619999],[0.935103],[-1.748121],[-6.706012],[-2.618622],[8.698848],[-3.382740],[-9.855919],[-5.650282],[8.659254],[8.786366],[-3.415159],[-2.342763],[-2.268729],[4.230606],[-8.933682],[7.346307],[7.667582],[-1.098433],[2.440875],[8.979883],[-5.302038],[4.820341],[-0.948512],[4.546753],[1.054981],[4.433520],[8.962916],[-0.687551],[4.163298],[7.656460],[4.261277],[-1.339965],[-7.077912],[-6.987512],[1.009054],[-6.001444],[-3.788705],[7.752271],[-1.898849],[-0.484849],[9.472112],[0.152664],[8.128942],[-9.889010],[-6.995728],[8.468263],[6.610776],[-8.899391],[-8.296804],[5.489092],[-9.004005],[4.496215],[4.637375],[-9.782637],[3.285308],[1.371858],[-4.907618],[-7.837026],[-7.302864],[4.327844],[-4.100826],[-8.504194],[-0.655286],[7.849841],[-6.752274],[-1.945739],[9.353229],[3.100546],[-7.306552],[-9.182408],[-4.281514],[-6.364578],[-9.442384],[2.796363],[-5.655412],[1.091506],[8.292044],[-1.602179],[6.195799],[-8.046366],[-1.472533],[-3.602413],[-4.780149],[-4.948065],[1.301756],[-0.848996],[-7.035320],[2.942445],[4.716697],[-7.760682],[7.754986],[-7.362488],[3.987651],[-7.651697],[3.396434],[-6.826623],[1.282891],[5.638460],[-8.645956],[7.615178],[-3.964097],[-9.937198],[-7.902522]], dtype = "float64")#candidate|13755|(390, 1)|const|float64
const_13756 = relay.const([-5,-8,6,7,-2,8,-2,8,4,1,5,9,10,6,7,4,4,7,9,-3,-7,-7,-9,-8,-4,8,6,-7,9,10,-5,-2,-8,6,-10,-10,-10,-5,-1,4,2,7,1,-2,-7,10,9,-10,8,-6,-5,-7,-3,-5,-7,-10,-1,7,-10,4,-3,1,4], dtype = "uint32")#candidate|13756|(63,)|const|uint32
const_13757 = relay.const([5.084557,-8.208944,2.716152,9.698497,1.782205,7.916520,-5.732460,-5.596988,-2.298143,8.809546,5.579813,6.498843,-6.049713,-0.784848,-9.195546,-8.332943,6.920168,-5.453916,2.709865,-5.936442,-1.214546,-0.369525,-0.044026,-8.251743,1.299646,4.902631,0.748266,0.383171,7.879218,3.011439,-2.607508,8.027754,-0.142223,-1.183498,-8.488668,2.610907,-9.205514,8.224497,-3.993019,-5.214899,6.564594,-7.013866,-7.507063,3.518407,4.887135,9.986782,-5.661058,5.704703,7.098401,-4.786879,-7.672012,-9.122008,-9.960922,-7.555524,1.958936,-0.625700,-9.073698,7.679251,-2.615175,-2.909272,8.683298,6.279529,-3.056697,0.586765,-0.027796,9.274290,6.302138,-0.165415,-2.142484,-6.076188,9.187573,-3.062685,5.840375,-5.768204,-6.560130,3.262277,-9.728248,-9.647579,4.070218,-5.603147,4.677552,-4.321159,6.841108,-2.572935,9.654466,-4.521079,-6.998397,-3.684491,-6.690378,5.634484,6.257706,2.664827,-6.698478,2.939834,5.129151,0.618257,7.769612,5.221651,-3.379051,-1.408429,-9.127390,-3.281714,-2.560246,-0.171914,8.997622,2.354463,-8.016377,9.761706,-6.517206,-9.556437,-5.727547,2.618227,7.240992,8.858466,-0.240440,-7.324731,-0.434236,2.475247,2.770524,4.740319,-5.439565,-3.113771,6.948259,2.590685,-7.503966,7.217347,4.301018,-1.569553,5.819268,2.835298,-5.277824,-3.260562,-0.940147,6.649899,7.311328,3.598742,5.802321,-3.581424,9.448603,2.068152,7.651708,-3.065489,3.388567,-8.422136,-2.958362,-3.362118,7.198814,4.299398,1.522859,4.080688,-9.821794,-8.231255,-0.893870,-1.303099,-9.999557,5.011421,4.479808,-9.670873,7.784658,3.512511,-7.057538,-8.682663,8.422567,-9.264388,-4.704847,7.445046,-8.778054,-4.682076,4.050629,-3.245409,-9.587283,7.994729,8.867504,-7.129894,-4.886547,5.317911,-3.966937,-5.626302,1.375714,-9.105323,5.748230,-9.028555,5.301861,-3.980844,-5.697878,-3.076064,4.931215,-2.141140,6.904999,5.507780,-8.980867,5.864200,-2.946533,-9.860227,-8.031344,3.606450,7.467240,5.165719,-4.603136,8.035790,-7.626448,-0.698857,5.876593,-2.668560,0.910123,3.839455,-4.226959,-3.439273,-9.959302,3.019570,7.973781,-4.144442,-7.374487,0.444587,-4.132154,8.780411,-9.161020,-7.551247,-2.991859,7.018374,-2.912054,-8.078219,0.213048,9.265322,9.566226,-3.109223,5.779906,1.581531,-3.493532,-3.934841,8.998519,1.425322,1.405924,-1.513927,-0.533096,-7.354359,-9.943241,-4.001656,9.597756,9.433467,-0.571743,-5.664759,8.319352,5.075810,-6.706433,-1.892699,-6.556774,-2.121625,8.140651,5.387828,-6.642998,-2.591124,-6.266200,-7.327836,-9.749353,0.980390,4.194532,-7.942743,6.986001,-6.639576,3.792171,-0.421754,-6.105783,-0.467607,0.281708,1.990116,8.333964,-9.113318,-2.070725,8.221488,-9.282354,9.309372,-1.645219,-2.856855,-1.522260,-9.452513,6.301130,2.627416,4.683077,0.628902,7.309932,-1.581228,-5.696777,3.111511,5.699011,6.414357,1.988156,1.450893,-8.215983,3.818296,-6.882877,1.643685,-9.479489,1.848447,-9.715728,-0.220208,7.862433,-6.045729,4.345763,7.558384,-0.600516,2.842745,8.059788,-2.633516,-7.378640,-9.060004,9.969680,0.614862,-3.806305,9.459348,1.060188,8.095932,-1.905240,4.009773,4.046658,-3.209574,2.272945,7.705944,-6.552357,2.789341,1.158736,1.381932,7.696012,7.832997,4.274738,-5.406039,-8.532141,4.276659,1.580802,2.910668,3.106089,-1.617953,0.378962,-3.377701,0.982283,-3.923500,4.776476,9.363952,-2.708780,6.755540,4.296660,2.785667,0.692640,-7.656100,1.187361,8.817495,4.393293,3.180616,7.303681,-2.414821,9.892007,9.761259,-6.879983,7.041338,0.577644,-8.088660,-6.844509,9.881998,4.552155,-1.834131,8.292995,3.640868,-0.778505,0.267155,-2.055733,-1.020665,-6.085166,2.589307,5.809091,-7.060056,7.951107,4.465816,-6.815021,3.855717,8.564220,-9.823663,3.109930,3.744435,-8.226816,8.232679,6.634946,6.854463,9.747070,-6.344153,4.137438,-1.771902,-2.188247,1.081254,-0.003001,-6.340524,-1.478356,-0.724898,-7.885193,0.868835,-3.797240,-3.179574,1.102039,7.072951,-7.816724,9.642572,-6.047522,-3.940249,1.843914,8.552601,-7.532008,6.431405,-9.408233,-3.218295,-5.110020,-1.159511,-8.638559,-4.708285,-7.690902,-6.284485,1.506032,-3.745473,5.848161,-5.292355,-4.071380,-8.531336,3.074794,-2.259996,3.805620,2.243088,-1.552883,-7.344092,-9.443309,-2.486324,1.042833,5.876110,-6.641381,-1.807720,-0.370759,7.388944,7.879434,0.182600,1.463477,-1.267364,-8.058297,-1.113573,3.354044,8.566069,5.303702,-6.821995,-4.477749,-4.876828,-4.714425,3.274080,7.404341,5.608774,-9.660047,-4.084257,-6.860284,3.803347,-3.843702,-8.913830,-1.731968,3.231571,5.606242,-8.144336,1.122404,7.321037,-7.342403,-4.850239,1.947940,-5.670133,-4.972112,7.811874,6.649563,9.272170,5.727124,-2.587438,3.071543,9.676498,6.196757,-9.626663,-1.029592,-1.833469,-9.162836,1.782011,5.860231,-8.880729,-8.270786,-9.879182,-4.176452,7.003660,9.639060,8.098089,9.964334,-9.734021,0.884328,2.836139,-1.545309,-9.265290,-8.700954,-3.892496,4.299870,7.125854,-1.549791,4.210977,5.814150,-5.567648,-6.537936,3.947550,4.843168,0.769397,-5.653170,-0.968871,-0.665090,-2.430611,-9.180376,-3.855355,2.460462,4.215835,-4.801326,-2.715347,4.930879,-7.488009,-9.668285,2.210721,7.940543,-3.109733,4.519245,-2.544891,6.393492,-1.873290,1.630399,1.567894,-9.845263,6.433467,-8.626818,-0.758430,-8.932460,0.028770,-9.920634,-4.222429,0.800080,-9.680497,-2.648998,3.478183,9.568704,9.128073,-3.383242,9.770815,-9.548299,0.278388,-2.885616,-9.436340,1.266093,8.860426,8.447572,9.205896,4.800685,3.397582,1.380450,0.402590,9.375875,6.700006,-5.284428,-8.873680,7.973027,2.633339,-8.269913,2.698596,9.192216,2.495484,-6.166848,-6.671353,-4.094065,3.217566,-2.218808,-9.776260,-0.207998,8.481351,-9.691952,1.362712,-1.053069,5.103738,-6.616434,-7.624306,-4.858857,-6.381760,-6.033796,-3.489186,1.905219,-9.761558,-3.709227,1.031620,4.568252,4.133129,-5.382597,2.666170,2.990111,4.792282,7.315021,-7.150478,-9.880421,6.214532,0.689848,9.117322,4.514002,-9.015153,1.879113,-7.934403,-3.177398,-8.275115,-3.513178,9.536856,6.689011,-6.230580,-8.822754,-8.597496,5.013021,-1.842245,6.008055,8.949041,4.027539,-4.213323,7.602844,7.131131,7.971727,0.699895,-2.642334,0.652735,9.344367,-0.633198,-0.853911,-0.490617,-3.722789,-9.904707,3.735713,0.193428,2.438624,0.454104,-9.230243,4.456362,-7.986318,-9.862388,3.838995,-9.597031,3.508461,8.973041,0.515214,0.475330,-2.143186,4.849181,-4.984265,-8.947630,3.148692,-4.034848,1.965626,3.515917,-4.581698,-4.123956,1.302563,0.168612,5.804596,9.134664,-0.223633,1.267032,-4.854364,-6.435324,2.039064,0.157204,-8.844434,-4.674427,7.987116,-8.973791,4.544354,9.167394,1.897021,5.298712,9.715532,-0.490188,-1.666421,-5.342162,-0.040354,7.018318,-7.031740,-1.603316,-2.561416,-5.067625,-1.000557,-9.502968,1.832502,3.563748,-4.086627,8.847893,3.000562,9.190958,8.168029,-2.146282,2.079504,6.115517,-2.207794,-6.430614,4.377930,-9.601390,2.994155,1.283860,0.186412,-4.245730,-6.822698,5.415200,1.502146,4.847279,4.194648,-4.145529,9.475397,-1.225315,-6.040111,-3.163575,9.014790,7.801307,9.321879,8.105551,6.852861,-9.405387,0.432655,8.282951,3.777837,-5.417341,8.393343,2.395649,-6.284117,-4.866108,-5.769093,-7.545871,-2.238261,9.814024,8.593250,-7.365947,-1.954666,-8.694111,-0.982495,-8.401286,-6.075389,-2.272388,2.810341,-9.834558,6.713131,-1.800503,5.096936,1.692710,5.975775,-3.711245,9.612955,9.611720,8.341472,-5.248365,-8.508619,6.681424,1.913683,-5.024415,0.173914,-8.031505,3.641639,7.138638,-3.593297,-3.688515,9.181836,-4.229309,0.323920,-3.346462,8.750555,1.224317,8.717036,-3.074706,-6.697365,5.333544,4.509094,3.249788,5.528982,0.702633,8.564553,1.920716,-9.782172,-2.480922,4.093320,9.915894,4.800364,-6.977710,1.176830,1.094162,3.286200,-4.634912,-4.667431,-0.954872,-1.992516,0.771093,8.172468,-1.860089,-2.378224,-3.453465,2.003872,-7.773666,-6.621193,4.897356,9.489761,1.325114,8.434818,4.096232,9.397177,1.418325,-5.787742,-0.172892,6.452306,1.927216,4.126123,-9.962536,3.472825,9.167826,7.940212,-4.122519,0.587230,-5.418207,9.468152,-2.897914,9.023363,-4.888543,2.511743,8.278468,9.923671,-1.776133,-0.054027,1.226447,-5.726410,4.565289,5.882606,-4.012466,-4.451793,7.360967,5.147565,-7.533587,-5.756779,-7.013675,3.876590,-8.781723,-4.541495,3.651069,5.041725,6.455302,9.811721,-0.337851,-2.579803,0.500862,3.322884,-1.325589,2.778683,4.999097,6.041878,5.764665,0.736873,4.750322,-6.305546,5.999494,3.240609,1.228659,3.976522,6.898150,2.728379,-0.372913,9.057740,7.984446,-5.964198,-1.810993,-1.903297,-8.875884,-7.315917,4.229899,3.986047,-1.103681,3.131320,7.025186,9.765679,-6.324702,-0.051063,3.010350,6.810067,-5.888858,6.494432,4.983106,-8.737499,-7.878473,2.098365,7.394601,-7.982862,6.785081,-2.222447,-4.980688,9.734718,-3.162527,-6.662691,-1.549894,-9.850504,2.954539,4.411521,8.884683,-5.994863,-0.797658,7.676667,-7.153541,-3.886921,-4.748698,2.517518,-9.102625,4.142443,-6.040626,1.686741,-6.678914,4.053097,9.143857,-8.144170,-3.428235,-9.833166,4.308297,-4.607865,5.356407,3.898094,8.478267,3.311052,-2.464371,-1.516570,-0.890583,6.755152,1.129763,-6.810782,3.900106,9.123685,3.431267,1.592997,-7.618253,1.811596,-5.502102,8.260035,9.273916,8.010487,0.658352,-7.793428,5.430257,-3.504509,-0.877283,-3.811111,-5.133828,9.441377,8.232985,-3.005799,-8.039725,-2.887454,-9.726631,1.816538,-3.262061,2.298725,-1.208455,0.422175,5.162080,3.895103,-8.919020,-4.000140,2.240795,-3.519968,-1.322793,-3.400655,-6.811438,0.462398,-2.076418,-1.224104,5.144965,2.606509,6.116608,-3.105644,-3.439812,-9.263373,0.316647,9.391985,-8.446284,7.869016,-1.216195,-4.272655,-2.248183,-8.814650,-4.640311,3.678174,-5.486308,8.300673,3.339694,8.253520,2.556358,-2.449613,-7.311882,-3.832054,-9.436998,9.754508,5.949841,2.953016,5.260623,0.680260,9.835123,4.197103,7.310133,2.955132,-3.142991,-3.793978,0.330112,-9.429509,6.896561,-2.584575,9.371047,-0.079433,9.939421,-1.453260,5.838843,-2.307363,4.394328,9.805254,4.886880,9.805402,0.811149,7.865020,6.951821,-6.505083,-5.487919,-2.848765,-9.415607,2.966783,-7.251598,-5.057483,3.044447,-7.200290,-7.746492,9.814887,7.724923,-6.401934,-1.751024,9.658581,6.608126,-1.884988,-0.709708,6.373399,-5.078927,6.004005,3.126388,-4.644993,-3.566736,1.941777,-7.486692,-1.325288,6.835414,-0.974422,6.248789,6.024883,6.992682,-3.082787,-5.883134,-3.404293,-6.478088,-4.408830,6.306584,-9.563184,9.787348,6.235869,-4.018159,3.637826,-7.832145,-5.400279,1.436786,-5.783942,0.604737,3.918510,3.100008,-7.171668,1.870443,0.226440,-1.468352,-7.603045,7.929829,4.142243,-2.691731,4.883164,8.351752,-4.402863,-2.272974,3.747008,5.147474,3.819059,2.317071,4.130993,-9.824570,4.894925,-5.742336,1.634329,7.664209,-6.657580,1.874411,-4.678252,6.271687,-6.534783,-8.934033,2.119810,-3.906151,-7.296273,8.057838,-4.758972,-2.709978,-9.187999,2.114595,-5.200583,-7.964354,-5.338412,-4.639196,-2.355488,3.709428,2.886903,9.604725,-3.361292,-0.771511,5.358435,-2.745604,9.748931,0.400081,3.806889,9.537981,-1.157867,-2.052884,-1.069963,6.365726,-5.834550,4.451985,-7.331987,6.457794,-7.807320,0.696110,4.390770,1.631815,-2.506319,-1.679149,5.770178,7.525958,3.919828,5.155273,7.837797,4.846849,3.267812,1.186391,7.530840,-7.459327,-3.151777,8.903494,2.932662,5.193500,0.669073,-9.033699,0.260865,-5.793187,6.456867,-4.739967,4.969066,8.220984,-1.570345,-0.201008,3.125641,0.059836,1.913180,6.598853,2.330706,-4.044464,-2.910492,-8.832809,1.474642,-9.621516,-3.227611,5.253032,-8.269639,-2.971442,8.297548,-7.797177,-7.524811,2.350432,-5.644297,-9.536258,5.277670,1.080014,3.757785,1.591209,-5.270110,-7.561797,9.156781,-7.677006,-2.233731,-0.095736,-5.171539,-0.005989,4.589713,-9.979918,-1.856286,3.372389,1.562705,9.260997,-2.314234,7.985125,-6.570901,8.913571,5.368342,-9.463232,9.696416,-4.169948,0.833548,-9.532793,-5.198726,1.790447,1.317435,-1.000120,2.310582,-1.213279,-3.538050,-4.605232,5.619696,-0.368584,-9.631642,-0.021638,-8.866831,1.525430,2.496126,-7.605228,-6.302729,-2.921525,-3.781452,-5.211042,-6.194769,-1.416529,3.367213,9.978159,-0.736287,1.153986,-7.426065,-3.712177,-6.894556,5.063259,4.824623,6.369638,1.834130,-7.935071,-0.284576,2.567230,4.364155,-3.016528,-0.002698,6.882335,7.800893,2.873644,-2.547590,-2.767704,4.769890,-9.550521,5.567810,-7.855991,9.802249,6.227984,-3.020293,-0.992301,-7.444360,-1.314119,-9.502034,4.340449,-3.215482,-7.380535,9.222639,-6.205205,-1.689116,5.561550,-3.643115,-9.222287,-6.827634,-7.896405,-2.482991,-7.614852,8.422987,5.162056,-3.315186,0.407452,-3.896497,7.731109,4.630869,-4.345516,-2.763753,5.748917,-5.350044,-0.783713,5.811400,0.888060,9.504644,-3.101135,-5.323059,6.315783,5.893745,4.530763,-7.146696,0.115915,-8.665657,2.075129,2.682114,-1.275456,-6.982488,0.116332,9.946629,9.571455,-4.760392,5.397410,5.051417,-8.251481,9.953246,-8.074872,-4.237985,8.724119,-0.553284,-2.388436,-0.489737,0.802657,7.577306,-9.903929,1.821546,-4.861990,-1.877055,-2.685670,-4.355266,-1.942218,-2.956288,0.053191,-1.501186,-1.992375,7.221917,-9.005597,9.826472,-5.354466,-5.631872,1.175993,-9.107596,-6.523881,2.867923,-7.381557,9.869514,8.586733,-0.217612,-8.818801,-1.342912,5.931396,7.547503,4.329238,6.840725,-2.846986,-0.430295,1.620928,3.745627,2.380536,-6.331669,-4.586423,-1.023316,1.602075,-5.233545,7.621543,-7.803773,-5.227532,4.642153,-8.231677,8.771065,-7.558199,-8.908335,-1.868546,7.710092,-9.909863,7.675320,7.632148,3.931338,-8.799520,7.846164,-1.060639,-9.694237,6.197696,-0.008011,-8.592106,-7.190794,8.332076,-9.923702,-2.998048,-2.966897,8.832337,8.779276,5.177827,-2.679936,-3.601498,-6.570923,0.642252,1.753539,-1.759901,6.986837,5.475340,5.993385,-0.601570,-6.467225,-9.546060,-3.474269,8.128087,-8.225679,-6.207836,-1.210859,-1.827441,7.460265,-3.088419,7.273057,-1.859021,5.834833,-3.941783,-2.417764,8.648987,-9.451364,6.032317,8.284195,-7.792784,-7.135380,-1.338944,-5.785739,5.967956,9.616343,-2.198671,-6.665538,6.907653,3.576079,-1.460307,-9.194463,-2.626669,3.827582,2.538309,-2.614877,1.637583,-2.066491,-2.197974,-2.609702,-4.328442,6.370319,-9.413312,1.443159,6.825585,-7.368691,7.261160,7.005916,4.059867,2.613086,-3.749994,-9.171995,-7.012089,3.734148,5.488523,-2.189698,8.410632,7.234730,2.563964,5.697917,3.755818,0.162958,9.315909,-7.356409,9.962200,4.325626,-8.763310,8.815933,9.237147,3.966411,6.943664,-2.232046,2.301636,-8.110322,8.490097,6.571382,3.112192,7.839304,-6.881319,2.976929,3.492829,5.579514,1.417093,8.591559,0.924016,0.360393,-8.680770,-7.409657,6.590434,0.799823,-5.597162,8.328381,2.355780,-0.715909,1.850176,9.303934,8.755082,-6.680341,-3.742120,6.850955,-7.215384,-3.495797,-2.979654,-0.549688,0.814906,-0.159407,-1.272999,-2.645022,-3.525335,7.773999,-1.117050,3.870013,6.506831,-3.366843,9.747812,-3.968599,2.463035,-7.707742,4.975107,8.023127,-8.541999,-2.620449,-2.514820,-4.156967,-6.523211,-3.166272,1.736911,-1.132739,7.188029,-0.569228,-9.840954,-1.196064,8.707527,9.869424,8.869897,1.471361,5.928057,-4.628099,-4.873548,-2.345902,8.708756,-0.255993,-0.172464,2.001464,9.616103,-5.120688,-4.620400,6.753694,-8.835629,-4.836707,-5.509361,6.533895,-6.106430,5.135905,5.639872,8.986948,-0.084985,0.688298,-9.287522,-7.242353,-8.638925,9.661697,0.778006,-7.261202,4.690192,5.513494,-4.767071,9.889876,-0.857367,-1.296788,9.484790,-4.933516,2.303242,-7.519765,8.457576,7.728765,-2.673137,-3.427870,-9.877196,4.818560,-5.799360,3.039282,9.203587,0.233802,8.537697,3.544635,7.541309,-3.962501,8.618631,-0.573650,1.754748,-9.385766,-8.119088,4.436822,5.924738,-5.587756,6.526898,5.517877,4.891211,-9.736376,-7.175265,1.498489,-4.803005,-9.095472,-2.789827,-0.915633,-5.910566,1.933195,4.822980,9.299785,0.785270,-2.725803,5.334447,-3.437896,-4.837509,6.084137,-3.580469,-5.650609,-9.936702,7.818055,3.075541,-6.187950,-4.247740,-2.729319,-1.575557,2.419588,-3.704696,-6.702934,0.880873,-7.990959,-8.804179,-3.238750,-8.396662,9.927902,2.767778,1.014366,-5.937863,-0.631331,-6.996406,-2.917705,9.124466,-2.141253,-7.321326,3.441860,9.788397,1.309311,-9.866134,0.200751,0.899352,1.601848,0.216957,8.891841,9.515983,-9.120043,3.340133,-2.299231,-3.467823,-2.681555,-7.922859,-5.801935,0.377846,2.448540,6.378937,-8.087019,4.141320,5.904662,-4.930733,-7.611927,0.457563,7.155923,5.803932,9.846105,8.763559,-4.438354,5.791774,2.607624,6.958477,-4.139029,5.256315,9.291126,8.564176,5.275958,9.583873,6.638273,8.030410,0.884166,-9.085017,-9.783453,-5.476311,0.325504,-8.551803,-8.772478,4.565605,-6.802713,4.120250,3.559564,4.159780,3.123182,-0.570629,2.172149,0.168160,5.381688,3.939138,8.077671,-5.825866,7.523181,-9.356904,-7.966429,7.459816,-3.403989,-0.716343,5.562268,5.714256,8.366691,0.533750,2.904904,1.201106,-1.052893,-4.436717,5.949647,0.381115,2.322495,-4.676513,1.977873,8.076960,5.328338,-2.797131,3.437945,4.740004,5.534947,9.396006,4.078628,0.849457,2.491965,-6.669548,0.140732,4.246194,5.222941,-4.025415,3.413674,-5.270202,-0.250863,9.732961,-2.769948,-1.376565,2.238046,-7.868236,-8.342133,7.531928,-0.785260,-2.813623,4.905575,-5.745982,-4.997514,5.997341,-9.646362,-6.001611,-0.904831,-7.966657,-1.929982,3.104416,-2.667830,-5.389811,0.114786,-6.502460,1.156944,4.184912,5.068764,4.991940,0.108791,5.104349,5.987775,-8.436915,-3.803182,-0.765933,6.364889,-5.814108,-1.547154,-1.400221,-4.708058,5.845586,-6.199050,-8.767480,-4.470464,8.481139,7.868959,-0.792478,-4.325407,-4.510819,0.214029,5.140349,-8.650067,6.306533,-1.901834,4.532568,-5.937981,6.508183,3.148169,-8.876977,8.317480,7.702511,7.892534,9.068464,-7.049402,-0.837909,6.826757,-1.120779,6.974153,-2.973412,-1.022560,7.901805,-5.392819,0.801352,-2.069574,0.746293,7.464008,-8.295636,-0.407569,-6.627129,-2.453064,4.684340,-6.665775,7.847168,7.853466,1.782911,5.118584,-3.851825,3.332441,-8.117178,-7.571349,-8.290944,-5.982613,-7.144258,-8.884377,-6.919824,3.166821,-1.435672,0.181072,6.920115,0.753079,-8.846338,4.613838,-4.116805,-5.240421,4.077877,1.777505,-2.307069,-8.759784,-9.455425,1.200118,6.384799,-1.270478,-6.152345,-6.240317,-5.778632,3.212472,-6.848898,-3.846457,8.273834,8.842375,9.436927,-9.841459,3.937918,-1.461080,-3.732999,-7.109815,-1.002813,6.370509,-3.320750,-8.715969,-6.367845,-7.289455,4.576233,5.608750,7.680638,9.505283,5.087257,9.290136,-5.810089,2.507314,6.058377,6.440072,-2.426866,4.845571,-5.555999,-7.096077,8.089362,4.008001,7.499611,5.648014,-1.535041,5.148614,5.364300,-2.577475,-5.925703,-5.595910,7.451908,0.973027,-0.945314,-7.253779,-4.190811,5.951118,4.266785,-2.550121,-6.141921,-4.044615,-9.618066,-3.489154,-8.778444,-3.905322,-1.098192,-7.781315,-8.066315,-6.017649,-6.086742,1.075980,3.425617,-3.280367,6.348442,6.029627,8.658359,-8.879822,0.975898,0.706886,1.312249,-2.884007,-2.436640,8.086502,-2.485922,5.873436,7.131458,3.492996,-2.728345,6.133238,9.528189,5.986215,-6.571554,-4.462812,-5.793955,9.324489,9.675545,-1.802336,8.105641,-0.587181,0.885570,-3.705100,-2.892267,5.979469,-1.167194,0.844139,9.715622,-7.921018,-8.074748,4.618959,-1.227209,0.225405,-1.477678,4.767127,7.841360,3.227366,5.075486,9.424185,4.523631,-6.178560,-0.102347,5.304235,-1.426407,2.960422,3.395467,-3.768589,-7.421984,7.902391,9.332595,-6.459306,7.767659,3.069713,5.496304,-3.537662,1.226321,-1.703039,-6.881843,4.551751,3.612451,-6.955665,6.439297,-5.199890,-5.346755,-4.016614,-1.339107,-3.118817,-2.115728,1.009167,1.332517,-3.972706,-0.574633,-1.507847,7.860802,-4.083881,-6.301411,4.655071,8.327347,8.336070,9.347397,3.170870,-2.251220,2.642357,2.318102,3.963167,8.918546,9.290849,-1.670174,-7.555282,3.706132,3.688826,3.116976,7.569779,-8.442605,-9.383165,-4.030131,-9.177318,-7.023791,2.522416,-3.123533,-5.456626,-3.837445,4.433989,8.050027,-4.076270,-9.780598,-3.194254,-5.815476,-2.242311,4.691988,9.452018,-6.471888,-6.237056,5.869935,-7.812061,-0.183498,4.266433,-9.292927,-4.087587,6.991458,-5.862302,-0.026907,9.151767,-6.167210,4.359246,0.396664,0.915229,-1.670945,-3.994069,1.679464,2.895036,0.592514,3.878327,-8.694941,0.354015,-0.750268,6.244250,-0.184906,-9.662858,8.753953,-5.469522,-0.972700,-3.447229,-2.020475,-7.072667,-4.682145,7.103313,3.862677,0.811247,-6.960429,4.304614,0.730462,1.149110,5.501141,-9.195473,-2.564603,6.309272,6.503371,3.483383,-7.792143,4.812475,-1.497406,-8.640426,9.440086,1.853309,-1.853506,5.128672,4.632017,-1.493004,-6.182907,0.679605,8.637555,3.295176,6.277968,-3.598109,-8.546923,-5.856937,7.933869,-2.709882,-1.192046,-6.056857,-9.710328,-9.545396,7.216592,4.760097,-1.625212,-7.353717,4.329223,-6.954558,-4.972362,2.641431,-0.738572,3.217625,-3.547626,1.362945,2.951315,-5.184173,0.046878,-6.196038,1.893513,-6.081325,-5.411935,6.513836,-7.952092,-7.552685,7.823259,5.254537,2.332052,8.005496,5.611450,2.476735,-2.607038,-7.229108,-3.794758,-7.656771,-5.543289,0.505549,1.823398,5.959163,-9.383594,9.969612,8.173473,-6.081284,7.080645,-2.098761,-4.005412,-6.631093,3.739258,-7.128935,1.272790,0.555937,4.346713,-1.948164,-0.443773,-0.157332,-7.369122,-0.002430,-5.129233,-4.470717,-1.910547,-8.198483,-0.062071,9.588694,-4.276647,-8.632187,8.134032,6.783694,-7.534404,6.072380,9.863978,-9.206299,5.597420,7.885795,9.715264,-9.785068,6.643881,-3.680250,5.764784,8.022793,8.868870,5.885575,-6.817550,6.906063,-4.987339,9.488864,-5.443590,2.516057,-7.718725,2.349926,7.589772,9.429861,6.885717,-2.005199,8.961924,-4.983442,3.150973,9.467199,-2.978776,9.652474,-9.000565,4.871004,-7.340102,-5.845965,6.195978,-4.338351,1.559871,3.602781,8.684111,1.221147,-7.872206,5.251086,9.105060,4.841174,7.550169,8.764570,6.079231,-1.346002,4.968225,-0.406737,-2.760702,6.992160,-5.086585,-0.983635,0.888668,-2.574068,9.273887,3.045341,3.583628,5.227906,8.097766,-5.183856,2.714976,-4.209190,6.426877,8.917028,3.369965,-0.108587,-8.822102,3.711828,-9.163132,7.503011,4.037544,6.486243,2.935305,4.326723,1.027038,3.215010,-3.800409,7.758285,-8.860560,-5.577570,-0.878500,6.348971,4.312938,-2.821095,-5.282565,-9.229146,-1.659749,-1.684381,-2.659271,2.832934,9.481361,-7.126289,-5.707418,-4.450005,-7.220647,4.377719,3.733586,5.427101,1.430609,-9.865556,0.621654,-2.560460,-8.116755,2.340741,-0.133069,-0.366130,1.325714,-8.762556,6.045216,-6.718035,6.643164,-8.460641,-9.161766,9.721433,5.473752,-3.113916,-4.548552,-9.308463,6.891893,1.269213,-4.835243,-4.585725,-0.220390,-2.919410,9.703383,-3.172481,-5.931349,8.226228,-1.126441,-1.366174,-3.683248,7.002374,3.669501,-8.628125,7.832453,7.857868,0.541371,-8.513074,-7.822327,0.458865,0.225093,-5.470130,-1.832099,1.454697,-7.910652,-6.727721,-6.807095,-9.404250,-2.432226,-1.434098,-2.154547,9.554107,6.749751,-5.935420,-3.150577,8.979475,2.253967,5.530821,5.226510,-0.081667,0.115880,4.434037,-5.508923,1.206829,-8.479965,3.423444,2.239547,-6.634474,-0.448347,-5.482362,7.661146,-6.090867,4.585963,-5.013329,-1.386770,3.512659,-7.451432,3.923221,-3.014869,3.918776,1.073377,2.763869,8.132351,3.135321,-7.421639,7.544372,-7.842689,-4.174805,6.198399,-9.132865,-1.238901,5.817976,-9.082896,7.283771,-2.433433,2.219638,5.534604,-6.356625,2.460903,-0.905991,-6.394173,2.861683,-1.469499,-6.286087,-7.043399,3.223012,-7.834330,7.299964,-2.386835,3.014574,2.754241,-7.954623,-0.340932,-8.429011,-9.528826,9.754057,-1.594011,8.461341,4.777145,-6.188731,0.202366,-0.750152,9.688307,-7.059040,-8.124709,-6.787788,4.460301,3.958615,8.556868], dtype = "float32")#candidate|13757|(2400,)|const|float32
call_13754 = relay.TupleGetItem(func_11601_call(relay.reshape(const_13755.astype('float64'), [390,]), relay.reshape(const_13756.astype('uint32'), [63,]), relay.reshape(const_13757.astype('float32'), [300, 8]), ), 4)
call_13758 = relay.TupleGetItem(func_11605_call(relay.reshape(const_13755.astype('float64'), [390,]), relay.reshape(const_13756.astype('uint32'), [63,]), relay.reshape(const_13757.astype('float32'), [300, 8]), ), 4)
output = relay.Tuple([call_13743,call_13754,const_13755,const_13756,const_13757,])
output2 = relay.Tuple([call_13744,call_13758,const_13755,const_13756,const_13757,])
func_13771 = relay.Function([], output)
mod['func_13771'] = func_13771
mod = relay.transform.InferType()(mod)
mutated_mod['func_13771'] = func_13771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13771_call = mutated_mod.get_global_var('func_13771')
call_13772 = func_13771_call()
output = call_13772
func_13773 = relay.Function([], output)
mutated_mod['func_13773'] = func_13773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12779_call = mod.get_global_var('func_12779')
func_12781_call = mutated_mod.get_global_var('func_12781')
call_13781 = func_12779_call()
call_13782 = func_12779_call()
output = relay.Tuple([call_13781,])
output2 = relay.Tuple([call_13782,])
func_13789 = relay.Function([], output)
mod['func_13789'] = func_13789
mod = relay.transform.InferType()(mod)
mutated_mod['func_13789'] = func_13789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13789_call = mutated_mod.get_global_var('func_13789')
call_13790 = func_13789_call()
output = call_13790
func_13791 = relay.Function([], output)
mutated_mod['func_13791'] = func_13791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10945_call = mod.get_global_var('func_10945')
func_10946_call = mutated_mod.get_global_var('func_10946')
call_13872 = func_10945_call()
call_13873 = func_10945_call()
output = call_13872
output2 = call_13873
func_13918 = relay.Function([], output)
mod['func_13918'] = func_13918
mod = relay.transform.InferType()(mod)
output = func_13918()
func_13919 = relay.Function([], output)
mutated_mod['func_13919'] = func_13919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12287_call = mod.get_global_var('func_12287')
func_12289_call = mutated_mod.get_global_var('func_12289')
call_13959 = relay.TupleGetItem(func_12287_call(), 0)
call_13960 = relay.TupleGetItem(func_12289_call(), 0)
output = call_13959
output2 = call_13960
func_13961 = relay.Function([], output)
mod['func_13961'] = func_13961
mod = relay.transform.InferType()(mod)
output = func_13961()
func_13962 = relay.Function([], output)
mutated_mod['func_13962'] = func_13962
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14088 = relay.var("var_14088", dtype = "uint64", shape = (9, 13, 10))#candidate|14088|(9, 13, 10)|var|uint64
var_14089 = relay.var("var_14089", dtype = "uint64", shape = (9, 13, 10))#candidate|14089|(9, 13, 10)|var|uint64
bop_14090 = relay.bitwise_and(var_14088.astype('uint64'), relay.reshape(var_14089.astype('uint64'), relay.shape_of(var_14088))) # shape=(9, 13, 10)
func_13771_call = mod.get_global_var('func_13771')
func_13773_call = mutated_mod.get_global_var('func_13773')
call_14096 = relay.TupleGetItem(func_13771_call(), 3)
call_14097 = relay.TupleGetItem(func_13773_call(), 3)
output = relay.Tuple([bop_14090,call_14096,])
output2 = relay.Tuple([bop_14090,call_14097,])
func_14114 = relay.Function([var_14088,var_14089,], output)
mod['func_14114'] = func_14114
mod = relay.transform.InferType()(mod)
var_14115 = relay.var("var_14115", dtype = "uint64", shape = (9, 13, 10))#candidate|14115|(9, 13, 10)|var|uint64
var_14116 = relay.var("var_14116", dtype = "uint64", shape = (9, 13, 10))#candidate|14116|(9, 13, 10)|var|uint64
output = func_14114(var_14115,var_14116,)
func_14117 = relay.Function([var_14115,var_14116,], output)
mutated_mod['func_14117'] = func_14117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_14165 = func_11738_call()
call_14166 = func_11738_call()
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
var_14171 = relay.var("var_14171", dtype = "int8", shape = ())#candidate|14171|()|var|int8
call_14170 = func_592_call(relay.reshape(var_14171.astype('int8'), []))
call_14172 = func_592_call(relay.reshape(var_14171.astype('int8'), []))
output = relay.Tuple([call_14165,call_14170,var_14171,])
output2 = relay.Tuple([call_14166,call_14172,var_14171,])
func_14173 = relay.Function([var_14171,], output)
mod['func_14173'] = func_14173
mod = relay.transform.InferType()(mod)
var_14174 = relay.var("var_14174", dtype = "int8", shape = ())#candidate|14174|()|var|int8
output = func_14173(var_14174)
func_14175 = relay.Function([var_14174], output)
mutated_mod['func_14175'] = func_14175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13789_call = mod.get_global_var('func_13789')
func_13791_call = mutated_mod.get_global_var('func_13791')
call_14180 = relay.TupleGetItem(func_13789_call(), 0)
call_14181 = relay.TupleGetItem(func_13791_call(), 0)
func_12123_call = mod.get_global_var('func_12123')
func_12127_call = mutated_mod.get_global_var('func_12127')
const_14208 = relay.const(-6.242294, dtype = "float64")#candidate|14208|()|const|float64
const_14209 = relay.const([False,True,True,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True], dtype = "bool")#candidate|14209|(495,)|const|bool
call_14207 = relay.TupleGetItem(func_12123_call(relay.reshape(const_14208.astype('float64'), []), relay.reshape(const_14209.astype('bool'), [495,]), ), 3)
call_14210 = relay.TupleGetItem(func_12127_call(relay.reshape(const_14208.astype('float64'), []), relay.reshape(const_14209.astype('bool'), [495,]), ), 3)
func_6813_call = mod.get_global_var('func_6813')
func_6816_call = mutated_mod.get_global_var('func_6816')
var_14220 = relay.var("var_14220", dtype = "float64", shape = (250,))#candidate|14220|(250,)|var|float64
var_14221 = relay.var("var_14221", dtype = "int8", shape = (550, 1))#candidate|14221|(550, 1)|var|int8
call_14219 = relay.TupleGetItem(func_6813_call(relay.reshape(var_14220.astype('float64'), [5, 5, 10]), relay.reshape(var_14221.astype('int8'), [550,]), ), 2)
call_14222 = relay.TupleGetItem(func_6816_call(relay.reshape(var_14220.astype('float64'), [5, 5, 10]), relay.reshape(var_14221.astype('int8'), [550,]), ), 2)
output = relay.Tuple([call_14180,call_14207,const_14208,const_14209,call_14219,var_14220,var_14221,])
output2 = relay.Tuple([call_14181,call_14210,const_14208,const_14209,call_14222,var_14220,var_14221,])
func_14235 = relay.Function([var_14220,var_14221,], output)
mod['func_14235'] = func_14235
mod = relay.transform.InferType()(mod)
var_14236 = relay.var("var_14236", dtype = "float64", shape = (250,))#candidate|14236|(250,)|var|float64
var_14237 = relay.var("var_14237", dtype = "int8", shape = (550, 1))#candidate|14237|(550, 1)|var|int8
output = func_14235(var_14236,var_14237,)
func_14238 = relay.Function([var_14236,var_14237,], output)
mutated_mod['func_14238'] = func_14238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12870_call = mod.get_global_var('func_12870')
func_12871_call = mutated_mod.get_global_var('func_12871')
call_14302 = func_12870_call()
call_14303 = func_12870_call()
output = call_14302
output2 = call_14303
func_14320 = relay.Function([], output)
mod['func_14320'] = func_14320
mod = relay.transform.InferType()(mod)
mutated_mod['func_14320'] = func_14320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14320_call = mutated_mod.get_global_var('func_14320')
call_14321 = func_14320_call()
output = call_14321
func_14322 = relay.Function([], output)
mutated_mod['func_14322'] = func_14322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14443 = relay.var("var_14443", dtype = "int8", shape = (9, 5, 6))#candidate|14443|(9, 5, 6)|var|int8
var_14444 = relay.var("var_14444", dtype = "int8", shape = (9, 5, 6))#candidate|14444|(9, 5, 6)|var|int8
bop_14445 = relay.not_equal(var_14443.astype('bool'), relay.reshape(var_14444.astype('bool'), relay.shape_of(var_14443))) # shape=(9, 5, 6)
func_3701_call = mod.get_global_var('func_3701')
func_3706_call = mutated_mod.get_global_var('func_3706')
const_14450 = relay.const([-7.160493,-8.514596,8.053056,8.665619,-7.231996,2.931379,-0.322264,-8.229606,7.255614,-0.275734,8.196996,-8.113553,-9.837963,1.522709,6.373342,0.865527,6.417092,-4.500157,-1.149213,-8.120900,-1.692737,8.330956,7.848984,1.636442,4.958837,-1.282439,1.265899,8.383749,0.103970,7.870754,-5.556270,-0.802034,1.355766,-9.036856,6.240092,-3.111302,2.932327,-4.896517,3.115552,6.999867,-3.155392,4.712049,-1.831019,5.501545,-1.305134,-4.137770,1.390189,-0.639877,-7.528804,1.071573,5.474921,2.331236,9.356644,-2.710689,-7.477186,1.329490,3.843900,-2.495623,7.535080,8.005459,1.115157,-9.368968,-3.711187,2.832566,-9.229894,-3.454218,-1.805543,-7.818773,-3.479389,-6.794970,-2.355028,5.238610,-9.989285,5.349878,0.138677,2.924195,-5.195997,-6.674769,2.053581,8.772866,-3.828256,7.001942,-0.683462,-4.458609,-6.517513,4.436913,-0.613499,-7.413820,-9.234792,6.954463,-4.466840,-9.000605,-4.612304,-7.733686,-6.892856,2.700941,7.552245,5.301257,-7.213084,-2.401537,-5.677339,1.027171,-3.544864,-6.488942,3.392730,0.746330,-2.759472,8.018327,-4.183020,-8.262543,6.954733,1.321675,5.639236,-6.274053,-2.833068,-6.646257,-4.903153,0.371038,-4.223006,-4.677237,1.329335,8.205761,8.359508,6.406162,-6.251861,6.317614,1.833916,1.679714,9.702702,7.441034,-0.071371,7.199392,9.995882,-2.607936,-8.386900,-7.323315,-3.906921,6.210064,-2.930066,7.203641,7.060586,-8.636602,5.129815,3.692307,-1.220091,-7.649075,-1.406282,5.015806,-3.239198,2.278289,-1.934798,1.802651,-0.408558,7.603958,6.525845,2.594861,2.608978,9.954008,0.197518,2.876902,9.752091,3.542550,4.425382,-1.031787,-5.810123,-1.796416,9.073683,3.223085,3.229062,-4.810171,0.610004,8.727234,1.859409,5.857290,3.209032,-5.086377,-8.798525,-2.045706,3.981909,2.525777,2.630657,-6.277771,1.387273,-2.523467,-1.691119,2.521904,-0.751908,-8.084157,-3.271663,1.405193,1.413099,-1.193186,8.095902,6.213825,8.308869,-4.722838,5.694846,5.391097,-7.516211,8.674790,-9.917206,-0.569965,3.757259,1.764020,-0.359724,4.130772,-4.266763,8.839262,-3.428208,-0.841676,5.154333,-8.713992,-6.007624,-4.887624,2.648853,3.500304,-0.670927,2.060938,5.652902,5.295413,1.395302,8.050995,3.544657,5.875334,0.152763,3.596147,-0.819190,1.784408,-0.326883,7.622888,6.145601,1.825227,-0.766835,3.725659,9.454025,1.584470,3.821744,4.158627,4.447291,3.142316,-8.535170,9.564452,-2.765416,7.034533,-4.806345,9.443419,-1.708554,-6.693989,1.967617,-6.044721,-2.983869,5.905110,-6.446134,-8.535740,7.305328,-4.692847,9.081336,-2.273380,0.605742,-5.155172,-2.220893,8.008935,-1.991365,2.538740,-2.329973,2.890618,7.877188,-7.039908,9.233542,6.636371,-4.459919,-1.004100,6.411786,-2.350214,1.234601,7.528793,-2.620212,-8.393571,-0.284915,-8.684535,9.131829,2.831486,-2.906437,-4.110181,7.295522,-2.589346,2.152955,9.269584,1.322058,8.674044,-6.054053,-1.667946,-6.306116,9.464829,-4.965906,8.976400,0.907389,-5.815572,-2.012553,2.088715,-9.946582,-6.390232,5.453765,-4.240800,9.076523,0.760152,-7.142424,-6.307750,-1.661474,1.689103,0.961004,-9.518011,-2.045765,-2.909577,7.588896,-2.763570,8.590434,1.448463,-3.531129,6.557467,-4.786920,9.034314,-3.066696,5.756490,8.136856,3.969466,2.750971,-0.762117,-7.772193,-8.317995,-9.595311,7.932760,3.731019,-9.854498,-6.835362,3.027760,-7.205465,-0.313419,-7.491338,9.553624,-2.753416,-6.036073,-6.700631,7.996682,4.483733,-5.720176,-9.346823,0.817484,0.467177,9.582207,3.663696,-2.337481,6.492330,-8.638846,-0.995642,-8.590489,-5.610712,-4.995914,5.460168,4.410183,5.616393,-0.179697,2.654043,-8.310430,-6.879585,4.256473,-7.572061,6.352987,-0.270226,-8.333506,-7.367551,7.107039,9.010831,1.165402,-2.129784,-0.424578,1.992613,1.628207,-0.237389,6.384501,-4.638040,5.281086,-8.594926,-2.731262,-1.259014,8.381546,7.473979,-6.499363,-6.874086,7.878867], dtype = "float64")#candidate|14450|(390,)|const|float64
var_14451 = relay.var("var_14451", dtype = "uint32", shape = (63,))#candidate|14451|(63,)|var|uint32
const_14452 = relay.const([4.310468,-6.159403,2.009746,6.236708,-3.940804,-9.876146,-2.507909,5.536369,-8.805189,-0.692890,-3.925783,7.233002,2.570331,-7.120863,-1.260180,1.039937,-3.601325,6.800224,5.725828,5.253394,-6.958818,-7.500755,1.441888,3.304543,0.930946,-8.474699,3.490844,1.552908,5.158313,0.546878,3.506687,-8.374402,-8.368212,7.970769,-7.701315,-6.974930,-4.818657,8.723482,-6.471548,6.897932,-7.688350,7.575803,-9.507715,9.540766,-6.421337,2.627927,9.380966,0.679339,4.753182,1.396485,4.843972,-8.788338,-0.434592,8.821265,-6.775314,7.812941,-4.621655,6.226660,6.629744,6.528511,0.689541,7.975418,-6.495659,5.209889,3.508463,0.915334,-2.115470,-5.056329,0.763136,5.753725,-7.575904,-0.331536,-4.133443,5.773390,-5.076808,2.272243,9.058499,-9.209641,-1.305148,3.020462,-4.056006,-0.182568,5.680729,-2.967416,0.425204,-6.059411,-9.960643,-3.115024,-5.054560,-7.515686,-9.578749,9.228200,-4.829231,5.133054,1.780971,-5.080426,3.281696,-6.290506,5.441039,3.178871,-9.845472,-5.885387,7.593838,2.302321,3.680897,-3.424130,-3.500388,8.735924,-2.721038,6.191863,-9.049612,5.646685,-2.266272,-4.156323,-2.081626,-5.697916,4.744532,8.894817,-0.360622,6.275305,-8.709407,9.146851,9.890249,0.259433,-6.014521,6.050514,-4.791615,-0.520973,-5.396831,-3.328371,2.736814,2.220666,-7.916233,8.048264,-2.982470,-5.853964,-7.329452,9.462795,-8.326059,6.165360,8.510269,3.165520,-9.181818,-2.401585,-5.710523,1.613147,-3.092192,9.448465,-8.990934,9.281591,6.828751,4.647791,0.071413,8.956622,-5.047004,-6.020800,5.578982,2.924700,-3.036839,-2.573351,2.715031,-3.664132,-3.327598,-2.673704,-9.085600,1.573983,6.776951,2.211646,0.791807,-6.524286,-5.287139,9.696819,9.113186,8.458125,8.147899,-1.410356,4.082083,-3.505204,-8.118570,-6.160221,-6.923086,-4.490252,8.068307,-9.825060,-1.549666,-2.220204,-3.657669,-7.316846,-8.949351,2.952418,6.241152,-3.843574,-6.514964,4.482776,2.268281,9.609526,0.161549,2.236425,8.453757,-2.788885,4.066600,-1.998726,-5.916143,1.851656,-6.272202,-2.144852,-9.856146,0.432289,7.403157,-5.652449,-1.569246,-0.735291,2.427212,-5.466767,-9.767070,2.421400,0.819170,4.138803,-0.437845,5.169570,0.774796,8.564955,-1.183094,-5.904765,7.513959,7.167205,-9.223982,7.377091,8.450638,-9.285768,-8.168712,9.892580,-6.122942,-0.229957,2.899473,2.177054,5.936378,1.776735,4.057719,-3.351872,-7.271454,7.979236,7.797304,-7.323606,-4.291523,-6.688493,-0.638531,4.895914,-2.835239,-3.204953,5.218914,-4.188470,-7.105105,-0.071708,1.327541,-5.924745,-4.278440,-0.439925,-9.271665,8.029189,-1.194041,-6.693538,9.335640,8.752740,0.577193,-6.152698,9.828839,8.753895,-0.755977,-5.260341,-4.617717,4.690343,-3.519571,3.000780,-7.768686,5.851060,-7.681276,-0.200115,4.937487,-9.730152,0.481191,0.371423,1.961596,-0.079845,9.614285,-0.224082,9.130143,-3.924908,6.297217,-1.067151,-9.750683,-3.935343,4.484909,7.761098,-0.463840,1.545656,-8.726943,9.262984,-2.489922,1.387052,-3.299730,8.823629,5.361318,9.892759,8.831397,-2.011140,0.569908,2.694342,4.089440,-9.931200,-6.682842,6.808328,-8.636502,-1.384324,-9.693321,-9.102957,4.463955,-6.162851,-3.150510,-3.601912,-1.359992,1.351431,0.612008,-2.957912,0.235150,9.112279,4.618092,-2.793697,5.510447,-3.696605,-1.594670,-2.483657,-2.789070,-0.077489,-8.998727,1.362190,-0.954388,-3.095039,7.776278,-2.110647,7.545491,-3.688723,4.643316,5.783776,7.000301,-8.320491,-6.419909,-5.020193,-6.061835,5.327301,0.438679,2.898225,-2.898745,8.413180,-9.232850,-9.228047,1.810917,-5.005865,-2.828280,6.146783,7.174319,4.001701,-4.856681,6.621486,9.713208,5.237597,4.057836,-5.848960,5.825828,9.860732,1.547237,9.620093,-2.656033,6.010823,6.579897,-8.510794,5.700830,1.698122,8.405440,-7.859129,6.127456,9.406905,-3.431363,-1.589604,-4.078471,4.624028,-8.588866,-3.736144,9.340148,7.878234,5.144718,8.815560,9.892630,-6.945397,2.809668,1.159775,6.225628,4.136625,-8.783589,8.916429,2.393946,0.646406,5.082516,-9.674007,6.187993,-8.493882,-2.752702,2.146776,-8.482342,-5.532595,-1.567592,-5.011383,8.689635,0.451833,-3.598288,-2.066038,-1.660216,4.087778,5.358331,-0.133752,9.821426,6.746772,-7.761182,4.834049,7.020202,2.236937,-1.702249,7.140753,8.700887,0.116720,6.129186,-6.675121,2.556831,4.296201,3.555220,-0.541791,-5.237570,-3.199118,-4.887475,1.206390,-6.247751,-8.733909,5.231957,-0.155455,-8.075992,-2.955013,7.407315,7.290009,-3.513409,8.530779,-0.044914,-1.960519,-3.991558,-7.895764,-9.282593,-1.708740,-7.041468,4.870290,-0.781680,-4.438212,-5.774840,-3.273909,1.962047,-7.023705,-5.858993,-4.609830,5.762387,-5.490436,2.174627,1.204674,-5.629235,-7.089934,-9.875782,-4.079107,1.688144,6.339091,0.025936,7.201106,-0.290635,-1.912226,-0.341151,2.784358,7.924802,8.415057,-4.660565,2.933496,-9.244710,8.010143,8.864196,0.034498,9.492852,-2.157147,-7.199425,6.892195,-2.739635,0.990556,-3.136915,-7.184370,-1.095958,9.538461,-7.387237,-6.188510,-5.380995,4.513231,9.995045,7.182880,-8.396893,-1.743226,7.065341,6.622779,7.696176,-2.138507,2.390420,-5.882776,-7.622820,7.550157,-5.822117,6.368353,7.775253,-4.138851,5.003657,9.581093,-2.341933,-7.505229,-2.814880,5.478295,7.081592,7.806233,-9.681300,-3.727728,4.309344,-0.678749,6.425573,6.994850,-7.718304,-1.563895,6.633471,8.342216,8.814956,8.752496,2.111558,4.219051,8.314588,-4.545409,-2.263821,-3.433156,-1.164759,5.394224,7.661247,-4.873670,2.415692,7.368630,7.405254,-6.906329,9.947950,-0.983604,-6.554798,5.673555,-8.166191,3.351202,-1.992484,7.571595,-4.055023,3.949249,1.244989,-9.439719,-2.424543,7.743914,-1.531153,-7.600446,6.594615,0.723332,-2.335146,3.296364,-0.312098,-9.359015,2.163250,4.888959,-8.349861,4.930169,-6.910934,-5.219956,7.662181,-0.573243,3.495519,5.251011,1.608447,-5.773828,3.100133,2.435386,7.727788,7.261604,5.942072,-2.793266,7.980330,9.785461,9.441117,-7.502392,8.382081,0.999679,8.829900,1.767816,1.595918,-1.996084,-1.675210,-5.330221,7.752109,-0.620122,-4.605006,9.915002,-9.178201,7.896170,-0.589867,-2.215782,4.391655,5.140649,8.746054,2.347922,-7.729893,7.147912,3.433970,-8.445427,8.652638,1.618743,-2.242785,0.877788,0.520273,-2.740476,-0.748986,3.778856,-5.014299,-2.128839,-4.149086,-7.065076,-5.284414,9.183182,2.993296,-0.337302,-7.281620,-5.761649,-7.428278,3.752780,6.071588,-4.864885,-8.986794,6.857639,-8.839974,-3.549900,6.672680,1.783518,4.246459,-8.493855,2.734007,0.466013,-3.460443,-3.571167,-5.403859,1.380283,1.180083,4.345417,8.649652,9.510695,3.709813,-5.283219,-0.999370,-7.715874,-7.932118,0.728702,3.150483,7.650525,-1.513600,9.025094,5.943635,-5.687070,-5.561060,5.214932,-5.159145,6.414281,-2.185173,4.317409,1.792006,-2.012020,-6.554811,2.286276,6.330297,7.226629,-0.587454,-8.494111,3.092406,0.410047,-4.468219,-7.175857,5.136334,-6.779429,7.705604,-0.263997,3.569880,3.996471,-8.166651,-1.401316,0.541384,-9.299678,-6.557244,-0.536173,1.388725,6.438407,-4.024121,4.495143,1.667423,4.505309,4.399750,3.766283,6.459566,-5.820386,-7.695966,4.864405,-5.277641,0.246671,-4.649661,5.919238,1.199322,4.567255,-3.708210,1.007815,7.457458,-1.472521,7.291562,5.229390,-6.296041,-9.885759,-7.643022,0.104669,2.750069,2.594003,-3.045147,-0.953654,3.958895,1.456242,-9.347231,0.020882,1.473498,-5.977841,-4.350638,5.568165,8.264033,4.778645,3.736599,-2.970516,1.359141,-0.345587,-9.966293,-9.694931,7.191463,7.326853,-6.076810,1.619558,3.561137,-8.653687,1.682385,-9.411750,-4.031360,8.252033,-7.018116,-0.380535,9.621067,9.488775,7.607695,-4.138808,9.952908,-5.849582,-4.428757,-2.500444,3.458446,7.770861,-9.141996,8.786757,5.232313,3.236959,6.646771,-0.364921,-3.498282,-1.749859,6.536533,-2.849962,5.688924,-0.785951,-8.722394,5.763846,-0.788621,9.065936,-9.154644,5.248058,8.873324,-4.540070,-3.954166,8.029979,-8.763487,5.857892,-3.832365,9.634160,-8.375781,-9.250991,-9.096774,7.260928,-8.763728,3.686202,7.729815,8.375296,3.200758,5.766768,-7.718328,5.246862,3.784339,-8.283653,-4.940199,8.906468,5.862122,-7.373238,6.522372,-3.039815,-2.933147,-1.040981,-9.588237,-3.550253,6.876241,-4.486732,-9.185992,2.829915,-4.149961,-0.613138,2.193619,9.066851,3.436377,-4.380075,2.081756,-8.259539,-5.558034,-9.439751,-8.641038,3.517184,-5.788447,3.917903,1.192249,-3.372918,-8.949470,-3.601734,-8.017998,9.004555,6.289830,-4.872013,-8.196259,-1.386499,-9.434189,-2.894371,8.731950,-0.782400,9.079000,2.473630,-7.641489,-4.421433,-0.087596,-0.404425,-8.025547,-2.525012,4.024618,3.246983,7.476765,7.549702,-1.311699,2.344041,0.607529,9.223034,0.910194,3.014765,5.465456,8.469152,-3.833181,-2.687225,5.432934,2.756218,-2.588964,-2.359773,-0.441144,1.255529,1.705462,1.049478,-6.090087,9.171108,7.081603,-7.774988,-4.425309,-3.129549,4.582480,-1.323466,1.799289,-1.576307,-3.919532,9.902530,-5.032607,6.284445,3.230522,-6.703795,1.520451,-8.903399,-1.981656,7.499087,-2.302851,4.150810,4.127032,-1.299584,8.898496,-2.877425,2.437826,7.042981,-8.450077,-9.207352,6.941373,6.675329,-1.756642,4.523029,-8.198951,-7.881643,-9.487613,5.799245,2.814439,-6.378732,-5.431973,-2.455856,-9.254948,7.807992,-9.390787,9.215449,-3.483306,-0.044072,-6.950557,9.834017,6.421840,3.480922,4.722514,1.021235,-6.644545,-9.593904,-1.097862,-9.970422,-1.418725,3.111167,8.003676,-0.595614,7.667123,8.980808,-9.619097,0.915232,-8.665113,1.358303,3.636116,-3.506743,-3.640873,-6.170720,9.018096,2.309676,-2.411604,-5.736231,6.780950,4.058068,2.244300,-5.326703,6.462913,9.976023,-0.692355,4.323524,3.819187,9.436661,-6.315697,-6.573510,4.701139,3.831234,-4.532343,6.564429,-2.966835,0.686489,6.442541,8.442927,2.296781,-5.859355,0.151459,6.345835,9.651356,-2.907395,-2.661260,7.926104,8.301215,1.517073,-3.919880,5.032812,5.775527,6.205596,3.966770,0.460571,7.729988,-5.030306,9.420206,-4.566480,3.851955,2.308044,0.380071,0.612871,0.301781,0.590241,8.445841,2.443581,5.126401,-2.363450,1.786966,7.381130,7.343742,-2.626616,6.061880,-5.805108,0.263751,-0.971616,-5.439304,1.162764,-0.008955,-0.049741,-4.682155,-1.623469,-3.352953,-7.735485,-6.452330,-1.223827,6.797694,-9.543430,8.734634,3.884097,-6.859013,-9.117024,8.223801,7.710437,-0.141576,-0.666991,1.326542,-3.781895,9.794693,5.496815,-3.873919,0.879740,-4.172217,-9.150762,-9.013883,3.907613,0.811731,-2.012714,3.786375,-0.834151,3.809235,-5.966996,6.743957,-6.248296,7.607070,-3.826595,5.970791,-0.828580,5.121080,-3.085869,-0.730179,0.523990,7.118881,2.094413,4.968813,-4.416610,-2.499957,4.880672,0.190531,-1.965288,5.328074,-9.673461,-9.976254,9.437795,6.551221,-0.612525,6.270023,0.488596,9.772108,7.722058,-4.762555,8.719326,3.904558,-0.809090,-1.429478,6.242760,5.572019,-0.616298,-1.602835,1.972167,0.880517,-7.086692,7.186373,4.757056,-4.954313,4.268412,-4.662692,3.766408,7.778770,-6.786832,-4.134648,-1.176732,9.741773,1.744859,-7.131269,0.869183,-7.927817,-6.954873,8.912654,-2.645777,-9.669734,-3.269124,-1.019413,-3.246891,2.562508,4.436845,7.654066,8.736691,8.661306,-5.172457,-6.421261,5.594477,4.099055,-1.217351,-3.300578,-0.031490,4.762268,3.125773,-2.820315,6.936188,0.278443,2.282921,-8.443703,7.601559,-7.792175,1.211912,-8.686485,6.785663,-9.288698,-0.391164,5.492952,-6.799099,-5.550932,-7.385462,2.818416,-2.411864,3.624666,4.538936,5.067243,8.172336,8.189270,-0.023784,0.984497,7.963803,2.919768,-5.579615,9.055497,7.444181,2.318783,-2.206890,-2.142933,7.328568,3.844049,7.292463,8.809024,-3.833124,-7.211463,-6.195758,-8.284462,2.323277,-7.189822,-6.055785,-2.649526,5.441822,-1.113443,1.386827,-0.068097,-1.661838,8.266778,-5.690173,-8.172673,0.204120,1.311044,-4.601472,-6.674213,-5.635625,-5.175112,-5.332807,-9.915634,-7.081725,8.256996,7.256105,-2.096336,4.339242,-3.963336,-2.377242,-3.474982,8.155683,-1.161183,-0.577323,0.138608,4.035736,9.833649,9.797429,3.199006,-6.103946,4.215559,-3.835793,3.414105,3.218902,-0.401901,-6.604988,-8.007819,-6.058128,-7.568839,9.791600,2.068179,6.835672,-6.626011,8.350137,-4.461202,-3.627851,3.029186,5.453791,3.682624,-0.411874,-8.020400,-9.222985,-4.642598,7.588820,8.457474,8.789637,4.382079,-2.436870,7.769941,4.899694,0.868535,7.768359,0.027772,-2.064047,5.152215,-6.941825,3.386963,-4.673376,8.581636,-7.489595,-4.811828,-0.420014,-6.142782,6.636537,-9.891167,6.656994,6.954237,-8.200328,8.242785,3.408544,-1.260254,1.329103,-4.941446,0.217785,6.946039,9.496662,0.764502,-7.698281,-2.449476,9.952527,-3.544437,-0.384221,6.123684,-4.159257,9.257799,-5.938329,6.620717,-2.757416,9.448299,-7.892814,8.806399,3.227329,9.817658,5.362013,3.240416,-9.706441,0.563592,4.719023,8.111371,-3.439753,6.469291,-3.767906,-2.767411,6.067516,2.998833,-0.967658,0.662137,0.015238,4.063022,-0.648189,-0.920181,4.380810,8.868146,-5.706443,-9.686326,-8.120261,1.005669,3.457766,6.014373,-6.398501,-1.898929,9.042138,-2.608627,-1.251050,3.760771,-5.181505,2.348171,-2.016243,5.748904,8.462011,9.589805,9.132974,4.113594,-7.956981,3.012013,9.546045,7.590316,2.061742,5.941547,-7.429185,-1.461749,-1.797941,-8.460434,8.292028,-8.187998,2.537091,-6.302418,-6.887866,6.275243,-3.920055,7.715001,-9.253437,-7.456603,-9.959154,9.279062,2.100863,-1.693900,2.814874,-1.624256,-6.329360,-3.609981,-0.577684,-3.681626,-5.299207,7.580326,4.574384,-2.656721,3.973927,7.158778,-5.038450,-6.650437,5.810470,-9.409165,5.576454,6.196592,7.466235,-6.207447,-2.582848,-8.442867,-0.363644,2.600380,5.663730,-2.954843,-3.868101,-2.649304,-3.929050,-5.751882,5.743252,5.245011,5.585952,-5.424254,-6.509209,-1.131983,-9.276424,5.952539,-0.416102,-3.910482,-9.167025,5.197456,-3.539576,3.254707,-3.136434,-6.301998,-2.091918,6.911005,-9.423921,-8.118372,-4.318135,9.781227,-8.663423,1.714056,1.369565,-5.414023,-2.618829,0.401014,4.347620,-6.391700,-4.865115,-4.258978,-6.386797,5.068742,3.873884,0.438892,-1.372934,-3.603463,7.157921,-7.270159,5.360862,-7.929237,-7.391865,8.799406,-0.262773,4.883779,-9.517026,-8.162298,2.168722,-1.387121,4.898564,-3.024706,-6.422754,-4.531633,2.966532,5.442847,3.992590,-3.986228,2.518738,-6.418620,6.613905,-0.875757,5.826179,-0.551297,-8.022435,8.058590,-8.475166,-2.767087,1.682879,-8.885277,1.617009,7.504992,1.604671,-1.195060,9.098333,9.413378,-4.852937,0.468943,-5.315711,6.974021,-5.732964,-9.001120,-7.045802,7.871002,-5.525833,-3.368889,8.779435,-4.707563,-7.720019,2.112067,1.982056,-2.705863,5.084018,6.961803,-8.183955,-1.406293,-4.338469,7.347628,6.263525,-2.129732,0.635915,3.008083,-0.597715,9.110385,-2.079444,2.819643,6.911842,-0.531096,8.754040,-8.848252,-2.091512,-6.953133,-5.295010,7.798121,-3.198490,7.259516,1.372664,1.651732,-5.668036,-4.850528,4.071445,5.736395,6.233094,7.921553,8.867901,-8.636049,1.135247,-8.117732,5.139821,1.732093,0.418018,1.540766,-9.594683,7.640214,8.977525,8.512265,7.016429,-9.506990,-6.559477,2.166852,2.025903,1.039821,-4.607586,-4.675729,-8.927605,6.299832,-7.135356,-9.291312,0.393925,-4.376115,6.337649,-9.768733,-0.150657,3.969016,-2.598927,-0.458203,3.467541,-0.307193,-3.066487,7.719312,2.279741,-0.510348,5.852405,-0.376759,-3.209259,6.818853,-1.524956,-2.423488,-7.078043,-7.874208,-6.696116,1.306412,-2.783733,7.876758,-1.791439,6.852917,-2.567475,-7.021610,-7.473170,-6.612814,5.551562,-2.202928,1.279852,-6.443375,9.959638,8.633649,6.437727,9.936212,-2.291377,-7.740408,9.484306,-5.388316,-6.133975,5.267243,7.435796,7.356678,4.323605,9.481866,0.271963,6.913757,-3.556961,-4.463162,8.011577,2.249074,9.464531,-9.203100,-8.419727,-3.241641,6.456959,5.518108,3.519810,9.767657,9.895336,-6.438565,-3.024303,0.605984,-1.099560,7.592542,5.233201,2.209191,-1.671481,0.825015,7.025141,6.399309,4.091021,1.111981,-2.677074,8.812079,0.026834,-9.879388,8.491729,-9.625943,8.554014,7.129085,7.091215,1.222363,3.085036,-0.544407,-4.289686,8.819371,-8.853811,3.017824,-0.094427,-6.284582,-7.696125,3.447510,-4.109863,5.837732,3.525844,-0.224498,8.597323,1.212387,-8.342325,1.912247,8.477672,-3.224540,-6.372335,-5.356089,8.593050,-5.024100,1.239164,3.486503,-1.659231,-8.276886,-9.437154,-9.152670,-1.552887,-9.402139,7.462208,-4.883335,-6.396620,-0.700833,-9.446029,4.853915,-9.742283,3.203561,-9.538241,0.679172,4.183268,-1.838008,3.198962,1.972017,-6.925001,-6.242571,-2.646592,7.224673,-2.487500,7.881472,-2.831778,-5.370298,-2.383856,8.579196,-9.207316,7.223923,-3.786755,4.687026,-6.782068,8.320759,-1.381538,-7.587825,-7.033998,-5.346182,-9.682927,7.996636,-9.961668,2.094910,1.811263,9.240686,6.379524,0.509310,9.290067,2.765150,-3.914139,-7.527896,3.672228,0.086431,-3.106474,-2.356491,2.153504,-1.764957,4.994170,-2.949429,-3.640722,-8.335719,3.937337,1.431819,5.331319,-8.928504,7.364058,-9.631088,-1.527234,7.621449,3.388346,4.901242,5.268585,8.990593,5.719637,-7.326298,9.408010,0.071674,-5.328459,3.970163,-3.785138,4.191363,1.331970,-5.162733,2.425677,-2.844633,6.159134,6.408328,7.142585,7.080869,9.911477,-2.463753,-1.091483,7.576237,-3.376345,-1.525613,-5.346967,1.616304,-5.663236,7.600817,7.001307,-0.814204,1.810975,4.942429,-9.196321,2.597897,-3.017612,4.952154,-8.155797,-2.221998,2.760981,4.453938,-5.419725,5.226079,-2.224512,3.838212,2.860197,-3.693851,2.291856,7.089565,-5.705948,5.963517,5.888160,9.870136,4.166263,-2.986454,7.519054,7.209202,-8.168034,-7.585137,1.436165,-3.353925,7.349123,-3.891793,9.410448,5.398946,-5.305354,-6.205204,6.002388,0.386557,0.465707,4.980801,4.596999,1.828757,-5.065139,-4.000751,7.112359,-8.961012,2.632245,3.046188,-8.261014,-7.442022,-4.177943,-9.598004,5.972724,-4.538011,-7.160539,4.737642,-5.334998,1.404620,-1.692399,9.848877,3.474404,-7.773548,-7.549993,4.157035,-8.717148,8.060535,-3.742144,-2.155047,-5.016111,1.780785,4.859876,-3.697903,3.292680,-9.563543,-7.496111,4.563976,8.565189,-7.926737,8.344564,-8.591300,-3.812734,-4.595808,-6.429571,-2.989503,-9.784926,2.992020,-5.990235,5.144950,6.281422,4.236633,1.790521,6.525916,-0.401581,-0.441686,3.027228,-9.968701,2.363689,2.032667,4.930039,-6.613795,2.427400,5.381011,3.158644,6.643501,-4.740935,-8.015740,8.857419,-5.386816,-9.737582,8.617104,-6.928808,3.935798,8.547894,4.726981,-9.606144,-6.369344,2.228197,5.637397,-1.031137,2.313137,1.797876,5.585380,-9.898098,-0.987910,-6.509364,-9.659937,4.685781,-4.258558,-7.653825,-7.286943,8.362056,-3.627766,-8.489694,-1.595632,-9.935127,-2.559976,8.611352,-7.372037,5.854252,-1.021536,0.936000,-2.610150,-2.285923,2.394268,-6.364695,6.786242,-0.232765,-9.253147,3.327887,1.618787,9.996713,6.358235,4.263422,-5.159916,8.634866,9.016156,5.338106,0.561986,-0.785486,2.070208,-6.830789,0.133949,-5.566715,-0.310942,-5.372695,-5.868707,9.174787,-2.358943,6.405616,7.905356,-3.802941,3.126453,0.822707,6.010487,8.067477,-5.203042,-9.878317,-4.384383,-9.111509,-5.932091,0.592085,-1.342651,2.820800,1.346821,0.786456,3.170560,1.503314,3.345113,7.217701,4.991956,9.580239,7.898535,3.809975,8.327806,-9.591094,-8.680963,-2.447255,-1.907349,0.921855,-6.298411,-9.440784,-3.544565,3.825667,-3.215210,1.195735,2.505602,-8.724248,-3.358513,1.769398,3.236461,8.482860,2.239592,-8.027520,0.014194,2.603647,-8.827041,1.799677,-7.076504,-9.176600,-3.978707,-3.082524,9.356435,-3.240023,-6.741076,4.720412,9.168455,5.381114,-6.154063,-6.835833,2.542860,5.673857,8.366875,5.051498,5.315816,3.791997,3.832465,-3.997584,-0.528671,-6.650377,-3.289765,-8.241938,-3.113565,-6.257510,7.014330,0.793456,-3.557675,-6.319606,5.562521,0.474809,6.562434,-3.341812,-0.161061,3.539841,6.468140,8.604533,0.208682,8.800911,5.504092,-0.370209,-5.305388,-9.440689,9.503513,5.002627,-4.359965,0.494688,6.534599,-6.489625,-0.323676,-1.943813,7.314414,4.007705,2.035196,-4.459563,-1.840136,7.322655,-9.566535,-2.938272,-9.566726,4.808324,-0.442630,-4.910539,-4.933034,-2.382607,4.463869,0.683500,-4.368926,5.788059,6.087654,3.809693,4.808233,2.338854,-8.115784,3.845005,3.777482,5.443022,6.818161,8.632063,-5.909949,4.531024,-0.984278,-1.554286,1.817724,-7.845959,0.523602,1.848471,-8.519100,9.877778,-9.619514,7.743692,4.527949,4.480180,-0.321157,-7.774786,-0.851457,-4.330527,-9.520658,-8.433379,8.653551,1.622296,-1.195039,5.179180,6.403581,5.122745,1.619260,6.627206,8.207479,1.758403,4.073545,-9.362627,0.199028,-3.009100,0.687043,-4.644085,6.657666,6.566583,-0.598266,-6.531708,0.481275,5.515300,-6.962838,4.030383,8.016139,4.369313,0.283346,1.309101,0.154774,-3.007895,-3.503481,8.878721,-0.846510,5.525683,9.006242,-0.841876,0.698322,1.900567,-7.322465,0.728502,0.259789,-1.688848,-6.800266,-1.055287,9.059586,-4.221039,9.594943,7.406096,-0.171333,-7.568353,-6.865051,7.195045,-0.430667,5.507172,1.542713,-0.517687,-6.886508,5.900802,-7.600584,-4.591534,8.953280,7.346026,-3.608804,-9.697166,9.406627,-3.887582,-4.190094,5.934141,-2.359512,8.515676,9.678398,-6.350229,8.416122,-8.614292,7.666027,3.163731,8.726242,8.595628,-2.266750,3.438679,-4.828802,5.913600,5.229593,4.992122,-9.412411,6.130003,8.361405,6.063014,-5.014154,-7.201517,-6.829744,-0.287308,0.487445,1.660215,8.615470,8.703856,-1.829916,-8.400864,-0.369932,8.098041,3.336498,-5.579714,-3.937243,6.572262,-1.028946,7.259779,9.437281,-9.776558,4.078301,-1.675405,-0.800778,6.020023,2.017391,-7.672387,1.152607,-8.061198,8.923712,7.240988,-0.894252,-7.518721,7.812395,4.691402,3.728713,1.422539,1.510886,9.952794,6.359330,-4.679211,4.456976,-5.082806,-8.570995,5.653805,-4.334772,0.756493,1.741436,3.707001,2.311806,7.435346,-0.675061,-8.026496,3.121701,-5.754880,-5.371113,7.876401,6.807041,-7.075039,-1.789043,3.715741,9.247675,5.941954,-0.162523,9.034800,5.705272,-5.087163,1.035145,3.168152,6.403547,8.716181,-4.619464,2.326218,3.928150,7.563437,1.430924,-0.223292,6.036766,8.800098,-6.610624,-3.753874,7.460311,3.817962,6.873662,5.845715,-2.465188,-7.289608,3.589745,1.083274,7.518497,-6.579564,5.942871,3.872043,-1.772302,5.996747,2.923352,-9.331614,-8.060043,3.044515,-1.382946,-0.817085,-6.830838,0.897048,-1.911588,-9.437780,6.561999,-1.779742,4.543289,-2.401366,-3.828852,-2.728640,4.229331,6.918943,-6.936735,2.861275,5.726146,-6.010981,-3.635078,-0.121019,-2.056606,-7.971609,5.648688,-7.446913,1.761661,7.792465,-8.917754,1.678747,-7.171157,-5.968369,-6.220870,-9.448912,5.494570,5.334515,-4.170168,4.554521,-7.289356,6.069023,-0.310455,-5.582049,-2.180934,-1.659282,7.933859,-9.733739,-9.020504,-3.089882,-0.945399,-5.007700,4.556465,5.368218,2.305775,-7.281249,-7.057305,-1.858548,-4.967176,-7.020550,-1.661047,2.546570,4.826868,0.607868,-1.769833,-2.106687,-9.555002,5.733829,-5.788898,-7.138297,3.316408,7.051278,-4.272128,-8.905307,-1.443669,2.380240,2.062095,-5.384478,-1.175045,-7.023644,8.607958,3.411613,-3.719951,-8.569902,6.691212,-1.676331,7.133712,-7.738585,1.913233,-0.064982,-3.960430,-4.412385,5.549106,-5.787914,6.553313,-2.424988,5.936088,-4.054584,-9.240396,-8.630903,9.833970,-2.790155,-8.183729,-5.125951,-6.425670,3.492159,-0.652445,-9.352968,-9.674564,1.278424,-2.924601,-4.145111,3.859781,6.283908,8.519558,8.401218,-4.686203,-7.337293,3.496344,3.022645,5.092374,-4.534985,-7.597255,9.376556,0.564340,-9.727672,5.639988,8.444890,-5.268504,-2.390552,-6.586366,-0.130924,-2.238300,3.298859,-5.542479,6.927287,8.427628,5.884532,-6.793591,-4.042057,-7.624611,7.351540,7.146834,-9.685188,2.867655,-6.201955,7.683702,0.244548,4.805126,3.591999,6.933667,2.838323,-5.017395,-2.311258,-4.095446,-7.175908,-8.450491,-1.965702,-0.768149,9.987988], dtype = "float32")#candidate|14452|(2400,)|const|float32
call_14449 = relay.TupleGetItem(func_3701_call(relay.reshape(const_14450.astype('float64'), [13, 6, 5]), relay.reshape(var_14451.astype('uint32'), [63,]), relay.reshape(const_14452.astype('float32'), [2400,]), ), 1)
call_14453 = relay.TupleGetItem(func_3706_call(relay.reshape(const_14450.astype('float64'), [13, 6, 5]), relay.reshape(var_14451.astype('uint32'), [63,]), relay.reshape(const_14452.astype('float32'), [2400,]), ), 1)
output = relay.Tuple([bop_14445,call_14449,const_14450,var_14451,const_14452,])
output2 = relay.Tuple([bop_14445,call_14453,const_14450,var_14451,const_14452,])
func_14462 = relay.Function([var_14443,var_14444,var_14451,], output)
mod['func_14462'] = func_14462
mod = relay.transform.InferType()(mod)
var_14463 = relay.var("var_14463", dtype = "int8", shape = (9, 5, 6))#candidate|14463|(9, 5, 6)|var|int8
var_14464 = relay.var("var_14464", dtype = "int8", shape = (9, 5, 6))#candidate|14464|(9, 5, 6)|var|int8
var_14465 = relay.var("var_14465", dtype = "uint32", shape = (63,))#candidate|14465|(63,)|var|uint32
output = func_14462(var_14463,var_14464,var_14465,)
func_14466 = relay.Function([var_14463,var_14464,var_14465,], output)
mutated_mod['func_14466'] = func_14466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10241_call = mod.get_global_var('func_10241')
func_10243_call = mutated_mod.get_global_var('func_10243')
call_14473 = func_10241_call()
call_14474 = func_10241_call()
output = relay.Tuple([call_14473,])
output2 = relay.Tuple([call_14474,])
func_14486 = relay.Function([], output)
mod['func_14486'] = func_14486
mod = relay.transform.InferType()(mod)
output = func_14486()
func_14487 = relay.Function([], output)
mutated_mod['func_14487'] = func_14487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13445_call = mod.get_global_var('func_13445')
func_13447_call = mutated_mod.get_global_var('func_13447')
call_14494 = relay.TupleGetItem(func_13445_call(), 0)
call_14495 = relay.TupleGetItem(func_13447_call(), 0)
var_14507 = relay.var("var_14507", dtype = "float32", shape = (65, 9))#candidate|14507|(65, 9)|var|float32
bop_14508 = relay.equal(call_14494.astype('bool'), relay.reshape(var_14507.astype('bool'), relay.shape_of(call_14494))) # shape=(65, 9)
bop_14511 = relay.equal(call_14495.astype('bool'), relay.reshape(var_14507.astype('bool'), relay.shape_of(call_14495))) # shape=(65, 9)
uop_14514 = relay.asinh(bop_14508.astype('float64')) # shape=(65, 9)
uop_14516 = relay.asinh(bop_14511.astype('float64')) # shape=(65, 9)
output = uop_14514
output2 = uop_14516
func_14520 = relay.Function([var_14507,], output)
mod['func_14520'] = func_14520
mod = relay.transform.InferType()(mod)
mutated_mod['func_14520'] = func_14520
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14521 = relay.var("var_14521", dtype = "float32", shape = (65, 9))#candidate|14521|(65, 9)|var|float32
func_14520_call = mutated_mod.get_global_var('func_14520')
call_14522 = func_14520_call(var_14521)
output = call_14522
func_14523 = relay.Function([var_14521], output)
mutated_mod['func_14523'] = func_14523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11872_call = mod.get_global_var('func_11872')
func_11873_call = mutated_mod.get_global_var('func_11873')
call_14559 = relay.TupleGetItem(func_11872_call(), 0)
call_14560 = relay.TupleGetItem(func_11873_call(), 0)
func_11872_call = mod.get_global_var('func_11872')
func_11873_call = mutated_mod.get_global_var('func_11873')
call_14572 = relay.TupleGetItem(func_11872_call(), 1)
call_14573 = relay.TupleGetItem(func_11873_call(), 1)
func_6067_call = mod.get_global_var('func_6067')
func_6073_call = mutated_mod.get_global_var('func_6073')
var_14588 = relay.var("var_14588", dtype = "uint16", shape = (1024,))#candidate|14588|(1024,)|var|uint16
var_14589 = relay.var("var_14589", dtype = "float32", shape = (630,))#candidate|14589|(630,)|var|float32
call_14587 = relay.TupleGetItem(func_6067_call(relay.reshape(var_14588.astype('uint16'), [16, 4, 16]), relay.reshape(var_14588.astype('uint16'), [16, 4, 16]), relay.reshape(var_14589.astype('float32'), [70, 9]), relay.reshape(var_14588.astype('bool'), [16, 4, 16]), ), 1)
call_14590 = relay.TupleGetItem(func_6073_call(relay.reshape(var_14588.astype('uint16'), [16, 4, 16]), relay.reshape(var_14588.astype('uint16'), [16, 4, 16]), relay.reshape(var_14589.astype('float32'), [70, 9]), relay.reshape(var_14588.astype('bool'), [16, 4, 16]), ), 1)
output = relay.Tuple([call_14559,call_14572,call_14587,var_14588,var_14589,])
output2 = relay.Tuple([call_14560,call_14573,call_14590,var_14588,var_14589,])
func_14608 = relay.Function([var_14588,var_14589,], output)
mod['func_14608'] = func_14608
mod = relay.transform.InferType()(mod)
mutated_mod['func_14608'] = func_14608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14608_call = mutated_mod.get_global_var('func_14608')
var_14610 = relay.var("var_14610", dtype = "uint16", shape = (1024,))#candidate|14610|(1024,)|var|uint16
var_14611 = relay.var("var_14611", dtype = "float32", shape = (630,))#candidate|14611|(630,)|var|float32
call_14609 = func_14608_call(var_14610,var_14611,)
output = call_14609
func_14612 = relay.Function([var_14610,var_14611,], output)
mutated_mod['func_14612'] = func_14612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13380_call = mod.get_global_var('func_13380')
func_13382_call = mutated_mod.get_global_var('func_13382')
call_14678 = func_13380_call()
call_14679 = func_13380_call()
func_12779_call = mod.get_global_var('func_12779')
func_12781_call = mutated_mod.get_global_var('func_12781')
call_14681 = func_12779_call()
call_14682 = func_12779_call()
func_13643_call = mod.get_global_var('func_13643')
func_13646_call = mutated_mod.get_global_var('func_13646')
var_14688 = relay.var("var_14688", dtype = "float64", shape = ())#candidate|14688|()|var|float64
call_14687 = relay.TupleGetItem(func_13643_call(relay.reshape(var_14688.astype('float64'), [])), 2)
call_14689 = relay.TupleGetItem(func_13646_call(relay.reshape(var_14688.astype('float64'), [])), 2)
output = relay.Tuple([call_14678,call_14681,call_14687,var_14688,])
output2 = relay.Tuple([call_14679,call_14682,call_14689,var_14688,])
func_14691 = relay.Function([var_14688,], output)
mod['func_14691'] = func_14691
mod = relay.transform.InferType()(mod)
var_14692 = relay.var("var_14692", dtype = "float64", shape = ())#candidate|14692|()|var|float64
output = func_14691(var_14692)
func_14693 = relay.Function([var_14692], output)
mutated_mod['func_14693'] = func_14693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14486_call = mod.get_global_var('func_14486')
func_14487_call = mutated_mod.get_global_var('func_14487')
call_14709 = relay.TupleGetItem(func_14486_call(), 0)
call_14710 = relay.TupleGetItem(func_14487_call(), 0)
output = call_14709
output2 = call_14710
func_14723 = relay.Function([], output)
mod['func_14723'] = func_14723
mod = relay.transform.InferType()(mod)
mutated_mod['func_14723'] = func_14723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14723_call = mutated_mod.get_global_var('func_14723')
call_14724 = func_14723_call()
output = call_14724
func_14725 = relay.Function([], output)
mutated_mod['func_14725'] = func_14725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13380_call = mod.get_global_var('func_13380')
func_13382_call = mutated_mod.get_global_var('func_13382')
call_14788 = func_13380_call()
call_14789 = func_13380_call()
func_12368_call = mod.get_global_var('func_12368')
func_12370_call = mutated_mod.get_global_var('func_12370')
call_14790 = relay.TupleGetItem(func_12368_call(), 0)
call_14791 = relay.TupleGetItem(func_12370_call(), 0)
output = relay.Tuple([call_14788,call_14790,])
output2 = relay.Tuple([call_14789,call_14791,])
func_14810 = relay.Function([], output)
mod['func_14810'] = func_14810
mod = relay.transform.InferType()(mod)
mutated_mod['func_14810'] = func_14810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14810_call = mutated_mod.get_global_var('func_14810')
call_14811 = func_14810_call()
output = call_14811
func_14812 = relay.Function([], output)
mutated_mod['func_14812'] = func_14812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13692_call = mod.get_global_var('func_13692')
func_13694_call = mutated_mod.get_global_var('func_13694')
call_14831 = relay.TupleGetItem(func_13692_call(), 0)
call_14832 = relay.TupleGetItem(func_13694_call(), 0)
var_14845 = relay.var("var_14845", dtype = "float32", shape = (65, 9))#candidate|14845|(65, 9)|var|float32
bop_14846 = relay.mod(call_14831.astype('float64'), relay.reshape(var_14845.astype('float64'), relay.shape_of(call_14831))) # shape=(65, 9)
bop_14849 = relay.mod(call_14832.astype('float64'), relay.reshape(var_14845.astype('float64'), relay.shape_of(call_14832))) # shape=(65, 9)
output = bop_14846
output2 = bop_14849
func_14854 = relay.Function([var_14845,], output)
mod['func_14854'] = func_14854
mod = relay.transform.InferType()(mod)
var_14855 = relay.var("var_14855", dtype = "float32", shape = (65, 9))#candidate|14855|(65, 9)|var|float32
output = func_14854(var_14855)
func_14856 = relay.Function([var_14855], output)
mutated_mod['func_14856'] = func_14856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_14984 = func_10556_call()
call_14985 = func_10556_call()
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_15081 = func_11738_call()
call_15082 = func_11738_call()
output = relay.Tuple([call_14984,call_15081,])
output2 = relay.Tuple([call_14985,call_15082,])
func_15095 = relay.Function([], output)
mod['func_15095'] = func_15095
mod = relay.transform.InferType()(mod)
mutated_mod['func_15095'] = func_15095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15095_call = mutated_mod.get_global_var('func_15095')
call_15096 = func_15095_call()
output = call_15096
func_15097 = relay.Function([], output)
mutated_mod['func_15097'] = func_15097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13918_call = mod.get_global_var('func_13918')
func_13919_call = mutated_mod.get_global_var('func_13919')
call_15098 = func_13918_call()
call_15099 = func_13918_call()
func_11796_call = mod.get_global_var('func_11796')
func_11797_call = mutated_mod.get_global_var('func_11797')
call_15113 = func_11796_call()
call_15114 = func_11796_call()
uop_15125 = relay.cosh(call_15113.astype('float64')) # shape=(10, 14, 4)
uop_15127 = relay.cosh(call_15114.astype('float64')) # shape=(10, 14, 4)
output = relay.Tuple([call_15098,uop_15125,])
output2 = relay.Tuple([call_15099,uop_15127,])
func_15129 = relay.Function([], output)
mod['func_15129'] = func_15129
mod = relay.transform.InferType()(mod)
mutated_mod['func_15129'] = func_15129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15129_call = mutated_mod.get_global_var('func_15129')
call_15130 = func_15129_call()
output = call_15130
func_15131 = relay.Function([], output)
mutated_mod['func_15131'] = func_15131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11796_call = mod.get_global_var('func_11796')
func_11797_call = mutated_mod.get_global_var('func_11797')
call_15198 = func_11796_call()
call_15199 = func_11796_call()
output = relay.Tuple([call_15198,])
output2 = relay.Tuple([call_15199,])
func_15200 = relay.Function([], output)
mod['func_15200'] = func_15200
mod = relay.transform.InferType()(mod)
output = func_15200()
func_15201 = relay.Function([], output)
mutated_mod['func_15201'] = func_15201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12999_call = mod.get_global_var('func_12999')
func_13000_call = mutated_mod.get_global_var('func_13000')
call_15255 = func_12999_call()
call_15256 = func_12999_call()
output = call_15255
output2 = call_15256
func_15274 = relay.Function([], output)
mod['func_15274'] = func_15274
mod = relay.transform.InferType()(mod)
mutated_mod['func_15274'] = func_15274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15274_call = mutated_mod.get_global_var('func_15274')
call_15275 = func_15274_call()
output = call_15275
func_15276 = relay.Function([], output)
mutated_mod['func_15276'] = func_15276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12277_call = mod.get_global_var('func_12277')
func_12279_call = mutated_mod.get_global_var('func_12279')
call_15295 = relay.TupleGetItem(func_12277_call(), 3)
call_15296 = relay.TupleGetItem(func_12279_call(), 3)
output = relay.Tuple([call_15295,])
output2 = relay.Tuple([call_15296,])
func_15316 = relay.Function([], output)
mod['func_15316'] = func_15316
mod = relay.transform.InferType()(mod)
output = func_15316()
func_15317 = relay.Function([], output)
mutated_mod['func_15317'] = func_15317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14486_call = mod.get_global_var('func_14486')
func_14487_call = mutated_mod.get_global_var('func_14487')
call_15321 = relay.TupleGetItem(func_14486_call(), 0)
call_15322 = relay.TupleGetItem(func_14487_call(), 0)
func_15316_call = mod.get_global_var('func_15316')
func_15317_call = mutated_mod.get_global_var('func_15317')
call_15327 = relay.TupleGetItem(func_15316_call(), 0)
call_15328 = relay.TupleGetItem(func_15317_call(), 0)
func_6813_call = mod.get_global_var('func_6813')
func_6816_call = mutated_mod.get_global_var('func_6816')
var_15330 = relay.var("var_15330", dtype = "float64", shape = (250,))#candidate|15330|(250,)|var|float64
var_15331 = relay.var("var_15331", dtype = "int8", shape = (275, 2))#candidate|15331|(275, 2)|var|int8
call_15329 = relay.TupleGetItem(func_6813_call(relay.reshape(var_15330.astype('float64'), [5, 5, 10]), relay.reshape(var_15331.astype('int8'), [550,]), ), 1)
call_15332 = relay.TupleGetItem(func_6816_call(relay.reshape(var_15330.astype('float64'), [5, 5, 10]), relay.reshape(var_15331.astype('int8'), [550,]), ), 1)
output = relay.Tuple([call_15321,call_15327,call_15329,var_15330,var_15331,])
output2 = relay.Tuple([call_15322,call_15328,call_15332,var_15330,var_15331,])
func_15333 = relay.Function([var_15330,var_15331,], output)
mod['func_15333'] = func_15333
mod = relay.transform.InferType()(mod)
mutated_mod['func_15333'] = func_15333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15333_call = mutated_mod.get_global_var('func_15333')
var_15335 = relay.var("var_15335", dtype = "float64", shape = (250,))#candidate|15335|(250,)|var|float64
var_15336 = relay.var("var_15336", dtype = "int8", shape = (275, 2))#candidate|15336|(275, 2)|var|int8
call_15334 = func_15333_call(var_15335,var_15336,)
output = call_15334
func_15337 = relay.Function([var_15335,var_15336,], output)
mutated_mod['func_15337'] = func_15337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14810_call = mod.get_global_var('func_14810')
func_14812_call = mutated_mod.get_global_var('func_14812')
call_15341 = relay.TupleGetItem(func_14810_call(), 1)
call_15342 = relay.TupleGetItem(func_14812_call(), 1)
func_10945_call = mod.get_global_var('func_10945')
func_10946_call = mutated_mod.get_global_var('func_10946')
call_15359 = func_10945_call()
call_15360 = func_10945_call()
func_11633_call = mod.get_global_var('func_11633')
func_11636_call = mutated_mod.get_global_var('func_11636')
call_15362 = relay.TupleGetItem(func_11633_call(relay.reshape(call_15341.astype('float32'), [15, 9, 9])), 0)
call_15363 = relay.TupleGetItem(func_11636_call(relay.reshape(call_15341.astype('float32'), [15, 9, 9])), 0)
func_11215_call = mod.get_global_var('func_11215')
func_11219_call = mutated_mod.get_global_var('func_11219')
const_15396 = relay.const([-1,-5,4,2,-10,6,-2,6,8,4,-4,-5,-2,9,-9,9,-9,7,-8,-3,-3,6,6,3,8,5,10,-9,8,4,-6,9,1,1,4,8,5,-5,6,4,-9,7,10,4,2,7,-4,7,4,-3,-2,-10,-6,5,-4,7,-7,-3,-10,6,6,4,-2,5,7,-8,2,-5,2,-2,10,-2,-4,5,-3,-8,4,10,2,-4,5,9,2,6,5,-2,7,-1,10,-7,-5,-3,8,7,-9,7,4,3,-10,-10,7,10,-8,7,5,1,10,10,-7,5,7,2,-10,7,-4,-6,1,-6,-5,8,-8,1,-3,5,-8,-8,4,8,4,5,6,-10,-7,7,1,3,2,-7,-7,-7,-3,-3,4,3,9,-8,9,-2,-8,10,2,-9,9,1,10,-2,2,2,-5,6,2,8,3,8,9,-3,3,-7,-9,8,-8,-4,4,-6,10,-4,7,-4,4,-4,-1,-5,-8,-7,-3,-10,-3,-1,2,-7,-1,-7,-5,-9,-4,-3,9,-9,2,-7,9,4,-2,9,4,6,-9,4,-3,-4,-7,2,-4,-4,-7,1,-8,7,2,4,6,-9,-3,6,7,5,-6,9,-9,8,6,1,-4,4,8,2,-7,6,6,-8,-3,-5,1,1,-9,-6,-10,-8,7,10,7,-9,5,-6,9,-1,8,-3,10,-1,-5,-3,-7,-9,3,2,-3,6,-6,6,6,-2,-3,-5,9,3,4,10,9,6,1,5,8,-2,6,4,7,-8,8,-5,-9,4,-6,-7,-4,-8,10,8,7,-4,8,-4,-3,5,-6,-10,-9,-10,-9,-2,1,-7,-3,1,-5,-4,-3,9,-3,-9,5,5,4,-10,4,5,2,-6,-6,-7,-2,-5,-1,2,9,4,3,-9,-9,-1,3,-10,-9,-9,3,-8,-9,1,9,8,7,3,3,6,-5,7,-2,-10,-3,-7,-7,9,-8,-7,-4,-7,9,10,6,-6,-2,6,9,-6,-4,-7,8,8,8,4,-2,-4,3,-3,-1,-7,-1,8,8,2,-7,-5,-9,-2,8,-1,-9,1,1,10,-2,-5,-9,-5,-9,10,-8,-2,8,1,9,8,1,9,-5,5,5,2,-3,2,-4,9,-1,-6,-2,-7,-1,9,6,5,7,9,-10,-6,8,6,-4,1,-5,-4,-3,9,8,9,6,-7,4,4,7,-8,10,6,-10,-7,3,1,4,2,-8,8,-7,-6,1,4,10,4,7,-3,-6,-1,4,4,9,-10,1,10,2,-6,8,4,5,9,9,-10,-4,3,10,-8,7,6,7,-3,-4,4,2,-9,8,-8,1,2,-8,5,-4,7,-10,-7,-10,6,1,5,9,-10,-3,-4,8,-10,-8,-4,-8,4,-3,5,-3,-7,-2,-10,10,8,10,-8,7,-3,-4,9,-8,-10,-4,-6,7,-3,-8,1,-5,-1,-2,-1,8,-4,-1,-4], dtype = "int8")#candidate|15396|(550,)|const|int8
call_15395 = relay.TupleGetItem(func_11215_call(relay.reshape(call_15341.astype('float32'), [15, 9, 9]), relay.reshape(const_15396.astype('int8'), [55, 10]), ), 2)
call_15397 = relay.TupleGetItem(func_11219_call(relay.reshape(call_15341.astype('float32'), [15, 9, 9]), relay.reshape(const_15396.astype('int8'), [55, 10]), ), 2)
output = relay.Tuple([call_15341,call_15359,call_15362,call_15395,const_15396,])
output2 = relay.Tuple([call_15342,call_15360,call_15363,call_15397,const_15396,])
func_15399 = relay.Function([], output)
mod['func_15399'] = func_15399
mod = relay.transform.InferType()(mod)
mutated_mod['func_15399'] = func_15399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15399_call = mutated_mod.get_global_var('func_15399')
call_15400 = func_15399_call()
output = call_15400
func_15401 = relay.Function([], output)
mutated_mod['func_15401'] = func_15401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_15444 = relay.TupleGetItem(func_11409_call(), 4)
call_15445 = relay.TupleGetItem(func_11410_call(), 4)
func_12800_call = mod.get_global_var('func_12800')
func_12802_call = mutated_mod.get_global_var('func_12802')
call_15448 = relay.TupleGetItem(func_12800_call(), 0)
call_15449 = relay.TupleGetItem(func_12802_call(), 0)
func_12665_call = mod.get_global_var('func_12665')
func_12666_call = mutated_mod.get_global_var('func_12666')
call_15456 = func_12665_call()
call_15457 = func_12665_call()
func_12567_call = mod.get_global_var('func_12567')
func_12568_call = mutated_mod.get_global_var('func_12568')
call_15480 = relay.TupleGetItem(func_12567_call(), 0)
call_15481 = relay.TupleGetItem(func_12568_call(), 0)
output = relay.Tuple([call_15444,call_15448,call_15456,call_15480,])
output2 = relay.Tuple([call_15445,call_15449,call_15457,call_15481,])
func_15486 = relay.Function([], output)
mod['func_15486'] = func_15486
mod = relay.transform.InferType()(mod)
mutated_mod['func_15486'] = func_15486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15486_call = mutated_mod.get_global_var('func_15486')
call_15487 = func_15486_call()
output = call_15487
func_15488 = relay.Function([], output)
mutated_mod['func_15488'] = func_15488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14320_call = mod.get_global_var('func_14320')
func_14322_call = mutated_mod.get_global_var('func_14322')
call_15556 = func_14320_call()
call_15557 = func_14320_call()
func_14235_call = mod.get_global_var('func_14235')
func_14238_call = mutated_mod.get_global_var('func_14238')
var_15582 = relay.var("var_15582", dtype = "float64", shape = (250,))#candidate|15582|(250,)|var|float64
const_15583 = relay.const([2,-9,4,-9,3,-10,-6,10,1,-5,-2,-10,-8,8,-3,-7,-7,-1,2,-3,3,7,-2,-3,10,-2,9,-9,-4,-4,10,-1,10,5,-6,-1,2,10,5,-4,1,7,-7,6,-3,-8,6,7,-5,-9,1,-10,8,-6,5,-9,-4,-6,-3,2,-7,-9,2,-8,-10,-8,7,-5,-9,-7,9,-1,-4,-5,3,5,10,2,1,10,7,2,5,-10,-8,-9,4,-1,-8,5,4,3,3,-9,-5,4,7,9,-5,8,-5,10,8,-6,-6,10,-1,7,8,8,4,-9,-10,-3,-5,-8,-8,10,10,2,8,-7,7,-5,-9,-10,5,-4,-8,-1,7,-5,-10,1,-10,-5,7,9,5,8,-7,8,2,8,-10,4,10,6,-4,-7,2,-5,3,4,6,-3,2,6,5,3,4,-7,-7,-4,10,7,5,-2,4,6,7,6,5,3,-5,-7,6,-3,7,-5,-9,10,4,2,-5,1,-2,-1,-6,-6,1,-10,-9,1,8,-4,10,-3,-5,4,7,-10,-10,-5,5,9,-5,4,-10,2,3,-9,2,-9,10,5,-7,-6,7,-5,-3,8,-3,-3,-9,3,3,-7,5,-9,7,2,-10,3,2,-8,4,4,-10,10,-4,-3,4,-1,6,-6,4,9,8,1,-3,4,7,-3,-7,-8,4,7,3,-1,-7,-2,-4,-7,6,-2,-7,4,-8,-2,-10,7,4,-3,3,-6,10,-1,10,7,-6,-4,-9,8,5,-2,2,10,5,-3,-9,7,6,4,-8,3,-3,-8,5,-10,5,7,3,-1,3,5,2,1,-3,-3,7,-4,3,3,-7,-2,4,10,-9,6,-7,-3,-4,-5,9,-8,4,-9,6,-4,-4,5,-6,-5,-6,-8,-1,-9,5,-10,2,3,9,-2,3,-8,-4,4,8,6,10,4,-5,4,9,-6,-1,-8,2,-7,-9,1,8,7,5,-9,-9,4,-7,4,2,10,9,-6,-1,-6,-8,6,-2,-3,8,2,4,-1,-6,-1,-5,4,9,4,4,10,9,-1,1,-8,5,-6,9,2,-4,-6,1,4,-1,-10,10,-9,8,-10,4,-9,9,8,5,-3,-2,-10,8,-3,-4,-4,-4,3,-6,4,2,-1,-1,1,8,4,3,-2,-10,10,9,8,10,9,6,-6,-7,1,5,-3,-4,-4,3,-7,-3,4,-10,7,-6,6,10,-10,8,-4,-1,-7,-3,3,-6,-6,-5,1,5,-7,-6,10,-2,2,2,-4,-2,8,-1,1,1,-8,-10,-4,-9,-3,-2,1,-5,-6,9,-10,3,4,10,3,5,-8,2,-9,2,6,-6,2,9,10,9,7,-1,8,-8,-3,-2,-7,4,5,-7,4,9,-9,-3,6,-1,6,8,3,2,-9,8,1,2,-10,9,4,-9,8,-2,-5,-9,-6,4,-3,5,3,9,-7,-1,10,10,-10], dtype = "int8")#candidate|15583|(550,)|const|int8
call_15581 = relay.TupleGetItem(func_14235_call(relay.reshape(var_15582.astype('float64'), [250,]), relay.reshape(const_15583.astype('int8'), [550, 1]), ), 0)
call_15584 = relay.TupleGetItem(func_14238_call(relay.reshape(var_15582.astype('float64'), [250,]), relay.reshape(const_15583.astype('int8'), [550, 1]), ), 0)
func_12475_call = mod.get_global_var('func_12475')
func_12478_call = mutated_mod.get_global_var('func_12478')
call_15610 = func_12475_call(relay.reshape(call_15556.astype('float32'), [15, 9, 9]))
call_15611 = func_12475_call(relay.reshape(call_15556.astype('float32'), [15, 9, 9]))
output = relay.Tuple([call_15556,call_15581,var_15582,const_15583,call_15610,])
output2 = relay.Tuple([call_15557,call_15584,var_15582,const_15583,call_15611,])
func_15613 = relay.Function([var_15582,], output)
mod['func_15613'] = func_15613
mod = relay.transform.InferType()(mod)
var_15614 = relay.var("var_15614", dtype = "float64", shape = (250,))#candidate|15614|(250,)|var|float64
output = func_15613(var_15614)
func_15615 = relay.Function([var_15614], output)
mutated_mod['func_15615'] = func_15615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12870_call = mod.get_global_var('func_12870')
func_12871_call = mutated_mod.get_global_var('func_12871')
call_15687 = func_12870_call()
call_15688 = func_12870_call()
func_14320_call = mod.get_global_var('func_14320')
func_14322_call = mutated_mod.get_global_var('func_14322')
call_15689 = func_14320_call()
call_15690 = func_14320_call()
func_10945_call = mod.get_global_var('func_10945')
func_10946_call = mutated_mod.get_global_var('func_10946')
call_15696 = func_10945_call()
call_15697 = func_10945_call()
output = relay.Tuple([call_15687,call_15689,call_15696,])
output2 = relay.Tuple([call_15688,call_15690,call_15697,])
func_15709 = relay.Function([], output)
mod['func_15709'] = func_15709
mod = relay.transform.InferType()(mod)
mutated_mod['func_15709'] = func_15709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15709_call = mutated_mod.get_global_var('func_15709')
call_15710 = func_15709_call()
output = call_15710
func_15711 = relay.Function([], output)
mutated_mod['func_15711'] = func_15711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15709_call = mod.get_global_var('func_15709')
func_15711_call = mutated_mod.get_global_var('func_15711')
call_15801 = relay.TupleGetItem(func_15709_call(), 2)
call_15802 = relay.TupleGetItem(func_15711_call(), 2)
output = call_15801
output2 = call_15802
func_15823 = relay.Function([], output)
mod['func_15823'] = func_15823
mod = relay.transform.InferType()(mod)
mutated_mod['func_15823'] = func_15823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15823_call = mutated_mod.get_global_var('func_15823')
call_15824 = func_15823_call()
output = call_15824
func_15825 = relay.Function([], output)
mutated_mod['func_15825'] = func_15825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_15853 = func_10099_call()
call_15854 = func_10099_call()
output = relay.Tuple([call_15853,])
output2 = relay.Tuple([call_15854,])
func_15870 = relay.Function([], output)
mod['func_15870'] = func_15870
mod = relay.transform.InferType()(mod)
mutated_mod['func_15870'] = func_15870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15870_call = mutated_mod.get_global_var('func_15870')
call_15871 = func_15870_call()
output = call_15871
func_15872 = relay.Function([], output)
mutated_mod['func_15872'] = func_15872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13692_call = mod.get_global_var('func_13692')
func_13694_call = mutated_mod.get_global_var('func_13694')
call_15873 = relay.TupleGetItem(func_13692_call(), 0)
call_15874 = relay.TupleGetItem(func_13694_call(), 0)
func_12999_call = mod.get_global_var('func_12999')
func_13000_call = mutated_mod.get_global_var('func_13000')
call_15893 = func_12999_call()
call_15894 = func_12999_call()
var_15899 = relay.var("var_15899", dtype = "float32", shape = (65, 9))#candidate|15899|(65, 9)|var|float32
bop_15900 = relay.minimum(call_15873.astype('float32'), relay.reshape(var_15899.astype('float32'), relay.shape_of(call_15873))) # shape=(65, 9)
bop_15903 = relay.minimum(call_15874.astype('float32'), relay.reshape(var_15899.astype('float32'), relay.shape_of(call_15874))) # shape=(65, 9)
output = relay.Tuple([call_15893,bop_15900,])
output2 = relay.Tuple([call_15894,bop_15903,])
func_15905 = relay.Function([var_15899,], output)
mod['func_15905'] = func_15905
mod = relay.transform.InferType()(mod)
var_15906 = relay.var("var_15906", dtype = "float32", shape = (65, 9))#candidate|15906|(65, 9)|var|float32
output = func_15905(var_15906)
func_15907 = relay.Function([var_15906], output)
mutated_mod['func_15907'] = func_15907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12567_call = mod.get_global_var('func_12567')
func_12568_call = mutated_mod.get_global_var('func_12568')
call_15972 = relay.TupleGetItem(func_12567_call(), 0)
call_15973 = relay.TupleGetItem(func_12568_call(), 0)
func_12890_call = mod.get_global_var('func_12890')
func_12892_call = mutated_mod.get_global_var('func_12892')
call_16000 = relay.TupleGetItem(func_12890_call(), 0)
call_16001 = relay.TupleGetItem(func_12892_call(), 0)
func_12990_call = mod.get_global_var('func_12990')
func_12991_call = mutated_mod.get_global_var('func_12991')
call_16012 = relay.TupleGetItem(func_12990_call(), 1)
call_16013 = relay.TupleGetItem(func_12991_call(), 1)
func_11780_call = mod.get_global_var('func_11780')
func_11782_call = mutated_mod.get_global_var('func_11782')
call_16032 = relay.TupleGetItem(func_11780_call(), 0)
call_16033 = relay.TupleGetItem(func_11782_call(), 0)
func_5891_call = mod.get_global_var('func_5891')
func_5894_call = mutated_mod.get_global_var('func_5894')
var_16039 = relay.var("var_16039", dtype = "uint32", shape = (896,))#candidate|16039|(896,)|var|uint32
call_16038 = relay.TupleGetItem(func_5891_call(relay.reshape(var_16039.astype('uint32'), [14, 16, 4])), 0)
call_16040 = relay.TupleGetItem(func_5894_call(relay.reshape(var_16039.astype('uint32'), [14, 16, 4])), 0)
output = relay.Tuple([call_15972,call_16000,call_16012,call_16032,call_16038,var_16039,])
output2 = relay.Tuple([call_15973,call_16001,call_16013,call_16033,call_16040,var_16039,])
func_16050 = relay.Function([var_16039,], output)
mod['func_16050'] = func_16050
mod = relay.transform.InferType()(mod)
var_16051 = relay.var("var_16051", dtype = "uint32", shape = (896,))#candidate|16051|(896,)|var|uint32
output = func_16050(var_16051)
func_16052 = relay.Function([var_16051], output)
mutated_mod['func_16052'] = func_16052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10450_call = mod.get_global_var('func_10450')
func_10451_call = mutated_mod.get_global_var('func_10451')
call_16137 = func_10450_call()
call_16138 = func_10450_call()
output = relay.Tuple([call_16137,])
output2 = relay.Tuple([call_16138,])
func_16162 = relay.Function([], output)
mod['func_16162'] = func_16162
mod = relay.transform.InferType()(mod)
mutated_mod['func_16162'] = func_16162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16162_call = mutated_mod.get_global_var('func_16162')
call_16163 = func_16162_call()
output = call_16163
func_16164 = relay.Function([], output)
mutated_mod['func_16164'] = func_16164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_16186 = func_11738_call()
call_16187 = func_11738_call()
func_10879_call = mod.get_global_var('func_10879')
func_10882_call = mutated_mod.get_global_var('func_10882')
var_16190 = relay.var("var_16190", dtype = "uint32", shape = ())#candidate|16190|()|var|uint32
call_16189 = relay.TupleGetItem(func_10879_call(relay.reshape(var_16190.astype('uint32'), [])), 3)
call_16191 = relay.TupleGetItem(func_10882_call(relay.reshape(var_16190.astype('uint32'), [])), 3)
output = relay.Tuple([call_16186,call_16189,var_16190,])
output2 = relay.Tuple([call_16187,call_16191,var_16190,])
func_16230 = relay.Function([var_16190,], output)
mod['func_16230'] = func_16230
mod = relay.transform.InferType()(mod)
mutated_mod['func_16230'] = func_16230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16231 = relay.var("var_16231", dtype = "uint32", shape = ())#candidate|16231|()|var|uint32
func_16230_call = mutated_mod.get_global_var('func_16230')
call_16232 = func_16230_call(var_16231)
output = call_16232
func_16233 = relay.Function([var_16231], output)
mutated_mod['func_16233'] = func_16233
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16240 = relay.var("var_16240", dtype = "float64", shape = (15, 13, 15))#candidate|16240|(15, 13, 15)|var|float64
uop_16241 = relay.sin(var_16240.astype('float64')) # shape=(15, 13, 15)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_16243 = relay.TupleGetItem(func_10933_call(), 0)
call_16244 = relay.TupleGetItem(func_10935_call(), 0)
uop_16267 = relay.erf(var_16240.astype('float64')) # shape=(15, 13, 15)
output = relay.Tuple([uop_16241,call_16243,uop_16267,])
output2 = relay.Tuple([uop_16241,call_16244,uop_16267,])
func_16272 = relay.Function([var_16240,], output)
mod['func_16272'] = func_16272
mod = relay.transform.InferType()(mod)
var_16273 = relay.var("var_16273", dtype = "float64", shape = (15, 13, 15))#candidate|16273|(15, 13, 15)|var|float64
output = func_16272(var_16273)
func_16274 = relay.Function([var_16273], output)
mutated_mod['func_16274'] = func_16274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12890_call = mod.get_global_var('func_12890')
func_12892_call = mutated_mod.get_global_var('func_12892')
call_16276 = relay.TupleGetItem(func_12890_call(), 0)
call_16277 = relay.TupleGetItem(func_12892_call(), 0)
output = call_16276
output2 = call_16277
func_16298 = relay.Function([], output)
mod['func_16298'] = func_16298
mod = relay.transform.InferType()(mod)
mutated_mod['func_16298'] = func_16298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16298_call = mutated_mod.get_global_var('func_16298')
call_16299 = func_16298_call()
output = call_16299
func_16300 = relay.Function([], output)
mutated_mod['func_16300'] = func_16300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15129_call = mod.get_global_var('func_15129')
func_15131_call = mutated_mod.get_global_var('func_15131')
call_16301 = relay.TupleGetItem(func_15129_call(), 1)
call_16302 = relay.TupleGetItem(func_15131_call(), 1)
output = call_16301
output2 = call_16302
func_16303 = relay.Function([], output)
mod['func_16303'] = func_16303
mod = relay.transform.InferType()(mod)
mutated_mod['func_16303'] = func_16303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16303_call = mutated_mod.get_global_var('func_16303')
call_16304 = func_16303_call()
output = call_16304
func_16305 = relay.Function([], output)
mutated_mod['func_16305'] = func_16305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12870_call = mod.get_global_var('func_12870')
func_12871_call = mutated_mod.get_global_var('func_12871')
call_16371 = func_12870_call()
call_16372 = func_12870_call()
func_14462_call = mod.get_global_var('func_14462')
func_14466_call = mutated_mod.get_global_var('func_14466')
var_16374 = relay.var("var_16374", dtype = "int8", shape = (270,))#candidate|16374|(270,)|var|int8
const_16375 = relay.const([-10,6,-4,10,-4,-9,-10,8,9,-2,6,4,-9,7,5,-2,8,3,-8,-4,-7,1,4,-9,-3,-1,-5,7,3,5,9,-2,-7,10,10,-10,-9,-4,2,-5,4,-2,-10,-2,4,-10,7,9,-9,-9,-5,3,2,4,-1,-9,-4,4,1,-4,5,7,5], dtype = "uint32")#candidate|16375|(63,)|const|uint32
call_16373 = relay.TupleGetItem(func_14462_call(relay.reshape(var_16374.astype('int8'), [9, 5, 6]), relay.reshape(var_16374.astype('int8'), [9, 5, 6]), relay.reshape(const_16375.astype('uint32'), [63,]), ), 2)
call_16376 = relay.TupleGetItem(func_14466_call(relay.reshape(var_16374.astype('int8'), [9, 5, 6]), relay.reshape(var_16374.astype('int8'), [9, 5, 6]), relay.reshape(const_16375.astype('uint32'), [63,]), ), 2)
func_10241_call = mod.get_global_var('func_10241')
func_10243_call = mutated_mod.get_global_var('func_10243')
call_16377 = func_10241_call()
call_16378 = func_10241_call()
func_10348_call = mod.get_global_var('func_10348')
func_10352_call = mutated_mod.get_global_var('func_10352')
var_16384 = relay.var("var_16384", dtype = "float32", shape = (195, 3))#candidate|16384|(195, 3)|var|float32
call_16383 = relay.TupleGetItem(func_10348_call(relay.reshape(var_16384.astype('float32'), [13, 9, 5]), relay.reshape(var_16384.astype('float32'), [13, 9, 5]), relay.reshape(var_16384.astype('float32'), [13, 9, 5]), ), 1)
call_16385 = relay.TupleGetItem(func_10352_call(relay.reshape(var_16384.astype('float32'), [13, 9, 5]), relay.reshape(var_16384.astype('float32'), [13, 9, 5]), relay.reshape(var_16384.astype('float32'), [13, 9, 5]), ), 1)
func_2616_call = mod.get_global_var('func_2616')
func_2620_call = mutated_mod.get_global_var('func_2620')
const_16395 = relay.const([-9.251304,-2.343595,-3.040689,-5.647676,-9.379175,7.578456,-2.724874,6.106050,-2.699889,-0.603109,-8.120902,-4.263242,-3.385904,-2.772480,-6.304633,-8.573436,9.094371,-6.333948,-5.101736,-5.558955,-3.785124,-8.119276,-2.407481,-2.417776,8.932550,-6.184086,-6.224074,0.376204,4.128983,-9.396090,-0.836566,-4.755416,4.262760,6.448281,5.504928,-3.566348,5.920867,1.472079,4.086404,1.017893,-5.626857,-0.580406,-8.508501,-9.818949,3.795588,3.811706,0.713305,0.844713,-5.351038,-6.153524,8.907426,-8.601661,8.380727,-5.057994,2.459682,2.107769,0.243580,-1.490425,-0.414056,1.868550,5.147824,3.173745,-2.775416,-1.955920,1.590385,6.075100,8.980224,-1.677899,4.933916,5.419438,-5.543755,-4.245982,5.376697,4.776815,2.676850,2.568336,1.028226,-0.126989,-9.742566,-0.346298,0.643960,-3.641875,6.008548,-7.132872,4.776408,9.696667,-2.845853,-4.762380,-4.458291,2.998553,-1.093932,8.191896,4.624833,-1.110502,-5.301520,-2.866418,-1.958067,-3.739026,8.225784,-0.944145,2.030136,-4.794322,2.358849,8.384179,-4.017957,-8.251895,3.938641,-0.368339,5.898151,-8.806526,9.854041,3.713478,5.424270,-2.660583,-4.368500,-2.114898,-0.700212,-9.656289,0.623773,-0.660894,-7.345367,-0.235180,-8.843777,4.379548,0.802912,8.337196,-4.555829,-5.614338,-9.314383,-8.480051,8.903467,-8.353234,8.287315,-7.973312,-9.134908,-2.128849,7.006455,5.851642,2.520714,6.669969,-1.477753,3.952216,4.952526,4.345268,-3.126360,5.086390,-3.283472,-3.776166,-3.827042,-3.303416,6.627814,5.490602,4.810404,-2.711688,4.374590,-8.899707,-2.023217,-7.340147,6.583125,0.649981,2.772742,-2.581015,3.268255,6.805588,4.590800,-2.175180,-8.837887,5.219350,-7.975331,-5.834300,7.399444,-8.905174,7.184237,2.613316,-6.004781,-3.778090,5.490381,0.889503,9.690214,-5.371843,-8.137107,3.510640,2.982559,-0.501574,-6.723565,2.568225,9.703237,5.345138,8.617834,-1.250959,-9.161809,8.261798,8.632698,-2.473493,-2.594232,9.920981,7.024946,6.110988,8.945859,8.984077,3.820848,9.869886,-9.726509,8.581964,6.162562,3.374110,-9.463168,-3.214070,6.729408,9.953133,9.938358,-4.704832,9.734864,4.779752,4.387965,3.509902,-1.372105,-6.127371,8.349833,-1.298429,1.823173,-8.655553,-8.716369,0.745027,4.839676,2.492757,2.300251,-0.912183,-4.974440,9.220506,-4.344766,-6.199550,8.886951,3.455243,-8.723580,8.200157,1.141325,4.380960,-8.346130,1.391932,2.931143,2.071719,-1.090994,-8.848560,8.840248,-3.805631,-0.786856,-8.218041,7.447487,-2.846329,6.938232,2.678338,-3.917858,8.991022,9.969256,-4.010417,3.622470,0.237300,8.341441,-4.845903,6.394640,-6.856620,0.013489,0.910184,-7.834220,-6.021808,-6.104546,-7.492426,0.867740,5.384832,-3.069708,0.504568,3.643652,6.839194,-2.411391,-6.901818,1.861041,8.152888,6.916916,2.126600,9.756144,-9.683496,-6.474654,-4.553656,-8.370305,-8.555746,2.913262,-9.971009,0.904487,-9.426333,-1.468433,3.565586,9.330879,-4.096255,-1.669515,7.372946,-7.184797,8.306438,-6.840845,-4.617093,5.724555,-9.594492,-1.916283,-3.282230,-1.690638,-2.199913,4.759834,-5.860427,-8.531800,1.607910,2.636448,-5.321759,-7.803444,-1.974512,1.192991,1.715290,5.737337,-7.677305,5.024207,6.209760,8.162891,-8.699290,-4.880719,3.336558,9.542141,6.766226,2.097965,-0.226121,7.552198,0.253235,4.896186,0.993459,-9.513484,7.264725,-9.330582,5.955655,-5.814814,-3.370742,4.083092,7.877975,0.257287,8.302023,5.153185,-2.933900,-8.831855,0.947785,1.599751,-5.496907,-7.971684,2.155226,9.808381,-6.462946,-2.582109,-3.628003,9.771565,-3.652134,-9.216124,6.359123,-9.602915,-5.831777,4.122991,-0.652084,-8.664020,-3.801521,-2.330737,-4.595896,4.261700,1.544457,2.266735,0.225522,-2.385002,6.434722,8.935440,-4.401188,0.281314,-6.785630,-2.920128,3.341346,4.752638,-7.170675,7.690211,0.912945,6.665064,-7.749967,-3.143329,1.192657,7.172472,5.049234,-6.983021,-8.663725,-0.168030,-2.082544,-0.595968,-3.368537,-4.726079,9.860824,5.727749,-5.346135,-2.921993,4.336032,-9.591448,4.140440,-5.614333,-0.467609,-1.325802,-9.799921,2.843820,9.527178,-5.038127,6.748027,-8.864423,-0.352171,-0.987537,9.911437,5.934186,6.990328,1.049641,6.597071,-8.611118,-4.532203,5.370355,6.980811,-3.918031,-0.880363,-6.284123,8.128675,-7.593360,-9.798180,-7.114586,6.300198,9.144147,8.849194,7.660233,-3.675391,-3.690758,-1.417081,4.775634,-9.149391,9.674804,-5.322530,-9.441037,-1.529821,9.699399,8.467277,-1.237900,3.237007,-5.936371,5.636624,3.465254,8.645066,-1.134928,3.976250,8.408557,5.178744,-9.132370,6.206304,3.905155,-6.154122,-1.052983,-4.332532,-4.301045,-8.215599,-0.966199,3.625407,8.813805,8.520988,-3.867299,1.290274,-2.008602,-6.123990,-9.880254,-9.509754,-3.368511,-2.905108,-0.800886,9.337183,-6.285901,7.696431,1.069965,4.339548,9.773216,9.809530,5.934445,-9.461908,3.591552,5.936084,-5.643159,-0.328530,-7.134592,6.387195,9.353811,2.234454,3.969506,7.956716,7.362515,9.515737,4.034904,2.606519,-0.053868,3.263088,-6.794351,4.214689,-6.529248,8.477200,3.873329,3.288428,-2.792284,-3.952384,-0.397785,-6.205722,-8.239052,-2.897086,-9.106251,0.629852,8.652597,8.604214,8.991174,-0.641375,-3.899057,-0.079817,9.761680,-3.207597,-5.466560,1.642596,-2.198149,0.018466,0.681838,0.122112,5.246288,-9.304297,5.358072,-2.871387,0.042208,-0.568546,0.600504,5.277233,-6.142045,-2.173275,-8.126492,6.060628,6.893839,-2.701923,1.127312,1.712041,-0.218075,4.804517,9.316410,-0.158795,3.760046,-6.392290,3.504260,4.151903,9.337479,-5.974085,3.710184,8.935342,-4.447041,4.691585,8.742194,-7.012506,4.839202,8.960144,-8.617945,2.093677,-4.019165,-0.346458,1.700068,4.695338,6.577030,-3.197301,-0.950937,0.842656,9.951839,-3.584638,7.202529,-3.525344,-0.497600,6.926985,3.981838,-3.256954,-8.616041,5.829941,-7.736724,5.191911,4.604122,-2.417343,8.438940,-0.074073,9.227981,4.493672,-7.839663,9.611663,4.885278,6.041041,0.075037,-5.545362,-2.596196,0.070270,-9.704465,-0.048828,-6.103700,6.540884,-8.113774,9.807789,-0.495623,6.098256,-2.570343,-5.431742,0.354319,6.307636,5.579863,0.372362,9.693659,7.763624,4.953639,3.648922,-6.841605,0.558288,8.770061,-8.872045,0.865043,-0.524733,-2.063425,7.750364,-1.367637,-1.733293,-3.863077,8.172812,-5.133430,2.224205,-0.457985,-6.437533,-3.466060,8.623832,-4.222738,4.662164,9.007289,8.684970,-5.213819,-8.637633,5.071996,0.587821,-8.053801,-1.478805,1.410829,-8.375387,-3.353142,-4.387509,-1.725201,-2.737574,-8.868036,-8.802666,1.320139,3.704403,-7.608522,-0.080209,1.925310,4.646044,-6.177701,-5.197255,5.417388,6.417083,5.032732,-4.565591,-1.394292,-4.387275,3.143322,-3.032202,7.644697,-3.355215,8.014616,1.240654,-7.952762,-0.887585,-2.182035,-9.289613,6.964628,-4.883030,-7.326318,-8.578030,9.036076,0.959695,9.597503,-6.991027,3.566476,-4.908297,7.838008,7.712226,-3.979520,5.917922,5.540011,1.261195,1.838420,2.093542,-0.165374,-8.342518,9.281367,-4.251477,-9.398344,0.809818,-7.288918,-5.661493,7.113352,8.236611,-6.853881,6.789761,2.439892,-1.256588,-9.249415,-5.456685,-3.597288,-4.552365,-4.426872,-5.430976,5.533146,-1.149380,-9.143693,-6.671690,9.933646,3.093269,-4.371036,1.570720,9.892801,-6.131590,1.923404,4.396802,-4.345499,6.355964,-5.371273,5.187404,1.350507,5.327517,-1.280984,-9.751332,-6.893631,5.460991,-8.399025,-3.937857,1.692053,6.028715,9.913630,-5.738541,-7.551415,-3.043106,4.366790,0.302698,9.555358,-6.460895,-6.000299,8.073979,3.534243,4.208507,9.246736,3.445407,-5.335049,-3.768550,7.541662,6.057880,-9.507145,2.242847,5.083965,4.492133,3.846842,2.821392,-2.877652,-2.528750,7.041122,6.160896,9.265125,8.951446,9.109564,1.016545,-3.070762,-4.220965,-2.959662,0.040215,-2.814607,5.267385,-3.221192,2.526615,1.977108,-4.806184,4.047939,-8.249515,8.918674,0.398892,2.348320,1.372014,4.632834,-7.736721,5.184449,-9.443132,-4.536793,-8.052300,-8.134617,5.797310,3.215504,-4.614934,7.940293,-0.518481,8.210705,2.619334,-1.825092,-3.823222,1.498482,-3.170518,-7.678784,-5.493665,-0.146427,-8.551956,2.365259,-4.841486,1.855892,2.416039,8.150681,4.397313,2.347829,6.094045,-9.005580,-7.799596,1.647650,-4.505873,7.940993,-3.591395,8.663090,-0.107410,9.466802,-2.061473,7.510662,4.667402,8.444553,3.994550,-3.722917,-7.967913,3.546464,-9.330493,8.249281,-1.838673,1.072179,-8.130651,5.432949,1.766532,-3.438249,-3.138915,-4.878410,-2.194448,-8.235965,-2.586085,0.469700,0.340608,7.112815,7.966951,5.732657,6.134103,-4.913111,1.510002,-2.855821,-6.936635,-7.912289,3.043333,4.502103,-5.942458,9.850889,-7.635990,-1.010996,6.554580,7.489974,-7.139703,7.181993,5.391856,-3.814511,9.844382,-8.733212,1.978643,-7.449559,7.861255,-1.453258,-4.485082,-5.957804,-4.745471,-6.213536,0.740058,-8.778843,-5.794898,2.545065,-8.507168,3.325467,5.843322,1.632194,-7.278835,7.059194,4.045865,-9.744525,1.738768,-5.033497,6.302824,-1.072880,-7.812823,-1.668817,-7.673267,9.731011,6.402845,-5.271375,-7.866153,7.054234,-9.746563,-4.343949,8.618791,0.737389,5.353930,-5.463901,-1.570447,6.951938,-1.445606,-6.604390,-2.616296,6.137791,-0.120802,-6.567955,7.321938,3.467797,-7.003744,-4.168956,-3.343678,-7.449756,6.283080,-0.959675,7.318232,2.953455,-7.223124,-8.148908,5.322082,-0.165926,-9.097398,-7.833356,4.448363,7.302731,4.086906,7.845356,3.322565,6.181751,-4.299692,-2.338362,-9.738143,1.399659,6.460142,5.632210,9.526328,-9.364732,-6.195717,-3.549008,6.371893,7.831683,4.614750,-1.719334,-2.114783,3.226508,-4.461560,1.389267,4.697001,1.246475,-4.807352,4.977637,-1.550050,8.769153,-9.889918,-7.244526,5.165870,-0.420157,-1.345702,8.780494,3.263276,-9.313877,0.330692,-0.103347,-4.398234,7.467001,-8.840686,3.810403,2.451899,1.238655,-5.611622,8.178630,1.089121,-9.538430,-2.510343,-3.369153,-3.250861,3.797741,-0.709103,2.518459,3.317015,-8.542320,5.954305,1.792997,-1.931954,0.786254,-8.460839,2.107754,-2.129535,-1.273194,5.127524,-1.505347,4.517384,8.260513,9.964321,-5.601751,-8.262743,-6.120113,-2.858163,-5.272736,-2.981708,3.419550,-7.789212,-1.140195,-4.739652,2.892547,-3.030078,-8.235729,-3.798499,4.900255,-8.596253,-0.920495,-5.270704,-8.694752,-1.753321,-3.042955,-3.096203,-4.237329,-0.787467,-2.955105,6.337797,-4.723760,4.854307,0.382131,9.510849,-2.768418,-2.295298,-4.825409,6.570911,-0.947979,5.910102,7.779998,-6.973001,-3.117064,-1.568666,-8.430529,-2.851719,8.740269,9.452655,3.979886,-9.309945,-1.404623,7.920509,3.094168,4.488284,-9.366111,-2.145292,4.325861,4.171427,1.174632,-2.481924,9.042199,6.151083,-6.140397,2.827263,8.377892,6.508965,6.818524,-3.064433,-2.021869,-6.886249,-3.280067,-7.080041,2.664351,7.986694,0.227100,-1.844913,-1.684038,-4.597749,-4.090386,0.152153,5.460917,9.314424,1.595190,7.227793,-2.595765,-4.281855,1.602938,-4.229550,7.424929,2.849144,6.252406,0.597187,5.465033,-9.415723,-3.935495,4.829952,1.852059,-5.602658,-4.912238,-8.655191,3.982374,9.437935,5.926094,5.840282,7.300569,5.100599,3.525563,0.798592,-3.587752,-9.690584,8.800768,-1.275571,3.001270,2.820270,3.001109,-7.483728,-8.552746,8.457247,4.418905,-5.005115,7.899939,4.921422,0.737437,-5.318711,-2.250923,-3.116718,-8.671591,-0.370406,6.511815,-3.179663,3.144035,4.037006,-5.405816,4.757426,3.617155,1.999964,-3.120477,1.854038,4.886056,0.958055,6.837777,6.386877,8.792146,2.838344,3.749804,9.937159,-4.677819,-7.344460,3.851129,-3.316323,-0.720496,5.055852,-3.627769,-5.604167,-2.235976,6.757541,8.260751,-7.695670,1.155532,9.188171,3.922854,2.544077,5.371447,-5.840626,-8.100557,5.712657,-5.145369,1.186012,-9.381605,-5.036322,0.200510,-3.471890,-4.469154,9.122157,-3.431254,-7.423379,2.108059,1.774579,-4.402262,6.755841,-1.842658,3.787765,-8.279443,0.319777,-8.659474,4.167277,9.083937,-6.609046,-5.364585,4.818323,-1.595193,-2.819576,-4.449574,-9.087310,-3.694980,9.555845,-2.424364,3.815502,5.696648,1.059160,3.014068,1.321260,-1.725794,-8.540932,-0.964913,4.838580,-3.926798,-2.506867,8.937170,0.343652,3.854727,-5.231856,4.629880,-9.790655,-4.462214,-1.629222,-4.680665,5.691298,6.012879,-2.137861,7.812982,-4.070233,0.345867,-9.073158,4.655982,-7.815043,-1.785019,-0.301689,5.131893,-5.933575,5.740621,8.045251,6.161416,-9.572733,-3.996565,-7.074052,4.038138,8.398524,8.305849,1.503178,7.874501,2.438529,5.594284,4.597693,-0.135108,-7.541863,-6.419319,-6.869625,-1.531648,-9.010021,3.241079,9.698754,6.060975,3.823182,-0.471622,0.974040,0.394249,-4.694562,3.499338,3.637323,4.925276,2.190594,0.942924,1.053649,-0.391025,-9.014659,-6.135377,-7.696891,1.388880,2.477203,4.656001,5.494424,8.173901,5.369983,-8.936906,6.969853,-3.375979,0.451237,-3.634014,-3.594746,8.084302,-0.433341,-8.793391,0.987580,-8.081334,1.187923,-9.202543,-0.486981,-2.081498,-5.851901,-4.072202,3.763753,-9.651502,-7.465530,1.572310,9.818309,-3.909629,1.294950,9.532240,-1.264236,2.691272,3.303548,-0.769226,7.387242,9.339109,3.227580,1.859261,-4.942364,-1.496476,-6.523466,5.246334,-7.362943,8.484402,-0.957147,-1.584233,7.723850,1.942711,6.819161,-8.079469,-4.330585,-5.263396,-9.686319,-9.510404,1.056486,7.257435,2.814637,-3.118501,-4.021087,7.589684,-2.898228,8.061905,8.008013,-6.527330,2.741623,4.720941,-9.140095,6.755866,-3.018376,7.944018,-5.563236,1.344427,-6.430657,1.859998,-9.388878,2.134613,2.682303,-9.860707,1.469038,3.779718,0.072019,5.797929,9.518786,-7.827356,-9.167028,2.868876,6.010786,-3.900787,-2.868265,-0.602585,-3.457409,1.978824,3.741747,-7.043654,-8.038385,3.210288,5.876235,9.576256,7.024437,-6.940856,-8.476445,5.131963,-2.176175,4.400809,6.524178,7.193159,5.012021,6.504839,-5.807937,-6.181007,-3.683029,2.094899,-8.363334,-1.644921,-0.143801,1.765943,-7.818667,-2.016570,5.541317,-5.066306,-2.146968,-6.445574,-5.487745,-3.204086,-3.327381,-0.073646,-9.172873,-8.129980,-8.078596,-4.537222,8.204731,7.156788,-6.247372,-4.800055,0.903111,4.189187,0.391515,-7.203781,4.971687,-7.081879,7.240992,-4.701856,-3.701913,-6.641424,5.122809,-2.786627,-1.178237,9.783108,0.569972,-8.591474,-5.328391,-4.324215,-5.377695,9.459248,6.043326,6.126317,-8.413751,-0.718550,-9.015942,-8.465954,-9.149858,-1.179168,-6.026736,3.537416,6.548632,8.555782,0.317710,3.261729,-1.409308,-8.142997,0.950451,-2.670124,6.665607,-7.732236,8.464057,-5.930312,8.586721,-6.085943,-2.513711,-3.961603,-7.591213,1.252442,9.851640,5.050346,9.906744,-0.905354,1.268772,7.101085,2.199325,-1.796551,-1.604435,-9.629718,3.980455,5.022097,2.529452,4.388427,2.977107,1.865210,-5.120343,-1.199750,-5.268382,-2.093863,0.182113,1.326859,8.055264,7.362491,-4.093568,-5.338683,2.432640,5.490334,4.143095,-4.548597,0.542670,7.087825,-0.702470,9.165470,-4.634960,-4.848098,6.795809,0.278043,0.001950,-0.109394,-3.314713,9.469563,5.466026,-7.878866,1.156338,1.459287,9.011109,-2.829063,1.289015,-4.219010,4.198873,9.208058,-4.843960,-9.763671,-9.650914,8.468927,5.474281,-1.452972,1.677474,6.907696,4.400370,1.740612,2.448064,-0.409399,-9.977117,9.776679,6.998156,-9.619096,4.485603,1.090491,-3.537316,-8.260039,2.659249,-8.609221,-8.000092,9.218798,-8.633484,-7.967800,5.802698,-2.357794,5.303213,8.399847,6.385676,0.117023,-0.563335,-2.953837,2.340445,-2.323373,0.192352,-6.896929,-5.635954,5.844038,-9.833795,6.988219,-7.095933,1.428987,0.737280,-9.814367,2.997572,7.693891,-3.792964,-6.700961,-1.503110,-1.865751,7.471509,3.690463,-1.365122,-5.261606,-8.945571,-4.230245,-4.737125,2.516255,8.623446,-3.567150,8.699612,-6.765551,4.819372,5.352663,-5.480089,0.810471,-2.978207,9.916765,3.597060,-2.664953,4.663299,-1.904764,-5.971379,1.387168,9.310739,-5.126889,2.327650,-0.168301,5.185478,8.909013,0.362348,4.392994,2.484497,-9.108434,2.084410,2.421901,-6.781366,-3.632247,3.361403,-0.497447,2.352544,3.852806,0.037818,7.005357,8.301826,-5.008603,5.688266,1.993486,6.715189,4.905061,-1.528007,2.256940,-8.252203,2.091682,-0.450138,-3.675848,0.953139,-8.239495,3.189917,4.318094,-6.747355,3.576364,-6.376551,9.923208,-3.857542,-6.573456,8.041547,3.761994,5.510868,4.365415,-5.944770,1.015187,5.856306,6.037448,6.010614,7.597855,-2.692764,9.256815,3.064995,-2.671434,3.611860,-4.791693,6.590190,-3.568736,4.364751,-2.258399,2.117357,6.116619,1.871605,4.035575,6.186112,5.987304,7.193112,-8.694228,3.886037,-9.981388,1.947928,0.209508,9.036868,6.540653,1.085815,-8.998717,3.101524,0.928151,-2.719992,4.886645,0.885556,-1.643017,9.674351,-8.666090,3.890076,9.242103,7.774923,6.473686,-2.975728,2.315343,-4.591342,-0.197042,8.750129,1.022404,-9.151738,-5.683406,3.759133,-1.555106,6.216858,6.636367,-0.241997,-8.011361,9.137803,-5.684998,-4.916291,2.313313,1.734277,4.404834,5.976095,5.356506,3.474636,6.707572,-7.921741,-1.035745,-2.153855,-8.141896,-5.622571,2.645538,9.951800,-8.602597,6.419347,-5.335670,8.709735,-7.818599,-4.438003,6.036120,7.979137,-3.991368,-4.167670,3.076029,-6.642171,3.846219,-6.922998,-5.932973,-4.889057,-5.371388,-6.113410,1.859210,-5.837780,-0.754642,2.473350,-0.555271,2.258479,-0.896109,3.922118,-5.820107,1.268863,6.533279,-3.275395,7.543291,-5.912172,3.439788,5.230303,-2.057205,-7.021997,-4.692886,-3.096318,-6.047545,-0.041051,-1.419293,-7.217480,8.254450,-7.333617,-6.920216,1.882838,-2.386720,1.544608,-4.081059,-7.062848,-7.807326,-2.841356,-1.119065,3.740166,-5.749160,9.398170,-8.839551,4.022946,1.023834,-7.266997,7.323203,-9.235992,3.537956,2.246138,-9.793858,-9.579239,-9.907861,9.792061,-6.166707,5.238959,-9.194145,3.288373,-8.696689,0.617223,-2.711207,0.495132,2.513531,7.963189,1.142264,-3.950275,-0.413579,-4.029524,5.606548,2.143297,8.021701,-9.861915,1.799755,-7.132936,4.331678,-1.015949,5.259649,5.163425,1.994228,6.636653,6.450438,-4.828723,-4.907757,-8.355920,-1.886359,8.219926,-5.099316,-9.320462,9.606112,6.169654,-7.077647,6.673656,-1.989825,-9.854404,8.647391,-1.100607,6.798443,1.872139,-5.819423,-4.903364,5.077082,-4.212789,2.195041,-7.323461,0.811776,0.832507,2.873937,0.192479,7.756416,5.082230,3.444908,7.289854,-2.252348,-2.632778,-2.662792,2.268123,3.564540,3.144103,-7.674912,4.364675,-0.128410,5.952736,1.594694,9.966811,-3.111057,-4.002572,-9.365991,4.846508,-9.254139,3.333413,-6.809866,-5.907830,-4.429234,-9.112952,5.007274,-8.968164,7.889868,8.728641,-6.752423,4.636147,3.262081,-6.603470,-5.181453,-3.472043,-7.642536,0.531168,1.832334,-1.739861,-4.169598,-8.814467,-0.738725,3.054374,3.188622,0.273777,9.164467,-2.548957,-2.041038,-5.633788,-4.493555,9.855610,2.531566,7.357491,-4.450080,-0.467755,3.035376,3.761168,-6.095864,3.524189,9.880087,2.583860,6.451651,-5.275294,5.324568,-9.709029,6.192013,-8.251963,8.328405,9.738864,7.048179,-7.604830,1.787633,-6.601175,-2.385492,9.354947,-4.582789,-7.058003,-5.064099,0.350370,8.717903,-6.749354,6.151642,9.227828,-3.639195,2.302365,5.809691,-9.961502,4.687638,-3.085311,-0.634857,9.506463,-6.126800,3.932565,-6.997191,-4.803066,-1.960653,8.628723,9.270505,-6.611161,1.807185,4.373752,0.937821,5.534034,2.475883,-7.010592,7.735463,-6.617084,7.238056,6.287902,2.115874,-8.144025,-8.128466,3.598933,-4.883321,3.788854,7.849563,-2.890371,4.965582,5.581938,5.575135,-5.881833,-5.532743,5.771608,-3.934105,0.999761,-1.415673,-2.061783,8.699823,0.627315,2.197821,-7.001162,4.369299,-3.276601,-1.575097,6.174076,0.202653,7.215927,1.852911,-8.265256,6.107212,3.589006,3.030266,-0.789400,0.201401,-4.751278,-0.080701,-1.971409,-5.603660,-4.358372,-7.908646,-1.983648,-2.342093,4.786316,-0.886607,0.702971,-8.132445,-4.921305,-3.039876,-8.565146,-1.479147,2.342881,2.177771,-3.609557,-4.464987,4.689527,6.129864,-5.407051,3.992566,8.756884,8.593381,1.562099,9.933896,5.443904,-0.692564,3.329924,1.987545,1.389807,-1.376811,-6.226943,3.554449,-6.219506,2.465424,-6.415997,-5.058099,5.415488,-5.451687,2.652986,-9.935402,-1.291667,2.817596,0.209606,-9.784153,0.152623,-4.147581,0.634428,4.638927,-0.390472,-4.326227,9.077440,-4.990879,8.365611,2.695669,-3.740251,4.860041,-8.956765,2.038113,0.503873,5.113165,-8.532390,-8.823049,2.704470,4.583430,8.573363,-1.417580,5.339012,4.523920,1.398104,5.951074,-2.032911,-1.827077,4.638669,-1.796257,6.838686,-4.548640,4.068899,9.839697,-4.767374,2.245388,0.335042,0.287456,-7.127646,4.988015,6.426428,-9.323915,2.520524,9.490729,-5.090042,-2.332389,1.555356,8.332696,6.909345,1.762532,-1.225623,4.324013,-9.455503,-8.097560,5.522211,-8.786538,-7.824018,-2.863796,-8.348847,8.859754,4.780874,-7.346977,-8.725044,-9.449342,9.636160,7.780362,-1.953442,0.577208,9.254799,2.429366,7.200992,-5.462840,-8.375766,2.733065,-9.129697,2.550485,-7.269727,-9.234931,-9.908920,5.887275,-9.070846,6.522557,6.552475,7.829749,-1.491043,-0.787367,-9.360514,0.406379,1.437837,4.227090,0.392648,-0.561169,6.590623,-3.871728,5.323929,0.902987,0.772195,-3.205791,3.777544,2.627520,-6.620949,5.164965,-2.357816,-5.777706,4.403915,2.095358,-5.133706,8.300251,-9.959220,8.350187,6.846392,0.711915,0.222034,8.648594,4.230113,-0.052744,-1.978543,2.694820,2.487600,1.386636,0.653640,7.350070,-6.233195,6.168904,5.295541,-0.230411,1.566410,3.710979,2.503596,7.001816,2.402006,-5.406609,1.737447,2.014423,7.110406,-9.665003,4.600336,7.223679,-5.880553,1.158389,3.143768,-0.522643,9.225187,-0.562949,-0.436973,-4.013251,4.009466,-8.896629,-7.577890,6.589600,-2.312331,-1.896823,-5.996560,8.466074,1.392338,-8.425287,-9.200644,4.587552,-7.993836,-1.013871,-6.410391,-2.570796,6.401753,-8.661189,-6.829969,-4.045472,1.588178,7.223129,-1.247279,-9.852372,1.753137,-5.083040,5.373221,5.769368,3.460914,0.111628,-2.186997,-4.698816,-8.661282,3.450258,-7.226338,9.664881,9.468106,0.314174,2.635714,5.095380,-1.828852,-4.248461,4.461985,8.636418,6.219308,-7.853994,2.909335,8.232795,-3.381537,-1.993761,-8.904054,-7.975935,-2.658109,4.140945,-3.065060,-6.843292,5.111501,-4.301786,1.535986,1.602199,-6.243286,-2.465692,-1.651391,3.428665,7.556875,-7.941659,1.647771,8.663637,-7.800876,0.988732,5.880442,-7.678120,-1.151672,7.797653,-6.377225,-9.593429,1.995032,-8.797557,9.276150,-7.990589,-7.586034,-0.764995,6.614727,0.445990,0.192722,-1.631976,4.793942,2.537278,-9.856865,0.490081,1.709536,5.918264,-7.141997,4.640079,-4.203667,-3.622276,-7.244875,-5.458827,-5.728437,6.145607,4.712066,-2.146661,-7.645345,-2.718018,1.220767,-8.835568,-4.924223,4.789138,3.285150,-4.024253,-5.752858,-6.605377,9.699336,-1.667543,6.004351,8.975338,-3.459492,1.239697,0.003175,2.083981,5.653763,-4.586838,1.678951,-5.330639,-7.688583,-5.548541,-7.751390,6.226497,-7.750754,0.128750,4.299933,-5.955272,0.841407,5.241597,8.532273,9.293568,-1.031381,-7.031014,6.251298,-6.508236,1.510820,-5.231889,-2.384526,-7.492062,0.607775,-7.625115,-3.431172,-2.185762,-0.075358,2.169500,-6.166261,-1.788456,-0.592475,9.323309,2.269499,2.654480,-8.716812,-2.934239,0.876741,3.806861,6.289234,6.184261,-0.149807,0.372861,8.040530,4.161797,4.656649,-9.557055,-3.797436,0.683077,-6.741223,3.638796,-1.648486,6.238515,-8.932155,-1.801218,-6.371924,2.283573,-7.970842,8.679453,7.068576,1.377684,-4.652715,-8.941702,9.938558,-5.745628,-3.134534,4.913210,-5.764097,-5.670108,1.077906,-3.439924,1.143900,0.855804,-5.456971,2.185259,5.265496,-6.363605,8.469743,-1.523130,-7.732450,-5.460994,-5.116257,8.970242,-0.136034,3.979006,-1.386919,5.414966,-7.565005,1.522326,9.474657,-5.338639,-4.707472,-3.887193,-6.988275,-9.122749,8.211755,1.259129,-5.918531,-1.641977,0.404230,0.280636,8.589276,5.608916,0.067683,-0.893810,6.436893,7.850457,9.118051,7.479012,-0.040560,-1.221248,-9.387008,-4.278924,-9.334367,0.219292,-9.999524], dtype = "float32")#candidate|16395|(2400,)|const|float32
call_16394 = relay.TupleGetItem(func_2616_call(relay.reshape(const_16395.astype('float32'), [10, 15, 16]), relay.reshape(const_16395.astype('float32'), [10, 15, 16]), ), 0)
call_16396 = relay.TupleGetItem(func_2620_call(relay.reshape(const_16395.astype('float32'), [10, 15, 16]), relay.reshape(const_16395.astype('float32'), [10, 15, 16]), ), 0)
uop_16397 = relay.sigmoid(var_16384.astype('float64')) # shape=(195, 3)
uop_16404 = relay.acosh(uop_16397.astype('float64')) # shape=(195, 3)
func_6813_call = mod.get_global_var('func_6813')
func_6816_call = mutated_mod.get_global_var('func_6816')
var_16410 = relay.var("var_16410", dtype = "float64", shape = (250,))#candidate|16410|(250,)|var|float64
const_16411 = relay.const([[1],[-10],[5],[9],[-2],[6],[-9],[-9],[-1],[-2],[6],[-3],[-1],[-5],[-8],[-9],[-5],[8],[-2],[-8],[9],[-10],[-2],[-5],[-1],[-3],[4],[-9],[2],[-3],[5],[7],[-1],[-9],[-4],[-1],[2],[-1],[10],[7],[-7],[-6],[8],[-6],[-1],[1],[1],[7],[-5],[-6],[5],[1],[-9],[-10],[-2],[-2],[-1],[8],[6],[-10],[-4],[-3],[8],[-8],[-6],[1],[-4],[-7],[-9],[-3],[7],[-8],[4],[8],[1],[-6],[-10],[10],[9],[-3],[4],[4],[-10],[-10],[1],[-8],[7],[-7],[-3],[2],[4],[8],[7],[3],[8],[10],[-10],[10],[7],[-9],[-1],[9],[2],[-2],[10],[8],[2],[-7],[8],[4],[6],[7],[-8],[7],[5],[6],[-10],[6],[10],[6],[2],[5],[2],[2],[3],[-5],[9],[6],[9],[7],[-9],[1],[-7],[-5],[5],[-8],[-7],[-2],[6],[-10],[-9],[10],[9],[7],[1],[-1],[6],[-2],[-1],[1],[-8],[4],[5],[-6],[-9],[2],[1],[7],[-7],[-9],[8],[-1],[-4],[-9],[-9],[10],[3],[-7],[-1],[9],[-9],[-7],[10],[2],[8],[-8],[-1],[-1],[1],[9],[-2],[1],[4],[-2],[-9],[4],[-2],[10],[-3],[-1],[-4],[-5],[9],[2],[-8],[2],[-10],[3],[-1],[9],[-6],[9],[4],[-1],[-4],[7],[-3],[-2],[10],[2],[5],[-6],[-7],[10],[-6],[1],[4],[1],[9],[-4],[-4],[10],[-3],[2],[8],[-1],[-8],[-7],[8],[6],[-8],[5],[4],[9],[-7],[8],[-4],[-3],[-5],[-10],[8],[6],[-10],[2],[2],[-9],[2],[-4],[1],[-4],[8],[2],[-2],[-1],[-9],[-10],[4],[-5],[-10],[-10],[5],[-7],[-5],[-5],[-8],[-5],[-1],[-10],[-5],[2],[4],[2],[-9],[-2],[-2],[-3],[6],[-3],[-3],[-7],[5],[9],[10],[-1],[-2],[8],[-4],[-4],[7],[-1],[-2],[5],[-6],[-9],[7],[4],[-8],[8],[-2],[-5],[-1],[-10],[3],[-7],[4],[9],[-4],[-4],[-5],[3],[-10],[3],[-10],[8],[-1],[6],[-7],[-8],[-2],[3],[5],[-2],[6],[-1],[-10],[2],[3],[-8],[8],[5],[-10],[-1],[7],[7],[4],[-5],[-2],[8],[-2],[1],[-5],[-4],[8],[-1],[7],[-4],[-7],[3],[-4],[-3],[-8],[7],[-3],[8],[-4],[-1],[-1],[9],[-6],[-6],[6],[-9],[-6],[-7],[3],[-9],[6],[1],[-1],[-9],[9],[5],[-5],[-9],[-7],[-4],[-4],[-8],[-5],[3],[4],[-9],[9],[2],[-10],[-6],[2],[-8],[8],[-8],[2],[-7],[-6],[9],[9],[9],[5],[4],[9],[-6],[8],[7],[3],[-9],[-3],[-3],[-2],[1],[7],[-1],[-3],[10],[10],[4],[1],[-8],[9],[-2],[-1],[3],[-9],[-8],[9],[9],[1],[-2],[10],[-4],[5],[2],[5],[-8],[-7],[9],[1],[-3],[8],[-1],[3],[3],[-2],[8],[-7],[4],[10],[2],[6],[-4],[-8],[3],[6],[-10],[-7],[3],[5],[-4],[3],[8],[-6],[-3],[-6],[4],[5],[-5],[2],[4],[3],[-4],[9],[10],[5],[8],[6],[7],[-8],[-10],[7],[8],[-3],[-5],[-2],[5],[-5],[6],[8],[5],[-10],[1],[-10],[-9],[1],[5],[-5],[-10],[-6],[5],[5],[3],[-9],[-1],[5],[-10],[2],[-10],[-2],[-1],[8],[10],[8],[2],[-4],[4],[-7],[7],[-8],[-2],[-8],[-5],[-6],[1],[5],[10],[9],[-7],[-8],[1],[-7],[9],[-3],[-1],[7],[-1],[8],[5],[2],[1],[-9],[1],[10],[3],[10],[-8],[-10],[-5],[5],[4],[-9],[-9],[3],[-10]], dtype = "int8")#candidate|16411|(550, 1)|const|int8
call_16409 = relay.TupleGetItem(func_6813_call(relay.reshape(var_16410.astype('float64'), [5, 5, 10]), relay.reshape(const_16411.astype('int8'), [550,]), ), 1)
call_16412 = relay.TupleGetItem(func_6816_call(relay.reshape(var_16410.astype('float64'), [5, 5, 10]), relay.reshape(const_16411.astype('int8'), [550,]), ), 1)
output = relay.Tuple([call_16371,call_16373,var_16374,const_16375,call_16377,call_16383,call_16394,const_16395,uop_16404,call_16409,var_16410,const_16411,])
output2 = relay.Tuple([call_16372,call_16376,var_16374,const_16375,call_16378,call_16385,call_16396,const_16395,uop_16404,call_16412,var_16410,const_16411,])
func_16423 = relay.Function([var_16374,var_16384,var_16410,], output)
mod['func_16423'] = func_16423
mod = relay.transform.InferType()(mod)
mutated_mod['func_16423'] = func_16423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16423_call = mutated_mod.get_global_var('func_16423')
var_16425 = relay.var("var_16425", dtype = "int8", shape = (270,))#candidate|16425|(270,)|var|int8
var_16426 = relay.var("var_16426", dtype = "float32", shape = (195, 3))#candidate|16426|(195, 3)|var|float32
var_16427 = relay.var("var_16427", dtype = "float64", shape = (250,))#candidate|16427|(250,)|var|float64
call_16424 = func_16423_call(var_16425,var_16426,var_16427,)
output = call_16424
func_16428 = relay.Function([var_16425,var_16426,var_16427,], output)
mutated_mod['func_16428'] = func_16428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15709_call = mod.get_global_var('func_15709')
func_15711_call = mutated_mod.get_global_var('func_15711')
call_16430 = relay.TupleGetItem(func_15709_call(), 1)
call_16431 = relay.TupleGetItem(func_15711_call(), 1)
output = relay.Tuple([call_16430,])
output2 = relay.Tuple([call_16431,])
func_16446 = relay.Function([], output)
mod['func_16446'] = func_16446
mod = relay.transform.InferType()(mod)
mutated_mod['func_16446'] = func_16446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16446_call = mutated_mod.get_global_var('func_16446')
call_16447 = func_16446_call()
output = call_16447
func_16448 = relay.Function([], output)
mutated_mod['func_16448'] = func_16448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12870_call = mod.get_global_var('func_12870')
func_12871_call = mutated_mod.get_global_var('func_12871')
call_16468 = func_12870_call()
call_16469 = func_12870_call()
func_13918_call = mod.get_global_var('func_13918')
func_13919_call = mutated_mod.get_global_var('func_13919')
call_16498 = func_13918_call()
call_16499 = func_13918_call()
output = relay.Tuple([call_16468,call_16498,])
output2 = relay.Tuple([call_16469,call_16499,])
func_16515 = relay.Function([], output)
mod['func_16515'] = func_16515
mod = relay.transform.InferType()(mod)
mutated_mod['func_16515'] = func_16515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16515_call = mutated_mod.get_global_var('func_16515')
call_16516 = func_16515_call()
output = call_16516
func_16517 = relay.Function([], output)
mutated_mod['func_16517'] = func_16517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13771_call = mod.get_global_var('func_13771')
func_13773_call = mutated_mod.get_global_var('func_13773')
call_16557 = relay.TupleGetItem(func_13771_call(), 1)
call_16558 = relay.TupleGetItem(func_13773_call(), 1)
var_16560 = relay.var("var_16560", dtype = "bool", shape = (300, 8))#candidate|16560|(300, 8)|var|bool
bop_16561 = relay.not_equal(call_16557.astype('bool'), relay.reshape(var_16560.astype('bool'), relay.shape_of(call_16557))) # shape=(300, 8)
bop_16564 = relay.not_equal(call_16558.astype('bool'), relay.reshape(var_16560.astype('bool'), relay.shape_of(call_16558))) # shape=(300, 8)
output = bop_16561
output2 = bop_16564
func_16568 = relay.Function([var_16560,], output)
mod['func_16568'] = func_16568
mod = relay.transform.InferType()(mod)
var_16569 = relay.var("var_16569", dtype = "bool", shape = (300, 8))#candidate|16569|(300, 8)|var|bool
output = func_16568(var_16569)
func_16570 = relay.Function([var_16569], output)
mutated_mod['func_16570'] = func_16570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16303_call = mod.get_global_var('func_16303')
func_16305_call = mutated_mod.get_global_var('func_16305')
call_16612 = func_16303_call()
call_16613 = func_16303_call()
output = call_16612
output2 = call_16613
func_16614 = relay.Function([], output)
mod['func_16614'] = func_16614
mod = relay.transform.InferType()(mod)
mutated_mod['func_16614'] = func_16614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16614_call = mutated_mod.get_global_var('func_16614')
call_16615 = func_16614_call()
output = call_16615
func_16616 = relay.Function([], output)
mutated_mod['func_16616'] = func_16616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14810_call = mod.get_global_var('func_14810')
func_14812_call = mutated_mod.get_global_var('func_14812')
call_16623 = relay.TupleGetItem(func_14810_call(), 0)
call_16624 = relay.TupleGetItem(func_14812_call(), 0)
func_13918_call = mod.get_global_var('func_13918')
func_13919_call = mutated_mod.get_global_var('func_13919')
call_16648 = func_13918_call()
call_16649 = func_13918_call()
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_16652 = relay.TupleGetItem(func_11409_call(), 0)
call_16653 = relay.TupleGetItem(func_11410_call(), 0)
func_16230_call = mod.get_global_var('func_16230')
func_16233_call = mutated_mod.get_global_var('func_16233')
var_16663 = relay.var("var_16663", dtype = "uint32", shape = ())#candidate|16663|()|var|uint32
call_16662 = relay.TupleGetItem(func_16230_call(relay.reshape(var_16663.astype('uint32'), [])), 2)
call_16664 = relay.TupleGetItem(func_16233_call(relay.reshape(var_16663.astype('uint32'), [])), 2)
output = relay.Tuple([call_16623,call_16648,call_16652,call_16662,var_16663,])
output2 = relay.Tuple([call_16624,call_16649,call_16653,call_16664,var_16663,])
func_16666 = relay.Function([var_16663,], output)
mod['func_16666'] = func_16666
mod = relay.transform.InferType()(mod)
mutated_mod['func_16666'] = func_16666
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16667 = relay.var("var_16667", dtype = "uint32", shape = ())#candidate|16667|()|var|uint32
func_16666_call = mutated_mod.get_global_var('func_16666')
call_16668 = func_16666_call(var_16667)
output = call_16668
func_16669 = relay.Function([var_16667], output)
mutated_mod['func_16669'] = func_16669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12334_call = mod.get_global_var('func_12334')
func_12336_call = mutated_mod.get_global_var('func_12336')
call_16703 = relay.TupleGetItem(func_12334_call(), 0)
call_16704 = relay.TupleGetItem(func_12336_call(), 0)
func_12198_call = mod.get_global_var('func_12198')
func_12202_call = mutated_mod.get_global_var('func_12202')
var_16727 = relay.var("var_16727", dtype = "int8", shape = (550, 1))#candidate|16727|(550, 1)|var|int8
call_16726 = relay.TupleGetItem(func_12198_call(relay.reshape(var_16727.astype('int8'), [275, 2]), relay.reshape(var_16727.astype('int8'), [275, 2]), ), 0)
call_16728 = relay.TupleGetItem(func_12202_call(relay.reshape(var_16727.astype('int8'), [275, 2]), relay.reshape(var_16727.astype('int8'), [275, 2]), ), 0)
uop_16734 = relay.acosh(var_16727.astype('float64')) # shape=(550, 1)
func_12890_call = mod.get_global_var('func_12890')
func_12892_call = mutated_mod.get_global_var('func_12892')
call_16738 = relay.TupleGetItem(func_12890_call(), 0)
call_16739 = relay.TupleGetItem(func_12892_call(), 0)
func_3151_call = mod.get_global_var('func_3151')
func_3156_call = mutated_mod.get_global_var('func_3156')
var_16741 = relay.var("var_16741", dtype = "float32", shape = (700,))#candidate|16741|(700,)|var|float32
var_16742 = relay.var("var_16742", dtype = "int8", shape = ())#candidate|16742|()|var|int8
var_16743 = relay.var("var_16743", dtype = "float32", shape = (20, 120))#candidate|16743|(20, 120)|var|float32
call_16740 = relay.TupleGetItem(func_3151_call(relay.reshape(var_16741.astype('float32'), [5, 10, 14]), relay.reshape(var_16742.astype('int8'), []), relay.reshape(var_16743.astype('float32'), [2400,]), ), 3)
call_16744 = relay.TupleGetItem(func_3156_call(relay.reshape(var_16741.astype('float32'), [5, 10, 14]), relay.reshape(var_16742.astype('int8'), []), relay.reshape(var_16743.astype('float32'), [2400,]), ), 3)
output = relay.Tuple([call_16703,call_16726,uop_16734,call_16738,call_16740,var_16741,var_16742,var_16743,])
output2 = relay.Tuple([call_16704,call_16728,uop_16734,call_16739,call_16744,var_16741,var_16742,var_16743,])
func_16747 = relay.Function([var_16727,var_16741,var_16742,var_16743,], output)
mod['func_16747'] = func_16747
mod = relay.transform.InferType()(mod)
var_16748 = relay.var("var_16748", dtype = "int8", shape = (550, 1))#candidate|16748|(550, 1)|var|int8
var_16749 = relay.var("var_16749", dtype = "float32", shape = (700,))#candidate|16749|(700,)|var|float32
var_16750 = relay.var("var_16750", dtype = "int8", shape = ())#candidate|16750|()|var|int8
var_16751 = relay.var("var_16751", dtype = "float32", shape = (20, 120))#candidate|16751|(20, 120)|var|float32
output = func_16747(var_16748,var_16749,var_16750,var_16751,)
func_16752 = relay.Function([var_16748,var_16749,var_16750,var_16751,], output)
mutated_mod['func_16752'] = func_16752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12234_call = mod.get_global_var('func_12234')
func_12235_call = mutated_mod.get_global_var('func_12235')
call_16820 = relay.TupleGetItem(func_12234_call(), 0)
call_16821 = relay.TupleGetItem(func_12235_call(), 0)
func_12999_call = mod.get_global_var('func_12999')
func_13000_call = mutated_mod.get_global_var('func_13000')
call_16823 = func_12999_call()
call_16824 = func_12999_call()
func_16568_call = mod.get_global_var('func_16568')
func_16570_call = mutated_mod.get_global_var('func_16570')
var_16833 = relay.var("var_16833", dtype = "bool", shape = (10, 240))#candidate|16833|(10, 240)|var|bool
call_16832 = func_16568_call(relay.reshape(var_16833.astype('bool'), [300, 8]))
call_16834 = func_16568_call(relay.reshape(var_16833.astype('bool'), [300, 8]))
func_13273_call = mod.get_global_var('func_13273')
func_13274_call = mutated_mod.get_global_var('func_13274')
call_16837 = relay.TupleGetItem(func_13273_call(), 0)
call_16838 = relay.TupleGetItem(func_13274_call(), 0)
uop_16843 = relay.sin(var_16833.astype('float32')) # shape=(10, 240)
func_14114_call = mod.get_global_var('func_14114')
func_14117_call = mutated_mod.get_global_var('func_14117')
const_16854 = relay.const([5,-8,5,-3,-8,-4,-2,1,5,-2,10,4,-6,9,5,-1,1,7,1,3,-5,-6,3,6,-5,10,10,-9,-2,10,8,10,-1,5,8,-3,6,-10,9,8,4,-3,-1,1,-3,-5,-4,-2,3,-9,5,6,1,2,-1,6,-8,10,-3,7,3,7,-6,-2,-6,9,-3,5,-2,6,5,1,-2,5,3,1,3,-3,9,-7,8,-6,-3,-3,-8,-8,-10,8,-9,9,-6,-10,-10,-5,10,-4,10,-7,3,-5,10,3,2,4,-6,-5,-3,1,-8,2,10,6,8,-10,7,1,1,-9,-5,6,8,-6,-6,6,-3,2,6,3,3,-4,-1,8,-9,6,-2,7,-4,2,-8,-4,7,-6,5,-7,-3,7,-4,-5,-1,-8,3,-2,-8,9,-1,9,-8,-10,-4,-1,6,2,-4,4,8,-8,-7,10,-5,1,1,-5,-7,-3,-4,2,2,-1,-1,-2,8,1,-2,-1,9,6,-4,-8,8,5,-4,1,9,4,8,8,-8,1,10,-9,-6,9,-6,2,-8,5,4,-10,7,-2,2,10,10,1,5,-1,5,-2,6,-4,-3,-8,4,-1,-4,7,-6,7,10,8,-8,-8,-8,5,-6,-10,-9,-9,6,3,4,5,8,-6,2,8,2,4,-8,-3,9,7,-2,10,-4,-8,-2,8,7,-10,7,-10,6,8,4,-10,5,-8,2,4,10,6,-5,5,10,10,5,-8,-3,-5,-8,-9,-4,9,-4,4,3,9,6,-9,-9,-6,10,-5,10,9,7,-10,-4,7,-2,-5,10,-4,-5,-7,-3,-9,6,-5,4,-4,-3,-1,3,-6,-8,-9,-2,-9,5,1,8,10,-4,2,-10,-10,-3,9,-1,-1,5,-9,5,6,-3,-10,1,-7,-9,-4,7,2,-4,-6,-6,-4,-10,-2,1,7,-8,-7,8,-3,-2,6,8,-1,-8,7,-7,9,-4,-2,-8,10,-5,5,10,-10,5,-4,-3,7,-4,-7,7,-8,-6,7,9,-2,-4,-8,4,-7,-4,-2,-7,-8,5,-10,1,3,-8,9,-10,2,7,8,-7,-10,7,-10,3,5,-3,-10,5,-10,-6,10,2,-1,1,-10,-8,1,-6,-2,-9,9,-4,-4,2,1,3,-5,-5,-3,8,7,8,3,-1,5,2,1,10,-6,-9,4,10,8,8,10,-7,-3,-6,-10,-3,-6,6,-10,5,3,-3,-10,8,8,9,3,-6,-2,-7,9,5,5,-5,2,-1,3,-3,8,-1,7,-6,-8,1,5,2,7,9,1,-7,1,-9,3,-9,1,-9,2,1,8,-9,9,6,9,8,-9,-4,-2,-9,2,7,-8,2,-2,9,6,-4,9,10,5,-9,-2,7,3,10,3,-9,-4,2,-5,-7,-9,5,-10,8,-5,-2,-10,-1,-6,-8,-8,2,9,9,5,6,-8,-3,-8,-6,10,1,6,2,-3,-10,9,-5,6,-6,-4,6,-3,-10,4,3,-3,-1,-6,-10,-5,-2,-2,5,-2,8,1,-8,7,-5,-6,-2,-3,-8,5,-8,8,-5,10,8,-2,10,10,-10,-5,-7,-3,10,1,-3,-3,9,4,2,5,-5,-6,-10,2,5,-5,8,9,-4,-3,-9,9,-10,1,6,-1,4,-6,4,-4,-5,9,-7,-9,-1,7,1,-7,10,2,-5,-8,10,3,2,-1,6,-10,10,-5,4,-10,-9,-7,-4,-6,-1,8,-10,5,8,-9,-10,1,-8,3,-8,6,-10,10,-1,-3,-3,-6,-1,5,1,-6,-10,-2,-3,10,-6,1,-9,-1,7,5,-4,3,5,7,-9,-8,-1,-7,3,-6,-4,-6,7,-5,1,4,-2,5,6,-5,6,-6,-2,-9,-2,6,1,-9,9,-3,-4,8,-8,5,-4,9,-6,6,9,4,2,9,4,-2,-4,5,-3,-5,-7,-3,5,-10,-8,-8,4,10,4,9,-9,-2,5,-10,4,9,10,-2,-3,-3,-1,-10,4,2,3,-5,4,5,7,-10,-3,-2,-1,7,9,7,-2,8,8,4,-3,4,-10,-1,-6,-10,1,1,6,-6,-7,-8,1,-7,-6,-2,1,8,-5,-8,1,-10,-10,4,9,5,-4,-9,7,-4,6,-1,2,-8,-10,7,-6,6,8,-4,-2,6,-1,1,-10,10,10,5,-3,-10,3,4,4,5,-2,2,-1,-1,5,10,-6,-3,2,-2,-1,7,10,3,-3,-8,1,-8,10,3,-1,3,3,-8,2,-7,-2,8,6,-6,2,-6,7,5,5,-5,3,6,3,-9,3,9,2,7,-3,-9,-10,9,-10,7,4,-2,9,1,1,7,9,1,-7,1,3,4,6,-3,8,2,1,9,1,1,3,7,-8,-3,-9,5,-6,-5,4,1,-7,4,-8,-7,-4,-2,-8,8,9,3,8,10,-8,-10,-5,4,3,-10,-2,1,-5,2,-4,-1,4,3,-3,7,9,4,8,8,8,4,4,6,8,5,10,7,10,-5,-2,-4,8,7,-6,7,4,3,-7,-7,9,-7,8,3,3,-2,-8,7,4,2,-10,5,-2,-2,-9,4,-1,-7,6,-10,7,5,8,-3,-6,4,6,10,10,-7,-8,-7,3,-1,-5,9,3,-7,-5,-7,5,-7,-3,-1,8,1,8,-7,3,3,9,8,-7,6,7,-5,5,5,10,10,-1,-3,9,3,8,-8,7,2,4,8,-1,4,-4,3,-5,1,4,-7,6,4,6,-2,1,9,-3,-5,-7,-10,9,8,-6,10,-4,2,-6,3,-10,7,2,5,10,-10,2,-1,-3,3,-7,-1,9,-1,2,1,1,-3,3,-6,9,-1,6,-2,-8,-10,7,5,5,-4,-8,-8,10,-1,9,-5,3,-1,-5,-8,9,7,-9,3,6,2,-10,-4,4,-5,-3,5,-6,7,-1,-4,4,6,4,9,7,-4,4,9,-5,4,5,-6,-6,-4,-9,-7,10,8,3,5,-9,-8,9,4,4,-2,7,-3,2,-10,-6,3,2,-1,1,6,-5,4,6,7,-7,-2,-8,7,-10,8,6,3,7,3,-10,-7,-5,-10,-10,-2,8,9,-7,-4,5,-3,7,9], dtype = "uint64")#candidate|16854|(1170,)|const|uint64
call_16853 = relay.TupleGetItem(func_14114_call(relay.reshape(const_16854.astype('uint64'), [9, 13, 10]), relay.reshape(const_16854.astype('uint64'), [9, 13, 10]), ), 1)
call_16855 = relay.TupleGetItem(func_14117_call(relay.reshape(const_16854.astype('uint64'), [9, 13, 10]), relay.reshape(const_16854.astype('uint64'), [9, 13, 10]), ), 1)
output = relay.Tuple([call_16820,call_16823,call_16832,call_16837,uop_16843,call_16853,const_16854,])
output2 = relay.Tuple([call_16821,call_16824,call_16834,call_16838,uop_16843,call_16855,const_16854,])
func_16863 = relay.Function([var_16833,], output)
mod['func_16863'] = func_16863
mod = relay.transform.InferType()(mod)
var_16864 = relay.var("var_16864", dtype = "bool", shape = (10, 240))#candidate|16864|(10, 240)|var|bool
output = func_16863(var_16864)
func_16865 = relay.Function([var_16864], output)
mutated_mod['func_16865'] = func_16865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12990_call = mod.get_global_var('func_12990')
func_12991_call = mutated_mod.get_global_var('func_12991')
call_16891 = relay.TupleGetItem(func_12990_call(), 0)
call_16892 = relay.TupleGetItem(func_12991_call(), 0)
output = relay.Tuple([call_16891,])
output2 = relay.Tuple([call_16892,])
func_16901 = relay.Function([], output)
mod['func_16901'] = func_16901
mod = relay.transform.InferType()(mod)
mutated_mod['func_16901'] = func_16901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16901_call = mutated_mod.get_global_var('func_16901')
call_16902 = func_16901_call()
output = call_16902
func_16903 = relay.Function([], output)
mutated_mod['func_16903'] = func_16903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16927 = relay.var("var_16927", dtype = "uint8", shape = (1, 14, 8))#candidate|16927|(1, 14, 8)|var|uint8
const_16928 = relay.const([[[1,-6,9,5,-6,-8,10,2],[-8,-7,-4,2,9,-7,10,-4],[1,-10,-5,-6,5,-7,5,-2],[-4,2,5,2,-9,-8,-4,4],[4,10,8,-2,9,7,-9,-9],[-9,-10,4,10,-10,-4,3,-4],[1,-6,-9,3,8,-5,10,9],[-6,-6,1,-6,6,-7,-10,-6],[4,-2,-10,2,7,-4,-1,8],[2,-8,10,3,-3,-5,-1,4],[10,-8,-2,-8,-8,-8,5,-6],[10,9,-7,-7,5,5,-10,-9],[6,-3,-8,9,-3,-4,-7,-3],[-6,8,-7,6,-7,-7,-10,7]],[[4,6,1,5,-6,-2,1,1],[-10,-1,-4,-8,-9,-7,-9,-7],[-6,-4,-2,-3,-2,-3,-10,10],[-3,-6,1,-9,-7,9,3,-1],[-1,-8,-8,1,-5,2,-9,5],[5,-9,5,7,4,-10,-2,-6],[9,-5,-6,-4,-1,6,9,1],[3,2,-8,10,5,-9,-2,-9],[10,8,10,-6,-8,-2,6,-5],[-5,-6,8,-5,7,-9,10,2],[3,7,-3,6,-9,-2,-6,-3],[6,2,-7,-8,-2,7,-6,-3],[10,2,-6,7,-1,-10,6,5],[-3,7,-5,-8,3,-10,-4,-9]],[[4,-8,-2,-6,3,-7,7,2],[-1,4,3,5,-7,8,8,8],[9,-2,10,-5,2,-4,5,3],[-5,2,-8,6,1,-7,-1,9],[-10,4,-9,-4,10,1,4,-9],[-10,-8,9,-4,-10,-9,5,-3],[-9,6,4,10,-10,9,-5,-4],[1,-3,-6,1,5,6,-8,-4],[6,8,2,5,-8,-7,-3,8],[-10,6,-6,-1,7,-3,-8,5],[-9,-7,-10,4,-7,1,-9,-3],[9,-7,6,-8,-9,9,1,3],[-8,2,1,4,-4,-9,3,4],[-1,7,-2,2,7,9,9,8]],[[10,-3,-6,2,-3,3,-3,10],[-1,-3,3,4,-9,9,-5,-3],[-9,-8,5,-4,-9,6,5,5],[-2,-1,-4,-6,8,-2,4,-7],[-4,-7,5,9,8,7,1,3],[2,10,-9,-10,-4,7,8,1],[1,4,9,1,1,5,1,7],[2,-1,6,7,4,9,9,5],[-8,-7,2,-8,-7,-5,3,-4],[-1,-7,6,8,1,1,7,-2],[-5,-6,7,10,-1,6,8,10],[-7,-8,-2,-3,6,-2,2,-2],[3,5,-3,5,3,7,-3,3],[-7,-3,9,-3,9,-10,1,7]],[[-9,3,-1,-8,-4,-4,-4,-7],[7,-2,-5,3,-10,7,6,-5],[-8,9,-1,-2,1,-1,4,-8],[7,9,-4,-8,-7,6,-10,-8],[-1,8,5,-6,7,-3,-5,-1],[-2,-6,3,3,-2,-3,1,-1],[-2,4,-8,-4,-8,-7,2,7],[8,-2,-1,3,3,-4,-9,5],[-3,-9,-1,-7,3,-4,-1,9],[-6,2,-6,-1,-1,1,1,3],[9,6,-8,9,-8,-6,-5,10],[-8,9,7,10,8,-2,-1,2],[9,-10,-4,6,-1,2,-9,-7],[5,10,-9,-2,4,-3,-8,-5]],[[-6,4,3,1,6,1,-6,-2],[-6,2,3,-10,7,1,2,-4],[10,-6,2,8,1,-1,10,7],[-6,-1,3,3,9,-7,2,7],[1,-5,-3,9,2,10,-5,-10],[-3,9,4,-6,-8,4,-4,1],[6,-8,-1,-2,1,7,-6,7],[7,7,-8,6,8,5,3,-9],[4,-8,6,-7,2,3,10,7],[-5,-9,-9,-10,-7,9,3,-2],[5,1,10,6,-2,9,-10,9],[3,10,-5,9,7,5,-7,-6],[-7,-4,5,-10,-1,-8,9,6],[-7,6,-9,7,6,-6,9,5]],[[-9,4,1,10,6,4,-7,-7],[-9,8,1,-3,-7,8,-3,1],[-4,-7,-2,-8,6,4,-2,-10],[8,-8,3,-4,2,-4,6,8],[-4,-8,3,5,-8,7,-1,-1],[-4,6,2,-6,3,-1,9,1],[-6,8,-5,-1,3,4,-4,1],[-6,5,-6,-2,3,7,3,-5],[-9,10,-7,10,8,2,-1,-10],[-1,-4,-8,-7,10,-2,4,-3],[10,10,4,-7,-3,6,3,8],[-3,-2,-1,-1,-3,-7,10,-1],[-3,8,-10,-2,4,-5,-6,-3],[-9,1,6,-2,-4,-7,9,5]]], dtype = "uint8")#candidate|16928|(7, 14, 8)|const|uint8
bop_16929 = relay.subtract(var_16927.astype('uint8'), const_16928.astype('uint8')) # shape=(7, 14, 8)
func_14723_call = mod.get_global_var('func_14723')
func_14725_call = mutated_mod.get_global_var('func_14725')
call_16939 = func_14723_call()
call_16940 = func_14723_call()
output = relay.Tuple([bop_16929,call_16939,])
output2 = relay.Tuple([bop_16929,call_16940,])
func_16946 = relay.Function([var_16927,], output)
mod['func_16946'] = func_16946
mod = relay.transform.InferType()(mod)
var_16947 = relay.var("var_16947", dtype = "uint8", shape = (1, 14, 8))#candidate|16947|(1, 14, 8)|var|uint8
output = func_16946(var_16947)
func_16948 = relay.Function([var_16947], output)
mutated_mod['func_16948'] = func_16948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16614_call = mod.get_global_var('func_16614')
func_16616_call = mutated_mod.get_global_var('func_16616')
call_16964 = func_16614_call()
call_16965 = func_16614_call()
output = relay.Tuple([call_16964,])
output2 = relay.Tuple([call_16965,])
func_17001 = relay.Function([], output)
mod['func_17001'] = func_17001
mod = relay.transform.InferType()(mod)
output = func_17001()
func_17002 = relay.Function([], output)
mutated_mod['func_17002'] = func_17002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15129_call = mod.get_global_var('func_15129')
func_15131_call = mutated_mod.get_global_var('func_15131')
call_17026 = relay.TupleGetItem(func_15129_call(), 1)
call_17027 = relay.TupleGetItem(func_15131_call(), 1)
func_10137_call = mod.get_global_var('func_10137')
func_10139_call = mutated_mod.get_global_var('func_10139')
call_17038 = func_10137_call()
call_17039 = func_10137_call()
output = relay.Tuple([call_17026,call_17038,])
output2 = relay.Tuple([call_17027,call_17039,])
func_17047 = relay.Function([], output)
mod['func_17047'] = func_17047
mod = relay.transform.InferType()(mod)
output = func_17047()
func_17048 = relay.Function([], output)
mutated_mod['func_17048'] = func_17048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16901_call = mod.get_global_var('func_16901')
func_16903_call = mutated_mod.get_global_var('func_16903')
call_17057 = relay.TupleGetItem(func_16901_call(), 0)
call_17058 = relay.TupleGetItem(func_16903_call(), 0)
func_3434_call = mod.get_global_var('func_3434')
func_3437_call = mutated_mod.get_global_var('func_3437')
var_17062 = relay.var("var_17062", dtype = "int8", shape = (550,))#candidate|17062|(550,)|var|int8
call_17061 = relay.TupleGetItem(func_3434_call(relay.reshape(var_17062.astype('int8'), [10, 5, 11])), 0)
call_17063 = relay.TupleGetItem(func_3437_call(relay.reshape(var_17062.astype('int8'), [10, 5, 11])), 0)
output = relay.Tuple([call_17057,call_17061,var_17062,])
output2 = relay.Tuple([call_17058,call_17063,var_17062,])
func_17070 = relay.Function([var_17062,], output)
mod['func_17070'] = func_17070
mod = relay.transform.InferType()(mod)
var_17071 = relay.var("var_17071", dtype = "int8", shape = (550,))#candidate|17071|(550,)|var|int8
output = func_17070(var_17071)
func_17072 = relay.Function([var_17071], output)
mutated_mod['func_17072'] = func_17072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12890_call = mod.get_global_var('func_12890')
func_12892_call = mutated_mod.get_global_var('func_12892')
call_17076 = relay.TupleGetItem(func_12890_call(), 0)
call_17077 = relay.TupleGetItem(func_12892_call(), 0)
output = call_17076
output2 = call_17077
func_17104 = relay.Function([], output)
mod['func_17104'] = func_17104
mod = relay.transform.InferType()(mod)
output = func_17104()
func_17105 = relay.Function([], output)
mutated_mod['func_17105'] = func_17105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15095_call = mod.get_global_var('func_15095')
func_15097_call = mutated_mod.get_global_var('func_15097')
call_17136 = relay.TupleGetItem(func_15095_call(), 1)
call_17137 = relay.TupleGetItem(func_15097_call(), 1)
output = relay.Tuple([call_17136,])
output2 = relay.Tuple([call_17137,])
func_17138 = relay.Function([], output)
mod['func_17138'] = func_17138
mod = relay.transform.InferType()(mod)
mutated_mod['func_17138'] = func_17138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17138_call = mutated_mod.get_global_var('func_17138')
call_17139 = func_17138_call()
output = call_17139
func_17140 = relay.Function([], output)
mutated_mod['func_17140'] = func_17140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15200_call = mod.get_global_var('func_15200')
func_15201_call = mutated_mod.get_global_var('func_15201')
call_17157 = relay.TupleGetItem(func_15200_call(), 0)
call_17158 = relay.TupleGetItem(func_15201_call(), 0)
output = call_17157
output2 = call_17158
func_17164 = relay.Function([], output)
mod['func_17164'] = func_17164
mod = relay.transform.InferType()(mod)
output = func_17164()
func_17165 = relay.Function([], output)
mutated_mod['func_17165'] = func_17165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13918_call = mod.get_global_var('func_13918')
func_13919_call = mutated_mod.get_global_var('func_13919')
call_17176 = func_13918_call()
call_17177 = func_13918_call()
output = relay.Tuple([call_17176,])
output2 = relay.Tuple([call_17177,])
func_17185 = relay.Function([], output)
mod['func_17185'] = func_17185
mod = relay.transform.InferType()(mod)
output = func_17185()
func_17186 = relay.Function([], output)
mutated_mod['func_17186'] = func_17186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10137_call = mod.get_global_var('func_10137')
func_10139_call = mutated_mod.get_global_var('func_10139')
call_17210 = func_10137_call()
call_17211 = func_10137_call()
output = relay.Tuple([call_17210,])
output2 = relay.Tuple([call_17211,])
func_17224 = relay.Function([], output)
mod['func_17224'] = func_17224
mod = relay.transform.InferType()(mod)
output = func_17224()
func_17225 = relay.Function([], output)
mutated_mod['func_17225'] = func_17225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16515_call = mod.get_global_var('func_16515')
func_16517_call = mutated_mod.get_global_var('func_16517')
call_17228 = relay.TupleGetItem(func_16515_call(), 0)
call_17229 = relay.TupleGetItem(func_16517_call(), 0)
output = relay.Tuple([call_17228,])
output2 = relay.Tuple([call_17229,])
func_17232 = relay.Function([], output)
mod['func_17232'] = func_17232
mod = relay.transform.InferType()(mod)
mutated_mod['func_17232'] = func_17232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17232_call = mutated_mod.get_global_var('func_17232')
call_17233 = func_17232_call()
output = call_17233
func_17234 = relay.Function([], output)
mutated_mod['func_17234'] = func_17234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15274_call = mod.get_global_var('func_15274')
func_15276_call = mutated_mod.get_global_var('func_15276')
call_17255 = func_15274_call()
call_17256 = func_15274_call()
output = call_17255
output2 = call_17256
func_17271 = relay.Function([], output)
mod['func_17271'] = func_17271
mod = relay.transform.InferType()(mod)
mutated_mod['func_17271'] = func_17271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17271_call = mutated_mod.get_global_var('func_17271')
call_17272 = func_17271_call()
output = call_17272
func_17273 = relay.Function([], output)
mutated_mod['func_17273'] = func_17273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11409_call = mod.get_global_var('func_11409')
func_11410_call = mutated_mod.get_global_var('func_11410')
call_17295 = relay.TupleGetItem(func_11409_call(), 2)
call_17296 = relay.TupleGetItem(func_11410_call(), 2)
output = relay.Tuple([call_17295,])
output2 = relay.Tuple([call_17296,])
func_17297 = relay.Function([], output)
mod['func_17297'] = func_17297
mod = relay.transform.InferType()(mod)
output = func_17297()
func_17298 = relay.Function([], output)
mutated_mod['func_17298'] = func_17298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12334_call = mod.get_global_var('func_12334')
func_12336_call = mutated_mod.get_global_var('func_12336')
call_17304 = relay.TupleGetItem(func_12334_call(), 0)
call_17305 = relay.TupleGetItem(func_12336_call(), 0)
func_11738_call = mod.get_global_var('func_11738')
func_11739_call = mutated_mod.get_global_var('func_11739')
call_17308 = func_11738_call()
call_17309 = func_11738_call()
output = relay.Tuple([call_17304,call_17308,])
output2 = relay.Tuple([call_17305,call_17309,])
func_17314 = relay.Function([], output)
mod['func_17314'] = func_17314
mod = relay.transform.InferType()(mod)
mutated_mod['func_17314'] = func_17314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17314_call = mutated_mod.get_global_var('func_17314')
call_17315 = func_17314_call()
output = call_17315
func_17316 = relay.Function([], output)
mutated_mod['func_17316'] = func_17316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17346 = relay.var("var_17346", dtype = "int64", shape = (5, 10, 3))#candidate|17346|(5, 10, 3)|var|int64
var_17347 = relay.var("var_17347", dtype = "int64", shape = (5, 10, 3))#candidate|17347|(5, 10, 3)|var|int64
bop_17348 = relay.logical_xor(var_17346.astype('int64'), relay.reshape(var_17347.astype('int64'), relay.shape_of(var_17346))) # shape=(5, 10, 3)
func_708_call = mod.get_global_var('func_708')
func_712_call = mutated_mod.get_global_var('func_712')
var_17353 = relay.var("var_17353", dtype = "uint64", shape = (60,))#candidate|17353|(60,)|var|uint64
var_17354 = relay.var("var_17354", dtype = "uint32", shape = (63,))#candidate|17354|(63,)|var|uint32
call_17352 = relay.TupleGetItem(func_708_call(relay.reshape(var_17353.astype('uint64'), [12, 5, 1]), relay.reshape(var_17354.astype('uint32'), [7, 9]), ), 0)
call_17355 = relay.TupleGetItem(func_712_call(relay.reshape(var_17353.astype('uint64'), [12, 5, 1]), relay.reshape(var_17354.astype('uint32'), [7, 9]), ), 0)
func_5753_call = mod.get_global_var('func_5753')
func_5756_call = mutated_mod.get_global_var('func_5756')
const_17363 = relay.const([-5.003770,8.100024,-1.609440,2.318000,8.215766,3.115545,-6.038193,-0.485740,3.426333,7.208624,-5.956604,1.550384,-3.928281,-9.751269,1.713767,6.840489,0.423271,-8.481567,5.157714,3.999255,-1.060501,0.549577,6.054512,-4.616005,-4.086816,-3.465037,7.613078,-7.383986,0.647803,-1.455438,6.136996,-6.664374,-6.065580,5.256780,0.334233,-2.483012,2.779288,-7.525591,-2.348927,-2.476376,-9.228236,7.826787,-5.232503,7.914492,-2.178609,-4.621749,-9.591800,-4.376486,2.410616,-6.555391,1.622548,-5.283514,6.309722,7.031014,3.991884,-6.808415,-4.832458,-4.210923,1.262887,-2.036698,4.122021,2.638356,-8.633871,-4.800523,1.110196,-1.458333,-4.384956,-9.539005,6.776096,5.408430,4.990771,-8.778649,8.669166,-0.794369,-6.808962,-3.005208,3.773465,7.433419,-1.052216,9.053733,5.713220,-3.870955,-3.413602,3.225686,-9.621577,0.516960,-4.254163,7.192991,-8.520796,-5.327772,-3.707648,-9.133453,-7.566647,4.869028,0.927236,1.330236,-0.346155,-6.786189,-4.677781,-2.152905,-9.348767,-0.809612,9.206962,-7.024604,7.393212], dtype = "float32")#candidate|17363|(105,)|const|float32
call_17362 = relay.TupleGetItem(func_5753_call(relay.reshape(const_17363.astype('float32'), [15, 1, 7])), 1)
call_17364 = relay.TupleGetItem(func_5756_call(relay.reshape(const_17363.astype('float32'), [15, 1, 7])), 1)
uop_17381 = relay.asinh(var_17347.astype('float64')) # shape=(5, 10, 3)
output = relay.Tuple([bop_17348,call_17352,var_17353,var_17354,call_17362,const_17363,uop_17381,])
output2 = relay.Tuple([bop_17348,call_17355,var_17353,var_17354,call_17364,const_17363,uop_17381,])
func_17383 = relay.Function([var_17346,var_17347,var_17353,var_17354,], output)
mod['func_17383'] = func_17383
mod = relay.transform.InferType()(mod)
mutated_mod['func_17383'] = func_17383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17383_call = mutated_mod.get_global_var('func_17383')
var_17385 = relay.var("var_17385", dtype = "int64", shape = (5, 10, 3))#candidate|17385|(5, 10, 3)|var|int64
var_17386 = relay.var("var_17386", dtype = "int64", shape = (5, 10, 3))#candidate|17386|(5, 10, 3)|var|int64
var_17387 = relay.var("var_17387", dtype = "uint64", shape = (60,))#candidate|17387|(60,)|var|uint64
var_17388 = relay.var("var_17388", dtype = "uint32", shape = (63,))#candidate|17388|(63,)|var|uint32
call_17384 = func_17383_call(var_17385,var_17386,var_17387,var_17388,)
output = call_17384
func_17389 = relay.Function([var_17385,var_17386,var_17387,var_17388,], output)
mutated_mod['func_17389'] = func_17389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12225_call = mod.get_global_var('func_12225')
func_12226_call = mutated_mod.get_global_var('func_12226')
call_17435 = func_12225_call()
call_17436 = func_12225_call()
output = call_17435
output2 = call_17436
func_17480 = relay.Function([], output)
mod['func_17480'] = func_17480
mod = relay.transform.InferType()(mod)
mutated_mod['func_17480'] = func_17480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17480_call = mutated_mod.get_global_var('func_17480')
call_17481 = func_17480_call()
output = call_17481
func_17482 = relay.Function([], output)
mutated_mod['func_17482'] = func_17482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13273_call = mod.get_global_var('func_13273')
func_13274_call = mutated_mod.get_global_var('func_13274')
call_17523 = relay.TupleGetItem(func_13273_call(), 0)
call_17524 = relay.TupleGetItem(func_13274_call(), 0)
func_17271_call = mod.get_global_var('func_17271')
func_17273_call = mutated_mod.get_global_var('func_17273')
call_17543 = func_17271_call()
call_17544 = func_17271_call()
output = relay.Tuple([call_17523,call_17543,])
output2 = relay.Tuple([call_17524,call_17544,])
func_17547 = relay.Function([], output)
mod['func_17547'] = func_17547
mod = relay.transform.InferType()(mod)
output = func_17547()
func_17548 = relay.Function([], output)
mutated_mod['func_17548'] = func_17548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12665_call = mod.get_global_var('func_12665')
func_12666_call = mutated_mod.get_global_var('func_12666')
call_17694 = func_12665_call()
call_17695 = func_12665_call()
func_17164_call = mod.get_global_var('func_17164')
func_17165_call = mutated_mod.get_global_var('func_17165')
call_17706 = func_17164_call()
call_17707 = func_17164_call()
output = relay.Tuple([call_17694,call_17706,])
output2 = relay.Tuple([call_17695,call_17707,])
func_17708 = relay.Function([], output)
mod['func_17708'] = func_17708
mod = relay.transform.InferType()(mod)
mutated_mod['func_17708'] = func_17708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17708_call = mutated_mod.get_global_var('func_17708')
call_17709 = func_17708_call()
output = call_17709
func_17710 = relay.Function([], output)
mutated_mod['func_17710'] = func_17710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_17733 = func_10556_call()
call_17734 = func_10556_call()
func_13445_call = mod.get_global_var('func_13445')
func_13447_call = mutated_mod.get_global_var('func_13447')
call_17748 = relay.TupleGetItem(func_13445_call(), 0)
call_17749 = relay.TupleGetItem(func_13447_call(), 0)
const_17752 = relay.const([[-8.797352,-3.246597,-6.630076,-5.836327,5.834324,-3.100099,-2.711295,6.318980,2.537496],[-2.117425,-1.737968,-6.526134,-9.501674,0.120368,4.309210,-4.146663,1.847456,8.809086],[-4.902558,-4.776445,7.464702,-4.540814,1.408442,8.474132,3.658155,-2.003769,1.038394],[-4.715356,3.792016,1.284035,-4.348516,3.943950,-2.320536,3.426547,-0.571724,-7.209495],[8.370392,3.628635,-8.356975,9.305126,0.326315,3.054149,-8.986294,-0.515849,-1.323524],[-1.263532,5.336507,-1.394151,-2.009790,0.627679,8.891785,-9.305558,-7.018422,8.562064],[-2.986688,-1.356315,-8.602479,9.666711,4.270907,7.480751,2.085373,-8.280905,6.069092],[3.561716,7.145530,-2.225380,-6.090388,2.434827,9.010942,-8.835715,9.886058,8.321819],[-3.655848,4.662620,-2.938178,1.990634,-6.860115,6.799764,-3.629434,-5.336514,9.572354],[0.975282,3.443614,-0.575138,6.991836,2.188885,5.210277,2.854973,9.473164,-2.256942],[7.956509,8.149555,4.234245,8.949340,1.604839,4.015868,-0.217959,0.535524,5.270023],[-8.350699,-6.812792,-8.017833,-0.895472,0.578413,-9.036283,-3.496321,-2.852907,1.015943],[-3.510299,1.718517,-4.445970,-6.112654,4.222185,0.020986,7.970875,-7.941892,3.612324],[5.345674,-7.558432,9.984416,-4.226584,-1.002704,8.162378,9.496522,-0.278084,-0.009949],[7.904766,1.770897,-3.881154,-0.990845,6.111166,3.426187,4.608442,-5.717541,7.922863],[-5.313064,4.368944,-1.278024,-4.527111,-7.635205,1.627628,-9.783431,4.678097,5.011476],[-4.905168,1.334681,-9.233244,-2.771655,-0.623088,3.196157,-9.416675,8.991455,-0.588594],[-4.773787,7.879784,6.273838,1.125660,-7.458549,-9.361511,-2.371992,1.251689,-7.073113],[-4.191063,2.658072,1.578829,0.129903,-1.612918,-2.339748,-5.178820,0.405957,3.112298],[-6.482195,-1.084612,-3.292811,2.802361,1.739335,-7.874474,-7.645536,-3.815440,5.817458],[3.148885,7.341353,-6.340460,-6.469771,4.086763,-0.785716,1.068935,5.606261,4.562168],[-5.960051,0.954195,7.426685,9.635607,-0.414104,6.591203,1.134712,-6.918266,-0.485408],[-9.944702,-1.456990,8.264112,9.173160,4.417462,-9.758606,-7.463601,0.956231,0.920388],[0.885657,8.596292,-5.921250,-9.020036,3.560435,8.382864,3.049582,-4.731789,3.505226],[-0.569750,-9.915810,9.640766,4.629268,6.120499,9.674357,6.448123,2.344008,1.598982],[-4.261671,-8.818261,-3.393119,6.382173,8.451815,9.795090,0.322138,8.129668,-3.605857],[3.919752,-1.561314,-7.884809,4.652115,9.122425,-6.689315,-7.239539,-6.057544,-4.559965],[-9.139116,-2.952387,-0.258746,-9.867236,6.401791,4.637958,5.701598,9.969149,-2.263185],[4.821607,-7.242612,-6.964836,8.566278,3.030040,2.329504,9.371941,1.476204,-8.990024],[9.936534,-7.305983,-0.181733,-4.881205,-9.860936,-2.456016,-6.870755,-7.688431,-2.138026],[6.760154,7.900555,5.526184,2.798278,6.049473,-0.385693,-2.981035,-5.855912,-0.742508],[-2.540569,-0.036033,0.220321,4.285271,7.060429,-6.293942,3.317816,9.377229,-5.919333],[6.184269,4.132538,-6.477801,-6.330074,-2.881851,1.769818,-8.873175,4.939897,-9.861857],[5.097841,-1.092001,4.230222,-9.032714,7.275597,-6.790012,-1.730472,3.291940,-4.637677],[9.181049,-6.882954,8.700561,-4.521602,8.778537,0.964995,-0.818115,-5.413941,9.740743],[8.177755,-5.462190,4.977885,-7.467407,-6.322778,-3.270825,-8.056287,-9.899287,1.912518],[-2.263908,4.209435,9.979500,-4.180690,6.173301,0.304404,-1.854300,-2.134611,2.496609],[3.199816,5.870482,3.042140,-0.191130,7.676304,-4.952633,3.662121,-9.498477,-5.084719],[8.365645,-0.028847,0.705696,2.210152,-9.778748,-7.479013,1.098720,-4.645889,-0.566450],[-8.810047,5.412674,3.899190,-6.997061,-7.627783,4.993164,9.982457,7.124913,8.036840],[8.198476,9.688751,-7.199468,6.055579,6.761197,-0.629577,5.329411,2.983076,-5.421443],[-5.029476,0.037390,0.567695,4.223131,4.360737,-8.570907,-4.927380,1.999331,-5.314875],[3.769782,0.296787,4.133103,-7.064130,3.074751,7.549176,-1.137825,-9.811446,-0.066860],[-9.258679,-4.527851,8.993385,-5.361902,-2.716423,4.107232,9.239816,-3.002565,7.820614],[-3.496479,-7.831305,7.098362,8.680717,5.618893,2.476913,-2.622925,-3.476793,6.174621],[4.746961,2.745314,1.504915,-3.753111,4.754796,-3.903647,-1.756222,9.009907,-3.361071],[-6.942961,-1.790349,8.054047,-6.176608,-9.119083,6.538734,-4.052727,5.193410,-1.967821],[-1.634680,-1.268624,-3.755653,-6.606828,8.672321,2.174212,7.682273,-4.426435,-6.781078],[9.923929,6.317681,4.058081,-6.288547,1.005454,2.330899,-9.718569,0.646158,1.981398],[7.565730,-2.577738,6.873042,-0.585566,-5.066283,8.278348,5.127535,8.697262,-6.987426],[6.967570,-9.120038,-7.266988,-6.767750,9.109055,2.999132,9.429652,-7.791566,-3.074176],[-1.881988,-1.786199,8.053268,3.161858,5.103275,2.075154,4.112963,-6.543283,5.825888],[0.472064,4.468258,8.618587,5.169935,-8.200429,9.446802,-0.887374,5.042629,-1.396031],[-6.329434,2.763297,-7.559772,1.852662,3.473406,5.362837,-7.254587,5.622293,6.469982],[6.222870,1.671311,-8.675389,-6.424162,-3.859469,-5.868660,-6.154824,-4.912551,-7.814523],[-7.901113,-6.188784,6.905791,-8.619349,-8.115407,3.581005,5.736442,1.793275,-8.977957],[8.532369,-6.931279,6.845011,-4.394726,0.162952,8.798241,9.844158,9.705754,-8.353683],[9.041238,-4.648773,-8.193211,9.249800,-3.684661,-8.782856,-5.929333,6.260191,-6.604267],[4.989723,-9.951687,6.604231,-0.883731,5.218474,2.712595,-0.144567,4.236134,-5.097756],[8.837985,3.004618,-3.258277,-1.707594,0.439983,9.916023,-4.786508,-5.045385,5.376458],[5.679521,-0.822531,8.841445,-1.499009,-9.757273,8.153227,1.874206,-1.967052,-9.142048],[-4.260096,7.348263,2.719504,3.927459,-1.002494,-8.686174,-8.734476,6.900230,3.203375],[-1.912600,6.348416,3.410202,3.563090,8.564137,6.505752,5.717161,-5.222089,5.394925],[9.451562,-3.181192,-3.687092,-1.637181,-8.513779,5.879457,-5.030130,1.012632,-5.957126],[-0.990942,8.293492,2.966770,-7.715731,-5.343598,4.092749,-0.667355,9.730451,-6.916450]], dtype = "float32")#candidate|17752|(65, 9)|const|float32
bop_17753 = relay.add(call_17748.astype('int8'), relay.reshape(const_17752.astype('int8'), relay.shape_of(call_17748))) # shape=(65, 9)
bop_17756 = relay.add(call_17749.astype('int8'), relay.reshape(const_17752.astype('int8'), relay.shape_of(call_17749))) # shape=(65, 9)
bop_17767 = relay.less_equal(call_17748.astype('bool'), relay.reshape(const_17752.astype('bool'), relay.shape_of(call_17748))) # shape=(65, 9)
bop_17770 = relay.less_equal(call_17749.astype('bool'), relay.reshape(const_17752.astype('bool'), relay.shape_of(call_17749))) # shape=(65, 9)
output = relay.Tuple([call_17733,bop_17753,bop_17767,])
output2 = relay.Tuple([call_17734,bop_17756,bop_17770,])
func_17771 = relay.Function([], output)
mod['func_17771'] = func_17771
mod = relay.transform.InferType()(mod)
mutated_mod['func_17771'] = func_17771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17771_call = mutated_mod.get_global_var('func_17771')
call_17772 = func_17771_call()
output = call_17772
func_17773 = relay.Function([], output)
mutated_mod['func_17773'] = func_17773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12225_call = mod.get_global_var('func_12225')
func_12226_call = mutated_mod.get_global_var('func_12226')
call_17847 = func_12225_call()
call_17848 = func_12225_call()
func_15274_call = mod.get_global_var('func_15274')
func_15276_call = mutated_mod.get_global_var('func_15276')
call_17851 = func_15274_call()
call_17852 = func_15274_call()
func_13380_call = mod.get_global_var('func_13380')
func_13382_call = mutated_mod.get_global_var('func_13382')
call_17853 = func_13380_call()
call_17854 = func_13380_call()
output = relay.Tuple([call_17847,call_17851,call_17853,])
output2 = relay.Tuple([call_17848,call_17852,call_17854,])
func_17857 = relay.Function([], output)
mod['func_17857'] = func_17857
mod = relay.transform.InferType()(mod)
mutated_mod['func_17857'] = func_17857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17857_call = mutated_mod.get_global_var('func_17857')
call_17858 = func_17857_call()
output = call_17858
func_17859 = relay.Function([], output)
mutated_mod['func_17859'] = func_17859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14320_call = mod.get_global_var('func_14320')
func_14322_call = mutated_mod.get_global_var('func_14322')
call_17862 = func_14320_call()
call_17863 = func_14320_call()
output = relay.Tuple([call_17862,])
output2 = relay.Tuple([call_17863,])
func_17868 = relay.Function([], output)
mod['func_17868'] = func_17868
mod = relay.transform.InferType()(mod)
output = func_17868()
func_17869 = relay.Function([], output)
mutated_mod['func_17869'] = func_17869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17001_call = mod.get_global_var('func_17001')
func_17002_call = mutated_mod.get_global_var('func_17002')
call_17887 = relay.TupleGetItem(func_17001_call(), 0)
call_17888 = relay.TupleGetItem(func_17002_call(), 0)
output = call_17887
output2 = call_17888
func_17902 = relay.Function([], output)
mod['func_17902'] = func_17902
mod = relay.transform.InferType()(mod)
mutated_mod['func_17902'] = func_17902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17902_call = mutated_mod.get_global_var('func_17902')
call_17903 = func_17902_call()
output = call_17903
func_17904 = relay.Function([], output)
mutated_mod['func_17904'] = func_17904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12779_call = mod.get_global_var('func_12779')
func_12781_call = mutated_mod.get_global_var('func_12781')
call_17910 = func_12779_call()
call_17911 = func_12779_call()
func_11127_call = mod.get_global_var('func_11127')
func_11133_call = mutated_mod.get_global_var('func_11133')
const_17916 = relay.const([-2,3,4,5,1,-9,9,6,7,-2,7,-2,1,10,3,-10,-4,7,9,3,3,3,-9,-3,-10,3,-10,2,-7,7,4,8,-2,-7,6,-1,5,2,4,-10,-2,-4,2,-2,-8,2,8,-9,5,-1,7,2,5,8,1,6,3,-4,5,7,-6,-5,-6,-5,2,4,6,-3,-1,-2,1,6,9,-10,-7,-10,-5,-9,3,4,10,7,3,8,-3,6,10,9,-3,6,7,5,4,2,8,3,1,3,-1,8,1,9,6,-1,-8,-1,4,6,-1,-5,4,8,-9,-1,-2,-8,1,-4,-7,7,3,-2,-7,-7,1,-9,2,-2,8,3,10,-3,-9,9,-4,-5,8,6,-8,-4,-6,3,10,-1,7,-8,-5,10,-10,2,-7,2,4,9,-2,-2,7,8,-9,4,3,4,3,-4,3,8,4,-5,10,2,-10,4,-8,-3,-3,4,8,-6,2,-5,-7,-6,5,-9,9,8,-4,5,5,10,4,4,3,-5,1,3,5,8,3,4,9,-1,6,-4,3,-9,-9,3,4,-9,9,4,1,3,-9,6,-9,-8,3,8,-7,7,1,-8,-7,1,-8,2,-6,1,-2,-1,4,-7,-5,-2,-1,10,8,-10,-6,-3,-7,2,-1,-9,10,5,-1,-10,7,-1,-3,-2,-1,-8,-3,-9,-7,2,-4,1,10,9,-8,2,-4,-4,3,8,6,1,8,-10,3,-2,-2,4,-9,-7,-3,-10,1,-4,10,10,-9,-7,-5,3,-8,8,8,-6,-4,-3,2,-5,-9,-7,2,-7,10,-9,1,-4,7,-1,-1,-5,9,-5,-3,-4,-1,3,10,-8,4,-7,9,3,1,-4,-2,1,-7,4,9,4,1,-5,9,-3,-1,7,-10,-8,6,-5,-3,10,3,1,4,-1,-5,5,-8,-9,9,-8,8,-1,-10,-3,-5,4,-8,1,10,-6,8,1,2,-6,-5,9,2,10,-6,-6,7,-10,-3,-9,-3,-10,-8,9,-10,-8,-9,10,7,-3,2,-4,7,8,-7,3,-3,10,-3,-1,4,-9,8,-2,9,8,5,2,9,2,-6,5,9,1,6,6,-3,3,-2,8,2,-3,-1,-9,-7,-4,7,2,-5,-7,-7,1,5,3,8,-1,9,-7,10,-9,-6,-10,2,-8,-5,8,-9,-9,-10,4,-6,-8,10,3,1,7,-7,-2,-8,-6,7,-2,10,1,-8,9,9,-8,3,8,-5,3,5,1,-4,-6,-10,7,2,1,10,-3,-7,9,4,6,-4,1,2,3,-8,9,9,-9,2,10,-2,-5,6,1,-9,1,-5,5,4,-5,6,2,10,6,-3,-7,3,-4,-4,-1,3,10,-4,-7,-2,-3,-8,4,6,1,-10,2,10,2,-2,-9,-5,-3,2,7,2,-2,5,-8,8,8,-10,1,8,-2,-10,-7,7,-4,-10,3,-3,4,-3,-8,-4,10,1,-1,-9,-1,-5,-4,8,3,2,-2,5,2,-8,10,9,5,-3,8,1,-1,-8,1,4,4,2,-1,-1,4,3,3,-3,-1,5,8,-9,-2,-5,-4,7,-3,5,-7,-6,8,-2,-3,-1,3,6,-4,2,5,-1,6,-7,8,-2,-10,3,-10,-1,1,-9,-8,8,3,7,9,5,5,-4,-5,7,7,-5,8,1,-10,6,9,-1,5,-10,-8,-2,8,8,-2,-1,9,-7,-4,6,1,3,7,-2,-3,-9,-7,4,6,-1,8,-9,-7,-4,5,4,-2,-5,10,1,8,-2,2,-10,-9,7,2,6,2,-8,-10,10,9,10,3,-1,-3,5,1,4,-8,-9,6,-8,3,-3,10,4,-1,7,8,-6,-2,-8,8,-3,10,-7,-7,-5,2,-5,3,10,-6,9,-8,4,-6,3,4,-2,-9,-1,3,9,3,-8,3,-2,6,2,-6,3,1,-8,3,-7,1,9,7,-1,-9,-9,-6,3,2,-5,-2,-2,4,7,-2,-10,-4,6,6,-2,-6,-9,-1,4,8,4,6,4,-6,7,-5,10,5,-3,-5,8,-7,2,1,-5,-5,-10,5,-1,7,10,5,5,7,-1,-4,-4,7,-3,3,-7,7,9,5,4,10,-4,-3,4,-9,-4,3,-6,-5,-9,6,-9,5,-4,10,10,9,4,5,4,5,6,8,-8,-10,-3,3,9,2,8,-9,-1,-4,-4,4,-2,-8,7,-8,-10,4,-7,5,-4,-7,-8,-1,-9,-5,4,1,-10,-2,-4,2,1,7,-4,3,-7,2,-9,6,8,8,-3,-5,7,-8,2,-5,7,-2,-2,10,-5,7,-3,-1,4,-2,10,8,9,-8,-7,3,-5,-6,7,-8,-6,8,6,4,-1,-7,-8,-8,-10,-5,1,2,2,-3,-3,3,6,3,-3,3,5,-6,-4,7,3,2,1,-2,-3,-4,-7,-10,-2,-8,9,-8,-3,7,-9,3,8,7,-1,-4,3,-5,-7,-5,7,4,5,2,6,-5,-4,8,6,-1,6,3,5,10,-2,-1,-8,-7,-8,-1,10,9,4,8,-5,-9,4,10,10,1,7,-1,10,-6,-8,-1,2,-2,9,10,-9,-7,-1,-4,1,2,-9,2,2,-8,-6,-9,-10,9,-1,5,6,-2,-1,7,-2,-1,-4,2,3,-6,-8,-7,6,-8,-5,-4,7,7,4,1,6,9,-4,-8,1,-6,-1,-7,-1,3,-8,-6,-4,-2,-10,6,-4,8,10,-5,-1,1,-3,8,-3,-7,-7,5,-7,-2,1,-3,-7,-3,6,-7,6,-1,-6,5,10,-2,7,10,6,1,2,-2,-4,3,10,10,-7,7,10,5,-5,6,-6,-6,-10,10,10,10,-5,-7,-4,3,6,9,3,5,-10,-10,9,9,-2,1,10,-7,8,-2,-10,8,-8,-3,10,10,1,6,-5,-9,-5,10,-4,10,2,-6,8,10,10,6,-3,10,4,6,-3,8,-7,-5,5,5,-9,10,5,-3,5,-3,-6,4,10,-1,5,3,8,-3,5,-8,8,-4,-10,-8,-6,3,5,-4,-9,10,-4,6,-2,3,-6,4,1,-7,-6,-5,-7,4,8,-6,3,-1,-10,-9,5,-2,4,-4,-5,-5,-7,3,9,-7,5,1,1,7,6,-4,7,-3,3,6,-10,10,1,3,-1,4,4,-6,-7,6,8,-6,7,5,-9,-9,4,-8,1,5,-2,9,-6,10,-9,-9,-6,1,-6,-3,-1,-4,10,-2,-3,-2,-7,2,-8,-7,9,-6,-4,-8,5,-5,-2,3,-3,2,9,-1,-6,10,-5,5,-6,1,-7,-2,8,1,8,-3,-7,7,10,-4,10,2,-4,3,7,-10,1,-7,1,1,1,10,-9,-8,4,-5,8,2,-6,2], dtype = "int16")#candidate|17916|(1274,)|const|int16
const_17917 = relay.const([1.610303,8.171349,-9.227116,-8.949345,-4.698917,-0.432056,-7.239276,-0.471245,-2.640947,0.806065,1.364680,2.535340,2.093958,3.794100,-9.162833,-6.402753,-3.742007,-1.377606,2.826027,5.648693,8.697170,7.104490,-4.699986,-0.948198,-0.102719,-2.259548,7.074328,-7.987195,-8.468462,9.973295,0.700432,-6.850547,7.811155,-5.828614,3.824550,-2.213750,7.934656,3.679619,1.591072,5.551801,5.503255,-6.233459,1.089237,4.495535,-7.057016,-2.978068,-7.356486,5.525685,2.798351,-4.171705,-8.587313,-1.139922,-7.664144,2.382068,2.762080,-5.343404,-7.649279,5.195473,2.197415,4.571845,4.870839,-8.392455,-0.714700,1.151352,1.112326,0.741104,7.736102,-2.920534,2.147796,9.489771,-2.439539,1.142614,-6.379406,-6.918803,0.771895,3.908854,8.617617,-6.186568,-1.102806,2.136477,-2.818174,7.688858,-6.020288,5.602277,5.544949,-9.011112,-9.795496,4.752239,-1.743384,6.695036,1.518314,-9.599577,-4.558865,1.147339,2.425507,-8.367642,8.077382,7.052758,1.613762,2.813259,6.832890,-5.505579,7.424345,5.412026,2.417214,3.038000,3.070372,2.011760,-3.920929,-8.189499,-5.108355,9.048635,-7.205333,0.704655,-1.032902,9.878099,8.880021,2.837195,1.559284,-8.088119,6.857929,2.866768,-1.313791,-1.305132,5.719677,-9.220781,-5.238966,8.003745,-7.835364,-6.553174,3.889777,-5.816976,-1.838076,4.069825,-4.625844,-7.176319,8.963104,8.881093,8.233853,5.235246,-8.228349,-4.253494,5.036917,-1.907524,-6.211673,-2.753477,-0.607058,-8.747809,0.904271,-0.952415,-9.931060,7.029373,-8.281917,8.457557,5.884290,9.076103,-7.597214,-8.710630,6.357197,2.203728,5.499551,-9.088300,-2.602157,-1.817918,-3.886688,-9.583770,-9.126541,6.452826,-3.545772,-8.552355,6.418902,8.819499,7.802135,3.679631,-6.759762,-7.680570,0.533669,1.159976,-2.074919,3.045772,-5.243918,6.182092,4.120287,-1.916055,5.900463,6.997096,-4.228243,-0.412896,-2.767636,-6.478960,-2.430727,9.440871,9.582437,3.222212,-1.925361,9.707598,-4.097180,5.818621,9.147642,6.653200,-3.320000,2.788327,-3.840440,-5.201059,1.314771,3.810366,-6.356892,8.813228,-7.817418,7.013945,7.810155,3.860908,2.169610,-6.547226,-5.704076,4.860083,-2.383297,9.187343,-2.927627,-9.147079,1.679645,9.265275,-6.259385,5.355407,5.351901,7.890877,8.569161,2.538071,-3.322119,4.448617,7.406548,6.336157,1.836958,-9.582843,4.959017,-9.500969,0.452069,-9.851839,-1.815750,-6.016773,-9.446255,3.017664,-0.530883,-7.861779,-8.791490,-0.962797,-4.906484,2.178225,-5.002463,6.965814,-1.318814,-8.437177,3.926391,9.944514,9.630835,7.232791,-0.472081,0.791892,1.370605,8.084802,-2.552783,-4.290266,6.485399,-4.564392,7.833702,8.219474,1.931936,6.759058,-8.029038,6.567710,-2.368543,1.524439,5.470237,-7.550590,-9.025315,-6.314212,8.584496,0.166460,-8.747396,-2.207893,5.129158,-8.711934,-3.405767,6.289436,-8.381367,-2.341745,-0.033201,5.859415,-6.976038,-6.005278,3.998473,2.208610,7.265724,-9.818517,6.889119,-8.844840,-2.215056,2.798135,-8.605676,-5.897624,1.042045,-9.419133,-4.609217,6.435849,7.178128,-5.766478,-7.139932,1.591159,-4.855410,-0.740912,-6.992003,0.135515,6.032438,3.899384,5.564865,-0.510771,-1.033368,-1.563263,5.501872,-1.880265,-1.827138,1.235456,-5.145021,-0.744301,-5.425964,-6.749140,2.147063,-5.620034,2.585022,8.564809,9.530682,3.127844,-7.574044,-7.207508,-4.896212,-6.395685,5.935860,6.742571,-2.644763,6.122103,-0.495828,8.097451,9.905404,-5.433804,-3.986010,0.135884,-6.052730,2.226590,7.731113,-3.453070,-3.387382,-5.443728,-3.321752,-6.719500,9.332865,-8.854688,9.499492,-4.602385,7.634412,7.490737,-9.188865,0.214809,-7.310048,2.224243,-4.711460,9.235668,-3.067728,8.006024,3.172664,9.182247,4.949559,1.144821,2.318990,7.848418,-4.706948,-6.466741,7.803026,6.565656,8.646891,2.539425,-7.769079,-8.772853,-1.375101,-9.312493,8.226551,7.524572,6.567786,-2.426567,-8.997740,8.427831], dtype = "float64")#candidate|17917|(390,)|const|float64
var_17918 = relay.var("var_17918", dtype = "uint32", shape = (63,))#candidate|17918|(63,)|var|uint32
call_17915 = relay.TupleGetItem(func_11127_call(relay.reshape(const_17916.astype('int16'), [14, 7, 13]), relay.reshape(const_17916.astype('int16'), [14, 7, 13]), relay.reshape(const_17917.astype('float64'), [195, 2]), relay.reshape(var_17918.astype('uint32'), [63,]), ), 1)
call_17919 = relay.TupleGetItem(func_11133_call(relay.reshape(const_17916.astype('int16'), [14, 7, 13]), relay.reshape(const_17916.astype('int16'), [14, 7, 13]), relay.reshape(const_17917.astype('float64'), [195, 2]), relay.reshape(var_17918.astype('uint32'), [63,]), ), 1)
output = relay.Tuple([call_17910,call_17915,const_17916,const_17917,var_17918,])
output2 = relay.Tuple([call_17911,call_17919,const_17916,const_17917,var_17918,])
func_17920 = relay.Function([var_17918,], output)
mod['func_17920'] = func_17920
mod = relay.transform.InferType()(mod)
mutated_mod['func_17920'] = func_17920
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17921 = relay.var("var_17921", dtype = "uint32", shape = (63,))#candidate|17921|(63,)|var|uint32
func_17920_call = mutated_mod.get_global_var('func_17920')
call_17922 = func_17920_call(var_17921)
output = call_17922
func_17923 = relay.Function([var_17921], output)
mutated_mod['func_17923'] = func_17923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17297_call = mod.get_global_var('func_17297')
func_17298_call = mutated_mod.get_global_var('func_17298')
call_17931 = relay.TupleGetItem(func_17297_call(), 0)
call_17932 = relay.TupleGetItem(func_17298_call(), 0)
uop_17938 = relay.erf(call_17931.astype('float64')) # shape=(65, 9)
uop_17940 = relay.erf(call_17932.astype('float64')) # shape=(65, 9)
func_13260_call = mod.get_global_var('func_13260')
func_13263_call = mutated_mod.get_global_var('func_13263')
var_17948 = relay.var("var_17948", dtype = "uint16", shape = (1024,))#candidate|17948|(1024,)|var|uint16
call_17947 = relay.TupleGetItem(func_13260_call(relay.reshape(var_17948.astype('uint16'), [1024,])), 0)
call_17949 = relay.TupleGetItem(func_13263_call(relay.reshape(var_17948.astype('uint16'), [1024,])), 0)
output = relay.Tuple([uop_17938,call_17947,var_17948,])
output2 = relay.Tuple([uop_17940,call_17949,var_17948,])
func_17968 = relay.Function([var_17948,], output)
mod['func_17968'] = func_17968
mod = relay.transform.InferType()(mod)
var_17969 = relay.var("var_17969", dtype = "uint16", shape = (1024,))#candidate|17969|(1024,)|var|uint16
output = func_17968(var_17969)
func_17970 = relay.Function([var_17969], output)
mutated_mod['func_17970'] = func_17970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17480_call = mod.get_global_var('func_17480')
func_17482_call = mutated_mod.get_global_var('func_17482')
call_17988 = func_17480_call()
call_17989 = func_17480_call()
output = relay.Tuple([call_17988,])
output2 = relay.Tuple([call_17989,])
func_18013 = relay.Function([], output)
mod['func_18013'] = func_18013
mod = relay.transform.InferType()(mod)
mutated_mod['func_18013'] = func_18013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18013_call = mutated_mod.get_global_var('func_18013')
call_18014 = func_18013_call()
output = call_18014
func_18015 = relay.Function([], output)
mutated_mod['func_18015'] = func_18015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15200_call = mod.get_global_var('func_15200')
func_15201_call = mutated_mod.get_global_var('func_15201')
call_18020 = relay.TupleGetItem(func_15200_call(), 0)
call_18021 = relay.TupleGetItem(func_15201_call(), 0)
output = call_18020
output2 = call_18021
func_18027 = relay.Function([], output)
mod['func_18027'] = func_18027
mod = relay.transform.InferType()(mod)
mutated_mod['func_18027'] = func_18027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18027_call = mutated_mod.get_global_var('func_18027')
call_18028 = func_18027_call()
output = call_18028
func_18029 = relay.Function([], output)
mutated_mod['func_18029'] = func_18029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17047_call = mod.get_global_var('func_17047')
func_17048_call = mutated_mod.get_global_var('func_17048')
call_18054 = relay.TupleGetItem(func_17047_call(), 1)
call_18055 = relay.TupleGetItem(func_17048_call(), 1)
output = call_18054
output2 = call_18055
func_18087 = relay.Function([], output)
mod['func_18087'] = func_18087
mod = relay.transform.InferType()(mod)
mutated_mod['func_18087'] = func_18087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18087_call = mutated_mod.get_global_var('func_18087')
call_18088 = func_18087_call()
output = call_18088
func_18089 = relay.Function([], output)
mutated_mod['func_18089'] = func_18089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18146 = relay.var("var_18146", dtype = "float32", shape = (15, 6, 4))#candidate|18146|(15, 6, 4)|var|float32
uop_18147 = relay.sqrt(var_18146.astype('float32')) # shape=(15, 6, 4)
func_16303_call = mod.get_global_var('func_16303')
func_16305_call = mutated_mod.get_global_var('func_16305')
call_18151 = func_16303_call()
call_18152 = func_16303_call()
output = relay.Tuple([uop_18147,call_18151,])
output2 = relay.Tuple([uop_18147,call_18152,])
func_18164 = relay.Function([var_18146,], output)
mod['func_18164'] = func_18164
mod = relay.transform.InferType()(mod)
mutated_mod['func_18164'] = func_18164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18165 = relay.var("var_18165", dtype = "float32", shape = (15, 6, 4))#candidate|18165|(15, 6, 4)|var|float32
func_18164_call = mutated_mod.get_global_var('func_18164')
call_18166 = func_18164_call(var_18165)
output = call_18166
func_18167 = relay.Function([var_18165], output)
mutated_mod['func_18167'] = func_18167
mutated_mod = relay.transform.InferType()(mutated_mod)
const_18212 = relay.const([[[-5.455174],[-9.421730],[-1.084360],[3.919154],[5.936391],[-1.924974],[-6.366773],[7.358154],[-2.427794],[-0.775227],[4.906898],[-1.911941],[-1.084167],[-6.183191]],[[7.795928],[-6.646492],[-5.516310],[4.690314],[-5.887413],[6.492344],[2.648752],[3.499945],[-5.099755],[2.212603],[-5.396899],[-2.265534],[-2.261127],[-4.250238]],[[9.434268],[-9.650574],[-1.933914],[-6.909362],[0.066383],[7.588447],[-9.224183],[4.792845],[6.480284],[-5.910125],[9.577392],[-8.068355],[5.511945],[-1.110851]],[[-8.709078],[-7.416396],[1.449539],[-0.378844],[4.720610],[-1.425102],[-8.710807],[-3.885340],[9.849269],[8.979162],[-1.108251],[-0.565075],[5.623533],[-7.148698]]], dtype = "float64")#candidate|18212|(4, 14, 1)|const|float64
uop_18213 = relay.exp(const_18212.astype('float64')) # shape=(4, 14, 1)
func_13178_call = mod.get_global_var('func_13178')
func_13180_call = mutated_mod.get_global_var('func_13180')
call_18215 = relay.TupleGetItem(func_13178_call(), 2)
call_18216 = relay.TupleGetItem(func_13180_call(), 2)
func_11215_call = mod.get_global_var('func_11215')
func_11219_call = mutated_mod.get_global_var('func_11219')
const_18222 = relay.const([[5.425042,6.473191,0.212016,2.234302,7.072466,9.907387,6.478578,1.951056,-5.699056,7.600718,7.767675,4.276624,-2.255327,-4.077240,1.834379,-4.669591,-9.654956,6.704171,-6.915329,5.823963,9.206645,4.074576,-6.872641,0.960196,0.363245,2.930710,6.927510,-4.807064,3.176830,-3.216747,-4.232800,-8.636602,-5.558437,-5.389211,-7.078375,-4.289832,-3.364697,9.435092,-3.387255,2.789404,2.899589,-6.099118,-2.629401,-6.670545,-6.618875],[-2.528602,0.636347,3.788214,-2.032170,-9.824601,2.180338,-5.875663,-6.060552,-1.618374,-4.679007,-8.259639,5.975617,-8.479932,-6.920658,8.844934,0.498796,0.077271,-1.891565,-0.250978,-8.470350,-6.525588,-0.156331,4.055874,-3.537051,3.605428,-9.977505,-1.515823,0.497596,4.176309,1.399723,-0.619611,-8.368475,6.272767,-1.292045,1.468318,-1.623947,-6.894656,-9.660964,3.718417,-0.152943,1.064149,-6.270521,-9.038464,8.019195,6.721242],[-1.241347,4.500629,2.584454,-6.507784,2.105293,-8.453327,8.507815,-6.142290,4.360847,-3.145926,-3.065580,-6.740414,4.021803,-2.860094,-6.745606,6.501468,1.176483,2.002975,1.263271,-5.267924,6.726129,-3.754765,-2.602809,-6.135073,-7.642211,6.751629,-1.663903,2.502481,-7.303782,-1.098947,-6.365571,3.340040,0.357257,-4.238266,-2.403035,4.252744,-8.505513,-7.203291,-8.590983,-4.023606,0.463907,7.916224,8.037907,0.302850,0.173925],[-1.250793,4.912968,3.817198,-4.843664,2.500450,3.950863,-5.831832,-9.461307,-8.670269,6.707457,2.419005,-6.214614,-3.815346,-8.339255,7.106707,-0.545264,3.173573,8.107567,-1.916443,-0.723355,5.170720,-0.902700,4.828660,-5.350381,5.166355,-2.053005,4.088357,2.532465,-5.484680,5.564891,4.490881,2.018592,-6.862833,-1.107845,-3.997925,-4.858570,-2.817471,4.834081,-6.021309,1.166708,8.434164,-3.236314,-0.085116,0.450069,6.286732],[-4.197458,-4.852830,0.179316,-7.147092,9.693076,3.418577,-9.592900,-9.893961,9.615970,-2.809390,-4.958404,9.929695,-9.755251,-6.728099,-6.983428,-0.912063,1.185066,1.098929,9.672164,-7.723468,-0.800966,0.053075,1.559856,2.372137,-6.366495,9.854382,1.611896,2.758720,-9.191037,8.792190,-8.587630,8.364828,-6.016189,-3.323205,-8.822924,-7.536985,-0.936548,-1.559963,8.254688,7.604598,7.668426,-7.082684,3.568153,-1.847452,-5.234706],[-3.279329,7.893001,-0.901266,-7.750869,-6.354364,6.270727,-5.689642,-0.203377,2.507675,-7.011369,5.522305,5.653123,-8.963299,9.185134,-9.030185,1.625066,-8.688945,-6.420825,-4.259454,-0.063856,6.771184,-0.155853,8.124182,-0.001302,-0.161074,4.020012,-3.257754,-8.808263,2.052033,2.800837,9.122057,3.133689,-2.078935,-8.470607,-6.575270,3.087868,-8.454647,1.619415,-3.575168,-3.218786,-5.099371,-6.018779,-4.466873,-3.423996,-5.259706],[1.172909,-2.243872,-3.431731,-4.485334,9.331401,8.417584,-6.672526,-1.648779,1.688177,-9.165824,-2.752386,-5.262594,7.258420,0.977393,-6.016703,-7.865453,6.924981,-9.215792,7.431541,-9.644073,-8.664911,3.618963,5.243235,-2.113202,-0.425854,-9.443664,-5.575741,4.193060,9.309247,7.283072,-8.317128,8.018052,-4.801428,9.665993,-4.794996,-7.766670,8.166151,7.380989,-9.780571,-3.604351,-0.923712,7.951171,3.835902,7.008658,8.825311],[-4.647746,-4.020391,1.502133,-3.205527,-4.368892,-3.500894,8.319863,-0.395429,-3.807417,-6.311473,8.205868,5.766667,8.565214,5.418335,0.264018,0.230477,-6.347091,1.702534,-9.961352,6.608996,-4.439244,-0.973591,6.881057,-5.038733,0.646345,-8.727325,-6.858788,0.462124,-5.271639,-9.156819,5.608393,-5.680999,9.764333,8.098929,6.635023,-3.068953,-7.354313,2.957533,7.445948,0.099629,-0.589526,0.173364,1.855170,6.808506,3.908943],[6.663979,3.648260,-0.170040,3.030620,0.118361,-6.914667,-8.733734,-1.765514,5.224858,3.654565,-3.664374,-5.887040,-6.371324,-3.442772,-3.617637,1.867841,-0.243957,0.223209,2.552993,-3.526551,6.936613,-4.846937,2.666971,3.234711,-1.443420,5.810477,-7.188109,-5.108866,5.019644,-2.685735,-8.709320,8.344033,5.880472,-4.554402,6.955060,8.624028,1.849938,-5.807465,-1.578654,8.230470,-8.385558,9.715580,1.121346,-6.522566,-6.159270],[-8.087122,-0.352509,2.613252,-4.162085,1.768377,-8.995394,-1.978430,-7.129149,-3.351758,-6.349096,-4.828480,-7.040383,4.373820,6.664070,-6.029359,5.785037,9.213018,-3.459641,9.973802,-1.076192,-0.125826,6.865122,-9.280271,9.724749,-5.482131,7.359918,-7.494237,-5.674175,3.492268,7.900227,7.260695,-5.235163,0.200378,7.449877,5.702488,1.706831,-0.121145,-6.330327,-0.575826,7.877451,0.356804,9.554312,-0.321893,9.997822,-8.834739],[2.725028,9.764539,-0.543177,-0.643504,8.767811,3.370632,2.039388,9.576788,-1.698666,9.687074,-9.607773,-7.434660,-0.986641,8.571546,-2.265838,7.103769,3.960356,6.312358,7.830448,5.007533,4.404397,4.716034,-0.550209,-6.602915,-0.108524,-1.280074,-8.395007,4.954859,6.874746,2.374968,-0.635742,9.052233,6.235658,7.289892,-6.845669,-5.612899,2.153980,-9.207217,-9.001149,-5.584451,-4.121727,-8.623926,-9.904115,-7.220945,-3.920670],[1.765924,-0.403231,7.267849,-7.375946,-1.196329,4.652070,-3.542738,-7.813764,7.358201,-8.817441,0.018390,-0.766088,7.802889,4.635464,5.684730,3.980121,-9.245625,0.388266,-2.417671,-6.616116,5.708008,9.960571,-5.674431,-7.366187,-3.180741,-7.572352,-9.712204,3.314730,2.318389,6.919775,4.222750,4.947260,-7.929092,2.317965,-1.270567,2.216336,0.931447,-0.807246,-6.454031,5.642089,7.502081,-3.437383,8.819857,5.706442,7.589045],[7.454579,-3.258402,-0.201502,1.650528,0.790941,-4.235700,3.594287,4.602666,7.465574,4.872585,-4.200769,-2.640066,-7.768645,0.221364,-0.241545,-3.388353,7.808222,4.347909,5.947397,8.534320,-2.049216,7.948574,7.797593,4.198658,-5.371382,-9.697859,0.193319,6.063296,-1.879379,-3.522607,1.943210,-3.793794,5.826666,9.343867,-0.990845,3.540864,-6.157173,9.252142,1.312183,-8.294927,8.862569,-6.367941,-8.785847,-6.979508,-1.847947],[5.133069,1.236409,-3.991972,3.650544,2.546026,-2.838793,2.623291,9.227046,7.176383,9.976024,-5.867656,-7.596208,-5.214608,-7.307741,2.945383,2.326585,7.079580,-1.320857,7.216322,8.642543,5.851620,9.450022,-3.362622,9.080013,6.272610,4.559625,8.738421,-1.260321,-7.944944,-4.210418,-0.070224,8.821785,-7.932480,0.487939,2.433776,-6.768293,3.671533,7.625686,-5.133297,6.977220,-4.569329,1.886230,-7.417677,7.833690,2.192770],[-7.258485,5.238548,0.997761,5.556886,1.046597,7.989413,6.158812,1.514230,-1.463942,-8.386853,3.588241,-0.483509,-9.192357,-5.736694,-3.803939,-3.164182,8.008713,-1.142907,3.907110,-1.738578,-2.975634,6.845192,-5.126089,2.602780,-5.695940,-4.202177,-9.493945,4.806002,6.796276,-3.846097,7.540627,-7.826297,-3.912896,9.991165,-7.016372,-2.939115,1.862549,-1.548948,-3.306966,-9.167270,5.338570,-4.502512,3.144900,1.823791,3.023084],[-9.259664,-7.293773,-9.911478,5.363935,-7.489455,6.353154,6.529668,-9.159658,-1.794553,4.632765,-2.323701,8.880369,-2.619394,-9.355982,4.232873,9.018266,-8.184385,-0.445657,-2.819687,-8.555635,2.381379,0.913757,-8.647644,-6.265011,-8.536796,6.151022,9.571409,6.177576,2.345121,0.776133,4.305312,9.012489,-5.277101,-3.447431,4.363459,5.784930,-3.373178,5.968888,3.818135,3.035822,4.498279,-3.969974,6.454885,-4.024934,2.118622],[1.696394,-3.173983,-0.631202,-0.679266,0.406499,9.693623,-4.146976,5.527897,-1.508461,-3.374480,-5.152635,-5.727934,-8.764399,-0.447712,-9.375563,-5.248804,1.878520,-5.549721,2.183822,-1.752565,8.598578,7.611800,-8.956964,0.809537,8.537559,-2.908687,-4.890856,-6.171183,5.566560,1.164940,-5.215732,5.547747,6.460939,0.415246,1.053336,4.395041,3.349459,-2.130114,-2.023448,-6.002009,0.799387,5.126712,3.123566,-6.792766,9.659230],[3.181868,2.285276,6.955383,-3.628157,8.421100,-9.913071,-4.073579,-6.765967,8.749970,7.905080,-5.179156,0.811583,-4.470319,-7.040484,6.529780,-7.061350,9.137259,9.233512,-5.715742,-7.579618,2.790457,0.662570,-8.034050,2.298318,-0.024431,-9.594040,3.130208,-7.329577,-1.701729,1.897954,-2.009111,-2.850570,3.110549,-5.486759,-8.875575,-7.705334,-6.009326,0.097560,3.404907,-3.309068,5.416371,-7.904656,-6.483227,-5.678280,9.918125],[-8.242080,-5.685107,-6.618619,5.680459,5.963850,5.804446,4.771265,0.762194,-9.760459,3.733758,-0.831685,8.478678,-1.586547,-6.718757,4.894274,-9.145000,2.288456,-1.266563,-7.697113,8.683687,9.498171,3.093174,-8.740279,-0.268962,1.406896,5.449467,-2.419642,8.331598,8.286641,-1.286605,1.640736,-2.422163,7.022997,-1.779993,-3.218085,2.017831,-9.929250,5.667095,-0.180486,-0.930096,2.678819,7.748953,-1.063879,-6.079742,-0.873997],[-7.323467,1.038311,2.005974,-0.990290,2.565585,4.848388,-0.793967,2.716053,-1.196340,9.836315,-7.792173,-9.641082,1.437952,-2.092933,-9.144549,-8.783371,-2.577650,-9.436555,-3.310735,-9.694530,2.022062,-1.183012,8.179294,8.286251,0.475095,-8.180804,-6.269169,-8.764357,-4.528034,0.493478,9.512831,2.484535,-3.563181,2.112846,-5.447253,-9.204773,1.052330,-6.539543,-6.725193,-0.679947,-8.430815,4.096107,-5.145215,-7.143582,-9.033389],[6.352020,9.445927,-7.879503,-9.568506,-6.798056,5.411960,1.083013,-6.129982,2.022542,9.117446,-9.666246,4.292658,-6.619965,8.525129,-5.233363,0.680999,-7.512456,-3.555580,-2.248709,-5.360637,-7.515724,7.105110,1.136476,9.640227,-0.939406,-4.620159,-2.040864,8.297794,3.143957,-0.740940,-8.630813,-2.575321,-1.000599,2.573502,3.616346,-5.186860,1.509255,0.717355,0.207452,-0.354498,-1.909023,-8.372292,-6.706190,8.500048,7.443380],[1.911764,1.905064,-1.426377,-8.018901,-5.629695,5.954832,1.654414,-6.705078,8.457506,2.416143,-0.803374,6.561950,6.672348,-8.887345,0.506758,-8.967234,6.055617,-0.301385,1.812699,-0.296833,9.407016,-7.069326,-0.953725,3.727155,-7.416394,5.342521,-2.616558,-8.146427,-5.842918,9.125664,-3.641239,-3.286716,0.138788,7.443671,-4.788156,9.261430,3.637586,-2.010514,-4.805327,-6.121405,3.293160,4.314213,-4.885196,8.443567,-0.991693],[-2.493725,-3.089450,1.112905,-0.550937,-0.919544,-7.514814,-5.314168,-9.275841,7.809543,-4.842412,7.419496,-4.853409,-6.636125,-1.248890,4.713960,-7.666837,3.272295,3.466135,-3.117144,7.930970,-5.301173,-7.766949,-6.238173,9.654173,-5.070787,5.805196,1.297053,-6.946341,-2.054196,2.318872,-9.583214,4.116128,-3.525717,-0.427994,-6.516470,-9.156553,8.296152,8.940845,0.199998,2.020325,2.726734,1.805194,-1.573032,-0.463575,2.924924],[8.944216,0.387434,3.081447,4.659503,-6.495301,-0.990783,-9.425031,-3.209072,5.773794,-5.791465,7.311090,0.034888,1.777385,-7.464872,-8.875311,6.144141,1.606616,-3.238404,4.841096,-9.189210,-0.684758,-4.389743,-4.725233,-5.507635,-8.364391,3.267638,-5.794336,-7.692062,-8.782313,5.641605,-0.816965,-7.563818,7.215395,6.729995,-9.268704,9.789189,-5.465674,2.357145,-5.188976,-4.531609,3.867431,-6.823024,-0.337338,7.205391,4.962446],[7.945065,3.781553,-7.158149,-6.910319,8.087291,0.453193,2.604467,-0.808398,9.091502,5.630871,9.973422,0.864980,-1.561280,4.485112,-9.419973,9.642072,-5.007470,-4.488053,6.018155,-2.280343,4.959304,4.873970,2.582582,-1.586710,-1.260306,-0.412274,-8.445685,7.448711,9.782655,-5.903992,-9.635666,2.865475,-7.302642,4.104050,0.232468,3.576686,6.763594,8.550663,-6.810261,0.256696,3.421390,8.421842,1.128578,6.015190,0.050137],[6.861300,5.810514,-4.165076,-3.199732,6.959575,-1.155371,-7.979457,-0.571932,-2.719325,9.019781,9.832283,-4.010872,-2.896492,-8.825259,-3.569844,8.877371,8.118888,0.970159,4.119975,3.456036,3.598422,7.215552,0.320713,6.838860,-4.609100,-5.208655,-1.961323,-6.074001,-7.518039,-9.899741,-5.757317,-5.725290,-0.372297,-0.148299,0.050092,-4.291004,0.532562,9.824401,1.587750,-0.752962,9.834131,-7.100247,1.083690,0.383759,3.457726],[7.035187,2.514606,3.083546,4.632166,1.791267,4.163378,4.656931,3.787719,1.166395,1.471765,6.280407,-5.350934,-5.558693,-8.468690,-9.935031,1.771830,-4.965090,3.570787,-3.280076,4.460669,-5.126106,-1.166769,5.260598,-6.019795,-8.293747,-0.308614,-2.719727,0.026743,3.629738,-1.900642,2.668799,1.351272,7.460934,3.774826,6.768952,5.650574,1.228632,8.140494,-9.924647,-3.650786,8.483368,-7.249676,5.691608,9.946111,6.274432]], dtype = "float32")#candidate|18222|(27, 45)|const|float32
call_18221 = relay.TupleGetItem(func_11215_call(relay.reshape(const_18222.astype('float32'), [15, 9, 9]), relay.reshape(call_18215.astype('int8'), [55, 10]), ), 2)
call_18223 = relay.TupleGetItem(func_11219_call(relay.reshape(const_18222.astype('float32'), [15, 9, 9]), relay.reshape(call_18215.astype('int8'), [55, 10]), ), 2)
output = relay.Tuple([uop_18213,call_18215,call_18221,const_18222,])
output2 = relay.Tuple([uop_18213,call_18216,call_18223,const_18222,])
func_18225 = relay.Function([], output)
mod['func_18225'] = func_18225
mod = relay.transform.InferType()(mod)
mutated_mod['func_18225'] = func_18225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18225_call = mutated_mod.get_global_var('func_18225')
call_18226 = func_18225_call()
output = call_18226
func_18227 = relay.Function([], output)
mutated_mod['func_18227'] = func_18227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15200_call = mod.get_global_var('func_15200')
func_15201_call = mutated_mod.get_global_var('func_15201')
call_18312 = relay.TupleGetItem(func_15200_call(), 0)
call_18313 = relay.TupleGetItem(func_15201_call(), 0)
output = call_18312
output2 = call_18313
func_18332 = relay.Function([], output)
mod['func_18332'] = func_18332
mod = relay.transform.InferType()(mod)
output = func_18332()
func_18333 = relay.Function([], output)
mutated_mod['func_18333'] = func_18333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17232_call = mod.get_global_var('func_17232')
func_17234_call = mutated_mod.get_global_var('func_17234')
call_18336 = relay.TupleGetItem(func_17232_call(), 0)
call_18337 = relay.TupleGetItem(func_17234_call(), 0)
func_12368_call = mod.get_global_var('func_12368')
func_12370_call = mutated_mod.get_global_var('func_12370')
call_18352 = relay.TupleGetItem(func_12368_call(), 0)
call_18353 = relay.TupleGetItem(func_12370_call(), 0)
func_15095_call = mod.get_global_var('func_15095')
func_15097_call = mutated_mod.get_global_var('func_15097')
call_18359 = relay.TupleGetItem(func_15095_call(), 1)
call_18360 = relay.TupleGetItem(func_15097_call(), 1)
output = relay.Tuple([call_18336,call_18352,call_18359,])
output2 = relay.Tuple([call_18337,call_18353,call_18360,])
func_18373 = relay.Function([], output)
mod['func_18373'] = func_18373
mod = relay.transform.InferType()(mod)
output = func_18373()
func_18374 = relay.Function([], output)
mutated_mod['func_18374'] = func_18374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12234_call = mod.get_global_var('func_12234')
func_12235_call = mutated_mod.get_global_var('func_12235')
call_18445 = relay.TupleGetItem(func_12234_call(), 0)
call_18446 = relay.TupleGetItem(func_12235_call(), 0)
func_6067_call = mod.get_global_var('func_6067')
func_6073_call = mutated_mod.get_global_var('func_6073')
var_18469 = relay.var("var_18469", dtype = "uint16", shape = (1024,))#candidate|18469|(1024,)|var|uint16
var_18470 = relay.var("var_18470", dtype = "float32", shape = (210, 3))#candidate|18470|(210, 3)|var|float32
call_18468 = relay.TupleGetItem(func_6067_call(relay.reshape(var_18469.astype('uint16'), [16, 4, 16]), relay.reshape(var_18469.astype('uint16'), [16, 4, 16]), relay.reshape(var_18470.astype('float32'), [70, 9]), relay.reshape(var_18469.astype('bool'), [16, 4, 16]), ), 2)
call_18471 = relay.TupleGetItem(func_6073_call(relay.reshape(var_18469.astype('uint16'), [16, 4, 16]), relay.reshape(var_18469.astype('uint16'), [16, 4, 16]), relay.reshape(var_18470.astype('float32'), [70, 9]), relay.reshape(var_18469.astype('bool'), [16, 4, 16]), ), 2)
output = relay.Tuple([call_18445,call_18468,var_18469,var_18470,])
output2 = relay.Tuple([call_18446,call_18471,var_18469,var_18470,])
func_18480 = relay.Function([var_18469,var_18470,], output)
mod['func_18480'] = func_18480
mod = relay.transform.InferType()(mod)
var_18481 = relay.var("var_18481", dtype = "uint16", shape = (1024,))#candidate|18481|(1024,)|var|uint16
var_18482 = relay.var("var_18482", dtype = "float32", shape = (210, 3))#candidate|18482|(210, 3)|var|float32
output = func_18480(var_18481,var_18482,)
func_18483 = relay.Function([var_18481,var_18482,], output)
mutated_mod['func_18483'] = func_18483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13739_call = mod.get_global_var('func_13739')
func_13740_call = mutated_mod.get_global_var('func_13740')
call_18497 = func_13739_call()
call_18498 = func_13739_call()
func_13178_call = mod.get_global_var('func_13178')
func_13180_call = mutated_mod.get_global_var('func_13180')
call_18514 = relay.TupleGetItem(func_13178_call(), 0)
call_18515 = relay.TupleGetItem(func_13180_call(), 0)
output = relay.Tuple([call_18497,call_18514,])
output2 = relay.Tuple([call_18498,call_18515,])
func_18522 = relay.Function([], output)
mod['func_18522'] = func_18522
mod = relay.transform.InferType()(mod)
mutated_mod['func_18522'] = func_18522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18522_call = mutated_mod.get_global_var('func_18522')
call_18523 = func_18522_call()
output = call_18523
func_18524 = relay.Function([], output)
mutated_mod['func_18524'] = func_18524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17547_call = mod.get_global_var('func_17547')
func_17548_call = mutated_mod.get_global_var('func_17548')
call_18547 = relay.TupleGetItem(func_17547_call(), 1)
call_18548 = relay.TupleGetItem(func_17548_call(), 1)
func_12999_call = mod.get_global_var('func_12999')
func_13000_call = mutated_mod.get_global_var('func_13000')
call_18587 = func_12999_call()
call_18588 = func_12999_call()
func_13534_call = mod.get_global_var('func_13534')
func_13536_call = mutated_mod.get_global_var('func_13536')
call_18593 = func_13534_call()
call_18594 = func_13534_call()
output = relay.Tuple([call_18547,call_18587,call_18593,])
output2 = relay.Tuple([call_18548,call_18588,call_18594,])
func_18603 = relay.Function([], output)
mod['func_18603'] = func_18603
mod = relay.transform.InferType()(mod)
mutated_mod['func_18603'] = func_18603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18603_call = mutated_mod.get_global_var('func_18603')
call_18604 = func_18603_call()
output = call_18604
func_18605 = relay.Function([], output)
mutated_mod['func_18605'] = func_18605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17138_call = mod.get_global_var('func_17138')
func_17140_call = mutated_mod.get_global_var('func_17140')
call_18651 = relay.TupleGetItem(func_17138_call(), 0)
call_18652 = relay.TupleGetItem(func_17140_call(), 0)
output = relay.Tuple([call_18651,])
output2 = relay.Tuple([call_18652,])
func_18664 = relay.Function([], output)
mod['func_18664'] = func_18664
mod = relay.transform.InferType()(mod)
mutated_mod['func_18664'] = func_18664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18664_call = mutated_mod.get_global_var('func_18664')
call_18665 = func_18664_call()
output = call_18665
func_18666 = relay.Function([], output)
mutated_mod['func_18666'] = func_18666
mutated_mod = relay.transform.InferType()(mutated_mod)
const_18678 = relay.const([[[7.346756,2.500913,-5.311394,3.023053,-0.894325,-1.698874,-8.737567,1.357650,-1.872949,-0.817781,-1.444639,1.306825,5.033356,-6.225091,-0.182923],[-9.081022,-5.416762,-8.533648,8.597287,-5.520007,-3.380253,3.338341,0.885640,9.762912,5.879372,3.843913,-5.451724,-1.847447,-3.725377,-4.614174],[-8.127877,-0.603334,-3.142403,6.491522,-1.331393,6.677090,6.218297,7.054216,-0.591995,-3.631497,6.111997,4.246822,9.547272,9.019937,-6.886283],[-3.624686,-1.061458,2.965423,-4.109071,-6.495899,-7.349418,3.532466,1.142896,-4.983971,0.219366,6.501764,1.500355,5.974295,-4.492726,-4.788052]],[[-4.425667,8.351607,-4.146601,-1.775614,-5.390136,5.515497,-1.449091,-6.263620,-5.661517,1.515010,1.113352,-0.092049,-0.079991,3.260986,-9.813550],[4.436444,1.441322,1.787398,-1.654484,-9.274978,-2.128596,5.076874,-3.378918,-5.805715,8.566804,7.141884,-5.624227,7.891406,4.138366,8.603539],[-8.770564,-1.431121,-0.379120,9.380401,2.013797,2.290131,-4.630984,2.288517,-4.543890,5.319028,8.457551,-1.882129,-2.071847,-2.412172,8.585305],[1.694855,2.351355,8.327966,9.736021,-7.713185,-5.842327,-1.264489,-0.342634,8.203075,-7.632726,-3.895054,8.879358,7.051962,-6.792418,1.348635]],[[-6.689182,-5.493200,0.510480,6.303784,-8.722978,5.890068,9.760662,6.076193,2.073926,-8.727704,9.260096,-2.072631,2.687444,-6.877814,5.313395],[3.834236,-9.253242,0.044952,6.033322,-6.873097,-1.058378,-2.794758,-5.290861,-6.708834,3.475197,0.068404,8.063236,8.356372,6.860985,5.747363],[-3.918838,-1.355144,-5.774056,-1.417859,-9.878845,2.388469,-8.583041,-0.864774,-2.551836,5.101539,1.911440,-8.607172,-8.444481,-1.469360,-7.061334],[-3.753021,-3.112676,6.164535,9.158997,4.999931,1.251796,-9.788215,-3.940786,-4.391190,6.534169,-4.077439,-2.893391,-1.015798,4.203880,-3.163003]],[[-2.315970,-9.585358,-2.643984,1.021804,6.520300,4.612133,9.287193,-7.428176,5.100246,-9.551093,-0.295903,0.958359,-1.658606,1.668718,-9.681275],[8.203687,7.364883,-0.053064,3.220827,7.280129,-9.563354,2.194419,-0.206688,1.945970,-4.832924,5.827226,2.169982,0.169546,-9.075720,4.831458],[3.926378,5.192700,-6.192072,-2.822854,5.764883,-9.561488,-9.525813,2.007450,5.374336,-4.295213,2.655169,8.870083,3.362731,-8.890655,7.658242],[-7.735006,-4.454411,3.004162,5.783961,-5.068394,6.728930,-7.509567,0.336906,1.218752,8.129467,-1.820251,0.744486,4.113635,1.881123,-4.271111]],[[9.897063,8.813561,-3.949894,-3.148395,-8.761099,-0.674034,0.226856,8.626016,-2.795316,7.209847,2.767818,-2.298238,5.802515,0.742634,3.999407],[-2.359705,-7.445491,-6.847720,-4.386056,2.438741,-6.306409,5.411123,-7.631395,-5.515996,0.548618,-4.903553,6.893378,1.489788,-7.938287,5.794427],[-4.270089,-1.437895,5.391278,6.099586,5.613840,-6.498920,-0.186799,8.764540,9.117847,5.939400,-9.760106,3.745065,5.471783,-0.771767,1.191998],[6.614402,2.496159,-4.391202,9.170875,6.725943,-7.138127,-9.764406,2.817218,-6.835885,2.248249,3.770487,5.245977,9.578147,4.073047,3.052337]],[[-2.155965,-1.836647,-2.264449,-7.644807,-1.563162,5.314033,-1.139465,2.926494,7.120093,-7.955151,0.532655,-6.022806,-4.441143,9.799942,-9.520788],[-9.038207,-0.876145,-7.783044,0.984393,-4.030160,-7.924143,2.729034,4.795105,-3.352462,-3.717461,5.279846,-5.612189,-3.363053,4.554115,-2.912563],[-2.428477,-6.125347,9.676317,-4.441067,-0.353727,-2.321129,-5.009517,8.142885,-5.438954,-3.080712,-4.327885,3.486579,-7.687600,7.197882,8.589187],[0.050298,-3.600001,-1.093345,-5.436029,-3.931066,2.744948,-9.396805,-7.059223,2.298232,3.709650,2.112066,7.749160,0.257945,3.764212,-3.283220]],[[-8.164488,-2.458483,0.459944,9.492644,1.938915,-6.628476,-1.766765,-6.941179,-9.852931,-6.832389,-2.429823,6.314580,-1.027342,0.747088,7.957605],[-2.034280,1.387543,-7.007483,-0.817506,-4.627522,-6.742662,-1.647771,2.435177,3.341131,4.030759,-6.953285,-7.529077,3.525715,-9.809043,-7.716838],[-0.420025,5.206268,5.426375,9.374620,1.519531,-6.272630,-8.738072,4.544375,9.142909,-3.824730,-6.349563,-6.326376,-8.751074,9.810646,-3.402695],[7.067944,-8.742638,-3.209050,-3.262506,2.227141,-1.250798,2.731088,4.683776,-0.415192,-1.109879,5.253881,7.776807,5.043438,3.532162,-1.036980]],[[-4.114265,9.575935,7.690409,-1.730790,7.767972,3.870243,1.684954,-8.519623,1.940449,-6.928937,5.004785,-6.097720,6.623662,9.268911,-0.383904],[7.861277,1.943177,-0.287287,-9.560274,-2.871373,-8.722125,7.116935,3.946093,-8.240193,0.038876,-5.668271,-1.960559,2.323890,-1.646598,9.776691],[8.545456,2.583553,9.070253,7.019449,-1.250992,7.924773,9.213832,6.306724,-1.818987,-4.699640,-7.575465,1.593483,3.541802,-8.496833,2.608108],[5.755570,-2.045490,5.049161,-2.395882,-3.157231,-3.933519,6.868604,-7.644702,-2.161753,8.453234,-3.323860,7.516582,-1.591339,0.908000,-4.713179]],[[-4.501009,1.485223,-6.949445,-9.983101,0.337839,-6.912029,-0.278263,7.110620,-9.777914,-1.592814,-2.447299,0.257191,-1.871675,0.793242,-3.843092],[-0.449337,5.201767,-7.572044,-6.569615,-1.783015,8.262525,6.202515,-1.255548,-7.897512,5.357536,-3.507797,-5.894589,9.249372,-6.682554,-6.437457],[0.695597,2.351179,-5.680423,-0.634446,8.382261,-4.908888,8.972570,-3.871801,-9.150540,-3.339487,0.021728,-4.490217,-0.269205,-2.976709,-0.020192],[-3.388610,1.762611,-8.169271,7.536466,-8.413586,9.540507,9.081161,2.046735,-5.091434,-0.329501,9.720717,-6.286029,2.024371,7.991938,8.209308]],[[-5.975992,8.984821,4.289546,5.292642,3.197510,5.578468,-0.879260,7.439966,3.785823,-3.543766,3.552998,6.721299,0.337511,-0.097702,3.178114],[-6.476142,5.175283,1.942566,5.274850,1.692343,3.138860,2.923126,6.132710,1.507102,-0.091541,3.484740,9.247674,5.894017,5.213198,8.231843],[0.741713,7.853847,-9.508109,-8.581208,9.804781,-2.334914,-1.550401,9.693466,-7.574760,-1.088721,-0.731006,-5.861037,3.367201,-5.929947,-7.557675],[9.352662,0.042857,-7.646822,8.268907,1.360415,3.346069,3.806880,8.306108,7.073237,1.521655,-8.539416,1.131111,4.963611,2.057157,-2.923051]],[[-9.383017,4.862328,-4.407298,6.933480,-1.383440,-5.018740,-2.796239,-8.969261,-5.820178,7.036622,3.014297,0.749133,1.638349,5.408402,-2.082268],[-8.951515,2.400110,-1.294723,1.285583,-4.774968,-7.016209,8.213006,-1.264116,-9.697655,-3.471074,6.316654,-3.003415,-0.476463,5.157650,-6.310366],[3.530626,-6.404118,-7.395729,-3.104803,-1.293375,-0.105288,-9.600562,2.465721,3.266148,0.898319,-9.368770,1.632058,-2.703454,-1.967611,-9.173840],[4.523438,5.981795,-0.303039,5.024154,2.378173,1.856717,-2.577431,-1.413810,3.005647,-3.504902,5.801735,6.757013,9.632521,-9.028110,0.007593]],[[-3.982247,7.210286,8.830719,1.221304,-6.031662,-2.286381,-8.414308,0.176376,7.005356,-0.191610,-7.617896,-7.212243,8.111691,2.496646,0.415709],[-3.799124,9.547924,3.432354,0.996958,3.520823,1.005445,-1.795498,3.633171,-6.509585,-5.221019,-2.179413,-4.854569,-8.938103,-9.871960,-9.094717],[-9.016738,2.131684,-6.034036,-4.894091,6.436759,9.388731,-5.580382,3.424344,-5.342674,-7.064390,-9.403465,6.908900,0.637170,-3.044917,5.841192],[6.210383,8.322730,9.294147,3.077006,-7.406697,-5.419425,8.048955,6.738970,-5.553828,7.207375,-4.901642,1.032627,-5.471195,6.201605,-2.662797]]], dtype = "float64")#candidate|18678|(12, 4, 15)|const|float64
uop_18679 = relay.atanh(const_18678.astype('float64')) # shape=(12, 4, 15)
func_10305_call = mod.get_global_var('func_10305')
func_10306_call = mutated_mod.get_global_var('func_10306')
call_18681 = func_10305_call()
call_18682 = func_10305_call()
output = relay.Tuple([uop_18679,call_18681,])
output2 = relay.Tuple([uop_18679,call_18682,])
func_18694 = relay.Function([], output)
mod['func_18694'] = func_18694
mod = relay.transform.InferType()(mod)
output = func_18694()
func_18695 = relay.Function([], output)
mutated_mod['func_18695'] = func_18695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13273_call = mod.get_global_var('func_13273')
func_13274_call = mutated_mod.get_global_var('func_13274')
call_18707 = relay.TupleGetItem(func_13273_call(), 0)
call_18708 = relay.TupleGetItem(func_13274_call(), 0)
output = call_18707
output2 = call_18708
func_18716 = relay.Function([], output)
mod['func_18716'] = func_18716
mod = relay.transform.InferType()(mod)
output = func_18716()
func_18717 = relay.Function([], output)
mutated_mod['func_18717'] = func_18717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17138_call = mod.get_global_var('func_17138')
func_17140_call = mutated_mod.get_global_var('func_17140')
call_18737 = relay.TupleGetItem(func_17138_call(), 0)
call_18738 = relay.TupleGetItem(func_17140_call(), 0)
func_12870_call = mod.get_global_var('func_12870')
func_12871_call = mutated_mod.get_global_var('func_12871')
call_18774 = func_12870_call()
call_18775 = func_12870_call()
func_17708_call = mod.get_global_var('func_17708')
func_17710_call = mutated_mod.get_global_var('func_17710')
call_18787 = relay.TupleGetItem(func_17708_call(), 0)
call_18788 = relay.TupleGetItem(func_17710_call(), 0)
func_10485_call = mod.get_global_var('func_10485')
func_10486_call = mutated_mod.get_global_var('func_10486')
call_18794 = relay.TupleGetItem(func_10485_call(), 0)
call_18795 = relay.TupleGetItem(func_10486_call(), 0)
output = relay.Tuple([call_18737,call_18774,call_18787,call_18794,])
output2 = relay.Tuple([call_18738,call_18775,call_18788,call_18795,])
func_18813 = relay.Function([], output)
mod['func_18813'] = func_18813
mod = relay.transform.InferType()(mod)
output = func_18813()
func_18814 = relay.Function([], output)
mutated_mod['func_18814'] = func_18814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13512_call = mod.get_global_var('func_13512')
func_13514_call = mutated_mod.get_global_var('func_13514')
call_18844 = relay.TupleGetItem(func_13512_call(), 2)
call_18845 = relay.TupleGetItem(func_13514_call(), 2)
output = call_18844
output2 = call_18845
func_18879 = relay.Function([], output)
mod['func_18879'] = func_18879
mod = relay.transform.InferType()(mod)
mutated_mod['func_18879'] = func_18879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18879_call = mutated_mod.get_global_var('func_18879')
call_18880 = func_18879_call()
output = call_18880
func_18881 = relay.Function([], output)
mutated_mod['func_18881'] = func_18881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15709_call = mod.get_global_var('func_15709')
func_15711_call = mutated_mod.get_global_var('func_15711')
call_18884 = relay.TupleGetItem(func_15709_call(), 2)
call_18885 = relay.TupleGetItem(func_15711_call(), 2)
func_3701_call = mod.get_global_var('func_3701')
func_3706_call = mutated_mod.get_global_var('func_3706')
var_18891 = relay.var("var_18891", dtype = "float64", shape = (390,))#candidate|18891|(390,)|var|float64
var_18892 = relay.var("var_18892", dtype = "uint32", shape = (63,))#candidate|18892|(63,)|var|uint32
var_18893 = relay.var("var_18893", dtype = "float32", shape = (2400,))#candidate|18893|(2400,)|var|float32
call_18890 = relay.TupleGetItem(func_3701_call(relay.reshape(var_18891.astype('float64'), [13, 6, 5]), relay.reshape(var_18892.astype('uint32'), [63,]), relay.reshape(var_18893.astype('float32'), [2400,]), ), 0)
call_18894 = relay.TupleGetItem(func_3706_call(relay.reshape(var_18891.astype('float64'), [13, 6, 5]), relay.reshape(var_18892.astype('uint32'), [63,]), relay.reshape(var_18893.astype('float32'), [2400,]), ), 0)
output = relay.Tuple([call_18884,call_18890,var_18891,var_18892,var_18893,])
output2 = relay.Tuple([call_18885,call_18894,var_18891,var_18892,var_18893,])
func_18907 = relay.Function([var_18891,var_18892,var_18893,], output)
mod['func_18907'] = func_18907
mod = relay.transform.InferType()(mod)
mutated_mod['func_18907'] = func_18907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18907_call = mutated_mod.get_global_var('func_18907')
var_18909 = relay.var("var_18909", dtype = "float64", shape = (390,))#candidate|18909|(390,)|var|float64
var_18910 = relay.var("var_18910", dtype = "uint32", shape = (63,))#candidate|18910|(63,)|var|uint32
var_18911 = relay.var("var_18911", dtype = "float32", shape = (2400,))#candidate|18911|(2400,)|var|float32
call_18908 = func_18907_call(var_18909,var_18910,var_18911,)
output = call_18908
func_18912 = relay.Function([var_18909,var_18910,var_18911,], output)
mutated_mod['func_18912'] = func_18912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17138_call = mod.get_global_var('func_17138')
func_17140_call = mutated_mod.get_global_var('func_17140')
call_18950 = relay.TupleGetItem(func_17138_call(), 0)
call_18951 = relay.TupleGetItem(func_17140_call(), 0)
func_17047_call = mod.get_global_var('func_17047')
func_17048_call = mutated_mod.get_global_var('func_17048')
call_18956 = relay.TupleGetItem(func_17047_call(), 0)
call_18957 = relay.TupleGetItem(func_17048_call(), 0)
output = relay.Tuple([call_18950,call_18956,])
output2 = relay.Tuple([call_18951,call_18957,])
func_18962 = relay.Function([], output)
mod['func_18962'] = func_18962
mod = relay.transform.InferType()(mod)
output = func_18962()
func_18963 = relay.Function([], output)
mutated_mod['func_18963'] = func_18963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15274_call = mod.get_global_var('func_15274')
func_15276_call = mutated_mod.get_global_var('func_15276')
call_19050 = func_15274_call()
call_19051 = func_15274_call()
func_17164_call = mod.get_global_var('func_17164')
func_17165_call = mutated_mod.get_global_var('func_17165')
call_19055 = func_17164_call()
call_19056 = func_17164_call()
output = relay.Tuple([call_19050,call_19055,])
output2 = relay.Tuple([call_19051,call_19056,])
func_19058 = relay.Function([], output)
mod['func_19058'] = func_19058
mod = relay.transform.InferType()(mod)
output = func_19058()
func_19059 = relay.Function([], output)
mutated_mod['func_19059'] = func_19059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17857_call = mod.get_global_var('func_17857')
func_17859_call = mutated_mod.get_global_var('func_17859')
call_19124 = relay.TupleGetItem(func_17857_call(), 1)
call_19125 = relay.TupleGetItem(func_17859_call(), 1)
output = call_19124
output2 = call_19125
func_19136 = relay.Function([], output)
mod['func_19136'] = func_19136
mod = relay.transform.InferType()(mod)
mutated_mod['func_19136'] = func_19136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19136_call = mutated_mod.get_global_var('func_19136')
call_19137 = func_19136_call()
output = call_19137
func_19138 = relay.Function([], output)
mutated_mod['func_19138'] = func_19138
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19152 = relay.var("var_19152", dtype = "float32", shape = (12, 11, 13))#candidate|19152|(12, 11, 13)|var|float32
var_19153 = relay.var("var_19153", dtype = "float32", shape = (12, 11, 13))#candidate|19153|(12, 11, 13)|var|float32
bop_19154 = relay.floor_mod(var_19152.astype('float32'), relay.reshape(var_19153.astype('float32'), relay.shape_of(var_19152))) # shape=(12, 11, 13)
output = bop_19154
output2 = bop_19154
func_19174 = relay.Function([var_19152,var_19153,], output)
mod['func_19174'] = func_19174
mod = relay.transform.InferType()(mod)
mutated_mod['func_19174'] = func_19174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19174_call = mutated_mod.get_global_var('func_19174')
var_19176 = relay.var("var_19176", dtype = "float32", shape = (12, 11, 13))#candidate|19176|(12, 11, 13)|var|float32
var_19177 = relay.var("var_19177", dtype = "float32", shape = (12, 11, 13))#candidate|19177|(12, 11, 13)|var|float32
call_19175 = func_19174_call(var_19176,var_19177,)
output = call_19175
func_19178 = relay.Function([var_19176,var_19177,], output)
mutated_mod['func_19178'] = func_19178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18664_call = mod.get_global_var('func_18664')
func_18666_call = mutated_mod.get_global_var('func_18666')
call_19220 = relay.TupleGetItem(func_18664_call(), 0)
call_19221 = relay.TupleGetItem(func_18666_call(), 0)
output = relay.Tuple([call_19220,])
output2 = relay.Tuple([call_19221,])
func_19228 = relay.Function([], output)
mod['func_19228'] = func_19228
mod = relay.transform.InferType()(mod)
mutated_mod['func_19228'] = func_19228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19228_call = mutated_mod.get_global_var('func_19228')
call_19229 = func_19228_call()
output = call_19229
func_19230 = relay.Function([], output)
mutated_mod['func_19230'] = func_19230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16298_call = mod.get_global_var('func_16298')
func_16300_call = mutated_mod.get_global_var('func_16300')
call_19231 = func_16298_call()
call_19232 = func_16298_call()
output = call_19231
output2 = call_19232
func_19234 = relay.Function([], output)
mod['func_19234'] = func_19234
mod = relay.transform.InferType()(mod)
mutated_mod['func_19234'] = func_19234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19234_call = mutated_mod.get_global_var('func_19234')
call_19235 = func_19234_call()
output = call_19235
func_19236 = relay.Function([], output)
mutated_mod['func_19236'] = func_19236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18603_call = mod.get_global_var('func_18603')
func_18605_call = mutated_mod.get_global_var('func_18605')
call_19268 = relay.TupleGetItem(func_18603_call(), 0)
call_19269 = relay.TupleGetItem(func_18605_call(), 0)
output = relay.Tuple([call_19268,])
output2 = relay.Tuple([call_19269,])
func_19292 = relay.Function([], output)
mod['func_19292'] = func_19292
mod = relay.transform.InferType()(mod)
output = func_19292()
func_19293 = relay.Function([], output)
mutated_mod['func_19293'] = func_19293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16515_call = mod.get_global_var('func_16515')
func_16517_call = mutated_mod.get_global_var('func_16517')
call_19319 = relay.TupleGetItem(func_16515_call(), 1)
call_19320 = relay.TupleGetItem(func_16517_call(), 1)
func_4093_call = mod.get_global_var('func_4093')
func_4097_call = mutated_mod.get_global_var('func_4097')
const_19329 = relay.const([-2.891099,-2.338057,-9.910238,8.121423,-1.294339,5.621167,-5.684281,-1.555880,8.524721,-1.021379,3.655390,-9.054584,-1.621188,0.685423,5.307047,5.008815,8.861913,2.105133,7.137182,-7.509144,-3.316840,-0.259195,-7.707330,-3.090298,-2.786300,-6.113276,2.955966,0.576174,-5.575746,5.200544,7.243225,1.153686,-7.931438,-3.289145,9.773937,3.607709,-7.787682,-9.260202,-1.183717,-1.108811,7.083728,-9.854670,0.670674,-7.756158,-9.398861,1.682192,5.497445,8.318851,-7.939400,0.456425,-8.085177,7.429388,-3.827196,9.494049,-7.594132,-7.079908,-6.686815,8.580914,-8.102774,7.221848,5.615556,-2.341842,1.841678,2.069994,5.901674,-0.642142,0.196489,-6.703492,5.719831,3.926133,4.357393,-5.208121,-2.790447,1.587451,0.036981,-2.511990,1.378668,6.703157,-1.083783,-3.382148,7.778763,6.935378,-6.915291,8.335303,9.370754,-9.426074,-7.815215,-2.277166,-5.200536,0.976071,-7.577460,-5.970405,-2.420826,-1.935166,-6.119784,-3.223041,4.545561,9.297417,3.647387,-6.113730,1.134420,9.418531,5.105140,-7.876015,9.110636,2.083397,6.805447,3.853316,-0.336341,-9.837320,8.857703,-5.050199,-8.376193,-4.927153,-5.245720,-5.371611,2.218437,8.670452,6.704148,-7.034934,9.931116,-4.781280,-7.490347,-2.864472,-3.672300,9.988825,2.247786,-2.878016,7.135910,5.788997,0.139445,9.515443,4.526072,6.436690,2.394824,6.481491,-4.958349,4.710749,-7.045904,6.769711,7.182355,-9.546530,-9.112520,-6.943800,4.939164,-2.020151,-9.216131,-8.470239,-6.284734,-0.727347,1.969378,0.646668,-0.526550,-8.988352,-5.044160,9.805355,2.235005,8.429682,-8.582516,6.795840,5.834775,0.275270,-2.193611,-7.749109,1.979202,-3.030491,-4.136477,-0.495044,-2.252614,0.778406,-3.296808,-6.566535,-6.179119,-9.587492,-8.854043,6.396747,5.601426,1.535674,-6.749826,-5.010785,-8.447244,-0.537685,-9.672295,5.383845,-3.970275,-5.430610,1.672814,-7.780056,-5.821619,2.063597,-7.734389,-8.164978,3.390014,3.432596,0.463227,2.689310,-3.083760,8.739195,2.550235,-8.241367,0.839565,-9.897551,7.674728,0.988526,7.131210,-8.974434,5.037576,3.314612,-9.643676,-7.897540,8.311578,-6.666308,9.684008,-9.469894,-1.892143,-0.548645,5.461817,5.643019,0.121146,-5.282928,5.197679,1.988671,-7.120708,3.901443,0.943527,-9.462395,3.655550,7.210487,-0.122271,1.256363,-5.796250,2.434067,3.997736,-2.199899,1.869031,5.310542,-8.685826,6.193278,-3.906918,8.423704,-9.374965,-2.580804,-6.291072,-9.701457,9.199092,-5.973310,-8.385956,-9.761783,-0.223502,-9.272254,3.820150,-3.617262,-1.492149,-6.451186,-0.593351,5.416270,-4.285706,-5.719238,9.769007,9.109788,5.925244,-9.642426,8.248104,1.653646,4.349972,1.597582,3.805461,-5.323409,4.932414,-7.323828,5.440358,-3.951435,2.171746,-9.198774,-3.248569,-2.536929,9.482400,5.615976,6.130250,-8.371555,-8.339709,3.837059,4.073028,-9.546198,2.184103,-0.761128,-5.984434,-0.688429,-1.356240,-7.750145,-3.567853,-8.669705,1.368832,5.947363,-6.314039,3.201569,3.551455,-4.865986,6.286876,-5.522155,-0.009709,2.965876,3.772246,-0.003948,-5.591580,-6.177849,2.966201,4.900534,-8.865065,1.709124,-7.296687,-1.100964,-9.504840,6.342997,1.028926,-0.916548,-9.131403,-1.937860,3.317782,8.747609,7.994975,-6.914291,-2.541009,0.419545,-8.435144,2.670548,3.952945,3.265571,2.810379,6.953998,-0.894218,-8.600810,9.597686,-0.913611,4.695697,3.026494,-6.445354,-8.597124,0.608593,3.225493,-4.934347,-3.690996,-6.204136,1.155389,-9.480486,-3.714787,-9.274363,-8.386271,2.079592,-7.182343,-1.359379,7.426086,-0.747777,-0.836930,2.033299,0.304883,-5.295477,-9.572560,9.494862,-4.789957,-7.973023,-3.543811,1.462767,4.450737,-2.447975,-5.639011,3.482963,0.156160,4.340267,0.434808,5.941225,-4.531051,-6.773106,0.893181,0.723833,-0.670946,-6.492652,-0.553976,5.043139,4.576521,-9.218369,-3.873730,8.736541,8.095408,3.874767,-3.915656,3.774544,0.671317,3.109688,-7.132496,-9.801652,-0.991572,0.371454,3.636897,-0.800361,-2.659681,-6.174893,-2.481549,-1.822705,-4.730271,-6.537257,0.617707,2.003443,-5.769503,4.160769,9.066861,6.916451,-9.261784,5.196166,5.060885,-5.150514,-5.028252,-5.811991,3.355157,-9.224934,3.935966,-3.730498,-3.168207,0.300756,-0.346385,5.648559,-5.365739,1.098815,-9.246264,-4.223040,0.758327,8.975917,5.530017,-3.860131,5.777431,-2.867458,-0.466807,4.969591,7.286013,1.002206,2.490068,5.431105,7.933171,-5.462301,0.966237,8.859931,-3.536088,-6.897090,-9.516779,-9.095520,1.669600,-6.828454,8.387159,1.064557,-4.247761,-5.146679,8.892517,-3.468997,-7.513744,-3.387320,1.479655,-3.060521,9.778154,-6.242086,-2.035468,3.388382,0.381634,2.671148,0.850563,7.282831,5.143553,1.370198,-5.995496,7.882143,-5.696273,-9.109195,6.395683,5.626887,-4.429935,-5.905303,-6.076519,-7.873555,-1.315488,-9.860814,-3.857479,3.494989,5.024402,7.866465,-9.397107,2.769129,-0.981180,2.918907,-4.201716,-7.701992,-8.883970,2.756313,-5.121068,-4.813112,0.744305,-8.607493,6.309513,1.931636,-0.304872,-3.099887,1.547124,-4.679641,9.871939,3.788030,-0.227855,-8.096288,7.027399,-1.758919,-7.423427,-8.666527,2.646061,3.556998,-4.105552,-6.542457,7.656902,-7.528799,-9.972114,1.647954,-9.026045,1.684426,-0.745325,5.786118,-2.289599,-3.721185,-8.296465,-0.890040,9.833369,-7.997630,1.125926,5.260884,1.159142,6.234987,-1.864348,-0.972475,-7.857406,6.680230,5.602504,-9.022764,-2.229171,-0.978581,1.500416,7.709078,6.964796,-2.402704,-0.917459,9.176224,2.801729,0.036338,6.226346,-8.707069,3.918335,1.588636,-9.922104,-1.371776,-8.972214,-7.519447,-1.012929,-0.709679,4.543077,-1.161017,-9.938304,-8.209793,-4.517683,5.985044,2.410015,1.562628,-8.824625,6.115094,-6.445800,7.826318,6.462933,-7.095977,3.739341,2.689451,-2.537130,-4.417843,4.878058,-3.404759,-8.460972,-1.896543,-6.441494,2.182540,-9.506631,0.826724,-2.784529,0.804287,-7.735861,7.292134,-2.936874,4.786900,-0.133041,-4.094894,-3.325576,-9.062490,-5.527006,-0.199057,-8.115863,5.883209,-4.161933,-7.066082,-8.216821,-2.726228,7.792512,-5.968750,-3.487503,-9.383670,-9.994409,1.249635,-4.486719,6.195444,-9.040612,3.068725,7.494982,3.408837,6.975487,4.980790,6.698091,4.040320,0.526529,-3.237332,6.888898,2.488008,2.513642,-8.417796,-5.846531,6.983839,3.760176,7.532437,5.821800,-3.219010,-5.591738,-3.691641,-4.940324,0.098318,-9.998641,2.672566,-4.858768,9.878879,4.440498,3.340727,4.861346,-6.355645,0.641816,-6.741528,-5.508538,-1.503718,-4.845010,-9.073210,-2.082577,-4.289875,-9.636048,-7.067034,-5.074294,-0.138106,8.101538,3.431589,-8.736009,3.152258,-0.745574,6.894881,-3.697169,3.478874,-8.590479,3.238982,3.517973,7.739964,-8.040478,5.794586,4.843138,-4.619401,6.914211,-9.839390,-4.584355,-3.640822,6.858005,1.840861,4.151269,-8.479622,0.491905,-7.286776,6.647094,-9.923716,5.106739,8.816883,8.103559,1.940879,6.917444,3.957946,0.417862,-1.610994,9.528632,-8.948595,7.060879,-2.847088,1.365048,0.817540,8.669093,-3.479732,0.237054,7.209849,6.046591,-4.514307,-3.956995,-0.125417,6.633139,-5.832628,3.902072,0.164088,5.261886,9.008776,-6.102115,-0.285226,-5.279543,-2.687042,-4.113133,-2.509454,-6.495795,-5.234001,-9.148963,-2.853842,-6.034879,-6.124784,5.032765,-5.404029,-4.513255,4.106436,-3.504170,-8.669129,-8.131070,3.875823,-9.112850,7.544288,-6.101719,-8.869637,-1.966253,-1.370998,7.290958,-9.281607,-2.851579,-1.328715,-9.943777,6.408369,7.173747,0.037601,-6.155542,-6.965317,5.538609,5.166381,4.017618,-8.816708,-9.328815,-2.272483,-9.376743,-8.662095,7.545436,3.128108,8.268470,1.198602,-2.320760,-8.633928,6.174491,8.162174,-4.807685,-3.214642,-2.404444,-6.212207,7.418367,9.564239,4.387386,-8.276290,-4.835875,8.732103,-8.067134,-9.548771,2.909901,3.266492,8.493444,0.141177,8.343430,5.194283,6.971386,-7.320672,1.383354,-9.098705,5.197946,2.970195,-3.743303,3.211379,6.156755,8.128674,6.401002,8.498253,1.710803,-8.197472,-1.758928,7.066293,4.834157,-9.046228,4.487950,-8.646603,9.125625,-9.800842,-9.172779,-9.273125,4.184754,-4.810181,-1.333219,3.813343,6.877770,-8.029745,1.127442,8.495246,1.112719,1.036851,-5.313218,-3.372211,-5.581551,3.623729,-0.473416,-5.403671,1.818994,-9.168600,0.844224,9.168798,-7.799365,-9.769237,2.966992,-6.482784,-6.034340,7.462501,8.480472,-1.009287,-6.829524,-4.472927,-8.547493,-5.890762,-9.948116,4.507146,-9.400313,-5.858186,8.501369,5.956756,-4.618582,3.000096,8.416695,9.738595,-6.002832,-6.648583,8.335636,-0.367106,-3.527792,6.013405,6.856045,-4.178228,0.631922,-8.746281,0.106159,-2.924524,-4.541940,-0.298524,-7.706644,-9.556790,-0.408907,-6.171674,-4.856810,2.689291,8.607690,4.788628,7.220797,9.681252,-3.461415,1.820061,6.304004,1.129216,-0.937601,5.158219,3.044446,8.380376,1.991414,6.967745,-0.236141,-2.197885,7.909062,0.378108,9.905398,4.341937,-2.588222,3.909849,-5.476003,5.840564,8.970603,-8.941059,1.023790,-6.255250,4.052871,-3.517917,-3.095232], dtype = "float64")#candidate|19329|(896,)|const|float64
const_19330 = relay.const([-5.958004,3.919674,8.673912,1.347221,7.399190,0.247182,-8.536732,-8.514808,2.028165,-8.476331,-7.820094,1.588325,-3.847996,5.495823,1.423248,-4.870710,3.360209,6.206331,1.188326,4.061122,5.380354,-3.882947,7.773618,-7.209635,-2.490942,-2.588078,-2.427153,6.022609,0.889521,-1.141473,-6.773307,6.800482,7.177261,-9.425479,5.696815,5.194254,-2.384977,-1.837662,-5.561940,-2.956329,0.120856,9.848968,-6.964161,-8.496833,1.314274,-8.705607,2.617009,1.407000,-8.771350,-8.836605,-4.307095,-6.423675,4.900687,-2.769916,6.393084,-7.206932,-9.895600,-2.314115,-3.022450,-4.476674,-1.295195,8.813166,-0.757632,-6.671579,-6.201970,-5.409718,-7.912714,8.888059,8.316285,-7.905162,-3.207569,-2.635665,-9.472979,0.171710,4.341134,3.192841,-6.462883,-9.341547,9.578292,1.603742,4.811189,-9.933527,1.646498,1.007424,-1.844441,8.984444,-0.792007,6.866121,8.790619,1.380884,-5.562736,-1.122098,6.284591,-1.852127,5.947085,-4.396166,5.989961,-3.597288,-4.504128,-5.239966,7.263035,7.048335,0.299048,2.355125,9.721715,8.356564,4.016610,-6.390538,-2.290067,0.843912,-6.925486,-1.696589,8.585796,-1.294061,-4.480696,-2.307573,4.523654,3.035317,-6.010726,6.085179,4.196644,5.054410,-0.484535,4.223496,-8.852160,-8.931586,-9.701376,2.022373,3.005342,8.863573,-8.033701,-2.026170,1.317449,-1.209715,-0.044964,5.063633,-3.597321,-1.469187,-0.204547,-0.863427,-9.920107,-6.472441,5.940524,-6.694329,1.419574,9.180007,6.954127,6.969346,5.353844,-8.022753,9.501399,-0.092512,2.892237,-7.214873,-9.088050,-9.306088,8.503760,-2.315847,-3.382459,-3.390768,-8.983658,8.418889,8.090836,4.032493,-9.126239,-2.514006,0.697660,-7.241380,0.017726,0.202833,1.717332,-5.975240,-6.782880,1.351767,-8.039670,-7.850182,0.173532,-5.753078,1.246617,-0.925440,-2.052512,0.527181,9.177292,-5.525584,1.176510,-6.908938,0.407632,1.594492,3.343731,1.850314,-7.499328,0.476633,3.221900,-0.750213,2.502517,5.132184,6.197676,7.063307,-1.609951,0.176025,8.751778,-8.009577,5.481031,-0.017590,-9.163270,-8.291768,-3.166059,9.228353,5.019799,-1.254635,-8.315763,-8.932804,-5.926876,-0.980931,3.470146,-4.632082,4.427438,-9.504608,9.994631,-6.465858,-9.555101,-8.910915,-4.007420,-5.539281,-2.925209,-1.338941,-5.146247,-0.783939,-1.296350,5.890553,4.105169,3.805564,-7.217176,8.655616,-9.596101,-0.657847,-2.216195,5.240295,-1.299159,-9.333791,-2.511620,7.342471,-9.545907,-0.564773,-8.272892,-6.147721,9.237840,-0.964235,7.459387,1.333188,2.858896,-4.194279,3.615981,-5.975646,-1.979711,-2.452006,0.526417,2.985850,1.945490,4.376566,-5.884868,2.852639,9.004720,4.379375,0.903503,-3.743649,-5.259517,-2.645329,0.579374,2.550099,-1.328726,-6.908802,8.358435,1.958640,6.930174,-6.014655,-8.889305,-8.812164,-4.171287,1.157735,-4.395319,-9.790294,-1.613827,-8.030564,-0.424229,3.552738,1.027067,-5.280139,-9.206003,-0.841074,-6.077536,0.796068,-5.301320,-8.501855,5.937796,8.781944,-2.557444,6.173680,-6.482964,-8.840286,2.824372,1.174102,6.954848,-2.748968,7.177416,-7.412483,0.289618,1.867557,5.752526,-5.875223,9.452158,-9.462166,-9.347383,-3.795539,-9.979763,0.997082,9.325802,-2.229437,-8.405703,-7.635633,5.053123,-4.798026,-0.870213,8.159784,3.915550,-8.223401,4.613808,-9.613289,-2.157644,-6.934772,3.891964,2.885288,6.365155,-6.513105,-1.631874,1.370804,4.210257,-9.966124,6.350640,6.397212,-3.046153,2.364543,-3.279495,1.281219,7.846054,1.649646,2.289225,7.670502,9.492241,-9.646533,-3.770747,8.753291,7.990097,4.519833,4.528320,-5.300369,-8.237160,4.114029,4.092145,-1.029042,8.615145,-4.097738,-5.044471,1.196766,5.219619,5.175451,8.833750,8.336226,-4.255160,-1.467608,2.747019,2.986487,-7.205209,-9.340450,3.447683,-4.713617,6.495235,1.809118,-0.745535,3.680014,0.435530,3.585129,0.802921,9.482164,0.079553,-1.751683,-9.170210,3.615128,-7.132766,3.035563,-9.989696,-9.127112,-7.846493,4.408182,-0.915671,-2.014866,4.450322,1.139892,-4.489384,-2.641020,-4.509974,-3.715319,9.938954,4.416292,4.880908,4.844818,7.296283,1.701019,-0.452191,-7.698657,3.993467,-9.853245,3.282980,-3.168072,-9.368218,4.459486,5.485245,-6.806956,3.207429,-6.734488,-2.078188,-9.335227,-3.867652,0.929527,-6.274884,2.124270,-6.679641,-8.840249,5.974952,7.653425,-3.337679,-2.387842,-5.438687,-0.469899,3.180805,-0.467092,-2.539622,4.314592,0.250582,3.026149,-2.920644,7.243430,-9.148525,-3.699082,-6.697094,-7.993445,3.903042,-1.476933,0.170181,0.793625,-7.459582,-3.620439,5.565856,4.469436,-7.790963,-5.738451,2.766007,7.068301,-0.865529,-1.808908,4.838020,7.841738,6.359291,-9.335753,-8.396707,7.575348,4.757242,9.068447,7.554967,8.207370,-4.023994,5.184122,-2.989601,5.712408,-7.392687,0.927356,-3.778992,-3.007115,8.443579,-6.211899,9.706625,-5.828788,3.832300,5.806204,-4.420082,-6.430711,-6.871132,-7.245048,-1.815281,7.804388,8.092031,-8.339947,4.257164,-1.096040,6.037183,-5.036927,-6.841147,-1.715439,6.158530,2.805951,-1.135190,-8.069564,3.208614,6.317200,-6.756821,-3.814225,-8.447369,-2.881625,-2.428908,-7.332195,7.860506,-9.024034,6.773394,-3.194770,-3.777546,-8.392833,1.389212,9.712202,7.179046,8.746324,-8.163889,-7.354236,-6.911662,-6.498867,0.482436,2.777722,-7.156110,-2.571182,-3.380907,-5.379575,-4.872166,9.904421,9.170340,-6.267171,-3.914692,-5.791299,-6.965997,5.872988,5.767833,4.452627,-9.166872,-4.463937,-4.874762,-6.435233,8.979731,7.130595,2.453609,8.128004,3.050639,9.354566,5.428675,-6.360004,-2.250499,8.096908,-0.404358,-1.384500,9.320396,1.392147,-5.078717,-0.587436,-4.515930,6.776215,-7.029925,-7.385353,1.828391,9.509646,3.249442,-3.183054,6.323734,-5.041749,-9.120915,-5.568965,8.349304,2.394134,2.079897,8.889978,3.727554,5.734329,9.885463,4.870375,-6.112509,-4.259979,1.696327,0.206124,-2.104383,-2.855327,2.179635,-9.710114,-5.005648,-9.442160,4.920239,6.871275,-9.679197,-4.195603,-0.548803,-2.294599,5.443247,-9.153467,8.324192,9.373316,7.878271,-4.712881,9.879227,7.850746,-6.876558,4.913417,2.356906,-7.391184,-7.213619,-5.337403,7.800850,2.421281,2.204579,3.702582,0.406167,-4.652426,-2.831310,0.908268,5.543180,7.736210,-4.840734,3.354428,3.573883,-1.576577,-1.379143,-7.583388,5.011243,-9.340271,8.430506,-6.897228,0.286760,-0.916745,7.784165,1.930664,-7.175998,5.608617,9.585625,3.241561,-5.044124,-3.685749,-8.819805,-8.577179,-9.951357,-9.641672,-7.352615,3.905771,3.363896,7.825261,3.766289,6.437315,8.970366,6.568558,9.418891,0.909918,-3.376320,-4.194754,-8.202837,-5.147242,-9.304371,3.294639,4.618600,-9.661708,-9.482033,-6.606615,-7.524444,3.510186,-4.406096,-4.286596,5.056235,5.757148,-2.734871,-2.578038,8.398872,3.091079,8.015787,-3.769763,2.668835,4.556320,9.060922,-5.767842,8.643062,2.335622,-0.646086,4.907304,-5.445424,4.786931,3.608835,3.022218,-9.944710,-5.165467,7.850512,4.790361,1.145436,-6.009573,-4.508328,-4.273108,9.228507,9.880723,6.613680,3.463547], dtype = "float32")#candidate|19330|(700,)|const|float32
const_19331 = relay.const([[4.850090,6.033259,7.472210,9.443913,7.145261,-5.683514,7.430970,-8.324593,-2.699544,6.626240,9.790034,3.512831,-2.832116,1.040863,2.193594,0.201407,2.857883,-1.555592,2.678872,3.033315,-7.326503,1.194281,-8.398892,8.123897,8.793751,-2.010516,3.666219,5.012207,-5.614136,5.769247,9.161062,6.653658,2.062000,-6.159252,3.784340,6.842741,9.605499,6.263950,4.397585,-3.496771,6.454590,2.603602,-6.517221,6.993770,-2.324277,-1.823961,1.783989,-6.683749,4.829152,8.193548,-7.491606,-5.430570,9.402220,9.084606,-4.495728,6.365425,-7.112754,7.865340,-7.067952,6.149664,5.377683,-1.051005,3.006509,5.100427,3.435236,0.874520,6.542622,0.503292,3.705730,1.820302,7.044539,-9.501331,-7.604033,-4.459797,-7.316748,5.737205,-1.074064,-2.996292,-5.054062,-3.912132,-2.205490,0.475803,-0.570029,4.794932,4.190834,0.519524,7.247368,-6.822841,3.533631,-0.403446,-0.259239,0.678067,-2.657955,0.297294,6.608443,-1.232841,0.669138,-4.563706,7.530110,-5.544843,-4.247855,5.401855,6.807237,9.707005,-0.252594,-6.450094,0.002497,1.396408,2.612289,-8.777142,7.906050,-9.569042,-5.397288,-3.160484,-2.703346,-3.957892,-6.444799,6.772618,2.839884,1.914882,-4.259900,7.186213,9.621646,5.757596,1.937537,-2.236936,0.564190,3.436321,4.213425,4.633846,-8.954119,-7.608426,6.913192,-3.683282,0.594727,-8.444180,7.478133,8.751758,2.424271,9.796594,7.837429,5.677298,6.125493,-4.842708,-0.591691,-7.463793,-1.083511,8.400483,-5.943788,-8.420189,1.711986,-6.492032,-1.903861,-8.335067,-4.454034,-2.483302,9.699826,-9.030863,2.839473,7.198737,-2.801718,-6.227083,-8.679261,-3.043028,-6.071994,-4.019521,-6.090238,-7.206931,9.420393,-8.355733,6.092566,6.566541,-7.213800,4.247355,-5.096091,1.819859,-4.368654,9.162847,8.175937,-2.095963,2.869649,-2.538967,5.683995,-3.907057,1.006031,-6.927904,-1.830119,0.676214,-8.912990,-4.963678,7.026537,5.494902,7.331186,-7.459275,9.342863,-9.112749,-7.317397,-5.371476,-8.251257,-1.951122,3.877774,-7.270643,-2.320822,-8.783456,-0.073399,0.403374,-1.026851,8.953185,-5.790043,-6.383511,-5.220825,-5.753895,9.382181,-3.850030,8.299869,2.436892,-7.568761,-6.825001,4.723097,7.685447,5.965920,8.329445,9.656939,-7.509451,9.189340,0.990234,8.325273,-5.620693,-2.559567,-9.332774,7.310954,-8.534234,0.483088,-4.661350,7.450823,-7.422537,-9.792796,-9.078749,8.289330,4.946842,-5.728680,-9.319606,-7.546472,-7.326465,-2.782839,0.685101,6.332267,7.666926,-7.435123,9.366100,1.744168,1.623159,-6.512403,5.822815,-7.078004,-8.001146,-8.976208,-1.575165,0.497117,7.455515,-4.338836,7.883821,2.983044,-9.650343,-2.914055,1.023199,-4.014037,7.002303,9.942909,-1.002220,-3.587065,-3.083359,3.085424,7.784853,5.559224,-9.566203,1.733102,6.384292,-2.679991,4.779250,-4.968869,-5.454761,5.301256,0.107773,7.961128,-9.170343,-4.119114,-7.965046,0.720164,-0.887291,-9.203521,-2.138626,-8.032171,-1.349981,-3.593041,1.016902,2.904102,2.507703,3.208498,7.604779,-5.701117,-4.627805,-1.528636,-8.873851,9.881040,-3.747748,-7.163782,6.876896,5.240950,1.115879,6.560921,-4.524179,8.546037,0.232151,-1.444354,3.370768,-2.169046,1.895993,-6.152027,7.413468,-9.560733,2.025643,-6.404529,1.100469,9.018252,0.710854,4.663019,3.003822,9.711611,4.674145,1.617299,-1.322852,1.772487,-0.328924,-2.001476,6.245866,3.656973,0.530358,8.030383,8.500890,0.729807,-7.517639,-5.025865,9.178563,-4.844996,3.559599,2.539793,-9.554756,0.737207,-0.667285,-7.151935,-2.807630,5.373796,1.117754,-8.574706,8.173335,-5.390412,-2.319180,5.527872,-3.866827,0.395207,8.622856,-2.310944,1.031045,-5.526401,6.881239,5.955523,-7.468772,3.794790,3.679735,7.083977,1.257364,-6.221153,-2.038572,-8.949251,-2.004127,6.250167,-4.971433,2.947884,7.579135,-6.442227,-5.767765,9.043643,-0.633427,-9.687243,-2.943237,-6.227921,3.146729,-4.096211,-8.620878,6.287946,-8.503176,-8.612628,-4.967232,-2.522252,1.783579,-4.828023,-8.117692,-7.557995,-5.586289,-1.486880,-7.694697,-8.048640,-3.374549,-6.823327,8.338007,2.526575,-6.992708,5.979619,1.330727,-7.764063,-3.840122,-1.531275,-8.859709,3.302861,9.204867,-9.298444,-6.872125,-2.215879,6.380521,9.302867,-1.652942,-6.956681,-3.328724,5.252881,3.636926,-5.445926,-4.717306,-9.416058,6.828747,0.674858,7.871819,9.554818,-1.573396,-1.471252,-3.618735,9.933844,-9.936068,8.771091,8.636077,-5.372828,-0.575133,-3.931973,2.062734,-7.072723,-0.280726,-7.516450,2.022014,9.635859,3.215313,0.223919,6.088941,-9.861666,-3.364022,-3.820399,-6.626358,-2.230008,1.971219,2.575913,3.930084,9.908982,4.704194,5.147123,8.984546,-0.655918,9.655089,-2.846647,-5.749468,-2.759715,-9.315291,-6.001535,-2.093082,-4.888934,4.864223,-0.538694,6.096699,-5.669168,5.912523,2.285334,-1.136856,0.877680,6.390854,-9.027630,-6.973027,-5.902217,9.612084,6.968359,7.549124,6.111327,8.706295,2.753832,-6.461402,5.103804,2.086083,-6.019447,9.611286,1.354143,-8.217853,-2.210117,7.425908,2.548114,-1.800349,-4.020138,-7.502585,-4.000687,0.183086,-8.583483,-6.162614,-0.454393,-3.267466,6.422320,-5.407054,-4.185856,8.125104,-5.241426,9.436155,6.928343,-4.499649,0.768153,-9.257856,8.916869,9.591007,9.301621,6.223039,-6.117617,-5.397139,5.834755,-6.798313,1.817813,6.797636,-8.885940,-5.239448,-1.240170,4.652756,5.992667,1.399702,-9.449298,1.758722,-1.877200,1.757585,-0.715153,3.216252,-8.501050,-4.151633,3.901284,0.056986,-7.406699,6.322231,4.297284,2.074774,-2.826736,2.397646,2.828358,-7.666648,9.275770,-5.507554,-0.637611,-3.328300,-2.482211,-4.657762,-7.893994,3.854162,7.287428,7.845198,-1.694683,-0.917391,3.511038,5.441187,-9.402423,1.867498,6.892638,6.136579,3.948804,-8.785826,-9.171921,5.386956,6.976893,-7.096865,6.355555,4.528180,-1.597375,4.223638,6.656799,-4.090501,-7.423885,9.065074,-2.663717,9.270647,-8.675388,3.363131,8.695661,2.423109,0.543884,2.969139,5.618998,-2.860362,-4.064831,-5.078660,-4.802580,0.263171,-6.079813,-9.747525,-4.814789,-2.524282,-7.562685,6.351176,-8.556636,-5.808167,-6.332974,-0.294835,-0.964952,0.949563,-7.077703,-8.293224,8.358502,-0.767310,-3.854473,-8.347884,-6.376498,-6.671807,-8.577972,-5.681262,-3.368745,-2.329033,5.173875,2.195809,-1.931069,-4.901965,-0.790336,8.536162,1.793449,6.716352,5.048863,-5.777470,-4.713378,-3.262970,-5.851928,2.808221,9.982157,-8.821639,-4.296452,-2.217407,-7.795306,-8.991772,0.630510,-0.639874,0.244069,-3.719996,9.852343,-1.899127,1.356653,-5.411075,-7.692808,2.354194,-1.391274,-4.501499,5.516009,9.530582,6.341264,-1.649863,6.959121,9.623062,-5.970371,7.269532,-0.179032,2.230649,-6.697692,-3.177222,1.146903,-4.057540,9.857406,-6.379648,1.933192,-0.392509,4.960763,3.046525,-8.118068,5.142767,1.771001,-8.290202,6.470814,2.815033,-0.590483,-7.566147,5.478952,2.434712,7.263756,9.027318,7.259870,8.910582,-0.122377,9.848768,-5.010451,0.056472,-0.882945,5.283854,3.878569,7.447662,-3.457305,4.411942,0.939948,-1.308291,4.832219,7.325929,-7.086311,8.500934,-8.632975,5.322817,-5.524409,-5.547463,-4.760126,-9.365591,-0.449688,7.533234,5.045585,0.959521,0.699768,9.889351,3.357635,8.204488,1.578035,7.251226,-7.312184,-5.528979,5.829909,5.504768,2.272486,-8.741784,3.262538,-8.389709,-7.311940,1.128541,-5.962797,-4.234806,-9.131134,3.734995,3.835047,5.998530,0.498818,-6.359246,-2.683470,-4.243976,7.589834,0.442686,7.563721,5.785677,4.684727,4.691227,5.813484,-3.791827,-8.569919,9.897904,-3.612412,4.135929,4.866009,-9.832411,0.158879,3.993787,2.642020,0.702661,-8.086886,4.648148,-8.126085,6.988376,-0.465607,4.216842,7.404304,-8.396024,7.899007,9.988417,9.905660,-5.681899,5.574811,4.031877,-4.517018,8.775926,1.942116,3.814675,6.466666,2.617016,-7.710587,-6.580789,-2.151414,1.736965,-7.958928,-0.461643,-2.193626,-3.995805,-7.840922,8.307385,7.625300,0.309912,4.256255,-8.554595,-2.266118,-8.689617,-0.731519,-0.053903,-1.290273,-9.424768,2.505333,-8.619035,4.656798,6.382186,2.797990,-0.157673,1.400146,8.948689,-9.485347,9.294688,-0.993382,2.320154,5.359689,2.014969,6.797264,-5.711179,-5.370762,1.232813,-4.555670,4.521386,8.677036,-9.661566,3.358973,1.007649,1.922103,-9.123395,-0.640754,-0.907379,-6.111543,1.930303,7.913579,-7.498603,9.618226,4.061980,-7.498901,2.415272,-1.552087,-6.747319,7.657788,-4.698096,-0.744856,-7.092034,-4.341376,-7.388551,-0.220854,6.067051,-3.367171,7.472405,1.511625,3.066077,5.988689,1.661667,-0.010025,-2.213228,6.533095,-0.369729,7.729449,-0.546344,9.237364,-7.161447,0.673874,4.252704,9.891120,8.593777,5.259125,-5.420375,3.364933,-6.577527,1.371790,5.449604,0.841418,6.453119,3.042755,2.086249,-6.616943,-5.359370,1.762485,3.067233,4.624741,7.058742,0.362139,1.161561,5.959212,-8.107619,-0.524257,6.843682,3.044908,5.185607,-0.204623,9.521316,-6.039341,-5.026013,8.033447,3.258854,-7.623157,5.633778,-6.535547,-8.888747,2.668023,7.083002,3.325300,2.349614,8.457460,0.409535,7.746907,-2.921969,-5.443834,4.234450,7.109833,-3.132680,2.258243,2.884491,9.811990,2.498668,6.380098,-3.139122,0.290306,3.535899,-1.748519,3.472041,-9.757027,-0.909580,-2.747510,-9.539532,-5.611389,-3.138396,3.787935,4.686117,3.858661,1.364975,7.106123,4.999320,3.991445,4.540993,5.872245,-4.736752,8.453947,9.582213,-0.284685,7.747673,-7.851030,9.276951,1.893435,-0.104494,6.688077,0.546043,-4.020323,-1.331381,-7.020041,3.800052,-4.657131,1.883032,-5.515827,6.275408,-1.898379,8.114227,-2.641162,-4.401275,-8.992080,8.952384,-8.307853,-7.463808,3.125962,1.598597,9.258439,-7.139803,-6.340826,3.805598,-5.208090,7.403621,4.492403,3.549706,5.499105,4.301991,9.882763,-8.285652,-8.587054,-5.990047,6.857148,4.641414,-7.613177,-4.581271,0.793870,-1.408434,-0.867621,-3.074389,-5.921396,-7.628921,-1.140201,1.838506,-5.758104,5.749390,9.964204,-5.755911,8.973212,2.551668,0.673681,-5.903447,0.085144,-5.216427,1.622351,9.732889,0.771686,2.236527,0.480059,2.359338,-8.032600,-4.146781,-1.404520,-6.909466,-1.628354,9.426223,0.639094,-6.886477,-6.196273,9.520911,-4.239253,-0.988515,-3.336839,4.267922,-7.324770,5.816300,2.479013,-3.895725,-8.807214,-6.451549,-0.382818,3.404826,9.213998,-4.670251,-7.714989,5.452448,-0.516142,-2.087687,-5.133042,9.494799,-7.679048,5.753975,-7.559371,4.469127,9.704374,-3.048629,-8.523100,5.041152,5.508499,7.230203,6.114769,-4.367574,-2.553149,-1.743151,-1.799752,-8.404873,-2.045277,8.611939,1.791296,-0.027706,-1.058016,6.724968,-3.745903,-7.447940,-4.072127,9.191173,4.958574,-7.652195,1.414125,-7.678157,-3.607795,-0.841504,-3.448130,7.618374,3.045619,-6.410776,-7.472217,-3.172463,3.646045,4.658875,-3.008880,8.092222,-2.511878,-3.326386,7.777817,-1.581694,7.778631,-9.080454,-7.537749,7.601795,1.868578,7.666836,9.036092,-6.729161,-7.082813,4.091818,8.547854,-4.423221,-0.172116,5.727920,1.682530,2.486042,-9.184082,9.920614,2.289438,-3.700124,-6.249877,4.980194,6.327330,-1.675668,5.346368,2.323461,3.326469,-9.176493,-2.123267,2.329152,3.772474,-7.556279,-7.801732,-2.685149,-9.062924,1.348645,-9.834371,5.283046,-2.197658,-8.199480,4.257062,-7.409724,0.627225,-1.041039,-2.380259,-5.686359,-8.332258,-0.443760,-1.206605,-0.618398,2.578951,5.059814,-7.072467,-6.053425,9.372287,-3.023237,-0.722777,7.407707,-0.956137,6.545265,6.490082,-2.185718,-7.959370,-0.293232,-2.463154,3.700964,-6.289224,3.380249,2.623489,-7.054570,-8.770683,8.181459,3.800634,6.931574,-3.080192,1.778742,-3.925118,4.699308,-6.752760,2.933314,9.159708,-9.199332,8.184064,-9.763093,2.594283,9.461290,-0.004229,-0.461098,1.911642,9.934485,-5.502085,1.190665,-6.392962,5.492311,9.288836,0.700105,-0.593776,-9.141033,-5.270382,-4.271982,1.010964,8.913402,7.627121,-9.942657,7.220784,-6.440291,-9.896166,-1.055662,7.035379,5.149708,-7.225635,5.622207,-3.686594,8.612269,-0.142653,5.401866,9.772747,1.966368,-7.007405,-0.492596,6.202321,-0.488927,-6.996613,2.393756,-4.685212,-4.524870,2.387339,4.193141,-3.858834,-1.345311,1.713284,-7.517816,6.666895,3.451451,8.716518,6.109162,-9.904855,-0.274095,0.077320,-0.250738,-8.797179,-5.937512,-0.852751,-6.805560,-7.101259,-5.632939,-9.516630,7.303052,-8.521509,0.502349,-9.699614,6.654529,-7.139266,2.805730,3.259344,-3.651863,7.349900,8.080996,-6.751330,-3.282721,9.744729,-5.248446,5.557399,4.895730,-1.678394,-4.684026,8.873113,-4.722962,6.053205,0.120366,7.238332,7.595733,3.114459,0.554706,-4.410214,-4.069737,-2.663631,6.488409,-0.237941,9.619984,3.896572,7.563260,0.132321,3.789876,-3.039478,4.192845,-8.720343,-8.519254,-0.951177,5.939309,7.793808,-6.237000,5.102323,3.758806,-7.485031,-2.142981,-3.373918,-2.516945,9.295723,9.991452,1.640473,-2.678333,7.220660,5.225605,-1.561534,-0.892468,-9.285697,4.033558,-4.724433,-2.831347,9.092559,-4.359577,-0.093930,-4.816829,-6.755516,2.118578,-1.560682,6.804174,-0.861567,8.397616,-4.775079,-6.651133,-5.694507,-8.154716,0.173160,8.737778,0.654007,-9.280313,1.464393,-9.836844,-0.341684,1.707796,4.550237,-4.486241,4.270206,-2.302384,1.654860,-3.780364,-2.246795,-3.632491,9.666930,-6.600525,-2.172348,9.700620,7.051268,7.194715,0.899879,2.836375,-2.155205,0.387259,0.524765,4.316433,-1.879112,5.251313,-9.419350,-9.113079,2.562779,-6.694057,-0.319539,7.266955,3.820812,7.534997,3.737071,4.800653,1.081082,7.890649,-0.027838,4.633995,1.589298,1.407044,8.439355,7.728480,4.296004,-3.855604,4.992948,9.468306,-5.850022,-6.711753,3.633014,1.210785,-1.888226,-9.364448,9.613657,2.440596,-8.260697,-5.243942,3.018560,-2.588794,-2.565392,-1.581332,4.958272,-8.965573,-5.820627,6.125015,9.610947,-4.369492,-6.567252,-1.152451,8.323073,-3.982872,2.285017,3.668941,-4.596429,0.894821,-1.268784,0.832173,1.541943,1.741245,-3.457763,-0.991961,-3.483438,2.576281,9.848445,-7.892925,2.850135,-6.655718,-3.075966,3.455456,7.198039,9.997759,-4.695517,3.186735,-6.355440,-1.382605,-9.627311,-9.358707,0.648283,8.308536,-3.087293,0.914770,-8.315088,-0.290385,4.165415,9.538782,-4.575947,-1.002142,4.393632,-3.766186,3.860502,-6.034036,4.606955,-0.701476,-5.159953,5.271989,8.448403,5.124249,-4.493019,-1.786323,5.151273,6.901523,-9.743137,9.941119,4.596660,-0.193010,-6.314507,-5.572923,4.217987,-4.389275,-3.888952,-5.628510,0.793061,2.886630,9.327925,8.562451,-8.729372,-4.339028,6.488697,-7.766581,-0.199698,0.182126,-7.958449,-5.089146,-5.147920,0.859973,0.248159,-2.810078,5.186140,-9.365490,-4.180998,-7.184653,-5.263526,9.577854,-9.570888,4.124797,-2.442106,9.514791,-5.679444,8.293027,-3.850448,-8.575582,-3.186688,-6.535722,-6.555037,8.264353,8.579216,2.518180,-0.499795,9.567161,4.115763,5.489907,2.999393,-4.130459,6.831681,-1.624421,-9.799076,1.389598,5.594866,1.312984,-8.219081,-6.125232,-4.815979,-0.190452,3.551846,1.093088,-1.762627,-2.607985,2.847569,7.665019,-6.041905,-4.209131,-9.967269,-7.410342,-2.278332,-0.485413,-9.380414,-7.352443,-4.212190,6.479584,-2.222389,-1.735853,-2.249548,-4.543328,0.279184,-6.355535,8.624795,9.864102,-0.833146,3.253383,5.796424,8.952399,9.590125,-8.200574,-3.479947,0.883218,-4.796733,7.576491,-8.149560,-8.607713,-4.534283,-8.312001,0.352196,1.817055,3.289419,-3.486250,-8.700934,-6.408168,9.367966,-0.784418,-6.184698,-9.528468,6.257284,5.379071,2.792396,-1.804609,-5.282134,7.607948,-8.796466,9.881455,-3.155536,-1.927784,-2.972052,-9.704180,9.153908,1.183186,-9.602677,-6.624202,-0.454599,0.716912,9.268198,6.555152,-0.251669,0.283793,1.443633,-1.473900,5.192961,7.391134,9.306511,0.243260,-7.218498,4.662768,1.419429,-8.283525,5.841469,4.778429,2.907115,4.947896,-0.853891,-1.020222,6.205511,7.928759,5.919576,-7.726383,-8.740218,1.848799,1.920553,4.055175,-6.331005,-5.688770,9.828108,-0.149677,-8.110957,4.261399,5.125346,-7.783446,-2.924313,7.795549,-1.075370,1.914541,0.677714,4.680614,5.860468,9.580174,2.774435,7.796987,-8.242146,2.351063,2.313212,9.913817,3.677407,-8.162401,1.267625,2.690072,6.919778,-8.757639,-3.700157,8.741137,-4.276694,3.968556,-3.353876,-9.995820,4.874361,9.632787,-1.282514,4.649622,1.585053,-8.419412,5.391556,-2.210242,-5.099418,5.132581,7.362578,-3.797460,-4.085854,7.431352,-9.524918,2.242485,4.875260,2.062210,4.846399,4.077754,-5.566714,0.524155,-0.193330,-7.439341,-1.815441,2.164101,8.887912,8.507580,6.126414,-3.316574,-0.044595,7.539398,4.755337,-0.947150,0.878444,5.211950,0.112916,6.729162,-2.132792,-0.324056,-3.639451,-0.333033,8.442939,5.611031,-2.392800,-0.378590,7.573009,9.246656,-2.996586,1.140250,6.693885,1.683759,0.989777,-3.649092,5.769401,-5.187758,-0.697733,3.250919,-6.519894,1.403475,-8.854894,7.537622,6.345861,-8.188546,-7.728237,-1.731770,-5.460749,-8.916869,-2.717700,-5.473301,5.417000,2.164547,0.749313,8.252761,4.622573,5.568388,7.344787,2.720512,9.678198,-0.621989,7.476734,8.200479,3.689206,6.821658,6.389196,2.251732,-2.921241,-7.298579,5.204234,3.719971,-8.833698,-9.225415,-6.201634,8.434823,-0.160857,6.285912,-8.820466,3.600845,6.064010,6.946385,-4.985412,5.628603,-3.782540,5.668024,-7.664303,-6.381226,4.041578,-9.635170,4.797701,3.667976,5.866901,8.423435,7.968166,5.843441,-1.261548,2.734886,3.738416,2.139831,4.699460,7.645967,-1.974739,-0.592842,4.546433,8.823081,-1.748014,-3.362833,9.980927,0.237602,-2.136817,9.054872,-5.999290,-2.147268,-1.178912,1.527721,-1.361512,2.504859,-3.882068,-1.449831,-6.627424,-9.460877,-4.929614,-8.851945,9.411017,-2.064107,0.392180,-5.438561,1.660477,4.761779,-6.828150,7.150278,-1.514015,2.971837,-3.598093,-4.645858,6.958303,-2.871597,1.104124,-6.031106,-8.358413,-1.311749,-4.961934,6.483337,0.511424,7.947228,4.949282,-0.418553,3.297201,3.515755,4.713190,-0.606975,-6.727076,-8.340639,-2.110444,-0.317112,-6.584386,-3.883267,7.574271,-2.787635,-2.639967,6.427104,-9.871003,7.434360,7.176190,8.607604,-2.204988,-1.479317,-8.567157,-3.220244,8.683601,-0.963429,-8.555135,-4.371288,-8.797951,-3.944566,2.078250,4.803157,-3.468972,5.312276,2.584377,-9.953626,0.724894,-6.265494,-0.697539,-2.496595,-5.357626,0.529462,4.338743,-2.040411,-0.663583,-9.944373,-5.286228,6.581337,9.545400,8.198618,8.712458,-0.899039,-3.752430,5.202138,-9.965154,-7.188500,-2.320107,8.538444,7.351024,4.545450,-6.095567,6.106876,6.213441,9.997072,-8.858740,7.762712,5.104733,-1.564778,0.393078,-7.104788,9.049808,-1.407741,-4.975431,7.060489,1.872453,2.750140,-7.951243,9.017416,7.666532,-2.099014,2.262282,3.028922,-5.672157,-2.322498,9.586633,8.318206,7.356328,-9.349457,4.573994,4.736395,4.053743,-9.197406,-7.279140,8.126818,5.576415,3.958152,-3.162358,2.343606,-2.222329,-5.138979,-8.031139,-0.471292,1.263053,6.729823,-9.966128,1.639695,2.806136,6.728986,7.123759,9.119466,6.823114,4.931590,8.115507,-9.029546,-7.851188,-8.224268,-6.081707,-4.332377,8.925573,-9.558060,2.096923,5.445578,1.628067,-5.450517,-8.967153,9.204009,-1.850703,8.800967,1.641036,5.390848,-7.873061,-1.279289,-3.921275,-2.297322,-8.922850,9.885045,-8.660578,-9.515922,4.763128,0.307182,-7.406692,6.604156,7.804839,2.241960,-2.679392,1.143536,-2.042574,4.903440,-0.322112,-0.892237,-9.038522,-0.493729,3.541943,2.437474,3.586290,-3.317748,7.792909,-7.983275,-1.750548,-1.217382,-6.653037,1.368149,0.720637,6.794652,-1.502910,6.214274,0.317124,7.943925,-4.725981,-1.617363,6.617393,-2.023341,-4.692829,-0.463395,-6.900496,-0.697273,-1.891884,5.457670,-4.910204,4.224345,-4.318255,-3.569766,3.835573,-8.450043,-7.121666,9.483781,4.807978,-2.072549,6.178475,-5.642119,7.850200,-6.637125,-5.275436,-2.192746,3.041026,1.668938,-7.919049,3.173883,-2.004580,0.922772,-7.182292,-2.974684,-6.403072,-6.987733,5.543551,6.933071,4.317619,-8.316024,0.509642,-8.756468,5.852998,3.427994,5.269209,2.229137,-9.250187,-0.058211,5.872617,6.074842,-8.579265,6.108792,-0.748492,-7.740865,0.316692,-9.701128,6.052261,7.374278,-0.629915,-4.605728,2.975550,8.643776,9.377457,4.963489,0.375754,-7.304294,-7.269954,4.979612,2.102268,-9.560909,7.899463,4.144660,9.955486,7.181992,9.198607,-7.040204,0.087249,3.843384,3.682386,4.122356,9.653897,-0.601034,-7.080070,-3.237978,-6.773643,-5.581062,7.264440,-3.552787,-0.731701,2.397439,-0.748075,-5.105277,2.751866,-1.936069,-5.976595,3.725714,1.067264,5.583366,-1.992271,6.067378,-3.202526,-4.927937,-6.706784,3.814613,-4.215526,-0.475055,-1.296837,-5.894886,-3.789017,-5.280535,-3.407699,-3.159374,-7.573085,4.339492,-3.860928,9.780447,-9.191944,-6.922917,-6.781434,9.262720,-8.730282,2.886645,6.875119,0.448726,-0.567268,-8.322838,3.247602,2.558210,8.981236,-8.730085,6.964845,-5.056739,5.225061,-4.456613,-5.561834,-3.020988,-2.477982,3.472263,9.070509,2.516392,8.779389,3.023315,4.388433,-2.992874,2.076660,-9.376560,-8.732079,1.835596,7.288687,0.299465,7.586442,3.375131,-4.462788,0.996121,7.952944,5.763262,8.452708,4.340263,0.303883,3.086189,0.616347,-5.528881,-5.649873,8.548216,3.546829,-6.014955,6.225085,-4.742887,-5.115871,9.987048,7.204802,-9.943812,7.080083,3.056173,0.137320,-0.473427,-6.057023,-6.623438,-0.762728,-0.172227,1.248681,-9.246697,-0.007543,-9.039850,2.450076,-4.704509,-6.087846,6.944306,7.438862,4.216010,7.333211,0.885911,-0.594882,-4.108624,5.324879,-9.481009,3.091374,6.528681,-3.675409,7.975555,-6.345424,-1.158221,-3.759654,-0.994821,-4.544902,6.012821,5.217701,0.219281,-1.646496,-2.385699,-0.719858,-1.448040,-1.891378,-8.929152,1.489743,-6.053770,1.310693,5.609566,-7.453999,2.237443,9.028860,-0.282380,8.698384,-4.484405,2.982268,-7.760882,6.092282,-3.853480,-8.481569,-0.022284,-8.055490,7.043371,7.226241,7.186302,9.352087,-5.748472,8.519094,1.566791,-6.226236,9.067422,8.885981,-7.759370,-6.622883,-5.939335,5.288069,1.576507,2.143207,7.666707,1.245115,-5.511585,-3.540852,8.987398,1.188355,-0.014845,-8.728044,5.590763,4.587874,-9.866424,-7.042649,6.793400,-1.600617,1.299454,8.431220,-2.075292,-2.104541,3.504581,-0.248490,-1.957646,-2.283015,8.107477,-7.952371,-2.595101,-6.362306,-6.051521,0.098225,-1.107446,-6.270830,0.951048,1.809956,-1.977528,-4.263939,-8.414175,-1.769172,-5.142717,4.525070,9.332198,-4.680807,-1.454936,-4.957951,-3.543194,-5.629183,9.189740,-6.404624,-8.136938,5.268527,6.064637,0.585696,-2.783324,5.296197,-4.789594,-3.540793,-2.123236,2.175045,-5.523897,1.871382,2.248460,2.595014,-7.207880,9.557435,1.317030,9.809428,-9.992564,-6.777179,-9.820646,3.462290,2.820336,-7.482402,-2.203309,-4.741406,-0.355680,8.537304,4.361351,-9.206325,6.772839,-4.145173,-0.726923,2.181719,-9.045410,9.124989,0.766114,3.990267,2.609008,4.631383,2.399594,-7.314470,4.994975,6.256888,-8.438892,6.340870,5.408521,5.379912,7.701924,-0.939161,-4.910378,0.476459,-9.412871,-3.286025,-8.341245,-9.786898,5.775755,8.122280,-1.910015,7.547954,6.733260,-4.014207,6.271348,-8.055061,5.797242,-2.676189,2.873668,4.233095,5.969050,9.309680,2.501399,3.879067,-6.978389,-7.327845,-6.220726,6.916305,-1.403374,-9.492246,8.460460,-2.469835,-2.791663,6.006599,-8.655144,5.156444,-2.926007,-6.695789,-0.344424,4.348814,-5.029570,-8.564676,2.272026,-0.020630,2.094233,6.929962,-5.918778,5.955179,7.165873,-7.235596,-7.717332,9.294782,-0.335184,-5.521942,5.471773,6.357340,1.592687,-0.736385,5.522849,-5.522865,-1.397815,-2.213306,-4.387943,4.480581,-9.207646,8.625122,8.972837,7.443438,-7.018769,8.199066,0.633019,-1.760913,-4.992676,-0.095359,6.485764,-0.608599,-9.446203,-1.610952,7.640058,-7.521074,2.278559,-7.503016,-1.485795,-7.205571,1.068259,1.116594,-6.123899,-2.162510,-4.980721,6.177449,0.343545,8.438473,-0.658451,-6.156975,9.838276,4.210155,9.221393,-6.455889,9.277958,-3.152731,-0.150649,-2.686916,3.130540,1.132490,3.596504]], dtype = "float32")#candidate|19331|(1, 2400)|const|float32
call_19328 = relay.TupleGetItem(func_4093_call(relay.reshape(const_19329.astype('float64'), [14, 8, 8]), relay.reshape(const_19330.astype('float32'), [700,]), relay.reshape(const_19331.astype('float32'), [2400,]), ), 2)
call_19332 = relay.TupleGetItem(func_4097_call(relay.reshape(const_19329.astype('float64'), [14, 8, 8]), relay.reshape(const_19330.astype('float32'), [700,]), relay.reshape(const_19331.astype('float32'), [2400,]), ), 2)
var_19342 = relay.var("var_19342", dtype = "float32", shape = (11, 2400))#candidate|19342|(11, 2400)|var|float32
bop_19343 = relay.greater(const_19331.astype('bool'), var_19342.astype('bool')) # shape=(11, 2400)
func_18013_call = mod.get_global_var('func_18013')
func_18015_call = mutated_mod.get_global_var('func_18015')
call_19348 = relay.TupleGetItem(func_18013_call(), 0)
call_19349 = relay.TupleGetItem(func_18015_call(), 0)
output = relay.Tuple([call_19319,call_19328,const_19329,const_19330,bop_19343,call_19348,])
output2 = relay.Tuple([call_19320,call_19332,const_19329,const_19330,bop_19343,call_19349,])
func_19370 = relay.Function([var_19342,], output)
mod['func_19370'] = func_19370
mod = relay.transform.InferType()(mod)
mutated_mod['func_19370'] = func_19370
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19371 = relay.var("var_19371", dtype = "float32", shape = (11, 2400))#candidate|19371|(11, 2400)|var|float32
func_19370_call = mutated_mod.get_global_var('func_19370')
call_19372 = func_19370_call(var_19371)
output = call_19372
func_19373 = relay.Function([var_19371], output)
mutated_mod['func_19373'] = func_19373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17138_call = mod.get_global_var('func_17138')
func_17140_call = mutated_mod.get_global_var('func_17140')
call_19377 = relay.TupleGetItem(func_17138_call(), 0)
call_19378 = relay.TupleGetItem(func_17140_call(), 0)
uop_19419 = relay.acos(call_19377.astype('float64')) # shape=(15, 9, 9)
uop_19421 = relay.acos(call_19378.astype('float64')) # shape=(15, 9, 9)
func_592_call = mod.get_global_var('func_592')
func_594_call = mutated_mod.get_global_var('func_594')
var_19423 = relay.var("var_19423", dtype = "int8", shape = ())#candidate|19423|()|var|int8
call_19422 = func_592_call(relay.reshape(var_19423.astype('int8'), []))
call_19424 = func_592_call(relay.reshape(var_19423.astype('int8'), []))
output = relay.Tuple([uop_19419,call_19422,var_19423,])
output2 = relay.Tuple([uop_19421,call_19424,var_19423,])
func_19426 = relay.Function([var_19423,], output)
mod['func_19426'] = func_19426
mod = relay.transform.InferType()(mod)
mutated_mod['func_19426'] = func_19426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19427 = relay.var("var_19427", dtype = "int8", shape = ())#candidate|19427|()|var|int8
func_19426_call = mutated_mod.get_global_var('func_19426')
call_19428 = func_19426_call(var_19427)
output = call_19428
func_19429 = relay.Function([var_19427], output)
mutated_mod['func_19429'] = func_19429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18603_call = mod.get_global_var('func_18603')
func_18605_call = mutated_mod.get_global_var('func_18605')
call_19437 = relay.TupleGetItem(func_18603_call(), 0)
call_19438 = relay.TupleGetItem(func_18605_call(), 0)
func_14608_call = mod.get_global_var('func_14608')
func_14612_call = mutated_mod.get_global_var('func_14612')
const_19479 = relay.const([-4,4,-6,2,1,-1,10,10,-7,8,-2,1,7,-1,-2,-8,1,-2,-6,-7,2,5,4,-1,-4,10,-9,7,-2,-6,1,1,-7,-10,-9,-1,-5,-5,6,3,-9,4,-3,4,9,2,-6,-3,7,-6,-10,-9,5,-7,2,-9,-10,10,5,-1,-6,6,5,6,5,-8,1,2,-1,-7,7,-7,2,-4,-1,-1,7,2,-9,6,2,-8,1,-1,9,9,-5,-6,-4,-1,-5,-6,4,-6,6,-6,8,-1,6,-5,-9,2,3,-10,10,3,-6,10,9,-2,8,3,-1,-6,8,3,-6,-3,5,-5,7,-10,9,4,6,2,5,1,-2,5,8,7,-5,10,-6,-4,-5,5,-6,3,-6,-7,10,6,-7,-2,-9,7,-1,-3,-4,-9,3,4,-4,3,-9,8,-10,-3,-5,2,-4,-5,7,-4,-5,9,-7,-9,-9,-1,-5,-10,-3,-4,6,2,6,-6,7,2,-5,2,-6,-4,-7,3,-4,-1,-6,7,2,5,-9,10,3,8,5,-9,-4,3,-8,5,1,-2,10,10,-1,9,6,-7,-1,6,-6,-6,7,-2,-8,-6,-3,-6,8,-3,9,-10,-1,-5,-2,10,-5,10,8,5,-1,6,1,-4,-8,-9,-1,3,4,6,-6,-5,5,-10,-7,2,10,-1,10,10,-2,-6,-8,7,-4,1,1,10,1,-2,9,-6,2,9,-3,-1,-10,10,-3,-3,1,-6,7,-10,-9,7,-6,4,2,-9,4,2,6,-1,8,-5,-5,-1,10,3,2,5,4,-6,-5,-1,-7,-3,2,2,-10,-9,2,9,1,-1,-1,1,-10,-2,-1,5,6,1,-4,10,-3,-8,10,7,9,-4,-6,8,3,-2,2,4,-5,-8,9,-2,-8,7,10,-9,2,1,-2,6,8,-10,3,-8,9,9,3,-2,2,9,3,-10,5,5,-10,-3,-8,1,-6,-2,-5,5,-2,9,6,5,7,-6,-7,-10,-1,9,5,-1,-9,6,-5,1,9,9,-7,-7,-10,-7,-4,-5,-9,4,-4,-4,9,-4,4,2,-3,-1,5,-5,8,3,-8,-9,-5,-2,10,-10,8,5,-9,-5,8,-5,3,10,-1,-5,3,7,-7,-5,-4,5,-10,4,-7,-4,-5,10,8,-1,-4,9,10,-7,4,3,-8,-8,1,8,10,-5,-10,7,6,8,-4,-9,-2,3,-8,-3,-9,3,-2,-9,2,1,8,1,-6,4,-5,-6,7,4,-10,-2,-8,10,-5,-6,3,-10,-5,-5,-9,3,-3,-2,10,6,4,8,4,-6,9,7,-9,-4,-7,7,9,-1,-9,-3,-2,9,-8,10,7,10,-5,-7,-5,1,10,-1,6,-1,4,3,2,1,-9,1,-6,1,1,8,-8,1,6,9,1,-6,2,2,1,6,-6,-7,10,-6,7,9,2,5,10,-10,2,10,7,-9,-7,2,2,6,9,-4,-7,-2,-3,-6,1,-5,-2,-6,-7,9,2,7,-9,7,-6,-4,6,-1,5,1,3,-8,3,4,-10,3,-2,-5,5,3,-5,-6,5,9,7,5,-9,5,-6,1,-1,10,-7,8,-9,5,8,-4,-1,2,-6,-9,9,-9,2,2,6,-1,-7,5,8,9,-3,8,9,-5,-8,-1,8,-3,-2,6,-7,1,3,-1,7,-8,4,-8,7,-1,8,1,4,4,9,3,6,1,9,-2,-3,-7,-8,3,8,10,5,-2,3,4,8,9,9,-3,5,5,6,6,-8,-9,2,4,1,6,-4,8,-10,-5,-9,7,4,2,5,5,-7,-2,4,-6,-4,8,5,-9,5,3,-2,7,-6,9,-9,7,-9,-4,-6,7,-5,7,5,4,-8,3,1,8,-1,9,1,5,-4,4,-1,2,-10,-7,-3,-4,-2,-4,6,-8,-9,6,-2,4,2,-8,1,-1,6,-5,-3,-3,3,-5,9,8,2,-10,7,-2,1,3,9,2,-6,-6,3,1,7,7,-1,4,10,-10,9,7,-2,-4,8,8,-1,10,-6,-2,-9,8,3,-5,-7,2,-9,-8,9,3,7,1,6,4,2,-4,6,-3,6,-1,-5,1,-2,-6,-2,-10,2,7,-3,-1,-6,8,-9,-10,-10,-9,6,10,10,10,-7,-9,2,-7,8,1,-5,5,-9,8,-9,-4,-9,-4,-10,-1,5,-6,-7,-3,10,-8,-3,8,1,9,5,5,-8,4,-1,7,-6,-4,-7,-9,-1,4,1,5,-10,-10,-8,10,1,-5,9,-10,-6,-10,-3,10,6,-9,-5,-9,-7,-1,-3,4,-5,8,-3,-10,7,2,7,-6,-7,9,7,7,4,-10,1,3,-3,1,-3,4,9,10,9,8,-8,6,-3,-1,4,-6,-7,2,-3,-7,4,-4,9,-10,9,2,4,-3,4,-6,7,-3,2,-4,6,1,3,2,9,-10,-9,8,-10,-10,6,1,9,-8,9,8,-3,5,4,10,1,-4,2,-6,4,7,2,-3,-3,-2,3,8,-6,-4,2,6,3,6,3,-8,-7,-8,4,-8,2,-9,-7,-1,-10,5,-10,-7,-2,-10,4,1,4,10,1,-7,5,8,-3,-7,5,-6,3,-7,8,-10,-5,6,10,-9,2,-4,2,-3,10,-7,-1,9,8,-9,-3,-1,-9,8,-10,10,3,-3,5,-9,3,9,10,-10,-4,-7,7,5,-2,5,2,-6,-9,-7], dtype = "uint16")#candidate|19479|(1024,)|const|uint16
var_19480 = relay.var("var_19480", dtype = "float32", shape = (630,))#candidate|19480|(630,)|var|float32
call_19478 = relay.TupleGetItem(func_14608_call(relay.reshape(const_19479.astype('uint16'), [1024,]), relay.reshape(var_19480.astype('float32'), [630,]), ), 4)
call_19481 = relay.TupleGetItem(func_14612_call(relay.reshape(const_19479.astype('uint16'), [1024,]), relay.reshape(var_19480.astype('float32'), [630,]), ), 4)
output = relay.Tuple([call_19437,call_19478,const_19479,var_19480,])
output2 = relay.Tuple([call_19438,call_19481,const_19479,var_19480,])
func_19483 = relay.Function([var_19480,], output)
mod['func_19483'] = func_19483
mod = relay.transform.InferType()(mod)
var_19484 = relay.var("var_19484", dtype = "float32", shape = (630,))#candidate|19484|(630,)|var|float32
output = func_19483(var_19484)
func_19485 = relay.Function([var_19484], output)
mutated_mod['func_19485'] = func_19485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16303_call = mod.get_global_var('func_16303')
func_16305_call = mutated_mod.get_global_var('func_16305')
call_19594 = func_16303_call()
call_19595 = func_16303_call()
output = relay.Tuple([call_19594,])
output2 = relay.Tuple([call_19595,])
func_19596 = relay.Function([], output)
mod['func_19596'] = func_19596
mod = relay.transform.InferType()(mod)
output = func_19596()
func_19597 = relay.Function([], output)
mutated_mod['func_19597'] = func_19597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19778 = relay.var("var_19778", dtype = "float32", shape = (7, 3, 4))#candidate|19778|(7, 3, 4)|var|float32
var_19779 = relay.var("var_19779", dtype = "float32", shape = (7, 3, 4))#candidate|19779|(7, 3, 4)|var|float32
bop_19780 = relay.power(var_19778.astype('float32'), relay.reshape(var_19779.astype('float32'), relay.shape_of(var_19778))) # shape=(7, 3, 4)
output = bop_19780
output2 = bop_19780
func_19786 = relay.Function([var_19778,var_19779,], output)
mod['func_19786'] = func_19786
mod = relay.transform.InferType()(mod)
var_19787 = relay.var("var_19787", dtype = "float32", shape = (7, 3, 4))#candidate|19787|(7, 3, 4)|var|float32
var_19788 = relay.var("var_19788", dtype = "float32", shape = (7, 3, 4))#candidate|19788|(7, 3, 4)|var|float32
output = func_19786(var_19787,var_19788,)
func_19789 = relay.Function([var_19787,var_19788,], output)
mutated_mod['func_19789'] = func_19789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18522_call = mod.get_global_var('func_18522')
func_18524_call = mutated_mod.get_global_var('func_18524')
call_19845 = relay.TupleGetItem(func_18522_call(), 1)
call_19846 = relay.TupleGetItem(func_18524_call(), 1)
func_14173_call = mod.get_global_var('func_14173')
func_14175_call = mutated_mod.get_global_var('func_14175')
var_19853 = relay.var("var_19853", dtype = "int8", shape = ())#candidate|19853|()|var|int8
call_19852 = relay.TupleGetItem(func_14173_call(relay.reshape(var_19853.astype('int8'), [])), 0)
call_19854 = relay.TupleGetItem(func_14175_call(relay.reshape(var_19853.astype('int8'), [])), 0)
output = relay.Tuple([call_19845,call_19852,var_19853,])
output2 = relay.Tuple([call_19846,call_19854,var_19853,])
func_19855 = relay.Function([var_19853,], output)
mod['func_19855'] = func_19855
mod = relay.transform.InferType()(mod)
var_19856 = relay.var("var_19856", dtype = "int8", shape = ())#candidate|19856|()|var|int8
output = func_19855(var_19856)
func_19857 = relay.Function([var_19856], output)
mutated_mod['func_19857'] = func_19857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17708_call = mod.get_global_var('func_17708')
func_17710_call = mutated_mod.get_global_var('func_17710')
call_19888 = relay.TupleGetItem(func_17708_call(), 0)
call_19889 = relay.TupleGetItem(func_17710_call(), 0)
func_13260_call = mod.get_global_var('func_13260')
func_13263_call = mutated_mod.get_global_var('func_13263')
var_19893 = relay.var("var_19893", dtype = "uint16", shape = (1024,))#candidate|19893|(1024,)|var|uint16
call_19892 = relay.TupleGetItem(func_13260_call(relay.reshape(var_19893.astype('uint16'), [1024,])), 0)
call_19894 = relay.TupleGetItem(func_13263_call(relay.reshape(var_19893.astype('uint16'), [1024,])), 0)
output = relay.Tuple([call_19888,call_19892,var_19893,])
output2 = relay.Tuple([call_19889,call_19894,var_19893,])
func_19896 = relay.Function([var_19893,], output)
mod['func_19896'] = func_19896
mod = relay.transform.InferType()(mod)
mutated_mod['func_19896'] = func_19896
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19897 = relay.var("var_19897", dtype = "uint16", shape = (1024,))#candidate|19897|(1024,)|var|uint16
func_19896_call = mutated_mod.get_global_var('func_19896')
call_19898 = func_19896_call(var_19897)
output = call_19898
func_19899 = relay.Function([var_19897], output)
mutated_mod['func_19899'] = func_19899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11796_call = mod.get_global_var('func_11796')
func_11797_call = mutated_mod.get_global_var('func_11797')
call_19967 = func_11796_call()
call_19968 = func_11796_call()
func_14486_call = mod.get_global_var('func_14486')
func_14487_call = mutated_mod.get_global_var('func_14487')
call_19979 = relay.TupleGetItem(func_14486_call(), 0)
call_19980 = relay.TupleGetItem(func_14487_call(), 0)
func_13059_call = mod.get_global_var('func_13059')
func_13062_call = mutated_mod.get_global_var('func_13062')
const_19985 = relay.const(3.908619, dtype = "float64")#candidate|19985|()|const|float64
var_19986 = relay.var("var_19986", dtype = "bool", shape = (495,))#candidate|19986|(495,)|var|bool
call_19984 = relay.TupleGetItem(func_13059_call(relay.reshape(const_19985.astype('float64'), []), relay.reshape(var_19986.astype('bool'), [495,]), ), 1)
call_19987 = relay.TupleGetItem(func_13062_call(relay.reshape(const_19985.astype('float64'), []), relay.reshape(var_19986.astype('bool'), [495,]), ), 1)
func_15200_call = mod.get_global_var('func_15200')
func_15201_call = mutated_mod.get_global_var('func_15201')
call_19997 = relay.TupleGetItem(func_15200_call(), 0)
call_19998 = relay.TupleGetItem(func_15201_call(), 0)
func_12277_call = mod.get_global_var('func_12277')
func_12279_call = mutated_mod.get_global_var('func_12279')
call_20006 = relay.TupleGetItem(func_12277_call(), 3)
call_20007 = relay.TupleGetItem(func_12279_call(), 3)
func_17968_call = mod.get_global_var('func_17968')
func_17970_call = mutated_mod.get_global_var('func_17970')
const_20010 = relay.const([-3,-5,-5,-7,-3,2,-1,10,-10,-10,-3,-3,9,-8,1,-8,4,-3,-2,6,7,7,-10,7,-1,-2,5,9,3,9,-1,-10,10,-6,4,-10,-9,-8,-5,-9,-9,-3,6,-8,-9,5,-6,5,-6,8,4,-10,6,3,10,10,-5,-6,4,10,-3,-5,9,4,-10,7,2,-8,3,2,3,5,-4,9,-4,-3,-5,5,8,-1,-2,4,-4,-4,4,-2,-5,-5,9,7,4,-10,8,-2,3,-7,-10,8,-5,-2,-8,6,-5,-10,-6,6,9,-8,1,5,1,-10,-7,8,-1,-1,-7,2,-9,-6,1,4,10,-1,9,-5,-10,-5,3,8,-4,-5,-5,4,-9,-8,2,4,-3,-1,1,-5,10,9,-3,-9,6,-9,1,7,-6,2,-9,10,-9,4,-8,2,-9,3,-8,1,6,-8,-5,-7,-10,-9,-5,-10,-9,-4,-3,6,9,-6,-2,2,-8,3,5,-6,-8,3,3,8,10,-10,-10,7,-6,6,-1,-3,1,6,-5,1,9,-7,-9,-6,-6,-2,-5,-8,5,8,-4,-6,-9,1,7,9,7,-8,-10,-7,-3,5,-9,10,6,-1,2,-7,2,-7,1,-4,-2,7,9,10,-5,1,-7,10,-10,4,-8,3,9,10,-7,-10,-7,3,-3,9,8,-1,-10,6,2,1,1,10,5,-1,4,-1,8,-8,-7,-8,6,1,2,7,-9,4,4,1,-5,2,-2,2,-7,3,-7,10,-4,-3,-8,2,1,-7,-1,-6,1,-6,1,4,-8,3,-2,1,3,2,-6,-1,10,6,8,-10,2,-1,5,2,-6,1,9,2,7,5,8,-2,6,4,2,3,1,8,3,1,6,-5,-3,-8,3,-6,1,-1,-8,1,10,-3,-9,-7,10,2,-10,-2,4,-3,-3,-7,-7,-1,5,4,-7,-4,-7,-1,-1,-6,9,-3,-5,-7,-7,5,5,10,10,-3,10,-5,10,-7,-8,1,-10,10,3,6,-4,-4,6,6,6,5,7,-7,8,10,-9,-5,7,4,3,-10,8,-5,-5,-2,-10,-1,9,-6,3,4,10,9,-5,7,-3,-6,-10,7,1,8,-8,-10,6,5,3,1,1,1,5,5,-5,-8,1,10,-7,-5,5,4,-3,-3,2,-10,-4,-8,-10,-6,5,10,9,10,-8,3,-10,9,7,10,3,-2,-2,7,-7,-7,-5,8,8,-10,-3,-4,-1,8,4,-7,1,-6,-2,-5,6,-1,2,4,7,8,8,-7,-6,7,5,7,-5,-9,5,-8,-7,-1,10,10,-3,9,2,-2,-3,8,-5,3,7,-9,-7,3,-7,4,-4,-5,3,-8,-2,-5,1,2,-8,6,-1,8,-3,4,7,-7,2,-8,8,2,-8,6,8,-3,-4,-2,5,5,-2,8,-10,-2,1,-9,-8,10,8,3,-3,-4,7,-6,-7,10,1,-3,-7,3,-5,-8,3,-8,3,7,-10,-6,5,1,2,-3,9,4,-1,3,-9,-10,8,-3,1,-10,-9,10,-8,-7,-2,3,-6,-9,-6,-4,5,9,-2,-6,-10,-4,3,-4,4,-1,-6,8,-3,-9,-9,-6,-7,-8,5,9,-2,-8,-6,-8,-6,7,-5,-3,1,-9,-7,7,-8,-10,-10,-2,-4,1,-3,-2,-10,-10,-3,-5,-7,7,7,-7,-8,2,9,-4,2,-3,-4,5,-4,-1,10,-3,8,2,-3,-4,7,3,-8,7,2,-9,4,2,-9,-5,9,-5,-10,-4,-5,6,-4,5,5,6,-3,4,6,-5,1,3,8,6,-4,-10,1,-8,6,1,-7,-9,-1,-10,-10,-2,-5,-10,-3,-10,1,4,8,10,-7,-7,5,9,-2,-3,-1,5,1,8,4,-1,-10,8,8,5,-7,4,-10,-10,-9,5,1,8,5,-6,-6,3,-3,-7,9,10,6,-9,-4,-9,3,5,-5,-6,8,9,-10,-3,5,5,2,1,-7,4,-1,-4,-8,8,9,4,-5,-5,-9,-7,-6,10,8,-6,2,-8,-3,-7,1,-4,9,-10,-3,9,-3,8,-1,-9,-8,5,5,2,6,-8,-5,7,-4,-8,4,-1,-6,-6,5,-9,10,-4,-7,-2,-6,-2,-7,-4,-8,8,-10,8,-5,-6,-2,5,10,7,-8,2,3,4,3,-9,-10,2,5,9,-6,2,9,10,-9,-7,-7,-10,3,8,-1,6,7,3,-9,4,7,-3,-5,6,-9,-2,5,7,-7,-3,-4,-2,-8,3,-7,-3,4,1,-9,7,3,4,-3,-6,-8,1,-10,4,-9,-7,5,1,6,-1,10,-2,-7,-10,9,-3,7,-8,-8,-6,9,-5,3,-6,-9,-1,4,1,10,-4,-7,4,2,10,-4,8,10,-8,1,-10,-10,9,-4,7,-2,-3,-1,-3,-8,-4,-1,-8,8,-4,1,-9,-6,-6,1,-4,-8,3,3,2,-1,6,9,-5,-9,7,-4,10,5,10,-1,8,-3,-7,-9,10,3,3,9,10,6,9,-4,-10,6,6,6,5,6,-6,10,6,1,9,9,9,7,-7,-8,9,-9,-1,10,4,1,3,-7,7,10,7,5,7,5,-2,-3,9,5,-4,-8,-1,10,2,-2,-5,-7,4,-10,4,8,-10,-5,10,-9,-7,5,-5,1,-4,6,-9,-2,5,-5,7,2,-4,-6,-1,1,1,-5,2,-4,2,6,5,4,9,-8,5,-6,9], dtype = "uint16")#candidate|20010|(1024,)|const|uint16
call_20009 = relay.TupleGetItem(func_17968_call(relay.reshape(const_20010.astype('uint16'), [1024,])), 1)
call_20011 = relay.TupleGetItem(func_17970_call(relay.reshape(const_20010.astype('uint16'), [1024,])), 1)
bop_20030 = relay.greater_equal(const_20010.astype('bool'), call_19984.astype('bool')) # shape=(1024,)
bop_20033 = relay.greater_equal(const_20010.astype('bool'), call_19987.astype('bool')) # shape=(1024,)
func_12475_call = mod.get_global_var('func_12475')
func_12478_call = mutated_mod.get_global_var('func_12478')
call_20037 = func_12475_call(relay.reshape(call_19979.astype('float32'), [15, 9, 9]))
call_20038 = func_12475_call(relay.reshape(call_19979.astype('float32'), [15, 9, 9]))
func_15613_call = mod.get_global_var('func_15613')
func_15615_call = mutated_mod.get_global_var('func_15615')
var_20042 = relay.var("var_20042", dtype = "float64", shape = (25, 10))#candidate|20042|(25, 10)|var|float64
call_20041 = relay.TupleGetItem(func_15613_call(relay.reshape(var_20042.astype('float64'), [250,])), 2)
call_20043 = relay.TupleGetItem(func_15615_call(relay.reshape(var_20042.astype('float64'), [250,])), 2)
output = relay.Tuple([call_19967,call_19979,const_19985,var_19986,call_19997,call_20006,call_20009,bop_20030,call_20037,call_20041,var_20042,])
output2 = relay.Tuple([call_19968,call_19980,const_19985,var_19986,call_19998,call_20007,call_20011,bop_20033,call_20038,call_20043,var_20042,])
func_20046 = relay.Function([var_19986,var_20042,], output)
mod['func_20046'] = func_20046
mod = relay.transform.InferType()(mod)
var_20047 = relay.var("var_20047", dtype = "bool", shape = (495,))#candidate|20047|(495,)|var|bool
var_20048 = relay.var("var_20048", dtype = "float64", shape = (25, 10))#candidate|20048|(25, 10)|var|float64
output = func_20046(var_20047,var_20048,)
func_20049 = relay.Function([var_20047,var_20048,], output)
mutated_mod['func_20049'] = func_20049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15870_call = mod.get_global_var('func_15870')
func_15872_call = mutated_mod.get_global_var('func_15872')
call_20146 = relay.TupleGetItem(func_15870_call(), 0)
call_20147 = relay.TupleGetItem(func_15872_call(), 0)
func_11261_call = mod.get_global_var('func_11261')
func_11263_call = mutated_mod.get_global_var('func_11263')
call_20161 = relay.TupleGetItem(func_11261_call(), 0)
call_20162 = relay.TupleGetItem(func_11263_call(), 0)
output = relay.Tuple([call_20146,call_20161,])
output2 = relay.Tuple([call_20147,call_20162,])
func_20183 = relay.Function([], output)
mod['func_20183'] = func_20183
mod = relay.transform.InferType()(mod)
output = func_20183()
func_20184 = relay.Function([], output)
mutated_mod['func_20184'] = func_20184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18813_call = mod.get_global_var('func_18813')
func_18814_call = mutated_mod.get_global_var('func_18814')
call_20197 = relay.TupleGetItem(func_18813_call(), 0)
call_20198 = relay.TupleGetItem(func_18814_call(), 0)
func_16050_call = mod.get_global_var('func_16050')
func_16052_call = mutated_mod.get_global_var('func_16052')
const_20200 = relay.const([-3,-8,-10,4,7,-5,7,1,-2,-4,-10,-2,-6,-9,3,7,-6,-8,-3,-6,6,5,3,-3,-3,-5,-9,5,8,-8,-1,8,-8,-4,9,-5,-3,10,4,-10,10,1,-2,7,-8,10,-8,7,-5,10,10,10,-4,9,4,7,5,-5,4,-7,-7,-2,-7,2,1,-5,9,-4,6,3,1,5,-7,2,-4,-4,10,-5,-6,-9,1,7,9,-3,3,6,5,1,-4,3,-6,9,4,2,-3,6,7,5,7,3,-5,5,2,4,-2,4,-4,3,6,-8,6,-2,9,1,5,-7,6,-10,9,6,1,-9,-4,-2,6,9,6,-7,1,3,3,-6,-4,-9,2,-6,5,9,6,10,-1,-7,2,-2,-3,9,-4,7,5,3,-9,-2,2,6,3,1,-8,-9,-2,3,5,-3,1,9,6,-5,8,-1,-1,10,6,-5,10,5,6,-9,-2,-2,-2,10,10,3,7,8,-5,-1,10,3,2,3,-6,9,-7,-2,1,-9,1,6,-7,5,3,-1,2,4,-2,1,1,7,-10,-9,2,1,9,1,-4,-8,-10,9,-4,5,-9,-3,8,-10,-10,-1,-6,-6,-10,1,-3,10,-9,-7,-3,7,1,-2,-2,9,-1,4,3,-2,-9,8,3,7,-8,-5,1,2,-3,-2,9,7,-2,-9,1,7,-6,3,-2,3,9,10,9,-1,-10,-9,4,1,7,2,-3,9,3,-1,4,-6,2,-2,-2,5,-8,1,8,-10,3,-4,-1,8,-7,-1,-4,6,7,-9,3,-10,-8,-4,2,3,4,-2,10,-10,-8,10,10,-10,-5,3,-2,-8,-4,7,6,1,-7,6,-2,6,5,-2,1,-1,10,6,-9,-4,-7,-8,1,5,-2,-5,5,-4,7,-7,-9,-9,-4,-3,-9,5,8,-1,5,-6,6,3,5,4,-5,-2,-9,5,4,-6,7,-1,7,3,-7,-8,2,-4,9,9,-1,8,4,5,3,2,-5,4,-2,-1,-6,2,2,-5,6,-7,-6,8,10,9,7,1,2,-3,2,5,-4,-8,-7,-7,8,1,-9,-4,-6,-2,4,-6,-1,-3,2,-3,-9,3,5,-8,-4,-6,9,3,3,-10,-9,3,3,2,-6,-2,-5,10,6,10,-6,-4,8,-2,-3,10,-9,9,-1,-7,-6,-1,-7,1,-8,3,9,2,-7,8,7,1,1,7,-2,10,-7,-9,3,-6,-2,6,10,-9,-2,-6,-5,4,6,-9,-10,-6,-1,9,-6,-2,8,8,-3,5,-3,4,-8,7,4,4,-4,-8,5,6,6,10,7,-2,-6,-8,1,-9,2,5,-2,7,9,-1,-5,-6,9,7,-5,-6,7,9,6,7,2,4,-10,1,6,-6,1,6,-9,5,1,2,-7,-7,7,-3,-7,4,-7,9,-7,6,6,-9,4,-6,9,-2,10,-1,5,-7,-10,10,-8,-1,-3,-4,-1,-5,-8,10,10,4,-3,-9,9,-1,-9,-6,-1,3,-6,-4,-9,-1,-1,-2,7,10,-3,8,-7,2,-9,4,-7,-5,-3,1,-9,8,-5,10,-10,-2,3,4,-9,5,-7,10,-7,9,6,-3,2,7,-4,9,-1,-7,-1,2,9,9,-10,2,-4,7,-10,-6,-4,2,-2,-3,2,-7,3,2,-9,-10,10,6,4,5,-6,8,6,9,9,-10,2,-3,-7,4,5,-6,-7,-8,-6,5,-6,3,1,9,-3,-2,-8,-7,9,4,-7,-1,-1,-7,4,10,-5,1,6,-9,-2,-2,-5,7,4,9,10,-8,-1,-1,-7,4,-5,-9,4,7,-8,-6,2,6,-7,-7,-5,9,10,-8,10,-8,-6,7,4,7,5,-4,9,2,2,-2,-6,2,2,2,1,-8,-6,8,8,-3,-9,1,4,-3,-5,-5,7,-5,-7,-10,7,-7,4,5,3,7,5,-1,3,5,-10,-7,8,-5,-10,-7,-6,4,-2,-1,8,-8,-6,-2,-2,7,9,-10,-9,-4,-1,-10,5,-6,-2,3,-5,-3,-9,-9,3,-4,3,1,-8,-3,-8,-5,-4,2,-8,-7,8,-3,4,8,10,-4,-6,5,2,3,10,4,1,-1,3,-1,8,7,-5,-1,-9,-10,-10,8,-4,3,-3,7,5,2,-5,-10,-4,-5,4,-6,3,-9,-10,6,-10,-7,7,8,3,9,-2,3,8,6,5,4,-7,-2,1,-10,-8,5,-2,-7,-2,5,7,-3,7,6,3,-2,4,7,4,6,6,-9,-6,-5,5,6,9,9,-9,8,7,-4,5,-8,-1,-3,8,7,-10,-4,-4,9,10,-1,-6,-2,-10,6,10,-4,-10,1,-9,-6,3,-4,-10,2,4,8,-4,-3,-9,-8], dtype = "uint32")#candidate|20200|(896,)|const|uint32
call_20199 = relay.TupleGetItem(func_16050_call(relay.reshape(const_20200.astype('uint32'), [896,])), 4)
call_20201 = relay.TupleGetItem(func_16052_call(relay.reshape(const_20200.astype('uint32'), [896,])), 4)
func_10426_call = mod.get_global_var('func_10426')
func_10428_call = mutated_mod.get_global_var('func_10428')
call_20204 = relay.TupleGetItem(func_10426_call(), 0)
call_20205 = relay.TupleGetItem(func_10428_call(), 0)
output = relay.Tuple([call_20197,call_20199,const_20200,call_20204,])
output2 = relay.Tuple([call_20198,call_20201,const_20200,call_20205,])
func_20215 = relay.Function([], output)
mod['func_20215'] = func_20215
mod = relay.transform.InferType()(mod)
mutated_mod['func_20215'] = func_20215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20215_call = mutated_mod.get_global_var('func_20215')
call_20216 = func_20215_call()
output = call_20216
func_20217 = relay.Function([], output)
mutated_mod['func_20217'] = func_20217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17480_call = mod.get_global_var('func_17480')
func_17482_call = mutated_mod.get_global_var('func_17482')
call_20242 = func_17480_call()
call_20243 = func_17480_call()
output = relay.Tuple([call_20242,])
output2 = relay.Tuple([call_20243,])
func_20255 = relay.Function([], output)
mod['func_20255'] = func_20255
mod = relay.transform.InferType()(mod)
output = func_20255()
func_20256 = relay.Function([], output)
mutated_mod['func_20256'] = func_20256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11780_call = mod.get_global_var('func_11780')
func_11782_call = mutated_mod.get_global_var('func_11782')
call_20257 = relay.TupleGetItem(func_11780_call(), 0)
call_20258 = relay.TupleGetItem(func_11782_call(), 0)
func_13918_call = mod.get_global_var('func_13918')
func_13919_call = mutated_mod.get_global_var('func_13919')
call_20260 = func_13918_call()
call_20261 = func_13918_call()
output = relay.Tuple([call_20257,call_20260,])
output2 = relay.Tuple([call_20258,call_20261,])
func_20263 = relay.Function([], output)
mod['func_20263'] = func_20263
mod = relay.transform.InferType()(mod)
output = func_20263()
func_20264 = relay.Function([], output)
mutated_mod['func_20264'] = func_20264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12287_call = mod.get_global_var('func_12287')
func_12289_call = mutated_mod.get_global_var('func_12289')
call_20271 = relay.TupleGetItem(func_12287_call(), 0)
call_20272 = relay.TupleGetItem(func_12289_call(), 0)
func_16946_call = mod.get_global_var('func_16946')
func_16948_call = mutated_mod.get_global_var('func_16948')
const_20289 = relay.const([7,-4,1,2,-8,2,7,1,10,-7,-5,1,-2,7,3,-8,7,-1,1,2,10,-5,5,6,2,-2,-2,10,7,2,3,-10,1,9,-7,-3,5,3,6,7,-3,-4,5,8,1,-2,1,7,3,6,-6,-6,7,-3,1,8,3,6,7,-8,6,-7,1,-9,-9,-6,-3,6,-4,-10,10,-8,3,-1,-9,-1,10,-10,-9,7,5,2,8,8,10,-8,8,-3,9,1,2,3,-9,3,3,9,5,-5,-1,6,1,-2,-9,1,-9,-8,-6,5,3,7,-9,-5], dtype = "uint8")#candidate|20289|(112,)|const|uint8
call_20288 = relay.TupleGetItem(func_16946_call(relay.reshape(const_20289.astype('uint8'), [1, 14, 8])), 1)
call_20290 = relay.TupleGetItem(func_16948_call(relay.reshape(const_20289.astype('uint8'), [1, 14, 8])), 1)
func_13095_call = mod.get_global_var('func_13095')
func_13096_call = mutated_mod.get_global_var('func_13096')
call_20302 = func_13095_call()
call_20303 = func_13095_call()
output = relay.Tuple([call_20271,call_20288,const_20289,call_20302,])
output2 = relay.Tuple([call_20272,call_20290,const_20289,call_20303,])
func_20305 = relay.Function([], output)
mod['func_20305'] = func_20305
mod = relay.transform.InferType()(mod)
output = func_20305()
func_20306 = relay.Function([], output)
mutated_mod['func_20306'] = func_20306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19136_call = mod.get_global_var('func_19136')
func_19138_call = mutated_mod.get_global_var('func_19138')
call_20369 = func_19136_call()
call_20370 = func_19136_call()
func_10348_call = mod.get_global_var('func_10348')
func_10352_call = mutated_mod.get_global_var('func_10352')
const_20382 = relay.const([[1.265170,0.996694,-1.515393,7.767277,-1.051667,-5.595721,-8.090823,4.448599,-2.728233,-7.522935,2.446367,8.675221,2.788061,-5.090132,-2.457939,5.648486,-5.820466,-9.987065,-1.099675,6.238656,9.450403,-3.145278,4.745995,2.454658,-5.029953,9.513534,6.053866,1.275523,-1.696900,-5.311709,-3.341890,-9.522351,-8.871284,7.250466,-7.426585,-0.977019,-8.412247,9.003798,-2.347985,-0.061081,-4.843741,-6.600285,-2.191573,0.550020,-0.363997,5.145626,0.865690,4.239493,-9.422011,-8.959267,4.442339,-5.788362,-6.020330,-2.691025,-1.441469,2.941487,-1.257944,-9.534573,1.818733,6.324176,5.781852,-6.818025,-8.783905,0.798966,-1.773309,-6.417460,-5.817213,-0.371103,-7.511821,7.285233,6.586407,-5.613096,-0.363541,-3.379574,-2.492090,1.591662,-8.714251,-5.045132,7.696586,9.863486,0.233511,-3.896851,-2.896163,-1.722938,7.679679,-6.682099,-4.203665,-8.804345,9.959068,0.851865,3.933224,-6.912930,-0.701677,-4.552770,-9.706580,-1.914702,9.434433,3.692917,9.237959,0.081485,8.700025,7.279788,-9.339972,-0.204499,-8.534060,0.755065,2.774793,9.199119,-4.007917,4.843011,4.282788,-0.777426,-5.990496,-3.355890,-5.124674,-4.636037,1.762249,7.904910,-3.937855,-2.829483,6.207348,-8.538886,1.706173,1.433057,0.022267,-8.831197,-6.995481,-6.350395,-4.773562,-9.319785,-3.617629,-2.211274,-6.854029,8.115323,5.894334,4.893494,4.178839,2.193115,5.639690,-5.789943,-9.452106,3.977559,5.811137,2.479277,-9.961533,-6.653406,2.598780,2.874402,0.055599,-4.437688,-7.298403,7.851576,1.818216,-2.764267,2.489377,2.272443,9.200348,-2.236343,-8.296808,-2.064889,9.531737,8.325166,4.673075,-4.600828,8.152684,0.515941,-1.671235,6.936658,-8.332460,-5.197841,-2.186022,9.938199,-9.102781,4.257907,5.852639,-8.358664,-7.720152,7.082195,-2.824931,-0.355600,-1.800180,5.105363,3.282436,-7.521936,-7.931050,7.246925,8.878384,-5.801602,7.125070,-5.407341,8.939853,2.290577,8.987631,3.544031,6.211493,3.090669,1.705669,-7.613048,-2.855835,-4.951045,-4.646648,8.450945,-3.256283,7.874606,9.192639,2.098189,-9.849944,1.064265,2.650321,2.808341,-0.640175,5.274422,0.175673,-0.332642,-8.008499,-2.556859,1.812723,-9.917300,4.712126,2.657653,-7.226074,5.531304,8.029731,-1.185610,4.037432,3.453700,-8.121394,-5.597429,7.746499,7.126483,0.953105,-8.193184,-4.335554,3.878080,-9.135836,-0.710696,1.968532,-2.009594,-5.158770,9.451612,-3.090291,-2.061087,0.300687,7.362877,3.509634,9.018334,-5.449912,8.603658,-6.246098,7.906174,5.290032,7.399434,3.868686,-9.170792,-1.037320,-9.417647,-5.554291,-8.551142,1.607177,-4.230368,-1.172308,5.954718,5.550683,3.743108,5.928074,1.343727,7.514112,4.212449,-0.945295,-7.038128,-8.766061,1.816010,9.795882,-9.734908,5.015315,-1.557290,-3.964085,4.060034,-3.809206,-5.931309,6.065195,8.038577,-6.851774,2.621860,-9.942561,-0.171710,-3.249211,5.402303,3.658332,-5.807727,7.711668,-2.696271,1.107039,1.040965,1.392166,2.736457,7.209754,9.191707,-5.443154,-8.062697,-8.930232,0.926219,3.206259,0.144917,-3.180127,7.136698,-2.625497,-7.130062,0.729231,3.905112,3.536045,6.651877,3.784439,-8.443282,-0.784031,-2.902762,2.642813,5.631359,1.763885,0.679638,6.706978,1.267171,2.738745,6.327753,2.953795,3.440902,4.692656,-6.205200,2.364011,-3.900096,7.569867,-5.042415,-4.856056,8.789820,-1.247904,-9.682746,-6.866034,5.582961,5.858367,-4.407698,-6.164060,2.135106,6.844989,-5.041842,-3.096057,-0.374196,-9.851840,8.015735,-8.676747,-8.619414,0.751570,-9.880670,-5.731058,6.989791,-6.173938,-2.140966,2.339949,6.080900,5.941108,0.782041,-4.806034,-5.621789,8.218933,-4.919881,-5.316925,-7.707214,1.814252,2.726503,4.365119,9.496462,9.356896,-8.782570,9.543120,5.911932,2.651561,-5.885132,-3.543243,-7.484669,-0.302977,3.737923,1.889546,7.608539,1.871688,-8.030143,4.161965,-5.222509,-5.114197,-6.513854,-8.062236,-1.890562,-2.627281,-3.744850,3.069003,-2.271958,9.070741,3.261813,-2.941700,9.704781,3.221363,-2.634963,7.929325,0.014795,6.791839,4.868098,6.134217,1.343411,-6.487359,-4.645592,4.018160,-6.445040,8.166992,5.400522,-7.534798,5.592198,5.222698,-0.221075,-9.900668,-9.248382,5.448055,-5.902804,1.757882,9.544853,6.243870,-3.423935,-4.304106,6.601517,-3.526758,4.797771,3.092378,-1.455187,-5.456801,4.102491,2.946223,-7.003956,8.982295,1.939170,3.447011,-5.463515,2.326135,9.733686,7.947648,4.635067,7.568292,-7.998564,1.241884,5.348736,-0.793566,-3.511063,-6.787261,-6.449047,0.905026,4.539049,-3.055723,2.865974,-8.047868,-9.621186,9.038708,8.643003,-9.417092,5.564258,-4.430534,-8.238499,2.187037,-6.818715,0.587623,0.913689,2.077932,3.003692,1.220807,8.687982,4.922516,2.886938,1.325044,-3.016196,9.266635,6.840023,-5.049866,-7.162911,-6.366047,-2.823080,5.014232,6.630541,-5.770277,4.327191,3.503042,1.978378,-8.715232,-6.492329,7.838891,1.856305,-8.599625,-0.319576,-7.102173,0.094790,-1.229947,0.078177,9.661219,-7.699192,4.420289,5.621513,-3.219972,-3.200800,-5.899429,-6.164821,7.875293,-4.648106,-6.459493,-7.284889,3.678143,9.915502,8.433884,1.637315,7.251007,-3.300656,7.498848,-1.303311,-0.391091,-0.118304,6.752600,-1.388144,6.056377,-5.720560,-6.552766,-0.467332,-4.834269,4.905230,-0.187077,0.473517,-4.374350,6.870481,2.847603,5.351550,-3.028239,-1.174063,-0.477075,-0.271612,5.331082,7.579103,6.666553,0.213038,4.837613,-9.392245,-1.132797,-2.397588,8.923037,-1.912685,9.654869,4.495360,-2.710552,6.603797,-1.609135,-9.215061,-5.301969,5.108406,9.104532,-7.298353,6.065501,4.350775,-4.931756,-2.976107,9.634867,-6.516848,-4.314450,-3.362471,-8.953966,4.373198,3.843129,-2.555490,9.769853,8.572627,4.312205,-2.345025,-0.882199,-5.705672,1.091587,9.914963,9.908783,1.536007,9.008976,-0.838911,2.898978,-1.428999,3.133553,-2.627221,6.476959]], dtype = "float32")#candidate|20382|(1, 585)|const|float32
call_20381 = relay.TupleGetItem(func_10348_call(relay.reshape(const_20382.astype('float32'), [13, 9, 5]), relay.reshape(const_20382.astype('float32'), [13, 9, 5]), relay.reshape(const_20382.astype('float32'), [13, 9, 5]), ), 0)
call_20383 = relay.TupleGetItem(func_10352_call(relay.reshape(const_20382.astype('float32'), [13, 9, 5]), relay.reshape(const_20382.astype('float32'), [13, 9, 5]), relay.reshape(const_20382.astype('float32'), [13, 9, 5]), ), 0)
output = relay.Tuple([call_20369,call_20381,const_20382,])
output2 = relay.Tuple([call_20370,call_20383,const_20382,])
func_20389 = relay.Function([], output)
mod['func_20389'] = func_20389
mod = relay.transform.InferType()(mod)
output = func_20389()
func_20390 = relay.Function([], output)
mutated_mod['func_20390'] = func_20390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18522_call = mod.get_global_var('func_18522')
func_18524_call = mutated_mod.get_global_var('func_18524')
call_20532 = relay.TupleGetItem(func_18522_call(), 0)
call_20533 = relay.TupleGetItem(func_18524_call(), 0)
func_19228_call = mod.get_global_var('func_19228')
func_19230_call = mutated_mod.get_global_var('func_19230')
call_20553 = relay.TupleGetItem(func_19228_call(), 0)
call_20554 = relay.TupleGetItem(func_19230_call(), 0)
output = relay.Tuple([call_20532,call_20553,])
output2 = relay.Tuple([call_20533,call_20554,])
func_20571 = relay.Function([], output)
mod['func_20571'] = func_20571
mod = relay.transform.InferType()(mod)
mutated_mod['func_20571'] = func_20571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20571_call = mutated_mod.get_global_var('func_20571')
call_20572 = func_20571_call()
output = call_20572
func_20573 = relay.Function([], output)
mutated_mod['func_20573'] = func_20573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18716_call = mod.get_global_var('func_18716')
func_18717_call = mutated_mod.get_global_var('func_18717')
call_20594 = func_18716_call()
call_20595 = func_18716_call()
output = call_20594
output2 = call_20595
func_20601 = relay.Function([], output)
mod['func_20601'] = func_20601
mod = relay.transform.InferType()(mod)
output = func_20601()
func_20602 = relay.Function([], output)
mutated_mod['func_20602'] = func_20602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17771_call = mod.get_global_var('func_17771')
func_17773_call = mutated_mod.get_global_var('func_17773')
call_20611 = relay.TupleGetItem(func_17771_call(), 0)
call_20612 = relay.TupleGetItem(func_17773_call(), 0)
func_19370_call = mod.get_global_var('func_19370')
func_19373_call = mutated_mod.get_global_var('func_19373')
var_20616 = relay.var("var_20616", dtype = "float32", shape = (26400,))#candidate|20616|(26400,)|var|float32
call_20615 = relay.TupleGetItem(func_19370_call(relay.reshape(var_20616.astype('float32'), [11, 2400])), 2)
call_20617 = relay.TupleGetItem(func_19373_call(relay.reshape(var_20616.astype('float32'), [11, 2400])), 2)
func_708_call = mod.get_global_var('func_708')
func_712_call = mutated_mod.get_global_var('func_712')
const_20628 = relay.const([[-10,1,2,-8],[-9,-5,-3,5],[-1,-1,4,-3],[6,4,4,7],[2,-5,9,7],[-2,-4,-5,-10],[-5,-1,4,4],[5,-5,-10,5],[2,8,5,-7],[8,-5,-2,9],[7,-4,3,-10],[8,9,8,1],[6,-1,-5,-10],[-4,3,-10,-1],[2,8,5,-8]], dtype = "uint64")#candidate|20628|(15, 4)|const|uint64
const_20629 = relay.const([[4],[3],[8],[7],[-7],[-10],[-1],[-2],[5],[-8],[-9],[1],[-3],[-4],[6],[-10],[-3],[-8],[-4],[-3],[-2],[-1],[-9],[9],[9],[7],[4],[-3],[-10],[-4],[8],[9],[-6],[4],[-1],[-2],[-2],[-6],[-5],[5],[6],[-9],[1],[7],[-10],[-8],[-2],[10],[1],[9],[-3],[-5],[-3],[-5],[9],[10],[3],[-4],[-3],[4],[2],[2],[8]], dtype = "uint32")#candidate|20629|(63, 1)|const|uint32
call_20627 = relay.TupleGetItem(func_708_call(relay.reshape(const_20628.astype('uint64'), [12, 5, 1]), relay.reshape(const_20629.astype('uint32'), [7, 9]), ), 2)
call_20630 = relay.TupleGetItem(func_712_call(relay.reshape(const_20628.astype('uint64'), [12, 5, 1]), relay.reshape(const_20629.astype('uint32'), [7, 9]), ), 2)
output = relay.Tuple([call_20611,call_20615,var_20616,call_20627,const_20628,const_20629,])
output2 = relay.Tuple([call_20612,call_20617,var_20616,call_20630,const_20628,const_20629,])
func_20633 = relay.Function([var_20616,], output)
mod['func_20633'] = func_20633
mod = relay.transform.InferType()(mod)
mutated_mod['func_20633'] = func_20633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20634 = relay.var("var_20634", dtype = "float32", shape = (26400,))#candidate|20634|(26400,)|var|float32
func_20633_call = mutated_mod.get_global_var('func_20633')
call_20635 = func_20633_call(var_20634)
output = call_20635
func_20636 = relay.Function([var_20634], output)
mutated_mod['func_20636'] = func_20636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11088_call = mod.get_global_var('func_11088')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_20691 = func_11088_call()
call_20692 = func_11088_call()
func_10099_call = mod.get_global_var('func_10099')
func_10100_call = mutated_mod.get_global_var('func_10100')
call_20705 = func_10099_call()
call_20706 = func_10099_call()
func_14520_call = mod.get_global_var('func_14520')
func_14523_call = mutated_mod.get_global_var('func_14523')
const_20715 = relay.const([0.486788,3.335799,8.308994,9.483051,9.234236,9.643034,5.037045,9.227708,-0.254239,-4.198406,5.479193,-2.566363,-3.815455,8.761394,6.292162,-1.791382,-9.712320,5.267896,4.762384,6.047974,-1.687147,4.186827,6.478092,5.638314,-1.240045,2.868613,6.547773,0.702764,-3.354488,-9.982924,-6.258473,-7.873275,-3.067119,-9.824646,-7.051994,-0.336241,-4.821558,2.573131,-2.234474,3.637544,-0.215634,-7.612271,-3.770837,-7.381460,6.330131,5.737852,5.163397,-4.991669,1.656468,9.972543,-3.732563,-6.915607,8.269206,-4.161082,-4.747526,8.706590,-5.013633,0.272062,4.327897,2.871637,-8.964243,-5.059957,-6.454981,2.208763,2.508808,-3.962594,-8.961821,-7.415864,-3.850226,-5.949710,-1.300392,6.247045,5.584441,7.926550,-5.948509,3.219073,2.051510,-7.486826,-6.802944,0.139813,-6.407247,5.349235,-6.946356,6.642211,-0.135402,-8.827508,5.918255,6.531405,-9.898549,1.615280,8.689864,5.848361,-8.565541,8.202205,7.443070,-7.199099,-2.772463,-6.516456,4.128697,5.759649,0.162492,-0.239058,7.965066,-6.621685,-4.627248,2.351464,-5.136347,9.077146,-0.239463,-8.244946,9.581879,-5.000670,-9.254601,6.514187,-7.752387,-1.682812,-8.485540,-8.520931,-9.745015,5.404150,-8.817608,7.984675,6.291298,2.747917,8.747083,0.606895,-5.219790,-4.981551,-8.319843,-5.057557,-2.800425,3.020900,0.009577,-8.199862,-7.633458,-1.341293,-8.849672,1.028141,-9.614294,-0.245042,-9.970516,5.935844,2.988470,-6.299624,7.673490,-2.196468,8.884089,-1.774297,1.210092,-9.412870,-2.801944,-8.571866,-7.512841,-8.313841,-7.920116,-6.996267,-3.807929,9.463482,9.661306,4.661759,-6.737377,-2.086357,5.328326,-8.220989,-8.152584,-7.746762,6.586283,9.660940,1.053906,5.856974,-3.778521,-4.895930,2.535319,-7.142876,8.916825,8.197518,3.433832,1.511120,-8.104444,7.588353,6.754452,2.364563,-5.560251,-5.471952,-4.348516,2.654554,-8.110780,3.909594,6.898944,-9.366862,6.607946,-3.921055,-4.286975,-1.949477,7.844923,0.840262,8.572182,-9.842141,6.132033,6.637152,-7.773755,4.871774,9.347965,-3.257340,-7.169277,9.341912,-0.313286,0.387580,-0.026625,4.966079,3.740801,-4.517410,7.406650,1.853919,3.235610,-2.968282,9.147563,-2.256162,-3.400652,-4.762272,-2.992324,-2.860820,6.259065,9.356572,3.505073,-8.718586,1.163109,-0.085786,1.399410,0.074951,-6.591984,-3.474171,0.999236,-4.333714,7.845708,9.062430,1.154375,-0.376649,1.411344,-0.395305,-9.083684,3.304532,9.291108,-2.387039,7.857505,4.281956,7.181569,-7.279047,6.605443,-8.562952,2.410636,-6.734326,2.501431,0.735831,-4.379703,-5.015449,-1.788566,-8.962339,3.627468,-3.377952,-9.918731,-4.249499,4.087954,8.250095,-9.341785,7.940463,7.574719,-8.074957,-5.786274,6.803541,4.824328,7.378345,3.574342,8.957439,-2.364203,-1.296429,7.609913,-1.747628,2.756307,1.397655,9.968234,9.530589,-6.503378,-9.515273,3.491285,9.919646,5.347587,1.794413,-9.483867,0.741876,-2.179173,-3.750291,-9.340383,4.048716,-9.827055,2.244943,7.239316,-3.123345,-6.525903,8.837420,-7.844020,-2.459935,0.241137,-8.625854,-8.200501,6.456802,3.286827,5.969436,-7.368623,0.369372,0.797974,7.141433,5.101277,8.142288,-4.435381,-9.531206,6.010405,-4.534751,-2.827750,1.347868,-7.347290,5.658667,-4.074331,9.429051,6.733578,6.977706,-2.312198,-7.506247,-2.483548,5.122712,-0.379832,1.306773,9.368245,-3.077081,-6.110013,-1.139162,-7.721365,8.470659,-3.365497,-4.009527,2.646540,5.704220,-1.893558,-4.276753,5.739303,0.264632,9.033921,5.158519,-4.930173,-5.911925,2.573530,5.857457,-6.413827,-1.439769,4.145558,8.503454,-0.422905,-9.307144,-1.965164,2.521623,3.566530,8.143170,0.997257,4.047038,-6.836527,2.770505,-4.915933,-7.691634,4.612543,-2.360684,0.062299,1.682793,-3.246468,-2.951684,-8.099872,-9.350564,-6.374056,-1.759930,-0.976742,2.139552,9.126552,2.534569,4.281934,5.758971,-4.211540,0.827968,9.425683,-7.715377,6.239823,-9.128697,-1.698430,2.652367,-8.283950,3.641537,1.198097,7.069938,5.845738,-7.703203,-9.792515,9.878686,8.331222,-9.135051,6.712319,-2.000888,9.147603,6.970023,5.149576,-6.537550,-8.884097,6.326833,-4.532675,8.164359,3.165062,-5.219842,5.055985,-3.984253,9.670911,0.924160,2.476287,4.467561,-9.587277,8.354334,0.905969,5.602599,9.043592,7.652006,9.860783,9.780656,-6.028822,5.341045,0.697712,5.014810,-5.749395,0.950221,-4.409704,1.507522,3.965751,2.908731,-7.205247,6.553578,4.726424,-1.774470,8.873615,4.165051,5.762952,0.574510,-7.595623,2.531103,0.402949,0.887335,0.431477,-3.709442,6.127357,3.150903,-4.277565,9.651319,3.756420,-3.644100,9.263666,9.570175,-0.106140,7.924123,7.873460,-8.915958,1.675111,-1.185489,-4.476409,-4.626648,-9.501393,3.259013,-7.746179,-6.101289,-1.740544,-9.499687,-5.767317,8.284791,-2.475612,-7.672207,5.716489,-3.342406,-3.254328,-7.494540,9.479710,-8.687230,-0.541470,-7.212469,-0.522768,7.651746,6.606202,-7.415524,8.589866,2.450482,-7.983437,2.651038,-8.995082,-7.993339,-0.799547,6.959132,4.406238,-1.640380,3.195178,-7.070047,3.579767,0.649133,2.729665,7.910913,8.395593,-7.557737,-3.753687,2.628089,0.942616,5.573886,-7.685528,2.714599,-5.988650,-4.190167,-9.781872,8.575383,-3.605153,5.496828,-7.519017,-3.818627,3.583080,7.930625,-7.805574,-9.086087,-1.315370,4.165538,-0.462737,3.779090,-6.874295,-3.725156,-8.037243,2.336858,-2.679588,5.399635,9.498366,-0.161805,-5.153092,-1.526925,1.871765,9.509963,-8.374523,-9.321315,7.723727,8.191543,8.253849,2.301980,8.327796,-0.379733,6.805424,-1.745767,4.857611,4.171544,-3.243271,-7.315363,-2.996925,3.665184,2.253509,0.535702,9.399199,-3.762529,-9.131456,3.268084,-4.864717,-5.274048,4.844839,-3.629637,2.263435,-8.246933,0.862276,9.495286,-0.832850,-9.720949,9.249333,2.783453,-4.632531,9.474178,7.908848,-7.784131,8.701394,9.383411,5.007292,2.027640,1.268677], dtype = "float32")#candidate|20715|(585,)|const|float32
call_20714 = func_14520_call(relay.reshape(const_20715.astype('float32'), [65, 9]))
call_20716 = func_14520_call(relay.reshape(const_20715.astype('float32'), [65, 9]))
func_18813_call = mod.get_global_var('func_18813')
func_18814_call = mutated_mod.get_global_var('func_18814')
call_20725 = relay.TupleGetItem(func_18813_call(), 1)
call_20726 = relay.TupleGetItem(func_18814_call(), 1)
func_11215_call = mod.get_global_var('func_11215')
func_11219_call = mutated_mod.get_global_var('func_11219')
const_20730 = relay.const([[7,-4,10,6,1,-5,7,7,-6,-5,2,-1,-9,-4,3,8,7,-6,1,-1,5,5,9,8,-6,6,-2,-1,-10,-5,-10,-4,6,4,-10,-2,-2,9,-10,7,-1,-3,10,5,10,2,5,-7,-5,-10,7,-2,-8,2,-7,3,-2,2,-4,-3,-6,-4,-2,-4,3,2,6,3,-4,-4,-4,10,5,7,6,4,6,5,-1,4,4,6,-9,-6,3,-5,-6,2,-4,3,-8,4,-4,-1,9,-9,-1,-5,-5,5,-10,7,-5,9,8,1,-8,-2,-5,7],[8,9,2,-10,-4,7,5,-3,-2,2,-6,-8,10,-7,4,-9,10,2,1,-1,8,2,-1,-8,7,7,-4,8,-6,9,10,2,5,6,-7,2,2,-1,-6,9,8,9,-10,8,-5,-6,4,-7,-4,-6,7,-8,-9,-5,9,-2,-10,1,-9,6,5,-7,9,-9,-8,-4,10,-7,3,7,7,-1,10,7,-10,-1,6,-5,5,-10,6,9,7,8,-7,-4,-4,-1,6,4,-2,2,-5,5,-10,3,10,-3,-6,-7,-5,7,-5,-6,6,-8,4,-8,-6,7],[9,-1,9,-4,-4,-10,-3,10,5,10,5,2,7,-6,-5,8,-2,3,-2,8,9,8,-5,1,-4,1,-6,-9,-5,5,-8,3,9,-5,2,-8,3,4,-4,-6,-3,-10,-2,-1,1,-4,-8,-3,5,-9,-1,-10,5,-2,1,1,-7,-5,9,-5,-4,1,7,1,2,-1,-1,9,6,-6,1,1,10,6,-3,-10,-1,-9,7,-10,-1,3,-1,7,4,-4,-3,-3,-2,10,2,-2,-3,1,10,8,-4,1,-3,-5,-4,-2,-8,9,5,-5,9,2,-8,-1],[-6,-10,-10,-8,-1,-2,3,-9,-10,-1,8,-4,3,1,8,-2,9,-5,-2,3,-5,6,8,1,6,5,-9,-2,-4,6,3,6,-9,-4,-5,4,-2,10,-8,10,-6,-7,-5,-9,-2,-10,-4,-8,9,-4,8,4,6,2,6,7,10,-7,3,-3,-3,-9,-9,-10,10,1,-9,10,9,-1,-7,-7,4,-9,7,3,4,7,-10,10,-10,-8,5,6,9,9,8,10,-7,1,2,6,-6,7,-9,-4,7,-7,7,6,-3,-1,-10,-4,-9,-3,-9,-6,3,8],[10,10,-3,2,2,-7,5,-7,8,-4,-8,-9,9,1,7,-3,-3,-6,3,10,10,-2,5,1,-3,-2,5,8,-7,3,10,2,-10,2,10,9,-9,-4,10,-10,2,6,3,9,-4,-3,10,-10,8,6,-3,-6,7,7,-7,2,8,7,3,3,-10,-6,4,5,-7,9,-7,2,-7,3,7,3,5,-9,6,10,8,8,-9,5,-3,5,9,6,-8,2,-6,1,3,-2,3,6,-9,5,-5,-3,5,8,7,4,3,-9,8,-10,3,1,5,9,-2,-1]], dtype = "int8")#candidate|20730|(5, 110)|const|int8
call_20729 = relay.TupleGetItem(func_11215_call(relay.reshape(call_20725.astype('float32'), [15, 9, 9]), relay.reshape(const_20730.astype('int8'), [55, 10]), ), 1)
call_20731 = relay.TupleGetItem(func_11219_call(relay.reshape(call_20725.astype('float32'), [15, 9, 9]), relay.reshape(const_20730.astype('int8'), [55, 10]), ), 1)
output = relay.Tuple([call_20691,call_20705,call_20714,const_20715,call_20725,call_20729,const_20730,])
output2 = relay.Tuple([call_20692,call_20706,call_20716,const_20715,call_20726,call_20731,const_20730,])
func_20732 = relay.Function([], output)
mod['func_20732'] = func_20732
mod = relay.transform.InferType()(mod)
mutated_mod['func_20732'] = func_20732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20732_call = mutated_mod.get_global_var('func_20732')
call_20733 = func_20732_call()
output = call_20733
func_20734 = relay.Function([], output)
mutated_mod['func_20734'] = func_20734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18087_call = mod.get_global_var('func_18087')
func_18089_call = mutated_mod.get_global_var('func_18089')
call_20744 = func_18087_call()
call_20745 = func_18087_call()
func_18087_call = mod.get_global_var('func_18087')
func_18089_call = mutated_mod.get_global_var('func_18089')
call_20754 = func_18087_call()
call_20755 = func_18087_call()
output = relay.Tuple([call_20744,call_20754,])
output2 = relay.Tuple([call_20745,call_20755,])
func_20773 = relay.Function([], output)
mod['func_20773'] = func_20773
mod = relay.transform.InferType()(mod)
mutated_mod['func_20773'] = func_20773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20773_call = mutated_mod.get_global_var('func_20773')
call_20774 = func_20773_call()
output = call_20774
func_20775 = relay.Function([], output)
mutated_mod['func_20775'] = func_20775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13771_call = mod.get_global_var('func_13771')
func_13773_call = mutated_mod.get_global_var('func_13773')
call_20871 = relay.TupleGetItem(func_13771_call(), 2)
call_20872 = relay.TupleGetItem(func_13773_call(), 2)
func_20046_call = mod.get_global_var('func_20046')
func_20049_call = mutated_mod.get_global_var('func_20049')
var_20877 = relay.var("var_20877", dtype = "bool", shape = (495,))#candidate|20877|(495,)|var|bool
const_20878 = relay.const([-6.412934,3.858950,0.082052,0.309443,-8.875828,2.151371,0.397738,-9.643067,4.294885,-3.540064,9.276541,6.127042,-2.532750,-1.498549,-2.271349,5.683664,-4.732482,4.961293,-2.949317,4.655602,4.925034,5.696771,-9.074076,-7.539602,-0.855910,4.205510,-7.356515,7.158106,8.276297,-9.222248,-3.781767,-6.632214,-2.384173,-5.742997,-9.930276,9.746197,-4.629780,-8.203636,-7.947270,-9.623772,-5.806276,-7.822888,-1.601248,7.005545,-8.829045,2.834512,9.190610,5.827709,-7.013296,7.017834,0.322251,-1.179349,5.813306,-5.294335,-1.233465,-2.886890,-7.960474,4.622297,7.705130,6.314942,-6.991248,-4.830191,-9.216747,2.593820,4.840224,-8.412117,9.492242,-6.260795,9.036956,-0.518682,-4.747947,-4.657888,5.224801,9.732970,7.654144,-8.419768,-3.099305,0.320133,-4.607203,4.336253,4.753608,-5.599327,-8.646890,-9.378006,-1.522216,6.557852,2.982775,8.972512,3.628803,3.802476,1.848785,-6.749976,-6.252381,6.284917,-8.656925,-9.782321,-6.372334,-5.231923,-9.409572,-9.351245,6.020711,0.872098,-3.885292,-9.260208,7.896271,-2.575809,3.577274,-1.093047,-4.263357,5.838519,-7.637534,1.914082,-8.542670,-5.675143,-4.076443,1.226737,-6.444712,-2.393631,-8.324823,3.401492,4.291628,-6.343216,-8.915961,-7.252668,-3.086062,-2.920472,-0.356412,0.769397,3.967265,8.237028,2.194624,-3.333714,5.978632,-4.910635,7.166345,2.904120,0.831244,7.793080,8.056151,-5.177298,8.967817,-2.858918,-9.908911,5.291596,7.275223,0.216445,7.383972,5.195565,4.129263,-7.925883,2.108807,2.746403,-3.144914,-5.728108,-6.891539,9.897918,2.580118,4.315549,-9.876787,-4.538985,3.044561,-0.322915,8.437509,3.203831,3.513245,7.012168,-9.646269,3.676148,2.366128,-2.579971,-4.733735,-2.155572,3.753504,-9.837191,-0.476400,-1.127625,-3.235086,-9.702509,-4.502862,-2.770592,-6.263025,-7.030351,-0.587527,9.193181,4.007452,-5.940329,2.972274,-8.355387,-4.162219,-4.726463,8.469896,0.227180,6.344531,7.700513,2.594877,7.111575,8.586726,-2.670735,0.473855,5.477527,4.851037,0.526321,-4.697464,-6.621531,-9.585905,8.732705,2.015618,2.205916,8.182741,-4.908747,5.140337,-3.369357,7.266785,-7.049466,-4.546967,3.288476,7.546561,-2.919029,-5.756504,1.719191,-6.362337,-3.351215,2.868320,-1.371112,-8.529829,7.429153,8.298007,-2.285957,3.783819,5.379520,8.998728,3.215150,8.860255,-2.228594,-0.808682,-3.297421,2.559833,-2.087784,7.127738,4.759412,5.100934,5.642156,-4.938288,6.346716,-6.799771,1.407976,-5.875573,7.806025,-8.518755,9.549679], dtype = "float64")#candidate|20878|(250,)|const|float64
call_20876 = relay.TupleGetItem(func_20046_call(relay.reshape(var_20877.astype('bool'), [495,]), relay.reshape(const_20878.astype('float64'), [25, 10]), ), 3)
call_20879 = relay.TupleGetItem(func_20049_call(relay.reshape(var_20877.astype('bool'), [495,]), relay.reshape(const_20878.astype('float64'), [25, 10]), ), 3)
func_6067_call = mod.get_global_var('func_6067')
func_6073_call = mutated_mod.get_global_var('func_6073')
var_20883 = relay.var("var_20883", dtype = "uint16", shape = (1024, 1))#candidate|20883|(1024, 1)|var|uint16
const_20884 = relay.const([6.877087,3.074322,9.794149,7.790363,7.893225,-8.307321,-8.573966,2.617037,-6.832541,2.053018,4.072013,-3.186891,5.996322,0.479307,-2.140513,5.957487,4.488807,-7.996052,0.409785,0.412683,-8.066869,-7.290603,-7.494197,9.168761,1.028449,8.171283,-6.016623,8.364508,0.535141,-4.708647,-3.006233,8.862409,1.759570,-0.637672,-4.419232,9.061262,-8.052820,0.376545,0.418344,2.256294,9.004457,8.346923,-2.329544,3.969887,6.638246,-3.225691,-2.865381,1.436209,3.560923,-9.646839,-4.535347,3.060568,7.908360,0.595014,2.433774,0.880396,4.977067,-6.649743,0.720117,5.795481,4.570082,-2.866096,-3.277808,9.682333,-5.216484,1.878843,-1.616634,3.276779,2.238865,-9.017762,1.357629,9.871029,2.494354,4.657937,8.509130,8.080435,-8.419718,-1.755919,-0.189832,-3.208516,5.788222,6.034254,-6.289714,8.659531,2.764680,-8.722543,9.734797,8.827085,7.502512,-0.070012,7.461273,-0.872221,5.253047,-2.037674,-2.805833,-2.748975,-9.665319,3.333501,-1.619710,-7.292068,9.305756,3.250940,-4.348702,7.765788,9.954602,9.395928,3.507845,-6.859529,-2.276862,-4.293783,3.540606,5.993904,-0.657431,8.292587,1.455622,-8.779682,-2.637116,-4.141243,-5.490962,8.910827,7.072907,0.915451,-4.964416,1.222841,-9.384480,1.522624,8.847820,-2.768779,-8.891683,-9.629111,0.275900,-2.540617,-1.701819,4.490839,-9.517743,-0.450693,5.574887,-1.475890,5.993593,-0.401012,-5.385047,-9.540358,-9.611167,4.680263,-8.001123,8.531202,6.764583,4.877406,-1.815290,-2.789829,8.367281,-5.311541,-8.491480,-9.035728,-6.890655,-2.214425,6.480137,-8.755407,2.515220,-8.350321,-2.891373,9.291589,8.413900,5.098789,6.888535,-5.754149,8.977584,6.414578,0.623057,3.218626,3.414927,-8.868730,-1.910926,-1.436997,0.722945,5.863186,-6.221595,3.296815,-9.090465,7.116671,-9.166871,-2.093962,-0.831037,-4.536792,-4.339597,-7.291549,9.373369,-0.909176,9.746081,8.713184,8.333758,-3.161681,1.432781,6.693392,0.423865,-6.640737,-6.673201,2.044543,-1.516202,-9.582970,6.686701,-5.669804,-1.339594,9.150949,-1.088053,-7.331316,5.374787,6.076405,-3.192753,-9.827097,-3.728596,8.896385,-4.045280,3.667624,-9.838299,7.752790,-9.289082,-6.308472,-4.764824,7.697083,-9.918776,-7.483973,-7.009150,7.793960,-4.463164,-7.748397,-0.329333,4.863204,-8.517057,1.502907,-3.966238,2.279271,7.604906,5.786804,7.713330,-5.719098,-4.783628,4.621662,-4.005159,5.055850,6.414411,8.104365,-5.394454,-0.309859,-1.763916,4.744166,-5.378855,8.264985,7.691594,6.979529,0.283910,-9.012805,-7.654596,8.394076,-9.745996,5.052700,-9.001979,3.444852,1.357536,-2.117455,-8.121704,-9.591963,-2.965974,-6.697542,3.053848,-9.211706,9.763383,-6.438267,-0.011399,-1.527183,7.757679,-9.310070,4.357336,-6.071703,9.693087,-9.098817,-7.876208,-4.193469,-4.015510,-8.248503,-5.684344,6.138074,-2.892286,7.028598,9.998058,6.985769,6.527992,-2.313472,-8.383267,4.080179,6.859228,4.477187,7.230215,-5.569343,-0.561162,9.520203,2.165734,-1.880095,-3.148689,4.457429,6.404388,-5.755645,-5.377934,6.725236,9.720915,9.712761,-6.446624,8.195292,-8.854223,-4.066323,-5.120223,-7.648450,-1.358251,0.373477,-6.720757,-5.714749,-1.720348,0.560323,1.608052,7.467433,6.578804,-0.114303,9.810418,6.309604,8.480148,-9.776949,0.283593,-1.984744,3.641233,6.096051,-2.596582,4.256882,-9.421764,5.926585,-5.984951,5.704261,9.162374,4.997275,1.960865,8.225150,-0.543835,-1.588630,-4.053552,1.274855,3.085712,7.221535,-9.918630,-6.282553,6.426421,2.037646,-5.459427,-9.542606,-8.015206,-2.786027,-1.189573,-9.912995,7.494718,6.697860,9.850669,5.987211,2.826352,-1.853586,6.244475,-5.622754,4.324977,-3.909733,-5.401644,1.514043,8.631047,-1.996873,2.245560,-7.088100,-8.856555,-2.415497,9.566944,-4.568975,6.895284,-8.889850,8.480576,2.222112,-8.572489,-4.924433,-8.904675,3.394788,1.246961,-2.840312,6.505476,8.073635,-2.372187,2.202811,0.354486,-5.807695,5.049159,2.006485,3.318342,6.224472,5.334359,9.151658,9.596450,1.811658,-4.854048,-1.144027,-3.472618,0.574580,6.936373,-9.603973,-7.917107,6.346267,-6.362552,-7.979401,-9.164937,8.405198,3.694206,0.411750,-8.542723,3.103421,-9.501173,-9.887483,1.042175,3.508597,-0.841638,7.071479,-5.802002,-2.391325,-0.744652,2.227428,-4.508842,-5.919974,1.187394,9.615523,-2.967676,-4.869835,-0.067260,2.447521,2.170518,-2.744245,4.253868,-4.468721,5.952245,-1.573697,-1.705873,-8.081398,-2.219607,-9.925234,-3.301805,2.418113,0.294664,-9.145550,-2.716149,7.249418,-1.480887,-3.432211,-4.850012,-4.567380,9.991914,5.979691,-3.558023,8.425850,-8.398706,-8.499346,1.937576,3.058306,6.309844,-1.829424,8.644445,6.807991,7.699252,4.646228,4.498196,3.769783,-9.192850,-4.518762,-7.569816,-0.246152,8.315523,-2.525098,-4.953300,4.183160,6.726003,-2.535752,-4.199111,-5.547791,3.285392,4.544019,5.846657,2.243784,7.854530,-3.855802,6.703290,-6.289818,5.110662,6.187383,-0.533953,-4.237792,-4.277325,-0.597693,-7.621363,2.831697,1.671262,-7.326800,1.233449,-2.886958,5.983759,8.428840,3.943743,-7.394927,-0.536690,6.523820,-8.435260,-0.633449,-9.138700,5.966488,0.773253,-8.129518,2.569279,-8.796044,-0.281734,7.208993,9.523650,8.478552,-4.549691,-9.424344,5.846033,4.512792,3.693941,7.174835,6.125701,-5.225589,1.925859,0.838196,-5.903355,5.849425,-9.813314,-0.487930,8.142078,8.562599,2.233785,-8.442070,1.462503,7.747343,8.921225,-4.288001,8.760716,-1.699976,8.997109,-8.787708,2.689336,-8.431331,-7.027899,4.429760,-2.795518,-4.192591,-9.988748,6.401390,-7.549007,-0.084289,1.349400,-7.321582,-6.487433,0.400449,-8.096506,7.250562,1.845766,-6.152822,-0.198975,-1.701119,-9.207934,2.265993,1.217096,-4.597288,8.620124,-9.473343,3.712914,8.571039,5.847531,9.394706,-4.708011,1.704378,-1.297812,-6.755114,7.838683,-4.308721,3.235505,6.823318,-1.353940,-1.362637,-8.834140,-5.605204,-7.283148,3.004588,-9.466263,5.518467,9.651138,-0.378082,-2.169429,4.387217,6.916625,7.839547,4.677271,-8.515241,-8.656346,8.118351,6.281539,-1.102609,7.894456,9.453326,-1.183635,0.079393,5.888876,-5.228490,-3.139520,5.317244,4.000206,-6.613905,8.515492,-2.988812,6.173232,6.665262,1.335794,-2.994045,6.967416,-7.496005,8.620767,-3.057478,6.296431,-0.239892,-7.213383,-5.157662,4.777747,-6.932252], dtype = "float32")#candidate|20884|(630,)|const|float32
call_20882 = relay.TupleGetItem(func_6067_call(relay.reshape(var_20883.astype('uint16'), [16, 4, 16]), relay.reshape(var_20883.astype('uint16'), [16, 4, 16]), relay.reshape(const_20884.astype('float32'), [70, 9]), relay.reshape(var_20883.astype('bool'), [16, 4, 16]), ), 0)
call_20885 = relay.TupleGetItem(func_6073_call(relay.reshape(var_20883.astype('uint16'), [16, 4, 16]), relay.reshape(var_20883.astype('uint16'), [16, 4, 16]), relay.reshape(const_20884.astype('float32'), [70, 9]), relay.reshape(var_20883.astype('bool'), [16, 4, 16]), ), 0)
output = relay.Tuple([call_20871,call_20876,var_20877,const_20878,call_20882,var_20883,const_20884,])
output2 = relay.Tuple([call_20872,call_20879,var_20877,const_20878,call_20885,var_20883,const_20884,])
func_20891 = relay.Function([var_20877,var_20883,], output)
mod['func_20891'] = func_20891
mod = relay.transform.InferType()(mod)
var_20892 = relay.var("var_20892", dtype = "bool", shape = (495,))#candidate|20892|(495,)|var|bool
var_20893 = relay.var("var_20893", dtype = "uint16", shape = (1024, 1))#candidate|20893|(1024, 1)|var|uint16
output = func_20891(var_20892,var_20893,)
func_20894 = relay.Function([var_20892,var_20893,], output)
mutated_mod['func_20894'] = func_20894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10933_call = mod.get_global_var('func_10933')
func_10935_call = mutated_mod.get_global_var('func_10935')
call_20952 = relay.TupleGetItem(func_10933_call(), 0)
call_20953 = relay.TupleGetItem(func_10935_call(), 0)
output = call_20952
output2 = call_20953
func_20968 = relay.Function([], output)
mod['func_20968'] = func_20968
mod = relay.transform.InferType()(mod)
output = func_20968()
func_20969 = relay.Function([], output)
mutated_mod['func_20969'] = func_20969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10556_call = mod.get_global_var('func_10556')
func_10558_call = mutated_mod.get_global_var('func_10558')
call_20989 = func_10556_call()
call_20990 = func_10556_call()
func_12567_call = mod.get_global_var('func_12567')
func_12568_call = mutated_mod.get_global_var('func_12568')
call_21003 = relay.TupleGetItem(func_12567_call(), 0)
call_21004 = relay.TupleGetItem(func_12568_call(), 0)
func_12779_call = mod.get_global_var('func_12779')
func_12781_call = mutated_mod.get_global_var('func_12781')
call_21024 = func_12779_call()
call_21025 = func_12779_call()
output = relay.Tuple([call_20989,call_21003,call_21024,])
output2 = relay.Tuple([call_20990,call_21004,call_21025,])
func_21027 = relay.Function([], output)
mod['func_21027'] = func_21027
mod = relay.transform.InferType()(mod)
mutated_mod['func_21027'] = func_21027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21027_call = mutated_mod.get_global_var('func_21027')
call_21028 = func_21027_call()
output = call_21028
func_21029 = relay.Function([], output)
mutated_mod['func_21029'] = func_21029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17902_call = mod.get_global_var('func_17902')
func_17904_call = mutated_mod.get_global_var('func_17904')
call_21030 = func_17902_call()
call_21031 = func_17902_call()
uop_21052 = relay.log2(call_21030.astype('float32')) # shape=(10, 14, 4)
uop_21054 = relay.log2(call_21031.astype('float32')) # shape=(10, 14, 4)
func_17001_call = mod.get_global_var('func_17001')
func_17002_call = mutated_mod.get_global_var('func_17002')
call_21057 = relay.TupleGetItem(func_17001_call(), 0)
call_21058 = relay.TupleGetItem(func_17002_call(), 0)
func_15095_call = mod.get_global_var('func_15095')
func_15097_call = mutated_mod.get_global_var('func_15097')
call_21061 = relay.TupleGetItem(func_15095_call(), 1)
call_21062 = relay.TupleGetItem(func_15097_call(), 1)
func_12990_call = mod.get_global_var('func_12990')
func_12991_call = mutated_mod.get_global_var('func_12991')
call_21063 = relay.TupleGetItem(func_12990_call(), 0)
call_21064 = relay.TupleGetItem(func_12991_call(), 0)
func_16272_call = mod.get_global_var('func_16272')
func_16274_call = mutated_mod.get_global_var('func_16274')
const_21066 = relay.const([0.660037,0.483522,8.897168,-6.112250,-3.425835,-1.242533,-0.499976,-3.229010,-7.888424,-2.784470,-0.093492,6.785453,-6.339184,6.747042,8.284090,-2.236359,-0.036985,2.056561,3.440504,8.399114,3.709886,9.555546,-7.278351,7.992580,-1.369724,-9.377842,4.430773,-7.607573,-3.807104,4.560085,4.040747,-8.111786,-7.068879,7.136937,0.396758,7.826672,2.715296,9.163667,-7.752915,-2.206858,-3.662967,7.103601,-5.490008,-3.461930,-7.329313,-6.318044,8.314119,0.843527,3.317709,-1.591032,5.535175,6.069415,-1.763280,-2.389723,-1.613901,8.377809,8.725864,-5.534778,-1.276434,-3.904810,5.839432,-9.633804,-5.261277,-2.334348,8.688990,-2.267546,-3.896693,5.528316,-0.896071,-0.283408,-8.399897,-2.834721,-0.869222,7.249271,5.794125,9.330343,-7.151277,4.108558,1.004798,-2.366457,-1.946678,2.028154,5.284307,2.288070,-9.933651,-9.000280,7.507281,-5.661184,2.271265,3.378279,-3.944689,3.969401,-0.738797,2.469794,-2.254783,-7.877436,-3.432262,-7.433402,-7.953983,-3.175104,2.562761,0.940473,0.162079,-4.631291,8.411646,4.796202,0.559497,2.195979,3.467022,0.368412,-8.231428,8.375407,-0.512568,-9.721529,1.504179,8.889112,9.005096,-3.466161,6.045462,-1.475414,-1.311601,-3.582449,-1.961006,1.480035,-7.703508,-5.097663,1.417259,9.912756,2.180128,-0.564033,-2.536002,2.646014,6.326157,-4.258575,-3.911913,3.604496,-9.561711,-6.990975,3.154118,2.317269,5.581159,3.353866,2.608023,-8.587567,-4.911864,0.590620,-1.056986,1.337377,-1.598513,-3.919690,-2.986688,5.378696,0.684459,5.403593,-4.731835,-2.438237,-9.697271,-2.989455,3.703078,-5.443931,1.511393,-6.389957,-4.822629,5.792326,-9.223845,-5.931590,-3.878210,9.518002,2.845869,-8.316641,5.015638,4.218874,-3.016338,8.986357,-1.096822,-6.181779,-0.402831,-9.336806,-8.856840,3.742371,8.345263,2.171187,-5.662400,-9.054464,1.486947,5.773325,1.059361,4.780158,-6.235289,2.606858,-7.799203,-9.003814,9.160666,-7.766192,1.529722,-2.640435,0.414061,-3.394987,-9.207573,0.923267,1.592125,0.058110,-0.967151,4.732133,4.411787,4.610228,-9.507606,-0.479261,-6.143848,4.559239,2.400717,3.482873,9.590031,-7.750844,-8.642459,7.405494,-5.352516,-4.219049,9.252799,3.083813,6.830515,4.458019,-7.738348,4.746895,-0.904841,-9.585297,-6.359644,-9.809680,8.225808,3.639302,-5.266105,-5.088156,0.770303,4.836583,-4.113601,-9.703617,-6.958108,7.336088,7.910159,4.791840,4.857129,1.268444,6.709368,6.641647,-0.761093,-7.969000,9.167089,0.792569,-1.283152,-6.506222,3.340399,-9.050729,-6.032121,0.927775,-1.581808,4.720982,-5.168031,8.245153,-0.032256,3.780391,7.639334,9.558614,-7.345152,-4.247011,-3.186424,2.365437,0.588980,4.798263,7.804541,1.368372,2.132274,2.161798,-0.555623,-8.795680,5.430089,5.559992,0.090015,8.051534,-9.926597,-6.815474,-7.122983,-7.906853,0.987812,0.667075,-7.445790,-4.535193,1.395816,-6.775788,-2.213948,-9.061561,-1.442246,8.915291,8.713332,8.984331,-2.432679,-8.462938,5.046723,-2.401186,-1.433988,3.806132,-6.591984,-6.928471,4.327545,2.859010,2.139738,2.674415,-0.686475,-1.517909,3.924961,1.798671,7.078976,6.840787,-5.941370,-8.415409,7.413155,-8.142673,4.409860,-1.997182,3.212932,4.324985,0.467231,-6.033183,7.840858,4.410077,-6.920049,-4.925540,-6.276515,-9.736295,8.207503,6.385333,-7.494635,-1.274367,7.280771,-9.362396,0.118680,1.380993,-5.631785,-0.795249,-8.918034,-9.017082,-6.106875,2.778381,-7.672371,9.550761,-3.844833,6.421039,-0.013026,-8.245223,-3.524947,-3.855520,-7.983532,-9.369009,8.457711,-0.971911,2.043386,-0.292838,5.639762,-8.132823,5.032567,3.641260,6.771353,-3.387995,2.784325,3.800255,6.493225,3.467476,9.321880,-4.560544,-9.810748,8.563868,-0.059956,0.716216,0.574341,4.774211,3.640280,-6.078880,6.643538,3.554723,3.547702,-5.379993,-0.271211,5.293686,-7.351554,7.219117,-3.158610,-7.811086,-2.091502,3.478208,8.175999,9.285599,7.798416,1.634742,-9.124385,7.374324,1.065048,2.930485,3.480542,-7.626266,-7.788662,-4.767020,-2.543956,6.918570,-1.408788,-7.050801,-2.822334,8.021958,3.276001,-6.684525,0.126294,1.463535,-0.904091,-3.729092,7.705867,0.499606,-6.699291,1.866008,-8.148104,-1.556540,9.768201,-1.740782,-4.224253,9.596202,6.911479,6.772782,-8.849404,7.817806,7.709021,-3.785117,-6.008632,8.097661,-4.344267,0.625544,1.364083,6.359806,-6.124497,-7.567418,4.772562,-5.977992,-4.116629,0.799523,4.152296,1.772221,5.207868,8.726126,9.328285,-4.725688,6.105264,-4.645103,5.774410,0.676505,8.831843,-9.995661,-5.273613,9.876007,1.138038,4.918876,-4.882898,6.769755,-7.171784,9.234959,4.778341,8.010899,-7.559458,-6.914039,-4.541695,3.893660,0.565323,-2.218585,7.945875,-2.811667,0.200057,1.193954,-4.471808,5.298042,2.260410,-4.926628,-7.638992,-8.954992,3.819417,1.059097,-4.987386,-0.281348,-8.453219,9.678494,-7.845109,-9.108072,7.983412,0.014074,0.264079,2.725778,-9.845505,5.721813,1.738296,3.091714,-9.599637,-0.627603,1.569561,3.666898,-2.177016,8.174693,-9.573960,-5.733130,3.940352,-9.645215,-6.728281,-7.283662,0.798063,8.348438,2.984153,-5.768226,5.701438,-3.262902,2.089807,9.260783,2.865081,-6.174480,-4.318665,2.150714,5.929892,-1.604977,1.037817,-2.529067,2.087843,-6.405439,-3.317387,-0.823319,2.716260,-0.531739,-9.900376,-5.081368,9.427872,-5.789747,3.316968,6.178501,8.674562,-8.502129,-2.995531,9.897708,7.886651,-8.332643,-2.167108,7.102818,-8.908576,-6.950187,6.290543,-8.106526,-7.521636,7.595348,-5.735661,-2.782994,-4.744396,0.818699,2.200182,-6.387490,-8.178938,-0.361351,-9.210222,-7.124993,8.550369,5.118558,-6.842775,1.975434,-9.597437,-6.139252,-0.338313,-2.458547,-4.042473,4.864283,1.330509,-6.129995,3.955135,-9.213200,-8.249219,-7.302434,-1.243400,0.218102,1.741822,6.342554,6.353896,-9.515844,-4.123736,-8.719457,-4.025228,-3.209126,-8.598610,2.551489,9.214100,8.801929,0.360475,4.688543,2.441500,-5.567168,-2.248314,8.808967,7.491652,1.127836,-3.108070,-1.042748,7.650264,-9.890085,0.797424,0.012637,-0.232760,5.394498,-0.973325,1.913527,7.997552,-0.478481,2.715734,0.833450,-0.555992,-7.270748,-3.108283,4.070448,9.346951,7.869806,-7.957657,4.192401,5.063519,-9.205413,9.143140,-3.603571,2.947858,-2.269234,-5.642112,2.288521,-2.021116,4.142569,7.814731,8.474481,5.942034,4.583689,4.163959,-4.676229,9.647973,6.229329,-8.440269,1.425498,-2.853288,-1.021235,0.263268,2.426288,1.332439,0.077984,-3.069931,3.270126,8.877436,0.948133,9.470091,-2.479119,-1.960316,2.086088,2.257022,-4.791788,7.451484,-5.105642,-2.193711,-0.456704,-5.936228,-3.006344,-2.236896,-0.667304,4.010406,7.344265,1.412114,3.995484,4.011274,-6.614722,-9.921154,-1.003580,5.419677,-6.177994,8.221436,4.791320,-9.563669,-4.159923,4.651739,0.533570,-2.417319,9.588591,-0.392974,8.384958,-0.129203,-7.530611,-1.784353,-0.383257,3.612594,0.301339,7.040814,-9.651243,9.933713,0.439710,-1.214746,9.767820,9.703517,-4.481142,6.114165,9.769910,-7.675310,-0.297714,-0.477441,-3.598789,-1.264957,-7.532324,1.894073,7.250088,0.624946,6.831899,4.086794,-8.136544,-8.629414,-3.473056,-6.746421,7.866927,3.030736,3.452470,-4.736874,5.033973,-3.360961,-7.679781,8.431896,-8.537856,-0.910091,-9.224311,-3.955569,-3.335550,7.955043,-4.235063,-0.678741,-1.414019,-6.533919,-7.550479,-8.071163,7.383672,7.481613,-2.784714,0.664168,-9.097125,-6.590174,-3.719235,7.858971,0.541103,8.584895,1.732637,7.365067,-3.202588,3.898539,-2.114677,-8.753340,-1.415225,-3.515465,-0.156143,3.589147,3.995083,1.154720,-5.247717,2.825675,-0.808358,-7.557109,-8.578944,2.934736,1.814279,7.581482,-4.614312,0.005797,-2.109075,4.432926,1.770350,1.572402,3.498390,-2.426136,0.004814,1.381322,7.941033,4.873611,-3.194472,-8.116430,-3.079847,6.618672,1.397460,8.000671,-3.722232,8.119893,-4.577559,7.917678,1.023145,0.484326,3.464350,-3.233041,-2.454956,-2.279035,4.687608,-6.075056,0.022146,-8.156043,-4.882809,-8.685867,1.640047,5.166892,-0.271844,6.146413,-0.602174,-9.356606,8.776510,-3.054189,4.865957,-7.678172,0.074096,-9.106885,1.806613,-5.379862,-6.919482,-5.061498,-4.535641,7.573270,-2.926478,-5.192984,-9.053714,-1.176643,-9.768206,7.077134,-7.798665,-5.534077,7.753201,-9.823113,2.005787,-1.775112,0.217719,0.241137,-3.302786,-8.371976,5.915522,-0.882806,9.424251,-5.064029,4.734079,8.508620,1.219417,-4.449007,-9.312569,5.975982,8.016336,-6.110450,5.759003,-7.420584,-5.498106,-8.197593,2.294760,2.827539,-7.830159,-2.202942,-3.367811,0.770012,5.138465,-3.352256,-5.063289,-9.539260,4.825178,-8.616590,-0.506087,0.721081,6.593952,5.249353,-2.293574,9.222399,-3.903398,-7.772603,-7.992356,-2.704164,7.555535,5.728037,2.250342,7.296380,-9.722796,9.154785,-4.200453,-8.818002,-7.997302,1.999864,-6.097883,6.120207,-0.228896,6.749474,0.090930,3.128200,-3.610326,-6.733858,-6.100256,1.114500,8.383601,1.930169,0.791955,3.076243,1.866812,-7.781996,-8.966836,-4.271485,0.526491,9.480489,-6.854940,-1.222760,6.845376,-0.585035,-2.917869,6.120004,-3.337236,-6.377923,-0.126143,7.568247,-0.837654,7.538532,-8.675209,8.088162,-9.763506,-6.581489,1.619080,6.958637,-0.609374,-3.118474,2.763198,-7.164780,2.102381,9.061522,0.475233,5.640692,-6.770420,-8.921945,6.123648,8.314566,-6.564052,-9.553714,-4.255579,-3.761998,6.686319,7.171912,-5.761395,-7.279156,-8.041950,8.819144,-0.498279,5.863450,-4.543027,2.459782,-2.972257,8.567605,3.376888,-3.848672,2.936710,-0.128466,-5.737807,-3.426012,8.272694,-3.313169,-0.788952,1.154873,-9.104796,-3.033561,-1.637744,-3.135898,-1.066256,5.067629,3.507841,2.841614,9.504266,3.098696,4.274172,-1.840250,-2.056500,1.039932,6.362692,-6.177383,9.719593,-1.432756,-8.691781,-7.786958,-5.365845,-7.954989,-6.425357,-8.080921,7.027505,9.109239,4.731149,-2.234083,-5.960391,7.920971,-3.429760,7.437893,-1.496599,-5.083017,3.297015,9.856674,-9.082418,0.566886,9.017206,-7.752057,-0.503484,3.166282,-6.341387,8.974318,1.797443,-6.326935,-3.563383,-7.045953,3.034279,-5.908615,0.490937,-3.318658,5.124637,-9.742095,8.264233,-9.154288,-2.205082,-7.289081,0.545396,2.222587,-6.618231,-2.385921,-6.348378,5.390777,8.987465,-6.735863,0.835557,8.879065,-1.065763,3.184803,-0.572443,3.749453,8.199885,2.022042,-4.025500,-0.613277,-6.531759,0.288427,8.394329,-5.996258,-4.310622,1.147895,8.144078,6.146921,9.156746,-3.467962,-1.195876,-3.802260,2.707517,-4.968681,2.658212,-3.125944,6.806352,-9.044419,-5.806190,-5.523250,8.711963,-6.510351,-2.770470,-1.441978,-2.726282,4.915047,1.374179,-9.180851,-6.726674,-1.420734,6.234761,7.255650,-5.909029,6.496735,8.014006,-6.347880,-9.892835,9.941516,-4.614954,-3.519481,-2.465769,1.696208,2.115266,-3.920776,-2.550609,5.026432,3.250855,-5.375649,-5.087338,-9.620455,3.076734,-3.654126,3.732166,-6.831960,-1.275803,-5.782111,9.369187,-2.755823,-4.919241,-5.777650,9.445780,-3.461502,-9.086078,-6.929266,9.318114,-8.762817,2.579946,-7.600964,4.662074,-3.484892,4.864314,-6.471624,-1.174115,2.918080,-1.100576,4.313244,-9.063524,-1.747775,5.057062,1.239384,-6.818855,3.538993,9.182214,-3.570241,1.218086,-3.046930,-6.307746,0.159334,2.271400,9.790603,-7.018072,5.028213,-3.179697,3.562410,-8.683702,-0.993406,3.135413,2.167199,6.278700,7.265434,-0.064659,2.385893,-4.826213,-6.474204,-1.514190,6.253318,-0.419908,3.112095,5.066981,-1.744479,6.254128,-7.055501,3.840535,8.203765,6.880766,7.655510,-2.618340,-2.068956,9.257702,-6.359753,-7.804684,-0.078030,-3.821406,-1.910522,-7.447734,-0.968897,6.601614,-1.640699,-2.917829,-7.842360,-6.206875,3.743360,-0.763573,-2.637234,-1.254508,5.993453,-3.701798,-7.730033,1.843004,-3.098915,6.913132,-2.478090,2.268618,4.101403,-6.191961,-6.465363,6.535793,-4.311453,9.925311,8.290395,5.187358,8.645113,-2.179722,3.100063,-7.781184,-6.589654,-9.621078,-2.818009,1.524211,7.586753,0.274665,9.170060,7.747731,0.419758,-9.983861,8.394367,4.690018,2.772317,-0.388718,-0.813624,0.758905,-3.339364,3.766116,5.802542,3.315492,-0.381887,-7.412540,4.279233,9.487036,3.471106,-4.001280,-9.163957,5.367262,4.951531,-5.832202,-9.533923,-2.088865,5.235372,9.440665,0.932169,4.442691,-8.513904,4.694679,8.745598,-2.738804,-0.937917,8.652661,-0.285565,-5.699612,-1.092966,2.388187,-0.190714,-0.284528,7.141761,4.131595,-6.309151,1.822247,-4.841085,-2.335786,4.908493,-7.903366,2.752239,-6.306164,-4.550699,-8.057770,7.455735,0.537659,1.042258,6.448203,-5.667845,5.786665,5.750402,3.691067,2.948903,-5.681532,-4.465725,-1.483975,-0.612870,0.524574,-2.528983,-4.388787,-4.414269,6.274997,1.088064,-5.995078,8.772714,-8.538648,-5.121789,1.281672,1.005867,8.202763,-4.451028,-3.277189,-0.650882,-4.892451,0.043732,6.959946,-7.353221,4.689056,4.824613,3.144101,-9.567637,-7.144446,0.364993,-9.341657,8.316886,-4.987706,-1.064574,-1.971144,4.820614,9.608285,1.127312,-3.537395,0.816293,7.438236,0.033906,-5.299513,-1.971201,4.406915,-9.933477,2.113613,1.195481,0.805449,-9.012462,-3.931281,-2.660417,-3.555451,-7.709073,-2.211791,-4.814642,9.664638,-7.904268,2.639055,-1.533784,2.068916,9.639472,-5.436209,-9.209397,-6.928841,4.413033,-1.913001,-9.161195,-4.761265,8.210670,-4.687149,-2.698428,-4.455965,6.528977,-7.809893,-1.963464,-1.711950,-2.347821,-1.351451,7.111237,7.387338,2.664142,-6.356007,-7.013385,5.780400,7.921625,3.990409,5.310961,6.245244,-9.458843,-0.919602,6.147541,-2.590557,9.712080,-6.547711,1.955925,2.196096,-7.348351,-8.259588,-6.363247,-2.334482,2.962232,-4.942079,7.598867,-0.300816,7.249250,-4.240823,5.924671,-1.126311,0.485518,5.742557,-7.189503,-1.984191,0.119044,4.335780,-1.975861,5.190416,8.064635,-0.217308,1.177073,-8.798139,2.808090,9.518041,3.945894,5.350327,0.515071,3.522352,3.461092,-3.891169,-8.986115,5.351089,7.687619,5.144356,-8.985507,-1.776165,-6.726202,-1.947904,3.248872,-9.435331,4.079078,-7.695980,9.164550,-0.644603,2.989110,2.873634,-1.780043,-4.170468,3.070899,-0.218956,4.858645,-5.862745,-0.458171,8.367620,-1.207855,-4.169977,6.227567,-3.307893,4.646421,8.137304,2.170397,-5.317548,1.706005,-2.430408,-9.948981,-2.753097,0.945188,7.526708,2.228834,6.275238,4.689134,2.039126,-7.418510,0.099600,-0.160293,-4.800853,9.019886,6.067440,3.865084,1.284587,9.951396,8.586694,-9.808777,-7.525166,2.400703,-5.235363,2.253856,4.119075,6.359726,8.304840,-6.993775,-8.746050,6.289119,-8.319546,8.746835,-0.927086,-9.974518,0.531735,4.556988,-2.515306,1.651138,4.980078,9.115042,8.887325,3.910608,-8.497168,-6.454493,0.990885,3.857328,2.890432,3.065288,3.540693,0.922510,7.981364,-3.275294,-0.473437,-4.242482,-1.122179,-8.182055,-1.633219,0.981593,5.536733,0.224435,9.540510,8.318897,4.739755,-1.281552,-1.535244,0.448951,-4.663304,2.068204,-9.180560,-1.534539,8.221857,-2.368961,-8.771155,6.111438,0.675916,-0.232994,7.416910,7.735088,4.092443,3.090418,-2.385319,7.015652,-3.111938,3.500099,-4.656506,7.018143,-5.402422,8.544391,3.940657,1.669389,-7.730891,2.848893,2.791061,-7.252623,7.796044,-9.277493,8.305831,-3.866540,-4.461632,-4.399602,-8.649472,6.493244,6.411818,9.705536,2.686813,1.196242,8.803037,9.577806,-4.756444,7.086317,4.482588,0.503702,4.800660,-9.659166,9.744081,-9.026397,-8.871674,-6.181737,-1.501958,4.641749,-2.283999,9.243929,9.845790,-8.987897,9.586764,6.577865,1.421921,2.915885,5.411186,6.309228,-4.466557,-3.111574,7.981799,-7.976856,-0.834609,3.158364,-9.618448,-5.363361,5.283555,3.521826,-1.465422,4.078810,5.138012,-9.664230,-1.114120,2.715461,5.986190,9.211012,4.149054,6.455685,6.703964,-4.124430,3.546967,-9.495275,-3.077920,3.077216,-0.410292,-4.411685,3.097461,-5.203192,-9.834749,-3.994268,6.463030,-2.326337,9.004069,2.770908,-0.624522,1.808859,-2.054740,-5.412413,9.195123,-0.447394,-9.843568,-8.648681,0.034287,9.110529,-7.116712,-2.344343,-6.603035,-5.397363,-0.833772,-7.585450,-8.708995,-0.222443,0.574066,1.857381,1.628718,7.922136,-5.085259,5.767501,-1.361105,-7.223341,3.631562,5.820751,6.109246,1.274599,3.681229,4.740977,0.152575,-1.349998,-9.723365,-8.420085,3.226900,-8.879205,3.688667,-7.758714,-1.916493,-2.910635,9.351827,0.078551,-8.172261,-3.043596,5.226236,4.273988,4.912181,7.184151,1.373545,0.743466,2.546997,-6.555419,-4.675838,6.229555,6.451877,-1.758401,6.668562,-5.308426,-3.159330,5.909067,-7.045248,2.741031,-5.160497,3.991045,-9.360587,1.213113,-6.423428,-2.348453,-6.798279,-2.972878,8.206054,-5.540300,-8.751943,-5.235132,1.850186,-4.818239,-3.435488,4.753279,4.471784,-0.794178,-8.640418,1.904730,-3.267412,5.854245,7.702884,-7.831307,-2.707494,1.849008,3.991256,6.461682,2.553562,-7.659626,4.800345,5.521905,1.633585,-7.183500,1.630906,-2.749068,3.894110,-6.519758,9.099280,-3.800531,2.183832,2.068723,3.804693,7.262594,-3.790739,1.438880,9.861543,-0.848271,-6.077831,-4.774856,6.968402,7.826627,-9.502894,8.138872,1.480214,9.152846,-3.847527,7.690446,-6.486797,-4.341169,9.296752,-1.777550,-7.365431,4.242828,-2.739139,-8.992543,-0.368390,-4.090075,6.308386,9.344257,6.454187,0.411950,8.466284,-4.000509,9.070561,-1.383442,-8.852413,-8.484671,-7.507141,3.738224,6.189217,-0.481922,-7.612015,4.678602,-2.588701,-0.547500,6.544319,0.347077,-1.142779,-3.161658,6.998898,-3.837603,-1.589232,-3.695261,-3.539755,5.602842,-6.679772,-8.818825,-9.225822,-7.892424,-7.945792,0.783239,2.695391,-4.375354,-6.446612,2.177459,0.784561,4.608764,-8.783353,-9.097328,4.446903,5.302380,5.494534,-2.158388,5.928782,1.886465,2.378290,2.861140,7.331691,6.360103,1.086574,1.421782,-7.379082,-3.858806,8.178512,-4.167547,-1.353998,-1.747565,8.856733,4.263337,6.210465,-5.015927,4.910189,6.354635,6.667156,-7.967446,-5.872490,8.385722,-6.986244,3.674300,0.903843,8.990216,5.270837,1.621379,-4.751764,4.199649,0.253051,3.232125,-3.934316,-2.133667,1.173676,-5.341906,-6.607201,-2.346732,5.412092,-4.557377,2.454690,-5.083058,6.052735,3.829853,-1.259197,-7.151498,-8.896881,9.309001,-5.239624,-3.073708,-9.745969,2.007625,5.133974,-7.749232,-5.417172,5.971978,-3.962437,-8.064029,0.541894,0.618205,0.060925,-2.670156,2.237962,-5.919837,7.742494,5.247982,0.016247,-7.495865,2.268793,9.744501,-9.395945,7.479661,-2.192084,-8.279664,-7.488983,3.182600,5.006905,2.339869,0.089105,6.155926,2.526819,3.279645,7.808875,0.271498,-8.849267,-9.332504,6.767786,3.699878,-8.101344,5.734229,7.943544,-5.196063,-2.891218,-3.450325,0.481995,-3.544728,-0.448587,7.908373,-9.541208,-7.223500,3.709374,1.014696,5.151122,-9.386818,-5.341721,-0.174503,-5.156936,2.414991,-9.906034,3.039861,0.032605,-9.090950,3.668253,9.346334,-3.981865,-8.152254,1.194452,-0.949537,-7.992727,-1.114926,8.431304,-7.895933,5.728401,-7.483079,9.020658,5.191866,-7.301050,9.578761,6.330794,3.477483,-8.109349,6.337540,7.422000,-9.015038,-6.236326,-6.756227,2.640690,9.988514,-8.456486,2.670709,5.076266,-2.028614,-2.662457,7.188927,4.011177,-6.720973,-6.011596,8.601394,0.895313,6.306679,-9.275089,1.604272,6.486867,-9.954050,2.414338,2.424243,-7.477321,-3.713424,6.774550,-9.171357,-8.738497,4.653440,-8.641884,-1.011173,-2.045229,5.063474,8.816656,4.600805,5.205165,0.818892,6.792118,-6.351404,-4.768560,-1.647372,-9.902603,-6.162063,4.517541,-7.348204,-6.884877,-7.741172,-9.163489,4.102437,-0.148216,-7.168279,-1.652204,-2.634432,5.033625,9.193196,2.986780,1.593686,-4.122323,-3.371358,9.238483,8.724638,8.708364,0.728730,0.558635,-9.773443,0.566519,-2.927303,-1.063526,9.983228,9.003093,7.096273,-1.232591,-5.282548,3.873598,8.881747,2.663369,-5.503600,-3.947862,4.685508,6.627930,3.978812,-3.116661,-1.998836,1.496405,-8.217213,0.666174,5.905618,9.856262,-1.560009,1.545282,2.778459,3.645445,0.089590,4.321751,5.323632,-9.850241,8.739292,-3.426530,3.885505,3.920471,-4.811095,-7.757857,1.667237,-0.853280,-3.103746,6.200460,-6.897732,5.662006,-3.271942,-2.943707,6.129208,-8.868122,-3.293814,5.030482,-2.661972,6.533583,3.941706,1.646550,2.871656,-9.621160,8.409075,-8.258398,-6.147890,4.281579,-6.567661,1.714966,6.117953,5.430779,-8.741109,2.927811,3.936813,-3.519732,-0.116007,0.191995,9.848463,2.874775,0.798509,-5.222092,-8.132119,-3.442079,-3.117562,-3.919506,-3.964010,8.596251,-9.389088,0.528257,8.612589,-9.396767,0.284628,-5.015275,-2.346911,1.641103,7.815001,5.696320,-3.440598,-2.676699,6.129214,-0.483554,-0.789517,9.791124,-6.892040,9.045445,-6.198912,-1.190069,2.797863,-1.568344,-6.045172,-8.738455,3.326348,0.734641,4.311450,-9.561705,2.057454,-9.780358,-4.007936,-1.501494,6.817428,0.851948,-9.886789,6.056886,-3.530723,2.908589,-2.610110,-8.958215,4.263964,8.265623,4.551789,-7.233564,-9.918737,7.432213,-1.157946,1.363343,8.046317,3.934391,-4.066125,4.025149,-5.088638,-5.520896,-4.568646,-0.202417,-2.536454,7.408846,-2.228811,-5.092315,-0.894339,2.881419,-7.563369,-1.006819,5.073496,7.789615,4.707231,-1.940050,3.851572,-4.838636,4.062104,9.854586,-2.373412,-2.114631,-6.563845,6.944077,-0.993031,4.017897,9.521734,-7.502042,9.657663,7.237393,-7.655576,-8.203758,-0.264642,-5.902010,-2.820277,9.928786,-7.786228,0.414989,6.951881,2.254460,0.898324,-6.571690,0.437692,-4.552167,-1.528673,7.401681,7.270297,-0.228576,-9.224033,-8.991807,-1.721286,0.480514,8.170626,-7.930872,1.401340,-9.867670,-1.704941,6.999463,5.795250,2.938635,7.220641,-9.011975,-0.315536,-6.368398,3.060501,3.589724,7.712436,-4.798903,8.322949,2.785387,0.599220,-9.462038,-6.879970,7.785269,8.112093,9.950117,4.673730,9.295182,-7.022875,-8.316295,-9.033828,1.786734,-6.888170,-6.335816,-5.441877,-9.795449,0.352868,-1.785963,-0.549051,2.573829,-3.594276,8.655998,1.048592,8.264182,-6.343321,7.797974,-7.416332,-4.201333,2.413001,-7.572010,-1.270816,8.198501,6.848927,9.006751,5.868855,2.667369,8.216295,7.919032,-9.990742,-3.820787,-9.702144,1.804635,2.025115,6.786407,9.017762,-9.490375,-0.357757,2.132301,9.498702,1.437674,-6.084944,-5.748185,2.421425,-9.145745,6.052195,8.017521,-6.050618,-7.927710,-2.805081,-9.198050,0.688464,-0.883764,-6.829998,-4.982066,-0.091513,-5.675110,-6.668472,8.638301,-1.622363,7.571454,-8.888651,6.533952,-5.595076,-7.847574,1.755582,-2.130563,-5.550780,-9.337851,-0.216371,-7.170764,2.459528,2.439429,-2.942762,2.709161,-8.705031,-4.717860,4.573443,-9.727258,2.420508,0.478491,0.962190,1.725013,-9.300861,3.271856,-6.023101,4.325360,-7.014131,-8.651696,7.194595,-5.185371,-7.601541,8.132832,-2.894619,0.881864,-3.555292,2.024426,-3.360706,7.690820,-0.077245,-7.282446,2.560892,-9.960183,-1.637059,-9.411081,4.570278,-6.084611,5.106213,0.159474,6.046599,3.934901,1.318396,3.200314,1.487013,-3.209730,4.011772,5.435220,4.113302,8.703307,-4.365188,2.781151,-7.257378,1.085193,5.226736,0.279035,-8.859684,7.831431,4.088223,2.638633,8.214501,7.943141,-7.226406,9.702448,-4.895472,-0.375231,-3.422801,-4.658703,4.456960,-6.361391,6.831595,5.552367,-3.769360,7.491148,1.694751,8.949644,9.216855,-3.045411,6.142162,1.278542,-9.706185,-8.238378,8.822352,7.315013,-3.421434,-3.406453,1.602399,8.603338,-2.228206,-1.048617,-8.539258,-3.143043,-8.357401,8.175753,5.083127,4.564116,-7.570442,-6.499298,6.642160,-4.774432,-9.873600,7.189904,-6.684861,2.956019,2.279499,4.178923,0.305374,6.228074,-8.282425,7.956236,2.278766,1.814231,-9.713700,-4.516927,9.762083,-8.857998,6.390945,4.476836,-8.857599,-0.800367,-0.157644,2.932865,5.923426,3.123207,-5.728776,6.419972,-8.523974,8.987788,3.627110,-9.203142,7.485940,-2.041007,-6.423181,-2.554473,-9.971049,-9.870675,-3.854207,6.189434,4.314601,0.025533,1.894115,7.929764,6.837209,6.646331,-9.327213,0.232649,-2.399448,-1.827868,-1.077868,4.223543,5.656610,2.250491,-5.632893,-0.583185,-1.991833,5.015247,-1.587086,3.976429,3.814904,-6.938317,-1.140530,7.426317,9.906815,1.052142,3.940924,2.722705,-7.538841,-3.061271,1.870197,-5.281647,1.263481,3.640142,7.279448,2.860444,2.861226,-5.229129,-5.068076,-1.133323,-5.164785,1.823862,8.236258,-2.066514,3.964472,-7.426264,1.834075,-7.105043,-1.904176,6.418880,-7.374962,-1.417074,-4.652305,0.215969,9.617971,8.191855,3.826029,5.778401,8.598821,9.213183,-4.796067,8.802228,-3.436809,-4.234948,8.172916,-2.145824,8.658498,-2.087826,-8.928377,-7.293685,4.501656,5.271651,-6.704131,6.712635,-8.560787,-2.289628,-5.896424,3.334694,-2.710288,4.055925,5.447512,9.484877,3.491830,-4.514972,-8.066077,8.454419,-8.029605,-3.282230,1.489654,-2.814194,-1.937143,-4.154812,-0.768339,-0.432273,-1.061002,1.510497,2.430679,-3.221654,-8.499892,-5.519638,0.730657,-4.989310,-0.994715,-0.570942,7.790850,-9.296770,2.040080,-6.993509,-2.158957,-4.084823,7.508340,-4.061016,8.720485,9.353977,5.071479,-2.659838,5.325484,4.939646,1.821155,4.226971,-0.366185,1.951717,-1.635477,-6.121433,-6.215590,1.571239,-8.174328,-6.394907,-3.453178,8.124665,-7.006701,-1.333591,-6.868134,8.277267,2.403831,-1.340640,-2.745043,-3.760400,-1.111152,5.853655,9.812399,-5.831833,-2.317438,8.134432,-5.718509,7.534235,-6.524171,-3.951034,3.421351,1.748758,-6.633774,-0.969805,1.430444,7.493375,7.209342,-3.593640,-0.702920,-5.026369,3.108220,6.014216,-7.066613,-3.049427,3.978285,-2.253680,1.397762,2.904428,1.558829,-7.993944,-7.034874,-7.385346,4.574352,3.928342,9.249314,-6.191950,9.315156,-5.927283,-8.460355,0.458174,3.458116,-5.148721,1.794677,-7.090470,-7.122427,5.168730,7.885493,-9.020680,-7.679730,-5.024479,-1.555974,-9.356192,-2.308914,6.366175,-5.562131,-8.940544,-2.007128,-4.331566,1.819073,5.925770,8.046501,-8.481284,-3.870866,9.573072,-8.092582,3.202813,5.607394,3.257831,-4.959959,-4.554997,6.816672,4.493220,-8.170752,5.905673,-3.280120,7.537254,6.073278,-8.543698,-7.352433,-5.649553,1.317499,0.858711,1.446987,9.608565,-3.790316,-9.472199,-6.128561,4.671093,2.685942,-8.419397,9.925085,-5.272966,-3.312665,1.875314,-7.548069,6.940891,8.967792,-4.143071,6.823637,-6.237401,-2.346526,2.283137,-4.953854,1.870123,1.721035,-6.526095,8.989004,8.174760,2.025849,-0.187256,-0.924317,-7.405605,4.551152,7.107627,-8.623938,-6.933043,-6.321219,5.042185,-0.010306,6.916625,6.515199,5.650674,-0.081885,-8.478885,2.475340,3.336265,-4.055815,0.225511,1.086064,6.882862,-5.798171,-8.908344,0.017052,-8.291748,-0.627813,-9.585124,6.770711,-0.470260,-3.365679,2.393594,8.430616,-4.096286,-8.111344,6.069879,-5.795726,5.369397,-5.921260,6.789157,-4.389455,-0.913443,7.785178,-9.486098,-7.576280,-9.711940,3.417600,-4.625379,9.561499,-8.254066,-3.842436,6.892112,-9.400839,0.342760,-7.618189,5.177421,-5.908574,2.680837,-8.719366,-1.708162,-2.106060,0.848559,7.519403,-7.337482,-5.723847,-2.316416,9.527155,5.745595,6.814015,-5.012269,-1.733850,-1.000560,6.245074,-9.688767,5.426422,-2.910270,-3.145963,4.885052,0.782323,-5.223826,-4.581092,-6.854361,-7.628014,-1.647231,0.951624,4.825521,-8.103636,-4.547492,5.868427,0.216539,-2.939592,-1.348624,6.363010,-1.472233,0.268622,6.666531,5.340327,1.379744,0.446200,5.471120,9.801388,-0.001960,-3.463860,4.554225,-7.626285,-8.894536,8.261821,3.733906,-8.797216,1.509917,-8.796829,-5.216336,8.310738,0.770430,3.435938,1.133727,5.730899,-6.617008,-5.713560,6.896501,-5.259636,0.004449,-1.522701,-2.957213,-8.822007,-5.872081,-1.073953,6.341928,6.894258,1.471541,4.521011,1.496587,-6.671259,0.558440,4.926607,2.201454,-1.046243,0.062257,1.043118,-4.291074,-2.202737,-1.797228,2.218404,-7.002103,-9.842176,1.955654,-4.192385,-1.871651,-4.429583,4.497516,-6.112281,9.599449,-7.525633,9.719953,-5.485478,9.231636,8.260873,-7.697082,2.428281,7.349980,-5.453538,-9.397569,4.963873,0.331457,-8.516150,7.553773,-1.856737,8.516959,-1.889481,-2.936906,-0.898094,3.888146,-5.254499,-2.127880,-6.894013,9.146400,-7.230205,7.928446,1.063540,0.598558,2.134293,-1.773859,5.288701,-3.484116,0.999928,8.901094,5.486885,7.123907,-8.208607,7.498166,7.081153,7.770017,-3.906120,2.039383,7.353098,6.567189,6.841195,-0.483628,-1.740175,-0.539608,-7.967117,1.280490,-8.005263,6.141787,8.257362,3.699370,9.208287,-1.313779,0.600192,3.863714,6.799883,-7.728077,5.198159,1.537977,5.028482,2.608051,8.200456,7.519704,9.764863,-4.190519,-7.195277,3.042768,-3.712684,0.395764,2.694907,8.565296,-4.515640,6.688402,-4.639734,9.678146,7.173495,1.909483,5.442149,-7.373385,7.910051,5.777873,8.468172,-6.390050,2.837570,9.797324,-7.072436,6.023371,-0.040747,-1.613510,7.959685,4.796854,-8.092492,-3.360762,3.644237,-5.491028,8.735550,-4.849737,-0.837047,2.047636,0.686758,-4.110093,5.425783,-1.421704,3.865741,-0.824216,-0.222304,7.201874,8.086048,-9.710862,-3.523130,8.328093,5.545844,-7.651332,-1.096686,5.616026,1.808740,-2.144326,8.071647,-3.267395,9.233749,6.265159,-6.347329,3.548678,-7.703305,6.349988,-7.129476,7.661605,-5.462432,-3.417215,5.858564,-4.220960,3.974327,1.195716,3.435539,9.917723,-3.561832,-2.254657,2.969151,-4.931382,-3.154414,5.521902,7.554157,-9.549664,-9.132570,-3.107778,-1.647871], dtype = "float64")#candidate|21066|(2925,)|const|float64
call_21065 = relay.TupleGetItem(func_16272_call(relay.reshape(const_21066.astype('float64'), [15, 13, 15])), 1)
call_21067 = relay.TupleGetItem(func_16274_call(relay.reshape(const_21066.astype('float64'), [15, 13, 15])), 1)
func_12935_call = mod.get_global_var('func_12935')
func_12938_call = mutated_mod.get_global_var('func_12938')
var_21076 = relay.var("var_21076", dtype = "float64", shape = (78,))#candidate|21076|(78,)|var|float64
call_21075 = relay.TupleGetItem(func_12935_call(relay.reshape(var_21076.astype('float64'), [78,])), 1)
call_21077 = relay.TupleGetItem(func_12938_call(relay.reshape(var_21076.astype('float64'), [78,])), 1)
output = relay.Tuple([uop_21052,call_21057,call_21061,call_21063,call_21065,const_21066,call_21075,var_21076,])
output2 = relay.Tuple([uop_21054,call_21058,call_21062,call_21064,call_21067,const_21066,call_21077,var_21076,])
func_21090 = relay.Function([var_21076,], output)
mod['func_21090'] = func_21090
mod = relay.transform.InferType()(mod)
mutated_mod['func_21090'] = func_21090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21091 = relay.var("var_21091", dtype = "float64", shape = (78,))#candidate|21091|(78,)|var|float64
func_21090_call = mutated_mod.get_global_var('func_21090')
call_21092 = func_21090_call(var_21091)
output = call_21092
func_21093 = relay.Function([var_21091], output)
mutated_mod['func_21093'] = func_21093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16614_call = mod.get_global_var('func_16614')
func_16616_call = mutated_mod.get_global_var('func_16616')
call_21178 = func_16614_call()
call_21179 = func_16614_call()
var_21185 = relay.var("var_21185", dtype = "float64", shape = (10, 14, 4))#candidate|21185|(10, 14, 4)|var|float64
bop_21186 = relay.not_equal(call_21178.astype('bool'), relay.reshape(var_21185.astype('bool'), relay.shape_of(call_21178))) # shape=(10, 14, 4)
bop_21189 = relay.not_equal(call_21179.astype('bool'), relay.reshape(var_21185.astype('bool'), relay.shape_of(call_21179))) # shape=(10, 14, 4)
func_16515_call = mod.get_global_var('func_16515')
func_16517_call = mutated_mod.get_global_var('func_16517')
call_21190 = relay.TupleGetItem(func_16515_call(), 0)
call_21191 = relay.TupleGetItem(func_16517_call(), 0)
func_16423_call = mod.get_global_var('func_16423')
func_16428_call = mutated_mod.get_global_var('func_16428')
const_21197 = relay.const([5,8,3,-8,-8,-2,9,3,-1,5,-1,-7,10,-4,-1,2,1,6,1,-4,4,1,-9,3,3,1,3,-8,-1,6,9,2,9,-5,-1,-9,-2,-10,-7,2,3,1,5,-8,2,-10,1,-3,7,3,7,-7,-2,-2,2,-6,1,-10,1,-3,-2,-5,5,3,8,-2,-8,5,-5,-9,-3,1,-6,-10,-9,-9,-8,-3,-2,4,2,4,4,10,-6,-6,5,3,-8,-8,6,9,-10,6,9,-2,6,1,-5,1,3,10,-7,-9,4,4,-3,-5,-3,6,10,5,6,-8,-8,-4,-8,-8,5,-10,5,10,-4,4,3,1,10,9,-1,-8,-6,9,7,9,-7,1,-10,1,-6,-1,-6,2,6,3,8,6,4,-10,-5,2,-5,-3,4,8,10,8,-2,4,-4,7,8,8,1,4,-4,-7,9,-3,-7,-4,-10,4,5,-2,-5,-10,2,-9,-7,-10,-9,-1,8,-5,7,-1,2,-9,-5,5,-9,5,5,4,-6,3,3,6,-10,-8,10,3,7,8,-2,4,-10,-3,-2,8,-3,-3,-5,-8,10,1,7,10,6,6,3,-9,8,1,-9,5,-10,-8,7,-1,4,-7,-3,-3,-8,-7,10,5,8,-7,3,-6,-10,7,2,6,-9,5,1,3,10,2,7,-7,3,9,5,8,-2,5,-4,-8,-6,-7,4,8,-1,3,8,-3], dtype = "int8")#candidate|21197|(270,)|const|int8
const_21198 = relay.const([3.091688,0.264066,1.657943,-9.044785,0.184464,-1.586186,-0.112842,2.463055,5.759502,5.439907,3.051944,-6.648872,8.352918,-5.801709,1.883795,0.216266,6.882436,-5.971589,0.795636,0.026011,-5.066690,6.319411,-5.311122,-8.713834,1.304373,2.434989,-6.530179,0.157224,-9.244526,-2.240702,-7.969105,-7.703629,-3.782082,-9.662748,-3.247123,8.861808,-6.256635,7.385371,5.884425,-6.836657,8.692385,3.500900,5.190494,2.270506,-5.098149,2.968936,6.426049,8.328336,-8.964784,6.745552,9.403024,7.979296,0.027749,-3.987733,-6.948620,-3.986226,-1.944391,1.775185,-2.809085,4.410507,-5.866597,2.943248,6.055687,2.946159,4.304042,-9.222813,9.628462,-8.273472,-9.108632,-8.593337,0.165611,-4.005754,-0.835082,4.135708,7.592690,-1.349264,4.335577,7.702806,-0.983863,-4.817394,-1.083508,-5.458660,-6.128365,-5.295616,3.170328,9.012323,9.195853,-5.031824,0.326862,3.341457,-8.042540,-9.940236,4.493919,-2.594653,-5.733260,4.909308,7.893540,3.581686,-4.198375,-4.208418,-4.881407,-7.569249,-4.801223,2.884195,-0.253953,-7.217657,-6.378744,-9.863864,-4.976258,4.265345,3.452034,8.424561,-3.533882,-3.896199,8.983700,-9.497946,-7.030441,9.089642,3.044323,-9.838872,6.361757,3.112215,5.689365,-1.264807,-7.805298,0.749827,-9.713479,2.478707,3.948709,-4.660498,-0.289709,-8.604730,7.607643,4.000136,-8.225678,3.887333,-9.767270,-7.738176,-8.316605,-9.280797,-2.066238,4.659547,-4.200645,-3.169137,-1.704534,-4.454548,1.505734,-1.088158,2.694932,-7.356526,9.615546,1.486270,-7.511883,-2.795703,-7.035610,9.917505,-1.966660,-3.659020,7.194994,-8.716003,9.527278,9.200475,1.312918,2.305773,0.362222,-1.944804,4.138959,1.873984,5.561560,4.096629,-1.826945,1.196620,8.844531,3.866791,-1.839976,-1.206953,8.137368,-4.701949,0.482547,3.335848,3.064008,-6.770958,2.517290,-4.250566,2.609333,8.295553,7.141678,-0.768411,-1.728372,9.344880,0.334395,-0.288114,7.850634,7.533887,-1.957166,-4.142947,-5.605170,8.238799,-1.405316,0.474199,8.522710,6.572559,8.157810,7.037957,5.341665,-1.033580,-3.133291,6.927633,6.269713,9.310719,7.283533,-3.919139,-8.819228,-4.470170,2.998020,-0.876407,-0.237367,3.736965,0.284186,4.207132,-8.314120,5.533717,-0.881209,-6.706693,0.571239,3.944219,6.684320,-9.014954,5.974334,-9.072437,-7.434459,3.220488,-5.872465,-4.863919,8.484719,3.417466,8.735158,1.785039,4.708101,-3.546078,0.041880,-1.726321,6.430325,-7.793993,6.838937,7.670689,6.743350,-7.921540,-2.167623,6.329340,-6.287619,5.758146,4.089434,0.390467,-4.608359,7.003103,5.456957,4.938236,-2.966560,-6.118438,-8.372415,-2.315790,-2.874655,-6.542582,8.655785,2.241464,-8.092483,-7.739558,6.892342,-7.506887,6.239945,5.345830,0.477770,8.655100,-5.840354,5.541388,8.095464,-9.133690,-8.235881,-0.210871,-4.693947,5.861597,-4.052345,-5.631302,7.920856,-4.186214,-5.774354,-3.276386,-9.611365,4.387586,6.888506,3.689561,-5.294030,-7.830731,-2.918131,0.853702,-6.183604,7.003610,-0.333554,-1.459440,9.833844,-4.259249,-3.544041,0.326729,-3.496517,1.703841,-1.031413,-7.511061,-1.744007,0.498033,-4.651760,1.566710,-3.583602,0.940781,-3.162508,-0.997518,-9.760655,6.718351,3.153117,8.707082,-4.636981,5.368977,-5.405716,0.199471,8.566364,5.587848,3.643087,-4.056173,-1.940444,-2.522481,-0.926441,-0.773291,2.988678,6.366896,-5.011689,-8.405697,-6.691626,9.125509,-4.619190,8.135578,-5.865748,0.065738,-4.065287,9.255290,0.687615,1.382622,-2.863937,1.886409,-5.118102,3.502355,1.231200,7.395104,7.537750,-0.917428,2.458549,6.701308,7.776961,-8.615512,8.914795,-5.815509,9.835884,-2.729255,1.536777,-6.465431,-9.894834,-0.600047,2.758923,9.864715,0.950354,-9.434637,-5.373681,-4.671218,-1.431272,9.595415,-6.610153,3.562179,1.506279,1.775224,8.655965,-0.019564,8.612605,5.758522,-2.051129,-1.662959,2.586885,6.855220,-5.726835,9.208624,-5.803153,-2.419976,-7.191629,-6.824475,3.675328,-5.693896,2.092428,8.251699,0.957330,-3.360592,9.145535,1.795204,0.917833,-7.173960,-8.520436,6.668875,-5.184947,8.790611,0.168734,7.627390,-6.278924,2.928979,-7.969150,-4.124054,6.989329,-0.300002,1.979432,6.086379,-1.410562,7.460014,6.959768,3.353808,-7.701059,-6.516630,-7.800647,6.017622,7.309589,8.408479,6.832834,-2.089331,-7.870844,1.672377,-9.067583,-2.601232,3.757150,-0.936843,-5.610396,-2.408926,-4.617015,-3.465663,-0.121484,0.645957,-7.281426,-6.216694,3.762571,7.018989,9.302532,6.774285,9.990202,-7.271763,6.742163,-4.756289,-1.575292,8.426118,8.093726,3.952117,7.578118,-3.090851,8.245610,6.277281,1.978275,-2.545815,4.548056,-7.302137,-1.894183,8.488366,5.057435,0.682267,1.320632,5.234221,2.703192,-7.381822,2.884571,-9.216007,0.351323,8.687132,-9.112559,4.114460,-8.888092,7.025884,-1.221319,-9.623341,-6.825288,2.072028,-2.615416,-5.800841,-3.617849,-4.875711,2.932632,-1.872658,-1.645117,9.647282,-2.808783,7.502210,4.230870,8.217572,5.214356,4.253239,4.370001,7.703614,9.879593,6.207375,4.521298,-2.076934,0.667033,0.671938,-8.907417,-2.075738,-6.506886,5.138479,-3.872456,3.138127,2.361698,9.442920,-6.835487,-6.745633,5.925113,9.491544,-3.313428,3.411763,-6.859475,9.339252,-9.163670,4.294766,5.581505,-4.230273,8.577977,-8.949083,-4.105182,-0.362295,-2.147141,0.580071,-0.832207,-6.182493,-1.816470,-5.282081,5.958283,7.899816,-4.030512,-9.257587,-9.555444,3.312732,-8.205287,-3.769881,-6.672954,9.647215,4.751488,-0.525618,7.544736,-1.328635,-7.594995,1.196633,9.972908,2.168333,6.207918,3.111701,-1.919467,-9.461120,-1.457862,-9.614388,9.898765,-2.446438,-6.113127,-0.387603,0.773146,0.830178,-7.944918,9.704704,8.083209,2.278649,-2.028338,-3.789450,5.865668,-7.276646,7.632222,-7.532129,-0.931959,-8.018208,0.607679,0.973860,0.044957,9.171233,4.639743,6.493248,2.427033,5.252504,-5.722723], dtype = "float32")#candidate|21198|(585,)|const|float32
const_21199 = relay.const([[-6.187232,-5.111824,-2.198122,4.795033,-5.439108,9.367143,4.891523,6.456979,7.739984,6.476629,5.227749,5.346814,2.909160,5.646117,-2.038676,1.877389,3.189369,5.281881,-4.355612,7.762460,7.244350,1.003044,6.299228,7.600800,2.387402,-6.278535,-4.938639,-0.512683,-4.613994,0.264979,9.848988,3.219567,3.339228,-3.096893,8.979009,-9.979024,-8.295406,5.285389,-6.258312,2.069837,6.022317,-6.027470,3.269118,7.652805,-7.115870,-8.302122,-9.066248,-7.782815,-7.285634,9.982867,9.647134,6.637192,8.052406,3.594561,9.895509,-2.116831,-0.111155,-9.617142,1.103859,8.893335,7.569764,3.388772,0.376215,4.761136,2.028021,3.638586,-0.051369,-9.949561,2.761001,2.604522,-0.854189,-2.743435,-6.251330,-0.065438,-6.836087,2.998521,3.533374,0.053103,3.657798,6.445124,-6.443584,9.613315,7.041745,-0.206031,6.205058,5.848374,4.267944,9.996183,2.306304,-9.587004,0.802378,4.096581,-4.275172,-0.861258,0.890280,-8.526939,-3.633845,-6.673789,-4.497877,9.338849,-5.452913,3.736017,-6.198424,1.395819,8.910330,5.012534,7.710790,6.734760,-5.823550,4.496141,7.782468,3.391556,8.160034,1.308557,-4.999153,-5.996031,-2.957949,7.333339,-5.361095,-3.385000,-3.631664,-0.148228,-7.246884,0.999536,3.959520,-8.850517,4.839507,8.231193,9.139189,-0.136748,7.248387,-0.810602,-9.059289,-3.816278,-8.758057,-0.645696,-6.952425,-5.648986,3.689620,5.850777,0.170269,0.233471,8.516422,0.519057,-6.264881,7.364739,-3.053864,6.300610,8.646048,0.393883,-2.780035,-5.114730,8.251816,8.634175,-1.394108,0.757503,-8.748963,-2.280202,5.414188,-4.822818,2.770154,1.354899,2.555307,9.604925,-1.084501,-1.286997,-7.083663,-0.882885,1.205816,-4.231539,-8.494280,1.721753,3.351455,1.815279,-0.133251,-4.393021,9.370079,1.330276,-8.664463,7.910056,-7.324109,6.372222,-6.656740,-4.786556,2.496101,9.757579,-9.939052,-1.190433,5.578056,9.600884,4.283783,4.012204,3.789320,6.769138,7.914371,1.069607,-3.750626,8.990126,-3.239765,-8.713701,-9.350762,9.668396,9.465678,-8.370418,0.399709,-7.649208,5.892080,3.970868,-3.686573,-1.770679,3.876792,0.700578,-7.884395,-9.488565,-4.294794,-8.051070,2.984685,-9.964085,0.877082,1.075873,-4.479299,1.036119,3.332568,-1.133689,6.409554,-8.029050,-9.784190,-5.147232,-9.216085,5.052470,-6.389815,2.654349,-2.221368,-0.772465,4.567954,-5.592759,1.619505,6.036301,9.598382,-4.003930,4.859700,2.487897,6.237546,-2.965653,3.161498,-1.158673,-5.308810,5.176237,3.108756,-1.558966]], dtype = "float64")#candidate|21199|(1, 250)|const|float64
call_21196 = relay.TupleGetItem(func_16423_call(relay.reshape(const_21197.astype('int8'), [270,]), relay.reshape(const_21198.astype('float32'), [195, 3]), relay.reshape(const_21199.astype('float64'), [250,]), ), 6)
call_21200 = relay.TupleGetItem(func_16428_call(relay.reshape(const_21197.astype('int8'), [270,]), relay.reshape(const_21198.astype('float32'), [195, 3]), relay.reshape(const_21199.astype('float64'), [250,]), ), 6)
var_21201 = relay.var("var_21201", dtype = "float64", shape = (5, 250))#candidate|21201|(5, 250)|var|float64
bop_21202 = relay.divide(const_21199.astype('float32'), var_21201.astype('float32')) # shape=(5, 250)
output = relay.Tuple([bop_21186,call_21190,call_21196,const_21197,const_21198,bop_21202,])
output2 = relay.Tuple([bop_21189,call_21191,call_21200,const_21197,const_21198,bop_21202,])
func_21206 = relay.Function([var_21185,var_21201,], output)
mod['func_21206'] = func_21206
mod = relay.transform.InferType()(mod)
mutated_mod['func_21206'] = func_21206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21206_call = mutated_mod.get_global_var('func_21206')
var_21208 = relay.var("var_21208", dtype = "float64", shape = (10, 14, 4))#candidate|21208|(10, 14, 4)|var|float64
var_21209 = relay.var("var_21209", dtype = "float64", shape = (5, 250))#candidate|21209|(5, 250)|var|float64
call_21207 = func_21206_call(var_21208,var_21209,)
output = call_21207
func_21210 = relay.Function([var_21208,var_21209,], output)
mutated_mod['func_21210'] = func_21210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15823_call = mod.get_global_var('func_15823')
func_15825_call = mutated_mod.get_global_var('func_15825')
call_21284 = func_15823_call()
call_21285 = func_15823_call()
output = call_21284
output2 = call_21285
func_21323 = relay.Function([], output)
mod['func_21323'] = func_21323
mod = relay.transform.InferType()(mod)
mutated_mod['func_21323'] = func_21323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_21323_call = mutated_mod.get_global_var('func_21323')
call_21324 = func_21323_call()
output = call_21324
func_21325 = relay.Function([], output)
mutated_mod['func_21325'] = func_21325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18087_call = mod.get_global_var('func_18087')
func_18089_call = mutated_mod.get_global_var('func_18089')
call_21331 = func_18087_call()
call_21332 = func_18087_call()
output = relay.Tuple([call_21331,])
output2 = relay.Tuple([call_21332,])
func_21340 = relay.Function([], output)
mod['func_21340'] = func_21340
mod = relay.transform.InferType()(mod)
output = func_21340()
func_21341 = relay.Function([], output)
mutated_mod['func_21341'] = func_21341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11872_call = mod.get_global_var('func_11872')
func_11873_call = mutated_mod.get_global_var('func_11873')
call_21377 = relay.TupleGetItem(func_11872_call(), 1)
call_21378 = relay.TupleGetItem(func_11873_call(), 1)
output = call_21377
output2 = call_21378
func_21379 = relay.Function([], output)
mod['func_21379'] = func_21379
mod = relay.transform.InferType()(mod)
output = func_21379()
func_21380 = relay.Function([], output)
mutated_mod['func_21380'] = func_21380
mutated_mod = relay.transform.InferType()(mutated_mod)
var_21468 = relay.var("var_21468", dtype = "bool", shape = (7, 8, 7))#candidate|21468|(7, 8, 7)|var|bool
const_21469 = relay.const([[[False,False,True,True,False,False,True],[False,True,True,True,True,True,True],[False,False,True,False,True,False,True],[False,True,True,True,True,True,False],[True,False,False,False,False,True,True],[False,True,True,True,False,False,False],[False,True,False,False,False,True,True],[True,False,False,True,True,True,False]],[[False,False,False,False,True,True,False],[True,False,True,False,False,False,True],[False,False,True,False,False,True,True],[False,True,False,True,True,False,False],[False,False,False,True,False,False,True],[True,True,True,True,False,False,True],[False,True,False,False,True,True,True],[True,True,False,True,False,False,False]],[[True,False,False,True,False,False,False],[True,True,True,False,False,False,True],[False,True,False,False,False,False,True],[True,False,False,True,True,False,False],[True,False,True,False,False,True,True],[True,False,False,False,True,True,False],[True,False,False,False,True,False,False],[True,True,True,False,True,True,True]],[[False,True,False,True,True,True,True],[False,False,False,True,False,False,True],[True,False,True,True,False,True,True],[True,False,True,False,True,True,False],[False,False,False,False,False,False,True],[True,True,False,True,True,False,False],[False,True,True,True,True,True,False],[True,False,True,False,False,True,False]],[[True,False,False,True,False,False,True],[False,False,False,False,True,False,True],[True,True,False,True,False,True,False],[True,False,True,False,True,False,False],[True,True,False,True,True,False,False],[False,True,False,False,True,False,False],[True,True,False,False,False,False,True],[False,True,True,True,False,False,True]],[[True,True,True,False,False,True,True],[False,True,False,False,False,False,False],[False,False,True,True,True,True,True],[True,True,False,True,False,True,False],[False,False,True,True,True,False,False],[True,True,True,True,True,True,True],[True,True,False,True,False,True,False],[True,False,True,True,True,True,False]],[[True,True,True,False,True,False,True],[False,True,True,True,False,True,True],[True,False,False,True,False,False,False],[False,True,True,True,True,False,False],[False,False,True,False,True,False,False],[False,False,True,False,True,True,True],[False,False,False,True,False,True,False],[False,True,True,False,True,False,False]]], dtype = "bool")#candidate|21469|(7, 8, 7)|const|bool
bop_21470 = relay.logical_and(var_21468.astype('bool'), relay.reshape(const_21469.astype('bool'), relay.shape_of(var_21468))) # shape=(7, 8, 7)
output = bop_21470
output2 = bop_21470
F = relay.Function([var_21468,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_21468,], output2)
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
