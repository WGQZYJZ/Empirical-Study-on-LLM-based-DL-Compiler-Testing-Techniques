import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_119 = relay.var("var_119", dtype = "float64", shape = (14, 2, 12))#candidate|119|(14, 2, 12)|var|float64
uop_120 = relay.log2(var_119.astype('float64')) # shape=(14, 2, 12)
output = uop_120
output2 = uop_120
func_123 = relay.Function([var_119,], output)
mod['func_123'] = func_123
mod = relay.transform.InferType()(mod)
var_124 = relay.var("var_124", dtype = "float64", shape = (14, 2, 12))#candidate|124|(14, 2, 12)|var|float64
output = func_123(var_124)
func_125 = relay.Function([var_124], output)
mutated_mod['func_125'] = func_125
mutated_mod = relay.transform.InferType()(mutated_mod)
var_140 = relay.var("var_140", dtype = "float32", shape = (6, 3, 11))#candidate|140|(6, 3, 11)|var|float32
uop_141 = relay.tan(var_140.astype('float32')) # shape=(6, 3, 11)
output = relay.Tuple([uop_141,])
output2 = relay.Tuple([uop_141,])
func_149 = relay.Function([var_140,], output)
mod['func_149'] = func_149
mod = relay.transform.InferType()(mod)
var_150 = relay.var("var_150", dtype = "float32", shape = (6, 3, 11))#candidate|150|(6, 3, 11)|var|float32
output = func_149(var_150)
func_151 = relay.Function([var_150], output)
mutated_mod['func_151'] = func_151
mutated_mod = relay.transform.InferType()(mutated_mod)
var_525 = relay.var("var_525", dtype = "uint8", shape = ())#candidate|525|()|var|uint8
const_526 = relay.const([[[-10,-3,1,-6,-3,10,-4,3,8],[-4,3,-8,5,3,1,-8,-5,3],[-4,2,1,-9,7,-6,6,-5,-7],[1,3,6,4,-4,-6,4,7,9],[-6,-5,-4,9,-1,8,-9,2,5],[-5,-1,-9,-7,8,6,4,-10,6],[1,4,2,-2,3,3,9,8,-7],[8,9,-10,5,-9,-4,-7,-2,9]],[[-4,-3,2,-6,3,2,2,-4,3],[-8,-7,-3,3,7,2,-7,4,5],[7,-8,9,2,7,-4,9,1,8],[8,4,7,1,4,6,-3,1,3],[3,-1,1,-3,7,8,-7,-9,4],[-9,-9,-2,2,-8,-9,5,6,2],[-1,-10,10,6,-8,2,-2,-9,-6],[8,6,-3,6,-7,-3,-2,6,5]],[[-1,7,9,-1,10,1,-1,-4,-4],[-4,-4,-7,-3,-3,10,-7,2,-8],[1,9,-9,9,-9,7,-1,-6,-5],[4,-1,-7,5,-1,7,-8,-9,2],[-9,-8,-6,-4,9,2,4,-9,10],[-5,9,-4,5,7,-8,4,9,-8],[8,-2,1,-8,-7,-9,3,6,9],[-10,-1,-10,5,-8,7,-9,-5,1]],[[-2,-2,-6,-10,6,2,-3,2,9],[-4,-8,-9,8,10,-7,-1,10,10],[6,-8,3,10,4,3,-5,-8,-1],[10,2,-3,2,8,7,9,-7,8],[7,-9,9,4,8,1,-6,-9,2],[7,-5,-8,-6,-8,6,-6,-1,3],[6,-5,9,4,-8,6,-4,-6,2],[1,-4,3,-4,-2,2,8,5,2]],[[1,1,-2,9,-2,5,2,-1,7],[-4,-1,-10,4,-2,-1,-2,4,-2],[-2,10,-8,7,-5,6,-4,-4,1],[-1,2,-3,-8,5,-10,-8,-8,6],[5,9,6,1,10,-7,1,-3,9],[-10,-2,-1,-4,3,-9,-9,6,4],[5,-2,-5,3,6,3,-3,4,-7],[-6,-6,-2,-1,9,1,9,-3,9]],[[7,5,10,-1,-10,8,10,8,-6],[10,3,5,5,10,-3,5,2,5],[8,5,-1,-5,9,-8,6,-2,-9],[3,-1,3,3,-7,-10,5,8,-7],[-2,-3,-10,6,1,4,-5,6,-1],[1,9,-9,10,-10,-5,-1,-1,-10],[5,6,-3,6,9,-5,10,-4,-4],[9,-8,-6,6,-2,2,-10,7,1]],[[-6,8,-10,6,9,-1,7,-8,-9],[-10,2,3,-3,10,-9,-7,-9,-10],[10,-9,10,-3,-9,9,-7,-4,10],[-4,-10,-10,7,-4,4,3,4,4],[-1,-8,-10,-8,-8,8,10,1,-8],[9,-10,-10,-10,10,-7,5,-9,-8],[-2,6,1,-7,7,10,-1,-1,-3],[5,5,7,-8,-10,7,-8,6,-8]],[[9,9,5,3,10,7,6,9,7],[-3,-10,4,3,-6,-7,8,-2,-3],[-8,-3,2,-4,-1,-2,-10,-5,-10],[-6,2,-1,-8,6,8,7,8,4],[9,10,2,-8,9,-1,-2,-9,10],[-3,1,-6,-9,-2,-4,-8,-6,-5],[-10,-1,8,-5,8,5,6,-6,-9],[5,-7,6,-5,8,-1,-10,-8,10]],[[-4,6,-1,-1,1,5,10,-10,8],[10,-10,-5,-3,-4,7,-7,-10,-4],[-6,-9,10,8,3,9,-6,5,9],[-7,-6,-3,6,3,-3,-7,1,7],[-10,-1,5,-6,-1,6,-10,10,5],[-8,-3,7,9,-6,-9,-2,-8,-4],[5,3,-1,-5,4,-7,-1,2,-8],[-2,2,-9,-1,-10,8,-9,3,8]]], dtype = "uint8")#candidate|526|(9, 8, 9)|const|uint8
bop_527 = relay.equal(var_525.astype('bool'), const_526.astype('bool')) # shape=(9, 8, 9)
output = bop_527
output2 = bop_527
func_530 = relay.Function([var_525,], output)
mod['func_530'] = func_530
mod = relay.transform.InferType()(mod)
mutated_mod['func_530'] = func_530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_531 = relay.var("var_531", dtype = "uint8", shape = ())#candidate|531|()|var|uint8
func_530_call = mutated_mod.get_global_var('func_530')
call_532 = func_530_call(var_531)
output = call_532
func_533 = relay.Function([var_531], output)
mutated_mod['func_533'] = func_533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1004 = relay.var("var_1004", dtype = "int32", shape = (13, 3, 6))#candidate|1004|(13, 3, 6)|var|int32
var_1005 = relay.var("var_1005", dtype = "int32", shape = (13, 3, 6))#candidate|1005|(13, 3, 6)|var|int32
bop_1006 = relay.less(var_1004.astype('bool'), relay.reshape(var_1005.astype('bool'), relay.shape_of(var_1004))) # shape=(13, 3, 6)
uop_1013 = relay.asin(var_1004.astype('float32')) # shape=(13, 3, 6)
output = relay.Tuple([bop_1006,uop_1013,])
output2 = relay.Tuple([bop_1006,uop_1013,])
func_1015 = relay.Function([var_1004,var_1005,], output)
mod['func_1015'] = func_1015
mod = relay.transform.InferType()(mod)
var_1016 = relay.var("var_1016", dtype = "int32", shape = (13, 3, 6))#candidate|1016|(13, 3, 6)|var|int32
var_1017 = relay.var("var_1017", dtype = "int32", shape = (13, 3, 6))#candidate|1017|(13, 3, 6)|var|int32
output = func_1015(var_1016,var_1017,)
func_1018 = relay.Function([var_1016,var_1017,], output)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1088 = relay.const([[[1.218900,5.475777,7.429687,3.953134,-9.738101,0.417755,5.550786,9.169319]],[[0.301158,1.748062,-5.183783,-2.778488,-2.090219,2.872541,-9.094025,-9.867243]],[[-7.811303,-5.220165,1.111767,9.182763,-1.593706,6.670274,-7.844695,-8.364601]],[[8.987207,-9.666419,-3.530723,0.248995,1.113684,3.010167,8.075888,3.865237]],[[8.197908,7.099412,1.012901,-6.488732,-4.556130,2.643796,-1.572528,-1.028635]],[[7.925680,-6.403650,2.879793,-9.748921,-8.245554,-0.680534,1.226734,1.354647]],[[0.893639,8.917887,4.558181,8.644599,2.699291,-7.571868,-4.773348,5.279200]],[[-8.575318,5.425870,-6.007318,-7.044083,2.285681,-4.705437,-2.654082,9.554817]],[[7.893691,-9.163294,-3.328188,-7.555493,-8.201700,-8.047989,4.118289,-1.184382]]], dtype = "float64")#candidate|1088|(9, 1, 8)|const|float64
uop_1089 = relay.cos(const_1088.astype('float64')) # shape=(9, 1, 8)
output = uop_1089
output2 = uop_1089
func_1097 = relay.Function([], output)
mod['func_1097'] = func_1097
mod = relay.transform.InferType()(mod)
output = func_1097()
func_1098 = relay.Function([], output)
mutated_mod['func_1098'] = func_1098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1107 = relay.var("var_1107", dtype = "float32", shape = (5, 1, 10))#candidate|1107|(5, 1, 10)|var|float32
var_1108 = relay.var("var_1108", dtype = "float32", shape = (5, 4, 10))#candidate|1108|(5, 4, 10)|var|float32
bop_1109 = relay.mod(var_1107.astype('float32'), var_1108.astype('float32')) # shape=(5, 4, 10)
output = bop_1109
output2 = bop_1109
func_1112 = relay.Function([var_1107,var_1108,], output)
mod['func_1112'] = func_1112
mod = relay.transform.InferType()(mod)
var_1113 = relay.var("var_1113", dtype = "float32", shape = (5, 1, 10))#candidate|1113|(5, 1, 10)|var|float32
var_1114 = relay.var("var_1114", dtype = "float32", shape = (5, 4, 10))#candidate|1114|(5, 4, 10)|var|float32
output = func_1112(var_1113,var_1114,)
func_1115 = relay.Function([var_1113,var_1114,], output)
mutated_mod['func_1115'] = func_1115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1164 = func_1097_call()
call_1165 = func_1097_call()
func_1112_call = mod.get_global_var('func_1112')
func_1115_call = mutated_mod.get_global_var('func_1115')
const_1167 = relay.const([2.944193,-2.034103,-7.507269,4.880601,-2.685616,-4.330265,-6.124027,6.918323,2.824399,8.331720,-0.218466,-5.779206,4.375128,1.283762,2.958386,-0.827613,2.068087,5.484413,4.652157,0.479510,6.702841,4.678772,-9.125303,6.902887,-9.930385,9.618327,3.305074,-7.656801,-6.827784,0.509738,-1.989804,-4.608697,-2.531306,3.576541,-6.437222,-4.949340,9.893276,1.699084,-5.788818,9.493396,-8.997450,-6.584342,-8.987623,-5.798866,-8.862478,-3.227511,4.692984,5.786971,-3.313267,9.970663], dtype = "float32")#candidate|1167|(50,)|const|float32
const_1168 = relay.const([[-5.151261,-6.041486],[0.427955,-9.343213],[8.841683,-2.473483],[9.838297,0.301018],[-6.578442,-9.635295],[0.677111,-2.154060],[-7.830025,-1.392657],[-1.111881,-4.487614],[8.087681,-3.896634],[5.915407,-1.761006],[0.673156,6.273663],[-1.269268,-2.353303],[7.743071,-1.132900],[5.544573,-2.280441],[-8.060390,-9.699880],[-0.905488,5.289470],[-8.839334,-4.171720],[7.026569,-1.146245],[-3.128287,2.115855],[-2.170317,3.288394],[5.027395,-4.211830],[-8.169894,-9.750503],[8.651926,-7.902741],[0.708241,-0.970375],[4.387083,-8.677572],[2.028233,-3.121602],[-9.618840,-1.521208],[3.220276,-9.522508],[6.654130,-6.245520],[7.239148,-2.163338],[1.428636,8.513823],[8.722056,-5.799663],[-5.045389,1.298793],[7.044745,0.792074],[8.601832,3.614222],[4.295427,5.163759],[-1.688881,0.214848],[-9.271440,9.785732],[-4.214237,6.424915],[-8.130995,-5.291252],[-7.489030,-0.692585],[5.430973,5.789977],[-2.652723,-4.344028],[-0.293727,-6.369548],[2.005285,2.323852],[-4.380881,6.816103],[6.004719,-7.870552],[0.795389,-8.727933],[-9.092321,7.378639],[4.468240,-2.927918],[3.897364,5.394996],[9.580225,9.984215],[9.132971,-9.360843],[7.497521,-0.293447],[-6.379010,-6.647104],[-2.827637,2.876902],[4.458721,-9.423978],[0.973691,-7.270738],[3.536397,2.972358],[-4.910914,5.947190],[0.198751,5.863084],[-2.302258,4.932134],[-5.774923,-2.143707],[-4.887385,1.676925],[-7.231388,-7.319877],[-7.661748,0.449880],[7.527190,-6.129087],[5.766333,8.247632],[-9.761402,1.692238],[1.339243,2.964519],[-3.592946,-2.729481],[-8.763885,-7.067465],[9.021245,-0.394024],[-4.438733,-4.203947],[-0.170579,3.225063],[-9.950706,-6.202680],[8.925736,5.415776],[-1.328049,-9.769227],[-1.473141,-7.914407],[-1.424278,-7.998677],[2.722454,7.054011],[-9.544337,2.696202],[4.105281,-3.009441],[-3.977254,-1.210924],[-2.637147,-7.694134],[-3.917158,4.015326],[1.678328,1.181295],[-5.089035,0.197728],[9.255297,2.522747],[-7.029387,-9.926474],[7.390476,-9.179955],[-3.253434,4.157688],[-5.232089,6.498091],[-7.580895,-3.142673],[-6.997256,9.271084],[7.112234,2.587143],[-5.744531,-9.464617],[4.876882,-8.984921],[5.463174,-5.501446],[2.086180,-7.447320]], dtype = "float32")#candidate|1168|(100, 2)|const|float32
call_1166 = func_1112_call(relay.reshape(const_1167.astype('float32'), [5, 1, 10]), relay.reshape(const_1168.astype('float32'), [5, 4, 10]), )
call_1169 = func_1112_call(relay.reshape(const_1167.astype('float32'), [5, 1, 10]), relay.reshape(const_1168.astype('float32'), [5, 4, 10]), )
output = relay.Tuple([call_1164,call_1166,const_1167,const_1168,])
output2 = relay.Tuple([call_1165,call_1169,const_1167,const_1168,])
func_1174 = relay.Function([], output)
mod['func_1174'] = func_1174
mod = relay.transform.InferType()(mod)
mutated_mod['func_1174'] = func_1174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mutated_mod.get_global_var('func_1174')
call_1175 = func_1174_call()
output = call_1175
func_1176 = relay.Function([], output)
mutated_mod['func_1176'] = func_1176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_1236 = relay.TupleGetItem(func_1174_call(), 0)
call_1237 = relay.TupleGetItem(func_1176_call(), 0)
output = call_1236
output2 = call_1237
func_1251 = relay.Function([], output)
mod['func_1251'] = func_1251
mod = relay.transform.InferType()(mod)
output = func_1251()
func_1252 = relay.Function([], output)
mutated_mod['func_1252'] = func_1252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_1306 = func_1251_call()
call_1307 = func_1251_call()
output = call_1306
output2 = call_1307
func_1308 = relay.Function([], output)
mod['func_1308'] = func_1308
mod = relay.transform.InferType()(mod)
output = func_1308()
func_1309 = relay.Function([], output)
mutated_mod['func_1309'] = func_1309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_1313 = func_1251_call()
call_1314 = func_1251_call()
output = call_1313
output2 = call_1314
func_1323 = relay.Function([], output)
mod['func_1323'] = func_1323
mod = relay.transform.InferType()(mod)
mutated_mod['func_1323'] = func_1323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mutated_mod.get_global_var('func_1323')
call_1324 = func_1323_call()
output = call_1324
func_1325 = relay.Function([], output)
mutated_mod['func_1325'] = func_1325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_1469 = relay.TupleGetItem(func_1174_call(), 3)
call_1470 = relay.TupleGetItem(func_1176_call(), 3)
func_1323_call = mod.get_global_var('func_1323')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_1474 = func_1323_call()
call_1475 = func_1323_call()
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_1476 = func_1251_call()
call_1477 = func_1251_call()
output = relay.Tuple([call_1469,call_1474,call_1476,])
output2 = relay.Tuple([call_1470,call_1475,call_1477,])
func_1486 = relay.Function([], output)
mod['func_1486'] = func_1486
mod = relay.transform.InferType()(mod)
mutated_mod['func_1486'] = func_1486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1486_call = mutated_mod.get_global_var('func_1486')
call_1487 = func_1486_call()
output = call_1487
func_1488 = relay.Function([], output)
mutated_mod['func_1488'] = func_1488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_1509 = func_1308_call()
call_1510 = func_1308_call()
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
var_1517 = relay.var("var_1517", dtype = "uint8", shape = ())#candidate|1517|()|var|uint8
call_1516 = func_530_call(relay.reshape(var_1517.astype('uint8'), []))
call_1518 = func_530_call(relay.reshape(var_1517.astype('uint8'), []))
output = relay.Tuple([call_1509,call_1516,var_1517,])
output2 = relay.Tuple([call_1510,call_1518,var_1517,])
func_1525 = relay.Function([var_1517,], output)
mod['func_1525'] = func_1525
mod = relay.transform.InferType()(mod)
mutated_mod['func_1525'] = func_1525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1526 = relay.var("var_1526", dtype = "uint8", shape = ())#candidate|1526|()|var|uint8
func_1525_call = mutated_mod.get_global_var('func_1525')
call_1527 = func_1525_call(var_1526)
output = call_1527
func_1528 = relay.Function([var_1526], output)
mutated_mod['func_1528'] = func_1528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_1530 = func_1323_call()
call_1531 = func_1323_call()
output = relay.Tuple([call_1530,])
output2 = relay.Tuple([call_1531,])
func_1538 = relay.Function([], output)
mod['func_1538'] = func_1538
mod = relay.transform.InferType()(mod)
output = func_1538()
func_1539 = relay.Function([], output)
mutated_mod['func_1539'] = func_1539
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_1571 = func_1251_call()
call_1572 = func_1251_call()
output = relay.Tuple([call_1571,])
output2 = relay.Tuple([call_1572,])
func_1579 = relay.Function([], output)
mod['func_1579'] = func_1579
mod = relay.transform.InferType()(mod)
output = func_1579()
func_1580 = relay.Function([], output)
mutated_mod['func_1580'] = func_1580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_1592 = relay.TupleGetItem(func_1174_call(), 3)
call_1593 = relay.TupleGetItem(func_1176_call(), 3)
var_1602 = relay.var("var_1602", dtype = "float32", shape = (100, 2))#candidate|1602|(100, 2)|var|float32
bop_1603 = relay.mod(call_1592.astype('float32'), relay.reshape(var_1602.astype('float32'), relay.shape_of(call_1592))) # shape=(100, 2)
bop_1606 = relay.mod(call_1593.astype('float32'), relay.reshape(var_1602.astype('float32'), relay.shape_of(call_1593))) # shape=(100, 2)
bop_1607 = relay.less_equal(bop_1603.astype('bool'), relay.reshape(call_1592.astype('bool'), relay.shape_of(bop_1603))) # shape=(100, 2)
bop_1610 = relay.less_equal(bop_1606.astype('bool'), relay.reshape(call_1593.astype('bool'), relay.shape_of(bop_1606))) # shape=(100, 2)
output = relay.Tuple([bop_1607,])
output2 = relay.Tuple([bop_1610,])
func_1614 = relay.Function([var_1602,], output)
mod['func_1614'] = func_1614
mod = relay.transform.InferType()(mod)
mutated_mod['func_1614'] = func_1614
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1615 = relay.var("var_1615", dtype = "float32", shape = (100, 2))#candidate|1615|(100, 2)|var|float32
func_1614_call = mutated_mod.get_global_var('func_1614')
call_1616 = func_1614_call(var_1615)
output = call_1616
func_1617 = relay.Function([var_1615], output)
mutated_mod['func_1617'] = func_1617
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1634 = relay.const([[[8]],[[9]],[[-6]],[[-4]],[[-2]],[[-5]],[[3]],[[1]],[[10]],[[8]],[[3]],[[-10]],[[-3]],[[-1]],[[9]],[[-2]]], dtype = "int16")#candidate|1634|(16, 1, 1)|const|int16
var_1635 = relay.var("var_1635", dtype = "int16", shape = (16, 7, 15))#candidate|1635|(16, 7, 15)|var|int16
bop_1636 = relay.left_shift(const_1634.astype('int16'), var_1635.astype('int16')) # shape=(16, 7, 15)
output = relay.Tuple([bop_1636,])
output2 = relay.Tuple([bop_1636,])
func_1649 = relay.Function([var_1635,], output)
mod['func_1649'] = func_1649
mod = relay.transform.InferType()(mod)
mutated_mod['func_1649'] = func_1649
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1650 = relay.var("var_1650", dtype = "int16", shape = (16, 7, 15))#candidate|1650|(16, 7, 15)|var|int16
func_1649_call = mutated_mod.get_global_var('func_1649')
call_1651 = func_1649_call(var_1650)
output = call_1651
func_1652 = relay.Function([var_1650], output)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1660 = func_1097_call()
call_1661 = func_1097_call()
uop_1664 = relay.sqrt(call_1660.astype('float64')) # shape=(9, 1, 8)
uop_1666 = relay.sqrt(call_1661.astype('float64')) # shape=(9, 1, 8)
output = uop_1664
output2 = uop_1666
func_1671 = relay.Function([], output)
mod['func_1671'] = func_1671
mod = relay.transform.InferType()(mod)
mutated_mod['func_1671'] = func_1671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mutated_mod.get_global_var('func_1671')
call_1672 = func_1671_call()
output = call_1672
func_1673 = relay.Function([], output)
mutated_mod['func_1673'] = func_1673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_1677 = relay.TupleGetItem(func_1486_call(), 2)
call_1678 = relay.TupleGetItem(func_1488_call(), 2)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_1679 = func_1671_call()
call_1680 = func_1671_call()
var_1681 = relay.var("var_1681", dtype = "float64", shape = (9, 4, 8))#candidate|1681|(9, 4, 8)|var|float64
bop_1682 = relay.floor_divide(call_1679.astype('float64'), var_1681.astype('float64')) # shape=(9, 4, 8)
bop_1685 = relay.floor_divide(call_1680.astype('float64'), var_1681.astype('float64')) # shape=(9, 4, 8)
const_1694 = relay.const([[[0.183682,5.679770,8.967296,5.373168,9.985032,-0.188465,1.826062,9.610775],[-0.829429,-0.165648,2.488510,-3.089907,3.257466,-8.578248,4.238340,-1.596078],[1.341102,-6.927583,4.247325,-1.851363,-4.504135,7.377517,0.300764,-8.284862],[-7.457563,-9.896759,-9.837257,-2.929246,-8.912013,9.159308,-4.916036,-0.189223],[2.562512,-1.245476,-1.098085,2.155602,-4.401837,-9.666824,9.922483,4.037846],[-3.313799,6.226529,-0.710766,-4.474271,-8.143083,-4.381818,0.168565,6.418619],[8.871313,2.184147,-5.342536,4.702509,-5.900192,-3.680894,-3.908211,3.534132],[5.991971,6.607259,-2.223948,-8.652259,7.405534,-2.931020,4.948121,-1.928182],[6.470996,4.683815,-0.433189,-5.889237,-8.368150,4.872805,-3.807039,9.123430],[6.773672,2.432168,-8.376582,7.346385,-6.654710,3.084345,9.967698,4.297498],[5.113316,-8.514230,4.784207,-7.939681,5.055115,-8.244129,-8.067396,4.110001],[-7.409752,-4.578045,-6.933179,-6.442662,8.555767,-1.113008,6.088315,5.191268]],[[-4.855116,4.235664,1.163948,-3.923021,9.785274,-3.835085,-6.931722,3.103756],[1.547741,-1.702481,6.875891,-7.466230,-9.111281,0.734435,-3.571827,-1.683165],[-8.269373,-4.679401,-5.177138,-9.330737,4.982509,9.765573,-7.378608,-3.075790],[-4.745463,7.672263,-9.164299,-5.991225,4.453259,-0.277189,3.430461,-0.010470],[-6.738434,7.149831,0.320022,-2.950852,-1.485718,0.860088,5.123116,-8.291415],[-0.167762,1.934178,-1.863632,3.267359,-9.500272,1.033597,-5.429387,2.689940],[2.258648,3.567435,0.313697,2.389026,-4.955616,-1.049252,6.812317,2.635806],[1.801444,-5.719099,8.341487,0.542228,8.980630,0.122762,-3.363024,6.700209],[0.331765,7.625740,-5.637938,-1.225156,3.318284,-1.779156,-1.500122,-1.621763],[7.284041,7.308080,-2.395991,-5.818378,2.635616,7.942852,-3.920001,7.466400],[-1.926013,-1.193312,-4.227648,3.173127,-5.172623,-4.449282,8.624125,-3.486413],[3.666851,0.053168,-9.062512,3.428283,7.356892,4.467520,5.472741,5.024938]],[[8.459171,1.261856,5.209184,5.397406,-7.349205,-3.974718,-0.450879,-4.787381],[-7.752321,7.273819,5.683678,-2.828964,-8.067089,0.565119,2.805699,9.113981],[-1.899042,-4.116730,6.997281,8.702846,3.105716,0.346041,-3.461704,0.181849],[-1.988010,3.994310,5.017659,-0.756347,-6.558630,-3.980686,3.943134,-6.586152],[-3.408536,9.728509,0.351827,1.917669,-1.103571,-0.347990,4.821432,3.903738],[0.994809,1.634219,-9.404610,-0.346983,3.122932,-5.106004,-7.692179,5.784011],[9.454518,-8.428276,1.280226,4.157240,-4.919677,0.990347,2.632792,4.629300],[6.078251,-8.915615,6.097464,-9.646289,5.306254,2.811399,-4.006539,-0.382235],[2.325351,-4.012621,-9.181705,-3.816157,3.532751,-0.393139,-0.760366,9.149328],[7.977935,5.725556,-3.796495,7.259298,7.355649,0.225534,5.827411,5.488889],[-1.928663,-6.669518,-3.342588,-6.358776,-5.359398,-4.989728,-9.213967,-2.736491],[7.513662,-1.294751,-4.613422,1.534342,-2.430890,9.688833,-6.828940,-6.050064]],[[-8.861065,-7.120971,9.635825,-9.292021,9.124502,-7.550454,9.157611,2.857888],[8.376958,-0.220781,-2.809078,7.933213,4.534079,-0.555330,0.804725,-3.064180],[6.456240,-4.791397,9.347101,-9.464828,-2.082957,0.457859,-1.630336,-6.516636],[-9.595532,2.805861,3.166318,-7.200226,9.863668,-6.667543,4.275816,-4.619421],[2.385432,-9.085386,2.168179,-4.502761,5.919412,5.473267,-3.946581,3.017812],[3.399788,1.735336,6.361257,7.760792,4.312951,-7.520849,-5.685099,3.528360],[9.662938,0.454757,7.375560,-8.423720,5.403037,-7.223613,-2.063679,-4.376255],[-9.932444,-8.178657,1.948479,-7.722182,9.040180,-8.330991,4.578485,-6.924532],[9.563289,2.722819,3.462088,9.411157,-8.523507,-9.684304,-2.549442,-0.094597],[7.583709,-3.663232,-1.623041,0.231225,8.632739,5.547555,9.331180,-9.057601],[4.212901,1.264313,1.434804,4.266618,-1.884636,-1.917338,2.705077,6.995737],[3.826868,4.843050,-4.935455,-6.305767,-2.157845,-1.361499,4.974647,-0.569833]],[[0.789417,5.248697,2.130393,-2.252406,-5.994762,-8.993760,4.072962,-7.007350],[9.639521,-6.144625,-8.660124,-5.045371,-2.936514,2.727929,1.120278,7.342352],[0.740016,5.390226,4.377999,8.713351,8.292615,0.021335,5.339598,9.047240],[-3.114861,2.184647,-6.157265,1.009746,-9.500271,-8.297017,0.446676,-7.797851],[-6.865267,9.534104,1.880579,-1.667447,-6.639868,5.533237,5.285365,-5.293210],[-1.501174,1.239175,5.747218,-5.497901,9.105228,1.153969,-8.281626,4.103712],[-2.125483,-4.010944,5.376160,-8.302350,8.227675,-5.335561,-3.417866,-3.019318],[-3.349601,-0.632041,-1.081577,2.968750,7.528334,-4.963327,6.833129,5.788889],[-9.380572,4.192850,-1.654010,6.028408,-1.010841,-8.865076,8.175707,6.899981],[-0.467550,8.319198,-3.615271,-2.718601,-3.058795,0.287881,9.190687,8.769033],[4.027314,0.503973,-8.659449,2.089380,-3.608348,4.481493,-6.699986,8.103856],[-0.668503,9.144037,-3.518303,7.981410,3.108316,-4.833349,4.876710,-5.816650]],[[-0.312046,-7.520400,9.183250,7.761273,5.320002,7.949707,-0.123309,7.339582],[5.740021,8.466646,-3.192653,-4.495737,-7.812667,-2.928795,-3.621651,-5.012556],[2.075930,0.485303,-9.753570,-1.452602,-2.053234,9.978302,9.938709,0.561583],[3.929438,-6.309687,2.400596,6.718224,7.505243,8.352216,9.603162,-1.032091],[-3.150594,4.621943,8.575692,2.785429,0.006723,-0.140298,2.253177,0.830353],[-9.142813,-4.324550,1.303081,5.988214,-7.152451,-5.295511,-7.976220,-1.943609],[1.030240,5.417074,6.451545,-0.997279,9.448574,8.419335,-9.436057,-8.857697],[-4.466687,2.916537,-1.425937,-3.720543,9.053162,-0.696001,-9.561732,0.842482],[-2.374108,-4.187121,1.743920,-7.176367,1.157849,8.320718,8.008304,-5.803890],[-8.117262,1.037130,2.368382,3.820010,-8.796709,-4.711683,-3.217098,-9.630045],[5.222197,5.498678,0.929337,6.065731,7.722345,5.534368,-7.044466,4.098008],[7.685552,-1.630821,-2.783162,4.491760,0.907621,0.533564,5.220058,6.765114]],[[-0.932776,5.285322,-7.425340,-9.023528,1.490938,-2.281129,-6.341473,8.538747],[-7.066102,-1.229596,9.910321,-4.529204,5.821894,1.241659,1.076048,9.603065],[7.738000,-8.291317,-8.106163,9.139509,-3.660950,1.103389,7.151210,-4.782849],[-4.406651,8.259486,-0.353917,5.915281,1.255952,7.642288,4.018332,0.464668],[2.971005,-3.979115,-6.514620,-3.377699,-4.022348,1.665611,-6.872250,3.227853],[-8.451592,-9.065565,-3.481292,9.100544,-0.190761,9.737584,5.771918,-8.309997],[-9.265656,-3.651061,1.757051,4.084044,0.560870,6.206697,-3.012628,-7.374393],[0.758098,9.794078,-0.844625,-2.100751,9.118745,-2.014673,-7.423929,-6.921268],[-2.500944,6.738758,5.801474,3.218798,-6.267551,-3.435221,2.437397,2.235740],[1.797923,0.989645,3.745172,4.489382,8.778000,-1.596291,-9.256574,-1.061931],[2.228153,-7.466668,-7.870618,7.419949,5.259199,4.547953,1.395804,0.696238],[2.848098,-0.799696,-6.470303,-4.383739,-4.702124,7.697178,7.307914,7.743031]],[[-1.083125,8.450985,9.575586,4.831004,-7.276340,7.773543,0.821741,-0.597538],[8.195257,-3.580016,-1.681839,2.726215,4.246485,-0.067261,-5.022354,1.413872],[8.352239,8.947306,-3.803654,9.501168,3.918698,-8.092871,-3.794544,-4.774402],[9.897409,7.418348,7.961424,-7.489325,-8.473950,1.576583,-0.363136,3.522731],[3.083904,-3.817515,5.997046,-5.784484,3.842140,7.869126,6.812749,6.879645],[-8.051103,6.178655,-2.068569,-8.204948,-6.077551,7.918976,2.691006,-4.172536],[-9.776136,-2.795153,8.987942,-0.795632,5.574336,-6.017036,3.646179,8.147958],[-1.466313,0.249543,4.182493,1.514057,5.266103,-3.793604,4.295790,2.833010],[-5.360460,3.727190,-4.176277,-5.090036,-9.167832,6.023809,-5.584647,7.530596],[9.032307,2.609116,8.398379,-4.069027,-6.384481,6.365750,4.982910,1.917465],[-5.982041,0.650802,-2.473386,-3.139888,-7.979540,3.100877,-6.744303,-4.567996],[9.954435,-7.581587,-8.751316,-8.789778,-9.486919,3.338644,-5.504444,8.022611]],[[2.402776,-6.554102,-3.974976,-5.073992,-1.367051,5.081322,6.069519,-3.191904],[-8.347519,0.871182,2.524953,0.085730,7.142750,2.570022,4.003998,-6.262642],[-6.222514,-6.132468,7.023920,9.557765,-8.201405,-0.724477,-5.819508,0.953314],[-8.975841,-4.749673,-3.893286,7.409034,-9.508242,1.515284,5.327303,-7.475446],[-1.464223,-1.269698,-4.186733,8.984458,-6.130208,-9.910761,-6.769229,3.739596],[-7.064188,-0.921823,9.581445,-6.632933,0.891826,4.381632,5.288068,-4.228223],[4.098729,4.231751,-5.800666,-9.541697,-5.770942,-9.435538,-1.634257,5.106146],[8.758260,0.222271,3.733662,-3.380001,-9.477413,7.632742,3.732049,7.228640],[-5.206265,-4.169772,-7.369864,-4.779205,2.722758,5.668981,-2.744900,-8.924801],[1.868232,9.548972,8.928694,8.009669,7.684656,8.646739,-7.468974,9.670926],[0.758250,5.449453,6.581052,7.167864,-2.325658,-2.334675,0.688956,-9.263761],[6.417077,-6.650759,0.920194,-7.071617,-2.690530,-2.127879,-5.854282,-5.892692]]], dtype = "float64")#candidate|1694|(9, 12, 8)|const|float64
bop_1695 = relay.greater(call_1677.astype('bool'), const_1694.astype('bool')) # shape=(9, 12, 8)
bop_1698 = relay.greater(call_1678.astype('bool'), const_1694.astype('bool')) # shape=(9, 12, 8)
uop_1699 = relay.sigmoid(call_1679.astype('float64')) # shape=(9, 1, 8)
uop_1701 = relay.sigmoid(call_1680.astype('float64')) # shape=(9, 1, 8)
const_1703 = relay.const([[[5.778418,4.318776,-3.890808,0.025878,-2.123748,4.811227,-4.174279,-5.836558],[-8.531313,1.736865,3.813522,-6.362398,-6.221148,1.068099,8.540650,1.764283],[-1.726190,-8.139089,-4.218488,-2.891312,1.785852,6.287072,-3.961547,-2.787277]],[[9.682437,-7.924601,-4.226214,4.497901,8.931094,-6.371830,3.125489,7.938917],[6.562705,9.107640,0.079717,-7.725846,6.423690,-1.970642,0.472216,-5.605576],[-2.265149,0.161654,5.655703,0.087324,9.442086,-2.757917,3.203780,0.811001]],[[9.418729,-0.257594,-6.074556,9.396359,-3.644463,3.119351,-1.491782,-6.867945],[-4.721885,-5.399633,9.664940,-2.725930,1.851561,5.365452,-2.871491,6.567564],[0.367139,-6.405446,7.716832,6.278512,3.411083,8.334675,-1.768019,1.035531]],[[-7.592544,8.838696,4.613136,-6.716368,-7.247321,-7.112763,-0.690424,-3.769442],[9.254861,9.135895,-5.180237,4.677422,2.156463,4.109874,-4.271985,1.599266],[-4.492335,-2.672202,-9.988034,7.543810,4.774995,-9.050270,4.995119,2.892247]],[[6.676651,6.621489,-9.090391,-3.971688,-3.285591,5.033335,-8.388039,6.322264],[1.883692,-0.834534,-5.356988,-7.840275,8.437720,-6.808078,2.259305,-6.543410],[-4.554200,-1.016635,-5.621962,2.544432,9.180712,2.416991,5.217024,-6.087237]],[[0.184884,-7.067722,-1.154423,5.625791,1.923346,2.726727,3.275117,-6.253165],[8.937319,-5.366265,6.531422,-0.822620,8.599957,-8.510740,-2.351691,9.085039],[2.899402,-3.778839,7.595737,-1.312586,1.131108,1.146311,6.169676,-5.386091]],[[9.895545,-7.825061,-6.486100,2.489566,-2.589094,-4.746653,-4.201571,-0.128566],[-2.574557,-2.378458,-3.648799,-8.627061,-5.219357,8.630975,5.941090,-1.826938],[-7.723769,9.029360,-7.798146,-7.832510,-1.138728,2.385902,8.224307,4.897833]],[[-1.300457,3.377917,-1.565058,-2.116793,4.103095,-9.232146,-0.773640,6.695403],[0.170763,6.340471,4.102898,-6.128739,4.524245,5.051663,-2.799260,-3.167845],[-3.831739,5.005153,4.212731,7.439982,8.498337,-4.025721,-4.032047,7.399057]],[[-7.148877,2.767749,-9.874533,-3.923297,-0.510864,-1.296596,-0.540471,8.219108],[-6.080689,7.127225,9.713561,4.795582,-6.892685,-9.844515,7.752378,-7.549191],[-8.259026,-7.948467,4.533897,-1.275789,-3.423211,-3.500044,4.288014,7.644501]]], dtype = "float64")#candidate|1703|(9, 3, 8)|const|float64
bop_1704 = relay.power(uop_1699.astype('float64'), const_1703.astype('float64')) # shape=(9, 3, 8)
bop_1707 = relay.power(uop_1701.astype('float64'), const_1703.astype('float64')) # shape=(9, 3, 8)
output = relay.Tuple([bop_1682,bop_1695,bop_1704,])
output2 = relay.Tuple([bop_1685,bop_1698,bop_1707,])
func_1708 = relay.Function([var_1681,], output)
mod['func_1708'] = func_1708
mod = relay.transform.InferType()(mod)
mutated_mod['func_1708'] = func_1708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1709 = relay.var("var_1709", dtype = "float64", shape = (9, 4, 8))#candidate|1709|(9, 4, 8)|var|float64
func_1708_call = mutated_mod.get_global_var('func_1708')
call_1710 = func_1708_call(var_1709)
output = call_1710
func_1711 = relay.Function([var_1709], output)
mutated_mod['func_1711'] = func_1711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_1713 = relay.TupleGetItem(func_1486_call(), 0)
call_1714 = relay.TupleGetItem(func_1488_call(), 0)
output = call_1713
output2 = call_1714
func_1720 = relay.Function([], output)
mod['func_1720'] = func_1720
mod = relay.transform.InferType()(mod)
output = func_1720()
func_1721 = relay.Function([], output)
mutated_mod['func_1721'] = func_1721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_1743 = func_1671_call()
call_1744 = func_1671_call()
output = relay.Tuple([call_1743,])
output2 = relay.Tuple([call_1744,])
func_1745 = relay.Function([], output)
mod['func_1745'] = func_1745
mod = relay.transform.InferType()(mod)
output = func_1745()
func_1746 = relay.Function([], output)
mutated_mod['func_1746'] = func_1746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_1822 = func_1308_call()
call_1823 = func_1308_call()
var_1826 = relay.var("var_1826", dtype = "float64", shape = (9, 14, 8))#candidate|1826|(9, 14, 8)|var|float64
bop_1827 = relay.logical_or(call_1822.astype('bool'), var_1826.astype('bool')) # shape=(9, 14, 8)
bop_1830 = relay.logical_or(call_1823.astype('bool'), var_1826.astype('bool')) # shape=(9, 14, 8)
output = relay.Tuple([bop_1827,])
output2 = relay.Tuple([bop_1830,])
func_1836 = relay.Function([var_1826,], output)
mod['func_1836'] = func_1836
mod = relay.transform.InferType()(mod)
var_1837 = relay.var("var_1837", dtype = "float64", shape = (9, 14, 8))#candidate|1837|(9, 14, 8)|var|float64
output = func_1836(var_1837)
func_1838 = relay.Function([var_1837], output)
mutated_mod['func_1838'] = func_1838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_1848 = relay.TupleGetItem(func_1486_call(), 2)
call_1849 = relay.TupleGetItem(func_1488_call(), 2)
output = call_1848
output2 = call_1849
func_1850 = relay.Function([], output)
mod['func_1850'] = func_1850
mod = relay.transform.InferType()(mod)
output = func_1850()
func_1851 = relay.Function([], output)
mutated_mod['func_1851'] = func_1851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1855 = func_1097_call()
call_1856 = func_1097_call()
output = call_1855
output2 = call_1856
func_1857 = relay.Function([], output)
mod['func_1857'] = func_1857
mod = relay.transform.InferType()(mod)
mutated_mod['func_1857'] = func_1857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mutated_mod.get_global_var('func_1857')
call_1858 = func_1857_call()
output = call_1858
func_1859 = relay.Function([], output)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_1909 = func_1850_call()
call_1910 = func_1850_call()
var_1913 = relay.var("var_1913", dtype = "float64", shape = (9, 7, 8))#candidate|1913|(9, 7, 8)|var|float64
bop_1914 = relay.logical_or(call_1909.astype('bool'), var_1913.astype('bool')) # shape=(9, 7, 8)
bop_1917 = relay.logical_or(call_1910.astype('bool'), var_1913.astype('bool')) # shape=(9, 7, 8)
bop_1936 = relay.greater(call_1909.astype('bool'), var_1913.astype('bool')) # shape=(9, 7, 8)
bop_1939 = relay.greater(call_1910.astype('bool'), var_1913.astype('bool')) # shape=(9, 7, 8)
func_1579_call = mod.get_global_var('func_1579')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_1950 = relay.TupleGetItem(func_1579_call(), 0)
call_1951 = relay.TupleGetItem(func_1580_call(), 0)
uop_1979 = relay.erf(var_1913.astype('float32')) # shape=(9, 7, 8)
func_1015_call = mod.get_global_var('func_1015')
func_1018_call = mutated_mod.get_global_var('func_1018')
const_1982 = relay.const([-4,-4,9,-7,-8,-8,-4,7,6,7,-6,-5,-3,5,-9,1,-1,10,-2,3,-1,-1,7,-2,-9,-2,-1,2,-3,-9,-1,-8,5,6,-6,-7,1,3,-9,10,-5,3,-3,-9,5,-1,-8,1,-6,9,6,-8,-6,-5,-7,3,9,-7,2,-1,5,3,8,7,3,-5,-3,-5,5,4,-7,5,4,10,-9,2,10,7,3,3,1,-4,2,-3,-1,10,-5,-6,8,-6,-5,-3,6,-5,6,-7,-8,9,-2,9,-1,-1,-4,5,1,1,10,4,-5,-8,-9,-8,-4,6,-1,-9,-4,9,5,1,7,-3,5,-6,-6,-3,-7,-1,10,-9,4,3,6,7,-8,-9,-10,2,10,8,-2,1,2,10,-3,10,7,-5,-5,-6,1,-8,10,8,9,5,7,-1,-2,-10,10,-10,3,-1,10,-3,-5,-3,2,2,-7,5,5,-4,8,1,4,-6,1,-7,-7,3,3,6,9,-1,6,-2,-1,-9,-10,9,-4,-3,2,-5,2,10,5,-5,3,3,-1,2,1,2,-2,7,6,2,-10,7,-4,-9,3,3,7,7,1,9,1,-5,-2,2,2,6,-8,2,-1,2,5,2,-1,10], dtype = "int32")#candidate|1982|(234,)|const|int32
call_1981 = relay.TupleGetItem(func_1015_call(relay.reshape(const_1982.astype('int32'), [13, 3, 6]), relay.reshape(const_1982.astype('int32'), [13, 3, 6]), ), 1)
call_1983 = relay.TupleGetItem(func_1018_call(relay.reshape(const_1982.astype('int32'), [13, 3, 6]), relay.reshape(const_1982.astype('int32'), [13, 3, 6]), ), 1)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_1992 = func_1097_call()
call_1993 = func_1097_call()
output = relay.Tuple([bop_1914,bop_1936,call_1950,uop_1979,call_1981,const_1982,call_1992,])
output2 = relay.Tuple([bop_1917,bop_1939,call_1951,uop_1979,call_1983,const_1982,call_1993,])
func_1999 = relay.Function([var_1913,], output)
mod['func_1999'] = func_1999
mod = relay.transform.InferType()(mod)
mutated_mod['func_1999'] = func_1999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2000 = relay.var("var_2000", dtype = "float64", shape = (9, 7, 8))#candidate|2000|(9, 7, 8)|var|float64
func_1999_call = mutated_mod.get_global_var('func_1999')
call_2001 = func_1999_call(var_2000)
output = call_2001
func_2002 = relay.Function([var_2000], output)
mutated_mod['func_2002'] = func_2002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_2025 = relay.TupleGetItem(func_1174_call(), 0)
call_2026 = relay.TupleGetItem(func_1176_call(), 0)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_2027 = func_1857_call()
call_2028 = func_1857_call()
bop_2030 = relay.mod(call_2025.astype('float64'), relay.reshape(call_2027.astype('float64'), relay.shape_of(call_2025))) # shape=(9, 1, 8)
bop_2033 = relay.mod(call_2026.astype('float64'), relay.reshape(call_2028.astype('float64'), relay.shape_of(call_2026))) # shape=(9, 1, 8)
output = relay.Tuple([bop_2030,])
output2 = relay.Tuple([bop_2033,])
func_2036 = relay.Function([], output)
mod['func_2036'] = func_2036
mod = relay.transform.InferType()(mod)
mutated_mod['func_2036'] = func_2036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2036_call = mutated_mod.get_global_var('func_2036')
call_2037 = func_2036_call()
output = call_2037
func_2038 = relay.Function([], output)
mutated_mod['func_2038'] = func_2038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_2083 = relay.TupleGetItem(func_1745_call(), 0)
call_2084 = relay.TupleGetItem(func_1746_call(), 0)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_2085 = func_1850_call()
call_2086 = func_1850_call()
bop_2098 = relay.add(call_2083.astype('int16'), relay.reshape(call_2085.astype('int16'), relay.shape_of(call_2083))) # shape=(9, 1, 8)
bop_2101 = relay.add(call_2084.astype('int16'), relay.reshape(call_2086.astype('int16'), relay.shape_of(call_2084))) # shape=(9, 1, 8)
func_1649_call = mod.get_global_var('func_1649')
func_1652_call = mutated_mod.get_global_var('func_1652')
var_2103 = relay.var("var_2103", dtype = "int16", shape = (1680,))#candidate|2103|(1680,)|var|int16
call_2102 = relay.TupleGetItem(func_1649_call(relay.reshape(var_2103.astype('int16'), [16, 7, 15])), 0)
call_2104 = relay.TupleGetItem(func_1652_call(relay.reshape(var_2103.astype('int16'), [16, 7, 15])), 0)
output = relay.Tuple([bop_2098,call_2102,var_2103,])
output2 = relay.Tuple([bop_2101,call_2104,var_2103,])
func_2113 = relay.Function([var_2103,], output)
mod['func_2113'] = func_2113
mod = relay.transform.InferType()(mod)
var_2114 = relay.var("var_2114", dtype = "int16", shape = (1680,))#candidate|2114|(1680,)|var|int16
output = func_2113(var_2114)
func_2115 = relay.Function([var_2114], output)
mutated_mod['func_2115'] = func_2115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_2167 = func_1671_call()
call_2168 = func_1671_call()
output = call_2167
output2 = call_2168
func_2177 = relay.Function([], output)
mod['func_2177'] = func_2177
mod = relay.transform.InferType()(mod)
mutated_mod['func_2177'] = func_2177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2177_call = mutated_mod.get_global_var('func_2177')
call_2178 = func_2177_call()
output = call_2178
func_2179 = relay.Function([], output)
mutated_mod['func_2179'] = func_2179
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2234 = relay.var("var_2234", dtype = "float64", shape = (2, 15, 12))#candidate|2234|(2, 15, 12)|var|float64
uop_2235 = relay.sinh(var_2234.astype('float64')) # shape=(2, 15, 12)
func_123_call = mod.get_global_var('func_123')
func_125_call = mutated_mod.get_global_var('func_125')
var_2241 = relay.var("var_2241", dtype = "float64", shape = (336,))#candidate|2241|(336,)|var|float64
call_2240 = func_123_call(relay.reshape(var_2241.astype('float64'), [14, 2, 12]))
call_2242 = func_123_call(relay.reshape(var_2241.astype('float64'), [14, 2, 12]))
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_2248 = func_1251_call()
call_2249 = func_1251_call()
output = relay.Tuple([uop_2235,call_2240,var_2241,call_2248,])
output2 = relay.Tuple([uop_2235,call_2242,var_2241,call_2249,])
func_2259 = relay.Function([var_2234,var_2241,], output)
mod['func_2259'] = func_2259
mod = relay.transform.InferType()(mod)
var_2260 = relay.var("var_2260", dtype = "float64", shape = (2, 15, 12))#candidate|2260|(2, 15, 12)|var|float64
var_2261 = relay.var("var_2261", dtype = "float64", shape = (336,))#candidate|2261|(336,)|var|float64
output = func_2259(var_2260,var_2261,)
func_2262 = relay.Function([var_2260,var_2261,], output)
mutated_mod['func_2262'] = func_2262
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2264 = relay.var("var_2264", dtype = "uint16", shape = (10, 13, 11))#candidate|2264|(10, 13, 11)|var|uint16
const_2265 = relay.const([[[-10,-7,-7,-3,3,-1,-7,6,3,6,-3],[5,-9,3,9,-7,10,-5,2,-1,1,10],[3,5,1,2,-2,-9,3,6,-6,2,-6],[5,4,4,10,-5,-1,8,10,7,-8,4],[10,5,4,4,-2,-9,-6,4,-9,10,-7],[-2,-6,-2,7,6,-7,-5,-8,-2,-1,9],[-6,-5,1,-4,2,9,7,4,9,-3,-1],[-7,1,-1,10,10,-4,10,-10,6,-10,-2],[8,5,6,-4,-8,7,-10,-2,8,-4,-8],[-8,9,-10,10,-10,-6,6,2,-10,-10,-2],[5,1,-7,-6,1,3,7,-1,-5,-7,-3],[-4,4,-7,-1,7,2,-9,-6,6,-8,-9],[2,6,-10,-8,-8,8,-6,-10,-4,3,6]],[[-7,-9,-10,-1,6,9,-9,-4,2,9,8],[6,2,-5,-10,-1,5,-9,8,6,-1,5],[3,-7,5,-8,-1,1,6,10,-8,2,-10],[-8,1,2,8,6,-9,8,-10,7,1,-5],[-3,-3,-4,4,-8,-2,-6,-4,4,-8,2],[-6,-4,-4,-8,-4,-3,-2,1,-3,-10,-9],[3,-3,-1,9,10,-8,6,-9,-2,-7,-9],[-4,-7,-1,-5,-5,4,-3,-10,-2,6,5],[3,-8,9,8,8,-2,10,-2,-6,3,-5],[-6,-9,-7,10,8,-8,-6,4,8,-7,-7],[-6,4,-7,1,-3,7,9,6,-6,1,-1],[-4,3,8,-2,1,-5,-9,3,-2,-9,6],[-5,-5,7,6,5,6,3,9,9,3,-6]],[[4,-2,-4,7,9,4,-4,2,-2,9,-6],[-10,-8,-5,-2,-3,10,5,6,-8,6,9],[-5,-10,-7,-5,-3,-7,5,-4,-7,-5,2],[-1,-6,3,10,-3,-4,-4,-6,-5,-5,2],[8,-8,4,-10,-5,-7,1,-4,2,8,2],[7,4,-7,-6,-10,6,7,-3,-8,-9,1],[3,-1,-5,-2,-4,5,3,-6,2,1,-5],[-9,5,-9,10,-2,-5,9,3,-7,2,-4],[3,-2,-7,-4,-1,-3,8,-9,-3,-3,-4],[-8,-6,4,6,-3,-8,-3,-7,-9,10,5],[5,-6,4,7,-2,7,-2,5,10,7,4],[3,9,-10,-6,-4,-10,1,2,4,-7,-1],[3,-4,-6,1,3,1,-7,-8,9,-8,-4]],[[3,-1,9,9,6,10,4,-3,7,-10,5],[-1,-2,6,-7,1,8,6,-9,-1,-8,-4],[-8,7,2,-4,-7,-1,5,-9,2,2,-3],[9,-7,6,1,6,-7,-5,-4,-8,-1,-10],[-8,1,-10,-2,-5,-4,3,-6,9,4,-8],[-7,-7,3,-5,6,-3,-5,-10,-7,-8,-5],[-2,5,-4,-9,9,3,4,4,9,3,9],[-7,5,-3,-5,-3,-1,10,9,-6,-7,4],[6,-1,2,-7,3,7,7,2,10,1,-6],[-5,-10,5,9,-1,9,-10,-5,1,2,-6],[10,1,3,-9,2,-6,-6,-2,-10,10,4],[-10,8,8,1,-8,-4,-9,2,-6,4,9],[-2,-7,-3,-2,8,9,-7,-7,-3,-7,6]],[[3,-6,2,-2,-1,1,7,-6,2,-4,1],[8,-8,-5,-5,3,-8,-7,-10,-1,-3,3],[-6,-10,-3,7,-6,4,-3,8,-9,-6,-9],[-7,-1,-4,-1,-2,-5,3,-7,-4,7,-6],[8,-8,5,5,-6,7,-1,10,9,8,6],[-4,4,-7,-7,-1,7,3,5,7,10,-9],[-6,-4,-2,-9,-4,5,-2,-6,3,3,9],[1,-1,5,4,-4,-4,-5,1,-7,10,2],[4,8,-7,7,-6,8,-9,-9,-7,-5,-1],[9,8,-6,8,8,-6,-9,-9,9,-7,3],[1,10,4,1,8,7,6,4,-1,-5,-3],[10,-3,7,7,5,-1,10,-4,1,10,10],[1,-1,-8,-9,-3,3,9,3,2,-8,6]],[[-8,-8,4,7,4,-8,10,3,9,10,9],[3,-7,-3,8,10,2,3,6,8,9,6],[1,1,-5,-3,-10,8,1,-10,-3,-3,10],[8,9,9,1,-7,7,4,9,-6,-4,-6],[-8,-4,-9,-5,-6,-9,1,2,5,8,-9],[4,2,7,-8,10,9,6,-2,9,4,-2],[-5,-8,-4,-2,9,-1,8,6,8,2,2],[5,1,-4,9,-1,-8,5,-3,5,3,-2],[3,-8,4,8,8,-1,-7,-5,1,-1,2],[3,2,-7,5,5,7,-8,-3,-4,10,-1],[10,-3,9,10,-1,9,2,-8,7,-4,7],[3,8,3,5,-7,10,-6,6,-10,-10,10],[-7,6,10,-8,1,8,-1,1,5,-2,8]],[[3,5,-10,-4,-4,7,-5,-1,-5,-4,-6],[-6,-10,-3,-5,10,6,1,8,-6,-6,-4],[1,4,10,1,-3,-2,-7,5,7,-7,-1],[-9,-4,5,8,-3,-7,-5,6,-4,4,-2],[-3,10,-4,-7,5,-8,-10,3,2,-9,4],[9,-1,-7,-1,3,-5,7,9,-4,9,5],[5,-9,3,-8,-1,7,10,-6,-4,-6,-1],[-10,-5,5,6,-3,-10,-10,10,2,-6,3],[4,8,8,6,-5,2,-3,-5,-8,2,1],[-3,-1,-4,5,-3,-9,-6,5,8,10,-3],[6,-2,4,-4,-5,8,3,4,-1,4,10],[-9,-2,6,-7,-5,-4,-9,10,-7,-2,2],[9,3,3,-2,-7,-9,-7,3,3,-1,4]],[[9,-5,8,1,5,7,2,5,-4,-4,-3],[7,9,3,-9,9,-8,4,2,-9,-7,-4],[8,-2,2,-3,-1,1,10,-7,9,-7,-2],[7,6,2,-2,-4,-6,3,4,-4,-6,-4],[-9,5,9,-8,-3,-7,-1,-4,-5,-5,7],[-10,-4,8,9,6,5,7,5,6,-10,-9],[-10,-8,-3,6,9,-3,-10,2,-4,-9,-10],[-4,-2,3,3,-7,-4,10,7,9,3,8],[-4,-5,1,-7,2,7,4,-8,-1,10,9],[5,5,2,8,1,2,-10,2,3,-1,-8],[10,1,-10,-9,10,-4,9,-3,6,9,-2],[1,8,-7,-6,-3,-10,8,-5,8,-10,-10],[-6,6,-7,-2,-5,2,-8,-2,4,3,-2]],[[-4,9,-2,-4,-9,-5,4,1,-2,10,-8],[3,-5,9,-10,2,-10,6,1,6,10,-7],[5,2,-2,1,1,4,-4,-7,-8,8,9],[1,4,1,1,10,-8,3,-5,4,2,-5],[2,1,-10,-7,-3,-10,-8,-10,-1,-6,3],[10,6,3,1,4,-9,-3,-4,-7,-1,-1],[-7,7,-1,8,-4,9,10,8,1,5,9],[-10,-8,-9,3,-7,10,10,-9,-5,-5,-1],[-8,8,-4,-3,1,-7,10,8,-7,6,9],[1,6,-10,-2,-8,1,2,-9,10,8,-10],[5,-6,3,10,-9,1,-6,-8,2,-1,-4],[-10,-9,4,8,-8,2,-5,-5,8,-5,1],[9,-2,-7,-4,5,5,-4,1,-3,-7,2]],[[-1,-7,3,7,5,-3,-9,-9,1,-8,-8],[-7,8,-8,4,-7,7,3,5,-5,-8,-9],[-9,9,-2,8,1,7,-5,4,-4,-6,4],[2,9,-2,-6,-3,9,6,-1,3,2,-1],[6,-8,-6,-3,4,-2,5,-2,-6,5,-9],[9,9,-3,-2,10,10,10,4,6,1,1],[-1,4,-9,3,3,-7,-3,-5,-5,-5,-5],[-10,-8,-7,2,2,10,-1,8,7,5,6],[-6,-5,8,-3,6,-3,10,3,9,-7,3],[10,-1,3,-10,-4,-1,-7,-10,3,-4,10],[6,7,-9,4,2,3,10,-9,-6,9,3],[-6,6,1,-6,5,-4,-9,5,-5,7,10],[8,10,-2,1,4,-2,-7,-2,4,6,10]]], dtype = "uint16")#candidate|2265|(10, 13, 11)|const|uint16
bop_2266 = relay.multiply(var_2264.astype('uint16'), relay.reshape(const_2265.astype('uint16'), relay.shape_of(var_2264))) # shape=(10, 13, 11)
func_2113_call = mod.get_global_var('func_2113')
func_2115_call = mutated_mod.get_global_var('func_2115')
var_2281 = relay.var("var_2281", dtype = "int16", shape = (1680,))#candidate|2281|(1680,)|var|int16
call_2280 = relay.TupleGetItem(func_2113_call(relay.reshape(var_2281.astype('int16'), [1680,])), 1)
call_2282 = relay.TupleGetItem(func_2115_call(relay.reshape(var_2281.astype('int16'), [1680,])), 1)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_2330 = func_1097_call()
call_2331 = func_1097_call()
output = relay.Tuple([bop_2266,call_2280,var_2281,call_2330,])
output2 = relay.Tuple([bop_2266,call_2282,var_2281,call_2331,])
func_2338 = relay.Function([var_2264,var_2281,], output)
mod['func_2338'] = func_2338
mod = relay.transform.InferType()(mod)
var_2339 = relay.var("var_2339", dtype = "uint16", shape = (10, 13, 11))#candidate|2339|(10, 13, 11)|var|uint16
var_2340 = relay.var("var_2340", dtype = "int16", shape = (1680,))#candidate|2340|(1680,)|var|int16
output = func_2338(var_2339,var_2340,)
func_2341 = relay.Function([var_2339,var_2340,], output)
mutated_mod['func_2341'] = func_2341
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2358 = relay.var("var_2358", dtype = "float32", shape = (11, 7, 16))#candidate|2358|(11, 7, 16)|var|float32
uop_2359 = relay.acosh(var_2358.astype('float32')) # shape=(11, 7, 16)
output = relay.Tuple([uop_2359,])
output2 = relay.Tuple([uop_2359,])
func_2368 = relay.Function([var_2358,], output)
mod['func_2368'] = func_2368
mod = relay.transform.InferType()(mod)
var_2369 = relay.var("var_2369", dtype = "float32", shape = (11, 7, 16))#candidate|2369|(11, 7, 16)|var|float32
output = func_2368(var_2369)
func_2370 = relay.Function([var_2369], output)
mutated_mod['func_2370'] = func_2370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_2415 = func_1251_call()
call_2416 = func_1251_call()
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_2428 = relay.TupleGetItem(func_1174_call(), 3)
call_2429 = relay.TupleGetItem(func_1176_call(), 3)
output = relay.Tuple([call_2415,call_2428,])
output2 = relay.Tuple([call_2416,call_2429,])
func_2436 = relay.Function([], output)
mod['func_2436'] = func_2436
mod = relay.transform.InferType()(mod)
mutated_mod['func_2436'] = func_2436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2436_call = mutated_mod.get_global_var('func_2436')
call_2437 = func_2436_call()
output = call_2437
func_2438 = relay.Function([], output)
mutated_mod['func_2438'] = func_2438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_2455 = func_1671_call()
call_2456 = func_1671_call()
output = relay.Tuple([call_2455,])
output2 = relay.Tuple([call_2456,])
func_2458 = relay.Function([], output)
mod['func_2458'] = func_2458
mod = relay.transform.InferType()(mod)
output = func_2458()
func_2459 = relay.Function([], output)
mutated_mod['func_2459'] = func_2459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_2481 = func_1308_call()
call_2482 = func_1308_call()
output = call_2481
output2 = call_2482
func_2499 = relay.Function([], output)
mod['func_2499'] = func_2499
mod = relay.transform.InferType()(mod)
output = func_2499()
func_2500 = relay.Function([], output)
mutated_mod['func_2500'] = func_2500
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2554 = relay.var("var_2554", dtype = "int16", shape = (8, 5, 2))#candidate|2554|(8, 5, 2)|var|int16
var_2555 = relay.var("var_2555", dtype = "int16", shape = (8, 5, 2))#candidate|2555|(8, 5, 2)|var|int16
bop_2556 = relay.greater(var_2554.astype('bool'), relay.reshape(var_2555.astype('bool'), relay.shape_of(var_2554))) # shape=(8, 5, 2)
func_2368_call = mod.get_global_var('func_2368')
func_2370_call = mutated_mod.get_global_var('func_2370')
const_2561 = relay.const([[-3.096521],[0.235800],[1.614184],[0.071648],[-9.396396],[2.218150],[-7.521532],[-9.957982],[-1.725701],[-5.317452],[6.022043],[9.736619],[1.805646],[9.413221],[9.290977],[3.248285],[-6.209933],[-2.718356],[3.840286],[1.134817],[-3.728406],[-0.569041],[-3.703093],[-4.497213],[-1.682969],[-0.819366],[-2.711770],[2.889617],[-3.282612],[6.732555],[-9.279954],[8.673858],[9.726057],[-0.938550],[-3.447467],[-4.629280],[-3.628168],[5.680528],[-3.711493],[0.174311],[6.704578],[-6.242722],[-9.442561],[6.056841],[-9.395559],[-0.788209],[6.310195],[5.851074],[9.723193],[3.863629],[0.986455],[4.408146],[-7.741100],[-0.700552],[-6.386269],[1.165565],[-6.296735],[5.915134],[0.330033],[1.539430],[0.060313],[-4.522613],[-0.784306],[6.215351],[3.837094],[8.726676],[8.511266],[-9.445390],[5.359518],[-4.204433],[-4.720418],[2.181172],[3.452153],[1.707604],[2.752354],[1.030044],[-7.303932],[9.637334],[5.539787],[0.619695],[8.651217],[-3.907371],[9.890789],[-5.204926],[9.971630],[-7.506887],[-9.920128],[-9.404631],[-0.695419],[-3.251351],[9.393987],[-1.335462],[7.051769],[-8.141949],[-0.730228],[6.734873],[-6.211606],[-6.532680],[-6.215409],[-9.270934],[0.051327],[-9.168977],[1.267498],[-0.594776],[-0.945299],[7.992786],[-0.547694],[-5.952421],[-5.108247],[-0.626267],[-3.667780],[-5.986471],[5.643166],[-7.959741],[-4.113581],[-2.934514],[5.302949],[4.730834],[1.476967],[-1.938576],[7.291440],[8.952126],[7.510222],[7.357296],[-5.946603],[-1.057201],[-1.993669],[4.843369],[-7.206661],[4.949080],[8.629540],[-6.533200],[-8.443698],[0.083464],[0.278306],[-7.218512],[4.512651],[-2.435054],[1.888384],[-5.136938],[-0.156649],[-4.293522],[-1.238820],[-2.390968],[4.420365],[1.913904],[7.985139],[9.025534],[8.965501],[-2.101143],[-3.745113],[5.768709],[-9.478875],[-8.165312],[-5.179138],[-6.355244],[2.700153],[9.746313],[-4.360485],[-1.008460],[6.821702],[-6.175519],[-1.540236],[6.351288],[-8.143917],[-9.065888],[-9.937488],[9.574351],[-4.924273],[-9.868553],[-6.718327],[8.905020],[9.502357],[6.941789],[-8.967412],[9.053685],[4.030285],[1.905584],[6.770677],[-7.693319],[-5.593588],[-7.050486],[-1.491795],[7.943221],[5.130631],[1.110479],[-2.544743],[9.558145],[8.732746],[-4.964663],[3.388928],[-8.509261],[8.676387],[-7.132827],[-9.758105],[5.658993],[9.981757],[8.697168],[6.293050],[-7.050390],[-5.032878],[-2.387751],[-4.512510],[-3.275266],[8.656786],[-7.561216],[-1.776311],[3.842317],[-0.198742],[-6.747477],[-0.485614],[8.786298],[8.727705],[-1.747442],[7.436180],[8.550834],[-6.587815],[6.488951],[7.967613],[9.236308],[-3.595621],[5.793058],[-7.804663],[-9.229155],[-0.413354],[8.460181],[-2.447666],[3.586703],[0.309043],[-4.849577],[-4.959771],[-4.521099],[-1.781318],[-0.909278],[2.434942],[-5.163728],[4.873016],[-3.646454],[-0.604463],[-1.120975],[3.308084],[-5.811481],[-1.897724],[6.775971],[7.296607],[-0.294559],[7.157926],[-0.319243],[-1.262404],[8.512714],[-3.561006],[8.254968],[-7.506742],[6.973280],[7.866309],[5.460085],[4.873259],[-6.914716],[6.446145],[0.963256],[-4.959643],[8.089107],[-6.797730],[3.500816],[-0.071694],[-4.996578],[-9.634064],[-1.389356],[4.165557],[8.878422],[7.879585],[3.307432],[-4.957564],[-7.513277],[1.936253],[-5.593429],[0.381226],[6.775531],[-6.234833],[3.881731],[-9.097166],[9.610298],[2.711650],[4.231985],[-8.066549],[3.970470],[4.818365],[-6.243725],[1.920146],[-5.464238],[7.256468],[-4.322299],[-7.278837],[-9.892895],[-8.887533],[3.495484],[-7.672035],[9.442268],[-3.924400],[-0.654773],[0.052890],[-9.251363],[5.157675],[4.061445],[8.946979],[2.153750],[-7.667292],[2.589230],[-6.325238],[6.987065],[2.603660],[8.276591],[-1.237378],[-2.351967],[6.489708],[1.169952],[-3.917010],[8.150784],[-6.669287],[-2.191757],[-4.006197],[-4.498696],[1.197303],[0.975509],[-8.579019],[-0.190911],[2.329701],[5.288556],[-2.645446],[-4.000810],[-0.400538],[1.871794],[3.991110],[-8.836101],[4.449673],[7.919457],[9.791115],[-0.873947],[-2.302200],[-3.192529],[7.183913],[-5.207955],[-3.811141],[-7.604471],[1.931002],[-3.802172],[-5.491530],[7.887505],[-2.731385],[5.935167],[-3.843383],[-1.680364],[0.011393],[5.650239],[-1.161488],[-7.399581],[-3.963143],[1.930374],[-4.192767],[-4.075227],[-5.861976],[7.686721],[-0.462474],[2.437023],[3.372974],[-2.699972],[3.183317],[6.501577],[1.703569],[-5.848108],[-3.273198],[5.878355],[-0.350816],[5.108078],[-5.103672],[-0.129510],[-9.350384],[4.936415],[-9.625513],[7.138613],[-1.399505],[-3.654658],[-9.773419],[-9.604599],[-8.672964],[-8.409952],[3.352360],[2.152321],[-0.906704],[-8.386173],[-6.264488],[3.494481],[-9.544691],[7.694164],[9.326398],[-8.051967],[-6.680670],[-0.160361],[-9.649029],[0.956050],[2.070474],[4.255884],[9.860108],[-3.432303],[5.190921],[2.215110],[-5.627768],[-9.880687],[5.179816],[9.685777],[9.704838],[-6.607543],[-3.924872],[-4.386500],[6.796196],[7.835141],[2.048665],[7.797812],[-3.726800],[-7.719651],[-5.012721],[1.303137],[6.251717],[-6.733842],[-2.915271],[7.305484],[5.905781],[0.938598],[-8.326835],[3.756649],[5.460714],[3.817200],[1.132871],[-4.662983],[-0.975210],[-4.618030],[-6.918219],[2.135524],[1.341432],[-3.911158],[-1.419265],[1.716397],[-8.116001],[5.207715],[2.867621],[-8.509635],[-2.077996],[9.332702],[9.476153],[7.596834],[5.977326],[-0.320613],[6.060048],[3.352234],[7.705722],[-8.637302],[2.326455],[-6.046545],[9.556593],[5.030845],[-8.598471],[1.027514],[4.694506],[-0.879367],[-9.307350],[-3.329172],[5.620844],[0.412747],[4.738683],[-3.466366],[6.882954],[-6.403767],[-8.169500],[-2.404110],[-7.613624],[-9.991470],[6.203610],[8.108174],[7.729540],[6.940791],[6.551680],[1.250270],[1.429733],[-9.101054],[4.779818],[6.333437],[7.076553],[6.861431],[-2.479473],[0.785088],[9.495947],[3.199475],[-4.701253],[1.688311],[7.718192],[6.653739],[3.547230],[5.892354],[-9.661386],[7.245134],[-5.275352],[-8.021098],[-1.516107],[-2.560332],[8.348656],[7.045523],[3.630584],[5.132426],[-4.306447],[6.133169],[-1.686831],[-1.615420],[3.784020],[-8.300753],[7.008598],[3.584911],[-9.956532],[-7.346060],[-4.975664],[-1.143220],[-7.789850],[-4.545134],[-2.452796],[9.224244],[4.635985],[-3.161854],[-5.198870],[8.625994],[3.029748],[7.306285],[9.643958],[-3.130879],[-5.578159],[-2.790264],[5.574235],[-2.949653],[-3.609290],[-5.814966],[-8.198547],[2.022572],[-7.102706],[7.200315],[5.870022],[3.682849],[-3.131677],[2.508633],[1.124153],[-9.493841],[-3.966613],[-6.672668],[6.977610],[-6.032368],[-4.858365],[-3.486748],[-7.071258],[-0.128835],[-4.420422],[7.332748],[-8.306429],[-4.546129],[1.144676],[-8.654216],[0.526105],[-9.662822],[2.131419],[-4.718897],[2.899680],[-1.818773],[3.807592],[0.145687],[7.462790],[-7.102774],[6.603411],[0.590866],[-3.651162],[3.379658],[8.441035],[4.506382],[-1.129763],[5.142292],[-4.059102],[-9.687430],[-9.996647],[6.343333],[0.224651],[0.241650],[-1.885308],[-0.174773],[-0.937224],[4.198466],[6.853191],[-7.577530],[-9.804826],[-5.974464],[-4.530823],[-5.933063],[4.887186],[-5.215168],[-3.721086],[8.469553],[-0.046478],[-0.074371],[-7.894976],[3.125779],[-4.311827],[-4.400669],[9.102844],[-3.752141],[-7.210888],[-3.364171],[-1.310629],[0.981511],[8.332078],[3.853376],[-8.984976],[2.438278],[-3.481660],[5.926224],[0.124222],[2.571550],[-8.074228],[6.981347],[-1.751105],[0.106589],[-4.248583],[4.122593],[7.413566],[-3.433409],[5.822112],[-4.900239],[-9.726768],[-5.178677],[1.930906],[-9.699097],[-3.182100],[-1.261170],[9.669870],[-2.416345],[8.572336],[-3.853133],[6.837880],[5.548095],[-8.203085],[7.401728],[1.953842],[4.383428],[-5.596159],[-4.736454],[-9.459110],[-9.665743],[-7.910478],[6.412866],[-9.846063],[-0.535134],[2.318771],[-3.952176],[-2.462470],[4.633627],[7.381503],[-4.558903],[-2.582663],[9.109622],[-9.609404],[-8.658138],[-0.959231],[9.509898],[6.437230],[-2.287959],[0.342732],[-5.594020],[9.531183],[4.019080],[-7.731169],[-4.823028],[-3.195707],[-6.379397],[6.391903],[7.603548],[-3.458629],[-9.047099],[-6.785171],[5.962473],[-8.687731],[0.017879],[-2.607704],[-9.599019],[-3.032850],[-6.365696],[6.717740],[7.445773],[3.200051],[-7.490817],[1.804255],[-0.639228],[-0.173228],[-1.350039],[4.121347],[-0.755628],[1.356512],[4.778572],[1.775045],[7.649380],[8.504940],[-1.988387],[-5.142302],[-5.048853],[-7.542164],[-5.980465],[-2.528955],[8.769847],[4.356535],[6.746356],[9.718638],[-2.975051],[-3.034885],[9.068119],[-7.665201],[4.310300],[-1.152481],[-7.015428],[0.889574],[-9.579738],[9.782517],[7.245926],[-1.093537],[-3.504548],[-8.164751],[-3.948898],[-7.050809],[-7.122894],[-2.268233],[-2.296420],[-9.178289],[-8.572471],[-7.836661],[-8.976666],[-0.987880],[4.959166],[5.202783],[8.843491],[8.834269],[-9.781136],[-1.772508],[9.197695],[3.421717],[5.249902],[9.861165],[-6.233178],[7.966776],[-9.408100],[9.324036],[-7.918322],[-5.853355],[-9.001424],[-3.718950],[9.950114],[5.928031],[-4.510617],[-9.595982],[-8.157584],[3.586503],[0.246560],[-5.516338],[5.538296],[-3.053717],[4.450660],[-6.473451],[1.706023],[4.964912],[-2.032238],[-1.620048],[0.155396],[4.888945],[1.903309],[3.413944],[-1.270833],[2.160922],[-3.693274],[7.063790],[7.041415],[4.518675],[-2.758988],[-7.014045],[-0.446199],[4.178230],[-7.376950],[-7.768317],[9.048149],[2.595580],[0.049235],[0.860956],[0.244124],[9.253111],[-2.003189],[2.997808],[5.307827],[-6.383057],[-1.474655],[4.963415],[-0.064563],[-4.239687],[-9.782464],[-2.278060],[-8.441865],[-7.952115],[-5.913158],[9.659289],[-4.110764],[9.715147],[-1.615480],[2.931621],[-6.834288],[2.535192],[-6.012339],[9.467523],[7.745293],[8.875855],[3.799456],[0.862439],[3.654474],[7.706760],[7.537374],[-4.761168],[-9.349450],[-8.186153],[-1.525192],[-7.955887],[1.216252],[-1.316246],[-1.692367],[-4.939589],[4.943725],[-8.785043],[2.087392],[-7.365290],[4.754994],[2.209527],[3.205083],[5.687014],[0.199879],[-1.193011],[2.440436],[-2.713335],[-9.017278],[-7.136996],[0.777910],[-8.403098],[8.845891],[0.482638],[-7.915904],[3.000519],[1.405298],[1.229251],[-3.241382],[-0.445429],[-8.420998],[-5.733022],[7.301130],[8.772076],[2.696098],[4.540688],[-2.893305],[9.270685],[-6.184372],[3.403332],[-4.617371],[-7.487383],[1.533263],[-4.052914],[-3.457938],[0.510696],[0.307401],[-6.348322],[7.421554],[-0.802532],[-6.079720],[0.664245],[0.476713],[-0.559303],[6.858555],[3.454275],[-3.937759],[5.444654],[4.157201],[-6.755845],[0.887856],[-3.263689],[9.599362],[8.487504],[-7.654009],[4.626634],[7.678906],[-4.614540],[9.290339],[-2.958898],[-6.616728],[-1.747385],[-8.224815],[-5.378733],[-7.245268],[4.613121],[-7.097727],[-2.131554],[1.855802],[-7.578562],[-0.090128],[-6.309420],[-0.756430],[-8.124713],[3.613223],[-3.529726],[-1.561685],[-5.019019],[8.962280],[-5.906366],[9.777894],[9.834355],[-8.875429],[7.529023],[3.510419],[2.516884],[8.336201],[-3.565572],[-5.375811],[4.466129],[7.888105],[7.373172],[7.561496],[-5.678995],[-7.791415],[-0.599585],[3.949834],[-2.207479],[1.709442],[7.432358],[5.542292],[-1.099178],[-4.748127],[1.188946],[-4.782308],[-7.785065],[-7.151661],[1.187792],[2.887311],[-0.637547],[5.560267],[-6.372932],[-9.508599],[-5.518000],[-9.627546],[4.088857],[-1.215680],[5.023082],[-3.796073],[-4.821904],[8.495302],[-0.450799],[-5.209163],[9.084832],[-6.113482],[-4.304670],[-3.548526],[-6.362739],[5.144013],[8.939339],[-5.885946],[5.193620],[-8.354846],[8.003158],[2.363163],[2.993809],[-7.858788],[0.732889],[-3.810070],[-6.247143],[-7.460727],[-0.381629],[2.071095],[-8.994116],[0.512904],[0.569433],[-6.582379],[-6.273617],[8.639889],[8.132232],[2.803212],[9.877304],[-4.576191],[9.591562],[-5.709871],[2.748385],[-4.900991],[4.365858],[-6.378661],[-0.716150],[7.756735],[9.813373],[-2.536328],[3.124504],[0.574398],[3.363928],[8.728074],[-6.707174],[4.440156],[-9.499880],[-0.050386],[-1.090359],[7.784367],[-4.404728],[6.987717],[8.875605],[-0.366926],[-2.011762],[6.593243],[-1.538135],[-9.916600],[8.384388],[9.431397],[-6.694833],[1.733920],[-4.982993],[-7.126326],[-5.704210],[-7.068614],[-0.955400],[7.002002],[3.665946],[-3.162095],[5.556460],[1.169321],[5.801292],[6.781036],[1.585190],[-7.102402],[4.342574],[5.030504],[5.912082],[-0.457882],[1.952551],[0.358056],[9.481166],[-3.377465],[-7.403709],[-7.096013],[-3.669309],[-3.396881],[-8.507305],[-3.982331],[-5.449038],[1.449225],[4.359933],[2.901570],[-5.158933],[-8.142210],[-5.045664],[3.506793],[9.895478],[-8.982418],[9.782978],[3.457386],[-1.048395],[4.836823],[9.833622],[9.227234],[-5.570127],[3.898120],[4.210082],[0.320527],[-1.490884],[0.032424],[3.502720],[-2.800154],[-3.972810],[-5.206561],[-1.707136],[3.672344],[7.557034],[7.769828],[9.979829],[-2.657852],[4.125871],[7.819913],[-0.052391],[-7.875035],[-9.671854],[-9.633562],[1.755525],[-8.895073],[4.016451],[9.635829],[-7.585476],[2.597580],[2.103054],[-2.280564],[8.216727],[-9.345305],[-0.780269],[9.401789],[-5.694995],[-1.285054],[7.944720],[-9.021113],[3.272772],[0.293170],[-3.892250],[-9.298514],[4.254369],[-4.697885],[-9.972505],[9.104592],[-3.871326],[-8.869073],[2.483694],[2.645905],[-0.026913],[3.303705],[-5.690152],[-7.298126],[-5.815827],[7.223174],[-6.718784],[-1.240509],[4.741814],[-3.686248],[8.287896],[4.296756],[3.519349],[5.452381],[9.381389],[7.807786],[-5.224272],[8.275639],[-2.781802],[-1.049076],[3.406532],[8.412608],[-5.063854],[-1.023558],[9.466706],[9.377400],[-8.273079],[-2.214629],[6.514169],[6.195312],[-1.421934],[-2.393384],[4.147966],[-9.494393],[1.869054],[-2.266953],[-1.669479],[-0.020792],[5.819344],[-3.139845],[3.670061],[-6.220290],[-4.998309],[7.010145],[-4.055371],[-8.624163],[9.912473],[5.159853],[-4.405250],[2.012558],[-3.371357],[6.947933],[9.577485],[7.749188],[-3.408364],[5.779217],[-1.673463],[0.803883],[-7.687314],[-9.945445],[5.218525],[-2.874008],[8.239925],[2.132264],[0.442272],[4.335442],[2.681334],[-8.902008],[-1.195904],[4.413558],[8.374787],[-5.393424],[-3.471529],[-1.571794],[-0.631938],[3.277652],[3.921950],[7.933126],[4.351481],[-2.075171],[7.219347],[8.357558],[-6.535934],[5.444531],[2.470631],[7.329908],[-8.692552],[-4.265667],[-6.821572],[3.286934],[1.308197],[-2.491850],[-8.665430],[7.895639],[8.467221],[-4.691873],[8.029554],[7.222463],[4.296232],[-1.637285],[4.878890],[9.163920],[1.210900],[0.681942],[-6.105755],[1.580926],[4.299545],[-0.453809],[4.442724],[-0.786153],[-5.205223],[6.053795],[-5.689743],[0.080090],[5.687059],[-5.502064],[-5.645859],[-0.919066]], dtype = "float32")#candidate|2561|(1232, 1)|const|float32
call_2560 = relay.TupleGetItem(func_2368_call(relay.reshape(const_2561.astype('float32'), [11, 7, 16])), 0)
call_2562 = relay.TupleGetItem(func_2370_call(relay.reshape(const_2561.astype('float32'), [11, 7, 16])), 0)
func_1112_call = mod.get_global_var('func_1112')
func_1115_call = mutated_mod.get_global_var('func_1115')
var_2570 = relay.var("var_2570", dtype = "float32", shape = (50, 1))#candidate|2570|(50, 1)|var|float32
var_2571 = relay.var("var_2571", dtype = "float32", shape = (200,))#candidate|2571|(200,)|var|float32
call_2569 = func_1112_call(relay.reshape(var_2570.astype('float32'), [5, 1, 10]), relay.reshape(var_2571.astype('float32'), [5, 4, 10]), )
call_2572 = func_1112_call(relay.reshape(var_2570.astype('float32'), [5, 1, 10]), relay.reshape(var_2571.astype('float32'), [5, 4, 10]), )
func_1999_call = mod.get_global_var('func_1999')
func_2002_call = mutated_mod.get_global_var('func_2002')
var_2575 = relay.var("var_2575", dtype = "float64", shape = (504,))#candidate|2575|(504,)|var|float64
call_2574 = relay.TupleGetItem(func_1999_call(relay.reshape(var_2575.astype('float64'), [9, 7, 8])), 1)
call_2576 = relay.TupleGetItem(func_2002_call(relay.reshape(var_2575.astype('float64'), [9, 7, 8])), 1)
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_2591 = relay.TupleGetItem(func_2036_call(), 0)
call_2592 = relay.TupleGetItem(func_2038_call(), 0)
bop_2594 = relay.equal(call_2569.astype('bool'), relay.reshape(var_2571.astype('bool'), relay.shape_of(call_2569))) # shape=(5, 4, 10)
bop_2597 = relay.equal(call_2572.astype('bool'), relay.reshape(var_2571.astype('bool'), relay.shape_of(call_2572))) # shape=(5, 4, 10)
output = relay.Tuple([bop_2556,call_2560,const_2561,var_2570,call_2574,var_2575,call_2591,bop_2594,])
output2 = relay.Tuple([bop_2556,call_2562,const_2561,var_2570,call_2576,var_2575,call_2592,bop_2597,])
func_2612 = relay.Function([var_2554,var_2555,var_2570,var_2571,var_2575,], output)
mod['func_2612'] = func_2612
mod = relay.transform.InferType()(mod)
var_2613 = relay.var("var_2613", dtype = "int16", shape = (8, 5, 2))#candidate|2613|(8, 5, 2)|var|int16
var_2614 = relay.var("var_2614", dtype = "int16", shape = (8, 5, 2))#candidate|2614|(8, 5, 2)|var|int16
var_2615 = relay.var("var_2615", dtype = "float32", shape = (50, 1))#candidate|2615|(50, 1)|var|float32
var_2616 = relay.var("var_2616", dtype = "float32", shape = (200,))#candidate|2616|(200,)|var|float32
var_2617 = relay.var("var_2617", dtype = "float64", shape = (504,))#candidate|2617|(504,)|var|float64
output = func_2612(var_2613,var_2614,var_2615,var_2616,var_2617,)
func_2618 = relay.Function([var_2613,var_2614,var_2615,var_2616,var_2617,], output)
mutated_mod['func_2618'] = func_2618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_2708 = relay.TupleGetItem(func_1174_call(), 2)
call_2709 = relay.TupleGetItem(func_1176_call(), 2)
output = relay.Tuple([call_2708,])
output2 = relay.Tuple([call_2709,])
func_2713 = relay.Function([], output)
mod['func_2713'] = func_2713
mod = relay.transform.InferType()(mod)
output = func_2713()
func_2714 = relay.Function([], output)
mutated_mod['func_2714'] = func_2714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_2808 = func_1671_call()
call_2809 = func_1671_call()
output = relay.Tuple([call_2808,])
output2 = relay.Tuple([call_2809,])
func_2816 = relay.Function([], output)
mod['func_2816'] = func_2816
mod = relay.transform.InferType()(mod)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mutated_mod.get_global_var('func_2816')
call_2817 = func_2816_call()
output = call_2817
func_2818 = relay.Function([], output)
mutated_mod['func_2818'] = func_2818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_2866 = relay.TupleGetItem(func_2458_call(), 0)
call_2867 = relay.TupleGetItem(func_2459_call(), 0)
output = relay.Tuple([call_2866,])
output2 = relay.Tuple([call_2867,])
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
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_2892 = relay.TupleGetItem(func_2816_call(), 0)
call_2893 = relay.TupleGetItem(func_2818_call(), 0)
func_123_call = mod.get_global_var('func_123')
func_125_call = mutated_mod.get_global_var('func_125')
const_2904 = relay.const([3.226912,-9.399264,-4.130536,3.161669,-4.378740,5.923518,1.714520,0.386573,4.379369,-1.362047,-9.667573,6.271523,1.878020,-1.305268,-1.177113,1.970911,9.532326,-0.421927,-5.239708,-5.003316,1.828852,9.386994,8.070927,-8.700138,-8.738221,3.303755,1.503467,-2.138113,7.848011,-4.044860,-7.595629,8.645332,8.985979,5.105812,7.277731,4.941806,8.889433,0.714861,6.324706,3.852647,-2.941394,1.903469,6.953664,-4.689315,-6.646844,0.526461,-9.851703,-2.559492,-7.165006,8.326970,0.314043,-3.069332,0.444468,-1.262480,7.662694,-4.631919,-1.741108,5.958704,1.719708,-8.405485,-1.551328,-6.428376,-5.714610,4.371652,-3.521313,-1.892758,1.095237,-1.648972,-4.920360,3.425427,8.678164,1.127638,0.711553,3.039297,-4.811781,-8.618295,9.156715,7.246725,6.215079,-7.814032,4.975218,-8.843838,9.302322,-0.688376,2.414373,5.354774,0.594450,-8.918902,-0.066774,-0.156763,9.467472,4.843297,1.076717,-5.242787,9.533283,5.946314,1.546213,2.326628,-6.142304,-8.492423,-6.366371,-4.504294,-8.642067,-4.108676,6.062177,3.098398,-2.222049,5.155656,8.505415,-9.643446,2.694473,7.988177,5.615524,6.291519,-3.993778,3.536434,-1.157831,4.662304,-7.792069,5.956016,-2.835699,-4.874091,4.569107,-8.970159,0.115389,-9.794901,-0.398430,0.490423,-7.808889,-4.716386,-2.449080,9.439134,6.155865,9.680365,7.106377,4.002341,7.977113,-0.122031,-2.494703,9.932437,1.839096,-8.241891,-2.147217,-9.454376,-3.467511,4.201250,-5.755722,4.841362,3.761473,-8.009870,3.948125,-9.700164,0.813540,-1.768009,-3.240477,-3.251088,4.230701,8.075683,-6.965755,-3.241197,-3.967399,-8.116370,5.362990,2.518140,-8.920245,3.066528,7.716688,0.950405,-0.364757,-3.103399,2.279451,-0.351017,3.161060,-1.497035,9.392317,9.961534,5.420860,0.772016,9.754976,3.065204,-1.078345,-5.787988,8.853877,-7.169020,3.612847,-2.373751,6.967808,3.476934,-5.967109,5.308367,-7.641410,-4.839469,-4.537675,-6.318886,-3.242372,2.559471,-6.305753,-7.762313,6.360129,5.424973,-1.561951,-6.527288,4.182336,-8.056682,3.736937,2.020960,-6.125201,8.926968,5.404147,9.201876,-5.223636,-2.937879,-2.843845,-7.894644,-5.417599,-3.169573,9.395368,-7.968400,-1.256528,-1.010134,-0.350163,3.814612,9.734158,8.113720,7.935025,-8.320439,-6.628943,-7.074642,-7.627715,-5.082337,0.107388,7.791249,7.706933,4.246068,-7.885450,-7.283805,1.030176,-4.215427,-2.486214,-3.845882,-5.860127,5.628676,1.875565,1.591773,-2.877427,-8.699315,-0.857679,-3.849865,-5.767502,0.093140,-9.485897,3.503097,5.515954,-9.256566,-1.520470,8.761950,-7.890178,4.029731,7.050011,4.922944,-6.022830,1.643189,3.758667,5.197494,1.487547,-5.327483,-2.465544,3.464136,3.709106,9.293900,-5.010473,-0.937052,-1.445025,7.277460,-0.717950,9.647263,-7.829527,5.051569,6.761205,8.743029,0.380712,-0.774119,-6.272550,-8.795028,0.781304,4.204996,-6.837421,-6.652982,9.102410,-6.173173,-1.490221,-2.371080,-5.590147,-3.691365,-2.018531,-2.958104,-8.950380,0.244987,4.355155,-6.385707,-8.777200,-2.821870,-3.882106,1.362296,-4.840411,4.352549,5.622068,-2.813601,-2.897976,9.281926,-9.551699,-9.101895,-7.328270,2.211637,7.836969,6.280990,5.033468,0.850718,-4.455443,1.125774,-5.750105,-2.364830,4.611983,-6.667483,2.551653,-7.100710,2.758625,-0.580761,3.589372,9.415625,-0.447690,-8.579245,3.155811,9.323273,-7.632035,-4.571577], dtype = "float64")#candidate|2904|(336,)|const|float64
call_2903 = func_123_call(relay.reshape(const_2904.astype('float64'), [14, 2, 12]))
call_2905 = func_123_call(relay.reshape(const_2904.astype('float64'), [14, 2, 12]))
func_149_call = mod.get_global_var('func_149')
func_151_call = mutated_mod.get_global_var('func_151')
var_2908 = relay.var("var_2908", dtype = "float32", shape = (198,))#candidate|2908|(198,)|var|float32
call_2907 = relay.TupleGetItem(func_149_call(relay.reshape(var_2908.astype('float32'), [6, 3, 11])), 0)
call_2909 = relay.TupleGetItem(func_151_call(relay.reshape(var_2908.astype('float32'), [6, 3, 11])), 0)
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_2910 = relay.TupleGetItem(func_2036_call(), 0)
call_2911 = relay.TupleGetItem(func_2038_call(), 0)
func_1999_call = mod.get_global_var('func_1999')
func_2002_call = mutated_mod.get_global_var('func_2002')
var_2923 = relay.var("var_2923", dtype = "float64", shape = (504,))#candidate|2923|(504,)|var|float64
call_2922 = relay.TupleGetItem(func_1999_call(relay.reshape(var_2923.astype('float64'), [9, 7, 8])), 5)
call_2924 = relay.TupleGetItem(func_2002_call(relay.reshape(var_2923.astype('float64'), [9, 7, 8])), 5)
output = relay.Tuple([call_2892,call_2903,const_2904,call_2907,var_2908,call_2910,call_2922,var_2923,])
output2 = relay.Tuple([call_2893,call_2905,const_2904,call_2909,var_2908,call_2911,call_2924,var_2923,])
func_2949 = relay.Function([var_2908,var_2923,], output)
mod['func_2949'] = func_2949
mod = relay.transform.InferType()(mod)
var_2950 = relay.var("var_2950", dtype = "float32", shape = (198,))#candidate|2950|(198,)|var|float32
var_2951 = relay.var("var_2951", dtype = "float64", shape = (504,))#candidate|2951|(504,)|var|float64
output = func_2949(var_2950,var_2951,)
func_2952 = relay.Function([var_2950,var_2951,], output)
mutated_mod['func_2952'] = func_2952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2872_call = mutated_mod.get_global_var('func_2872')
call_2985 = relay.TupleGetItem(func_2870_call(), 0)
call_2986 = relay.TupleGetItem(func_2872_call(), 0)
output = call_2985
output2 = call_2986
func_2987 = relay.Function([], output)
mod['func_2987'] = func_2987
mod = relay.transform.InferType()(mod)
output = func_2987()
func_2988 = relay.Function([], output)
mutated_mod['func_2988'] = func_2988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_3002 = relay.TupleGetItem(func_1174_call(), 3)
call_3003 = relay.TupleGetItem(func_1176_call(), 3)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_3005 = func_1251_call()
call_3006 = func_1251_call()
func_2612_call = mod.get_global_var('func_2612')
func_2618_call = mutated_mod.get_global_var('func_2618')
const_3014 = relay.const([-7,-7,3,-4,-10,3,-10,-8,5,-5,3,6,-1,3,2,-6,-4,-10,7,-5,-10,2,7,8,-3,7,-10,2,-9,5,-3,-2,6,-8,-5,-1,-1,-6,-2,-8,-9,3,-10,-1,1,2,-8,5,-6,8,-7,-8,-3,-7,-1,2,-2,9,3,2,-7,2,-1,-9,1,10,-8,4,-5,8,8,5,-6,-1,-6,3,-7,9,1,7], dtype = "int16")#candidate|3014|(80,)|const|int16
var_3015 = relay.var("var_3015", dtype = "float32", shape = (50,))#candidate|3015|(50,)|var|float32
const_3016 = relay.const([3.554486,6.982810,-3.958949,-5.560487,1.997137,8.739809,9.176910,-9.436177,6.990003,-6.679460,8.221113,8.528650,-7.914458,-6.895476,3.828701,-4.601219,-8.780143,9.859024,3.274748,-8.695955,-4.794958,5.326999,0.164465,-0.597978,9.774583,8.302023,3.971532,5.319706,7.075941,-8.024669,7.323537,4.287019,-9.360624,1.948454,2.802301,2.545819,7.877622,7.639650,-6.274468,-5.189690,-3.143092,-8.321517,-2.611162,5.561564,5.400741,-4.974551,-2.522334,7.473922,3.480186,-1.911454,-9.245015,-3.712682,-7.681479,-5.833122,7.755661,-5.535800,1.562833,4.066662,1.677386,7.958206,-8.998011,4.726927,-0.715474,-3.887271,7.400093,-0.088087,-9.537248,-2.772258,-1.049161,4.077500,3.888178,1.041783,-7.974044,-7.609216,-9.482442,-4.637013,-3.866744,3.918228,-5.618300,-3.014076,4.351327,-4.919270,0.466123,-8.596111,4.339844,9.094450,-2.534269,1.833888,0.830661,-7.994863,-7.385790,6.660657,-7.187742,0.547165,-7.798601,7.620002,-0.224150,2.293149,-7.983380,5.199058,6.513338,-8.403933,5.741752,-1.857445,3.487478,-0.739317,2.222758,-3.048607,6.303493,1.358578,9.080991,4.234126,-1.341829,8.184484,-7.462295,-1.604692,7.189473,3.587843,9.465709,-0.765323,-0.930212,-6.242562,-3.898495,-4.098263,-8.038672,0.278270,-6.183413,8.158887,2.706158,0.051153,0.077313,8.471244,-5.247829,3.967764,-8.780939,-6.148311,6.327005,-0.084224,-7.968891,1.893079,-6.469823,-2.809401,8.030662,5.227037,4.101262,-1.079937,0.115448,1.912497,3.129529,3.308952,-0.914563,-8.620139,-8.837258,6.764656,1.777444,6.363200,9.129052,-1.436343,9.185014,9.814443,-6.405190,4.431234,5.329512,1.341916,1.153286,-1.400673,5.595801,8.005093,-4.895870,-5.010595,7.175222,5.447174,2.291751,4.654811,-2.801819,0.256079,9.046930,-1.619372,-4.372544,5.939037,-2.735113,5.003785,-7.238145,4.106568,-7.007675,2.862725,9.195740,-6.824115,-4.452254,1.081130,2.064691,-1.353436,0.708586,1.676579,-0.736674,5.199544,3.473261,-7.933035,-4.655036,-2.121578,9.027858,-0.033658,-9.500867,-8.297871,1.295585,2.423796,-7.238677,7.222309,-1.141201,9.889424,5.558006,7.748605,-2.061092,-8.853816,0.425380,9.997728,-3.593129,3.330565,-1.672490,-8.716365,6.064856,-1.337082,3.365838,1.624078,0.859061,-7.642701,-8.307990,4.907906,-8.941756,9.053621,-7.016999,-7.971795,-6.609612,1.718887,9.581849,-2.574555,-0.059873,2.855885,-9.862280,3.247402,9.015997,-1.043608,-5.690235,-6.239141,-3.162767,-8.924661,-8.602886,5.195704,0.146013,-8.520972,-4.059499,1.706173,4.155581,-8.710457,-0.918581,3.870543,-2.692375,5.487816,0.421221,5.423190,3.615331,-6.717082,-2.358497,-1.312204,6.978909,7.203817,-8.462079,-8.112297,1.084035,3.938895,-8.192910,6.222864,2.524655,6.675799,8.382452,-3.630945,3.886036,-2.002700,-4.385872,3.809620,6.767261,-4.457076,2.080689,-0.233837,0.341972,-7.476722,-2.511956,-8.097386,-4.029307,2.043580,-1.474999,-4.311506,-5.060772,-2.140359,-6.248818,-3.173012,-4.071263,0.641208,7.000453,-8.289349,5.063880,9.182557,-1.288477,1.224324,3.922690,-4.382241,-0.051346,6.551557,-6.084142,-1.418046,7.689020,-4.444902,8.235759,-5.424738,8.084304,2.609951,7.809208,4.893905,6.335846,8.978049,7.593696,-7.297476,-3.954553,-1.064681,7.131177,0.035205,-8.477844,-6.246107,1.752220,-5.337513,6.229084,-9.453377,-4.471071,5.934464,-9.889903,9.360210,-3.999997,-5.339720,2.422625,7.449647,1.393230,-8.874164,1.418994,1.125262,0.296335,0.297525,3.115266,8.996812,8.336952,8.159772,0.505076,3.673169,1.292852,1.759881,8.624311,9.487008,5.623017,-4.727806,2.426253,-8.591691,7.415833,1.083275,9.325838,4.301223,9.173101,-2.841774,7.049119,3.674356,8.062705,7.248495,4.056666,8.656660,-3.528811,0.472717,8.110662,-0.266635,-9.317163,-0.338128,6.704358,-2.651700,-8.815250,5.935530,0.985102,-2.842846,9.103758,5.239884,7.911458,-4.906975,-9.474150,9.057501,0.473636,-2.088425,4.342106,5.894476,-4.987213,-4.312912,-8.990986,-1.453598,-0.403528,5.442136,6.454889,-5.318217,6.195325,-4.491345,7.626970,-2.280799,-3.485129,-1.290192,2.521906,-5.120644,1.984601,-0.145309,-1.533331,0.739782,-4.258473,9.087225,4.252991,-6.433463,-6.053624,-7.129001,-3.149752,-6.589957,-9.119518,-9.613369,-2.950887,5.458107,0.813568,6.618684,6.911811,-6.878760,6.239264,1.016497,-1.529172,-1.958903,-3.079777,-0.517618,5.190694,8.553270,4.072680,3.088405,-4.455856,3.061065,-9.420630,-4.938842,-0.901344,0.442838,-1.379876,-7.393654,-0.708651,5.875053,-2.083538,3.468606,-1.867582,4.267546,6.003026,6.768549,5.578111,6.956515,2.538144,0.899791,4.838267,-2.408383,8.125035,-3.717819,9.373755,9.245659,0.762695,6.799586,9.492717,7.769028,1.376257,6.803675,4.004401,-8.357291,-1.899735,-9.638596,4.925818,7.219841,-1.500569,-2.061610,8.522544,7.648006,3.329227,-7.740772,8.625787,4.611600,-4.263750,4.841458,9.790576,-9.490399,-1.785899,5.044303,6.756632,-2.999678,-9.559973,4.283501,-6.461169,-3.462389,0.712959,6.152249,-4.176261,3.393792,5.271167,2.436160], dtype = "float64")#candidate|3016|(504,)|const|float64
call_3013 = relay.TupleGetItem(func_2612_call(relay.reshape(const_3014.astype('int16'), [8, 5, 2]), relay.reshape(const_3014.astype('int16'), [8, 5, 2]), relay.reshape(var_3015.astype('float32'), [50, 1]), relay.reshape(call_3002.astype('float32'), [200,]), relay.reshape(const_3016.astype('float64'), [504,]), ), 6)
call_3017 = relay.TupleGetItem(func_2618_call(relay.reshape(const_3014.astype('int16'), [8, 5, 2]), relay.reshape(const_3014.astype('int16'), [8, 5, 2]), relay.reshape(var_3015.astype('float32'), [50, 1]), relay.reshape(call_3002.astype('float32'), [200,]), relay.reshape(const_3016.astype('float64'), [504,]), ), 6)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_3023 = relay.TupleGetItem(func_1486_call(), 0)
call_3024 = relay.TupleGetItem(func_1488_call(), 0)
uop_3032 = relay.acosh(call_3023.astype('float32')) # shape=(100, 2)
uop_3034 = relay.acosh(call_3024.astype('float32')) # shape=(100, 2)
output = relay.Tuple([call_3002,call_3005,call_3013,const_3014,var_3015,const_3016,uop_3032,])
output2 = relay.Tuple([call_3003,call_3006,call_3017,const_3014,var_3015,const_3016,uop_3034,])
func_3036 = relay.Function([var_3015,], output)
mod['func_3036'] = func_3036
mod = relay.transform.InferType()(mod)
var_3037 = relay.var("var_3037", dtype = "float32", shape = (50,))#candidate|3037|(50,)|var|float32
output = func_3036(var_3037)
func_3038 = relay.Function([var_3037], output)
mutated_mod['func_3038'] = func_3038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2987_call = mod.get_global_var('func_2987')
func_2988_call = mutated_mod.get_global_var('func_2988')
call_3078 = func_2987_call()
call_3079 = func_2987_call()
output = call_3078
output2 = call_3079
func_3085 = relay.Function([], output)
mod['func_3085'] = func_3085
mod = relay.transform.InferType()(mod)
mutated_mod['func_3085'] = func_3085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mutated_mod.get_global_var('func_3085')
call_3086 = func_3085_call()
output = call_3086
func_3087 = relay.Function([], output)
mutated_mod['func_3087'] = func_3087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1323_call = mod.get_global_var('func_1323')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_3096 = func_1323_call()
call_3097 = func_1323_call()
func_1999_call = mod.get_global_var('func_1999')
func_2002_call = mutated_mod.get_global_var('func_2002')
const_3103 = relay.const([[0.276300],[1.516036],[-4.284615],[-5.488147],[-5.639623],[-7.516245],[3.995727],[0.650514],[-5.738241],[-1.614872],[-2.040402],[-1.438963],[0.474956],[-5.306188],[6.814552],[-4.359506],[-6.889361],[-6.508701],[-7.939066],[-9.678532],[3.642628],[-6.073794],[-1.627684],[-2.393437],[-5.377415],[4.392226],[-1.280465],[-6.805307],[8.980537],[0.052447],[-8.973798],[0.745227],[-1.050207],[-1.711309],[-0.523925],[2.562599],[3.170988],[4.249442],[9.036291],[2.898671],[-3.675325],[1.305422],[-4.253333],[-7.596453],[-1.892226],[-5.946970],[9.131261],[2.513030],[5.282766],[3.954189],[2.576708],[8.211369],[-0.180522],[-1.199425],[-6.400219],[-1.273654],[-6.714616],[-4.403338],[0.770692],[-1.856223],[-8.325140],[-0.799272],[7.971609],[2.173574],[7.649254],[-8.718818],[-7.454434],[-4.213874],[-7.599355],[-5.518297],[-4.518122],[4.690422],[-6.628260],[5.916615],[0.136292],[-4.832319],[-0.254557],[9.006102],[-4.700395],[1.090492],[1.528496],[-3.002649],[1.863983],[3.654826],[8.389004],[7.235300],[-7.217396],[-7.982005],[-0.488958],[-4.416073],[-1.251897],[2.879651],[3.730624],[-7.894498],[-7.005439],[-7.141280],[4.208659],[8.445651],[2.763437],[1.002080],[-8.865722],[-8.552208],[8.152114],[-9.790452],[-1.878661],[6.157358],[2.691023],[3.568375],[-4.673465],[-9.636856],[4.227219],[-5.921653],[-2.334337],[-4.970323],[-5.678842],[-5.766294],[-7.155726],[2.509533],[-8.802922],[8.283441],[-0.087271],[5.414621],[5.575632],[7.104198],[-8.747989],[-3.225035],[-1.020724],[-0.172511],[-2.647914],[-8.814619],[-5.175727],[-8.707735],[1.537242],[6.038574],[2.719016],[-5.084773],[0.608061],[2.492659],[-4.303919],[-8.079513],[-2.826477],[9.508732],[-5.637357],[1.162194],[-9.482466],[3.008827],[8.141583],[4.589985],[-4.478824],[-5.227241],[2.935971],[7.164712],[-5.901718],[0.028567],[3.879673],[2.871549],[9.209348],[-3.929255],[-6.994577],[-5.478055],[7.552438],[-7.616757],[5.108891],[0.872019],[-4.962197],[1.458786],[-5.231622],[-8.190890],[7.522087],[-4.798915],[-5.932565],[8.192067],[-5.287611],[5.335990],[6.746150],[0.267397],[9.504866],[9.895810],[3.693305],[-2.602954],[-1.106158],[4.899719],[0.479130],[3.472333],[9.546097],[6.403509],[3.474412],[5.239189],[0.058529],[0.905366],[2.195680],[0.850714],[-9.064100],[3.816351],[-2.842820],[7.303224],[-0.199611],[4.258145],[-7.821712],[-6.351331],[-0.269148],[9.105803],[-2.097809],[2.578836],[8.925863],[2.391684],[9.888944],[-9.154343],[4.690379],[7.717011],[5.174472],[2.286696],[6.192447],[3.197467],[9.723589],[-4.776417],[-9.711445],[-8.521527],[-1.963732],[-6.212717],[-7.373827],[-0.460343],[-7.604905],[4.546348],[9.584060],[0.029721],[8.920645],[-1.179538],[-4.740335],[-0.938478],[6.709980],[3.172482],[0.510245],[2.214988],[-1.630476],[2.155240],[3.549780],[-3.780068],[-6.094186],[2.269462],[1.911339],[9.267598],[1.420532],[8.577076],[0.340821],[-1.985961],[-5.074645],[-5.674457],[0.863719],[-8.683776],[8.246652],[-2.151077],[7.586138],[4.884844],[-6.682609],[2.533554],[1.610311],[-7.563372],[-9.338222],[-5.917743],[5.417917],[3.568997],[7.395721],[8.091990],[5.578476],[-5.538228],[-1.042588],[6.533324],[7.731634],[1.219728],[7.537946],[9.361456],[5.141156],[-1.425804],[-9.957383],[-4.079703],[3.457801],[8.465908],[1.512741],[6.248318],[-3.289487],[-9.458450],[-3.345269],[5.558649],[-8.938844],[6.375337],[2.107812],[-2.261441],[-8.738180],[5.767402],[-8.573859],[-8.272104],[2.015651],[-5.954103],[1.422111],[3.348944],[2.141320],[-3.293053],[7.638821],[9.791025],[-2.808291],[2.840566],[-3.018302],[4.371171],[-3.299079],[8.203083],[-3.796219],[-8.057398],[3.013973],[-9.836672],[-2.100712],[0.545504],[6.066721],[1.793020],[1.367005],[-2.833183],[2.263784],[8.527883],[-3.285250],[-5.558691],[7.831926],[9.813658],[-2.383990],[4.077850],[-3.410829],[-0.788774],[7.109255],[-8.235718],[0.118455],[7.082925],[-0.969842],[-5.457824],[-4.687968],[0.928885],[-9.587920],[1.071348],[3.365053],[2.231487],[2.291868],[-3.177545],[4.210415],[-0.557862],[-7.513504],[6.983001],[1.856788],[-0.052595],[2.991316],[7.093055],[-5.979098],[-2.330732],[2.353454],[6.627773],[-6.642649],[-5.278115],[5.776699],[6.145452],[0.816905],[-7.953999],[-6.405624],[0.586382],[-7.179117],[3.238862],[-0.392934],[5.617209],[-2.542917],[-9.094044],[-6.182966],[-6.208943],[-8.120098],[-6.153063],[7.763687],[-2.823725],[9.857727],[-0.791259],[6.424979],[1.754966],[5.946154],[5.404555],[-3.596189],[2.527862],[-1.683246],[-3.073453],[1.770731],[2.696358],[6.140327],[6.979325],[0.649368],[2.390270],[-9.336954],[-3.923182],[2.621883],[-7.169110],[-9.247475],[-8.160071],[-6.569131],[7.005838],[0.637062],[7.767659],[5.340012],[4.701387],[-4.705504],[7.201979],[-2.150822],[5.342002],[3.019932],[-0.600299],[3.261203],[2.929476],[-6.403755],[-5.555749],[9.998352],[3.144613],[6.047934],[4.563005],[7.694131],[8.164644],[-2.688086],[8.456271],[0.400607],[4.992605],[-7.338599],[7.632849],[-7.823407],[-1.945575],[2.936898],[-8.678319],[-8.186820],[2.919064],[-9.327736],[-4.827953],[0.859680],[-4.256778],[4.522376],[2.346624],[-9.176065],[1.288700],[-4.329976],[-2.375551],[7.231953],[-2.210658],[-8.152213],[-7.845494],[-4.821111],[-3.461104],[-7.361181],[1.049510],[4.176940],[2.886436],[1.856285],[0.533513],[-0.319166],[7.539362],[-9.215871],[6.914588],[-4.709589],[-9.290299],[-2.449920],[1.046817],[-8.168624],[-9.888822],[8.229486],[7.199699],[2.924634],[3.602332],[8.330733],[-5.146214],[4.076802],[-5.282712],[6.880534],[5.577080],[8.039683],[-5.516957],[-1.485412],[5.311707],[-4.385960],[-5.034294],[4.602246],[-2.749440],[-7.937253],[3.917044],[-6.526285],[7.120141],[9.506844],[4.010585],[-7.730000],[-0.943164],[-1.290529],[7.141155],[0.041440],[-6.375323],[-6.784103],[8.913440],[-4.459686],[-5.881843],[1.799423],[-5.731112],[8.238289],[2.497647],[2.627735],[-5.139038],[4.704121],[-5.751821],[0.154518],[5.878549]], dtype = "float64")#candidate|3103|(504, 1)|const|float64
call_3102 = relay.TupleGetItem(func_1999_call(relay.reshape(const_3103.astype('float64'), [9, 7, 8])), 5)
call_3104 = relay.TupleGetItem(func_2002_call(relay.reshape(const_3103.astype('float64'), [9, 7, 8])), 5)
output = relay.Tuple([call_3096,call_3102,const_3103,])
output2 = relay.Tuple([call_3097,call_3104,const_3103,])
func_3107 = relay.Function([], output)
mod['func_3107'] = func_3107
mod = relay.transform.InferType()(mod)
output = func_3107()
func_3108 = relay.Function([], output)
mutated_mod['func_3108'] = func_3108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_3145 = func_3085_call()
call_3146 = func_3085_call()
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_3153 = func_1251_call()
call_3154 = func_1251_call()
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_3169 = func_1308_call()
call_3170 = func_1308_call()
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_3171 = relay.TupleGetItem(func_2036_call(), 0)
call_3172 = relay.TupleGetItem(func_2038_call(), 0)
output = relay.Tuple([call_3145,call_3153,call_3169,call_3171,])
output2 = relay.Tuple([call_3146,call_3154,call_3170,call_3172,])
func_3183 = relay.Function([], output)
mod['func_3183'] = func_3183
mod = relay.transform.InferType()(mod)
output = func_3183()
func_3184 = relay.Function([], output)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2177_call = mod.get_global_var('func_2177')
func_2179_call = mutated_mod.get_global_var('func_2179')
call_3296 = func_2177_call()
call_3297 = func_2177_call()
output = relay.Tuple([call_3296,])
output2 = relay.Tuple([call_3297,])
func_3300 = relay.Function([], output)
mod['func_3300'] = func_3300
mod = relay.transform.InferType()(mod)
output = func_3300()
func_3301 = relay.Function([], output)
mutated_mod['func_3301'] = func_3301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3321 = relay.var("var_3321", dtype = "float32", shape = (2, 9, 2))#candidate|3321|(2, 9, 2)|var|float32
var_3322 = relay.var("var_3322", dtype = "float32", shape = (2, 9, 2))#candidate|3322|(2, 9, 2)|var|float32
bop_3323 = relay.mod(var_3321.astype('float32'), relay.reshape(var_3322.astype('float32'), relay.shape_of(var_3321))) # shape=(2, 9, 2)
output = relay.Tuple([bop_3323,])
output2 = relay.Tuple([bop_3323,])
func_3330 = relay.Function([var_3321,var_3322,], output)
mod['func_3330'] = func_3330
mod = relay.transform.InferType()(mod)
mutated_mod['func_3330'] = func_3330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3330_call = mutated_mod.get_global_var('func_3330')
var_3332 = relay.var("var_3332", dtype = "float32", shape = (2, 9, 2))#candidate|3332|(2, 9, 2)|var|float32
var_3333 = relay.var("var_3333", dtype = "float32", shape = (2, 9, 2))#candidate|3333|(2, 9, 2)|var|float32
call_3331 = func_3330_call(var_3332,var_3333,)
output = call_3331
func_3334 = relay.Function([var_3332,var_3333,], output)
mutated_mod['func_3334'] = func_3334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3339 = relay.var("var_3339", dtype = "float32", shape = (15, 6, 3))#candidate|3339|(15, 6, 3)|var|float32
uop_3340 = relay.asin(var_3339.astype('float32')) # shape=(15, 6, 3)
func_1538_call = mod.get_global_var('func_1538')
func_1539_call = mutated_mod.get_global_var('func_1539')
call_3359 = relay.TupleGetItem(func_1538_call(), 0)
call_3360 = relay.TupleGetItem(func_1539_call(), 0)
func_1649_call = mod.get_global_var('func_1649')
func_1652_call = mutated_mod.get_global_var('func_1652')
var_3366 = relay.var("var_3366", dtype = "int16", shape = (1680,))#candidate|3366|(1680,)|var|int16
call_3365 = relay.TupleGetItem(func_1649_call(relay.reshape(var_3366.astype('int16'), [16, 7, 15])), 0)
call_3367 = relay.TupleGetItem(func_1652_call(relay.reshape(var_3366.astype('int16'), [16, 7, 15])), 0)
func_123_call = mod.get_global_var('func_123')
func_125_call = mutated_mod.get_global_var('func_125')
var_3373 = relay.var("var_3373", dtype = "float64", shape = (336,))#candidate|3373|(336,)|var|float64
call_3372 = func_123_call(relay.reshape(var_3373.astype('float64'), [14, 2, 12]))
call_3374 = func_123_call(relay.reshape(var_3373.astype('float64'), [14, 2, 12]))
output = relay.Tuple([uop_3340,call_3359,call_3365,var_3366,call_3372,var_3373,])
output2 = relay.Tuple([uop_3340,call_3360,call_3367,var_3366,call_3374,var_3373,])
func_3376 = relay.Function([var_3339,var_3366,var_3373,], output)
mod['func_3376'] = func_3376
mod = relay.transform.InferType()(mod)
mutated_mod['func_3376'] = func_3376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3376_call = mutated_mod.get_global_var('func_3376')
var_3378 = relay.var("var_3378", dtype = "float32", shape = (15, 6, 3))#candidate|3378|(15, 6, 3)|var|float32
var_3379 = relay.var("var_3379", dtype = "int16", shape = (1680,))#candidate|3379|(1680,)|var|int16
var_3380 = relay.var("var_3380", dtype = "float64", shape = (336,))#candidate|3380|(336,)|var|float64
call_3377 = func_3376_call(var_3378,var_3379,var_3380,)
output = call_3377
func_3381 = relay.Function([var_3378,var_3379,var_3380,], output)
mutated_mod['func_3381'] = func_3381
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3403 = relay.var("var_3403", dtype = "float32", shape = (1, 6, 4))#candidate|3403|(1, 6, 4)|var|float32
const_3404 = relay.const([[[8.699890,6.621382,-3.690347,7.427766],[-5.295939,0.710896,-7.096191,-8.211655],[-5.736705,-9.971564,-4.464193,-4.564155],[8.400780,8.407963,-5.161937,8.110857],[4.282266,-8.526260,-6.948447,-2.829563],[3.370521,8.633022,9.024144,3.838829]]], dtype = "float32")#candidate|3404|(1, 6, 4)|const|float32
bop_3405 = relay.floor_mod(var_3403.astype('float32'), relay.reshape(const_3404.astype('float32'), relay.shape_of(var_3403))) # shape=(1, 6, 4)
uop_3414 = relay.cosh(const_3404.astype('float32')) # shape=(1, 6, 4)
func_1015_call = mod.get_global_var('func_1015')
func_1018_call = mutated_mod.get_global_var('func_1018')
var_3418 = relay.var("var_3418", dtype = "int32", shape = (234,))#candidate|3418|(234,)|var|int32
call_3417 = relay.TupleGetItem(func_1015_call(relay.reshape(var_3418.astype('int32'), [13, 3, 6]), relay.reshape(var_3418.astype('int32'), [13, 3, 6]), ), 1)
call_3419 = relay.TupleGetItem(func_1018_call(relay.reshape(var_3418.astype('int32'), [13, 3, 6]), relay.reshape(var_3418.astype('int32'), [13, 3, 6]), ), 1)
output = relay.Tuple([bop_3405,uop_3414,call_3417,var_3418,])
output2 = relay.Tuple([bop_3405,uop_3414,call_3419,var_3418,])
func_3422 = relay.Function([var_3403,var_3418,], output)
mod['func_3422'] = func_3422
mod = relay.transform.InferType()(mod)
var_3423 = relay.var("var_3423", dtype = "float32", shape = (1, 6, 4))#candidate|3423|(1, 6, 4)|var|float32
var_3424 = relay.var("var_3424", dtype = "int32", shape = (234,))#candidate|3424|(234,)|var|int32
output = func_3422(var_3423,var_3424,)
func_3425 = relay.Function([var_3423,var_3424,], output)
mutated_mod['func_3425'] = func_3425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_3470 = func_1850_call()
call_3471 = func_1850_call()
uop_3488 = relay.cosh(call_3470.astype('float64')) # shape=(9, 1, 8)
uop_3490 = relay.cosh(call_3471.astype('float64')) # shape=(9, 1, 8)
func_1614_call = mod.get_global_var('func_1614')
func_1617_call = mutated_mod.get_global_var('func_1617')
var_3496 = relay.var("var_3496", dtype = "float32", shape = (200,))#candidate|3496|(200,)|var|float32
call_3495 = relay.TupleGetItem(func_1614_call(relay.reshape(var_3496.astype('float32'), [100, 2])), 0)
call_3497 = relay.TupleGetItem(func_1617_call(relay.reshape(var_3496.astype('float32'), [100, 2])), 0)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_3500 = func_3085_call()
call_3501 = func_3085_call()
bop_3504 = relay.logical_and(uop_3488.astype('bool'), relay.reshape(call_3500.astype('bool'), relay.shape_of(uop_3488))) # shape=(9, 1, 8)
bop_3507 = relay.logical_and(uop_3490.astype('bool'), relay.reshape(call_3501.astype('bool'), relay.shape_of(uop_3490))) # shape=(9, 1, 8)
output = relay.Tuple([call_3495,var_3496,bop_3504,])
output2 = relay.Tuple([call_3497,var_3496,bop_3507,])
func_3508 = relay.Function([var_3496,], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
var_3509 = relay.var("var_3509", dtype = "float32", shape = (200,))#candidate|3509|(200,)|var|float32
output = func_3508(var_3509)
func_3510 = relay.Function([var_3509], output)
mutated_mod['func_3510'] = func_3510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3512 = relay.TupleGetItem(func_3183_call(), 3)
call_3513 = relay.TupleGetItem(func_3184_call(), 3)
output = relay.Tuple([call_3512,])
output2 = relay.Tuple([call_3513,])
func_3524 = relay.Function([], output)
mod['func_3524'] = func_3524
mod = relay.transform.InferType()(mod)
mutated_mod['func_3524'] = func_3524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mutated_mod.get_global_var('func_3524')
call_3525 = func_3524_call()
output = call_3525
func_3526 = relay.Function([], output)
mutated_mod['func_3526'] = func_3526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_3537 = func_1671_call()
call_3538 = func_1671_call()
output = relay.Tuple([call_3537,])
output2 = relay.Tuple([call_3538,])
func_3542 = relay.Function([], output)
mod['func_3542'] = func_3542
mod = relay.transform.InferType()(mod)
mutated_mod['func_3542'] = func_3542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mutated_mod.get_global_var('func_3542')
call_3543 = func_3542_call()
output = call_3543
func_3544 = relay.Function([], output)
mutated_mod['func_3544'] = func_3544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_3603 = relay.TupleGetItem(func_2036_call(), 0)
call_3604 = relay.TupleGetItem(func_2038_call(), 0)
func_1836_call = mod.get_global_var('func_1836')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_3636 = relay.var("var_3636", dtype = "float64", shape = (504, 2))#candidate|3636|(504, 2)|var|float64
call_3635 = relay.TupleGetItem(func_1836_call(relay.reshape(var_3636.astype('float64'), [9, 14, 8])), 0)
call_3637 = relay.TupleGetItem(func_1838_call(relay.reshape(var_3636.astype('float64'), [9, 14, 8])), 0)
output = relay.Tuple([call_3603,call_3635,var_3636,])
output2 = relay.Tuple([call_3604,call_3637,var_3636,])
func_3645 = relay.Function([var_3636,], output)
mod['func_3645'] = func_3645
mod = relay.transform.InferType()(mod)
mutated_mod['func_3645'] = func_3645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3646 = relay.var("var_3646", dtype = "float64", shape = (504, 2))#candidate|3646|(504, 2)|var|float64
func_3645_call = mutated_mod.get_global_var('func_3645')
call_3647 = func_3645_call(var_3646)
output = call_3647
func_3648 = relay.Function([var_3646], output)
mutated_mod['func_3648'] = func_3648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_3657 = func_3085_call()
call_3658 = func_3085_call()
output = call_3657
output2 = call_3658
func_3659 = relay.Function([], output)
mod['func_3659'] = func_3659
mod = relay.transform.InferType()(mod)
output = func_3659()
func_3660 = relay.Function([], output)
mutated_mod['func_3660'] = func_3660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_3680 = relay.TupleGetItem(func_1486_call(), 2)
call_3681 = relay.TupleGetItem(func_1488_call(), 2)
func_149_call = mod.get_global_var('func_149')
func_151_call = mutated_mod.get_global_var('func_151')
const_3687 = relay.const([0.237094,-1.776897,4.624865,8.153237,9.373651,-4.406908,9.448985,-5.687883,-9.711602,4.872059,-3.146126,-4.850875,7.545627,-3.237626,2.259796,3.962503,9.735513,0.177267,0.877939,8.752132,5.520743,2.321401,9.608480,-1.866746,-6.048998,-6.014142,-8.570576,2.288241,5.115235,-4.309892,-5.381934,-3.823719,-0.610991,5.517667,-8.969867,-0.927399,-1.869711,0.660205,-6.703128,6.129331,7.471132,5.197101,5.540115,-0.703204,-1.108873,4.178585,-8.480441,-4.603153,-8.967936,-6.857458,-4.291733,-0.601152,-8.229765,-0.236270,-8.748892,5.756145,8.397464,7.748028,2.186193,-3.876774,-8.865881,0.226163,9.933976,6.917140,9.690350,-6.323951,9.859251,-1.843768,-7.592830,-0.162871,0.346047,1.614252,-7.482649,0.134562,-6.499537,3.610254,6.688899,3.792085,-9.868250,-7.446874,-0.839248,-6.881788,-0.568718,4.325581,0.246400,0.037026,5.515330,-1.933544,2.737776,6.882498,2.606601,-7.750562,3.909792,8.175512,4.784821,0.272807,-2.771139,9.240160,5.296932,-8.188269,-6.753642,1.599702,-2.842473,2.087004,5.086752,8.787551,2.220594,9.070477,5.069588,-6.975297,6.665414,-7.485580,0.626872,-3.288665,-0.847201,-2.835986,-3.012407,-4.907338,6.978116,-0.280474,-5.409938,4.848110,2.604500,6.251575,1.338046,5.328617,0.847276,-4.526762,6.583598,0.144856,4.542638,-8.292196,1.464829,-0.669364,-0.352824,7.258913,-1.633246,-3.509780,-1.422495,-5.079775,-8.384973,-7.180654,9.451577,-9.581083,8.854454,-1.108350,6.456723,-5.674013,3.937782,9.265803,5.603885,4.219226,9.836507,2.304328,5.411236,0.694062,-2.643909,3.878684,3.356167,-4.400372,-8.407417,7.246877,-7.011536,-8.359964,6.821403,7.800452,0.731707,-9.371737,9.610355,-9.481813,-5.684528,-8.621525,6.362613,-5.322007,0.293136,0.008728,-6.942059,-9.832456,-8.262857,-6.677313,-5.802209,-4.875793,-1.940540,8.447923,-2.774965,-0.951067,8.366010,9.053057,5.822469,0.448072,2.507366,-6.370877,-1.981924,-3.644436,2.157501,-8.080198,-1.790887,8.845457], dtype = "float32")#candidate|3687|(198,)|const|float32
call_3686 = relay.TupleGetItem(func_149_call(relay.reshape(const_3687.astype('float32'), [6, 3, 11])), 0)
call_3688 = relay.TupleGetItem(func_151_call(relay.reshape(const_3687.astype('float32'), [6, 3, 11])), 0)
func_1323_call = mod.get_global_var('func_1323')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_3689 = func_1323_call()
call_3690 = func_1323_call()
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_3699 = func_2499_call()
call_3700 = func_2499_call()
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_3704 = func_3085_call()
call_3705 = func_3085_call()
output = relay.Tuple([call_3680,call_3686,const_3687,call_3689,call_3699,call_3704,])
output2 = relay.Tuple([call_3681,call_3688,const_3687,call_3690,call_3700,call_3705,])
func_3713 = relay.Function([], output)
mod['func_3713'] = func_3713
mod = relay.transform.InferType()(mod)
output = func_3713()
func_3714 = relay.Function([], output)
mutated_mod['func_3714'] = func_3714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_3735 = relay.TupleGetItem(func_1745_call(), 0)
call_3736 = relay.TupleGetItem(func_1746_call(), 0)
func_2436_call = mod.get_global_var('func_2436')
func_2438_call = mutated_mod.get_global_var('func_2438')
call_3746 = relay.TupleGetItem(func_2436_call(), 0)
call_3747 = relay.TupleGetItem(func_2438_call(), 0)
output = relay.Tuple([call_3735,call_3746,])
output2 = relay.Tuple([call_3736,call_3747,])
func_3753 = relay.Function([], output)
mod['func_3753'] = func_3753
mod = relay.transform.InferType()(mod)
output = func_3753()
func_3754 = relay.Function([], output)
mutated_mod['func_3754'] = func_3754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_3779 = func_3085_call()
call_3780 = func_3085_call()
output = call_3779
output2 = call_3780
func_3781 = relay.Function([], output)
mod['func_3781'] = func_3781
mod = relay.transform.InferType()(mod)
mutated_mod['func_3781'] = func_3781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mutated_mod.get_global_var('func_3781')
call_3782 = func_3781_call()
output = call_3782
func_3783 = relay.Function([], output)
mutated_mod['func_3783'] = func_3783
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3805 = relay.var("var_3805", dtype = "float32", shape = (11, 5, 9))#candidate|3805|(11, 5, 9)|var|float32
uop_3806 = relay.rsqrt(var_3805.astype('float32')) # shape=(11, 5, 9)
output = uop_3806
output2 = uop_3806
func_3814 = relay.Function([var_3805,], output)
mod['func_3814'] = func_3814
mod = relay.transform.InferType()(mod)
var_3815 = relay.var("var_3815", dtype = "float32", shape = (11, 5, 9))#candidate|3815|(11, 5, 9)|var|float32
output = func_3814(var_3815)
func_3816 = relay.Function([var_3815], output)
mutated_mod['func_3816'] = func_3816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_3821 = func_1857_call()
call_3822 = func_1857_call()
output = relay.Tuple([call_3821,])
output2 = relay.Tuple([call_3822,])
func_3829 = relay.Function([], output)
mod['func_3829'] = func_3829
mod = relay.transform.InferType()(mod)
output = func_3829()
func_3830 = relay.Function([], output)
mutated_mod['func_3830'] = func_3830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mod.get_global_var('func_3524')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_3853 = relay.TupleGetItem(func_3524_call(), 0)
call_3854 = relay.TupleGetItem(func_3526_call(), 0)
func_2177_call = mod.get_global_var('func_2177')
func_2179_call = mutated_mod.get_global_var('func_2179')
call_3855 = func_2177_call()
call_3856 = func_2177_call()
bop_3857 = relay.right_shift(call_3853.astype('uint8'), relay.reshape(call_3855.astype('uint8'), relay.shape_of(call_3853))) # shape=(9, 1, 8)
bop_3860 = relay.right_shift(call_3854.astype('uint8'), relay.reshape(call_3856.astype('uint8'), relay.shape_of(call_3854))) # shape=(9, 1, 8)
func_2612_call = mod.get_global_var('func_2612')
func_2618_call = mutated_mod.get_global_var('func_2618')
const_3874 = relay.const([[-8,-6],[-9,6],[9,-3],[-2,-7],[-7,-9],[7,4],[-4,5],[9,-7],[-2,-3],[-3,10],[-10,9],[5,-10],[2,9],[-3,-3],[-10,-4],[-2,7],[7,4],[-8,2],[-9,-1],[-8,9],[2,1],[-2,10],[-5,-10],[-9,-10],[4,6],[8,1],[10,2],[-5,-2],[-8,4],[-9,10],[1,2],[7,-6],[-6,5],[10,-1],[-8,-10],[5,-3],[5,3],[-2,-8],[4,-2],[-2,2]], dtype = "int16")#candidate|3874|(40, 2)|const|int16
var_3875 = relay.var("var_3875", dtype = "float32", shape = (50,))#candidate|3875|(50,)|var|float32
var_3876 = relay.var("var_3876", dtype = "float32", shape = (50, 4))#candidate|3876|(50, 4)|var|float32
const_3877 = relay.const([2.696823,6.472672,-2.050080,-1.753131,2.517083,0.880050,4.968765,5.467786,5.264784,2.778229,-9.127110,-0.518610,-8.080644,1.093680,9.436001,-6.101246,5.683183,-9.674236,4.655857,-6.111618,6.507070,-9.614472,-8.481381,1.889200,7.039569,8.867883,4.039611,2.247720,-2.496589,8.920401,8.923451,-3.868606,8.594055,5.430617,9.337056,-9.971125,5.479777,-2.955376,-2.957523,3.895227,-0.876835,0.461203,-4.354733,-4.948451,6.079496,-7.979603,7.407510,-8.134431,1.226608,6.354693,7.106020,-0.964808,8.871721,3.654025,-4.248238,9.160643,8.971853,-2.032339,7.074742,-8.599122,1.800395,-3.216701,5.011570,0.842942,-6.656432,-8.677687,-8.077511,-2.253702,3.513031,-7.873586,-2.610028,-3.446896,-7.843051,0.194487,9.974153,3.156461,-3.138861,9.623860,-5.282324,-4.796775,-8.364272,-7.908543,2.972007,-7.161718,-5.159878,6.602772,-8.502079,-3.490301,-7.539143,3.824967,6.479463,-2.481358,-6.805738,-5.746225,8.229650,0.109214,9.992594,-6.784035,-3.248723,4.326596,6.589162,4.877117,-4.064497,6.376466,0.021085,1.524181,4.591316,-1.268246,6.081105,-8.650795,0.077418,-1.180893,6.741308,-0.249771,6.607868,9.895529,-1.756250,7.442677,-5.006861,2.370472,9.727491,4.515553,4.411716,-7.729672,-5.544942,2.141574,-9.785875,-1.720949,-6.189839,6.986726,-7.976330,9.985058,5.843992,5.069557,1.114533,0.339578,0.214300,9.003181,-6.418115,-4.719659,-7.157605,-4.679422,1.942942,-1.112816,6.392784,-0.752326,-8.491002,-9.601517,-9.422413,-1.411455,0.094979,-6.025142,-6.577660,9.712154,4.873227,0.498467,1.633220,-8.886458,-0.436677,-3.480210,-0.405848,3.383547,-9.462797,-3.046682,6.082004,-3.900504,-8.460040,-3.113421,-5.796425,0.527309,9.184202,7.541523,-3.299277,3.479349,7.309997,9.628236,-1.303372,-3.555177,-8.094093,6.072603,7.454551,-2.893379,-4.814991,-9.366524,-9.265763,-3.425537,-4.946367,-7.870998,5.190494,5.612588,-9.595588,-7.055343,7.784086,5.864278,8.942505,-6.144097,9.281819,-7.300096,7.677545,-3.684896,-9.817286,4.072461,7.594235,-0.586137,8.798636,3.430495,-3.848526,7.645177,-1.379017,0.186133,8.676729,6.769866,9.372588,4.961599,-0.062252,-6.777060,-7.316498,-3.754894,-6.962509,1.082825,-3.618823,1.515046,-4.064847,9.585015,4.283749,9.581700,-8.395936,0.455362,-3.906252,-1.895616,4.105341,-3.348188,-5.842892,0.117574,0.228402,-7.255277,5.357416,-9.252493,-4.322696,-1.320327,-4.642505,4.116834,-4.265649,-4.622592,8.315906,-9.766765,-6.092569,-1.287885,2.912632,4.356775,-1.387591,-3.593364,1.029696,-6.075635,-8.375502,0.620441,-6.488447,2.353119,-7.789157,2.016168,-4.082597,-4.208814,-9.581897,8.911221,-2.270651,-5.630495,3.715305,-7.160154,0.483656,-9.144616,7.803215,9.725511,-5.215491,8.735512,-9.094920,-9.771801,-3.570064,7.741478,-7.479963,-5.770708,5.310920,8.046830,6.832598,7.290008,-9.733422,8.067251,-4.791247,6.114642,2.989906,8.246331,-1.237555,6.089728,-4.051945,8.791493,1.647459,2.882424,3.101857,7.977221,-4.490770,1.585874,2.629266,-4.201727,3.297907,-5.161808,-4.253159,7.876191,-5.374845,5.984374,2.409373,1.638323,-9.619919,-9.454517,6.014897,1.459458,-0.073684,6.526241,6.665507,5.676802,7.557744,5.441426,0.901746,-1.702699,1.718145,-3.895095,6.885251,-4.792133,-1.357501,2.580059,-6.096254,7.222337,2.736833,-2.767782,6.704544,-6.704839,-0.808027,-8.668999,-0.179794,1.285583,6.095100,-6.176356,4.410253,-1.167447,9.848757,5.993001,-7.360000,3.903000,1.952914,-3.170984,9.152465,-9.842216,8.317155,-3.561078,1.371331,1.718602,4.209160,4.011600,-2.707768,7.916416,9.822236,-6.097470,9.525428,-1.391651,2.654348,9.029337,9.732539,-3.778984,4.867960,-6.008880,-6.676600,3.993411,0.271649,-4.379086,-8.853578,-2.450702,9.010060,-7.291652,-7.746236,0.497215,0.294428,-3.798652,-2.522502,7.107258,5.343904,3.447039,-5.039474,-5.164061,2.289576,5.416559,-0.030748,-5.754609,-3.161756,-5.422579,6.283517,3.991731,5.618914,4.107170,-6.826467,2.051695,-3.386102,-2.951762,1.238744,-0.217747,1.785453,-5.673717,2.331118,8.753230,6.597334,-0.118864,-8.666780,-0.061272,-4.664291,5.667953,-1.979598,-5.826563,0.574062,8.532116,4.535626,-4.063665,-8.110857,-3.119491,3.468637,8.664237,-1.256319,4.859433,8.534172,-3.687716,2.308058,5.045229,-2.384016,-2.354189,-1.832500,-2.090929,0.792025,-0.998420,7.429522,-0.906248,5.769562,-3.553385,7.656698,-7.765408,4.623594,-1.350618,-7.389950,-4.921647,-2.365410,3.371595,2.226561,-0.401666,-0.928777,-5.024699,-5.451720,-6.746290,-9.939285,6.714617,-7.129405,2.144702,-3.834990,-6.851445,7.376572,5.251606,3.650963,-8.975635,-3.222032,7.277399,8.172981,-4.082423,-9.822448,7.533974,0.004749,7.007884,-1.781299,7.153922,-5.550228,-7.049081,1.722657,0.243426,-9.176636,6.236148,6.033403,8.341252,-2.503016,-6.126622,-4.468598,7.550460,-8.257566,9.823933,6.439255,1.370925,-6.507520,5.782249,7.917825,-2.474809,-4.426462,-3.917153,-6.766285,4.051343,3.344837,-3.515007,8.832386,-6.171825,-0.135710,3.014061,-5.585285,5.959290], dtype = "float64")#candidate|3877|(504,)|const|float64
call_3873 = relay.TupleGetItem(func_2612_call(relay.reshape(const_3874.astype('int16'), [8, 5, 2]), relay.reshape(const_3874.astype('int16'), [8, 5, 2]), relay.reshape(var_3875.astype('float32'), [50, 1]), relay.reshape(var_3876.astype('float32'), [200,]), relay.reshape(const_3877.astype('float64'), [504,]), ), 5)
call_3878 = relay.TupleGetItem(func_2618_call(relay.reshape(const_3874.astype('int16'), [8, 5, 2]), relay.reshape(const_3874.astype('int16'), [8, 5, 2]), relay.reshape(var_3875.astype('float32'), [50, 1]), relay.reshape(var_3876.astype('float32'), [200,]), relay.reshape(const_3877.astype('float64'), [504,]), ), 5)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_3882 = func_2499_call()
call_3883 = func_2499_call()
bop_3887 = relay.bitwise_xor(call_3855.astype('uint16'), relay.reshape(call_3882.astype('uint16'), relay.shape_of(call_3855))) # shape=(9, 1, 8)
bop_3890 = relay.bitwise_xor(call_3856.astype('uint16'), relay.reshape(call_3883.astype('uint16'), relay.shape_of(call_3856))) # shape=(9, 1, 8)
func_3829_call = mod.get_global_var('func_3829')
func_3830_call = mutated_mod.get_global_var('func_3830')
call_3893 = relay.TupleGetItem(func_3829_call(), 0)
call_3894 = relay.TupleGetItem(func_3830_call(), 0)
output = relay.Tuple([bop_3857,call_3873,const_3874,var_3875,var_3876,const_3877,bop_3887,call_3893,])
output2 = relay.Tuple([bop_3860,call_3878,const_3874,var_3875,var_3876,const_3877,bop_3890,call_3894,])
func_3896 = relay.Function([var_3875,var_3876,], output)
mod['func_3896'] = func_3896
mod = relay.transform.InferType()(mod)
var_3897 = relay.var("var_3897", dtype = "float32", shape = (50,))#candidate|3897|(50,)|var|float32
var_3898 = relay.var("var_3898", dtype = "float32", shape = (50, 4))#candidate|3898|(50, 4)|var|float32
output = func_3896(var_3897,var_3898,)
func_3899 = relay.Function([var_3897,var_3898,], output)
mutated_mod['func_3899'] = func_3899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_3918 = func_1850_call()
call_3919 = func_1850_call()
uop_3931 = relay.rsqrt(call_3918.astype('float32')) # shape=(9, 1, 8)
uop_3933 = relay.rsqrt(call_3919.astype('float32')) # shape=(9, 1, 8)
output = relay.Tuple([uop_3931,])
output2 = relay.Tuple([uop_3933,])
func_3937 = relay.Function([], output)
mod['func_3937'] = func_3937
mod = relay.transform.InferType()(mod)
output = func_3937()
func_3938 = relay.Function([], output)
mutated_mod['func_3938'] = func_3938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_3956 = relay.TupleGetItem(func_3183_call(), 1)
call_3957 = relay.TupleGetItem(func_3184_call(), 1)
output = relay.Tuple([call_3956,])
output2 = relay.Tuple([call_3957,])
func_3966 = relay.Function([], output)
mod['func_3966'] = func_3966
mod = relay.transform.InferType()(mod)
mutated_mod['func_3966'] = func_3966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3966_call = mutated_mod.get_global_var('func_3966')
call_3967 = func_3966_call()
output = call_3967
func_3968 = relay.Function([], output)
mutated_mod['func_3968'] = func_3968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3300_call = mod.get_global_var('func_3300')
func_3301_call = mutated_mod.get_global_var('func_3301')
call_3987 = relay.TupleGetItem(func_3300_call(), 0)
call_3988 = relay.TupleGetItem(func_3301_call(), 0)
output = relay.Tuple([call_3987,])
output2 = relay.Tuple([call_3988,])
func_3989 = relay.Function([], output)
mod['func_3989'] = func_3989
mod = relay.transform.InferType()(mod)
mutated_mod['func_3989'] = func_3989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3989_call = mutated_mod.get_global_var('func_3989')
call_3990 = func_3989_call()
output = call_3990
func_3991 = relay.Function([], output)
mutated_mod['func_3991'] = func_3991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4009 = relay.var("var_4009", dtype = "int8", shape = ())#candidate|4009|()|var|int8
var_4010 = relay.var("var_4010", dtype = "int8", shape = (8, 8, 16))#candidate|4010|(8, 8, 16)|var|int8
bop_4011 = relay.bitwise_or(var_4009.astype('int8'), var_4010.astype('int8')) # shape=(8, 8, 16)
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_4026 = func_1308_call()
call_4027 = func_1308_call()
func_1836_call = mod.get_global_var('func_1836')
func_1838_call = mutated_mod.get_global_var('func_1838')
const_4036 = relay.const([[-1.764602,-6.316784],[3.407048,-1.494661],[6.688822,-0.964885],[9.819934,-9.956094],[-7.499064,-5.735287],[-4.476671,-9.833815],[6.601093,5.107219],[-4.546314,-7.934303],[6.601245,8.876289],[4.667244,9.309281],[-5.928306,1.127561],[-7.031757,6.688896],[6.248620,4.766412],[-3.427786,-6.399779],[-7.649684,2.302401],[-3.870147,5.027278],[0.992838,7.528514],[-4.624845,8.262431],[-8.666197,-3.202766],[-6.914164,5.372686],[-0.002938,-5.494388],[8.355879,-5.541438],[-5.337529,-9.685773],[7.364515,9.729392],[-5.937889,6.634003],[1.224662,6.751847],[-8.405914,-8.952695],[-4.626696,-2.774608],[2.914772,0.642186],[4.992179,-3.841953],[5.823777,-8.733867],[-6.369863,5.248928],[-5.078025,2.685843],[-4.121105,5.333701],[-9.339712,4.372233],[-5.666965,6.853420],[-9.366534,-8.761610],[9.930420,-9.143990],[5.580593,3.863564],[-0.644820,-6.999744],[-6.786563,-8.010329],[-8.587125,3.882741],[-5.924524,9.458792],[-5.819847,-7.032776],[4.344619,-2.165545],[0.288350,-8.362708],[3.006770,-1.275244],[-9.671978,1.902748],[-2.171894,8.362053],[6.849353,6.824640],[-0.329347,-9.116541],[-0.437543,2.368360],[5.638475,-1.190251],[-2.456043,8.662480],[-2.200454,5.595950],[-8.228236,3.223302],[3.256360,-0.373577],[2.935421,-4.841299],[-6.234272,-0.817966],[4.280528,3.135336],[7.684196,8.362312],[-1.199547,-4.318444],[-5.796863,8.167604],[-8.440504,7.010051],[-5.410720,-4.193427],[2.279035,1.630813],[-2.984182,-6.337144],[4.917066,-0.591070],[8.986719,2.621206],[4.465663,7.873871],[7.565122,-6.343046],[6.846079,5.574788],[9.446353,-8.252734],[-2.445573,6.661668],[1.648789,-6.568755],[7.081758,-6.185966],[-4.572893,-4.215653],[7.023880,0.928332],[-9.443007,-3.320841],[3.838822,0.380674],[9.194141,-4.917716],[4.556152,-4.640938],[1.480043,-1.735684],[-5.138160,-0.460449],[-8.514007,-6.674332],[-3.587454,-9.065079],[7.392962,-5.210926],[8.717389,-4.129248],[9.688388,-8.188580],[-5.499544,-2.734984],[-0.634993,-7.646344],[7.503661,7.209877],[4.388327,2.480001],[-4.353378,-0.381158],[-4.966671,-6.510409],[4.215102,-0.054083],[6.733813,9.816985],[-8.723298,-0.086992],[-1.362247,9.832485],[2.984803,5.767339],[-1.158704,-1.534409],[9.957888,-8.389281],[1.499683,5.784692],[0.926207,-3.661775],[-1.661399,-8.241710],[4.568940,6.421249],[1.678524,6.584771],[-4.309669,8.628496],[0.936411,3.367778],[4.582134,-0.443305],[-8.825172,0.214881],[6.224758,5.593623],[8.056644,-4.422231],[-7.661220,9.268853],[-8.691508,-2.906967],[8.062126,4.805629],[7.268583,7.514217],[2.150130,6.603795],[7.353067,5.584001],[-5.161484,7.347392],[1.124680,-1.002373],[0.672644,1.521236],[-4.900054,-7.765993],[-9.172783,-6.440166],[-5.073956,-2.540899],[5.230744,-0.881401],[-2.513093,-4.473263],[-2.742443,-7.048226],[9.199201,1.039179],[-4.003921,7.719930],[-8.526491,9.473596],[8.935297,-1.669305],[9.761447,6.921442],[-3.685628,-8.117088],[-7.430785,-5.127872],[-5.745338,-4.639127],[8.692516,-9.325338],[-7.991804,8.913832],[-0.929246,9.316350],[-4.111663,6.601604],[-1.953366,0.685470],[-0.108797,5.213535],[-7.555950,1.529470],[5.125513,-3.263302],[2.769146,-7.213278],[-0.507924,-3.770321],[-3.015443,9.223061],[9.909959,8.812466],[4.145599,1.517107],[-7.357134,-7.415738],[-3.997191,4.401244],[1.680080,-0.452623],[-1.315428,1.570326],[-4.847021,2.725398],[2.864581,-1.651401],[-4.015365,7.564095],[-1.356419,0.448550],[1.028237,1.423946],[-8.810685,0.504957],[-6.211235,-1.885771],[5.357673,-2.344358],[-4.974447,-6.790846],[-3.788321,-3.609439],[-0.337181,-3.981371],[-7.835562,4.357456],[-6.243640,6.551094],[1.051319,-6.491022],[8.549648,6.688747],[-7.859624,-7.383817],[9.014591,5.072755],[6.151161,-2.273513],[7.684140,-7.729199],[3.047481,9.164829],[-3.201660,-0.461187],[-3.481040,-6.542396],[6.680002,-7.059635],[4.957023,-5.359135],[8.570220,-8.831750],[-5.700416,2.167251],[4.791166,7.209038],[4.277116,-4.045772],[-3.518633,-3.835071],[-6.536434,-3.872725],[-6.470766,6.246027],[8.448581,-9.311777],[4.171841,-1.718703],[-1.072501,9.450359],[3.166653,-1.864029],[-3.318160,0.611258],[1.139256,1.275687],[-5.483176,5.550592],[-0.858408,-8.789497],[1.400526,-2.235684],[6.922129,-8.626833],[-5.319316,4.088255],[-5.587728,1.337463],[8.956548,7.131318],[-9.413675,-9.977551],[-4.939080,8.830678],[-8.121564,6.363252],[-4.445394,9.907963],[-8.337499,3.772442],[8.787002,-4.936658],[-1.806270,-7.217995],[-4.110431,-2.996075],[-4.536595,5.450243],[3.361069,9.355819],[-5.895281,7.924492],[2.965877,-6.242879],[-4.068556,-8.275137],[1.430040,8.366310],[-3.286812,5.720225],[-6.939630,0.200958],[-0.929220,9.354255],[6.618957,1.905634],[6.607929,6.155448],[7.979574,-6.086994],[3.682152,-2.398029],[-4.778428,7.994194],[4.077076,3.271467],[-5.370341,1.441254],[-3.160307,-1.960225],[2.049676,6.042208],[-6.698129,5.008122],[0.892450,6.222748],[0.587810,2.368553],[-4.384818,-9.354008],[0.251467,1.139845],[9.943769,-0.402693],[7.001440,0.659530],[-5.617369,-6.453741],[2.287365,2.262126],[0.325120,-7.742991],[-8.795982,-2.153649],[-7.998834,-5.468952],[5.115680,7.421321],[-2.218311,-2.989202],[6.802287,2.292502],[-4.699163,-6.871574],[2.160591,-0.003345],[4.339111,6.620575],[-9.613124,-9.643833],[4.638154,-6.617204],[-7.694327,0.134578],[3.538666,-9.114441],[9.908748,3.583299],[5.650300,-4.580922],[2.440403,-6.598906],[0.677984,-3.409061],[9.639457,-5.845409],[3.483775,8.808319],[-7.814458,9.914766],[-9.297006,-6.633046],[1.998416,-5.925396],[-5.128275,6.320567],[2.407825,-1.852353],[-7.996804,2.003887],[4.975104,-0.668309],[-1.216252,-8.408432],[-1.131092,3.957137],[0.128828,-8.118107],[6.894265,-0.387394],[2.279134,3.162516],[9.029688,4.456495],[-5.773534,8.178152],[-1.700236,-6.342353],[-1.589850,-3.569960],[-2.861552,1.050047],[4.577129,-8.037246],[-4.030182,-2.436089],[8.930213,4.585677],[2.824369,-4.488387],[5.869412,5.512586],[9.055362,-6.936306],[-0.281028,-9.209491],[-3.255477,8.184962],[4.020526,-1.091316],[-9.622117,-1.942429],[-7.937211,-0.198724],[-5.833953,2.801106],[-7.764825,-2.569839],[8.588799,2.782802],[3.513736,-8.110417],[-2.393463,2.483243],[-9.170408,3.622038],[3.771262,-4.039095],[2.390331,5.949246],[6.497134,5.429328],[-0.767653,0.446053],[7.178786,3.041135],[-4.199037,-1.879130],[3.539967,-0.518168],[-7.045581,-3.845737],[7.366849,8.482036],[1.828753,4.869376],[-4.813440,6.561294],[-7.092716,-4.624660],[8.131525,-6.968438],[6.466536,-3.067385],[-8.212993,-6.180584],[1.843693,-1.878993],[6.131516,1.823073],[8.619216,0.929139],[-1.932986,-7.810149],[1.234134,-2.443160],[-3.950407,-0.043082],[6.239190,1.344856],[-4.564680,-2.459898],[-3.577793,-0.081360],[5.272958,1.939978],[-6.890362,-9.407657],[4.806277,1.479551],[2.030137,8.354484],[-3.881383,0.038974],[9.773953,-7.525711],[1.837054,6.543179],[6.496355,8.247535],[5.662136,5.980229],[-6.476565,-2.761409],[-9.017122,-2.491782],[8.145997,-3.393000],[-1.738641,-5.187538],[-3.616601,8.245512],[9.014236,5.268684],[-4.666563,0.961099],[2.567523,-3.550130],[-6.206690,2.660375],[-6.536026,-7.394674],[-7.699959,-0.686935],[7.242614,-0.442630],[0.371639,1.756301],[-6.483464,3.874133],[2.800414,-3.795671],[-0.549084,-7.497130],[-5.081675,1.039488],[-4.441501,-6.266034],[-8.512006,8.347859],[5.953043,8.374128],[5.854149,-0.760478],[-5.690333,-6.017673],[-4.144410,-9.599120],[0.800164,-0.997575],[8.874841,4.127327],[1.409849,-1.539524],[-4.812149,1.853255],[2.017381,-3.419642],[6.637805,-4.616239],[-9.537401,-9.010523],[5.923301,6.242968],[0.702647,-6.063008],[-8.649362,-0.601288],[-7.562459,1.846145],[-7.062091,-4.601521],[-6.414775,-4.432978],[6.958862,9.990718],[-8.666565,2.021402],[-5.457021,-8.771572],[-0.757110,-5.481762],[-5.856750,-6.809739],[5.446467,8.516576],[8.153694,8.247257],[-3.508966,9.864169],[-5.873065,-2.411411],[-6.582209,5.973995],[-5.375872,2.596058],[-5.475978,6.182687],[-9.171077,6.138405],[-0.506369,-3.712684],[4.002929,9.707435],[2.093348,4.516230],[5.712942,-2.256323],[3.187554,-7.906774],[-0.671420,-5.837512],[-9.669872,9.089830],[-2.057186,-0.639380],[-9.817922,-1.170541],[8.999955,9.201721],[-2.113650,-1.409174],[-4.178234,-9.374762],[-9.251986,-7.388130],[-4.482430,-4.535184],[-4.018980,7.623330],[-8.278303,5.617248],[-2.571082,-2.167230],[4.086031,8.156881],[8.004866,6.701380],[-6.816364,5.139854],[8.335056,2.403712],[7.367991,-4.275934],[-3.904831,-2.593601],[7.121846,1.366519],[6.576833,1.778870],[7.653891,-9.420532],[3.911173,4.699975],[9.726461,-1.274092],[-1.086098,-1.137677],[4.434479,3.902678],[8.303884,5.456677],[-1.273928,-7.743046],[-8.158195,-7.358248],[-8.069627,-9.506109],[9.726648,-7.484746],[3.482022,7.000984],[-0.642233,2.869429],[-6.336365,6.844032],[-7.014543,-3.270473],[3.551902,-3.465660],[3.216712,-8.385912],[1.763366,2.651000],[-3.011235,-5.127062],[-5.259307,5.164477],[1.244643,9.246004],[9.336910,3.604516],[3.314800,-4.295202],[2.226485,-7.347086],[-6.216088,-0.242127],[-6.255551,-8.326768],[6.329911,-9.587718],[-2.571134,4.861887],[-4.402650,9.058031],[2.882536,6.230340],[-7.813809,-2.972686],[-9.286031,-0.075747],[8.415342,-1.003871],[-6.804724,-7.234799],[4.427908,-1.550448],[-7.391910,-4.248742],[-0.024484,-5.129241],[-9.379709,-3.288776],[-2.955831,-5.249440],[0.402611,0.161323],[-3.248189,-1.973087],[-4.284263,-6.341069],[5.282489,2.974793],[-0.767581,-0.522215],[6.148522,3.609733],[-7.147714,-5.214997],[-1.081110,7.434795],[-6.231828,-5.864639],[0.550577,0.717132],[1.101158,1.072811],[-1.992914,-1.936739],[-2.313920,7.368114],[1.076025,-2.245969],[-9.638687,-8.086342],[4.346880,7.244843],[-3.977291,-9.084658],[-3.966469,5.278260],[-5.386975,5.694213],[0.136594,7.655536],[-3.772788,1.376090],[1.116076,-8.285572],[2.169277,-7.234450],[-1.723544,-3.690844],[5.495720,-3.814213],[-6.680975,6.051399],[4.264074,-3.785158],[-1.529876,-3.316172],[-0.571375,2.206203],[1.432989,-6.292231],[-9.807502,-0.657036],[-6.813390,-9.908219],[5.344232,2.002837],[-9.817300,-5.741072],[1.457735,0.499848],[1.840368,3.771300],[2.675985,2.528256],[-3.888011,5.839935],[1.388555,1.856048],[-7.486427,4.653539],[7.787246,-5.532217],[-4.576865,7.266783],[4.733451,1.424972],[-8.997488,-3.765680],[7.018131,4.376143],[5.500447,6.570871],[-4.718680,-2.172208],[-5.628605,-5.902213],[0.566921,5.650040],[-4.735929,7.349152],[0.548477,-3.472649],[0.803540,-1.964960],[-6.260723,-9.492404],[-8.881389,-2.779596],[9.878632,-2.163494],[6.147260,4.838196],[5.891428,-3.247021],[8.598375,8.471495],[-6.261932,-4.727898],[-6.307242,3.878809],[-6.044222,2.294729],[2.951770,0.287654],[-7.789452,-9.865939],[8.540439,-1.632575],[-6.241603,-4.985436],[9.414088,1.716714],[6.740333,3.305467],[-3.592730,-2.760825],[7.101648,3.668663],[-1.905388,0.402076],[-2.655935,-9.959806],[9.209318,-8.533770],[7.826380,3.067705],[-2.156464,-7.366352]], dtype = "float64")#candidate|4036|(504, 2)|const|float64
call_4035 = relay.TupleGetItem(func_1836_call(relay.reshape(const_4036.astype('float64'), [9, 14, 8])), 0)
call_4037 = relay.TupleGetItem(func_1838_call(relay.reshape(const_4036.astype('float64'), [9, 14, 8])), 0)
func_2338_call = mod.get_global_var('func_2338')
func_2341_call = mutated_mod.get_global_var('func_2341')
var_4040 = relay.var("var_4040", dtype = "uint16", shape = (1430,))#candidate|4040|(1430,)|var|uint16
const_4041 = relay.const([1,1,2,-5,10,8,1,3,-3,-7,-6,7,7,10,-7,9,-2,10,-10,8,3,3,10,-2,-4,5,5,10,9,-3,-2,4,3,-9,-9,4,-5,-7,-4,1,9,8,9,6,-7,-6,-3,2,-4,-10,9,6,2,10,-4,6,8,-9,-1,7,-6,-4,3,7,-6,-2,-5,-9,-4,5,-4,3,-4,-9,9,-10,8,6,-1,-9,-1,1,9,-5,3,-3,10,8,-10,6,4,-6,1,4,-6,8,-1,-5,3,5,7,-4,6,10,1,-7,5,9,-7,7,-5,-1,6,-9,4,-6,4,10,3,7,-8,-1,10,-9,5,10,-1,-8,-5,-7,-3,-9,-4,-8,-9,-9,1,-9,1,10,4,-8,9,3,5,2,-4,6,4,-2,-8,1,2,2,8,9,-2,-8,-3,6,10,7,-2,9,-6,8,-4,5,9,-9,-1,-10,7,7,-8,9,2,-9,6,2,-10,8,-1,8,-10,8,9,-6,7,-6,6,-2,-1,5,-10,-1,-9,-2,2,10,-9,5,8,4,-5,-2,-8,-1,5,8,3,4,8,2,-6,-4,-1,-4,-10,-6,-1,-8,-3,9,5,3,-7,-9,5,-5,-2,-7,-7,3,1,2,2,-2,9,4,9,9,6,-10,-1,-1,1,-7,-1,6,4,6,8,-10,1,10,-3,5,8,10,10,4,1,10,4,4,5,-3,-9,-9,-8,10,7,1,-3,-7,-4,4,10,5,-1,-3,8,9,-10,-8,7,-10,-5,4,-5,9,-9,3,7,5,-9,-4,4,-4,2,-3,-2,-7,-7,3,9,-1,6,-2,-4,-3,-7,1,10,6,-9,-3,3,8,-9,3,-4,8,8,7,7,8,6,-5,-7,8,-3,7,-9,7,-5,-7,5,-2,-5,7,-6,-8,-4,-1,-6,-9,10,-5,10,-8,-2,-7,-10,2,-6,7,-5,6,-8,2,-4,4,-6,4,1,-4,-6,-4,8,2,-4,-5,6,10,-6,9,-5,5,-2,-9,10,-9,-4,1,-6,5,-3,-3,-4,2,-7,-4,-4,6,-8,10,-10,-4,-10,6,7,-10,-4,9,5,-9,-2,5,-2,3,-7,7,10,10,6,7,-9,-6,-7,-2,6,-7,4,6,4,-5,-10,8,6,9,-6,-7,-3,-2,8,5,7,2,-5,-7,-8,9,7,-10,-7,-4,7,-10,4,3,7,-6,1,6,-8,6,-7,4,2,8,-4,4,6,4,-7,-2,8,-7,-7,6,7,-1,-6,-2,-10,-10,5,-6,8,-10,8,7,1,-4,8,4,-9,-2,10,3,-4,-6,7,-9,3,-9,-3,-8,2,-7,-1,8,5,-7,5,7,-5,8,5,6,-9,1,-1,8,-1,6,5,-2,-7,7,10,-1,9,6,9,3,7,9,3,3,-2,5,-4,-10,-7,3,5,2,-5,7,10,-9,-6,-5,6,4,-7,-9,-8,-2,-8,-4,-2,6,-7,-1,-4,4,-9,-10,4,-6,5,-2,4,9,2,4,4,-9,-2,-7,-3,6,-9,8,2,-6,9,1,-3,-5,8,9,7,2,-10,-6,10,-4,10,-4,-10,-1,-8,2,5,-8,-7,4,7,-3,-4,8,1,-5,-8,3,-7,6,-7,1,-8,-6,6,-8,5,-9,-10,-5,3,-4,-6,8,1,3,4,9,-2,6,-4,-2,8,2,-10,-1,-4,3,-1,-7,5,-10,3,1,-6,-5,3,-1,-1,-9,9,-4,-6,-7,8,-7,4,-3,9,-2,3,5,-7,7,1,-8,7,-5,9,-9,-6,9,6,-6,-8,-9,-6,-6,-3,2,10,-6,2,-1,-5,-7,7,-2,-7,-9,7,-5,2,-9,-6,-1,-10,5,-10,2,-7,8,-4,8,-1,8,4,-2,-7,-3,9,-1,-3,-1,-5,10,-4,7,-1,9,3,-9,-1,5,-3,2,4,-10,-4,-2,6,2,-2,-7,-5,6,-6,-6,7,6,10,1,5,-3,-6,7,-4,-3,-7,1,9,-9,2,3,-7,-1,-10,2,-6,4,7,6,-10,10,-9,1,-8,-4,-6,-2,-7,1,-5,-3,-6,-5,-8,-6,7,-8,-9,-6,-9,-9,-7,-9,4,-4,-1,-4,-5,1,7,4,5,2,-2,1,7,8,1,-2,9,7,-4,8,9,5,-9,10,2,10,-8,-7,10,-1,-5,9,-9,-4,7,-4,-3,10,9,-8,4,7,10,9,1,3,4,-2,8,8,9,-10,3,8,4,5,5,-9,7,-5,9,6,9,8,5,-1,-8,-1,-2,2,-7,3,-8,7,10,6,9,3,-2,-3,7,-5,6,-7,-5,4,6,3,10,3,-1,7,3,-6,-1,3,-5,-2,-6,-9,9,-2,3,-1,5,-10,3,6,1,10,-5,9,-5,10,1,-2,-7,5,4,-2,2,-5,3,-10,5,6,6,9,8,1,-3,10,-1,-9,-5,-4,-2,3,-2,10,4,9,-1,9,2,-9,-5,2,-5,1,-1,-6,-5,8,1,-9,4,-3,8,2,-4,-2,9,-6,-6,-4,-3,-10,9,-8,-8,5,4,-6,-2,2,-1,-6,10,-5,-1,1,-9,-4,9,-1,8,-10,4,5,-6,1,-3,8,-8,-8,-1,-3,-2,-1,9,-9,-7,-9,4,-4,-3,6,1,9,-6,-8,-8,9,10,-10,-3,-5,-7,-1,10,-1,-2,9,10,3,-5,-5,4,2,6,-2,-10,-9,-1,5,-6,6,-3,1,3,1,7,-10,10,6,3,-4,4,7,4,7,-10,7,-8,-9,4,-8,6,3,-9,1,-4,-2,-8,4,-2,-1,-5,-6,-9,-3,-6,4,-10,-7,6,8,3,-10,10,-5,6,5,-8,-6,7,-8,4,-5,8,1,2,-4,1,7,6,6,-2,7,3,5,-5,-2,-4,1,-1,-4,6,-7,9,-10,8,1,6,-9,1,6,-8,5,7,4,2,10,-5,5,-1,-3,9,-10,-9,-4,3,-8,-10,3,-1,-7,4,-9,2,-2,-8,-1,-8,4,10,-10,7,3,3,7,2,6,-1,4,-8,-6,3,5,-10,9,-6,4,8,-3,5,4,-5,-3,5,10,4,-10,-3,6,-4,5,7,3,7,8,-9,-9,-3,1,-8,3,-4,6,-10,3,1,-3,-7,6,4,4,-6,-10,-5,-9,9,-2,-5,-4,-5,8,-7,6,9,6,6,9,-4,3,7,2,-3,2,-5,2,5,5,1,4,3,-3,1,-3,10,-4,-7,6,-1,8,5,7,10,-2,3,-2,7,5,9,4,-3,6,-7,10,1,7,9,-7,-5,-1,8,-5,1,4,-10,-7,1,3,-6,-7,2,-4,-5,10,-2,8,-6,-5,-5,-5,9,7,7,-7,6,9,-7,9,-6,4,1,9,7,4,-5,6,-3,4,-5,-1,7,9,7,-8,10,-2,-5,8,-7,1,-3,5,-2,-6,-2,-7,8,-2,7,-7,-3,-8,2,-10,10,10,-10,9,-6,8,3,8,5,-8,2,-9,-6,5,3,-6,1,-6,3,-5,-4,10,10,9,-7,-8,-2,-6,-4,-8,-8,-9,2,-10,-5,-7,-7,4,-2,5,-10,10,1,-4,-9,-1,-9,-6,8,-6,-10,-3,10,6,-2,3,3,-8,1,9,-4,-7,-3,-4,10,5,2,8,-5,6,-5,-9,-6,3,9,-7,4,-6,8,7,9,-7,10,-7,-10,-10,3,3,8,-9,10,2,2,1,9,8,-10,10,-10,2,-9,-5,6,4,-4,5,-8,7,6,-10,6,2,2,-5,-9,2,-1,-2,3,-3,8,-10,-4,4,5,-2,1,8,-7,4,9,-4,3,7,2,2,7,-6,-10,-10,4,9,-7,-7,-7,-10,8,-7,2,6,8,-5,3,8,2,10,2,-3,6,5,2,-10,-1,-1,4,10,5,-7,-9,-2,2,8,3,5,1,5,-7,-4,-3,-3,2,9,1,8,10,10,5,-10,-1,-10,-6,8,9,2,-8,-10,-10,-10,6,10,9,2,10,-2,6,5,-6,-3,-6,-10,-2,7,-1,3,-4,-5,-5,-6,-6,7,-10,-2,-9,5,2,2,-8,-7,5,-6,5,1,-8,-6,-5,4,7,-6,-5,-2,8,2,-2,-7,-1,7,4,-5,-4,7,-3,-9,-9,5,-5,10,10,1,10,-8,-1,-6,-2,9,1,-7,9,3,10,1,-6,3,4,7,-2,-5,-9,-1,-4,-6,8,-9,1,4,-1,-1,9,-2,-5,-9,3,3,-6,10,-5,-5,4,-2,6,-8,-3,6,2,7,7,6,9,-10,4,-3,10,3,-1,-1,-1,6,10,7,1,9,9,8,5,-3,1,7,3,7,5,3,-9,-1,10,-10,2,-9,-7,1,6,-10,-9,8,10,-7,3,2,-8,10,-1,-9,4,-5,6,2,9,8,-2,1,-4,-7,-8,-9,-2,-4,-3,-5,4,5,-8,-3,10,5], dtype = "int16")#candidate|4041|(1680,)|const|int16
call_4039 = relay.TupleGetItem(func_2338_call(relay.reshape(var_4040.astype('uint16'), [10, 13, 11]), relay.reshape(const_4041.astype('int16'), [1680,]), ), 0)
call_4042 = relay.TupleGetItem(func_2341_call(relay.reshape(var_4040.astype('uint16'), [10, 13, 11]), relay.reshape(const_4041.astype('int16'), [1680,]), ), 0)
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_4044 = relay.TupleGetItem(func_3542_call(), 0)
call_4045 = relay.TupleGetItem(func_3544_call(), 0)
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_4058 = func_1308_call()
call_4059 = func_1308_call()
output = relay.Tuple([bop_4011,call_4026,call_4035,const_4036,call_4039,var_4040,const_4041,call_4044,call_4058,])
output2 = relay.Tuple([bop_4011,call_4027,call_4037,const_4036,call_4042,var_4040,const_4041,call_4045,call_4059,])
func_4092 = relay.Function([var_4009,var_4010,var_4040,], output)
mod['func_4092'] = func_4092
mod = relay.transform.InferType()(mod)
var_4093 = relay.var("var_4093", dtype = "int8", shape = ())#candidate|4093|()|var|int8
var_4094 = relay.var("var_4094", dtype = "int8", shape = (8, 8, 16))#candidate|4094|(8, 8, 16)|var|int8
var_4095 = relay.var("var_4095", dtype = "uint16", shape = (1430,))#candidate|4095|(1430,)|var|uint16
output = func_4092(var_4093,var_4094,var_4095,)
func_4096 = relay.Function([var_4093,var_4094,var_4095,], output)
mutated_mod['func_4096'] = func_4096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_4098 = func_2499_call()
call_4099 = func_2499_call()
const_4128 = relay.const([[[9.220199,5.386334,-4.399577,-5.200968,-0.697448,9.733402,3.357550,4.934501],[0.839567,-1.321348,9.504972,-3.020503,9.107047,-2.852284,-2.206628,0.858028],[-2.357361,8.460810,6.535378,5.127789,1.486746,9.062640,0.097760,-8.525431],[-4.441795,3.197788,-8.599922,-4.650664,8.709855,9.124447,3.399444,5.907798],[8.752587,-4.917265,2.186314,1.380853,5.049065,8.843611,1.986454,3.486219],[-1.246816,6.799420,8.721017,-7.591218,-7.155483,-0.813315,0.680920,4.923836],[-8.121576,2.224388,4.936485,-9.568576,7.127960,8.225546,-7.881434,-1.885626],[6.039667,9.395872,-8.089324,2.239886,8.064384,-1.601169,-8.260334,-6.813373],[1.608076,-1.510461,-9.023704,4.689641,-4.371470,-4.575880,-6.873618,6.938748]],[[-7.855986,-4.625241,-7.625294,6.139833,1.920537,-1.733386,7.965273,-9.300241],[-1.370648,9.362521,0.554447,-6.369987,0.371669,-2.630810,-0.982546,8.345351],[1.478059,9.795697,-5.184650,4.607047,-5.760934,0.744267,-7.225933,-8.262867],[-1.861172,0.165468,9.843290,5.144655,-5.472214,-4.807046,3.211970,3.040851],[1.167058,-8.659957,4.789587,1.501048,-9.221023,0.233277,-2.289193,3.421799],[5.038847,-1.547224,6.673979,1.690208,-9.876185,-2.095604,-6.122824,-2.843427],[-1.677008,7.784749,-3.437559,6.694601,5.009965,-3.744774,-0.217321,-6.943568],[-8.868807,-8.420999,-7.863437,-1.830599,9.920029,-8.134146,-7.172570,2.799592],[1.030269,2.937095,5.246846,-8.447715,6.543924,-5.113315,6.973930,-9.447783]],[[-6.781086,9.962137,-7.025628,0.623688,-8.107823,8.424036,-9.204564,3.437562],[5.351819,1.841282,1.114888,4.979681,-5.062146,-2.732768,-1.346053,-1.792296],[-0.880953,9.400275,6.033590,-1.499652,-1.109617,-9.583295,4.588315,6.314949],[-0.260269,0.641798,-7.270843,8.667575,5.834836,-2.807112,-2.996337,-2.098357],[-3.070658,6.588908,-5.860144,4.936640,-1.468366,0.897092,5.439604,-5.066385],[1.365507,2.052734,7.452739,2.065819,0.487517,-6.814093,-1.451638,-7.587165],[6.870690,-8.053352,3.160739,-2.823020,7.629167,4.881987,-2.016022,5.127377],[-6.610360,-7.980278,1.719709,-8.419723,3.289630,-6.472387,1.408661,4.263804],[-5.922591,-6.280535,5.172682,7.429970,-6.583323,-2.744189,2.398540,-4.436234]],[[-2.257890,6.698902,-9.730946,-7.817293,-0.974743,0.342730,9.948008,-1.685961],[-4.890386,-8.140746,-9.173035,7.997013,-7.138155,3.703946,1.004955,3.184720],[-6.278169,0.146954,-4.386677,1.211458,-8.378810,-9.100642,7.007825,8.938920],[5.586753,7.754611,-6.460026,-7.485412,-7.991624,-8.320288,-2.350176,-1.180632],[-8.190902,4.227413,9.007545,8.499930,-4.418688,-8.862177,1.277937,7.890935],[0.465904,-3.725386,1.175787,-8.627742,-3.011030,8.982622,2.269575,-7.270781],[9.001769,-2.290197,-1.364384,-1.021188,-9.374164,-0.494935,9.072929,-7.894363],[-8.331611,-4.206609,-7.171586,-3.198397,4.401872,3.691842,7.643890,-7.907826],[7.292689,3.171000,-1.027489,-4.273277,-7.482438,-3.136761,0.122594,-0.291337]],[[6.099187,4.013004,-1.907187,9.544603,-4.293710,-5.862162,-6.609835,-0.691127],[7.031310,4.758326,-9.536774,-6.849204,-5.372639,-7.147724,-4.506843,4.404405],[4.180130,2.542978,-8.308289,3.008276,0.659908,-5.635266,-9.179100,7.539830],[3.556045,3.007766,3.197312,-4.990588,5.148074,7.312211,-3.941777,2.238994],[0.997768,3.785902,9.405198,-9.375174,-3.627199,-9.987211,-3.494267,-9.208976],[-0.512155,8.731160,-7.394656,3.910796,-0.730042,7.085544,-0.482428,-0.559637],[6.607655,6.281644,-5.914874,7.312991,5.063646,1.943319,7.420198,0.711026],[5.216815,2.616924,-0.618452,3.964494,9.983422,2.042639,-6.217745,-7.435861],[8.898912,-6.762512,4.586253,-2.056883,-7.990931,-7.977866,-1.281335,8.118318]],[[-8.184464,6.320685,-1.087181,7.709391,6.361459,7.596685,-9.281013,5.840912],[7.248225,1.031714,4.866873,0.944059,9.025138,2.245641,2.431456,-5.038620],[-5.321906,4.778303,-5.190125,-2.917530,0.866254,3.703937,0.315668,-7.412031],[9.616285,-6.908054,0.441298,-6.802508,5.182572,-1.198140,-2.500673,3.770171],[-5.502534,4.810270,6.960173,-3.963736,7.957835,5.777137,-1.196969,-8.970780],[6.962543,-9.449333,-5.016580,-7.100424,8.201622,7.031988,1.210853,-6.597133],[5.490751,-2.550111,5.290848,0.527037,7.141826,-9.460740,-9.501713,4.016691],[4.971432,9.742113,-3.116675,3.783193,-2.062034,6.613962,6.333837,-1.133246],[-9.089031,-4.452703,6.191312,-8.411877,-4.034192,7.599046,5.139138,-6.791358]],[[-8.391632,3.956030,3.024289,-5.913806,0.223925,4.401602,4.914651,4.433958],[5.041760,-1.669609,6.705388,4.003313,3.443003,0.139271,5.693965,7.339148],[0.784337,-9.270267,7.098697,-4.039583,-5.151852,-3.247984,1.532211,5.169340],[3.325267,-8.472920,3.639599,-5.632601,-0.511796,8.486276,4.938229,6.347774],[5.275341,-6.411214,9.846772,8.206618,-4.519099,1.815563,9.910959,-7.781560],[-0.054753,-9.259010,-9.384841,-0.203547,-3.190585,-2.277459,-1.342468,-5.870223],[5.294472,0.843554,3.850436,9.468805,-2.100895,-6.102036,7.591221,-1.619140],[6.555137,6.696416,9.222887,-6.699100,-3.211070,9.208111,-7.583923,-5.181630],[-2.346477,-2.009505,8.508712,-4.603825,6.660146,1.706785,5.950371,-0.196655]],[[-5.252144,2.078113,-9.139091,7.126533,-5.539945,2.694812,-5.585715,5.131017],[1.668016,0.867726,9.938973,-3.900947,-7.539889,1.454157,4.468495,-6.562734],[-3.867977,2.268980,2.661447,9.313344,-7.339474,-9.178165,-6.725980,6.197158],[-6.344101,-9.978249,-2.303638,-0.175004,5.883784,2.492155,0.955096,-4.500517],[5.070384,-2.519182,5.236924,-3.269290,6.227019,-3.476348,-1.136872,9.144180],[-3.991758,-5.780873,4.935512,1.803098,6.947686,4.338385,-7.866710,-5.388441],[-2.973988,-1.348239,-5.984722,8.027106,-2.977127,8.467124,9.044105,5.747058],[9.141708,5.538016,-5.890560,6.188416,7.947853,-1.819298,-3.336912,8.117690],[-6.520514,-1.240897,-9.518567,-2.198393,-1.519281,-0.292426,-7.354783,8.155577]],[[8.823033,-5.174699,-2.579949,5.690787,5.440601,0.113226,-1.891182,-4.880691],[9.733427,8.258971,-1.915019,-0.615000,-5.595923,-0.414895,-0.719907,-6.146619],[-3.338295,9.285531,-5.173490,-3.458590,-0.323832,0.335494,-7.323188,7.932133],[4.011300,-5.626567,-3.850737,-0.799965,6.879383,-9.211249,-5.307571,8.218300],[2.692222,4.618410,-1.526055,0.897131,-9.106815,1.483102,-2.217102,-6.897835],[-5.427489,3.815777,5.925636,0.321182,4.205914,-9.095746,-9.762565,-3.622096],[-4.738488,6.698655,-7.016516,1.915882,5.613678,0.945680,-5.910284,0.694437],[-8.953604,9.584923,-6.729624,-6.347834,-8.551849,-4.031102,6.703186,3.090299],[-4.478163,-5.366013,5.975933,1.076384,-2.811997,5.828604,-7.970796,5.249625]]], dtype = "float64")#candidate|4128|(9, 9, 8)|const|float64
bop_4129 = relay.less_equal(call_4098.astype('bool'), const_4128.astype('bool')) # shape=(9, 9, 8)
bop_4132 = relay.less_equal(call_4099.astype('bool'), const_4128.astype('bool')) # shape=(9, 9, 8)
bop_4140 = relay.less(const_4128.astype('bool'), call_4098.astype('bool')) # shape=(9, 9, 8)
bop_4143 = relay.less(const_4128.astype('bool'), call_4099.astype('bool')) # shape=(9, 9, 8)
func_3753_call = mod.get_global_var('func_3753')
func_3754_call = mutated_mod.get_global_var('func_3754')
call_4144 = relay.TupleGetItem(func_3753_call(), 1)
call_4145 = relay.TupleGetItem(func_3754_call(), 1)
output = relay.Tuple([bop_4129,bop_4140,call_4144,])
output2 = relay.Tuple([bop_4132,bop_4143,call_4145,])
func_4147 = relay.Function([], output)
mod['func_4147'] = func_4147
mod = relay.transform.InferType()(mod)
output = func_4147()
func_4148 = relay.Function([], output)
mutated_mod['func_4148'] = func_4148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_4165 = func_1671_call()
call_4166 = func_1671_call()
var_4199 = relay.var("var_4199", dtype = "float64", shape = (9, 14, 8))#candidate|4199|(9, 14, 8)|var|float64
bop_4200 = relay.bitwise_or(call_4165.astype('int8'), var_4199.astype('int8')) # shape=(9, 14, 8)
bop_4203 = relay.bitwise_or(call_4166.astype('int8'), var_4199.astype('int8')) # shape=(9, 14, 8)
func_3376_call = mod.get_global_var('func_3376')
func_3381_call = mutated_mod.get_global_var('func_3381')
const_4213 = relay.const([[4.153761,5.249621,-1.761963,-3.824190,5.591554,2.986117,3.258869,3.102239,-1.321143],[5.038395,-6.568424,-8.789619,-5.704085,1.581247,-2.411673,-7.087924,4.627758,5.929896],[3.897356,9.997549,4.241382,7.157830,-5.642363,-3.980093,-0.456465,-1.670705,4.403795],[5.139027,-5.177229,-0.152347,-2.116020,-6.330610,-4.592982,4.002500,5.632713,-8.660956],[-7.156542,-9.828919,-3.232180,4.380169,-9.942521,3.395056,-4.080424,2.527732,-3.812321],[6.535027,-4.653311,-2.671731,-6.847275,-5.517120,-6.699710,-2.987213,-5.152469,3.233679],[8.521278,0.360805,3.578806,-2.420440,4.403047,-5.782233,9.142445,-8.238831,-5.544235],[7.605122,8.988681,-4.798074,-6.508243,-2.825059,0.372409,-3.116923,-2.873604,-2.034607],[-7.649865,3.237907,-6.999904,3.517903,-3.967781,8.651866,-8.319782,7.713019,8.827726],[-0.637876,-8.530224,-6.668750,-6.532872,3.802282,5.759140,-0.810550,-0.169399,6.121306],[-3.573903,-0.751045,1.019359,6.487495,-7.868325,5.129547,-4.732691,-9.282917,-7.994635],[8.695273,7.762462,6.123367,-8.311218,-3.533633,1.438350,-9.474892,3.188517,-7.666987],[-1.297044,-8.682707,-7.071274,-5.333344,4.985541,-6.403566,-8.672778,0.134624,-3.018321],[-3.622082,-4.180652,0.483062,-9.807514,6.968060,-5.455867,-9.433662,2.304482,-6.968834],[-0.605620,9.852656,1.374645,3.592838,2.668133,9.641470,0.823373,-5.207236,-5.804184],[-2.727153,0.413093,-3.449172,7.191858,2.175389,-1.043064,6.073943,-3.229821,-6.287498],[-9.356343,1.464842,-8.472297,3.816674,-7.417592,-4.709625,5.175347,-9.257111,-8.667692],[-3.563199,8.640834,5.425904,4.115764,6.013576,9.507136,7.422801,8.761209,1.466084],[1.633288,-2.845513,-4.712118,8.344184,6.205411,6.112617,-7.832779,2.013996,4.119846],[6.543545,3.638651,-1.047805,5.284246,-7.114996,5.495969,-4.293655,-8.418565,-5.336869],[0.670127,-8.187749,6.189417,5.560861,-5.014171,-2.047526,5.958301,-8.333321,-6.615258],[3.588905,4.974023,-1.422093,8.977663,3.657913,7.296823,-4.209601,3.458435,7.827988],[-1.818970,2.502452,-3.338839,-4.162524,2.655758,-4.496511,-9.653722,5.284169,-1.271980],[-1.687747,7.782484,7.808762,9.490247,6.441111,7.157305,-5.483509,4.397545,-3.353407],[8.883961,5.388691,9.774815,-5.087002,2.782685,3.968411,8.222128,3.846713,-6.923075],[-5.012908,3.326054,-2.513342,-6.649031,-7.687373,-2.249936,0.322582,-2.938899,9.824909],[5.900620,7.687575,4.957304,-7.618689,-9.049980,4.334382,-4.877497,-3.538057,-2.900048],[-2.270505,3.863801,-0.119610,8.575187,7.816338,3.070525,-4.738957,-0.267454,4.616068],[-8.447728,9.178474,-2.781190,1.163499,-5.469392,-9.272756,7.289314,1.513025,2.094762],[-7.815720,-5.204570,-6.931123,-0.178144,-7.117603,-9.846575,2.123914,1.235651,0.382181]], dtype = "float32")#candidate|4213|(30, 9)|const|float32
const_4214 = relay.const([[-8,-9,-8,6,-1,3,1,-4,9,5,-2,8,-2,-5,-1,-2,7,5,-8,-9,6,-3,-2,-6,-6,8,-3,-9,3,10,7,5,5,-1,-3,-4,-4,7,-3,9,-3,-7,-3,-3,-4,-10,-7,5,5,7,-8,-6,-7,10,-6,-1,-6,-7,-9,-5,3,2,-10,-2,-4,-2,9,7,-3,-7,-8,9,-9,2,7,8,3,-10,8,-10,10,-7,2,-4,-2,3,9,3,8,-5,5,7,-5,2,10,6,-6,10,8,2,-4,2,-8,-3,-2,-3,2,-6,-8,10,2,9,-10,7,-2,-2,5,2,-10,-8,-3,-1,1,-2,10,7,10,2,-7,-10,8,-7,-5,-4,2,-7,-5,10,8,4,-5,-1,-1,5,-2,6,4,-4,-2,3,-4,-9,-1,-4,-2,-8,-1,10,-4,9,9,-7,-9,-1,9,7,6,-2,-6,9,-7,4,8,2,-8,-9,8,-9,6,8,-8,1,-10,5,9,3,-3,-6,3,-2,-8,-8,-6,3,-1,-7,7,-4,-1,4,-1,6,6,-4,9,-9,-8,5,-6,-5,-1,-5,-2,-5,8,-3,-8,4,2,-10,5,-1,-6,8,-3,8,-7,2,4,2,-1,-2,5,-3,-3,9,-2,-2,5,2,-2,3,7,-9,-7,4,6,-4,-1,8,-10,3,-5,4,-2,-9,-9,6,-10,-7,-5,-4,7,2,7,-2,-6,2,-10,3,-3,8,7,-5,8,3,-3,4,6,-9,-7,1,6,7,8,-9,4,-2,-9,5,1,1,-8,-7,3,7,-7,-5,10,8,-2,10,4,5,10,-1,2,8,-6,-4,9,1,10,8,8,9,-4,-5,2,4,-2,5,-6,5,6,-3,1,-2,9,-2,-9,-6,1,-3,-1,-6,-9,-8,2,1,3,6,9,4,7,5,-8,-8,4,3,-8,10,-10,4,-4,-3,-8,-2,6,-7,3,-8,4,-1,9,6,4,5,-6,7,6,8,8,1,5,6,1,-10,-2,-5,-6,-10,-5,-6,6,3,-3,3,9,5,5,6,7,-1,9,-2,7,7,7,-4,-9,2,-6,-3,-3,2,2,-2,-4,-8,10,-9,-1,10,-2,-8,9,-2,7,1],[6,5,-9,-6,1,7,-3,-10,-3,-10,-3,5,-8,-9,2,4,3,-5,8,7,-3,-3,-9,1,-1,8,-9,8,-9,4,-6,9,-8,2,-4,-5,3,5,9,5,-7,6,5,-5,10,4,-8,7,-7,-9,-10,-10,-2,-5,3,3,-3,9,-4,2,4,1,-1,7,9,-1,-2,-2,-7,5,10,-1,-8,1,-5,-7,-1,2,-9,9,8,-9,-10,5,9,-9,-10,2,-3,10,-7,8,7,9,-2,4,-10,-10,-3,10,-5,-2,1,2,10,3,-1,7,-2,6,7,-4,4,-7,-9,2,8,-8,2,5,6,-1,-9,-6,7,5,-3,-10,2,-5,-6,4,1,-5,4,4,7,6,6,-7,4,-6,10,6,-5,5,-6,-9,1,-1,-3,-2,2,8,-9,-2,8,2,6,-2,-8,4,5,2,-7,-8,2,5,-9,-4,8,3,-2,6,4,-10,-4,-6,-10,-5,-3,-1,5,9,-9,-4,6,4,4,-7,7,-9,-4,10,-5,-2,7,5,7,6,8,-4,-7,4,6,8,-3,-4,3,-2,8,9,7,-7,-8,10,-5,2,-3,-5,-10,-2,-1,-9,-10,-3,4,4,-5,-6,6,-1,-10,-4,9,-2,4,1,10,-10,-10,-1,-6,-6,7,-6,-7,7,9,-2,3,-9,-10,2,2,-2,-6,9,-7,-5,-6,-1,-7,10,-10,-6,8,9,6,8,5,2,-3,3,5,-6,8,-2,6,1,-8,-8,-2,4,8,8,2,-5,9,6,-8,3,-10,1,10,-1,-10,-5,-7,2,1,-9,8,-7,-3,-2,-5,-7,1,2,-1,-10,-3,-5,1,6,-9,-4,-10,-5,6,-6,-2,8,2,-5,-5,5,-9,8,10,-4,10,6,-1,-3,-6,-9,-3,-4,-9,7,3,3,4,3,-9,3,-5,9,9,2,-2,-6,8,-9,8,-4,-10,4,-10,8,-4,-9,9,2,2,5,-4,9,10,2,4,10,3,-7,-3,-4,-5,3,-3,-2,-10,8,-8,10,5,-8,10,-4,-4,-7,8,-3,6,-7,-4,1,5,-1,-6,-1,-5,-3,-6,7,10,8,-5,8,-8,10,5,-7,-1,-3,9,2,-2,-6],[-2,2,-7,7,-3,5,2,-5,-7,7,-1,6,4,-4,3,-9,-5,6,-1,-3,-9,-8,-4,-10,-5,8,7,6,2,-10,-9,1,-1,-5,-9,9,-7,-3,-9,-1,-1,-8,10,10,1,-8,-2,-4,5,5,8,-6,-10,7,1,2,4,10,6,-10,1,-9,9,6,-5,-10,7,-9,2,-8,5,-6,-4,4,6,6,4,-2,1,6,1,8,-1,-8,-6,-7,8,1,-8,9,1,-3,3,9,-5,9,-1,7,7,-7,2,5,7,-2,-10,-1,8,-5,3,-6,-9,8,3,5,3,-4,-6,-6,4,-10,-1,-5,-8,2,6,-2,5,8,5,10,5,-2,-5,-4,6,-1,-4,8,9,-3,-9,2,3,2,5,-4,7,9,-4,-9,6,1,-8,-2,-10,4,8,-1,-7,-8,6,3,10,3,5,-8,2,1,-8,-9,-7,-6,-10,-7,2,1,1,-1,-4,-9,-6,1,6,-10,-6,1,-3,-2,7,-9,-7,9,4,1,4,-8,4,-10,3,5,8,-7,-4,-3,-10,-2,-5,-5,10,-7,-5,-5,-6,9,5,-3,1,-6,-10,-10,3,7,10,7,7,4,-10,-1,4,-10,-6,-3,-2,6,8,-10,7,-1,9,-6,-3,-10,-1,-3,-3,-5,-3,-7,-5,-7,-10,-6,-6,3,6,-4,2,-5,-5,10,-1,-6,-1,-1,8,3,-9,-3,7,-10,5,-5,-8,-2,1,8,4,8,6,6,-9,2,-8,-5,-10,10,-1,-4,5,1,-7,8,2,9,-7,-4,3,-6,-2,8,6,-9,4,5,9,-7,-4,10,-1,7,-5,4,-8,1,-1,-4,-8,5,6,1,-5,-2,3,8,10,-4,8,-4,-10,6,3,-10,3,-3,5,-2,4,9,5,-3,-3,-1,7,-7,10,10,-5,8,-8,-5,-7,-3,-3,2,2,-7,4,-7,-3,8,8,-1,-10,1,10,-3,4,-9,10,9,7,-8,3,-2,10,2,-1,2,-1,-1,8,-7,-10,1,10,-4,5,-7,-9,-5,-2,6,-9,5,1,1,10,4,-6,1,-5,2,9,8,-10,-7,-9,6,-1,-8,-8,2,8,-1,-8,-8,-9,5,-10,6],[-6,-4,5,-5,-4,-7,-3,-2,2,3,6,-7,4,5,-6,5,3,9,3,4,-8,-2,9,-1,-9,-5,8,2,-5,-7,7,5,3,-7,7,-6,2,5,3,-6,-2,9,-2,-5,7,8,-4,-3,-8,-3,-4,1,6,9,3,2,-6,-9,-10,-7,-4,3,9,-5,8,1,9,-10,-7,-6,6,-8,-7,-1,1,5,3,5,6,9,2,-8,2,-7,8,-1,-1,7,6,-6,5,4,1,-2,-1,-3,-8,5,-10,9,6,-2,-9,-5,-6,3,2,9,-9,10,-1,3,3,-1,10,1,-10,-3,2,5,6,-9,-5,4,1,-4,-9,2,-6,-5,3,-2,-10,3,2,-10,-5,-1,-9,-6,8,-3,-10,-9,9,5,-3,-8,-4,5,-8,6,-5,-8,1,5,6,6,-6,-4,-10,-1,-6,6,-10,5,7,3,-8,6,-5,-1,-2,8,-2,5,9,-5,-2,4,3,2,-1,-1,6,-10,-10,-3,-8,2,-1,-3,2,-5,2,-8,9,4,3,-10,-5,-9,3,-9,2,4,8,-6,-7,5,-2,-4,-1,10,-6,-4,-5,7,-4,3,-8,9,-6,6,-6,5,-4,-9,-9,-8,3,7,-4,8,-1,-3,-9,4,-7,-9,1,-3,2,9,-10,8,8,1,-10,-1,-1,-9,-9,6,-3,-3,8,9,-5,-1,5,10,5,-9,-2,5,5,6,8,3,6,8,-1,3,-7,-3,-4,-8,-4,-3,7,2,3,-9,-9,-2,8,8,-9,5,5,-10,3,-7,5,3,-9,8,-4,-1,-9,9,-5,7,10,-1,2,-6,-9,1,-5,8,1,6,-2,10,1,7,8,3,-7,-3,-4,-5,-3,9,-3,2,4,1,8,-7,1,-7,9,-7,4,7,-8,-3,9,9,-10,7,-2,9,-2,-8,-2,3,5,-10,-1,-9,9,10,-3,-1,-3,-6,-9,-2,5,5,7,9,-10,-2,-3,-10,10,-2,2,-5,-4,-7,-10,-7,10,-2,-1,-8,-7,-2,9,7,-3,-2,4,9,2,4,-6,7,-2,3,-10,-4,1,-9,9,2,7,-6,-3,1,-10,9,4,4,-5,-1,7,-3,-1,-1,-10,-2,-6,8]], dtype = "int16")#candidate|4214|(4, 420)|const|int16
const_4215 = relay.const([[3.815306,3.442374],[2.510987,5.304192],[-6.672391,-7.895354],[-6.474530,8.821983],[-3.123096,0.240341],[9.320342,4.678151],[-1.699020,4.646498],[4.504747,6.695058],[-9.778300,-1.197428],[8.340091,3.759698],[-3.806719,-4.257208],[-1.322771,6.950668],[9.657443,6.743251],[-7.714029,2.962557],[-7.734994,7.246420],[2.009126,-0.496159],[-8.810470,-0.567706],[-0.312490,3.324402],[9.975894,-1.282759],[4.289172,-4.843432],[-1.856802,-6.411236],[-6.661428,3.406705],[-7.265865,-6.927559],[2.193541,1.299929],[-7.751085,6.006192],[8.865876,8.624141],[-2.804535,2.662320],[3.929684,4.304335],[5.770921,9.064581],[2.894282,-9.987333],[1.703084,-5.868034],[9.343675,-7.532883],[1.300643,3.116227],[3.331353,6.271724],[-5.846188,0.087255],[-3.103784,2.560886],[-3.464460,5.918223],[-7.675770,-5.841653],[-2.594795,-2.189326],[-8.617791,9.568947],[8.937216,3.788555],[1.307611,-8.280522],[2.026505,-6.586846],[-2.713727,6.039264],[-3.319296,3.910039],[6.490968,-9.542612],[-2.209392,1.528763],[-1.300348,-6.379223],[5.726702,-6.287786],[-7.121417,-1.840973],[-5.499361,9.765487],[4.085532,-2.529174],[3.485350,-2.875338],[3.380520,-6.632678],[6.247817,-9.404785],[2.536064,2.459823],[-4.242104,9.919182],[3.081651,-1.965648],[-1.018100,-1.869033],[7.298397,2.196862],[-2.584992,0.210513],[0.338493,5.672266],[4.463254,-1.222521],[-0.960509,-6.022397],[3.397171,3.851384],[8.551219,-6.621312],[7.946313,7.166426],[9.701623,9.749631],[-4.148209,3.919415],[1.478316,6.645854],[6.904025,9.950877],[4.312676,-1.024905],[8.852670,3.596051],[-7.859415,5.795241],[0.650101,-7.997941],[4.238094,-0.084157],[-0.506642,7.198720],[3.622203,-2.872957],[-9.046187,-5.670982],[0.820007,-9.689399],[1.052784,-7.015726],[-4.417703,7.020060],[-8.885762,-8.738679],[-9.253820,-9.711111],[5.481956,-4.877232],[-7.464191,5.448918],[-1.107259,-7.715758],[-0.229959,-8.440205],[6.890813,2.532999],[-3.634691,8.892572],[-1.113872,1.065449],[-9.265950,0.264853],[3.530322,-1.034111],[6.740530,3.302383],[-2.721601,4.632478],[-0.301558,-7.244060],[-1.370708,1.802117],[-0.864191,-2.479644],[4.283254,8.104319],[7.224233,8.293140],[-6.485632,-9.648935],[7.369824,8.551827],[1.812374,-1.174687],[8.241816,4.206293],[4.565340,-8.912645],[4.711535,-6.543944],[-3.621251,8.712009],[5.375796,0.511299],[-4.819239,1.112458],[9.820571,6.644330],[5.561919,-5.341726],[-6.626721,9.800513],[8.560969,-0.050025],[-6.177905,8.129580],[-0.633596,-8.510115],[2.511485,-8.171330],[5.671751,2.347086],[-2.119980,5.035938],[-6.722642,-4.657913],[-2.144466,-7.543872],[-1.616355,-3.979526],[-8.717378,4.610273],[-3.157091,-7.790383],[1.480073,-5.802019],[-3.188445,8.997155],[-5.725430,-7.649323],[9.348103,-1.637232],[-6.040864,4.186552],[3.864770,3.971277],[4.240784,-3.705624],[-8.433630,1.801715],[8.083570,-7.901881],[5.261593,4.781839],[2.006431,-7.695043],[-4.117534,-8.106977],[-3.681980,7.746161],[1.500065,4.528489],[-3.356958,5.549718],[-1.870733,-7.684556],[-1.758665,2.364494],[1.283648,6.715619],[-6.026743,8.048134],[-5.128624,-9.648838],[7.064525,-5.370624],[-7.902626,8.226355],[-8.448105,-7.649669],[6.696662,-6.607718],[6.760291,3.781127],[-0.313532,9.961583],[-8.135800,-4.740952],[-4.436931,7.856162],[-3.538185,1.656290],[8.328707,1.517180],[0.071787,-3.848970],[4.018521,-9.317301],[-1.071661,1.160696],[-1.852989,-7.138941],[7.612852,-0.569062],[8.726198,9.307894],[1.540189,-6.001092],[3.904486,-5.047103],[4.950770,0.720912],[-9.909525,-7.317928],[9.665191,7.887290],[-6.596470,-7.899551],[-9.399332,-6.743709],[1.875315,-3.496979],[-0.138576,9.994518]], dtype = "float64")#candidate|4215|(168, 2)|const|float64
call_4212 = relay.TupleGetItem(func_3376_call(relay.reshape(const_4213.astype('float32'), [15, 6, 3]), relay.reshape(const_4214.astype('int16'), [1680,]), relay.reshape(const_4215.astype('float64'), [336,]), ), 1)
call_4216 = relay.TupleGetItem(func_3381_call(relay.reshape(const_4213.astype('float32'), [15, 6, 3]), relay.reshape(const_4214.astype('int16'), [1680,]), relay.reshape(const_4215.astype('float64'), [336,]), ), 1)
output = relay.Tuple([bop_4200,call_4212,const_4213,const_4214,const_4215,])
output2 = relay.Tuple([bop_4203,call_4216,const_4213,const_4214,const_4215,])
func_4217 = relay.Function([var_4199,], output)
mod['func_4217'] = func_4217
mod = relay.transform.InferType()(mod)
var_4218 = relay.var("var_4218", dtype = "float64", shape = (9, 14, 8))#candidate|4218|(9, 14, 8)|var|float64
output = func_4217(var_4218)
func_4219 = relay.Function([var_4218], output)
mutated_mod['func_4219'] = func_4219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_4310 = func_3085_call()
call_4311 = func_3085_call()
output = call_4310
output2 = call_4311
func_4324 = relay.Function([], output)
mod['func_4324'] = func_4324
mod = relay.transform.InferType()(mod)
output = func_4324()
func_4325 = relay.Function([], output)
mutated_mod['func_4325'] = func_4325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_4355 = relay.TupleGetItem(func_3183_call(), 3)
call_4356 = relay.TupleGetItem(func_3184_call(), 3)
output = relay.Tuple([call_4355,])
output2 = relay.Tuple([call_4356,])
func_4362 = relay.Function([], output)
mod['func_4362'] = func_4362
mod = relay.transform.InferType()(mod)
output = func_4362()
func_4363 = relay.Function([], output)
mutated_mod['func_4363'] = func_4363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1579_call = mod.get_global_var('func_1579')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_4382 = relay.TupleGetItem(func_1579_call(), 0)
call_4383 = relay.TupleGetItem(func_1580_call(), 0)
output = relay.Tuple([call_4382,])
output2 = relay.Tuple([call_4383,])
func_4401 = relay.Function([], output)
mod['func_4401'] = func_4401
mod = relay.transform.InferType()(mod)
output = func_4401()
func_4402 = relay.Function([], output)
mutated_mod['func_4402'] = func_4402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_4449 = func_3085_call()
call_4450 = func_3085_call()
func_2259_call = mod.get_global_var('func_2259')
func_2262_call = mutated_mod.get_global_var('func_2262')
var_4454 = relay.var("var_4454", dtype = "float64", shape = (360,))#candidate|4454|(360,)|var|float64
const_4455 = relay.const([[8.232974,2.017296,0.504136,-1.947539,-4.020474,-2.810652,-1.842961,7.594758,8.651116,-5.667736,2.668268,-0.303930,-8.000213,-0.587669,4.880541,5.072571,8.378592,2.269293,-9.642959,-7.042955,-8.828239,-7.199961,8.380826,-6.330779,-8.026807,7.641976,1.391261,-5.299435,-3.105805,-1.248361,6.844805,-9.824280,-9.327391,1.441158,6.876555,4.139618,-7.978566,5.437127,0.227196,-6.704447,-5.025421,-9.110768,-0.380487,1.353048,1.900912,-6.636292,7.141650,4.036333,-4.270582,-4.212623,-3.830600,-3.129913,1.929727,-1.958960,1.231971,4.276163,9.663124,0.890398,-9.423051,-6.750515,-4.461591,-3.045535,9.317101,-9.763697,-8.366726,-7.936506,-2.784975,8.532691,-7.384096,2.394913,2.038675,3.534627,-4.011879,-2.403866,-1.004828,-5.047952,1.422202,-1.779700,-1.511695,-6.112549,-1.409670,6.906146,4.417075,-6.053380,0.036062,5.310471,-9.178777,0.354656,1.140280,4.318420,-6.496378,6.407993,-6.129897,-5.289434,-3.268590,1.052152,8.007602,4.334166,-1.833511,-8.501810,2.478539,-7.324803,6.116317,-9.779203,9.819941,-2.784966,0.196392,6.436965,2.446849,-1.837187,-0.255862,-8.076394,1.352065,1.037566,-2.327522,8.664220,6.337640,1.394037,4.338698,-0.062319,-4.473003,-7.430415,-1.956126,3.148226,5.707498,4.402173,-5.557422,-9.887081,1.523988,2.264293,4.486644,-7.419252,-3.131917,4.874529,2.800679,-5.953071,-3.921833,-3.952378,-9.785956,1.374230,9.339615,8.881933,-3.405823,0.829668,2.417096,2.716177,5.541538,-9.404239,-4.577223,2.018290,5.206238,7.030761,-1.936176,-4.929660,4.779113,3.853821,-8.649401,-0.667854,-7.510942,-2.191696,-5.098786,-5.589926,1.950214,7.767805,6.417913,-7.494153,-0.106788,-6.330309],[4.879708,5.682480,-2.241473,2.833557,-8.248936,-4.884099,-1.682097,-5.423158,-7.085933,-1.239071,1.654017,0.491227,4.784788,0.792294,9.675853,-9.992654,-1.872638,-8.256966,-3.891173,8.933942,1.452533,4.206363,1.777230,2.617618,5.288773,6.633604,8.004269,8.379035,-7.999678,4.056587,-9.795625,-1.625627,4.510343,-0.766078,4.620542,-6.851986,2.934093,-0.356437,-2.737420,-6.598856,7.251974,-5.959833,8.188748,6.370950,8.106051,4.976094,6.477426,-5.012504,-2.528306,-0.098079,4.307019,6.796333,3.081624,0.092268,4.279162,2.278729,7.144674,6.967274,9.762725,6.504766,8.153852,-4.892049,-0.166292,-3.138380,7.586849,-2.661152,0.052228,2.680891,2.231744,-6.524049,8.507649,-6.461986,-7.398740,3.124824,-7.309502,-8.785404,2.584874,-2.023526,5.458595,7.430581,-3.719625,7.296222,3.587117,-6.254940,3.683384,5.272485,-7.872007,-7.912461,9.944724,-9.624843,-5.454500,-1.873174,8.719717,0.203804,5.521861,-6.755710,8.134593,8.672281,-7.550633,9.172631,8.698127,-5.790576,-7.937277,-2.782557,-0.541897,-2.553348,0.745130,5.920010,6.267493,1.265064,6.490804,-6.568629,-3.361398,7.313017,8.862716,-5.568394,1.212373,-0.229249,4.360342,1.123248,7.364114,-8.777307,-8.323595,-3.096969,4.194147,-0.721461,9.056748,9.692743,2.635956,-8.520413,9.828726,6.474168,-3.225952,1.676842,-2.729578,9.455871,-4.149714,-3.332493,3.231349,-4.946513,-0.577782,7.005435,-8.227799,7.693148,3.864640,-9.986167,8.987406,2.598555,-2.988099,8.130841,-3.112181,-8.451369,5.073627,2.957103,8.930551,3.758770,6.852643,0.708614,5.140353,2.579216,2.218677,9.263540,8.813743,-3.347176,9.443090,-1.823694,-1.686792,-0.794281]], dtype = "float64")#candidate|4455|(2, 168)|const|float64
call_4453 = relay.TupleGetItem(func_2259_call(relay.reshape(var_4454.astype('float64'), [2, 15, 12]), relay.reshape(const_4455.astype('float64'), [336,]), ), 2)
call_4456 = relay.TupleGetItem(func_2262_call(relay.reshape(var_4454.astype('float64'), [2, 15, 12]), relay.reshape(const_4455.astype('float64'), [336,]), ), 2)
func_1308_call = mod.get_global_var('func_1308')
func_1309_call = mutated_mod.get_global_var('func_1309')
call_4463 = func_1308_call()
call_4464 = func_1308_call()
output = relay.Tuple([call_4449,call_4453,var_4454,const_4455,call_4463,])
output2 = relay.Tuple([call_4450,call_4456,var_4454,const_4455,call_4464,])
func_4489 = relay.Function([var_4454,], output)
mod['func_4489'] = func_4489
mod = relay.transform.InferType()(mod)
mutated_mod['func_4489'] = func_4489
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4490 = relay.var("var_4490", dtype = "float64", shape = (360,))#candidate|4490|(360,)|var|float64
func_4489_call = mutated_mod.get_global_var('func_4489')
call_4491 = func_4489_call(var_4490)
output = call_4491
func_4492 = relay.Function([var_4490], output)
mutated_mod['func_4492'] = func_4492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_4565 = relay.TupleGetItem(func_4147_call(), 0)
call_4566 = relay.TupleGetItem(func_4148_call(), 0)
output = call_4565
output2 = call_4566
func_4578 = relay.Function([], output)
mod['func_4578'] = func_4578
mod = relay.transform.InferType()(mod)
mutated_mod['func_4578'] = func_4578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4578_call = mutated_mod.get_global_var('func_4578')
call_4579 = func_4578_call()
output = call_4579
func_4580 = relay.Function([], output)
mutated_mod['func_4580'] = func_4580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_4619 = relay.TupleGetItem(func_1745_call(), 0)
call_4620 = relay.TupleGetItem(func_1746_call(), 0)
output = relay.Tuple([call_4619,])
output2 = relay.Tuple([call_4620,])
func_4625 = relay.Function([], output)
mod['func_4625'] = func_4625
mod = relay.transform.InferType()(mod)
mutated_mod['func_4625'] = func_4625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4625_call = mutated_mod.get_global_var('func_4625')
call_4626 = func_4625_call()
output = call_4626
func_4627 = relay.Function([], output)
mutated_mod['func_4627'] = func_4627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_4640 = func_1857_call()
call_4641 = func_1857_call()
func_1015_call = mod.get_global_var('func_1015')
func_1018_call = mutated_mod.get_global_var('func_1018')
var_4644 = relay.var("var_4644", dtype = "int32", shape = (234,))#candidate|4644|(234,)|var|int32
call_4643 = relay.TupleGetItem(func_1015_call(relay.reshape(var_4644.astype('int32'), [13, 3, 6]), relay.reshape(var_4644.astype('int32'), [13, 3, 6]), ), 0)
call_4645 = relay.TupleGetItem(func_1018_call(relay.reshape(var_4644.astype('int32'), [13, 3, 6]), relay.reshape(var_4644.astype('int32'), [13, 3, 6]), ), 0)
output = relay.Tuple([call_4640,call_4643,var_4644,])
output2 = relay.Tuple([call_4641,call_4645,var_4644,])
func_4654 = relay.Function([var_4644,], output)
mod['func_4654'] = func_4654
mod = relay.transform.InferType()(mod)
var_4655 = relay.var("var_4655", dtype = "int32", shape = (234,))#candidate|4655|(234,)|var|int32
output = func_4654(var_4655)
func_4656 = relay.Function([var_4655], output)
mutated_mod['func_4656'] = func_4656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4660 = relay.var("var_4660", dtype = "uint32", shape = ())#candidate|4660|()|var|uint32
const_4661 = relay.const([[[-1,-10,-1,-9,-4,7,1,1,7,1,-8,-9,1],[-9,-10,1,-5,-2,-9,-1,8,-8,3,-8,5,-6],[-4,-7,-4,-2,-5,8,3,8,-3,-6,-6,3,2],[-10,3,-10,-10,-2,5,3,-6,-2,2,-10,1,-7]],[[-10,6,2,-1,-1,1,-9,-10,-6,4,3,-10,6],[-2,-8,3,1,-10,-7,-9,-3,10,3,4,-2,-3],[4,1,-5,-8,4,-1,-3,10,-3,8,9,-5,7],[-4,-8,3,-2,4,7,-2,-5,10,5,10,8,3]],[[-6,-10,8,2,-10,-1,-9,-10,9,9,-7,6,8],[-10,-3,-4,1,-2,5,-8,8,7,-6,-4,-1,1],[-4,9,-2,-10,2,-4,7,6,1,-9,3,4,5],[4,-3,-5,1,-10,-3,-10,4,1,-3,3,9,10]],[[-8,-1,6,-2,-10,5,10,-6,8,9,-1,3,-7],[7,8,8,-6,2,4,-9,10,-6,3,-3,-10,-3],[5,7,2,-8,1,-6,-4,-9,2,-3,-5,-1,10],[9,10,-3,8,9,-1,-8,-4,1,5,-8,-7,-7]],[[9,1,6,1,10,3,3,-7,10,9,4,-3,10],[-3,-2,1,10,3,10,2,-8,-9,8,7,5,-3],[8,5,-9,8,1,-3,9,-5,-9,-2,-3,-2,-9],[8,-7,-3,8,6,6,-9,3,-8,-9,3,1,9]],[[-6,-4,9,9,2,2,7,7,2,-2,7,7,-2],[-6,-4,6,3,5,3,-8,3,7,8,5,10,-4],[7,5,-10,2,-5,3,10,1,-1,8,-1,-6,-9],[-10,10,5,7,-5,-10,-2,5,2,5,-7,-4,-10]],[[2,-5,-7,-7,3,2,-10,7,-6,-5,-6,6,-2],[-8,10,3,-2,-2,-7,5,10,10,-8,10,-7,5],[-3,7,-6,2,-10,9,-5,-2,9,-10,7,-9,-6],[7,5,9,4,3,-10,7,2,-6,8,-7,5,6]],[[-9,5,5,1,5,-7,-7,-1,7,-10,6,8,-4],[-1,-4,1,1,9,1,3,9,6,-2,6,3,-10],[2,2,-3,-6,-7,10,-4,-1,6,-10,-6,4,1],[1,6,4,-1,5,-7,-1,-6,4,8,5,-1,-1]],[[-9,-7,5,-6,-1,-10,-7,4,-3,-10,-8,1,10],[-1,10,10,-9,4,4,4,10,-8,8,-3,-9,-2],[-7,-2,-10,10,5,3,-6,7,-7,-7,-6,6,-7],[4,1,-10,2,7,-4,-4,-6,2,-4,-4,-1,-9]],[[-6,-10,-3,-6,4,-7,9,-10,3,-2,3,-1,-3],[9,5,-1,-1,1,-9,10,-6,-2,1,8,8,-2],[-1,7,7,-10,-1,3,-5,-8,5,8,5,4,1],[-9,-9,-7,4,-8,1,-5,-8,6,5,8,2,-9]]], dtype = "uint32")#candidate|4661|(10, 4, 13)|const|uint32
bop_4662 = relay.maximum(var_4660.astype('uint32'), const_4661.astype('uint32')) # shape=(10, 4, 13)
output = relay.Tuple([bop_4662,])
output2 = relay.Tuple([bop_4662,])
func_4673 = relay.Function([var_4660,], output)
mod['func_4673'] = func_4673
mod = relay.transform.InferType()(mod)
mutated_mod['func_4673'] = func_4673
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4674 = relay.var("var_4674", dtype = "uint32", shape = ())#candidate|4674|()|var|uint32
func_4673_call = mutated_mod.get_global_var('func_4673')
call_4675 = func_4673_call(var_4674)
output = call_4675
func_4676 = relay.Function([var_4674], output)
mutated_mod['func_4676'] = func_4676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3107_call = mod.get_global_var('func_3107')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_4796 = relay.TupleGetItem(func_3107_call(), 0)
call_4797 = relay.TupleGetItem(func_3108_call(), 0)
output = call_4796
output2 = call_4797
func_4816 = relay.Function([], output)
mod['func_4816'] = func_4816
mod = relay.transform.InferType()(mod)
output = func_4816()
func_4817 = relay.Function([], output)
mutated_mod['func_4817'] = func_4817
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4845 = relay.const([[[-0.259467,3.000857,-5.721912,2.116197,-0.568688,-9.019055,-5.531382,-3.869459,-2.219417,2.467606,4.279498,-3.636331],[-8.298263,-2.701751,-7.308008,6.196920,7.943831,8.032776,-8.079312,3.234471,0.656981,8.531214,3.620313,-4.716988],[-0.453930,-5.636743,9.788105,8.993291,6.531283,3.003195,2.195076,-7.935086,9.230820,-5.163646,0.610586,-4.521530],[6.534322,-2.587620,-6.338269,-5.751007,-2.044737,-1.396754,1.980571,9.117145,7.070498,2.252698,0.294208,-9.513606],[3.520929,-1.457789,-1.403618,8.057413,8.128926,-2.257253,-8.212778,-0.600064,6.184728,0.935174,-2.922463,-4.950632],[6.025634,-2.829655,2.424139,0.587412,7.476104,1.450245,0.950217,-9.129342,-2.144119,-6.056329,7.721568,-7.192275],[6.036269,-1.791110,-1.109136,7.167331,-9.133567,6.994523,-4.677659,-7.156781,-2.527156,5.633989,-7.747357,-2.200660],[9.260673,-4.599453,8.208919,3.261645,-2.457366,-0.313118,-5.748850,-0.169832,2.633728,1.346027,-5.090336,-5.173296],[2.637262,-5.290509,5.241836,5.060085,1.092823,2.366960,-8.840680,9.680142,-7.836899,1.830560,-9.451126,1.187791],[3.757953,4.833552,-3.199769,2.399041,-5.787007,-3.995217,-7.064444,-4.021219,5.605569,5.861913,-6.085248,-5.499032]],[[-0.896186,-9.397522,0.041867,4.851613,-6.791151,-0.285005,-9.632498,-7.614235,-2.479500,-6.579490,-8.215317,-2.276977],[-1.991137,3.652619,8.252408,-7.402139,-3.351710,-6.760427,-0.742010,-3.849185,-6.748553,-4.767933,-5.252761,9.256784],[7.897540,-7.938042,-6.442186,4.691136,-2.958848,-9.017468,-4.133218,8.934012,5.382801,-9.540190,4.159276,-7.422704],[7.326276,-4.056249,0.875146,-0.266091,3.205072,6.725130,-8.679107,6.919533,1.815136,-3.617928,-7.790893,-0.340145],[0.076800,9.684746,-1.937622,-0.285288,-4.173425,7.597975,3.634744,-1.553350,-7.382136,-8.276928,-8.136039,2.881376],[0.825141,0.390212,-2.470516,3.540742,-0.622228,-5.619156,-3.271931,6.702012,-7.698764,8.827242,-1.956221,-9.555281],[2.942311,4.696124,-1.691603,5.423289,-6.698789,3.688069,0.758704,-2.114721,-4.137627,-4.419627,-8.067185,4.962470],[-2.418709,-5.849887,7.683466,-3.517648,7.622183,-7.486815,-3.032086,-7.880046,8.884785,6.883093,-0.376110,-8.868027],[4.894175,-9.863739,-2.385869,-3.761441,-9.570881,-6.694302,9.408659,-5.270780,-2.332246,7.065322,-7.688852,-0.451246],[6.682390,-2.521804,6.265531,-8.250979,0.805904,-4.863783,9.027965,5.963484,1.667714,2.544731,-3.224800,-9.684640]],[[-8.015364,8.504659,6.648491,-2.538812,-0.267255,-8.033384,-7.330437,-4.492059,7.947712,1.700592,3.312495,-8.469104],[-6.112952,6.020832,3.216266,-0.603158,3.418906,8.938476,3.690908,-3.711985,-8.651084,0.358861,4.591322,6.110238],[4.005232,6.357311,7.454731,0.251707,6.543177,-8.124225,-2.735218,0.818647,-2.121926,-7.437209,-5.423137,8.066389],[-4.005867,7.650673,-3.210583,-6.222623,-9.346245,-4.921645,-4.938595,2.334459,3.643531,-1.535570,-3.409098,4.228604],[-6.185296,-1.167104,-3.075447,-7.328142,9.684798,6.398909,-9.369569,4.213882,0.193100,-4.911072,6.271107,-3.453580],[3.852726,7.713839,-7.510086,-3.570331,-7.044719,5.590064,3.403734,6.006776,-5.310851,-9.741515,1.558705,8.164033],[-9.395433,-9.555165,5.119693,-1.851511,1.383298,5.989433,-3.606967,2.074561,-8.956682,-7.080489,-4.563038,-1.890620],[-1.706409,3.437249,-7.995049,-1.353822,-9.092766,9.797820,2.759398,-5.512715,5.678541,-7.655365,2.069068,-5.260066],[8.488509,8.800022,3.158293,-7.819659,5.067698,0.134377,-3.403850,-4.410997,-6.235378,-2.642297,8.984844,-7.405917],[-2.064637,-3.916391,-9.685369,-1.369904,7.163516,0.606578,6.399860,-8.417777,4.197395,5.312635,-9.723555,-2.412187]],[[9.149667,-5.994129,0.385710,5.572771,-0.971395,-8.814382,-1.717582,-2.081030,-8.413452,-4.551637,5.444181,-2.156861],[-3.508747,-3.454302,7.690639,9.908379,3.601874,7.219768,5.247718,1.294296,3.637411,-6.380366,-3.326412,3.906469],[0.997909,-5.881847,5.823329,5.410958,-0.532094,-7.344514,6.355909,-8.877875,3.332021,0.190291,-8.587761,-2.448275],[-9.156577,-6.664818,7.739175,-9.234935,8.853404,8.566402,2.979219,1.083433,-7.976476,-8.809770,6.681167,8.095164],[-7.972793,2.955739,9.238357,-7.209558,6.761746,-5.122489,0.259983,5.172130,9.738434,0.552834,8.617920,1.564795],[-7.187435,1.344037,-1.292240,-9.717160,-2.153527,-7.409166,-5.780025,8.962381,3.082288,-8.217516,-1.389637,3.126732],[6.486955,9.031384,1.036841,-4.906964,-7.315768,-4.892611,-9.370174,6.769270,-5.247049,-5.984795,6.426021,-9.683545],[1.814849,5.727670,-1.638261,-3.131056,5.899928,7.046450,-9.728459,-0.108964,6.488260,3.215367,0.250300,-4.615440],[-0.094468,-9.649944,1.856936,-1.122864,-6.459794,-9.925995,4.443164,-0.352316,-6.236389,7.858628,6.348301,5.614764],[-3.143020,6.860490,-4.130332,-3.950656,-8.798767,-8.283977,2.637313,4.758762,-6.936081,3.866290,-7.070836,-6.686892]]], dtype = "float64")#candidate|4845|(4, 10, 12)|const|float64
const_4846 = relay.const([[[1.804311,4.572185,6.844555,4.729086,2.850511,6.861411,4.898973,5.479587,8.168120,-2.956414,-1.237711,-8.124832],[-7.111445,7.161752,-9.817764,7.828778,8.489007,-8.676574,-5.444287,7.595989,7.135474,6.899908,7.456975,-9.084336],[-4.432382,0.675913,1.014574,-1.766731,-5.839132,-1.901608,-7.256665,-0.738182,-0.251284,-7.460220,-7.702570,7.808438],[-7.183264,-9.033735,7.728928,-5.233481,-4.492154,-7.357488,-4.805469,2.662574,-1.234846,5.515606,6.010740,-3.686372],[-9.877527,2.426710,0.921359,4.772408,5.575961,9.769090,-6.698326,-8.879820,0.293001,5.125339,0.261876,-4.839418],[-9.359421,-1.214436,9.787931,-5.980941,-2.457498,-6.473496,-2.715919,1.528367,-3.522043,-9.497960,4.560352,9.183010],[9.876681,-0.896408,5.616847,-5.040368,-8.468731,-4.776556,2.800064,6.583641,-4.607239,9.013821,2.786541,-7.744647],[7.890861,5.888435,-8.073302,7.777270,6.905219,-4.023717,-7.900618,-9.527223,-3.836867,-4.869230,7.053082,1.052540],[-9.994046,-4.061754,0.693329,5.709808,5.390063,5.138339,0.477876,4.730207,-8.703649,9.511766,-0.534967,3.441158],[-0.321819,5.518034,-5.365743,9.245101,6.667976,-2.822873,1.576232,-1.647206,-9.618129,-7.844880,-0.732235,-1.614030]],[[4.874256,-7.111007,-7.239287,-1.483714,8.071546,-0.167896,-2.744291,-9.517203,-2.583351,3.881494,-9.784918,-8.830660],[9.255030,-8.118185,8.584977,1.838340,6.813390,-8.479606,0.057951,-6.520314,-7.923058,-0.751659,8.071976,5.003188],[-9.564597,5.952620,-7.562679,9.524509,-9.714093,7.815000,9.098832,-2.101084,-2.058226,-2.035800,-1.102122,2.681200],[1.407483,4.850413,-5.631726,-2.993708,1.039307,-4.979303,-9.534691,-9.823138,0.868767,-3.217214,-7.415400,9.555513],[5.904990,-8.218057,0.135375,0.038580,-4.626807,9.862566,1.316324,7.042037,9.842601,-6.449975,0.413923,-4.961892],[-0.680350,9.069421,7.638855,-4.688922,-4.084221,-4.281585,-5.358591,7.106858,1.587651,3.601931,-7.749735,6.089845],[-2.769971,7.680773,-6.473358,0.820128,-5.626767,9.287575,7.962803,1.180498,9.852858,4.126752,1.340691,-0.836377],[4.099574,7.839962,-3.201727,4.739794,-9.238882,-6.002516,-0.538136,9.645659,0.781366,1.670209,-6.931801,-1.764267],[-3.090482,4.439151,-9.736530,-3.476552,-8.266604,-9.138792,9.243804,1.925505,-2.754759,-4.003707,3.963655,-0.688177],[1.028392,-2.386323,-8.949068,6.557606,-2.032379,-1.856060,-7.781331,5.897442,-3.801251,5.980190,4.573398,5.418053]],[[-7.274844,5.898574,7.928583,-8.152989,0.758416,4.807281,-0.453388,-9.778714,1.669735,3.855405,-1.931971,-3.359638],[-4.488173,-3.314161,3.766020,-6.129289,7.847178,1.160083,3.966373,1.226768,-0.602220,-0.887056,0.844429,-3.781280],[7.261553,-8.647950,-2.174627,-3.128346,-8.758780,-1.071211,-5.844316,-5.832702,-6.626785,-3.245120,3.961769,-8.587457],[-7.413263,-4.698254,-3.471250,5.763639,2.291839,5.778212,-6.508734,-3.873422,-9.371253,-2.447096,2.844571,-1.309602],[2.898223,4.053200,3.739345,-6.261416,-2.147413,1.783106,4.287805,-3.239363,2.730812,-3.608627,4.521887,-2.552289],[-6.870851,-2.797861,7.130157,0.187059,-7.104663,-9.791757,3.941707,7.439493,6.250166,-7.804414,2.653584,6.747253],[-9.451843,6.962987,7.795106,2.028093,-8.759086,2.571520,-5.908283,-5.069821,-1.180874,-6.263964,-7.868080,5.506151],[7.206340,-2.253280,9.146093,9.644327,-9.847115,4.053724,-6.582867,8.945337,3.876661,3.333332,4.863513,-7.029999],[-4.249525,5.469713,-6.392910,-7.550865,-0.608877,9.854293,2.694505,2.828989,6.635534,0.877694,2.325877,-5.466748],[2.170628,4.177663,-9.381733,-8.632990,-8.082899,9.828676,4.253634,-6.478740,-4.658082,5.661855,-3.897157,2.078764]],[[4.740718,-8.329757,3.446795,4.939554,-5.090977,-1.024270,-4.480408,1.546824,-1.230667,-3.319441,-2.323741,-5.475911],[-9.792055,-7.856949,-6.714746,-2.353850,-8.055718,7.301804,2.427635,7.045396,7.350208,-6.742334,-5.811828,-4.539153],[-9.559735,-6.063285,-6.683896,-0.598983,-4.112128,9.763876,-8.872428,1.696037,-2.549320,0.967698,7.707824,4.614121],[-8.952228,8.171857,0.901333,7.978275,-8.267487,6.107148,-3.822142,0.870081,-9.768928,-9.119265,-0.357186,-3.985237],[-9.650047,-3.902112,-7.033147,-9.236049,-9.122013,1.026951,4.872603,8.738240,3.312628,-1.298259,-3.871227,-3.427199],[1.693632,-2.402385,-8.400838,-2.339754,-9.952418,8.966089,9.195624,3.662428,5.561180,8.712681,7.318691,-0.979563],[3.026762,1.875881,-8.094039,8.924436,-2.289469,3.346733,-8.200476,9.209797,-9.678557,2.933766,-5.972924,5.854500],[1.997508,-7.996261,-5.483095,0.268708,-2.807349,5.118189,6.094593,-3.936638,-9.928777,-2.667726,1.255348,1.212058],[-2.956135,0.005670,8.309386,-5.047113,-3.998713,-6.943860,9.835740,-2.003564,-0.461410,-1.924109,-3.749520,0.929237],[-1.887138,5.284788,5.635716,-0.900853,8.215324,-9.832902,-3.775137,-8.024253,7.649888,1.489977,-8.786274,-3.789729]]], dtype = "float64")#candidate|4846|(4, 10, 12)|const|float64
bop_4847 = relay.power(const_4845.astype('float64'), relay.reshape(const_4846.astype('float64'), relay.shape_of(const_4845))) # shape=(4, 10, 12)
output = relay.Tuple([bop_4847,])
output2 = relay.Tuple([bop_4847,])
func_4887 = relay.Function([], output)
mod['func_4887'] = func_4887
mod = relay.transform.InferType()(mod)
mutated_mod['func_4887'] = func_4887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4887_call = mutated_mod.get_global_var('func_4887')
call_4888 = func_4887_call()
output = call_4888
func_4889 = relay.Function([], output)
mutated_mod['func_4889'] = func_4889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1720_call = mod.get_global_var('func_1720')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_4964 = func_1720_call()
call_4965 = func_1720_call()
func_3937_call = mod.get_global_var('func_3937')
func_3938_call = mutated_mod.get_global_var('func_3938')
call_4969 = relay.TupleGetItem(func_3937_call(), 0)
call_4970 = relay.TupleGetItem(func_3938_call(), 0)
uop_4975 = relay.sinh(call_4964.astype('float32')) # shape=(100, 2)
uop_4977 = relay.sinh(call_4965.astype('float32')) # shape=(100, 2)
output = relay.Tuple([call_4969,uop_4975,])
output2 = relay.Tuple([call_4970,uop_4977,])
func_4988 = relay.Function([], output)
mod['func_4988'] = func_4988
mod = relay.transform.InferType()(mod)
mutated_mod['func_4988'] = func_4988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4988_call = mutated_mod.get_global_var('func_4988')
call_4989 = func_4988_call()
output = call_4989
func_4990 = relay.Function([], output)
mutated_mod['func_4990'] = func_4990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_5015 = relay.TupleGetItem(func_3542_call(), 0)
call_5016 = relay.TupleGetItem(func_3544_call(), 0)
func_3659_call = mod.get_global_var('func_3659')
func_3660_call = mutated_mod.get_global_var('func_3660')
call_5039 = func_3659_call()
call_5040 = func_3659_call()
bop_5044 = relay.less_equal(call_5015.astype('bool'), relay.reshape(call_5039.astype('bool'), relay.shape_of(call_5015))) # shape=(9, 1, 8)
bop_5047 = relay.less_equal(call_5016.astype('bool'), relay.reshape(call_5040.astype('bool'), relay.shape_of(call_5016))) # shape=(9, 1, 8)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_5053 = relay.TupleGetItem(func_1174_call(), 1)
call_5054 = relay.TupleGetItem(func_1176_call(), 1)
func_4887_call = mod.get_global_var('func_4887')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_5056 = relay.TupleGetItem(func_4887_call(), 0)
call_5057 = relay.TupleGetItem(func_4889_call(), 0)
bop_5064 = relay.floor_divide(call_5039.astype('float64'), relay.reshape(call_5015.astype('float64'), relay.shape_of(call_5039))) # shape=(9, 1, 8)
bop_5067 = relay.floor_divide(call_5040.astype('float64'), relay.reshape(call_5016.astype('float64'), relay.shape_of(call_5040))) # shape=(9, 1, 8)
uop_5103 = relay.log(call_5056.astype('float32')) # shape=(4, 10, 12)
uop_5105 = relay.log(call_5057.astype('float32')) # shape=(4, 10, 12)
output = relay.Tuple([bop_5044,call_5053,bop_5064,uop_5103,])
output2 = relay.Tuple([bop_5047,call_5054,bop_5067,uop_5105,])
func_5107 = relay.Function([], output)
mod['func_5107'] = func_5107
mod = relay.transform.InferType()(mod)
mutated_mod['func_5107'] = func_5107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5107_call = mutated_mod.get_global_var('func_5107')
call_5108 = func_5107_call()
output = call_5108
func_5109 = relay.Function([], output)
mutated_mod['func_5109'] = func_5109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_5116 = func_1857_call()
call_5117 = func_1857_call()
output = call_5116
output2 = call_5117
func_5118 = relay.Function([], output)
mod['func_5118'] = func_5118
mod = relay.transform.InferType()(mod)
output = func_5118()
func_5119 = relay.Function([], output)
mutated_mod['func_5119'] = func_5119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2713_call = mod.get_global_var('func_2713')
func_2714_call = mutated_mod.get_global_var('func_2714')
call_5129 = relay.TupleGetItem(func_2713_call(), 0)
call_5130 = relay.TupleGetItem(func_2714_call(), 0)
func_3645_call = mod.get_global_var('func_3645')
func_3648_call = mutated_mod.get_global_var('func_3648')
const_5146 = relay.const([2.067839,-5.148776,8.465111,-8.671809,-5.080887,-6.536485,-1.011371,-8.630652,6.441072,1.485727,-8.808151,-0.198023,8.670771,6.216572,0.725993,0.134475,-8.136530,0.672197,-9.167046,-0.663301,-2.971216,7.047674,2.132510,7.870547,-9.036911,-5.166485,1.583132,8.092068,-8.859504,9.825286,7.143377,-3.800227,8.858307,9.388703,8.100228,-2.873328,-4.720134,4.280992,9.094786,-4.977201,3.084314,5.806759,9.806067,7.476940,6.631044,-5.908611,-5.060675,-7.720110,-7.569568,3.026091,1.343078,9.062390,2.130675,0.344175,-8.536922,-7.906914,-8.574886,-9.119137,-9.809321,-7.467772,6.744886,-7.639026,7.261665,9.878416,-1.110914,-4.908422,-2.559113,3.888036,-1.407273,-8.892063,-7.602865,-3.899136,-0.357371,7.281946,-9.276124,-9.386082,-3.043385,8.491638,0.414795,5.129709,-1.732944,-5.381962,-2.572542,-7.384604,-0.176281,7.646429,-9.650030,-1.981022,-8.784561,5.061309,3.492067,-2.554120,3.218991,9.967278,-3.286705,-0.548554,-0.133344,3.098886,3.953893,9.888630,9.757772,-4.940570,-7.594003,-4.443598,-5.372544,-8.880292,-8.652871,6.013983,-6.764511,-8.307573,-8.125054,0.829922,7.224231,2.312531,4.750901,0.230025,6.439517,-0.503842,-0.204903,-0.680921,-3.686837,-9.741828,-9.343087,-1.492732,-7.072052,1.711223,-9.043553,-8.002936,-8.075077,-2.125812,-3.219954,-7.325892,9.042224,-1.637046,0.933317,0.476826,6.336577,-3.998911,1.719327,-7.968982,-5.948716,-5.613782,9.845020,-0.408430,-9.707161,6.296141,-3.063376,-8.016811,-0.973723,8.628500,-9.046814,5.286986,-1.950616,6.663436,0.392661,-0.355194,2.248495,-1.263093,1.110862,-9.017163,4.290626,-5.268838,0.221102,7.156546,6.179874,-2.087386,7.721924,5.059384,7.788222,-4.659200,1.739680,-5.555794,7.643763,1.131951,-1.947427,3.664217,6.948864,0.683201,-4.893365,-9.439927,-3.176924,3.438268,-6.171336,8.274519,9.573494,-3.224317,-8.182241,-1.069094,4.077366,-3.950792,7.297876,0.958799,-1.901155,-6.016081,-5.255659,-7.838160,4.497599,-4.718249,4.452928,5.952908,0.689464,6.431069,7.163661,-8.972567,7.414200,-8.436733,-4.501843,6.268615,-4.940819,6.269732,-8.218218,4.472751,-6.397131,5.786951,-3.969962,-5.007172,3.437122,5.891141,0.005205,8.608670,4.332444,-0.062747,-5.387292,-7.874871,0.919620,4.824442,9.734534,5.893170,-5.766353,2.919302,0.537166,2.176023,3.372022,5.566069,-6.475461,5.300495,-5.333698,2.409515,5.799216,-0.215483,5.038340,-4.497352,-4.348718,-0.092482,6.450831,8.281983,-8.858585,1.998905,-9.820122,-5.405167,3.663822,-2.173259,9.079995,-2.980507,6.704097,1.935826,-4.464234,8.299516,1.739828,-9.745085,-2.214537,-0.759422,-3.012838,-7.552839,-8.560710,6.179932,4.572584,-3.522460,0.774166,0.590343,6.743892,8.642409,7.800305,-8.231289,4.867865,0.617040,7.352146,-2.960154,7.571222,-9.574355,8.724113,4.601898,2.509285,-9.503650,6.631392,8.554290,-8.581675,-1.310049,2.729371,9.377306,5.758841,-2.067801,-5.397386,-7.734522,-0.811442,8.550923,-6.686705,-2.593431,-3.163652,-7.760908,-9.788627,-3.471741,9.901008,-8.852239,-3.155856,1.547548,-0.928188,-7.064493,-0.257816,-4.468765,4.039293,-6.622472,6.996884,5.831602,1.036261,1.265789,6.924959,4.356535,-1.313774,3.785722,3.474825,1.331194,3.897896,-6.017532,-0.999844,-3.909881,-9.343358,-4.145856,5.383475,-9.823467,9.548803,-3.253126,9.369583,2.828210,-0.916341,-5.183997,1.333349,6.634912,5.199193,-8.407295,5.522868,8.797202,-2.828802,3.367187,8.588214,-8.835288,6.870170,0.148994,-5.905016,-5.600906,-7.228952,-6.538877,-0.219261,-5.671737,0.786304,-7.254426,1.624342,5.615813,6.779333,8.968032,-6.338107,2.967032,-3.296885,-0.683980,-2.150151,0.518675,-6.200112,-2.756525,-1.369002,-7.934415,-5.379268,-3.596242,1.928634,0.277906,-1.403396,2.320602,-9.775783,-1.775216,-0.412800,-4.624165,9.665819,4.083006,4.909399,0.241416,-5.819165,-7.745681,-7.319941,-6.113648,-7.284873,-2.810847,-1.985076,2.753238,-8.911100,1.323372,-6.161640,4.660591,-4.097233,6.336041,3.845423,6.681856,1.798871,-4.398599,-9.095756,1.514877,-7.638285,7.442990,2.863925,7.235816,-3.430086,-0.486259,-6.020123,-2.177514,-7.852394,9.465572,-5.538392,0.246438,-0.942830,0.937898,-0.183821,1.309116,-9.033743,2.214122,3.838698,-9.738109,-4.395305,-0.202623,-0.517886,2.424469,1.909493,-9.330164,5.053822,9.020804,3.887425,-1.509010,6.619904,-6.982909,-4.541715,2.847521,6.713508,2.368299,4.444012,-6.666764,-7.756537,-8.191761,-2.759246,-4.827832,7.013046,5.947607,-3.418971,-3.733883,3.671770,-4.599359,3.017571,2.485223,4.638367,-9.045888,9.359044,-6.756804,-8.954589,7.722095,-8.398279,-5.884548,5.265113,-2.292518,0.990614,5.910460,-5.925612,-9.204123,4.415599,-5.834747,-9.244390,7.267024,2.960897,3.196964,7.320975,3.845187,-1.415144,5.506396,9.728317,-4.124288,-0.163753,-5.933055,9.830043,-0.422569,-8.320826,8.260163,7.076677,-4.204388,-9.192959,-8.292300,-6.422736,3.952237,2.851623,-4.203154,9.974279,2.592586,-9.502687,-8.923884,-0.693893,9.568699,0.273339,6.025461,7.019667,8.903414,-7.915522,1.776882,3.437287,5.963843,0.556635,-7.606175,-7.517272,2.046488,0.061755,-5.729078,-2.917578,-1.777634,-6.045699,0.461603,-5.991601,-8.621813,-8.290936,9.048610,-0.341299,9.792031,1.620288,-0.046579,9.806346,-6.044685,2.318829,2.103388,-3.902769,0.413939,3.482671,6.160529,-7.967274,-3.247246,4.409423,-9.056607,0.088125,-6.540698,3.414419,-3.597667,-1.239420,2.539921,-8.667024,1.854437,5.576620,8.571460,1.218263,-3.508074,-0.705251,9.448292,-6.338587,-2.724473,7.319721,-2.470542,3.807627,2.785045,-6.092610,-5.243596,8.229013,8.097456,-4.815746,-8.425243,9.711801,2.660142,8.516672,-6.228866,8.864485,9.407565,6.871966,6.376053,8.571808,-5.493938,-5.502738,-7.783106,-0.439670,-8.812089,-9.480116,3.809901,3.070670,-9.648688,3.510056,-4.901460,7.152512,7.255195,-5.058034,5.215381,2.649804,0.391076,-8.315153,-3.237246,9.250743,-4.168887,3.268833,-0.925584,-8.646149,1.331003,7.033646,-5.324864,-9.036001,6.772831,8.187177,-1.505835,-5.850438,-2.770186,9.492082,8.878722,0.743358,-0.330066,0.301437,6.026964,6.550958,8.161144,-5.436150,1.317481,8.075803,0.581424,-8.769359,-6.750206,9.938992,4.643384,6.734154,-8.111284,-7.705360,7.852807,9.555365,-2.394524,2.996046,8.030246,9.286220,-7.176946,2.949802,7.956409,2.681163,-1.012161,-0.225261,1.155473,-6.476530,-2.113536,4.967321,8.234383,-0.789327,6.061017,3.435252,-8.789502,-0.579113,-1.538065,-4.282198,9.210447,5.673154,9.093225,6.293352,7.740603,-5.454812,6.775232,4.899871,-9.241289,-0.136902,9.774462,-1.789555,-9.345228,8.579487,-3.345731,2.206446,9.697202,2.737154,-2.020955,-6.249384,-0.966820,-7.130050,-4.992884,-8.888473,6.745594,-3.603218,4.181201,-9.746312,1.283666,-2.047253,-8.909611,9.941743,-2.782763,-9.717321,-2.811110,-3.126883,5.774609,-2.881170,-9.895147,-8.623542,5.239131,-2.689790,9.224237,-9.905389,-4.808115,-3.346707,-8.261304,5.663230,-5.676333,-5.900229,-1.838871,8.371843,9.683845,6.668460,4.872902,6.075223,-3.072399,0.625181,4.916616,5.595080,-0.509715,-6.672471,7.822195,2.863301,1.535680,-1.218594,-6.241067,3.143521,4.496248,9.355710,-6.383603,2.969298,-9.244179,-2.474179,1.156580,-1.998377,4.703599,-9.223289,-3.365364,-0.165700,2.476386,6.257946,-0.310507,5.238161,6.964037,-8.223619,-5.332153,-2.233131,-7.457161,-5.607736,-5.768189,9.433952,3.855865,0.126305,4.270896,0.996712,-6.622831,-8.859925,9.942606,9.159339,-7.169439,-9.409856,9.083066,-7.334023,5.634224,2.963052,6.810945,3.479754,9.967977,-9.432980,-9.218914,7.542983,-4.542276,4.052154,-1.582492,-3.571231,5.724979,5.474627,0.422381,-6.234898,-9.184446,1.449920,2.508887,-7.308705,2.917242,0.655865,-1.476340,-5.157190,1.715620,-2.336197,-7.961321,-3.773423,4.283974,1.937481,5.311977,6.420353,8.970478,7.336269,1.673863,7.723694,-4.413091,-6.508852,-8.648065,6.699431,-3.153405,0.144228,-4.489504,-2.311329,9.110979,0.042000,-3.179327,-6.698167,1.820832,-2.505934,2.714827,3.415757,-5.713496,-5.247539,-6.410087,-0.950358,4.953063,-3.523877,-1.614170,4.543714,-4.838341,-2.944522,9.547843,-5.609982,6.209351,9.655452,8.487039,-9.410579,-4.997212,-7.166666,0.059542,8.950094,-7.306195,-8.126710,1.667530,-3.300402,-8.349228,-0.641494,6.149348,-9.673757,6.149868,4.896003,-2.181251,-9.012989,-4.159343,-1.879728,-4.972386,-9.358574,9.134904,0.845118,-8.528158,-1.114078,-2.495478,-1.144028,9.557254,-8.250845,-5.780471,3.917140,-7.659355,2.084929,-1.277948,-5.445928,8.439771,8.627972,1.373601,5.599724,-5.670116,8.593443,-9.035669,-4.480561,-7.417837,-5.021351,-6.482984,-2.849504,-8.441125,3.292932,8.194616,0.415462,-1.207047,2.369202,7.809751,4.705158,-5.256980,-8.836915,-4.991176,-0.756465,-4.465693,9.588415,8.649564,7.594606,3.365393,-7.972569,-6.768844,-4.606776,8.879209,-1.328164,-0.717492,-7.857075,-9.980605,-5.978695,-6.583438,-9.128959,9.823560,3.973281,6.281697,-6.561132,-3.863003,7.267079,-9.046367,8.342232,0.788276,-8.342246,-6.670818,-3.471369,-3.099314,9.126107,8.762774,8.625678,-7.485018,4.993881,5.381300,-0.131489,0.845954,-7.269399,4.175069,2.630547,7.003910,8.081608,-7.120899,7.804608,-7.257784,0.119190,-4.221977,-9.572254,-5.257775,-3.866327,-3.963444,4.059518,-2.182975,7.150804,4.119903,-6.703175,7.668508,-0.913749,6.025967,-4.837068,7.194386,5.834815,-4.857411,-2.705559,-8.338579,-6.094024,6.759154,-4.826750,6.890563,-6.352681,-5.134275,7.597964,-9.155607,7.390003,7.096807,3.912508,-7.548164,-0.702397,-5.804080,7.577040,2.164541,9.368991,3.263630,-1.068103,-8.323050,3.353802,0.218440,-4.988518,4.958692,6.366756,5.463376,4.655726,-2.336888,-3.243664,-9.104840,2.617745,8.950244,-2.178653,-1.866106,1.857278,8.192677,9.933597,3.218229,-4.457565,1.164176,-4.398872,-9.067556,-8.687045,6.586815,-0.959654,-4.125216,-1.897263,-8.493798,-1.984404,0.612053,1.724818,4.852876,-4.981788,-9.839434,9.381647,-3.421817,-9.896239,6.994437,5.253404,3.759257,-4.957722,5.155190,5.931436,4.486830], dtype = "float64")#candidate|5146|(1008,)|const|float64
call_5145 = relay.TupleGetItem(func_3645_call(relay.reshape(const_5146.astype('float64'), [504, 2])), 2)
call_5147 = relay.TupleGetItem(func_3648_call(relay.reshape(const_5146.astype('float64'), [504, 2])), 2)
output = relay.Tuple([call_5129,call_5145,const_5146,])
output2 = relay.Tuple([call_5130,call_5147,const_5146,])
func_5154 = relay.Function([], output)
mod['func_5154'] = func_5154
mod = relay.transform.InferType()(mod)
mutated_mod['func_5154'] = func_5154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5154_call = mutated_mod.get_global_var('func_5154')
call_5155 = func_5154_call()
output = call_5155
func_5156 = relay.Function([], output)
mutated_mod['func_5156'] = func_5156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_5188 = relay.TupleGetItem(func_2816_call(), 0)
call_5189 = relay.TupleGetItem(func_2818_call(), 0)
func_1720_call = mod.get_global_var('func_1720')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_5206 = func_1720_call()
call_5207 = func_1720_call()
output = relay.Tuple([call_5188,call_5206,])
output2 = relay.Tuple([call_5189,call_5207,])
func_5211 = relay.Function([], output)
mod['func_5211'] = func_5211
mod = relay.transform.InferType()(mod)
mutated_mod['func_5211'] = func_5211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mutated_mod.get_global_var('func_5211')
call_5212 = func_5211_call()
output = call_5212
func_5213 = relay.Function([], output)
mutated_mod['func_5213'] = func_5213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4625_call = mod.get_global_var('func_4625')
func_4627_call = mutated_mod.get_global_var('func_4627')
call_5280 = relay.TupleGetItem(func_4625_call(), 0)
call_5281 = relay.TupleGetItem(func_4627_call(), 0)
output = call_5280
output2 = call_5281
func_5295 = relay.Function([], output)
mod['func_5295'] = func_5295
mod = relay.transform.InferType()(mod)
mutated_mod['func_5295'] = func_5295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5295_call = mutated_mod.get_global_var('func_5295')
call_5296 = func_5295_call()
output = call_5296
func_5297 = relay.Function([], output)
mutated_mod['func_5297'] = func_5297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3783_call = mutated_mod.get_global_var('func_3783')
call_5300 = func_3781_call()
call_5301 = func_3781_call()
var_5312 = relay.var("var_5312", dtype = "float64", shape = (9, 5, 8))#candidate|5312|(9, 5, 8)|var|float64
bop_5313 = relay.less(call_5300.astype('bool'), var_5312.astype('bool')) # shape=(9, 5, 8)
bop_5316 = relay.less(call_5301.astype('bool'), var_5312.astype('bool')) # shape=(9, 5, 8)
output = relay.Tuple([bop_5313,])
output2 = relay.Tuple([bop_5316,])
func_5324 = relay.Function([var_5312,], output)
mod['func_5324'] = func_5324
mod = relay.transform.InferType()(mod)
mutated_mod['func_5324'] = func_5324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5325 = relay.var("var_5325", dtype = "float64", shape = (9, 5, 8))#candidate|5325|(9, 5, 8)|var|float64
func_5324_call = mutated_mod.get_global_var('func_5324')
call_5326 = func_5324_call(var_5325)
output = call_5326
func_5327 = relay.Function([var_5325], output)
mutated_mod['func_5327'] = func_5327
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5387 = relay.const([[[5.802597],[-8.352910],[-2.881091],[7.989629],[9.504700],[3.707165],[-8.427241],[-9.818079]],[[2.118327],[7.855660],[7.962309],[8.934013],[0.993814],[-7.784768],[3.935608],[-6.576696]],[[3.400513],[0.519310],[0.676149],[-9.742375],[-8.826351],[-4.644031],[8.368657],[-3.650368]],[[2.065174],[-2.904208],[-3.892824],[-8.039197],[3.994189],[-0.689672],[-4.768437],[-4.066430]],[[9.294327],[0.822972],[-4.859709],[-9.921198],[4.731568],[1.292112],[7.546403],[-5.142551]],[[6.110842],[3.145378],[-0.435174],[3.770400],[3.076201],[-0.635045],[7.069447],[5.337509]],[[3.440328],[9.128768],[-9.128952],[-4.402839],[-7.050725],[-3.191594],[-0.151734],[7.917161]],[[3.832872],[1.499409],[-4.517987],[-8.054581],[-3.627799],[7.289429],[9.800573],[0.196373]],[[4.405502],[-4.857186],[-9.356331],[-7.747119],[-3.200275],[-0.127897],[6.817373],[9.823374]],[[-3.371061],[-5.634739],[3.486258],[-9.595964],[-3.641895],[3.484239],[-3.547752],[-6.866452]],[[-1.831405],[-3.260695],[4.773510],[1.897641],[4.334925],[-1.261303],[6.976421],[-0.771665]]], dtype = "float32")#candidate|5387|(11, 8, 1)|const|float32
uop_5388 = relay.log2(const_5387.astype('float32')) # shape=(11, 8, 1)
output = uop_5388
output2 = uop_5388
func_5390 = relay.Function([], output)
mod['func_5390'] = func_5390
mod = relay.transform.InferType()(mod)
output = func_5390()
func_5391 = relay.Function([], output)
mutated_mod['func_5391'] = func_5391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_5392 = relay.TupleGetItem(func_4147_call(), 0)
call_5393 = relay.TupleGetItem(func_4148_call(), 0)
func_4092_call = mod.get_global_var('func_4092')
func_4096_call = mutated_mod.get_global_var('func_4096')
var_5398 = relay.var("var_5398", dtype = "int8", shape = ())#candidate|5398|()|var|int8
const_5399 = relay.const([-3,-8,-5,9,8,4,3,-5,-7,-10,1,-2,-2,5,-4,-6,5,9,10,7,-5,6,-4,-10,-2,-5,8,5,-4,3,-9,7,2,-3,-6,-2,3,1,-9,-10,3,-1,-5,-2,9,9,4,-1,3,-1,-6,2,-9,7,-5,-8,-4,-1,7,10,-1,-5,4,-3,2,8,7,7,2,-5,-3,-5,-3,-8,4,-10,4,1,-1,-6,10,-3,3,-2,-6,-4,-9,-7,-7,-5,-10,5,-10,3,3,-6,-3,-8,1,-3,-7,5,6,-10,-7,-4,-10,1,5,3,3,-1,-10,-3,10,-5,1,-3,-4,-9,-8,5,10,-7,-10,-5,10,9,6,1,10,-3,8,7,8,10,-9,-5,-3,-5,5,-7,-9,-4,-2,1,3,-10,-7,-10,5,3,8,-2,-2,-5,-9,1,1,-3,2,-3,-5,3,-4,-10,-6,-10,1,-5,-8,-8,-3,5,6,-6,-1,1,-6,9,-9,6,2,-10,-7,-5,-5,4,-4,1,8,-10,10,4,-8,-3,-1,-4,6,-5,-9,10,7,-2,-2,3,-2,-8,4,8,6,-1,-2,-2,-9,3,-9,-1,-6,7,6,9,-3,-10,-10,1,2,3,-6,-4,1,-4,2,-7,8,8,6,-2,4,-9,2,10,-1,10,9,-2,-3,1,2,4,5,-2,7,1,-7,6,10,3,-9,7,-7,8,-5,-3,-10,5,-9,6,2,-7,-10,8,9,1,4,-7,9,9,6,-3,1,4,8,5,-9,-8,-7,1,10,5,-4,-3,8,10,-7,2,2,7,-6,-9,7,8,-6,10,-2,9,7,-10,-5,-9,-3,10,9,-5,-4,-3,-4,4,9,7,1,9,8,-1,10,-5,2,-6,5,-7,-8,9,-1,-1,9,4,-3,-5,4,4,-7,5,-4,-4,4,7,2,-3,9,3,-3,-7,10,7,-10,-6,-2,8,-3,5,4,1,-8,-8,8,4,-6,10,-4,10,10,3,-8,-7,5,-2,4,4,-8,8,2,9,-4,6,8,4,-3,-1,7,-3,10,1,9,-7,-8,4,8,1,-4,1,-4,-1,9,-7,-10,1,8,-7,9,-5,-10,8,4,-1,6,-10,5,7,-1,-2,-7,-2,-5,5,10,1,-10,-9,10,-1,-10,-7,10,10,-10,-4,-5,3,3,4,-7,5,-5,2,-4,2,-3,10,-4,-7,-3,3,-7,-10,4,4,-10,-1,-3,10,7,3,4,-5,4,-5,5,6,4,-2,9,-10,-7,6,5,9,-10,3,-8,4,-4,-8,7,-3,-10,-7,-3,10,9,9,-3,-7,-3,-9,-1,-2,2,-6,-3,-7,-3,4,3,-5,-7,8,5,5,10,-10,4,7,-3,4,1,-9,-6,-2,6,-1,4,-4,-9,-10,10,-9,1,2,-1,9,8,8,-2,4,10,2,-7,2,3,4,-1,2,10,-5,10,5,-4,5,3,-6,5,6,2,9,-9,3,-9,-3,8,-2,-4,8,9,-5,-3,5,9,-1,1,-8,-4,-2,5,1,-5,-4,9,-8,5,1,4,-5,7,-4,5,-1,-7,1,-8,5,-5,-2,-3,3,2,6,-9,-1,-9,7,8,-3,8,-7,6,10,3,8,-10,3,-2,-2,-4,-9,7,-6,-1,10,-5,-8,10,-4,9,8,10,5,-2,7,7,6,-2,-9,-3,4,5,-9,-1,-10,3,-2,-1,9,2,-9,9,-1,10,-4,8,-1,2,-9,-2,-3,-9,10,-10,3,-2,-10,-10,4,2,2,-7,-4,4,-2,-4,-1,-10,5,9,-1,-2,4,6,1,5,10,10,-1,-9,1,7,-10,-3,6,-5,-3,-2,1,4,-5,-7,10,-1,10,-5,-5,2,-1,10,-9,6,4,-8,5,-6,10,7,1,-3,8,-3,-2,6,-2,-1,-3,-2,5,1,1,-2,3,2,-7,-4,-5,-8,1,-8,-2,5,-6,-2,6,-10,-3,9,10,-7,-8,-2,9,8,5,5,7,-3,-7,-1,-8,-2,-3,-6,-4,-2,5,7,-5,4,-3,7,8,-2,-5,-8,3,-6,2,-1,-5,3,8,-4,5,3,8,7,-10,-1,-1,9,-10,2,5,2,-6,-1,-5,7,4,7,2,8,-10,-8,-9,-4,-10,-2,-10,6,-1,10,2,3,9,-8,3,-2,2,-3,7,-1,-6,1,-9,-1,1,-6,9,1,-1,-9,-4,7,-1,8,-10,4,-1,-1,9,3,-3,7,2,10,-6,8,-9,7,-9,-9,-1,6,-7,4,-9,10,-8,4,4,3,-2,-9,10,-5,10,-8,9,2,-1,6,5,-1,-10,3,8,5,9,-5,9,-7,-5,9,-1,4,1,-1,3,-1,7,-8,-2,-7,6,-9,1,5,3,4,6,5,5,4,-9,2,1,-5,10,1,5,2,-5,3,-10,1,4,-3,-3,-8,4,-2,-9,-5,8,-6,7,8,2,10,-10,-6,-7,3,8,6,-9,-8,-5,7,10,-8,-1,10,10,3,-1,4,2,1,9,3,-6,-8,5,-6,-1,1,-3,-3,-3,6,-9,-3,10,-10,-1,-8,-3,10,2,-2,-2,-4,6,-1,6,-4,-8,6,10,6,1,10,10,4,8,6,-1,-9,10,7,-9,-2,7,-4,6,-2,-6,10,4,8,10,-6,-4,9,6,1,8,-2,-1,-3,8,1,10,10,5,-8,1,7,8,1,-5,-9,4,-9,-8,2,-10], dtype = "int8")#candidate|5399|(1024,)|const|int8
var_5400 = relay.var("var_5400", dtype = "uint16", shape = (1430,))#candidate|5400|(1430,)|var|uint16
call_5397 = relay.TupleGetItem(func_4092_call(relay.reshape(var_5398.astype('int8'), []), relay.reshape(const_5399.astype('int8'), [8, 8, 16]), relay.reshape(var_5400.astype('uint16'), [1430,]), ), 0)
call_5401 = relay.TupleGetItem(func_4096_call(relay.reshape(var_5398.astype('int8'), []), relay.reshape(const_5399.astype('int8'), [8, 8, 16]), relay.reshape(var_5400.astype('uint16'), [1430,]), ), 0)
output = relay.Tuple([call_5392,call_5397,var_5398,const_5399,var_5400,])
output2 = relay.Tuple([call_5393,call_5401,var_5398,const_5399,var_5400,])
func_5411 = relay.Function([var_5398,var_5400,], output)
mod['func_5411'] = func_5411
mod = relay.transform.InferType()(mod)
var_5412 = relay.var("var_5412", dtype = "int8", shape = ())#candidate|5412|()|var|int8
var_5413 = relay.var("var_5413", dtype = "uint16", shape = (1430,))#candidate|5413|(1430,)|var|uint16
output = func_5411(var_5412,var_5413,)
func_5414 = relay.Function([var_5412,var_5413,], output)
mutated_mod['func_5414'] = func_5414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2177_call = mod.get_global_var('func_2177')
func_2179_call = mutated_mod.get_global_var('func_2179')
call_5447 = func_2177_call()
call_5448 = func_2177_call()
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_5468 = func_2499_call()
call_5469 = func_2499_call()
output = relay.Tuple([call_5447,call_5468,])
output2 = relay.Tuple([call_5448,call_5469,])
func_5470 = relay.Function([], output)
mod['func_5470'] = func_5470
mod = relay.transform.InferType()(mod)
output = func_5470()
func_5471 = relay.Function([], output)
mutated_mod['func_5471'] = func_5471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2872_call = mutated_mod.get_global_var('func_2872')
call_5532 = relay.TupleGetItem(func_2870_call(), 0)
call_5533 = relay.TupleGetItem(func_2872_call(), 0)
output = call_5532
output2 = call_5533
func_5534 = relay.Function([], output)
mod['func_5534'] = func_5534
mod = relay.transform.InferType()(mod)
mutated_mod['func_5534'] = func_5534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5534_call = mutated_mod.get_global_var('func_5534')
call_5535 = func_5534_call()
output = call_5535
func_5536 = relay.Function([], output)
mutated_mod['func_5536'] = func_5536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4887_call = mod.get_global_var('func_4887')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_5569 = relay.TupleGetItem(func_4887_call(), 0)
call_5570 = relay.TupleGetItem(func_4889_call(), 0)
func_1850_call = mod.get_global_var('func_1850')
func_1851_call = mutated_mod.get_global_var('func_1851')
call_5573 = func_1850_call()
call_5574 = func_1850_call()
func_123_call = mod.get_global_var('func_123')
func_125_call = mutated_mod.get_global_var('func_125')
const_5584 = relay.const([[4.287979],[-0.062689],[-9.769316],[6.783322],[6.837347],[5.682095],[-2.018441],[8.927017],[1.332283],[9.317207],[-2.614061],[4.373842],[-2.152678],[-4.844529],[0.868295],[-6.000427],[-0.351085],[-8.982555],[3.193382],[-9.196566],[7.483403],[-1.762594],[6.717372],[3.771086],[2.837159],[-0.203280],[-1.553568],[1.726856],[-1.643429],[6.808483],[4.383786],[-7.012368],[-0.030597],[-5.580266],[-3.418607],[0.818054],[-0.208996],[5.350784],[5.244551],[-2.072239],[7.862108],[-8.759248],[7.554584],[6.302641],[1.400576],[8.469344],[-0.613966],[-8.322115],[9.811719],[-3.398986],[-7.972756],[0.362337],[-4.657826],[-4.146793],[5.378010],[-6.921361],[-9.255616],[0.921810],[-0.784226],[5.127395],[3.075327],[-9.966944],[0.236237],[9.889921],[2.833557],[-0.239186],[6.125278],[-0.892131],[5.639482],[6.534140],[2.156256],[2.208695],[-2.804864],[2.802922],[6.738322],[7.916037],[-7.559329],[5.018966],[-2.918940],[-2.940349],[-0.561413],[1.042946],[-4.024454],[8.087040],[0.777346],[2.023070],[-8.637334],[-0.574342],[8.003901],[0.172143],[-6.096376],[2.892354],[-6.916584],[-8.461588],[6.022440],[-3.291680],[-6.719756],[6.989002],[1.995832],[-4.516986],[1.985818],[-5.990469],[-1.917538],[6.541024],[-3.034931],[4.500450],[5.349835],[7.149085],[6.103497],[-7.860436],[-8.619804],[-0.221179],[1.326481],[-5.529006],[7.114365],[4.652725],[-9.235659],[-1.545736],[-1.172653],[-3.642608],[1.787224],[2.783149],[-1.814322],[-4.799694],[2.776585],[8.380324],[-6.795733],[-3.378559],[2.865013],[-2.743037],[2.262236],[-3.575941],[8.956050],[-8.415412],[-4.348233],[5.039835],[-6.177905],[-1.212531],[1.229146],[-5.756794],[2.471791],[7.358811],[-3.392662],[7.730780],[-1.441531],[-0.974794],[5.011285],[7.998491],[0.487873],[-5.859356],[-3.973796],[3.330256],[3.514889],[6.708163],[8.378420],[9.116272],[3.242898],[-9.901755],[-8.406190],[-8.650863],[6.508994],[-4.199445],[1.400728],[-1.939404],[0.648222],[-5.822639],[-5.081956],[6.303149],[6.188207],[-9.472456],[-4.381233],[4.965316],[-2.223739],[7.171017],[-6.444568],[9.136400],[-8.897211],[-8.028573],[9.840231],[0.404666],[-9.511537],[-1.551341],[3.202476],[-4.741414],[5.075098],[1.057667],[-5.730280],[6.476367],[-9.411708],[5.087203],[-7.067157],[4.648622],[-0.321415],[-2.061872],[-5.568769],[-3.799549],[6.313849],[8.695812],[-7.459267],[0.336074],[-1.827668],[-0.943552],[-8.429201],[-2.752356],[-5.366781],[8.623375],[-3.009143],[-3.957772],[-2.799643],[4.854167],[-9.892434],[5.532262],[-2.711440],[-3.418903],[-0.405265],[-6.905853],[1.835893],[8.094317],[2.464668],[-6.929496],[1.481392],[-9.987157],[-6.647818],[-5.350325],[-5.206795],[8.998294],[-0.899353],[-8.078840],[1.694652],[6.988573],[3.449328],[7.531697],[-7.216882],[-2.481722],[-4.409148],[-7.705603],[-7.498829],[0.400642],[3.687156],[0.299338],[0.176634],[-6.805098],[-6.940642],[7.077260],[9.708968],[0.458975],[-4.978865],[9.992528],[-4.104665],[-4.912397],[7.527856],[-6.271275],[-3.361192],[-5.074209],[-4.704646],[7.727775],[9.869782],[1.506525],[-4.125612],[2.781796],[7.691526],[-9.267823],[5.193822],[4.810995],[0.553678],[-0.909186],[-5.935001],[-2.048653],[5.067480],[-5.924288],[4.692726],[5.274696],[1.516995],[-4.587438],[1.408313],[9.769773],[-9.914861],[2.883013],[-5.374082],[8.734725],[-5.892968],[-4.897298],[7.392649],[5.458787],[5.035765],[-3.088725],[1.419213],[6.477155],[-6.610275],[8.438596],[-8.725162],[-4.429091],[-2.945955],[-5.416785],[-9.960325],[2.958593],[-5.890814],[3.605719],[-7.156489],[-3.333639],[-8.930801],[-7.563248],[-0.129474],[-6.190653],[5.571059],[3.046452],[8.361750],[8.068637],[4.293247],[-4.969949],[8.465727],[-3.537437],[9.438096],[4.177848],[1.374621],[9.927708],[-7.362675],[7.263432],[-4.609780],[3.923321],[6.221641],[4.191069],[6.171669],[8.808158],[-9.995059],[-9.358167],[0.682383],[2.757894],[0.229614],[-0.361712],[-1.057973],[-7.603325],[-4.607738],[-1.529810],[-8.680334],[-8.259371]], dtype = "float64")#candidate|5584|(336, 1)|const|float64
call_5583 = func_123_call(relay.reshape(const_5584.astype('float64'), [14, 2, 12]))
call_5585 = func_123_call(relay.reshape(const_5584.astype('float64'), [14, 2, 12]))
func_4217_call = mod.get_global_var('func_4217')
func_4219_call = mutated_mod.get_global_var('func_4219')
var_5591 = relay.var("var_5591", dtype = "float64", shape = (1008,))#candidate|5591|(1008,)|var|float64
call_5590 = relay.TupleGetItem(func_4217_call(relay.reshape(var_5591.astype('float64'), [9, 14, 8])), 2)
call_5592 = relay.TupleGetItem(func_4219_call(relay.reshape(var_5591.astype('float64'), [9, 14, 8])), 2)
func_1112_call = mod.get_global_var('func_1112')
func_1115_call = mutated_mod.get_global_var('func_1115')
var_5618 = relay.var("var_5618", dtype = "float32", shape = (50,))#candidate|5618|(50,)|var|float32
const_5619 = relay.const([[-8.283127,-8.325440,-8.925181,-1.273467,3.391074,1.896154,-8.516229,9.375760,4.234053,2.516656,2.599683,7.892074,8.024974,-7.444278,4.571188,-5.519747,3.587392,-2.211094,-4.902052,9.938002,-5.360323,-2.147507,6.775074,-1.499745,-2.832543,-2.729039,2.108931,9.683226,3.912944,-1.991656,0.335823,-4.791162,1.136289,-7.152771,9.993755,2.651606,2.766565,4.234341,-4.335987,7.672720,8.731602,-3.383117,7.332968,6.098722,5.685659,6.112869,9.991657,5.691705,-8.731559,-1.059333,-9.690823,2.297718,-4.417640,-0.887999,2.669645,2.617654,3.108801,9.063763,0.684585,3.182844,3.899973,4.973230,-3.646605,6.675792,2.389543,2.011648,-2.128205,3.140709,1.751737,3.761655,1.254268,5.307743,-4.479059,1.903036,9.937858,-5.012276,3.102341,0.305238,8.589079,0.317313,3.995901,-7.751371,8.208902,-2.653675,7.024531,6.629930,-6.002931,2.195447,-5.015400,1.078776,-2.282931,-0.006417,5.244229,2.370870,-8.324742,1.628369,8.587688,5.392195,4.684829,6.700920,8.148252,2.126277,8.109008,-9.673491,9.139143,-8.506637,-3.771585,-5.912467,-2.671129,-6.775518,-3.393534,-7.169616,3.552254,-4.180314,4.301191,3.641837,8.225761,2.858246,1.550706,-1.704586,2.846787,-1.909306,4.972838,4.474042,3.229183,-0.764224,-5.463682,4.164304,5.858887,-5.842944,-8.549808,1.064623,5.346337,-1.222938,7.797682,0.030300,7.495404,-9.288040,-0.287231,0.408131,6.385880,2.918708,-2.836778,0.837933,5.277376,7.657385,0.515951,8.034393,8.328415,4.805623,-7.033113,2.816197,9.279861,-4.621066,8.605295,9.612011,0.539698,-8.137872,7.710608,4.049466,-5.147080,-1.300084,-9.138694,-8.750357,-4.366237,-2.676577,-9.654587,-1.655479,2.128177,-6.035184,-4.513187,7.095088,-2.447193,-9.684532,6.410850,-4.339474,-2.101686,5.132586,-3.744405,-0.603821,9.146183,4.713276,-5.700711,7.366903,-2.287282,-4.334400,2.186502,5.238604,-9.048633,-0.318104,7.893709,0.527896,4.046041,-9.722611,-3.680954,-7.575446,0.045759,6.623850,-2.781355,3.079514]], dtype = "float32")#candidate|5619|(1, 200)|const|float32
call_5617 = func_1112_call(relay.reshape(var_5618.astype('float32'), [5, 1, 10]), relay.reshape(const_5619.astype('float32'), [5, 4, 10]), )
call_5620 = func_1112_call(relay.reshape(var_5618.astype('float32'), [5, 1, 10]), relay.reshape(const_5619.astype('float32'), [5, 4, 10]), )
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_5621 = relay.TupleGetItem(func_3542_call(), 0)
call_5622 = relay.TupleGetItem(func_3544_call(), 0)
output = relay.Tuple([call_5569,call_5573,call_5583,const_5584,call_5590,var_5591,call_5617,var_5618,const_5619,call_5621,])
output2 = relay.Tuple([call_5570,call_5574,call_5585,const_5584,call_5592,var_5591,call_5620,var_5618,const_5619,call_5622,])
func_5626 = relay.Function([var_5591,var_5618,], output)
mod['func_5626'] = func_5626
mod = relay.transform.InferType()(mod)
var_5627 = relay.var("var_5627", dtype = "float64", shape = (1008,))#candidate|5627|(1008,)|var|float64
var_5628 = relay.var("var_5628", dtype = "float32", shape = (50,))#candidate|5628|(50,)|var|float32
output = func_5626(var_5627,var_5628,)
func_5629 = relay.Function([var_5627,var_5628,], output)
mutated_mod['func_5629'] = func_5629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1486_call = mod.get_global_var('func_1486')
func_1488_call = mutated_mod.get_global_var('func_1488')
call_5634 = relay.TupleGetItem(func_1486_call(), 2)
call_5635 = relay.TupleGetItem(func_1488_call(), 2)
func_5470_call = mod.get_global_var('func_5470')
func_5471_call = mutated_mod.get_global_var('func_5471')
call_5636 = relay.TupleGetItem(func_5470_call(), 1)
call_5637 = relay.TupleGetItem(func_5471_call(), 1)
bop_5643 = relay.greater(call_5634.astype('bool'), relay.reshape(call_5636.astype('bool'), relay.shape_of(call_5634))) # shape=(9, 1, 8)
bop_5646 = relay.greater(call_5635.astype('bool'), relay.reshape(call_5637.astype('bool'), relay.shape_of(call_5635))) # shape=(9, 1, 8)
output = bop_5643
output2 = bop_5646
func_5648 = relay.Function([], output)
mod['func_5648'] = func_5648
mod = relay.transform.InferType()(mod)
output = func_5648()
func_5649 = relay.Function([], output)
mutated_mod['func_5649'] = func_5649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2713_call = mod.get_global_var('func_2713')
func_2714_call = mutated_mod.get_global_var('func_2714')
call_5662 = relay.TupleGetItem(func_2713_call(), 0)
call_5663 = relay.TupleGetItem(func_2714_call(), 0)
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
func_3107_call = mod.get_global_var('func_3107')
func_3108_call = mutated_mod.get_global_var('func_3108')
call_5688 = relay.TupleGetItem(func_3107_call(), 1)
call_5689 = relay.TupleGetItem(func_3108_call(), 1)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_5690 = relay.TupleGetItem(func_1745_call(), 0)
call_5691 = relay.TupleGetItem(func_1746_call(), 0)
output = relay.Tuple([call_5688,call_5690,])
output2 = relay.Tuple([call_5689,call_5691,])
func_5706 = relay.Function([], output)
mod['func_5706'] = func_5706
mod = relay.transform.InferType()(mod)
mutated_mod['func_5706'] = func_5706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5706_call = mutated_mod.get_global_var('func_5706')
call_5707 = func_5706_call()
output = call_5707
func_5708 = relay.Function([], output)
mutated_mod['func_5708'] = func_5708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5767 = relay.var("var_5767", dtype = "uint16", shape = (1, 3, 6))#candidate|5767|(1, 3, 6)|var|uint16
const_5768 = relay.const([[[2,2,8,8,-2,-8],[8,6,-9,9,8,-9],[8,10,4,-7,5,-6]],[[-1,10,9,-8,10,-5],[2,-6,-5,7,-4,5],[-9,4,-4,-5,-7,6]],[[-5,-2,-8,-7,-10,1],[7,-1,4,-8,-10,9],[5,7,-10,-7,-9,1]],[[8,8,-10,-3,8,9],[10,7,10,-2,-1,-6],[-5,-8,-1,-2,7,-5]],[[10,6,-2,9,2,1],[-3,6,3,-5,-2,1],[-1,2,-4,9,-7,-3]],[[9,10,-10,-5,4,-9],[3,5,8,-9,-10,9],[10,-7,4,-7,-2,6]]], dtype = "uint16")#candidate|5768|(6, 3, 6)|const|uint16
bop_5769 = relay.greater(var_5767.astype('bool'), const_5768.astype('bool')) # shape=(6, 3, 6)
func_1015_call = mod.get_global_var('func_1015')
func_1018_call = mutated_mod.get_global_var('func_1018')
const_5777 = relay.const([4,-3,-7,8,6,3,-4,-10,-4,-8,-2,-1,6,3,1,-7,7,6,1,-3,-9,-10,3,-6,6,6,-4,4,-3,6,-9,1,-3,4,-10,-10,5,3,-2,5,-4,8,9,10,1,6,-10,-7,-3,-8,8,-1,8,1,3,-9,-10,-9,-1,1,-6,9,5,9,-7,-10,-5,-9,4,-4,-9,-6,-10,-8,-3,-2,-7,2,-8,-1,-8,-1,-1,-5,-2,10,3,-10,10,-3,-6,-1,-5,6,-4,10,7,6,-2,1,-1,7,8,7,5,2,-5,6,-5,-3,1,-2,5,-6,-10,-4,9,-3,9,8,9,7,2,6,-8,-8,-4,-7,10,-9,2,1,5,2,-5,-9,-10,-10,10,2,7,-6,4,-2,-9,-5,4,-4,-10,-2,7,-9,6,3,-7,5,-7,-7,-6,-5,9,8,4,2,-10,-8,4,8,-9,7,6,-10,-4,-1,-7,7,-6,9,9,-5,6,8,5,9,6,9,-9,-4,7,3,-4,2,-5,2,-4,3,-2,-7,6,10,3,2,10,5,1,-3,-8,5,-6,7,3,10,-8,4,-5,4,6,4,-1,-7,-8,-9,5,-10,-10,3,-7,-3,-9,7,-3,-6,8,-9], dtype = "int32")#candidate|5777|(234,)|const|int32
call_5776 = relay.TupleGetItem(func_1015_call(relay.reshape(const_5777.astype('int32'), [13, 3, 6]), relay.reshape(const_5777.astype('int32'), [13, 3, 6]), ), 0)
call_5778 = relay.TupleGetItem(func_1018_call(relay.reshape(const_5777.astype('int32'), [13, 3, 6]), relay.reshape(const_5777.astype('int32'), [13, 3, 6]), ), 0)
var_5782 = relay.var("var_5782", dtype = "int32", shape = (234,))#candidate|5782|(234,)|var|int32
bop_5783 = relay.greater_equal(const_5777.astype('bool'), relay.reshape(var_5782.astype('bool'), relay.shape_of(const_5777))) # shape=(234,)
output = relay.Tuple([bop_5769,call_5776,bop_5783,])
output2 = relay.Tuple([bop_5769,call_5778,bop_5783,])
func_5789 = relay.Function([var_5767,var_5782,], output)
mod['func_5789'] = func_5789
mod = relay.transform.InferType()(mod)
var_5790 = relay.var("var_5790", dtype = "uint16", shape = (1, 3, 6))#candidate|5790|(1, 3, 6)|var|uint16
var_5791 = relay.var("var_5791", dtype = "int32", shape = (234,))#candidate|5791|(234,)|var|int32
output = func_5789(var_5790,var_5791,)
func_5792 = relay.Function([var_5790,var_5791,], output)
mutated_mod['func_5792'] = func_5792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4625_call = mod.get_global_var('func_4625')
func_4627_call = mutated_mod.get_global_var('func_4627')
call_5803 = relay.TupleGetItem(func_4625_call(), 0)
call_5804 = relay.TupleGetItem(func_4627_call(), 0)
output = call_5803
output2 = call_5804
func_5807 = relay.Function([], output)
mod['func_5807'] = func_5807
mod = relay.transform.InferType()(mod)
mutated_mod['func_5807'] = func_5807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mutated_mod.get_global_var('func_5807')
call_5808 = func_5807_call()
output = call_5808
func_5809 = relay.Function([], output)
mutated_mod['func_5809'] = func_5809
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5154_call = mod.get_global_var('func_5154')
func_5156_call = mutated_mod.get_global_var('func_5156')
call_5814 = relay.TupleGetItem(func_5154_call(), 1)
call_5815 = relay.TupleGetItem(func_5156_call(), 1)
uop_5818 = relay.exp(call_5814.astype('float64')) # shape=(504, 2)
uop_5820 = relay.exp(call_5815.astype('float64')) # shape=(504, 2)
func_1999_call = mod.get_global_var('func_1999')
func_2002_call = mutated_mod.get_global_var('func_2002')
const_5827 = relay.const([-1.303366,-6.956870,7.272678,6.974124,8.918086,-9.027776,-7.880317,-4.532699,-4.927830,-5.465295,-4.867884,-0.610543,9.125805,-8.080040,-0.896702,0.909330,-2.666059,-7.719039,5.087357,5.858681,-4.645493,-9.441997,-4.235076,-1.590945,-6.307036,-6.700781,-6.798696,9.361578,-3.349924,6.708419,-1.304151,1.475583,-3.507448,-0.763487,-5.883047,7.495041,5.608510,5.102012,-2.761388,-5.304498,-3.569458,4.411561,8.017295,-6.607295,-9.560219,4.556140,-8.325420,0.616683,-4.663105,-3.921828,1.318189,3.863935,8.908063,-2.507534,-1.128960,8.493888,-7.417099,-7.576160,6.951741,0.722433,-7.668161,-7.066084,0.772610,5.374861,4.494308,-6.373314,2.088081,9.854628,6.250466,-2.928862,-1.321573,-2.787385,4.110392,-8.777558,-0.279359,-3.842491,-3.258795,5.030683,9.291961,1.857471,8.067956,1.825012,-1.672478,0.812883,2.113847,7.030465,8.777681,-8.414027,-3.126337,6.681583,-3.465720,2.035212,-4.682294,-9.179215,-5.574913,-1.871225,-8.731201,-2.347111,-4.046724,-0.862127,-2.622683,6.270141,7.270716,-2.084318,4.699265,-8.361617,9.174694,-9.691143,9.806531,4.481547,3.466820,6.604499,-8.075890,-5.579217,0.875996,-4.658250,-8.694446,-2.551384,2.715260,-6.368280,-2.793918,-9.978854,-4.288504,-7.251886,3.483843,0.452864,9.660842,-2.281363,3.936412,0.993740,3.835400,-6.730541,7.743764,-3.529579,4.740300,3.278349,1.434789,7.370692,1.275079,3.792735,-8.694431,8.930202,5.743216,4.748606,-0.306285,-3.049200,-9.207541,1.762444,8.487566,-3.638839,-2.989456,-2.163604,0.254557,-2.006517,8.375619,8.173277,-4.538199,-5.549580,9.069301,-4.106939,-6.134246,8.239574,9.805694,-7.579436,-7.510835,2.522632,1.313427,8.856989,-8.999121,9.985219,6.096810,5.561854,7.427458,-2.264976,7.897480,-3.487699,2.318303,-6.753685,-2.743075,4.580339,1.788600,-2.434859,-9.046703,4.091961,1.414604,8.309248,0.275821,-2.323813,-8.069922,7.106696,-3.764178,8.044224,-7.120062,-5.915820,-1.261751,5.800256,3.775556,-0.948885,4.891548,-8.846897,-1.254139,-5.845574,-4.832679,-5.556784,1.215153,-1.534460,3.556845,4.883057,7.239162,6.732881,4.270004,4.152372,-2.113048,-1.042551,8.518881,-9.355782,-8.566562,7.184183,1.094759,1.707217,-8.523203,-3.980465,4.281285,3.308846,-9.869140,8.642036,2.271570,-4.213765,-6.890723,-1.663075,2.401767,-7.175662,1.123527,-0.612597,5.162040,4.313064,0.898742,-4.519353,1.045040,4.161179,-5.603667,8.412344,6.846556,6.411455,-7.577830,6.683936,-8.210471,-1.167304,6.543653,-4.486425,-6.894915,-6.387997,-2.100824,4.424815,-9.596358,9.355491,8.850122,2.938723,-9.997741,-1.690590,-4.555183,-5.350559,7.842780,-7.881735,4.695087,-5.234874,-1.724222,0.554272,5.757648,-3.381877,4.317046,-7.902062,-6.413694,2.587720,-5.741294,3.914321,0.586036,2.659650,-0.298295,5.612709,-7.904953,-8.043339,7.562452,1.218621,-5.741195,-4.972273,9.343298,-5.043705,-5.853251,-7.953591,6.761494,3.788338,8.153605,-2.518115,-7.487833,9.178043,1.373444,7.477134,7.814200,7.888233,-3.920253,4.062729,-8.456640,9.432978,1.132654,9.857991,-6.680394,3.777942,7.461234,7.981625,-7.201075,-0.672479,-6.044117,-8.215960,9.010536,2.469044,2.854312,4.782281,-2.944956,8.721747,8.075128,1.052871,2.747105,4.969751,-3.834428,3.481001,-0.443177,-6.241507,1.501344,-7.574034,-4.707920,5.973009,1.922278,8.291694,0.825855,3.447194,1.479041,-5.407921,-2.877105,8.661622,0.234087,1.542451,-1.467835,-2.414754,-6.753812,-2.731870,6.802047,-9.067955,4.516187,-2.808873,-7.247287,3.979820,-9.175228,2.667246,3.143508,9.615590,2.111996,-8.071994,-1.582641,1.353836,-0.182612,5.124945,3.280934,-9.932467,4.901261,-0.973906,-4.578467,2.164695,6.614785,1.427699,9.878381,4.934769,4.599371,4.970520,7.426359,-3.320718,-3.723938,3.765220,-1.803172,-4.484188,-1.683376,3.818413,-6.290751,-0.638316,2.852029,0.277868,-0.931979,1.685795,-7.390122,-9.171993,-3.481885,5.564714,-6.034708,-3.937273,-3.302520,1.063046,4.992045,-9.152770,2.529885,-3.258389,-4.051677,-9.169746,-0.541499,2.724010,-3.882042,-1.032426,-4.450429,9.676826,-1.883298,6.554664,6.224626,-0.422773,-0.588093,-1.690302,6.596590,-6.264443,-3.554409,-2.859467,5.944300,-5.974589,6.334872,-5.750377,-0.807157,8.897117,6.746380,-7.061070,4.015413,-0.734042,9.379519,6.234040,3.453044,-3.907533,-2.782925,-6.815199,-2.739121,6.620195,-0.368777,-0.396056,-7.511820,0.359264,-9.803006,-1.672464,-2.188040,5.479287,4.014116,-3.073175,4.209746,8.673816,-1.682792,9.623526,-5.615445,-2.465074,-4.812481,6.498560,-2.179050,-1.566896,-5.939723,-5.086171,3.878408,-7.680998,1.816342,0.782794,-8.315541,-3.991249,4.483302,2.834150,5.503529,-2.816917,-8.221894,-9.622778,-8.842138,-1.944710,9.916133,-8.747441,-2.792563,0.800529,8.913587,-3.920572,5.910950,-6.279272,-7.882641,-7.211875,-5.462195,9.240213,6.586673,7.556040,7.392763,-2.657477,2.236437,9.936968,-1.268342,0.718826,-7.848942,9.645750,-7.610331,-7.924687,9.690807,-6.861549,9.067861,5.790871,8.913335,-8.794111,-1.702094,6.489971], dtype = "float64")#candidate|5827|(504,)|const|float64
call_5826 = relay.TupleGetItem(func_1999_call(relay.reshape(const_5827.astype('float64'), [9, 7, 8])), 0)
call_5828 = relay.TupleGetItem(func_2002_call(relay.reshape(const_5827.astype('float64'), [9, 7, 8])), 0)
func_4887_call = mod.get_global_var('func_4887')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_5830 = relay.TupleGetItem(func_4887_call(), 0)
call_5831 = relay.TupleGetItem(func_4889_call(), 0)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_5860 = relay.TupleGetItem(func_3183_call(), 0)
call_5861 = relay.TupleGetItem(func_3184_call(), 0)
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
const_5872 = relay.const(-9, dtype = "uint8")#candidate|5872|()|const|uint8
call_5871 = func_530_call(relay.reshape(const_5872.astype('uint8'), []))
call_5873 = func_530_call(relay.reshape(const_5872.astype('uint8'), []))
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
call_5887 = func_530_call(relay.reshape(const_5872.astype('uint8'), []))
call_5888 = func_530_call(relay.reshape(const_5872.astype('uint8'), []))
output = relay.Tuple([uop_5818,call_5826,const_5827,call_5830,call_5860,call_5871,const_5872,call_5887,])
output2 = relay.Tuple([uop_5820,call_5828,const_5827,call_5831,call_5861,call_5873,const_5872,call_5888,])
func_5898 = relay.Function([], output)
mod['func_5898'] = func_5898
mod = relay.transform.InferType()(mod)
output = func_5898()
func_5899 = relay.Function([], output)
mutated_mod['func_5899'] = func_5899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_6014 = relay.TupleGetItem(func_4147_call(), 1)
call_6015 = relay.TupleGetItem(func_4148_call(), 1)
func_5390_call = mod.get_global_var('func_5390')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_6016 = func_5390_call()
call_6017 = func_5390_call()
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_6018 = relay.TupleGetItem(func_3542_call(), 0)
call_6019 = relay.TupleGetItem(func_3544_call(), 0)
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_6020 = relay.TupleGetItem(func_2036_call(), 0)
call_6021 = relay.TupleGetItem(func_2038_call(), 0)
func_2987_call = mod.get_global_var('func_2987')
func_2988_call = mutated_mod.get_global_var('func_2988')
call_6026 = func_2987_call()
call_6027 = func_2987_call()
output = relay.Tuple([call_6014,call_6016,call_6018,call_6020,call_6026,])
output2 = relay.Tuple([call_6015,call_6017,call_6019,call_6021,call_6027,])
func_6028 = relay.Function([], output)
mod['func_6028'] = func_6028
mod = relay.transform.InferType()(mod)
output = func_6028()
func_6029 = relay.Function([], output)
mutated_mod['func_6029'] = func_6029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3989_call = mod.get_global_var('func_3989')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_6036 = relay.TupleGetItem(func_3989_call(), 0)
call_6037 = relay.TupleGetItem(func_3991_call(), 0)
output = call_6036
output2 = call_6037
func_6041 = relay.Function([], output)
mod['func_6041'] = func_6041
mod = relay.transform.InferType()(mod)
output = func_6041()
func_6042 = relay.Function([], output)
mutated_mod['func_6042'] = func_6042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mod.get_global_var('func_3524')
func_3526_call = mutated_mod.get_global_var('func_3526')
call_6048 = relay.TupleGetItem(func_3524_call(), 0)
call_6049 = relay.TupleGetItem(func_3526_call(), 0)
output = call_6048
output2 = call_6049
func_6082 = relay.Function([], output)
mod['func_6082'] = func_6082
mod = relay.transform.InferType()(mod)
mutated_mod['func_6082'] = func_6082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6082_call = mutated_mod.get_global_var('func_6082')
call_6083 = func_6082_call()
output = call_6083
func_6084 = relay.Function([], output)
mutated_mod['func_6084'] = func_6084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6193 = relay.var("var_6193", dtype = "float64", shape = (9, 5, 1))#candidate|6193|(9, 5, 1)|var|float64
uop_6194 = relay.atan(var_6193.astype('float64')) # shape=(9, 5, 1)
output = uop_6194
output2 = uop_6194
func_6198 = relay.Function([var_6193,], output)
mod['func_6198'] = func_6198
mod = relay.transform.InferType()(mod)
mutated_mod['func_6198'] = func_6198
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6199 = relay.var("var_6199", dtype = "float64", shape = (9, 5, 1))#candidate|6199|(9, 5, 1)|var|float64
func_6198_call = mutated_mod.get_global_var('func_6198')
call_6200 = func_6198_call(var_6199)
output = call_6200
func_6201 = relay.Function([var_6199], output)
mutated_mod['func_6201'] = func_6201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3713_call = mod.get_global_var('func_3713')
func_3714_call = mutated_mod.get_global_var('func_3714')
call_6213 = relay.TupleGetItem(func_3713_call(), 0)
call_6214 = relay.TupleGetItem(func_3714_call(), 0)
const_6221 = relay.const([[[-2.382519,-4.366825,-2.608657,-1.557452,7.091848,-0.841829,-7.794201,5.400203],[4.545953,3.658123,-0.787195,5.133965,0.890522,1.772591,5.816168,-0.480916],[6.808126,4.409625,5.842902,9.098503,-4.745715,3.895121,5.491503,-2.267935],[-3.549426,-3.869464,6.169143,6.193783,6.591096,2.715701,-0.124889,-7.152275],[-1.483590,8.421957,7.490080,-9.223918,0.698602,3.928505,4.280007,0.911913],[4.279486,-3.258506,-6.818934,-5.676315,-8.953407,-8.501472,1.734888,-7.674600],[6.939659,-1.351271,6.062923,-8.216822,-7.346746,9.539444,9.884117,-5.436117]],[[4.324828,5.226607,-9.298988,8.760842,2.044096,8.806528,-2.576824,-9.995721],[-3.816755,-6.506993,-7.560155,-2.123689,-8.762865,-9.789418,-2.335220,7.116064],[9.932942,9.272457,-5.106782,2.826011,1.822226,-6.864881,-7.658879,1.285849],[6.566998,-8.242727,-3.977449,4.582620,4.686367,-9.963629,-9.209792,8.568393],[-0.282691,7.241940,0.550934,-5.193132,-6.657106,-8.770239,2.934563,9.279483],[4.924917,-0.168749,-7.582894,3.976122,1.532665,9.519876,5.460565,-3.464968],[-4.081697,-5.168399,-7.171335,-4.997827,5.342209,9.355813,-7.993844,-5.690568]],[[4.320917,0.490285,-0.811866,6.747936,-9.261867,6.633707,8.940511,8.048242],[3.081963,2.821126,-3.240348,-0.309004,-2.799315,-0.161483,-5.846576,-0.400714],[-6.686071,1.039564,-9.323853,-9.827352,-0.471906,-7.601692,9.666524,8.619852],[6.769264,-5.433120,-8.621722,-0.431147,0.211360,7.923679,7.349178,7.976387],[8.438499,-2.012687,3.457634,-1.309826,-1.290176,8.044740,-6.363291,-0.284480],[2.877472,9.362511,-2.774751,-4.680375,-7.043349,8.483435,3.880189,4.222495],[-7.998664,3.615657,7.672281,7.704345,-5.977598,6.013939,2.337950,5.567510]],[[2.838929,-1.277638,-7.195822,7.033440,-2.518416,-3.789489,6.904986,-2.536317],[3.478536,1.988807,6.181637,-0.961788,6.001922,-3.971053,3.600116,6.179028],[-0.664162,-4.996348,-3.434755,4.083932,2.397481,-2.983537,-9.353234,-8.289834],[-6.023830,-7.549398,-1.474817,-3.103049,-3.371060,-8.007777,-9.180671,-1.814845],[7.533806,0.490849,-4.811898,-2.731734,-1.373480,-3.496077,3.119770,-5.668385],[-5.488668,7.422170,4.902583,-5.730520,-9.014929,1.821155,-2.197147,6.387764],[5.029283,1.129733,2.813675,6.108502,0.089615,-5.175550,-8.686050,-3.249322]],[[0.429773,1.636690,1.789403,6.704803,-2.568069,-3.986479,-5.230053,-0.195228],[-9.017227,-1.562866,1.899202,8.275466,6.497244,0.150300,-0.806662,1.681154],[3.773941,-8.781059,-4.196549,-8.307116,0.579389,-6.548297,-8.387228,1.404843],[-9.172344,-3.644996,1.952862,-2.504089,-4.411291,-3.645636,-3.388353,-4.606147],[-7.680677,-6.362091,-5.751489,0.818104,-6.435163,-9.088714,-8.782044,2.980050],[4.608018,-8.265976,-9.764891,7.236779,-5.273449,6.324640,0.866729,-2.831290],[5.592716,3.232906,9.689644,0.937663,-4.816640,-9.321175,2.080301,0.348561]],[[8.753826,3.382173,1.579167,-7.999506,-3.795280,-8.825946,-1.051080,0.456225],[5.777568,4.085771,3.329008,-8.881275,-2.315558,-4.699727,8.243898,-7.027845],[9.804788,-3.100051,6.400855,-3.933760,-0.822628,9.072011,0.212724,-1.751681],[7.796388,2.809166,-3.398300,-4.584768,-2.425664,-9.772526,9.183078,-9.875399],[-7.473210,3.264146,-4.809590,9.904159,-6.538025,1.926894,2.294637,-5.096592],[4.994461,8.911560,-6.672956,6.480170,-5.845680,-8.081144,-1.317332,-7.358368],[5.247642,-0.616940,3.058300,-0.069190,1.212967,2.516986,-7.613132,5.370575]],[[2.060832,8.692016,2.938312,-4.840146,4.746299,2.592157,-8.162343,-4.639825],[4.209209,8.693088,9.320837,-4.223599,2.173394,9.919371,1.863254,7.029252],[-0.651202,-1.554492,3.254358,5.714544,1.443330,3.319609,9.382180,9.555258],[-1.566026,8.484225,6.921938,-1.091221,-5.596928,-9.574865,3.532550,-7.106466],[-6.481336,4.650167,-9.660976,-9.636779,1.303472,9.987326,-9.665616,9.545513],[6.512208,-8.521184,-2.316605,2.039336,-4.322060,-3.208879,2.004313,5.224198],[-3.349427,-1.947465,-4.013582,-3.988972,-2.195420,-3.932904,5.364392,1.222895]],[[-7.892237,8.666138,1.412924,4.192305,-9.980399,3.218194,9.159781,3.061958],[7.164728,-2.157468,0.967321,7.537260,-9.579946,-3.548748,4.322600,-4.031823],[2.259864,-3.118389,-1.243018,-9.818504,9.592376,-7.028815,5.750056,-4.098595],[2.577606,-5.731981,-7.486341,-2.648950,2.625766,-4.537839,2.316957,-8.896048],[-9.068991,0.959311,9.386588,6.999117,1.717741,5.395368,4.751269,9.987720],[-7.774376,2.503592,6.250686,3.322338,-4.652898,2.222564,-7.857669,-5.019494],[-2.222830,8.022333,-7.673009,-5.804727,-8.274341,-1.979014,-2.413839,6.433286]],[[4.477753,2.674013,-1.642235,5.703457,-6.854990,-1.489094,-7.191909,1.601432],[-9.524371,-8.872522,8.730235,-9.929082,-2.668435,4.307610,-5.425722,3.753736],[-0.927640,-9.906734,9.038104,2.066645,-9.234247,-8.602608,8.457409,9.056085],[-1.540966,-5.769021,1.324264,-1.688854,6.477435,-9.805540,-5.576577,7.668304],[-3.961560,8.868228,8.143474,1.409701,1.347133,-4.333441,5.096856,-7.479934],[-9.643888,7.681192,-7.055596,2.096849,1.991900,6.566955,-4.391215,-9.229416],[1.862711,-9.517961,3.589558,-1.509090,-5.450504,3.043486,0.304823,2.132079]]], dtype = "float64")#candidate|6221|(9, 7, 8)|const|float64
bop_6222 = relay.floor_mod(call_6213.astype('float32'), const_6221.astype('float32')) # shape=(9, 7, 8)
bop_6225 = relay.floor_mod(call_6214.astype('float32'), const_6221.astype('float32')) # shape=(9, 7, 8)
uop_6226 = relay.erf(call_6213.astype('float32')) # shape=(9, 1, 8)
uop_6228 = relay.erf(call_6214.astype('float32')) # shape=(9, 1, 8)
func_4578_call = mod.get_global_var('func_4578')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_6242 = func_4578_call()
call_6243 = func_4578_call()
output = relay.Tuple([bop_6222,uop_6226,call_6242,])
output2 = relay.Tuple([bop_6225,uop_6228,call_6243,])
func_6246 = relay.Function([], output)
mod['func_6246'] = func_6246
mod = relay.transform.InferType()(mod)
output = func_6246()
func_6247 = relay.Function([], output)
mutated_mod['func_6247'] = func_6247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3989_call = mod.get_global_var('func_3989')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_6262 = relay.TupleGetItem(func_3989_call(), 0)
call_6263 = relay.TupleGetItem(func_3991_call(), 0)
func_5411_call = mod.get_global_var('func_5411')
func_5414_call = mutated_mod.get_global_var('func_5414')
const_6272 = relay.const(-1, dtype = "int8")#candidate|6272|()|const|int8
const_6273 = relay.const([4,3,-6,7,-4,8,3,-2,-8,10,-6,6,7,5,2,9,1,-3,-4,2,3,-5,-1,-5,-1,-2,7,8,-3,-3,4,-10,3,-3,-6,-6,-7,5,7,7,-6,-6,-7,6,-9,5,-10,-10,10,1,-8,-5,5,3,2,1,8,-3,-2,-5,2,6,-6,-7,10,4,-5,3,3,-4,-3,-4,-2,8,-10,7,-4,3,9,-10,-8,-7,5,6,5,2,-7,-10,5,-7,10,4,4,6,7,-2,-10,1,6,-1,1,10,-2,-9,8,-2,7,-4,5,-6,-6,9,-7,9,-10,-6,-8,9,9,-6,3,7,8,-2,-1,-7,-9,3,7,-3,6,7,8,-1,5,3,-9,-7,2,-2,-2,-2,-5,8,6,-10,1,-6,5,-5,7,8,10,5,-5,-7,-5,-9,-1,-4,-8,-1,4,-7,5,1,2,1,3,4,-4,6,-7,2,1,6,10,8,5,5,9,-3,5,3,-10,7,-5,3,-7,-1,-1,-10,4,-9,5,-8,-1,-5,5,-4,2,-8,4,10,-8,-2,10,2,-1,-5,-4,-1,6,-9,4,5,-5,-7,-6,-2,8,5,-7,-3,7,-5,1,-6,-3,-7,10,-7,6,-6,10,7,6,-5,-9,3,6,-7,-5,-3,9,9,3,6,9,2,-4,7,-2,-2,3,-7,5,-6,-10,-3,3,10,-8,-5,-10,6,9,3,10,-2,-3,1,-6,2,-10,-5,-7,-8,3,3,2,7,-5,-3,-8,-9,8,2,-9,-2,-9,1,-3,-10,2,-10,-5,8,-9,-6,-9,-1,4,-3,-8,-3,1,1,-1,-8,6,-9,-7,2,9,-5,4,-5,9,-3,-2,-2,-10,-7,-7,6,-5,6,-2,-9,8,-9,-10,-1,2,-6,2,-5,2,-5,-9,2,-8,5,7,-2,8,7,6,6,4,10,1,-10,9,2,8,9,2,-7,10,4,-1,-5,-9,-2,-5,10,-10,-1,-10,7,8,-4,-2,1,-10,-9,6,-5,4,-9,-4,7,3,-2,-2,9,-7,-10,5,10,-8,4,2,10,-1,-9,2,-8,5,-8,-1,4,-1,6,10,1,4,2,9,3,5,-6,7,1,-5,6,-7,3,-9,-6,-4,6,4,-5,-2,-4,2,5,3,-1,5,4,2,-2,6,-9,-2,-10,3,-1,6,3,3,-5,-3,7,-6,2,10,-8,-9,-7,-3,9,-4,2,-4,-6,-4,5,9,-5,-5,-2,10,-9,8,2,-5,-9,1,-9,-10,-4,-5,-10,-3,9,4,2,3,5,-1,7,9,-5,9,5,-8,-4,10,-9,-10,2,2,-2,-5,-10,-5,2,-3,4,2,3,-8,5,2,-2,2,10,6,-9,-10,-9,6,-1,-2,-2,2,-6,-2,-10,-3,-9,-4,7,1,-5,8,6,-7,2,-1,6,2,6,1,10,-8,-6,-6,-4,-2,-7,-3,4,-9,-1,-3,-4,7,8,-5,1,-7,-6,4,9,-9,6,-9,-5,-7,9,-3,4,4,-9,10,4,7,-2,10,-6,-8,-4,-1,7,5,-7,-10,8,10,-7,-7,10,1,-6,-3,-3,-3,2,-5,-3,7,-9,-8,5,6,2,10,-7,4,-3,6,-2,2,4,-2,-8,-6,8,-3,5,4,3,9,-7,5,-4,6,1,-7,-5,-3,-10,9,-4,2,4,-7,9,8,1,-6,6,8,-1,-4,7,-9,-8,-6,3,-4,-3,-5,-6,-8,8,-1,-7,-4,7,-3,7,1,2,-2,7,-3,8,3,-3,-3,7,7,-5,10,-1,4,7,-7,-5,6,-6,2,-9,8,-6,-4,6,-6,-4,-3,-9,7,4,-5,-3,-1,-1,3,-8,9,1,-8,7,-8,-10,8,-9,7,8,-4,-4,2,-10,3,-3,3,-8,-2,6,-5,-2,6,-9,5,-7,-10,8,6,4,-5,4,4,-10,8,-6,-10,8,-10,-1,4,-7,-8,-6,-10,-4,9,4,1,-10,10,3,-6,10,-10,4,8,2,-6,-10,9,3,1,3,-3,-2,1,-5,-10,3,-5,-8,8,-8,-8,-3,2,7,5,-7,3,3,7,-10,-4,-9,-2,1,6,-6,-10,1,5,5,-8,-10,6,-4,1,1,7,-4,8,-8,-7,-7,1,6,6,6,8,4,9,-6,-9,8,9,-4,-9,1,7,10,-8,4,2,7,-7,-3,-8,-9,-7,5,-10,5,1,3,4,6,2,3,3,3,2,8,-8,-10,-7,3,6,-7,3,-7,-5,-6,-6,-10,-2,10,-2,5,7,-5,4,2,-5,9,8,3,-10,10,-10,4,5,8,-4,5,10,-8,7,4,-10,10,-8,1,3,-5,-4,-7,-5,-8,7,10,3,-2,9,-4,9,-5,8,7,9,-6,-1,4,5,-4,-5,-10,4,3,-7,10,-1,-3,3,10,-1,9,-9,-9,4,7,-10,10,-10,-5,9,1,10,-9,-5,9,5,-2,-8,9,6,3,-6,8,-7,-10,-8,-6,-6,-3,6,-1,-7,-7,5,1,5,-7,-9,4,-10,10,-7,8,3,-6,-3,-2,-1,-9,7,8,-2,-1,-10,6,-1,-7,5,4,7,7,-9,2,7,6,9,-4,-7,-3,3,-6,-8,-3,-6,-10,-6,-3,-5,-5,-6,4,5,8,6,10,3,-4,-8,-3,-5,-9,10,-8,-9,-5,5,10,-1,3,-4,-7,-10,-7,9,5,2,6,8,-7,10,3,3,-7,-4,2,-3,4,-9,2,-2,3,-2,6,-7,-8,2,2,5,-10,10,-10,10,-4,6,8,-4,-9,-1,6,-5,5,-6,-5,-8,3,-8,9,-6,6,1,-7,4,-1,1,3,2,5,6,-2,-6,10,-7,-3,-4,-4,-2,1,-8,-1,10,7,1,-3,-4,9,9,6,-10,2,8,10,8,6,-6,7,10,-9,5,-7,-6,-9,-8,4,3,-4,1,-3,-7,-6,-7,-8,-4,1,8,8,-6,10,1,-6,7,9,3,-8,-2,-5,7,7,10,-1,-8,4,-6,-10,6,3,-5,3,4,-10,4,-7,-1,-2,-4,1,4,6,8,8,3,7,-6,7,10,8,5,6,-10,6,5,-6,1,-10,-7,2,2,7,10,9,3,7,-1,-1,3,-6,5,9,3,6,10,9,7,-9,2,-8,-5,1,10,-8,-1,3,-6,3,-4,9,-9,5,8,5,-3,-5,8,4,-1,-2,9,-10,10,6,4,-7,6,9,7,6,-6,6,-6,-3,5,9,1,-10,-7,-4,-4,4,-2,-5,-8,8,-9,-10,-7,4,-8,-7,-6,-9,-5,-4,5,-8,2,7,2,1,-4,-10,4,4,-1,-3,9,-10,7,3,1,-1,3,-10,-5,-8,-4,9,-4,-1,5,-10,6,-1,3,6,-3,4,7,1,-6,1,9,7,-7,6,10,8,-7,10,-1,1,-5,2,-8,-4,-3,-4,8,-6,8,7,-10,-4,4,-7,2,10,3,-7,-6,7,9,4,1,-10,-3,-8,2,2,-8,2,6,-5,-6,4,-5,-3,-2,-2,10,3,1,-8,3,-10,8,-9,5,-5,-8,3,10,10,5,-5,5,10,-1,-10,8,-3,3,-1,8,7,3,-3,-8,-4,-4,9,9,5,6,2,7,-8,-1,-7,5,7,6,10,3,-6,-3,8,2,1,1,2,3,8,-1,5,1,-5,-1,10,8,-3,-8,-6,4,-8,3,5,-4,-9,10,-10,-5,-9,-9,-2,-2,2,8,2,-3,9,2,3,-6,10,6,6,-6,-10,1,-4,9,-5,-3,-8,-7,4,10,-7], dtype = "uint16")#candidate|6273|(1430,)|const|uint16
call_6271 = relay.TupleGetItem(func_5411_call(relay.reshape(const_6272.astype('int8'), []), relay.reshape(const_6273.astype('uint16'), [1430,]), ), 4)
call_6274 = relay.TupleGetItem(func_5414_call(relay.reshape(const_6272.astype('int8'), []), relay.reshape(const_6273.astype('uint16'), [1430,]), ), 4)
func_3829_call = mod.get_global_var('func_3829')
func_3830_call = mutated_mod.get_global_var('func_3830')
call_6276 = relay.TupleGetItem(func_3829_call(), 0)
call_6277 = relay.TupleGetItem(func_3830_call(), 0)
output = relay.Tuple([call_6262,call_6271,const_6272,const_6273,call_6276,])
output2 = relay.Tuple([call_6263,call_6274,const_6272,const_6273,call_6277,])
func_6286 = relay.Function([], output)
mod['func_6286'] = func_6286
mod = relay.transform.InferType()(mod)
output = func_6286()
func_6287 = relay.Function([], output)
mutated_mod['func_6287'] = func_6287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4887_call = mod.get_global_var('func_4887')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_6324 = relay.TupleGetItem(func_4887_call(), 0)
call_6325 = relay.TupleGetItem(func_4889_call(), 0)
output = call_6324
output2 = call_6325
func_6329 = relay.Function([], output)
mod['func_6329'] = func_6329
mod = relay.transform.InferType()(mod)
mutated_mod['func_6329'] = func_6329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6329_call = mutated_mod.get_global_var('func_6329')
call_6330 = func_6329_call()
output = call_6330
func_6331 = relay.Function([], output)
mutated_mod['func_6331'] = func_6331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_6334 = func_3085_call()
call_6335 = func_3085_call()
func_1323_call = mod.get_global_var('func_1323')
func_1325_call = mutated_mod.get_global_var('func_1325')
call_6336 = func_1323_call()
call_6337 = func_1323_call()
func_5789_call = mod.get_global_var('func_5789')
func_5792_call = mutated_mod.get_global_var('func_5792')
var_6351 = relay.var("var_6351", dtype = "uint16", shape = (18,))#candidate|6351|(18,)|var|uint16
var_6352 = relay.var("var_6352", dtype = "int32", shape = (234,))#candidate|6352|(234,)|var|int32
call_6350 = relay.TupleGetItem(func_5789_call(relay.reshape(var_6351.astype('uint16'), [1, 3, 6]), relay.reshape(var_6352.astype('int32'), [234,]), ), 2)
call_6353 = relay.TupleGetItem(func_5792_call(relay.reshape(var_6351.astype('uint16'), [1, 3, 6]), relay.reshape(var_6352.astype('int32'), [234,]), ), 2)
output = relay.Tuple([call_6334,call_6336,call_6350,var_6351,var_6352,])
output2 = relay.Tuple([call_6335,call_6337,call_6353,var_6351,var_6352,])
func_6364 = relay.Function([var_6351,var_6352,], output)
mod['func_6364'] = func_6364
mod = relay.transform.InferType()(mod)
mutated_mod['func_6364'] = func_6364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6364_call = mutated_mod.get_global_var('func_6364')
var_6366 = relay.var("var_6366", dtype = "uint16", shape = (18,))#candidate|6366|(18,)|var|uint16
var_6367 = relay.var("var_6367", dtype = "int32", shape = (234,))#candidate|6367|(234,)|var|int32
call_6365 = func_6364_call(var_6366,var_6367,)
output = call_6365
func_6368 = relay.Function([var_6366,var_6367,], output)
mutated_mod['func_6368'] = func_6368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6028_call = mod.get_global_var('func_6028')
func_6029_call = mutated_mod.get_global_var('func_6029')
call_6384 = relay.TupleGetItem(func_6028_call(), 1)
call_6385 = relay.TupleGetItem(func_6029_call(), 1)
var_6428 = relay.var("var_6428", dtype = "float32", shape = (11, 8, 8))#candidate|6428|(11, 8, 8)|var|float32
bop_6429 = relay.bitwise_and(call_6384.astype('uint32'), var_6428.astype('uint32')) # shape=(11, 8, 8)
bop_6432 = relay.bitwise_and(call_6385.astype('uint32'), var_6428.astype('uint32')) # shape=(11, 8, 8)
output = bop_6429
output2 = bop_6432
func_6434 = relay.Function([var_6428,], output)
mod['func_6434'] = func_6434
mod = relay.transform.InferType()(mod)
mutated_mod['func_6434'] = func_6434
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6435 = relay.var("var_6435", dtype = "float32", shape = (11, 8, 8))#candidate|6435|(11, 8, 8)|var|float32
func_6434_call = mutated_mod.get_global_var('func_6434')
call_6436 = func_6434_call(var_6435)
output = call_6436
func_6437 = relay.Function([var_6435], output)
mutated_mod['func_6437'] = func_6437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3937_call = mod.get_global_var('func_3937')
func_3938_call = mutated_mod.get_global_var('func_3938')
call_6463 = relay.TupleGetItem(func_3937_call(), 0)
call_6464 = relay.TupleGetItem(func_3938_call(), 0)
output = relay.Tuple([call_6463,])
output2 = relay.Tuple([call_6464,])
func_6490 = relay.Function([], output)
mod['func_6490'] = func_6490
mod = relay.transform.InferType()(mod)
mutated_mod['func_6490'] = func_6490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6490_call = mutated_mod.get_global_var('func_6490')
call_6491 = func_6490_call()
output = call_6491
func_6492 = relay.Function([], output)
mutated_mod['func_6492'] = func_6492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5668_call = mod.get_global_var('func_5668')
func_5670_call = mutated_mod.get_global_var('func_5670')
call_6493 = relay.TupleGetItem(func_5668_call(), 0)
call_6494 = relay.TupleGetItem(func_5670_call(), 0)
output = relay.Tuple([call_6493,])
output2 = relay.Tuple([call_6494,])
func_6497 = relay.Function([], output)
mod['func_6497'] = func_6497
mod = relay.transform.InferType()(mod)
output = func_6497()
func_6498 = relay.Function([], output)
mutated_mod['func_6498'] = func_6498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_6555 = func_5807_call()
call_6556 = func_5807_call()
output = call_6555
output2 = call_6556
func_6563 = relay.Function([], output)
mod['func_6563'] = func_6563
mod = relay.transform.InferType()(mod)
mutated_mod['func_6563'] = func_6563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6563_call = mutated_mod.get_global_var('func_6563')
call_6564 = func_6563_call()
output = call_6564
func_6565 = relay.Function([], output)
mutated_mod['func_6565'] = func_6565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_6572 = func_1251_call()
call_6573 = func_1251_call()
output = relay.Tuple([call_6572,])
output2 = relay.Tuple([call_6573,])
func_6612 = relay.Function([], output)
mod['func_6612'] = func_6612
mod = relay.transform.InferType()(mod)
mutated_mod['func_6612'] = func_6612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6612_call = mutated_mod.get_global_var('func_6612')
call_6613 = func_6612_call()
output = call_6613
func_6614 = relay.Function([], output)
mutated_mod['func_6614'] = func_6614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5534_call = mod.get_global_var('func_5534')
func_5536_call = mutated_mod.get_global_var('func_5536')
call_6632 = func_5534_call()
call_6633 = func_5534_call()
var_6646 = relay.var("var_6646", dtype = "float64", shape = (9, 6, 8))#candidate|6646|(9, 6, 8)|var|float64
bop_6647 = relay.minimum(call_6632.astype('float64'), var_6646.astype('float64')) # shape=(9, 6, 8)
bop_6650 = relay.minimum(call_6633.astype('float64'), var_6646.astype('float64')) # shape=(9, 6, 8)
uop_6656 = relay.log10(var_6646.astype('float64')) # shape=(9, 6, 8)
output = relay.Tuple([bop_6647,uop_6656,])
output2 = relay.Tuple([bop_6650,uop_6656,])
func_6671 = relay.Function([var_6646,], output)
mod['func_6671'] = func_6671
mod = relay.transform.InferType()(mod)
var_6672 = relay.var("var_6672", dtype = "float64", shape = (9, 6, 8))#candidate|6672|(9, 6, 8)|var|float64
output = func_6671(var_6672)
func_6673 = relay.Function([var_6672], output)
mutated_mod['func_6673'] = func_6673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4578_call = mod.get_global_var('func_4578')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_6727 = func_4578_call()
call_6728 = func_4578_call()
uop_6749 = relay.rsqrt(call_6727.astype('float64')) # shape=(9, 9, 8)
uop_6751 = relay.rsqrt(call_6728.astype('float64')) # shape=(9, 9, 8)
uop_6764 = relay.tan(uop_6749.astype('float32')) # shape=(9, 9, 8)
uop_6766 = relay.tan(uop_6751.astype('float32')) # shape=(9, 9, 8)
func_1836_call = mod.get_global_var('func_1836')
func_1838_call = mutated_mod.get_global_var('func_1838')
var_6768 = relay.var("var_6768", dtype = "float64", shape = (1008,))#candidate|6768|(1008,)|var|float64
call_6767 = relay.TupleGetItem(func_1836_call(relay.reshape(var_6768.astype('float64'), [9, 14, 8])), 0)
call_6769 = relay.TupleGetItem(func_1838_call(relay.reshape(var_6768.astype('float64'), [9, 14, 8])), 0)
output = relay.Tuple([uop_6764,call_6767,var_6768,])
output2 = relay.Tuple([uop_6766,call_6769,var_6768,])
func_6771 = relay.Function([var_6768,], output)
mod['func_6771'] = func_6771
mod = relay.transform.InferType()(mod)
var_6772 = relay.var("var_6772", dtype = "float64", shape = (1008,))#candidate|6772|(1008,)|var|float64
output = func_6771(var_6772)
func_6773 = relay.Function([var_6772], output)
mutated_mod['func_6773'] = func_6773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1579_call = mod.get_global_var('func_1579')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_6987 = relay.TupleGetItem(func_1579_call(), 0)
call_6988 = relay.TupleGetItem(func_1580_call(), 0)
func_5626_call = mod.get_global_var('func_5626')
func_5629_call = mutated_mod.get_global_var('func_5629')
const_6996 = relay.const([3.261014,-9.037639,0.222644,0.344051,-1.246646,-2.569468,9.576958,3.637530,-1.973937,6.241252,1.450662,-4.671619,1.905069,-5.666175,7.347219,7.732217,2.325797,5.308415,-6.375371,-4.534363,-7.495692,9.772712,-9.365653,-3.772825,8.570067,-7.481557,7.644235,1.171914,-1.107711,0.927453,2.668962,9.421263,9.197962,1.265157,3.345764,-8.469454,-7.762987,4.505357,-1.188808,2.854114,1.188549,-8.365125,-5.647850,3.737187,4.038824,-9.565508,-6.229977,-2.045985,-1.620676,3.093866,5.088322,2.308892,-9.838875,-6.996671,-6.122285,-7.843961,8.066781,6.880332,-0.846776,6.557801,0.010768,-8.109901,7.110061,8.652670,-5.792721,8.388512,7.882194,8.898406,1.855398,-7.605863,6.908192,3.376183,-6.013633,-6.883552,-2.826441,-9.035971,2.575129,3.255001,5.564864,-2.935348,5.854689,3.146929,-3.101269,-9.666223,0.755327,6.374948,8.179047,3.093898,4.611886,-6.724793,4.677212,-9.803779,2.208506,5.954211,-8.202416,-7.210006,6.484996,-3.661732,-3.995175,5.048831,-0.875527,-3.170612,-1.402705,7.456336,3.468813,5.549779,-2.150927,7.051058,3.445036,2.311563,-4.291255,5.276077,2.070434,8.264078,3.495411,8.555125,-4.739477,0.534772,-0.810118,-2.060420,4.699582,-6.768248,4.230563,8.591843,4.150448,3.363439,9.582244,7.495141,-8.189785,-3.452647,-6.295493,6.490725,-3.835447,5.211229,4.061892,-4.482384,9.938795,9.399456,6.559272,6.141180,4.559899,-7.355606,9.445895,7.358379,1.610845,9.936622,-1.423903,-0.109810,-0.169706,2.223183,4.910009,-8.955405,-1.891692,-6.655437,-7.383492,-5.188300,-5.749340,-3.448009,2.973060,5.213571,-9.030742,-0.399314,-8.233775,5.650831,-2.436072,-4.677715,-3.726802,-5.428827,-1.608609,-0.172499,-9.680271,-7.621638,-5.145501,-6.926090,3.199944,-6.391232,6.010622,-6.210455,2.016463,-5.735974,-0.248302,9.830127,0.751037,8.273669,-0.536760,-1.219074,0.528687,4.964451,-3.609508,2.360875,-8.370788,4.943284,-8.364613,7.429103,5.170780,7.267702,-9.083979,-2.820492,-4.039686,-1.596143,-5.899899,3.932275,1.037474,1.806071,-6.207008,0.637041,-4.856220,-2.510973,-9.516632,-9.618541,2.564916,4.486092,-5.079297,9.303999,-0.970611,-6.853403,2.145267,-0.481609,-3.850969,-3.526470,-6.346888,3.903688,-9.957400,9.578551,2.920785,-7.533623,1.083410,2.205027,4.480712,-6.340264,-3.453540,-2.744583,-3.839587,-9.441009,-0.666912,0.786944,7.510131,6.214217,6.578927,-0.810114,-3.252322,5.563632,4.864849,-3.833895,-6.025257,-1.641845,4.027375,-1.481783,2.429728,-3.363517,6.363840,-7.513452,9.886810,-1.381696,-4.835668,4.610355,9.587370,-6.171713,1.178020,8.250109,1.357272,-1.167352,0.602977,-0.184701,-1.215539,-1.732886,-5.297511,-9.941881,8.491345,-9.460901,2.416419,-5.848218,6.563053,9.358753,4.771769,-9.958822,-4.328089,5.985780,9.231172,-1.905689,7.576371,8.172488,7.313162,4.640594,-5.883503,-5.171653,7.514189,-1.317111,1.632725,-9.628856,-1.886671,9.927670,2.671449,-6.729545,-5.469252,-4.497579,-3.483977,-5.577444,3.924466,-5.756672,2.854860,-2.461086,4.222113,5.628561,-5.613113,-3.085310,-9.394955,-9.680268,-6.400125,-7.859000,7.979453,-6.263320,-0.454443,-4.257966,-2.248998,1.768074,2.418360,8.216488,-3.632233,-5.586167,-8.295284,-7.955089,-1.667327,-0.988597,6.049167,-8.798995,-2.315223,-0.504682,0.331473,-4.301797,6.332665,0.808104,5.724108,-0.131886,-9.314396,6.130934,8.559840,3.726891,-4.974878,-8.971531,6.482335,-4.854126,-1.902935,-5.247279,3.919594,0.432269,2.464115,-6.970537,3.852513,-4.117794,8.860550,-1.715907,0.618517,-0.431529,-8.872239,-8.036189,0.393826,4.659808,7.297379,3.461292,-8.397562,-3.597829,-0.261155,2.495243,7.698572,0.175800,5.796638,5.040136,2.953710,-0.159643,-6.937410,8.353026,4.354256,2.765537,3.871853,-6.311343,-6.189473,2.513763,6.183807,-8.875209,-6.759275,2.856660,-1.719295,6.142227,-4.872061,1.118817,-7.531241,9.061060,1.657845,-0.630853,4.382200,-0.219160,5.174216,-5.107874,-3.906551,3.047179,-9.537156,-7.521178,7.725502,2.707678,2.547913,1.450116,9.384886,-2.114815,7.227987,8.846151,6.074185,-7.228639,7.936792,8.053403,-0.902236,8.403177,1.694878,5.900755,5.961450,-5.481940,2.097777,-3.812352,-7.875935,6.287743,0.323335,4.278857,-3.862694,-0.045479,-6.505568,-6.140384,-5.669261,-8.103076,4.902063,2.255884,-4.197511,-0.944923,1.604462,-8.309009,3.897574,4.655944,6.282500,4.337560,2.489817,7.941080,7.889461,-1.514556,8.606019,7.091152,-4.357450,2.777988,-2.943032,-1.108106,-8.411141,-6.840342,-8.899356,8.603584,-6.275231,5.068267,-1.632185,7.376246,-8.047738,8.555101,-3.167454,4.916693,9.808608,6.291895,-5.015812,1.084226,3.353417,-0.804957,-5.793548,9.818196,-3.304163,-2.594685,9.408750,-8.810303,0.225605,-2.604576,-8.645005,-2.728654,-6.772918,6.018457,6.552800,-8.436318,-5.390912,-9.827034,-6.209560,8.108251,-7.831775,5.146600,-5.782647,-7.071465,1.352154,1.759011,-3.403717,-5.421942,-5.543585,1.629932,-1.039433,-4.267154,-3.953738,0.321298,-2.550885,3.276099,-9.471845,-8.983582,-9.713323,-3.357724,7.833239,0.786107,8.784073,6.465522,3.181845,7.679801,-9.733241,6.178002,-4.787068,0.943483,5.992562,-2.640767,3.226456,-0.485215,9.707560,7.624432,7.718390,-2.639382,-6.990051,-8.896397,-6.784943,-0.883992,3.560852,8.785192,-0.205483,-0.186139,8.158413,-5.850285,8.382967,-8.093236,1.620319,-7.312837,-3.932475,-3.173286,-6.348255,-4.112605,-6.381737,3.081204,-2.856143,-0.948638,7.799947,4.812755,3.564669,4.267436,-2.101074,4.041835,6.732659,-5.497288,-6.581692,2.577564,5.705126,8.451462,-3.700419,9.213475,5.146120,8.694669,-5.262016,8.466927,-4.296893,5.908328,-8.885806,9.249386,-1.613485,5.637487,-9.087972,3.333940,-8.362662,7.317934,9.155631,-9.094477,-3.700775,0.591448,-6.475208,-8.841833,0.711693,8.987001,-3.217148,6.251876,9.165591,9.350283,9.155302,1.188622,8.035358,-7.308209,-7.018507,8.369280,7.370433,1.702089,6.860909,-7.363148,8.293736,-5.997731,-5.721269,-9.270808,-9.339671,7.250760,-2.256302,-0.666050,-6.580237,-3.852257,7.569808,3.683217,-3.819525,-2.347131,8.772454,-3.589795,-7.405183,-9.475970,3.810546,-4.406997,2.723954,3.702205,3.595064,4.926986,4.133472,-5.034793,-8.040049,0.548978,-2.713578,-4.782098,-5.630665,6.760594,-0.628932,-9.346843,-8.980396,7.173554,-4.955759,-7.377650,-6.511004,2.133201,6.138856,-0.448711,-2.604910,1.819745,6.841267,-3.323593,-0.475718,3.657994,1.333204,-6.967416,-7.829064,1.834404,7.787856,-4.643441,-3.353828,8.581153,3.570888,6.976050,7.428516,8.551356,-4.685641,-4.242891,5.646208,9.843379,0.879404,-1.418101,-9.006949,5.105994,7.755591,0.958392,3.322509,-8.005000,3.649939,-0.377225,-8.906028,9.989157,5.995851,8.324642,6.144045,-6.173211,3.949797,9.242830,-9.980208,0.710063,-0.053818,7.808523,4.525582,5.076102,5.067065,5.231167,6.663911,8.021062,-4.823029,5.432135,0.915207,9.357461,-4.651570,-9.975800,5.049105,3.332541,2.294772,3.395267,-1.398284,8.006290,1.745707,5.814247,6.305517,9.466604,4.543255,-6.559899,-8.880878,8.957001,-7.086774,-4.196839,1.722396,2.391816,-8.236865,1.826155,8.930132,4.614503,5.167179,5.173345,4.952710,5.686096,4.584454,0.692723,2.718402,7.330268,3.494105,6.530764,6.424393,9.256104,0.846961,-7.859204,8.970151,2.862496,-6.322187,9.803828,-9.353807,-5.745708,-5.486217,1.027724,3.744913,9.960916,-1.572002,0.182088,-5.487816,-0.165453,-3.464951,-4.671150,-7.329874,-9.149430,6.580654,-3.451171,-9.461386,0.081493,-1.308780,-5.505584,4.018064,-9.312356,-5.641539,1.027028,-0.918700,5.452346,-3.381404,-2.970891,6.562607,5.115181,3.445117,-2.538716,3.277727,-0.820982,9.047283,9.866452,3.999693,-9.426267,2.433523,-6.735506,3.383269,-8.988725,0.149031,-4.303511,-7.320988,1.365894,8.147932,4.618839,-9.387765,4.712807,7.247910,-7.640314,-4.489412,-1.337940,7.978658,-3.180438,-2.177438,-8.038189,0.973027,6.371966,9.665320,7.903609,-0.818086,4.758592,1.190428,-5.270799,2.269626,8.415446,-7.813893,0.167168,-1.610311,-3.107675,2.607389,-8.419649,-8.381908,-0.963388,6.443988,-3.132768,-0.717678,-3.256763,-3.651162,-2.000835,6.612247,-2.918958,-2.278076,6.436550,9.725339,8.277761,5.351765,6.692063,9.622803,2.660952,-8.186063,0.930739,6.417536,-6.551766,-2.381427,8.299804,-0.337317,7.914038,7.897222,4.939939,3.805175,4.509563,-2.021816,-4.349479,-0.373411,-2.676388,9.931692,-1.213187,7.638601,8.787000,9.296931,-6.081333,-4.100011,-8.210949,-4.330448,-1.496123,2.598817,-1.502483,-1.025445,1.903497,-6.293848,8.379818,9.519367,-7.437281,-7.561808,3.498439,-9.222856,0.251468,4.958944,2.486733,3.663780,7.159936,6.496336,2.786558,-1.638052,2.554100,-1.436534,3.744766,-8.745281,9.685213,9.463108,-6.061022,-1.897420,-9.777851,-7.715359,3.116317,2.626557,-0.336338,3.833295,-1.476117,-2.892452,-1.465084,4.473190,8.733070,-0.863471,-5.614198,2.477030,6.563354,9.155490,5.255171,0.671798,6.301722,-9.625294,-3.204319,9.887109,5.956658,-9.105094,4.655624,2.967483,1.265254,1.243928,1.573759,-5.574768,-5.626609,-5.488118,2.364218,-1.519446,-1.659250,-0.928824,-7.364542,-1.296783,-6.993813,-5.027743,-9.408029,-6.905406,4.756428,8.659005,-2.215511,3.338370,0.609163,-6.175941,-0.326448,-8.590119,1.352404,7.637064,-0.050827,-5.673801,-7.698435,-2.336464,-3.503943,-9.992188,-1.969696,6.513039,3.410104,4.254196,-1.100776,-2.905033,5.375945,-6.818830,8.052829,-4.297416,5.870282,-5.651762,5.460169,-1.035775,4.387843,5.485526,-5.833980,-8.803343,-0.740233,8.985225,-6.079550,5.254181,-2.133649,-4.372212,1.719306,7.368584,3.171465,-4.997950,2.806511,4.805745,8.598033,-7.268805,4.835492,6.544954,5.160170,-4.099301,-0.726747,5.350735,2.110841,2.929619,-0.256342,2.610821,-9.421886,7.938446,-9.736218,1.516968,9.401435,-2.960641,-5.738308,-8.014288,-9.169896,8.013103,-1.829488,9.012498,4.312230,-9.507698,6.072274,3.373058,8.106978,6.868604,7.560557,1.705240,4.642117,1.165008,-9.442829,2.510751,0.568297,2.572847,4.319677,1.534815,2.808686,-8.271354,-3.684897], dtype = "float64")#candidate|6996|(1008,)|const|float64
const_6997 = relay.const([9.730415,6.257788,5.855266,-0.299794,-1.316889,-1.990760,7.168558,3.430429,-8.235184,9.606231,5.845564,4.098190,-0.423697,0.565441,-7.278128,-4.441427,-5.107483,-1.116168,-7.649091,-6.154675,0.870416,-9.697729,-9.179169,-6.298924,-2.707409,1.740254,-9.489850,-7.394418,-4.649820,-9.147021,9.189869,-6.428932,-0.021221,5.255126,-4.247250,-9.750415,3.127742,-9.591505,-7.323824,-0.821247,0.742604,-4.230428,-6.191442,-4.282495,-8.941420,2.029535,1.210424,2.587474,9.079396,9.426211], dtype = "float32")#candidate|6997|(50,)|const|float32
call_6995 = relay.TupleGetItem(func_5626_call(relay.reshape(const_6996.astype('float64'), [1008,]), relay.reshape(const_6997.astype('float32'), [50,]), ), 6)
call_6998 = relay.TupleGetItem(func_5629_call(relay.reshape(const_6996.astype('float64'), [1008,]), relay.reshape(const_6997.astype('float32'), [50,]), ), 6)
output = relay.Tuple([call_6987,call_6995,const_6996,const_6997,])
output2 = relay.Tuple([call_6988,call_6998,const_6996,const_6997,])
func_7014 = relay.Function([], output)
mod['func_7014'] = func_7014
mod = relay.transform.InferType()(mod)
output = func_7014()
func_7015 = relay.Function([], output)
mutated_mod['func_7015'] = func_7015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5107_call = mod.get_global_var('func_5107')
func_5109_call = mutated_mod.get_global_var('func_5109')
call_7069 = relay.TupleGetItem(func_5107_call(), 3)
call_7070 = relay.TupleGetItem(func_5109_call(), 3)
output = relay.Tuple([call_7069,])
output2 = relay.Tuple([call_7070,])
func_7087 = relay.Function([], output)
mod['func_7087'] = func_7087
mod = relay.transform.InferType()(mod)
mutated_mod['func_7087'] = func_7087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7087_call = mutated_mod.get_global_var('func_7087')
call_7088 = func_7087_call()
output = call_7088
func_7089 = relay.Function([], output)
mutated_mod['func_7089'] = func_7089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_7139 = relay.TupleGetItem(func_2036_call(), 0)
call_7140 = relay.TupleGetItem(func_2038_call(), 0)
func_4092_call = mod.get_global_var('func_4092')
func_4096_call = mutated_mod.get_global_var('func_4096')
const_7164 = relay.const(-10, dtype = "int8")#candidate|7164|()|const|int8
const_7165 = relay.const([[2,7],[-10,10],[1,2],[7,-7],[-5,-6],[-10,2],[-9,-8],[-4,-1],[4,-8],[6,10],[1,3],[-6,-1],[-5,-7],[-3,2],[2,6],[-8,-4],[7,-5],[-3,-10],[8,2],[-6,-6],[-1,7],[-4,5],[-10,-3],[10,-9],[3,-1],[2,1],[-5,-4],[6,-3],[5,-1],[8,4],[-7,-6],[-6,3],[2,6],[-5,4],[9,-2],[-7,4],[-4,10],[10,-4],[5,-5],[7,-2],[4,-5],[-4,9],[-6,-10],[6,7],[-10,-6],[5,9],[-9,10],[-4,7],[10,-5],[10,2],[6,10],[-8,4],[6,-10],[9,8],[6,4],[-10,-8],[-6,7],[-8,3],[-2,6],[10,8],[1,8],[9,-7],[-5,7],[-5,-8],[-7,-8],[-5,-8],[2,7],[-7,1],[-4,9],[-4,-10],[-1,-4],[1,7],[8,-2],[-6,8],[-6,1],[9,-1],[-8,8],[-7,1],[-5,-4],[7,-6],[-9,-8],[1,-3],[10,-10],[8,5],[10,-10],[-2,-6],[-5,5],[4,-7],[-2,-7],[10,9],[4,2],[-9,-7],[-8,9],[-7,-9],[5,-2],[-7,-1],[-3,-1],[-6,2],[8,-3],[-9,-9],[9,-9],[2,9],[-1,-6],[2,-7],[-4,6],[9,-4],[-4,-5],[9,-1],[9,-7],[7,-8],[-6,9],[2,1],[-6,-7],[-6,1],[8,-2],[7,7],[3,-9],[-7,1],[1,-1],[5,8],[2,-6],[6,10],[-3,-3],[6,-10],[-2,-1],[6,-4],[9,-8],[9,8],[1,10],[3,-1],[2,9],[-4,9],[6,6],[-10,-8],[4,-7],[-4,-4],[9,2],[4,8],[-9,-4],[-6,10],[-2,5],[-5,-5],[1,-3],[5,9],[1,-7],[7,3],[-2,9],[-1,-1],[5,7],[1,10],[3,6],[-1,5],[-6,-1],[8,9],[10,-8],[-8,3],[5,3],[3,-7],[-7,8],[7,1],[4,6],[-3,-1],[-4,-1],[-10,-4],[-6,10],[-8,-8],[1,2],[9,-1],[5,-4],[2,-1],[-4,7],[-9,-10],[7,6],[8,-2],[-2,-5],[8,-4],[3,3],[-3,4],[-1,3],[3,6],[-3,7],[8,8],[-4,1],[-1,6],[2,1],[-6,-3],[5,8],[7,-10],[-8,-2],[4,8],[-3,1],[3,7],[-9,-1],[3,-1],[-9,-8],[4,-7],[-5,-9],[-8,-9],[8,-4],[7,6],[-10,-10],[-10,5],[3,8],[-3,8],[-5,-9],[5,-4],[9,-4],[9,-4],[-9,-4],[-9,-10],[2,8],[4,-3],[4,-2],[3,-10],[5,-1],[-5,5],[-1,-5],[-8,3],[-5,-7],[-10,8],[6,2],[7,2],[-7,-6],[7,-6],[-2,1],[6,-2],[-6,9],[-3,9],[-6,-9],[-5,5],[-3,4],[-4,-8],[-9,-6],[2,5],[-9,5],[1,3],[7,10],[-4,-1],[8,5],[-6,-6],[-4,2],[-2,-8],[-3,-5],[7,2],[2,5],[9,-3],[1,-8],[-2,2],[9,-4],[2,2],[-4,-10],[8,6],[-5,8],[-7,10],[-10,5],[-5,10],[10,6],[5,-9],[-6,-2],[10,6],[9,7],[4,3],[8,-6],[2,10],[1,8],[-4,6],[4,4],[-6,-9],[-4,-10],[-6,2],[9,-10],[5,7],[-3,-1],[9,-9],[-7,-7],[5,9],[-2,10],[2,-3],[-10,-3],[2,3],[4,4],[-3,-6],[-6,-5],[-9,-2],[3,-1],[2,5],[-1,-10],[-8,-10],[-7,4],[7,-10],[5,6],[10,-6],[-8,8],[-5,3],[-3,8],[-6,-4],[5,2],[-9,7],[-8,9],[10,2],[6,-9],[7,8],[-7,-1],[-7,5],[-2,5],[9,-7],[-6,-6],[-4,6],[2,-3],[-9,9],[7,10],[-3,-5],[-2,-10],[2,-8],[6,5],[-4,-1],[6,5],[3,5],[4,-4],[-10,5],[9,3],[-5,-10],[-4,-2],[-3,7],[7,7],[8,9],[-7,10],[-10,-1],[2,-10],[2,-7],[-4,7],[2,-9],[9,-8],[-9,-10],[8,6],[-7,-8],[-9,-6],[-10,-9],[2,2],[-3,-2],[8,-9],[4,5],[-3,3],[10,-9],[-2,1],[-7,-6],[8,2],[10,4],[-3,9],[6,1],[-7,-9],[6,7],[4,1],[10,-8],[-5,2],[4,7],[10,-7],[10,-6],[-4,3],[5,-9],[-7,10],[-8,-6],[1,-2],[3,-4],[-3,-9],[-1,-9],[4,-9],[3,-7],[8,8],[8,-3],[-3,3],[4,8],[10,-2],[6,8],[-5,-8],[4,-1],[-5,-10],[-4,-1],[8,10],[3,9],[9,4],[3,3],[6,-8],[-7,3],[-7,-4],[-8,7],[-10,9],[-9,7],[-10,-1],[-1,-4],[-8,-9],[1,-8],[7,-1],[-6,2],[-7,9],[1,-4],[-7,5],[1,-6],[2,-5],[-7,5],[-4,8],[7,8],[-3,2],[5,5],[2,9],[-1,-4],[8,8],[-10,-9],[1,6],[9,4],[3,6],[-3,-7],[2,10],[-10,-6],[2,6],[-9,8],[-2,8],[8,-5],[-9,8],[-3,6],[-2,-9],[-9,-1],[-1,4],[-1,7],[-9,-7],[6,-10],[5,6],[-5,-5],[9,7],[9,8],[4,7],[8,-9],[1,-6],[1,2],[5,6],[-10,-5],[5,6],[2,3],[10,3],[3,5],[-9,-1],[-6,-8],[2,-9],[7,1],[7,-5],[3,-7],[7,1],[4,-6],[-4,5],[1,-10],[-9,7],[-4,7],[8,-2],[-1,6],[-1,-10],[2,7],[-2,-5],[-6,-7],[-4,9],[5,-9],[10,-7],[-2,-9],[-9,-7],[-2,6],[-7,-8],[-8,7],[1,7],[-4,2],[10,4],[-2,7],[1,-4],[-8,-10],[3,-9],[-5,10],[2,4],[6,9],[3,9],[10,9],[-10,6],[-3,-7],[4,-7],[10,-5],[-7,-6],[4,10],[-3,-5],[7,-4],[-6,8],[-7,-6],[-9,-10],[-10,-9],[3,-1],[-5,4],[-2,-8],[-2,-7],[-3,10],[10,-10],[10,-7],[-6,-9],[-4,-8],[3,-6],[3,-5],[6,-3],[-7,-8],[-10,-5],[10,-1],[8,5],[-10,2],[5,8],[4,2],[5,1],[-2,-10],[-9,1]], dtype = "int8")#candidate|7165|(512, 2)|const|int8
const_7166 = relay.const([-6,-9,7,-4,-3,-9,-8,4,2,-9,3,2,-2,-8,-10,4,-8,-7,-2,-5,1,-6,6,-10,1,-3,-3,-8,8,9,-1,-2,-5,3,1,4,2,10,2,-8,3,7,-8,10,-3,4,1,-10,-6,-4,2,6,10,4,9,-4,5,6,-8,-9,-7,-2,10,5,-6,-2,8,4,5,-1,2,-7,-9,-2,1,-8,6,-7,4,2,-10,2,-2,8,-4,2,-4,-5,-1,-10,10,-3,9,-3,-1,-7,-9,8,3,1,-5,-5,1,2,9,-6,-1,7,6,-5,7,7,10,9,3,3,10,-9,-2,-5,-4,-1,-8,6,-10,-3,4,-5,7,-8,-2,10,-2,5,9,-6,10,9,8,6,-8,-5,10,7,-3,-10,7,-9,9,5,-5,-1,8,7,-5,4,-1,-8,-10,-10,1,8,-2,-8,-2,-8,-4,3,9,8,10,-9,-2,6,1,4,8,1,10,10,2,8,7,8,1,1,-7,-4,9,-10,6,4,8,3,-5,-10,10,-5,-1,-2,6,-4,4,-1,-6,3,2,7,3,8,2,4,-7,-9,-1,-1,-2,9,2,9,10,-1,9,4,7,-9,1,-3,4,7,2,-2,4,10,-3,4,-1,6,5,4,-2,-5,6,-1,9,-8,9,-5,3,-9,-6,-10,9,9,-7,-10,-5,2,-10,-4,3,9,-1,-3,10,1,-4,-5,6,-1,-6,-2,3,-2,6,-1,7,-1,6,3,7,-4,-2,7,2,10,6,-8,-3,1,6,10,-4,4,-8,-6,10,7,-8,9,-2,-7,-1,9,-5,5,4,7,-8,-10,7,-3,-7,-8,-7,-4,-5,7,-5,-2,-7,-2,-4,-1,-9,1,8,-10,4,-1,-4,-10,-7,7,-5,2,5,5,4,-4,-8,6,8,-10,-3,-5,-7,10,-2,-7,5,9,5,1,-9,-10,-1,2,4,6,-4,-6,6,6,-2,-6,-2,9,8,-7,-7,5,-5,9,-10,7,-6,4,1,-1,-3,-10,-2,2,-10,-1,8,-7,3,-2,-3,-5,-4,-10,-1,9,-9,-8,-9,3,1,-6,-9,10,9,3,3,-10,8,-3,2,-4,-1,2,-3,9,10,-1,-8,-1,4,-8,1,-3,7,-2,8,-2,8,-8,10,5,3,-8,-8,8,2,-9,6,-6,10,4,1,8,1,-10,-5,10,10,9,-9,-2,-6,6,4,5,-7,3,-6,-9,7,7,-4,-10,-6,-2,9,-8,4,-7,3,6,2,9,-10,-2,-8,1,-7,-6,-3,10,2,-8,-9,9,-8,3,4,-7,-2,3,9,2,6,-9,-6,-10,-4,-7,5,8,-10,-3,-4,-9,9,-6,8,2,-6,5,-7,-2,-5,-7,-6,-2,-5,3,5,-8,5,-1,-2,9,2,-1,8,4,-4,-4,6,-7,2,4,1,10,-4,1,3,-5,3,-8,9,6,4,4,-7,3,-2,-7,-7,-10,-9,8,-2,-9,-8,6,8,3,-4,-2,-9,-10,-3,5,-3,4,10,4,-6,-7,-9,-4,-6,8,5,9,-8,6,-8,-5,7,-5,-1,7,1,4,6,6,6,-2,-8,4,1,-9,-10,-2,-4,-4,-5,6,6,5,-7,-5,-8,3,-9,-4,-6,1,-7,-1,-9,10,7,-9,6,-4,-8,-8,-4,-2,8,3,-9,8,-7,-1,-5,10,6,2,3,7,-4,10,5,-3,10,-5,-2,6,-3,6,9,1,-3,-9,10,10,10,2,-3,-8,-10,-1,7,4,6,9,5,-1,2,7,-8,6,10,-3,2,4,-4,6,2,-1,-9,-4,-10,-3,6,4,10,10,-7,-10,4,-3,-1,-8,-9,1,-9,2,-9,2,8,7,-6,-7,2,2,-5,4,5,9,1,4,5,1,-5,-1,-1,-3,7,-1,-9,-7,-9,-10,-1,10,9,5,-4,-9,-3,1,1,2,4,-9,8,9,6,-4,8,-10,10,2,4,-10,-6,-3,-5,-4,-10,-3,-10,-8,4,3,5,-1,-3,-6,8,5,9,10,-3,-4,-9,1,-1,-8,-8,9,8,-10,-4,-7,-4,-6,-10,-10,1,6,-3,3,-6,1,4,9,9,-1,8,7,2,-7,-10,-7,-1,4,10,9,8,1,-9,2,-2,1,2,-1,1,-7,5,1,7,-1,3,-4,-8,-3,-7,-5,7,-8,5,-3,9,7,-4,-1,6,-9,-2,9,9,-6,-8,-7,8,4,-9,10,-7,-4,-5,-1,9,-9,-4,-10,2,-1,-1,-7,-6,-4,8,-2,3,7,3,1,9,-2,10,-5,-9,7,3,-1,-5,-1,-1,9,9,1,5,3,-2,4,-6,-8,-3,7,7,6,-4,-6,-2,-6,2,-2,-9,-8,1,-7,-10,3,10,-1,9,10,6,8,-2,8,6,-8,8,-10,-7,-5,-1,-2,10,9,-3,-5,-6,9,-1,-9,-1,-2,4,-6,-8,-10,9,2,-7,1,2,3,10,6,-8,-8,4,6,3,-7,-2,2,8,3,4,7,9,-4,1,2,-4,10,2,6,-9,8,1,-5,3,6,1,3,-5,-10,-8,-8,3,-2,4,-4,-10,-4,-2,2,4,-3,3,-4,-3,-7,-7,5,10,8,-3,5,-5,-8,6,2,-10,-5,-1,3,5,6,2,-5,9,6,-6,-7,8,7,5,-5,4,-8,-3,2,-3,-2,-10,-7,10,10,4,4,3,7,-1,-5,-4,-4,5,5,-2,3,5,10,-5,1,10,-3,-9,2,-5,-8,1,-8,-6,6,-3,2,3,3,-4,9,-10,-8,-5,10,1,-2,8,1,-6,-3,-8,-7,1,-8,4,1,-2,-4,1,-8,2,5,2,5,4,7,5,2,-1,10,-10,9,2,-8,7,-5,7,-8,-7,7,1,3,5,1,-8,3,-4,1,-6,-8,6,-2,5,-2,-5,2,-2,-3,2,2,6,9,8,5,10,8,9,1,-2,-4,3,-4,-3,-9,-2,5,8,10,-4,1,8,-10,-9,-1,-5,9,-3,10,-9,-2,-1,1,-3,-7,-5,10,8,-10,-2,-10,-6,-2,4,-6,2,6,-7,7,5,4,2,3,6,7,-6,7,-5,-2,3,-4,8,-10,-4,-2,9,-8,3,-1,7,-9,4,-5,-4,-10,5,-2,1,-7,-9,5,-6,-10,-4,-8,-8,4,-10,5,-3,1,-8,-2,-4,-7,7,-2,-4,-10,3,1,-4,5,1,-9,6,4,-2,-4,-5,-1,2,-3,-4,-7,2,10,3,9,-5,10,-8,-5,3,9,2,-8,1,-1,6,-2,7,2,7,-6,2,6,-2,-10,-2,-3,-9,9,6,-5,-7,1,-10,4,6,2,7,8,10,-6,-9,7,2,7,5,10,-2,-7,-6,10,2,10,1,-9,-7,5,6,5,-7,7,6,-3,-8,1,-1,6,6,-3,3,9,-8,8,-6,1,-7,5,-6,4,-9,8,7,-7,9,1,3,3,-2,-7,-6,-2,-7,-8,5,8,8,-6,-9,9,3,1,-8,9,-7,-8,5,10,7,6,2,6,2,-5,6,-1,4,7,8,3,2,-10,1,2,8,10,4,9,7,-8,-10,2,-1,-7,6,-4,-1,-7,6,10,9,-3,-5,8,-8,7,-7,1,9,-7,-8,-3,-9,3,2,-9,-5,-2,7,-4,-8,5,9,5,6,3,5,2,6,9,-1,9,-3,6,-2,-8,-9,-8,-9,-6,-7,10,5,-7,-9,1,7,4,2,1,-8,6,2,-8,9,7,-5,9,8,4,-10,-7,-4,6,-1,-10,8,10,2,-4,-4,-8], dtype = "uint16")#candidate|7166|(1430,)|const|uint16
call_7163 = relay.TupleGetItem(func_4092_call(relay.reshape(const_7164.astype('int8'), []), relay.reshape(const_7165.astype('int8'), [8, 8, 16]), relay.reshape(const_7166.astype('uint16'), [1430,]), ), 1)
call_7167 = relay.TupleGetItem(func_4096_call(relay.reshape(const_7164.astype('int8'), []), relay.reshape(const_7165.astype('int8'), [8, 8, 16]), relay.reshape(const_7166.astype('uint16'), [1430,]), ), 1)
bop_7171 = relay.maximum(const_7165.astype('uint16'), const_7164.astype('uint16')) # shape=(512, 2)
output = relay.Tuple([call_7139,call_7163,const_7166,bop_7171,])
output2 = relay.Tuple([call_7140,call_7167,const_7166,bop_7171,])
func_7189 = relay.Function([], output)
mod['func_7189'] = func_7189
mod = relay.transform.InferType()(mod)
mutated_mod['func_7189'] = func_7189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7189_call = mutated_mod.get_global_var('func_7189')
call_7190 = func_7189_call()
output = call_7190
func_7191 = relay.Function([], output)
mutated_mod['func_7191'] = func_7191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6329_call = mod.get_global_var('func_6329')
func_6331_call = mutated_mod.get_global_var('func_6331')
call_7255 = func_6329_call()
call_7256 = func_6329_call()
output = relay.Tuple([call_7255,])
output2 = relay.Tuple([call_7256,])
func_7262 = relay.Function([], output)
mod['func_7262'] = func_7262
mod = relay.transform.InferType()(mod)
output = func_7262()
func_7263 = relay.Function([], output)
mutated_mod['func_7263'] = func_7263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1720_call = mod.get_global_var('func_1720')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_7281 = func_1720_call()
call_7282 = func_1720_call()
func_5668_call = mod.get_global_var('func_5668')
func_5670_call = mutated_mod.get_global_var('func_5670')
call_7284 = relay.TupleGetItem(func_5668_call(), 0)
call_7285 = relay.TupleGetItem(func_5670_call(), 0)
uop_7290 = relay.sin(call_7281.astype('float64')) # shape=(100, 2)
uop_7292 = relay.sin(call_7282.astype('float64')) # shape=(100, 2)
uop_7293 = relay.log2(uop_7290.astype('float64')) # shape=(100, 2)
uop_7295 = relay.log2(uop_7292.astype('float64')) # shape=(100, 2)
bop_7305 = relay.floor_divide(uop_7293.astype('float64'), relay.reshape(uop_7290.astype('float64'), relay.shape_of(uop_7293))) # shape=(100, 2)
bop_7308 = relay.floor_divide(uop_7295.astype('float64'), relay.reshape(uop_7292.astype('float64'), relay.shape_of(uop_7295))) # shape=(100, 2)
func_1525_call = mod.get_global_var('func_1525')
func_1528_call = mutated_mod.get_global_var('func_1528')
const_7318 = relay.const(10, dtype = "uint8")#candidate|7318|()|const|uint8
call_7317 = relay.TupleGetItem(func_1525_call(relay.reshape(const_7318.astype('uint8'), [])), 0)
call_7319 = relay.TupleGetItem(func_1528_call(relay.reshape(const_7318.astype('uint8'), [])), 0)
func_5898_call = mod.get_global_var('func_5898')
func_5899_call = mutated_mod.get_global_var('func_5899')
call_7320 = relay.TupleGetItem(func_5898_call(), 5)
call_7321 = relay.TupleGetItem(func_5899_call(), 5)
uop_7325 = relay.acos(uop_7293.astype('float32')) # shape=(100, 2)
uop_7327 = relay.acos(uop_7295.astype('float32')) # shape=(100, 2)
uop_7337 = relay.atan(uop_7325.astype('float32')) # shape=(100, 2)
uop_7339 = relay.atan(uop_7327.astype('float32')) # shape=(100, 2)
func_4362_call = mod.get_global_var('func_4362')
func_4363_call = mutated_mod.get_global_var('func_4363')
call_7345 = relay.TupleGetItem(func_4362_call(), 0)
call_7346 = relay.TupleGetItem(func_4363_call(), 0)
uop_7347 = relay.exp(uop_7337.astype('float32')) # shape=(100, 2)
uop_7349 = relay.exp(uop_7339.astype('float32')) # shape=(100, 2)
uop_7373 = relay.cos(uop_7347.astype('float32')) # shape=(100, 2)
uop_7375 = relay.cos(uop_7349.astype('float32')) # shape=(100, 2)
output = relay.Tuple([call_7284,bop_7305,call_7317,const_7318,call_7320,call_7345,uop_7373,])
output2 = relay.Tuple([call_7285,bop_7308,call_7319,const_7318,call_7321,call_7346,uop_7375,])
func_7376 = relay.Function([], output)
mod['func_7376'] = func_7376
mod = relay.transform.InferType()(mod)
output = func_7376()
func_7377 = relay.Function([], output)
mutated_mod['func_7377'] = func_7377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3781_call = mod.get_global_var('func_3781')
func_3783_call = mutated_mod.get_global_var('func_3783')
call_7388 = func_3781_call()
call_7389 = func_3781_call()
func_3376_call = mod.get_global_var('func_3376')
func_3381_call = mutated_mod.get_global_var('func_3381')
const_7394 = relay.const([0.526424,-4.159213,5.743309,-9.782547,-9.017678,-5.146473,-9.977081,-7.371509,-9.959206,9.129462,-2.841490,3.962681,-3.687903,-8.992511,-7.194371,-3.374884,-8.870963,-6.843598,5.552454,-3.113781,-4.970331,4.875422,4.675667,2.927343,3.201157,-4.998192,-7.460181,-1.306111,-3.990926,-9.842992,-9.581768,-7.644882,2.838244,-3.955610,6.099772,-1.765382,0.402920,-9.866190,-7.010596,-9.721018,9.908711,0.321759,-8.173866,-2.518764,-9.411862,-5.534200,8.474066,5.792486,7.685349,3.321398,4.952779,-3.354700,4.221507,5.783046,-7.964630,3.468398,-6.877336,4.816456,-9.415514,9.087771,3.906179,-1.483483,3.514292,6.649347,8.566937,8.913012,7.115686,-2.804373,7.976896,-2.929759,2.168076,4.664834,-1.410060,8.518331,-3.972984,-1.421190,-9.312824,-6.280664,-9.975164,-2.162963,-1.616704,-9.968891,-2.879325,9.406960,-2.631954,8.623699,2.891259,-6.614929,-7.871820,4.220927,-1.274539,-9.127846,-8.237516,-2.992765,-1.178898,-0.932065,7.167514,-1.857345,5.495670,7.266428,9.847691,-8.201961,6.102316,9.483503,-1.572779,-3.725347,-8.115936,7.337381,5.905068,9.667405,-3.656333,-0.635776,3.046747,0.206092,-7.399940,-7.675880,-2.539576,6.204200,3.746525,7.261702,3.608671,1.415979,-4.710307,-8.340634,-0.766444,1.512694,0.809700,-8.448656,1.207158,-7.575143,-7.218666,0.189876,1.758896,-1.070512,7.507435,-6.825377,2.493982,-8.326625,-0.453355,6.322143,8.995496,7.380885,9.980781,6.065305,-2.482366,-7.139291,-9.184543,0.300646,-1.030747,6.146103,2.293905,-2.648770,4.641737,-6.645993,7.255994,-1.400606,-1.757936,-8.468408,-2.062452,-1.847328,5.873808,4.744249,1.438957,2.670389,6.416796,9.126922,-1.552908,5.482232,5.402579,4.560158,-9.954388,4.252719,6.757710,-2.082191,0.090377,-8.683823,8.775698,-5.003345,-2.881587,1.336111,-3.973591,-4.704856,-2.658489,-7.139238,2.468371,0.673692,-1.103267,1.653075,-1.854838,1.798396,-6.251892,-1.108026,6.859166,-0.061626,-4.252813,5.264372,8.247690,4.824807,-3.753128,2.473985,0.440810,4.766555,0.334252,3.042801,-9.715822,7.601519,6.033552,-4.197811,-3.020766,-3.566846,-5.619154,-3.120792,-5.680280,-8.916250,8.022896,-9.186313,-5.551774,-0.771883,-5.575773,8.683799,-8.185493,-2.038106,-3.091977,2.733618,4.519792,4.858991,6.562510,9.463115,2.239454,-5.112229,6.274067,2.002325,-4.251057,9.838669,2.603551,0.970865,0.528045,9.165887,8.351726,6.803330,5.957563,-8.956845,-2.914124,-1.269103,7.302435,-5.148026,6.578697,-1.723450,-5.365379,0.419028,-1.582672,7.207946,-7.211199,6.150019,2.214962,-8.473443,7.684800,-4.474265,9.763000,6.355070,6.262998,3.124999,9.586992,4.829182,-0.077005,-3.865947,1.344399,-5.636322,-6.024018,9.026423], dtype = "float32")#candidate|7394|(270,)|const|float32
var_7395 = relay.var("var_7395", dtype = "int16", shape = (1680,))#candidate|7395|(1680,)|var|int16
const_7396 = relay.const([1.816119,0.619441,0.856810,-0.325980,2.215990,-3.395014,-2.965270,-7.869792,-7.499967,6.948354,7.634510,0.817247,-7.445990,8.342679,-9.568010,-8.356263,-2.970142,-4.395960,7.845034,-8.491330,-7.087350,-4.345873,3.969480,1.159595,5.996484,1.015117,9.252405,5.832518,-1.913646,8.329042,9.219156,5.416512,-9.016640,6.364196,-3.855954,-3.336538,-2.043860,2.473969,3.491832,-1.461809,0.398594,8.980476,-9.487301,-1.491518,-3.041894,7.547662,-0.089989,2.062641,-2.876540,-2.321374,-0.680859,-0.286652,9.989115,1.569975,-4.235713,2.542163,4.945003,-6.215869,0.270863,-9.239797,4.700846,-0.466913,-5.710984,-6.656058,-0.189180,5.739159,3.623993,-9.446921,5.160340,8.797799,4.912121,4.070510,-9.072300,-4.358470,1.440542,3.022331,-4.656001,-5.625993,0.330813,7.940815,7.863009,-2.054124,-6.851541,6.034032,-1.349473,2.281616,6.071100,-6.275411,5.648649,-0.470694,-2.385394,7.220660,6.831494,4.720820,-4.334267,-2.883181,-1.687615,-3.884649,1.347823,-5.306016,-0.117822,9.868296,1.916825,7.337628,-1.401409,6.386643,0.075105,2.827780,-5.055243,3.838505,-2.648828,-7.879612,0.742608,4.052141,-4.625308,-1.237284,-2.920319,-7.042008,-3.580778,-2.174696,4.479571,0.170194,-4.562960,1.019919,6.576252,4.796349,8.095232,-5.888144,-2.023257,9.170498,-3.550222,7.607125,-8.800565,-0.154386,-2.908236,2.833974,-9.703938,-7.865430,-7.931540,6.358504,9.863974,5.561879,-4.408884,3.368026,6.253232,5.099918,-4.639860,-9.869089,-0.921175,5.963193,8.341298,6.480336,1.265608,-3.702319,9.605182,-7.915038,-5.301468,8.345309,0.125262,5.766150,-6.064435,-2.888443,-0.075193,1.212881,7.932651,8.982370,8.056845,-8.450356,-2.883884,-0.985062,-0.470630,-4.916176,-3.277716,6.891478,-2.321044,9.473512,6.347812,-0.967464,-1.807519,0.821136,-1.116068,0.452111,5.366416,6.955929,-7.573575,5.283437,-1.591838,-1.107828,-8.355179,-9.036985,-7.734237,9.249761,-4.414772,8.681707,5.821708,-7.668452,1.283988,3.909517,-2.922519,8.786452,7.099840,5.419043,-2.417610,-2.749763,-8.185173,-2.116241,-3.295404,-6.768242,3.481945,-6.662002,-8.797912,-2.986929,-1.196913,-1.940223,-3.238318,2.050031,1.102829,4.814743,-0.442420,-6.326544,4.917473,-6.527058,-8.818030,-3.320479,-6.131751,-9.252171,1.796077,9.696840,-3.608407,-8.561503,5.957246,-5.998850,3.601697,-0.049065,-9.218955,-8.501526,2.621587,0.102906,4.678838,0.316486,-1.250010,3.452979,3.546931,9.348507,-6.039549,-4.027314,-6.120617,-1.422893,0.389049,1.248139,4.297571,1.587545,-9.667796,-3.175365,-1.444397,-4.788483,0.355618,-6.687737,-3.469013,7.014217,-8.791620,-4.996639,-0.781766,-8.144524,9.982328,1.685718,0.312111,-1.608480,-0.643832,6.248206,-9.797433,0.200331,8.855951,-2.195001,-2.038872,6.309806,-7.535038,5.904710,-9.105826,-1.398753,7.910502,1.136522,-1.991543,7.340839,-3.103727,6.492889,-8.831028,8.068639,-8.868166,1.940187,8.930233,4.869596,-4.289204,-8.688970,-7.565215,-0.605139,0.974400,-2.660786,1.116739,-9.468871,5.540468,4.790259,-0.543938,2.259056,-5.567683,4.200176,5.970199,6.131718,7.768500,3.362609,-5.073256,-6.000560,2.436955,3.500943,-2.720711,-1.388831,4.706159,2.639993,-3.184176,3.543304,0.669105,-3.561951,4.002370,-0.911340,-4.584676,7.432400,8.085020,-6.436171,-4.388140,-7.365555,3.932600,-1.027152,-5.593008,-6.017005,3.840464,0.309038], dtype = "float64")#candidate|7396|(336,)|const|float64
call_7393 = relay.TupleGetItem(func_3376_call(relay.reshape(const_7394.astype('float32'), [15, 6, 3]), relay.reshape(var_7395.astype('int16'), [1680,]), relay.reshape(const_7396.astype('float64'), [336,]), ), 3)
call_7397 = relay.TupleGetItem(func_3381_call(relay.reshape(const_7394.astype('float32'), [15, 6, 3]), relay.reshape(var_7395.astype('int16'), [1680,]), relay.reshape(const_7396.astype('float64'), [336,]), ), 3)
output = relay.Tuple([call_7388,call_7393,const_7394,var_7395,const_7396,])
output2 = relay.Tuple([call_7389,call_7397,const_7394,var_7395,const_7396,])
func_7436 = relay.Function([var_7395,], output)
mod['func_7436'] = func_7436
mod = relay.transform.InferType()(mod)
mutated_mod['func_7436'] = func_7436
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7437 = relay.var("var_7437", dtype = "int16", shape = (1680,))#candidate|7437|(1680,)|var|int16
func_7436_call = mutated_mod.get_global_var('func_7436')
call_7438 = func_7436_call(var_7437)
output = call_7438
func_7439 = relay.Function([var_7437], output)
mutated_mod['func_7439'] = func_7439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7376_call = mod.get_global_var('func_7376')
func_7377_call = mutated_mod.get_global_var('func_7377')
call_7545 = relay.TupleGetItem(func_7376_call(), 5)
call_7546 = relay.TupleGetItem(func_7377_call(), 5)
output = call_7545
output2 = call_7546
func_7550 = relay.Function([], output)
mod['func_7550'] = func_7550
mod = relay.transform.InferType()(mod)
output = func_7550()
func_7551 = relay.Function([], output)
mutated_mod['func_7551'] = func_7551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7087_call = mod.get_global_var('func_7087')
func_7089_call = mutated_mod.get_global_var('func_7089')
call_7552 = relay.TupleGetItem(func_7087_call(), 0)
call_7553 = relay.TupleGetItem(func_7089_call(), 0)
func_6490_call = mod.get_global_var('func_6490')
func_6492_call = mutated_mod.get_global_var('func_6492')
call_7558 = relay.TupleGetItem(func_6490_call(), 0)
call_7559 = relay.TupleGetItem(func_6492_call(), 0)
output = relay.Tuple([call_7552,call_7558,])
output2 = relay.Tuple([call_7553,call_7559,])
func_7580 = relay.Function([], output)
mod['func_7580'] = func_7580
mod = relay.transform.InferType()(mod)
mutated_mod['func_7580'] = func_7580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7580_call = mutated_mod.get_global_var('func_7580')
call_7581 = func_7580_call()
output = call_7581
func_7582 = relay.Function([], output)
mutated_mod['func_7582'] = func_7582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4816_call = mod.get_global_var('func_4816')
func_4817_call = mutated_mod.get_global_var('func_4817')
call_7608 = func_4816_call()
call_7609 = func_4816_call()
output = call_7608
output2 = call_7609
func_7639 = relay.Function([], output)
mod['func_7639'] = func_7639
mod = relay.transform.InferType()(mod)
output = func_7639()
func_7640 = relay.Function([], output)
mutated_mod['func_7640'] = func_7640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7014_call = mod.get_global_var('func_7014')
func_7015_call = mutated_mod.get_global_var('func_7015')
call_7662 = relay.TupleGetItem(func_7014_call(), 1)
call_7663 = relay.TupleGetItem(func_7015_call(), 1)
output = relay.Tuple([call_7662,])
output2 = relay.Tuple([call_7663,])
func_7668 = relay.Function([], output)
mod['func_7668'] = func_7668
mod = relay.transform.InferType()(mod)
output = func_7668()
func_7669 = relay.Function([], output)
mutated_mod['func_7669'] = func_7669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_7670 = func_5648_call()
call_7671 = func_5648_call()
func_530_call = mod.get_global_var('func_530')
func_533_call = mutated_mod.get_global_var('func_533')
var_7695 = relay.var("var_7695", dtype = "uint8", shape = ())#candidate|7695|()|var|uint8
call_7694 = func_530_call(relay.reshape(var_7695.astype('uint8'), []))
call_7696 = func_530_call(relay.reshape(var_7695.astype('uint8'), []))
func_4578_call = mod.get_global_var('func_4578')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_7719 = func_4578_call()
call_7720 = func_4578_call()
func_1614_call = mod.get_global_var('func_1614')
func_1617_call = mutated_mod.get_global_var('func_1617')
const_7734 = relay.const([[2.989548,-1.049321,-7.714137,4.294479,3.200267,-9.428600,-5.437435,3.043254,6.655642,8.414043,1.769172,9.725024,0.456987,-1.347289,-5.126018,5.006342,-5.650474,3.722608,6.843722,8.812530],[-7.413738,8.742863,1.088748,-6.103667,6.922800,9.388802,1.154312,-1.279576,9.690589,-6.447885,-0.118445,9.434018,-7.254591,3.653819,4.487900,-6.364390,-9.424165,-5.361715,-4.725451,-7.090823],[-0.985093,6.292406,-4.968660,5.939769,-0.953074,-5.339119,6.501961,7.945301,-5.030600,0.106967,6.892321,8.199027,-5.445811,-6.007245,-9.084150,-1.461946,-6.429989,-5.330187,5.950216,9.385224],[3.791130,4.576421,8.863935,-7.630397,9.919271,-1.926256,-0.871251,0.805741,4.656265,9.302142,-5.805125,1.756681,5.562773,-6.790113,3.799008,-3.436033,1.369773,0.370455,-4.967477,-6.722338],[9.055220,9.080469,-9.615292,-9.750704,-3.857888,7.454076,-0.036800,8.977900,-6.068119,-8.288126,7.769594,-9.370231,-0.622637,-7.179935,-6.453568,7.250476,9.232261,3.503872,3.886016,3.628045],[1.932873,-8.398814,5.048339,-4.497279,1.167653,3.392996,8.101649,9.022006,6.131519,5.756490,-6.478982,-1.724724,8.385870,6.413585,5.194160,-3.799275,4.099750,-3.093817,-1.341248,-5.321284],[-9.629787,5.112371,-0.777055,3.433876,-4.077987,6.924306,1.621251,-1.170691,5.368778,5.541429,-3.850879,8.469020,8.066619,3.935083,-4.773405,6.474436,9.514389,2.903111,-7.648085,-0.808037],[9.364206,2.299908,4.831094,3.403328,-9.583577,2.439453,-4.999927,-0.607290,8.853442,9.826454,-7.667256,-5.217014,2.741555,4.585053,-2.330662,-0.617934,6.526913,9.403772,4.754312,6.151788],[2.688614,1.082244,8.452680,5.795628,1.028458,6.858926,-3.039711,9.773458,4.003094,3.448364,-2.148887,3.309896,0.015413,-1.943266,8.463298,-2.469215,5.005009,-5.065908,-2.223617,2.642020],[-7.692191,3.806598,-9.612394,1.893711,7.067559,0.807440,-1.073085,1.516066,5.736632,5.357011,6.561178,-1.981915,0.773154,6.753861,-0.173698,2.217692,0.143099,4.579240,2.920008,1.535109]], dtype = "float32")#candidate|7734|(10, 20)|const|float32
call_7733 = relay.TupleGetItem(func_1614_call(relay.reshape(const_7734.astype('float32'), [100, 2])), 0)
call_7735 = relay.TupleGetItem(func_1617_call(relay.reshape(const_7734.astype('float32'), [100, 2])), 0)
func_7189_call = mod.get_global_var('func_7189')
func_7191_call = mutated_mod.get_global_var('func_7191')
call_7738 = relay.TupleGetItem(func_7189_call(), 3)
call_7739 = relay.TupleGetItem(func_7191_call(), 3)
func_2113_call = mod.get_global_var('func_2113')
func_2115_call = mutated_mod.get_global_var('func_2115')
var_7773 = relay.var("var_7773", dtype = "int16", shape = (1680,))#candidate|7773|(1680,)|var|int16
call_7772 = relay.TupleGetItem(func_2113_call(relay.reshape(var_7773.astype('int16'), [1680,])), 0)
call_7774 = relay.TupleGetItem(func_2115_call(relay.reshape(var_7773.astype('int16'), [1680,])), 0)
uop_7778 = relay.atanh(call_7733.astype('float32')) # shape=(100, 2)
uop_7780 = relay.atanh(call_7735.astype('float32')) # shape=(100, 2)
output = relay.Tuple([call_7670,call_7694,var_7695,call_7719,const_7734,call_7738,call_7772,var_7773,uop_7778,])
output2 = relay.Tuple([call_7671,call_7696,var_7695,call_7720,const_7734,call_7739,call_7774,var_7773,uop_7780,])
func_7789 = relay.Function([var_7695,var_7773,], output)
mod['func_7789'] = func_7789
mod = relay.transform.InferType()(mod)
mutated_mod['func_7789'] = func_7789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7789_call = mutated_mod.get_global_var('func_7789')
var_7791 = relay.var("var_7791", dtype = "uint8", shape = ())#candidate|7791|()|var|uint8
var_7792 = relay.var("var_7792", dtype = "int16", shape = (1680,))#candidate|7792|(1680,)|var|int16
call_7790 = func_7789_call(var_7791,var_7792,)
output = call_7790
func_7793 = relay.Function([var_7791,var_7792,], output)
mutated_mod['func_7793'] = func_7793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1579_call = mod.get_global_var('func_1579')
func_1580_call = mutated_mod.get_global_var('func_1580')
call_7884 = relay.TupleGetItem(func_1579_call(), 0)
call_7885 = relay.TupleGetItem(func_1580_call(), 0)
func_7376_call = mod.get_global_var('func_7376')
func_7377_call = mutated_mod.get_global_var('func_7377')
call_7889 = relay.TupleGetItem(func_7376_call(), 6)
call_7890 = relay.TupleGetItem(func_7377_call(), 6)
output = relay.Tuple([call_7884,call_7889,])
output2 = relay.Tuple([call_7885,call_7890,])
func_7899 = relay.Function([], output)
mod['func_7899'] = func_7899
mod = relay.transform.InferType()(mod)
mutated_mod['func_7899'] = func_7899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7899_call = mutated_mod.get_global_var('func_7899')
call_7900 = func_7899_call()
output = call_7900
func_7901 = relay.Function([], output)
mutated_mod['func_7901'] = func_7901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_7918 = relay.TupleGetItem(func_2458_call(), 0)
call_7919 = relay.TupleGetItem(func_2459_call(), 0)
output = relay.Tuple([call_7918,])
output2 = relay.Tuple([call_7919,])
func_7920 = relay.Function([], output)
mod['func_7920'] = func_7920
mod = relay.transform.InferType()(mod)
output = func_7920()
func_7921 = relay.Function([], output)
mutated_mod['func_7921'] = func_7921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_7955 = relay.TupleGetItem(func_3183_call(), 0)
call_7956 = relay.TupleGetItem(func_3184_call(), 0)
func_1174_call = mod.get_global_var('func_1174')
func_1176_call = mutated_mod.get_global_var('func_1176')
call_7970 = relay.TupleGetItem(func_1174_call(), 2)
call_7971 = relay.TupleGetItem(func_1176_call(), 2)
func_3937_call = mod.get_global_var('func_3937')
func_3938_call = mutated_mod.get_global_var('func_3938')
call_7974 = relay.TupleGetItem(func_3937_call(), 0)
call_7975 = relay.TupleGetItem(func_3938_call(), 0)
bop_7976 = relay.less(call_7955.astype('bool'), relay.reshape(call_7974.astype('bool'), relay.shape_of(call_7955))) # shape=(9, 1, 8)
bop_7979 = relay.less(call_7956.astype('bool'), relay.reshape(call_7975.astype('bool'), relay.shape_of(call_7956))) # shape=(9, 1, 8)
output = relay.Tuple([call_7970,bop_7976,])
output2 = relay.Tuple([call_7971,bop_7979,])
func_7985 = relay.Function([], output)
mod['func_7985'] = func_7985
mod = relay.transform.InferType()(mod)
output = func_7985()
func_7986 = relay.Function([], output)
mutated_mod['func_7986'] = func_7986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5534_call = mod.get_global_var('func_5534')
func_5536_call = mutated_mod.get_global_var('func_5536')
call_8003 = func_5534_call()
call_8004 = func_5534_call()
output = relay.Tuple([call_8003,])
output2 = relay.Tuple([call_8004,])
func_8017 = relay.Function([], output)
mod['func_8017'] = func_8017
mod = relay.transform.InferType()(mod)
output = func_8017()
func_8018 = relay.Function([], output)
mutated_mod['func_8018'] = func_8018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6082_call = mod.get_global_var('func_6082')
func_6084_call = mutated_mod.get_global_var('func_6084')
call_8078 = func_6082_call()
call_8079 = func_6082_call()
output = call_8078
output2 = call_8079
func_8096 = relay.Function([], output)
mod['func_8096'] = func_8096
mod = relay.transform.InferType()(mod)
output = func_8096()
func_8097 = relay.Function([], output)
mutated_mod['func_8097'] = func_8097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5211_call = mod.get_global_var('func_5211')
func_5213_call = mutated_mod.get_global_var('func_5213')
call_8128 = relay.TupleGetItem(func_5211_call(), 1)
call_8129 = relay.TupleGetItem(func_5213_call(), 1)
uop_8142 = relay.log(call_8128.astype('float32')) # shape=(100, 2)
uop_8144 = relay.log(call_8129.astype('float32')) # shape=(100, 2)
bop_8149 = relay.greater(uop_8142.astype('bool'), relay.reshape(call_8128.astype('bool'), relay.shape_of(uop_8142))) # shape=(100, 2)
bop_8152 = relay.greater(uop_8144.astype('bool'), relay.reshape(call_8129.astype('bool'), relay.shape_of(uop_8144))) # shape=(100, 2)
var_8154 = relay.var("var_8154", dtype = "float32", shape = (100, 2))#candidate|8154|(100, 2)|var|float32
bop_8155 = relay.equal(call_8128.astype('bool'), relay.reshape(var_8154.astype('bool'), relay.shape_of(call_8128))) # shape=(100, 2)
bop_8158 = relay.equal(call_8129.astype('bool'), relay.reshape(var_8154.astype('bool'), relay.shape_of(call_8129))) # shape=(100, 2)
const_8165 = relay.const([[7.365510,0.023940],[0.868382,9.693226],[3.244639,0.637082],[7.739195,6.333899],[-7.351944,9.306857],[-0.835062,5.405183],[-2.436376,0.492619],[7.723275,-6.099738],[1.721828,-8.322463],[5.952069,-5.694547],[3.345598,-9.060133],[2.364845,-6.966609],[-1.532060,-4.214598],[-2.287055,3.166179],[-6.640768,6.211997],[9.094759,-4.852838],[-3.927179,1.184847],[-9.782188,-6.875665],[3.579235,-4.462352],[-7.259681,-0.357445],[8.818459,8.991355],[2.389595,-1.525847],[7.108629,7.220659],[-6.669716,4.117016],[-1.781694,-8.748134],[-0.806523,-2.355467],[8.032091,0.444410],[-1.510033,-4.330321],[-0.840601,4.866922],[-2.342494,-8.033619],[2.060768,-9.376909],[9.072697,-5.524114],[-1.160027,5.108656],[2.721159,-4.426595],[-2.009367,-7.534810],[-1.690933,-7.514225],[-4.913563,-0.575496],[-6.709145,-6.930986],[-3.811743,7.813145],[1.653653,8.328827],[-9.092498,-8.497243],[-0.802713,-5.459428],[-1.057108,1.155415],[0.006170,-2.635157],[2.102115,8.293039],[8.129842,-4.644153],[-8.118764,6.129444],[4.157372,-5.404033],[4.311079,-3.898792],[6.015251,0.199407],[3.370438,-1.097481],[-9.164044,1.004810],[2.883680,6.703742],[-8.335379,-4.439663],[1.500672,-3.047382],[-9.259883,-2.948217],[-7.821230,-3.432754],[3.726223,8.310793],[-1.871768,-6.395100],[-4.069886,3.900636],[-5.254833,-2.330741],[-9.807057,8.851742],[6.652801,-7.067372],[-9.081265,4.666297],[5.131133,3.363739],[6.384603,-8.892789],[-4.473746,0.656253],[-9.965189,9.262198],[1.399197,9.039379],[-5.802342,-4.603740],[8.177018,-4.045774],[7.888187,-8.305069],[0.893427,-3.404013],[-3.531124,-1.263504],[9.039311,-7.840220],[-9.299411,-8.388502],[8.785401,2.954168],[-7.913930,0.132987],[1.200399,-0.257631],[-5.028662,4.059200],[-0.004760,-0.594435],[-5.104813,4.500012],[-6.922772,2.159976],[4.919985,0.185397],[-7.042942,0.090476],[-3.089212,-7.174704],[-9.960988,-2.192553],[7.817023,-9.986855],[2.117652,-3.278856],[5.345094,4.028154],[3.835160,4.356284],[-3.623233,-0.767401],[4.104693,-7.827549],[-7.798554,7.885345],[2.190636,6.850487],[-2.680953,-7.073490],[2.473302,8.479506],[-1.247563,-5.441809],[-3.754500,6.374302],[-4.570206,9.484682]], dtype = "float32")#candidate|8165|(100, 2)|const|float32
bop_8166 = relay.bitwise_xor(call_8128.astype('uint16'), relay.reshape(const_8165.astype('uint16'), relay.shape_of(call_8128))) # shape=(100, 2)
bop_8169 = relay.bitwise_xor(call_8129.astype('uint16'), relay.reshape(const_8165.astype('uint16'), relay.shape_of(call_8129))) # shape=(100, 2)
output = relay.Tuple([bop_8149,bop_8155,bop_8166,])
output2 = relay.Tuple([bop_8152,bop_8158,bop_8169,])
func_8188 = relay.Function([var_8154,], output)
mod['func_8188'] = func_8188
mod = relay.transform.InferType()(mod)
var_8189 = relay.var("var_8189", dtype = "float32", shape = (100, 2))#candidate|8189|(100, 2)|var|float32
output = func_8188(var_8189)
func_8190 = relay.Function([var_8189], output)
mutated_mod['func_8190'] = func_8190
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8198 = relay.const([[[4],[7],[-8],[4],[-3],[-3],[-5],[10],[4],[4],[10],[-2],[-6],[2],[-3]],[[-9],[-6],[4],[-1],[4],[-7],[10],[3],[9],[-4],[7],[-2],[10],[4],[-2]],[[-5],[-3],[-9],[5],[-7],[-8],[5],[-8],[8],[6],[-10],[-5],[-3],[-10],[9]],[[5],[3],[4],[-7],[4],[9],[-6],[-7],[-3],[-2],[6],[-3],[4],[-6],[-5]],[[6],[-10],[8],[-1],[-5],[6],[-4],[-8],[-9],[-8],[1],[4],[-5],[-2],[-5]],[[-7],[-6],[10],[-2],[-8],[-3],[-1],[-9],[9],[-10],[-2],[9],[9],[-8],[-6]],[[-7],[-4],[1],[-7],[-2],[-10],[-9],[3],[7],[-9],[-9],[2],[-9],[-3],[-1]],[[10],[1],[10],[-5],[-6],[2],[-5],[4],[1],[9],[2],[3],[7],[4],[-8]],[[10],[-2],[-1],[4],[-1],[-4],[-4],[-6],[-6],[4],[8],[-7],[-10],[10],[-4]],[[-9],[-6],[5],[5],[-3],[10],[9],[-8],[-4],[1],[4],[-6],[10],[-5],[9]],[[1],[-6],[-1],[4],[2],[10],[9],[-8],[4],[1],[-2],[7],[-4],[-3],[7]],[[10],[2],[-7],[-7],[-8],[-10],[-1],[-2],[6],[-10],[3],[2],[1],[7],[8]],[[-8],[4],[-2],[-4],[3],[6],[-4],[4],[5],[-10],[-7],[-1],[3],[8],[6]],[[3],[-2],[-3],[-7],[-3],[-8],[-6],[7],[8],[8],[-1],[1],[7],[-1],[-3]],[[2],[-10],[-5],[1],[9],[4],[5],[2],[8],[6],[-6],[-4],[-8],[-4],[-5]],[[-6],[4],[-1],[9],[1],[-6],[-7],[-5],[-2],[7],[-8],[4],[3],[-2],[-1]]], dtype = "int64")#candidate|8198|(16, 15, 1)|const|int64
var_8199 = relay.var("var_8199", dtype = "int64", shape = (16, 15, 9))#candidate|8199|(16, 15, 9)|var|int64
bop_8200 = relay.greater_equal(const_8198.astype('bool'), var_8199.astype('bool')) # shape=(16, 15, 9)
func_3966_call = mod.get_global_var('func_3966')
func_3968_call = mutated_mod.get_global_var('func_3968')
call_8212 = relay.TupleGetItem(func_3966_call(), 0)
call_8213 = relay.TupleGetItem(func_3968_call(), 0)
uop_8242 = relay.log2(var_8199.astype('float32')) # shape=(16, 15, 9)
func_1614_call = mod.get_global_var('func_1614')
func_1617_call = mutated_mod.get_global_var('func_1617')
var_8249 = relay.var("var_8249", dtype = "float32", shape = (200,))#candidate|8249|(200,)|var|float32
call_8248 = relay.TupleGetItem(func_1614_call(relay.reshape(var_8249.astype('float32'), [100, 2])), 0)
call_8250 = relay.TupleGetItem(func_1617_call(relay.reshape(var_8249.astype('float32'), [100, 2])), 0)
func_6286_call = mod.get_global_var('func_6286')
func_6287_call = mutated_mod.get_global_var('func_6287')
call_8262 = relay.TupleGetItem(func_6286_call(), 3)
call_8263 = relay.TupleGetItem(func_6287_call(), 3)
func_3937_call = mod.get_global_var('func_3937')
func_3938_call = mutated_mod.get_global_var('func_3938')
call_8266 = relay.TupleGetItem(func_3937_call(), 0)
call_8267 = relay.TupleGetItem(func_3938_call(), 0)
output = relay.Tuple([bop_8200,call_8212,uop_8242,call_8248,var_8249,call_8262,call_8266,])
output2 = relay.Tuple([bop_8200,call_8213,uop_8242,call_8250,var_8249,call_8263,call_8267,])
func_8306 = relay.Function([var_8199,var_8249,], output)
mod['func_8306'] = func_8306
mod = relay.transform.InferType()(mod)
mutated_mod['func_8306'] = func_8306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8306_call = mutated_mod.get_global_var('func_8306')
var_8308 = relay.var("var_8308", dtype = "int64", shape = (16, 15, 9))#candidate|8308|(16, 15, 9)|var|int64
var_8309 = relay.var("var_8309", dtype = "float32", shape = (200,))#candidate|8309|(200,)|var|float32
call_8307 = func_8306_call(var_8308,var_8309,)
output = call_8307
func_8310 = relay.Function([var_8308,var_8309,], output)
mutated_mod['func_8310'] = func_8310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8096_call = mod.get_global_var('func_8096')
func_8097_call = mutated_mod.get_global_var('func_8097')
call_8327 = func_8096_call()
call_8328 = func_8096_call()
func_4362_call = mod.get_global_var('func_4362')
func_4363_call = mutated_mod.get_global_var('func_4363')
call_8358 = relay.TupleGetItem(func_4362_call(), 0)
call_8359 = relay.TupleGetItem(func_4363_call(), 0)
uop_8360 = relay.log2(call_8327.astype('float32')) # shape=(9, 1, 8)
uop_8362 = relay.log2(call_8328.astype('float32')) # shape=(9, 1, 8)
output = relay.Tuple([call_8358,uop_8360,])
output2 = relay.Tuple([call_8359,uop_8362,])
func_8367 = relay.Function([], output)
mod['func_8367'] = func_8367
mod = relay.transform.InferType()(mod)
mutated_mod['func_8367'] = func_8367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8367_call = mutated_mod.get_global_var('func_8367')
call_8368 = func_8367_call()
output = call_8368
func_8369 = relay.Function([], output)
mutated_mod['func_8369'] = func_8369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_8400 = func_3085_call()
call_8401 = func_3085_call()
func_2036_call = mod.get_global_var('func_2036')
func_2038_call = mutated_mod.get_global_var('func_2038')
call_8406 = relay.TupleGetItem(func_2036_call(), 0)
call_8407 = relay.TupleGetItem(func_2038_call(), 0)
func_1708_call = mod.get_global_var('func_1708')
func_1711_call = mutated_mod.get_global_var('func_1711')
var_8415 = relay.var("var_8415", dtype = "float64", shape = (1, 288))#candidate|8415|(1, 288)|var|float64
call_8414 = relay.TupleGetItem(func_1708_call(relay.reshape(var_8415.astype('float64'), [9, 4, 8])), 1)
call_8416 = relay.TupleGetItem(func_1711_call(relay.reshape(var_8415.astype('float64'), [9, 4, 8])), 1)
output = relay.Tuple([call_8400,call_8406,call_8414,var_8415,])
output2 = relay.Tuple([call_8401,call_8407,call_8416,var_8415,])
func_8417 = relay.Function([var_8415,], output)
mod['func_8417'] = func_8417
mod = relay.transform.InferType()(mod)
var_8418 = relay.var("var_8418", dtype = "float64", shape = (1, 288))#candidate|8418|(1, 288)|var|float64
output = func_8417(var_8418)
func_8419 = relay.Function([var_8418], output)
mutated_mod['func_8419'] = func_8419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4147_call = mod.get_global_var('func_4147')
func_4148_call = mutated_mod.get_global_var('func_4148')
call_8421 = relay.TupleGetItem(func_4147_call(), 2)
call_8422 = relay.TupleGetItem(func_4148_call(), 2)
output = call_8421
output2 = call_8422
func_8428 = relay.Function([], output)
mod['func_8428'] = func_8428
mod = relay.transform.InferType()(mod)
mutated_mod['func_8428'] = func_8428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8428_call = mutated_mod.get_global_var('func_8428')
call_8429 = func_8428_call()
output = call_8429
func_8430 = relay.Function([], output)
mutated_mod['func_8430'] = func_8430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6563_call = mod.get_global_var('func_6563')
func_6565_call = mutated_mod.get_global_var('func_6565')
call_8466 = func_6563_call()
call_8467 = func_6563_call()
var_8474 = relay.var("var_8474", dtype = "float64", shape = (9, 12, 8))#candidate|8474|(9, 12, 8)|var|float64
bop_8475 = relay.logical_and(call_8466.astype('bool'), var_8474.astype('bool')) # shape=(9, 12, 8)
bop_8478 = relay.logical_and(call_8467.astype('bool'), var_8474.astype('bool')) # shape=(9, 12, 8)
uop_8486 = relay.asin(call_8466.astype('float32')) # shape=(9, 1, 8)
uop_8488 = relay.asin(call_8467.astype('float32')) # shape=(9, 1, 8)
output = relay.Tuple([bop_8475,uop_8486,])
output2 = relay.Tuple([bop_8478,uop_8488,])
func_8508 = relay.Function([var_8474,], output)
mod['func_8508'] = func_8508
mod = relay.transform.InferType()(mod)
var_8509 = relay.var("var_8509", dtype = "float64", shape = (9, 12, 8))#candidate|8509|(9, 12, 8)|var|float64
output = func_8508(var_8509)
func_8510 = relay.Function([var_8509], output)
mutated_mod['func_8510'] = func_8510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7899_call = mod.get_global_var('func_7899')
func_7901_call = mutated_mod.get_global_var('func_7901')
call_8517 = relay.TupleGetItem(func_7899_call(), 0)
call_8518 = relay.TupleGetItem(func_7901_call(), 0)
func_1720_call = mod.get_global_var('func_1720')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_8522 = func_1720_call()
call_8523 = func_1720_call()
output = relay.Tuple([call_8517,call_8522,])
output2 = relay.Tuple([call_8518,call_8523,])
func_8549 = relay.Function([], output)
mod['func_8549'] = func_8549
mod = relay.transform.InferType()(mod)
output = func_8549()
func_8550 = relay.Function([], output)
mutated_mod['func_8550'] = func_8550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4578_call = mod.get_global_var('func_4578')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_8576 = func_4578_call()
call_8577 = func_4578_call()
output = call_8576
output2 = call_8577
func_8582 = relay.Function([], output)
mod['func_8582'] = func_8582
mod = relay.transform.InferType()(mod)
mutated_mod['func_8582'] = func_8582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8582_call = mutated_mod.get_global_var('func_8582')
call_8583 = func_8582_call()
output = call_8583
func_8584 = relay.Function([], output)
mutated_mod['func_8584'] = func_8584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2499_call = mod.get_global_var('func_2499')
func_2500_call = mutated_mod.get_global_var('func_2500')
call_8652 = func_2499_call()
call_8653 = func_2499_call()
output = relay.Tuple([call_8652,])
output2 = relay.Tuple([call_8653,])
func_8656 = relay.Function([], output)
mod['func_8656'] = func_8656
mod = relay.transform.InferType()(mod)
output = func_8656()
func_8657 = relay.Function([], output)
mutated_mod['func_8657'] = func_8657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5648_call = mod.get_global_var('func_5648')
func_5649_call = mutated_mod.get_global_var('func_5649')
call_8667 = func_5648_call()
call_8668 = func_5648_call()
func_7668_call = mod.get_global_var('func_7668')
func_7669_call = mutated_mod.get_global_var('func_7669')
call_8691 = relay.TupleGetItem(func_7668_call(), 0)
call_8692 = relay.TupleGetItem(func_7669_call(), 0)
var_8693 = relay.var("var_8693", dtype = "bool", shape = (9, 6, 8))#candidate|8693|(9, 6, 8)|var|bool
bop_8694 = relay.mod(call_8667.astype('float32'), var_8693.astype('float32')) # shape=(9, 6, 8)
bop_8697 = relay.mod(call_8668.astype('float32'), var_8693.astype('float32')) # shape=(9, 6, 8)
func_2612_call = mod.get_global_var('func_2612')
func_2618_call = mutated_mod.get_global_var('func_2618')
var_8703 = relay.var("var_8703", dtype = "int16", shape = (80,))#candidate|8703|(80,)|var|int16
const_8704 = relay.const([[-8.160222,-2.748125,-3.033075,-3.593317,3.317705,-0.935757,-6.591973,-5.305899,0.002879,2.178621],[1.757177,-8.916345,7.511459,-4.329404,1.908198,-6.442914,-3.751472,7.803712,4.099739,5.269406],[-6.075055,-5.738358,6.927280,3.902327,8.326960,-9.934547,7.481154,-0.669816,-7.696404,0.514346],[7.788535,4.010251,-0.805999,7.581773,-1.089748,-8.974494,-1.054794,5.100752,8.142630,-2.955390],[6.571232,9.417059,5.016551,4.635542,-7.647811,3.649335,0.215396,-3.418096,0.523601,7.217475]], dtype = "float32")#candidate|8704|(5, 10)|const|float32
var_8705 = relay.var("var_8705", dtype = "float64", shape = (504,))#candidate|8705|(504,)|var|float64
call_8702 = relay.TupleGetItem(func_2612_call(relay.reshape(var_8703.astype('int16'), [8, 5, 2]), relay.reshape(var_8703.astype('int16'), [8, 5, 2]), relay.reshape(const_8704.astype('float32'), [50, 1]), relay.reshape(call_8691.astype('float32'), [200,]), relay.reshape(var_8705.astype('float64'), [504,]), ), 1)
call_8706 = relay.TupleGetItem(func_2618_call(relay.reshape(var_8703.astype('int16'), [8, 5, 2]), relay.reshape(var_8703.astype('int16'), [8, 5, 2]), relay.reshape(const_8704.astype('float32'), [50, 1]), relay.reshape(call_8691.astype('float32'), [200,]), relay.reshape(var_8705.astype('float64'), [504,]), ), 1)
func_6563_call = mod.get_global_var('func_6563')
func_6565_call = mutated_mod.get_global_var('func_6565')
call_8735 = func_6563_call()
call_8736 = func_6563_call()
output = relay.Tuple([call_8691,bop_8694,call_8702,var_8703,const_8704,var_8705,call_8735,])
output2 = relay.Tuple([call_8692,bop_8697,call_8706,var_8703,const_8704,var_8705,call_8736,])
func_8744 = relay.Function([var_8693,var_8703,var_8705,], output)
mod['func_8744'] = func_8744
mod = relay.transform.InferType()(mod)
var_8745 = relay.var("var_8745", dtype = "bool", shape = (9, 6, 8))#candidate|8745|(9, 6, 8)|var|bool
var_8746 = relay.var("var_8746", dtype = "int16", shape = (80,))#candidate|8746|(80,)|var|int16
var_8747 = relay.var("var_8747", dtype = "float64", shape = (504,))#candidate|8747|(504,)|var|float64
output = func_8744(var_8745,var_8746,var_8747,)
func_8748 = relay.Function([var_8745,var_8746,var_8747,], output)
mutated_mod['func_8748'] = func_8748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7087_call = mod.get_global_var('func_7087')
func_7089_call = mutated_mod.get_global_var('func_7089')
call_8812 = relay.TupleGetItem(func_7087_call(), 0)
call_8813 = relay.TupleGetItem(func_7089_call(), 0)
func_2612_call = mod.get_global_var('func_2612')
func_2618_call = mutated_mod.get_global_var('func_2618')
var_8818 = relay.var("var_8818", dtype = "int16", shape = (80,))#candidate|8818|(80,)|var|int16
var_8819 = relay.var("var_8819", dtype = "float32", shape = (50, 1))#candidate|8819|(50, 1)|var|float32
const_8820 = relay.const([-3.140606,3.042310,4.955145,-3.282728,-1.570413,6.158968,5.521626,8.386942,-7.803141,-2.537398,8.345737,-8.138894,-8.548340,-0.058038,-0.248318,4.899844,2.633168,7.155375,2.704233,2.569609,9.149423,-0.507863,-2.203249,9.447923,-6.530594,-1.359552,-9.165351,8.058261,9.945518,1.755256,6.960155,-9.296143,8.480066,4.421333,-3.482964,-5.639495,2.018695,-6.875069,2.700175,-9.844467,-8.652984,3.272196,6.402523,4.318418,6.854659,-2.824449,-1.857305,8.359831,5.239073,-2.654524,1.967509,2.608625,4.490743,-7.311397,2.267711,-4.371634,8.107898,9.374770,7.000161,1.385858,8.665900,5.516365,-9.744485,0.281883,7.218121,5.816709,-6.447939,3.776404,6.212007,-8.879881,-3.127724,-8.420017,6.780501,2.812958,-5.328669,0.416744,-9.445816,4.039948,4.396582,-5.360259,-9.283319,1.525216,6.847671,-6.041155,-7.279654,9.367665,-9.948430,-0.636179,3.502560,-9.509489,-1.885881,5.620074,-5.614223,9.190017,3.898224,-5.083449,-2.371926,6.704391,-7.868548,-5.907334,-5.018466,7.459038,8.949187,-9.635322,0.508074,-6.212425,-1.591808,4.787952,2.932112,-9.931399,-4.674868,-9.188847,-9.891576,-0.899389,-3.839907,6.333942,9.796976,4.908742,-1.652213,6.502675,-4.408676,6.932211,-6.331579,6.133593,-2.373314,-1.809162,-8.383454,7.696266,-7.502949,5.779341,-4.148508,-9.072759,7.899175,-9.342966,5.764858,-2.611061,7.135324,4.901580,-7.376331,2.530452,-5.888430,4.563560,6.870771,-8.886353,3.330883,-0.353803,-7.210775,6.441809,-9.518020,-3.158007,4.658302,2.392823,-2.969697,-8.355159,2.665837,8.288516,-4.245003,-1.553594,0.074163,5.906162,-9.411579,-7.135990,-9.860577,-5.480645,9.283800,3.219341,8.899974,-9.902688,1.168975,-4.334127,-3.814938,-3.267887,5.932292,-8.526744,1.024295,7.337152,4.589687,1.933622,5.909161,-8.386425,-0.829718,7.568288,-7.879503,7.703911,2.523520,-5.678616,-5.784166,-9.320269,8.371753,-7.886565,-9.722040,-9.028505,-3.219045,-6.406866,-9.457004,-7.663337,-2.017141,-9.932766,0.831699,-0.352119], dtype = "float32")#candidate|8820|(200,)|const|float32
var_8821 = relay.var("var_8821", dtype = "float64", shape = (504,))#candidate|8821|(504,)|var|float64
call_8817 = relay.TupleGetItem(func_2612_call(relay.reshape(var_8818.astype('int16'), [8, 5, 2]), relay.reshape(var_8818.astype('int16'), [8, 5, 2]), relay.reshape(var_8819.astype('float32'), [50, 1]), relay.reshape(const_8820.astype('float32'), [200,]), relay.reshape(var_8821.astype('float64'), [504,]), ), 3)
call_8822 = relay.TupleGetItem(func_2618_call(relay.reshape(var_8818.astype('int16'), [8, 5, 2]), relay.reshape(var_8818.astype('int16'), [8, 5, 2]), relay.reshape(var_8819.astype('float32'), [50, 1]), relay.reshape(const_8820.astype('float32'), [200,]), relay.reshape(var_8821.astype('float64'), [504,]), ), 3)
output = relay.Tuple([call_8812,call_8817,var_8818,var_8819,const_8820,var_8821,])
output2 = relay.Tuple([call_8813,call_8822,var_8818,var_8819,const_8820,var_8821,])
func_8838 = relay.Function([var_8818,var_8819,var_8821,], output)
mod['func_8838'] = func_8838
mod = relay.transform.InferType()(mod)
mutated_mod['func_8838'] = func_8838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8838_call = mutated_mod.get_global_var('func_8838')
var_8840 = relay.var("var_8840", dtype = "int16", shape = (80,))#candidate|8840|(80,)|var|int16
var_8841 = relay.var("var_8841", dtype = "float32", shape = (50, 1))#candidate|8841|(50, 1)|var|float32
var_8842 = relay.var("var_8842", dtype = "float64", shape = (504,))#candidate|8842|(504,)|var|float64
call_8839 = func_8838_call(var_8840,var_8841,var_8842,)
output = call_8839
func_8843 = relay.Function([var_8840,var_8841,var_8842,], output)
mutated_mod['func_8843'] = func_8843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1720_call = mod.get_global_var('func_1720')
func_1721_call = mutated_mod.get_global_var('func_1721')
call_8947 = func_1720_call()
call_8948 = func_1720_call()
var_8966 = relay.var("var_8966", dtype = "float32", shape = (100, 2))#candidate|8966|(100, 2)|var|float32
bop_8967 = relay.floor_mod(call_8947.astype('float32'), relay.reshape(var_8966.astype('float32'), relay.shape_of(call_8947))) # shape=(100, 2)
bop_8970 = relay.floor_mod(call_8948.astype('float32'), relay.reshape(var_8966.astype('float32'), relay.shape_of(call_8948))) # shape=(100, 2)
func_2368_call = mod.get_global_var('func_2368')
func_2370_call = mutated_mod.get_global_var('func_2370')
var_8972 = relay.var("var_8972", dtype = "float32", shape = (1232,))#candidate|8972|(1232,)|var|float32
call_8971 = relay.TupleGetItem(func_2368_call(relay.reshape(var_8972.astype('float32'), [11, 7, 16])), 0)
call_8973 = relay.TupleGetItem(func_2370_call(relay.reshape(var_8972.astype('float32'), [11, 7, 16])), 0)
func_5470_call = mod.get_global_var('func_5470')
func_5471_call = mutated_mod.get_global_var('func_5471')
call_8974 = relay.TupleGetItem(func_5470_call(), 0)
call_8975 = relay.TupleGetItem(func_5471_call(), 0)
func_7899_call = mod.get_global_var('func_7899')
func_7901_call = mutated_mod.get_global_var('func_7901')
call_8977 = relay.TupleGetItem(func_7899_call(), 1)
call_8978 = relay.TupleGetItem(func_7901_call(), 1)
uop_8993 = relay.asinh(bop_8967.astype('float32')) # shape=(100, 2)
uop_8995 = relay.asinh(bop_8970.astype('float32')) # shape=(100, 2)
uop_8996 = relay.asin(uop_8993.astype('float32')) # shape=(100, 2)
uop_8998 = relay.asin(uop_8995.astype('float32')) # shape=(100, 2)
output = relay.Tuple([call_8971,var_8972,call_8974,call_8977,uop_8996,])
output2 = relay.Tuple([call_8973,var_8972,call_8975,call_8978,uop_8998,])
func_9002 = relay.Function([var_8966,var_8972,], output)
mod['func_9002'] = func_9002
mod = relay.transform.InferType()(mod)
mutated_mod['func_9002'] = func_9002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9002_call = mutated_mod.get_global_var('func_9002')
var_9004 = relay.var("var_9004", dtype = "float32", shape = (100, 2))#candidate|9004|(100, 2)|var|float32
var_9005 = relay.var("var_9005", dtype = "float32", shape = (1232,))#candidate|9005|(1232,)|var|float32
call_9003 = func_9002_call(var_9004,var_9005,)
output = call_9003
func_9006 = relay.Function([var_9004,var_9005,], output)
mutated_mod['func_9006'] = func_9006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4625_call = mod.get_global_var('func_4625')
func_4627_call = mutated_mod.get_global_var('func_4627')
call_9170 = relay.TupleGetItem(func_4625_call(), 0)
call_9171 = relay.TupleGetItem(func_4627_call(), 0)
output = call_9170
output2 = call_9171
func_9172 = relay.Function([], output)
mod['func_9172'] = func_9172
mod = relay.transform.InferType()(mod)
mutated_mod['func_9172'] = func_9172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9172_call = mutated_mod.get_global_var('func_9172')
call_9173 = func_9172_call()
output = call_9173
func_9174 = relay.Function([], output)
mutated_mod['func_9174'] = func_9174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5295_call = mod.get_global_var('func_5295')
func_5297_call = mutated_mod.get_global_var('func_5297')
call_9187 = func_5295_call()
call_9188 = func_5295_call()
output = call_9187
output2 = call_9188
func_9205 = relay.Function([], output)
mod['func_9205'] = func_9205
mod = relay.transform.InferType()(mod)
output = func_9205()
func_9206 = relay.Function([], output)
mutated_mod['func_9206'] = func_9206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3829_call = mod.get_global_var('func_3829')
func_3830_call = mutated_mod.get_global_var('func_3830')
call_9228 = relay.TupleGetItem(func_3829_call(), 0)
call_9229 = relay.TupleGetItem(func_3830_call(), 0)
func_4988_call = mod.get_global_var('func_4988')
func_4990_call = mutated_mod.get_global_var('func_4990')
call_9232 = relay.TupleGetItem(func_4988_call(), 0)
call_9233 = relay.TupleGetItem(func_4990_call(), 0)
output = relay.Tuple([call_9228,call_9232,])
output2 = relay.Tuple([call_9229,call_9233,])
func_9234 = relay.Function([], output)
mod['func_9234'] = func_9234
mod = relay.transform.InferType()(mod)
mutated_mod['func_9234'] = func_9234
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9234_call = mutated_mod.get_global_var('func_9234')
call_9235 = func_9234_call()
output = call_9235
func_9236 = relay.Function([], output)
mutated_mod['func_9236'] = func_9236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7550_call = mod.get_global_var('func_7550')
func_7551_call = mutated_mod.get_global_var('func_7551')
call_9240 = func_7550_call()
call_9241 = func_7550_call()
output = relay.Tuple([call_9240,])
output2 = relay.Tuple([call_9241,])
func_9247 = relay.Function([], output)
mod['func_9247'] = func_9247
mod = relay.transform.InferType()(mod)
mutated_mod['func_9247'] = func_9247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9247_call = mutated_mod.get_global_var('func_9247')
call_9248 = func_9247_call()
output = call_9248
func_9249 = relay.Function([], output)
mutated_mod['func_9249'] = func_9249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1671_call = mod.get_global_var('func_1671')
func_1673_call = mutated_mod.get_global_var('func_1673')
call_9270 = func_1671_call()
call_9271 = func_1671_call()
output = relay.Tuple([call_9270,])
output2 = relay.Tuple([call_9271,])
func_9273 = relay.Function([], output)
mod['func_9273'] = func_9273
mod = relay.transform.InferType()(mod)
mutated_mod['func_9273'] = func_9273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9273_call = mutated_mod.get_global_var('func_9273')
call_9274 = func_9273_call()
output = call_9274
func_9275 = relay.Function([], output)
mutated_mod['func_9275'] = func_9275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5807_call = mod.get_global_var('func_5807')
func_5809_call = mutated_mod.get_global_var('func_5809')
call_9300 = func_5807_call()
call_9301 = func_5807_call()
output = relay.Tuple([call_9300,])
output2 = relay.Tuple([call_9301,])
func_9302 = relay.Function([], output)
mod['func_9302'] = func_9302
mod = relay.transform.InferType()(mod)
mutated_mod['func_9302'] = func_9302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9302_call = mutated_mod.get_global_var('func_9302')
call_9303 = func_9302_call()
output = call_9303
func_9304 = relay.Function([], output)
mutated_mod['func_9304'] = func_9304
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9332 = relay.var("var_9332", dtype = "float64", shape = (6, 5, 9))#candidate|9332|(6, 5, 9)|var|float64
uop_9333 = relay.acos(var_9332.astype('float64')) # shape=(6, 5, 9)
func_2177_call = mod.get_global_var('func_2177')
func_2179_call = mutated_mod.get_global_var('func_2179')
call_9340 = func_2177_call()
call_9341 = func_2177_call()
output = relay.Tuple([uop_9333,call_9340,])
output2 = relay.Tuple([uop_9333,call_9341,])
func_9350 = relay.Function([var_9332,], output)
mod['func_9350'] = func_9350
mod = relay.transform.InferType()(mod)
mutated_mod['func_9350'] = func_9350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9351 = relay.var("var_9351", dtype = "float64", shape = (6, 5, 9))#candidate|9351|(6, 5, 9)|var|float64
func_9350_call = mutated_mod.get_global_var('func_9350')
call_9352 = func_9350_call(var_9351)
output = call_9352
func_9353 = relay.Function([var_9351], output)
mutated_mod['func_9353'] = func_9353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3713_call = mod.get_global_var('func_3713')
func_3714_call = mutated_mod.get_global_var('func_3714')
call_9373 = relay.TupleGetItem(func_3713_call(), 1)
call_9374 = relay.TupleGetItem(func_3714_call(), 1)
output = relay.Tuple([call_9373,])
output2 = relay.Tuple([call_9374,])
func_9382 = relay.Function([], output)
mod['func_9382'] = func_9382
mod = relay.transform.InferType()(mod)
output = func_9382()
func_9383 = relay.Function([], output)
mutated_mod['func_9383'] = func_9383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9386 = relay.var("var_9386", dtype = "float64", shape = (10, 9, 11))#candidate|9386|(10, 9, 11)|var|float64
uop_9387 = relay.acosh(var_9386.astype('float64')) # shape=(10, 9, 11)
output = relay.Tuple([uop_9387,])
output2 = relay.Tuple([uop_9387,])
func_9413 = relay.Function([var_9386,], output)
mod['func_9413'] = func_9413
mod = relay.transform.InferType()(mod)
var_9414 = relay.var("var_9414", dtype = "float64", shape = (10, 9, 11))#candidate|9414|(10, 9, 11)|var|float64
output = func_9413(var_9414)
func_9415 = relay.Function([var_9414], output)
mutated_mod['func_9415'] = func_9415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8096_call = mod.get_global_var('func_8096')
func_8097_call = mutated_mod.get_global_var('func_8097')
call_9461 = func_8096_call()
call_9462 = func_8096_call()
func_3989_call = mod.get_global_var('func_3989')
func_3991_call = mutated_mod.get_global_var('func_3991')
call_9478 = relay.TupleGetItem(func_3989_call(), 0)
call_9479 = relay.TupleGetItem(func_3991_call(), 0)
output = relay.Tuple([call_9461,call_9478,])
output2 = relay.Tuple([call_9462,call_9479,])
func_9480 = relay.Function([], output)
mod['func_9480'] = func_9480
mod = relay.transform.InferType()(mod)
output = func_9480()
func_9481 = relay.Function([], output)
mutated_mod['func_9481'] = func_9481
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9506 = relay.const([[[-4.721465,0.898012,7.224962,-1.952970,4.347077,3.401605,-9.777473,4.202920,1.595507,8.076513,-8.943856],[3.907011,-5.058018,9.042136,9.687421,-7.274278,7.787667,1.495036,-1.729372,-8.462009,0.171612,9.130352],[-2.031685,-7.339073,7.175972,-4.860163,-2.369364,5.680571,-1.569082,-5.345144,9.510230,3.452421,-9.090129],[9.784509,-6.636530,-2.099711,-5.209199,-3.510792,-5.927180,-9.602660,-1.489164,1.914690,8.467170,5.774835],[8.634329,1.290213,-9.157561,0.620742,0.877362,8.657162,2.438670,3.024694,2.482384,-2.985152,5.311195],[0.953425,-6.280441,-3.106798,4.736590,2.096816,2.710793,8.238852,3.269546,-3.533423,-0.955673,-8.412644],[2.551010,6.505970,2.512123,4.253916,-8.584779,-8.709497,3.343873,-2.406890,-5.588363,-0.331248,-1.149087],[0.924523,-2.819200,-6.648755,3.079284,-9.205709,1.955345,1.314572,-5.778389,2.401936,2.633849,5.297995],[-1.214849,4.446526,2.221647,-4.590961,-1.689673,4.673793,6.614294,4.213575,-1.589633,1.383066,7.822454],[0.797490,0.041186,-5.275253,-8.728861,-1.439755,-8.399420,-8.250504,1.954373,1.019214,-3.536130,-1.584367],[4.515861,8.476009,-3.795667,5.681107,9.353329,8.309694,2.208556,-7.817037,4.434027,-1.112556,-6.766768],[8.813904,1.041876,0.607083,1.232602,6.039412,2.689835,-5.242759,2.239935,8.280910,-5.607817,-5.315774],[0.561559,-0.804346,2.348677,-0.391095,7.199783,6.350231,-2.720994,-0.822862,-1.450508,-4.924435,-5.891671],[5.253827,-9.640727,4.525488,8.275592,-3.872493,-9.604942,6.103262,0.231022,3.698671,6.233232,8.466832]],[[-1.143440,2.221836,4.665833,-0.336219,9.815179,-8.220474,1.081552,-1.220865,0.640965,2.182931,4.984182],[7.671242,-9.359660,3.666654,1.027141,7.946348,3.545642,-4.515361,2.127522,-7.829539,0.852990,-9.528160],[-3.352103,2.117738,-7.410135,9.291343,-3.950979,-5.547256,-2.404828,-5.646801,9.417434,6.589238,6.267042],[2.341025,-4.412826,5.446260,-6.940616,-5.651689,-2.393732,-2.995828,-2.141722,9.635270,-9.541395,0.768611],[0.115691,-0.639265,-1.509828,0.398022,-5.309820,-1.917686,6.583049,-4.743972,6.008455,-0.751380,-1.307693],[-2.115442,6.376403,5.670867,-7.338500,-3.416093,1.444189,-9.715390,-5.353019,0.972440,-2.865317,1.266200],[8.512767,-4.752540,9.615531,-5.274752,1.348649,-1.890837,-7.781027,8.340533,5.053212,1.205702,-8.320703],[-4.997605,1.606199,5.609816,9.957346,9.690797,-6.456091,7.561580,1.125447,-4.939022,8.501711,4.685948],[-3.405131,-3.090850,-0.617339,-6.575079,6.904349,0.615531,-1.028780,-0.532850,7.920314,-0.391740,8.359922],[8.927001,-8.631977,-4.568019,8.543182,9.818284,-0.304277,6.264186,8.949447,7.690197,-2.965300,-5.337976],[-6.976992,-8.260026,-1.338790,5.519330,-2.477039,-6.962424,-1.910743,-7.782711,-3.398638,-8.057343,9.864753],[1.979615,0.430522,1.027770,3.430801,1.942462,3.606786,-5.177986,-2.502198,4.253999,-8.172614,2.764328],[-7.782957,-2.482760,-0.698718,6.471204,-2.740111,-3.680874,-5.043915,4.361274,3.715198,1.347448,-4.764525],[9.633260,4.664934,-0.995467,-0.552328,9.549478,1.773639,-1.216898,-4.962403,-3.930010,-3.638311,-1.390267]],[[-2.884691,8.933579,-2.955834,-6.537449,-8.934302,-8.905577,2.047386,8.957226,-6.252302,-7.296609,5.823930],[2.531050,4.852524,-3.318946,5.553326,-8.326039,4.189833,8.040471,-1.683770,-5.413869,6.706012,-6.908985],[3.287970,6.433108,-3.848171,-9.141535,-5.585198,2.232568,7.430999,7.111477,3.695292,-6.707466,6.197685],[-0.690891,-7.961089,-3.195340,0.216292,-1.685475,3.645706,2.166611,6.812212,4.369459,9.465103,1.831255],[-6.079582,9.990454,-2.815122,-5.988423,-9.378646,4.257925,-9.606867,-6.738300,8.810905,-0.585994,-2.697795],[-3.138195,2.916946,3.294816,5.345523,9.269659,-4.921939,1.249635,1.423762,-4.981851,-2.197452,-9.215739],[-8.053169,5.569667,1.093599,-4.701228,1.050623,9.311315,-1.136366,2.230828,-8.138953,4.394031,-4.907124],[8.063065,4.644025,9.393463,-8.737797,-4.842567,-1.421730,-8.516931,3.561014,-9.246424,3.382377,-9.754956],[-6.907782,2.556657,-8.293095,1.165157,5.853992,-0.182121,5.327034,1.612388,5.258909,-2.907373,4.542056],[9.743504,8.916432,8.474143,-8.694658,-7.994257,7.957795,1.459193,-8.197526,-6.106421,9.822877,-8.970736],[-9.605685,-4.087262,1.287792,-5.235573,7.134970,-5.647379,3.318285,-0.978511,6.370587,-0.642493,-8.715609],[-2.827319,2.303068,8.875445,-3.248011,2.367414,1.476683,-2.893688,-0.330463,7.824868,5.862697,-5.155910],[6.767888,-6.396990,7.594820,3.885953,-1.578281,-3.490430,2.085701,-2.544072,-6.424810,-4.683339,-1.947142],[-5.055781,1.320395,-0.275328,3.437222,4.801525,4.126948,3.451192,8.063184,3.309585,5.995576,2.464778]],[[8.889900,-7.533128,1.322944,5.154079,1.959125,-6.207041,5.500782,8.463618,2.044972,1.498400,-2.072801],[5.059982,2.388819,9.469733,-5.891526,5.980680,6.027190,6.077593,1.051351,-9.625737,9.077374,7.854298],[3.863353,8.893863,-6.420347,-2.330169,-1.956531,-2.428015,-8.541032,-2.706711,-3.986682,-7.346486,4.290337],[-5.794699,-6.345931,3.661345,2.668087,-6.671972,-6.938166,5.388931,-9.358887,9.390812,7.831125,-7.744541],[-8.385808,-4.182557,0.450584,-4.298146,1.906887,9.593277,7.190016,7.017939,6.872406,1.683299,3.286202],[-8.504721,-6.380978,-3.101729,7.250496,6.635631,3.892390,-7.143294,-8.908479,1.005171,9.431088,2.005884],[-8.996535,0.779529,-3.410987,2.473463,9.972749,7.061838,6.124885,6.067836,1.479128,-6.643110,8.975464],[7.583325,7.992602,5.644509,6.471597,7.629457,9.121107,4.055348,-1.921517,3.291670,2.936506,2.242050],[7.600528,0.234228,-5.501120,0.165867,2.045766,6.946136,-1.125082,7.303726,-6.523782,3.278695,-8.077735],[7.678804,3.002043,-4.921487,-7.223859,1.841082,9.723970,-2.229809,8.336157,5.080596,-5.556251,7.235932],[9.360707,-3.580084,-5.901776,2.406395,-0.742406,1.048815,9.481791,-8.468141,4.875663,7.956849,2.335027],[-6.589383,-6.784335,1.502337,6.644562,5.341224,5.947704,-5.197503,8.847003,-0.821875,-3.584045,4.148360],[-1.271631,2.082953,4.417540,-3.561790,-9.317423,1.538612,-2.214429,7.204444,-3.562193,-0.100611,-7.929818],[9.701506,-8.178519,-6.107083,1.213504,-5.290363,1.070680,3.966064,7.462780,7.214670,0.043584,-8.112971]],[[1.443781,6.065089,-8.235091,-9.300631,-4.293024,-7.370744,6.454092,5.965869,-4.317517,-1.296770,-6.555447],[-8.570712,2.794160,5.173303,2.350044,-6.827700,-6.601916,-4.355412,7.053658,1.312915,-6.626907,-8.735249],[-0.376764,-0.289187,-4.658395,6.169215,-2.623304,-5.516805,0.013510,-2.916063,5.128398,-9.443162,-1.158060],[-8.667537,8.156564,7.719121,6.799217,8.915751,-4.254040,-7.589880,6.933734,5.707360,8.335339,9.480890],[0.382420,3.143423,0.431357,-2.743299,-3.543997,0.882915,1.031498,5.694855,8.964949,-5.135675,-5.087188],[-6.064073,-3.209018,-2.123954,6.418830,0.371197,5.561176,9.113236,-7.836911,8.831204,-1.312708,-7.038001],[4.108337,-0.933970,-6.068901,-9.935963,2.234909,-5.801054,-5.478375,9.851372,6.295968,2.693420,-0.967146],[6.434274,-4.770334,5.252809,8.888045,-0.967908,-3.550154,4.869541,-2.987856,9.862368,-4.030904,8.836046],[-5.430103,-7.454015,7.594783,0.957327,-7.788721,-2.430083,8.149486,8.713892,9.278950,1.400834,-3.004795],[7.696584,3.070663,-3.795208,-3.571828,-0.575042,5.294738,-9.667222,-8.426812,-5.493592,-6.189751,-8.280264],[-9.042042,2.535938,9.497315,3.327615,6.953300,-7.921735,-7.535121,9.157867,6.954915,5.616809,-3.568513],[7.917061,5.850454,-4.787312,7.487698,8.269748,-1.402962,0.536602,-5.837662,-1.128482,8.048431,-3.273879],[5.903229,6.046100,9.967432,7.816362,-6.960156,3.461519,-0.336638,-0.333533,-0.939476,-1.184952,-5.904187],[-8.238472,-1.940014,-8.006577,-6.948956,4.443726,-8.461311,-7.298282,-3.032402,-3.296906,-0.593463,-5.621447]],[[8.698717,-7.564043,6.570855,-9.138685,9.260217,-7.172572,4.164068,9.384459,2.231671,-8.362966,7.645251],[6.525172,-1.557908,9.540260,7.747888,-1.576778,-0.024113,-4.015099,1.368435,1.689400,-2.031992,-4.218192],[-1.508282,1.922419,2.354438,-3.891066,-9.611225,-2.044994,2.018612,5.682612,2.177990,6.287760,9.837125],[7.096350,-4.908072,8.563261,-6.721139,2.402561,0.502781,-9.132587,-3.130572,-5.987427,8.589614,3.232231],[-3.957727,1.380799,-5.395291,3.976515,2.874771,-6.121013,5.785729,-9.917108,-7.996657,-2.977250,-8.622335],[-9.756687,4.261421,0.005827,2.597960,4.193080,2.609279,6.373201,5.459410,4.890283,-5.179227,1.922622],[2.570960,8.631535,4.677876,-1.885771,2.430154,-1.646191,3.705701,3.536362,-9.279203,-2.198133,4.145236],[-2.903733,-1.021021,4.192693,2.731529,-8.664341,-5.834869,-9.546776,3.076099,4.747324,6.670387,-3.325400],[4.274355,5.418949,-5.477333,-6.329101,-7.141452,8.687516,-6.645653,9.595445,1.607077,5.482193,3.675468],[1.585248,-8.800682,4.753956,-8.416540,-4.662675,3.705476,2.603132,6.826587,-8.788817,-1.495750,-4.387980],[-4.109609,1.090515,6.006152,-1.085631,-5.459934,6.042174,-7.609329,2.850708,-0.889405,8.345754,0.473236],[-3.667975,-7.150247,-4.800876,-1.276285,3.830322,-6.012157,-9.838727,2.518541,1.380750,-3.301089,-2.575049],[6.094250,4.736855,9.296343,-8.765289,8.381259,6.297683,0.036006,2.336101,-9.995540,-3.624304,6.004520],[-3.076224,9.939474,-3.406329,5.951981,2.939000,-4.666069,-2.812392,2.989181,9.607178,7.699470,-5.509484]],[[-0.047328,-7.941398,-8.920152,-9.516880,4.204925,1.825099,-2.494328,-6.107258,-9.794803,-6.610258,-1.428174],[4.369279,0.078203,8.428515,3.212324,0.312895,1.714868,8.582624,4.851334,2.691527,-7.796374,0.152179],[-2.847368,-6.753397,6.615313,-8.256615,-6.225220,0.001623,-6.069354,-6.278046,-8.572849,2.783271,-4.976509],[-1.816712,-7.717583,-5.631286,-0.538511,8.258514,-3.948923,2.702697,8.634858,9.641882,3.322308,0.672597],[1.261025,-1.473456,-0.564188,5.323281,-9.231407,-4.458202,0.710844,3.601661,-3.178731,2.458733,2.427220],[8.118507,-7.462672,-2.334665,8.811930,7.473692,4.047651,6.452305,1.915926,-0.769187,-6.380695,5.001093],[-8.223959,4.479632,6.469763,0.941437,2.287538,7.284323,3.782393,-3.508012,-9.540941,-5.976939,1.494280],[6.853062,-1.528933,-3.509378,-3.435947,3.664546,-8.237233,7.660179,0.651142,-9.650973,9.767234,-4.313367],[7.401715,-2.859940,-1.555035,-6.480501,-8.988786,-3.308863,6.954267,8.003057,-4.800463,-4.401300,8.559093],[5.612753,-0.667534,6.208138,3.552289,4.164365,-0.250002,-0.016048,-4.101874,-7.129164,-8.601892,9.648372],[7.669152,0.346501,2.296228,4.680558,-1.110306,3.920408,-2.830153,-2.926167,-1.608671,6.286399,0.360735],[7.134437,-8.061762,-1.295611,3.153082,-6.062425,-4.653211,-9.274716,-3.937822,-3.216286,-2.382986,6.537793],[9.754500,1.917946,2.352359,-6.965616,-1.133592,-2.867703,-5.732491,-3.820259,8.220023,-1.456571,-7.528792],[7.694139,-0.410742,5.139864,-4.489229,-6.671145,5.319889,6.095975,-2.550465,6.766322,-5.631175,1.741608]],[[6.132992,-9.396630,-5.301627,-6.873468,8.725338,8.583566,-8.278171,4.410225,-2.903763,-4.447709,2.925179],[-0.289172,0.976711,-2.519155,-1.600651,-0.619745,0.756984,-1.403156,-8.433075,7.990010,-7.770656,1.511496],[3.015788,1.250083,-1.187190,8.873658,-2.972954,0.792869,-8.905104,4.901923,5.294402,-0.611082,-4.046927],[5.280212,9.723010,-3.362254,9.646995,-4.800959,-3.454792,-9.015713,3.138040,-8.326052,-3.659024,-5.604038],[-6.248874,9.095341,1.775278,-8.423260,-7.479483,-3.692719,-7.298891,1.789332,5.556031,5.470939,-3.152607],[-1.247344,2.869519,6.546480,2.070587,-3.663318,3.336024,8.967677,3.320812,-8.009647,8.862712,-3.617241],[8.727915,-3.380013,4.351129,7.840361,5.325876,-5.302762,-5.423816,-8.130613,1.375876,6.040844,-3.172743],[3.107654,4.809345,4.956389,7.667205,-4.666019,-2.071209,9.412112,-4.133686,5.908478,-0.749980,3.937308],[1.324461,-4.051699,-9.304721,7.565768,7.139890,9.055371,-4.880409,0.330243,-1.543100,-1.334140,-4.398998],[-7.532082,-1.079661,6.879039,9.900420,-9.908065,-1.650512,3.706199,-4.558615,-8.112215,-5.029007,-1.481034],[-2.638482,-1.880184,-7.956468,8.241732,-4.997731,1.307164,5.327584,3.904269,9.443218,7.346257,0.500198],[6.823413,4.451942,9.508388,8.081631,-4.454987,8.769982,-9.152654,-3.648019,6.292434,0.755526,8.805921],[0.824859,-4.703853,-1.398887,-6.905694,-1.772069,-1.782209,0.417324,0.756915,3.788615,9.616756,-1.505173],[-0.595267,1.363523,1.731052,0.222827,-9.769453,-2.838128,2.748746,-3.096766,-6.391958,1.794857,9.243495]],[[-0.613393,7.885723,-8.637775,-5.119932,-8.445111,0.485274,-4.284315,4.185067,-7.572051,-8.634764,-8.134648],[9.879558,-7.473066,6.586240,-6.273360,-9.436652,-0.721371,9.643772,-4.465392,8.992722,-8.346220,5.927252],[-9.717825,-9.138281,-7.206481,2.532540,4.522978,0.423801,-3.500676,1.315002,3.348610,0.904122,-3.191259],[7.519777,-9.336903,0.915562,8.453143,-8.022272,6.207366,-3.987904,2.665443,-3.139942,7.518432,-2.239862],[9.133518,-8.583058,-2.817173,-3.019028,-0.100615,6.032464,-7.672337,-0.437928,8.801056,7.390624,1.183073],[-4.368858,5.164091,1.384348,0.093294,-9.352616,-3.813176,8.263468,-3.854548,2.114671,3.135962,-8.083539],[1.439943,-0.856633,3.865475,-6.458124,5.270081,3.582800,8.000895,4.965140,8.183752,6.658307,2.890516],[-9.040265,-4.763328,-4.169432,-9.339908,-0.048643,8.638367,5.105827,-5.015081,-8.314882,-1.005958,2.745806],[-5.745629,-4.142353,-0.449609,9.012403,4.855268,-9.264922,1.455771,7.505206,7.672676,-9.656337,-5.658300],[2.850161,3.624959,2.241235,1.267173,1.091616,5.300869,4.173854,-4.909229,7.996104,-3.019481,4.866754],[4.727301,-9.270386,-2.028446,1.220731,-4.715082,-2.644831,-9.039835,6.583408,-7.092550,-8.287464,2.234633],[0.430177,-4.574604,6.805048,-0.923575,9.337363,2.278177,-0.511568,-4.405734,7.009975,-2.127389,-8.435158],[0.632934,1.397171,-5.618446,9.798489,8.967752,2.554719,-1.620239,6.393175,-9.338094,-4.742916,-4.313410],[3.904960,-4.768550,9.134993,-4.014493,-9.819361,2.611387,9.410707,2.288628,3.277903,-2.803461,-5.728214]]], dtype = "float64")#candidate|9506|(9, 14, 11)|const|float64
uop_9507 = relay.erf(const_9506.astype('float64')) # shape=(9, 14, 11)
output = relay.Tuple([uop_9507,])
output2 = relay.Tuple([uop_9507,])
func_9509 = relay.Function([], output)
mod['func_9509'] = func_9509
mod = relay.transform.InferType()(mod)
output = func_9509()
func_9510 = relay.Function([], output)
mutated_mod['func_9510'] = func_9510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2713_call = mod.get_global_var('func_2713')
func_2714_call = mutated_mod.get_global_var('func_2714')
call_9569 = relay.TupleGetItem(func_2713_call(), 0)
call_9570 = relay.TupleGetItem(func_2714_call(), 0)
func_5324_call = mod.get_global_var('func_5324')
func_5327_call = mutated_mod.get_global_var('func_5327')
var_9606 = relay.var("var_9606", dtype = "float64", shape = (360,))#candidate|9606|(360,)|var|float64
call_9605 = relay.TupleGetItem(func_5324_call(relay.reshape(var_9606.astype('float64'), [9, 5, 8])), 0)
call_9607 = relay.TupleGetItem(func_5327_call(relay.reshape(var_9606.astype('float64'), [9, 5, 8])), 0)
output = relay.Tuple([call_9569,call_9605,var_9606,])
output2 = relay.Tuple([call_9570,call_9607,var_9606,])
func_9611 = relay.Function([var_9606,], output)
mod['func_9611'] = func_9611
mod = relay.transform.InferType()(mod)
mutated_mod['func_9611'] = func_9611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9612 = relay.var("var_9612", dtype = "float64", shape = (360,))#candidate|9612|(360,)|var|float64
func_9611_call = mutated_mod.get_global_var('func_9611')
call_9613 = func_9611_call(var_9612)
output = call_9613
func_9614 = relay.Function([var_9612], output)
mutated_mod['func_9614'] = func_9614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3085_call = mod.get_global_var('func_3085')
func_3087_call = mutated_mod.get_global_var('func_3087')
call_9616 = func_3085_call()
call_9617 = func_3085_call()
func_4578_call = mod.get_global_var('func_4578')
func_4580_call = mutated_mod.get_global_var('func_4580')
call_9627 = func_4578_call()
call_9628 = func_4578_call()
output = relay.Tuple([call_9616,call_9627,])
output2 = relay.Tuple([call_9617,call_9628,])
func_9631 = relay.Function([], output)
mod['func_9631'] = func_9631
mod = relay.transform.InferType()(mod)
mutated_mod['func_9631'] = func_9631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9631_call = mutated_mod.get_global_var('func_9631')
call_9632 = func_9631_call()
output = call_9632
func_9633 = relay.Function([], output)
mutated_mod['func_9633'] = func_9633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6246_call = mod.get_global_var('func_6246')
func_6247_call = mutated_mod.get_global_var('func_6247')
call_9641 = relay.TupleGetItem(func_6246_call(), 0)
call_9642 = relay.TupleGetItem(func_6247_call(), 0)
func_9002_call = mod.get_global_var('func_9002')
func_9006_call = mutated_mod.get_global_var('func_9006')
var_9644 = relay.var("var_9644", dtype = "float32", shape = (200,))#candidate|9644|(200,)|var|float32
var_9645 = relay.var("var_9645", dtype = "float32", shape = (1232,))#candidate|9645|(1232,)|var|float32
call_9643 = relay.TupleGetItem(func_9002_call(relay.reshape(var_9644.astype('float32'), [100, 2]), relay.reshape(var_9645.astype('float32'), [1232,]), ), 0)
call_9646 = relay.TupleGetItem(func_9006_call(relay.reshape(var_9644.astype('float32'), [100, 2]), relay.reshape(var_9645.astype('float32'), [1232,]), ), 0)
output = relay.Tuple([call_9641,call_9643,var_9644,var_9645,])
output2 = relay.Tuple([call_9642,call_9646,var_9644,var_9645,])
func_9649 = relay.Function([var_9644,var_9645,], output)
mod['func_9649'] = func_9649
mod = relay.transform.InferType()(mod)
mutated_mod['func_9649'] = func_9649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9649_call = mutated_mod.get_global_var('func_9649')
var_9651 = relay.var("var_9651", dtype = "float32", shape = (200,))#candidate|9651|(200,)|var|float32
var_9652 = relay.var("var_9652", dtype = "float32", shape = (1232,))#candidate|9652|(1232,)|var|float32
call_9650 = func_9649_call(var_9651,var_9652,)
output = call_9650
func_9653 = relay.Function([var_9651,var_9652,], output)
mutated_mod['func_9653'] = func_9653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3542_call = mod.get_global_var('func_3542')
func_3544_call = mutated_mod.get_global_var('func_3544')
call_9655 = relay.TupleGetItem(func_3542_call(), 0)
call_9656 = relay.TupleGetItem(func_3544_call(), 0)
var_9664 = relay.var("var_9664", dtype = "float64", shape = (9, 13, 8))#candidate|9664|(9, 13, 8)|var|float64
bop_9665 = relay.less_equal(call_9655.astype('bool'), var_9664.astype('bool')) # shape=(9, 13, 8)
bop_9668 = relay.less_equal(call_9656.astype('bool'), var_9664.astype('bool')) # shape=(9, 13, 8)
output = bop_9665
output2 = bop_9668
func_9670 = relay.Function([var_9664,], output)
mod['func_9670'] = func_9670
mod = relay.transform.InferType()(mod)
mutated_mod['func_9670'] = func_9670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9671 = relay.var("var_9671", dtype = "float64", shape = (9, 13, 8))#candidate|9671|(9, 13, 8)|var|float64
func_9670_call = mutated_mod.get_global_var('func_9670')
call_9672 = func_9670_call(var_9671)
output = call_9672
func_9673 = relay.Function([var_9671], output)
mutated_mod['func_9673'] = func_9673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1745_call = mod.get_global_var('func_1745')
func_1746_call = mutated_mod.get_global_var('func_1746')
call_9689 = relay.TupleGetItem(func_1745_call(), 0)
call_9690 = relay.TupleGetItem(func_1746_call(), 0)
func_8428_call = mod.get_global_var('func_8428')
func_8430_call = mutated_mod.get_global_var('func_8430')
call_9696 = func_8428_call()
call_9697 = func_8428_call()
output = relay.Tuple([call_9689,call_9696,])
output2 = relay.Tuple([call_9690,call_9697,])
func_9708 = relay.Function([], output)
mod['func_9708'] = func_9708
mod = relay.transform.InferType()(mod)
mutated_mod['func_9708'] = func_9708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9708_call = mutated_mod.get_global_var('func_9708')
call_9709 = func_9708_call()
output = call_9709
func_9710 = relay.Function([], output)
mutated_mod['func_9710'] = func_9710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3183_call = mod.get_global_var('func_3183')
func_3184_call = mutated_mod.get_global_var('func_3184')
call_9725 = relay.TupleGetItem(func_3183_call(), 2)
call_9726 = relay.TupleGetItem(func_3184_call(), 2)
output = call_9725
output2 = call_9726
func_9746 = relay.Function([], output)
mod['func_9746'] = func_9746
mod = relay.transform.InferType()(mod)
output = func_9746()
func_9747 = relay.Function([], output)
mutated_mod['func_9747'] = func_9747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8096_call = mod.get_global_var('func_8096')
func_8097_call = mutated_mod.get_global_var('func_8097')
call_9786 = func_8096_call()
call_9787 = func_8096_call()
func_4092_call = mod.get_global_var('func_4092')
func_4096_call = mutated_mod.get_global_var('func_4096')
var_9805 = relay.var("var_9805", dtype = "int8", shape = ())#candidate|9805|()|var|int8
var_9806 = relay.var("var_9806", dtype = "int8", shape = (1024,))#candidate|9806|(1024,)|var|int8
var_9807 = relay.var("var_9807", dtype = "uint16", shape = (1430,))#candidate|9807|(1430,)|var|uint16
call_9804 = relay.TupleGetItem(func_4092_call(relay.reshape(var_9805.astype('int8'), []), relay.reshape(var_9806.astype('int8'), [8, 8, 16]), relay.reshape(var_9807.astype('uint16'), [1430,]), ), 0)
call_9808 = relay.TupleGetItem(func_4096_call(relay.reshape(var_9805.astype('int8'), []), relay.reshape(var_9806.astype('int8'), [8, 8, 16]), relay.reshape(var_9807.astype('uint16'), [1430,]), ), 0)
func_5390_call = mod.get_global_var('func_5390')
func_5391_call = mutated_mod.get_global_var('func_5391')
call_9815 = func_5390_call()
call_9816 = func_5390_call()
func_5118_call = mod.get_global_var('func_5118')
func_5119_call = mutated_mod.get_global_var('func_5119')
call_9819 = func_5118_call()
call_9820 = func_5118_call()
uop_9838 = relay.acosh(var_9806.astype('float32')) # shape=(1024,)
bop_9852 = relay.floor_divide(call_9815.astype('float32'), var_9807.astype('float32')) # shape=(11, 8, 1430)
bop_9855 = relay.floor_divide(call_9816.astype('float32'), var_9807.astype('float32')) # shape=(11, 8, 1430)
bop_9857 = relay.right_shift(uop_9838.astype('uint64'), relay.reshape(call_9804.astype('uint64'), relay.shape_of(uop_9838))) # shape=(1024,)
bop_9860 = relay.right_shift(uop_9838.astype('uint64'), relay.reshape(call_9808.astype('uint64'), relay.shape_of(uop_9838))) # shape=(1024,)
bop_9864 = relay.power(bop_9857.astype('float64'), relay.reshape(uop_9838.astype('float64'), relay.shape_of(bop_9857))) # shape=(1024,)
bop_9867 = relay.power(bop_9860.astype('float64'), relay.reshape(uop_9838.astype('float64'), relay.shape_of(bop_9860))) # shape=(1024,)
output = relay.Tuple([call_9786,var_9805,call_9819,bop_9852,bop_9864,])
output2 = relay.Tuple([call_9787,var_9805,call_9820,bop_9855,bop_9867,])
func_9873 = relay.Function([var_9805,var_9806,var_9807,], output)
mod['func_9873'] = func_9873
mod = relay.transform.InferType()(mod)
var_9874 = relay.var("var_9874", dtype = "int8", shape = ())#candidate|9874|()|var|int8
var_9875 = relay.var("var_9875", dtype = "int8", shape = (1024,))#candidate|9875|(1024,)|var|int8
var_9876 = relay.var("var_9876", dtype = "uint16", shape = (1430,))#candidate|9876|(1430,)|var|uint16
output = func_9873(var_9874,var_9875,var_9876,)
func_9877 = relay.Function([var_9874,var_9875,var_9876,], output)
mutated_mod['func_9877'] = func_9877
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9888 = relay.var("var_9888", dtype = "float64", shape = (14, 13, 15))#candidate|9888|(14, 13, 15)|var|float64
var_9889 = relay.var("var_9889", dtype = "float64", shape = (14, 13, 15))#candidate|9889|(14, 13, 15)|var|float64
bop_9890 = relay.multiply(var_9888.astype('float64'), relay.reshape(var_9889.astype('float64'), relay.shape_of(var_9888))) # shape=(14, 13, 15)
output = bop_9890
output2 = bop_9890
func_9893 = relay.Function([var_9888,var_9889,], output)
mod['func_9893'] = func_9893
mod = relay.transform.InferType()(mod)
var_9894 = relay.var("var_9894", dtype = "float64", shape = (14, 13, 15))#candidate|9894|(14, 13, 15)|var|float64
var_9895 = relay.var("var_9895", dtype = "float64", shape = (14, 13, 15))#candidate|9895|(14, 13, 15)|var|float64
output = func_9893(var_9894,var_9895,)
func_9896 = relay.Function([var_9894,var_9895,], output)
mutated_mod['func_9896'] = func_9896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9382_call = mod.get_global_var('func_9382')
func_9383_call = mutated_mod.get_global_var('func_9383')
call_9904 = relay.TupleGetItem(func_9382_call(), 0)
call_9905 = relay.TupleGetItem(func_9383_call(), 0)
func_6434_call = mod.get_global_var('func_6434')
func_6437_call = mutated_mod.get_global_var('func_6437')
var_9914 = relay.var("var_9914", dtype = "float32", shape = (704,))#candidate|9914|(704,)|var|float32
call_9913 = func_6434_call(relay.reshape(var_9914.astype('float32'), [11, 8, 8]))
call_9915 = func_6434_call(relay.reshape(var_9914.astype('float32'), [11, 8, 8]))
func_6364_call = mod.get_global_var('func_6364')
func_6368_call = mutated_mod.get_global_var('func_6368')
var_9921 = relay.var("var_9921", dtype = "uint16", shape = (18,))#candidate|9921|(18,)|var|uint16
var_9922 = relay.var("var_9922", dtype = "int32", shape = (234,))#candidate|9922|(234,)|var|int32
call_9920 = relay.TupleGetItem(func_6364_call(relay.reshape(var_9921.astype('uint16'), [18,]), relay.reshape(var_9922.astype('int32'), [234,]), ), 3)
call_9923 = relay.TupleGetItem(func_6368_call(relay.reshape(var_9921.astype('uint16'), [18,]), relay.reshape(var_9922.astype('int32'), [234,]), ), 3)
func_4887_call = mod.get_global_var('func_4887')
func_4889_call = mutated_mod.get_global_var('func_4889')
call_9926 = relay.TupleGetItem(func_4887_call(), 0)
call_9927 = relay.TupleGetItem(func_4889_call(), 0)
uop_9932 = relay.asin(call_9904.astype('float32')) # shape=(6, 3, 11)
uop_9934 = relay.asin(call_9905.astype('float32')) # shape=(6, 3, 11)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
const_9938 = relay.const([[-5.373642,-2.261888,5.972050,-1.787102],[6.912283,1.961541,-7.010864,4.439999],[-2.755830,5.478363,-4.444783,5.035080],[6.668011,-9.505087,-8.005849,7.130121],[-8.283803,3.034649,2.374270,5.383356],[-6.382402,-2.784767,6.521190,-9.065757],[-0.706965,-4.961052,7.836115,-7.578379],[-8.723887,-5.459239,4.471587,5.779993],[6.075483,4.979752,1.476796,6.969048],[5.022498,-7.497933,9.199538,7.183286],[-3.261308,-4.763260,1.552855,-3.757356],[8.902001,-2.439568,-7.895866,-9.066224],[-7.113937,-1.971238,-1.665885,-4.637485],[5.769821,6.363882,6.267641,3.629613],[-7.507721,2.443653,-7.001683,0.491591],[-6.419281,0.018377,0.421052,-9.371345],[1.118596,5.852790,-9.716937,-1.724148],[-4.495701,6.352788,-5.155936,4.803891],[-7.399229,-4.699042,-2.202449,9.680379],[1.719357,-1.200477,-5.171724,9.700244],[6.695107,-0.667250,-9.117119,-3.379745],[-3.109053,-9.709867,-3.507337,5.730128],[-1.449499,7.472683,4.763676,8.326206],[0.954768,7.879305,-1.511753,-7.643698],[-5.214485,6.485683,4.146835,0.827205],[5.397933,-0.457438,-0.930622,2.397586],[8.114448,2.484841,1.307157,6.388495],[-3.388164,-2.337175,3.756941,2.825821],[5.327522,-0.979119,-3.248893,-2.383936],[3.098397,4.759495,-8.858894,-6.977362],[6.745110,-3.142526,-1.472641,-5.710850],[7.357029,3.883499,9.153881,-7.631828],[-8.186607,1.750457,-9.456200,-7.175148],[-9.569053,5.596928,-6.298053,-7.148110],[-9.179283,-1.072777,-7.889288,9.701864],[-0.922530,0.481110,5.697049,-4.477233],[-3.164917,-0.162696,-3.798955,1.368131],[-8.428107,8.160484,-1.936975,6.725991],[7.098067,-7.888808,-5.676971,5.235711],[-2.435408,-6.954831,-6.025015,9.438834],[-1.531053,4.183954,3.773262,1.024173],[-4.181381,-6.003682,-4.663273,5.588848],[-8.808745,3.865351,9.583541,3.630109],[4.992589,-7.574548,-3.665461,4.978908],[0.978128,6.525948,6.976643,5.250673],[-1.147567,-7.988770,2.576615,-7.208859],[1.742397,-0.640915,-0.838247,5.012143],[2.248687,3.516942,7.720366,-1.728077],[6.948503,0.559318,-0.394420,-7.455899],[0.837283,2.864209,-6.265660,-9.776414]], dtype = "float32")#candidate|9938|(50, 4)|const|float32
call_9937 = relay.TupleGetItem(func_3508_call(relay.reshape(const_9938.astype('float32'), [200,])), 1)
call_9939 = relay.TupleGetItem(func_3510_call(relay.reshape(const_9938.astype('float32'), [200,])), 1)
func_4816_call = mod.get_global_var('func_4816')
func_4817_call = mutated_mod.get_global_var('func_4817')
call_9951 = func_4816_call()
call_9952 = func_4816_call()
output = relay.Tuple([call_9913,var_9914,call_9920,var_9921,var_9922,call_9926,uop_9932,call_9937,const_9938,call_9951,])
output2 = relay.Tuple([call_9915,var_9914,call_9923,var_9921,var_9922,call_9927,uop_9934,call_9939,const_9938,call_9952,])
func_9954 = relay.Function([var_9914,var_9921,var_9922,], output)
mod['func_9954'] = func_9954
mod = relay.transform.InferType()(mod)
mutated_mod['func_9954'] = func_9954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9954_call = mutated_mod.get_global_var('func_9954')
var_9956 = relay.var("var_9956", dtype = "float32", shape = (704,))#candidate|9956|(704,)|var|float32
var_9957 = relay.var("var_9957", dtype = "uint16", shape = (18,))#candidate|9957|(18,)|var|uint16
var_9958 = relay.var("var_9958", dtype = "int32", shape = (234,))#candidate|9958|(234,)|var|int32
call_9955 = func_9954_call(var_9956,var_9957,var_9958,)
output = call_9955
func_9959 = relay.Function([var_9956,var_9957,var_9958,], output)
mutated_mod['func_9959'] = func_9959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1251_call = mod.get_global_var('func_1251')
func_1252_call = mutated_mod.get_global_var('func_1252')
call_10087 = func_1251_call()
call_10088 = func_1251_call()
output = call_10087
output2 = call_10088
func_10117 = relay.Function([], output)
mod['func_10117'] = func_10117
mod = relay.transform.InferType()(mod)
output = func_10117()
func_10118 = relay.Function([], output)
mutated_mod['func_10118'] = func_10118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2816_call = mod.get_global_var('func_2816')
func_2818_call = mutated_mod.get_global_var('func_2818')
call_10149 = relay.TupleGetItem(func_2816_call(), 0)
call_10150 = relay.TupleGetItem(func_2818_call(), 0)
var_10169 = relay.var("var_10169", dtype = "float64", shape = (9, 7, 8))#candidate|10169|(9, 7, 8)|var|float64
bop_10170 = relay.bitwise_xor(call_10149.astype('uint8'), var_10169.astype('uint8')) # shape=(9, 7, 8)
bop_10173 = relay.bitwise_xor(call_10150.astype('uint8'), var_10169.astype('uint8')) # shape=(9, 7, 8)
var_10176 = relay.var("var_10176", dtype = "float64", shape = (9, 6, 8))#candidate|10176|(9, 6, 8)|var|float64
bop_10177 = relay.less(call_10149.astype('bool'), var_10176.astype('bool')) # shape=(9, 6, 8)
bop_10180 = relay.less(call_10150.astype('bool'), var_10176.astype('bool')) # shape=(9, 6, 8)
output = relay.Tuple([bop_10170,bop_10177,])
output2 = relay.Tuple([bop_10173,bop_10180,])
func_10183 = relay.Function([var_10169,var_10176,], output)
mod['func_10183'] = func_10183
mod = relay.transform.InferType()(mod)
mutated_mod['func_10183'] = func_10183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10183_call = mutated_mod.get_global_var('func_10183')
var_10185 = relay.var("var_10185", dtype = "float64", shape = (9, 7, 8))#candidate|10185|(9, 7, 8)|var|float64
var_10186 = relay.var("var_10186", dtype = "float64", shape = (9, 6, 8))#candidate|10186|(9, 6, 8)|var|float64
call_10184 = func_10183_call(var_10185,var_10186,)
output = call_10184
func_10187 = relay.Function([var_10185,var_10186,], output)
mutated_mod['func_10187'] = func_10187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5898_call = mod.get_global_var('func_5898')
func_5899_call = mutated_mod.get_global_var('func_5899')
call_10189 = relay.TupleGetItem(func_5898_call(), 7)
call_10190 = relay.TupleGetItem(func_5899_call(), 7)
uop_10222 = relay.asin(call_10189.astype('float64')) # shape=(9, 8, 9)
uop_10224 = relay.asin(call_10190.astype('float64')) # shape=(9, 8, 9)
uop_10252 = relay.exp(uop_10222.astype('float32')) # shape=(9, 8, 9)
uop_10254 = relay.exp(uop_10224.astype('float32')) # shape=(9, 8, 9)
func_6329_call = mod.get_global_var('func_6329')
func_6331_call = mutated_mod.get_global_var('func_6331')
call_10257 = func_6329_call()
call_10258 = func_6329_call()
uop_10267 = relay.sigmoid(uop_10252.astype('float64')) # shape=(9, 8, 9)
uop_10269 = relay.sigmoid(uop_10254.astype('float64')) # shape=(9, 8, 9)
output = relay.Tuple([call_10257,uop_10267,])
output2 = relay.Tuple([call_10258,uop_10269,])
func_10292 = relay.Function([], output)
mod['func_10292'] = func_10292
mod = relay.transform.InferType()(mod)
mutated_mod['func_10292'] = func_10292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10292_call = mutated_mod.get_global_var('func_10292')
call_10293 = func_10292_call()
output = call_10293
func_10294 = relay.Function([], output)
mutated_mod['func_10294'] = func_10294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9382_call = mod.get_global_var('func_9382')
func_9383_call = mutated_mod.get_global_var('func_9383')
call_10322 = relay.TupleGetItem(func_9382_call(), 0)
call_10323 = relay.TupleGetItem(func_9383_call(), 0)
output = relay.Tuple([call_10322,])
output2 = relay.Tuple([call_10323,])
func_10329 = relay.Function([], output)
mod['func_10329'] = func_10329
mod = relay.transform.InferType()(mod)
mutated_mod['func_10329'] = func_10329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10329_call = mutated_mod.get_global_var('func_10329')
call_10330 = func_10329_call()
output = call_10330
func_10331 = relay.Function([], output)
mutated_mod['func_10331'] = func_10331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4625_call = mod.get_global_var('func_4625')
func_4627_call = mutated_mod.get_global_var('func_4627')
call_10347 = relay.TupleGetItem(func_4625_call(), 0)
call_10348 = relay.TupleGetItem(func_4627_call(), 0)
func_8306_call = mod.get_global_var('func_8306')
func_8310_call = mutated_mod.get_global_var('func_8310')
var_10352 = relay.var("var_10352", dtype = "int64", shape = (20, 108))#candidate|10352|(20, 108)|var|int64
var_10353 = relay.var("var_10353", dtype = "float32", shape = (1, 200))#candidate|10353|(1, 200)|var|float32
call_10351 = relay.TupleGetItem(func_8306_call(relay.reshape(var_10352.astype('int64'), [16, 15, 9]), relay.reshape(var_10353.astype('float32'), [200,]), ), 5)
call_10354 = relay.TupleGetItem(func_8310_call(relay.reshape(var_10352.astype('int64'), [16, 15, 9]), relay.reshape(var_10353.astype('float32'), [200,]), ), 5)
func_1097_call = mod.get_global_var('func_1097')
func_1098_call = mutated_mod.get_global_var('func_1098')
call_10391 = func_1097_call()
call_10392 = func_1097_call()
uop_10404 = relay.sigmoid(var_10352.astype('float32')) # shape=(20, 108)
output = relay.Tuple([call_10347,call_10351,var_10353,call_10391,uop_10404,])
output2 = relay.Tuple([call_10348,call_10354,var_10353,call_10392,uop_10404,])
F = relay.Function([var_10352,var_10353,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10352,var_10353,], output2)
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
