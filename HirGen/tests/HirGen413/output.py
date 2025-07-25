import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_85 = relay.const(9, dtype = "uint8")#candidate|85|()|const|uint8
const_86 = relay.const([[[-7,-6,-2,8],[4,3,-5,6],[-10,6,1,-9],[5,-3,-2,-4],[-1,-7,-1,6],[-10,1,-9,1],[-1,-7,4,-7],[3,-7,-6,-3]],[[-1,-1,9,8],[-4,5,3,-5],[2,9,7,4],[-7,-4,-1,-9],[9,-5,-7,8],[-1,7,8,10],[-3,7,-4,-7],[-1,5,9,-4]],[[-6,-9,-1,4],[-9,-6,2,-8],[-5,-4,-7,2],[-3,-1,3,-5],[2,1,10,-5],[-8,-7,-7,7],[3,10,2,9],[1,10,-3,4]],[[-8,1,2,-8],[-7,5,1,5],[-1,3,7,9],[-9,-3,-1,-2],[-3,8,10,-8],[-2,-2,-2,6],[-10,-7,10,-6],[-4,-5,-5,5]],[[-9,3,-10,6],[-5,6,5,-3],[2,3,-5,-2],[7,5,4,10],[-4,3,-6,-7],[-7,-8,-6,9],[-2,-9,-1,-7],[10,-2,1,-8]],[[-5,-8,-9,-3],[9,-1,4,-10],[-2,3,-4,4],[10,6,8,-6],[-4,7,1,-10],[-1,3,8,-10],[-6,6,3,2],[7,-7,-4,9]],[[7,-1,-6,-9],[9,2,7,10],[7,1,-7,5],[3,-9,5,6],[4,2,-8,8],[-3,7,-2,-3],[-4,-1,9,4],[-8,-10,-1,-4]],[[-4,6,7,9],[4,-10,-6,9],[9,-2,-4,4],[-9,4,3,-6],[8,8,8,5],[-7,2,2,-3],[9,-1,2,-6],[10,-3,-2,9]],[[-3,-5,-6,4],[-7,-5,8,-2],[-5,-2,8,10],[-10,2,-1,1],[-8,6,-7,7],[7,-3,-2,-1],[-7,4,3,-7],[8,-6,-2,3]],[[-3,6,-9,6],[-5,-10,5,1],[-8,-1,-10,7],[-8,7,2,-10],[10,7,-8,-5],[1,7,-1,-9],[-7,2,-7,-5],[2,6,1,10]],[[-3,1,1,4],[5,9,-4,-5],[-9,6,5,-2],[3,-4,-6,-8],[-3,-2,-8,6],[10,9,4,-4],[-2,8,4,-8],[-9,-3,-7,6]],[[1,4,-6,3],[8,3,6,4],[8,7,3,8],[8,-1,-2,6],[-6,-5,3,-2],[9,-4,1,-7],[1,2,9,-9],[1,1,6,-1]],[[8,-7,-3,1],[-2,-1,4,-3],[-1,-2,-5,7],[-1,-1,4,9],[7,2,-5,-6],[-1,-2,-4,-1],[-2,-5,-3,2],[9,-1,7,-6]],[[6,-4,4,-7],[-6,9,6,5],[2,-4,2,-1],[1,-7,-1,-3],[-2,5,-7,-10],[-1,-5,10,2],[1,9,4,-6],[1,5,8,-7]]], dtype = "uint8")#candidate|86|(14, 8, 4)|const|uint8
bop_87 = relay.equal(const_85.astype('bool'), const_86.astype('bool')) # shape=(14, 8, 4)
output = relay.Tuple([bop_87,])
output2 = relay.Tuple([bop_87,])
func_108 = relay.Function([], output)
mod['func_108'] = func_108
mod = relay.transform.InferType()(mod)
mutated_mod['func_108'] = func_108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mutated_mod.get_global_var('func_108')
call_109 = func_108_call()
output = call_109
func_110 = relay.Function([], output)
mutated_mod['func_110'] = func_110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_206 = relay.TupleGetItem(func_108_call(), 0)
call_207 = relay.TupleGetItem(func_110_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_219 = relay.TupleGetItem(func_108_call(), 0)
call_220 = relay.TupleGetItem(func_110_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_225 = relay.TupleGetItem(func_108_call(), 0)
call_226 = relay.TupleGetItem(func_110_call(), 0)
output = relay.Tuple([call_206,call_219,call_225,])
output2 = relay.Tuple([call_207,call_220,call_226,])
func_235 = relay.Function([], output)
mod['func_235'] = func_235
mod = relay.transform.InferType()(mod)
mutated_mod['func_235'] = func_235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mutated_mod.get_global_var('func_235')
call_236 = func_235_call()
output = call_236
func_237 = relay.Function([], output)
mutated_mod['func_237'] = func_237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_261 = relay.TupleGetItem(func_108_call(), 0)
call_262 = relay.TupleGetItem(func_110_call(), 0)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_264 = relay.TupleGetItem(func_235_call(), 2)
call_265 = relay.TupleGetItem(func_237_call(), 2)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_287 = relay.TupleGetItem(func_108_call(), 0)
call_288 = relay.TupleGetItem(func_110_call(), 0)
var_294 = relay.var("var_294", dtype = "bool", shape = (14, 8, 4))#candidate|294|(14, 8, 4)|var|bool
bop_295 = relay.subtract(call_264.astype('uint32'), relay.reshape(var_294.astype('uint32'), relay.shape_of(call_264))) # shape=(14, 8, 4)
bop_298 = relay.subtract(call_265.astype('uint32'), relay.reshape(var_294.astype('uint32'), relay.shape_of(call_265))) # shape=(14, 8, 4)
output = relay.Tuple([call_261,call_287,bop_295,])
output2 = relay.Tuple([call_262,call_288,bop_298,])
func_300 = relay.Function([var_294,], output)
mod['func_300'] = func_300
mod = relay.transform.InferType()(mod)
var_301 = relay.var("var_301", dtype = "bool", shape = (14, 8, 4))#candidate|301|(14, 8, 4)|var|bool
output = func_300(var_301)
func_302 = relay.Function([var_301], output)
mutated_mod['func_302'] = func_302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_343 = relay.var("var_343", dtype = "float32", shape = (11, 10, 8))#candidate|343|(11, 10, 8)|var|float32
uop_344 = relay.log10(var_343.astype('float32')) # shape=(11, 10, 8)
bop_361 = relay.left_shift(uop_344.astype('int8'), relay.reshape(var_343.astype('int8'), relay.shape_of(uop_344))) # shape=(11, 10, 8)
uop_364 = relay.sqrt(bop_361.astype('float32')) # shape=(11, 10, 8)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_370 = relay.TupleGetItem(func_108_call(), 0)
call_371 = relay.TupleGetItem(func_110_call(), 0)
uop_384 = relay.log2(var_343.astype('float64')) # shape=(11, 10, 8)
func_300_call = mod.get_global_var('func_300')
func_302_call = mutated_mod.get_global_var('func_302')
call_391 = relay.TupleGetItem(func_300_call(relay.reshape(call_370.astype('bool'), [14, 8, 4])), 2)
call_392 = relay.TupleGetItem(func_302_call(relay.reshape(call_370.astype('bool'), [14, 8, 4])), 2)
bop_394 = relay.bitwise_xor(uop_364.astype('int16'), relay.reshape(bop_361.astype('int16'), relay.shape_of(uop_364))) # shape=(11, 10, 8)
uop_398 = relay.asin(bop_361.astype('float64')) # shape=(11, 10, 8)
var_416 = relay.var("var_416", dtype = "float32", shape = (11, 10, 8))#candidate|416|(11, 10, 8)|var|float32
bop_417 = relay.maximum(uop_364.astype('int16'), relay.reshape(var_416.astype('int16'), relay.shape_of(uop_364))) # shape=(11, 10, 8)
output = relay.Tuple([call_370,uop_384,call_391,bop_394,uop_398,bop_417,])
output2 = relay.Tuple([call_371,uop_384,call_392,bop_394,uop_398,bop_417,])
func_435 = relay.Function([var_343,var_416,], output)
mod['func_435'] = func_435
mod = relay.transform.InferType()(mod)
mutated_mod['func_435'] = func_435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_435_call = mutated_mod.get_global_var('func_435')
var_437 = relay.var("var_437", dtype = "float32", shape = (11, 10, 8))#candidate|437|(11, 10, 8)|var|float32
var_438 = relay.var("var_438", dtype = "float32", shape = (11, 10, 8))#candidate|438|(11, 10, 8)|var|float32
call_436 = func_435_call(var_437,var_438,)
output = call_436
func_439 = relay.Function([var_437,var_438,], output)
mutated_mod['func_439'] = func_439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_465 = relay.TupleGetItem(func_235_call(), 0)
call_466 = relay.TupleGetItem(func_237_call(), 0)
var_469 = relay.var("var_469", dtype = "bool", shape = (14, 8, 4))#candidate|469|(14, 8, 4)|var|bool
bop_470 = relay.less(call_465.astype('bool'), relay.reshape(var_469.astype('bool'), relay.shape_of(call_465))) # shape=(14, 8, 4)
bop_473 = relay.less(call_466.astype('bool'), relay.reshape(var_469.astype('bool'), relay.shape_of(call_466))) # shape=(14, 8, 4)
output = bop_470
output2 = bop_473
func_481 = relay.Function([var_469,], output)
mod['func_481'] = func_481
mod = relay.transform.InferType()(mod)
var_482 = relay.var("var_482", dtype = "bool", shape = (14, 8, 4))#candidate|482|(14, 8, 4)|var|bool
output = func_481(var_482)
func_483 = relay.Function([var_482], output)
mutated_mod['func_483'] = func_483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_536 = relay.TupleGetItem(func_108_call(), 0)
call_537 = relay.TupleGetItem(func_110_call(), 0)
func_300_call = mod.get_global_var('func_300')
func_302_call = mutated_mod.get_global_var('func_302')
call_544 = relay.TupleGetItem(func_300_call(relay.reshape(call_536.astype('bool'), [14, 8, 4])), 0)
call_545 = relay.TupleGetItem(func_302_call(relay.reshape(call_536.astype('bool'), [14, 8, 4])), 0)
var_559 = relay.var("var_559", dtype = "bool", shape = (14, 8, 4))#candidate|559|(14, 8, 4)|var|bool
bop_560 = relay.logical_or(call_536.astype('bool'), relay.reshape(var_559.astype('bool'), relay.shape_of(call_536))) # shape=(14, 8, 4)
bop_563 = relay.logical_or(call_537.astype('bool'), relay.reshape(var_559.astype('bool'), relay.shape_of(call_537))) # shape=(14, 8, 4)
output = relay.Tuple([call_544,bop_560,])
output2 = relay.Tuple([call_545,bop_563,])
func_569 = relay.Function([var_559,], output)
mod['func_569'] = func_569
mod = relay.transform.InferType()(mod)
mutated_mod['func_569'] = func_569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_570 = relay.var("var_570", dtype = "bool", shape = (14, 8, 4))#candidate|570|(14, 8, 4)|var|bool
func_569_call = mutated_mod.get_global_var('func_569')
call_571 = func_569_call(var_570)
output = call_571
func_572 = relay.Function([var_570], output)
mutated_mod['func_572'] = func_572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_622 = relay.TupleGetItem(func_235_call(), 1)
call_623 = relay.TupleGetItem(func_237_call(), 1)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_639 = relay.TupleGetItem(func_108_call(), 0)
call_640 = relay.TupleGetItem(func_110_call(), 0)
const_644 = relay.const([[[False,False,True,True],[False,False,True,False],[False,False,False,True],[True,False,False,True],[False,False,True,True],[True,True,True,False],[False,False,False,False],[True,False,True,False]],[[True,False,True,True],[False,False,True,True],[False,True,False,True],[False,True,False,False],[True,False,True,False],[True,True,True,True],[True,True,False,False],[False,True,False,True]],[[True,True,False,True],[True,False,False,True],[True,True,False,True],[False,True,True,True],[True,True,False,False],[False,True,False,True],[False,False,True,False],[True,False,True,False]],[[True,False,True,True],[False,False,False,True],[True,True,True,True],[False,False,False,True],[True,False,True,True],[True,True,False,False],[True,False,False,False],[False,False,False,True]],[[False,False,False,False],[False,True,True,True],[False,False,False,False],[True,False,True,False],[True,False,False,False],[False,False,False,True],[False,True,False,False],[True,False,False,True]],[[False,False,True,False],[True,False,True,True],[True,True,True,False],[False,False,False,True],[True,False,True,True],[True,False,False,True],[True,False,False,False],[True,False,True,True]],[[False,False,False,False],[False,True,True,True],[True,True,True,True],[True,False,False,False],[False,True,True,True],[True,False,True,False],[False,True,False,True],[True,True,True,True]],[[True,True,True,False],[False,True,True,True],[False,True,False,True],[True,False,False,True],[False,True,True,True],[True,False,False,False],[True,False,True,False],[False,False,True,True]],[[True,True,True,False],[False,True,True,False],[False,False,True,True],[False,True,False,False],[True,True,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False]],[[True,True,False,True],[False,True,True,False],[True,False,True,False],[False,False,False,True],[True,False,True,True],[False,False,True,True],[False,False,True,False],[False,True,False,True]],[[True,False,False,True],[False,True,False,True],[True,True,True,True],[True,False,False,True],[False,False,False,True],[False,True,False,False],[True,True,False,True],[True,True,False,False]],[[True,False,True,True],[True,True,True,True],[True,False,False,False],[False,True,True,True],[True,True,False,True],[True,False,True,False],[True,True,False,False],[False,False,False,False]],[[True,False,True,False],[True,False,True,False],[True,False,True,True],[True,False,False,False],[False,False,True,True],[False,False,True,False],[True,True,False,False],[False,True,False,True]],[[True,True,True,False],[False,True,True,True],[True,False,False,False],[False,True,False,False],[True,True,True,False],[True,True,False,False],[False,False,False,False],[True,False,True,False]]], dtype = "bool")#candidate|644|(14, 8, 4)|const|bool
bop_645 = relay.divide(call_639.astype('float64'), relay.reshape(const_644.astype('float64'), relay.shape_of(call_639))) # shape=(14, 8, 4)
bop_648 = relay.divide(call_640.astype('float64'), relay.reshape(const_644.astype('float64'), relay.shape_of(call_640))) # shape=(14, 8, 4)
output = relay.Tuple([call_622,bop_645,])
output2 = relay.Tuple([call_623,bop_648,])
func_650 = relay.Function([], output)
mod['func_650'] = func_650
mod = relay.transform.InferType()(mod)
mutated_mod['func_650'] = func_650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mutated_mod.get_global_var('func_650')
call_651 = func_650_call()
output = call_651
func_652 = relay.Function([], output)
mutated_mod['func_652'] = func_652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_703 = relay.TupleGetItem(func_235_call(), 0)
call_704 = relay.TupleGetItem(func_237_call(), 0)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_711 = relay.TupleGetItem(func_650_call(), 0)
call_712 = relay.TupleGetItem(func_652_call(), 0)
output = relay.Tuple([call_703,call_711,])
output2 = relay.Tuple([call_704,call_712,])
func_713 = relay.Function([], output)
mod['func_713'] = func_713
mod = relay.transform.InferType()(mod)
output = func_713()
func_714 = relay.Function([], output)
mutated_mod['func_714'] = func_714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_723 = relay.TupleGetItem(func_108_call(), 0)
call_724 = relay.TupleGetItem(func_110_call(), 0)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_733 = relay.TupleGetItem(func_235_call(), 0)
call_734 = relay.TupleGetItem(func_237_call(), 0)
output = relay.Tuple([call_723,call_733,])
output2 = relay.Tuple([call_724,call_734,])
func_735 = relay.Function([], output)
mod['func_735'] = func_735
mod = relay.transform.InferType()(mod)
mutated_mod['func_735'] = func_735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mutated_mod.get_global_var('func_735')
call_736 = func_735_call()
output = call_736
func_737 = relay.Function([], output)
mutated_mod['func_737'] = func_737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_766 = relay.TupleGetItem(func_713_call(), 1)
call_767 = relay.TupleGetItem(func_714_call(), 1)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_784 = relay.TupleGetItem(func_713_call(), 0)
call_785 = relay.TupleGetItem(func_714_call(), 0)
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
const_789 = relay.const([[8.400313,6.365848,1.556292,-6.682714,-0.933127,1.869571,6.979499,-4.967420,-7.225302,5.741409,1.716997,6.430517,-3.457957,-9.286860,-4.368176,5.605958,1.015081,-4.148534,9.532094,1.432626,-5.454135,6.255052,-4.193651,-0.073748,-2.063837,-4.795371,2.165333,-7.693314,6.257248,3.502264,-4.023218,9.584259,9.960151,-4.880218,9.158382,-3.147560,-3.463953,1.565158,0.607434,2.787991,1.835561,6.657896,6.080610,-1.844055,-9.103018,-8.300723,7.589594,4.107602,5.298579,7.289436,8.872463,7.033301,8.819172,-5.426335,-1.275690,4.377716,0.357831,-2.293592,-4.739535,5.107991,-2.092881,2.470467,-0.667864,-9.658921,-5.372272,-0.728247,0.575586,3.757097,-6.275706,7.557167,1.377842,-1.138817,-0.333338,-2.728447,4.753201,2.506801,6.833404,9.289000,1.623161,-4.192129,6.101695,2.361904,-1.362078,-4.341550,-7.873362,4.033869,-2.889855,5.595265,-8.226102,3.601059,5.660489,-7.987643,-5.088695,-7.609227,3.489722,9.333832,8.309774,-1.420797,-3.660110,-8.142121,-5.933431,-4.834077,3.646891,8.057600,5.860054,-8.655307,-7.702938,-9.915680,-6.309419,-3.590475],[1.558426,1.351279,9.899939,-9.548615,-2.635837,-2.438159,-5.834160,3.973248,-6.165590,2.774852,8.424431,2.069148,-0.954636,-4.742769,-4.371647,8.831713,8.801435,5.041237,-5.716278,-6.397187,-4.464393,9.710245,1.369166,8.378160,-5.237668,-5.755034,-1.675756,7.597202,4.609122,9.422308,-3.880977,5.688057,3.228965,-3.324387,-6.305387,-7.615051,-9.756003,6.950114,-1.683482,1.873055,4.479639,6.397402,6.045412,6.750101,-0.257086,3.650381,0.100689,-3.197257,2.045458,-8.224226,0.534426,-8.680570,-1.399414,-4.083568,-7.986496,5.982756,4.226108,7.789784,2.892494,2.793516,-1.492835,1.020372,8.467324,-0.470573,-9.171108,-1.396294,-9.511929,9.755767,-5.866973,9.376017,-4.139559,-3.406796,2.882038,-2.307331,-2.730657,0.094163,-4.306831,-7.338841,-7.679048,-1.648911,4.746466,4.559544,-3.566863,1.751917,-9.070892,4.527033,4.340406,-0.673594,-1.131764,-4.702843,-4.773526,2.610933,-6.607394,-5.864444,-0.891621,8.123893,9.823650,1.127040,-3.094582,-3.068166,-1.746388,3.799837,4.346760,-3.254596,-3.096963,1.272161,-7.836649,-9.841716,-1.767354,-9.258542],[8.537073,6.662820,-2.718504,-8.705089,7.369915,0.793420,8.462824,8.061736,-4.435147,-7.817952,-8.876485,5.757686,-2.127689,2.160089,-5.010284,0.990545,-4.141580,-5.030990,-9.953488,1.253126,7.345333,1.266027,6.285245,1.231689,-0.223598,-1.747675,9.936880,-6.893736,7.093241,9.575690,7.321154,-2.798531,8.955726,-6.213367,0.486419,8.084688,-7.897520,4.995187,2.112794,9.086585,-6.412557,8.814721,3.973817,3.683269,8.771084,-5.376763,-1.425148,-1.148230,0.262227,1.977616,-7.513395,7.070536,7.815767,-0.363535,2.691767,-2.666957,-7.945490,-5.997554,1.962270,-1.841820,-4.919223,1.845176,3.058399,-0.732667,-1.659833,-4.263063,-7.332983,6.610055,-4.243269,-3.288517,7.209362,-2.223043,-2.011655,8.652638,-6.710854,5.273601,-5.957056,3.195163,-2.034945,-1.352779,1.945215,-1.034860,-5.228953,5.599237,0.786825,4.913340,1.281107,-9.316905,-1.094624,7.072531,-3.244699,2.437343,-9.795408,-2.754616,-6.950337,1.752910,2.377709,4.431667,-9.072621,7.873355,-7.150719,-4.318754,-0.593155,-2.011952,3.209451,5.815923,-3.014872,-6.121569,-9.969079,8.238928],[-5.457753,-5.832553,-8.081415,3.378955,1.513722,5.441232,5.916021,0.950344,-3.478179,-2.461266,7.476799,2.008255,-9.295561,-7.029193,6.008727,5.305680,8.128337,2.268682,5.289600,-4.762695,7.341628,8.182318,8.812320,-0.023760,-9.131473,4.598385,8.125932,4.702491,3.441013,-7.098433,5.418264,-1.780408,0.043868,8.574994,-1.733538,6.865613,8.091701,1.172044,7.228888,-5.369176,-8.558445,-7.754781,8.457758,-6.840032,3.194147,3.853821,-0.956919,4.494058,6.041747,8.530982,-2.236413,-9.061501,3.963788,4.936953,9.158730,-1.263543,8.459400,6.814544,-3.432566,5.707619,-2.648698,-4.744931,-0.112833,4.443357,-8.359660,-4.689926,7.822106,-3.727773,-8.337225,-3.806619,-3.118507,2.723508,7.174866,-1.168695,-6.218709,5.990757,-8.119356,-1.848500,-8.622976,-7.816104,-0.484011,8.029029,0.748244,-8.546153,4.894754,-9.383719,5.637720,-8.491623,-0.211864,-4.236371,-3.876438,-4.288514,4.202061,-1.913146,-2.600919,5.050716,3.609015,-9.878144,-8.012585,-7.877732,0.532511,3.578335,-3.240597,8.058196,-1.886919,-2.390101,-8.005988,8.185828,4.656157,3.897290],[0.760655,-4.759887,6.589900,0.106280,0.489013,-3.195776,-8.178279,0.416531,7.625632,-9.311579,-5.518489,-5.802428,7.321145,-3.221948,9.780791,-0.259622,-9.376281,3.759232,2.882437,-3.673965,-3.787946,-1.122489,-6.214475,-6.842764,-0.940751,-5.488322,9.661570,2.289979,-6.369802,5.780799,1.922383,-7.380267,-8.040703,-3.634471,5.227218,-7.175703,0.927645,-7.405546,-2.575372,0.158106,0.405699,2.955446,-1.198450,3.896706,-7.669010,1.769245,-7.679874,-0.702671,0.469936,3.199310,3.243368,1.962759,-5.556705,-3.116203,-0.049888,1.072997,3.388708,-0.496567,-8.004091,9.681791,-2.267252,-7.942451,-2.968578,4.751113,4.460119,-4.930716,-3.986289,4.054235,-1.494486,2.527586,8.840952,-8.515410,6.700650,6.576175,3.640321,-0.541747,3.668279,-9.298663,2.710864,3.892635,-9.672768,2.687341,0.229151,6.017955,5.942806,-3.197786,-2.319523,3.413240,3.199804,0.060092,7.968092,-8.479227,-6.999218,9.389946,-7.898234,5.800849,-2.409094,2.741534,8.524318,7.793692,8.762559,-9.555907,6.405535,7.520400,-0.316914,8.115763,1.880750,-2.961368,-7.044709,6.626798],[-9.346188,-2.844058,-3.714533,4.835014,-6.861919,-3.980061,-4.445669,1.683171,-4.114526,4.115527,3.704978,3.014988,-0.159443,7.033307,9.232429,-4.268164,4.522788,-8.605333,-2.321167,7.941815,7.628874,3.533768,-7.094222,8.852454,7.686851,8.397616,5.306368,3.287503,-0.974643,-6.245126,-6.003250,-2.768074,6.559474,5.262032,-6.542092,2.646327,-2.462237,4.949534,8.330696,7.586450,7.922000,-0.184847,7.801731,7.907004,-9.632306,4.725107,-8.913874,-6.197304,1.206337,0.246949,-8.766748,3.425009,8.917792,-9.249765,0.411513,-8.353353,-8.443051,5.240352,-3.675429,-0.669304,-0.422212,6.205210,0.035913,5.168654,6.530809,-4.983207,1.812417,-4.427831,-3.147037,1.375834,3.913883,0.390139,-1.015721,6.323545,2.792212,5.951075,-4.753903,-7.720036,-8.528904,-8.112988,-0.930914,-5.348350,-3.112891,7.461123,5.478067,-0.917502,-1.086241,-1.565729,-3.165077,0.347083,4.367560,4.251343,-7.429560,9.510317,4.215138,-2.602473,-5.466262,6.638139,-2.393125,-9.466203,-7.343729,-0.745074,-2.420883,9.405592,-5.231942,-2.082219,-8.480483,3.263655,3.895505,0.034935],[-1.077929,-9.199329,-0.185196,4.946184,-2.231146,-3.710433,-3.928588,8.108007,-3.843732,9.521142,-6.022127,-6.996517,-3.140995,6.923114,6.658065,-9.606118,-7.897965,-1.423736,9.562521,4.386967,5.788618,-8.134339,-6.342039,-4.233321,-8.487337,-0.817128,8.676108,2.959454,-4.518517,0.530640,-6.399122,-7.967025,5.201030,5.955764,-2.798151,-0.832152,1.978710,-8.158684,3.060967,-2.902532,-2.174292,-1.159749,7.377535,6.449840,-5.827486,3.785292,5.235387,7.282444,7.560365,2.224402,-9.063239,6.397003,-8.596596,5.656246,0.921724,0.607728,-5.426194,7.825394,-0.105330,-9.368401,-6.060240,5.270608,5.400724,-6.921666,3.810369,-4.632279,7.483886,3.522505,8.169742,6.013271,-6.978554,7.346307,-3.558634,1.241934,1.146373,5.310049,7.446425,8.174100,-0.547499,3.192602,6.830676,3.661959,-4.403785,-5.203868,9.734688,-3.499189,0.015424,9.950570,-4.124485,-9.488540,-3.295679,3.614421,-4.988284,-7.149069,-2.552422,-6.931506,6.164403,1.184641,6.361692,-2.246912,9.014904,-7.194249,-6.555025,3.508915,-9.978661,-2.024191,4.543134,5.376460,2.350740,-9.036284],[1.417785,8.003319,-0.695953,-4.683128,6.768400,8.513208,2.820056,5.672450,6.064558,6.207501,-1.984994,-6.967821,9.043147,5.013054,5.512146,6.683288,-3.014171,6.224048,5.741774,-3.548446,-7.508899,6.596963,-2.636033,0.944859,2.815215,2.372897,7.068460,-7.941563,9.784697,0.762401,5.719231,-3.768476,0.589132,0.968667,4.992141,5.478170,9.947840,-8.989998,7.434426,3.356022,-6.822472,-7.541009,-5.094911,-5.526662,-5.966398,-0.042345,-0.307421,-8.915682,-0.530699,-8.574092,0.822076,-7.576256,9.093642,-5.741318,-6.049807,2.460577,5.913709,-4.699280,-4.165312,1.984734,-1.599720,1.115862,-6.454267,4.113533,9.147759,9.580296,6.968841,5.308722,-6.616460,-8.804558,4.889657,2.175759,3.464901,-0.454468,-7.230988,4.188575,9.425177,-2.609341,-4.390882,-2.330152,2.143719,-2.911440,2.922120,4.882468,-2.452173,7.896504,-6.718260,-5.372137,-5.690179,0.393084,-2.285620,-6.862407,5.704507,-4.850213,-9.795163,3.368408,-3.139252,-6.351577,9.976995,5.821656,7.852118,4.443460,7.203450,-4.859139,-2.178804,-7.009879,-5.767606,-7.406985,9.475336,8.367921]], dtype = "float32")#candidate|789|(8, 110)|const|float32
call_788 = relay.TupleGetItem(func_435_call(relay.reshape(const_789.astype('float32'), [11, 10, 8]), relay.reshape(const_789.astype('float32'), [11, 10, 8]), ), 0)
call_790 = relay.TupleGetItem(func_439_call(relay.reshape(const_789.astype('float32'), [11, 10, 8]), relay.reshape(const_789.astype('float32'), [11, 10, 8]), ), 0)
bop_791 = relay.multiply(call_784.astype('int32'), relay.reshape(call_788.astype('int32'), relay.shape_of(call_784))) # shape=(14, 8, 4)
bop_794 = relay.multiply(call_785.astype('int32'), relay.reshape(call_790.astype('int32'), relay.shape_of(call_785))) # shape=(14, 8, 4)
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
call_800 = relay.TupleGetItem(func_435_call(relay.reshape(const_789.astype('float32'), [11, 10, 8]), relay.reshape(const_789.astype('float32'), [11, 10, 8]), ), 2)
call_801 = relay.TupleGetItem(func_439_call(relay.reshape(const_789.astype('float32'), [11, 10, 8]), relay.reshape(const_789.astype('float32'), [11, 10, 8]), ), 2)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_802 = relay.TupleGetItem(func_735_call(), 1)
call_803 = relay.TupleGetItem(func_737_call(), 1)
uop_805 = relay.sin(const_789.astype('float64')) # shape=(8, 110)
output = relay.Tuple([call_766,bop_791,call_800,call_802,uop_805,])
output2 = relay.Tuple([call_767,bop_794,call_801,call_803,uop_805,])
func_807 = relay.Function([], output)
mod['func_807'] = func_807
mod = relay.transform.InferType()(mod)
mutated_mod['func_807'] = func_807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_807_call = mutated_mod.get_global_var('func_807')
call_808 = func_807_call()
output = call_808
func_809 = relay.Function([], output)
mutated_mod['func_809'] = func_809
mutated_mod = relay.transform.InferType()(mutated_mod)
var_824 = relay.var("var_824", dtype = "float64", shape = (12, 5, 4))#candidate|824|(12, 5, 4)|var|float64
var_825 = relay.var("var_825", dtype = "float64", shape = (12, 5, 4))#candidate|825|(12, 5, 4)|var|float64
bop_826 = relay.floor_mod(var_824.astype('float64'), relay.reshape(var_825.astype('float64'), relay.shape_of(var_824))) # shape=(12, 5, 4)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_829 = relay.TupleGetItem(func_713_call(), 0)
call_830 = relay.TupleGetItem(func_714_call(), 0)
func_300_call = mod.get_global_var('func_300')
func_302_call = mutated_mod.get_global_var('func_302')
call_842 = relay.TupleGetItem(func_300_call(relay.reshape(call_829.astype('bool'), [14, 8, 4])), 2)
call_843 = relay.TupleGetItem(func_302_call(relay.reshape(call_829.astype('bool'), [14, 8, 4])), 2)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_845 = relay.TupleGetItem(func_713_call(), 0)
call_846 = relay.TupleGetItem(func_714_call(), 0)
func_807_call = mod.get_global_var('func_807')
func_809_call = mutated_mod.get_global_var('func_809')
call_853 = relay.TupleGetItem(func_807_call(), 0)
call_854 = relay.TupleGetItem(func_809_call(), 0)
bop_860 = relay.floor_mod(call_829.astype('float64'), relay.reshape(call_853.astype('float64'), relay.shape_of(call_829))) # shape=(14, 8, 4)
bop_863 = relay.floor_mod(call_830.astype('float64'), relay.reshape(call_854.astype('float64'), relay.shape_of(call_830))) # shape=(14, 8, 4)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_865 = relay.TupleGetItem(func_713_call(), 0)
call_866 = relay.TupleGetItem(func_714_call(), 0)
output = relay.Tuple([bop_826,call_842,call_845,bop_860,call_865,])
output2 = relay.Tuple([bop_826,call_843,call_846,bop_863,call_866,])
func_873 = relay.Function([var_824,var_825,], output)
mod['func_873'] = func_873
mod = relay.transform.InferType()(mod)
var_874 = relay.var("var_874", dtype = "float64", shape = (12, 5, 4))#candidate|874|(12, 5, 4)|var|float64
var_875 = relay.var("var_875", dtype = "float64", shape = (12, 5, 4))#candidate|875|(12, 5, 4)|var|float64
output = func_873(var_874,var_875,)
func_876 = relay.Function([var_874,var_875,], output)
mutated_mod['func_876'] = func_876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_878 = relay.TupleGetItem(func_735_call(), 0)
call_879 = relay.TupleGetItem(func_737_call(), 0)
output = relay.Tuple([call_878,])
output2 = relay.Tuple([call_879,])
func_882 = relay.Function([], output)
mod['func_882'] = func_882
mod = relay.transform.InferType()(mod)
mutated_mod['func_882'] = func_882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mutated_mod.get_global_var('func_882')
call_883 = func_882_call()
output = call_883
func_884 = relay.Function([], output)
mutated_mod['func_884'] = func_884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_992 = relay.TupleGetItem(func_650_call(), 1)
call_993 = relay.TupleGetItem(func_652_call(), 1)
uop_996 = relay.acos(call_992.astype('float32')) # shape=(14, 8, 4)
uop_998 = relay.acos(call_993.astype('float32')) # shape=(14, 8, 4)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_1011 = relay.TupleGetItem(func_735_call(), 1)
call_1012 = relay.TupleGetItem(func_737_call(), 1)
func_481_call = mod.get_global_var('func_481')
func_483_call = mutated_mod.get_global_var('func_483')
call_1013 = func_481_call(relay.reshape(uop_996.astype('bool'), [14, 8, 4]))
call_1014 = func_481_call(relay.reshape(uop_996.astype('bool'), [14, 8, 4]))
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_1016 = relay.TupleGetItem(func_735_call(), 1)
call_1017 = relay.TupleGetItem(func_737_call(), 1)
bop_1021 = relay.floor_divide(call_1013.astype('float64'), relay.reshape(call_1011.astype('float64'), relay.shape_of(call_1013))) # shape=(14, 8, 4)
bop_1024 = relay.floor_divide(call_1014.astype('float64'), relay.reshape(call_1012.astype('float64'), relay.shape_of(call_1014))) # shape=(14, 8, 4)
func_481_call = mod.get_global_var('func_481')
func_483_call = mutated_mod.get_global_var('func_483')
call_1042 = func_481_call(relay.reshape(call_1016.astype('bool'), [14, 8, 4]))
call_1043 = func_481_call(relay.reshape(call_1016.astype('bool'), [14, 8, 4]))
bop_1046 = relay.greater_equal(uop_996.astype('bool'), relay.reshape(call_1016.astype('bool'), relay.shape_of(uop_996))) # shape=(14, 8, 4)
bop_1049 = relay.greater_equal(uop_998.astype('bool'), relay.reshape(call_1017.astype('bool'), relay.shape_of(uop_998))) # shape=(14, 8, 4)
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_1050 = relay.TupleGetItem(func_882_call(), 0)
call_1051 = relay.TupleGetItem(func_884_call(), 0)
output = relay.Tuple([bop_1021,call_1042,bop_1046,call_1050,])
output2 = relay.Tuple([bop_1024,call_1043,bop_1049,call_1051,])
func_1072 = relay.Function([], output)
mod['func_1072'] = func_1072
mod = relay.transform.InferType()(mod)
output = func_1072()
func_1073 = relay.Function([], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_807_call = mod.get_global_var('func_807')
func_809_call = mutated_mod.get_global_var('func_809')
call_1110 = relay.TupleGetItem(func_807_call(), 2)
call_1111 = relay.TupleGetItem(func_809_call(), 2)
output = call_1110
output2 = call_1111
func_1116 = relay.Function([], output)
mod['func_1116'] = func_1116
mod = relay.transform.InferType()(mod)
mutated_mod['func_1116'] = func_1116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mutated_mod.get_global_var('func_1116')
call_1117 = func_1116_call()
output = call_1117
func_1118 = relay.Function([], output)
mutated_mod['func_1118'] = func_1118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_1139 = relay.TupleGetItem(func_650_call(), 1)
call_1140 = relay.TupleGetItem(func_652_call(), 1)
uop_1141 = relay.sinh(call_1139.astype('float64')) # shape=(14, 8, 4)
uop_1143 = relay.sinh(call_1140.astype('float64')) # shape=(14, 8, 4)
output = uop_1141
output2 = uop_1143
func_1148 = relay.Function([], output)
mod['func_1148'] = func_1148
mod = relay.transform.InferType()(mod)
output = func_1148()
func_1149 = relay.Function([], output)
mutated_mod['func_1149'] = func_1149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_1163 = relay.TupleGetItem(func_650_call(), 1)
call_1164 = relay.TupleGetItem(func_652_call(), 1)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_1167 = relay.TupleGetItem(func_650_call(), 1)
call_1168 = relay.TupleGetItem(func_652_call(), 1)
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
const_1173 = relay.const([[9.217151,-7.953902,8.548460,-2.760711,7.285720,1.344486,-1.778393,4.387917,2.409914,-0.948408,-6.287094,-1.090165,-6.814862,-0.053310,8.836086,-2.131721,-6.188465,7.200619,0.916189,0.791437,-3.453354,-7.470427,-7.968842,5.256327,-0.005253,-7.871559,-8.412366,1.638494,-5.576400,4.556607,-6.986915,-2.232469,-2.038840,9.487831,-1.723212,-5.865864,7.628173,2.904436,-6.218602,8.007511,0.486864,3.638645,-3.531629,-9.580791,2.015439,3.832395,6.517900,-9.876391,0.817425,-3.792225,-7.914594,-7.332494,3.729351,2.840505,1.385884,-2.199676,8.321229,-1.312819,-3.689522,-0.403059,-8.043196,-6.493207,-3.586727,5.286023,-2.906463,6.592852,-0.362672,-5.458564,7.492359,7.584768,3.846586,5.200331,-9.385117,-4.440783,-4.310913,-1.837646,-7.185753,9.703909,5.488652,-9.110813,-8.665926,9.015312,-9.893350,-6.712888,5.632823,-5.621207,6.781926,5.375061,1.228807,-2.221806,1.159079,-5.971217,8.902080,-0.936265,-8.415407,-1.272375,-1.041120,7.873401,-9.629970,-3.271010,1.003375,-2.514870,6.020278,-6.833654,8.167769,-8.983230,8.754609,6.242918,-1.338209,-9.378998,-3.113091,3.416145,-7.952209,4.374500,-0.125069,-1.004497,-4.841477,-7.486942,8.814969,-8.376839,-3.089909,2.836683,2.667929,-8.083478,-8.131299,-0.293393,-1.937620,8.321548,-8.897662,5.891285,-0.057789,8.485191,-3.854368,-2.601235,-7.232365,-2.524963,-5.693411,3.277078,-7.219720,1.023670,-6.560803,-5.970109,-6.173096,0.821634,-0.146840,4.336312,-3.748821,-9.095970,2.823147,-7.777257,6.040827,-5.626953,-1.901256,-0.929071,7.562705,3.684555,3.884866,-2.529552,1.929341,3.186876,-9.052848,0.562862,2.024644,7.596476,-6.734331,-9.518978,7.694699,0.492403,-7.127997,-2.329612,-3.288666,4.337316,0.291157,8.648141,4.624065,8.041686,7.717253,4.945631,-6.469168,5.122079,-1.139962,-9.138587,-7.284444,-1.787598,9.498688,6.957733,-0.497385,-5.623763,-2.619815,8.288911,-6.896937,-9.134773,7.220992,-1.440384,-1.971594,-2.606409,5.765395,-8.368192,9.776054,4.121080,-8.504993,-6.016914,9.408364,-1.348951,-8.108403,-5.700738,-8.323507,-5.352269,-3.827550,4.303029,6.098616,0.632446,3.559147,-2.414645,-1.154584,2.681187,-9.087007,-2.192317,-8.584486,-3.991817],[-0.910872,9.181699,7.936694,-0.482256,-8.543117,-6.963494,3.351769,9.600964,-1.990588,1.028243,6.827100,1.213202,-1.491309,6.764507,-4.034600,0.685579,-1.609376,-3.914678,1.663823,0.547302,-3.071877,1.761634,-0.748119,-4.031344,-4.074382,1.059218,1.658763,-9.503540,-3.207433,-8.644243,3.667086,0.355073,7.823498,2.731146,-5.992295,-3.673448,-5.163437,3.822551,-7.458138,6.940777,5.590220,-9.528065,8.285054,5.070410,5.959420,8.231232,9.392636,-9.357606,-3.425925,9.720192,4.626853,7.019326,4.669988,-5.002105,6.772768,9.637143,-3.742728,9.151686,-9.656892,-6.877652,-9.649240,-4.089157,-1.391950,-5.041122,-8.451194,-1.540549,-7.940768,5.320470,-7.907764,2.082811,-6.504982,-9.493367,9.809772,-8.742582,-0.596711,6.842342,-6.839446,5.264501,-6.831462,1.442572,2.057592,-0.520993,-5.386506,-4.230313,8.282818,-5.851007,-3.184412,6.726249,-2.716051,6.329225,-5.612377,7.760040,-4.887425,0.403856,7.247969,8.879359,-2.946042,-5.057065,8.673321,7.498670,-3.563410,-4.770577,6.047009,-9.608655,-1.344547,-0.723441,-7.835527,5.495962,-7.651304,-9.017542,-1.198067,8.283394,7.209814,6.793082,-8.251172,-3.359042,-9.623205,6.060586,-0.744263,3.566336,7.845646,9.793444,9.552151,-9.224041,1.433175,7.868006,-4.150816,7.148821,-2.060785,-3.016035,9.161236,-8.973451,-8.807261,2.273439,2.741107,3.159232,0.046646,4.576265,1.742913,-4.836193,-1.301912,-4.665932,-2.427330,-9.705813,-7.088696,9.769342,1.425511,0.186389,6.388748,-5.008505,6.643910,7.988459,-1.385004,-8.657610,-2.403036,1.573494,-0.409758,4.860033,3.066123,-1.776050,4.097136,4.655034,2.727053,-0.961307,-5.263776,9.170203,-6.719324,-4.592459,3.498820,-0.356781,4.557005,-1.198798,-7.845864,2.728185,-8.968932,0.126708,8.067572,-0.734794,-2.101191,-0.423652,-9.700552,-8.586640,-9.142393,6.353456,4.698505,-5.474330,6.195744,2.001396,-7.873153,2.376223,-8.043807,-3.226274,-0.145407,-0.036118,2.234322,7.818538,-3.317604,-4.649763,-3.983925,5.984426,-6.171903,-9.651963,-3.071548,8.701571,-7.203879,7.773380,5.365817,1.436590,3.856594,-9.169932,-9.408674,-0.128552,-0.695831,1.370131,-1.629592,-1.301528,-3.877137,1.294488,-6.497478,-2.122951],[5.149725,9.916360,2.574622,-4.001744,-3.937173,-1.935772,-0.896191,-4.972536,1.545672,3.458769,-5.298652,-7.319602,5.469661,6.060599,-3.540265,-6.384176,-3.494907,2.607816,-2.797519,-1.307732,-0.519278,2.357359,1.783895,3.422094,-4.244430,-9.079666,1.730973,5.892511,-7.038233,-0.095751,-0.814229,0.307897,5.327533,7.958043,-3.034556,-8.495504,-7.882684,-7.065200,1.421914,-4.715809,-0.778001,-6.026934,-3.966706,-9.656961,2.910279,4.418487,-0.446057,-7.864254,2.401254,3.675887,3.515618,8.721888,-8.614131,8.563837,2.909389,7.988493,-3.860334,9.982897,1.869931,-8.359075,2.691387,9.702578,-2.888889,6.314744,6.319047,8.391596,-3.370460,-9.037090,-1.972446,0.046651,8.745781,-5.771886,-4.525547,-5.749472,7.907825,-4.363127,6.381257,-6.312698,0.759045,9.084944,1.290586,7.463480,2.546667,-4.587384,3.645791,-9.111110,-7.928159,4.605136,-3.810823,-8.362626,-4.971171,-9.156732,-3.748877,8.664839,-0.192594,-0.203868,9.079034,-1.740778,3.872830,3.152683,-7.106024,-4.450624,-7.174759,3.245849,4.922858,-7.723150,8.054152,6.477049,-3.187027,1.338767,-0.307611,-5.968849,-8.996925,-6.441581,4.871107,-1.763624,2.236163,-0.854860,-5.979049,6.264075,1.444860,5.426395,-5.063970,4.364631,0.909065,-4.277362,-5.359848,-6.429948,3.813140,2.616208,-0.679804,-5.467094,-6.349332,2.396648,-6.248749,-8.260881,-4.375584,-8.403189,9.733382,3.886912,2.516193,-1.280341,-1.481897,-9.765191,5.019049,-6.317416,6.858288,-0.633918,5.997440,6.691763,-3.295946,-3.181696,3.330516,0.996078,-7.986112,-6.329233,-7.777142,0.167231,8.807769,-5.946432,5.037296,-7.133882,3.754137,-7.787732,-8.589776,6.624310,-5.077399,3.940612,-6.000931,-3.233185,-7.096521,-1.811577,7.678517,3.077219,2.788921,4.596880,9.280695,-9.607781,-4.916848,4.266626,-4.441362,0.838458,-5.747973,-8.464548,-2.547277,8.515425,8.018795,8.374204,-4.887731,8.780474,0.498204,-3.915868,-4.670983,1.429914,-9.434199,9.981149,2.107283,9.723982,-3.716558,1.463394,-0.635169,4.270631,-2.647138,-6.859749,5.753553,6.776138,-4.793881,8.658048,-0.193693,-0.013757,-2.760743,3.471357,-5.378133,2.316573,-8.553317,1.736838,-6.963934,4.391125,-4.122105,1.071754],[0.634431,-4.805643,-9.150335,2.089769,-8.656144,4.987115,8.252946,7.320247,0.571022,-4.783877,8.118696,-0.331662,-7.763786,-0.303328,3.471194,1.512063,-6.611138,8.873127,4.784978,2.741122,-6.917440,-3.930984,9.272256,3.568588,9.265548,0.859077,-4.683471,-0.567416,3.026662,7.347332,-3.312605,8.006093,-3.644246,5.564879,3.898103,1.461836,-9.202406,-8.366190,4.306675,-2.113175,9.771535,6.639850,-8.111457,5.024589,0.216509,-3.749786,8.627412,-7.433724,-9.593067,4.785589,2.698689,5.746813,9.703985,3.609563,-0.536378,4.312724,7.205663,4.772666,-6.273888,7.831214,9.674789,1.040943,-3.087027,-8.412551,7.334498,-5.206464,-1.420972,-6.424184,1.778013,8.320119,-3.962948,-3.754586,5.880631,1.936529,-2.477992,0.412671,-6.834186,-3.015700,4.744531,-7.530263,-6.435686,7.664182,-8.391014,-3.588628,5.242326,3.701038,-1.343667,-9.232882,2.736918,2.405675,-0.466611,5.733233,3.360532,8.005437,-2.815884,-5.451116,0.876048,-5.091094,4.541737,1.122017,-2.606119,-0.744614,-7.684970,-4.693074,-6.202767,4.163765,8.909052,-7.876119,-8.259754,0.041195,3.899769,-4.315660,1.015804,-1.322688,6.584158,2.129868,3.591253,4.012984,-7.525312,5.923324,7.573321,-5.592122,-5.020878,-5.025917,-1.936817,0.873929,5.453156,-3.919691,-6.704288,6.502301,6.095440,5.589633,7.615472,-4.103725,5.900322,-5.997794,5.847129,5.139515,5.264357,-4.509308,9.191013,5.896678,1.051113,6.360449,4.343467,-3.274822,3.591994,8.015737,-9.744489,7.282437,8.697535,-2.913391,-5.023583,-9.654305,6.885654,5.823521,1.560220,6.329894,3.323239,-2.694192,-1.136273,6.888778,1.923151,-2.552811,-3.190559,6.702975,4.149990,-9.729507,4.762508,-0.165385,-7.365112,0.690464,-6.753771,-1.611456,9.239492,-5.966351,0.616537,2.262994,-8.354519,-7.738950,0.774844,0.399360,-3.792030,-9.630101,-8.701636,-5.764915,2.088416,-5.095666,0.431837,5.490472,-8.493954,-8.523907,3.268015,-2.851443,6.821519,-2.589231,-1.718029,9.337371,-9.876310,-9.851158,-6.834213,4.796021,-7.333780,-0.275574,-3.059406,-8.683437,0.928067,8.945002,-3.982362,8.267188,-4.850993,7.490424,0.285235,8.092178,-3.278055,-0.036040,8.190795,-4.771750,-6.686740,0.430519]], dtype = "float32")#candidate|1173|(4, 220)|const|float32
call_1172 = relay.TupleGetItem(func_435_call(relay.reshape(const_1173.astype('float32'), [11, 10, 8]), relay.reshape(const_1173.astype('float32'), [11, 10, 8]), ), 5)
call_1174 = relay.TupleGetItem(func_439_call(relay.reshape(const_1173.astype('float32'), [11, 10, 8]), relay.reshape(const_1173.astype('float32'), [11, 10, 8]), ), 5)
output = relay.Tuple([call_1163,call_1167,call_1172,const_1173,])
output2 = relay.Tuple([call_1164,call_1168,call_1174,const_1173,])
func_1183 = relay.Function([], output)
mod['func_1183'] = func_1183
mod = relay.transform.InferType()(mod)
mutated_mod['func_1183'] = func_1183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1183_call = mutated_mod.get_global_var('func_1183')
call_1184 = func_1183_call()
output = call_1184
func_1185 = relay.Function([], output)
mutated_mod['func_1185'] = func_1185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_1194 = relay.TupleGetItem(func_882_call(), 0)
call_1195 = relay.TupleGetItem(func_884_call(), 0)
var_1201 = relay.var("var_1201", dtype = "bool", shape = (14, 8, 4))#candidate|1201|(14, 8, 4)|var|bool
bop_1202 = relay.right_shift(call_1194.astype('uint64'), relay.reshape(var_1201.astype('uint64'), relay.shape_of(call_1194))) # shape=(14, 8, 4)
bop_1205 = relay.right_shift(call_1195.astype('uint64'), relay.reshape(var_1201.astype('uint64'), relay.shape_of(call_1195))) # shape=(14, 8, 4)
func_873_call = mod.get_global_var('func_873')
func_876_call = mutated_mod.get_global_var('func_876')
var_1210 = relay.var("var_1210", dtype = "float64", shape = (240,))#candidate|1210|(240,)|var|float64
call_1209 = relay.TupleGetItem(func_873_call(relay.reshape(var_1210.astype('float64'), [12, 5, 4]), relay.reshape(var_1210.astype('float64'), [12, 5, 4]), ), 1)
call_1211 = relay.TupleGetItem(func_876_call(relay.reshape(var_1210.astype('float64'), [12, 5, 4]), relay.reshape(var_1210.astype('float64'), [12, 5, 4]), ), 1)
output = relay.Tuple([bop_1202,call_1209,var_1210,])
output2 = relay.Tuple([bop_1205,call_1211,var_1210,])
func_1217 = relay.Function([var_1201,var_1210,], output)
mod['func_1217'] = func_1217
mod = relay.transform.InferType()(mod)
mutated_mod['func_1217'] = func_1217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1217_call = mutated_mod.get_global_var('func_1217')
var_1219 = relay.var("var_1219", dtype = "bool", shape = (14, 8, 4))#candidate|1219|(14, 8, 4)|var|bool
var_1220 = relay.var("var_1220", dtype = "float64", shape = (240,))#candidate|1220|(240,)|var|float64
call_1218 = func_1217_call(var_1219,var_1220,)
output = call_1218
func_1221 = relay.Function([var_1219,var_1220,], output)
mutated_mod['func_1221'] = func_1221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1232 = relay.TupleGetItem(func_1072_call(), 3)
call_1233 = relay.TupleGetItem(func_1073_call(), 3)
uop_1234 = relay.exp(call_1232.astype('float32')) # shape=(14, 8, 4)
uop_1236 = relay.exp(call_1233.astype('float32')) # shape=(14, 8, 4)
output = uop_1234
output2 = uop_1236
func_1240 = relay.Function([], output)
mod['func_1240'] = func_1240
mod = relay.transform.InferType()(mod)
output = func_1240()
func_1241 = relay.Function([], output)
mutated_mod['func_1241'] = func_1241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1183_call = mod.get_global_var('func_1183')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_1348 = relay.TupleGetItem(func_1183_call(), 1)
call_1349 = relay.TupleGetItem(func_1185_call(), 1)
func_1148_call = mod.get_global_var('func_1148')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_1350 = func_1148_call()
call_1351 = func_1148_call()
output = relay.Tuple([call_1348,call_1350,])
output2 = relay.Tuple([call_1349,call_1351,])
func_1357 = relay.Function([], output)
mod['func_1357'] = func_1357
mod = relay.transform.InferType()(mod)
output = func_1357()
func_1358 = relay.Function([], output)
mutated_mod['func_1358'] = func_1358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_1459 = relay.TupleGetItem(func_713_call(), 0)
call_1460 = relay.TupleGetItem(func_714_call(), 0)
output = call_1459
output2 = call_1460
func_1464 = relay.Function([], output)
mod['func_1464'] = func_1464
mod = relay.transform.InferType()(mod)
output = func_1464()
func_1465 = relay.Function([], output)
mutated_mod['func_1465'] = func_1465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1148_call = mod.get_global_var('func_1148')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_1466 = func_1148_call()
call_1467 = func_1148_call()
uop_1471 = relay.log10(call_1466.astype('float64')) # shape=(14, 8, 4)
uop_1473 = relay.log10(call_1467.astype('float64')) # shape=(14, 8, 4)
output = relay.Tuple([uop_1471,])
output2 = relay.Tuple([uop_1473,])
func_1474 = relay.Function([], output)
mod['func_1474'] = func_1474
mod = relay.transform.InferType()(mod)
mutated_mod['func_1474'] = func_1474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mutated_mod.get_global_var('func_1474')
call_1475 = func_1474_call()
output = call_1475
func_1476 = relay.Function([], output)
mutated_mod['func_1476'] = func_1476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1148_call = mod.get_global_var('func_1148')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_1480 = func_1148_call()
call_1481 = func_1148_call()
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_1491 = relay.TupleGetItem(func_650_call(), 1)
call_1492 = relay.TupleGetItem(func_652_call(), 1)
bop_1493 = relay.left_shift(call_1491.astype('int64'), relay.reshape(call_1480.astype('int64'), relay.shape_of(call_1491))) # shape=(14, 8, 4)
bop_1496 = relay.left_shift(call_1492.astype('int64'), relay.reshape(call_1481.astype('int64'), relay.shape_of(call_1492))) # shape=(14, 8, 4)
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
var_1499 = relay.var("var_1499", dtype = "float32", shape = (4, 220))#candidate|1499|(4, 220)|var|float32
call_1498 = relay.TupleGetItem(func_435_call(relay.reshape(var_1499.astype('float32'), [11, 10, 8]), relay.reshape(var_1499.astype('float32'), [11, 10, 8]), ), 5)
call_1500 = relay.TupleGetItem(func_439_call(relay.reshape(var_1499.astype('float32'), [11, 10, 8]), relay.reshape(var_1499.astype('float32'), [11, 10, 8]), ), 5)
bop_1506 = relay.logical_xor(var_1499.astype('int8'), relay.reshape(call_1498.astype('int8'), relay.shape_of(var_1499))) # shape=(4, 220)
bop_1509 = relay.logical_xor(var_1499.astype('int8'), relay.reshape(call_1500.astype('int8'), relay.shape_of(var_1499))) # shape=(4, 220)
output = relay.Tuple([bop_1493,bop_1506,])
output2 = relay.Tuple([bop_1496,bop_1509,])
func_1513 = relay.Function([var_1499,], output)
mod['func_1513'] = func_1513
mod = relay.transform.InferType()(mod)
mutated_mod['func_1513'] = func_1513
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1514 = relay.var("var_1514", dtype = "float32", shape = (4, 220))#candidate|1514|(4, 220)|var|float32
func_1513_call = mutated_mod.get_global_var('func_1513')
call_1515 = func_1513_call(var_1514)
output = call_1515
func_1516 = relay.Function([var_1514], output)
mutated_mod['func_1516'] = func_1516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_1632 = relay.TupleGetItem(func_1474_call(), 0)
call_1633 = relay.TupleGetItem(func_1476_call(), 0)
func_873_call = mod.get_global_var('func_873')
func_876_call = mutated_mod.get_global_var('func_876')
const_1636 = relay.const([4.664202,7.207402,-9.436805,-4.809425,-2.544669,0.035001,5.233483,-7.887318,4.516719,-8.501448,7.099995,9.343637,-4.665621,5.928324,6.806520,5.345921,2.433767,-6.109892,-0.353738,5.436918,-9.450497,-1.173391,-8.477928,3.760146,9.377277,9.241064,7.703694,8.131511,4.645790,7.048737,-3.310616,4.538174,0.490467,3.463363,6.774788,1.668274,1.284466,3.689162,-4.710658,1.504892,-3.789688,-7.974748,-7.441695,0.517542,-3.201895,-4.046182,7.950146,4.420413,-1.121215,-6.570885,9.664292,2.193385,-7.300314,-6.373361,3.136492,-0.787071,-2.056685,1.105336,7.506985,-8.903469,3.624847,-8.581691,3.378715,-6.272042,-0.430035,9.015389,-4.856688,-2.663131,7.839803,7.275602,-1.004060,-9.592913,0.121975,7.402771,-7.763705,-0.648136,2.458403,3.788924,-6.818539,-3.300276,-1.496671,8.864404,-5.263043,7.107064,-5.951631,-4.233289,8.868096,-2.371332,-8.291181,1.851132,2.051949,-8.494554,-4.215489,2.263332,5.314067,1.556662,4.724644,-5.148850,-9.431866,9.948247,3.528144,3.007617,-0.176753,5.571986,-9.851024,-2.153109,-2.946788,-8.641842,-8.073640,-1.970243,9.156698,7.298534,-1.375366,-1.197558,-9.027592,3.832732,1.661412,-9.056997,-8.187484,-4.372120,-8.550862,1.218963,8.825203,3.432775,1.671766,-0.999278,9.059926,-6.450776,0.916046,-0.160267,-3.350732,1.599353,-3.774871,-8.390749,2.362803,3.035504,4.890001,9.106736,-8.046627,-9.260672,-1.510920,-4.271320,-4.088518,3.500643,7.849764,3.713540,6.632242,1.077613,-6.952258,1.107833,-6.682228,2.526923,5.788459,4.153065,5.378002,8.052913,-3.884478,0.343319,-9.407073,-8.044003,-0.199430,-9.492960,5.495635,-8.211920,9.597856,9.937521,-5.667008,0.493583,8.687420,-8.988068,-9.352973,-7.226466,8.862228,6.527266,-0.898481,-4.927193,-6.271236,8.189007,-3.539473,1.677549,4.133761,-4.455041,-0.308018,9.622211,-7.018868,-0.264711,2.102380,4.044819,4.195584,1.553876,-8.061807,-5.796005,-5.332580,-6.206560,6.432356,-3.744207,1.577820,9.206427,-9.277387,8.915822,-1.051789,9.806109,3.548873,-2.831956,2.097672,-4.867047,5.965251,-1.420249,-5.343610,6.917340,7.858905,-5.753541,-6.808191,-8.759294,-1.647178,0.131336,3.189443,5.437708,2.415729,2.054083,7.901590,-0.780850,4.927824,-3.940877,-0.162990,6.614431,4.137821,-3.029821,1.488412,-8.056598,-4.814338,-3.663209,-0.315165,-2.421772,-9.485858,-8.776415,-3.214163,-0.375990,-2.688640,2.467832], dtype = "float64")#candidate|1636|(240,)|const|float64
call_1635 = relay.TupleGetItem(func_873_call(relay.reshape(const_1636.astype('float64'), [12, 5, 4]), relay.reshape(const_1636.astype('float64'), [12, 5, 4]), ), 3)
call_1637 = relay.TupleGetItem(func_876_call(relay.reshape(const_1636.astype('float64'), [12, 5, 4]), relay.reshape(const_1636.astype('float64'), [12, 5, 4]), ), 3)
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_1648 = func_1240_call()
call_1649 = func_1240_call()
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_1650 = relay.TupleGetItem(func_882_call(), 0)
call_1651 = relay.TupleGetItem(func_884_call(), 0)
uop_1652 = relay.log(call_1648.astype('float64')) # shape=(14, 8, 4)
uop_1654 = relay.log(call_1649.astype('float64')) # shape=(14, 8, 4)
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_1670 = func_1240_call()
call_1671 = func_1240_call()
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_1672 = relay.TupleGetItem(func_882_call(), 0)
call_1673 = relay.TupleGetItem(func_884_call(), 0)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_1688 = relay.TupleGetItem(func_735_call(), 0)
call_1689 = relay.TupleGetItem(func_737_call(), 0)
func_481_call = mod.get_global_var('func_481')
func_483_call = mutated_mod.get_global_var('func_483')
call_1692 = func_481_call(relay.reshape(call_1672.astype('bool'), [14, 8, 4]))
call_1693 = func_481_call(relay.reshape(call_1672.astype('bool'), [14, 8, 4]))
output = relay.Tuple([call_1632,call_1635,const_1636,call_1650,uop_1652,call_1670,call_1672,call_1688,call_1692,])
output2 = relay.Tuple([call_1633,call_1637,const_1636,call_1651,uop_1654,call_1671,call_1673,call_1689,call_1693,])
func_1699 = relay.Function([], output)
mod['func_1699'] = func_1699
mod = relay.transform.InferType()(mod)
output = func_1699()
func_1700 = relay.Function([], output)
mutated_mod['func_1700'] = func_1700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_1703 = relay.TupleGetItem(func_1699_call(), 2)
call_1704 = relay.TupleGetItem(func_1700_call(), 2)
func_1357_call = mod.get_global_var('func_1357')
func_1358_call = mutated_mod.get_global_var('func_1358')
call_1714 = relay.TupleGetItem(func_1357_call(), 1)
call_1715 = relay.TupleGetItem(func_1358_call(), 1)
func_1464_call = mod.get_global_var('func_1464')
func_1465_call = mutated_mod.get_global_var('func_1465')
call_1720 = func_1464_call()
call_1721 = func_1464_call()
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_1722 = relay.TupleGetItem(func_650_call(), 0)
call_1723 = relay.TupleGetItem(func_652_call(), 0)
uop_1734 = relay.tan(call_1722.astype('float64')) # shape=(14, 8, 4)
uop_1736 = relay.tan(call_1723.astype('float64')) # shape=(14, 8, 4)
output = relay.Tuple([call_1703,call_1714,call_1720,uop_1734,])
output2 = relay.Tuple([call_1704,call_1715,call_1721,uop_1736,])
func_1743 = relay.Function([], output)
mod['func_1743'] = func_1743
mod = relay.transform.InferType()(mod)
mutated_mod['func_1743'] = func_1743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mutated_mod.get_global_var('func_1743')
call_1744 = func_1743_call()
output = call_1744
func_1745 = relay.Function([], output)
mutated_mod['func_1745'] = func_1745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_1746 = func_1116_call()
call_1747 = func_1116_call()
output = call_1746
output2 = call_1747
func_1757 = relay.Function([], output)
mod['func_1757'] = func_1757
mod = relay.transform.InferType()(mod)
mutated_mod['func_1757'] = func_1757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mutated_mod.get_global_var('func_1757')
call_1758 = func_1757_call()
output = call_1758
func_1759 = relay.Function([], output)
mutated_mod['func_1759'] = func_1759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_1797 = relay.TupleGetItem(func_713_call(), 1)
call_1798 = relay.TupleGetItem(func_714_call(), 1)
output = relay.Tuple([call_1797,])
output2 = relay.Tuple([call_1798,])
func_1800 = relay.Function([], output)
mod['func_1800'] = func_1800
mod = relay.transform.InferType()(mod)
output = func_1800()
func_1801 = relay.Function([], output)
mutated_mod['func_1801'] = func_1801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_1809 = relay.TupleGetItem(func_235_call(), 0)
call_1810 = relay.TupleGetItem(func_237_call(), 0)
uop_1825 = relay.cosh(call_1809.astype('float64')) # shape=(14, 8, 4)
uop_1827 = relay.cosh(call_1810.astype('float64')) # shape=(14, 8, 4)
output = relay.Tuple([uop_1825,])
output2 = relay.Tuple([uop_1827,])
func_1853 = relay.Function([], output)
mod['func_1853'] = func_1853
mod = relay.transform.InferType()(mod)
output = func_1853()
func_1854 = relay.Function([], output)
mutated_mod['func_1854'] = func_1854
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1876 = relay.var("var_1876", dtype = "float32", shape = (14, 2, 3))#candidate|1876|(14, 2, 3)|var|float32
var_1877 = relay.var("var_1877", dtype = "float32", shape = (14, 2, 3))#candidate|1877|(14, 2, 3)|var|float32
bop_1878 = relay.less_equal(var_1876.astype('bool'), relay.reshape(var_1877.astype('bool'), relay.shape_of(var_1876))) # shape=(14, 2, 3)
bop_1896 = relay.minimum(var_1876.astype('uint8'), relay.reshape(bop_1878.astype('uint8'), relay.shape_of(var_1876))) # shape=(14, 2, 3)
bop_1899 = relay.subtract(bop_1878.astype('float64'), relay.reshape(bop_1896.astype('float64'), relay.shape_of(bop_1878))) # shape=(14, 2, 3)
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_1903 = relay.TupleGetItem(func_882_call(), 0)
call_1904 = relay.TupleGetItem(func_884_call(), 0)
func_569_call = mod.get_global_var('func_569')
func_572_call = mutated_mod.get_global_var('func_572')
call_1906 = relay.TupleGetItem(func_569_call(relay.reshape(call_1903.astype('bool'), [14, 8, 4])), 1)
call_1907 = relay.TupleGetItem(func_572_call(relay.reshape(call_1903.astype('bool'), [14, 8, 4])), 1)
uop_1911 = relay.sin(bop_1899.astype('float64')) # shape=(14, 2, 3)
bop_1913 = relay.not_equal(bop_1878.astype('bool'), relay.reshape(bop_1899.astype('bool'), relay.shape_of(bop_1878))) # shape=(14, 2, 3)
func_1357_call = mod.get_global_var('func_1357')
func_1358_call = mutated_mod.get_global_var('func_1358')
call_1917 = relay.TupleGetItem(func_1357_call(), 0)
call_1918 = relay.TupleGetItem(func_1358_call(), 0)
func_1464_call = mod.get_global_var('func_1464')
func_1465_call = mutated_mod.get_global_var('func_1465')
call_1922 = func_1464_call()
call_1923 = func_1464_call()
uop_1926 = relay.rsqrt(uop_1911.astype('float64')) # shape=(14, 2, 3)
func_1148_call = mod.get_global_var('func_1148')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_1934 = func_1148_call()
call_1935 = func_1148_call()
uop_1945 = relay.cosh(uop_1911.astype('float64')) # shape=(14, 2, 3)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_1948 = relay.TupleGetItem(func_713_call(), 1)
call_1949 = relay.TupleGetItem(func_714_call(), 1)
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_1959 = func_1240_call()
call_1960 = func_1240_call()
output = relay.Tuple([call_1903,call_1906,bop_1913,call_1917,call_1922,uop_1926,call_1934,uop_1945,call_1948,call_1959,])
output2 = relay.Tuple([call_1904,call_1907,bop_1913,call_1918,call_1923,uop_1926,call_1935,uop_1945,call_1949,call_1960,])
func_1975 = relay.Function([var_1876,var_1877,], output)
mod['func_1975'] = func_1975
mod = relay.transform.InferType()(mod)
mutated_mod['func_1975'] = func_1975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1975_call = mutated_mod.get_global_var('func_1975')
var_1977 = relay.var("var_1977", dtype = "float32", shape = (14, 2, 3))#candidate|1977|(14, 2, 3)|var|float32
var_1978 = relay.var("var_1978", dtype = "float32", shape = (14, 2, 3))#candidate|1978|(14, 2, 3)|var|float32
call_1976 = func_1975_call(var_1977,var_1978,)
output = call_1976
func_1979 = relay.Function([var_1977,var_1978,], output)
mutated_mod['func_1979'] = func_1979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2016 = relay.var("var_2016", dtype = "int8", shape = ())#candidate|2016|()|var|int8
const_2017 = relay.const([[[-1],[-10],[-2],[-3],[-9],[7],[-4],[6],[-4],[-3],[10],[-10],[5]],[[3],[3],[-9],[-9],[-1],[6],[-9],[-2],[6],[9],[-4],[-2],[6]]], dtype = "int8")#candidate|2017|(2, 13, 1)|const|int8
bop_2018 = relay.less(var_2016.astype('bool'), const_2017.astype('bool')) # shape=(2, 13, 1)
func_569_call = mod.get_global_var('func_569')
func_572_call = mutated_mod.get_global_var('func_572')
const_2022 = relay.const([False,True,False,False,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,False,False], dtype = "bool")#candidate|2022|(448,)|const|bool
call_2021 = relay.TupleGetItem(func_569_call(relay.reshape(const_2022.astype('bool'), [14, 8, 4])), 0)
call_2023 = relay.TupleGetItem(func_572_call(relay.reshape(const_2022.astype('bool'), [14, 8, 4])), 0)
output = relay.Tuple([bop_2018,call_2021,const_2022,])
output2 = relay.Tuple([bop_2018,call_2023,const_2022,])
func_2025 = relay.Function([var_2016,], output)
mod['func_2025'] = func_2025
mod = relay.transform.InferType()(mod)
var_2026 = relay.var("var_2026", dtype = "int8", shape = ())#candidate|2026|()|var|int8
output = func_2025(var_2026)
func_2027 = relay.Function([var_2026], output)
mutated_mod['func_2027'] = func_2027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1800_call = mod.get_global_var('func_1800')
func_1801_call = mutated_mod.get_global_var('func_1801')
call_2130 = relay.TupleGetItem(func_1800_call(), 0)
call_2131 = relay.TupleGetItem(func_1801_call(), 0)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_2140 = relay.TupleGetItem(func_108_call(), 0)
call_2141 = relay.TupleGetItem(func_110_call(), 0)
func_873_call = mod.get_global_var('func_873')
func_876_call = mutated_mod.get_global_var('func_876')
var_2146 = relay.var("var_2146", dtype = "float64", shape = (240,))#candidate|2146|(240,)|var|float64
call_2145 = relay.TupleGetItem(func_873_call(relay.reshape(var_2146.astype('float64'), [12, 5, 4]), relay.reshape(var_2146.astype('float64'), [12, 5, 4]), ), 2)
call_2147 = relay.TupleGetItem(func_876_call(relay.reshape(var_2146.astype('float64'), [12, 5, 4]), relay.reshape(var_2146.astype('float64'), [12, 5, 4]), ), 2)
output = relay.Tuple([call_2130,call_2140,call_2145,var_2146,])
output2 = relay.Tuple([call_2131,call_2141,call_2147,var_2146,])
func_2149 = relay.Function([var_2146,], output)
mod['func_2149'] = func_2149
mod = relay.transform.InferType()(mod)
mutated_mod['func_2149'] = func_2149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2150 = relay.var("var_2150", dtype = "float64", shape = (240,))#candidate|2150|(240,)|var|float64
func_2149_call = mutated_mod.get_global_var('func_2149')
call_2151 = func_2149_call(var_2150)
output = call_2151
func_2152 = relay.Function([var_2150], output)
mutated_mod['func_2152'] = func_2152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_2166 = relay.TupleGetItem(func_713_call(), 0)
call_2167 = relay.TupleGetItem(func_714_call(), 0)
output = call_2166
output2 = call_2167
func_2227 = relay.Function([], output)
mod['func_2227'] = func_2227
mod = relay.transform.InferType()(mod)
output = func_2227()
func_2228 = relay.Function([], output)
mutated_mod['func_2228'] = func_2228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_2255 = relay.TupleGetItem(func_1474_call(), 0)
call_2256 = relay.TupleGetItem(func_1476_call(), 0)
var_2277 = relay.var("var_2277", dtype = "float64", shape = (14, 8, 4))#candidate|2277|(14, 8, 4)|var|float64
bop_2278 = relay.bitwise_xor(call_2255.astype('uint16'), relay.reshape(var_2277.astype('uint16'), relay.shape_of(call_2255))) # shape=(14, 8, 4)
bop_2281 = relay.bitwise_xor(call_2256.astype('uint16'), relay.reshape(var_2277.astype('uint16'), relay.shape_of(call_2256))) # shape=(14, 8, 4)
func_481_call = mod.get_global_var('func_481')
func_483_call = mutated_mod.get_global_var('func_483')
call_2283 = func_481_call(relay.reshape(var_2277.astype('bool'), [14, 8, 4]))
call_2284 = func_481_call(relay.reshape(var_2277.astype('bool'), [14, 8, 4]))
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
var_2300 = relay.var("var_2300", dtype = "float32", shape = (880,))#candidate|2300|(880,)|var|float32
call_2299 = relay.TupleGetItem(func_435_call(relay.reshape(var_2300.astype('float32'), [11, 10, 8]), relay.reshape(var_2300.astype('float32'), [11, 10, 8]), ), 3)
call_2301 = relay.TupleGetItem(func_439_call(relay.reshape(var_2300.astype('float32'), [11, 10, 8]), relay.reshape(var_2300.astype('float32'), [11, 10, 8]), ), 3)
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
call_2318 = relay.TupleGetItem(func_435_call(relay.reshape(call_2299.astype('float32'), [11, 10, 8]), relay.reshape(call_2299.astype('float32'), [11, 10, 8]), ), 2)
call_2319 = relay.TupleGetItem(func_439_call(relay.reshape(call_2299.astype('float32'), [11, 10, 8]), relay.reshape(call_2299.astype('float32'), [11, 10, 8]), ), 2)
output = relay.Tuple([bop_2278,call_2283,call_2299,var_2300,call_2318,])
output2 = relay.Tuple([bop_2281,call_2284,call_2301,var_2300,call_2319,])
func_2323 = relay.Function([var_2277,var_2300,], output)
mod['func_2323'] = func_2323
mod = relay.transform.InferType()(mod)
mutated_mod['func_2323'] = func_2323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2323_call = mutated_mod.get_global_var('func_2323')
var_2325 = relay.var("var_2325", dtype = "float64", shape = (14, 8, 4))#candidate|2325|(14, 8, 4)|var|float64
var_2326 = relay.var("var_2326", dtype = "float32", shape = (880,))#candidate|2326|(880,)|var|float32
call_2324 = func_2323_call(var_2325,var_2326,)
output = call_2324
func_2327 = relay.Function([var_2325,var_2326,], output)
mutated_mod['func_2327'] = func_2327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_2334 = relay.TupleGetItem(func_713_call(), 0)
call_2335 = relay.TupleGetItem(func_714_call(), 0)
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_2336 = func_1240_call()
call_2337 = func_1240_call()
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_2341 = relay.TupleGetItem(func_108_call(), 0)
call_2342 = relay.TupleGetItem(func_110_call(), 0)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_2345 = relay.TupleGetItem(func_1699_call(), 7)
call_2346 = relay.TupleGetItem(func_1700_call(), 7)
func_1183_call = mod.get_global_var('func_1183')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_2351 = relay.TupleGetItem(func_1183_call(), 1)
call_2352 = relay.TupleGetItem(func_1185_call(), 1)
func_300_call = mod.get_global_var('func_300')
func_302_call = mutated_mod.get_global_var('func_302')
call_2353 = relay.TupleGetItem(func_300_call(relay.reshape(call_2351.astype('bool'), [14, 8, 4])), 1)
call_2354 = relay.TupleGetItem(func_302_call(relay.reshape(call_2351.astype('bool'), [14, 8, 4])), 1)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_2359 = relay.TupleGetItem(func_1743_call(), 1)
call_2360 = relay.TupleGetItem(func_1745_call(), 1)
output = relay.Tuple([call_2334,call_2336,call_2341,call_2345,call_2351,call_2353,call_2359,])
output2 = relay.Tuple([call_2335,call_2337,call_2342,call_2346,call_2352,call_2354,call_2360,])
func_2362 = relay.Function([], output)
mod['func_2362'] = func_2362
mod = relay.transform.InferType()(mod)
mutated_mod['func_2362'] = func_2362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2362_call = mutated_mod.get_global_var('func_2362')
call_2363 = func_2362_call()
output = call_2363
func_2364 = relay.Function([], output)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2392 = relay.var("var_2392", dtype = "int16", shape = (4, 16, 4))#candidate|2392|(4, 16, 4)|var|int16
var_2393 = relay.var("var_2393", dtype = "int16", shape = (4, 16, 4))#candidate|2393|(4, 16, 4)|var|int16
bop_2394 = relay.not_equal(var_2392.astype('bool'), relay.reshape(var_2393.astype('bool'), relay.shape_of(var_2392))) # shape=(4, 16, 4)
uop_2400 = relay.sinh(var_2393.astype('float32')) # shape=(4, 16, 4)
output = relay.Tuple([bop_2394,uop_2400,])
output2 = relay.Tuple([bop_2394,uop_2400,])
func_2402 = relay.Function([var_2392,var_2393,], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
var_2403 = relay.var("var_2403", dtype = "int16", shape = (4, 16, 4))#candidate|2403|(4, 16, 4)|var|int16
var_2404 = relay.var("var_2404", dtype = "int16", shape = (4, 16, 4))#candidate|2404|(4, 16, 4)|var|int16
output = func_2402(var_2403,var_2404,)
func_2405 = relay.Function([var_2403,var_2404,], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2413 = relay.var("var_2413", dtype = "float64", shape = (5, 7, 3))#candidate|2413|(5, 7, 3)|var|float64
uop_2414 = relay.asinh(var_2413.astype('float64')) # shape=(5, 7, 3)
output = relay.Tuple([uop_2414,])
output2 = relay.Tuple([uop_2414,])
func_2418 = relay.Function([var_2413,], output)
mod['func_2418'] = func_2418
mod = relay.transform.InferType()(mod)
var_2419 = relay.var("var_2419", dtype = "float64", shape = (5, 7, 3))#candidate|2419|(5, 7, 3)|var|float64
output = func_2418(var_2419)
func_2420 = relay.Function([var_2419], output)
mutated_mod['func_2420'] = func_2420
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2531 = relay.var("var_2531", dtype = "float32", shape = (7, 7, 6))#candidate|2531|(7, 7, 6)|var|float32
uop_2532 = relay.atan(var_2531.astype('float32')) # shape=(7, 7, 6)
output = uop_2532
output2 = uop_2532
func_2534 = relay.Function([var_2531,], output)
mod['func_2534'] = func_2534
mod = relay.transform.InferType()(mod)
mutated_mod['func_2534'] = func_2534
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2535 = relay.var("var_2535", dtype = "float32", shape = (7, 7, 6))#candidate|2535|(7, 7, 6)|var|float32
func_2534_call = mutated_mod.get_global_var('func_2534')
call_2536 = func_2534_call(var_2535)
output = call_2536
func_2537 = relay.Function([var_2535], output)
mutated_mod['func_2537'] = func_2537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mod.get_global_var('func_1357')
func_1358_call = mutated_mod.get_global_var('func_1358')
call_2605 = relay.TupleGetItem(func_1357_call(), 1)
call_2606 = relay.TupleGetItem(func_1358_call(), 1)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
const_2608 = relay.const(7, dtype = "int8")#candidate|2608|()|const|int8
call_2607 = relay.TupleGetItem(func_2025_call(relay.reshape(const_2608.astype('int8'), [])), 0)
call_2609 = relay.TupleGetItem(func_2027_call(relay.reshape(const_2608.astype('int8'), [])), 0)
bop_2619 = relay.left_shift(const_2608.astype('uint32'), call_2607.astype('uint32')) # shape=(2, 13, 1)
bop_2622 = relay.left_shift(const_2608.astype('uint32'), call_2609.astype('uint32')) # shape=(2, 13, 1)
output = relay.Tuple([call_2605,bop_2619,])
output2 = relay.Tuple([call_2606,bop_2622,])
func_2623 = relay.Function([], output)
mod['func_2623'] = func_2623
mod = relay.transform.InferType()(mod)
mutated_mod['func_2623'] = func_2623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mutated_mod.get_global_var('func_2623')
call_2624 = func_2623_call()
output = call_2624
func_2625 = relay.Function([], output)
mutated_mod['func_2625'] = func_2625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1464_call = mod.get_global_var('func_1464')
func_1465_call = mutated_mod.get_global_var('func_1465')
call_2673 = func_1464_call()
call_2674 = func_1464_call()
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
var_2676 = relay.var("var_2676", dtype = "float32", shape = (880,))#candidate|2676|(880,)|var|float32
call_2675 = relay.TupleGetItem(func_435_call(relay.reshape(var_2676.astype('float32'), [11, 10, 8]), relay.reshape(var_2676.astype('float32'), [11, 10, 8]), ), 4)
call_2677 = relay.TupleGetItem(func_439_call(relay.reshape(var_2676.astype('float32'), [11, 10, 8]), relay.reshape(var_2676.astype('float32'), [11, 10, 8]), ), 4)
output = relay.Tuple([call_2673,call_2675,var_2676,])
output2 = relay.Tuple([call_2674,call_2677,var_2676,])
func_2694 = relay.Function([var_2676,], output)
mod['func_2694'] = func_2694
mod = relay.transform.InferType()(mod)
var_2695 = relay.var("var_2695", dtype = "float32", shape = (880,))#candidate|2695|(880,)|var|float32
output = func_2694(var_2695)
func_2696 = relay.Function([var_2695], output)
mutated_mod['func_2696'] = func_2696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2727 = relay.var("var_2727", dtype = "float64", shape = (8, 3, 14))#candidate|2727|(8, 3, 14)|var|float64
var_2728 = relay.var("var_2728", dtype = "float64", shape = (8, 3, 14))#candidate|2728|(8, 3, 14)|var|float64
bop_2729 = relay.not_equal(var_2727.astype('bool'), relay.reshape(var_2728.astype('bool'), relay.shape_of(var_2727))) # shape=(8, 3, 14)
func_1853_call = mod.get_global_var('func_1853')
func_1854_call = mutated_mod.get_global_var('func_1854')
call_2744 = relay.TupleGetItem(func_1853_call(), 0)
call_2745 = relay.TupleGetItem(func_1854_call(), 0)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_2747 = relay.TupleGetItem(func_2623_call(), 0)
call_2748 = relay.TupleGetItem(func_2625_call(), 0)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_2770 = relay.TupleGetItem(func_713_call(), 0)
call_2771 = relay.TupleGetItem(func_714_call(), 0)
func_2323_call = mod.get_global_var('func_2323')
func_2327_call = mutated_mod.get_global_var('func_2327')
var_2804 = relay.var("var_2804", dtype = "float32", shape = (880,))#candidate|2804|(880,)|var|float32
call_2803 = relay.TupleGetItem(func_2323_call(relay.reshape(call_2747.astype('float64'), [14, 8, 4]), relay.reshape(var_2804.astype('float32'), [880,]), ), 1)
call_2805 = relay.TupleGetItem(func_2327_call(relay.reshape(call_2747.astype('float64'), [14, 8, 4]), relay.reshape(var_2804.astype('float32'), [880,]), ), 1)
output = relay.Tuple([bop_2729,call_2744,call_2747,call_2770,call_2803,var_2804,])
output2 = relay.Tuple([bop_2729,call_2745,call_2748,call_2771,call_2805,var_2804,])
func_2816 = relay.Function([var_2727,var_2728,var_2804,], output)
mod['func_2816'] = func_2816
mod = relay.transform.InferType()(mod)
var_2817 = relay.var("var_2817", dtype = "float64", shape = (8, 3, 14))#candidate|2817|(8, 3, 14)|var|float64
var_2818 = relay.var("var_2818", dtype = "float64", shape = (8, 3, 14))#candidate|2818|(8, 3, 14)|var|float64
var_2819 = relay.var("var_2819", dtype = "float32", shape = (880,))#candidate|2819|(880,)|var|float32
output = func_2816(var_2817,var_2818,var_2819,)
func_2820 = relay.Function([var_2817,var_2818,var_2819,], output)
mutated_mod['func_2820'] = func_2820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1853_call = mod.get_global_var('func_1853')
func_1854_call = mutated_mod.get_global_var('func_1854')
call_2830 = relay.TupleGetItem(func_1853_call(), 0)
call_2831 = relay.TupleGetItem(func_1854_call(), 0)
output = relay.Tuple([call_2830,])
output2 = relay.Tuple([call_2831,])
func_2832 = relay.Function([], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
output = func_2832()
func_2833 = relay.Function([], output)
mutated_mod['func_2833'] = func_2833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mod.get_global_var('func_1757')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_2839 = func_1757_call()
call_2840 = func_1757_call()
func_2534_call = mod.get_global_var('func_2534')
func_2537_call = mutated_mod.get_global_var('func_2537')
var_2850 = relay.var("var_2850", dtype = "float32", shape = (7, 42))#candidate|2850|(7, 42)|var|float32
call_2849 = func_2534_call(relay.reshape(var_2850.astype('float32'), [7, 7, 6]))
call_2851 = func_2534_call(relay.reshape(var_2850.astype('float32'), [7, 7, 6]))
output = relay.Tuple([call_2839,call_2849,var_2850,])
output2 = relay.Tuple([call_2840,call_2851,var_2850,])
func_2856 = relay.Function([var_2850,], output)
mod['func_2856'] = func_2856
mod = relay.transform.InferType()(mod)
mutated_mod['func_2856'] = func_2856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2857 = relay.var("var_2857", dtype = "float32", shape = (7, 42))#candidate|2857|(7, 42)|var|float32
func_2856_call = mutated_mod.get_global_var('func_2856')
call_2858 = func_2856_call(var_2857)
output = call_2858
func_2859 = relay.Function([var_2857], output)
mutated_mod['func_2859'] = func_2859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_2910 = relay.TupleGetItem(func_1743_call(), 1)
call_2911 = relay.TupleGetItem(func_1745_call(), 1)
func_2418_call = mod.get_global_var('func_2418')
func_2420_call = mutated_mod.get_global_var('func_2420')
var_2913 = relay.var("var_2913", dtype = "float64", shape = (105,))#candidate|2913|(105,)|var|float64
call_2912 = relay.TupleGetItem(func_2418_call(relay.reshape(var_2913.astype('float64'), [5, 7, 3])), 0)
call_2914 = relay.TupleGetItem(func_2420_call(relay.reshape(var_2913.astype('float64'), [5, 7, 3])), 0)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_2921 = relay.TupleGetItem(func_235_call(), 1)
call_2922 = relay.TupleGetItem(func_237_call(), 1)
bop_2924 = relay.maximum(call_2921.astype('float64'), relay.reshape(call_2910.astype('float64'), relay.shape_of(call_2921))) # shape=(14, 8, 4)
bop_2927 = relay.maximum(call_2922.astype('float64'), relay.reshape(call_2911.astype('float64'), relay.shape_of(call_2922))) # shape=(14, 8, 4)
output = relay.Tuple([call_2912,var_2913,bop_2924,])
output2 = relay.Tuple([call_2914,var_2913,bop_2927,])
func_2938 = relay.Function([var_2913,], output)
mod['func_2938'] = func_2938
mod = relay.transform.InferType()(mod)
mutated_mod['func_2938'] = func_2938
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2939 = relay.var("var_2939", dtype = "float64", shape = (105,))#candidate|2939|(105,)|var|float64
func_2938_call = mutated_mod.get_global_var('func_2938')
call_2940 = func_2938_call(var_2939)
output = call_2940
func_2941 = relay.Function([var_2939], output)
mutated_mod['func_2941'] = func_2941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_2955 = relay.TupleGetItem(func_650_call(), 1)
call_2956 = relay.TupleGetItem(func_652_call(), 1)
func_2362_call = mod.get_global_var('func_2362')
func_2364_call = mutated_mod.get_global_var('func_2364')
call_2961 = relay.TupleGetItem(func_2362_call(), 2)
call_2962 = relay.TupleGetItem(func_2364_call(), 2)
output = relay.Tuple([call_2955,call_2961,])
output2 = relay.Tuple([call_2956,call_2962,])
func_2968 = relay.Function([], output)
mod['func_2968'] = func_2968
mod = relay.transform.InferType()(mod)
output = func_2968()
func_2969 = relay.Function([], output)
mutated_mod['func_2969'] = func_2969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_2988 = relay.TupleGetItem(func_1474_call(), 0)
call_2989 = relay.TupleGetItem(func_1476_call(), 0)
output = relay.Tuple([call_2988,])
output2 = relay.Tuple([call_2989,])
func_2997 = relay.Function([], output)
mod['func_2997'] = func_2997
mod = relay.transform.InferType()(mod)
output = func_2997()
func_2998 = relay.Function([], output)
mutated_mod['func_2998'] = func_2998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_3001 = relay.TupleGetItem(func_1072_call(), 3)
call_3002 = relay.TupleGetItem(func_1073_call(), 3)
output = call_3001
output2 = call_3002
func_3011 = relay.Function([], output)
mod['func_3011'] = func_3011
mod = relay.transform.InferType()(mod)
mutated_mod['func_3011'] = func_3011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3011_call = mutated_mod.get_global_var('func_3011')
call_3012 = func_3011_call()
output = call_3012
func_3013 = relay.Function([], output)
mutated_mod['func_3013'] = func_3013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_3041 = relay.TupleGetItem(func_2968_call(), 1)
call_3042 = relay.TupleGetItem(func_2969_call(), 1)
output = relay.Tuple([call_3041,])
output2 = relay.Tuple([call_3042,])
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
func_2362_call = mod.get_global_var('func_2362')
func_2364_call = mutated_mod.get_global_var('func_2364')
call_3062 = relay.TupleGetItem(func_2362_call(), 4)
call_3063 = relay.TupleGetItem(func_2364_call(), 4)
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
var_3074 = relay.var("var_3074", dtype = "int8", shape = ())#candidate|3074|()|var|int8
call_3073 = relay.TupleGetItem(func_2025_call(relay.reshape(var_3074.astype('int8'), [])), 1)
call_3075 = relay.TupleGetItem(func_2027_call(relay.reshape(var_3074.astype('int8'), [])), 1)
func_1148_call = mod.get_global_var('func_1148')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_3076 = func_1148_call()
call_3077 = func_1148_call()
output = relay.Tuple([call_3062,call_3073,var_3074,call_3076,])
output2 = relay.Tuple([call_3063,call_3075,var_3074,call_3077,])
func_3091 = relay.Function([var_3074,], output)
mod['func_3091'] = func_3091
mod = relay.transform.InferType()(mod)
mutated_mod['func_3091'] = func_3091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3092 = relay.var("var_3092", dtype = "int8", shape = ())#candidate|3092|()|var|int8
func_3091_call = mutated_mod.get_global_var('func_3091')
call_3093 = func_3091_call(var_3092)
output = call_3093
func_3094 = relay.Function([var_3092], output)
mutated_mod['func_3094'] = func_3094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_807_call = mod.get_global_var('func_807')
func_809_call = mutated_mod.get_global_var('func_809')
call_3172 = relay.TupleGetItem(func_807_call(), 3)
call_3173 = relay.TupleGetItem(func_809_call(), 3)
func_2832_call = mod.get_global_var('func_2832')
func_2833_call = mutated_mod.get_global_var('func_2833')
call_3178 = relay.TupleGetItem(func_2832_call(), 0)
call_3179 = relay.TupleGetItem(func_2833_call(), 0)
output = relay.Tuple([call_3172,call_3178,])
output2 = relay.Tuple([call_3173,call_3179,])
func_3233 = relay.Function([], output)
mod['func_3233'] = func_3233
mod = relay.transform.InferType()(mod)
mutated_mod['func_3233'] = func_3233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3233_call = mutated_mod.get_global_var('func_3233')
call_3234 = func_3233_call()
output = call_3234
func_3235 = relay.Function([], output)
mutated_mod['func_3235'] = func_3235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_3291 = relay.TupleGetItem(func_882_call(), 0)
call_3292 = relay.TupleGetItem(func_884_call(), 0)
uop_3297 = relay.atanh(call_3291.astype('float64')) # shape=(14, 8, 4)
uop_3299 = relay.atanh(call_3292.astype('float64')) # shape=(14, 8, 4)
output = relay.Tuple([uop_3297,])
output2 = relay.Tuple([uop_3299,])
func_3309 = relay.Function([], output)
mod['func_3309'] = func_3309
mod = relay.transform.InferType()(mod)
output = func_3309()
func_3310 = relay.Function([], output)
mutated_mod['func_3310'] = func_3310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3365 = relay.var("var_3365", dtype = "float32", shape = (15, 16, 10))#candidate|3365|(15, 16, 10)|var|float32
uop_3366 = relay.erf(var_3365.astype('float32')) # shape=(15, 16, 10)
func_873_call = mod.get_global_var('func_873')
func_876_call = mutated_mod.get_global_var('func_876')
var_3371 = relay.var("var_3371", dtype = "float64", shape = (240,))#candidate|3371|(240,)|var|float64
call_3370 = relay.TupleGetItem(func_873_call(relay.reshape(var_3371.astype('float64'), [12, 5, 4]), relay.reshape(var_3371.astype('float64'), [12, 5, 4]), ), 2)
call_3372 = relay.TupleGetItem(func_876_call(relay.reshape(var_3371.astype('float64'), [12, 5, 4]), relay.reshape(var_3371.astype('float64'), [12, 5, 4]), ), 2)
output = relay.Tuple([uop_3366,call_3370,var_3371,])
output2 = relay.Tuple([uop_3366,call_3372,var_3371,])
func_3376 = relay.Function([var_3365,var_3371,], output)
mod['func_3376'] = func_3376
mod = relay.transform.InferType()(mod)
mutated_mod['func_3376'] = func_3376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mutated_mod.get_global_var('func_3376')
var_3378 = relay.var("var_3378", dtype = "float32", shape = (15, 16, 10))#candidate|3378|(15, 16, 10)|var|float32
var_3379 = relay.var("var_3379", dtype = "float64", shape = (240,))#candidate|3379|(240,)|var|float64
call_3377 = func_3376_call(var_3378,var_3379,)
output = call_3377
func_3380 = relay.Function([var_3378,var_3379,], output)
mutated_mod['func_3380'] = func_3380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_3397 = relay.TupleGetItem(func_713_call(), 1)
call_3398 = relay.TupleGetItem(func_714_call(), 1)
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_3399 = relay.TupleGetItem(func_1474_call(), 0)
call_3400 = relay.TupleGetItem(func_1476_call(), 0)
output = relay.Tuple([call_3397,call_3399,])
output2 = relay.Tuple([call_3398,call_3400,])
func_3403 = relay.Function([], output)
mod['func_3403'] = func_3403
mod = relay.transform.InferType()(mod)
mutated_mod['func_3403'] = func_3403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3403_call = mutated_mod.get_global_var('func_3403')
call_3404 = func_3403_call()
output = call_3404
func_3405 = relay.Function([], output)
mutated_mod['func_3405'] = func_3405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1800_call = mod.get_global_var('func_1800')
func_1801_call = mutated_mod.get_global_var('func_1801')
call_3445 = relay.TupleGetItem(func_1800_call(), 0)
call_3446 = relay.TupleGetItem(func_1801_call(), 0)
func_1975_call = mod.get_global_var('func_1975')
func_1979_call = mutated_mod.get_global_var('func_1979')
var_3449 = relay.var("var_3449", dtype = "float32", shape = (84,))#candidate|3449|(84,)|var|float32
call_3448 = relay.TupleGetItem(func_1975_call(relay.reshape(var_3449.astype('float32'), [14, 2, 3]), relay.reshape(var_3449.astype('float32'), [14, 2, 3]), ), 3)
call_3450 = relay.TupleGetItem(func_1979_call(relay.reshape(var_3449.astype('float32'), [14, 2, 3]), relay.reshape(var_3449.astype('float32'), [14, 2, 3]), ), 3)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_3454 = relay.TupleGetItem(func_1699_call(), 2)
call_3455 = relay.TupleGetItem(func_1700_call(), 2)
func_1183_call = mod.get_global_var('func_1183')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_3465 = relay.TupleGetItem(func_1183_call(), 2)
call_3466 = relay.TupleGetItem(func_1185_call(), 2)
output = relay.Tuple([call_3445,call_3448,var_3449,call_3454,call_3465,])
output2 = relay.Tuple([call_3446,call_3450,var_3449,call_3455,call_3466,])
func_3474 = relay.Function([var_3449,], output)
mod['func_3474'] = func_3474
mod = relay.transform.InferType()(mod)
mutated_mod['func_3474'] = func_3474
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3475 = relay.var("var_3475", dtype = "float32", shape = (84,))#candidate|3475|(84,)|var|float32
func_3474_call = mutated_mod.get_global_var('func_3474')
call_3476 = func_3474_call(var_3475)
output = call_3476
func_3477 = relay.Function([var_3475], output)
mutated_mod['func_3477'] = func_3477
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3490 = relay.const([[[-5.313937,3.895382,5.712881,-4.629785,-6.390946],[-6.472580,3.098995,-3.637790,1.008857,-7.007430],[-6.865811,-0.399203,3.152319,-3.196458,-2.849826],[2.571420,5.940531,-9.002924,0.064915,-9.465580],[-1.800027,-9.034461,5.460732,0.948328,0.760339],[-6.539713,0.727998,-5.574772,-3.767979,0.503925],[-8.362956,4.927174,1.234656,-4.933281,7.847840],[1.667099,-8.126002,6.983759,-8.110696,-6.191912],[2.008784,1.659906,-6.518169,3.731033,-8.294591],[3.493840,0.235368,-9.083697,1.365056,2.166325],[2.549643,-9.953475,7.071004,-3.637212,-6.627781],[4.313564,1.416954,-2.037132,-8.791987,-1.517301],[4.952314,4.650868,9.193980,1.693587,4.092887],[6.848268,4.485509,-7.496639,3.168305,-4.900698]],[[5.474737,6.159423,-8.689776,-5.673403,1.864377],[7.027970,2.308751,-6.878241,-5.846928,8.975855],[-5.862818,8.987526,-0.241765,-6.424356,-9.971504],[7.119624,6.003633,-7.130643,6.168981,-6.894879],[-9.460377,0.396704,7.495782,-6.851230,8.348437],[0.473557,-0.505099,-8.151601,-4.711311,-1.004839],[1.885437,-8.925308,9.348714,8.004269,-3.664462],[7.852281,8.659045,-1.896537,-7.829903,8.118100],[-1.260791,-7.391663,4.776164,9.816309,5.199161],[-0.173297,7.998721,0.547434,7.453998,4.584446],[3.856802,-4.289849,1.389641,0.505530,5.746016],[-6.167054,0.904935,-3.352707,4.931448,-0.789318],[-0.307342,5.833732,6.554997,-9.657899,9.643985],[-5.052696,-9.072540,-7.274754,9.744602,-1.511727]],[[-2.220021,-4.847896,8.773262,-2.572463,-1.199554],[0.485449,6.899916,7.763914,-1.697079,9.854779],[6.779457,-1.450954,9.878206,-5.632782,-5.014336],[2.148859,5.330630,-5.748008,9.247131,3.589339],[5.930977,-6.339281,1.233381,3.349849,2.548502],[-7.805830,4.365883,-1.220137,9.747128,5.332257],[1.241616,-8.858516,6.520462,0.988601,2.382815],[-3.197781,-6.636714,7.616790,-9.091945,5.867987],[6.421282,9.811356,-2.724867,8.278985,-7.994864],[3.279018,-1.168627,-6.859743,-5.245708,-5.764924],[-7.780907,-4.141588,1.804333,-1.135859,-4.717492],[8.187360,6.762798,-8.345459,-4.187398,3.694933],[9.589509,9.003395,-9.931213,1.930913,3.256945],[-2.297979,-3.490704,-5.710620,-4.278830,-0.934631]],[[-3.976432,5.713213,-7.408854,4.538763,7.241014],[2.234422,6.140141,-9.768242,-2.237350,-1.540556],[4.098853,3.614109,1.531939,7.295116,-8.333347],[0.482284,0.349444,5.353798,-9.650129,8.025805],[3.019179,-1.074391,1.851820,4.052048,-4.904451],[5.635725,-9.601202,-7.488206,2.396183,-9.122273],[9.429510,-8.420997,-0.202286,-2.087446,1.472061],[-7.234713,-9.553595,7.715745,-8.575874,3.230599],[2.275269,-9.697290,7.873044,6.621418,6.030016],[-9.483427,7.875591,9.950578,-4.822289,4.307137],[9.287872,6.805602,-0.760488,0.657143,5.982288],[-5.480307,-1.913158,-4.127192,7.560766,-8.666735],[8.579441,6.988477,9.916115,-0.763097,-2.914380],[9.311765,-0.588591,0.344861,-8.016087,3.324886]],[[6.286361,-8.131932,-3.219412,4.438003,-9.013863],[-0.204795,-6.075708,0.912936,9.060869,-0.064522],[4.306661,0.657388,-3.055993,-4.605877,-2.365702],[-6.277021,4.318450,2.295476,9.658606,4.384002],[-3.101176,-4.701874,8.274172,-4.182149,2.515192],[-8.695256,7.540812,-1.289777,-3.503739,-1.413755],[-6.052622,-1.228279,9.662980,-5.090664,-7.400813],[-6.439120,4.616880,-6.235051,-2.829820,7.007541],[4.446775,-0.084726,-9.392150,-7.480870,-1.074837],[3.295452,9.601256,-9.525378,6.469766,2.107802],[3.919371,-1.631412,-6.754350,7.521776,2.927747],[2.881747,5.907371,7.607165,-0.267299,-2.364771],[-3.639931,-3.658675,-4.676133,-0.177815,6.072932],[7.655565,-1.566719,6.648071,-5.905699,1.518786]],[[-0.248407,-6.312955,4.804002,4.586762,0.269676],[-4.779219,1.447611,6.749367,8.670503,0.827568],[-5.007132,1.276641,-7.387920,6.684071,-8.504863],[-0.766904,0.236566,-9.701689,7.246729,3.072213],[6.989554,-3.985092,-0.841708,-5.075992,-6.660642],[-7.386850,9.620379,8.942970,-6.869041,-6.913208],[6.305225,4.493958,-0.581561,3.753768,6.024536],[-3.040070,-8.548576,1.534632,8.260067,9.937714],[0.659497,-0.033585,6.218845,-8.693921,-8.298571],[-1.983185,-4.908204,0.055699,8.122160,-6.783673],[9.196261,-2.868576,5.273208,-1.463881,2.460930],[-7.409829,8.575867,6.080695,-1.600808,-6.743858],[1.457671,9.908700,8.279286,-0.708223,3.991968],[4.362323,5.383194,3.346453,-4.358606,6.433169]],[[3.088990,-0.435937,-6.938331,3.706385,-2.088546],[-5.275129,1.009056,3.663120,-3.195001,2.992603],[-1.365548,-5.534679,-8.740564,-6.366797,1.196049],[1.647244,-6.107695,4.625293,7.763768,8.031938],[-0.747130,9.226050,7.496866,-0.720329,-3.775712],[-5.799039,3.702137,2.835341,-0.984556,-6.982740],[1.242103,-8.260710,6.486320,9.831140,-3.723082],[-6.586102,-7.313320,-5.242005,-7.622779,9.356456],[9.200634,3.405418,-9.646166,-0.929113,1.850166],[-3.863327,-1.211945,-2.253442,-8.044751,3.529374],[-3.461480,4.909525,1.263565,1.360906,5.664221],[3.418585,-3.374166,3.971934,1.964399,7.100848],[-9.060674,6.167855,-7.144216,-8.391358,1.032940],[7.462399,-6.582547,-6.890757,7.810833,8.428147]],[[-9.287255,7.572986,-7.990898,3.732621,-4.673581],[-1.790864,-8.712599,-5.647326,8.652648,4.174565],[-1.283091,-6.163717,-2.456641,-5.253276,-2.649456],[-9.354308,-4.563066,3.184888,-5.580648,-0.454015],[5.634020,2.209534,3.692800,-8.140500,-2.655908],[8.822277,8.183856,7.746030,6.076939,1.977170],[-6.049048,-1.966307,1.355799,8.657097,3.669021],[-1.627588,-1.642395,-8.780793,1.226268,-6.576805],[0.813481,-3.567003,4.406415,-9.852032,-1.050934],[1.930691,6.383712,1.487291,1.312348,-0.696167],[5.488110,-4.670519,-5.011486,1.695905,5.992903],[8.747295,9.877826,2.176948,-8.876022,1.321300],[3.758569,4.648465,6.280065,2.361427,5.383149],[4.186690,8.459205,-7.355787,-2.776249,0.633557]],[[1.177374,-9.605627,8.264010,9.178954,7.561621],[-7.995236,4.052341,2.390978,-9.936311,-4.472753],[-6.010467,-7.101571,1.760916,2.960016,-4.892056],[8.303386,-9.730840,5.957318,-5.945390,5.615024],[2.481514,-6.140791,9.935934,3.027739,3.776239],[3.573351,3.876761,9.343864,-4.328838,4.650798],[6.866963,-4.907875,-8.755601,1.486803,-4.816657],[4.148350,-7.917332,5.357640,2.955447,-4.732515],[-3.139842,9.221687,2.427273,-6.636137,2.176383],[0.452956,-7.608958,-7.840523,2.161738,2.600152],[-2.744123,4.880424,7.957280,-7.322308,-4.629513],[6.252435,-6.501560,-8.893648,2.984209,7.265076],[-9.057289,9.932380,-8.496269,-5.632950,-8.307298],[-3.364282,-0.055541,1.277816,-1.143300,-4.898576]],[[-5.280814,0.484058,-7.406557,2.262530,-7.890949],[6.754920,7.155177,3.724951,-0.707945,4.431011],[-8.156853,-0.675052,8.673968,-4.411324,8.829773],[-7.258161,-2.723463,2.263536,-2.636106,-6.633495],[9.521056,7.196517,-8.127661,2.393573,-2.262746],[7.518239,-2.082672,2.532860,-7.728863,9.933461],[7.910792,1.712156,8.881435,-2.140313,7.072444],[-0.708770,-1.512967,4.480533,-9.979770,-2.243024],[3.090105,4.815699,0.738295,-8.267151,-3.647532],[0.012944,6.394622,5.842790,7.304833,-7.589884],[-1.443385,-1.411121,4.368309,-0.062851,-3.023890],[-9.749558,-7.092536,1.411878,7.792402,3.637706],[8.804792,3.256002,-8.609821,5.539784,-7.160099],[-9.717004,-8.908136,-0.917946,9.908849,3.628136]],[[3.003599,0.148558,-3.752805,8.869917,-4.681142],[8.747105,0.177053,4.101602,-0.830682,-5.600606],[-3.022071,7.264670,8.036677,-7.744072,-0.557860],[-5.255609,-4.023841,-1.279333,-5.548610,-7.274294],[-6.801355,-2.936771,-6.789544,6.681849,-7.737469],[3.426147,8.816263,3.067770,-9.053162,3.113343],[3.005400,-4.113043,3.199725,-0.911870,-3.113555],[0.006708,8.919406,5.395597,0.656762,-8.060178],[-5.839755,-2.613626,-0.751818,-6.231818,-9.029723],[-7.037478,8.055602,9.095725,6.686153,-6.179785],[-0.348785,-5.541806,3.280679,9.822101,1.290441],[-0.794056,6.927011,8.882119,-7.098463,1.978557],[4.271793,-7.819778,-9.335094,3.996925,-8.769446],[-4.988885,2.941328,-2.198081,-7.638516,8.743350]],[[9.731286,3.824996,1.173560,-6.768475,-9.664509],[-3.042881,7.747436,-9.057478,-1.002990,1.252882],[9.543666,3.047635,2.764739,6.986481,3.224235],[3.852978,-9.886188,3.431736,9.063645,5.652406],[3.046701,3.162371,-8.833879,8.799011,3.910293],[6.590587,-0.880927,-6.537416,-8.490417,9.515632],[-9.223229,-1.141844,8.835415,-1.343147,-0.590041],[-0.871767,9.654974,-9.805660,7.230234,-6.556850],[8.761920,1.515329,-6.556480,6.629935,9.377659],[-9.062585,3.240494,-8.088165,7.516973,8.443123],[-5.538731,0.057828,9.088743,3.307366,4.044801],[2.521353,-3.827502,-9.155098,-8.738160,8.458595],[-7.950217,-7.882542,6.864264,-8.007812,0.305291],[-0.345014,6.164970,-0.239485,5.845131,7.051563]],[[6.871156,3.436672,6.530228,7.190628,7.835533],[1.172162,-6.814706,1.077347,-0.417636,-7.072496],[8.240478,4.900037,0.867256,4.675621,-7.702576],[4.760668,-3.956797,1.126735,9.031993,1.908537],[6.280843,-9.479001,-5.247684,9.535271,-2.393883],[3.260222,-7.132697,-6.697946,-7.847458,0.954085],[0.286377,-6.306379,9.854704,9.455436,-1.178992],[-9.614696,-0.424463,-6.148577,-7.415221,1.401052],[2.765738,5.801023,-1.246142,1.464583,2.729978],[4.611165,-5.182582,-1.148154,8.436776,-0.501609],[6.524289,6.321245,9.761177,-1.231035,-1.873964],[-7.433212,-7.245826,2.626045,-7.042370,2.320326],[7.029679,-1.698210,8.763847,-2.143063,-8.558984],[-4.702647,0.145271,5.353604,0.800609,-2.735829]]], dtype = "float32")#candidate|3490|(13, 14, 5)|const|float32
uop_3491 = relay.asinh(const_3490.astype('float32')) # shape=(13, 14, 5)
output = uop_3491
output2 = uop_3491
func_3502 = relay.Function([], output)
mod['func_3502'] = func_3502
mod = relay.transform.InferType()(mod)
mutated_mod['func_3502'] = func_3502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3502_call = mutated_mod.get_global_var('func_3502')
call_3503 = func_3502_call()
output = call_3503
func_3504 = relay.Function([], output)
mutated_mod['func_3504'] = func_3504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3620 = relay.var("var_3620", dtype = "float64", shape = (10, 13, 1))#candidate|3620|(10, 13, 1)|var|float64
uop_3621 = relay.acosh(var_3620.astype('float64')) # shape=(10, 13, 1)
uop_3623 = relay.sqrt(uop_3621.astype('float64')) # shape=(10, 13, 1)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_3646 = relay.TupleGetItem(func_1743_call(), 3)
call_3647 = relay.TupleGetItem(func_1745_call(), 3)
output = relay.Tuple([uop_3623,call_3646,])
output2 = relay.Tuple([uop_3623,call_3647,])
func_3648 = relay.Function([var_3620,], output)
mod['func_3648'] = func_3648
mod = relay.transform.InferType()(mod)
mutated_mod['func_3648'] = func_3648
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3649 = relay.var("var_3649", dtype = "float64", shape = (10, 13, 1))#candidate|3649|(10, 13, 1)|var|float64
func_3648_call = mutated_mod.get_global_var('func_3648')
call_3650 = func_3648_call(var_3649)
output = call_3650
func_3651 = relay.Function([var_3649], output)
mutated_mod['func_3651'] = func_3651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3665 = relay.var("var_3665", dtype = "float32", shape = (7, 5, 9))#candidate|3665|(7, 5, 9)|var|float32
var_3666 = relay.var("var_3666", dtype = "float32", shape = (7, 5, 9))#candidate|3666|(7, 5, 9)|var|float32
bop_3667 = relay.floor_divide(var_3665.astype('float32'), relay.reshape(var_3666.astype('float32'), relay.shape_of(var_3665))) # shape=(7, 5, 9)
output = relay.Tuple([bop_3667,])
output2 = relay.Tuple([bop_3667,])
func_3671 = relay.Function([var_3665,var_3666,], output)
mod['func_3671'] = func_3671
mod = relay.transform.InferType()(mod)
mutated_mod['func_3671'] = func_3671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3671_call = mutated_mod.get_global_var('func_3671')
var_3673 = relay.var("var_3673", dtype = "float32", shape = (7, 5, 9))#candidate|3673|(7, 5, 9)|var|float32
var_3674 = relay.var("var_3674", dtype = "float32", shape = (7, 5, 9))#candidate|3674|(7, 5, 9)|var|float32
call_3672 = func_3671_call(var_3673,var_3674,)
output = call_3672
func_3675 = relay.Function([var_3673,var_3674,], output)
mutated_mod['func_3675'] = func_3675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_3696 = relay.TupleGetItem(func_735_call(), 0)
call_3697 = relay.TupleGetItem(func_737_call(), 0)
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_3699 = relay.TupleGetItem(func_1474_call(), 0)
call_3700 = relay.TupleGetItem(func_1476_call(), 0)
output = relay.Tuple([call_3696,call_3699,])
output2 = relay.Tuple([call_3697,call_3700,])
func_3703 = relay.Function([], output)
mod['func_3703'] = func_3703
mod = relay.transform.InferType()(mod)
mutated_mod['func_3703'] = func_3703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mutated_mod.get_global_var('func_3703')
call_3704 = func_3703_call()
output = call_3704
func_3705 = relay.Function([], output)
mutated_mod['func_3705'] = func_3705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_3731 = relay.TupleGetItem(func_882_call(), 0)
call_3732 = relay.TupleGetItem(func_884_call(), 0)
output = call_3731
output2 = call_3732
func_3736 = relay.Function([], output)
mod['func_3736'] = func_3736
mod = relay.transform.InferType()(mod)
output = func_3736()
func_3737 = relay.Function([], output)
mutated_mod['func_3737'] = func_3737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_3762 = relay.TupleGetItem(func_108_call(), 0)
call_3763 = relay.TupleGetItem(func_110_call(), 0)
var_3772 = relay.var("var_3772", dtype = "bool", shape = (14, 8, 4))#candidate|3772|(14, 8, 4)|var|bool
bop_3773 = relay.logical_xor(call_3762.astype('int8'), relay.reshape(var_3772.astype('int8'), relay.shape_of(call_3762))) # shape=(14, 8, 4)
bop_3776 = relay.logical_xor(call_3763.astype('int8'), relay.reshape(var_3772.astype('int8'), relay.shape_of(call_3763))) # shape=(14, 8, 4)
output = bop_3773
output2 = bop_3776
func_3781 = relay.Function([var_3772,], output)
mod['func_3781'] = func_3781
mod = relay.transform.InferType()(mod)
mutated_mod['func_3781'] = func_3781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3782 = relay.var("var_3782", dtype = "bool", shape = (14, 8, 4))#candidate|3782|(14, 8, 4)|var|bool
func_3781_call = mutated_mod.get_global_var('func_3781')
call_3783 = func_3781_call(var_3782)
output = call_3783
func_3784 = relay.Function([var_3782], output)
mutated_mod['func_3784'] = func_3784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mod.get_global_var('func_1757')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_3821 = func_1757_call()
call_3822 = func_1757_call()
func_2938_call = mod.get_global_var('func_2938')
func_2941_call = mutated_mod.get_global_var('func_2941')
var_3824 = relay.var("var_3824", dtype = "float64", shape = (105,))#candidate|3824|(105,)|var|float64
call_3823 = relay.TupleGetItem(func_2938_call(relay.reshape(var_3824.astype('float64'), [105,])), 0)
call_3825 = relay.TupleGetItem(func_2941_call(relay.reshape(var_3824.astype('float64'), [105,])), 0)
output = relay.Tuple([call_3821,call_3823,var_3824,])
output2 = relay.Tuple([call_3822,call_3825,var_3824,])
func_3832 = relay.Function([var_3824,], output)
mod['func_3832'] = func_3832
mod = relay.transform.InferType()(mod)
var_3833 = relay.var("var_3833", dtype = "float64", shape = (105,))#candidate|3833|(105,)|var|float64
output = func_3832(var_3833)
func_3834 = relay.Function([var_3833], output)
mutated_mod['func_3834'] = func_3834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_3852 = relay.TupleGetItem(func_235_call(), 0)
call_3853 = relay.TupleGetItem(func_237_call(), 0)
output = relay.Tuple([call_3852,])
output2 = relay.Tuple([call_3853,])
func_3862 = relay.Function([], output)
mod['func_3862'] = func_3862
mod = relay.transform.InferType()(mod)
output = func_3862()
func_3863 = relay.Function([], output)
mutated_mod['func_3863'] = func_3863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_3874 = relay.TupleGetItem(func_713_call(), 1)
call_3875 = relay.TupleGetItem(func_714_call(), 1)
func_569_call = mod.get_global_var('func_569')
func_572_call = mutated_mod.get_global_var('func_572')
call_3878 = relay.TupleGetItem(func_569_call(relay.reshape(call_3874.astype('bool'), [14, 8, 4])), 1)
call_3879 = relay.TupleGetItem(func_572_call(relay.reshape(call_3874.astype('bool'), [14, 8, 4])), 1)
uop_3880 = relay.asin(call_3878.astype('float64')) # shape=(14, 8, 4)
uop_3882 = relay.asin(call_3879.astype('float64')) # shape=(14, 8, 4)
bop_3900 = relay.bitwise_or(call_3874.astype('uint16'), relay.reshape(call_3878.astype('uint16'), relay.shape_of(call_3874))) # shape=(14, 8, 4)
bop_3903 = relay.bitwise_or(call_3875.astype('uint16'), relay.reshape(call_3879.astype('uint16'), relay.shape_of(call_3875))) # shape=(14, 8, 4)
func_3403_call = mod.get_global_var('func_3403')
func_3405_call = mutated_mod.get_global_var('func_3405')
call_3913 = relay.TupleGetItem(func_3403_call(), 0)
call_3914 = relay.TupleGetItem(func_3405_call(), 0)
output = relay.Tuple([uop_3880,bop_3900,call_3913,])
output2 = relay.Tuple([uop_3882,bop_3903,call_3914,])
func_3915 = relay.Function([], output)
mod['func_3915'] = func_3915
mod = relay.transform.InferType()(mod)
output = func_3915()
func_3916 = relay.Function([], output)
mutated_mod['func_3916'] = func_3916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mod.get_global_var('func_1357')
func_1358_call = mutated_mod.get_global_var('func_1358')
call_3951 = relay.TupleGetItem(func_1357_call(), 0)
call_3952 = relay.TupleGetItem(func_1358_call(), 0)
uop_3953 = relay.sin(call_3951.astype('float32')) # shape=(14, 8, 4)
uop_3955 = relay.sin(call_3952.astype('float32')) # shape=(14, 8, 4)
output = uop_3953
output2 = uop_3955
func_3956 = relay.Function([], output)
mod['func_3956'] = func_3956
mod = relay.transform.InferType()(mod)
output = func_3956()
func_3957 = relay.Function([], output)
mutated_mod['func_3957'] = func_3957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_807_call = mod.get_global_var('func_807')
func_809_call = mutated_mod.get_global_var('func_809')
call_3960 = relay.TupleGetItem(func_807_call(), 1)
call_3961 = relay.TupleGetItem(func_809_call(), 1)
uop_3964 = relay.asinh(call_3960.astype('float64')) # shape=(14, 8, 4)
uop_3966 = relay.asinh(call_3961.astype('float64')) # shape=(14, 8, 4)
func_1800_call = mod.get_global_var('func_1800')
func_1801_call = mutated_mod.get_global_var('func_1801')
call_3972 = relay.TupleGetItem(func_1800_call(), 0)
call_3973 = relay.TupleGetItem(func_1801_call(), 0)
func_2323_call = mod.get_global_var('func_2323')
func_2327_call = mutated_mod.get_global_var('func_2327')
var_3975 = relay.var("var_3975", dtype = "float32", shape = (880,))#candidate|3975|(880,)|var|float32
call_3974 = relay.TupleGetItem(func_2323_call(relay.reshape(call_3972.astype('float64'), [14, 8, 4]), relay.reshape(var_3975.astype('float32'), [880,]), ), 4)
call_3976 = relay.TupleGetItem(func_2327_call(relay.reshape(call_3972.astype('float64'), [14, 8, 4]), relay.reshape(var_3975.astype('float32'), [880,]), ), 4)
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_3977 = relay.TupleGetItem(func_2968_call(), 1)
call_3978 = relay.TupleGetItem(func_2969_call(), 1)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_3979 = relay.TupleGetItem(func_235_call(), 2)
call_3980 = relay.TupleGetItem(func_237_call(), 2)
output = relay.Tuple([uop_3964,call_3972,call_3974,var_3975,call_3977,call_3979,])
output2 = relay.Tuple([uop_3966,call_3973,call_3976,var_3975,call_3978,call_3980,])
func_3997 = relay.Function([var_3975,], output)
mod['func_3997'] = func_3997
mod = relay.transform.InferType()(mod)
mutated_mod['func_3997'] = func_3997
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3998 = relay.var("var_3998", dtype = "float32", shape = (880,))#candidate|3998|(880,)|var|float32
func_3997_call = mutated_mod.get_global_var('func_3997')
call_3999 = func_3997_call(var_3998)
output = call_3999
func_4000 = relay.Function([var_3998], output)
mutated_mod['func_4000'] = func_4000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3915_call = mod.get_global_var('func_3915')
func_3916_call = mutated_mod.get_global_var('func_3916')
call_4016 = relay.TupleGetItem(func_3915_call(), 2)
call_4017 = relay.TupleGetItem(func_3916_call(), 2)
func_3736_call = mod.get_global_var('func_3736')
func_3737_call = mutated_mod.get_global_var('func_3737')
call_4053 = func_3736_call()
call_4054 = func_3736_call()
output = relay.Tuple([call_4016,call_4053,])
output2 = relay.Tuple([call_4017,call_4054,])
func_4055 = relay.Function([], output)
mod['func_4055'] = func_4055
mod = relay.transform.InferType()(mod)
output = func_4055()
func_4056 = relay.Function([], output)
mutated_mod['func_4056'] = func_4056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4057 = relay.var("var_4057", dtype = "float64", shape = ())#candidate|4057|()|var|float64
var_4058 = relay.var("var_4058", dtype = "float64", shape = (10, 1, 5))#candidate|4058|(10, 1, 5)|var|float64
bop_4059 = relay.floor_mod(var_4057.astype('float64'), var_4058.astype('float64')) # shape=(10, 1, 5)
func_3403_call = mod.get_global_var('func_3403')
func_3405_call = mutated_mod.get_global_var('func_3405')
call_4062 = relay.TupleGetItem(func_3403_call(), 0)
call_4063 = relay.TupleGetItem(func_3405_call(), 0)
func_2816_call = mod.get_global_var('func_2816')
func_2820_call = mutated_mod.get_global_var('func_2820')
const_4068 = relay.const([[7.166465,3.813558,3.132256,9.488028,-9.807732,8.292869,-6.450546,7.413537,1.613420,5.370154,3.296948,-3.053483,-5.268375,0.458422,5.895184,8.467252,-0.801575,-0.032946,3.717116,1.396706,1.640832,-6.457246,-1.151348,-2.387347,2.089952,6.231592,4.820901,-5.470836,3.283699,-6.191956,-0.039438,4.667809,-7.269989,-0.521251,3.580116,6.544185,-9.668406,8.646881,8.742797,-0.060022,5.944575,2.146900],[-1.015212,-5.897390,0.117020,-5.310923,1.367965,0.680883,2.676548,2.748438,8.588260,5.645354,-5.867298,-2.876565,3.355332,-9.121272,-0.042539,7.342286,-7.391268,-1.000421,-7.034911,2.570245,-6.330846,3.402862,-1.689409,-9.437878,-7.396814,-3.407016,-2.276507,-5.663427,0.970209,-2.469462,3.202320,-0.292357,-4.461572,9.124948,-4.146638,-3.030238,7.579596,-0.470851,-1.582549,7.556325,2.352161,8.741482],[-0.211148,8.042299,2.656426,7.738501,8.541638,-9.360761,-5.334933,-8.715565,-9.033502,1.258381,-5.895788,7.737694,5.206982,8.919773,-1.857841,-0.704164,2.776119,4.172057,-5.568291,5.755599,-5.866369,5.607322,8.838722,1.873263,-5.217034,-6.490527,8.933406,1.039072,-9.671421,0.022981,8.729668,-5.079787,2.691963,6.315926,-6.125517,2.260847,-2.517364,-2.035941,-3.648589,6.399192,-3.485453,6.417182],[-0.189293,-3.680258,-1.375953,3.201191,-3.066995,-8.279122,2.924570,2.130726,-6.754589,2.283747,3.978075,-7.835375,7.310218,-3.219458,9.439182,6.768363,-2.260969,2.828512,3.560756,-5.511541,-7.681534,8.588669,2.100150,5.721552,4.193351,-3.024125,-8.856038,-3.254129,2.360104,-4.779894,5.788019,-1.200183,4.956753,-9.588582,-7.261977,-7.428149,3.847985,2.152367,-1.425381,-5.119877,0.072354,-9.704146],[6.713138,8.268677,5.427861,-7.173824,-7.458661,-9.945427,-1.414046,-3.372236,-1.447003,6.945215,6.778252,-1.714060,7.707335,0.903170,5.274694,4.255035,9.253767,6.362862,-6.960732,4.398519,-8.399134,-4.110725,-2.633823,-0.501826,-2.862713,-2.087393,-4.084968,5.851074,9.341874,-8.671941,4.975840,6.949737,-7.333778,1.777586,-7.880395,4.242207,2.850292,4.020665,7.124825,-3.359562,6.536363,7.682320],[1.643742,-8.643317,3.834078,1.199185,-1.041925,1.322750,-1.484612,0.887303,3.517793,4.112430,-5.529419,-4.348822,-9.467684,2.981408,1.885136,0.103544,-4.207104,9.242271,-5.485393,-8.362162,-0.295793,-8.334856,-4.938312,0.199184,-4.470554,-3.969154,-7.209786,-9.767417,2.859205,-1.975428,-4.817932,8.010646,0.992559,4.327342,-2.468375,-8.484233,3.934433,1.417632,-3.245486,-8.990185,6.811096,-7.863030],[5.160961,9.242819,-8.977118,-0.580944,8.235584,3.421531,-9.852315,6.443241,-6.963247,7.641141,-6.462055,-4.322109,-2.922986,8.552788,6.199304,5.964311,8.051516,-3.812936,-3.292358,-9.870921,-2.822473,9.405788,-1.613801,6.018068,-0.540761,1.114355,2.591461,-4.756012,-7.513064,-0.299839,7.489993,-7.660932,-5.942552,-8.492142,9.437330,-6.685386,0.492259,3.133139,-8.538220,-9.931083,7.393307,2.125648],[0.789831,-5.046887,-8.371194,-3.818744,-0.785750,-2.142754,8.876547,-7.850296,7.732285,-4.631808,-5.428382,4.793427,7.467121,2.295427,7.421559,2.100013,-2.089498,-5.472982,-4.250502,-1.467326,5.845557,7.865953,-0.020479,-9.016119,6.549696,-6.983206,-0.272727,-4.278162,4.517346,-6.203041,4.548544,-0.579343,-7.352542,-1.017743,0.332540,3.807412,9.215452,1.031177,-1.763002,8.250345,-6.596595,7.356662]], dtype = "float64")#candidate|4068|(8, 42)|const|float64
var_4069 = relay.var("var_4069", dtype = "float32", shape = (880, 1))#candidate|4069|(880, 1)|var|float32
call_4067 = relay.TupleGetItem(func_2816_call(relay.reshape(const_4068.astype('float64'), [8, 3, 14]), relay.reshape(const_4068.astype('float64'), [8, 3, 14]), relay.reshape(var_4069.astype('float32'), [880,]), ), 1)
call_4070 = relay.TupleGetItem(func_2820_call(relay.reshape(const_4068.astype('float64'), [8, 3, 14]), relay.reshape(const_4068.astype('float64'), [8, 3, 14]), relay.reshape(var_4069.astype('float32'), [880,]), ), 1)
func_3011_call = mod.get_global_var('func_3011')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_4074 = func_3011_call()
call_4075 = func_3011_call()
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_4076 = relay.TupleGetItem(func_235_call(), 2)
call_4077 = relay.TupleGetItem(func_237_call(), 2)
func_3915_call = mod.get_global_var('func_3915')
func_3916_call = mutated_mod.get_global_var('func_3916')
call_4084 = relay.TupleGetItem(func_3915_call(), 1)
call_4085 = relay.TupleGetItem(func_3916_call(), 1)
uop_4086 = relay.atanh(var_4058.astype('float64')) # shape=(10, 1, 5)
output = relay.Tuple([bop_4059,call_4062,call_4067,const_4068,var_4069,call_4074,call_4076,call_4084,uop_4086,])
output2 = relay.Tuple([bop_4059,call_4063,call_4070,const_4068,var_4069,call_4075,call_4077,call_4085,uop_4086,])
func_4089 = relay.Function([var_4057,var_4058,var_4069,], output)
mod['func_4089'] = func_4089
mod = relay.transform.InferType()(mod)
mutated_mod['func_4089'] = func_4089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4089_call = mutated_mod.get_global_var('func_4089')
var_4091 = relay.var("var_4091", dtype = "float64", shape = ())#candidate|4091|()|var|float64
var_4092 = relay.var("var_4092", dtype = "float64", shape = (10, 1, 5))#candidate|4092|(10, 1, 5)|var|float64
var_4093 = relay.var("var_4093", dtype = "float32", shape = (880, 1))#candidate|4093|(880, 1)|var|float32
call_4090 = func_4089_call(var_4091,var_4092,var_4093,)
output = call_4090
func_4094 = relay.Function([var_4091,var_4092,var_4093,], output)
mutated_mod['func_4094'] = func_4094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_4096 = func_1116_call()
call_4097 = func_1116_call()
func_3403_call = mod.get_global_var('func_3403')
func_3405_call = mutated_mod.get_global_var('func_3405')
call_4104 = relay.TupleGetItem(func_3403_call(), 0)
call_4105 = relay.TupleGetItem(func_3405_call(), 0)
output = relay.Tuple([call_4096,call_4104,])
output2 = relay.Tuple([call_4097,call_4105,])
func_4109 = relay.Function([], output)
mod['func_4109'] = func_4109
mod = relay.transform.InferType()(mod)
output = func_4109()
func_4110 = relay.Function([], output)
mutated_mod['func_4110'] = func_4110
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4199 = relay.var("var_4199", dtype = "int64", shape = (6, 13, 6))#candidate|4199|(6, 13, 6)|var|int64
var_4200 = relay.var("var_4200", dtype = "int64", shape = (6, 13, 6))#candidate|4200|(6, 13, 6)|var|int64
bop_4201 = relay.bitwise_and(var_4199.astype('int64'), relay.reshape(var_4200.astype('int64'), relay.shape_of(var_4199))) # shape=(6, 13, 6)
bop_4204 = relay.logical_or(var_4200.astype('bool'), relay.reshape(bop_4201.astype('bool'), relay.shape_of(var_4200))) # shape=(6, 13, 6)
uop_4210 = relay.atanh(var_4199.astype('float64')) # shape=(6, 13, 6)
bop_4214 = relay.left_shift(bop_4201.astype('int64'), relay.reshape(var_4200.astype('int64'), relay.shape_of(bop_4201))) # shape=(6, 13, 6)
func_2997_call = mod.get_global_var('func_2997')
func_2998_call = mutated_mod.get_global_var('func_2998')
call_4233 = relay.TupleGetItem(func_2997_call(), 0)
call_4234 = relay.TupleGetItem(func_2998_call(), 0)
var_4241 = relay.var("var_4241", dtype = "float64", shape = (6, 13, 6))#candidate|4241|(6, 13, 6)|var|float64
bop_4242 = relay.maximum(uop_4210.astype('int16'), relay.reshape(var_4241.astype('int16'), relay.shape_of(uop_4210))) # shape=(6, 13, 6)
func_1975_call = mod.get_global_var('func_1975')
func_1979_call = mutated_mod.get_global_var('func_1979')
var_4252 = relay.var("var_4252", dtype = "float32", shape = (84,))#candidate|4252|(84,)|var|float32
call_4251 = relay.TupleGetItem(func_1975_call(relay.reshape(var_4252.astype('float32'), [14, 2, 3]), relay.reshape(var_4252.astype('float32'), [14, 2, 3]), ), 3)
call_4253 = relay.TupleGetItem(func_1979_call(relay.reshape(var_4252.astype('float32'), [14, 2, 3]), relay.reshape(var_4252.astype('float32'), [14, 2, 3]), ), 3)
func_2856_call = mod.get_global_var('func_2856')
func_2859_call = mutated_mod.get_global_var('func_2859')
var_4265 = relay.var("var_4265", dtype = "float32", shape = (294,))#candidate|4265|(294,)|var|float32
call_4264 = relay.TupleGetItem(func_2856_call(relay.reshape(var_4265.astype('float32'), [7, 42])), 2)
call_4266 = relay.TupleGetItem(func_2859_call(relay.reshape(var_4265.astype('float32'), [7, 42])), 2)
bop_4267 = relay.less(bop_4242.astype('bool'), relay.reshape(uop_4210.astype('bool'), relay.shape_of(bop_4242))) # shape=(6, 13, 6)
func_4109_call = mod.get_global_var('func_4109')
func_4110_call = mutated_mod.get_global_var('func_4110')
call_4277 = relay.TupleGetItem(func_4109_call(), 1)
call_4278 = relay.TupleGetItem(func_4110_call(), 1)
uop_4282 = relay.cos(bop_4242.astype('float64')) # shape=(6, 13, 6)
output = relay.Tuple([bop_4204,bop_4214,call_4233,call_4251,var_4252,call_4264,var_4265,bop_4267,call_4277,uop_4282,])
output2 = relay.Tuple([bop_4204,bop_4214,call_4234,call_4253,var_4252,call_4266,var_4265,bop_4267,call_4278,uop_4282,])
func_4284 = relay.Function([var_4199,var_4200,var_4241,var_4252,var_4265,], output)
mod['func_4284'] = func_4284
mod = relay.transform.InferType()(mod)
var_4285 = relay.var("var_4285", dtype = "int64", shape = (6, 13, 6))#candidate|4285|(6, 13, 6)|var|int64
var_4286 = relay.var("var_4286", dtype = "int64", shape = (6, 13, 6))#candidate|4286|(6, 13, 6)|var|int64
var_4287 = relay.var("var_4287", dtype = "float64", shape = (6, 13, 6))#candidate|4287|(6, 13, 6)|var|float64
var_4288 = relay.var("var_4288", dtype = "float32", shape = (84,))#candidate|4288|(84,)|var|float32
var_4289 = relay.var("var_4289", dtype = "float32", shape = (294,))#candidate|4289|(294,)|var|float32
output = func_4284(var_4285,var_4286,var_4287,var_4288,var_4289,)
func_4290 = relay.Function([var_4285,var_4286,var_4287,var_4288,var_4289,], output)
mutated_mod['func_4290'] = func_4290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_807_call = mod.get_global_var('func_807')
func_809_call = mutated_mod.get_global_var('func_809')
call_4371 = relay.TupleGetItem(func_807_call(), 4)
call_4372 = relay.TupleGetItem(func_809_call(), 4)
output = call_4371
output2 = call_4372
func_4378 = relay.Function([], output)
mod['func_4378'] = func_4378
mod = relay.transform.InferType()(mod)
output = func_4378()
func_4379 = relay.Function([], output)
mutated_mod['func_4379'] = func_4379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_4402 = func_1116_call()
call_4403 = func_1116_call()
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_4430 = relay.TupleGetItem(func_735_call(), 1)
call_4431 = relay.TupleGetItem(func_737_call(), 1)
func_3502_call = mod.get_global_var('func_3502')
func_3504_call = mutated_mod.get_global_var('func_3504')
call_4494 = func_3502_call()
call_4495 = func_3502_call()
output = relay.Tuple([call_4402,call_4430,call_4494,])
output2 = relay.Tuple([call_4403,call_4431,call_4495,])
func_4501 = relay.Function([], output)
mod['func_4501'] = func_4501
mod = relay.transform.InferType()(mod)
output = func_4501()
func_4502 = relay.Function([], output)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_4600 = relay.TupleGetItem(func_1474_call(), 0)
call_4601 = relay.TupleGetItem(func_1476_call(), 0)
output = relay.Tuple([call_4600,])
output2 = relay.Tuple([call_4601,])
func_4604 = relay.Function([], output)
mod['func_4604'] = func_4604
mod = relay.transform.InferType()(mod)
output = func_4604()
func_4605 = relay.Function([], output)
mutated_mod['func_4605'] = func_4605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_4642 = func_1240_call()
call_4643 = func_1240_call()
output = relay.Tuple([call_4642,])
output2 = relay.Tuple([call_4643,])
func_4645 = relay.Function([], output)
mod['func_4645'] = func_4645
mod = relay.transform.InferType()(mod)
output = func_4645()
func_4646 = relay.Function([], output)
mutated_mod['func_4646'] = func_4646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3309_call = mod.get_global_var('func_3309')
func_3310_call = mutated_mod.get_global_var('func_3310')
call_4661 = relay.TupleGetItem(func_3309_call(), 0)
call_4662 = relay.TupleGetItem(func_3310_call(), 0)
output = relay.Tuple([call_4661,])
output2 = relay.Tuple([call_4662,])
func_4667 = relay.Function([], output)
mod['func_4667'] = func_4667
mod = relay.transform.InferType()(mod)
output = func_4667()
func_4668 = relay.Function([], output)
mutated_mod['func_4668'] = func_4668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_4768 = relay.TupleGetItem(func_1699_call(), 5)
call_4769 = relay.TupleGetItem(func_1700_call(), 5)
output = relay.Tuple([call_4768,])
output2 = relay.Tuple([call_4769,])
func_4781 = relay.Function([], output)
mod['func_4781'] = func_4781
mod = relay.transform.InferType()(mod)
mutated_mod['func_4781'] = func_4781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4781_call = mutated_mod.get_global_var('func_4781')
call_4782 = func_4781_call()
output = call_4782
func_4783 = relay.Function([], output)
mutated_mod['func_4783'] = func_4783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4645_call = mod.get_global_var('func_4645')
func_4646_call = mutated_mod.get_global_var('func_4646')
call_4798 = relay.TupleGetItem(func_4645_call(), 0)
call_4799 = relay.TupleGetItem(func_4646_call(), 0)
func_873_call = mod.get_global_var('func_873')
func_876_call = mutated_mod.get_global_var('func_876')
const_4818 = relay.const([-9.712103,-1.629516,-0.228324,2.225638,-4.226071,2.898886,-7.365340,2.364928,-6.673975,7.926107,4.724473,-5.994453,-4.297942,-6.501002,-3.825182,-5.455565,-8.651293,-0.393961,6.433706,-8.098220,8.060665,6.028810,6.559258,-9.722202,-9.808170,-6.552778,-3.554172,1.776125,-5.314655,-0.046133,1.566818,2.506595,9.969586,-6.825381,-0.611998,1.847761,0.507767,4.853212,0.117835,-6.106127,8.727558,-0.143124,0.208498,-5.887952,8.402674,5.710759,4.048134,0.961037,-7.431414,-9.703105,-8.362647,-3.964614,-8.276791,-6.790812,1.025716,-3.207924,-3.357040,8.006581,-2.116332,0.892141,-4.600154,-6.741809,8.510284,0.912549,-6.200754,-5.995496,4.822309,-7.811601,8.518555,1.358306,9.172500,2.413025,-5.045674,-1.672944,5.345148,5.646031,-6.167616,3.648266,9.415648,2.240011,-9.764588,-9.099763,-1.154583,-9.951457,2.407538,4.057633,2.043392,-4.582343,1.413529,-5.634530,-2.704674,-2.969281,-7.864963,2.029341,-1.035378,4.996458,-3.776782,-9.201924,-4.021800,-8.169471,9.161948,-2.956370,3.790591,-6.992186,6.596319,5.041035,-6.890224,-6.284016,2.421227,-4.660625,-3.820016,3.528194,5.882277,-8.293246,-1.467189,-0.886764,-3.279674,-2.488304,5.665724,-8.265650,0.726424,7.328136,0.983018,-4.447111,8.126983,3.126071,-0.298062,-7.054483,-0.540655,7.232406,-8.349392,-9.919605,2.785011,-0.705555,-9.407176,9.632098,-0.761372,5.788347,3.721166,-0.109442,4.296064,-9.013198,-9.022276,2.651885,4.424150,8.358266,-8.784318,-8.786903,-3.820986,3.288750,9.576370,1.963472,7.034593,-8.111829,-9.439242,0.877015,-5.603322,-9.047562,-2.238968,0.907655,-6.646631,4.070404,7.539688,-7.448341,-9.543645,-0.647958,5.528913,2.363478,-5.234571,2.414491,6.282842,-6.674309,-8.102681,-4.893360,7.854703,8.487235,0.791975,-9.598528,-1.912612,-4.745944,-8.544818,9.167837,-8.606552,-4.831528,-4.483298,-7.898935,-2.184280,7.439432,6.814894,-4.180617,6.969666,-0.507848,-6.988508,5.928939,-3.633605,-9.774878,-3.324259,-1.810658,-7.926594,-4.709075,-9.221033,-3.626497,4.968188,5.325154,-5.205162,7.466574,9.513748,-0.770884,5.664217,7.684442,2.812833,-3.974940,1.620150,7.965450,-6.342825,-0.676050,-4.811323,7.119697,-4.479777,-5.520270,-2.129546,-6.109856,3.445711,-5.200258,8.117381,-1.102507,1.018945,-0.862974,7.526110,-7.341553,1.661990,-4.115434,-1.395982,-7.604616,3.357241,1.529830,-5.600179,0.455864,-1.581095,-9.126850], dtype = "float64")#candidate|4818|(240,)|const|float64
call_4817 = relay.TupleGetItem(func_873_call(relay.reshape(const_4818.astype('float64'), [12, 5, 4]), relay.reshape(const_4818.astype('float64'), [12, 5, 4]), ), 4)
call_4819 = relay.TupleGetItem(func_876_call(relay.reshape(const_4818.astype('float64'), [12, 5, 4]), relay.reshape(const_4818.astype('float64'), [12, 5, 4]), ), 4)
func_4667_call = mod.get_global_var('func_4667')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_4838 = relay.TupleGetItem(func_4667_call(), 0)
call_4839 = relay.TupleGetItem(func_4668_call(), 0)
output = relay.Tuple([call_4798,call_4817,const_4818,call_4838,])
output2 = relay.Tuple([call_4799,call_4819,const_4818,call_4839,])
func_4886 = relay.Function([], output)
mod['func_4886'] = func_4886
mod = relay.transform.InferType()(mod)
mutated_mod['func_4886'] = func_4886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mutated_mod.get_global_var('func_4886')
call_4887 = func_4886_call()
output = call_4887
func_4888 = relay.Function([], output)
mutated_mod['func_4888'] = func_4888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4667_call = mod.get_global_var('func_4667')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_5024 = relay.TupleGetItem(func_4667_call(), 0)
call_5025 = relay.TupleGetItem(func_4668_call(), 0)
func_2149_call = mod.get_global_var('func_2149')
func_2152_call = mutated_mod.get_global_var('func_2152')
var_5036 = relay.var("var_5036", dtype = "float64", shape = (240,))#candidate|5036|(240,)|var|float64
call_5035 = relay.TupleGetItem(func_2149_call(relay.reshape(var_5036.astype('float64'), [240,])), 3)
call_5037 = relay.TupleGetItem(func_2152_call(relay.reshape(var_5036.astype('float64'), [240,])), 3)
uop_5038 = relay.sqrt(call_5024.astype('float64')) # shape=(14, 8, 4)
uop_5040 = relay.sqrt(call_5025.astype('float64')) # shape=(14, 8, 4)
output = relay.Tuple([call_5035,var_5036,uop_5038,])
output2 = relay.Tuple([call_5037,var_5036,uop_5040,])
func_5047 = relay.Function([var_5036,], output)
mod['func_5047'] = func_5047
mod = relay.transform.InferType()(mod)
mutated_mod['func_5047'] = func_5047
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5048 = relay.var("var_5048", dtype = "float64", shape = (240,))#candidate|5048|(240,)|var|float64
func_5047_call = mutated_mod.get_global_var('func_5047')
call_5049 = func_5047_call(var_5048)
output = call_5049
func_5050 = relay.Function([var_5048], output)
mutated_mod['func_5050'] = func_5050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3705_call = mutated_mod.get_global_var('func_3705')
call_5088 = relay.TupleGetItem(func_3703_call(), 0)
call_5089 = relay.TupleGetItem(func_3705_call(), 0)
output = call_5088
output2 = call_5089
func_5092 = relay.Function([], output)
mod['func_5092'] = func_5092
mod = relay.transform.InferType()(mod)
output = func_5092()
func_5093 = relay.Function([], output)
mutated_mod['func_5093'] = func_5093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mod.get_global_var('func_4604')
func_4605_call = mutated_mod.get_global_var('func_4605')
call_5169 = relay.TupleGetItem(func_4604_call(), 0)
call_5170 = relay.TupleGetItem(func_4605_call(), 0)
output = call_5169
output2 = call_5170
func_5204 = relay.Function([], output)
mod['func_5204'] = func_5204
mod = relay.transform.InferType()(mod)
output = func_5204()
func_5205 = relay.Function([], output)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4109_call = mod.get_global_var('func_4109')
func_4110_call = mutated_mod.get_global_var('func_4110')
call_5289 = relay.TupleGetItem(func_4109_call(), 1)
call_5290 = relay.TupleGetItem(func_4110_call(), 1)
output = call_5289
output2 = call_5290
func_5291 = relay.Function([], output)
mod['func_5291'] = func_5291
mod = relay.transform.InferType()(mod)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5291_call = mutated_mod.get_global_var('func_5291')
call_5292 = func_5291_call()
output = call_5292
func_5293 = relay.Function([], output)
mutated_mod['func_5293'] = func_5293
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5308 = relay.const(-7, dtype = "uint32")#candidate|5308|()|const|uint32
var_5309 = relay.var("var_5309", dtype = "uint32", shape = (1, 9, 2))#candidate|5309|(1, 9, 2)|var|uint32
bop_5310 = relay.logical_xor(const_5308.astype('uint32'), var_5309.astype('uint32')) # shape=(1, 9, 2)
uop_5317 = relay.acos(bop_5310.astype('float32')) # shape=(1, 9, 2)
func_3233_call = mod.get_global_var('func_3233')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_5320 = relay.TupleGetItem(func_3233_call(), 1)
call_5321 = relay.TupleGetItem(func_3235_call(), 1)
output = relay.Tuple([uop_5317,call_5320,])
output2 = relay.Tuple([uop_5317,call_5321,])
func_5331 = relay.Function([var_5309,], output)
mod['func_5331'] = func_5331
mod = relay.transform.InferType()(mod)
var_5332 = relay.var("var_5332", dtype = "uint32", shape = (1, 9, 2))#candidate|5332|(1, 9, 2)|var|uint32
output = func_5331(var_5332)
func_5333 = relay.Function([var_5332], output)
mutated_mod['func_5333'] = func_5333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3233_call = mod.get_global_var('func_3233')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_5351 = relay.TupleGetItem(func_3233_call(), 0)
call_5352 = relay.TupleGetItem(func_3235_call(), 0)
func_5331_call = mod.get_global_var('func_5331')
func_5333_call = mutated_mod.get_global_var('func_5333')
var_5360 = relay.var("var_5360", dtype = "uint32", shape = (18,))#candidate|5360|(18,)|var|uint32
call_5359 = relay.TupleGetItem(func_5331_call(relay.reshape(var_5360.astype('uint32'), [1, 9, 2])), 1)
call_5361 = relay.TupleGetItem(func_5333_call(relay.reshape(var_5360.astype('uint32'), [1, 9, 2])), 1)
output = relay.Tuple([call_5351,call_5359,var_5360,])
output2 = relay.Tuple([call_5352,call_5361,var_5360,])
func_5370 = relay.Function([var_5360,], output)
mod['func_5370'] = func_5370
mod = relay.transform.InferType()(mod)
mutated_mod['func_5370'] = func_5370
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5371 = relay.var("var_5371", dtype = "uint32", shape = (18,))#candidate|5371|(18,)|var|uint32
func_5370_call = mutated_mod.get_global_var('func_5370')
call_5372 = func_5370_call(var_5371)
output = call_5372
func_5373 = relay.Function([var_5371], output)
mutated_mod['func_5373'] = func_5373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4501_call = mod.get_global_var('func_4501')
func_4502_call = mutated_mod.get_global_var('func_4502')
call_5396 = relay.TupleGetItem(func_4501_call(), 0)
call_5397 = relay.TupleGetItem(func_4502_call(), 0)
output = call_5396
output2 = call_5397
func_5436 = relay.Function([], output)
mod['func_5436'] = func_5436
mod = relay.transform.InferType()(mod)
output = func_5436()
func_5437 = relay.Function([], output)
mutated_mod['func_5437'] = func_5437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1757_call = mod.get_global_var('func_1757')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_5441 = func_1757_call()
call_5442 = func_1757_call()
func_3648_call = mod.get_global_var('func_3648')
func_3651_call = mutated_mod.get_global_var('func_3651')
var_5447 = relay.var("var_5447", dtype = "float64", shape = (130,))#candidate|5447|(130,)|var|float64
call_5446 = relay.TupleGetItem(func_3648_call(relay.reshape(var_5447.astype('float64'), [10, 13, 1])), 1)
call_5448 = relay.TupleGetItem(func_3651_call(relay.reshape(var_5447.astype('float64'), [10, 13, 1])), 1)
output = relay.Tuple([call_5441,call_5446,var_5447,])
output2 = relay.Tuple([call_5442,call_5448,var_5447,])
func_5455 = relay.Function([var_5447,], output)
mod['func_5455'] = func_5455
mod = relay.transform.InferType()(mod)
var_5456 = relay.var("var_5456", dtype = "float64", shape = (130,))#candidate|5456|(130,)|var|float64
output = func_5455(var_5456)
func_5457 = relay.Function([var_5456], output)
mutated_mod['func_5457'] = func_5457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_5496 = relay.TupleGetItem(func_1072_call(), 1)
call_5497 = relay.TupleGetItem(func_1073_call(), 1)
func_1464_call = mod.get_global_var('func_1464')
func_1465_call = mutated_mod.get_global_var('func_1465')
call_5512 = func_1464_call()
call_5513 = func_1464_call()
func_1474_call = mod.get_global_var('func_1474')
func_1476_call = mutated_mod.get_global_var('func_1476')
call_5523 = relay.TupleGetItem(func_1474_call(), 0)
call_5524 = relay.TupleGetItem(func_1476_call(), 0)
func_3091_call = mod.get_global_var('func_3091')
func_3094_call = mutated_mod.get_global_var('func_3094')
var_5558 = relay.var("var_5558", dtype = "int8", shape = ())#candidate|5558|()|var|int8
call_5557 = relay.TupleGetItem(func_3091_call(relay.reshape(var_5558.astype('int8'), [])), 0)
call_5559 = relay.TupleGetItem(func_3094_call(relay.reshape(var_5558.astype('int8'), [])), 0)
func_2816_call = mod.get_global_var('func_2816')
func_2820_call = mutated_mod.get_global_var('func_2820')
const_5561 = relay.const([-8.963823,5.349128,-7.054134,-9.566899,-6.114570,5.655469,-2.721427,-6.525899,-1.606685,-3.824228,2.933247,9.846679,1.662347,3.923873,9.350415,4.856480,-5.599355,-8.215279,-4.299167,-0.630421,-0.494649,-3.898317,-3.291056,-8.267149,7.941879,-1.930404,-2.313590,9.038011,7.883956,-7.849165,-8.237535,-7.296162,2.712280,-4.504788,-5.699864,-5.937133,-8.832021,0.940839,5.436991,9.397950,-4.106089,-6.584736,8.560263,5.026175,-4.841139,3.721995,0.346396,-2.091569,-2.837153,-8.636973,9.012949,-6.880349,-4.494906,-3.913831,1.967612,-4.068330,8.757176,9.602369,-3.254694,0.052233,-8.814137,-1.248358,2.404154,-3.101345,7.008707,-7.460280,-2.708807,-0.119090,-8.400801,-4.461095,-6.211759,6.842281,3.354970,9.889067,6.696454,0.124492,2.855512,-0.986464,-1.234287,0.186285,5.692609,-7.686011,-7.436655,-6.584426,5.908409,-9.439319,5.681078,-1.380533,-3.273362,1.674887,-3.969611,-5.902761,-6.087593,-3.950387,0.836919,-6.920058,3.637278,-2.078718,5.435268,-6.602203,-9.429481,-0.535042,7.569924,-3.736195,-3.452233,2.682202,-2.111511,1.290506,-6.118859,9.248948,7.722273,4.138913,-3.068258,-1.863728,-9.518672,7.353115,2.319315,1.511533,-6.476372,7.803274,6.760972,5.563501,-2.339905,-3.845853,2.681238,-3.022030,5.781871,3.174961,-4.582133,8.021789,8.603790,3.099946,-9.086016,4.864801,-4.571355,-1.024556,8.163841,-0.983049,-0.578558,0.396869,-5.931118,-2.633684,8.103338,-0.893537,3.516218,-4.713153,-1.464011,3.812381,-4.088069,4.420111,2.051417,-2.606563,7.244595,-6.200780,5.424380,8.766151,-6.605142,5.630414,-1.942095,0.659539,3.739938,-9.742273,8.958800,0.614634,-8.940211,-4.367784,-7.771781,-2.519888,2.925753,4.000771,-9.498986,7.621218,-9.904699,-8.053032,-2.539432,-6.549513,-6.890160,1.672438,-0.760707,3.723150,1.974823,9.825644,5.840488,5.076183,-5.629406,0.030372,-5.965130,1.769456,-5.299258,4.185515,0.729163,-9.174486,-4.977006,1.850211,-7.830048,2.941665,0.247193,5.934003,-6.108236,7.847682,5.018032,-4.917465,1.268081,-8.129392,0.643284,-4.864635,0.749715,-8.194374,-2.656934,8.938351,0.640672,-5.112788,7.596401,8.488486,8.470722,-9.363431,9.199037,-8.841807,7.955651,-5.375199,-5.914150,6.611054,-0.500392,4.862796,-9.805131,6.448069,8.774617,-1.428201,-4.750032,-2.338880,-8.572287,-9.107623,4.828464,9.738789,-8.169919,-4.051596,-9.127241,-7.785912,2.167318,-0.714438,-3.421807,9.033469,2.842493,-6.279783,0.297497,2.633271,-4.381084,-1.469240,-6.072017,-6.127987,1.073341,6.272605,-7.761695,-3.695440,6.706161,7.054391,5.067541,8.179299,-1.370260,-5.723729,3.092632,-5.336400,2.508350,3.436870,-8.163809,-1.985381,-1.792165,1.019380,-4.380450,9.750156,-2.305591,5.021341,5.045797,3.561142,0.204524,-4.063214,7.011296,-9.243349,3.129940,0.803637,7.621316,7.161014,7.221640,-1.276575,0.914142,-8.799653,4.282639,2.522430,-8.609023,-1.367331,-5.474616,-4.377825,7.757575,-1.947060,9.147379,-9.426595,-2.453038,-8.954739,2.716987,6.630369,-3.455758,-6.972795,9.034630,3.747165,-0.421001,1.604539,-4.688124,3.822879,-9.363319,-0.796645,0.227576,-6.677117,-2.630132,3.754510,-4.241910,-6.596127,-5.757224,-1.535210,-8.907078,-9.134231,6.939059,5.370171,1.725535,-8.970530,1.717348,3.875214,7.274443,-4.921295,9.936583,6.414935,-7.521885,-0.049032,1.807437,-1.617798,-9.707677,-5.455618], dtype = "float64")#candidate|5561|(336,)|const|float64
const_5562 = relay.const([-0.896360,-4.853572,-2.252207,-9.711597,-0.895481,8.086629,7.968778,8.372776,-6.994073,-4.294409,4.788245,2.855838,-4.948581,3.215377,-5.262732,7.054449,6.684523,-3.363949,-9.579052,-3.629859,-3.693363,-6.172337,7.984013,-4.513472,-6.869765,2.271329,5.984788,-5.967887,8.344654,-4.647595,0.390370,-2.194839,6.382587,2.627196,8.979058,-3.420887,9.952892,5.894320,8.829647,-6.736611,-5.500113,5.704308,4.064357,-8.933951,5.868137,-8.171291,-7.106920,-7.987897,6.212529,6.784774,2.777253,3.627175,8.932894,-6.476486,-0.414718,-8.589609,-7.187073,-7.774014,7.040459,-7.638660,0.564870,-5.877758,1.756458,-3.402185,-3.673765,-4.424004,2.572781,-9.000566,-8.228175,8.081367,0.254592,-8.695310,9.084536,3.493832,5.473277,-5.529030,-1.085466,-3.789422,0.362971,4.160815,1.728116,6.356498,1.295480,9.381898,-4.179002,-5.983328,-2.031697,5.687206,4.141728,4.904143,-7.350971,-0.784499,-3.441530,7.310511,4.720768,3.898591,-8.593112,1.427865,-5.678234,2.522300,-9.731928,-1.799165,-3.346052,-5.451579,1.048712,-0.505548,8.625840,-5.683439,-7.650574,5.352056,-8.969515,-4.658231,-1.131266,-7.720138,-3.364833,2.272115,1.092482,4.632888,-5.426202,-9.679651,3.370475,8.456569,3.379593,-9.131654,6.003337,3.861544,-1.621518,-8.153573,2.725059,2.662687,3.960021,-4.064906,5.480951,-7.471688,-4.086455,4.140660,-6.008517,-7.686700,-9.088142,0.760633,1.778449,-3.792556,-0.336152,-7.996808,9.625740,1.344901,-1.253480,-7.651407,4.003459,2.028643,9.855371,-1.342350,-8.777553,0.884548,3.684227,-2.503283,1.128869,2.688320,-7.459247,5.918919,0.660133,-2.440235,2.285029,1.507130,2.784243,-3.130195,3.414748,-1.498626,3.463221,4.928810,-4.746456,4.232492,-4.892692,8.496271,-8.424207,-7.002891,0.583741,-8.375933,2.293911,-6.761869,-7.226271,5.284497,8.896947,3.602014,7.970551,6.491517,1.513174,8.206114,9.430529,-7.216893,-6.610170,-2.408244,7.721978,-6.739239,-4.842951,1.559320,1.505694,5.960796,4.432601,6.072995,9.836946,-0.624878,-1.308401,-7.059335,5.898575,8.378909,7.931298,1.559906,-7.214936,-5.442918,-8.829637,-4.319068,-9.733698,-5.036111,-2.890532,3.807477,7.462733,-5.284032,7.350370,4.662924,1.958873,-6.883546,-1.162986,3.083983,0.175047,-1.426611,-6.568563,7.688134,-2.867021,-5.049321,-8.155279,-2.582521,6.730999,3.254938,9.489658,6.706879,6.917639,7.420488,-8.863904,5.999319,-3.961923,6.723705,-9.157807,-2.421250,8.142900,4.799584,-4.219191,9.985785,5.745817,-0.129754,7.686717,1.232418,-1.298025,2.186921,-6.818049,-1.262930,-0.943669,5.752764,5.947597,2.341521,-3.863574,-8.877433,-9.789241,-4.864393,-1.516960,-7.972264,9.510601,-8.074555,-1.562219,-4.963432,-6.516117,-6.892612,-6.883960,4.006352,7.774758,-0.610679,-9.048968,-8.483240,-1.353016,-9.758024,1.197303,2.087197,-5.023591,-2.307088,1.083804,1.273101,-0.357047,-5.598970,1.339321,-3.873620,-9.411015,-6.813735,3.240421,2.311516,-9.666974,-5.171847,-3.429755,-3.642005,7.286544,4.134931,8.612240,5.190333,-7.245346,-2.901861,4.184279,-8.365576,-1.958469,-7.430642,0.566612,0.446017,8.217983,-1.759471,8.492263,9.593091,2.910927,7.540067,0.477273,-2.567908,-4.927184,-3.644038,9.928310,7.293372,6.175872,6.166752,9.924058,-8.482593,-7.015604,-2.719466,0.102484,8.985442,4.843398,4.765932,9.562707,-7.759812,2.617873,8.837077,-2.628592,-3.459501,1.933478,-2.538224,-1.877344,2.334556,9.730719,9.458934,3.109679,-5.350038,7.811471,-2.877756,2.539631,9.673187,4.350166,-5.983381,3.785649,1.045689,-6.087888,-5.139726,5.805443,-2.801842,1.431038,3.055840,-2.469559,4.475683,-8.213489,-3.986224,8.137889,-2.446237,-2.770814,-7.179276,3.343907,-7.939047,3.104152,-9.368680,5.307967,-9.624703,-5.437554,4.269349,4.604309,3.567679,-0.974303,3.759709,3.550169,-5.501509,-1.701920,7.785121,4.758679,-6.484243,-6.538869,9.863879,0.291272,4.239157,8.032844,-8.088798,3.484618,-1.754392,6.158621,2.929791,6.885777,-6.299023,-0.483877,7.525375,-9.427247,5.452748,5.877779,-7.069601,-6.863272,-9.505724,-2.245417,-8.297876,-9.838004,-5.788674,-0.374869,-4.609718,0.864513,-3.196921,7.317861,9.658048,8.629332,-7.434268,7.304257,0.577656,-7.521508,-9.261891,-9.090859,0.153439,7.948874,-4.859904,5.288630,-1.425114,4.006579,5.148679,-2.519597,-1.374000,4.896860,-8.746416,4.125055,-0.692777,-3.901966,1.199938,4.549624,8.474784,-1.259576,-6.621433,0.865139,-9.363361,8.069617,3.512755,9.844723,6.808668,-1.504480,5.242640,7.032849,-4.217915,-0.722871,-8.568654,-9.450007,6.905857,7.834934,-5.322670,-0.393461,-1.824456,-5.430257,4.986964,9.500929,-5.775300,7.080961,-8.627351,1.231108,-9.576644,-6.302802,8.143401,-4.196131,5.629062,9.676087,-6.447781,-5.374904,3.681247,-0.246911,-0.642292,-3.975791,-7.481720,7.036159,-0.641469,4.303866,-8.239337,-8.630760,-7.071270,-5.277847,-5.237545,8.413206,2.649369,9.766384,0.708091,-8.709015,-5.535142,-3.633198,-4.551128,4.369268,6.756443,8.578544,-9.516952,2.708578,-3.697394,-1.446170,0.846543,-5.749735,4.331793,-5.483759,6.401308,6.318380,0.381467,-0.213388,7.286279,-2.845879,-5.870567,-1.184243,1.842090,0.734199,-7.787463,0.766137,-9.709137,-9.346493,1.990213,-7.653116,0.818832,-9.538226,2.626895,-7.090705,-6.161048,4.167112,-2.710375,9.666463,-0.755168,-6.082069,-1.104796,-3.304344,1.855682,0.842994,8.068602,8.878205,2.307748,9.789348,7.717616,7.186081,4.297067,-1.837145,-5.467200,7.456876,3.916242,8.096773,8.363387,-6.659537,7.489084,-6.164927,4.198506,6.794451,8.670100,0.432289,4.148590,2.501143,-0.888652,-7.474615,1.254677,0.224856,0.199815,6.347786,-4.740670,0.088999,6.164953,5.743865,-4.262980,0.589339,3.280890,-4.513418,1.436721,8.811429,8.743142,-3.264536,-8.082295,9.298222,7.223445,-6.313456,-8.885157,9.399295,9.080654,-7.716949,5.074603,-0.092436,1.695868,3.887058,-0.633241,-5.645883,4.209045,-8.015306,-2.081631,0.082174,-2.951981,5.258193,-3.906430,-4.241011,5.955116,1.248009,-4.989172,-0.064161,-1.046567,-6.577791,-4.755676,-9.296412,-2.389394,5.109177,3.316325,-0.405823,5.526263,-7.997367,-5.016464,5.132369,-8.382691,-2.283502,-7.689709,-9.915786,1.983739,7.806211,3.635305,3.094433,5.132070,-8.948293,7.437577,-6.042548,-5.511170,-2.416504,-7.597360,0.689566,-7.484727,0.008206,-4.823471,1.056491,6.141781,8.210074,8.884303,-8.207937,-1.236012,1.299536,4.506818,-3.470333,-5.315838,-6.654125,-0.611036,0.480442,8.174397,-7.453068,-0.650649,1.342849,-8.073888,-6.059615,0.990426,-4.695764,5.021638,-9.746795,-8.923027,9.889939,3.290820,9.270447,8.673282,3.393844,0.584685,-0.883971,7.185684,8.353051,-5.440858,2.910525,-8.404017,2.278297,2.591139,-6.272820,-5.727771,4.106897,0.322398,-5.151755,2.582480,-1.699472,2.160708,2.818684,-2.995419,-7.360983,-9.907592,8.975136,-5.474629,1.929098,-9.650781,7.746862,5.307565,-0.590248,6.276513,0.841056,-9.953723,4.948303,-1.934369,1.595773,-6.965147,1.543494,2.797982,8.985563,-3.690231,-8.188734,2.561656,9.942000,-7.731258,3.779046,-0.638955,-2.470004,-9.574764,-6.834424,-7.035383,-2.103567,-8.515619,-7.521572,-6.025059,2.633553,-6.138581,3.492804,9.615304,-7.649871,-8.927531,1.879804,-2.630642,-1.494798,1.019522,5.570974,-8.438872,-6.122595,6.617739,-9.792572,1.967811,-7.169032,8.357029,1.362021,3.779015,-8.235541,0.773427,-8.431122,-2.710789,6.580984,-0.674941,2.094798,-0.780744,8.920837,-9.175869,1.050044,2.260027,1.291864,4.255451,4.207544,-3.133606,-4.005471,0.244908,6.774675,4.780676,8.870620,3.336388,-9.690308,3.036396,-2.184201,-3.136451,5.176896,8.258812,-8.043024,9.142691,7.886715,-7.764417,3.845616,8.250955,0.332060,1.337379,-9.022007,0.985343,-6.392323,-7.956577,6.617137,-9.451000,-8.300059,0.017579,-7.253062,-2.441312,8.245540,-4.823364,-1.016262,0.024405,-7.510350,-6.593911,-4.874255,-4.570995,-7.641015,5.797640,8.504876,-7.181356,8.780306,-4.925218,-1.923168,-4.603681,5.155926,2.787841,-0.290650,9.498338,4.709164,3.020678,-3.578111,9.245109,-6.479812,-6.382096,-0.642177,8.377747,-4.653858,-9.213166,-6.560009,-6.210643,2.872898,8.332695,0.754580,-8.132305,-4.197799,-7.963888,1.600346,-4.825751,-7.340760,0.682186,6.147705,-0.591217,5.282520,2.895921,8.764424,9.222483,9.431952,-7.432285,-3.671339,3.682125,-0.194992,9.784891,6.203737,9.572887,-7.918685,9.003171,2.254259,4.044617,-9.184374,-9.008781,9.689722,-3.301068,-3.905076,2.493945,0.015730,-8.056528,-0.255457,-9.830319,7.952058,4.163291,-6.702205,1.399324,-3.095518,-5.880160,6.670739,3.333328,9.180672,0.919027,-0.430794,-2.722652,-2.823433,-6.645523,-6.952093,-6.926501,-2.125271,2.916524,-7.767827,5.198084,5.380999,8.973443,-6.071025,2.659730,-8.780240,-7.761008,7.861877,9.335444], dtype = "float32")#candidate|5562|(880,)|const|float32
call_5560 = relay.TupleGetItem(func_2816_call(relay.reshape(const_5561.astype('float64'), [8, 3, 14]), relay.reshape(const_5561.astype('float64'), [8, 3, 14]), relay.reshape(const_5562.astype('float32'), [880,]), ), 3)
call_5563 = relay.TupleGetItem(func_2820_call(relay.reshape(const_5561.astype('float64'), [8, 3, 14]), relay.reshape(const_5561.astype('float64'), [8, 3, 14]), relay.reshape(const_5562.astype('float32'), [880,]), ), 3)
func_1357_call = mod.get_global_var('func_1357')
func_1358_call = mutated_mod.get_global_var('func_1358')
call_5567 = relay.TupleGetItem(func_1357_call(), 1)
call_5568 = relay.TupleGetItem(func_1358_call(), 1)
output = relay.Tuple([call_5496,call_5512,call_5523,call_5557,var_5558,call_5560,const_5561,const_5562,call_5567,])
output2 = relay.Tuple([call_5497,call_5513,call_5524,call_5559,var_5558,call_5563,const_5561,const_5562,call_5568,])
func_5589 = relay.Function([var_5558,], output)
mod['func_5589'] = func_5589
mod = relay.transform.InferType()(mod)
var_5590 = relay.var("var_5590", dtype = "int8", shape = ())#candidate|5590|()|var|int8
output = func_5589(var_5590)
func_5591 = relay.Function([var_5590], output)
mutated_mod['func_5591'] = func_5591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3233_call = mod.get_global_var('func_3233')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_5609 = relay.TupleGetItem(func_3233_call(), 0)
call_5610 = relay.TupleGetItem(func_3235_call(), 0)
output = call_5609
output2 = call_5610
func_5621 = relay.Function([], output)
mod['func_5621'] = func_5621
mod = relay.transform.InferType()(mod)
output = func_5621()
func_5622 = relay.Function([], output)
mutated_mod['func_5622'] = func_5622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3502_call = mod.get_global_var('func_3502')
func_3504_call = mutated_mod.get_global_var('func_3504')
call_5662 = func_3502_call()
call_5663 = func_3502_call()
output = relay.Tuple([call_5662,])
output2 = relay.Tuple([call_5663,])
func_5668 = relay.Function([], output)
mod['func_5668'] = func_5668
mod = relay.transform.InferType()(mod)
mutated_mod['func_5668'] = func_5668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5668_call = mutated_mod.get_global_var('func_5668')
call_5669 = func_5668_call()
output = call_5669
func_5670 = relay.Function([], output)
mutated_mod['func_5670'] = func_5670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_5693 = relay.TupleGetItem(func_108_call(), 0)
call_5694 = relay.TupleGetItem(func_110_call(), 0)
output = call_5693
output2 = call_5694
func_5705 = relay.Function([], output)
mod['func_5705'] = func_5705
mod = relay.transform.InferType()(mod)
output = func_5705()
func_5706 = relay.Function([], output)
mutated_mod['func_5706'] = func_5706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5436_call = mod.get_global_var('func_5436')
func_5437_call = mutated_mod.get_global_var('func_5437')
call_5807 = func_5436_call()
call_5808 = func_5436_call()
output = relay.Tuple([call_5807,])
output2 = relay.Tuple([call_5808,])
func_5810 = relay.Function([], output)
mod['func_5810'] = func_5810
mod = relay.transform.InferType()(mod)
mutated_mod['func_5810'] = func_5810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5810_call = mutated_mod.get_global_var('func_5810')
call_5811 = func_5810_call()
output = call_5811
func_5812 = relay.Function([], output)
mutated_mod['func_5812'] = func_5812
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5866 = relay.var("var_5866", dtype = "int8", shape = (5, 15, 1))#candidate|5866|(5, 15, 1)|var|int8
var_5867 = relay.var("var_5867", dtype = "int8", shape = (5, 15, 13))#candidate|5867|(5, 15, 13)|var|int8
bop_5868 = relay.less(var_5866.astype('bool'), var_5867.astype('bool')) # shape=(5, 15, 13)
func_2938_call = mod.get_global_var('func_2938')
func_2941_call = mutated_mod.get_global_var('func_2941')
var_5880 = relay.var("var_5880", dtype = "float64", shape = (105,))#candidate|5880|(105,)|var|float64
call_5879 = relay.TupleGetItem(func_2938_call(relay.reshape(var_5880.astype('float64'), [105,])), 1)
call_5881 = relay.TupleGetItem(func_2941_call(relay.reshape(var_5880.astype('float64'), [105,])), 1)
output = relay.Tuple([bop_5868,call_5879,var_5880,])
output2 = relay.Tuple([bop_5868,call_5881,var_5880,])
func_5899 = relay.Function([var_5866,var_5867,var_5880,], output)
mod['func_5899'] = func_5899
mod = relay.transform.InferType()(mod)
var_5900 = relay.var("var_5900", dtype = "int8", shape = (5, 15, 1))#candidate|5900|(5, 15, 1)|var|int8
var_5901 = relay.var("var_5901", dtype = "int8", shape = (5, 15, 13))#candidate|5901|(5, 15, 13)|var|int8
var_5902 = relay.var("var_5902", dtype = "float64", shape = (105,))#candidate|5902|(105,)|var|float64
output = func_5899(var_5900,var_5901,var_5902,)
func_5903 = relay.Function([var_5900,var_5901,var_5902,], output)
mutated_mod['func_5903'] = func_5903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5093_call = mutated_mod.get_global_var('func_5093')
call_5910 = func_5092_call()
call_5911 = func_5092_call()
output = call_5910
output2 = call_5911
func_5933 = relay.Function([], output)
mod['func_5933'] = func_5933
mod = relay.transform.InferType()(mod)
mutated_mod['func_5933'] = func_5933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5933_call = mutated_mod.get_global_var('func_5933')
call_5934 = func_5933_call()
output = call_5934
func_5935 = relay.Function([], output)
mutated_mod['func_5935'] = func_5935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_5947 = relay.TupleGetItem(func_1699_call(), 3)
call_5948 = relay.TupleGetItem(func_1700_call(), 3)
func_1975_call = mod.get_global_var('func_1975')
func_1979_call = mutated_mod.get_global_var('func_1979')
const_5951 = relay.const([[9.793824],[2.955490],[2.019706],[-4.940247],[1.406502],[-3.819558],[1.803948],[-1.134435],[-3.861848],[3.111443],[0.558059],[0.107537],[-7.739660],[6.371576],[-1.345889],[9.621190],[-3.756180],[9.255033],[-4.273278],[-9.201095],[-9.668620],[-6.834861],[-3.566772],[0.174577],[7.559605],[0.808046],[5.921095],[-6.153348],[7.680618],[7.519153],[8.739553],[2.150237],[6.302031],[-7.845154],[-4.951142],[4.822591],[2.667197],[-0.069583],[-0.140755],[-4.669313],[5.457557],[-4.534290],[1.449382],[-5.000379],[1.457020],[-4.089480],[-0.476422],[-1.350640],[-9.308356],[2.260592],[5.636612],[1.750157],[-8.820025],[4.788305],[4.414823],[-2.879616],[2.443665],[-5.511274],[6.448590],[9.733238],[-7.288085],[-4.244189],[1.391810],[-3.136628],[9.973607],[-9.897979],[-9.282072],[1.751192],[-6.532326],[6.374924],[-7.918314],[-9.055940],[-6.141315],[-6.120918],[1.688474],[-3.707208],[0.809664],[-1.412140],[-5.469897],[4.829142],[-3.615339],[-6.546700],[3.458593],[3.137929]], dtype = "float32")#candidate|5951|(84, 1)|const|float32
call_5950 = relay.TupleGetItem(func_1975_call(relay.reshape(const_5951.astype('float32'), [14, 2, 3]), relay.reshape(const_5951.astype('float32'), [14, 2, 3]), ), 4)
call_5952 = relay.TupleGetItem(func_1979_call(relay.reshape(const_5951.astype('float32'), [14, 2, 3]), relay.reshape(const_5951.astype('float32'), [14, 2, 3]), ), 4)
func_1757_call = mod.get_global_var('func_1757')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_5960 = func_1757_call()
call_5961 = func_1757_call()
output = relay.Tuple([call_5947,call_5950,const_5951,call_5960,])
output2 = relay.Tuple([call_5948,call_5952,const_5951,call_5961,])
func_5971 = relay.Function([], output)
mod['func_5971'] = func_5971
mod = relay.transform.InferType()(mod)
mutated_mod['func_5971'] = func_5971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5971_call = mutated_mod.get_global_var('func_5971')
call_5972 = func_5971_call()
output = call_5972
func_5973 = relay.Function([], output)
mutated_mod['func_5973'] = func_5973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_6011 = relay.TupleGetItem(func_1699_call(), 2)
call_6012 = relay.TupleGetItem(func_1700_call(), 2)
func_3736_call = mod.get_global_var('func_3736')
func_3737_call = mutated_mod.get_global_var('func_3737')
call_6024 = func_3736_call()
call_6025 = func_3736_call()
func_2694_call = mod.get_global_var('func_2694')
func_2696_call = mutated_mod.get_global_var('func_2696')
const_6027 = relay.const([-5.397285,2.245671,-6.272691,-2.427535,-8.296944,-6.832182,-2.456613,-2.084734,2.193001,5.655432,-7.703650,-8.173706,-0.933251,-1.852703,3.044404,8.288184,-1.535670,-5.850196,-9.251206,-9.305792,-4.715741,2.154049,0.436710,-4.034548,2.263156,-4.703972,-1.707505,7.304527,1.011877,-5.339893,-7.618785,-7.317738,-7.494643,2.632639,0.311209,8.518215,-0.039633,3.106214,-0.526495,-4.538625,1.981039,5.857320,5.074507,0.239906,4.641746,-8.402378,1.848135,-6.214502,0.610997,-9.986661,6.191321,-5.804262,-4.261076,-7.307280,1.910654,-2.197567,0.031583,-9.266411,-3.764547,3.095601,3.606320,9.814810,-0.656251,-1.016078,0.550160,-8.061386,-3.031706,3.689381,-6.832029,-8.426818,-3.064253,4.530227,-7.167265,9.199387,4.217234,-7.067751,-0.752411,7.605913,0.159838,-8.499041,-4.183670,-2.607568,2.207399,6.096783,6.646452,1.796486,-7.368831,0.075768,-4.647614,-4.754445,4.681886,-2.811786,-4.499602,-4.590456,5.970542,3.559667,2.578724,-2.891651,0.635133,1.149707,3.176636,-3.615695,9.320639,2.154990,-6.296749,6.920073,-9.197498,5.366831,3.919485,4.930382,-0.407687,-7.297114,-5.618011,-1.019415,-8.691576,-3.444712,-9.900497,2.900735,-4.125412,6.259727,-8.372585,-3.154599,-1.023022,-7.553113,0.589406,-6.152809,-1.391119,9.637540,-7.188815,-8.215972,9.632403,-9.346845,9.487172,5.904026,-6.409482,8.502092,4.290710,-5.313108,5.283061,5.915920,-5.809460,8.466213,-0.833336,8.944197,-5.920278,7.564215,-9.056486,-5.434786,-0.708632,2.746202,-9.057120,9.410655,-0.731649,-0.362880,-3.587457,-9.760393,2.286072,3.457938,-6.683912,-4.052859,-3.258709,8.042591,-7.716798,2.724662,1.155239,5.331852,5.335754,-9.101382,-4.191088,1.205743,-1.910119,5.119366,1.168799,-9.003207,0.928954,0.969669,-0.080194,-1.420507,-5.548256,2.052771,-7.368989,4.555937,-8.020054,2.359059,-7.143242,5.094743,-9.280005,3.109265,-9.729666,-5.769784,-8.341728,2.363270,-8.643914,2.247344,4.089781,-7.849886,-9.357001,0.567125,8.706993,8.956043,-6.785963,0.682486,-7.199108,-2.930689,-4.006245,-3.683285,-7.449659,7.241132,-5.634165,8.890183,-4.405435,6.966791,-6.143588,0.779568,-4.915557,9.339633,4.580687,3.618161,0.634021,-2.548255,-0.100636,8.848449,0.877629,9.776783,5.304844,8.276861,2.346926,-8.418651,-0.268295,7.910545,7.304544,5.402964,5.142880,-7.502978,-9.339274,-6.665972,6.175612,-6.881432,5.242679,-7.461982,-3.822610,-1.221897,9.940368,5.880795,-1.403330,-7.542206,-6.496966,-9.083774,-3.100119,-0.912724,-6.623594,-6.832973,-8.786314,-3.591490,-3.518176,7.133068,-7.710154,-1.000731,-0.814710,6.474034,4.633126,-3.165295,5.653990,7.738883,6.197476,4.075722,8.238183,-7.882192,-8.457847,7.816959,1.695842,6.979761,-8.136071,0.131964,-9.323017,1.406995,-0.137130,2.712510,-2.956119,-8.575644,-1.221865,8.470876,1.572043,-7.481308,-7.475058,-0.758044,-5.786211,-2.803238,-7.133411,7.540494,-7.835930,-0.920535,6.945362,5.483844,-5.701768,7.565994,7.664004,-1.458202,-7.708019,-2.763016,-4.638929,4.809520,-1.608129,3.877800,0.458690,9.554433,3.291668,2.029241,9.219161,2.368834,-7.201599,0.124366,9.059838,-2.498258,-6.609812,7.395904,5.773799,6.101570,-9.106649,-0.593714,7.292441,9.660802,9.197387,0.812823,7.942736,5.231307,-2.352023,7.469754,-7.686799,6.850131,-1.753999,-1.601594,5.338788,-9.433819,-3.442261,-2.302970,-1.042003,1.073213,-7.811101,0.156757,5.438067,9.968209,7.371043,6.316096,-9.081281,-8.572071,9.292698,-0.501307,-1.550079,-1.130549,-9.515276,-4.768087,6.129306,-8.681505,3.662943,5.495191,-0.656629,-8.949735,-5.537996,-5.131070,-3.619095,7.910541,6.782564,9.913408,-4.643249,-3.426084,-5.706428,-9.777155,-8.514371,3.454786,-1.582952,-6.059281,1.674668,-1.638789,8.473813,-2.403345,8.734945,5.554532,6.599963,-1.317935,0.379540,-9.278448,7.910044,7.184136,-5.549458,4.256281,1.346456,6.956602,-6.079747,-5.988185,-9.236547,-6.140983,9.096255,-2.369564,-4.161385,-1.414674,-6.360674,5.488857,6.471652,9.038862,3.563157,-5.881308,2.343584,2.737215,8.050091,5.410333,-7.172704,7.161017,4.980239,-6.962477,-1.128004,0.979267,-5.700446,4.120638,6.867414,0.519050,3.992087,-7.238423,4.428524,3.436581,4.225316,7.993163,-1.123242,9.744667,-4.123018,8.720395,1.355210,1.445525,7.636897,1.959292,-9.648049,0.240015,7.518432,-6.041395,9.891865,4.822471,-8.566610,-8.108714,-9.137760,-1.129714,6.089870,0.435147,7.327266,-8.277771,1.187663,3.489097,-0.862544,-6.010580,-0.354656,2.735726,-0.651551,9.923991,5.504921,8.516599,9.646299,-7.859483,3.795248,3.435714,9.553302,4.648317,-7.741449,-8.842205,4.316891,-9.153895,3.352506,3.670559,-4.480567,-2.364168,-9.951116,4.913124,5.989688,-1.188177,-4.106427,6.485647,-5.233184,-6.561884,-9.729224,2.165416,8.136423,5.973268,6.102287,-6.684744,5.329766,2.990486,-2.149537,-4.275039,2.983328,-2.344865,-4.088475,7.679548,-6.217966,3.843057,-0.461579,-5.494127,-0.461932,-1.857441,-7.612225,-4.924164,8.824207,8.232798,-2.259488,4.194967,5.071671,6.350449,-7.501034,-5.867479,4.400442,7.149215,-8.275964,0.855088,9.454838,7.065747,5.866945,-4.725959,7.060599,-3.669881,3.834124,6.054604,-8.614912,-6.019694,4.166063,4.114899,2.693734,-2.215191,4.771236,-1.430347,1.963173,-6.519279,4.426264,4.210434,0.171976,8.439807,-4.943632,8.988847,0.311609,7.311990,-3.906827,7.742764,5.024024,2.588597,-3.406128,5.594767,6.482102,-7.957569,-8.810816,-4.916587,1.462305,-7.568949,-0.309560,-6.061531,-7.723462,1.919180,3.323850,-7.274845,-3.624408,3.139455,4.019508,8.387844,-8.619072,-6.607469,3.068714,-0.943241,-1.063681,-1.806046,-7.719782,-8.909368,-8.036218,9.383186,2.049105,-1.999641,-2.833288,-5.859738,8.030804,-7.805848,8.424558,-6.835393,8.834542,3.430623,-9.165385,7.916597,3.277276,6.998255,9.893257,4.632318,-7.434039,-5.066707,0.246057,-4.214505,-9.827252,-6.488593,2.143115,4.061328,-1.351618,-4.212834,-7.431324,9.749534,-2.070243,-8.688289,-7.703880,-3.630801,6.345823,5.536353,2.263522,6.509196,-7.356964,8.764130,2.181517,9.336084,3.736315,-3.905710,5.471290,7.908596,-9.768154,2.397174,1.780742,1.568308,-1.132118,7.916413,-4.407018,-8.258690,7.904499,8.019074,-6.837473,-3.816381,-5.554115,7.909715,-4.734679,9.767122,-8.264709,1.681455,-3.881272,9.923284,1.651487,-3.419388,2.987634,1.538049,-3.778855,6.229621,8.563676,0.968783,-0.643483,2.172463,5.473061,1.694754,9.724998,-5.080429,9.331383,-3.539241,-0.411260,7.247337,4.551278,-7.615947,3.389112,-9.227831,9.900766,-6.599872,2.653519,5.221299,0.827570,-3.773742,1.394719,-9.026582,-6.404137,-3.671787,-7.247714,9.428878,-5.817508,3.289242,6.298825,-9.553906,4.726557,0.869616,-3.941193,-0.026710,6.402584,-1.458338,8.927566,-2.522016,2.364148,-3.602525,-1.250158,-3.218578,-4.637768,-4.743358,5.718281,-4.185250,8.706885,6.432114,-4.942638,5.200935,3.627802,1.495238,1.362200,-4.463692,-2.235189,-2.559341,-0.940357,4.784740,-4.887123,9.631545,-7.539582,2.453473,1.974326,6.072900,-6.344081,2.420438,-4.333173,-3.256788,-8.182106,-9.552261,5.894582,0.447287,5.367021,-2.622600,-2.191092,-9.694535,-6.502225,9.577131,-9.374356,8.855419,1.243725,-6.382941,1.107358,5.407053,-8.481277,-0.032863,-2.095488,4.401476,-1.172384,-4.748943,9.766125,3.657876,-4.435715,0.383623,2.942383,0.476617,-7.525585,-2.692289,-7.288465,8.808731,-6.227485,-0.152541,-4.200718,-5.308718,-0.086880,9.575170,4.245587,5.307391,2.993718,2.606587,7.688099,-8.513226,-9.645726,-2.806124,-0.161812,9.136542,4.170068,-5.024056,-0.687138,9.718777,9.383337,-4.174163,7.272981,-6.015060,7.841096,-8.383178,-9.162178,-9.173497,1.327573,0.217168,-4.450612,-8.454477,-6.415109,2.924226,-6.082659,3.479885,-5.047645,-7.639617,8.784213,-1.589694,-7.231207,-8.476362,1.621190,-8.236213,4.908948,5.951161,-8.850613,9.995157,-2.757336,4.841100,3.737363,-9.209296,7.707720,-7.540278,1.336763,1.956089,1.266669,-4.803855,-0.923526,1.386852,-2.904710,5.095897,4.722404,4.156561,-5.175748,-0.036735,-4.816663,0.817876,6.572556,-7.652384,-8.589799,7.251343,6.023200,2.045773,-8.227812,6.355844,9.355005,5.647089,-0.303721,-2.147893,-8.402847,-8.918070,7.150565,-6.318395,6.277352,5.925181,-5.417484,6.642462,-4.744244,6.510530,-5.404524,7.216274,8.890553,-8.946196,4.408051,-0.615526,9.378502,-0.694547,-9.529583,1.561395,-7.242346,-9.527212,3.358247,-9.087615,-5.646795,-5.492622,4.252262,-9.816913,8.029688,-7.832088,3.319311,-0.772144,0.984874,9.315632,3.206703,-2.077236,9.788348,-6.878984,-8.102221,-5.953038,-5.024381,2.360065,-6.571470,-9.481843,-1.645372,-4.942621,-2.202779,-1.310322,-1.869064,1.868601,7.651360,1.719136,-5.887434,5.726807,-3.015887,4.879545,7.336032,-6.028889,-5.320919,9.339681], dtype = "float32")#candidate|6027|(880,)|const|float32
call_6026 = relay.TupleGetItem(func_2694_call(relay.reshape(const_6027.astype('float32'), [880,])), 2)
call_6028 = relay.TupleGetItem(func_2696_call(relay.reshape(const_6027.astype('float32'), [880,])), 2)
func_2362_call = mod.get_global_var('func_2362')
func_2364_call = mutated_mod.get_global_var('func_2364')
call_6035 = relay.TupleGetItem(func_2362_call(), 3)
call_6036 = relay.TupleGetItem(func_2364_call(), 3)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_6037 = relay.TupleGetItem(func_1743_call(), 1)
call_6038 = relay.TupleGetItem(func_1745_call(), 1)
output = relay.Tuple([call_6011,call_6024,call_6026,const_6027,call_6035,call_6037,])
output2 = relay.Tuple([call_6012,call_6025,call_6028,const_6027,call_6036,call_6038,])
func_6043 = relay.Function([], output)
mod['func_6043'] = func_6043
mod = relay.transform.InferType()(mod)
mutated_mod['func_6043'] = func_6043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6043_call = mutated_mod.get_global_var('func_6043')
call_6044 = func_6043_call()
output = call_6044
func_6045 = relay.Function([], output)
mutated_mod['func_6045'] = func_6045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3055_call = mod.get_global_var('func_3055')
func_3057_call = mutated_mod.get_global_var('func_3057')
call_6064 = relay.TupleGetItem(func_3055_call(), 0)
call_6065 = relay.TupleGetItem(func_3057_call(), 0)
output = relay.Tuple([call_6064,])
output2 = relay.Tuple([call_6065,])
func_6076 = relay.Function([], output)
mod['func_6076'] = func_6076
mod = relay.transform.InferType()(mod)
mutated_mod['func_6076'] = func_6076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6076_call = mutated_mod.get_global_var('func_6076')
call_6077 = func_6076_call()
output = call_6077
func_6078 = relay.Function([], output)
mutated_mod['func_6078'] = func_6078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5291_call = mod.get_global_var('func_5291')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_6087 = func_5291_call()
call_6088 = func_5291_call()
output = relay.Tuple([call_6087,])
output2 = relay.Tuple([call_6088,])
func_6091 = relay.Function([], output)
mod['func_6091'] = func_6091
mod = relay.transform.InferType()(mod)
output = func_6091()
func_6092 = relay.Function([], output)
mutated_mod['func_6092'] = func_6092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1800_call = mod.get_global_var('func_1800')
func_1801_call = mutated_mod.get_global_var('func_1801')
call_6111 = relay.TupleGetItem(func_1800_call(), 0)
call_6112 = relay.TupleGetItem(func_1801_call(), 0)
output = call_6111
output2 = call_6112
func_6144 = relay.Function([], output)
mod['func_6144'] = func_6144
mod = relay.transform.InferType()(mod)
output = func_6144()
func_6145 = relay.Function([], output)
mutated_mod['func_6145'] = func_6145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3736_call = mod.get_global_var('func_3736')
func_3737_call = mutated_mod.get_global_var('func_3737')
call_6157 = func_3736_call()
call_6158 = func_3736_call()
func_2025_call = mod.get_global_var('func_2025')
func_2027_call = mutated_mod.get_global_var('func_2027')
const_6169 = relay.const(3, dtype = "int8")#candidate|6169|()|const|int8
call_6168 = relay.TupleGetItem(func_2025_call(relay.reshape(const_6169.astype('int8'), [])), 1)
call_6170 = relay.TupleGetItem(func_2027_call(relay.reshape(const_6169.astype('int8'), [])), 1)
func_5291_call = mod.get_global_var('func_5291')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_6176 = func_5291_call()
call_6177 = func_5291_call()
output = relay.Tuple([call_6157,call_6168,const_6169,call_6176,])
output2 = relay.Tuple([call_6158,call_6170,const_6169,call_6177,])
func_6194 = relay.Function([], output)
mod['func_6194'] = func_6194
mod = relay.transform.InferType()(mod)
output = func_6194()
func_6195 = relay.Function([], output)
mutated_mod['func_6195'] = func_6195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2227_call = mod.get_global_var('func_2227')
func_2228_call = mutated_mod.get_global_var('func_2228')
call_6485 = func_2227_call()
call_6486 = func_2227_call()
func_5455_call = mod.get_global_var('func_5455')
func_5457_call = mutated_mod.get_global_var('func_5457')
var_6489 = relay.var("var_6489", dtype = "float64", shape = (130,))#candidate|6489|(130,)|var|float64
call_6488 = relay.TupleGetItem(func_5455_call(relay.reshape(var_6489.astype('float64'), [130,])), 1)
call_6490 = relay.TupleGetItem(func_5457_call(relay.reshape(var_6489.astype('float64'), [130,])), 1)
output = relay.Tuple([call_6485,call_6488,var_6489,])
output2 = relay.Tuple([call_6486,call_6490,var_6489,])
func_6497 = relay.Function([var_6489,], output)
mod['func_6497'] = func_6497
mod = relay.transform.InferType()(mod)
mutated_mod['func_6497'] = func_6497
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6498 = relay.var("var_6498", dtype = "float64", shape = (130,))#candidate|6498|(130,)|var|float64
func_6497_call = mutated_mod.get_global_var('func_6497')
call_6499 = func_6497_call(var_6498)
output = call_6499
func_6500 = relay.Function([var_6498], output)
mutated_mod['func_6500'] = func_6500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5291_call = mod.get_global_var('func_5291')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_6504 = func_5291_call()
call_6505 = func_5291_call()
output = relay.Tuple([call_6504,])
output2 = relay.Tuple([call_6505,])
func_6513 = relay.Function([], output)
mod['func_6513'] = func_6513
mod = relay.transform.InferType()(mod)
output = func_6513()
func_6514 = relay.Function([], output)
mutated_mod['func_6514'] = func_6514
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6537 = relay.var("var_6537", dtype = "uint8", shape = (7, 14, 1))#candidate|6537|(7, 14, 1)|var|uint8
var_6538 = relay.var("var_6538", dtype = "uint8", shape = (7, 14, 1))#candidate|6538|(7, 14, 1)|var|uint8
bop_6539 = relay.left_shift(var_6537.astype('uint8'), relay.reshape(var_6538.astype('uint8'), relay.shape_of(var_6537))) # shape=(7, 14, 1)
output = bop_6539
output2 = bop_6539
func_6542 = relay.Function([var_6537,var_6538,], output)
mod['func_6542'] = func_6542
mod = relay.transform.InferType()(mod)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6542_call = mutated_mod.get_global_var('func_6542')
var_6544 = relay.var("var_6544", dtype = "uint8", shape = (7, 14, 1))#candidate|6544|(7, 14, 1)|var|uint8
var_6545 = relay.var("var_6545", dtype = "uint8", shape = (7, 14, 1))#candidate|6545|(7, 14, 1)|var|uint8
call_6543 = func_6542_call(var_6544,var_6545,)
output = call_6543
func_6546 = relay.Function([var_6544,var_6545,], output)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5971_call = mod.get_global_var('func_5971')
func_5973_call = mutated_mod.get_global_var('func_5973')
call_6574 = relay.TupleGetItem(func_5971_call(), 0)
call_6575 = relay.TupleGetItem(func_5973_call(), 0)
output = relay.Tuple([call_6574,])
output2 = relay.Tuple([call_6575,])
func_6588 = relay.Function([], output)
mod['func_6588'] = func_6588
mod = relay.transform.InferType()(mod)
output = func_6588()
func_6589 = relay.Function([], output)
mutated_mod['func_6589'] = func_6589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_807_call = mod.get_global_var('func_807')
func_809_call = mutated_mod.get_global_var('func_809')
call_6658 = relay.TupleGetItem(func_807_call(), 3)
call_6659 = relay.TupleGetItem(func_809_call(), 3)
output = call_6658
output2 = call_6659
func_6665 = relay.Function([], output)
mod['func_6665'] = func_6665
mod = relay.transform.InferType()(mod)
mutated_mod['func_6665'] = func_6665
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6665_call = mutated_mod.get_global_var('func_6665')
call_6666 = func_6665_call()
output = call_6666
func_6667 = relay.Function([], output)
mutated_mod['func_6667'] = func_6667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6144_call = mod.get_global_var('func_6144')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_6707 = func_6144_call()
call_6708 = func_6144_call()
func_3736_call = mod.get_global_var('func_3736')
func_3737_call = mutated_mod.get_global_var('func_3737')
call_6709 = func_3736_call()
call_6710 = func_3736_call()
output = relay.Tuple([call_6707,call_6709,])
output2 = relay.Tuple([call_6708,call_6710,])
func_6713 = relay.Function([], output)
mod['func_6713'] = func_6713
mod = relay.transform.InferType()(mod)
mutated_mod['func_6713'] = func_6713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6713_call = mutated_mod.get_global_var('func_6713')
call_6714 = func_6713_call()
output = call_6714
func_6715 = relay.Function([], output)
mutated_mod['func_6715'] = func_6715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_6718 = relay.TupleGetItem(func_1699_call(), 3)
call_6719 = relay.TupleGetItem(func_1700_call(), 3)
func_3091_call = mod.get_global_var('func_3091')
func_3094_call = mutated_mod.get_global_var('func_3094')
var_6739 = relay.var("var_6739", dtype = "int8", shape = ())#candidate|6739|()|var|int8
call_6738 = relay.TupleGetItem(func_3091_call(relay.reshape(var_6739.astype('int8'), [])), 3)
call_6740 = relay.TupleGetItem(func_3094_call(relay.reshape(var_6739.astype('int8'), [])), 3)
output = relay.Tuple([call_6718,call_6738,var_6739,])
output2 = relay.Tuple([call_6719,call_6740,var_6739,])
func_6762 = relay.Function([var_6739,], output)
mod['func_6762'] = func_6762
mod = relay.transform.InferType()(mod)
var_6763 = relay.var("var_6763", dtype = "int8", shape = ())#candidate|6763|()|var|int8
output = func_6762(var_6763)
func_6764 = relay.Function([var_6763], output)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_6814 = relay.TupleGetItem(func_2623_call(), 1)
call_6815 = relay.TupleGetItem(func_2625_call(), 1)
func_4781_call = mod.get_global_var('func_4781')
func_4783_call = mutated_mod.get_global_var('func_4783')
call_6831 = relay.TupleGetItem(func_4781_call(), 0)
call_6832 = relay.TupleGetItem(func_4783_call(), 0)
output = relay.Tuple([call_6814,call_6831,])
output2 = relay.Tuple([call_6815,call_6832,])
func_6841 = relay.Function([], output)
mod['func_6841'] = func_6841
mod = relay.transform.InferType()(mod)
output = func_6841()
func_6842 = relay.Function([], output)
mutated_mod['func_6842'] = func_6842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2997_call = mod.get_global_var('func_2997')
func_2998_call = mutated_mod.get_global_var('func_2998')
call_6880 = relay.TupleGetItem(func_2997_call(), 0)
call_6881 = relay.TupleGetItem(func_2998_call(), 0)
output = relay.Tuple([call_6880,])
output2 = relay.Tuple([call_6881,])
func_6888 = relay.Function([], output)
mod['func_6888'] = func_6888
mod = relay.transform.InferType()(mod)
mutated_mod['func_6888'] = func_6888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6888_call = mutated_mod.get_global_var('func_6888')
call_6889 = func_6888_call()
output = call_6889
func_6890 = relay.Function([], output)
mutated_mod['func_6890'] = func_6890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_6966 = relay.TupleGetItem(func_713_call(), 1)
call_6967 = relay.TupleGetItem(func_714_call(), 1)
func_1464_call = mod.get_global_var('func_1464')
func_1465_call = mutated_mod.get_global_var('func_1465')
call_6974 = func_1464_call()
call_6975 = func_1464_call()
func_4055_call = mod.get_global_var('func_4055')
func_4056_call = mutated_mod.get_global_var('func_4056')
call_6986 = relay.TupleGetItem(func_4055_call(), 1)
call_6987 = relay.TupleGetItem(func_4056_call(), 1)
func_4645_call = mod.get_global_var('func_4645')
func_4646_call = mutated_mod.get_global_var('func_4646')
call_6995 = relay.TupleGetItem(func_4645_call(), 0)
call_6996 = relay.TupleGetItem(func_4646_call(), 0)
func_569_call = mod.get_global_var('func_569')
func_572_call = mutated_mod.get_global_var('func_572')
call_6997 = relay.TupleGetItem(func_569_call(relay.reshape(call_6974.astype('bool'), [14, 8, 4])), 0)
call_6998 = relay.TupleGetItem(func_572_call(relay.reshape(call_6974.astype('bool'), [14, 8, 4])), 0)
output = relay.Tuple([call_6966,call_6974,call_6986,call_6995,call_6997,])
output2 = relay.Tuple([call_6967,call_6975,call_6987,call_6996,call_6998,])
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
func_7008_call = mod.get_global_var('func_7008')
func_7010_call = mutated_mod.get_global_var('func_7010')
call_7019 = relay.TupleGetItem(func_7008_call(), 3)
call_7020 = relay.TupleGetItem(func_7010_call(), 3)
func_2534_call = mod.get_global_var('func_2534')
func_2537_call = mutated_mod.get_global_var('func_2537')
const_7057 = relay.const([-7.291309,-6.015925,6.170590,6.108856,8.441390,8.653549,6.411546,3.910853,4.946232,4.347496,5.859281,0.649102,-2.044050,3.365235,9.237124,8.885438,2.952680,-4.776796,-1.910368,3.446952,-9.799916,6.212187,-7.643817,0.028335,-3.616741,1.390111,-3.971779,4.753722,-6.206273,-1.126729,-2.378915,7.628334,1.748624,7.913258,-3.347567,-7.550129,9.097742,-4.125757,-6.237138,0.545630,-5.634767,-8.617095,9.929982,-8.415486,3.138407,0.075417,-6.076077,2.251638,-5.235523,3.743047,0.870264,-8.504756,5.504043,7.215089,-8.686977,2.728078,8.429489,1.396986,8.408788,-4.850708,-1.135995,-9.312564,5.729539,9.469620,-6.398520,-5.348080,-8.050204,-5.257680,2.069373,5.427596,-4.716615,5.633710,0.432246,4.230395,-3.897989,2.628060,2.212489,8.733566,0.402619,4.487583,-2.627907,-7.322120,-3.415304,-1.251024,-9.994940,3.827504,-4.188288,-8.446860,-0.082998,-8.753988,-1.744917,2.563159,-9.494637,-1.625543,8.337482,1.878464,5.106607,-2.958234,4.287436,2.441975,1.663266,-2.535033,9.742884,2.642320,-0.814438,-8.474824,0.040309,1.509361,3.358457,4.341114,5.999321,-6.573795,-9.087179,-1.674012,2.390105,1.346599,-1.544535,9.195492,2.834026,0.908467,-1.404829,-9.718919,-7.622590,1.746469,2.776192,-8.323631,-6.482658,1.785197,-1.851701,-8.345299,5.231246,-7.984911,0.212176,-9.098339,-1.006846,8.412578,9.201978,-5.274427,3.794202,3.207697,-9.343716,9.229786,-9.185401,-6.900491,-8.721133,7.497152,-9.781526,3.900001,2.228896,-0.123241,-4.344744,-8.990669,8.445195,3.943097,1.389288,5.026047,-5.608522,-5.451810,8.220276,4.099745,8.890517,-9.747101,-0.709075,9.894747,2.136596,5.655760,3.514159,4.388926,-8.639779,0.635740,-5.309622,-2.441500,9.474175,8.228294,6.486158,-2.902905,7.151966,-1.271461,1.841408,0.631552,-8.001420,-9.892124,4.265942,-8.810379,-5.179191,1.687925,0.781979,5.974703,-7.130736,5.246713,-1.067649,-7.921870,-1.461898,8.997715,-8.291141,-1.044791,-6.836559,2.142632,4.376513,8.903722,6.528221,-1.569545,-3.595687,-6.875783,-5.497931,-7.843294,9.260535,1.159363,-2.676754,5.735044,9.646337,5.123043,-2.729551,0.342897,-2.108880,4.275046,4.863873,-6.539012,-7.328104,-7.180933,3.973840,1.071555,4.040056,-6.733699,1.161293,6.026062,-7.048687,-1.095322,2.218914,-8.254529,5.789361,3.444889,9.971440,-8.252073,-2.333825,-0.993689,-3.805326,6.884191,-3.551257,5.708080,3.752174,4.396355,3.990786,1.871050,8.417749,-3.925672,5.011024,-5.060004,-5.975738,-1.460633,6.880873,-4.033313,-7.524630,-2.356076,9.180413,9.181300,-9.697071,-6.300676,-3.308827,-9.044317,4.546542,-3.091830,-1.029927,0.942838,-8.271788,-5.116126,5.595904,8.324479,-4.543521,-1.180015,6.909415,-6.267091,-6.974090,7.845328,-9.379978,9.135026,-9.263362,1.354983,-3.022120,1.863181,-9.424544,-2.165355,-0.110063,-9.357520,4.552273,8.260137,-6.540353,-8.756908,-7.876237,3.277899,6.220983,3.096738,2.702573,7.124768], dtype = "float32")#candidate|7057|(294,)|const|float32
call_7056 = func_2534_call(relay.reshape(const_7057.astype('float32'), [7, 7, 6]))
call_7058 = func_2534_call(relay.reshape(const_7057.astype('float32'), [7, 7, 6]))
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_7061 = relay.TupleGetItem(func_735_call(), 1)
call_7062 = relay.TupleGetItem(func_737_call(), 1)
output = relay.Tuple([call_7019,call_7056,const_7057,call_7061,])
output2 = relay.Tuple([call_7020,call_7058,const_7057,call_7062,])
func_7063 = relay.Function([], output)
mod['func_7063'] = func_7063
mod = relay.transform.InferType()(mod)
mutated_mod['func_7063'] = func_7063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7063_call = mutated_mod.get_global_var('func_7063')
call_7064 = func_7063_call()
output = call_7064
func_7065 = relay.Function([], output)
mutated_mod['func_7065'] = func_7065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mod.get_global_var('func_4378')
func_4379_call = mutated_mod.get_global_var('func_4379')
call_7074 = func_4378_call()
call_7075 = func_4378_call()
output = call_7074
output2 = call_7075
func_7088 = relay.Function([], output)
mod['func_7088'] = func_7088
mod = relay.transform.InferType()(mod)
output = func_7088()
func_7089 = relay.Function([], output)
mutated_mod['func_7089'] = func_7089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4378_call = mod.get_global_var('func_4378')
func_4379_call = mutated_mod.get_global_var('func_4379')
call_7092 = func_4378_call()
call_7093 = func_4378_call()
func_4284_call = mod.get_global_var('func_4284')
func_4290_call = mutated_mod.get_global_var('func_4290')
var_7095 = relay.var("var_7095", dtype = "int64", shape = (468,))#candidate|7095|(468,)|var|int64
const_7096 = relay.const([[-8.023926,3.238687,-7.121461,3.210726],[-6.062767,-9.371565,3.254731,9.885802],[-5.047678,5.652284,3.004900,-0.801521],[-7.402717,-5.713995,-1.238897,6.691432],[7.511967,5.507115,6.672443,1.188830],[-6.522334,-3.820563,-0.832142,9.906084],[-7.750367,-8.709601,7.897896,0.416402],[5.721640,-3.511012,4.644076,-7.697340],[-0.380945,-7.288185,-9.977195,-2.888489],[2.134605,-9.619448,-9.397907,-6.493751],[-4.830967,-8.322829,0.946469,1.692919],[-8.348194,-3.332773,-5.133817,-3.236634],[-8.809243,-3.866750,2.752173,3.854831],[3.494165,-4.630341,8.682754,-0.995790],[2.462367,7.064221,9.005815,6.265422],[0.429147,9.222456,3.150804,-1.613233],[4.195081,-2.445158,3.225909,3.740028],[-7.489874,5.069425,8.931400,8.890763],[-1.900730,9.924543,-7.429318,6.700910],[3.186041,3.173470,7.751531,-8.145526],[-1.342154,7.612825,7.672124,-5.121892]], dtype = "float32")#candidate|7096|(21, 4)|const|float32
var_7097 = relay.var("var_7097", dtype = "float32", shape = (294,))#candidate|7097|(294,)|var|float32
call_7094 = relay.TupleGetItem(func_4284_call(relay.reshape(var_7095.astype('int64'), [6, 13, 6]), relay.reshape(var_7095.astype('int64'), [6, 13, 6]), relay.reshape(var_7095.astype('float64'), [6, 13, 6]), relay.reshape(const_7096.astype('float32'), [84,]), relay.reshape(var_7097.astype('float32'), [294,]), ), 5)
call_7098 = relay.TupleGetItem(func_4290_call(relay.reshape(var_7095.astype('int64'), [6, 13, 6]), relay.reshape(var_7095.astype('int64'), [6, 13, 6]), relay.reshape(var_7095.astype('float64'), [6, 13, 6]), relay.reshape(const_7096.astype('float32'), [84,]), relay.reshape(var_7097.astype('float32'), [294,]), ), 5)
var_7102 = relay.var("var_7102", dtype = "float32", shape = (21, 4))#candidate|7102|(21, 4)|var|float32
bop_7103 = relay.floor_divide(const_7096.astype('float64'), relay.reshape(var_7102.astype('float64'), relay.shape_of(const_7096))) # shape=(21, 4)
func_1464_call = mod.get_global_var('func_1464')
func_1465_call = mutated_mod.get_global_var('func_1465')
call_7107 = func_1464_call()
call_7108 = func_1464_call()
func_3997_call = mod.get_global_var('func_3997')
func_4000_call = mutated_mod.get_global_var('func_4000')
call_7109 = relay.TupleGetItem(func_3997_call(relay.reshape(call_7092.astype('float32'), [880,])), 0)
call_7110 = relay.TupleGetItem(func_4000_call(relay.reshape(call_7092.astype('float32'), [880,])), 0)
bop_7127 = relay.greater(const_7096.astype('bool'), relay.reshape(var_7102.astype('bool'), relay.shape_of(const_7096))) # shape=(21, 4)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_7131 = relay.TupleGetItem(func_2623_call(), 1)
call_7132 = relay.TupleGetItem(func_2625_call(), 1)
bop_7139 = relay.left_shift(bop_7127.astype('uint16'), relay.reshape(bop_7103.astype('uint16'), relay.shape_of(bop_7127))) # shape=(21, 4)
func_5455_call = mod.get_global_var('func_5455')
func_5457_call = mutated_mod.get_global_var('func_5457')
var_7147 = relay.var("var_7147", dtype = "float64", shape = (130,))#candidate|7147|(130,)|var|float64
call_7146 = relay.TupleGetItem(func_5455_call(relay.reshape(var_7147.astype('float64'), [130,])), 0)
call_7148 = relay.TupleGetItem(func_5457_call(relay.reshape(var_7147.astype('float64'), [130,])), 0)
output = relay.Tuple([call_7092,call_7094,var_7095,var_7097,call_7107,call_7109,call_7131,bop_7139,call_7146,var_7147,])
output2 = relay.Tuple([call_7093,call_7098,var_7095,var_7097,call_7108,call_7110,call_7132,bop_7139,call_7148,var_7147,])
func_7155 = relay.Function([var_7095,var_7097,var_7102,var_7147,], output)
mod['func_7155'] = func_7155
mod = relay.transform.InferType()(mod)
var_7156 = relay.var("var_7156", dtype = "int64", shape = (468,))#candidate|7156|(468,)|var|int64
var_7157 = relay.var("var_7157", dtype = "float32", shape = (294,))#candidate|7157|(294,)|var|float32
var_7158 = relay.var("var_7158", dtype = "float32", shape = (21, 4))#candidate|7158|(21, 4)|var|float32
var_7159 = relay.var("var_7159", dtype = "float64", shape = (130,))#candidate|7159|(130,)|var|float64
output = func_7155(var_7156,var_7157,var_7158,var_7159,)
func_7160 = relay.Function([var_7156,var_7157,var_7158,var_7159,], output)
mutated_mod['func_7160'] = func_7160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3011_call = mod.get_global_var('func_3011')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_7166 = func_3011_call()
call_7167 = func_3011_call()
output = relay.Tuple([call_7166,])
output2 = relay.Tuple([call_7167,])
func_7183 = relay.Function([], output)
mod['func_7183'] = func_7183
mod = relay.transform.InferType()(mod)
mutated_mod['func_7183'] = func_7183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7183_call = mutated_mod.get_global_var('func_7183')
call_7184 = func_7183_call()
output = call_7184
func_7185 = relay.Function([], output)
mutated_mod['func_7185'] = func_7185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_7296 = relay.TupleGetItem(func_1699_call(), 5)
call_7297 = relay.TupleGetItem(func_1700_call(), 5)
output = call_7296
output2 = call_7297
func_7363 = relay.Function([], output)
mod['func_7363'] = func_7363
mod = relay.transform.InferType()(mod)
mutated_mod['func_7363'] = func_7363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7363_call = mutated_mod.get_global_var('func_7363')
call_7364 = func_7363_call()
output = call_7364
func_7365 = relay.Function([], output)
mutated_mod['func_7365'] = func_7365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5092_call = mod.get_global_var('func_5092')
func_5093_call = mutated_mod.get_global_var('func_5093')
call_7438 = func_5092_call()
call_7439 = func_5092_call()
output = call_7438
output2 = call_7439
func_7450 = relay.Function([], output)
mod['func_7450'] = func_7450
mod = relay.transform.InferType()(mod)
output = func_7450()
func_7451 = relay.Function([], output)
mutated_mod['func_7451'] = func_7451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2623_call = mod.get_global_var('func_2623')
func_2625_call = mutated_mod.get_global_var('func_2625')
call_7504 = relay.TupleGetItem(func_2623_call(), 1)
call_7505 = relay.TupleGetItem(func_2625_call(), 1)
output = relay.Tuple([call_7504,])
output2 = relay.Tuple([call_7505,])
func_7506 = relay.Function([], output)
mod['func_7506'] = func_7506
mod = relay.transform.InferType()(mod)
mutated_mod['func_7506'] = func_7506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mutated_mod.get_global_var('func_7506')
call_7507 = func_7506_call()
output = call_7507
func_7508 = relay.Function([], output)
mutated_mod['func_7508'] = func_7508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7508_call = mutated_mod.get_global_var('func_7508')
call_7535 = relay.TupleGetItem(func_7506_call(), 0)
call_7536 = relay.TupleGetItem(func_7508_call(), 0)
output = call_7535
output2 = call_7536
func_7540 = relay.Function([], output)
mod['func_7540'] = func_7540
mod = relay.transform.InferType()(mod)
output = func_7540()
func_7541 = relay.Function([], output)
mutated_mod['func_7541'] = func_7541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4645_call = mod.get_global_var('func_4645')
func_4646_call = mutated_mod.get_global_var('func_4646')
call_7550 = relay.TupleGetItem(func_4645_call(), 0)
call_7551 = relay.TupleGetItem(func_4646_call(), 0)
func_1116_call = mod.get_global_var('func_1116')
func_1118_call = mutated_mod.get_global_var('func_1118')
call_7555 = func_1116_call()
call_7556 = func_1116_call()
output = relay.Tuple([call_7550,call_7555,])
output2 = relay.Tuple([call_7551,call_7556,])
func_7571 = relay.Function([], output)
mod['func_7571'] = func_7571
mod = relay.transform.InferType()(mod)
output = func_7571()
func_7572 = relay.Function([], output)
mutated_mod['func_7572'] = func_7572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_7612 = relay.TupleGetItem(func_108_call(), 0)
call_7613 = relay.TupleGetItem(func_110_call(), 0)
output = call_7612
output2 = call_7613
func_7621 = relay.Function([], output)
mod['func_7621'] = func_7621
mod = relay.transform.InferType()(mod)
output = func_7621()
func_7622 = relay.Function([], output)
mutated_mod['func_7622'] = func_7622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mod.get_global_var('func_3703')
func_3705_call = mutated_mod.get_global_var('func_3705')
call_7630 = relay.TupleGetItem(func_3703_call(), 1)
call_7631 = relay.TupleGetItem(func_3705_call(), 1)
output = relay.Tuple([call_7630,])
output2 = relay.Tuple([call_7631,])
func_7651 = relay.Function([], output)
mod['func_7651'] = func_7651
mod = relay.transform.InferType()(mod)
mutated_mod['func_7651'] = func_7651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7651_call = mutated_mod.get_global_var('func_7651')
call_7652 = func_7651_call()
output = call_7652
func_7653 = relay.Function([], output)
mutated_mod['func_7653'] = func_7653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6144_call = mod.get_global_var('func_6144')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_7654 = func_6144_call()
call_7655 = func_6144_call()
func_5621_call = mod.get_global_var('func_5621')
func_5622_call = mutated_mod.get_global_var('func_5622')
call_7677 = func_5621_call()
call_7678 = func_5621_call()
output = relay.Tuple([call_7654,call_7677,])
output2 = relay.Tuple([call_7655,call_7678,])
func_7680 = relay.Function([], output)
mod['func_7680'] = func_7680
mod = relay.transform.InferType()(mod)
mutated_mod['func_7680'] = func_7680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7680_call = mutated_mod.get_global_var('func_7680')
call_7681 = func_7680_call()
output = call_7681
func_7682 = relay.Function([], output)
mutated_mod['func_7682'] = func_7682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7063_call = mod.get_global_var('func_7063')
func_7065_call = mutated_mod.get_global_var('func_7065')
call_7689 = relay.TupleGetItem(func_7063_call(), 1)
call_7690 = relay.TupleGetItem(func_7065_call(), 1)
output = relay.Tuple([call_7689,])
output2 = relay.Tuple([call_7690,])
func_7706 = relay.Function([], output)
mod['func_7706'] = func_7706
mod = relay.transform.InferType()(mod)
mutated_mod['func_7706'] = func_7706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7706_call = mutated_mod.get_global_var('func_7706')
call_7707 = func_7706_call()
output = call_7707
func_7708 = relay.Function([], output)
mutated_mod['func_7708'] = func_7708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3403_call = mod.get_global_var('func_3403')
func_3405_call = mutated_mod.get_global_var('func_3405')
call_7720 = relay.TupleGetItem(func_3403_call(), 0)
call_7721 = relay.TupleGetItem(func_3405_call(), 0)
output = call_7720
output2 = call_7721
func_7735 = relay.Function([], output)
mod['func_7735'] = func_7735
mod = relay.transform.InferType()(mod)
mutated_mod['func_7735'] = func_7735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7735_call = mutated_mod.get_global_var('func_7735')
call_7736 = func_7735_call()
output = call_7736
func_7737 = relay.Function([], output)
mutated_mod['func_7737'] = func_7737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2968_call = mod.get_global_var('func_2968')
func_2969_call = mutated_mod.get_global_var('func_2969')
call_7744 = relay.TupleGetItem(func_2968_call(), 1)
call_7745 = relay.TupleGetItem(func_2969_call(), 1)
output = relay.Tuple([call_7744,])
output2 = relay.Tuple([call_7745,])
func_7790 = relay.Function([], output)
mod['func_7790'] = func_7790
mod = relay.transform.InferType()(mod)
mutated_mod['func_7790'] = func_7790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7790_call = mutated_mod.get_global_var('func_7790')
call_7791 = func_7790_call()
output = call_7791
func_7792 = relay.Function([], output)
mutated_mod['func_7792'] = func_7792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7706_call = mod.get_global_var('func_7706')
func_7708_call = mutated_mod.get_global_var('func_7708')
call_7850 = relay.TupleGetItem(func_7706_call(), 0)
call_7851 = relay.TupleGetItem(func_7708_call(), 0)
uop_7859 = relay.acosh(call_7850.astype('float64')) # shape=(7, 7, 6)
uop_7861 = relay.acosh(call_7851.astype('float64')) # shape=(7, 7, 6)
func_2938_call = mod.get_global_var('func_2938')
func_2941_call = mutated_mod.get_global_var('func_2941')
const_7878 = relay.const([7.822668,-9.297721,-7.410080,-4.307621,0.089535,2.225330,-0.187356,4.814158,5.670574,-6.135492,-3.886036,5.710309,-1.896670,-7.794156,4.752791,-6.234445,-9.356128,-3.884962,6.843786,5.685301,-2.314045,6.802588,4.427985,7.676105,0.316235,-5.405778,9.420073,7.102292,0.898190,1.729528,8.733708,4.886593,6.880237,9.940752,-6.233312,3.976129,4.811419,6.318678,6.588769,4.482173,-7.557307,-4.580141,8.073550,-1.493599,4.401318,-7.500767,2.525118,-4.519634,8.465701,0.303348,0.544749,-4.828761,2.193132,1.567698,1.082841,6.045241,7.328219,5.037393,7.923739,7.995307,0.537116,-1.416703,8.380609,8.598680,-6.505309,7.085433,0.719994,-9.776347,6.640807,5.196275,-3.361050,2.063784,8.463984,-1.751936,-7.703543,0.662639,0.938561,-5.013010,1.852533,0.653145,-3.278296,4.919671,2.383759,-2.230867,2.457445,5.112202,-0.687736,0.217902,0.113613,7.327181,1.063492,5.776985,-2.534198,-5.313116,-7.633846,8.233528,-9.881672,-5.800485,-4.395010,-0.902933,1.018063,6.527327,-5.840897,4.052347,-1.377447], dtype = "float64")#candidate|7878|(105,)|const|float64
call_7877 = relay.TupleGetItem(func_2938_call(relay.reshape(const_7878.astype('float64'), [105,])), 1)
call_7879 = relay.TupleGetItem(func_2941_call(relay.reshape(const_7878.astype('float64'), [105,])), 1)
bop_7885 = relay.power(uop_7859.astype('float32'), relay.reshape(call_7850.astype('float32'), relay.shape_of(uop_7859))) # shape=(7, 7, 6)
bop_7888 = relay.power(uop_7861.astype('float32'), relay.reshape(call_7851.astype('float32'), relay.shape_of(uop_7861))) # shape=(7, 7, 6)
output = relay.Tuple([call_7877,const_7878,bop_7885,])
output2 = relay.Tuple([call_7879,const_7878,bop_7888,])
func_7899 = relay.Function([], output)
mod['func_7899'] = func_7899
mod = relay.transform.InferType()(mod)
output = func_7899()
func_7900 = relay.Function([], output)
mutated_mod['func_7900'] = func_7900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2362_call = mod.get_global_var('func_2362')
func_2364_call = mutated_mod.get_global_var('func_2364')
call_7920 = relay.TupleGetItem(func_2362_call(), 3)
call_7921 = relay.TupleGetItem(func_2364_call(), 3)
func_2149_call = mod.get_global_var('func_2149')
func_2152_call = mutated_mod.get_global_var('func_2152')
var_7923 = relay.var("var_7923", dtype = "float64", shape = (240,))#candidate|7923|(240,)|var|float64
call_7922 = relay.TupleGetItem(func_2149_call(relay.reshape(var_7923.astype('float64'), [240,])), 2)
call_7924 = relay.TupleGetItem(func_2152_call(relay.reshape(var_7923.astype('float64'), [240,])), 2)
output = relay.Tuple([call_7920,call_7922,var_7923,])
output2 = relay.Tuple([call_7921,call_7924,var_7923,])
func_7929 = relay.Function([var_7923,], output)
mod['func_7929'] = func_7929
mod = relay.transform.InferType()(mod)
mutated_mod['func_7929'] = func_7929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7930 = relay.var("var_7930", dtype = "float64", shape = (240,))#candidate|7930|(240,)|var|float64
func_7929_call = mutated_mod.get_global_var('func_7929')
call_7931 = func_7929_call(var_7930)
output = call_7931
func_7932 = relay.Function([var_7930], output)
mutated_mod['func_7932'] = func_7932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3403_call = mod.get_global_var('func_3403')
func_3405_call = mutated_mod.get_global_var('func_3405')
call_7934 = relay.TupleGetItem(func_3403_call(), 0)
call_7935 = relay.TupleGetItem(func_3405_call(), 0)
func_6497_call = mod.get_global_var('func_6497')
func_6500_call = mutated_mod.get_global_var('func_6500')
var_7938 = relay.var("var_7938", dtype = "float64", shape = (130,))#candidate|7938|(130,)|var|float64
call_7937 = relay.TupleGetItem(func_6497_call(relay.reshape(var_7938.astype('float64'), [130,])), 1)
call_7939 = relay.TupleGetItem(func_6500_call(relay.reshape(var_7938.astype('float64'), [130,])), 1)
func_3736_call = mod.get_global_var('func_3736')
func_3737_call = mutated_mod.get_global_var('func_3737')
call_7949 = func_3736_call()
call_7950 = func_3736_call()
output = relay.Tuple([call_7934,call_7937,var_7938,call_7949,])
output2 = relay.Tuple([call_7935,call_7939,var_7938,call_7950,])
func_7951 = relay.Function([var_7938,], output)
mod['func_7951'] = func_7951
mod = relay.transform.InferType()(mod)
var_7952 = relay.var("var_7952", dtype = "float64", shape = (130,))#candidate|7952|(130,)|var|float64
output = func_7951(var_7952)
func_7953 = relay.Function([var_7952], output)
mutated_mod['func_7953'] = func_7953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_7999 = relay.TupleGetItem(func_735_call(), 1)
call_8000 = relay.TupleGetItem(func_737_call(), 1)
func_7571_call = mod.get_global_var('func_7571')
func_7572_call = mutated_mod.get_global_var('func_7572')
call_8004 = relay.TupleGetItem(func_7571_call(), 1)
call_8005 = relay.TupleGetItem(func_7572_call(), 1)
func_3474_call = mod.get_global_var('func_3474')
func_3477_call = mutated_mod.get_global_var('func_3477')
const_8007 = relay.const([9.171955,3.944162,2.990100,6.549376,-8.754825,2.215235,0.065190,3.193251,7.614929,3.107982,5.969737,-6.771326,-2.770766,-0.124184,1.029291,7.057659,-3.760519,-1.692728,7.757399,0.968601,3.404837,5.422186,5.471830,0.121886,-8.988982,7.019584,7.528386,5.087271,-1.133517,5.137152,-2.305634,7.123826,4.500163,-3.905470,9.618490,9.668802,3.257589,-8.062126,6.558780,1.800513,-2.142142,-7.576031,-0.857734,0.800185,4.907914,2.460745,5.041193,9.271925,-2.374044,3.110373,4.525359,-0.266041,-4.536363,-4.669004,-3.513818,2.439809,-2.046100,3.584370,-4.764050,7.860133,7.283740,0.465025,2.170164,-4.029932,-1.000165,-4.945985,-1.754522,-2.003177,9.020258,-6.731911,-9.779119,-5.065717,3.221259,-8.219996,-9.781376,-4.691616,-9.099374,-2.702864,-0.693395,0.956125,8.870539,-4.378966,3.264733,-1.508056], dtype = "float32")#candidate|8007|(84,)|const|float32
call_8006 = relay.TupleGetItem(func_3474_call(relay.reshape(const_8007.astype('float32'), [84,])), 2)
call_8008 = relay.TupleGetItem(func_3477_call(relay.reshape(const_8007.astype('float32'), [84,])), 2)
output = relay.Tuple([call_7999,call_8004,call_8006,const_8007,])
output2 = relay.Tuple([call_8000,call_8005,call_8008,const_8007,])
func_8014 = relay.Function([], output)
mod['func_8014'] = func_8014
mod = relay.transform.InferType()(mod)
output = func_8014()
func_8015 = relay.Function([], output)
mutated_mod['func_8015'] = func_8015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6194_call = mod.get_global_var('func_6194')
func_6195_call = mutated_mod.get_global_var('func_6195')
call_8022 = relay.TupleGetItem(func_6194_call(), 1)
call_8023 = relay.TupleGetItem(func_6195_call(), 1)
output = call_8022
output2 = call_8023
func_8027 = relay.Function([], output)
mod['func_8027'] = func_8027
mod = relay.transform.InferType()(mod)
mutated_mod['func_8027'] = func_8027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8027_call = mutated_mod.get_global_var('func_8027')
call_8028 = func_8027_call()
output = call_8028
func_8029 = relay.Function([], output)
mutated_mod['func_8029'] = func_8029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_8081 = relay.TupleGetItem(func_108_call(), 0)
call_8082 = relay.TupleGetItem(func_110_call(), 0)
func_3233_call = mod.get_global_var('func_3233')
func_3235_call = mutated_mod.get_global_var('func_3235')
call_8099 = relay.TupleGetItem(func_3233_call(), 1)
call_8100 = relay.TupleGetItem(func_3235_call(), 1)
output = relay.Tuple([call_8081,call_8099,])
output2 = relay.Tuple([call_8082,call_8100,])
func_8106 = relay.Function([], output)
mod['func_8106'] = func_8106
mod = relay.transform.InferType()(mod)
mutated_mod['func_8106'] = func_8106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8106_call = mutated_mod.get_global_var('func_8106')
call_8107 = func_8106_call()
output = call_8107
func_8108 = relay.Function([], output)
mutated_mod['func_8108'] = func_8108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8027_call = mod.get_global_var('func_8027')
func_8029_call = mutated_mod.get_global_var('func_8029')
call_8126 = func_8027_call()
call_8127 = func_8027_call()
output = call_8126
output2 = call_8127
func_8128 = relay.Function([], output)
mod['func_8128'] = func_8128
mod = relay.transform.InferType()(mod)
output = func_8128()
func_8129 = relay.Function([], output)
mutated_mod['func_8129'] = func_8129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6588_call = mod.get_global_var('func_6588')
func_6589_call = mutated_mod.get_global_var('func_6589')
call_8158 = relay.TupleGetItem(func_6588_call(), 0)
call_8159 = relay.TupleGetItem(func_6589_call(), 0)
func_7363_call = mod.get_global_var('func_7363')
func_7365_call = mutated_mod.get_global_var('func_7365')
call_8160 = func_7363_call()
call_8161 = func_7363_call()
func_7540_call = mod.get_global_var('func_7540')
func_7541_call = mutated_mod.get_global_var('func_7541')
call_8173 = func_7540_call()
call_8174 = func_7540_call()
output = relay.Tuple([call_8158,call_8160,call_8173,])
output2 = relay.Tuple([call_8159,call_8161,call_8174,])
func_8185 = relay.Function([], output)
mod['func_8185'] = func_8185
mod = relay.transform.InferType()(mod)
mutated_mod['func_8185'] = func_8185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8185_call = mutated_mod.get_global_var('func_8185')
call_8186 = func_8185_call()
output = call_8186
func_8187 = relay.Function([], output)
mutated_mod['func_8187'] = func_8187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3011_call = mod.get_global_var('func_3011')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_8191 = func_3011_call()
call_8192 = func_3011_call()
func_1217_call = mod.get_global_var('func_1217')
func_1221_call = mutated_mod.get_global_var('func_1221')
const_8194 = relay.const([2.692741,6.992562,-3.066180,7.549548,-2.973032,9.294839,-8.507102,7.656792,4.618171,5.825225,-1.121538,-8.309910,1.679796,9.730361,-2.304444,1.770675,9.252823,1.695163,-2.182359,-7.294806,-4.247787,0.770976,6.810911,-5.179991,-0.952688,0.893571,-8.878664,1.950020,-2.365134,9.378356,-0.204161,6.980591,3.651872,3.659290,4.862415,-0.582658,5.691251,-6.194241,-8.348020,-4.562665,-5.987698,8.242003,5.045074,4.958279,9.610930,-4.261517,7.474901,0.204264,5.429472,-2.833058,6.292746,-9.063363,0.586367,3.994457,7.279707,-3.787908,9.776870,-1.319155,-5.019177,9.874643,-2.020131,3.717852,6.966911,-1.647320,-9.672717,1.137286,9.962363,-1.284665,-9.811018,-4.901678,5.220862,2.139666,2.291959,6.040351,9.385890,3.397047,8.601411,0.272667,-6.121741,1.507610,7.895615,-7.993719,-3.647358,3.375116,-1.143095,-3.245985,-0.148365,2.899347,9.446230,3.797629,7.607698,6.623224,-0.735391,7.955092,-4.464725,4.937102,8.434946,2.342835,-1.836440,-6.000667,-1.352843,1.631610,-9.090881,-1.003656,3.769696,5.986452,7.183684,7.983293,7.037994,-9.292490,7.734680,3.840595,4.272340,-1.322725,6.600879,-8.978227,2.239608,-0.275465,-3.174036,-4.052809,8.540361,-9.402896,-9.121779,-6.105205,-3.771360,9.095345,-7.084151,-8.860261,5.649807,1.294857,6.602560,6.174422,2.881407,7.163549,-3.417903,-4.715153,8.194243,-5.239352,-0.352550,4.024439,6.920728,9.908741,-6.435282,7.381992,-8.081121,-2.408854,5.332509,5.700745,-3.253925,-1.009040,-5.163633,-1.117896,-5.214661,9.099523,3.699436,7.713118,5.465390,-3.536356,3.125345,-7.727089,-8.478216,7.998938,-6.844388,4.687138,9.896206,9.913433,-5.189614,7.054789,9.221775,5.467673,-3.976257,2.358221,9.526161,9.156047,-9.809418,5.699714,-9.642045,-2.483089,5.685097,4.673078,6.819016,-9.341795,-1.030085,-8.973495,-7.258706,-1.387415,3.393481,-4.611969,1.703876,4.130390,7.638655,9.575180,2.790090,-0.617848,6.199407,-4.711569,7.649074,-5.030052,-6.600880,3.049947,-8.916146,7.356811,8.073813,7.190368,9.016593,-5.836346,1.884416,8.775696,7.926534,7.757666,5.961287,-3.767566,-3.869337,8.962517,2.095637,7.850669,-1.701469,2.511684,-6.320182,0.439846,5.055235,5.270982,0.850429,-8.974641,-6.547435,8.028498,8.712675,-8.666664,-1.536918,-3.046809,-3.856645,0.649442,1.206655,0.984388,6.121768,4.452610,-1.908255,2.066134,9.566017,0.553279], dtype = "float64")#candidate|8194|(240,)|const|float64
call_8193 = relay.TupleGetItem(func_1217_call(relay.reshape(call_8191.astype('bool'), [14, 8, 4]), relay.reshape(const_8194.astype('float64'), [240,]), ), 1)
call_8195 = relay.TupleGetItem(func_1221_call(relay.reshape(call_8191.astype('bool'), [14, 8, 4]), relay.reshape(const_8194.astype('float64'), [240,]), ), 1)
func_435_call = mod.get_global_var('func_435')
func_439_call = mutated_mod.get_global_var('func_439')
var_8201 = relay.var("var_8201", dtype = "float32", shape = (880,))#candidate|8201|(880,)|var|float32
call_8200 = relay.TupleGetItem(func_435_call(relay.reshape(var_8201.astype('float32'), [11, 10, 8]), relay.reshape(var_8201.astype('float32'), [11, 10, 8]), ), 1)
call_8202 = relay.TupleGetItem(func_439_call(relay.reshape(var_8201.astype('float32'), [11, 10, 8]), relay.reshape(var_8201.astype('float32'), [11, 10, 8]), ), 1)
output = relay.Tuple([call_8191,call_8193,const_8194,call_8200,var_8201,])
output2 = relay.Tuple([call_8192,call_8195,const_8194,call_8202,var_8201,])
func_8203 = relay.Function([var_8201,], output)
mod['func_8203'] = func_8203
mod = relay.transform.InferType()(mod)
mutated_mod['func_8203'] = func_8203
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8204 = relay.var("var_8204", dtype = "float32", shape = (880,))#candidate|8204|(880,)|var|float32
func_8203_call = mutated_mod.get_global_var('func_8203')
call_8205 = func_8203_call(var_8204)
output = call_8205
func_8206 = relay.Function([var_8204], output)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3502_call = mod.get_global_var('func_3502')
func_3504_call = mutated_mod.get_global_var('func_3504')
call_8208 = func_3502_call()
call_8209 = func_3502_call()
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_8218 = func_1240_call()
call_8219 = func_1240_call()
func_2323_call = mod.get_global_var('func_2323')
func_2327_call = mutated_mod.get_global_var('func_2327')
const_8225 = relay.const([1.016169,4.257316,-5.131522,1.032380,-7.217039,1.525849,4.947835,-9.039961,-1.371012,-5.552869,4.678188,-8.846981,-2.913559,-9.897814,-7.660379,-9.838595,1.134008,8.476175,-4.920231,6.380121,2.661047,3.901959,9.543692,-0.327904,-7.190859,6.269775,2.359625,-9.449829,-1.280326,5.311269,-7.696112,-3.956843,4.365277,6.742604,-5.796979,9.135665,-2.694140,0.685299,-1.316569,8.004286,-6.933652,3.029642,-0.527682,-0.863301,-5.486604,0.650227,2.306401,-4.485274,-8.077726,-2.159999,1.271737,-7.112071,-4.510021,6.997865,-5.665548,2.495707,7.434778,-4.683281,4.864378,-9.812352,-8.854698,-2.171323,0.160810,1.369973,-8.483360,-2.431563,7.638536,9.639586,-4.065753,-7.223355,3.750526,-3.996742,-9.008212,9.578726,7.324106,0.625317,9.607913,3.853282,8.593044,-0.920476,8.184437,8.434420,-3.772886,-8.775343,2.360467,9.049524,0.490652,0.184922,-5.911467,8.501645,-8.663252,7.726572,-9.358289,-0.421557,3.666692,7.199789,1.308209,3.633628,-6.341307,9.578569,8.708198,-0.341121,-3.412811,-3.730332,-3.923026,-4.698016,5.210598,9.630385,-6.618685,3.028628,-4.777466,-8.609528,8.589391,3.617365,-2.252302,9.022012,3.240834,-1.821815,1.908287,-9.383486,-8.138449,-9.943438,6.314022,2.763440,3.769452,2.399943,5.982047,2.158935,-9.832922,-5.168796,7.098429,-7.024547,-8.164202,-4.567868,8.699370,4.115285,0.208337,7.929500,0.142959,9.072324,5.877842,9.146037,-4.309795,4.635196,7.913681,9.118268,6.427865,-3.783635,-6.197895,6.009651,9.245117,5.015251,-6.878656,5.192456,9.350538,-6.500296,-7.193976,-4.702262,7.215671,8.602380,2.797039,2.792076,-3.745470,-5.371466,7.226825,-8.456742,7.433817,8.712813,5.705827,3.103525,8.722452,9.137957,9.557988,2.244102,-1.272540,-5.522229,1.829074,-5.865488,1.985309,6.217974,7.426652,8.262762,6.027178,-4.981948,-4.497499,-9.854978,-1.961655,4.554154,8.900706,-9.950665,4.258937,6.423216,-1.266862,-9.965331,6.090804,-2.816245,0.625987,3.314544,1.684193,5.077497,0.552359,6.202019,-9.025818,-9.691749,8.895731,8.345230,3.675699,-2.923085,-9.827721,2.170752,-8.960094,-7.051929,7.859580,-8.598696,-5.511382,-6.208321,9.923882,2.122743,-6.532927,6.844233,-1.229469,-3.343353,-9.182751,4.274171,2.048725,-4.814184,9.273775,-0.005293,-0.082549,6.025479,-8.952527,-1.930776,4.402247,3.094153,8.415322,-3.849344,4.841419,7.230810,9.797072,0.369941,5.501992,-5.627650,-1.679068,-2.108078,7.809784,3.951622,3.008969,-8.789533,9.010521,4.319819,-9.845195,-9.792471,-0.824539,5.848290,4.831163,7.130165,-1.315152,0.475493,-0.702973,6.118853,4.487745,8.251199,4.345411,9.022537,-3.374971,7.398029,-0.246340,-8.282117,-1.105445,-2.778282,-4.736065,-5.544260,7.029430,-4.638847,2.751610,-2.111476,-7.696537,-2.208237,4.813751,9.809102,-8.203075,-1.487816,-5.368945,8.039923,5.373709,-4.017798,4.458570,-3.804311,-7.117713,-6.839460,0.244967,-3.065474,4.272570,5.140123,1.389256,-5.226414,4.571150,-2.617965,1.283890,-0.110504,-5.816679,4.423308,-0.265455,-8.186213,-2.295306,-9.713115,4.773868,7.226686,4.137147,6.807148,6.426276,-6.879648,0.909143,2.394622,4.131336,3.170317,-3.729839,6.914631,-1.071149,-2.458499,0.711269,-3.906329,5.842683,7.967069,-0.987696,3.160997,-7.098530,6.075751,2.852306,-5.001857,-9.393613,-7.275166,-4.228810,4.956514,4.255728,9.716361,2.261227,-2.821777,-7.047299,8.231953,-7.253889,-4.834325,2.343963,-9.908384,-4.976610,4.390648,-6.332783,-3.687422,0.412524,-7.539440,2.704473,8.416738,6.860572,1.205037,9.710483,6.889623,-7.326766,-0.169004,4.979671,-5.771451,-7.963277,-9.362168,1.381543,8.143492,1.588601,3.422953,-0.785487,7.456317,-3.865797,8.624643,1.878288,-8.233421,-8.391389,2.413726,9.127647,-1.340290,5.219695,7.457112,0.311304,-6.009096,-3.435031,9.492019,-6.689748,-6.462554,1.937864,9.448761,-0.235045,-8.485083,-6.096232,-8.721931,8.837711,0.053455,-3.090805,1.255221,-3.822557,-9.669112,-6.832938,5.657632,-7.409861,3.730514,7.582094,-9.766751,-3.252254,-1.772844,3.688168,0.924954,9.683757,7.815085,8.831054,8.213193,-9.641105,-7.006467,5.171969,-9.356133,9.064724,-2.111804,-5.533872,6.561345,6.303374,5.244405,-8.089342,-2.220356,-5.586772,4.255687,-9.202939,6.150134,-0.258061,9.777788,1.320772,4.830489,-2.635962,6.904632,5.236793,9.545895,-5.988775,4.113276,2.944329,8.706088,4.780778,3.053313,4.944737,2.409905,-1.214141,-5.814635,-4.959031,8.395947,2.954822,5.829499,6.534922,1.663784,9.692907,-9.956053,-7.395240,-8.647623,9.964406,-7.010019,-0.538724,-3.916235,-9.211231,-3.261547,3.656074,1.055544,-1.156152,9.189188,-0.004377,-0.046677,9.264264,-9.220103,-0.110729,0.143438,5.153361,-1.469654,9.937507,-1.345619,4.397557,-7.041511,-3.609244,3.858193,-7.134896,-0.034357,-8.460653,0.990665,-7.337555,3.280856,-6.503924,-7.923321,-0.470934,-3.434252,0.824617,-3.997454,8.318489,6.173571,-4.898426,6.417988,3.525016,6.644368,-6.136741,7.526569,6.422234,6.801584,-3.759896,7.529979,-2.697618,-0.824112,-9.999125,5.852813,-4.542089,-4.631276,5.117462,0.857582,6.582287,-4.477624,1.753725,-1.173471,3.603047,4.677799,9.582817,-7.253857,-2.253339,-0.692195,4.733385,-5.679746,-4.274914,0.268918,-4.866149,4.295670,5.888234,2.690565,1.329894,6.281240,5.972517,-4.622251,4.429646,8.775797,-1.914060,2.221555,4.054391,7.868122,-8.335141,2.607319,4.971205,-2.501245,6.212963,-2.424641,-4.754674,9.197313,-1.956539,-9.207284,-8.377614,7.653596,5.277120,9.297967,-1.623368,1.285405,6.201208,-6.548615,9.215003,1.850809,-1.969841,0.031245,-9.040101,5.700041,9.585887,-3.914115,0.130606,-3.920371,-9.786868,9.269725,-7.754609,7.522859,6.623388,-2.290871,5.934262,6.669561,7.677401,-9.787385,7.185911,-5.320966,8.177346,7.776097,-0.367997,-0.410556,5.033504,-7.365194,-5.356475,3.573000,1.737398,-6.658942,3.554725,-4.128046,-5.356508,-2.118929,-5.657731,-5.251777,-1.880628,-7.386516,7.047851,1.921241,-6.919472,-8.125854,-0.338772,0.298258,-1.380550,-4.928365,3.544863,-6.731915,2.722623,-0.705621,-6.400465,4.300830,-3.402373,8.811868,-0.196921,-7.656166,-6.746677,7.257436,-3.103397,-3.530784,-1.731381,-5.372445,-1.105231,-2.767504,-3.801962,2.922421,6.846074,5.238012,4.479470,-1.639132,0.801332,-5.673949,6.108450,-5.587795,-0.017426,-2.146656,3.725008,3.676226,-8.452839,2.302078,-0.481188,1.075545,-7.899786,0.453148,2.864650,6.477768,-8.131872,8.701744,-1.469330,0.490956,-8.528067,2.100119,-4.709383,3.772063,-6.292703,8.488601,-5.041261,9.681902,5.394956,-8.716343,-8.014403,-4.314163,9.493241,-0.717647,3.655188,3.302172,-5.442280,-4.226165,8.066423,3.333138,-1.676619,-6.746662,5.761892,1.639237,-0.475064,6.021106,-0.376559,3.583943,4.086850,9.247106,4.582350,9.779164,7.728786,-3.280798,7.202671,4.445983,6.320443,-0.739177,4.364099,3.581129,6.193138,-9.715241,-9.054042,-6.471174,0.955782,8.221082,-9.848348,-7.704736,-8.087313,-0.998586,-5.133956,4.138836,6.524775,-3.009145,-5.181193,-1.284794,4.349068,1.248487,-5.317970,9.240989,9.931774,-6.240311,4.199541,3.779665,8.047403,-9.060348,3.013248,3.114841,7.910147,2.140916,-9.405678,-6.701800,-5.599373,3.407076,9.857732,4.641312,7.023287,-7.003719,-9.432750,-5.204729,4.223079,-9.880227,9.756804,4.906630,4.429401,-6.291388,-1.272818,0.339153,-9.249296,0.154841,-3.276905,-2.302635,-8.756129,-1.349704,-3.514972,-3.548880,0.685369,8.699137,7.007454,-3.450237,9.742784,-6.249846,4.767089,3.805668,-4.210299,6.569167,7.912676,6.418296,-5.671218,-4.197823,-3.676663,-4.825696,2.577464,-8.174344,-2.355147,-8.771798,4.451728,5.528426,-6.868637,-1.701073,8.350941,8.666150,4.534152,-5.976244,7.472845,2.760535,0.831084,2.717763,8.988489,4.283793,-9.548828,1.862169,-0.508282,-4.562051,4.588379,-5.763000,-6.808212,9.996458,-8.083262,5.901916,4.007113,8.448120,-8.509725,7.730068,2.624180,4.345769,-4.102700,2.338935,8.713101,-2.265987,4.345109,1.072816,-7.861803,9.108229,-2.147296,-3.809967,6.571769,7.850834,2.959923,8.821359,1.580606,-7.636918,-5.130719,6.301842,-1.938814,-5.490079,-0.781034,7.936551,1.011252,6.279272,-7.672905,6.107547,8.438220,8.136523,5.624179,1.060074,-4.276880,0.344102,-8.576099,-2.240578,-3.099299,-0.715273,1.346121,2.526591,-1.793815,-4.620032,6.223164,6.278700,-9.235732,3.945568,2.255493,6.763782,-8.692368,-6.820061,7.645475,4.010914,-6.468857,-4.379027,-6.916497,-6.930635,-9.915477,3.624161,-6.535881,-0.925170,1.248699,-2.601425,4.688065,-4.233289,-3.776338,-0.580570,-1.021912,0.623160,9.383524,-2.476715,-2.278848,-7.299730,4.553191,-7.703223,-5.429274,1.862681,-4.317589,9.241019,4.674819,1.080752,-4.285573,1.942237,-0.231694,1.591336,-6.028360,9.930430,-6.066608,8.206543], dtype = "float32")#candidate|8225|(880,)|const|float32
call_8224 = relay.TupleGetItem(func_2323_call(relay.reshape(call_8218.astype('float64'), [14, 8, 4]), relay.reshape(const_8225.astype('float32'), [880,]), ), 1)
call_8226 = relay.TupleGetItem(func_2327_call(relay.reshape(call_8218.astype('float64'), [14, 8, 4]), relay.reshape(const_8225.astype('float32'), [880,]), ), 1)
output = relay.Tuple([call_8208,call_8218,call_8224,const_8225,])
output2 = relay.Tuple([call_8209,call_8219,call_8226,const_8225,])
func_8232 = relay.Function([], output)
mod['func_8232'] = func_8232
mod = relay.transform.InferType()(mod)
output = func_8232()
func_8233 = relay.Function([], output)
mutated_mod['func_8233'] = func_8233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3309_call = mod.get_global_var('func_3309')
func_3310_call = mutated_mod.get_global_var('func_3310')
call_8242 = relay.TupleGetItem(func_3309_call(), 0)
call_8243 = relay.TupleGetItem(func_3310_call(), 0)
output = call_8242
output2 = call_8243
func_8246 = relay.Function([], output)
mod['func_8246'] = func_8246
mod = relay.transform.InferType()(mod)
mutated_mod['func_8246'] = func_8246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8246_call = mutated_mod.get_global_var('func_8246')
call_8247 = func_8246_call()
output = call_8247
func_8248 = relay.Function([], output)
mutated_mod['func_8248'] = func_8248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7621_call = mod.get_global_var('func_7621')
func_7622_call = mutated_mod.get_global_var('func_7622')
call_8249 = func_7621_call()
call_8250 = func_7621_call()
func_6091_call = mod.get_global_var('func_6091')
func_6092_call = mutated_mod.get_global_var('func_6092')
call_8301 = relay.TupleGetItem(func_6091_call(), 0)
call_8302 = relay.TupleGetItem(func_6092_call(), 0)
func_1757_call = mod.get_global_var('func_1757')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_8305 = func_1757_call()
call_8306 = func_1757_call()
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_8359 = relay.TupleGetItem(func_882_call(), 0)
call_8360 = relay.TupleGetItem(func_884_call(), 0)
output = relay.Tuple([call_8249,call_8301,call_8305,call_8359,])
output2 = relay.Tuple([call_8250,call_8302,call_8306,call_8360,])
func_8364 = relay.Function([], output)
mod['func_8364'] = func_8364
mod = relay.transform.InferType()(mod)
output = func_8364()
func_8365 = relay.Function([], output)
mutated_mod['func_8365'] = func_8365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7363_call = mod.get_global_var('func_7363')
func_7365_call = mutated_mod.get_global_var('func_7365')
call_8374 = func_7363_call()
call_8375 = func_7363_call()
output = relay.Tuple([call_8374,])
output2 = relay.Tuple([call_8375,])
func_8381 = relay.Function([], output)
mod['func_8381'] = func_8381
mod = relay.transform.InferType()(mod)
output = func_8381()
func_8382 = relay.Function([], output)
mutated_mod['func_8382'] = func_8382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2832_call = mod.get_global_var('func_2832')
func_2833_call = mutated_mod.get_global_var('func_2833')
call_8391 = relay.TupleGetItem(func_2832_call(), 0)
call_8392 = relay.TupleGetItem(func_2833_call(), 0)
func_5705_call = mod.get_global_var('func_5705')
func_5706_call = mutated_mod.get_global_var('func_5706')
call_8406 = func_5705_call()
call_8407 = func_5705_call()
func_7621_call = mod.get_global_var('func_7621')
func_7622_call = mutated_mod.get_global_var('func_7622')
call_8421 = func_7621_call()
call_8422 = func_7621_call()
output = relay.Tuple([call_8391,call_8406,call_8421,])
output2 = relay.Tuple([call_8392,call_8407,call_8422,])
func_8430 = relay.Function([], output)
mod['func_8430'] = func_8430
mod = relay.transform.InferType()(mod)
output = func_8430()
func_8431 = relay.Function([], output)
mutated_mod['func_8431'] = func_8431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8448 = relay.var("var_8448", dtype = "uint8", shape = (3, 12, 13))#candidate|8448|(3, 12, 13)|var|uint8
var_8449 = relay.var("var_8449", dtype = "uint8", shape = (3, 12, 13))#candidate|8449|(3, 12, 13)|var|uint8
bop_8450 = relay.minimum(var_8448.astype('uint8'), relay.reshape(var_8449.astype('uint8'), relay.shape_of(var_8448))) # shape=(3, 12, 13)
uop_8455 = relay.asin(var_8449.astype('float64')) # shape=(3, 12, 13)
output = relay.Tuple([bop_8450,uop_8455,])
output2 = relay.Tuple([bop_8450,uop_8455,])
func_8461 = relay.Function([var_8448,var_8449,], output)
mod['func_8461'] = func_8461
mod = relay.transform.InferType()(mod)
mutated_mod['func_8461'] = func_8461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8461_call = mutated_mod.get_global_var('func_8461')
var_8463 = relay.var("var_8463", dtype = "uint8", shape = (3, 12, 13))#candidate|8463|(3, 12, 13)|var|uint8
var_8464 = relay.var("var_8464", dtype = "uint8", shape = (3, 12, 13))#candidate|8464|(3, 12, 13)|var|uint8
call_8462 = func_8461_call(var_8463,var_8464,)
output = call_8462
func_8465 = relay.Function([var_8463,var_8464,], output)
mutated_mod['func_8465'] = func_8465
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8467 = relay.var("var_8467", dtype = "float64", shape = (12, 9, 4))#candidate|8467|(12, 9, 4)|var|float64
uop_8468 = relay.atan(var_8467.astype('float64')) # shape=(12, 9, 4)
func_569_call = mod.get_global_var('func_569')
func_572_call = mutated_mod.get_global_var('func_572')
const_8472 = relay.const([True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,False], dtype = "bool")#candidate|8472|(448,)|const|bool
call_8471 = relay.TupleGetItem(func_569_call(relay.reshape(const_8472.astype('bool'), [14, 8, 4])), 0)
call_8473 = relay.TupleGetItem(func_572_call(relay.reshape(const_8472.astype('bool'), [14, 8, 4])), 0)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_8476 = relay.TupleGetItem(func_735_call(), 0)
call_8477 = relay.TupleGetItem(func_737_call(), 0)
func_3997_call = mod.get_global_var('func_3997')
func_4000_call = mutated_mod.get_global_var('func_4000')
const_8479 = relay.const([-7.572770,4.961037,2.125621,-8.260405,6.000274,6.569663,-3.275706,-3.145122,3.575969,-5.099021,-8.147463,4.160135,-0.591906,-8.168617,-0.373064,-7.613514,-4.595806,-9.319457,-6.008815,8.356003,2.430028,7.591594,9.616021,-2.753523,-2.222002,2.469904,9.514340,-2.313164,-7.321012,-1.965131,8.996911,2.180843,-3.257658,-7.614847,-0.456929,-5.553790,-0.484182,-7.454337,-3.694637,-1.329372,4.902092,0.936037,1.410909,1.260271,-0.216691,-1.132817,-4.504305,-4.764436,8.399512,6.477256,-7.239835,7.013940,2.904359,-0.356107,2.066559,8.738992,3.344194,6.800520,-5.677354,-2.799154,-7.544946,-5.510274,4.606028,7.856245,9.067543,-6.366083,6.091959,-0.921403,5.566354,-9.498675,-3.604744,-2.480676,-6.045924,-6.827213,-7.213166,-9.091830,5.066419,3.155747,3.127604,6.175403,-8.811972,-6.146478,-2.283460,-5.184705,9.329815,-2.681164,-5.473349,4.237314,-8.499457,8.081736,6.597640,-3.408211,3.614168,7.544242,-6.378088,8.664933,-2.895434,-9.996659,4.146837,4.005798,6.644051,-6.093441,-3.683123,7.585703,5.815600,1.050624,-4.262835,8.443931,2.588238,-0.231095,5.899341,-9.973340,1.308134,-4.160055,-0.460720,1.301722,6.576524,9.294750,-7.603016,6.953323,-0.753875,-1.226782,-5.383599,-0.032488,-2.287170,0.069947,-5.989184,9.154301,7.609968,-0.420863,7.425680,8.155735,1.307425,-4.816669,0.502350,6.613452,-5.825525,-3.818563,5.649302,2.491376,6.106163,-9.753194,-8.333550,6.734276,9.377354,9.958811,-4.570147,-4.885407,-0.788458,9.441374,-8.758916,8.580671,-3.606355,7.702084,-3.684992,6.100165,8.878220,8.969247,3.815665,3.662532,5.956214,-9.485874,-9.791716,7.803139,8.929637,-4.849179,-4.287319,4.281165,-2.445492,-0.132429,6.510834,-4.836427,0.308164,-4.139224,3.488155,-8.810862,0.154563,-0.669456,1.413988,-0.725649,-3.160956,-8.688747,-4.115929,6.246411,-7.366698,5.358688,6.251460,-4.038492,5.956444,6.714736,0.670267,9.777946,-4.644407,-7.036374,-8.792470,6.241676,2.643504,2.397313,3.233646,-6.034632,-0.002585,2.959141,-1.947563,2.951714,-9.141932,-4.792281,-2.819963,-4.154542,2.124036,-3.573890,0.560660,-1.679765,7.146613,-1.540877,-3.564214,-0.005823,-7.969178,-0.478270,7.252384,2.001397,-2.425253,8.183804,5.913035,-8.306397,-6.433853,-8.482937,-1.817448,6.073022,-3.004239,-5.086597,-5.083628,-1.307790,-0.218513,8.259830,-2.796779,7.788986,-9.583556,9.074847,9.463033,-7.944293,-2.655755,6.035779,2.926323,-6.983918,1.496457,-1.251989,0.796748,-6.548201,4.255933,2.367551,-2.556999,7.846443,-7.216507,9.062505,-7.980911,7.761083,-3.021169,7.300245,8.408892,-4.552590,-1.992115,5.122545,1.501533,4.844064,8.115310,-4.824604,7.982190,4.567360,-0.984448,6.644546,-8.711487,5.113644,-3.926430,2.864478,-1.241826,-1.360314,-1.521677,-3.831730,6.238161,6.807931,-4.395997,1.970470,2.855110,6.132436,4.161465,-9.095129,-3.537731,-3.152907,-2.669937,-8.014933,8.079064,9.743804,-8.002395,0.251245,8.011787,4.242849,-8.953103,9.772776,7.994962,8.578990,-4.871702,-0.975200,7.889463,7.105262,-8.750895,-6.816986,-6.370849,-6.183515,6.579338,-5.029747,-1.768183,6.964274,-7.736472,-2.145946,2.331655,-5.107240,5.752992,-2.511717,-1.379281,-3.367695,-9.879640,-4.334987,-1.342024,5.697394,8.957598,-1.890898,0.620827,-1.488297,-5.237983,4.160293,5.564735,1.867627,4.245760,4.339831,9.971340,-5.652950,4.855843,-0.356561,2.248389,2.855689,-1.397911,-9.638393,6.728061,9.435727,7.596046,-7.967192,8.612360,4.729628,5.737806,-4.649035,-7.535993,-1.699995,3.840485,8.362021,1.476015,2.159636,-3.104337,8.983463,4.554220,-6.804035,-9.710509,0.311026,-5.931104,-7.751780,7.529578,8.529620,9.927597,6.498175,-5.472805,-2.131805,-6.147627,8.164990,1.795486,-0.076837,-5.901550,-6.706602,3.247825,-6.753339,-4.705483,-4.970892,3.346911,-9.586477,2.518882,4.248309,-6.201695,5.313424,-0.913265,-2.246246,-0.196345,-3.741395,8.296294,1.715995,-0.431833,-0.410517,-4.306063,-6.732296,-2.161775,-9.666819,4.282716,-5.063233,6.124907,-5.254922,-2.801876,-2.792765,7.843983,2.289525,5.983288,-5.418865,-8.054688,-6.324801,6.386213,-4.081985,2.344031,2.398034,6.727829,7.385165,-8.705735,-1.711411,-0.629554,6.932178,3.713031,-1.838353,8.331094,-3.423877,8.436947,-3.258366,2.374296,3.548762,9.060697,6.883745,-3.600206,-7.474056,-7.049034,2.498399,3.769567,5.604019,-8.155876,4.268822,-7.148798,5.775106,-2.560699,-3.352855,8.937302,3.065795,-2.869845,6.437227,1.306160,7.077712,-6.841127,-2.608518,9.463465,-9.451196,9.512976,2.239264,6.343031,6.999776,-8.357374,7.445060,0.844741,9.714508,-3.293800,-4.545236,-5.653004,6.396073,5.940146,-4.753061,8.118700,-5.809450,-3.445519,-6.544282,-8.912695,9.531521,4.660431,-9.059948,7.890281,6.352883,-7.397000,5.247908,9.447861,6.317102,-1.771214,-9.767315,-2.360827,-5.518039,-0.852033,-8.180842,0.122637,-4.590827,3.183188,2.603971,-9.385896,-0.008205,6.502758,5.322924,-7.312756,3.776473,-0.734642,9.373597,-3.951815,7.904796,-6.074997,6.510879,7.613264,7.049938,9.937463,-2.818182,4.959030,-0.480977,-3.528524,0.861520,3.846372,-1.807514,-9.717217,-5.237586,6.251899,-2.115992,-0.492298,3.652043,7.353687,-8.193380,-3.249050,-6.889720,8.104396,-1.966485,-7.422563,-3.803806,-2.279636,9.112635,-5.441083,0.547966,8.471167,-5.105056,9.870811,4.840572,-8.577837,4.357402,-7.078217,-3.397129,0.110475,-9.829744,-0.670004,6.865670,1.163238,-7.660045,-9.696175,2.980695,7.191210,7.950644,-7.201201,2.760712,-9.148518,1.391562,-0.826475,-5.640832,-2.933940,2.394510,-7.255742,5.990636,5.210950,2.167995,6.099899,3.405872,-6.954210,6.912724,2.936925,8.718665,-0.583672,7.500074,-9.072118,-8.605028,-0.662552,-6.309776,-3.909369,-8.749659,7.097935,3.303086,-6.831540,1.377155,-6.384218,0.265075,4.885651,6.813084,2.362415,-6.359777,0.918639,-9.442806,-9.436677,-5.498922,-0.568528,-9.532834,-7.582755,-2.524364,-1.838913,-9.011630,2.284564,-9.866410,-3.291216,-5.877679,-1.023032,-2.963282,8.874038,5.009751,7.244305,-0.987122,-5.529441,9.443132,-6.008483,-8.884038,4.004602,7.935838,-1.059254,7.289605,-6.752990,9.549536,-1.883730,-3.907478,-3.166589,3.556210,3.430112,-3.727043,-5.374568,-2.631980,9.964768,3.890046,2.137754,9.012221,-6.324314,2.610071,-7.054818,-0.538549,-0.838663,-8.772853,-9.144916,-3.011722,9.449122,-4.289185,-3.552419,2.125049,1.429567,-1.683135,7.734487,-1.370315,-8.622708,-2.596826,-2.501572,6.983271,2.561368,-9.800829,8.204101,4.067372,1.431859,-1.238670,8.057222,7.453087,-1.445906,1.407132,-4.693152,6.692549,1.169549,2.414677,-4.495315,-2.414220,0.561362,-7.808665,0.242267,5.825156,3.721204,-3.759992,8.103225,9.941283,7.854746,-5.281737,-3.586185,-0.469270,3.450527,-1.190602,-4.767924,-1.946389,9.903832,-9.057426,-4.363698,3.813211,5.586557,-3.071421,3.362640,-9.713462,6.593300,-7.817376,5.890189,0.132387,1.034691,-9.177591,1.944638,8.130353,5.744087,2.707150,9.693602,2.513869,9.177466,-0.141246,0.951918,9.679222,5.022832,4.201790,4.846114,0.745791,-5.033274,-5.971427,-4.569397,-1.002768,-3.199050,-2.583976,-3.259316,-3.347563,3.467658,-4.220858,-3.449895,9.674363,-1.284607,-4.943051,-3.699770,-3.028658,4.095113,-2.005966,-4.752045,-5.295029,-5.520875,-1.556054,-1.902486,-5.102242,8.026826,4.055292,3.044814,1.235906,1.553491,5.705447,-1.156550,-0.985556,-6.037151,9.011587,6.831941,5.956474,-9.414642,-0.193233,1.150727,3.652128,0.804442,-5.576529,0.947920,-1.330256,0.875875,-2.763912,2.414114,4.518236,3.221824,-8.346605,-5.603547,1.728784,-9.755481,-6.886993,-2.181911,-4.417826,-1.386565,-5.120566,0.876157,-2.606911,-2.243680,-5.108183,9.522527,-2.677603,-5.792212,3.558113,-5.471924,-6.303669,-0.111697,-9.466591,-7.823682,-1.680441,0.635881,-4.177929,-4.794284,2.079645,-4.611963,-8.731533,-4.123999,-0.433638,-5.866831,3.295111,-8.201701,8.913158,-9.133458,-1.879675,-7.533482,1.982534,4.958053,-3.877855,-9.960703,1.511912,6.138121,-7.618089,-0.459826,4.509472,-9.531558,9.972533,-1.134269,7.662846,1.194113,2.829357,1.978563,9.648222,-1.399967,-0.864047,-1.093531,7.105529,1.842726,9.514696,1.310161,-7.009957,1.193567,-4.843370,-9.910148,6.173127,6.140801,-7.587812,9.608774,-0.715316,6.127853,5.750325,-8.077150,-9.670956,-3.064191,3.044563,-9.387782,-9.389239,2.865604,5.066800,-4.814484,8.579320,1.628142,-3.704367,-0.002486,-9.694265,9.371355,6.746927,1.874701,-1.030345,5.441900,0.404252,3.808269,3.520614,-5.713204,5.223342,6.668446,9.529485,-7.950802,-3.927164,-5.787139,-5.768271,-3.892256,4.528296,6.846410,7.576229,6.819638,-6.506670,-3.816397,7.044487,-2.674538,-0.736570,-2.970711,-7.591386,2.457041,5.239548,-5.685982,-5.694763,2.827155,-5.447801,6.944184,9.722950,-2.868338,8.878726], dtype = "float32")#candidate|8479|(880,)|const|float32
call_8478 = relay.TupleGetItem(func_3997_call(relay.reshape(const_8479.astype('float32'), [880,])), 3)
call_8480 = relay.TupleGetItem(func_4000_call(relay.reshape(const_8479.astype('float32'), [880,])), 3)
bop_8481 = relay.greater(uop_8468.astype('bool'), relay.reshape(var_8467.astype('bool'), relay.shape_of(uop_8468))) # shape=(12, 9, 4)
output = relay.Tuple([call_8471,const_8472,call_8476,call_8478,const_8479,bop_8481,])
output2 = relay.Tuple([call_8473,const_8472,call_8477,call_8480,const_8479,bop_8481,])
func_8492 = relay.Function([var_8467,], output)
mod['func_8492'] = func_8492
mod = relay.transform.InferType()(mod)
var_8493 = relay.var("var_8493", dtype = "float64", shape = (12, 9, 4))#candidate|8493|(12, 9, 4)|var|float64
output = func_8492(var_8493)
func_8494 = relay.Function([var_8493], output)
mutated_mod['func_8494'] = func_8494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1800_call = mod.get_global_var('func_1800')
func_1801_call = mutated_mod.get_global_var('func_1801')
call_8564 = relay.TupleGetItem(func_1800_call(), 0)
call_8565 = relay.TupleGetItem(func_1801_call(), 0)
output = relay.Tuple([call_8564,])
output2 = relay.Tuple([call_8565,])
func_8573 = relay.Function([], output)
mod['func_8573'] = func_8573
mod = relay.transform.InferType()(mod)
mutated_mod['func_8573'] = func_8573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8573_call = mutated_mod.get_global_var('func_8573')
call_8574 = func_8573_call()
output = call_8574
func_8575 = relay.Function([], output)
mutated_mod['func_8575'] = func_8575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1743_call = mod.get_global_var('func_1743')
func_1745_call = mutated_mod.get_global_var('func_1745')
call_8582 = relay.TupleGetItem(func_1743_call(), 1)
call_8583 = relay.TupleGetItem(func_1745_call(), 1)
output = relay.Tuple([call_8582,])
output2 = relay.Tuple([call_8583,])
func_8596 = relay.Function([], output)
mod['func_8596'] = func_8596
mod = relay.transform.InferType()(mod)
output = func_8596()
func_8597 = relay.Function([], output)
mutated_mod['func_8597'] = func_8597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_108_call = mod.get_global_var('func_108')
func_110_call = mutated_mod.get_global_var('func_110')
call_8614 = relay.TupleGetItem(func_108_call(), 0)
call_8615 = relay.TupleGetItem(func_110_call(), 0)
func_882_call = mod.get_global_var('func_882')
func_884_call = mutated_mod.get_global_var('func_884')
call_8617 = relay.TupleGetItem(func_882_call(), 0)
call_8618 = relay.TupleGetItem(func_884_call(), 0)
output = relay.Tuple([call_8614,call_8617,])
output2 = relay.Tuple([call_8615,call_8618,])
func_8647 = relay.Function([], output)
mod['func_8647'] = func_8647
mod = relay.transform.InferType()(mod)
mutated_mod['func_8647'] = func_8647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8647_call = mutated_mod.get_global_var('func_8647')
call_8648 = func_8647_call()
output = call_8648
func_8649 = relay.Function([], output)
mutated_mod['func_8649'] = func_8649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8430_call = mod.get_global_var('func_8430')
func_8431_call = mutated_mod.get_global_var('func_8431')
call_8691 = relay.TupleGetItem(func_8430_call(), 1)
call_8692 = relay.TupleGetItem(func_8431_call(), 1)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_8718 = relay.TupleGetItem(func_1072_call(), 1)
call_8719 = relay.TupleGetItem(func_1073_call(), 1)
output = relay.Tuple([call_8691,call_8718,])
output2 = relay.Tuple([call_8692,call_8719,])
func_8723 = relay.Function([], output)
mod['func_8723'] = func_8723
mod = relay.transform.InferType()(mod)
mutated_mod['func_8723'] = func_8723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8723_call = mutated_mod.get_global_var('func_8723')
call_8724 = func_8723_call()
output = call_8724
func_8725 = relay.Function([], output)
mutated_mod['func_8725'] = func_8725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8381_call = mod.get_global_var('func_8381')
func_8382_call = mutated_mod.get_global_var('func_8382')
call_8732 = relay.TupleGetItem(func_8381_call(), 0)
call_8733 = relay.TupleGetItem(func_8382_call(), 0)
output = call_8732
output2 = call_8733
func_8735 = relay.Function([], output)
mod['func_8735'] = func_8735
mod = relay.transform.InferType()(mod)
mutated_mod['func_8735'] = func_8735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8735_call = mutated_mod.get_global_var('func_8735')
call_8736 = func_8735_call()
output = call_8736
func_8737 = relay.Function([], output)
mutated_mod['func_8737'] = func_8737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7450_call = mod.get_global_var('func_7450')
func_7451_call = mutated_mod.get_global_var('func_7451')
call_8886 = func_7450_call()
call_8887 = func_7450_call()
func_1148_call = mod.get_global_var('func_1148')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_8893 = func_1148_call()
call_8894 = func_1148_call()
output = relay.Tuple([call_8886,call_8893,])
output2 = relay.Tuple([call_8887,call_8894,])
func_8902 = relay.Function([], output)
mod['func_8902'] = func_8902
mod = relay.transform.InferType()(mod)
mutated_mod['func_8902'] = func_8902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8902_call = mutated_mod.get_global_var('func_8902')
call_8903 = func_8902_call()
output = call_8903
func_8904 = relay.Function([], output)
mutated_mod['func_8904'] = func_8904
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8907 = relay.const([[[-5.247352,7.138288,-9.091293,0.917220,4.612141,8.307710,-2.854540,3.580186,-1.101960,-8.656072],[0.536826,9.470918,-1.724347,-0.621794,-2.016992,4.151626,-3.106923,-0.581847,0.500986,-2.219486],[6.941243,-3.312789,-5.215523,-5.981530,-4.092703,-5.385759,4.662348,-8.099402,4.850734,-4.222339],[-1.749643,-6.442371,-0.648098,4.271446,1.853003,3.954877,3.051825,-3.199800,5.282909,-2.171391],[6.153120,8.628826,-0.579902,4.066616,7.829833,9.870779,1.903336,-1.613244,6.148151,-6.210093],[4.523265,7.196466,2.654616,-2.700720,-3.578145,-6.426031,2.174049,-0.453049,7.245149,3.622139],[5.296168,-2.220446,1.427368,6.140492,-3.898439,9.876783,2.863244,-5.145513,-5.128175,3.119559],[4.168642,-4.936771,-8.031621,-6.359183,-1.078900,-1.561377,4.935945,2.572087,5.632778,1.366345],[-2.315361,-9.713716,8.680545,-8.895880,4.414022,-8.354235,-6.577893,-4.054687,1.728251,-3.653747],[-0.567718,3.845821,-0.788636,-2.734285,9.054039,5.547145,-5.363629,5.995828,5.438605,8.604652],[-7.947097,5.813549,2.425875,6.647240,0.843971,-1.324773,-9.162146,9.678029,-4.261524,-6.339972],[9.461035,7.752072,0.889934,2.798578,8.523493,-7.104554,-6.099936,-7.457173,4.265664,-8.106450],[2.524989,-6.621608,-9.004708,-9.307195,-8.007999,0.891780,1.790748,4.035157,9.916927,2.063651],[-0.009635,-7.186019,3.203556,-6.354868,-6.849865,1.440280,3.464334,7.967415,0.787760,6.180000],[9.837875,1.091092,3.181810,5.159298,6.316913,7.521046,-7.959592,-5.873910,-1.295383,-1.300376],[0.028056,2.860089,-7.168777,7.543485,-7.713364,1.830137,1.528713,-1.424726,6.555048,4.244850]],[[-8.232046,-4.552158,2.825718,3.205056,3.271718,-8.869537,2.759255,-6.467109,3.005615,-9.846007],[-5.436122,3.739278,-2.850848,-2.105737,6.520857,8.801564,3.725962,0.600109,-3.661244,-8.841437],[-3.214396,1.522543,-0.251754,6.275357,4.178096,-1.671999,7.134740,5.821178,0.707216,-3.242619],[5.062173,2.624644,9.094920,7.764736,8.210563,-8.249359,0.860159,4.811225,9.210830,0.053959],[-3.476578,-3.195226,7.229535,-4.122839,4.182837,4.887108,-8.966665,5.086092,0.963162,2.681734],[1.993945,1.596187,5.664765,-8.442883,8.270030,8.374998,8.047156,-0.114487,9.348779,-2.623004],[8.572935,-2.255094,-7.155452,2.947662,-8.096477,-8.330207,-9.663212,-9.391832,-6.286381,-0.706690],[-1.392846,-3.288392,5.769797,-6.896474,9.144572,-0.932499,6.551160,-9.571859,-3.298052,0.445592],[-6.669246,-0.535328,2.034969,1.645434,-1.747006,-6.647611,0.520112,-3.169184,3.294429,-9.529859],[4.508295,7.789985,9.520635,-4.855672,0.442838,-4.031266,6.674966,7.842914,-7.024337,9.175905],[-8.836069,1.342819,-7.849738,7.846488,9.987101,-8.554784,-9.946105,6.706486,5.781953,8.390300],[8.255965,-6.776971,9.434794,-8.998476,-8.259595,-1.142562,3.673289,3.995517,0.092669,2.900728],[-5.165082,-4.167707,3.448180,-6.423296,9.761126,9.849829,8.115099,-9.521840,4.858327,-0.273189],[-5.050976,4.063499,9.201201,0.465206,3.188219,9.767157,-0.599860,-4.267602,2.032074,-6.247262],[-4.416409,1.656186,7.003186,-5.062022,-8.528223,1.187233,9.698323,-8.444232,2.836489,-5.656137],[-3.494598,-0.440643,1.195789,-2.235031,4.112173,5.149886,5.873726,9.209420,-9.561815,5.369073]],[[3.937405,6.456801,6.437327,2.790552,7.264783,8.586858,1.291026,-1.927505,-9.192863,3.995971],[5.250621,-9.259639,8.328248,-0.627624,7.765822,0.090438,-3.570361,-2.499167,-6.156044,-7.688787],[1.324341,-6.336643,4.127213,1.810377,8.323650,6.635950,0.817705,3.444977,0.322676,3.933272],[-8.249773,9.060734,3.552071,-5.350499,2.188659,-9.562910,1.443314,6.464439,7.225040,-8.228926],[8.501699,-0.523162,9.785932,-4.282062,8.354592,-9.576776,-6.479225,-1.055226,6.728778,7.385768],[4.436225,8.235228,-5.864123,0.708178,0.963723,1.812664,0.652330,9.720322,1.766464,8.688046],[6.358733,-1.386401,-2.569554,-0.127556,-2.672614,-1.410591,9.997774,-8.849598,7.730515,4.055995],[6.279606,5.260342,-4.105596,-4.528464,-0.718359,-5.708812,5.792559,4.922260,8.168079,7.446097],[-1.043237,7.851239,8.806491,8.682979,9.410391,1.689229,6.819401,6.549648,0.678175,-7.245243],[-6.371587,-1.258264,0.748355,1.481358,9.633689,-2.680785,-3.193817,1.750108,0.938331,-6.587290],[9.666489,-4.414196,3.203613,9.022373,5.948665,-7.241011,-5.415848,3.248376,9.301656,5.748879],[6.572737,-1.512099,7.517145,8.401771,-1.166757,-9.894083,6.267275,5.776766,-8.059123,2.593399],[-6.114423,4.173420,-4.075209,-3.443960,0.024550,-0.962117,-4.027910,9.645855,-4.914752,-1.502187],[-6.408239,3.696119,0.450425,-7.288687,2.227113,1.185000,-7.069452,-7.323521,8.763393,-0.155023],[-6.703560,2.009092,8.793776,5.761379,0.948601,-2.127079,-5.347252,1.496428,-5.165307,7.450800],[-1.457347,3.842885,-3.206111,4.362737,2.267064,-8.714273,4.546121,-8.704491,-3.665525,-9.849672]],[[6.207493,-3.609243,-4.383366,-9.493492,2.368055,-7.931975,-7.067843,-6.330973,-0.557286,3.588279],[1.453872,3.991195,1.511685,8.670106,8.230804,-5.269750,1.576572,-8.766546,-4.587033,-0.565926],[7.793744,8.050579,1.975378,-5.975033,-8.330171,7.054269,7.714859,-2.121581,-2.365388,6.118616],[8.038584,-6.024324,-1.526751,0.278411,6.396537,-0.725785,-7.375416,4.228632,-8.930021,3.144454],[1.028637,-8.455987,-1.568160,1.741081,4.695465,-5.300607,-0.190915,9.446280,-5.056011,-1.049106],[-7.431000,-1.311930,-3.964075,-6.921304,5.431235,3.120247,-4.215128,8.122071,-3.676900,4.068066],[1.131578,7.254455,2.040874,-4.369625,0.340152,7.199421,-9.612650,-1.333715,6.470303,3.365829],[6.856614,9.114735,-5.085899,-3.976651,-5.467402,-6.846900,3.522850,8.147423,-3.978332,-4.190383],[-0.834510,-7.737612,4.221076,-8.996951,0.354595,7.083355,-5.048798,4.099724,-3.937747,-7.105740],[9.755680,-0.128266,-4.139087,3.984824,-7.390919,-3.145385,-9.881512,8.466423,7.712156,-7.277728],[2.243996,2.819960,7.812537,-5.005386,-8.742311,-6.235145,-5.027825,1.391294,-5.783757,3.717853],[-4.648506,-9.166050,-5.974451,9.599186,8.280659,2.007595,6.206270,-1.918509,1.943410,-8.122267],[1.837829,0.477598,-5.533795,-1.195057,-4.225767,7.259941,6.603145,5.897533,6.669970,-3.298562],[-6.904676,2.374665,-2.002400,-6.156191,-0.499775,-9.907548,9.170943,2.882999,-2.723394,4.508309],[-4.117033,9.831130,-8.546185,5.497425,6.116618,-7.496860,8.657977,-6.048639,5.644292,1.529457],[2.603563,-1.774547,-5.556502,-8.727332,0.233889,4.920629,-7.000836,-1.437112,6.857187,-7.123893]],[[4.652251,-0.469506,-1.730736,-7.556660,-5.343277,-6.746196,7.081216,-8.171758,-1.147475,-1.783113],[-1.265045,2.441845,6.378057,5.337765,-2.648004,9.111093,-2.536012,-0.676376,-0.869137,1.798893],[4.441570,1.004189,-7.623389,-6.943726,-6.093349,-5.351510,-5.313499,-5.090386,5.373877,-6.461375],[6.003569,5.101072,6.196916,0.025587,8.785218,-2.829932,-0.155995,7.357878,-1.816889,6.057089],[5.316399,7.652420,-6.231180,0.571116,-6.752532,9.023356,1.502103,3.793677,-7.997815,1.822465],[4.792446,-4.177304,3.431907,-5.429976,7.442939,-3.426001,-7.304515,-7.153893,4.081020,-1.695214],[3.038977,-0.199955,4.963756,-2.423379,-1.757352,0.832173,1.750186,3.918527,1.464295,-8.663498],[5.491308,3.351836,2.095142,-6.691016,2.350929,-9.741466,-6.796227,-1.129768,-4.940718,-1.173610],[-4.929556,1.354595,0.511511,-5.398923,-9.355924,-3.197096,8.767317,9.968747,0.488278,-3.619555],[3.623036,-1.581991,0.498305,3.424898,0.439312,-5.208835,6.458613,3.128150,-9.679068,8.566068],[1.093532,-2.039536,-3.461914,7.167307,-2.380693,-7.448465,-3.957935,8.026270,4.769790,0.669700],[-5.700162,-3.948210,7.964469,6.754788,0.853266,5.017529,-2.340072,-6.790107,9.316382,-4.821848],[6.719857,2.125334,0.314358,9.264856,2.866032,6.664348,-5.724665,0.257777,-4.970389,7.188693],[-4.455495,-2.996952,-6.659429,6.392483,-2.780984,7.040036,-9.235275,1.615049,-6.935134,9.156074],[6.730314,2.747228,-8.225069,-2.395628,8.541146,5.389738,-6.660824,-9.765394,-2.089129,-1.452572],[-2.441062,-1.077016,3.523587,-4.633422,-4.053410,9.868235,7.160404,7.229610,-9.555776,-9.603453]],[[6.962760,7.217125,5.039583,-9.108589,1.274631,-4.484529,3.548666,-8.081535,-8.016721,-1.839017],[-7.808655,-6.784067,-5.183740,-0.421726,8.027303,9.947819,-7.822284,-1.671606,-7.034768,5.946755],[-1.589676,4.962281,-5.780792,-3.727960,1.359845,2.303257,-3.140641,8.571376,1.162535,2.602657],[-8.722421,7.865398,4.061351,-1.682506,-8.021451,5.765942,1.076926,-8.818184,3.596587,-5.369255],[4.590724,-1.857786,5.830908,8.910574,6.191782,-8.557643,8.571596,-4.498172,1.338776,-2.327035],[-0.898197,-0.535356,6.656788,3.558228,2.518569,0.122169,2.972028,9.097333,4.867047,8.169970],[7.499590,-1.441971,2.991490,-9.491603,6.455327,0.185400,-5.121497,1.893728,-1.247718,-0.643073],[-6.714970,3.988261,-6.197638,-1.975881,7.039620,-0.471978,9.041234,4.402181,-3.600258,-6.993847],[-3.910962,9.408851,7.440164,-1.994545,-1.396489,-2.372119,-6.509008,-6.616874,-5.571085,-3.366967],[5.849581,-5.787764,7.742527,8.242674,5.324648,3.655681,5.890523,4.961834,6.711469,1.758705],[-4.436104,-4.256155,2.443444,0.168864,-5.219235,2.240565,5.955027,-3.188490,6.964891,-5.437790],[6.307334,-9.544330,-1.564934,-8.924428,-4.818925,1.565067,1.865024,8.184651,0.728696,-7.934211],[9.711200,4.712222,2.629667,4.699795,3.691593,-4.678015,-9.619484,-2.328616,-1.541583,-5.029513],[-8.010913,7.977086,-5.143332,-3.755545,-7.695626,1.727833,-8.428321,-0.694804,-0.258651,-3.649802],[5.591792,7.324827,9.019081,-3.784340,-3.838531,-8.109642,0.972883,-6.617905,0.673195,2.516276],[9.063699,4.014708,3.795998,7.341982,6.199505,6.132800,-2.777449,-4.419518,-1.147531,0.602547]],[[-2.708296,3.296991,-9.245715,9.646876,-4.308016,5.795756,6.363189,1.035274,-4.804303,-8.863330],[-6.512553,-2.481614,-2.903074,5.842713,1.603851,7.291089,-3.884969,1.332119,-5.565596,-1.578240],[6.149743,-0.225033,-5.096983,9.004529,4.045313,5.470051,-2.853471,-0.958748,-6.203036,9.221974],[3.766587,4.741037,-3.323868,-1.577435,4.552321,9.613920,-3.984199,8.067936,-3.477753,4.015428],[2.501822,1.213516,-1.797543,-8.235160,8.405091,-4.104204,2.035709,9.031456,9.813701,-9.283898],[-2.284710,0.393728,-9.370377,-7.179349,-7.798680,-9.664897,-2.893519,0.393087,5.918346,8.184503],[2.834933,2.926701,-6.771934,-2.537211,-5.969119,-5.589059,3.027244,7.594944,4.625323,-0.758912],[5.769299,7.289640,-2.016737,-6.470307,-1.800873,7.789593,-2.976234,-0.612961,1.633089,-2.753993],[-9.638691,-1.078811,-9.545217,6.594332,5.761126,0.249948,-0.041257,-5.544549,8.476512,-9.836699],[3.845324,-1.661857,3.480214,-5.694016,2.406462,-9.999403,0.847822,3.782540,8.920431,8.641865],[-4.779667,6.855410,0.875290,-8.571453,0.841057,8.246358,-2.871637,-1.358030,-6.719330,-0.544082],[4.520671,8.587307,8.454114,-2.786795,3.544983,-2.672749,6.899519,-3.825458,8.167946,2.268944],[-2.538608,1.407847,-0.337491,-8.692116,-7.576714,7.453232,8.685206,8.181538,7.325098,1.570930],[1.302569,1.080718,-9.114685,-3.626683,-6.216410,-5.532724,-2.476303,7.098420,0.805198,4.296935],[-8.597836,2.489226,-6.453717,-2.876724,-3.856476,-5.175884,6.096672,-8.615533,-7.525067,-3.635746],[4.794665,8.255158,-6.067747,-1.598433,-2.481835,-0.217935,-8.307210,-7.075361,-6.339967,1.366124]],[[2.481897,-9.378192,0.578219,-6.057768,7.829371,-1.700268,5.554062,-0.470568,-3.003848,6.697179],[7.910351,6.406754,9.904320,-8.806016,-8.507908,-4.790961,7.329079,9.877510,-7.876692,-1.554267],[-8.552679,-3.714407,-2.831011,6.520863,8.876594,7.370059,-5.634259,8.955915,0.495661,2.844926],[2.764540,1.757595,9.433324,3.355111,-1.544731,6.283312,-5.345501,-4.613887,4.981990,5.880852],[-6.879132,4.691695,1.280669,-1.361632,-4.360974,-3.235641,0.149638,-9.941803,-8.855291,-6.039903],[-3.477778,2.322893,3.069199,0.224326,-3.431708,-5.236868,-4.402598,0.106540,-1.463230,-9.631926],[-2.532917,-5.490901,-2.351257,-5.986771,-8.597501,4.803081,-8.803495,0.325190,-4.799579,-6.145927],[9.011981,5.494450,-8.547031,2.789226,-2.521214,4.828391,-1.390512,-3.055259,1.853124,-5.591606],[-1.185326,-6.863718,-3.432691,-7.097999,-6.663830,5.895705,8.194869,9.035019,-2.753202,-3.350116],[-8.792211,2.061295,8.657832,8.853767,-5.738842,-8.535400,7.347434,6.863971,-2.113339,-9.544500],[5.799846,-8.944552,-8.810969,-5.126655,-5.491175,4.516392,3.333314,-3.949689,8.977856,8.026871],[2.688432,-1.712153,-1.516961,-3.568029,6.537087,4.892372,3.070080,-1.795710,-8.822558,-2.568154],[4.196183,3.292655,-0.785698,-0.683503,-0.699842,1.238777,5.815532,-0.373318,4.046164,6.999893],[-6.139226,9.875499,-9.735784,2.603739,0.823884,-5.156224,-4.211980,6.983463,3.730805,-4.547116],[3.009576,6.545654,7.601126,-1.367076,-5.264943,4.225457,-4.952299,-1.491944,-0.270220,3.524676],[7.233218,5.779869,-3.030266,-5.819546,-2.945258,0.645651,-8.805181,-2.623933,-1.108102,3.802076]],[[-7.363056,8.038797,3.002684,-9.844528,-8.076429,6.305297,2.240752,8.829405,1.656170,9.689776],[-9.916236,4.127167,1.057646,-7.456657,-5.111046,-4.921544,-3.623556,-9.391223,-5.845074,-2.613758],[-6.798605,-5.216057,-4.529556,2.785771,-8.433687,9.570610,9.514906,6.015559,-6.326415,4.018235],[8.980319,-9.158877,1.437342,-1.720419,9.840193,-0.395792,-6.542668,8.647614,-9.148155,3.255859],[6.401221,5.694087,3.973144,2.819380,-4.796498,8.368013,-7.793284,-4.118800,-6.773624,4.250043],[1.123143,4.950948,0.943691,-2.117798,-6.332282,-6.127460,-9.824279,-5.722013,-9.244346,3.239783],[-2.477376,6.453992,-9.315993,9.037236,-7.182266,-7.888721,-6.856736,3.803290,-2.882027,-9.910534],[3.189635,-5.305910,-8.526429,-9.466873,-9.222093,-2.238271,-6.009619,-8.982223,8.383357,6.063779],[-2.241767,5.798362,5.265534,-6.068935,-9.024196,-8.795218,7.624265,2.867273,-8.928644,0.013842],[3.178556,1.483359,9.823367,0.760313,0.687072,-6.700109,-0.068744,6.826801,-0.506138,-7.912857],[-1.695034,7.018393,3.963883,4.205329,-7.592206,7.009409,-2.710941,8.470103,-3.013051,-4.870524],[3.193799,2.089386,-9.196598,3.960291,3.757113,8.521072,5.901192,2.838804,2.153961,-7.979408],[5.125426,-8.065419,-7.678813,2.970454,-0.216274,2.518425,-6.430002,7.504731,0.443803,-0.738063],[-6.458134,-8.463152,-7.548536,4.519438,-4.720849,5.329895,4.875903,-0.250754,8.248810,-2.877129],[0.378772,6.855271,-3.527122,1.555258,1.834511,-1.115733,7.306660,3.843805,1.351688,-6.140384],[-3.470001,2.322747,3.316731,-9.021375,-6.564644,-0.316668,-4.663296,9.424021,-0.371970,-4.686594]],[[-0.232967,-4.600130,1.396047,6.993635,-6.591929,-9.874236,8.024177,-0.012423,0.089893,4.528467],[6.007486,-8.213569,5.690925,-3.142468,-7.597963,-8.569727,-8.811520,-5.785929,-0.106046,-3.081277],[9.810892,-6.986919,-2.948744,7.486941,5.469505,9.208016,-6.261066,-6.314368,-0.592314,-6.545953],[0.662348,2.148878,9.891271,9.011645,-9.800831,-4.649409,-9.767955,-1.055157,5.986570,6.455183],[1.223570,3.938857,-1.398876,7.500680,-7.353910,8.245504,-1.805482,6.117515,-8.856344,-7.832773],[-9.809828,6.270632,1.297627,-1.767469,1.823312,6.897006,-7.603123,3.136642,-3.054467,5.559034],[-5.437687,-2.138409,-6.733935,-7.598632,-1.575459,3.491198,7.918378,4.695288,-8.663136,6.621480],[6.578671,-9.981287,9.975054,-5.546525,8.765382,-3.522705,-0.691904,-4.829945,4.146861,-2.082998],[9.210319,-2.514088,-5.709300,4.015969,9.721183,-8.360832,5.664985,8.024576,-6.291041,-4.172082],[9.141941,9.686657,3.378328,-2.342425,-3.855297,-2.063556,-7.027362,-9.501621,2.342778,-0.905784],[-2.199225,5.637108,8.471175,-9.392120,3.389540,0.277740,-2.911717,-1.122261,1.855086,-7.265554],[6.745030,0.213081,3.285060,-3.963460,-2.533441,-8.347856,-5.901070,-2.465842,-2.441060,5.094652],[-0.694698,-6.806666,-5.125790,-9.654824,-6.214381,8.187630,-3.550886,6.048452,3.702620,-1.729236],[-4.415795,-7.347917,-6.258401,3.107639,-5.688395,-6.553671,3.751190,7.224944,-2.582767,9.214649],[-5.025291,-8.493328,-5.283039,-9.847700,-4.124479,8.946019,6.415625,2.873874,-0.593349,-8.833576],[4.428505,8.806353,-5.931829,-7.300912,4.616600,3.331604,5.030486,-8.323435,4.034927,9.387609]],[[4.201956,0.309113,-9.459269,-7.367404,3.543571,3.463208,-0.842770,8.198771,2.817269,0.362893],[-2.081567,-2.189406,-3.932884,1.308395,-1.784401,6.393664,8.535704,-3.936861,1.977871,-4.464430],[-3.804560,-5.140947,1.832627,1.526861,6.471144,9.465763,0.639719,7.710627,-3.605176,7.593789],[0.226115,-7.403298,9.636533,2.313092,8.031728,7.750688,9.131921,-3.381014,-0.324401,-0.701600],[-8.123512,7.403062,9.345221,-5.583797,5.125219,-8.634132,-3.830714,1.735939,-7.449074,1.235419],[-5.657200,1.128449,-2.754147,-2.513602,8.420910,-3.499183,-5.988391,2.984324,7.803038,6.392764],[0.884454,0.852273,-5.928175,-4.886536,5.969739,2.311268,-8.532218,-0.296277,-2.164944,7.809519],[5.870297,-8.507037,8.182675,3.816617,6.323476,5.519588,9.807417,-1.872048,4.589165,-6.840701],[-5.920945,8.859437,-2.802207,9.764424,-5.521210,-9.462805,6.339581,-3.352416,-7.915385,3.090983],[-0.232694,-9.668382,6.173929,-9.906622,4.129821,-2.041532,-5.010430,6.776564,2.323659,8.095250],[9.363792,2.377972,-5.965280,-1.987950,4.116164,-3.830306,-1.464652,6.743426,-9.730426,4.679338],[-3.175637,5.013360,8.144747,0.380563,-3.870937,-5.699272,-0.557954,-4.308250,1.520693,8.927203],[-5.884496,9.723898,7.801618,-6.531784,-6.190500,2.534876,1.935492,7.042484,0.182679,8.499940],[4.700315,-5.790860,5.632883,5.068801,0.678843,-7.291247,-2.270579,-3.858420,-1.964142,7.027240],[-8.176027,-1.315806,-8.109406,-3.871897,-5.854499,1.858525,-3.639313,-3.053644,-0.814659,-9.307774],[-9.105826,7.190030,-5.884049,-6.352967,-7.237109,3.121183,1.417844,2.736729,7.608377,9.574911]]], dtype = "float64")#candidate|8907|(11, 16, 10)|const|float64
uop_8908 = relay.log2(const_8907.astype('float64')) # shape=(11, 16, 10)
output = uop_8908
output2 = uop_8908
func_8914 = relay.Function([], output)
mod['func_8914'] = func_8914
mod = relay.transform.InferType()(mod)
mutated_mod['func_8914'] = func_8914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8914_call = mutated_mod.get_global_var('func_8914')
call_8915 = func_8914_call()
output = call_8915
func_8916 = relay.Function([], output)
mutated_mod['func_8916'] = func_8916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8364_call = mod.get_global_var('func_8364')
func_8365_call = mutated_mod.get_global_var('func_8365')
call_8962 = relay.TupleGetItem(func_8364_call(), 0)
call_8963 = relay.TupleGetItem(func_8365_call(), 0)
output = call_8962
output2 = call_8963
func_8985 = relay.Function([], output)
mod['func_8985'] = func_8985
mod = relay.transform.InferType()(mod)
output = func_8985()
func_8986 = relay.Function([], output)
mutated_mod['func_8986'] = func_8986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3309_call = mod.get_global_var('func_3309')
func_3310_call = mutated_mod.get_global_var('func_3310')
call_9032 = relay.TupleGetItem(func_3309_call(), 0)
call_9033 = relay.TupleGetItem(func_3310_call(), 0)
func_6542_call = mod.get_global_var('func_6542')
func_6546_call = mutated_mod.get_global_var('func_6546')
const_9039 = relay.const([[9,3,-4,9,-2,6,8,4,-10,7,-6,9,-1,-9,-4,-4,-2,6,-5,-6,4,9,-9,-10,-7,-8,7,2,-8,-3,-9,7,8,-7,-10,10,-6,-6,1,2,2,-2,-1,7,7,-2,-8,10,-6,-9,-2,10,7,3,-3,-7,-8,4,-5,-9,-10,1,-1,8,-7,-4,5,9,4,-3,10,2,10,7,6,10,-4,7,-1,3,-1,9,4,9,1,-5,-1,8,2,9,-9,5,9,1,5,7,4,2]], dtype = "uint8")#candidate|9039|(1, 98)|const|uint8
call_9038 = func_6542_call(relay.reshape(const_9039.astype('uint8'), [7, 14, 1]), relay.reshape(const_9039.astype('uint8'), [7, 14, 1]), )
call_9040 = func_6542_call(relay.reshape(const_9039.astype('uint8'), [7, 14, 1]), relay.reshape(const_9039.astype('uint8'), [7, 14, 1]), )
output = relay.Tuple([call_9032,call_9038,const_9039,])
output2 = relay.Tuple([call_9033,call_9040,const_9039,])
func_9043 = relay.Function([], output)
mod['func_9043'] = func_9043
mod = relay.transform.InferType()(mod)
mutated_mod['func_9043'] = func_9043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9043_call = mutated_mod.get_global_var('func_9043')
call_9044 = func_9043_call()
output = call_9044
func_9045 = relay.Function([], output)
mutated_mod['func_9045'] = func_9045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7790_call = mod.get_global_var('func_7790')
func_7792_call = mutated_mod.get_global_var('func_7792')
call_9046 = relay.TupleGetItem(func_7790_call(), 0)
call_9047 = relay.TupleGetItem(func_7792_call(), 0)
func_6713_call = mod.get_global_var('func_6713')
func_6715_call = mutated_mod.get_global_var('func_6715')
call_9067 = relay.TupleGetItem(func_6713_call(), 1)
call_9068 = relay.TupleGetItem(func_6715_call(), 1)
func_7706_call = mod.get_global_var('func_7706')
func_7708_call = mutated_mod.get_global_var('func_7708')
call_9072 = relay.TupleGetItem(func_7706_call(), 0)
call_9073 = relay.TupleGetItem(func_7708_call(), 0)
func_4055_call = mod.get_global_var('func_4055')
func_4056_call = mutated_mod.get_global_var('func_4056')
call_9080 = relay.TupleGetItem(func_4055_call(), 0)
call_9081 = relay.TupleGetItem(func_4056_call(), 0)
output = relay.Tuple([call_9046,call_9067,call_9072,call_9080,])
output2 = relay.Tuple([call_9047,call_9068,call_9073,call_9081,])
func_9085 = relay.Function([], output)
mod['func_9085'] = func_9085
mod = relay.transform.InferType()(mod)
mutated_mod['func_9085'] = func_9085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9085_call = mutated_mod.get_global_var('func_9085')
call_9086 = func_9085_call()
output = call_9086
func_9087 = relay.Function([], output)
mutated_mod['func_9087'] = func_9087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1183_call = mod.get_global_var('func_1183')
func_1185_call = mutated_mod.get_global_var('func_1185')
call_9128 = relay.TupleGetItem(func_1183_call(), 3)
call_9129 = relay.TupleGetItem(func_1185_call(), 3)
uop_9130 = relay.sigmoid(call_9128.astype('float64')) # shape=(4, 220)
uop_9132 = relay.sigmoid(call_9129.astype('float64')) # shape=(4, 220)
var_9135 = relay.var("var_9135", dtype = "float32", shape = (4, 220))#candidate|9135|(4, 220)|var|float32
bop_9136 = relay.bitwise_xor(call_9128.astype('uint8'), relay.reshape(var_9135.astype('uint8'), relay.shape_of(call_9128))) # shape=(4, 220)
bop_9139 = relay.bitwise_xor(call_9129.astype('uint8'), relay.reshape(var_9135.astype('uint8'), relay.shape_of(call_9129))) # shape=(4, 220)
func_4055_call = mod.get_global_var('func_4055')
func_4056_call = mutated_mod.get_global_var('func_4056')
call_9147 = relay.TupleGetItem(func_4055_call(), 0)
call_9148 = relay.TupleGetItem(func_4056_call(), 0)
output = relay.Tuple([uop_9130,bop_9136,call_9147,])
output2 = relay.Tuple([uop_9132,bop_9139,call_9148,])
func_9155 = relay.Function([var_9135,], output)
mod['func_9155'] = func_9155
mod = relay.transform.InferType()(mod)
mutated_mod['func_9155'] = func_9155
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9156 = relay.var("var_9156", dtype = "float32", shape = (4, 220))#candidate|9156|(4, 220)|var|float32
func_9155_call = mutated_mod.get_global_var('func_9155')
call_9157 = func_9155_call(var_9156)
output = call_9157
func_9158 = relay.Function([var_9156], output)
mutated_mod['func_9158'] = func_9158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5705_call = mod.get_global_var('func_5705')
func_5706_call = mutated_mod.get_global_var('func_5706')
call_9184 = func_5705_call()
call_9185 = func_5705_call()
func_8596_call = mod.get_global_var('func_8596')
func_8597_call = mutated_mod.get_global_var('func_8597')
call_9186 = relay.TupleGetItem(func_8596_call(), 0)
call_9187 = relay.TupleGetItem(func_8597_call(), 0)
func_1975_call = mod.get_global_var('func_1975')
func_1979_call = mutated_mod.get_global_var('func_1979')
const_9224 = relay.const([3.947854,0.784752,3.394867,-4.909735,6.811008,1.226023,-9.833698,6.029659,4.507975,0.324898,-5.367545,-2.745850,-6.708867,-5.285757,-4.930379,-8.810406,8.965483,-1.246861,3.857975,2.635708,0.007087,6.337060,0.719646,-9.586356,-3.143800,1.989601,0.769725,-6.477770,2.031438,5.809612,-3.971288,7.939372,-5.241102,-1.813639,-4.720722,-9.639344,5.670328,7.053661,-4.570519,3.421664,8.561344,9.014759,7.588242,-9.258018,-8.394799,-4.552725,8.851131,-1.373702,2.675912,4.306970,-1.434077,5.604584,1.054168,8.185205,-1.282570,3.537044,4.422813,-1.521851,-1.379228,2.127576,1.711415,-6.314081,8.717808,-0.206994,0.002844,-4.351848,6.360621,4.715490,0.631683,-6.257868,-1.130012,9.578523,-7.385950,-9.819235,8.460892,1.814214,2.170525,0.204325,-6.336868,-9.348370,-3.936661,7.101050,-2.453674,-2.181721], dtype = "float32")#candidate|9224|(84,)|const|float32
call_9223 = relay.TupleGetItem(func_1975_call(relay.reshape(const_9224.astype('float32'), [14, 2, 3]), relay.reshape(const_9224.astype('float32'), [14, 2, 3]), ), 8)
call_9225 = relay.TupleGetItem(func_1979_call(relay.reshape(const_9224.astype('float32'), [14, 2, 3]), relay.reshape(const_9224.astype('float32'), [14, 2, 3]), ), 8)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_9228 = relay.TupleGetItem(func_713_call(), 0)
call_9229 = relay.TupleGetItem(func_714_call(), 0)
func_2997_call = mod.get_global_var('func_2997')
func_2998_call = mutated_mod.get_global_var('func_2998')
call_9245 = relay.TupleGetItem(func_2997_call(), 0)
call_9246 = relay.TupleGetItem(func_2998_call(), 0)
output = relay.Tuple([call_9184,call_9186,call_9223,const_9224,call_9228,call_9245,])
output2 = relay.Tuple([call_9185,call_9187,call_9225,const_9224,call_9229,call_9246,])
func_9278 = relay.Function([], output)
mod['func_9278'] = func_9278
mod = relay.transform.InferType()(mod)
output = func_9278()
func_9279 = relay.Function([], output)
mutated_mod['func_9279'] = func_9279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8430_call = mod.get_global_var('func_8430')
func_8431_call = mutated_mod.get_global_var('func_8431')
call_9293 = relay.TupleGetItem(func_8430_call(), 0)
call_9294 = relay.TupleGetItem(func_8431_call(), 0)
func_4781_call = mod.get_global_var('func_4781')
func_4783_call = mutated_mod.get_global_var('func_4783')
call_9300 = relay.TupleGetItem(func_4781_call(), 0)
call_9301 = relay.TupleGetItem(func_4783_call(), 0)
output = relay.Tuple([call_9293,call_9300,])
output2 = relay.Tuple([call_9294,call_9301,])
func_9309 = relay.Function([], output)
mod['func_9309'] = func_9309
mod = relay.transform.InferType()(mod)
mutated_mod['func_9309'] = func_9309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9309_call = mutated_mod.get_global_var('func_9309')
call_9310 = func_9309_call()
output = call_9310
func_9311 = relay.Function([], output)
mutated_mod['func_9311'] = func_9311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6076_call = mod.get_global_var('func_6076')
func_6078_call = mutated_mod.get_global_var('func_6078')
call_9390 = relay.TupleGetItem(func_6076_call(), 0)
call_9391 = relay.TupleGetItem(func_6078_call(), 0)
func_3474_call = mod.get_global_var('func_3474')
func_3477_call = mutated_mod.get_global_var('func_3477')
var_9405 = relay.var("var_9405", dtype = "float32", shape = (1, 84))#candidate|9405|(1, 84)|var|float32
call_9404 = relay.TupleGetItem(func_3474_call(relay.reshape(var_9405.astype('float32'), [84,])), 3)
call_9406 = relay.TupleGetItem(func_3477_call(relay.reshape(var_9405.astype('float32'), [84,])), 3)
func_7621_call = mod.get_global_var('func_7621')
func_7622_call = mutated_mod.get_global_var('func_7622')
call_9411 = func_7621_call()
call_9412 = func_7621_call()
output = relay.Tuple([call_9390,call_9404,var_9405,call_9411,])
output2 = relay.Tuple([call_9391,call_9406,var_9405,call_9412,])
func_9415 = relay.Function([var_9405,], output)
mod['func_9415'] = func_9415
mod = relay.transform.InferType()(mod)
var_9416 = relay.var("var_9416", dtype = "float32", shape = (1, 84))#candidate|9416|(1, 84)|var|float32
output = func_9415(var_9416)
func_9417 = relay.Function([var_9416], output)
mutated_mod['func_9417'] = func_9417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_9455 = relay.TupleGetItem(func_235_call(), 1)
call_9456 = relay.TupleGetItem(func_237_call(), 1)
output = call_9455
output2 = call_9456
func_9471 = relay.Function([], output)
mod['func_9471'] = func_9471
mod = relay.transform.InferType()(mod)
mutated_mod['func_9471'] = func_9471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9471_call = mutated_mod.get_global_var('func_9471')
call_9472 = func_9471_call()
output = call_9472
func_9473 = relay.Function([], output)
mutated_mod['func_9473'] = func_9473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7088_call = mod.get_global_var('func_7088')
func_7089_call = mutated_mod.get_global_var('func_7089')
call_9474 = func_7088_call()
call_9475 = func_7088_call()
func_6497_call = mod.get_global_var('func_6497')
func_6500_call = mutated_mod.get_global_var('func_6500')
const_9477 = relay.const([-9.533081,6.608358,7.690771,-8.940225,7.396444,-9.310438,-3.522782,-4.311119,1.684449,-2.318874,8.910499,7.559541,3.885627,-5.203420,2.723361,6.183212,5.217831,3.970347,8.802932,-1.736732,-9.209438,5.307169,-6.977284,-5.162031,8.096915,-7.202095,9.416937,-4.204379,6.867802,7.161609,-6.409591,8.089189,0.709535,4.076381,-5.771999,-5.116342,-1.363289,6.539978,4.128001,-8.878529,-1.516803,-5.243071,-3.789154,-9.992092,1.140347,-1.445368,-0.122876,-6.809648,-2.332903,-6.006747,4.981709,6.222090,-2.635127,9.615602,8.034692,-9.724084,-5.080744,0.035994,7.176557,-3.796324,-5.837749,7.779707,-1.857622,-2.527076,2.430213,1.629305,2.261050,-7.924516,-6.293117,-8.451602,5.985757,0.843682,8.215156,-0.673341,6.609103,6.569048,1.019634,-6.806136,-9.760862,-4.161664,-8.007898,8.332343,0.941639,1.212219,1.312945,0.159686,3.289300,-6.218974,3.840374,3.935266,5.424238,-1.119320,6.619403,0.426813,-5.033834,9.281591,6.637889,-1.196804,-8.833455,-4.215235,1.015070,-8.846354,9.976327,7.487738,5.401253,2.075623,-6.464733,1.364375,-2.089625,0.490630,8.958308,8.146465,8.601454,7.149397,-5.665417,4.851510,6.685837,-6.411678,-0.359874,9.020913,-7.441778,5.874509,9.555776,4.050886,8.778577,-4.303029,0.262036,8.095353,2.265262,1.383882], dtype = "float64")#candidate|9477|(130,)|const|float64
call_9476 = relay.TupleGetItem(func_6497_call(relay.reshape(const_9477.astype('float64'), [130,])), 0)
call_9478 = relay.TupleGetItem(func_6500_call(relay.reshape(const_9477.astype('float64'), [130,])), 0)
output = relay.Tuple([call_9474,call_9476,const_9477,])
output2 = relay.Tuple([call_9475,call_9478,const_9477,])
func_9481 = relay.Function([], output)
mod['func_9481'] = func_9481
mod = relay.transform.InferType()(mod)
mutated_mod['func_9481'] = func_9481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9481_call = mutated_mod.get_global_var('func_9481')
call_9482 = func_9481_call()
output = call_9482
func_9483 = relay.Function([], output)
mutated_mod['func_9483'] = func_9483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8985_call = mod.get_global_var('func_8985')
func_8986_call = mutated_mod.get_global_var('func_8986')
call_9570 = func_8985_call()
call_9571 = func_8985_call()
output = relay.Tuple([call_9570,])
output2 = relay.Tuple([call_9571,])
func_9588 = relay.Function([], output)
mod['func_9588'] = func_9588
mod = relay.transform.InferType()(mod)
mutated_mod['func_9588'] = func_9588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9588_call = mutated_mod.get_global_var('func_9588')
call_9589 = func_9588_call()
output = call_9589
func_9590 = relay.Function([], output)
mutated_mod['func_9590'] = func_9590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_713_call = mod.get_global_var('func_713')
func_714_call = mutated_mod.get_global_var('func_714')
call_9618 = relay.TupleGetItem(func_713_call(), 1)
call_9619 = relay.TupleGetItem(func_714_call(), 1)
func_3736_call = mod.get_global_var('func_3736')
func_3737_call = mutated_mod.get_global_var('func_3737')
call_9625 = func_3736_call()
call_9626 = func_3736_call()
output = relay.Tuple([call_9618,call_9625,])
output2 = relay.Tuple([call_9619,call_9626,])
func_9632 = relay.Function([], output)
mod['func_9632'] = func_9632
mod = relay.transform.InferType()(mod)
output = func_9632()
func_9633 = relay.Function([], output)
mutated_mod['func_9633'] = func_9633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9688 = relay.var("var_9688", dtype = "float32", shape = (8, 8, 14))#candidate|9688|(8, 8, 14)|var|float32
uop_9689 = relay.sinh(var_9688.astype('float32')) # shape=(8, 8, 14)
output = relay.Tuple([uop_9689,])
output2 = relay.Tuple([uop_9689,])
func_9691 = relay.Function([var_9688,], output)
mod['func_9691'] = func_9691
mod = relay.transform.InferType()(mod)
var_9692 = relay.var("var_9692", dtype = "float32", shape = (8, 8, 14))#candidate|9692|(8, 8, 14)|var|float32
output = func_9691(var_9692)
func_9693 = relay.Function([var_9692], output)
mutated_mod['func_9693'] = func_9693
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9753 = relay.const([[[-6,-7,-10,-6,-1,6,-4,-8,-9,7,5,8,-10,-3],[-3,-5,8,9,-4,-8,-5,-10,7,5,6,7,-5,7],[9,10,-7,-2,-8,2,-7,8,-5,4,-6,-2,-9,4],[-2,-1,3,5,-6,-4,8,-8,-6,-9,-7,-7,-10,-5],[-7,-4,2,-10,-7,-4,1,-9,5,4,-6,-4,-5,-5],[-9,-5,3,-5,-7,9,-1,-6,2,1,-7,-9,-9,-7]],[[4,-1,-4,9,-8,-2,1,-8,4,-7,1,4,-7,10],[-5,-2,9,-4,-2,2,-7,-6,6,5,7,-10,3,4],[-8,8,3,4,5,-7,-1,8,5,-8,-7,-5,-6,3],[-9,-9,-3,-2,-7,8,-2,-9,-6,-1,-5,4,-6,8],[-5,1,-10,-3,-7,9,9,6,-4,6,-5,3,-10,4],[7,7,-5,-6,-1,7,-3,-4,8,8,8,-4,-3,-5]],[[-5,8,-10,-3,-7,9,-9,-8,7,-7,-5,-6,8,-7],[4,-3,-10,-10,10,-5,-4,7,-3,8,-8,-4,7,-7],[8,8,-4,3,-4,4,8,-2,-8,-8,3,-2,8,-5],[5,-3,-4,7,2,3,2,-1,-9,-5,-2,-9,-8,6],[-4,-4,-3,-2,-6,6,-8,5,6,-2,-10,3,9,-7],[-2,4,3,5,-3,-4,5,-8,-9,-4,-8,2,-3,-10]],[[-9,-1,9,7,3,10,10,-8,2,-9,-8,5,-9,-4],[6,-9,10,-5,5,-2,5,-8,-6,1,10,-10,-5,6],[4,10,-5,-4,-9,3,1,4,-7,-3,7,-10,6,-7],[5,-8,-5,-8,7,5,-10,-8,6,-7,4,-4,3,-10],[-4,-3,4,9,-10,-2,-10,1,-7,-1,2,-6,9,9],[-5,-5,10,9,9,-5,-4,6,-4,-4,-9,-4,6,-9]],[[-1,8,-1,-5,1,7,2,9,-7,-2,3,3,-2,4],[8,-2,4,-5,3,8,-5,-3,6,-5,-8,-5,-2,4],[-5,1,-2,2,-10,-2,8,6,6,-10,-3,9,-3,-4],[-3,10,-7,-3,3,4,4,-8,-8,6,6,-8,3,2],[-2,-5,-7,4,6,-2,5,-4,-5,-1,-9,-7,-5,5],[2,5,6,-6,-3,-6,10,-9,7,3,-8,-5,3,3]],[[6,-5,-7,-2,-8,-5,-1,-3,-10,-5,6,9,4,10],[-5,-5,-10,1,1,-10,2,-2,-8,-3,7,-7,5,8],[1,9,2,-9,6,-2,1,-8,7,5,4,4,-5,-6],[-9,4,-4,-4,-10,-9,-4,5,-10,10,4,-5,-5,-2],[1,5,-4,-8,3,-3,6,9,-2,5,9,1,3,4],[6,10,-5,5,-3,6,-6,1,10,2,-6,3,-4,-9]],[[-2,-7,-10,-4,-2,-2,2,5,8,10,5,1,-8,-7],[1,-1,10,9,-5,-2,-2,3,6,-1,-3,-4,10,-8],[-10,-5,2,3,-4,-9,-5,-5,9,10,8,-10,10,-7],[-9,-3,1,-1,-3,-4,-7,7,8,-9,-10,2,10,-8],[6,-5,2,4,-7,8,-9,9,7,-8,-8,2,7,7],[-4,10,-10,-4,10,-8,3,6,-8,10,1,-2,6,-6]],[[-6,10,7,1,-2,2,1,10,-5,7,-3,1,-4,4],[7,-3,-4,4,-3,-1,-9,9,-2,-5,-5,-2,-7,6],[-8,-1,10,-9,-7,6,-7,4,-9,-6,-2,-9,3,-7],[4,4,-4,6,-1,8,7,9,-2,-2,6,5,-8,4],[6,4,5,-4,4,-2,-7,4,-8,-10,6,3,-9,-9],[-3,-10,6,-8,1,9,2,-10,-4,2,7,-2,5,6]],[[-6,-3,-8,7,-7,5,7,-3,9,-7,-10,-5,-5,2],[4,6,-1,-8,-3,4,-10,-10,-7,5,8,7,2,-5],[-10,-9,-4,-6,-5,5,9,-10,10,-5,4,-3,3,2],[-3,-4,-5,9,7,4,8,-10,1,-8,-1,-10,-3,1],[4,-1,2,1,-8,7,-4,7,-2,-2,8,-8,3,8],[-2,3,-2,-2,-2,2,-3,-5,-1,10,-9,8,2,-8]],[[3,-2,5,-10,10,1,-5,1,-3,-5,-9,10,9,7],[6,-6,-3,6,2,5,10,-5,1,2,-2,-10,6,-1],[10,6,-7,-6,1,-8,-8,6,-1,2,6,-7,5,-1],[9,-5,2,-4,-6,-9,2,1,-2,-7,-9,-6,5,3],[-1,10,-6,9,-8,7,5,10,-7,9,-9,4,-7,3],[4,-3,-8,-6,-2,2,-2,-4,9,6,9,5,2,-6]],[[-10,5,2,-2,5,-7,-7,-6,2,-7,8,-6,9,-6],[3,-1,10,-10,6,-7,1,5,-2,6,5,-6,-7,1],[-6,-4,-7,-3,-3,-1,4,-7,1,3,-6,-9,2,-3],[8,2,1,2,-3,6,7,-4,-7,-5,2,2,-7,-9],[8,6,8,-9,-6,-6,7,6,1,-8,8,5,-1,9],[1,7,-2,5,-2,8,7,-8,5,-2,-1,-3,4,-2]],[[6,-5,1,-6,4,2,6,-6,3,-1,6,-3,6,8],[5,-4,-9,-9,10,3,5,-2,7,-7,-9,-9,2,2],[9,7,-7,-4,-2,9,8,-8,9,-5,-7,9,1,-1],[-9,2,-2,-9,-1,-7,7,7,-10,-8,4,-9,6,-6],[-3,1,-9,-7,1,2,-2,7,7,-5,-8,9,-8,2],[4,2,-5,9,-5,7,-6,-2,-9,10,-2,6,9,3]],[[-4,5,2,-5,-2,1,3,-5,-8,-7,-5,-5,-3,-10],[-6,4,-9,8,-8,-8,-7,10,-8,1,4,-3,7,8],[6,-4,3,2,7,-1,3,5,-10,-2,-2,4,-2,-2],[2,-1,-2,-3,-3,4,5,6,7,-7,-8,7,3,3],[8,-4,-9,-1,10,-3,10,-4,5,2,5,2,10,3],[-3,-1,-4,-3,2,4,-9,6,6,-4,-1,-4,-8,10]],[[-8,-5,9,-1,-1,-6,8,4,6,-7,-9,3,9,-6],[6,7,9,2,-8,-3,-7,1,-8,5,4,-8,6,4],[-9,-2,-8,-8,3,-9,4,9,10,9,4,3,7,-4],[3,8,-10,-6,1,9,3,-4,-7,-8,-4,6,10,-7],[-1,10,1,-3,-8,1,-2,-5,6,1,4,-2,-8,-8],[8,-5,-8,-10,-3,-8,-5,-2,9,3,9,-3,-5,1]],[[3,-2,-5,-9,-2,-2,3,5,10,4,-5,7,1,6],[4,7,-7,8,6,6,6,4,-7,9,6,-9,10,-4],[-5,-7,8,-8,-5,-8,4,10,2,-3,-4,-6,-6,3],[10,-7,10,6,9,4,10,6,5,-8,-1,6,1,-8],[-7,-3,10,4,3,9,-3,6,4,1,-10,-6,10,-8],[4,-8,-7,-9,-10,-9,4,6,3,-3,6,6,-3,-6]]], dtype = "int16")#candidate|9753|(15, 6, 14)|const|int16
var_9754 = relay.var("var_9754", dtype = "int16", shape = (15, 6, 14))#candidate|9754|(15, 6, 14)|var|int16
bop_9755 = relay.minimum(const_9753.astype('int16'), relay.reshape(var_9754.astype('int16'), relay.shape_of(const_9753))) # shape=(15, 6, 14)
output = bop_9755
output2 = bop_9755
func_9763 = relay.Function([var_9754,], output)
mod['func_9763'] = func_9763
mod = relay.transform.InferType()(mod)
var_9764 = relay.var("var_9764", dtype = "int16", shape = (15, 6, 14))#candidate|9764|(15, 6, 14)|var|int16
output = func_9763(var_9764)
func_9765 = relay.Function([var_9764], output)
mutated_mod['func_9765'] = func_9765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8647_call = mod.get_global_var('func_8647')
func_8649_call = mutated_mod.get_global_var('func_8649')
call_9825 = relay.TupleGetItem(func_8647_call(), 0)
call_9826 = relay.TupleGetItem(func_8649_call(), 0)
func_235_call = mod.get_global_var('func_235')
func_237_call = mutated_mod.get_global_var('func_237')
call_9867 = relay.TupleGetItem(func_235_call(), 2)
call_9868 = relay.TupleGetItem(func_237_call(), 2)
output = relay.Tuple([call_9825,call_9867,])
output2 = relay.Tuple([call_9826,call_9868,])
func_9871 = relay.Function([], output)
mod['func_9871'] = func_9871
mod = relay.transform.InferType()(mod)
output = func_9871()
func_9872 = relay.Function([], output)
mutated_mod['func_9872'] = func_9872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7508_call = mutated_mod.get_global_var('func_7508')
call_9890 = relay.TupleGetItem(func_7506_call(), 0)
call_9891 = relay.TupleGetItem(func_7508_call(), 0)
func_8596_call = mod.get_global_var('func_8596')
func_8597_call = mutated_mod.get_global_var('func_8597')
call_9927 = relay.TupleGetItem(func_8596_call(), 0)
call_9928 = relay.TupleGetItem(func_8597_call(), 0)
output = relay.Tuple([call_9890,call_9927,])
output2 = relay.Tuple([call_9891,call_9928,])
func_9936 = relay.Function([], output)
mod['func_9936'] = func_9936
mod = relay.transform.InferType()(mod)
output = func_9936()
func_9937 = relay.Function([], output)
mutated_mod['func_9937'] = func_9937
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9987 = relay.var("var_9987", dtype = "bool", shape = (9, 8, 12))#candidate|9987|(9, 8, 12)|var|bool
var_9988 = relay.var("var_9988", dtype = "bool", shape = (9, 8, 12))#candidate|9988|(9, 8, 12)|var|bool
bop_9989 = relay.logical_and(var_9987.astype('bool'), relay.reshape(var_9988.astype('bool'), relay.shape_of(var_9987))) # shape=(9, 8, 12)
uop_9999 = relay.acosh(var_9988.astype('float32')) # shape=(9, 8, 12)
func_6144_call = mod.get_global_var('func_6144')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_10003 = func_6144_call()
call_10004 = func_6144_call()
func_9763_call = mod.get_global_var('func_9763')
func_9765_call = mutated_mod.get_global_var('func_9765')
const_10009 = relay.const([9,-10,-5,5,2,-3,-3,7,-10,-5,-6,3,7,-3,1,8,2,-10,10,2,-9,10,-9,-9,-5,-5,9,5,10,-3,-10,2,1,-8,9,1,-5,10,-8,-5,3,-4,-10,8,-6,10,4,-7,-3,-3,7,10,5,-5,9,7,-2,4,-9,1,-1,-3,-4,-9,-9,9,8,-7,-9,7,-2,10,3,-5,6,2,-8,4,7,-9,6,2,9,-7,10,10,6,8,-4,6,1,-7,4,1,5,-10,9,-6,-9,-1,-9,-5,-1,-6,5,6,1,3,7,9,-5,6,10,6,-7,10,-8,-2,-7,-7,-2,8,-8,-1,8,-8,6,9,-8,-7,2,10,4,10,-10,-6,9,8,-9,-4,-6,10,-8,9,-1,-2,6,2,4,3,-6,10,5,5,-4,10,3,5,-6,9,3,-10,-3,-8,2,-3,-2,-8,-1,-2,-1,-7,2,-6,-6,-6,4,5,8,-4,-5,-3,-2,-6,1,5,10,-6,4,3,-9,-7,6,-2,-5,9,5,-9,-10,-7,-4,-4,-6,9,4,-8,-2,8,6,6,-6,3,4,8,8,-4,-10,7,1,-8,9,-10,2,10,-5,1,-9,3,-8,-9,6,9,2,-4,5,9,-7,-4,4,6,2,1,4,7,4,-10,-9,-6,8,-5,-9,4,1,6,-6,7,2,9,3,-9,10,-7,10,-10,-3,-1,9,-8,-5,-8,-7,-9,4,-6,-2,3,-6,-10,4,-9,7,9,5,-6,4,-3,8,3,-10,8,5,3,-4,2,-5,6,8,7,7,-8,-9,3,5,-1,4,-4,-3,-2,1,6,4,-9,-1,8,10,-8,-8,-8,8,5,-1,3,-7,-2,9,-6,1,-5,-2,10,-10,-4,-1,9,-4,-1,5,-8,9,3,-7,2,6,2,-2,-1,1,1,8,1,-6,4,6,-6,-1,2,-9,5,2,3,-10,-6,-10,2,9,-1,-6,6,8,-7,-10,6,-5,-5,10,3,-4,2,-8,-5,10,3,10,7,3,6,7,5,3,-9,9,5,-2,1,-1,-8,2,-6,1,10,-9,7,6,-8,-1,-4,-8,6,-5,-2,3,7,9,8,7,4,-4,-2,1,1,-6,4,5,-7,-7,7,7,5,-7,6,1,-10,8,-5,-3,-3,-3,-6,-7,1,2,-3,-3,-4,3,4,9,9,7,10,-4,2,2,-8,-3,-2,-8,-3,-5,-9,9,2,-9,-9,7,-8,-4,10,10,-4,6,5,3,3,5,4,-7,-3,-9,3,-2,7,-3,2,5,-4,4,-5,7,4,-1,-7,-7,5,3,-2,-10,10,7,5,-8,5,10,10,7,1,-6,-8,-9,1,-4,-6,3,8,-6,6,-3,7,-10,-1,2,-8,-10,-3,1,10,6,-10,2,1,-10,-5,7,-6,-10,5,-9,-2,9,-10,9,6,8,4,-1,-9,3,3,5,-6,-8,-8,-4,-8,6,-3,-7,-8,-4,-4,-9,-5,-4,-10,-10,3,9,-7,-2,8,-2,-2,-2,4,5,1,1,-4,-6,6,-5,6,-10,1,-7,-9,1,-7,-2,-9,1,2,-5,8,3,7,-3,-3,5,5,2,10,5,-6,-8,-5,2,10,-4,-9,2,-6,-1,10,-5,-10,10,10,-5,2,9,10,-7,-1,9,-9,-7,10,5,4,6,5,-3,-9,1,-2,1,4,-4,-8,-4,-6,9,9,-5,-2,-8,-4,3,-1,-5,7,-5,-5,-5,-2,7,1,3,1,-4,6,1,-5,5,1,9,7,8,-4,2,-5,5,6,8,5,-10,6,-3,8,-8,-8,-6,4,-7,-8,-6,10,8,9,-1,10,5,3,-8,6,1,-5,-8,-10,7,6,10,3,9,-6,6,2,-9,-1,-9,4,-2,-4,6,-7,-3,-6,-6,2,1,-8,1,10,8,-8,-10,-4,1,-3,5,2,1,-10,7,4,10,-6,-1,-3,-10,5,-3,-10,-8,-3,-3,10,3,10,-2,7,-6,2,-9,-8,6,-9,-4,-5,-4,-7,5,8,7,-7,4,-2,-7,10,9,-7,3,4,-4,2,-9,-4,4,2,2,2,-5,6,9,10,-6,-3,-2,8,7,-6,7,-3,-2,4,-8,7,3,3,-1,-9,9,-8,10,9,-4,-6,-4,3,7,9,-6,-7,2,-10,-5,10,3,-7,1,-2,2,7,-8,6,-10,1,1,-4,9,4,4,-10,-1,10,6,9,10,7,-8,5,6,-3,-5,-10,2,-10,9,3,-8,3,7,-1,-10,8,1,-8,-9,-4,10,9,-9,8,9,-9,6,-1,6,3,2,5,-5,10,4,8,-9,5,8,-7,5,-3,8,6,-10,9,8,-7,7,-7,-3,-6,-4,2,2,-8,-5,-8,7,-8,-2,-10,1,5,5,10,9,-2,-6,-6,6,-7,-6,-6,10,-1,9,5,9,9,-4,-3,8,7,-2,4,8,8,10,-9,8,-5,5,10,-3,-9,-1,-9,2,2,-8,3,-10,2,-7,-2,-2,3,-8,3,-3,8,9,-10,1,4,-10,7,-9,2,9,10,-1,-1,7,2,-8,-3,-6,-7,-7,-8,9,-9,-2,2,-2,-3,7,-4,9,6,4,4,6,-9,-4,2,-10,-2,1,-6,-8,6,4,-4,5,8,-1,9,6,10,5,-3,-2,-9,-1,-6,5,-8,3,10,2,-9,-4,10,-8,-10,-10,-8,-10,-5,-4,-1,4,-8,3,-7,7,8,6,-1,-8,-7,-4,1,4,6,-9,-8,8,4,-3,-6,8,-2,-2,9,4,8,-1,-1,-9,4,3,4,6,-3,-8,-1,-5,-1,8,8,-5,9,7,10,8,-5,6,4,-5,2,8,-2,-8,9,-4,-7,5,-5,-7,-10,3,-6,5,2,9,-5,-9,7,1,-3,-4,4,-6,4,7,8,9,8,4,-4,-8,-9,6,-6,3,-2,8,6,8,-7,4,-5,-9,-5,-5,-7,7,-7,1,2,3,-1,-1,-6,7,-3,9,3,3,5,6,8,-8,-6,10,-1,1,5,8,-2,7,7,-7,5,8,-5,-2,10,8,6,-6,-3,10,-1,-9,7,-2,1,-5,-7,-8,1,-5,-9,9,-5,4,-1,3,-5,7,-8,6,-8,8,8,-10,-6,-10,-2,-10,-1,2,-1,6,-7,7,3,5,-6,9,-8,1,-7,-9,-7,5,-5,9,-4,-1,-7,-6,-4,4,-7,4,-3,1,7,9,1,1,1,-2,-7,5,5,-6,6,1,-2,-1,1,7,4,-9,1,10,3,6,9,6,7,-5,2,8,-8,-3,1,-6,-5,9,-6,-8,5,1,-7,9,8,9,-7,-6,-4,-5,-6], dtype = "int16")#candidate|10009|(1260,)|const|int16
call_10008 = func_9763_call(relay.reshape(const_10009.astype('int16'), [15, 6, 14]))
call_10010 = func_9763_call(relay.reshape(const_10009.astype('int16'), [15, 6, 14]))
output = relay.Tuple([bop_9989,uop_9999,call_10003,call_10008,const_10009,])
output2 = relay.Tuple([bop_9989,uop_9999,call_10004,call_10010,const_10009,])
func_10021 = relay.Function([var_9987,var_9988,], output)
mod['func_10021'] = func_10021
mod = relay.transform.InferType()(mod)
mutated_mod['func_10021'] = func_10021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10021_call = mutated_mod.get_global_var('func_10021')
var_10023 = relay.var("var_10023", dtype = "bool", shape = (9, 8, 12))#candidate|10023|(9, 8, 12)|var|bool
var_10024 = relay.var("var_10024", dtype = "bool", shape = (9, 8, 12))#candidate|10024|(9, 8, 12)|var|bool
call_10022 = func_10021_call(var_10023,var_10024,)
output = call_10022
func_10025 = relay.Function([var_10023,var_10024,], output)
mutated_mod['func_10025'] = func_10025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1357_call = mod.get_global_var('func_1357')
func_1358_call = mutated_mod.get_global_var('func_1358')
call_10050 = relay.TupleGetItem(func_1357_call(), 0)
call_10051 = relay.TupleGetItem(func_1358_call(), 0)
func_6513_call = mod.get_global_var('func_6513')
func_6514_call = mutated_mod.get_global_var('func_6514')
call_10061 = relay.TupleGetItem(func_6513_call(), 0)
call_10062 = relay.TupleGetItem(func_6514_call(), 0)
output = relay.Tuple([call_10050,call_10061,])
output2 = relay.Tuple([call_10051,call_10062,])
func_10088 = relay.Function([], output)
mod['func_10088'] = func_10088
mod = relay.transform.InferType()(mod)
output = func_10088()
func_10089 = relay.Function([], output)
mutated_mod['func_10089'] = func_10089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_735_call = mod.get_global_var('func_735')
func_737_call = mutated_mod.get_global_var('func_737')
call_10138 = relay.TupleGetItem(func_735_call(), 0)
call_10139 = relay.TupleGetItem(func_737_call(), 0)
func_3781_call = mod.get_global_var('func_3781')
func_3784_call = mutated_mod.get_global_var('func_3784')
call_10145 = func_3781_call(relay.reshape(call_10138.astype('bool'), [14, 8, 4]))
call_10146 = func_3781_call(relay.reshape(call_10138.astype('bool'), [14, 8, 4]))
func_8492_call = mod.get_global_var('func_8492')
func_8494_call = mutated_mod.get_global_var('func_8494')
var_10148 = relay.var("var_10148", dtype = "float64", shape = (1, 432))#candidate|10148|(1, 432)|var|float64
call_10147 = relay.TupleGetItem(func_8492_call(relay.reshape(var_10148.astype('float64'), [12, 9, 4])), 2)
call_10149 = relay.TupleGetItem(func_8494_call(relay.reshape(var_10148.astype('float64'), [12, 9, 4])), 2)
func_1240_call = mod.get_global_var('func_1240')
func_1241_call = mutated_mod.get_global_var('func_1241')
call_10152 = func_1240_call()
call_10153 = func_1240_call()
const_10156 = relay.const([[2.794682,4.962499,-1.806595,-9.280377,0.059514,-8.068105,5.029642,-7.768782,5.341760,-4.674076,9.965341,5.122806,0.386931,-1.455321,-0.637232,-8.389253,-2.017165,0.723651,-6.972923,9.587528,0.800658,-2.590741,5.127753,7.600715,5.086553,2.584814,5.687766,-9.998475,-2.974933,-2.527782,-2.495811,-6.876983,-5.185779,4.281700,2.397908,5.678878,-2.174350,-7.611374,-0.745979,-4.024018,6.134638,-4.237166,-2.488486,3.451881,5.141192,-0.267942,-6.685505,-9.052516,-3.555770,0.961294,-8.945153,-8.934784,-3.923108,5.335801,-3.560209,-8.934550,0.716894,-9.715293,9.188361,-7.512811,1.590915,-8.577138,8.000779,4.071063,9.936127,-0.016099,6.182334,-0.416806,4.367137,-7.324805,-9.999590,2.002775,8.313965,4.731287,-3.329500,7.380303,-2.742841,8.787935,-3.032584,7.751518,-4.211774,-7.254491,9.361946,1.541132,-7.350209,-7.756376,5.840394,-1.485006,-4.168560,5.298930,-5.212516,-8.361638,9.284501,-4.817514,-2.049227,3.277542,4.366881,-2.398179,-2.285417,8.358075,7.846583,6.052379,-1.084854,4.285292,-1.074898,4.724588,6.818308,7.561581,8.705524,9.912743,-0.515826,-3.299334,-1.001300,-9.949667,6.742945,0.039563,2.947975,6.599550,-1.870850,-9.058690,6.955884,7.326222,-4.357646,9.279231,3.083552,2.983324,3.907900,7.055259,9.032913,1.106153,-3.563811,7.409081,1.307170,1.439806,-9.920986,-7.822961,6.880551,-6.182046,0.886170,9.960467,-8.856518,-5.904058,1.112270,5.234024,4.188225,0.968499,9.402031,4.250202,7.279276,3.824974,6.351969,1.953786,7.235993,-9.090851,-4.980154,7.521346,-2.634548,-2.317085,-5.580780,-1.801368,-0.432056,5.606333,3.129292,8.936439,6.769167,-5.968281,-9.523439,3.757026,1.785316,-7.484555,8.707992,9.807430,8.717366,5.500375,5.304942,0.501545,9.138720,-1.763521,-5.182176,6.691799,-6.698682,-0.346207,-9.977745,-0.503403,9.648308,0.413098,4.485785,-9.622139,-2.860873,-8.742369,-5.943341,-9.636274,-7.863771,-2.831909,-7.053697,-6.873551,3.378312,4.392363,-6.836597,3.735916,9.905229,-0.801623,5.619399,6.622850,9.955167,-3.445930,-7.887089,3.604259,2.114625,9.142001,-7.247689,-3.550639,-7.604987,3.883425,0.481066,-9.770365,4.438834,9.315938,0.713104,-6.049868,-6.082698,-1.539744,6.106330,3.938709,1.830642,-1.360742,-6.119492,1.076398,5.247971,8.442561,-6.749214,5.295546,8.995516,-0.795187,6.978915,7.466090,9.931507,-1.971680,3.986140,2.592095,-6.573925,-9.295419,-1.716799,8.996010,-2.858496,1.305290,-1.746242,-7.778627,0.421199,4.769257,-7.530843,9.777364,-3.949687,-2.933289,4.765737,8.240378,-0.854394,3.538235,7.281540,-5.014601,7.106143,-3.912190,-4.037268,2.526517,-6.114529,-6.659423,8.255959,-7.381007,-1.975723,-1.405960,9.794057,1.516190,0.118036,-2.466749,-0.411460,0.165769,-9.659392,6.874893,-8.986115,2.164171,1.688761,0.154790,8.635543,9.608080,7.963864,0.458619,9.166243,-8.170833,5.082911,9.659215,2.874524,-8.068328,6.206522,-8.988655,-5.734086,-2.017020,5.954162,6.469602,5.502042,-4.600752,-3.562803,8.235352,5.035420,-5.560646,7.730840,-9.841151,-3.262098,-0.125015,-4.515287,-0.288284,-7.424320,6.237577,-8.872280,-1.798083,9.251936,-3.131090,8.389969,5.521918,5.831429,8.778658,1.126665,2.668942,-5.865570,5.837264,-3.336921,-3.231991,-7.175396,4.952581,-6.840453,3.209581,-8.185828,0.341121,7.679644,-8.397970,-6.465114,9.937664,5.621615,-2.247307,1.203526,9.414355,3.487467,-0.099957,8.193653,-8.125101,-7.503936,1.631337,-8.502698,-4.812214,5.745289,-1.287123,-2.332122,0.599944,2.544009,-6.734225,-3.287087,-7.480594,8.377499,0.777470,-6.915441,-9.906806,2.999784,-3.286263,-1.823976,-5.904011,3.564637,8.201206,-4.717835,-5.752293,-1.889671,-2.389983,-5.993541,-8.093775,-3.117758,-0.429453,-5.662250,5.971143,-5.679794,4.643596,-5.205365,-6.756986,-4.347801,9.021066,-0.877009,-2.590114,-9.416782,1.641063,-2.160828,-5.039246,-4.766797,2.611413,0.470525,-3.060486,-3.168556,-7.934169,7.510494,5.072374,0.261954,1.964170,-3.798426,-6.303264,-5.300891,7.369345,-4.801380,1.784415,-3.571391,0.810133,7.762189,7.805374,0.908550,-5.882452,-8.450380,-0.070771,1.490294,0.379940,-0.095992,-2.186783,-7.057831,6.903358,-9.611305,7.634462,4.053872,-3.828993,-4.012328,5.919972,-7.698739,3.925801,1.053477,-1.324610,7.651441,-1.698467,2.567380,-0.339110],[-7.031338,-9.103500,4.647272,2.975690,-3.516763,5.555542,3.859606,-5.337961,2.041856,-1.849368,-6.964815,8.516451,-5.298888,3.519296,-1.698614,0.227979,0.434346,6.437925,3.145011,9.663241,2.578306,5.995666,2.684913,-7.401681,2.947527,6.086462,1.927493,4.879759,-1.536281,3.886552,-4.636551,2.184749,4.352205,-8.354292,6.134464,-6.581435,2.352291,4.062068,-3.157554,9.790234,-6.758519,5.298656,0.883010,-4.702632,9.838351,-1.310087,-3.740866,4.374521,6.594361,8.936944,9.997463,1.080483,5.389863,-7.874184,-3.019856,8.423028,-1.932493,-0.046525,7.815732,-6.000690,-6.171409,-6.652388,-2.337438,-8.567186,-6.756249,0.809587,-7.361382,-8.001943,6.692135,5.470215,-3.483910,6.182376,7.468180,-5.968819,-6.331438,6.589634,3.832507,6.799514,8.847874,7.037288,1.693686,8.724654,9.134880,6.051741,-5.135850,-0.856752,6.821932,-6.258176,4.266577,7.092615,4.660005,3.968306,5.036417,-7.700330,-6.184010,-9.746852,-9.411076,7.736183,2.700792,6.081284,4.369757,-8.115128,1.502879,2.153568,0.794614,-8.432292,6.833693,9.055267,-6.118815,7.773836,-4.950531,0.362492,-7.229724,-0.533312,4.398362,5.133869,-9.580967,-6.208754,-6.060275,-4.782466,-2.990038,-3.274785,-9.396250,-0.877251,-0.016399,-5.255351,1.536878,3.222949,-5.454907,3.820446,6.322802,9.940440,-9.235824,3.267673,0.368384,-8.738480,-3.702987,-8.758848,5.050936,-0.717260,-1.595586,-5.620586,-8.101067,9.978013,8.370223,-5.453590,-6.420198,-2.029755,0.328782,9.165350,-7.923853,5.304178,3.020092,8.479368,-3.136562,-1.624236,-8.462798,2.491639,-3.177660,-4.770644,9.642920,9.901552,-7.379014,2.501261,8.221725,-4.211509,-8.220236,1.985038,1.116383,-7.660185,-8.107110,4.677563,1.110364,4.895118,6.244855,-0.522744,-9.652541,-6.436518,6.788604,2.806159,9.395823,-1.211632,0.630570,8.350532,4.700050,-9.997658,-5.832063,-6.906362,-4.032161,2.189059,3.918653,7.145260,2.290764,-1.748983,6.392683,-0.110604,-4.389586,-1.468869,-5.031008,-5.790239,-7.794708,1.870843,-6.917345,-8.803436,8.054443,1.162621,1.457491,-6.755739,-9.545890,-6.218008,-6.759995,-8.482208,9.299812,-3.467334,-4.040690,4.762982,-3.651774,1.617538,3.447144,8.911645,-1.181195,3.245352,7.656605,-8.633227,4.828919,3.313360,5.899980,-0.203476,9.130634,-3.889919,4.626305,-9.266754,-1.947199,2.370163,7.234574,-9.139412,9.585829,-6.685700,-5.443205,-2.066809,9.309843,2.554404,-5.378591,0.483107,6.874371,0.930199,-4.806534,-8.708661,-8.546608,-4.544169,-2.532278,2.636386,-1.234616,8.790513,-6.350211,-1.045750,6.672052,0.991581,2.878459,9.014096,-5.991391,-2.727951,-9.182140,-4.224048,-6.310330,6.420910,2.109691,-3.346001,-8.764613,-0.404125,2.640906,-8.661770,5.912974,-2.243210,-8.060099,8.671671,7.400773,1.126033,-5.717706,-8.407275,-9.132627,8.974987,-0.914262,-6.353430,4.591557,7.041991,4.586122,-1.376979,6.235158,-9.162021,-8.798841,2.728183,4.204104,-4.767449,-2.976344,-9.694287,-6.472146,-8.552752,5.086913,7.297840,-1.489942,6.631218,-1.687498,-7.856506,8.740510,9.751655,-2.683494,1.108666,-9.635885,6.911139,-4.074018,6.262811,2.860557,7.356925,-2.729413,-4.534396,7.905195,5.764935,3.119536,-0.050558,-6.248121,-8.833345,-0.084597,-9.972382,2.455698,8.058492,7.918077,-0.709263,-2.648762,1.257150,-8.248420,5.344338,5.811492,7.810616,-6.230367,0.159305,-8.178042,1.946998,0.972153,7.682244,1.764275,-0.498900,5.090586,-8.395760,-5.637512,3.680950,4.369769,7.251584,5.771789,6.309621,-7.921417,-5.613515,-4.910235,8.159481,3.045873,0.930766,4.036647,0.562511,-9.601478,-7.330816,1.751485,-9.747798,8.444933,9.277125,-6.014497,-6.471752,-2.329292,1.937635,4.416363,-8.921697,4.199992,1.325377,-0.533980,-8.583628,-7.488233,4.052612,-8.354764,-0.638825,6.307474,-9.941845,-9.071304,-5.925642,5.942416,-9.530104,-3.696432,6.419294,-2.583805,-7.860174,4.967616,2.841245,-0.527635,8.190007,-9.793251,-0.704330,3.249499,-1.015620,2.819848,-0.617630,-4.839390,7.933990,-3.309881,4.881148,-2.232169,5.538020,-4.563523,7.913093,2.726583,8.765741,6.810443,-8.511027,-9.984820,-9.477151,8.704539,-9.537974,1.307241,7.631005,-2.042096,-3.009687,-9.172268,-2.532447,4.158386,5.503741,-6.303842,-9.930252,-3.912858,-9.190907,4.876543,3.163031,-2.116941,0.180810,8.445937,9.088964],[9.063092,-8.315294,3.367272,-3.420786,0.166678,0.025530,-9.878064,8.377847,-1.997720,4.027572,-1.833271,0.288353,-7.197667,1.410371,7.242857,4.267466,-9.109165,-4.251136,-4.975692,-9.853587,9.139927,0.889276,-2.627812,-6.146245,-5.580071,-8.712021,-8.966509,6.672910,-4.018786,9.559795,1.925479,-6.431433,-3.547645,4.835171,0.371916,-6.904205,-1.889404,-2.462444,-9.536093,7.042693,-1.472577,-4.757853,4.798137,0.720652,-8.373710,2.781185,7.691914,6.239187,0.289452,-8.501653,5.357628,1.302546,-5.137545,-7.383050,-6.107391,-1.893234,8.612801,-9.306170,-5.586848,5.657672,-7.021370,9.164140,-9.469599,8.785580,2.854059,9.092371,2.469331,-9.118224,-7.299260,-3.255584,2.792571,-4.607983,7.498536,5.126407,-2.860595,-0.664534,-7.101371,9.024212,4.927590,-9.550218,-4.501392,4.631023,-6.724800,-9.681718,-9.370148,3.575939,1.756818,-7.585616,-9.917038,-8.619731,-1.916461,4.873627,-8.469370,-0.487289,-1.028219,6.259490,-9.779217,-7.525358,-6.816201,4.226723,6.594799,-3.594751,-0.378143,-9.643115,4.162453,-7.780539,3.465285,-1.476162,-4.390593,1.949662,4.843698,0.451002,1.258376,-4.686500,-6.928553,-1.665562,-1.363355,-8.013332,-2.482765,-1.978635,-3.173893,0.722521,-6.979517,9.524049,-1.279751,4.855065,7.040059,5.275522,-9.792346,0.726086,-6.834853,7.298186,-3.732333,8.665817,-3.074159,-6.345705,-2.145652,-4.899310,9.157791,7.994909,9.387656,8.307380,-3.297126,2.553026,-4.831948,9.001419,5.299848,-5.722314,4.017235,-1.654315,4.055217,-6.814839,-2.733229,-4.397707,-0.630479,-7.829863,2.530333,2.030742,-4.508115,-8.005250,2.648147,9.660746,-9.177503,-2.431629,-2.627444,7.866123,-5.492796,2.523755,4.548896,-0.903161,-0.775792,6.438268,9.554324,0.237486,2.101600,-5.800124,9.317325,5.391090,4.640385,3.541745,-8.702307,6.038093,-7.835186,-4.396013,2.508307,-1.793915,3.694380,4.511427,-8.543996,-8.863406,-3.314856,-5.456068,5.855905,-7.298436,1.583895,-6.932215,-0.911944,-3.935691,-5.007699,-9.993893,-5.249615,9.136742,-0.461978,-3.191171,5.069943,5.688989,9.570728,-8.897309,2.830372,-5.553706,-1.815077,8.531693,-4.211938,-4.328808,-0.901682,-6.459007,9.288648,-4.742994,-9.414218,-6.421133,4.286945,-5.958891,4.238470,1.582296,2.446929,0.980220,-4.158527,-7.348138,6.611907,-7.686920,-8.789698,-0.913415,-0.668979,1.746391,2.843632,5.747054,1.601172,8.037907,-2.029143,-8.649109,-6.522399,4.987214,-8.094681,-9.286662,-7.042528,9.576003,9.965907,-4.048850,-3.098819,5.128745,6.188364,-0.917153,-8.168392,7.756611,1.630332,-9.669057,-3.613578,-4.555031,8.017705,-9.578857,5.397770,-7.915695,7.865168,5.191458,0.001780,5.547343,0.770906,4.775371,2.135177,-9.397782,-7.419206,4.307492,-9.347132,8.362070,-1.108848,-0.728804,1.273535,-6.924169,1.438160,-6.465164,-2.200341,-1.639148,-4.000432,6.158987,-0.316984,-7.755403,-7.879521,9.503502,4.656738,7.367433,-2.944483,-2.418596,-0.770588,-5.009316,-8.203716,-4.648476,-7.362267,-7.513203,0.579456,3.816577,8.115853,-4.941353,5.408330,-9.810646,5.914730,-3.254017,4.620134,4.170711,0.274094,-7.269865,0.419092,4.515448,1.050197,-6.369190,8.954034,-9.350427,0.858509,1.934947,9.183793,1.972126,4.140620,-4.593469,-7.884524,-0.393608,-4.755787,1.212708,-8.311614,5.927505,-5.198849,-7.508227,0.270534,-5.814089,5.737333,9.850510,-8.701422,9.542541,-8.251381,-6.826926,-9.155971,1.046631,1.283907,-1.966060,2.055057,2.661488,2.969609,6.244820,3.961356,2.545216,6.269005,8.484708,8.408414,5.892496,-4.101274,9.821673,9.549399,1.048169,1.379436,-5.652479,-3.353802,8.111816,2.430076,-7.607615,-6.592913,9.490966,5.347039,2.922102,-4.770482,-9.963622,9.913415,0.811422,-6.117174,0.939746,-4.129022,-1.561451,-9.261383,-1.447216,5.542703,-5.784701,-7.601522,7.248103,-2.819522,-7.837831,-9.153424,5.307262,-2.548587,-2.627059,-0.255573,2.877625,4.222536,3.396322,0.634668,3.027815,-7.122703,-7.964605,1.102878,-0.860460,2.409740,-7.646101,-2.921676,8.016080,-7.911519,0.217791,1.057642,9.195024,5.839395,-9.628547,-4.459909,4.185138,2.191625,5.381115,2.126496,-6.557838,7.416675,-6.503119,4.154842,-4.024416,2.187297,-1.021641,-7.938454,0.118949,-9.448522,-6.849695,1.625898,3.032547,-7.016984,-3.350486,7.977039,-4.689648,9.766786,-3.489955,-0.594189,8.811425],[-8.150387,-2.370670,6.393802,-5.989648,-3.942709,7.863975,-1.335313,-9.082871,4.761581,6.754709,-6.570241,0.310387,-0.144685,-9.049030,8.304665,7.777256,0.517957,-7.450820,2.692889,-6.617431,-9.245153,-5.135127,-9.411050,8.193605,0.031366,-0.456219,-3.798836,1.546982,0.385462,2.323913,8.180863,6.055964,-7.667884,-7.462818,-2.309497,2.746643,-2.134383,-9.169727,0.826997,-1.902110,-6.766307,-2.019766,9.247324,2.729204,1.545874,7.830878,3.411294,2.005524,-9.985728,-5.129492,-2.528342,9.565733,0.208552,3.468926,2.841977,5.610038,5.473980,-9.342772,2.545655,1.816736,-6.498801,-2.921566,4.813040,-2.938830,0.044689,6.823024,-3.647312,-7.159929,-2.834912,-3.971870,7.508175,9.528674,9.067439,3.423910,3.384515,7.667241,6.808266,-4.291222,1.052343,0.389547,9.098857,-4.962438,2.360330,3.967764,3.901311,-4.998017,3.446063,9.261135,0.897516,2.324916,5.693289,8.375185,-5.253475,-7.531243,-0.821094,-0.058883,-9.847198,3.684495,3.894115,8.625479,8.770130,-9.301738,8.032797,9.071241,-7.872543,2.772544,-4.280469,8.883581,-7.583502,-8.089190,3.128250,-1.107449,-7.794004,0.059252,-7.835431,-0.525544,-4.059319,-0.186049,-0.451790,8.005624,1.137469,-1.419196,0.425898,-1.834434,6.538322,-7.109738,-1.150315,-1.421801,-3.614398,-2.409736,-4.523609,-0.467125,4.877912,-5.040400,6.864114,7.735190,3.217006,-0.304416,6.799336,-6.397575,7.324163,8.173435,-7.652987,-0.556890,4.598626,5.959868,9.183529,7.310357,2.390027,-6.566839,3.230638,7.724089,-0.130822,4.973654,-9.330757,-7.214945,-4.868773,7.175075,-6.878291,7.297039,9.131558,9.035502,7.069280,3.205659,3.166038,8.716459,2.887182,0.249833,-4.138288,7.740067,-5.014507,-0.623101,9.203457,9.494074,-6.799658,-7.969671,-3.965868,-4.960773,-0.556190,-8.245859,-4.621788,-9.299718,-0.972139,6.300750,-6.801451,2.368253,-3.962106,0.978971,-8.010385,1.336612,1.511696,-6.111133,-6.576573,0.765286,-6.152963,-0.467295,0.887386,9.465836,-7.014180,-2.606499,2.935441,0.268139,-3.527371,-8.539900,-4.350745,7.467024,2.857718,1.812031,-6.216483,-4.706768,-2.665750,6.151415,4.862924,5.759135,3.092559,-9.385352,7.729455,4.066457,-6.279289,-2.908039,5.711385,-3.975649,4.542207,-0.132977,7.156466,3.879423,5.522193,2.638833,8.678118,-0.159819,7.203603,0.479454,3.634014,-5.279898,-2.566483,-4.316239,-5.765957,-8.135919,-6.635865,0.712204,1.791171,0.992848,-0.955768,8.808587,0.776610,-7.285055,-8.293097,4.630518,-9.856588,7.546958,5.384141,3.271566,8.928881,0.853217,-8.015336,7.246463,4.612315,0.191335,3.489018,8.702227,-4.800939,2.296577,-0.729750,-2.328066,-0.793904,6.076216,5.820169,4.721360,6.402804,-5.960470,-6.453392,7.246855,-9.948256,7.242912,-1.214609,-1.786385,-9.080532,6.268087,2.650562,-4.860117,-6.877016,4.178754,-1.182636,-8.993699,2.275249,4.579389,-7.438218,-5.818957,0.436214,-3.326438,-6.035613,9.546842,0.504115,4.206940,-8.217922,-5.252297,-3.965670,5.352835,7.187656,-9.680585,-2.519936,-7.980922,-2.185023,-0.939688,-2.125776,1.784546,9.318640,7.890584,-8.209520,0.740202,-7.666028,8.868659,2.453527,4.193312,-2.577094,-2.561820,-2.110006,6.011266,6.524290,-3.244558,-5.139515,-3.353593,-5.641851,-2.366606,1.178008,-1.063639,-9.832085,-1.843032,-4.417350,-6.190420,7.100300,3.163926,0.006533,-8.862706,-8.216247,-5.786444,7.686747,4.450279,-9.478774,-3.183990,3.312498,-1.086460,-1.158207,-4.083898,-4.074689,4.969485,6.393467,2.870124,1.581384,1.538780,3.708576,-7.181449,-1.446965,-9.031143,-1.858336,-2.573571,1.908258,6.626084,9.842185,-9.223765,-9.772102,6.531117,5.801974,-3.905868,8.546217,-5.437751,0.814647,2.432894,-3.204408,-8.286297,-2.915044,5.145500,5.344976,3.474894,-0.581166,2.889726,8.475295,-6.290991,7.625352,8.944872,-6.869930,0.970449,-8.163743,9.604079,9.035710,1.544653,3.651766,2.361114,9.064274,0.660067,6.503238,-2.416764,-6.738697,1.836935,5.099132,-0.541110,-9.359651,6.031926,-6.995695,-6.844163,6.218635,7.135734,-3.611428,7.925011,8.136959,2.134720,0.147178,3.898762,-8.559876,-8.946136,7.742385,5.598764,-2.860305,-4.819971,4.150835,-3.877662,1.642080,7.151691,8.451869,2.091542,-8.245977,7.408339,9.554282,3.005485,4.480900,5.419076,-8.781002,-1.525085,-4.864123,6.923111,1.060291,-9.636051],[8.878694,-0.578965,-7.738869,9.123422,-7.462981,4.053943,8.581120,4.779936,-4.152960,4.610058,1.190755,9.115254,-2.122982,-9.723685,8.914681,-6.950483,-6.916858,7.619987,9.371629,0.034399,2.876035,5.486846,9.066257,4.855791,1.040186,-8.633407,-4.783781,-2.799248,-4.982142,3.073591,9.796976,-6.733923,-1.530568,2.861758,-3.684167,-1.266657,3.359283,-9.420080,-2.257037,-6.948253,-5.115030,6.625257,-2.269627,-2.370502,-6.752121,-6.138606,6.627364,6.581157,-1.757184,7.614170,-2.915652,-4.983177,8.731119,-1.925009,-1.263240,-4.108627,-6.684356,-1.154651,0.342336,2.163472,-9.699251,-8.087904,0.511652,8.961612,-0.319053,-9.204546,-8.081810,-8.901351,-1.262132,-7.288071,5.139552,7.841197,-7.027325,-7.955912,-9.933402,8.476944,-7.019131,7.759338,7.951758,2.280295,9.874746,-4.392274,3.221683,-1.455046,-3.802927,-4.657484,2.402384,4.173793,1.734956,1.403719,3.850402,-1.318406,-8.288802,4.205302,8.288905,8.763817,9.831953,-4.670060,-6.862959,-8.067526,4.133081,-6.548935,-8.910792,-9.440520,-6.926159,-8.514253,-7.960217,3.572643,-4.457088,7.633956,3.417786,-2.909701,-0.003416,6.024669,7.620552,9.074890,5.756725,5.420811,8.163165,9.732756,-7.317538,-5.479687,6.139616,9.780801,-9.853073,0.940440,-3.240051,-8.851126,-9.963152,3.904273,9.814508,8.528687,7.118851,8.009426,-7.097717,-5.874643,-9.813857,-1.214794,-9.890778,6.763708,-6.765215,-9.641948,-5.069870,7.610436,3.891419,8.848830,-6.748643,2.183282,3.595795,-7.301481,7.132154,-0.085477,4.537161,6.205769,9.545290,7.416057,0.798489,-4.392371,-7.830566,0.482931,-6.495717,7.680458,9.151433,-5.590298,7.918176,-7.728516,2.741980,-6.430812,4.984896,-8.260422,-1.780377,-1.314581,-1.986754,8.598984,3.397208,-7.767854,0.102689,-3.823363,-2.203437,-4.251341,8.575579,-9.264741,1.441182,-0.092927,6.940290,0.037241,-8.168033,8.229316,-2.763150,3.282665,2.899467,-2.897807,3.962052,6.401887,8.026177,5.087585,4.947812,-6.279667,-9.090396,2.199199,9.021199,2.500927,1.758475,-7.428636,-7.989711,9.180407,4.101890,-9.546851,-8.315546,-5.542578,4.624110,-9.787466,-5.055070,-7.222676,5.997181,-5.036791,-5.227075,-4.835847,-3.010578,-3.446988,3.812213,4.778761,3.364067,9.302905,1.906159,6.592499,-0.362790,0.608181,-6.136137,3.055612,-1.376039,3.076125,-0.510237,-0.839948,-5.089391,9.425658,-1.626176,3.880348,-2.626216,5.603653,-7.436859,9.621988,-7.184300,7.577693,-9.599585,7.693524,-9.415980,8.294153,-6.432016,-2.016654,-5.598437,-8.003704,-6.226587,-8.616440,3.770093,-5.019670,4.480207,-9.134362,7.546319,-9.960902,-7.058576,-7.518658,-2.434284,7.271627,5.161572,-7.084782,4.889264,-6.702359,-1.741070,3.120765,-1.217488,9.676482,0.344607,7.469763,-6.302802,-5.686320,7.048620,5.422417,-9.314441,8.703372,-3.533323,-2.435422,-8.218804,2.852156,7.186646,-1.407916,6.780703,9.384289,1.038016,5.331864,2.010539,3.388706,-4.865756,-3.191249,2.040833,-6.721545,8.653802,-8.197535,5.718297,-5.105194,-7.218767,-2.770234,6.295771,-5.793332,-3.678961,-2.041520,5.580775,1.650078,-0.458409,-5.363114,0.215319,-7.126049,2.377836,-0.591839,-3.025311,-8.220837,-5.407656,-7.941621,-2.714514,-1.646469,-3.761527,-3.842785,-5.680550,0.643712,-8.854954,1.178711,-3.147087,-0.758644,-4.037660,-4.079650,-5.613487,5.007214,6.516182,-7.332380,-3.829532,1.100575,6.644503,-7.251961,9.142850,-9.606426,3.524115,6.253052,2.874745,-0.411513,-9.559516,2.236743,0.924917,3.936482,-7.266536,-9.572428,0.635849,-1.568815,-5.940365,-3.679554,-4.581027,2.159307,-7.342743,-9.196080,-1.586523,5.156089,1.963649,4.449043,5.939905,-7.640821,-8.726060,-8.021056,-6.493845,-4.450249,7.258160,-5.205384,-8.230479,-4.326784,-1.471238,-4.288006,5.809017,6.994211,-7.275445,0.586165,-2.600965,-9.992589,-0.921475,-7.238026,1.231319,1.209165,9.551629,-6.438649,0.794508,2.196512,9.473613,1.493937,2.401274,-5.118339,4.867566,-9.657401,0.181108,4.764536,9.332871,-0.488881,-7.828248,-4.568218,2.184016,6.775426,9.927903,-9.455665,7.629949,2.294732,-5.073106,-3.677692,2.140547,1.619847,8.394891,-3.808341,-6.116578,5.696880,3.090690,1.245248,7.393783,9.652757,7.132797,1.625417,6.459839,1.176589,-1.684021,-5.573686,-6.868296,-1.466422,-2.747258,4.402441,0.017806,0.975621,-4.123034,3.401749],[-2.301366,-2.285490,-3.506104,-9.385364,-8.562034,-2.706255,7.445109,-4.116117,-1.977739,-5.036091,6.188987,-9.297096,-2.376376,1.797732,-0.071975,-5.569478,-0.952770,-9.406901,1.235114,-8.245753,-6.375198,-9.316869,5.914326,-9.065960,-4.435418,-6.238337,-1.297436,-3.481561,1.725073,1.459029,3.818052,-9.470591,-3.989359,-2.746122,4.499002,3.103875,8.108181,9.204428,-0.216109,3.248135,-5.925273,-1.813804,-1.798531,-6.563179,8.934808,0.889288,6.911662,-0.889990,-4.976234,9.393764,4.413350,2.013187,8.688856,-6.122741,-1.799831,-8.687561,7.065216,2.074809,3.058473,1.219269,9.557066,6.555986,-3.434080,-6.647261,7.208742,-7.140634,-4.326099,5.467834,8.001318,1.433304,0.702456,-8.107477,1.685277,-5.888574,7.119791,1.598262,-3.055338,-4.460628,-2.635135,5.290203,-2.481064,-7.206160,-4.556255,-8.321738,2.288282,3.838567,2.620808,-7.652999,-9.143907,-4.802809,-3.263368,-5.804064,-2.361167,-8.248909,-4.281504,-9.384059,2.417318,2.694171,9.322910,5.833840,-4.667375,0.922686,0.636752,-1.463721,7.481183,8.402095,-0.557282,-2.313458,-8.514540,6.603654,0.382225,-7.204005,-4.255131,-4.245286,3.143975,5.232423,-1.078817,-1.582473,-9.318955,8.303291,9.981955,3.519139,9.768890,-4.630789,-6.841643,-6.667716,-6.474775,1.163549,-2.816268,-2.679320,8.227251,9.009194,-2.365433,7.235793,-2.459262,-8.504715,-3.764358,1.125951,-3.964871,7.737980,6.975751,-2.746019,-7.067225,6.709366,5.628365,2.790189,4.513883,-5.122039,-0.495310,-3.210079,4.607940,-6.561469,-1.731164,6.241651,7.464916,-8.317979,-4.798309,-4.793624,-0.750217,9.730301,0.432356,-1.156625,-2.264359,2.882973,4.250133,2.477619,-7.326703,-5.686144,-3.719225,5.761486,-1.592990,-3.640311,-3.014577,-5.883262,-9.828589,-6.263875,-2.263174,-4.119207,-8.318548,2.490257,6.806217,-3.087115,-5.282139,5.115143,-8.987739,-9.451684,-5.414647,1.545680,-6.983555,0.398502,3.396999,-2.245351,-8.883185,-8.679937,-4.386421,-5.363406,7.771760,-3.274086,0.891541,-8.082634,-4.531993,4.476121,0.021929,-1.508235,-5.685720,7.752712,9.653293,0.955197,-0.684080,-7.622040,6.777962,9.787042,7.800753,-2.723750,0.751864,-6.665791,3.564886,-5.848058,-7.263643,-0.689679,-3.348581,8.867090,-6.478819,4.583955,-8.777354,9.461529,1.557488,-3.260496,-3.342149,2.603286,7.933033,-3.950466,7.568616,-6.542437,0.151544,-0.341245,-3.196195,8.655437,-5.659506,8.716087,8.482738,-9.310522,4.094183,8.725744,7.485039,6.933254,5.366185,-2.960666,-9.879442,-1.064981,1.066861,7.549741,-5.780492,-6.558873,-6.500700,-0.525991,2.169315,-4.869837,2.657550,-9.739830,-5.383276,-8.384703,8.136732,4.344973,2.136382,9.075356,-5.344289,-2.098073,-4.193320,-2.163509,-0.049869,-1.640024,7.537793,2.885751,-9.662538,-2.119476,3.459694,-9.976644,8.331214,7.396491,-3.531139,6.654389,7.954193,0.117366,8.986470,-3.700321,-4.191493,6.879054,2.379634,2.141968,-9.193867,3.665625,-3.926125,3.142596,2.227715,-7.147944,0.722231,-3.033217,7.448508,-0.375120,4.619067,-3.670080,1.985222,-4.615550,-3.978105,1.148964,2.882959,6.995448,-4.705328,4.590863,8.421734,8.319705,4.135761,2.223672,-5.752742,6.625457,3.641297,0.353522,8.096700,7.788593,0.922805,5.835499,5.381987,-8.054590,2.381280,9.710737,9.117363,2.802469,7.026561,7.116572,8.830534,4.826588,4.027978,4.951880,-3.712216,-7.355939,0.044502,-3.159389,-9.863354,8.309358,-0.837930,-0.173663,6.896326,9.061275,6.006462,-4.716883,1.154206,1.876070,9.977481,-8.417556,3.450853,0.112988,-4.754273,-3.395434,0.529527,-6.743628,-0.343715,8.680025,-2.091905,-5.114010,-2.705491,-1.342697,6.402867,-3.851621,9.326562,-1.704845,4.236965,7.201865,-5.201497,6.792032,6.725165,0.729351,-4.147652,-9.444613,0.194600,-3.577141,6.718436,-4.030400,-0.601635,9.184140,9.679824,6.873945,-5.436253,-5.452205,-6.101401,-2.981332,0.240055,4.290677,-4.832353,-9.684932,4.654310,3.014046,-4.373498,5.857690,-0.794951,-6.762698,-2.127992,8.091171,-8.419238,8.987080,8.916768,9.117911,-3.342007,-9.172748,-6.253092,-5.464549,-1.625832,-7.230269,9.621530,5.928519,6.345406,5.028549,0.194863,-8.550264,-4.887031,-8.652884,6.095261,-7.926292,7.612288,-6.265325,-5.680183,7.163651,5.195795,6.438130,7.241576,-2.949563,-2.094403,-4.046725,-3.483052,3.592519,3.929081,-4.842730],[1.316798,-9.148951,-5.989075,-3.255231,6.027464,9.145351,-2.683891,-7.792231,8.991087,-9.809245,-9.531151,-9.184478,3.617695,-8.670077,4.568560,0.844136,6.568244,9.432465,-6.382090,-6.795640,5.574101,-0.425970,-7.528594,4.216722,-1.177602,5.335614,5.808468,6.210504,-8.432168,3.070995,5.505304,-4.182745,-7.349154,-9.450538,-5.641583,-5.157458,-0.353456,9.986631,7.101483,-1.231716,-5.053493,7.219943,8.665706,-9.692974,-5.943445,-1.282721,-1.906386,-0.983092,-9.813992,5.228846,-7.634938,3.221841,3.121079,9.662799,2.411285,-4.733022,-6.327208,8.810864,-3.835833,6.986819,6.858370,-1.381133,-8.550848,-8.331942,9.857586,3.696894,-1.764756,-6.801949,9.286700,-5.488827,-9.042473,-7.733356,-0.686243,-5.705875,0.642933,0.764766,9.826515,-7.041967,7.741626,5.809903,5.999605,-8.989229,0.393166,2.101906,-4.527879,6.820937,-7.689003,7.362766,-6.800900,7.535574,6.127497,-0.433174,7.719309,8.520340,-1.518632,2.434310,0.783284,8.730239,2.170054,-2.825911,-8.430215,-2.863682,6.323943,-7.364874,3.006507,-2.403644,-9.412833,-2.471565,1.252807,-1.425943,-5.123513,0.135300,5.641773,-9.952797,7.735748,9.191650,-9.645027,-3.228302,7.266837,0.961914,1.926816,-2.805168,8.558507,9.925152,-3.523054,-0.606923,7.759970,-2.055419,-7.867822,1.573020,7.351893,0.846119,-9.010524,-6.663801,-1.578347,2.800837,4.806988,-8.634683,-8.824287,9.331621,4.156792,7.969926,-7.609710,-4.050157,-6.440710,-7.398432,-0.371828,7.328424,-9.058250,-6.863969,-4.488641,-3.922728,0.723167,-2.616210,-2.346675,-6.858048,3.835034,-9.269849,-2.370983,-7.071724,2.826187,-7.023797,-9.687873,-5.938901,0.121256,-8.306392,-8.143439,1.587085,8.373907,4.567567,-2.050062,7.751278,2.305658,8.530156,-3.902718,-9.013966,-9.819179,6.088712,1.717460,4.005029,6.657912,-3.076380,-7.812514,9.977774,7.902550,7.681952,0.159941,2.919621,9.375066,-5.603297,-2.377088,5.944885,0.801227,6.937067,-2.323492,-4.473220,-6.980224,-0.142259,-7.079632,-2.656950,-0.105274,7.039619,7.945376,4.482059,5.746165,-6.821176,-2.529287,0.232508,6.856818,-9.873285,5.986038,4.877007,1.281711,9.261077,1.657436,4.054859,0.681696,5.398019,4.523031,1.617084,-0.020867,-8.435744,1.264065,1.797822,0.273882,6.303621,-5.559254,-6.826690,-6.409935,9.357887,-3.499099,9.724588,-4.146616,-4.609629,3.553556,-0.381857,0.216121,6.735507,-5.563381,2.450207,-0.681254,6.918612,5.546324,6.294147,5.705954,-8.728649,6.254326,8.064075,-9.763609,-9.867275,-3.956810,-6.267305,6.939783,-5.869187,-2.410049,4.548319,-2.185546,3.658100,7.886298,2.929904,5.713193,-2.817686,-7.805810,-9.749416,2.255274,-7.795532,-5.709836,6.425541,-0.570646,3.668105,-6.699126,-6.788429,6.073945,-7.056364,-5.169270,1.111738,6.528877,-7.798013,-1.710399,6.368096,1.576022,2.866684,-9.273037,-9.981969,-4.499149,8.495809,-9.031731,-0.804542,5.399396,-6.369516,-8.567456,5.083145,3.782202,1.592815,4.216107,5.074216,6.635302,-3.125157,-0.997116,-6.594169,-1.463559,9.315396,7.029191,2.989488,-3.522220,-7.716760,2.540200,1.677888,-0.082031,-1.272999,0.933101,-9.473155,-1.847525,-7.016437,9.878946,-2.166535,-5.829140,1.387081,0.410134,-2.442291,-7.972698,-0.843109,-1.968458,2.759440,3.027197,-7.916846,3.449804,1.784446,2.138847,-7.639531,-3.487540,9.104921,-5.151534,2.426132,1.697037,-1.378925,-5.064468,3.188825,-7.902640,8.695406,2.625366,-5.743837,2.902054,-2.642305,0.003991,9.755284,8.827767,-3.146427,6.628076,7.408477,3.226472,3.067517,0.585950,-8.289941,1.707213,8.755976,-6.357223,5.283881,6.044922,-7.913203,5.941907,-5.838267,-7.148538,-3.301104,-8.458166,-5.672918,9.777970,-2.337869,1.629683,-1.299526,-2.884140,9.239785,0.194359,-1.447174,-5.032841,8.232326,5.614413,9.351694,-3.582459,9.542634,7.120502,-4.819409,6.736630,7.514814,-1.210170,5.790675,0.272019,0.860703,-5.999216,3.846671,-4.850652,-1.140113,5.274875,-2.384879,7.552451,-4.220627,8.272772,-2.830933,2.287030,8.996935,3.088734,0.584161,7.240754,-7.578155,-4.409007,8.198730,-4.168205,-1.167857,3.020869,-8.250622,5.301041,7.751664,6.176972,4.401670,-4.556738,-8.977989,-2.808141,-9.827078,-6.469141,7.976923,9.467090,-6.249154,-3.846208,2.281495,8.481584,-4.412045,-0.065466,5.842766,1.342750,8.264152,-3.031157,-0.924057],[6.009875,-4.342538,7.595347,-1.240252,-7.052515,-2.300708,-6.785174,-2.707728,1.486729,-4.007679,8.583275,-0.487215,-2.445146,-2.617886,2.886341,9.591422,8.511420,7.264618,8.996125,7.494760,-2.571304,-7.583856,3.193898,-9.202024,-3.281773,2.446666,-8.250546,-2.636121,6.253995,5.222526,7.667177,6.570649,9.627663,3.054783,-8.318660,-2.784780,0.339662,3.080315,-3.532885,1.193547,-5.019679,-4.016474,-8.272694,-0.109447,8.406119,8.519737,-4.579631,6.099943,2.213834,4.707075,-1.330913,-6.965500,-4.293806,-3.557920,5.033740,9.740935,-0.694262,-9.370905,7.372204,-8.474722,3.808152,2.985672,-1.381290,3.709073,-9.439843,-6.791605,-2.239038,-0.595215,-1.384357,1.956021,-1.091211,-5.155974,-3.402583,-5.458520,2.380635,-3.713008,-9.124925,-1.557792,5.861313,-7.146328,-8.151336,-6.650704,0.794692,-7.882163,7.346887,6.961771,-9.220337,6.741944,-4.182525,-1.959345,-8.170842,-0.604632,5.870513,-7.955424,-3.439075,-3.518899,1.035045,-5.794694,6.498384,-7.295412,-2.141051,-8.996017,8.974617,-1.313937,1.699301,3.615966,0.990123,-1.202672,4.134624,7.353646,2.496587,-0.805427,-6.096223,5.019019,1.741514,6.101081,6.636353,3.427708,9.133545,8.700726,-8.050226,-4.584107,-1.896472,-4.814642,7.167565,-6.638816,8.472363,8.967206,6.621336,0.626983,6.889738,-0.308900,9.664359,8.988808,0.785782,0.852531,-8.946092,-7.953548,0.249539,-7.602406,-5.887486,1.691182,9.214775,-8.425694,-3.545854,-6.608290,-0.688608,-3.378552,-5.235949,-0.565203,-4.542748,2.754232,3.211636,-0.538785,6.153492,-1.989743,9.214222,4.096698,-1.283745,5.453639,-1.338849,-0.048036,-7.697871,-5.041307,1.167754,2.120392,-2.895333,-5.192101,-2.222228,-4.644667,3.436005,0.528780,2.585366,0.482159,-3.032901,-9.815024,-9.298598,7.595074,8.041044,5.792390,-3.706092,2.520328,-0.864705,9.119390,-0.986192,-7.777807,-4.867905,-7.783487,-1.018634,7.207106,-7.547075,9.959029,6.656492,0.398927,-6.488760,4.361555,4.882565,-1.300296,-6.250790,-5.108582,8.020042,-4.985410,8.480012,5.467530,-0.667152,-8.897748,-3.659844,-3.570893,8.573277,1.912899,-1.966693,-5.908284,2.425133,6.869462,-8.158051,-0.614293,-5.440743,8.522468,9.238589,-7.098352,-6.696806,-2.189311,-0.013950,-6.049869,-1.050673,-5.573604,-7.483202,7.501911,4.147839,5.126274,-2.717361,5.205750,-2.673066,-6.283223,-5.299930,0.135443,-6.085007,3.847752,-9.503822,-1.979044,4.459496,-2.833138,8.589782,0.923980,-3.354516,5.989834,-2.605116,-4.434282,5.481312,-6.551433,6.932752,-2.149788,7.704899,-6.262833,6.938697,3.790528,0.482946,-3.995521,0.555128,4.990238,-2.959686,-9.865299,-4.244557,5.549382,-0.715667,2.969448,-9.822336,1.541404,7.596962,3.152325,-2.119374,-9.931855,-2.993777,-6.995860,-2.963527,-1.724363,-4.584185,-1.568910,9.529775,4.212973,6.428501,2.930845,-0.109629,-2.181030,-9.980974,5.516136,-5.086916,9.717764,-9.494475,-4.658110,1.437936,-9.311520,9.303762,-4.480036,-6.420283,-8.218529,-2.139039,6.917462,-2.828931,8.096297,-3.572396,3.306817,-0.307775,3.183128,1.843130,8.749006,-1.510530,-4.314689,-8.812468,-8.018874,-0.596780,1.879744,-0.304184,-8.954759,-6.210751,-5.979733,-5.069863,1.488924,-4.929733,6.559781,-0.268879,-6.554101,-6.967253,-8.263314,-7.956344,-1.654971,-8.639550,8.202300,-7.205377,9.285853,2.131157,0.013883,-1.582255,-0.157451,-0.378171,-1.656149,6.816164,8.799889,7.257971,-1.524398,5.577276,4.527124,-9.258051,-5.540523,-9.916982,4.642473,5.215755,5.907281,1.633257,-9.194339,3.119656,-8.530953,-7.902788,9.809911,-6.968940,5.549786,-0.398677,7.821643,5.941909,8.716250,2.239065,-9.018611,-6.299617,-6.690508,9.660604,0.108975,1.288021,3.506506,9.736208,-5.044103,4.762168,4.091723,-3.556978,-7.469820,3.606933,8.612936,5.745117,4.698445,0.937997,7.757825,1.899451,0.526555,8.080708,-5.725721,1.101201,-4.069836,-4.099169,-1.179750,-9.876456,-4.657322,5.490976,-1.970381,1.514411,-5.604193,-6.727101,-3.997785,-2.224434,-0.819016,-1.144531,-7.566921,0.104499,-7.382859,3.446586,-4.606325,-0.033431,1.717596,-7.928022,-5.904910,8.876351,-1.745653,-7.992434,3.718965,1.373316,-5.462220,-7.742064,0.385292,0.936152,3.508306,4.868775,-5.853961,1.709491,9.794495,-5.303219,1.165811,-6.447752,1.263231,-2.434571,2.435272,-6.284906,-6.235022,-0.195133,9.011890],[7.224530,-8.261653,-5.862705,-7.224863,-3.913669,-0.682071,6.353411,7.772050,8.003998,6.078200,4.558045,8.869981,-1.638664,7.101303,-2.688631,8.052985,6.327062,-1.246563,-1.980314,4.250835,-2.965152,2.579792,-0.339621,2.793186,6.161440,9.330588,6.594910,5.980044,-5.223472,-7.830671,9.063986,8.339717,-5.783977,-9.535501,-6.575259,6.770826,3.384929,6.402748,7.723836,-0.793141,4.807454,-0.877871,-2.101892,-3.962600,-9.923458,6.868926,-3.112438,-2.859572,-1.117474,-6.794766,5.442613,1.503303,-7.277778,-2.428771,3.219287,1.749926,-8.350084,0.492932,0.460020,-5.335881,1.761311,2.461797,-9.149785,-5.401371,-7.078671,3.576268,-7.232726,5.933395,8.111960,0.178538,-0.614125,5.330950,-3.190240,0.316410,7.369989,1.183422,-0.968619,-4.222056,-4.957187,2.842608,8.456605,-8.833337,-3.177176,3.294190,4.495754,-4.935397,7.422423,1.036205,4.842236,2.176554,-9.958435,1.934620,4.557233,4.611959,-2.564744,-7.112981,3.308445,3.025828,-4.903998,-0.905933,9.776109,8.095761,-4.633098,-6.765821,-7.975881,-1.410111,-3.399781,6.729501,-7.109678,-6.134213,9.667414,-6.999065,7.836398,-1.205263,-4.699758,-2.191457,-0.690465,-8.556644,-7.091607,-4.049269,-3.251965,8.761810,-0.497489,-4.352307,7.719575,0.890120,-6.573906,5.917788,9.148665,5.792684,-4.107473,-7.899759,-3.029205,-2.912560,3.095951,8.186422,0.689646,5.855685,7.082466,-0.572819,-4.504323,2.490544,-3.083850,-0.376693,1.563503,1.038923,7.875949,-3.097012,3.943570,-5.693288,5.397128,-3.313039,-5.455486,-6.283913,-8.110602,-3.707602,-4.332917,2.901640,0.865336,-9.225988,6.801466,-0.779926,3.535891,-4.988818,1.137752,-7.166549,-2.076451,-0.933829,-4.374298,-2.800060,7.594205,2.349003,1.494144,-1.115344,-5.890252,5.210774,7.613634,9.425397,-6.257983,0.133250,-9.218598,-7.205254,-6.527269,-5.491523,7.391397,7.690032,7.608831,-3.186987,2.688819,8.776096,3.186087,-4.273421,5.772842,-8.899956,5.313765,7.903381,4.971802,1.825702,-6.324836,-1.655567,-7.059374,3.413321,-7.900238,-7.871187,-4.184463,4.694075,-7.021959,-4.945500,6.307714,2.457680,-4.283362,9.027359,-8.079502,-3.545210,-2.250249,-0.563021,-5.515853,-0.948448,2.945347,3.687670,0.713953,-9.257855,-2.925288,4.370449,2.843972,-3.971200,9.794660,9.973491,-0.761141,7.328850,-3.989830,-3.340041,6.577203,1.388751,5.707783,-2.277034,9.427949,3.530726,-4.024486,-4.270913,2.370988,6.626445,-2.786471,3.666465,-5.151610,2.843679,-0.915901,-9.573713,-6.282482,3.684181,-8.977612,-9.108509,-6.563278,1.520022,-1.563100,-3.333230,-0.175112,7.577735,-6.064386,-7.824635,0.633440,5.434397,2.999420,7.396223,4.181093,6.597565,-9.423478,2.080184,5.817358,4.407205,-1.469205,-7.173062,-4.648005,5.435661,-1.160573,0.834037,4.661660,3.590537,-6.219444,3.888832,1.964891,0.378108,-0.150736,-0.296333,1.177964,-7.610601,0.711612,2.503226,-6.743087,-1.387781,-9.366005,-7.482963,-7.327895,-0.508185,-9.264358,-2.076064,-0.218551,6.598934,1.089075,7.131404,-0.478131,-1.912843,-3.098559,0.447996,8.375809,2.765796,1.961672,3.895852,6.688697,0.439457,3.890008,-3.123085,4.749115,7.298333,0.945018,-8.127451,-2.869084,-7.120824,-5.638556,8.301748,8.549842,0.348325,-0.457589,3.456443,-7.435558,6.021435,-3.382746,4.802297,8.873960,-0.915018,3.578739,-5.019900,-7.371726,-3.953956,-0.829974,-8.073054,-7.222186,2.857471,-3.251025,7.941253,5.144948,9.734820,-4.902274,1.081869,1.914945,-0.444414,-6.907196,-7.325680,0.179014,0.474585,-0.250872,-3.102553,4.279361,2.872715,-5.067854,-9.715145,3.667588,8.224601,1.845202,5.901514,5.706342,8.318582,3.047545,-8.229022,6.663700,-7.232748,1.202802,-8.931959,-5.987048,-7.554817,-6.108226,-1.025931,-3.550342,0.101199,6.903187,-3.870880,7.502858,-1.667622,7.033001,0.497955,6.156647,-2.385261,-0.358449,7.097016,-7.284111,9.131280,3.392209,-5.752610,-4.129005,0.186056,6.618910,-0.606104,2.441802,6.029485,0.708286,8.218477,-5.927752,8.974758,5.058095,-5.523885,-8.713308,-2.588529,3.313381,-5.453771,3.340497,8.741057,7.095160,3.007929,6.544317,-5.723857,5.044839,4.553941,5.710914,3.590556,0.756096,5.776837,6.298085,6.622551,-4.968951,-8.747758,6.642287,-6.673577,3.721116,-4.930921,-6.732743,5.450545,-3.246936,-3.874763,9.912898,-5.278354,0.619125,4.991719],[-0.088908,4.123472,-2.779819,-5.950513,-3.398595,-7.812149,-7.971350,-3.805550,7.796194,-5.322403,-4.815348,-6.171123,-4.136155,-8.112838,-5.643700,6.567009,9.734065,9.587154,-0.162968,2.368477,6.044332,9.306653,-7.788762,-2.371964,6.572871,-5.848979,5.136474,-8.450950,8.416664,1.868952,-3.532457,-7.682452,-3.640049,7.359413,0.002565,8.308038,-9.935259,-1.272323,-2.110865,6.179216,-9.323988,4.891771,-8.950250,7.850211,-4.022508,9.846931,6.473821,-6.899488,1.821492,8.476328,2.466339,7.448387,9.362761,-9.848261,7.839157,7.088491,5.479379,6.585055,-3.694451,-0.621134,-5.159249,2.479131,2.131450,8.294439,1.606038,-5.177044,0.586273,5.111777,6.845097,-1.554202,8.473859,-4.529426,-3.795655,-6.896828,3.621059,5.204777,-7.567536,4.275658,1.377983,-2.979992,5.132040,4.697956,8.902451,7.888941,-0.856178,7.782584,-7.986408,9.134571,3.628221,0.122396,-8.743974,-3.641430,-4.984439,-1.925544,-8.018635,-7.466569,1.612921,-1.672579,-4.880939,-0.068157,1.576285,-9.487337,0.252194,-1.040561,9.995451,6.677210,4.949422,-8.063764,-6.099976,8.354966,-6.891285,-8.894899,2.271717,-0.213341,0.877378,-9.395801,-5.247808,-4.532091,-2.179201,-7.841228,-7.197824,7.795817,-3.674192,6.080752,9.744308,1.483377,5.211587,6.491700,8.337589,-5.984134,-2.078037,5.791326,-2.932527,0.356132,8.346644,-5.086390,1.232602,2.939791,-7.657147,-8.128234,1.144432,1.197198,-6.805340,7.393306,-4.967488,-3.457261,-7.198735,7.759433,1.788085,-6.836428,-2.286965,-1.311759,-8.759855,9.686441,3.322754,-2.038182,-8.740751,6.902673,2.072279,-5.812792,-7.756284,-4.072383,-0.203007,0.609134,-0.389074,-0.877042,6.945520,1.776254,-6.107156,-1.057864,-7.716952,-5.960046,-4.803800,1.771033,-6.610128,2.013221,-6.672439,-5.524935,4.205550,-3.069715,8.737346,-1.144378,-6.836524,-6.543451,6.322093,-4.439283,-5.736326,-4.043181,-0.229012,-7.764770,4.662936,8.924337,2.643470,-7.945750,-7.504192,5.515710,-6.367332,-4.449562,3.663944,8.040218,5.173501,-8.750667,8.243006,-5.996940,0.096316,-8.761063,-4.634856,-7.668838,1.252256,-6.976702,-0.886558,0.797744,2.018769,4.271864,7.797245,0.929626,-9.149865,-2.986347,-9.665020,7.807889,3.471333,-5.336312,7.316998,8.879957,-6.042369,-0.180332,5.272408,0.341641,7.706990,4.248600,0.056063,5.899954,9.755240,1.064978,-2.968391,1.198132,0.484507,4.331081,-5.278744,5.579558,-9.026917,8.318530,-1.726588,5.460898,0.262769,-9.231522,7.521568,-0.084617,4.446248,0.701034,-5.287191,7.067031,-2.897469,8.345703,9.380547,8.341633,-9.463900,-4.490576,7.363709,5.528022,-5.475918,-3.744825,4.875030,-2.286801,-7.517853,1.472845,-6.099960,-5.469853,7.946298,-5.187414,0.418434,8.913901,-7.843392,-3.550018,4.992986,9.573536,9.659663,2.671555,-2.871768,2.727898,7.875722,-4.318199,4.237860,5.510109,-3.203595,2.301464,1.672636,9.104059,-1.371260,-6.325670,5.462589,-1.287404,6.209910,-9.501045,8.970519,-9.442863,-5.524907,8.537749,-0.316861,-2.747263,-0.380750,-0.759434,-5.398486,2.610614,1.182828,-5.144778,5.870333,9.352767,0.211468,9.792241,7.145813,9.549332,-1.842622,3.083509,6.993998,3.644151,3.110221,-5.325399,3.111684,5.653724,6.898823,-9.022331,-3.444223,4.871796,1.472248,-2.842525,-0.940706,-8.686803,-1.468850,8.854132,0.858202,6.206979,-5.877231,3.015118,-2.733867,-5.011870,-9.696325,-9.696541,-4.103803,-1.977409,-5.469447,-7.610480,7.323389,3.167111,-8.514948,8.028297,8.996730,8.699748,-6.577532,-0.930067,1.248460,-2.475545,1.017283,-3.294968,-1.970961,0.653886,0.602292,-0.141448,-5.924780,6.214587,-2.972107,-7.688131,1.250505,-9.643232,-6.819997,-8.305743,8.859784,-0.352704,-3.700648,3.321864,9.328347,4.254169,-4.300731,1.029162,-2.216652,-5.472467,-1.419734,-8.383176,-0.775001,8.982542,1.522757,-4.741995,6.223001,2.595411,1.019927,-8.650344,7.101609,1.521656,7.039746,-5.193722,4.131609,0.371093,-8.704883,-2.215867,-5.163405,0.845241,5.466125,-7.595151,-3.677543,-9.994587,-0.850209,8.968659,8.958638,-3.573341,1.381605,-9.662489,8.141963,-4.126565,7.748346,-0.576203,2.303430,-0.216951,0.624132,1.335918,-0.180550,6.470931,-9.474165,0.652994,0.987735,3.687381,-8.148568,-0.223890,8.096076,0.770627,2.891947,-1.320229,-0.556318,0.691526,7.619078,6.985500,9.799137,1.447884]], dtype = "float64")#candidate|10156|(10, 432)|const|float64
bop_10157 = relay.divide(var_10148.astype('float64'), const_10156.astype('float64')) # shape=(10, 432)
func_5933_call = mod.get_global_var('func_5933')
func_5935_call = mutated_mod.get_global_var('func_5935')
call_10162 = func_5933_call()
call_10163 = func_5933_call()
output = relay.Tuple([call_10138,call_10145,call_10147,call_10152,bop_10157,call_10162,])
output2 = relay.Tuple([call_10139,call_10146,call_10149,call_10153,bop_10157,call_10163,])
func_10171 = relay.Function([var_10148,], output)
mod['func_10171'] = func_10171
mod = relay.transform.InferType()(mod)
var_10172 = relay.var("var_10172", dtype = "float64", shape = (1, 432))#candidate|10172|(1, 432)|var|float64
output = func_10171(var_10172)
func_10173 = relay.Function([var_10172], output)
mutated_mod['func_10173'] = func_10173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9481_call = mod.get_global_var('func_9481')
func_9483_call = mutated_mod.get_global_var('func_9483')
call_10226 = relay.TupleGetItem(func_9481_call(), 2)
call_10227 = relay.TupleGetItem(func_9483_call(), 2)
output = call_10226
output2 = call_10227
func_10228 = relay.Function([], output)
mod['func_10228'] = func_10228
mod = relay.transform.InferType()(mod)
output = func_10228()
func_10229 = relay.Function([], output)
mutated_mod['func_10229'] = func_10229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3403_call = mod.get_global_var('func_3403')
func_3405_call = mutated_mod.get_global_var('func_3405')
call_10323 = relay.TupleGetItem(func_3403_call(), 0)
call_10324 = relay.TupleGetItem(func_3405_call(), 0)
func_2362_call = mod.get_global_var('func_2362')
func_2364_call = mutated_mod.get_global_var('func_2364')
call_10329 = relay.TupleGetItem(func_2362_call(), 4)
call_10330 = relay.TupleGetItem(func_2364_call(), 4)
func_3648_call = mod.get_global_var('func_3648')
func_3651_call = mutated_mod.get_global_var('func_3651')
const_10359 = relay.const([4.568009,3.570771,-1.174173,-4.318048,5.388945,5.454561,-7.176336,-4.366288,9.780349,-6.687989,-1.612829,4.051439,7.779241,0.508580,0.430789,-3.315321,-1.801553,-7.077911,-0.654359,8.406361,-0.998135,-8.327707,-7.436590,5.858442,-5.845063,4.808073,-1.028820,7.118329,6.220532,8.316039,-5.651206,-1.369021,6.799240,6.259457,2.676727,6.055998,1.512441,-4.037707,-9.529293,-9.035884,8.499517,-3.524346,-0.589659,7.595241,-0.464541,7.550465,-7.095395,3.860959,-5.135182,3.755066,-2.684268,4.749210,-4.318716,9.433319,6.870440,5.283166,9.733790,8.087788,-1.719370,-1.984810,8.442423,3.212434,0.598338,5.962036,1.517303,7.654492,5.171020,-4.848124,-4.071032,-9.609129,0.500439,-9.850615,1.709947,-1.832865,-7.221460,-3.774731,-1.909968,4.827477,5.039601,8.632802,3.142858,-3.783452,-7.378501,-0.170486,-3.889819,-7.655773,4.917431,-5.434806,-0.309071,-8.792190,7.989724,-9.380877,-8.230091,1.541372,-5.009767,-9.771849,8.640977,-5.190422,4.779108,-8.000568,-3.727296,2.445063,7.971226,-7.038753,9.217034,-4.997257,-4.307478,-6.998536,-3.315854,-0.094109,4.329781,-5.603796,3.151668,-8.210726,-4.946586,-1.853653,8.563698,-8.439686,9.227945,5.005299,2.147864,-0.927674,-3.376034,-1.854697,-1.669527,-6.991593,6.258573,6.644182,4.908997,-1.957672], dtype = "float64")#candidate|10359|(130,)|const|float64
call_10358 = relay.TupleGetItem(func_3648_call(relay.reshape(const_10359.astype('float64'), [10, 13, 1])), 0)
call_10360 = relay.TupleGetItem(func_3651_call(relay.reshape(const_10359.astype('float64'), [10, 13, 1])), 0)
output = relay.Tuple([call_10323,call_10329,call_10358,const_10359,])
output2 = relay.Tuple([call_10324,call_10330,call_10360,const_10359,])
func_10366 = relay.Function([], output)
mod['func_10366'] = func_10366
mod = relay.transform.InferType()(mod)
output = func_10366()
func_10367 = relay.Function([], output)
mutated_mod['func_10367'] = func_10367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7540_call = mod.get_global_var('func_7540')
func_7541_call = mutated_mod.get_global_var('func_7541')
call_10393 = func_7540_call()
call_10394 = func_7540_call()
output = call_10393
output2 = call_10394
func_10397 = relay.Function([], output)
mod['func_10397'] = func_10397
mod = relay.transform.InferType()(mod)
mutated_mod['func_10397'] = func_10397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10397_call = mutated_mod.get_global_var('func_10397')
call_10398 = func_10397_call()
output = call_10398
func_10399 = relay.Function([], output)
mutated_mod['func_10399'] = func_10399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6713_call = mod.get_global_var('func_6713')
func_6715_call = mutated_mod.get_global_var('func_6715')
call_10470 = relay.TupleGetItem(func_6713_call(), 1)
call_10471 = relay.TupleGetItem(func_6715_call(), 1)
func_8430_call = mod.get_global_var('func_8430')
func_8431_call = mutated_mod.get_global_var('func_8431')
call_10488 = relay.TupleGetItem(func_8430_call(), 1)
call_10489 = relay.TupleGetItem(func_8431_call(), 1)
func_5971_call = mod.get_global_var('func_5971')
func_5973_call = mutated_mod.get_global_var('func_5973')
call_10506 = relay.TupleGetItem(func_5971_call(), 1)
call_10507 = relay.TupleGetItem(func_5973_call(), 1)
output = relay.Tuple([call_10470,call_10488,call_10506,])
output2 = relay.Tuple([call_10471,call_10489,call_10507,])
func_10510 = relay.Function([], output)
mod['func_10510'] = func_10510
mod = relay.transform.InferType()(mod)
mutated_mod['func_10510'] = func_10510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10510_call = mutated_mod.get_global_var('func_10510')
call_10511 = func_10510_call()
output = call_10511
func_10512 = relay.Function([], output)
mutated_mod['func_10512'] = func_10512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6144_call = mod.get_global_var('func_6144')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_10528 = func_6144_call()
call_10529 = func_6144_call()
output = call_10528
output2 = call_10529
func_10541 = relay.Function([], output)
mod['func_10541'] = func_10541
mod = relay.transform.InferType()(mod)
mutated_mod['func_10541'] = func_10541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10541_call = mutated_mod.get_global_var('func_10541')
call_10542 = func_10541_call()
output = call_10542
func_10543 = relay.Function([], output)
mutated_mod['func_10543'] = func_10543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1699_call = mod.get_global_var('func_1699')
func_1700_call = mutated_mod.get_global_var('func_1700')
call_10548 = relay.TupleGetItem(func_1699_call(), 0)
call_10549 = relay.TupleGetItem(func_1700_call(), 0)
func_650_call = mod.get_global_var('func_650')
func_652_call = mutated_mod.get_global_var('func_652')
call_10563 = relay.TupleGetItem(func_650_call(), 1)
call_10564 = relay.TupleGetItem(func_652_call(), 1)
output = relay.Tuple([call_10548,call_10563,])
output2 = relay.Tuple([call_10549,call_10564,])
func_10565 = relay.Function([], output)
mod['func_10565'] = func_10565
mod = relay.transform.InferType()(mod)
output = func_10565()
func_10566 = relay.Function([], output)
mutated_mod['func_10566'] = func_10566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9309_call = mod.get_global_var('func_9309')
func_9311_call = mutated_mod.get_global_var('func_9311')
call_10580 = relay.TupleGetItem(func_9309_call(), 0)
call_10581 = relay.TupleGetItem(func_9311_call(), 0)
output = relay.Tuple([call_10580,])
output2 = relay.Tuple([call_10581,])
func_10597 = relay.Function([], output)
mod['func_10597'] = func_10597
mod = relay.transform.InferType()(mod)
mutated_mod['func_10597'] = func_10597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10597_call = mutated_mod.get_global_var('func_10597')
call_10598 = func_10597_call()
output = call_10598
func_10599 = relay.Function([], output)
mutated_mod['func_10599'] = func_10599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8596_call = mod.get_global_var('func_8596')
func_8597_call = mutated_mod.get_global_var('func_8597')
call_10646 = relay.TupleGetItem(func_8596_call(), 0)
call_10647 = relay.TupleGetItem(func_8597_call(), 0)
output = call_10646
output2 = call_10647
func_10660 = relay.Function([], output)
mod['func_10660'] = func_10660
mod = relay.transform.InferType()(mod)
mutated_mod['func_10660'] = func_10660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10660_call = mutated_mod.get_global_var('func_10660')
call_10661 = func_10660_call()
output = call_10661
func_10662 = relay.Function([], output)
mutated_mod['func_10662'] = func_10662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5668_call = mod.get_global_var('func_5668')
func_5670_call = mutated_mod.get_global_var('func_5670')
call_10676 = relay.TupleGetItem(func_5668_call(), 0)
call_10677 = relay.TupleGetItem(func_5670_call(), 0)
var_10685 = relay.var("var_10685", dtype = "float32", shape = (13, 14, 5))#candidate|10685|(13, 14, 5)|var|float32
bop_10686 = relay.logical_and(call_10676.astype('bool'), relay.reshape(var_10685.astype('bool'), relay.shape_of(call_10676))) # shape=(13, 14, 5)
bop_10689 = relay.logical_and(call_10677.astype('bool'), relay.reshape(var_10685.astype('bool'), relay.shape_of(call_10677))) # shape=(13, 14, 5)
func_8735_call = mod.get_global_var('func_8735')
func_8737_call = mutated_mod.get_global_var('func_8737')
call_10693 = func_8735_call()
call_10694 = func_8735_call()
output = relay.Tuple([bop_10686,call_10693,])
output2 = relay.Tuple([bop_10689,call_10694,])
func_10695 = relay.Function([var_10685,], output)
mod['func_10695'] = func_10695
mod = relay.transform.InferType()(mod)
mutated_mod['func_10695'] = func_10695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10696 = relay.var("var_10696", dtype = "float32", shape = (13, 14, 5))#candidate|10696|(13, 14, 5)|var|float32
func_10695_call = mutated_mod.get_global_var('func_10695')
call_10697 = func_10695_call(var_10696)
output = call_10697
func_10698 = relay.Function([var_10696], output)
mutated_mod['func_10698'] = func_10698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8723_call = mod.get_global_var('func_8723')
func_8725_call = mutated_mod.get_global_var('func_8725')
call_10714 = relay.TupleGetItem(func_8723_call(), 0)
call_10715 = relay.TupleGetItem(func_8725_call(), 0)
output = call_10714
output2 = call_10715
func_10724 = relay.Function([], output)
mod['func_10724'] = func_10724
mod = relay.transform.InferType()(mod)
mutated_mod['func_10724'] = func_10724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10724_call = mutated_mod.get_global_var('func_10724')
call_10725 = func_10724_call()
output = call_10725
func_10726 = relay.Function([], output)
mutated_mod['func_10726'] = func_10726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6076_call = mod.get_global_var('func_6076')
func_6078_call = mutated_mod.get_global_var('func_6078')
call_10742 = relay.TupleGetItem(func_6076_call(), 0)
call_10743 = relay.TupleGetItem(func_6078_call(), 0)
output = call_10742
output2 = call_10743
func_10771 = relay.Function([], output)
mod['func_10771'] = func_10771
mod = relay.transform.InferType()(mod)
mutated_mod['func_10771'] = func_10771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10771_call = mutated_mod.get_global_var('func_10771')
call_10772 = func_10771_call()
output = call_10772
func_10773 = relay.Function([], output)
mutated_mod['func_10773'] = func_10773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9936_call = mod.get_global_var('func_9936')
func_9937_call = mutated_mod.get_global_var('func_9937')
call_10809 = relay.TupleGetItem(func_9936_call(), 0)
call_10810 = relay.TupleGetItem(func_9937_call(), 0)
func_5899_call = mod.get_global_var('func_5899')
func_5903_call = mutated_mod.get_global_var('func_5903')
var_10814 = relay.var("var_10814", dtype = "int8", shape = (1, 75))#candidate|10814|(1, 75)|var|int8
var_10815 = relay.var("var_10815", dtype = "int8", shape = (975,))#candidate|10815|(975,)|var|int8
const_10816 = relay.const([9.629138,-7.745276,1.448867,-9.534857,7.926978,3.916351,-6.079729,-6.383772,6.708776,-7.944488,5.987005,-8.207774,-9.814330,-3.743268,-7.134017,-1.387858,7.923324,0.939141,5.902153,0.865955,-4.758852,0.629000,-4.453918,8.269463,-6.317227,5.709474,0.066649,-6.359978,5.597553,-9.938408,-6.584011,-9.399151,9.073687,8.297656,8.148095,5.907224,3.175636,1.219257,-7.746826,4.938489,-3.777422,-0.113079,-0.163578,5.774480,1.164729,-4.652015,-1.308823,-9.771579,-8.926271,-9.559984,-7.439483,-4.657444,0.423598,-2.941327,-3.186114,-8.486891,-9.755968,8.026778,7.052812,6.707326,-9.955427,2.397809,-0.992047,-2.392593,4.412954,-0.917390,-4.805919,0.839182,-0.252626,0.370891,-0.570649,6.808164,-4.023924,5.123599,-2.176112,3.660568,-0.367159,7.504281,-5.758139,-4.517912,1.573278,3.953571,1.862824,9.371818,-8.591528,-4.627093,-1.570302,-7.491735,-7.455211,0.214081,-1.504324,5.017772,3.840599,8.746560,-3.477911,8.032701,-5.973809,9.129591,9.386155,-6.581880,9.721469,-3.373308,-6.966559,1.866570,4.534091], dtype = "float64")#candidate|10816|(105,)|const|float64
call_10813 = relay.TupleGetItem(func_5899_call(relay.reshape(var_10814.astype('int8'), [5, 15, 1]), relay.reshape(var_10815.astype('int8'), [5, 15, 13]), relay.reshape(const_10816.astype('float64'), [105,]), ), 1)
call_10817 = relay.TupleGetItem(func_5903_call(relay.reshape(var_10814.astype('int8'), [5, 15, 1]), relay.reshape(var_10815.astype('int8'), [5, 15, 13]), relay.reshape(const_10816.astype('float64'), [105,]), ), 1)
bop_10824 = relay.right_shift(call_10813.astype('int32'), call_10809.astype('int32')) # shape=(2, 13, 105)
bop_10827 = relay.right_shift(call_10817.astype('int32'), call_10810.astype('int32')) # shape=(2, 13, 105)
bop_10837 = relay.logical_and(const_10816.astype('bool'), call_10809.astype('bool')) # shape=(2, 13, 105)
bop_10840 = relay.logical_and(const_10816.astype('bool'), call_10810.astype('bool')) # shape=(2, 13, 105)
func_9481_call = mod.get_global_var('func_9481')
func_9483_call = mutated_mod.get_global_var('func_9483')
call_10843 = relay.TupleGetItem(func_9481_call(), 2)
call_10844 = relay.TupleGetItem(func_9483_call(), 2)
output = relay.Tuple([var_10814,var_10815,bop_10824,bop_10837,call_10843,])
output2 = relay.Tuple([var_10814,var_10815,bop_10827,bop_10840,call_10844,])
func_10847 = relay.Function([var_10814,var_10815,], output)
mod['func_10847'] = func_10847
mod = relay.transform.InferType()(mod)
mutated_mod['func_10847'] = func_10847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10847_call = mutated_mod.get_global_var('func_10847')
var_10849 = relay.var("var_10849", dtype = "int8", shape = (1, 75))#candidate|10849|(1, 75)|var|int8
var_10850 = relay.var("var_10850", dtype = "int8", shape = (975,))#candidate|10850|(975,)|var|int8
call_10848 = func_10847_call(var_10849,var_10850,)
output = call_10848
func_10851 = relay.Function([var_10849,var_10850,], output)
mutated_mod['func_10851'] = func_10851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6713_call = mod.get_global_var('func_6713')
func_6715_call = mutated_mod.get_global_var('func_6715')
call_10880 = relay.TupleGetItem(func_6713_call(), 0)
call_10881 = relay.TupleGetItem(func_6715_call(), 0)
func_8735_call = mod.get_global_var('func_8735')
func_8737_call = mutated_mod.get_global_var('func_8737')
call_10891 = func_8735_call()
call_10892 = func_8735_call()
output = relay.Tuple([call_10880,call_10891,])
output2 = relay.Tuple([call_10881,call_10892,])
func_10910 = relay.Function([], output)
mod['func_10910'] = func_10910
mod = relay.transform.InferType()(mod)
output = func_10910()
func_10911 = relay.Function([], output)
mutated_mod['func_10911'] = func_10911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4886_call = mod.get_global_var('func_4886')
func_4888_call = mutated_mod.get_global_var('func_4888')
call_10954 = relay.TupleGetItem(func_4886_call(), 2)
call_10955 = relay.TupleGetItem(func_4888_call(), 2)
output = relay.Tuple([call_10954,])
output2 = relay.Tuple([call_10955,])
func_10972 = relay.Function([], output)
mod['func_10972'] = func_10972
mod = relay.transform.InferType()(mod)
output = func_10972()
func_10973 = relay.Function([], output)
mutated_mod['func_10973'] = func_10973
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5436_call = mod.get_global_var('func_5436')
func_5437_call = mutated_mod.get_global_var('func_5437')
call_11020 = func_5436_call()
call_11021 = func_5436_call()
output = call_11020
output2 = call_11021
func_11024 = relay.Function([], output)
mod['func_11024'] = func_11024
mod = relay.transform.InferType()(mod)
mutated_mod['func_11024'] = func_11024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11024_call = mutated_mod.get_global_var('func_11024')
call_11025 = func_11024_call()
output = call_11025
func_11026 = relay.Function([], output)
mutated_mod['func_11026'] = func_11026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8015_call = mutated_mod.get_global_var('func_8015')
call_11050 = relay.TupleGetItem(func_8014_call(), 2)
call_11051 = relay.TupleGetItem(func_8015_call(), 2)
output = relay.Tuple([call_11050,])
output2 = relay.Tuple([call_11051,])
func_11058 = relay.Function([], output)
mod['func_11058'] = func_11058
mod = relay.transform.InferType()(mod)
mutated_mod['func_11058'] = func_11058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11058_call = mutated_mod.get_global_var('func_11058')
call_11059 = func_11058_call()
output = call_11059
func_11060 = relay.Function([], output)
mutated_mod['func_11060'] = func_11060
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11084 = relay.var("var_11084", dtype = "uint16", shape = ())#candidate|11084|()|var|uint16
var_11085 = relay.var("var_11085", dtype = "uint16", shape = (1, 6, 12))#candidate|11085|(1, 6, 12)|var|uint16
bop_11086 = relay.greater(var_11084.astype('bool'), var_11085.astype('bool')) # shape=(1, 6, 12)
func_9309_call = mod.get_global_var('func_9309')
func_9311_call = mutated_mod.get_global_var('func_9311')
call_11089 = relay.TupleGetItem(func_9309_call(), 0)
call_11090 = relay.TupleGetItem(func_9311_call(), 0)
output = relay.Tuple([bop_11086,call_11089,])
output2 = relay.Tuple([bop_11086,call_11090,])
func_11099 = relay.Function([var_11084,var_11085,], output)
mod['func_11099'] = func_11099
mod = relay.transform.InferType()(mod)
var_11100 = relay.var("var_11100", dtype = "uint16", shape = ())#candidate|11100|()|var|uint16
var_11101 = relay.var("var_11101", dtype = "uint16", shape = (1, 6, 12))#candidate|11101|(1, 6, 12)|var|uint16
output = func_11099(var_11100,var_11101,)
func_11102 = relay.Function([var_11100,var_11101,], output)
mutated_mod['func_11102'] = func_11102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7540_call = mod.get_global_var('func_7540')
func_7541_call = mutated_mod.get_global_var('func_7541')
call_11109 = func_7540_call()
call_11110 = func_7540_call()
func_6144_call = mod.get_global_var('func_6144')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_11112 = func_6144_call()
call_11113 = func_6144_call()
const_11117 = relay.const([[[7,1,10,8],[9,-2,-1,2],[10,-5,1,-10],[-1,1,-7,7],[7,-3,4,-6],[-9,-9,-3,-6],[-2,7,-8,-10],[-1,6,-6,-1],[-1,-9,6,-7],[4,-7,-5,-10],[-5,2,-6,-4],[-1,-5,3,1],[-10,10,-6,3]],[[1,8,5,6],[-7,-3,1,9],[10,-1,10,9],[-2,8,-6,-9],[2,-6,7,7],[10,-6,7,-3],[7,-10,-5,7],[-9,-5,-7,-3],[-4,-8,-1,-5],[-4,10,-6,10],[6,-10,-8,6],[5,2,8,3],[-4,-4,-5,-6]]], dtype = "uint32")#candidate|11117|(2, 13, 4)|const|uint32
bop_11118 = relay.bitwise_or(call_11109.astype('int8'), const_11117.astype('int8')) # shape=(2, 13, 4)
bop_11121 = relay.bitwise_or(call_11110.astype('int8'), const_11117.astype('int8')) # shape=(2, 13, 4)
func_3474_call = mod.get_global_var('func_3474')
func_3477_call = mutated_mod.get_global_var('func_3477')
var_11134 = relay.var("var_11134", dtype = "float32", shape = (84, 1))#candidate|11134|(84, 1)|var|float32
call_11133 = relay.TupleGetItem(func_3474_call(relay.reshape(var_11134.astype('float32'), [84,])), 1)
call_11135 = relay.TupleGetItem(func_3477_call(relay.reshape(var_11134.astype('float32'), [84,])), 1)
output = relay.Tuple([call_11112,bop_11118,call_11133,var_11134,])
output2 = relay.Tuple([call_11113,bop_11121,call_11135,var_11134,])
func_11136 = relay.Function([var_11134,], output)
mod['func_11136'] = func_11136
mod = relay.transform.InferType()(mod)
mutated_mod['func_11136'] = func_11136
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11137 = relay.var("var_11137", dtype = "float32", shape = (84, 1))#candidate|11137|(84, 1)|var|float32
func_11136_call = mutated_mod.get_global_var('func_11136')
call_11138 = func_11136_call(var_11137)
output = call_11138
func_11139 = relay.Function([var_11137], output)
mutated_mod['func_11139'] = func_11139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11231 = relay.var("var_11231", dtype = "int16", shape = (5, 4, 16))#candidate|11231|(5, 4, 16)|var|int16
var_11232 = relay.var("var_11232", dtype = "int16", shape = (5, 4, 16))#candidate|11232|(5, 4, 16)|var|int16
bop_11233 = relay.greater(var_11231.astype('bool'), relay.reshape(var_11232.astype('bool'), relay.shape_of(var_11231))) # shape=(5, 4, 16)
uop_11243 = relay.sigmoid(var_11231.astype('float64')) # shape=(5, 4, 16)
output = relay.Tuple([bop_11233,uop_11243,])
output2 = relay.Tuple([bop_11233,uop_11243,])
func_11247 = relay.Function([var_11231,var_11232,], output)
mod['func_11247'] = func_11247
mod = relay.transform.InferType()(mod)
var_11248 = relay.var("var_11248", dtype = "int16", shape = (5, 4, 16))#candidate|11248|(5, 4, 16)|var|int16
var_11249 = relay.var("var_11249", dtype = "int16", shape = (5, 4, 16))#candidate|11249|(5, 4, 16)|var|int16
output = func_11247(var_11248,var_11249,)
func_11250 = relay.Function([var_11248,var_11249,], output)
mutated_mod['func_11250'] = func_11250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7571_call = mod.get_global_var('func_7571')
func_7572_call = mutated_mod.get_global_var('func_7572')
call_11318 = relay.TupleGetItem(func_7571_call(), 0)
call_11319 = relay.TupleGetItem(func_7572_call(), 0)
func_1513_call = mod.get_global_var('func_1513')
func_1516_call = mutated_mod.get_global_var('func_1516')
var_11332 = relay.var("var_11332", dtype = "float32", shape = (880,))#candidate|11332|(880,)|var|float32
call_11331 = relay.TupleGetItem(func_1513_call(relay.reshape(var_11332.astype('float32'), [4, 220])), 0)
call_11333 = relay.TupleGetItem(func_1516_call(relay.reshape(var_11332.astype('float32'), [4, 220])), 0)
func_5668_call = mod.get_global_var('func_5668')
func_5670_call = mutated_mod.get_global_var('func_5670')
call_11337 = relay.TupleGetItem(func_5668_call(), 0)
call_11338 = relay.TupleGetItem(func_5670_call(), 0)
output = relay.Tuple([call_11318,call_11331,var_11332,call_11337,])
output2 = relay.Tuple([call_11319,call_11333,var_11332,call_11338,])
func_11348 = relay.Function([var_11332,], output)
mod['func_11348'] = func_11348
mod = relay.transform.InferType()(mod)
var_11349 = relay.var("var_11349", dtype = "float32", shape = (880,))#candidate|11349|(880,)|var|float32
output = func_11348(var_11349)
func_11350 = relay.Function([var_11349], output)
mutated_mod['func_11350'] = func_11350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8596_call = mod.get_global_var('func_8596')
func_8597_call = mutated_mod.get_global_var('func_8597')
call_11436 = relay.TupleGetItem(func_8596_call(), 0)
call_11437 = relay.TupleGetItem(func_8597_call(), 0)
func_4284_call = mod.get_global_var('func_4284')
func_4290_call = mutated_mod.get_global_var('func_4290')
const_11451 = relay.const([[-6],[-4],[-3],[1],[6],[-5],[10],[-6],[2],[6],[-10],[-7],[-1],[9],[-8],[2],[-3],[-5],[5],[-8],[3],[-1],[1],[-4],[9],[-6],[6],[-9],[8],[10],[-1],[1],[1],[10],[-2],[-7],[4],[-10],[5],[-8],[3],[-5],[-7],[-7],[2],[-4],[2],[-7],[-3],[-8],[-7],[-10],[1],[6],[3],[2],[9],[-6],[-10],[5],[10],[5],[5],[2],[-8],[3],[-5],[6],[2],[-4],[5],[-10],[1],[-3],[8],[-3],[7],[10],[-7],[-2],[-5],[8],[-7],[-6],[6],[3],[-3],[-8],[-10],[5],[8],[6],[-3],[7],[-9],[5],[-3],[3],[-9],[8],[-8],[9],[-3],[-6],[-5],[-1],[-9],[8],[1],[4],[-6],[5],[-3],[-9],[7],[10],[-6],[9],[-3],[2],[-5],[10],[-10],[-8],[6],[3],[10],[-1],[-8],[7],[-8],[3],[3],[5],[6],[-3],[2],[7],[-4],[3],[4],[1],[-5],[8],[5],[-1],[10],[8],[7],[-9],[-5],[-5],[8],[7],[6],[9],[5],[7],[4],[-5],[9],[-3],[1],[2],[7],[10],[4],[8],[-9],[3],[4],[-7],[-3],[1],[10],[-8],[2],[-5],[3],[1],[-9],[-1],[-8],[6],[-4],[3],[2],[-9],[6],[4],[-7],[-4],[2],[-2],[-7],[4],[-5],[10],[5],[-1],[4],[9],[7],[2],[-9],[1],[9],[-5],[-5],[7],[-1],[9],[-7],[1],[4],[3],[7],[-5],[-9],[10],[-3],[3],[6],[-2],[-6],[-2],[-1],[5],[9],[-2],[-8],[-2],[-8],[-1],[-4],[-6],[-2],[1],[-7],[-9],[-4],[-8],[-4],[-5],[-8],[8],[3],[-3],[7],[-9],[-5],[-1],[3],[6],[-5],[-1],[-8],[3],[3],[-4],[6],[-9],[2],[-1],[7],[3],[4],[10],[-4],[-5],[1],[-9],[6],[-10],[-2],[2],[-8],[9],[4],[-2],[-10],[5],[-9],[-1],[-1],[-3],[4],[-1],[5],[-1],[-10],[7],[5],[-10],[3],[-4],[-9],[9],[1],[-2],[-8],[-5],[8],[-7],[1],[-2],[-3],[9],[-2],[-1],[-2],[-10],[-1],[8],[8],[-6],[-4],[3],[1],[7],[-7],[1],[7],[-10],[-8],[5],[-5],[1],[-5],[1],[7],[-2],[-2],[-5],[4],[-3],[10],[-1],[-3],[-5],[3],[2],[-7],[7],[2],[-5],[-9],[3],[3],[-2],[-9],[-8],[-10],[-5],[3],[7],[10],[-5],[2],[8],[1],[-4],[2],[2],[5],[-4],[1],[-3],[-2],[-8],[-10],[10],[-6],[-8],[-8],[4],[-2],[2],[6],[-1],[7],[7],[-7],[3],[-1],[-2],[-7],[1],[-7],[2],[5],[-7],[-6],[3],[10],[-5],[9],[-9],[4],[-8],[4],[-6],[-4],[4],[5],[-7],[4],[9],[2],[4],[-6],[-10],[-10],[-3],[-10],[9],[-1],[-5],[-3],[-6],[-7],[-1],[8],[10],[2],[3],[10],[-4],[4],[-9],[8],[-10],[-3],[6],[6],[-4],[-9],[-1],[-7],[-9],[3],[-6],[7],[7],[9],[6],[4],[-8],[1],[-4],[-10],[-7],[5],[7],[10],[-10],[8],[-8],[-6],[-6],[3],[-4],[-6],[-5],[-8],[3],[7],[-8]], dtype = "int64")#candidate|11451|(468, 1)|const|int64
var_11452 = relay.var("var_11452", dtype = "float32", shape = (84,))#candidate|11452|(84,)|var|float32
const_11453 = relay.const([[-8.744969,-4.753269,0.218037,-3.069957,2.897114,-8.203892,9.157184,5.858168,-2.426040,-3.491244,-1.470456,2.178501,3.863030,9.452759,6.679646,-6.393422,9.255984,6.240631,-7.935446,8.362226,9.497409,-3.772755,8.926449,-3.835262,-1.693975,8.598884,-2.995758,0.137362,7.988751,7.270454,-5.498221,3.585217,-7.827816,-0.681854,-3.106176,7.882257,-0.585060,-6.110730,9.075328,9.273947,6.290604,-8.559689],[-9.842409,2.424130,4.775952,-4.678900,-0.092273,8.859348,-3.048029,1.558732,2.261022,3.422674,-8.019858,5.328595,-6.430623,0.352664,2.081514,1.415226,-6.876328,-2.490613,1.333063,8.382345,-3.506465,6.435334,3.020144,7.415888,0.889234,-6.024186,-1.325517,3.235296,-1.445364,0.421777,-9.521487,9.745458,5.491571,-1.056024,6.498500,1.756665,-1.138984,-0.045416,8.084449,3.281185,-8.795973,9.171935],[2.086017,-6.654760,4.077024,-5.586241,-7.948178,-2.299061,7.285493,9.710211,8.762243,-5.372046,0.750841,4.338509,-5.217624,3.940882,-1.644617,1.198661,4.790701,5.630575,4.177688,-6.053877,-9.545090,-2.481483,-5.386637,-1.844460,-4.904861,5.603759,1.956282,-2.379226,9.020054,7.726462,-7.632912,-2.917649,-7.730393,5.399863,1.946495,0.969033,-2.403025,8.929627,1.260682,-5.895113,-3.352144,1.026594],[-9.854746,0.242298,0.861668,4.796309,5.279988,7.097012,-6.343763,-0.578734,1.812685,3.848319,8.190769,-3.467474,-2.557823,-7.662305,-4.498294,-6.765077,7.362477,3.312290,-2.745876,0.281163,-5.425645,4.656057,6.580467,-8.599282,-5.297963,-7.289437,-8.616858,-8.747251,-3.975873,8.951175,0.673160,8.169727,1.744510,1.752614,-3.212202,3.382323,-7.086320,3.168247,-3.587881,-3.946731,4.614983,-6.255298],[2.710408,-9.526185,2.118317,-8.966841,6.071277,-6.732540,-5.781349,4.364191,-1.780859,9.949554,5.619619,-8.733827,-8.481549,-2.811698,3.646796,3.764798,-7.085170,-6.051808,8.052336,-8.830908,8.072763,1.362424,-8.428686,-7.176816,-5.049366,4.911560,-2.587078,3.456282,-8.381856,-5.383987,9.169715,-8.637376,2.858644,7.603296,-7.026145,7.563797,-9.847922,2.890869,6.185242,7.045278,-5.049843,-3.669185],[-1.448090,9.683630,5.915546,8.531774,-2.438541,-1.607532,-3.191709,-9.390850,7.633509,-2.352599,4.073087,5.354724,0.708518,-7.344872,2.356169,-1.467332,-7.953294,0.305372,4.131168,-4.860719,-3.436563,2.462498,0.627640,8.575649,-0.081806,-8.242290,-1.408679,-7.527018,0.554504,6.866904,9.127632,-4.008907,7.520651,-7.990222,-1.548871,-4.972833,4.571806,-1.262936,-6.101471,-0.218725,9.805536,-4.506797],[-6.275543,-6.944953,9.074463,-2.802463,6.847614,-4.407247,-3.879632,-3.045036,-9.534837,-8.391096,-5.599198,-2.924783,-9.056220,5.895299,1.373340,2.578920,3.031602,9.830747,7.035343,3.481273,8.376074,-8.661531,-2.745983,-4.054036,5.088732,6.009928,6.420018,-6.409850,-5.914416,-0.984131,0.861847,9.786613,6.629550,7.503090,-9.739919,0.754691,3.924519,-7.069305,-6.457625,-7.823593,1.885909,-2.277702]], dtype = "float32")#candidate|11453|(7, 42)|const|float32
call_11450 = relay.TupleGetItem(func_4284_call(relay.reshape(const_11451.astype('int64'), [6, 13, 6]), relay.reshape(const_11451.astype('int64'), [6, 13, 6]), relay.reshape(const_11451.astype('float64'), [6, 13, 6]), relay.reshape(var_11452.astype('float32'), [84,]), relay.reshape(const_11453.astype('float32'), [294,]), ), 9)
call_11454 = relay.TupleGetItem(func_4290_call(relay.reshape(const_11451.astype('int64'), [6, 13, 6]), relay.reshape(const_11451.astype('int64'), [6, 13, 6]), relay.reshape(const_11451.astype('float64'), [6, 13, 6]), relay.reshape(var_11452.astype('float32'), [84,]), relay.reshape(const_11453.astype('float32'), [294,]), ), 9)
bop_11457 = relay.mod(var_11452.astype('float64'), const_11451.astype('float64')) # shape=(468, 84)
func_3011_call = mod.get_global_var('func_3011')
func_3013_call = mutated_mod.get_global_var('func_3013')
call_11462 = func_3011_call()
call_11463 = func_3011_call()
var_11464 = relay.var("var_11464", dtype = "int64", shape = (468, 1))#candidate|11464|(468, 1)|var|int64
bop_11465 = relay.not_equal(const_11451.astype('bool'), relay.reshape(var_11464.astype('bool'), relay.shape_of(const_11451))) # shape=(468, 1)
var_11468 = relay.var("var_11468", dtype = "int64", shape = (468, 15))#candidate|11468|(468, 15)|var|int64
bop_11469 = relay.minimum(const_11451.astype('uint8'), var_11468.astype('uint8')) # shape=(468, 15)
bop_11472 = relay.less_equal(bop_11469.astype('bool'), const_11451.astype('bool')) # shape=(468, 15)
func_1513_call = mod.get_global_var('func_1513')
func_1516_call = mutated_mod.get_global_var('func_1516')
const_11481 = relay.const([-8.811862,3.363879,-8.794493,-0.104999,-0.588590,1.290109,-9.687486,-0.200001,-1.076728,7.432516,-0.450120,-9.061977,4.239474,-7.661057,-5.070609,7.842858,4.662794,9.700530,4.523823,-6.401474,8.371987,-6.122048,-2.738050,-1.264499,8.173804,-9.907004,0.415954,7.691396,8.856658,0.600133,-5.209783,-8.674112,4.528028,6.049525,0.957180,-8.756030,0.951576,-5.011803,4.392604,4.949477,3.855015,-6.326052,-9.584398,2.337031,-8.330378,-8.556401,0.621216,-8.695447,-0.020895,1.271173,3.489933,5.991163,-6.738896,-5.851154,-8.368008,-0.724246,0.538168,-5.723885,-7.486115,7.559922,-1.543038,-9.754246,-4.074664,-3.093759,-6.796287,4.326146,-4.311359,8.761893,-9.398887,-1.256397,4.121547,-8.296095,-6.418218,-8.369513,-5.769650,6.303685,0.660195,-0.909417,-4.770541,0.389805,-4.368358,7.276784,6.316152,7.095613,-6.118551,-5.374233,8.891194,3.883921,4.362475,-3.818555,1.788748,-0.910284,5.214030,8.492595,0.428988,0.860263,9.082996,-4.944841,6.874707,-0.176798,-7.715010,0.812614,-0.833131,7.834288,-2.653860,8.860042,6.236845,8.971871,5.230701,-3.294511,2.339005,-1.080645,-4.936584,4.959377,9.190266,-6.819644,-4.337061,3.474951,-9.633188,-2.572465,-6.475327,-4.418850,0.850448,2.230950,-4.459422,3.445340,3.327469,-8.727974,9.029561,0.170378,-0.373919,-9.053483,5.267541,6.962383,-6.356756,-5.901246,4.255948,-7.567740,-6.047240,9.142162,5.255322,-5.867485,1.673975,5.754335,-1.005019,8.966213,-2.265927,7.645194,4.255254,3.728211,-5.604907,-1.772512,-2.106526,-3.193382,-3.582571,-9.230875,2.086626,-1.453515,8.369707,2.407409,-6.064138,-8.767545,-2.186664,-8.612599,-4.135292,6.668761,-4.255134,7.253686,-6.614722,9.136033,4.167737,-6.902478,8.574405,9.981170,-1.468030,-4.730757,8.559955,8.276276,6.363250,4.128241,6.905375,-5.521068,6.978398,4.316838,-9.666430,-8.887638,-3.014919,-0.297951,-2.769773,-6.254866,-1.050578,6.773967,-8.680713,6.049288,2.882891,9.825750,8.698534,-4.269209,8.981086,-5.086875,-3.566683,-8.993304,8.670850,-6.820448,-2.126442,3.841985,-9.746293,1.007757,9.042389,-0.548724,1.636189,-0.129578,2.681675,0.958509,-1.978889,-9.093465,4.417815,6.889377,9.643939,-3.753904,-0.611318,-5.086148,-4.529088,2.017705,-3.260513,-6.118928,-5.943813,-7.017039,8.263990,-1.142369,5.326043,7.138445,5.397162,-5.888143,-2.693093,3.316487,-7.906650,8.828158,1.396571,-2.897050,-2.379345,9.254771,7.818505,8.252665,-1.941471,-5.526895,-5.565672,-2.145999,-8.334971,4.002784,5.154547,-8.089621,-3.502431,-8.757066,-2.958963,-1.009346,-6.970851,9.270100,9.907737,-2.773354,5.868139,-9.183641,-6.872137,9.078046,6.082024,-9.369107,0.752591,-7.592798,-2.934063,7.951480,0.332453,-2.634372,-4.487077,-9.756386,-8.998660,8.458929,8.166912,7.036894,-7.928410,3.443111,0.709969,-2.987494,-5.385575,9.074515,7.690324,3.555938,-1.731880,-0.934711,-6.120010,-6.436317,-5.892775,-6.380446,1.452575,6.904785,-1.602202,5.354226,-0.251654,1.654242,-7.861661,-3.002274,3.275257,6.724787,8.375179,-9.769776,-3.979632,-1.542459,-4.605816,-6.574445,-2.018723,2.794482,-8.221396,7.436470,-2.091686,4.373334,7.570675,4.048818,-5.160862,-2.135324,-2.922497,9.080708,8.821890,4.516743,-1.284560,-6.347869,-6.284887,3.422815,-7.060975,9.113968,3.665518,-2.380839,-4.353072,-4.952101,-9.438634,-3.179161,8.830932,7.113208,6.460769,4.021906,-2.655473,5.568401,2.589851,-4.295872,5.699351,1.884965,-5.995261,3.862005,2.450888,3.707335,-9.686319,-7.698539,1.866236,-6.991749,0.319292,-9.660299,9.777614,-2.158829,5.374577,9.312878,-6.890616,3.835934,-5.696267,-6.309623,-4.233469,2.307365,9.805917,2.797947,4.731316,-8.629421,3.267685,-9.461682,-2.133486,4.145972,9.183236,-6.336498,9.761968,2.135937,-1.899791,1.899686,6.969316,8.324580,1.150437,-8.633125,-6.173754,4.368220,1.965097,8.679495,-4.846280,0.427074,9.549614,3.017542,-0.521293,-4.715007,-6.174636,7.315727,-5.526077,8.380940,0.586408,-9.792657,-3.492062,8.286443,5.064816,3.254467,-9.229766,-7.108183,-6.185547,-0.661750,-2.027385,2.163724,6.656299,-2.206020,4.165667,9.000001,2.619332,-4.378282,1.308042,-4.082822,-4.656421,-3.754358,-8.839730,-9.596560,-8.022493,0.856018,6.227272,-9.590370,-5.125487,-3.708010,-9.612564,-1.895252,4.663005,2.905737,9.995058,-4.571870,2.943679,-3.137897,4.259287,-8.609102,2.923947,-3.241855,-4.610717,3.382353,8.207383,-5.235788,0.044072,-4.713386,8.620230,3.836948,0.483339,9.734176,-6.136436,-6.184174,-0.069419,-2.474434,4.062057,8.008626,4.491203,-1.094050,-9.025925,-6.261588,8.610859,3.680375,-8.504529,9.103944,-1.772806,-2.075889,-8.586273,-6.302590,9.774760,0.277819,9.658043,-8.265217,0.151058,6.107280,1.120657,-8.054765,-8.373179,6.151641,-3.561180,-2.988294,3.778379,-9.693507,-5.434771,1.236491,1.138183,-4.256962,5.154574,6.758625,0.107860,-1.588103,-5.230356,7.960080,-4.205473,8.476311,-7.109025,1.570641,-0.037446,5.054778,-2.126830,-3.334211,9.479535,-0.805806,7.073935,-8.702873,0.139371,5.592551,9.298078,-8.809250,7.138363,-9.450595,-7.585336,-9.106128,4.870012,6.920056,-6.022323,4.194469,-3.616852,-7.415508,3.049689,-7.730111,0.481024,-3.617333,-0.301555,3.383944,-5.996542,9.688253,4.133516,9.105482,-0.191304,9.658769,-3.336373,-1.608309,-6.716241,-5.163060,6.280570,-2.534207,-7.802776,4.786816,-2.061971,2.991596,4.727052,6.481305,-5.981740,3.224236,9.728368,3.733511,-2.072873,-1.395778,-3.021091,-7.961675,9.553265,-2.188252,-5.197976,-8.651116,-8.807184,1.924522,9.343423,8.253573,-4.717538,-2.186346,7.310111,6.385848,0.413906,-8.315165,3.122368,-9.470510,-5.383568,-9.741479,-6.315389,2.017499,-2.198077,-8.742532,1.600817,7.265368,2.654868,5.781818,0.662548,-5.032665,-7.425003,-8.982488,1.427495,-8.339245,-6.492529,-9.591332,2.145024,4.462682,8.318800,9.335256,6.012494,-8.662002,-7.024094,7.279167,-2.684969,3.941261,5.019862,-7.553167,-5.084972,-0.744510,-0.430495,8.746296,-6.567642,7.999695,4.060849,-0.106177,-2.406800,2.789737,-7.461356,-2.497809,-1.916769,2.404326,-8.050137,-4.654871,-9.579829,4.266813,-0.938336,-5.671652,2.655497,-5.615870,5.461413,-1.665343,3.814440,-2.581934,-2.288812,-6.514086,-4.475230,-3.844704,-5.620839,1.756541,1.038096,0.508804,-8.338081,-4.039692,4.966788,-0.214146,1.368537,-3.495152,-6.284776,-0.828847,-0.739567,6.111383,-5.926372,0.742325,-9.138661,1.144661,4.619421,8.740773,5.706776,4.820962,-6.859320,5.461167,-1.178103,-3.453382,-4.166165,-7.099101,-6.152922,-4.198472,1.612152,1.000275,-4.161150,-1.493854,8.123008,5.759201,2.602866,1.982606,-8.302144,-0.604874,2.823023,7.922750,4.100538,-8.270499,3.349632,1.649879,-9.620850,3.691192,3.708909,-9.847036,0.636573,4.891974,-9.477026,5.744249,7.962824,-7.553943,-0.665587,3.741378,0.106796,1.060454,-2.336065,7.172733,6.677002,4.828108,-2.857687,0.381908,-3.552453,6.628011,-0.419641,1.969207,-9.736115,-8.727773,-0.661604,-7.978422,2.502996,-8.763270,-1.018005,-3.151407,-3.566604,3.500880,7.187950,6.249441,8.966019,-6.938709,2.565424,-5.881004,5.245858,-3.480992,-7.188710,8.388444,2.938362,3.989333,-3.144112,8.196175,0.902816,2.095310,-4.364660,-7.672678,7.948393,1.073871,6.906704,-5.980776,-4.476836,-5.298238,-7.330965,-7.478922,6.464286,1.679257,6.708056,5.156404,4.023565,7.063089,9.451417,-3.299099,-4.499537,2.049747,0.685554,8.497617,-2.635560,-2.173678,7.189872,-0.038873,-7.430889,-3.089483,6.119904,-8.709624,6.665546,-2.720288,-6.633315,2.530858,-9.932479,-8.552896,9.391504,9.650862,5.488255,-1.316429,-5.910637,5.202135,-2.580014,-1.630511,2.390142,0.373836,-8.626557,6.019739,-5.954078,7.481348,5.584651,-2.189305,0.067845,3.921813,2.862825,-1.850980,-6.307060,-1.080593,7.789137,-0.597365,3.563921,3.311026,0.688545,-0.332674,-6.974886,-3.954721,5.590326,-5.880151,-5.870764,2.345376,8.993031,8.724162,-3.947318,-2.759769,-2.310561,-7.617332,-6.820839,9.971381,3.840799,9.841609,-2.951033,0.254559,-3.364731,-9.639313,0.219856,-9.330547,1.844514,2.876126,0.029018,-2.344435,-3.822908,-5.847647,-5.384527,3.431838,6.783910,2.577847,-2.315262,-2.080422,-7.533936,-6.852017,-7.204796,-5.792964,-3.177715,9.455342,-5.833603,-1.875214,6.575226,9.525001,-3.349163,4.932265,-2.777948,3.518346,9.905298,1.350693,8.579920,-6.622626,3.603085,4.733559,-9.503174,2.753634,-2.020747,9.440354,-0.151799,-1.742620,3.401611,7.316481,-7.000990,3.511569,-6.894558,-5.586648,-9.221406,1.890076,6.738599,2.916193,-9.221179,-3.324751,-0.029385,-8.559211,5.125660,-0.557350,-9.359307,-0.468087,-5.506358,-5.295694,-3.945048,-7.572176,1.883555,-9.359010,9.586371,-9.420587,3.911091,-9.332799,6.312996,-9.769124,6.793017,3.593274,-7.853100,3.414421,2.010696,4.248389], dtype = "float32")#candidate|11481|(880,)|const|float32
call_11480 = relay.TupleGetItem(func_1513_call(relay.reshape(const_11481.astype('float32'), [4, 220])), 1)
call_11482 = relay.TupleGetItem(func_1516_call(relay.reshape(const_11481.astype('float32'), [4, 220])), 1)
bop_11483 = relay.logical_xor(bop_11472.astype('uint16'), relay.reshape(bop_11469.astype('uint16'), relay.shape_of(bop_11472))) # shape=(468, 15)
func_7063_call = mod.get_global_var('func_7063')
func_7065_call = mutated_mod.get_global_var('func_7065')
call_11494 = relay.TupleGetItem(func_7063_call(), 0)
call_11495 = relay.TupleGetItem(func_7065_call(), 0)
uop_11501 = relay.rsqrt(bop_11469.astype('float32')) # shape=(468, 15)
output = relay.Tuple([call_11436,call_11450,const_11453,bop_11457,call_11462,bop_11465,call_11480,const_11481,bop_11483,call_11494,uop_11501,])
output2 = relay.Tuple([call_11437,call_11454,const_11453,bop_11457,call_11463,bop_11465,call_11482,const_11481,bop_11483,call_11495,uop_11501,])
func_11505 = relay.Function([var_11452,var_11464,var_11468,], output)
mod['func_11505'] = func_11505
mod = relay.transform.InferType()(mod)
var_11506 = relay.var("var_11506", dtype = "float32", shape = (84,))#candidate|11506|(84,)|var|float32
var_11507 = relay.var("var_11507", dtype = "int64", shape = (468, 1))#candidate|11507|(468, 1)|var|int64
var_11508 = relay.var("var_11508", dtype = "int64", shape = (468, 15))#candidate|11508|(468, 15)|var|int64
output = func_11505(var_11506,var_11507,var_11508,)
func_11509 = relay.Function([var_11506,var_11507,var_11508,], output)
mutated_mod['func_11509'] = func_11509
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11513 = relay.var("var_11513", dtype = "uint64", shape = (1, 16, 9))#candidate|11513|(1, 16, 9)|var|uint64
const_11514 = relay.const([[[-7,-7,10,5,-9,-5,-6,1,-4],[3,-3,-3,3,-5,-2,10,-3,-2],[-7,5,6,8,8,-5,4,-4,-8],[5,4,4,8,-7,-10,-6,-10,5],[-10,7,-2,-10,10,-5,-10,8,10],[-2,-5,-1,-10,4,-7,-5,1,7],[-4,-2,-1,-3,-7,7,-4,-8,-9],[-5,-6,-2,-9,-2,-1,-6,5,1],[4,7,6,1,-4,-8,7,-6,4],[8,5,4,2,-10,9,-5,5,6],[-7,-1,7,-5,-5,-1,-1,2,2],[1,-7,1,2,9,-7,1,4,-4],[-3,9,-4,-7,-9,10,-9,5,1],[2,-1,3,7,-1,-7,-6,-8,8],[-7,-6,6,-10,-4,-2,1,10,-6],[10,-8,8,10,6,1,1,-9,-4]],[[10,1,-7,10,-7,-1,-3,8,-4],[9,-2,-3,8,-1,-10,3,9,5],[-9,5,5,-10,-7,-2,-7,-6,-5],[-4,-2,4,-1,3,3,7,2,7],[-10,-8,9,9,-2,-7,-5,-1,-7],[8,-2,-8,-10,6,-9,-1,-3,-5],[10,8,-8,-8,7,9,-6,4,9],[-2,8,-10,2,3,2,-8,1,-4],[-3,1,4,6,8,-8,3,-7,10],[6,-1,-9,-9,5,5,1,2,7],[-4,5,-4,-1,3,-8,5,6,4],[-1,4,-5,5,-6,9,-4,10,-7],[2,-3,-7,-1,4,-10,-5,-1,7],[8,1,-3,-9,5,6,-6,-1,-7],[-8,3,-6,-2,6,-1,-9,-8,-7],[1,8,7,-10,-6,10,1,2,1]],[[1,-2,-7,1,-4,-6,-2,6,7],[-5,4,7,-5,-3,-4,-8,10,-3],[2,2,-5,-6,-7,6,-4,10,2],[-4,-8,5,-3,-9,2,-9,8,-10],[-2,-1,-7,-5,-7,10,4,8,3],[6,-8,-1,8,5,-3,-10,-9,6],[-7,-8,-5,8,4,-1,-1,5,1],[10,-7,-7,9,-7,-8,6,-3,-4],[5,-10,-7,-10,-8,-8,2,-10,4],[-1,-5,-3,3,-2,6,-9,-7,-1],[-9,-3,-7,-8,8,10,-7,4,3],[-7,-5,-5,7,3,2,-8,-7,8],[1,-5,-5,-10,-7,-4,-10,-7,2],[-7,5,-2,-3,7,-3,-4,-4,1],[3,10,6,2,-7,-2,-2,-9,-8],[-5,-3,-3,-9,9,7,3,-3,-1]],[[8,-4,4,-5,4,5,-3,5,3],[2,-8,-5,3,6,-2,-3,-2,-5],[-3,-7,2,-1,2,-3,-5,-9,6],[-9,-4,4,-1,6,6,-4,-2,7],[2,-1,3,1,10,2,-8,6,-3],[-7,7,-2,5,-1,-8,2,-6,6],[8,-7,9,-4,-10,8,1,10,1],[9,9,-4,10,-6,-9,-6,-2,-5],[2,-10,2,-6,5,8,-9,3,-1],[-4,3,5,-4,8,4,9,-5,-10],[8,9,-3,1,-8,-9,-1,7,-3],[-3,3,-3,7,5,-4,10,-1,7],[-9,-8,-5,5,-10,-8,-7,9,4],[-9,5,-4,6,-3,6,3,-10,-2],[7,-9,-4,-9,-9,2,-2,6,-4],[-8,-8,-9,1,-8,4,4,-1,-8]],[[1,5,8,5,8,-7,6,3,4],[-6,6,6,8,-3,6,-2,-1,-8],[4,-8,9,-3,1,-6,-9,-2,10],[5,9,-5,-9,1,-3,8,-4,-8],[-2,-7,8,-9,-8,2,-8,-4,-6],[9,5,5,9,-3,-2,6,-3,-6],[-6,8,6,2,6,1,6,-7,-2],[-10,8,5,-6,3,-2,2,5,-4],[9,-7,5,-9,9,-3,-10,3,-8],[-7,7,-6,10,9,-8,-6,-10,-4],[-10,5,8,-2,2,-8,4,-5,-7],[2,-8,1,-7,-3,-10,1,9,-3],[5,-7,3,-7,3,9,-2,-5,5],[4,-5,-8,-3,6,6,-1,5,10],[-3,6,-9,-6,-6,-9,9,3,-2],[8,2,9,1,1,-8,-5,-7,7]],[[-6,5,5,4,-1,7,-8,1,9],[7,2,8,-8,2,-4,1,3,-3],[-2,-2,2,8,-4,-9,1,-3,-2],[4,5,-5,-7,10,-2,10,-10,9],[-4,3,6,-1,5,-1,-6,-9,2],[-10,10,-1,-5,-8,-7,-6,-4,9],[10,-8,-5,-6,-5,-1,-8,-6,-5],[3,-1,-2,8,7,8,5,-7,6],[3,4,6,-4,8,-5,10,2,8],[8,-5,-1,5,2,-8,-6,10,-10],[-5,3,6,-8,-5,-8,6,1,4],[-4,-6,1,-3,-9,-6,9,5,7],[-9,10,5,7,7,-3,-7,-10,-1],[1,7,-1,10,4,-2,-1,-6,-5],[10,-6,-9,7,-6,-1,7,5,3],[-7,-5,-10,-4,10,-1,-2,-6,-7]],[[-7,-10,-1,-2,-2,-10,-10,-10,10],[4,9,3,-8,1,5,-8,4,7],[-9,-2,5,-10,1,-2,7,4,-9],[-8,-3,-10,8,-1,5,8,7,7],[-3,9,-6,-6,8,-9,-6,3,-7],[-8,-8,-7,-8,-9,4,9,2,3],[10,10,-9,6,-7,7,-9,-9,3],[-9,3,-8,-3,-8,6,4,-1,5],[-7,-9,7,8,-10,-2,-7,6,1],[10,-10,1,-8,-1,1,-2,8,-3],[-5,10,10,-10,4,-8,7,-9,6],[10,-4,4,-10,4,-8,-2,9,-10],[-5,7,-4,6,-3,-8,-4,-3,-3],[8,5,-9,10,-4,3,-8,-4,-10],[10,-10,3,-1,10,9,-3,5,8],[9,-7,-7,-8,-1,-7,-1,-8,-9]],[[-2,-10,-6,-4,-6,7,4,2,-2],[2,-3,4,-3,-9,9,4,10,-2],[2,7,6,4,1,-1,-6,-7,-5],[10,-8,-3,-9,-8,10,5,-7,-2],[6,5,1,-4,-1,5,-2,8,-6],[-8,-5,-3,-8,8,1,-10,-5,8],[-5,2,-1,-3,-4,4,-9,4,-9],[-2,-7,4,-2,9,-1,3,9,-1],[-2,5,5,-5,-2,-2,-10,-9,5],[-7,6,-4,4,3,3,-4,-10,3],[10,2,1,-4,8,-7,5,-2,1],[9,5,7,-8,5,1,3,-5,3],[9,-6,9,10,7,-4,-9,-4,-7],[-2,-3,4,4,3,-4,-7,2,-2],[7,4,5,2,2,-6,-8,-5,5],[3,9,-9,2,8,9,4,1,10]]], dtype = "uint64")#candidate|11514|(8, 16, 9)|const|uint64
bop_11515 = relay.bitwise_or(var_11513.astype('uint64'), const_11514.astype('uint64')) # shape=(8, 16, 9)
output = bop_11515
output2 = bop_11515
F = relay.Function([var_11513,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11513,], output2)
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
	relay.transform.SimplifyExpr(),
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
