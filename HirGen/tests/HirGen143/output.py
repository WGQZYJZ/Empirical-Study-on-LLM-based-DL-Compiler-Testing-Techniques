import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_29 = relay.var("var_29", dtype = "int64", shape = ())#candidate|29|()|var|int64
var_30 = relay.var("var_30", dtype = "int64", shape = (1, 7, 16))#candidate|30|(1, 7, 16)|var|int64
bop_31 = relay.less(var_29.astype('bool'), var_30.astype('bool')) # shape=(1, 7, 16)
output = relay.Tuple([bop_31,])
output2 = relay.Tuple([bop_31,])
func_43 = relay.Function([var_29,var_30,], output)
mod['func_43'] = func_43
mod = relay.transform.InferType()(mod)
var_44 = relay.var("var_44", dtype = "int64", shape = ())#candidate|44|()|var|int64
var_45 = relay.var("var_45", dtype = "int64", shape = (1, 7, 16))#candidate|45|(1, 7, 16)|var|int64
output = func_43(var_44,var_45,)
func_46 = relay.Function([var_44,var_45,], output)
mutated_mod['func_46'] = func_46
mutated_mod = relay.transform.InferType()(mutated_mod)
var_221 = relay.var("var_221", dtype = "float32", shape = (15, 9, 15))#candidate|221|(15, 9, 15)|var|float32
uop_222 = relay.asinh(var_221.astype('float32')) # shape=(15, 9, 15)
func_43_call = mod.get_global_var('func_43')
func_46_call = mutated_mod.get_global_var('func_46')
var_225 = relay.var("var_225", dtype = "int64", shape = ())#candidate|225|()|var|int64
var_226 = relay.var("var_226", dtype = "int64", shape = (112,))#candidate|226|(112,)|var|int64
call_224 = relay.TupleGetItem(func_43_call(relay.reshape(var_225.astype('int64'), []), relay.reshape(var_226.astype('int64'), [1, 7, 16]), ), 0)
call_227 = relay.TupleGetItem(func_46_call(relay.reshape(var_225.astype('int64'), []), relay.reshape(var_226.astype('int64'), [1, 7, 16]), ), 0)
bop_236 = relay.divide(uop_222.astype('float32'), var_225.astype('float32')) # shape=(15, 9, 15)
output = relay.Tuple([call_224,var_226,bop_236,])
output2 = relay.Tuple([call_227,var_226,bop_236,])
func_243 = relay.Function([var_221,var_225,var_226,], output)
mod['func_243'] = func_243
mod = relay.transform.InferType()(mod)
mutated_mod['func_243'] = func_243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_243_call = mutated_mod.get_global_var('func_243')
var_245 = relay.var("var_245", dtype = "float32", shape = (15, 9, 15))#candidate|245|(15, 9, 15)|var|float32
var_246 = relay.var("var_246", dtype = "int64", shape = ())#candidate|246|()|var|int64
var_247 = relay.var("var_247", dtype = "int64", shape = (112,))#candidate|247|(112,)|var|int64
call_244 = func_243_call(var_245,var_246,var_247,)
output = call_244
func_248 = relay.Function([var_245,var_246,var_247,], output)
mutated_mod['func_248'] = func_248
mutated_mod = relay.transform.InferType()(mutated_mod)
const_365 = relay.const([[[-3.882572,2.296712,-9.212887,1.623628,8.707779,-4.422101,8.422469,4.051565,-9.293443,-8.653972,-8.249134,9.806105,7.379793,8.860100,-6.805512],[2.390624,2.824619,2.522471,8.278379,-3.134089,9.279443,0.399018,2.108535,-8.031601,7.757523,4.578913,-1.982702,8.531156,2.580253,-6.479815],[3.404707,8.510817,1.822041,-5.759079,6.586699,5.602560,3.752021,4.598682,2.135956,0.506230,1.476484,-8.219129,5.896719,4.837918,-6.694690],[3.630066,9.386982,-8.332636,5.822881,1.384375,-8.072132,7.729772,2.191913,-1.141335,-7.106605,1.938586,9.141165,2.134033,0.776632,6.973906],[0.997862,-9.999533,0.112892,4.754752,1.948311,2.117726,1.077504,-3.451237,-9.056722,0.181571,-7.967709,-4.537542,-3.123733,-1.639059,-0.078967]],[[2.755897,-5.019117,-2.219262,6.575675,-1.041202,-3.710234,-0.032289,-4.829679,6.453315,6.436856,-5.141394,9.368405,4.211638,-9.397711,-6.418185],[-3.112209,-3.044566,1.296878,-7.248332,-6.564513,4.988598,1.663444,-5.849575,-6.636313,-7.166381,-1.151449,6.861380,9.478011,7.805938,6.055716],[-2.715598,-2.101958,-4.897748,3.612442,-7.866281,-9.666066,-4.157006,2.673093,9.685554,-7.485096,6.210340,-6.891961,1.549476,-3.881571,-7.195612],[-7.877224,6.074744,4.591851,-5.225660,-3.518502,9.796304,-0.331529,-0.130873,-0.866316,-7.086783,1.138960,-7.639951,-0.730051,2.920497,-0.440848],[-9.865033,-3.865076,9.595381,-3.693055,-8.599806,-5.451473,6.178588,-0.396665,-4.693064,5.618701,9.871898,3.658280,9.729839,4.549693,-7.377444]],[[-1.725869,-3.067293,-9.273375,-2.231322,9.458755,0.410874,-5.620683,6.003090,2.903591,-3.910179,-4.207187,6.343383,9.827743,3.330742,-7.217209],[-0.096108,7.737734,0.294655,3.271951,-1.209572,4.927085,-3.247499,-1.957313,-9.351132,-2.899202,-9.585901,-5.026558,-1.030226,-3.682245,7.888474],[3.350729,4.565946,-1.376898,-2.626854,8.273789,3.317776,-4.690843,-9.990280,0.364697,-4.303531,3.625029,-6.650825,4.319381,2.911058,-1.294577],[-7.483000,4.192492,-5.425049,-3.964004,7.174862,8.537663,-6.626129,-4.634227,-3.995017,6.922338,3.329444,-0.996110,2.971148,-4.890428,4.958177],[6.187836,-1.076859,-3.925164,-9.816998,3.319013,-6.272406,-9.174396,9.985706,0.610107,-8.395648,-2.908220,-5.481787,4.585712,-2.852528,-1.494008]]], dtype = "float64")#candidate|365|(3, 5, 15)|const|float64
uop_366 = relay.cosh(const_365.astype('float64')) # shape=(3, 5, 15)
output = relay.Tuple([uop_366,])
output2 = relay.Tuple([uop_366,])
func_378 = relay.Function([], output)
mod['func_378'] = func_378
mod = relay.transform.InferType()(mod)
mutated_mod['func_378'] = func_378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_378_call = mutated_mod.get_global_var('func_378')
call_379 = func_378_call()
output = call_379
func_380 = relay.Function([], output)
mutated_mod['func_380'] = func_380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_396 = relay.TupleGetItem(func_378_call(), 0)
call_397 = relay.TupleGetItem(func_380_call(), 0)
output = call_396
output2 = call_397
func_404 = relay.Function([], output)
mod['func_404'] = func_404
mod = relay.transform.InferType()(mod)
mutated_mod['func_404'] = func_404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_404_call = mutated_mod.get_global_var('func_404')
call_405 = func_404_call()
output = call_405
func_406 = relay.Function([], output)
mutated_mod['func_406'] = func_406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_404_call = mod.get_global_var('func_404')
func_406_call = mutated_mod.get_global_var('func_406')
call_412 = func_404_call()
call_413 = func_404_call()
uop_418 = relay.acosh(call_412.astype('float64')) # shape=(3, 5, 15)
uop_420 = relay.acosh(call_413.astype('float64')) # shape=(3, 5, 15)
output = uop_418
output2 = uop_420
func_425 = relay.Function([], output)
mod['func_425'] = func_425
mod = relay.transform.InferType()(mod)
output = func_425()
func_426 = relay.Function([], output)
mutated_mod['func_426'] = func_426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_438 = relay.TupleGetItem(func_378_call(), 0)
call_439 = relay.TupleGetItem(func_380_call(), 0)
output = call_438
output2 = call_439
func_446 = relay.Function([], output)
mod['func_446'] = func_446
mod = relay.transform.InferType()(mod)
mutated_mod['func_446'] = func_446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_446_call = mutated_mod.get_global_var('func_446')
call_447 = func_446_call()
output = call_447
func_448 = relay.Function([], output)
mutated_mod['func_448'] = func_448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_404_call = mod.get_global_var('func_404')
func_406_call = mutated_mod.get_global_var('func_406')
call_449 = func_404_call()
call_450 = func_404_call()
var_452 = relay.var("var_452", dtype = "float64", shape = (3, 5, 15))#candidate|452|(3, 5, 15)|var|float64
bop_453 = relay.not_equal(call_449.astype('bool'), relay.reshape(var_452.astype('bool'), relay.shape_of(call_449))) # shape=(3, 5, 15)
bop_456 = relay.not_equal(call_450.astype('bool'), relay.reshape(var_452.astype('bool'), relay.shape_of(call_450))) # shape=(3, 5, 15)
bop_460 = relay.floor_divide(bop_453.astype('float32'), relay.reshape(var_452.astype('float32'), relay.shape_of(bop_453))) # shape=(3, 5, 15)
bop_463 = relay.floor_divide(bop_456.astype('float32'), relay.reshape(var_452.astype('float32'), relay.shape_of(bop_456))) # shape=(3, 5, 15)
bop_464 = relay.greater(call_449.astype('bool'), relay.reshape(bop_453.astype('bool'), relay.shape_of(call_449))) # shape=(3, 5, 15)
bop_467 = relay.greater(call_450.astype('bool'), relay.reshape(bop_456.astype('bool'), relay.shape_of(call_450))) # shape=(3, 5, 15)
output = relay.Tuple([bop_460,bop_464,])
output2 = relay.Tuple([bop_463,bop_467,])
func_480 = relay.Function([var_452,], output)
mod['func_480'] = func_480
mod = relay.transform.InferType()(mod)
var_481 = relay.var("var_481", dtype = "float64", shape = (3, 5, 15))#candidate|481|(3, 5, 15)|var|float64
output = func_480(var_481)
func_482 = relay.Function([var_481], output)
mutated_mod['func_482'] = func_482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_493 = relay.var("var_493", dtype = "uint16", shape = (9, 3, 12))#candidate|493|(9, 3, 12)|var|uint16
var_494 = relay.var("var_494", dtype = "uint16", shape = (9, 3, 12))#candidate|494|(9, 3, 12)|var|uint16
bop_495 = relay.subtract(var_493.astype('uint16'), relay.reshape(var_494.astype('uint16'), relay.shape_of(var_493))) # shape=(9, 3, 12)
output = bop_495
output2 = bop_495
func_500 = relay.Function([var_493,var_494,], output)
mod['func_500'] = func_500
mod = relay.transform.InferType()(mod)
mutated_mod['func_500'] = func_500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_500_call = mutated_mod.get_global_var('func_500')
var_502 = relay.var("var_502", dtype = "uint16", shape = (9, 3, 12))#candidate|502|(9, 3, 12)|var|uint16
var_503 = relay.var("var_503", dtype = "uint16", shape = (9, 3, 12))#candidate|503|(9, 3, 12)|var|uint16
call_501 = func_500_call(var_502,var_503,)
output = call_501
func_504 = relay.Function([var_502,var_503,], output)
mutated_mod['func_504'] = func_504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_538 = func_425_call()
call_539 = func_425_call()
uop_540 = relay.rsqrt(call_538.astype('float64')) # shape=(3, 5, 15)
uop_542 = relay.rsqrt(call_539.astype('float64')) # shape=(3, 5, 15)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_544 = relay.TupleGetItem(func_480_call(relay.reshape(call_538.astype('float64'), [3, 5, 15])), 0)
call_545 = relay.TupleGetItem(func_482_call(relay.reshape(call_538.astype('float64'), [3, 5, 15])), 0)
bop_548 = relay.floor_mod(call_538.astype('float64'), relay.reshape(uop_540.astype('float64'), relay.shape_of(call_538))) # shape=(3, 5, 15)
bop_551 = relay.floor_mod(call_539.astype('float64'), relay.reshape(uop_542.astype('float64'), relay.shape_of(call_539))) # shape=(3, 5, 15)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_559 = func_425_call()
call_560 = func_425_call()
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_561 = relay.TupleGetItem(func_480_call(relay.reshape(bop_548.astype('float64'), [3, 5, 15])), 0)
call_562 = relay.TupleGetItem(func_482_call(relay.reshape(bop_548.astype('float64'), [3, 5, 15])), 0)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_564 = relay.TupleGetItem(func_480_call(relay.reshape(call_561.astype('float64'), [3, 5, 15])), 1)
call_565 = relay.TupleGetItem(func_482_call(relay.reshape(call_561.astype('float64'), [3, 5, 15])), 1)
uop_569 = relay.log10(call_538.astype('float64')) # shape=(3, 5, 15)
uop_571 = relay.log10(call_539.astype('float64')) # shape=(3, 5, 15)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_572 = relay.TupleGetItem(func_480_call(relay.reshape(call_544.astype('float64'), [3, 5, 15])), 1)
call_573 = relay.TupleGetItem(func_482_call(relay.reshape(call_544.astype('float64'), [3, 5, 15])), 1)
output = relay.Tuple([call_544,bop_548,call_559,call_561,call_564,uop_569,call_572,])
output2 = relay.Tuple([call_545,bop_551,call_560,call_562,call_565,uop_571,call_573,])
func_580 = relay.Function([], output)
mod['func_580'] = func_580
mod = relay.transform.InferType()(mod)
mutated_mod['func_580'] = func_580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mutated_mod.get_global_var('func_580')
call_581 = func_580_call()
output = call_581
func_582 = relay.Function([], output)
mutated_mod['func_582'] = func_582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_599 = func_446_call()
call_600 = func_446_call()
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
const_605 = relay.const([3,9,-8,-6,6,-5,7,-1,-2,10,-7,8,9,7,10,-3,2,5,-6,10,-7,9,10,5,-10,-5,-1,8,-3,-5,6,5,1,5,-1,9,2,3,1,-6,-5,7,-6,-6,-9,1,1,3,-8,-9,-3,-6,-10,9,-7,2,7,-7,-4,3,4,-1,2,8,10,8,8,2,-2,-9,5,-2,1,-9,-10,10,-6,10,-3,-7,-8,10,-10,-3,-3,-3,4,-3,5,-1,4,-1,-2,-8,1,-2,2,-6,6,5,4,8,-5,2,-4,-7,4,-9,-10,5,-4,-10,-1,-1,6,6,5,-7,-6,-10,-3,7,4,-6,-2,-8,8,-5,6,5,1,3,5,8,-8,4,-5,1,-8,6,9,-8,-1,5,-8,-9,-2,-7,-2,-10,3,-4,-6,10,3,4,9,1,7,-9,-8,6,-3,-9,-7,-7,-5,-9,-7,5,-6,-4,-2,-6,2,-6,4,-10,-4,-1,-2,-3,9,-9,2,8,4,-2,-8,-5,-2,1,-4,2,-2,1,3,-10,-6,1,-3,-8,3,-3,-8,1,1,7,-5,-5,4,-2,2,9,2,-7,-1,2,-5,-6,5,-5,1,6,-3,-4,9,-5,-9,10,-8,-6,4,-4,-5,3,10,-8,2,-9,-5,3,1,6,6,-1,6,3,7,2,6,2,3,-8,-6,-1,10,-6,4,10,9,-4,1,7,-5,-10,4,8,5,-4,1,-3,-1,-3,-10,-7,-6,-6,-10,-7,-3,5,-10,-7,-7,8,-8,10,-10,6,-5,1,-6,10,-3,1,3,-3,1,10,1,-7,-8,8,-1,10,-7,-9,1,1,6,9,-1,2,10,-9,1,10,4,-9,-2,3,1,4], dtype = "uint16")#candidate|605|(324,)|const|uint16
call_604 = func_500_call(relay.reshape(const_605.astype('uint16'), [9, 3, 12]), relay.reshape(const_605.astype('uint16'), [9, 3, 12]), )
call_606 = func_500_call(relay.reshape(const_605.astype('uint16'), [9, 3, 12]), relay.reshape(const_605.astype('uint16'), [9, 3, 12]), )
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_607 = relay.TupleGetItem(func_378_call(), 0)
call_608 = relay.TupleGetItem(func_380_call(), 0)
output = relay.Tuple([call_599,call_604,const_605,call_607,])
output2 = relay.Tuple([call_600,call_606,const_605,call_608,])
func_611 = relay.Function([], output)
mod['func_611'] = func_611
mod = relay.transform.InferType()(mod)
mutated_mod['func_611'] = func_611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mutated_mod.get_global_var('func_611')
call_612 = func_611_call()
output = call_612
func_613 = relay.Function([], output)
mutated_mod['func_613'] = func_613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_646 = func_446_call()
call_647 = func_446_call()
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_657 = relay.TupleGetItem(func_580_call(), 1)
call_658 = relay.TupleGetItem(func_582_call(), 1)
output = relay.Tuple([call_646,call_657,])
output2 = relay.Tuple([call_647,call_658,])
func_674 = relay.Function([], output)
mod['func_674'] = func_674
mod = relay.transform.InferType()(mod)
output = func_674()
func_675 = relay.Function([], output)
mutated_mod['func_675'] = func_675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_682 = relay.TupleGetItem(func_580_call(), 0)
call_683 = relay.TupleGetItem(func_582_call(), 0)
output = relay.Tuple([call_682,])
output2 = relay.Tuple([call_683,])
func_691 = relay.Function([], output)
mod['func_691'] = func_691
mod = relay.transform.InferType()(mod)
output = func_691()
func_692 = relay.Function([], output)
mutated_mod['func_692'] = func_692
mutated_mod = relay.transform.InferType()(mutated_mod)
var_732 = relay.var("var_732", dtype = "float64", shape = (2, 15, 5))#candidate|732|(2, 15, 5)|var|float64
uop_733 = relay.atan(var_732.astype('float64')) # shape=(2, 15, 5)
uop_737 = relay.sin(var_732.astype('float64')) # shape=(2, 15, 5)
output = relay.Tuple([uop_733,uop_737,])
output2 = relay.Tuple([uop_733,uop_737,])
func_742 = relay.Function([var_732,], output)
mod['func_742'] = func_742
mod = relay.transform.InferType()(mod)
var_743 = relay.var("var_743", dtype = "float64", shape = (2, 15, 5))#candidate|743|(2, 15, 5)|var|float64
output = func_742(var_743)
func_744 = relay.Function([var_743], output)
mutated_mod['func_744'] = func_744
mutated_mod = relay.transform.InferType()(mutated_mod)
var_777 = relay.var("var_777", dtype = "int16", shape = ())#candidate|777|()|var|int16
var_778 = relay.var("var_778", dtype = "int16", shape = (10, 10, 6))#candidate|778|(10, 10, 6)|var|int16
bop_779 = relay.bitwise_and(var_777.astype('int16'), var_778.astype('int16')) # shape=(10, 10, 6)
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
const_807 = relay.const([1,-2,4,-9,6,-10,-6,6,1,-9,6,6,9,-1,10,5,-4,4,4,7,-3,-10,7,1,10,1,-5,3,10,-1,3,-4,4,5,1,8,2,-5,4,7,3,-1,4,4,-5,6,2,7,10,-4,7,-7,9,-7,7,6,-3,-10,-10,-3,-1,5,3,-1,-5,3,6,10,-1,10,-3,8,5,5,4,10,-8,-1,8,-5,-9,-6,10,2,-3,9,-1,1,7,-1,3,8,-8,-4,3,1,8,8,-3,7,-7,9,-5,1,-4,5,-6,9,-2,-2,10,8,1,4,-10,-10,-1,-4,9,10,-10,3,6,9,4,-4,5,4,1,9,-3,8,-8,-10,-8,2,-5,-1,8,-10,1,9,-9,-3,-3,2,3,-9,2,10,10,-5,9,-8,8,-9,4,-9,3,3,-4,3,5,-10,3,-7,4,-10,10,7,-5,-10,-4,-2,-1,-4,-10,-4,-9,1,4,5,-10,10,10,-1,-6,4,10,-9,-2,7,8,-8,6,8,-9,-10,5,-10,-7,-2,4,5,3,-6,-4,9,-4,10,-10,2,1,-8,-1,-3,-1,-3,2,-8,1,2,-7,-1,9,1,-2,-9,-6,-9,-7,-9,-9,3,2,6,5,1,8,3,5,-7,6,8,-2,10,3,-8,-4,4,2,9,10,9,2,-5,5,-2,7,6,-8,9,-6,4,5,5,-1,-7,2,9,10,-3,-8,-10,6,6,-2,7,-9,-7,-2,6,-7,-4,-10,5,9,-7,-4,3,10,-7,-4,2,7,2,4,-3,-10,9,10,-2,-5,-7,5,-10,9,9,4,-9,-1,-2,-8,5,4,7,-10,-4,-7,4,10,9,3,-3], dtype = "uint16")#candidate|807|(324,)|const|uint16
call_806 = func_500_call(relay.reshape(const_807.astype('uint16'), [9, 3, 12]), relay.reshape(const_807.astype('uint16'), [9, 3, 12]), )
call_808 = func_500_call(relay.reshape(const_807.astype('uint16'), [9, 3, 12]), relay.reshape(const_807.astype('uint16'), [9, 3, 12]), )
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
call_812 = func_500_call(relay.reshape(const_807.astype('uint16'), [9, 3, 12]), relay.reshape(call_806.astype('uint16'), [9, 3, 12]), )
call_813 = func_500_call(relay.reshape(const_807.astype('uint16'), [9, 3, 12]), relay.reshape(call_806.astype('uint16'), [9, 3, 12]), )
output = relay.Tuple([bop_779,call_806,const_807,call_812,])
output2 = relay.Tuple([bop_779,call_808,const_807,call_813,])
func_820 = relay.Function([var_777,var_778,], output)
mod['func_820'] = func_820
mod = relay.transform.InferType()(mod)
var_821 = relay.var("var_821", dtype = "int16", shape = ())#candidate|821|()|var|int16
var_822 = relay.var("var_822", dtype = "int16", shape = (10, 10, 6))#candidate|822|(10, 10, 6)|var|int16
output = func_820(var_821,var_822,)
func_823 = relay.Function([var_821,var_822,], output)
mutated_mod['func_823'] = func_823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_827 = relay.TupleGetItem(func_611_call(), 0)
call_828 = relay.TupleGetItem(func_613_call(), 0)
output = relay.Tuple([call_827,])
output2 = relay.Tuple([call_828,])
func_830 = relay.Function([], output)
mod['func_830'] = func_830
mod = relay.transform.InferType()(mod)
mutated_mod['func_830'] = func_830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mutated_mod.get_global_var('func_830')
call_831 = func_830_call()
output = call_831
func_832 = relay.Function([], output)
mutated_mod['func_832'] = func_832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_674_call = mod.get_global_var('func_674')
func_675_call = mutated_mod.get_global_var('func_675')
call_864 = relay.TupleGetItem(func_674_call(), 0)
call_865 = relay.TupleGetItem(func_675_call(), 0)
output = relay.Tuple([call_864,])
output2 = relay.Tuple([call_865,])
func_890 = relay.Function([], output)
mod['func_890'] = func_890
mod = relay.transform.InferType()(mod)
output = func_890()
func_891 = relay.Function([], output)
mutated_mod['func_891'] = func_891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mod.get_global_var('func_830')
func_832_call = mutated_mod.get_global_var('func_832')
call_947 = relay.TupleGetItem(func_830_call(), 0)
call_948 = relay.TupleGetItem(func_832_call(), 0)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_953 = relay.TupleGetItem(func_691_call(), 0)
call_954 = relay.TupleGetItem(func_692_call(), 0)
bop_963 = relay.left_shift(call_953.astype('uint32'), relay.reshape(call_947.astype('uint32'), relay.shape_of(call_953))) # shape=(3, 5, 15)
bop_966 = relay.left_shift(call_954.astype('uint32'), relay.reshape(call_948.astype('uint32'), relay.shape_of(call_954))) # shape=(3, 5, 15)
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
var_969 = relay.var("var_969", dtype = "uint16", shape = (324,))#candidate|969|(324,)|var|uint16
call_968 = func_500_call(relay.reshape(var_969.astype('uint16'), [9, 3, 12]), relay.reshape(var_969.astype('uint16'), [9, 3, 12]), )
call_970 = func_500_call(relay.reshape(var_969.astype('uint16'), [9, 3, 12]), relay.reshape(var_969.astype('uint16'), [9, 3, 12]), )
output = relay.Tuple([bop_963,call_968,var_969,])
output2 = relay.Tuple([bop_966,call_970,var_969,])
func_981 = relay.Function([var_969,], output)
mod['func_981'] = func_981
mod = relay.transform.InferType()(mod)
var_982 = relay.var("var_982", dtype = "uint16", shape = (324,))#candidate|982|(324,)|var|uint16
output = func_981(var_982)
func_983 = relay.Function([var_982], output)
mutated_mod['func_983'] = func_983
mutated_mod = relay.transform.InferType()(mutated_mod)
var_985 = relay.var("var_985", dtype = "float64", shape = (8, 4, 1))#candidate|985|(8, 4, 1)|var|float64
uop_986 = relay.tan(var_985.astype('float64')) # shape=(8, 4, 1)
bop_990 = relay.minimum(uop_986.astype('uint16'), relay.reshape(var_985.astype('uint16'), relay.shape_of(uop_986))) # shape=(8, 4, 1)
bop_1001 = relay.bitwise_xor(bop_990.astype('int32'), relay.reshape(var_985.astype('int32'), relay.shape_of(bop_990))) # shape=(8, 4, 1)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_1008 = relay.TupleGetItem(func_691_call(), 0)
call_1009 = relay.TupleGetItem(func_692_call(), 0)
bop_1010 = relay.power(bop_990.astype('float32'), relay.reshape(var_985.astype('float32'), relay.shape_of(bop_990))) # shape=(8, 4, 1)
func_43_call = mod.get_global_var('func_43')
func_46_call = mutated_mod.get_global_var('func_46')
const_1016 = relay.const(-6, dtype = "int64")#candidate|1016|()|const|int64
var_1017 = relay.var("var_1017", dtype = "int64", shape = (4, 28))#candidate|1017|(4, 28)|var|int64
call_1015 = relay.TupleGetItem(func_43_call(relay.reshape(const_1016.astype('int64'), []), relay.reshape(var_1017.astype('int64'), [1, 7, 16]), ), 0)
call_1018 = relay.TupleGetItem(func_46_call(relay.reshape(const_1016.astype('int64'), []), relay.reshape(var_1017.astype('int64'), [1, 7, 16]), ), 0)
output = relay.Tuple([bop_1001,call_1008,bop_1010,call_1015,const_1016,var_1017,])
output2 = relay.Tuple([bop_1001,call_1009,bop_1010,call_1018,const_1016,var_1017,])
func_1022 = relay.Function([var_985,var_1017,], output)
mod['func_1022'] = func_1022
mod = relay.transform.InferType()(mod)
mutated_mod['func_1022'] = func_1022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1022_call = mutated_mod.get_global_var('func_1022')
var_1024 = relay.var("var_1024", dtype = "float64", shape = (8, 4, 1))#candidate|1024|(8, 4, 1)|var|float64
var_1025 = relay.var("var_1025", dtype = "int64", shape = (4, 28))#candidate|1025|(4, 28)|var|int64
call_1023 = func_1022_call(var_1024,var_1025,)
output = call_1023
func_1026 = relay.Function([var_1024,var_1025,], output)
mutated_mod['func_1026'] = func_1026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1043 = relay.var("var_1043", dtype = "float32", shape = (15, 11, 12))#candidate|1043|(15, 11, 12)|var|float32
uop_1044 = relay.sqrt(var_1043.astype('float32')) # shape=(15, 11, 12)
var_1046 = relay.var("var_1046", dtype = "float32", shape = (15, 11, 12))#candidate|1046|(15, 11, 12)|var|float32
bop_1047 = relay.left_shift(uop_1044.astype('int64'), relay.reshape(var_1046.astype('int64'), relay.shape_of(uop_1044))) # shape=(15, 11, 12)
output = bop_1047
output2 = bop_1047
func_1055 = relay.Function([var_1043,var_1046,], output)
mod['func_1055'] = func_1055
mod = relay.transform.InferType()(mod)
var_1056 = relay.var("var_1056", dtype = "float32", shape = (15, 11, 12))#candidate|1056|(15, 11, 12)|var|float32
var_1057 = relay.var("var_1057", dtype = "float32", shape = (15, 11, 12))#candidate|1057|(15, 11, 12)|var|float32
output = func_1055(var_1056,var_1057,)
func_1058 = relay.Function([var_1056,var_1057,], output)
mutated_mod['func_1058'] = func_1058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_1070 = relay.TupleGetItem(func_378_call(), 0)
call_1071 = relay.TupleGetItem(func_380_call(), 0)
var_1086 = relay.var("var_1086", dtype = "float64", shape = (3, 5, 15))#candidate|1086|(3, 5, 15)|var|float64
bop_1087 = relay.bitwise_or(call_1070.astype('int64'), relay.reshape(var_1086.astype('int64'), relay.shape_of(call_1070))) # shape=(3, 5, 15)
bop_1090 = relay.bitwise_or(call_1071.astype('int64'), relay.reshape(var_1086.astype('int64'), relay.shape_of(call_1071))) # shape=(3, 5, 15)
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
var_1097 = relay.var("var_1097", dtype = "uint16", shape = (9, 36))#candidate|1097|(9, 36)|var|uint16
call_1096 = func_500_call(relay.reshape(var_1097.astype('uint16'), [9, 3, 12]), relay.reshape(var_1097.astype('uint16'), [9, 3, 12]), )
call_1098 = func_500_call(relay.reshape(var_1097.astype('uint16'), [9, 3, 12]), relay.reshape(var_1097.astype('uint16'), [9, 3, 12]), )
var_1099 = relay.var("var_1099", dtype = "uint16", shape = (9, 36))#candidate|1099|(9, 36)|var|uint16
bop_1100 = relay.mod(var_1097.astype('float32'), relay.reshape(var_1099.astype('float32'), relay.shape_of(var_1097))) # shape=(9, 36)
var_1105 = relay.var("var_1105", dtype = "uint16", shape = (9, 3, 12))#candidate|1105|(9, 3, 12)|var|uint16
bop_1106 = relay.less_equal(call_1096.astype('bool'), relay.reshape(var_1105.astype('bool'), relay.shape_of(call_1096))) # shape=(9, 3, 12)
bop_1109 = relay.less_equal(call_1098.astype('bool'), relay.reshape(var_1105.astype('bool'), relay.shape_of(call_1098))) # shape=(9, 3, 12)
output = relay.Tuple([bop_1087,bop_1100,bop_1106,])
output2 = relay.Tuple([bop_1090,bop_1100,bop_1109,])
func_1111 = relay.Function([var_1086,var_1097,var_1099,var_1105,], output)
mod['func_1111'] = func_1111
mod = relay.transform.InferType()(mod)
mutated_mod['func_1111'] = func_1111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1111_call = mutated_mod.get_global_var('func_1111')
var_1113 = relay.var("var_1113", dtype = "float64", shape = (3, 5, 15))#candidate|1113|(3, 5, 15)|var|float64
var_1114 = relay.var("var_1114", dtype = "uint16", shape = (9, 36))#candidate|1114|(9, 36)|var|uint16
var_1115 = relay.var("var_1115", dtype = "uint16", shape = (9, 36))#candidate|1115|(9, 36)|var|uint16
var_1116 = relay.var("var_1116", dtype = "uint16", shape = (9, 3, 12))#candidate|1116|(9, 3, 12)|var|uint16
call_1112 = func_1111_call(var_1113,var_1114,var_1115,var_1116,)
output = call_1112
func_1117 = relay.Function([var_1113,var_1114,var_1115,var_1116,], output)
mutated_mod['func_1117'] = func_1117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_1164 = relay.TupleGetItem(func_691_call(), 0)
call_1165 = relay.TupleGetItem(func_692_call(), 0)
output = call_1164
output2 = call_1165
func_1171 = relay.Function([], output)
mod['func_1171'] = func_1171
mod = relay.transform.InferType()(mod)
output = func_1171()
func_1172 = relay.Function([], output)
mutated_mod['func_1172'] = func_1172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1179 = relay.var("var_1179", dtype = "float64", shape = (14, 6, 13))#candidate|1179|(14, 6, 13)|var|float64
var_1180 = relay.var("var_1180", dtype = "float64", shape = (14, 6, 13))#candidate|1180|(14, 6, 13)|var|float64
bop_1181 = relay.floor_divide(var_1179.astype('float64'), relay.reshape(var_1180.astype('float64'), relay.shape_of(var_1179))) # shape=(14, 6, 13)
const_1194 = relay.const([[[3.159897,-5.123584,-0.442701,-4.940667,0.194867,-6.435589,6.428452,-9.145157,-9.760416,7.273190,7.455709,1.020346,8.343389],[-2.350447,7.326364,1.149570,0.406959,-8.536995,1.028813,-0.578369,-0.529368,-0.937037,-4.354527,-8.232443,4.083619,2.807675],[-7.309844,4.749600,8.362379,-2.599394,5.266159,7.965259,7.873074,-3.683998,-3.527210,6.534947,7.205175,-0.696625,5.492412],[9.805458,-3.435672,5.030145,0.354256,7.676554,-6.741535,8.301564,0.329827,2.904290,7.415522,7.951034,-9.093735,-7.013277],[2.158150,8.652113,-4.244129,0.228642,8.106483,6.584149,2.494334,7.015687,-5.888051,0.599569,6.533089,3.627133,-8.892134],[-8.574718,3.269502,7.253363,7.303075,7.087148,2.886763,7.314290,2.153713,9.931982,6.709182,8.431783,0.117389,0.298347]],[[0.345192,6.098868,5.578524,-7.095045,3.198081,5.140697,-6.606344,-7.501877,-5.459555,-4.510317,-9.556340,-4.374734,9.708310],[8.416816,1.373988,3.082356,7.855973,-5.287677,5.192070,-4.941807,-8.123549,2.204679,-7.254368,-7.730250,1.358167,4.028817],[-1.215791,1.930307,2.213268,7.313407,0.613892,6.897853,0.770299,-0.486130,-4.372372,0.495243,-2.591840,1.034969,-8.585709],[7.975551,-5.316321,8.571403,4.622290,-0.819718,-8.423515,4.396298,9.841618,-2.838489,-7.532368,3.474348,4.317433,-4.141786],[0.780463,6.801603,1.638746,-7.690022,7.266444,8.600676,-9.416920,5.677839,5.460518,6.925866,4.168142,9.654063,-0.845940],[-9.589218,-4.947752,5.214918,-2.574529,2.020902,-9.649998,8.670631,-0.405140,-5.449937,4.114051,2.961191,-2.094393,1.138821]],[[-3.248936,0.851353,6.208381,0.568407,-1.837365,7.351731,8.983286,1.113961,-2.637123,2.147478,6.884601,-3.114454,9.802513],[8.460804,-0.012342,0.021274,4.429272,8.877857,-2.069661,-5.093053,4.038874,7.029707,7.854305,-4.670012,3.978700,-8.395122],[2.356293,5.255629,-3.062525,-7.672486,2.957633,2.303474,5.649385,8.650149,1.089486,-6.728574,-0.508139,9.521619,-3.087407],[1.154395,7.518700,-6.063761,-6.366452,7.982552,-4.764969,8.663027,0.987100,5.151666,2.135074,-3.459430,-8.285033,-9.057915],[-5.362379,-4.871699,0.806944,9.151891,0.845085,-0.348371,6.862619,-8.018792,7.205861,-4.719540,5.477561,6.582441,-1.930572],[1.428360,9.455196,0.385149,-0.722325,-7.835242,-0.737446,-7.581306,-1.514591,9.647594,3.997206,2.782669,-0.030292,7.101836]],[[1.958582,-9.749960,6.001535,0.847252,8.012257,-4.160365,-9.573384,-1.659299,-9.411513,7.534368,6.709153,2.979536,-5.882379],[0.008742,-7.620395,-1.564977,-5.958753,5.210997,4.340453,-5.157294,-0.810322,-8.552380,7.863671,3.414716,2.288485,-5.863708],[0.113079,7.202401,8.641346,-2.832485,-2.430780,9.352946,-1.147829,-4.349485,9.951212,-7.542170,9.600057,7.069237,7.191290],[9.936053,2.400498,4.433600,0.735946,-2.851317,-6.314028,-2.330673,-4.110635,2.146167,-2.556382,-6.231282,-7.949993,8.232751],[3.215114,-5.596279,8.665669,6.077751,-2.294093,-1.609148,-7.433693,-5.286865,9.713497,7.564048,-8.969631,-8.938760,-2.790992],[8.682567,-2.606333,-1.056613,2.832799,-3.001996,-9.576344,1.518121,1.409114,-9.910503,-5.772368,-0.633991,2.154837,0.476100]],[[-9.399543,5.485407,-5.984625,8.363803,0.577062,-6.937297,-3.903569,-7.762040,0.017471,5.379793,4.512009,-2.572949,-0.678352],[1.430909,-7.883334,-9.949599,5.923476,6.036712,-6.743974,-5.774212,-9.882801,-6.731510,7.414257,-9.668326,-8.959778,8.991049],[4.393928,1.341833,-5.300374,-2.653144,-6.159731,3.428742,-9.148535,8.424767,4.049911,-0.637237,1.428087,9.931586,1.145913],[0.885303,2.520721,9.303895,-9.546090,5.552222,-1.076267,9.624798,-3.633761,-1.196324,7.719383,9.749985,7.182593,-8.983284],[-2.590665,6.813839,5.336737,4.427398,-0.855351,-0.643673,1.601374,7.572948,2.687565,-1.063697,-9.126765,-8.832580,2.670592],[-5.447566,2.003715,2.664670,-2.827019,-7.711797,3.751599,9.674953,-3.487450,-7.772951,1.106685,0.321733,-8.213798,-4.296592]],[[-9.739790,-2.179414,-4.570556,-0.710304,9.109869,4.167688,3.259512,-5.019604,2.442880,-6.243174,1.245131,6.349382,-1.925858],[0.911674,2.951368,5.617408,-8.168698,7.231358,6.595335,-1.525748,5.294473,-5.387199,2.547978,6.644399,-5.348248,7.772703],[-0.900346,-1.771469,3.886663,6.205539,7.646712,5.199869,-9.382108,-5.021749,-3.779736,-4.590265,-5.729095,-0.839257,6.358628],[-7.835772,0.091036,6.206783,7.341433,0.760347,2.005547,3.877094,9.384440,-1.803084,0.631181,9.871459,-5.132459,3.249981],[9.236854,-3.644444,6.643424,-6.467922,-6.014839,-8.814211,-5.891538,0.761767,-2.956617,-5.690972,0.399718,9.599015,-3.333844],[-4.579160,-7.809605,3.935082,-8.761672,6.687942,5.618881,-3.968537,6.865984,1.000215,-0.660021,-2.775282,2.493606,0.188111]],[[7.352408,5.781679,1.100918,-3.795488,8.863050,6.421775,-4.950153,0.140304,2.979575,4.937946,-9.402569,-3.946306,6.669837],[4.363109,7.580803,1.527926,8.515058,-4.930468,2.375276,-2.151011,7.717353,-4.048785,-6.244811,2.625531,3.449407,9.113006],[3.831944,4.678180,-2.506760,7.817790,2.362691,-4.197073,3.564461,4.919907,-0.426076,1.917659,-2.551386,3.282258,2.243029],[-5.312373,0.870253,-0.773911,7.003632,-3.110834,-5.068999,7.801420,-9.674830,-2.646129,7.848524,-6.164578,5.340440,6.609845],[5.041737,6.478599,6.590065,-5.239278,0.699226,0.383003,-7.009857,-3.873907,5.030815,-8.495389,9.030716,5.614521,-8.278071],[-5.248145,7.454425,1.496509,-2.537163,6.463478,-9.832087,1.951181,-5.277321,-3.301862,-5.807694,5.243058,8.148310,5.011696]],[[-8.935294,0.030340,7.029233,-4.040728,0.708390,3.189815,-1.459351,8.042690,-5.179603,-9.568686,5.740010,8.267012,4.404568],[0.796422,-1.758159,-1.023270,0.082965,-9.635232,7.969525,6.731093,-6.759190,9.659374,3.625508,-0.253868,6.315635,-9.846728],[7.542134,-2.166965,-1.310917,3.493220,-5.268849,4.349783,7.568963,-2.949520,-8.156811,2.262350,1.135197,-4.667509,4.497048],[-4.767319,9.922014,5.518929,7.974523,-0.980517,0.203205,-4.239715,0.746854,1.265855,5.224354,9.018516,9.750609,2.391113],[7.932761,7.612663,-6.763517,2.702955,-7.953214,-8.370794,-0.955579,0.499865,2.097332,-1.215114,7.952415,6.490913,2.494864],[5.234704,-3.496356,0.660330,-8.537589,-3.724292,3.751417,-1.979312,0.164199,6.284248,8.858607,6.002555,-6.217791,4.049000]],[[-5.920831,8.547114,-6.392697,-9.002154,9.780633,-6.950319,1.540225,-6.253798,5.868237,-1.245914,4.839171,-9.882100,3.285463],[6.606005,9.320021,0.326002,-7.087145,-3.612503,6.163650,6.856875,-7.092008,-6.281192,-4.964946,-1.027208,-5.217199,-0.014254],[-2.283049,-6.583999,4.312702,-5.520158,3.562562,-0.462960,-5.250398,-5.343002,7.162208,-1.137451,4.822239,1.391965,1.659768],[8.674816,1.015049,7.066817,6.180081,2.694522,-6.739504,1.117630,5.246486,3.305118,-9.366491,-5.827215,4.027165,-3.956198],[3.279588,-1.559920,0.991375,-8.260095,-7.169141,8.396395,-3.117016,-4.248875,-3.371616,-0.362219,7.519921,0.034877,3.329740],[8.155754,-2.215871,2.189615,-1.231791,-2.638070,-4.297249,-5.897559,-3.615530,-4.217685,-4.889143,6.951355,-3.243342,-1.208768]],[[3.541284,-1.487811,5.070025,2.138778,0.927448,-2.464696,0.472098,7.952292,7.266367,-9.054082,4.732101,-5.282470,0.525867],[-7.845069,9.134037,5.473948,-3.845691,6.619266,2.928224,1.832737,-1.689393,-7.660578,-5.918955,7.720632,3.950103,-0.787009],[-4.278370,-0.357382,-5.935540,1.232633,-3.480390,9.834190,-4.384030,-8.700401,8.688509,-7.478591,1.021930,6.169825,9.129092],[-8.301292,-5.690484,9.616369,1.119657,-9.772643,3.044424,-5.801991,-4.148519,-9.347748,-1.062310,8.511518,2.949454,5.315654],[-7.631130,-3.837050,9.479919,6.389107,4.927584,-5.376131,-2.521723,9.132895,0.317558,1.875255,8.829918,-7.898935,5.273682],[6.982082,-7.118458,4.323039,-7.333665,-4.772531,-9.530123,9.119306,-9.241310,4.059770,2.984298,-9.633273,-6.784101,-8.579510]],[[-9.239362,3.976433,-8.070928,-1.457770,-9.070134,-4.561555,9.975119,-4.081555,-0.809353,-6.036897,-0.009342,2.792132,-5.692025],[-7.793438,-2.917446,-7.346600,9.930294,-3.064678,-2.860965,-7.072551,-9.662971,9.995575,1.088549,-0.015157,-1.128371,6.515254],[-7.763117,-7.698604,-7.924281,9.662337,1.096932,4.830672,0.988710,4.644009,-8.158747,-2.081697,-4.525871,9.779949,-7.098389],[3.935521,-3.526326,4.957048,2.082635,1.884884,-1.657675,-3.248880,-1.109558,-4.072748,4.990044,2.016124,-6.706897,1.467905],[-0.484425,-2.794576,-8.311719,9.826542,-6.848039,9.829718,-2.593072,-9.615442,3.403048,-9.844789,-3.920150,2.635511,-8.831760],[-1.959397,6.825536,2.498850,-6.232254,-2.359785,5.322197,2.901930,-0.647767,-9.313615,3.563372,0.622347,8.313611,-2.227841]],[[-7.694705,-7.322562,-6.865959,1.937586,-8.121139,5.390852,8.821188,8.750203,3.577613,-9.665332,9.569532,-5.837208,1.219572],[2.961129,-1.596695,7.909323,6.500091,9.728176,-0.028242,5.825053,-6.747971,0.993078,-6.784248,-9.234290,9.983841,5.797733],[4.058721,5.729883,3.746779,-9.236145,-2.318857,6.172178,7.381907,3.024514,4.498729,-0.789803,-2.651307,7.347413,-2.692071],[-7.887787,0.985465,-1.501900,-9.619538,2.899336,-9.770438,6.260829,4.939972,-2.552048,0.706717,-1.245700,3.048222,-6.759232],[-6.937236,-4.069624,-3.190649,-9.543133,7.275559,-1.472798,-8.840695,6.479871,4.849262,2.785744,5.110845,4.638445,-5.552034],[-1.438220,-1.612409,7.049544,-8.705049,5.427060,-6.175073,-8.168906,-8.550747,7.928102,3.081989,8.489057,0.874387,7.813118]],[[4.788448,-4.055665,3.774294,9.268241,0.611119,-9.574555,-7.348167,-9.831423,-4.070529,-4.920321,-2.325332,0.960394,7.415272],[-8.396252,-7.039053,8.128075,1.142667,4.442254,-1.407733,-9.249487,4.158745,-8.690544,8.202046,-5.364951,5.900247,-0.463557],[0.913201,7.285373,7.432171,1.495470,-6.466488,0.696262,-9.852293,-1.895560,4.019863,7.553410,1.100440,-6.618837,-4.761750],[-6.081211,-2.245636,1.174204,4.819749,-2.166794,9.721285,-6.959646,-4.355592,9.390212,-8.575925,-4.137025,-0.503547,-3.723205],[8.320942,-0.498027,1.678073,7.501191,-7.864204,5.246619,-3.424751,-7.005134,-5.490305,7.317780,-7.802979,0.952371,-1.516067],[-2.825163,9.748498,-2.392917,5.568202,3.381502,-9.288419,-4.082595,4.061466,-5.427236,5.638641,7.259782,9.976572,7.131210]],[[3.000018,-5.528736,-3.346022,0.670998,5.637314,-0.313370,-5.624486,5.868821,-9.501841,8.534162,-9.246161,6.369475,-2.554033],[1.324927,3.900719,3.955251,2.606966,-9.213389,-1.243785,-3.327954,-6.303115,6.171649,-8.697268,4.560152,-4.431982,-8.288363],[-8.674098,5.184547,4.325831,-4.770949,9.881144,8.697288,0.685192,-8.152093,2.027387,0.375354,6.390026,4.929694,0.944016],[-8.133699,8.732169,-4.196003,8.837171,4.522633,-2.600776,5.119338,5.546140,9.918674,9.334260,4.021598,-6.749211,-2.583578],[0.791008,7.834492,-2.818393,-3.197612,-4.785717,4.952992,-7.427529,-1.267577,-0.603182,-8.506814,5.467380,-6.603307,2.396290],[4.875104,-8.815766,5.037301,5.801781,-1.548625,0.010409,-2.604888,-0.489277,9.056973,-9.217201,7.389848,8.326836,-2.147880]]], dtype = "float64")#candidate|1194|(14, 6, 13)|const|float64
bop_1195 = relay.less(var_1180.astype('bool'), relay.reshape(const_1194.astype('bool'), relay.shape_of(var_1180))) # shape=(14, 6, 13)
uop_1206 = relay.erf(const_1194.astype('float64')) # shape=(14, 6, 13)
output = relay.Tuple([bop_1181,bop_1195,uop_1206,])
output2 = relay.Tuple([bop_1181,bop_1195,uop_1206,])
func_1210 = relay.Function([var_1179,var_1180,], output)
mod['func_1210'] = func_1210
mod = relay.transform.InferType()(mod)
var_1211 = relay.var("var_1211", dtype = "float64", shape = (14, 6, 13))#candidate|1211|(14, 6, 13)|var|float64
var_1212 = relay.var("var_1212", dtype = "float64", shape = (14, 6, 13))#candidate|1212|(14, 6, 13)|var|float64
output = func_1210(var_1211,var_1212,)
func_1213 = relay.Function([var_1211,var_1212,], output)
mutated_mod['func_1213'] = func_1213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1225 = relay.var("var_1225", dtype = "float32", shape = (14, 2, 3))#candidate|1225|(14, 2, 3)|var|float32
uop_1226 = relay.asinh(var_1225.astype('float32')) # shape=(14, 2, 3)
uop_1229 = relay.tan(uop_1226.astype('float32')) # shape=(14, 2, 3)
output = uop_1229
output2 = uop_1229
func_1231 = relay.Function([var_1225,], output)
mod['func_1231'] = func_1231
mod = relay.transform.InferType()(mod)
mutated_mod['func_1231'] = func_1231
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1232 = relay.var("var_1232", dtype = "float32", shape = (14, 2, 3))#candidate|1232|(14, 2, 3)|var|float32
func_1231_call = mutated_mod.get_global_var('func_1231')
call_1233 = func_1231_call(var_1232)
output = call_1233
func_1234 = relay.Function([var_1232], output)
mutated_mod['func_1234'] = func_1234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_1284 = relay.TupleGetItem(func_691_call(), 0)
call_1285 = relay.TupleGetItem(func_692_call(), 0)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_1319 = func_1171_call()
call_1320 = func_1171_call()
uop_1330 = relay.cos(call_1284.astype('float32')) # shape=(3, 5, 15)
uop_1332 = relay.cos(call_1285.astype('float32')) # shape=(3, 5, 15)
uop_1335 = relay.asinh(uop_1330.astype('float64')) # shape=(3, 5, 15)
uop_1337 = relay.asinh(uop_1332.astype('float64')) # shape=(3, 5, 15)
func_674_call = mod.get_global_var('func_674')
func_675_call = mutated_mod.get_global_var('func_675')
call_1345 = relay.TupleGetItem(func_674_call(), 1)
call_1346 = relay.TupleGetItem(func_675_call(), 1)
func_1022_call = mod.get_global_var('func_1022')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_1359 = relay.var("var_1359", dtype = "float64", shape = (32,))#candidate|1359|(32,)|var|float64
var_1360 = relay.var("var_1360", dtype = "int64", shape = (112,))#candidate|1360|(112,)|var|int64
call_1358 = relay.TupleGetItem(func_1022_call(relay.reshape(var_1359.astype('float64'), [8, 4, 1]), relay.reshape(var_1360.astype('int64'), [4, 28]), ), 0)
call_1361 = relay.TupleGetItem(func_1026_call(relay.reshape(var_1359.astype('float64'), [8, 4, 1]), relay.reshape(var_1360.astype('int64'), [4, 28]), ), 0)
output = relay.Tuple([call_1319,uop_1335,call_1345,call_1358,var_1359,var_1360,])
output2 = relay.Tuple([call_1320,uop_1337,call_1346,call_1361,var_1359,var_1360,])
func_1366 = relay.Function([var_1359,var_1360,], output)
mod['func_1366'] = func_1366
mod = relay.transform.InferType()(mod)
var_1367 = relay.var("var_1367", dtype = "float64", shape = (32,))#candidate|1367|(32,)|var|float64
var_1368 = relay.var("var_1368", dtype = "int64", shape = (112,))#candidate|1368|(112,)|var|int64
output = func_1366(var_1367,var_1368,)
func_1369 = relay.Function([var_1367,var_1368,], output)
mutated_mod['func_1369'] = func_1369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_1371 = relay.TupleGetItem(func_580_call(), 2)
call_1372 = relay.TupleGetItem(func_582_call(), 2)
var_1404 = relay.var("var_1404", dtype = "float64", shape = (3, 5, 15))#candidate|1404|(3, 5, 15)|var|float64
bop_1405 = relay.maximum(call_1371.astype('uint16'), relay.reshape(var_1404.astype('uint16'), relay.shape_of(call_1371))) # shape=(3, 5, 15)
bop_1408 = relay.maximum(call_1372.astype('uint16'), relay.reshape(var_1404.astype('uint16'), relay.shape_of(call_1372))) # shape=(3, 5, 15)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_1411 = func_446_call()
call_1412 = func_446_call()
output = relay.Tuple([bop_1405,call_1411,])
output2 = relay.Tuple([bop_1408,call_1412,])
func_1413 = relay.Function([var_1404,], output)
mod['func_1413'] = func_1413
mod = relay.transform.InferType()(mod)
mutated_mod['func_1413'] = func_1413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1414 = relay.var("var_1414", dtype = "float64", shape = (3, 5, 15))#candidate|1414|(3, 5, 15)|var|float64
func_1413_call = mutated_mod.get_global_var('func_1413')
call_1415 = func_1413_call(var_1414)
output = call_1415
func_1416 = relay.Function([var_1414], output)
mutated_mod['func_1416'] = func_1416
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1427 = relay.var("var_1427", dtype = "float32", shape = (10, 16, 11))#candidate|1427|(10, 16, 11)|var|float32
uop_1428 = relay.atanh(var_1427.astype('float32')) # shape=(10, 16, 11)
const_1436 = relay.const([[[5.854593,-3.709307,-7.911657,0.485827,6.058913,-8.262051,4.191098,4.151800,3.289053,-3.302223,5.370573],[-7.435207,-1.700003,-2.941788,5.364393,-9.048407,-9.086208,-1.890771,-0.499420,-5.425325,-1.654072,-4.895084],[-8.203564,-3.587408,1.847979,-9.897739,2.970368,-0.480968,-5.542838,-7.708737,-8.944777,-9.018152,5.148092],[-4.199363,3.877321,8.449931,0.485256,3.262240,7.775726,9.965567,-6.651021,-3.095539,-4.197849,7.534077],[1.465692,-3.861747,-8.240960,-7.069953,7.145482,-9.476867,6.172193,-0.631964,7.523272,-8.628194,-1.025780],[4.907713,-9.196508,-4.128106,9.295042,7.113133,3.158894,-0.689099,-4.233102,5.459709,2.379934,-9.340062],[7.623065,5.736882,-2.391713,-9.924447,5.930722,8.214866,0.549220,-7.128032,-3.161296,7.477124,-9.975836],[2.691436,-7.181374,-5.300840,-7.292550,-9.673800,-1.628031,-2.872626,8.462264,0.332373,3.855428,-0.037473],[-3.507888,3.986533,-1.776123,7.830292,-1.032899,-2.085163,7.182025,6.243888,8.652497,-3.186808,2.915865],[1.287811,1.959453,-5.065080,1.058594,9.146618,1.785295,-6.360833,2.240061,-6.461736,9.115398,-0.726038],[-1.373243,-8.638621,1.053503,8.247150,-4.079319,9.705783,9.934585,-6.996098,8.996636,-8.953182,-0.035176],[-9.612524,-9.848774,9.714857,0.287696,8.949306,3.426866,-2.217540,-8.771514,-8.313578,-6.815290,-6.216896],[2.458464,-7.725368,-9.747743,8.749035,-2.806335,-5.380342,9.797079,-7.186048,4.314977,-9.191288,6.350791],[4.971259,-8.335049,-2.613427,3.499568,-0.451646,1.056456,5.116073,5.661841,-9.854198,5.569586,1.208144],[1.412223,7.783296,7.912041,9.106171,-9.226653,-1.115428,-3.966599,4.952056,7.543895,-1.788556,5.136510],[-1.062199,3.737488,-3.571739,8.382494,5.610873,6.401984,4.868171,-0.039823,6.369364,3.510189,1.622067]],[[5.721594,9.739508,-6.928830,4.036401,-0.653649,-5.908547,3.673639,-4.280053,-6.179872,2.656699,-9.735103],[-5.223274,1.342385,-3.054076,2.349217,7.818615,-6.683639,3.856105,-7.095057,-3.420188,-0.349467,-3.724616],[6.000147,-0.420936,-5.005893,3.143586,-8.791310,7.974063,-2.605927,-4.207342,5.709587,-6.394004,0.179616],[-8.359779,-5.732178,-1.982552,-5.206086,-8.510905,0.889249,6.189912,-4.154818,-3.399441,6.313154,8.290944],[1.246898,4.883215,3.272137,7.683576,-9.680024,-6.543468,-8.904154,8.449952,-1.254286,3.702808,0.594286],[7.976409,5.119701,-6.945410,-2.435916,-6.706834,-7.003020,-5.427820,7.773211,-6.479633,-0.399073,2.523884],[2.362789,6.729098,-3.146809,6.132727,0.481759,-9.343935,-6.939515,7.666914,-5.784021,3.728290,-0.065415],[-2.080291,8.922036,1.523658,4.494698,-0.405647,3.001496,-5.032726,-0.488286,8.957114,0.979434,7.813467],[3.660021,-7.743399,-9.975326,-5.660071,5.994035,3.929225,7.603741,-6.762126,5.596891,3.236742,-7.034300],[-7.947903,0.656386,2.774234,3.394914,-5.992327,1.143093,-9.832321,-9.378566,-0.238646,1.169404,-2.759858],[-8.021012,-1.776287,-0.939250,2.767216,2.354837,1.092728,5.347205,8.143036,7.014702,7.155434,-6.645710],[5.026780,-6.122246,5.502710,3.184435,-2.485277,-5.933589,3.844140,-1.014740,-9.045722,-7.574719,-5.308641],[-4.831216,0.381350,-5.469997,-7.952644,-5.486487,8.692638,-6.781055,3.220308,6.124837,9.790858,-8.231426],[-8.251471,2.923032,-8.792627,-6.955224,-0.786682,6.809853,7.048726,-8.151115,-4.046417,9.127842,-1.687069],[-2.134262,9.818337,5.240032,-1.833713,6.215335,8.305546,4.428834,-0.271958,-0.239799,-0.797367,-3.853662],[1.423067,9.742489,-7.293930,-5.534934,-1.579756,-4.566807,-7.033972,5.977005,8.345871,3.309389,0.432404]],[[-4.048241,-2.435806,-9.151363,-1.463348,-5.988091,-1.635084,-6.771480,-1.849207,8.335586,2.660585,-7.538878],[8.434068,-0.908474,-2.626090,4.987404,-7.919331,-9.976860,7.732051,6.433851,9.860257,9.777134,-6.653452],[-2.727990,-1.095865,8.824305,0.131950,3.530153,2.216420,8.048408,5.381394,-2.263154,7.486912,9.588055],[5.144409,-1.658554,-8.316893,-9.974280,9.178661,-8.321993,-4.959288,-9.583216,4.100400,3.175768,5.631919],[9.310802,4.281398,5.062867,-8.726398,6.011147,8.794187,-4.139194,-7.484147,-6.582677,-0.071907,0.056315],[6.177868,-1.068349,-2.453125,5.730562,3.210522,-5.384055,-6.641743,0.321088,-4.084543,9.376807,-1.392430],[-1.701852,-6.372162,1.023616,2.824003,-4.776653,-9.310333,7.122932,-2.794935,-8.977570,3.247563,-9.379598],[-2.983205,-4.653235,6.755119,6.073395,-7.207922,-1.018571,-3.327015,9.978217,-3.738775,-7.490574,-3.781557],[6.693848,3.118455,-0.062631,0.925541,-8.806115,-3.723828,-5.439366,-6.987834,-5.810566,9.721686,-8.868278],[-8.623257,8.708989,3.214403,4.727518,-3.931050,-6.889049,-3.796015,-2.426302,5.881320,-1.710628,-8.693240],[3.089892,-7.581505,9.794320,-3.995898,4.540001,2.277159,-4.615627,3.432008,-5.028339,-6.918728,5.867993],[-5.922771,-0.188293,-2.969920,1.753836,-8.466431,-7.467154,-6.656748,-6.117609,4.863177,0.652820,2.818720],[6.917316,9.237463,-0.767068,-9.881892,6.804526,7.854094,-3.694722,-7.719314,-5.121725,2.408354,1.238680],[-5.506215,-8.669576,7.816432,-2.495347,9.930382,0.204825,-0.765034,2.105860,4.034198,5.503160,-1.936489],[9.295522,4.937647,0.920357,-7.839767,6.044734,4.917613,-4.589934,3.920808,1.715405,-5.548578,-7.142990],[-2.927988,3.911527,-3.622116,-2.053585,-6.633995,0.747069,-9.403844,-7.874288,5.134406,2.616783,-3.738398]],[[1.941464,2.919855,-4.707668,-4.093432,-8.884619,-1.581617,-0.336150,-8.013532,-7.678186,-7.618967,-2.507973],[-2.521126,7.494481,-8.598411,-5.141444,-5.117571,1.023641,-6.937425,0.838990,-3.587035,4.692202,1.065298],[0.606868,3.204042,5.532168,9.219810,-8.287776,-0.019063,4.190588,-9.829137,8.804055,6.322071,-4.442433],[6.958189,-1.678226,7.645618,-3.833173,-9.744227,-0.522487,9.925486,0.034035,-2.791959,7.444444,-3.425456],[4.982568,-5.161752,6.216898,4.866486,-6.861917,-3.359830,-3.277659,-0.016009,-0.558496,-8.807881,-8.884324],[-5.356479,-0.500406,5.991656,-4.957265,-8.559828,5.880967,-9.283998,1.065506,-7.737853,-2.957875,-0.108813],[1.534930,-3.468907,4.784276,-8.065641,-0.697236,-1.077913,4.464850,-4.920259,4.560904,-5.129682,-5.025504],[2.070994,-2.043633,5.158349,-1.531884,-6.007333,-5.386472,-7.395611,1.193455,-3.060664,8.174797,7.951066],[-6.586971,-0.355097,-7.787901,-2.725222,-8.623970,-6.983897,-0.913971,8.512074,-7.083871,-8.650333,-0.300278],[-4.607575,9.000653,-1.599144,9.529337,-7.731512,4.552857,3.797688,8.622944,-7.926140,-7.557562,-4.287195],[-9.024168,1.983874,6.610906,-6.233527,-6.438787,-9.843366,6.466306,0.134026,-8.696100,-7.294366,-5.121375],[5.913703,-1.571062,6.090379,3.101578,3.362918,-3.116987,-1.877661,-4.417790,8.485652,4.753611,-5.322671],[-2.706468,-5.746383,9.615425,0.780429,-3.441101,0.241998,-0.467593,3.292937,8.413858,-5.918650,-0.020099],[0.418204,3.469170,0.832605,-7.947648,3.911080,7.158693,9.635262,-8.024873,0.095694,-9.903700,0.145013],[1.811248,-6.944864,2.505072,-0.041437,8.592686,-0.696421,2.436771,6.006179,-8.515220,-8.927188,-9.138366],[-7.687108,-7.830525,-6.309655,4.327909,-4.154259,-1.264831,7.665559,1.847694,6.027385,0.686972,4.878851]],[[-3.966572,0.038864,3.425040,-3.723468,9.429315,-0.879697,-2.944383,-4.593528,2.772859,3.370194,5.481759],[5.555017,-7.954487,9.495913,5.259205,-0.289387,-0.762969,-8.086095,-6.307360,8.498951,6.070866,1.660196],[-3.633486,3.656626,-2.048837,-2.894053,7.382271,-3.871033,-0.618381,-6.388840,-4.574116,5.883547,-3.815985],[-4.998577,0.770294,-5.711123,-7.483708,-3.601770,-9.076422,-9.248112,-2.146598,-0.022781,-5.354703,-5.094576],[6.760596,-1.003143,0.170475,-3.562754,2.893763,-3.508469,-1.567376,-1.190698,0.594540,-5.289995,-3.597517],[-9.624523,6.341306,4.845921,-2.473034,-5.684133,-2.830302,1.790871,2.056906,2.212600,8.029156,7.505567],[-2.659489,-2.436709,-3.660319,5.595023,2.148842,-4.521782,2.659081,-8.677081,2.694692,9.778461,-7.844749],[9.034819,-1.071117,-6.469358,0.193831,1.054601,3.531915,9.411086,-4.006532,3.369870,-0.175291,-6.049670],[3.796891,4.750320,-2.130277,-6.723272,-6.761549,-8.843680,-8.237863,-8.700691,-3.384506,2.103858,4.768306],[1.574706,-5.211540,4.670296,-1.691337,-3.084967,-4.170518,-8.815361,-1.589416,9.166622,7.432770,9.176049],[5.172697,8.997173,8.451632,4.715729,5.789744,3.371754,1.808599,-0.335595,-1.348895,2.239134,4.588950],[7.015065,-8.986260,-6.512229,-5.302653,6.605780,9.428006,2.081886,-2.129842,1.435062,-4.577101,9.626865],[4.396592,4.186601,-1.849355,-8.908046,4.534958,2.912903,9.792124,0.480999,6.216019,3.342997,6.539416],[7.094483,5.463211,1.331413,6.595013,-7.781990,-0.849688,6.644770,-7.229777,-2.747976,0.226260,-6.976219],[2.818640,7.094804,-4.127203,9.201728,0.821352,5.347006,2.086483,-9.656969,7.627133,2.493390,5.609763],[-6.103606,3.036620,7.044557,-9.325214,6.851304,4.144480,-6.087914,7.789291,0.070791,2.529670,1.629648]],[[8.651567,2.584569,-5.016853,-1.496091,6.872131,-7.228223,-1.877660,-8.529197,2.906392,-3.154060,-4.560764],[-8.701336,2.617500,-4.970757,6.261608,5.838833,-7.811998,7.261881,-8.458504,-9.528459,0.584246,-8.353646],[-8.831948,-9.398336,-3.599618,-0.860767,-8.683671,-6.192563,-0.724685,-8.228449,-3.620430,-4.600537,-9.114465],[-1.900478,2.515817,1.378473,9.310332,-0.660282,-9.994787,5.281536,-7.179133,0.892318,-0.729195,-1.199459],[-2.546819,-1.976461,-1.127125,9.278059,4.271799,6.819025,-5.279850,2.837023,-7.954378,9.147877,-1.040225],[5.991583,-0.564680,2.334246,-8.784386,0.197473,-4.018932,-9.129877,-1.914998,-2.696731,2.187917,0.886477],[-6.144970,6.225528,-4.134691,2.258127,1.085530,7.446029,3.244001,-5.418647,-9.820312,-0.644850,-3.490139],[-3.665730,6.832920,-3.534322,-8.618802,-1.536053,-5.779209,-8.803535,3.676087,8.699834,-1.516055,-3.391816],[-8.683655,-0.311591,2.141917,5.471091,7.254410,-0.965693,-2.948287,7.025661,-7.199331,1.156685,6.043745],[-3.086267,1.949916,0.569229,-6.064979,1.109422,-5.262905,-9.501170,5.997740,2.783352,9.484521,0.359985],[-3.118802,-4.108732,-5.982830,5.699079,7.101286,-3.652328,-7.064656,3.834660,-3.107871,7.090596,-1.220869],[-5.848940,4.348673,-3.826469,2.892215,4.720637,-3.339463,5.336707,0.693637,-2.330175,-5.348987,-8.515448],[-9.059319,8.491790,-6.401091,0.849468,-9.153733,-5.141354,-7.194590,-7.000615,-5.430360,8.236890,-5.258175],[-9.584288,-4.431742,-4.473653,4.480090,7.938748,-8.660244,-7.271530,8.459400,4.811431,6.510427,0.294731],[-3.587821,-2.263361,2.589337,2.000331,-8.641157,-1.013157,-7.364897,8.759132,9.915740,4.607317,5.260842],[-3.545865,-4.913153,9.508905,-7.155073,6.967846,-6.032868,7.059962,8.211135,1.810208,-5.513366,-0.836675]],[[8.050832,1.939023,-0.103264,-9.510810,-1.062370,-8.507634,9.490164,6.062580,3.833317,-2.947886,-1.401433],[6.360560,5.075946,2.465521,-0.300654,-3.295677,7.551830,-1.499793,7.445324,6.733869,-5.882454,-3.470242],[9.570540,9.160430,-4.498566,4.801237,1.346422,-9.410213,9.534228,0.635157,-4.483394,2.621778,5.732599],[6.588169,4.610724,-4.526371,6.570329,8.116254,-8.064656,8.687366,-5.620398,4.074198,0.256429,-6.363060],[3.443037,5.490258,-7.201454,7.147087,-7.789213,-5.050768,-6.346197,4.730831,6.148620,-3.781015,4.181547],[-9.069379,-4.441727,-8.407085,4.830392,2.157295,-7.353672,-6.299851,0.262945,-0.749048,0.403216,3.092831],[9.684301,2.396659,1.980051,7.954179,9.059552,0.708602,1.731506,1.620568,-9.855525,-9.085437,6.155435],[5.078791,-5.261777,8.295673,-5.719955,7.096251,6.146977,-3.114855,0.033128,-4.701671,6.638125,-4.054939],[1.820586,-0.095213,-0.030616,-8.073374,9.357901,0.893186,7.256394,3.659728,6.848898,2.587362,7.777107],[-9.963337,7.191014,2.022235,-6.238929,-0.595695,-8.258255,9.691780,0.957650,-7.742601,-5.341099,-2.665916],[-4.757166,7.567309,5.133128,1.668648,4.422957,6.416699,-1.325438,9.389132,-6.520140,-1.782058,-5.162333],[-4.388151,0.984400,9.811846,-5.897313,1.865369,9.672840,-3.521150,5.618591,-4.557597,7.453608,-5.202021],[-1.184938,-4.698727,3.137125,5.212858,6.669142,3.154645,2.406116,-8.329359,-8.112006,-3.533524,-4.369146],[-2.999072,-4.585177,-7.162478,-5.538981,0.546454,6.995842,-8.568606,-9.911791,-8.265643,3.593520,-4.912933],[-8.793794,-9.262711,-4.675049,1.808391,7.165480,1.056198,-3.174577,-6.578043,-5.180293,3.777765,9.327605],[-8.977444,-2.427759,1.668599,-6.942647,-1.084448,-2.799343,1.998695,1.557276,-7.117083,1.723218,2.821262]],[[0.166045,-1.175058,5.445870,2.002537,2.078954,1.105448,4.318019,9.971000,-8.364994,-2.872043,-9.435468],[-5.578401,-6.266749,1.281759,-9.939248,3.063764,-9.867360,4.869249,-3.011716,-3.443334,-7.989163,3.897802],[9.079120,3.206277,-0.884613,-5.638369,2.422905,-3.389076,0.056756,2.506160,-2.287280,-6.995123,6.130670],[9.067932,-1.046867,8.091179,4.373244,-9.406514,-8.424155,-4.430480,-1.161148,0.633048,6.964887,5.157565],[1.031346,-3.412609,-3.582247,-2.793720,-4.182282,1.911078,-2.419733,0.923342,8.028308,-7.100600,5.915510],[-2.863830,7.214793,-8.738133,2.384604,-9.640792,-6.615080,1.009742,5.135686,-1.184397,9.727611,-8.665215],[4.900688,9.045467,-7.178450,-0.364327,-4.599695,0.005580,-7.540832,7.364811,0.327478,1.852079,-0.769540],[-2.007955,-5.172636,-5.096261,-0.999161,3.355083,-9.959502,-5.094236,-7.144075,1.365604,1.553048,3.122983],[-9.198538,-2.452706,-9.517027,1.986575,-3.082252,-9.875576,0.996681,-5.618454,5.689010,4.456185,-9.080662],[-3.590075,-5.356969,7.323015,-6.216958,5.685085,0.926538,4.341334,9.844740,9.736398,-3.017960,1.523725],[-2.628915,-2.508557,7.274402,9.504211,6.259089,4.552069,3.370129,-9.595986,9.814050,-1.460939,5.534348],[-7.073253,4.780355,-2.054054,3.882942,8.603726,9.818225,4.441242,1.698392,-6.599457,8.763154,-5.863709],[-8.181668,-5.103323,-9.982269,2.689831,-6.456739,0.994408,9.431621,-4.053690,5.187498,-5.303836,2.823909],[4.756736,-1.486072,2.682602,5.083134,8.993850,-7.667324,0.126614,-3.706028,-1.399892,-9.665361,-0.079519],[1.700546,-1.069307,-6.679167,2.297200,9.215766,-2.481751,-5.193333,7.037827,1.264276,-1.927845,-1.739931],[0.800049,-8.747686,-0.056560,3.139932,-6.132659,7.676151,2.609281,7.955051,4.173025,7.351845,-3.408842]],[[6.235545,-0.332122,-4.601824,6.889772,-8.397235,-4.807072,-9.535406,-1.778570,0.824443,5.093647,8.778486],[9.243659,3.129172,7.063034,-1.176405,9.983313,9.484579,4.843378,-6.811898,8.563811,8.024311,4.280927],[-1.325437,4.046497,-3.464583,-9.525118,3.044042,-4.987649,-2.952640,5.166741,9.387953,-3.834644,-7.880228],[1.497322,-1.933109,-2.355388,-3.922177,-0.372867,5.486539,-9.268044,-2.508819,3.094527,-3.178564,-9.086953],[-8.752841,-0.564019,-6.352844,-4.649631,-1.398897,8.322138,-5.366724,-0.990050,1.772101,4.919668,-1.881426],[-7.160732,-2.290116,-2.814434,7.229382,7.739900,-7.583184,-1.539984,4.969214,-6.575323,-5.749504,-2.916333],[3.519925,6.415869,1.707990,6.618047,-4.213898,-4.095137,6.018908,-0.154282,-8.898692,-0.013517,7.189294],[0.189790,-6.264393,-1.722147,-6.436813,0.047819,9.491959,-9.756139,-6.692457,-4.056583,-8.926193,9.072026],[9.865487,-2.289201,-2.733720,-3.048937,8.632137,-8.224910,9.222011,-2.015204,9.191490,5.709441,-6.506559],[-0.495025,3.746045,-9.660795,7.004871,-3.633316,3.522100,-6.220262,0.453954,1.584723,7.173380,-4.165910],[-3.206031,-6.173725,5.310412,-1.812288,6.537559,-8.838838,8.935993,-7.785858,-3.096341,3.937092,-3.588884],[6.557771,-4.654282,-9.527701,-2.998598,2.517564,-3.836352,2.021471,7.743974,4.663476,-3.490041,-2.939383],[-1.844996,-5.663821,3.741645,-3.151479,-8.560785,5.624769,-9.344187,-1.310351,4.517706,0.903476,9.042005],[2.406341,-0.902101,2.048364,-9.092767,-4.737870,3.308423,2.193463,-7.232862,-4.066591,-0.827711,-6.847061],[3.577741,5.523524,-3.338682,-2.861094,2.981172,-6.602647,2.185939,-0.513836,1.859168,-7.411277,-6.923757],[9.125014,-0.071520,2.416281,-4.275132,4.345757,-9.228259,-1.337518,-7.317231,-8.985543,-7.774245,5.459324]],[[-5.339922,0.749357,8.522635,-7.097366,7.560181,-1.224102,2.533632,-8.190567,4.084736,-1.748904,0.636135],[-3.188766,8.105563,1.177311,-3.939295,4.002644,4.737101,-8.062274,4.182668,-1.622757,0.530136,-3.814373],[-5.329308,-0.723536,-4.440986,7.422951,2.727695,2.311439,-1.020676,-5.276811,-5.826472,0.833407,-3.850765],[-0.458951,4.591309,-0.637155,5.644535,1.374186,-7.650624,-7.049136,-1.895547,-6.446636,7.806358,2.001244],[-1.196775,-9.604889,2.708048,-7.869529,-5.342524,3.147858,9.710857,-5.671692,-7.377662,-3.517536,1.992174],[-7.692049,-1.889749,2.542333,-9.450095,7.277459,-7.466650,3.236126,-4.919141,5.420884,-9.364654,-4.245127],[-2.231125,7.325340,-9.255151,7.040171,-6.289495,-3.031934,-7.824882,-9.841797,-8.453969,-9.556250,-0.150488],[-9.103771,3.133665,7.809542,1.518259,-8.955402,-3.961399,-6.626499,9.572790,-6.308197,9.244232,9.317590],[-5.141481,5.650618,2.652721,4.516067,2.423442,-5.648048,2.388595,7.138645,4.935841,-1.110257,8.969975],[1.821801,1.931038,-6.181401,-8.726772,-9.397721,2.124751,9.780583,0.999725,-8.698711,-8.076611,-0.492308],[-5.555607,-5.132215,3.606606,0.327892,-2.005229,8.374289,-7.673961,-0.235517,5.578685,2.692604,-7.030242],[-7.917696,4.545937,7.895137,9.789793,5.645483,9.894439,-7.761881,7.692111,0.920897,-9.870772,8.607265],[-1.568780,8.915043,-0.983440,-2.527031,0.772157,3.022510,-1.800233,-6.025374,-6.318653,0.046221,-2.318238],[-8.945701,-9.138609,1.441681,-2.868671,2.404744,-0.779488,0.614374,-4.054588,-0.979133,-0.575375,-5.328140],[-8.622805,-8.541366,7.741455,-1.157559,8.015969,2.650523,-6.762722,-3.541513,3.622764,4.048183,-4.795183],[-6.208468,-0.483418,-6.735069,-6.787539,5.538905,-7.261912,7.997952,-8.162992,9.493696,-4.221496,0.874429]]], dtype = "float32")#candidate|1436|(10, 16, 11)|const|float32
bop_1437 = relay.not_equal(uop_1428.astype('bool'), relay.reshape(const_1436.astype('bool'), relay.shape_of(uop_1428))) # shape=(10, 16, 11)
uop_1442 = relay.asinh(bop_1437.astype('float32')) # shape=(10, 16, 11)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_1448 = func_446_call()
call_1449 = func_446_call()
func_1022_call = mod.get_global_var('func_1022')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_1462 = relay.var("var_1462", dtype = "float64", shape = (32,))#candidate|1462|(32,)|var|float64
var_1463 = relay.var("var_1463", dtype = "int64", shape = (112,))#candidate|1463|(112,)|var|int64
call_1461 = relay.TupleGetItem(func_1022_call(relay.reshape(var_1462.astype('float64'), [8, 4, 1]), relay.reshape(var_1463.astype('int64'), [4, 28]), ), 1)
call_1464 = relay.TupleGetItem(func_1026_call(relay.reshape(var_1462.astype('float64'), [8, 4, 1]), relay.reshape(var_1463.astype('int64'), [4, 28]), ), 1)
func_1413_call = mod.get_global_var('func_1413')
func_1416_call = mutated_mod.get_global_var('func_1416')
call_1487 = relay.TupleGetItem(func_1413_call(relay.reshape(call_1448.astype('float64'), [3, 5, 15])), 0)
call_1488 = relay.TupleGetItem(func_1416_call(relay.reshape(call_1448.astype('float64'), [3, 5, 15])), 0)
output = relay.Tuple([uop_1442,call_1448,call_1461,var_1462,var_1463,call_1487,])
output2 = relay.Tuple([uop_1442,call_1449,call_1464,var_1462,var_1463,call_1488,])
func_1498 = relay.Function([var_1427,var_1462,var_1463,], output)
mod['func_1498'] = func_1498
mod = relay.transform.InferType()(mod)
mutated_mod['func_1498'] = func_1498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1498_call = mutated_mod.get_global_var('func_1498')
var_1500 = relay.var("var_1500", dtype = "float32", shape = (10, 16, 11))#candidate|1500|(10, 16, 11)|var|float32
var_1501 = relay.var("var_1501", dtype = "float64", shape = (32,))#candidate|1501|(32,)|var|float64
var_1502 = relay.var("var_1502", dtype = "int64", shape = (112,))#candidate|1502|(112,)|var|int64
call_1499 = func_1498_call(var_1500,var_1501,var_1502,)
output = call_1499
func_1503 = relay.Function([var_1500,var_1501,var_1502,], output)
mutated_mod['func_1503'] = func_1503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mod.get_global_var('func_830')
func_832_call = mutated_mod.get_global_var('func_832')
call_1510 = relay.TupleGetItem(func_830_call(), 0)
call_1511 = relay.TupleGetItem(func_832_call(), 0)
output = call_1510
output2 = call_1511
func_1529 = relay.Function([], output)
mod['func_1529'] = func_1529
mod = relay.transform.InferType()(mod)
output = func_1529()
func_1530 = relay.Function([], output)
mutated_mod['func_1530'] = func_1530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_1531 = relay.TupleGetItem(func_611_call(), 3)
call_1532 = relay.TupleGetItem(func_613_call(), 3)
uop_1537 = relay.acos(call_1531.astype('float32')) # shape=(3, 5, 15)
uop_1539 = relay.acos(call_1532.astype('float32')) # shape=(3, 5, 15)
func_981_call = mod.get_global_var('func_981')
func_983_call = mutated_mod.get_global_var('func_983')
var_1551 = relay.var("var_1551", dtype = "uint16", shape = (324,))#candidate|1551|(324,)|var|uint16
call_1550 = relay.TupleGetItem(func_981_call(relay.reshape(var_1551.astype('uint16'), [324,])), 2)
call_1552 = relay.TupleGetItem(func_983_call(relay.reshape(var_1551.astype('uint16'), [324,])), 2)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_1553 = relay.TupleGetItem(func_691_call(), 0)
call_1554 = relay.TupleGetItem(func_692_call(), 0)
bop_1555 = relay.add(uop_1537.astype('int16'), relay.reshape(call_1553.astype('int16'), relay.shape_of(uop_1537))) # shape=(3, 5, 15)
bop_1558 = relay.add(uop_1539.astype('int16'), relay.reshape(call_1554.astype('int16'), relay.shape_of(uop_1539))) # shape=(3, 5, 15)
func_820_call = mod.get_global_var('func_820')
func_823_call = mutated_mod.get_global_var('func_823')
var_1573 = relay.var("var_1573", dtype = "int16", shape = ())#candidate|1573|()|var|int16
var_1574 = relay.var("var_1574", dtype = "int16", shape = (600,))#candidate|1574|(600,)|var|int16
call_1572 = relay.TupleGetItem(func_820_call(relay.reshape(var_1573.astype('int16'), []), relay.reshape(var_1574.astype('int16'), [10, 10, 6]), ), 2)
call_1575 = relay.TupleGetItem(func_823_call(relay.reshape(var_1573.astype('int16'), []), relay.reshape(var_1574.astype('int16'), [10, 10, 6]), ), 2)
output = relay.Tuple([call_1550,var_1551,bop_1555,call_1572,var_1573,var_1574,])
output2 = relay.Tuple([call_1552,var_1551,bop_1558,call_1575,var_1573,var_1574,])
func_1609 = relay.Function([var_1551,var_1573,var_1574,], output)
mod['func_1609'] = func_1609
mod = relay.transform.InferType()(mod)
mutated_mod['func_1609'] = func_1609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mutated_mod.get_global_var('func_1609')
var_1611 = relay.var("var_1611", dtype = "uint16", shape = (324,))#candidate|1611|(324,)|var|uint16
var_1612 = relay.var("var_1612", dtype = "int16", shape = ())#candidate|1612|()|var|int16
var_1613 = relay.var("var_1613", dtype = "int16", shape = (600,))#candidate|1613|(600,)|var|int16
call_1610 = func_1609_call(var_1611,var_1612,var_1613,)
output = call_1610
func_1614 = relay.Function([var_1611,var_1612,var_1613,], output)
mutated_mod['func_1614'] = func_1614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_1628 = relay.TupleGetItem(func_611_call(), 2)
call_1629 = relay.TupleGetItem(func_613_call(), 2)
func_1231_call = mod.get_global_var('func_1231')
func_1234_call = mutated_mod.get_global_var('func_1234')
var_1658 = relay.var("var_1658", dtype = "float32", shape = (84,))#candidate|1658|(84,)|var|float32
call_1657 = func_1231_call(relay.reshape(var_1658.astype('float32'), [14, 2, 3]))
call_1659 = func_1231_call(relay.reshape(var_1658.astype('float32'), [14, 2, 3]))
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_1666 = relay.TupleGetItem(func_580_call(), 3)
call_1667 = relay.TupleGetItem(func_582_call(), 3)
output = relay.Tuple([call_1628,call_1657,var_1658,call_1666,])
output2 = relay.Tuple([call_1629,call_1659,var_1658,call_1667,])
func_1672 = relay.Function([var_1658,], output)
mod['func_1672'] = func_1672
mod = relay.transform.InferType()(mod)
var_1673 = relay.var("var_1673", dtype = "float32", shape = (84,))#candidate|1673|(84,)|var|float32
output = func_1672(var_1673)
func_1674 = relay.Function([var_1673], output)
mutated_mod['func_1674'] = func_1674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_1687 = func_425_call()
call_1688 = func_425_call()
func_1413_call = mod.get_global_var('func_1413')
func_1416_call = mutated_mod.get_global_var('func_1416')
call_1691 = relay.TupleGetItem(func_1413_call(relay.reshape(call_1687.astype('float64'), [3, 5, 15])), 1)
call_1692 = relay.TupleGetItem(func_1416_call(relay.reshape(call_1687.astype('float64'), [3, 5, 15])), 1)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_1704 = relay.TupleGetItem(func_480_call(relay.reshape(call_1687.astype('float64'), [3, 5, 15])), 1)
call_1705 = relay.TupleGetItem(func_482_call(relay.reshape(call_1687.astype('float64'), [3, 5, 15])), 1)
output = relay.Tuple([call_1687,call_1691,call_1704,])
output2 = relay.Tuple([call_1688,call_1692,call_1705,])
func_1709 = relay.Function([], output)
mod['func_1709'] = func_1709
mod = relay.transform.InferType()(mod)
mutated_mod['func_1709'] = func_1709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1709_call = mutated_mod.get_global_var('func_1709')
call_1710 = func_1709_call()
output = call_1710
func_1711 = relay.Function([], output)
mutated_mod['func_1711'] = func_1711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_674_call = mod.get_global_var('func_674')
func_675_call = mutated_mod.get_global_var('func_675')
call_1722 = relay.TupleGetItem(func_674_call(), 1)
call_1723 = relay.TupleGetItem(func_675_call(), 1)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_1726 = func_446_call()
call_1727 = func_446_call()
output = relay.Tuple([call_1722,call_1726,])
output2 = relay.Tuple([call_1723,call_1727,])
func_1729 = relay.Function([], output)
mod['func_1729'] = func_1729
mod = relay.transform.InferType()(mod)
mutated_mod['func_1729'] = func_1729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1729_call = mutated_mod.get_global_var('func_1729')
call_1730 = func_1729_call()
output = call_1730
func_1731 = relay.Function([], output)
mutated_mod['func_1731'] = func_1731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mod.get_global_var('func_830')
func_832_call = mutated_mod.get_global_var('func_832')
call_1746 = relay.TupleGetItem(func_830_call(), 0)
call_1747 = relay.TupleGetItem(func_832_call(), 0)
output = relay.Tuple([call_1746,])
output2 = relay.Tuple([call_1747,])
func_1752 = relay.Function([], output)
mod['func_1752'] = func_1752
mod = relay.transform.InferType()(mod)
output = func_1752()
func_1753 = relay.Function([], output)
mutated_mod['func_1753'] = func_1753
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1780 = relay.const([[[-6.871189,7.355341,3.655391,-1.833381,2.333833,-2.680616,5.107235,7.973485,0.443433,-2.764300,-5.097927,-3.826886,5.364466,-9.307489,-6.078697,4.448653],[6.881405,-5.909853,0.555430,9.659642,-4.947842,7.745656,6.203924,-2.153670,-6.398444,4.772334,-7.040069,4.215264,-4.837810,4.246845,5.690297,8.883652],[3.747272,9.442745,-7.542164,4.009928,3.449886,2.107216,2.478765,7.079509,-2.392696,6.887458,0.244447,-7.402672,-9.861979,-5.421243,-4.756601,-3.978897],[-7.132758,-3.420417,6.477621,3.016592,2.963932,2.572032,2.962977,-4.292239,-8.937355,-4.481568,-9.714162,9.733613,-0.087814,-1.717312,2.779821,6.167966],[6.264368,1.529165,1.737251,6.435476,1.820491,-4.050310,4.529492,-9.609960,-0.278839,8.332012,8.684228,1.041244,3.781920,2.659976,6.453354,-2.532058]],[[-9.236579,4.507252,-8.549088,-5.367755,3.308479,-1.734475,2.307229,-9.674743,4.605612,-5.886364,-1.942619,5.693535,-6.961918,2.552622,5.194259,-5.725163],[9.259954,6.081749,-4.198030,0.727450,-5.041529,-4.682844,-9.878209,8.450695,3.652690,-7.716319,-3.527231,4.902275,-0.884306,-4.166057,-1.429606,-4.516308],[-8.491966,1.749193,0.440687,-5.839083,0.892697,-5.447898,-9.569001,7.090334,6.121020,8.802640,3.528239,-4.599633,8.549707,6.213969,8.383593,4.833980],[-1.761946,-5.163299,6.912697,8.116355,-6.394273,-4.140752,-6.207972,-8.439868,-2.322809,0.939971,-5.274159,2.341492,-7.078425,9.893868,-1.444022,2.580258],[4.373865,8.002407,-4.776143,4.248300,-0.247155,3.976251,-1.485834,-6.990857,-4.927063,-7.156731,-0.833606,-2.870916,3.231826,-7.959555,1.717419,-4.320585]]], dtype = "float64")#candidate|1780|(2, 5, 16)|const|float64
uop_1781 = relay.erf(const_1780.astype('float64')) # shape=(2, 5, 16)
bop_1796 = relay.divide(uop_1781.astype('float32'), relay.reshape(const_1780.astype('float32'), relay.shape_of(uop_1781))) # shape=(2, 5, 16)
func_820_call = mod.get_global_var('func_820')
func_823_call = mutated_mod.get_global_var('func_823')
var_1800 = relay.var("var_1800", dtype = "int16", shape = ())#candidate|1800|()|var|int16
const_1801 = relay.const([-4,-8,3,-10,-2,8,4,-5,-10,9,6,-4,2,5,2,5,-2,6,2,2,7,-3,2,8,-4,-7,-4,5,8,9,8,5,-8,7,9,6,-9,-6,7,-2,2,-3,2,-2,10,10,5,9,-8,-7,-4,-2,-10,-4,4,-1,-9,5,-2,4,8,1,-9,9,7,-6,-9,-5,-9,-7,9,3,2,-9,-7,-8,7,10,-10,-7,7,7,2,-4,-3,7,-10,-9,-2,-9,-3,4,6,10,-3,2,-8,5,-3,4,1,-9,4,5,8,5,-1,-3,-2,-3,-8,6,-6,-10,9,6,-5,-3,2,-7,2,-4,-10,9,10,7,-9,-5,-4,-7,-9,5,7,-7,7,-3,-3,-1,-4,4,-4,-3,4,9,3,2,-8,-9,8,8,-7,6,8,4,-8,5,9,-7,5,2,-4,3,-3,9,-6,7,-9,-7,10,8,-10,-10,-2,4,4,7,-2,10,-1,-7,7,4,8,-3,-3,-6,6,3,-4,-5,-5,-4,1,2,-2,-2,-4,-5,10,-1,-8,7,3,-10,-9,5,7,2,-1,3,5,4,-4,4,-8,-8,-9,10,6,-1,7,10,-3,-4,-9,2,4,5,-7,-1,-1,-1,5,6,-3,8,-3,6,3,2,8,-5,-2,-2,9,-3,-4,3,-8,-1,-6,-3,-9,4,-8,5,-2,10,-3,2,8,2,-2,3,6,2,-5,10,1,-8,-2,-7,-3,6,-1,-6,6,3,5,-7,-10,-2,2,-10,7,4,-9,2,7,-6,8,9,1,1,8,8,7,-4,3,-3,-2,-10,7,-4,1,5,3,-5,-6,4,-4,-3,-6,3,-2,2,5,-6,-5,9,2,7,-7,-4,9,-8,-10,-6,-9,8,7,-7,1,3,8,1,-5,5,-1,9,-7,-4,10,-5,-1,2,10,-8,-7,-6,4,-4,6,-3,8,-8,10,4,-4,-1,-2,2,-4,-3,-3,7,6,8,-1,-10,4,-4,10,4,-8,8,8,2,-10,5,5,3,-3,5,4,3,-5,-4,-8,10,3,-4,8,5,10,-5,3,-8,1,-2,-9,2,-5,-1,-5,7,-9,-1,6,8,5,2,-3,6,-4,-6,-5,-8,-7,1,10,-1,10,7,-5,3,10,2,8,7,8,4,4,-2,-3,-4,-3,-1,7,9,6,-4,9,-10,-5,6,10,5,-6,-6,1,1,7,7,3,-7,-5,-5,-8,1,2,5,1,-8,8,-5,8,-3,9,10,-3,9,8,4,1,-9,5,4,5,-3,8,2,-2,-8,4,-3,4,6,-7,10,-8,-8,-7,6,-6,5,-7,-7,-3,-1,4,-3,-5,-2,9,-10,-3,9,5,-3,6,-3,6,-1,-7,-3,4,7,5,4,3,3,6,-7,-7,10,-8,-6,2,-1,-8,10,-10,-3,-8,1,3,-7,-5,-10,5,-8,2,9,-9,-5,-7,-3,1,4,-5,1,6,-8,2,-3,-7,-2,-5,5,1,3,2,-5,-1,2,-3,-5,1,-9,-1,-2,3,5,6,2,-7,-7,2,-4,2,-9,7,3,-7,-10,5,5,7,8,2,-3,6,10,2,8,-9,9,3,3], dtype = "int16")#candidate|1801|(600,)|const|int16
call_1799 = relay.TupleGetItem(func_820_call(relay.reshape(var_1800.astype('int16'), []), relay.reshape(const_1801.astype('int16'), [10, 10, 6]), ), 1)
call_1802 = relay.TupleGetItem(func_823_call(relay.reshape(var_1800.astype('int16'), []), relay.reshape(const_1801.astype('int16'), [10, 10, 6]), ), 1)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_1805 = func_425_call()
call_1806 = func_425_call()
output = relay.Tuple([bop_1796,call_1799,var_1800,const_1801,call_1805,])
output2 = relay.Tuple([bop_1796,call_1802,var_1800,const_1801,call_1806,])
func_1816 = relay.Function([var_1800,], output)
mod['func_1816'] = func_1816
mod = relay.transform.InferType()(mod)
var_1817 = relay.var("var_1817", dtype = "int16", shape = ())#candidate|1817|()|var|int16
output = func_1816(var_1817)
func_1818 = relay.Function([var_1817], output)
mutated_mod['func_1818'] = func_1818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1729_call = mod.get_global_var('func_1729')
func_1731_call = mutated_mod.get_global_var('func_1731')
call_1826 = relay.TupleGetItem(func_1729_call(), 1)
call_1827 = relay.TupleGetItem(func_1731_call(), 1)
output = call_1826
output2 = call_1827
func_1832 = relay.Function([], output)
mod['func_1832'] = func_1832
mod = relay.transform.InferType()(mod)
output = func_1832()
func_1833 = relay.Function([], output)
mutated_mod['func_1833'] = func_1833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_1890 = func_425_call()
call_1891 = func_425_call()
func_1832_call = mod.get_global_var('func_1832')
func_1833_call = mutated_mod.get_global_var('func_1833')
call_1904 = func_1832_call()
call_1905 = func_1832_call()
output = relay.Tuple([call_1890,call_1904,])
output2 = relay.Tuple([call_1891,call_1905,])
func_1912 = relay.Function([], output)
mod['func_1912'] = func_1912
mod = relay.transform.InferType()(mod)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mutated_mod.get_global_var('func_1912')
call_1913 = func_1912_call()
output = call_1913
func_1914 = relay.Function([], output)
mutated_mod['func_1914'] = func_1914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1752_call = mod.get_global_var('func_1752')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_2006 = relay.TupleGetItem(func_1752_call(), 0)
call_2007 = relay.TupleGetItem(func_1753_call(), 0)
output = relay.Tuple([call_2006,])
output2 = relay.Tuple([call_2007,])
func_2022 = relay.Function([], output)
mod['func_2022'] = func_2022
mod = relay.transform.InferType()(mod)
output = func_2022()
func_2023 = relay.Function([], output)
mutated_mod['func_2023'] = func_2023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_2048 = relay.TupleGetItem(func_691_call(), 0)
call_2049 = relay.TupleGetItem(func_692_call(), 0)
uop_2056 = relay.sigmoid(call_2048.astype('float64')) # shape=(3, 5, 15)
uop_2058 = relay.sigmoid(call_2049.astype('float64')) # shape=(3, 5, 15)
uop_2064 = relay.sqrt(uop_2056.astype('float32')) # shape=(3, 5, 15)
uop_2066 = relay.sqrt(uop_2058.astype('float32')) # shape=(3, 5, 15)
output = relay.Tuple([uop_2064,])
output2 = relay.Tuple([uop_2066,])
func_2076 = relay.Function([], output)
mod['func_2076'] = func_2076
mod = relay.transform.InferType()(mod)
mutated_mod['func_2076'] = func_2076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2076_call = mutated_mod.get_global_var('func_2076')
call_2077 = func_2076_call()
output = call_2077
func_2078 = relay.Function([], output)
mutated_mod['func_2078'] = func_2078
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2149 = relay.var("var_2149", dtype = "float64", shape = (9, 11, 7))#candidate|2149|(9, 11, 7)|var|float64
uop_2150 = relay.atanh(var_2149.astype('float64')) # shape=(9, 11, 7)
bop_2152 = relay.bitwise_xor(uop_2150.astype('int16'), relay.reshape(var_2149.astype('int16'), relay.shape_of(uop_2150))) # shape=(9, 11, 7)
bop_2161 = relay.greater(bop_2152.astype('bool'), relay.reshape(uop_2150.astype('bool'), relay.shape_of(bop_2152))) # shape=(9, 11, 7)
output = relay.Tuple([bop_2161,])
output2 = relay.Tuple([bop_2161,])
func_2165 = relay.Function([var_2149,], output)
mod['func_2165'] = func_2165
mod = relay.transform.InferType()(mod)
mutated_mod['func_2165'] = func_2165
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2166 = relay.var("var_2166", dtype = "float64", shape = (9, 11, 7))#candidate|2166|(9, 11, 7)|var|float64
func_2165_call = mutated_mod.get_global_var('func_2165')
call_2167 = func_2165_call(var_2166)
output = call_2167
func_2168 = relay.Function([var_2166], output)
mutated_mod['func_2168'] = func_2168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2175 = relay.TupleGetItem(func_1912_call(), 1)
call_2176 = relay.TupleGetItem(func_1914_call(), 1)
output = call_2175
output2 = call_2176
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
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2229 = relay.TupleGetItem(func_1912_call(), 1)
call_2230 = relay.TupleGetItem(func_1914_call(), 1)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_2234 = relay.TupleGetItem(func_480_call(relay.reshape(call_2229.astype('float64'), [3, 5, 15])), 1)
call_2235 = relay.TupleGetItem(func_482_call(relay.reshape(call_2229.astype('float64'), [3, 5, 15])), 1)
var_2237 = relay.var("var_2237", dtype = "float64", shape = (3, 5, 15))#candidate|2237|(3, 5, 15)|var|float64
bop_2238 = relay.bitwise_xor(call_2229.astype('uint32'), relay.reshape(var_2237.astype('uint32'), relay.shape_of(call_2229))) # shape=(3, 5, 15)
bop_2241 = relay.bitwise_xor(call_2230.astype('uint32'), relay.reshape(var_2237.astype('uint32'), relay.shape_of(call_2230))) # shape=(3, 5, 15)
uop_2252 = relay.sin(var_2237.astype('float64')) # shape=(3, 5, 15)
output = relay.Tuple([call_2234,bop_2238,uop_2252,])
output2 = relay.Tuple([call_2235,bop_2241,uop_2252,])
func_2263 = relay.Function([var_2237,], output)
mod['func_2263'] = func_2263
mod = relay.transform.InferType()(mod)
var_2264 = relay.var("var_2264", dtype = "float64", shape = (3, 5, 15))#candidate|2264|(3, 5, 15)|var|float64
output = func_2263(var_2264)
func_2265 = relay.Function([var_2264], output)
mutated_mod['func_2265'] = func_2265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_2271 = func_446_call()
call_2272 = func_446_call()
func_742_call = mod.get_global_var('func_742')
func_744_call = mutated_mod.get_global_var('func_744')
var_2274 = relay.var("var_2274", dtype = "float64", shape = (150,))#candidate|2274|(150,)|var|float64
call_2273 = relay.TupleGetItem(func_742_call(relay.reshape(var_2274.astype('float64'), [2, 15, 5])), 1)
call_2275 = relay.TupleGetItem(func_744_call(relay.reshape(var_2274.astype('float64'), [2, 15, 5])), 1)
func_2022_call = mod.get_global_var('func_2022')
func_2023_call = mutated_mod.get_global_var('func_2023')
call_2298 = relay.TupleGetItem(func_2022_call(), 0)
call_2299 = relay.TupleGetItem(func_2023_call(), 0)
func_1752_call = mod.get_global_var('func_1752')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_2304 = relay.TupleGetItem(func_1752_call(), 0)
call_2305 = relay.TupleGetItem(func_1753_call(), 0)
var_2334 = relay.var("var_2334", dtype = "float64", shape = (150,))#candidate|2334|(150,)|var|float64
bop_2335 = relay.add(var_2274.astype('int32'), relay.reshape(var_2334.astype('int32'), relay.shape_of(var_2274))) # shape=(150,)
output = relay.Tuple([call_2271,call_2273,call_2298,call_2304,bop_2335,])
output2 = relay.Tuple([call_2272,call_2275,call_2299,call_2305,bop_2335,])
func_2341 = relay.Function([var_2274,var_2334,], output)
mod['func_2341'] = func_2341
mod = relay.transform.InferType()(mod)
mutated_mod['func_2341'] = func_2341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2341_call = mutated_mod.get_global_var('func_2341')
var_2343 = relay.var("var_2343", dtype = "float64", shape = (150,))#candidate|2343|(150,)|var|float64
var_2344 = relay.var("var_2344", dtype = "float64", shape = (150,))#candidate|2344|(150,)|var|float64
call_2342 = func_2341_call(var_2343,var_2344,)
output = call_2342
func_2345 = relay.Function([var_2343,var_2344,], output)
mutated_mod['func_2345'] = func_2345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_2374 = relay.TupleGetItem(func_611_call(), 1)
call_2375 = relay.TupleGetItem(func_613_call(), 1)
output = relay.Tuple([call_2374,])
output2 = relay.Tuple([call_2375,])
func_2377 = relay.Function([], output)
mod['func_2377'] = func_2377
mod = relay.transform.InferType()(mod)
mutated_mod['func_2377'] = func_2377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mutated_mod.get_global_var('func_2377')
call_2378 = func_2377_call()
output = call_2378
func_2379 = relay.Function([], output)
mutated_mod['func_2379'] = func_2379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_2445 = relay.TupleGetItem(func_2377_call(), 0)
call_2446 = relay.TupleGetItem(func_2379_call(), 0)
var_2448 = relay.var("var_2448", dtype = "uint16", shape = (9, 3, 12))#candidate|2448|(9, 3, 12)|var|uint16
bop_2449 = relay.floor_mod(call_2445.astype('float64'), relay.reshape(var_2448.astype('float64'), relay.shape_of(call_2445))) # shape=(9, 3, 12)
bop_2452 = relay.floor_mod(call_2446.astype('float64'), relay.reshape(var_2448.astype('float64'), relay.shape_of(call_2446))) # shape=(9, 3, 12)
func_1022_call = mod.get_global_var('func_1022')
func_1026_call = mutated_mod.get_global_var('func_1026')
var_2454 = relay.var("var_2454", dtype = "float64", shape = (32,))#candidate|2454|(32,)|var|float64
var_2455 = relay.var("var_2455", dtype = "int64", shape = (112,))#candidate|2455|(112,)|var|int64
call_2453 = relay.TupleGetItem(func_1022_call(relay.reshape(var_2454.astype('float64'), [8, 4, 1]), relay.reshape(var_2455.astype('int64'), [4, 28]), ), 5)
call_2456 = relay.TupleGetItem(func_1026_call(relay.reshape(var_2454.astype('float64'), [8, 4, 1]), relay.reshape(var_2455.astype('int64'), [4, 28]), ), 5)
output = relay.Tuple([bop_2449,call_2453,var_2454,var_2455,])
output2 = relay.Tuple([bop_2452,call_2456,var_2454,var_2455,])
func_2462 = relay.Function([var_2448,var_2454,var_2455,], output)
mod['func_2462'] = func_2462
mod = relay.transform.InferType()(mod)
var_2463 = relay.var("var_2463", dtype = "uint16", shape = (9, 3, 12))#candidate|2463|(9, 3, 12)|var|uint16
var_2464 = relay.var("var_2464", dtype = "float64", shape = (32,))#candidate|2464|(32,)|var|float64
var_2465 = relay.var("var_2465", dtype = "int64", shape = (112,))#candidate|2465|(112,)|var|int64
output = func_2462(var_2463,var_2464,var_2465,)
func_2466 = relay.Function([var_2463,var_2464,var_2465,], output)
mutated_mod['func_2466'] = func_2466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_2503 = relay.TupleGetItem(func_378_call(), 0)
call_2504 = relay.TupleGetItem(func_380_call(), 0)
output = relay.Tuple([call_2503,])
output2 = relay.Tuple([call_2504,])
func_2530 = relay.Function([], output)
mod['func_2530'] = func_2530
mod = relay.transform.InferType()(mod)
output = func_2530()
func_2531 = relay.Function([], output)
mutated_mod['func_2531'] = func_2531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_2553 = func_446_call()
call_2554 = func_446_call()
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
var_2557 = relay.var("var_2557", dtype = "uint16", shape = (324,))#candidate|2557|(324,)|var|uint16
call_2556 = func_500_call(relay.reshape(var_2557.astype('uint16'), [9, 3, 12]), relay.reshape(var_2557.astype('uint16'), [9, 3, 12]), )
call_2558 = func_500_call(relay.reshape(var_2557.astype('uint16'), [9, 3, 12]), relay.reshape(var_2557.astype('uint16'), [9, 3, 12]), )
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_2580 = relay.TupleGetItem(func_691_call(), 0)
call_2581 = relay.TupleGetItem(func_692_call(), 0)
output = relay.Tuple([call_2553,call_2556,var_2557,call_2580,])
output2 = relay.Tuple([call_2554,call_2558,var_2557,call_2581,])
func_2584 = relay.Function([var_2557,], output)
mod['func_2584'] = func_2584
mod = relay.transform.InferType()(mod)
var_2585 = relay.var("var_2585", dtype = "uint16", shape = (324,))#candidate|2585|(324,)|var|uint16
output = func_2584(var_2585)
func_2586 = relay.Function([var_2585], output)
mutated_mod['func_2586'] = func_2586
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2613 = relay.var("var_2613", dtype = "float64", shape = (1, 16, 9))#candidate|2613|(1, 16, 9)|var|float64
uop_2614 = relay.log(var_2613.astype('float64')) # shape=(1, 16, 9)
func_1752_call = mod.get_global_var('func_1752')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_2616 = relay.TupleGetItem(func_1752_call(), 0)
call_2617 = relay.TupleGetItem(func_1753_call(), 0)
bop_2625 = relay.bitwise_and(uop_2614.astype('uint64'), relay.reshape(var_2613.astype('uint64'), relay.shape_of(uop_2614))) # shape=(1, 16, 9)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_2632 = relay.TupleGetItem(func_480_call(relay.reshape(call_2616.astype('float64'), [3, 5, 15])), 0)
call_2633 = relay.TupleGetItem(func_482_call(relay.reshape(call_2616.astype('float64'), [3, 5, 15])), 0)
output = relay.Tuple([call_2616,bop_2625,call_2632,])
output2 = relay.Tuple([call_2617,bop_2625,call_2633,])
func_2634 = relay.Function([var_2613,], output)
mod['func_2634'] = func_2634
mod = relay.transform.InferType()(mod)
var_2635 = relay.var("var_2635", dtype = "float64", shape = (1, 16, 9))#candidate|2635|(1, 16, 9)|var|float64
output = func_2634(var_2635)
func_2636 = relay.Function([var_2635], output)
mutated_mod['func_2636'] = func_2636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_2655 = func_425_call()
call_2656 = func_425_call()
output = call_2655
output2 = call_2656
func_2663 = relay.Function([], output)
mod['func_2663'] = func_2663
mod = relay.transform.InferType()(mod)
mutated_mod['func_2663'] = func_2663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2663_call = mutated_mod.get_global_var('func_2663')
call_2664 = func_2663_call()
output = call_2664
func_2665 = relay.Function([], output)
mutated_mod['func_2665'] = func_2665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_2672 = relay.TupleGetItem(func_378_call(), 0)
call_2673 = relay.TupleGetItem(func_380_call(), 0)
uop_2676 = relay.atanh(call_2672.astype('float64')) # shape=(3, 5, 15)
uop_2678 = relay.atanh(call_2673.astype('float64')) # shape=(3, 5, 15)
func_2663_call = mod.get_global_var('func_2663')
func_2665_call = mutated_mod.get_global_var('func_2665')
call_2679 = func_2663_call()
call_2680 = func_2663_call()
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2684 = relay.TupleGetItem(func_1912_call(), 1)
call_2685 = relay.TupleGetItem(func_1914_call(), 1)
func_1832_call = mod.get_global_var('func_1832')
func_1833_call = mutated_mod.get_global_var('func_1833')
call_2695 = func_1832_call()
call_2696 = func_1832_call()
output = relay.Tuple([uop_2676,call_2679,call_2684,call_2695,])
output2 = relay.Tuple([uop_2678,call_2680,call_2685,call_2696,])
func_2697 = relay.Function([], output)
mod['func_2697'] = func_2697
mod = relay.transform.InferType()(mod)
output = func_2697()
func_2698 = relay.Function([], output)
mutated_mod['func_2698'] = func_2698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2076_call = mod.get_global_var('func_2076')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_2713 = relay.TupleGetItem(func_2076_call(), 0)
call_2714 = relay.TupleGetItem(func_2078_call(), 0)
output = call_2713
output2 = call_2714
func_2716 = relay.Function([], output)
mod['func_2716'] = func_2716
mod = relay.transform.InferType()(mod)
mutated_mod['func_2716'] = func_2716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2716_call = mutated_mod.get_global_var('func_2716')
call_2717 = func_2716_call()
output = call_2717
func_2718 = relay.Function([], output)
mutated_mod['func_2718'] = func_2718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_2730 = func_1529_call()
call_2731 = func_1529_call()
func_1111_call = mod.get_global_var('func_1111')
func_1117_call = mutated_mod.get_global_var('func_1117')
const_2744 = relay.const([-5,-1,1,9,-9,-3,-4,-8,8,10,-4,-2,8,-6,-6,-3,8,-6,-7,-6,-5,-3,-2,5,-7,-5,-7,8,5,-6,-9,-2,1,5,10,-6,10,7,10,-4,-8,-10,8,-2,-9,3,-5,4,2,8,3,-10,-3,9,-10,10,1,-5,-7,-1,-5,-6,-1,10,4,-7,2,-3,4,-8,-2,2,-10,2,6,-6,2,-5,6,6,5,-8,1,-2,3,7,10,-9,-8,10,8,9,9,3,-1,-7,2,-3,-7,8,-7,-5,6,-9,-7,-2,-6,5,5,3,8,-2,5,5,-2,-2,-10,8,-1,4,-8,4,-7,1,10,-8,6,-9,7,3,-9,-10,3,8,-7,-3,9,8,8,-10,7,-7,9,-4,-1,6,3,2,-4,-10,-3,5,-2,-9,-4,9,8,4,3,4,4,-6,7,-3,-8,-1,7,4,9,-10,-4,-4,-6,-2,6,-4,7,9,8,5,6,7,-10,-1,-4,-3,1,-1,-6,7,-10,-4,1,-2,-5,6,-3,-3,4,3,8,-6,-1,-9,1,-1,-8,-9,8,9,6,-5,10,3,5,-2,10,-1,7,10,-7,-1,7,4,-9,9,10,-8,3,2,5,-8,-4,-8,10,-2,-2,-1,-3,4,-8,1,6,-6,-9,6,4,1,-6,10,-10,4,5,10,-8,2,-7,4,10,-4,-2,-7,6,-6,-8,8,-9,9,-8,2,3,-4,6,-8,1,9,4,-10,3,-3,-2,-8,-5,-7,-6,-1,-4,1,-6,-8,3,-2,3,-7,8,5,5,3,2,5,8,9,4,3,9,8,-1,10,2,8,1,10,-1,-6,-10,1,6,3,9,1,-9,1,7,4], dtype = "uint16")#candidate|2744|(324,)|const|uint16
call_2743 = relay.TupleGetItem(func_1111_call(relay.reshape(call_2730.astype('float64'), [3, 5, 15]), relay.reshape(const_2744.astype('uint16'), [9, 36]), relay.reshape(const_2744.astype('uint16'), [9, 36]), relay.reshape(const_2744.astype('uint16'), [9, 3, 12]), ), 1)
call_2745 = relay.TupleGetItem(func_1117_call(relay.reshape(call_2730.astype('float64'), [3, 5, 15]), relay.reshape(const_2744.astype('uint16'), [9, 36]), relay.reshape(const_2744.astype('uint16'), [9, 36]), relay.reshape(const_2744.astype('uint16'), [9, 3, 12]), ), 1)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_2759 = relay.TupleGetItem(func_1912_call(), 1)
call_2760 = relay.TupleGetItem(func_1914_call(), 1)
func_1366_call = mod.get_global_var('func_1366')
func_1369_call = mutated_mod.get_global_var('func_1369')
const_2769 = relay.const([-1.131016,-0.252625,-9.756684,1.334568,1.248575,4.928312,1.906285,-7.015253,3.681157,-3.396214,-1.728499,-7.668942,-3.641529,-1.657190,-5.759227,-2.041952,3.257912,-3.153693,0.262548,6.433391,5.312682,4.403282,-7.115617,5.421820,-9.381675,-6.514577,-9.581614,-0.541964,-2.266782,-9.401899,-4.502327,5.131366], dtype = "float64")#candidate|2769|(32,)|const|float64
const_2770 = relay.const([4,-6,-7,-1,5,-9,-2,-6,-2,2,6,1,-3,-5,6,1,-10,-6,7,-5,9,-3,-2,3,6,4,-1,4,-5,-9,10,1,-7,6,-6,-4,7,-7,-8,1,-8,-10,9,3,2,4,-1,2,2,2,3,3,5,8,-2,9,-7,9,2,1,3,8,2,4,1,2,-1,-3,8,-10,-4,10,-8,7,-10,-6,6,9,-5,2,8,-8,-2,7,-4,-10,-6,10,-9,5,-9,-10,-4,-3,-1,-3,-10,10,-5,9,4,10,10,-5,8,6,-1,-2,-7,-4,-1,-9], dtype = "int64")#candidate|2770|(112,)|const|int64
call_2768 = relay.TupleGetItem(func_1366_call(relay.reshape(const_2769.astype('float64'), [32,]), relay.reshape(const_2770.astype('int64'), [112,]), ), 5)
call_2771 = relay.TupleGetItem(func_1369_call(relay.reshape(const_2769.astype('float64'), [32,]), relay.reshape(const_2770.astype('int64'), [112,]), ), 5)
output = relay.Tuple([call_2730,call_2743,const_2744,call_2759,call_2768,const_2769,const_2770,])
output2 = relay.Tuple([call_2731,call_2745,const_2744,call_2760,call_2771,const_2769,const_2770,])
func_2776 = relay.Function([], output)
mod['func_2776'] = func_2776
mod = relay.transform.InferType()(mod)
mutated_mod['func_2776'] = func_2776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2776_call = mutated_mod.get_global_var('func_2776')
call_2777 = func_2776_call()
output = call_2777
func_2778 = relay.Function([], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2795 = relay.const([[[-0.544696],[-0.081698],[1.789892],[2.313800],[2.692559],[8.622488],[8.369857],[-9.005961],[-2.488906],[6.902843],[-1.779333],[6.849968]],[[-9.293027],[7.912751],[1.593178],[-5.757502],[-9.552695],[3.995043],[3.914115],[-6.115763],[4.458252],[-1.245885],[-7.790074],[8.371147]],[[5.086189],[-0.263955],[7.028040],[9.389519],[6.338062],[6.101939],[6.972820],[-3.275755],[-4.726917],[-8.400189],[-9.527128],[-8.224448]],[[-3.121436],[-6.669152],[-7.324853],[6.846054],[-9.237003],[0.442018],[0.115533],[-7.615597],[2.865776],[0.682305],[6.046751],[-6.124956]],[[-4.155007],[-9.419125],[-7.579383],[-7.631545],[3.442502],[5.784166],[8.732673],[5.805465],[-9.576108],[6.313921],[0.082560],[-4.303783]],[[8.421689],[4.651351],[4.558987],[-7.159192],[-2.348164],[4.206771],[-5.864949],[0.285105],[-8.234062],[3.983600],[8.566044],[-1.068128]],[[0.428628],[9.399087],[0.220791],[5.840743],[-2.463880],[2.361758],[2.026850],[8.542941],[-6.956814],[-0.752623],[-1.310751],[-8.213732]],[[-3.788769],[-4.562041],[-9.356744],[1.244458],[-6.185856],[-4.318760],[-5.712153],[-9.779136],[8.554612],[-1.322718],[-9.916355],[-1.889298]],[[-2.949821],[5.068678],[3.866318],[-8.414802],[5.599757],[5.621148],[1.085404],[1.906513],[-3.975983],[4.809499],[9.722751],[5.563691]],[[0.746924],[0.051535],[6.216166],[6.975651],[-5.873513],[-1.675758],[-7.177765],[6.920514],[-0.242539],[-8.957106],[3.324765],[5.611002]],[[2.243703],[-5.335506],[2.630265],[2.079762],[-5.528922],[-3.798889],[5.394935],[6.675980],[-7.491798],[7.033766],[-9.610936],[-7.322805]],[[2.140923],[-6.302409],[-4.528157],[-5.789540],[-1.426414],[-6.134289],[-1.431798],[5.090205],[0.657437],[-7.068737],[0.483160],[-7.096328]],[[-3.220680],[-6.115028],[9.415201],[4.398254],[2.582984],[3.894379],[7.986590],[-8.112379],[7.517211],[7.739080],[-2.489612],[-0.822052]],[[-7.409749],[-2.417666],[-2.823419],[3.831187],[-5.799499],[-8.523043],[-8.001009],[8.773778],[4.455716],[5.993771],[-7.861790],[8.407518]],[[1.212663],[-7.880602],[2.465822],[7.422394],[7.362621],[8.335276],[-9.964879],[-0.691386],[-7.773959],[-4.188163],[-9.770132],[3.223333]]], dtype = "float64")#candidate|2795|(15, 12, 1)|const|float64
uop_2796 = relay.sinh(const_2795.astype('float64')) # shape=(15, 12, 1)
func_2076_call = mod.get_global_var('func_2076')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_2803 = relay.TupleGetItem(func_2076_call(), 0)
call_2804 = relay.TupleGetItem(func_2078_call(), 0)
bop_2820 = relay.left_shift(uop_2796.astype('int8'), relay.reshape(const_2795.astype('int8'), relay.shape_of(uop_2796))) # shape=(15, 12, 1)
func_2634_call = mod.get_global_var('func_2634')
func_2636_call = mutated_mod.get_global_var('func_2636')
var_2832 = relay.var("var_2832", dtype = "float64", shape = (24, 6))#candidate|2832|(24, 6)|var|float64
call_2831 = relay.TupleGetItem(func_2634_call(relay.reshape(var_2832.astype('float64'), [1, 16, 9])), 2)
call_2833 = relay.TupleGetItem(func_2636_call(relay.reshape(var_2832.astype('float64'), [1, 16, 9])), 2)
uop_2845 = relay.log2(uop_2796.astype('float64')) # shape=(15, 12, 1)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_2847 = relay.TupleGetItem(func_2776_call(), 5)
call_2848 = relay.TupleGetItem(func_2778_call(), 5)
func_2076_call = mod.get_global_var('func_2076')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_2856 = relay.TupleGetItem(func_2076_call(), 0)
call_2857 = relay.TupleGetItem(func_2078_call(), 0)
func_378_call = mod.get_global_var('func_378')
func_380_call = mutated_mod.get_global_var('func_380')
call_2858 = relay.TupleGetItem(func_378_call(), 0)
call_2859 = relay.TupleGetItem(func_380_call(), 0)
func_2165_call = mod.get_global_var('func_2165')
func_2168_call = mutated_mod.get_global_var('func_2168')
const_2862 = relay.const([1.999796,-5.031471,-6.406584,3.787548,-5.086056,-3.675794,2.258610,5.879599,9.452115,0.049655,-2.631747,-5.705039,-3.457145,5.792498,-6.769428,-0.247473,-3.849413,-4.259480,4.545638,7.184714,-3.082331,5.917190,-1.603405,4.371075,4.005232,2.108372,6.361965,-7.542124,-4.435181,-6.249471,-9.459463,-8.006807,9.473382,4.393458,2.678863,-1.985004,-8.148892,3.807430,-9.926247,-5.874233,7.101992,6.964109,6.584279,8.012966,-5.363898,-7.557852,-5.678054,0.367830,6.916492,-5.274477,0.743973,4.951177,-2.735144,-7.198164,7.381254,-4.208594,-2.897528,-2.542244,5.405488,3.795905,3.785522,-5.354498,-1.776908,1.459018,0.675305,-0.396284,-6.713489,-7.664423,-1.141092,5.150427,-4.523206,7.756594,-4.412854,-3.699870,1.693256,4.377973,-3.681085,-6.999264,4.595431,-3.078684,-9.619284,7.738113,-9.750051,0.467099,-7.691954,5.886660,9.710740,7.765671,-7.008477,9.304374,9.119368,-2.529958,5.604464,-1.693742,-6.954069,6.881403,-5.323648,8.623330,-4.120647,1.073895,3.968119,0.034860,5.325937,-0.922042,0.904635,6.847835,-7.301899,-1.892477,8.531029,-1.928863,1.651437,-0.233250,-9.227816,2.428289,-4.175582,9.735333,9.995965,-7.106426,1.047739,-1.743903,5.317783,2.828514,8.743898,4.452491,3.154464,-2.613565,9.316136,-5.881791,-1.665015,-6.972194,-0.639389,-2.539772,2.941799,7.586404,-6.889658,8.752401,0.479870,2.453499,-3.657660,3.976799,9.248301,-5.142247,-6.854129,-4.054307,-8.299519,-5.307843,3.110259,-4.436628,7.317587,9.471830,1.696409,0.857002,-6.240221,5.545089,3.188513,-9.971577,-6.345033,4.999670,2.854698,4.624554,3.210070,-3.368008,2.013286,1.167056,-6.970769,-4.999248,3.410957,6.894493,-5.776777,-9.538676,1.897052,-4.076989,4.798888,8.904161,-0.814614,7.797788,-5.296256,-7.699368,-6.738756,-1.572388,-5.653442,8.224370,1.226536,0.762910,0.279386,3.377851,-7.731384,1.099122,-6.699101,-1.048631,6.062060,-7.963481,-0.993167,5.825785,-3.860553,1.630375,-9.116162,-9.370687,6.870169,-8.043533,0.571974,-3.083232,5.505634,2.542498,-6.151473,-7.146772,2.005911,1.361667,4.508930,0.307495,-2.592814,2.849282,2.999704,-3.285765,4.065808,7.798496,7.079655,3.599847,5.369595,-3.280043,-3.372469,-0.039259,4.701663,7.779143,-1.790603,-1.665396,-3.720576,-8.911564,5.855814,-8.564145,7.883688,2.588226,6.502992,3.753314,9.417786,-0.971983,1.184390,-2.611248,-4.093473,8.148595,-4.590551,-7.378153,1.224002,-1.266855,9.856389,-7.750699,-2.519814,4.401578,-9.947435,7.794871,-1.919678,2.791455,-7.562784,-5.674898,-9.564796,5.838905,4.203538,6.164620,-3.054095,7.689241,-1.842043,-7.636715,7.485516,9.058185,0.907504,-2.477477,-7.798672,7.498536,7.907236,-5.222719,9.905188,-2.309201,4.859957,-7.251868,6.073687,3.439970,7.688764,-4.423750,-4.548637,-6.798755,-5.817119,0.027322,-2.774133,3.879085,4.996700,5.720561,-1.198708,3.734605,9.286741,5.412909,-8.935454,2.000321,9.851082,-4.433322,5.124281,7.695565,5.433006,-2.183279,1.861795,6.024610,9.503394,4.684973,-9.489964,5.369004,-0.244898,-8.534609,-8.228723,-7.486228,-7.770160,2.657140,0.884796,7.512465,0.074981,4.139863,-9.816347,6.182238,0.890910,8.016553,-5.745446,-1.931937,5.789908,1.735408,-9.967949,0.026557,-2.507907,-1.936357,9.043341,6.749707,6.180905,3.623723,3.131298,-1.667095,-5.346720,9.390313,-0.395559,2.685643,-3.521203,1.275021,4.335438,7.156545,9.436917,3.141453,-5.550475,-9.342138,7.083867,6.321518,-2.516568,-0.328573,9.389039,3.673210,0.110585,1.433376,0.299983,-8.385812,-9.332948,2.211783,8.909263,-4.568177,3.768235,4.455499,4.238972,8.171386,-6.187893,-6.189908,2.230196,-3.227431,-6.458641,5.762515,-3.094386,-9.508254,5.551788,8.033804,6.716705,-7.318024,-8.887401,0.695095,-4.103824,0.560474,-8.802510,-8.183499,-8.350632,-3.818150,0.431841,-3.192215,9.269913,-3.668796,-2.091875,0.570761,4.690982,-7.669893,-2.489128,9.157628,3.045227,9.179250,-0.926798,0.603946,-8.139957,-1.981864,5.856308,-1.110422,0.303190,-9.086528,-9.346517,1.222063,8.892316,6.128877,-2.659039,1.382821,4.296751,4.546832,-1.165082,-1.129268,6.170345,-6.650392,-7.264172,6.612177,4.267612,1.160689,-3.907694,-1.770836,1.127016,4.997620,-3.535094,2.446593,5.030033,-6.913952,9.310011,6.161524,5.145137,-1.365847,-0.671850,2.685343,8.189299,6.874022,-8.515269,2.926571,8.713322,5.511212,5.921989,2.115347,6.900090,5.690289,4.087478,0.097300,-8.843939,-2.238582,-0.809618,3.160088,-1.091101,2.369729,-0.502241,-9.915808,6.901071,2.217764,-6.438829,4.643661,-5.313383,1.599262,7.495322,-6.549764,-5.971623,-1.352456,1.358047,-1.340013,-6.613282,-5.860150,-1.280675,-6.567368,-9.732079,1.109877,5.327393,-4.754359,3.822207,0.085700,6.752643,-8.014853,-9.716704,-4.847503,-6.131313,1.615441,-9.248659,7.942733,1.929834,-6.604556,-2.096421,-9.815645,-0.792199,6.376614,-2.081911,7.579081,6.220427,8.889930,-3.548437,1.311145,-0.676039,-8.004221,-9.451475,-4.437488,4.943935,1.461161,-1.552461,0.593986,-6.224719,-5.199856,4.941433,-6.230266,6.391375,-6.891492,3.561375,2.327230,3.440267,-8.911477,7.624460,6.409228,6.291438,-6.793510,-8.251842,5.649819,0.525508,-9.574692,9.637575,5.327375,-9.121734,-8.825910,0.076449,-8.967918,2.340910,-7.558464,7.645461,-2.419687,-2.873013,-0.587717,-6.787934,7.104443,1.124597,0.233735,8.113429,7.560326,-0.630291,4.608867,1.395074,-2.972290,9.435056,-2.964105,-7.235464,9.734482,0.682757,-2.308448,7.759424,5.686292,8.324046,2.835331,6.072246,-8.061378,8.548224,1.841596,2.267475,6.921081,-9.791877,3.664292,-3.085281,2.288370,-0.782834,-2.847310,-1.734595,-0.808157,-7.030562,-6.385465,5.213993,0.807419,-7.449987,6.861656,5.528810,-8.274723,-3.194248,-7.636375,3.767397,4.114974,4.903075,5.734688,9.391529,3.189429,-0.209357,-8.964962,3.192849,-3.748201,-3.520145,2.115078,-5.493321,-6.137304,-0.681053,-0.316235,-6.301211,4.026519,1.217296,5.228999,3.954018,-6.164240,-3.112587,5.716673,-8.880759,-6.065778,3.299149,-2.216019,0.486924,6.574915,-1.185922,3.566827,4.495555,-3.894175,-3.221262,6.323389,2.168549,5.773080,-7.545519,5.295948,-6.720895,-3.959939,8.319510,5.370357,2.427547,-8.311647,-2.934484,-2.390393,3.281064,-5.773218,4.598688,2.263670,1.466854,-7.277586,8.994752,8.257134,8.557933,7.924639,-8.161591,-4.891085,9.076093,4.290596,-4.795354,6.680855,7.221346,7.482996,-5.246879,6.218942,0.413809,6.949382,2.168710,-0.471254,-9.814463,1.778681,2.524842,-7.044563,8.638509,-7.064521,-0.991600,8.530445,-9.665241,-6.610103,3.987521,-8.737089,3.964635,9.285922,-9.447014,-1.418836,9.741985,-0.128115,9.437206,-4.297124,-0.827047,-6.240161,-3.818110,-0.195581,6.769097,7.833990,-3.626788,9.963463,-7.913951,-1.753998,8.939134,6.219977,3.199198,8.466262,8.914263,8.832929,-8.965875,-5.061874,6.355842,4.847472,3.882228,6.127606,2.867986,2.274469,0.756665], dtype = "float64")#candidate|2862|(693,)|const|float64
call_2861 = relay.TupleGetItem(func_2165_call(relay.reshape(const_2862.astype('float64'), [9, 11, 7])), 0)
call_2863 = relay.TupleGetItem(func_2168_call(relay.reshape(const_2862.astype('float64'), [9, 11, 7])), 0)
bop_2865 = relay.subtract(uop_2845.astype('uint8'), relay.reshape(uop_2796.astype('uint8'), relay.shape_of(uop_2845))) # shape=(15, 12, 1)
output = relay.Tuple([call_2803,bop_2820,call_2831,var_2832,call_2847,call_2856,call_2858,call_2861,const_2862,bop_2865,])
output2 = relay.Tuple([call_2804,bop_2820,call_2833,var_2832,call_2848,call_2857,call_2859,call_2863,const_2862,bop_2865,])
func_2873 = relay.Function([var_2832,], output)
mod['func_2873'] = func_2873
mod = relay.transform.InferType()(mod)
mutated_mod['func_2873'] = func_2873
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2874 = relay.var("var_2874", dtype = "float64", shape = (24, 6))#candidate|2874|(24, 6)|var|float64
func_2873_call = mutated_mod.get_global_var('func_2873')
call_2875 = func_2873_call(var_2874)
output = call_2875
func_2876 = relay.Function([var_2874], output)
mutated_mod['func_2876'] = func_2876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2883 = relay.var("var_2883", dtype = "float64", shape = (14, 8, 13))#candidate|2883|(14, 8, 13)|var|float64
uop_2884 = relay.rsqrt(var_2883.astype('float64')) # shape=(14, 8, 13)
output = relay.Tuple([uop_2884,])
output2 = relay.Tuple([uop_2884,])
func_2887 = relay.Function([var_2883,], output)
mod['func_2887'] = func_2887
mod = relay.transform.InferType()(mod)
var_2888 = relay.var("var_2888", dtype = "float64", shape = (14, 8, 13))#candidate|2888|(14, 8, 13)|var|float64
output = func_2887(var_2888)
func_2889 = relay.Function([var_2888], output)
mutated_mod['func_2889'] = func_2889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_2917 = relay.TupleGetItem(func_580_call(), 0)
call_2918 = relay.TupleGetItem(func_582_call(), 0)
output = relay.Tuple([call_2917,])
output2 = relay.Tuple([call_2918,])
func_2921 = relay.Function([], output)
mod['func_2921'] = func_2921
mod = relay.transform.InferType()(mod)
mutated_mod['func_2921'] = func_2921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2921_call = mutated_mod.get_global_var('func_2921')
call_2922 = func_2921_call()
output = call_2922
func_2923 = relay.Function([], output)
mutated_mod['func_2923'] = func_2923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_2995 = relay.TupleGetItem(func_691_call(), 0)
call_2996 = relay.TupleGetItem(func_692_call(), 0)
output = call_2995
output2 = call_2996
func_2998 = relay.Function([], output)
mod['func_2998'] = func_2998
mod = relay.transform.InferType()(mod)
mutated_mod['func_2998'] = func_2998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2998_call = mutated_mod.get_global_var('func_2998')
call_2999 = func_2998_call()
output = call_2999
func_3000 = relay.Function([], output)
mutated_mod['func_3000'] = func_3000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2716_call = mod.get_global_var('func_2716')
func_2718_call = mutated_mod.get_global_var('func_2718')
call_3001 = func_2716_call()
call_3002 = func_2716_call()
uop_3010 = relay.erf(call_3001.astype('float64')) # shape=(3, 5, 15)
uop_3012 = relay.erf(call_3002.astype('float64')) # shape=(3, 5, 15)
func_404_call = mod.get_global_var('func_404')
func_406_call = mutated_mod.get_global_var('func_406')
call_3017 = func_404_call()
call_3018 = func_404_call()
output = relay.Tuple([uop_3010,call_3017,])
output2 = relay.Tuple([uop_3012,call_3018,])
func_3020 = relay.Function([], output)
mod['func_3020'] = func_3020
mod = relay.transform.InferType()(mod)
mutated_mod['func_3020'] = func_3020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3020_call = mutated_mod.get_global_var('func_3020')
call_3021 = func_3020_call()
output = call_3021
func_3022 = relay.Function([], output)
mutated_mod['func_3022'] = func_3022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_425_call = mod.get_global_var('func_425')
func_426_call = mutated_mod.get_global_var('func_426')
call_3029 = func_425_call()
call_3030 = func_425_call()
func_1055_call = mod.get_global_var('func_1055')
func_1058_call = mutated_mod.get_global_var('func_1058')
var_3059 = relay.var("var_3059", dtype = "float32", shape = (1980,))#candidate|3059|(1980,)|var|float32
call_3058 = func_1055_call(relay.reshape(var_3059.astype('float32'), [15, 11, 12]), relay.reshape(var_3059.astype('float32'), [15, 11, 12]), )
call_3060 = func_1055_call(relay.reshape(var_3059.astype('float32'), [15, 11, 12]), relay.reshape(var_3059.astype('float32'), [15, 11, 12]), )
uop_3061 = relay.asinh(var_3059.astype('float64')) # shape=(1980,)
func_2341_call = mod.get_global_var('func_2341')
func_2345_call = mutated_mod.get_global_var('func_2345')
var_3066 = relay.var("var_3066", dtype = "float64", shape = (150,))#candidate|3066|(150,)|var|float64
call_3065 = relay.TupleGetItem(func_2341_call(relay.reshape(var_3066.astype('float64'), [150,]), relay.reshape(var_3066.astype('float64'), [150,]), ), 3)
call_3067 = relay.TupleGetItem(func_2345_call(relay.reshape(var_3066.astype('float64'), [150,]), relay.reshape(var_3066.astype('float64'), [150,]), ), 3)
uop_3078 = relay.log10(uop_3061.astype('float64')) # shape=(1980,)
output = relay.Tuple([call_3029,call_3058,call_3065,var_3066,uop_3078,])
output2 = relay.Tuple([call_3030,call_3060,call_3067,var_3066,uop_3078,])
func_3084 = relay.Function([var_3059,var_3066,], output)
mod['func_3084'] = func_3084
mod = relay.transform.InferType()(mod)
var_3085 = relay.var("var_3085", dtype = "float32", shape = (1980,))#candidate|3085|(1980,)|var|float32
var_3086 = relay.var("var_3086", dtype = "float64", shape = (150,))#candidate|3086|(150,)|var|float64
output = func_3084(var_3085,var_3086,)
func_3087 = relay.Function([var_3085,var_3086,], output)
mutated_mod['func_3087'] = func_3087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1709_call = mod.get_global_var('func_1709')
func_1711_call = mutated_mod.get_global_var('func_1711')
call_3127 = relay.TupleGetItem(func_1709_call(), 0)
call_3128 = relay.TupleGetItem(func_1711_call(), 0)
output = relay.Tuple([call_3127,])
output2 = relay.Tuple([call_3128,])
func_3136 = relay.Function([], output)
mod['func_3136'] = func_3136
mod = relay.transform.InferType()(mod)
mutated_mod['func_3136'] = func_3136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mutated_mod.get_global_var('func_3136')
call_3137 = func_3136_call()
output = call_3137
func_3138 = relay.Function([], output)
mutated_mod['func_3138'] = func_3138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mod.get_global_var('func_1529')
func_1530_call = mutated_mod.get_global_var('func_1530')
call_3167 = func_1529_call()
call_3168 = func_1529_call()
func_1111_call = mod.get_global_var('func_1111')
func_1117_call = mutated_mod.get_global_var('func_1117')
var_3184 = relay.var("var_3184", dtype = "uint16", shape = (324,))#candidate|3184|(324,)|var|uint16
call_3183 = relay.TupleGetItem(func_1111_call(relay.reshape(call_3167.astype('float64'), [3, 5, 15]), relay.reshape(var_3184.astype('uint16'), [9, 36]), relay.reshape(var_3184.astype('uint16'), [9, 36]), relay.reshape(var_3184.astype('uint16'), [9, 3, 12]), ), 0)
call_3185 = relay.TupleGetItem(func_1117_call(relay.reshape(call_3167.astype('float64'), [3, 5, 15]), relay.reshape(var_3184.astype('uint16'), [9, 36]), relay.reshape(var_3184.astype('uint16'), [9, 36]), relay.reshape(var_3184.astype('uint16'), [9, 3, 12]), ), 0)
uop_3200 = relay.asin(var_3184.astype('float32')) # shape=(324,)
bop_3217 = relay.greater(uop_3200.astype('bool'), relay.reshape(var_3184.astype('bool'), relay.shape_of(uop_3200))) # shape=(324,)
output = relay.Tuple([call_3167,call_3183,bop_3217,])
output2 = relay.Tuple([call_3168,call_3185,bop_3217,])
func_3230 = relay.Function([var_3184,], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
var_3231 = relay.var("var_3231", dtype = "uint16", shape = (324,))#candidate|3231|(324,)|var|uint16
output = func_3230(var_3231)
func_3232 = relay.Function([var_3231], output)
mutated_mod['func_3232'] = func_3232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mod.get_global_var('func_830')
func_832_call = mutated_mod.get_global_var('func_832')
call_3281 = relay.TupleGetItem(func_830_call(), 0)
call_3282 = relay.TupleGetItem(func_832_call(), 0)
func_2921_call = mod.get_global_var('func_2921')
func_2923_call = mutated_mod.get_global_var('func_2923')
call_3291 = relay.TupleGetItem(func_2921_call(), 0)
call_3292 = relay.TupleGetItem(func_2923_call(), 0)
func_3230_call = mod.get_global_var('func_3230')
func_3232_call = mutated_mod.get_global_var('func_3232')
const_3311 = relay.const([[3,5,3,-2,-3,-3,-8,-4,5,8,4,-4,3,3,-7,-2,-10,8,-2,-6,7,-8,8,-8,3,-4,-1,3,-2,9,9,2,6,-7,-10,5],[-2,-6,2,1,1,10,6,3,-2,-1,-2,4,-5,-8,2,4,-6,-4,4,4,3,-7,-9,-10,3,-6,4,-4,-9,-4,8,6,-8,-4,6,-10],[-4,-9,-7,6,10,-4,-1,3,-5,-2,-9,-6,-9,-1,-8,7,8,-7,-6,-3,-4,-1,9,7,-5,6,-7,10,3,-2,-2,5,4,-5,6,7],[8,6,-5,9,10,-3,8,-5,-5,-5,6,9,3,-2,-3,-10,-8,8,9,-3,-3,-8,-10,-5,9,-5,10,-9,-9,4,2,5,-10,5,-10,-8],[5,-5,8,3,10,4,-4,-4,6,7,2,7,-2,-9,3,7,-5,4,-4,1,-6,5,10,3,9,-3,1,-3,4,-9,-1,-4,9,-10,-6,-9],[7,-2,-7,-2,-6,-9,5,-4,-8,-4,9,7,-6,3,7,-4,-9,-3,3,5,10,-8,10,4,5,6,7,-4,-10,5,-10,-6,-7,-7,4,-2],[8,1,-4,-3,-4,4,4,-4,-6,4,2,-7,8,-1,-6,9,5,-1,9,-9,-4,-6,-1,-5,-1,-3,6,4,-3,-8,-10,-2,-9,3,6,-2],[-2,-1,9,2,-4,5,-4,-5,5,-6,10,-1,3,-8,-3,1,1,2,9,-1,8,4,8,9,-3,-10,4,-4,3,-6,-4,-6,1,6,2,3],[-5,2,-6,-7,-5,-2,10,4,9,2,6,-10,-5,-9,6,-7,-10,-4,-9,7,-2,2,6,5,-7,1,-4,2,-9,-8,-4,-8,5,5,5,-7]], dtype = "uint16")#candidate|3311|(9, 36)|const|uint16
call_3310 = relay.TupleGetItem(func_3230_call(relay.reshape(const_3311.astype('uint16'), [324,])), 0)
call_3312 = relay.TupleGetItem(func_3232_call(relay.reshape(const_3311.astype('uint16'), [324,])), 0)
uop_3316 = relay.sin(const_3311.astype('float32')) # shape=(9, 36)
bop_3318 = relay.bitwise_xor(uop_3316.astype('int64'), relay.reshape(const_3311.astype('int64'), relay.shape_of(uop_3316))) # shape=(9, 36)
output = relay.Tuple([call_3281,call_3291,call_3310,bop_3318,])
output2 = relay.Tuple([call_3282,call_3292,call_3312,bop_3318,])
func_3322 = relay.Function([], output)
mod['func_3322'] = func_3322
mod = relay.transform.InferType()(mod)
mutated_mod['func_3322'] = func_3322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3322_call = mutated_mod.get_global_var('func_3322')
call_3323 = func_3322_call()
output = call_3323
func_3324 = relay.Function([], output)
mutated_mod['func_3324'] = func_3324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3325 = relay.var("var_3325", dtype = "float64", shape = (9, 2, 1))#candidate|3325|(9, 2, 1)|var|float64
uop_3326 = relay.log10(var_3325.astype('float64')) # shape=(9, 2, 1)
func_1816_call = mod.get_global_var('func_1816')
func_1818_call = mutated_mod.get_global_var('func_1818')
const_3342 = relay.const(7, dtype = "int16")#candidate|3342|()|const|int16
call_3341 = relay.TupleGetItem(func_1816_call(relay.reshape(const_3342.astype('int16'), [])), 1)
call_3343 = relay.TupleGetItem(func_1818_call(relay.reshape(const_3342.astype('int16'), [])), 1)
bop_3346 = relay.greater(uop_3326.astype('bool'), relay.reshape(var_3325.astype('bool'), relay.shape_of(uop_3326))) # shape=(9, 2, 1)
var_3356 = relay.var("var_3356", dtype = "float64", shape = (9, 2, 9))#candidate|3356|(9, 2, 9)|var|float64
bop_3357 = relay.logical_and(uop_3326.astype('bool'), var_3356.astype('bool')) # shape=(9, 2, 9)
func_1752_call = mod.get_global_var('func_1752')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_3373 = relay.TupleGetItem(func_1752_call(), 0)
call_3374 = relay.TupleGetItem(func_1753_call(), 0)
output = relay.Tuple([call_3341,const_3342,bop_3346,bop_3357,call_3373,])
output2 = relay.Tuple([call_3343,const_3342,bop_3346,bop_3357,call_3374,])
func_3381 = relay.Function([var_3325,var_3356,], output)
mod['func_3381'] = func_3381
mod = relay.transform.InferType()(mod)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3381_call = mutated_mod.get_global_var('func_3381')
var_3383 = relay.var("var_3383", dtype = "float64", shape = (9, 2, 1))#candidate|3383|(9, 2, 1)|var|float64
var_3384 = relay.var("var_3384", dtype = "float64", shape = (9, 2, 9))#candidate|3384|(9, 2, 9)|var|float64
call_3382 = func_3381_call(var_3383,var_3384,)
output = call_3382
func_3385 = relay.Function([var_3383,var_3384,], output)
mutated_mod['func_3385'] = func_3385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3450 = relay.var("var_3450", dtype = "float32", shape = (14, 8, 1))#candidate|3450|(14, 8, 1)|var|float32
var_3451 = relay.var("var_3451", dtype = "float32", shape = (14, 8, 3))#candidate|3451|(14, 8, 3)|var|float32
bop_3452 = relay.power(var_3450.astype('float32'), var_3451.astype('float32')) # shape=(14, 8, 3)
func_1752_call = mod.get_global_var('func_1752')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_3460 = relay.TupleGetItem(func_1752_call(), 0)
call_3461 = relay.TupleGetItem(func_1753_call(), 0)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_3464 = relay.TupleGetItem(func_3136_call(), 0)
call_3465 = relay.TupleGetItem(func_3138_call(), 0)
uop_3466 = relay.asinh(var_3450.astype('float64')) # shape=(14, 8, 1)
func_981_call = mod.get_global_var('func_981')
func_983_call = mutated_mod.get_global_var('func_983')
const_3469 = relay.const([-2,-1,3,7,-5,5,9,10,5,4,-5,-8,7,5,6,-6,-4,7,-5,9,1,7,-9,-1,4,8,10,-6,-7,3,-4,4,-5,5,-5,10,-10,6,-4,2,2,-7,-4,-9,3,-6,10,7,1,7,-8,-4,4,6,8,-7,-9,-3,7,-6,4,9,4,-3,-10,2,9,-6,9,2,1,-8,-4,-3,-2,3,-3,-2,-10,1,-5,-10,1,9,10,-9,-9,-3,-7,3,-5,5,-1,-4,-4,-3,-10,-5,-10,4,6,-3,10,9,2,7,10,-7,1,-6,-8,5,-3,-10,-7,-5,8,1,5,3,3,7,4,-8,5,1,2,-3,10,-2,-10,1,6,-3,-3,-10,-8,4,1,8,-6,1,-7,-7,-8,4,-5,-5,9,3,6,-8,10,-6,-4,7,3,9,2,7,-2,-7,5,9,-10,6,6,10,-8,9,1,5,5,6,-10,7,-3,1,8,4,2,6,5,-6,-2,-6,-2,-9,-7,-2,7,10,-8,9,-3,-6,2,5,-7,2,-7,-4,-1,3,7,4,-9,-3,-7,2,5,5,9,-7,-2,-8,9,-7,5,6,-9,6,-5,6,-3,-2,-8,8,-8,6,3,-10,-3,3,-8,10,1,5,6,10,10,2,10,7,-6,-9,-4,3,5,-5,-5,10,10,-4,7,-6,7,-6,7,-6,-4,-3,-3,6,-2,-10,-4,5,-6,-10,4,-3,-5,7,-2,-6,7,5,-6,9,-1,-5,9,-1,-8,1,7,2,-3,-6,3,1,1,-3,8,3,10,8,-7,-6,10,-6,1,10,10,-9,8,-4,-8,4,-8,9,6,-9,8,5,-7,6,-10,2,-4,2,2,1], dtype = "uint16")#candidate|3469|(324,)|const|uint16
call_3468 = relay.TupleGetItem(func_981_call(relay.reshape(const_3469.astype('uint16'), [324,])), 0)
call_3470 = relay.TupleGetItem(func_983_call(relay.reshape(const_3469.astype('uint16'), [324,])), 0)
uop_3472 = relay.erf(uop_3466.astype('float32')) # shape=(14, 8, 1)
uop_3482 = relay.log2(uop_3466.astype('float32')) # shape=(14, 8, 1)
uop_3484 = relay.exp(uop_3482.astype('float64')) # shape=(14, 8, 1)
output = relay.Tuple([bop_3452,call_3460,call_3464,call_3468,const_3469,uop_3472,uop_3484,])
output2 = relay.Tuple([bop_3452,call_3461,call_3465,call_3470,const_3469,uop_3472,uop_3484,])
func_3486 = relay.Function([var_3450,var_3451,], output)
mod['func_3486'] = func_3486
mod = relay.transform.InferType()(mod)
var_3487 = relay.var("var_3487", dtype = "float32", shape = (14, 8, 1))#candidate|3487|(14, 8, 1)|var|float32
var_3488 = relay.var("var_3488", dtype = "float32", shape = (14, 8, 3))#candidate|3488|(14, 8, 3)|var|float32
output = func_3486(var_3487,var_3488,)
func_3489 = relay.Function([var_3487,var_3488,], output)
mutated_mod['func_3489'] = func_3489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1752_call = mod.get_global_var('func_1752')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_3553 = relay.TupleGetItem(func_1752_call(), 0)
call_3554 = relay.TupleGetItem(func_1753_call(), 0)
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_3563 = relay.TupleGetItem(func_2377_call(), 0)
call_3564 = relay.TupleGetItem(func_2379_call(), 0)
output = relay.Tuple([call_3553,call_3563,])
output2 = relay.Tuple([call_3554,call_3564,])
func_3582 = relay.Function([], output)
mod['func_3582'] = func_3582
mod = relay.transform.InferType()(mod)
output = func_3582()
func_3583 = relay.Function([], output)
mutated_mod['func_3583'] = func_3583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2022_call = mod.get_global_var('func_2022')
func_2023_call = mutated_mod.get_global_var('func_2023')
call_3584 = relay.TupleGetItem(func_2022_call(), 0)
call_3585 = relay.TupleGetItem(func_2023_call(), 0)
output = relay.Tuple([call_3584,])
output2 = relay.Tuple([call_3585,])
func_3593 = relay.Function([], output)
mod['func_3593'] = func_3593
mod = relay.transform.InferType()(mod)
mutated_mod['func_3593'] = func_3593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3593_call = mutated_mod.get_global_var('func_3593')
call_3594 = func_3593_call()
output = call_3594
func_3595 = relay.Function([], output)
mutated_mod['func_3595'] = func_3595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1729_call = mod.get_global_var('func_1729')
func_1731_call = mutated_mod.get_global_var('func_1731')
call_3625 = relay.TupleGetItem(func_1729_call(), 1)
call_3626 = relay.TupleGetItem(func_1731_call(), 1)
func_1729_call = mod.get_global_var('func_1729')
func_1731_call = mutated_mod.get_global_var('func_1731')
call_3627 = relay.TupleGetItem(func_1729_call(), 1)
call_3628 = relay.TupleGetItem(func_1731_call(), 1)
output = relay.Tuple([call_3625,call_3627,])
output2 = relay.Tuple([call_3626,call_3628,])
func_3629 = relay.Function([], output)
mod['func_3629'] = func_3629
mod = relay.transform.InferType()(mod)
mutated_mod['func_3629'] = func_3629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3629_call = mutated_mod.get_global_var('func_3629')
call_3630 = func_3629_call()
output = call_3630
func_3631 = relay.Function([], output)
mutated_mod['func_3631'] = func_3631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3650 = relay.var("var_3650", dtype = "int32", shape = (8, 5, 11))#candidate|3650|(8, 5, 11)|var|int32
const_3651 = relay.const([[[-7,4,-9,3,-5,3,-10,-3,3,-4,-3],[1,8,-8,-3,1,-5,3,-1,1,5,2],[-7,4,10,-10,-4,-4,4,-7,8,-7,1],[6,8,8,5,9,-4,1,-3,-9,-6,7],[-5,-5,10,-6,3,3,-1,-3,10,8,6]],[[-9,2,4,-1,6,-7,6,4,-10,-4,-8],[-5,-3,4,-2,3,-9,-1,3,-6,-7,1],[-10,-7,-3,5,-10,-4,-7,6,-9,1,4],[-9,-2,-7,7,6,4,-10,-6,2,-5,-9],[-3,10,-4,9,2,4,-4,5,-10,1,-4]],[[-4,-7,-6,-1,5,-2,7,7,-3,-4,3],[9,-1,2,-4,4,9,-2,-4,-2,10,-3],[9,3,-8,-8,-6,2,-7,-1,1,8,-9],[-6,5,1,1,2,-5,-1,-3,6,7,9],[2,-4,-9,2,-3,10,-6,5,8,-7,-2]],[[6,7,-7,1,8,-5,-8,-5,2,-1,-9],[-7,6,4,6,2,-1,5,-5,3,-2,8],[-3,-10,-4,-9,-8,7,-10,7,-7,2,-10],[-8,-5,-2,1,5,-4,1,6,1,8,7],[-9,8,3,-7,-6,2,6,-10,-6,3,2]],[[8,-7,1,8,-5,-10,4,2,-8,4,2],[4,1,7,-9,-9,4,-5,1,-2,-10,-9],[6,6,10,6,4,-1,1,8,-6,7,2],[6,-7,2,-1,-4,10,4,1,-9,-9,7],[-2,-10,-1,10,-10,9,-7,7,-1,8,2]],[[-9,-10,-6,-3,-1,-8,-3,7,-4,-2,-8],[-7,-8,7,-8,-5,-2,9,6,-10,7,7],[9,-3,-4,-10,-3,-9,-3,-4,7,-2,-6],[4,-3,8,-4,-9,-10,-8,9,-7,4,5],[2,10,1,-6,-1,9,-7,-3,2,6,6]],[[6,-1,-10,-9,-2,-6,-8,-2,-4,-7,8],[-9,-6,7,-5,-5,10,4,-9,-7,-3,3],[8,6,-2,-4,-8,5,4,-6,-5,-9,-5],[7,5,-6,4,10,9,-5,-10,5,-2,1],[-10,-4,-6,-2,-8,-6,2,3,-5,10,-10]],[[7,4,7,-10,-1,-3,-7,-9,-1,-7,-10],[-1,7,-6,10,-1,-6,-6,-2,-1,-9,7],[-5,-9,3,-3,7,6,10,10,-9,-4,8],[8,-8,-3,5,-7,8,9,1,4,8,9],[-3,-7,-10,7,-10,-7,8,-7,2,5,7]]], dtype = "int32")#candidate|3651|(8, 5, 11)|const|int32
bop_3652 = relay.right_shift(var_3650.astype('int32'), relay.reshape(const_3651.astype('int32'), relay.shape_of(var_3650))) # shape=(8, 5, 11)
func_1609_call = mod.get_global_var('func_1609')
func_1614_call = mutated_mod.get_global_var('func_1614')
var_3656 = relay.var("var_3656", dtype = "uint16", shape = (324,))#candidate|3656|(324,)|var|uint16
const_3657 = relay.const(7, dtype = "int16")#candidate|3657|()|const|int16
var_3658 = relay.var("var_3658", dtype = "int16", shape = (300, 2))#candidate|3658|(300, 2)|var|int16
call_3655 = relay.TupleGetItem(func_1609_call(relay.reshape(var_3656.astype('uint16'), [324,]), relay.reshape(const_3657.astype('int16'), []), relay.reshape(var_3658.astype('int16'), [600,]), ), 2)
call_3659 = relay.TupleGetItem(func_1614_call(relay.reshape(var_3656.astype('uint16'), [324,]), relay.reshape(const_3657.astype('int16'), []), relay.reshape(var_3658.astype('int16'), [600,]), ), 2)
output = relay.Tuple([bop_3652,call_3655,var_3656,const_3657,var_3658,])
output2 = relay.Tuple([bop_3652,call_3659,var_3656,const_3657,var_3658,])
func_3660 = relay.Function([var_3650,var_3656,var_3658,], output)
mod['func_3660'] = func_3660
mod = relay.transform.InferType()(mod)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3660_call = mutated_mod.get_global_var('func_3660')
var_3662 = relay.var("var_3662", dtype = "int32", shape = (8, 5, 11))#candidate|3662|(8, 5, 11)|var|int32
var_3663 = relay.var("var_3663", dtype = "uint16", shape = (324,))#candidate|3663|(324,)|var|uint16
var_3664 = relay.var("var_3664", dtype = "int16", shape = (300, 2))#candidate|3664|(300, 2)|var|int16
call_3661 = func_3660_call(var_3662,var_3663,var_3664,)
output = call_3661
func_3665 = relay.Function([var_3662,var_3663,var_3664,], output)
mutated_mod['func_3665'] = func_3665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3582_call = mod.get_global_var('func_3582')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_3724 = relay.TupleGetItem(func_3582_call(), 1)
call_3725 = relay.TupleGetItem(func_3583_call(), 1)
uop_3744 = relay.sinh(call_3724.astype('float64')) # shape=(9, 3, 12)
uop_3746 = relay.sinh(call_3725.astype('float64')) # shape=(9, 3, 12)
bop_3747 = relay.logical_xor(call_3724.astype('uint32'), relay.reshape(uop_3744.astype('uint32'), relay.shape_of(call_3724))) # shape=(9, 3, 12)
bop_3750 = relay.logical_xor(call_3725.astype('uint32'), relay.reshape(uop_3746.astype('uint32'), relay.shape_of(call_3725))) # shape=(9, 3, 12)
uop_3771 = relay.cos(bop_3747.astype('float32')) # shape=(9, 3, 12)
uop_3773 = relay.cos(bop_3750.astype('float32')) # shape=(9, 3, 12)
uop_3781 = relay.atan(uop_3771.astype('float64')) # shape=(9, 3, 12)
uop_3783 = relay.atan(uop_3773.astype('float64')) # shape=(9, 3, 12)
bop_3798 = relay.mod(uop_3781.astype('float32'), relay.reshape(uop_3771.astype('float32'), relay.shape_of(uop_3781))) # shape=(9, 3, 12)
bop_3801 = relay.mod(uop_3783.astype('float32'), relay.reshape(uop_3773.astype('float32'), relay.shape_of(uop_3783))) # shape=(9, 3, 12)
bop_3803 = relay.power(uop_3771.astype('float64'), relay.reshape(uop_3744.astype('float64'), relay.shape_of(uop_3771))) # shape=(9, 3, 12)
bop_3806 = relay.power(uop_3773.astype('float64'), relay.reshape(uop_3746.astype('float64'), relay.shape_of(uop_3773))) # shape=(9, 3, 12)
var_3809 = relay.var("var_3809", dtype = "float64", shape = (9, 3, 12))#candidate|3809|(9, 3, 12)|var|float64
bop_3810 = relay.minimum(uop_3781.astype('int32'), relay.reshape(var_3809.astype('int32'), relay.shape_of(uop_3781))) # shape=(9, 3, 12)
bop_3813 = relay.minimum(uop_3783.astype('int32'), relay.reshape(var_3809.astype('int32'), relay.shape_of(uop_3783))) # shape=(9, 3, 12)
uop_3819 = relay.acosh(bop_3810.astype('float32')) # shape=(9, 3, 12)
uop_3821 = relay.acosh(bop_3813.astype('float32')) # shape=(9, 3, 12)
output = relay.Tuple([bop_3798,bop_3803,uop_3819,])
output2 = relay.Tuple([bop_3801,bop_3806,uop_3821,])
func_3822 = relay.Function([var_3809,], output)
mod['func_3822'] = func_3822
mod = relay.transform.InferType()(mod)
var_3823 = relay.var("var_3823", dtype = "float64", shape = (9, 3, 12))#candidate|3823|(9, 3, 12)|var|float64
output = func_3822(var_3823)
func_3824 = relay.Function([var_3823], output)
mutated_mod['func_3824'] = func_3824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3020_call = mod.get_global_var('func_3020')
func_3022_call = mutated_mod.get_global_var('func_3022')
call_3831 = relay.TupleGetItem(func_3020_call(), 1)
call_3832 = relay.TupleGetItem(func_3022_call(), 1)
const_3847 = relay.const([[[-0.973019,2.299798,6.353951,-5.384468,7.106235,-3.320317,7.103058,-0.808637,4.346369,2.269224,-6.625609,-8.002837,-6.460355,-3.577503,-9.432915],[-5.167239,3.897858,-8.962613,-2.446989,-3.859237,-7.307813,2.129423,-7.596033,4.102137,5.042828,1.874877,-6.552703,-6.412577,-1.610308,0.091306],[-7.692665,-7.915555,9.612035,-1.246158,3.942704,6.418277,3.802774,1.194416,-8.487460,0.827360,-1.467862,2.091136,9.798332,5.039788,-4.990519],[-1.432593,-3.602968,6.096032,-2.761008,-3.778447,-5.749173,9.612543,-8.045982,3.866102,7.730667,-7.333671,-2.775907,-8.655997,3.790883,6.431322],[-3.723257,-4.079889,-5.625129,-1.819304,9.574954,-8.556453,-3.161939,4.763932,7.160504,4.606658,-0.996920,-9.761638,0.968430,-1.672296,-9.171557]],[[-0.819082,7.759490,-6.255403,-4.466055,-8.945543,2.875333,-3.965641,-4.475002,-7.056846,-7.648422,-9.156374,7.517420,3.679195,1.256714,2.464482],[-8.560010,-2.662501,-2.849300,7.389702,9.666782,-1.842479,3.821328,-5.402030,-9.242226,2.678331,-4.052855,5.735983,-2.887904,-1.217262,-8.306282],[9.688919,-7.923617,1.665687,-5.001081,5.430761,-0.453236,-1.251511,-4.203708,-6.362873,5.644306,-4.470896,8.462639,3.892862,-1.196708,-0.807708],[5.940880,6.154359,6.471825,-4.746144,-4.335728,-9.618900,7.925724,-5.858613,5.192268,8.482234,-3.329320,5.833472,6.564224,2.730597,-6.306375],[3.740043,6.892414,2.163911,2.880885,8.265665,-7.793147,-9.726044,-1.375962,6.514402,2.064445,4.025665,-6.680354,-2.623992,5.369140,-5.393026]],[[7.059739,-4.307467,-9.217927,2.777663,0.486205,3.640845,-2.039921,-1.073987,-5.667655,3.586420,-3.471862,7.716345,2.885686,-0.124412,9.024332],[-5.542841,-2.823037,-2.805000,6.963452,-2.798223,-8.745811,-9.224349,-1.278942,7.472241,-8.605136,-7.492321,4.006090,-0.176639,2.497276,-8.863236],[3.885338,5.067607,7.440245,-5.499869,-2.013446,9.795385,8.167980,4.237577,-1.397268,-3.970016,7.508982,5.616884,8.361893,3.631307,9.029366],[8.387434,7.988882,-0.349895,-7.250009,7.805605,-2.821903,2.117529,-9.027034,2.676466,-2.362172,9.431454,-6.457174,-9.352982,-2.714783,7.898753],[8.520614,-6.551619,2.905618,4.579507,-2.596695,-9.002853,-8.215893,-7.350393,8.285876,2.975504,3.847538,2.421991,-3.233818,7.917389,-9.847675]]], dtype = "float64")#candidate|3847|(3, 5, 15)|const|float64
bop_3848 = relay.logical_or(call_3831.astype('bool'), relay.reshape(const_3847.astype('bool'), relay.shape_of(call_3831))) # shape=(3, 5, 15)
bop_3851 = relay.logical_or(call_3832.astype('bool'), relay.reshape(const_3847.astype('bool'), relay.shape_of(call_3832))) # shape=(3, 5, 15)
output = bop_3848
output2 = bop_3851
func_3859 = relay.Function([], output)
mod['func_3859'] = func_3859
mod = relay.transform.InferType()(mod)
mutated_mod['func_3859'] = func_3859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3859_call = mutated_mod.get_global_var('func_3859')
call_3860 = func_3859_call()
output = call_3860
func_3861 = relay.Function([], output)
mutated_mod['func_3861'] = func_3861
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3900 = relay.var("var_3900", dtype = "uint16", shape = (6, 10, 2))#candidate|3900|(6, 10, 2)|var|uint16
const_3901 = relay.const([[[-10,-10],[-6,-10],[-1,-8],[4,-3],[-7,2],[-9,9],[-5,-1],[1,7],[-4,6],[-7,-9]],[[-3,-5],[8,-1],[3,10],[2,-6],[-8,4],[-8,-3],[-7,-6],[-7,-5],[1,-7],[-9,4]],[[4,6],[3,2],[6,3],[6,10],[-6,10],[-9,-2],[-4,-9],[-1,-7],[-7,10],[-4,5]],[[10,-5],[3,2],[10,-1],[-8,1],[-5,-6],[-5,1],[5,-6],[-6,8],[7,2],[7,-9]],[[7,-7],[-6,8],[-9,6],[-7,-8],[8,1],[2,-8],[1,1],[4,-4],[-2,6],[9,9]],[[-8,6],[4,8],[-7,-4],[8,-10],[-3,-6],[2,10],[3,4],[-1,4],[10,7],[-3,5]]], dtype = "uint16")#candidate|3901|(6, 10, 2)|const|uint16
bop_3902 = relay.equal(var_3900.astype('bool'), relay.reshape(const_3901.astype('bool'), relay.shape_of(var_3900))) # shape=(6, 10, 2)
output = relay.Tuple([bop_3902,])
output2 = relay.Tuple([bop_3902,])
func_3907 = relay.Function([var_3900,], output)
mod['func_3907'] = func_3907
mod = relay.transform.InferType()(mod)
var_3908 = relay.var("var_3908", dtype = "uint16", shape = (6, 10, 2))#candidate|3908|(6, 10, 2)|var|uint16
output = func_3907(var_3908)
func_3909 = relay.Function([var_3908], output)
mutated_mod['func_3909'] = func_3909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_3949 = relay.TupleGetItem(func_3136_call(), 0)
call_3950 = relay.TupleGetItem(func_3138_call(), 0)
func_691_call = mod.get_global_var('func_691')
func_692_call = mutated_mod.get_global_var('func_692')
call_3955 = relay.TupleGetItem(func_691_call(), 0)
call_3956 = relay.TupleGetItem(func_692_call(), 0)
output = relay.Tuple([call_3949,call_3955,])
output2 = relay.Tuple([call_3950,call_3956,])
func_3968 = relay.Function([], output)
mod['func_3968'] = func_3968
mod = relay.transform.InferType()(mod)
output = func_3968()
func_3969 = relay.Function([], output)
mutated_mod['func_3969'] = func_3969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_3975 = func_446_call()
call_3976 = func_446_call()
func_981_call = mod.get_global_var('func_981')
func_983_call = mutated_mod.get_global_var('func_983')
var_3982 = relay.var("var_3982", dtype = "uint16", shape = (324,))#candidate|3982|(324,)|var|uint16
call_3981 = relay.TupleGetItem(func_981_call(relay.reshape(var_3982.astype('uint16'), [324,])), 2)
call_3983 = relay.TupleGetItem(func_983_call(relay.reshape(var_3982.astype('uint16'), [324,])), 2)
func_1498_call = mod.get_global_var('func_1498')
func_1503_call = mutated_mod.get_global_var('func_1503')
const_4014 = relay.const([[-9.360613,8.745069,-9.283535,-7.733704,-2.179311,-3.203630,-6.308805,-4.983758,-5.548012,9.495056,0.354009,-8.522511,-7.727814,-6.594979,-7.179325,8.026005,6.368244,-6.672543,4.358574,-3.473905,1.721546,2.343300,6.123507,-7.306753,5.507484,-9.985116,3.230110,-4.975097,4.997057,-6.838422,-0.807321,-2.707975,-4.691742,-1.297060,-6.027750,-7.089537,2.271786,8.138849,7.799940,-4.861571,7.115134,8.993443,-7.942780,-7.952703,-2.837879,0.731347,-5.602984,-3.538312,-8.154481,-4.094549,-0.028109,-8.237674,7.480527,-6.356630,6.856719,1.723366,-3.756922,-4.087368,-6.352993,-3.837856,8.580546,1.390450,7.171004,9.646136,-3.608668,-3.554653,-9.691883,2.789122,2.004268,-1.838811,-9.229884,7.322412,1.179265,0.185191,7.679079,-2.392753,-9.511268,-7.589132,-7.546373,9.379362,-8.595141,3.312039,6.245886,-0.972980,-2.277365,9.185573,-5.234730,8.119111,-9.616408,3.799063,-2.401343,8.307445,1.998267,2.781790,6.816214,9.261092,-7.277271,-4.101233,1.938694,-5.271155,1.370834,-7.728131,4.389977,5.327305,5.611818,1.510582,3.893198,-8.206845,-5.612111,-7.606412,-2.368596,1.045266,-0.582762,-5.527732,-8.578324,4.789229,1.099234,5.849274,-0.026385,-7.408342,3.071041,1.677933,-4.692170,-4.161520,0.443799,-5.605948,-8.914575,0.083168,9.702387,-9.763869,-0.358666,-8.255361,3.625018,-4.177587,-8.936435,5.260234,-9.549445,-3.468577,-4.893586,-9.132018,6.170757,-2.383181,-9.762478,-0.649229,1.604939,-5.694854,3.375694,7.322750,-1.916700,-6.925592,0.708029,4.744467,-1.824063,-0.764817,-3.288271,1.114010,-7.408075,1.108823,8.380044,-2.161729,-1.246630,-0.006970,8.043147,-5.191045,-3.461883,0.019512,1.759446,6.926948,-7.848513,-3.448686,-0.454648,8.408758,5.154680,-4.935594,-1.904045,-4.274099,4.662358,-3.081172,-1.519759,-4.428463,4.031031,-3.537302,-5.313503,4.701753,-5.547285,6.489693,3.846349,5.527441,6.093943,1.998208,-0.117665,-8.262387,-5.095449,2.459828,-4.024759,0.345155,6.212073,-2.325020,-0.756726,-3.502355,9.020700,2.964281,-6.188089,-8.402121,-8.374801,-2.588014,8.295179,-3.315183,7.128518,-0.089580,-7.195613,-2.670555,-6.076742,9.278609,-6.384956,8.655733,-0.529725,-7.692864,2.441526,-1.785922,-1.223675,-7.650623,-4.793422,9.353388,-0.035848,4.879922,-7.720827,-2.993331,-4.703776,5.748444,-0.254686,-9.643603,6.510944,4.868684,3.407514,2.138219,-7.655487,2.976333,-5.965382,1.388317,3.837394,7.405697,-6.168882,-9.434023,-4.280757,6.856594,-7.030669,0.404357,-2.448196,-2.736985,-3.592870,3.972492,8.633079,2.941914,4.966621,0.240934,6.189945,-0.806217,-1.613870,-1.754542,-4.060638,3.828427,-6.204430,8.515769,-3.900846,-7.050177,4.850853,4.779837,9.148934,-5.501998,2.325562,5.689675,2.309848,-2.540407,-7.277935,-5.717419,-9.950549,0.372311,-0.695520,5.975066,-9.346683,5.635720,7.223364,-6.198587,-6.646945,-5.607063,-1.221245,-4.948867,4.577142,-9.224424,-5.334992,0.950381,-2.948176,4.676549,9.807067,5.704325,-7.920060,1.461239,-3.754609,-6.895041,-9.779174,-9.102724,-5.164359,-6.850028,-5.844408,6.347931,5.901732,5.138017,0.032831,-2.801847,-4.516909,-0.017080,6.865031,-5.846404,-5.797999,-8.295440,1.127646,7.291462,7.932505,-0.062732,-2.529230,-8.552323,-0.029565,-3.472485,-3.142992,-9.112710,-3.741036,-7.965230,-9.932747,5.528442,4.794199,6.490007,6.338148,3.251359,2.636558,-8.978748,1.743160,3.513928,-8.819014,-0.826994,6.037013,7.352933,4.382688,3.837909,1.035539,-1.795622,-6.835577,8.247245,9.810770,-7.627413,-0.525831,-9.185732,-9.749796,2.052468,4.070598,3.632291,-6.567032,3.875456,-7.395380,3.903996,8.200432,3.237661,-9.088704,5.122573,8.292950,-5.526680,-6.954403,1.879054,-3.667532,-6.689089,-4.580042,-8.218362,-7.545047,3.522789,-6.616782,-6.211568,-4.156850,9.445806,7.557197,-5.609738,8.139396,-8.842915,-3.551473,-7.942057,8.739874,-7.728283,-1.160458,-5.094953,-4.421522,-1.679513,2.658181,2.275062,-4.912136,-9.190170,2.291671,-3.208881,2.779034,5.764909,-2.504373,-6.148913,-6.371783,-6.771618,-5.081578,1.158591,-8.461061,1.463623,7.818281,6.068444,-3.761126,9.324754,7.197662,-1.730985,-3.158751,-3.049256,9.888205,-9.569323,0.036065,-9.195543,-7.533874,6.373868,1.455320,-0.042155,4.620903,-8.307385,4.860295,1.343086,0.248200,3.650643,8.519599,9.657138,-5.118066,-5.792791,-2.997320,7.389984,8.077933,5.758969,-6.991931,3.968298,0.607153,2.964271],[5.185125,8.280660,-3.191001,-1.234526,-6.197371,-6.355105,-3.602252,8.449331,8.731368,6.545482,1.078320,-9.106665,-9.116558,2.252002,4.239034,-2.922249,8.536201,-2.984760,-7.982077,-5.028301,-5.313473,8.811164,5.654207,5.949503,-7.035206,6.141456,2.089591,1.016587,1.563760,2.127715,9.406263,8.655007,-2.617283,-7.260013,2.749285,3.219827,1.199413,-6.606805,2.432345,4.859768,-8.548154,4.506664,-4.663964,0.201605,9.089961,4.444370,-2.623271,-6.217152,-0.963773,2.475989,8.676753,0.223993,0.926293,7.374877,7.935240,-7.606749,-5.550836,7.983720,-8.976696,-1.305678,3.158149,-9.443960,4.340093,-9.052532,3.368818,1.575933,9.667541,9.380964,-0.645247,3.183938,-0.436585,3.412091,-8.728472,3.911663,0.190701,-0.735670,0.449335,-3.587952,7.459802,-6.556653,-1.790094,0.337090,-1.632355,-5.882840,-9.147764,-2.355418,-5.353688,4.566297,-8.753407,7.099353,-6.094018,5.811794,6.560749,-6.058784,-4.270254,8.588914,-4.329033,-1.203418,-0.305667,1.254408,8.815540,1.954079,4.970782,-5.490242,8.650800,0.818769,3.082072,-2.244369,-0.241218,-3.457734,9.584137,1.208117,-7.707308,1.346940,3.759352,1.024243,-2.655982,-7.748184,6.160494,-6.567067,-0.001839,1.036035,-0.037736,-0.941425,-1.530334,2.568480,3.125767,-4.782325,8.114873,-9.921105,-5.404613,8.382841,-0.408477,5.661621,-0.324454,-3.107439,0.890623,-3.658818,4.870518,9.543110,7.750691,-0.942632,2.955587,2.103273,-6.885224,6.116984,2.481459,2.506540,-3.645189,-3.486560,-1.539324,-5.171728,-9.651071,4.392089,3.440001,6.954799,-6.035896,1.629839,-4.830322,-2.199878,-1.365849,-6.128288,-7.560150,5.365121,-4.304733,1.572614,6.138689,-0.303273,-4.663446,8.818216,-4.713808,2.544074,-4.032249,2.620627,7.098494,7.903782,9.396972,1.513541,-3.365067,9.793076,-2.845136,6.517604,-9.590899,6.493779,-5.767476,-0.374082,-3.312192,7.249107,3.758900,2.471640,-0.260807,-4.914414,-6.743442,4.816340,4.829267,8.717110,3.605599,7.813285,5.423542,-8.959925,2.577341,-5.621679,-9.241470,9.018370,-9.673155,-2.655586,3.943736,6.513119,5.390800,-4.153236,6.024416,-7.626340,4.810220,-5.653512,9.862283,-1.160191,2.185995,-7.144036,-5.870927,4.752671,-8.877958,8.171512,0.326301,-1.315285,3.113975,1.390413,-5.450746,4.436377,8.370716,-2.098725,-9.803120,1.895626,-2.772948,-7.651869,0.999392,6.960500,4.765041,-0.119037,7.402630,8.113752,1.473303,5.091636,9.069462,1.133235,-6.529653,6.226304,-2.290046,5.461443,-7.988362,0.978348,3.531002,3.832228,8.386159,7.510076,-6.607069,8.782317,0.506337,-5.057604,8.749785,5.501732,2.208554,3.519266,-1.324185,-7.032022,-7.297691,-2.810082,5.812146,-5.099107,2.405647,9.800670,1.146746,-0.311445,-9.634665,0.282117,-9.765948,4.079784,8.538937,-5.197212,1.980919,-2.391452,-5.298723,-6.677220,-3.359316,6.566069,-3.316152,-5.345879,5.940396,1.605070,6.768680,-4.836151,4.313171,6.991865,-1.908304,-4.454719,6.664601,7.093432,-8.119696,1.935527,-9.258537,-3.097000,5.951644,-1.780014,8.767224,-8.004195,-6.561880,5.283132,2.476730,-1.772365,-5.434631,9.852463,9.348233,5.309332,-7.716864,9.337636,4.760185,-5.153791,-3.559835,-3.053184,-3.718614,-5.754439,5.253048,-2.734600,-3.385881,-5.614189,-5.809834,-0.373234,-5.399742,6.023416,-6.321718,8.567150,-6.487803,1.943368,2.807298,6.871948,-0.653952,-0.269393,4.846692,-4.291516,-5.371282,-7.794190,5.724849,-8.336404,-4.488980,-1.426098,-9.823873,1.266777,9.037632,0.255633,-7.474554,-8.139860,-9.284090,-7.549508,-0.732421,-7.071607,7.795497,8.683656,9.152607,-5.415003,2.128173,8.999853,-5.945695,-9.736611,0.905713,-0.356354,-8.915949,-3.015817,-2.594390,-3.271341,-9.523225,4.574071,0.777168,-0.309336,-0.159244,2.147328,0.741566,-4.666219,2.294488,-0.418631,-5.148666,-4.058079,9.067598,-3.920653,9.051991,-4.737510,6.677633,8.981980,-9.506216,4.745849,-1.156204,-8.935794,0.322123,1.830390,-1.495614,5.803681,7.564273,0.283250,8.229499,-9.577027,0.013787,-6.646163,-4.037365,8.074485,4.135670,3.740618,2.449905,0.004597,-6.256079,5.163994,-0.880895,-7.467886,-5.355363,9.983614,1.759455,-5.179418,-4.892166,4.540824,-0.630778,-9.135965,1.851554,3.062832,2.422065,-7.774515,-5.594788,-8.004801,-5.432953,-2.865873,2.294303,-0.240272,8.296137,9.876345,0.004862,-7.995314,6.078319,3.885463,-0.906171,-5.271046,-0.589211,-9.840542,-3.402099,5.189147],[9.000523,-4.882045,8.913252,9.903997,4.585183,0.515392,6.066023,9.548337,-7.408218,8.933736,2.868178,-6.735430,-4.626935,-1.432993,-2.636757,-2.793707,0.011160,-6.386186,7.453448,8.129814,-5.488368,-2.077410,-1.991594,-6.044216,-0.199812,-0.643759,0.157101,5.462253,8.186590,6.846310,-9.540358,1.488931,-5.071097,-6.026430,2.025211,-8.418357,-4.182618,9.835462,-3.915249,0.284267,1.607113,6.239335,5.124108,7.171404,-2.683074,-9.936119,-0.804734,2.107145,2.174798,-1.411846,9.504113,-6.617934,8.171295,8.353820,8.688156,4.821948,-8.032637,-7.977419,6.976515,-1.925860,-3.125328,-0.385972,-7.533597,4.579266,-6.354089,-8.341591,-6.293740,1.599491,-8.046952,-3.935541,-7.716880,-3.139120,-6.929479,-6.326852,-6.830877,7.912652,3.023667,1.755638,2.941962,8.071523,1.048992,-3.669015,-6.872735,2.583623,-1.376505,-7.360601,4.507499,3.521312,2.620401,-9.822857,-4.633111,-3.774503,5.397143,9.929140,-2.057946,-4.339735,-4.226315,-5.192454,7.839899,6.277440,8.068843,-0.649910,-3.444721,-6.715559,9.117170,-4.413832,-2.935125,3.811151,-0.152283,1.025773,0.944835,-7.321547,-3.135605,-8.254726,4.231521,9.836960,2.041971,4.996327,4.934297,-3.349360,-0.420198,-8.735149,3.545348,6.222610,-5.793611,1.258271,-4.101004,7.064073,-2.648518,-8.081758,6.572142,-6.033850,7.594443,-8.131829,9.488651,3.992268,8.828721,-7.994722,6.545500,9.722621,-1.118930,4.582592,-4.292378,7.223098,-8.921987,-2.670573,8.701547,3.414965,6.173769,3.559217,-7.083618,-5.608398,-3.495071,-6.899202,-3.673989,5.284342,-0.361681,-0.305327,7.885526,0.246117,6.899123,5.141138,-0.139743,-4.519784,4.294549,-3.256919,-8.965815,3.092284,-0.217712,4.117833,7.736409,1.050908,7.535151,2.767344,-9.643004,4.422453,-2.346857,-0.479386,7.782289,-2.930305,3.738079,-6.921442,-6.026103,-3.171230,6.219788,3.542758,5.691033,0.706062,-8.098091,9.842671,2.004094,6.125771,-5.198140,2.927813,-7.052776,-2.158401,-2.641430,3.722047,-6.147873,5.637853,5.399650,5.852451,-1.509345,-7.103614,6.402753,7.018346,-8.735757,-6.008053,-7.885101,-0.986206,-6.377494,-8.514600,9.286492,9.794829,-2.554259,4.129207,2.900251,-9.074932,8.815559,7.107974,-7.616960,-5.061240,1.314502,5.870834,-7.936375,-5.451040,-0.369879,7.509133,-5.840589,-8.352311,-3.776262,2.954859,-5.372133,6.172758,-4.130662,-5.604977,3.765014,7.468502,6.382623,-3.192009,-4.244920,-5.456194,-6.313598,-5.220114,-7.258514,1.723708,-5.708454,7.315873,-8.313167,4.896606,9.973826,7.756850,-1.509555,5.351769,-9.089753,0.947113,-5.888703,6.588213,7.103414,6.318153,-2.041249,-7.589369,4.318750,7.033006,-5.523661,-7.613570,-6.370940,-1.689172,-2.736055,9.473931,-7.561957,1.374645,-8.399380,0.288007,-8.809233,-9.439399,2.883317,-7.729252,-8.180340,-1.105508,-0.528156,-3.927490,-8.636617,1.981081,-2.907625,1.918378,0.220020,0.893468,-0.087587,6.897762,8.528386,5.682765,1.126539,-6.026472,-3.026706,-2.301119,8.036623,6.276726,-1.779924,8.605406,4.871428,1.162456,2.909902,9.065237,7.008452,4.311767,-9.091724,6.585070,-7.771973,9.285026,-7.792451,0.230554,-0.899522,7.373044,5.645827,7.165282,-1.770347,9.697167,2.095496,9.215109,0.563409,6.914541,8.263658,3.635042,-2.105596,-3.403046,0.265910,6.690021,2.237077,-8.399800,2.981632,4.940986,-9.272762,1.580555,7.120620,-1.593765,4.224108,-1.945961,-9.272843,-0.083798,-7.247351,5.832933,-3.477336,2.529728,2.357762,-9.875650,9.736916,-1.028381,-4.245796,4.701188,-6.820564,8.331353,-8.036728,2.274599,2.133762,9.674726,-9.173588,1.739985,5.196617,-5.405684,-4.444371,9.135392,3.727988,1.269966,-6.904607,0.748785,-8.224735,-4.939108,4.748434,1.468767,-9.775402,-6.841176,9.032381,2.911400,3.896242,-4.163719,5.339723,7.489804,4.117861,-4.581087,-5.061920,4.936973,-4.272441,9.869437,1.652742,0.543546,5.824413,-1.928705,6.783587,-0.516508,-1.291186,8.280832,-4.473723,-4.422829,2.094629,6.113699,-9.730527,3.038668,6.008521,-1.884738,1.985415,-4.379605,-9.098012,-7.101699,-0.591413,-4.721908,6.697275,-1.552115,-7.799897,2.668104,-1.221001,9.911608,2.396636,1.935550,4.427479,4.677364,4.357623,-5.139526,4.495980,-0.921404,7.541927,-6.080540,-9.308297,-7.017369,5.009880,-2.037109,6.917102,-7.190942,-7.222512,1.175448,-8.770121,8.903267,-4.761902,1.197861,-3.591391,3.816528,-4.845816,-2.348184,7.228041,3.691561],[-9.931256,-1.186820,-2.437848,0.818539,-3.513436,-8.476087,6.778968,8.603004,8.029473,2.688656,-2.627782,7.895211,-9.620787,7.464602,4.948622,-7.288647,-3.267626,4.416509,-2.526845,-2.780741,1.433506,6.409603,-3.072416,-8.658462,2.088558,9.416289,-2.469698,-9.058141,-5.222700,-1.643286,-2.574604,8.767104,6.173240,4.474046,0.103925,3.980717,4.137697,-1.863667,0.914489,6.336333,-2.403078,-5.164952,-5.388857,-9.147246,-1.500188,-2.397916,4.487661,6.008312,-2.904850,-2.702899,-2.996314,-1.398338,-3.805454,2.502304,8.153094,-8.662851,0.471881,-7.878047,9.606298,-4.090309,-0.185737,8.798321,9.810224,-2.304324,7.449100,5.739952,-5.455618,3.435021,-2.274378,-9.256231,-1.306240,-0.560913,3.818800,1.075954,7.239030,-3.336284,-6.170774,0.218837,4.199375,5.215469,4.308116,-3.071999,-3.193911,-2.765244,0.988276,-2.506587,-1.085786,5.921120,0.793521,-8.304406,9.876010,-8.145065,-5.014329,4.448018,-6.849394,0.437634,7.461991,2.329070,2.137018,5.751509,2.029097,-0.440883,-5.553578,0.221578,-3.295275,-6.632738,8.133164,0.941392,-5.066352,4.663819,2.758539,-1.123652,-1.184542,-7.574123,-5.801645,-4.775610,9.847253,3.360900,6.496424,-7.140120,-7.460629,1.589133,1.633012,-7.125479,8.564635,-0.058994,-2.655729,9.322420,2.627709,-8.719207,2.414117,1.597011,-1.881235,-9.016978,0.057349,6.529594,0.097097,5.206299,-8.498427,3.859772,5.462153,-5.774632,-8.818077,9.495934,-5.610982,4.982837,-4.278982,-0.485208,4.855959,-1.742248,4.669580,9.048060,-7.987903,-2.060968,-4.824599,-8.027719,0.298853,3.783670,5.746990,2.193675,-9.642305,1.613930,5.691921,4.181363,1.143670,-2.511766,-0.358550,9.458673,-5.788912,6.123705,7.213835,0.661516,-6.976265,4.825288,6.973186,4.396162,0.423717,-8.586840,7.954879,-8.849722,-8.297483,3.072451,-8.120588,8.480934,-6.477015,2.080732,5.943356,8.329112,0.438205,1.837473,1.166984,-5.108244,0.940945,-6.401702,8.404892,5.192270,5.077660,-6.622093,-4.228618,-7.723088,-6.407828,-9.387532,-6.020868,7.432302,-4.821292,-5.986249,-6.263142,0.150057,-9.440846,-2.254953,-6.133664,1.817511,-6.557265,9.619534,9.712183,-2.702145,9.713161,7.583110,-5.319870,0.762484,4.747641,-2.652139,-2.075277,-4.775614,2.504287,-1.744874,-4.853567,1.233505,4.385573,0.248481,2.907838,-1.807590,2.526354,-8.033645,8.538324,-6.908480,-1.782436,-6.191714,-1.418669,1.447596,7.746604,1.056018,8.882651,-8.710447,4.200087,0.803013,8.145852,8.555529,-7.169356,-5.455936,8.341703,-7.000704,-0.867615,2.378975,8.857184,-2.438989,-1.723497,6.165239,6.629341,3.710726,2.722938,5.529730,-4.931786,0.114689,-3.474605,-4.952968,5.661712,4.652729,7.626190,-7.660570,2.197872,0.104118,1.981511,9.245960,1.689136,6.370415,-7.019679,5.042739,-1.846314,4.299028,3.955291,-9.711220,-4.149992,-2.365227,-1.315275,9.377795,7.266704,-2.311341,0.746292,7.102880,-6.232178,6.155299,9.807003,2.975680,-4.259223,0.370761,5.025403,-8.576765,1.126161,8.603723,1.816319,-8.030659,-7.176696,4.316409,-7.462145,-3.770599,-4.410760,1.447101,-0.691932,4.845613,8.739763,-8.661817,-8.406677,9.785050,3.858515,-2.040121,1.650236,-2.053770,3.078486,0.840121,-1.117214,-5.077044,5.155974,6.679086,-4.174857,-2.585937,9.336563,-5.204325,4.362915,4.247824,8.461800,-4.903690,-6.432436,-3.438459,-8.374794,-3.381949,6.046644,7.094524,-0.419921,-7.316616,3.807130,6.727929,-5.119892,3.554281,8.246524,-2.052030,-9.168030,4.954319,1.804576,-8.945031,1.377218,3.084096,7.416540,7.814661,4.398276,-3.454316,1.018229,7.634549,-1.236283,3.883686,4.555983,-8.009413,-1.697115,4.160559,3.769563,-8.036994,-5.623111,0.886220,-2.932590,4.310454,-1.001282,4.899332,8.149270,0.915005,1.888447,1.951874,1.259089,-8.269021,6.714676,3.349188,8.624372,1.252976,2.521413,5.496958,-4.937236,0.984452,-8.840013,-8.723786,1.648522,5.162749,-4.575090,-7.515446,-9.728301,-6.745784,-5.860567,-7.774701,4.460945,3.438576,-2.010856,-2.778096,8.175773,-6.284697,-3.270848,-9.262124,-6.806792,-4.952256,-7.761818,-6.312171,9.142624,6.977314,1.997886,9.570413,3.943101,5.883907,5.896990,-8.770203,-4.756427,7.569399,0.428541,-3.090123,5.197889,6.789530,7.178098,2.561918,-6.894111,-4.710865,-1.299907,-8.895890,-1.275053,-6.421972,8.710981,1.204142,0.658880,0.373195,-0.452007,-3.563127,-4.663352,5.030648,-3.944075,1.197952]], dtype = "float32")#candidate|4014|(4, 440)|const|float32
const_4015 = relay.const([9.293180,-0.062490,-3.303359,-5.184890,9.452470,4.056010,-5.890201,-7.435767,9.125646,-8.468635,-5.954089,6.143155,-1.425970,1.399925,6.538452,-0.276502,-1.865751,-3.427371,3.196548,-9.766760,-9.936900,5.195575,-9.293238,8.737447,-3.841520,-9.821394,-5.794850,6.146184,-1.757903,-5.104655,-5.199435,-0.383408], dtype = "float64")#candidate|4015|(32,)|const|float64
const_4016 = relay.const([-1,-2,-1,-2,5,8,6,-4,-4,-10,-8,9,-8,-3,9,-9,-10,-3,-10,-7,-1,-6,6,-6,10,-7,2,-6,-4,-9,7,-5,-8,8,-3,4,10,3,-10,10,-6,-10,-2,9,5,1,7,-9,-4,5,-3,-5,9,-1,-6,-8,-8,3,3,6,-1,10,-4,-6,-7,10,-2,-3,1,-7,-6,1,1,4,7,4,8,7,4,-2,6,10,-5,6,-10,-4,10,-10,1,-7,-5,-6,6,7,-9,-10,1,3,-7,-3,-6,3,4,6,-9,-4,5,-7,5,2,3,9], dtype = "int64")#candidate|4016|(112,)|const|int64
call_4013 = relay.TupleGetItem(func_1498_call(relay.reshape(const_4014.astype('float32'), [10, 16, 11]), relay.reshape(const_4015.astype('float64'), [32,]), relay.reshape(const_4016.astype('int64'), [112,]), ), 3)
call_4017 = relay.TupleGetItem(func_1503_call(relay.reshape(const_4014.astype('float32'), [10, 16, 11]), relay.reshape(const_4015.astype('float64'), [32,]), relay.reshape(const_4016.astype('int64'), [112,]), ), 3)
func_500_call = mod.get_global_var('func_500')
func_504_call = mutated_mod.get_global_var('func_504')
call_4035 = func_500_call(relay.reshape(var_3982.astype('uint16'), [9, 3, 12]), relay.reshape(var_3982.astype('uint16'), [9, 3, 12]), )
call_4036 = func_500_call(relay.reshape(var_3982.astype('uint16'), [9, 3, 12]), relay.reshape(var_3982.astype('uint16'), [9, 3, 12]), )
output = relay.Tuple([call_3975,call_3981,var_3982,call_4013,const_4014,const_4015,const_4016,call_4035,])
output2 = relay.Tuple([call_3976,call_3983,var_3982,call_4017,const_4014,const_4015,const_4016,call_4036,])
func_4039 = relay.Function([var_3982,], output)
mod['func_4039'] = func_4039
mod = relay.transform.InferType()(mod)
var_4040 = relay.var("var_4040", dtype = "uint16", shape = (324,))#candidate|4040|(324,)|var|uint16
output = func_4039(var_4040)
func_4041 = relay.Function([var_4040], output)
mutated_mod['func_4041'] = func_4041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4081 = relay.var("var_4081", dtype = "float64", shape = (10, 10, 10))#candidate|4081|(10, 10, 10)|var|float64
uop_4082 = relay.exp(var_4081.astype('float64')) # shape=(10, 10, 10)
bop_4084 = relay.floor_mod(var_4081.astype('float64'), relay.reshape(uop_4082.astype('float64'), relay.shape_of(var_4081))) # shape=(10, 10, 10)
output = bop_4084
output2 = bop_4084
func_4089 = relay.Function([var_4081,], output)
mod['func_4089'] = func_4089
mod = relay.transform.InferType()(mod)
var_4090 = relay.var("var_4090", dtype = "float64", shape = (10, 10, 10))#candidate|4090|(10, 10, 10)|var|float64
output = func_4089(var_4090)
func_4091 = relay.Function([var_4090], output)
mutated_mod['func_4091'] = func_4091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mod.get_global_var('func_830')
func_832_call = mutated_mod.get_global_var('func_832')
call_4096 = relay.TupleGetItem(func_830_call(), 0)
call_4097 = relay.TupleGetItem(func_832_call(), 0)
func_3629_call = mod.get_global_var('func_3629')
func_3631_call = mutated_mod.get_global_var('func_3631')
call_4106 = relay.TupleGetItem(func_3629_call(), 1)
call_4107 = relay.TupleGetItem(func_3631_call(), 1)
output = relay.Tuple([call_4096,call_4106,])
output2 = relay.Tuple([call_4097,call_4107,])
func_4108 = relay.Function([], output)
mod['func_4108'] = func_4108
mod = relay.transform.InferType()(mod)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4109 = func_4108_call()
output = call_4109
func_4110 = relay.Function([], output)
mutated_mod['func_4110'] = func_4110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4202 = relay.var("var_4202", dtype = "float32", shape = (14, 4, 7))#candidate|4202|(14, 4, 7)|var|float32
var_4203 = relay.var("var_4203", dtype = "float32", shape = (14, 4, 7))#candidate|4203|(14, 4, 7)|var|float32
bop_4204 = relay.divide(var_4202.astype('float32'), relay.reshape(var_4203.astype('float32'), relay.shape_of(var_4202))) # shape=(14, 4, 7)
const_4209 = relay.const([[[-2.996755,5.568745,0.326178,8.281734,8.523306,5.864982,-6.425788],[8.352974,1.586092,-4.487115,-1.908742,-2.162611,-2.806868,-7.231890],[2.382771,1.982164,8.130613,-8.906541,6.320995,0.904702,-5.150484],[-7.079247,-8.961161,-5.741426,4.927010,-1.307197,-3.413655,-8.937906]],[[-7.591565,5.083651,7.893816,7.537890,7.479701,7.081094,5.011345],[-6.825954,-4.271421,-4.018025,-0.926548,-2.350030,3.956176,1.041757],[2.134922,8.418317,-7.229301,8.798333,3.069258,-7.527033,3.151646],[0.450861,-7.150232,-8.697567,9.340730,7.687209,9.772166,0.228435]],[[5.985962,-3.268257,7.885358,-6.301605,-2.194802,3.885083,-1.127460],[0.758365,9.677356,-9.184549,-9.772372,-5.971574,7.476322,1.253464],[3.463561,-4.810855,2.323847,8.857151,-2.081194,-1.341845,-0.915949],[-6.088046,-9.421443,-1.976545,-0.794868,8.160034,7.708018,-7.677646]],[[-3.474822,5.960631,3.436833,-1.006809,-0.380892,2.638030,4.737904],[-3.554866,3.183761,-9.964085,-0.561543,1.052295,5.913105,7.370583],[3.887935,5.891856,1.322415,9.248022,-1.282419,8.121156,-7.413024],[9.820091,-9.716561,3.332016,-1.489706,2.651325,-3.459351,-2.241607]],[[-8.432902,-5.755405,5.431229,8.742358,-2.498583,0.674874,-2.868111],[8.668126,8.638658,-0.778376,-6.979716,1.742313,2.033276,6.215279],[-1.109364,2.125638,3.258259,-3.619206,2.703636,9.593925,-9.774186],[4.756715,3.919119,1.576073,9.617430,4.201736,6.065808,8.249857]],[[8.167263,-3.954490,-8.940951,-0.802482,9.484882,-9.130147,-9.285999],[-8.224568,2.925734,7.791847,1.038582,2.062686,-2.435830,-4.225872],[-5.262456,-1.586368,9.929796,9.827788,-3.401319,0.518239,-8.602954],[7.670685,-1.896363,9.548687,3.050180,-3.435427,-7.579832,5.217381]],[[-3.464937,-3.591445,0.855372,0.486819,-1.910503,-0.949992,-8.126796],[-8.795251,-4.373551,-6.289900,-0.436113,-6.103048,-0.149752,-1.862943],[-6.768328,-5.010085,8.880516,7.399654,7.224957,0.962193,8.906591],[6.013456,-4.305931,-2.935623,4.053572,9.143717,6.129131,6.596941]],[[-2.538466,-3.723854,2.589253,-4.510340,8.495181,-7.476814,-6.915924],[-4.151586,9.449541,5.616132,-2.074897,-9.245923,-4.241184,9.645027],[0.862377,-4.470146,-4.293361,7.856764,2.699153,-3.998455,2.426615],[0.085476,6.042374,-4.343605,0.235908,-7.692051,8.566222,7.465424]],[[-8.391102,1.383094,8.476959,1.325171,-1.714168,-9.076937,-8.526994],[3.881996,4.985999,5.403537,-4.205480,8.175176,-5.207111,6.924900],[7.961544,1.450183,3.643796,1.273040,-7.799720,-5.912272,4.226804],[-9.987081,-5.482340,-6.717137,7.217410,-2.732013,7.197782,4.568267]],[[3.336541,7.775298,-8.033991,-8.698618,-4.428640,-1.439204,-3.658657],[6.858388,2.004393,-9.383309,0.020501,7.274842,-9.812854,6.374380],[-0.404537,7.510374,2.494855,-2.063259,-6.853270,-3.128127,-8.615284],[0.558386,6.959090,0.912382,5.073787,-6.251629,-9.533537,9.705938]],[[6.574375,-5.021885,6.362520,3.975992,-5.917138,-6.344912,-6.977995],[7.499931,-8.606584,-7.131771,-8.844648,-9.692991,8.225568,-3.183836],[7.722479,-0.819756,-6.488052,-2.395237,3.019855,8.035516,1.183151],[-7.052931,-0.012561,-0.272302,-1.612063,-2.677067,-7.391038,-1.456006]],[[-4.126346,3.258415,-1.991961,-0.734844,-2.956186,5.697421,9.939975],[-5.583728,-8.331244,-9.742646,-4.736369,4.014847,3.591607,5.776333],[0.516140,0.987967,1.286709,8.222451,7.952753,-1.928362,-8.977363],[6.444016,-4.473049,-2.587821,-4.924244,7.412099,6.703612,6.507779]],[[3.805572,5.335464,2.116253,-5.032963,1.915681,-0.762914,3.963417],[5.858404,-2.210727,3.414052,-3.150358,-6.102415,2.846799,2.861956],[-9.810300,7.372853,-5.175147,-7.566218,-9.915835,-5.432816,-9.935667],[-4.047202,6.968078,5.458163,-6.366926,6.428558,-0.292309,6.686638]],[[0.090939,5.581573,9.352450,9.144704,8.193927,7.858641,-4.877637],[0.569976,2.888579,3.301610,3.356023,-9.114022,9.856681,-5.751467],[4.896682,0.759104,0.799646,9.414321,-3.456480,-4.398837,-3.307463],[0.279282,6.633833,-2.609709,-2.239501,8.333891,-6.614860,5.646619]]], dtype = "float32")#candidate|4209|(14, 4, 7)|const|float32
bop_4210 = relay.equal(bop_4204.astype('bool'), relay.reshape(const_4209.astype('bool'), relay.shape_of(bop_4204))) # shape=(14, 4, 7)
func_1366_call = mod.get_global_var('func_1366')
func_1369_call = mutated_mod.get_global_var('func_1369')
const_4223 = relay.const([-9.441589,-4.564966,-9.750202,-5.440153,4.567212,-8.858886,0.589393,-8.829524,0.567956,-0.771580,-8.557271,-8.460653,-1.934553,-0.403083,-7.284218,8.825462,8.124911,-0.775538,1.517135,8.528802,-2.754657,8.209973,-1.911392,5.442001,7.258954,-1.615745,-1.645023,-8.618596,0.147799,0.660375,-2.016193,1.528740], dtype = "float64")#candidate|4223|(32,)|const|float64
var_4224 = relay.var("var_4224", dtype = "int64", shape = (28, 4))#candidate|4224|(28, 4)|var|int64
call_4222 = relay.TupleGetItem(func_1366_call(relay.reshape(const_4223.astype('float64'), [32,]), relay.reshape(var_4224.astype('int64'), [112,]), ), 1)
call_4225 = relay.TupleGetItem(func_1369_call(relay.reshape(const_4223.astype('float64'), [32,]), relay.reshape(var_4224.astype('int64'), [112,]), ), 1)
func_3486_call = mod.get_global_var('func_3486')
func_3489_call = mutated_mod.get_global_var('func_3489')
var_4227 = relay.var("var_4227", dtype = "float32", shape = (336,))#candidate|4227|(336,)|var|float32
call_4226 = relay.TupleGetItem(func_3486_call(relay.reshape(var_4224.astype('float32'), [14, 8, 1]), relay.reshape(var_4227.astype('float32'), [14, 8, 3]), ), 3)
call_4228 = relay.TupleGetItem(func_3489_call(relay.reshape(var_4224.astype('float32'), [14, 8, 1]), relay.reshape(var_4227.astype('float32'), [14, 8, 3]), ), 3)
output = relay.Tuple([bop_4210,call_4222,const_4223,var_4224,call_4226,var_4227,])
output2 = relay.Tuple([bop_4210,call_4225,const_4223,var_4224,call_4228,var_4227,])
func_4231 = relay.Function([var_4202,var_4203,var_4224,var_4227,], output)
mod['func_4231'] = func_4231
mod = relay.transform.InferType()(mod)
var_4232 = relay.var("var_4232", dtype = "float32", shape = (14, 4, 7))#candidate|4232|(14, 4, 7)|var|float32
var_4233 = relay.var("var_4233", dtype = "float32", shape = (14, 4, 7))#candidate|4233|(14, 4, 7)|var|float32
var_4234 = relay.var("var_4234", dtype = "int64", shape = (28, 4))#candidate|4234|(28, 4)|var|int64
var_4235 = relay.var("var_4235", dtype = "float32", shape = (336,))#candidate|4235|(336,)|var|float32
output = func_4231(var_4232,var_4233,var_4234,var_4235,)
func_4236 = relay.Function([var_4232,var_4233,var_4234,var_4235,], output)
mutated_mod['func_4236'] = func_4236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_830_call = mod.get_global_var('func_830')
func_832_call = mutated_mod.get_global_var('func_832')
call_4345 = relay.TupleGetItem(func_830_call(), 0)
call_4346 = relay.TupleGetItem(func_832_call(), 0)
output = call_4345
output2 = call_4346
func_4352 = relay.Function([], output)
mod['func_4352'] = func_4352
mod = relay.transform.InferType()(mod)
output = func_4352()
func_4353 = relay.Function([], output)
mutated_mod['func_4353'] = func_4353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2022_call = mod.get_global_var('func_2022')
func_2023_call = mutated_mod.get_global_var('func_2023')
call_4377 = relay.TupleGetItem(func_2022_call(), 0)
call_4378 = relay.TupleGetItem(func_2023_call(), 0)
output = call_4377
output2 = call_4378
func_4390 = relay.Function([], output)
mod['func_4390'] = func_4390
mod = relay.transform.InferType()(mod)
output = func_4390()
func_4391 = relay.Function([], output)
mutated_mod['func_4391'] = func_4391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3582_call = mod.get_global_var('func_3582')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_4451 = relay.TupleGetItem(func_3582_call(), 0)
call_4452 = relay.TupleGetItem(func_3583_call(), 0)
output = relay.Tuple([call_4451,])
output2 = relay.Tuple([call_4452,])
func_4460 = relay.Function([], output)
mod['func_4460'] = func_4460
mod = relay.transform.InferType()(mod)
output = func_4460()
func_4461 = relay.Function([], output)
mutated_mod['func_4461'] = func_4461
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4517 = relay.var("var_4517", dtype = "int32", shape = (10, 15, 2))#candidate|4517|(10, 15, 2)|var|int32
const_4518 = relay.const([[[2,5],[-6,-3],[-2,7],[1,-3],[-4,-5],[5,-5],[-8,9],[-3,-9],[8,8],[2,10],[10,-1],[-5,-4],[-1,8],[-4,8],[-7,-3]],[[-7,3],[6,-1],[5,-2],[1,10],[10,-6],[4,6],[-8,1],[-3,-6],[-7,-8],[-4,-3],[10,-6],[1,-6],[-1,-1],[-6,-6],[-3,-2]],[[3,9],[-8,-3],[3,3],[-3,4],[-6,-4],[-3,-3],[-4,-5],[-6,-7],[6,-9],[10,7],[9,-9],[-9,-6],[-3,4],[-5,-7],[6,10]],[[-9,-2],[-3,-9],[4,8],[-8,-6],[8,-3],[-2,7],[4,10],[5,3],[-7,1],[6,4],[-8,5],[-9,-2],[-5,-10],[-2,6],[-2,-7]],[[6,-3],[4,4],[-3,-2],[-1,6],[2,-7],[-3,-5],[5,-10],[-8,3],[6,1],[-1,-2],[5,7],[2,8],[-1,10],[3,10],[7,-4]],[[-6,2],[-5,4],[10,-10],[9,-3],[-1,5],[-5,8],[8,-5],[-8,9],[7,8],[4,8],[7,9],[5,8],[-2,-10],[8,4],[-5,-1]],[[9,7],[-3,8],[6,-3],[5,-8],[3,-8],[9,-1],[-7,-2],[-5,3],[5,10],[4,7],[-7,2],[2,2],[-6,-10],[10,3],[-6,10]],[[-8,-5],[-5,-2],[6,-9],[-10,3],[-1,-9],[7,3],[1,-9],[-10,8],[3,2],[-10,-7],[4,7],[4,-9],[-7,3],[8,-3],[1,5]],[[10,1],[7,-1],[8,3],[-3,9],[10,-6],[6,3],[5,-4],[8,10],[-5,3],[-4,10],[4,3],[2,7],[-10,1],[2,2],[9,-6]],[[9,7],[10,-7],[4,-6],[9,-6],[-3,-6],[-7,1],[-2,9],[-2,10],[-4,3],[-5,-8],[-8,-7],[-6,-9],[-7,-4],[-2,6],[-9,-5]]], dtype = "int32")#candidate|4518|(10, 15, 2)|const|int32
bop_4519 = relay.equal(var_4517.astype('bool'), relay.reshape(const_4518.astype('bool'), relay.shape_of(var_4517))) # shape=(10, 15, 2)
output = relay.Tuple([bop_4519,])
output2 = relay.Tuple([bop_4519,])
func_4523 = relay.Function([var_4517,], output)
mod['func_4523'] = func_4523
mod = relay.transform.InferType()(mod)
var_4524 = relay.var("var_4524", dtype = "int32", shape = (10, 15, 2))#candidate|4524|(10, 15, 2)|var|int32
output = func_4523(var_4524)
func_4525 = relay.Function([var_4524], output)
mutated_mod['func_4525'] = func_4525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2076_call = mod.get_global_var('func_2076')
func_2078_call = mutated_mod.get_global_var('func_2078')
call_4538 = relay.TupleGetItem(func_2076_call(), 0)
call_4539 = relay.TupleGetItem(func_2078_call(), 0)
output = relay.Tuple([call_4538,])
output2 = relay.Tuple([call_4539,])
func_4543 = relay.Function([], output)
mod['func_4543'] = func_4543
mod = relay.transform.InferType()(mod)
mutated_mod['func_4543'] = func_4543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4543_call = mutated_mod.get_global_var('func_4543')
call_4544 = func_4543_call()
output = call_4544
func_4545 = relay.Function([], output)
mutated_mod['func_4545'] = func_4545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1832_call = mod.get_global_var('func_1832')
func_1833_call = mutated_mod.get_global_var('func_1833')
call_4593 = func_1832_call()
call_4594 = func_1832_call()
output = call_4593
output2 = call_4594
func_4595 = relay.Function([], output)
mod['func_4595'] = func_4595
mod = relay.transform.InferType()(mod)
mutated_mod['func_4595'] = func_4595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4595_call = mutated_mod.get_global_var('func_4595')
call_4596 = func_4595_call()
output = call_4596
func_4597 = relay.Function([], output)
mutated_mod['func_4597'] = func_4597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1171_call = mod.get_global_var('func_1171')
func_1172_call = mutated_mod.get_global_var('func_1172')
call_4608 = func_1171_call()
call_4609 = func_1171_call()
var_4629 = relay.var("var_4629", dtype = "float32", shape = (3, 5, 15))#candidate|4629|(3, 5, 15)|var|float32
bop_4630 = relay.less(call_4608.astype('bool'), relay.reshape(var_4629.astype('bool'), relay.shape_of(call_4608))) # shape=(3, 5, 15)
bop_4633 = relay.less(call_4609.astype('bool'), relay.reshape(var_4629.astype('bool'), relay.shape_of(call_4609))) # shape=(3, 5, 15)
output = relay.Tuple([bop_4630,])
output2 = relay.Tuple([bop_4633,])
func_4636 = relay.Function([var_4629,], output)
mod['func_4636'] = func_4636
mod = relay.transform.InferType()(mod)
var_4637 = relay.var("var_4637", dtype = "float32", shape = (3, 5, 15))#candidate|4637|(3, 5, 15)|var|float32
output = func_4636(var_4637)
func_4638 = relay.Function([var_4637], output)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2998_call = mod.get_global_var('func_2998')
func_3000_call = mutated_mod.get_global_var('func_3000')
call_4673 = func_2998_call()
call_4674 = func_2998_call()
func_404_call = mod.get_global_var('func_404')
func_406_call = mutated_mod.get_global_var('func_406')
call_4680 = func_404_call()
call_4681 = func_404_call()
func_3582_call = mod.get_global_var('func_3582')
func_3583_call = mutated_mod.get_global_var('func_3583')
call_4697 = relay.TupleGetItem(func_3582_call(), 0)
call_4698 = relay.TupleGetItem(func_3583_call(), 0)
output = relay.Tuple([call_4673,call_4680,call_4697,])
output2 = relay.Tuple([call_4674,call_4681,call_4698,])
func_4712 = relay.Function([], output)
mod['func_4712'] = func_4712
mod = relay.transform.InferType()(mod)
mutated_mod['func_4712'] = func_4712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4712_call = mutated_mod.get_global_var('func_4712')
call_4713 = func_4712_call()
output = call_4713
func_4714 = relay.Function([], output)
mutated_mod['func_4714'] = func_4714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_582_call = mutated_mod.get_global_var('func_582')
call_4734 = relay.TupleGetItem(func_580_call(), 1)
call_4735 = relay.TupleGetItem(func_582_call(), 1)
func_2998_call = mod.get_global_var('func_2998')
func_3000_call = mutated_mod.get_global_var('func_3000')
call_4740 = func_2998_call()
call_4741 = func_2998_call()
output = relay.Tuple([call_4734,call_4740,])
output2 = relay.Tuple([call_4735,call_4741,])
func_4749 = relay.Function([], output)
mod['func_4749'] = func_4749
mod = relay.transform.InferType()(mod)
mutated_mod['func_4749'] = func_4749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4749_call = mutated_mod.get_global_var('func_4749')
call_4750 = func_4749_call()
output = call_4750
func_4751 = relay.Function([], output)
mutated_mod['func_4751'] = func_4751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4108_call = mod.get_global_var('func_4108')
func_4110_call = mutated_mod.get_global_var('func_4110')
call_4799 = relay.TupleGetItem(func_4108_call(), 1)
call_4800 = relay.TupleGetItem(func_4110_call(), 1)
func_3322_call = mod.get_global_var('func_3322')
func_3324_call = mutated_mod.get_global_var('func_3324')
call_4802 = relay.TupleGetItem(func_3322_call(), 3)
call_4803 = relay.TupleGetItem(func_3324_call(), 3)
output = relay.Tuple([call_4799,call_4802,])
output2 = relay.Tuple([call_4800,call_4803,])
func_4812 = relay.Function([], output)
mod['func_4812'] = func_4812
mod = relay.transform.InferType()(mod)
output = func_4812()
func_4813 = relay.Function([], output)
mutated_mod['func_4813'] = func_4813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1709_call = mod.get_global_var('func_1709')
func_1711_call = mutated_mod.get_global_var('func_1711')
call_4846 = relay.TupleGetItem(func_1709_call(), 0)
call_4847 = relay.TupleGetItem(func_1711_call(), 0)
func_243_call = mod.get_global_var('func_243')
func_248_call = mutated_mod.get_global_var('func_248')
const_4864 = relay.const([[-4.889024],[9.332769],[-0.379195],[2.126233],[-3.679661],[2.774642],[4.069722],[1.027540],[1.896888],[7.081999],[5.912719],[-7.903677],[-5.522060],[7.012350],[0.401517],[5.874791],[-5.838834],[1.220742],[2.541175],[1.906302],[-1.361462],[6.009089],[-4.586134],[3.550211],[9.495231],[8.472284],[-7.254447],[-1.884848],[4.220150],[1.001376],[-3.915662],[-2.366981],[1.650913],[1.159583],[-5.899683],[9.238197],[5.144578],[-4.511002],[0.378156],[8.581294],[6.442314],[0.792411],[-7.857936],[-1.723694],[-5.428909],[-3.910790],[-3.729750],[3.232529],[-1.474463],[-8.923759],[5.693490],[-6.903568],[1.458493],[-6.733182],[-0.736375],[2.385065],[-7.960664],[5.098448],[-1.408745],[-6.172322],[6.502092],[5.361338],[-8.816745],[-7.891114],[2.507223],[2.285799],[-7.268369],[2.923333],[9.371432],[-1.373578],[-4.972521],[7.788062],[3.121298],[1.619433],[-4.325691],[-1.855904],[5.693817],[2.909872],[-8.067694],[-1.794844],[6.283262],[-1.111994],[8.428333],[4.263057],[-3.745198],[-3.705243],[2.339887],[1.144356],[-9.865665],[-7.346125],[2.715621],[1.021875],[4.293484],[-6.475794],[-5.774042],[1.116411],[-8.030827],[5.344798],[-0.638787],[-2.294819],[-7.365390],[4.318777],[-1.390497],[-4.201076],[9.672154],[6.412278],[5.297007],[8.189603],[-3.146485],[-8.259925],[6.639911],[-3.320941],[-5.917293],[1.728159],[-3.374164],[3.207651],[9.069973],[-0.174604],[3.289557],[-8.125300],[7.016759],[3.183396],[-7.693144],[1.537002],[-7.511616],[3.835216],[-4.928525],[-1.810709],[3.218815],[5.116823],[9.525020],[8.561380],[9.873769],[1.914139],[-9.593086],[9.163150],[5.954066],[6.882004],[-2.743286],[-8.553017],[-3.949789],[-6.928932],[1.801748],[7.397519],[-5.036195],[-0.432789],[8.992209],[-2.299700],[4.847295],[-3.228186],[-3.479301],[-5.334563],[-2.300541],[9.309788],[-0.612760],[-2.715814],[-7.494054],[8.650906],[7.113219],[-6.261407],[3.387338],[2.839345],[-3.445408],[4.090989],[9.603533],[-3.680147],[-8.565877],[-1.995512],[-2.745936],[4.068568],[8.648874],[2.142340],[-5.912439],[-4.968180],[-7.645831],[4.955168],[4.246578],[-7.046592],[5.682894],[-9.161163],[8.498056],[-8.707570],[6.657522],[9.922399],[-5.903864],[-8.875408],[-8.449514],[8.104322],[6.519608],[-7.697904],[7.893403],[4.441142],[-2.690457],[-8.687426],[-4.245574],[9.630111],[3.472174],[2.812709],[-4.406705],[-7.877154],[3.204162],[-2.325374],[0.241745],[-1.549505],[3.229906],[-9.058126],[-7.597529],[-9.602127],[5.427919],[-6.212996],[8.258734],[-6.992569],[3.177272],[6.768264],[-4.777891],[2.215613],[-4.017932],[4.758287],[7.046881],[-8.560099],[-8.442628],[6.588885],[9.123607],[8.770559],[5.686866],[-5.616587],[9.846221],[7.999734],[-0.034860],[-4.356388],[1.193509],[-8.395582],[-8.768051],[0.152678],[9.371070],[-8.310855],[-6.084397],[-7.620328],[6.972295],[-5.971566],[-7.100432],[7.227273],[0.826462],[-9.627259],[8.016440],[-6.794159],[-1.972586],[9.606299],[-6.241353],[1.237171],[-7.840595],[5.305947],[0.058013],[-9.190341],[-6.700243],[2.615973],[7.660735],[-9.177741],[-1.185932],[-7.709282],[-2.034353],[-2.154400],[0.137892],[9.503727],[-5.811807],[6.303443],[-9.461093],[6.754469],[4.108984],[5.665355],[-4.964610],[-5.557839],[1.689448],[0.709175],[5.741849],[-8.571622],[-3.091205],[3.691377],[-6.464286],[-3.894960],[3.879438],[0.537480],[-8.172752],[4.912027],[3.224183],[5.087719],[-7.350116],[5.233664],[1.261534],[0.093960],[7.132881],[-6.170802],[-2.601782],[4.744635],[-3.067073],[7.864401],[-5.772090],[5.364233],[5.689054],[-1.598688],[3.537521],[-3.980599],[6.840999],[-9.502385],[-8.407850],[2.358637],[3.084564],[-3.797282],[5.888774],[-1.355624],[2.527400],[2.722782],[-4.826719],[-7.366417],[-2.378430],[-1.523159],[2.969462],[9.853903],[6.580861],[3.410775],[0.144843],[6.217118],[-4.413960],[-7.791351],[4.447417],[5.752754],[-2.133515],[-1.905727],[5.152249],[-1.242861],[9.845460],[-0.650510],[1.962957],[4.950223],[0.514172],[7.732658],[-8.725837],[5.366924],[-0.603360],[-4.111897],[-9.218140],[-2.118059],[9.368539],[0.915206],[6.322187],[-5.298790],[1.886852],[4.588806],[-8.781180],[9.523747],[4.513945],[-0.831210],[3.500742],[-3.210774],[8.822624],[7.538275],[-8.976077],[-4.509037],[6.327586],[3.854768],[3.843469],[2.837718],[-1.886015],[6.507516],[-8.062967],[-1.789643],[9.502364],[2.251162],[-1.492302],[-8.633164],[-5.287183],[8.086009],[9.484243],[-2.496423],[8.396925],[-0.699250],[9.203554],[9.629318],[-0.754613],[-5.580051],[6.336433],[2.081017],[1.419899],[0.187326],[-0.015550],[7.141089],[-6.794574],[-4.546329],[-9.047116],[-8.028098],[-9.102931],[-9.741460],[-9.205391],[5.667741],[7.117617],[3.556019],[-2.725106],[9.257595],[3.887949],[6.613200],[5.208151],[2.172229],[2.251469],[2.477119],[-3.659870],[5.323427],[-5.582327],[8.381095],[-7.928809],[-3.709009],[-5.597354],[-2.194496],[-5.752757],[1.843909],[4.153688],[4.706364],[6.771091],[-3.152635],[-4.793351],[2.023410],[1.518584],[0.178485],[-2.504587],[-7.757016],[4.737879],[-8.168568],[0.026556],[-6.525499],[1.131455],[5.840961],[-6.984963],[3.949379],[5.412984],[-7.778046],[8.849397],[9.074689],[2.873720],[4.216635],[5.536071],[-2.227074],[-3.540313],[-5.676033],[9.090130],[3.168384],[-2.060966],[0.140389],[1.291892],[7.392371],[-4.188963],[5.207933],[6.251424],[-0.076553],[8.741787],[-2.052991],[-5.618112],[-0.812695],[-7.907040],[-3.013579],[8.613679],[-1.375816],[-7.359923],[5.794143],[-7.413825],[5.461400],[-2.152427],[-3.503986],[3.614047],[-4.040732],[-9.511819],[4.300027],[2.030076],[6.918800],[-4.061464],[-1.024723],[0.165721],[-5.121944],[-5.197663],[-2.674078],[-7.222839],[-4.511288],[-5.024177],[-1.199028],[5.777129],[-1.266012],[4.585189],[-2.643336],[8.399103],[-4.031306],[9.859271],[-5.380110],[3.048076],[5.795416],[-2.978269],[-8.931688],[6.731487],[3.966380],[-6.129884],[8.641024],[1.123897],[6.656937],[9.239967],[7.584672],[-1.788020],[-5.491992],[-5.750749],[-0.705915],[1.290543],[-2.270142],[1.115056],[-3.888893],[0.194693],[-2.969206],[2.370279],[2.962613],[-2.909306],[-2.760275],[6.257058],[-5.139197],[2.166036],[5.703252],[5.020295],[-9.298348],[7.865229],[-9.769688],[5.849585],[5.458990],[5.692614],[-7.724901],[6.019908],[1.360495],[7.730930],[5.654663],[7.622547],[-0.655529],[5.546051],[0.106779],[0.836931],[0.003291],[-1.251882],[-9.647173],[3.354640],[-9.316609],[0.756758],[2.700779],[-8.342688],[-5.371803],[-8.880804],[-8.440584],[-9.940348],[2.061057],[7.686858],[-6.353200],[-3.714930],[4.178101],[-8.906852],[-6.356621],[-7.844869],[-1.708765],[-6.448742],[-0.642421],[-7.214423],[-0.267784],[7.708612],[-5.769763],[0.660197],[7.200263],[-7.573150],[1.870099],[7.371407],[5.144236],[-6.066258],[8.057810],[-1.079315],[2.398454],[-6.391641],[-1.628057],[-5.144072],[0.787879],[8.015820],[1.446074],[6.886634],[5.387598],[3.382641],[-6.681487],[-4.035556],[-2.295052],[-4.822147],[8.275393],[0.106468],[3.680365],[-7.151866],[-5.141734],[-9.929709],[-7.103627],[6.340138],[-8.804203],[-2.157810],[7.664994],[-0.890594],[1.238322],[3.102290],[-6.555762],[1.596590],[2.187488],[-8.093816],[-8.152424],[-3.937557],[7.442330],[5.488711],[-7.022302],[-3.954664],[9.564783],[7.414270],[-8.878677],[9.922650],[-4.612255],[7.790639],[-1.039837],[-3.233404],[7.422517],[-4.969666],[4.217045],[-5.465487],[4.086963],[1.139272],[-6.094976],[-7.522586],[-1.127875],[-4.634526],[0.354858],[-0.670372],[4.703330],[-2.837009],[6.657329],[9.231230],[5.817414],[-6.605328],[-1.496707],[-5.543045],[-0.578395],[8.464383],[7.575865],[9.560729],[6.244358],[-7.173833],[9.125378],[-7.318950],[-6.054149],[-7.894093],[1.165574],[-8.270233],[2.696246],[-6.045610],[2.263050],[3.213823],[-8.444539],[-9.113656],[-7.665691],[8.647953],[-9.455867],[-5.340703],[7.124989],[-4.907531],[-2.847353],[4.657486],[-8.146752],[-2.916315],[-1.901911],[8.003640],[7.674815],[-5.483277],[1.629206],[5.072286],[-2.267700],[-8.339884],[-8.917533],[-9.215638],[4.411156],[3.040681],[1.647724],[-0.578705],[-7.164395],[6.174938],[2.038556],[-9.086829],[8.422027],[-0.314899],[-1.827551],[-1.067246],[-7.145851],[6.152538],[1.456527],[-1.063694],[-3.557008],[-5.057855],[-8.056020],[8.963196],[-6.289219],[-0.749877],[1.603755],[-2.568747],[3.876537],[8.965970],[3.796497],[-6.346163],[-5.796215],[-8.219173],[2.276871],[4.959754],[1.801949],[0.332741],[-4.499506],[-0.601010],[3.028402],[-1.555684],[-3.070263],[2.131692],[8.867923],[3.122668],[-5.780318],[-6.721175],[4.493017],[-3.235664],[-2.952903],[-5.778184],[-1.902362],[7.065297],[-8.856456],[2.069157],[-9.152685],[-4.417804],[-5.967821],[-3.116381],[-5.863395],[-0.156461],[3.902482],[-1.702070],[-1.688914],[7.755604],[-4.744089],[-0.680934],[9.466643],[4.493214],[4.386226],[7.162166],[-2.076857],[-5.159028],[4.993409],[-6.628571],[-0.534132],[-6.137797],[4.522567],[-2.332492],[-8.062374],[-1.212864],[2.811547],[8.473580],[7.601727],[-7.620651],[3.077346],[-7.386643],[3.490320],[-2.449804],[-3.289016],[3.522523],[-5.815960],[-8.983447],[-4.481005],[0.573472],[9.252420],[7.987582],[-2.040862],[2.853590],[4.610317],[-2.482558],[-2.201772],[-0.585274],[-6.997597],[-6.712805],[2.061867],[6.036281],[-5.102425],[1.741362],[6.451581],[9.635563],[4.224657],[3.055285],[1.603932],[2.083162],[2.705296],[1.107131],[-3.729300],[8.148083],[-6.541429],[0.362963],[1.431577],[2.198697],[5.423955],[-3.806666],[9.193380],[3.872526],[-0.569324],[-5.056934],[2.710803],[-2.964841],[-4.018419],[-5.515133],[0.459274],[0.159091],[-3.593574],[2.636229],[6.061487],[3.664123],[-7.653035],[7.701328],[2.561255],[-7.453835],[-3.848488],[3.883311],[-6.262601],[-2.708832],[8.592259],[1.500703],[-9.193209],[-6.747324],[-9.917394],[3.303030],[3.396576],[-2.687402],[-0.853361],[9.481059],[-0.962458],[-8.607073],[0.520931],[-7.341231],[8.325094],[-9.628910],[-2.000220],[-0.524924],[-5.550330],[4.330390],[-6.588729],[-9.995185],[5.222078],[7.000444],[1.242624],[3.687830],[-0.097556],[-9.633147],[2.368813],[9.745097],[1.564625],[0.134082],[-3.083069],[-2.233337],[-4.920244],[7.438985],[-2.729415],[-9.694571],[-5.973928],[-3.661919],[2.136836],[6.957516],[3.371605],[6.124860],[-1.790989],[5.902532],[-1.023802],[9.401398],[-2.531595],[6.501723],[6.014328],[-9.509773],[-8.718764],[7.267062],[-0.176304],[-7.800755],[4.045504],[-5.435588],[2.342988],[6.713232],[-7.534287],[2.370285],[0.654488],[2.826255],[4.235723],[4.564896],[0.945471],[-3.690199],[-6.812967],[-7.431238],[4.617923],[-2.009501],[-7.813469],[0.081323],[-5.993211],[-6.728977],[-5.909424],[5.619079],[-2.455188],[3.007321],[3.736534],[8.424217],[-5.280869],[1.644822],[2.864646],[-6.399474],[-7.530618],[-1.747253],[6.810789],[8.703966],[-1.201430],[-4.655324],[2.052229],[9.738258],[8.140619],[2.107738],[4.293781],[7.784098],[3.180793],[-9.777565],[4.857647],[6.069600],[-0.148698],[-9.645952],[-4.585621],[6.912233],[6.570030],[6.750928],[-0.659303],[1.896988],[7.874867],[-9.629037],[5.968178],[0.301899],[-1.213514],[3.873957],[-1.739662],[-2.839428],[-3.273884],[-5.392699],[-3.213425],[-6.834633],[8.177528],[-7.149771],[-7.305783],[8.260624],[1.027238],[-0.475130],[-5.093103],[7.632022],[7.745822],[-2.510626],[6.942121],[-5.662305],[5.693204],[-8.293038],[2.406244],[-1.296642],[-9.577669],[-3.486361],[-1.833112],[7.978605],[7.932503],[-0.754578],[8.248727],[7.966945],[-5.013929],[-7.210562],[-4.715923],[-8.022426],[2.727398],[6.973267],[2.050470],[4.561140],[-0.101062],[-6.600633],[-1.500843],[-0.647706],[6.592333],[0.215018],[-2.282566],[3.302440],[-8.109372],[7.379771],[5.388607],[-3.714655],[-5.674832],[5.202197],[2.778670],[-0.725242],[-8.501860],[-9.894179],[-9.510969],[-9.266413],[1.942408],[-9.518820],[-3.646065],[0.875392],[0.839825],[7.324885],[-0.758944],[2.171875],[0.661114],[-8.438768],[0.964414],[0.783563],[9.614134],[-6.416422],[-7.554581],[3.805694],[-4.280513],[-6.272007],[9.973485],[4.119832],[-6.437172],[2.245391],[6.873480],[0.096553],[1.900539],[8.885959],[-9.024777],[-5.212861],[9.564200],[9.837098],[-0.977567],[2.736569],[-5.349269],[7.252640],[7.676989],[-8.170510],[-9.002176],[-5.940815],[-3.429171],[-7.039550],[1.678867],[7.364583],[-2.797804],[7.701624],[-0.080856],[-4.816289],[6.677343],[-8.173310],[4.087842],[-2.366564],[-9.105364],[-2.843551],[-2.316865],[-3.969192],[-5.909492],[9.242023],[5.911142],[-6.621325],[-8.388077],[3.543338],[-1.790137],[4.367167],[8.368474],[-2.523034],[-2.200142],[-6.390100],[1.821706],[1.047208],[5.318959],[0.592066],[-5.173897],[-6.052184],[8.849932],[-3.237333],[-5.442756],[-1.779332],[3.088385],[2.498122],[1.618886],[0.271973],[-5.562415],[4.276959],[-4.265620],[9.309689],[-2.476464],[4.146981],[5.257354],[-2.413330],[-2.276911],[5.231057],[-6.348189],[-3.580887],[1.864174],[3.524416],[4.556587],[-6.385928],[-5.511100],[2.214845],[-5.921423],[-6.656465],[8.836187],[-0.192002],[5.995334],[2.740516],[0.652457],[7.654383],[7.248591],[0.652625],[4.236357],[7.428952],[3.735438],[-8.238963],[5.882220],[-8.432341],[-3.521788],[7.270818],[-2.209367],[5.102117],[-0.241740],[-2.802234],[1.123609],[-1.645793],[7.459135],[8.029055],[-6.638244],[5.800998],[8.795043],[9.704211],[9.015420],[-8.153507],[-3.112831],[-3.602363],[9.685043],[6.447446],[-2.246429],[5.663376],[1.016667],[-9.490084],[8.225203],[3.124944],[4.756382],[5.476590],[-3.323408],[4.855352],[-0.077396],[3.694184],[7.642178],[-9.448259],[4.192776],[0.531276],[9.596304],[7.338153],[-7.964102],[7.024691],[-1.398851],[1.123658],[2.949823],[-7.248655],[3.062373],[4.214579],[6.492749],[-7.092630],[-5.198674],[-5.496243],[-3.886957],[-7.174874],[-6.284251],[-4.626613],[0.432882],[6.059338],[-4.971065],[4.920563],[3.854582],[9.398578],[-4.321328],[9.873424],[-5.572192],[-6.263065],[-7.905950],[-8.717735],[-7.761792],[-1.860612],[0.476967],[0.720269],[-2.125230],[-9.252719],[5.113187],[-2.217856],[1.722435],[4.106476],[-6.152156],[5.281597],[9.908577],[-4.364060],[-1.674977],[-2.203722],[2.301677],[-4.658970],[-7.820397],[5.499839],[-9.590140],[7.873879],[-5.543301],[-3.607730],[-6.737356],[6.749862],[-8.283713],[8.137956],[-9.550510],[3.200436],[-5.740017],[-2.199719],[-7.860428],[-2.643708],[-6.673818],[1.837408],[8.303411],[7.906089],[-8.152989],[9.106104],[0.060881],[-5.651062],[-4.316549],[4.113890],[7.558850],[7.769120],[4.650571],[5.872607],[-9.658435],[-7.142442],[1.631226],[0.189631],[-1.543827],[-8.296610],[2.544798],[7.432568],[-9.938608],[-1.480734],[6.074783],[-4.425324],[8.401700],[8.594075],[1.090111],[-5.177731],[-8.284796],[-5.830579],[5.284450],[6.452122],[-9.405510],[-6.012546],[0.304074],[3.212501],[1.384031],[-4.653007],[1.813514],[2.378764],[6.268807],[3.436813],[4.996291],[-0.600675],[-4.192939],[-0.601695],[5.164333],[-6.013637],[1.322321],[2.998952],[-9.959493],[0.648125],[-4.427418],[5.586117],[-3.817277],[-7.902489],[0.394141],[-0.097542],[-8.929290],[-4.838675],[1.465776],[-3.466968],[-7.107920],[3.484618],[5.325984],[7.358829],[9.454698],[-9.565547],[-9.590796],[0.207219],[-6.264490],[-7.324325],[-5.111375],[7.400860],[-5.186183],[6.072081],[-7.745354],[-5.910036],[-7.568371],[-6.318540],[-8.010105],[-9.861174],[-0.390883],[0.498977],[-8.913132],[2.230055],[9.925215],[-4.864744],[-9.486962],[-8.734327],[2.032399],[4.229655],[4.068030],[7.045434],[2.386186],[4.084648],[2.427628],[5.138618],[-3.856488],[-2.298831],[1.993913],[-9.615492],[-8.242388],[-9.624465],[-4.664912],[6.568547],[4.303484],[3.925217],[-2.558169],[-2.606660],[-3.645671],[5.937178],[2.192025],[-2.660501],[7.372954],[-1.400159],[-6.008995],[4.490194],[3.967307],[-5.316065],[-9.486630],[-3.426466],[-6.138754],[-4.733631],[-6.182525],[-8.775633],[4.384453],[-8.036437],[-5.870061],[-8.429105],[2.930474],[-6.782578],[9.586899],[-2.444850],[-4.088052],[-6.686435],[-6.045962],[-9.908322],[-2.956471],[4.509291],[0.289429],[-6.596012],[6.873163],[-6.341078],[9.493160],[-3.679757],[7.445294],[-9.078723],[-9.632343],[-2.508456],[7.031893],[-5.540534],[1.827417],[-6.171153],[4.205495],[-5.524008],[6.224951],[6.955898],[2.992496],[-0.743057],[2.370449],[3.981450],[-4.293056],[5.756479],[6.016529],[4.638895],[9.933302],[-4.669145],[-8.299068],[-9.126489],[0.068347],[-5.950860],[9.317051],[5.384869],[6.148979],[3.101631],[-6.731552],[-1.612917],[4.595749],[-9.773919],[1.751325],[2.877394],[9.506267],[5.074265],[2.561890],[9.962680],[-1.708921],[7.892974],[-4.059499],[-2.602646],[7.031745],[-6.319229],[-2.128116],[-1.588032],[-1.287721],[-4.991216],[-1.730697],[-5.122278],[-7.677925],[5.589883],[-4.948205],[-1.061698],[-0.541076],[-4.703859],[-4.016601],[4.808538],[4.106634],[-3.692834],[-8.339925],[7.717520],[9.168877],[-5.344385],[1.231175],[1.577332],[-9.238790],[0.319613],[5.359550],[5.400586],[-5.427541],[-7.994331],[-0.592897],[-9.774904],[7.744904],[6.331353],[9.849320],[3.213967],[3.476846],[-0.257866],[-9.037218],[-2.434664],[-8.663544],[2.381332],[7.107177],[4.111567],[7.061403],[-3.038436],[3.150412],[8.188365],[0.856026],[-0.627082],[3.442216],[2.701495],[5.589621],[1.572025],[4.206016],[-8.747795],[-7.616885],[-8.063073],[-9.283773],[4.898852],[3.006241],[1.900105],[-5.623146],[-7.431260],[-9.182638],[-8.924859],[-3.124766],[-4.634761],[4.231260],[2.984128],[9.916336],[-8.268404],[-7.954530],[5.588578],[-8.818977],[-0.650101],[-4.068925],[1.572168],[-8.306810],[6.005328],[-8.646696],[-9.664810],[2.425799],[3.860332],[-0.241852],[-2.972079],[-0.462387],[8.275695],[8.451714],[-0.962113],[0.777695],[9.153611],[-8.558702],[-1.806107],[-4.752572],[9.104953],[8.951322],[0.792131],[-5.442880],[2.138254],[-2.439011],[-3.743827],[-4.235533],[2.896390],[-8.537568],[-7.649019],[-4.071919],[-2.962429],[-1.864118],[6.376545],[-3.267582],[3.476273],[-9.367600],[-3.838552],[2.602971],[5.262436],[9.497401],[0.345544],[-2.162209],[7.328489],[-2.270906],[-7.995702],[-5.888556],[1.332559],[-2.941232],[0.606386],[-6.161329],[-0.602617],[-2.767839],[9.606465],[0.795516],[0.123986],[7.852188],[-1.178990],[8.527675],[-5.110162],[1.983414],[-3.625528],[2.336400],[-9.573476],[-9.820373],[-7.624755],[5.933771],[1.517276],[-6.742545],[2.984289],[4.479783],[-1.900340],[8.958026],[-9.285818],[5.808561],[-0.737837],[-6.854299],[-8.738625],[2.238277],[7.565172],[-2.907984],[-3.472303],[-3.671592],[5.958887],[-8.115899],[-2.819499],[3.438903],[-4.317562],[-7.578321],[8.850864],[-2.714209],[-3.096868],[-3.142816],[-1.395874],[-0.104049],[1.712332],[-8.158126],[-0.243374],[1.721378],[5.768844],[-3.658672],[-3.330300],[-6.018492],[2.633128],[7.047139],[-8.678896],[-8.768537],[-8.848848],[3.458258],[-7.012953],[-4.032615],[2.171845],[7.082091],[-6.572930],[1.392660],[2.929637],[8.027608],[-5.245821],[-5.563483],[-9.019359],[-1.178210],[7.920888],[-8.643997],[-1.216519],[0.085224],[5.478187],[-9.547886],[-3.894557],[-2.287225],[5.957834],[-9.044583],[5.157473],[-7.786859],[2.507748],[0.230079],[-9.255258],[2.800186],[5.505579],[-4.658729],[4.714285],[-9.259922],[6.108455],[9.552434],[3.890244],[-5.946128],[-1.435984],[2.664597],[7.257701],[5.888280],[-4.253379],[-0.546961],[-4.648519],[1.715965],[4.540897],[9.541781],[9.687744],[1.787421],[3.633111],[-5.965625],[-1.350901],[9.733988],[4.060553],[5.539470],[-3.775900],[5.862175],[7.414742],[7.951249],[9.853342],[6.062076],[-6.890599],[-5.582757],[7.432893],[6.438939],[-3.065944],[7.052247],[-9.268158],[7.035076],[4.432773],[-1.456789],[4.585983],[-5.194978],[-8.214060],[3.051540],[-3.870989],[-1.245719],[8.878740],[-1.287834],[2.348510],[0.642214],[2.646559],[-4.370439],[2.543738],[0.561492],[-7.859243],[-7.146977],[-3.719106],[6.686126],[6.407332],[-5.130570],[6.680487],[-3.275081],[5.045037],[3.580468],[-3.650509],[2.810900],[2.442340],[-2.350715],[7.090626],[0.726447],[3.262169],[-9.402565],[4.529391],[-8.082512],[-0.850354],[-4.358672],[-3.152256],[-8.090009],[-5.471131],[-7.409345],[6.055365],[-7.082154],[5.710006],[5.969615],[7.367660],[3.607168],[4.551974],[-7.927724],[8.993268],[8.068734],[9.165710],[5.211235],[-1.601568],[-0.854454],[-2.146793],[-8.294557],[-1.047860],[-5.043848],[2.387452],[-2.333166],[4.537990],[8.059567],[2.593470],[2.419977],[2.020459],[-2.128311],[-6.357794],[-8.007332],[-2.150572],[1.570306],[4.591608],[-9.730842],[8.960001],[2.701526],[-6.681485],[8.230915],[8.549536],[-3.580698],[-8.003179],[3.814685],[-7.822108],[-9.070935],[-4.642131],[-3.111505],[2.309643],[2.412060],[9.710601],[-6.071369],[-9.780787],[8.988457],[-5.681869],[-6.100088],[3.484001],[-1.278880],[-5.941365],[5.542611],[-5.032336],[-0.016002],[-1.319950],[7.636456],[-7.600964],[-8.613790],[-8.875020],[-0.878851],[3.134732],[4.843845],[-0.223259],[1.368688],[4.377253],[2.132362],[-9.595156],[-0.316516],[1.653034],[0.151435],[4.837223],[1.770846],[8.323743],[2.872523],[7.099623],[-2.895103],[6.195616],[-8.145423],[-7.714291],[-6.299892],[8.485785],[8.063153],[-5.934170],[-4.218487],[-2.302717],[-6.349271],[-2.940093],[-7.216224],[9.171905],[3.532666],[5.143864],[2.006722],[-7.923136],[4.785913],[-7.621763],[-9.104371],[7.717124],[6.367659],[0.564745],[5.968828],[1.867887],[-4.098962],[-7.370208],[0.087231],[-3.221041],[-5.608307],[-7.189709],[9.796785],[7.065811],[7.496375],[-4.698959],[0.441062],[-4.384585],[9.878439],[0.330999],[1.826474],[-3.506620],[-6.166222],[-6.878360],[7.920303],[0.168549],[8.879176],[0.091095],[-0.388972],[2.589403],[-9.718678],[2.795901],[3.915730],[-2.788236],[5.482604],[-6.485683],[-6.407754],[-5.052607],[1.189597],[-4.071526],[-7.080250],[-5.373807],[-3.925783],[-8.410819],[-1.861178],[-3.062030],[8.938011],[-4.916439],[1.643030],[2.735104],[-5.503978],[-7.572659],[4.698789],[-0.662937],[0.609797],[5.647116],[-3.225799],[2.556576],[1.473228],[5.440474],[4.800535],[9.704263],[9.539014],[-1.053707],[-6.501452],[3.860044],[4.318639],[-1.332499],[0.800248],[9.689743],[0.652911],[-3.101152],[-9.001865],[-4.316719],[8.402781],[7.199919],[-4.323111],[4.157308],[-7.691610],[-2.433233],[2.370503],[-0.091319],[9.919802],[6.603855],[2.211613],[-4.034356],[3.165825],[-9.357364],[-5.264600],[-8.128329],[-6.605543],[6.044545],[-5.764424],[-2.033745],[-4.559934],[6.901199],[-7.705998],[-8.544245],[-0.462901],[-4.877241],[-2.506872],[8.856350],[3.856416],[5.167041],[-5.119316],[5.141724],[2.349478],[5.299832],[1.964345],[-9.858906],[0.491720],[-8.315578],[6.127023],[1.588339],[-1.255999],[6.168777],[-3.972241],[0.447023],[-4.139857],[-9.192834],[-1.135994],[0.991353],[-9.595243],[9.373636],[-3.646077],[7.398212],[1.686201],[-9.008428],[-9.069774],[5.314612],[6.840172],[2.834154],[6.300742],[-0.936938],[3.671693],[-2.743322],[-0.938124],[0.409029],[3.242598],[3.661037],[-9.927598],[2.010934],[-6.018899],[3.461566],[9.621822],[1.494539],[7.673189],[8.687581],[7.464440],[6.492318],[-6.181107],[-1.247088],[4.282294],[6.186777],[-9.308418],[8.677318],[0.421746],[6.013221],[-4.853196],[-6.028834],[9.900387],[-8.438272],[-1.193780],[9.439000],[1.126984],[-7.248911],[-3.436308],[8.543606],[-0.224230],[-8.388908],[3.987197],[3.939373],[-7.798232],[-7.438159],[8.447612],[4.731881],[-4.743712],[-6.069381],[8.845791],[4.374982],[-6.033396],[-5.488365],[-2.333078],[-6.423148],[-7.871028],[-3.319036],[-5.239291],[-9.100290],[-6.427196],[2.983534],[3.826564],[-0.243391],[0.443990],[-2.575920],[-0.223064],[8.634421],[1.182170],[0.671809],[1.738673],[-6.802954],[0.998173],[2.892271],[-0.913725],[-5.422739],[-0.229210],[2.307105],[-1.806323],[-2.304587],[-5.408723],[-2.614407],[-7.723031],[3.677652],[6.322302],[7.352111],[-3.780694],[-4.170537],[-1.910567],[-5.341468],[4.713946],[8.636614],[-4.985384],[7.530497],[-9.801505],[-4.223591],[-9.156215],[9.243755],[2.167238],[-4.350876],[-5.494825],[5.249768]], dtype = "float32")#candidate|4864|(2025, 1)|const|float32
const_4865 = relay.const(-2, dtype = "int64")#candidate|4865|()|const|int64
const_4866 = relay.const([3,-1,-4,-5,-5,-1,-3,-5,2,5,-3,-3,-5,-9,5,8,-3,-5,10,-3,4,9,7,-10,-4,-8,9,9,6,-10,-3,10,-1,-10,-5,-7,-1,10,10,4,5,10,5,-8,7,-3,8,6,-8,-2,1,6,4,9,-6,-8,7,4,5,-7,10,3,-3,7,7,-6,9,-10,8,8,4,-4,2,-7,10,1,1,-7,-3,6,6,-8,-2,9,-10,3,-1,-7,6,1,-7,3,-6,-4,7,-9,-10,7,9,-3,10,-5,4,7,-7,6,-9,-3,1,6,-5,-10], dtype = "int64")#candidate|4866|(112,)|const|int64
call_4863 = relay.TupleGetItem(func_243_call(relay.reshape(const_4864.astype('float32'), [15, 9, 15]), relay.reshape(const_4865.astype('int64'), []), relay.reshape(const_4866.astype('int64'), [112,]), ), 2)
call_4867 = relay.TupleGetItem(func_248_call(relay.reshape(const_4864.astype('float32'), [15, 9, 15]), relay.reshape(const_4865.astype('int64'), []), relay.reshape(const_4866.astype('int64'), [112,]), ), 2)
func_4231_call = mod.get_global_var('func_4231')
func_4236_call = mutated_mod.get_global_var('func_4236')
var_4878 = relay.var("var_4878", dtype = "float32", shape = (392,))#candidate|4878|(392,)|var|float32
const_4879 = relay.const([6.059484,-8.023756,-7.144103,-8.005349,-0.732077,-2.161246,-0.544955,3.378315,-8.204406,0.391406,6.926261,9.192884,-9.054134,1.361837,-2.536676,-1.583960,3.940661,-7.008843,5.393279,8.472488,7.185513,-6.840350,-5.335792,-8.401426,-2.795207,9.250938,5.196375,0.001570,4.537643,-9.377895,-5.311914,-5.471168,5.074196,-2.169656,4.306204,-4.336517,3.233949,-5.421199,-2.629294,-8.041602,-2.731941,0.315106,-4.698577,-3.179120,6.540427,8.143957,0.545161,8.081683,2.706003,8.171764,9.841597,1.485194,9.385441,-6.986621,-0.518458,-0.003910,-3.357797,-1.170255,-5.308981,2.593450,3.090576,-7.217342,-7.607774,-4.929648,5.725188,-5.657601,2.650057,3.602360,8.634240,1.062026,-9.014843,-2.033962,3.127698,7.422682,1.278509,8.397921,3.345037,-6.307169,-4.685128,7.355438,-3.951359,-5.086857,6.625113,-7.347199,-9.674234,-1.359009,5.481294,6.230983,-4.091998,1.729581,3.863378,-6.409788,-9.820726,-1.290854,7.147376,-1.036099,9.404187,-9.302578,-3.637572,6.007870,-4.325507,0.950845,2.289011,-4.616590,1.604617,6.379584,-6.993901,8.524946,-9.471310,5.935011,-4.232865,-9.992523,9.049046,-6.274449,0.641825,-0.352954,-1.194573,-2.490693,-7.155434,2.560536,-8.874902,7.486368,-3.897366,3.236043,-5.801465,2.257255,-7.017934,1.601591,-5.877695,3.041223,6.045860,9.259402,7.728704,1.602180,-5.222397,4.252324,-4.731923,5.459843,6.839502,0.791993,-8.775214,-4.870456,-7.252260,-3.384620,-3.244799,2.883711,9.120195,6.779901,-0.568194,-7.689830,2.190495,4.139845,-1.064402,-9.229690,3.470860,-4.884241,-2.825022,-1.723817,-5.455188,8.342849,-4.532197,-0.095950,9.034537,-1.235663,5.092849,-9.101778,-7.079090,-9.333030,4.812729,-5.306038,-3.178404,-0.704969,-8.788119,-3.023939,7.622800,3.018067,-8.209160,5.272701,1.078795,7.359957,-0.641657,9.179040,3.848238,-3.771074,-7.690825,0.548285,3.949422,-9.826417,-9.066512,-3.245315,-0.840192,1.154638,8.802038,5.110142,-5.229486,3.529133,-9.867156,8.455167,-1.085777,-4.034885,-6.746590,-3.042168,7.375095,4.107286,1.374709,7.928555,4.710376,-1.408658,4.906692,3.529310,-2.448532,7.047298,8.240817,-1.480860,-1.170255,3.754575,-1.685527,-8.280967,-5.232146,4.073835,6.745342,0.287428,4.088505,2.368082,2.565069,-7.195950,-8.994841,3.898339,-9.454014,7.636353,-8.041122,3.790483,-2.634841,6.407213,-8.093946,-8.051553,7.112052,-7.822955,8.147259,-5.757563,7.862435,-8.502192,-6.191758,7.068009,4.559382,8.393442,7.341315,-9.606608,-7.829088,-5.679975,-5.151119,-1.152489,0.904293,-0.528755,-7.278394,9.924834,6.240114,1.152284,8.259618,-7.676572,-5.996205,2.614587,4.562022,3.601698,9.149340,-0.598765,3.337266,4.285042,3.664183,2.401783,-1.432474,9.565649,9.944016,2.983194,-8.874293,7.012980,1.959480,-7.845700,3.661709,-6.259835,-3.520790,-9.682967,7.257525,-2.548727,-1.631686,0.428919,-2.070687,-3.259028,2.790037,7.368450,-7.386770,-0.635687,9.843056,-0.847968,8.435356,1.011088,9.925284,0.902614,0.474759,0.194023,0.708775,1.178214,-7.334453,9.884838,3.933222,6.506846,-8.356172,-0.203007,-9.472278,-4.967525,7.307700,7.544168,3.565449,-7.831942,-2.736842,-5.315916,-9.577450,-1.848650,-4.323916,-1.184121,-7.061138,6.653854,-6.674600,-6.429267,-1.990674,-6.102623,-9.574890,-8.744625,-4.059482,-0.880597,-0.942836,-0.785033,-7.940559,9.035807,4.075038,4.752463], dtype = "float32")#candidate|4879|(336,)|const|float32
call_4877 = relay.TupleGetItem(func_4231_call(relay.reshape(var_4878.astype('float32'), [14, 4, 7]), relay.reshape(var_4878.astype('float32'), [14, 4, 7]), relay.reshape(const_4866.astype('int64'), [28, 4]), relay.reshape(const_4879.astype('float32'), [336,]), ), 1)
call_4880 = relay.TupleGetItem(func_4236_call(relay.reshape(var_4878.astype('float32'), [14, 4, 7]), relay.reshape(var_4878.astype('float32'), [14, 4, 7]), relay.reshape(const_4866.astype('int64'), [28, 4]), relay.reshape(const_4879.astype('float32'), [336,]), ), 1)
func_2584_call = mod.get_global_var('func_2584')
func_2586_call = mutated_mod.get_global_var('func_2586')
var_4894 = relay.var("var_4894", dtype = "uint16", shape = (324,))#candidate|4894|(324,)|var|uint16
call_4893 = relay.TupleGetItem(func_2584_call(relay.reshape(var_4894.astype('uint16'), [324,])), 0)
call_4895 = relay.TupleGetItem(func_2586_call(relay.reshape(var_4894.astype('uint16'), [324,])), 0)
func_2181_call = mod.get_global_var('func_2181')
func_2183_call = mutated_mod.get_global_var('func_2183')
call_4899 = func_2181_call()
call_4900 = func_2181_call()
func_4636_call = mod.get_global_var('func_4636')
func_4638_call = mutated_mod.get_global_var('func_4638')
call_4901 = relay.TupleGetItem(func_4636_call(relay.reshape(call_4899.astype('float32'), [3, 5, 15])), 0)
call_4902 = relay.TupleGetItem(func_4638_call(relay.reshape(call_4899.astype('float32'), [3, 5, 15])), 0)
func_4749_call = mod.get_global_var('func_4749')
func_4751_call = mutated_mod.get_global_var('func_4751')
call_4914 = relay.TupleGetItem(func_4749_call(), 0)
call_4915 = relay.TupleGetItem(func_4751_call(), 0)
bop_4917 = relay.equal(call_4893.astype('bool'), relay.reshape(call_4901.astype('bool'), relay.shape_of(call_4893))) # shape=(3, 5, 15)
bop_4920 = relay.equal(call_4895.astype('bool'), relay.reshape(call_4902.astype('bool'), relay.shape_of(call_4895))) # shape=(3, 5, 15)
func_3859_call = mod.get_global_var('func_3859')
func_3861_call = mutated_mod.get_global_var('func_3861')
call_4921 = func_3859_call()
call_4922 = func_3859_call()
output = relay.Tuple([call_4846,call_4863,const_4864,const_4865,const_4866,call_4877,var_4878,const_4879,var_4894,call_4899,call_4914,bop_4917,call_4921,])
output2 = relay.Tuple([call_4847,call_4867,const_4864,const_4865,const_4866,call_4880,var_4878,const_4879,var_4894,call_4900,call_4915,bop_4920,call_4922,])
func_4924 = relay.Function([var_4878,var_4894,], output)
mod['func_4924'] = func_4924
mod = relay.transform.InferType()(mod)
mutated_mod['func_4924'] = func_4924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4924_call = mutated_mod.get_global_var('func_4924')
var_4926 = relay.var("var_4926", dtype = "float32", shape = (392,))#candidate|4926|(392,)|var|float32
var_4927 = relay.var("var_4927", dtype = "uint16", shape = (324,))#candidate|4927|(324,)|var|uint16
call_4925 = func_4924_call(var_4926,var_4927,)
output = call_4925
func_4928 = relay.Function([var_4926,var_4927,], output)
mutated_mod['func_4928'] = func_4928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2998_call = mod.get_global_var('func_2998')
func_3000_call = mutated_mod.get_global_var('func_3000')
call_4951 = func_2998_call()
call_4952 = func_2998_call()
output = call_4951
output2 = call_4952
func_4967 = relay.Function([], output)
mod['func_4967'] = func_4967
mod = relay.transform.InferType()(mod)
mutated_mod['func_4967'] = func_4967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4967_call = mutated_mod.get_global_var('func_4967')
call_4968 = func_4967_call()
output = call_4968
func_4969 = relay.Function([], output)
mutated_mod['func_4969'] = func_4969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4970 = relay.var("var_4970", dtype = "float32", shape = ())#candidate|4970|()|var|float32
var_4971 = relay.var("var_4971", dtype = "float32", shape = (6, 6, 10))#candidate|4971|(6, 6, 10)|var|float32
bop_4972 = relay.maximum(var_4970.astype('float32'), var_4971.astype('float32')) # shape=(6, 6, 10)
output = relay.Tuple([bop_4972,])
output2 = relay.Tuple([bop_4972,])
func_4988 = relay.Function([var_4970,var_4971,], output)
mod['func_4988'] = func_4988
mod = relay.transform.InferType()(mod)
var_4989 = relay.var("var_4989", dtype = "float32", shape = ())#candidate|4989|()|var|float32
var_4990 = relay.var("var_4990", dtype = "float32", shape = (6, 6, 10))#candidate|4990|(6, 6, 10)|var|float32
output = func_4988(var_4989,var_4990,)
func_4991 = relay.Function([var_4989,var_4990,], output)
mutated_mod['func_4991'] = func_4991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2716_call = mod.get_global_var('func_2716')
func_2718_call = mutated_mod.get_global_var('func_2718')
call_5008 = func_2716_call()
call_5009 = func_2716_call()
output = call_5008
output2 = call_5009
func_5017 = relay.Function([], output)
mod['func_5017'] = func_5017
mod = relay.transform.InferType()(mod)
mutated_mod['func_5017'] = func_5017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5017_call = mutated_mod.get_global_var('func_5017')
call_5018 = func_5017_call()
output = call_5018
func_5019 = relay.Function([], output)
mutated_mod['func_5019'] = func_5019
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5031 = relay.var("var_5031", dtype = "float32", shape = (11, 5, 3))#candidate|5031|(11, 5, 3)|var|float32
uop_5032 = relay.sinh(var_5031.astype('float32')) # shape=(11, 5, 3)
bop_5042 = relay.greater(uop_5032.astype('bool'), relay.reshape(var_5031.astype('bool'), relay.shape_of(uop_5032))) # shape=(11, 5, 3)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_5045 = relay.TupleGetItem(func_2776_call(), 3)
call_5046 = relay.TupleGetItem(func_2778_call(), 3)
func_611_call = mod.get_global_var('func_611')
func_613_call = mutated_mod.get_global_var('func_613')
call_5065 = relay.TupleGetItem(func_611_call(), 1)
call_5066 = relay.TupleGetItem(func_613_call(), 1)
func_1111_call = mod.get_global_var('func_1111')
func_1117_call = mutated_mod.get_global_var('func_1117')
call_5067 = relay.TupleGetItem(func_1111_call(relay.reshape(call_5045.astype('float64'), [3, 5, 15]), relay.reshape(call_5065.astype('uint16'), [9, 36]), relay.reshape(call_5065.astype('uint16'), [9, 36]), relay.reshape(call_5065.astype('uint16'), [9, 3, 12]), ), 2)
call_5068 = relay.TupleGetItem(func_1117_call(relay.reshape(call_5045.astype('float64'), [3, 5, 15]), relay.reshape(call_5065.astype('uint16'), [9, 36]), relay.reshape(call_5065.astype('uint16'), [9, 36]), relay.reshape(call_5065.astype('uint16'), [9, 3, 12]), ), 2)
func_4924_call = mod.get_global_var('func_4924')
func_4928_call = mutated_mod.get_global_var('func_4928')
const_5075 = relay.const([-5.878767,8.666240,-4.395116,0.692855,-0.781288,9.925283,3.419149,-1.413572,6.709024,-2.371910,8.088760,-5.491514,6.315181,5.701696,2.532412,-7.562349,-0.542044,2.443196,-3.525869,-1.239699,-9.482176,-4.529673,8.841350,6.835570,-0.137605,5.383562,-1.613614,-7.910333,1.809772,-0.416770,-3.449069,0.687956,-4.758677,8.356814,8.480210,1.266680,-0.287287,-8.411198,4.913940,-9.890374,5.628882,1.519976,6.125983,-5.351090,4.575392,2.719720,6.884616,-4.486071,-6.991130,-9.180528,6.033316,8.298300,0.558272,6.211783,1.510572,0.556479,4.098195,-2.510117,-0.462115,-5.858009,-4.657885,2.356055,-0.803129,5.309719,6.251654,-9.459416,-1.016232,-9.375231,7.403456,-4.261060,6.822739,-2.895248,-4.164966,5.684615,2.617847,4.313281,-7.023676,6.982617,-4.393523,3.248759,-6.084311,9.209114,3.522595,-5.482177,1.570855,9.693796,-3.080868,-0.225306,6.305511,3.514386,6.285417,-9.588593,6.499341,-2.670886,-7.377007,-5.462749,4.295051,8.479094,9.382886,-9.906659,-4.732183,-8.510924,4.227898,-1.899259,-2.288628,1.149762,-7.463149,4.798727,1.179729,2.025614,3.258317,-0.205110,5.480414,4.230339,2.763472,-9.999955,-0.866965,5.656891,7.504146,-8.172359,8.078725,3.468981,1.894780,-7.417479,-6.267564,-3.065927,3.633035,-0.393728,7.687703,1.924688,4.676037,-1.998286,-2.933697,1.158593,7.486773,-6.262141,1.246741,-7.624598,-3.401366,7.695302,2.087734,1.701664,-0.477211,7.932929,8.483609,6.562255,-1.467395,-4.239370,6.954421,-4.476449,9.902319,5.198881,-4.149734,8.519923,-4.236346,1.087954,5.436768,-1.788894,3.526156,8.953947,8.891257,4.646791,-3.710954,-5.861520,-5.630087,3.990830,3.921022,-8.081941,-6.999715,5.254642,3.072403,-8.622980,4.677520,-8.158797,2.099649,7.345795,-1.726341,-6.073667,7.545661,-0.646987,-2.856075,3.819999,8.864828,3.263035,-7.425006,-5.815021,-2.552034,-4.180520,-2.678899,-3.328508,-0.878683,-1.790280,-6.072643,9.317707,7.045339,1.151715,1.559550,-1.213687,2.069383,9.459658,-9.304194,3.399942,-4.128461,-3.671963,-6.417944,-8.645573,-5.246672,-4.754344,-3.434489,-3.204149,0.749786,9.314226,0.362623,1.703580,5.626716,-3.588438,8.012805,-4.819683,7.035454,-8.838100,3.821482,-1.112025,9.710683,8.673467,-8.030570,5.758831,6.814181,0.684669,-8.012322,6.895177,9.337019,1.388988,9.507559,-2.758411,-4.465977,1.823269,-8.692475,-1.600823,-8.262777,8.633664,2.961845,-1.996927,2.104219,2.370211,7.692959,0.466003,-7.264412,8.416752,9.253901,-9.228326,-2.331235,1.814837,3.014129,-7.180923,8.356253,8.831540,-0.725027,-0.912560,1.954830,-4.119448,-3.243718,8.960179,-9.360878,9.115690,-9.370424,-2.697885,0.530027,2.637256,2.052409,-7.066768,4.554254,9.896957,9.733473,7.703617,-3.222414,3.803518,-6.862715,9.947113,8.595902,-4.829561,4.365164,-9.518336,-7.201349,5.271505,3.092121,4.005895,7.583479,1.017238,-2.523418,7.604942,-0.168857,2.034683,2.105584,5.418366,9.080124,1.379079,-3.469397,6.199876,1.214921,-9.432925,-8.558146,-2.155652,8.651697,2.253218,-2.413151,-9.922218,8.010472,7.662265,-5.394328,-6.634013,-3.225273,-0.540863,2.854606,-0.131656,1.568866,-9.873868,-9.212129,5.227855,-9.871951,7.535635,-0.748969,3.069124,6.018857,-0.032745,4.489602,-1.701398,-6.751729,5.444171,-6.256841,4.549432,-1.071190,-6.993461,-2.288060,-9.615829,-2.655212,7.017604,8.951261,-3.049267,-5.130522,4.925226,6.452768,9.557438,-6.040747,-3.118315,-5.884599,-6.243317,4.808137,3.637180,4.225100,-1.484269,8.945554,-0.408084,-2.000543,-6.566429,9.098565,-8.423810,8.885822,0.724249,-4.105518,-1.547152,4.334860,-8.884044,6.447301,-1.002645,1.974632,-1.295478,-9.549698,-1.926704,-8.779886,4.885780,-3.089569,-7.107175,-1.837184,3.094769,9.310766,7.647016,9.518644,3.811610,-2.556039,7.653049,-7.349116,-0.145384,-6.710395,2.969399,4.372904,-7.944828,5.102274,6.611128,-6.359650,-3.671890,5.377674,-8.728768], dtype = "float32")#candidate|5075|(392,)|const|float32
call_5074 = relay.TupleGetItem(func_4924_call(relay.reshape(const_5075.astype('float32'), [392,]), relay.reshape(call_5065.astype('uint16'), [324,]), ), 4)
call_5076 = relay.TupleGetItem(func_4928_call(relay.reshape(const_5075.astype('float32'), [392,]), relay.reshape(call_5065.astype('uint16'), [324,]), ), 4)
func_2181_call = mod.get_global_var('func_2181')
func_2183_call = mutated_mod.get_global_var('func_2183')
call_5077 = func_2181_call()
call_5078 = func_2181_call()
var_5090 = relay.var("var_5090", dtype = "bool", shape = (11, 5, 3))#candidate|5090|(11, 5, 3)|var|bool
bop_5091 = relay.not_equal(bop_5042.astype('bool'), relay.reshape(var_5090.astype('bool'), relay.shape_of(bop_5042))) # shape=(11, 5, 3)
uop_5126 = relay.atanh(bop_5042.astype('float64')) # shape=(11, 5, 3)
func_4352_call = mod.get_global_var('func_4352')
func_4353_call = mutated_mod.get_global_var('func_4353')
call_5128 = func_4352_call()
call_5129 = func_4352_call()
uop_5130 = relay.acosh(uop_5126.astype('float64')) # shape=(11, 5, 3)
output = relay.Tuple([call_5045,call_5065,call_5067,call_5074,const_5075,call_5077,bop_5091,call_5128,uop_5130,])
output2 = relay.Tuple([call_5046,call_5066,call_5068,call_5076,const_5075,call_5078,bop_5091,call_5129,uop_5130,])
func_5132 = relay.Function([var_5031,var_5090,], output)
mod['func_5132'] = func_5132
mod = relay.transform.InferType()(mod)
var_5133 = relay.var("var_5133", dtype = "float32", shape = (11, 5, 3))#candidate|5133|(11, 5, 3)|var|float32
var_5134 = relay.var("var_5134", dtype = "bool", shape = (11, 5, 3))#candidate|5134|(11, 5, 3)|var|bool
output = func_5132(var_5133,var_5134,)
func_5135 = relay.Function([var_5133,var_5134,], output)
mutated_mod['func_5135'] = func_5135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2697_call = mod.get_global_var('func_2697')
func_2698_call = mutated_mod.get_global_var('func_2698')
call_5149 = relay.TupleGetItem(func_2697_call(), 1)
call_5150 = relay.TupleGetItem(func_2698_call(), 1)
uop_5153 = relay.atan(call_5149.astype('float32')) # shape=(3, 5, 15)
uop_5155 = relay.atan(call_5150.astype('float32')) # shape=(3, 5, 15)
func_446_call = mod.get_global_var('func_446')
func_448_call = mutated_mod.get_global_var('func_448')
call_5160 = func_446_call()
call_5161 = func_446_call()
output = relay.Tuple([uop_5153,call_5160,])
output2 = relay.Tuple([uop_5155,call_5161,])
func_5166 = relay.Function([], output)
mod['func_5166'] = func_5166
mod = relay.transform.InferType()(mod)
output = func_5166()
func_5167 = relay.Function([], output)
mutated_mod['func_5167'] = func_5167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3136_call = mod.get_global_var('func_3136')
func_3138_call = mutated_mod.get_global_var('func_3138')
call_5171 = relay.TupleGetItem(func_3136_call(), 0)
call_5172 = relay.TupleGetItem(func_3138_call(), 0)
output = call_5171
output2 = call_5172
func_5197 = relay.Function([], output)
mod['func_5197'] = func_5197
mod = relay.transform.InferType()(mod)
mutated_mod['func_5197'] = func_5197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5197_call = mutated_mod.get_global_var('func_5197')
call_5198 = func_5197_call()
output = call_5198
func_5199 = relay.Function([], output)
mutated_mod['func_5199'] = func_5199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3629_call = mod.get_global_var('func_3629')
func_3631_call = mutated_mod.get_global_var('func_3631')
call_5274 = relay.TupleGetItem(func_3629_call(), 1)
call_5275 = relay.TupleGetItem(func_3631_call(), 1)
output = call_5274
output2 = call_5275
func_5278 = relay.Function([], output)
mod['func_5278'] = func_5278
mod = relay.transform.InferType()(mod)
output = func_5278()
func_5279 = relay.Function([], output)
mutated_mod['func_5279'] = func_5279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5295 = relay.var("var_5295", dtype = "uint8", shape = (6, 5, 14))#candidate|5295|(6, 5, 14)|var|uint8
const_5296 = relay.const([[[-10,3,-2,4,-9,-1,8,-1,-8,-6,9,-9,-8,8],[-8,9,9,-5,8,3,2,4,-7,-2,3,6,-9,-3],[-3,-10,3,10,3,3,7,-1,-9,-10,9,5,-9,6],[-3,-6,-1,1,8,-7,7,2,-5,-2,7,3,3,8],[9,1,-4,-10,5,-10,-3,4,7,1,-1,8,-4,-4]],[[9,8,-7,-1,7,-7,-3,5,-3,5,7,4,10,5],[-5,10,2,-3,6,-3,5,7,-8,5,3,3,-5,-7],[-1,8,3,1,5,-6,9,-6,-9,4,5,-1,9,-8],[3,3,10,-1,9,-8,-5,7,-6,-10,-6,-2,-6,-9],[7,1,-3,-3,6,-3,5,1,-10,5,1,-10,-10,8]],[[-5,10,4,-1,8,7,-7,8,6,1,-8,-9,-2,8],[3,-7,-4,-2,8,5,-9,-9,5,-8,9,-4,-8,7],[-3,-1,10,-5,-2,-3,2,8,10,-8,7,5,-7,-2],[-3,-4,-4,5,10,-10,-6,-7,-1,-10,2,-4,-3,-6],[10,-5,7,-1,2,-6,-7,9,9,4,2,-9,-1,5]],[[3,-6,9,6,-9,-8,-5,7,1,5,-3,8,-2,-10],[-1,9,-6,5,-4,-3,9,8,-6,-6,-3,6,2,1],[-2,-7,8,5,10,-1,-4,-1,-6,9,-4,-8,7,-2],[2,3,6,5,7,-8,-3,-3,-3,-1,3,-10,2,5],[4,8,-3,-9,10,-3,-5,6,-9,-6,3,-1,5,5]],[[-9,-9,-2,-8,8,3,1,-7,-6,6,-1,-10,-10,-1],[10,6,-8,4,-4,4,10,-1,5,9,10,9,-10,6],[-9,6,-2,-1,-9,-10,-7,-4,4,-10,-3,2,-6,5],[-9,-7,5,-10,-10,-9,5,-10,6,1,-7,-2,-2,4],[-5,-6,-7,5,-8,10,3,7,-1,-10,10,8,2,10]],[[4,2,2,-4,-2,-2,3,10,-3,5,3,10,9,-3],[-8,5,-8,1,-8,10,5,2,-5,-3,-9,-2,-4,-8],[-10,3,5,-2,-8,2,8,-6,3,1,8,6,-10,2],[9,-6,10,-9,-9,7,-1,-3,-8,-4,-5,-8,-8,-2],[3,4,-5,-2,-2,-9,9,-10,4,3,-2,-2,-1,2]]], dtype = "uint8")#candidate|5296|(6, 5, 14)|const|uint8
bop_5297 = relay.logical_xor(var_5295.astype('uint8'), relay.reshape(const_5296.astype('uint8'), relay.shape_of(var_5295))) # shape=(6, 5, 14)
output = bop_5297
output2 = bop_5297
func_5308 = relay.Function([var_5295,], output)
mod['func_5308'] = func_5308
mod = relay.transform.InferType()(mod)
mutated_mod['func_5308'] = func_5308
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5309 = relay.var("var_5309", dtype = "uint8", shape = (6, 5, 14))#candidate|5309|(6, 5, 14)|var|uint8
func_5308_call = mutated_mod.get_global_var('func_5308')
call_5310 = func_5308_call(var_5309)
output = call_5310
func_5311 = relay.Function([var_5309], output)
mutated_mod['func_5311'] = func_5311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5316 = relay.var("var_5316", dtype = "float64", shape = (16, 14, 9))#candidate|5316|(16, 14, 9)|var|float64
uop_5317 = relay.tan(var_5316.astype('float64')) # shape=(16, 14, 9)
const_5328 = relay.const([[[5.717782,-0.079983,-4.853746,-9.305978,-0.420824,1.718191,2.792557,3.921388,6.895018],[-3.935931,-8.268423,-2.492658,-2.079365,-2.869476,-1.957957,-3.195601,9.220160,-1.618142],[-5.055604,-1.159155,-9.225239,8.361381,9.753558,1.093480,-1.555794,4.586066,5.101544],[-5.120741,-2.013086,0.376313,-1.463721,2.779634,-9.036540,2.425152,-5.033808,9.753377],[-0.147915,-5.737098,6.070883,-2.026211,1.857944,-5.942437,-3.128829,-4.731314,-1.663689],[5.104263,0.671083,-2.219756,-8.483135,-0.636976,0.564178,5.021339,-5.274835,2.631413],[4.609873,-5.634457,-8.460497,-2.323541,2.904727,3.427400,-5.272091,-7.216059,1.403560],[0.387125,-1.393635,-4.086430,7.559442,0.538429,7.258692,9.612519,2.466327,7.808388],[6.863156,-5.663022,-2.285327,-9.480048,-6.066162,-0.162500,3.737950,-6.343703,3.578218],[-8.473959,-3.395367,7.854737,-9.739749,5.636739,-6.420649,1.397548,-7.200151,-9.963328],[-9.891911,8.800102,4.017525,-2.773311,9.513635,-3.450844,-3.668156,7.806594,7.121285],[-0.667275,9.476983,9.851024,3.419053,8.203764,-0.835743,-0.217372,-2.028123,4.039769],[-7.993166,3.357194,-0.744970,-3.734143,-9.401253,-4.138056,-3.335988,5.138702,-5.740557],[9.529354,-2.096992,0.085046,-3.550288,0.490762,5.674536,-5.070771,-2.779158,8.958360]],[[-0.708949,7.813054,9.389116,-9.276008,3.197279,7.163003,-7.583319,4.974896,-0.773790],[2.425207,-2.100905,0.247570,6.775623,6.806444,5.470431,1.394189,7.601313,-7.311405],[-1.901508,-2.087111,4.257919,9.457783,2.372530,-1.089148,0.275510,-3.060977,-7.231275],[4.592598,-1.099749,0.017097,4.966407,8.748821,-8.791392,8.831059,-7.004643,-2.443739],[9.359795,0.654296,-6.764268,-5.247453,0.903978,1.788761,7.695525,5.293890,-8.009139],[7.901683,2.366755,-2.427989,7.943281,-0.750846,2.486687,6.903060,-9.386255,6.973347],[-2.485387,-0.251450,1.503153,8.151790,-1.591379,-5.059961,4.992361,-5.980551,-8.694060],[-0.199733,-2.670546,1.421343,6.903773,1.904940,0.468829,-9.438927,-9.596706,9.837780],[4.125249,-6.009061,9.312209,-5.701153,2.278716,-5.701742,8.304802,1.454600,4.167374],[7.724151,7.628539,8.211428,-6.686140,-6.033435,-1.314634,-8.354959,-0.399585,-4.497743],[8.755464,-9.899630,2.287609,-9.427045,-3.051970,7.772711,-3.470784,-3.202023,3.806044],[-6.058556,-7.424371,-0.078390,-0.116309,-6.026035,-4.188231,-3.425068,5.317761,-6.537072],[3.616822,3.840192,-7.902072,-7.890347,2.394610,-9.222154,-9.651449,-2.942897,1.136002],[1.979217,2.395603,-8.866762,-9.379874,9.304240,1.939344,4.307297,-7.315629,-4.826762]],[[6.451720,0.405150,-3.673300,0.619346,-3.070929,2.388113,-5.540620,6.928879,-1.098487],[3.248672,0.194792,-0.253196,-5.103924,1.626750,-0.331341,3.682927,-4.617768,-0.586805],[-4.497956,9.350759,-5.584273,-3.657105,-5.452508,-8.444023,8.747092,0.775155,7.726020],[-2.304350,5.225445,-1.354276,7.258549,1.774402,8.893342,-1.228963,6.870808,-5.358522],[-3.877132,2.536439,7.518597,6.081494,6.695653,2.134587,-9.352434,9.920152,0.325359],[8.269894,7.529630,9.725767,7.041846,9.641341,7.850249,-1.131660,-3.322922,-3.668537],[0.459726,2.160889,8.751535,7.000888,-9.945198,3.179448,5.720238,-3.198691,-5.734069],[3.584656,-5.291118,-3.360105,-5.049788,3.800943,-0.385708,-2.379841,-3.039545,7.047064],[-7.458872,1.919767,8.972388,6.076255,-1.461009,1.868836,4.318517,-7.403030,0.051499],[5.457864,1.834678,9.530987,9.139868,9.077425,1.409758,0.388714,-5.958762,-7.646392],[9.653092,-8.359234,1.070192,-7.182105,-9.133557,-0.629312,-5.325279,7.211248,0.237380],[6.368021,6.308372,-2.539420,3.662928,-8.265078,-5.482581,8.686420,-7.976549,5.940021],[-3.191437,-3.649439,-9.379205,-1.876920,6.448640,-4.396718,-3.283859,3.438711,1.753675],[-4.090865,7.836250,-1.814503,9.213845,8.109602,9.671988,-8.207917,3.463059,-8.005334]],[[9.204858,-2.653394,-2.310783,9.478885,-6.174758,-9.100560,-5.096757,5.308524,-9.348012],[-2.438747,2.529115,6.166223,-9.477646,-4.063845,7.252253,-2.068507,-4.942540,1.646081],[0.205176,0.605938,8.571042,0.803721,1.224445,8.072850,-8.110190,7.702006,6.151888],[-1.262594,-2.663504,1.839564,0.464982,8.284720,-9.964712,9.045183,3.957105,-0.981287],[-5.998023,3.354661,-7.823674,8.975418,-3.436689,-0.149594,-1.254815,0.847642,-8.056419],[-0.799569,-8.786396,7.305602,-1.194196,9.062947,3.363568,-2.489068,5.084876,2.057569],[-1.466555,6.920352,-5.404663,-8.568642,-5.874368,8.170710,2.353668,3.900317,3.809839],[-6.339647,9.022980,-4.221672,3.097734,-9.809993,-3.709728,-7.411093,7.056322,6.366215],[-7.433352,-2.500077,1.946924,7.224668,0.988861,2.192493,4.479587,-4.635200,4.628830],[8.944626,9.401012,4.052621,-6.132321,-9.881353,9.069821,9.064385,3.628859,2.074125],[1.405367,5.224299,8.481976,-7.443632,6.462860,0.011518,1.627799,4.261731,-0.152853],[-3.833670,7.703633,-2.683487,-5.894108,-4.866727,5.685201,-2.283244,-2.179343,6.754968],[-2.692541,-1.843811,-4.213861,-3.924556,-6.465861,-5.141757,7.744449,5.349966,6.563944],[1.404942,0.822363,-8.615047,8.624401,-0.354125,-7.838820,9.341519,0.636797,-8.890303]],[[7.713260,5.530448,4.801514,0.487488,-3.363882,8.840752,-4.643070,5.582678,-5.911987],[7.959357,-7.986241,7.931235,1.360628,-3.967491,-2.652132,7.899551,7.794003,5.421155],[-9.749348,1.750085,-6.068318,8.287451,-5.675303,-8.679640,-3.796053,-0.981151,9.981403],[8.915025,5.710338,8.991466,0.132338,1.812969,7.797108,8.236865,8.677628,-4.035089],[0.859215,2.349037,-7.510242,-5.316601,8.591710,-0.297469,-3.087292,4.888686,1.685400],[7.679421,6.563642,7.569701,2.066690,8.169180,-8.186086,-0.401266,7.081952,9.580762],[-1.733745,-8.279874,-2.239051,-7.086501,-5.836089,-3.112414,6.647382,-8.905606,6.869161],[2.243106,-1.372108,1.295650,9.653443,-4.380364,7.768584,-7.610334,9.959742,7.404859],[9.877774,-5.932354,-0.851305,9.170595,-3.260346,-1.924585,-5.135642,9.910169,-8.279116],[3.475936,-6.256638,-7.248715,9.542053,1.715730,9.486269,-2.776327,7.981628,0.181793],[-6.698065,4.145948,-1.879415,-6.076104,1.890255,-1.468315,-7.325533,4.987935,1.974680],[9.863067,6.950716,-6.163708,6.741301,9.702096,5.201727,-3.958022,-4.507558,7.260120],[-4.010044,9.582421,9.024685,0.358337,5.723627,-3.750970,1.832656,8.169538,2.214816],[9.961702,-4.174859,0.369541,6.493522,7.843315,2.147245,3.668142,-1.444899,1.813425]],[[-2.851036,-4.753323,-1.882718,-1.688262,-7.549914,-8.507819,2.847020,-8.974380,-4.019853],[-7.396301,-0.992857,2.815595,-3.385811,1.387656,0.062734,-8.444236,8.496517,1.099085],[5.680919,9.158914,1.189388,2.979123,-2.061158,6.598847,8.613537,-2.163362,5.865976],[1.141100,-3.620545,6.522759,-5.021245,8.366310,-0.700611,2.303699,9.745199,4.513963],[-3.993018,5.310721,-7.846941,4.541928,-5.203278,9.998161,-1.724811,3.895736,1.726417],[-2.542064,-5.411069,-5.481381,9.937846,9.440329,-2.474662,8.362711,5.521390,5.129708],[4.570268,-3.954868,8.659643,-6.738916,-1.743277,-4.171002,-8.582222,0.184199,0.157241],[5.257380,1.695554,1.002349,4.899160,-8.267659,5.640533,-7.231259,6.970525,3.523099],[3.224239,-2.640236,8.497940,1.728112,5.348241,3.724449,-9.133768,2.443082,7.110292],[-5.795965,-9.501528,0.301440,-5.633225,-8.428817,-9.906323,-8.366228,0.090521,-4.783463],[-8.491182,-6.007526,-0.756516,-2.791002,-4.441924,9.133787,-0.899761,-2.999667,-2.590330],[-7.614081,-9.116735,-3.896675,-4.103056,-9.904328,0.231476,7.848552,-7.670709,-6.889068],[4.688741,-2.889303,-0.482465,3.200620,9.483559,9.224461,2.924278,-3.113823,3.362269],[9.154009,-2.578848,2.194999,-2.650141,7.011377,2.711006,7.570423,-0.331660,-9.655748]],[[9.350957,8.432576,-7.704264,3.783283,-2.672394,0.628807,-9.355207,-8.701003,-5.224346],[1.896768,-6.784015,5.828676,-3.112685,-2.577909,-0.809048,2.318357,-3.454267,-5.918422],[-6.814596,-4.844832,-9.560593,-2.661600,-5.033289,3.216553,-5.548437,2.586216,7.864597],[-6.004334,-3.101279,-7.553833,-5.605365,-9.956233,-5.663822,0.460931,-3.044231,9.623887],[8.907455,-3.591448,-7.351774,-4.209439,-5.543507,4.747012,-0.446800,7.039576,-3.752408],[-9.808857,2.651490,6.947088,4.447982,-7.421392,3.839756,-8.319018,6.971611,-2.257571],[-9.787032,8.206810,3.570958,-7.292718,-3.319372,-6.931473,3.852183,4.592725,6.108926],[-1.004018,5.628732,9.490288,7.724427,6.749991,-8.795381,-4.620763,-4.651666,0.865199],[9.246586,-9.526312,0.728208,-0.745438,1.104168,0.224794,5.526395,7.460221,7.015752],[3.223006,0.603419,7.594109,-5.792496,-7.423708,9.518866,-9.782437,-8.469044,4.720871],[0.051083,-1.747834,6.727420,-3.088933,-2.790217,-9.544828,-6.508372,-8.923488,-2.971948],[3.699109,9.178306,-6.607447,6.922071,5.507777,1.291167,9.430103,1.462939,3.412004],[2.790263,8.088059,9.188903,5.296290,3.406793,3.625724,-2.596977,-5.531820,5.559688],[-2.207466,-9.846910,-6.387493,-8.676411,-2.741052,1.266847,8.860504,0.908068,-6.876688]],[[-5.325070,-2.286669,4.267759,2.002135,-6.531473,-9.886982,-7.999495,-7.557228,-9.423986],[-6.650606,-4.435223,-4.737444,-5.249914,2.411443,-8.871767,5.609561,0.641394,-0.928445],[1.393125,-0.125489,-2.038670,8.442904,-5.058009,9.412529,-3.595526,0.260194,-2.262539],[8.170615,0.441958,7.452943,-1.058683,-6.789352,-7.996728,8.398585,4.323235,-9.892630],[-0.077775,-1.429087,0.738022,0.884566,-4.112404,8.470695,4.424568,5.220499,1.787642],[-6.385241,2.632758,4.439050,-1.282075,-8.837138,9.107154,2.023960,-6.271414,-8.481584],[7.361677,-1.590690,-7.661675,-7.722269,-4.198525,5.869102,-1.533984,3.669580,-1.208599],[-0.898423,3.521437,-1.502585,5.466461,-3.063550,-9.798196,8.584504,8.122398,0.616537],[7.938031,7.362643,7.418228,1.617799,-3.995648,-0.690889,-7.452868,4.374622,1.928433],[-1.569288,0.916843,-7.453146,6.864370,0.615170,8.841867,-1.632413,3.080880,-1.251213],[-7.415799,-2.235202,1.105145,-2.444764,2.854235,7.085106,9.193276,2.341873,7.033836],[-5.033075,-2.087866,1.746284,-9.327208,-7.566260,0.534730,0.280216,9.847644,-2.679398],[-9.658492,-1.016699,9.107431,-3.824124,7.303892,1.995548,5.147416,2.561181,-2.320082],[-6.423334,-2.062852,-2.053710,7.170804,-7.334019,3.966898,8.481202,0.294804,-7.528908]],[[-2.573225,0.460342,-1.471318,-3.349831,3.684995,1.966855,-8.027131,-2.440812,0.500070],[-1.489340,-5.730668,5.827701,4.561007,6.091839,-9.405922,3.408477,-8.534467,-5.633715],[-7.152402,7.063398,-5.335215,2.172050,-8.785702,1.777582,-3.052347,-1.048410,-5.821721],[-8.105169,4.751405,-5.621001,9.791900,-7.411015,2.106887,9.181067,7.771047,7.629411],[2.995185,-2.205330,-9.463495,9.040573,4.274121,-0.127395,7.334502,6.392220,-9.111882],[-0.747749,-0.545210,-9.892975,9.305914,5.352860,-3.449225,-5.050067,6.342767,7.124172],[1.554934,-7.238317,-1.412945,-0.196561,0.831061,-1.487155,-3.222109,-7.091114,8.517105],[-4.611643,-4.772400,1.937188,-5.186774,-3.818824,-3.292520,9.011785,5.950590,-3.243849],[-7.913595,5.657590,0.022221,-5.410489,6.425932,-2.058688,6.279285,2.329236,-2.367180],[-0.883531,9.238010,-0.005750,-1.141385,1.364714,0.743961,0.475978,-9.994429,7.599481],[6.761111,8.401538,-8.216283,4.782727,-7.667204,5.713906,-0.944066,1.561856,7.146667],[8.367140,-2.522825,4.048670,4.414403,5.267061,9.261693,6.136087,-7.404182,7.730369],[-8.087450,-4.785519,-3.238475,2.024938,4.057181,-4.135624,-8.887197,-9.973313,-4.177055],[-0.779303,8.215537,4.293630,-2.155172,0.834058,-1.851956,-9.120156,5.507506,6.302778]],[[-0.363192,-1.629713,-0.451108,-4.891482,3.099224,5.112155,-3.419936,2.268428,6.125739],[7.066495,7.241075,3.028439,3.577083,-9.627141,-9.871977,-4.068487,-2.095426,9.431198],[5.134274,7.664493,-1.416162,-3.793612,-6.158823,-3.660260,2.851497,8.661696,-5.992308],[-8.353002,-6.658427,6.146077,-1.304278,-3.244160,-4.321441,7.133520,9.286946,-4.061919],[0.183318,1.773508,-6.710412,-8.355769,3.509243,-3.510267,-6.015565,5.850100,0.777553],[9.683871,8.307472,-4.547847,2.523514,8.868702,-9.741867,8.776215,4.523653,0.072303],[-3.763944,4.814320,-1.276578,-3.930783,-4.120879,5.910140,-7.853876,9.587087,-2.780891],[0.518574,-9.880302,7.602175,6.362681,-6.843837,9.410673,-0.968708,7.628961,6.821836],[-7.688166,-5.093491,2.475525,-8.144404,6.380223,7.489864,-9.293853,2.168279,-0.859488],[5.407827,8.738487,-3.192809,-8.004359,2.771512,-0.619747,3.509041,-7.502807,1.936261],[9.460536,6.392487,7.899718,7.418002,9.239353,-3.376140,3.806954,5.925849,-5.629956],[7.415483,7.022279,-8.903971,3.471968,-0.292559,-3.398208,9.066609,8.685877,-7.872402],[-0.409100,-0.550695,-3.323775,5.274557,5.914284,7.760997,-9.490019,-9.389164,2.999053],[9.247405,-6.089124,-7.342492,0.613944,-4.360534,-2.700441,9.862558,-5.048660,-8.241795]],[[0.463671,-0.603552,7.820360,-9.065975,-4.868808,3.409189,3.761606,-5.438928,-9.613083],[-0.796266,1.720661,-1.138406,4.434317,-5.026441,-7.746873,5.207335,-6.464395,-1.509087],[2.898846,6.926485,0.987658,4.238259,9.233539,-0.356128,-2.793659,1.165822,2.772849],[0.097666,9.861610,9.177332,-5.208168,5.682007,-1.117162,-6.426646,-7.410916,-3.744567],[-1.968323,2.279149,7.641824,7.416570,-3.935989,2.914838,1.601682,2.944043,-8.282086],[-7.887605,8.844327,5.378497,3.154076,2.419932,7.763753,8.750659,3.153085,0.744087],[-6.092563,-4.977775,2.458177,-9.721251,-0.331378,-0.897023,-3.072549,7.685099,-2.255103],[-5.445744,5.240340,-5.292024,4.949257,-1.521791,-6.953544,5.543472,0.791470,5.671064],[-5.623745,1.225643,5.553034,1.007071,-7.763761,1.377237,-5.458994,-7.925357,6.721652],[-9.009212,-9.784422,6.876826,6.386108,1.197774,-8.490556,0.967115,-9.586806,8.478864],[-2.206582,-0.011720,-6.179030,-4.953388,3.248740,-5.909746,8.217155,4.541376,9.309346],[-1.872787,6.427483,6.200075,-7.912433,-3.609009,9.832272,6.573901,5.123181,-3.115487],[8.983062,-2.109971,1.376666,-2.447704,0.905572,-2.169282,-3.840449,6.416656,-1.199350],[-2.503956,-0.239706,-7.202247,-6.136126,4.819962,6.201222,4.951619,-6.158620,5.674470]],[[-8.044557,-4.127643,2.866593,1.248367,9.259514,3.097765,2.280428,0.129096,7.714944],[-9.576269,6.699908,1.546392,6.526230,8.380240,-0.550600,-9.218045,-6.297137,-2.712560],[6.466078,-8.069836,8.010128,5.491357,2.928188,-0.967939,-2.740737,-7.409099,-2.129541],[-0.331687,7.682550,-3.860458,-7.637835,-3.113715,0.336402,-1.755094,-2.475965,-0.346570],[-9.295461,4.106000,-1.315038,-9.019122,-6.385505,-5.475799,-2.550828,-4.484516,-4.455068],[3.728141,1.516928,-4.939047,4.312272,-0.785485,5.778360,2.199475,-5.638820,1.510075],[-9.625611,8.880662,-6.230182,7.509480,-9.413167,-6.915232,-2.476939,9.339503,-2.462881],[8.508225,-7.596822,2.696119,-5.805499,1.304119,1.027512,1.797415,1.004428,-4.797778],[-2.551904,-4.031868,-8.609845,1.558092,8.202365,-9.846059,-9.687571,9.353856,5.335010],[-8.798238,1.493714,-9.199683,-3.660171,-8.297140,-4.706373,-4.039436,-5.484161,2.991329],[7.519307,-2.548635,7.317626,-2.643797,-1.554027,-1.493195,8.318728,9.442032,6.823634],[6.646755,2.888289,9.173239,4.322768,-3.449743,-7.651427,-6.042527,-2.131542,-9.530780],[4.362879,-0.225131,-5.596954,-8.952831,9.924810,-0.805655,1.915243,8.725667,7.064597],[0.638355,-0.080131,6.487394,8.082603,-9.946825,-9.318440,-2.521424,-7.970996,9.901341]],[[6.331195,-4.834535,0.949351,1.292157,-8.212865,1.510349,8.535290,-1.096811,-2.615077],[1.328962,5.259225,1.550805,-5.530871,-0.298491,-9.072880,-9.342922,4.082060,2.674405],[8.907847,5.219659,6.164318,-6.825279,0.615244,-6.440731,-6.388492,-1.165743,3.027605],[8.321671,0.193437,-2.600066,7.071653,5.970978,2.346671,7.811528,-2.326218,4.570691],[5.231530,-7.099702,-5.676091,-9.534897,-8.734922,3.148715,-0.485616,-0.606168,-7.881466],[-7.915555,4.040571,-2.173490,-3.678615,5.380270,-2.600530,-5.784028,-0.136214,8.859789],[1.916852,2.271023,-2.313192,6.172836,1.157152,-0.393950,0.778044,4.382533,-7.796331],[8.930030,1.280306,2.114876,3.431497,3.766879,9.268695,8.285826,-7.477123,-2.260893],[3.667345,-2.246535,4.797228,-8.935521,0.831421,7.272042,3.855120,-8.643726,-4.893677],[-9.965658,4.862605,1.374691,-1.797578,3.313912,-2.679647,1.121154,6.902632,-2.975720],[-7.496204,1.434703,7.973427,-0.556906,-2.559900,3.954319,-2.656581,-4.750557,-0.248312],[-7.203607,-5.991335,6.603080,-4.922823,-7.593338,-8.745890,-1.018111,6.108039,-0.169373],[5.582557,3.224954,0.316612,-6.534382,7.259179,1.681066,-8.275642,-0.100739,8.573747],[9.563922,1.718356,-7.631692,9.612252,-5.533333,-2.319279,2.416099,6.472922,4.869701]],[[4.479254,4.283968,4.505168,-9.508441,-9.885800,-6.491681,7.765963,8.681497,-6.300267],[-3.689485,0.689312,-3.836258,-1.716455,4.404021,1.814295,-6.398934,-6.721879,6.093658],[0.908108,4.529386,-5.854063,2.034835,-9.537396,-7.554118,-7.881677,-4.763724,-4.479778],[-8.552252,-2.033043,-9.684982,-7.830388,-2.037026,-2.693071,-6.824365,-4.999991,-0.199356],[-5.904306,-7.045276,-2.738344,3.723214,2.623681,-0.164208,-6.876810,-0.063944,-5.210808],[-1.004890,-2.079693,7.865764,-6.010239,-0.626056,-5.475607,-7.275518,-0.081786,1.833812],[8.203498,-8.540065,-7.927492,-3.068987,0.813628,0.439358,-6.464955,-4.779768,-0.211767],[6.522857,-0.511530,4.912232,-3.993495,5.281532,-4.154269,-6.878540,7.741150,2.706332],[5.728879,-2.424649,-1.057280,4.576405,-1.408655,9.858345,6.787059,8.607106,-5.578716],[-1.400744,-6.310433,-5.059062,-7.529971,5.679368,1.531145,3.730605,-5.700282,0.870280],[6.506057,0.490344,-8.941296,4.461444,-9.166524,2.902074,3.189743,5.584659,7.246742],[5.414875,-0.503200,0.949024,7.936914,9.649334,3.349832,-5.237658,4.442679,-8.895121],[3.405912,4.743634,-9.830131,-8.895671,4.831805,-3.589946,7.971800,-3.057178,-7.068754],[7.685300,0.268979,6.414551,8.921652,9.611509,-2.473448,6.417871,8.618544,4.166134]],[[1.803776,-1.771036,6.084124,-9.163749,-0.214516,3.549683,-1.892209,-2.316439,5.977897],[-8.633924,0.684736,3.484384,2.674342,9.383701,8.552174,7.584235,5.653141,9.023579],[-6.062466,9.886934,6.296455,0.332241,-3.457973,5.407845,7.780262,-5.229093,8.612209],[-9.961478,-7.910144,-1.317019,-9.010969,4.305171,9.004953,8.664502,-3.076056,-3.573615],[6.997831,3.719272,9.693199,4.377058,5.037116,3.452387,3.870018,2.687280,-7.153667],[2.769751,2.170617,-5.087043,-6.980373,-6.808480,-3.157306,-5.321854,-6.241377,0.050519],[-2.852429,4.416431,5.597272,-6.426997,-3.906045,-5.250504,2.316683,-9.415857,-4.013455],[9.037712,-0.796630,5.886865,-9.228771,-5.869968,-9.125853,-1.831256,-6.318244,-3.650544],[7.324121,-8.238803,-5.644912,-1.484435,-8.372140,4.486328,0.352113,9.259829,-6.982750],[-4.177184,-4.859129,-0.999763,4.395636,9.928782,-2.172594,5.791208,1.360461,2.882548],[-6.280886,9.714882,-4.013536,-3.994010,-4.249997,0.035991,-6.619057,2.446519,-6.491918],[1.561906,4.213179,7.579131,-3.546922,8.873539,-9.059085,-8.005102,-1.936056,-3.639097],[-3.198490,-9.749863,-7.497000,9.452807,5.264489,-6.315495,-2.690675,0.749396,-3.978525],[6.174762,8.375789,-9.709506,-9.378994,3.430237,0.280511,2.845729,-1.975237,-0.307649]],[[-2.486532,8.959872,-8.296621,0.834423,-2.943417,-7.999896,-5.966124,1.745725,-0.343757],[8.340866,-9.133666,3.880949,-4.208228,8.356751,-2.192099,-5.172323,-1.594924,3.388842],[0.605258,9.171015,7.014178,-0.222600,-3.715385,-8.503812,-5.214373,8.025701,-9.058442],[-8.380984,8.728537,0.699383,1.072423,-2.595830,7.003060,-1.464313,1.228505,-8.030198],[-2.297966,-4.623611,9.049402,2.521862,-9.647657,-5.115532,-6.651017,-9.368581,8.311110],[5.637955,7.282009,-3.474216,8.389136,2.995268,-9.546346,-4.635023,-9.235601,0.455131],[6.860133,8.343349,1.517074,-7.100442,-2.105996,-4.388583,-4.911182,-4.522364,0.035215],[-5.828917,-1.075220,7.215864,-6.945382,7.599304,-3.088800,-2.592122,0.515502,-2.781892],[3.863521,-7.400433,6.143173,9.873537,5.860925,5.652165,-6.803037,0.545175,8.689453],[-5.170361,-9.200147,-1.626479,-6.924432,-1.697234,0.530950,8.717941,7.327981,-2.102344],[-5.255937,-1.312187,-1.389813,-7.851934,-3.154531,2.795807,3.635446,7.028457,6.690074],[-3.882999,-4.725403,2.473643,2.920208,-2.142702,4.851109,9.627678,6.073311,5.758144],[3.967651,-9.986932,4.280741,8.114816,2.965882,9.445545,3.797196,5.266726,-3.274657],[2.919173,0.846159,0.702267,-2.707274,-7.013267,-8.180990,9.060873,4.808313,3.420016]]], dtype = "float64")#candidate|5328|(16, 14, 9)|const|float64
bop_5329 = relay.not_equal(uop_5317.astype('bool'), relay.reshape(const_5328.astype('bool'), relay.shape_of(uop_5317))) # shape=(16, 14, 9)
output = bop_5329
output2 = bop_5329
F = relay.Function([var_5316,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5316,], output2)
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
