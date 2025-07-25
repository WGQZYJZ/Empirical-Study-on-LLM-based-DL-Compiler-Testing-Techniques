import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_300 = relay.var("var_300", dtype = "int8", shape = (8, 14, 1))#candidate|300|(8, 14, 1)|var|int8
var_301 = relay.var("var_301", dtype = "int8", shape = (8, 14, 10))#candidate|301|(8, 14, 10)|var|int8
bop_302 = relay.bitwise_xor(var_300.astype('int8'), var_301.astype('int8')) # shape=(8, 14, 10)
output = bop_302
output2 = bop_302
func_307 = relay.Function([var_300,var_301,], output)
mod['func_307'] = func_307
mod = relay.transform.InferType()(mod)
var_308 = relay.var("var_308", dtype = "int8", shape = (8, 14, 1))#candidate|308|(8, 14, 1)|var|int8
var_309 = relay.var("var_309", dtype = "int8", shape = (8, 14, 10))#candidate|309|(8, 14, 10)|var|int8
output = func_307(var_308,var_309,)
func_310 = relay.Function([var_308,var_309,], output)
mutated_mod['func_310'] = func_310
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1245 = relay.var("var_1245", dtype = "float32", shape = (6, 13, 4))#candidate|1245|(6, 13, 4)|var|float32
uop_1246 = relay.tan(var_1245.astype('float32')) # shape=(6, 13, 4)
uop_1250 = relay.log10(var_1245.astype('float32')) # shape=(6, 13, 4)
bop_1252 = relay.power(uop_1246.astype('float32'), relay.reshape(uop_1250.astype('float32'), relay.shape_of(uop_1246))) # shape=(6, 13, 4)
output = relay.Tuple([bop_1252,])
output2 = relay.Tuple([bop_1252,])
func_1258 = relay.Function([var_1245,], output)
mod['func_1258'] = func_1258
mod = relay.transform.InferType()(mod)
mutated_mod['func_1258'] = func_1258
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1259 = relay.var("var_1259", dtype = "float32", shape = (6, 13, 4))#candidate|1259|(6, 13, 4)|var|float32
func_1258_call = mutated_mod.get_global_var('func_1258')
call_1260 = func_1258_call(var_1259)
output = call_1260
func_1261 = relay.Function([var_1259], output)
mutated_mod['func_1261'] = func_1261
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1453 = relay.const([[[-7,8,1,7,-1,4,8,4,-3,-1,-4,2,9,-10,-7,7],[-7,-8,-6,2,5,-7,3,3,6,7,-8,-5,-5,10,-1,-6],[1,-1,-10,4,6,8,-7,-7,6,4,-3,3,-3,-9,-1,5],[10,-8,-8,6,8,-7,-7,-9,-10,-9,3,2,4,-10,-8,-6],[4,1,-8,8,-2,-2,-1,2,-3,4,-2,2,10,10,1,-6],[-1,7,-3,7,1,-4,10,4,6,1,-4,3,-9,2,10,4],[-5,1,5,-3,9,1,-3,5,2,-5,-3,2,3,1,-2,-3],[4,-6,3,-9,7,2,-2,-9,-4,-3,-5,8,-7,-9,2,7],[-9,-8,10,-3,-7,7,3,-4,-10,-4,1,3,9,-8,-8,-10],[6,7,7,-5,6,-4,9,6,6,-6,-9,5,-3,-2,8,7],[-2,-1,6,-3,-9,-3,-6,2,8,1,7,9,10,2,-5,-3]],[[-5,4,-10,6,-6,2,10,6,-9,9,-4,9,-10,-4,-10,-10],[1,6,2,3,-5,-2,6,-4,6,5,10,5,-5,-6,6,-1],[3,8,-1,5,-5,-10,-4,6,-6,9,-4,-9,-5,-5,-3,10],[6,-1,-9,5,-1,5,-9,-5,-3,-4,-1,6,-8,-7,-7,-4],[4,-2,-2,-9,9,-10,6,-5,2,-5,-10,8,-4,-8,-3,6],[10,4,-2,-6,-6,1,-2,10,6,6,8,6,1,3,-6,3],[6,7,8,-10,10,6,-10,7,-4,1,-8,-4,-1,-3,7,-3],[3,2,3,-6,5,-6,-2,10,7,8,8,-4,-8,-8,-5,9],[-2,9,-4,10,-1,-6,-7,-7,-10,10,6,9,-5,8,-7,-9],[-7,-6,-5,2,-1,7,7,-4,10,6,-2,-1,-9,8,-5,7],[-7,-6,-7,6,-9,8,10,4,8,5,5,8,4,-2,-2,4]],[[-1,-2,9,6,3,-5,-8,3,8,-7,-4,9,-2,1,-1,5],[-5,8,-5,3,2,10,-8,-7,1,-1,10,6,-2,-6,-2,-3],[-6,-3,9,8,6,1,-3,10,4,-10,1,4,3,-6,-1,-5],[4,-9,-6,4,8,-5,4,2,7,2,-10,-1,8,-9,8,9],[4,5,-6,-1,4,3,1,8,9,-6,-8,-1,6,-7,-6,6],[-4,-9,2,5,7,-6,5,-8,5,5,-3,-2,-8,5,7,5],[6,4,-5,-4,6,1,-7,8,-3,7,-9,8,10,-5,-7,-8],[4,1,-10,-4,-8,-8,3,6,8,5,2,7,7,9,-2,-8],[-1,-8,7,-7,-6,-9,2,-9,9,-8,-5,5,8,-7,2,-9],[-6,2,-8,8,6,6,-5,8,7,4,-2,-4,-2,-1,8,-7],[-6,8,2,1,-5,3,10,-3,9,10,6,-2,-7,-7,4,9]],[[-7,-5,5,4,-2,10,-10,10,-10,-3,-6,-9,9,-8,-1,2],[-4,-4,2,6,7,-8,9,-8,-10,-7,5,9,-3,-6,4,10],[-4,4,4,-2,8,-10,7,7,-9,4,-2,8,2,10,2,3],[-6,-6,8,3,-7,4,3,1,-8,5,-2,7,-7,-1,9,-6],[2,5,-9,8,3,10,-3,-7,-8,5,5,5,1,10,-1,-4],[10,2,10,-5,-2,-9,6,10,-8,7,6,-3,9,6,-4,2],[2,5,-6,4,-5,-6,9,-6,-10,-8,4,-5,9,-4,4,8],[2,5,-2,-7,-2,-8,7,-7,9,-5,-9,8,4,2,6,1],[1,-7,6,2,4,-2,5,10,-7,5,-5,-5,-4,6,-4,9],[4,-8,7,2,-9,-4,2,-6,-1,4,-5,7,-3,-9,-2,2],[-2,8,-2,3,-3,-6,5,5,-7,3,9,1,-5,-10,-1,-10]]], dtype = "int32")#candidate|1453|(4, 11, 16)|const|int32
const_1454 = relay.const([[[-10,8,-8,-1,-7,-2,-2,8,-2,1,1,-7,-2,4,3,-1],[1,-2,-8,7,-1,-6,9,4,-2,-5,6,-7,-6,-4,9,4],[5,-10,9,6,10,5,-3,1,4,10,1,-2,-8,-7,-2,-8],[-9,9,8,9,9,-7,3,-10,7,8,-7,4,7,-4,-4,-7],[3,-10,1,-8,3,3,-5,-2,-2,10,-3,7,-8,10,-7,5],[-2,10,-6,6,-6,-7,3,-3,2,-6,-8,6,6,-7,4,3],[-9,-1,-3,-4,7,2,-3,-7,-8,1,-6,1,-2,6,-10,-1],[-4,-2,1,-10,9,8,-8,-8,-8,4,5,-9,-4,4,4,3],[-10,-6,2,1,9,5,6,4,2,9,5,-6,-3,-3,6,6],[10,10,10,-7,-1,-6,8,3,8,-7,10,-2,-4,1,-2,9],[-8,5,-10,-9,-7,-10,-5,-4,4,7,-7,-8,-5,-2,-3,8]],[[9,3,8,-10,5,9,-2,-2,-6,-2,-8,-5,-9,-10,1,-6],[-3,-10,1,3,2,5,-7,-10,-5,-8,-3,8,4,-6,7,-5],[-1,1,-9,-7,8,-4,-8,-10,9,8,4,5,7,3,3,4],[3,7,2,2,5,-7,-2,-8,6,4,5,8,-1,3,8,-2],[-7,-2,3,2,-2,1,-7,-3,-6,-5,-6,-2,-3,-5,-4,-2],[3,1,10,4,-2,3,5,-4,-5,-3,-1,10,-9,5,-9,6],[10,8,3,-1,-8,-6,-2,-3,1,-10,10,-8,-6,-4,-9,8],[2,-1,-9,-9,9,-7,6,-10,7,-1,9,-8,2,1,-6,3],[5,2,8,-9,7,-8,8,-3,-7,6,4,2,-9,9,9,3],[8,8,-9,3,-4,2,-10,-9,-7,-4,8,-9,8,-2,2,5],[-3,5,9,-9,-10,7,3,-6,10,5,5,-6,-2,4,-4,-3]],[[1,10,-8,4,-9,6,6,6,2,-5,5,-2,10,2,-4,-2],[5,-6,2,-8,3,-4,-8,7,2,-6,5,-6,7,-8,3,7],[-3,-10,5,5,4,8,-10,1,-9,10,9,9,-2,-7,9,2],[9,7,9,-3,-1,-6,-8,-4,-6,-2,-10,10,-8,-6,3,8],[-1,-5,5,5,8,9,-8,2,-7,8,-5,-9,5,7,5,-9],[10,-9,1,3,5,5,4,9,4,-9,8,-10,-5,-3,4,-9],[6,-9,1,-8,5,4,-3,-3,2,3,-9,-3,2,7,7,-10],[1,2,3,-10,3,8,-7,-10,2,-9,6,7,9,6,7,1],[-7,-2,2,1,-8,-9,9,-5,5,-5,-7,1,-6,6,-2,5],[-9,-10,-1,-6,1,5,7,2,-4,-2,-9,9,-9,1,1,1],[-3,2,-3,4,-4,-3,-6,2,1,-1,5,8,-6,-5,6,-8]],[[6,-4,10,10,-4,-6,7,-10,-10,-3,-2,10,1,-6,1,8],[6,4,-2,4,9,-8,-6,7,1,2,10,-5,7,-1,-5,-6],[3,-1,-6,10,-4,4,-9,7,-10,5,-3,2,-2,-10,4,-10],[-8,1,-5,-1,-9,9,5,-8,-7,6,3,-1,3,-4,7,-1],[6,-1,2,1,7,9,-8,-7,-2,-4,-3,10,8,10,-7,-2],[-4,5,5,7,-6,3,5,-8,3,2,6,-1,-7,2,5,-8],[-7,4,8,3,2,-7,-6,-2,6,-4,-7,9,-7,7,-4,-10],[7,-10,-9,-1,9,-8,3,-3,-5,1,3,5,10,-3,-6,-3],[8,9,8,-10,8,-9,7,7,-8,-3,10,-2,-9,-5,7,9],[-3,5,-8,8,1,6,1,2,-6,2,-5,8,-9,-1,3,2],[-10,-9,9,4,-7,10,8,7,8,-9,4,-7,10,-9,-9,9]]], dtype = "int32")#candidate|1454|(4, 11, 16)|const|int32
bop_1455 = relay.multiply(const_1453.astype('int32'), relay.reshape(const_1454.astype('int32'), relay.shape_of(const_1453))) # shape=(4, 11, 16)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
const_1463 = relay.const([3.016952,1.495821,5.702949,3.211783,1.580571,-3.294139,-2.029716,-5.272099,-4.663502,-2.488270,-2.167199,-5.228144,-2.671070,3.822059,-8.099652,3.667302,4.842131,0.766903,8.453673,-7.174425,-1.506332,-4.018157,1.131940,6.068968,-9.735585,8.838723,8.463885,7.898962,3.113481,4.114957,3.619342,5.322277,9.238656,2.498617,-2.746106,-3.341999,-9.799569,6.316104,5.096133,-7.003497,-4.252412,-4.873454,5.228357,-4.437082,1.579925,-1.271503,-8.689667,6.547536,-9.546196,-7.444062,-8.728182,4.497879,8.578361,-9.880057,6.500136,-3.355040,-5.446426,-4.800782,8.600592,6.829505,-1.713514,9.174936,6.757432,9.265685,-3.096950,-1.772803,-9.897652,2.709614,7.992730,-5.963256,-3.106094,-8.650310,7.018595,-2.162788,4.899406,1.532622,-9.911828,-7.995152,5.349616,1.784301,1.819747,1.412504,-0.927283,-5.993217,-5.230016,-3.850324,2.684776,-0.060282,2.117266,3.699997,-3.426582,7.687520,-4.186359,-7.606050,4.597192,6.872409,-5.776405,-6.501788,5.464803,-1.850878,2.091888,4.178383,3.140342,6.720102,-2.547103,-0.283848,-4.309335,2.573458,3.532491,-2.730612,-5.705939,-2.329573,-1.371199,6.493018,0.929196,-8.534740,-1.188768,1.335565,2.348743,9.338837,-5.519263,-9.838356,3.649906,2.642816,6.385810,0.556334,7.527950,-3.590979,-6.824937,8.292849,2.061164,-9.418976,9.233284,-7.063755,-3.781924,8.544048,0.855046,8.838654,5.490693,1.867993,9.164484,-7.089958,-0.222528,-8.391348,-8.783405,-3.304621,7.682609,-0.464288,1.328366,6.512577,-2.073484,-6.157890,-0.167600,-5.829513,-3.997919,7.966081,-1.507712,-9.602993,-4.628833,2.237586,-0.602600,4.551246,-6.334237,0.412109,-8.814884,1.439857,4.299964,-0.753765,-2.284625,7.772510,-8.824605,-9.997526,3.512664,-5.044768,9.195061,-7.864816,2.935103,-6.364559,4.212301,6.597401,-9.786426,-6.411413,-6.045849,-7.405436,6.477663,6.205822,-7.536747,-5.537524,-4.067273,7.331360,-8.949904,-1.720877,5.489000,3.142343,-8.255264,-9.096496,-0.349458,-5.862156,9.935299,8.052704,-4.179249,5.087240,-4.851173,-6.508405,-2.218369,-6.353918,-1.698879,-9.257759,9.863660,-4.872657,4.557742,2.660849,-0.923802,-5.444207,-9.473080,-2.505880,3.882675,4.279784,-5.947097,-0.598258,0.938975,0.306936,0.185488,-5.312458,-0.960507,-9.522204,0.593835,7.877125,5.667281,-0.593120,3.357583,8.746493,-5.769712,-0.141588,-5.958288,5.920994,7.524682,2.671923,-5.529506,-6.163075,9.677660,-2.375758,-1.375525,-0.385001,-8.190767,5.683845,9.642080,-9.099354,8.709139,-5.433265,8.671495,1.349286,0.587372,-5.002052,-7.678457,-4.066063,8.814190,5.301477,-9.899487,-0.131989,-4.685415,-4.387362,-2.708105,0.303593,5.826277,3.564340,9.049471,1.498424,-3.275642,-2.728544,-6.765289,-6.315528,-1.399445,4.634481,5.670374,1.698067,6.063468,6.682435,-0.716859,2.651993,2.657999,-2.495333,-3.600865,8.130675,8.110674,0.253434,-4.101095,-9.873523,7.553397,3.442564,6.834335,-3.442531,-3.645900,-1.405844,-5.113318,-4.303345,-5.493584,-1.663356,-8.411240,0.444012,-9.526714,-9.411038,-6.748378,7.836125,-1.910544,-5.452337,4.509495,3.183060,6.989208,-0.735806,8.863469,3.110376], dtype = "float32")#candidate|1463|(312,)|const|float32
call_1462 = relay.TupleGetItem(func_1258_call(relay.reshape(const_1463.astype('float32'), [6, 13, 4])), 0)
call_1464 = relay.TupleGetItem(func_1261_call(relay.reshape(const_1463.astype('float32'), [6, 13, 4])), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_1468 = relay.TupleGetItem(func_1258_call(relay.reshape(call_1462.astype('float32'), [6, 13, 4])), 0)
call_1469 = relay.TupleGetItem(func_1261_call(relay.reshape(call_1462.astype('float32'), [6, 13, 4])), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_1476 = relay.TupleGetItem(func_1258_call(relay.reshape(call_1462.astype('float32'), [6, 13, 4])), 0)
call_1477 = relay.TupleGetItem(func_1261_call(relay.reshape(call_1462.astype('float32'), [6, 13, 4])), 0)
output = relay.Tuple([bop_1455,call_1462,const_1463,call_1468,call_1476,])
output2 = relay.Tuple([bop_1455,call_1464,const_1463,call_1469,call_1477,])
func_1488 = relay.Function([], output)
mod['func_1488'] = func_1488
mod = relay.transform.InferType()(mod)
mutated_mod['func_1488'] = func_1488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mutated_mod.get_global_var('func_1488')
call_1489 = func_1488_call()
output = call_1489
func_1490 = relay.Function([], output)
mutated_mod['func_1490'] = func_1490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1497 = relay.TupleGetItem(func_1488_call(), 0)
call_1498 = relay.TupleGetItem(func_1490_call(), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
var_1530 = relay.var("var_1530", dtype = "float32", shape = (1, 312))#candidate|1530|(1, 312)|var|float32
call_1529 = relay.TupleGetItem(func_1258_call(relay.reshape(var_1530.astype('float32'), [6, 13, 4])), 0)
call_1531 = relay.TupleGetItem(func_1261_call(relay.reshape(var_1530.astype('float32'), [6, 13, 4])), 0)
output = relay.Tuple([call_1497,call_1529,var_1530,])
output2 = relay.Tuple([call_1498,call_1531,var_1530,])
func_1535 = relay.Function([var_1530,], output)
mod['func_1535'] = func_1535
mod = relay.transform.InferType()(mod)
mutated_mod['func_1535'] = func_1535
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1536 = relay.var("var_1536", dtype = "float32", shape = (1, 312))#candidate|1536|(1, 312)|var|float32
func_1535_call = mutated_mod.get_global_var('func_1535')
call_1537 = func_1535_call(var_1536)
output = call_1537
func_1538 = relay.Function([var_1536], output)
mutated_mod['func_1538'] = func_1538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1549 = relay.TupleGetItem(func_1488_call(), 3)
call_1550 = relay.TupleGetItem(func_1490_call(), 3)
uop_1551 = relay.atan(call_1549.astype('float64')) # shape=(6, 13, 4)
uop_1553 = relay.atan(call_1550.astype('float64')) # shape=(6, 13, 4)
output = relay.Tuple([uop_1551,])
output2 = relay.Tuple([uop_1553,])
func_1556 = relay.Function([], output)
mod['func_1556'] = func_1556
mod = relay.transform.InferType()(mod)
output = func_1556()
func_1557 = relay.Function([], output)
mutated_mod['func_1557'] = func_1557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1578 = relay.TupleGetItem(func_1488_call(), 0)
call_1579 = relay.TupleGetItem(func_1490_call(), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
var_1585 = relay.var("var_1585", dtype = "float32", shape = (312, 1))#candidate|1585|(312, 1)|var|float32
call_1584 = relay.TupleGetItem(func_1535_call(relay.reshape(var_1585.astype('float32'), [1, 312])), 0)
call_1586 = relay.TupleGetItem(func_1538_call(relay.reshape(var_1585.astype('float32'), [1, 312])), 0)
output = relay.Tuple([call_1578,call_1584,var_1585,])
output2 = relay.Tuple([call_1579,call_1586,var_1585,])
func_1588 = relay.Function([var_1585,], output)
mod['func_1588'] = func_1588
mod = relay.transform.InferType()(mod)
var_1589 = relay.var("var_1589", dtype = "float32", shape = (312, 1))#candidate|1589|(312, 1)|var|float32
output = func_1588(var_1589)
func_1590 = relay.Function([var_1589], output)
mutated_mod['func_1590'] = func_1590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_1681 = relay.TupleGetItem(func_1556_call(), 0)
call_1682 = relay.TupleGetItem(func_1557_call(), 0)
var_1693 = relay.var("var_1693", dtype = "float64", shape = (6, 13, 4))#candidate|1693|(6, 13, 4)|var|float64
bop_1694 = relay.greater_equal(call_1681.astype('bool'), relay.reshape(var_1693.astype('bool'), relay.shape_of(call_1681))) # shape=(6, 13, 4)
bop_1697 = relay.greater_equal(call_1682.astype('bool'), relay.reshape(var_1693.astype('bool'), relay.shape_of(call_1682))) # shape=(6, 13, 4)
bop_1698 = relay.greater(bop_1694.astype('bool'), relay.reshape(var_1693.astype('bool'), relay.shape_of(bop_1694))) # shape=(6, 13, 4)
bop_1701 = relay.greater(bop_1697.astype('bool'), relay.reshape(var_1693.astype('bool'), relay.shape_of(bop_1697))) # shape=(6, 13, 4)
output = relay.Tuple([bop_1698,])
output2 = relay.Tuple([bop_1701,])
func_1706 = relay.Function([var_1693,], output)
mod['func_1706'] = func_1706
mod = relay.transform.InferType()(mod)
mutated_mod['func_1706'] = func_1706
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1707 = relay.var("var_1707", dtype = "float64", shape = (6, 13, 4))#candidate|1707|(6, 13, 4)|var|float64
func_1706_call = mutated_mod.get_global_var('func_1706')
call_1708 = func_1706_call(var_1707)
output = call_1708
func_1709 = relay.Function([var_1707], output)
mutated_mod['func_1709'] = func_1709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_1721 = relay.TupleGetItem(func_1488_call(), 4)
call_1722 = relay.TupleGetItem(func_1490_call(), 4)
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
const_1732 = relay.const([-9,10,10,-3,6,5,2,-6,-7,-6,-5,1,2,5,10,-8,8,-4,-5,-5,9,-8,7,-8,6,-3,-2,-8,-8,2,6,-6,9,3,7,6,7,-8,1,-1,9,5,-10,-6,8,6,-7,10,-2,-1,-10,4,-4,-4,-8,9,10,-1,-8,9,-6,-4,7,10,-5,-8,-1,-2,7,-7,2,-4,-1,-3,3,-9,-6,1,-6,-5,-3,6,9,8,-4,1,-2,-8,-2,-6,-2,-6,-9,-4,-10,-6,5,-9,-1,-8,-4,3,-6,1,-4,6,5,6,1,-8,2,5], dtype = "int8")#candidate|1732|(112,)|const|int8
const_1733 = relay.const([-10,3,-3,9,-2,-7,-4,3,6,-2,-1,4,-3,5,-4,4,-1,3,1,-10,-6,8,-7,-2,7,7,8,-7,-10,10,5,7,8,-9,-2,4,5,2,2,-7,1,-9,9,-1,-10,-4,-5,-2,3,-2,10,4,7,-7,1,8,-8,-10,-4,-8,10,-9,3,7,-3,-10,6,-6,2,-2,7,-5,-6,4,4,4,3,8,-7,3,-6,10,-9,-3,-2,-3,6,8,3,-3,5,10,3,6,-2,9,-2,-8,-7,-3,7,-10,6,-6,-1,5,-6,-3,-10,8,-6,8,6,-10,-8,-4,2,9,-5,8,-3,1,5,-10,-1,-9,-5,-6,4,8,2,8,-9,2,1,7,3,5,1,7,4,-10,4,4,3,-1,-3,9,-7,5,10,-3,-9,3,4,2,5,-8,8,-6,-3,6,-5,7,5,-1,3,10,-2,4,2,-3,9,-5,-3,-10,7,4,10,-5,3,-1,-9,2,3,-7,-5,-1,2,-3,-6,-5,8,4,-1,2,4,4,-2,5,4,2,4,6,-1,5,10,8,-7,6,1,4,9,1,4,-1,-9,10,6,1,2,3,-4,-2,5,-1,-3,-4,-2,-8,-2,-5,-9,6,10,5,1,-6,10,8,-3,4,3,-10,4,1,4,6,-2,1,8,-4,3,-6,7,10,2,-7,3,-9,-7,10,-6,-7,1,-2,5,9,-7,2,-10,5,-8,6,2,-6,-6,10,-5,2,-6,-6,-2,8,-10,3,-5,-4,1,-4,-5,-3,9,7,-2,-1,-5,9,1,-5,2,-3,-6,-1,6,3,-8,-6,-10,2,-2,-10,9,4,-1,-3,7,-1,10,4,-1,-9,1,-7,-8,5,-3,7,-6,-2,-10,-1,10,1,-6,-7,-2,-6,-2,6,-2,-10,-5,7,-7,-10,3,-3,-3,-2,-1,-8,5,-6,6,9,-2,-3,7,10,-6,-1,2,-1,-2,6,1,-4,7,-5,5,-1,4,-6,1,-5,6,7,3,3,-10,-7,-2,-7,-5,3,6,-9,-7,9,2,-8,-3,-6,-4,2,-7,-5,3,9,-4,-10,-4,1,5,-1,8,-5,6,-7,-8,4,-9,-6,1,-2,6,7,10,-5,-8,10,-8,6,6,-2,-4,2,5,8,3,-5,2,3,10,5,-2,3,-1,4,4,-2,4,2,3,-7,1,-7,4,3,6,1,6,-10,2,-2,9,5,-9,-3,8,-9,2,10,-4,9,4,9,-3,-4,-2,1,2,5,4,4,-9,-1,-8,8,-5,-3,-6,-8,3,4,-10,-7,3,-6,9,9,4,9,-10,-6,-6,5,-5,-1,-4,-2,-3,9,-10,-3,4,6,-1,-9,-4,7,6,-1,6,9,-8,6,-9,-9,7,-7,5,8,10,10,-2,5,-10,1,8,-8,1,2,-9,9,5,9,-1,8,4,-7,-7,-4,-9,-5,-3,5,-6,-3,8,-3,8,-2,8,-10,10,-7,-10,-3,6,-5,-10,-2,-7,-3,7,-7,7,5,9,-8,-5,-5,-7,-3,8,-3,-8,7,2,-2,4,-5,7,8,5,7,2,4,-2,-4,5,-1,4,10,-7,-6,-10,-4,3,4,-8,8,5,-9,7,9,1,-4,-9,-5,-5,-9,-4,-3,-5,-4,10,-10,2,-1,-3,10,2,10,-8,-8,-8,9,8,-8,9,-5,-4,5,4,-6,8,-10,-1,2,7,-4,6,6,5,8,-8,6,-8,9,-7,-9,-2,-7,-9,-2,-8,-1,2,-8,-3,-5,-9,-4,-2,-9,9,-5,-6,4,9,4,-4,4,4,5,10,10,-10,6,-1,-10,4,-1,-6,-6,3,-6,6,-5,2,10,9,-1,6,1,-4,-10,-6,7,-8,-9,-4,9,3,-2,1,6,2,1,3,-9,-2,-5,2,10,-8,10,-6,-4,3,3,-8,6,-4,-9,-8,6,-7,-8,-7,-8,1,-7,-9,5,8,5,-7,-7,-7,-10,7,7,-10,-3,-7,-10,-1,3,-9,-9,6,-3,5,4,6,-9,1,-7,10,6,2,-6,-4,-2,-7,9,5,6,2,3,5,9,7,7,-7,-5,-2,2,9,-10,-3,10,1,-9,8,-10,-6,-1,6,-10,-4,10,7,-3,-3,3,-1,7,2,4,-10,5,5,6,-3,-2,3,-2,-5,-7,7,6,4,10,1,-6,-10,6,-6,-7,-1,7,-3,6,-3,6,-2,7,-8,-4,3,-2,2,10,-2,-8,-6,-9,-3,6,-6,7,7,-8,3,3,-3,-10,-3,-2,7,-8,-4,-3,1,-2,-2,-7,-2,-3,6,-10,-3,3,-1,10,6,3,4,4,5,-4,-6,7,5,-3,-10,-1,5,8,8,4,-6,3,-2,7,6,6,4,10,-5,-2,7,-7,-7,8,3,-1,-10,-10,3,2,9,-1,-5,-2,-5,-7,-10,-5,-9,2,7,-2,-10,-1,-10,-4,5,1,6,10,2,6,-2,-6,-3,5,-4,9,9,-6,-5,7,-6,9,4,5,-9,-5,-1,-3,3,-6,-5,10,-7,3,7,-3,8,6,5,7,4,4,5,2,5,5,-5,6,-1,5,8,-2,-3,-8,2,2,-9,1,-4,-4,-1,9,-3,-7,3,-2,-1,7,5,-10,-3,2,9,-8,6,-9,10,-2,-4,-9,10,-8,-8,-3,-4,-9,-7,1,-6,-6,2,9,5,6,10,-6,7,-3,3,-7,1,6,-8,-4,9,-7,7,-4,9,4,7,2,-8,-10,-3,9,-6,-1,-5,9,5,6,3,-6,2,-2,2,5,-10,-2,-4,6,8,-4,-2,-5,-10,3,-1,-6,1,-3,5,-4,5,-10,8,10,-3,7,9,4,-4,-5,-8,-9,-2,-3,-2,-3,-4,7,7,6,-4,-7,6,6,-8,7,3,-4,-2,-1,-3,-3,-7,9,-8,4,-9,-6,-2,-8,-3,-8,-3,-3,-9,-1,-1,1,5,-2,6,-6,6,-3,4,1,-6,-6], dtype = "int8")#candidate|1733|(1120,)|const|int8
call_1731 = func_307_call(relay.reshape(const_1732.astype('int8'), [8, 14, 1]), relay.reshape(const_1733.astype('int8'), [8, 14, 10]), )
call_1734 = func_307_call(relay.reshape(const_1732.astype('int8'), [8, 14, 1]), relay.reshape(const_1733.astype('int8'), [8, 14, 10]), )
output = relay.Tuple([call_1721,call_1731,const_1732,const_1733,])
output2 = relay.Tuple([call_1722,call_1734,const_1732,const_1733,])
func_1769 = relay.Function([], output)
mod['func_1769'] = func_1769
mod = relay.transform.InferType()(mod)
mutated_mod['func_1769'] = func_1769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mutated_mod.get_global_var('func_1769')
call_1770 = func_1769_call()
output = call_1770
func_1771 = relay.Function([], output)
mutated_mod['func_1771'] = func_1771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_1775 = relay.TupleGetItem(func_1556_call(), 0)
call_1776 = relay.TupleGetItem(func_1557_call(), 0)
output = relay.Tuple([call_1775,])
output2 = relay.Tuple([call_1776,])
func_1803 = relay.Function([], output)
mod['func_1803'] = func_1803
mod = relay.transform.InferType()(mod)
mutated_mod['func_1803'] = func_1803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mutated_mod.get_global_var('func_1803')
call_1804 = func_1803_call()
output = call_1804
func_1805 = relay.Function([], output)
mutated_mod['func_1805'] = func_1805
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1815 = relay.var("var_1815", dtype = "uint32", shape = (11, 3, 11))#candidate|1815|(11, 3, 11)|var|uint32
const_1816 = relay.const([[[-2,-2,-1,3,-9,-10,-9,1,7,-7,-9],[-10,-7,5,8,3,8,-10,-2,-6,7,8],[-6,-3,6,-9,8,-6,-10,5,6,-7,-3]],[[-3,9,8,5,1,2,-4,7,-7,-5,-3],[5,10,-6,-4,-3,4,6,7,5,-3,-5],[7,-10,-8,-9,-7,-9,-4,5,3,-6,-1]],[[6,-6,-7,10,-5,7,-3,-8,8,-7,-4],[1,8,9,-1,-6,8,10,10,1,-10,1],[-3,-6,-6,-7,3,-10,-2,-6,-9,1,-4]],[[-5,4,-10,-2,8,9,4,8,-6,9,-3],[-6,5,-1,3,1,10,3,8,2,-1,-1],[-8,8,1,1,2,10,5,6,-7,-5,2]],[[10,3,7,2,-1,-8,-4,8,-2,-5,8],[6,-7,2,-3,-1,-6,4,8,-3,6,-10],[2,-10,-6,9,-6,-7,9,6,-4,4,1]],[[3,-3,10,10,2,8,8,-8,8,-3,6],[6,3,-8,10,-2,9,-1,-5,-1,-5,-10],[2,10,-1,-7,-5,8,3,-5,-5,7,-2]],[[-7,1,3,-6,1,-10,-8,-3,7,-5,8],[-1,2,7,2,-8,-6,6,7,2,-9,-8],[-5,-9,-1,-7,4,-9,6,6,7,6,4]],[[-3,-3,8,9,-7,9,7,4,-8,-4,7],[-4,7,-8,3,4,-7,-4,8,-3,10,-3],[-9,-10,5,3,-3,6,8,-4,10,-8,-6]],[[-1,8,9,3,2,9,10,-8,-8,2,3],[-10,1,-7,-6,-3,-7,-1,6,6,-8,2],[1,-3,-10,-2,2,-2,-3,-4,-1,-6,-8]],[[3,-2,4,6,-8,-3,-7,-5,-8,3,2],[6,-3,-4,5,5,-8,7,-7,-5,1,7],[2,6,-10,9,-5,9,4,-8,-7,-5,9]],[[4,-6,-2,-8,-4,4,-2,9,8,6,3],[-3,7,5,7,-5,-2,10,7,-5,-10,-10],[-3,4,6,-1,10,-1,5,10,-2,3,-7]]], dtype = "uint32")#candidate|1816|(11, 3, 11)|const|uint32
bop_1817 = relay.logical_xor(var_1815.astype('uint32'), relay.reshape(const_1816.astype('uint32'), relay.shape_of(var_1815))) # shape=(11, 3, 11)
output = relay.Tuple([bop_1817,])
output2 = relay.Tuple([bop_1817,])
func_1824 = relay.Function([var_1815,], output)
mod['func_1824'] = func_1824
mod = relay.transform.InferType()(mod)
var_1825 = relay.var("var_1825", dtype = "uint32", shape = (11, 3, 11))#candidate|1825|(11, 3, 11)|var|uint32
output = func_1824(var_1825)
func_1826 = relay.Function([var_1825], output)
mutated_mod['func_1826'] = func_1826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_1847 = relay.TupleGetItem(func_1803_call(), 0)
call_1848 = relay.TupleGetItem(func_1805_call(), 0)
func_1588_call = mod.get_global_var('func_1588')
func_1590_call = mutated_mod.get_global_var('func_1590')
call_1853 = relay.TupleGetItem(func_1588_call(relay.reshape(call_1847.astype('float32'), [312, 1])), 1)
call_1854 = relay.TupleGetItem(func_1590_call(relay.reshape(call_1847.astype('float32'), [312, 1])), 1)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_1905 = relay.TupleGetItem(func_1803_call(), 0)
call_1906 = relay.TupleGetItem(func_1805_call(), 0)
output = relay.Tuple([call_1847,call_1853,call_1905,])
output2 = relay.Tuple([call_1848,call_1854,call_1906,])
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
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_1944 = relay.TupleGetItem(func_1556_call(), 0)
call_1945 = relay.TupleGetItem(func_1557_call(), 0)
func_1824_call = mod.get_global_var('func_1824')
func_1826_call = mutated_mod.get_global_var('func_1826')
var_1955 = relay.var("var_1955", dtype = "uint32", shape = (363,))#candidate|1955|(363,)|var|uint32
call_1954 = relay.TupleGetItem(func_1824_call(relay.reshape(var_1955.astype('uint32'), [11, 3, 11])), 0)
call_1956 = relay.TupleGetItem(func_1826_call(relay.reshape(var_1955.astype('uint32'), [11, 3, 11])), 0)
output = relay.Tuple([call_1944,call_1954,var_1955,])
output2 = relay.Tuple([call_1945,call_1956,var_1955,])
func_1964 = relay.Function([var_1955,], output)
mod['func_1964'] = func_1964
mod = relay.transform.InferType()(mod)
mutated_mod['func_1964'] = func_1964
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1965 = relay.var("var_1965", dtype = "uint32", shape = (363,))#candidate|1965|(363,)|var|uint32
func_1964_call = mutated_mod.get_global_var('func_1964')
call_1966 = func_1964_call(var_1965)
output = call_1966
func_1967 = relay.Function([var_1965], output)
mutated_mod['func_1967'] = func_1967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2006 = relay.TupleGetItem(func_1769_call(), 0)
call_2007 = relay.TupleGetItem(func_1771_call(), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
call_2014 = relay.TupleGetItem(func_1535_call(relay.reshape(call_2006.astype('float32'), [1, 312])), 1)
call_2015 = relay.TupleGetItem(func_1538_call(relay.reshape(call_2006.astype('float32'), [1, 312])), 1)
var_2027 = relay.var("var_2027", dtype = "float32", shape = (6, 13, 4))#candidate|2027|(6, 13, 4)|var|float32
bop_2028 = relay.logical_and(call_2014.astype('bool'), relay.reshape(var_2027.astype('bool'), relay.shape_of(call_2014))) # shape=(6, 13, 4)
bop_2031 = relay.logical_and(call_2015.astype('bool'), relay.reshape(var_2027.astype('bool'), relay.shape_of(call_2015))) # shape=(6, 13, 4)
output = relay.Tuple([call_2006,bop_2028,])
output2 = relay.Tuple([call_2007,bop_2031,])
func_2032 = relay.Function([var_2027,], output)
mod['func_2032'] = func_2032
mod = relay.transform.InferType()(mod)
var_2033 = relay.var("var_2033", dtype = "float32", shape = (6, 13, 4))#candidate|2033|(6, 13, 4)|var|float32
output = func_2032(var_2033)
func_2034 = relay.Function([var_2033], output)
mutated_mod['func_2034'] = func_2034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_2058 = relay.TupleGetItem(func_1556_call(), 0)
call_2059 = relay.TupleGetItem(func_1557_call(), 0)
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
var_2062 = relay.var("var_2062", dtype = "int8", shape = (112,))#candidate|2062|(112,)|var|int8
var_2063 = relay.var("var_2063", dtype = "int8", shape = (1120,))#candidate|2063|(1120,)|var|int8
call_2061 = func_307_call(relay.reshape(var_2062.astype('int8'), [8, 14, 1]), relay.reshape(var_2063.astype('int8'), [8, 14, 10]), )
call_2064 = func_307_call(relay.reshape(var_2062.astype('int8'), [8, 14, 1]), relay.reshape(var_2063.astype('int8'), [8, 14, 10]), )
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_2069 = relay.TupleGetItem(func_1803_call(), 0)
call_2070 = relay.TupleGetItem(func_1805_call(), 0)
output = relay.Tuple([call_2058,call_2061,var_2062,var_2063,call_2069,])
output2 = relay.Tuple([call_2059,call_2064,var_2062,var_2063,call_2070,])
func_2080 = relay.Function([var_2062,var_2063,], output)
mod['func_2080'] = func_2080
mod = relay.transform.InferType()(mod)
mutated_mod['func_2080'] = func_2080
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2080_call = mutated_mod.get_global_var('func_2080')
var_2082 = relay.var("var_2082", dtype = "int8", shape = (112,))#candidate|2082|(112,)|var|int8
var_2083 = relay.var("var_2083", dtype = "int8", shape = (1120,))#candidate|2083|(1120,)|var|int8
call_2081 = func_2080_call(var_2082,var_2083,)
output = call_2081
func_2084 = relay.Function([var_2082,var_2083,], output)
mutated_mod['func_2084'] = func_2084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2130 = relay.TupleGetItem(func_1769_call(), 1)
call_2131 = relay.TupleGetItem(func_1771_call(), 1)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2139 = relay.TupleGetItem(func_1769_call(), 1)
call_2140 = relay.TupleGetItem(func_1771_call(), 1)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_2148 = relay.TupleGetItem(func_1556_call(), 0)
call_2149 = relay.TupleGetItem(func_1557_call(), 0)
output = relay.Tuple([call_2130,call_2139,call_2148,])
output2 = relay.Tuple([call_2131,call_2140,call_2149,])
func_2162 = relay.Function([], output)
mod['func_2162'] = func_2162
mod = relay.transform.InferType()(mod)
output = func_2162()
func_2163 = relay.Function([], output)
mutated_mod['func_2163'] = func_2163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2195 = relay.TupleGetItem(func_1769_call(), 0)
call_2196 = relay.TupleGetItem(func_1771_call(), 0)
output = call_2195
output2 = call_2196
func_2204 = relay.Function([], output)
mod['func_2204'] = func_2204
mod = relay.transform.InferType()(mod)
output = func_2204()
func_2205 = relay.Function([], output)
mutated_mod['func_2205'] = func_2205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2270 = relay.TupleGetItem(func_1769_call(), 1)
call_2271 = relay.TupleGetItem(func_1771_call(), 1)
output = call_2270
output2 = call_2271
func_2281 = relay.Function([], output)
mod['func_2281'] = func_2281
mod = relay.transform.InferType()(mod)
mutated_mod['func_2281'] = func_2281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mutated_mod.get_global_var('func_2281')
call_2282 = func_2281_call()
output = call_2282
func_2283 = relay.Function([], output)
mutated_mod['func_2283'] = func_2283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_2287 = func_2281_call()
call_2288 = func_2281_call()
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
const_2295 = relay.const([-0.247014,-8.458428,-0.641926,1.199489,8.563514,7.430460,-3.727999,5.377514,-7.291618,7.373607,9.459112,2.599550,-8.568781,5.709648,-2.775174,-9.815685,9.194238,-0.701624,4.889021,6.538705,-5.363438,-9.583160,-7.044117,2.037600,9.923688,-0.512298,1.440793,9.443947,-9.983472,-9.537899,-5.105122,-0.035531,0.287579,9.981900,-0.164059,-9.474721,9.904948,-3.822952,-3.007436,-3.049211,-1.187145,-9.661804,-4.935151,4.455363,-8.750737,-7.436181,-0.992921,-7.988313,5.885555,-9.420181,-4.202393,5.187937,-0.378284,-9.774517,2.670687,-3.782956,6.266805,-2.092825,-1.903158,0.795941,2.241448,6.732965,-4.120642,0.179049,7.664009,5.949248,-9.563862,8.385974,-7.760561,4.048925,-9.979592,-3.221271,0.328339,-8.317777,-8.585493,-2.079113,1.474043,-2.697076,-1.025488,0.319643,2.263381,0.005431,1.226996,-8.214810,-1.962029,-4.748002,7.619578,5.878916,1.573816,6.754786,6.140550,4.785752,4.898314,-3.427391,8.751631,-3.816250,-0.728868,8.528207,-1.402337,-4.215711,7.408094,-6.097475,6.982009,3.764358,6.513658,-2.261551,9.822319,8.207949,2.758179,-8.296242,7.553241,-8.990587,-3.255191,-9.608062,8.328544,-0.486591,9.457245,-5.838805,-1.934907,8.074678,-4.882205,-0.259135,1.381091,-8.637021,6.921796,6.540980,8.748137,-5.631276,1.652498,8.694790,8.461174,-5.752914,-0.470767,2.119586,-3.635689,-6.651206,2.528770,-1.602139,-1.510680,1.696436,5.779926,-1.115995,-6.830395,5.065027,2.405598,7.246127,-2.825049,0.554461,-6.225692,9.303061,8.861266,2.380507,-4.560307,0.809109,-4.017010,-8.335494,-2.134930,9.120200,7.611349,-9.583193,3.159209,-0.281309,6.098210,-7.528008,-8.711786,8.088806,6.624664,-5.119264,-7.651782,-9.500059,4.094739,9.304177,4.050050,-5.183935,6.947574,-3.211234,-6.577342,-9.229494,-7.287026,7.290019,-9.436193,7.562780,8.398592,5.085169,7.204919,9.414582,-8.300116,-8.568365,6.287538,-7.733348,-6.768394,7.745041,6.363410,-1.405983,-1.618216,8.755257,-6.965670,-1.017040,-3.326677,-9.797432,5.885913,-3.423125,-3.886445,7.289839,-5.459085,-0.387616,-3.779095,9.869280,9.060044,-9.175891,-4.784316,-6.743945,-1.162394,-7.227521,-7.482611,-2.261671,-6.181072,9.302103,-3.612736,-7.399113,-1.689793,5.821113,-1.183002,6.046969,-6.979038,6.596222,5.490739,-7.725626,-1.620092,-8.507692,6.715746,-7.300141,-5.062964,-7.896777,2.770199,4.267280,1.933349,-8.489816,9.559787,9.468951,3.106941,-5.932075,-9.601570,-4.599976,-4.739192,0.967917,-0.076155,4.863480,9.655320,9.488170,7.804432,-6.741498,7.591633,-0.884160,-1.614091,-4.197564,5.030891,-8.164160,4.690192,-4.174965,-5.210815,0.011924,-5.362032,0.586667,-0.425420,-5.811300,0.847522,-5.619534,0.725272,3.144481,-6.872606,-3.534434,0.261107,7.085415,0.209759,-4.555916,1.163330,-8.082121,-3.470242,2.455828,-5.282354,-6.606251,4.101572,-0.790927,-0.972502,-2.860841,-9.182142,-3.823037,-6.996624,-3.865473,1.127211,3.349747,7.455480,-2.543237,5.858293,-1.881673,2.839338,0.200038,-8.074331,-7.661518,4.657972,4.882083,5.688347,5.142683,-7.073574,7.512020,-6.597027,-2.423261,0.642345,-8.643186,9.022316,-7.082708], dtype = "float32")#candidate|2295|(312,)|const|float32
call_2294 = relay.TupleGetItem(func_1535_call(relay.reshape(const_2295.astype('float32'), [1, 312])), 2)
call_2296 = relay.TupleGetItem(func_1538_call(relay.reshape(const_2295.astype('float32'), [1, 312])), 2)
output = relay.Tuple([call_2287,call_2294,const_2295,])
output2 = relay.Tuple([call_2288,call_2296,const_2295,])
func_2297 = relay.Function([], output)
mod['func_2297'] = func_2297
mod = relay.transform.InferType()(mod)
mutated_mod['func_2297'] = func_2297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2297_call = mutated_mod.get_global_var('func_2297')
call_2298 = func_2297_call()
output = call_2298
func_2299 = relay.Function([], output)
mutated_mod['func_2299'] = func_2299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_2308 = relay.TupleGetItem(func_1488_call(), 1)
call_2309 = relay.TupleGetItem(func_1490_call(), 1)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2318 = relay.TupleGetItem(func_2162_call(), 0)
call_2319 = relay.TupleGetItem(func_2163_call(), 0)
output = relay.Tuple([call_2308,call_2318,])
output2 = relay.Tuple([call_2309,call_2319,])
func_2320 = relay.Function([], output)
mod['func_2320'] = func_2320
mod = relay.transform.InferType()(mod)
output = func_2320()
func_2321 = relay.Function([], output)
mutated_mod['func_2321'] = func_2321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_2336 = func_2281_call()
call_2337 = func_2281_call()
output = call_2336
output2 = call_2337
func_2361 = relay.Function([], output)
mod['func_2361'] = func_2361
mod = relay.transform.InferType()(mod)
output = func_2361()
func_2362 = relay.Function([], output)
mutated_mod['func_2362'] = func_2362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2379 = relay.TupleGetItem(func_2162_call(), 1)
call_2380 = relay.TupleGetItem(func_2163_call(), 1)
output = relay.Tuple([call_2379,])
output2 = relay.Tuple([call_2380,])
func_2403 = relay.Function([], output)
mod['func_2403'] = func_2403
mod = relay.transform.InferType()(mod)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2404 = func_2403_call()
output = call_2404
func_2405 = relay.Function([], output)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2297_call = mod.get_global_var('func_2297')
func_2299_call = mutated_mod.get_global_var('func_2299')
call_2433 = relay.TupleGetItem(func_2297_call(), 2)
call_2434 = relay.TupleGetItem(func_2299_call(), 2)
func_1588_call = mod.get_global_var('func_1588')
func_1590_call = mutated_mod.get_global_var('func_1590')
call_2435 = relay.TupleGetItem(func_1588_call(relay.reshape(call_2433.astype('float32'), [312, 1])), 1)
call_2436 = relay.TupleGetItem(func_1590_call(relay.reshape(call_2433.astype('float32'), [312, 1])), 1)
var_2477 = relay.var("var_2477", dtype = "float32", shape = (312,))#candidate|2477|(312,)|var|float32
bop_2478 = relay.mod(call_2433.astype('float32'), relay.reshape(var_2477.astype('float32'), relay.shape_of(call_2433))) # shape=(312,)
bop_2481 = relay.mod(call_2434.astype('float32'), relay.reshape(var_2477.astype('float32'), relay.shape_of(call_2434))) # shape=(312,)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_2507 = relay.TupleGetItem(func_1258_call(relay.reshape(bop_2478.astype('float32'), [6, 13, 4])), 0)
call_2508 = relay.TupleGetItem(func_1261_call(relay.reshape(bop_2478.astype('float32'), [6, 13, 4])), 0)
output = relay.Tuple([call_2435,bop_2478,call_2507,])
output2 = relay.Tuple([call_2436,bop_2481,call_2508,])
func_2510 = relay.Function([var_2477,], output)
mod['func_2510'] = func_2510
mod = relay.transform.InferType()(mod)
mutated_mod['func_2510'] = func_2510
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2511 = relay.var("var_2511", dtype = "float32", shape = (312,))#candidate|2511|(312,)|var|float32
func_2510_call = mutated_mod.get_global_var('func_2510')
call_2512 = func_2510_call(var_2511)
output = call_2512
func_2513 = relay.Function([var_2511], output)
mutated_mod['func_2513'] = func_2513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_2520 = relay.TupleGetItem(func_1769_call(), 2)
call_2521 = relay.TupleGetItem(func_1771_call(), 2)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2525 = relay.TupleGetItem(func_2162_call(), 1)
call_2526 = relay.TupleGetItem(func_2163_call(), 1)
func_2080_call = mod.get_global_var('func_2080')
func_2084_call = mutated_mod.get_global_var('func_2084')
call_2537 = relay.TupleGetItem(func_2080_call(relay.reshape(call_2520.astype('int8'), [112,]), relay.reshape(call_2525.astype('int8'), [1120,]), ), 1)
call_2538 = relay.TupleGetItem(func_2084_call(relay.reshape(call_2520.astype('int8'), [112,]), relay.reshape(call_2525.astype('int8'), [1120,]), ), 1)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_2544 = func_2361_call()
call_2545 = func_2361_call()
bop_2555 = relay.left_shift(call_2525.astype('int64'), relay.reshape(call_2537.astype('int64'), relay.shape_of(call_2525))) # shape=(8, 14, 10)
bop_2558 = relay.left_shift(call_2526.astype('int64'), relay.reshape(call_2538.astype('int64'), relay.shape_of(call_2526))) # shape=(8, 14, 10)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_2560 = func_2281_call()
call_2561 = func_2281_call()
output = relay.Tuple([call_2520,call_2544,bop_2555,call_2560,])
output2 = relay.Tuple([call_2521,call_2545,bop_2558,call_2561,])
func_2587 = relay.Function([], output)
mod['func_2587'] = func_2587
mod = relay.transform.InferType()(mod)
output = func_2587()
func_2588 = relay.Function([], output)
mutated_mod['func_2588'] = func_2588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_2703 = func_2361_call()
call_2704 = func_2361_call()
output = call_2703
output2 = call_2704
func_2714 = relay.Function([], output)
mod['func_2714'] = func_2714
mod = relay.transform.InferType()(mod)
output = func_2714()
func_2715 = relay.Function([], output)
mutated_mod['func_2715'] = func_2715
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2799 = relay.var("var_2799", dtype = "float32", shape = (16, 14, 5))#candidate|2799|(16, 14, 5)|var|float32
var_2800 = relay.var("var_2800", dtype = "float32", shape = (16, 14, 5))#candidate|2800|(16, 14, 5)|var|float32
bop_2801 = relay.power(var_2799.astype('float32'), relay.reshape(var_2800.astype('float32'), relay.shape_of(var_2799))) # shape=(16, 14, 5)
output = bop_2801
output2 = bop_2801
func_2804 = relay.Function([var_2799,var_2800,], output)
mod['func_2804'] = func_2804
mod = relay.transform.InferType()(mod)
var_2805 = relay.var("var_2805", dtype = "float32", shape = (16, 14, 5))#candidate|2805|(16, 14, 5)|var|float32
var_2806 = relay.var("var_2806", dtype = "float32", shape = (16, 14, 5))#candidate|2806|(16, 14, 5)|var|float32
output = func_2804(var_2805,var_2806,)
func_2807 = relay.Function([var_2805,var_2806,], output)
mutated_mod['func_2807'] = func_2807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2204_call = mod.get_global_var('func_2204')
func_2205_call = mutated_mod.get_global_var('func_2205')
call_2828 = func_2204_call()
call_2829 = func_2204_call()
uop_2839 = relay.rsqrt(call_2828.astype('float32')) # shape=(6, 13, 4)
uop_2841 = relay.rsqrt(call_2829.astype('float32')) # shape=(6, 13, 4)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_2842 = relay.TupleGetItem(func_2162_call(), 1)
call_2843 = relay.TupleGetItem(func_2163_call(), 1)
uop_2856 = relay.atanh(uop_2839.astype('float32')) # shape=(6, 13, 4)
uop_2858 = relay.atanh(uop_2841.astype('float32')) # shape=(6, 13, 4)
uop_2869 = relay.log2(uop_2856.astype('float64')) # shape=(6, 13, 4)
uop_2871 = relay.log2(uop_2858.astype('float64')) # shape=(6, 13, 4)
uop_2872 = relay.cos(uop_2869.astype('float32')) # shape=(6, 13, 4)
uop_2874 = relay.cos(uop_2871.astype('float32')) # shape=(6, 13, 4)
func_2080_call = mod.get_global_var('func_2080')
func_2084_call = mutated_mod.get_global_var('func_2084')
const_2878 = relay.const([[-10,-3],[7,-10],[4,-8],[6,-7],[10,-10],[7,7],[10,9],[7,-3],[6,-7],[-5,8],[5,-6],[-1,-1],[-6,1],[2,3],[9,3],[-3,4],[4,4],[10,-9],[-5,5],[-7,8],[9,9],[7,-3],[-1,-2],[-3,-6],[10,6],[-2,-5],[1,-5],[-8,2],[-4,9],[10,-8],[8,-7],[-10,8],[5,-8],[-1,5],[2,-10],[5,-8],[-2,10],[10,-5],[2,9],[-7,10],[3,10],[-2,7],[7,4],[7,10],[-10,-1],[10,9],[8,-4],[5,6],[3,-3],[10,-8],[-5,-10],[-8,-2],[-3,-9],[9,-7],[-5,1],[-6,-7]], dtype = "int8")#candidate|2878|(56, 2)|const|int8
call_2877 = relay.TupleGetItem(func_2080_call(relay.reshape(const_2878.astype('int8'), [112,]), relay.reshape(call_2842.astype('int8'), [1120,]), ), 1)
call_2879 = relay.TupleGetItem(func_2084_call(relay.reshape(const_2878.astype('int8'), [112,]), relay.reshape(call_2842.astype('int8'), [1120,]), ), 1)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_2899 = relay.TupleGetItem(func_1488_call(), 0)
call_2900 = relay.TupleGetItem(func_1490_call(), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
call_2904 = relay.TupleGetItem(func_1535_call(relay.reshape(uop_2839.astype('float32'), [1, 312])), 0)
call_2905 = relay.TupleGetItem(func_1538_call(relay.reshape(uop_2839.astype('float32'), [1, 312])), 0)
func_1258_call = mod.get_global_var('func_1258')
func_1261_call = mutated_mod.get_global_var('func_1261')
call_2916 = relay.TupleGetItem(func_1258_call(relay.reshape(call_2828.astype('float32'), [6, 13, 4])), 0)
call_2917 = relay.TupleGetItem(func_1261_call(relay.reshape(call_2828.astype('float32'), [6, 13, 4])), 0)
output = relay.Tuple([call_2842,uop_2872,call_2877,const_2878,call_2899,call_2904,call_2916,])
output2 = relay.Tuple([call_2843,uop_2874,call_2879,const_2878,call_2900,call_2905,call_2917,])
func_2937 = relay.Function([], output)
mod['func_2937'] = func_2937
mod = relay.transform.InferType()(mod)
mutated_mod['func_2937'] = func_2937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2937_call = mutated_mod.get_global_var('func_2937')
call_2938 = func_2937_call()
output = call_2938
func_2939 = relay.Function([], output)
mutated_mod['func_2939'] = func_2939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_3044 = func_2361_call()
call_3045 = func_2361_call()
output = relay.Tuple([call_3044,])
output2 = relay.Tuple([call_3045,])
func_3047 = relay.Function([], output)
mod['func_3047'] = func_3047
mod = relay.transform.InferType()(mod)
output = func_3047()
func_3048 = relay.Function([], output)
mutated_mod['func_3048'] = func_3048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3075 = relay.var("var_3075", dtype = "float32", shape = (15, 4, 5))#candidate|3075|(15, 4, 5)|var|float32
uop_3076 = relay.exp(var_3075.astype('float32')) # shape=(15, 4, 5)
bop_3078 = relay.minimum(var_3075.astype('float32'), relay.reshape(uop_3076.astype('float32'), relay.shape_of(var_3075))) # shape=(15, 4, 5)
uop_3081 = relay.asinh(bop_3078.astype('float32')) # shape=(15, 4, 5)
bop_3093 = relay.bitwise_and(uop_3081.astype('uint16'), relay.reshape(uop_3076.astype('uint16'), relay.shape_of(uop_3081))) # shape=(15, 4, 5)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_3110 = relay.TupleGetItem(func_1769_call(), 1)
call_3111 = relay.TupleGetItem(func_1771_call(), 1)
func_1588_call = mod.get_global_var('func_1588')
func_1590_call = mutated_mod.get_global_var('func_1590')
var_3126 = relay.var("var_3126", dtype = "float32", shape = (6, 52))#candidate|3126|(6, 52)|var|float32
call_3125 = relay.TupleGetItem(func_1588_call(relay.reshape(var_3126.astype('float32'), [312, 1])), 1)
call_3127 = relay.TupleGetItem(func_1590_call(relay.reshape(var_3126.astype('float32'), [312, 1])), 1)
var_3130 = relay.var("var_3130", dtype = "int8", shape = (8, 14, 10))#candidate|3130|(8, 14, 10)|var|int8
bop_3131 = relay.less_equal(call_3110.astype('bool'), relay.reshape(var_3130.astype('bool'), relay.shape_of(call_3110))) # shape=(8, 14, 10)
bop_3134 = relay.less_equal(call_3111.astype('bool'), relay.reshape(var_3130.astype('bool'), relay.shape_of(call_3111))) # shape=(8, 14, 10)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_3137 = relay.TupleGetItem(func_2937_call(), 0)
call_3138 = relay.TupleGetItem(func_2939_call(), 0)
output = relay.Tuple([bop_3093,call_3125,var_3126,bop_3131,call_3137,])
output2 = relay.Tuple([bop_3093,call_3127,var_3126,bop_3134,call_3138,])
func_3143 = relay.Function([var_3075,var_3126,var_3130,], output)
mod['func_3143'] = func_3143
mod = relay.transform.InferType()(mod)
mutated_mod['func_3143'] = func_3143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3143_call = mutated_mod.get_global_var('func_3143')
var_3145 = relay.var("var_3145", dtype = "float32", shape = (15, 4, 5))#candidate|3145|(15, 4, 5)|var|float32
var_3146 = relay.var("var_3146", dtype = "float32", shape = (6, 52))#candidate|3146|(6, 52)|var|float32
var_3147 = relay.var("var_3147", dtype = "int8", shape = (8, 14, 10))#candidate|3147|(8, 14, 10)|var|int8
call_3144 = func_3143_call(var_3145,var_3146,var_3147,)
output = call_3144
func_3148 = relay.Function([var_3145,var_3146,var_3147,], output)
mutated_mod['func_3148'] = func_3148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_3176 = relay.TupleGetItem(func_2403_call(), 0)
call_3177 = relay.TupleGetItem(func_2405_call(), 0)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_3203 = func_2281_call()
call_3204 = func_2281_call()
uop_3208 = relay.sin(call_3176.astype('float32')) # shape=(8, 14, 10)
uop_3210 = relay.sin(call_3177.astype('float32')) # shape=(8, 14, 10)
output = relay.Tuple([call_3203,uop_3208,])
output2 = relay.Tuple([call_3204,uop_3210,])
func_3212 = relay.Function([], output)
mod['func_3212'] = func_3212
mod = relay.transform.InferType()(mod)
mutated_mod['func_3212'] = func_3212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3212_call = mutated_mod.get_global_var('func_3212')
call_3213 = func_3212_call()
output = call_3213
func_3214 = relay.Function([], output)
mutated_mod['func_3214'] = func_3214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_3239 = relay.TupleGetItem(func_2937_call(), 0)
call_3240 = relay.TupleGetItem(func_2939_call(), 0)
func_2510_call = mod.get_global_var('func_2510')
func_2513_call = mutated_mod.get_global_var('func_2513')
const_3248 = relay.const([[-9.349918,-8.719655,-7.964708,-7.382603,3.323609,-2.883918,8.458133,9.841828,1.727084,1.038683,-9.906753,-3.086660,3.310879,-3.323377,7.606036,-2.059593,-8.871803,-9.797196,6.525144,-4.694009,-1.922086,6.348247,8.717057,7.863593,0.306689,2.885135,5.551433,3.843466,9.297322,6.180927,7.483555,3.660034,-3.913694,-2.600015,-6.103375,-6.312132,-5.092438,-0.492227,-0.691788,-8.769576,-8.328687,-3.133540,1.532926,2.223209,5.051494,5.579202,-7.253111,7.726921,-5.813958,7.017578,-5.112546,9.914430,3.110783,0.930089,1.611846,8.605180,6.023653,-4.299033,-2.845636,-6.041362,-8.924094,-8.764216,-7.478656,8.278060,0.105457,3.154718,4.432965,-0.104704,-5.719673,-7.598523,3.005035,-4.730527,2.756044,7.002836,-3.447210,-3.188137,4.414367,4.131758,-8.207088,-4.982344,1.208629,5.587927,3.874634,6.164248,4.557333,6.834286,-5.190566,-5.725366,-0.311606,0.942794,8.296570,3.634536,-7.288980,-2.582081,-4.806358,-8.534378,-7.508071,-2.898958,-0.939532,8.953881,7.478018,-3.411233,-9.538197,-1.994932],[0.721530,3.965340,5.214831,3.325965,-8.168501,-7.118524,1.973387,-7.485537,-3.550492,2.452065,6.965058,9.947297,2.902145,-4.769179,-9.116905,4.095377,-0.786071,-0.286638,6.126323,1.498918,2.193646,-8.461532,-5.855207,-0.915638,9.633621,9.658130,-3.658558,-3.993878,8.838648,-4.337044,3.649464,9.219456,-1.272243,4.387544,7.962017,8.679237,-9.655135,4.485555,0.223448,1.741259,9.483609,0.433286,3.996308,-5.588822,-9.260099,-3.032789,-6.137280,6.306077,0.491389,-9.522163,7.153576,1.055606,-2.037331,-6.516229,-9.611069,-4.160943,7.919347,-0.720041,4.084118,9.910762,4.423819,2.471397,8.108432,-6.495170,2.519930,2.389913,6.100249,-5.058214,-8.677472,0.067805,9.632861,-6.879392,1.305568,2.208831,1.231049,-3.924929,3.280825,-7.498419,-5.040559,9.812827,-3.625151,-3.042531,-7.207692,8.463538,7.038871,7.341014,-2.531672,3.565418,-4.947588,8.191616,9.691406,-0.145549,6.115573,2.296044,-6.363969,-9.278696,-9.761950,-6.072223,0.427514,4.148160,-1.800583,3.681888,-4.397379,-3.652799],[-1.155606,7.198942,6.350523,-3.482087,-5.206311,-9.535582,-4.090321,0.135233,8.036742,3.143740,8.486116,3.684278,-4.959244,0.389570,-9.914789,8.683396,9.338302,-3.773183,6.110457,8.836994,4.368212,-3.004528,-0.307175,-1.793100,5.356207,4.423013,-9.864199,-6.877217,8.741302,2.740717,5.776996,-1.273380,5.067422,7.161609,5.808523,4.661000,-4.194606,2.427485,1.943171,-7.635085,8.415900,-8.323437,-2.268508,-4.177395,-9.311932,1.717256,1.272162,-3.163718,5.607685,1.615925,-6.099638,6.722260,-9.028729,-0.724726,-2.904689,-0.387238,-5.952393,4.755147,5.630528,-2.391410,5.926840,9.844213,-5.852480,-5.196785,5.154048,-5.043586,-8.136322,-8.873198,-5.313774,-5.793714,4.765478,3.618112,2.495310,-9.991796,-8.107757,-5.102201,3.280144,-8.873535,6.746960,2.034351,-7.105670,3.994823,5.404400,3.445544,-8.157590,-2.828249,-5.198507,6.541057,-7.198424,-8.455266,-1.553265,-2.148062,-3.915842,8.778005,8.718003,-9.262740,6.093389,-6.887205,1.007735,-8.956077,-5.130921,0.167576,-8.316152,-1.494283]], dtype = "float32")#candidate|3248|(3, 104)|const|float32
call_3247 = relay.TupleGetItem(func_2510_call(relay.reshape(const_3248.astype('float32'), [312,])), 2)
call_3249 = relay.TupleGetItem(func_2513_call(relay.reshape(const_3248.astype('float32'), [312,])), 2)
const_3260 = relay.const([[5.940241,-3.847056,-7.152110,-0.506907,-1.834234,6.734370,2.752859,3.844139,0.494202,9.931902,-2.629047,-2.333063,9.704836,4.934232,-5.181178,3.562857,-9.594897,-5.110700,-2.841068,3.480838,5.499649,7.349307,-9.426559,7.461895,9.233953,4.736809,9.779762,-7.598820,1.767378,7.553231,0.660448,-5.635244,-4.087874,-6.118544,7.263129,7.883531,-7.293387,5.678712,8.003338,9.568201,1.468603,-5.182575,-0.551204,-8.870166,9.322154,2.734248,-1.162008,-3.731092,-9.700226,-6.579262,6.385935,-4.503497,-3.346672,-4.916759,-8.707265,-9.942588,-3.613457,-3.940285,-1.144458,-8.553402,-9.723215,-6.158935,1.714691,1.783422,0.896381,1.609306,5.104184,-2.777724,7.662038,-1.196541,-4.131693,-8.270464,8.673305,0.794155,6.253044,0.026666,2.836757,-5.132625,3.815990,-8.918766,6.469291,9.174052,5.533790,-7.553872,-6.806753,6.942334,-3.199242,4.815639,-8.607077,4.665625,-3.276261,-0.109936,-0.651686,7.966285,-7.722945,-5.286085,9.641135,0.869042,8.213646,-1.507751,-9.717323,1.553056,5.693502,-4.939095],[9.529539,6.803695,9.893832,-2.659613,-2.401374,7.565439,1.301275,0.689893,3.459696,-0.774752,-5.316136,-6.734174,-6.634625,2.318979,-3.771478,3.141729,6.722810,6.097180,-7.547186,-9.347815,3.429196,-8.684955,0.329033,-6.319925,-5.664753,-1.940150,4.120707,5.875126,-9.066227,8.751127,-1.850448,-2.324203,3.917996,-7.119310,5.685620,-8.856996,-2.107559,-1.721822,-1.568481,-1.342342,2.961792,-7.792592,4.650047,-1.622177,-6.413166,-0.443210,-6.512729,3.054828,4.806126,-5.881377,-1.468220,0.232703,1.525995,9.495954,-2.556493,-8.770050,-5.568096,-4.818359,-8.942023,5.009206,-1.294804,7.112091,-6.748097,-3.861903,5.989032,5.167696,-9.251041,-2.218366,-4.250460,9.485491,-5.183064,-3.048489,-6.209175,-9.716606,8.514886,-1.112546,-5.917763,-5.404941,-1.751874,-1.566626,9.896170,8.897005,-0.974717,7.851799,1.429372,-1.380719,-0.343229,-2.338233,6.238327,7.642086,-0.456003,2.937399,-0.677573,-0.025323,-8.139110,-1.400016,-1.287593,4.694709,8.709809,7.887693,-6.999985,-3.942323,-3.382781,9.558248],[-8.867377,-7.285337,-3.565469,1.811462,7.590657,7.474986,-7.828468,-5.212230,-1.967892,2.929069,-4.036064,-5.176856,-1.999887,-4.300520,-6.585814,7.553582,-2.608072,0.555452,6.073427,2.510031,-2.659974,-5.680171,-7.196798,1.731780,7.226960,8.672667,8.064131,-9.935143,-4.572094,-0.389565,-3.666647,9.224815,9.090365,-0.388722,3.962498,-1.026493,-0.896332,-5.871204,9.433275,7.430517,2.853409,-7.587835,9.340696,-6.657322,8.677415,-0.189528,-5.413090,0.992358,-0.787606,-4.107414,2.968252,-0.513737,-5.569009,9.724381,-2.599816,-8.239945,9.032569,1.580839,2.759178,-6.310177,-7.533513,-6.476056,1.739901,0.064229,2.621593,3.507015,-7.844697,4.628900,7.272510,-2.063915,5.023738,0.592257,2.329697,3.904819,-5.647463,-1.787498,-9.154998,-2.843325,-8.457440,-4.192318,9.271910,-8.082039,6.869875,-5.498264,-5.397509,-2.792582,0.441735,-1.350900,-6.920212,9.787021,-6.340916,-9.892294,7.519088,-4.410156,-6.972210,2.573041,-8.664374,1.954134,9.290869,-0.383752,-6.284534,-9.135372,-2.024327,-0.565879]], dtype = "float32")#candidate|3260|(3, 104)|const|float32
bop_3261 = relay.multiply(const_3248.astype('uint8'), relay.reshape(const_3260.astype('uint8'), relay.shape_of(const_3248))) # shape=(3, 104)
uop_3287 = relay.cosh(bop_3261.astype('float64')) # shape=(3, 104)
var_3293 = relay.var("var_3293", dtype = "float64", shape = (3, 104))#candidate|3293|(3, 104)|var|float64
bop_3294 = relay.mod(uop_3287.astype('float32'), relay.reshape(var_3293.astype('float32'), relay.shape_of(uop_3287))) # shape=(3, 104)
bop_3299 = relay.floor_mod(bop_3294.astype('float32'), relay.reshape(var_3293.astype('float32'), relay.shape_of(bop_3294))) # shape=(3, 104)
uop_3309 = relay.acos(bop_3294.astype('float64')) # shape=(3, 104)
var_3322 = relay.var("var_3322", dtype = "float64", shape = (3, 104))#candidate|3322|(3, 104)|var|float64
bop_3323 = relay.not_equal(uop_3309.astype('bool'), relay.reshape(var_3322.astype('bool'), relay.shape_of(uop_3309))) # shape=(3, 104)
func_2297_call = mod.get_global_var('func_2297')
func_2299_call = mutated_mod.get_global_var('func_2299')
call_3333 = relay.TupleGetItem(func_2297_call(), 2)
call_3334 = relay.TupleGetItem(func_2299_call(), 2)
output = relay.Tuple([call_3239,call_3247,bop_3299,bop_3323,call_3333,])
output2 = relay.Tuple([call_3240,call_3249,bop_3299,bop_3323,call_3334,])
func_3335 = relay.Function([var_3293,var_3322,], output)
mod['func_3335'] = func_3335
mod = relay.transform.InferType()(mod)
var_3336 = relay.var("var_3336", dtype = "float64", shape = (3, 104))#candidate|3336|(3, 104)|var|float64
var_3337 = relay.var("var_3337", dtype = "float64", shape = (3, 104))#candidate|3337|(3, 104)|var|float64
output = func_3335(var_3336,var_3337,)
func_3338 = relay.Function([var_3336,var_3337,], output)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_3351 = relay.TupleGetItem(func_1556_call(), 0)
call_3352 = relay.TupleGetItem(func_1557_call(), 0)
output = call_3351
output2 = call_3352
func_3359 = relay.Function([], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
output = func_3359()
func_3360 = relay.Function([], output)
mutated_mod['func_3360'] = func_3360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mod.get_global_var('func_3359')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_3409 = func_3359_call()
call_3410 = func_3359_call()
output = call_3409
output2 = call_3410
func_3418 = relay.Function([], output)
mod['func_3418'] = func_3418
mod = relay.transform.InferType()(mod)
mutated_mod['func_3418'] = func_3418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mutated_mod.get_global_var('func_3418')
call_3419 = func_3418_call()
output = call_3419
func_3420 = relay.Function([], output)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3212_call = mod.get_global_var('func_3212')
func_3214_call = mutated_mod.get_global_var('func_3214')
call_3458 = relay.TupleGetItem(func_3212_call(), 1)
call_3459 = relay.TupleGetItem(func_3214_call(), 1)
output = relay.Tuple([call_3458,])
output2 = relay.Tuple([call_3459,])
func_3463 = relay.Function([], output)
mod['func_3463'] = func_3463
mod = relay.transform.InferType()(mod)
output = func_3463()
func_3464 = relay.Function([], output)
mutated_mod['func_3464'] = func_3464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3463_call = mod.get_global_var('func_3463')
func_3464_call = mutated_mod.get_global_var('func_3464')
call_3465 = relay.TupleGetItem(func_3463_call(), 0)
call_3466 = relay.TupleGetItem(func_3464_call(), 0)
uop_3472 = relay.atan(call_3465.astype('float64')) # shape=(8, 14, 10)
uop_3474 = relay.atan(call_3466.astype('float64')) # shape=(8, 14, 10)
func_2510_call = mod.get_global_var('func_2510')
func_2513_call = mutated_mod.get_global_var('func_2513')
const_3483 = relay.const([[-9.889260,-8.839676,-6.239506,-2.042408,-2.892225,1.959106,4.144595,-2.483845,3.856438,-5.375822,9.596042,-8.410302,-3.086936,-7.842433,-4.120579,-8.544554,2.050359,-3.022587,9.248855,-5.794021,-1.231747,-3.627649,-6.409736,-8.383629,8.174671,5.770348,-4.305474,-1.892113,6.028407,-0.483531,-0.651846,-0.666961,9.035849,6.677429,-8.115205,-0.474395,-7.212579,-1.735435,-3.372629,-4.363551,-6.996864,-5.772463,2.245697,6.901027,6.707835,-3.277470,-0.340456,-6.289929,-5.798674,-5.752347,9.781407,5.314954],[1.817398,-2.930776,-7.285820,-5.642319,-7.160476,8.261834,0.524408,-7.599870,-4.289312,-7.728949,-2.017648,-6.033246,5.582963,8.924504,-9.438998,-6.794150,-2.568566,6.758201,1.116002,0.395987,-3.249716,-4.577980,9.332017,-4.711187,2.995000,-7.719632,5.280443,-6.894141,4.637981,-2.241839,-9.805468,-9.460272,2.431567,9.471003,7.707957,7.498006,-7.007249,0.284831,-8.841826,0.767920,-1.814450,4.740958,3.008237,-2.225933,7.481168,-7.476902,5.202725,2.368799,-0.989687,-9.529624,4.507193,8.424390],[6.552716,-3.080061,-2.669401,2.257463,7.082677,4.928232,8.140973,-3.406687,-5.609737,-0.263585,9.558944,-8.598041,8.250257,8.281598,-2.403137,-6.421033,7.724920,-5.622754,-8.291235,-5.795623,-3.326428,-5.544252,-0.470734,7.637377,1.576065,-0.842193,1.751889,-0.195666,2.280945,2.099833,-0.309680,2.053651,-8.464251,-7.624002,-3.892477,4.718630,-6.078601,-1.875288,-4.863631,4.428145,1.355027,-7.582283,-7.597384,5.286901,-1.401447,-4.592993,-6.829650,-0.960897,1.738523,-0.907554,4.028036,-5.498235],[0.557578,-1.276196,-3.885388,-3.887083,-2.153774,-0.665438,8.594803,-3.571083,3.010220,6.197571,4.518894,-3.629722,-1.649390,-6.877719,-5.262127,7.434057,2.725113,9.715962,2.075286,0.138809,-3.167247,-6.631655,-2.191009,7.097517,5.730852,2.792181,-3.786680,6.537102,-9.644945,9.592795,1.670012,9.355992,-9.758720,-8.432844,-3.759448,8.331642,-7.833432,-9.859615,6.846542,-6.505981,-0.151163,8.918115,5.782940,1.094148,-3.604589,4.863064,7.980159,-9.882682,1.234717,3.829712,-5.021412,3.613925],[5.865614,3.323715,6.707680,7.231996,-1.734153,3.306483,-5.976913,3.614504,9.158999,-8.889973,8.404846,-1.349674,9.781663,-1.601111,6.126717,-0.145916,-6.250589,4.741643,6.734369,4.663209,5.923357,-1.101926,-3.899575,-3.282837,-5.785679,-0.526629,8.865712,-0.623008,0.851448,-2.943580,-1.203458,4.973714,6.430259,3.866626,9.978860,-1.244589,7.348163,-4.650710,-2.759725,3.310841,0.091874,1.892089,-3.935063,-6.659445,-5.554171,-4.029743,3.940892,0.243450,-9.279007,-3.800112,-8.635512,-2.766442],[1.499965,5.833972,8.270090,-6.863046,-1.467074,5.500814,6.285978,-2.051271,2.368991,6.641236,-6.785584,9.612657,5.710021,2.308371,-8.689269,8.035835,-3.744027,0.750533,0.168438,5.529327,7.864408,-3.388652,-9.520146,4.752865,-9.058817,-3.213077,2.888193,4.330311,6.462395,-9.325626,0.967991,2.523352,-6.690533,5.802087,-2.303791,-3.331176,-4.301912,9.442964,3.405660,-6.348045,3.971423,5.802068,-7.805220,6.111565,5.802127,7.839704,2.008442,-3.976650,5.630872,4.147066,-0.096573,-6.857622]], dtype = "float32")#candidate|3483|(6, 52)|const|float32
call_3482 = relay.TupleGetItem(func_2510_call(relay.reshape(const_3483.astype('float32'), [312,])), 1)
call_3484 = relay.TupleGetItem(func_2513_call(relay.reshape(const_3483.astype('float32'), [312,])), 1)
func_2510_call = mod.get_global_var('func_2510')
func_2513_call = mutated_mod.get_global_var('func_2513')
call_3485 = relay.TupleGetItem(func_2510_call(relay.reshape(const_3483.astype('float32'), [312,])), 2)
call_3486 = relay.TupleGetItem(func_2513_call(relay.reshape(const_3483.astype('float32'), [312,])), 2)
bop_3487 = relay.maximum(uop_3472.astype('uint16'), relay.reshape(call_3465.astype('uint16'), relay.shape_of(uop_3472))) # shape=(8, 14, 10)
bop_3490 = relay.maximum(uop_3474.astype('uint16'), relay.reshape(call_3466.astype('uint16'), relay.shape_of(uop_3474))) # shape=(8, 14, 10)
output = relay.Tuple([call_3482,const_3483,call_3485,bop_3487,])
output2 = relay.Tuple([call_3484,const_3483,call_3486,bop_3490,])
func_3492 = relay.Function([], output)
mod['func_3492'] = func_3492
mod = relay.transform.InferType()(mod)
mutated_mod['func_3492'] = func_3492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3492_call = mutated_mod.get_global_var('func_3492')
call_3493 = func_3492_call()
output = call_3493
func_3494 = relay.Function([], output)
mutated_mod['func_3494'] = func_3494
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3503 = relay.var("var_3503", dtype = "float64", shape = (5, 13, 12))#candidate|3503|(5, 13, 12)|var|float64
const_3504 = relay.const([[[8.497680,-7.886373,1.926480,7.563695,-5.498298,8.456417,-1.544083,-5.980251,-6.306759,-0.923803,-4.826546,9.669573],[5.788814,2.665324,9.148222,0.433738,-1.555853,-6.306580,8.765929,-6.460305,-8.613535,2.254645,-1.511861,-2.824616],[3.875425,0.356095,-6.925538,2.253930,-1.486469,5.722719,-3.442374,-5.402141,6.384687,-8.405432,6.672209,-7.791172],[-2.983096,-9.898782,-4.480948,4.433165,1.012909,2.373217,4.553506,7.965490,9.452158,1.890813,0.897089,-9.909050],[-1.715592,-6.793683,9.162370,-7.351658,-7.025363,-8.567290,0.873386,-9.535160,-0.991233,-0.299880,9.437659,-3.194754],[-9.258594,-2.464086,3.716433,-2.776428,4.425263,6.120522,-5.458267,-0.445934,-4.807685,0.992761,0.750630,6.936010],[5.103867,8.119396,0.415589,8.217540,-8.843714,-0.404350,-8.763991,4.612231,0.597942,0.244252,-9.885533,-6.734378],[-5.912676,-2.115554,9.159157,-5.990468,2.836521,4.086194,6.387867,9.100634,-4.377099,5.855891,-4.519565,-6.644069],[-4.175497,9.788470,-5.201771,0.206355,8.587074,-9.207072,3.639264,9.251868,-1.730002,-2.066889,4.447202,9.285143],[5.190973,5.988152,-1.107885,5.442707,4.229652,9.372274,-5.883645,-5.935257,9.644829,-4.329991,3.808932,5.098893],[6.229406,7.656650,0.292297,-1.971590,-1.574973,0.814225,-2.457406,7.466924,3.052376,3.174597,9.204840,-8.391531],[-0.507972,-9.984913,-6.379845,2.418262,9.681149,2.458010,-4.167416,2.666436,9.668269,8.407379,4.677416,7.365662],[3.027747,-2.544372,-9.182152,5.370619,9.190478,4.536836,-9.474046,2.668070,3.989763,-2.549089,8.516027,-7.164902]],[[-4.513026,-8.113211,-7.936942,4.481406,-9.294279,9.261818,-5.540896,2.541714,-2.266728,4.287715,1.240554,-0.870624],[8.493045,-1.655030,-6.048351,8.803870,-4.164424,-5.703095,6.711330,0.115872,5.335115,1.728991,7.184246,7.023432],[5.743648,-7.444672,-1.958915,0.533730,-6.481829,-2.637998,4.995443,6.646227,7.018576,-5.138982,9.374775,-3.264264],[-7.605801,-7.491736,-8.285550,3.292065,2.915291,-2.941338,-4.784507,7.093554,-0.960558,6.520710,-6.445208,8.004743],[-2.372172,-8.685731,4.741629,-9.493855,-2.864959,-1.778196,9.075948,-9.650726,9.151168,-6.838536,6.170919,-4.411982],[7.805362,0.733628,9.559266,0.843080,-4.560906,2.408351,-8.807569,-7.638682,9.432078,6.369548,-6.190706,7.586003],[-8.254163,-1.618317,1.187401,8.285360,-3.308974,-3.129731,-7.615449,-4.797919,-0.269793,-9.399822,2.934146,5.513856],[7.771784,2.800554,0.821870,-7.675994,-2.119230,8.892628,0.168019,-5.689244,6.458318,0.735014,-9.882626,-3.807836],[-5.624372,4.060380,9.183911,-5.054824,0.778065,7.480993,-1.070797,2.460770,-4.378506,-6.138240,6.433148,1.819948],[-5.675152,-4.999117,-6.453136,0.610783,-8.413038,3.547256,2.495669,-3.511035,5.532061,5.806297,4.532164,0.670773],[0.534730,-0.906822,-1.992993,4.020479,-9.727163,-4.204075,4.985400,7.165085,-6.608906,0.804872,-9.675023,4.765201],[0.985689,3.684045,1.088787,-9.703567,1.257143,6.777547,5.855468,-3.983664,4.237373,-3.146736,-4.181826,-2.404152],[-9.024040,-6.566297,2.170472,6.582730,0.454562,-7.259786,0.378879,3.532344,9.012709,-2.953336,-7.007156,-8.723912]],[[9.935396,-6.872363,6.176856,6.419067,-3.397188,-4.977666,8.166267,6.190911,5.618718,7.824533,-0.035926,8.678327],[9.134480,-1.241421,-6.795505,8.363635,-1.258742,1.764817,-9.721615,9.313219,-3.889699,2.352368,3.000189,-3.662246],[-2.912233,5.157917,5.069215,-5.905552,8.129948,-3.518229,6.015085,1.554482,8.923509,8.898458,1.174307,-8.083448],[4.644397,4.634467,-7.021241,4.004101,1.209925,-6.587920,5.935995,-6.204469,4.474216,-3.179407,-0.908655,-6.640643],[-9.850360,-7.811654,2.274813,3.290295,-7.998891,6.114698,8.518759,9.312842,-9.508212,1.373072,-4.843440,-2.659326],[-4.855631,-6.993728,-8.265328,-7.465910,1.214546,6.915842,3.082150,9.565289,6.593262,7.678462,7.937522,-0.369949],[-1.072368,3.722885,8.957138,-9.244741,-7.088238,-7.336325,-0.361030,3.015729,2.481726,-6.744466,5.919420,-9.491806],[-8.963713,4.470367,-8.786017,9.220982,1.942620,2.147462,-1.952578,-7.967935,6.364989,-4.972397,2.978476,2.329460],[-1.859870,-0.302913,0.426930,-1.093818,-1.876091,1.282556,2.207708,2.498544,3.353625,4.255450,-6.223182,-6.235135],[1.577612,9.201677,-1.838980,1.754923,-8.391623,-2.976507,7.333780,-2.309711,9.126486,-0.812881,-7.897883,4.780265],[9.731933,-1.764136,0.688296,5.045586,7.065451,1.526307,9.250396,-7.796907,-1.929979,7.279708,8.241007,1.027412],[0.255032,-8.377643,6.025967,9.712497,-0.301200,7.506034,-0.894756,-1.323543,6.303939,4.004272,1.821843,1.262043],[-8.106921,3.035689,-7.855741,-0.701631,-2.780002,5.979574,0.998009,-4.327849,-9.654668,6.917754,-5.363893,-8.076629]],[[4.399925,-1.882147,3.462512,7.328809,-5.924429,-7.051881,2.204207,-4.819267,7.400797,-3.678931,-2.334353,-5.372950],[-7.776736,0.394182,-3.224166,-1.906418,8.810726,-1.925989,-4.503356,8.461048,-4.624587,8.560919,-6.726290,2.063854],[-0.946783,-6.271448,5.087648,4.032884,-5.424773,-7.002655,0.144082,7.702526,-0.167212,9.272608,1.828893,3.244734],[-2.993257,2.355178,3.525115,-4.718312,-3.602087,-7.603431,-5.902234,8.120348,2.434196,6.132663,5.692097,4.022338],[-0.564186,-7.745324,5.187448,9.175516,4.766373,2.073718,4.852659,-4.968990,-7.397069,3.581554,-7.178795,-4.991661],[5.797095,-4.082533,-9.060339,-6.611220,8.419316,-1.246791,-8.935548,-7.595320,-9.097800,-6.132816,-4.222029,-2.063298],[-5.288156,3.910261,-0.777368,-4.165665,7.217095,-9.183420,-4.417705,-1.049885,-8.604364,9.633814,-4.584910,-2.468608],[0.954311,-4.293997,8.384332,-7.671917,8.143339,-1.452085,5.300381,1.754958,-3.146932,-4.178454,-0.127375,-3.823765],[1.692485,5.254028,3.130921,9.270159,9.736593,-7.770753,-8.942482,-8.624074,-5.441342,5.763268,1.137249,-6.554102],[1.585295,-6.949360,8.188663,-9.164359,-5.720022,-9.644897,7.101305,-1.633353,-2.860596,4.532914,-7.120481,-5.711977],[-6.220239,-0.118566,-2.545882,0.904684,-7.472143,2.369744,-7.409282,-8.140060,9.750644,6.295497,-7.131440,1.850739],[-3.424119,3.806158,-1.850643,-6.088456,-7.266842,-4.423579,9.553876,-7.426546,-4.268362,-0.627305,0.141842,7.753487],[9.940407,4.890063,2.535877,-9.535757,4.808973,-7.180610,7.392759,-4.849797,9.007817,-1.279786,8.210988,-3.919425]],[[-2.912941,-9.479409,-1.393416,7.594067,-3.732987,9.579158,3.257790,-0.260525,-6.795181,1.002981,9.236846,9.928117],[-8.411253,5.866407,-9.220487,0.158899,-2.766008,-4.034399,-3.994478,8.655858,-9.726839,-6.329995,-3.583487,-9.357257],[8.296866,1.255540,0.211245,5.632713,-1.600953,0.543868,7.365909,-8.594631,9.312723,-2.835699,-5.626146,-8.080083],[-8.719512,-9.144781,7.442003,1.909487,-1.493975,3.356791,4.526889,-9.871919,-4.925859,-6.886047,-1.940083,1.322266],[4.945595,6.674135,7.975569,-0.432210,-7.527222,4.111687,5.287164,-0.918162,4.013934,-4.239546,0.142507,-2.391355],[-4.177493,0.275531,5.645147,-2.726159,-1.275619,-8.149514,-4.136937,1.777333,-5.243691,-6.042313,-0.775022,0.474289],[7.567112,-8.059464,-8.326257,-3.935446,-9.468417,-5.988682,-6.533625,-5.824729,-8.815082,8.638423,-8.823054,-0.725339],[9.024736,-5.621369,6.074581,2.901974,0.155054,0.428622,-7.247074,5.934672,6.207085,3.891971,-9.582425,-8.005223],[-8.575435,3.997629,9.269955,9.695857,7.884398,-5.637493,-2.216164,3.578799,7.758767,8.210311,-3.967262,-9.218232],[-8.895219,8.247975,-8.161990,-0.283320,8.139767,2.945413,3.541147,2.061566,-0.658847,5.302336,0.879809,8.157631],[-8.043200,1.627681,1.498426,-8.204812,6.808727,-0.869501,-0.398631,-7.407500,6.688219,-1.637159,1.728490,9.760931],[4.871834,-2.196469,9.924382,6.867401,-0.799166,-3.917785,4.538040,-5.105593,-9.422318,-4.439632,3.749826,7.024315],[-7.507911,7.394010,7.635424,0.987475,3.413405,-3.468839,4.461879,-5.643923,-6.828012,0.769213,-8.920915,-8.521331]]], dtype = "float64")#candidate|3504|(5, 13, 12)|const|float64
bop_3505 = relay.greater_equal(var_3503.astype('bool'), relay.reshape(const_3504.astype('bool'), relay.shape_of(var_3503))) # shape=(5, 13, 12)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_3511 = relay.TupleGetItem(func_1803_call(), 0)
call_3512 = relay.TupleGetItem(func_1805_call(), 0)
func_3418_call = mod.get_global_var('func_3418')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_3516 = func_3418_call()
call_3517 = func_3418_call()
uop_3523 = relay.acosh(var_3503.astype('float64')) # shape=(5, 13, 12)
func_1588_call = mod.get_global_var('func_1588')
func_1590_call = mutated_mod.get_global_var('func_1590')
call_3527 = relay.TupleGetItem(func_1588_call(relay.reshape(call_3511.astype('float32'), [312, 1])), 2)
call_3528 = relay.TupleGetItem(func_1590_call(relay.reshape(call_3511.astype('float32'), [312, 1])), 2)
output = relay.Tuple([bop_3505,call_3511,call_3516,uop_3523,call_3527,])
output2 = relay.Tuple([bop_3505,call_3512,call_3517,uop_3523,call_3528,])
func_3536 = relay.Function([var_3503,], output)
mod['func_3536'] = func_3536
mod = relay.transform.InferType()(mod)
var_3537 = relay.var("var_3537", dtype = "float64", shape = (5, 13, 12))#candidate|3537|(5, 13, 12)|var|float64
output = func_3536(var_3537)
func_3538 = relay.Function([var_3537], output)
mutated_mod['func_3538'] = func_3538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_3540 = func_3418_call()
call_3541 = func_3418_call()
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_3557 = relay.TupleGetItem(func_1556_call(), 0)
call_3558 = relay.TupleGetItem(func_1557_call(), 0)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_3561 = relay.TupleGetItem(func_1769_call(), 1)
call_3562 = relay.TupleGetItem(func_1771_call(), 1)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_3568 = relay.TupleGetItem(func_2162_call(), 0)
call_3569 = relay.TupleGetItem(func_2163_call(), 0)
output = relay.Tuple([call_3540,call_3557,call_3561,call_3568,])
output2 = relay.Tuple([call_3541,call_3558,call_3562,call_3569,])
func_3571 = relay.Function([], output)
mod['func_3571'] = func_3571
mod = relay.transform.InferType()(mod)
output = func_3571()
func_3572 = relay.Function([], output)
mutated_mod['func_3572'] = func_3572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2714_call = mod.get_global_var('func_2714')
func_2715_call = mutated_mod.get_global_var('func_2715')
call_3663 = func_2714_call()
call_3664 = func_2714_call()
output = call_3663
output2 = call_3664
func_3692 = relay.Function([], output)
mod['func_3692'] = func_3692
mod = relay.transform.InferType()(mod)
output = func_3692()
func_3693 = relay.Function([], output)
mutated_mod['func_3693'] = func_3693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_3766 = relay.TupleGetItem(func_1912_call(), 2)
call_3767 = relay.TupleGetItem(func_1914_call(), 2)
output = relay.Tuple([call_3766,])
output2 = relay.Tuple([call_3767,])
func_3789 = relay.Function([], output)
mod['func_3789'] = func_3789
mod = relay.transform.InferType()(mod)
output = func_3789()
func_3790 = relay.Function([], output)
mutated_mod['func_3790'] = func_3790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3047_call = mod.get_global_var('func_3047')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_3820 = relay.TupleGetItem(func_3047_call(), 0)
call_3821 = relay.TupleGetItem(func_3048_call(), 0)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_3825 = relay.TupleGetItem(func_1769_call(), 2)
call_3826 = relay.TupleGetItem(func_1771_call(), 2)
const_3829 = relay.const([[[4,9,2,7,9,-1,-5,9,-2,-7],[-8,10,8,-3,4,6,7,7,9,5],[5,4,-3,-9,6,7,1,-5,1,-5],[8,-4,-9,4,-6,-7,7,1,6,4],[-6,-5,8,5,8,4,-3,2,-1,7],[-9,8,-6,7,-1,-4,-4,3,9,-1],[9,-6,8,-2,6,8,-6,3,-7,5],[-1,-4,-10,-7,6,9,-7,-6,2,-4],[9,-4,-10,8,5,-5,4,1,8,-4],[-8,-10,7,8,5,-8,5,1,10,3],[3,-4,-7,3,-5,-2,2,-5,-7,10],[8,8,1,7,9,7,-7,-10,-7,2],[4,2,5,8,-4,-5,6,6,-3,9],[4,-3,-8,-7,-10,7,-2,-1,-10,-10]],[[5,7,-9,1,5,-1,9,-1,-10,3],[7,3,1,-10,-3,5,6,-1,4,-6],[-5,1,-2,2,1,10,-5,9,9,7],[10,9,-6,2,2,3,4,1,4,-7],[-9,3,2,-10,-3,-10,-2,10,9,10],[-7,-1,6,-6,5,5,2,8,2,-4],[8,8,3,8,10,-5,2,8,10,-8],[9,1,-3,-5,10,10,1,7,-5,-8],[-4,2,1,-2,7,-7,5,-8,-8,3],[-10,3,-10,7,-7,2,2,-7,-7,-5],[1,1,-10,2,1,6,-8,-3,1,-6],[9,-8,-6,-3,4,-9,9,-10,-8,9],[-6,1,3,-2,7,1,-8,8,-5,-8],[8,5,7,8,-8,7,1,-7,5,7]],[[9,-10,10,-2,-9,-6,-6,-6,-6,8],[-1,-7,-4,-7,6,-1,-3,-4,8,-7],[-6,6,4,5,-6,4,-10,2,-7,-1],[4,-8,2,1,9,7,-1,-7,4,-6],[9,-2,1,2,-4,1,-4,6,-10,-6],[-4,-4,5,-1,7,1,-5,4,-6,4],[-7,9,-3,-9,-1,3,1,2,3,7],[9,4,1,-2,4,9,2,-5,3,9],[1,1,1,10,-7,2,4,-1,-5,2],[-10,1,8,-6,-1,3,9,6,7,2],[2,1,-1,1,-5,7,3,-7,5,-10],[-10,-10,8,9,-3,-1,-6,-1,5,4],[4,-5,-1,-7,-10,3,-3,9,3,9],[8,9,4,-10,1,-9,5,-1,8,3]],[[7,10,-10,-3,8,9,4,7,-7,7],[2,2,-1,4,-2,-9,-4,1,9,-9],[8,10,-5,1,5,1,-5,-5,-7,-6],[-7,-8,-4,-6,-2,10,2,-3,-9,10],[-4,3,5,4,8,-9,-4,7,7,-3],[-10,-1,2,-1,10,-5,4,2,8,9],[7,-3,4,-1,5,10,-8,10,-6,-1],[4,-9,-5,-6,-10,-9,3,-9,1,-10],[5,-6,2,3,6,-2,-1,9,-5,-7],[9,1,-7,3,-10,8,4,10,-9,3],[6,-8,-8,3,1,6,7,6,-8,3],[1,-5,5,-8,-10,-2,6,-5,6,-8],[7,8,3,-7,-2,-1,2,-5,-3,1],[-6,10,-2,6,3,6,-2,-6,-8,-8]],[[-5,-3,-6,4,-3,-5,-8,1,-1,10],[5,-4,10,-3,-2,1,1,6,4,9],[7,-8,-10,-6,10,-5,-10,1,10,8],[-7,1,5,-5,7,10,-1,-10,-9,-4],[-2,5,9,-2,2,-4,1,4,3,8],[-5,-8,7,9,-4,-7,1,8,8,10],[-4,-8,10,-2,1,-6,8,-7,2,3],[7,2,-1,-10,2,10,4,2,10,-10],[-6,1,8,9,2,-6,1,8,10,-3],[-8,10,-3,-8,8,3,-4,-8,-2,4],[8,-2,-8,10,-6,2,-8,-8,5,-3],[5,7,-2,-4,3,-8,-10,7,-1,-7],[2,3,-2,-4,-10,-9,4,-6,4,-1],[-10,5,1,9,1,-9,3,-6,6,1]],[[-6,10,-10,-6,-8,9,-10,-7,8,-1],[2,-5,-5,-2,-2,6,5,8,4,-10],[-5,-10,5,5,5,-4,7,2,2,-2],[6,2,4,7,-6,-10,-5,-5,2,-4],[6,-4,7,7,-9,-4,9,-8,-6,10],[-3,-4,-5,-1,-10,3,-4,1,10,-3],[-8,-6,2,1,3,9,-4,-6,-1,5],[3,7,5,-1,7,6,2,4,9,2],[-7,-8,4,-1,1,8,5,1,5,-5],[-5,-2,6,-1,-3,7,-5,-4,-6,-8],[2,9,1,-9,2,-3,-6,6,-2,9],[9,7,8,5,-6,-1,8,8,-1,-10],[-3,-2,9,-3,4,-8,5,-8,-9,-6],[-5,5,-8,5,-2,-10,7,3,9,-8]],[[-9,7,4,-6,-10,7,-1,1,5,-7],[-2,-9,-3,6,10,5,10,3,7,6],[6,-3,4,-6,-1,-6,-4,-1,-9,6],[-10,-9,5,6,-3,-9,6,6,7,10],[5,-8,-1,3,-5,9,2,-6,2,-8],[6,4,1,-3,1,4,-9,6,-3,-10],[-2,4,7,-10,5,5,-7,-3,-10,7],[-10,-1,5,-7,-8,9,-5,3,-6,-10],[5,10,4,-10,-10,8,-10,-8,-6,-5],[3,-2,6,10,-10,-3,-8,7,-6,8],[8,5,5,-4,8,5,3,8,5,-1],[10,2,-7,-10,7,-9,4,-4,-7,9],[-6,-7,-2,-8,6,-1,-5,4,3,-7],[4,7,1,-6,-8,6,-9,-4,-1,-7]],[[-6,-3,3,-5,1,-9,7,2,7,-6],[5,10,-6,-5,9,-4,-2,5,4,4],[-9,10,-6,2,2,-8,-10,1,3,3],[-9,6,-3,9,-3,3,-5,-8,7,6],[-9,-6,-5,7,4,1,-8,-7,1,8],[-10,-4,6,-7,3,2,-10,-5,7,2],[-1,-5,3,9,7,-6,8,3,3,7],[-3,-1,1,-7,-5,2,-5,6,10,-10],[5,-5,5,7,7,-5,6,5,-2,-8],[3,-5,-10,4,8,-10,-9,6,-2,-3],[8,1,-6,3,-9,4,-4,10,-10,5],[-10,1,-9,-5,-9,-4,-8,2,1,1],[10,-4,6,8,2,-6,-8,4,-3,10],[9,10,9,1,-9,2,10,4,1,2]]], dtype = "int8")#candidate|3829|(8, 14, 10)|const|int8
bop_3830 = relay.minimum(call_3820.astype('float64'), relay.reshape(const_3829.astype('float64'), relay.shape_of(call_3820))) # shape=(8, 14, 10)
bop_3833 = relay.minimum(call_3821.astype('float64'), relay.reshape(const_3829.astype('float64'), relay.shape_of(call_3821))) # shape=(8, 14, 10)
output = relay.Tuple([call_3825,bop_3830,])
output2 = relay.Tuple([call_3826,bop_3833,])
func_3841 = relay.Function([], output)
mod['func_3841'] = func_3841
mod = relay.transform.InferType()(mod)
output = func_3841()
func_3842 = relay.Function([], output)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_3843 = relay.TupleGetItem(func_1803_call(), 0)
call_3844 = relay.TupleGetItem(func_1805_call(), 0)
output = relay.Tuple([call_3843,])
output2 = relay.Tuple([call_3844,])
func_3870 = relay.Function([], output)
mod['func_3870'] = func_3870
mod = relay.transform.InferType()(mod)
output = func_3870()
func_3871 = relay.Function([], output)
mutated_mod['func_3871'] = func_3871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_3900 = relay.TupleGetItem(func_1556_call(), 0)
call_3901 = relay.TupleGetItem(func_1557_call(), 0)
output = relay.Tuple([call_3900,])
output2 = relay.Tuple([call_3901,])
func_3907 = relay.Function([], output)
mod['func_3907'] = func_3907
mod = relay.transform.InferType()(mod)
mutated_mod['func_3907'] = func_3907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mutated_mod.get_global_var('func_3907')
call_3908 = func_3907_call()
output = call_3908
func_3909 = relay.Function([], output)
mutated_mod['func_3909'] = func_3909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_3935 = relay.TupleGetItem(func_3789_call(), 0)
call_3936 = relay.TupleGetItem(func_3790_call(), 0)
func_3571_call = mod.get_global_var('func_3571')
func_3572_call = mutated_mod.get_global_var('func_3572')
call_3943 = relay.TupleGetItem(func_3571_call(), 0)
call_3944 = relay.TupleGetItem(func_3572_call(), 0)
uop_3947 = relay.acosh(call_3935.astype('float64')) # shape=(6, 13, 4)
uop_3949 = relay.acosh(call_3936.astype('float64')) # shape=(6, 13, 4)
output = relay.Tuple([call_3943,uop_3947,])
output2 = relay.Tuple([call_3944,uop_3949,])
func_3950 = relay.Function([], output)
mod['func_3950'] = func_3950
mod = relay.transform.InferType()(mod)
mutated_mod['func_3950'] = func_3950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mutated_mod.get_global_var('func_3950')
call_3951 = func_3950_call()
output = call_3951
func_3952 = relay.Function([], output)
mutated_mod['func_3952'] = func_3952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_3956 = relay.TupleGetItem(func_1803_call(), 0)
call_3957 = relay.TupleGetItem(func_1805_call(), 0)
func_1964_call = mod.get_global_var('func_1964')
func_1967_call = mutated_mod.get_global_var('func_1967')
var_3959 = relay.var("var_3959", dtype = "uint32", shape = (363,))#candidate|3959|(363,)|var|uint32
call_3958 = relay.TupleGetItem(func_1964_call(relay.reshape(var_3959.astype('uint32'), [363,])), 2)
call_3960 = relay.TupleGetItem(func_1967_call(relay.reshape(var_3959.astype('uint32'), [363,])), 2)
output = relay.Tuple([call_3956,call_3958,var_3959,])
output2 = relay.Tuple([call_3957,call_3960,var_3959,])
func_3978 = relay.Function([var_3959,], output)
mod['func_3978'] = func_3978
mod = relay.transform.InferType()(mod)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3979 = relay.var("var_3979", dtype = "uint32", shape = (363,))#candidate|3979|(363,)|var|uint32
func_3978_call = mutated_mod.get_global_var('func_3978')
call_3980 = func_3978_call(var_3979)
output = call_3980
func_3981 = relay.Function([var_3979], output)
mutated_mod['func_3981'] = func_3981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4015 = relay.var("var_4015", dtype = "float64", shape = (12, 7, 13))#candidate|4015|(12, 7, 13)|var|float64
uop_4016 = relay.sinh(var_4015.astype('float64')) # shape=(12, 7, 13)
output = uop_4016
output2 = uop_4016
func_4031 = relay.Function([var_4015,], output)
mod['func_4031'] = func_4031
mod = relay.transform.InferType()(mod)
var_4032 = relay.var("var_4032", dtype = "float64", shape = (12, 7, 13))#candidate|4032|(12, 7, 13)|var|float64
output = func_4031(var_4032)
func_4033 = relay.Function([var_4032], output)
mutated_mod['func_4033'] = func_4033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_4060 = relay.TupleGetItem(func_1912_call(), 0)
call_4061 = relay.TupleGetItem(func_1914_call(), 0)
output = relay.Tuple([call_4060,])
output2 = relay.Tuple([call_4061,])
func_4064 = relay.Function([], output)
mod['func_4064'] = func_4064
mod = relay.transform.InferType()(mod)
output = func_4064()
func_4065 = relay.Function([], output)
mutated_mod['func_4065'] = func_4065
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4075 = relay.var("var_4075", dtype = "float32", shape = (6, 12, 5))#candidate|4075|(6, 12, 5)|var|float32
uop_4076 = relay.exp(var_4075.astype('float32')) # shape=(6, 12, 5)
output = uop_4076
output2 = uop_4076
func_4081 = relay.Function([var_4075,], output)
mod['func_4081'] = func_4081
mod = relay.transform.InferType()(mod)
mutated_mod['func_4081'] = func_4081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4082 = relay.var("var_4082", dtype = "float32", shape = (6, 12, 5))#candidate|4082|(6, 12, 5)|var|float32
func_4081_call = mutated_mod.get_global_var('func_4081')
call_4083 = func_4081_call(var_4082)
output = call_4083
func_4084 = relay.Function([var_4082], output)
mutated_mod['func_4084'] = func_4084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4112 = relay.var("var_4112", dtype = "bool", shape = ())#candidate|4112|()|var|bool
var_4113 = relay.var("var_4113", dtype = "bool", shape = (14, 4, 8))#candidate|4113|(14, 4, 8)|var|bool
bop_4114 = relay.logical_or(var_4112.astype('bool'), var_4113.astype('bool')) # shape=(14, 4, 8)
output = bop_4114
output2 = bop_4114
func_4123 = relay.Function([var_4112,var_4113,], output)
mod['func_4123'] = func_4123
mod = relay.transform.InferType()(mod)
mutated_mod['func_4123'] = func_4123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4123_call = mutated_mod.get_global_var('func_4123')
var_4125 = relay.var("var_4125", dtype = "bool", shape = ())#candidate|4125|()|var|bool
var_4126 = relay.var("var_4126", dtype = "bool", shape = (14, 4, 8))#candidate|4126|(14, 4, 8)|var|bool
call_4124 = func_4123_call(var_4125,var_4126,)
output = call_4124
func_4127 = relay.Function([var_4125,var_4126,], output)
mutated_mod['func_4127'] = func_4127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_4143 = relay.TupleGetItem(func_3950_call(), 1)
call_4144 = relay.TupleGetItem(func_3952_call(), 1)
func_3418_call = mod.get_global_var('func_3418')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_4148 = func_3418_call()
call_4149 = func_3418_call()
bop_4168 = relay.mod(call_4148.astype('float64'), relay.reshape(call_4143.astype('float64'), relay.shape_of(call_4148))) # shape=(6, 13, 4)
bop_4171 = relay.mod(call_4149.astype('float64'), relay.reshape(call_4144.astype('float64'), relay.shape_of(call_4149))) # shape=(6, 13, 4)
func_2204_call = mod.get_global_var('func_2204')
func_2205_call = mutated_mod.get_global_var('func_2205')
call_4178 = func_2204_call()
call_4179 = func_2204_call()
output = relay.Tuple([bop_4168,call_4178,])
output2 = relay.Tuple([bop_4171,call_4179,])
func_4180 = relay.Function([], output)
mod['func_4180'] = func_4180
mod = relay.transform.InferType()(mod)
output = func_4180()
func_4181 = relay.Function([], output)
mutated_mod['func_4181'] = func_4181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_4200 = relay.TupleGetItem(func_3950_call(), 1)
call_4201 = relay.TupleGetItem(func_3952_call(), 1)
func_3335_call = mod.get_global_var('func_3335')
func_3338_call = mutated_mod.get_global_var('func_3338')
call_4206 = relay.TupleGetItem(func_3335_call(relay.reshape(call_4200.astype('float64'), [3, 104]), relay.reshape(call_4200.astype('float64'), [3, 104]), ), 3)
call_4207 = relay.TupleGetItem(func_3338_call(relay.reshape(call_4200.astype('float64'), [3, 104]), relay.reshape(call_4200.astype('float64'), [3, 104]), ), 3)
output = relay.Tuple([call_4200,call_4206,])
output2 = relay.Tuple([call_4201,call_4207,])
func_4208 = relay.Function([], output)
mod['func_4208'] = func_4208
mod = relay.transform.InferType()(mod)
output = func_4208()
func_4209 = relay.Function([], output)
mutated_mod['func_4209'] = func_4209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2714_call = mod.get_global_var('func_2714')
func_2715_call = mutated_mod.get_global_var('func_2715')
call_4248 = func_2714_call()
call_4249 = func_2714_call()
output = call_4248
output2 = call_4249
func_4256 = relay.Function([], output)
mod['func_4256'] = func_4256
mod = relay.transform.InferType()(mod)
output = func_4256()
func_4257 = relay.Function([], output)
mutated_mod['func_4257'] = func_4257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_4280 = relay.TupleGetItem(func_2937_call(), 4)
call_4281 = relay.TupleGetItem(func_2939_call(), 4)
func_2297_call = mod.get_global_var('func_2297')
func_2299_call = mutated_mod.get_global_var('func_2299')
call_4286 = relay.TupleGetItem(func_2297_call(), 0)
call_4287 = relay.TupleGetItem(func_2299_call(), 0)
func_2714_call = mod.get_global_var('func_2714')
func_2715_call = mutated_mod.get_global_var('func_2715')
call_4293 = func_2714_call()
call_4294 = func_2714_call()
func_2714_call = mod.get_global_var('func_2714')
func_2715_call = mutated_mod.get_global_var('func_2715')
call_4313 = func_2714_call()
call_4314 = func_2714_call()
output = relay.Tuple([call_4280,call_4286,call_4293,call_4313,])
output2 = relay.Tuple([call_4281,call_4287,call_4294,call_4314,])
func_4316 = relay.Function([], output)
mod['func_4316'] = func_4316
mod = relay.transform.InferType()(mod)
output = func_4316()
func_4317 = relay.Function([], output)
mutated_mod['func_4317'] = func_4317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3571_call = mod.get_global_var('func_3571')
func_3572_call = mutated_mod.get_global_var('func_3572')
call_4339 = relay.TupleGetItem(func_3571_call(), 1)
call_4340 = relay.TupleGetItem(func_3572_call(), 1)
func_3692_call = mod.get_global_var('func_3692')
func_3693_call = mutated_mod.get_global_var('func_3693')
call_4344 = func_3692_call()
call_4345 = func_3692_call()
output = relay.Tuple([call_4339,call_4344,])
output2 = relay.Tuple([call_4340,call_4345,])
func_4375 = relay.Function([], output)
mod['func_4375'] = func_4375
mod = relay.transform.InferType()(mod)
mutated_mod['func_4375'] = func_4375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4375_call = mutated_mod.get_global_var('func_4375')
call_4376 = func_4375_call()
output = call_4376
func_4377 = relay.Function([], output)
mutated_mod['func_4377'] = func_4377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_4384 = relay.TupleGetItem(func_3789_call(), 0)
call_4385 = relay.TupleGetItem(func_3790_call(), 0)
func_2297_call = mod.get_global_var('func_2297')
func_2299_call = mutated_mod.get_global_var('func_2299')
call_4409 = relay.TupleGetItem(func_2297_call(), 0)
call_4410 = relay.TupleGetItem(func_2299_call(), 0)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_4436 = func_2281_call()
call_4437 = func_2281_call()
func_1964_call = mod.get_global_var('func_1964')
func_1967_call = mutated_mod.get_global_var('func_1967')
const_4441 = relay.const([3,-1,9,2,2,2,7,-8,1,-3,-7,-3,-6,8,-4,-5,4,-1,8,4,5,1,4,-6,-5,-1,6,5,-2,-2,-1,-5,-5,-9,-2,-2,-9,-8,4,7,-10,4,-6,-10,1,5,8,-8,-6,5,-9,4,2,2,3,7,-2,1,-9,6,-2,-3,-1,-5,-9,-5,-9,-10,-1,7,4,9,-5,3,1,8,-2,-6,-4,-10,-3,-3,3,5,6,8,-6,-7,5,-6,1,2,7,-6,8,5,-10,6,-2,5,-1,-9,10,-9,-7,-3,-1,2,10,-8,-4,2,1,-5,-6,-2,-5,-5,6,10,-1,2,6,1,-1,-6,3,-7,5,1,6,8,4,-6,9,6,1,-5,1,4,-6,9,10,8,-1,7,-2,-9,-10,7,-3,1,-10,-2,2,-6,-8,-2,10,6,-8,-9,7,5,4,-9,6,10,6,-8,10,1,-7,-8,2,10,-4,8,-8,-1,8,9,9,9,-3,-6,-1,9,-7,-6,-9,-8,-7,8,-3,8,-6,5,-6,1,-3,10,-3,1,8,-10,4,-1,6,6,8,-1,1,-2,-2,6,-9,9,-7,-1,-8,1,-8,-4,-4,2,-4,-6,10,-2,10,-8,-6,8,-9,-6,9,10,-2,10,5,-7,6,8,1,8,9,2,-5,7,-1,-1,-4,8,5,1,-3,-3,-4,-4,-10,-8,-8,-4,-1,7,6,2,8,6,-9,5,5,-10,-8,4,5,-7,-2,-6,-2,5,-8,9,-9,3,-2,-2,8,-8,4,-6,-5,2,4,2,-10,5,6,-5,-9,-4,9,-9,-6,3,10,1,-2,7,-2,3,6,9,4,-6,4,-5,4,10,-3,-1,2,-2,-4,10,6,7,3,-3,-2,9,8,9,-8,-3,-1,5,4,-10,6,6,5,-5,9,-3,-8,-7,6,10,6,-6,6,4,1,-10,-4,-9,8,-5,-4,8,-3], dtype = "uint32")#candidate|4441|(363,)|const|uint32
call_4440 = relay.TupleGetItem(func_1964_call(relay.reshape(const_4441.astype('uint32'), [363,])), 0)
call_4442 = relay.TupleGetItem(func_1967_call(relay.reshape(const_4441.astype('uint32'), [363,])), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
call_4446 = relay.TupleGetItem(func_1535_call(relay.reshape(call_4440.astype('float32'), [1, 312])), 1)
call_4447 = relay.TupleGetItem(func_1538_call(relay.reshape(call_4440.astype('float32'), [1, 312])), 1)
func_3571_call = mod.get_global_var('func_3571')
func_3572_call = mutated_mod.get_global_var('func_3572')
call_4456 = relay.TupleGetItem(func_3571_call(), 0)
call_4457 = relay.TupleGetItem(func_3572_call(), 0)
func_2714_call = mod.get_global_var('func_2714')
func_2715_call = mutated_mod.get_global_var('func_2715')
call_4458 = func_2714_call()
call_4459 = func_2714_call()
output = relay.Tuple([call_4384,call_4409,call_4436,call_4440,const_4441,call_4446,call_4456,call_4458,])
output2 = relay.Tuple([call_4385,call_4410,call_4437,call_4442,const_4441,call_4447,call_4457,call_4459,])
func_4460 = relay.Function([], output)
mod['func_4460'] = func_4460
mod = relay.transform.InferType()(mod)
output = func_4460()
func_4461 = relay.Function([], output)
mutated_mod['func_4461'] = func_4461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_4462 = relay.TupleGetItem(func_1769_call(), 2)
call_4463 = relay.TupleGetItem(func_1771_call(), 2)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_4465 = relay.TupleGetItem(func_2587_call(), 2)
call_4466 = relay.TupleGetItem(func_2588_call(), 2)
output = relay.Tuple([call_4462,call_4465,])
output2 = relay.Tuple([call_4463,call_4466,])
func_4504 = relay.Function([], output)
mod['func_4504'] = func_4504
mod = relay.transform.InferType()(mod)
mutated_mod['func_4504'] = func_4504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4504_call = mutated_mod.get_global_var('func_4504')
call_4505 = func_4504_call()
output = call_4505
func_4506 = relay.Function([], output)
mutated_mod['func_4506'] = func_4506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4316_call = mod.get_global_var('func_4316')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_4554 = relay.TupleGetItem(func_4316_call(), 0)
call_4555 = relay.TupleGetItem(func_4317_call(), 0)
output = relay.Tuple([call_4554,])
output2 = relay.Tuple([call_4555,])
func_4558 = relay.Function([], output)
mod['func_4558'] = func_4558
mod = relay.transform.InferType()(mod)
output = func_4558()
func_4559 = relay.Function([], output)
mutated_mod['func_4559'] = func_4559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4316_call = mod.get_global_var('func_4316')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_4592 = relay.TupleGetItem(func_4316_call(), 2)
call_4593 = relay.TupleGetItem(func_4317_call(), 2)
output = call_4592
output2 = call_4593
func_4598 = relay.Function([], output)
mod['func_4598'] = func_4598
mod = relay.transform.InferType()(mod)
output = func_4598()
func_4599 = relay.Function([], output)
mutated_mod['func_4599'] = func_4599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_4816 = relay.TupleGetItem(func_2937_call(), 5)
call_4817 = relay.TupleGetItem(func_2939_call(), 5)
output = relay.Tuple([call_4816,])
output2 = relay.Tuple([call_4817,])
func_4822 = relay.Function([], output)
mod['func_4822'] = func_4822
mod = relay.transform.InferType()(mod)
mutated_mod['func_4822'] = func_4822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4822_call = mutated_mod.get_global_var('func_4822')
call_4823 = func_4822_call()
output = call_4823
func_4824 = relay.Function([], output)
mutated_mod['func_4824'] = func_4824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_4853 = func_2281_call()
call_4854 = func_2281_call()
func_307_call = mod.get_global_var('func_307')
func_310_call = mutated_mod.get_global_var('func_310')
const_4861 = relay.const([-4,-9,8,-2,-3,1,1,3,2,-10,-2,3,-10,2,-7,-3,-6,9,-10,-7,4,-3,7,8,3,-6,5,-8,4,-8,-5,-10,-5,-6,-2,8,-3,10,-8,-3,8,-7,-1,-9,-7,6,10,-4,6,10,5,3,2,9,-4,2,-4,-5,7,9,-3,-5,-10,-5,-1,6,6,5,3,-7,-8,8,-9,-6,7,10,10,-2,-8,-9,-4,6,-4,-8,-7,-5,4,-9,-6,-1,10,-4,9,-3,5,-6,8,-8,5,1,-3,-8,-2,1,-2,5,-6,-10,-5,1,-6,-8], dtype = "int8")#candidate|4861|(112,)|const|int8
call_4860 = func_307_call(relay.reshape(const_4861.astype('int8'), [8, 14, 1]), relay.reshape(call_4853.astype('int8'), [8, 14, 10]), )
call_4862 = func_307_call(relay.reshape(const_4861.astype('int8'), [8, 14, 1]), relay.reshape(call_4853.astype('int8'), [8, 14, 10]), )
func_4064_call = mod.get_global_var('func_4064')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_4863 = relay.TupleGetItem(func_4064_call(), 0)
call_4864 = relay.TupleGetItem(func_4065_call(), 0)
output = relay.Tuple([call_4853,call_4860,const_4861,call_4863,])
output2 = relay.Tuple([call_4854,call_4862,const_4861,call_4864,])
func_4869 = relay.Function([], output)
mod['func_4869'] = func_4869
mod = relay.transform.InferType()(mod)
mutated_mod['func_4869'] = func_4869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4869_call = mutated_mod.get_global_var('func_4869')
call_4870 = func_4869_call()
output = call_4870
func_4871 = relay.Function([], output)
mutated_mod['func_4871'] = func_4871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4903 = relay.var("var_4903", dtype = "uint8", shape = ())#candidate|4903|()|var|uint8
var_4904 = relay.var("var_4904", dtype = "uint8", shape = (12, 3, 12))#candidate|4904|(12, 3, 12)|var|uint8
bop_4905 = relay.greater(var_4903.astype('bool'), var_4904.astype('bool')) # shape=(12, 3, 12)
func_4031_call = mod.get_global_var('func_4031')
func_4033_call = mutated_mod.get_global_var('func_4033')
var_4914 = relay.var("var_4914", dtype = "float64", shape = (1092,))#candidate|4914|(1092,)|var|float64
call_4913 = func_4031_call(relay.reshape(var_4914.astype('float64'), [12, 7, 13]))
call_4915 = func_4031_call(relay.reshape(var_4914.astype('float64'), [12, 7, 13]))
output = relay.Tuple([bop_4905,call_4913,var_4914,])
output2 = relay.Tuple([bop_4905,call_4915,var_4914,])
func_4927 = relay.Function([var_4903,var_4904,var_4914,], output)
mod['func_4927'] = func_4927
mod = relay.transform.InferType()(mod)
mutated_mod['func_4927'] = func_4927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4927_call = mutated_mod.get_global_var('func_4927')
var_4929 = relay.var("var_4929", dtype = "uint8", shape = ())#candidate|4929|()|var|uint8
var_4930 = relay.var("var_4930", dtype = "uint8", shape = (12, 3, 12))#candidate|4930|(12, 3, 12)|var|uint8
var_4931 = relay.var("var_4931", dtype = "float64", shape = (1092,))#candidate|4931|(1092,)|var|float64
call_4928 = func_4927_call(var_4929,var_4930,var_4931,)
output = call_4928
func_4932 = relay.Function([var_4929,var_4930,var_4931,], output)
mutated_mod['func_4932'] = func_4932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_4934 = relay.TupleGetItem(func_2403_call(), 0)
call_4935 = relay.TupleGetItem(func_2405_call(), 0)
output = relay.Tuple([call_4934,])
output2 = relay.Tuple([call_4935,])
func_4942 = relay.Function([], output)
mod['func_4942'] = func_4942
mod = relay.transform.InferType()(mod)
mutated_mod['func_4942'] = func_4942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4942_call = mutated_mod.get_global_var('func_4942')
call_4943 = func_4942_call()
output = call_4943
func_4944 = relay.Function([], output)
mutated_mod['func_4944'] = func_4944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_4950 = func_2361_call()
call_4951 = func_2361_call()
func_3870_call = mod.get_global_var('func_3870')
func_3871_call = mutated_mod.get_global_var('func_3871')
call_4958 = relay.TupleGetItem(func_3870_call(), 0)
call_4959 = relay.TupleGetItem(func_3871_call(), 0)
output = relay.Tuple([call_4950,call_4958,])
output2 = relay.Tuple([call_4951,call_4959,])
func_4966 = relay.Function([], output)
mod['func_4966'] = func_4966
mod = relay.transform.InferType()(mod)
mutated_mod['func_4966'] = func_4966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4966_call = mutated_mod.get_global_var('func_4966')
call_4967 = func_4966_call()
output = call_4967
func_4968 = relay.Function([], output)
mutated_mod['func_4968'] = func_4968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4256_call = mod.get_global_var('func_4256')
func_4257_call = mutated_mod.get_global_var('func_4257')
call_4982 = func_4256_call()
call_4983 = func_4256_call()
func_3907_call = mod.get_global_var('func_3907')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_4985 = relay.TupleGetItem(func_3907_call(), 0)
call_4986 = relay.TupleGetItem(func_3909_call(), 0)
output = relay.Tuple([call_4982,call_4985,])
output2 = relay.Tuple([call_4983,call_4986,])
func_4997 = relay.Function([], output)
mod['func_4997'] = func_4997
mod = relay.transform.InferType()(mod)
mutated_mod['func_4997'] = func_4997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4997_call = mutated_mod.get_global_var('func_4997')
call_4998 = func_4997_call()
output = call_4998
func_4999 = relay.Function([], output)
mutated_mod['func_4999'] = func_4999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_5003 = relay.TupleGetItem(func_2162_call(), 1)
call_5004 = relay.TupleGetItem(func_2163_call(), 1)
uop_5008 = relay.erf(call_5003.astype('float64')) # shape=(8, 14, 10)
uop_5010 = relay.erf(call_5004.astype('float64')) # shape=(8, 14, 10)
output = uop_5008
output2 = uop_5010
func_5013 = relay.Function([], output)
mod['func_5013'] = func_5013
mod = relay.transform.InferType()(mod)
mutated_mod['func_5013'] = func_5013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5013_call = mutated_mod.get_global_var('func_5013')
call_5014 = func_5013_call()
output = call_5014
func_5015 = relay.Function([], output)
mutated_mod['func_5015'] = func_5015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4997_call = mod.get_global_var('func_4997')
func_4999_call = mutated_mod.get_global_var('func_4999')
call_5026 = relay.TupleGetItem(func_4997_call(), 0)
call_5027 = relay.TupleGetItem(func_4999_call(), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
const_5051 = relay.const([4.268249,-9.330713,6.838531,-5.818079,1.163414,-7.578943,4.606735,-8.014875,-7.345238,2.405253,5.563094,6.426112,6.731779,8.994928,2.631299,-7.567088,-8.777940,-6.509706,5.320626,2.018192,-2.189628,-5.747763,-3.853950,-2.691678,0.567562,6.777563,-8.152324,-3.443979,-6.481696,-5.353809,-3.632313,-1.850524,6.189295,-3.421102,-2.709840,2.349762,3.183329,-6.787948,-1.854415,-0.977951,0.353152,-8.904299,4.783455,3.128287,6.215732,2.395238,-1.272356,-4.741780,-1.198763,-6.647107,9.914319,-8.777180,2.796257,-3.221374,7.082891,1.987577,-9.884044,-5.573210,-1.303555,8.892878,4.285225,2.680213,7.038887,-6.811970,-0.825818,-3.721391,-4.367087,-2.839172,4.554250,-2.956075,-4.919323,6.310141,9.618416,-3.106136,2.886892,6.608167,-0.884305,-6.636128,2.573513,-0.482027,6.388157,4.529349,1.096830,5.550748,-9.347913,7.039354,2.468939,-1.968893,1.665154,5.187368,-4.136356,8.456228,0.020960,-0.036435,-6.693564,4.718136,4.465251,-1.678804,-7.720900,-9.359149,0.803646,0.842611,-6.468883,4.379803,-7.802438,3.163995,-2.327224,-3.519154,-2.196852,-2.857584,3.770751,4.381762,-4.012324,5.137826,5.202990,1.331711,0.100941,-7.858817,-8.559243,1.566741,-8.910177,-7.160817,-9.808214,-8.158663,0.477436,6.905927,-9.608354,-8.141774,-5.174789,-6.626342,3.940611,-7.857918,-9.137183,-5.393351,9.226248,-2.246324,-4.012538,-9.533036,3.106940,-5.029234,8.990422,6.899076,-8.501733,-3.332097,0.791085,-0.867074,-0.079575,8.251975,3.719122,-3.982658,-6.406211,-4.296334,3.239517,4.635459,-8.424091,6.297286,5.028304,0.086015,-9.910043,7.469110,-4.976778,-9.645433,-3.554959,-6.173913,-8.907699,-8.313075,4.465557,9.140122,3.364920,5.048465,-3.510518,9.580541,3.372089,6.320578,-1.183176,9.962256,2.445588,-7.623292,3.539405,5.101589,1.186343,-4.453647,7.007863,3.918247,-4.564400,-8.883038,3.234606,4.198424,-5.614659,8.567938,5.892745,-3.134835,-7.099059,-2.803338,8.917509,9.792264,-0.395920,7.775627,-5.394360,-4.161815,7.360184,5.986413,3.369031,6.522456,-0.417751,-8.210643,2.221561,-7.063676,2.580002,5.011437,-8.703840,5.842028,3.319233,-5.910048,9.423887,-8.514469,7.837611,-7.170082,-0.308898,4.463659,-3.859294,-6.323401,-9.431601,0.477490,-4.551438,-1.004027,-7.232891,0.584902,-4.821440,2.795137,-2.724320,-1.511863,3.433143,-6.600752,-9.332375,-2.836856,-8.183531,-6.752588,3.434656,-5.023263,-2.574558,6.315962,1.033212,-0.995207,-0.030437,0.951273,-5.128972,8.598913,-3.539499,5.906149,1.094526,4.539016,4.765970,-6.171866,-2.646139,-3.260433,1.860985,0.011586,-9.244711,-5.622194,4.741888,3.583524,8.347039,4.357308,9.765030,-5.902365,8.296358,-8.586356,4.354327,1.470229,6.985576,-8.776941,5.759804,3.902064,-9.557268,4.111260,-7.754719,6.592073,9.609381,7.494616,0.015832,4.722962,-8.075793,7.770379,-9.336240,5.426659,-6.663107,-1.700565,3.626855,6.326795,3.089142,8.408031,-1.029355,1.418199,3.171046,-3.020102,-0.692797,5.687417,7.009122,-7.397037,-6.093301,1.858726,6.670211,-1.058891,-1.489086,-1.739480,-5.555333,4.148077,-5.281833,-8.008863,7.266784,0.549208], dtype = "float32")#candidate|5051|(312,)|const|float32
call_5050 = relay.TupleGetItem(func_1535_call(relay.reshape(const_5051.astype('float32'), [1, 312])), 1)
call_5052 = relay.TupleGetItem(func_1538_call(relay.reshape(const_5051.astype('float32'), [1, 312])), 1)
output = relay.Tuple([call_5026,call_5050,const_5051,])
output2 = relay.Tuple([call_5027,call_5052,const_5051,])
func_5063 = relay.Function([], output)
mod['func_5063'] = func_5063
mod = relay.transform.InferType()(mod)
output = func_5063()
func_5064 = relay.Function([], output)
mutated_mod['func_5064'] = func_5064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4316_call = mod.get_global_var('func_4316')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_5091 = relay.TupleGetItem(func_4316_call(), 2)
call_5092 = relay.TupleGetItem(func_4317_call(), 2)
func_3492_call = mod.get_global_var('func_3492')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_5101 = relay.TupleGetItem(func_3492_call(), 1)
call_5102 = relay.TupleGetItem(func_3494_call(), 1)
output = relay.Tuple([call_5091,call_5101,])
output2 = relay.Tuple([call_5092,call_5102,])
func_5124 = relay.Function([], output)
mod['func_5124'] = func_5124
mod = relay.transform.InferType()(mod)
mutated_mod['func_5124'] = func_5124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5124_call = mutated_mod.get_global_var('func_5124')
call_5125 = func_5124_call()
output = call_5125
func_5126 = relay.Function([], output)
mutated_mod['func_5126'] = func_5126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3692_call = mod.get_global_var('func_3692')
func_3693_call = mutated_mod.get_global_var('func_3693')
call_5165 = func_3692_call()
call_5166 = func_3692_call()
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_5189 = relay.TupleGetItem(func_1769_call(), 3)
call_5190 = relay.TupleGetItem(func_1771_call(), 3)
func_5124_call = mod.get_global_var('func_5124')
func_5126_call = mutated_mod.get_global_var('func_5126')
call_5211 = relay.TupleGetItem(func_5124_call(), 1)
call_5212 = relay.TupleGetItem(func_5126_call(), 1)
output = relay.Tuple([call_5165,call_5189,call_5211,])
output2 = relay.Tuple([call_5166,call_5190,call_5212,])
func_5219 = relay.Function([], output)
mod['func_5219'] = func_5219
mod = relay.transform.InferType()(mod)
mutated_mod['func_5219'] = func_5219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5219_call = mutated_mod.get_global_var('func_5219')
call_5220 = func_5219_call()
output = call_5220
func_5221 = relay.Function([], output)
mutated_mod['func_5221'] = func_5221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4997_call = mod.get_global_var('func_4997')
func_4999_call = mutated_mod.get_global_var('func_4999')
call_5291 = relay.TupleGetItem(func_4997_call(), 0)
call_5292 = relay.TupleGetItem(func_4999_call(), 0)
func_1769_call = mod.get_global_var('func_1769')
func_1771_call = mutated_mod.get_global_var('func_1771')
call_5296 = relay.TupleGetItem(func_1769_call(), 0)
call_5297 = relay.TupleGetItem(func_1771_call(), 0)
output = relay.Tuple([call_5291,call_5296,])
output2 = relay.Tuple([call_5292,call_5297,])
func_5309 = relay.Function([], output)
mod['func_5309'] = func_5309
mod = relay.transform.InferType()(mod)
output = func_5309()
func_5310 = relay.Function([], output)
mutated_mod['func_5310'] = func_5310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5013_call = mod.get_global_var('func_5013')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_5339 = func_5013_call()
call_5340 = func_5013_call()
output = call_5339
output2 = call_5340
func_5341 = relay.Function([], output)
mod['func_5341'] = func_5341
mod = relay.transform.InferType()(mod)
mutated_mod['func_5341'] = func_5341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5341_call = mutated_mod.get_global_var('func_5341')
call_5342 = func_5341_call()
output = call_5342
func_5343 = relay.Function([], output)
mutated_mod['func_5343'] = func_5343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5013_call = mod.get_global_var('func_5013')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_5370 = func_5013_call()
call_5371 = func_5013_call()
func_5063_call = mod.get_global_var('func_5063')
func_5064_call = mutated_mod.get_global_var('func_5064')
call_5385 = relay.TupleGetItem(func_5063_call(), 1)
call_5386 = relay.TupleGetItem(func_5064_call(), 1)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_5391 = relay.TupleGetItem(func_1912_call(), 0)
call_5392 = relay.TupleGetItem(func_1914_call(), 0)
func_4927_call = mod.get_global_var('func_4927')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_5404 = relay.var("var_5404", dtype = "uint8", shape = ())#candidate|5404|()|var|uint8
const_5405 = relay.const([[-10,-7,1,-4,8,9,-5,6,1,-5,10,9,2,8,-1,-8,-7,1,-10,4,8,-3,4,4,5,-4,-7,6,6,-7,-2,-7,9,6,-10,1,-4,1,-2,-3,4,1,-4,-3,2,-5,-7,1,8,-5,-8,8,-9,-9,-6,9,2,3,8,4,6,-4,2,8,3,-10,-10,-10,-7,-1,3,-5,1,-1,-4,10,-6,2,8,-10,3,-1,-10,1,3,-2,-1,1,3,-2,-9,-8,5,-5,-1,-5,8,-9,-10,-8,2,7,-5,7,2,-6,10,-6],[-3,9,9,-10,1,-7,-8,3,-3,7,-1,-7,-4,2,8,-10,-2,-6,-4,-9,-4,7,1,5,-10,-3,7,-4,4,6,5,-2,-6,9,5,-6,-6,2,-2,-1,-9,5,-4,-6,4,-10,-9,-7,3,6,6,6,6,-9,-4,5,3,-9,9,-7,7,-4,-2,-3,9,-2,3,8,3,-2,-6,-10,6,-9,-5,2,4,10,8,-10,5,3,7,1,-7,-8,-7,5,10,-2,8,10,-9,9,-6,-4,10,-10,9,8,-4,2,-9,-7,-8,-7,-3,2],[7,-9,10,-5,3,7,9,-9,-6,-4,-5,-5,2,-3,8,6,7,-8,1,7,-9,5,4,8,-4,-6,-5,-3,-2,9,4,-3,3,7,-5,7,9,-3,-5,-2,5,-7,8,5,-8,9,-2,-10,6,-8,-2,-8,-6,-5,-1,-7,4,7,5,3,8,3,6,6,3,-6,10,5,2,4,-6,2,-8,5,10,-7,1,10,-5,3,2,-2,-1,6,-6,1,-5,3,9,-7,7,-9,3,-6,-6,6,-8,10,-5,7,1,5,-8,-9,8,9,-7,-2],[8,9,-6,-3,3,-6,-2,-10,-8,8,3,4,-1,-5,-1,-1,6,4,2,8,1,-4,4,5,-8,9,-10,1,8,-2,-4,8,10,3,9,9,-7,4,-8,-5,-2,6,-9,-3,-4,6,7,-1,7,-1,7,-6,-5,-6,-9,-9,-7,-5,3,-5,-5,6,-6,1,1,10,3,2,8,3,1,2,-5,4,5,5,-10,-3,10,-2,5,-10,-9,6,-4,-7,-1,3,-6,-5,8,-4,-3,-7,-9,7,-10,-10,-1,8,-7,10,-6,3,-2,4,10,-10]], dtype = "uint8")#candidate|5405|(4, 108)|const|uint8
var_5406 = relay.var("var_5406", dtype = "float64", shape = (546, 2))#candidate|5406|(546, 2)|var|float64
call_5403 = relay.TupleGetItem(func_4927_call(relay.reshape(var_5404.astype('uint8'), []), relay.reshape(const_5405.astype('uint8'), [12, 3, 12]), relay.reshape(var_5406.astype('float64'), [1092,]), ), 2)
call_5407 = relay.TupleGetItem(func_4932_call(relay.reshape(var_5404.astype('uint8'), []), relay.reshape(const_5405.astype('uint8'), [12, 3, 12]), relay.reshape(var_5406.astype('float64'), [1092,]), ), 2)
uop_5412 = relay.sigmoid(call_5385.astype('float64')) # shape=(6, 13, 4)
uop_5414 = relay.sigmoid(call_5386.astype('float64')) # shape=(6, 13, 4)
output = relay.Tuple([call_5370,call_5391,call_5403,var_5404,const_5405,var_5406,uop_5412,])
output2 = relay.Tuple([call_5371,call_5392,call_5407,var_5404,const_5405,var_5406,uop_5414,])
func_5432 = relay.Function([var_5404,var_5406,], output)
mod['func_5432'] = func_5432
mod = relay.transform.InferType()(mod)
mutated_mod['func_5432'] = func_5432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5432_call = mutated_mod.get_global_var('func_5432')
var_5434 = relay.var("var_5434", dtype = "uint8", shape = ())#candidate|5434|()|var|uint8
var_5435 = relay.var("var_5435", dtype = "float64", shape = (546, 2))#candidate|5435|(546, 2)|var|float64
call_5433 = func_5432_call(var_5434,var_5435,)
output = call_5433
func_5436 = relay.Function([var_5434,var_5435,], output)
mutated_mod['func_5436'] = func_5436
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5438 = relay.const(-3, dtype = "uint8")#candidate|5438|()|const|uint8
var_5439 = relay.var("var_5439", dtype = "uint8", shape = (10, 1, 6))#candidate|5439|(10, 1, 6)|var|uint8
bop_5440 = relay.bitwise_and(const_5438.astype('uint8'), var_5439.astype('uint8')) # shape=(10, 1, 6)
output = relay.Tuple([bop_5440,])
output2 = relay.Tuple([bop_5440,])
func_5459 = relay.Function([var_5439,], output)
mod['func_5459'] = func_5459
mod = relay.transform.InferType()(mod)
var_5460 = relay.var("var_5460", dtype = "uint8", shape = (10, 1, 6))#candidate|5460|(10, 1, 6)|var|uint8
output = func_5459(var_5460)
func_5461 = relay.Function([var_5460], output)
mutated_mod['func_5461'] = func_5461
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5492 = relay.const([[[7.225213,-9.221333,8.755705,2.400627,-4.270340,-4.164745,-3.182626,-4.527899,-7.859239,4.705949],[2.361517,8.350218,7.524047,4.637956,3.655709,-6.413404,-1.782066,-8.206471,-8.691331,-8.418607],[0.536275,-4.702650,1.916904,4.141944,3.508884,-9.421410,-3.237944,-3.116122,-1.682916,9.369631],[-3.660863,-3.800625,8.336502,-6.376776,-3.008655,-6.133705,-4.753861,-5.290147,2.788271,8.819286],[-3.177650,-3.688782,2.405880,-4.563342,-6.328382,6.857153,0.260215,-0.222751,-8.313526,-5.072496]],[[7.025537,-4.813578,6.126629,0.270801,-8.592782,-7.695824,-6.285170,6.748278,8.269617,-0.187720],[0.467336,-8.751445,3.364155,0.116199,-6.082681,4.582668,-4.776622,1.156205,-6.738582,6.507545],[5.495147,7.657751,-8.493900,0.592292,-5.488128,9.125365,7.804604,-4.805135,-5.992364,-6.351213],[7.074612,-6.769215,2.128776,-2.579984,6.501465,-2.033808,8.591624,-9.633792,-9.845575,9.242854],[6.269960,-8.561542,-6.237025,-0.567984,0.755705,5.830180,-2.100746,-4.952039,4.640246,4.490874]],[[-9.554750,7.889004,2.726321,9.451401,4.567319,-5.068240,-3.304427,8.756858,5.760935,2.669791],[-0.086609,9.421999,7.697804,-4.718469,-8.126655,0.076788,8.045808,-8.092779,-8.811623,-8.036154],[-1.651572,0.078933,-9.808969,-6.082161,-8.227724,-9.429287,-2.770237,4.836826,8.011060,7.534641],[7.378440,6.717274,4.962151,4.237673,8.965054,-6.843142,-9.590527,-1.423125,-9.951102,-5.903831],[4.040467,-3.537896,-0.582438,3.401416,1.687815,-7.163220,7.790754,-3.233866,5.277437,-7.320470]],[[6.866703,6.029718,-3.835606,-0.946967,-9.950022,1.041193,0.215598,5.329212,9.838142,-3.096182],[6.634085,2.626568,-0.366709,-8.916253,4.114496,-7.160623,7.084682,-8.280198,-2.282754,-4.699527],[2.118117,-3.332917,8.593669,6.609227,-1.222961,-6.197202,-5.515663,-9.620478,6.250145,-8.145701],[7.893953,1.749525,-7.680240,8.579685,8.898195,5.929620,2.184363,5.963980,-8.732424,-5.864129],[-9.046827,-9.884208,-4.391460,6.767516,2.141742,6.138362,8.765012,9.065375,-6.485659,-9.277871]],[[6.486263,3.819996,6.298885,4.853195,4.966478,-1.808225,-8.282366,-3.486920,6.274967,-5.784302],[8.588152,1.949427,9.625171,8.999794,3.989726,5.289893,3.999019,-7.009040,9.220549,-0.513714],[3.920011,3.166049,-6.579103,-4.735761,8.468154,-2.006213,-5.032745,4.114113,2.506900,-6.554215],[-2.807385,4.915282,-6.561879,-3.381056,9.007237,-7.441432,5.539687,3.711334,5.604421,9.383273],[-7.606638,3.183052,-1.915010,-2.373572,2.015261,-2.571547,-0.637659,-8.737458,0.374090,3.080532]],[[1.531031,2.726252,5.862591,-0.592108,0.969785,5.574320,-0.546885,-1.054130,-7.111130,-5.633057],[6.189827,8.507624,-0.599801,-7.191477,4.555065,-2.718021,0.148794,9.980485,-6.561097,6.826532],[-6.892058,-2.872173,-5.461098,0.662859,0.838947,-3.335162,-5.592207,5.076761,5.444986,7.610210],[9.161898,-7.846276,4.247264,7.064749,0.256151,0.680809,1.158901,-3.120762,1.584829,-2.011033],[5.115646,2.058410,8.708162,-3.544368,4.441277,3.623355,-9.563878,9.407122,6.647340,2.777082]],[[-1.604894,-2.866639,-3.019473,6.718013,-4.754410,6.526231,-6.480340,-6.112727,5.043091,8.810135],[-3.705174,5.977205,-9.572771,-6.579805,3.982234,-6.012976,3.307992,2.382967,-8.567449,8.237772],[3.960158,-8.819948,1.343859,7.095578,-2.909404,5.476878,2.949993,0.191022,-9.246193,8.731458],[0.708273,2.948334,0.543346,1.850621,9.932643,-6.730719,6.787106,-3.553731,2.497977,4.817782],[-2.304832,-9.287542,0.460449,3.613592,-1.400558,8.874659,0.440152,-5.746461,2.339655,-2.936467]],[[-8.641421,5.908539,1.982330,-0.787464,9.795947,-9.088795,5.145161,7.961420,-6.961479,-7.784832],[-0.019873,2.684278,-5.749260,-1.924733,5.919551,-0.385890,0.830361,6.511699,4.494555,-1.693514],[5.229427,4.444691,4.740288,4.419607,3.344877,-0.853502,1.688682,5.000522,9.498048,5.218571],[-1.337659,-8.538383,-7.721288,8.442499,-8.452301,-2.391391,-0.380931,-3.210952,6.919370,-4.980790],[1.788202,-8.972661,-0.215038,-0.903650,2.770728,-5.502621,7.262028,4.960991,-0.028859,9.325604]],[[-3.901334,-7.533763,9.966792,6.443538,-2.877555,-3.378331,-9.512503,-4.485682,-4.171363,0.055345],[-1.154587,-5.485792,-1.470296,4.807734,-1.900230,6.758953,4.262982,0.544156,-7.419281,3.240836],[-9.673717,-6.205271,-6.986085,0.011287,3.116444,-5.386290,-2.765709,2.254212,-8.394933,0.356628],[-8.459172,-0.727549,-6.779290,-6.595182,-5.844798,7.263939,4.251232,7.141291,-5.539129,7.151749],[0.786838,-8.654310,-0.805926,9.347782,-1.304268,7.507463,0.701828,-0.771805,1.897313,9.150937]]], dtype = "float64")#candidate|5492|(9, 5, 10)|const|float64
uop_5493 = relay.asinh(const_5492.astype('float64')) # shape=(9, 5, 10)
output = uop_5493
output2 = uop_5493
func_5498 = relay.Function([], output)
mod['func_5498'] = func_5498
mod = relay.transform.InferType()(mod)
output = func_5498()
func_5499 = relay.Function([], output)
mutated_mod['func_5499'] = func_5499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4064_call = mod.get_global_var('func_4064')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_5521 = relay.TupleGetItem(func_4064_call(), 0)
call_5522 = relay.TupleGetItem(func_4065_call(), 0)
func_3463_call = mod.get_global_var('func_3463')
func_3464_call = mutated_mod.get_global_var('func_3464')
call_5523 = relay.TupleGetItem(func_3463_call(), 0)
call_5524 = relay.TupleGetItem(func_3464_call(), 0)
output = relay.Tuple([call_5521,call_5523,])
output2 = relay.Tuple([call_5522,call_5524,])
func_5533 = relay.Function([], output)
mod['func_5533'] = func_5533
mod = relay.transform.InferType()(mod)
mutated_mod['func_5533'] = func_5533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5533_call = mutated_mod.get_global_var('func_5533')
call_5534 = func_5533_call()
output = call_5534
func_5535 = relay.Function([], output)
mutated_mod['func_5535'] = func_5535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5309_call = mod.get_global_var('func_5309')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_5554 = relay.TupleGetItem(func_5309_call(), 1)
call_5555 = relay.TupleGetItem(func_5310_call(), 1)
output = relay.Tuple([call_5554,])
output2 = relay.Tuple([call_5555,])
func_5559 = relay.Function([], output)
mod['func_5559'] = func_5559
mod = relay.transform.InferType()(mod)
output = func_5559()
func_5560 = relay.Function([], output)
mutated_mod['func_5560'] = func_5560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_5606 = relay.TupleGetItem(func_4460_call(), 7)
call_5607 = relay.TupleGetItem(func_4461_call(), 7)
func_5013_call = mod.get_global_var('func_5013')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_5608 = func_5013_call()
call_5609 = func_5013_call()
uop_5617 = relay.rsqrt(call_5606.astype('float32')) # shape=(8, 14, 10)
uop_5619 = relay.rsqrt(call_5607.astype('float32')) # shape=(8, 14, 10)
func_4598_call = mod.get_global_var('func_4598')
func_4599_call = mutated_mod.get_global_var('func_4599')
call_5628 = func_4598_call()
call_5629 = func_4598_call()
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_5635 = relay.TupleGetItem(func_4460_call(), 7)
call_5636 = relay.TupleGetItem(func_4461_call(), 7)
output = relay.Tuple([call_5608,uop_5617,call_5628,call_5635,])
output2 = relay.Tuple([call_5609,uop_5619,call_5629,call_5636,])
func_5648 = relay.Function([], output)
mod['func_5648'] = func_5648
mod = relay.transform.InferType()(mod)
mutated_mod['func_5648'] = func_5648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mutated_mod.get_global_var('func_5648')
call_5649 = func_5648_call()
output = call_5649
func_5650 = relay.Function([], output)
mutated_mod['func_5650'] = func_5650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5702 = relay.var("var_5702", dtype = "float64", shape = ())#candidate|5702|()|var|float64
var_5703 = relay.var("var_5703", dtype = "float64", shape = (1, 11, 8))#candidate|5703|(1, 11, 8)|var|float64
bop_5704 = relay.floor_mod(var_5702.astype('float64'), var_5703.astype('float64')) # shape=(1, 11, 8)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_5707 = relay.TupleGetItem(func_2937_call(), 4)
call_5708 = relay.TupleGetItem(func_2939_call(), 4)
output = relay.Tuple([bop_5704,call_5707,])
output2 = relay.Tuple([bop_5704,call_5708,])
func_5710 = relay.Function([var_5702,var_5703,], output)
mod['func_5710'] = func_5710
mod = relay.transform.InferType()(mod)
mutated_mod['func_5710'] = func_5710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5710_call = mutated_mod.get_global_var('func_5710')
var_5712 = relay.var("var_5712", dtype = "float64", shape = ())#candidate|5712|()|var|float64
var_5713 = relay.var("var_5713", dtype = "float64", shape = (1, 11, 8))#candidate|5713|(1, 11, 8)|var|float64
call_5711 = func_5710_call(var_5712,var_5713,)
output = call_5711
func_5714 = relay.Function([var_5712,var_5713,], output)
mutated_mod['func_5714'] = func_5714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_5727 = relay.TupleGetItem(func_3841_call(), 0)
call_5728 = relay.TupleGetItem(func_3842_call(), 0)
output = relay.Tuple([call_5727,])
output2 = relay.Tuple([call_5728,])
func_5732 = relay.Function([], output)
mod['func_5732'] = func_5732
mod = relay.transform.InferType()(mod)
mutated_mod['func_5732'] = func_5732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mutated_mod.get_global_var('func_5732')
call_5733 = func_5732_call()
output = call_5733
func_5734 = relay.Function([], output)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_5786 = relay.TupleGetItem(func_3907_call(), 0)
call_5787 = relay.TupleGetItem(func_3909_call(), 0)
uop_5788 = relay.asin(call_5786.astype('float32')) # shape=(6, 13, 4)
uop_5790 = relay.asin(call_5787.astype('float32')) # shape=(6, 13, 4)
uop_5792 = relay.acos(call_5786.astype('float32')) # shape=(6, 13, 4)
uop_5794 = relay.acos(call_5787.astype('float32')) # shape=(6, 13, 4)
output = relay.Tuple([uop_5788,uop_5792,])
output2 = relay.Tuple([uop_5790,uop_5794,])
func_5811 = relay.Function([], output)
mod['func_5811'] = func_5811
mod = relay.transform.InferType()(mod)
output = func_5811()
func_5812 = relay.Function([], output)
mutated_mod['func_5812'] = func_5812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4869_call = mod.get_global_var('func_4869')
func_4871_call = mutated_mod.get_global_var('func_4871')
call_5817 = relay.TupleGetItem(func_4869_call(), 3)
call_5818 = relay.TupleGetItem(func_4871_call(), 3)
output = relay.Tuple([call_5817,])
output2 = relay.Tuple([call_5818,])
func_5820 = relay.Function([], output)
mod['func_5820'] = func_5820
mod = relay.transform.InferType()(mod)
mutated_mod['func_5820'] = func_5820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5820_call = mutated_mod.get_global_var('func_5820')
call_5821 = func_5820_call()
output = call_5821
func_5822 = relay.Function([], output)
mutated_mod['func_5822'] = func_5822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5820_call = mod.get_global_var('func_5820')
func_5822_call = mutated_mod.get_global_var('func_5822')
call_5858 = relay.TupleGetItem(func_5820_call(), 0)
call_5859 = relay.TupleGetItem(func_5822_call(), 0)
uop_5873 = relay.asinh(call_5858.astype('float32')) # shape=(6, 13, 4)
uop_5875 = relay.asinh(call_5859.astype('float32')) # shape=(6, 13, 4)
func_5811_call = mod.get_global_var('func_5811')
func_5812_call = mutated_mod.get_global_var('func_5812')
call_5925 = relay.TupleGetItem(func_5811_call(), 0)
call_5926 = relay.TupleGetItem(func_5812_call(), 0)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_5932 = relay.TupleGetItem(func_3789_call(), 0)
call_5933 = relay.TupleGetItem(func_3790_call(), 0)
func_5124_call = mod.get_global_var('func_5124')
func_5126_call = mutated_mod.get_global_var('func_5126')
call_5967 = relay.TupleGetItem(func_5124_call(), 1)
call_5968 = relay.TupleGetItem(func_5126_call(), 1)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_5971 = relay.TupleGetItem(func_2162_call(), 2)
call_5972 = relay.TupleGetItem(func_2163_call(), 2)
func_2032_call = mod.get_global_var('func_2032')
func_2034_call = mutated_mod.get_global_var('func_2034')
call_5973 = relay.TupleGetItem(func_2032_call(relay.reshape(call_5858.astype('float32'), [6, 13, 4])), 0)
call_5974 = relay.TupleGetItem(func_2034_call(relay.reshape(call_5858.astype('float32'), [6, 13, 4])), 0)
func_2804_call = mod.get_global_var('func_2804')
func_2807_call = mutated_mod.get_global_var('func_2807')
const_5980 = relay.const([[1.624523,1.431000,9.721104,-3.201450,-9.751306,-2.259149,-8.497930,7.281182,-2.702705,-4.194863,8.090179,1.825342,-9.249109,-2.077862,9.326019,0.620352,4.747402,-8.325646,-8.727930,6.150340,-4.959751,2.385642,7.277900,0.841442,5.050435,-9.196704,-0.351258,3.567135,-5.781495,0.961230,-9.586901,4.737028,-8.913975,9.483968,-7.389609,0.621511,-6.428083,2.293479,-1.495933,9.504321,-4.863310,-3.358257,-7.142777,1.825271,7.244445,-7.052753,8.521100,3.735368,-4.549847,1.173423,8.817912,9.404043,4.674806,8.081107,1.887340,8.488619,-2.239917,2.369606,-1.651299,-7.218470,2.228607,4.513160,-3.900561,-5.261215,3.056132,0.510267,9.976455,-9.050211,4.317529,-7.504871,2.605228,-2.958311,0.430261,-0.220434,-0.022868,8.329249,8.776853,-7.326838,-4.914961,-0.037822,-1.046911,-5.169485,5.930665,-9.714172,6.354133,7.505667,2.308885,-4.375084,9.164980,-7.604754,4.295637,-1.672501,-8.513945,-4.503852,5.403184,2.128723,-6.398331,8.459657,-1.478723,-8.434089,-5.305729,-1.570051,5.799277,-6.785600,8.381184,-1.901845,1.921701,-9.530824,-9.886780,-5.697848,7.118215,0.107374,1.174312,5.941243,4.309721,0.884856,-7.430468,2.194168,9.768099,-2.599400,-5.726326,5.179889,0.301113,2.431457,2.837750,-2.787548,3.264017,-4.570652,-4.719230,0.490233,-1.590500,-5.665194,-5.500041,-9.046530,1.764124,6.659085,-6.711476,5.534440,-4.671189,9.123199],[-0.712382,-3.844312,6.829514,2.843610,3.793795,7.373077,5.399279,-6.925525,9.739721,7.765549,8.219284,-3.298287,-5.773962,-6.251281,2.438954,-2.432114,5.883243,9.851654,3.558473,-1.675034,7.680691,-1.834893,1.063965,1.667777,-0.519693,-1.473278,1.405709,9.934887,-8.705944,-8.153465,8.128517,-5.494369,3.859923,4.016966,-6.171104,4.342397,-8.749559,-1.092764,-8.831102,-2.147490,9.018867,7.513067,-3.358286,-7.952229,-0.243375,-7.118916,4.750171,-0.847649,-2.626368,3.159553,1.482226,9.813834,9.778900,-0.975816,0.417265,-2.175325,4.423491,8.352349,-0.404517,-5.723530,-8.449961,-7.267082,1.726984,-2.254727,-9.546189,-7.662463,2.033799,7.431402,-3.263299,-9.795199,5.964554,-8.982480,-7.035977,-5.525181,2.287043,9.830109,3.946647,2.118801,-6.181343,-1.595050,0.135636,4.048587,-2.552619,9.576414,-3.386214,-3.723598,-7.840748,-2.953454,-3.122297,4.088302,7.933457,4.844347,-3.796618,-2.251503,9.129198,-5.171630,6.272467,2.292841,-3.344063,-0.200650,-2.768589,-7.213092,9.283371,-0.978581,6.783920,4.419583,-0.212839,1.813934,7.633453,-3.963316,8.524114,-2.958429,-7.738557,-7.523386,-3.288834,5.044408,-9.490420,-6.908333,-2.696862,1.660319,-8.004019,-8.899540,-8.093220,-0.886555,5.829630,-2.401460,2.053856,-4.909447,-9.150027,-7.930040,3.455948,4.981892,-7.593871,-7.852668,-4.096661,-5.275578,-8.145868,-2.434474,2.423122,3.404073],[7.028066,3.648113,-4.182682,-4.813335,-8.587456,4.485437,-2.247645,3.874798,-6.821564,0.775550,-6.407360,-8.770930,-9.875506,5.250626,5.042169,5.063636,-2.281570,5.403811,-5.252431,7.739993,-5.276799,-3.526916,3.423205,1.300941,6.718091,2.838332,7.972808,4.914010,-5.056663,2.131907,7.228167,-4.668980,6.279731,-5.247865,4.099554,-1.213358,-0.819601,-5.290379,2.481488,-2.169002,-4.735909,-5.499224,5.772490,2.929432,-7.966979,5.830318,0.163576,4.621205,6.380520,-0.247141,1.472994,-9.508938,-9.339816,0.860998,1.885096,-3.477928,1.281329,1.520452,-7.085508,-9.286804,3.130878,-7.058639,2.607786,8.278756,9.477892,7.704966,-9.856011,2.412072,-4.057598,-3.030528,-4.329095,4.015269,5.177760,-6.957536,-0.415860,-1.270284,-1.006073,-6.983142,-5.042571,-2.493853,-0.093434,-6.137707,7.615205,7.448046,2.338382,7.720779,-4.575319,7.162518,4.856472,-9.657688,2.704396,0.934607,0.637402,6.405171,2.239066,-2.906277,-9.646447,6.650504,-3.374970,3.105516,-8.316687,5.801098,-3.682209,2.765399,-7.904602,3.455205,-1.251656,4.812314,-3.797668,-5.962274,-6.799493,9.282993,0.338755,-5.972852,1.176972,0.756907,3.037394,6.672646,-9.078328,8.848551,-4.690089,-5.157293,-3.831738,-2.646908,-9.320762,-9.868114,1.574428,8.221435,-4.573474,-5.242947,-8.803649,-0.115140,-9.861220,7.339613,-7.397188,0.927347,7.854828,4.023554,6.827699,-0.895601],[-3.494750,-5.110166,2.944483,9.657149,-3.009022,9.082356,2.944253,-6.681900,9.977846,-5.765117,-1.245595,-8.014921,1.600876,9.392541,-3.227545,2.636266,9.064408,-8.957632,6.224255,-2.229354,-7.137855,-5.381880,8.557559,4.468100,-4.433247,-1.048015,-8.228232,-2.144536,4.566061,-3.010425,-8.583138,-1.778548,-3.829263,-2.355217,-4.067064,2.066935,-5.378668,2.152724,-6.488167,2.558222,-8.635806,7.026312,-6.975685,6.985096,-8.445475,8.799474,7.119255,-9.700412,0.381430,9.911230,4.725423,-0.642145,8.590561,-0.103132,-4.457573,-8.292752,3.700715,2.028542,-2.630055,5.643445,5.167239,5.676608,4.728177,-9.735638,-5.632457,-5.268343,-0.471704,8.356029,-9.388959,9.934246,1.040055,-3.142860,3.649537,1.432065,-5.620493,-4.376321,1.499708,-8.811701,9.960336,8.251417,-0.076808,-6.831723,-4.236535,-1.125843,6.185139,-9.247943,-3.210646,3.463066,-3.493628,1.829819,-1.195247,-3.633236,3.663102,-0.832126,7.615929,-9.521477,4.185480,-3.591577,-0.100049,2.542080,-8.538755,6.247640,-9.096132,7.314326,7.725877,6.332739,-4.554771,3.889368,-3.934415,3.113028,-4.354461,2.149633,-9.456057,3.203390,6.621001,-5.432015,-4.795443,-1.186340,-8.832590,-2.347973,-1.747449,8.533015,6.595045,-8.455007,-4.918006,-1.487316,9.846273,8.657512,8.853679,-0.570869,5.461044,7.094506,-3.745181,-3.641227,1.461364,-8.711182,-6.029970,-9.772898,7.868840,3.371007],[-9.770104,-8.095870,8.658702,8.363074,-5.815583,0.867840,-0.576723,-6.667487,-0.087223,-2.360771,6.565669,5.558819,-0.834025,3.573775,-2.020014,-5.268073,-4.271503,-5.564729,-4.343691,7.896404,-8.597186,-2.012290,4.133492,0.092096,9.884562,2.474730,0.481996,-4.227885,-5.901267,3.798716,-1.392817,-4.315563,-6.883864,-3.795650,-7.778662,4.438462,0.904575,-8.030614,-9.671523,-9.063053,3.903202,-6.291159,2.438289,-2.871540,0.986636,-4.690241,0.978265,-6.466596,-9.449645,-0.559586,-9.313174,6.119453,3.240929,-5.958969,4.752211,9.736033,-7.410857,4.219708,-4.379868,-0.963836,7.633422,5.866713,4.585156,-3.189551,2.522381,-1.150377,4.744153,7.615710,0.798017,-4.583660,-3.193154,2.831141,-1.455280,-6.656981,6.995759,-2.270800,-8.463566,9.701379,2.141580,9.326047,7.261983,9.637832,1.096541,2.356982,-6.655720,0.721403,-4.215277,-4.763378,-3.342174,9.008029,4.174634,-9.740584,-6.086137,1.714580,-7.276534,-3.540195,-8.092071,-3.831659,-4.326406,2.778291,1.004548,7.265806,2.349620,-2.681171,7.385240,8.329163,5.791852,-3.142857,-0.132743,-7.166053,-0.279584,-0.730724,-0.332994,-2.189289,-2.741950,5.223068,-4.949017,6.684871,-8.695976,5.876581,-3.478122,-9.708876,4.793294,5.520168,-5.564974,-0.957304,-0.525892,-3.340822,9.019476,3.717323,-8.773730,5.686844,3.785571,-3.095194,8.318495,3.216992,2.089006,8.300825,-5.280978,-3.199586],[-8.166214,7.115075,6.866236,9.362309,-5.631799,-3.293234,-8.364843,-8.741292,8.502560,2.394352,-0.980313,-4.889202,6.922255,-6.158454,-1.011721,-8.522578,5.308146,2.725114,4.065841,4.040382,6.293898,-7.920582,-0.323305,5.118931,-3.869281,-6.117852,-6.395357,-0.846673,-6.510836,3.354704,4.100435,-9.207662,-5.449174,9.537920,-2.612318,6.964338,-6.054681,0.147872,-1.515439,-6.547497,-9.442673,-6.021904,2.302226,-5.255277,3.454561,-6.530788,9.978818,-2.143371,-5.129459,-7.804466,-2.313048,-3.296620,6.347557,6.531465,2.318450,-4.355071,-0.792627,-3.965554,1.630319,-4.022598,-9.459740,1.650046,9.011222,0.616495,2.577929,-8.241304,-5.207009,6.837479,4.475476,7.598217,-3.096760,-4.511965,-7.837855,2.583704,7.567390,1.476563,-3.369608,6.354641,-5.352477,-8.554392,-0.465873,4.765560,9.011404,6.048404,-5.633472,0.454146,-1.376289,9.229093,-6.043841,9.598341,-3.658901,-4.309834,5.088812,-2.733610,-2.752694,-6.257431,-0.173896,3.352074,-1.822460,-8.921594,-1.530986,7.117050,2.700339,8.634713,2.519159,1.715856,2.024038,0.895171,6.170528,-2.771504,-6.463767,3.048371,1.190778,-6.104796,1.777978,-5.139224,6.089984,-0.326623,-9.544447,-3.464374,-4.223181,-2.509738,2.691879,7.110019,4.355637,2.672378,-9.714654,-2.416619,7.743764,9.416875,4.281670,-5.964705,2.679526,8.246212,7.964374,-3.367123,6.827943,7.726017,-6.365785,-7.916466],[7.407236,3.691291,-1.550661,5.043133,-0.321436,-7.967246,-3.358560,-3.452757,3.906621,8.664116,-0.505565,2.612194,-3.307663,-1.722383,3.968187,4.767187,-5.959117,-3.553474,-4.254994,8.334868,-3.022503,2.806786,-6.751784,-0.991609,3.570783,-0.675695,0.056389,-1.526554,5.887351,-7.075957,8.242341,2.736344,-2.191395,-2.696398,9.798863,-7.247178,8.546818,-7.371192,9.555349,0.994795,-4.328857,-2.577311,1.827014,-3.920003,-2.059298,2.875786,-4.457631,2.223343,-5.667087,7.752264,7.354105,0.790003,9.954966,5.672619,7.465051,-9.534722,-0.856135,6.855063,9.894973,-0.154078,8.371503,5.701251,-7.476004,-8.129127,-5.404155,-0.236251,0.398090,-5.364419,0.298156,-5.768777,-7.251638,2.988764,4.055777,5.947575,-6.629509,-3.798597,7.522818,4.057556,2.702671,5.027850,6.525293,1.116011,2.989614,-5.017017,5.273265,4.546446,1.482732,3.770871,-1.647245,9.242394,-2.048894,-2.104410,4.794276,-1.297535,5.427052,-4.356498,5.901557,-0.539853,9.413233,-7.593276,7.221650,-2.309481,-6.430694,6.068546,-6.714839,7.319215,6.931311,2.510067,4.073793,2.598531,6.018965,2.736241,4.602304,3.101338,-5.784463,-3.745513,-0.486662,-3.002113,-1.101080,4.294202,-9.295000,3.695582,-7.914239,-0.754583,-3.626093,-1.269616,0.514743,7.554965,9.140109,9.479096,-4.383169,9.251645,6.087714,5.435865,-0.506554,-5.535757,7.525708,-5.688660,-3.260592,4.337237],[-4.320707,-7.373704,2.423515,-6.351136,8.143925,1.812145,9.194058,-4.653124,-9.394403,-0.306659,-3.499807,-4.511807,8.083436,0.916159,1.641731,-0.826053,-0.181714,-8.059791,-9.858183,7.605311,-5.974291,8.570827,2.510593,-7.753034,2.244261,-2.907413,-6.089295,9.700923,1.055725,6.873068,2.675968,-0.500871,7.620748,-8.502714,-4.078161,6.610210,-1.265408,-5.525253,-5.451818,9.644795,-2.738965,5.330413,-0.031764,-2.731138,9.646097,9.161142,6.569422,-3.586919,-3.661245,6.603340,-8.062663,0.376359,0.425559,0.089471,7.650018,-1.090379,-5.173779,-8.475914,-1.295910,2.633846,-4.813700,5.848487,-4.939424,-0.327665,-3.323148,2.580412,-9.309831,0.762790,5.332562,6.454268,3.213959,-5.691814,8.924822,5.891524,2.196362,0.844992,5.585267,6.285985,3.718539,-4.908807,1.221879,-2.196069,-7.846071,-1.134413,-8.729599,-2.924565,8.343090,-3.097283,8.019548,-0.095301,-1.888176,5.220653,-7.347615,9.304691,-4.298743,8.509457,-3.888208,-2.627902,6.949448,-0.409633,-5.837416,-9.633648,8.315818,7.019071,-1.895595,9.347959,7.666375,-3.463465,0.048626,5.980798,1.459145,-5.315941,2.846098,-8.104309,0.405357,-6.969301,-8.029355,8.257286,4.036048,-9.151296,-3.054958,-7.135343,-1.499053,-5.734003,6.482477,-7.051414,-7.058470,-9.192654,0.993002,8.258344,9.171662,-4.782115,-2.945711,2.952650,-3.068239,8.794028,3.347330,4.676974,-7.620541,5.594100]], dtype = "float32")#candidate|5980|(8, 140)|const|float32
call_5979 = func_2804_call(relay.reshape(const_5980.astype('float32'), [16, 14, 5]), relay.reshape(const_5980.astype('float32'), [16, 14, 5]), )
call_5981 = func_2804_call(relay.reshape(const_5980.astype('float32'), [16, 14, 5]), relay.reshape(const_5980.astype('float32'), [16, 14, 5]), )
const_5987 = relay.const([[[-8.058639,2.675965,4.765337,7.367790],[-7.177495,-4.031385,7.122709,1.848095],[-1.664843,0.337084,-1.889477,0.435284],[-4.955719,-2.765564,8.383360,9.587485],[9.175743,1.683631,-2.928825,8.111177],[-4.090765,8.944431,-3.787626,9.236726],[-8.748433,9.312598,-3.229472,1.725323],[-7.114304,8.270346,-7.326400,-2.292037],[8.349831,-8.224312,-6.586923,0.572459],[3.189578,-6.800868,7.952155,-8.726445],[-8.844211,-5.843095,-3.685058,6.992214],[8.316967,-0.214113,4.648457,6.965892],[9.135752,-1.055370,-0.538051,-5.372940]],[[-9.233083,3.409460,-8.826887,3.474547],[7.785180,2.350295,-6.219488,-3.369242],[2.401347,7.163729,0.329014,-7.849781],[-3.769186,-6.127339,-5.312789,-6.751685],[4.510606,-9.801904,1.597797,-7.771319],[5.568078,-4.595984,-2.063658,-3.635579],[-8.035814,-1.140562,-8.754637,-4.429514],[8.849213,0.952045,0.742303,-1.356855],[3.908654,-6.351447,1.007933,3.555329],[3.197333,-4.183479,1.379108,1.569234],[-4.176733,7.661035,-6.303704,5.977903],[1.478665,9.018610,-3.131718,1.369578],[-2.858561,-3.023581,4.690843,0.613813]],[[1.300018,-2.668622,-2.241919,-6.579290],[-4.078325,2.247083,8.026357,-8.061349],[-2.585664,0.147666,-4.754240,-9.411885],[4.815624,-3.646016,5.044940,6.081007],[5.534385,4.510122,1.246192,-9.246582],[7.968226,4.014652,-4.188891,3.931809],[1.691923,1.893226,-7.076464,8.996666],[-0.183297,-4.844261,7.312297,-2.448355],[5.856912,-9.365459,-8.644874,-3.640586],[-0.897302,-1.742473,-3.641815,0.807567],[9.103630,3.193844,9.535508,6.796720],[-5.297586,8.228983,2.449399,-7.059519],[9.577271,1.474847,8.452039,5.375850]],[[5.125210,-4.898888,-9.315935,-4.340447],[-8.200988,1.044935,-2.445266,4.618343],[-9.147274,-6.553399,-5.014049,-8.516596],[8.091776,0.121251,-0.530318,-7.275083],[6.662681,0.032812,3.909929,6.087614],[8.789593,6.291678,5.636326,-9.862819],[9.679312,2.076667,4.501770,1.674299],[4.475386,1.815193,7.312210,-1.648173],[-7.939882,-5.256753,3.588958,6.102947],[-2.889594,-1.235282,5.430263,0.096410],[7.396519,-0.355095,9.160539,7.619961],[4.769611,-3.528543,-2.976933,9.222090],[-7.051368,-9.868725,1.898020,-2.548622]],[[-3.190818,6.464903,4.734541,-7.028628],[3.274213,8.537170,-1.089953,1.362198],[2.798510,6.195751,-9.498996,-6.008272],[-0.882889,-2.629619,-7.975371,-3.771697],[5.304115,-0.231247,-2.953924,1.145397],[2.405075,-0.810780,9.550400,6.751256],[7.829973,2.183394,0.879896,-7.754309],[-1.977342,4.232355,8.990735,-9.391432],[4.930467,8.748703,0.275718,5.226233],[5.651378,2.561293,-7.302087,6.236686],[9.925152,7.121856,-4.338027,-0.622109],[1.906736,9.431919,7.670202,1.034765],[-9.138193,1.398865,-1.277519,8.432747]],[[-8.193140,-9.927988,9.197194,7.741385],[-0.877839,-0.293855,-0.101362,-4.796872],[-0.029326,7.027992,4.124913,0.751856],[9.179851,4.636695,4.074632,-3.318869],[2.504530,-6.728151,-4.318646,5.748217],[8.253517,-6.496252,8.031880,5.147460],[-5.562087,1.043915,7.735339,-1.322427],[0.613525,-9.454878,-1.688315,9.747429],[-6.744680,-9.433352,6.841912,2.763875],[2.059751,-3.794480,-3.930348,5.816914],[-6.886897,-0.692535,2.184210,8.104813],[3.921226,3.881334,-1.006343,0.345855],[5.093601,1.866370,-7.704178,2.760432]]], dtype = "float32")#candidate|5987|(6, 13, 4)|const|float32
bop_5988 = relay.not_equal(uop_5873.astype('bool'), relay.reshape(const_5987.astype('bool'), relay.shape_of(uop_5873))) # shape=(6, 13, 4)
bop_5991 = relay.not_equal(uop_5875.astype('bool'), relay.reshape(const_5987.astype('bool'), relay.shape_of(uop_5875))) # shape=(6, 13, 4)
output = relay.Tuple([call_5925,call_5932,call_5967,call_5971,call_5973,call_5979,const_5980,bop_5988,])
output2 = relay.Tuple([call_5926,call_5933,call_5968,call_5972,call_5974,call_5981,const_5980,bop_5991,])
func_6013 = relay.Function([], output)
mod['func_6013'] = func_6013
mod = relay.transform.InferType()(mod)
mutated_mod['func_6013'] = func_6013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6013_call = mutated_mod.get_global_var('func_6013')
call_6014 = func_6013_call()
output = call_6014
func_6015 = relay.Function([], output)
mutated_mod['func_6015'] = func_6015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4997_call = mod.get_global_var('func_4997')
func_4999_call = mutated_mod.get_global_var('func_4999')
call_6053 = relay.TupleGetItem(func_4997_call(), 1)
call_6054 = relay.TupleGetItem(func_4999_call(), 1)
func_3463_call = mod.get_global_var('func_3463')
func_3464_call = mutated_mod.get_global_var('func_3464')
call_6058 = relay.TupleGetItem(func_3463_call(), 0)
call_6059 = relay.TupleGetItem(func_3464_call(), 0)
output = relay.Tuple([call_6053,call_6058,])
output2 = relay.Tuple([call_6054,call_6059,])
func_6086 = relay.Function([], output)
mod['func_6086'] = func_6086
mod = relay.transform.InferType()(mod)
output = func_6086()
func_6087 = relay.Function([], output)
mutated_mod['func_6087'] = func_6087
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6095 = relay.var("var_6095", dtype = "float64", shape = ())#candidate|6095|()|var|float64
const_6096 = relay.const([[[-3.776415,6.925781,3.908454,-9.326342,3.595192,9.652455,-1.959846,-4.904379,-2.135629,-2.330986,9.823788],[-1.618343,-6.071859,0.609485,0.144979,0.455920,7.348939,0.298232,4.722473,2.334838,-0.575779,5.480747],[4.703893,-0.710058,-8.124611,7.067125,0.924080,-5.792193,-5.725190,9.142201,-3.470448,1.885676,8.777603],[3.422793,-8.535490,5.080499,8.768036,1.291249,-9.939887,8.986101,1.105691,-5.078761,-5.052736,-9.118425],[-2.496849,-0.404519,-7.857519,-9.112602,3.061608,-1.794443,-0.069681,-8.340037,9.425518,6.737470,-0.172240],[-5.118066,4.622307,-3.046618,3.782299,-3.304856,3.548974,6.988851,-2.224984,0.922949,4.276782,8.165502],[-7.765593,8.106301,-8.620581,4.296564,9.667137,-7.453245,7.074164,-6.410496,2.734596,-9.497810,-9.193898],[-8.235545,-0.595217,-7.222038,6.248135,5.270812,7.012245,3.117005,8.347828,-9.144767,-0.492057,-6.029913],[-7.422857,5.452767,8.362411,-8.360132,2.740817,4.167099,-5.942951,7.400853,9.373653,1.079421,7.416452]]], dtype = "float64")#candidate|6096|(1, 9, 11)|const|float64
bop_6097 = relay.floor_mod(var_6095.astype('float64'), const_6096.astype('float64')) # shape=(1, 9, 11)
func_4316_call = mod.get_global_var('func_4316')
func_4317_call = mutated_mod.get_global_var('func_4317')
call_6105 = relay.TupleGetItem(func_4316_call(), 1)
call_6106 = relay.TupleGetItem(func_4317_call(), 1)
uop_6136 = relay.cos(bop_6097.astype('float64')) # shape=(1, 9, 11)
func_2080_call = mod.get_global_var('func_2080')
func_2084_call = mutated_mod.get_global_var('func_2084')
const_6147 = relay.const([2,3,-8,2,-2,3,-5,-2,3,6,5,9,7,8,-8,3,2,-8,9,-6,-4,-8,3,9,6,-2,-5,6,-2,5,5,10,4,-6,7,-3,-2,1,1,-1,-7,7,3,-4,-10,-3,-7,-2,10,-3,1,1,6,-1,3,-1,-3,2,4,9,5,10,-8,2,-2,8,-2,9,10,-3,9,7,4,8,-7,5,2,3,-10,7,-1,-5,3,-9,3,-9,-7,6,6,-3,-4,5,6,5,3,7,-8,-7,6,3,-9,4,9,-9,-6,9,5,-6,-4,-6,-3,-2], dtype = "int8")#candidate|6147|(112,)|const|int8
call_6146 = relay.TupleGetItem(func_2080_call(relay.reshape(const_6147.astype('int8'), [112,]), relay.reshape(call_6105.astype('int8'), [1120,]), ), 0)
call_6148 = relay.TupleGetItem(func_2084_call(relay.reshape(const_6147.astype('int8'), [112,]), relay.reshape(call_6105.astype('int8'), [1120,]), ), 0)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_6150 = relay.TupleGetItem(func_2162_call(), 0)
call_6151 = relay.TupleGetItem(func_2163_call(), 0)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_6158 = relay.TupleGetItem(func_1556_call(), 0)
call_6159 = relay.TupleGetItem(func_1557_call(), 0)
output = relay.Tuple([call_6105,uop_6136,call_6146,const_6147,call_6150,call_6158,])
output2 = relay.Tuple([call_6106,uop_6136,call_6148,const_6147,call_6151,call_6159,])
func_6167 = relay.Function([var_6095,], output)
mod['func_6167'] = func_6167
mod = relay.transform.InferType()(mod)
mutated_mod['func_6167'] = func_6167
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6168 = relay.var("var_6168", dtype = "float64", shape = ())#candidate|6168|()|var|float64
func_6167_call = mutated_mod.get_global_var('func_6167')
call_6169 = func_6167_call(var_6168)
output = call_6169
func_6170 = relay.Function([var_6168], output)
mutated_mod['func_6170'] = func_6170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5063_call = mod.get_global_var('func_5063')
func_5064_call = mutated_mod.get_global_var('func_5064')
call_6201 = relay.TupleGetItem(func_5063_call(), 0)
call_6202 = relay.TupleGetItem(func_5064_call(), 0)
uop_6209 = relay.acos(call_6201.astype('float64')) # shape=(8, 14, 10)
uop_6211 = relay.acos(call_6202.astype('float64')) # shape=(8, 14, 10)
func_4031_call = mod.get_global_var('func_4031')
func_4033_call = mutated_mod.get_global_var('func_4033')
var_6217 = relay.var("var_6217", dtype = "float64", shape = (182, 6))#candidate|6217|(182, 6)|var|float64
call_6216 = func_4031_call(relay.reshape(var_6217.astype('float64'), [12, 7, 13]))
call_6218 = func_4031_call(relay.reshape(var_6217.astype('float64'), [12, 7, 13]))
func_4031_call = mod.get_global_var('func_4031')
func_4033_call = mutated_mod.get_global_var('func_4033')
call_6234 = func_4031_call(relay.reshape(call_6216.astype('float64'), [12, 7, 13]))
call_6235 = func_4031_call(relay.reshape(call_6216.astype('float64'), [12, 7, 13]))
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_6243 = relay.TupleGetItem(func_2587_call(), 3)
call_6244 = relay.TupleGetItem(func_2588_call(), 3)
func_5533_call = mod.get_global_var('func_5533')
func_5535_call = mutated_mod.get_global_var('func_5535')
call_6248 = relay.TupleGetItem(func_5533_call(), 1)
call_6249 = relay.TupleGetItem(func_5535_call(), 1)
var_6256 = relay.var("var_6256", dtype = "float64", shape = (12, 7, 13))#candidate|6256|(12, 7, 13)|var|float64
bop_6257 = relay.floor_mod(call_6216.astype('float32'), relay.reshape(var_6256.astype('float32'), relay.shape_of(call_6216))) # shape=(12, 7, 13)
bop_6260 = relay.floor_mod(call_6218.astype('float32'), relay.reshape(var_6256.astype('float32'), relay.shape_of(call_6218))) # shape=(12, 7, 13)
func_1824_call = mod.get_global_var('func_1824')
func_1826_call = mutated_mod.get_global_var('func_1826')
var_6277 = relay.var("var_6277", dtype = "uint32", shape = (363,))#candidate|6277|(363,)|var|uint32
call_6276 = relay.TupleGetItem(func_1824_call(relay.reshape(var_6277.astype('uint32'), [11, 3, 11])), 0)
call_6278 = relay.TupleGetItem(func_1826_call(relay.reshape(var_6277.astype('uint32'), [11, 3, 11])), 0)
output = relay.Tuple([uop_6209,var_6217,call_6234,call_6243,call_6248,bop_6257,call_6276,var_6277,])
output2 = relay.Tuple([uop_6211,var_6217,call_6235,call_6244,call_6249,bop_6260,call_6278,var_6277,])
func_6281 = relay.Function([var_6217,var_6256,var_6277,], output)
mod['func_6281'] = func_6281
mod = relay.transform.InferType()(mod)
var_6282 = relay.var("var_6282", dtype = "float64", shape = (182, 6))#candidate|6282|(182, 6)|var|float64
var_6283 = relay.var("var_6283", dtype = "float64", shape = (12, 7, 13))#candidate|6283|(12, 7, 13)|var|float64
var_6284 = relay.var("var_6284", dtype = "uint32", shape = (363,))#candidate|6284|(363,)|var|uint32
output = func_6281(var_6282,var_6283,var_6284,)
func_6285 = relay.Function([var_6282,var_6283,var_6284,], output)
mutated_mod['func_6285'] = func_6285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2297_call = mod.get_global_var('func_2297')
func_2299_call = mutated_mod.get_global_var('func_2299')
call_6366 = relay.TupleGetItem(func_2297_call(), 0)
call_6367 = relay.TupleGetItem(func_2299_call(), 0)
func_5710_call = mod.get_global_var('func_5710')
func_5714_call = mutated_mod.get_global_var('func_5714')
const_6374 = relay.const(6.387227, dtype = "float64")#candidate|6374|()|const|float64
const_6375 = relay.const([-9.751318,-2.854222,-9.868604,-2.520563,-8.917844,-5.681324,-3.526309,3.096377,4.543514,-9.646639,7.479787,2.452701,-9.332539,7.806545,-2.685724,9.482676,-1.041969,-2.601436,-6.067057,-1.570869,7.562999,-8.148881,1.707385,-6.706281,1.666276,-6.782790,-3.667907,0.010583,-7.238994,-7.836825,-0.122859,4.242898,-4.272319,5.866274,-3.389382,8.202048,-8.094917,6.293648,0.562581,-1.307881,-6.205395,-2.752978,-0.667314,-4.851415,-3.477601,-4.208176,-8.209370,-9.947555,1.341287,7.539044,8.301228,4.066014,-6.843891,2.267389,-5.042114,-5.584874,-2.225359,-9.210912,-3.144683,2.132320,7.955474,-0.784336,9.112562,-9.353748,-0.016515,-2.068558,2.019117,-7.043057,-3.637659,2.369326,1.860849,-5.975672,-0.318838,8.275726,9.115736,-2.894319,-3.045443,-1.632537,3.915789,-4.976400,5.772345,7.184750,-5.804777,-7.453644,8.430018,5.907518,-5.635154,0.287787], dtype = "float64")#candidate|6375|(88,)|const|float64
call_6373 = relay.TupleGetItem(func_5710_call(relay.reshape(const_6374.astype('float64'), []), relay.reshape(const_6375.astype('float64'), [1, 11, 8]), ), 0)
call_6376 = relay.TupleGetItem(func_5714_call(relay.reshape(const_6374.astype('float64'), []), relay.reshape(const_6375.astype('float64'), [1, 11, 8]), ), 0)
output = relay.Tuple([call_6366,call_6373,const_6374,const_6375,])
output2 = relay.Tuple([call_6367,call_6376,const_6374,const_6375,])
func_6399 = relay.Function([], output)
mod['func_6399'] = func_6399
mod = relay.transform.InferType()(mod)
mutated_mod['func_6399'] = func_6399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6399_call = mutated_mod.get_global_var('func_6399')
call_6400 = func_6399_call()
output = call_6400
func_6401 = relay.Function([], output)
mutated_mod['func_6401'] = func_6401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3789_call = mod.get_global_var('func_3789')
func_3790_call = mutated_mod.get_global_var('func_3790')
call_6418 = relay.TupleGetItem(func_3789_call(), 0)
call_6419 = relay.TupleGetItem(func_3790_call(), 0)
func_2804_call = mod.get_global_var('func_2804')
func_2807_call = mutated_mod.get_global_var('func_2807')
const_6461 = relay.const([[6.512130],[-8.557393],[-1.499623],[6.240027],[-1.491174],[-2.916525],[9.571769],[-7.681644],[8.416853],[1.228496],[2.459957],[-0.858272],[4.962145],[-4.751670],[4.329338],[5.365521],[-5.031623],[7.378359],[-3.494333],[5.117979],[2.485641],[-2.269621],[-3.086387],[-0.176923],[-1.489181],[9.797476],[8.134192],[4.241418],[-1.759206],[-7.775906],[-2.344438],[-4.859752],[0.333427],[-7.246413],[-4.580708],[-5.657369],[7.345485],[5.060517],[-9.720596],[3.356938],[7.224705],[-8.802949],[9.604391],[2.993547],[1.700331],[7.890140],[9.430943],[-5.869643],[4.817275],[-1.653701],[2.433652],[-9.709047],[2.910559],[-7.954857],[1.528582],[-5.619678],[3.228120],[2.579040],[-7.242847],[-3.132628],[4.406064],[-3.155235],[0.419235],[4.450243],[2.637489],[-8.999134],[6.088684],[5.758431],[-3.971621],[-3.061855],[-5.021071],[-6.601789],[2.599912],[-7.287027],[6.751268],[-6.361292],[-9.814361],[7.488213],[5.747366],[-4.954313],[1.900572],[8.880685],[5.214897],[5.868654],[7.722748],[5.432542],[3.182885],[7.378398],[-2.438921],[-6.318789],[-9.613063],[-1.259376],[6.491308],[-4.968947],[-4.612078],[8.510002],[6.185781],[-1.896537],[-4.907960],[3.539812],[0.087425],[0.736208],[-3.867206],[-0.543997],[-4.574117],[-5.736585],[5.406659],[9.645970],[9.967832],[2.905722],[-4.259086],[4.864353],[-4.814504],[7.526049],[4.700643],[-0.353223],[5.266059],[3.449800],[-2.198763],[-4.317367],[9.199087],[5.468616],[1.790909],[6.463170],[-3.948299],[1.034920],[-0.440486],[-3.551006],[-9.757105],[6.703374],[-6.329879],[9.598832],[1.571540],[-4.226552],[-2.105427],[-5.538824],[4.524620],[-4.717467],[-5.439922],[1.200823],[-9.485314],[7.617732],[3.590469],[1.497064],[2.162043],[-4.228235],[-7.906597],[-1.927063],[-2.244673],[2.289965],[5.329975],[-5.821092],[7.860416],[-6.856473],[8.177383],[-0.592226],[-2.088040],[-9.453224],[-7.834385],[2.526158],[-4.178705],[3.009052],[2.185420],[-6.584853],[-3.120266],[-9.796176],[2.069466],[5.023805],[4.232177],[-4.719240],[9.611628],[0.937147],[-9.837950],[-9.685256],[7.388088],[9.393248],[4.056242],[3.452455],[-4.023257],[-8.252684],[5.820618],[-2.669503],[-7.912263],[-5.178365],[4.691107],[-1.718635],[6.827528],[-9.343139],[3.717984],[-6.721570],[5.398643],[-7.079799],[0.738167],[6.822585],[0.331445],[-6.658454],[7.325113],[9.839871],[-6.558624],[3.342817],[-9.080019],[2.318114],[6.845693],[8.036838],[-2.560884],[-1.037744],[9.923405],[-7.889084],[-8.363678],[-3.494559],[2.443594],[-7.026618],[-5.518447],[-0.785957],[2.580986],[-6.384308],[0.630739],[-5.140019],[-4.409104],[5.243218],[3.006225],[-8.066316],[-3.264903],[0.152476],[-4.929860],[-7.688291],[4.668436],[-1.960738],[-0.199045],[-3.455293],[3.261793],[5.705226],[-9.793908],[9.932066],[-2.965105],[0.217378],[-6.008498],[-2.740814],[-0.961163],[1.438134],[-3.186027],[7.179148],[4.494043],[2.983075],[-4.619097],[0.017440],[-7.565343],[1.802064],[-1.916932],[5.549672],[7.913727],[6.670426],[-2.288742],[9.117387],[7.342817],[-6.228977],[-0.080281],[7.118635],[4.738136],[-7.100797],[8.310658],[8.659971],[-2.510018],[-9.421192],[-7.382014],[2.216179],[9.088961],[6.139105],[1.751108],[-4.559361],[-4.502785],[-7.451639],[-1.252882],[-0.519658],[-5.678481],[-0.251514],[-7.456012],[8.815892],[-2.204393],[-4.488576],[-0.792415],[-8.585857],[-5.164419],[5.766507],[-9.770511],[-9.014909],[-5.556334],[-5.575698],[3.728104],[6.836897],[1.965725],[1.730570],[8.304472],[-2.508476],[-2.254719],[-1.813509],[8.708096],[-6.797261],[1.995700],[0.782515],[-8.248036],[-7.732279],[-9.520066],[5.337049],[0.559663],[6.942337],[-7.855724],[-8.213708],[4.068703],[1.928184],[7.754071],[-6.662348],[1.832714],[-0.583131],[9.968378],[-7.558052],[-3.687387],[-9.101239],[8.564107],[-3.253849],[-0.523251],[8.259525],[-5.283458],[7.413048],[2.353602],[9.694235],[-5.086294],[4.221589],[4.140292],[-4.808133],[0.687369],[-6.993507],[4.736562],[-6.485711],[-6.037070],[3.370207],[-6.221001],[-6.513362],[0.585646],[-9.156801],[-9.204542],[5.977752],[-5.758479],[-5.767214],[6.833836],[-4.692713],[-1.379669],[-9.632804],[5.810445],[-8.501369],[7.260536],[4.382776],[0.854862],[-0.239395],[4.723798],[2.539915],[-1.959417],[-4.303449],[8.860851],[-5.730736],[-6.181533],[2.466911],[1.054093],[-6.470916],[-2.523851],[7.447543],[1.680410],[1.360544],[-6.062747],[8.195083],[-5.173427],[0.741743],[2.399188],[8.674001],[0.610289],[4.239314],[-7.163161],[-8.322723],[-0.261098],[1.795299],[0.225040],[-8.728455],[4.359008],[2.624965],[6.405045],[8.490615],[7.653622],[3.118899],[-5.980412],[5.983945],[-1.691227],[5.054596],[6.575731],[3.998353],[8.406700],[-2.978975],[0.261795],[1.218276],[-7.281139],[-1.875235],[6.577775],[-4.968368],[-5.411924],[5.984025],[-7.734103],[-2.246843],[-0.741002],[-1.560349],[5.245896],[6.311625],[-2.399149],[-6.760131],[7.402645],[-2.230500],[-2.554882],[1.759771],[-2.781335],[9.672042],[7.028883],[1.415451],[4.568380],[7.589152],[-4.429482],[-0.004829],[7.499963],[-8.326294],[6.556802],[0.478026],[-9.212461],[4.202554],[-6.123549],[-8.844894],[-6.061342],[7.079004],[-6.609188],[3.207237],[9.582183],[1.602795],[-4.118255],[3.230420],[-3.589790],[6.075274],[-0.873265],[-8.018654],[-3.449174],[-0.240560],[-1.467456],[3.270590],[-2.130981],[3.674607],[-8.514547],[-9.004677],[8.067202],[5.118824],[9.793828],[7.850406],[-4.881352],[-1.253572],[0.064197],[1.569108],[-8.970359],[-2.957502],[-2.935731],[7.728717],[-8.292395],[4.572363],[9.629730],[-4.329400],[-9.624096],[1.813608],[5.212245],[0.244214],[0.750898],[-8.730918],[-5.509434],[5.991552],[3.854641],[4.379698],[5.851405],[-3.025373],[8.148115],[-1.537611],[-1.780002],[8.305413],[-8.995546],[-6.917521],[2.904270],[7.599399],[3.619495],[8.582154],[6.007032],[-7.284408],[-0.201349],[-3.606159],[-6.847250],[-7.010196],[1.791391],[1.083193],[1.287169],[-0.237755],[6.198507],[5.864466],[-4.039363],[5.763852],[8.069419],[7.457838],[5.268270],[4.055535],[1.145670],[-3.259074],[4.311559],[-0.776937],[2.029858],[-3.285404],[-2.114054],[2.144236],[2.916318],[6.260176],[1.762477],[-2.080962],[7.223138],[-4.519953],[8.553338],[2.324552],[6.403514],[4.677117],[-5.023946],[5.971164],[2.117022],[-6.826664],[-1.454018],[5.537831],[9.696069],[9.945158],[2.447127],[6.897811],[9.978705],[-1.303024],[5.424642],[-0.848280],[1.615429],[4.748837],[0.356230],[9.337231],[-7.316451],[-7.306681],[8.864458],[9.803454],[-7.971243],[-8.662714],[-5.086405],[6.000378],[9.362170],[-1.099252],[6.802257],[2.285405],[-9.626906],[-0.964276],[-2.196435],[-3.793235],[4.575649],[7.146208],[-6.252251],[7.258220],[-1.470149],[7.345918],[0.808597],[-2.750860],[-0.586533],[-3.993802],[3.094696],[-8.964157],[-7.454696],[1.126498],[-2.943839],[-9.519082],[4.383399],[6.164218],[-6.797775],[-5.732381],[-1.316702],[7.041966],[-6.211551],[-3.809854],[-4.627560],[-9.344251],[-5.141309],[-7.975140],[5.372519],[5.713276],[4.625331],[-4.244425],[-1.799145],[6.334868],[-1.084897],[6.472585],[1.215187],[8.506293],[-1.195227],[-0.157908],[-9.715178],[9.559806],[4.455735],[5.370482],[8.452928],[-8.547612],[-8.953343],[9.349451],[-7.203069],[9.893567],[9.847675],[5.511944],[3.592749],[-3.880146],[-1.833680],[4.052346],[-9.697516],[-2.769732],[-5.707071],[-8.965247],[-1.550503],[-0.536138],[6.502755],[5.931790],[-0.183033],[7.282584],[2.214977],[-1.116841],[6.626040],[9.537301],[6.455460],[-1.871491],[3.838880],[0.874026],[-1.685010],[2.015931],[2.351161],[-1.330791],[-8.914547],[-5.477739],[-3.678542],[-7.923463],[3.877216],[4.546883],[5.978306],[-6.180848],[3.504735],[-2.448741],[7.653038],[-9.484479],[-6.115266],[3.417163],[4.403265],[-8.082329],[1.167288],[0.139960],[-6.860218],[-7.062686],[-9.495338],[-5.877328],[-2.188506],[2.051042],[0.455537],[-9.634316],[3.933927],[9.539363],[-3.615112],[1.499870],[-8.951677],[4.840919],[1.899658],[1.968385],[-0.605399],[5.908424],[5.055192],[7.562058],[-8.483405],[4.681327],[-4.395889],[9.046105],[-0.159872],[0.202206],[2.581753],[0.186269],[6.070498],[1.698316],[2.225142],[-4.072386],[-3.125999],[-6.161506],[-3.644412],[9.121546],[-3.840769],[-3.952843],[-1.393032],[6.230973],[-0.003567],[-0.752490],[7.135534],[0.318182],[-7.578113],[5.024039],[-7.844531],[-0.065350],[5.470008],[-0.943048],[-8.904428],[3.972976],[1.393575],[4.575200],[0.758990],[-7.518252],[-7.318079],[9.143597],[-5.876331],[-8.237545],[2.399747],[-3.457072],[9.230695],[9.531754],[-8.743583],[-1.822656],[1.586337],[3.673421],[-9.899002],[3.904654],[2.735300],[9.633990],[-7.656307],[-7.989473],[-2.077875],[3.687370],[-4.482286],[7.037630],[-7.315247],[0.431067],[-2.264361],[1.771553],[6.184740],[-6.987389],[-0.990932],[5.726196],[-8.269046],[0.863464],[7.810591],[1.875545],[-5.667239],[2.047226],[4.028061],[-5.223378],[3.924707],[-8.613222],[-7.948791],[-0.286520],[-3.302456],[4.400120],[-0.747409],[3.081467],[8.066588],[7.418048],[-3.494591],[-4.422459],[2.128006],[4.729268],[-6.934889],[3.154776],[4.591728],[-5.884434],[8.306135],[7.967387],[3.485242],[-8.202205],[4.315357],[-2.671301],[-4.946680],[4.497959],[6.385545],[7.096542],[-1.429944],[4.565056],[9.531146],[-2.518933],[-2.056248],[-8.435096],[9.027254],[1.518978],[-4.050328],[-0.905442],[5.278998],[-3.825932],[-3.082208],[-5.110581],[-8.495116],[3.736333],[9.094840],[8.004174],[4.595605],[3.580048],[-3.327180],[2.012059],[-3.359449],[3.537358],[1.993757],[-7.709815],[-1.541942],[-5.643671],[4.624668],[-7.732784],[8.590181],[-8.684830],[-1.469416],[5.776207],[5.990038],[1.796608],[-5.460190],[-3.486269],[-5.902939],[6.526316],[8.628148],[-0.948412],[-0.782839],[6.281188],[-9.180415],[8.343172],[0.316550],[-6.600438],[-8.968872],[0.075490],[-9.018101],[3.168020],[9.523991],[9.489997],[2.233482],[2.500192],[9.297630],[2.305540],[6.048892],[2.599485],[-0.030743],[3.007818],[-9.930866],[-8.101835],[3.920005],[-9.461864],[-2.362960],[-2.111280],[1.899102],[5.001958],[-8.037057],[-9.285136],[3.878979],[6.705001],[-1.833613],[-4.785488],[-6.750470],[-0.443193],[3.317409],[9.946383],[-8.434338],[-3.165956],[9.193058],[-9.031757],[3.563948],[-8.634735],[2.839846],[9.050206],[-6.181143],[1.513687],[9.304510],[6.233797],[7.139645],[-3.215566],[-1.249963],[7.996731],[5.710132],[-9.120772],[-9.648194],[-4.808234],[-8.390409],[5.245134],[2.501715],[-8.516718],[5.405192],[-0.908997],[1.147500],[-5.083401],[8.756730],[9.602008],[-3.099549],[-6.595507],[1.363324],[6.842106],[7.893963],[2.132838],[-4.081468],[3.791231],[3.082423],[0.572279],[7.434537],[5.061012],[6.139654],[9.670804],[-4.687907],[0.659655],[5.856331],[-6.436935],[-8.913035],[-3.127009],[0.725706],[4.389346],[-5.474238],[4.743129],[3.901464],[3.697524],[-4.573129],[8.123972],[-4.598128],[-8.619268],[-9.849625],[-0.133253],[9.323660],[-0.141824],[-5.178342],[-7.521389],[-4.190961],[6.550224],[-9.311397],[-8.807027],[7.679027],[3.022207],[-6.516013],[2.178587],[1.105392],[7.068293],[6.989276],[-0.216192],[-4.838769],[-1.512483],[9.473724],[5.155334],[8.954001],[6.448782],[1.303809],[2.681203],[2.146912],[5.296640],[6.949418],[-1.254878],[-0.880243],[-5.571048],[0.045196],[6.551865],[9.819424],[-5.031454],[-1.456581],[-0.762738],[-3.446628],[2.240457],[4.926351],[-3.429905],[0.062609],[-1.484505],[4.413746],[-0.700380],[-6.817815],[2.171136],[3.645636],[-0.781997],[3.544965],[5.562909],[-7.281293],[4.100398],[2.726547],[-4.878980],[0.645927],[1.766855],[-8.059147],[8.176038],[7.869398],[-6.507932],[2.909920],[5.039741],[-5.671035],[0.651488],[4.554812],[4.281404],[4.955283],[-5.374588],[9.980426],[5.769865],[-2.167264],[-6.225638],[9.352346],[-7.518167],[4.503547],[-8.405550],[-0.773618],[6.375188],[4.667457],[-0.649298],[2.127798],[-9.872624],[-3.106911],[-6.910894],[-1.837981],[-7.008218],[-7.658841],[3.095781],[4.269925],[-4.167442],[-2.248002],[4.073615],[0.433215],[8.423092],[0.711307],[3.946060],[0.536598],[8.183262],[-0.007878],[-4.709082],[-0.849029],[8.630452],[9.903824],[-0.555714],[-0.795463],[7.120794],[4.491055],[-1.780512],[3.547020],[-2.936767],[5.022008],[1.981450],[6.768129],[6.176672],[-6.137908],[-3.463090],[-9.955437],[-8.045273],[1.143098],[-2.733731],[1.375477],[-6.804849],[-7.568416],[5.354360],[1.539122],[3.087810],[6.197890],[1.702767],[9.004578],[0.126691],[-5.338018],[-5.604024],[8.940700],[-6.705686],[8.247058],[2.805245],[-1.686734],[-8.378230],[-7.592458],[-2.615551],[8.632887],[-7.729483],[3.743030],[0.828671],[-7.242623],[-8.365037],[1.604425],[-3.234245],[1.399611],[1.105565],[1.368561],[-2.090595],[-2.741410],[1.556275],[-3.619964],[-6.916090],[8.901371],[4.733971],[1.588287],[5.814638],[0.882090],[-7.926984],[0.980490],[3.634652],[-1.736706],[9.121615],[6.226768],[4.119564],[-2.054046],[-0.895903],[4.655634],[-5.387287],[-7.110320],[5.216714],[4.468652],[6.611503],[-9.409261],[0.551469],[-4.476625],[5.264474],[0.905176],[2.741433],[-7.632638],[-8.689255],[7.315758],[9.119163],[-9.480867],[5.091408],[3.451800],[-4.349805],[8.304063],[7.721322],[0.334612],[8.363940],[-2.751721],[-5.422689],[-3.489033],[-0.301252],[3.082197],[4.794208]], dtype = "float32")#candidate|6461|(1120, 1)|const|float32
call_6460 = func_2804_call(relay.reshape(const_6461.astype('float32'), [16, 14, 5]), relay.reshape(const_6461.astype('float32'), [16, 14, 5]), )
call_6462 = func_2804_call(relay.reshape(const_6461.astype('float32'), [16, 14, 5]), relay.reshape(const_6461.astype('float32'), [16, 14, 5]), )
func_1964_call = mod.get_global_var('func_1964')
func_1967_call = mutated_mod.get_global_var('func_1967')
const_6465 = relay.const([2,9,8,2,-7,2,1,-8,10,-5,-9,4,-6,1,4,3,3,10,9,5,10,-7,-1,-7,-4,4,5,5,-1,-5,8,2,9,3,5,5,5,6,1,-9,-8,-8,10,-8,-2,7,10,-3,3,-10,-4,-6,1,7,5,-6,-8,10,8,1,1,-1,-9,-2,10,5,-9,7,2,1,-9,-2,9,-6,-10,-8,7,1,-6,10,-7,2,-5,7,2,-5,-2,9,-1,-2,-2,-1,2,6,-9,3,-1,-3,5,-4,-7,-9,5,4,-3,-6,-7,-5,-1,6,-7,-5,6,-5,-7,8,-7,2,-5,8,3,4,-3,8,7,-3,4,5,7,3,-8,-7,-9,8,7,1,-10,-9,-3,-8,-2,-7,10,-6,-1,-10,-1,-5,-9,-4,9,-6,2,3,-2,-8,-1,-1,-4,-7,-8,-5,7,9,2,-2,-1,-1,4,10,4,-2,-10,7,2,10,-2,-8,4,-3,-3,9,-3,-8,-4,-3,-4,-5,-8,2,-6,-1,-9,5,6,-2,-3,2,-9,3,9,-2,-10,9,9,1,4,-2,-1,-6,7,8,7,5,2,-1,-3,4,-10,-5,-4,4,8,-1,-3,8,5,9,9,1,-4,-2,5,-2,3,-4,6,7,4,-5,-6,-6,-10,-4,10,10,-8,-1,-10,-8,2,10,-9,-2,-6,9,-9,-5,-1,7,6,5,10,5,-9,-5,-4,-9,-3,-8,-5,10,-4,-2,-6,8,6,4,-1,8,-1,-1,9,9,-10,-10,6,8,7,-6,-10,-4,10,-4,8,-3,4,-5,-3,-2,3,-7,-4,-8,-8,5,-9,-4,-7,-1,10,-4,-7,7,5,-4,-3,-7,9,-9,8,-5,-5,7,9,6,2,-4,-3,1,-10,6,6,-2,9,-2,-7,5,5,-3,9,-6,3,2,-10,-4,5,-6,5,6,1,-10,-4,-10,4,7,-5,6,2,-4,8,5,-9], dtype = "uint32")#candidate|6465|(363,)|const|uint32
call_6464 = relay.TupleGetItem(func_1964_call(relay.reshape(const_6465.astype('uint32'), [363,])), 0)
call_6466 = relay.TupleGetItem(func_1967_call(relay.reshape(const_6465.astype('uint32'), [363,])), 0)
func_4942_call = mod.get_global_var('func_4942')
func_4944_call = mutated_mod.get_global_var('func_4944')
call_6467 = relay.TupleGetItem(func_4942_call(), 0)
call_6468 = relay.TupleGetItem(func_4944_call(), 0)
func_4123_call = mod.get_global_var('func_4123')
func_4127_call = mutated_mod.get_global_var('func_4127')
var_6478 = relay.var("var_6478", dtype = "bool", shape = ())#candidate|6478|()|var|bool
var_6479 = relay.var("var_6479", dtype = "bool", shape = (448,))#candidate|6479|(448,)|var|bool
call_6477 = func_4123_call(relay.reshape(var_6478.astype('bool'), []), relay.reshape(var_6479.astype('bool'), [14, 4, 8]), )
call_6480 = func_4123_call(relay.reshape(var_6478.astype('bool'), []), relay.reshape(var_6479.astype('bool'), [14, 4, 8]), )
bop_6488 = relay.floor_mod(call_6418.astype('float32'), relay.reshape(call_6464.astype('float32'), relay.shape_of(call_6418))) # shape=(6, 13, 4)
bop_6491 = relay.floor_mod(call_6419.astype('float32'), relay.reshape(call_6466.astype('float32'), relay.shape_of(call_6419))) # shape=(6, 13, 4)
output = relay.Tuple([call_6460,const_6461,const_6465,call_6467,call_6477,var_6478,var_6479,bop_6488,])
output2 = relay.Tuple([call_6462,const_6461,const_6465,call_6468,call_6480,var_6478,var_6479,bop_6491,])
func_6514 = relay.Function([var_6478,var_6479,], output)
mod['func_6514'] = func_6514
mod = relay.transform.InferType()(mod)
var_6515 = relay.var("var_6515", dtype = "bool", shape = ())#candidate|6515|()|var|bool
var_6516 = relay.var("var_6516", dtype = "bool", shape = (448,))#candidate|6516|(448,)|var|bool
output = func_6514(var_6515,var_6516,)
func_6517 = relay.Function([var_6515,var_6516,], output)
mutated_mod['func_6517'] = func_6517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_6519 = relay.TupleGetItem(func_5732_call(), 0)
call_6520 = relay.TupleGetItem(func_5734_call(), 0)
output = call_6519
output2 = call_6520
func_6541 = relay.Function([], output)
mod['func_6541'] = func_6541
mod = relay.transform.InferType()(mod)
output = func_6541()
func_6542 = relay.Function([], output)
mutated_mod['func_6542'] = func_6542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5650_call = mutated_mod.get_global_var('func_5650')
call_6548 = relay.TupleGetItem(func_5648_call(), 2)
call_6549 = relay.TupleGetItem(func_5650_call(), 2)
output = call_6548
output2 = call_6549
func_6558 = relay.Function([], output)
mod['func_6558'] = func_6558
mod = relay.transform.InferType()(mod)
mutated_mod['func_6558'] = func_6558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6558_call = mutated_mod.get_global_var('func_6558')
call_6559 = func_6558_call()
output = call_6559
func_6560 = relay.Function([], output)
mutated_mod['func_6560'] = func_6560
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4256_call = mod.get_global_var('func_4256')
func_4257_call = mutated_mod.get_global_var('func_4257')
call_6572 = func_4256_call()
call_6573 = func_4256_call()
uop_6578 = relay.cosh(call_6572.astype('float32')) # shape=(8, 14, 10)
uop_6580 = relay.cosh(call_6573.astype('float32')) # shape=(8, 14, 10)
output = relay.Tuple([uop_6578,])
output2 = relay.Tuple([uop_6580,])
func_6595 = relay.Function([], output)
mod['func_6595'] = func_6595
mod = relay.transform.InferType()(mod)
output = func_6595()
func_6596 = relay.Function([], output)
mutated_mod['func_6596'] = func_6596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_6615 = relay.TupleGetItem(func_3907_call(), 0)
call_6616 = relay.TupleGetItem(func_3909_call(), 0)
output = relay.Tuple([call_6615,])
output2 = relay.Tuple([call_6616,])
func_6640 = relay.Function([], output)
mod['func_6640'] = func_6640
mod = relay.transform.InferType()(mod)
output = func_6640()
func_6641 = relay.Function([], output)
mutated_mod['func_6641'] = func_6641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_6664 = func_3418_call()
call_6665 = func_3418_call()
output = call_6664
output2 = call_6665
func_6670 = relay.Function([], output)
mod['func_6670'] = func_6670
mod = relay.transform.InferType()(mod)
output = func_6670()
func_6671 = relay.Function([], output)
mutated_mod['func_6671'] = func_6671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6681 = relay.var("var_6681", dtype = "uint64", shape = (2, 8, 12))#candidate|6681|(2, 8, 12)|var|uint64
const_6682 = relay.const([[[-4,-4,7,4,5,-10,1,4,5,8,9,-8],[4,-1,10,6,5,4,-5,-1,-2,9,4,-5],[-7,5,-8,-8,2,-7,-9,8,-2,5,3,-2],[-8,-8,-4,-1,7,9,-10,-8,-6,5,-9,-9],[-5,10,2,-1,-3,-3,2,-2,-10,6,7,2],[-8,-9,10,-8,4,-3,2,-7,2,3,-1,-5],[-5,-1,-5,-6,-2,2,4,-6,-7,-5,2,-3],[-1,10,-3,-3,6,-1,-10,5,-3,-3,6,3]],[[10,-2,9,9,-4,-2,-6,7,10,4,-6,-2],[-6,6,-8,-7,7,3,5,-8,2,7,-6,9],[-2,-7,-4,7,-6,3,-2,-4,-10,-6,10,-5],[5,-2,4,-8,6,5,4,1,-5,-6,5,-5],[-5,-9,7,9,5,3,-3,-6,-6,-9,2,-2],[6,-3,6,-7,1,7,-9,-1,8,-4,7,-9],[10,5,10,9,3,-7,2,-1,-10,-4,-7,-5],[-1,3,8,10,2,2,-3,7,4,7,10,10]]], dtype = "uint64")#candidate|6682|(2, 8, 12)|const|uint64
bop_6683 = relay.less_equal(var_6681.astype('bool'), relay.reshape(const_6682.astype('bool'), relay.shape_of(var_6681))) # shape=(2, 8, 12)
func_5309_call = mod.get_global_var('func_5309')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_6694 = relay.TupleGetItem(func_5309_call(), 1)
call_6695 = relay.TupleGetItem(func_5310_call(), 1)
output = relay.Tuple([bop_6683,call_6694,])
output2 = relay.Tuple([bop_6683,call_6695,])
func_6742 = relay.Function([var_6681,], output)
mod['func_6742'] = func_6742
mod = relay.transform.InferType()(mod)
var_6743 = relay.var("var_6743", dtype = "uint64", shape = (2, 8, 12))#candidate|6743|(2, 8, 12)|var|uint64
output = func_6742(var_6743)
func_6744 = relay.Function([var_6743], output)
mutated_mod['func_6744'] = func_6744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5309_call = mod.get_global_var('func_5309')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_6781 = relay.TupleGetItem(func_5309_call(), 1)
call_6782 = relay.TupleGetItem(func_5310_call(), 1)
uop_6783 = relay.log(call_6781.astype('float32')) # shape=(6, 13, 4)
uop_6785 = relay.log(call_6782.astype('float32')) # shape=(6, 13, 4)
output = relay.Tuple([uop_6783,])
output2 = relay.Tuple([uop_6785,])
func_6806 = relay.Function([], output)
mod['func_6806'] = func_6806
mod = relay.transform.InferType()(mod)
output = func_6806()
func_6807 = relay.Function([], output)
mutated_mod['func_6807'] = func_6807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6558_call = mod.get_global_var('func_6558')
func_6560_call = mutated_mod.get_global_var('func_6560')
call_6819 = func_6558_call()
call_6820 = func_6558_call()
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_6830 = relay.TupleGetItem(func_4180_call(), 1)
call_6831 = relay.TupleGetItem(func_4181_call(), 1)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_6833 = relay.TupleGetItem(func_3950_call(), 0)
call_6834 = relay.TupleGetItem(func_3952_call(), 0)
func_5219_call = mod.get_global_var('func_5219')
func_5221_call = mutated_mod.get_global_var('func_5221')
call_6847 = relay.TupleGetItem(func_5219_call(), 2)
call_6848 = relay.TupleGetItem(func_5221_call(), 2)
output = relay.Tuple([call_6819,call_6830,call_6833,call_6847,])
output2 = relay.Tuple([call_6820,call_6831,call_6834,call_6848,])
func_6868 = relay.Function([], output)
mod['func_6868'] = func_6868
mod = relay.transform.InferType()(mod)
output = func_6868()
func_6869 = relay.Function([], output)
mutated_mod['func_6869'] = func_6869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_6922 = relay.TupleGetItem(func_4460_call(), 7)
call_6923 = relay.TupleGetItem(func_4461_call(), 7)
output = relay.Tuple([call_6922,])
output2 = relay.Tuple([call_6923,])
func_6926 = relay.Function([], output)
mod['func_6926'] = func_6926
mod = relay.transform.InferType()(mod)
mutated_mod['func_6926'] = func_6926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6926_call = mutated_mod.get_global_var('func_6926')
call_6927 = func_6926_call()
output = call_6927
func_6928 = relay.Function([], output)
mutated_mod['func_6928'] = func_6928
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6969 = relay.const([[[3,-2,7,-8],[4,-10,-4,2],[-2,-5,7,1],[6,9,-10,-9],[-4,9,-3,-10],[-4,-7,-9,8],[-4,-10,-5,-3]],[[3,-8,-10,7],[10,-7,2,-9],[6,-5,-4,6],[5,1,7,10],[3,-4,-5,-6],[6,9,1,-4],[-3,-3,3,-9]],[[5,10,-3,3],[-6,-10,7,-7],[9,3,-3,8],[6,-7,1,7],[7,10,-8,5],[-8,-7,10,8],[-10,-1,7,-3]],[[9,2,-9,7],[-8,3,8,2],[-4,10,2,3],[-8,7,4,-8],[3,4,-1,-5],[8,7,-7,-5],[-5,-4,5,-1]],[[4,8,-9,2],[8,-3,8,10],[-7,3,7,4],[3,10,-7,-10],[-8,-8,7,-10],[-5,4,10,-9],[-4,-10,10,-2]],[[2,-10,-1,-10],[1,8,8,-4],[1,-6,3,-6],[10,7,-10,3],[-1,2,7,2],[2,7,10,-2],[-9,-9,-6,1]],[[-1,-3,9,6],[3,3,10,10],[-7,-1,-8,7],[-1,-4,-1,2],[5,-6,3,6],[10,6,7,1],[2,-1,6,10]],[[4,4,-10,1],[2,-2,7,-1],[-9,8,-2,10],[-2,-6,10,-4],[1,2,-6,9],[-10,3,10,6],[-2,5,-3,7]]], dtype = "int64")#candidate|6969|(8, 7, 4)|const|int64
const_6970 = relay.const([[[-3,9,-7,10],[-7,-3,10,2],[-3,10,-7,-8],[-3,-5,9,5],[2,-1,-8,-4],[-3,-7,-7,2],[-7,-10,9,5]],[[1,1,9,-3],[1,-7,7,5],[8,-1,-1,7],[-5,-2,6,-6],[-7,-6,-2,-5],[-5,1,6,1],[10,-1,5,8]],[[-6,4,-10,-9],[-9,3,-6,-4],[3,-2,-5,-4],[-7,5,6,1],[4,4,-8,-2],[7,-8,-6,-5],[-10,-1,-2,-10]],[[-2,10,-6,10],[8,7,8,-3],[-5,-10,-5,-1],[4,10,6,4],[2,-8,4,-2],[3,-8,-7,7],[-4,-4,-4,4]],[[6,3,-3,-2],[8,5,7,4],[-7,2,-7,-7],[-6,2,5,-7],[1,4,4,8],[5,5,1,3],[-6,-1,4,6]],[[8,-9,5,5],[-3,-7,-5,10],[-8,-4,-4,4],[-2,3,-10,5],[6,-2,-9,4],[-6,-8,5,2],[4,-2,-3,-8]],[[-9,10,-1,-9],[8,-5,-8,8],[1,-6,-5,-2],[2,-9,10,1],[-10,1,5,-6],[3,9,-4,7],[4,-4,10,10]],[[-1,1,8,-1],[1,10,3,-1],[1,8,-9,-1],[-8,6,2,-4],[-6,-2,-4,-3],[-4,3,8,4],[3,3,8,-5]]], dtype = "int64")#candidate|6970|(8, 7, 4)|const|int64
bop_6971 = relay.subtract(const_6969.astype('int64'), relay.reshape(const_6970.astype('int64'), relay.shape_of(const_6969))) # shape=(8, 7, 4)
output = relay.Tuple([bop_6971,])
output2 = relay.Tuple([bop_6971,])
func_6979 = relay.Function([], output)
mod['func_6979'] = func_6979
mod = relay.transform.InferType()(mod)
output = func_6979()
func_6980 = relay.Function([], output)
mutated_mod['func_6980'] = func_6980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3212_call = mod.get_global_var('func_3212')
func_3214_call = mutated_mod.get_global_var('func_3214')
call_6992 = relay.TupleGetItem(func_3212_call(), 1)
call_6993 = relay.TupleGetItem(func_3214_call(), 1)
output = relay.Tuple([call_6992,])
output2 = relay.Tuple([call_6993,])
func_7000 = relay.Function([], output)
mod['func_7000'] = func_7000
mod = relay.transform.InferType()(mod)
output = func_7000()
func_7001 = relay.Function([], output)
mutated_mod['func_7001'] = func_7001
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7002 = relay.var("var_7002", dtype = "int64", shape = (7, 7, 1))#candidate|7002|(7, 7, 1)|var|int64
var_7003 = relay.var("var_7003", dtype = "int64", shape = (7, 7, 8))#candidate|7003|(7, 7, 8)|var|int64
bop_7004 = relay.logical_xor(var_7002.astype('int64'), var_7003.astype('int64')) # shape=(7, 7, 8)
func_2804_call = mod.get_global_var('func_2804')
func_2807_call = mutated_mod.get_global_var('func_2807')
const_7011 = relay.const([6.323248,-9.526829,0.491684,2.701710,-3.323741,9.003712,-4.258545,-4.513104,4.347691,4.409347,-0.960678,-1.673651,-3.390583,-9.245712,-0.143782,9.744418,-8.916836,-2.514800,-8.630429,3.570930,4.491567,1.597925,1.321126,1.549896,-3.781730,1.352015,4.210746,-5.234359,0.680268,1.501490,8.748993,-9.686960,7.960119,2.722297,-5.585353,-1.545103,2.445521,8.907683,8.012334,-4.411648,8.087123,-2.251044,7.819396,-0.780720,1.839441,7.934267,-1.589996,6.250115,-3.982482,8.180911,0.650468,-0.421084,-1.163492,6.613309,-3.760441,7.246968,-1.574771,-7.903825,-0.049969,-3.504076,1.612029,4.982348,8.369519,7.862837,7.965537,-4.379706,-8.625371,-6.874172,7.364761,-5.281050,3.031077,3.168360,1.558437,3.953172,6.808747,5.616528,1.384117,-4.305477,8.509035,-1.557235,6.372663,6.531976,-5.684181,-9.123219,-3.559203,9.261426,-0.790593,5.228032,8.445851,4.437347,-4.494981,0.589505,5.568857,7.742612,3.613090,-6.781502,-4.451110,-5.621757,3.531719,-1.389706,2.843827,2.032610,9.916710,4.858500,9.663252,1.050573,7.372330,-5.355365,-5.568452,-5.926126,5.129001,-8.565618,-3.809609,-7.480318,7.182091,9.644416,2.049555,-3.407279,0.661238,7.323621,9.251252,9.663193,1.819482,7.163521,4.860715,2.365019,-0.058209,-4.419149,-8.194798,-5.032281,-7.742274,-4.093764,-9.486654,-4.327426,-2.344787,8.681816,-4.709334,-1.461156,-0.364067,2.722578,7.473932,-4.539479,3.746882,1.245078,-6.424399,1.915004,4.345025,-5.389978,6.012326,-1.009125,-1.952055,2.616751,-7.481637,-9.421017,2.093615,-3.854255,-6.503127,3.241816,1.934941,8.741678,-9.116416,-2.075093,-9.900331,-5.073984,0.638521,5.125229,-2.571094,-8.143401,-2.874844,3.635344,1.582747,8.811439,-1.093552,9.408539,0.394546,8.323546,7.434622,4.194108,-3.844327,1.307496,-5.531733,3.672285,7.941019,7.248519,-6.815829,-5.526724,-1.955073,5.954728,-7.245192,2.644515,7.804296,3.181262,-5.257425,-9.192898,-4.460038,2.886195,-7.839521,5.698463,-3.414379,-3.054084,5.125593,-3.734534,-0.229945,9.341118,-4.769533,-0.029129,2.685107,0.817949,-6.156849,1.742524,2.308261,-0.302007,6.039409,-2.406827,-8.858774,8.986953,2.822440,-3.135595,5.100214,-7.138738,-3.470990,-4.380930,-5.133187,7.184310,3.290047,-8.704364,3.295752,8.172363,-9.336902,6.787944,-0.859975,7.133952,-6.941988,6.155922,4.181380,-0.524662,-2.495943,8.438865,-9.497845,3.986323,8.434487,-4.205250,-3.388886,-2.089122,4.949233,-0.113486,-0.585552,6.348594,8.547370,-6.090083,-4.155368,-8.259315,9.369736,-0.418323,-9.509174,-3.195864,8.756011,1.520307,-7.627548,-1.321362,2.698993,9.185350,-9.273942,-3.303639,2.199115,-6.293260,6.489835,-7.588684,3.675528,-5.799392,-2.823273,5.186729,-6.721819,-6.386581,-9.270822,-5.195170,3.667117,2.316724,8.913874,5.836084,3.492102,-9.888447,-2.738997,8.036813,7.151046,0.225024,-0.692148,4.184909,1.879643,6.268560,3.326894,0.271324,8.634210,-1.165174,8.563966,9.199163,-5.032422,6.449131,-2.153106,-6.270774,8.242040,-8.499901,-7.967980,-2.084636,8.910106,-4.093637,2.566827,6.997971,-3.074301,9.864546,1.930491,-1.850910,8.479749,-2.028705,9.662615,8.742839,-3.270074,-3.135371,-8.105722,1.382421,7.488344,-6.812349,3.846510,9.699486,9.884565,5.324720,-8.646563,-1.735547,-0.790725,8.939703,0.461216,-8.264403,-3.403305,4.904733,9.522130,-4.576779,-0.852047,9.277552,-2.854651,8.643561,-9.896011,-3.495435,9.671641,-2.279354,1.497098,6.555067,-1.162315,1.779203,-6.496292,1.145982,7.701063,-1.918922,-4.922969,9.123071,1.408274,1.378810,-4.594611,-7.681495,-4.006573,9.630435,-9.116435,3.197008,-6.441943,-5.709512,4.692076,-2.156519,2.959750,-1.273485,-9.016717,4.043861,-2.550153,8.434135,-3.187220,-5.014911,-3.226617,8.484780,-7.946387,-5.513660,7.184273,-6.760841,-9.283663,1.689256,4.943173,-7.091012,2.446227,1.480619,-8.838537,-5.867255,-4.354450,2.487141,-8.691267,-0.556647,9.739256,4.045136,6.967053,7.516426,-6.473810,7.932170,-6.889715,-6.072757,6.567774,-4.697525,-3.939789,8.964236,3.143749,-5.360244,4.737944,4.219945,5.714355,7.847630,-1.463559,-3.593366,5.009851,-5.548810,5.119753,6.505952,0.296245,-6.921124,0.349666,-0.404807,9.205053,-1.476951,7.019790,5.711002,1.435355,9.629599,-8.306238,-3.615745,-1.282464,9.032678,4.581425,-7.397010,-6.651816,7.281687,-7.508614,2.741358,-1.143390,-3.096359,5.229825,-4.452599,-1.433197,-3.032208,2.155493,-6.677285,0.817057,-9.893791,1.086311,5.981317,1.029516,2.763199,6.728816,7.752394,-9.228434,0.709285,-5.212576,-1.155216,-7.726167,6.105312,-1.634478,4.606918,2.662316,-4.371985,-5.711763,6.087961,-3.018856,-0.948931,0.612767,2.606465,5.778113,1.509730,-0.760386,4.168181,-5.125049,5.452498,-6.471515,-8.866678,-2.248512,-9.916129,5.496655,-8.584788,-1.289264,2.650929,1.061851,-6.633208,3.363505,-0.626826,3.211466,-4.131251,-1.375343,-2.041745,-7.005471,-8.903378,-9.458944,-5.152951,-2.499676,9.540452,2.144493,-0.473710,-9.596219,8.500196,-7.111624,1.305931,9.394864,8.969527,8.137917,0.889457,2.130452,-9.306519,-1.280171,4.382035,-7.325687,-6.746723,7.810813,-7.955140,1.929196,3.071997,7.472531,8.805354,0.915829,-5.616962,2.937160,-2.656684,3.873156,-2.952122,2.312046,5.841155,-3.054175,3.696551,-1.814354,8.369213,-4.222784,-5.284723,-6.964754,-3.789935,-6.185240,-2.594578,-8.805258,-5.978730,-6.082506,-9.839034,-9.830443,8.575025,7.379926,-6.197574,-0.411828,9.810625,2.119723,-4.492526,1.678583,6.246843,8.351076,8.489045,-7.903282,5.098958,-5.192942,1.042719,1.682513,-4.569349,7.903819,2.119639,-4.974008,-3.917323,-9.426556,4.909435,-2.267952,6.796742,1.250143,6.292711,2.761607,-5.837118,-4.328190,-7.146958,-6.283756,-8.674269,-8.858106,9.909253,-9.167094,-2.668769,-1.688998,0.243620,-0.784437,-5.829630,0.635197,0.009837,-4.404619,2.615071,0.634010,2.278941,-1.782950,-2.231552,4.123257,7.908978,7.100678,-5.792201,-7.655732,-1.963709,-6.091745,-9.652540,7.568954,-3.704014,0.802449,-8.288314,-2.073243,-6.538849,-1.795931,5.369985,-0.729922,2.365158,-3.458299,5.507028,7.841065,1.858341,-7.219687,-9.755478,7.120974,6.127302,-8.327257,-4.232655,0.183700,7.585057,8.788615,3.940083,5.880822,9.409480,-0.975887,-2.224708,4.289932,-1.654218,2.722811,7.546525,0.041691,6.126241,-3.642005,-0.055430,-8.852283,5.593081,-5.663788,5.792251,-5.126849,8.859785,5.801076,-8.387197,9.028295,-3.782829,5.556297,-2.034781,4.447666,-7.236122,8.334725,4.257812,-6.563024,9.539065,-3.824659,3.128267,0.117356,7.113744,-4.874019,2.756622,-8.770793,8.000039,2.248640,9.987713,1.183524,8.290175,-7.140910,1.410608,7.236584,-4.570766,8.007676,-6.087912,-5.884579,-9.146624,-4.742096,4.173988,3.890159,-2.744091,-4.689633,2.783158,-5.692189,-5.899476,-4.588282,8.548356,-3.394035,2.487124,3.092192,-0.670028,9.806191,3.101831,9.908663,5.262664,4.893575,9.090442,1.471953,8.654611,5.665032,-6.589571,9.595353,-1.615869,0.326900,-5.692311,2.308569,9.894527,8.358557,-0.514667,3.321329,5.678456,-1.370652,-9.318089,-2.883063,6.416328,9.659398,4.333248,3.758910,-7.640909,6.298404,-0.933522,1.668313,3.671856,-8.251890,7.413323,9.861607,-4.682310,-0.725933,6.297467,-9.591451,-7.442981,3.820412,8.840011,3.869913,9.463047,-1.242073,-8.828092,4.471602,-4.837587,3.926973,5.143723,-3.187807,-1.026589,-4.064496,3.358343,-5.256754,-7.737895,8.180797,3.762704,3.438998,6.114438,-8.876913,-2.384857,-0.543782,4.246389,-6.759755,-5.734994,-1.882927,1.817936,6.226340,8.705178,8.313062,3.135374,8.873580,1.044533,2.792322,-1.137695,-8.804694,-7.117687,8.302038,8.006589,-6.451119,6.837855,-0.285984,-9.546935,0.857475,-2.580865,5.128902,-4.128465,-6.868023,-1.730952,-6.750856,2.463811,8.019961,9.946953,8.137255,-1.816857,3.972081,-7.009185,7.511109,4.236165,-9.509735,4.255061,0.987934,0.111956,0.749162,8.685982,-2.163839,1.206715,-1.442369,4.795839,8.546101,-5.694233,8.823124,-0.449196,4.863568,9.502190,9.977774,6.006976,-1.423607,-7.415815,-3.134723,-9.102012,-4.418498,-2.698701,-5.954504,-7.245005,-1.714247,-0.585702,9.057444,-8.921431,-8.452135,6.718592,-9.943584,-9.573109,7.100267,-4.431248,5.832055,-7.146743,-8.648568,-6.686165,-7.130434,-7.789463,1.891568,-1.846786,-3.861796,7.841705,0.018000,-5.802027,-2.856861,-4.954065,-0.777514,5.655723,6.999643,5.727914,4.171486,4.053903,5.212697,-4.145359,-5.127240,6.451126,3.984182,-6.519697,9.526767,-1.301327,2.693450,8.918155,4.651017,8.479117,3.723264,6.935223,0.722268,-2.971943,-8.243452,7.528674,-8.566371,6.786561,-5.167882,-7.187176,5.583842,4.571421,7.975636,-0.838440,0.930190,-6.910968,-9.876916,5.911455,-1.212858,-0.864522,-2.762013,3.231742,9.260749,-9.531386,-6.358367,7.426669,4.533498,9.254599,-0.439998,-3.375936,9.545037,-8.548821,-2.885089,8.987058,7.774276,8.301769,-4.386632,-0.516160,-8.333765,3.191511,3.312035,-2.243973,6.890586,-7.840898,3.874146,3.411266,8.776331,-8.534853,-0.508132,-8.224836,-7.327538,2.249244,-1.630783,-7.782783,2.565884,-9.840665,-6.856637,6.607856,-4.371240,8.011136,-5.869009,-9.695775,-6.423149,0.161875,4.061209,6.956160,-5.643671,-1.050552,-3.229721,9.613179,-4.805553,9.426938,-7.360992,-0.610084,-7.504915,-2.832764,-1.541697,-2.106664,3.907175,9.910582,8.085243,-2.980967,-2.207893,-8.023843,9.346577,-9.568964,5.896684,9.236008,-9.431976,-6.171250,0.851232,-3.102486,-3.393301,0.611892,-4.451141,-8.355063,1.673591,1.175182,0.920553,-7.357188,4.795399,-9.954755,-8.719227,-6.164588,5.294319,8.893700,2.211413,-3.464821,-4.246008,-8.640995,2.747152,-1.168259,0.207323,-0.591715,-0.169603,-4.230785,6.045002,-8.369407,-8.688923,-5.794169,-2.676471,-0.599203,7.564212,5.053736,-9.419133,9.953420,-3.673643,-1.178953,6.573954,-7.222368,-5.927140,-0.102610,4.282040,6.925794,0.246579,5.898731,-5.754117,-2.417933,-2.799831,0.022326,5.562320,-4.452222,5.013618,2.279039,5.162256,-6.789484,-2.139655,3.785942,3.203382,2.295702,9.384629,-2.675097,8.642335,9.623903,-6.165448,-4.878758,9.551736,4.278049,-3.299331,-9.807482,-5.509129,2.430697,2.538824,-8.121062,5.147732,3.583628,-2.693706,-8.062209,-3.350780,-6.506927,7.922485,-5.676202,6.388735,8.514331,1.387709,-7.882817,-0.722769,-5.608192,-1.177642,-2.530000,0.705351,-8.247763,-7.641745,7.361656,8.496599,2.475392,-9.724929,8.878290,-2.057702,3.944670,-5.094951,3.211495,2.721828,-9.133133,2.017420,-6.012355,1.515542,-8.178121,6.552521,-8.076261,9.105324,6.707865,-5.023307,-5.344740,5.269991,-7.305686,1.308403,-8.174495,8.596293,-3.239396,-3.491381,2.753413,-0.157573,7.889325,3.776281,-1.176367,6.875605,9.215149,-7.295326,-8.546244,3.805242,-3.267070,7.737488,-9.008685,0.087190,4.435553,0.917253,3.769632,-6.571762,2.773923,1.765695,9.509936,-5.398670,-8.056733,-6.265781,-1.689951,3.519399,-3.753157,-2.554740,1.417089,5.499308,9.937746,-9.588665,-9.111006,7.659223,-5.227673,3.424158,5.312762,-7.388609,1.883458,3.582335,1.283481,-3.678561,3.724217,-3.989025,-8.664104,0.548328,-7.486177,2.656390,-5.830897,-6.223636,0.336605,-5.353287,4.074257,-0.089498,1.201501], dtype = "float32")#candidate|7011|(1120,)|const|float32
call_7010 = func_2804_call(relay.reshape(const_7011.astype('float32'), [16, 14, 5]), relay.reshape(const_7011.astype('float32'), [16, 14, 5]), )
call_7012 = func_2804_call(relay.reshape(const_7011.astype('float32'), [16, 14, 5]), relay.reshape(const_7011.astype('float32'), [16, 14, 5]), )
bop_7020 = relay.left_shift(var_7003.astype('int32'), var_7002.astype('int32')) # shape=(7, 7, 8)
output = relay.Tuple([bop_7004,call_7010,const_7011,bop_7020,])
output2 = relay.Tuple([bop_7004,call_7012,const_7011,bop_7020,])
func_7024 = relay.Function([var_7002,var_7003,], output)
mod['func_7024'] = func_7024
mod = relay.transform.InferType()(mod)
var_7025 = relay.var("var_7025", dtype = "int64", shape = (7, 7, 1))#candidate|7025|(7, 7, 1)|var|int64
var_7026 = relay.var("var_7026", dtype = "int64", shape = (7, 7, 8))#candidate|7026|(7, 7, 8)|var|int64
output = func_7024(var_7025,var_7026,)
func_7027 = relay.Function([var_7025,var_7026,], output)
mutated_mod['func_7027'] = func_7027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2403_call = mod.get_global_var('func_2403')
func_2405_call = mutated_mod.get_global_var('func_2405')
call_7044 = relay.TupleGetItem(func_2403_call(), 0)
call_7045 = relay.TupleGetItem(func_2405_call(), 0)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_7054 = relay.TupleGetItem(func_2587_call(), 3)
call_7055 = relay.TupleGetItem(func_2588_call(), 3)
func_4822_call = mod.get_global_var('func_4822')
func_4824_call = mutated_mod.get_global_var('func_4824')
call_7071 = relay.TupleGetItem(func_4822_call(), 0)
call_7072 = relay.TupleGetItem(func_4824_call(), 0)
func_3870_call = mod.get_global_var('func_3870')
func_3871_call = mutated_mod.get_global_var('func_3871')
call_7073 = relay.TupleGetItem(func_3870_call(), 0)
call_7074 = relay.TupleGetItem(func_3871_call(), 0)
output = relay.Tuple([call_7044,call_7054,call_7071,call_7073,])
output2 = relay.Tuple([call_7045,call_7055,call_7072,call_7074,])
func_7075 = relay.Function([], output)
mod['func_7075'] = func_7075
mod = relay.transform.InferType()(mod)
output = func_7075()
func_7076 = relay.Function([], output)
mutated_mod['func_7076'] = func_7076
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_7087 = relay.TupleGetItem(func_5732_call(), 0)
call_7088 = relay.TupleGetItem(func_5734_call(), 0)
func_4064_call = mod.get_global_var('func_4064')
func_4065_call = mutated_mod.get_global_var('func_4065')
call_7091 = relay.TupleGetItem(func_4064_call(), 0)
call_7092 = relay.TupleGetItem(func_4065_call(), 0)
output = relay.Tuple([call_7087,call_7091,])
output2 = relay.Tuple([call_7088,call_7092,])
func_7098 = relay.Function([], output)
mod['func_7098'] = func_7098
mod = relay.transform.InferType()(mod)
mutated_mod['func_7098'] = func_7098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7098_call = mutated_mod.get_global_var('func_7098')
call_7099 = func_7098_call()
output = call_7099
func_7100 = relay.Function([], output)
mutated_mod['func_7100'] = func_7100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3212_call = mod.get_global_var('func_3212')
func_3214_call = mutated_mod.get_global_var('func_3214')
call_7109 = relay.TupleGetItem(func_3212_call(), 1)
call_7110 = relay.TupleGetItem(func_3214_call(), 1)
var_7113 = relay.var("var_7113", dtype = "float32", shape = (8, 14, 10))#candidate|7113|(8, 14, 10)|var|float32
bop_7114 = relay.logical_xor(call_7109.astype('int8'), relay.reshape(var_7113.astype('int8'), relay.shape_of(call_7109))) # shape=(8, 14, 10)
bop_7117 = relay.logical_xor(call_7110.astype('int8'), relay.reshape(var_7113.astype('int8'), relay.shape_of(call_7110))) # shape=(8, 14, 10)
func_6541_call = mod.get_global_var('func_6541')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_7129 = func_6541_call()
call_7130 = func_6541_call()
uop_7146 = relay.sigmoid(call_7109.astype('float32')) # shape=(8, 14, 10)
uop_7148 = relay.sigmoid(call_7110.astype('float32')) # shape=(8, 14, 10)
output = relay.Tuple([bop_7114,call_7129,uop_7146,])
output2 = relay.Tuple([bop_7117,call_7130,uop_7148,])
func_7151 = relay.Function([var_7113,], output)
mod['func_7151'] = func_7151
mod = relay.transform.InferType()(mod)
mutated_mod['func_7151'] = func_7151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7152 = relay.var("var_7152", dtype = "float32", shape = (8, 14, 10))#candidate|7152|(8, 14, 10)|var|float32
func_7151_call = mutated_mod.get_global_var('func_7151')
call_7153 = func_7151_call(var_7152)
output = call_7153
func_7154 = relay.Function([var_7152], output)
mutated_mod['func_7154'] = func_7154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6541_call = mod.get_global_var('func_6541')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_7187 = func_6541_call()
call_7188 = func_6541_call()
output = call_7187
output2 = call_7188
func_7189 = relay.Function([], output)
mod['func_7189'] = func_7189
mod = relay.transform.InferType()(mod)
output = func_7189()
func_7190 = relay.Function([], output)
mutated_mod['func_7190'] = func_7190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7202 = relay.const([[[-8.937358,-0.853081],[0.067312,-7.175007],[6.282484,-0.915933],[-0.979953,-3.211668],[-8.455662,-0.293926],[-4.865901,-1.847899],[6.365133,0.071369],[0.080990,-2.824888],[4.444171,-5.676650],[5.841432,0.837625]],[[-1.951851,9.437338],[-2.254320,8.632383],[9.911416,-1.226037],[-5.117852,-2.807650],[-0.763237,0.602208],[-6.409545,9.353279],[6.055916,-4.018610],[-5.323774,4.103269],[9.790809,8.483970],[-7.193105,-9.821228]],[[-1.149879,4.828465],[-4.374612,9.801102],[9.209357,-3.526351],[-8.803760,-6.300556],[-6.069093,-6.622236],[-1.002805,0.858609],[4.818692,6.059635],[7.364932,7.427651],[2.334013,-4.328978],[-5.163905,-0.595793]],[[6.477823,0.944789],[-5.988277,0.309915],[-5.155691,4.957186],[1.701106,-1.840509],[6.815354,-2.673717],[-1.014762,8.004793],[-4.414037,8.570183],[6.297548,-8.756776],[-5.720325,-8.295082],[0.408858,9.675307]],[[8.189870,-9.481180],[0.946014,1.416687],[4.927991,5.387684],[5.575581,2.981102],[8.873019,-8.151387],[-6.863609,2.360340],[-6.190538,3.112412],[0.510590,1.425959],[7.509587,0.669788],[5.813492,8.156656]],[[-2.692447,-6.608742],[8.105458,6.364613],[-7.287988,6.678214],[-0.039294,3.278657],[-5.378251,2.503757],[-1.492753,9.099292],[-0.291973,-2.244052],[1.588332,-5.393709],[1.013968,-6.925619],[-4.987301,4.254306]],[[9.579406,9.750311],[6.313895,4.726944],[4.134030,4.880245],[0.039705,7.874167],[9.317502,1.664139],[-7.475881,-1.691295],[-8.591320,-9.920482],[-6.011265,9.216408],[7.065113,6.285868],[-4.409572,-8.404251]],[[0.257897,2.523537],[-1.062819,9.741417],[-9.183375,3.994824],[-0.221193,-7.085735],[-7.513335,-7.634999],[-6.345818,-0.072825],[-3.245361,-1.318415],[-5.002806,1.707698],[-6.584431,6.061290],[5.077101,-9.457776]]], dtype = "float64")#candidate|7202|(8, 10, 2)|const|float64
uop_7203 = relay.cosh(const_7202.astype('float64')) # shape=(8, 10, 2)
output = relay.Tuple([uop_7203,])
output2 = relay.Tuple([uop_7203,])
func_7212 = relay.Function([], output)
mod['func_7212'] = func_7212
mod = relay.transform.InferType()(mod)
mutated_mod['func_7212'] = func_7212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7212_call = mutated_mod.get_global_var('func_7212')
call_7213 = func_7212_call()
output = call_7213
func_7214 = relay.Function([], output)
mutated_mod['func_7214'] = func_7214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4822_call = mod.get_global_var('func_4822')
func_4824_call = mutated_mod.get_global_var('func_4824')
call_7312 = relay.TupleGetItem(func_4822_call(), 0)
call_7313 = relay.TupleGetItem(func_4824_call(), 0)
func_4927_call = mod.get_global_var('func_4927')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_7316 = relay.var("var_7316", dtype = "uint8", shape = ())#candidate|7316|()|var|uint8
var_7317 = relay.var("var_7317", dtype = "uint8", shape = (432,))#candidate|7317|(432,)|var|uint8
var_7318 = relay.var("var_7318", dtype = "float64", shape = (1092,))#candidate|7318|(1092,)|var|float64
call_7315 = relay.TupleGetItem(func_4927_call(relay.reshape(var_7316.astype('uint8'), []), relay.reshape(var_7317.astype('uint8'), [12, 3, 12]), relay.reshape(var_7318.astype('float64'), [1092,]), ), 2)
call_7319 = relay.TupleGetItem(func_4932_call(relay.reshape(var_7316.astype('uint8'), []), relay.reshape(var_7317.astype('uint8'), [12, 3, 12]), relay.reshape(var_7318.astype('float64'), [1092,]), ), 2)
output = relay.Tuple([call_7312,call_7315,var_7316,var_7317,var_7318,])
output2 = relay.Tuple([call_7313,call_7319,var_7316,var_7317,var_7318,])
func_7323 = relay.Function([var_7316,var_7317,var_7318,], output)
mod['func_7323'] = func_7323
mod = relay.transform.InferType()(mod)
mutated_mod['func_7323'] = func_7323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7323_call = mutated_mod.get_global_var('func_7323')
var_7325 = relay.var("var_7325", dtype = "uint8", shape = ())#candidate|7325|()|var|uint8
var_7326 = relay.var("var_7326", dtype = "uint8", shape = (432,))#candidate|7326|(432,)|var|uint8
var_7327 = relay.var("var_7327", dtype = "float64", shape = (1092,))#candidate|7327|(1092,)|var|float64
call_7324 = func_7323_call(var_7325,var_7326,var_7327,)
output = call_7324
func_7328 = relay.Function([var_7325,var_7326,var_7327,], output)
mutated_mod['func_7328'] = func_7328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6595_call = mod.get_global_var('func_6595')
func_6596_call = mutated_mod.get_global_var('func_6596')
call_7352 = relay.TupleGetItem(func_6595_call(), 0)
call_7353 = relay.TupleGetItem(func_6596_call(), 0)
func_4927_call = mod.get_global_var('func_4927')
func_4932_call = mutated_mod.get_global_var('func_4932')
var_7362 = relay.var("var_7362", dtype = "uint8", shape = ())#candidate|7362|()|var|uint8
const_7363 = relay.const([2,10,9,-2,-10,-7,-2,8,8,2,-8,-4,-5,-5,9,-10,1,8,6,8,-6,-8,8,2,-7,-9,-1,2,-8,-4,10,-10,8,3,-8,1,-6,4,-6,1,1,8,3,-9,-8,9,-10,9,7,-1,2,10,-10,-3,1,10,6,-5,10,1,8,6,-9,6,-8,2,7,-10,-6,-3,-9,-8,-5,-3,8,4,5,4,6,1,-6,-4,5,-2,-6,-8,10,-7,1,-9,-5,-5,-3,-6,8,3,-10,-9,-10,8,5,-9,5,1,8,-5,5,5,8,8,-9,-1,7,-6,10,3,1,2,9,-2,-3,2,-6,5,6,-1,2,4,4,8,-3,9,4,1,-3,2,9,-4,-9,-10,-10,-10,5,-6,3,2,7,-3,1,6,-7,9,-2,-1,-2,8,4,-6,3,7,-6,-3,10,-3,9,6,10,10,-10,3,-3,-4,10,-5,10,8,-3,-8,-8,-6,2,3,-7,4,-7,7,-9,-5,1,-1,-4,-6,3,-9,-6,-9,5,10,8,-9,-2,-5,7,9,9,-8,2,-9,-9,7,-1,6,10,-10,-10,3,5,-3,7,-2,-4,9,-6,1,7,3,-4,-6,2,3,4,4,-6,-4,10,9,-6,-10,-9,8,-8,-5,-9,-9,8,-5,-9,-6,7,-8,-5,1,-9,4,3,-7,-4,-3,5,5,3,-10,2,-9,-5,6,-8,-1,-9,7,8,2,6,6,9,-9,-3,7,4,-4,7,-8,8,-1,8,-10,-4,10,-10,-5,8,-3,10,6,-8,-4,-2,-9,4,9,10,10,-4,7,-7,-2,4,-5,5,-10,-4,9,7,-6,8,4,-5,-5,3,4,2,-4,-3,-3,-2,3,-7,2,8,4,-3,5,1,8,2,5,-10,-2,-9,1,-10,-9,-7,-9,-7,3,1,8,10,9,10,7,2,10,8,5,8,-3,3,9,4,1,-2,9,-7,-5,2,-4,5,8,-9,-9,6,-9,-3,10,2,5,10,-7,2,-1,-8,-1,-3,6,9,-9,9,-6,6,-2,-5,4,2,-2,5,-1,2,-6,8,-7,7,-3,-3,1,-5,10,3,-5,5,-1,3,-3,-3,-10,-1,1,-4,-6,-3,10,1,8,-4,-9,2,-9,-2,-10,1,8], dtype = "uint8")#candidate|7363|(432,)|const|uint8
var_7364 = relay.var("var_7364", dtype = "float64", shape = (1092,))#candidate|7364|(1092,)|var|float64
call_7361 = relay.TupleGetItem(func_4927_call(relay.reshape(var_7362.astype('uint8'), []), relay.reshape(const_7363.astype('uint8'), [12, 3, 12]), relay.reshape(var_7364.astype('float64'), [1092,]), ), 2)
call_7365 = relay.TupleGetItem(func_4932_call(relay.reshape(var_7362.astype('uint8'), []), relay.reshape(const_7363.astype('uint8'), [12, 3, 12]), relay.reshape(var_7364.astype('float64'), [1092,]), ), 2)
output = relay.Tuple([call_7352,call_7361,var_7362,const_7363,var_7364,])
output2 = relay.Tuple([call_7353,call_7365,var_7362,const_7363,var_7364,])
func_7387 = relay.Function([var_7362,var_7364,], output)
mod['func_7387'] = func_7387
mod = relay.transform.InferType()(mod)
mutated_mod['func_7387'] = func_7387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7387_call = mutated_mod.get_global_var('func_7387')
var_7389 = relay.var("var_7389", dtype = "uint8", shape = ())#candidate|7389|()|var|uint8
var_7390 = relay.var("var_7390", dtype = "float64", shape = (1092,))#candidate|7390|(1092,)|var|float64
call_7388 = func_7387_call(var_7389,var_7390,)
output = call_7388
func_7391 = relay.Function([var_7389,var_7390,], output)
mutated_mod['func_7391'] = func_7391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6541_call = mod.get_global_var('func_6541')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_7401 = func_6541_call()
call_7402 = func_6541_call()
uop_7419 = relay.log2(call_7401.astype('float32')) # shape=(112,)
uop_7421 = relay.log2(call_7402.astype('float32')) # shape=(112,)
func_3335_call = mod.get_global_var('func_3335')
func_3338_call = mutated_mod.get_global_var('func_3338')
var_7433 = relay.var("var_7433", dtype = "float64", shape = (312,))#candidate|7433|(312,)|var|float64
call_7432 = relay.TupleGetItem(func_3335_call(relay.reshape(var_7433.astype('float64'), [3, 104]), relay.reshape(var_7433.astype('float64'), [3, 104]), ), 4)
call_7434 = relay.TupleGetItem(func_3338_call(relay.reshape(var_7433.astype('float64'), [3, 104]), relay.reshape(var_7433.astype('float64'), [3, 104]), ), 4)
func_3870_call = mod.get_global_var('func_3870')
func_3871_call = mutated_mod.get_global_var('func_3871')
call_7439 = relay.TupleGetItem(func_3870_call(), 0)
call_7440 = relay.TupleGetItem(func_3871_call(), 0)
func_3978_call = mod.get_global_var('func_3978')
func_3981_call = mutated_mod.get_global_var('func_3981')
var_7443 = relay.var("var_7443", dtype = "uint32", shape = (363, 1))#candidate|7443|(363, 1)|var|uint32
call_7442 = relay.TupleGetItem(func_3978_call(relay.reshape(var_7443.astype('uint32'), [363,])), 2)
call_7444 = relay.TupleGetItem(func_3981_call(relay.reshape(var_7443.astype('uint32'), [363,])), 2)
func_6514_call = mod.get_global_var('func_6514')
func_6517_call = mutated_mod.get_global_var('func_6517')
var_7453 = relay.var("var_7453", dtype = "bool", shape = ())#candidate|7453|()|var|bool
var_7454 = relay.var("var_7454", dtype = "bool", shape = (448,))#candidate|7454|(448,)|var|bool
call_7452 = relay.TupleGetItem(func_6514_call(relay.reshape(var_7453.astype('bool'), []), relay.reshape(var_7454.astype('bool'), [448,]), ), 5)
call_7455 = relay.TupleGetItem(func_6517_call(relay.reshape(var_7453.astype('bool'), []), relay.reshape(var_7454.astype('bool'), [448,]), ), 5)
bop_7464 = relay.subtract(var_7443.astype('int32'), uop_7419.astype('int32')) # shape=(363, 112)
bop_7467 = relay.subtract(var_7443.astype('int32'), uop_7421.astype('int32')) # shape=(363, 112)
output = relay.Tuple([call_7432,var_7433,call_7439,call_7442,call_7452,var_7453,var_7454,bop_7464,])
output2 = relay.Tuple([call_7434,var_7433,call_7440,call_7444,call_7455,var_7453,var_7454,bop_7467,])
func_7468 = relay.Function([var_7433,var_7443,var_7453,var_7454,], output)
mod['func_7468'] = func_7468
mod = relay.transform.InferType()(mod)
mutated_mod['func_7468'] = func_7468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7468_call = mutated_mod.get_global_var('func_7468')
var_7470 = relay.var("var_7470", dtype = "float64", shape = (312,))#candidate|7470|(312,)|var|float64
var_7471 = relay.var("var_7471", dtype = "uint32", shape = (363, 1))#candidate|7471|(363, 1)|var|uint32
var_7472 = relay.var("var_7472", dtype = "bool", shape = ())#candidate|7472|()|var|bool
var_7473 = relay.var("var_7473", dtype = "bool", shape = (448,))#candidate|7473|(448,)|var|bool
call_7469 = func_7468_call(var_7470,var_7471,var_7472,var_7473,)
output = call_7469
func_7474 = relay.Function([var_7470,var_7471,var_7472,var_7473,], output)
mutated_mod['func_7474'] = func_7474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5124_call = mod.get_global_var('func_5124')
func_5126_call = mutated_mod.get_global_var('func_5126')
call_7503 = relay.TupleGetItem(func_5124_call(), 0)
call_7504 = relay.TupleGetItem(func_5126_call(), 0)
func_3907_call = mod.get_global_var('func_3907')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_7506 = relay.TupleGetItem(func_3907_call(), 0)
call_7507 = relay.TupleGetItem(func_3909_call(), 0)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_7508 = func_2361_call()
call_7509 = func_2361_call()
output = relay.Tuple([call_7503,call_7506,call_7508,])
output2 = relay.Tuple([call_7504,call_7507,call_7509,])
func_7515 = relay.Function([], output)
mod['func_7515'] = func_7515
mod = relay.transform.InferType()(mod)
output = func_7515()
func_7516 = relay.Function([], output)
mutated_mod['func_7516'] = func_7516
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7561 = relay.var("var_7561", dtype = "uint16", shape = (9, 15, 7))#candidate|7561|(9, 15, 7)|var|uint16
var_7562 = relay.var("var_7562", dtype = "uint16", shape = (9, 15, 7))#candidate|7562|(9, 15, 7)|var|uint16
bop_7563 = relay.left_shift(var_7561.astype('uint16'), relay.reshape(var_7562.astype('uint16'), relay.shape_of(var_7561))) # shape=(9, 15, 7)
func_6514_call = mod.get_global_var('func_6514')
func_6517_call = mutated_mod.get_global_var('func_6517')
const_7568 = relay.const(True, dtype = "bool")#candidate|7568|()|const|bool
var_7569 = relay.var("var_7569", dtype = "bool", shape = (448,))#candidate|7569|(448,)|var|bool
call_7567 = relay.TupleGetItem(func_6514_call(relay.reshape(const_7568.astype('bool'), []), relay.reshape(var_7569.astype('bool'), [448,]), ), 3)
call_7570 = relay.TupleGetItem(func_6517_call(relay.reshape(const_7568.astype('bool'), []), relay.reshape(var_7569.astype('bool'), [448,]), ), 3)
output = relay.Tuple([bop_7563,call_7567,const_7568,var_7569,])
output2 = relay.Tuple([bop_7563,call_7570,const_7568,var_7569,])
func_7575 = relay.Function([var_7561,var_7562,var_7569,], output)
mod['func_7575'] = func_7575
mod = relay.transform.InferType()(mod)
mutated_mod['func_7575'] = func_7575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7575_call = mutated_mod.get_global_var('func_7575')
var_7577 = relay.var("var_7577", dtype = "uint16", shape = (9, 15, 7))#candidate|7577|(9, 15, 7)|var|uint16
var_7578 = relay.var("var_7578", dtype = "uint16", shape = (9, 15, 7))#candidate|7578|(9, 15, 7)|var|uint16
var_7579 = relay.var("var_7579", dtype = "bool", shape = (448,))#candidate|7579|(448,)|var|bool
call_7576 = func_7575_call(var_7577,var_7578,var_7579,)
output = call_7576
func_7580 = relay.Function([var_7577,var_7578,var_7579,], output)
mutated_mod['func_7580'] = func_7580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_7638 = relay.TupleGetItem(func_3907_call(), 0)
call_7639 = relay.TupleGetItem(func_3909_call(), 0)
output = call_7638
output2 = call_7639
func_7640 = relay.Function([], output)
mod['func_7640'] = func_7640
mod = relay.transform.InferType()(mod)
mutated_mod['func_7640'] = func_7640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7640_call = mutated_mod.get_global_var('func_7640')
call_7641 = func_7640_call()
output = call_7641
func_7642 = relay.Function([], output)
mutated_mod['func_7642'] = func_7642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3492_call = mod.get_global_var('func_3492')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_7716 = relay.TupleGetItem(func_3492_call(), 2)
call_7717 = relay.TupleGetItem(func_3494_call(), 2)
output = relay.Tuple([call_7716,])
output2 = relay.Tuple([call_7717,])
func_7726 = relay.Function([], output)
mod['func_7726'] = func_7726
mod = relay.transform.InferType()(mod)
mutated_mod['func_7726'] = func_7726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7726_call = mutated_mod.get_global_var('func_7726')
call_7727 = func_7726_call()
output = call_7727
func_7728 = relay.Function([], output)
mutated_mod['func_7728'] = func_7728
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7835 = relay.var("var_7835", dtype = "float64", shape = (11, 3, 15))#candidate|7835|(11, 3, 15)|var|float64
uop_7836 = relay.sqrt(var_7835.astype('float64')) # shape=(11, 3, 15)
output = uop_7836
output2 = uop_7836
func_7843 = relay.Function([var_7835,], output)
mod['func_7843'] = func_7843
mod = relay.transform.InferType()(mod)
mutated_mod['func_7843'] = func_7843
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7844 = relay.var("var_7844", dtype = "float64", shape = (11, 3, 15))#candidate|7844|(11, 3, 15)|var|float64
func_7843_call = mutated_mod.get_global_var('func_7843')
call_7845 = func_7843_call(var_7844)
output = call_7845
func_7846 = relay.Function([var_7844], output)
mutated_mod['func_7846'] = func_7846
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7923 = relay.var("var_7923", dtype = "float32", shape = (14, 16, 3))#candidate|7923|(14, 16, 3)|var|float32
uop_7924 = relay.sigmoid(var_7923.astype('float32')) # shape=(14, 16, 3)
output = uop_7924
output2 = uop_7924
func_7926 = relay.Function([var_7923,], output)
mod['func_7926'] = func_7926
mod = relay.transform.InferType()(mod)
var_7927 = relay.var("var_7927", dtype = "float32", shape = (14, 16, 3))#candidate|7927|(14, 16, 3)|var|float32
output = func_7926(var_7927)
func_7928 = relay.Function([var_7927], output)
mutated_mod['func_7928'] = func_7928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mod.get_global_var('func_3359')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_7940 = func_3359_call()
call_7941 = func_3359_call()
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_7960 = relay.TupleGetItem(func_4180_call(), 0)
call_7961 = relay.TupleGetItem(func_4181_call(), 0)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_7970 = relay.TupleGetItem(func_2587_call(), 2)
call_7971 = relay.TupleGetItem(func_2588_call(), 2)
func_7189_call = mod.get_global_var('func_7189')
func_7190_call = mutated_mod.get_global_var('func_7190')
call_7983 = func_7189_call()
call_7984 = func_7189_call()
output = relay.Tuple([call_7940,call_7960,call_7970,call_7983,])
output2 = relay.Tuple([call_7941,call_7961,call_7971,call_7984,])
func_7987 = relay.Function([], output)
mod['func_7987'] = func_7987
mod = relay.transform.InferType()(mod)
output = func_7987()
func_7988 = relay.Function([], output)
mutated_mod['func_7988'] = func_7988
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8046 = relay.var("var_8046", dtype = "float64", shape = (12, 1, 13))#candidate|8046|(12, 1, 13)|var|float64
uop_8047 = relay.sigmoid(var_8046.astype('float64')) # shape=(12, 1, 13)
output = relay.Tuple([uop_8047,])
output2 = relay.Tuple([uop_8047,])
func_8049 = relay.Function([var_8046,], output)
mod['func_8049'] = func_8049
mod = relay.transform.InferType()(mod)
var_8050 = relay.var("var_8050", dtype = "float64", shape = (12, 1, 13))#candidate|8050|(12, 1, 13)|var|float64
output = func_8049(var_8050)
func_8051 = relay.Function([var_8050], output)
mutated_mod['func_8051'] = func_8051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3420_call = mutated_mod.get_global_var('func_3420')
call_8062 = func_3418_call()
call_8063 = func_3418_call()
output = call_8062
output2 = call_8063
func_8071 = relay.Function([], output)
mod['func_8071'] = func_8071
mod = relay.transform.InferType()(mod)
mutated_mod['func_8071'] = func_8071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8071_call = mutated_mod.get_global_var('func_8071')
call_8072 = func_8071_call()
output = call_8072
func_8073 = relay.Function([], output)
mutated_mod['func_8073'] = func_8073
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8085 = relay.const([[[10,-8,-8,-1,-10,2,-10,5,-9,-2,9,-7],[-6,4,7,2,5,-4,-10,-5,3,2,-8,-5],[8,-6,-7,1,-7,-1,-9,6,2,-9,4,3],[-3,5,4,8,5,-8,-6,6,-4,-10,10,10],[-5,-4,-5,8,-2,9,3,9,-1,10,5,-9],[-3,-3,6,-6,-2,-1,7,-3,4,-6,-9,-5],[-9,-8,-1,3,-7,-10,10,3,6,9,3,2],[-5,-4,-1,-7,-2,-5,1,10,6,10,-3,10],[-4,1,-2,-7,-1,-3,8,3,2,-4,5,10],[1,7,-10,-3,5,-6,-9,6,-3,-2,-7,-10],[10,2,9,9,2,6,-5,10,7,9,-8,5],[3,2,-2,-1,-8,10,-4,1,-6,-10,8,-1]],[[4,2,-6,-3,4,-1,8,9,-4,5,-9,-6],[3,-4,-5,-7,-6,3,8,10,-1,-10,-10,5],[9,2,8,1,-5,4,1,-9,2,8,9,-2],[9,-9,1,3,-6,6,-4,-7,3,8,-5,-8],[10,5,-3,10,-8,-1,3,-9,-2,4,3,6],[5,9,-3,-6,-2,-2,1,9,9,8,-7,-2],[5,4,9,3,5,5,10,1,-4,9,3,5],[-9,5,-2,-4,2,5,9,7,-2,2,-4,6],[-3,3,6,-9,3,-10,10,-1,1,4,-8,5],[-3,-3,-9,-3,5,-10,6,-5,-5,3,8,-8],[4,8,4,1,10,2,-3,2,5,-1,3,-9],[1,-6,9,-6,7,-2,-9,8,-7,9,-9,9]]], dtype = "uint16")#candidate|8085|(2, 12, 12)|const|uint16
var_8086 = relay.var("var_8086", dtype = "uint16", shape = (2, 12, 12))#candidate|8086|(2, 12, 12)|var|uint16
bop_8087 = relay.minimum(const_8085.astype('uint16'), relay.reshape(var_8086.astype('uint16'), relay.shape_of(const_8085))) # shape=(2, 12, 12)
func_3143_call = mod.get_global_var('func_3143')
func_3148_call = mutated_mod.get_global_var('func_3148')
const_8093 = relay.const([-4.020312,-9.246819,6.952890,6.055113,-1.257688,6.183101,6.360379,1.241371,3.071698,7.713820,4.679085,-9.157341,-7.903006,-3.121145,-5.578663,-5.930733,2.921950,-6.776666,6.876387,4.792646,4.528213,-8.060248,-2.886596,3.992758,6.167748,-7.271562,3.419173,-7.992031,-9.739721,2.365777,-5.875826,1.202908,-4.007638,2.288651,1.449627,0.980130,8.992827,-6.304674,3.067355,-4.247298,-9.617816,-6.067538,3.735349,8.856183,2.667579,-9.183996,0.960531,9.836605,4.956261,8.981349,5.116072,9.950286,0.345175,4.732231,8.200797,3.076489,-6.788116,3.624312,-4.807252,6.874659,3.022217,-6.973733,8.499149,1.735953,-6.998559,-7.076844,3.907553,-0.131615,2.383720,-4.986544,5.336810,-0.685425,1.275691,-5.460660,2.346223,1.477304,8.441691,5.473988,4.873121,-2.260260,8.565195,-1.569886,-9.007954,0.373303,-0.114027,0.675983,2.585954,0.048351,9.437571,4.558931,-2.596089,-3.406407,-4.758952,-5.363776,-1.862063,6.285655,4.543272,-3.010933,-9.900303,0.989270,6.539383,0.019177,3.333678,4.921058,-4.845490,2.959397,2.483449,-1.637327,0.800875,-3.273073,3.131384,4.328051,3.807615,0.790896,-3.774236,-1.223342,6.848033,-6.067073,-3.520834,9.449108,-9.591812,6.420877,-2.598989,0.793522,3.821981,3.349655,3.482710,2.632317,4.315956,8.697172,-0.841264,6.664873,5.805122,-0.671704,-7.092562,-0.659609,-6.995070,-2.420464,3.627328,-7.059687,7.720870,-6.090035,-4.191804,5.811718,-1.516132,3.390260,-0.887951,-5.896583,8.918131,-6.770416,-6.421253,-7.650564,-1.934446,-7.210907,4.725457,-9.460079,-3.446261,4.476339,1.172456,-1.476919,4.300425,-3.731763,9.890121,5.822814,4.893828,-8.406750,-6.109697,-0.482784,7.009593,9.216226,7.597204,-8.845101,-4.794100,-7.073710,-4.785110,3.432259,9.212558,-5.457847,-4.053394,7.159143,8.248985,1.361666,-0.619221,-9.029698,-6.182192,-6.845499,-7.373416,-9.117922,6.357906,-0.619565,9.232210,2.963701,1.700268,2.792088,-3.622130,9.142071,-6.980829,4.059564,-0.503993,5.875933,0.867362,-3.592679,-0.493301,-6.428226,4.698194,9.129850,-8.751217,7.644502,-9.007804,6.512582,3.902523,-2.211028,-2.482084,0.304398,-9.418822,2.297403,-4.424465,9.301613,-7.802029,-7.649569,-9.087837,9.114919,5.348770,-4.564736,9.196062,-6.804115,-1.128530,1.001449,-2.185938,2.389349,5.297520,4.497609,-8.529623,-7.142359,-7.288866,-2.912568,-5.062735,-6.871164,2.715189,-0.080957,-4.005573,4.279993,3.023227,6.091081,0.977693,-8.860980,-6.249451,9.599658,-9.176151,8.002412,-1.718856,5.379348,3.398725,-3.744041,-5.745776,-8.396589,8.322412,3.887150,-3.242903,6.211338,0.506791,-3.426296,8.728425,-9.581730,7.537787,-6.197176,-9.343279,-4.301971,8.049181,-6.852186,7.387656,8.340860,-0.480112,-5.981265,1.530122,3.865704,1.212372,-2.650728,6.030269,4.884312,6.492976,-7.924860,0.129312,1.968243,-9.732500,9.480524,-5.868000,-2.379530,2.887780,1.178246,-8.889699,-8.528026,-2.297818,-5.963152,0.279450,-4.709379,-3.509923,-9.704185,-2.773544,-2.960759], dtype = "float32")#candidate|8093|(300,)|const|float32
const_8094 = relay.const([[4.978360,3.217518,3.400962,8.804993],[-1.494942,-2.460149,8.550707,-5.784753],[-3.906598,-5.508813,-1.904248,1.584716],[4.033620,-0.343539,-1.517349,5.453296],[6.805081,8.616757,-3.067205,-8.053280],[-2.667831,-7.612115,-9.484039,-7.434977],[2.647658,-9.062186,0.495734,-3.948031],[-4.299156,-2.601560,-7.526898,-4.101827],[1.284531,-2.044035,-1.369141,-3.911585],[7.966405,-2.484617,8.323273,9.526806],[-7.409145,-5.805170,8.366639,-4.044819],[-6.236144,-3.930449,-4.932547,-2.985240],[-8.762734,-4.661208,6.723324,-0.742443],[3.649899,-5.269729,7.766125,2.413807],[8.048886,3.339048,-8.147902,0.872488],[-4.185005,2.028635,-7.296325,-9.478672],[-6.199207,-2.740480,5.421286,9.608022],[8.967328,9.569837,4.388523,-4.851166],[4.041886,0.862632,-5.163282,-1.542760],[-1.404836,2.481726,9.940004,-5.988448],[-1.684096,3.739180,5.591373,-8.969828],[-3.670116,7.867440,-3.088651,8.437015],[8.940648,-8.722411,9.817535,-5.804673],[-1.387690,-7.804792,-9.126214,-9.275655],[2.193171,-9.925627,-4.933519,-5.653345],[4.305499,-4.637370,2.403155,9.469356],[-4.146537,-9.189197,-0.926413,7.929659],[8.721359,-9.717923,-4.088476,-6.367909],[-9.965791,-2.064730,-5.143597,0.556670],[-7.773511,5.821556,7.129868,-6.587212],[-2.014075,3.066522,-2.260431,-4.589379],[1.978091,1.471107,0.809816,5.549861],[-9.884719,-4.230987,-7.104563,-5.368324],[7.173367,5.447035,-6.001880,-2.932148],[-5.895952,8.093076,-1.304935,-3.595591],[-8.391457,-0.487820,-8.231877,0.998125],[2.353320,5.440588,-8.634969,1.204332],[0.982452,-7.995538,-8.089702,1.489202],[5.317208,0.259334,-0.352563,7.264516],[1.146804,-4.994558,6.016285,2.839761],[2.420532,1.492663,-7.256743,9.255952],[8.293015,-2.757318,-6.382215,-0.719480],[-1.496705,9.092782,-0.490744,-4.658459],[-3.566455,5.256265,-7.357453,0.644271],[7.030596,1.523109,7.487319,6.992975],[6.603834,-7.170249,1.128620,1.364954],[1.957140,-4.533296,6.038844,0.838896],[0.483917,3.746942,9.792926,5.731833],[9.491207,6.585849,9.541414,2.723559],[-2.701012,-4.638469,7.656711,4.493206],[1.310927,-1.761563,-9.994536,-1.810072],[-6.550815,-5.695042,-7.587390,-3.109019],[-4.283279,-8.301484,-4.968055,-8.630395],[-2.228157,5.709720,-0.859052,-7.118525],[-2.884923,-5.616763,-3.501103,9.562042],[9.885037,6.433328,3.983238,2.642596],[8.204595,-4.219045,-4.214475,-4.052217],[1.451198,-7.473709,-5.618378,4.473777],[5.986770,-0.058015,5.600887,-3.079419],[4.041797,-9.710960,5.405719,-4.370676],[-0.025389,-1.082723,-6.677473,6.516360],[-7.994669,3.265927,-6.950840,-7.347604],[7.111463,7.577676,-7.730207,9.515271],[5.136107,-2.904528,3.434555,1.288509],[0.120611,-8.216244,-9.673932,-7.438068],[9.883659,-2.607086,-5.064896,7.547864],[2.633229,-6.219957,-2.239192,3.235468],[-1.799517,-4.561009,-9.981019,3.584728],[-2.245213,0.470044,1.555074,3.904975],[-3.815736,-9.339547,-4.242825,-3.811816],[-8.052963,8.557334,-6.499309,5.129634],[1.029595,-7.958137,4.124741,7.903689],[-6.833215,5.033439,-7.638842,-6.754200],[-2.229686,-9.117422,1.655394,-2.277473],[6.627906,-0.996089,-9.177506,-8.634224],[-7.219390,6.497453,-8.866261,2.644576],[-0.577341,-1.968794,5.726954,5.978280],[3.991049,4.533793,-3.677001,6.766523]], dtype = "float32")#candidate|8094|(78, 4)|const|float32
const_8095 = relay.const([1,10,6,7,-7,4,5,-2,10,-7,-9,-7,-8,8,-8,-3,-7,-6,3,4,-4,3,-4,2,-5,10,9,-6,2,6,-3,10,4,-2,1,4,-6,7,-1,8,10,-10,7,-8,10,-8,5,-2,8,-5,-1,4,-5,9,-10,4,7,8,7,-3,-2,-9,-3,-7,4,9,8,-3,4,2,1,5,7,-1,1,-1,-5,3,1,8,-9,-9,10,-1,5,2,9,-3,-1,1,8,-7,4,2,10,-1,7,-6,-3,3,2,6,-3,6,-5,7,2,-8,-6,2,-10,-4,4,-4,-9,-6,6,-10,3,4,6,-3,9,-5,-2,2,-1,-9,-6,-1,-3,6,1,8,-6,3,-6,-10,-6,10,1,9,6,-8,-2,7,-8,-5,-1,-4,-7,-6,-3,-8,1,-8,7,6,-7,10,-5,-9,2,-1,-8,7,-2,-8,1,-6,3,-9,-1,-8,9,-10,-4,7,-4,6,-5,-7,10,-4,3,-5,1,-1,-9,3,-6,4,3,-6,2,-8,7,-8,5,9,-1,6,-10,-6,-5,-1,-5,1,-8,6,-8,-9,-2,-3,-8,-4,-9,-2,-9,-10,-9,-7,5,2,-6,-5,3,-3,-2,1,-1,10,-9,-10,3,5,10,6,-4,1,7,8,4,6,-8,-10,5,-8,2,-3,8,7,-3,-3,1,9,-2,9,-8,3,-5,-6,3,-3,4,10,-5,9,-9,-5,8,10,10,-7,-6,6,-3,10,-6,1,-10,-1,-9,10,-3,-8,-10,-1,10,1,-8,9,-9,7,3,-5,-10,-7,5,9,-4,-8,-7,-7,7,-5,6,8,3,3,5,9,6,-4,-3,10,-2,-4,-7,6,-8,1,-2,-1,6,1,4,7,-5,-1,-6,8,9,-4,2,2,-8,-5,-4,7,10,1,7,-4,-1,-3,-7,-2,2,3,-8,3,8,8,4,-3,-3,-10,2,-5,10,9,-10,4,-9,-5,1,-2,-7,2,6,-8,10,9,4,5,3,-1,-5,4,-1,-2,10,3,6,9,-3,-3,6,4,-8,-4,-3,4,2,-3,-9,-7,-8,-6,-8,-8,-3,1,-5,-9,-4,-1,-8,4,-3,2,1,-2,-10,7,5,-6,-6,-8,-1,-3,-10,1,-9,9,-1,5,10,5,6,-9,-7,9,-1,-6,6,9,-6,-5,5,-9,6,-2,-3,-10,9,2,-2,1,10,10,-9,-3,7,-9,3,-1,-6,-7,8,-10,7,-2,4,4,3,1,3,4,-3,4,-3,-7,6,7,-3,2,8,-9,-9,4,9,1,-9,-3,10,-8,-10,9,1,1,-3,-4,-7,1,7,8,-3,7,-6,4,-6,8,-9,4,-2,-4,8,-4,-10,-2,2,-3,1,-9,-2,2,7,-6,6,8,4,3,-1,-10,-5,8,-4,-2,-2,-3,-6,-2,6,1,7,10,-1,-7,3,3,-10,5,3,9,10,10,9,-9,2,-7,-9,-4,1,5,7,-3,-1,10,-8,1,-3,4,-5,-6,-4,7,9,6,-1,7,-8,-4,1,-5,3,8,7,7,-8,-8,-6,-4,6,-7,10,6,4,-9,6,-5,7,4,-9,5,-5,-8,8,6,-1,-3,-8,-8,-1,-9,-8,5,-10,-9,-3,4,7,-9,-3,1,9,-4,-2,-1,-9,9,7,-5,6,-7,8,7,5,-2,-10,-4,-8,-9,-1,5,-3,9,10,-8,-8,5,8,5,7,-4,2,-9,-6,-1,9,9,2,-3,-2,1,7,9,-8,-9,-2,2,-10,-6,-9,3,5,-9,2,9,2,7,6,5,10,8,6,8,3,2,3,10,-9,-2,1,-6,-1,-2,-9,-8,-2,3,-8,-6,6,-1,-5,-4,-9,7,8,-3,-8,-6,4,8,-10,-4,1,-9,7,-4,2,7,6,3,1,3,-3,-8,2,-10,4,-1,3,-4,10,1,7,5,-5,-7,4,-6,8,-3,8,3,7,-9,-5,-1,2,-9,1,10,10,-2,7,1,-10,6,-8,-1,4,-7,4,4,-9,5,-6,-6,4,1,6,7,-8,5,3,-3,8,5,-6,-8,-3,5,-9,8,-10,3,10,-3,4,-4,-4,5,7,-3,-1,7,3,-7,-2,-6,-1,10,10,2,9,-2,-5,4,6,-6,-8,5,5,-6,5,1,10,9,-5,5,-1,9,-5,-9,-10,-10,-7,2,6,-1,9,-9,5,10,-1,4,-3,7,3,10,10,-6,4,-1,7,3,7,-6,10,-10,2,-2,-6,4,4,5,-4,4,-8,-10,8,2,3,-10,3,-3,-6,1,-3,-1,10,4,-8,4,3,2,7,-9,-1,5,-10,8,-5,-8,-5,9,9,-1,-2,-5,-1,8,-3,2,5,8,8,-1,-7,3,-8,-9,-6,5,7,2,-9,8,7,-7,-7,-10,-5,8,-10,5,-3,-6,-7,4,-1,4,7,5,1,-6,9,3,-9,-7,2,-10,8,-4,6,-1,-4,-10,-8,-5,-9,7,-9,3,1,-8,1,8,1,-6,-9,8,3,-6,-5,8,-4,-5,5,-2,7,9,-5,9,8,6,4,1,-4,-8,10,4,-1,10,6,-2,1,2,8,-5,-7,-4,-5,-8,-5,-9,-2,-10,1,-1,-3,1,-6,-1,4,-3,-7,2,5,2,-6,-5,-5,1,7,2,-9,-6,-5,1,3,10,4,-3,-4,7,7,6,8,-7,-3,5,-3,7,7,9,6,3,3,-9,2,-7,-9,-10,-2,2,-7,7,7,10,-4,8,-8,1,7,-10,-7,8,10,3,-5,9,-1,2,10,5,-10,-5,-4,-2,6,9,-7,-1,3,8,10,-1,-4,10,4,-10,-8,5,-3,2,8,-5,6,-1,2,8,9,-5,-2,-6,10,-3,5,2,-4,9,6,7,2,3,-1,7,10,-2,-7,-9,8,-9,1,-9,6,6,-2,1,5,9,5,-6,6,-7,6,-1,-9,7,2,4,-6,7,5,3], dtype = "int8")#candidate|8095|(1120,)|const|int8
call_8092 = relay.TupleGetItem(func_3143_call(relay.reshape(const_8093.astype('float32'), [15, 4, 5]), relay.reshape(const_8094.astype('float32'), [6, 52]), relay.reshape(const_8095.astype('int8'), [8, 14, 10]), ), 2)
call_8096 = relay.TupleGetItem(func_3148_call(relay.reshape(const_8093.astype('float32'), [15, 4, 5]), relay.reshape(const_8094.astype('float32'), [6, 52]), relay.reshape(const_8095.astype('int8'), [8, 14, 10]), ), 2)
func_2080_call = mod.get_global_var('func_2080')
func_2084_call = mutated_mod.get_global_var('func_2084')
var_8102 = relay.var("var_8102", dtype = "int8", shape = (2, 56))#candidate|8102|(2, 56)|var|int8
call_8101 = relay.TupleGetItem(func_2080_call(relay.reshape(var_8102.astype('int8'), [112,]), relay.reshape(const_8095.astype('int8'), [1120,]), ), 4)
call_8103 = relay.TupleGetItem(func_2084_call(relay.reshape(var_8102.astype('int8'), [112,]), relay.reshape(const_8095.astype('int8'), [1120,]), ), 4)
uop_8126 = relay.erf(const_8094.astype('float32')) # shape=(78, 4)
var_8134 = relay.var("var_8134", dtype = "float32", shape = (300,))#candidate|8134|(300,)|var|float32
bop_8135 = relay.floor_mod(const_8093.astype('float32'), relay.reshape(var_8134.astype('float32'), relay.shape_of(const_8093))) # shape=(300,)
output = relay.Tuple([bop_8087,call_8092,const_8095,call_8101,var_8102,uop_8126,bop_8135,])
output2 = relay.Tuple([bop_8087,call_8096,const_8095,call_8103,var_8102,uop_8126,bop_8135,])
func_8140 = relay.Function([var_8086,var_8102,var_8134,], output)
mod['func_8140'] = func_8140
mod = relay.transform.InferType()(mod)
mutated_mod['func_8140'] = func_8140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8140_call = mutated_mod.get_global_var('func_8140')
var_8142 = relay.var("var_8142", dtype = "uint16", shape = (2, 12, 12))#candidate|8142|(2, 12, 12)|var|uint16
var_8143 = relay.var("var_8143", dtype = "int8", shape = (2, 56))#candidate|8143|(2, 56)|var|int8
var_8144 = relay.var("var_8144", dtype = "float32", shape = (300,))#candidate|8144|(300,)|var|float32
call_8141 = func_8140_call(var_8142,var_8143,var_8144,)
output = call_8141
func_8145 = relay.Function([var_8142,var_8143,var_8144,], output)
mutated_mod['func_8145'] = func_8145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5341_call = mod.get_global_var('func_5341')
func_5343_call = mutated_mod.get_global_var('func_5343')
call_8151 = func_5341_call()
call_8152 = func_5341_call()
output = relay.Tuple([call_8151,])
output2 = relay.Tuple([call_8152,])
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
func_5559_call = mod.get_global_var('func_5559')
func_5560_call = mutated_mod.get_global_var('func_5560')
call_8208 = relay.TupleGetItem(func_5559_call(), 0)
call_8209 = relay.TupleGetItem(func_5560_call(), 0)
output = call_8208
output2 = call_8209
func_8210 = relay.Function([], output)
mod['func_8210'] = func_8210
mod = relay.transform.InferType()(mod)
mutated_mod['func_8210'] = func_8210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8210_call = mutated_mod.get_global_var('func_8210')
call_8211 = func_8210_call()
output = call_8211
func_8212 = relay.Function([], output)
mutated_mod['func_8212'] = func_8212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3870_call = mod.get_global_var('func_3870')
func_3871_call = mutated_mod.get_global_var('func_3871')
call_8246 = relay.TupleGetItem(func_3870_call(), 0)
call_8247 = relay.TupleGetItem(func_3871_call(), 0)
func_1535_call = mod.get_global_var('func_1535')
func_1538_call = mutated_mod.get_global_var('func_1538')
call_8270 = relay.TupleGetItem(func_1535_call(relay.reshape(call_8246.astype('float32'), [1, 312])), 2)
call_8271 = relay.TupleGetItem(func_1538_call(relay.reshape(call_8246.astype('float32'), [1, 312])), 2)
output = relay.Tuple([call_8246,call_8270,])
output2 = relay.Tuple([call_8247,call_8271,])
func_8276 = relay.Function([], output)
mod['func_8276'] = func_8276
mod = relay.transform.InferType()(mod)
mutated_mod['func_8276'] = func_8276
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8276_call = mutated_mod.get_global_var('func_8276')
call_8277 = func_8276_call()
output = call_8277
func_8278 = relay.Function([], output)
mutated_mod['func_8278'] = func_8278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3492_call = mod.get_global_var('func_3492')
func_3494_call = mutated_mod.get_global_var('func_3494')
call_8315 = relay.TupleGetItem(func_3492_call(), 1)
call_8316 = relay.TupleGetItem(func_3494_call(), 1)
output = relay.Tuple([call_8315,])
output2 = relay.Tuple([call_8316,])
func_8328 = relay.Function([], output)
mod['func_8328'] = func_8328
mod = relay.transform.InferType()(mod)
mutated_mod['func_8328'] = func_8328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8328_call = mutated_mod.get_global_var('func_8328')
call_8329 = func_8328_call()
output = call_8329
func_8330 = relay.Function([], output)
mutated_mod['func_8330'] = func_8330
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8339 = relay.var("var_8339", dtype = "float64", shape = ())#candidate|8339|()|var|float64
var_8340 = relay.var("var_8340", dtype = "float64", shape = (2, 15, 14))#candidate|8340|(2, 15, 14)|var|float64
bop_8341 = relay.mod(var_8339.astype('float64'), var_8340.astype('float64')) # shape=(2, 15, 14)
output = bop_8341
output2 = bop_8341
func_8360 = relay.Function([var_8339,var_8340,], output)
mod['func_8360'] = func_8360
mod = relay.transform.InferType()(mod)
var_8361 = relay.var("var_8361", dtype = "float64", shape = ())#candidate|8361|()|var|float64
var_8362 = relay.var("var_8362", dtype = "float64", shape = (2, 15, 14))#candidate|8362|(2, 15, 14)|var|float64
output = func_8360(var_8361,var_8362,)
func_8363 = relay.Function([var_8361,var_8362,], output)
mutated_mod['func_8363'] = func_8363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3841_call = mod.get_global_var('func_3841')
func_3842_call = mutated_mod.get_global_var('func_3842')
call_8368 = relay.TupleGetItem(func_3841_call(), 0)
call_8369 = relay.TupleGetItem(func_3842_call(), 0)
func_3950_call = mod.get_global_var('func_3950')
func_3952_call = mutated_mod.get_global_var('func_3952')
call_8395 = relay.TupleGetItem(func_3950_call(), 0)
call_8396 = relay.TupleGetItem(func_3952_call(), 0)
func_4208_call = mod.get_global_var('func_4208')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_8399 = relay.TupleGetItem(func_4208_call(), 1)
call_8400 = relay.TupleGetItem(func_4209_call(), 1)
func_7640_call = mod.get_global_var('func_7640')
func_7642_call = mutated_mod.get_global_var('func_7642')
call_8418 = func_7640_call()
call_8419 = func_7640_call()
output = relay.Tuple([call_8368,call_8395,call_8399,call_8418,])
output2 = relay.Tuple([call_8369,call_8396,call_8400,call_8419,])
func_8428 = relay.Function([], output)
mod['func_8428'] = func_8428
mod = relay.transform.InferType()(mod)
output = func_8428()
func_8429 = relay.Function([], output)
mutated_mod['func_8429'] = func_8429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1912_call = mod.get_global_var('func_1912')
func_1914_call = mutated_mod.get_global_var('func_1914')
call_8451 = relay.TupleGetItem(func_1912_call(), 0)
call_8452 = relay.TupleGetItem(func_1914_call(), 0)
func_1964_call = mod.get_global_var('func_1964')
func_1967_call = mutated_mod.get_global_var('func_1967')
var_8454 = relay.var("var_8454", dtype = "uint32", shape = (363,))#candidate|8454|(363,)|var|uint32
call_8453 = relay.TupleGetItem(func_1964_call(relay.reshape(var_8454.astype('uint32'), [363,])), 1)
call_8455 = relay.TupleGetItem(func_1967_call(relay.reshape(var_8454.astype('uint32'), [363,])), 1)
func_6742_call = mod.get_global_var('func_6742')
func_6744_call = mutated_mod.get_global_var('func_6744')
const_8457 = relay.const([2,6,4,10,-2,10,-3,-10,2,-9,2,5,6,-9,6,6,-5,3,-2,9,9,-2,10,7,1,-7,2,7,5,-2,-5,-10,-5,-2,-8,-8,2,7,-5,4,-2,9,2,2,3,10,-6,-10,3,-5,5,-6,-7,-1,-1,8,-5,-9,-4,-8,-7,-5,-9,2,-9,3,-4,2,-5,-6,7,10,-3,-1,-10,-2,-7,9,-1,10,-2,3,1,7,-6,2,7,7,1,-4,7,9,2,2,3,-3,-4,-8,2,10,-8,-3,-4,-2,-8,-9,2,-3,-8,-10,-8,5,-9,-6,8,-3,8,-9,6,-1,-10,3,8,8,2,8,-1,9,-6,5,1,-10,3,3,-5,-8,-5,-6,-7,-3,-2,-9,6,7,5,7,9,6,9,1,-6,-6,10,-5,6,-7,9,-5,8,-6,-3,8,10,-4,-7,-2,6,3,-2,6,-4,-8,1,-7,-7,-1,-6,2,4,5,-3,-4,7,-6,6,8,-4,-5,2,-3,7,-9], dtype = "uint64")#candidate|8457|(192,)|const|uint64
call_8456 = relay.TupleGetItem(func_6742_call(relay.reshape(const_8457.astype('uint64'), [2, 8, 12])), 1)
call_8458 = relay.TupleGetItem(func_6744_call(relay.reshape(const_8457.astype('uint64'), [2, 8, 12])), 1)
func_3212_call = mod.get_global_var('func_3212')
func_3214_call = mutated_mod.get_global_var('func_3214')
call_8462 = relay.TupleGetItem(func_3212_call(), 0)
call_8463 = relay.TupleGetItem(func_3214_call(), 0)
func_8071_call = mod.get_global_var('func_8071')
func_8073_call = mutated_mod.get_global_var('func_8073')
call_8467 = func_8071_call()
call_8468 = func_8071_call()
bop_8471 = relay.bitwise_or(call_8456.astype('int16'), relay.reshape(call_8451.astype('int16'), relay.shape_of(call_8456))) # shape=(6, 13, 4)
bop_8474 = relay.bitwise_or(call_8458.astype('int16'), relay.reshape(call_8452.astype('int16'), relay.shape_of(call_8458))) # shape=(6, 13, 4)
output = relay.Tuple([call_8453,var_8454,const_8457,call_8462,call_8467,bop_8471,])
output2 = relay.Tuple([call_8455,var_8454,const_8457,call_8463,call_8468,bop_8474,])
func_8499 = relay.Function([var_8454,], output)
mod['func_8499'] = func_8499
mod = relay.transform.InferType()(mod)
mutated_mod['func_8499'] = func_8499
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8500 = relay.var("var_8500", dtype = "uint32", shape = (363,))#candidate|8500|(363,)|var|uint32
func_8499_call = mutated_mod.get_global_var('func_8499')
call_8501 = func_8499_call(var_8500)
output = call_8501
func_8502 = relay.Function([var_8500], output)
mutated_mod['func_8502'] = func_8502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4209_call = mutated_mod.get_global_var('func_4209')
call_8529 = relay.TupleGetItem(func_4208_call(), 0)
call_8530 = relay.TupleGetItem(func_4209_call(), 0)
func_4822_call = mod.get_global_var('func_4822')
func_4824_call = mutated_mod.get_global_var('func_4824')
call_8540 = relay.TupleGetItem(func_4822_call(), 0)
call_8541 = relay.TupleGetItem(func_4824_call(), 0)
output = relay.Tuple([call_8529,call_8540,])
output2 = relay.Tuple([call_8530,call_8541,])
func_8563 = relay.Function([], output)
mod['func_8563'] = func_8563
mod = relay.transform.InferType()(mod)
mutated_mod['func_8563'] = func_8563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8563_call = mutated_mod.get_global_var('func_8563')
call_8564 = func_8563_call()
output = call_8564
func_8565 = relay.Function([], output)
mutated_mod['func_8565'] = func_8565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3907_call = mod.get_global_var('func_3907')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_8618 = relay.TupleGetItem(func_3907_call(), 0)
call_8619 = relay.TupleGetItem(func_3909_call(), 0)
output = relay.Tuple([call_8618,])
output2 = relay.Tuple([call_8619,])
func_8622 = relay.Function([], output)
mod['func_8622'] = func_8622
mod = relay.transform.InferType()(mod)
mutated_mod['func_8622'] = func_8622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8622_call = mutated_mod.get_global_var('func_8622')
call_8623 = func_8622_call()
output = call_8623
func_8624 = relay.Function([], output)
mutated_mod['func_8624'] = func_8624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6558_call = mod.get_global_var('func_6558')
func_6560_call = mutated_mod.get_global_var('func_6560')
call_8720 = func_6558_call()
call_8721 = func_6558_call()
output = relay.Tuple([call_8720,])
output2 = relay.Tuple([call_8721,])
func_8736 = relay.Function([], output)
mod['func_8736'] = func_8736
mod = relay.transform.InferType()(mod)
output = func_8736()
func_8737 = relay.Function([], output)
mutated_mod['func_8737'] = func_8737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_8783 = relay.TupleGetItem(func_7075_call(), 0)
call_8784 = relay.TupleGetItem(func_7076_call(), 0)
func_6167_call = mod.get_global_var('func_6167')
func_6170_call = mutated_mod.get_global_var('func_6170')
const_8790 = relay.const(7.365574, dtype = "float64")#candidate|8790|()|const|float64
call_8789 = relay.TupleGetItem(func_6167_call(relay.reshape(const_8790.astype('float64'), [])), 5)
call_8791 = relay.TupleGetItem(func_6170_call(relay.reshape(const_8790.astype('float64'), [])), 5)
func_3536_call = mod.get_global_var('func_3536')
func_3538_call = mutated_mod.get_global_var('func_3538')
var_8802 = relay.var("var_8802", dtype = "float64", shape = (780,))#candidate|8802|(780,)|var|float64
call_8801 = relay.TupleGetItem(func_3536_call(relay.reshape(var_8802.astype('float64'), [5, 13, 12])), 4)
call_8803 = relay.TupleGetItem(func_3538_call(relay.reshape(var_8802.astype('float64'), [5, 13, 12])), 4)
output = relay.Tuple([call_8783,call_8789,const_8790,call_8801,var_8802,])
output2 = relay.Tuple([call_8784,call_8791,const_8790,call_8803,var_8802,])
func_8820 = relay.Function([var_8802,], output)
mod['func_8820'] = func_8820
mod = relay.transform.InferType()(mod)
mutated_mod['func_8820'] = func_8820
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8821 = relay.var("var_8821", dtype = "float64", shape = (780,))#candidate|8821|(780,)|var|float64
func_8820_call = mutated_mod.get_global_var('func_8820')
call_8822 = func_8820_call(var_8821)
output = call_8822
func_8823 = relay.Function([var_8821], output)
mutated_mod['func_8823'] = func_8823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2163_call = mutated_mod.get_global_var('func_2163')
call_8848 = relay.TupleGetItem(func_2162_call(), 0)
call_8849 = relay.TupleGetItem(func_2163_call(), 0)
func_7575_call = mod.get_global_var('func_7575')
func_7580_call = mutated_mod.get_global_var('func_7580')
const_8865 = relay.const([-9,2,8,6,9,1,-3,-4,-5,-6,-9,-2,-8,7,5,7,-1,-9,-8,-6,3,6,-10,-6,-3,6,5,-6,-4,-6,-5,10,1,-6,-4,-6,2,6,-4,-6,3,8,-7,-3,-7,9,2,-7,9,-2,8,2,1,9,-8,-4,-7,1,7,7,2,6,-5,7,-8,9,-10,-5,8,-8,-1,9,3,1,5,3,-4,-1,2,5,8,8,-4,9,-7,8,7,5,9,-1,-4,2,-3,-8,-3,-7,-4,1,7,10,6,3,5,-7,-4,1,-3,9,-7,3,10,3,6,-2,3,-9,9,-4,10,3,10,-3,8,-10,-6,5,4,2,9,3,7,10,-3,-2,-8,6,-10,2,8,-1,5,-2,3,9,7,3,-5,10,9,-1,-9,-6,4,7,10,-10,-3,3,6,7,5,7,-4,8,-1,10,-5,-8,-4,3,-2,-10,5,2,-7,-5,10,-4,9,6,10,1,-4,-6,-6,4,-4,-5,-10,-2,-6,9,9,8,5,1,2,3,-10,6,-10,4,-5,-2,-5,-1,-1,7,-4,-1,1,-6,-1,8,-8,7,-5,1,-9,-4,-9,-5,5,-2,7,10,3,-10,7,-6,-2,-2,-6,-6,7,-1,-5,7,-8,-1,-2,2,10,-10,10,9,-2,7,-5,-5,5,9,2,-1,4,-7,4,-2,9,-1,-9,-1,3,-9,2,-1,1,6,7,-6,-1,9,-2,2,-4,-10,-5,-6,-8,-9,10,-9,1,6,5,8,5,-1,-8,-6,-6,-7,-9,1,7,-10,-9,10,4,-7,6,-5,3,-5,9,-3,-2,-7,-5,-8,8,1,-7,-7,-7,-10,-10,-3,10,-5,-3,-5,-1,4,9,-8,10,-4,10,-9,-10,1,5,4,-4,-4,7,4,2,-4,1,-7,1,9,-7,-10,7,-6,5,-8,8,10,3,-3,-1,7,-9,5,8,-5,2,3,-7,4,8,5,-5,-1,-8,-5,-3,2,-7,-4,-3,-3,6,-4,2,9,9,-7,-8,7,3,8,4,-10,9,9,4,-6,-5,-5,8,8,7,-4,-4,-2,2,-4,2,-1,-7,2,10,2,-8,-4,-9,6,8,1,-2,2,5,-4,10,-7,-4,10,6,-1,9,1,-6,3,8,7,-1,5,4,4,-3,-5,-1,-2,7,9,9,-3,8,10,-4,-5,-7,-2,10,-9,8,-9,-8,-3,-6,-10,-4,-9,-1,-8,9,9,-6,9,8,6,-1,-4,-7,4,1,8,7,10,10,2,-3,-5,5,-2,3,8,4,5,-8,7,-10,-5,-4,-6,4,2,-10,-6,-5,7,-8,-2,-4,-6,-5,-2,-7,4,1,-4,8,2,-6,-5,7,-7,-7,-5,-7,3,-3,-8,1,10,2,7,-1,-9,5,6,-6,-5,5,3,-3,5,-3,-6,7,-6,-1,10,-2,-9,-5,-9,1,3,5,9,4,6,8,-2,8,-3,-1,-1,6,-9,6,-3,3,-2,-3,8,6,7,-4,9,6,-10,-7,-1,-2,3,10,4,3,2,10,3,4,10,-8,-1,-10,-1,-4,9,5,-4,7,8,8,4,-10,2,9,-3,10,1,-6,7,7,8,8,-6,-1,-3,-6,5,-7,1,10,5,7,9,2,-7,-4,10,-6,4,-3,-8,-7,-5,1,-4,-10,-10,7,-4,7,-8,6,-2,-6,-2,7,-8,-3,1,-10,5,-6,-1,-6,1,-6,-6,-9,-7,-7,4,8,-8,-6,9,6,8,-10,-2,-3,4,4,-2,-10,-5,-7,-9,-4,8,-6,8,10,1,-4,-8,9,-6,4,3,-6,-9,1,8,4,5,-4,3,10,5,8,5,-9,-10,1,-5,4,-10,1,-10,5,-7,2,-4,-4,8,-6,1,4,-8,-5,-1,-6,-5,8,-6,-3,-3,-4,7,8,2,-10,1,4,-8,2,-1,-10,-9,-2,-1,-9,1,-1,-1,-6,5,8,10,3,5,9,6,-2,8,-10,-10,3,-10,10,5,8,3,-6,-10,-5,6,10,-3,-7,-6,-2,-5,8,1,-1,-5,6,5,-3,5,-9,-1,-5,1,5,-10,-4,2,-10,-9,1,10,-3,1,7,1,-9,6,7,7,-5,-1,-1,2,-7,-4,6,-6,-8,-3,7,2,-8,-1,6,-9,6,-1,-4,-2,-3,-9,-10,-7,6,-5,8,8,-8,3,6,8,-3,-10,-1,9,-9,-4,-5,-1,-3,-3,-4,8,-9,-7,-4,-8,-3,7,-3,1,-5,2,7,3,10,2,-9,7,3,5,-8,-8,3,6,-2,-7,3,8,-5,-2,1,8,-6,5,8,9,-3,8,10,2,-2,-10,-8,-6,1,7,-4,1,-9,-1,8,-6,5,-7,-9,-9,-7,7,7,-10,3,-2,2,1,2,2,-2,-1,2,3,6,-4,1,10,-7,10,-10,1,8,7,1,-9,8,9,-5,-1,6,-6,9,9,-10,9,3,-4,-9,-10,8,5,-9,-6,-9,-7,-4,-4,-3,-2,9,-3,-9,-5,7], dtype = "uint16")#candidate|8865|(945,)|const|uint16
const_8866 = relay.const([False,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True], dtype = "bool")#candidate|8866|(448,)|const|bool
call_8864 = relay.TupleGetItem(func_7575_call(relay.reshape(const_8865.astype('uint16'), [9, 15, 7]), relay.reshape(const_8865.astype('uint16'), [9, 15, 7]), relay.reshape(const_8866.astype('bool'), [448,]), ), 3)
call_8867 = relay.TupleGetItem(func_7580_call(relay.reshape(const_8865.astype('uint16'), [9, 15, 7]), relay.reshape(const_8865.astype('uint16'), [9, 15, 7]), relay.reshape(const_8866.astype('bool'), [448,]), ), 3)
output = relay.Tuple([call_8848,call_8864,const_8865,const_8866,])
output2 = relay.Tuple([call_8849,call_8867,const_8865,const_8866,])
func_8871 = relay.Function([], output)
mod['func_8871'] = func_8871
mod = relay.transform.InferType()(mod)
mutated_mod['func_8871'] = func_8871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8871_call = mutated_mod.get_global_var('func_8871')
call_8872 = func_8871_call()
output = call_8872
func_8873 = relay.Function([], output)
mutated_mod['func_8873'] = func_8873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_8894 = func_2281_call()
call_8895 = func_2281_call()
var_8910 = relay.var("var_8910", dtype = "int8", shape = (8, 14, 10))#candidate|8910|(8, 14, 10)|var|int8
bop_8911 = relay.subtract(call_8894.astype('uint8'), relay.reshape(var_8910.astype('uint8'), relay.shape_of(call_8894))) # shape=(8, 14, 10)
bop_8914 = relay.subtract(call_8895.astype('uint8'), relay.reshape(var_8910.astype('uint8'), relay.shape_of(call_8895))) # shape=(8, 14, 10)
output = relay.Tuple([bop_8911,])
output2 = relay.Tuple([bop_8914,])
func_8916 = relay.Function([var_8910,], output)
mod['func_8916'] = func_8916
mod = relay.transform.InferType()(mod)
mutated_mod['func_8916'] = func_8916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8917 = relay.var("var_8917", dtype = "int8", shape = (8, 14, 10))#candidate|8917|(8, 14, 10)|var|int8
func_8916_call = mutated_mod.get_global_var('func_8916')
call_8918 = func_8916_call(var_8917)
output = call_8918
func_8919 = relay.Function([var_8917], output)
mutated_mod['func_8919'] = func_8919
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8931 = relay.var("var_8931", dtype = "int8", shape = (10, 15, 9))#candidate|8931|(10, 15, 9)|var|int8
const_8932 = relay.const([[[4,10,9,-3,7,4,5,6,1],[7,5,-7,-7,-5,-2,2,9,2],[-5,8,8,-2,2,-8,-7,-6,-5],[3,4,2,-2,-4,6,9,-10,5],[-9,-1,-2,5,-4,-2,-5,-10,-2],[7,-9,-7,4,8,2,-1,10,-3],[1,-4,8,1,-2,4,-5,9,9],[-1,-1,8,2,-6,1,7,-7,6],[-6,1,-2,-3,6,-1,6,-10,10],[-10,-7,-9,6,-2,-6,10,-9,-1],[6,8,-5,-6,10,10,4,-6,-8],[9,10,9,-2,-9,10,2,5,-5],[-8,1,-9,-1,1,-3,-2,-5,6],[10,10,10,3,-5,3,-9,3,10],[1,4,-1,-2,-9,-7,8,-4,-9]],[[10,8,10,-9,2,-9,3,-8,-1],[-4,-3,-10,10,10,-10,-10,-2,-8],[-2,1,9,8,9,1,-4,5,-7],[-8,2,-3,-8,3,-5,-4,9,1],[-3,-10,-5,-4,-5,6,1,1,3],[-8,-10,3,-3,10,-2,10,2,-10],[10,-5,1,6,-7,-7,-2,-5,7],[8,7,-2,3,-6,3,-1,8,-7],[-9,-10,2,1,4,8,6,-1,-8],[-3,6,-5,3,-1,1,-9,3,-1],[1,-10,-7,-6,8,7,-2,-6,-8],[-9,-6,4,-10,-10,-4,-7,2,-10],[10,2,-5,4,9,-8,-3,-10,9],[6,6,-2,6,7,-9,-7,-5,6],[9,-7,-2,-7,-4,-3,10,-2,-5]],[[9,4,-9,3,9,-6,9,-5,-4],[-5,-1,10,2,5,-6,-8,4,-1],[2,-9,-3,10,-10,10,3,7,-4],[7,-6,-2,5,-9,10,1,3,7],[-7,-10,1,3,7,7,6,9,-8],[-8,9,-9,-7,-2,-2,-8,7,6],[-2,-1,8,2,2,9,2,-3,3],[1,4,-2,-4,5,-10,9,-1,-3],[-8,4,6,-10,-1,1,-6,-3,6],[5,6,3,-5,10,-3,-5,-9,3],[-4,-6,-7,-8,9,-1,9,-7,10],[-4,4,-10,-8,10,-6,5,-5,5],[-7,-2,6,-1,1,-1,8,5,9],[9,-10,7,1,8,-2,-7,-5,5],[-6,8,4,10,7,4,-9,-5,3]],[[5,-3,-1,5,6,-8,-5,7,2],[5,5,-5,9,-5,5,8,3,4],[-8,1,2,5,2,1,5,-5,-9],[1,-8,-4,-4,4,6,1,-8,-8],[-10,6,-2,7,2,-8,-6,-10,-5],[7,7,-9,1,6,2,8,4,-7],[2,6,8,6,4,10,10,-1,9],[7,1,9,-7,7,-2,10,10,9],[-1,-4,3,-4,-1,8,-8,10,-2],[5,6,3,-8,-6,-10,-6,2,-5],[4,-7,-8,-5,-4,6,-5,-5,4],[-1,-10,3,-1,-2,1,-9,-9,-1],[5,-1,-2,7,9,8,-10,8,-5],[-4,9,1,-3,4,9,7,3,5],[9,3,-3,-3,-10,-7,-1,-3,-4]],[[10,-9,9,2,-3,6,-10,-9,-2],[4,7,6,2,4,-10,4,-6,-6],[10,-3,-5,-9,5,-2,10,4,-1],[-1,10,10,4,9,6,6,-5,7],[9,9,-5,3,-6,-5,9,-1,9],[-8,7,4,-3,9,9,-2,-3,-2],[-1,-6,-2,-7,4,10,1,-8,-5],[4,-3,10,9,10,-2,-2,9,-1],[6,-2,5,-8,1,-7,-8,-6,3],[3,-5,-4,7,-3,4,7,-1,-2],[2,7,8,10,6,-7,10,-1,-4],[6,-10,8,-3,6,6,4,-10,1],[-4,3,9,-9,1,5,-4,9,-8],[-10,3,-6,-3,-9,9,2,3,3],[7,-10,-1,-6,-6,1,-3,6,4]],[[-7,2,4,5,5,1,-9,-4,-7],[-4,10,-7,5,-1,-7,4,-5,-9],[-6,-5,2,2,4,-2,1,-5,5],[1,1,-2,-6,-2,1,-10,-6,1],[-10,-1,9,9,-9,-2,-4,6,-4],[8,7,2,1,-6,-6,-7,1,5],[1,-1,-6,-7,-7,-10,3,2,-7],[-9,-8,-9,1,-3,6,-4,1,9],[10,2,9,8,-9,4,-7,-8,8],[-9,3,-3,9,-8,-5,-10,3,2],[-3,7,-1,9,4,2,5,2,1],[-9,-5,5,-5,6,-6,-1,-9,10],[-9,-7,-6,-6,-8,1,4,-4,-8],[-10,3,-1,4,-7,-10,2,-5,2],[-8,6,-7,-9,-8,3,-1,9,8]],[[-10,-1,3,3,-1,-4,4,1,2],[-7,-10,-4,-1,5,7,-1,6,-6],[-3,4,-1,-5,4,5,8,7,-6],[-1,5,8,-1,-1,-1,6,9,-6],[-10,-5,10,10,-1,6,-7,-6,-4],[6,-5,2,7,-8,8,5,6,4],[-10,-4,3,-10,-6,7,-3,5,2],[-4,3,-3,7,-1,-8,10,1,-10],[-1,-9,1,5,8,3,-5,-7,8],[-9,8,9,7,7,-1,-4,-9,9],[10,-5,-4,-8,-5,9,-5,-10,10],[-2,-9,7,-5,-6,6,6,9,-4],[-10,-6,-9,8,-5,8,8,-6,-6],[10,-4,8,2,-7,7,-8,6,-10],[8,9,-4,3,-5,-2,-2,6,9]],[[-7,10,-1,-5,-4,2,-6,-1,6],[-9,9,7,-9,-4,-4,-9,-1,5],[5,-3,-1,-2,7,-9,9,1,-4],[-9,-9,7,3,6,-4,10,-9,10],[-7,-6,-6,-7,-4,4,1,2,4],[5,3,5,-10,-9,-7,-10,3,-1],[2,-5,8,-4,-3,-1,6,-8,9],[8,-8,10,-8,-2,-8,-2,-10,-7],[-8,-1,9,-2,10,-4,3,10,-3],[-7,-3,-3,-9,-1,4,1,-9,7],[-4,1,-8,5,-10,-3,5,3,-6],[-9,1,-7,-6,-9,1,-2,-4,1],[1,5,8,4,7,-1,4,-1,-10],[2,-5,2,8,10,-1,5,-6,-3],[10,10,-5,-4,1,-5,-2,-6,9]],[[-2,3,2,3,-6,-10,5,-6,-9],[6,-1,-7,-7,-5,-5,-2,-3,10],[-9,-5,-2,-5,4,2,4,7,2],[-4,-4,-3,-3,-9,-1,4,-2,8],[3,-2,5,-2,-9,-8,6,3,1],[10,-2,4,8,7,6,-5,-9,8],[1,4,-1,-3,6,-7,-2,5,-8],[9,-7,-7,2,-2,8,-6,9,1],[4,-7,9,-9,2,7,3,7,4],[4,7,6,7,-6,-2,8,-8,8],[10,-10,-3,4,3,-7,7,-3,-9],[-10,3,-5,-1,-2,-10,8,-10,-2],[-5,9,10,-5,9,-9,-8,-7,5],[7,6,8,-2,4,7,4,-4,10],[-9,1,4,8,-1,5,6,-3,-1]],[[-8,9,6,-10,8,3,6,-4,2],[6,-9,5,-4,-6,-5,8,-2,5],[-3,-8,7,-8,5,-1,-9,7,6],[2,4,7,-6,1,1,6,9,2],[5,-10,-1,5,9,-8,5,5,9],[-9,4,-1,-7,9,-10,3,-3,6],[-5,-6,5,9,5,1,3,-6,-1],[-4,-5,4,5,3,-2,6,9,2],[-7,6,-5,5,-9,7,-10,-8,-5],[10,-2,2,1,-1,-1,6,6,-9],[1,10,-4,3,7,9,-6,4,4],[-3,-5,7,9,-3,7,7,7,-9],[-4,7,4,5,-6,9,6,-9,8],[6,-9,-4,10,-6,9,-8,-10,6],[10,5,2,-8,-7,1,2,5,-6]]], dtype = "int8")#candidate|8932|(10, 15, 9)|const|int8
bop_8933 = relay.minimum(var_8931.astype('int8'), relay.reshape(const_8932.astype('int8'), relay.shape_of(var_8931))) # shape=(10, 15, 9)
output = bop_8933
output2 = bop_8933
func_8955 = relay.Function([var_8931,], output)
mod['func_8955'] = func_8955
mod = relay.transform.InferType()(mod)
mutated_mod['func_8955'] = func_8955
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8956 = relay.var("var_8956", dtype = "int8", shape = (10, 15, 9))#candidate|8956|(10, 15, 9)|var|int8
func_8955_call = mutated_mod.get_global_var('func_8955')
call_8957 = func_8955_call(var_8956)
output = call_8957
func_8958 = relay.Function([var_8956], output)
mutated_mod['func_8958'] = func_8958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5811_call = mod.get_global_var('func_5811')
func_5812_call = mutated_mod.get_global_var('func_5812')
call_8967 = relay.TupleGetItem(func_5811_call(), 0)
call_8968 = relay.TupleGetItem(func_5812_call(), 0)
func_2080_call = mod.get_global_var('func_2080')
func_2084_call = mutated_mod.get_global_var('func_2084')
var_8972 = relay.var("var_8972", dtype = "int8", shape = (4, 28))#candidate|8972|(4, 28)|var|int8
var_8973 = relay.var("var_8973", dtype = "int8", shape = (8, 140))#candidate|8973|(8, 140)|var|int8
call_8971 = relay.TupleGetItem(func_2080_call(relay.reshape(var_8972.astype('int8'), [112,]), relay.reshape(var_8973.astype('int8'), [1120,]), ), 4)
call_8974 = relay.TupleGetItem(func_2084_call(relay.reshape(var_8972.astype('int8'), [112,]), relay.reshape(var_8973.astype('int8'), [1120,]), ), 4)
func_8820_call = mod.get_global_var('func_8820')
func_8823_call = mutated_mod.get_global_var('func_8823')
const_8980 = relay.const([7.629436,-4.235141,-6.123572,2.464542,3.790078,1.947125,-8.629941,5.634857,-1.940620,-2.702688,5.686803,5.457835,-5.130850,-3.876008,-8.513343,6.311361,-5.940564,-7.265353,0.352911,3.238311,9.716033,-5.160440,-6.389291,4.581823,-8.161095,6.290687,2.969135,-2.617378,-4.956892,-0.016307,-4.693888,6.603591,3.363330,1.950704,9.916273,-6.019321,3.425098,-1.866040,-8.807887,-7.979471,2.652372,-4.203368,6.295448,2.107454,-9.630829,-1.420569,1.850616,9.900543,3.669742,1.377423,7.021877,6.101310,-9.046788,-0.516762,8.070065,2.547623,-1.138018,-9.403392,-8.434098,-2.890751,5.181944,2.232382,-4.294277,8.543595,-5.338491,-2.109014,-4.477936,-5.946694,2.430751,1.198090,-9.595204,-5.424069,1.774158,-3.516621,-8.030250,-2.928690,1.022928,-6.238820,-9.277159,3.059555,-0.892662,-7.754849,9.919201,-3.280668,8.106205,0.214083,-9.652366,-3.564416,-9.647672,-4.318640,6.604462,-6.847397,-3.576064,-9.595443,3.868983,0.679130,1.452736,-4.118053,3.980405,-4.196400,1.382843,-9.404905,8.343730,4.156161,9.502333,-0.728064,-5.911009,6.026013,4.706406,0.306909,5.010294,-5.017797,-3.610569,8.466308,8.832066,-7.880163,0.991293,6.323241,2.538192,8.588194,-3.420216,-1.834256,-2.967418,9.363823,2.789063,-5.661101,-5.756335,-0.875324,-4.875019,-1.452323,9.557100,-0.129559,7.872739,7.030851,-6.284726,6.426290,-2.834272,7.362747,1.642872,-7.054672,7.343705,9.033518,9.071151,-5.406974,1.772119,-0.643544,9.680184,1.404066,-0.153902,5.414458,9.154695,0.221980,-9.568307,7.658743,0.498979,0.035176,-3.285288,-8.494453,-5.044509,6.937660,1.461626,-3.321655,-7.837198,4.347148,-2.140433,2.157993,8.332618,3.144100,5.246337,7.279632,-7.641610,1.613279,7.527933,-0.734146,-0.334812,5.816882,6.793793,-9.335062,-0.908122,-1.559021,3.623854,-4.223378,-3.859186,-6.521812,-1.070714,3.144569,-8.878574,-9.563400,-3.700470,2.599286,-4.235501,8.801509,-1.679086,-0.545478,1.686859,9.429163,-9.234485,-6.974896,4.734942,4.964257,-5.163835,-1.662094,5.408903,5.928867,-6.008754,5.058221,8.218610,-3.504433,-3.239315,-9.393280,-8.671852,-3.692689,-4.511848,1.890469,-6.431298,3.520095,3.668450,8.282387,-9.841944,1.676289,-0.935956,-1.106260,9.387576,9.496589,6.051463,2.083651,-5.079471,-6.048307,-2.516114,-6.970788,-6.810188,-0.766790,-0.412695,4.092987,-5.248429,1.644756,8.759206,-8.877279,-6.925523,-3.334906,-9.303844,0.613867,-0.760248,0.798542,-6.007854,3.053007,1.044079,-1.414799,2.683605,0.180271,-6.049495,-8.769514,-8.749986,-4.653197,9.388264,-5.551258,3.966917,-5.765118,4.928445,-3.957493,5.117443,5.276928,2.917778,-0.181173,3.448821,-3.172498,-2.920945,5.310073,-5.189620,-7.976669,-1.124466,0.825879,-4.069363,9.916709,1.302454,5.320753,4.575933,9.580487,6.390755,-9.571624,9.292207,-3.039776,8.471399,-9.560790,-9.036244,6.009551,6.665145,-5.636206,-8.425467,-6.432138,2.661871,5.220610,-7.912965,-4.870962,-0.957398,-5.409858,5.424547,-5.874874,-4.653838,-4.290477,3.776150,4.220983,-6.500097,-0.027734,-4.409911,-1.878599,8.174762,-0.233552,4.392923,7.397366,3.667301,7.241919,-1.907675,-6.290455,5.409782,7.267678,-5.957206,9.712860,-5.397099,-7.438137,-3.478830,8.760096,-2.023030,5.664196,-3.108053,0.565763,-1.239035,-1.660320,-2.164321,4.016958,-0.422933,-4.766823,-4.707115,0.011538,-5.620852,0.801909,8.812393,-4.729676,-8.255690,1.517648,-4.506667,1.372388,8.071513,0.494680,-0.690386,6.560178,-8.198611,4.974474,-5.063819,2.572808,-4.242163,9.418869,4.032553,9.036344,-1.549503,-6.865565,-1.450999,9.582484,-8.930218,1.767200,-2.509599,3.535114,4.663263,4.604716,7.813017,-3.617908,5.148598,8.575443,3.375955,-2.641634,0.238989,-5.501613,-1.539291,-8.826294,-3.412372,4.005113,-7.272756,3.902821,-1.775745,6.278100,-3.187081,1.280266,-5.866518,-0.185996,-6.672414,4.669326,-3.481907,1.143919,3.569171,1.870349,0.089888,-0.608424,2.045686,4.954947,-4.285996,0.587100,-4.429401,-9.468794,-8.242502,-4.231845,-6.350217,-8.581908,8.879136,0.309634,0.718190,5.988155,-9.829001,0.362975,9.419359,8.745426,5.658465,-7.941542,7.728052,-9.676056,-5.616458,-8.218314,-7.675230,6.557991,-7.233631,3.864389,2.916608,9.786861,-6.804402,6.988749,0.878909,-1.372787,3.274579,8.743760,1.745845,-9.172058,-9.002926,-3.182719,-1.403731,9.852844,8.617943,-9.733533,6.014592,-3.513464,-9.900740,8.754241,-8.775742,6.449598,5.133889,-9.860291,-8.163158,-4.154364,-9.450180,-6.809158,-0.346461,9.791100,-0.842380,-5.719544,5.303059,2.743083,-4.937004,-1.362393,-1.530676,-9.654459,-6.421615,6.333264,-0.665776,1.140879,-3.303317,9.054184,4.797204,-9.904383,-4.713321,0.833964,9.061598,-8.756022,-4.612197,-1.683651,-4.157803,-6.387135,-9.813633,4.996494,0.709240,2.955769,-0.896380,-3.531089,5.753112,3.838908,2.524677,-1.427768,-9.091862,-5.133806,1.856289,9.001073,2.165559,-1.633121,6.204745,-5.373544,-6.275240,2.418865,-5.308652,4.397314,-0.287717,-9.218664,6.010064,5.892490,1.081924,-7.306432,-5.072170,-0.187899,1.117381,8.827146,-1.980326,1.147809,0.379681,-1.783537,-1.406105,-7.681917,-0.043863,-8.979591,6.532753,6.906901,1.848215,0.162640,-5.849633,-8.277887,-1.069716,-9.781147,6.092976,7.345165,-6.097499,0.649509,1.380463,-1.130008,-5.540175,-6.735950,-2.999432,-2.760855,7.156135,0.120694,0.102643,-1.572491,-2.309145,-2.492527,-2.510515,-1.848557,3.209441,-7.782248,6.841828,9.147007,4.062201,3.909800,4.962495,-9.577176,0.905127,-4.744514,6.232485,-6.663525,-6.287695,4.952446,2.141369,9.617230,5.498074,4.645658,-2.654875,-9.812601,-8.962540,9.326852,4.814454,3.378684,-8.743447,5.896312,-7.343525,8.484478,2.030710,7.049892,-2.338887,3.331043,-9.162775,7.481517,2.265184,7.819790,0.816199,-3.186275,-2.513341,-8.247770,3.890871,-8.661000,8.614170,-4.178275,-2.414570,8.457783,1.622411,1.112847,-8.364202,-3.869562,-5.525272,9.053538,3.640975,9.024675,6.511296,-9.571331,4.456377,-9.845838,-2.758562,3.497360,0.548425,6.060238,-9.127532,-8.821433,7.052207,-8.496001,-1.456916,-9.935775,9.600182,7.127151,8.234889,-8.476956,-7.331046,2.363697,8.840582,-3.401471,-1.212212,6.131641,-8.374307,5.966505,5.899294,8.421747,3.637926,4.537209,9.865032,-2.409047,-1.592214,-9.830728,4.073937,7.342897,-1.738936,1.388357,2.546884,6.020954,0.972634,-8.127544,6.048157,-6.336999,0.081110,3.190748,5.254523,5.200216,-5.478349,-8.191682,6.996968,7.630615,3.450225,-2.438062,3.645866,-3.612228,-3.255427,3.882326,5.107982,5.368555,7.100976,8.341125,-1.240633,-2.376228,-0.693486,-2.287303,-9.398625,-2.433566,9.320137,4.576905,-0.916056,7.068667,-1.284683,-1.893791,-0.904080,-2.602027,6.334168,-9.669121,-2.068872,-4.528300,-9.493152,-9.747141,-3.053148,-3.268418,-1.658443,3.339005,-1.249129,1.916929,3.585096,-0.135633,5.994342,-8.984461,-5.581882,-5.115537,0.479506,-4.338702,-1.992733,7.434162,1.166822,-6.414346,1.450899,-2.738053,-1.912114,-6.367913,-6.318755,4.871351,1.263696,-0.285688,6.809141,-5.713130,8.056923,-6.362738,3.986269,7.207543,2.525099,-8.934138,9.817230,-0.014889,7.376255,1.136056,5.687190,6.577926,-0.409202,1.241765,6.017104,0.776033,-0.453925,-5.867091,8.619716,-8.930913,8.072900,1.853648,0.599768,-7.894355,-3.567009,-7.593812,-3.899093,-3.819149,2.661808,-2.999316,4.016145,-1.030650,7.784337,4.349311,-9.410607,-8.385322,8.254470,-7.445024,2.971262,3.884754,-9.209937,-4.197512,1.953244,-3.461749,-3.056319,9.251580,-3.490552,6.139154,-5.802221,-9.722084,-7.177322,-4.822580,-8.786581,-0.933606,3.686319,9.911903,-4.253747,3.741400,-2.895758,-6.807236,-8.738981,-8.044035,8.764778,7.705644,-3.470470,-2.351845,-9.184312,-5.217395,8.940803,-7.939689,-6.931720,4.849430,1.550465,5.032249,-1.775180,-9.482322], dtype = "float64")#candidate|8980|(780,)|const|float64
call_8979 = relay.TupleGetItem(func_8820_call(relay.reshape(const_8980.astype('float64'), [780,])), 3)
call_8981 = relay.TupleGetItem(func_8823_call(relay.reshape(const_8980.astype('float64'), [780,])), 3)
func_7212_call = mod.get_global_var('func_7212')
func_7214_call = mutated_mod.get_global_var('func_7214')
call_8988 = relay.TupleGetItem(func_7212_call(), 0)
call_8989 = relay.TupleGetItem(func_7214_call(), 0)
output = relay.Tuple([call_8967,call_8971,var_8972,var_8973,call_8979,const_8980,call_8988,])
output2 = relay.Tuple([call_8968,call_8974,var_8972,var_8973,call_8981,const_8980,call_8989,])
func_8994 = relay.Function([var_8972,var_8973,], output)
mod['func_8994'] = func_8994
mod = relay.transform.InferType()(mod)
mutated_mod['func_8994'] = func_8994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8994_call = mutated_mod.get_global_var('func_8994')
var_8996 = relay.var("var_8996", dtype = "int8", shape = (4, 28))#candidate|8996|(4, 28)|var|int8
var_8997 = relay.var("var_8997", dtype = "int8", shape = (8, 140))#candidate|8997|(8, 140)|var|int8
call_8995 = func_8994_call(var_8996,var_8997,)
output = call_8995
func_8998 = relay.Function([var_8996,var_8997,], output)
mutated_mod['func_8998'] = func_8998
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3571_call = mod.get_global_var('func_3571')
func_3572_call = mutated_mod.get_global_var('func_3572')
call_9015 = relay.TupleGetItem(func_3571_call(), 3)
call_9016 = relay.TupleGetItem(func_3572_call(), 3)
func_6670_call = mod.get_global_var('func_6670')
func_6671_call = mutated_mod.get_global_var('func_6671')
call_9023 = func_6670_call()
call_9024 = func_6670_call()
output = relay.Tuple([call_9015,call_9023,])
output2 = relay.Tuple([call_9016,call_9024,])
func_9029 = relay.Function([], output)
mod['func_9029'] = func_9029
mod = relay.transform.InferType()(mod)
mutated_mod['func_9029'] = func_9029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9029_call = mutated_mod.get_global_var('func_9029')
call_9030 = func_9029_call()
output = call_9030
func_9031 = relay.Function([], output)
mutated_mod['func_9031'] = func_9031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4180_call = mod.get_global_var('func_4180')
func_4181_call = mutated_mod.get_global_var('func_4181')
call_9043 = relay.TupleGetItem(func_4180_call(), 1)
call_9044 = relay.TupleGetItem(func_4181_call(), 1)
uop_9048 = relay.sqrt(call_9043.astype('float64')) # shape=(6, 13, 4)
uop_9050 = relay.sqrt(call_9044.astype('float64')) # shape=(6, 13, 4)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_9058 = relay.TupleGetItem(func_2587_call(), 1)
call_9059 = relay.TupleGetItem(func_2588_call(), 1)
output = relay.Tuple([uop_9048,call_9058,])
output2 = relay.Tuple([uop_9050,call_9059,])
func_9060 = relay.Function([], output)
mod['func_9060'] = func_9060
mod = relay.transform.InferType()(mod)
output = func_9060()
func_9061 = relay.Function([], output)
mutated_mod['func_9061'] = func_9061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4966_call = mod.get_global_var('func_4966')
func_4968_call = mutated_mod.get_global_var('func_4968')
call_9076 = relay.TupleGetItem(func_4966_call(), 0)
call_9077 = relay.TupleGetItem(func_4968_call(), 0)
output = call_9076
output2 = call_9077
func_9097 = relay.Function([], output)
mod['func_9097'] = func_9097
mod = relay.transform.InferType()(mod)
mutated_mod['func_9097'] = func_9097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9097_call = mutated_mod.get_global_var('func_9097')
call_9098 = func_9097_call()
output = call_9098
func_9099 = relay.Function([], output)
mutated_mod['func_9099'] = func_9099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5533_call = mod.get_global_var('func_5533')
func_5535_call = mutated_mod.get_global_var('func_5535')
call_9146 = relay.TupleGetItem(func_5533_call(), 0)
call_9147 = relay.TupleGetItem(func_5535_call(), 0)
output = call_9146
output2 = call_9147
func_9156 = relay.Function([], output)
mod['func_9156'] = func_9156
mod = relay.transform.InferType()(mod)
mutated_mod['func_9156'] = func_9156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9156_call = mutated_mod.get_global_var('func_9156')
call_9157 = func_9156_call()
output = call_9157
func_9158 = relay.Function([], output)
mutated_mod['func_9158'] = func_9158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_9173 = relay.TupleGetItem(func_2937_call(), 0)
call_9174 = relay.TupleGetItem(func_2939_call(), 0)
output = call_9173
output2 = call_9174
func_9175 = relay.Function([], output)
mod['func_9175'] = func_9175
mod = relay.transform.InferType()(mod)
mutated_mod['func_9175'] = func_9175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9175_call = mutated_mod.get_global_var('func_9175')
call_9176 = func_9175_call()
output = call_9176
func_9177 = relay.Function([], output)
mutated_mod['func_9177'] = func_9177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5063_call = mod.get_global_var('func_5063')
func_5064_call = mutated_mod.get_global_var('func_5064')
call_9250 = relay.TupleGetItem(func_5063_call(), 0)
call_9251 = relay.TupleGetItem(func_5064_call(), 0)
output = call_9250
output2 = call_9251
func_9265 = relay.Function([], output)
mod['func_9265'] = func_9265
mod = relay.transform.InferType()(mod)
mutated_mod['func_9265'] = func_9265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9265_call = mutated_mod.get_global_var('func_9265')
call_9266 = func_9265_call()
output = call_9266
func_9267 = relay.Function([], output)
mutated_mod['func_9267'] = func_9267
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9285 = relay.const([[[1.313582,9.525302,5.821635,1.600037,-2.165279,6.262005,-7.554649,0.200810,-3.210081,-1.646092,-6.611454,7.498070,2.985664,2.705825,4.975805,-6.053649],[2.565465,1.185876,8.814432,9.368321,-7.225375,6.459049,-3.075970,5.070494,-9.127091,7.272923,-2.386452,-4.037238,3.377275,1.832962,-1.575676,5.755272],[9.002933,-4.052578,-7.197162,5.143018,-1.332146,4.110383,1.998198,1.629316,-7.035965,-4.304647,1.305355,2.785547,-5.810064,-3.562727,-4.999310,-2.562721],[-2.974685,-3.734757,9.621565,1.583498,0.792793,-3.796281,3.154830,-2.869386,-7.397584,-0.648741,2.193510,-7.330424,1.565520,-2.916274,6.272536,5.599204],[4.269433,-4.115702,6.244244,-5.942444,-6.356306,4.848911,7.721401,-6.253290,-3.025206,6.563616,-3.848437,6.367325,-2.417918,0.247424,7.192266,7.728069],[1.922576,6.166449,7.641717,5.441696,-5.553578,3.903587,-7.292365,3.266615,6.746570,1.257028,-6.633744,0.269115,-3.067198,-9.684138,0.761757,6.218625],[3.998790,-1.028072,-3.466395,2.793895,-4.122073,-6.259580,-3.246036,-6.796091,1.905218,5.337343,-8.982410,-8.802905,9.339290,-2.767807,4.760254,9.202525],[-7.980028,4.934977,8.444483,5.486257,-6.040317,8.076434,0.906404,-5.247186,8.511270,3.124291,-8.019347,-6.429293,-2.784065,-1.571446,-2.015879,6.651883],[9.575914,-5.956089,5.571362,2.438013,0.413541,-9.507071,-2.370926,8.468756,-1.090145,1.772884,1.604175,-5.837212,2.373684,3.785884,2.566588,-6.296291],[6.500522,7.709891,3.306236,-9.792547,9.007229,0.810813,3.628774,0.396338,8.112732,-6.512688,4.712801,2.022903,-1.658036,-3.826366,0.561529,-9.568722],[1.545181,6.013933,-4.562297,-5.944186,-4.857889,0.280739,-2.667632,4.815981,-2.664773,-1.080833,-3.556392,-2.611170,-4.750961,-8.267942,4.209865,5.462668]],[[8.499123,2.594329,-6.168583,8.003919,-3.013611,7.137320,-6.415171,-7.578129,-3.404883,-6.216558,-1.152827,6.002762,5.836739,-9.417684,6.262057,-6.037337],[-0.850978,-6.298808,3.126884,5.403353,6.498198,-8.119725,8.276310,-0.891849,-8.109100,8.245428,4.456036,2.601008,-0.980857,2.057223,9.935097,-5.230704],[-9.034696,9.269102,9.666156,0.493120,6.308142,-3.495260,-3.253274,-3.074497,8.625064,-0.616712,1.206271,4.866111,9.593575,5.886994,-7.981377,6.776373],[-1.329431,-1.076131,2.870250,-6.905688,-0.800382,-4.767660,3.674370,0.396402,-9.170676,7.837214,1.704222,3.834320,-3.500586,-7.780880,2.833236,7.206010],[-7.461942,9.987984,5.743052,-8.413417,-7.183821,-8.356010,7.584437,-6.364423,4.678081,4.326233,-2.216501,-1.741586,2.903193,-2.471946,-9.845635,9.768698],[5.973286,-1.399433,-5.886454,-1.896249,1.398408,4.585653,-8.673096,-1.714457,7.625185,5.672214,3.460660,-0.482448,-8.473540,2.197280,-7.387613,9.711630],[9.936769,-0.294077,-6.923304,-4.215408,-0.862487,-4.724318,9.083300,-9.835446,8.106391,-1.281763,3.212289,7.731821,2.653194,-7.801193,4.556558,-1.968000],[-1.849353,4.718262,3.605530,-3.789719,0.892453,5.271469,-4.674250,4.862689,4.010064,-3.957516,3.299421,-5.064036,-4.366117,-5.351024,-1.335968,-8.825129],[-0.208432,4.625477,7.180741,1.001511,-5.388476,7.838781,-8.296304,-1.057582,-3.598147,6.765069,7.116129,1.954147,-6.839765,3.971417,-9.431413,9.853835],[9.420427,-8.821860,5.576837,8.701323,-7.173351,-2.203498,-1.540179,-3.037394,5.992845,-6.975602,5.294582,-4.208265,4.189170,-5.433777,7.483523,-9.407334],[-9.703710,9.362766,-1.225689,-5.181675,2.350510,-7.078708,7.130693,-0.696353,-6.056484,8.093648,-5.481009,4.095192,-4.534941,9.667485,-5.738483,-2.262704]],[[1.250835,-3.727559,1.550146,-6.028804,9.536053,-3.499169,-3.984065,1.966079,1.980015,-1.933464,-5.321186,8.933528,-9.435481,-5.773182,4.670071,2.448322],[-2.435250,-5.580989,-9.718457,-1.856468,3.338001,1.324499,5.039081,-3.701731,3.211254,6.254202,6.055403,-4.705846,0.124395,-5.396546,-4.517683,9.982780],[9.807171,-0.853542,7.027993,7.254499,2.324486,-4.122785,5.551574,2.193883,5.191844,-7.346468,2.299524,-0.108682,6.668626,4.130537,1.848481,-2.051840],[5.023712,-2.349424,4.712912,2.408478,-3.901477,6.271718,5.675567,9.680091,8.758465,0.208024,-0.075097,-9.732129,-0.260460,9.667185,-6.978392,-6.317156],[-6.799107,-7.447884,-7.319396,-2.937438,4.450554,-4.251861,-5.339817,-2.784989,3.033130,6.227337,9.313479,8.333765,0.535313,3.989033,-5.838625,8.770790],[1.872962,-2.504338,-2.323883,-8.013209,-1.452278,-3.413204,-4.443842,6.280466,-0.723929,-7.898753,-6.841059,1.291338,-3.896888,5.760665,-4.247775,-5.780825],[9.527520,6.698043,2.028700,1.179936,-3.200617,4.627678,-8.996817,-2.986224,3.983494,3.229170,-2.070426,0.528270,7.805728,2.849849,-9.077784,1.364439],[-2.175113,3.986804,1.171735,7.262998,-1.891859,-4.950102,8.881030,7.313268,9.005860,-7.847180,4.973713,1.383697,1.879692,-0.243547,-7.143786,3.614653],[-6.663579,-8.242137,1.697183,6.105220,-3.302330,5.821377,-9.519200,-6.188104,2.851960,7.557375,1.232046,8.969638,8.310034,-3.723087,-5.605328,-5.139701],[-4.085379,-2.262315,-4.839509,4.748746,0.073601,7.358918,8.476289,-2.868574,-9.094664,6.807367,-6.341765,-9.016227,-5.976929,5.501784,-9.697120,4.911545],[-4.748537,5.120906,7.105031,-5.354660,2.946613,-9.281627,9.873628,8.268535,-3.765372,0.944733,4.605868,-8.099793,-8.357167,-6.121915,6.272124,6.352458]],[[3.418609,-4.594337,3.082302,-4.868275,-6.386609,4.979284,4.185610,-0.332134,4.387856,-7.188133,5.103080,-1.766480,-4.611376,4.075229,-7.603221,8.349061],[1.509482,-3.337086,-9.416892,7.187158,7.227126,4.618679,7.882284,-1.090302,9.352887,7.167032,9.801897,4.584898,2.840648,9.729388,2.855426,5.829703],[6.507713,-2.518182,-0.131292,-3.370599,-1.761920,-3.317045,8.387077,8.795794,1.730522,-0.271048,-4.388154,-7.923723,-9.049990,-5.717916,2.983951,-1.688538],[2.464739,-5.595331,-5.856949,-7.042976,-2.250673,-8.520335,6.567169,2.561348,-7.569829,-8.229914,3.813056,-8.298034,-7.950333,3.469746,2.843810,-2.454922],[-2.006323,-3.463086,-1.370882,-9.129710,-2.318533,-2.051931,-8.849834,-3.963155,6.336117,0.587910,-6.449174,-1.602638,-0.124160,-9.076913,0.497782,1.867608],[6.452750,-6.329235,-4.592425,4.047205,4.620187,-7.590131,3.626194,9.728277,0.854033,0.282354,-4.690113,3.262141,7.469751,-4.091220,-3.251335,5.745931],[-3.502181,0.348533,-1.297524,4.250399,9.846697,9.914635,-2.578504,9.094429,1.951531,9.774409,5.650878,1.338180,-4.377417,6.239869,0.995650,0.089960],[9.515817,-1.072553,3.531701,2.715010,8.015957,6.466946,3.337287,-8.274461,4.301505,1.699850,-2.097422,1.645451,-3.034561,9.707518,0.814001,8.034245],[-0.676103,-2.615792,8.844856,-8.051810,-9.737577,7.150661,-7.109849,5.808014,5.814391,-9.856505,0.748436,9.677616,6.866560,2.588060,8.960512,9.686000],[-8.922502,7.951147,3.919902,-9.908927,0.734254,-5.229845,5.771566,0.423570,-0.797635,-8.221288,1.936230,0.325847,8.180870,-2.437559,-2.307714,-8.239829],[5.953018,-1.585269,3.338519,3.384646,-8.922284,-8.179585,7.213829,4.593740,-0.373325,0.696107,3.064573,-6.042151,4.797085,1.723882,-8.607006,-4.042600]],[[1.501361,-0.409837,2.015209,6.103146,8.989666,-4.933921,0.551831,-3.582666,7.730249,7.005686,1.311185,2.386668,-6.868297,-1.389087,-7.943596,4.377639],[0.324211,-9.579231,8.942504,6.968791,-8.470905,2.844888,1.435391,3.382862,9.402719,4.895961,-2.191813,1.301035,3.347458,8.440932,-9.287948,0.791398],[-9.314181,-5.057207,9.095530,2.679435,9.608319,9.740525,-3.118841,-8.784392,9.229296,-0.711313,-1.912654,7.964454,7.411406,-8.757795,2.192869,-3.908383],[2.471669,3.514274,-5.794093,-2.149779,6.850354,-1.681056,-3.906588,5.537591,-2.580944,6.797861,4.530642,-4.065794,2.276326,-9.871919,-7.306847,7.911458],[2.386241,-2.726767,3.140347,-6.437782,-0.377084,-2.218264,5.684502,-8.017469,-8.051637,-6.948609,-3.714206,-5.482312,5.440740,-6.635537,3.205970,-6.349258],[-7.455879,-1.700011,7.470535,-0.112139,1.487235,0.226893,-8.282351,-8.685718,2.435314,-4.766612,1.396004,-1.750885,1.462655,-0.968328,-1.367448,-7.898714],[4.913693,-0.061420,9.957015,-1.294633,4.792214,1.990177,-4.029829,-6.626680,-2.662904,6.247600,-1.568848,8.841399,6.181308,-4.536714,-5.218076,-8.260923],[-5.083326,-0.404807,-2.429562,-2.170948,-8.637657,5.075998,-0.111451,7.769501,0.542838,-8.389168,-9.404663,7.949961,-9.200160,0.380646,-4.096945,-3.548823],[-1.768176,-6.073676,-2.578117,-3.130418,-0.860687,6.170544,-7.894865,-3.412105,5.681697,6.583257,-6.406429,3.707127,-9.176466,8.282303,3.317887,4.866821],[-2.414923,-8.672925,7.747903,-9.793918,-7.130540,-4.285326,-3.647572,-2.341678,6.065023,8.577271,9.319832,-7.036477,2.061775,-5.100574,-5.922144,-0.965738],[-2.731238,9.496824,4.743486,5.683366,3.382023,-3.532595,-9.758858,2.249230,-9.316383,8.161957,-8.180206,-4.886802,5.430038,-8.860794,-2.272316,6.523680]],[[4.181303,-1.210163,-9.746702,-1.043931,8.038243,7.071588,-6.032413,-3.614499,4.346770,-2.532405,9.581830,2.035780,3.000694,-9.737766,-5.917520,-1.138040],[-3.479904,-5.911309,1.748479,-8.248046,-8.113453,-9.538064,4.621935,0.889468,3.135014,-1.502986,-3.567347,2.304307,5.939645,-6.059574,1.796780,9.485103],[9.241864,-1.337761,-4.828174,-9.960950,-7.898773,1.362959,0.277147,-5.088164,-0.256681,8.919554,-3.809488,7.612069,4.014538,5.391336,-4.700015,-1.953099],[7.704773,-1.088208,-5.469316,-2.295084,-4.952124,-9.499187,-8.836378,-4.038816,4.778320,-5.658275,-4.752977,6.990769,7.313820,8.670196,4.269840,9.090076],[-6.514395,-6.821747,-3.332353,-5.173979,4.407704,-1.836982,3.352570,-1.915985,6.950382,7.986463,-7.530393,2.824752,2.385730,-6.041793,-4.930449,9.924633],[6.478425,7.399688,-3.685574,-3.176052,-4.386737,-0.728272,3.653988,-8.538558,0.355897,5.686397,-4.161809,6.110542,9.083885,-4.190842,4.811017,-1.837084],[-0.679497,4.746981,1.138116,-7.349147,-2.441253,-2.080571,4.541628,-7.601846,-9.269676,9.228698,-1.963630,-0.697975,-7.073607,-7.618384,7.798350,-6.168988],[-1.307793,-1.889164,-3.558088,-2.468899,1.642321,-5.368484,9.130059,3.813440,-1.727643,0.029193,2.497581,-0.836480,-4.311998,-5.144200,-2.103117,1.081648],[-0.780911,-2.488406,-7.828341,4.798555,1.290963,2.465406,1.716038,-3.460903,1.468567,-7.579480,-9.935686,-6.660825,1.142008,-9.355363,5.704688,9.552956],[3.665942,-2.492703,-3.799234,-8.061730,-6.057773,-5.068449,-9.444703,6.453446,-8.044617,5.977704,2.857199,-3.473934,-5.811862,-7.047449,-9.204800,8.991723],[2.478517,-6.181411,9.338746,-1.922304,-7.582995,6.859867,6.310245,-3.202227,2.061506,-5.330741,7.240968,6.569746,8.794883,5.825133,2.438760,-3.734215]],[[0.236289,-0.809491,4.219943,-8.483097,-2.630712,-5.508653,-5.547801,4.583819,-5.529610,-7.778949,-9.551355,0.778650,9.239551,-8.348347,5.595959,-7.374520],[3.594313,-9.489705,2.852186,-9.775211,-2.353446,1.819768,4.052560,-7.261317,2.050627,6.446011,5.385896,4.756697,5.561313,3.105407,-3.023789,3.773927],[7.605482,-0.434623,-1.159071,-3.768197,-8.218503,-6.585459,-1.852775,6.256344,9.933637,-3.609170,-4.443517,-4.396668,2.632277,-5.184149,9.799476,0.883853],[8.288928,4.736002,-8.544909,9.024995,8.657895,-0.044210,-0.120604,8.322545,-2.126572,-8.172675,-8.984931,-1.326272,5.569630,6.056805,9.970191,3.731729],[0.233744,-1.287756,-4.489563,-3.327190,9.796959,9.941198,-5.556837,-3.467769,-5.010885,8.253510,6.617091,-0.592684,6.891589,5.838378,-9.389330,8.470006],[3.748306,0.549226,6.589871,8.503693,-7.012639,8.712505,-2.279927,0.537504,-9.484352,5.340552,9.794034,-3.744847,2.979414,1.328030,-2.291847,1.619782],[-1.516298,8.833061,-9.892668,7.686315,-2.845066,-6.554630,-0.021531,6.738712,-2.659813,-2.614435,3.014865,-3.364163,-7.616365,-2.191181,1.153195,-1.398252],[9.030153,9.953488,-8.456712,-7.628316,0.681152,9.304852,0.534052,6.651385,3.382670,4.887194,-7.538610,-8.328862,2.992676,-6.176106,-3.459445,-2.381039],[-5.445598,-4.226415,-0.730552,1.736060,2.289135,7.664350,-7.939376,-7.585667,-3.029768,-3.521159,-5.668961,2.412792,5.390001,-8.413184,-8.340676,9.800711],[-9.424561,-9.848590,1.358413,5.580213,-3.634686,5.443863,4.131126,5.164553,0.437445,-5.724546,-6.513678,0.484257,4.232786,3.836345,-1.029949,8.268813],[-9.612927,-1.207840,0.106139,-8.322352,-1.450237,-2.333713,-0.580151,-1.100162,2.650304,2.542275,-6.992763,-1.902055,-1.834420,-4.488578,-8.675770,6.448570]],[[5.048608,-1.517978,1.047200,-8.358843,-1.089443,4.866678,-6.419723,-0.009517,8.219737,4.978756,-1.254291,8.915579,-4.814904,-3.106535,3.842468,8.083845],[1.232840,-9.539161,3.910939,-0.540363,6.132082,-9.026051,0.107316,-6.870474,-7.404404,3.766293,1.020220,8.678585,-7.642636,-7.501483,6.553777,-7.471580],[-5.656859,-9.071600,9.069098,0.484988,-2.002677,4.380519,8.708618,-0.971049,4.760461,-3.870192,0.837142,-9.419007,9.220531,2.986988,2.582927,5.710092],[-1.619824,1.909581,6.133694,9.110741,-6.840037,0.729017,-8.612660,7.431054,4.208227,-0.871232,0.836698,-9.574180,3.933300,9.294560,9.030205,-7.309855],[-6.112123,-9.096621,0.903456,-9.895634,-1.022373,4.228751,5.250647,-8.478763,-9.618040,1.052303,-6.549211,3.223882,-7.317510,-4.138232,8.257542,2.185766],[-0.671010,7.588192,9.772039,4.385203,-9.193841,-5.984736,2.253557,-8.652713,8.875622,3.493649,-4.522373,-6.600309,4.748018,-2.272398,6.849474,5.378275],[8.435196,0.481197,-8.557956,-5.778565,5.333646,-4.432049,-7.849796,5.803059,9.845349,9.000975,7.919148,-4.956160,-1.363394,0.109914,-1.305406,7.887625],[-0.521613,4.507863,7.622062,3.693770,-3.191505,8.714027,-3.970496,1.144595,0.044196,1.835099,-2.326398,4.541509,6.523812,-4.003090,8.730098,0.018017],[1.305050,-4.318991,9.976927,0.816646,-6.562344,-1.351409,8.756972,-3.669641,-9.771245,2.742089,5.191991,4.591599,-2.042224,-7.383047,3.401734,6.406333],[-5.500356,7.008607,8.397864,-4.546292,0.429576,-9.179525,-1.424549,3.157314,2.493243,8.210329,3.064787,4.260861,-0.466723,-1.307344,8.294855,-5.222971],[3.053566,3.503046,7.109272,-3.437051,-0.793430,2.065369,2.187852,6.829160,-7.420768,2.732910,1.850654,9.270853,9.617086,2.872080,8.616055,-2.258726]],[[4.398906,8.018595,5.769554,3.146706,-8.349808,-9.731508,8.786294,-5.065209,-4.530145,-8.416283,-7.835918,-7.436502,0.278871,0.186207,2.022564,1.240443],[4.472174,8.178083,4.040020,5.689009,-9.701453,3.082299,1.195247,1.951496,-6.048522,-9.531042,0.300992,-3.752763,-1.898561,3.824080,5.278187,6.605050],[1.144002,-8.556233,3.622005,-7.970762,0.785432,-1.602708,-0.363341,4.216335,2.617781,6.844888,-8.797935,7.185036,3.125978,-1.878102,9.091827,-3.040054],[1.130305,7.647792,-9.254013,-9.375443,-2.365605,-2.401476,-6.960551,2.116325,9.757379,-4.935660,-8.535948,6.884387,-3.911291,-1.336228,6.390863,-9.923413],[7.284345,0.802778,8.602459,-3.294261,-8.855891,-4.095167,-4.181759,-1.426663,6.744045,2.102197,-6.718963,4.808304,-7.637727,4.520499,-8.864949,-7.799073],[4.251165,4.587458,2.038225,-9.250664,1.128344,-3.957678,-7.533200,8.356796,1.146355,6.973135,1.321697,-1.927036,7.892079,6.462206,2.474974,4.122930],[-9.473280,-6.223077,-7.986910,3.233634,3.786420,2.790490,2.736060,7.257098,0.112634,-8.668991,-5.613629,5.371730,-2.429805,0.959048,-7.556818,0.392214],[-1.693028,2.692806,-7.144071,-2.227056,-5.688946,-3.324593,-6.493541,0.426386,-1.207913,0.081856,-3.467449,-0.549357,3.086472,0.521193,4.006574,-5.629211],[-9.636379,-3.747273,7.296174,-8.283092,4.171745,9.359965,7.517906,0.835148,-2.457322,-2.228604,3.756702,-3.429385,-4.140261,7.273475,-3.089599,4.039756],[1.128937,9.432329,-2.213162,-7.065388,-4.735348,-4.579012,-5.417697,-1.791983,-0.797174,-9.307019,4.105387,-6.250470,-7.908534,3.354687,-9.995114,1.660860],[6.234910,-1.948767,-8.704546,7.540404,-0.460923,-6.425293,0.735407,9.031456,6.224259,-1.157185,-6.006533,8.912278,-8.149444,3.601432,4.525533,-7.389871]],[[-1.518532,1.631715,8.092658,1.722600,-7.189307,0.614440,-4.039262,8.884213,-7.655156,9.281748,-9.097657,8.163974,6.868705,4.886497,1.113566,1.267010],[-7.487367,-7.575248,5.448192,4.547410,-0.438799,-6.126255,-9.024878,-0.624136,7.781960,3.488273,-9.111374,-3.017828,-5.307977,0.753679,6.042355,7.179644],[4.477374,1.380046,1.830034,-9.769533,4.958422,3.196154,-8.584409,-8.138892,7.864200,7.443143,-8.975346,1.223379,-8.488035,-8.326150,-0.097278,3.456334],[-6.213416,-7.866632,-6.742975,9.918452,3.859419,4.738773,-9.721888,2.857700,2.228737,-3.468031,-8.110792,-2.696011,-4.334174,-2.661428,-2.049271,-8.604808],[0.384331,3.987231,3.001744,5.833397,0.190987,-8.723598,2.258655,8.252769,-7.402123,-7.061311,6.884839,2.786510,-5.943383,-8.664265,-2.823429,7.437884],[-0.269974,2.986703,7.828533,-6.053087,7.721714,-0.321223,6.825938,9.809812,2.898543,-1.553756,9.222735,-1.565513,-9.824837,-9.855345,8.560976,-1.361396],[-8.091196,7.642663,-8.976516,-8.029370,-5.234000,-0.596907,-6.388536,-9.434458,-9.284436,4.462598,-2.701072,2.371519,-1.937053,2.304084,2.871133,9.052185],[6.826585,1.377303,4.903442,3.970547,-4.601081,9.661465,-5.481993,8.067003,-7.683389,-8.456920,-3.136742,1.655733,6.187930,1.083719,-6.170794,4.797202],[8.440365,-5.353421,-0.064511,3.508518,0.728360,-7.843377,-4.031365,-8.555436,-3.023087,4.764449,-9.072681,9.115977,-0.602953,-9.473310,-1.475114,-2.091681],[-1.349082,-6.667292,0.502484,-1.762957,-5.062294,-2.774799,-1.837702,0.808585,7.873426,3.205978,-1.728359,9.187710,4.743463,2.905478,9.239564,-1.184555],[-3.352040,4.933684,-6.335815,6.381012,-5.416806,7.152795,-9.168220,0.576000,8.476404,-9.146506,0.418808,-5.073386,2.974178,-2.727589,-4.082310,4.915845]]], dtype = "float32")#candidate|9285|(10, 11, 16)|const|float32
const_9286 = relay.const([[[-9.919327,-9.853771,-1.488797,4.822565,9.582487,4.827171,8.894799,8.324104,-1.003242,3.913875,-0.119744,-4.495273,-3.914298,1.327453,-5.283171,-0.741821],[-2.614250,-3.360693,9.917038,-6.830622,4.493139,4.232545,-3.128255,-8.826365,5.765825,-2.730960,1.762480,1.979135,2.868223,3.921355,4.982037,-1.474031],[-0.822860,3.706450,-4.497662,-4.330113,2.396447,-9.550881,-3.628227,-7.006281,-0.798363,0.664985,4.203456,3.589900,1.272652,-4.714497,-1.787547,-0.434174],[2.703109,-6.606987,9.248152,-7.557461,-5.186861,7.753177,6.276027,1.997829,-5.801977,0.570801,1.006863,-9.373700,9.445092,1.235680,6.990921,-1.141453],[7.730350,-2.481739,0.750261,3.744427,7.926543,7.888792,-6.459744,-8.054971,6.755364,5.706589,0.650885,-6.624167,-4.990418,-7.447452,7.641486,0.270988],[-0.407336,-2.801849,-1.059209,5.273311,-5.604187,-8.558087,4.106307,0.897832,2.992290,9.064814,-2.166866,3.231952,-3.123801,-6.116254,2.827973,-1.578698],[6.113948,9.309021,4.805388,1.828009,4.889090,-1.625988,-6.937512,-3.240702,-0.681270,-3.487887,8.512501,-9.593301,-1.682641,7.520945,-5.049137,6.334934],[-6.055995,1.516240,1.386495,7.613301,-2.671131,-0.958250,1.234561,-6.339243,-8.493552,-9.054893,2.741908,5.930745,8.711319,0.729105,5.817038,5.336066],[8.707523,3.152397,9.520817,-5.521551,-7.160212,6.723529,1.420579,-4.098794,-8.765352,5.357892,3.337608,8.700630,9.222091,-2.555129,8.339138,1.700095],[-7.813114,-5.323069,9.591712,6.617696,9.870885,-6.538417,6.949022,-4.216096,4.019673,7.370674,5.213156,-3.132374,9.032489,4.924830,-2.824980,0.101082],[0.472355,3.395213,-9.299813,-5.917086,3.784341,-6.506757,2.519768,-2.877366,-5.295319,8.767442,6.970372,6.365765,-7.569355,3.363280,7.794642,5.471315]],[[-1.266024,5.424303,-3.250231,-2.663111,-3.063854,-7.132000,-4.420162,0.835121,-2.322199,-0.124948,-4.687494,-7.742289,-5.895808,3.831292,-9.946043,-9.397424],[3.754637,-7.726971,0.370842,0.502692,3.690927,-8.551035,8.688873,4.107301,-5.640731,3.273953,9.122398,-9.268036,9.586479,2.651751,-9.653371,8.112999],[5.585329,4.779483,-1.832335,7.960020,-3.455201,0.473431,7.086061,3.389506,-0.652698,-3.830519,-3.184567,5.300276,-6.389707,-9.509921,-9.994985,8.972459],[6.528186,4.074606,8.060527,7.740082,-0.741416,9.332006,1.245272,1.555358,6.217956,3.118309,-2.119635,-2.443594,2.145900,-7.440398,-9.996968,-6.061710],[-6.991339,5.044846,-6.674949,-7.659352,-0.307559,-9.775687,-0.407411,5.208738,3.091518,-3.490485,-3.858058,-3.152509,9.287980,9.632450,-7.980861,5.358422],[1.274866,0.027647,0.335732,-9.300001,0.487400,-5.237679,6.677788,-3.024926,-8.379732,-6.539438,2.946727,9.821066,9.284784,-8.394656,-7.703188,6.409659],[-4.589890,0.459848,-8.253633,6.361912,-3.220304,6.198268,-0.976166,-7.671428,-1.588061,5.963948,7.551558,-9.375415,7.620724,8.132891,-5.574825,-3.043249],[4.164294,6.094886,1.787697,7.819880,-6.154687,6.823570,-6.095877,2.099656,9.004080,-9.328639,3.987711,5.357200,2.156335,-2.304134,0.459593,3.512602],[-0.560361,-4.320159,5.980994,9.156104,5.086995,-5.537229,-1.083827,-1.875804,-2.727126,4.187704,-0.149791,3.712107,1.555120,3.353237,-2.834830,6.620941],[1.185540,-4.227808,7.863459,-1.147323,4.221815,3.107653,7.832313,8.506122,-6.120474,9.654151,2.688256,3.343105,1.529479,-2.823710,9.743627,-2.056300],[4.777849,7.614280,1.365281,9.281535,7.617889,-9.365568,0.034029,-3.548016,-8.329987,-2.139669,-1.725593,-6.695699,-7.320736,9.917767,-3.882192,4.398324]],[[1.674405,3.577485,-2.811810,7.561186,2.711237,-4.544029,8.061954,-6.129190,0.861068,3.999445,-3.902204,6.880459,-5.647732,-7.753822,-2.118597,7.565103],[9.448326,-4.359078,0.893491,2.223046,-3.013777,1.201751,-1.105110,4.042765,-9.194206,-0.722123,6.091098,-9.049764,-0.636642,-7.591776,-0.009117,-3.111333],[-2.345414,0.665008,-0.052037,-8.821218,0.952061,-4.157858,-9.426096,8.564469,6.975943,2.906756,9.140167,-8.844731,5.384516,-7.134000,-6.801485,9.552266],[-4.422915,1.463765,6.825133,3.404316,1.769090,-5.131168,6.499270,6.952476,9.477930,0.872884,-0.221405,3.246014,2.370905,8.899395,-0.952858,-4.015819],[4.173587,-7.737394,-4.627528,5.810943,9.553539,2.465789,3.408926,4.993130,8.142602,8.368635,8.729804,3.422534,3.150960,-3.322006,2.766031,-9.141237],[-6.115257,9.720397,-1.367810,3.855373,8.349641,-8.142547,0.953033,2.210915,0.591822,-1.095531,7.534864,9.044341,-4.371059,8.252739,-2.457900,-2.005411],[-6.041806,0.018487,3.466327,-1.366925,5.027862,1.397711,9.544880,-9.240001,-0.635797,5.191976,-8.348457,-3.061071,-2.384619,6.423712,4.870306,-2.406627],[8.760024,-6.510319,-3.905146,9.779965,3.320419,-6.565497,-4.183501,5.511985,8.471078,-2.919350,2.679172,-9.287193,-6.505738,4.314493,3.068646,4.181921],[2.157673,0.123153,4.369378,-3.861976,-0.757497,8.601774,8.705083,9.522249,5.875625,-6.680731,-9.613663,-4.214735,-1.679739,-8.437206,4.364596,4.121485],[0.500422,-0.112561,0.998063,2.343208,4.075454,-0.752132,-0.115211,2.318119,-7.954395,-6.377578,-1.336834,6.489485,-2.912574,4.671825,-9.030855,5.769494],[3.671289,-3.359728,-7.870511,-3.297225,-5.660375,-9.479586,-0.322356,-7.407028,1.378691,5.134785,2.869337,5.132603,-8.310016,-2.755524,9.944705,-5.943397]],[[0.687849,7.389290,0.797598,-0.298575,9.907598,-5.102163,-5.651679,-2.969933,1.179491,-8.257999,-6.106888,8.758633,-2.459039,1.065606,6.883932,-2.426815],[-3.076420,-8.992487,-6.667817,7.923249,7.342818,2.333465,-2.701439,5.979918,-6.488514,6.470312,1.743481,0.148066,-0.653684,5.677169,7.650529,-6.105597],[-4.731845,6.956458,1.374866,-4.951504,-3.869633,0.888725,3.973532,-3.875057,-1.633485,-9.058442,-5.920511,0.769291,7.987894,-9.364190,-2.786349,-8.894507],[9.700725,8.320509,7.292775,7.225446,-8.374508,-4.476661,-2.463444,0.152786,-2.355415,-2.037303,2.978854,7.546660,4.867629,9.309344,8.782997,-0.417707],[7.630606,9.578043,2.561974,-9.801828,4.969993,9.542654,-9.798180,-1.860017,-7.795000,8.109053,-3.747973,-1.584087,8.708251,-2.825610,-8.501252,0.687550],[-5.220212,-7.268591,-1.011332,7.872248,5.247279,1.755511,0.601008,8.131581,-5.705651,-4.426742,0.128555,-8.179083,-3.296564,4.024115,7.547144,3.896952],[-9.317274,5.538366,-9.870089,-2.529185,5.910022,9.295742,-1.910603,6.025234,-1.833945,3.794055,-1.307020,-6.931953,-9.319752,4.188353,-1.391093,-8.780744],[-6.725179,1.551033,-7.825628,4.633370,5.200652,1.684376,7.650299,4.065263,-9.303302,9.712208,-9.246373,1.660718,-5.314564,8.039227,3.497602,1.052263],[3.506484,3.488715,-2.944458,-0.778085,3.789279,6.647262,-3.621547,-6.048776,-3.153113,4.845375,5.427078,6.743821,-1.993006,7.191263,-2.645277,8.151541],[1.596853,-4.797926,0.111204,-9.366359,-2.985000,2.474787,-2.492020,6.712871,-3.752892,1.121147,9.233081,4.392382,0.142797,-0.094146,4.973365,-0.428621],[-0.695237,-1.207607,7.126784,-4.374308,5.572116,-0.062514,-9.823531,-3.069974,-1.507023,-3.125458,-7.738197,2.081248,-9.826480,-8.325709,-7.335169,8.597866]],[[2.744742,-6.267513,-1.966184,-5.840462,9.513933,5.617804,-5.753707,-9.998152,7.334692,-3.369729,-6.451553,-6.130803,2.530604,-8.144283,8.512933,-2.555652],[1.950478,0.515659,-4.830553,8.388370,-3.627808,6.556350,-2.131756,9.674793,-8.659875,-4.358480,-4.160221,-3.405733,7.482932,4.625476,-9.277388,1.705288],[-6.455205,7.587333,-2.292665,-1.241802,5.369723,5.018834,2.965770,6.622854,-3.548922,-8.113192,-5.722450,6.480944,6.343387,-3.528651,-5.480169,-7.021247],[-6.443606,0.702659,-2.942506,6.888275,7.517790,-0.180214,-4.226679,1.908242,1.741608,1.460243,-7.197831,9.663179,7.194110,4.523523,6.263157,-0.320099],[4.328713,-3.913846,-0.273261,9.558545,-3.635443,-3.917152,8.769998,8.360186,-9.742562,1.258836,8.626814,-1.906861,-6.088682,6.817225,8.615741,-2.828636],[6.960780,6.359869,-9.670690,-9.947673,-6.120012,5.926601,-0.310744,-9.287465,1.226874,3.315286,-5.311203,0.831202,7.165288,-6.146436,2.402628,9.183785],[4.995275,-0.918148,2.014738,-7.238932,8.221436,4.528892,-1.685287,-7.754775,9.358010,8.179029,-8.943982,0.235756,8.289239,-8.615198,-0.116492,7.912227],[-4.097851,7.856218,-3.127897,6.771091,-2.545058,5.866027,-4.130153,-6.652332,8.556721,1.961881,8.655623,2.334966,-3.019211,3.289196,0.769361,-2.533938],[-2.208572,0.404258,5.318423,-5.292009,-6.072302,1.642129,-1.560230,-4.388148,6.614421,8.060129,-3.113858,0.295954,-1.809011,8.914777,8.936040,-8.396298],[-3.667776,3.936067,-7.420824,8.185487,6.523929,-1.210320,-3.345222,-8.881533,-9.285225,-2.658791,-5.985474,-5.396361,-2.390938,6.307631,9.232033,4.255753],[7.187041,-8.433539,1.332166,-6.494782,-5.573728,-8.658956,-9.199044,-9.750882,-0.631534,3.793743,-8.203946,9.681321,-1.133575,-9.631498,-7.674870,7.272120]],[[-9.534174,-6.662055,6.432306,7.737213,3.781272,-7.530582,-9.752449,-1.180587,-6.882641,9.794098,3.453946,6.057631,0.637076,-3.442803,-1.303997,-3.031507],[4.095182,-3.845590,0.293720,-5.281753,1.725495,-9.074888,4.539761,-7.563189,3.076424,-4.986762,-5.277629,-7.004601,6.342688,-5.677968,-8.422542,4.195781],[8.134926,-3.970591,1.719362,1.000983,7.328153,-6.614085,-1.589027,-3.004424,-4.360605,9.308341,8.333399,3.607794,-9.724067,-0.180937,-7.017382,-6.392624],[1.918117,-3.112884,3.854630,2.748361,-8.565687,4.770397,-7.176942,-3.356247,-7.346780,1.490261,7.961731,-1.616057,-6.634546,-4.461237,-6.482458,-6.813143],[8.311547,-8.289843,-6.938964,9.999720,9.042523,-3.926772,3.039457,3.217074,-1.648423,9.837991,8.124758,7.730779,-8.210757,-4.622410,-6.760540,-1.404050],[8.351752,-9.943590,-6.509601,-7.862563,-9.662535,8.563190,3.531707,1.604449,7.134205,7.208182,-5.534599,4.541361,-8.961321,-8.282306,-5.801266,-5.972508],[8.944338,-5.052273,9.965833,-2.857086,7.327318,7.328016,-4.223238,-8.187341,9.054542,-1.026418,-2.044183,-5.635429,8.173027,9.833823,7.540792,0.137739],[-7.524872,-4.694047,1.005714,5.844554,-1.057480,7.405152,2.289398,-1.229972,-5.689034,-3.904358,-3.081859,6.869211,2.986882,-4.328623,1.772500,-9.505248],[2.770069,1.379451,7.040241,8.006776,6.620126,-5.180969,-4.937778,1.952807,5.759527,2.939358,-9.427158,7.020841,9.541444,-2.653778,1.347204,-2.525134],[6.019307,3.439430,-6.249250,-1.363882,-4.180428,-7.151437,3.271357,3.098093,9.860971,6.870613,8.755129,-7.007970,-2.367949,5.605375,0.969569,-4.686594],[8.561807,6.534170,-4.543427,5.259380,-8.306640,9.571679,4.430629,-9.414459,4.110971,-5.087259,-9.986686,0.827874,7.873605,-7.649057,-2.972602,6.382359]],[[6.066335,6.621487,-4.575224,-3.139324,-1.283682,8.170914,-0.106432,-3.399996,6.705176,-6.959998,7.801000,-0.194459,4.140164,2.591445,4.158299,1.398420],[6.142788,-5.201750,-9.096485,-8.134595,-0.445855,-5.408766,8.731004,-6.055255,-8.943933,-3.126987,-8.032766,-1.942224,-9.353766,7.148158,4.099481,-6.630769],[2.555931,-1.416864,4.426015,-0.856940,-9.589019,-9.997966,2.642550,-2.236447,4.634584,-1.441120,2.026760,8.744103,-8.666518,1.382441,-0.762445,9.307660],[-1.823452,7.367754,-3.664193,3.654958,-0.303742,5.604875,-0.367249,6.007617,-4.145026,9.756953,4.015652,3.682382,8.194991,4.410646,-3.409256,7.744312],[-8.365118,-4.162280,-9.906718,-9.645158,0.223745,2.235248,6.839405,-0.932400,-4.354062,-2.780190,-2.884543,8.138296,-9.355105,6.035625,5.663186,-0.825755],[4.924591,7.528338,-0.288926,9.193791,5.692270,-4.928903,1.869363,-3.278922,-4.606874,7.417732,8.063628,1.935459,3.893877,-1.388919,5.613079,9.045444],[-4.635365,1.710185,-1.825318,-1.368707,8.105096,-9.754191,4.901509,-4.915215,2.047398,1.371218,-9.633058,3.682247,5.017755,5.231715,-5.698223,-9.405843],[3.826544,7.989462,-2.260884,7.395891,-2.003573,-6.036010,-7.559649,-5.941922,6.115020,-9.031478,-8.816522,9.613448,-5.208039,-2.941159,0.080121,9.261046],[-3.923054,-4.991766,-8.613860,-2.427325,-1.761194,0.524850,6.820602,-4.738532,9.519051,9.368345,-5.681983,2.457990,1.423481,1.835058,-1.467917,4.003122],[-4.998575,2.345416,9.532840,6.232353,9.108026,-3.791736,-7.786119,0.842802,-7.284876,2.165454,2.728417,7.799057,4.555910,-9.170573,3.365742,-5.354987],[0.132049,-0.564259,-6.103268,-3.629331,-2.166498,-7.284357,-7.166754,-5.133004,-6.215678,6.752203,2.534907,-1.236461,-6.224954,-5.419504,-4.663217,0.703303]],[[6.202968,-5.667183,6.245850,4.577610,-2.278820,6.613617,1.508254,7.516107,0.655737,0.260079,5.239273,6.822762,-9.910830,9.377776,7.204960,2.720806],[-2.222992,-9.636887,-8.591618,-2.177950,6.174101,2.764184,1.020358,2.446687,-4.086198,6.685394,-2.472390,3.776499,5.536491,-7.157431,4.495659,1.411761],[2.865277,1.463198,1.505738,-7.171274,8.535785,0.377855,-1.560180,-7.942644,6.925248,-2.114153,-0.807300,9.612160,-3.549937,-9.155138,1.530402,-3.464239],[3.281542,-3.456846,6.753573,-8.403803,5.376235,8.794945,-9.121213,-9.076988,-8.808705,4.459577,-7.618877,-2.605658,-5.779363,-0.912985,-8.117915,0.270515],[-3.839899,-5.814064,-5.116291,2.909367,-0.819542,-1.927726,-4.524926,-9.580866,7.398271,2.798500,-5.161746,3.661497,6.234547,-8.081343,-2.444774,8.149389],[-9.792066,-6.400725,-7.063617,-8.712298,-0.841618,3.864086,6.754905,0.559425,-2.692006,-7.203164,-4.203359,1.691718,1.747960,6.234439,3.344202,-0.993708],[-6.668540,7.199256,-1.896653,8.527514,-2.726032,1.578468,4.852259,-1.054123,-0.263772,-1.266099,-6.180255,-0.850304,-4.136334,4.906061,-6.065922,9.677447],[-3.893818,-2.302079,-4.396364,-8.523391,-4.655546,-1.391326,-5.874503,1.045688,6.563103,-9.022399,-7.292839,4.777947,-2.246564,-6.708409,-3.966079,-1.984518],[-2.867832,-5.290982,-0.363184,9.847566,-3.979974,-2.105093,3.091111,5.375853,-7.431006,-7.949116,-9.579097,4.825590,6.465895,-1.087133,4.805725,-8.085479],[6.439693,-0.944850,0.749118,-9.067095,8.730906,7.038405,2.319700,7.827851,-9.017382,-3.023789,9.391746,0.008502,9.996779,-4.572617,-6.764959,1.429148],[2.199635,-7.929106,7.244493,6.312675,1.993532,6.045098,2.967779,-1.520686,7.839801,6.766519,-4.605281,2.598259,-2.683457,-6.463161,-5.906639,-8.337141]],[[8.657123,3.062308,9.775552,8.636224,7.090682,2.779234,8.854333,-7.311012,-8.124289,1.659670,-7.006311,8.292770,3.467738,-3.080317,7.014515,8.227560],[3.729021,6.044654,1.220117,3.386401,-0.346534,-4.234153,0.206137,-7.134665,-1.258781,-9.092194,-7.045839,3.418492,-9.171716,9.392226,-0.198992,-5.367514],[9.859783,-4.565282,3.770850,5.365980,7.943923,9.374211,-0.964093,-3.777497,-0.292650,-5.172422,-4.549970,-4.694689,6.435044,-1.065256,-1.670965,0.665041],[1.933551,0.813432,0.212708,-6.343383,-6.199456,5.878572,8.992484,6.617865,2.693544,-3.294894,0.697539,-5.110687,-3.865903,-7.293147,4.350573,5.408155],[0.062667,8.653377,0.777040,8.564276,-8.179521,9.956381,9.542043,8.866034,-1.571592,-1.175076,-7.116971,-5.266112,-6.546320,6.773085,-6.563270,-4.691447],[1.613429,-8.572572,3.327954,-4.503374,7.966857,7.078642,-3.096381,2.751389,-0.149107,-6.061910,-0.682639,7.582741,0.417582,-6.179614,4.855177,-1.242017],[0.467544,-7.195460,-9.217553,-7.258011,-4.411386,-9.343995,-6.945285,2.042094,-2.458542,6.615061,-7.851322,4.434447,2.565482,0.400385,-8.317709,-6.893322],[-8.240215,-7.198016,4.443298,-9.873027,-2.527478,2.334422,-5.764142,6.118156,-9.813828,2.073997,3.424432,0.083384,1.744840,-9.979032,-1.475817,1.554334],[4.281982,3.472224,-3.773532,-4.949111,9.889672,1.910010,-6.757551,-4.497669,2.458297,4.445450,-3.141234,7.567696,6.269288,3.117392,-4.535834,-6.443679],[-7.393617,2.005858,-4.318054,3.799670,0.726791,1.516037,2.495069,-9.274846,-5.750457,4.806504,-3.827515,-1.277705,-0.206809,3.722042,-2.946488,-3.787255],[-9.905832,7.021360,7.095626,-0.185864,6.846510,-1.285442,7.220014,7.110007,-5.560609,-6.902754,4.002587,-2.918724,-2.260408,9.358844,-7.543450,6.871646]],[[5.516471,3.854546,7.732008,5.412738,5.034845,5.481164,-1.958818,-8.630883,0.501165,-9.404719,3.915772,5.011843,-3.984890,-8.543008,-7.828363,5.119259],[-0.236558,4.964900,-1.570689,-7.903229,-9.666079,-6.955666,-9.556894,-3.461744,8.719044,3.493925,9.447214,-9.438310,2.293320,-9.242277,-8.896281,6.689431],[-8.634451,-4.024481,1.533844,2.168034,-3.311433,-3.182424,-1.755908,3.531886,0.696941,5.348959,2.797363,9.084371,-9.645591,-2.438451,1.590531,-1.308010],[-3.457842,8.782679,6.681947,-8.866862,-5.827356,4.101412,6.473385,9.549070,9.819927,4.498375,-4.715721,9.934829,5.141427,-9.838361,3.357099,-2.516608],[4.720946,3.958984,-2.628674,3.365829,-8.985390,-7.181341,1.246651,6.769443,-4.625858,1.439100,1.613835,1.731052,-7.417266,1.082455,-9.094138,-8.851802],[0.475602,2.010995,7.454182,4.293279,9.056559,5.853091,6.521657,6.678381,4.214876,-2.857929,7.462082,3.861874,1.574244,9.721384,8.783553,-8.683048],[0.407478,-7.203543,-7.049132,-5.900846,5.203848,-2.271222,-4.018134,-8.511896,-9.429493,-6.869595,8.925814,3.618213,6.640677,-9.060796,-3.955502,0.103769],[-2.743402,-1.541681,2.021760,-4.293845,-1.127694,9.761539,-6.776787,8.400920,5.236427,-7.324753,4.489096,4.911177,-0.586734,6.206004,-9.233051,-6.557863],[3.139067,6.726685,-9.815875,7.438148,-9.035124,5.114821,7.345230,7.088791,4.398965,1.355912,-1.892135,1.780206,-3.020287,0.611487,7.404303,-5.613826],[2.099345,-0.197380,8.915152,-2.705044,-0.679128,0.589295,-4.885430,-8.905240,-4.359325,4.546363,1.492613,-9.527464,4.364802,-1.044492,1.243707,6.999558],[5.401004,-1.527540,-1.776417,-0.275956,9.960541,-7.714659,2.756257,0.303823,-9.341589,-8.662347,2.473170,3.253910,-3.026007,0.081067,-9.453980,-6.297312]]], dtype = "float32")#candidate|9286|(10, 11, 16)|const|float32
bop_9287 = relay.floor_divide(const_9285.astype('float32'), relay.reshape(const_9286.astype('float32'), relay.shape_of(const_9285))) # shape=(10, 11, 16)
func_9156_call = mod.get_global_var('func_9156')
func_9158_call = mutated_mod.get_global_var('func_9158')
call_9291 = func_9156_call()
call_9292 = func_9156_call()
output = relay.Tuple([bop_9287,call_9291,])
output2 = relay.Tuple([bop_9287,call_9292,])
func_9293 = relay.Function([], output)
mod['func_9293'] = func_9293
mod = relay.transform.InferType()(mod)
output = func_9293()
func_9294 = relay.Function([], output)
mutated_mod['func_9294'] = func_9294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mod.get_global_var('func_5732')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_9329 = relay.TupleGetItem(func_5732_call(), 0)
call_9330 = relay.TupleGetItem(func_5734_call(), 0)
output = call_9329
output2 = call_9330
func_9335 = relay.Function([], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
mutated_mod['func_9335'] = func_9335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9335_call = mutated_mod.get_global_var('func_9335')
call_9336 = func_9335_call()
output = call_9336
func_9337 = relay.Function([], output)
mutated_mod['func_9337'] = func_9337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9029_call = mod.get_global_var('func_9029')
func_9031_call = mutated_mod.get_global_var('func_9031')
call_9340 = relay.TupleGetItem(func_9029_call(), 1)
call_9341 = relay.TupleGetItem(func_9031_call(), 1)
func_8276_call = mod.get_global_var('func_8276')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_9347 = relay.TupleGetItem(func_8276_call(), 0)
call_9348 = relay.TupleGetItem(func_8278_call(), 0)
uop_9362 = relay.exp(call_9340.astype('float64')) # shape=(6, 13, 4)
uop_9364 = relay.exp(call_9341.astype('float64')) # shape=(6, 13, 4)
func_5459_call = mod.get_global_var('func_5459')
func_5461_call = mutated_mod.get_global_var('func_5461')
const_9379 = relay.const([[7,-5,10,3],[-3,-9,-3,9],[-5,6,2,2],[-8,-7,-2,-10],[2,9,1,-2],[-5,3,5,4],[8,6,1,8],[-8,8,1,-8],[5,-7,-1,1],[9,-6,5,-4],[9,-2,10,2],[2,-10,9,-6],[-7,-3,9,6],[7,2,-1,-6],[6,3,-6,4]], dtype = "uint8")#candidate|9379|(15, 4)|const|uint8
call_9378 = relay.TupleGetItem(func_5459_call(relay.reshape(const_9379.astype('uint8'), [10, 1, 6])), 0)
call_9380 = relay.TupleGetItem(func_5461_call(relay.reshape(const_9379.astype('uint8'), [10, 1, 6])), 0)
output = relay.Tuple([call_9347,uop_9362,call_9378,const_9379,])
output2 = relay.Tuple([call_9348,uop_9364,call_9380,const_9379,])
func_9383 = relay.Function([], output)
mod['func_9383'] = func_9383
mod = relay.transform.InferType()(mod)
mutated_mod['func_9383'] = func_9383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9383_call = mutated_mod.get_global_var('func_9383')
call_9384 = func_9383_call()
output = call_9384
func_9385 = relay.Function([], output)
mutated_mod['func_9385'] = func_9385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9427 = relay.var("var_9427", dtype = "uint32", shape = (15, 14, 10))#candidate|9427|(15, 14, 10)|var|uint32
var_9428 = relay.var("var_9428", dtype = "uint32", shape = (15, 14, 10))#candidate|9428|(15, 14, 10)|var|uint32
bop_9429 = relay.greater_equal(var_9427.astype('bool'), relay.reshape(var_9428.astype('bool'), relay.shape_of(var_9427))) # shape=(15, 14, 10)
output = bop_9429
output2 = bop_9429
func_9434 = relay.Function([var_9427,var_9428,], output)
mod['func_9434'] = func_9434
mod = relay.transform.InferType()(mod)
var_9435 = relay.var("var_9435", dtype = "uint32", shape = (15, 14, 10))#candidate|9435|(15, 14, 10)|var|uint32
var_9436 = relay.var("var_9436", dtype = "uint32", shape = (15, 14, 10))#candidate|9436|(15, 14, 10)|var|uint32
output = func_9434(var_9435,var_9436,)
func_9437 = relay.Function([var_9435,var_9436,], output)
mutated_mod['func_9437'] = func_9437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5811_call = mod.get_global_var('func_5811')
func_5812_call = mutated_mod.get_global_var('func_5812')
call_9446 = relay.TupleGetItem(func_5811_call(), 0)
call_9447 = relay.TupleGetItem(func_5812_call(), 0)
output = call_9446
output2 = call_9447
func_9456 = relay.Function([], output)
mod['func_9456'] = func_9456
mod = relay.transform.InferType()(mod)
output = func_9456()
func_9457 = relay.Function([], output)
mutated_mod['func_9457'] = func_9457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_9466 = relay.TupleGetItem(func_1556_call(), 0)
call_9467 = relay.TupleGetItem(func_1557_call(), 0)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_9468 = relay.TupleGetItem(func_1556_call(), 0)
call_9469 = relay.TupleGetItem(func_1557_call(), 0)
func_5063_call = mod.get_global_var('func_5063')
func_5064_call = mutated_mod.get_global_var('func_5064')
call_9477 = relay.TupleGetItem(func_5063_call(), 0)
call_9478 = relay.TupleGetItem(func_5064_call(), 0)
const_9493 = relay.const([[[-9,-2,-2,3,-6,-4,8,4,5,-3],[-1,3,-8,-10,8,-10,2,7,9,-3],[-2,7,-6,-5,-8,-3,-1,-8,-5,-3],[8,9,5,5,5,-9,4,7,9,-8],[10,-6,10,-3,-2,7,10,-1,3,9],[3,-4,-3,6,-3,-1,-10,8,-2,-6],[-7,-6,10,-4,-3,-2,2,-3,7,9],[6,6,4,7,-5,2,-3,-1,-8,-5],[-9,-9,-2,-5,4,2,-1,-7,4,-3],[-4,-3,5,-1,2,-6,-4,1,7,-7],[-2,-2,-9,10,-2,2,-9,-6,-10,9],[-4,4,-10,-4,-3,-10,9,-9,-5,-2],[3,-5,-1,-1,8,5,-5,-10,6,-3],[-4,-3,9,3,-1,2,-9,10,-8,2]],[[-9,9,-6,10,-2,10,-10,-1,6,-4],[9,3,-3,-9,-4,-10,-8,8,8,7],[-2,8,-9,-4,2,-4,-2,-10,-1,-7],[-2,7,-5,-5,2,-5,-6,-10,-1,-1],[-10,6,3,-8,-5,-9,-1,-6,-1,1],[2,10,8,-4,-4,-2,4,-8,-3,1],[-3,-6,7,1,4,1,-8,5,-1,-5],[-8,9,4,-8,6,-7,-2,-5,7,-6],[8,9,10,-1,5,-8,-2,2,6,5],[1,-3,6,-1,4,8,-7,-9,2,-10],[6,9,-4,-4,-3,2,-4,7,5,-5],[-7,10,-1,-1,-8,10,-8,10,2,-2],[-6,10,-1,9,5,4,8,-6,-4,-10],[9,-4,10,6,-1,-8,-3,6,7,2]],[[1,4,2,8,6,-8,-9,9,-8,3],[5,8,-2,-4,2,-1,-1,-2,-2,9],[-10,2,-9,9,5,-9,-5,-10,3,-8],[-9,-10,3,-5,2,-4,1,2,-4,-1],[4,1,9,6,5,-9,-2,-7,10,-1],[-8,-7,-8,10,1,-5,1,2,-9,-4],[-6,-1,1,-5,-1,-5,1,9,10,-5],[1,6,8,-4,8,-1,10,-5,1,-1],[-6,3,-8,-9,2,-1,-2,6,5,-6],[7,-9,1,-7,-2,7,5,-7,2,3],[-8,6,-1,1,-2,9,6,4,10,2],[-10,-3,-10,-7,-4,4,-7,5,5,-2],[-5,-4,-8,2,2,3,-4,-8,-7,-5],[-7,5,1,2,6,-1,-6,5,7,-4]],[[-1,2,5,8,-7,3,3,-8,7,-10],[-5,-7,-10,-4,8,-8,7,4,4,-4],[-6,4,6,-6,3,10,-9,-8,-7,-7],[-10,-4,9,-9,-2,3,-3,-7,-1,3],[-9,4,8,-8,-2,-2,2,-9,5,-3],[4,-5,4,-5,-5,1,-9,-1,-6,-6],[3,-1,5,7,10,7,7,9,3,6],[-10,9,1,10,10,4,-3,10,4,8],[-7,-8,-6,-4,10,-5,7,2,6,5],[-8,-9,5,7,-5,5,-9,-6,7,3],[2,-10,2,8,3,-3,-4,10,-2,-1],[3,10,-9,6,-8,3,-7,-2,-4,8],[-4,10,3,-9,8,-3,8,-2,10,2],[9,10,10,-4,2,4,2,6,-4,4]],[[7,-3,-1,-1,-5,10,8,-9,-2,3],[-4,10,8,5,4,-4,-7,7,1,10],[1,-9,10,7,8,5,-6,-2,-2,-6],[8,-9,-4,4,4,-1,-4,2,-6,-7],[9,-10,9,-9,1,-9,-5,6,5,-5],[4,2,6,-5,4,-1,-3,10,-3,7],[6,4,4,-1,10,10,3,3,7,-4],[-9,8,5,8,-8,-5,8,-8,-9,-3],[-4,-2,-4,-8,2,-6,8,5,-3,-5],[-5,-9,-10,-9,-3,-8,5,8,5,-4],[10,10,-3,5,-9,1,1,-8,5,9],[-10,-9,-7,6,-2,2,10,4,-8,-1],[9,10,-4,-10,8,8,-6,-4,-3,8],[-9,-1,-2,-4,4,-7,9,-1,-10,1]],[[10,-5,-8,3,9,1,2,9,-7,-4],[8,1,3,-10,3,-10,-3,-1,-3,-4],[-6,2,-5,9,4,10,-7,9,3,2],[1,10,8,-6,-6,5,3,7,8,1],[-3,2,-2,-9,-2,-2,4,8,-3,-3],[3,10,-5,6,-5,3,-10,8,-8,8],[10,3,-1,-6,-5,3,6,6,10,-3],[2,5,-3,-3,-3,-2,-10,9,-6,-6],[-3,-1,-2,-8,-2,1,9,4,-10,4],[8,8,-1,-9,-1,9,4,1,-8,10],[10,-4,7,2,6,3,-1,2,-8,-10],[6,3,1,5,2,1,-7,2,4,-5],[1,-2,1,-4,-5,-7,6,-8,-3,8],[8,-1,4,-1,9,-9,-4,-1,-7,3]],[[3,-10,2,-8,2,-2,3,9,9,6],[-6,6,-5,4,-6,-3,-8,10,4,-7],[-1,-1,4,-4,10,9,-6,-5,-4,5],[9,-8,3,-9,5,-5,6,-3,-6,1],[8,9,5,-6,-6,-8,9,1,6,-10],[7,9,3,-2,-8,2,-3,1,8,6],[8,-6,3,-10,-1,-10,-10,-10,1,-10],[6,-7,7,-4,5,7,-5,-2,-4,7],[-7,-2,8,-7,-7,-7,1,10,4,-2],[-6,-4,-4,9,-1,1,-5,-4,-8,-1],[-10,-6,6,8,9,-1,-9,-6,-3,10],[3,-3,-6,-1,-8,7,-5,-8,6,1],[7,10,6,8,-1,3,-10,2,1,-8],[8,-6,8,-3,1,-2,3,4,-8,-9]],[[1,-4,-6,6,-4,8,-2,4,-10,6],[1,10,10,3,6,-10,4,7,4,9],[8,9,-4,1,2,-7,-5,-6,1,-4],[1,-4,-10,5,4,10,-3,-3,-4,1],[10,-6,7,10,1,-4,8,9,1,-1],[-10,-7,10,10,-4,7,-10,-1,-4,4],[-6,10,-8,-3,-3,-4,-5,-3,-2,-8],[-3,2,-9,10,-5,9,-3,-7,-7,10],[3,10,8,3,-8,8,-6,-5,-3,-8],[-7,2,-5,-3,-7,2,-8,10,-8,7],[5,-7,6,-6,9,9,-1,8,-8,-10],[-3,-9,-5,-6,-3,8,8,1,-9,5],[10,-4,5,-1,-10,-9,1,3,-10,-10],[-3,3,4,-7,10,1,-8,-3,6,5]]], dtype = "int8")#candidate|9493|(8, 14, 10)|const|int8
bop_9494 = relay.greater_equal(call_9477.astype('bool'), relay.reshape(const_9493.astype('bool'), relay.shape_of(call_9477))) # shape=(8, 14, 10)
bop_9497 = relay.greater_equal(call_9478.astype('bool'), relay.reshape(const_9493.astype('bool'), relay.shape_of(call_9478))) # shape=(8, 14, 10)
func_9293_call = mod.get_global_var('func_9293')
func_9294_call = mutated_mod.get_global_var('func_9294')
call_9516 = relay.TupleGetItem(func_9293_call(), 0)
call_9517 = relay.TupleGetItem(func_9294_call(), 0)
func_9029_call = mod.get_global_var('func_9029')
func_9031_call = mutated_mod.get_global_var('func_9031')
call_9536 = relay.TupleGetItem(func_9029_call(), 0)
call_9537 = relay.TupleGetItem(func_9031_call(), 0)
output = relay.Tuple([call_9466,call_9468,bop_9494,call_9516,call_9536,])
output2 = relay.Tuple([call_9467,call_9469,bop_9497,call_9517,call_9537,])
func_9538 = relay.Function([], output)
mod['func_9538'] = func_9538
mod = relay.transform.InferType()(mod)
mutated_mod['func_9538'] = func_9538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9538_call = mutated_mod.get_global_var('func_9538')
call_9539 = func_9538_call()
output = call_9539
func_9540 = relay.Function([], output)
mutated_mod['func_9540'] = func_9540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8276_call = mod.get_global_var('func_8276')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_9573 = relay.TupleGetItem(func_8276_call(), 0)
call_9574 = relay.TupleGetItem(func_8278_call(), 0)
output = call_9573
output2 = call_9574
func_9593 = relay.Function([], output)
mod['func_9593'] = func_9593
mod = relay.transform.InferType()(mod)
mutated_mod['func_9593'] = func_9593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9593_call = mutated_mod.get_global_var('func_9593')
call_9594 = func_9593_call()
output = call_9594
func_9595 = relay.Function([], output)
mutated_mod['func_9595'] = func_9595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6086_call = mod.get_global_var('func_6086')
func_6087_call = mutated_mod.get_global_var('func_6087')
call_9596 = relay.TupleGetItem(func_6086_call(), 1)
call_9597 = relay.TupleGetItem(func_6087_call(), 1)
output = relay.Tuple([call_9596,])
output2 = relay.Tuple([call_9597,])
func_9600 = relay.Function([], output)
mod['func_9600'] = func_9600
mod = relay.transform.InferType()(mod)
output = func_9600()
func_9601 = relay.Function([], output)
mutated_mod['func_9601'] = func_9601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5559_call = mod.get_global_var('func_5559')
func_5560_call = mutated_mod.get_global_var('func_5560')
call_9615 = relay.TupleGetItem(func_5559_call(), 0)
call_9616 = relay.TupleGetItem(func_5560_call(), 0)
output = relay.Tuple([call_9615,])
output2 = relay.Tuple([call_9616,])
func_9627 = relay.Function([], output)
mod['func_9627'] = func_9627
mod = relay.transform.InferType()(mod)
output = func_9627()
func_9628 = relay.Function([], output)
mutated_mod['func_9628'] = func_9628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5533_call = mod.get_global_var('func_5533')
func_5535_call = mutated_mod.get_global_var('func_5535')
call_9695 = relay.TupleGetItem(func_5533_call(), 1)
call_9696 = relay.TupleGetItem(func_5535_call(), 1)
output = relay.Tuple([call_9695,])
output2 = relay.Tuple([call_9696,])
func_9737 = relay.Function([], output)
mod['func_9737'] = func_9737
mod = relay.transform.InferType()(mod)
mutated_mod['func_9737'] = func_9737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9737_call = mutated_mod.get_global_var('func_9737')
call_9738 = func_9737_call()
output = call_9738
func_9739 = relay.Function([], output)
mutated_mod['func_9739'] = func_9739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9265_call = mod.get_global_var('func_9265')
func_9267_call = mutated_mod.get_global_var('func_9267')
call_9746 = func_9265_call()
call_9747 = func_9265_call()
output = call_9746
output2 = call_9747
func_9759 = relay.Function([], output)
mod['func_9759'] = func_9759
mod = relay.transform.InferType()(mod)
mutated_mod['func_9759'] = func_9759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9759_call = mutated_mod.get_global_var('func_9759')
call_9760 = func_9759_call()
output = call_9760
func_9761 = relay.Function([], output)
mutated_mod['func_9761'] = func_9761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9762 = relay.var("var_9762", dtype = "uint32", shape = (12, 14, 13))#candidate|9762|(12, 14, 13)|var|uint32
var_9763 = relay.var("var_9763", dtype = "uint32", shape = (12, 14, 13))#candidate|9763|(12, 14, 13)|var|uint32
bop_9764 = relay.bitwise_and(var_9762.astype('uint32'), relay.reshape(var_9763.astype('uint32'), relay.shape_of(var_9762))) # shape=(12, 14, 13)
func_2297_call = mod.get_global_var('func_2297')
func_2299_call = mutated_mod.get_global_var('func_2299')
call_9776 = relay.TupleGetItem(func_2297_call(), 2)
call_9777 = relay.TupleGetItem(func_2299_call(), 2)
uop_9782 = relay.erf(var_9763.astype('float64')) # shape=(12, 14, 13)
func_5309_call = mod.get_global_var('func_5309')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_9788 = relay.TupleGetItem(func_5309_call(), 1)
call_9789 = relay.TupleGetItem(func_5310_call(), 1)
func_6399_call = mod.get_global_var('func_6399')
func_6401_call = mutated_mod.get_global_var('func_6401')
call_9790 = relay.TupleGetItem(func_6399_call(), 1)
call_9791 = relay.TupleGetItem(func_6401_call(), 1)
output = relay.Tuple([bop_9764,call_9776,uop_9782,call_9788,call_9790,])
output2 = relay.Tuple([bop_9764,call_9777,uop_9782,call_9789,call_9791,])
func_9792 = relay.Function([var_9762,var_9763,], output)
mod['func_9792'] = func_9792
mod = relay.transform.InferType()(mod)
var_9793 = relay.var("var_9793", dtype = "uint32", shape = (12, 14, 13))#candidate|9793|(12, 14, 13)|var|uint32
var_9794 = relay.var("var_9794", dtype = "uint32", shape = (12, 14, 13))#candidate|9794|(12, 14, 13)|var|uint32
output = func_9792(var_9793,var_9794,)
func_9795 = relay.Function([var_9793,var_9794,], output)
mutated_mod['func_9795'] = func_9795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3047_call = mod.get_global_var('func_3047')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_9816 = relay.TupleGetItem(func_3047_call(), 0)
call_9817 = relay.TupleGetItem(func_3048_call(), 0)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_9819 = relay.TupleGetItem(func_4460_call(), 3)
call_9820 = relay.TupleGetItem(func_4461_call(), 3)
func_4460_call = mod.get_global_var('func_4460')
func_4461_call = mutated_mod.get_global_var('func_4461')
call_9830 = relay.TupleGetItem(func_4460_call(), 7)
call_9831 = relay.TupleGetItem(func_4461_call(), 7)
func_5710_call = mod.get_global_var('func_5710')
func_5714_call = mutated_mod.get_global_var('func_5714')
const_9836 = relay.const(-2.285311, dtype = "float64")#candidate|9836|()|const|float64
var_9837 = relay.var("var_9837", dtype = "float64", shape = (88,))#candidate|9837|(88,)|var|float64
call_9835 = relay.TupleGetItem(func_5710_call(relay.reshape(const_9836.astype('float64'), []), relay.reshape(var_9837.astype('float64'), [1, 11, 8]), ), 0)
call_9838 = relay.TupleGetItem(func_5714_call(relay.reshape(const_9836.astype('float64'), []), relay.reshape(var_9837.astype('float64'), [1, 11, 8]), ), 0)
bop_9839 = relay.bitwise_xor(call_9835.astype('int8'), const_9836.astype('int8')) # shape=(1, 11, 8)
bop_9842 = relay.bitwise_xor(call_9838.astype('int8'), const_9836.astype('int8')) # shape=(1, 11, 8)
output = relay.Tuple([call_9816,call_9819,call_9830,var_9837,bop_9839,])
output2 = relay.Tuple([call_9817,call_9820,call_9831,var_9837,bop_9842,])
func_9863 = relay.Function([var_9837,], output)
mod['func_9863'] = func_9863
mod = relay.transform.InferType()(mod)
var_9864 = relay.var("var_9864", dtype = "float64", shape = (88,))#candidate|9864|(88,)|var|float64
output = func_9863(var_9864)
func_9865 = relay.Function([var_9864], output)
mutated_mod['func_9865'] = func_9865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2587_call = mod.get_global_var('func_2587')
func_2588_call = mutated_mod.get_global_var('func_2588')
call_9906 = relay.TupleGetItem(func_2587_call(), 1)
call_9907 = relay.TupleGetItem(func_2588_call(), 1)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_9913 = relay.TupleGetItem(func_1803_call(), 0)
call_9914 = relay.TupleGetItem(func_1805_call(), 0)
output = relay.Tuple([call_9906,call_9913,])
output2 = relay.Tuple([call_9907,call_9914,])
func_9924 = relay.Function([], output)
mod['func_9924'] = func_9924
mod = relay.transform.InferType()(mod)
mutated_mod['func_9924'] = func_9924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9924_call = mutated_mod.get_global_var('func_9924')
call_9925 = func_9924_call()
output = call_9925
func_9926 = relay.Function([], output)
mutated_mod['func_9926'] = func_9926
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4598_call = mod.get_global_var('func_4598')
func_4599_call = mutated_mod.get_global_var('func_4599')
call_9927 = func_4598_call()
call_9928 = func_4598_call()
output = relay.Tuple([call_9927,])
output2 = relay.Tuple([call_9928,])
func_9933 = relay.Function([], output)
mod['func_9933'] = func_9933
mod = relay.transform.InferType()(mod)
output = func_9933()
func_9934 = relay.Function([], output)
mutated_mod['func_9934'] = func_9934
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9947 = relay.const([[[-2,7,-10,-10,-9,-10,-5,7,-6],[8,-7,-10,4,7,3,-1,-1,-8],[7,-10,5,7,10,2,2,10,5],[-4,-1,6,4,-8,-6,-6,6,-1],[7,-1,-1,2,2,-5,-3,-6,9],[-8,-9,-10,3,-2,-3,10,-9,4],[5,-5,10,-2,8,-7,9,-10,2],[-5,-5,3,-8,-5,-5,8,6,5],[-3,1,4,-8,5,-3,-9,1,-5],[-1,7,-1,8,-10,-3,2,-3,-7],[5,4,-5,-9,3,-8,6,3,-7],[6,4,-2,3,4,9,7,-7,7]],[[5,-6,-8,9,6,-7,-6,2,9],[8,-8,-9,4,-4,-6,4,-7,-4],[-9,-6,6,-9,6,-4,-5,-6,7],[-1,-3,5,-4,-5,-3,5,-3,-6],[6,-3,9,7,2,-7,1,1,3],[-5,6,9,10,-9,6,-4,-3,5],[6,3,7,8,-8,-4,-6,-9,1],[-2,-3,-4,8,-3,4,-2,4,-8],[-5,-9,-7,5,1,8,3,3,-4],[-9,4,3,4,8,-1,6,-3,1],[7,-7,-10,-2,-8,-3,3,-5,3],[-7,-5,2,-1,2,-5,-8,-8,3]],[[-2,3,4,-10,-5,6,-7,5,-7],[-8,7,-4,4,7,7,-10,-8,8],[-6,-9,-5,10,-9,4,4,-6,-3],[-5,2,-8,3,9,10,3,6,-8],[-6,-3,-5,-1,-8,-10,-7,7,-9],[2,3,-3,-9,-7,-8,-5,5,-1],[4,7,-1,4,-4,-9,6,-4,5],[9,4,8,-5,8,3,-8,1,1],[-6,2,-8,2,-4,-4,-4,2,3],[9,5,5,7,6,-3,-2,4,9],[-4,-7,-7,-9,5,8,3,3,-5],[7,4,-1,-10,5,4,-5,7,9]],[[4,7,-9,-5,-4,-2,7,-2,1],[-9,4,-5,2,-7,4,4,-3,-5],[-8,7,-9,1,-8,-8,-4,-2,-4],[9,6,4,-3,8,-9,-10,-3,9],[6,7,-4,-5,-1,9,3,-1,3],[1,-4,-3,1,-2,-10,4,4,2],[-6,8,-3,5,6,-6,-1,-6,5],[-8,1,-9,-2,7,-4,-3,5,8],[-10,-3,-8,7,8,-2,3,9,1],[-4,-1,-8,9,5,-3,-1,7,1],[-5,-3,-4,-5,-7,10,2,-1,-5],[8,-10,-8,-8,-8,-5,8,-9,-2]],[[-8,-7,-3,2,-1,8,2,3,-9],[-5,-2,-1,3,-6,2,3,-8,4],[-9,7,-1,-9,-1,7,3,-8,-6],[-1,-10,-1,-8,-2,-7,6,-7,8],[-7,3,9,-9,-1,-9,-6,5,-9],[8,-1,2,9,5,-4,-3,10,-1],[5,3,-5,-2,5,6,-2,-1,-5],[2,-2,9,10,7,10,-10,7,1],[-8,-4,-2,4,5,8,8,-3,5],[-8,-5,-6,4,2,-1,-5,7,9],[10,-3,1,-4,-1,1,10,-2,4],[-2,4,-10,-8,-4,-4,6,6,-10]]], dtype = "uint8")#candidate|9947|(5, 12, 9)|const|uint8
var_9948 = relay.var("var_9948", dtype = "uint8", shape = (5, 12, 9))#candidate|9948|(5, 12, 9)|var|uint8
bop_9949 = relay.minimum(const_9947.astype('uint8'), relay.reshape(var_9948.astype('uint8'), relay.shape_of(const_9947))) # shape=(5, 12, 9)
output = bop_9949
output2 = bop_9949
func_9952 = relay.Function([var_9948,], output)
mod['func_9952'] = func_9952
mod = relay.transform.InferType()(mod)
var_9953 = relay.var("var_9953", dtype = "uint8", shape = (5, 12, 9))#candidate|9953|(5, 12, 9)|var|uint8
output = func_9952(var_9953)
func_9954 = relay.Function([var_9953], output)
mutated_mod['func_9954'] = func_9954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9600_call = mod.get_global_var('func_9600')
func_9601_call = mutated_mod.get_global_var('func_9601')
call_9956 = relay.TupleGetItem(func_9600_call(), 0)
call_9957 = relay.TupleGetItem(func_9601_call(), 0)
func_8210_call = mod.get_global_var('func_8210')
func_8212_call = mutated_mod.get_global_var('func_8212')
call_9961 = func_8210_call()
call_9962 = func_8210_call()
output = relay.Tuple([call_9956,call_9961,])
output2 = relay.Tuple([call_9957,call_9962,])
func_9968 = relay.Function([], output)
mod['func_9968'] = func_9968
mod = relay.transform.InferType()(mod)
output = func_9968()
func_9969 = relay.Function([], output)
mutated_mod['func_9969'] = func_9969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4558_call = mod.get_global_var('func_4558')
func_4559_call = mutated_mod.get_global_var('func_4559')
call_9986 = relay.TupleGetItem(func_4558_call(), 0)
call_9987 = relay.TupleGetItem(func_4559_call(), 0)
uop_10010 = relay.atanh(call_9986.astype('float32')) # shape=(4, 11, 16)
uop_10012 = relay.atanh(call_9987.astype('float32')) # shape=(4, 11, 16)
func_6399_call = mod.get_global_var('func_6399')
func_6401_call = mutated_mod.get_global_var('func_6401')
call_10019 = relay.TupleGetItem(func_6399_call(), 3)
call_10020 = relay.TupleGetItem(func_6401_call(), 3)
func_5013_call = mod.get_global_var('func_5013')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_10021 = func_5013_call()
call_10022 = func_5013_call()
func_5432_call = mod.get_global_var('func_5432')
func_5436_call = mutated_mod.get_global_var('func_5436')
const_10040 = relay.const(1, dtype = "uint8")#candidate|10040|()|const|uint8
const_10041 = relay.const([-7.294623,-3.501872,-7.326229,-6.186069,-4.765006,-9.218391,-3.725693,3.949207,7.644747,-2.914752,7.914353,3.121685,-0.844334,-0.127084,2.145891,4.281212,6.719792,-8.523567,-6.088560,0.138461,-6.854214,6.916173,0.052751,-0.905274,2.943735,-9.650050,9.330599,2.373495,-1.426887,7.353117,-1.382425,4.768777,-5.503328,1.323597,1.871823,-1.943954,8.754585,-5.173135,-3.952830,7.570751,-4.432634,-7.408146,-2.748075,4.887048,3.169244,-6.199806,-9.915666,0.423531,2.472374,6.240913,-6.718861,-5.259819,7.651993,-7.924556,-1.861179,4.465399,4.221055,-1.043610,4.647661,-1.702509,-2.694087,-9.775809,9.769404,3.947694,1.738926,1.161762,-4.370476,7.689351,-7.150565,-9.814456,2.295681,5.804586,4.955167,-7.042465,-5.809044,-8.732030,4.671781,1.965402,-3.576088,8.109786,8.310630,0.545693,8.597202,-7.388606,-2.698931,-7.097321,-2.799371,-5.247837,2.564125,7.184716,-5.159817,-9.483153,-3.932224,-6.369486,-2.343965,-9.362144,-3.999734,-8.259553,-6.320838,0.301090,7.316716,0.241241,-8.344840,8.696701,-0.350320,2.062544,-2.326074,3.863549,7.026066,-2.719530,1.863802,9.965272,-4.141322,0.010172,-1.142313,-7.044839,-4.487851,-5.463540,1.667974,-5.291094,-4.515780,-7.919129,6.247297,9.824045,6.191750,5.609234,5.308571,-4.183879,-3.836791,-2.266434,1.314146,-3.341214,-4.130296,-9.887729,-7.112129,-1.314633,-7.551342,-4.592886,-6.830000,-8.017194,9.349836,-1.693612,-3.113787,-2.130986,6.061014,-2.389711,6.050779,-6.502122,0.630385,-7.103033,-6.679609,-6.947644,0.104487,-9.854026,-6.394007,-4.928424,-2.162513,-8.817810,6.554232,8.762423,-1.290298,5.665361,-9.820909,2.168674,-0.481967,-5.221608,-0.626403,9.671965,8.205345,1.819301,-1.803542,2.864193,7.999522,-9.901333,-5.983843,1.098304,3.444426,4.033223,-0.210042,2.345164,-7.453599,4.488422,-8.875493,-6.320925,7.058194,3.802625,9.030631,-4.073583,2.443341,-4.203396,2.336852,-5.906338,-6.823987,-1.199873,-9.128871,-6.223349,2.935346,-2.795729,-0.795894,0.640240,-4.877411,-5.444632,0.267627,-3.307946,6.355046,3.670910,-9.865215,8.153124,7.601147,-6.285450,2.955560,-4.580733,-2.734476,-5.238839,8.818217,-4.690530,-7.322921,-7.791470,-1.235880,-0.639186,8.325065,-3.363698,8.875234,-1.739784,0.860670,4.733735,5.024307,-3.037031,-9.420482,3.348925,-8.118909,1.631523,-4.728585,0.462217,5.898599,-6.109249,6.348535,-1.381524,-7.220036,1.640881,5.107216,-7.745184,-3.574059,8.306942,3.907049,-5.809133,-1.641511,-1.469924,4.535835,6.813888,-9.658729,1.285547,-7.757983,-2.340332,5.083197,6.231089,-8.566779,9.584520,-8.194617,6.645056,9.045922,6.933619,-4.688899,-4.138925,7.142877,-7.667468,5.810845,5.662409,1.945714,-2.694243,1.132362,-3.336467,1.521405,-7.883775,-1.019386,2.650821,-4.647588,6.629040,9.146888,-7.048338,-9.029852,-4.520023,6.934020,7.352308,0.748007,9.330470,1.105253,2.634086,1.341455,-5.275259,8.128247,-8.808057,9.611852,-4.994230,9.607633,5.159647,8.016331,-4.050504,-9.986104,-5.031363,1.974037,-4.610569,1.217502,-4.962188,-7.411136,-4.778171,-9.880406,3.199575,-4.298093,-5.708242,-4.762969,4.973566,8.573403,-1.702551,-0.879839,-2.878527,-0.469964,-1.776105,-6.795549,5.213395,-6.618040,-9.334181,-7.453234,-4.478898,-0.211499,-5.953184,-5.668076,-4.329647,7.499174,2.209626,8.747357,-2.479536,9.407589,4.152400,5.583562,-0.725318,-1.553016,-7.823522,-2.936182,-4.539701,-4.943943,6.886549,-9.612482,-7.008694,9.744504,0.302249,0.481046,-0.305429,7.884612,-2.907473,-2.556865,-4.842263,-3.527815,3.100527,1.307956,3.442578,2.222066,-8.020984,-4.794506,6.091276,9.550546,8.123876,-7.934648,8.325832,6.078413,-8.715137,-0.565380,2.917273,-6.793294,3.548986,-4.919735,5.030918,7.592613,4.747274,-0.754172,9.387418,-8.350247,7.369955,8.532053,-5.870899,-0.417158,-7.031344,6.097138,1.854052,1.289005,8.469519,6.231077,0.450430,-6.387399,5.101055,1.598414,-9.487696,2.446595,6.626806,-6.657995,8.451405,-4.803620,5.833854,4.943124,2.658903,4.258834,-0.629046,3.331515,-9.167639,8.472656,4.207798,-0.429172,-8.971583,8.303098,-1.731797,0.874636,-1.633820,-4.526292,2.552394,7.734536,-7.180228,9.155054,3.019604,-7.079082,-3.126041,2.614414,-0.359903,-4.824874,5.998437,-0.204853,9.617642,-1.320043,-5.584937,-0.044297,-7.011244,-8.285713,-9.248880,-6.060968,7.476421,4.975351,-9.978582,7.896079,1.107671,2.800309,5.061794,-8.453653,6.240130,-2.380850,6.507497,9.734885,-7.538730,-8.952475,5.421611,1.460482,4.301647,-1.339692,0.579515,5.712645,0.786274,-9.934143,-9.759931,-6.663108,3.482089,2.337969,7.215147,-7.704728,1.540749,-8.281156,6.943407,2.189513,5.852349,-6.254053,0.923904,7.842236,-3.562203,2.307024,-2.936954,-9.089889,-8.803713,3.314955,-7.910786,-8.493902,-1.167995,-7.286448,-3.990399,9.894882,-6.761121,-1.966560,5.260318,-8.966600,0.957992,-8.003473,8.025408,4.712214,4.473535,1.705767,3.607923,6.781991,3.500613,0.820342,6.104370,5.447400,6.890725,4.774744,8.816279,-5.469183,1.160541,-8.312376,-4.266705,-2.569403,-6.583109,3.775297,1.603727,-4.080617,2.198145,-5.665682,-8.324978,-8.943663,-3.414103,-4.612848,4.268338,-7.243412,3.372379,-4.664235,5.141473,5.981558,-8.456304,6.841226,6.231723,-0.337671,9.015493,8.514714,-2.017559,5.756638,7.777242,-1.513918,7.010075,5.906563,-0.352195,-3.999255,8.195857,8.915469,-6.472715,2.110927,-5.626638,-9.157730,6.032203,4.863895,2.492654,-6.222467,-3.803001,-9.923388,8.105399,9.100985,9.106398,4.700850,8.260756,-1.916476,3.903591,-9.415832,-8.341553,-1.856635,-4.949455,2.356406,-0.490401,9.092503,8.769621,-5.137793,6.972847,-3.246785,5.371788,5.509857,-4.805695,1.902498,-1.760574,-5.877064,-0.121940,-1.286164,-3.425615,4.716499,4.886447,-4.646228,-8.059172,9.069859,-4.064544,-8.375206,-2.918975,-5.601289,6.813819,-9.121437,1.390904,-6.345818,8.936829,1.787556,4.409126,6.238071,3.507979,0.205999,-3.860199,9.172770,-0.886306,2.839276,-6.432647,1.638410,0.607914,4.786727,-5.687115,-2.865826,-9.822852,-1.050213,-7.471012,-5.602396,2.046510,6.678108,-6.874748,-5.145720,-8.747722,2.979783,0.705962,3.243354,0.558360,-9.457269,-5.543014,0.551798,-8.131580,-6.179515,6.320871,-8.489534,-6.362627,0.659651,-5.814954,7.529265,8.255998,7.096371,-3.066329,0.633148,4.664257,5.728023,-9.022695,-6.443383,-7.248493,-9.937315,3.966470,-4.935314,-3.212376,1.380677,6.721587,-1.107328,7.470440,-9.798847,-6.620277,4.708331,9.264865,7.213276,-6.946615,-2.463029,1.956459,-9.709744,3.236501,-6.973817,-6.195074,-1.101430,9.709471,-5.779224,2.884527,-5.285407,-4.334976,0.619753,-4.560719,-3.210152,2.890150,-5.517569,2.559004,1.078220,7.991090,-2.072597,9.280716,-8.506333,5.962862,-5.276604,0.027943,-1.008500,-3.932518,8.558549,0.107700,5.800565,-5.710990,0.206244,0.420754,-0.763959,-6.870502,-1.293177,3.822636,-9.072835,-4.978798,2.770739,9.900322,6.234826,-3.792160,3.215845,-2.590899,-1.407810,-3.742219,-4.937119,-0.769588,-6.585715,-4.992182,7.422007,6.359587,-4.685914,-2.019314,8.710712,-2.305933,8.787212,6.224000,-3.768982,-4.873516,-2.549344,-4.535796,-6.001703,8.818797,9.814558,5.300807,-5.091061,7.968402,-0.696651,-2.397514,8.940683,1.238628,1.736457,6.816737,-5.028862,-9.539681,-0.424108,-6.680507,-9.337270,-2.699345,1.668006,-5.563162,-9.336885,-0.843005,5.538278,1.481663,7.348825,1.262263,7.124952,-2.800540,-6.324714,6.260033,4.583649,8.586078,9.795169,-1.482298,-8.950336,-7.011566,-8.488190,1.087566,-9.361194,-2.101631,8.383589,-3.988823,9.812650,0.421285,-1.308807,-8.573435,-9.020885,3.990329,9.131351,-8.688569,-6.488243,4.043959,8.696345,-0.315304,4.035975,-6.548594,-1.373718,5.797692,4.036937,-5.309321,3.217142,-5.408517,-9.996945,-7.197826,4.341418,4.480742,0.791545,-9.995186,-8.731303,-5.046080,4.652634,-7.518762,-9.039548,2.315004,-3.371633,5.466304,5.038002,5.462763,3.391752,8.077940,-3.194238,-2.468305,5.793845,0.438944,5.884881,1.136328,-6.865452,-3.433548,-0.602030,-6.120688,8.778271,-4.950794,6.355742,6.928961,2.748589,7.400187,9.581775,-0.026048,-2.008832,-8.924404,6.411246,3.255924,-8.110674,-6.296437,0.163499,3.695349,-5.666739,3.171277,-5.803031,-6.284233,-5.317732,3.858739,2.875074,-1.135563,3.854092,3.485283,3.112582,-6.097791,3.303856,-6.688708,-1.880836,0.272398,7.363084,-1.878121,6.121632,-0.747066,2.366889,-5.358289,1.179390,-4.978545,9.083679,0.157460,-8.692991,-6.704497,3.350080,7.230153,2.458120,-5.944849,1.470420,-6.011902,-7.545174,-0.909862,-5.553192,-0.850180,-0.267719,1.818815,2.460997,-2.130505,-2.500329,4.722197,5.465422,1.508233,1.075800,6.278063,4.033301,-5.700260,-9.883780,3.419010,9.597771,-1.296537,-5.411423,3.793548,0.038970,-6.952109,4.025404,9.026888,-0.897451,1.054813,-8.349102,-8.082798,-7.179390,7.308076,-9.608410,4.275236,0.787151,0.034837,6.594370,3.936253,-5.808717,8.590002,7.239763,-7.590981,1.313879,8.412705,-5.521841,3.399031,-5.684324,-5.671311,5.115048,-1.964828,8.164788,7.383384,4.785511,1.457240,-2.009486,9.004419,6.582933,3.022112,3.469912,1.461374,-4.477217,-0.345458,0.302834,0.161968,-5.436264,4.115110,8.668754,0.803015,3.970570,-9.566173,1.004868,6.233993,3.096949,2.219214,-6.850107,5.841037,-8.548141,5.294524,-4.688909,-5.785299,9.242843,-8.966250,-3.139961,8.042016,3.135235,5.438552,1.050196,2.422867,3.326703,3.717092,9.932413,3.767904,-1.695346,-8.127211,1.933779,1.010868,-7.221075,-9.689165,3.928682,3.003098,7.285059,8.160045,9.891638,-9.112389,-4.399847,-1.444821,-3.051838,6.043311,7.311847,2.185182,-0.182146,8.820806,-3.279815,-8.830332,4.787538,-7.180215,-5.003259,4.395336,9.253340,9.749605,2.307806,9.725016,1.057134,-5.467882,-0.402042,0.947875,-0.982565,-5.958679,-1.822394,2.809980,-2.922395,3.430202,7.544198,-5.367195,-3.200729,-6.474218,-6.415569,8.515257,-0.947662,-9.455954,5.285897,-0.400304,-0.003268,-3.487807,8.059088,-7.895527,-8.284271,-5.399383,-4.240843,-6.361486,-4.098787,-8.863212,-8.893270,-5.256801,3.694516,-5.529995,1.469141,-4.647559,9.607307,-3.530108,-0.159872,-5.537449,-9.560048,3.702185,2.394637,3.763033,-2.007461,-6.933209,1.753491,-2.635552,2.632870,2.958543,1.628211,-5.308686,8.484834,4.225236,0.243453,-8.801723,-0.228919,-3.385838,3.503083,-4.722395,2.381489,-8.892020,7.232653,1.769091,7.345237,7.177570,3.237959,3.393370,0.540683,-3.611801,-3.597611,-7.928203,-2.753153,6.924988,5.281350,-6.030927,-0.997969,6.174299,5.279315,2.310646,-6.791272,8.865313,-8.629129,-1.611390,8.570565,7.916861,9.230234,-5.458538,-2.266252,2.004456,0.629262,1.637961,-0.609837,-5.083645,2.017603,8.356759,-6.467769,8.153100,1.440680,-1.629762,3.809345,4.855909,-7.825584,-6.976263,6.059552,-6.539837,0.814254,-5.640363,-3.742286,9.742875,-0.248958,7.003982,7.923305,-5.738848,-8.950880,5.029312], dtype = "float64")#candidate|10041|(1092,)|const|float64
call_10039 = relay.TupleGetItem(func_5432_call(relay.reshape(const_10040.astype('uint8'), []), relay.reshape(const_10041.astype('float64'), [546, 2]), ), 1)
call_10042 = relay.TupleGetItem(func_5436_call(relay.reshape(const_10040.astype('uint8'), []), relay.reshape(const_10041.astype('float64'), [546, 2]), ), 1)
output = relay.Tuple([uop_10010,call_10019,call_10021,call_10039,const_10040,const_10041,])
output2 = relay.Tuple([uop_10012,call_10020,call_10022,call_10042,const_10040,const_10041,])
func_10045 = relay.Function([], output)
mod['func_10045'] = func_10045
mod = relay.transform.InferType()(mod)
output = func_10045()
func_10046 = relay.Function([], output)
mutated_mod['func_10046'] = func_10046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1556_call = mod.get_global_var('func_1556')
func_1557_call = mutated_mod.get_global_var('func_1557')
call_10083 = relay.TupleGetItem(func_1556_call(), 0)
call_10084 = relay.TupleGetItem(func_1557_call(), 0)
func_6514_call = mod.get_global_var('func_6514')
func_6517_call = mutated_mod.get_global_var('func_6517')
var_10109 = relay.var("var_10109", dtype = "bool", shape = ())#candidate|10109|()|var|bool
var_10110 = relay.var("var_10110", dtype = "bool", shape = (56, 8))#candidate|10110|(56, 8)|var|bool
call_10108 = relay.TupleGetItem(func_6514_call(relay.reshape(var_10109.astype('bool'), []), relay.reshape(var_10110.astype('bool'), [448,]), ), 2)
call_10111 = relay.TupleGetItem(func_6517_call(relay.reshape(var_10109.astype('bool'), []), relay.reshape(var_10110.astype('bool'), [448,]), ), 2)
func_1488_call = mod.get_global_var('func_1488')
func_1490_call = mutated_mod.get_global_var('func_1490')
call_10116 = relay.TupleGetItem(func_1488_call(), 1)
call_10117 = relay.TupleGetItem(func_1490_call(), 1)
func_2361_call = mod.get_global_var('func_2361')
func_2362_call = mutated_mod.get_global_var('func_2362')
call_10121 = func_2361_call()
call_10122 = func_2361_call()
output = relay.Tuple([call_10083,call_10108,var_10109,var_10110,call_10116,call_10121,])
output2 = relay.Tuple([call_10084,call_10111,var_10109,var_10110,call_10117,call_10122,])
func_10123 = relay.Function([var_10109,var_10110,], output)
mod['func_10123'] = func_10123
mod = relay.transform.InferType()(mod)
mutated_mod['func_10123'] = func_10123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10123_call = mutated_mod.get_global_var('func_10123')
var_10125 = relay.var("var_10125", dtype = "bool", shape = ())#candidate|10125|()|var|bool
var_10126 = relay.var("var_10126", dtype = "bool", shape = (56, 8))#candidate|10126|(56, 8)|var|bool
call_10124 = func_10123_call(var_10125,var_10126,)
output = call_10124
func_10127 = relay.Function([var_10125,var_10126,], output)
mutated_mod['func_10127'] = func_10127
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10135 = relay.var("var_10135", dtype = "int32", shape = ())#candidate|10135|()|var|int32
var_10136 = relay.var("var_10136", dtype = "int32", shape = (6, 12, 11))#candidate|10136|(6, 12, 11)|var|int32
bop_10137 = relay.maximum(var_10135.astype('int32'), var_10136.astype('int32')) # shape=(6, 12, 11)
output = relay.Tuple([bop_10137,])
output2 = relay.Tuple([bop_10137,])
func_10140 = relay.Function([var_10135,var_10136,], output)
mod['func_10140'] = func_10140
mod = relay.transform.InferType()(mod)
mutated_mod['func_10140'] = func_10140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10140_call = mutated_mod.get_global_var('func_10140')
var_10142 = relay.var("var_10142", dtype = "int32", shape = ())#candidate|10142|()|var|int32
var_10143 = relay.var("var_10143", dtype = "int32", shape = (6, 12, 11))#candidate|10143|(6, 12, 11)|var|int32
call_10141 = func_10140_call(var_10142,var_10143,)
output = call_10141
func_10144 = relay.Function([var_10142,var_10143,], output)
mutated_mod['func_10144'] = func_10144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5013_call = mod.get_global_var('func_5013')
func_5015_call = mutated_mod.get_global_var('func_5015')
call_10154 = func_5013_call()
call_10155 = func_5013_call()
func_9383_call = mod.get_global_var('func_9383')
func_9385_call = mutated_mod.get_global_var('func_9385')
call_10171 = relay.TupleGetItem(func_9383_call(), 0)
call_10172 = relay.TupleGetItem(func_9385_call(), 0)
output = relay.Tuple([call_10154,call_10171,])
output2 = relay.Tuple([call_10155,call_10172,])
func_10173 = relay.Function([], output)
mod['func_10173'] = func_10173
mod = relay.transform.InferType()(mod)
output = func_10173()
func_10174 = relay.Function([], output)
mutated_mod['func_10174'] = func_10174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8428_call = mod.get_global_var('func_8428')
func_8429_call = mutated_mod.get_global_var('func_8429')
call_10179 = relay.TupleGetItem(func_8428_call(), 2)
call_10180 = relay.TupleGetItem(func_8429_call(), 2)
output = relay.Tuple([call_10179,])
output2 = relay.Tuple([call_10180,])
func_10187 = relay.Function([], output)
mod['func_10187'] = func_10187
mod = relay.transform.InferType()(mod)
output = func_10187()
func_10188 = relay.Function([], output)
mutated_mod['func_10188'] = func_10188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9759_call = mod.get_global_var('func_9759')
func_9761_call = mutated_mod.get_global_var('func_9761')
call_10214 = func_9759_call()
call_10215 = func_9759_call()
func_6399_call = mod.get_global_var('func_6399')
func_6401_call = mutated_mod.get_global_var('func_6401')
call_10227 = relay.TupleGetItem(func_6399_call(), 0)
call_10228 = relay.TupleGetItem(func_6401_call(), 0)
func_8955_call = mod.get_global_var('func_8955')
func_8958_call = mutated_mod.get_global_var('func_8958')
const_10232 = relay.const([8,-9,4,-3,-4,-8,10,1,-6,-8,5,-4,-2,9,7,-2,-6,9,7,-10,7,-5,-5,-6,1,4,3,5,10,-1,-10,1,4,-9,-1,1,6,-5,-4,1,-9,3,4,9,4,10,-3,-3,10,9,10,9,7,6,-7,9,4,7,-2,2,8,-1,1,-9,7,-2,9,-2,7,8,-6,1,-10,8,7,-1,9,8,-7,3,-7,8,8,2,9,1,-8,-5,-1,4,2,2,7,-3,9,8,-5,-3,8,10,5,3,2,-4,3,-10,3,-6,6,-7,-9,2,-1,7,-10,9,8,1,-1,2,2,9,-6,8,-6,6,9,-9,2,-4,-3,-8,-6,-1,-3,-3,7,-2,8,-4,6,10,-9,-10,5,5,-6,10,-1,8,-6,-1,-4,-7,-7,-7,-2,-10,3,3,-3,-7,1,-8,-10,8,-9,8,-4,-6,-7,-5,9,9,-5,-2,-1,5,6,-4,-2,-2,-3,-6,7,-7,-6,-3,-8,-7,-7,9,-7,9,10,2,8,-6,-8,8,-8,-10,-9,-7,7,10,-2,1,-5,-5,-8,10,-2,-6,1,-6,1,1,-10,7,-2,-1,-7,-6,-5,-1,9,-8,8,-3,-10,-5,-6,-2,-7,-4,-7,-5,-7,9,3,4,9,-3,6,5,-9,-8,9,3,-9,6,4,-2,-2,3,-1,7,9,-9,8,-8,8,-3,-5,2,-3,-2,10,8,-7,9,-9,9,8,10,6,2,5,-9,-2,-6,1,-4,4,-7,4,-10,-2,-1,-9,-6,-1,6,-6,8,-10,-2,2,4,-7,-8,4,-6,-7,7,-7,2,3,-4,5,-4,-4,-5,-4,6,-9,6,4,-2,-6,8,1,-1,-8,-3,5,-7,6,9,1,3,10,3,-1,7,-3,-1,5,-1,5,5,1,-2,1,9,7,-2,-3,-2,-10,-2,-4,-9,4,-1,4,-2,-7,2,-6,-10,2,1,-6,10,2,9,4,4,-6,9,-10,-4,3,-4,6,-1,7,6,5,-9,7,-2,4,8,-10,9,-8,-6,1,-10,-6,-9,-3,6,2,-2,3,-9,1,-6,-6,2,2,-5,-9,-9,-5,8,3,3,-9,-4,2,-9,5,-5,-4,5,6,6,4,-10,6,-7,4,-4,-7,-7,-4,-2,-4,9,4,4,3,-5,9,-8,-7,-4,4,-6,-6,10,1,-6,8,7,-9,-2,-2,1,-4,4,5,2,6,10,1,2,3,1,5,-3,-8,9,4,1,1,7,3,-5,7,1,-9,-4,-2,4,-2,2,-4,1,-2,-5,-6,-1,2,-8,-1,-9,-3,-3,-7,-2,7,-10,-8,-10,1,-5,8,8,10,-10,-8,-3,9,5,6,4,5,4,-5,4,-10,5,-5,-7,-2,7,-6,-10,-8,-3,-6,8,1,5,-8,3,9,5,2,8,1,-3,-8,3,8,2,3,5,4,1,10,8,-4,1,7,10,-5,-6,-6,8,-3,9,-2,1,4,-6,5,-4,-8,-5,-6,-6,7,-3,1,6,4,1,10,10,3,10,1,-7,1,-8,6,-8,-6,-6,2,2,-9,-2,4,-5,-9,4,-1,10,4,8,10,5,-7,-4,4,7,-8,2,-10,-10,2,-8,7,-6,4,5,10,-3,-10,7,2,9,2,3,-10,2,6,-6,8,6,-6,7,10,2,-6,5,-5,-7,8,1,-2,2,3,-1,-8,4,-9,-9,-10,8,-1,3,1,-5,1,-9,-8,-10,-6,3,-9,7,7,-6,8,2,-1,5,6,-1,5,7,10,6,8,2,-6,5,7,-10,-7,4,9,10,-9,-2,2,10,7,-9,-7,4,10,-9,-3,1,3,-10,5,8,2,2,9,7,8,-1,-7,-10,-4,-5,8,-9,-1,3,-8,2,3,3,6,8,-5,10,-5,10,-7,-8,-9,6,-7,-6,2,-2,-1,-6,6,10,-4,3,1,1,-6,-5,-10,-7,-1,-10,2,-9,9,-10,1,6,10,-7,3,-9,8,6,-6,-3,-7,-2,-6,-1,-6,2,1,-3,7,4,-9,-1,-8,5,1,10,2,4,-3,-5,-8,-8,-4,1,-10,-3,9,-6,-10,-8,-10,8,2,-1,9,-8,2,-7,7,-10,-5,6,7,-9,-4,10,9,7,10,-8,4,7,10,-2,1,3,-5,10,-2,10,9,-1,10,10,6,10,-2,7,10,-8,-3,9,-2,1,9,2,-3,-6,3,-2,2,10,-6,7,-10,7,7,-1,-6,-5,-6,-4,-1,2,6,2,6,3,3,-10,-8,4,2,6,-2,2,9,-6,6,-4,-2,10,2,-9,-5,6,5,-9,-9,-6,6,-6,-6,5,2,4,-8,9,-10,-5,-9,-8,-2,3,4,2,-7,-6,3,-5,-5,-9,5,-4,-8,10,1,4,-7,-7,-6,2,9,8,-1,9,4,-8,-5,2,3,-3,-1,8,-1,8,5,-1,-10,-8,-4,9,-2,6,1,-1,1,-7,-10,-10,-1,10,-10,10,-2,3,3,3,-10,5,7,4,-9,-8,-9,1,9,-5,2,1,6,-9,7,-6,-1,6,6,-5,4,-5,-4,-2,8,3,5,-6,-9,9,7,1,-6,-7,1,-7,-7,-10,1,-7,-1,10,4,6,1,7,3,-7,9,1,-5,-6,5,7,-8,-6,3,-5,-4,-10,10,-6,-9,4,-6,-7,7,5,-9,-7,-7,6,-1,-8,-3,1,-8,-8,9,-3,7,7,-3,-4,-7,9,-6,-5,-7,-1,1,-6,10,-8,-6,-3,2,6,2,-10,-3,-4,-6,-5,2,-5,-1,-4,7,-7,4,5,-9,1,-1,4,-2,4,-5,-2,6,-2,2,-7,9,-1,5,8,5,7,2,3,-8,-3,7,-4,7,-9,5,6,-9,8,3,9,-5,5,8,3,-6,-2,6,-5,3,9,-9,1,-4,-3,5,6,-8,9,-10,3,1,-6,-1,-9,4,-10,5,-4,-10,-7,-8,-5,3,-4,6,-8,1,3,6,6,-10,-4,10,5,4,3,6,-2,-1,3,-2,-6,6,6,-3,-3,-1,-9,6,8,-7,-3,10,1,2,1,-6,8,8,5,8,-6,6,9,1,-1,-10,-1,-2,6,-8,-7,-5,6,8,-7,-1,5,-8,7,-2,6,-5,-4,1,10,-6,4,9,-5,3,-5,-4,-10,-5,-10,9,10,-6,10,4,-7,-6,-4,-10,4,-2,8,1,8,8,2,-7,1,7,-1,3,5,-8,6,9,-3,-1,7,-8,-6,7,2,-2,-7,4,2,-5,-7,-6,-1,3,6,-5,-3,-1,9,-1,-2,-6,2,5,9,2,3,7,5,-7,3,5,7,9,4,9,-2,2,-4,1,9,9,1,5,7,8,-6,-10,-1,-8,-10,10,1,10,-3,9,2,3,6,-1,1,-5,-4,-1,5,-9,-8,8,3,5,9,-7,3,-8,9,4,-1,-1,5,8,-3,4,8,-9,4,-8,-9,5,6,-3,-3,4,-5,6,7,9,-3,-1,6,1,-5,2,3,-8,-9,3,-7,5,-2,-9,5,10,10,8,-3,-8,5,4,7,6,-4,-9,5,-2,-5,9,10], dtype = "int8")#candidate|10232|(1350,)|const|int8
call_10231 = func_8955_call(relay.reshape(const_10232.astype('int8'), [10, 15, 9]))
call_10233 = func_8955_call(relay.reshape(const_10232.astype('int8'), [10, 15, 9]))
output = relay.Tuple([call_10214,call_10227,call_10231,const_10232,])
output2 = relay.Tuple([call_10215,call_10228,call_10233,const_10232,])
func_10241 = relay.Function([], output)
mod['func_10241'] = func_10241
mod = relay.transform.InferType()(mod)
output = func_10241()
func_10242 = relay.Function([], output)
mutated_mod['func_10242'] = func_10242
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10269 = relay.const([[[4,-7,-2,3,-4,-4,4,-3,3,3,-9,-8],[1,-7,2,2,-9,-2,-4,2,-9,-9,4,-10],[-8,-6,-10,-5,-6,-9,4,-6,-10,3,-5,-4],[-3,7,-6,6,-8,2,9,-10,10,5,3,-6],[-10,-7,-5,-9,-5,-8,3,-5,-8,-2,-4,2],[-2,-7,-6,7,3,-3,6,-9,-10,2,-2,-6],[-3,7,-1,-1,-4,9,3,-10,-2,7,4,-1],[-4,10,1,4,6,-3,-10,1,5,8,6,6]],[[-10,7,10,10,10,-10,8,5,7,1,2,-5],[-2,5,-10,7,6,4,2,10,6,3,5,-5],[5,2,-8,6,-10,7,4,10,7,-5,-9,-3],[6,8,5,6,1,-9,6,8,-6,4,8,9],[-9,6,-1,3,-8,-1,-6,5,8,6,-1,8],[7,9,-9,3,-5,3,2,5,9,-3,6,2],[-1,-8,3,2,-1,7,9,5,1,-2,-6,-2],[-5,-1,2,7,-4,-8,10,-6,8,10,-5,1]],[[-2,10,-10,-4,7,9,1,-3,-10,1,-8,10],[2,3,-4,-5,9,-8,-8,-5,-10,-4,-10,-5],[9,-10,-2,-5,2,-2,-4,5,-4,2,5,-9],[-4,5,2,-2,-3,8,-5,-8,10,-3,8,-10],[9,4,-1,-9,8,9,-4,-10,5,10,10,-7],[1,9,-10,-2,10,4,-1,-4,-7,-8,4,-7],[6,1,9,-10,-9,-10,7,7,9,7,-4,-8],[6,5,-4,10,-2,-9,8,1,-8,6,2,3]],[[7,-1,2,6,-7,-7,3,-2,10,-8,-1,-8],[2,4,-9,7,-6,-7,-10,-6,1,-6,3,-1],[-9,3,-8,1,-7,3,-4,2,-1,-8,-1,5],[-8,-8,1,5,-8,10,-9,5,-7,-2,1,1],[-2,-10,-3,-6,-8,-3,-4,8,7,10,-10,4],[5,8,-1,-7,-8,-7,-4,2,-7,-10,3,5],[-10,8,9,-9,1,2,6,6,-8,7,-3,-3],[-5,-3,5,-10,2,4,3,8,1,-5,-9,1]],[[3,-9,-8,-7,7,3,8,4,-3,-3,-2,-2],[3,9,8,9,-9,-8,-1,10,-4,10,6,4],[-4,6,10,-8,5,4,9,-7,-2,-5,-9,-10],[6,7,-4,1,-7,-6,5,1,3,-7,3,-1],[10,-7,-1,-4,-7,-8,1,10,6,-7,2,-5],[7,7,6,4,-6,-5,-10,-3,-7,9,-8,-7],[5,-7,4,-1,-2,1,-10,5,8,2,-8,-4],[-6,4,3,10,5,-6,7,-4,-10,10,1,-6]]], dtype = "uint64")#candidate|10269|(5, 8, 12)|const|uint64
var_10270 = relay.var("var_10270", dtype = "uint64", shape = (5, 8, 12))#candidate|10270|(5, 8, 12)|var|uint64
bop_10271 = relay.add(const_10269.astype('uint64'), relay.reshape(var_10270.astype('uint64'), relay.shape_of(const_10269))) # shape=(5, 8, 12)
uop_10278 = relay.erf(var_10270.astype('float32')) # shape=(5, 8, 12)
func_4869_call = mod.get_global_var('func_4869')
func_4871_call = mutated_mod.get_global_var('func_4871')
call_10291 = relay.TupleGetItem(func_4869_call(), 3)
call_10292 = relay.TupleGetItem(func_4871_call(), 3)
func_6868_call = mod.get_global_var('func_6868')
func_6869_call = mutated_mod.get_global_var('func_6869')
call_10294 = relay.TupleGetItem(func_6868_call(), 3)
call_10295 = relay.TupleGetItem(func_6869_call(), 3)
output = relay.Tuple([bop_10271,uop_10278,call_10291,call_10294,])
output2 = relay.Tuple([bop_10271,uop_10278,call_10292,call_10295,])
func_10302 = relay.Function([var_10270,], output)
mod['func_10302'] = func_10302
mod = relay.transform.InferType()(mod)
mutated_mod['func_10302'] = func_10302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10303 = relay.var("var_10303", dtype = "uint64", shape = (5, 8, 12))#candidate|10303|(5, 8, 12)|var|uint64
func_10302_call = mutated_mod.get_global_var('func_10302')
call_10304 = func_10302_call(var_10303)
output = call_10304
func_10305 = relay.Function([var_10303], output)
mutated_mod['func_10305'] = func_10305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6558_call = mod.get_global_var('func_6558')
func_6560_call = mutated_mod.get_global_var('func_6560')
call_10322 = func_6558_call()
call_10323 = func_6558_call()
output = call_10322
output2 = call_10323
func_10330 = relay.Function([], output)
mod['func_10330'] = func_10330
mod = relay.transform.InferType()(mod)
mutated_mod['func_10330'] = func_10330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10330_call = mutated_mod.get_global_var('func_10330')
call_10331 = func_10330_call()
output = call_10331
func_10332 = relay.Function([], output)
mutated_mod['func_10332'] = func_10332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7640_call = mod.get_global_var('func_7640')
func_7642_call = mutated_mod.get_global_var('func_7642')
call_10401 = func_7640_call()
call_10402 = func_7640_call()
func_6742_call = mod.get_global_var('func_6742')
func_6744_call = mutated_mod.get_global_var('func_6744')
const_10406 = relay.const([-8,3,-1,-1,4,8,7,8,9,-2,-4,8,-4,6,-10,-8,-4,-8,1,5,-9,-5,-4,-2,1,-4,10,10,-1,-7,-5,-9,10,-5,9,8,-2,-4,-6,-1,-10,-3,7,4,2,-8,8,6,-7,9,-3,-1,10,3,-2,4,-9,4,-10,7,2,7,-5,10,-5,5,7,-3,1,-2,10,5,-1,-9,-7,-1,2,-1,-2,-8,-1,5,8,3,-3,10,-1,5,4,-2,-10,4,-2,10,7,1,8,-3,5,6,1,3,1,-5,-2,9,-2,6,7,8,-4,9,-6,-10,8,-8,2,-4,-9,-9,6,7,-1,1,-10,2,-9,-8,5,7,2,4,-9,6,-7,-1,4,-10,2,5,-10,6,9,-6,1,-8,9,8,2,7,10,-4,-7,-3,6,9,-4,7,10,-8,7,4,9,5,6,3,-10,-4,1,-6,-5,5,1,-5,-5,1,-10,-9,9,-2,-6,2,-4,-2,4,-4,-4,-8,-2,5,-7,-1], dtype = "uint64")#candidate|10406|(192,)|const|uint64
call_10405 = relay.TupleGetItem(func_6742_call(relay.reshape(const_10406.astype('uint64'), [2, 8, 12])), 0)
call_10407 = relay.TupleGetItem(func_6744_call(relay.reshape(const_10406.astype('uint64'), [2, 8, 12])), 0)
func_7098_call = mod.get_global_var('func_7098')
func_7100_call = mutated_mod.get_global_var('func_7100')
call_10438 = relay.TupleGetItem(func_7098_call(), 1)
call_10439 = relay.TupleGetItem(func_7100_call(), 1)
func_2937_call = mod.get_global_var('func_2937')
func_2939_call = mutated_mod.get_global_var('func_2939')
call_10440 = relay.TupleGetItem(func_2937_call(), 3)
call_10441 = relay.TupleGetItem(func_2939_call(), 3)
func_10140_call = mod.get_global_var('func_10140')
func_10144_call = mutated_mod.get_global_var('func_10144')
const_10446 = relay.const(3, dtype = "int32")#candidate|10446|()|const|int32
var_10447 = relay.var("var_10447", dtype = "int32", shape = (792,))#candidate|10447|(792,)|var|int32
call_10445 = relay.TupleGetItem(func_10140_call(relay.reshape(const_10446.astype('int32'), []), relay.reshape(var_10447.astype('int32'), [6, 12, 11]), ), 0)
call_10448 = relay.TupleGetItem(func_10144_call(relay.reshape(const_10446.astype('int32'), []), relay.reshape(var_10447.astype('int32'), [6, 12, 11]), ), 0)
func_9593_call = mod.get_global_var('func_9593')
func_9595_call = mutated_mod.get_global_var('func_9595')
call_10452 = func_9593_call()
call_10453 = func_9593_call()
output = relay.Tuple([call_10401,call_10405,const_10406,call_10438,call_10440,call_10445,const_10446,var_10447,call_10452,])
output2 = relay.Tuple([call_10402,call_10407,const_10406,call_10439,call_10441,call_10448,const_10446,var_10447,call_10453,])
func_10463 = relay.Function([var_10447,], output)
mod['func_10463'] = func_10463
mod = relay.transform.InferType()(mod)
mutated_mod['func_10463'] = func_10463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10464 = relay.var("var_10464", dtype = "int32", shape = (792,))#candidate|10464|(792,)|var|int32
func_10463_call = mutated_mod.get_global_var('func_10463')
call_10465 = func_10463_call(var_10464)
output = call_10465
func_10466 = relay.Function([var_10464], output)
mutated_mod['func_10466'] = func_10466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3359_call = mod.get_global_var('func_3359')
func_3360_call = mutated_mod.get_global_var('func_3360')
call_10557 = func_3359_call()
call_10558 = func_3359_call()
output = relay.Tuple([call_10557,])
output2 = relay.Tuple([call_10558,])
func_10568 = relay.Function([], output)
mod['func_10568'] = func_10568
mod = relay.transform.InferType()(mod)
output = func_10568()
func_10569 = relay.Function([], output)
mutated_mod['func_10569'] = func_10569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6086_call = mod.get_global_var('func_6086')
func_6087_call = mutated_mod.get_global_var('func_6087')
call_10592 = relay.TupleGetItem(func_6086_call(), 0)
call_10593 = relay.TupleGetItem(func_6087_call(), 0)
output = relay.Tuple([call_10592,])
output2 = relay.Tuple([call_10593,])
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
const_10609 = relay.const([[[6.572584,3.189987,7.470885,-2.878848,-4.811784,8.938900,-4.601281,-0.392024,-0.069924,7.103009,-9.551571,5.741256,-9.457671,-5.370495,0.914915],[-4.808493,8.790605,-1.850850,-2.974674,-2.086914,-4.473352,-7.734536,-9.417943,-7.468378,8.602266,7.348241,7.820039,8.997208,-5.269147,3.200239],[7.337380,-7.764368,-2.572066,1.801216,2.404439,2.795551,-5.847113,-3.900130,-3.852266,2.321030,4.177447,7.934747,-3.212777,-8.500137,1.398880],[-5.318980,6.058574,9.313857,6.861659,5.550829,-3.524806,-5.339369,-9.691550,-0.711450,9.375748,-2.821058,-6.268272,4.896151,-7.038141,3.695130],[-7.125473,-8.661777,-4.944617,6.133438,5.632396,-7.273731,7.142275,-1.608373,2.907651,-3.078336,-4.605960,6.245035,7.267784,8.028425,-6.318966],[5.967037,-4.143953,3.354819,3.455839,-8.138594,7.378497,6.024363,-8.381236,-3.802372,-7.945093,-2.248876,2.065476,0.195734,2.529603,-7.206446]]], dtype = "float64")#candidate|10609|(1, 6, 15)|const|float64
uop_10610 = relay.atanh(const_10609.astype('float64')) # shape=(1, 6, 15)
output = relay.Tuple([uop_10610,])
output2 = relay.Tuple([uop_10610,])
func_10618 = relay.Function([], output)
mod['func_10618'] = func_10618
mod = relay.transform.InferType()(mod)
output = func_10618()
func_10619 = relay.Function([], output)
mutated_mod['func_10619'] = func_10619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10568_call = mod.get_global_var('func_10568')
func_10569_call = mutated_mod.get_global_var('func_10569')
call_10625 = relay.TupleGetItem(func_10568_call(), 0)
call_10626 = relay.TupleGetItem(func_10569_call(), 0)
output = call_10625
output2 = call_10626
func_10628 = relay.Function([], output)
mod['func_10628'] = func_10628
mod = relay.transform.InferType()(mod)
output = func_10628()
func_10629 = relay.Function([], output)
mutated_mod['func_10629'] = func_10629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7075_call = mod.get_global_var('func_7075')
func_7076_call = mutated_mod.get_global_var('func_7076')
call_10654 = relay.TupleGetItem(func_7075_call(), 2)
call_10655 = relay.TupleGetItem(func_7076_call(), 2)
uop_10681 = relay.rsqrt(call_10654.astype('float32')) # shape=(4, 11, 16)
uop_10683 = relay.rsqrt(call_10655.astype('float32')) # shape=(4, 11, 16)
output = uop_10681
output2 = uop_10683
func_10689 = relay.Function([], output)
mod['func_10689'] = func_10689
mod = relay.transform.InferType()(mod)
mutated_mod['func_10689'] = func_10689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10689_call = mutated_mod.get_global_var('func_10689')
call_10690 = func_10689_call()
output = call_10690
func_10691 = relay.Function([], output)
mutated_mod['func_10691'] = func_10691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5219_call = mod.get_global_var('func_5219')
func_5221_call = mutated_mod.get_global_var('func_5221')
call_10692 = relay.TupleGetItem(func_5219_call(), 0)
call_10693 = relay.TupleGetItem(func_5221_call(), 0)
func_4375_call = mod.get_global_var('func_4375')
func_4377_call = mutated_mod.get_global_var('func_4377')
call_10699 = relay.TupleGetItem(func_4375_call(), 1)
call_10700 = relay.TupleGetItem(func_4377_call(), 1)
output = relay.Tuple([call_10692,call_10699,])
output2 = relay.Tuple([call_10693,call_10700,])
func_10710 = relay.Function([], output)
mod['func_10710'] = func_10710
mod = relay.transform.InferType()(mod)
mutated_mod['func_10710'] = func_10710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10710_call = mutated_mod.get_global_var('func_10710')
call_10711 = func_10710_call()
output = call_10711
func_10712 = relay.Function([], output)
mutated_mod['func_10712'] = func_10712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10241_call = mod.get_global_var('func_10241')
func_10242_call = mutated_mod.get_global_var('func_10242')
call_10736 = relay.TupleGetItem(func_10241_call(), 3)
call_10737 = relay.TupleGetItem(func_10242_call(), 3)
func_6595_call = mod.get_global_var('func_6595')
func_6596_call = mutated_mod.get_global_var('func_6596')
call_10740 = relay.TupleGetItem(func_6595_call(), 0)
call_10741 = relay.TupleGetItem(func_6596_call(), 0)
output = relay.Tuple([call_10736,call_10740,])
output2 = relay.Tuple([call_10737,call_10741,])
func_10747 = relay.Function([], output)
mod['func_10747'] = func_10747
mod = relay.transform.InferType()(mod)
output = func_10747()
func_10748 = relay.Function([], output)
mutated_mod['func_10748'] = func_10748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5309_call = mod.get_global_var('func_5309')
func_5310_call = mutated_mod.get_global_var('func_5310')
call_10770 = relay.TupleGetItem(func_5309_call(), 0)
call_10771 = relay.TupleGetItem(func_5310_call(), 0)
output = call_10770
output2 = call_10771
func_10772 = relay.Function([], output)
mod['func_10772'] = func_10772
mod = relay.transform.InferType()(mod)
mutated_mod['func_10772'] = func_10772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10772_call = mutated_mod.get_global_var('func_10772')
call_10773 = func_10772_call()
output = call_10773
func_10774 = relay.Function([], output)
mutated_mod['func_10774'] = func_10774
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10788 = relay.const([[[3.223715,-8.679667,7.507157],[-9.352645,-3.803627,-9.300205],[2.282991,-0.052598,-8.515438],[-6.265278,-6.789136,-6.435026],[8.718627,-9.213713,7.392192],[-1.228316,7.838849,3.955478]],[[0.026807,-1.990791,8.229193],[9.591272,-0.473774,3.150234],[7.213540,9.005706,-5.000936],[-2.476930,-8.031085,8.587064],[5.601545,-2.100370,-3.938283],[7.967403,7.884247,8.526326]],[[-1.654624,1.380978,5.595740],[4.078614,5.174797,-7.144495],[-0.656849,3.199825,9.340068],[-5.936937,1.071350,1.360589],[5.411817,1.597755,-9.326047],[5.661880,-8.140717,2.361707]],[[7.642715,-8.860371,8.402036],[5.127247,2.140118,-8.495742],[7.000882,9.019358,-1.385541],[-8.838726,4.028358,-1.096941],[-6.174734,-6.446587,9.119454],[-3.237259,-9.906312,9.077724]]], dtype = "float32")#candidate|10788|(4, 6, 3)|const|float32
uop_10789 = relay.atan(const_10788.astype('float32')) # shape=(4, 6, 3)
output = relay.Tuple([uop_10789,])
output2 = relay.Tuple([uop_10789,])
func_10798 = relay.Function([], output)
mod['func_10798'] = func_10798
mod = relay.transform.InferType()(mod)
mutated_mod['func_10798'] = func_10798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10798_call = mutated_mod.get_global_var('func_10798')
call_10799 = func_10798_call()
output = call_10799
func_10800 = relay.Function([], output)
mutated_mod['func_10800'] = func_10800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2714_call = mod.get_global_var('func_2714')
func_2715_call = mutated_mod.get_global_var('func_2715')
call_10801 = func_2714_call()
call_10802 = func_2714_call()
func_6541_call = mod.get_global_var('func_6541')
func_6542_call = mutated_mod.get_global_var('func_6542')
call_10828 = func_6541_call()
call_10829 = func_6541_call()
output = relay.Tuple([call_10801,call_10828,])
output2 = relay.Tuple([call_10802,call_10829,])
func_10834 = relay.Function([], output)
mod['func_10834'] = func_10834
mod = relay.transform.InferType()(mod)
output = func_10834()
func_10835 = relay.Function([], output)
mutated_mod['func_10835'] = func_10835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10849 = relay.var("var_10849", dtype = "float32", shape = (10, 2, 5))#candidate|10849|(10, 2, 5)|var|float32
uop_10850 = relay.sqrt(var_10849.astype('float32')) # shape=(10, 2, 5)
const_10862 = relay.const([[[-2.501562,-1.966973,-8.541478,-2.772194,9.799319],[5.919662,-6.039513,-4.141297,4.843134,0.512486]],[[-0.561682,9.233985,-6.031818,6.183790,4.457072],[4.237972,6.711962,-4.817654,5.725084,2.577556]],[[-6.297844,-7.140479,-7.543112,1.774436,-8.059113],[-5.023727,-7.028464,5.623037,-4.949711,4.387999]],[[2.574787,7.186477,-0.084312,7.697196,-3.242207],[-6.354869,3.153780,-6.874671,9.080358,2.077482]],[[-3.316153,-0.765822,2.777795,4.394133,1.312144],[-6.051483,4.177087,7.074955,8.499874,6.691965]],[[4.761336,-1.415858,-9.293918,-7.287253,3.931943],[6.017022,1.030151,-1.731324,2.265705,-3.920839]],[[9.951000,-1.752631,1.249657,-2.494761,-2.440904],[-5.390381,-2.885275,-6.288048,6.974336,-5.520625]],[[-8.542166,-0.973192,-2.698186,-6.005800,-2.962003],[-1.693706,1.826286,-1.707395,-2.067578,8.502671]],[[5.490089,-9.965499,3.729270,-4.611017,9.110123],[9.764034,1.758621,9.399761,-3.804065,6.791408]],[[-1.897982,-2.053461,-6.362545,-2.393964,-4.353615],[3.213087,-1.983975,7.558923,-8.727793,-6.287435]]], dtype = "float32")#candidate|10862|(10, 2, 5)|const|float32
bop_10863 = relay.not_equal(uop_10850.astype('bool'), relay.reshape(const_10862.astype('bool'), relay.shape_of(uop_10850))) # shape=(10, 2, 5)
output = relay.Tuple([bop_10863,])
output2 = relay.Tuple([bop_10863,])
func_10866 = relay.Function([var_10849,], output)
mod['func_10866'] = func_10866
mod = relay.transform.InferType()(mod)
mutated_mod['func_10866'] = func_10866
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10867 = relay.var("var_10867", dtype = "float32", shape = (10, 2, 5))#candidate|10867|(10, 2, 5)|var|float32
func_10866_call = mutated_mod.get_global_var('func_10866')
call_10868 = func_10866_call(var_10867)
output = call_10868
func_10869 = relay.Function([var_10867], output)
mutated_mod['func_10869'] = func_10869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10187_call = mod.get_global_var('func_10187')
func_10188_call = mutated_mod.get_global_var('func_10188')
call_10879 = relay.TupleGetItem(func_10187_call(), 0)
call_10880 = relay.TupleGetItem(func_10188_call(), 0)
uop_10885 = relay.log2(call_10879.astype('float32')) # shape=(3, 104)
uop_10887 = relay.log2(call_10880.astype('float32')) # shape=(3, 104)
var_10892 = relay.var("var_10892", dtype = "float32", shape = (3, 104))#candidate|10892|(3, 104)|var|float32
bop_10893 = relay.right_shift(uop_10885.astype('int32'), relay.reshape(var_10892.astype('int32'), relay.shape_of(uop_10885))) # shape=(3, 104)
bop_10896 = relay.right_shift(uop_10887.astype('int32'), relay.reshape(var_10892.astype('int32'), relay.shape_of(uop_10887))) # shape=(3, 104)
func_8328_call = mod.get_global_var('func_8328')
func_8330_call = mutated_mod.get_global_var('func_8330')
call_10904 = relay.TupleGetItem(func_8328_call(), 0)
call_10905 = relay.TupleGetItem(func_8330_call(), 0)
output = relay.Tuple([bop_10893,call_10904,])
output2 = relay.Tuple([bop_10896,call_10905,])
func_10906 = relay.Function([var_10892,], output)
mod['func_10906'] = func_10906
mod = relay.transform.InferType()(mod)
mutated_mod['func_10906'] = func_10906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10907 = relay.var("var_10907", dtype = "float32", shape = (3, 104))#candidate|10907|(3, 104)|var|float32
func_10906_call = mutated_mod.get_global_var('func_10906')
call_10908 = func_10906_call(var_10907)
output = call_10908
func_10909 = relay.Function([var_10907], output)
mutated_mod['func_10909'] = func_10909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8276_call = mod.get_global_var('func_8276')
func_8278_call = mutated_mod.get_global_var('func_8278')
call_10955 = relay.TupleGetItem(func_8276_call(), 1)
call_10956 = relay.TupleGetItem(func_8278_call(), 1)
output = call_10955
output2 = call_10956
func_10957 = relay.Function([], output)
mod['func_10957'] = func_10957
mod = relay.transform.InferType()(mod)
output = func_10957()
func_10958 = relay.Function([], output)
mutated_mod['func_10958'] = func_10958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10187_call = mod.get_global_var('func_10187')
func_10188_call = mutated_mod.get_global_var('func_10188')
call_10978 = relay.TupleGetItem(func_10187_call(), 0)
call_10979 = relay.TupleGetItem(func_10188_call(), 0)
var_10980 = relay.var("var_10980", dtype = "bool", shape = (3, 104))#candidate|10980|(3, 104)|var|bool
bop_10981 = relay.floor_divide(call_10978.astype('float64'), relay.reshape(var_10980.astype('float64'), relay.shape_of(call_10978))) # shape=(3, 104)
bop_10984 = relay.floor_divide(call_10979.astype('float64'), relay.reshape(var_10980.astype('float64'), relay.shape_of(call_10979))) # shape=(3, 104)
func_7843_call = mod.get_global_var('func_7843')
func_7846_call = mutated_mod.get_global_var('func_7846')
var_10986 = relay.var("var_10986", dtype = "float64", shape = (495, 1))#candidate|10986|(495, 1)|var|float64
call_10985 = func_7843_call(relay.reshape(var_10986.astype('float64'), [11, 3, 15]))
call_10987 = func_7843_call(relay.reshape(var_10986.astype('float64'), [11, 3, 15]))
var_10988 = relay.var("var_10988", dtype = "float64", shape = (495, 7))#candidate|10988|(495, 7)|var|float64
bop_10989 = relay.divide(var_10986.astype('float32'), var_10988.astype('float32')) # shape=(495, 7)
uop_10992 = relay.erf(bop_10989.astype('float32')) # shape=(495, 7)
output = relay.Tuple([bop_10981,call_10985,uop_10992,])
output2 = relay.Tuple([bop_10984,call_10987,uop_10992,])
F = relay.Function([var_10980,var_10986,var_10988,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10980,var_10986,var_10988,], output2)
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
