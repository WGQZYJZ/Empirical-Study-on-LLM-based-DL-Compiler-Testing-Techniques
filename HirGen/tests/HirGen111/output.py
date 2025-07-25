import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_271 = relay.var("var_271", dtype = "float64", shape = (10, 1, 2))#candidate|271|(10, 1, 2)|var|float64
uop_272 = relay.atan(var_271.astype('float64')) # shape=(10, 1, 2)
output = relay.Tuple([uop_272,])
output2 = relay.Tuple([uop_272,])
func_276 = relay.Function([var_271,], output)
mod['func_276'] = func_276
mod = relay.transform.InferType()(mod)
mutated_mod['func_276'] = func_276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_277 = relay.var("var_277", dtype = "float64", shape = (10, 1, 2))#candidate|277|(10, 1, 2)|var|float64
func_276_call = mutated_mod.get_global_var('func_276')
call_278 = func_276_call(var_277)
output = call_278
func_279 = relay.Function([var_277], output)
mutated_mod['func_279'] = func_279
mutated_mod = relay.transform.InferType()(mutated_mod)
const_466 = relay.const([[[4,-5,3,4,9,3,5]],[[10,4,-6,-9,-7,9,7]],[[-1,-3,-6,1,-10,-7,10]],[[-4,6,3,-9,-6,8,-3]],[[-9,-6,-9,-5,-9,-6,3]],[[1,-3,-8,-7,8,-10,6]],[[10,-4,2,-1,-10,9,5]]], dtype = "int8")#candidate|466|(7, 1, 7)|const|int8
var_467 = relay.var("var_467", dtype = "int8", shape = (7, 8, 7))#candidate|467|(7, 8, 7)|var|int8
bop_468 = relay.logical_xor(const_466.astype('int8'), var_467.astype('int8')) # shape=(7, 8, 7)
output = bop_468
output2 = bop_468
func_474 = relay.Function([var_467,], output)
mod['func_474'] = func_474
mod = relay.transform.InferType()(mod)
var_475 = relay.var("var_475", dtype = "int8", shape = (7, 8, 7))#candidate|475|(7, 8, 7)|var|int8
output = func_474(var_475)
func_476 = relay.Function([var_475], output)
mutated_mod['func_476'] = func_476
mutated_mod = relay.transform.InferType()(mutated_mod)
var_555 = relay.var("var_555", dtype = "int8", shape = (16, 15, 12))#candidate|555|(16, 15, 12)|var|int8
var_556 = relay.var("var_556", dtype = "int8", shape = (16, 15, 12))#candidate|556|(16, 15, 12)|var|int8
bop_557 = relay.right_shift(var_555.astype('int8'), relay.reshape(var_556.astype('int8'), relay.shape_of(var_555))) # shape=(16, 15, 12)
uop_570 = relay.erf(bop_557.astype('float64')) # shape=(16, 15, 12)
uop_578 = relay.sigmoid(var_556.astype('float32')) # shape=(16, 15, 12)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
var_583 = relay.var("var_583", dtype = "float64", shape = (20,))#candidate|583|(20,)|var|float64
call_582 = relay.TupleGetItem(func_276_call(relay.reshape(var_583.astype('float64'), [10, 1, 2])), 0)
call_584 = relay.TupleGetItem(func_279_call(relay.reshape(var_583.astype('float64'), [10, 1, 2])), 0)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_587 = relay.TupleGetItem(func_276_call(relay.reshape(call_582.astype('float64'), [10, 1, 2])), 0)
call_588 = relay.TupleGetItem(func_279_call(relay.reshape(call_582.astype('float64'), [10, 1, 2])), 0)
output = relay.Tuple([uop_570,uop_578,call_582,var_583,call_587,])
output2 = relay.Tuple([uop_570,uop_578,call_584,var_583,call_588,])
func_599 = relay.Function([var_555,var_556,var_583,], output)
mod['func_599'] = func_599
mod = relay.transform.InferType()(mod)
var_600 = relay.var("var_600", dtype = "int8", shape = (16, 15, 12))#candidate|600|(16, 15, 12)|var|int8
var_601 = relay.var("var_601", dtype = "int8", shape = (16, 15, 12))#candidate|601|(16, 15, 12)|var|int8
var_602 = relay.var("var_602", dtype = "float64", shape = (20,))#candidate|602|(20,)|var|float64
output = func_599(var_600,var_601,var_602,)
func_603 = relay.Function([var_600,var_601,var_602,], output)
mutated_mod['func_603'] = func_603
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1037 = relay.var("var_1037", dtype = "float32", shape = (10, 2))#candidate|1037|(10, 2)|var|float32
uop_1038 = relay.atanh(var_1037.astype('float32')) # shape=(10, 2)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_1049 = relay.TupleGetItem(func_276_call(relay.reshape(var_1037.astype('float64'), [10, 1, 2])), 0)
call_1050 = relay.TupleGetItem(func_279_call(relay.reshape(var_1037.astype('float64'), [10, 1, 2])), 0)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_1051 = relay.TupleGetItem(func_276_call(relay.reshape(call_1049.astype('float64'), [10, 1, 2])), 0)
call_1052 = relay.TupleGetItem(func_279_call(relay.reshape(call_1049.astype('float64'), [10, 1, 2])), 0)
output = relay.Tuple([uop_1038,call_1049,call_1051,])
output2 = relay.Tuple([uop_1038,call_1050,call_1052,])
func_1078 = relay.Function([var_1037,], output)
mod['func_1078'] = func_1078
mod = relay.transform.InferType()(mod)
var_1079 = relay.var("var_1079", dtype = "float32", shape = (10, 2))#candidate|1079|(10, 2)|var|float32
output = func_1078(var_1079)
func_1080 = relay.Function([var_1079], output)
mutated_mod['func_1080'] = func_1080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1238 = relay.var("var_1238", dtype = "float32", shape = (2, 1, 6))#candidate|1238|(2, 1, 6)|var|float32
uop_1239 = relay.rsqrt(var_1238.astype('float32')) # shape=(2, 1, 6)
uop_1241 = relay.atanh(uop_1239.astype('float64')) # shape=(2, 1, 6)
output = relay.Tuple([uop_1241,])
output2 = relay.Tuple([uop_1241,])
func_1276 = relay.Function([var_1238,], output)
mod['func_1276'] = func_1276
mod = relay.transform.InferType()(mod)
var_1277 = relay.var("var_1277", dtype = "float32", shape = (2, 1, 6))#candidate|1277|(2, 1, 6)|var|float32
output = func_1276(var_1277)
func_1278 = relay.Function([var_1277], output)
mutated_mod['func_1278'] = func_1278
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1299 = relay.const([[[2.681360,6.606138],[-4.060848,-2.619532],[3.122966,8.525378],[7.729655,8.138999],[7.597153,1.203483],[-4.309065,-9.804979],[4.080054,2.117722],[-8.815357,0.528665],[-9.072077,5.588892],[-6.428098,8.006104],[-7.250840,-1.926648],[-0.119830,-4.513542],[-5.963937,-1.178094]],[[7.738911,9.584381],[7.466919,-0.406945],[7.164886,3.738916],[-7.420345,-6.111407],[-2.889599,-3.509322],[-2.514831,-3.559980],[2.983024,-6.066996],[7.129155,-9.605208],[-0.690218,1.359833],[-8.033132,9.938137],[9.087532,-0.882274],[9.244349,-2.539194],[-4.147207,4.808772]]], dtype = "float64")#candidate|1299|(2, 13, 2)|const|float64
uop_1300 = relay.sinh(const_1299.astype('float64')) # shape=(2, 13, 2)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
const_1303 = relay.const([[2.207683,4.587277,-0.396143,-1.057275],[-2.231177,3.179199,6.310725,-2.481345],[4.940277,8.800643,-0.087405,-6.295612],[0.485089,3.077089,1.915667,9.538539],[-3.507883,-3.109157,5.173418,7.167924]], dtype = "float64")#candidate|1303|(5, 4)|const|float64
call_1302 = relay.TupleGetItem(func_276_call(relay.reshape(const_1303.astype('float64'), [10, 1, 2])), 0)
call_1304 = relay.TupleGetItem(func_279_call(relay.reshape(const_1303.astype('float64'), [10, 1, 2])), 0)
output = relay.Tuple([uop_1300,call_1302,const_1303,])
output2 = relay.Tuple([uop_1300,call_1304,const_1303,])
func_1321 = relay.Function([], output)
mod['func_1321'] = func_1321
mod = relay.transform.InferType()(mod)
output = func_1321()
func_1322 = relay.Function([], output)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1338 = relay.var("var_1338", dtype = "float64", shape = (3, 15, 16))#candidate|1338|(3, 15, 16)|var|float64
uop_1339 = relay.asinh(var_1338.astype('float64')) # shape=(3, 15, 16)
func_474_call = mod.get_global_var('func_474')
func_476_call = mutated_mod.get_global_var('func_476')
const_1346 = relay.const([[9,-7,-4,-10],[-6,10,6,8],[-9,-7,-4,-7],[6,2,-5,-2],[6,-1,-4,7],[-10,6,2,-5],[-4,1,9,-4],[-4,-5,-1,-5],[10,7,7,-4],[3,-10,-5,-8],[-1,-7,-9,-5],[7,3,-1,-3],[6,-5,-4,-9],[-10,-3,-6,-3],[4,-7,-1,7],[6,-4,-10,-10],[-8,9,-3,-10],[7,-7,8,10],[-8,-4,-1,6],[5,-6,10,-1],[-10,-10,-7,7],[6,7,-4,6],[3,-2,5,4],[2,2,8,10],[-4,-5,3,-4],[-6,2,7,-3],[-10,-7,-2,4],[2,6,9,-8],[-6,-3,4,7],[8,3,1,-8],[-10,-5,-7,-8],[5,9,-10,7],[1,-7,9,7],[7,-5,-6,9],[-9,8,-3,6],[-10,4,-3,10],[-2,1,2,9],[9,-8,-8,-1],[-3,-2,7,6],[5,9,-10,-4],[-7,2,-2,-1],[-4,6,-7,-8],[5,-7,-9,10],[-3,-4,10,-5],[-10,6,-9,-4],[5,-4,6,3],[5,-4,4,-10],[4,10,-9,-1],[-2,-2,-4,-4],[6,-3,2,-4],[7,3,1,-8],[5,-1,1,-5],[8,3,-6,3],[5,-4,2,-5],[-5,10,-2,-5],[6,-3,-7,-1],[-10,9,9,9],[9,-4,3,-2],[8,6,-10,-6],[6,-3,-8,10],[-9,3,2,-4],[5,-2,7,-9],[-5,4,-8,4],[-10,9,-3,5],[9,-10,9,-1],[-1,-5,8,3],[10,1,-6,10],[-1,-3,7,6],[7,6,-9,-2],[-4,9,2,-5],[7,-10,10,8],[-10,-6,10,-2],[8,-3,-9,-9],[4,2,8,-10],[-3,10,2,-5],[-3,-9,4,10],[-1,1,7,-2],[-8,1,-4,-2],[3,2,-2,-6],[-9,7,-6,7],[7,-9,8,9],[6,1,-1,8],[-7,-9,-7,-5],[10,2,-7,5],[-7,-2,6,10],[-1,1,-3,8],[-9,-10,-2,7],[-5,9,-7,9],[9,-8,1,6],[-6,6,5,-3],[8,3,8,-3],[-10,-8,7,1],[-7,10,7,-1],[-10,-4,8,-1],[3,-8,5,-4],[4,-2,-9,4],[1,5,-9,-1],[-3,5,-4,-10]], dtype = "int8")#candidate|1346|(98, 4)|const|int8
call_1345 = func_474_call(relay.reshape(const_1346.astype('int8'), [7, 8, 7]))
call_1347 = func_474_call(relay.reshape(const_1346.astype('int8'), [7, 8, 7]))
func_599_call = mod.get_global_var('func_599')
func_603_call = mutated_mod.get_global_var('func_603')
const_1356 = relay.const([6,9,-8,3,-2,-6,-2,2,-2,-4,1,-5,10,-3,2,6,-9,-7,-7,-1,-7,-8,10,9,-6,-4,-2,3,5,-1,-10,-5,4,-8,-2,-2,7,-8,-1,-10,9,-3,-3,3,2,4,-10,3,-3,-7,-1,6,8,-7,-10,-5,9,9,6,-1,-5,2,-8,-1,7,7,-6,6,-4,2,-9,4,9,-1,5,-5,1,-8,-4,9,7,-1,-7,-7,-1,-9,-8,-8,6,3,-5,4,8,4,-2,-5,-1,4,-5,-10,-1,-7,-4,7,-4,3,-7,-5,10,-6,4,-3,-10,-2,-9,-1,3,-9,-1,-7,7,6,7,-10,1,-9,-9,-10,1,-4,-6,1,3,6,-8,-10,-1,10,8,-4,6,-5,-6,-6,9,-7,4,-2,-10,10,-1,5,-9,-9,3,-9,7,-5,-1,9,-10,-4,-6,3,5,8,-6,-8,-5,3,2,-10,5,1,-8,-7,1,-5,8,-7,-1,-10,5,1,7,-2,5,-8,-9,8,3,8,-5,-1,2,7,-2,-2,3,10,7,-8,6,-5,-7,10,8,-2,-2,-5,4,10,9,4,5,-3,-8,7,7,6,-4,-3,-6,-5,-9,-5,-4,-8,4,4,-8,4,-8,-7,-2,10,-1,10,10,-8,-8,4,5,-5,-6,10,8,7,4,4,8,4,8,7,-9,-7,-5,1,2,8,-8,1,2,-3,-3,2,10,-1,2,-4,-10,-10,-3,4,8,5,-2,-2,-6,9,-10,1,9,-6,-9,-3,-3,-3,-3,-2,-10,-7,-3,5,3,-9,6,-3,-1,7,-9,-10,-3,-9,-1,-9,7,-3,6,10,-5,2,-8,-8,2,-10,6,-5,2,-7,-6,5,-2,-6,8,8,4,7,-3,-2,2,9,-1,-9,10,-7,2,-4,10,-5,-7,-2,-2,-6,3,3,-1,5,7,-4,-10,7,-10,-8,-2,-1,-5,3,-3,6,6,-1,-2,-8,10,9,-4,-10,9,7,1,2,10,-7,6,-8,3,-1,8,5,3,6,2,2,-5,3,-4,4,-2,-6,4,-3,5,-3,3,-1,-4,2,4,-5,2,9,-5,-1,-5,7,2,8,4,-10,-1,-3,-7,-9,8,4,-2,-5,5,5,-4,-1,2,4,1,3,7,5,1,-9,-9,-9,5,9,-10,1,-9,-2,2,-9,2,-4,-9,2,-4,9,3,6,1,-9,-2,-7,-3,-1,5,-7,-3,-3,-2,2,-6,-1,8,7,3,-10,-6,-5,4,-3,8,-5,1,-5,2,8,8,-9,7,4,3,4,-1,-8,6,5,1,7,5,-6,-7,7,6,-2,3,2,1,5,6,8,-5,8,-10,-10,6,6,-10,1,-10,-8,10,-6,7,-3,-5,7,-2,7,-9,-9,-5,-10,-7,-1,-5,-9,-1,6,-6,-1,7,-2,4,-3,8,-9,8,-10,-10,3,1,10,6,-8,-4,5,8,4,-9,-4,-10,2,4,-4,-2,-2,10,-5,-10,1,3,-9,5,4,10,-3,-2,-8,-6,1,-1,10,-4,10,-7,10,-8,2,2,-7,5,1,-6,4,-3,-9,7,-8,6,7,-8,5,7,9,-5,-10,-8,-8,1,-4,8,-1,-5,-7,6,4,2,9,-7,9,-7,-2,3,7,3,-10,-5,5,-1,-10,-6,-4,4,-10,-4,-4,-9,3,-6,7,4,-10,10,10,6,10,-4,2,10,10,-10,-4,-1,-4,9,-8,-9,-1,-2,10,-1,-1,7,-5,-5,10,1,8,-10,9,-2,-2,5,-9,4,-6,2,-2,-3,5,-3,-5,10,6,-6,1,2,-10,-5,-4,8,4,9,8,-4,-2,-9,-3,2,1,4,7,-5,3,-6,1,-8,2,2,1,-3,2,2,3,5,-4,-5,-5,10,2,-4,7,-7,-9,-9,4,-5,-5,4,-5,-1,-7,3,-7,-9,-6,2,-5,4,-8,6,6,10,2,-9,-4,7,-7,3,-3,2,5,5,-3,-6,4,4,-5,9,-10,-4,9,6,-4,-9,-3,-8,-7,10,4,2,6,-7,-4,-8,-5,9,-8,9,5,-8,-2,-9,-1,-10,5,-2,10,3,6,-8,-8,6,-5,-7,-6,1,1,-7,-10,-7,1,-7,-9,-6,-4,7,-3,-7,9,-9,10,2,-1,-4,-8,-8,-10,-1,-5,-5,3,-2,-6,-7,4,-1,9,6,4,10,10,-10,-3,9,-10,-7,-8,-3,10,9,-7,6,6,5,1,10,3,2,-5,-4,-7,7,-3,-10,-10,7,-1,-3,-5,7,-4,-7,-8,-5,-2,-7,-3,4,7,-9,5,6,8,-5,8,1,10,10,-1,-3,7,3,6,-6,-3,2,10,8,-7,-3,6,8,-5,3,7,-8,8,4,1,7,-4,4,8,2,-4,2,-2,-5,1,3,-6,2,-4,-5,4,-1,-4,-4,6,8,2,1,4,-1,3,-5,-6,-10,1,7,1,8,2,8,8,9,7,6,-5,-6,-2,7,8,-10,7,6,7,3,-4,9,-6,5,-10,7,-7,-4,-4,7,-2,-10,-8,9,10,7,5,-7,-6,-6,-3,-2,6,9,10,-9,-5,-3,5,10,-8,-9,-5,-3,1,9,-4,4,10,-7,1,3,7,9,-2,9,-6,-2,-7,1,-6,-1,3,10,1,4,-5,6,-4,8,-3,-7,-5,9,-4,1,-5,2,-10,-1,-10,-10,3,1,-2,5,-5,-6,1,-2,10,-7,-6,10,1,-6,8,6,-4,9,5,5,6,10,-9,-2,-8,3,-8,-1,-6,-10,2,6,-4,-6,-8,-8,-4,-2,1,-1,3,-4,-9,-1,-1,-9,-8,1,-9,2,-7,2,7,4,7,6,1,2,4,-5,4,-7,9,6,-2,7,-7,1,-4,3,-2,3,10,1,7,-6,-2,-5,1,-10,8,-4,-10,-10,-10,8,-3,-5,-6,-4,4,6,-2,-6,-2,8,8,6,7,-4,10,-10,3,-3,-4,2,6,-4,6,-5,-10,8,-3,6,2,-10,2,-5,-5,-1,-5,5,-10,-4,-10,-7,-10,-8,3,4,2,8,-3,-8,-1,-7,4,8,2,-4,-8,3,-8,-2,3,-8,1,-10,9,3,8,6,2,8,5,6,-5,-3,8,-5,1,-7,-9,9,6,10,1,-6,10,-7,-7,10,10,6,9,10,-5,4,-7,-4,4,6,9,-8,-7,-8,8,6,-1,7,-4,-2,7,4,1,-6,3,-10,-4,-5,-3,-7,9,8,-8,2,3,2,1,3,-8,-5,-1,-5,-1,-7,-3,5,8,4,10,9,-9,5,-8,10,-7,7,9,-4,2,7,6,7,-7,1,8,-1,2,7,-4,8,-3,9,8,-6,-5,-8,-7,6,-8,1,8,3,8,3,-8,-5,-7,4,-10,-8,7,5,-10,10,-9,-6,-5,-8,-10,6,4,-8,8,6,6,10,-9,7,-7,1,-10,-4,5,-9,-4,2,6,9,-4,1,-9,3,-7,9,-9,-1,-7,-3,8,-7,7,-2,-9,-9,4,-3,1,2,8,4,-2,-6,2,1,-1,6,-8,-3,7,-10,-1,5,10,-2,9,-6,2,1,-5,-8,3,-6,-2,7,-2,2,1,7,-5,8,8,-8,-9,-6,3,1,-8,8,8,9,4,3,-9,5,-1,1,-10,-10,9,-1,2,10,-1,-1,-6,8,4,-5,4,-8,-4,4,9,3,4,10,-8,-7,1,-7,-10,6,6,6,3,5,-4,-3,7,-1,-10,6,-1,8,-10,-8,-9,2,-8,-7,4,-10,3,3,9,-2,5,8,10,8,10,10,-2,9,5,-5,-8,-9,-8,2,6,-8,-3,-7,-2,-2,-2,-4,-9,8,-8,2,10,8,6,7,5,3,10,10,-8,4,7,6,-2,-9,-7,-6,-2,5,8,10,-7,-3,6,9,-8,-1,1,-10,-4,-3,9,8,-6,7,-6,9,-1,-8,-6,8,10,-8,9,-3,-8,-3,-8,8,5,9,-2,3,-3,-10,-8,2,8,-10,-9,-9,1,-3,5,4,7,-9,4,-4,-3,-3,-1,-2,4,-7,4,1,1,6,-5,4,-4,3,-7,4,-1,4,1,-2,-5,-9,8,8,-5,-3,-5,-4,-2,-8,6,-10,8,-1,-7,7,4,4,-7,1,-7,2,-3,-2,5,-5,-3,-10,-8,-1,1,-8,-5,9,7,3,4,7,-6,-2,10,-4,10,-3,2,-3,5,10,-6,-3,6,-8,-5,-8,3,-2,5,5,7,-6,-5,1,-2,9,9,2,9,-8,4,-3,-3,-1,8,-6,5,3,-2,-9,5,-4,-1,-2,6,-5,5,9,-5,-10,6,10,-9,3,-9,-4,4,1,-6,-6,-4,-5,2,-8,-4,-2,6,6,-4,5,-3,8,-8,-3,-3,-7,1,-7,-7,2,5,4,5,-7,8,2,2,9,10,-6,-10,-1,4,5,-5,5,-10,-3,8,4,3,-7,6,7,-7,-1,6,1,-2,-3,5,8,6,10,3,-2,-8,3,7,3,5,-3,8,2,10,8,5,1,-9,-7,-3,-1,8,-8,-4,-8,-5,-9,-7,-4,8,4,-1,-7,6,-3,1,-3,-7,-3,-9,1,4,-10,3,-9,7,-6,-10,9,5,6,-7,4,-9,-5,7,-4,-6,-1,-8,1,4,6,-10,-10,6,-10,5,6,-10,2,-7,-8,1,-3,10,6,3,7,-4,8,-3,4,-4,-1,1,4,10,-4,-1,-1,3,4,9,9,10,-5,8,2,2,-8,9,-3,-4,-1,6,-6,9,-4,3,2,-3,-8,-8,6,-6,-3,6,3,4,3,-5,-8,-10,3,-8,-9,-1,3,-9,-9,3,9,9,7,7,-3,8,-7,2,2,-4,-2,-7,-4,3,-3,-7,-6,-6,10,-5,-8,-2,3,-4,5,-5,-10,-1,-3,10,-3,-8,-1,-3,10,4,3,2,10,-1,1,-2,-2,-7,-9,1,-4,-2,5,-8,5,2,7,-6,-9,4,6,-3,10,3,9,-1,3,9,-9,5,-10,4,3,8,8,4,-9,2,10,-7,1,3,-1,4,-1,6,7,1,-1,-4,3,2,-8,9,2,-7,6,-7,-2,9,-9,5,6,-10,6,-7,-3,-9,3,-8,-8,6,-3,-2,-3,6,-5,-9,-8,-9,4,-3,5,7,2,3,-8,-5,-3,6,8,-9,5,-6,-9,-9,-1,10,-2,5,4,-5,8,-5,-7,-8,-3,9,-7,2,10,-10,2,10,-9,-2,-3,-5,-7,2,1,10,-9,3,4,3,-7,-6,5,4,10,-6,3,4,4,-5,-7,1,3,-3,9,10,1,6,-3,9,-6,-4,10,10,-5,-1,1,-10,5,-9,1,2,-7,-7,9,-2,5,-4,8,-9,9,7,3,2,1,4,-3,4,-7,10,9,8,2,8,-6,-2,8,-4,-5,1,-2,-9,-3,4,-8,-5,8,2,7,-7,9,-9,7,8,-4,1,5,-10,7,-10,10,-1,-1,8,2,-3,5,8,7,-7,6,-6,9,1,10,8,-7,8,-3,5,2,-6,10,-8,-1,-8,2,-8,-8,5,-10,-9,6,-4,4,4,-5,-2,6,2,6,4,3,-8,-3,-10,10,2,7,-2,-5,-8,9,-5,-1,-4,-6,4,2,-10,-7,-10,10,-10,7,-9,-2,-3,8,-8,7,-3,-10,-2,-10,-9,-3,-1,-2,3,7,-2,-10,8,2,-4,-7,2,5,-4,-8,-2,-4,5,6,-5,-9,-9,-1,4,4,2,6,-1,-10,8,7,-9,2,7,2,-8,9,10,6,-3,4,4,-1,-5,-9,9,2,7,1,-2,5,6,9,4,-1,-6,4,7,4,-6,-4,10,-2,1,-2,8,5,1,-7,-9,-4,3,6,3,3,-4,-6,-4,9,2,8,-9,2,-7,7,-9,-3,-8,4,1,-3,-6,-7,-7,-6,10,-9,-9,10,-3,-3,7,7,-7,7,8,-2,8,5,-8,4,-6,-6,7,-2,3,3,3,7,2,-9,3,7,1,-7,-4,6,4,-9,-7,1,6,2,-5,1,-5,2,-2,-9,2,3,-7,-7,2,-1,-5,-1,-6,2,3,1,-2,6,-1,-6,-1,8,-9,-8,-1,9,1,8,-4,1,4,5,-6,-1,-8,-9,-7,6,1,4,-2,7,5,-1,8,6,5,-9,6,5,10,-2,10,-2,3,3,10,-1,7,-4,5,8,-3,10,-8,3,10,4,5,-2,-1,6,-7,6,2,-9,-10,-8,4,4,2,2,1,3,-10,-4,10,-4,-8,10,-2,6,6,7,-1,-3,-6,-4,-1,-5,-2,5,1,-8,2,9,-7,-6,-1,4,-3,5,-4,-6,-6,5,10,-9,-1,-9,4,-7,-5,3,-7,7,6,7,1,-6,-6,6,-2,6,3,-4,-7,8,-5,9,-10,2,-8,-7,-4,-9,-5,-8,-9,8,-2,-9,-7,-3,7,-6,8,-4,-9,-7,-5,3,1,-7,-6,4,-1,-8,-7,-1,-3,-3,5,7,-10,6,3,5,3,-6,-9,10,1,-8,-9,5,6,-10,5,6,6,-1,3,4,-10,-6,1,10,-4,-2,-9,-4,7,7,-3,-7,5,7,6,6,2,-6,10,6,-4,6,9,8,3,-8,-10,-7,-5,-5,-6,4,4,4,5,9,-10,3,-6,5,-8,-8,-10,-5,9,-3,-2,-4,8,-4,8,2,-10,-7,-8,6,7,-6,6,3,3,10,-4,6,4,5,-1,10,-4,8,1,-9,5,-7,-9,8,-6,-9,-7,-4,-3,1,-8,7,-1,-5,6,-3,1,6,10,-2,-4,-9,-6,-10,-2,2,5,3,2,-8,-5,-3,-1,-6,3,-9,1,-8,9,-5,-10,-4,-6,-10,-6,-9,9,9,1,1,5,10,8,-4,-5,-9,-4,1,1,-10,-2,-9,-1,1,4,-5,-3,-7,-3,7,10,7,8,-5,1,-5,-4,-6,-3,-6,-10,-5,8,-2,-5,-10,-5,-8,-7,4,-8,-3,-5,9,5,-4,8,5,-3,6,-8,-2,5,9,-5,-10,-4,-7,-1,9,-2,10,-4,6,6,7,10,6,-3,7,-10,3,1,2,-6,7,-4,10,4,7,-9,3,-6,-7,5,-7,1,8,-7,4,-3,-1,-2,5,6,7,6,5,10,-1,5,10,7,10,10,7,-8,10,-9,7,9,-1,3,-9,9,8,9,4,5,9,-9,-9,-5,7,4,-9,8,-7,9,2,7,4,7,9,-1,9,5,8,-7,-5,-1,-5,8,7,-10,-5,-10,-3,6,-1,2,-8,-10,-8,1,9,10,10,5,-3,-8,-2,-9,5,8,-2,-6,9,7,4,-1,-2,6,-6,1,8,10,-8,-6,4,-9,-6,9,2,1,5,-8,2,1,6,7,-1,-5,-6,4,-7,-6,-1,-8,-2,8,10,6,-1,-10,-9,3,6,3,-3,1,1,4,-4,-6,1,4,1,3,-9,10,-2,9,3,9,10,-5,-9,4,1,-8,5,6,-3,7,4,9,-2,-3,2,-10,-3,-3,6,-6,7,-1,-7,8,6,10,-7,-7,7,2,3,10,-9,-10,2,1,-1,2,1,-6,9,8,-4,3,-4,-1,-8,-5,-5,1,-3,7,-7,10,2,5,-1,-7,6,4,-6,-7,5,-1,-8,-10,-9,3,-7,-3,10,-2], dtype = "int8")#candidate|1356|(2880,)|const|int8
const_1357 = relay.const([-1.244838,9.636329,1.218528,-1.456107,4.928966,-0.116416,-6.068089,-1.306360,6.175644,-0.562072,-1.705786,-5.419962,-1.359557,2.516251,6.563200,0.474268,0.065714,-5.159947,5.185376,8.018469], dtype = "float64")#candidate|1357|(20,)|const|float64
call_1355 = relay.TupleGetItem(func_599_call(relay.reshape(const_1356.astype('int8'), [16, 15, 12]), relay.reshape(const_1356.astype('int8'), [16, 15, 12]), relay.reshape(const_1357.astype('float64'), [20,]), ), 2)
call_1358 = relay.TupleGetItem(func_603_call(relay.reshape(const_1356.astype('int8'), [16, 15, 12]), relay.reshape(const_1356.astype('int8'), [16, 15, 12]), relay.reshape(const_1357.astype('float64'), [20,]), ), 2)
uop_1363 = relay.sqrt(uop_1339.astype('float32')) # shape=(3, 15, 16)
output = relay.Tuple([call_1345,const_1346,call_1355,const_1356,const_1357,uop_1363,])
output2 = relay.Tuple([call_1347,const_1346,call_1358,const_1356,const_1357,uop_1363,])
func_1366 = relay.Function([var_1338,], output)
mod['func_1366'] = func_1366
mod = relay.transform.InferType()(mod)
mutated_mod['func_1366'] = func_1366
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1367 = relay.var("var_1367", dtype = "float64", shape = (3, 15, 16))#candidate|1367|(3, 15, 16)|var|float64
func_1366_call = mutated_mod.get_global_var('func_1366')
call_1368 = func_1366_call(var_1367)
output = call_1368
func_1369 = relay.Function([var_1367], output)
mutated_mod['func_1369'] = func_1369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1322_call = mutated_mod.get_global_var('func_1322')
call_1391 = relay.TupleGetItem(func_1321_call(), 1)
call_1392 = relay.TupleGetItem(func_1322_call(), 1)
const_1393 = relay.const([[[1.587944,-1.669284],[-1.940629,8.222252],[9.228267,-6.228789],[-0.788439,-2.110166],[4.308979,7.959923],[-4.875675,-3.785031],[-6.795417,-6.979572],[-5.306807,7.147678],[-6.434329,5.753728],[-0.718234,9.827178]],[[-6.561950,7.318317],[3.296967,-8.275471],[-9.679397,0.630144],[9.791700,5.643628],[7.647007,-1.866575],[5.924212,6.885920],[0.690977,-4.595543],[-0.609504,5.072931],[-6.347404,3.522318],[4.444986,-9.156324]],[[3.285155,-9.179399],[-1.665175,6.759091],[2.008432,1.995920],[5.226889,-8.459261],[-5.679941,6.486353],[-5.819329,2.216979],[3.118638,-9.839465],[-6.250595,-7.706641],[-1.225576,6.301287],[0.027935,3.357550]],[[-2.540204,3.839086],[6.009700,4.958436],[8.568063,-4.224755],[7.846800,-3.089074],[-7.859566,2.718848],[9.586064,3.445327],[-7.220540,-5.544934],[8.703659,-9.330548],[4.747184,3.867258],[5.619768,-2.217195]],[[1.876871,-4.331379],[-5.734020,-4.843125],[-9.222364,-6.118674],[2.223686,3.100446],[-4.063053,7.145036],[3.012727,2.573102],[-6.946731,-0.641520],[6.037373,-8.654367],[5.364846,-0.774707],[9.191537,0.084040]],[[-3.090188,3.446809],[2.305264,-3.063982],[0.475630,2.222760],[5.185491,4.560922],[3.564673,-5.423764],[-2.056177,-4.162233],[4.831527,5.262735],[8.653556,-4.370385],[-1.890146,3.676664],[6.946772,8.134870]],[[-8.288575,8.692404],[-3.348766,2.619219],[-1.334566,-6.919897],[-3.716547,6.975494],[0.045714,-6.530024],[3.356422,2.242680],[-6.019273,6.707665],[-4.308945,-9.798229],[4.107517,-6.995556],[-4.443562,5.908380]],[[7.768652,8.196511],[-4.442434,-5.714638],[-3.287194,-6.898734],[5.617804,7.938870],[3.486295,5.593818],[-9.735965,-5.883933],[-3.295990,7.983758],[-7.362659,7.001060],[-1.133468,0.521265],[0.315142,7.075272]],[[-2.326747,5.180044],[7.074709,9.917754],[3.066635,-2.139365],[9.244108,4.447632],[4.760610,-7.504349],[-7.031420,-9.470819],[1.521833,0.733750],[3.392978,-8.651803],[7.992871,0.595541],[-3.380768,0.098022]],[[-0.385392,1.550409],[-7.761795,7.605802],[8.053689,7.960865],[8.281397,9.287950],[7.404647,-7.506470],[6.586004,-6.779898],[-9.611600,9.815492],[-2.378915,8.997702],[-8.094002,-4.478741],[2.608830,-9.863256]]], dtype = "float64")#candidate|1393|(10, 10, 2)|const|float64
bop_1394 = relay.greater_equal(call_1391.astype('bool'), const_1393.astype('bool')) # shape=(10, 10, 2)
bop_1397 = relay.greater_equal(call_1392.astype('bool'), const_1393.astype('bool')) # shape=(10, 10, 2)
uop_1429 = relay.rsqrt(bop_1394.astype('float32')) # shape=(10, 10, 2)
uop_1431 = relay.rsqrt(bop_1397.astype('float32')) # shape=(10, 10, 2)
uop_1434 = relay.exp(uop_1429.astype('float32')) # shape=(10, 10, 2)
uop_1436 = relay.exp(uop_1431.astype('float32')) # shape=(10, 10, 2)
output = uop_1434
output2 = uop_1436
func_1439 = relay.Function([], output)
mod['func_1439'] = func_1439
mod = relay.transform.InferType()(mod)
output = func_1439()
func_1440 = relay.Function([], output)
mutated_mod['func_1440'] = func_1440
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1499 = relay.var("var_1499", dtype = "float32", shape = (5, 15, 3))#candidate|1499|(5, 15, 3)|var|float32
uop_1500 = relay.acosh(var_1499.astype('float32')) # shape=(5, 15, 3)
uop_1510 = relay.sigmoid(uop_1500.astype('float32')) # shape=(5, 15, 3)
output = relay.Tuple([uop_1510,])
output2 = relay.Tuple([uop_1510,])
func_1529 = relay.Function([var_1499,], output)
mod['func_1529'] = func_1529
mod = relay.transform.InferType()(mod)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1530 = relay.var("var_1530", dtype = "float32", shape = (5, 15, 3))#candidate|1530|(5, 15, 3)|var|float32
func_1529_call = mutated_mod.get_global_var('func_1529')
call_1531 = func_1529_call(var_1530)
output = call_1531
func_1532 = relay.Function([var_1530], output)
mutated_mod['func_1532'] = func_1532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1547 = func_1439_call()
call_1548 = func_1439_call()
func_1366_call = mod.get_global_var('func_1366')
func_1369_call = mutated_mod.get_global_var('func_1369')
var_1550 = relay.var("var_1550", dtype = "float64", shape = (720,))#candidate|1550|(720,)|var|float64
call_1549 = relay.TupleGetItem(func_1366_call(relay.reshape(var_1550.astype('float64'), [3, 15, 16])), 2)
call_1551 = relay.TupleGetItem(func_1369_call(relay.reshape(var_1550.astype('float64'), [3, 15, 16])), 2)
uop_1558 = relay.sin(call_1549.astype('float32')) # shape=(10, 1, 2)
uop_1560 = relay.sin(call_1551.astype('float32')) # shape=(10, 1, 2)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1564 = func_1439_call()
call_1565 = func_1439_call()
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1580 = func_1439_call()
call_1581 = func_1439_call()
output = relay.Tuple([call_1547,var_1550,uop_1558,call_1564,call_1580,])
output2 = relay.Tuple([call_1548,var_1550,uop_1560,call_1565,call_1581,])
func_1582 = relay.Function([var_1550,], output)
mod['func_1582'] = func_1582
mod = relay.transform.InferType()(mod)
var_1583 = relay.var("var_1583", dtype = "float64", shape = (720,))#candidate|1583|(720,)|var|float64
output = func_1582(var_1583)
func_1584 = relay.Function([var_1583], output)
mutated_mod['func_1584'] = func_1584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1588 = func_1439_call()
call_1589 = func_1439_call()
output = call_1588
output2 = call_1589
func_1597 = relay.Function([], output)
mod['func_1597'] = func_1597
mod = relay.transform.InferType()(mod)
mutated_mod['func_1597'] = func_1597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mutated_mod.get_global_var('func_1597')
call_1598 = func_1597_call()
output = call_1598
func_1599 = relay.Function([], output)
mutated_mod['func_1599'] = func_1599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_1600 = func_1439_call()
call_1601 = func_1439_call()
output = call_1600
output2 = call_1601
func_1606 = relay.Function([], output)
mod['func_1606'] = func_1606
mod = relay.transform.InferType()(mod)
mutated_mod['func_1606'] = func_1606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1606_call = mutated_mod.get_global_var('func_1606')
call_1607 = func_1606_call()
output = call_1607
func_1608 = relay.Function([], output)
mutated_mod['func_1608'] = func_1608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1606_call = mod.get_global_var('func_1606')
func_1608_call = mutated_mod.get_global_var('func_1608')
call_1609 = func_1606_call()
call_1610 = func_1606_call()
output = relay.Tuple([call_1609,])
output2 = relay.Tuple([call_1610,])
func_1613 = relay.Function([], output)
mod['func_1613'] = func_1613
mod = relay.transform.InferType()(mod)
mutated_mod['func_1613'] = func_1613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1613_call = mutated_mod.get_global_var('func_1613')
call_1614 = func_1613_call()
output = call_1614
func_1615 = relay.Function([], output)
mutated_mod['func_1615'] = func_1615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1606_call = mod.get_global_var('func_1606')
func_1608_call = mutated_mod.get_global_var('func_1608')
call_1631 = func_1606_call()
call_1632 = func_1606_call()
output = call_1631
output2 = call_1632
func_1640 = relay.Function([], output)
mod['func_1640'] = func_1640
mod = relay.transform.InferType()(mod)
output = func_1640()
func_1641 = relay.Function([], output)
mutated_mod['func_1641'] = func_1641
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1690 = relay.var("var_1690", dtype = "float32", shape = (3, 16, 8))#candidate|1690|(3, 16, 8)|var|float32
uop_1691 = relay.exp(var_1690.astype('float32')) # shape=(3, 16, 8)
uop_1697 = relay.sin(uop_1691.astype('float64')) # shape=(3, 16, 8)
output = uop_1697
output2 = uop_1697
func_1699 = relay.Function([var_1690,], output)
mod['func_1699'] = func_1699
mod = relay.transform.InferType()(mod)
var_1700 = relay.var("var_1700", dtype = "float32", shape = (3, 16, 8))#candidate|1700|(3, 16, 8)|var|float32
output = func_1699(var_1700)
func_1701 = relay.Function([var_1700], output)
mutated_mod['func_1701'] = func_1701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1613_call = mod.get_global_var('func_1613')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_1712 = relay.TupleGetItem(func_1613_call(), 0)
call_1713 = relay.TupleGetItem(func_1615_call(), 0)
output = relay.Tuple([call_1712,])
output2 = relay.Tuple([call_1713,])
func_1716 = relay.Function([], output)
mod['func_1716'] = func_1716
mod = relay.transform.InferType()(mod)
output = func_1716()
func_1717 = relay.Function([], output)
mutated_mod['func_1717'] = func_1717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1824 = relay.TupleGetItem(func_1716_call(), 0)
call_1825 = relay.TupleGetItem(func_1717_call(), 0)
output = relay.Tuple([call_1824,])
output2 = relay.Tuple([call_1825,])
func_1833 = relay.Function([], output)
mod['func_1833'] = func_1833
mod = relay.transform.InferType()(mod)
output = func_1833()
func_1834 = relay.Function([], output)
mutated_mod['func_1834'] = func_1834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_1847 = func_1640_call()
call_1848 = func_1640_call()
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_1879 = relay.TupleGetItem(func_1716_call(), 0)
call_1880 = relay.TupleGetItem(func_1717_call(), 0)
var_1892 = relay.var("var_1892", dtype = "float32", shape = (10, 10, 2))#candidate|1892|(10, 10, 2)|var|float32
bop_1893 = relay.add(call_1847.astype('uint32'), relay.reshape(var_1892.astype('uint32'), relay.shape_of(call_1847))) # shape=(10, 10, 2)
bop_1896 = relay.add(call_1848.astype('uint32'), relay.reshape(var_1892.astype('uint32'), relay.shape_of(call_1848))) # shape=(10, 10, 2)
func_1529_call = mod.get_global_var('func_1529')
func_1532_call = mutated_mod.get_global_var('func_1532')
const_1899 = relay.const([-0.849928,4.924604,-4.844289,3.324871,-1.992002,-6.438776,-7.222117,-4.480905,4.010255,-8.501270,3.418716,1.533994,7.402976,-3.577784,-4.424599,0.437213,3.531872,-5.889367,-1.729906,-7.904072,7.114026,-4.073983,2.384104,-1.707962,9.986276,0.185199,0.431113,-5.066175,5.122093,9.810699,1.604638,-9.516508,-0.181193,-9.225086,-3.419944,5.342091,7.825882,-4.473637,-9.094764,-4.723669,4.912636,-5.361874,-9.714067,4.193650,-7.796018,6.786531,7.307433,-8.729989,-9.270136,-1.071097,4.795285,-8.908621,3.460059,7.275444,-4.344199,2.050034,8.182617,-8.867596,-0.502579,6.181357,-2.268691,6.011416,2.861642,8.189346,-7.887553,-7.215229,-4.043451,3.000801,0.006859,9.261349,-0.251085,6.599780,8.990504,4.313615,-5.949965,-0.596642,-2.644915,-2.989487,6.072059,6.692886,-2.622359,5.984333,8.493550,-4.626759,9.376188,-0.709255,1.374098,0.200791,1.829520,-4.138950,-9.589912,-4.849233,-8.007840,-5.965564,0.945319,-6.822106,2.545141,-4.186596,-7.051922,-5.221708,-5.243119,3.577744,-4.002158,-3.865340,3.801324,6.979890,4.508674,-8.981621,5.330142,1.103503,2.528366,-1.856757,5.992541,9.128487,2.939829,3.618834,-2.869439,1.278786,-4.178003,-7.346280,4.959412,2.535615,3.313508,-3.382323,-0.110705,4.573177,9.060079,-8.043099,-2.414117,-8.605571,7.964228,-9.299801,-1.702551,8.758949,3.339192,5.097516,9.040169,-9.812660,-2.867685,7.764768,-4.404562,-4.590176,-3.099162,9.470720,-6.827067,0.364037,7.691689,3.086062,8.744867,-2.226598,-6.913419,0.941080,-3.775972,9.420336,8.356426,6.065657,2.450538,5.175253,4.484688,8.388961,0.425948,1.590289,-2.407908,-8.445260,7.175962,-7.302974,-2.564503,-2.688398,8.079412,-0.574966,-4.272756,9.566170,1.069470,-2.537148,0.744247,4.778522,-5.349322,5.139564,8.879996,-3.224620,1.525628,9.226854,5.083247,-5.047231,5.326109,8.257852,4.677901,2.708692,1.318936,5.145051,9.599000,3.552195,4.457554,-2.405810,1.079583,-1.836298,-1.873191,-5.745040,9.764958,-3.145397,3.483128,-5.742531,-6.084529,-9.097660,1.333153,-1.859320,-0.731705,-3.658351,7.252328,-0.353140,-2.976620,5.475289,-0.738765,-5.479386,-8.987869,-9.715887,-4.782303,-5.219610,8.041967,-4.584309,-2.727882,3.888283,7.666668,2.100942,1.081182], dtype = "float32")#candidate|1899|(225,)|const|float32
call_1898 = relay.TupleGetItem(func_1529_call(relay.reshape(const_1899.astype('float32'), [5, 15, 3])), 0)
call_1900 = relay.TupleGetItem(func_1532_call(relay.reshape(const_1899.astype('float32'), [5, 15, 3])), 0)
output = relay.Tuple([call_1879,bop_1893,call_1898,const_1899,])
output2 = relay.Tuple([call_1880,bop_1896,call_1900,const_1899,])
func_1902 = relay.Function([var_1892,], output)
mod['func_1902'] = func_1902
mod = relay.transform.InferType()(mod)
mutated_mod['func_1902'] = func_1902
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1903 = relay.var("var_1903", dtype = "float32", shape = (10, 10, 2))#candidate|1903|(10, 10, 2)|var|float32
func_1902_call = mutated_mod.get_global_var('func_1902')
call_1904 = func_1902_call(var_1903)
output = call_1904
func_1905 = relay.Function([var_1903], output)
mutated_mod['func_1905'] = func_1905
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1914 = relay.var("var_1914", dtype = "float64", shape = (9, 4, 12))#candidate|1914|(9, 4, 12)|var|float64
uop_1915 = relay.sinh(var_1914.astype('float64')) # shape=(9, 4, 12)
func_599_call = mod.get_global_var('func_599')
func_603_call = mutated_mod.get_global_var('func_603')
var_1919 = relay.var("var_1919", dtype = "int8", shape = (2880,))#candidate|1919|(2880,)|var|int8
const_1920 = relay.const([-5.097391,-7.914732,-1.268447,2.049332,1.444239,5.955518,2.833886,-6.654061,5.805190,-8.155371,8.036655,7.768187,5.374547,-8.460849,2.869671,-4.947016,1.581954,-6.291188,-6.794961,-5.165455], dtype = "float64")#candidate|1920|(20,)|const|float64
call_1918 = relay.TupleGetItem(func_599_call(relay.reshape(var_1919.astype('int8'), [16, 15, 12]), relay.reshape(var_1919.astype('int8'), [16, 15, 12]), relay.reshape(const_1920.astype('float64'), [20,]), ), 3)
call_1921 = relay.TupleGetItem(func_603_call(relay.reshape(var_1919.astype('int8'), [16, 15, 12]), relay.reshape(var_1919.astype('int8'), [16, 15, 12]), relay.reshape(const_1920.astype('float64'), [20,]), ), 3)
output = relay.Tuple([uop_1915,call_1918,var_1919,const_1920,])
output2 = relay.Tuple([uop_1915,call_1921,var_1919,const_1920,])
func_1925 = relay.Function([var_1914,var_1919,], output)
mod['func_1925'] = func_1925
mod = relay.transform.InferType()(mod)
var_1926 = relay.var("var_1926", dtype = "float64", shape = (9, 4, 12))#candidate|1926|(9, 4, 12)|var|float64
var_1927 = relay.var("var_1927", dtype = "int8", shape = (2880,))#candidate|1927|(2880,)|var|int8
output = func_1925(var_1926,var_1927,)
func_1928 = relay.Function([var_1926,var_1927,], output)
mutated_mod['func_1928'] = func_1928
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1990 = relay.var("var_1990", dtype = "float64", shape = (13, 7, 8))#candidate|1990|(13, 7, 8)|var|float64
uop_1991 = relay.asin(var_1990.astype('float64')) # shape=(13, 7, 8)
func_1699_call = mod.get_global_var('func_1699')
func_1701_call = mutated_mod.get_global_var('func_1701')
const_2004 = relay.const([[0.954097,-3.506581,-4.098337,-4.543258,-6.016542,-8.541171,1.238365,-0.952102,-6.929117,-6.843564,-9.613518,-4.960977,3.091365,2.888024,4.039204,6.186463,-2.138169,-8.412820,0.783903,-4.489914,6.468692,1.024669,-5.415076,5.908324,1.785194,-8.742867,9.232512,4.805119,-5.081876,-6.786830,6.326224,2.183992],[-0.942700,-2.827493,-8.579752,6.501987,6.390942,4.935779,-5.415649,6.909299,-3.500013,-4.803118,-7.800316,7.218572,-4.667068,7.691172,1.809696,8.534903,-9.275660,-0.220971,-8.922653,-4.611169,-9.051021,0.693003,-3.756822,-5.538615,-1.716379,5.354736,-0.351286,-2.140217,-5.452658,4.257456,-7.524528,5.464367],[-2.945174,7.695112,-0.634629,3.476740,3.742959,5.924514,2.293262,1.570870,-2.444453,-4.341977,2.654867,3.975783,-0.443031,1.653851,6.918565,8.625399,-3.764273,0.900045,-8.232789,4.485681,2.171517,-2.440803,-9.912130,1.639143,-0.085699,-1.573620,-2.451347,3.454792,-5.844869,4.922597,-2.403695,2.094005],[0.628068,1.261412,7.694856,-6.769127,5.527624,2.541686,-3.624484,8.367628,3.455706,-8.798184,8.066126,-2.229883,-7.015628,-7.718540,4.630127,-4.925666,-9.403302,-7.390016,-5.522654,-7.115976,0.117419,-2.188624,-5.705237,-0.177355,6.617871,1.761829,7.686863,-8.294433,5.094432,-5.569015,-6.139012,-2.447041],[-5.536106,3.843895,8.213958,-9.285909,5.354581,-7.347990,-5.834494,0.965976,8.104345,7.273058,8.084875,-3.532359,-2.218159,8.289119,8.630809,1.850064,-3.822629,7.371500,-7.161150,5.359493,-3.296455,-4.134914,-7.033068,-6.671565,-0.389680,-2.774522,3.338006,9.733193,8.696310,-3.428963,-5.968397,-5.265519],[-7.836734,-6.132564,-8.680168,6.307599,6.857626,0.607153,1.380056,8.053858,0.207142,0.005131,-5.689062,-0.177049,3.407195,0.981537,-6.501333,8.750256,0.667170,-2.097772,3.613949,-2.248429,4.310694,-8.076822,7.554407,-6.516475,-3.615428,8.186494,-8.811711,-8.222319,-4.227245,1.143866,-5.316480,-0.923605],[-2.103320,2.254344,-0.112237,-7.502831,4.326382,-0.973206,-8.189250,-3.779057,7.651053,-3.684095,7.678074,2.608138,-5.894456,5.508753,9.503885,-8.395612,-6.456209,0.316260,1.556781,-1.194610,4.680824,8.604923,6.116341,-1.502461,8.929655,1.828394,3.217878,-4.709734,0.221153,-7.000221,6.423371,4.507186],[-4.999785,-4.753864,-3.141675,3.207107,-8.759035,-6.122443,-9.306875,-7.372779,2.410875,-9.183136,-9.119946,-0.707926,-3.893409,9.362366,0.234082,5.576172,7.654683,3.753583,-2.534021,5.986751,8.301330,4.664160,-3.261801,7.212472,0.502612,2.448987,-6.753850,7.378901,-9.729198,5.081636,5.200117,-4.917398],[-0.701102,3.888531,-4.412708,3.337683,-2.414927,6.062597,-3.356978,-0.733430,-5.823868,-8.059641,5.179187,-2.021755,-1.752587,4.085712,-1.266601,-2.638000,2.097002,-2.848409,2.356507,8.546468,-5.496246,-0.382302,3.304798,-2.990142,-4.330761,-8.951180,-2.849675,-0.005232,-2.276302,1.625548,0.818146,-0.392602],[1.494038,-5.967134,-0.111620,-6.951729,-6.220024,-9.147398,2.276811,4.903612,8.331509,2.227906,-5.076521,-5.154368,0.654080,-9.394138,0.705063,0.300389,9.951911,1.998907,1.299234,-9.119577,8.912624,3.095375,6.556184,-4.524449,-9.564591,-3.792259,7.774127,-6.397501,-6.363019,4.638582,9.248571,-6.434848],[-4.670918,-4.559301,2.501193,8.610237,6.296171,2.867987,-8.014049,0.961677,6.199877,2.629818,-3.961244,2.751577,-8.758457,7.726141,4.891540,-3.586125,3.598717,0.724901,6.716764,7.284718,3.976535,7.109183,5.826627,5.918416,5.589219,1.893226,-8.672947,-6.991927,-6.080584,-0.807676,-8.668085,8.997535],[9.095256,-5.748956,-3.101784,-4.245471,3.914757,1.658893,-7.130851,7.570697,7.904609,-8.745988,-0.435449,1.864151,-7.279657,-3.177701,-6.886697,-8.859769,2.112432,8.560759,5.281021,4.571360,8.300472,0.308164,4.407769,8.656633,7.713673,-6.051032,8.310388,-9.427497,3.903075,-3.517834,4.966954,-5.686740]], dtype = "float32")#candidate|2004|(12, 32)|const|float32
call_2003 = func_1699_call(relay.reshape(const_2004.astype('float32'), [3, 16, 8]))
call_2005 = func_1699_call(relay.reshape(const_2004.astype('float32'), [3, 16, 8]))
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_2011 = func_1640_call()
call_2012 = func_1640_call()
output = relay.Tuple([uop_1991,call_2003,const_2004,call_2011,])
output2 = relay.Tuple([uop_1991,call_2005,const_2004,call_2012,])
func_2014 = relay.Function([var_1990,], output)
mod['func_2014'] = func_2014
mod = relay.transform.InferType()(mod)
var_2015 = relay.var("var_2015", dtype = "float64", shape = (13, 7, 8))#candidate|2015|(13, 7, 8)|var|float64
output = func_2014(var_2015)
func_2016 = relay.Function([var_2015], output)
mutated_mod['func_2016'] = func_2016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_2036 = func_1439_call()
call_2037 = func_1439_call()
uop_2042 = relay.sigmoid(call_2036.astype('float32')) # shape=(10, 10, 2)
uop_2044 = relay.sigmoid(call_2037.astype('float32')) # shape=(10, 10, 2)
bop_2048 = relay.greater(uop_2042.astype('bool'), relay.reshape(call_2036.astype('bool'), relay.shape_of(uop_2042))) # shape=(10, 10, 2)
bop_2051 = relay.greater(uop_2044.astype('bool'), relay.reshape(call_2037.astype('bool'), relay.shape_of(uop_2044))) # shape=(10, 10, 2)
func_1366_call = mod.get_global_var('func_1366')
func_1369_call = mutated_mod.get_global_var('func_1369')
const_2059 = relay.const([-0.649886,-3.652955,-0.804081,9.049147,3.489842,-1.768905,-0.344764,-0.516108,1.869194,6.379439,3.725060,-0.353469,-1.800559,5.393820,-0.822161,5.395838,0.864491,-3.526789,-7.110468,3.497786,2.310818,6.315168,-7.701893,-4.367280,7.951001,2.737895,6.284930,-0.934384,-6.212689,-4.285345,-7.096297,0.115818,8.599848,-1.201556,-6.863035,5.414307,5.127175,7.354084,-0.392838,9.906437,2.252182,8.576721,-3.614253,9.608926,4.284801,0.140468,8.906159,5.752074,-1.512178,9.395673,9.344669,5.761280,2.366794,6.000923,-7.372413,-3.064845,2.020276,8.573264,1.128742,9.842349,-0.844747,-0.431409,6.042356,-3.118621,0.980212,-2.507342,4.039155,0.470239,-3.153824,-8.172004,0.308085,6.344963,-9.734707,-8.906930,8.521840,-7.824346,-0.999393,1.088732,1.921015,-2.649942,8.593705,6.950120,-9.204488,-5.104512,5.514054,7.977986,6.270003,-5.427283,7.743259,1.028339,-9.143673,-3.727713,-0.083684,-3.751876,-8.895893,3.517426,-8.896563,-9.397992,1.936440,6.477613,7.557656,-4.427809,1.155600,9.197384,4.329624,9.346981,-9.050111,3.458885,-3.635989,-9.507562,-1.183822,-1.791702,1.981726,4.173170,7.433779,5.220551,7.284494,1.476505,-9.307941,-1.367835,4.253963,6.160049,0.379189,8.249729,1.133721,-7.831239,4.969720,-0.044454,9.278711,5.797255,-8.746185,-5.976462,-6.653725,8.581029,-2.035100,3.088858,9.413672,2.256024,6.635514,-2.668023,2.955117,-2.705449,-1.693467,3.628072,-2.378222,-8.914387,4.897478,-4.682358,9.935172,7.649587,9.245439,6.897432,2.861194,-2.352956,0.319725,8.086238,6.915192,8.447361,-6.674292,-2.342359,-8.914937,-6.453460,9.455950,6.481055,-0.882650,-2.069578,0.208741,-4.005612,-9.226541,7.537485,-9.831021,-4.357292,-0.320860,9.289445,-6.049823,4.067777,-5.130398,6.174988,2.271443,-6.681815,7.846899,6.890769,6.966340,5.727313,-6.352168,1.693842,-0.536611,9.384902,-2.097325,2.524048,-1.910220,5.180841,-5.358529,-9.018326,5.324507,2.214503,1.331633,-6.420951,6.415829,-2.098381,-8.377107,-8.301644,-6.063992,-9.511516,-9.122181,1.737732,-3.530115,4.029751,1.966265,-3.393367,3.413291,4.837709,5.548022,8.478843,-7.928440,-9.725421,5.894180,8.015349,-4.227711,-9.046149,7.377229,6.858439,-6.871836,1.701945,-1.238755,3.956929,9.248229,-0.349913,-4.774729,2.175330,-3.977732,8.140824,-5.892663,8.459772,-8.203700,1.677535,5.489198,-7.559542,-5.726325,-0.933097,3.098399,-0.415844,-1.105956,5.437216,-6.289044,0.344094,0.285537,-7.957313,0.508534,-3.983887,-6.266861,-2.045996,6.983653,9.919096,-2.967483,-7.354481,5.722461,-7.361243,-4.629663,-1.245184,6.371132,1.316214,9.025343,-3.564070,3.251837,-0.723899,6.176515,7.138611,4.302640,-2.564937,-0.706522,-3.195737,4.502219,-0.509561,-5.719863,-8.542359,-3.260595,-9.349973,0.588514,7.987710,-0.278914,-3.018631,-0.933715,-8.887507,7.061736,8.070528,3.546525,8.441862,-5.206439,-3.261721,6.446936,-5.172575,-8.436392,4.473134,-2.619808,-9.013092,-2.513678,-1.985212,8.144542,0.555474,8.560145,-0.878923,-4.746275,8.770994,1.407009,7.075581,-4.117520,6.179948,1.085750,-3.343591,2.038766,-7.253387,-1.187985,-0.820352,3.085046,-5.753233,-9.635631,8.725876,-5.810578,0.726033,7.666323,-7.149626,8.338100,-7.611225,-6.565943,-0.113002,-6.908840,-7.271873,2.585372,-0.688648,-8.738386,5.443947,1.006969,2.872858,0.758807,-3.871822,2.435246,-3.755886,-9.405361,8.103476,9.388817,-6.967949,-8.629592,-7.919833,8.586593,-2.376762,6.943847,-6.400838,3.899547,9.041887,-8.201494,6.135002,-1.512893,-8.777094,-5.502507,-9.963772,5.080582,2.125099,8.033531,2.195463,-1.999584,-6.775691,6.726091,6.594193,-3.346356,7.496546,-7.609352,-1.836796,-1.793904,3.190652,8.072251,6.300695,-3.129556,-4.599067,-8.426989,-4.219354,-3.631616,2.880202,8.043288,-1.231788,1.529938,-4.443926,-9.521576,-9.806403,-5.152971,3.178440,7.996198,-3.364465,-8.883710,1.372315,8.826621,6.898511,-4.154796,2.798232,5.108596,3.933571,-4.682350,-6.405236,7.453457,1.807849,-2.178016,1.958016,6.158975,1.643470,-7.076486,6.575800,-2.507243,9.520492,8.484622,-7.124199,-5.292650,9.509290,-7.216819,8.767829,-7.224693,0.223775,-1.693507,4.911801,-5.075149,2.641089,6.982464,-7.839722,6.575481,3.700543,3.782007,-4.587078,4.432466,-0.601948,6.869458,9.573433,-8.695847,5.040786,1.160250,8.146969,6.100220,4.604490,5.522274,3.042919,2.287938,3.294851,-7.261704,4.488220,3.661673,7.143882,9.236783,-3.983956,3.846229,-1.847769,-8.061978,6.277031,-7.535961,2.089334,-0.956974,4.062012,6.188760,-0.875313,-5.612119,0.464364,8.776121,-7.943533,-7.512243,0.863591,-4.345786,-0.729835,0.637712,3.643470,-7.435459,5.026594,9.139043,8.200419,0.652843,-0.636070,2.907255,9.267366,3.468370,5.776235,-6.652147,0.989535,2.816713,-4.428426,9.076283,-7.485640,-5.297984,7.573299,-0.933312,-6.363815,-9.608751,0.839704,-0.413793,5.346010,9.317310,2.680149,6.397658,-8.511011,5.320258,1.899486,-0.019652,-7.227995,5.530625,-2.898947,-7.260741,8.507261,-9.013797,-5.448291,2.825105,-7.567423,9.210116,-0.651041,-4.228629,2.560184,7.390135,2.059042,-1.622550,-6.951502,4.398775,-2.779893,4.129465,-8.641907,-3.122411,4.514744,-7.613319,-3.535736,6.598754,-2.030610,-3.885977,4.740880,-3.914407,5.661374,0.222479,-2.503846,8.945211,-7.704821,-3.452050,-8.759204,-3.869073,-1.268224,7.881003,-9.573203,-8.947762,-8.967641,-5.681070,-2.252468,-5.824331,6.575165,-7.331006,-0.412028,-0.883303,-7.224070,-8.323778,-9.500456,-6.609845,6.096185,8.827859,0.159883,2.139615,-2.814099,0.927290,-2.774673,6.282246,2.015069,-3.211296,2.541219,6.747396,2.861457,-1.917425,-1.262809,4.086416,-8.841707,4.767502,-4.557085,6.222223,-2.294589,2.144566,2.188693,-0.419429,-5.264050,-1.118417,-3.078021,-2.720003,2.249940,3.742098,2.966448,-0.317640,1.105485,6.268142,-8.200160,9.970600,-6.191315,7.081569,7.029613,-8.429247,-3.440957,5.385441,-6.350517,4.971731,-3.248385,8.080098,0.426665,0.057708,8.243036,-9.568624,9.487423,-0.142301,-1.665008,1.135603,-6.117581,-7.113586,4.392689,0.878113,6.627160,2.235147,4.059161,2.119451,-2.649004,8.188096,-7.595265,9.772421,2.372221,9.870746,-7.989760,9.283677,-8.078759,1.689774,8.136912,-0.253899,6.891151,-9.887629,-0.450057,6.608754,-7.818817,9.546387,-4.438280,3.681826,-0.953747,-2.902924,7.012403,9.799419,7.645537,4.289949,8.444831,6.565536,-4.985317,1.294199,4.492387,4.175448,-5.482625,-7.878366,-6.467339,-3.041770,-6.173389,3.052840,9.930821,-3.782057,8.819706,7.151471,7.805518,-4.860370,5.888616,-7.669066,-6.804855,-3.755711,-0.112006,-4.982842,-6.212441,-4.827440,5.586689,7.305547,-8.941586,1.398766,0.667122,1.348090,0.447816,-2.572507,9.027594,5.134161,6.779905,-5.311613,5.759976,-1.306159,-3.133245,-8.169857,-2.965321,-3.412712,0.006015,-8.062531,-6.332671,8.763525,7.800960,-3.822949,4.065397,2.532919,-4.696273,-0.880695,-5.389553,3.692593,5.974215,-9.012009,0.552645,4.628261,-9.217927,-8.536738,1.056995,-2.669700,2.557270,6.144317,-1.465986,3.160467,1.372062,-9.873321,-9.882046,-1.883623,-4.760872,8.828123,6.455739,-0.416017,4.949000,-5.179045,0.154318,8.694343,-3.319867], dtype = "float64")#candidate|2059|(720,)|const|float64
call_2058 = relay.TupleGetItem(func_1366_call(relay.reshape(const_2059.astype('float64'), [3, 15, 16])), 1)
call_2060 = relay.TupleGetItem(func_1369_call(relay.reshape(const_2059.astype('float64'), [3, 15, 16])), 1)
output = relay.Tuple([bop_2048,call_2058,const_2059,])
output2 = relay.Tuple([bop_2051,call_2060,const_2059,])
func_2064 = relay.Function([], output)
mod['func_2064'] = func_2064
mod = relay.transform.InferType()(mod)
mutated_mod['func_2064'] = func_2064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mutated_mod.get_global_var('func_2064')
call_2065 = func_2064_call()
output = call_2065
func_2066 = relay.Function([], output)
mutated_mod['func_2066'] = func_2066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_2069 = func_1640_call()
call_2070 = func_1640_call()
output = call_2069
output2 = call_2070
func_2072 = relay.Function([], output)
mod['func_2072'] = func_2072
mod = relay.transform.InferType()(mod)
output = func_2072()
func_2073 = relay.Function([], output)
mutated_mod['func_2073'] = func_2073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2073_call = mutated_mod.get_global_var('func_2073')
call_2088 = func_2072_call()
call_2089 = func_2072_call()
output = call_2088
output2 = call_2089
func_2090 = relay.Function([], output)
mod['func_2090'] = func_2090
mod = relay.transform.InferType()(mod)
mutated_mod['func_2090'] = func_2090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2090_call = mutated_mod.get_global_var('func_2090')
call_2091 = func_2090_call()
output = call_2091
func_2092 = relay.Function([], output)
mutated_mod['func_2092'] = func_2092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_2102 = relay.TupleGetItem(func_2064_call(), 0)
call_2103 = relay.TupleGetItem(func_2066_call(), 0)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_2127 = func_1439_call()
call_2128 = func_1439_call()
var_2131 = relay.var("var_2131", dtype = "float32", shape = (10, 10, 2))#candidate|2131|(10, 10, 2)|var|float32
bop_2132 = relay.subtract(call_2127.astype('uint16'), relay.reshape(var_2131.astype('uint16'), relay.shape_of(call_2127))) # shape=(10, 10, 2)
bop_2135 = relay.subtract(call_2128.astype('uint16'), relay.reshape(var_2131.astype('uint16'), relay.shape_of(call_2128))) # shape=(10, 10, 2)
uop_2138 = relay.asin(bop_2132.astype('float32')) # shape=(10, 10, 2)
uop_2140 = relay.asin(bop_2135.astype('float32')) # shape=(10, 10, 2)
output = relay.Tuple([call_2102,uop_2138,])
output2 = relay.Tuple([call_2103,uop_2140,])
func_2142 = relay.Function([var_2131,], output)
mod['func_2142'] = func_2142
mod = relay.transform.InferType()(mod)
var_2143 = relay.var("var_2143", dtype = "float32", shape = (10, 10, 2))#candidate|2143|(10, 10, 2)|var|float32
output = func_2142(var_2143)
func_2144 = relay.Function([var_2143], output)
mutated_mod['func_2144'] = func_2144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_2176 = func_1640_call()
call_2177 = func_1640_call()
output = call_2176
output2 = call_2177
func_2178 = relay.Function([], output)
mod['func_2178'] = func_2178
mod = relay.transform.InferType()(mod)
mutated_mod['func_2178'] = func_2178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2178_call = mutated_mod.get_global_var('func_2178')
call_2179 = func_2178_call()
output = call_2179
func_2180 = relay.Function([], output)
mutated_mod['func_2180'] = func_2180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1322_call = mutated_mod.get_global_var('func_1322')
call_2228 = relay.TupleGetItem(func_1321_call(), 1)
call_2229 = relay.TupleGetItem(func_1322_call(), 1)
output = call_2228
output2 = call_2229
func_2238 = relay.Function([], output)
mod['func_2238'] = func_2238
mod = relay.transform.InferType()(mod)
output = func_2238()
func_2239 = relay.Function([], output)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2242 = func_2238_call()
call_2243 = func_2238_call()
func_599_call = mod.get_global_var('func_599')
func_603_call = mutated_mod.get_global_var('func_603')
const_2245 = relay.const([[-3,-5,-7,-4,-10,9,-4,-9,-2,-1,8,1,8,-5,1,-5,-2,-3,-7,-1,-10,10,5,6,2,4,-1,-8,-6,3,-2,2,-1,3,3,-4,6,6,-3,1,-2,-5,-9,-4,-6,2,7,2,-8,7,-8,-4,-7,6,-5,-7,-3,1,-3,-8,-4,-7,-4,-3,1,-4,5,3,-10,-1,-7,1,-1,3,1,-5,10,8,-10,-6,4,-1,-10,8,5,-3,10,-4,10,6,-9,-6,2,4,-6,-2,2,9,8,-2,-9,-9,10,-1,-3,2,8,4,2,2,10,-10,7,-4,7,10,-2,-6,-4,-5,-3,-10,4,3,-4,6,8,6,-5,2,10,-7,-3,-5,9,-6,6,5,10,8,2,-5,9,-8,6,6,6,-8,-8,7,-4,10,-7,-10,1,-10,-1,5,-10,4,-5,-2,8,9,5,-1,-7,9,-4,-10,6,-7,-6,-6,-5,10,5,-8,-4,-6,1,7,8,3,-4,6,2,8,-6,-4,-7,1,-8,4,8,-2,7,8,-7,7,3,-3,9,-4,-6,-7,3,-6,9,-5,-9,-5,-8,4,-3,7,6,-4,1,-9,-8,-1,-4,-4,-4,9,7,2,8,-3,6,-10,3,-7,-2,1,-3,-1,-9,10,-5,7,-5,-1,4,6,7,-2,10,3,6,-1,8,5,-8,-1,6,-7,8,5,-4,-1,7,-1,5,-8,-10,9,3,-7,9,-6,-7,-7,2,4,5,7,1,8,4,6,-4,-3,-8,-10,8,3,8,10,-4,-6,-10,-2,2,8,5,-9,-8,8,5,-5,3,-10,-8,10,5,-2,2,-7,-3,2,10,8,6,-3,5,5,6,8,-6,-7,-4,-5,2,-1,-8,2,6,5,8,-2,8,1,-3,-1,7,9,8,10,-9,-6,3,6,-1,-1,2,4,-1,5,5,-4,-5,-6,10,-4,6,-7,-9,-10,5,-9,-7,9,7,-3,-2,-7,-1,-10,8,9,2,-4,-8,-1,-8,-9,3,-2,-4,5,1,10,6,2,-4,9,-6,6,9,-8,-8,-3,-5,-1,9,4,9,-3,-6,10,-7,-5,-2,-8,10,10,-3,9,8,-8,10,-9,9,-6,9,6,-3,-1,-4,9,-5,4,-2,5,-6,8,-6,-7,-1,2,8,-7,9,-9,-9,10,5,-9,8,-8,-10,2,-5,2,3,7,-2,-4,6,-7,-10,-6,-3,-4,2,7,10,7,10,3,-5,-5,-7,-9,2,8,5,9,-1,-8,6,-5,9,-4,-3,-4,-9,5,-10,1,-4,-6,-2,-6,-7,-8,-4,-1,-6,3,4,-8,-8,1,1,2,10,6,-10,-7,-9,-9,-7,-7,7,-2,7,6,-5,5,-8,3,2,1,2,-10,10,-5,10,-10,1,-8,2,-4,-10,4,6,7,5,-2,4,7,1,-3,-1,10,2,10,3,-2,-3,-10,-2,-6,4,3,10,-4,-9,4,7,-3,1,7,-7,6,3,-8,-4,3,10,8,5,1,-6,-7,-8,-5,4,-4,9,1,-7,-9,1,10,10,-3,9,-1,10,9,-8,8,4,-3,1,7,2,2,-9,-9,10,4,-10,6,2,-8,8,2,-6,-7,10,-7,-9,10,-1,7,-2,3,-5,-2,4,9,5,-6,-8,-2,-4,-3,-7,-10,-3,-2,-9,9,-5,3,10,-3,-5,10,9,-4,-10,-5,1,7,-4,10,-5,-7,9,-2,-2,-8,2,-10,9,-4,-10,-7,-4,-6,-5,-2,-5,-3,-9,-3,-1,-9,8,-4,5,7,-6,-8,-1,1,-1,8,-1,10,7,-2,4,-3,-1,1,-6,-1,5,5,4,-1,8,-10,-2,9,-4,10,-2,-10,10,9,2,-10,-9,-2,-4,9,4,-3,10,6,4,-3,10,9,7,-8,8,-5,-5,-2,-9,3,10,10,7,-7,-3,-5,-6,-3,-2,1,10,-7,-2,-4,-9,6,2,-3,-1,9,-1,-9,9,-9,4,3,7,-9,-8,-1,1,-10,3,-1,4,-10,-4,-1,2,6,-1,8,-8,8,-1,4,-6,6,-8,6,6,-6,-5,-3,-8,-3,-5,-8,9,10,-6,-3,-9,-4,5,-10,5,9,-4,7,3,-2,2,-3,9,-2,-8,-9,-5,5,-2,10,4,7,6,-9,-5,-7,-4,-7,-2,7,-5,8,-1,1,9,-9,3,-10,-2,-5,-3,-6,-3,-9,4,-6,2,9,6,-7,1,9,-3,-2,9,4,10,-8,-2,7,-2,-5,4,10,-5,-8,-2,-10,-5,10,10,7,-3,-10,-3,-1,7,-9,-1,4,3,-10,-6,-10,5,-8,-7,2,1,4,-8,-6,10,-7,-6,5,-2,6,9,10,9,6,4,-3,9,-6,4,-3,9,7,10,5,-1,9,-9,2,8,4,-8,-4,6,-6,-4,-7,9,-8,-8,-1,6,-6,1,-2,10,1,-3,-4,7,-1,9,1,4,8,-2,8,1,2,-4,2,-10,-1,-8,-2,-9,5,3,-7,-5,6,4,-7,9,-6,4,8,-1,-5,-8,-5,3,4,-7,-2,5,-2,-3,-3,-6,9,9,4,-8,10,-7,2,6,-6,8,5,-8,-2,4,5,-6,-2,4,6,4,-10,2,10,10,9,6,1,1,-4,1,-6,6,4,3,-3,-8,9,7,-8,-7,-4,2,-4,-9,7,10,6,3,-7,2,5,-3,9,-6,-6,5,6,5,10,8,3,5,5,9,-6,2,-10,10,6,10,8,1,-5,-4,10,6,-2,-3,9,-9,-5,-10,7,-8,-3,4,-6,-5,-3,5,1,-9,2,-9,5,6,10,-9,-6,-9,-7,-10,10,-3,-4,-6,-10,9,-6,3,-6,-5,6,3,-3,1,-7,-3,8,-8,4,9,-9,-8,-9,-8,1,-3,-7,1,1,2,-2,-7,-10,-5,10,-2,4,-4,2,-10,-5,-2,-1,4,2,2,-10,-6,-3,-7,-5,-2,9,-2,1,-4,4,1,-8,5,-9,-5,5,1,2,-3,-7,4,4,-6,7,-9,7,-6,5,6,10,4,5,-5,5,4,4,9,5,1,7,-4,-2,-1,2,2,1,9,-3,-4,2,-2,7,2,-7,5,5,-10,2,3,-9,7,-10,7,-1,-4,1,1,7,10,-8,-10,6,7,1,1,-4,-9,3,8,9,8,7,-7,-5,-8,2,6,-10,-4,-3,-1,1,3,-8,-1,4,8,-1,6,10,8,4,9,-9,2,-8,-10,5,-7,4,-1,-9,10,1,-7,1,-4,1,6,-4,1,3,3,5,-10,-5,-9,-9,-6,6,3,9,10,-1,-10,-7,9,4,-8,9,10,-7,2,-8,6,2,-9,9,2,10,-6,-5,-6,6,-8,4,-3,-6,6,-3,-8,-6,-5,10,6,9,6,-7,-5,-8,10,-2,2,-7,-4,5,-5,-2,-7,-8,-2,-4,-3,1,-8,4,3,-2,-5,-5,1,-2,-2,-7,-7,-3,3,7,2,5,-9,7,-4,8,10,-6,-5,7,3,10,8,8,3,-7,-5,5,1,5,3,-5,-9,5,-1,3,8,-5,7,10,-1,6,-1,-10,-5,10,-10,-4,-5,-1,3,2,9,2,1,7,10,7,-4,-6,2,8,8,-9,1,1,5,-7,-1,10,10,-3,1,-2,7,-4,3,-8,-2,-5,-8,6,10,-10,2,-2,-9,5,-6,-7,-4,-9,2,7,6,-8,-8,10,10,10,3,-6,-8,-6,-7,-5,-3,7,4,3,6,4,10,6,7,-3,8,5,-2,10,4,-10,2,6,1,-3,3,-3,-5,-2,-4,5,6,-10,2,10,7,-5,-9,-4,10,-9,9,5],[-10,-6,-4,8,2,-10,10,-8,-10,-8,4,9,-1,7,10,-2,3,-5,-1,-8,-3,-5,10,1,-8,9,3,8,-6,-4,8,-7,5,7,8,-9,8,5,-9,10,-7,9,-8,-6,1,1,5,2,3,-6,-7,-2,-8,4,5,-5,2,-4,3,5,7,5,5,2,7,10,4,10,9,9,8,6,-8,-10,-8,4,10,-9,-7,4,-10,9,-6,-6,-4,1,-9,-2,7,9,-7,-3,4,-4,3,-6,-4,-7,-5,7,9,3,-5,4,-9,7,8,2,2,-5,-6,9,8,-2,2,4,7,9,4,-4,-8,10,-3,-10,-10,3,7,-8,2,8,9,-3,-9,8,8,8,-5,2,3,-4,-8,-1,-10,8,8,4,-7,-4,1,-2,4,-5,-8,-6,10,4,-6,2,3,-8,7,-10,8,1,-4,8,-2,-6,1,-1,-3,-8,-1,6,2,7,-3,2,-1,-5,-7,-4,6,-9,-3,8,7,-6,8,-4,-4,-10,10,-2,-6,-5,-10,1,-8,-4,3,8,10,10,-3,-10,7,-6,1,-5,5,-1,-8,10,5,10,6,7,9,-3,4,-1,-3,-8,-7,3,-5,-6,9,3,-9,-1,9,10,7,-4,9,2,4,-8,4,-2,8,-4,-5,-2,-7,9,2,8,5,10,9,7,1,4,-7,-6,6,5,-6,6,-9,-1,-4,-10,-3,2,2,5,5,1,-8,10,-7,-5,-9,8,4,8,-2,-7,-9,-7,8,-6,-1,-6,6,-1,8,-9,7,-8,-9,-10,-7,4,-8,8,-2,3,-5,-10,-5,-7,-9,4,2,-10,8,-9,-9,-10,-5,4,-7,1,-6,-3,4,-5,-4,10,1,-8,9,4,4,6,-6,-9,9,-5,10,7,-7,8,3,9,7,-5,-7,-6,-4,-10,-5,3,8,-1,5,-4,-2,6,-8,1,4,-2,6,-2,10,-3,3,-9,6,-1,7,3,-6,5,4,1,-4,9,-3,-10,-6,-10,-9,-2,-8,-5,-8,4,-9,-10,-9,-1,6,-10,-4,3,-5,1,-1,-8,5,6,4,-7,-1,6,-10,2,10,4,-4,5,8,-3,8,10,7,-9,5,5,-5,-5,-9,-10,1,-4,10,6,5,9,-1,9,2,-10,-5,3,6,-4,7,6,5,4,-7,-3,10,-8,-10,2,6,-9,6,1,-1,9,-9,7,2,1,-2,4,8,-6,10,10,-7,-6,-2,7,4,-1,-10,8,2,5,-4,7,-2,10,-8,-7,1,1,4,7,3,-2,-8,7,10,5,1,-5,6,5,10,-2,7,4,-1,-1,1,-7,2,3,4,-5,2,7,9,-2,4,-10,7,-4,5,3,7,-8,-4,2,-9,-4,-8,8,5,-6,6,-1,10,-1,1,4,4,10,3,7,-8,4,3,5,6,6,5,-4,5,1,-9,-5,-7,10,-6,3,-7,-1,-10,8,-6,-5,4,-10,-5,4,-4,-7,-3,-10,-4,-4,-9,-3,1,-3,8,2,7,10,10,8,-10,-6,1,-3,-8,-6,-3,-4,-10,3,-4,1,-8,-5,-2,4,-7,-6,-6,-1,-7,-1,-6,7,1,8,-7,-7,10,3,7,4,10,2,3,2,2,2,-8,8,1,5,4,2,7,6,7,-10,3,4,-7,6,2,9,-7,1,4,-5,-9,-4,4,-10,1,-9,2,-10,4,8,4,-7,-6,-8,-4,9,-9,10,3,6,10,8,-1,-10,-4,10,-8,10,5,4,-10,3,-8,-5,-2,6,-8,-3,3,-5,-4,7,-4,-7,5,-6,-6,4,-1,6,-2,5,-7,9,6,8,-1,-1,2,-1,1,1,8,3,4,3,4,-6,-10,10,10,-5,1,-5,-6,-9,6,6,5,5,1,-3,-10,5,-5,8,-2,-6,1,-7,8,5,6,-1,-1,10,6,8,-4,6,7,-3,-8,-4,-10,7,-9,-5,-4,-5,3,-8,1,-5,-8,-2,-6,5,-6,3,2,-6,-4,7,7,4,7,1,9,-1,-8,3,-10,9,1,-1,-4,5,8,-6,4,-5,2,-9,3,-8,-4,6,-1,-1,-1,-7,-1,-2,2,2,-8,7,4,-10,7,-7,-1,9,9,6,4,4,-6,2,6,4,-4,5,6,-4,-7,5,3,-2,6,4,-3,-3,7,-7,-3,9,1,-5,1,-1,10,6,4,10,8,-7,-4,-10,-10,-4,-9,10,6,8,-5,-6,8,8,10,9,-2,8,9,-7,-8,-1,5,-6,7,10,4,-6,-6,2,4,3,-10,-4,-3,-9,3,6,1,2,-6,1,8,2,-2,1,8,4,7,10,-6,-10,10,10,10,1,-4,-7,8,10,6,7,-7,5,-6,5,3,-4,3,-4,4,2,8,2,-1,-7,4,-4,-7,-7,5,9,-7,-10,-5,-7,10,8,-1,5,5,-2,7,9,6,-9,8,-8,10,-9,-2,5,6,-1,8,-10,9,-1,9,-2,-8,5,-6,-4,8,-3,-10,2,4,4,9,-4,-7,5,-6,10,-6,1,5,-2,9,-5,4,6,3,1,-5,10,-9,-7,-2,1,1,3,7,2,9,-4,7,2,-1,1,5,7,8,2,-10,-9,-5,8,-10,-10,8,-3,-6,-4,-5,3,8,-5,-4,6,10,-7,-2,10,7,-10,-6,9,-7,10,-10,1,3,-2,-2,2,-8,8,-6,-1,-8,8,-3,7,10,1,8,-5,7,-7,10,3,-10,7,1,7,-8,-5,-1,-2,-8,10,2,-9,7,-9,7,6,-7,3,10,1,-6,10,1,-10,-4,6,-8,-6,-3,3,-1,9,-9,-7,-6,-8,7,2,3,-6,2,4,9,4,-6,-3,-5,6,9,-4,2,-7,-3,6,1,-2,3,3,-7,3,-6,-2,-1,5,-2,6,3,4,2,-4,9,6,-2,-4,-5,-4,-3,10,-7,-5,5,6,5,-6,7,2,5,-9,-4,-10,10,-10,2,-9,6,-1,-7,1,-4,-1,-6,-8,10,2,10,4,5,5,3,-8,9,-10,-6,-8,-7,-3,1,-7,-9,-4,-8,1,4,1,-9,8,10,-4,-8,-7,9,-1,-1,1,5,1,6,5,9,7,6,-7,3,3,4,-8,7,-5,-8,-10,-4,4,-4,-1,-8,-10,4,-1,9,-2,-3,7,-2,8,-1,-10,-9,4,-7,6,-3,-10,-4,-8,4,-5,10,6,-6,-9,5,9,-6,-9,10,-8,4,4,8,10,-1,8,-8,-3,-1,9,-6,1,-5,-4,-6,8,8,-7,-5,8,-1,-7,-1,3,-7,-9,3,4,10,3,-10,-7,4,-5,-10,-4,9,2,-6,-3,9,7,-10,2,-8,-8,-9,-5,7,-3,-2,10,10,3,-10,10,-8,3,-7,10,3,2,-10,-4,-8,8,4,3,-1,-4,5,-10,3,3,-2,3,-8,5,5,-7,-6,5,4,-8,6,-5,5,2,-1,-6,-7,-6,8,-4,-3,-6,-7,-1,-8,-5,-10,-3,-6,-3,-1,9,9,-2,-9,10,9,-2,-6,7,-1,-8,3,-6,-10,7,7,9,3,7,-10,-5,4,7,-10,5,7,4,9,-10,-8,-10,4,5,5,-1,-10,5,-4,5,9,5,7,7,-9,5,-3,-4,-8,-4,10,9,-10,3,9,7,-10,-3,4,-3,6,-10,-6,-5,5,9,-3,-7,-3,8,-10,7,9,-9,9,-6,3,-3,2,5,-5,5,3,2,4,-7,5,8,-5,7,-10,-10,-10,-2,-10,2,-1,3,10,-7,5,3,-9,6,-8,7,-7,-1,-9,9,-9,-5,1,4,5,-10,-7,-2]], dtype = "int8")#candidate|2245|(2, 1440)|const|int8
call_2244 = relay.TupleGetItem(func_599_call(relay.reshape(const_2245.astype('int8'), [16, 15, 12]), relay.reshape(const_2245.astype('int8'), [16, 15, 12]), relay.reshape(call_2242.astype('float64'), [20,]), ), 1)
call_2246 = relay.TupleGetItem(func_603_call(relay.reshape(const_2245.astype('int8'), [16, 15, 12]), relay.reshape(const_2245.astype('int8'), [16, 15, 12]), relay.reshape(call_2242.astype('float64'), [20,]), ), 1)
uop_2247 = relay.atan(call_2244.astype('float32')) # shape=(16, 15, 12)
uop_2249 = relay.atan(call_2246.astype('float32')) # shape=(16, 15, 12)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2253 = relay.TupleGetItem(func_1716_call(), 0)
call_2254 = relay.TupleGetItem(func_1717_call(), 0)
func_1613_call = mod.get_global_var('func_1613')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_2259 = relay.TupleGetItem(func_1613_call(), 0)
call_2260 = relay.TupleGetItem(func_1615_call(), 0)
var_2282 = relay.var("var_2282", dtype = "float32", shape = (16, 15, 12))#candidate|2282|(16, 15, 12)|var|float32
bop_2283 = relay.mod(uop_2247.astype('float32'), relay.reshape(var_2282.astype('float32'), relay.shape_of(uop_2247))) # shape=(16, 15, 12)
bop_2286 = relay.mod(uop_2249.astype('float32'), relay.reshape(var_2282.astype('float32'), relay.shape_of(uop_2249))) # shape=(16, 15, 12)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_2287 = relay.TupleGetItem(func_1716_call(), 0)
call_2288 = relay.TupleGetItem(func_1717_call(), 0)
bop_2290 = relay.left_shift(bop_2283.astype('int64'), relay.reshape(call_2244.astype('int64'), relay.shape_of(bop_2283))) # shape=(16, 15, 12)
bop_2293 = relay.left_shift(bop_2286.astype('int64'), relay.reshape(call_2246.astype('int64'), relay.shape_of(bop_2286))) # shape=(16, 15, 12)
output = relay.Tuple([call_2242,const_2245,call_2253,call_2259,call_2287,bop_2290,])
output2 = relay.Tuple([call_2243,const_2245,call_2254,call_2260,call_2288,bop_2293,])
func_2294 = relay.Function([var_2282,], output)
mod['func_2294'] = func_2294
mod = relay.transform.InferType()(mod)
var_2295 = relay.var("var_2295", dtype = "float32", shape = (16, 15, 12))#candidate|2295|(16, 15, 12)|var|float32
output = func_2294(var_2295)
func_2296 = relay.Function([var_2295], output)
mutated_mod['func_2296'] = func_2296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2073_call = mutated_mod.get_global_var('func_2073')
call_2369 = func_2072_call()
call_2370 = func_2072_call()
output = call_2369
output2 = call_2370
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
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2385 = func_2238_call()
call_2386 = func_2238_call()
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_2387 = func_2377_call()
call_2388 = func_2377_call()
func_2142_call = mod.get_global_var('func_2142')
func_2144_call = mutated_mod.get_global_var('func_2144')
call_2395 = relay.TupleGetItem(func_2142_call(relay.reshape(call_2387.astype('float32'), [10, 10, 2])), 0)
call_2396 = relay.TupleGetItem(func_2144_call(relay.reshape(call_2387.astype('float32'), [10, 10, 2])), 0)
func_1529_call = mod.get_global_var('func_1529')
func_1532_call = mutated_mod.get_global_var('func_1532')
const_2398 = relay.const([[1.546597],[-9.815230],[8.104854],[6.164753],[7.668984],[7.246028],[-1.405108],[-8.744965],[6.863882],[-2.221195],[-0.196158],[7.150942],[9.364065],[-8.116035],[6.774192],[-7.291833],[-4.765898],[9.193987],[-6.273555],[-3.169232],[6.309182],[7.784889],[9.237446],[9.869602],[0.455907],[-7.265861],[8.701595],[-6.674901],[-7.164535],[-8.031398],[7.469905],[6.168033],[5.921542],[2.999449],[1.951102],[7.402827],[-9.076463],[-3.947954],[5.435223],[-1.440504],[4.616661],[-0.631507],[8.652081],[6.751736],[-1.238470],[9.151297],[6.497923],[8.163791],[9.189307],[-3.291521],[3.974539],[2.386839],[-5.392986],[2.035245],[-0.724052],[-3.706948],[-2.130450],[-7.961923],[-0.382813],[-6.997051],[-8.107393],[-5.201131],[-7.959487],[-4.171654],[-7.069485],[-6.648223],[1.209753],[7.353139],[5.025561],[3.517041],[5.116555],[3.880016],[-4.277328],[1.907011],[-6.234642],[7.318423],[0.643268],[-5.616448],[-8.766719],[8.601184],[6.763146],[-6.770997],[6.686752],[-4.222476],[-7.696001],[-9.496394],[6.584049],[-5.467401],[-9.386560],[-0.936049],[1.710427],[2.095859],[7.020805],[-3.190483],[-2.436712],[7.779190],[7.202499],[-0.879518],[3.043050],[7.379091],[-3.733544],[8.598477],[2.386868],[-4.578356],[5.138278],[-5.872324],[-9.227722],[8.574921],[6.461107],[7.718804],[8.779690],[0.120234],[-1.415581],[-2.061161],[-3.858181],[-7.353724],[3.823554],[8.992791],[1.749762],[-5.807750],[-9.673314],[0.432145],[-3.276665],[0.913569],[-3.982349],[-3.256373],[5.746210],[-6.766730],[3.186036],[6.898879],[-3.918067],[2.129088],[-3.381123],[-1.270807],[-0.864906],[-0.680496],[-7.412247],[8.405453],[7.950840],[-5.997989],[-3.613671],[1.317562],[9.741352],[2.590001],[-0.289633],[-5.253628],[-7.350758],[5.400662],[-2.383966],[-6.213813],[-8.741204],[-7.286356],[-9.360879],[-8.206667],[-6.268776],[4.268744],[5.017635],[-5.836243],[-1.486091],[6.854003],[-6.510039],[5.259682],[4.355869],[1.405387],[1.998878],[-7.135316],[9.472366],[-2.216033],[0.213471],[6.058576],[2.425066],[-3.820977],[5.898654],[1.123007],[-7.488600],[1.171697],[2.364242],[-6.434784],[9.857636],[-5.612814],[9.375192],[-8.941232],[9.286578],[9.420259],[7.138091],[-1.368528],[9.649250],[5.825336],[4.709954],[8.365217],[-3.038297],[0.590945],[2.895797],[-1.782056],[0.693904],[4.637510],[-7.144764],[6.088848],[-1.452020],[-1.670196],[1.605209],[0.802063],[9.059611],[-9.518996],[7.897567],[-9.881879],[-3.636000],[4.894030],[4.793854],[-0.079678],[7.912160],[-4.986397],[8.636958],[9.694988],[-8.465301],[-2.684566],[0.328871],[-7.813478],[-3.627971],[8.908722],[-9.098243],[4.936336],[7.753042],[4.616707],[9.175973]], dtype = "float32")#candidate|2398|(225, 1)|const|float32
call_2397 = relay.TupleGetItem(func_1529_call(relay.reshape(const_2398.astype('float32'), [5, 15, 3])), 0)
call_2399 = relay.TupleGetItem(func_1532_call(relay.reshape(const_2398.astype('float32'), [5, 15, 3])), 0)
output = relay.Tuple([call_2385,call_2387,call_2395,call_2397,const_2398,])
output2 = relay.Tuple([call_2386,call_2388,call_2396,call_2399,const_2398,])
func_2402 = relay.Function([], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
mutated_mod['func_2402'] = func_2402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mutated_mod.get_global_var('func_2402')
call_2403 = func_2402_call()
output = call_2403
func_2404 = relay.Function([], output)
mutated_mod['func_2404'] = func_2404
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2178_call = mod.get_global_var('func_2178')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_2421 = func_2178_call()
call_2422 = func_2178_call()
var_2425 = relay.var("var_2425", dtype = "float32", shape = (10, 10, 2))#candidate|2425|(10, 10, 2)|var|float32
bop_2426 = relay.minimum(call_2421.astype('float64'), relay.reshape(var_2425.astype('float64'), relay.shape_of(call_2421))) # shape=(10, 10, 2)
bop_2429 = relay.minimum(call_2422.astype('float64'), relay.reshape(var_2425.astype('float64'), relay.shape_of(call_2422))) # shape=(10, 10, 2)
func_2294_call = mod.get_global_var('func_2294')
func_2296_call = mutated_mod.get_global_var('func_2296')
var_2456 = relay.var("var_2456", dtype = "float32", shape = (2880,))#candidate|2456|(2880,)|var|float32
call_2455 = relay.TupleGetItem(func_2294_call(relay.reshape(var_2456.astype('float32'), [16, 15, 12])), 4)
call_2457 = relay.TupleGetItem(func_2296_call(relay.reshape(var_2456.astype('float32'), [16, 15, 12])), 4)
func_599_call = mod.get_global_var('func_599')
func_603_call = mutated_mod.get_global_var('func_603')
var_2459 = relay.var("var_2459", dtype = "float64", shape = (20,))#candidate|2459|(20,)|var|float64
call_2458 = relay.TupleGetItem(func_599_call(relay.reshape(var_2456.astype('int8'), [16, 15, 12]), relay.reshape(var_2456.astype('int8'), [16, 15, 12]), relay.reshape(var_2459.astype('float64'), [20,]), ), 3)
call_2460 = relay.TupleGetItem(func_603_call(relay.reshape(var_2456.astype('int8'), [16, 15, 12]), relay.reshape(var_2456.astype('int8'), [16, 15, 12]), relay.reshape(var_2459.astype('float64'), [20,]), ), 3)
output = relay.Tuple([bop_2426,call_2455,var_2456,call_2458,var_2459,])
output2 = relay.Tuple([bop_2429,call_2457,var_2456,call_2460,var_2459,])
func_2463 = relay.Function([var_2425,var_2456,var_2459,], output)
mod['func_2463'] = func_2463
mod = relay.transform.InferType()(mod)
var_2464 = relay.var("var_2464", dtype = "float32", shape = (10, 10, 2))#candidate|2464|(10, 10, 2)|var|float32
var_2465 = relay.var("var_2465", dtype = "float32", shape = (2880,))#candidate|2465|(2880,)|var|float32
var_2466 = relay.var("var_2466", dtype = "float64", shape = (20,))#candidate|2466|(20,)|var|float64
output = func_2463(var_2464,var_2465,var_2466,)
func_2467 = relay.Function([var_2464,var_2465,var_2466,], output)
mutated_mod['func_2467'] = func_2467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_2492 = func_2377_call()
call_2493 = func_2377_call()
output = call_2492
output2 = call_2493
func_2506 = relay.Function([], output)
mod['func_2506'] = func_2506
mod = relay.transform.InferType()(mod)
mutated_mod['func_2506'] = func_2506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2506_call = mutated_mod.get_global_var('func_2506')
call_2507 = func_2506_call()
output = call_2507
func_2508 = relay.Function([], output)
mutated_mod['func_2508'] = func_2508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1613_call = mod.get_global_var('func_1613')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_2542 = relay.TupleGetItem(func_1613_call(), 0)
call_2543 = relay.TupleGetItem(func_1615_call(), 0)
func_2072_call = mod.get_global_var('func_2072')
func_2073_call = mutated_mod.get_global_var('func_2073')
call_2550 = func_2072_call()
call_2551 = func_2072_call()
output = relay.Tuple([call_2542,call_2550,])
output2 = relay.Tuple([call_2543,call_2551,])
func_2564 = relay.Function([], output)
mod['func_2564'] = func_2564
mod = relay.transform.InferType()(mod)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2565 = func_2564_call()
output = call_2565
func_2566 = relay.Function([], output)
mutated_mod['func_2566'] = func_2566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1833_call = mod.get_global_var('func_1833')
func_1834_call = mutated_mod.get_global_var('func_1834')
call_2579 = relay.TupleGetItem(func_1833_call(), 0)
call_2580 = relay.TupleGetItem(func_1834_call(), 0)
func_1321_call = mod.get_global_var('func_1321')
func_1322_call = mutated_mod.get_global_var('func_1322')
call_2585 = relay.TupleGetItem(func_1321_call(), 2)
call_2586 = relay.TupleGetItem(func_1322_call(), 2)
output = relay.Tuple([call_2579,call_2585,])
output2 = relay.Tuple([call_2580,call_2586,])
func_2590 = relay.Function([], output)
mod['func_2590'] = func_2590
mod = relay.transform.InferType()(mod)
mutated_mod['func_2590'] = func_2590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2590_call = mutated_mod.get_global_var('func_2590')
call_2591 = func_2590_call()
output = call_2591
func_2592 = relay.Function([], output)
mutated_mod['func_2592'] = func_2592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2649 = func_2238_call()
call_2650 = func_2238_call()
func_599_call = mod.get_global_var('func_599')
func_603_call = mutated_mod.get_global_var('func_603')
const_2665 = relay.const([-6,-3,-1,-7,6,-8,1,5,-9,6,9,-3,4,6,-8,10,-8,-1,9,4,3,8,-9,6,3,-7,-3,9,-4,9,-5,-8,-9,4,6,-7,-1,4,7,-9,5,-7,6,-6,-2,-2,3,10,8,1,-1,6,-3,-5,2,5,7,8,7,-4,8,-5,-8,2,-6,-2,1,-2,-10,-5,10,2,1,3,-3,-6,-4,3,-4,8,7,-1,-9,3,10,2,9,7,3,9,-6,-10,-5,-2,7,1,1,-4,-4,10,6,-4,-7,6,-3,-9,-9,-1,1,3,5,-3,5,7,-6,-5,-10,-1,2,-8,-2,3,-3,6,-8,-1,3,9,3,9,-2,6,-3,-8,2,-7,-10,-8,7,-8,-2,-7,-5,5,2,-1,-8,6,-2,6,10,-10,6,-5,3,7,4,-10,-4,-1,9,-3,-9,-10,-5,6,-2,8,-6,10,-8,-5,-4,-5,2,-5,10,-1,8,1,-8,9,-5,5,-1,1,5,-4,-4,7,9,-8,1,9,9,-3,8,4,-8,-7,7,10,5,-10,5,5,-9,-4,-2,-10,-4,9,-4,7,5,2,-3,3,8,-9,1,8,8,-2,4,5,-4,2,-9,-1,3,6,8,4,-3,9,-8,7,1,-6,1,5,-6,-3,-5,9,10,4,5,1,2,3,1,5,9,-6,-5,-4,-7,-5,-3,-2,10,-8,5,-2,-3,10,6,3,9,4,2,6,-6,4,7,-2,-2,-3,-2,-8,1,9,3,3,-3,9,-6,5,-8,-3,4,4,-8,7,-4,-6,-4,4,-9,1,-5,-9,5,-5,4,-10,5,-6,-2,2,-9,3,-5,3,4,-6,-4,2,-9,-6,6,1,1,4,-2,1,7,7,1,-4,3,5,-4,-1,-1,6,-3,9,-6,-9,-1,2,-6,-10,8,-3,-5,-2,-3,-4,10,-4,-8,-8,7,-5,-8,6,5,-1,9,5,10,5,-2,10,2,4,-8,-6,-10,3,7,1,5,-6,8,10,-1,-3,-5,-5,-8,9,-1,-1,6,-10,3,-7,-5,-5,-6,-1,2,-8,-7,-6,-1,-3,9,-5,9,-10,-9,3,1,9,4,2,3,7,-4,9,7,2,-5,3,-4,-6,-1,9,6,-7,7,8,-3,2,-7,5,-10,-2,-3,8,-7,10,-3,9,-4,-10,8,-1,-3,10,-3,-4,1,-9,-10,-2,3,-4,-9,-6,9,-6,-5,10,9,8,5,6,-5,-8,5,-1,-2,-5,-7,-5,-10,-7,-5,3,-7,7,-2,-7,1,-1,7,-5,6,-9,-2,3,-5,-6,-9,6,9,-9,-8,7,4,-8,-7,-2,-4,8,-5,-7,-3,-3,-2,-8,2,-4,-4,2,9,10,2,1,-5,1,1,-2,-2,7,-2,7,-10,8,1,5,1,-6,-9,10,-7,4,10,-2,-9,-6,-4,6,-3,-10,-6,4,10,2,-8,-1,-3,3,-9,8,6,10,7,3,-2,-6,-6,6,2,-5,-8,5,3,9,-5,-9,-8,-8,-5,-9,-2,5,-7,5,-9,-10,-9,10,-5,4,-5,8,4,-10,-8,7,-4,-9,-5,2,7,1,-9,9,-2,-3,-8,10,-8,2,-1,-6,-3,-6,1,2,-2,-7,-4,4,-1,-10,-7,-2,3,10,5,9,-3,8,-4,6,-1,-4,1,-2,-4,-1,5,5,1,9,5,6,4,-4,2,4,-2,10,-6,-4,-5,1,-2,7,6,-9,-6,7,-9,-8,-10,6,-1,-5,-9,7,-6,5,7,-1,-7,-3,5,3,-10,5,-3,4,-7,1,8,1,8,-3,-7,-9,-5,7,2,-4,-1,4,7,-6,-7,-2,6,-8,-9,-1,-3,1,3,-8,10,-9,10,-4,3,3,8,-2,9,9,9,4,-2,-2,5,-2,-1,-5,-6,9,-1,-9,8,-3,1,6,-4,4,7,1,-7,6,-3,10,-2,-9,1,-1,-9,-7,8,2,6,-8,-1,5,-3,7,-4,5,4,-8,-4,-6,-3,3,8,5,-1,-7,3,2,2,2,-4,3,-5,-7,-8,-1,-7,4,10,-9,4,5,7,3,-7,-9,-4,-1,1,-7,2,-4,4,6,9,7,3,-1,1,4,-9,-1,3,-3,1,-7,-9,1,1,9,5,1,2,-10,6,-3,5,9,7,6,3,10,-6,-7,-8,-7,6,1,-2,1,5,2,-9,9,4,-3,-1,-2,5,4,-8,8,-8,10,-2,-7,-6,-6,-3,-2,-10,-5,9,8,7,-7,4,8,4,4,-2,2,2,-4,3,-2,-2,-6,4,-5,7,-7,9,2,7,9,7,-9,9,5,-1,5,-6,6,-6,-3,5,5,-9,-7,-3,6,-2,-10,-10,3,4,5,-10,9,2,-10,-4,-2,1,1,-10,7,-4,10,-4,5,2,5,1,-9,-8,3,-7,-6,6,4,4,5,8,2,-10,-9,7,6,10,4,-8,1,-1,4,4,-1,-9,8,4,1,-5,6,-4,1,-10,3,9,3,-1,-5,-5,5,3,-3,-1,10,-5,-9,1,-3,4,-10,10,-3,2,-7,-6,-3,4,-7,10,-3,6,-4,-4,9,-4,1,4,-4,3,3,4,10,4,4,-5,-9,-1,-9,1,-2,-8,-9,-6,7,6,9,-8,5,6,-5,8,-3,8,-3,1,4,-8,-2,-7,4,-10,1,-1,9,-8,10,8,-7,7,-5,-7,8,3,-2,10,4,-10,-8,-5,-10,-1,1,6,-4,-7,-3,-10,-10,2,3,-7,-4,6,-7,8,4,-8,9,-2,-10,3,-3,-8,-6,-4,-4,8,5,-9,2,10,9,4,5,-2,-7,10,-10,5,-1,-4,8,-3,3,7,-1,5,6,-7,-5,8,8,2,-8,-3,-5,-2,-7,8,-6,7,-4,7,-2,-3,-7,-9,-8,-2,-9,5,-2,-7,-3,8,1,-7,10,7,10,10,-10,2,-3,4,9,-6,-6,9,9,9,5,-5,1,10,1,-1,-9,8,-7,-4,4,7,-2,-9,6,-10,-7,-9,-8,-2,-6,-9,3,-9,-2,9,10,5,-4,2,4,2,-9,-10,7,6,-4,-10,-6,9,9,-3,-6,4,7,-10,10,-4,1,5,-5,-1,10,6,-10,4,-3,-2,-7,8,2,7,-8,-10,3,8,8,9,-1,-2,9,2,-4,2,-1,-5,8,3,-3,4,-10,-5,2,-6,8,7,5,1,4,-1,4,5,10,-8,3,-8,-6,1,7,-2,7,-2,9,-4,-9,-9,4,6,4,-8,6,1,-1,2,4,-2,-5,5,-10,-8,-5,3,-3,-3,1,-5,7,10,2,5,8,-7,4,9,-3,2,-6,-9,-3,5,6,-2,-7,1,6,5,5,-9,6,-4,6,10,2,10,-2,9,4,10,-6,3,1,8,-10,7,-6,6,7,-6,5,-4,9,-6,-5,-6,-1,4,7,-8,-2,4,5,2,7,-1,-1,1,8,-5,-6,-3,2,-9,-1,5,-3,1,-8,-2,-10,7,-9,1,8,10,9,-10,-3,9,7,9,-2,10,5,4,6,-7,2,10,-6,-3,-6,-9,4,-6,1,-5,-10,-2,6,2,-7,-4,-9,-8,-7,-3,4,5,-7,2,-8,2,9,-3,-9,-6,-4,-7,7,9,6,10,-1,9,5,7,-6,1,2,-2,-9,-1,-1,7,4,3,-5,2,-7,5,2,-7,-10,6,2,-4,8,-5,4,8,-7,9,-3,9,4,4,-5,-6,9,8,-2,2,10,1,-9,-3,10,-10,5,-7,-1,-6,-3,-3,4,4,8,10,-5,-1,1,-3,-9,8,-2,4,-7,2,-1,-2,10,3,-6,-5,5,7,3,-7,-5,-6,-9,10,9,5,9,-4,-5,-9,1,2,-2,-10,-9,5,1,10,-2,-5,4,-10,9,-4,-1,5,-6,8,6,-3,4,-8,1,-6,-8,-3,-4,7,-5,6,-3,9,-8,9,4,8,2,-4,3,6,-2,-6,-10,-10,4,-2,-8,6,10,9,-7,-2,2,2,6,9,-6,6,7,-2,1,8,7,-5,-9,-10,9,7,-8,9,6,-3,2,-10,-5,-4,6,-6,-7,-1,5,-5,3,-8,-1,-4,4,1,9,6,2,10,1,-3,9,7,5,-2,1,1,6,9,5,5,1,-5,3,-3,5,5,9,-10,1,5,2,6,-3,8,-6,9,-6,10,-4,-4,-8,5,-8,-4,-8,4,6,8,6,-7,-8,-10,3,-4,5,-7,6,2,6,-6,6,-4,8,4,-7,8,7,2,10,-8,3,-9,5,4,9,6,9,-10,2,-3,-4,6,9,-1,1,5,5,2,7,-3,-7,-2,9,-3,7,-9,7,2,3,-4,-5,8,-4,1,-10,6,5,4,-3,6,5,10,-3,7,-6,-2,-3,-10,-3,-6,7,-10,1,10,-5,3,4,-1,4,4,-2,-10,7,9,2,2,-9,-4,8,-6,10,2,-3,-2,-2,8,3,8,9,-9,-3,10,5,2,-8,8,-8,-4,5,7,-4,-3,2,-6,-7,1,8,-1,5,-10,-4,5,-1,10,-6,-5,-1,-9,8,-3,2,4,-5,-5,-10,7,5,5,-2,-2,-3,9,3,-8,-5,5,-5,9,6,2,1,2,-1,10,4,-2,-6,3,-10,10,2,-3,6,6,-6,-10,8,-2,10,2,3,3,6,-1,-6,10,-8,-4,-2,6,1,-6,-9,9,10,5,7,5,5,10,8,-1,4,1,-10,-6,3,1,8,-1,-3,-4,-6,6,4,7,7,-8,-5,-6,6,-5,4,10,8,-2,10,3,-4,1,8,-10,8,-5,7,-10,-5,-1,-1,-5,-6,1,-5,-6,-5,7,-7,-10,4,-9,-9,3,6,-7,7,-5,8,-1,-10,2,-3,1,-5,-4,6,-10,-4,1,9,8,-9,-10,-1,-2,7,-8,-4,-2,-10,9,-2,3,4,-8,3,2,1,10,5,2,-7,-6,-1,-1,-5,-9,1,-6,9,1,-2,-5,-7,4,7,5,6,5,10,-10,-6,3,-4,-4,5,-6,-8,-9,-6,-6,8,-8,-3,-4,1,-7,5,-6,-8,-4,8,9,9,-9,-10,-9,-6,-5,-2,-3,4,-9,1,10,8,2,3,1,9,8,-7,-8,-4,4,-1,-8,-9,4,4,9,7,9,-3,4,2,-1,-9,-4,9,8,6,-5,-4,-5,2,-10,5,2,2,2,-6,-5,-2,-9,-6,3,4,9,6,6,-7,-8,8,10,6,5,5,-8,-8,7,7,-8,-7,-10,-10,-10,3,-9,10,4,-3,7,-1,-4,3,5,-3,-2,1,-1,6,-7,-1,-3,-8,-6,-6,-9,-9,7,6,1,-6,-10,-5,-9,-4,2,-3,-6,-2,1,5,-6,-5,-6,7,-2,2,-2,-3,-8,7,2,-6,2,3,7,-5,2,-8,-3,-10,7,-7,1,-10,-8,-10,9,-1,6,-4,3,8,9,6,10,-5,9,8,3,-8,6,-1,6,6,7,-4,1,-6,9,-10,-9,8,8,-6,5,-2,-4,8,7,3,-5,-4,1,7,-3,9,-6,8,2,-7,-1,-9,-1,6,-10,2,6,-2,-8,-6,-7,-1,-3,-7,6,-3,-2,-10,7,3,-5,-5,-2,7,-7,1,8,-7,2,8,-9,-2,3,-3,10,-2,-2,-5,5,6,-2,7,8,5,-1,7,5,-10,3,-3,-1,9,1,10,5,9,3,-9,2,-3,6,3,-1,-10,-8,9,-7,3,-4,3,10,-7,9,-4,-2,6,-8,1,-1,4,-5,9,3,9,8,7,5,-9,-1,-7,-1,-3,1,-8,7,4,-7,2,-6,9,5,9,1,-8,4,-9,8,6,6,-6,6,-4,2,4,9,1,3,-5,2,9,9,-1,-10,10,8,10,5,-8,-10,-8,-10,-4,-1,-7,4,-6,-4,2,3,1,-10,-9,2,6,2,2,3,2,5,-4,5,-4,9,2,-9,-7,-3,8,2,1,7,3,-9,3,-4,5,-9,10,-4,-3,-7,-6,5,-10,-7,10,-4,4,-1,7,6,-7,-8,4,-9,-9,-7,9,-8,-8,9,10,2,5,3,-9,2,3,-2,4,-5,-8,-7,-2,-5,9,-8,-5,5,4,-2,4,-10,5,-5,5,-3,10,-1,6,-3,-10,-6,-3,-9,-6,3,-6,-8,-7,4,-2,-5,9,-7,2,8,2,10,-4,2,9,-9,-8,-8,9,-7,8,-3,7,-10,9,4,-3,-7,-5,-4,-4,-1,-1,7,10,-10,3,-5,-5,-1,4,-8,-2,-3,-3,1,-1,10,-1,1,9,10,-7,6,2,6,5,-3,8,3,-3,7,-7,8,-3,9,-10,-8,8,1,-1,3,1,-4,2,-10,-2,-10,5,-8,9,-2,8,8,-4,-3,-5,3,-4,7,-4,4,-6,-6,-4,-9,2,2,9,-8,-10,-10,-9,3,9,3,8,1,2,5,2,1,-5,-5,-4,9,-4,-8,-9,-10,10,-4,-1,-2,-2,10,-1,9,-3,-2,7,-2,-10,6,1,10,9,10,6,-2,-9,2,5,-7,6,-7,1,-6,8,-10,9,-10,3,8,-4,-8,7,4,-3,-10,2,-4,5,-4,3,3,6,-2,-5,-8,3,1,-8,-9,8,2,7,3,-5,8,-4,3,4,9,-6,-10,3,-10,-8,3,-10,-8,-8,-10,9,-4,9,-5,3,-4,-10,-9,-6,5,-7,10,3,4,-8,-6,-10,-1,10,-4,9,1,10,4,6,-10,10,-10,-7,-6,-9,-3,5,-10,10,-5,9,10,-5,-7,-6,5,8,-10,-10,-3,9,9,-2,6,-2,2,-8,-3,9,-5,1,-2,5,-6,-10,-3,-5,-2,1,8,2,5,2,-4,-9,5,-9,9,-3,-9,3,10,6,2,2,1,10,4,3,3,7,2,-9,9,5,2,10,6,6,3,8,3,-9,1,5,6,4,-7,10,-4,4,4,10,9,-8,5,8,5,7,3,-10,3,8,8,5,-4,-5,-4,8,2,-8,3,7,5,-6,7,7,1,-1,5,8,-7,-8,2,4,4,-3,8,-5,-5,1,-6,-1,4,-5,-9,8,9,-7,-2,3,3,-2,-7,5,-7,-3,5,-1,7,7,10,4,-1,-8,-1,10,-10,-6,9,-10,-10,-3,-8,-5,10,-3,-9,-2,7,5,5,-4,8,-2,5,-3,-5,-1,1,-10,-10,-5,-1,1,-7,9,-4,6,5,6,8,-5,8,-7,-4,1,-3,4,3,3,-6,3,5,9,-5,-2,-8,7,-4,6,5,-1,6,-2,3,-1,10,-8,-1,-7,-3,1,-7,-7,7,9,3,-10,-7,7,10,10,2,-6,-2,1,-3,7,3,1,9,9,1,-10,2,10,-7,-5,-6,-4,-6,-6,-7,1,10,7,-3,3,8,4,-3,5,5,-3,-10,1,-1,-7,3,8,9,5,4,9,1,3,10,-6,-7,-7,-5,3,7,-4,-5,4,-8,9,4,3,3,-9,-5,9,-5,6,-5,6,8,-10,2,8,-4,-3,7,4,-3,5,10,-7,8,-5,-4,-5,-2,-3,1,-6,10,-3,-7,-9,2,8,7,8,-1,-10,-3,5,-10,-10,4,7,-7,-3,9,-5,-7,4,-8,-1,3,-6,-6,4,1,-10,1,-9], dtype = "int8")#candidate|2665|(2880,)|const|int8
call_2664 = relay.TupleGetItem(func_599_call(relay.reshape(const_2665.astype('int8'), [16, 15, 12]), relay.reshape(const_2665.astype('int8'), [16, 15, 12]), relay.reshape(call_2649.astype('float64'), [20,]), ), 2)
call_2666 = relay.TupleGetItem(func_603_call(relay.reshape(const_2665.astype('int8'), [16, 15, 12]), relay.reshape(const_2665.astype('int8'), [16, 15, 12]), relay.reshape(call_2649.astype('float64'), [20,]), ), 2)
output = relay.Tuple([call_2649,call_2664,const_2665,])
output2 = relay.Tuple([call_2650,call_2666,const_2665,])
func_2676 = relay.Function([], output)
mod['func_2676'] = func_2676
mod = relay.transform.InferType()(mod)
mutated_mod['func_2676'] = func_2676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2676_call = mutated_mod.get_global_var('func_2676')
call_2677 = func_2676_call()
output = call_2677
func_2678 = relay.Function([], output)
mutated_mod['func_2678'] = func_2678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_2709 = relay.TupleGetItem(func_2064_call(), 1)
call_2710 = relay.TupleGetItem(func_2066_call(), 1)
uop_2711 = relay.exp(call_2709.astype('float64')) # shape=(98, 4)
uop_2713 = relay.exp(call_2710.astype('float64')) # shape=(98, 4)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2717 = func_2238_call()
call_2718 = func_2238_call()
output = relay.Tuple([uop_2711,call_2717,])
output2 = relay.Tuple([uop_2713,call_2718,])
func_2735 = relay.Function([], output)
mod['func_2735'] = func_2735
mod = relay.transform.InferType()(mod)
output = func_2735()
func_2736 = relay.Function([], output)
mutated_mod['func_2736'] = func_2736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_2759 = func_1597_call()
call_2760 = func_1597_call()
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_2772 = func_2377_call()
call_2773 = func_2377_call()
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
const_2790 = relay.const([5.258661,-7.413295,-1.166489,0.614346,-9.866742,5.597234,-8.270860,-5.093381,-3.510056,-7.953542,8.255042,2.998404,5.032868,-4.276009,-4.762474,-8.044671,8.354133,-2.922291,-2.330550,9.372607], dtype = "float64")#candidate|2790|(20,)|const|float64
call_2789 = relay.TupleGetItem(func_276_call(relay.reshape(const_2790.astype('float64'), [10, 1, 2])), 0)
call_2791 = relay.TupleGetItem(func_279_call(relay.reshape(const_2790.astype('float64'), [10, 1, 2])), 0)
func_2676_call = mod.get_global_var('func_2676')
func_2678_call = mutated_mod.get_global_var('func_2678')
call_2792 = relay.TupleGetItem(func_2676_call(), 2)
call_2793 = relay.TupleGetItem(func_2678_call(), 2)
const_2796 = relay.const([3,4,-10,1,2,-8,-4,10,-10,-6,9,-4,1,8,3,5,2,1,-10,3,2,8,-2,6,5,-4,7,3,-7,10,-3,-8,-6,-8,1,-10,-5,-1,-7,10,10,-8,3,-7,-4,-10,1,1,7,6,3,3,6,-4,10,7,-9,8,-8,-2,-3,-7,-2,-4,8,-9,5,8,7,-6,-7,8,8,7,3,6,4,10,4,5,3,-4,7,2,5,10,9,-9,3,2,-5,-4,2,5,8,-7,-5,9,-4,-3,-7,2,-10,-2,6,1,-2,10,-8,1,6,-7,10,2,-7,4,9,-1,-4,-4,-8,-2,9,-6,1,-5,9,8,5,5,7,7,3,5,-2,-10,5,1,-5,2,-8,3,-6,7,2,-5,-1,-3,10,-4,8,-1,5,6,2,-6,-5,-8,-9,-4,8,10,-2,4,2,4,-1,2,10,-7,-7,3,-1,3,-5,-1,-6,2,5,-2,5,8,3,-3,-7,5,1,-6,-8,-4,-7,6,5,3,-6,-8,3,9,3,10,2,6,3,8,2,-4,7,4,10,4,6,-10,-6,-6,-3,-3,-2,-8,2,6,-8,-4,-2,8,8,9,4,3,-10,-10,-5,-8,3,-2,4,8,-8,-10,1,-2,10,10,-3,-5,-2,-8,10,-4,3,-8,3,2,8,-10,10,5,5,5,8,3,-6,7,-6,-9,-8,-8,2,-2,10,9,-6,-9,2,1,3,-2,-2,7,3,-6,4,1,4,8,9,-3,4,6,-5,7,-10,8,-9,1,-10,2,3,-10,9,10,-5,-3,-4,-4,7,-6,10,10,-9,-3,9,3,-1,8,2,7,8,6,-10,-10,4,3,-2,-5,-5,-9,6,-6,-4,-6,-10,-4,3,-10,-2,10,-8,2,-6,-10,7,-5,9,9,-6,10,8,-6,-3,3,-9,-1,-8,7,-2,-6,6,4,-3,-1,-8,6,-2,-6,-9,10,2,2,-6,5,-8,1,-2,-1,5,-3,10,8,2,-7,-3,-6,10,-4,-1,-6,-9,4,1,-6,5,1,1,-9,1,3,-3,-10,8,-1,4,9,4,5,-7,4,-10,-1,-4,5,6,-1,6,-2,-5,5,-10,-3,8,-2,6,-10,8,-9,-2,8,-10,-7,-10,5,3,3,6,10,1,-10,-7,-5,-2,9,-9,-9,8,9,6,1,4,3,-9,6,6,-1,4,9,-10,-9,-5,-10,-4,-9,3,-10,-6,-8,9,-7,10,7,3,2,-4,6,7,4,-7,4,5,-8,6,-5,10,9,1,-5,-3,10,6,-1,-2,-6,10,-10,3,-5,3,-5,4,-4,1,-9,-6,4,-5,-7,-1,-7,-3,3,2,-5,10,2,6,-8,5,1,-6,-5,1,-9,3,1,-2,1,4,3,-8,7,10,10,3,-9,6,10,-4,-10,-7,-4,-9,5,5,-7,-10,6,2,-7,7,3,-10,3,-4,-4,7,-9,6,-10,-1,-3,-3,-3,5,9,-6,5,5,-3,-2,1,-6,6,6,3,2,10,-5,2,3,-1,-2,-8,-8,-8,-7,-10,1,4,-9,-5,-3,8,-8,-7,2,1,-8,-2,9,7,-1,8,2,-1,9,5,3,-9,4,3,7,1,-4,-2,-5,8,5,-9,-9,9,6,-1,7,-9,7,-8,-7,-8,2,-3,-8,-4,-8,3,1,9,-5,-6,10,7,9,-10,6,5,-9,-4,1,1,1,9,5,1,6,-6,5,4,9,-10,1,3,-6,-8,-7,6,-2,-9,-3,-10,-10,-7,-8,-10,-4,-3,8,6,5,10,-2,9,1,2,-2,3,9,-10,-3,-5,3,-4,6,-6,4,4,-10,2,4,-5,8,-10,-10,-3,1,9,-10,6,3,-6,5,2,4,9,8,4,-4,5,5,6,-8,1,-8,-3,-6,-5,-10,10,-1,-3,7,-6,-4,-6,9,-4,-8,6,-1,-6,-7,-1,10,-4,-2,-3,-6,9,-10,-8,8,-9,-8,-2,-1,7,-3,-8,10,5,8,-1,7,-4,-5,-9,6,-9,2,-3,-2,-2,9,-10,-1,-10,-3,3,1,10,-2,8,8,2,9,-2,10,-7,-5,7,-2,-6,8,-8,7,-4,8,6,-9,5,-8,8,2,-6,-2,4,1,-10,9,7,-5,-6,-5,8,-5,-2,9,-2,7,7,-2,-5,3,2,-5,-2,2,-5,4,-8,8,3,-2,-8,2,10,10,-7,-1,7,-7,-6,8,-3,7,-1,-3,-2,-9,4,8,7,9,1,10,6,6,6,7,8,3,9,-4,-1,-1,-6,10,7,5,9,-5,-5,-9,8,-2,-10,-6,1,9,-4,-10,1,2,-7,-5,6,-3,2,-4,10,7,-1,8,-2,7,-9,-4,4,8,7,-10,-3,6,7,-6,-5,8,5,-9,4,10,-10,-4,4,-8,5,-4,4,-4,9,9,-4,-10,-2,-5,-3,-2,3,1,-7,-6,8,-1,-9,5,-6,2,1,10,-10,-2,1,-8,-9,10,8,8,-10,-10,5,-9,-10,-10,10,4,6,3,-9,2,9,-6,9,-5,-5,10,-2,1,-7,-3,-3,-6,-3,4,1,-4,7,-1,3,7,-3,-8,-3,5,9,6,-4,-1,-5,-3,-1,1,4,-6,8,-9,-10,5,7,3,9,10,-6,-4,-5,9,1,-4,2,6,-3,2,-3,7,1,5,-1,-7,5,-8,-6,4,7,-6,8,-8,6,-4,-8,-8,1,1,10,9,-9,4,3,5,-8,8,3,-8,-7,10,5,6,-3,10,-7,9,-5,1,2,8,7,7,4,-8,8,-6,-8,-1,-3,4,-9,6,-5,1,-3,7,-7,-7,-10,1,5,-2,-2,-1,3,5,-8,3,-5,1,5,7,4,2,1,1,1,-8,-6,7,6,-9,-10,8,-1,5,-10,-8,8,-8,3,4,5,-6,3,-10,5,5,-6,-3,5,2,10,-10,2,-7,7,9,-5,5,-8,9,6,9,9,8,-9,7,-2,8,-5,9,8,6,-2,-3,5,4,-6,-5,4,-8,8,2,4,-4,-9,-3,-8,10,1,8,5,-9,-4,5,2,1,-9,-9,-7,4,-5,-10,-7,3,-4,-3,-5,-10,-1,-7,8,-4,-10,-4,8,-2,-4,-8,-5,-8,-1,7,-7,5,4,2,1,-1,-3,-8,2,5,-2,-6,3,-5,-4,2,-3,-1,10,-9,3,2,6,8,1,3,-8,2,2,6,2,-9,-5,-2,-6,-6,4,5,-7,9,8,-1,2,8,1,-1,-3,9,-3,-5,-3,-9,8,-8,-7,-4,10,3,-1,5,-8,6,-1,9,8,-6,-4,10,7,6,-5,-2,8,-7,10,-10,2,-10,-2,10,5,-3,-9,1,-2,-3,-9,-4,-2,-3,-6,-3,-8,-3,1,2,-7,7,9,3,6,10,3,-2,6,-9,10,-3,4,1,-9,-3,8,-4,7,8,-7,1,-4,-7,10,-5,8,1,3,-7,-4,1,-10,9,-6,3,5,1,6,-2,-4,9,6,-3,-3,-3,3,-9,1,-4,-4,8,10,-1,-9,-5,1,-6,5,5,-2,-6,-4,-1,4,-4,2,-10,-5,-1,3,9,1,8,-5,-7,-5,5,10,8,3,6,6,-10,-6,-5,-8,-2,10,-6,-5,5,7,-1,7,-3,-3,-8,5,-10,-10,10,1,-8,2,-7,8,-8,3,-4,-1,1,-7,3,-6,3,-9,-7,-4,3,-10,4,-6,4,4,-8,-6,10,-7,-5,7,-10,-2,-1,1,-4,-8,-10,3,-2,4,3,-8,-3,-8,-7,-8,-3,5,1,-10,8,5,10,3,-4,-1,-7,10,3,10,-4,10,-3,3,-10,10,1,-7,-1,5,7,4,7,6,3,2,6,-5,7,-2,-1,7,6,-4,-4,6,-7,7,-2,3,-9,-3,7,4,5,2,-6,1,1,-3,-6,-6,7,4,6,-7,4,-2,7,6,-1,2,-7,3,10,-3,-5,9,4,-3,1,-7,-9,6,6,10,2,7,6,-7,6,-1,1,-2,3,5,-5,-1,-3,2,10,-7,5,2,-3,-8,-9,9,8,2,7,9,10,-8,-8,-4,-6,3,-6,5,-1,10,1,-7,1,4,9,-3,3,3,4,10,-10,-1,7,6,8,-8,-5,2,6,-7,-7,-3,-2,2,4,5,-6,-10,4,-10,4,-3,-1,-7,1,2,-2,10,1,-9,-7,-9,-1,-5,7,-9,-1,7,1,1,-8,2,5,-4,-6,-1,7,6,-9,5,4,4,-10,9,9,-3,-10,8,7,-2,-7,5,-3,4,-2,7,-4,-3,-5,8,-2,-10,-4,-8,10,-5,2,-1,-1,-6,-1,-8,3,-3,-4,2,-10,8,9,-6,-7,6,-10,-4,-9,3,3,-6,3,-7,-10,2,-1,3,-10,9,-3,9,-9,4,3,-9,-9,7,6,-10,2,6,4,-3,10,2,-6,-7,-3,-4,-10,-7,10,2,7,-2,-6,2,8,4,9,3,8,2,-3,-10,-3,-4,10,-1,-8,5,3,-3,7,3,7,1,8,-9,-4,-5,-7,-10,-5,-3,5,-6,-7,3,8,10,-2,3,8,2,-2,-9,-4,-5,1,1,-7,-6,5,10,5,-9,5,-8,3,-5,7,-3,2,-9,9,10,-6,-2,-8,-6,-4,-4,6,-2,-4,-3,2,3,7,8,3,-2,6,1,6,-9,-10,-1,-6,7,-1,-10,-8,6,4,-1,-2,5,-5,-4,-4,3,-7,-2,9,-3,-10,5,6,5,-5,-9,7,7,-2,7,5,10,6,2,-1,-8,-8,1,4,5,10,8,-8,3,7,6,10,3,9,-3,-10,1,4,1,-8,9,10,5,-6,10,8,7,-5,6,-6,4,10,4,-9,-3,-1,5,4,9,-10,-3,-8,-6,1,-5,-1,-4,8,6,-3,4,-5,-5,-9,-7,7,7,2,-6,-3,1,4,6,3,7,3,10,-10,-7,1,-8,-3,4,6,10,3,-5,9,6,3,10,5,-6,-6,4,6,-8,6,-6,-9,4,-2,-8,-2,4,8,-5,-5,9,-1,-3,-6,-6,2,-7,-10,5,-1,4,-7,-1,4,1,-7,5,7,7,-8,8,-6,-2,-5,10,-10,-1,5,-4,-10,-2,-7,-8,-4,8,7,3,10,-2,2,2,8,-9,-7,-4,7,-7,3,-9,-10,3,2,3,-1,6,8,-5,3,-3,-8,1,-3,2,-4,4,-9,-1,3,2,10,-9,-7,-7,10,-1,7,6,10,5,-8,-8,-8,-7,-3,-4,8,-1,10,5,8,-10,10,4,-3,-4,1,-9,10,-7,4,6,-7,-9,7,-10,-2,9,-6,1,-5,4,6,-5,9,1,-5,7,4,-2,-10,5,1,-3,10,-10,-9,-10,-6,-1,-7,8,9,-8,1,-3,10,-2,-3,-2,7,7,6,10,4,-9,-4,-5,-2,6,-2,-4,-9,7,-1,5,1,-3,9,9,7,-4,-4,-5,-3,2,2,-10,-2,2,-4,-1,-9,1,10,-1,9,9,8,4,7,-9,-1,1,-3,-9,10,-5,-8,4,8,6,-5,-3,-9,6,-2,-6,-1,-8,-7,-5,-9,-3,7,-5,-7,4,-6,-4,-3,-2,5,-10,4,-3,7,8,-8,-4,-10,-10,2,10,-1,4,5,1,-7,-6,-10,-1,-7,-6,-10,10,9,-1,-1,10,5,6,-1,2,9,-8,7,10,6,10,4,10,-7,-6,-9,-10,10,6,4,-1,6,-4,7,-8,7,3,-8,-9,-5,3,9,10,-1,5,4,8,5,4,5,-9,2,6,-6,-4,7,-4,-1,10,-9,-7,8,5,-9,-5,3,-7,-5,-4,5,1,5,10,8,-10,-2,-1,4,4,-5,10,-5,2,7,1,5,-5,7,-8,5,1,-7,-10,8,-6,6,-10,2,-1,1,-2,5,-9,-5,7,-7,9,-1,-6,-4,-2,10,-1,6,-3,5,-5,5,3,3,9,-8,-5,-7,10,5,4,-5,-8,-7,2,-8,-4,-3,4,7,-7,4,-8,4,6,1,5,-3,1,-5,3,9,8,-6,-7,10,10,9,8,-5,3,2,-1,2,-6,2,10,-9,-3,-5,-8,8,10,5,9,10,-5,1,-9,8,9,7,3,-10,-8,9,-9,-5,2,-6,-9,4,-9,8,9,-3,5,-8,5,5,2,-1,-8,-1,-6,3,3,7,-4,2,-2,10,7,6,-5,-5,-4,9,3,-4,6,4,7,-3,-8,-4,2,-8,3,10,6,4,-4,-5,10,-7,9,8,-5,-6,-6,3,-6,6,8,5,3,-7,-2,-5,-2,-1,-6,-4,9,-5,-10,-4,1,6,-8,-5,-2,-10,-5,-1,9,-7,-10,-7,-2,-6,1,1,-10,3,-9,10,3,10,-5,6,-2,9,3,-10,6,-9,4,1,6,3,-6,-1,-3,8,1,-9,6,-4,4,6,-8,9,5,-7,5,8,-4,-2,-1,4,6,-4,1,-3,-2,5,4,-3,3,1,1,-1,10,4,4,5,9,-2,7,-7,4,8,-5,8,10,-10,-9,-8,4,10,7,-10,5,9,9,1,-8,-3,8,5,-9,1,-5,4,-8,-1,-2,-3,3,8,-8,7,-6,2,-10,-3,1,-6,10,10,-6,5,10,-4,-10,6,9,-7,-4,8,6,-2,5,7,-9,5,6,5,8,2,10,-9,3,-4,4,10,5,-1,1,-8,-3,-8,-1,-8,2,10,-9,-1,-4,9,10,10,-3,-8,8,-9,-6,-1,-9,9,-10,3,7,-2,-2,-1,-10,8,1,-10,-3,-2,-5,8,-4,7,-6,-3,-6,-6,-6,1,-7,9,-6,-8,7,7,-3,-8,-4,2,5,4,10,10,-4,-10,-1,-10,-10,-5,8,-1,-9,-9,3,-2,7,-2,6,1,-2,-1,-1,-9,9,8,-7,8,7,8,9,8,6,2,-1,-1,5,-7,3,7,-1,-9,3,4,-5,10,4,9,-8,-1,-6,-2,-4,-9,-7,1,3,-8,-5,8,7,-3,6,1,7,-2,4,-3,-5,9,1,9,8,-4,-2,-5,10,9,2,-1,2,1,7,8,10,-3,-7,-7,-4,8,-3,4,-2,1,-3,-4,-6,-2,-3,-7,8,-4,-6,10,1,-5,-2,8,-2,-10,3,-9,-9,4,-1,-4,4,-4,8,10,3,-4,4,8,2,8,-2,-4,8,-4,8,-8,8,3,-5,7,-10,-2,4,-8,-10,10,5,-6,2,2,7,-4,-9,1,4,1,-9,-6,-6,9,-3,9,-5,-1,-4,8,-10,-8,-3,-4,-9,1,-9,-10,1,3,10,-2,-7,-1,3,-2,-6,-3,-1,8,-3,7,5,-8,-9,-2,3,4,-6,-10,-6,3,5,3,-4,-6,-9,8,-10,-10,-7,8,6,-9,6,-3,-2,-6,-6,-2,7,5,1,-10,10,-2,2,-7,1,-1,5,-9,2,-5,4,7,5,9,-7,-7,-9,-4,-8,-7,6,5,-4,10,2,4,-3,9,-5,4,-7,9,-9,-5,5,-5,2,6,-8,9,4,-8,-4,-6,5,-1,10,-6,-6,-5,5,-3,2,10,-6,10,2,-8,4,7,2,2,9,-1,3,7,-6,2,10,7,-2,-7,-6,-5,6,2,10,-2,-5,6,-10,5,-3,-5,-10,-10,-3], dtype = "int8")#candidate|2796|(2880,)|const|int8
bop_2797 = relay.equal(call_2792.astype('bool'), relay.reshape(const_2796.astype('bool'), relay.shape_of(call_2792))) # shape=(2880,)
bop_2800 = relay.equal(call_2793.astype('bool'), relay.reshape(const_2796.astype('bool'), relay.shape_of(call_2793))) # shape=(2880,)
func_1925_call = mod.get_global_var('func_1925')
func_1928_call = mutated_mod.get_global_var('func_1928')
const_2812 = relay.const([0.617132,-1.399542,-4.776868,5.107705,-2.838206,3.181461,8.362947,3.832708,-8.889034,0.017784,3.823744,-9.635137,-6.910616,-5.752780,4.976115,-3.846934,4.669588,3.254739,-7.179138,-0.541007,-7.187247,1.338301,-1.445212,4.260458,-8.410775,-5.194601,3.298297,1.828480,9.078469,1.629256,7.059606,0.212412,-5.055390,-5.839949,-9.359363,8.118193,-6.017885,-6.227573,-5.756836,-2.672189,-0.664839,-1.242159,6.533637,3.016067,-2.286011,6.774995,-1.753024,-3.937947,-2.557927,9.339028,1.134506,6.566365,-2.183039,1.010611,-2.519492,2.808622,-7.143530,-5.115382,6.116749,-0.358057,-4.867248,8.077541,-2.868578,6.315472,-2.925095,7.514414,-9.429029,0.657306,-8.269770,6.672373,-7.642389,-3.507775,-8.097451,-7.446372,-7.953918,1.531240,8.862375,-4.850078,-3.523722,-0.053946,-1.477085,4.315749,-4.597756,8.333873,4.952542,6.422536,8.489901,-2.380458,-1.927943,3.996063,7.336215,4.318969,4.400858,-5.702208,-3.029013,-6.768274,0.116586,8.414294,3.295925,-7.664910,5.801700,-2.092521,3.530774,-1.240954,-2.304280,3.741820,7.553214,-4.332562,-6.935986,-1.783552,6.607262,0.116651,-3.496834,-1.056117,-0.104558,-5.460146,9.863634,-4.274497,3.356251,-6.626380,1.794933,5.598358,0.636103,1.337022,0.413797,-6.575710,2.468253,7.450516,-9.593230,8.554786,-8.804131,-6.276221,-8.468299,9.879414,1.863869,5.975303,3.573014,7.136847,-7.522576,-6.355791,4.072590,-4.898720,-4.612036,-6.619819,-2.077578,4.669787,-5.575844,-8.603173,8.879468,-7.871436,7.801022,3.871626,6.533346,2.060359,1.527841,0.883543,-1.948390,1.393867,5.719284,2.355416,3.141870,-2.835013,-2.414983,1.860183,-9.907682,6.626940,6.892720,-6.516520,4.004693,2.740036,2.614457,4.482916,-0.132059,6.302299,8.278961,8.653893,0.403977,-3.063343,-9.689380,3.950458,7.291031,1.640254,1.454407,7.099971,1.303593,-3.293713,8.195089,2.784398,-9.728158,5.286574,1.389421,0.813675,0.957515,9.280203,9.885033,-4.430620,5.054655,3.198151,-6.837692,4.813748,3.926312,-6.211952,-5.412777,7.524863,-7.295941,-1.715714,7.256716,6.132964,2.935073,7.628280,6.567934,1.327024,8.490603,-1.569818,-2.842822,3.652099,2.988757,-8.224756,3.799144,-7.119305,7.346940,-7.442416,-3.194240,1.948060,-5.004363,-4.803616,-2.044813,-4.124387,4.210649,0.077400,-3.713402,4.072815,6.448270,2.329633,2.170961,-1.522314,-1.322465,-0.118158,-7.443175,-6.747955,-8.171838,9.415008,3.778923,-6.896761,-1.589479,-3.961386,-5.578821,-2.247346,0.340715,4.472959,3.827598,8.364476,-3.933284,3.714780,0.276254,8.211404,-3.804581,7.212558,-1.043574,-7.886970,5.766611,7.528377,1.405274,1.278916,-4.997961,9.964932,1.864922,6.861380,-1.883476,-6.167955,5.822757,7.982355,-9.582833,1.665051,-8.571099,9.027047,-2.294147,-1.724590,-2.795894,-5.374076,-6.315064,7.784485,7.638060,9.258843,2.298054,3.796698,6.643641,-7.678904,9.115372,-4.925730,-7.894040,-5.540418,-3.062456,-0.879949,-4.365275,1.138393,-4.539282,-8.157077,-3.121096,-7.611202,-2.306909,-8.570645,-8.168779,2.074121,-5.262225,-4.253525,-4.246250,5.240360,3.167155,8.407648,-2.813878,-9.867479,6.536229,-9.452213,-4.333866,9.691666,2.686845,-1.112287,7.094013,8.516469,5.459912,-3.962041,-5.582448,-8.520493,5.443001,-0.573830,9.232318,-4.945079,5.924397,-6.369571,4.768847,-2.725046,6.195842,2.514879,8.306057,-3.869265,-3.217899,-3.684976,-7.790246,-3.044453,-2.832154,4.088893,8.771364,3.575391,5.087793,-5.924769,1.016064,7.331529,7.967865,1.740649,8.237369,2.642318,-1.530355,8.382293,-2.109295,-6.424594,-9.172102,-7.800269,-5.577925,-8.091220,0.107380,-1.551521,-1.880503,3.233938,-8.796292,-9.996491,-2.155935,5.167132,9.228697,1.979695,-9.725322,-3.735553,-4.242777,-5.482338,-0.950297,-2.659387,3.345295,4.134875,-6.592114,6.299653,8.078013,-9.532087,9.956786,7.028208,-9.066567,6.973216,-1.328766,8.883332,-7.393241,6.992422,2.102872,5.256299,7.649315,-0.461183,6.332995,-2.755800,4.742617,1.286017,0.552838,2.129055,6.576127,-5.718292,-3.667511,-3.264134,-6.727009,-3.257817,7.145602,-8.355165,-8.457450,-9.347392,4.706423,-1.024612,-6.406105,8.891607,-8.163293,8.205372,4.400876,-7.317988,-6.296281,5.803644,-5.481458,-6.182256,8.126524,-7.134016,4.209407,2.052061,-7.576928,8.070340,2.730355,-4.740262,2.225796,-5.725414], dtype = "float64")#candidate|2812|(432,)|const|float64
call_2811 = relay.TupleGetItem(func_1925_call(relay.reshape(const_2812.astype('float64'), [9, 4, 12]), relay.reshape(const_2796.astype('int8'), [2880,]), ), 1)
call_2813 = relay.TupleGetItem(func_1928_call(relay.reshape(const_2812.astype('float64'), [9, 4, 12]), relay.reshape(const_2796.astype('int8'), [2880,]), ), 1)
output = relay.Tuple([call_2759,call_2772,call_2789,const_2790,bop_2797,call_2811,const_2812,])
output2 = relay.Tuple([call_2760,call_2773,call_2791,const_2790,bop_2800,call_2813,const_2812,])
func_2814 = relay.Function([], output)
mod['func_2814'] = func_2814
mod = relay.transform.InferType()(mod)
mutated_mod['func_2814'] = func_2814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mutated_mod.get_global_var('func_2814')
call_2815 = func_2814_call()
output = call_2815
func_2816 = relay.Function([], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_2825 = relay.TupleGetItem(func_2814_call(), 3)
call_2826 = relay.TupleGetItem(func_2816_call(), 3)
func_1613_call = mod.get_global_var('func_1613')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_2827 = relay.TupleGetItem(func_1613_call(), 0)
call_2828 = relay.TupleGetItem(func_1615_call(), 0)
output = relay.Tuple([call_2825,call_2827,])
output2 = relay.Tuple([call_2826,call_2828,])
func_2838 = relay.Function([], output)
mod['func_2838'] = func_2838
mod = relay.transform.InferType()(mod)
mutated_mod['func_2838'] = func_2838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2838_call = mutated_mod.get_global_var('func_2838')
call_2839 = func_2838_call()
output = call_2839
func_2840 = relay.Function([], output)
mutated_mod['func_2840'] = func_2840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2590_call = mod.get_global_var('func_2590')
func_2592_call = mutated_mod.get_global_var('func_2592')
call_2848 = relay.TupleGetItem(func_2590_call(), 1)
call_2849 = relay.TupleGetItem(func_2592_call(), 1)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_2864 = relay.TupleGetItem(func_276_call(relay.reshape(call_2848.astype('float64'), [10, 1, 2])), 0)
call_2865 = relay.TupleGetItem(func_279_call(relay.reshape(call_2848.astype('float64'), [10, 1, 2])), 0)
output = relay.Tuple([call_2848,call_2864,])
output2 = relay.Tuple([call_2849,call_2865,])
func_2870 = relay.Function([], output)
mod['func_2870'] = func_2870
mod = relay.transform.InferType()(mod)
mutated_mod['func_2870'] = func_2870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mutated_mod.get_global_var('func_2870')
call_2871 = func_2870_call()
output = call_2871
func_2872 = relay.Function([], output)
mutated_mod['func_2872'] = func_2872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_2988 = func_1640_call()
call_2989 = func_1640_call()
output = call_2988
output2 = call_2989
func_3001 = relay.Function([], output)
mod['func_3001'] = func_3001
mod = relay.transform.InferType()(mod)
mutated_mod['func_3001'] = func_3001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3001_call = mutated_mod.get_global_var('func_3001')
call_3002 = func_3001_call()
output = call_3002
func_3003 = relay.Function([], output)
mutated_mod['func_3003'] = func_3003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2872_call = mutated_mod.get_global_var('func_2872')
call_3006 = relay.TupleGetItem(func_2870_call(), 0)
call_3007 = relay.TupleGetItem(func_2872_call(), 0)
func_1902_call = mod.get_global_var('func_1902')
func_1905_call = mutated_mod.get_global_var('func_1905')
var_3028 = relay.var("var_3028", dtype = "float32", shape = (200,))#candidate|3028|(200,)|var|float32
call_3027 = relay.TupleGetItem(func_1902_call(relay.reshape(var_3028.astype('float32'), [10, 10, 2])), 2)
call_3029 = relay.TupleGetItem(func_1905_call(relay.reshape(var_3028.astype('float32'), [10, 10, 2])), 2)
output = relay.Tuple([call_3006,call_3027,var_3028,])
output2 = relay.Tuple([call_3007,call_3029,var_3028,])
func_3046 = relay.Function([var_3028,], output)
mod['func_3046'] = func_3046
mod = relay.transform.InferType()(mod)
var_3047 = relay.var("var_3047", dtype = "float32", shape = (200,))#candidate|3047|(200,)|var|float32
output = func_3046(var_3047)
func_3048 = relay.Function([var_3047], output)
mutated_mod['func_3048'] = func_3048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_3064 = func_2377_call()
call_3065 = func_2377_call()
output = call_3064
output2 = call_3065
func_3101 = relay.Function([], output)
mod['func_3101'] = func_3101
mod = relay.transform.InferType()(mod)
mutated_mod['func_3101'] = func_3101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3101_call = mutated_mod.get_global_var('func_3101')
call_3102 = func_3101_call()
output = call_3102
func_3103 = relay.Function([], output)
mutated_mod['func_3103'] = func_3103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1613_call = mod.get_global_var('func_1613')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_3104 = relay.TupleGetItem(func_1613_call(), 0)
call_3105 = relay.TupleGetItem(func_1615_call(), 0)
func_2506_call = mod.get_global_var('func_2506')
func_2508_call = mutated_mod.get_global_var('func_2508')
call_3111 = func_2506_call()
call_3112 = func_2506_call()
output = relay.Tuple([call_3104,call_3111,])
output2 = relay.Tuple([call_3105,call_3112,])
func_3130 = relay.Function([], output)
mod['func_3130'] = func_3130
mod = relay.transform.InferType()(mod)
mutated_mod['func_3130'] = func_3130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mutated_mod.get_global_var('func_3130')
call_3131 = func_3130_call()
output = call_3131
func_3132 = relay.Function([], output)
mutated_mod['func_3132'] = func_3132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_3160 = func_1439_call()
call_3161 = func_1439_call()
func_1078_call = mod.get_global_var('func_1078')
func_1080_call = mutated_mod.get_global_var('func_1080')
const_3170 = relay.const([8.966895,-9.634319,-6.744966,-4.681905,1.088729,3.418914,-4.123303,-6.037251,-2.229899,3.979236,-4.374315,3.544377,-0.155235,-2.253527,-9.899445,8.811091,-6.811927,1.150621,-3.298441,6.108757], dtype = "float32")#candidate|3170|(20,)|const|float32
call_3169 = relay.TupleGetItem(func_1078_call(relay.reshape(const_3170.astype('float32'), [10, 2])), 1)
call_3171 = relay.TupleGetItem(func_1080_call(relay.reshape(const_3170.astype('float32'), [10, 2])), 1)
output = relay.Tuple([call_3160,call_3169,const_3170,])
output2 = relay.Tuple([call_3161,call_3171,const_3170,])
func_3189 = relay.Function([], output)
mod['func_3189'] = func_3189
mod = relay.transform.InferType()(mod)
mutated_mod['func_3189'] = func_3189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3189_call = mutated_mod.get_global_var('func_3189')
call_3190 = func_3189_call()
output = call_3190
func_3191 = relay.Function([], output)
mutated_mod['func_3191'] = func_3191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2073_call = mutated_mod.get_global_var('func_2073')
call_3224 = func_2072_call()
call_3225 = func_2072_call()
var_3238 = relay.var("var_3238", dtype = "float32", shape = (10, 10, 2))#candidate|3238|(10, 10, 2)|var|float32
bop_3239 = relay.not_equal(call_3224.astype('bool'), relay.reshape(var_3238.astype('bool'), relay.shape_of(call_3224))) # shape=(10, 10, 2)
bop_3242 = relay.not_equal(call_3225.astype('bool'), relay.reshape(var_3238.astype('bool'), relay.shape_of(call_3225))) # shape=(10, 10, 2)
uop_3271 = relay.log2(bop_3239.astype('float64')) # shape=(10, 10, 2)
uop_3273 = relay.log2(bop_3242.astype('float64')) # shape=(10, 10, 2)
uop_3285 = relay.tan(call_3224.astype('float32')) # shape=(10, 10, 2)
uop_3287 = relay.tan(call_3225.astype('float32')) # shape=(10, 10, 2)
output = relay.Tuple([uop_3271,uop_3285,])
output2 = relay.Tuple([uop_3273,uop_3287,])
func_3296 = relay.Function([var_3238,], output)
mod['func_3296'] = func_3296
mod = relay.transform.InferType()(mod)
mutated_mod['func_3296'] = func_3296
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3297 = relay.var("var_3297", dtype = "float32", shape = (10, 10, 2))#candidate|3297|(10, 10, 2)|var|float32
func_3296_call = mutated_mod.get_global_var('func_3296')
call_3298 = func_3296_call(var_3297)
output = call_3298
func_3299 = relay.Function([var_3297], output)
mutated_mod['func_3299'] = func_3299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1606_call = mod.get_global_var('func_1606')
func_1608_call = mutated_mod.get_global_var('func_1608')
call_3331 = func_1606_call()
call_3332 = func_1606_call()
output = call_3331
output2 = call_3332
func_3342 = relay.Function([], output)
mod['func_3342'] = func_3342
mod = relay.transform.InferType()(mod)
output = func_3342()
func_3343 = relay.Function([], output)
mutated_mod['func_3343'] = func_3343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1833_call = mod.get_global_var('func_1833')
func_1834_call = mutated_mod.get_global_var('func_1834')
call_3362 = relay.TupleGetItem(func_1833_call(), 0)
call_3363 = relay.TupleGetItem(func_1834_call(), 0)
output = relay.Tuple([call_3362,])
output2 = relay.Tuple([call_3363,])
func_3379 = relay.Function([], output)
mod['func_3379'] = func_3379
mod = relay.transform.InferType()(mod)
mutated_mod['func_3379'] = func_3379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mutated_mod.get_global_var('func_3379')
call_3380 = func_3379_call()
output = call_3380
func_3381 = relay.Function([], output)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1606_call = mod.get_global_var('func_1606')
func_1608_call = mutated_mod.get_global_var('func_1608')
call_3397 = func_1606_call()
call_3398 = func_1606_call()
output = call_3397
output2 = call_3398
func_3400 = relay.Function([], output)
mod['func_3400'] = func_3400
mod = relay.transform.InferType()(mod)
mutated_mod['func_3400'] = func_3400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3400_call = mutated_mod.get_global_var('func_3400')
call_3401 = func_3400_call()
output = call_3401
func_3402 = relay.Function([], output)
mutated_mod['func_3402'] = func_3402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3400_call = mod.get_global_var('func_3400')
func_3402_call = mutated_mod.get_global_var('func_3402')
call_3540 = func_3400_call()
call_3541 = func_3400_call()
output = call_3540
output2 = call_3541
func_3547 = relay.Function([], output)
mod['func_3547'] = func_3547
mod = relay.transform.InferType()(mod)
mutated_mod['func_3547'] = func_3547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3547_call = mutated_mod.get_global_var('func_3547')
call_3548 = func_3547_call()
output = call_3548
func_3549 = relay.Function([], output)
mutated_mod['func_3549'] = func_3549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2178_call = mod.get_global_var('func_2178')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_3599 = func_2178_call()
call_3600 = func_2178_call()
output = relay.Tuple([call_3599,])
output2 = relay.Tuple([call_3600,])
func_3603 = relay.Function([], output)
mod['func_3603'] = func_3603
mod = relay.transform.InferType()(mod)
output = func_3603()
func_3604 = relay.Function([], output)
mutated_mod['func_3604'] = func_3604
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3656 = relay.const([[[1.754223,-9.364393,5.236327,-6.671999,2.602211,0.141393,-4.997795,-5.584014,-9.793645,-9.979973,3.118411],[0.028247,2.685494,-7.488216,-4.109836,-0.636040,5.897979,3.855662,6.183472,2.415071,-8.740376,-1.745130],[-3.712833,0.170564,0.387772,5.578369,-1.480002,6.207018,7.362914,-9.121905,-4.137457,2.840030,9.395580],[-9.184182,5.514759,-0.644811,-8.093269,-3.691786,2.028019,-3.109416,9.933398,8.956102,-4.171858,4.386735],[7.209099,6.230770,-7.981784,9.187765,1.870866,-2.428939,-8.358890,-9.047480,4.634666,6.352314,-4.274118],[-3.806662,-6.786160,-6.429399,-0.525371,-1.011191,1.027059,4.086863,-6.872975,-9.302755,8.986834,-1.430059]],[[5.740808,-7.819379,3.636735,0.523497,8.872415,3.783613,-4.739305,-0.735507,4.214740,-8.657766,-7.978035],[-7.108540,-2.042741,-2.320997,-7.670115,0.952237,-7.979138,-1.616566,-5.990094,9.385881,2.343893,5.315321],[-7.983840,3.743364,-2.935048,7.959275,4.338724,7.384610,-8.267806,4.128664,0.810418,-0.287105,8.318202],[8.680507,-6.100876,0.444916,-4.603405,9.783220,2.345192,-5.846496,-6.793282,-0.190168,-9.602570,-5.629930],[-5.304873,0.143544,-6.854476,7.131220,-2.223507,1.721095,2.850630,4.695492,6.929966,4.976048,2.475603],[-4.340748,7.773689,2.820037,0.716073,-6.690231,-4.824130,5.138281,3.309260,-4.084952,6.265200,-1.278732]],[[-9.924227,-0.114510,0.743339,-9.927668,-9.497530,-8.668560,-7.215761,5.617837,1.559291,9.967160,5.125427],[8.908722,7.542719,-1.738867,4.259060,2.690926,-8.749464,-6.452913,4.553699,-5.173498,7.157879,9.380893],[3.945424,8.277994,-6.585138,-3.127230,7.148243,-5.278142,5.245765,-3.016765,-7.319005,-3.786692,7.172147],[-9.454955,-7.199382,-9.384399,6.680447,9.223383,-0.264280,-7.382174,9.753504,-7.121776,-1.917307,3.467324],[-0.577055,-4.005389,2.440233,4.050693,9.044024,-3.150091,9.875984,-1.815828,-9.175465,8.030947,-9.946195],[-7.468632,-9.882965,8.306097,9.804195,-9.586268,-5.481236,-0.889202,5.053005,-5.560871,3.946105,-4.468606]],[[-2.200574,-7.271884,-4.378953,5.647017,2.519287,-2.210188,5.177004,-0.168034,-9.949940,-7.372799,6.888682],[0.366782,-1.433665,-0.690619,-4.396599,-2.329096,7.111417,4.366535,-6.568071,-6.823357,-2.539857,2.342979],[-7.909668,1.212622,-0.470920,2.683658,-7.218677,2.277762,8.457373,7.981784,-1.280941,-5.112487,-2.610813],[-4.230996,-5.983826,-8.177905,7.100301,-7.949664,4.319313,9.464350,5.747572,2.943829,2.376804,1.658531],[-4.209191,-9.660276,-2.556928,-2.722551,-2.006950,-4.722778,-6.730998,-6.710276,-2.261920,9.188680,-4.226394],[-5.791060,-7.591336,8.625100,-4.832865,-6.624507,3.394048,8.349133,7.917704,-8.604283,-7.172091,-2.017674]],[[7.087986,8.177917,-9.436581,5.148588,3.737718,-1.416054,-4.705495,9.560366,-5.067545,5.002741,-2.807456],[-7.743608,0.410643,4.850182,7.148774,-3.429628,-0.306849,-6.203082,-9.103728,2.626854,5.707827,2.111535],[-3.741447,-3.366688,-9.964543,-6.987835,1.401654,-7.968292,-0.983242,-4.679048,-3.330336,-6.052057,-1.592931],[7.907764,1.974211,-5.329060,-0.059485,-3.050345,-9.419094,-7.075110,-8.614604,1.394978,7.474259,-3.493840],[-4.461144,7.573738,7.310899,7.129841,-9.236595,6.547800,-3.248411,2.466276,3.336733,5.631938,-7.783485],[2.219590,-8.594587,-4.260964,-5.770950,9.923205,-8.473007,6.131287,6.746972,4.747097,9.416782,9.737620]],[[1.453260,1.409550,-7.353910,-8.742713,-7.880808,8.146364,9.007302,-7.989570,8.385135,-8.742999,-0.855658],[2.794859,-4.134122,5.023400,0.689767,9.132224,4.969898,-1.424768,5.611841,7.955168,-3.661384,7.401341],[-9.967059,3.552907,7.540945,2.568786,-9.037412,2.690129,-8.916840,-7.790153,6.405651,-8.316894,-1.841840],[-2.533424,1.175398,5.426020,0.409234,0.542477,-6.494735,2.188072,-5.432717,7.389671,2.115662,-5.816067],[-6.128254,-0.873332,-5.450268,-2.483770,4.706622,0.789702,-5.646262,-5.147951,0.456325,-8.080664,-9.239256],[1.694722,-2.919397,9.684925,-2.954695,1.144760,8.688576,-7.383711,-9.114294,-7.044415,-8.420264,9.245790]],[[7.542774,-7.346201,1.539901,-9.773754,-8.414802,3.502511,3.524842,-6.843972,-6.542660,-4.207346,3.780914],[0.295737,0.871354,9.974042,1.867833,8.950844,-3.052132,9.942971,-2.505852,-4.354538,-4.464039,2.585634],[-4.447124,7.384948,-3.735953,-1.831472,-1.599971,9.119485,-7.318499,8.244964,8.143544,-6.664626,-1.525524],[-1.016382,6.547412,0.412197,-7.828348,3.632352,2.646989,7.245039,-3.434049,0.366105,9.599102,8.035533],[-1.066666,-7.919153,9.572533,8.325982,-6.667200,-9.253172,-6.530730,2.942220,-8.161563,-8.071896,1.248023],[9.578778,6.168108,5.614021,-0.522242,-3.140585,1.421019,-6.372798,4.464095,5.034194,9.834452,-4.902893]],[[4.089358,-3.954297,-4.677492,3.629694,-5.607893,-9.623795,-8.010242,8.558711,-9.344186,6.473341,-5.823310],[-9.689941,7.634845,0.379747,6.115115,3.537759,-0.306234,-2.444842,-0.898811,-9.465183,1.071263,-9.912435],[-9.941652,-9.665004,-0.533396,9.118532,9.504286,-4.469941,2.253023,-0.760768,4.651394,4.119326,9.921803],[2.152176,-4.349463,0.477261,-6.526105,1.479366,7.307354,4.928837,8.091146,-0.397175,-1.065088,1.447800],[-7.949758,-3.428612,9.500099,8.295655,1.731378,-9.117894,5.286660,1.671495,-3.843814,-1.768414,-3.774628],[0.580699,-9.434667,4.861006,-4.366605,-1.330395,-7.987105,2.569702,1.650732,-3.286922,8.166275,-4.514546]],[[-4.848647,-2.064013,-3.987930,-4.177552,-4.250748,-8.494435,7.186496,3.575374,-0.145800,3.808106,-0.490204],[2.860220,7.220016,-2.004680,-9.618134,3.044547,7.868419,1.079035,5.000256,-3.649083,0.984065,-2.517845],[-6.408088,2.648576,-9.953692,8.839737,6.759746,-9.244594,8.222229,7.207205,4.532231,-2.276158,-1.150997],[-9.069302,-7.730792,4.225555,8.320174,-3.149719,4.839660,-5.051133,-9.539467,-4.766336,-4.514903,2.227486],[7.107336,-7.568604,5.129717,2.552553,-8.179866,5.915467,2.292325,9.287976,9.300662,-6.416522,8.114097],[-8.971008,8.303141,6.809673,8.724927,3.165770,3.981673,0.145693,-8.146471,-8.483860,-4.924057,1.521417]],[[-9.890809,-4.511586,5.160165,-2.598286,6.983421,-6.737243,4.179986,0.181719,-6.745582,7.631237,-7.241770],[1.105498,-2.138099,1.166402,5.949535,-5.875710,6.010823,2.354477,0.800587,6.726352,-8.040188,5.059951],[0.991976,-1.132173,3.924431,3.378367,-5.384955,7.627118,-5.046964,6.217021,8.515308,8.361857,-1.647492],[5.320844,-8.106726,7.419648,0.678813,-6.959836,2.473015,-3.949002,2.605871,-2.902021,-5.391382,-5.295669],[-5.673532,9.064592,7.779920,5.721043,3.930991,1.298578,7.964882,5.721244,-3.839595,-4.679303,-6.187796],[-7.937197,-3.785470,-7.244557,-2.627374,-8.399586,-3.759131,6.193666,-9.746880,-9.839693,5.782629,-5.508068]],[[-9.465812,3.761987,0.736156,-4.905501,9.159970,2.406737,6.590120,-2.096178,-4.440840,-7.996592,-8.468238],[-6.400296,-0.420086,2.361715,0.657388,7.113679,5.356122,-7.398563,-8.017350,-5.649848,3.078588,6.901723],[8.675115,5.841139,-9.627136,6.541349,5.881050,-6.852879,-6.748831,4.229399,7.720061,1.981373,-0.890092],[1.576598,-4.772095,-6.099395,-6.398561,-5.529579,5.795705,9.820199,7.801464,5.753255,9.130730,2.857036],[9.455901,9.401264,6.035616,8.151995,-7.046867,-0.274224,-1.591762,-1.445088,-6.072482,3.970547,-5.802027],[-2.623965,3.737953,-6.782705,0.058470,-2.386234,7.788325,4.304830,-8.997683,-5.197792,8.803082,5.903624]],[[2.767583,-7.495872,-2.440356,2.776967,1.133404,-7.382573,9.433460,7.027134,-1.879747,3.798532,5.612787],[-1.468519,1.872139,-5.806634,1.758058,0.931209,6.191579,3.195306,1.313386,5.425300,-1.938285,0.870712],[-6.034756,-0.098605,-0.646405,-2.833973,-7.994681,1.036517,0.301782,-6.082878,8.847339,9.900188,-3.381700],[-2.449546,-3.890560,-9.622525,6.368631,-2.701998,-8.341427,4.634319,1.038513,-3.198062,-8.881701,8.432558],[4.920608,2.247510,6.330080,6.795342,4.505734,7.143951,2.530741,-6.602922,5.045029,4.340840,6.978322],[-1.076378,-0.141321,-0.604690,-4.083960,5.387586,7.338261,-8.989850,2.929238,-6.063885,9.605197,-5.706229]],[[2.093522,-7.710014,-7.749710,-4.360537,-6.239519,-9.949761,8.000638,3.281786,-3.931567,3.384341,3.204560],[7.590806,-1.797233,2.841602,8.442179,-3.706047,-0.456877,-0.406248,-9.110295,-9.106036,3.578992,-0.143152],[0.369844,5.611271,-5.565219,-8.172713,-6.100618,-1.479495,6.443573,6.062190,-1.539231,-5.377229,-9.486061],[0.083909,3.797539,3.304200,-2.188253,-6.324289,1.121122,1.571272,-2.196000,-6.186196,3.672286,6.888786],[-3.739219,-9.331770,8.397599,-2.892890,0.876705,-6.534123,5.490720,9.914162,4.500117,-0.787763,5.982233],[-6.594925,3.413791,0.502151,-0.345944,7.926262,8.252139,9.009200,-1.845713,-7.963577,3.409473,3.992137]],[[-9.906434,-6.463323,-3.132516,-2.196192,-6.851695,0.602566,7.848657,5.596226,-2.605449,3.084249,-7.934489],[-3.970174,-2.082636,-2.084756,1.284004,-1.780971,-0.549962,-4.549749,5.073420,7.707911,1.545912,3.217317],[7.982312,-0.451611,-6.274899,0.729179,-2.968919,1.249469,-7.229405,-4.154583,1.498876,1.005697,7.958270],[-3.543902,-4.183557,9.544020,4.137144,4.906208,5.479140,-6.088500,4.290312,-5.965560,4.796675,-3.790906],[8.967972,4.059916,8.832705,-2.604040,-0.168114,-3.580310,-6.573894,4.521301,-1.148885,-2.821125,-9.178395],[0.732379,-4.961644,-0.209438,-8.875470,6.806961,9.378261,-0.903361,9.012039,-4.050979,-6.743350,6.099097]],[[-2.647595,-0.276507,8.834622,-6.787473,9.830521,2.322389,5.752091,8.429586,-3.248521,4.566244,7.784313],[-1.393635,-5.090226,7.160691,1.417851,-2.229097,6.618669,1.938660,2.291828,-8.073769,0.295365,9.764593],[9.615115,-5.621591,3.929726,-0.070859,-1.338254,-4.412509,4.098454,5.320419,-0.585534,-7.631345,-7.943360],[-5.101000,6.085416,-7.361882,-5.414431,5.820652,-1.580687,0.172438,8.776675,-3.389647,-3.796943,-3.512764],[-1.110758,6.185183,9.440260,-4.692419,9.981226,-7.562313,-6.987959,1.804079,-7.140081,-2.280796,8.858382],[-3.063303,3.452954,-2.518010,7.017049,8.131439,-5.636670,-6.971324,-7.493116,6.109829,4.819775,-6.432777]]], dtype = "float32")#candidate|3656|(15, 6, 11)|const|float32
var_3657 = relay.var("var_3657", dtype = "float32", shape = (15, 6, 11))#candidate|3657|(15, 6, 11)|var|float32
bop_3658 = relay.floor_mod(const_3656.astype('float32'), relay.reshape(var_3657.astype('float32'), relay.shape_of(const_3656))) # shape=(15, 6, 11)
bop_3662 = relay.mod(bop_3658.astype('float32'), relay.reshape(const_3656.astype('float32'), relay.shape_of(bop_3658))) # shape=(15, 6, 11)
var_3669 = relay.var("var_3669", dtype = "float32", shape = (15, 6, 11))#candidate|3669|(15, 6, 11)|var|float32
bop_3670 = relay.less_equal(const_3656.astype('bool'), relay.reshape(var_3669.astype('bool'), relay.shape_of(const_3656))) # shape=(15, 6, 11)
uop_3684 = relay.sqrt(const_3656.astype('float32')) # shape=(15, 6, 11)
var_3694 = relay.var("var_3694", dtype = "float32", shape = (15, 6, 11))#candidate|3694|(15, 6, 11)|var|float32
bop_3695 = relay.divide(uop_3684.astype('float64'), relay.reshape(var_3694.astype('float64'), relay.shape_of(uop_3684))) # shape=(15, 6, 11)
func_3400_call = mod.get_global_var('func_3400')
func_3402_call = mutated_mod.get_global_var('func_3402')
call_3700 = func_3400_call()
call_3701 = func_3400_call()
uop_3717 = relay.log2(bop_3695.astype('float64')) # shape=(15, 6, 11)
output = relay.Tuple([bop_3662,bop_3670,call_3700,uop_3717,])
output2 = relay.Tuple([bop_3662,bop_3670,call_3701,uop_3717,])
func_3732 = relay.Function([var_3657,var_3669,var_3694,], output)
mod['func_3732'] = func_3732
mod = relay.transform.InferType()(mod)
mutated_mod['func_3732'] = func_3732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3732_call = mutated_mod.get_global_var('func_3732')
var_3734 = relay.var("var_3734", dtype = "float32", shape = (15, 6, 11))#candidate|3734|(15, 6, 11)|var|float32
var_3735 = relay.var("var_3735", dtype = "float32", shape = (15, 6, 11))#candidate|3735|(15, 6, 11)|var|float32
var_3736 = relay.var("var_3736", dtype = "float32", shape = (15, 6, 11))#candidate|3736|(15, 6, 11)|var|float32
call_3733 = func_3732_call(var_3734,var_3735,var_3736,)
output = call_3733
func_3737 = relay.Function([var_3734,var_3735,var_3736,], output)
mutated_mod['func_3737'] = func_3737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2872_call = mutated_mod.get_global_var('func_2872')
call_3748 = relay.TupleGetItem(func_2870_call(), 0)
call_3749 = relay.TupleGetItem(func_2872_call(), 0)
func_1276_call = mod.get_global_var('func_1276')
func_1278_call = mutated_mod.get_global_var('func_1278')
var_3757 = relay.var("var_3757", dtype = "float32", shape = (12,))#candidate|3757|(12,)|var|float32
call_3756 = relay.TupleGetItem(func_1276_call(relay.reshape(var_3757.astype('float32'), [2, 1, 6])), 0)
call_3758 = relay.TupleGetItem(func_1278_call(relay.reshape(var_3757.astype('float32'), [2, 1, 6])), 0)
output = relay.Tuple([call_3748,call_3756,var_3757,])
output2 = relay.Tuple([call_3749,call_3758,var_3757,])
func_3761 = relay.Function([var_3757,], output)
mod['func_3761'] = func_3761
mod = relay.transform.InferType()(mod)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3762 = relay.var("var_3762", dtype = "float32", shape = (12,))#candidate|3762|(12,)|var|float32
func_3761_call = mutated_mod.get_global_var('func_3761')
call_3763 = func_3761_call(var_3762)
output = call_3763
func_3764 = relay.Function([var_3762], output)
mutated_mod['func_3764'] = func_3764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3832 = relay.var("var_3832", dtype = "float32", shape = (10, 2, 13))#candidate|3832|(10, 2, 13)|var|float32
const_3833 = relay.const([[[-6.833288,4.584255,2.108376,-1.014829,7.288123,-2.487709,-3.264909,-0.548162,-9.883566,-4.204635,-9.831975,-2.422507,-5.912840],[5.071428,7.190261,3.130363,-4.736153,-8.766758,-3.401186,-3.791069,7.937592,-7.886852,0.840135,3.907889,0.427526,0.039380]],[[4.457522,-1.326927,6.906233,2.873963,8.430385,7.106073,4.047238,0.708205,-3.610393,-4.691583,-7.495964,-8.223148,5.184611],[-1.854937,6.905480,5.224711,2.946332,-1.960035,4.055126,9.753935,4.143286,6.447723,-6.809762,-6.400095,-9.592472,-9.123263]],[[6.302091,-7.333843,0.137368,8.087363,-8.626663,9.646412,-3.723270,2.782895,4.019914,-3.814914,2.863616,-6.291835,-2.337048],[-3.081598,7.169607,-8.561636,6.376873,1.824421,6.298261,-0.726131,8.397999,9.373201,0.750105,-1.077453,8.118845,5.217900]],[[-2.154891,-8.641022,-4.125779,9.400182,4.739986,-3.469623,-3.531034,8.462946,-1.285358,-5.720375,8.604920,-8.198573,-6.232088],[-8.389199,8.604562,-1.733204,6.984524,6.135951,7.780247,8.201237,-9.733037,-1.639317,9.559609,-6.299120,2.010203,-4.609815]],[[-3.172570,1.335377,6.058094,-7.193218,-5.691825,-4.372913,0.292370,7.729319,-3.721088,7.075722,8.961299,6.247548,-0.120180],[-6.116557,-0.938534,-8.750646,3.088326,6.269762,1.069149,-9.460003,-5.731198,5.799406,-5.148343,8.168455,0.762252,7.382341]],[[-7.468755,-1.834486,-6.542902,-1.951546,4.612238,3.217981,-8.690773,8.665043,-5.912098,8.051548,-8.998257,-0.036261,-1.955425],[8.735748,-7.815903,-4.494100,6.625249,4.835775,7.891541,0.072651,2.955638,-5.762028,3.243326,1.342457,5.027666,1.860438]],[[-2.152082,-1.797874,6.845582,-1.400794,-0.744618,-0.574401,7.461429,4.112230,5.933468,1.967261,4.343932,-1.577439,1.656310],[-7.796311,4.564503,-0.684601,5.381216,-0.673360,-0.606047,-6.691152,0.747562,2.870387,9.596978,8.704920,7.460563,2.166663]],[[-2.243186,5.491189,7.813523,-8.987283,4.928985,-8.091769,7.264033,9.446415,-3.157018,-0.557869,-7.884866,-6.259470,-1.584184],[-9.642943,9.287314,-3.395055,-9.829976,9.575420,7.449413,-6.359231,9.892274,9.037758,7.359884,-7.017907,6.435174,2.839203]],[[-8.894077,6.752369,6.993787,-8.056210,3.610919,9.871974,0.179611,3.818339,-5.879561,4.034348,6.012414,8.759033,-3.021473],[-2.406826,-9.689328,7.591441,5.044417,-5.070973,4.963209,6.496191,9.676100,-6.637225,-1.078764,-2.411670,3.469194,-4.137493]],[[-0.319785,3.572641,5.585613,-8.717638,0.703708,0.773307,-1.955588,8.592206,-9.233279,-8.361813,4.519730,-1.650489,3.330223],[8.116695,5.338161,6.336307,8.631227,-0.286793,-9.326018,-2.931675,-0.300224,-1.100292,8.714728,-2.652413,4.151491,-3.852798]]], dtype = "float32")#candidate|3833|(10, 2, 13)|const|float32
bop_3834 = relay.floor_divide(var_3832.astype('float32'), relay.reshape(const_3833.astype('float32'), relay.shape_of(var_3832))) # shape=(10, 2, 13)
uop_3840 = relay.atanh(const_3833.astype('float64')) # shape=(10, 2, 13)
func_1699_call = mod.get_global_var('func_1699')
func_1701_call = mutated_mod.get_global_var('func_1701')
var_3854 = relay.var("var_3854", dtype = "float32", shape = (384,))#candidate|3854|(384,)|var|float32
call_3853 = func_1699_call(relay.reshape(var_3854.astype('float32'), [3, 16, 8]))
call_3855 = func_1699_call(relay.reshape(var_3854.astype('float32'), [3, 16, 8]))
bop_3862 = relay.greater(const_3833.astype('bool'), relay.reshape(var_3832.astype('bool'), relay.shape_of(const_3833))) # shape=(10, 2, 13)
func_3342_call = mod.get_global_var('func_3342')
func_3343_call = mutated_mod.get_global_var('func_3343')
call_3865 = func_3342_call()
call_3866 = func_3342_call()
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_3878 = relay.TupleGetItem(func_1716_call(), 0)
call_3879 = relay.TupleGetItem(func_1717_call(), 0)
bop_3896 = relay.power(uop_3840.astype('float32'), relay.reshape(bop_3834.astype('float32'), relay.shape_of(uop_3840))) # shape=(10, 2, 13)
output = relay.Tuple([call_3853,var_3854,bop_3862,call_3865,call_3878,bop_3896,])
output2 = relay.Tuple([call_3855,var_3854,bop_3862,call_3866,call_3879,bop_3896,])
func_3913 = relay.Function([var_3832,var_3854,], output)
mod['func_3913'] = func_3913
mod = relay.transform.InferType()(mod)
mutated_mod['func_3913'] = func_3913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3913_call = mutated_mod.get_global_var('func_3913')
var_3915 = relay.var("var_3915", dtype = "float32", shape = (10, 2, 13))#candidate|3915|(10, 2, 13)|var|float32
var_3916 = relay.var("var_3916", dtype = "float32", shape = (384,))#candidate|3916|(384,)|var|float32
call_3914 = func_3913_call(var_3915,var_3916,)
output = call_3914
func_3917 = relay.Function([var_3915,var_3916,], output)
mutated_mod['func_3917'] = func_3917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_3942 = func_1439_call()
call_3943 = func_1439_call()
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
var_3953 = relay.var("var_3953", dtype = "float64", shape = (20,))#candidate|3953|(20,)|var|float64
call_3952 = relay.TupleGetItem(func_276_call(relay.reshape(var_3953.astype('float64'), [10, 1, 2])), 0)
call_3954 = relay.TupleGetItem(func_279_call(relay.reshape(var_3953.astype('float64'), [10, 1, 2])), 0)
func_2838_call = mod.get_global_var('func_2838')
func_2840_call = mutated_mod.get_global_var('func_2840')
call_3957 = relay.TupleGetItem(func_2838_call(), 0)
call_3958 = relay.TupleGetItem(func_2840_call(), 0)
output = relay.Tuple([call_3942,call_3952,var_3953,call_3957,])
output2 = relay.Tuple([call_3943,call_3954,var_3953,call_3958,])
func_3963 = relay.Function([var_3953,], output)
mod['func_3963'] = func_3963
mod = relay.transform.InferType()(mod)
mutated_mod['func_3963'] = func_3963
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3964 = relay.var("var_3964", dtype = "float64", shape = (20,))#candidate|3964|(20,)|var|float64
func_3963_call = mutated_mod.get_global_var('func_3963')
call_3965 = func_3963_call(var_3964)
output = call_3965
func_3966 = relay.Function([var_3964], output)
mutated_mod['func_3966'] = func_3966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3547_call = mod.get_global_var('func_3547')
func_3549_call = mutated_mod.get_global_var('func_3549')
call_4007 = func_3547_call()
call_4008 = func_3547_call()
func_2463_call = mod.get_global_var('func_2463')
func_2467_call = mutated_mod.get_global_var('func_2467')
const_4027 = relay.const([-6.308131,-7.260069,-3.904752,7.067206,-2.418288,-4.609103,3.234016,8.537151,5.778103,4.883039,2.568970,4.303999,-5.188211,-7.508234,-5.004327,3.546687,-6.169872,-5.413312,-1.982471,-2.145285,9.327333,3.252789,4.667416,7.213814,-0.809511,8.385240,3.257014,-1.322887,-6.239425,2.017040,-4.183227,-2.089326,9.081333,6.576555,-4.321690,-4.140678,0.720819,-5.076620,-5.058560,7.727732,-8.855857,1.865451,0.637657,4.357617,-8.100544,6.144796,1.667982,3.624180,-7.705644,3.799939,8.329822,-3.140806,9.430156,7.125719,-7.138405,-0.095388,4.615611,-8.556635,8.751980,-5.575483,4.525144,3.750150,0.451618,7.819231,4.172261,-0.391616,-1.785086,6.860044,2.313406,9.973841,-3.144923,9.054500,0.311254,-2.014638,6.656309,2.809105,-3.540823,-7.638315,0.012875,4.715268,-6.357164,6.375441,7.386848,-1.334652,5.553266,-4.540108,9.160338,0.592038,-4.089568,7.431511,1.689022,-5.302968,8.277117,4.916005,-8.338976,-2.154635,7.203424,7.440865,-9.852398,8.942397,5.310375,6.518853,3.133768,-5.717783,5.725224,-7.139440,-5.566342,-9.065920,6.536564,-3.879760,3.507569,-6.448480,9.918961,5.081756,4.312715,8.147748,-5.815113,9.253971,-4.284461,0.501228,8.558728,-4.097413,-2.450569,-9.393176,-2.770399,9.648212,6.882848,-4.957341,4.842902,-3.819358,3.289667,-9.711526,7.264790,3.607573,1.846714,4.944342,-4.084589,-6.556994,-1.954484,-6.036683,2.870659,-8.796332,4.994991,8.778589,-0.065121,9.810603,-1.896345,-8.381385,1.112373,7.336540,-8.622567,-9.848428,-6.203635,-9.247320,0.946021,1.703534,-6.764171,8.174270,7.598614,4.844529,-2.242741,7.643741,-2.331553,-9.823299,8.963448,-2.251390,-9.242047,8.648442,6.027684,-1.950065,-5.785271,5.219596,6.594739,2.836131,-8.927437,0.530529,0.407614,2.562301,-3.288936,-3.093503,1.785360,0.655569,6.217922,-6.260685,-1.107363,3.096641,-4.169453,-5.446880,1.038885,-4.338883,-3.929676,-5.500281,-7.081052,1.028491,-4.186035,8.975882,-8.925370,9.700442,2.101698,-1.912015,-3.583161,-6.945262,-1.511307,9.785320,-4.623754,4.854463,4.493585,2.404357,8.528534,-7.527103,-8.533302,3.946634,-7.439723,-4.583350,-5.223691,-8.532902,-8.888021,-7.718798,1.205450,-6.012106,2.710409,-1.158961,0.244678,3.413342,-3.667137,-6.855226,6.042499,6.518031,7.757930,4.160479,-4.000860,-5.028399,-1.504070,9.825840,-1.605671,-3.752641,-0.949488,-3.671305,-2.860826,-2.899192,3.666064,5.578213,4.517558,2.750084,-8.565387,-3.470229,-0.112120,7.798862,0.536869,-0.468883,-1.864458,-9.079475,6.048638,-5.996174,-1.064260,-0.915359,-2.519488,-7.576024,-3.479336,-0.396362,-7.013292,0.886531,1.334117,7.906649,6.519305,7.568619,-3.218250,-3.399013,-7.470983,3.233414,-4.934255,1.102875,2.945609,-4.062435,0.038705,-6.298486,7.034674,-3.491867,-2.202110,-9.517524,2.818395,7.205240,5.149111,9.085630,1.695814,-7.090825,-0.226925,-3.213758,4.223992,0.307468,8.289334,-6.400407,2.535794,3.897700,-6.267010,9.174451,5.683792,-9.509661,3.339064,3.428777,-9.802013,-7.809818,4.754245,4.496349,3.248996,4.780737,-5.668340,9.607268,-0.773554,-9.673546,-9.970171,-2.310244,-0.697429,-8.829999,-4.758228,-4.579273,9.709679,4.791200,0.577535,6.432942,0.036139,2.455257,-4.336992,9.578924,-6.430860,-9.319863,2.869314,-8.696966,8.623387,6.595412,-3.995324,-4.419195,-7.392966,-0.103071,-1.118766,-8.395017,-1.900184,-2.506703,9.299327,6.966934,7.182691,-3.220851,-8.279811,-0.797596,-4.922310,9.357354,-7.147841,-4.739742,9.708324,-2.214495,6.127403,1.945286,5.707549,-0.697708,6.484982,-3.929104,0.915246,-8.519080,8.300989,7.800399,-4.909647,0.897800,0.003753,-7.465325,-0.411000,-3.253131,1.372844,-3.515547,8.472594,3.246701,-1.176196,8.079712,9.574733,-4.769902,4.841911,-4.735080,-6.232812,-9.381982,5.301813,6.498412,6.432737,0.113657,8.655924,5.958945,9.579440,-5.867530,-9.523253,5.440853,4.518933,6.246559,-8.074789,-7.562475,6.217401,-6.811745,3.341017,-6.557775,2.314815,-2.487239,8.225868,-2.593876,-2.263183,7.979152,-7.210515,-8.902062,-2.615506,-6.619319,1.213240,1.748000,9.847000,-3.458813,1.278106,-3.933264,-0.097861,-6.566228,-1.450586,-4.958851,4.714351,-3.620496,5.584250,1.689970,-0.855609,-8.083912,-4.961557,-9.348809,0.821719,4.162234,3.481093,5.924296,-4.582324,-4.091519,-6.283528,3.653465,-5.540523,-1.399149,7.587223,7.236148,0.883019,7.938288,2.836773,-1.135833,-1.738013,-9.222705,0.415568,-0.861885,6.605438,-6.816812,5.154546,7.193804,8.170516,4.124062,9.608723,-5.207681,-2.008717,-1.640678,5.090897,-0.631988,-3.177064,-2.228694,3.071899,9.718454,0.631030,-3.122279,-2.285602,-5.452740,9.962332,-5.738273,-2.040548,-3.635310,-6.224837,-7.853360,0.374412,-5.091616,6.287144,1.993583,2.735478,0.540260,-5.974659,5.406092,0.659427,2.644266,-4.486764,8.643897,-7.163533,9.945331,8.839417,1.254543,8.689957,-7.797830,-9.430129,2.948434,5.814641,-7.541934,-2.072912,-1.268188,4.610861,3.535673,8.959585,-7.035192,-5.763055,-1.597035,0.688384,-2.480888,9.726097,-5.601239,-6.868984,2.634861,-7.337684,5.792671,-7.595064,9.623046,8.852674,1.010920,1.750481,3.103175,0.477751,2.073791,2.562409,0.266333,1.929297,-1.345629,1.087624,6.909338,6.213767,4.367357,-0.292533,8.759092,5.842005,-2.087890,-3.538055,-6.312860,8.185924,-3.968880,1.403577,-8.211808,6.943478,-1.157051,-0.651368,1.450160,-2.350319,0.208899,8.161338,5.561389,0.419422,0.641076,8.747328,-1.292742,-5.750949,5.298020,-7.060163,-0.797536,-8.902012,2.000421,-6.843640,-0.513451,5.310941,4.524674,-1.421524,9.607483,-5.815956,8.454717,-3.543791,-3.720471,-7.599860,-7.559271,8.134563,3.166836,5.195713,3.477037,7.382794,-2.070411,3.955077,5.972647,-9.052659,-4.409459,1.767063,-5.571593,3.444954,-0.353798,-8.478057,-2.983067,9.472444,6.069407,-5.886651,-4.936478,-7.722212,-7.793606,-7.075518,2.660871,-7.979667,1.884005,2.383245,4.925087,6.481109,7.416879,-3.363770,8.469134,4.013792,-7.063517,1.908371,2.118054,-6.102093,-3.953127,5.089571,0.432598,6.964292,6.133590,5.503403,2.649401,9.005071,-8.346822,-3.444130,7.680116,2.717880,-2.039281,0.726754,-0.033006,9.189926,-4.624901,8.353884,6.263818,1.397811,8.962342,3.265827,4.282992,9.662937,1.894532,5.010138,7.227388,-4.611034,-8.727900,4.140218,8.565691,4.321213,4.025471,-5.380630,6.388563,-5.580738,-2.321382,3.108664,-3.382575,3.946969,-8.634434,-6.451182,5.151923,8.680228,-8.983020,4.890683,-9.649242,-6.572432,2.787806,-1.583638,-6.474602,2.610901,-6.509425,-9.280671,-0.765152,-4.640134,-3.150471,-2.679799,-8.730904,4.251858,4.155941,-9.649547,9.473977,5.802537,0.016477,0.172080,-2.396223,-1.363850,1.972503,1.719262,8.015730,6.690965,9.782471,8.766516,0.035566,-4.807822,2.443941,-5.679588,9.469369,7.156608,8.290625,-5.038065,-3.760035,2.917828,7.219182,1.441366,-9.797276,3.864003,-9.831522,6.664699,4.206109,-8.267940,1.034827,-0.141802,1.895631,1.395727,-5.123893,-0.209462,7.086947,0.779234,2.636361,5.825976,0.751713,8.124389,6.897625,8.277940,-1.201338,-7.737225,5.221242,4.799426,-8.986098,3.404064,-5.201014,2.186390,2.488325,9.812723,4.566439,4.522169,6.507616,3.190143,1.961440,4.919359,-6.796185,5.898033,-2.525201,-6.352337,-4.514012,-2.265643,-8.113388,-8.312459,-6.736141,-6.774700,-3.740705,-7.912904,-9.157763,-4.741339,-4.619260,4.172610,1.671207,-7.213766,5.517069,2.583735,3.385956,1.600113,2.593535,8.592049,1.360482,-2.030255,9.821676,7.927228,-9.733304,-3.366049,7.939802,9.033938,-7.116682,8.609395,7.862220,4.487816,-4.793419,-8.920413,-9.434072,2.771780,6.084754,1.776764,-7.943999,-2.543550,2.496940,3.517965,-5.724956,7.193031,0.442925,7.575453,8.844491,9.154295,4.542513,-0.705837,1.406441,8.976676,9.467286,-4.874306,2.298979,-2.509320,7.286486,1.968103,-8.880238,-0.832578,0.614468,-2.680256,2.107032,-1.222666,4.098351,-1.917780,-3.142929,1.564434,4.311948,6.031457,-6.178269,2.148219,-6.848514,-8.808729,9.084970,-3.646589,-9.992644,-8.033947,-4.594347,-2.067872,3.147088,-0.110698,-6.004707,0.076480,4.293993,-0.748182,-0.446799,9.106777,-7.873846,0.813339,2.905343,1.307073,3.691734,8.378654,-5.229185,2.112494,-0.182917,-5.564052,-1.447843,-2.926917,-9.776200,2.547716,-7.333202,2.094677,-8.959132,3.727886,-5.670745,3.451355,-9.984073,7.755317,-7.963496,-5.917822,0.233012,6.792729,-9.721157,1.595848,-8.141956,4.784132,-1.297116,-6.958209,6.308800,-1.155427,-8.270653,6.802861,-6.853471,6.199091,-4.350341,6.618148,-0.814616,6.028132,9.404578,-7.387154,7.460732,-1.462828,-8.955398,6.083365,-1.139772,-2.060092,9.628258,5.544746,-2.165541,0.577464,-3.481273,-5.058773,5.317188,9.883604,0.151014,1.907010,1.617379,-7.501167,-5.900847,-2.465816,1.638362,6.613724,-2.059158,-8.748271,8.091182,6.146503,-3.989159,3.508124,6.761972,-5.916372,-7.939528,-8.895973,-8.340863,0.425230,-9.357729,6.723815,-2.372393,-6.449301,-5.809828,-4.410973,-3.547521,2.180760,8.237055,2.583726,-9.123039,5.108580,6.305748,-7.684790,-3.680731,-4.541553,7.483281,-1.943239,-8.975031,9.983597,5.020770,-8.924946,1.478604,1.771003,-4.234460,-9.135174,-1.079113,6.677485,6.581478,8.016988,-4.636545,-0.493279,-9.022857,6.276216,2.507846,7.048025,-5.437445,5.732691,2.533137,8.826018,2.977334,-5.736570,9.312254,1.011186,-5.464404,8.018893,-6.508623,-2.096892,-0.067447,0.355128,-6.795280,5.845112,-3.607416,9.457076,8.238515,-1.503655,-8.655547,-9.086938,-5.741646,-8.045819,1.597307,0.041785,7.502579,-6.296895,-8.669038,3.848727,-4.597484,9.525725,0.657893,-9.636640,9.993492,9.153558,-9.107806,-0.198267,7.535620,3.009161,-4.801330,-9.079714,-8.726628,9.712612,-6.220076,-2.843658,0.264416,-4.013952,-0.087949,9.309779,0.810906,0.184203,0.531386,-2.079707,-5.968514,8.994897,7.988932,-0.572532,-9.565152,-8.349921,-3.592560,5.084211,-5.535520,1.263850,-6.252167,8.167193,6.751660,1.585967,-2.357359,-4.611851,3.263795,2.331382,2.041684,0.507988,5.548235,8.272442,-0.035748,-2.646687,-5.985532,6.098288,-6.929407,-0.195349,8.190592,-2.935362,1.203108,-2.765957,-5.863316,9.749609,0.383429,4.685440,-8.965759,-0.794367,9.587530,-8.545331,-8.077853,4.720731,-5.264653,7.977933,7.247563,2.387509,-6.462664,-4.990481,0.339680,-5.268860,-7.955699,4.545502,-3.329771,3.673307,-9.987913,5.321756,5.324113,-4.703012,-3.061060,7.883399,7.633519,2.745999,-1.269523,9.145489,1.425102,-6.912942,2.268990,2.087105,0.965145,-1.269244,-6.058817,2.908936,-4.606996,1.969913,3.748447,-7.806895,5.688111,-9.882543,2.026650,4.186209,1.873461,-1.215114,5.473819,1.613205,-0.435873,7.895005,0.555920,-7.535771,-9.890132,9.556567,-1.341503,-9.402860,7.098959,9.231653,-0.030797,9.164612,-0.399913,9.008181,3.268553,2.834967,-1.621627,-3.457683,4.445518,3.643248,-3.819933,4.456732,-1.375559,-3.488703,-7.137378,7.732988,-9.476526,-7.535511,-9.862691,6.707945,-9.339449,-0.568577,7.520435,8.643552,1.871899,-7.440185,9.392300,7.803843,1.401896,6.329599,7.112499,2.175290,6.692484,6.295209,3.252124,-6.118428,6.381286,-9.375272,6.250660,6.072664,-7.613949,9.368144,7.689796,7.034373,-0.838211,-2.575864,8.490113,-1.853741,7.008784,2.660184,-9.030183,9.482659,-4.391947,-9.237495,5.150579,-3.087466,9.654839,4.900724,-3.622219,7.588898,8.734874,2.107745,7.302615,1.117660,6.947796,4.522427,-2.563531,9.156882,-5.218158,7.920214,1.907733,9.003162,4.263751,9.919097,-7.563588,-7.268864,-3.622740,-1.767609,8.418234,-0.353971,-2.756486,-4.891048,-2.460416,1.683732,0.459633,-0.261015,2.860731,1.786391,-7.894625,-8.790992,-8.058873,-9.807778,-5.632161,-5.196140,1.972201,-8.340873,7.737446,-5.391935,-1.793962,-8.857883,-0.769308,-8.492865,8.800113,-2.890893,-1.305762,-1.292661,-2.383844,9.076936,7.477858,-7.478897,5.682553,8.144591,-7.988237,-5.577137,6.289475,-3.409596,-0.949610,4.470145,4.602035,0.612947,4.370197,-0.146726,7.459925,-7.828755,4.426393,2.517175,-2.472530,0.772596,-0.797024,2.017799,4.065412,-5.145481,1.417366,4.165733,8.712071,-0.066460,-8.840018,-8.783758,8.607011,-4.807011,-1.430111,1.980493,-1.209778,7.540717,-7.176488,8.767547,-9.771762,2.009455,1.827621,-0.539583,-6.225895,3.480635,2.253478,-6.685145,3.885113,-4.112136,-3.182629,-9.084295,-4.932748,9.121639,-1.399976,-4.665997,-9.783724,-4.884227,-2.943002,5.974869,-3.426222,9.479069,-8.139652,-4.275558,2.619897,9.801138,-9.860625,-7.285021,1.550745,1.944254,-8.631320,7.595434,-8.456599,7.063670,-1.408694,0.077187,9.984224,0.530820,-2.249884,4.957409,-6.704345,8.385841,-2.387765,8.618204,6.050074,-4.518696,8.024690,4.899960,1.688659,-5.737711,4.711409,-8.486535,5.959488,-7.218986,9.399962,1.118629,5.102459,-6.318464,-4.531002,3.542091,2.375321,-4.677752,2.502093,-4.347857,-7.332805,4.864765,-7.401534,-9.380576,6.847112,8.163662,8.592872,-1.825704,9.521254,-1.333548,-1.801055,5.837909,6.777395,-0.176940,4.836380,-7.917600,-5.812838,3.541843,3.189644,-4.119263,4.419141,-5.001428,-0.787849,9.706696,9.686826,0.975914,3.826900,0.740135,-4.982167,-3.279064,-6.811825,5.648829,-7.283116,1.086806,0.330863,-3.366496,4.765297,0.336272,9.347960,5.427291,-9.453030,-8.310165,-6.778748,3.110727,-8.124649,-2.079743,-8.785689,7.713096,4.412358,-7.037580,-6.662112,9.283800,1.529438,7.803829,0.892439,-5.190670,7.180699,7.693207,-0.717681,2.817661,-6.244332,-0.386047,1.157031,5.276527,-6.147539,9.641646,-1.553731,9.292479,5.283901,-3.530330,2.273491,5.661271,-4.747535,-5.827983,7.830424,8.539154,-9.596712,-0.812107,7.008366,-1.487659,4.424732,-5.237996,-2.413848,-9.983054,-6.823656,-1.797769,7.221833,-7.931280,-9.458478,-8.682262,-8.544113,-0.341733,4.805325,3.575839,-8.760088,7.774715,1.306649,-5.799122,9.442651,-4.558581,1.843687,1.292455,-8.058263,-5.557605,4.803366,-4.974130,-5.199583,-7.190115,8.376313,-4.999408,4.203836,6.169542,0.676995,-3.272026,-8.186217,-8.704712,8.115619,-6.167611,-2.137790,-7.265835,-7.248600,8.453899,0.148730,-6.859590,9.568535,0.543327,-9.331367,-3.568720,-7.919557,-3.097017,9.660638,-6.221723,2.729683,-2.924565,-6.723938,8.521988,6.074007,0.487005,-1.299070,2.780898,3.234579,-7.208217,3.800671,2.387880,5.102904,1.638026,6.929754,6.130278,-2.976237,-8.077661,-0.705307,6.723486,-3.577833,9.068875,0.900926,3.850983,0.937140,-3.329764,-4.440552,-4.686895,-6.281001,-9.752754,8.050011,-5.350547,5.180404,-7.300694,-9.814036,3.279786,1.975959,1.469814,4.103837,1.555977,-7.799845,9.060840,7.484977,-4.356078,6.663315,1.910369,-4.840678,9.046522,-8.344109,7.133670,5.710352,-6.163989,3.240062,9.867128,-1.422629,1.248727,5.435104,0.540916,-6.592221,-7.366772,-5.982220,8.081405,2.132038,-6.208577,-6.220992,-5.497230,-6.409066,-5.517936,-2.063745,-3.482708,-2.934239,9.273482,-3.013363,2.124531,-9.401203,8.482074,3.897087,3.144437,3.431663,1.184286,1.675485,9.720435,-4.521828,-3.656500,-5.162499,4.379680,-0.033355,-6.000383,8.881251,-3.993718,9.929416,-9.909523,-6.390746,3.153024,0.286904,0.933869,-4.580773,-4.654235,7.432297,9.481211,5.936231,-0.459658,6.731783,-0.205317,-8.499024,-9.165930,-8.459390,3.808450,-9.825630,-1.214464,1.650002,-2.753495,6.207208,-7.881855,9.025464,-2.509621,-7.038159,6.303083,4.542061,-0.265044,-4.718031,0.254858,4.049116,6.926568,3.973783,6.128318,8.353482,-4.778849,-9.834308,4.223644,-2.776253,-8.004341,2.193482,-4.318208,2.548783,-7.080270,6.329725,0.264896,-9.094813,-6.567173,-2.969901,-9.688975,9.948349,-9.214675,0.669172,-4.322723,6.855703,-1.936789,-3.012160,8.920884,6.978264,8.667219,2.100303,0.325375,5.829545,0.461029,8.110376,6.198378,-2.716016,-5.164499,-2.528337,8.106869,2.028716,-2.621958,-3.312347,-5.691247,8.466340,-1.775753,-7.338113,4.911774,6.161489,3.315231,-3.155428,-3.551953,6.626958,7.111652,8.545886,6.657924,-5.713125,-4.264661,-9.014436,8.666972,-9.245676,-8.667116,9.350077,-8.606620,0.345909,-5.795833,-2.703514,-8.961966,0.948140,7.023877,6.974479,-6.390160,-2.586886,-1.480816,1.561075,4.259834,-0.680771,-5.401651,2.692954,-7.946684,-3.697713,-6.042693,0.750593,-5.239177,-5.068465,6.905785,4.736697,-9.641420,-9.555550,-9.339930,-2.475396,7.583221,7.298183,-0.022565,-4.049085,4.208078,9.578566,-3.557624,1.971045,-5.861863,-8.008810,0.358960,4.220868,-7.885166,-7.580373,1.980824,-2.082532,0.801564,-0.734006,-8.882453,8.109500,4.000068,7.698421,8.787419,2.364141,0.962780,-2.227442,8.844164,-9.071213,7.460712,-6.581566,4.680722,-4.836963,-1.626849,-8.186064,7.044373,5.110165,8.332110,-0.167793,3.783798,-9.260842,-6.914313,8.132202,-7.564490,5.428830,-7.956476,-2.949062,-8.516272,5.809273,6.743415,7.120785,6.369283,3.542745,3.538072,4.050974,6.938731,6.830976,-0.733791,6.876736,-9.721830,1.699836,-5.778940,-4.013094,-0.171782,-2.723536,-8.382137,-7.006212,-6.197112,-4.333996,-8.235068,-6.190907,6.113577,5.051332,-7.656857,-5.525235,0.402168,2.992590,1.248430,-4.490814,5.669242,3.432177,-4.433744,9.632401,8.761267,-2.598602,-6.249794,-7.902663,6.614855,9.722483,-4.692593,-3.436398,2.885024,-3.940940,-6.723946,-3.516451,5.157554,2.926870,-2.628512,-8.644900,-3.996448,2.854961,6.241866,-9.351466,4.085160,-0.667982,3.138312,7.616923,-7.694686,0.540676,-6.186088,2.819105,4.230550,8.417559,7.243838,8.974330,-0.682285,-4.084363,-0.674566,-0.200229,4.138977,-1.130043,-5.034844,0.122787,6.832243,6.877312,0.982719,5.402639,8.395631,-5.602298,-8.204842,-3.790858,-3.312158,-7.397498,4.178343,-3.148376,1.729991,9.761433,-8.561762,-3.697550,6.231912,0.136557,-9.629114,1.953342,5.176917,5.138019,0.549170,-5.689743,-5.054611,2.997197,-8.735464,-7.432164,-8.364266,3.092947,6.355989,-1.213872,3.522889,6.922829,-0.148220,1.285032,-3.966696,0.692241,-1.252644,9.663266,-8.183223,-6.417381,-9.425879,-7.005137,-9.833106,3.826073,0.847324,-2.568165,9.879712,1.745411,-6.562808,0.838197,5.262004,-2.937148,-8.575545,-6.801618,-3.183063,8.530661,-3.760353,8.675513,5.081254,-7.471231,-9.400370,3.214602,-6.276941,0.772114,1.105186,5.118660,2.560057,-8.821400,6.858801,-2.840886,0.232090,-2.633101,9.175888,-0.798913,-0.166504,-8.954153,4.082477,-7.826154,-4.673942,-1.718248,-3.730956,-1.676052,-9.109065,6.195608,4.311494,6.219134,-1.010774,-9.713504,-4.559313,-7.209414,6.990475,5.089050,7.602704,-6.191390,-5.487189,0.501482,-4.086707,-7.193500,7.985394,-7.343717,-1.696261,0.390830,2.427905,-5.062696,6.985264,-2.753083,5.077688,9.506924,4.784765,-2.713048,7.491575,-5.202380,8.091421,-0.387030,1.120642,-6.540932,-2.480507,-2.168212,2.207823,9.457981,4.800923,-0.480522,-2.660626,6.064246,9.053619,1.684671,-6.317662,9.428656,-3.749124,-0.092872,-8.560270,7.173186,-1.709003,9.846160,0.448837,-0.886581,-9.592447,4.702948,3.249426,6.896289,0.457294,5.522736,-7.230396,9.219169,-5.330114,-3.107153,-1.721112,0.923684,6.579485,7.313735,-1.611674,-7.437623,-0.219181,7.420014,-2.434882,-1.865493,4.159375,6.444638,-1.504360,-5.777302,-9.488166,-4.850894,3.817995,-5.033065,-7.762510,0.371215,0.622399,1.932078,1.940965,5.802440,3.383226,8.248554,8.580173,1.345336,-1.174535,-0.185816,-2.724202,8.824648,2.604925,4.787512,8.278806,-2.779377,-0.167918,-4.565786,-1.496412,9.805201,-7.129502,-7.324085,-0.554404,9.355944,4.998720,8.043396,-2.964988,7.244377,-4.183649,0.160636,4.607875,8.555772,-6.684642,-8.896524,6.657457,-4.344370,-3.053174,-6.930529,-5.452875,6.669896,4.500173,-5.605814,-0.436442,9.027117,-9.279313,-2.157391,-1.813212,2.389068,-6.825442,3.747611,8.763737,4.513747,-4.573731,-4.497862,0.047704,1.484307,3.709070,5.417697,9.200371,-0.474332,1.120741,-3.753408,-6.533478,-7.542676,9.045027,4.884159,-8.519253,-9.290955,-3.158044,8.836156,2.113610,-7.987640,-3.373180,-4.873648,5.564335,3.179478,2.430216,-3.357824,7.678109,-7.252805,2.200331,-4.295189,-2.761521,-1.363330,4.259666,9.701688,-4.601583,5.316735,2.361654,8.815945,4.935592,4.904495,-3.208336,-7.807794,2.942197,-4.077538,-1.945855,-1.247453,1.532880,5.772653,-1.633283,4.678419,8.372339,-7.287565,-6.702696,6.956422,-2.593858,8.280228,-7.750723,4.926010,-7.217989,-1.507018,-7.021597,-6.129430,-1.593259,-2.774426,-8.616989,6.715883,5.504582,-0.288940,3.988173,1.248483,-6.267251,-7.065076,-7.244106,-2.062306,6.595642,-3.768006,3.592653,-8.003978,-5.403572,8.575877,-5.236313,-2.742554,-4.996704,-6.253761,-7.305978,9.870920,-4.402802,-9.358182,4.905143,4.378138,1.841691,-5.177715,-1.903066,-1.797209,-5.614377,1.148513,9.183872,-2.152381,-6.049464,5.347106,-8.760336,-1.042372,1.965667,5.800149,9.624603,7.921792,-0.527084,-0.946875,-2.021558,-5.233261,-2.204612,-3.412754,2.372674,4.941442,3.112359,8.539942,8.327367,-5.415359,-6.907221,-3.476320,-7.726055,-0.155543,0.755040,-1.005244,-7.100821,-1.597643,-8.850784,-0.793220,2.301819,-3.443215,-6.541824,-3.836476,0.821402,-7.049527,9.842474,3.383704,7.374446,-8.680432,-9.993644,-6.730046,0.181135,4.178377,1.996849,-1.061763,2.975061,5.847134,-4.900867,-3.432771,-6.029972,7.648329,4.199770,-2.851490,-8.107807,4.540072,8.127268,7.673493,1.109843,-6.848177,-9.174085,0.981676,2.878057,-4.053629,4.942877,7.275418,9.562822,7.895752,-3.211287,3.160632,-9.479359,7.427452,3.117028,0.266568,-7.371053,3.662856,-4.748989,-6.361159,-5.584235,0.017450,6.254125,5.558317,0.507595,8.676733,-1.899232,-2.767012,-3.059673,-6.918541,3.241747,-9.356566,-2.268767,-0.211450,-1.844175,-9.755486,9.726890,-9.448563,5.440832,-4.215970,-1.009304,-9.004807,-0.234805,-7.574032,-8.311386,-8.788662,-8.975764,6.723372,9.022228,1.087895,2.140795,-1.707546,7.162212,7.553519,-9.697336,9.785148,-1.481601,-0.708472,-1.770212,1.513729,0.992447,-2.843180,-7.929635,-0.301456,-3.825399,4.843945,-2.685468,-0.799965,3.036654,-8.320954,9.485413,-7.396979,2.705130,2.245827,9.908811,-4.228890,-4.894762,-4.610038,5.062212,-8.184103,-8.414820,8.390463,9.543559,-4.403474,3.587040,8.424259,-9.128820,-8.115613,-0.731921,-9.774707,-7.735659,-9.523223,0.135468,1.735359,-6.456796,-1.880239,-7.973497,3.061443,-6.095881,-1.975794,-4.827489,-3.966032,8.021706,-7.743671,-1.577536,-8.364230,9.789971,-2.858351,1.326408,4.681834,7.344907,6.591428,3.270949,-8.823886,-7.208026,-6.174389,-2.615611,-6.772257,7.971134,3.112886,2.309457,0.228118,-3.037768,0.618954,0.096403,4.504414,0.037306,-9.751251,4.746508,-2.873641,7.453014,-2.399954,7.582967,-6.804816,1.719510,0.411527,7.379182,-0.352682,-2.343857,8.561024,-5.744622,-6.878800,5.620357,7.477113,5.797296,8.970664,-3.173449,-7.294676,-0.342162,-9.837622,-5.886411,-8.144394,-4.532505,-6.880923,-4.776980,6.074405,-6.762380,-4.391822,-2.676396,4.493564,1.663882,0.836946,-3.042516,-9.994727,-2.790014,3.995522,-4.428626,-7.530647,-7.832337,3.134531,-4.638915,0.558117,-6.624230,5.894863,9.317829,2.431090,4.248718,-7.795758,-7.245502,-3.804728,-4.136123,-3.124446,4.244294,8.758294,7.740050,-3.898622,6.987270,-4.275063,-3.631384,3.583523,-0.701985,-6.443892,4.950888,-9.760720,8.390971,-2.706737,-7.895988,-5.880804,2.566347,3.961503,-5.588418,-6.836018,4.502211,-1.058292,-8.980978,-1.459490,-0.874311,-5.486044,4.450390,4.504245,5.691483,-3.470859,-1.905780,7.095975,2.414462,-7.169564,4.951210,4.693570,-6.052695,-8.441342,5.010992,3.899077,1.717869,3.429468,-4.710376,-3.071294,-8.772628,0.295139,6.994123,-5.096353,4.794781,1.684174,-3.791949,-0.770521,-5.067416,2.578108,6.391851,4.171446,5.253558,9.395526,7.776227,6.573624,6.283372,8.843882,-4.000157,8.179711,-2.227705,-3.789557,3.813351,5.020206,7.823866,-4.817628,-2.593515,4.449672,-2.879280,7.703101,-0.542705,-2.463450,-6.578211,0.360432,6.785390,-3.202587,9.090501,-3.743047,1.977989,-6.485748,4.731483,8.814034,-7.371255,4.197188,-1.337960,-7.140695,1.946390,-7.824704,-3.471825,-3.030552,-1.551549,-0.126578,8.919356,-7.138540,-8.695062,5.606127,7.878811,8.868281,-8.437785,8.053844,-4.659228,9.185902,-1.304774,7.092529,5.226426,-3.655818,-8.326303,5.019687,-0.895230,7.193480,-0.857903,-0.171058,3.204055,7.497385,-6.222390,-5.796392,5.884219,-2.155530,2.302738,-6.569920,-0.737487,-3.292671,1.131812,-7.150368,-2.142300,7.886515,5.160438,-3.474081,9.676190,-8.815696,-1.507936,-6.094212,-7.622279,3.477712,-1.922633,4.040948,8.876837,-3.724219,4.553772,-3.779652,-0.215049,9.766065,9.414855,-6.637456,2.865938,-9.712685,-8.257750,6.493896,8.283720,-9.515790,6.417701,-6.173226,-9.391648,0.337472,-6.585010,5.349369,8.593713,-9.399038,-9.794055,-7.278749,8.850450,-3.230838,7.549241,-4.584870,-7.706844,4.978093,-7.225420,-6.461728,-8.792920,9.887498,6.350485,3.495929,2.015147,7.225481,-3.070448,1.597227,-2.968880,8.255673,-0.426858,7.440827,1.382203,-6.657062,-8.933266,-1.840266,-9.583369,7.508245,-1.360481,5.673954,-6.884227,3.482899,-9.652949,-7.691990,-0.938426,-6.852305,-3.244381,-0.449408,-1.730665,7.951545,0.383012,9.811707,7.235521,-7.043370,9.862497,1.793510,-8.558789,2.387938,-8.468182,-8.314685,1.557869,8.796241,-6.801724,2.378987,-4.707444,7.008049,-6.323197,7.307662,-1.439153,9.278821,8.061227,8.817510,-5.726413,-5.679023,3.741270,4.589067,-1.708466,-1.121558,-0.983173,1.561586,-8.423614,2.632858,-9.479743,3.817588,-3.552711,-1.985707,8.004644,5.527269,-7.185974,-8.622921,-4.404752,4.813702,-8.024765,9.406705,0.488269,4.411248,-1.070371,7.031206,-3.914995,6.476498,0.452008,-6.257315,3.879578,-3.640250,-4.524181,6.011426,6.436317,3.026452,-1.376157,-4.317170,3.991115,-2.396271,-6.719264,-7.031304,-5.007322,1.155904,-3.178789,-2.530141,-2.234142,6.768214,-6.228517,4.810935,8.269880,9.830619,-8.290619,-5.387846,-2.353261,4.910712,-0.530710,1.369495,2.429438,-1.194555,-5.829026,2.146750,-1.127367,5.396362,-9.919123,-6.670750,0.060524,9.542419,6.501453,-1.108617,-3.123531,9.990342,5.654823,4.166689,0.337090,-4.444939,8.895423,-4.913995,0.016475,-6.113669,3.676644,8.228198,-5.368903,-1.715427,-0.694408,9.475575,-4.686149,5.035469,6.235203,-6.977009,5.715967,0.409992,-1.418157,-5.622742,5.064657,1.962459,9.030183,-7.044206,-0.735426,4.961173,9.034415,2.648137,8.502191,5.865563,-5.520264,-2.443794,3.885892,-0.280381,5.208151,0.847072,8.106386,7.774413,8.396185,-8.173963,-0.053482,6.280984,7.063619,8.801724,2.885727,5.050062,-5.146496,2.529556,0.050220,-9.744220,-9.433616,-2.662622,-8.908785,-7.599468,7.665703,9.750158,4.948845,2.270091,-6.740101,7.183614,2.452086,3.332123,-3.212238,0.043443,-7.940861,7.811198,9.530949,-6.401853,7.884878,-1.885705,1.937043,3.889648,-9.548783,4.217598,1.271708,-7.478015,-5.807596,8.392096,1.510170,-0.467829,-3.038248,-6.761116,8.575818,6.526319,-2.733192,4.780698,-1.940740,-0.074129,7.686941,9.849488,-0.015007,-6.016191,6.456326,-5.599567,-9.149456,-7.266947,-0.042714,7.378637,4.258291,-9.572945,-4.653311,4.465565,-4.911708,3.922897,-9.925235,3.403453,-6.601878,7.924376,3.548901,-2.925902,-3.967941,-1.467093,-9.466144,5.333558,-0.314698,1.100841,6.872102,1.843341,-0.731341,-6.756672,3.399953,8.986118,0.491121,5.489772,-5.612373,-3.577467,-5.574094,6.060591,-4.994125,-1.476884,1.611607,2.449321,8.874430,-6.863802,7.521466,-6.994410,-5.521766,5.130635,-7.710868,-8.082554,-6.654885,3.336962,9.376086,5.916882,2.341954,0.139456,7.332465,-8.777083,0.100350,-6.152392,7.575161,-6.981733,1.822091,1.828975,-4.274891,-3.104279,-7.918476,-9.928537,4.238877,-0.051172,5.475231,9.702266,-8.814090,4.469825,-6.440534,2.726296,-0.949542,-1.977931,8.800989,3.993436,2.112562,-0.912123,-2.645016,-3.173897,1.294884,-0.799533,-3.326373,1.346369,4.742287,-4.199286,4.432680,8.869639,6.766340,3.559639,3.267454,3.968824,-9.656952,7.853812,-1.042147,-5.846175,-6.378576,-7.649316,-7.355769,4.005620,3.393425,-2.358802,7.811537,-8.422537,2.888110,6.836544,1.732458,5.179542,6.851215,-1.236769,-4.991244,6.486352,6.434102,3.465366,4.863960,-7.888670,8.894059,1.064345,-7.856876,5.055189,4.595568,4.856836,7.521161,1.508487,5.720955,-0.485025,-9.321491,-2.203782,-7.277548,-9.263726,-4.570237,-6.541529,4.209078,1.391542,9.853527,1.522253,4.534690,9.485795,4.363624,5.129053,-9.939028,1.041307,9.553570,2.491279,6.147309,-5.149424,-7.442833,3.607417,-2.370546,8.028051,-4.184128,0.468032,8.550630,-1.006820,6.286872,4.861588,-5.684041,-2.313323,-7.766219,8.390652,2.140236,-3.104055,-8.107283,7.778423,-0.787945,-2.809246,1.806632,-4.453140,8.158680,-8.486464,8.492110,-1.247264,-2.784439,8.035116,-3.638648,-0.851135], dtype = "float32")#candidate|4027|(2880,)|const|float32
var_4028 = relay.var("var_4028", dtype = "float64", shape = (20,))#candidate|4028|(20,)|var|float64
call_4026 = relay.TupleGetItem(func_2463_call(relay.reshape(call_4007.astype('float32'), [10, 10, 2]), relay.reshape(const_4027.astype('float32'), [2880,]), relay.reshape(var_4028.astype('float64'), [20,]), ), 2)
call_4029 = relay.TupleGetItem(func_2467_call(relay.reshape(call_4007.astype('float32'), [10, 10, 2]), relay.reshape(const_4027.astype('float32'), [2880,]), relay.reshape(var_4028.astype('float64'), [20,]), ), 2)
uop_4045 = relay.cos(const_4027.astype('float32')) # shape=(2880,)
func_1699_call = mod.get_global_var('func_1699')
func_1701_call = mutated_mod.get_global_var('func_1701')
const_4052 = relay.const([-0.614484,3.057683,-0.999940,-2.591028,-3.444796,8.486607,-9.299290,-6.036074,2.316762,7.920319,-2.127803,-7.342297,-6.832901,5.135579,-5.638982,-8.387938,-8.775510,5.454260,8.095940,-0.391420,3.432414,7.758360,-1.120267,-9.511587,8.875785,9.520659,6.708197,-0.549823,-5.167776,-5.569049,5.910339,7.486862,-1.511745,-0.116602,-3.942678,9.863779,1.947117,-0.844461,7.932649,2.838856,-5.507851,-8.672703,7.869869,-6.499031,-7.060775,-8.122034,3.894047,-8.677741,-4.535296,6.761342,4.726565,-6.785155,9.900504,1.657880,4.385064,-8.851113,7.098915,-5.721550,6.116211,-7.529180,5.931190,4.997208,2.190676,-7.637921,8.996101,-2.158642,-2.587246,4.301811,6.085816,-7.388563,2.945308,4.614411,-6.026416,2.408265,-4.264446,2.031137,-4.032788,-3.635452,-0.912912,-7.283954,-9.546098,3.451794,1.330411,-3.016717,6.086829,-1.768371,8.871014,0.783194,7.203724,0.992209,6.691725,7.001368,-1.979745,4.079016,-3.082391,-3.148270,-1.065344,0.023329,-0.776670,5.656574,6.317241,-0.172939,1.555866,-5.284373,6.508521,-3.046240,-0.914138,-6.763723,8.895847,-3.880848,9.514605,-9.025962,-4.242940,-6.187293,8.846174,-8.931164,7.953483,-5.109579,-7.708292,3.731101,-8.059648,-4.483453,3.598145,1.814982,-5.361839,-5.416011,-2.145935,-1.939312,-1.864271,0.969490,-0.103588,-6.187787,0.354545,-7.908059,6.790940,8.369195,7.084283,3.237999,-7.357480,4.321998,-8.436056,7.041627,-5.746561,1.956642,-5.689579,-1.645713,-2.431786,-1.938171,9.114151,7.013337,-9.781094,7.764920,2.609418,-8.671337,2.343179,-0.360365,5.729874,3.427976,7.017127,-1.809637,5.219281,-2.917412,-2.448262,0.580644,7.593520,-5.354615,5.625475,2.542605,-8.269586,1.005805,4.975761,1.469695,1.163248,-1.778105,2.666136,-8.312168,-0.636663,-5.914402,4.355319,-6.749354,4.543474,-1.667334,-6.868468,2.988035,8.853127,1.959120,-8.513377,4.025890,8.363332,6.754111,-0.933544,0.537116,-2.797912,0.791702,-6.388860,3.046236,1.368260,-6.181103,7.056959,-7.469006,-8.969899,-8.010501,3.417772,-5.165208,2.038872,8.920719,2.318364,-3.542884,4.041989,2.610801,-3.315702,5.940504,-2.012449,2.050738,5.431509,-4.054541,7.965726,-0.499001,-9.683934,1.042035,-5.120226,-1.452219,-1.801647,-0.929951,-4.215113,7.649061,-8.282523,-7.379538,-2.604956,-4.123336,-9.408485,-9.705088,0.923660,-4.055556,4.295365,-3.545212,-1.244961,-6.506480,7.378856,-5.560420,-0.767594,-2.306874,-8.034075,-2.109087,8.612124,-8.160891,5.741929,0.407780,-6.087447,1.623484,-3.238117,3.566715,-0.161361,0.900359,-9.830391,2.108676,9.863168,6.008969,2.981024,-4.675042,7.758435,-2.811133,1.901086,8.323219,8.446842,-8.973158,-6.501483,-0.651157,3.421396,8.598487,-4.297265,-5.602927,-8.488418,7.801773,6.914961,-5.516176,6.270081,-1.395723,8.527104,-2.087009,-8.356325,-6.932360,-3.709325,8.320530,-7.245020,-8.606688,1.217778,-2.426500,-9.320285,8.446637,9.006252,-1.795167,-4.633307,-7.439175,0.115492,-9.492290,6.905663,-7.105920,-0.284519,8.335642,-9.194208,3.989667,-2.022261,-1.321565,0.972781,8.986143,1.540339,8.910876,-9.826739,4.545460,-0.645304,8.059219,-9.275612,-1.570351,1.445351,3.138014,4.622299,8.573554,-4.208180,-3.259330,-5.391708,6.044138,-0.394700,4.411225,-0.180641,-6.901507,1.158614,-4.318786,0.575426,-0.351001,-3.699105,4.960462,-4.187677,4.754762,-6.419238,-2.811065,5.928944,-7.787529,5.253849,-9.044947,3.602015,-0.236164,-0.081673,-3.221016,0.479616,-6.454131,5.492421,9.891245,8.714235,-3.289819,3.884751,-5.390335,-1.168640,-5.747912,-3.337788,9.410716,6.230352,-4.978990,-9.736316,5.038245,0.995481,6.922990,0.440392,-6.716709,-9.866746,-7.380412,-6.605282,-7.290239,-7.924629,-1.698540,-9.386959,-7.740288,6.311946,4.327337,9.111449,-4.241633,4.362807,5.096655,-4.081673,4.757534,5.896754,-9.003842,-2.559180,-1.094525], dtype = "float32")#candidate|4052|(384,)|const|float32
call_4051 = func_1699_call(relay.reshape(const_4052.astype('float32'), [3, 16, 8]))
call_4053 = func_1699_call(relay.reshape(const_4052.astype('float32'), [3, 16, 8]))
output = relay.Tuple([call_4007,call_4026,var_4028,uop_4045,call_4051,const_4052,])
output2 = relay.Tuple([call_4008,call_4029,var_4028,uop_4045,call_4053,const_4052,])
func_4063 = relay.Function([var_4028,], output)
mod['func_4063'] = func_4063
mod = relay.transform.InferType()(mod)
var_4064 = relay.var("var_4064", dtype = "float64", shape = (20,))#candidate|4064|(20,)|var|float64
output = func_4063(var_4064)
func_4065 = relay.Function([var_4064], output)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3132_call = mutated_mod.get_global_var('func_3132')
call_4070 = relay.TupleGetItem(func_3130_call(), 1)
call_4071 = relay.TupleGetItem(func_3132_call(), 1)
output = relay.Tuple([call_4070,])
output2 = relay.Tuple([call_4071,])
func_4112 = relay.Function([], output)
mod['func_4112'] = func_4112
mod = relay.transform.InferType()(mod)
mutated_mod['func_4112'] = func_4112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4112_call = mutated_mod.get_global_var('func_4112')
call_4113 = func_4112_call()
output = call_4113
func_4114 = relay.Function([], output)
mutated_mod['func_4114'] = func_4114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3603_call = mod.get_global_var('func_3603')
func_3604_call = mutated_mod.get_global_var('func_3604')
call_4129 = relay.TupleGetItem(func_3603_call(), 0)
call_4130 = relay.TupleGetItem(func_3604_call(), 0)
uop_4140 = relay.atan(call_4129.astype('float32')) # shape=(10, 10, 2)
uop_4142 = relay.atan(call_4130.astype('float32')) # shape=(10, 10, 2)
output = uop_4140
output2 = uop_4142
func_4165 = relay.Function([], output)
mod['func_4165'] = func_4165
mod = relay.transform.InferType()(mod)
mutated_mod['func_4165'] = func_4165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mutated_mod.get_global_var('func_4165')
call_4166 = func_4165_call()
output = call_4166
func_4167 = relay.Function([], output)
mutated_mod['func_4167'] = func_4167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2676_call = mod.get_global_var('func_2676')
func_2678_call = mutated_mod.get_global_var('func_2678')
call_4170 = relay.TupleGetItem(func_2676_call(), 0)
call_4171 = relay.TupleGetItem(func_2678_call(), 0)
var_4177 = relay.var("var_4177", dtype = "float64", shape = (10, 14, 2))#candidate|4177|(10, 14, 2)|var|float64
bop_4178 = relay.not_equal(call_4170.astype('bool'), var_4177.astype('bool')) # shape=(10, 14, 2)
bop_4181 = relay.not_equal(call_4171.astype('bool'), var_4177.astype('bool')) # shape=(10, 14, 2)
output = relay.Tuple([bop_4178,])
output2 = relay.Tuple([bop_4181,])
func_4188 = relay.Function([var_4177,], output)
mod['func_4188'] = func_4188
mod = relay.transform.InferType()(mod)
mutated_mod['func_4188'] = func_4188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4189 = relay.var("var_4189", dtype = "float64", shape = (10, 14, 2))#candidate|4189|(10, 14, 2)|var|float64
func_4188_call = mutated_mod.get_global_var('func_4188')
call_4190 = func_4188_call(var_4189)
output = call_4190
func_4191 = relay.Function([var_4189], output)
mutated_mod['func_4191'] = func_4191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1321_call = mod.get_global_var('func_1321')
func_1322_call = mutated_mod.get_global_var('func_1322')
call_4230 = relay.TupleGetItem(func_1321_call(), 2)
call_4231 = relay.TupleGetItem(func_1322_call(), 2)
output = relay.Tuple([call_4230,])
output2 = relay.Tuple([call_4231,])
func_4232 = relay.Function([], output)
mod['func_4232'] = func_4232
mod = relay.transform.InferType()(mod)
output = func_4232()
func_4233 = relay.Function([], output)
mutated_mod['func_4233'] = func_4233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1613_call = mod.get_global_var('func_1613')
func_1615_call = mutated_mod.get_global_var('func_1615')
call_4257 = relay.TupleGetItem(func_1613_call(), 0)
call_4258 = relay.TupleGetItem(func_1615_call(), 0)
output = call_4257
output2 = call_4258
func_4263 = relay.Function([], output)
mod['func_4263'] = func_4263
mod = relay.transform.InferType()(mod)
output = func_4263()
func_4264 = relay.Function([], output)
mutated_mod['func_4264'] = func_4264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3342_call = mod.get_global_var('func_3342')
func_3343_call = mutated_mod.get_global_var('func_3343')
call_4297 = func_3342_call()
call_4298 = func_3342_call()
output = call_4297
output2 = call_4298
func_4300 = relay.Function([], output)
mod['func_4300'] = func_4300
mod = relay.transform.InferType()(mod)
mutated_mod['func_4300'] = func_4300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4300_call = mutated_mod.get_global_var('func_4300')
call_4301 = func_4300_call()
output = call_4301
func_4302 = relay.Function([], output)
mutated_mod['func_4302'] = func_4302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_4350 = func_2377_call()
call_4351 = func_2377_call()
output = relay.Tuple([call_4350,])
output2 = relay.Tuple([call_4351,])
func_4352 = relay.Function([], output)
mod['func_4352'] = func_4352
mod = relay.transform.InferType()(mod)
output = func_4352()
func_4353 = relay.Function([], output)
mutated_mod['func_4353'] = func_4353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3342_call = mod.get_global_var('func_3342')
func_3343_call = mutated_mod.get_global_var('func_3343')
call_4354 = func_3342_call()
call_4355 = func_3342_call()
func_4165_call = mod.get_global_var('func_4165')
func_4167_call = mutated_mod.get_global_var('func_4167')
call_4364 = func_4165_call()
call_4365 = func_4165_call()
func_2178_call = mod.get_global_var('func_2178')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_4370 = func_2178_call()
call_4371 = func_2178_call()
func_3603_call = mod.get_global_var('func_3603')
func_3604_call = mutated_mod.get_global_var('func_3604')
call_4373 = relay.TupleGetItem(func_3603_call(), 0)
call_4374 = relay.TupleGetItem(func_3604_call(), 0)
output = relay.Tuple([call_4354,call_4364,call_4370,call_4373,])
output2 = relay.Tuple([call_4355,call_4365,call_4371,call_4374,])
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
func_4263_call = mod.get_global_var('func_4263')
func_4264_call = mutated_mod.get_global_var('func_4264')
call_4426 = func_4263_call()
call_4427 = func_4263_call()
func_3046_call = mod.get_global_var('func_3046')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_4430 = relay.TupleGetItem(func_3046_call(relay.reshape(call_4426.astype('float32'), [200,])), 0)
call_4431 = relay.TupleGetItem(func_3048_call(relay.reshape(call_4426.astype('float32'), [200,])), 0)
func_4352_call = mod.get_global_var('func_4352')
func_4353_call = mutated_mod.get_global_var('func_4353')
call_4477 = relay.TupleGetItem(func_4352_call(), 0)
call_4478 = relay.TupleGetItem(func_4353_call(), 0)
output = relay.Tuple([call_4426,call_4430,call_4477,])
output2 = relay.Tuple([call_4427,call_4431,call_4478,])
func_4484 = relay.Function([], output)
mod['func_4484'] = func_4484
mod = relay.transform.InferType()(mod)
mutated_mod['func_4484'] = func_4484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4484_call = mutated_mod.get_global_var('func_4484')
call_4485 = func_4484_call()
output = call_4485
func_4486 = relay.Function([], output)
mutated_mod['func_4486'] = func_4486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_4490 = relay.TupleGetItem(func_1716_call(), 0)
call_4491 = relay.TupleGetItem(func_1717_call(), 0)
output = relay.Tuple([call_4490,])
output2 = relay.Tuple([call_4491,])
func_4495 = relay.Function([], output)
mod['func_4495'] = func_4495
mod = relay.transform.InferType()(mod)
output = func_4495()
func_4496 = relay.Function([], output)
mutated_mod['func_4496'] = func_4496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4263_call = mod.get_global_var('func_4263')
func_4264_call = mutated_mod.get_global_var('func_4264')
call_4511 = func_4263_call()
call_4512 = func_4263_call()
func_3189_call = mod.get_global_var('func_3189')
func_3191_call = mutated_mod.get_global_var('func_3191')
call_4516 = relay.TupleGetItem(func_3189_call(), 1)
call_4517 = relay.TupleGetItem(func_3191_call(), 1)
output = relay.Tuple([call_4511,call_4516,])
output2 = relay.Tuple([call_4512,call_4517,])
func_4523 = relay.Function([], output)
mod['func_4523'] = func_4523
mod = relay.transform.InferType()(mod)
output = func_4523()
func_4524 = relay.Function([], output)
mutated_mod['func_4524'] = func_4524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4167_call = mutated_mod.get_global_var('func_4167')
call_4525 = func_4165_call()
call_4526 = func_4165_call()
func_2377_call = mod.get_global_var('func_2377')
func_2379_call = mutated_mod.get_global_var('func_2379')
call_4527 = func_2377_call()
call_4528 = func_2377_call()
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_4533 = relay.TupleGetItem(func_2402_call(), 2)
call_4534 = relay.TupleGetItem(func_2404_call(), 2)
output = relay.Tuple([call_4525,call_4527,call_4533,])
output2 = relay.Tuple([call_4526,call_4528,call_4534,])
func_4552 = relay.Function([], output)
mod['func_4552'] = func_4552
mod = relay.transform.InferType()(mod)
mutated_mod['func_4552'] = func_4552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4552_call = mutated_mod.get_global_var('func_4552')
call_4553 = func_4552_call()
output = call_4553
func_4554 = relay.Function([], output)
mutated_mod['func_4554'] = func_4554
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4618 = relay.const([[[4,-7,-1,3,-7,-2,-7],[9,7,-7,7,2,-4,-4],[-9,-8,-10,-9,8,-2,9],[1,3,10,-2,-2,10,-2],[10,-1,-7,-9,-6,8,10],[-8,6,-5,-9,-2,-1,2],[10,-6,-2,-9,-5,-5,-7],[-4,-5,-6,-4,-1,-7,6],[7,9,-1,-10,-1,-1,-7],[9,1,1,-6,8,-9,4],[4,-3,-7,-2,9,-3,-1],[9,3,2,-1,-4,3,8]],[[-3,-7,2,9,4,10,-3],[6,-7,2,10,8,8,-10],[-3,2,-1,-2,10,-2,3],[2,5,10,10,4,5,-3],[1,3,-2,-2,3,-5,7],[1,-1,8,8,8,7,2],[-5,2,-8,1,-9,2,7],[8,7,6,2,-4,9,10],[7,7,-7,-7,3,5,-1],[5,-4,-3,-2,-1,-10,-7],[-8,-4,-9,8,-9,10,-4],[-5,10,4,5,-7,4,-3]],[[2,3,9,6,6,3,-8],[7,-8,7,-6,-3,6,-10],[-5,-5,5,6,3,1,5],[-7,8,5,8,-5,-2,-7],[-10,1,2,-2,-3,-10,-2],[8,-6,2,-8,-10,-10,-3],[5,3,7,-1,-9,5,-3],[10,7,-5,-2,-6,4,9],[3,6,-1,5,2,-4,-9],[3,-5,9,3,-4,-1,-7],[8,-8,-9,-1,7,6,-2],[-10,-1,-4,8,-10,-7,7]],[[-7,-4,-4,8,-1,4,4],[5,2,6,-2,2,6,-2],[8,-3,-6,2,9,3,-8],[6,-9,-6,10,-8,2,4],[-4,3,8,9,-10,5,-10],[1,-7,7,-2,1,-5,-4],[-1,-7,5,-8,-5,-8,-9],[-6,1,-8,6,6,-8,-10],[6,-4,-2,-3,-2,-1,-10],[-1,4,-10,7,-3,3,3],[-6,8,6,-10,-4,7,-4],[10,9,-4,1,8,-2,-4]],[[-2,-8,-9,2,-8,-4,-5],[-6,-1,-2,-8,-5,-10,10],[8,7,-1,10,-9,5,-5],[10,4,-7,-2,7,-5,2],[9,-7,4,-7,-7,4,9],[5,-10,4,-1,-9,1,-5],[-2,4,-9,-8,-3,9,-4],[-7,-4,-9,-9,8,-5,5],[7,-6,6,-8,-1,7,3],[-7,9,-10,-8,7,1,7],[4,-5,1,8,1,4,6],[7,9,4,8,1,2,-5]],[[-5,2,4,10,9,5,-8],[2,-10,3,5,-7,3,10],[8,-10,-8,2,-8,-7,2],[6,3,-4,-1,4,4,8],[1,-5,-1,-10,7,-1,4],[-1,2,-8,7,9,1,-3],[-5,4,-9,5,-4,-9,6],[-6,-9,-9,-8,9,-1,5],[-2,-10,-7,4,-3,-8,-3],[8,8,-10,-2,-2,-7,6],[-9,-1,7,-7,4,-4,10],[4,8,3,-5,-7,-1,7]]], dtype = "int32")#candidate|4618|(6, 12, 7)|const|int32
const_4619 = relay.const([[[-4,-8,6,-4,6,-1,3],[9,4,-5,3,-2,7,-6],[8,5,-10,8,-10,3,2],[-4,3,-1,5,-5,-7,-5],[7,-1,7,-10,-10,-2,-1],[-8,-1,10,-6,-5,6,-1],[-7,9,-2,-2,8,-7,-8],[-1,-6,-2,1,-4,-2,10],[-9,2,1,-9,-2,1,10],[-10,-7,-9,-8,-1,-2,8],[4,-1,8,8,-5,-2,7],[-10,-1,9,-1,-2,-9,10]],[[10,7,-3,-6,2,-2,-10],[-7,-8,-5,-7,-7,-3,7],[-4,7,-4,-9,-3,-10,10],[3,4,6,-6,1,7,10],[-6,6,-6,7,5,7,-2],[2,-8,-1,-4,-6,-10,-4],[4,-1,-2,4,9,-10,-7],[4,-3,-1,-3,5,9,-8],[6,-8,-7,-3,-3,9,-8],[8,-5,5,9,8,6,9],[-3,-4,10,-1,8,-8,-3],[-5,-5,4,-5,7,-5,-6]],[[-6,-6,-4,10,-10,-1,-9],[9,7,10,-9,1,5,8],[10,-1,-10,7,-7,8,-2],[-6,-9,10,1,7,6,3],[-5,-3,6,-3,-3,2,1],[-9,-10,-1,-4,-6,-3,-6],[-2,-4,2,2,-3,8,-7],[-8,-10,-1,-4,1,5,4],[2,-1,-8,1,-2,10,8],[-1,-8,-3,-8,9,7,1],[-1,2,-2,10,-7,2,4],[3,9,6,5,-6,-4,-4]],[[-8,4,7,-5,-10,10,5],[-7,3,-10,-5,4,6,10],[6,2,6,-5,4,3,4],[1,5,-8,-9,-5,-3,-4],[-8,8,8,-7,-5,-9,-2],[-3,6,-8,4,-1,2,-7],[2,5,-6,3,-4,8,5],[-8,-2,5,-5,-8,9,-1],[-5,8,-10,7,-8,9,1],[9,9,-4,8,-8,2,-1],[-5,-4,1,-8,-4,8,-3],[2,-6,-1,10,-3,-7,-3]],[[-7,2,9,2,5,-2,3],[1,-4,-2,-5,5,-8,-6],[-9,4,5,8,1,3,-8],[-6,-4,-6,1,-1,3,-4],[4,6,2,9,-7,1,-5],[-5,-1,3,-10,-4,-9,9],[-10,-2,6,-6,-1,6,-2],[-5,5,-9,3,-2,2,-5],[-2,4,-1,4,6,8,7],[-5,-2,5,4,-4,5,-1],[-3,-10,5,6,-2,-5,-4],[-6,-6,-9,5,6,5,6]],[[7,9,-8,-6,4,-8,4],[-5,-4,-9,-5,-9,-2,8],[8,-9,3,-6,6,-3,7],[7,7,-2,-6,-3,1,1],[-8,1,5,10,8,1,9],[-6,-7,10,8,7,2,5],[4,5,5,8,5,-9,6],[-9,-4,-3,-2,7,2,-4],[-5,-8,-2,-1,-10,-8,8],[10,-5,-9,5,-2,-5,-7],[-6,-1,-9,-10,-1,-10,1],[-6,3,-3,6,-9,-7,8]]], dtype = "int32")#candidate|4619|(6, 12, 7)|const|int32
bop_4620 = relay.right_shift(const_4618.astype('int32'), relay.reshape(const_4619.astype('int32'), relay.shape_of(const_4618))) # shape=(6, 12, 7)
output = relay.Tuple([bop_4620,])
output2 = relay.Tuple([bop_4620,])
func_4624 = relay.Function([], output)
mod['func_4624'] = func_4624
mod = relay.transform.InferType()(mod)
mutated_mod['func_4624'] = func_4624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mutated_mod.get_global_var('func_4624')
call_4625 = func_4624_call()
output = call_4625
func_4626 = relay.Function([], output)
mutated_mod['func_4626'] = func_4626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2506_call = mod.get_global_var('func_2506')
func_2508_call = mutated_mod.get_global_var('func_2508')
call_4629 = func_2506_call()
call_4630 = func_2506_call()
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_4633 = relay.TupleGetItem(func_2064_call(), 1)
call_4634 = relay.TupleGetItem(func_2066_call(), 1)
output = relay.Tuple([call_4629,call_4633,])
output2 = relay.Tuple([call_4630,call_4634,])
func_4638 = relay.Function([], output)
mod['func_4638'] = func_4638
mod = relay.transform.InferType()(mod)
output = func_4638()
func_4639 = relay.Function([], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4552_call = mod.get_global_var('func_4552')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_4674 = relay.TupleGetItem(func_4552_call(), 1)
call_4675 = relay.TupleGetItem(func_4554_call(), 1)
func_3046_call = mod.get_global_var('func_3046')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_4676 = relay.TupleGetItem(func_3046_call(relay.reshape(call_4674.astype('float32'), [200,])), 2)
call_4677 = relay.TupleGetItem(func_3048_call(relay.reshape(call_4674.astype('float32'), [200,])), 2)
func_3603_call = mod.get_global_var('func_3603')
func_3604_call = mutated_mod.get_global_var('func_3604')
call_4692 = relay.TupleGetItem(func_3603_call(), 0)
call_4693 = relay.TupleGetItem(func_3604_call(), 0)
var_4699 = relay.var("var_4699", dtype = "float32", shape = (10, 10, 2))#candidate|4699|(10, 10, 2)|var|float32
bop_4700 = relay.bitwise_and(call_4692.astype('uint8'), relay.reshape(var_4699.astype('uint8'), relay.shape_of(call_4692))) # shape=(10, 10, 2)
bop_4703 = relay.bitwise_and(call_4693.astype('uint8'), relay.reshape(var_4699.astype('uint8'), relay.shape_of(call_4693))) # shape=(10, 10, 2)
output = relay.Tuple([call_4674,call_4676,bop_4700,])
output2 = relay.Tuple([call_4675,call_4677,bop_4703,])
func_4716 = relay.Function([var_4699,], output)
mod['func_4716'] = func_4716
mod = relay.transform.InferType()(mod)
mutated_mod['func_4716'] = func_4716
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4717 = relay.var("var_4717", dtype = "float32", shape = (10, 10, 2))#candidate|4717|(10, 10, 2)|var|float32
func_4716_call = mutated_mod.get_global_var('func_4716')
call_4718 = func_4716_call(var_4717)
output = call_4718
func_4719 = relay.Function([var_4717], output)
mutated_mod['func_4719'] = func_4719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2073_call = mutated_mod.get_global_var('func_2073')
call_4721 = func_2072_call()
call_4722 = func_2072_call()
output = call_4721
output2 = call_4722
func_4723 = relay.Function([], output)
mod['func_4723'] = func_4723
mod = relay.transform.InferType()(mod)
output = func_4723()
func_4724 = relay.Function([], output)
mutated_mod['func_4724'] = func_4724
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4723_call = mod.get_global_var('func_4723')
func_4724_call = mutated_mod.get_global_var('func_4724')
call_4735 = func_4723_call()
call_4736 = func_4723_call()
uop_4749 = relay.log10(call_4735.astype('float32')) # shape=(10, 10, 2)
uop_4751 = relay.log10(call_4736.astype('float32')) # shape=(10, 10, 2)
uop_4755 = relay.sqrt(uop_4749.astype('float32')) # shape=(10, 10, 2)
uop_4757 = relay.sqrt(uop_4751.astype('float32')) # shape=(10, 10, 2)
bop_4762 = relay.right_shift(uop_4755.astype('uint32'), relay.reshape(uop_4749.astype('uint32'), relay.shape_of(uop_4755))) # shape=(10, 10, 2)
bop_4765 = relay.right_shift(uop_4757.astype('uint32'), relay.reshape(uop_4751.astype('uint32'), relay.shape_of(uop_4757))) # shape=(10, 10, 2)
func_3296_call = mod.get_global_var('func_3296')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_4772 = relay.TupleGetItem(func_3296_call(relay.reshape(uop_4755.astype('float32'), [10, 10, 2])), 1)
call_4773 = relay.TupleGetItem(func_3299_call(relay.reshape(uop_4755.astype('float32'), [10, 10, 2])), 1)
func_4624_call = mod.get_global_var('func_4624')
func_4626_call = mutated_mod.get_global_var('func_4626')
call_4774 = relay.TupleGetItem(func_4624_call(), 0)
call_4775 = relay.TupleGetItem(func_4626_call(), 0)
output = relay.Tuple([bop_4762,call_4772,call_4774,])
output2 = relay.Tuple([bop_4765,call_4773,call_4775,])
func_4798 = relay.Function([], output)
mod['func_4798'] = func_4798
mod = relay.transform.InferType()(mod)
mutated_mod['func_4798'] = func_4798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4798_call = mutated_mod.get_global_var('func_4798')
call_4799 = func_4798_call()
output = call_4799
func_4800 = relay.Function([], output)
mutated_mod['func_4800'] = func_4800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4523_call = mod.get_global_var('func_4523')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_4816 = relay.TupleGetItem(func_4523_call(), 1)
call_4817 = relay.TupleGetItem(func_4524_call(), 1)
output = relay.Tuple([call_4816,])
output2 = relay.Tuple([call_4817,])
func_4824 = relay.Function([], output)
mod['func_4824'] = func_4824
mod = relay.transform.InferType()(mod)
output = func_4824()
func_4825 = relay.Function([], output)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mod.get_global_var('func_3379')
func_3381_call = mutated_mod.get_global_var('func_3381')
call_4826 = relay.TupleGetItem(func_3379_call(), 0)
call_4827 = relay.TupleGetItem(func_3381_call(), 0)
func_3001_call = mod.get_global_var('func_3001')
func_3003_call = mutated_mod.get_global_var('func_3003')
call_4834 = func_3001_call()
call_4835 = func_3001_call()
func_1276_call = mod.get_global_var('func_1276')
func_1278_call = mutated_mod.get_global_var('func_1278')
const_4850 = relay.const([[-5.410134,-4.624414],[7.604849,-7.268612],[-0.355977,5.050347],[-1.070160,-2.943617],[-3.046050,-2.744350],[-0.116475,8.027505]], dtype = "float32")#candidate|4850|(6, 2)|const|float32
call_4849 = relay.TupleGetItem(func_1276_call(relay.reshape(const_4850.astype('float32'), [2, 1, 6])), 0)
call_4851 = relay.TupleGetItem(func_1278_call(relay.reshape(const_4850.astype('float32'), [2, 1, 6])), 0)
uop_4852 = relay.log(call_4834.astype('float32')) # shape=(10, 10, 2)
uop_4854 = relay.log(call_4835.astype('float32')) # shape=(10, 10, 2)
func_3342_call = mod.get_global_var('func_3342')
func_3343_call = mutated_mod.get_global_var('func_3343')
call_4873 = func_3342_call()
call_4874 = func_3342_call()
bop_4875 = relay.logical_and(call_4849.astype('bool'), relay.reshape(const_4850.astype('bool'), relay.shape_of(call_4849))) # shape=(2, 1, 6)
bop_4878 = relay.logical_and(call_4851.astype('bool'), relay.reshape(const_4850.astype('bool'), relay.shape_of(call_4851))) # shape=(2, 1, 6)
func_2735_call = mod.get_global_var('func_2735')
func_2736_call = mutated_mod.get_global_var('func_2736')
call_4880 = relay.TupleGetItem(func_2735_call(), 1)
call_4881 = relay.TupleGetItem(func_2736_call(), 1)
func_4112_call = mod.get_global_var('func_4112')
func_4114_call = mutated_mod.get_global_var('func_4114')
call_4885 = relay.TupleGetItem(func_4112_call(), 0)
call_4886 = relay.TupleGetItem(func_4114_call(), 0)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_4888 = relay.TupleGetItem(func_4063_call(relay.reshape(call_4880.astype('float64'), [20,])), 5)
call_4889 = relay.TupleGetItem(func_4065_call(relay.reshape(call_4880.astype('float64'), [20,])), 5)
output = relay.Tuple([call_4826,uop_4852,call_4873,bop_4875,call_4880,call_4885,call_4888,])
output2 = relay.Tuple([call_4827,uop_4854,call_4874,bop_4878,call_4881,call_4886,call_4889,])
func_4902 = relay.Function([], output)
mod['func_4902'] = func_4902
mod = relay.transform.InferType()(mod)
output = func_4902()
func_4903 = relay.Function([], output)
mutated_mod['func_4903'] = func_4903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4928 = relay.var("var_4928", dtype = "bool", shape = (7, 16, 11))#candidate|4928|(7, 16, 11)|var|bool
var_4929 = relay.var("var_4929", dtype = "bool", shape = (7, 16, 11))#candidate|4929|(7, 16, 11)|var|bool
bop_4930 = relay.logical_or(var_4928.astype('bool'), relay.reshape(var_4929.astype('bool'), relay.shape_of(var_4928))) # shape=(7, 16, 11)
output = bop_4930
output2 = bop_4930
func_4941 = relay.Function([var_4928,var_4929,], output)
mod['func_4941'] = func_4941
mod = relay.transform.InferType()(mod)
var_4942 = relay.var("var_4942", dtype = "bool", shape = (7, 16, 11))#candidate|4942|(7, 16, 11)|var|bool
var_4943 = relay.var("var_4943", dtype = "bool", shape = (7, 16, 11))#candidate|4943|(7, 16, 11)|var|bool
output = func_4941(var_4942,var_4943,)
func_4944 = relay.Function([var_4942,var_4943,], output)
mutated_mod['func_4944'] = func_4944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4626_call = mutated_mod.get_global_var('func_4626')
call_5041 = relay.TupleGetItem(func_4624_call(), 0)
call_5042 = relay.TupleGetItem(func_4626_call(), 0)
uop_5061 = relay.rsqrt(call_5041.astype('float64')) # shape=(6, 12, 7)
uop_5063 = relay.rsqrt(call_5042.astype('float64')) # shape=(6, 12, 7)
func_2590_call = mod.get_global_var('func_2590')
func_2592_call = mutated_mod.get_global_var('func_2592')
call_5064 = relay.TupleGetItem(func_2590_call(), 0)
call_5065 = relay.TupleGetItem(func_2592_call(), 0)
output = relay.Tuple([uop_5061,call_5064,])
output2 = relay.Tuple([uop_5063,call_5065,])
func_5069 = relay.Function([], output)
mod['func_5069'] = func_5069
mod = relay.transform.InferType()(mod)
mutated_mod['func_5069'] = func_5069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5069_call = mutated_mod.get_global_var('func_5069')
call_5070 = func_5069_call()
output = call_5070
func_5071 = relay.Function([], output)
mutated_mod['func_5071'] = func_5071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_5079 = relay.TupleGetItem(func_2814_call(), 2)
call_5080 = relay.TupleGetItem(func_2816_call(), 2)
output = relay.Tuple([call_5079,])
output2 = relay.Tuple([call_5080,])
func_5086 = relay.Function([], output)
mod['func_5086'] = func_5086
mod = relay.transform.InferType()(mod)
output = func_5086()
func_5087 = relay.Function([], output)
mutated_mod['func_5087'] = func_5087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_5091 = func_1439_call()
call_5092 = func_1439_call()
output = call_5091
output2 = call_5092
func_5093 = relay.Function([], output)
mod['func_5093'] = func_5093
mod = relay.transform.InferType()(mod)
mutated_mod['func_5093'] = func_5093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5093_call = mutated_mod.get_global_var('func_5093')
call_5094 = func_5093_call()
output = call_5094
func_5095 = relay.Function([], output)
mutated_mod['func_5095'] = func_5095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_5103 = relay.TupleGetItem(func_2064_call(), 1)
call_5104 = relay.TupleGetItem(func_2066_call(), 1)
var_5107 = relay.var("var_5107", dtype = "int8", shape = (98, 4))#candidate|5107|(98, 4)|var|int8
bop_5108 = relay.mod(call_5103.astype('float64'), relay.reshape(var_5107.astype('float64'), relay.shape_of(call_5103))) # shape=(98, 4)
bop_5111 = relay.mod(call_5104.astype('float64'), relay.reshape(var_5107.astype('float64'), relay.shape_of(call_5104))) # shape=(98, 4)
func_3379_call = mod.get_global_var('func_3379')
func_3381_call = mutated_mod.get_global_var('func_3381')
call_5113 = relay.TupleGetItem(func_3379_call(), 0)
call_5114 = relay.TupleGetItem(func_3381_call(), 0)
output = relay.Tuple([bop_5108,call_5113,])
output2 = relay.Tuple([bop_5111,call_5114,])
func_5116 = relay.Function([var_5107,], output)
mod['func_5116'] = func_5116
mod = relay.transform.InferType()(mod)
mutated_mod['func_5116'] = func_5116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5117 = relay.var("var_5117", dtype = "int8", shape = (98, 4))#candidate|5117|(98, 4)|var|int8
func_5116_call = mutated_mod.get_global_var('func_5116')
call_5118 = func_5116_call(var_5117)
output = call_5118
func_5119 = relay.Function([var_5117], output)
mutated_mod['func_5119'] = func_5119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_5138 = func_2090_call()
call_5139 = func_2090_call()
output = call_5138
output2 = call_5139
func_5142 = relay.Function([], output)
mod['func_5142'] = func_5142
mod = relay.transform.InferType()(mod)
output = func_5142()
func_5143 = relay.Function([], output)
mutated_mod['func_5143'] = func_5143
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5190 = relay.var("var_5190", dtype = "bool", shape = (4, 8, 11))#candidate|5190|(4, 8, 11)|var|bool
var_5191 = relay.var("var_5191", dtype = "bool", shape = (4, 8, 11))#candidate|5191|(4, 8, 11)|var|bool
bop_5192 = relay.logical_and(var_5190.astype('bool'), relay.reshape(var_5191.astype('bool'), relay.shape_of(var_5190))) # shape=(4, 8, 11)
output = bop_5192
output2 = bop_5192
func_5196 = relay.Function([var_5190,var_5191,], output)
mod['func_5196'] = func_5196
mod = relay.transform.InferType()(mod)
mutated_mod['func_5196'] = func_5196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5196_call = mutated_mod.get_global_var('func_5196')
var_5198 = relay.var("var_5198", dtype = "bool", shape = (4, 8, 11))#candidate|5198|(4, 8, 11)|var|bool
var_5199 = relay.var("var_5199", dtype = "bool", shape = (4, 8, 11))#candidate|5199|(4, 8, 11)|var|bool
call_5197 = func_5196_call(var_5198,var_5199,)
output = call_5197
func_5200 = relay.Function([var_5198,var_5199,], output)
mutated_mod['func_5200'] = func_5200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4552_call = mod.get_global_var('func_4552')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_5208 = relay.TupleGetItem(func_4552_call(), 2)
call_5209 = relay.TupleGetItem(func_4554_call(), 2)
output = call_5208
output2 = call_5209
func_5210 = relay.Function([], output)
mod['func_5210'] = func_5210
mod = relay.transform.InferType()(mod)
output = func_5210()
func_5211 = relay.Function([], output)
mutated_mod['func_5211'] = func_5211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4626_call = mutated_mod.get_global_var('func_4626')
call_5246 = relay.TupleGetItem(func_4624_call(), 0)
call_5247 = relay.TupleGetItem(func_4626_call(), 0)
output = call_5246
output2 = call_5247
func_5251 = relay.Function([], output)
mod['func_5251'] = func_5251
mod = relay.transform.InferType()(mod)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5251_call = mutated_mod.get_global_var('func_5251')
call_5252 = func_5251_call()
output = call_5252
func_5253 = relay.Function([], output)
mutated_mod['func_5253'] = func_5253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mod.get_global_var('func_3379')
func_3381_call = mutated_mod.get_global_var('func_3381')
call_5259 = relay.TupleGetItem(func_3379_call(), 0)
call_5260 = relay.TupleGetItem(func_3381_call(), 0)
func_3101_call = mod.get_global_var('func_3101')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_5266 = func_3101_call()
call_5267 = func_3101_call()
output = relay.Tuple([call_5259,call_5266,])
output2 = relay.Tuple([call_5260,call_5267,])
func_5276 = relay.Function([], output)
mod['func_5276'] = func_5276
mod = relay.transform.InferType()(mod)
output = func_5276()
func_5277 = relay.Function([], output)
mutated_mod['func_5277'] = func_5277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2072_call = mod.get_global_var('func_2072')
func_2073_call = mutated_mod.get_global_var('func_2073')
call_5404 = func_2072_call()
call_5405 = func_2072_call()
output = call_5404
output2 = call_5405
func_5406 = relay.Function([], output)
mod['func_5406'] = func_5406
mod = relay.transform.InferType()(mod)
output = func_5406()
func_5407 = relay.Function([], output)
mutated_mod['func_5407'] = func_5407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4624_call = mod.get_global_var('func_4624')
func_4626_call = mutated_mod.get_global_var('func_4626')
call_5498 = relay.TupleGetItem(func_4624_call(), 0)
call_5499 = relay.TupleGetItem(func_4626_call(), 0)
var_5500 = relay.var("var_5500", dtype = "int32", shape = (6, 12, 7))#candidate|5500|(6, 12, 7)|var|int32
bop_5501 = relay.multiply(call_5498.astype('float64'), relay.reshape(var_5500.astype('float64'), relay.shape_of(call_5498))) # shape=(6, 12, 7)
bop_5504 = relay.multiply(call_5499.astype('float64'), relay.reshape(var_5500.astype('float64'), relay.shape_of(call_5499))) # shape=(6, 12, 7)
uop_5511 = relay.atanh(var_5500.astype('float32')) # shape=(6, 12, 7)
output = relay.Tuple([bop_5501,uop_5511,])
output2 = relay.Tuple([bop_5504,uop_5511,])
func_5518 = relay.Function([var_5500,], output)
mod['func_5518'] = func_5518
mod = relay.transform.InferType()(mod)
var_5519 = relay.var("var_5519", dtype = "int32", shape = (6, 12, 7))#candidate|5519|(6, 12, 7)|var|int32
output = func_5518(var_5519)
func_5520 = relay.Function([var_5519], output)
mutated_mod['func_5520'] = func_5520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4798_call = mod.get_global_var('func_4798')
func_4800_call = mutated_mod.get_global_var('func_4800')
call_5586 = relay.TupleGetItem(func_4798_call(), 2)
call_5587 = relay.TupleGetItem(func_4800_call(), 2)
var_5597 = relay.var("var_5597", dtype = "int32", shape = (6, 12, 7))#candidate|5597|(6, 12, 7)|var|int32
bop_5598 = relay.logical_or(call_5586.astype('bool'), relay.reshape(var_5597.astype('bool'), relay.shape_of(call_5586))) # shape=(6, 12, 7)
bop_5601 = relay.logical_or(call_5587.astype('bool'), relay.reshape(var_5597.astype('bool'), relay.shape_of(call_5587))) # shape=(6, 12, 7)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_5603 = relay.TupleGetItem(func_2402_call(), 4)
call_5604 = relay.TupleGetItem(func_2404_call(), 4)
uop_5605 = relay.atanh(call_5603.astype('float32')) # shape=(225, 1)
uop_5607 = relay.atanh(call_5604.astype('float32')) # shape=(225, 1)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_5608 = func_2238_call()
call_5609 = func_2238_call()
output = relay.Tuple([bop_5598,uop_5605,call_5608,])
output2 = relay.Tuple([bop_5601,uop_5607,call_5609,])
func_5610 = relay.Function([var_5597,], output)
mod['func_5610'] = func_5610
mod = relay.transform.InferType()(mod)
var_5611 = relay.var("var_5611", dtype = "int32", shape = (6, 12, 7))#candidate|5611|(6, 12, 7)|var|int32
output = func_5610(var_5611)
func_5612 = relay.Function([var_5611], output)
mutated_mod['func_5612'] = func_5612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4232_call = mod.get_global_var('func_4232')
func_4233_call = mutated_mod.get_global_var('func_4233')
call_5704 = relay.TupleGetItem(func_4232_call(), 0)
call_5705 = relay.TupleGetItem(func_4233_call(), 0)
func_2870_call = mod.get_global_var('func_2870')
func_2872_call = mutated_mod.get_global_var('func_2872')
call_5706 = relay.TupleGetItem(func_2870_call(), 0)
call_5707 = relay.TupleGetItem(func_2872_call(), 0)
output = relay.Tuple([call_5704,call_5706,])
output2 = relay.Tuple([call_5705,call_5707,])
func_5716 = relay.Function([], output)
mod['func_5716'] = func_5716
mod = relay.transform.InferType()(mod)
output = func_5716()
func_5717 = relay.Function([], output)
mutated_mod['func_5717'] = func_5717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5757 = relay.var("var_5757", dtype = "float32", shape = (16, 1, 11))#candidate|5757|(16, 1, 11)|var|float32
uop_5758 = relay.atan(var_5757.astype('float32')) # shape=(16, 1, 11)
output = uop_5758
output2 = uop_5758
func_5761 = relay.Function([var_5757,], output)
mod['func_5761'] = func_5761
mod = relay.transform.InferType()(mod)
var_5762 = relay.var("var_5762", dtype = "float32", shape = (16, 1, 11))#candidate|5762|(16, 1, 11)|var|float32
output = func_5761(var_5762)
func_5763 = relay.Function([var_5762], output)
mutated_mod['func_5763'] = func_5763
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5778 = relay.const(-0.415788, dtype = "float64")#candidate|5778|()|const|float64
var_5779 = relay.var("var_5779", dtype = "float64", shape = (10, 4, 1))#candidate|5779|(10, 4, 1)|var|float64
bop_5780 = relay.floor_mod(const_5778.astype('float64'), var_5779.astype('float64')) # shape=(10, 4, 1)
func_1606_call = mod.get_global_var('func_1606')
func_1608_call = mutated_mod.get_global_var('func_1608')
call_5797 = func_1606_call()
call_5798 = func_1606_call()
func_4552_call = mod.get_global_var('func_4552')
func_4554_call = mutated_mod.get_global_var('func_4554')
call_5809 = relay.TupleGetItem(func_4552_call(), 1)
call_5810 = relay.TupleGetItem(func_4554_call(), 1)
output = relay.Tuple([bop_5780,call_5797,call_5809,])
output2 = relay.Tuple([bop_5780,call_5798,call_5810,])
func_5812 = relay.Function([var_5779,], output)
mod['func_5812'] = func_5812
mod = relay.transform.InferType()(mod)
mutated_mod['func_5812'] = func_5812
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5813 = relay.var("var_5813", dtype = "float64", shape = (10, 4, 1))#candidate|5813|(10, 4, 1)|var|float64
func_5812_call = mutated_mod.get_global_var('func_5812')
call_5814 = func_5812_call(var_5813)
output = call_5814
func_5815 = relay.Function([var_5813], output)
mutated_mod['func_5815'] = func_5815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_5912 = relay.TupleGetItem(func_1716_call(), 0)
call_5913 = relay.TupleGetItem(func_1717_call(), 0)
func_4165_call = mod.get_global_var('func_4165')
func_4167_call = mutated_mod.get_global_var('func_4167')
call_5914 = func_4165_call()
call_5915 = func_4165_call()
output = relay.Tuple([call_5912,call_5914,])
output2 = relay.Tuple([call_5913,call_5915,])
func_5919 = relay.Function([], output)
mod['func_5919'] = func_5919
mod = relay.transform.InferType()(mod)
output = func_5919()
func_5920 = relay.Function([], output)
mutated_mod['func_5920'] = func_5920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_5923 = func_2090_call()
call_5924 = func_2090_call()
func_5812_call = mod.get_global_var('func_5812')
func_5815_call = mutated_mod.get_global_var('func_5815')
var_5932 = relay.var("var_5932", dtype = "float64", shape = (40,))#candidate|5932|(40,)|var|float64
call_5931 = relay.TupleGetItem(func_5812_call(relay.reshape(var_5932.astype('float64'), [10, 4, 1])), 2)
call_5933 = relay.TupleGetItem(func_5815_call(relay.reshape(var_5932.astype('float64'), [10, 4, 1])), 2)
func_3296_call = mod.get_global_var('func_3296')
func_3299_call = mutated_mod.get_global_var('func_3299')
call_5949 = relay.TupleGetItem(func_3296_call(relay.reshape(call_5931.astype('float32'), [10, 10, 2])), 1)
call_5950 = relay.TupleGetItem(func_3299_call(relay.reshape(call_5931.astype('float32'), [10, 10, 2])), 1)
output = relay.Tuple([call_5923,call_5931,var_5932,call_5949,])
output2 = relay.Tuple([call_5924,call_5933,var_5932,call_5950,])
func_5951 = relay.Function([var_5932,], output)
mod['func_5951'] = func_5951
mod = relay.transform.InferType()(mod)
mutated_mod['func_5951'] = func_5951
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5952 = relay.var("var_5952", dtype = "float64", shape = (40,))#candidate|5952|(40,)|var|float64
func_5951_call = mutated_mod.get_global_var('func_5951')
call_5953 = func_5951_call(var_5952)
output = call_5953
func_5954 = relay.Function([var_5952], output)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_5956 = func_1640_call()
call_5957 = func_1640_call()
func_1582_call = mod.get_global_var('func_1582')
func_1584_call = mutated_mod.get_global_var('func_1584')
const_5976 = relay.const([-8.758836,-5.385355,1.572841,-7.710512,5.449572,-8.141021,4.973328,9.204998,-3.998741,6.860735,-2.484729,5.770475,6.768992,-2.252013,3.169573,6.427774,2.340386,-2.250922,-5.522108,8.457754,9.349360,-0.756805,8.591593,1.058978,3.229274,-9.858478,4.149263,6.888439,0.306219,6.205625,6.752157,4.557719,7.724684,4.392846,-7.071213,4.672876,-1.441500,6.366911,9.662334,-5.782611,8.320447,-2.272963,-3.077025,4.611922,-2.092255,-4.009994,1.509185,-1.933154,2.131431,-7.381369,-7.642849,3.118135,-8.262583,-2.382749,-1.224340,-8.516401,5.647949,-2.869268,-6.621916,-3.688284,3.141755,-3.815963,-5.148906,3.068495,8.665333,6.925083,6.820229,-3.628806,6.510647,-7.319692,0.146882,6.276650,2.685010,-5.837916,-5.208336,-9.153955,-6.718995,-7.191658,5.735196,-5.857434,-0.300902,8.821231,4.983908,8.014360,-7.470957,-0.315671,-3.893419,7.891083,4.040046,-8.615877,-9.174199,2.631240,7.487264,6.158465,7.543085,4.802237,0.319287,-4.631148,7.566823,-1.221417,3.530569,7.414816,-0.846869,4.259352,2.243690,1.077979,9.019149,-1.620468,0.811746,8.101168,7.962198,-6.082528,9.380040,1.556467,-9.487133,8.456419,-0.669018,5.235301,7.017507,2.108407,-9.621156,-5.325208,4.538764,6.353003,-7.466119,-4.828034,2.538485,-9.612923,3.925245,3.445347,7.856773,2.275519,-2.778080,1.199861,1.436848,-6.194626,8.077886,2.854611,3.525365,2.419309,-7.703122,4.362415,-7.282418,-4.427972,-0.932588,5.439585,-8.558180,6.185388,-8.671717,-7.032189,7.057969,8.416258,5.081822,-8.394117,6.537521,-5.444513,6.574147,-9.243145,-2.413476,7.553313,-7.063463,-4.080452,8.928130,7.429793,-3.574130,3.476323,-6.311102,6.147170,-9.301660,-3.812378,1.889761,6.848139,2.844393,1.785140,-6.184198,-1.881242,1.550962,-2.854618,-0.836409,-4.794359,8.975509,1.424328,0.265947,-9.420638,-9.090781,3.835064,6.094003,-3.579810,-9.635656,-3.297250,-8.515093,-2.540772,-6.758087,-3.142556,-6.345925,4.266201,-4.750354,-1.176190,8.108350,7.640894,7.088646,-6.612448,6.006119,3.855188,-7.051661,9.488089,-0.024097,-3.204084,-1.765505,-2.090744,-9.465063,-0.550932,-1.736566,-5.897035,9.416618,5.160847,-0.862346,-1.784894,-4.049797,-5.473906,9.918897,3.808897,3.541594,-2.627884,-8.778304,-9.141172,2.703755,9.304066,4.855813,1.428280,-5.602335,-9.716994,-9.818049,-3.916218,-6.646641,6.095232,-4.963421,-2.523794,7.366935,0.156114,7.549685,-1.287128,2.407704,-6.747760,6.227239,6.562150,-7.993959,-1.721306,-9.565377,4.581608,8.428952,3.649765,6.650509,9.900921,-0.820940,-1.985922,7.519504,-2.623171,-1.131936,7.240227,2.841876,3.414774,-7.369611,-0.237219,2.008580,-4.014109,9.893447,-6.453822,4.841930,5.687460,4.631231,5.109521,-1.916723,6.057074,-7.705419,-1.776629,4.947899,3.342782,8.005955,5.836992,0.194064,-9.263221,7.707106,5.609378,-0.997485,-7.661587,-0.493848,-8.898842,-9.322692,7.709248,4.125456,-1.770030,-1.435258,-3.331571,3.441153,-8.826094,6.061567,5.372131,9.291543,2.524604,4.099614,8.869908,2.672894,-7.684628,1.973257,-7.474654,3.974697,-6.286671,-5.083330,-6.247216,-1.334785,-7.113319,9.689326,-4.657372,-1.651402,-8.359405,5.327655,8.519937,-0.663577,-9.434672,-6.708081,-2.103653,2.354140,1.052053,9.740138,-3.391654,-4.223867,-7.240395,-4.498920,-3.862469,-2.956697,2.960656,2.003860,6.629811,-7.092910,8.152331,-3.398865,0.457583,-0.963829,-3.989848,-5.540301,0.795175,5.955910,-9.318147,-3.454988,1.889677,2.015215,8.786407,0.913959,-5.903052,-6.685518,-9.494451,2.197474,3.644993,-2.073769,-2.616051,-0.130105,6.268798,1.354256,8.893264,4.078025,-6.005270,0.154176,4.946734,-4.389998,1.018294,8.840654,-4.477695,5.295801,8.253406,0.537767,-1.889694,9.803566,6.664953,1.075720,0.051022,3.222860,7.052827,7.317509,-9.305149,2.871641,-7.716948,2.551920,6.971593,-3.250281,3.980987,-6.663817,6.001625,5.886854,-2.397691,-3.675634,5.155181,-5.307283,-7.650731,5.963083,6.019204,-5.831129,-6.871364,-6.899210,-8.646277,-9.133044,-0.341658,8.636738,-3.536690,9.597404,5.986396,-2.962917,1.541963,-6.068588,-3.677832,-4.271186,-4.951637,-7.489733,9.423079,-4.757617,0.037174,8.520476,-9.996321,-1.651533,2.087128,7.578684,9.696412,-9.918897,-6.577316,-7.212300,-0.765478,6.221387,-7.161489,8.469543,-5.118735,4.795640,-9.979188,-0.116183,-8.454121,-4.269714,-5.985226,-3.834067,0.772673,-5.085921,2.604604,3.812992,-8.657237,-8.555020,-8.888008,-5.533042,-7.333642,-9.522157,-8.460348,4.933330,0.588174,-1.356011,0.304876,9.526348,5.547111,3.697299,6.623969,3.965721,3.621417,-8.087877,3.123379,-8.201851,-7.333830,1.120955,5.538755,6.868425,-6.375102,-9.460928,6.252443,-2.160283,-8.633518,9.026179,-4.963882,8.964012,8.824434,4.560470,-8.101304,-1.540175,6.323947,1.453651,-0.567602,5.991693,-1.620669,-1.670146,-1.208198,6.785548,-1.483032,-9.286682,6.655467,-4.853164,3.930595,9.238231,-9.611748,-8.634640,7.110894,-8.898915,0.592112,-9.534308,-4.353085,2.733132,-2.040776,7.897902,3.552281,8.756508,9.462223,4.967608,-6.576279,-6.212026,-4.683484,-7.171385,-0.099992,6.600456,-8.170927,4.757343,1.992604,5.940116,8.555759,-0.735753,-4.638158,6.835132,-2.948149,-6.138090,-4.248018,0.610603,-8.894778,-1.276204,-4.255018,-8.315350,-7.976983,8.183165,-8.731896,9.136801,5.352205,-8.180801,9.273237,8.059226,2.679123,-6.401429,-3.213031,-1.506087,7.704884,5.937309,5.539019,1.195635,-7.336819,8.300712,5.088144,-1.942302,-0.195345,1.599014,3.422065,6.759424,-9.970126,-9.402705,1.471493,0.935034,1.256956,5.318758,-8.890782,-6.698803,3.891867,4.897098,-2.009976,-5.392330,7.805370,4.669793,-7.957829,9.849163,-3.408850,-8.378189,-5.285485,3.815478,-0.207473,-0.742617,2.657695,0.886473,-3.810238,7.780864,8.058735,-2.816686,5.043790,5.420347,-2.073950,0.457337,-3.481627,3.785288,1.451107,-0.468232,3.247049,9.049954,-5.370219,4.382168,0.427048,3.789264,-3.377368,0.682411,7.979750,-6.558352,9.553098,7.659162,0.363272,8.164141,8.151779,-8.859772,-7.382490,2.320350,2.212381,-9.917685,0.248252,6.503396,9.659847,-7.686896,3.008492,-2.915901,-9.981350,-9.872188,-0.364696,-8.278706,8.767287,-6.978635,-1.881230,-1.901710,6.779616,7.202092,7.923357,-9.671022,0.959304,7.143252,7.737211,-1.815769,4.599525,4.664680,-5.034233,7.794903,4.576140,4.484664,7.403214,5.470739,-8.150533,-6.451046,0.506626,-0.507875,7.750129,7.669203,-4.109403,-4.140462,-7.711538,6.365994,0.892404,-7.379905,8.758565,5.129462,-2.771325,5.323512,4.360152,-2.416487,-3.599744,4.815576,-7.540801,0.606502,-2.476017,8.374009,5.439880,0.956876,4.256411,9.701666,-1.971739,-0.333320,7.784717,9.813291,4.985270,4.148103,2.657878,5.644323,4.707851,-5.492685,-2.862683,-2.617617,-8.097265,-3.804776,-9.139343,-2.051875,-5.701116,7.746982,-0.968081,-6.636686,-5.509947,-0.071035,6.933259,2.228787,-1.303627,-1.107423,7.765653,-5.319677,4.655441,-4.478739,1.142330,-1.287927,3.161262,8.525646,-1.666858,6.233533,-0.796369,-2.250493,5.061595,-7.273443,2.044192,-1.539466,-3.331590,3.623647,3.240751,4.193806,-5.107884,2.937360,1.053397,-8.248012,-8.010424,-5.557450,8.407195,-0.811730,-2.122413], dtype = "float64")#candidate|5976|(720,)|const|float64
call_5975 = relay.TupleGetItem(func_1582_call(relay.reshape(const_5976.astype('float64'), [720,])), 4)
call_5977 = relay.TupleGetItem(func_1584_call(relay.reshape(const_5976.astype('float64'), [720,])), 4)
output = relay.Tuple([call_5956,call_5975,const_5976,])
output2 = relay.Tuple([call_5957,call_5977,const_5976,])
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
const_6012 = relay.const([[[-6.910956,-3.955368,-9.454374,-8.443706,-0.583633,0.469088,-1.874160,7.010216],[8.067323,5.203360,-7.642872,5.819073,0.715958,-7.117503,1.928565,2.213143],[-9.995411,-2.737134,-1.686243,-0.722569,-8.798993,4.096129,-3.018765,-2.898971],[1.776720,-8.798772,3.955171,-5.621353,-1.619092,-5.799056,-9.523451,-2.957000],[-1.508974,-2.123162,2.998234,0.360655,-4.022723,-6.406446,9.328650,-3.380414],[-2.576908,-8.695213,-5.091347,-2.330023,-9.378080,7.431106,-1.595984,4.570447],[-1.419944,-7.832300,-1.815837,-1.810968,-7.735454,-2.316040,7.183117,-2.371381],[1.810234,6.188542,8.151615,5.345554,6.446137,2.149801,-3.672615,-2.382574],[-3.447696,-3.873541,-9.853239,6.425355,-5.632225,-4.553691,-7.400399,6.904088]],[[-5.561698,-3.516138,8.933184,2.752592,-0.266411,-6.585930,1.307497,0.455449],[1.012765,-3.270495,-9.658450,-6.674124,1.565984,-4.215585,-9.738308,-0.185468],[2.054052,-0.139199,-9.079097,7.733654,-1.855581,9.727230,-6.021979,3.250667],[-5.408680,5.001633,1.345505,0.085968,-7.160642,5.833098,-3.053779,5.318302],[-5.137258,-7.498090,0.941178,2.527563,9.452129,4.617523,3.167982,-6.102692],[5.641543,3.210325,7.525544,8.933203,-8.515657,-3.789511,-7.324115,-0.490840],[-0.594386,0.824708,-9.789414,0.109739,9.342365,7.174634,-1.255389,2.278530],[9.809342,-2.117213,0.318125,8.025307,-5.339813,-3.883770,5.015818,0.749347],[5.710534,-1.713226,4.109883,-9.564103,-1.187663,-3.520740,2.123512,-5.036580]],[[-1.941347,1.239555,4.585928,4.538506,1.322471,-3.097588,6.014169,-5.885984],[7.223298,-8.332877,-8.314929,0.660285,8.953050,2.729236,1.694163,4.462884],[5.081970,-5.628669,3.139259,-1.057753,2.258561,-2.913392,0.548912,-5.051353],[9.794826,3.367315,2.411201,-3.268552,-4.739974,5.874547,-7.863577,3.819278],[9.128710,-6.367063,-7.273399,5.017379,9.573550,-1.534365,-9.533810,0.527817],[0.041938,-2.293741,-1.752579,4.131194,-4.432154,-4.122577,-0.107924,-5.164616],[3.895955,-4.137080,-6.610117,-9.250803,5.543138,-3.588497,0.092701,0.333980],[-6.501744,7.848869,6.857897,-7.470961,8.764563,-7.371247,-4.994486,5.604559],[6.503031,8.890934,-0.742512,5.139851,-9.904588,0.738102,-0.792557,1.856739]],[[-2.655766,9.683287,3.463099,-4.164937,-0.447896,-8.693092,4.860719,2.161886],[-6.619671,-7.491236,-3.093308,-4.558199,7.604007,-5.981281,4.071662,3.530174],[-8.917039,8.919126,-5.182002,-5.169426,-1.488207,8.360773,-9.136644,-8.751943],[-8.986583,3.289727,-4.987675,2.283788,-6.102599,5.731444,4.948706,9.944778],[3.894307,-6.677390,-9.378705,2.067897,6.984321,5.978089,8.275789,-7.321394],[-6.686795,-1.327832,-7.183796,9.568800,3.032755,-2.091402,1.661493,-1.197970],[-9.215771,-5.622907,3.770246,3.181795,-1.360268,-2.594622,-6.809597,3.527530],[4.493204,5.119406,-3.051497,-2.398416,-6.202282,-8.057752,-9.617842,-9.669065],[7.493480,-5.423538,-1.213990,-6.801283,-4.459718,-4.274928,2.060029,7.495391]],[[6.192046,-4.822630,1.433665,4.678176,7.228612,0.175446,-6.029367,-8.970553],[-8.900203,-6.024429,-4.371624,-3.327885,-2.075877,1.336722,-0.842034,-0.689906],[-1.787328,0.143110,2.255593,1.707749,0.254783,-9.918465,-2.317754,6.474817],[2.299139,-6.664304,-7.845445,-6.723830,8.791058,2.493027,6.202426,-2.275796],[-4.333145,1.136563,-2.845202,3.158467,-7.874982,-9.641485,-3.921839,6.214556],[0.610447,-9.711398,-1.454703,-2.873906,-4.729265,-9.341857,7.566499,8.857122],[-2.286979,5.038896,2.145271,-3.801776,8.689262,7.277566,4.033267,9.006668],[-2.973471,-9.092509,2.448171,-7.228843,-7.742247,2.197464,7.964738,-5.278464],[3.897036,8.450642,-2.203269,-8.463287,-1.763777,2.001662,9.398176,-2.823289]],[[-2.202969,-4.229656,-2.418674,-8.812550,3.138777,-5.416240,-8.369043,3.115079],[4.651129,6.822471,-2.460442,0.567834,9.463638,-7.625377,6.732629,-7.631260],[-6.355576,3.709242,3.066513,4.074254,6.200830,-0.065306,-2.964891,-8.012747],[-6.537221,4.106754,8.307021,7.266865,-9.078667,2.599627,-8.417145,0.142182],[1.543619,7.678319,-1.463230,1.210316,0.544379,-5.328338,1.819204,3.775265],[-7.842150,0.445213,9.146958,-5.402371,-0.460647,6.671991,7.445515,6.444183],[-3.116636,1.140627,-6.407370,-2.362101,-0.735251,5.828097,8.564335,8.271607],[-4.265556,-3.816341,7.721776,8.457350,-6.198076,3.067964,5.763764,-4.641836],[1.515996,0.421914,4.804371,1.997080,-0.448866,6.252737,2.787292,1.748185]],[[2.633348,2.449968,-6.471759,4.735374,-3.498439,-2.414119,6.096573,3.875214],[-3.112309,-5.123259,-6.940961,-8.625381,6.993771,9.906051,-0.942179,-3.201398],[-3.712560,5.958649,-8.837511,9.983870,5.189709,-3.810301,5.383249,0.697946],[-4.830988,5.479210,-0.878885,5.123604,4.606119,-9.824322,0.308825,-1.576316],[7.353363,-2.508786,-3.771283,-8.168708,0.384219,-5.336455,-3.196784,8.806443],[-0.678264,7.289041,-7.423225,-9.575369,5.694729,7.490009,2.640291,-0.088614],[3.788250,-4.630684,2.629677,5.336595,8.404648,9.089589,-3.525865,5.509019],[1.087338,6.077947,5.425095,1.928167,-2.836613,-9.592649,-2.588631,-8.406910],[6.980481,2.860395,1.554907,-2.630202,3.829727,-4.562341,-1.463006,-1.746322]]], dtype = "float64")#candidate|6012|(7, 9, 8)|const|float64
const_6013 = relay.const([[[9.373026,2.691569,0.847304,1.513816,1.260383,1.003059,-6.985267,-4.142694],[3.207567,-3.560934,-2.869223,2.702137,7.196991,-2.840638,9.663165,7.771814],[6.420206,5.545913,7.183741,-3.072290,2.551032,-4.046419,-6.998530,5.123899],[7.976234,9.396417,1.320021,-8.992682,-9.364782,-7.493538,-7.002636,-6.658907],[-4.831686,9.205552,7.670751,-7.671722,7.974177,-2.457101,6.743312,1.954094],[4.915081,2.268534,5.078344,-5.020105,-9.348778,4.722293,-7.907400,-3.260587],[9.418370,-4.748224,1.114298,6.045733,-8.587657,2.664674,-4.199902,-3.281718],[8.952034,-3.456936,3.893047,3.503016,-1.977057,8.469000,-4.629788,0.119138],[4.261063,-6.814916,1.836699,0.506534,2.188126,2.925862,4.920993,-9.044542]],[[2.663202,1.335498,6.815910,6.159344,5.155365,-6.948668,-0.877519,9.408399],[-6.090820,7.762650,-2.488704,7.532807,1.193072,9.609159,-1.463383,0.934091],[-0.915246,-8.210929,9.947949,7.441715,-2.721277,7.936202,-6.947956,-1.969394],[-9.973012,-0.001090,-2.720646,5.907957,-8.006222,-7.213778,-9.622618,5.389282],[-8.066522,-7.513254,7.944273,-3.964942,9.254211,-1.889588,0.441153,-2.489476],[-1.869526,-1.867746,-3.241958,-9.023606,-9.584895,8.296049,7.047223,6.863589],[8.663728,9.025713,-0.051602,-0.948479,1.112469,6.234227,-9.675467,9.465381],[-3.603457,3.203357,5.713855,5.013848,1.827031,-6.764150,2.971166,-7.667588],[7.788300,0.252076,-3.785167,0.103769,1.475689,-2.179895,7.971375,-9.637770]],[[0.428490,-8.598323,-9.974071,-9.447688,4.415512,-2.033441,-2.242163,9.650141],[-5.747233,2.177924,-1.423577,9.078000,8.788119,0.888571,2.639554,-5.413383],[-7.235620,3.596671,2.380892,-7.811500,-4.815060,5.244126,5.522345,-2.142800],[-8.937614,-6.258212,-9.206417,-6.003658,0.441324,-8.594110,6.659739,3.447893],[-8.266829,-1.573534,-1.164452,-3.084275,7.198650,-8.025559,-4.111785,0.284528],[-4.046910,4.789659,5.606784,0.540460,-7.289751,1.949198,-6.615922,7.559551],[9.513885,-3.532184,-2.475782,-1.284683,3.562800,-7.095189,6.998685,-7.105247],[-1.739476,-6.301083,4.266960,-3.944228,-0.020732,4.970134,5.680049,7.693166],[5.629773,-2.169351,-3.287547,0.460602,7.578210,1.327632,0.980596,0.595447]],[[3.311837,5.913635,5.204559,-1.983832,2.624182,-1.659883,-5.893227,1.300484],[-0.799525,1.903012,-2.051022,-1.202948,6.598083,-6.201043,7.110837,-4.255276],[-7.131004,4.038076,8.762985,2.007571,0.744057,2.857896,5.783524,8.365415],[9.886861,-2.446531,-9.734626,6.795986,-1.186156,-4.287006,6.314734,-1.118306],[9.424154,2.581828,-8.845656,3.578601,1.885653,9.887868,-3.656933,-9.686366],[-9.586395,9.194733,1.349102,-3.536461,9.177110,0.233585,4.713341,-5.190901],[9.910465,2.638704,-4.271459,8.121815,-9.024025,-0.275996,-4.186487,-0.925076],[9.426224,7.117201,-8.256932,-0.686243,-0.623242,9.093461,3.135547,-9.380131],[5.929941,-6.784009,5.073794,0.634012,3.847313,-6.455003,-4.223414,-8.297889]],[[-6.667341,-4.661733,1.210025,-0.029621,-3.230513,8.208069,6.732369,-4.813566],[5.601710,-4.932682,9.462395,-3.387499,5.358739,-3.971078,0.109355,5.507815],[-4.545814,3.323704,-4.562905,4.243966,0.964446,1.913836,3.238284,1.782426],[-3.951754,4.582256,-9.165271,-0.124128,-7.304001,1.237106,5.842915,0.920091],[8.535827,6.158513,8.289628,-1.395952,6.491430,3.733440,-6.588570,-9.145914],[8.291056,-0.536726,3.649845,3.686198,4.344285,-3.247240,-9.699422,-8.332177],[-8.163115,3.893622,-8.063027,-7.098550,0.419456,-7.258169,-7.177695,0.063891],[-6.860527,7.951567,-1.692076,6.682986,-0.104766,1.679736,-7.394398,-3.378981],[9.001133,-1.290956,2.087679,-1.357188,-9.214859,-8.121700,5.556338,-7.139682]],[[2.435591,4.620222,8.066119,2.581705,-1.401814,-9.412655,-0.428526,0.036364],[-3.329525,-8.943540,-7.667901,4.888213,0.021799,-7.353938,4.462897,1.680010],[-1.270653,-8.772719,6.365801,3.061905,-2.633244,-3.154833,-9.154412,6.066444],[7.536715,0.817256,-1.928813,4.405437,-3.489943,-8.010040,-9.842061,5.411781],[-1.298044,-7.294439,4.446903,-2.703026,2.066789,3.422088,-9.728542,4.043046],[-9.203629,-6.213809,5.097488,-1.774249,8.252384,8.077751,-8.828870,-3.947438],[-0.030418,4.913901,0.793416,-7.671234,-3.674850,-7.566652,-6.376023,9.273898],[-7.059349,4.387079,6.456048,-8.627490,-8.218355,-5.046868,-0.556885,8.893715],[-7.877288,-8.756686,-9.144187,-9.878286,-0.742660,-1.051603,-4.298938,6.805668]],[[7.267008,-8.493701,8.519208,0.224109,-7.239415,-4.076537,-7.185593,-0.847142],[-0.927182,-0.154977,0.086769,-8.206261,-7.182777,-4.763321,-8.629383,9.051273],[-1.464105,-2.376468,-1.358685,8.519766,4.952355,6.078153,6.623887,-7.549184],[7.873331,6.174433,-1.775880,-0.377515,-0.283275,0.970729,4.559730,-4.289858],[0.417571,2.767639,-3.075591,-9.052607,-8.680416,8.476893,4.554551,-0.792939],[1.197049,4.383075,4.709763,-6.872358,-0.131129,-5.108289,-6.476443,7.874449],[4.602261,-0.667717,1.326988,9.644151,-2.836576,-3.271965,1.837271,-7.435447],[-4.027465,-7.732030,-9.675452,3.238347,-9.961833,-1.820217,-2.215462,-9.473406],[-1.705485,4.902615,-8.084216,4.825798,3.547511,-3.301987,-1.515224,5.550183]]], dtype = "float64")#candidate|6013|(7, 9, 8)|const|float64
bop_6014 = relay.mod(const_6012.astype('float64'), relay.reshape(const_6013.astype('float64'), relay.shape_of(const_6012))) # shape=(7, 9, 8)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
const_6018 = relay.const([[4.947666,4.341573],[8.695083,-1.866399],[-0.222736,-2.347942],[-3.732759,-4.382901],[1.201184,1.065212],[8.766592,3.478744],[-0.612748,-0.694663],[-5.121939,-7.455769],[5.771319,-8.120838],[4.981105,8.789543]], dtype = "float64")#candidate|6018|(10, 2)|const|float64
call_6017 = relay.TupleGetItem(func_4063_call(relay.reshape(const_6018.astype('float64'), [20,])), 5)
call_6019 = relay.TupleGetItem(func_4065_call(relay.reshape(const_6018.astype('float64'), [20,])), 5)
func_3342_call = mod.get_global_var('func_3342')
func_3343_call = mutated_mod.get_global_var('func_3343')
call_6028 = func_3342_call()
call_6029 = func_3342_call()
func_4112_call = mod.get_global_var('func_4112')
func_4114_call = mutated_mod.get_global_var('func_4114')
call_6053 = relay.TupleGetItem(func_4112_call(), 0)
call_6054 = relay.TupleGetItem(func_4114_call(), 0)
func_2238_call = mod.get_global_var('func_2238')
func_2239_call = mutated_mod.get_global_var('func_2239')
call_6064 = func_2238_call()
call_6065 = func_2238_call()
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_6097 = relay.TupleGetItem(func_276_call(relay.reshape(const_6018.astype('float64'), [10, 1, 2])), 0)
call_6098 = relay.TupleGetItem(func_279_call(relay.reshape(const_6018.astype('float64'), [10, 1, 2])), 0)
output = relay.Tuple([bop_6014,call_6017,const_6018,call_6028,call_6053,call_6064,call_6097,])
output2 = relay.Tuple([bop_6014,call_6019,const_6018,call_6029,call_6054,call_6065,call_6098,])
func_6099 = relay.Function([], output)
mod['func_6099'] = func_6099
mod = relay.transform.InferType()(mod)
output = func_6099()
func_6100 = relay.Function([], output)
mutated_mod['func_6100'] = func_6100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5276_call = mod.get_global_var('func_5276')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_6106 = relay.TupleGetItem(func_5276_call(), 0)
call_6107 = relay.TupleGetItem(func_5277_call(), 0)
func_2064_call = mod.get_global_var('func_2064')
func_2066_call = mutated_mod.get_global_var('func_2066')
call_6112 = relay.TupleGetItem(func_2064_call(), 0)
call_6113 = relay.TupleGetItem(func_2066_call(), 0)
func_3130_call = mod.get_global_var('func_3130')
func_3132_call = mutated_mod.get_global_var('func_3132')
call_6114 = relay.TupleGetItem(func_3130_call(), 0)
call_6115 = relay.TupleGetItem(func_3132_call(), 0)
output = relay.Tuple([call_6106,call_6112,call_6114,])
output2 = relay.Tuple([call_6107,call_6113,call_6115,])
func_6120 = relay.Function([], output)
mod['func_6120'] = func_6120
mod = relay.transform.InferType()(mod)
output = func_6120()
func_6121 = relay.Function([], output)
mutated_mod['func_6121'] = func_6121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4167_call = mutated_mod.get_global_var('func_4167')
call_6128 = func_4165_call()
call_6129 = func_4165_call()
output = call_6128
output2 = call_6129
func_6135 = relay.Function([], output)
mod['func_6135'] = func_6135
mod = relay.transform.InferType()(mod)
mutated_mod['func_6135'] = func_6135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6136 = func_6135_call()
output = call_6136
func_6137 = relay.Function([], output)
mutated_mod['func_6137'] = func_6137
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6217 = relay.var("var_6217", dtype = "float64", shape = (3, 16, 14))#candidate|6217|(3, 16, 14)|var|float64
uop_6218 = relay.acos(var_6217.astype('float64')) # shape=(3, 16, 14)
func_1716_call = mod.get_global_var('func_1716')
func_1717_call = mutated_mod.get_global_var('func_1717')
call_6229 = relay.TupleGetItem(func_1716_call(), 0)
call_6230 = relay.TupleGetItem(func_1717_call(), 0)
output = relay.Tuple([uop_6218,call_6229,])
output2 = relay.Tuple([uop_6218,call_6230,])
func_6235 = relay.Function([var_6217,], output)
mod['func_6235'] = func_6235
mod = relay.transform.InferType()(mod)
var_6236 = relay.var("var_6236", dtype = "float64", shape = (3, 16, 14))#candidate|6236|(3, 16, 14)|var|float64
output = func_6235(var_6236)
func_6237 = relay.Function([var_6236], output)
mutated_mod['func_6237'] = func_6237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_6312 = func_2090_call()
call_6313 = func_2090_call()
output = relay.Tuple([call_6312,])
output2 = relay.Tuple([call_6313,])
func_6318 = relay.Function([], output)
mod['func_6318'] = func_6318
mod = relay.transform.InferType()(mod)
mutated_mod['func_6318'] = func_6318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6318_call = mutated_mod.get_global_var('func_6318')
call_6319 = func_6318_call()
output = call_6319
func_6320 = relay.Function([], output)
mutated_mod['func_6320'] = func_6320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2506_call = mod.get_global_var('func_2506')
func_2508_call = mutated_mod.get_global_var('func_2508')
call_6354 = func_2506_call()
call_6355 = func_2506_call()
output = relay.Tuple([call_6354,])
output2 = relay.Tuple([call_6355,])
func_6356 = relay.Function([], output)
mod['func_6356'] = func_6356
mod = relay.transform.InferType()(mod)
output = func_6356()
func_6357 = relay.Function([], output)
mutated_mod['func_6357'] = func_6357
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6378 = relay.var("var_6378", dtype = "float64", shape = (14, 6, 14))#candidate|6378|(14, 6, 14)|var|float64
uop_6379 = relay.acos(var_6378.astype('float64')) # shape=(14, 6, 14)
output = uop_6379
output2 = uop_6379
func_6383 = relay.Function([var_6378,], output)
mod['func_6383'] = func_6383
mod = relay.transform.InferType()(mod)
var_6384 = relay.var("var_6384", dtype = "float64", shape = (14, 6, 14))#candidate|6384|(14, 6, 14)|var|float64
output = func_6383(var_6384)
func_6385 = relay.Function([var_6384], output)
mutated_mod['func_6385'] = func_6385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6393 = relay.var("var_6393", dtype = "uint64", shape = (3, 8, 14))#candidate|6393|(3, 8, 14)|var|uint64
var_6394 = relay.var("var_6394", dtype = "uint64", shape = (3, 8, 14))#candidate|6394|(3, 8, 14)|var|uint64
bop_6395 = relay.equal(var_6393.astype('bool'), relay.reshape(var_6394.astype('bool'), relay.shape_of(var_6393))) # shape=(3, 8, 14)
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
var_6415 = relay.var("var_6415", dtype = "float64", shape = (20,))#candidate|6415|(20,)|var|float64
call_6414 = relay.TupleGetItem(func_4063_call(relay.reshape(var_6415.astype('float64'), [20,])), 1)
call_6416 = relay.TupleGetItem(func_4065_call(relay.reshape(var_6415.astype('float64'), [20,])), 1)
output = relay.Tuple([bop_6395,call_6414,var_6415,])
output2 = relay.Tuple([bop_6395,call_6416,var_6415,])
func_6425 = relay.Function([var_6393,var_6394,var_6415,], output)
mod['func_6425'] = func_6425
mod = relay.transform.InferType()(mod)
var_6426 = relay.var("var_6426", dtype = "uint64", shape = (3, 8, 14))#candidate|6426|(3, 8, 14)|var|uint64
var_6427 = relay.var("var_6427", dtype = "uint64", shape = (3, 8, 14))#candidate|6427|(3, 8, 14)|var|uint64
var_6428 = relay.var("var_6428", dtype = "float64", shape = (20,))#candidate|6428|(20,)|var|float64
output = func_6425(var_6426,var_6427,var_6428,)
func_6429 = relay.Function([var_6426,var_6427,var_6428,], output)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_6472 = func_1597_call()
call_6473 = func_1597_call()
uop_6500 = relay.acosh(call_6472.astype('float32')) # shape=(10, 10, 2)
uop_6502 = relay.acosh(call_6473.astype('float32')) # shape=(10, 10, 2)
func_2178_call = mod.get_global_var('func_2178')
func_2180_call = mutated_mod.get_global_var('func_2180')
call_6528 = func_2178_call()
call_6529 = func_2178_call()
func_4300_call = mod.get_global_var('func_4300')
func_4302_call = mutated_mod.get_global_var('func_4302')
call_6534 = func_4300_call()
call_6535 = func_4300_call()
func_474_call = mod.get_global_var('func_474')
func_476_call = mutated_mod.get_global_var('func_476')
var_6537 = relay.var("var_6537", dtype = "int8", shape = (392,))#candidate|6537|(392,)|var|int8
call_6536 = func_474_call(relay.reshape(var_6537.astype('int8'), [7, 8, 7]))
call_6538 = func_474_call(relay.reshape(var_6537.astype('int8'), [7, 8, 7]))
func_6425_call = mod.get_global_var('func_6425')
func_6429_call = mutated_mod.get_global_var('func_6429')
var_6547 = relay.var("var_6547", dtype = "uint64", shape = (336,))#candidate|6547|(336,)|var|uint64
const_6548 = relay.const([9.591390,3.674205,-7.330754,-8.765521,5.897124,-1.375803,-8.497636,-9.383520,-3.942278,1.613396,9.898394,2.374634,-8.335353,5.272954,0.041308,-8.763369,-6.003698,-3.651461,-4.441214,-6.918416], dtype = "float64")#candidate|6548|(20,)|const|float64
call_6546 = relay.TupleGetItem(func_6425_call(relay.reshape(var_6547.astype('uint64'), [3, 8, 14]), relay.reshape(var_6547.astype('uint64'), [3, 8, 14]), relay.reshape(const_6548.astype('float64'), [20,]), ), 1)
call_6549 = relay.TupleGetItem(func_6429_call(relay.reshape(var_6547.astype('uint64'), [3, 8, 14]), relay.reshape(var_6547.astype('uint64'), [3, 8, 14]), relay.reshape(const_6548.astype('float64'), [20,]), ), 1)
func_1276_call = mod.get_global_var('func_1276')
func_1278_call = mutated_mod.get_global_var('func_1278')
var_6568 = relay.var("var_6568", dtype = "float32", shape = (12,))#candidate|6568|(12,)|var|float32
call_6567 = relay.TupleGetItem(func_1276_call(relay.reshape(var_6568.astype('float32'), [2, 1, 6])), 0)
call_6569 = relay.TupleGetItem(func_1278_call(relay.reshape(var_6568.astype('float32'), [2, 1, 6])), 0)
func_4263_call = mod.get_global_var('func_4263')
func_4264_call = mutated_mod.get_global_var('func_4264')
call_6571 = func_4263_call()
call_6572 = func_4263_call()
func_1699_call = mod.get_global_var('func_1699')
func_1701_call = mutated_mod.get_global_var('func_1701')
var_6574 = relay.var("var_6574", dtype = "float32", shape = (192, 2))#candidate|6574|(192, 2)|var|float32
call_6573 = func_1699_call(relay.reshape(var_6574.astype('float32'), [3, 16, 8]))
call_6575 = func_1699_call(relay.reshape(var_6574.astype('float32'), [3, 16, 8]))
output = relay.Tuple([uop_6500,call_6528,call_6534,call_6536,var_6537,call_6546,var_6547,const_6548,call_6567,var_6568,call_6571,call_6573,var_6574,])
output2 = relay.Tuple([uop_6502,call_6529,call_6535,call_6538,var_6537,call_6549,var_6547,const_6548,call_6569,var_6568,call_6572,call_6575,var_6574,])
func_6577 = relay.Function([var_6537,var_6547,var_6568,var_6574,], output)
mod['func_6577'] = func_6577
mod = relay.transform.InferType()(mod)
mutated_mod['func_6577'] = func_6577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6577_call = mutated_mod.get_global_var('func_6577')
var_6579 = relay.var("var_6579", dtype = "int8", shape = (392,))#candidate|6579|(392,)|var|int8
var_6580 = relay.var("var_6580", dtype = "uint64", shape = (336,))#candidate|6580|(336,)|var|uint64
var_6581 = relay.var("var_6581", dtype = "float32", shape = (12,))#candidate|6581|(12,)|var|float32
var_6582 = relay.var("var_6582", dtype = "float32", shape = (192, 2))#candidate|6582|(192, 2)|var|float32
call_6578 = func_6577_call(var_6579,var_6580,var_6581,var_6582,)
output = call_6578
func_6583 = relay.Function([var_6579,var_6580,var_6581,var_6582,], output)
mutated_mod['func_6583'] = func_6583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_6606 = func_1640_call()
call_6607 = func_1640_call()
uop_6608 = relay.acos(call_6606.astype('float32')) # shape=(10, 10, 2)
uop_6610 = relay.acos(call_6607.astype('float32')) # shape=(10, 10, 2)
output = uop_6608
output2 = uop_6610
func_6613 = relay.Function([], output)
mod['func_6613'] = func_6613
mod = relay.transform.InferType()(mod)
mutated_mod['func_6613'] = func_6613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6613_call = mutated_mod.get_global_var('func_6613')
call_6614 = func_6613_call()
output = call_6614
func_6615 = relay.Function([], output)
mutated_mod['func_6615'] = func_6615
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6667 = relay.const([[[10,10,-6,-10,-5,-8,6,-9,-1,3,1,-8,4],[-8,-3,-5,-5,-9,-7,3,-1,-10,-7,6,-5,-3],[-4,1,-8,5,6,-6,-4,-1,-7,-4,5,7,-2],[1,-2,8,-5,6,-8,7,-10,4,-2,-8,1,-7],[-7,-2,9,-8,8,-9,-5,-6,-7,-8,6,4,8],[6,5,8,10,-2,-1,-2,-8,-2,9,7,-1,-4],[10,-6,3,8,5,-1,-5,-6,5,7,-10,-8,9],[6,2,-8,9,1,-5,-9,6,-7,-4,7,-2,3],[-7,2,6,-7,-7,1,8,7,2,6,-7,6,8],[1,2,-4,6,-5,4,-5,7,-7,9,-10,2,-8],[9,-10,-1,-6,8,-2,-8,1,8,-2,-1,10,5],[-10,6,-5,1,-1,-10,-5,-9,-5,3,8,1,6],[9,1,-8,8,-8,-10,-10,-1,-9,9,3,-4,9]],[[8,10,-1,2,10,2,5,-2,-8,3,3,8,-10],[7,7,-6,5,1,-4,7,-6,-5,-8,3,9,7],[-9,-7,6,-5,-9,10,-8,9,5,-9,6,1,10],[2,-9,5,-4,1,4,2,8,7,-4,-1,4,-9],[3,-4,3,4,7,-4,-2,2,10,1,-8,5,9],[-1,5,3,2,-2,-5,9,-8,4,7,-9,-2,4],[-3,1,2,-4,4,6,7,2,-6,6,5,5,-6],[6,9,7,8,3,-2,8,6,-5,-2,7,-10,-2],[-10,5,-3,5,3,-3,10,1,-5,-1,3,-6,-10],[2,5,-5,3,3,2,-10,-10,4,-3,5,5,10],[9,-4,-10,-1,2,-2,-5,-3,-2,10,9,3,2],[-9,3,9,-5,1,1,10,7,2,-6,-6,9,-2],[3,-8,5,-4,-7,8,-5,-9,2,-4,1,8,-1]],[[6,2,10,-5,-2,6,-7,-8,6,6,2,5,5],[-9,3,-9,2,9,9,-10,2,-7,-2,-6,8,6],[-7,5,-6,7,4,10,-1,8,3,-3,6,6,6],[-6,3,6,2,-6,-6,2,10,8,3,1,7,-4],[3,1,-1,6,1,-6,3,-5,-4,1,-1,5,-6],[-1,-10,6,-5,5,-7,2,2,3,1,-4,-7,10],[3,-1,4,2,8,-7,8,-3,-2,-3,4,-10,5],[1,-9,7,8,3,-3,6,-6,6,-5,-6,-3,-3],[-6,3,9,1,-7,-1,8,7,-10,3,-5,9,8],[-9,4,-8,-7,10,-5,3,1,4,-10,3,3,-6],[-4,8,-10,-3,-1,5,-9,3,9,-5,9,-10,-2],[9,-10,4,1,6,-1,8,-9,1,9,2,-7,8],[8,-5,2,6,2,-6,1,4,2,-7,6,-10,1]],[[3,-1,-6,-1,-9,-8,5,-4,2,-4,9,-10,-8],[6,1,10,-7,-7,1,-7,-10,-5,4,-7,-5,5],[-8,2,-3,-4,6,-8,-6,-8,-2,-7,-2,9,-10],[-4,-5,8,-6,-1,-7,-3,10,7,-8,-5,10,5],[6,7,10,10,-2,1,9,9,7,-2,-7,5,4],[8,-3,5,8,-5,5,4,-6,-5,6,-2,8,-10],[-2,10,6,-9,4,-6,6,-1,-9,-8,1,-9,-9],[-2,6,2,10,2,-2,2,-5,-10,-4,-3,7,5],[5,9,-6,1,-4,9,-6,9,-4,-6,3,-1,9],[7,5,8,-5,-6,-7,-2,1,-6,-2,7,-7,-4],[-10,-5,-9,7,-4,4,9,10,-6,-10,4,5,10],[-2,6,-5,-1,7,5,-1,-8,-10,-4,6,5,-8],[9,-4,5,6,-2,-10,-3,10,-3,-9,-8,10,3]],[[4,10,-8,-5,-10,8,4,8,2,2,-1,3,-6],[3,4,1,-4,2,-2,4,-1,-7,-2,-10,-6,6],[-7,-1,1,10,8,7,-2,3,8,-5,8,6,7],[-6,-8,2,1,-10,-5,-8,-10,6,6,6,-5,-4],[5,4,-6,4,-3,9,2,-4,10,2,9,-3,-7],[8,2,-6,-2,6,3,1,-8,7,10,7,-7,9],[8,2,1,-5,4,9,-4,-3,6,-10,-4,6,-2],[5,3,5,8,-7,9,-1,5,-8,-6,5,-5,-8],[-4,5,9,-5,-6,4,-10,-2,-2,10,4,6,9],[1,8,4,-4,-8,-1,-5,-5,-2,9,2,6,1],[-1,9,8,-3,9,-8,8,-8,-1,9,-2,-3,-2],[4,-8,-7,10,9,6,-4,-1,8,2,-10,8,1],[8,-1,-8,10,10,4,-3,-9,5,2,8,7,7]],[[-5,9,-5,9,-9,2,4,5,1,-3,5,-6,5],[-10,-5,2,-1,5,7,-1,2,4,-5,-6,-8,-7],[-8,-1,-6,-5,-7,-1,7,-4,10,9,-1,8,3],[-4,-4,4,-5,-4,8,-4,-6,3,10,8,-5,2],[1,5,5,-2,2,10,3,-10,5,5,-10,-5,-8],[-10,9,10,-1,3,-4,-6,3,6,10,-6,-2,6],[-1,-10,-5,3,-2,5,8,9,3,10,1,-3,-2],[6,1,-3,5,1,-6,6,-7,-9,-7,1,-4,-7],[7,-6,2,-2,-7,5,-2,4,3,4,-10,-9,3],[-8,-10,-4,8,7,-3,1,6,4,6,-4,7,-3],[4,6,3,-8,1,-2,-1,9,8,4,7,1,-5],[6,-4,-10,2,-8,10,-8,8,-9,10,3,-7,-3],[-6,-2,1,4,7,-6,10,4,1,-8,-3,-8,-7]],[[1,1,-10,8,9,-10,-5,-8,7,-6,-5,-4,-8],[4,-10,-8,-4,-6,-5,6,6,-10,4,3,-4,-4],[-7,-6,3,-10,10,5,6,-8,-6,6,2,-2,-4],[10,5,10,2,7,-5,-10,5,-9,-5,-2,1,4],[6,10,2,-9,-3,8,-5,1,-2,-5,6,-7,-8],[1,-9,-3,-10,6,-4,-10,-3,4,-3,-8,-8,1],[-4,5,7,3,1,-4,10,7,-6,5,-3,-7,-6],[3,-7,-5,3,3,6,-8,2,1,2,8,-3,7],[-1,-4,9,-10,2,-7,5,-6,8,1,-8,3,-10],[-7,-3,-1,-9,1,4,6,7,2,-5,-5,4,2],[10,-1,-6,3,3,4,-9,-3,6,-9,-5,5,1],[3,-9,7,-2,-8,-7,10,7,3,10,-10,-5,9],[2,-10,-5,-10,9,4,8,-2,4,-6,-7,-8,-4]],[[3,-7,-9,-8,4,1,-10,3,-2,7,-5,-5,4],[9,8,10,3,6,8,1,7,-8,-2,10,-2,-7],[8,10,-3,3,2,-3,-3,-7,2,5,-9,8,-5],[-3,-5,-6,2,6,4,-5,5,1,10,10,-5,-3],[1,-6,-10,-5,-9,2,8,-5,9,1,1,-1,2],[-2,10,3,-7,-8,-8,-5,-8,8,-5,8,-6,-6],[-1,-7,2,-1,-7,4,3,-2,-6,8,2,-10,1],[-8,7,4,-5,-2,-2,-9,-9,-2,4,-5,-1,-4],[9,1,-2,-6,5,10,3,-6,8,6,8,-10,-2],[-3,-8,-7,1,-10,6,-5,-8,-2,-8,9,-4,3],[-3,-4,-10,9,4,-8,3,-1,3,-2,2,3,-4],[7,-5,2,5,-4,-3,-4,10,-3,7,-4,1,-9],[-9,4,-5,1,-3,-8,9,3,7,-10,-7,-2,8]],[[-5,1,3,-8,-3,-9,-3,-9,1,4,-1,-1,-10],[3,-3,5,9,1,5,-10,10,-5,2,-5,4,-6],[10,4,-6,-1,8,-6,-3,-1,-8,-9,10,3,-9],[-4,-6,8,8,8,-8,4,9,5,10,-2,-6,-7],[6,8,-6,10,5,-2,9,10,10,-5,5,-3,-7],[3,8,2,10,1,4,-2,9,-3,-3,-6,-6,-4],[-5,8,-3,-5,-3,-7,7,-10,1,-10,-5,1,-6],[3,-1,5,-5,6,-3,1,10,-8,-7,-9,-2,3],[4,5,10,-3,6,-7,-10,9,5,-9,7,5,-6],[4,-7,-7,-10,2,2,-1,5,9,10,-9,5,4],[-5,-8,5,-1,9,-3,10,-9,3,1,9,-5,8],[-7,-2,-7,-10,-10,-6,-7,-8,-4,-8,-1,4,-2],[1,-1,9,-2,-9,-10,3,-5,-10,4,5,-6,-8]]], dtype = "uint8")#candidate|6667|(9, 13, 13)|const|uint8
var_6668 = relay.var("var_6668", dtype = "uint8", shape = (9, 13, 13))#candidate|6668|(9, 13, 13)|var|uint8
bop_6669 = relay.greater(const_6667.astype('bool'), relay.reshape(var_6668.astype('bool'), relay.shape_of(const_6667))) # shape=(9, 13, 13)
output = bop_6669
output2 = bop_6669
func_6679 = relay.Function([var_6668,], output)
mod['func_6679'] = func_6679
mod = relay.transform.InferType()(mod)
mutated_mod['func_6679'] = func_6679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6680 = relay.var("var_6680", dtype = "uint8", shape = (9, 13, 13))#candidate|6680|(9, 13, 13)|var|uint8
func_6679_call = mutated_mod.get_global_var('func_6679')
call_6681 = func_6679_call(var_6680)
output = call_6681
func_6682 = relay.Function([var_6680], output)
mutated_mod['func_6682'] = func_6682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4798_call = mod.get_global_var('func_4798')
func_4800_call = mutated_mod.get_global_var('func_4800')
call_6704 = relay.TupleGetItem(func_4798_call(), 2)
call_6705 = relay.TupleGetItem(func_4800_call(), 2)
func_4523_call = mod.get_global_var('func_4523')
func_4524_call = mutated_mod.get_global_var('func_4524')
call_6706 = relay.TupleGetItem(func_4523_call(), 1)
call_6707 = relay.TupleGetItem(func_4524_call(), 1)
output = relay.Tuple([call_6704,call_6706,])
output2 = relay.Tuple([call_6705,call_6707,])
func_6727 = relay.Function([], output)
mod['func_6727'] = func_6727
mod = relay.transform.InferType()(mod)
output = func_6727()
func_6728 = relay.Function([], output)
mutated_mod['func_6728'] = func_6728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4165_call = mod.get_global_var('func_4165')
func_4167_call = mutated_mod.get_global_var('func_4167')
call_6763 = func_4165_call()
call_6764 = func_4165_call()
func_6613_call = mod.get_global_var('func_6613')
func_6615_call = mutated_mod.get_global_var('func_6615')
call_6779 = func_6613_call()
call_6780 = func_6613_call()
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_6784 = func_2090_call()
call_6785 = func_2090_call()
output = relay.Tuple([call_6763,call_6779,call_6784,])
output2 = relay.Tuple([call_6764,call_6780,call_6785,])
func_6790 = relay.Function([], output)
mod['func_6790'] = func_6790
mod = relay.transform.InferType()(mod)
mutated_mod['func_6790'] = func_6790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6790_call = mutated_mod.get_global_var('func_6790')
call_6791 = func_6790_call()
output = call_6791
func_6792 = relay.Function([], output)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5276_call = mod.get_global_var('func_5276')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_6796 = relay.TupleGetItem(func_5276_call(), 0)
call_6797 = relay.TupleGetItem(func_5277_call(), 0)
output = relay.Tuple([call_6796,])
output2 = relay.Tuple([call_6797,])
func_6800 = relay.Function([], output)
mod['func_6800'] = func_6800
mod = relay.transform.InferType()(mod)
mutated_mod['func_6800'] = func_6800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6800_call = mutated_mod.get_global_var('func_6800')
call_6801 = func_6800_call()
output = call_6801
func_6802 = relay.Function([], output)
mutated_mod['func_6802'] = func_6802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_6827 = func_2090_call()
call_6828 = func_2090_call()
output = relay.Tuple([call_6827,])
output2 = relay.Tuple([call_6828,])
func_6838 = relay.Function([], output)
mod['func_6838'] = func_6838
mod = relay.transform.InferType()(mod)
mutated_mod['func_6838'] = func_6838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6838_call = mutated_mod.get_global_var('func_6838')
call_6839 = func_6838_call()
output = call_6839
func_6840 = relay.Function([], output)
mutated_mod['func_6840'] = func_6840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4232_call = mod.get_global_var('func_4232')
func_4233_call = mutated_mod.get_global_var('func_4233')
call_6843 = relay.TupleGetItem(func_4232_call(), 0)
call_6844 = relay.TupleGetItem(func_4233_call(), 0)
func_3296_call = mod.get_global_var('func_3296')
func_3299_call = mutated_mod.get_global_var('func_3299')
const_6856 = relay.const([3.854040,-3.725071,9.341027,7.708505,-3.428991,-8.570241,-3.429250,-0.851288,-4.249027,-2.457898,-7.512622,6.385344,-8.522103,-7.858181,-1.974319,-8.224735,0.662125,-1.316824,5.734488,-0.986123,-0.500208,2.847074,-3.172696,-8.202817,4.609927,8.310423,8.767628,-6.951079,-3.706227,3.099949,5.206122,7.762210,4.346224,7.763444,2.672633,-2.190271,-7.611210,-9.612953,4.618004,4.221045,-4.930075,-1.970625,8.387998,3.192239,1.250488,0.466114,-7.771448,9.327040,-9.732756,-9.598383,-2.474712,3.750886,8.702162,-1.316727,-6.818758,9.622927,-0.933760,-1.420760,5.517741,-8.752662,-7.753149,1.077085,-4.003471,-7.809843,4.275236,-5.186963,7.599338,5.181267,0.355975,-2.975469,3.547371,-3.635118,6.883250,-2.608156,-9.465620,-0.070733,-9.390769,-3.814130,-1.506737,2.332454,4.386855,-5.032564,6.198804,5.764346,0.085759,-8.388345,-2.544277,-6.232529,7.022455,-2.775477,5.893835,-4.725165,-5.335647,-7.824638,-7.847051,-2.630220,6.425883,-4.626174,-0.623701,-0.119169,7.795014,0.297624,4.855340,-4.870476,-5.182824,7.199823,5.307500,4.186393,-6.240891,-3.762940,2.029450,-4.006898,1.278844,4.368495,6.787841,6.241102,-7.976909,-0.006477,6.930459,-6.130006,0.687362,7.310528,3.105571,-9.927440,0.504344,-8.954290,9.884373,3.726450,-1.407934,6.198649,-8.053690,-9.895009,0.461466,1.255699,6.306278,-2.575667,4.196638,5.904010,-5.760647,-0.227529,5.080196,-0.271945,0.007251,6.273128,-1.718316,1.159291,-2.487737,8.929085,-4.115679,-2.389440,-9.614430,-7.979994,-9.019110,-5.161952,7.267145,-1.246944,-2.478177,-8.795401,8.980417,4.561367,-3.547743,-3.660624,-8.054207,-0.118019,-0.280090,9.453120,5.415989,-6.920494,4.384727,-3.406438,4.821937,7.167991,6.879984,-3.374969,-9.183696,-7.197845,-7.446279,3.466058,-1.163600,-2.189236,-8.060303,1.079747,1.127416,6.563821,-6.233877,-8.516572,6.354711,9.282274,2.400123,3.991654,3.269007,-9.900636,-8.934738,7.671426,7.346899,-8.475873,2.502792,6.853179,6.047119,5.111272], dtype = "float32")#candidate|6856|(200,)|const|float32
call_6855 = relay.TupleGetItem(func_3296_call(relay.reshape(const_6856.astype('float32'), [10, 10, 2])), 1)
call_6857 = relay.TupleGetItem(func_3299_call(relay.reshape(const_6856.astype('float32'), [10, 10, 2])), 1)
output = relay.Tuple([call_6843,call_6855,const_6856,])
output2 = relay.Tuple([call_6844,call_6857,const_6856,])
func_6882 = relay.Function([], output)
mod['func_6882'] = func_6882
mod = relay.transform.InferType()(mod)
mutated_mod['func_6882'] = func_6882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6882_call = mutated_mod.get_global_var('func_6882')
call_6883 = func_6882_call()
output = call_6883
func_6884 = relay.Function([], output)
mutated_mod['func_6884'] = func_6884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3379_call = mod.get_global_var('func_3379')
func_3381_call = mutated_mod.get_global_var('func_3381')
call_6918 = relay.TupleGetItem(func_3379_call(), 0)
call_6919 = relay.TupleGetItem(func_3381_call(), 0)
output = call_6918
output2 = call_6919
func_6923 = relay.Function([], output)
mod['func_6923'] = func_6923
mod = relay.transform.InferType()(mod)
mutated_mod['func_6923'] = func_6923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6923_call = mutated_mod.get_global_var('func_6923')
call_6924 = func_6923_call()
output = call_6924
func_6925 = relay.Function([], output)
mutated_mod['func_6925'] = func_6925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2090_call = mod.get_global_var('func_2090')
func_2092_call = mutated_mod.get_global_var('func_2092')
call_6967 = func_2090_call()
call_6968 = func_2090_call()
output = call_6967
output2 = call_6968
func_7019 = relay.Function([], output)
mod['func_7019'] = func_7019
mod = relay.transform.InferType()(mod)
mutated_mod['func_7019'] = func_7019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7019_call = mutated_mod.get_global_var('func_7019')
call_7020 = func_7019_call()
output = call_7020
func_7021 = relay.Function([], output)
mutated_mod['func_7021'] = func_7021
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1597_call = mod.get_global_var('func_1597')
func_1599_call = mutated_mod.get_global_var('func_1599')
call_7072 = func_1597_call()
call_7073 = func_1597_call()
func_1640_call = mod.get_global_var('func_1640')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_7074 = func_1640_call()
call_7075 = func_1640_call()
output = relay.Tuple([call_7072,call_7074,])
output2 = relay.Tuple([call_7073,call_7075,])
func_7076 = relay.Function([], output)
mod['func_7076'] = func_7076
mod = relay.transform.InferType()(mod)
mutated_mod['func_7076'] = func_7076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7076_call = mutated_mod.get_global_var('func_7076')
call_7077 = func_7076_call()
output = call_7077
func_7078 = relay.Function([], output)
mutated_mod['func_7078'] = func_7078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3547_call = mod.get_global_var('func_3547')
func_3549_call = mutated_mod.get_global_var('func_3549')
call_7079 = func_3547_call()
call_7080 = func_3547_call()
const_7081 = relay.const([[[6.894887,5.100356],[-4.068773,5.444773],[9.289966,-2.800958],[-4.321365,-5.683932],[4.273004,-6.042203],[5.423773,5.872618],[7.465713,-0.369937],[9.952840,5.754182],[5.833808,6.385721],[1.436457,-4.957078]],[[-6.917513,3.160295],[8.859520,-3.429586],[0.614754,-9.489931],[-0.496101,-8.251457],[3.408148,4.408215],[-3.295917,9.260275],[8.341423,5.992303],[-9.478865,6.529690],[-6.245586,5.460424],[3.508187,-9.628541]],[[-0.135921,7.892025],[8.249790,-1.523077],[-2.648175,9.752748],[-7.439494,-5.306392],[9.069660,-5.554633],[2.259009,-9.754608],[1.134511,7.473190],[-3.586220,4.673997],[9.456379,0.147137],[0.480041,4.051868]],[[6.545986,-0.100611],[3.454499,0.583326],[2.166789,-7.741495],[-0.072208,-5.117283],[-1.292057,-6.961118],[-3.005625,4.131355],[-2.398161,-6.661380],[-9.240777,3.496434],[-8.642219,1.749587],[-4.933325,-0.553514]],[[8.462047,-5.185954],[7.213782,9.317693],[6.910612,-1.506512],[9.480036,0.285470],[-2.861596,4.177534],[2.028297,-0.281087],[2.846768,3.373403],[0.829476,9.832002],[6.164387,-0.800499],[-9.395043,-1.632195]],[[7.227674,1.448331],[6.215970,-1.290094],[-0.060127,-5.553241],[-8.554575,3.521924],[9.523010,2.458839],[-3.389267,4.768172],[-1.688313,9.734360],[8.665988,-5.460540],[-3.712147,5.423259],[-0.331975,-9.378578]],[[-2.780333,-1.905327],[1.179016,-8.073484],[1.779954,3.836907],[-3.452105,1.419014],[-4.095871,0.616863],[-4.106140,-5.609183],[-5.339363,-5.223229],[4.977024,0.014792],[-7.898430,-6.747027],[-4.907651,-2.037854]],[[-6.408752,5.686467],[-1.907601,-1.953091],[9.127060,-7.535112],[9.830520,5.716119],[-6.929823,9.358506],[-1.784441,8.943271],[-4.592611,-0.892826],[-9.963900,-1.766450],[8.036051,2.690630],[-3.177665,-1.225205]],[[-4.281690,-0.083043],[-0.216070,2.989224],[2.868135,-0.375755],[8.934709,-5.145999],[-7.883260,-5.559390],[0.742013,4.875022],[0.659040,-9.382667],[-6.349023,0.044306],[7.583411,4.663709],[9.148056,1.194048]],[[4.991530,-1.795520],[9.001956,-9.004412],[-1.657963,9.033089],[-2.708541,-4.898518],[4.106989,1.022849],[2.687945,-8.032558],[-5.799819,-2.363756],[-4.224523,1.073452],[-5.296309,0.825863],[-9.270584,1.106244]]], dtype = "float32")#candidate|7081|(10, 10, 2)|const|float32
bop_7082 = relay.mod(call_7079.astype('float32'), relay.reshape(const_7081.astype('float32'), relay.shape_of(call_7079))) # shape=(10, 10, 2)
bop_7085 = relay.mod(call_7080.astype('float32'), relay.reshape(const_7081.astype('float32'), relay.shape_of(call_7080))) # shape=(10, 10, 2)
uop_7093 = relay.asinh(bop_7082.astype('float64')) # shape=(10, 10, 2)
uop_7095 = relay.asinh(bop_7085.astype('float64')) # shape=(10, 10, 2)
output = relay.Tuple([uop_7093,])
output2 = relay.Tuple([uop_7095,])
func_7096 = relay.Function([], output)
mod['func_7096'] = func_7096
mod = relay.transform.InferType()(mod)
output = func_7096()
func_7097 = relay.Function([], output)
mutated_mod['func_7097'] = func_7097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5086_call = mod.get_global_var('func_5086')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_7103 = relay.TupleGetItem(func_5086_call(), 0)
call_7104 = relay.TupleGetItem(func_5087_call(), 0)
func_2142_call = mod.get_global_var('func_2142')
func_2144_call = mutated_mod.get_global_var('func_2144')
var_7106 = relay.var("var_7106", dtype = "float32", shape = (200,))#candidate|7106|(200,)|var|float32
call_7105 = relay.TupleGetItem(func_2142_call(relay.reshape(var_7106.astype('float32'), [10, 10, 2])), 1)
call_7107 = relay.TupleGetItem(func_2144_call(relay.reshape(var_7106.astype('float32'), [10, 10, 2])), 1)
bop_7118 = relay.divide(call_7105.astype('float32'), relay.reshape(var_7106.astype('float32'), relay.shape_of(call_7105))) # shape=(10, 10, 2)
bop_7121 = relay.divide(call_7107.astype('float32'), relay.reshape(var_7106.astype('float32'), relay.shape_of(call_7107))) # shape=(10, 10, 2)
output = relay.Tuple([call_7103,bop_7118,])
output2 = relay.Tuple([call_7104,bop_7121,])
func_7123 = relay.Function([var_7106,], output)
mod['func_7123'] = func_7123
mod = relay.transform.InferType()(mod)
var_7124 = relay.var("var_7124", dtype = "float32", shape = (200,))#candidate|7124|(200,)|var|float32
output = func_7123(var_7124)
func_7125 = relay.Function([var_7124], output)
mutated_mod['func_7125'] = func_7125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5093_call = mod.get_global_var('func_5093')
func_5095_call = mutated_mod.get_global_var('func_5095')
call_7132 = func_5093_call()
call_7133 = func_5093_call()
output = relay.Tuple([call_7132,])
output2 = relay.Tuple([call_7133,])
func_7150 = relay.Function([], output)
mod['func_7150'] = func_7150
mod = relay.transform.InferType()(mod)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7150_call = mutated_mod.get_global_var('func_7150')
call_7151 = func_7150_call()
output = call_7151
func_7152 = relay.Function([], output)
mutated_mod['func_7152'] = func_7152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2676_call = mod.get_global_var('func_2676')
func_2678_call = mutated_mod.get_global_var('func_2678')
call_7166 = relay.TupleGetItem(func_2676_call(), 0)
call_7167 = relay.TupleGetItem(func_2678_call(), 0)
func_7076_call = mod.get_global_var('func_7076')
func_7078_call = mutated_mod.get_global_var('func_7078')
call_7172 = relay.TupleGetItem(func_7076_call(), 0)
call_7173 = relay.TupleGetItem(func_7078_call(), 0)
uop_7175 = relay.erf(call_7166.astype('float64')) # shape=(10, 1, 2)
uop_7177 = relay.erf(call_7167.astype('float64')) # shape=(10, 1, 2)
func_474_call = mod.get_global_var('func_474')
func_476_call = mutated_mod.get_global_var('func_476')
const_7181 = relay.const([9,-10,2,-10,-6,-4,-5,-4,-2,6,-1,1,-5,-8,3,-4,9,7,-7,-2,6,-9,-4,3,-9,-6,-7,2,-7,6,4,-2,3,-4,-10,3,-2,-8,-7,-4,7,7,-6,-6,1,-5,-4,-10,8,-9,-10,-6,-7,1,-5,-10,-7,-8,8,-10,-8,4,1,2,7,10,4,-2,-2,4,-1,10,1,-3,-4,10,7,5,-9,9,-8,5,-9,-4,-1,-8,5,2,-8,7,-7,3,10,-4,-6,-6,2,-6,-10,1,9,6,9,-9,3,8,-2,6,2,-2,-2,3,-2,4,9,5,-7,3,-9,3,-10,-5,-6,8,-2,-6,-1,-8,-8,-4,10,-9,2,-4,-6,-4,10,3,-10,-1,3,7,-6,8,-9,-5,2,7,7,5,-8,4,-8,-5,-9,-1,4,8,-2,8,-9,-2,8,-4,-3,-10,10,1,10,8,-2,4,6,-10,8,-10,10,7,3,10,-4,7,4,-6,3,4,3,-3,-9,7,-8,6,1,5,7,-10,-8,9,-4,-6,6,-2,9,-10,-8,-8,8,-6,7,4,9,-7,10,10,-10,1,-8,7,-10,-8,5,-7,-9,-3,6,-10,-1,3,6,7,10,2,-3,-7,-7,5,10,7,7,-4,7,-8,-5,-10,-2,7,-7,10,-9,6,2,9,3,1,-6,-1,-3,1,-9,8,-2,-5,-5,8,4,1,-5,-9,-8,6,-7,9,7,-7,5,-2,-2,5,-4,3,-8,5,5,-2,4,9,7,9,-9,2,6,10,-9,-7,-9,10,-3,9,-8,-2,-8,-2,-8,9,-1,-3,3,5,8,6,2,-5,2,4,-6,10,7,9,7,3,8,-3,1,6,9,7,9,-8,-7,-1,-7,4,-5,9,2,-7,10,-3,9,-10,-1,-2,10,-1,2,-7,3,5,6,-9,6,1,10,-6,-3,-1,-3,5,5,-10,8,-6,-1,-8,-4,7,6,7,2,-7,10,-7,1,8,-8,2,8,-6,10,-5,-2,6,10,6,-9,-5,2,-3,6,10,-2,9], dtype = "int8")#candidate|7181|(392,)|const|int8
call_7180 = func_474_call(relay.reshape(const_7181.astype('int8'), [7, 8, 7]))
call_7182 = func_474_call(relay.reshape(const_7181.astype('int8'), [7, 8, 7]))
uop_7191 = relay.acos(uop_7175.astype('float32')) # shape=(10, 1, 2)
uop_7193 = relay.acos(uop_7177.astype('float32')) # shape=(10, 1, 2)
output = relay.Tuple([call_7172,call_7180,const_7181,uop_7191,])
output2 = relay.Tuple([call_7173,call_7182,const_7181,uop_7193,])
func_7194 = relay.Function([], output)
mod['func_7194'] = func_7194
mod = relay.transform.InferType()(mod)
mutated_mod['func_7194'] = func_7194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7194_call = mutated_mod.get_global_var('func_7194')
call_7195 = func_7194_call()
output = call_7195
func_7196 = relay.Function([], output)
mutated_mod['func_7196'] = func_7196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3189_call = mod.get_global_var('func_3189')
func_3191_call = mutated_mod.get_global_var('func_3191')
call_7205 = relay.TupleGetItem(func_3189_call(), 2)
call_7206 = relay.TupleGetItem(func_3191_call(), 2)
func_4165_call = mod.get_global_var('func_4165')
func_4167_call = mutated_mod.get_global_var('func_4167')
call_7212 = func_4165_call()
call_7213 = func_4165_call()
func_4723_call = mod.get_global_var('func_4723')
func_4724_call = mutated_mod.get_global_var('func_4724')
call_7234 = func_4723_call()
call_7235 = func_4723_call()
output = relay.Tuple([call_7205,call_7212,call_7234,])
output2 = relay.Tuple([call_7206,call_7213,call_7235,])
func_7240 = relay.Function([], output)
mod['func_7240'] = func_7240
mod = relay.transform.InferType()(mod)
output = func_7240()
func_7241 = relay.Function([], output)
mutated_mod['func_7241'] = func_7241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3001_call = mod.get_global_var('func_3001')
func_3003_call = mutated_mod.get_global_var('func_3003')
call_7252 = func_3001_call()
call_7253 = func_3001_call()
output = relay.Tuple([call_7252,])
output2 = relay.Tuple([call_7253,])
func_7258 = relay.Function([], output)
mod['func_7258'] = func_7258
mod = relay.transform.InferType()(mod)
output = func_7258()
func_7259 = relay.Function([], output)
mutated_mod['func_7259'] = func_7259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3603_call = mod.get_global_var('func_3603')
func_3604_call = mutated_mod.get_global_var('func_3604')
call_7268 = relay.TupleGetItem(func_3603_call(), 0)
call_7269 = relay.TupleGetItem(func_3604_call(), 0)
func_7096_call = mod.get_global_var('func_7096')
func_7097_call = mutated_mod.get_global_var('func_7097')
call_7280 = relay.TupleGetItem(func_7096_call(), 0)
call_7281 = relay.TupleGetItem(func_7097_call(), 0)
func_3547_call = mod.get_global_var('func_3547')
func_3549_call = mutated_mod.get_global_var('func_3549')
call_7299 = func_3547_call()
call_7300 = func_3547_call()
output = relay.Tuple([call_7268,call_7280,call_7299,])
output2 = relay.Tuple([call_7269,call_7281,call_7300,])
func_7318 = relay.Function([], output)
mod['func_7318'] = func_7318
mod = relay.transform.InferType()(mod)
mutated_mod['func_7318'] = func_7318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7318_call = mutated_mod.get_global_var('func_7318')
call_7319 = func_7318_call()
output = call_7319
func_7320 = relay.Function([], output)
mutated_mod['func_7320'] = func_7320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3130_call = mod.get_global_var('func_3130')
func_3132_call = mutated_mod.get_global_var('func_3132')
call_7371 = relay.TupleGetItem(func_3130_call(), 0)
call_7372 = relay.TupleGetItem(func_3132_call(), 0)
output = call_7371
output2 = call_7372
func_7373 = relay.Function([], output)
mod['func_7373'] = func_7373
mod = relay.transform.InferType()(mod)
output = func_7373()
func_7374 = relay.Function([], output)
mutated_mod['func_7374'] = func_7374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4300_call = mod.get_global_var('func_4300')
func_4302_call = mutated_mod.get_global_var('func_4302')
call_7377 = func_4300_call()
call_7378 = func_4300_call()
func_6790_call = mod.get_global_var('func_6790')
func_6792_call = mutated_mod.get_global_var('func_6792')
call_7400 = relay.TupleGetItem(func_6790_call(), 2)
call_7401 = relay.TupleGetItem(func_6792_call(), 2)
func_4484_call = mod.get_global_var('func_4484')
func_4486_call = mutated_mod.get_global_var('func_4486')
call_7404 = relay.TupleGetItem(func_4484_call(), 1)
call_7405 = relay.TupleGetItem(func_4486_call(), 1)
func_2463_call = mod.get_global_var('func_2463')
func_2467_call = mutated_mod.get_global_var('func_2467')
const_7412 = relay.const([2.408335,-5.706754,5.169952,-1.722329,1.781682,8.062409,-0.354969,9.097748,5.217947,-7.665867,-9.921839,-7.292181,7.949552,0.303322,-4.422095,-7.630647,4.922960,-6.016859,5.038255,0.842563,-3.246558,-9.110023,-5.040611,9.291700,-7.638500,-9.811871,0.114306,2.172443,6.098861,-6.314413,-7.054044,-7.128084,5.209815,-3.167892,7.654283,7.540820,-7.985104,5.068274,7.759013,-0.161439,-2.173492,-5.089113,0.765986,-5.417223,7.372779,-1.684958,0.281453,8.373712,2.062969,4.264682,-1.696047,0.523122,-4.488936,0.401728,6.398191,8.050891,-4.894759,7.282922,8.081324,4.231371,-1.496799,-9.715069,-0.514655,4.969679,8.459440,-7.477914,2.275310,-0.274229,-6.912462,-5.387791,2.078361,0.053404,2.762466,0.876194,-8.779526,0.300474,3.070225,-9.857196,-7.552170,9.798824,4.004925,2.834853,0.274336,-4.725084,7.812646,4.670423,6.769947,-5.937737,-8.690307,2.956031,-9.162866,5.871058,9.761120,7.831712,3.810813,3.764847,5.946705,-3.801938,9.435943,-5.481322,0.308626,0.495805,8.851783,1.506006,-7.339436,-5.103478,-7.558313,-2.535083,-7.393489,3.501983,-0.665396,-6.722757,1.012461,6.303255,8.782563,9.144793,5.293950,3.302734,-9.942444,-6.691603,-4.913124,-3.628735,2.519477,-0.269789,-7.880655,3.747216,-0.194757,-0.062152,-7.053010,-5.339436,-8.955540,-2.081660,8.333877,-5.957037,7.040160,-9.587347,2.199011,-7.771149,4.927365,-7.909082,-1.005791,-3.257658,5.931892,-4.446711,-4.187676,-2.071013,-2.804496,4.956931,-8.671694,1.166250,-2.957411,0.869553,-0.159083,-3.791841,-1.596983,-5.821813,4.821238,-6.069097,1.880486,-5.036219,4.080509,-1.751418,-9.816063,0.821765,7.089407,-8.063745,-6.557072,-9.976159,4.475471,-2.747644,9.898837,-2.356283,-9.158870,-2.286928,9.703781,3.483377,5.599990,-8.004872,6.029996,-3.191960,-6.358519,8.052469,5.837120,-8.471604,-3.978047,-0.807994,6.371016,-5.161669,5.055137,7.337734,-6.160226,-6.967911,1.302598,3.929501,-4.524372,6.131213,-0.024789,-6.173441,-4.724051,-9.870116,8.827348,1.654409,3.322726,-1.010373,-2.170814,2.338605,6.106275,-3.246914,-2.034414,4.500682,4.079711,9.519726,5.263668,9.129373,-2.764246,8.792772,6.261802,-7.029640,-2.714468,5.109172,8.313955,1.561890,-9.345625,8.487454,2.542582,-8.045860,4.470598,-1.428828,7.672789,4.475020,1.871440,8.883319,8.161836,9.210444,0.152109,-3.348345,3.862232,6.847562,1.383771,-6.514283,1.102528,0.856826,3.348639,-7.444146,-0.742522,-8.344275,-4.968766,-6.364245,-4.413526,5.081181,-5.361351,-8.080314,-4.232514,-4.927055,-6.019288,-7.661105,7.568191,-0.025901,-3.169207,2.474367,-7.765403,-5.865348,4.224149,-1.388683,5.218927,6.903860,7.266009,3.168067,2.960061,5.972143,8.810774,-3.778816,-1.226765,9.661081,4.601665,8.392570,-8.225316,-9.887199,-7.697331,9.194696,-7.709935,9.081281,-1.637735,8.047555,-9.790965,0.470628,7.193004,-5.507231,5.272878,-3.244430,-3.810421,-5.045703,3.510857,2.826597,-4.270538,8.495031,7.630712,-1.250106,-3.976468,-0.524962,2.360388,-3.648086,0.118715,-7.923414,-9.729471,2.930960,-8.025381,4.120278,-5.467111,6.201808,-7.211772,7.189765,4.153981,8.037727,-7.235803,6.247671,-2.586773,-6.440859,-2.569645,-7.546796,1.208297,-3.279207,1.799684,1.751521,-5.228126,-3.444257,-6.831846,-3.626091,-1.894787,2.462903,9.935029,-6.259437,-8.675213,8.040993,6.883686,3.155696,1.210470,-4.647127,5.683318,-2.866135,-3.743567,-6.820465,5.291247,-7.511142,5.244898,-9.637824,-7.598718,-4.586951,5.331128,-5.507180,2.100510,1.751551,7.170451,8.267868,7.609326,-1.658609,8.073609,-8.065945,0.485797,-6.511507,-0.943050,-5.581462,4.540468,1.068934,-8.913959,8.961233,1.593734,4.810971,-4.240303,-4.520654,-8.298534,2.248773,8.017051,-5.981201,-2.852970,8.102693,3.132941,-0.460557,-6.381449,4.268758,7.313065,-7.350728,9.473898,0.828428,5.689501,-5.827481,-1.745109,1.971238,2.576504,-2.844279,-4.015720,0.964996,6.858190,-2.701843,3.208771,6.496984,-8.553694,-9.886118,3.889204,1.414703,2.985862,-2.221830,5.539739,8.549370,-1.759263,-3.325370,-6.316986,-1.566253,7.312724,3.430801,2.524563,9.768098,3.837587,3.164376,4.390433,2.269423,-3.071424,-9.824816,6.751439,2.403742,-0.142554,-8.677484,4.543764,-7.764453,1.547848,7.880856,-3.431090,-1.821090,-8.198244,-6.917132,-9.359165,-6.143018,-0.049488,-4.135634,1.006267,8.087002,9.876101,-5.788678,-5.181962,-0.112290,-7.494604,-2.044981,-3.051449,-3.742798,2.333441,2.549157,-7.302987,-6.875652,-4.123320,-6.055458,-0.041409,4.896259,3.095293,-5.680603,2.128915,5.043471,6.683753,-6.098807,-4.872589,-3.594493,-7.357018,0.735737,-6.499190,0.082224,-8.864260,-2.212296,0.747478,3.413913,2.489264,-2.241937,-8.360882,-5.201203,-5.192891,9.320999,-9.625561,-0.744398,3.891132,9.450595,9.541435,3.096064,4.208063,1.137490,7.249673,6.328389,-6.108263,3.869945,-5.411335,-0.661971,6.979603,3.072269,-5.671623,-2.902402,-4.025509,2.839963,-8.994420,1.179522,-7.980890,-7.087235,5.184548,-4.341884,2.738706,-3.077280,7.189225,-0.491345,3.883877,-1.497173,7.812491,7.439356,5.015161,-8.307300,2.886369,7.188262,-8.926595,-8.400491,0.112749,5.926256,-9.547608,-6.540423,6.871378,-9.908201,2.881552,-8.172803,7.192518,-5.487051,-2.463093,-9.219885,-8.726255,8.517250,0.307510,7.439638,-5.124163,-9.471234,-8.582950,-6.483752,7.843709,-6.709900,-4.082532,-3.293750,7.335334,-7.596342,9.915525,9.263294,-0.711791,-4.153236,-9.605978,-6.035387,-8.964152,-0.412890,-1.046011,-0.616255,8.038088,-5.014890,8.929148,-2.947524,3.000392,-9.319165,4.999576,-9.750823,-1.299643,-5.323365,-9.215437,0.565043,6.599642,-0.902247,8.619454,2.946996,8.097803,-6.704370,-1.351046,5.495866,4.888340,-6.684278,-2.785048,-2.516842,2.397531,3.834390,4.562491,9.507129,-3.211867,-1.036743,-2.419880,1.914060,2.356085,7.596187,-7.783551,2.546903,-5.132567,-9.199402,9.648040,-6.055689,3.412754,-3.762937,-6.663438,0.088906,1.052649,-6.895934,-0.494713,-4.515523,6.945661,4.906550,-8.907757,4.664073,5.697851,2.167268,-6.023630,4.318365,-3.535568,2.678070,8.099484,7.304887,-8.782784,0.372761,1.113975,0.710140,3.229009,-2.656565,0.865373,-1.966283,-9.392365,8.355254,3.495564,-8.586394,9.273543,6.243891,6.690088,2.734828,-4.510267,-6.715826,-5.343363,7.906302,-8.729869,-0.077458,9.423842,-1.131704,-3.461637,8.529689,0.741599,9.588073,7.215319,3.915023,-9.375091,-1.892188,9.198000,-9.646111,-9.037086,5.765355,-1.927693,0.541452,4.859970,6.249533,1.367460,4.183817,-5.062867,0.047819,2.953095,-7.009119,-6.220027,3.834209,3.244246,7.654704,6.424869,4.158772,-1.843538,8.752918,-0.986068,-6.800451,4.217383,-6.956804,-2.313812,9.775663,5.622242,8.712108,4.853890,4.040547,4.083146,-1.437305,-5.369674,-5.884527,-8.381677,-9.187748,-4.479542,1.205820,-3.432253,8.342523,1.651667,0.512853,1.806866,-2.072528,8.146016,0.572193,5.724826,1.781175,3.193661,-0.354142,3.044108,7.958101,0.496216,-8.114842,-6.646582,8.376861,-2.231189,-6.091382,3.956749,-5.865485,9.129873,5.780506,-8.562008,-5.765098,-1.586875,8.296472,3.723470,7.921352,1.467642,-3.740200,-0.613288,-5.734107,-2.387109,-3.780937,6.517987,-5.375379,-4.505622,9.398460,-9.575120,2.074363,6.445141,8.905220,7.518739,5.371595,-7.780189,-5.936548,4.089688,9.216672,-2.624766,-2.372318,8.137266,-2.026722,-8.289229,-2.208259,0.993663,-8.168359,-5.628071,2.089533,-2.996190,0.064760,-8.684061,9.119417,-2.835447,-5.424520,-2.354620,-1.074447,9.958148,-0.937840,6.698985,3.232876,-4.157161,3.421253,7.506731,-0.583613,7.185503,-4.966426,2.675352,-6.580298,-0.252779,-1.429693,9.823978,-2.982392,8.776952,-4.354030,0.886625,0.860908,3.483718,8.535072,9.896956,2.384123,9.642055,3.778644,8.664919,-1.464558,-8.575147,9.525997,0.833019,-9.040424,-0.357407,3.185119,-5.969899,3.909607,0.077112,-7.502392,-2.956778,-3.874151,5.709249,-6.209743,4.648569,9.926103,-6.073594,0.836609,-7.807355,-7.290339,-0.780729,3.239941,2.772717,0.944901,0.152277,6.213550,2.797813,8.382208,6.188167,0.304909,-3.885982,-9.390477,4.977911,-7.957171,-1.597090,-9.841037,0.104560,4.947387,-8.308862,9.716006,2.086835,5.203860,-8.458358,7.765212,5.321171,-8.807530,1.727326,-9.885654,-8.459235,4.040221,6.767688,-0.756055,9.783369,5.689873,-0.940328,6.320215,-0.262277,-3.915830,0.444857,-3.044707,-1.925950,-8.374615,-9.780896,9.761868,4.498629,6.414143,-7.713684,0.678548,0.088306,-0.155041,-5.222998,5.252516,-6.089034,2.344592,-1.624999,-6.339724,3.836104,-4.125915,3.096446,-1.028686,-8.621788,-3.215874,7.741758,-9.386113,-8.216074,-6.875133,-2.909106,5.589959,0.052978,-7.415402,6.068812,8.208253,2.025692,-1.256813,4.295191,-7.058579,-6.137206,-5.207013,-1.117197,-6.216883,2.665616,7.772988,4.083260,6.768132,-9.077980,-0.965129,-9.098326,-7.151078,4.941676,9.868790,7.252105,2.753953,-5.821640,-4.035666,-0.625835,8.329576,0.071358,-2.131742,-6.703128,-4.371408,1.406831,-1.761601,-8.357572,-3.438507,6.822996,-1.016487,0.106775,-7.211471,6.820908,-5.737833,8.269730,-6.811264,2.523973,0.376621,-3.162469,-5.650812,-1.875083,0.098291,4.057125,3.819283,3.358751,4.091748,0.168065,-8.081935,-2.048450,-5.117610,1.573927,6.023132,6.741316,-9.772618,-0.536478,-8.181946,0.224241,1.217843,2.342943,0.759469,-5.028337,4.335384,-5.552717,-6.199037,-2.606101,-3.181640,7.786536,-5.322328,2.803501,-3.150750,5.091389,-7.260700,0.027929,9.679417,-9.212635,6.712384,-3.629792,-6.704304,9.005161,5.993608,-8.918420,8.054326,0.605021,-3.563589,-3.090675,-7.422208,3.686858,-7.186316,-9.082015,5.813143,-0.147046,4.849672,8.047135,4.419566,3.179817,2.070865,-0.995056,6.742002,-8.238229,-7.561970,1.944391,4.097615,-1.227314,3.411345,0.088091,1.167311,2.974627,-0.004568,9.144067,0.943447,8.911164,-6.632858,8.196904,5.692596,8.524869,-1.316329,8.251090,-7.416496,8.461862,-7.387444,-3.670187,-3.768797,5.868760,2.191912,-1.628488,1.453598,3.633977,-3.722469,4.368836,-9.970855,5.061727,8.424266,-3.542449,-8.285394,2.916755,9.825428,5.863407,-9.207512,-3.735530,0.654813,-1.791363,-4.044215,-5.223769,5.676841,5.921865,-7.115909,-8.960456,4.012789,1.258826,6.328028,-4.433850,1.006455,-4.823782,-0.719333,9.791531,-0.351509,-2.879249,9.663213,3.120560,1.269751,-8.666217,3.522601,6.817468,-0.946493,3.328176,-3.093281,-3.968124,2.246764,8.379872,1.135577,9.334683,-3.061548,0.771632,-6.437281,-2.366623,9.570736,9.924753,-9.176989,8.716255,-0.154517,-6.895373,-6.073914,-8.666376,1.471474,-3.067617,-2.732798,-2.297905,6.465038,-0.585964,-4.563251,1.864107,4.945953,0.920286,-7.259779,-8.295823,0.264356,6.247365,8.609231,7.717029,1.870701,-9.419722,4.758930,-2.251751,-9.292071,-4.209759,-6.714238,-1.169677,-5.772561,7.027987,-7.632725,8.646014,-4.726139,5.524345,-2.492775,-7.531881,-5.174823,3.974179,-8.795682,7.102889,-6.993357,9.779995,4.556800,1.598732,9.065495,-7.897829,-2.746818,9.539490,-7.506094,8.034963,1.853866,-0.049188,-2.548169,9.026463,-5.614910,1.763944,-7.655487,2.252439,-3.979821,-9.590186,8.023007,2.585926,-4.067778,-6.455655,7.235168,-3.030158,2.688169,8.854718,-1.059208,-9.550738,6.109551,-2.613815,9.136915,8.054237,-9.518979,8.346453,7.942730,9.044868,-4.776734,-5.322144,1.848965,-7.264863,-7.068689,-7.320398,2.570856,6.461525,-9.481851,-1.317980,0.714706,5.894939,2.508094,7.139665,2.443732,8.010373,-9.400711,-8.325725,-0.804399,-3.261919,-8.007402,9.471648,-7.135922,-3.776861,-2.500034,-2.240413,-0.909935,8.486215,-6.335452,-0.695308,-2.963697,7.320269,-5.576741,-8.790367,1.525514,4.250019,-0.586221,8.583961,3.431638,8.865332,-5.575174,3.909557,-3.544551,7.173897,5.868666,-0.415789,1.914291,-3.136632,5.856990,-5.332994,0.691682,-0.847385,-8.505527,-6.221189,7.003529,-7.126951,6.677018,4.151599,-0.593708,7.011271,-9.334917,0.221922,6.061814,9.729755,8.189720,6.274376,1.089099,-5.394045,7.120716,2.813157,-9.694790,4.437985,8.250942,6.356644,1.892281,4.082215,4.607478,6.864472,-3.454854,0.844433,-2.560003,9.430284,8.969426,4.910892,-5.461722,7.472200,-1.902451,4.598466,3.176463,-0.221297,8.384964,4.352068,-2.203480,2.069109,8.234236,-7.979565,-8.726404,-4.844466,2.858758,-6.254531,-0.292610,2.583799,-7.944023,0.498881,7.654964,-6.027528,5.578462,2.940935,-7.151416,5.082413,-1.657622,7.425275,3.170253,-6.432147,-2.640027,-1.822820,-7.723132,4.195418,-8.826951,1.734134,-4.191309,-5.740992,4.098217,-0.091347,7.800907,7.002733,1.344405,-5.797203,-2.819442,-3.507233,3.313825,-7.167795,-2.906285,4.827696,-8.286648,-0.568153,-5.852236,-2.261297,4.883036,-9.668536,-4.004778,-9.701929,-6.433475,-4.347115,0.924216,4.110659,-0.848165,-9.288283,-2.840896,7.138223,-9.218341,6.784024,8.067633,-7.924044,-1.482959,6.221324,1.432675,7.601991,-1.871408,-8.063849,-3.875384,-9.816663,6.792680,3.226541,-3.183550,-9.099491,-3.666990,-5.764055,-3.397708,-7.511095,1.669532,1.913149,6.477295,-5.602596,9.275562,1.972617,5.323204,-0.194057,2.197600,-4.114765,-4.186002,-2.901536,-9.716671,-8.229133,-6.781794,-0.164427,-1.696427,-1.807304,-7.706585,1.597082,5.746984,2.158058,2.170608,-5.588167,2.225761,-1.270726,5.424222,-5.460935,1.403963,-1.881858,-3.292815,5.133785,1.385615,-6.019770,7.362896,4.956913,1.364669,3.161018,-4.628861,4.217939,-9.035393,5.991206,-9.036320,4.283154,6.964852,6.944580,-8.582052,-6.412327,-4.356107,4.786940,1.503862,2.920043,5.659151,6.167791,-8.881476,3.942310,-1.785481,-4.988653,2.597460,0.653044,-7.584692,-7.386653,3.225059,-6.504499,3.473858,5.180432,-3.366022,7.621378,2.744231,0.731639,6.403266,-9.095070,1.632533,7.348865,1.425801,5.009543,4.872160,-6.283054,6.690342,6.235022,3.540949,6.605181,0.884508,7.537827,1.499587,-0.921695,-5.072563,-2.476410,9.967730,-3.776282,-9.485408,-7.479148,1.999498,8.518908,2.606789,9.550673,9.868862,-1.508997,-3.768883,-4.333323,-1.563467,-3.005914,7.640996,5.305867,-5.647570,0.432561,5.272764,8.894529,7.142725,0.803685,8.308297,7.069022,8.135971,5.043030,8.401799,9.382857,-2.055091,-3.071035,8.509115,-8.266907,0.160050,-6.262882,-8.845204,3.719866,-9.560341,-1.035688,-3.976551,6.397260,-3.563291,8.582595,-6.726658,2.427540,-4.009309,-1.025347,2.970707,-2.112643,0.317178,-6.798589,-7.568355,7.722919,-1.322949,-2.448780,0.070807,6.475676,-8.914611,9.119072,0.180351,7.092793,3.288502,6.344975,-5.056389,6.387601,5.084453,8.500009,-8.060909,-5.354944,6.937520,0.623020,-3.478741,-8.210402,0.159120,8.318805,-1.729803,-9.463306,2.509785,8.106427,6.364703,9.630995,-4.308072,-8.553734,5.402514,9.709193,0.887015,3.557809,2.790098,-5.639924,4.526765,-3.178341,-5.383251,9.731639,-6.208343,-8.579505,-5.584989,-5.096602,-4.886287,7.284163,-3.854301,-8.932310,6.818832,0.886290,3.442193,0.034725,-4.983844,6.960108,-8.064020,-4.593534,4.425045,2.402213,-4.831128,-3.422859,-3.864478,-4.541027,-7.436386,4.691523,-0.717917,3.411291,-7.277697,-8.564311,-9.975746,-8.896788,4.658236,3.514534,5.519935,-9.455810,7.750019,-8.483467,-4.772765,-0.930125,-6.904190,-6.913121,-2.676553,-4.354724,-9.733546,5.850764,-0.433060,0.292142,-7.043726,-7.897374,1.385758,3.821530,8.318618,0.015999,-3.321367,7.440591,6.908786,0.339985,3.924901,-7.674435,4.338862,-4.125669,8.021017,6.261726,-5.305016,1.187849,-8.815395,-8.532054,8.565564,5.654021,1.093746,-2.604350,-7.108189,6.762207,5.446969,8.273981,2.457285,7.181812,5.751827,6.063506,-4.613953,-3.845587,0.985615,4.642459,-0.625667,7.073707,9.406320,-2.650078,0.232737,7.153898,3.303333,9.301472,-3.576543,-5.707869,5.123091,5.635188,-7.803436,-3.261224,7.003492,-8.333881,-6.078873,3.444006,5.186477,8.387825,3.949926,-4.578492,9.192533,-6.073669,-1.552906,-6.369267,-0.081594,9.508101,1.776137,-3.339385,3.914569,-9.497700,-7.743578,8.364996,4.832224,4.417468,9.611367,3.478089,9.906795,-5.595514,-1.746583,-1.384994,1.231110,-8.503247,1.934689,7.135812,9.453380,1.861014,2.228299,-2.430171,7.515613,-2.905205,6.539459,-7.286195,8.812596,-0.120402,7.384213,-0.291028,-2.050769,3.089730,2.395028,0.029918,-2.510704,2.683270,7.801797,-0.231646,9.612458,-6.207604,-6.702579,7.002780,5.937095,-7.752095,-9.116257,4.716247,8.617652,0.448044,0.023971,3.044682,7.038537,-2.717776,-7.471325,0.974670,4.240372,-6.841935,-4.292098,0.433382,1.279816,-5.046917,-7.027326,5.071631,-6.574970,-9.385863,9.776388,9.342886,-1.432818,0.549054,-0.807410,-2.784014,-7.102770,-7.339422,0.659764,1.220007,7.444738,-7.928281,5.819540,6.921898,-6.318581,-0.477290,3.804307,-5.297079,0.713307,8.773339,3.006420,5.068717,-1.287140,-0.196527,0.672613,1.504720,-8.826338,-9.571457,2.160334,0.679436,8.019076,7.870590,-2.022612,7.770368,5.806471,5.537666,-2.693404,4.698114,-7.007555,-0.602537,5.903381,-6.070971,-1.153667,5.031868,-9.346441,1.610570,-2.815708,6.573979,9.306073,-0.604318,9.139106,2.614744,-7.022319,-8.728729,-9.908000,-9.494068,-6.215762,1.725847,7.987712,-4.634615,-2.579863,-4.370899,-3.609496,8.874701,-6.055568,9.554002,5.766076,0.416770,2.978525,6.981252,6.653997,0.554985,-4.729867,-0.003404,6.874860,-5.358453,-5.338094,2.297432,-9.491261,-5.108486,-0.267109,-0.658524,-7.795698,-3.497943,3.109384,-7.840744,2.714835,7.175055,-8.435355,-4.110271,-5.309335,0.409107,2.763838,-6.608464,5.500076,-4.609199,-6.078272,-2.193428,-8.733426,-1.518881,-6.163449,-7.670709,-0.817555,4.057061,3.545048,-5.250331,-6.248295,7.666324,-5.354932,2.366295,-8.196875,-4.252127,-9.293974,-1.187266,0.419302,5.082735,9.778590,8.773270,9.644828,-8.068311,-2.781095,-0.087906,1.641616,-8.171743,0.576122,2.849896,6.993639,-0.694430,-3.762488,7.039944,8.246539,6.902581,-5.228180,-3.847027,-2.282120,3.669495,-7.840618,4.178242,4.350771,4.530602,-2.581149,-7.903925,-6.731240,1.117290,0.216557,-9.299582,5.889661,6.711471,0.680651,0.513183,9.573084,-6.493815,4.209194,8.568948,-9.248558,1.255612,1.091724,-9.501717,8.843645,9.365413,-6.207030,4.597044,8.993002,-1.498733,0.738251,-1.893003,-8.546656,-3.025690,9.059542,-5.384099,-3.292898,-3.620639,1.313877,-5.397214,-8.824868,-9.648930,7.712979,5.659523,-3.440192,6.686219,5.609902,-5.372876,7.088754,7.717067,-6.958366,-2.614454,-4.546967,6.480537,6.000022,-7.474915,7.065943,9.477913,-6.515682,8.509699,-5.187406,-3.207125,9.451278,9.846055,6.849236,7.880360,-6.469216,9.459166,-9.507835,-4.004434,-3.666951,3.561666,7.050652,-5.827142,6.606400,7.070047,6.791241,-8.563308,-3.302004,5.574674,-7.991802,-9.864029,-8.638872,6.430945,-2.946784,-4.911385,-8.797989,-1.658544,-3.855281,-9.018608,-5.295292,7.095456,9.892838,-6.309419,0.858029,-8.480893,-2.957823,-1.628378,-1.559140,0.650123,-0.392118,2.992229,-3.880348,-4.707287,-1.770421,-0.249390,-7.364804,-9.534943,2.924755,-3.338182,-6.970797,7.639332,3.980853,4.138378,2.456926,-4.185363,9.362040,0.144389,8.540741,-4.550155,-9.520292,-1.948531,6.454223,-0.646374,-9.946677,4.776573,4.695696,8.104361,2.085731,-1.424881,-4.373695,-0.289750,-1.941551,4.649783,7.583315,-5.668919,-3.246220,8.684307,5.178022,3.048597,-3.197231,2.914622,3.762936,-2.683333,6.597330,4.206086,7.174099,2.747152,0.654121,0.780419,9.102973,-9.451979,-5.558408,6.616138,-4.982532,6.083701,8.825382,-6.252417,-1.613726,9.714993,-9.944218,6.816511,-4.589997,6.487004,9.698114,6.896683,-8.484670,-6.697734,0.674295,4.927560,-7.395391,-5.696245,2.433177,-4.753475,7.363209,9.160711,0.062726,5.268740,-1.175403,2.238200,2.156816,-9.800096,3.685859,-3.339114,-8.522880,-1.279417,0.865432,-2.449009,8.073915,-2.530042,9.647980,-4.075582,-7.652904,-9.129015,5.998828,-9.977282,-9.739489,-1.476948,5.513204,-2.768493,-7.091986,7.526367,0.298477,-0.266403,-0.085653,0.667669,4.766463,-5.744073,7.738102,-5.090918,2.676048,2.178682,6.019415,2.488777,6.309032,-4.100114,-8.714090,7.081123,3.962927,-7.410975,-4.984492,3.829134,-7.863560,3.306827,5.292772,-3.334762,-9.207054,-5.120993,2.133144,-8.158911,-4.911692,3.874953,-6.114208,-5.660692,-6.052930,-3.899550,4.683195,-5.516973,0.622005,5.045585,0.945218,2.915646,-4.977076,0.692181,4.383757,-6.826450,-5.835836,-0.829336,-0.309712,6.565548,-4.417949,4.496146,8.827144,5.199265,6.783330,2.169252,-9.306660,-3.324904,6.450081,-4.887304,6.759577,-4.831479,-4.959352,9.280458,1.643263,-7.120013,-1.922205,9.707319,2.855968,-9.832220,-0.007900,-2.197704,1.079755,1.622583,-3.117878,3.908020,-6.762185,-1.178696,6.037338,1.052590,-9.257015,-2.307425,5.997088,-6.997169,-5.230310,2.739335,4.342576,4.662017,-3.977856,8.058707,-1.700846,-8.725279,-1.028033,-2.301769,-9.691715,-5.437380,9.458449,8.793782,2.402976,6.922456,0.687761,-5.361960,-5.908572,5.914044,-9.203113,-3.399110,2.375641,3.864637,9.346923,8.230146,3.813630,-9.617974,-1.659217,6.632752,5.431813,3.517529,4.499256,2.208294,6.831473,-5.027034,6.656372,3.978343,9.823398,-4.474776,-3.692144,6.205365,-0.089754,-2.992386,1.295042,-4.688378,-6.354086,0.389250,4.015091,-6.626383,9.614542,-2.715123,1.959726,-3.991445,-0.224060,6.427327,-3.487646,-9.942857,-0.013962,-1.524303,-1.062917,-1.275271,-8.807340,-4.874733,9.559944,3.780103,1.487844,1.736140,3.712436,0.185450,8.061396,-9.627491,6.734376,-7.639881,8.627163,-0.580564,5.441610,-3.552109,-6.834848,1.678288,3.560338,4.767254,-7.455790,6.366432,-5.157029,5.715392,3.609701,9.486944,-1.268856,-8.800132,-7.319939,5.795078,-2.460061,-6.996711,-7.769701,-7.662357,-8.386585,-8.976357,-5.758299,-9.102548,-5.057632,-9.199928,5.718039,2.288146,4.968385,6.346572,-4.249854,2.429710,-7.912465,0.017965,7.630810,7.709144,9.957273,-8.583945,3.558557,-2.263070,-4.752132,-0.905033,5.762430,0.005528,3.019639,-7.374392,7.792288,-3.993763,3.741188,-3.644688,6.413532,-1.118190,3.815006,0.481419,1.837256,7.679546,-6.699365,5.739876,5.510872,4.758836,2.507224,-4.106233,7.133059,2.317590,-8.079473,-9.109635,2.900847,8.871117,6.238376,6.039253,-8.262103,2.028958,-5.479805,-9.630493,7.050422,0.057717,-4.784898,-5.337838,-5.106036,-7.653186,7.251941,3.037733,-9.364603,-5.879249,8.283298,-9.459525,-9.729343,-5.381727,9.051812,-4.998443,-2.358825,1.253259,7.831376,0.349659,6.530550,-4.584035,-6.080651,6.460195,-7.399438,-4.460595,-5.764753,-7.422294,-5.445140,0.113585,5.716163,2.158300,7.003885,-8.545445,-3.441141,4.311644,-9.856670,-5.619160,1.633511,8.039790,1.092161,1.355154,-6.121605,-5.767558,-8.560950,-1.256658,4.699200,-9.566726,3.367242,2.350569,-3.174326,6.973385,3.139523,7.700409,-7.329904,-8.174847,-1.534239,0.035498,8.710468,-7.683646,7.339034,-3.621905,-9.689096,-9.967609,2.685972,4.856181,-8.866121,-0.765155,-9.529297,-6.214879,-9.376796,3.037656,-9.565979,-7.291103,-5.677400,4.906277,5.062400,3.867685,-7.056426,4.194154,2.339987,1.967416,-1.693329,8.497968,3.647442,0.262309,0.377770,8.949025,2.934504,8.809150,-1.374134,3.054080,-4.581343,5.754690,-8.562167,9.771758,3.122824,3.920066,-3.709742,-6.238773,-5.999438,-4.625453,-5.939976,3.402613,7.914665,-8.917376,-9.431349,6.097186,-9.940343,8.579554,-1.219789,-5.707487,-3.044190,2.395142,8.269918,-4.096959,5.671229,7.170008,-8.015054,2.524581,3.671857,3.357094,5.025097,6.082865,7.581628,7.698065,4.684767,8.634319,8.410873,-5.867424,4.306936,9.129697,3.611408,-8.931182,1.373245,4.912147,2.045503,-3.152555,-9.276298,-6.250527,6.425759,0.824294,-6.252203,-5.157005,3.544494,-0.895974,5.368731,3.141998,-2.852563,6.617497,7.674409,-2.947919,1.040063,4.032432,-0.425043,-9.257426,3.657444,-7.742536,-3.005027,-1.457835,-4.127495,-9.590392,-1.537633,-5.102518,-0.300720,-5.036655,2.634844,-7.270067,-3.124973,-7.445460,-6.906608,-3.753576,-7.231087,9.144152,5.411870,-7.688074,-2.895914,1.185364,-9.130088,4.080181,0.091757,-8.869897,-8.174346,-5.007255,-9.095161,-8.140222,5.693645,1.058751,7.813928,-2.855283,-1.349234,-6.475292,-7.672154,8.694697,-6.804990,8.604016,-3.100186,-6.482100,-6.919668,8.548422,2.494149,4.834513,-8.986128,-4.721226,7.750612,-2.369997,7.872107,-7.197541,5.591330,-9.413722,-8.256182,3.470034,1.792290,-0.475809,-3.619734,-7.856077,9.630273,-9.839120,-4.093384,0.641943,-0.466230,7.912683,1.133629,4.991067,1.402449,-5.100392,4.014636,0.812729,4.171196,-6.733722,7.428425,0.437032,1.485275,7.083160,-7.631071,2.957271,-9.513604,-7.710095,7.423099,-6.293441,9.785319,-1.666995,3.235695,4.164407,5.458157,-9.000557,-8.201652,0.823458,-3.086482,-1.011687,-6.327937,7.710664,-7.897411,-0.143302,0.513525,7.575638,5.363945,4.824805,7.195440,7.922393,-9.801438,5.667868,1.297654,-4.887730,7.047175,-3.422383,4.844125,5.148552,4.712918,4.771566,-4.478918,0.614999,-2.392111,-5.191223,5.819185,9.673905,-8.444899,-1.730063,0.684182,0.530121,4.196499,-0.414562,0.806752,8.282048,3.700507,8.636652,6.967259,8.405361,4.925261,4.145655,3.579792,-5.925498,1.397250,1.800662,-1.693129,-1.893626,-5.683171,-3.801225,-0.272964,-3.195059,-8.538286,7.950491,-0.309222,4.443045,1.932642,-7.420788,6.577844,-0.609596,-7.381472,-5.976458,-7.333448,-2.033525,8.869622,-4.665940,-9.375719,-2.939665,-7.825894,-5.827120,-6.001512,-7.273629,-0.176588,7.255552,7.225307,3.930447,2.048082,-7.622824,-6.010458,8.951106,6.192339,6.087030,-1.059542,-2.933251,5.591428,-7.256718,5.791414,4.878208,8.658842,8.880823,-4.483430,-7.716321,-9.333308,9.836910,-4.538042,6.631224,-7.206806,3.946582,-3.647863,7.985269,8.238097,8.120508,-4.119732,-0.411544,1.171971,5.537970,-6.947472,-1.347558,-6.945340,0.787504,-8.853372,7.679900,9.899551,0.077523,-0.315940,-0.689841,-3.107216,-8.684318,-4.743674,3.128317,1.881029,-1.428112,-6.333863,-5.281096,-0.686707,8.885682,-3.462634,-3.189296,-2.205447,4.696938,-1.373436,-2.613607,-5.061752,-0.396512,0.014703,-8.144196,-4.624086,1.832314,9.211497,9.280064,6.298752,-1.653412,5.780253,-5.270119,2.496797,8.741820,8.950510,-9.344207,-2.491106,-5.052186,-0.498102,-4.215998,2.058717,-5.237013,-6.782792,7.832623,-6.270719,0.245617,-4.116510,9.190011,-7.176858,9.146880,-9.180177,5.415830,-0.003246,2.418860,-6.896773,5.117696,3.812919,3.160881,-0.326644,7.928073,-3.058643,-2.875352,-1.864298,-5.812667,-8.323710,-1.232952,-0.294750,-7.174027,-5.275612,3.656011,1.017293,-6.359107,-2.845263,-5.624989,-1.505556,-7.084898,1.570483,4.699094,-7.796531,-8.040319,-2.124340,-3.850785,-9.183486,7.106694,-3.263876,7.662731,-8.372988,-5.537001,1.206224,1.460241,-7.812274,9.541343,-6.919972,-9.837937,-1.385389,-8.107644,8.485207,8.327850,6.998905,-5.783695,-1.479426,6.376860,-3.348884,5.269406,4.604356,2.318328,-1.409158,1.410894,-2.806124,-5.244123,-9.100147,4.658832,0.909492,9.648262,6.995989,-3.348674,9.463308,-6.299842,5.170153,-0.662422,-2.460239,-6.774707,-3.260794,-4.198156,0.518424,1.541724,9.739800,-4.188887,-1.094956,4.366947,0.119120,6.121714,9.460294,-2.402216,1.301719,8.445998,4.326519,7.173939,5.127605,-0.742506,-3.643514,-0.751248,-2.646927,-2.656967,-1.528956,-9.829182,9.449096,0.327734,-9.143924,7.974102,-0.662504,8.211984,-5.492743,4.644601,-6.267484,6.686586,9.172182,-2.049928,-0.169451,-1.158901,-5.280802,-5.838033,-6.985500,0.565280,-5.447795,0.194992,8.562217,-0.493749,1.424477,-0.613691,7.662641,-3.247624,8.268456,-6.323099,3.198833,0.051635,1.761174,3.135635,9.527451,-1.166731,7.558323,-7.791417,6.298938,-5.121454,-5.222746,-6.048110,-0.229838,-3.231626,-5.443331,0.341300,-1.066252,8.640284,3.086754,7.309647,0.406852,-4.216002,3.371391,-4.087017,6.001447,7.162091,8.906589,1.030877,-7.662817,3.629741,-3.678606,-0.476944,5.829578,-2.630118,-0.881651,8.329566,-9.374910,-2.296586,-1.242185,-4.955125,-4.983745,9.265052,8.176536,0.303302,3.726571,-6.123581,-4.643579,-9.090070,4.924234,-3.749834,-8.746719,5.921323,2.848035,7.193851,-5.309115,6.947068,5.024709,-9.403708,1.358893,5.755780,9.158818,-7.055315,-1.537036,0.323774,5.970369,-1.356561,-5.838148,-9.673608,7.495062,5.362607,4.445261,-6.468132,-1.536167,-6.130044,1.011524,-4.664397,3.945844,-2.253576,0.011084,2.288706,0.782354,-0.124918,-4.737757,8.042203,-4.484199,8.094889,2.155517,5.952099,9.278543,2.982497,4.660168,2.961798,-7.823172,-8.605676,9.232146,-8.181993,2.467144,-2.679435,-6.463482,-9.005669,9.359855,-0.808485,8.838362,-8.881671,2.033704,0.379872,6.344013,-0.625120,-8.463836,8.777824,-9.221227,-5.532314,-8.746657,3.685223,-2.977611,-2.056256,-8.227764,-2.579947,-3.701702,-8.756845,-3.191526,-4.054658,-5.971181], dtype = "float32")#candidate|7412|(2880,)|const|float32
call_7411 = relay.TupleGetItem(func_2463_call(relay.reshape(call_7400.astype('float32'), [10, 10, 2]), relay.reshape(const_7412.astype('float32'), [2880,]), relay.reshape(call_7404.astype('float64'), [20,]), ), 1)
call_7413 = relay.TupleGetItem(func_2467_call(relay.reshape(call_7400.astype('float32'), [10, 10, 2]), relay.reshape(const_7412.astype('float32'), [2880,]), relay.reshape(call_7404.astype('float64'), [20,]), ), 1)
func_6882_call = mod.get_global_var('func_6882')
func_6884_call = mutated_mod.get_global_var('func_6884')
call_7420 = relay.TupleGetItem(func_6882_call(), 2)
call_7421 = relay.TupleGetItem(func_6884_call(), 2)
output = relay.Tuple([call_7377,call_7400,call_7404,call_7411,const_7412,call_7420,])
output2 = relay.Tuple([call_7378,call_7401,call_7405,call_7413,const_7412,call_7421,])
func_7446 = relay.Function([], output)
mod['func_7446'] = func_7446
mod = relay.transform.InferType()(mod)
output = func_7446()
func_7447 = relay.Function([], output)
mutated_mod['func_7447'] = func_7447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3101_call = mod.get_global_var('func_3101')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_7460 = func_3101_call()
call_7461 = func_3101_call()
output = relay.Tuple([call_7460,])
output2 = relay.Tuple([call_7461,])
func_7465 = relay.Function([], output)
mod['func_7465'] = func_7465
mod = relay.transform.InferType()(mod)
output = func_7465()
func_7466 = relay.Function([], output)
mutated_mod['func_7466'] = func_7466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4300_call = mod.get_global_var('func_4300')
func_4302_call = mutated_mod.get_global_var('func_4302')
call_7481 = func_4300_call()
call_7482 = func_4300_call()
func_5210_call = mod.get_global_var('func_5210')
func_5211_call = mutated_mod.get_global_var('func_5211')
call_7499 = func_5210_call()
call_7500 = func_5210_call()
output = relay.Tuple([call_7481,call_7499,])
output2 = relay.Tuple([call_7482,call_7500,])
func_7512 = relay.Function([], output)
mod['func_7512'] = func_7512
mod = relay.transform.InferType()(mod)
mutated_mod['func_7512'] = func_7512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7512_call = mutated_mod.get_global_var('func_7512')
call_7513 = func_7512_call()
output = call_7513
func_7514 = relay.Function([], output)
mutated_mod['func_7514'] = func_7514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2404_call = mutated_mod.get_global_var('func_2404')
call_7534 = relay.TupleGetItem(func_2402_call(), 4)
call_7535 = relay.TupleGetItem(func_2404_call(), 4)
var_7549 = relay.var("var_7549", dtype = "float32", shape = (225, 6))#candidate|7549|(225, 6)|var|float32
bop_7550 = relay.logical_xor(call_7534.astype('int32'), var_7549.astype('int32')) # shape=(225, 6)
bop_7553 = relay.logical_xor(call_7535.astype('int32'), var_7549.astype('int32')) # shape=(225, 6)
output = bop_7550
output2 = bop_7553
func_7556 = relay.Function([var_7549,], output)
mod['func_7556'] = func_7556
mod = relay.transform.InferType()(mod)
mutated_mod['func_7556'] = func_7556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7557 = relay.var("var_7557", dtype = "float32", shape = (225, 6))#candidate|7557|(225, 6)|var|float32
func_7556_call = mutated_mod.get_global_var('func_7556')
call_7558 = func_7556_call(var_7557)
output = call_7558
func_7559 = relay.Function([var_7557], output)
mutated_mod['func_7559'] = func_7559
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7561 = relay.var("var_7561", dtype = "int32", shape = (7, 12, 6))#candidate|7561|(7, 12, 6)|var|int32
var_7562 = relay.var("var_7562", dtype = "int32", shape = (7, 12, 6))#candidate|7562|(7, 12, 6)|var|int32
bop_7563 = relay.bitwise_or(var_7561.astype('int32'), relay.reshape(var_7562.astype('int32'), relay.shape_of(var_7561))) # shape=(7, 12, 6)
var_7567 = relay.var("var_7567", dtype = "int32", shape = (7, 12, 6))#candidate|7567|(7, 12, 6)|var|int32
bop_7568 = relay.multiply(var_7561.astype('int16'), relay.reshape(var_7567.astype('int16'), relay.shape_of(var_7561))) # shape=(7, 12, 6)
func_1529_call = mod.get_global_var('func_1529')
func_1532_call = mutated_mod.get_global_var('func_1532')
const_7578 = relay.const([[-8.210291,2.572209,5.213094],[9.237982,8.555803,3.497239],[-2.305184,4.807715,8.606091],[3.795354,7.964525,-5.926775],[-9.562521,-2.611663,-5.087869],[-2.911320,-9.967738,2.320942],[-0.364817,4.164717,5.672869],[-6.135097,2.158977,6.121786],[-6.908031,0.562217,-9.688016],[0.167011,1.719653,1.699210],[3.546575,5.413294,-8.335589],[-1.036554,5.624641,-3.028639],[-9.901646,6.995004,9.996964],[-6.374826,5.337604,6.527194],[5.494427,-9.600537,-5.993024],[-8.009342,-8.356320,-5.012669],[-6.888289,1.832682,-6.685064],[-2.151822,-9.131843,-1.714611],[-0.916296,1.913722,-9.786353],[4.311935,-4.688095,1.778669],[-8.125564,-0.265078,7.028570],[0.093830,0.785914,7.462781],[-9.865815,-8.968003,5.447151],[-3.220633,0.872137,1.460369],[-8.405499,3.257882,0.008794],[-2.268285,-2.524209,-7.104923],[9.059891,6.191552,-2.075940],[-4.786520,4.113169,2.106578],[-0.186593,-9.914075,-5.173488],[7.682485,9.796961,8.895717],[5.614555,-1.993010,-8.413374],[8.838459,-9.238219,6.513117],[-4.598409,0.448532,-1.580688],[-3.164266,3.062227,0.947715],[1.182455,-2.552321,8.498580],[8.869853,2.632636,5.558479],[-4.584850,2.918672,2.310180],[3.672334,4.565417,5.985663],[8.272364,-2.137786,6.622140],[-5.039119,-9.718506,0.455275],[-4.796201,5.126424,-5.830164],[-5.275759,1.408808,1.365970],[-5.613091,-3.393709,2.568033],[5.202114,-8.036145,1.451032],[6.364595,-3.193640,8.980290],[-5.217813,-2.757844,4.166311],[-8.710475,3.142744,-4.890567],[-2.026204,1.025493,-8.623692],[8.380924,6.543401,7.281689],[3.838580,7.863757,-5.694567],[5.838882,-0.543003,-9.055299],[-1.377310,0.629409,6.155743],[-4.941247,-7.388432,-0.117658],[-9.872394,6.044999,2.419784],[8.127018,9.730541,-8.666832],[3.929697,-7.325816,4.677304],[6.429061,4.830432,6.860837],[-2.475970,2.176191,3.928817],[5.049900,7.033935,-9.236973],[9.576927,2.733915,-6.924432],[9.199208,4.643428,0.313601],[-9.098799,-4.325289,-1.109575],[-6.680616,8.167873,7.273947],[-1.326718,-2.644498,8.346599],[-9.627839,-2.207302,-7.647030],[-6.593431,-9.216388,4.519632],[-1.504162,7.655963,-3.940778],[0.926362,-1.271058,-6.583582],[9.117841,4.516840,-4.061794],[-8.362569,2.354763,-0.531434],[4.435816,4.997297,-9.731523],[-7.840772,0.319950,9.626037],[2.920564,-5.229430,9.171825],[6.723698,8.710330,-2.944979],[-1.580388,4.036856,-8.256554]], dtype = "float32")#candidate|7578|(75, 3)|const|float32
call_7577 = relay.TupleGetItem(func_1529_call(relay.reshape(const_7578.astype('float32'), [5, 15, 3])), 0)
call_7579 = relay.TupleGetItem(func_1532_call(relay.reshape(const_7578.astype('float32'), [5, 15, 3])), 0)
bop_7581 = relay.logical_and(var_7567.astype('bool'), relay.reshape(var_7562.astype('bool'), relay.shape_of(var_7567))) # shape=(7, 12, 6)
output = relay.Tuple([bop_7563,bop_7568,call_7577,const_7578,bop_7581,])
output2 = relay.Tuple([bop_7563,bop_7568,call_7579,const_7578,bop_7581,])
func_7599 = relay.Function([var_7561,var_7562,var_7567,], output)
mod['func_7599'] = func_7599
mod = relay.transform.InferType()(mod)
mutated_mod['func_7599'] = func_7599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7599_call = mutated_mod.get_global_var('func_7599')
var_7601 = relay.var("var_7601", dtype = "int32", shape = (7, 12, 6))#candidate|7601|(7, 12, 6)|var|int32
var_7602 = relay.var("var_7602", dtype = "int32", shape = (7, 12, 6))#candidate|7602|(7, 12, 6)|var|int32
var_7603 = relay.var("var_7603", dtype = "int32", shape = (7, 12, 6))#candidate|7603|(7, 12, 6)|var|int32
call_7600 = func_7599_call(var_7601,var_7602,var_7603,)
output = call_7600
func_7604 = relay.Function([var_7601,var_7602,var_7603,], output)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5069_call = mod.get_global_var('func_5069')
func_5071_call = mutated_mod.get_global_var('func_5071')
call_7629 = relay.TupleGetItem(func_5069_call(), 0)
call_7630 = relay.TupleGetItem(func_5071_call(), 0)
output = call_7629
output2 = call_7630
func_7638 = relay.Function([], output)
mod['func_7638'] = func_7638
mod = relay.transform.InferType()(mod)
mutated_mod['func_7638'] = func_7638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7638_call = mutated_mod.get_global_var('func_7638')
call_7639 = func_7638_call()
output = call_7639
func_7640 = relay.Function([], output)
mutated_mod['func_7640'] = func_7640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7641 = relay.var("var_7641", dtype = "uint64", shape = ())#candidate|7641|()|var|uint64
var_7642 = relay.var("var_7642", dtype = "uint64", shape = (7, 15, 10))#candidate|7642|(7, 15, 10)|var|uint64
bop_7643 = relay.logical_xor(var_7641.astype('uint64'), var_7642.astype('uint64')) # shape=(7, 15, 10)
output = bop_7643
output2 = bop_7643
func_7647 = relay.Function([var_7641,var_7642,], output)
mod['func_7647'] = func_7647
mod = relay.transform.InferType()(mod)
var_7648 = relay.var("var_7648", dtype = "uint64", shape = ())#candidate|7648|()|var|uint64
var_7649 = relay.var("var_7649", dtype = "uint64", shape = (7, 15, 10))#candidate|7649|(7, 15, 10)|var|uint64
output = func_7647(var_7648,var_7649,)
func_7650 = relay.Function([var_7648,var_7649,], output)
mutated_mod['func_7650'] = func_7650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5086_call = mod.get_global_var('func_5086')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_7666 = relay.TupleGetItem(func_5086_call(), 0)
call_7667 = relay.TupleGetItem(func_5087_call(), 0)
uop_7673 = relay.cosh(call_7666.astype('float32')) # shape=(10, 1, 2)
uop_7675 = relay.cosh(call_7667.astype('float32')) # shape=(10, 1, 2)
var_7676 = relay.var("var_7676", dtype = "float64", shape = (10, 7, 2))#candidate|7676|(10, 7, 2)|var|float64
bop_7677 = relay.equal(call_7666.astype('bool'), var_7676.astype('bool')) # shape=(10, 7, 2)
bop_7680 = relay.equal(call_7667.astype('bool'), var_7676.astype('bool')) # shape=(10, 7, 2)
output = relay.Tuple([uop_7673,bop_7677,])
output2 = relay.Tuple([uop_7675,bop_7680,])
func_7681 = relay.Function([var_7676,], output)
mod['func_7681'] = func_7681
mod = relay.transform.InferType()(mod)
mutated_mod['func_7681'] = func_7681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7682 = relay.var("var_7682", dtype = "float64", shape = (10, 7, 2))#candidate|7682|(10, 7, 2)|var|float64
func_7681_call = mutated_mod.get_global_var('func_7681')
call_7683 = func_7681_call(var_7682)
output = call_7683
func_7684 = relay.Function([var_7682], output)
mutated_mod['func_7684'] = func_7684
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7738 = relay.const(4, dtype = "int64")#candidate|7738|()|const|int64
var_7739 = relay.var("var_7739", dtype = "int64", shape = (9, 13, 11))#candidate|7739|(9, 13, 11)|var|int64
bop_7740 = relay.multiply(const_7738.astype('int64'), var_7739.astype('int64')) # shape=(9, 13, 11)
output = bop_7740
output2 = bop_7740
func_7746 = relay.Function([var_7739,], output)
mod['func_7746'] = func_7746
mod = relay.transform.InferType()(mod)
var_7747 = relay.var("var_7747", dtype = "int64", shape = (9, 13, 11))#candidate|7747|(9, 13, 11)|var|int64
output = func_7746(var_7747)
func_7748 = relay.Function([var_7747], output)
mutated_mod['func_7748'] = func_7748
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7753 = relay.var("var_7753", dtype = "float64", shape = (4, 3, 6))#candidate|7753|(4, 3, 6)|var|float64
uop_7754 = relay.log10(var_7753.astype('float64')) # shape=(4, 3, 6)
bop_7761 = relay.right_shift(var_7753.astype('int32'), relay.reshape(uop_7754.astype('int32'), relay.shape_of(var_7753))) # shape=(4, 3, 6)
func_3400_call = mod.get_global_var('func_3400')
func_3402_call = mutated_mod.get_global_var('func_3402')
call_7769 = func_3400_call()
call_7770 = func_3400_call()
func_1366_call = mod.get_global_var('func_1366')
func_1369_call = mutated_mod.get_global_var('func_1369')
var_7774 = relay.var("var_7774", dtype = "float64", shape = (720,))#candidate|7774|(720,)|var|float64
call_7773 = relay.TupleGetItem(func_1366_call(relay.reshape(var_7774.astype('float64'), [3, 15, 16])), 3)
call_7775 = relay.TupleGetItem(func_1369_call(relay.reshape(var_7774.astype('float64'), [3, 15, 16])), 3)
func_2142_call = mod.get_global_var('func_2142')
func_2144_call = mutated_mod.get_global_var('func_2144')
call_7780 = relay.TupleGetItem(func_2142_call(relay.reshape(call_7769.astype('float32'), [10, 10, 2])), 1)
call_7781 = relay.TupleGetItem(func_2144_call(relay.reshape(call_7769.astype('float32'), [10, 10, 2])), 1)
output = relay.Tuple([bop_7761,call_7769,call_7773,var_7774,call_7780,])
output2 = relay.Tuple([bop_7761,call_7770,call_7775,var_7774,call_7781,])
func_7797 = relay.Function([var_7753,var_7774,], output)
mod['func_7797'] = func_7797
mod = relay.transform.InferType()(mod)
mutated_mod['func_7797'] = func_7797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7797_call = mutated_mod.get_global_var('func_7797')
var_7799 = relay.var("var_7799", dtype = "float64", shape = (4, 3, 6))#candidate|7799|(4, 3, 6)|var|float64
var_7800 = relay.var("var_7800", dtype = "float64", shape = (720,))#candidate|7800|(720,)|var|float64
call_7798 = func_7797_call(var_7799,var_7800,)
output = call_7798
func_7801 = relay.Function([var_7799,var_7800,], output)
mutated_mod['func_7801'] = func_7801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5276_call = mod.get_global_var('func_5276')
func_5277_call = mutated_mod.get_global_var('func_5277')
call_7836 = relay.TupleGetItem(func_5276_call(), 0)
call_7837 = relay.TupleGetItem(func_5277_call(), 0)
output = relay.Tuple([call_7836,])
output2 = relay.Tuple([call_7837,])
func_7859 = relay.Function([], output)
mod['func_7859'] = func_7859
mod = relay.transform.InferType()(mod)
output = func_7859()
func_7860 = relay.Function([], output)
mutated_mod['func_7860'] = func_7860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5210_call = mod.get_global_var('func_5210')
func_5211_call = mutated_mod.get_global_var('func_5211')
call_7863 = func_5210_call()
call_7864 = func_5210_call()
output = relay.Tuple([call_7863,])
output2 = relay.Tuple([call_7864,])
func_7873 = relay.Function([], output)
mod['func_7873'] = func_7873
mod = relay.transform.InferType()(mod)
mutated_mod['func_7873'] = func_7873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7873_call = mutated_mod.get_global_var('func_7873')
call_7874 = func_7873_call()
output = call_7874
func_7875 = relay.Function([], output)
mutated_mod['func_7875'] = func_7875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7096_call = mod.get_global_var('func_7096')
func_7097_call = mutated_mod.get_global_var('func_7097')
call_7876 = relay.TupleGetItem(func_7096_call(), 0)
call_7877 = relay.TupleGetItem(func_7097_call(), 0)
output = call_7876
output2 = call_7877
func_7894 = relay.Function([], output)
mod['func_7894'] = func_7894
mod = relay.transform.InferType()(mod)
mutated_mod['func_7894'] = func_7894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7894_call = mutated_mod.get_global_var('func_7894')
call_7895 = func_7894_call()
output = call_7895
func_7896 = relay.Function([], output)
mutated_mod['func_7896'] = func_7896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1439_call = mod.get_global_var('func_1439')
func_1440_call = mutated_mod.get_global_var('func_1440')
call_7932 = func_1439_call()
call_7933 = func_1439_call()
func_2294_call = mod.get_global_var('func_2294')
func_2296_call = mutated_mod.get_global_var('func_2296')
var_7950 = relay.var("var_7950", dtype = "float32", shape = (2880,))#candidate|7950|(2880,)|var|float32
call_7949 = relay.TupleGetItem(func_2294_call(relay.reshape(var_7950.astype('float32'), [16, 15, 12])), 4)
call_7951 = relay.TupleGetItem(func_2296_call(relay.reshape(var_7950.astype('float32'), [16, 15, 12])), 4)
func_4263_call = mod.get_global_var('func_4263')
func_4264_call = mutated_mod.get_global_var('func_4264')
call_7954 = func_4263_call()
call_7955 = func_4263_call()
func_474_call = mod.get_global_var('func_474')
func_476_call = mutated_mod.get_global_var('func_476')
const_7964 = relay.const([5,8,5,4,5,7,-5,-9,-2,-10,-1,-9,-1,7,1,-1,-7,4,6,1,-3,-9,7,5,-6,-4,-5,10,-5,-2,-5,5,-1,4,-4,9,5,-6,-6,6,7,-1,-4,-10,7,7,2,4,10,-1,4,4,9,-4,2,-7,9,-3,8,-1,-5,7,-2,-3,8,9,-5,1,-4,9,4,-4,5,-3,-1,9,7,-3,8,1,1,10,-2,10,-6,1,6,-3,5,3,2,-1,-10,8,-2,4,9,-9,-4,9,9,-10,-5,5,10,-5,-2,1,-1,-9,-8,-6,4,-9,8,10,8,-4,4,-3,9,-7,4,-2,9,-8,4,-5,3,9,-2,1,-9,-2,-4,7,3,-6,-6,-10,2,3,5,-6,-3,-2,-6,-6,-5,9,-3,5,-2,1,-1,-4,-2,-1,-6,7,-4,8,-9,-4,-3,6,-9,2,-3,-1,7,-1,4,-5,-9,-2,9,-2,4,-5,-8,5,-3,1,3,2,1,6,-5,8,5,-10,1,5,9,4,-10,-7,7,10,-3,-7,-8,-2,8,-9,-1,5,3,9,9,-1,2,1,7,-9,-6,5,-1,-6,-6,-10,-6,-10,7,10,5,-5,9,-8,9,-7,4,-8,-8,4,3,-2,10,-9,3,3,3,7,-3,-8,-2,9,8,1,-2,-9,-8,4,-5,5,4,-8,-5,7,-1,2,2,7,9,-6,-2,7,-8,-10,-6,2,4,-5,8,8,-10,1,2,-2,8,5,2,2,5,-4,-8,10,-10,-10,10,-8,-8,2,6,4,-1,6,1,5,1,-8,10,2,5,-10,9,5,4,-1,9,-6,2,-6,-9,10,2,10,6,-4,3,-7,-10,4,-10,-8,-8,-1,-8,5,10,9,3,-6,1,-9,-3,-9,-9,-1,-5,7,-3,6,-7,-9,6,9,-7,-8,4,-1,6,-4,-10,-3,3,-10,2,8,-7,-4,-4,4,-5,-10,-2,10,2,2,-8,-8,-8,-7,-4,-8,3,6,3,1,-2,1,-1,-1,-4,6,9,10,2,-6,2,7], dtype = "int8")#candidate|7964|(392,)|const|int8
call_7963 = func_474_call(relay.reshape(const_7964.astype('int8'), [7, 8, 7]))
call_7965 = func_474_call(relay.reshape(const_7964.astype('int8'), [7, 8, 7]))
func_4063_call = mod.get_global_var('func_4063')
func_4065_call = mutated_mod.get_global_var('func_4065')
const_7972 = relay.const([-9.329357,8.643697,1.011666,-3.278729,-7.057964,6.240829,-6.781942,-9.946980,-3.954956,6.974020,-2.036988,-0.897928,-9.735643,1.409629,-4.724912,-9.277979,4.080555,-2.341569,-8.079462,-3.005710], dtype = "float64")#candidate|7972|(20,)|const|float64
call_7971 = relay.TupleGetItem(func_4063_call(relay.reshape(const_7972.astype('float64'), [20,])), 0)
call_7973 = relay.TupleGetItem(func_4065_call(relay.reshape(const_7972.astype('float64'), [20,])), 0)
output = relay.Tuple([call_7932,call_7949,var_7950,call_7954,call_7963,const_7964,call_7971,const_7972,])
output2 = relay.Tuple([call_7933,call_7951,var_7950,call_7955,call_7965,const_7964,call_7973,const_7972,])
func_7981 = relay.Function([var_7950,], output)
mod['func_7981'] = func_7981
mod = relay.transform.InferType()(mod)
mutated_mod['func_7981'] = func_7981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7982 = relay.var("var_7982", dtype = "float32", shape = (2880,))#candidate|7982|(2880,)|var|float32
func_7981_call = mutated_mod.get_global_var('func_7981')
call_7983 = func_7981_call(var_7982)
output = call_7983
func_7984 = relay.Function([var_7982], output)
mutated_mod['func_7984'] = func_7984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5086_call = mod.get_global_var('func_5086')
func_5087_call = mutated_mod.get_global_var('func_5087')
call_8012 = relay.TupleGetItem(func_5086_call(), 0)
call_8013 = relay.TupleGetItem(func_5087_call(), 0)
output = relay.Tuple([call_8012,])
output2 = relay.Tuple([call_8013,])
func_8016 = relay.Function([], output)
mod['func_8016'] = func_8016
mod = relay.transform.InferType()(mod)
output = func_8016()
func_8017 = relay.Function([], output)
mutated_mod['func_8017'] = func_8017
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8048 = relay.var("var_8048", dtype = "float64", shape = (3, 15))#candidate|8048|(3, 15)|var|float64
uop_8049 = relay.sinh(var_8048.astype('float64')) # shape=(3, 15)
func_7859_call = mod.get_global_var('func_7859')
func_7860_call = mutated_mod.get_global_var('func_7860')
call_8053 = relay.TupleGetItem(func_7859_call(), 0)
call_8054 = relay.TupleGetItem(func_7860_call(), 0)
func_7981_call = mod.get_global_var('func_7981')
func_7984_call = mutated_mod.get_global_var('func_7984')
var_8063 = relay.var("var_8063", dtype = "float32", shape = (2880,))#candidate|8063|(2880,)|var|float32
call_8062 = relay.TupleGetItem(func_7981_call(relay.reshape(var_8063.astype('float32'), [2880,])), 0)
call_8064 = relay.TupleGetItem(func_7984_call(relay.reshape(var_8063.astype('float32'), [2880,])), 0)
output = relay.Tuple([uop_8049,call_8053,call_8062,var_8063,])
output2 = relay.Tuple([uop_8049,call_8054,call_8064,var_8063,])
func_8072 = relay.Function([var_8048,var_8063,], output)
mod['func_8072'] = func_8072
mod = relay.transform.InferType()(mod)
var_8073 = relay.var("var_8073", dtype = "float64", shape = (3, 15))#candidate|8073|(3, 15)|var|float64
var_8074 = relay.var("var_8074", dtype = "float32", shape = (2880,))#candidate|8074|(2880,)|var|float32
output = func_8072(var_8073,var_8074,)
func_8075 = relay.Function([var_8073,var_8074,], output)
mutated_mod['func_8075'] = func_8075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2590_call = mod.get_global_var('func_2590')
func_2592_call = mutated_mod.get_global_var('func_2592')
call_8100 = relay.TupleGetItem(func_2590_call(), 0)
call_8101 = relay.TupleGetItem(func_2592_call(), 0)
func_7981_call = mod.get_global_var('func_7981')
func_7984_call = mutated_mod.get_global_var('func_7984')
const_8104 = relay.const([[-5.103729,0.772438,4.007198,4.157756,5.626619,1.746986,-9.439739,-4.166384,0.850282,-4.001634,1.684976,2.391055,-0.414448,-4.219095,7.362072,-9.113567,1.865580,-0.178353,-1.564689,5.400152,-9.783976,-0.125810,3.501170,-4.140806,-5.635589,-9.860623,3.633287,-6.185719,-3.270063,-4.241945,0.656649,-9.130518,-6.460943,9.647243,-9.841473,-3.961628,-3.733966,7.570231,4.095353,-3.012607,-3.539719,0.277679,-9.589208,9.948757,-3.067501,-8.912393,-4.397447,-3.857643,3.885196,-8.788466,0.071122,-4.658110,3.337449,1.373402,4.147834,8.731960,-8.682159,-6.741706,-3.329474,6.564526],[0.136405,5.989847,-9.884749,9.986224,2.330847,3.898486,-0.077635,-0.744028,4.283385,1.343753,-1.689182,-0.486388,6.277665,1.492206,3.084611,4.388388,4.369198,-1.708880,-1.570801,5.658465,3.356974,-8.021580,2.739936,-3.576333,-3.035520,4.708867,-8.334433,5.298655,-1.444725,7.251032,-9.339615,9.953443,8.311103,6.771272,4.153843,-3.394540,-1.370611,-4.822689,4.694632,-1.064198,-2.856451,-2.223386,-2.445891,0.984679,5.619455,-6.372626,1.335806,7.700919,7.972320,-9.844054,4.779197,-4.901106,-5.569863,1.723968,5.357461,0.615707,-8.403967,-6.133134,-0.313166,8.396619],[-0.873657,8.586885,9.216203,5.328033,3.048945,2.801542,-7.728118,-9.169264,1.191722,-5.998308,-6.496985,-6.534352,-2.281794,6.381950,-5.669116,-3.888065,-7.015790,-1.634181,-4.814264,-5.019458,-2.507282,-2.193464,6.547967,2.533067,3.574960,6.924171,8.779178,-6.242795,-3.144318,-2.978831,-1.885804,-2.228529,-5.168517,9.376495,-6.190745,2.150932,2.149085,9.551414,-5.639535,6.878308,-9.124445,3.368219,0.635195,2.026818,5.175553,-2.212283,-5.155620,-5.434657,-7.845164,7.791382,-1.388437,2.180489,3.190406,-8.033499,4.567468,6.700683,9.279726,0.161368,-2.241550,-1.423777],[3.906023,7.646960,0.132732,-8.398757,7.707352,-3.859316,-4.471094,-2.717735,-4.890534,-3.763385,-1.146145,-3.580101,-9.023223,-6.321967,-8.963257,3.006251,-3.595843,-5.901241,-6.500243,4.299610,-3.458116,6.116352,2.287684,-2.900079,2.624430,0.247488,-5.384566,5.677697,8.342203,3.280353,-0.697426,5.901741,-2.351645,4.361304,1.408024,-6.918055,-9.056581,-6.215398,1.864770,-6.128218,9.189223,9.565189,6.099302,0.535022,-5.923175,-8.187553,4.607200,6.528373,9.571590,-5.400236,9.863172,1.255060,1.965244,3.343888,-4.624357,5.511688,3.110893,-7.038951,0.728860,-2.204265],[-6.807810,-2.575177,-2.429397,5.522255,-1.742319,-2.415498,2.097506,-5.699800,-5.616537,4.437125,3.085635,-5.490642,2.348734,6.020375,-9.573224,4.427638,-4.419571,-3.273137,2.208587,3.825930,-6.352603,-8.064114,1.586983,-2.295014,-6.533940,-0.075240,-8.444981,4.025594,3.816719,-5.253432,-6.530935,7.098019,8.634731,4.334088,9.189442,9.062957,1.534784,2.571617,-2.282380,-5.980286,-1.711932,-8.413158,6.261188,-6.762990,-4.065608,8.705072,-6.767595,3.270616,-4.239691,5.775129,3.437517,6.252200,-5.906572,8.071561,-6.466822,1.642453,0.511165,5.238331,0.557022,4.407989],[-0.472653,-4.748361,1.452950,6.263503,2.134353,-9.370830,1.531373,3.892163,-1.018205,-1.873322,-3.781807,7.983563,1.609568,-0.371769,5.563224,-9.035491,-8.226580,-8.264678,-3.972804,-8.095268,-1.774275,4.812647,-2.559262,9.633652,4.619105,-3.474628,-2.029648,0.880571,-0.440470,-9.512290,-2.310212,-0.293651,-3.784156,-0.465953,-0.752490,-8.791824,4.136794,-1.898961,-9.702186,1.906993,7.303683,8.003436,1.304413,8.968455,-2.861313,6.158690,-3.684250,-4.598750,1.035464,8.713452,6.212812,-4.345800,1.694456,-1.333513,5.069279,-2.430889,1.964925,-1.067466,-3.805159,8.749688],[6.613339,5.738341,-0.888235,-6.879353,3.382940,2.892054,6.103315,2.126304,-0.131214,-8.291844,3.926025,-3.527150,-6.714993,-5.447819,-2.550962,-3.521493,-4.520110,1.870748,0.507665,-6.821120,2.019326,9.761458,-0.262230,-9.054505,-2.407021,-3.725460,5.921619,7.569631,1.404228,-1.931885,5.813184,8.783927,4.393984,-8.960337,0.177124,1.564869,-9.072215,1.972920,3.868543,8.082306,2.056703,-8.670614,-8.985363,-7.063931,6.541170,7.975133,1.224344,-6.822915,4.873383,8.330133,-1.779287,3.762500,3.755795,4.657027,-9.767938,8.972502,-5.714390,-2.987603,8.504593,-3.315224],[-3.628747,7.175709,-5.532228,-8.695685,-5.275804,-2.114209,-9.012902,9.058643,2.516261,-3.906459,1.028133,2.946662,3.781060,-6.417040,-1.003301,2.061895,-2.273638,7.948897,5.942461,-0.385608,5.677556,-4.260453,-2.668857,-4.457544,-0.468031,-4.799348,-2.061740,5.752194,5.374808,-2.596695,-5.756733,-6.934019,-0.166908,7.427336,4.872620,5.090271,8.832087,-6.193002,3.821953,1.737788,-2.317513,2.611040,9.386909,-8.175255,-6.910344,-4.093108,8.906916,9.238686,-3.024752,8.474780,-1.496585,0.714816,-1.327479,4.395083,-8.843285,5.144641,-4.245364,7.193408,5.541317,6.213009],[-8.802339,-7.097362,-4.241147,4.092268,-2.397619,0.460558,7.748244,-1.899501,-0.690855,2.467088,-5.643844,7.055319,1.163254,-3.687621,9.207934,-6.976990,-1.033647,0.641061,-2.078772,2.063122,1.410538,9.794969,3.113713,-4.090715,7.964517,-0.935974,-8.499902,4.079578,-8.917731,-0.897795,7.737172,8.141822,2.611940,-8.561189,4.162653,-6.765304,-5.184478,2.664060,-2.464984,-3.300591,9.053006,3.336649,-6.312698,3.595660,8.327163,-8.386549,-5.052432,-5.467181,-6.128999,0.106697,-1.743085,-0.894297,0.517333,1.970935,3.838224,-8.665984,-7.369813,-3.462643,-8.995582,-6.039124],[7.856298,-5.585378,-9.154034,5.016991,8.745571,4.707461,5.086917,0.905447,2.121366,-5.883140,-3.458686,-8.479196,-8.708766,3.353815,-8.291505,-8.028266,3.031047,-7.656117,0.911255,-3.510877,-9.150957,8.896143,-2.586860,7.727409,6.028125,-9.799957,-5.562074,-8.991486,-4.715336,2.234445,6.911630,-6.824625,-8.093860,7.575942,7.862314,-5.999088,6.357517,6.280205,-8.217601,6.086989,-3.491567,0.270754,-9.064143,3.458656,-6.340611,-9.935663,7.149379,-8.380608,8.852682,6.956360,9.249355,-6.999418,9.343800,-4.459064,-6.982532,8.180396,-6.767788,2.792735,6.830937,9.912756],[2.737704,1.825057,-8.520326,-4.909031,8.517799,-2.876953,-7.632453,4.691884,-9.723461,7.088896,-6.495277,3.749491,-7.873105,9.343526,-3.903845,3.675922,-0.332435,-1.041775,-3.132918,-7.893443,-9.735248,-3.864544,-8.535762,9.572318,-8.622371,2.607542,5.393784,1.651466,-8.395645,0.126380,8.470306,-4.433970,-5.480104,-8.854855,-6.535176,-1.110952,-0.893632,0.273626,8.849322,0.420201,2.486102,-5.582468,-7.889388,-9.032787,-0.710127,3.493214,-2.964085,-9.096334,-0.512152,0.589716,6.346256,6.674597,3.280143,-7.650034,9.376563,-3.407009,7.489283,-3.882792,-3.055766,-9.578700],[-0.728999,-4.200872,4.561492,2.317588,5.113424,-2.445830,7.207710,-1.527849,-9.713882,2.639482,1.343544,1.917056,-8.414867,-1.852710,-0.880107,0.465876,-7.486134,-6.264023,-5.176320,1.776032,-9.569665,5.448714,5.335323,-7.985405,-9.338430,-3.510594,6.380282,-5.543275,1.846413,-8.218994,0.689553,-0.169789,0.259044,-2.060116,9.581289,-1.473065,7.575078,1.931260,0.066397,9.431564,5.764422,4.588115,4.782466,-6.248934,-0.782618,-3.161255,-0.609567,8.310808,6.130498,-7.610012,5.246804,9.349017,-1.550538,-1.145999,-8.869774,2.379614,0.979795,2.474270,7.859932,0.241471],[-3.187000,3.920969,-7.386646,4.401344,-8.621834,-9.969044,-6.289721,7.756813,-0.334503,-4.459366,3.479995,-5.472354,9.620240,9.694820,5.862192,-3.974092,-9.794977,4.418301,5.658482,2.258426,-6.649501,6.139331,2.757790,9.489958,-0.223227,-1.477101,8.926495,-4.170282,-6.049954,5.495686,-0.913263,-7.817149,-2.159987,-9.705803,-7.839415,1.655916,4.671702,9.114141,7.360229,9.264001,-1.374013,4.534648,-8.313823,-4.219862,7.901766,6.013429,-0.343137,8.863955,5.420043,-1.697216,9.422007,-0.446366,-2.843222,0.817679,-8.869454,-1.007247,-1.625702,-3.542161,7.669408,-6.919318],[8.913532,5.756307,4.865203,-4.729447,-1.768519,-9.538685,-5.010195,-0.778647,-8.111354,6.245730,-1.952259,3.287344,1.999754,-9.732409,6.536951,-8.656505,-6.084757,-4.485818,-4.452985,-0.538089,2.984232,-1.359309,1.756606,-2.233628,-7.579725,-7.117737,0.621093,2.117912,1.319774,-9.052856,-9.180450,2.951111,-2.915683,-6.297633,-6.207315,9.764210,7.557562,-1.373583,-1.167280,-6.515504,-7.202833,-1.645031,6.725048,-6.556636,9.434251,1.674642,0.185825,-7.400877,-0.832421,-1.057643,1.836747,-0.483113,3.319476,8.966069,0.100258,-1.511410,-8.746780,-7.103074,8.726734,-2.338893],[1.052763,-8.677149,6.698312,-8.059260,-6.034794,-8.638408,-2.827675,-9.577659,2.877031,3.111676,-6.075560,-1.690433,-7.307604,-5.439977,-1.600257,-2.690590,-2.261473,-5.024298,6.360762,1.000847,-7.567911,3.092973,-7.007214,-3.311058,2.631325,-3.734891,-7.085940,-8.770650,0.645431,-1.848794,-9.360180,6.883903,8.183191,-0.092645,-9.247236,-4.492696,0.234166,8.017140,-3.088946,-6.946126,-6.230591,8.891333,3.114928,5.269970,-7.500797,-2.625851,0.840041,4.916741,-0.064382,1.535807,2.184762,1.646261,-7.965543,-7.357200,-9.727175,-9.895366,3.927566,7.949566,-5.178459,-8.282093],[-4.254863,0.987667,-9.424359,6.747596,-8.365016,-9.995061,-1.098877,-5.282436,-4.772891,6.767172,1.046217,6.171980,6.264354,-4.329067,-4.107421,-8.261222,6.928707,-8.126618,-0.029211,-6.823654,-1.796244,-1.158324,-1.199841,6.126358,7.239741,-3.420873,3.677542,-8.629200,-6.451391,-7.287469,2.743835,-8.573300,-0.373667,-9.807527,-8.003914,9.962542,6.005611,8.280332,-5.116541,7.669050,-4.549637,3.956255,0.077428,-9.558044,-3.380849,-6.860045,-8.635368,-8.751056,5.864686,4.673339,-6.011204,6.582440,8.892905,8.971410,2.251735,7.851998,-0.397242,9.104317,-6.304956,-8.695623],[-8.951791,-7.557515,1.148527,9.945742,-7.019430,-3.887471,9.952423,-8.490257,-9.948111,8.343139,-6.226986,3.472792,7.549480,4.833882,3.355026,-6.434085,-5.680259,-2.571295,8.380435,5.010910,-3.714166,-5.305231,1.712676,-8.229158,3.436945,3.723911,5.260678,-1.588053,-7.216450,-8.804738,1.789691,6.772459,-9.193143,0.420729,-5.956631,1.604145,-6.360573,-5.819369,-3.561163,-7.671997,-7.507462,-8.393369,-2.584666,-3.567806,-4.931379,-5.732925,9.615388,2.278461,7.314648,-7.492254,6.016091,8.608949,3.171974,5.952566,-9.560047,9.933813,-2.361389,-5.944549,8.315335,3.907393],[-5.325010,8.556742,1.912880,8.105108,-5.197769,-3.246608,9.647130,4.886788,-4.466933,-0.118456,-3.004559,2.427808,3.236715,-9.954440,1.608537,-7.747854,8.008844,7.777987,1.682147,-5.043541,-6.230059,5.931973,-6.102331,9.807061,-6.029227,7.917691,3.892329,2.650495,8.766763,6.460120,3.797231,-9.348041,-1.240212,2.038785,-7.297870,6.220133,7.305876,-1.344603,2.268941,-9.370687,7.504954,8.311509,-0.513382,-7.578297,-3.279095,-6.954632,6.981659,-6.382436,2.927455,0.456520,8.275989,-2.025788,-3.271793,-3.843342,-8.531837,2.871962,9.281850,5.888404,3.246750,2.725264],[6.289952,3.189253,-8.333020,-2.415325,0.816517,0.179410,-3.526844,6.228752,-8.589126,3.895889,-8.523993,-9.115784,7.281902,-7.818636,5.414717,-8.652090,3.865975,-3.936384,8.986963,3.191903,-5.191986,-4.638139,2.299414,3.540896,7.293452,-9.829751,2.518667,2.424352,-1.198891,5.539371,4.969071,6.903472,9.261659,-2.102640,-3.683080,-3.190969,-1.422463,-3.767371,-4.733059,7.108620,-7.344984,-6.404953,6.375612,-9.388277,6.691294,3.223919,8.269656,6.927708,-6.285084,2.857748,-3.972530,-8.200776,-6.227469,-0.415350,-1.916326,0.670098,6.340691,8.858260,8.915453,1.455797],[4.650019,-3.486378,6.174015,-4.130442,9.201649,-7.617245,7.184967,5.954529,8.319270,-1.728502,9.534401,-9.610352,3.159753,5.864781,9.036815,9.675899,-5.277347,4.196741,-8.655773,9.900505,-0.741897,7.058988,-1.548997,4.695810,-6.303282,-1.011193,2.184734,-8.144357,-0.678392,-4.646555,-0.842714,-6.331566,4.956151,-3.539447,7.590955,3.974974,-9.851381,4.095102,9.976632,-9.761342,5.423401,-0.485427,-2.381496,8.314436,-0.376380,-5.803696,-8.947145,1.446759,4.213006,0.127059,-6.040689,-1.151411,1.606260,8.467120,-8.062343,-1.138053,-8.581621,2.238822,2.760679,4.216070],[-8.319379,5.735589,1.737790,-2.740387,-3.850731,9.569028,-8.190940,2.704670,-3.533603,1.568486,6.004632,-3.920341,-9.047504,-0.111759,-2.462558,2.993794,4.290529,1.218291,-5.379278,7.609491,0.575504,9.544492,-2.706539,6.306967,6.926792,-2.400077,-7.441006,4.466683,-6.545043,4.705751,1.884235,7.082078,2.537211,9.673939,-8.514180,-6.833395,-2.558352,0.502397,2.975769,6.837483,9.787168,8.893927,-1.419001,-4.825765,-2.694537,1.788012,7.479299,-5.417262,-6.659214,-8.578557,3.862002,-9.368618,-3.910379,-6.614792,2.878593,-9.008793,3.633956,-8.548873,-4.518415,-5.351056],[-2.950920,3.068740,-7.283883,-8.701330,1.665979,5.307195,-5.181096,-1.929778,-7.220493,-8.319981,-0.906647,-8.065383,-3.892745,6.282046,-0.095109,3.736857,-3.639343,-2.364157,-1.724338,8.627138,4.010012,-5.885147,-7.806582,-8.206441,-5.373384,-0.860031,7.702335,-1.652385,-7.637528,7.766459,-5.509817,9.696489,8.421478,8.470432,3.699206,3.235817,-5.660938,-9.405923,3.395259,9.164326,2.882855,-5.855717,-6.814242,-7.562016,3.571146,8.334560,-3.352119,-0.506306,-4.322882,2.047613,-8.115097,-3.352103,9.322876,3.040934,6.217816,-5.033699,3.298925,-2.724633,7.704963,-2.413976],[-4.577018,-4.222041,-6.483523,-0.638482,3.131047,-5.250400,-5.109728,-5.019058,0.239207,-5.792289,-5.215736,0.811119,-6.497953,0.156711,-0.215183,-7.533041,-4.781779,9.318313,1.630984,5.580176,-7.073389,-7.873811,7.353654,-3.560345,-4.678620,5.559557,8.931795,-5.667809,-5.561183,4.360820,5.120727,4.009445,2.362713,5.087472,-5.999671,9.602152,-9.236876,-4.568786,-4.257061,7.439753,7.260235,3.886052,4.319188,-5.958803,3.829849,6.399014,1.960248,-2.705815,1.557750,9.128091,0.407615,-6.332852,-0.299290,6.894827,0.491200,-1.087637,7.721008,9.108887,1.127926,0.305657],[-5.911663,-8.492787,1.094527,-8.045518,-7.121646,7.669249,-3.312804,7.169070,-5.244326,9.025381,3.476566,-0.756115,1.400297,-0.585731,-0.014450,8.773993,-3.046211,-2.741217,8.602161,-5.075261,4.882773,8.678502,-0.719882,-9.366869,9.426967,-9.358398,8.900335,4.330296,7.164419,-7.934334,4.426757,-2.950160,2.610488,-8.571741,7.315087,-5.682052,-4.513646,-1.117616,-1.906631,4.408991,-5.815699,5.556426,-0.570302,-5.267235,-6.905163,1.873983,-9.900914,1.232311,6.090425,-4.042162,-9.559372,7.336810,-1.228174,3.136582,-0.233396,-1.684248,1.856603,0.955391,8.043068,8.094377],[-5.624706,6.595184,-1.742264,-3.970637,-3.993641,-0.363947,3.202747,3.433005,9.581923,-0.103899,2.667384,-0.962632,-3.973973,6.246220,0.798283,0.032673,1.871621,-9.443394,5.053430,1.343948,-7.960969,5.965210,3.670898,6.018225,4.133841,6.782693,1.552016,9.440923,7.970192,3.083554,3.970678,-3.904404,3.037339,-5.922335,8.358579,0.394643,7.819214,4.024302,0.009292,3.945952,-3.409782,-9.103817,-5.677217,-4.670378,-3.975224,-6.112365,-2.057658,-9.759753,-4.130822,2.481169,2.628823,5.281613,1.961436,1.283997,6.863541,4.618426,8.121970,9.515583,-6.801605,4.825487],[3.615749,-4.789911,-2.778264,-1.747798,-0.452315,-6.623698,-0.725508,-2.453703,-9.423250,-3.929626,5.514297,-6.610663,6.359359,-0.725650,1.970202,-2.538334,-0.176809,-8.307258,-6.970218,9.664894,-1.989115,-6.230275,3.389190,-2.482307,-2.487077,3.859172,0.346366,0.717913,-3.024859,-8.144752,8.736672,-3.734054,0.995919,6.381208,5.891973,-1.163125,-3.947613,-6.055046,-7.926310,-8.323842,-0.936047,-8.573879,9.974375,-2.168385,8.141247,5.604625,-4.002921,-3.849378,-8.565656,7.296185,-5.881415,-8.687069,-3.921449,-4.852089,5.275275,0.393523,2.463459,5.411744,5.233892,-3.751930],[-4.462058,-3.548820,9.400027,5.131990,-0.394107,-6.941567,-6.654496,0.301333,7.311021,1.806761,-7.266837,-4.394420,-7.602415,-0.302377,-1.562228,3.423405,-8.124420,6.471374,-6.151820,-6.089853,8.455597,-2.957272,7.093483,-3.589755,3.352808,3.687485,-6.610816,9.557412,-5.364173,7.579843,-5.492995,6.652347,-5.782868,1.964852,1.636981,6.788453,-0.434688,1.872312,5.956288,-2.274419,4.078946,4.033841,-1.327449,4.956502,-9.643618,5.723102,5.417779,-1.125313,2.311490,-9.106250,6.734194,7.293544,1.495415,3.149501,-2.420307,-7.039298,1.059108,1.770635,-7.175208,-8.932348],[9.291602,-8.866139,2.745648,-7.381235,-8.794089,4.704600,-5.119109,0.746141,8.467898,2.171841,-6.092797,-3.583977,3.116061,4.973632,-7.510407,-9.099974,4.002681,-3.736402,5.354079,9.891582,7.930673,3.816430,3.352504,-9.172339,5.389271,-9.403925,0.079071,-9.089582,8.031999,-1.809239,7.216436,9.940967,5.578088,2.688067,5.494373,-7.950208,-0.164419,-3.532920,-8.347677,-7.849449,-5.579797,-7.248148,2.154515,-5.291610,-7.941500,-0.376163,-9.608474,3.459552,3.055922,-6.008822,9.735455,-6.325160,0.707233,-9.357282,1.034350,7.284560,2.034540,1.041045,-7.374264,3.926067],[-1.879306,7.960066,-3.564025,0.463948,2.940737,-6.390083,-3.466326,-5.939658,6.260863,-6.162186,-7.415378,7.855966,7.321521,-7.016024,-6.627758,-3.542379,-5.494765,0.725473,-7.929121,-7.360116,1.280219,3.980438,9.708558,7.833063,-9.263843,5.410979,9.048149,-7.793853,9.667835,5.210491,6.496876,5.120307,5.562116,-1.785033,7.363473,0.708746,5.808187,-6.726538,6.177828,7.791047,8.333334,-3.588682,4.207081,6.115578,9.449536,4.334150,6.684122,-9.224098,7.515574,-4.589264,-0.032840,9.892528,-8.013808,-1.172378,9.090945,9.535549,3.794207,-5.156211,1.553285,1.403028],[-6.592672,3.155808,6.586707,-3.033257,-0.187916,7.274315,-1.936129,-4.714377,7.916638,-4.435266,-8.097700,2.310313,7.784866,3.592978,-6.358197,-6.124774,0.525175,-2.248567,3.595250,7.594472,7.302839,-8.046305,-0.376719,3.527094,-1.595017,-8.122404,2.006586,-8.661280,4.979076,1.374030,-0.082412,-1.113652,0.921337,3.200007,6.583601,-4.375538,6.946767,1.141357,0.358542,6.472907,-2.471983,2.804894,-6.367271,6.546768,7.907825,5.402457,-9.808227,1.361075,-7.686249,-0.328227,3.873615,-7.052938,-5.433395,-3.951081,-2.731755,3.090618,-6.750009,3.331899,-6.680318,-6.743098],[3.083145,4.617400,-7.309891,-9.852399,2.036294,-1.528747,5.429643,-5.435207,-8.714418,-5.309770,-3.951697,-1.626625,-8.806903,2.685582,-1.536853,-3.252801,5.031053,1.891794,-5.661061,-2.543845,-7.875262,-3.606279,-4.689381,8.022471,-6.780905,4.308851,8.338174,0.373442,9.290775,-3.797438,-6.582440,-9.421904,4.281588,6.279653,6.671689,9.151917,3.829426,2.464185,-1.816396,-8.594140,-4.449557,-0.955697,3.600846,5.789756,-0.829202,-6.077489,-2.970570,0.047822,-5.304983,6.321992,-5.591883,-7.953496,5.631006,0.403213,-5.924118,-6.158218,-0.839021,7.029899,-9.200779,-6.721212],[-9.821691,5.876727,4.976539,-2.859471,-4.016906,4.820788,0.493654,-2.728527,-8.106470,-5.319381,9.155333,7.462768,0.288606,-3.783396,-3.780299,5.836339,7.589777,0.082381,4.980213,2.105231,-8.365417,-9.671781,-4.325287,-6.016794,5.196753,6.196151,9.762570,-9.496712,4.120736,-7.937551,2.695715,3.467136,-2.539084,-2.621231,-0.365046,4.369391,-8.266295,-0.635221,-8.369847,0.369431,-1.608208,8.449955,-0.380073,-5.256428,-6.535712,6.263099,-7.673924,-4.187143,5.332908,-1.238420,-8.449035,-7.980833,-1.871730,9.148227,8.092486,-2.015343,-1.211978,2.968758,5.253033,-2.214857],[-0.717309,3.206840,-7.722140,-1.998850,-6.776441,-5.906745,-2.589136,-8.321631,5.607425,-2.690582,-4.319853,-9.826495,-0.888945,3.408736,-7.360245,7.594797,9.572214,5.271536,-4.347550,-4.061356,6.840003,-7.132582,4.533361,-1.925635,-3.199882,-1.263209,0.606142,4.363007,-4.728613,3.172410,0.833821,-4.901671,3.488767,-5.852377,5.088984,3.794267,5.312722,-6.650354,-9.299261,-8.399969,6.830949,6.645297,3.893407,-3.814260,-0.486882,-7.750404,-0.422006,-8.784813,6.865970,-5.274369,1.217722,0.276128,2.817937,-3.654828,-7.182453,-6.956199,7.490723,-4.814523,3.824419,-8.715276],[-8.300285,7.524890,0.314783,-6.467857,-0.717400,0.371389,-3.504120,7.979970,7.229586,1.594703,-8.024040,5.483519,-1.035612,-5.517022,4.638368,7.918698,-4.361131,-0.907383,-9.860386,-3.240328,6.651828,6.990095,-2.447556,0.242585,-6.438265,9.338574,0.333644,-9.201307,-0.385148,3.398851,6.374189,0.939628,7.168418,-1.952850,-6.572488,-0.151244,-1.777912,-0.064646,-5.141446,-0.785687,-5.651409,5.570894,8.961018,7.964584,1.494984,6.426906,3.203775,-1.238469,-4.725497,2.866579,0.947143,6.985320,5.513396,-5.371342,5.403313,-8.804882,-1.680536,8.846672,8.965205,8.481438],[0.979207,2.155985,5.634227,9.682803,-7.106603,-9.682668,9.041173,-4.395457,0.124357,-9.519591,3.034963,8.679128,7.619243,7.159440,1.472158,8.589701,9.542359,-4.507270,-3.033603,2.635504,-6.102579,-2.037204,4.558578,-6.871855,6.817206,7.803453,8.578007,-6.545388,-0.881562,8.547897,-6.060073,-6.039546,7.961723,-5.772646,2.316441,5.888807,9.424527,0.265192,-4.170799,-1.890409,-5.016921,-2.914953,-8.599373,-8.780345,5.197605,-3.089099,-7.637013,0.363443,4.048121,0.526191,4.043394,-6.442050,-1.288339,3.880738,6.401672,-0.225602,-8.713857,5.133358,6.892062,6.189554],[7.494833,-4.048945,-0.093119,-9.377825,3.394762,-6.612500,-8.510086,-7.494918,-2.677131,8.082681,3.417952,-4.087699,-1.697311,-1.121626,2.143902,-8.911876,5.919826,7.620013,0.346792,-2.516661,5.607896,4.527325,9.047619,6.228679,-6.107263,-6.231605,-3.907282,3.487357,-9.346438,6.900946,5.504206,4.779668,-7.752895,-0.164532,-5.461029,3.029261,-4.845035,8.444950,-0.075942,3.238082,1.779295,-2.149923,-4.803529,-2.793715,4.042034,2.313887,-7.206539,4.748313,1.135840,-3.797768,-0.546087,5.433907,-3.657158,6.487308,6.114380,5.742630,-5.259418,2.378164,0.321427,0.625890],[7.468910,0.303325,4.935802,-4.434166,2.735274,-3.712194,-8.974747,-9.839451,-6.201988,2.984993,-6.123194,-7.694201,-5.218796,-6.166680,-4.926054,-4.998456,-2.816800,9.881508,1.605923,-4.144300,-7.670065,-7.007918,-7.380962,0.598731,-2.890892,4.613755,-6.163908,9.514213,3.757685,-7.959690,-4.743149,4.288142,8.836571,-6.650695,-2.673751,0.255844,-2.457380,-3.220281,-9.801156,1.402620,-3.154608,5.538461,9.494036,-1.825219,-7.046221,-0.016392,8.300216,3.227665,-1.746704,5.766561,-2.146971,9.642662,0.905382,-1.867441,0.368844,-6.825886,-9.282334,-5.910376,5.548734,-3.916397],[-8.847296,-9.287623,-3.884968,-0.750124,1.428354,3.120383,-6.817932,-8.036674,-8.500340,7.808255,5.846651,-3.129918,0.740920,2.108101,5.925493,7.246794,-7.827255,3.619068,1.496755,5.523562,-4.753391,6.035206,6.761774,-6.903660,-8.019194,9.076629,3.124361,1.453513,2.262209,8.752775,-3.942050,-0.682496,-8.498290,8.654744,6.245336,2.742667,7.623579,-8.367434,-0.231938,3.384379,-1.976394,-7.509604,-7.994591,-2.106839,-2.128367,-1.553103,-5.493024,7.734015,-9.906959,0.192360,2.979707,5.943122,3.637768,3.341777,-7.894961,-2.450126,-3.114546,3.370630,-7.515068,-5.893110],[3.799261,8.736262,5.139428,1.218634,1.598623,1.275482,3.291735,5.107260,-5.000797,-4.541320,5.889667,8.881726,-8.142676,-2.949746,-8.148435,6.260517,5.976812,-2.472488,-2.785091,2.611274,-5.042662,-1.421391,3.759552,-6.376340,6.260922,2.581331,2.822009,-8.672127,5.002600,-0.280750,9.624375,9.082061,-6.501227,7.174831,9.667717,-3.309753,2.426709,9.230896,-3.068619,-9.536534,2.507565,0.377126,-6.508937,-2.307647,-0.547940,5.802245,-4.996327,3.595122,-6.771855,7.360174,7.827580,5.547385,7.949812,3.316171,-2.532487,5.578388,9.582716,-3.221448,-5.528904,9.743771],[2.574063,-4.079922,-6.366661,-2.485390,-9.806608,-3.978667,4.905693,-6.856616,8.528473,6.676180,1.167477,4.465091,2.993174,-9.774903,-7.801050,-8.202864,-5.432617,2.456652,-5.056956,-6.459508,-5.338684,-7.575349,-1.429233,-2.097838,3.981779,-5.970289,-9.685207,3.502481,2.661932,9.293149,-2.928958,-1.699882,-7.538510,4.392034,9.105075,2.329045,-6.689440,-3.658166,-2.148094,-8.880929,-4.686510,-1.973119,-6.876456,-7.672469,2.528740,4.649750,8.610058,-1.807450,-3.996703,1.039604,8.470808,2.657410,-6.776970,2.647278,-4.195431,-1.206444,-6.618214,4.066953,2.953554,-6.186862],[9.043775,-9.760506,6.675270,-3.113980,-5.745709,-8.091095,-3.339723,4.832037,6.568543,1.441371,7.174378,-5.581331,-4.561135,-3.923803,9.841899,-6.733966,0.454561,4.128007,0.174584,-6.747144,6.068624,-7.079610,-5.909445,3.685145,-5.923603,5.282584,-8.015336,6.990806,5.596204,-7.390855,-4.075997,9.868582,1.117998,6.925472,-3.603940,-6.352721,-6.178206,5.783293,4.816572,-9.771442,6.211271,2.029769,5.040825,-8.133137,-5.981611,5.142019,9.570128,-5.290410,3.316186,2.302750,2.425699,-4.156243,-2.802732,-4.767182,-9.293163,5.965081,-1.974302,8.223198,7.757739,-0.032254],[7.977424,7.601451,-6.269409,3.589408,9.137767,1.159344,2.165944,-6.030790,3.031863,0.799895,8.029978,6.147277,1.238489,7.538978,-9.632378,-8.363273,4.316419,-1.526751,-5.733898,2.525334,9.072828,-6.810546,-4.668581,-2.205430,-2.317594,8.984900,6.878319,9.056017,-7.803361,0.165318,0.534368,-9.249780,9.838224,-6.133651,-9.935475,5.861473,3.201054,-2.860859,-2.660044,3.453860,-9.354275,-8.757062,-6.747623,-9.632855,-1.655713,0.456874,-1.103720,-8.711887,2.438194,2.917744,2.723288,6.889624,-3.722843,-9.274823,-2.664852,1.062063,2.980880,-4.565159,-8.159903,-2.392594],[4.793279,-8.109996,3.960720,9.683397,0.515086,-8.927553,-0.637782,0.412786,-9.589819,3.631526,-9.286694,5.408413,2.614534,4.898605,4.562224,-6.956160,5.275267,-4.060327,-0.962540,2.539379,-8.085814,-1.684416,1.747838,4.502284,0.281617,0.170870,-0.629877,1.865150,-6.630536,8.935288,-3.398586,-1.691285,-4.170182,-9.350283,1.828953,-8.951752,-6.827043,-0.727211,7.977393,0.796453,-6.656182,-8.923428,0.222314,-4.889349,-2.041651,7.173519,-5.044779,-8.241326,-2.725184,0.875655,8.141798,3.978535,-5.333922,8.931421,-8.111969,-4.147369,5.143935,7.150798,8.908368,8.991981],[0.559807,-1.624073,-0.356969,-3.340955,-3.472350,-7.018184,1.610012,6.492710,9.333662,0.549447,8.352871,3.321750,-9.754069,1.367732,-4.841140,9.280463,-4.075475,9.646925,7.733281,4.743229,7.724000,5.956574,-3.378517,-5.463142,2.362193,5.080125,-9.600816,-0.385049,7.714753,-1.572903,-2.333159,7.251337,5.881513,4.584553,-3.906433,-0.265612,7.364245,-3.158544,-3.902202,0.079115,1.515711,-0.498308,7.454874,-5.871861,4.273048,4.651547,5.566613,-3.980698,3.078060,6.845281,-0.877543,-9.902021,6.420097,1.478614,0.546765,0.554544,5.255567,-2.276348,-7.323006,7.194547],[3.779797,7.453979,8.901538,-4.354692,-4.888841,-8.494656,5.931429,-3.727972,-1.530948,6.214821,-9.911484,-0.545087,-9.539980,6.529682,9.948353,-0.099297,2.854541,9.041721,4.335360,0.841587,6.364649,6.528396,-2.505262,6.399246,9.742876,9.336324,-6.106870,-0.863417,-1.459296,7.223832,-7.731557,4.874484,-2.517300,5.063639,-4.311135,7.514909,-3.795855,-6.190909,-8.174177,9.799898,-2.341243,7.964241,-5.385175,-0.530629,0.499816,2.913130,4.231415,0.997384,1.954352,-2.920389,-6.677629,-0.223259,-1.332409,2.822919,-9.857230,-4.530090,4.623426,5.202576,1.065103,1.493276],[-6.683698,8.458944,3.334857,1.359832,6.374221,-7.829582,0.343025,-2.944816,9.857288,-6.677185,1.612388,6.558941,-3.101025,-3.105334,-6.265532,2.787735,-4.281350,-1.755556,6.253629,8.899275,6.351732,-9.671655,-3.061068,-4.224495,7.179824,9.616419,-7.422764,4.861698,-9.128522,-7.879164,8.693138,0.844429,-1.714180,1.421197,6.296078,-8.742517,-9.668652,2.866221,-5.787792,3.626118,-6.689988,-2.536484,2.814160,1.691647,2.672501,-6.904280,3.632123,2.433186,6.135529,-1.483244,8.211527,-5.111084,1.381830,-2.478134,9.121777,3.050497,-1.123625,-8.329359,-7.527900,6.092216],[-7.791938,-9.668896,7.614753,7.134325,6.195712,3.617135,0.662189,-0.721008,3.266582,-7.464942,-5.706141,-0.109329,7.575884,-8.253864,0.392757,5.321224,6.147436,7.248506,4.175150,-6.404525,-3.625675,3.248684,3.894776,2.761451,-2.175787,6.947119,5.665849,-6.423545,2.025102,-8.765611,-3.661328,-2.715107,-8.622976,4.217004,-2.389602,-6.235377,7.473510,-0.102862,6.955111,-9.575051,5.274524,0.638313,1.157440,3.201473,-6.846630,4.989849,-1.825588,1.958938,-8.350786,-1.618883,-8.753887,7.449023,6.004347,-5.214006,9.814693,-6.889285,-7.321218,-6.257135,9.412143,-0.718892],[8.111561,8.994762,6.762495,-5.099239,2.846752,3.647067,6.351115,7.638707,-6.910804,-9.754328,-3.615524,2.592732,-6.491693,9.723184,2.514558,7.871328,5.151222,-5.497109,6.065509,-2.152564,-2.061255,-8.554565,3.153335,-8.936601,1.560825,0.815676,8.770249,8.537929,-1.526894,-7.989238,-9.800357,9.757656,-6.826911,7.617494,-9.035244,-3.865856,9.188085,7.202143,-7.257865,-1.220074,-2.344417,-0.201238,-1.207286,4.875304,-8.196647,6.590002,2.575931,-9.105882,-5.959113,-0.669839,-3.914288,7.305411,6.939112,-3.673310,-5.889712,-3.754449,-3.322498,6.631672,-6.806165,-9.868500]], dtype = "float32")#candidate|8104|(48, 60)|const|float32
call_8103 = relay.TupleGetItem(func_7981_call(relay.reshape(const_8104.astype('float32'), [2880,])), 6)
call_8105 = relay.TupleGetItem(func_7984_call(relay.reshape(const_8104.astype('float32'), [2880,])), 6)
output = relay.Tuple([call_8100,call_8103,const_8104,])
output2 = relay.Tuple([call_8101,call_8105,const_8104,])
func_8120 = relay.Function([], output)
mod['func_8120'] = func_8120
mod = relay.transform.InferType()(mod)
output = func_8120()
func_8121 = relay.Function([], output)
mutated_mod['func_8121'] = func_8121
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8140 = relay.var("var_8140", dtype = "float32", shape = (13, 10, 2))#candidate|8140|(13, 10, 2)|var|float32
uop_8141 = relay.erf(var_8140.astype('float32')) # shape=(13, 10, 2)
func_2294_call = mod.get_global_var('func_2294')
func_2296_call = mutated_mod.get_global_var('func_2296')
var_8153 = relay.var("var_8153", dtype = "float32", shape = (2880,))#candidate|8153|(2880,)|var|float32
call_8152 = relay.TupleGetItem(func_2294_call(relay.reshape(var_8153.astype('float32'), [16, 15, 12])), 0)
call_8154 = relay.TupleGetItem(func_2296_call(relay.reshape(var_8153.astype('float32'), [16, 15, 12])), 0)
uop_8163 = relay.atanh(var_8153.astype('float64')) # shape=(2880,)
uop_8173 = relay.erf(uop_8163.astype('float32')) # shape=(2880,)
bop_8179 = relay.bitwise_or(uop_8173.astype('uint16'), relay.reshape(uop_8163.astype('uint16'), relay.shape_of(uop_8173))) # shape=(2880,)
func_3101_call = mod.get_global_var('func_3101')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_8188 = func_3101_call()
call_8189 = func_3101_call()
output = relay.Tuple([uop_8141,call_8152,bop_8179,call_8188,])
output2 = relay.Tuple([uop_8141,call_8154,bop_8179,call_8189,])
func_8199 = relay.Function([var_8140,var_8153,], output)
mod['func_8199'] = func_8199
mod = relay.transform.InferType()(mod)
var_8200 = relay.var("var_8200", dtype = "float32", shape = (13, 10, 2))#candidate|8200|(13, 10, 2)|var|float32
var_8201 = relay.var("var_8201", dtype = "float32", shape = (2880,))#candidate|8201|(2880,)|var|float32
output = func_8199(var_8200,var_8201,)
func_8202 = relay.Function([var_8200,var_8201,], output)
mutated_mod['func_8202'] = func_8202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3547_call = mod.get_global_var('func_3547')
func_3549_call = mutated_mod.get_global_var('func_3549')
call_8204 = func_3547_call()
call_8205 = func_3547_call()
output = relay.Tuple([call_8204,])
output2 = relay.Tuple([call_8205,])
func_8208 = relay.Function([], output)
mod['func_8208'] = func_8208
mod = relay.transform.InferType()(mod)
mutated_mod['func_8208'] = func_8208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8208_call = mutated_mod.get_global_var('func_8208')
call_8209 = func_8208_call()
output = call_8209
func_8210 = relay.Function([], output)
mutated_mod['func_8210'] = func_8210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4232_call = mod.get_global_var('func_4232')
func_4233_call = mutated_mod.get_global_var('func_4233')
call_8223 = relay.TupleGetItem(func_4232_call(), 0)
call_8224 = relay.TupleGetItem(func_4233_call(), 0)
output = call_8223
output2 = call_8224
func_8230 = relay.Function([], output)
mod['func_8230'] = func_8230
mod = relay.transform.InferType()(mod)
mutated_mod['func_8230'] = func_8230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8230_call = mutated_mod.get_global_var('func_8230')
call_8231 = func_8230_call()
output = call_8231
func_8232 = relay.Function([], output)
mutated_mod['func_8232'] = func_8232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4798_call = mod.get_global_var('func_4798')
func_4800_call = mutated_mod.get_global_var('func_4800')
call_8247 = relay.TupleGetItem(func_4798_call(), 1)
call_8248 = relay.TupleGetItem(func_4800_call(), 1)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_8259 = relay.TupleGetItem(func_2564_call(), 0)
call_8260 = relay.TupleGetItem(func_2566_call(), 0)
func_7096_call = mod.get_global_var('func_7096')
func_7097_call = mutated_mod.get_global_var('func_7097')
call_8267 = relay.TupleGetItem(func_7096_call(), 0)
call_8268 = relay.TupleGetItem(func_7097_call(), 0)
output = relay.Tuple([call_8247,call_8259,call_8267,])
output2 = relay.Tuple([call_8248,call_8260,call_8268,])
func_8274 = relay.Function([], output)
mod['func_8274'] = func_8274
mod = relay.transform.InferType()(mod)
mutated_mod['func_8274'] = func_8274
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8274_call = mutated_mod.get_global_var('func_8274')
call_8275 = func_8274_call()
output = call_8275
func_8276 = relay.Function([], output)
mutated_mod['func_8276'] = func_8276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2872_call = mutated_mod.get_global_var('func_2872')
call_8326 = relay.TupleGetItem(func_2870_call(), 0)
call_8327 = relay.TupleGetItem(func_2872_call(), 0)
func_3603_call = mod.get_global_var('func_3603')
func_3604_call = mutated_mod.get_global_var('func_3604')
call_8330 = relay.TupleGetItem(func_3603_call(), 0)
call_8331 = relay.TupleGetItem(func_3604_call(), 0)
func_6882_call = mod.get_global_var('func_6882')
func_6884_call = mutated_mod.get_global_var('func_6884')
call_8342 = relay.TupleGetItem(func_6882_call(), 2)
call_8343 = relay.TupleGetItem(func_6884_call(), 2)
output = relay.Tuple([call_8326,call_8330,call_8342,])
output2 = relay.Tuple([call_8327,call_8331,call_8343,])
func_8345 = relay.Function([], output)
mod['func_8345'] = func_8345
mod = relay.transform.InferType()(mod)
mutated_mod['func_8345'] = func_8345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8345_call = mutated_mod.get_global_var('func_8345')
call_8346 = func_8345_call()
output = call_8346
func_8347 = relay.Function([], output)
mutated_mod['func_8347'] = func_8347
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8368 = relay.const([[[7.312050,3.070361,2.911493],[1.581055,-8.377967,5.365226],[5.725283,-0.046973,7.803493],[-0.076652,-7.470777,4.571652],[-1.901070,-7.500874,-3.177692],[-4.339523,-5.081498,-8.801794],[8.000397,5.469072,4.572945],[4.695466,-7.107338,-2.987355],[-3.181335,1.162291,3.859407],[3.502698,-8.004858,-7.921692],[6.487980,-4.955502,-5.081182],[6.475726,1.511358,4.561830],[1.295469,6.004699,-8.114995],[-8.182609,-4.223352,5.080559]],[[-9.392330,4.117786,-0.364291],[5.834350,-3.414028,-8.844430],[-3.949178,5.277697,-5.452923],[-1.712792,6.228615,9.421876],[8.652827,-7.001108,4.003629],[-4.386482,-2.089672,4.028846],[7.159015,-6.338786,-9.347304],[-1.323093,-5.477576,-7.115110],[-5.432392,5.376361,-6.559043],[9.066029,-2.301229,5.212842],[1.209555,7.207293,9.707948],[3.934569,-4.712849,4.217742],[-0.234555,8.183767,9.132310],[8.161273,1.039153,5.938046]],[[9.143921,7.286203,2.488802],[3.554896,-3.104562,-8.644961],[7.077738,-8.621426,-4.546557],[2.892801,9.988811,5.426230],[-8.138683,-3.791820,1.723426],[-5.038029,-5.725123,-3.648932],[-1.532563,5.584037,3.604922],[1.127104,5.693367,-5.877770],[7.661958,-0.404998,-5.124334],[3.967262,-0.502034,-6.655254],[5.174230,-2.214259,5.735194],[9.789322,-7.220254,-8.798451],[8.948303,3.962650,-6.838793],[-9.145438,7.452573,-6.132601]],[[-1.106107,-0.054807,-2.649689],[3.780062,2.223340,3.915950],[-2.436603,8.509356,0.011006],[-6.591793,2.165871,2.268039],[3.084454,1.607434,-7.173464],[1.765743,6.498876,4.245338],[-9.850005,5.575892,-6.646086],[-0.945487,-5.170915,-5.366281],[-5.789588,-1.948366,-8.713420],[7.132579,2.640157,-2.089651],[-1.470883,-0.572207,3.060267],[6.048413,-7.005644,-9.956300],[-6.854542,-9.215012,-5.505820],[-7.950971,8.176319,-4.026422]],[[5.217941,-5.336260,-8.282228],[-8.120272,-8.344067,-9.370826],[5.111459,3.618837,-3.442885],[-9.914567,8.952072,1.343825],[3.936910,-7.814396,-5.281926],[-1.846459,-0.732577,-1.604245],[6.499238,1.041404,-4.851239],[-8.576661,-1.166233,9.934162],[7.439211,9.394283,-0.325563],[-6.526561,-4.259468,2.590320],[9.288787,-9.120909,-5.205885],[-8.512543,-2.938893,4.058363],[6.202621,-0.925672,9.916580],[-2.237281,3.665659,0.551376]],[[7.455047,-4.498457,-0.773206],[-6.174169,6.279719,9.744921],[-2.156111,-9.986183,-7.760618],[1.453344,9.328051,0.562559],[6.243710,3.974733,6.289752],[4.708498,-3.939131,-0.588131],[0.166363,-3.396097,-7.917733],[-7.952407,8.134224,0.943678],[-5.904675,4.777275,-2.922252],[-9.326303,-3.489447,-4.684259],[2.046939,-4.813587,2.039459],[-0.112119,-9.251161,-3.913167],[1.696392,7.918585,1.528263],[-0.085593,2.575162,0.504506]],[[-4.982071,1.427419,6.144377],[-8.987486,0.107651,-4.520987],[8.158163,2.293393,1.400021],[-4.052406,-2.762077,6.003745],[-2.790619,4.115257,5.630710],[3.008092,7.048107,-0.936690],[9.243543,3.878181,-6.183942],[1.034904,-9.843008,0.464936],[-5.801561,-4.994107,0.050646],[-0.744297,1.816460,6.555742],[-8.337103,-0.402504,3.371512],[-3.153451,3.737869,-9.797970],[3.752545,-7.342780,-6.605548],[6.123276,8.686965,-8.035643]],[[8.738699,4.913455,-7.990109],[5.375355,6.410505,-6.513945],[6.137645,9.373536,-1.600203],[-4.237766,-2.202859,-4.909025],[-3.779774,6.422903,0.313046],[-2.325035,7.841742,-4.290838],[-8.494381,-3.337754,9.064223],[-1.481554,-1.081495,-5.589747],[4.410399,-1.158461,9.138596],[0.052793,7.871689,4.903546],[-9.419692,7.884221,1.714095],[4.979889,-5.705315,-5.211307],[3.929841,-4.675980,-1.866631],[-7.524389,1.779618,6.458911]]], dtype = "float32")#candidate|8368|(8, 14, 3)|const|float32
var_8369 = relay.var("var_8369", dtype = "float32", shape = (8, 14, 3))#candidate|8369|(8, 14, 3)|var|float32
bop_8370 = relay.multiply(const_8368.astype('float32'), relay.reshape(var_8369.astype('float32'), relay.shape_of(const_8368))) # shape=(8, 14, 3)
func_7019_call = mod.get_global_var('func_7019')
func_7021_call = mutated_mod.get_global_var('func_7021')
call_8385 = func_7019_call()
call_8386 = func_7019_call()
uop_8397 = relay.sin(var_8369.astype('float32')) # shape=(8, 14, 3)
output = relay.Tuple([bop_8370,call_8385,uop_8397,])
output2 = relay.Tuple([bop_8370,call_8386,uop_8397,])
func_8399 = relay.Function([var_8369,], output)
mod['func_8399'] = func_8399
mod = relay.transform.InferType()(mod)
mutated_mod['func_8399'] = func_8399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8400 = relay.var("var_8400", dtype = "float32", shape = (8, 14, 3))#candidate|8400|(8, 14, 3)|var|float32
func_8399_call = mutated_mod.get_global_var('func_8399')
call_8401 = func_8399_call(var_8400)
output = call_8401
func_8402 = relay.Function([var_8400], output)
mutated_mod['func_8402'] = func_8402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7258_call = mod.get_global_var('func_7258')
func_7259_call = mutated_mod.get_global_var('func_7259')
call_8457 = relay.TupleGetItem(func_7258_call(), 0)
call_8458 = relay.TupleGetItem(func_7259_call(), 0)
func_7240_call = mod.get_global_var('func_7240')
func_7241_call = mutated_mod.get_global_var('func_7241')
call_8462 = relay.TupleGetItem(func_7240_call(), 0)
call_8463 = relay.TupleGetItem(func_7241_call(), 0)
var_8476 = relay.var("var_8476", dtype = "float32", shape = (20,))#candidate|8476|(20,)|var|float32
bop_8477 = relay.less(call_8462.astype('bool'), relay.reshape(var_8476.astype('bool'), relay.shape_of(call_8462))) # shape=(20,)
bop_8480 = relay.less(call_8463.astype('bool'), relay.reshape(var_8476.astype('bool'), relay.shape_of(call_8463))) # shape=(20,)
output = relay.Tuple([call_8457,bop_8477,])
output2 = relay.Tuple([call_8458,bop_8480,])
func_8482 = relay.Function([var_8476,], output)
mod['func_8482'] = func_8482
mod = relay.transform.InferType()(mod)
mutated_mod['func_8482'] = func_8482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8483 = relay.var("var_8483", dtype = "float32", shape = (20,))#candidate|8483|(20,)|var|float32
func_8482_call = mutated_mod.get_global_var('func_8482')
call_8484 = func_8482_call(var_8483)
output = call_8484
func_8485 = relay.Function([var_8483], output)
mutated_mod['func_8485'] = func_8485
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8523 = relay.const([[[-3,10,9,8,-4,-6,9,4,-5,-3,5,7,-2,4],[8,-7,-7,4,-2,9,-7,10,6,-9,-2,6,-8,-9],[-1,-8,-4,-1,-3,-1,9,3,-7,-4,-7,-6,7,10],[-6,-6,3,7,10,-10,-4,7,1,1,-3,10,2,-10],[-9,-4,9,-3,3,-10,7,7,-1,7,4,-7,-7,-10],[-5,7,1,1,1,-4,6,-9,-6,-4,-1,-8,-1,6],[3,6,-6,-4,-4,1,-10,2,-1,-9,-9,3,-6,-9],[-7,6,10,-8,4,-5,8,4,1,6,-8,8,-7,-9],[3,1,-2,-9,-8,-1,10,1,-2,-8,2,4,8,-9]],[[-4,-10,-6,-8,-10,1,4,10,-7,-4,7,-1,-5,-1],[6,7,-8,-8,8,3,3,-5,5,2,6,3,7,2],[-7,-2,5,-7,-6,9,3,1,-7,4,4,6,-2,-3],[2,-1,-10,-4,-2,-10,-5,2,3,3,-2,2,5,-5],[-8,7,4,9,-3,-9,-3,3,9,8,-1,-10,10,-10],[-3,-3,3,-8,-2,-1,9,9,-8,-2,2,-9,-2,7],[-2,-8,-1,-5,-3,-1,10,-9,1,-3,-2,8,-6,6],[-5,-10,1,-1,9,7,8,6,-10,-7,2,-10,6,8],[-2,-7,-1,-5,5,5,1,-5,-1,-9,5,-10,7,-3]],[[5,-4,-10,-5,10,-1,5,8,-1,-8,-5,1,-4,-8],[10,-5,-5,-5,10,3,-9,2,2,1,4,-6,-6,-8],[10,1,-7,7,3,-6,2,-2,4,5,5,-1,-5,7],[-6,10,-3,5,7,-2,4,5,7,-6,-3,-9,9,1],[-9,-3,-5,10,-4,-8,7,-3,-7,-8,6,-7,7,1],[-8,-7,-1,1,-5,-2,3,2,-9,2,1,-2,4,-10],[-5,-6,-3,9,5,-10,8,1,-3,3,6,-9,3,-6],[9,9,-8,7,8,-5,-6,7,-10,-7,-9,-4,6,-4],[5,8,-7,-9,2,4,4,6,8,-3,-10,-1,1,-6]]], dtype = "uint8")#candidate|8523|(3, 9, 14)|const|uint8
const_8524 = relay.const([[[9,7,6,-5,-1,-5,4,-3,10,-5,-5,-3,7,10],[8,-5,6,6,-1,4,-1,-2,-6,-1,-8,1,-1,2],[-8,1,10,4,5,8,4,-2,3,-2,-1,-7,-1,-4],[-5,-10,1,-10,7,-5,-7,-10,4,-5,-8,-8,-10,-9],[3,3,2,-10,7,1,3,6,-8,-10,2,1,-10,8],[4,-1,1,-5,-7,5,3,8,2,8,4,-4,3,4],[-4,5,2,-5,2,-5,2,-3,-7,-5,-6,-1,-2,5],[-2,-1,5,-4,-4,9,8,-4,-5,-7,9,3,4,-6],[-1,-4,-1,-9,10,3,-2,-9,6,1,2,4,-10,9]],[[-3,2,7,4,10,-4,7,-6,10,1,1,-7,-10,6],[-10,-3,9,6,3,4,3,4,7,-3,7,5,6,3],[-5,-3,6,-9,-5,-1,-4,2,6,1,7,-2,-8,4],[-9,7,8,2,-9,-8,-5,-1,-5,8,8,-5,-5,-9],[4,-6,-10,8,4,9,10,-6,-6,5,1,-1,5,5],[-2,3,-8,10,2,6,-7,-9,-4,-5,-3,2,-6,-6],[10,10,-6,10,4,3,-8,-1,-6,6,-5,-10,9,-6],[-4,7,4,6,2,5,5,-1,-7,-10,3,2,-4,8],[-4,-10,5,-2,7,-8,-5,-7,10,-3,-10,-1,8,-1]],[[-6,10,1,8,-9,6,8,5,6,-4,-9,3,-10,2],[-8,4,2,-3,6,-1,-2,1,1,-5,-9,3,-6,7],[3,-7,4,6,-5,-1,2,4,-10,-8,-2,-8,-10,10],[7,3,9,-2,1,-1,9,-5,-5,-7,-5,-8,7,-9],[6,4,-7,5,7,10,-7,4,2,-9,10,4,10,-6],[5,-6,7,6,7,9,-1,3,10,4,-9,-9,-10,8],[-4,-8,10,-1,2,-10,-1,4,-9,-9,-6,-1,5,-6],[4,4,-6,8,-6,4,8,-8,6,8,1,-4,-10,2],[8,2,-9,1,-1,-5,10,5,-5,5,-7,7,-2,-4]]], dtype = "uint8")#candidate|8524|(3, 9, 14)|const|uint8
bop_8525 = relay.maximum(const_8523.astype('uint8'), relay.reshape(const_8524.astype('uint8'), relay.shape_of(const_8523))) # shape=(3, 9, 14)
func_7638_call = mod.get_global_var('func_7638')
func_7640_call = mutated_mod.get_global_var('func_7640')
call_8528 = func_7638_call()
call_8529 = func_7638_call()
var_8532 = relay.var("var_8532", dtype = "float64", shape = (6, 12, 7))#candidate|8532|(6, 12, 7)|var|float64
bop_8533 = relay.less_equal(call_8528.astype('bool'), relay.reshape(var_8532.astype('bool'), relay.shape_of(call_8528))) # shape=(6, 12, 7)
bop_8536 = relay.less_equal(call_8529.astype('bool'), relay.reshape(var_8532.astype('bool'), relay.shape_of(call_8529))) # shape=(6, 12, 7)
output = relay.Tuple([bop_8525,bop_8533,])
output2 = relay.Tuple([bop_8525,bop_8536,])
func_8538 = relay.Function([var_8532,], output)
mod['func_8538'] = func_8538
mod = relay.transform.InferType()(mod)
mutated_mod['func_8538'] = func_8538
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8539 = relay.var("var_8539", dtype = "float64", shape = (6, 12, 7))#candidate|8539|(6, 12, 7)|var|float64
func_8538_call = mutated_mod.get_global_var('func_8538')
call_8540 = func_8538_call(var_8539)
output = call_8540
func_8541 = relay.Function([var_8539], output)
mutated_mod['func_8541'] = func_8541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8208_call = mod.get_global_var('func_8208')
func_8210_call = mutated_mod.get_global_var('func_8210')
call_8563 = relay.TupleGetItem(func_8208_call(), 0)
call_8564 = relay.TupleGetItem(func_8210_call(), 0)
output = call_8563
output2 = call_8564
func_8572 = relay.Function([], output)
mod['func_8572'] = func_8572
mod = relay.transform.InferType()(mod)
mutated_mod['func_8572'] = func_8572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8572_call = mutated_mod.get_global_var('func_8572')
call_8573 = func_8572_call()
output = call_8573
func_8574 = relay.Function([], output)
mutated_mod['func_8574'] = func_8574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4495_call = mod.get_global_var('func_4495')
func_4496_call = mutated_mod.get_global_var('func_4496')
call_8575 = relay.TupleGetItem(func_4495_call(), 0)
call_8576 = relay.TupleGetItem(func_4496_call(), 0)
output = call_8575
output2 = call_8576
func_8580 = relay.Function([], output)
mod['func_8580'] = func_8580
mod = relay.transform.InferType()(mod)
mutated_mod['func_8580'] = func_8580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8580_call = mutated_mod.get_global_var('func_8580')
call_8581 = func_8580_call()
output = call_8581
func_8582 = relay.Function([], output)
mutated_mod['func_8582'] = func_8582
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8602 = relay.var("var_8602", dtype = "float64", shape = (8, 13, 2))#candidate|8602|(8, 13, 2)|var|float64
uop_8603 = relay.sigmoid(var_8602.astype('float64')) # shape=(8, 13, 2)
output = relay.Tuple([uop_8603,])
output2 = relay.Tuple([uop_8603,])
func_8614 = relay.Function([var_8602,], output)
mod['func_8614'] = func_8614
mod = relay.transform.InferType()(mod)
mutated_mod['func_8614'] = func_8614
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8615 = relay.var("var_8615", dtype = "float64", shape = (8, 13, 2))#candidate|8615|(8, 13, 2)|var|float64
func_8614_call = mutated_mod.get_global_var('func_8614')
call_8616 = func_8614_call(var_8615)
output = call_8616
func_8617 = relay.Function([var_8615], output)
mutated_mod['func_8617'] = func_8617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4902_call = mod.get_global_var('func_4902')
func_4903_call = mutated_mod.get_global_var('func_4903')
call_8619 = relay.TupleGetItem(func_4902_call(), 1)
call_8620 = relay.TupleGetItem(func_4903_call(), 1)
output = relay.Tuple([call_8619,])
output2 = relay.Tuple([call_8620,])
func_8634 = relay.Function([], output)
mod['func_8634'] = func_8634
mod = relay.transform.InferType()(mod)
mutated_mod['func_8634'] = func_8634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8634_call = mutated_mod.get_global_var('func_8634')
call_8635 = func_8634_call()
output = call_8635
func_8636 = relay.Function([], output)
mutated_mod['func_8636'] = func_8636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5716_call = mod.get_global_var('func_5716')
func_5717_call = mutated_mod.get_global_var('func_5717')
call_8654 = relay.TupleGetItem(func_5716_call(), 0)
call_8655 = relay.TupleGetItem(func_5717_call(), 0)
func_6800_call = mod.get_global_var('func_6800')
func_6802_call = mutated_mod.get_global_var('func_6802')
call_8656 = relay.TupleGetItem(func_6800_call(), 0)
call_8657 = relay.TupleGetItem(func_6802_call(), 0)
output = relay.Tuple([call_8654,call_8656,])
output2 = relay.Tuple([call_8655,call_8657,])
func_8658 = relay.Function([], output)
mod['func_8658'] = func_8658
mod = relay.transform.InferType()(mod)
mutated_mod['func_8658'] = func_8658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8658_call = mutated_mod.get_global_var('func_8658')
call_8659 = func_8658_call()
output = call_8659
func_8660 = relay.Function([], output)
mutated_mod['func_8660'] = func_8660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4798_call = mod.get_global_var('func_4798')
func_4800_call = mutated_mod.get_global_var('func_4800')
call_8757 = relay.TupleGetItem(func_4798_call(), 0)
call_8758 = relay.TupleGetItem(func_4800_call(), 0)
func_8120_call = mod.get_global_var('func_8120')
func_8121_call = mutated_mod.get_global_var('func_8121')
call_8819 = relay.TupleGetItem(func_8120_call(), 2)
call_8820 = relay.TupleGetItem(func_8121_call(), 2)
const_8824 = relay.const([[-0.182698,1.796005,-4.336717,2.589859,7.527108,-7.589648,-4.081728,-2.817034,-0.770076,-7.983206,9.080776,5.898497,-0.341189,6.040484,5.931840,-1.291986,-7.821971,1.878913,5.600225,-0.822419,9.421703,-2.732692,-0.767554,5.943783,-2.467714,-7.434102,-7.345015,-0.275752,-9.792377,0.552310,7.876363,4.111464,0.430031,-5.066703,-1.184526,-6.431179,2.804612,7.784328,2.007607,-1.247515,-6.645106,5.849432,-5.834050,-9.826016,5.422323,-8.959515,4.472037,7.726524,9.467812,0.680213,-2.173746,2.505439,-8.490861,-2.778328,0.417370,-4.995685,3.637847,-5.404457,6.641062,-4.293513],[-4.753129,2.633650,3.065843,4.773604,-4.166306,-4.876724,-9.052910,-2.333843,-8.199586,-1.477910,4.608409,6.729545,-6.212660,6.851428,-0.582214,6.131835,-1.989217,5.500122,3.455332,-4.141312,5.800713,-0.269445,-6.055776,6.943916,9.765753,-7.769168,-6.545757,-2.356146,-1.743923,-8.906981,3.224960,8.148384,7.929699,8.297563,8.398168,-3.828335,-3.226178,-6.915668,-3.624632,9.112424,3.596825,-9.734520,-5.061154,7.273099,-7.409055,7.227753,3.274649,-9.080858,2.901807,7.251834,9.949324,-0.434934,-9.124192,2.888591,-0.931250,8.126873,-4.007386,1.212248,-9.482961,5.073690],[-4.605934,-7.319475,-6.767997,-3.124642,1.585286,-9.213861,-9.440917,-3.348029,-5.536504,8.109245,5.966468,-3.728010,-3.424759,-2.456768,-1.450376,-8.348088,-8.084597,-3.830157,7.459738,8.226664,-9.637532,9.169409,-2.717303,-0.536004,3.543984,4.636973,-1.800182,2.108317,5.889796,0.533277,0.945836,-7.749794,-1.747524,-9.259109,-2.880053,-9.566146,-5.679181,3.800614,-2.343826,6.041329,0.611289,-4.204013,-0.823105,-5.642767,1.619162,-9.419515,7.832732,-5.433157,2.252749,0.443317,-2.167837,3.212242,-4.570971,0.718405,-5.615791,-9.862041,2.749796,6.333819,-5.509839,1.771314],[8.842210,1.252660,2.723577,-0.104287,-7.969966,-9.348871,-7.703522,4.589340,-0.431554,8.327587,3.477310,-5.968248,-2.696515,8.283450,5.056776,-3.231492,-4.986883,-6.000258,3.476003,-4.999030,-3.286012,9.026578,-9.957406,2.220358,6.378562,5.538263,5.204526,-0.776214,2.428917,-5.522590,-9.574451,3.055447,-1.198927,-2.022273,0.739085,-9.738589,4.804394,-2.779717,-2.438341,-3.197219,-9.749284,0.828826,0.726589,1.604458,1.766508,-4.419019,-1.613088,-5.452401,7.508258,-8.722730,4.040241,-4.679880,-9.177393,9.404374,7.629806,0.519334,1.313795,2.579808,-1.406126,-0.034693],[-7.236808,0.809727,-8.330924,-6.396231,3.527266,-6.088959,2.813144,5.029630,5.137024,-3.487384,5.120414,-5.431771,-2.896998,5.012974,-3.990875,-8.834842,-6.839287,3.920328,6.175460,-4.061323,5.999350,-6.994759,-9.155310,-0.772335,-6.687857,-6.239029,-0.749065,-0.220430,-0.868764,3.659997,4.311416,2.088411,-1.000717,7.664917,-6.522762,-8.240996,-4.984710,-2.723955,-2.321427,2.024465,-9.763704,-5.418470,-0.421769,3.952213,4.764601,-5.665562,0.298047,-5.034295,-1.047704,5.720792,-3.673059,-0.668737,-6.017503,6.671745,-0.530702,7.169314,-6.301972,8.721422,2.272244,4.898628],[-1.365198,3.127235,0.708724,0.063519,2.472593,4.259296,-9.368276,3.446436,-3.647601,0.642939,7.051953,9.226940,9.899648,-5.765952,-5.953987,3.629741,4.035609,-2.167126,-9.907190,7.242394,-4.333647,1.253576,-7.429215,-7.269182,7.553407,9.950802,-4.841392,-4.551078,-1.780725,-4.654488,-4.244213,3.480601,7.409115,0.711452,7.652676,8.215553,8.454031,-4.493073,0.275307,-2.074542,-0.509498,4.312352,6.648908,-1.030473,1.506721,-4.170842,-3.000569,7.266518,5.734848,-2.634026,0.577637,-9.329487,-3.741429,2.592929,2.346584,0.687370,5.814378,0.439146,-2.182439,-8.374877],[-2.461578,-4.825732,-8.436090,-7.851900,-6.222654,-1.050521,7.887325,-4.902215,1.767695,8.309780,0.530598,4.671079,-7.622801,3.303055,-5.850479,-5.993767,-6.949965,-3.476990,-1.464860,-0.404998,4.953294,1.476149,-1.917394,-2.592489,5.895937,-6.367448,-0.727483,2.779483,-3.031839,-7.697872,5.567132,-0.377826,3.147936,-8.532110,0.218353,-4.257208,-0.189030,1.648291,5.591975,-8.800882,-3.875758,6.307063,-8.245419,1.528316,-4.366177,-0.488418,-1.723506,5.830346,4.981360,6.603756,2.500744,0.452098,7.979370,-9.959685,-1.370684,8.435514,8.795691,-1.965664,-0.321926,2.445926],[5.229081,-1.670508,-9.352253,8.390351,9.678343,-4.243193,-5.891031,-2.156662,0.032156,-7.964860,-3.170153,-5.263673,-6.741163,4.659412,-3.957396,8.147013,-8.778266,3.331383,-6.047345,-3.522033,5.235826,-9.024340,-5.043538,-9.207921,8.176148,-7.475720,-2.137627,8.640555,5.532828,2.941144,2.806757,0.919865,-6.925656,-6.551497,9.996770,2.974547,-5.028602,-3.770090,-8.326459,-8.014055,0.522060,6.189075,6.815675,-1.111547,-9.368087,-8.980377,7.470078,0.452656,-2.622909,-1.037365,5.661406,-3.268659,7.360933,-5.012856,1.318860,9.518740,0.386851,6.407122,8.544660,9.811078],[6.807947,-0.858253,2.689794,3.874164,6.119660,2.155813,7.062668,-5.994958,-9.347071,-0.409825,6.327646,-0.645373,6.084768,0.014937,-3.279322,-0.260352,-0.919286,-0.727963,-5.139596,6.260596,6.713774,-1.420269,5.593755,9.473728,-8.283677,3.193910,8.221291,-4.229759,6.917109,4.941227,2.247991,-8.383634,-8.961865,0.891099,-0.769129,0.503186,-1.230607,-0.514695,-7.410779,2.581735,6.320840,2.193289,1.962015,7.418144,7.802913,-6.433242,-1.184547,1.259952,4.100520,-4.867497,1.846165,5.005104,2.599075,1.326060,4.698202,-9.253214,-5.435502,4.908068,-2.018960,-9.266405],[4.695958,-9.729168,7.374824,6.899930,-3.382431,-5.022606,3.085246,4.637221,4.340547,-2.924499,-7.663851,-4.455780,-4.942860,-7.504039,-4.342283,0.025720,9.828795,-1.317073,7.657343,0.292227,5.283842,8.190250,3.445431,7.028849,-9.252570,7.389047,8.071145,5.985601,7.956074,-8.719291,-2.778259,8.285163,5.347599,5.733232,2.741554,-2.113421,-8.206195,3.631860,3.282036,0.900093,5.482975,-2.539235,-5.463999,-4.005536,6.533742,6.825896,-7.212584,0.298968,-4.292539,-0.740024,4.947089,-8.775470,9.766343,8.599032,5.389176,-1.211262,0.965112,7.087879,-9.899712,8.214661],[-9.836744,6.576545,0.188520,-7.247990,7.089797,-3.418619,0.852108,0.073256,-0.534637,1.861361,7.897885,-8.597493,-8.406461,-6.706187,-5.511497,-2.296815,-0.798254,6.675567,-3.468524,-8.012486,9.762946,-4.698808,5.701987,8.151836,-3.441075,2.509619,-9.658107,-4.185501,6.100167,1.119395,-6.584902,-8.654763,7.400013,7.770382,7.391354,-7.485425,-1.080821,-4.082159,-9.808131,7.989716,-3.855982,-9.057668,5.235904,-3.939005,8.515733,-9.132224,3.164430,-8.135213,-6.545592,7.105106,3.333613,-4.710352,-0.503817,-6.906222,-7.490714,-5.869317,-1.565833,3.122480,4.148915,3.481943],[4.642232,0.198834,-8.153461,-9.475770,6.660628,4.055916,0.712533,-7.755174,-4.111922,-3.665915,-8.413395,2.250900,3.546127,-4.870773,-9.663609,4.599453,7.808105,8.624316,-2.221907,9.073131,5.162890,2.144101,-6.262282,-9.079089,-8.580507,-8.078064,3.590372,5.007561,-4.158525,-3.568521,9.741716,0.225233,-3.044298,8.026414,-2.859032,-1.500168,2.130663,-0.582203,1.488141,-4.970600,5.333829,-1.753659,-3.201261,1.168273,-9.169843,-4.137485,9.370704,-8.845305,-6.755029,-8.754275,-6.662209,-1.481615,-0.416296,-3.518287,1.971066,6.942216,4.179768,-6.009539,-5.367467,-1.974583],[9.199749,-2.349535,-7.735916,-1.512674,-4.111760,5.836178,4.127546,-5.768094,-6.393173,3.102525,4.082802,-0.550274,-6.496541,2.724557,-9.779988,5.489042,-8.138176,-6.790683,7.002200,9.145525,-0.097058,-7.380907,-1.021508,1.424896,5.978236,-2.833789,-2.484141,6.908689,4.948739,2.581243,3.056638,9.839870,-3.624617,-7.684829,-1.016899,-7.592193,6.559112,-9.221457,1.026299,-0.540367,-1.386492,-9.676559,-6.689627,-7.763674,-1.339083,2.798211,-9.595480,1.338015,0.794005,-1.270259,5.323943,-1.550136,-9.643546,-0.369757,-0.934164,-3.865602,1.233198,9.930373,3.011333,-4.650311],[1.871421,0.261575,-5.666395,6.932563,-7.117923,-8.534027,-7.153025,-9.413931,0.172901,-6.010925,-9.581719,3.491365,6.955849,5.090661,-5.780954,-7.147147,7.862955,8.936930,-0.758842,0.505150,0.070577,-3.092153,-6.807610,-3.628783,0.872330,-3.533898,7.124682,-8.434071,-8.681470,5.495749,7.739566,7.093614,6.055565,-6.584172,5.759362,1.117901,2.433771,-9.264566,-2.389261,-1.646436,5.694434,1.027622,-5.720116,-5.726944,9.733866,0.102419,9.749501,-5.698859,0.527872,3.671857,-6.771919,9.863535,-4.557119,-7.585346,-9.588633,6.552227,1.593056,1.792310,-8.047422,-6.614135],[5.637120,-7.011366,-7.064706,-3.881359,0.459394,-8.427265,-8.155178,-9.010686,8.464790,4.741214,2.064064,-6.656007,-9.834526,-0.320224,5.974366,-1.738606,-5.135779,5.210963,2.448012,-0.414476,9.337061,7.376958,0.440715,8.688168,-7.194995,-7.956539,5.316659,-0.049235,-8.310827,-0.701954,7.803122,2.145363,3.048917,9.234416,-9.221680,4.766055,-0.325651,4.227622,-4.066425,7.278068,5.896626,-7.467200,-2.274368,-7.262906,5.325240,-7.724937,-0.100223,-8.364870,-0.916449,-1.005365,-1.129546,2.469394,-4.451516,-6.355428,9.501493,2.709300,3.149823,8.959853,-4.658754,0.145280],[-3.576291,3.542470,8.450468,-3.716375,0.125163,-2.139951,-5.988860,-4.632529,-4.775748,-2.356390,-9.359500,-4.757969,3.600708,7.231241,-1.746061,-5.186616,-2.815795,6.122365,9.952290,-0.702905,-1.900461,-3.412548,-8.092874,-9.111179,5.959668,-0.834915,-1.629074,-7.424157,-8.530467,-4.517373,-1.779631,3.950897,-7.919076,-9.052156,-4.727107,-4.915091,7.585637,2.510650,2.189321,-1.835640,-5.581123,0.359995,1.020519,8.459925,4.580526,-4.700649,-1.342868,3.704076,-4.857486,-0.366283,-9.055867,-8.386835,-8.549327,9.424380,6.153744,-2.237281,-9.011932,-8.992797,2.700627,3.855478],[4.685431,-1.060004,2.027378,-2.213754,7.548555,-8.209542,7.860937,8.675132,-1.572126,-3.186083,-2.562637,-9.349373,-1.610764,8.335326,-4.246424,-8.627065,-6.569692,5.512178,-2.621324,-4.113688,-1.880150,3.760679,4.557405,3.762278,9.116876,6.918487,7.665425,-3.684891,-6.261613,6.248560,-1.592420,7.217104,1.394341,-1.160978,-7.974461,7.000605,5.489686,9.339387,-1.656641,4.322870,-1.444207,2.924435,-7.631115,5.496991,8.166003,6.509880,-9.186371,2.015484,1.897120,-7.073709,-4.439403,-3.313814,-0.960462,-0.154413,3.092872,6.545268,-3.046420,0.997689,-3.579594,0.612636],[3.318647,-5.771402,3.457492,3.026430,5.991563,1.512365,-6.920141,-2.471913,7.236158,3.376914,-2.976238,-7.519533,1.673194,4.326787,-6.434403,-1.631696,6.055790,4.463034,-1.847633,2.908267,-4.363279,0.206165,-2.061492,-1.123751,-4.904113,-0.193000,-4.878759,7.741826,-9.823091,2.263837,9.072858,0.884074,-3.467059,-5.878366,0.650667,7.688577,-6.287097,-3.482353,-9.448286,-9.527564,-4.991597,1.771200,2.238354,2.983511,0.392335,-5.903615,-5.629495,6.372937,-6.424374,7.591320,3.339809,-4.520361,5.637849,-5.255043,6.884553,-9.433134,-2.255603,-5.709151,-3.159422,8.661966],[-8.337633,-6.242633,2.285070,-3.065912,7.760414,-1.195338,-6.570650,-3.560519,4.556048,5.668418,4.069904,2.479013,5.991810,6.643096,6.458959,6.124725,-5.620067,-7.283783,5.771602,-2.301124,-6.334184,8.919437,7.122731,-9.345614,-1.074668,5.062038,6.140821,6.320926,-7.439111,-2.165063,-7.854247,8.920891,2.472677,-0.540720,-4.121454,-3.196566,1.804585,1.285299,1.966913,-9.658265,9.584856,-3.605203,-0.387687,8.279014,-2.861351,-3.996529,4.963827,-7.831456,6.272738,3.250238,0.024402,-9.592646,0.521977,2.002769,9.944867,6.760546,3.420626,4.134049,3.043285,-3.087214],[-5.119843,-4.807352,-1.648905,-3.453845,-1.902054,-9.816504,1.707298,-3.137756,-5.967301,-1.723877,0.091833,3.030691,1.088787,-9.947625,9.356796,-1.210854,9.483321,-6.876852,8.583492,4.324583,-8.986898,3.516297,-8.434248,6.467870,2.936217,-8.564369,6.560406,7.477604,-9.888127,6.603680,-1.838592,0.596707,3.447296,-0.353301,6.983395,-5.913600,6.122420,5.167700,3.039573,-8.951508,-7.677703,-6.828165,-5.306000,-6.620126,2.258781,9.310753,-3.222414,-3.592994,-7.755473,-0.151899,-0.785635,1.806250,7.332345,-9.028578,0.104803,8.468978,5.159445,8.113314,-5.788933,4.629155],[-3.524632,0.341614,6.717113,-6.141714,-4.790396,9.896635,1.588895,-8.921419,-5.978032,1.611896,-9.138744,5.169121,-0.132175,1.823060,9.893368,7.942199,2.029183,-8.893234,-4.720684,-1.185786,8.062497,8.118550,0.979448,3.700093,-2.714961,7.045498,-8.997989,0.269498,-3.365819,3.123636,7.694103,8.620959,1.533427,4.220641,-4.482808,8.464806,-9.412151,-8.278000,-6.398970,3.771099,-2.301495,8.136780,4.083016,-4.228935,-7.287775,7.815710,-3.388117,-8.261958,-8.644901,9.457037,-6.474125,8.083816,2.720242,-4.649847,3.231509,4.769265,-4.517583,-4.653167,7.864949,2.796160],[-0.320845,7.655916,8.435571,3.866488,7.854745,-0.686546,0.862192,-1.775904,9.032914,-0.389312,-7.965043,6.512926,7.462684,7.663302,-0.184485,-1.555584,6.493069,2.645991,7.755171,5.026766,6.537346,-7.348379,6.340429,6.317676,1.227603,7.537890,5.829654,6.957551,9.769093,3.141265,5.131947,-5.607485,4.226969,-4.368069,-1.003448,-1.534925,3.819250,-4.634265,5.947694,-4.657889,-0.233686,7.427461,-1.151909,-7.003885,9.903055,1.796395,4.366023,1.401995,7.830384,6.268370,2.891971,3.931190,5.610926,4.083950,8.301831,9.616071,-2.528807,-4.804574,5.208438,-6.796077],[-2.957204,-7.611371,3.074182,4.056822,4.294953,4.874506,-3.794431,7.043470,-7.236356,-7.015960,-6.909763,2.029586,-5.452748,7.372035,-3.916016,-4.693518,4.703413,-4.765621,4.345011,3.827078,2.105625,8.225179,2.873113,2.044657,-2.378559,-6.221980,1.923896,4.966436,2.228328,-7.806945,-7.786218,-3.108227,2.089268,-1.177667,-0.164754,6.038990,-8.702576,5.235405,1.601261,-6.296380,8.637111,4.957365,-0.463940,-7.351266,6.322406,-3.340127,-9.269294,-5.208495,2.650392,-4.349487,-4.904957,3.289062,-5.881881,7.577262,1.992965,5.970668,-9.182427,-4.501439,3.194441,-6.412260],[5.359220,-7.799682,1.491161,4.523769,-4.615295,7.992240,6.128617,5.245494,0.124401,4.385459,-4.818654,8.084980,6.615508,-1.418460,6.420049,-5.013669,3.227926,-0.969407,2.726016,2.144890,3.662958,-2.392232,-1.697760,-9.317219,-9.903768,-6.182657,4.607038,7.529292,5.217946,8.219730,-3.828438,8.252316,8.201780,5.329058,0.040544,-0.625873,7.343159,7.398089,-1.405466,4.462953,-3.134422,-1.008229,-0.908170,-3.822392,2.048616,-8.073440,3.642119,3.373157,4.966282,1.460402,9.917495,1.332593,2.936696,-7.834664,-4.748695,-0.189751,-1.722220,-6.364509,5.945101,-5.985147],[5.600616,-2.146180,0.570754,3.978156,-2.622618,3.205942,-6.724781,-2.660863,-6.946239,3.464986,4.008106,4.699693,-2.534810,-2.027808,-5.106606,-0.081352,2.025347,7.675248,-0.257684,6.786585,6.188044,6.708736,9.218714,3.117904,-3.117007,-3.709672,4.908879,8.053461,-5.968668,1.003928,7.904856,-4.561074,-0.245272,7.419884,-2.027939,-7.690291,3.218264,7.410434,6.983618,-3.191465,2.696183,3.306345,-3.777578,2.598873,-0.163139,-2.373871,-2.412478,-7.077860,-6.476573,-2.525563,-8.049822,-5.943973,-6.392197,-7.016086,3.298501,2.158181,-3.293464,9.876262,-2.204480,2.354909],[1.557321,-7.937501,-6.467856,-9.057923,-0.945801,0.297892,8.296515,-7.491247,0.320562,-7.475208,-8.461936,3.927460,-1.763543,1.210366,1.005618,-8.628215,-9.270409,9.873839,9.487920,3.160544,-8.394754,9.365448,9.602012,0.788557,-2.034900,4.205852,3.256510,3.123808,1.011922,-7.696079,8.179145,1.592673,9.229300,-5.566505,-0.497661,-9.778601,-3.784855,7.771296,-3.408138,-1.170620,-2.238357,9.217662,2.155934,1.987576,8.900262,7.392333,-4.532436,7.972136,1.868067,7.314124,2.816713,-4.502275,4.990819,3.046933,-7.483539,-6.080138,9.969945,1.836948,1.235273,1.140104],[-5.606530,8.207207,4.896989,1.556276,0.157346,7.294610,-4.578435,-8.141315,0.058006,3.097630,-8.710827,-1.032770,2.499236,-0.331301,-6.823803,-3.076868,-4.299829,-2.514020,-3.864305,7.034573,-3.784692,-2.251113,-7.406752,-2.218179,7.865692,-5.951730,3.394964,6.572674,-3.693136,5.358865,-2.238067,4.806864,-1.815465,-4.624338,0.660688,-4.175118,-9.324235,9.818239,2.292621,-5.586154,8.760203,-3.427618,1.255975,-4.257049,6.053848,6.950306,6.515140,5.689169,-9.224052,-0.539445,7.029856,3.790663,2.079455,-4.918325,-0.531757,3.330799,5.763282,-4.306569,-7.547218,-0.384163],[8.513020,7.788865,6.847632,-2.009999,-0.959811,2.330829,7.141166,-6.406085,6.919849,4.869997,1.589492,-5.965663,3.613304,-9.273054,5.499002,4.701490,-7.498840,2.485458,4.011348,3.200547,-0.710879,1.671617,9.778950,-5.687964,2.054893,-0.629164,8.808897,4.758228,9.100054,-9.284589,2.266944,0.873800,-7.582496,3.463552,-0.541269,1.475362,9.318589,-1.232341,-9.848223,-1.016527,5.405815,9.506527,4.642483,1.253090,-9.529155,8.452491,5.573397,2.204170,7.217317,-6.255848,1.259251,-0.542688,-3.862753,0.418546,8.315836,-8.130167,-2.479411,2.055665,0.856205,-8.846832],[-9.993374,0.869302,9.694352,5.347736,7.252496,-8.421045,-6.849242,2.794495,-7.380026,9.966860,-8.666479,-6.610136,6.602873,-0.374365,-8.945479,-3.866095,-6.372723,-0.392676,-6.679830,-9.087586,0.114057,-0.831884,1.947513,2.110137,-8.317023,-9.886004,-9.343001,2.816662,-4.771695,-3.398388,9.018418,-1.298756,-0.192802,1.118732,-9.078406,-5.731560,-3.662151,4.839433,4.978415,2.245707,-6.333231,-0.289915,-1.194408,-0.803779,-2.392706,7.170104,-1.737278,8.807111,2.762631,0.181837,7.787954,1.718692,0.395569,3.096770,9.734862,-9.821749,-9.368973,1.553423,7.411551,-4.192375],[-3.982145,1.355362,7.438182,-6.567617,5.551425,-3.387562,0.430075,-7.284593,5.266121,6.613604,9.514648,-0.357687,0.048471,-0.903737,8.374661,-5.942899,9.130320,-3.666147,-7.238807,4.466049,0.853438,-3.696902,5.731032,5.561086,6.181130,-6.498219,-4.074606,-9.958081,-7.725947,-0.954633,3.955303,3.494404,-0.990600,2.712002,-3.176938,-7.493872,7.908314,8.027768,-9.925547,9.953849,8.133573,-0.335704,-0.768318,4.413182,1.650041,-8.951257,-4.082774,6.478917,-6.087590,-2.386196,1.817540,-2.766601,9.594898,-2.137123,-3.688610,5.068032,7.209479,2.338384,5.198355,-2.411854],[6.873231,4.800789,-8.002806,-7.327262,-3.879846,-1.101424,-1.872441,-4.070246,-4.539594,8.606579,-0.388015,-5.073817,-8.869094,7.694048,1.225011,-1.959428,-6.285076,-1.048413,6.630171,9.245598,4.032419,2.121285,-0.847104,-9.189555,-9.272649,4.696903,-7.188551,-2.669888,-3.546143,-4.971912,6.195687,-7.518531,6.016249,4.278191,2.190234,-8.534390,-9.642503,-9.970479,9.601260,9.635284,-0.862680,-0.044565,-3.495440,6.658894,-8.889123,-6.853912,9.676597,5.735744,-8.048554,1.217828,-9.308839,-0.438564,4.580475,3.482421,8.575821,0.379651,-0.667473,3.824223,-3.562271,2.422090],[-4.502652,6.058350,-5.330915,-3.567219,8.112704,-3.174012,2.865611,-4.650352,-6.586446,0.656203,-0.684288,2.113182,-4.790073,9.288618,-7.244058,1.521280,4.318846,-1.053486,-6.869076,-5.748888,-7.017752,4.890287,9.859325,-0.753832,6.738911,-9.119816,-9.930741,-9.706476,-6.814252,-6.401603,-3.571033,6.217329,-8.228023,5.778051,6.485782,-1.000103,6.595422,7.719251,0.673985,-1.329964,-3.274914,-2.041606,-0.672317,9.900769,-8.422268,5.631151,-4.453848,-6.562166,-3.557601,8.924389,6.970159,7.317378,6.263619,-1.884389,9.301772,7.606653,5.418913,-1.435524,9.936274,-8.701244],[8.790104,-4.894270,-1.344505,-2.459495,9.943995,-4.589031,8.058107,7.019997,0.478090,3.067642,-5.749952,-4.334389,-1.111166,2.992822,-5.690481,-7.532390,-9.511709,6.717674,2.009879,2.853879,2.637353,-2.907220,-6.445850,3.237130,5.886431,-4.194139,-7.835242,6.023487,5.468618,-9.484428,-4.469316,-7.544616,0.666670,8.597458,3.018883,9.526732,7.767850,-9.977182,8.785920,6.748536,-2.394144,-4.007145,-8.826798,-2.107876,7.542066,2.200581,6.676085,-5.771473,-1.204051,6.419312,-8.152694,-6.208293,-2.497658,1.915464,8.569205,-6.387402,-5.641902,-8.250419,-2.803345,5.729833],[7.652756,2.015231,-8.430888,2.966575,-1.158696,-9.410008,-4.597768,-5.363090,0.864131,-2.017252,-2.866476,4.126712,-2.066583,0.224777,-8.833404,-0.746968,1.103727,-7.214085,5.411029,-7.854768,-8.143349,-3.060465,-6.289628,-9.996841,4.367981,-6.288632,6.411614,-3.370917,0.496764,3.345309,-7.428617,0.077672,8.504413,6.234984,6.074069,-4.358946,0.808439,-2.515177,9.087490,2.610972,-5.481291,-0.397498,9.489866,9.985526,-7.160432,-8.911790,-2.073587,9.828689,6.078306,-2.292832,-5.718646,1.173541,9.775599,2.984002,-5.477072,0.005272,-3.692449,-7.335456,4.573230,-8.049604],[-5.290789,-4.271706,-9.615633,4.967004,4.740796,1.122480,-3.230915,2.106182,-3.787147,2.605444,6.098340,3.418869,-6.455484,-2.122048,3.547215,-9.649277,7.366549,-4.731414,-7.592486,-7.939353,9.158282,6.079299,-8.919127,-5.637276,-0.017637,2.518624,-6.202501,8.707736,-8.426505,-9.711318,5.181787,-9.868310,-6.795723,-2.432317,-9.524616,-3.039882,-7.647994,5.151026,-5.437358,-4.808843,3.649124,-2.588228,-9.042198,3.135556,6.049954,3.804040,-2.168393,-0.361764,-1.349190,0.173546,5.141978,4.714721,0.796365,-2.404171,-3.483019,-1.273857,-9.901749,1.713878,8.760137,8.417496],[9.392920,8.475366,-7.389422,-8.831942,-1.128591,1.827732,8.298194,-3.726789,-2.550039,-0.713945,9.136544,-6.016484,0.816277,-4.891886,-9.898001,-6.853066,-6.346279,1.652062,6.307817,-4.518259,2.200019,9.874541,-0.601515,-9.466967,-8.785866,8.903732,6.023126,4.601916,0.365851,4.651643,9.640430,3.671069,2.900304,0.701484,-9.100850,0.795275,4.990552,-9.331931,-1.061060,-2.337182,4.608903,-5.622063,-4.077814,-7.036330,0.557112,7.552133,3.512059,5.956794,-4.653107,4.086791,-7.271961,-4.504512,7.880693,6.369829,0.583794,-7.038787,4.294145,-9.280128,-6.228776,0.572606],[-3.276520,-9.094336,-6.843490,5.575026,-6.677662,1.550990,1.456098,1.195946,3.669747,-2.869991,-8.515117,3.793076,5.070142,1.798760,-8.993959,3.008648,-7.664011,-1.135202,4.774534,7.419111,-3.306532,-2.855896,-7.155864,-7.624702,-9.306317,8.352145,7.727953,-4.219370,-1.592675,-8.732119,0.819240,0.813697,-1.757957,-4.113346,2.840882,1.857464,-5.721923,2.244536,7.483426,-1.543300,-5.258461,9.234622,9.249016,-5.660783,9.951594,-6.626171,1.275971,-3.747143,-5.027949,3.060878,-0.651786,7.836416,7.649713,-3.766313,9.083020,-1.979723,-2.587501,7.147933,-4.345579,9.375673],[5.137550,-1.865154,8.440591,-8.822748,6.341584,-5.276848,-5.421734,-8.214455,-7.732802,8.399796,-0.337899,-2.989822,3.806252,-5.874974,1.323866,8.659472,3.029663,8.858173,3.465290,-1.480755,-9.589690,-4.217266,8.002297,-6.104029,7.077990,2.540657,0.685643,-3.589718,9.547151,-0.579866,-5.680896,7.359498,3.595571,1.306020,-3.662520,5.729592,-9.729137,-3.421810,1.539655,0.739981,-9.613971,-1.099079,-1.731211,-4.797486,2.838652,0.354413,-3.849534,9.646174,8.849523,-4.395773,6.467234,-5.247330,-9.386665,1.286207,6.363722,-8.528139,0.565493,-7.781790,-0.010974,2.751652],[7.169475,1.965995,-0.712033,-1.116732,7.567000,5.019788,-1.790831,-3.571423,-5.825844,-6.839935,6.519655,6.404122,1.351867,-6.128384,-6.391544,0.813830,-4.778632,-6.015993,-6.134172,9.430420,6.325861,-3.010979,-3.262275,-3.914505,-5.280539,3.672331,-4.594061,-2.784241,-2.757589,8.174833,-4.640758,-4.092477,0.867051,5.297033,4.841323,-5.264746,-1.662353,2.689545,8.615720,1.182282,-4.340441,3.994122,-6.879737,6.197783,4.165233,6.919441,5.968854,-7.768619,-2.221861,-9.357728,-4.450651,8.427576,5.651918,-8.724182,-7.314087,-1.935815,-6.908718,0.434530,0.691037,8.380911],[8.543544,4.528794,-8.575760,-9.803825,9.995585,0.472853,0.289937,-0.134061,2.711583,5.205911,3.477207,-3.953328,-4.921956,-0.623484,-3.423118,-2.131924,-7.580955,4.098918,8.641944,-1.267207,-0.388925,3.982712,-1.741717,5.829024,-6.839597,8.911876,-9.278742,8.116925,-1.495133,1.770364,8.001712,-5.361160,3.861797,-7.878884,8.126777,7.653574,-6.309837,7.113551,4.376551,-4.133521,-8.686955,5.767674,-4.566532,2.581803,-1.987883,7.790822,-2.192180,1.751151,8.539652,-1.242139,-8.082144,6.797155,-5.864317,5.040734,1.317834,8.997464,-8.277993,-3.171943,2.988975,0.158756],[-0.411568,1.237251,-2.478790,-7.758762,9.878372,5.029202,2.586837,-5.610097,1.228388,4.459743,-1.133428,-8.647761,9.947280,3.717581,-6.128340,-6.072751,8.906436,5.660763,-3.339505,-1.983227,5.707206,-4.747850,-7.017045,-3.614407,-6.488354,-4.290703,9.194014,1.359468,4.137408,7.936826,5.176224,1.503759,-7.685157,0.988294,-4.912733,-0.789429,3.668297,-1.669983,5.767799,5.975566,-7.652169,-8.813887,8.465686,-3.872605,-5.750867,-1.863242,6.450623,2.091680,9.690059,6.421671,-1.137902,7.130967,-7.250076,5.894195,-1.524754,3.899306,-2.901616,-7.672013,-6.721646,-1.312052],[4.929886,-2.706808,-2.013151,-1.747516,-9.355369,-6.906336,0.641052,-2.780296,4.810825,3.323816,7.278002,7.585028,0.063845,5.775605,-2.225036,-4.896915,-2.052084,0.713863,-5.151998,-9.670849,3.935477,9.881418,-0.365600,-5.675217,1.217952,-8.291922,-8.562882,-4.879114,3.569120,6.664146,-0.505670,3.815211,7.317261,2.697828,-0.420120,-4.266778,-2.264989,-1.873132,-1.210416,5.429683,6.691105,-2.992207,6.847582,9.886757,-6.156717,-5.793903,-7.038488,1.742115,-4.397492,-9.567430,3.348142,-0.653451,-2.810974,-6.886226,7.158630,5.593668,7.071106,1.329843,-5.769357,-8.039124],[2.383947,9.263708,-4.519273,9.477696,-6.946519,-1.707319,1.788883,5.574236,9.759024,-9.118810,3.535388,7.407418,1.554405,9.789435,1.583495,-3.783277,7.290118,3.530067,-1.818582,-3.882129,-4.699277,-5.179528,-5.274285,6.541064,-3.248546,-8.902063,0.963550,-2.797105,-1.624414,0.809919,8.109147,9.238122,0.613576,9.587268,1.406110,-8.026156,-2.582790,3.098310,3.598147,-6.524686,-4.959911,6.599502,2.316305,-5.314498,-8.452593,4.980478,4.889351,-8.733489,8.895108,6.722941,1.964316,-4.596682,-2.229920,-7.162208,3.869683,4.396439,-9.481543,5.363344,3.849508,2.048732],[7.849528,0.580504,9.465210,-8.046400,2.836601,-1.331086,0.436084,-1.183640,-4.348154,6.065229,-3.749574,-0.905343,-3.753956,-5.416584,9.038660,5.487693,-5.890482,-5.822485,-2.445980,4.908326,-2.920703,-9.315072,-9.076303,8.211039,-8.522813,-0.472418,-6.614040,3.209909,3.052967,-2.993876,5.959881,8.037810,-0.688196,-1.233202,-1.795995,1.774358,7.401787,8.257616,-3.452850,-8.939820,0.760794,7.235482,9.703097,-9.449489,-8.051726,-3.416736,-4.942103,-5.558981,1.720169,2.430558,-9.850852,-6.326111,2.692984,5.906841,-2.277466,-0.033103,2.438291,6.099766,-4.143808,2.682398],[-0.940413,-5.324032,3.793657,-7.141396,0.441317,6.244523,-6.972035,5.519089,7.469739,0.644271,5.893085,5.833279,-0.417067,1.728530,6.501506,5.964788,-9.195210,-2.602704,-8.950516,-7.772046,7.749755,9.387540,0.921715,7.102834,-6.174499,2.029341,-6.687629,-0.780602,6.706712,5.542260,-3.488573,5.687543,-5.329034,-3.313075,-0.788735,3.265055,-9.159747,3.877204,3.317201,-9.334249,3.375750,8.343223,9.267261,-6.042411,-2.815679,2.549641,8.450092,7.386054,-4.166402,-5.253558,7.880844,-1.934873,5.899295,7.780070,-6.953079,-4.567155,9.265416,1.469546,0.055108,-1.201249],[0.445030,-3.524555,-6.764653,2.557498,9.250561,1.761665,9.673240,4.413954,6.636910,5.780380,-7.634361,0.279024,-0.613033,-3.917019,8.321560,1.835486,-3.180430,0.477129,6.171886,-5.845946,-7.365017,0.158417,7.886558,-9.908076,-8.122121,6.236883,4.318679,-7.043094,3.016134,6.712818,9.391166,-4.709520,-0.758008,-0.435127,-3.409914,7.634649,-8.799568,-6.006925,2.708226,-1.923878,-0.301776,-1.589891,9.013002,5.316600,-8.218926,6.078725,2.103518,6.068445,1.865390,-7.634281,-0.093090,-1.838167,-3.194131,7.875306,-9.378983,5.178069,6.026225,-2.260006,4.330421,7.150430],[7.273545,0.807235,-9.395851,-8.016007,6.382066,7.974762,-4.857542,-1.782984,-2.338687,-9.623939,-9.579963,-1.383121,-4.608120,-4.370485,-0.220972,9.984927,-2.010105,6.381946,9.621525,-6.517181,-0.329834,2.124462,1.921227,8.553066,6.225885,-4.425567,-4.281020,5.351283,-7.501889,-2.312883,3.867562,-9.934236,-6.544816,7.582793,8.280343,-5.464056,9.603650,2.846924,-5.175920,3.372008,-1.135308,2.211608,-6.266806,6.947153,-5.289047,2.872651,7.307006,8.365970,5.571447,-4.107556,-0.273901,-3.251116,-7.875072,-9.934082,4.544355,-4.355660,-2.185210,-4.776260,-6.186964,6.173644],[3.913199,-8.424497,-6.272347,-2.014261,-7.096556,-7.990162,-4.738211,2.950992,-6.442640,6.083294,5.201337,-7.779795,9.761847,-6.220561,-0.541111,-0.896189,-8.916562,2.589395,-3.504652,8.554861,-2.908751,8.342619,-2.670816,9.198639,-3.225483,-9.128470,-4.443649,3.555947,6.844802,4.766849,6.301992,7.313372,-9.115961,-9.329678,1.523221,-8.551567,-1.022264,-8.672465,-7.031971,2.846543,-3.570149,-3.903618,-2.186988,-3.767210,9.014891,-1.121992,9.479865,-0.012732,-1.812405,-6.547231,-6.250129,7.599989,-6.166599,-8.714780,6.207718,4.626603,5.394993,-9.893920,-9.868133,-3.863339]], dtype = "float32")#candidate|8824|(48, 60)|const|float32
bop_8825 = relay.add(call_8819.astype('int32'), relay.reshape(const_8824.astype('int32'), relay.shape_of(call_8819))) # shape=(48, 60)
bop_8828 = relay.add(call_8820.astype('int32'), relay.reshape(const_8824.astype('int32'), relay.shape_of(call_8820))) # shape=(48, 60)
var_8837 = relay.var("var_8837", dtype = "float32", shape = (48, 60))#candidate|8837|(48, 60)|var|float32
bop_8838 = relay.power(const_8824.astype('float64'), relay.reshape(var_8837.astype('float64'), relay.shape_of(const_8824))) # shape=(48, 60)
output = relay.Tuple([call_8757,bop_8825,bop_8838,])
output2 = relay.Tuple([call_8758,bop_8828,bop_8838,])
F = relay.Function([var_8837,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8837,], output2)
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
