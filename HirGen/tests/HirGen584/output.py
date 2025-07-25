import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_1091 = relay.const([[[-2.996333,-0.196781,-2.744391,-9.619531,-8.567672,-2.047962,9.828323,-7.579716,5.501662,2.429473,8.226502,-1.698191,3.155564,-5.227551,4.136123,3.723308]],[[-2.433771,2.161857,-1.990470,-3.997958,8.342364,1.357628,-3.757311,-3.510066,-9.519755,4.017592,8.428799,-7.413321,2.672122,-1.356978,-0.873924,-9.238572]],[[-9.773436,-5.723945,9.099134,0.897836,3.555165,-4.449832,4.669933,3.668108,-4.938353,1.183230,7.778054,-4.096614,-0.905199,1.241340,-0.966707,9.150538]],[[7.626074,5.334097,3.538252,1.041272,-0.006181,-8.259339,-7.324772,6.729203,-1.434641,5.666310,-6.349967,-4.805725,-4.480081,-6.422072,-3.084572,1.617266]],[[3.029016,-5.568588,-0.986299,2.747461,1.006893,-4.497638,4.292191,5.964961,-3.285058,4.527653,-5.626080,1.333342,-3.819801,-9.069382,-8.345228,-3.146520]],[[-9.613071,-5.763537,0.350724,5.214322,1.412954,-4.009241,8.694236,1.210391,-3.552918,2.581054,-5.354672,-6.919399,-0.677151,9.377890,-0.721646,-1.628086]],[[2.873280,7.654116,-7.448108,8.472517,-0.588762,-0.314407,4.268305,2.783224,3.293961,0.275176,-1.911989,-5.382599,-0.018783,1.996476,8.739196,0.218169]],[[-7.814277,6.434652,-3.365335,-7.105923,7.837913,-0.716585,-8.822865,-8.189897,-2.105037,-9.308440,0.842561,1.525138,-9.442153,9.067204,-6.308585,-5.189103]],[[6.234598,5.724020,3.868351,9.509506,7.228987,7.347573,1.504779,2.952948,5.023703,-7.590493,-6.147568,-5.665482,-2.893728,-4.347060,6.256332,2.032081]],[[6.564124,-0.114730,7.728999,4.614454,6.348867,-6.983526,-4.074988,5.975090,8.283875,2.867261,4.717853,6.426083,7.811897,1.943322,-2.864580,7.580013]],[[1.461516,-0.546550,2.514856,7.213654,1.916934,-4.511725,2.053696,0.974609,5.287003,-4.883580,5.299158,3.874377,-4.354293,8.123074,1.719298,-5.565580]],[[-7.606213,1.683095,-6.804168,-2.966813,2.809716,5.383835,-0.491408,5.375132,5.248644,8.246437,0.681540,5.395973,5.168707,2.297146,-5.040239,0.856094]],[[-2.806320,-7.216565,-3.051822,-8.895410,1.814612,-6.683079,9.621749,-2.264316,-0.198517,4.234715,-1.688091,6.693893,4.006467,-2.585078,-5.528600,-7.347138]],[[6.688021,1.292159,1.368144,7.126257,9.516838,0.356509,5.131506,-9.792011,5.170214,-4.166058,-1.443925,7.198909,-8.459011,6.220538,5.978883,7.275380]],[[9.922263,-4.586899,1.630734,9.409987,-9.696880,8.825718,-9.977293,0.965044,7.418064,6.558345,1.514730,8.603322,5.916385,-9.994180,-4.013101,9.613084]]], dtype = "float64")#candidate|1091|(15, 1, 16)|const|float64
uop_1092 = relay.asin(const_1091.astype('float64')) # shape=(15, 1, 16)
uop_1095 = relay.tan(const_1091.astype('float64')) # shape=(15, 1, 16)
output = relay.Tuple([uop_1092,uop_1095,])
output2 = relay.Tuple([uop_1092,uop_1095,])
func_1109 = relay.Function([], output)
mod['func_1109'] = func_1109
mod = relay.transform.InferType()(mod)
output = func_1109()
func_1110 = relay.Function([], output)
mutated_mod['func_1110'] = func_1110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1144 = relay.TupleGetItem(func_1109_call(), 1)
call_1145 = relay.TupleGetItem(func_1110_call(), 1)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1150 = relay.TupleGetItem(func_1109_call(), 1)
call_1151 = relay.TupleGetItem(func_1110_call(), 1)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1157 = relay.TupleGetItem(func_1109_call(), 1)
call_1158 = relay.TupleGetItem(func_1110_call(), 1)
output = relay.Tuple([call_1144,call_1150,call_1157,])
output2 = relay.Tuple([call_1145,call_1151,call_1158,])
func_1159 = relay.Function([], output)
mod['func_1159'] = func_1159
mod = relay.transform.InferType()(mod)
output = func_1159()
func_1160 = relay.Function([], output)
mutated_mod['func_1160'] = func_1160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1175 = relay.TupleGetItem(func_1159_call(), 1)
call_1176 = relay.TupleGetItem(func_1160_call(), 1)
var_1180 = relay.var("var_1180", dtype = "float64", shape = (15, 15, 16))#candidate|1180|(15, 15, 16)|var|float64
bop_1181 = relay.greater(call_1175.astype('bool'), var_1180.astype('bool')) # shape=(15, 15, 16)
bop_1184 = relay.greater(call_1176.astype('bool'), var_1180.astype('bool')) # shape=(15, 15, 16)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1187 = relay.TupleGetItem(func_1159_call(), 2)
call_1188 = relay.TupleGetItem(func_1160_call(), 2)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1191 = relay.TupleGetItem(func_1109_call(), 0)
call_1192 = relay.TupleGetItem(func_1110_call(), 0)
output = relay.Tuple([bop_1181,call_1187,call_1191,])
output2 = relay.Tuple([bop_1184,call_1188,call_1192,])
func_1195 = relay.Function([var_1180,], output)
mod['func_1195'] = func_1195
mod = relay.transform.InferType()(mod)
var_1196 = relay.var("var_1196", dtype = "float64", shape = (15, 15, 16))#candidate|1196|(15, 15, 16)|var|float64
output = func_1195(var_1196)
func_1197 = relay.Function([var_1196], output)
mutated_mod['func_1197'] = func_1197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1215 = relay.TupleGetItem(func_1109_call(), 1)
call_1216 = relay.TupleGetItem(func_1110_call(), 1)
var_1218 = relay.var("var_1218", dtype = "float64", shape = (15, 1, 16))#candidate|1218|(15, 1, 16)|var|float64
bop_1219 = relay.less(call_1215.astype('bool'), relay.reshape(var_1218.astype('bool'), relay.shape_of(call_1215))) # shape=(15, 1, 16)
bop_1222 = relay.less(call_1216.astype('bool'), relay.reshape(var_1218.astype('bool'), relay.shape_of(call_1216))) # shape=(15, 1, 16)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1224 = relay.TupleGetItem(func_1109_call(), 1)
call_1225 = relay.TupleGetItem(func_1110_call(), 1)
bop_1229 = relay.bitwise_and(bop_1219.astype('int8'), relay.reshape(var_1218.astype('int8'), relay.shape_of(bop_1219))) # shape=(15, 1, 16)
bop_1232 = relay.bitwise_and(bop_1222.astype('int8'), relay.reshape(var_1218.astype('int8'), relay.shape_of(bop_1222))) # shape=(15, 1, 16)
output = relay.Tuple([call_1224,bop_1229,])
output2 = relay.Tuple([call_1225,bop_1232,])
func_1235 = relay.Function([var_1218,], output)
mod['func_1235'] = func_1235
mod = relay.transform.InferType()(mod)
mutated_mod['func_1235'] = func_1235
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1236 = relay.var("var_1236", dtype = "float64", shape = (15, 1, 16))#candidate|1236|(15, 1, 16)|var|float64
func_1235_call = mutated_mod.get_global_var('func_1235')
call_1237 = func_1235_call(var_1236)
output = call_1237
func_1238 = relay.Function([var_1236], output)
mutated_mod['func_1238'] = func_1238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1245 = relay.TupleGetItem(func_1159_call(), 2)
call_1246 = relay.TupleGetItem(func_1160_call(), 2)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1256 = relay.TupleGetItem(func_1159_call(), 2)
call_1257 = relay.TupleGetItem(func_1160_call(), 2)
func_1235_call = mod.get_global_var('func_1235')
func_1238_call = mutated_mod.get_global_var('func_1238')
call_1262 = relay.TupleGetItem(func_1235_call(relay.reshape(call_1245.astype('float64'), [15, 1, 16])), 0)
call_1263 = relay.TupleGetItem(func_1238_call(relay.reshape(call_1245.astype('float64'), [15, 1, 16])), 0)
output = relay.Tuple([call_1245,call_1256,call_1262,])
output2 = relay.Tuple([call_1246,call_1257,call_1263,])
func_1274 = relay.Function([], output)
mod['func_1274'] = func_1274
mod = relay.transform.InferType()(mod)
output = func_1274()
func_1275 = relay.Function([], output)
mutated_mod['func_1275'] = func_1275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1274_call = mod.get_global_var('func_1274')
func_1275_call = mutated_mod.get_global_var('func_1275')
call_1356 = relay.TupleGetItem(func_1274_call(), 2)
call_1357 = relay.TupleGetItem(func_1275_call(), 2)
output = relay.Tuple([call_1356,])
output2 = relay.Tuple([call_1357,])
func_1381 = relay.Function([], output)
mod['func_1381'] = func_1381
mod = relay.transform.InferType()(mod)
output = func_1381()
func_1382 = relay.Function([], output)
mutated_mod['func_1382'] = func_1382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_1415 = relay.TupleGetItem(func_1381_call(), 0)
call_1416 = relay.TupleGetItem(func_1382_call(), 0)
output = call_1415
output2 = call_1416
func_1417 = relay.Function([], output)
mod['func_1417'] = func_1417
mod = relay.transform.InferType()(mod)
output = func_1417()
func_1418 = relay.Function([], output)
mutated_mod['func_1418'] = func_1418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_1447 = func_1417_call()
call_1448 = func_1417_call()
output = call_1447
output2 = call_1448
func_1470 = relay.Function([], output)
mod['func_1470'] = func_1470
mod = relay.transform.InferType()(mod)
output = func_1470()
func_1471 = relay.Function([], output)
mutated_mod['func_1471'] = func_1471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1516 = relay.TupleGetItem(func_1159_call(), 2)
call_1517 = relay.TupleGetItem(func_1160_call(), 2)
uop_1519 = relay.atanh(call_1516.astype('float64')) # shape=(15, 1, 16)
uop_1521 = relay.atanh(call_1517.astype('float64')) # shape=(15, 1, 16)
output = relay.Tuple([uop_1519,])
output2 = relay.Tuple([uop_1521,])
func_1524 = relay.Function([], output)
mod['func_1524'] = func_1524
mod = relay.transform.InferType()(mod)
output = func_1524()
func_1525 = relay.Function([], output)
mutated_mod['func_1525'] = func_1525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_1557 = func_1470_call()
call_1558 = func_1470_call()
output = relay.Tuple([call_1557,])
output2 = relay.Tuple([call_1558,])
func_1561 = relay.Function([], output)
mod['func_1561'] = func_1561
mod = relay.transform.InferType()(mod)
mutated_mod['func_1561'] = func_1561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mutated_mod.get_global_var('func_1561')
call_1562 = func_1561_call()
output = call_1562
func_1563 = relay.Function([], output)
mutated_mod['func_1563'] = func_1563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_1573 = func_1470_call()
call_1574 = func_1470_call()
output = relay.Tuple([call_1573,])
output2 = relay.Tuple([call_1574,])
func_1585 = relay.Function([], output)
mod['func_1585'] = func_1585
mod = relay.transform.InferType()(mod)
mutated_mod['func_1585'] = func_1585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1585_call = mutated_mod.get_global_var('func_1585')
call_1586 = func_1585_call()
output = call_1586
func_1587 = relay.Function([], output)
mutated_mod['func_1587'] = func_1587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1588 = relay.TupleGetItem(func_1109_call(), 0)
call_1589 = relay.TupleGetItem(func_1110_call(), 0)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1590 = relay.TupleGetItem(func_1159_call(), 0)
call_1591 = relay.TupleGetItem(func_1160_call(), 0)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_1604 = relay.TupleGetItem(func_1561_call(), 0)
call_1605 = relay.TupleGetItem(func_1563_call(), 0)
output = relay.Tuple([call_1588,call_1590,call_1604,])
output2 = relay.Tuple([call_1589,call_1591,call_1605,])
func_1608 = relay.Function([], output)
mod['func_1608'] = func_1608
mod = relay.transform.InferType()(mod)
output = func_1608()
func_1609 = relay.Function([], output)
mutated_mod['func_1609'] = func_1609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_1625 = relay.TupleGetItem(func_1608_call(), 0)
call_1626 = relay.TupleGetItem(func_1609_call(), 0)
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_1643 = func_1470_call()
call_1644 = func_1470_call()
output = relay.Tuple([call_1625,call_1643,])
output2 = relay.Tuple([call_1626,call_1644,])
func_1650 = relay.Function([], output)
mod['func_1650'] = func_1650
mod = relay.transform.InferType()(mod)
mutated_mod['func_1650'] = func_1650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1650_call = mutated_mod.get_global_var('func_1650')
call_1651 = func_1650_call()
output = call_1651
func_1652 = relay.Function([], output)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1653 = relay.TupleGetItem(func_1159_call(), 1)
call_1654 = relay.TupleGetItem(func_1160_call(), 1)
uop_1657 = relay.cos(call_1653.astype('float32')) # shape=(15, 1, 16)
uop_1659 = relay.cos(call_1654.astype('float32')) # shape=(15, 1, 16)
uop_1665 = relay.sinh(uop_1657.astype('float32')) # shape=(15, 1, 16)
uop_1667 = relay.sinh(uop_1659.astype('float32')) # shape=(15, 1, 16)
bop_1674 = relay.less_equal(call_1653.astype('bool'), relay.reshape(uop_1657.astype('bool'), relay.shape_of(call_1653))) # shape=(15, 1, 16)
bop_1677 = relay.less_equal(call_1654.astype('bool'), relay.reshape(uop_1659.astype('bool'), relay.shape_of(call_1654))) # shape=(15, 1, 16)
uop_1678 = relay.acos(uop_1665.astype('float64')) # shape=(15, 1, 16)
uop_1680 = relay.acos(uop_1667.astype('float64')) # shape=(15, 1, 16)
output = relay.Tuple([bop_1674,uop_1678,])
output2 = relay.Tuple([bop_1677,uop_1680,])
func_1683 = relay.Function([], output)
mod['func_1683'] = func_1683
mod = relay.transform.InferType()(mod)
output = func_1683()
func_1684 = relay.Function([], output)
mutated_mod['func_1684'] = func_1684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_1690 = func_1417_call()
call_1691 = func_1417_call()
func_1235_call = mod.get_global_var('func_1235')
func_1238_call = mutated_mod.get_global_var('func_1238')
call_1695 = relay.TupleGetItem(func_1235_call(relay.reshape(call_1690.astype('float64'), [15, 1, 16])), 0)
call_1696 = relay.TupleGetItem(func_1238_call(relay.reshape(call_1690.astype('float64'), [15, 1, 16])), 0)
output = relay.Tuple([call_1690,call_1695,])
output2 = relay.Tuple([call_1691,call_1696,])
func_1707 = relay.Function([], output)
mod['func_1707'] = func_1707
mod = relay.transform.InferType()(mod)
mutated_mod['func_1707'] = func_1707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mutated_mod.get_global_var('func_1707')
call_1708 = func_1707_call()
output = call_1708
func_1709 = relay.Function([], output)
mutated_mod['func_1709'] = func_1709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1683_call = mod.get_global_var('func_1683')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_1843 = relay.TupleGetItem(func_1683_call(), 0)
call_1844 = relay.TupleGetItem(func_1684_call(), 0)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_1845 = relay.TupleGetItem(func_1109_call(), 1)
call_1846 = relay.TupleGetItem(func_1110_call(), 1)
func_1524_call = mod.get_global_var('func_1524')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_1848 = relay.TupleGetItem(func_1524_call(), 0)
call_1849 = relay.TupleGetItem(func_1525_call(), 0)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1857 = relay.TupleGetItem(func_1159_call(), 0)
call_1858 = relay.TupleGetItem(func_1160_call(), 0)
output = relay.Tuple([call_1843,call_1845,call_1848,call_1857,])
output2 = relay.Tuple([call_1844,call_1846,call_1849,call_1858,])
func_1872 = relay.Function([], output)
mod['func_1872'] = func_1872
mod = relay.transform.InferType()(mod)
output = func_1872()
func_1873 = relay.Function([], output)
mutated_mod['func_1873'] = func_1873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_1992 = relay.TupleGetItem(func_1608_call(), 2)
call_1993 = relay.TupleGetItem(func_1609_call(), 2)
output = relay.Tuple([call_1992,])
output2 = relay.Tuple([call_1993,])
func_2006 = relay.Function([], output)
mod['func_2006'] = func_2006
mod = relay.transform.InferType()(mod)
mutated_mod['func_2006'] = func_2006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2006_call = mutated_mod.get_global_var('func_2006')
call_2007 = func_2006_call()
output = call_2007
func_2008 = relay.Function([], output)
mutated_mod['func_2008'] = func_2008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_2019 = func_1417_call()
call_2020 = func_1417_call()
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_2021 = relay.TupleGetItem(func_1381_call(), 0)
call_2022 = relay.TupleGetItem(func_1382_call(), 0)
uop_2023 = relay.log(call_2019.astype('float64')) # shape=(15, 1, 16)
uop_2025 = relay.log(call_2020.astype('float64')) # shape=(15, 1, 16)
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
call_2028 = relay.TupleGetItem(func_1650_call(), 1)
call_2029 = relay.TupleGetItem(func_1652_call(), 1)
output = relay.Tuple([call_2021,uop_2023,call_2028,])
output2 = relay.Tuple([call_2022,uop_2025,call_2029,])
func_2034 = relay.Function([], output)
mod['func_2034'] = func_2034
mod = relay.transform.InferType()(mod)
output = func_2034()
func_2035 = relay.Function([], output)
mutated_mod['func_2035'] = func_2035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_2066 = relay.TupleGetItem(func_1381_call(), 0)
call_2067 = relay.TupleGetItem(func_1382_call(), 0)
output = relay.Tuple([call_2066,])
output2 = relay.Tuple([call_2067,])
func_2076 = relay.Function([], output)
mod['func_2076'] = func_2076
mod = relay.transform.InferType()(mod)
output = func_2076()
func_2077 = relay.Function([], output)
mutated_mod['func_2077'] = func_2077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_2152 = relay.TupleGetItem(func_1608_call(), 0)
call_2153 = relay.TupleGetItem(func_1609_call(), 0)
output = relay.Tuple([call_2152,])
output2 = relay.Tuple([call_2153,])
func_2156 = relay.Function([], output)
mod['func_2156'] = func_2156
mod = relay.transform.InferType()(mod)
mutated_mod['func_2156'] = func_2156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2156_call = mutated_mod.get_global_var('func_2156')
call_2157 = func_2156_call()
output = call_2157
func_2158 = relay.Function([], output)
mutated_mod['func_2158'] = func_2158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2173 = relay.var("var_2173", dtype = "float32", shape = (2, 12, 15))#candidate|2173|(2, 12, 15)|var|float32
uop_2174 = relay.asinh(var_2173.astype('float32')) # shape=(2, 12, 15)
output = relay.Tuple([uop_2174,])
output2 = relay.Tuple([uop_2174,])
func_2177 = relay.Function([var_2173,], output)
mod['func_2177'] = func_2177
mod = relay.transform.InferType()(mod)
mutated_mod['func_2177'] = func_2177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2178 = relay.var("var_2178", dtype = "float32", shape = (2, 12, 15))#candidate|2178|(2, 12, 15)|var|float32
func_2177_call = mutated_mod.get_global_var('func_2177')
call_2179 = func_2177_call(var_2178)
output = call_2179
func_2180 = relay.Function([var_2178], output)
mutated_mod['func_2180'] = func_2180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_2212 = func_1470_call()
call_2213 = func_1470_call()
output = relay.Tuple([call_2212,])
output2 = relay.Tuple([call_2213,])
func_2223 = relay.Function([], output)
mod['func_2223'] = func_2223
mod = relay.transform.InferType()(mod)
output = func_2223()
func_2224 = relay.Function([], output)
mutated_mod['func_2224'] = func_2224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1683_call = mod.get_global_var('func_1683')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_2225 = relay.TupleGetItem(func_1683_call(), 1)
call_2226 = relay.TupleGetItem(func_1684_call(), 1)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
call_2246 = relay.TupleGetItem(func_1707_call(), 1)
call_2247 = relay.TupleGetItem(func_1709_call(), 1)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_2250 = relay.TupleGetItem(func_2006_call(), 0)
call_2251 = relay.TupleGetItem(func_2008_call(), 0)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_2252 = func_1417_call()
call_2253 = func_1417_call()
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_2271 = relay.TupleGetItem(func_1109_call(), 0)
call_2272 = relay.TupleGetItem(func_1110_call(), 0)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_2288 = relay.TupleGetItem(func_1109_call(), 1)
call_2289 = relay.TupleGetItem(func_1110_call(), 1)
func_2177_call = mod.get_global_var('func_2177')
func_2180_call = mutated_mod.get_global_var('func_2180')
var_2315 = relay.var("var_2315", dtype = "float32", shape = (360,))#candidate|2315|(360,)|var|float32
call_2314 = relay.TupleGetItem(func_2177_call(relay.reshape(var_2315.astype('float32'), [2, 12, 15])), 0)
call_2316 = relay.TupleGetItem(func_2180_call(relay.reshape(var_2315.astype('float32'), [2, 12, 15])), 0)
bop_2317 = relay.floor_divide(call_2314.astype('float64'), relay.reshape(var_2315.astype('float64'), relay.shape_of(call_2314))) # shape=(2, 12, 15)
bop_2320 = relay.floor_divide(call_2316.astype('float64'), relay.reshape(var_2315.astype('float64'), relay.shape_of(call_2316))) # shape=(2, 12, 15)
func_2076_call = mod.get_global_var('func_2076')
func_2077_call = mutated_mod.get_global_var('func_2077')
call_2326 = relay.TupleGetItem(func_2076_call(), 0)
call_2327 = relay.TupleGetItem(func_2077_call(), 0)
var_2368 = relay.var("var_2368", dtype = "float64", shape = (15, 16, 16))#candidate|2368|(15, 16, 16)|var|float64
bop_2369 = relay.bitwise_xor(call_2252.astype('uint64'), var_2368.astype('uint64')) # shape=(15, 16, 16)
bop_2372 = relay.bitwise_xor(call_2253.astype('uint64'), var_2368.astype('uint64')) # shape=(15, 16, 16)
uop_2373 = relay.acos(bop_2369.astype('float32')) # shape=(15, 16, 16)
uop_2375 = relay.acos(bop_2372.astype('float32')) # shape=(15, 16, 16)
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_2383 = relay.TupleGetItem(func_2156_call(), 0)
call_2384 = relay.TupleGetItem(func_2158_call(), 0)
bop_2391 = relay.bitwise_and(uop_2373.astype('uint16'), call_2326.astype('uint16')) # shape=(15, 16, 16)
bop_2394 = relay.bitwise_and(uop_2375.astype('uint16'), call_2327.astype('uint16')) # shape=(15, 16, 16)
func_1683_call = mod.get_global_var('func_1683')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_2399 = relay.TupleGetItem(func_1683_call(), 0)
call_2400 = relay.TupleGetItem(func_1684_call(), 0)
output = relay.Tuple([call_2225,call_2246,call_2250,call_2271,call_2288,bop_2317,call_2383,bop_2391,call_2399,])
output2 = relay.Tuple([call_2226,call_2247,call_2251,call_2272,call_2289,bop_2320,call_2384,bop_2394,call_2400,])
func_2426 = relay.Function([var_2315,var_2368,], output)
mod['func_2426'] = func_2426
mod = relay.transform.InferType()(mod)
var_2427 = relay.var("var_2427", dtype = "float32", shape = (360,))#candidate|2427|(360,)|var|float32
var_2428 = relay.var("var_2428", dtype = "float64", shape = (15, 16, 16))#candidate|2428|(15, 16, 16)|var|float64
output = func_2426(var_2427,var_2428,)
func_2429 = relay.Function([var_2427,var_2428,], output)
mutated_mod['func_2429'] = func_2429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2504 = relay.var("var_2504", dtype = "float64", shape = (12, 12, 16))#candidate|2504|(12, 12, 16)|var|float64
uop_2505 = relay.asinh(var_2504.astype('float64')) # shape=(12, 12, 16)
output = uop_2505
output2 = uop_2505
func_2510 = relay.Function([var_2504,], output)
mod['func_2510'] = func_2510
mod = relay.transform.InferType()(mod)
var_2511 = relay.var("var_2511", dtype = "float64", shape = (12, 12, 16))#candidate|2511|(12, 12, 16)|var|float64
output = func_2510(var_2511)
func_2512 = relay.Function([var_2511], output)
mutated_mod['func_2512'] = func_2512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_2566 = func_1417_call()
call_2567 = func_1417_call()
uop_2576 = relay.log2(call_2566.astype('float64')) # shape=(15, 1, 16)
uop_2578 = relay.log2(call_2567.astype('float64')) # shape=(15, 1, 16)
func_1524_call = mod.get_global_var('func_1524')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_2584 = relay.TupleGetItem(func_1524_call(), 0)
call_2585 = relay.TupleGetItem(func_1525_call(), 0)
output = relay.Tuple([uop_2576,call_2584,])
output2 = relay.Tuple([uop_2578,call_2585,])
func_2593 = relay.Function([], output)
mod['func_2593'] = func_2593
mod = relay.transform.InferType()(mod)
output = func_2593()
func_2594 = relay.Function([], output)
mutated_mod['func_2594'] = func_2594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_2614 = relay.TupleGetItem(func_1381_call(), 0)
call_2615 = relay.TupleGetItem(func_1382_call(), 0)
output = relay.Tuple([call_2614,])
output2 = relay.Tuple([call_2615,])
func_2632 = relay.Function([], output)
mod['func_2632'] = func_2632
mod = relay.transform.InferType()(mod)
mutated_mod['func_2632'] = func_2632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mutated_mod.get_global_var('func_2632')
call_2633 = func_2632_call()
output = call_2633
func_2634 = relay.Function([], output)
mutated_mod['func_2634'] = func_2634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2076_call = mod.get_global_var('func_2076')
func_2077_call = mutated_mod.get_global_var('func_2077')
call_2672 = relay.TupleGetItem(func_2076_call(), 0)
call_2673 = relay.TupleGetItem(func_2077_call(), 0)
output = relay.Tuple([call_2672,])
output2 = relay.Tuple([call_2673,])
func_2699 = relay.Function([], output)
mod['func_2699'] = func_2699
mod = relay.transform.InferType()(mod)
mutated_mod['func_2699'] = func_2699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2699_call = mutated_mod.get_global_var('func_2699')
call_2700 = func_2699_call()
output = call_2700
func_2701 = relay.Function([], output)
mutated_mod['func_2701'] = func_2701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_2748 = relay.TupleGetItem(func_1159_call(), 0)
call_2749 = relay.TupleGetItem(func_1160_call(), 0)
output = relay.Tuple([call_2748,])
output2 = relay.Tuple([call_2749,])
func_2765 = relay.Function([], output)
mod['func_2765'] = func_2765
mod = relay.transform.InferType()(mod)
output = func_2765()
func_2766 = relay.Function([], output)
mutated_mod['func_2766'] = func_2766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_2782 = relay.TupleGetItem(func_1608_call(), 0)
call_2783 = relay.TupleGetItem(func_1609_call(), 0)
output = relay.Tuple([call_2782,])
output2 = relay.Tuple([call_2783,])
func_2788 = relay.Function([], output)
mod['func_2788'] = func_2788
mod = relay.transform.InferType()(mod)
output = func_2788()
func_2789 = relay.Function([], output)
mutated_mod['func_2789'] = func_2789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_2839 = relay.TupleGetItem(func_1109_call(), 0)
call_2840 = relay.TupleGetItem(func_1110_call(), 0)
uop_2843 = relay.exp(call_2839.astype('float64')) # shape=(15, 1, 16)
uop_2845 = relay.exp(call_2840.astype('float64')) # shape=(15, 1, 16)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_2847 = relay.TupleGetItem(func_1109_call(), 1)
call_2848 = relay.TupleGetItem(func_1110_call(), 1)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_2851 = relay.TupleGetItem(func_1608_call(), 1)
call_2852 = relay.TupleGetItem(func_1609_call(), 1)
bop_2855 = relay.not_equal(uop_2843.astype('bool'), relay.reshape(call_2839.astype('bool'), relay.shape_of(uop_2843))) # shape=(15, 1, 16)
bop_2858 = relay.not_equal(uop_2845.astype('bool'), relay.reshape(call_2840.astype('bool'), relay.shape_of(uop_2845))) # shape=(15, 1, 16)
output = relay.Tuple([call_2847,call_2851,bop_2855,])
output2 = relay.Tuple([call_2848,call_2852,bop_2858,])
func_2869 = relay.Function([], output)
mod['func_2869'] = func_2869
mod = relay.transform.InferType()(mod)
mutated_mod['func_2869'] = func_2869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2869_call = mutated_mod.get_global_var('func_2869')
call_2870 = func_2869_call()
output = call_2870
func_2871 = relay.Function([], output)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2699_call = mod.get_global_var('func_2699')
func_2701_call = mutated_mod.get_global_var('func_2701')
call_2872 = relay.TupleGetItem(func_2699_call(), 0)
call_2873 = relay.TupleGetItem(func_2701_call(), 0)
func_2788_call = mod.get_global_var('func_2788')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_2888 = relay.TupleGetItem(func_2788_call(), 0)
call_2889 = relay.TupleGetItem(func_2789_call(), 0)
bop_2894 = relay.equal(call_2872.astype('bool'), relay.reshape(call_2888.astype('bool'), relay.shape_of(call_2872))) # shape=(15, 1, 16)
bop_2897 = relay.equal(call_2873.astype('bool'), relay.reshape(call_2889.astype('bool'), relay.shape_of(call_2873))) # shape=(15, 1, 16)
output = relay.Tuple([bop_2894,])
output2 = relay.Tuple([bop_2897,])
func_2902 = relay.Function([], output)
mod['func_2902'] = func_2902
mod = relay.transform.InferType()(mod)
mutated_mod['func_2902'] = func_2902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mutated_mod.get_global_var('func_2902')
call_2903 = func_2902_call()
output = call_2903
func_2904 = relay.Function([], output)
mutated_mod['func_2904'] = func_2904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_2931 = relay.TupleGetItem(func_2902_call(), 0)
call_2932 = relay.TupleGetItem(func_2904_call(), 0)
output = call_2931
output2 = call_2932
func_2953 = relay.Function([], output)
mod['func_2953'] = func_2953
mod = relay.transform.InferType()(mod)
mutated_mod['func_2953'] = func_2953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mutated_mod.get_global_var('func_2953')
call_2954 = func_2953_call()
output = call_2954
func_2955 = relay.Function([], output)
mutated_mod['func_2955'] = func_2955
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2968 = relay.const([[[-7.208690,-9.817063,-2.377382,5.645720,-6.170958,7.486928],[9.903474,8.849641,-3.310929,2.760544,1.537165,0.298455],[-5.823449,8.221730,1.350455,-4.123366,-0.777657,-5.318299],[1.561340,-0.249184,1.329300,-8.808294,-8.340862,-0.713931],[-2.977718,9.603218,-2.996584,-8.875735,2.128030,3.796255]],[[9.185390,-2.125941,6.012919,-5.945344,4.838432,-0.505418],[-0.188340,8.296511,-9.230101,-3.038656,6.490225,1.496498],[-6.770733,-5.057318,0.659477,-0.111456,-0.856491,-8.384296],[3.716092,-2.887601,8.024466,9.305242,8.847882,-9.551242],[-6.367870,-9.261335,-6.562419,1.611313,-5.475802,3.226242]],[[-2.016935,-9.257957,-5.312772,-7.840263,1.781712,-2.943372],[9.973671,-6.805278,7.625978,3.189350,7.554605,5.190820],[4.507616,-6.921049,8.006278,9.531373,4.218714,-6.226011],[-3.691887,1.149199,0.450754,4.306704,7.802944,7.404956],[-1.793641,5.599975,9.276014,-2.975021,0.257266,-2.056714]],[[-3.054239,-6.328738,8.515740,7.812503,3.616215,7.719486],[8.179423,-8.456237,-0.755420,0.287937,-4.679991,8.829359],[3.775474,-5.705906,-4.445265,8.902030,-6.429027,9.780404],[-2.222770,8.863577,5.061304,-0.108580,2.200903,-7.076751],[7.104211,8.692507,-8.901177,8.597350,-8.263469,-3.371126]],[[-5.239216,4.835348,-7.418673,-4.125201,5.478962,-1.287928],[-2.371284,5.715616,9.812018,0.167578,8.492549,-9.912598],[5.637176,-0.443349,2.134860,3.515713,-5.895114,-1.417994],[3.605371,-1.667950,0.387731,8.457872,9.235386,1.669722],[-1.850184,4.655799,9.560397,7.870857,1.644392,-5.188421]],[[8.794282,-8.326409,-1.944525,-6.977913,3.557386,8.424028],[7.908403,-4.530847,6.863671,-0.852126,1.368478,-2.171415],[2.473382,0.912381,5.533916,-0.122868,8.947604,-6.434879],[6.500359,9.726153,6.822018,0.259364,-3.774490,-2.490061],[-5.194263,1.453839,-3.200934,-0.773607,-3.512435,2.494703]],[[-2.231926,-5.816650,-8.240959,8.953943,6.470610,8.500404],[3.451315,6.995026,-9.644018,-5.434501,-4.648700,-0.302984],[5.078371,7.672459,4.961232,3.679191,-2.040022,5.535296],[-5.398948,-3.095129,-6.253757,9.575738,6.565732,6.169884],[-1.509519,-0.008292,4.816999,4.646657,0.474050,-2.345913]],[[1.401361,-7.532619,7.842783,8.785161,9.047251,3.235969],[8.350419,8.584036,-3.698094,-5.549399,-6.816788,4.752947],[-8.846818,-0.703859,2.165700,-8.511528,-7.170974,-5.740127],[-1.759895,-9.992853,-6.630755,2.461996,-8.219282,-2.665721],[5.680448,3.557804,8.143768,-5.977991,1.412874,4.131646]],[[9.723507,-4.509494,1.976702,-1.668976,-3.687246,3.853563],[-6.038837,-2.433367,0.971432,0.988066,8.708110,5.776086],[-0.950649,-8.543247,-2.056342,-9.434380,3.205633,-6.699221],[-5.437656,1.338340,4.834325,4.511012,0.099939,-1.631282],[-2.849201,-9.459800,-9.358412,-9.623156,7.845996,-4.281893]]], dtype = "float32")#candidate|2968|(9, 5, 6)|const|float32
var_2969 = relay.var("var_2969", dtype = "float32", shape = (9, 5, 6))#candidate|2969|(9, 5, 6)|var|float32
bop_2970 = relay.divide(const_2968.astype('float32'), relay.reshape(var_2969.astype('float32'), relay.shape_of(const_2968))) # shape=(9, 5, 6)
output = bop_2970
output2 = bop_2970
func_2979 = relay.Function([var_2969,], output)
mod['func_2979'] = func_2979
mod = relay.transform.InferType()(mod)
mutated_mod['func_2979'] = func_2979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2980 = relay.var("var_2980", dtype = "float32", shape = (9, 5, 6))#candidate|2980|(9, 5, 6)|var|float32
func_2979_call = mutated_mod.get_global_var('func_2979')
call_2981 = func_2979_call(var_2980)
output = call_2981
func_2982 = relay.Function([var_2980], output)
mutated_mod['func_2982'] = func_2982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_2986 = relay.TupleGetItem(func_1159_call(), 0)
call_2987 = relay.TupleGetItem(func_1160_call(), 0)
var_2989 = relay.var("var_2989", dtype = "float64", shape = (15, 11, 16))#candidate|2989|(15, 11, 16)|var|float64
bop_2990 = relay.minimum(call_2986.astype('uint16'), var_2989.astype('uint16')) # shape=(15, 11, 16)
bop_2993 = relay.minimum(call_2987.astype('uint16'), var_2989.astype('uint16')) # shape=(15, 11, 16)
uop_2995 = relay.log(bop_2990.astype('float64')) # shape=(15, 11, 16)
uop_2997 = relay.log(bop_2993.astype('float64')) # shape=(15, 11, 16)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_3012 = relay.TupleGetItem(func_1159_call(), 0)
call_3013 = relay.TupleGetItem(func_1160_call(), 0)
bop_3014 = relay.logical_and(call_3012.astype('bool'), var_2989.astype('bool')) # shape=(15, 11, 16)
bop_3017 = relay.logical_and(call_3013.astype('bool'), var_2989.astype('bool')) # shape=(15, 11, 16)
output = relay.Tuple([uop_2995,bop_3014,])
output2 = relay.Tuple([uop_2997,bop_3017,])
func_3026 = relay.Function([var_2989,], output)
mod['func_3026'] = func_3026
mod = relay.transform.InferType()(mod)
mutated_mod['func_3026'] = func_3026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3027 = relay.var("var_3027", dtype = "float64", shape = (15, 11, 16))#candidate|3027|(15, 11, 16)|var|float64
func_3026_call = mutated_mod.get_global_var('func_3026')
call_3028 = func_3026_call(var_3027)
output = call_3028
func_3029 = relay.Function([var_3027], output)
mutated_mod['func_3029'] = func_3029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_3045 = relay.TupleGetItem(func_2765_call(), 0)
call_3046 = relay.TupleGetItem(func_2766_call(), 0)
output = call_3045
output2 = call_3046
func_3047 = relay.Function([], output)
mod['func_3047'] = func_3047
mod = relay.transform.InferType()(mod)
output = func_3047()
func_3048 = relay.Function([], output)
mutated_mod['func_3048'] = func_3048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2788_call = mod.get_global_var('func_2788')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_3052 = relay.TupleGetItem(func_2788_call(), 0)
call_3053 = relay.TupleGetItem(func_2789_call(), 0)
output = call_3052
output2 = call_3053
func_3060 = relay.Function([], output)
mod['func_3060'] = func_3060
mod = relay.transform.InferType()(mod)
mutated_mod['func_3060'] = func_3060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mutated_mod.get_global_var('func_3060')
call_3061 = func_3060_call()
output = call_3061
func_3062 = relay.Function([], output)
mutated_mod['func_3062'] = func_3062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3088 = relay.var("var_3088", dtype = "float32", shape = (12, 1, 8))#candidate|3088|(12, 1, 8)|var|float32
uop_3089 = relay.tan(var_3088.astype('float32')) # shape=(12, 1, 8)
output = uop_3089
output2 = uop_3089
func_3105 = relay.Function([var_3088,], output)
mod['func_3105'] = func_3105
mod = relay.transform.InferType()(mod)
mutated_mod['func_3105'] = func_3105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3106 = relay.var("var_3106", dtype = "float32", shape = (12, 1, 8))#candidate|3106|(12, 1, 8)|var|float32
func_3105_call = mutated_mod.get_global_var('func_3105')
call_3107 = func_3105_call(var_3106)
output = call_3107
func_3108 = relay.Function([var_3106], output)
mutated_mod['func_3108'] = func_3108
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3115 = relay.const([[[-2.086954,2.232206,-9.655261,-9.840280,9.558106,5.275091,1.666481],[1.512666,8.175449,-0.439881,-1.188635,-1.843317,-2.548862,1.471469],[-2.046001,-8.492180,-8.351351,-1.574946,0.502867,-0.737257,6.430199],[-1.314893,2.051561,-5.089591,-4.261403,-2.287599,6.067917,-6.282432],[0.322961,1.689545,-7.405071,-5.559748,-7.185023,2.690841,-9.077383],[-2.143643,-6.990477,-1.197300,-2.493714,-2.488042,4.415319,1.276787],[4.513640,-2.592415,6.202535,-7.783226,-1.293768,-9.777879,-7.734439],[-5.855852,-9.954154,-0.768137,4.006170,-0.572926,1.107416,3.722449],[3.135315,5.805489,-9.003640,9.580401,0.049528,4.158635,-2.034851],[-6.653771,3.028182,2.028689,9.543713,-3.476779,8.951574,1.729620],[-7.859632,4.023850,2.111064,-7.535217,5.963752,-2.242304,-8.713126],[-4.193075,2.163128,6.544762,4.819975,-8.029672,-2.162675,-4.063457],[6.675411,-2.417358,-2.600000,8.158256,-7.161242,2.075646,3.304045],[-4.152124,3.395818,2.682016,-6.218879,1.672512,2.363740,-4.054343]],[[0.098838,6.211756,-5.208880,-5.805458,-4.803052,2.291256,3.870291],[-3.452545,-8.663540,-6.520715,6.366273,-9.275099,-8.144929,0.472694],[-1.803958,8.658827,-6.495322,-4.504522,-0.537185,8.137680,0.789241],[3.927970,7.650717,8.746794,3.449239,6.549398,3.284038,-9.500120],[-1.419798,-0.878385,4.163041,-2.669682,-3.517498,8.001049,1.334779],[6.351892,9.805310,1.291465,-5.475349,-9.395653,9.287100,-2.837371],[8.750273,-4.372485,8.043709,-5.061708,3.888930,-5.654727,-9.918506],[-1.074466,1.479774,-9.510813,0.514769,1.490750,-7.128815,1.469782],[-5.473923,7.616357,-7.498564,3.199574,-5.118773,-2.460238,-8.914987],[4.398440,-5.316708,-8.799646,-9.692267,-3.326499,-3.525634,2.609460],[2.537074,-8.813971,3.106841,-8.105412,-3.384212,9.301156,8.943112],[-6.487760,-7.470993,-9.284467,8.979329,-9.859797,5.719702,1.080337],[6.278657,8.046737,2.234546,-7.035950,3.061633,-9.876878,-8.061330],[-9.117139,-5.809563,4.365714,-0.384150,7.134383,-3.497863,3.878790]],[[4.626354,2.029503,-4.717896,9.579443,1.173589,-6.321342,-5.539232],[-4.239261,-7.879988,3.298335,6.474791,3.413381,-4.552466,3.059525],[6.173800,7.225269,-3.904649,0.046546,7.135852,-0.474192,-3.768074],[3.993514,-2.802386,3.061031,-6.904720,8.455952,2.238290,8.988709],[6.282969,-2.022096,-5.887912,1.269624,-2.281162,9.236146,-2.240587],[-1.192425,-6.611889,1.931132,7.070376,7.128358,1.146457,2.338593],[7.246731,7.652096,-2.370078,5.268506,6.298384,5.836355,9.662941],[1.555929,-5.029771,-8.481268,0.230907,1.789984,-1.431177,-7.942112],[1.446403,-5.897679,-0.952474,-0.019654,1.325700,5.384520,-5.759561],[1.375268,7.950462,5.597515,-9.883698,-2.206297,-8.544875,9.730805],[-0.076779,-9.380326,8.058983,1.790421,-8.957793,-0.395010,6.410338],[-7.822563,-5.346030,-9.931311,-7.918033,-5.220361,6.363378,-7.745641],[-7.837947,7.104968,0.736272,1.879193,-0.963650,4.601959,-7.883453],[6.502929,3.508449,1.388115,9.129752,-8.900147,-4.487298,-6.626224]],[[7.302304,4.414188,-4.278223,0.223151,-6.581850,5.585820,9.949785],[-8.111929,-6.768560,0.442164,2.028339,-7.562162,-3.964541,3.385062],[8.410719,5.650359,-0.429322,-8.516830,7.190109,2.773113,-2.145048],[-4.571302,1.286906,6.925824,-5.189930,5.748266,-4.872995,-9.308880],[-2.428738,5.717868,-3.431165,0.314362,3.285471,9.181049,8.190868],[-7.267296,0.216158,3.449680,8.535340,8.871021,9.198679,-3.957533],[-8.236221,6.135092,-0.695826,-7.785675,7.866123,3.187373,3.035228],[1.915491,6.761768,8.299317,-6.032609,5.047191,2.718288,-2.876656],[-1.502577,-8.826897,6.295389,4.977387,-1.455944,-7.567681,8.130672],[-0.728627,4.835209,9.409232,-1.666795,2.724019,6.865600,-1.716673],[1.287704,-4.256226,3.190093,-6.757428,-5.970656,-5.337205,8.739552],[-0.432291,7.531255,-0.904517,-0.445826,7.685135,-4.781010,8.755939],[-5.014922,-8.042555,-7.715922,1.896411,-0.682729,2.240579,8.479994],[3.307027,-1.395656,-1.732432,7.588549,-6.956712,-1.303308,-3.353700]],[[1.441111,9.634509,0.284996,5.916403,-0.495073,-2.518875,7.486108],[6.327209,2.472573,4.054989,-9.435598,9.676801,-1.551054,5.633199],[-6.647708,5.206087,7.808913,9.381116,4.231015,5.254596,5.736175],[-3.623713,9.883890,1.114170,-8.039057,-2.833492,-3.872017,-3.655881],[-7.488930,-2.467766,3.408604,-4.834477,-6.657326,-7.513878,-5.661741],[5.573167,0.332600,-7.215026,9.397235,3.798309,9.138456,-5.264034],[-4.518946,-6.660082,-4.329247,5.877774,7.415509,-0.980834,0.269505],[0.878799,-9.999263,8.572368,-8.764477,-7.274307,8.212891,6.980742],[-6.472661,3.244422,2.121729,5.479037,-2.175184,3.137781,-6.550789],[2.271771,-6.100777,2.994181,2.324477,-2.325368,4.485206,0.981555],[8.855804,6.181718,-1.219621,-5.530045,-3.483309,3.565315,-1.948745],[-4.025534,-0.947268,-0.522598,-6.524535,-9.871635,-4.716881,4.799589],[6.017947,-8.735238,-3.813701,-9.822753,-6.280976,-2.540402,-0.751880],[7.711107,-7.086099,0.537525,2.861499,-0.796701,-1.494006,1.863362]],[[0.309958,-2.304057,8.035779,8.305324,-3.645474,-9.601570,-4.783761],[6.982062,-9.882925,8.621435,4.885975,-1.727406,-5.924006,-3.399674],[9.855553,6.922209,5.560823,9.855420,5.783353,-3.170247,8.061475],[-9.156303,4.869334,-7.680929,7.457931,-0.633619,0.777484,7.301609],[7.362657,-3.532511,-0.994414,-4.562518,7.387607,-7.043003,-6.549278],[-6.346789,-8.796911,-8.829853,-0.991989,5.371689,-3.665234,-5.778104],[-1.728756,-9.979223,-5.486376,-2.600977,-0.071997,-0.006598,9.926054],[-5.548804,4.620971,0.452454,-2.148177,7.855665,-8.080255,-4.746569],[-1.537651,-9.805400,-6.211842,8.149324,7.540329,3.330063,-0.180068],[0.238224,3.432487,9.772016,-2.598805,-0.575125,-4.456358,-9.571126],[-7.338143,-7.083298,2.612344,-5.362624,8.346245,-5.606388,9.275580],[-3.342449,1.598439,5.780552,-1.166029,3.631899,1.039278,9.616815],[5.172143,1.084785,-7.391771,2.353704,-6.798954,4.357787,8.172776],[4.868987,-9.298660,-9.863881,5.278076,-0.670943,-4.257526,3.940775]],[[3.843483,-8.020081,-0.395661,-9.025954,3.527222,-4.735490,4.815061],[8.091546,-3.237971,-2.906568,-5.085748,-1.314591,-0.262247,9.867686],[3.101881,4.721732,5.248589,7.492117,0.489932,-6.076955,1.066743],[-6.092029,3.952698,0.533873,-3.538162,-8.510148,-9.035101,3.585682],[5.824717,-3.446900,1.471292,0.889660,3.247198,-6.956978,-1.071647],[5.749287,8.263133,3.188265,6.683557,-4.845959,-7.631978,-4.540484],[-6.312470,9.614834,1.998174,-7.518730,1.988626,8.850838,-0.074450],[7.054111,9.573592,3.042644,1.720758,1.894333,7.932776,-0.185255],[-6.650300,6.277874,-5.977876,-6.636584,-6.313721,-9.191038,-1.265854],[-1.985775,1.320744,3.386742,-3.017761,-6.389511,3.994820,-9.508882],[4.286463,-7.223324,8.487042,-0.539435,3.928771,9.411442,1.201448],[3.326232,-4.056993,8.713957,-1.600748,-4.902454,8.524621,-3.580096],[-4.058525,7.694083,7.910704,8.508579,1.189342,4.000221,-1.909133],[-0.037376,-8.445197,7.347727,3.429126,7.968158,8.730649,-5.278436]],[[-3.516779,-9.051477,9.684900,-2.662270,6.956385,-6.699583,-3.492304],[7.909398,-9.422004,-9.778166,-9.599676,3.376406,-2.861165,9.774555],[-8.639379,-5.700787,-5.166750,1.269609,0.980059,-0.312990,4.047715],[3.475412,-6.125160,-6.033501,2.558856,-4.255823,-1.680746,9.702000],[-7.270846,8.716744,5.013649,5.300518,-5.508706,8.527048,-1.259913],[-0.647945,-2.209768,6.493194,2.520262,-4.679494,0.050753,-9.876310],[-4.951795,-1.302607,-5.853958,-4.213657,-5.803015,9.263937,-6.657030],[-5.901769,-3.435319,2.376991,-3.950034,-2.403499,-8.568700,-1.994372],[1.425165,-7.274570,2.279503,-1.303815,-0.936431,1.678546,-2.384834],[9.420853,5.486472,8.318391,-9.205229,2.244429,-3.800786,-0.887833],[-1.344106,-8.446449,2.017834,9.438645,4.545346,-9.398833,-4.991153],[-8.189813,-5.996866,-3.555584,5.463489,-2.809257,-3.355806,7.486124],[1.082330,3.646788,-9.212258,1.883800,-1.747451,-6.638129,-7.204366],[4.372768,-5.491457,7.061803,1.439778,3.877947,7.285942,8.103868]]], dtype = "float32")#candidate|3115|(8, 14, 7)|const|float32
uop_3116 = relay.sinh(const_3115.astype('float32')) # shape=(8, 14, 7)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
call_3120 = relay.TupleGetItem(func_1707_call(), 0)
call_3121 = relay.TupleGetItem(func_1709_call(), 0)
func_2510_call = mod.get_global_var('func_2510')
func_2512_call = mutated_mod.get_global_var('func_2512')
var_3125 = relay.var("var_3125", dtype = "float64", shape = (2304,))#candidate|3125|(2304,)|var|float64
call_3124 = func_2510_call(relay.reshape(var_3125.astype('float64'), [12, 12, 16]))
call_3126 = func_2510_call(relay.reshape(var_3125.astype('float64'), [12, 12, 16]))
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_3138 = relay.TupleGetItem(func_1608_call(), 0)
call_3139 = relay.TupleGetItem(func_1609_call(), 0)
func_2593_call = mod.get_global_var('func_2593')
func_2594_call = mutated_mod.get_global_var('func_2594')
call_3141 = relay.TupleGetItem(func_2593_call(), 1)
call_3142 = relay.TupleGetItem(func_2594_call(), 1)
output = relay.Tuple([uop_3116,call_3120,call_3124,var_3125,call_3138,call_3141,])
output2 = relay.Tuple([uop_3116,call_3121,call_3126,var_3125,call_3139,call_3142,])
func_3153 = relay.Function([var_3125,], output)
mod['func_3153'] = func_3153
mod = relay.transform.InferType()(mod)
mutated_mod['func_3153'] = func_3153
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3154 = relay.var("var_3154", dtype = "float64", shape = (2304,))#candidate|3154|(2304,)|var|float64
func_3153_call = mutated_mod.get_global_var('func_3153')
call_3155 = func_3153_call(var_3154)
output = call_3155
func_3156 = relay.Function([var_3154], output)
mutated_mod['func_3156'] = func_3156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mod.get_global_var('func_2632')
func_2634_call = mutated_mod.get_global_var('func_2634')
call_3180 = relay.TupleGetItem(func_2632_call(), 0)
call_3181 = relay.TupleGetItem(func_2634_call(), 0)
var_3198 = relay.var("var_3198", dtype = "float64", shape = (15, 8, 16))#candidate|3198|(15, 8, 16)|var|float64
bop_3199 = relay.floor_mod(call_3180.astype('float32'), var_3198.astype('float32')) # shape=(15, 8, 16)
bop_3202 = relay.floor_mod(call_3181.astype('float32'), var_3198.astype('float32')) # shape=(15, 8, 16)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_3204 = relay.TupleGetItem(func_1381_call(), 0)
call_3205 = relay.TupleGetItem(func_1382_call(), 0)
bop_3210 = relay.left_shift(bop_3199.astype('int16'), relay.reshape(var_3198.astype('int16'), relay.shape_of(bop_3199))) # shape=(15, 8, 16)
bop_3213 = relay.left_shift(bop_3202.astype('int16'), relay.reshape(var_3198.astype('int16'), relay.shape_of(bop_3202))) # shape=(15, 8, 16)
func_2177_call = mod.get_global_var('func_2177')
func_2180_call = mutated_mod.get_global_var('func_2180')
var_3216 = relay.var("var_3216", dtype = "float32", shape = (360,))#candidate|3216|(360,)|var|float32
call_3215 = relay.TupleGetItem(func_2177_call(relay.reshape(var_3216.astype('float32'), [2, 12, 15])), 0)
call_3217 = relay.TupleGetItem(func_2180_call(relay.reshape(var_3216.astype('float32'), [2, 12, 15])), 0)
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_3219 = relay.TupleGetItem(func_2156_call(), 0)
call_3220 = relay.TupleGetItem(func_2158_call(), 0)
output = relay.Tuple([call_3204,bop_3210,call_3215,var_3216,call_3219,])
output2 = relay.Tuple([call_3205,bop_3213,call_3217,var_3216,call_3220,])
func_3230 = relay.Function([var_3198,var_3216,], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
var_3231 = relay.var("var_3231", dtype = "float64", shape = (15, 8, 16))#candidate|3231|(15, 8, 16)|var|float64
var_3232 = relay.var("var_3232", dtype = "float32", shape = (360,))#candidate|3232|(360,)|var|float32
output = func_3230(var_3231,var_3232,)
func_3233 = relay.Function([var_3231,var_3232,], output)
mutated_mod['func_3233'] = func_3233
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3235 = relay.const(-1.984814, dtype = "float64")#candidate|3235|()|const|float64
var_3236 = relay.var("var_3236", dtype = "float64", shape = (3, 11, 12))#candidate|3236|(3, 11, 12)|var|float64
bop_3237 = relay.power(const_3235.astype('float64'), var_3236.astype('float64')) # shape=(3, 11, 12)
output = bop_3237
output2 = bop_3237
func_3242 = relay.Function([var_3236,], output)
mod['func_3242'] = func_3242
mod = relay.transform.InferType()(mod)
var_3243 = relay.var("var_3243", dtype = "float64", shape = (3, 11, 12))#candidate|3243|(3, 11, 12)|var|float64
output = func_3242(var_3243)
func_3244 = relay.Function([var_3243], output)
mutated_mod['func_3244'] = func_3244
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3280 = relay.var("var_3280", dtype = "uint64", shape = (3, 3, 8))#candidate|3280|(3, 3, 8)|var|uint64
const_3281 = relay.const([[[4,-3,-1,1,2,-2,-1,-10],[-8,-7,5,2,9,7,9,-9],[7,-3,-2,4,4,-7,-10,5]],[[-3,8,4,-3,2,-4,5,-5],[-5,1,-5,-1,10,5,4,-9],[2,-6,-9,-9,7,1,-9,4]],[[-7,3,-9,-2,-2,-10,4,-7],[9,3,2,-9,5,3,-10,-8],[-2,-10,5,2,6,-6,-3,9]]], dtype = "uint64")#candidate|3281|(3, 3, 8)|const|uint64
bop_3282 = relay.bitwise_and(var_3280.astype('uint64'), relay.reshape(const_3281.astype('uint64'), relay.shape_of(var_3280))) # shape=(3, 3, 8)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_3287 = relay.TupleGetItem(func_1159_call(), 2)
call_3288 = relay.TupleGetItem(func_1160_call(), 2)
output = relay.Tuple([bop_3282,call_3287,])
output2 = relay.Tuple([bop_3282,call_3288,])
func_3292 = relay.Function([var_3280,], output)
mod['func_3292'] = func_3292
mod = relay.transform.InferType()(mod)
mutated_mod['func_3292'] = func_3292
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3293 = relay.var("var_3293", dtype = "uint64", shape = (3, 3, 8))#candidate|3293|(3, 3, 8)|var|uint64
func_3292_call = mutated_mod.get_global_var('func_3292')
call_3294 = func_3292_call(var_3293)
output = call_3294
func_3295 = relay.Function([var_3293], output)
mutated_mod['func_3295'] = func_3295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_3309 = relay.TupleGetItem(func_1561_call(), 0)
call_3310 = relay.TupleGetItem(func_1563_call(), 0)
output = call_3309
output2 = call_3310
func_3313 = relay.Function([], output)
mod['func_3313'] = func_3313
mod = relay.transform.InferType()(mod)
output = func_3313()
func_3314 = relay.Function([], output)
mutated_mod['func_3314'] = func_3314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2593_call = mod.get_global_var('func_2593')
func_2594_call = mutated_mod.get_global_var('func_2594')
call_3315 = relay.TupleGetItem(func_2593_call(), 0)
call_3316 = relay.TupleGetItem(func_2594_call(), 0)
func_1274_call = mod.get_global_var('func_1274')
func_1275_call = mutated_mod.get_global_var('func_1275')
call_3347 = relay.TupleGetItem(func_1274_call(), 0)
call_3348 = relay.TupleGetItem(func_1275_call(), 0)
output = relay.Tuple([call_3315,call_3347,])
output2 = relay.Tuple([call_3316,call_3348,])
func_3354 = relay.Function([], output)
mod['func_3354'] = func_3354
mod = relay.transform.InferType()(mod)
mutated_mod['func_3354'] = func_3354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3354_call = mutated_mod.get_global_var('func_3354')
call_3355 = func_3354_call()
output = call_3355
func_3356 = relay.Function([], output)
mutated_mod['func_3356'] = func_3356
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3363 = relay.const([[[-1.250625,-7.460263,3.104813,-9.123669,5.393661,4.167543,-2.252816,8.660659,-8.125227,5.522491,-6.269810,6.528977,-0.689144,1.467107,-8.820545,0.931767],[-2.744714,-2.081307,6.075476,-4.899274,-6.239491,1.148476,2.653027,2.383381,7.111262,-2.103049,-8.937245,5.668590,6.243769,4.258415,2.469051,2.770259],[-3.429449,-9.785429,-4.380117,-3.847500,-2.096482,7.585649,-3.156573,4.199966,-2.554356,4.793304,-8.691479,1.590738,6.139595,8.399952,-6.941820,-5.978075],[6.000370,-5.909685,-3.256053,-8.572987,0.571103,-2.217831,-8.915315,6.962935,2.460903,4.262992,6.363886,-5.224092,9.747008,0.761017,-5.755849,4.943831],[-8.129185,0.168259,-8.435872,-2.711748,4.109267,-9.604859,-4.149798,-6.488339,-7.338525,6.513008,8.426604,5.181482,-7.082157,-8.723320,-7.554577,-1.499179],[8.041638,5.436910,4.048121,9.141075,3.279034,5.821781,9.408942,0.569216,9.059300,4.930543,-3.931841,-9.505139,-9.275444,7.745421,-4.532903,4.461221]],[[7.211537,0.404609,-5.934542,-2.692158,-4.570946,-0.752048,8.854223,-4.840675,-4.704856,5.253369,-9.324280,9.564527,-2.408489,9.556755,-3.383439,7.043215],[-9.326711,8.703494,0.660220,-0.905664,6.749365,-6.918525,-9.595168,6.477851,-8.296624,-9.768155,-9.605088,5.490630,-8.895794,0.291482,-7.085984,9.649821],[-2.739575,2.158856,-6.901176,6.134207,-2.257590,-0.344145,-2.085622,-2.237194,9.340349,7.086144,-9.486808,-3.577639,-1.042403,-8.109812,-7.880626,2.426850],[-5.125137,5.769866,-6.580476,-3.983908,-4.666757,6.899755,-8.720631,4.954041,-6.989310,-7.294529,-2.166112,-9.810956,-9.279821,8.508167,-9.172269,7.515461],[6.833964,8.082041,-3.801667,7.147265,-6.828930,3.589384,-4.740268,-0.434312,-5.820782,1.275550,-4.163680,8.874700,-2.016913,5.888389,2.442388,2.850061],[1.518488,-6.308612,-4.523468,-2.253953,-7.217823,-1.289290,3.187299,-0.819894,2.620503,-1.115834,4.779130,-4.545144,-8.655308,-6.805735,1.020249,-8.172638]],[[-5.816039,-4.974857,-7.792901,2.138649,-2.389411,8.644908,4.822203,3.011501,-5.591720,-1.978196,1.013382,2.790055,-3.721106,2.758510,-4.997088,3.313205],[-9.350212,6.642581,-4.628895,-8.274927,-5.352971,-9.399679,0.435533,-8.595808,1.576733,0.625358,-7.766111,-2.622257,-6.118071,-7.302362,-1.418666,9.910817],[9.041949,7.109415,8.492205,-8.745361,-6.062718,0.474453,9.545579,3.005285,-0.248984,2.923916,0.224619,-1.762478,-0.612090,-2.674653,-8.906351,6.033785],[5.244148,8.164060,-5.220513,-4.547567,5.314145,-7.261189,-7.857445,5.295494,-3.765346,7.234152,2.785255,5.283395,-7.609591,-4.132227,0.147654,-3.550632],[-1.064231,-5.660257,3.578240,2.208550,-1.191545,7.100986,8.544963,-9.176680,-3.201687,-9.874973,5.687363,5.044406,9.662994,-5.378831,5.500107,2.636802],[-1.102930,5.436222,9.517036,-2.597886,-9.976984,-1.969880,0.214786,-1.925631,-2.863176,9.762977,-4.839859,8.543206,-7.367704,6.217886,-2.527221,9.661797]]], dtype = "float64")#candidate|3363|(3, 6, 16)|const|float64
uop_3364 = relay.log10(const_3363.astype('float64')) # shape=(3, 6, 16)
output = relay.Tuple([uop_3364,])
output2 = relay.Tuple([uop_3364,])
func_3366 = relay.Function([], output)
mod['func_3366'] = func_3366
mod = relay.transform.InferType()(mod)
mutated_mod['func_3366'] = func_3366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3366_call = mutated_mod.get_global_var('func_3366')
call_3367 = func_3366_call()
output = call_3367
func_3368 = relay.Function([], output)
mutated_mod['func_3368'] = func_3368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2632_call = mod.get_global_var('func_2632')
func_2634_call = mutated_mod.get_global_var('func_2634')
call_3425 = relay.TupleGetItem(func_2632_call(), 0)
call_3426 = relay.TupleGetItem(func_2634_call(), 0)
output = relay.Tuple([call_3425,])
output2 = relay.Tuple([call_3426,])
func_3462 = relay.Function([], output)
mod['func_3462'] = func_3462
mod = relay.transform.InferType()(mod)
mutated_mod['func_3462'] = func_3462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3462_call = mutated_mod.get_global_var('func_3462')
call_3463 = func_3462_call()
output = call_3463
func_3464 = relay.Function([], output)
mutated_mod['func_3464'] = func_3464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_3494 = relay.TupleGetItem(func_1381_call(), 0)
call_3495 = relay.TupleGetItem(func_1382_call(), 0)
output = call_3494
output2 = call_3495
func_3496 = relay.Function([], output)
mod['func_3496'] = func_3496
mod = relay.transform.InferType()(mod)
mutated_mod['func_3496'] = func_3496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3496_call = mutated_mod.get_global_var('func_3496')
call_3497 = func_3496_call()
output = call_3497
func_3498 = relay.Function([], output)
mutated_mod['func_3498'] = func_3498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_3515 = relay.TupleGetItem(func_3366_call(), 0)
call_3516 = relay.TupleGetItem(func_3368_call(), 0)
output = call_3515
output2 = call_3516
func_3533 = relay.Function([], output)
mod['func_3533'] = func_3533
mod = relay.transform.InferType()(mod)
mutated_mod['func_3533'] = func_3533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3533_call = mutated_mod.get_global_var('func_3533')
call_3534 = func_3533_call()
output = call_3534
func_3535 = relay.Function([], output)
mutated_mod['func_3535'] = func_3535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_3544 = func_3060_call()
call_3545 = func_3060_call()
func_3230_call = mod.get_global_var('func_3230')
func_3233_call = mutated_mod.get_global_var('func_3233')
var_3551 = relay.var("var_3551", dtype = "float64", shape = (1920,))#candidate|3551|(1920,)|var|float64
const_3552 = relay.const([[8.110938],[-6.307412],[-3.546599],[-0.792987],[2.931130],[-6.249174],[3.560359],[-5.729738],[-9.652599],[7.691411],[-2.098562],[-2.562730],[-7.303936],[5.437525],[5.425206],[1.439534],[-6.794355],[-6.111059],[7.647688],[-3.618520],[-5.383832],[2.709457],[2.920317],[-4.746087],[2.977594],[2.068074],[-2.589461],[4.644030],[-6.295296],[4.408397],[-3.853084],[-4.527595],[-3.403857],[8.308736],[4.944609],[7.500575],[-7.245741],[7.672347],[-0.342345],[6.030768],[6.375249],[8.625623],[6.180549],[-3.227432],[4.560835],[2.511095],[5.729434],[-0.611962],[-2.588652],[2.648411],[0.310123],[8.998908],[8.145618],[5.132544],[1.955130],[3.531775],[4.590007],[-3.371060],[0.287189],[-5.013201],[-7.566321],[3.260822],[2.272063],[-7.089629],[7.037167],[8.195045],[-6.703297],[8.081049],[2.308839],[8.877887],[2.017111],[-8.691175],[2.454963],[3.334389],[6.694749],[0.964639],[-1.551009],[7.437203],[-5.030670],[8.665465],[1.315903],[-8.695997],[-1.538659],[-4.046859],[-7.479957],[-1.308515],[-5.234547],[-0.139735],[0.202027],[5.955010],[-3.406583],[-3.758524],[7.447755],[-4.975440],[2.315545],[2.433689],[8.544112],[-6.424753],[0.001155],[4.238324],[-5.605355],[-9.601378],[-2.444294],[-7.818837],[-5.584562],[1.045548],[-2.790891],[2.048809],[3.407371],[9.179004],[-0.190601],[-2.248194],[-0.857503],[7.443161],[1.273056],[3.708964],[-8.382861],[-2.062052],[2.340185],[-9.766162],[-0.066746],[-4.448963],[7.435795],[-9.691717],[5.476028],[-6.001582],[2.511802],[7.144022],[2.998796],[8.189624],[-1.400976],[1.922842],[-6.682426],[7.169099],[-9.036928],[-9.665298],[5.401441],[-1.262975],[-9.523490],[-3.090216],[-1.636605],[1.103408],[9.108359],[-6.527275],[2.890959],[0.299445],[-9.476995],[-5.859340],[-8.450382],[-6.363589],[3.167451],[-3.582428],[5.578421],[-1.643654],[6.212074],[-4.340109],[0.813409],[0.842649],[-4.313135],[6.822684],[-5.259440],[0.334141],[8.386816],[3.455620],[-7.935461],[7.300875],[-9.468394],[-4.561143],[-8.746116],[-8.000185],[9.195453],[7.940274],[-8.346775],[9.963596],[-1.085703],[0.085873],[3.539594],[-1.553685],[-3.750388],[9.510422],[2.655048],[8.751192],[-8.192287],[-0.728619],[-9.292855],[-0.127268],[2.315690],[-6.080519],[3.450623],[-9.448700],[-0.768949],[-4.508772],[1.079169],[3.544582],[-5.410571],[-5.783232],[9.147561],[-9.067565],[1.278918],[-5.677417],[4.592387],[-4.997087],[-3.007872],[-7.262987],[-2.244087],[-5.671637],[-7.841467],[6.116650],[0.360252],[-6.366250],[5.017338],[4.108630],[-8.893247],[-5.962322],[-5.503956],[5.138193],[4.944336],[-1.282773],[-6.289423],[1.608471],[-4.137810],[9.794609],[-8.481637],[-5.589021],[2.794690],[-6.243848],[9.522066],[8.533458],[5.949118],[3.342676],[-9.176215],[4.905036],[-1.905700],[-4.761214],[-5.390984],[-8.058413],[8.844066],[-2.624255],[-5.797649],[1.325108],[4.480299],[-0.796715],[3.497937],[-9.656148],[6.723369],[3.957632],[-4.223323],[6.866177],[-1.505358],[7.650223],[-7.111957],[9.930899],[0.728668],[8.693569],[-7.379490],[-8.721469],[-9.556647],[-8.200039],[-0.712697],[-4.590843],[7.239125],[-4.200104],[-6.195262],[-1.018224],[0.412481],[-8.098814],[2.580160],[6.379990],[1.846507],[-0.429734],[1.553544],[4.166464],[9.922709],[3.105402],[-4.116656],[7.381696],[6.289468],[1.783719],[-9.455214],[8.790423],[4.487671],[8.218190],[3.379528],[9.392873],[9.908938],[5.016921],[-3.429340],[7.601396],[-5.342841],[-6.785046],[-5.575704],[-5.934644],[6.347366],[-1.745926],[-1.702402],[6.931211],[5.693233],[-8.048698],[4.409567],[3.812048],[-2.772228],[5.557413],[0.457986],[-0.678961],[4.146280],[-5.908155],[0.451489],[-7.658001],[-4.504456],[-1.781540],[-6.280147],[-7.309372],[-1.971974],[-0.963535],[-8.706822],[-5.417781],[-9.844415],[-9.278430],[-5.990838],[-5.861519],[8.291756],[-2.866309],[5.964323],[0.469331],[0.346925],[-5.134893],[2.451364],[8.309656],[-2.770815],[4.515312],[8.229926],[5.729639],[8.085353],[3.467750],[-8.812970],[0.581590],[-5.426064],[-5.113922],[-9.223849],[3.527136],[4.228705],[4.033713],[-6.742297],[-7.800961],[6.718061],[1.141552],[-1.805574],[-5.299561],[-3.966526],[7.268202],[5.249663],[-4.948085],[-5.113322],[-6.350167],[-2.999227],[-6.567418],[3.257643],[-1.380178],[-5.881076],[-2.875041]], dtype = "float32")#candidate|3552|(360, 1)|const|float32
call_3550 = relay.TupleGetItem(func_3230_call(relay.reshape(var_3551.astype('float64'), [15, 8, 16]), relay.reshape(const_3552.astype('float32'), [360,]), ), 0)
call_3553 = relay.TupleGetItem(func_3233_call(relay.reshape(var_3551.astype('float64'), [15, 8, 16]), relay.reshape(const_3552.astype('float32'), [360,]), ), 0)
output = relay.Tuple([call_3544,call_3550,var_3551,const_3552,])
output2 = relay.Tuple([call_3545,call_3553,var_3551,const_3552,])
func_3555 = relay.Function([var_3551,], output)
mod['func_3555'] = func_3555
mod = relay.transform.InferType()(mod)
var_3556 = relay.var("var_3556", dtype = "float64", shape = (1920,))#candidate|3556|(1920,)|var|float64
output = func_3555(var_3556)
func_3557 = relay.Function([var_3556], output)
mutated_mod['func_3557'] = func_3557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_3570 = relay.TupleGetItem(func_1381_call(), 0)
call_3571 = relay.TupleGetItem(func_1382_call(), 0)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_3599 = relay.TupleGetItem(func_2902_call(), 0)
call_3600 = relay.TupleGetItem(func_2904_call(), 0)
func_3462_call = mod.get_global_var('func_3462')
func_3464_call = mutated_mod.get_global_var('func_3464')
call_3603 = relay.TupleGetItem(func_3462_call(), 0)
call_3604 = relay.TupleGetItem(func_3464_call(), 0)
output = relay.Tuple([call_3570,call_3599,call_3603,])
output2 = relay.Tuple([call_3571,call_3600,call_3604,])
func_3606 = relay.Function([], output)
mod['func_3606'] = func_3606
mod = relay.transform.InferType()(mod)
output = func_3606()
func_3607 = relay.Function([], output)
mutated_mod['func_3607'] = func_3607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2223_call = mod.get_global_var('func_2223')
func_2224_call = mutated_mod.get_global_var('func_2224')
call_3639 = relay.TupleGetItem(func_2223_call(), 0)
call_3640 = relay.TupleGetItem(func_2224_call(), 0)
func_1585_call = mod.get_global_var('func_1585')
func_1587_call = mutated_mod.get_global_var('func_1587')
call_3644 = relay.TupleGetItem(func_1585_call(), 0)
call_3645 = relay.TupleGetItem(func_1587_call(), 0)
bop_3646 = relay.greater_equal(call_3639.astype('bool'), relay.reshape(call_3644.astype('bool'), relay.shape_of(call_3639))) # shape=(15, 1, 16)
bop_3649 = relay.greater_equal(call_3640.astype('bool'), relay.reshape(call_3645.astype('bool'), relay.shape_of(call_3640))) # shape=(15, 1, 16)
output = bop_3646
output2 = bop_3649
func_3650 = relay.Function([], output)
mod['func_3650'] = func_3650
mod = relay.transform.InferType()(mod)
output = func_3650()
func_3651 = relay.Function([], output)
mutated_mod['func_3651'] = func_3651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3655 = relay.var("var_3655", dtype = "float64", shape = (8, 7, 13))#candidate|3655|(8, 7, 13)|var|float64
var_3656 = relay.var("var_3656", dtype = "float64", shape = (8, 7, 13))#candidate|3656|(8, 7, 13)|var|float64
bop_3657 = relay.less(var_3655.astype('bool'), relay.reshape(var_3656.astype('bool'), relay.shape_of(var_3655))) # shape=(8, 7, 13)
output = relay.Tuple([bop_3657,])
output2 = relay.Tuple([bop_3657,])
func_3678 = relay.Function([var_3655,var_3656,], output)
mod['func_3678'] = func_3678
mod = relay.transform.InferType()(mod)
mutated_mod['func_3678'] = func_3678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3678_call = mutated_mod.get_global_var('func_3678')
var_3680 = relay.var("var_3680", dtype = "float64", shape = (8, 7, 13))#candidate|3680|(8, 7, 13)|var|float64
var_3681 = relay.var("var_3681", dtype = "float64", shape = (8, 7, 13))#candidate|3681|(8, 7, 13)|var|float64
call_3679 = func_3678_call(var_3680,var_3681,)
output = call_3679
func_3682 = relay.Function([var_3680,var_3681,], output)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3801 = relay.var("var_3801", dtype = "int8", shape = (11, 5, 3))#candidate|3801|(11, 5, 3)|var|int8
const_3802 = relay.const([[[5,-2,-4],[-6,5,7],[-6,-6,1],[3,-9,8],[4,-1,-10]],[[-6,-9,-7],[-9,2,-1],[-9,-3,-5],[4,-8,10],[-8,-8,3]],[[10,-2,-8],[-1,-4,-10],[-6,-1,-4],[5,6,-1],[-9,-3,8]],[[4,7,-8],[-3,-1,-4],[3,10,8],[2,-3,7],[7,5,-5]],[[-7,-10,3],[9,-8,4],[-1,-3,2],[-6,5,7],[5,9,3]],[[2,3,4],[1,3,-2],[-1,-5,-6],[6,-3,3],[-4,-3,6]],[[-9,6,10],[7,1,-1],[6,-10,6],[7,-9,-4],[10,1,-1]],[[9,-7,1],[7,9,5],[-3,-3,1],[10,-1,8],[-1,3,4]],[[-1,5,10],[-5,3,4],[-5,-10,-3],[-10,-9,-2],[-6,7,-7]],[[5,-6,5],[-6,2,8],[9,7,4],[10,-3,-2],[-6,-9,10]],[[-6,5,-5],[7,-3,-3],[6,-4,1],[1,1,10],[8,-4,3]]], dtype = "int8")#candidate|3802|(11, 5, 3)|const|int8
bop_3803 = relay.bitwise_or(var_3801.astype('int8'), relay.reshape(const_3802.astype('int8'), relay.shape_of(var_3801))) # shape=(11, 5, 3)
func_1683_call = mod.get_global_var('func_1683')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_3814 = relay.TupleGetItem(func_1683_call(), 1)
call_3815 = relay.TupleGetItem(func_1684_call(), 1)
var_3819 = relay.var("var_3819", dtype = "float64", shape = (15, 11, 16))#candidate|3819|(15, 11, 16)|var|float64
bop_3820 = relay.floor_mod(call_3814.astype('float32'), var_3819.astype('float32')) # shape=(15, 11, 16)
bop_3823 = relay.floor_mod(call_3815.astype('float32'), var_3819.astype('float32')) # shape=(15, 11, 16)
bop_3826 = relay.less(bop_3820.astype('bool'), relay.reshape(var_3819.astype('bool'), relay.shape_of(bop_3820))) # shape=(15, 11, 16)
bop_3829 = relay.less(bop_3823.astype('bool'), relay.reshape(var_3819.astype('bool'), relay.shape_of(bop_3823))) # shape=(15, 11, 16)
output = relay.Tuple([bop_3803,bop_3826,])
output2 = relay.Tuple([bop_3803,bop_3829,])
func_3835 = relay.Function([var_3801,var_3819,], output)
mod['func_3835'] = func_3835
mod = relay.transform.InferType()(mod)
var_3836 = relay.var("var_3836", dtype = "int8", shape = (11, 5, 3))#candidate|3836|(11, 5, 3)|var|int8
var_3837 = relay.var("var_3837", dtype = "float64", shape = (15, 11, 16))#candidate|3837|(15, 11, 16)|var|float64
output = func_3835(var_3836,var_3837,)
func_3838 = relay.Function([var_3836,var_3837,], output)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3855 = relay.var("var_3855", dtype = "float32", shape = (7, 3, 4))#candidate|3855|(7, 3, 4)|var|float32
var_3856 = relay.var("var_3856", dtype = "float32", shape = (7, 3, 4))#candidate|3856|(7, 3, 4)|var|float32
bop_3857 = relay.equal(var_3855.astype('bool'), relay.reshape(var_3856.astype('bool'), relay.shape_of(var_3855))) # shape=(7, 3, 4)
uop_3865 = relay.exp(bop_3857.astype('float64')) # shape=(7, 3, 4)
func_2869_call = mod.get_global_var('func_2869')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_3869 = relay.TupleGetItem(func_2869_call(), 0)
call_3870 = relay.TupleGetItem(func_2871_call(), 0)
output = relay.Tuple([uop_3865,call_3869,])
output2 = relay.Tuple([uop_3865,call_3870,])
func_3872 = relay.Function([var_3855,var_3856,], output)
mod['func_3872'] = func_3872
mod = relay.transform.InferType()(mod)
mutated_mod['func_3872'] = func_3872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3872_call = mutated_mod.get_global_var('func_3872')
var_3874 = relay.var("var_3874", dtype = "float32", shape = (7, 3, 4))#candidate|3874|(7, 3, 4)|var|float32
var_3875 = relay.var("var_3875", dtype = "float32", shape = (7, 3, 4))#candidate|3875|(7, 3, 4)|var|float32
call_3873 = func_3872_call(var_3874,var_3875,)
output = call_3873
func_3876 = relay.Function([var_3874,var_3875,], output)
mutated_mod['func_3876'] = func_3876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_3942 = relay.TupleGetItem(func_1159_call(), 2)
call_3943 = relay.TupleGetItem(func_1160_call(), 2)
output = call_3942
output2 = call_3943
func_3959 = relay.Function([], output)
mod['func_3959'] = func_3959
mod = relay.transform.InferType()(mod)
mutated_mod['func_3959'] = func_3959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3959_call = mutated_mod.get_global_var('func_3959')
call_3960 = func_3959_call()
output = call_3960
func_3961 = relay.Function([], output)
mutated_mod['func_3961'] = func_3961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_3989 = func_1470_call()
call_3990 = func_1470_call()
func_2979_call = mod.get_global_var('func_2979')
func_2982_call = mutated_mod.get_global_var('func_2982')
const_3992 = relay.const([7.538682,0.881481,-9.966282,-1.083477,2.852223,4.949892,4.767510,8.375971,-6.861732,-6.384675,-2.902575,-1.215950,4.101650,7.332477,5.802090,6.434000,-1.998023,3.271405,5.950950,-5.152864,-2.454245,-5.260243,-6.441570,5.139788,2.523325,5.272333,-0.195527,9.306614,-3.699280,8.753657,-0.209184,-7.711326,0.757290,7.437104,-0.990823,-9.356632,4.278664,-8.863782,-4.798308,7.876349,-6.153860,2.973033,-0.497741,-5.788959,-4.982818,-8.780158,-3.263417,1.675170,5.115669,-4.583810,0.535131,-1.042328,-5.514959,-1.953991,-3.315543,-0.010817,-1.676631,-2.680470,7.101955,9.322221,-7.026362,-0.162087,3.327583,-1.710551,-5.249029,-6.712143,3.403454,-2.688166,8.770378,-5.155480,-4.482990,-0.342603,0.373980,1.278390,-1.164725,-0.420446,4.597752,4.867159,-5.517096,8.151679,2.250271,-6.359793,-4.743136,-7.758568,7.486275,3.546189,0.290671,0.284325,-9.573042,8.253148,6.669565,0.044093,-3.672605,4.409473,2.911869,5.349095,-3.191299,0.717242,3.556611,8.917143,6.333864,-8.706565,-6.678345,0.773447,1.881869,5.206929,-4.517460,0.046403,-8.295253,8.962868,5.933916,-7.232508,9.087618,-9.963562,7.543952,7.324221,-4.712881,7.282662,3.467160,-8.065401,-9.065829,-0.723331,-4.578479,4.630438,-7.241521,-5.898692,-7.050624,-0.260788,2.904087,-6.932114,-7.263456,1.185414,6.822871,0.581693,9.569632,7.617138,-3.930063,-3.039593,4.576848,1.795226,-4.216012,7.409438,-3.929788,-2.721687,-6.923395,-4.076929,0.185082,-2.067292,-4.085374,0.704226,0.822731,0.507735,-0.844866,-7.476144,-8.587489,-4.584467,-4.123185,6.035512,9.472307,-0.811108,-9.948483,-7.049466,-5.403622,-7.070846,-5.626862,-8.101707,3.921554,4.431935,4.106172,2.421336,0.981360,-1.887028,-9.329262,-9.000394,-9.473547,0.850361,7.594616,-7.477553,-9.190937,5.336323,-7.028949,-3.347032,2.513866,-5.044313,-0.892026,-4.231027,1.499397,5.168032,-5.892314,3.251469,-2.469687,4.309638,-3.039715,6.016023,2.300362,6.790519,-8.771309,3.859441,-7.856230,-2.391102,0.328588,-9.974462,6.237774,-8.261647,-4.996071,-1.979142,7.196129,-4.349637,9.053133,-8.958265,-4.353531,6.187399,-0.478830,5.220608,-7.592878,5.721909,-1.245369,-5.279278,9.873379,-0.817930,-4.027701,-9.642796,-4.082245,8.907835,-7.451684,-5.270286,2.751113,0.460634,-3.499387,-3.244803,-9.672428,3.583816,-0.621109,-6.899636,-2.627323,3.334664,-7.811062,-7.739485,-0.930059,-3.194570,-0.427843,-4.055619,-6.417074,4.755713,-9.852379,8.067807,3.097452,1.981356,-5.998648,5.104046,-7.718568,6.013208,-3.631393,-2.844922,1.001837,2.489197,4.896898,-9.933750,6.554000,2.546343,5.603419,-2.658788,0.498580,-3.067487,7.267508,-0.771455,-6.520786,-8.785659,-1.954275,-3.332338], dtype = "float32")#candidate|3992|(270,)|const|float32
call_3991 = func_2979_call(relay.reshape(const_3992.astype('float32'), [9, 5, 6]))
call_3993 = func_2979_call(relay.reshape(const_3992.astype('float32'), [9, 5, 6]))
func_3026_call = mod.get_global_var('func_3026')
func_3029_call = mutated_mod.get_global_var('func_3029')
var_3997 = relay.var("var_3997", dtype = "float64", shape = (2640,))#candidate|3997|(2640,)|var|float64
call_3996 = relay.TupleGetItem(func_3026_call(relay.reshape(var_3997.astype('float64'), [15, 11, 16])), 1)
call_3998 = relay.TupleGetItem(func_3029_call(relay.reshape(var_3997.astype('float64'), [15, 11, 16])), 1)
uop_4003 = relay.acos(call_3996.astype('float32')) # shape=(15, 11, 16)
uop_4005 = relay.acos(call_3998.astype('float32')) # shape=(15, 11, 16)
func_2953_call = mod.get_global_var('func_2953')
func_2955_call = mutated_mod.get_global_var('func_2955')
call_4006 = func_2953_call()
call_4007 = func_2953_call()
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_4019 = relay.TupleGetItem(func_2156_call(), 0)
call_4020 = relay.TupleGetItem(func_2158_call(), 0)
uop_4030 = relay.rsqrt(uop_4003.astype('float64')) # shape=(15, 11, 16)
uop_4032 = relay.rsqrt(uop_4005.astype('float64')) # shape=(15, 11, 16)
uop_4040 = relay.atanh(uop_4003.astype('float32')) # shape=(15, 11, 16)
uop_4042 = relay.atanh(uop_4005.astype('float32')) # shape=(15, 11, 16)
output = relay.Tuple([call_3989,call_3991,const_3992,var_3997,call_4006,call_4019,uop_4030,uop_4040,])
output2 = relay.Tuple([call_3990,call_3993,const_3992,var_3997,call_4007,call_4020,uop_4032,uop_4042,])
func_4060 = relay.Function([var_3997,], output)
mod['func_4060'] = func_4060
mod = relay.transform.InferType()(mod)
mutated_mod['func_4060'] = func_4060
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4061 = relay.var("var_4061", dtype = "float64", shape = (2640,))#candidate|4061|(2640,)|var|float64
func_4060_call = mutated_mod.get_global_var('func_4060')
call_4062 = func_4060_call(var_4061)
output = call_4062
func_4063 = relay.Function([var_4061], output)
mutated_mod['func_4063'] = func_4063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_4065 = relay.TupleGetItem(func_1159_call(), 2)
call_4066 = relay.TupleGetItem(func_1160_call(), 2)
func_3105_call = mod.get_global_var('func_3105')
func_3108_call = mutated_mod.get_global_var('func_3108')
var_4074 = relay.var("var_4074", dtype = "float32", shape = (96,))#candidate|4074|(96,)|var|float32
call_4073 = func_3105_call(relay.reshape(var_4074.astype('float32'), [12, 1, 8]))
call_4075 = func_3105_call(relay.reshape(var_4074.astype('float32'), [12, 1, 8]))
output = relay.Tuple([call_4065,call_4073,var_4074,])
output2 = relay.Tuple([call_4066,call_4075,var_4074,])
func_4083 = relay.Function([var_4074,], output)
mod['func_4083'] = func_4083
mod = relay.transform.InferType()(mod)
mutated_mod['func_4083'] = func_4083
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4084 = relay.var("var_4084", dtype = "float32", shape = (96,))#candidate|4084|(96,)|var|float32
func_4083_call = mutated_mod.get_global_var('func_4083')
call_4085 = func_4083_call(var_4084)
output = call_4085
func_4086 = relay.Function([var_4084], output)
mutated_mod['func_4086'] = func_4086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mod.get_global_var('func_2953')
func_2955_call = mutated_mod.get_global_var('func_2955')
call_4097 = func_2953_call()
call_4098 = func_2953_call()
output = relay.Tuple([call_4097,])
output2 = relay.Tuple([call_4098,])
func_4107 = relay.Function([], output)
mod['func_4107'] = func_4107
mod = relay.transform.InferType()(mod)
output = func_4107()
func_4108 = relay.Function([], output)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1524_call = mod.get_global_var('func_1524')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_4133 = relay.TupleGetItem(func_1524_call(), 0)
call_4134 = relay.TupleGetItem(func_1525_call(), 0)
uop_4146 = relay.acosh(call_4133.astype('float64')) # shape=(15, 1, 16)
uop_4148 = relay.acosh(call_4134.astype('float64')) # shape=(15, 1, 16)
output = relay.Tuple([uop_4146,])
output2 = relay.Tuple([uop_4148,])
func_4154 = relay.Function([], output)
mod['func_4154'] = func_4154
mod = relay.transform.InferType()(mod)
output = func_4154()
func_4155 = relay.Function([], output)
mutated_mod['func_4155'] = func_4155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2953_call = mod.get_global_var('func_2953')
func_2955_call = mutated_mod.get_global_var('func_2955')
call_4182 = func_2953_call()
call_4183 = func_2953_call()
func_3354_call = mod.get_global_var('func_3354')
func_3356_call = mutated_mod.get_global_var('func_3356')
call_4186 = relay.TupleGetItem(func_3354_call(), 1)
call_4187 = relay.TupleGetItem(func_3356_call(), 1)
var_4190 = relay.var("var_4190", dtype = "float64", shape = (15, 12, 16))#candidate|4190|(15, 12, 16)|var|float64
bop_4191 = relay.less_equal(call_4186.astype('bool'), var_4190.astype('bool')) # shape=(15, 12, 16)
bop_4194 = relay.less_equal(call_4187.astype('bool'), var_4190.astype('bool')) # shape=(15, 12, 16)
output = relay.Tuple([call_4182,bop_4191,])
output2 = relay.Tuple([call_4183,bop_4194,])
func_4198 = relay.Function([var_4190,], output)
mod['func_4198'] = func_4198
mod = relay.transform.InferType()(mod)
var_4199 = relay.var("var_4199", dtype = "float64", shape = (15, 12, 16))#candidate|4199|(15, 12, 16)|var|float64
output = func_4198(var_4199)
func_4200 = relay.Function([var_4199], output)
mutated_mod['func_4200'] = func_4200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4408 = relay.TupleGetItem(func_4107_call(), 0)
call_4409 = relay.TupleGetItem(func_4108_call(), 0)
var_4427 = relay.var("var_4427", dtype = "bool", shape = (15, 3, 16))#candidate|4427|(15, 3, 16)|var|bool
bop_4428 = relay.floor_mod(call_4408.astype('float32'), var_4427.astype('float32')) # shape=(15, 3, 16)
bop_4431 = relay.floor_mod(call_4409.astype('float32'), var_4427.astype('float32')) # shape=(15, 3, 16)
func_2953_call = mod.get_global_var('func_2953')
func_2955_call = mutated_mod.get_global_var('func_2955')
call_4434 = func_2953_call()
call_4435 = func_2953_call()
output = relay.Tuple([bop_4428,call_4434,])
output2 = relay.Tuple([bop_4431,call_4435,])
func_4438 = relay.Function([var_4427,], output)
mod['func_4438'] = func_4438
mod = relay.transform.InferType()(mod)
mutated_mod['func_4438'] = func_4438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4439 = relay.var("var_4439", dtype = "bool", shape = (15, 3, 16))#candidate|4439|(15, 3, 16)|var|bool
func_4438_call = mutated_mod.get_global_var('func_4438')
call_4440 = func_4438_call(var_4439)
output = call_4440
func_4441 = relay.Function([var_4439], output)
mutated_mod['func_4441'] = func_4441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_4474 = relay.TupleGetItem(func_1381_call(), 0)
call_4475 = relay.TupleGetItem(func_1382_call(), 0)
func_2223_call = mod.get_global_var('func_2223')
func_2224_call = mutated_mod.get_global_var('func_2224')
call_4509 = relay.TupleGetItem(func_2223_call(), 0)
call_4510 = relay.TupleGetItem(func_2224_call(), 0)
bop_4511 = relay.logical_or(call_4474.astype('bool'), relay.reshape(call_4509.astype('bool'), relay.shape_of(call_4474))) # shape=(15, 1, 16)
bop_4514 = relay.logical_or(call_4475.astype('bool'), relay.reshape(call_4510.astype('bool'), relay.shape_of(call_4475))) # shape=(15, 1, 16)
func_3533_call = mod.get_global_var('func_3533')
func_3535_call = mutated_mod.get_global_var('func_3535')
call_4519 = func_3533_call()
call_4520 = func_3533_call()
const_4523 = relay.const([[[3.448444,5.570176,-9.344166,1.029149,0.586066,1.031267,-1.696019,-1.446212,3.841944,0.028609,-0.606252,-7.332701,-7.688932,0.945237,-4.965052,1.194264],[-1.668017,-1.370553,-5.018441,9.371327,2.382745,2.820009,-8.613745,-0.619099,-9.470291,-8.442103,-0.937487,2.515360,9.339408,9.173245,8.553108,5.234116],[7.382745,6.289563,8.482314,7.728861,5.071321,-8.182095,-0.780822,0.246284,2.638910,0.786530,-3.574939,-8.252509,-1.148526,5.216411,-9.276419,4.201266],[-0.575057,0.547268,2.920604,5.598987,-7.678277,6.617179,-7.658748,0.697290,-4.198834,-0.901572,-8.705033,-9.522794,-1.860763,-6.911132,-9.849522,9.552494],[-9.418319,-7.269508,3.072297,5.958525,2.149881,4.597639,8.711941,4.065803,0.592567,6.790823,-4.498102,-7.423342,4.158414,3.814955,-0.127717,7.737796],[-2.200219,8.718865,4.814977,5.413258,0.862325,-9.052715,8.891341,-8.336252,1.332263,-2.463388,3.980395,2.025199,-9.236442,-8.059247,4.734537,9.638791]],[[7.666174,6.136879,8.659100,3.985552,1.183881,-7.170467,-4.758557,-4.257652,-2.664495,4.706985,9.238741,-0.407871,-8.572883,0.003900,-9.656198,1.850371],[7.128809,-9.111960,2.845998,2.215538,-4.896792,0.452256,-8.872764,-0.106792,5.869517,-2.691342,-7.825124,-2.169708,5.491519,-3.021641,-7.780678,8.734121],[6.623642,5.654897,8.661373,5.331535,-3.507831,-5.152601,-5.879048,7.858047,2.603066,8.952161,-8.468559,-2.975215,8.242972,-6.719056,-4.002605,0.294664],[6.663745,-1.744484,6.466946,-7.798480,-5.670754,-3.504687,-7.298766,-3.204493,1.059339,1.416538,3.747218,7.995236,6.259282,0.915999,6.533034,8.317978],[6.387648,5.246845,3.744413,-3.558936,4.794799,3.228992,-3.144762,7.640747,1.800036,1.059112,-2.080772,3.019828,-4.542719,4.075092,5.410997,7.569146],[-6.675941,3.353173,-6.600226,0.579317,-9.442751,2.862449,5.215837,-8.175003,-7.071014,0.978605,-2.539187,-7.847501,5.907436,-3.253432,-5.062619,7.335107]],[[-4.769206,-0.256321,-6.395203,-6.737982,-6.174002,4.963209,-7.580148,-0.822142,-5.096096,7.165092,-7.899687,7.883787,7.669929,-8.570157,3.471452,-2.226350],[-3.833033,7.340765,5.898629,0.250816,0.148396,2.326681,-0.764704,-9.235084,0.683290,5.419230,9.854253,-6.996155,-0.750778,-4.485193,-4.890458,-5.535603],[-1.744947,-7.030483,0.026723,7.234208,-7.975004,0.366294,0.476388,9.894411,2.572004,-1.362806,-3.010578,-1.894402,-4.040119,-0.961276,6.880133,5.014023],[-8.934494,7.132646,-4.545761,0.850571,1.387243,5.178411,-0.243404,-5.874142,-9.027311,1.885735,5.237671,7.482215,-4.067671,-2.805039,-7.246155,6.031160],[1.373554,9.368634,-2.405638,8.731463,1.202534,-0.160927,2.582042,6.887842,2.248477,-6.834256,-8.457323,-3.044074,-8.947821,8.445847,8.562434,2.622975],[3.893847,-8.001459,8.077694,-5.221057,-4.790093,6.688573,0.932380,7.233632,4.436333,1.271474,-8.394834,-2.119430,-0.916641,5.506164,0.745077,3.953711]]], dtype = "float64")#candidate|4523|(3, 6, 16)|const|float64
bop_4524 = relay.left_shift(call_4519.astype('int64'), relay.reshape(const_4523.astype('int64'), relay.shape_of(call_4519))) # shape=(3, 6, 16)
bop_4527 = relay.left_shift(call_4520.astype('int64'), relay.reshape(const_4523.astype('int64'), relay.shape_of(call_4520))) # shape=(3, 6, 16)
uop_4529 = relay.cosh(call_4474.astype('float32')) # shape=(15, 1, 16)
uop_4531 = relay.cosh(call_4475.astype('float32')) # shape=(15, 1, 16)
output = relay.Tuple([bop_4511,bop_4524,uop_4529,])
output2 = relay.Tuple([bop_4514,bop_4527,uop_4531,])
func_4544 = relay.Function([], output)
mod['func_4544'] = func_4544
mod = relay.transform.InferType()(mod)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4544_call = mutated_mod.get_global_var('func_4544')
call_4545 = func_4544_call()
output = call_4545
func_4546 = relay.Function([], output)
mutated_mod['func_4546'] = func_4546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_4574 = relay.TupleGetItem(func_1159_call(), 0)
call_4575 = relay.TupleGetItem(func_1160_call(), 0)
output = call_4574
output2 = call_4575
func_4597 = relay.Function([], output)
mod['func_4597'] = func_4597
mod = relay.transform.InferType()(mod)
output = func_4597()
func_4598 = relay.Function([], output)
mutated_mod['func_4598'] = func_4598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1585_call = mod.get_global_var('func_1585')
func_1587_call = mutated_mod.get_global_var('func_1587')
call_4599 = relay.TupleGetItem(func_1585_call(), 0)
call_4600 = relay.TupleGetItem(func_1587_call(), 0)
output = call_4599
output2 = call_4600
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
func_2788_call = mod.get_global_var('func_2788')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_4659 = relay.TupleGetItem(func_2788_call(), 0)
call_4660 = relay.TupleGetItem(func_2789_call(), 0)
uop_4665 = relay.erf(call_4659.astype('float64')) # shape=(15, 1, 16)
uop_4667 = relay.erf(call_4660.astype('float64')) # shape=(15, 1, 16)
output = relay.Tuple([uop_4665,])
output2 = relay.Tuple([uop_4667,])
func_4685 = relay.Function([], output)
mod['func_4685'] = func_4685
mod = relay.transform.InferType()(mod)
mutated_mod['func_4685'] = func_4685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4685_call = mutated_mod.get_global_var('func_4685')
call_4686 = func_4685_call()
output = call_4686
func_4687 = relay.Function([], output)
mutated_mod['func_4687'] = func_4687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_4691 = relay.TupleGetItem(func_3366_call(), 0)
call_4692 = relay.TupleGetItem(func_3368_call(), 0)
func_3606_call = mod.get_global_var('func_3606')
func_3607_call = mutated_mod.get_global_var('func_3607')
call_4706 = relay.TupleGetItem(func_3606_call(), 2)
call_4707 = relay.TupleGetItem(func_3607_call(), 2)
output = relay.Tuple([call_4691,call_4706,])
output2 = relay.Tuple([call_4692,call_4707,])
func_4708 = relay.Function([], output)
mod['func_4708'] = func_4708
mod = relay.transform.InferType()(mod)
output = func_4708()
func_4709 = relay.Function([], output)
mutated_mod['func_4709'] = func_4709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4685_call = mod.get_global_var('func_4685')
func_4687_call = mutated_mod.get_global_var('func_4687')
call_4710 = relay.TupleGetItem(func_4685_call(), 0)
call_4711 = relay.TupleGetItem(func_4687_call(), 0)
func_3026_call = mod.get_global_var('func_3026')
func_3029_call = mutated_mod.get_global_var('func_3029')
var_4741 = relay.var("var_4741", dtype = "float64", shape = (132, 20))#candidate|4741|(132, 20)|var|float64
call_4740 = relay.TupleGetItem(func_3026_call(relay.reshape(var_4741.astype('float64'), [15, 11, 16])), 0)
call_4742 = relay.TupleGetItem(func_3029_call(relay.reshape(var_4741.astype('float64'), [15, 11, 16])), 0)
bop_4743 = relay.bitwise_or(var_4741.astype('uint64'), relay.reshape(call_4740.astype('uint64'), relay.shape_of(var_4741))) # shape=(132, 20)
bop_4746 = relay.bitwise_or(var_4741.astype('uint64'), relay.reshape(call_4742.astype('uint64'), relay.shape_of(var_4741))) # shape=(132, 20)
output = relay.Tuple([call_4710,bop_4743,])
output2 = relay.Tuple([call_4711,bop_4746,])
func_4752 = relay.Function([var_4741,], output)
mod['func_4752'] = func_4752
mod = relay.transform.InferType()(mod)
var_4753 = relay.var("var_4753", dtype = "float64", shape = (132, 20))#candidate|4753|(132, 20)|var|float64
output = func_4752(var_4753)
func_4754 = relay.Function([var_4753], output)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4779 = relay.TupleGetItem(func_4107_call(), 0)
call_4780 = relay.TupleGetItem(func_4108_call(), 0)
output = relay.Tuple([call_4779,])
output2 = relay.Tuple([call_4780,])
func_4783 = relay.Function([], output)
mod['func_4783'] = func_4783
mod = relay.transform.InferType()(mod)
mutated_mod['func_4783'] = func_4783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mutated_mod.get_global_var('func_4783')
call_4784 = func_4783_call()
output = call_4784
func_4785 = relay.Function([], output)
mutated_mod['func_4785'] = func_4785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3496_call = mod.get_global_var('func_3496')
func_3498_call = mutated_mod.get_global_var('func_3498')
call_4790 = func_3496_call()
call_4791 = func_3496_call()
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_4795 = relay.TupleGetItem(func_3366_call(), 0)
call_4796 = relay.TupleGetItem(func_3368_call(), 0)
func_3678_call = mod.get_global_var('func_3678')
func_3682_call = mutated_mod.get_global_var('func_3682')
var_4803 = relay.var("var_4803", dtype = "float64", shape = (728,))#candidate|4803|(728,)|var|float64
call_4802 = relay.TupleGetItem(func_3678_call(relay.reshape(var_4803.astype('float64'), [8, 7, 13]), relay.reshape(var_4803.astype('float64'), [8, 7, 13]), ), 0)
call_4804 = relay.TupleGetItem(func_3682_call(relay.reshape(var_4803.astype('float64'), [8, 7, 13]), relay.reshape(var_4803.astype('float64'), [8, 7, 13]), ), 0)
output = relay.Tuple([call_4790,call_4795,call_4802,var_4803,])
output2 = relay.Tuple([call_4791,call_4796,call_4804,var_4803,])
func_4805 = relay.Function([var_4803,], output)
mod['func_4805'] = func_4805
mod = relay.transform.InferType()(mod)
var_4806 = relay.var("var_4806", dtype = "float64", shape = (728,))#candidate|4806|(728,)|var|float64
output = func_4805(var_4806)
func_4807 = relay.Function([var_4806], output)
mutated_mod['func_4807'] = func_4807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2788_call = mod.get_global_var('func_2788')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_4827 = relay.TupleGetItem(func_2788_call(), 0)
call_4828 = relay.TupleGetItem(func_2789_call(), 0)
func_2426_call = mod.get_global_var('func_2426')
func_2429_call = mutated_mod.get_global_var('func_2429')
var_4830 = relay.var("var_4830", dtype = "float32", shape = (360,))#candidate|4830|(360,)|var|float32
var_4831 = relay.var("var_4831", dtype = "float64", shape = (3840,))#candidate|4831|(3840,)|var|float64
call_4829 = relay.TupleGetItem(func_2426_call(relay.reshape(var_4830.astype('float32'), [360,]), relay.reshape(var_4831.astype('float64'), [15, 16, 16]), ), 7)
call_4832 = relay.TupleGetItem(func_2429_call(relay.reshape(var_4830.astype('float32'), [360,]), relay.reshape(var_4831.astype('float64'), [15, 16, 16]), ), 7)
output = relay.Tuple([call_4827,call_4829,var_4830,var_4831,])
output2 = relay.Tuple([call_4828,call_4832,var_4830,var_4831,])
func_4839 = relay.Function([var_4830,var_4831,], output)
mod['func_4839'] = func_4839
mod = relay.transform.InferType()(mod)
var_4840 = relay.var("var_4840", dtype = "float32", shape = (360,))#candidate|4840|(360,)|var|float32
var_4841 = relay.var("var_4841", dtype = "float64", shape = (3840,))#candidate|4841|(3840,)|var|float64
output = func_4839(var_4840,var_4841,)
func_4842 = relay.Function([var_4840,var_4841,], output)
mutated_mod['func_4842'] = func_4842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_4888 = relay.TupleGetItem(func_4107_call(), 0)
call_4889 = relay.TupleGetItem(func_4108_call(), 0)
output = call_4888
output2 = call_4889
func_4895 = relay.Function([], output)
mod['func_4895'] = func_4895
mod = relay.transform.InferType()(mod)
output = func_4895()
func_4896 = relay.Function([], output)
mutated_mod['func_4896'] = func_4896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mod.get_global_var('func_4783')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_4945 = relay.TupleGetItem(func_4783_call(), 0)
call_4946 = relay.TupleGetItem(func_4785_call(), 0)
output = relay.Tuple([call_4945,])
output2 = relay.Tuple([call_4946,])
func_4951 = relay.Function([], output)
mod['func_4951'] = func_4951
mod = relay.transform.InferType()(mod)
output = func_4951()
func_4952 = relay.Function([], output)
mutated_mod['func_4952'] = func_4952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_4965 = relay.TupleGetItem(func_3366_call(), 0)
call_4966 = relay.TupleGetItem(func_3368_call(), 0)
func_4951_call = mod.get_global_var('func_4951')
func_4952_call = mutated_mod.get_global_var('func_4952')
call_4986 = relay.TupleGetItem(func_4951_call(), 0)
call_4987 = relay.TupleGetItem(func_4952_call(), 0)
func_3555_call = mod.get_global_var('func_3555')
func_3557_call = mutated_mod.get_global_var('func_3557')
var_4989 = relay.var("var_4989", dtype = "float64", shape = (1920,))#candidate|4989|(1920,)|var|float64
call_4988 = relay.TupleGetItem(func_3555_call(relay.reshape(var_4989.astype('float64'), [1920,])), 3)
call_4990 = relay.TupleGetItem(func_3557_call(relay.reshape(var_4989.astype('float64'), [1920,])), 3)
uop_4994 = relay.acosh(call_4988.astype('float64')) # shape=(360, 1)
uop_4996 = relay.acosh(call_4990.astype('float64')) # shape=(360, 1)
output = relay.Tuple([call_4965,call_4986,var_4989,uop_4994,])
output2 = relay.Tuple([call_4966,call_4987,var_4989,uop_4996,])
func_4997 = relay.Function([var_4989,], output)
mod['func_4997'] = func_4997
mod = relay.transform.InferType()(mod)
var_4998 = relay.var("var_4998", dtype = "float64", shape = (1920,))#candidate|4998|(1920,)|var|float64
output = func_4997(var_4998)
func_4999 = relay.Function([var_4998], output)
mutated_mod['func_4999'] = func_4999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_5011 = relay.TupleGetItem(func_4154_call(), 0)
call_5012 = relay.TupleGetItem(func_4155_call(), 0)
var_5020 = relay.var("var_5020", dtype = "float64", shape = (15, 1, 16))#candidate|5020|(15, 1, 16)|var|float64
bop_5021 = relay.bitwise_xor(call_5011.astype('uint16'), relay.reshape(var_5020.astype('uint16'), relay.shape_of(call_5011))) # shape=(15, 1, 16)
bop_5024 = relay.bitwise_xor(call_5012.astype('uint16'), relay.reshape(var_5020.astype('uint16'), relay.shape_of(call_5012))) # shape=(15, 1, 16)
func_4685_call = mod.get_global_var('func_4685')
func_4687_call = mutated_mod.get_global_var('func_4687')
call_5032 = relay.TupleGetItem(func_4685_call(), 0)
call_5033 = relay.TupleGetItem(func_4687_call(), 0)
output = relay.Tuple([bop_5021,call_5032,])
output2 = relay.Tuple([bop_5024,call_5033,])
func_5036 = relay.Function([var_5020,], output)
mod['func_5036'] = func_5036
mod = relay.transform.InferType()(mod)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5037 = relay.var("var_5037", dtype = "float64", shape = (15, 1, 16))#candidate|5037|(15, 1, 16)|var|float64
func_5036_call = mutated_mod.get_global_var('func_5036')
call_5038 = func_5036_call(var_5037)
output = call_5038
func_5039 = relay.Function([var_5037], output)
mutated_mod['func_5039'] = func_5039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4895_call = mod.get_global_var('func_4895')
func_4896_call = mutated_mod.get_global_var('func_4896')
call_5057 = func_4895_call()
call_5058 = func_4895_call()
func_3105_call = mod.get_global_var('func_3105')
func_3108_call = mutated_mod.get_global_var('func_3108')
var_5084 = relay.var("var_5084", dtype = "float32", shape = (96,))#candidate|5084|(96,)|var|float32
call_5083 = func_3105_call(relay.reshape(var_5084.astype('float32'), [12, 1, 8]))
call_5085 = func_3105_call(relay.reshape(var_5084.astype('float32'), [12, 1, 8]))
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_5092 = relay.TupleGetItem(func_4107_call(), 0)
call_5093 = relay.TupleGetItem(func_4108_call(), 0)
func_3230_call = mod.get_global_var('func_3230')
func_3233_call = mutated_mod.get_global_var('func_3233')
const_5104 = relay.const([-1.056664,0.091615,-1.288246,-8.030960,1.436692,8.452908,-1.153950,9.449060,0.475679,7.386880,-3.844276,-4.338645,1.284992,-4.496111,0.977735,0.382384,-0.870218,-5.601431,1.814371,1.654707,9.140849,-5.244824,8.058743,-7.635128,-0.497499,-8.885512,8.317205,-0.367106,0.428733,0.765290,3.793965,-8.289062,-6.588044,-7.407550,-5.633205,-9.760367,-7.139146,4.481641,3.441632,-3.230627,-4.633099,-6.822541,9.490133,-3.271884,-6.690524,9.053021,-0.838319,8.344428,-1.541604,-0.318432,9.557975,9.509315,-1.251009,1.157470,-6.958302,4.582855,-0.239194,-9.384280,-6.237726,-1.575987,9.166708,-9.457511,4.035025,-2.263150,0.251390,-1.874286,7.150807,-2.446758,2.623446,5.194567,8.454214,-9.612480,3.708405,-6.980903,6.536509,-2.885274,-1.471834,-5.042135,-0.363463,-7.872689,9.760628,-5.841630,-6.786215,-9.370150,-8.170140,1.408153,-0.258776,3.322655,9.176983,-8.118432,-8.823156,7.064626,9.425569,-7.285031,-7.093639,-8.386872,-9.197001,-8.480106,4.473909,-6.142502,9.666010,-8.034012,2.152500,0.316982,8.035079,0.491702,-8.631255,-3.213864,-2.613074,5.096900,7.954827,-7.837435,-2.178684,-2.794606,-4.947057,7.445771,8.233463,0.739343,0.746099,1.061078,-9.072319,-1.521274,0.554326,8.046796,8.290903,-1.742769,-1.712724,-8.320292,1.405590,-0.838802,1.191490,1.653464,2.780185,4.097854,7.142202,5.478479,0.061854,-1.221603,6.398600,-1.711957,-3.731800,1.447069,-4.632774,8.463384,9.418964,6.827587,8.210483,1.065043,7.111604,3.607806,9.579643,6.807947,-4.265759,4.863497,1.912562,5.641757,-6.744069,-1.263900,-4.615438,-7.615723,1.754682,2.421295,0.368111,-6.470994,2.934003,9.730229,-6.441027,-7.911750,2.192281,-4.172932,7.789519,-3.656602,4.076624,-1.940731,7.517269,4.673162,-1.370295,0.178472,3.240037,7.079348,-4.983519,9.837712,6.407609,6.230074,1.492099,2.591640,0.946857,-8.290559,-6.832955,5.962332,4.904978,-0.914526,0.305211,7.496385,6.412213,2.937229,-9.682146,0.972485,-1.697473,-2.081652,-8.589614,8.218736,3.514935,-7.639759,-8.831524,1.624228,-9.195623,-5.997206,-9.898693,-4.256034,-6.438083,8.595130,-4.634333,-9.577401,2.659491,-7.859339,-5.221286,-2.463948,9.137675,9.508691,-6.370179,-9.103840,-3.033245,-2.594693,-6.082148,4.851422,-6.329156,6.484018,5.028695,-2.893125,-5.952562,-6.864540,-1.129466,7.169289,-8.591999,2.853230,8.933102,7.376927,-9.284113,-2.217924,0.306670,5.407697,-0.019481,-8.120573,-1.465408,1.659262,-0.751026,3.624605,-0.434443,-5.520418,5.093175,0.115085,8.411195,2.229234,-5.559320,3.912609,5.973843,1.083509,5.687442,2.800922,-5.902296,6.725911,-9.116055,5.961760,0.231186,2.117384,-6.485180,4.303093,-5.641997,0.730772,2.332351,-3.738772,-3.260636,-5.089659,2.349682,1.996430,-9.576746,-1.956987,-8.353984,0.563610,-5.738903,-1.783271,7.686962,-9.612863,-0.343719,-0.073984,-9.915088,-6.951829,0.128348,1.842178,-8.095547,-7.062211,6.445852,-8.185128,1.024060,9.571283,-3.259711,-2.839137,3.535407,2.844809,-6.220580,6.711093,-8.084800,4.942631,6.888324,1.729707,-1.573638,-8.364586,-6.730199,4.996562,6.247627,9.590390,-9.549527,0.926634,9.454405,-1.124438,7.219996,-1.168601,4.739705,1.582384,-7.568736,4.741070,-7.717676,-4.306637,-2.185822,-3.335100,-6.815599,1.415478,0.238526,6.760503,-1.809882,8.153488,1.435583,4.614372,3.435745,3.786741,3.700001,-6.182225,9.617838,5.524312,-5.649640,4.363500,7.920840,-4.302175,7.042657,5.063867,6.633611,6.359224,9.213341,7.376196,1.203360,-8.338035,6.070776,7.286464,-0.008857,-7.459856,-1.701730,3.047572,6.497695,5.249179,8.572079,-5.624919,0.889328,-0.087279,-8.101526,6.118406,-8.413552,6.629911,4.926090,-8.035159,1.005109,-4.788805,-3.444000,5.309460,1.776924,9.695521,-2.624235,2.531939,9.942079,-7.048838,-9.761502,-1.660994,0.574480,-3.005147,-9.851451,-8.879745,-3.234571,9.676214,9.944883,-3.241543,1.860094,8.323257,7.996242,1.229707,-2.014419,-6.894803,-9.238742,-0.606531,-6.220074,-6.051368,7.705856,-0.866921,7.303264,7.692912,5.486450,-2.286594,6.162873,-4.812577,-6.033359,1.960972,7.842136,8.418726,-9.648496,0.342319,6.584823,3.694290,8.606210,-0.349982,-6.906089,1.324227,2.494012,-4.005575,9.138658,4.810641,3.438222,0.367807,-1.897036,-7.924817,-7.042029,-3.654836,2.959704,-0.197591,3.218763,2.406694,-3.996345,8.289020,-5.044032,-9.811388,-2.478601,-0.979793,4.364736,-7.246470,-0.602479,-8.393720,9.842070,-2.170963,6.853930,6.092728,1.443525,-3.696354,2.895899,1.782545,0.952477,5.382942,9.172558,0.753032,0.896017,6.855299,-2.624330,-2.156947,-0.484486,-7.353568,-5.341494,-1.935151,1.911403,3.850679,1.915807,-2.790666,2.183637,-0.196349,8.564286,1.165748,-6.761022,0.231403,-7.803026,-0.977483,-2.873832,-4.527517,-3.595402,1.327605,1.400697,-8.859463,4.257894,-9.212824,-6.621060,-7.032423,-6.735765,4.341488,-5.294054,-5.970061,-7.558569,9.950124,0.421451,7.657529,-6.118400,1.770271,-8.444633,-9.172610,7.013013,-9.096805,-3.343004,5.116839,-5.683484,3.770062,0.336527,0.469525,-6.328838,5.875162,3.757185,1.746538,1.956336,2.462633,-4.480336,7.136388,-1.277499,7.790912,-2.368516,-2.696557,7.019859,4.430991,5.064161,3.684205,0.128987,3.090560,8.714719,0.723849,-5.691214,-8.540703,-8.273483,-6.004351,8.296344,8.994650,-7.624658,-8.072397,7.801515,2.001013,6.514601,-5.424604,2.611415,0.553506,-1.496140,2.726015,4.615310,3.840471,1.952178,3.087508,-0.853506,1.006939,-5.002819,-0.863691,0.903362,-4.508540,-5.475325,-5.207429,-0.589502,1.813199,-4.473930,3.793504,-5.914080,7.712028,-0.907640,0.709641,-0.403513,-7.192089,-9.178346,-9.928152,-9.577703,-0.304272,-6.628615,-6.538601,-0.602275,7.606711,-1.786077,2.066093,-2.358396,-0.006101,1.258823,1.221655,-4.451925,-2.407904,-0.739045,9.223162,1.282409,-9.966862,-5.394367,-5.789243,-2.364625,8.505773,7.417298,2.970178,0.670695,-3.556896,9.183109,-7.386017,9.712259,2.447569,-8.763546,-0.688796,-1.334811,9.665071,8.787084,-0.303150,0.004357,-5.031233,-4.626512,-4.388834,-8.192281,-8.064247,-0.757330,6.141542,7.434137,-9.426956,7.518448,0.535552,7.655583,-4.237572,-7.522861,-1.578126,-4.979786,-2.558489,-5.746025,8.885833,-7.060994,7.689365,-2.541729,-8.282522,7.788260,7.383091,-8.113041,-9.211554,3.857111,-4.579951,4.149378,-4.920331,-6.625798,-7.643937,9.495441,2.204157,6.600287,9.784973,3.498318,2.052047,-3.391092,-1.361197,1.263081,-8.859525,9.259643,0.499831,5.477423,1.519376,-5.317490,-3.042572,5.990945,6.880345,-1.493192,-7.709555,9.549224,-2.441026,0.446739,-8.980416,-9.478442,6.076901,0.575667,-8.559938,-0.715620,-9.518480,-1.628205,7.424723,-7.825752,-4.580621,7.366082,9.168094,4.295936,-1.131549,-5.473384,8.667680,0.086286,-0.024388,7.207638,4.093764,-8.804206,6.273633,-6.811457,-1.523419,1.403988,-5.037369,-0.279147,4.018639,8.048118,-5.099524,-4.164836,-5.788051,-6.016285,1.759949,-1.714016,-6.815809,-0.933298,1.073897,-5.209104,-7.239409,-2.736063,-9.445262,-7.548568,-2.325303,4.216287,4.107231,6.524135,8.018256,-6.670082,4.590084,5.292484,-3.573640,8.143938,-0.186539,9.840975,-8.489043,1.710949,-4.612354,-1.842516,-1.559282,3.237989,-6.262798,8.417131,9.990930,-9.142003,-1.265778,-2.908234,1.592171,-1.758217,5.284620,-8.303920,-6.394969,-6.406696,0.646096,4.833853,-5.756528,8.329106,8.485636,-9.408605,0.762953,-3.400822,-6.231984,-9.216416,-1.331913,8.595083,-1.714491,3.014667,-8.872711,-9.080751,8.570790,8.452619,-3.867906,-3.714334,4.869081,-9.996721,0.912333,7.902814,2.411060,9.607405,-1.552443,7.574998,1.135833,2.593509,-5.380007,4.396767,-5.789623,8.213914,-0.801531,-5.778230,-6.912435,-7.840022,8.790278,3.051232,3.411602,7.367213,-7.330492,-0.460553,9.373881,2.441357,2.992367,8.623096,5.646289,3.868804,-3.651208,2.403870,-4.536542,-2.101729,3.469858,2.488695,8.854754,2.879515,9.056926,7.061803,8.013684,8.389360,6.867263,-4.284430,2.560561,-0.356741,-6.320583,9.641979,2.680141,-0.554865,0.703796,9.990865,-4.392368,-0.816280,6.685213,1.132331,-7.188237,5.351254,2.020339,-2.549392,8.674455,0.783793,3.117929,3.104001,-2.323159,5.313828,4.737430,-2.986310,2.784684,3.251473,-8.901693,-1.034623,2.081356,5.318566,0.916676,-3.106906,-4.139311,-8.590817,-7.289252,4.272285,-0.198554,-5.488952,4.795506,0.953253,-9.392419,0.542328,3.967368,5.751295,-5.628937,-1.928946,1.778233,-4.038440,-1.155396,9.699919,-2.211837,0.312637,3.286205,-6.052646,0.211707,-1.904981,6.627598,-1.564114,9.614064,5.760876,-3.357891,9.612237,-7.462294,-8.267863,4.444725,7.117473,-5.015083,-4.047715,5.621592,-8.386422,-2.402853,-5.325582,6.306590,2.924648,-9.030994,-6.210986,-9.988764,-8.794321,0.665395,8.430937,-4.766207,1.150096,7.411111,2.363434,-2.898231,3.047534,-1.245788,-5.714331,0.281724,-7.045892,5.035124,-0.445981,-9.429442,-3.269538,9.446631,-1.392684,6.029930,-8.272590,7.495985,4.221358,-9.103061,6.539696,-5.414826,-5.773022,6.982963,1.075239,1.814405,-3.347828,8.824612,9.563834,-8.017677,-0.756077,7.621706,-5.503190,-2.089056,9.057197,0.324484,2.058944,-8.528418,4.523895,-4.520726,-6.951158,-2.921212,-8.622433,-8.874075,9.147308,8.061107,-6.162080,-9.136160,-1.490050,-8.199494,3.207030,-1.929311,1.893305,-1.552912,-8.109637,9.179985,-5.623649,2.369394,9.522994,6.191777,-6.089863,2.423468,6.747081,6.253075,-8.797003,6.409905,5.518914,9.599402,3.166667,1.122463,-9.211971,-5.829560,3.570586,2.087781,3.180279,2.940617,-9.765261,-9.713475,-9.794840,5.445046,1.472101,5.606443,-3.538823,9.508598,-0.904689,4.890571,-4.940622,-0.117658,5.711295,-8.014507,-8.567880,-3.385361,-9.635305,-2.854306,-9.957690,-2.433170,2.194656,0.914440,-2.494471,4.321721,8.749393,5.136005,-9.096151,1.045463,-1.679442,0.156154,7.776333,7.954573,-8.634776,1.190124,1.816838,1.987789,1.867275,-2.842198,5.772595,-8.405265,-2.412456,-5.543111,7.426702,-1.596781,-1.132214,-5.256752,3.374761,9.804134,-4.546039,-7.022851,-3.108611,-8.289764,-4.036018,5.149289,-3.074765,7.784274,-8.682190,5.337139,9.016807,2.023968,6.271993,-1.766755,0.124137,3.641061,-2.735395,5.501183,3.040629,-3.122995,-0.234976,6.439497,0.525876,4.527325,4.203546,-7.779886,-5.590826,-2.576507,1.548450,-8.141258,-5.927424,-3.039710,2.247186,-8.537433,5.763534,9.611365,-3.295544,-9.334457,5.347614,2.750349,8.671581,9.635128,0.591984,1.840718,-3.565902,7.116715,8.288029,0.327870,1.900455,3.915436,-8.140545,-3.055164,-4.577378,6.646760,-9.079838,-6.229605,-0.422227,6.209810,4.273622,-7.443023,-7.758778,-8.257744,-7.716377,1.615308,3.852625,-6.645195,7.728229,3.763548,-5.906482,0.802516,3.047377,-4.119202,4.071992,-4.128711,-7.927017,6.096068,-6.778173,1.567112,9.417945,3.290982,9.855703,4.726550,-0.221265,-4.046711,6.467569,-5.597278,1.653611,-8.404134,-3.225679,0.050087,6.255032,-4.060706,6.867744,-3.399887,-7.089219,9.109329,-9.053857,-0.192222,7.182403,2.937733,-3.116466,-5.068488,-0.008951,-3.245329,0.118819,1.930779,-3.270890,-9.242930,6.307065,2.179771,-3.163062,-4.586605,8.702308,-7.026333,7.088807,4.650755,9.588991,-3.239504,-9.356703,-0.884934,-4.190103,-9.815434,2.410451,-9.948835,-6.370720,-8.093554,8.360050,6.551794,9.161786,1.733792,8.339523,-4.624714,-0.449736,-7.460796,-7.649108,-6.456789,-0.214790,1.690326,-8.416426,0.119895,0.952455,9.906068,-2.484039,1.709612,-3.260601,-2.574693,0.338956,-8.202781,1.700071,-9.914266,-5.856591,0.431412,-7.464054,-3.786309,-5.580273,0.133155,-9.404593,-0.812479,7.502207,-3.765274,7.496044,9.236058,-9.964639,-2.363457,-7.446379,8.989944,-5.133167,6.531641,4.720983,5.006140,7.515661,-8.709337,9.225858,-8.495712,-1.009759,1.662389,-0.931910,1.212003,-3.461318,-9.336760,-8.849531,4.689877,-3.065571,6.954681,5.831179,-0.806772,7.857413,-3.118857,7.014505,9.822639,0.976086,4.119375,2.988102,-7.222517,0.575537,-8.678821,-5.312595,-8.382750,4.576018,0.671130,-6.152348,3.489887,-8.400327,-5.929901,9.647660,0.232412,-1.572019,-4.940107,1.536582,-3.869834,9.008000,2.918722,-9.603401,8.908722,9.864791,-5.998412,-6.577027,-2.547300,4.741567,-3.317967,-4.748011,-8.368894,1.662351,6.232971,6.199512,6.451821,-2.510952,0.786890,-5.508381,-8.753988,5.370510,7.057441,9.418331,-6.548987,-4.106664,5.366097,-1.303246,-9.154972,-0.932966,6.144624,7.532109,-6.802009,4.686734,-4.590564,-6.487635,6.160175,-7.098810,7.364682,-1.805032,-0.065299,7.396042,-2.556660,2.151273,4.443408,-0.030194,-7.311308,9.344608,3.323942,-8.597595,-9.356870,1.890054,-8.512800,-7.417970,4.068590,5.243279,8.266223,1.440656,-1.239063,-1.613761,-1.248310,-2.015585,-1.515178,0.202436,-3.264614,-9.400144,4.570757,8.664298,9.071746,3.103159,-6.617156,-5.464566,2.567656,0.258326,5.457387,9.466843,-0.595114,-5.993786,9.021749,3.851400,7.842184,-6.642164,1.055704,-6.801307,1.543495,6.825394,-7.096088,-8.396441,8.494502,6.304515,7.455578,-3.240333,5.314990,4.696976,-1.224844,-5.183959,-3.789414,-7.241228,-4.884790,-5.840288,9.774078,-8.758942,4.597831,1.117276,-3.194673,3.532684,-4.978927,-9.231336,-1.356025,-9.523543,-2.955800,-7.147251,-9.623709,-0.974449,9.668369,-2.153317,-7.496550,-4.354479,4.217323,-9.112311,6.252371,-8.379956,6.765385,0.972985,-5.702975,-5.630492,-7.870811,0.823819,-8.947655,-5.085590,-0.695645,-4.533642,7.549164,-0.200323,-0.640493,-8.976907,0.198082,9.567862,0.733606,-8.905632,0.463401,-5.596192,-0.821568,-5.942697,6.664336,-3.516744,0.049609,-5.792535,-0.984519,-9.609448,3.627504,-1.179020,2.841464,7.167858,-6.449456,-9.731766,7.605883,6.438387,-6.568455,-0.553385,-5.742096,6.436927,2.942132,-7.914765,-2.533498,-4.297604,-8.860016,-2.585172,1.589075,-7.078349,-0.945295,6.178364,-9.205425,7.169791,-9.863477,-5.501990,-3.448933,-3.238083,-0.027490,0.452784,4.973537,-1.172669,-0.133798,2.074114,8.466459,1.491338,-9.045234,6.050570,-2.379699,5.689924,-9.414495,2.392468,2.773171,-5.829451,3.480882,3.296051,8.198674,-7.353540,-5.621872,8.371431,8.325405,8.852427,2.854426,-2.521651,4.882784,-0.934012,-8.088823,4.999023,-5.285948,8.540131,9.121617,-8.816218,-3.886410,7.186593,1.771993,-6.316902,5.292127,-0.812456,-8.983545,-5.861594,9.464751,7.937176,4.973503,3.776136,-1.819842,1.976806,7.111296,5.146000,-5.268157,7.768060,4.638359,-1.762761,0.388273,-0.260485,-5.137692,-6.376253,8.479365,7.913531,-3.371535,-1.739463,7.784814,-9.242716,-0.492612,-5.801575,-3.283169,-0.390370,-3.918835,5.006351,6.619092,9.504676,-6.702607,1.913835,-2.632585,-6.410587,-2.355548,8.451559,-5.012866,-2.469378,1.126816,2.366157,-0.009048,-8.368615,2.378453,9.548568,3.195067,-4.375294,-0.535715,0.795596,-0.279369,1.976436,7.426720,-0.789941,-8.763994,-8.590450,5.213542,-0.685266,6.618984,-4.064720,-3.426752,8.162079,7.364960,0.802646,-3.201978,-4.443756,8.838804,4.846772,-9.441024,-0.323240,-3.766429,7.118259,3.176182,-1.035627,-6.949730,9.136784,-9.425822,-6.179224,-7.409825,0.448007,-8.931262,6.932964,3.751603,-1.970166,-2.847828,-4.655767,4.473738,-9.775879,7.342942,5.739084,-3.434350,-7.896974,-9.031991,-2.910141,0.738028,9.497864,9.121198,7.004518,8.699058,-1.674253,-4.593318,-2.558039,-3.104424,-1.226274,5.826139,2.165598,-4.222876,-1.826920,-0.391487,0.188630,-5.740001,-3.412858,0.295294,-1.428552,8.067178,-0.756024,-4.065219,-1.797218,-8.093110,-3.792079,-1.907099,9.067509,-5.684364,6.779222,-7.271317,-0.961550,0.686735,-3.346652,-6.706406,5.248883,1.317430,9.429560,1.785224,1.617284,1.935399,3.721949,7.519567,-4.225425,5.900741,8.597758,3.248179,-8.482448,-6.756596,5.561300,-6.310897,-0.903457,5.380507,2.695744,0.469172,-8.859735,-7.527101,8.712657,-1.653511,7.048933,2.324697,3.807116,-3.508128,-2.562153,-3.047031,5.353514,-6.418146,-6.740849,-5.292126,-6.070455,-9.563348,-7.753802,0.857647,6.033593,5.569421,7.934540,9.199692,5.253407,-9.178209,-3.316509,-9.572092,7.357176,6.533949,-3.129912,2.491516,-7.758758,7.382719,5.160193,-6.631665,-2.146546,2.493510,-1.544790,-6.058374,6.042068,7.176615,9.602087,0.656256,3.814722,-9.485573,-4.415757,-0.635773,-1.660070,2.976362,-6.059100,-9.760465,-8.386207,-0.343057,-2.547209,-4.385996,-0.020520,2.744332,7.497289,-6.204958,6.594185,-6.661328,1.563843,-7.102441,-9.093635,8.148981,9.911370,4.182066,3.044629,7.756410,-6.324136,7.233545,3.082773,-3.342106,-7.321135,0.504188,-0.146241,9.356419,4.419413,3.661982,-6.260342,-1.334271,-6.192237,9.430341,-8.518903,2.635124,-0.710472,2.909392,7.872753,2.336954,-1.224649,5.007068,-3.522459,-2.903099,0.084947,-0.992213,-7.262095,2.755956,-7.039730,7.396758,2.819548,-6.772893,6.281583,-9.874054,3.574338,-6.530177,-0.631926,-2.002747,9.828276,-2.385727,-2.212261,-3.625737,-4.983374,6.515343,-8.986888,9.098796,0.020512,4.278977,4.467720,0.092153,4.437802,-0.818400,-1.443544,6.242147,-5.332713,-3.784795,-1.416126,3.350882,-8.900762,3.399646,4.144637,4.311204,-5.239090,-1.152675,-5.988912,8.989106,6.479039,6.454806,-2.162840,6.393180,0.761086,-6.708498,-3.383234,-5.486575,-4.264381,0.363821,-2.530541,5.127967,-9.000844,-6.355192,1.854041,-7.016463,0.160108,-7.712377,-9.765885,-9.529200,8.416120,6.769941,0.116951,3.079518,-9.465973,6.021995,3.521640,5.441055,-4.006318,-0.709344,2.556467,2.609979,-4.389245,3.409327,8.499459,-7.428369,-6.007064,5.431608,0.868004,6.839678,4.192879,-2.724432,4.887616,-2.593259,3.755170,-6.121699,-8.123231,-5.765059,0.466060,3.095167,4.986514,-0.495636,-8.366761,1.253452,-3.339851,7.177292,-1.784693,-4.292079,1.361721,5.474967,5.149636,-6.049049,7.721548,-4.566169,-2.811734,-5.471259,-0.007483,8.509576,-9.112416,-0.252397,1.472927,-2.547664,-4.017413,-8.183995,-9.474235,-8.207572,9.108205,7.044598,1.107803,5.383452,6.076762,-7.323547,-9.885842,-5.012294,-7.921332,0.532224,-9.883465,6.731023,-8.543406,8.275685,-8.174786,-2.152908,-3.757921,-4.954187,-0.633988,8.374745,0.630689,7.515721,9.032694,-9.122287,-3.257922,0.482576,-3.216064,0.934915,-5.496206,7.322333,0.886267,-9.000177,0.920292,6.027153,7.632556,1.737871,-4.027610,-0.775887,5.946374,-8.841786,9.202755,-0.445129,-3.068110,-8.953874,-4.927553,3.259697,-5.906536,3.960134,1.447216,3.267820,9.481718,1.533694,8.616612,8.088336,4.343468,-6.089775,-1.520957,-2.641426,4.947275,0.699372,-3.735740,0.159377,1.370012,-7.232099,6.575995,8.383600,-7.670704,2.237575,-7.248581,-4.539988,-9.555144,-4.780844,-0.313965,5.256027,-4.134341,8.640335,-9.594191,9.973433,-4.344600,-0.242451,8.595972,-0.162421,-6.305049,6.486041,2.334485,-4.277242,-8.569278,-2.015538,1.673213,-2.710285,-6.279912,-7.854503,-4.015261,-3.878661,5.498379,4.685749,-9.716605,6.568681,2.748017,-5.819116,-7.819082,-5.747137,6.660012,0.658670,-2.136784,-1.612982,-1.453923,3.032077,-9.101794,0.649522,-5.873033,-2.793671,-5.310749,-0.270462,-4.705614,-1.433241,6.422686,-0.951689,5.066058,-4.613988,2.587622,6.573515,9.265381,0.951250,-4.064340,-5.702083,8.815196,-4.686437,-5.370806,5.179128,9.141755,9.879486], dtype = "float64")#candidate|5104|(1920,)|const|float64
var_5105 = relay.var("var_5105", dtype = "float32", shape = (360,))#candidate|5105|(360,)|var|float32
call_5103 = relay.TupleGetItem(func_3230_call(relay.reshape(const_5104.astype('float64'), [15, 8, 16]), relay.reshape(var_5105.astype('float32'), [360,]), ), 3)
call_5106 = relay.TupleGetItem(func_3233_call(relay.reshape(const_5104.astype('float64'), [15, 8, 16]), relay.reshape(var_5105.astype('float32'), [360,]), ), 3)
output = relay.Tuple([call_5057,call_5083,var_5084,call_5092,call_5103,const_5104,var_5105,])
output2 = relay.Tuple([call_5058,call_5085,var_5084,call_5093,call_5106,const_5104,var_5105,])
func_5119 = relay.Function([var_5084,var_5105,], output)
mod['func_5119'] = func_5119
mod = relay.transform.InferType()(mod)
var_5120 = relay.var("var_5120", dtype = "float32", shape = (96,))#candidate|5120|(96,)|var|float32
var_5121 = relay.var("var_5121", dtype = "float32", shape = (360,))#candidate|5121|(360,)|var|float32
output = func_5119(var_5120,var_5121,)
func_5122 = relay.Function([var_5120,var_5121,], output)
mutated_mod['func_5122'] = func_5122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_5191 = relay.TupleGetItem(func_1608_call(), 2)
call_5192 = relay.TupleGetItem(func_1609_call(), 2)
output = call_5191
output2 = call_5192
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
func_1872_call = mod.get_global_var('func_1872')
func_1873_call = mutated_mod.get_global_var('func_1873')
call_5241 = relay.TupleGetItem(func_1872_call(), 3)
call_5242 = relay.TupleGetItem(func_1873_call(), 3)
output = call_5241
output2 = call_5242
func_5250 = relay.Function([], output)
mod['func_5250'] = func_5250
mod = relay.transform.InferType()(mod)
output = func_5250()
func_5251 = relay.Function([], output)
mutated_mod['func_5251'] = func_5251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5197_call = mod.get_global_var('func_5197')
func_5199_call = mutated_mod.get_global_var('func_5199')
call_5286 = func_5197_call()
call_5287 = func_5197_call()
func_4083_call = mod.get_global_var('func_4083')
func_4086_call = mutated_mod.get_global_var('func_4086')
var_5303 = relay.var("var_5303", dtype = "float32", shape = (16, 6))#candidate|5303|(16, 6)|var|float32
call_5302 = relay.TupleGetItem(func_4083_call(relay.reshape(var_5303.astype('float32'), [96,])), 2)
call_5304 = relay.TupleGetItem(func_4086_call(relay.reshape(var_5303.astype('float32'), [96,])), 2)
func_4839_call = mod.get_global_var('func_4839')
func_4842_call = mutated_mod.get_global_var('func_4842')
var_5313 = relay.var("var_5313", dtype = "float32", shape = (180, 2))#candidate|5313|(180, 2)|var|float32
const_5314 = relay.const([-0.252063,8.412713,5.549257,9.326681,-5.055182,4.244360,-2.443995,-9.864593,8.314916,-1.939421,0.106844,-0.538316,9.835960,9.844249,-0.424493,-9.751758,-6.762172,1.753038,7.952767,-7.757011,-4.504170,-3.483574,-1.210480,-7.384691,-3.708497,-4.983207,2.677489,4.571255,-5.531955,-7.776621,-4.744861,8.997635,-9.491674,-9.750359,5.746663,-7.497924,-8.672036,3.027912,5.207457,-9.417495,-7.508075,9.563370,1.170452,-1.214491,-5.896059,7.052537,5.242090,6.333834,5.948350,-2.958720,-6.753495,-3.554807,6.555738,3.315076,-7.554476,-5.125415,-4.232679,-7.793464,1.177214,3.165701,9.561619,-1.936125,-8.237302,1.881358,7.005081,-5.105492,-1.354432,-9.301104,-8.118267,-1.275341,-7.776621,9.742664,-4.523565,-8.050857,-2.539376,6.174779,-8.352518,1.857889,1.638590,8.735816,-1.591472,9.187230,-8.607624,-1.157798,1.560853,3.660159,3.109624,7.272523,4.693252,8.291859,6.237008,3.098676,-1.927832,-3.791070,6.260565,-4.070376,-4.942142,-3.148163,-2.404948,2.730283,8.641384,3.211309,-8.657437,7.940860,-3.004997,8.883244,9.404831,-5.759891,0.345305,-7.111216,-1.792621,-4.145757,-2.401861,6.441427,3.470011,-7.958207,-4.319415,-9.137111,-0.465692,-1.831467,-7.693881,5.104290,-9.422690,-5.765732,-7.630193,1.082077,5.553487,0.174118,-5.946893,-3.695863,-4.585685,0.442671,-9.407846,3.273263,2.541988,-3.269315,0.617899,4.258479,7.504222,-5.798539,-7.477815,-0.831484,5.277324,6.484045,-7.257185,-8.741195,9.840083,0.516110,1.912391,-8.126572,-4.222077,-3.870347,-7.391256,-8.864752,9.662885,-1.201353,-9.275525,-2.715383,-1.260929,6.556582,3.936017,3.310817,5.531601,3.280491,1.496310,4.429696,-9.669338,-5.506595,-3.004189,-3.298968,7.556870,6.406408,3.986135,7.423590,-4.751218,-7.216259,-5.516554,-6.689019,6.743912,-2.301256,9.716686,-9.363471,-6.598637,8.394178,2.609347,-5.248765,-5.125722,-8.471779,2.252214,5.233244,0.480498,-1.253106,-1.407613,9.564383,-0.471040,-4.071072,-0.646189,0.010089,2.247770,1.968014,-5.601417,1.554972,3.402107,-7.757773,-0.239613,-7.751006,0.434422,5.328857,0.224440,1.213274,0.149420,-7.537976,1.493949,-2.892622,-7.279413,6.575799,8.525973,4.568165,0.574236,-6.000610,7.238547,3.997447,3.380569,-8.675043,1.334156,-9.961851,-5.895271,-1.427594,-7.296034,-9.049402,-5.571402,0.276363,3.532382,0.818896,-8.024866,-9.139770,-0.401574,-6.934515,-1.826798,6.945462,3.692025,-1.618454,-0.241648,0.680528,0.271310,9.631402,5.342581,-7.687375,5.077898,7.334896,9.944292,9.116048,6.601148,0.437838,6.318990,-0.593047,-6.685354,-6.081181,9.992291,7.103463,4.618472,5.356100,7.660248,0.738841,7.760580,-0.479722,-6.611536,-1.605095,2.323917,-7.614890,-4.846761,8.369791,6.450641,9.606064,3.009404,-8.225736,3.173307,-4.119446,2.936543,8.070591,-9.594656,8.781299,-8.773759,1.752332,5.922632,-3.452418,-9.297658,-7.304401,8.270386,-0.126284,-8.287909,0.163697,-4.126108,-9.667571,-1.199719,-1.134106,7.802755,2.753451,-3.114939,3.696891,-4.630881,9.094629,-7.416301,8.865126,-8.652538,-6.032394,-7.431854,-7.474507,4.163811,-7.948036,4.133894,7.164765,-3.810052,-6.950768,3.716214,-3.791245,5.776868,-7.141907,5.787739,1.038749,7.907151,-6.420630,1.599467,9.338710,0.413610,-8.217845,-4.131747,7.857740,4.380169,4.779785,7.883215,-0.365924,-4.187716,-8.018292,-8.154993,7.871705,-2.096540,3.490637,-2.867989,-4.554250,-8.106949,-1.695554,-7.754808,1.426089,3.012262,-9.653506,-1.489321,6.978818,4.530758,-7.077662,7.161785,-2.217427,4.358745,-4.117063,-7.390082,9.335397,5.142988,9.504286,2.449930,0.757384,-1.739973,-9.998972,1.862555,8.872849,8.213942,-9.800000,8.113598,-3.655380,0.588387,-7.893455,-7.042891,-1.069683,-6.471183,9.703260,7.869858,-9.673494,4.542341,-0.108040,6.315854,2.099390,-4.958298,0.599796,-7.552433,-1.867650,-8.573755,0.273627,7.504092,2.160418,-5.925701,3.356468,5.522653,4.433646,-2.614709,5.589112,4.488029,7.044099,7.906548,8.087352,-6.785343,0.273336,-3.339109,2.856977,-3.632913,1.058490,-6.878232,-1.711859,7.556936,-6.300547,-8.992317,8.241171,-8.793742,9.275945,0.983456,-1.676925,-9.343552,4.788564,-5.108040,-2.531273,8.779543,0.807932,1.473008,7.053878,2.325747,-2.445306,-5.310040,6.875330,-4.300536,-6.903349,6.810640,-1.599397,-0.472466,1.604410,-3.975108,2.245310,9.907961,6.774327,6.800248,8.112696,-0.149168,-2.628691,0.337229,-8.766110,-2.462513,-5.283913,3.772121,8.759680,-9.702565,-5.374905,5.843222,-4.493699,8.120439,6.689396,-0.174218,6.850575,-3.524142,7.364890,-4.600806,-6.847274,-6.251991,-9.980215,8.660088,9.570955,-4.653899,-2.648967,-2.643173,0.326042,3.854879,-6.407115,9.495212,-0.697098,3.854041,-2.621316,7.083976,-1.391931,0.203704,4.678629,-5.094891,-9.139180,3.920039,-9.461671,2.408757,8.605660,-7.407571,-2.468543,3.228973,-7.810648,4.855345,-3.681275,8.170525,-6.908625,-6.752894,4.326187,3.333079,4.347359,-4.485893,-0.498460,5.221966,-2.318617,8.267063,-2.297822,-1.107173,6.141167,8.502267,-4.814429,-7.792626,6.528523,4.903527,1.309092,-6.887097,8.588078,3.356700,-6.983101,0.338868,-9.529341,7.120373,1.032698,0.505691,3.747939,0.532350,1.898768,4.672109,-9.582567,2.292650,4.167923,-0.903935,4.005310,-8.699441,4.210704,-4.390698,-9.976250,-7.313415,9.921549,-4.049212,-8.987980,0.176370,5.131005,-0.661753,4.382919,7.162858,0.012010,9.730875,9.913359,-7.279954,9.840082,9.752620,-5.654727,1.159908,2.966321,7.684847,9.087923,-6.620968,8.163501,-7.568601,-2.035750,1.260192,-1.386769,-2.120805,-8.160411,-0.529132,-5.195848,4.033185,5.342000,-4.475334,-2.025854,-8.329129,-7.465677,-9.592263,1.482937,-8.462720,-4.538978,8.164119,-5.823140,3.458413,-8.987627,-7.891162,1.520924,7.578426,2.012683,1.937276,1.981784,4.484715,-7.120792,0.488841,6.575989,-2.603626,8.801617,-1.527584,8.761652,-8.724386,5.670556,-4.908298,-0.051707,0.133671,-6.131869,1.426665,-8.702968,0.048425,-8.853171,-1.479928,0.001006,-0.326219,-2.492212,-9.128826,-6.945035,5.181713,-0.322957,-7.229359,0.238433,-8.338561,-0.915816,-6.759691,-0.226150,-5.725658,-6.336996,-1.783511,0.285624,4.696316,4.066998,1.605644,-0.075703,5.530331,4.854913,-7.063425,9.866853,-8.112159,-2.617060,-1.860495,-6.667983,-0.063917,8.116103,-4.120228,4.792068,-7.586535,-5.895223,-8.090614,-6.406477,2.346903,1.289748,1.757013,-1.679178,-0.945318,-2.811943,9.172034,2.501695,0.182307,7.626440,5.294012,0.643644,0.637334,-2.350121,4.248745,-2.782315,-5.893381,-0.709638,-1.809382,2.450970,9.072932,-0.881986,-4.174669,-8.186044,-7.915935,-5.571550,-9.916106,-7.713294,0.227903,2.467497,7.461625,9.283111,4.709252,1.386903,-0.535241,5.280794,-9.037495,-7.107986,8.730365,7.735533,-8.102433,-4.474668,0.469956,2.034354,2.053005,1.856945,-1.175882,-4.695448,-6.584648,4.760340,-3.391271,5.987283,-9.464760,2.890899,-1.657803,-4.451528,-3.403215,-7.261774,8.520051,-7.303821,-7.160974,6.078232,-6.790210,2.313039,-0.354438,7.418543,0.552510,8.544670,0.149929,3.899741,7.681458,-7.025498,-7.362320,-6.741442,-9.113693,-6.902372,-4.209351,1.944800,6.612378,-5.573829,-1.916635,-7.219719,-5.378842,1.254781,0.393174,4.522211,-7.652269,-7.742279,-0.961890,-6.885711,-5.172402,-9.896271,9.280206,9.254657,-4.191962,-0.152726,-9.935558,-5.661943,-5.560722,-6.314428,-4.763220,4.177037,3.890605,-4.038462,-8.833755,3.502683,7.638725,2.696548,9.427607,-9.105894,-3.293705,-0.333810,3.924332,6.158141,4.678272,1.564087,-5.991501,-2.914858,5.619132,1.728334,-8.190625,-0.193465,-8.970268,-6.207979,-9.668591,3.746750,2.507852,6.118626,-9.264540,-7.152398,-1.656174,-8.568936,-8.648330,2.758833,5.500692,2.613618,7.594941,7.599434,-1.173265,1.679768,-3.137863,5.769899,2.177573,9.884073,-4.241885,2.166609,4.393108,6.205043,-4.356303,8.521922,0.072314,7.723939,-5.065446,3.689324,-2.833919,-5.992139,6.217397,-3.560314,-7.910856,8.874688,-5.195307,-5.752604,-9.840349,6.101072,-4.998927,-5.488082,-3.053797,-1.553487,-3.962231,6.833702,-9.470846,-9.374246,9.535196,-2.220196,-6.270049,-5.585585,-9.867957,-9.727327,-9.486895,-4.244809,4.713635,6.269048,-5.607436,-2.384311,9.302193,-1.743851,0.614255,8.720566,2.678064,1.855886,5.986889,-9.344914,-2.558742,-5.429701,8.489441,4.438215,1.049918,-0.435813,-3.803121,7.660860,-1.326762,2.305041,-8.822184,-8.083400,7.804276,0.277120,-8.347012,-2.853977,-4.595803,8.926538,9.304075,-4.603316,5.646907,7.372967,-7.358213,6.755690,-7.156611,-6.705474,-7.300218,-1.326092,-8.662059,-8.666710,-1.513628,7.221720,-7.030473,-9.350290,5.188212,-0.677485,4.759790,-0.206215,-3.390698,-0.958609,0.988927,1.816642,0.774508,3.866057,8.233725,-6.284641,-9.877964,9.383612,4.219561,2.815977,-0.903378,7.541901,4.517393,7.434879,-3.507522,-7.573296,1.020924,8.785892,9.519285,-1.188398,-2.849835,-2.518774,4.494073,7.389384,6.694605,2.871182,3.774854,3.019363,5.424958,-5.043854,-1.515702,7.793149,8.954838,3.535127,2.442449,9.275331,-5.159190,-5.283277,2.514617,-6.510383,-3.865286,7.768231,9.967765,-6.252318,8.519786,-6.678310,5.458400,4.642207,-6.460957,-9.115542,0.042371,5.698986,9.741873,9.344259,-6.695034,-7.616396,2.966468,-4.266421,-8.625084,2.461371,9.250130,-4.390195,0.395062,3.329969,-1.613215,3.574581,-6.544866,1.995216,9.017023,-8.699081,0.739159,-0.502858,-9.191204,3.215574,-0.265381,3.006646,-7.866946,-0.869472,1.464333,4.048221,2.866279,6.537860,3.332264,-1.075831,6.593440,-6.031682,6.695159,-7.193972,4.506514,-0.912771,-7.924278,-9.064566,0.050000,3.918591,-3.013677,-2.710568,8.056350,2.663791,8.340372,6.505922,6.476475,9.763259,5.652431,-6.784844,2.258872,-6.480021,-5.946536,-8.919078,1.986904,8.256807,-8.052150,-5.700512,6.418890,-7.688279,4.003270,-4.739346,-5.190941,6.053766,8.126345,-8.955304,-7.872909,-0.948238,1.594381,1.149846,-3.694262,6.879121,-0.702869,8.060055,8.343558,-8.428305,7.821750,5.048485,-7.465504,3.457498,8.082036,-8.876870,-3.047490,-6.044115,3.696720,7.600845,-9.912467,-4.266881,-1.983236,1.101120,-2.193093,-1.696040,-5.548655,4.732429,-6.742678,-7.683455,-6.028825,6.720985,9.529093,0.979979,9.997953,7.462741,6.203665,0.152946,5.021805,6.670110,-5.016344,1.925119,-7.682484,-0.327021,-6.187998,-9.899335,7.335187,4.614447,7.150411,-9.222909,6.649590,4.196713,0.739793,-1.353139,0.434262,-5.074633,4.858331,-0.001707,-8.494322,-0.117857,9.891556,-4.680076,2.140149,1.061850,-8.564437,6.199405,4.463340,-9.395948,1.219974,5.149113,-8.031118,2.196378,-8.272217,8.230818,-3.868053,1.104766,-7.736618,-8.217037,7.032656,0.851495,2.174119,-9.046388,1.593874,-3.949013,0.089820,9.165060,3.499189,-8.642459,-2.481014,7.205571,2.241773,-8.632656,-8.975860,0.854652,-1.269711,6.061259,-6.581595,1.026622,-6.513044,-7.089566,0.859995,3.897113,-9.035198,-0.204709,-9.060358,9.400087,-3.460111,7.274345,9.059799,6.541598,4.576643,6.008189,-8.720859,8.702900,-2.467867,-6.612717,6.973908,9.614169,2.893546,-3.695347,6.180204,-3.244218,3.687523,-9.732132,-1.261777,5.591074,-7.234736,3.042550,4.131348,0.961235,8.442786,5.639290,2.195499,-1.939276,0.607231,-1.450781,5.611459,-4.066143,9.338258,0.535045,-8.001814,4.511568,2.353165,1.845320,-5.476143,9.729703,7.875871,-1.681661,6.350921,3.756931,-2.817656,1.833720,-5.686350,-8.444798,-2.237914,-9.820592,-4.213783,2.134621,-8.339250,-8.008779,3.172521,-6.113037,1.448395,7.110193,-0.220485,6.322173,9.513320,-9.475956,-1.875493,7.595674,-5.158310,-7.702159,3.051620,-7.205177,-5.485285,-4.942459,-2.460193,-6.097027,-3.884051,-0.788774,3.903487,1.773878,-1.351125,-6.439874,-6.088150,9.975087,4.465189,-7.574562,5.776701,3.566443,7.734981,7.518739,-5.235108,9.731922,-1.440922,9.433509,0.470045,-2.337300,-2.435214,8.559220,-7.594315,7.918880,-6.295616,-9.839372,6.669633,9.697981,-3.490745,-8.105274,6.055296,2.818422,-1.807244,5.282593,4.134118,6.752951,-8.264612,-1.019589,-7.778687,2.369917,9.271756,-7.874076,3.526645,-6.703665,5.766176,-1.854747,-7.450629,-6.962848,7.436222,3.884204,1.766614,-3.940663,7.514052,-8.559628,3.748227,-3.893086,9.327817,2.006032,-0.015562,-4.924094,-8.303785,-0.316667,-1.776531,0.739909,-7.322725,-2.840443,-5.580539,-1.748168,-5.540581,5.306448,-1.847602,-1.780645,-4.259954,-2.339052,7.006226,-9.826769,4.259100,2.362026,0.056391,1.109215,7.488482,3.184672,0.663792,8.687883,-7.681155,3.520122,-8.374226,8.038044,9.777748,5.526995,-8.451546,-7.601542,5.499545,-5.383535,8.085286,-2.781609,7.987728,-8.610662,4.312114,-5.434477,-6.480293,-0.975004,-9.808537,6.385057,9.707762,-6.003882,7.469357,-2.990638,-8.262318,5.507275,-2.648335,-6.084295,-9.794143,-9.970499,-3.535409,1.146888,-2.401528,3.789306,3.732795,-4.898669,-7.133642,0.372116,-0.962888,-3.254269,-0.224182,-0.293776,5.267482,-6.703437,3.460223,-9.958215,-0.313115,-5.743807,9.475629,9.766363,-2.839497,-4.563051,-0.679955,-9.405785,7.609566,-4.822064,7.375729,-1.800066,4.220438,-7.931533,-9.244398,0.337403,-3.632173,7.309651,5.664047,1.113087,4.642804,-1.783967,2.236919,-2.867595,8.924693,-5.447529,3.737541,-6.093898,1.657758,5.582553,4.399676,-6.078241,-9.794331,0.767102,-4.834492,1.842667,-6.206064,-9.342545,1.200848,-8.986119,6.184877,9.550932,-4.525745,9.543607,-8.390513,4.121261,8.617043,4.187744,7.340122,-9.611821,5.853031,6.622808,6.834583,4.068753,-2.995193,-5.471332,-6.575663,-9.944264,9.152213,6.768503,-7.203478,6.362795,-6.388951,7.131686,0.267679,-4.457961,-6.374115,8.726744,9.759813,-1.024839,-5.357549,7.992281,-0.878595,9.472744,6.361964,2.146163,1.147738,-1.707016,5.974966,-3.718378,9.318250,-4.466820,-4.905435,5.511105,-9.915757,-9.447390,-8.713105,-1.447694,2.443509,-4.204448,-2.621828,6.234287,-9.223573,5.407063,7.557064,8.990324,-7.122503,-0.479006,3.575359,-4.110682,3.444868,-8.728641,-8.452632,-6.439806,2.438217,6.121656,-5.027654,3.157084,-6.463806,7.911969,-8.236660,-6.927249,-5.779189,-8.497622,-1.044416,7.092579,6.942186,-5.275976,-1.960424,6.279011,7.071989,2.191764,4.987242,5.389948,-0.308311,-4.187744,0.209699,0.479546,1.576847,9.559898,7.261464,-4.497233,-7.897393,-4.146003,4.873916,-2.570147,-4.724451,5.263833,8.583607,4.633694,9.415472,-2.042066,-5.737616,-4.472536,5.354352,-3.767793,-4.268101,9.643332,6.755403,-8.251068,-6.609215,1.607540,-1.344078,-1.170527,5.430151,1.185549,1.839491,3.755070,-7.242003,-9.480246,7.647072,-3.560792,5.590282,1.586980,7.900123,7.242571,-8.747248,5.214658,2.240017,-0.434794,9.340471,2.998904,-1.097174,2.598123,-3.693120,-3.356509,-0.472386,-3.544654,1.839029,-0.351236,7.841148,-4.351631,-5.731258,-3.031266,0.212684,1.342328,9.600862,-2.684491,9.127375,-2.235930,3.376175,-9.562583,7.972696,0.455435,-1.501596,1.339870,0.379037,7.406377,2.534327,-3.229593,9.795852,-4.225023,-4.359790,-9.722068,-0.208317,-6.947303,4.634850,2.026484,3.351991,3.878228,-7.582344,0.028748,-0.314246,6.326563,-2.047997,6.901502,6.867116,-5.004529,-2.114352,-0.788266,7.619724,-7.195428,8.141540,6.535033,-9.659492,-6.344946,-6.848665,-2.959049,-2.637153,-1.571566,8.070978,-1.349387,0.805481,0.854682,6.310918,-4.811404,-3.947858,-1.971393,-3.465072,-6.676979,-4.160943,3.497406,-4.578148,-3.122429,-9.932179,3.130669,-3.160343,-1.970145,3.087303,9.738000,4.864973,5.042935,-4.825947,0.687304,-0.657522,4.836300,-3.867864,3.820102,-0.746358,-3.645885,-9.728116,7.570557,5.696266,8.884306,9.977255,-9.316382,-8.859112,-0.117918,9.803645,-0.033288,5.801450,-0.594421,-7.059304,-3.417281,0.345009,3.271919,-3.646917,-4.206188,5.409279,-5.654802,-9.495846,2.792474,1.061555,9.335583,-8.424246,-3.620766,2.040975,6.662430,-9.545160,7.049458,-0.361720,2.970536,3.073929,2.706541,3.122120,5.659192,-9.379208,7.112294,-0.466161,-7.624287,-9.297064,-2.090519,2.949543,1.115729,4.465352,-8.749270,-0.097638,-0.025566,0.319840,-9.712022,-7.928461,3.798064,-6.356651,-6.786921,1.333649,6.556156,8.578874,-8.713667,-8.397376,-4.023856,-9.281541,5.500188,-9.058347,-6.979628,1.543269,5.024123,-3.048135,-5.693939,7.049189,9.230247,1.986546,-9.344130,-1.477531,-6.604194,-0.636243,-7.351200,2.111895,9.589344,8.900663,2.697489,-1.708271,-7.657801,5.606672,-9.599081,3.738075,-6.087414,-1.158131,1.770592,8.049431,2.112463,-1.313573,-1.063990,-7.978863,-0.209764,2.687635,-7.875473,-2.621282,-8.731935,-6.425045,-5.383742,-4.217585,-9.417342,2.046023,2.847209,9.087704,-9.346398,-4.101188,0.317846,1.721582,-5.509683,-8.568994,-3.858330,-1.002390,-2.788061,4.261659,-0.666814,0.505096,8.887711,1.399683,8.206381,8.420943,-2.335001,-5.578170,-6.957815,2.293444,-2.567070,-5.824514,-4.165995,0.366774,0.899922,0.022613,-4.635643,-2.069196,2.793833,-0.447091,6.582286,2.740442,2.599492,3.637512,3.923855,8.617319,-2.026575,-9.776700,-7.282622,-7.987295,0.223213,1.895059,-4.908041,6.847354,9.029238,3.382221,7.164058,4.943991,-1.964854,8.711724,1.373273,-7.214603,-0.853605,0.020807,-9.766376,-6.013408,8.697467,-2.315839,8.748839,-1.231364,4.781704,2.334334,-0.718467,-9.849851,-1.666087,-2.430388,-4.072111,0.099775,6.007863,2.338873,-8.565320,8.603658,1.424361,-8.447056,8.288382,-9.815651,-6.206820,-6.059490,-6.878252,6.935609,-6.247520,-5.174718,-9.066273,0.029530,-4.503632,-9.714359,-9.964125,3.190607,8.852946,-6.018009,-1.177885,0.314845,5.794390,5.364377,-9.900791,-1.009517,-0.656896,0.621930,-8.956062,-2.747916,1.978157,-7.417610,7.203517,-1.946683,4.792631,3.946738,7.161984,-1.751476,-4.849100,-0.963663,-4.245925,8.328645,2.915251,-5.592092,7.408176,9.751900,9.060832,-2.631851,2.317968,1.757599,-8.311087,-2.109433,0.995782,-9.151691,-6.883298,1.743248,0.060993,7.244578,0.609874,-9.242070,-0.157416,-0.402632,8.355565,-4.364109,2.012250,5.825468,6.882430,8.987921,-1.442745,-8.977248,-2.097937,-2.876123,6.586006,-2.510172,3.353392,7.776018,-3.359141,7.402072,1.454891,-6.585576,8.006615,-7.948213,6.780490,7.019360,8.806204,-5.422983,0.492250,2.721487,-5.468128,-4.038893,-3.443166,-2.826428,0.027694,1.832117,6.484966,8.736018,9.453401,4.715529,3.925938,5.354634,9.479584,-4.421939,-7.022962,1.896412,3.653317,-2.340026,7.673311,0.016868,-9.255819,1.487486,-5.172897,-9.673936,-6.500102,9.529488,-1.950482,-4.273434,-5.551283,9.424073,-8.765632,-4.972707,-0.619394,-4.904852,7.429526,-2.499656,-2.867627,2.139737,-5.580494,-6.255574,-8.914395,-1.071973,-8.041226,-7.882713,6.606740,4.041467,-3.048521,2.170375,-0.926600,-1.030447,1.086380,0.681217,9.300123,3.926411,-9.881632,-5.139805,5.615436,-4.364270,-5.743452,-4.213593,-5.204682,5.588802,0.101735,8.258290,-1.644449,0.653370,-1.546155,9.781753,-2.979631,7.956901,2.948071,3.602696,-9.396992,-2.285614,-7.806211,-6.019741,8.850893,0.375206,-9.316822,-6.899173,-1.982179,1.500659,1.249127,-4.027697,0.833224,-3.430513,-7.417836,6.270056,4.359241,5.200348,-2.225409,-7.539690,5.392816,5.557080,-6.578820,8.401094,6.882352,6.432283,6.591980,-7.517771,6.559661,9.345651,-0.902220,-1.896173,4.028209,7.782192,4.982519,7.222307,6.109029,0.080669,-3.890319,2.947641,2.017087,-2.811047,-5.385782,2.463360,-8.980021,1.132300,6.898553,-9.065810,0.140451,-4.633146,-1.298581,-8.932039,-6.025793,9.140968,-9.609643,7.761985,-8.275596,-9.893300,-0.965250,-3.748415,2.821735,-2.556860,-3.137146,7.814165,-4.212809,-6.477560,7.086015,4.549670,-4.111933,-4.234607,0.347431,-8.990234,-5.952019,-8.465734,-2.314849,9.652874,1.922614,-5.003813,-8.653271,9.017292,-9.141153,6.689942,-6.834683,4.788701,-2.428145,7.985021,8.969430,3.581339,0.203770,3.144302,-1.288630,6.675955,-2.616934,8.964893,3.334147,3.700838,3.335425,5.892873,9.782369,-6.857171,-9.104265,9.241747,-3.638840,6.477067,5.256289,8.252337,6.757342,7.084467,3.216296,0.482127,7.583728,-8.488800,6.299591,1.638006,-4.354596,-7.813768,5.267230,4.325099,-3.972541,2.593460,8.133645,-6.361389,7.113310,-4.727984,-0.888968,8.824705,-1.397371,-6.481090,1.018444,4.906271,-2.352746,0.657166,9.941378,4.374090,2.062719,3.321121,4.104000,-7.425753,6.201602,6.520538,-9.380192,-5.217343,-1.693686,-8.671556,-9.510726,-8.177811,-1.979095,-1.289252,-2.907779,0.573353,3.021036,-9.975789,-3.629352,7.645627,1.413764,-7.657659,-3.970880,-2.049454,7.026141,-8.984921,-8.788113,-7.609885,-9.114497,0.067715,-2.697567,7.844390,7.154807,3.240532,-1.640140,-0.905880,6.022748,3.718266,7.081630,1.493854,-5.079543,-1.094036,-1.311196,0.615254,9.136131,5.401083,-9.069931,9.427377,-3.914760,6.718382,-0.309350,-6.645290,-5.872059,6.219357,0.225532,0.411513,-3.381463,0.379971,-2.871307,-9.856684,2.761032,-1.880369,-0.485507,9.192547,-2.721944,8.300224,-0.605759,-7.316063,0.823124,-9.103122,-7.499575,-1.334750,2.729597,9.890170,1.458376,-5.110904,6.859105,-2.758911,-8.440786,-0.228765,-2.812364,1.967866,0.290522,-1.516361,1.148880,-8.424141,-5.553924,6.293568,-6.989690,9.030500,-1.586868,-4.710100,-5.101341,1.396611,-6.084723,9.980362,4.542970,-6.864839,9.104911,4.319550,1.904449,-9.109001,-5.742908,-7.731069,8.347024,-3.760974,1.030671,6.486704,6.510386,-3.089018,9.818419,8.287521,3.394635,0.053349,-8.030081,6.157771,-6.473725,1.562570,8.810430,2.955983,1.682316,-1.966198,-4.670956,9.568070,-5.590023,-7.130297,1.853063,-2.639818,9.228553,7.633480,-9.534280,4.096208,0.421915,-1.556489,-2.500617,6.726804,3.487339,-2.885866,2.682457,-7.059130,-2.388955,5.026482,-7.644681,-7.171942,-3.699786,1.015853,-4.697816,7.972490,7.841436,0.718561,-2.506754,2.685938,-3.986221,2.614415,8.363096,-2.427406,-3.385460,-5.038519,7.099222,-7.828733,-0.274931,4.173608,3.067589,-6.381051,-9.873316,-1.140364,-3.884780,-1.805494,-4.193752,2.892157,8.840577,6.746711,1.636413,-8.550336,-1.204746,-4.720080,-0.087410,3.739352,5.994432,-3.892297,0.763614,-9.045762,1.780408,8.363589,-1.145808,1.981596,-2.355691,-3.929116,-5.745991,-9.162925,9.279158,-0.929159,-0.024287,4.179786,2.089397,9.092430,2.838920,2.299017,7.942244,-4.558563,2.256990,0.064734,-1.172698,1.907686,8.912518,4.928499,3.519303,-2.831149,6.660506,2.012619,-9.872346,-9.449922,-8.232881,-0.425790,-6.455369,6.845562,-8.095508,2.481795,-2.089204,-0.554848,-1.987942,4.178736,0.148894,-5.514135,0.545649,7.965649,-3.277795,8.123778,7.912057,-4.047361,-7.227794,7.268855,0.147047,7.039966,-3.686690,9.959006,2.749106,-0.241095,-1.310967,-7.539372,-9.491356,6.559351,4.733470,9.341344,-2.980563,-0.895119,8.662791,-8.823510,-2.983966,7.953975,7.103966,9.393895,4.885727,5.425359,-5.159440,0.611643,5.777086,-8.925800,-6.965859,-1.879119,1.443869,6.046702,-3.116990,7.288629,-7.492607,9.295165,8.318137,-9.842971,-3.168359,4.987968,6.352107,8.684348,2.652089,4.284955,8.405077,9.017707,-3.458511,-3.804635,-4.381755,9.953201,-7.204240,-9.160699,-8.104720,-4.497601,-4.761311,1.408975,-5.150593,-8.177511,-6.282995,5.820929,8.506057,4.224299,-9.445290,3.040262,5.543524,3.776184,2.880122,-5.954360,-0.655375,8.536307,-8.246908,0.916669,0.684680,-5.550637,7.622757,-3.804340,-0.154126,3.377832,1.835275,0.804468,8.753683,-1.377568,-3.721504,-0.343493,7.431238,9.918197,5.820454,-6.692259,6.279062,-9.858445,9.084989,9.393345,-6.797833,-7.603867,6.282373,9.373437,-4.541971,-7.421195,-2.383166,0.931899,-8.663463,8.835818,8.590748,-5.613375,-2.431235,-6.214058,9.720107,-3.988093,-6.015759,4.214355,-1.199256,-9.474588,-4.506613,-9.047406,-8.682048,-9.149591,-6.628482,-0.948470,-5.498225,-6.430798,5.766697,-5.421391,3.259117,0.296256,5.101616,3.620075,5.808692,-7.841806,-3.359412,-1.011932,-6.630040,8.966376,-7.110078,7.516560,0.409291,1.151958,-2.792700,9.983292,-5.670568,0.083566,-1.951271,-0.217402,-2.050902,6.612621,3.142379,6.213644,6.838168,-3.661880,-2.452704,-3.036198,-4.363130,7.693234,5.697209,-2.283153,2.600903,8.140463,-1.629248,1.240339,-2.905584,-6.014473,-6.893608,3.982018,-5.585460,2.840311,1.602121,-5.035077,2.518394,-7.512724,5.913159,9.465721,-9.266223,-2.382974,-6.038049,-0.636783,-0.217772,-0.099013,-9.302426,-4.599265,2.298070,-5.046366,6.966457,-3.582056,-5.084581,3.965612,9.044853,-4.231457,7.272101,6.242618,-6.445216,-3.523956,-4.660217,0.568862,6.041531,4.037945,0.852218,9.406426,6.866156,3.102480,0.555348,7.483095,1.997631,-8.395551,-9.549496,-6.572111,6.217145,6.500053,6.123806,8.268857,2.843635,-5.822274,-6.763268,5.499449,8.212543,0.617895,-1.726662,-7.607015,-5.116313,-0.401126,-2.303161,1.039321,-6.053514,4.028238,8.647222,-5.190900,4.116131,5.023650,-6.739368,8.850620,9.606571,-5.985075,4.082679,-2.272103,-5.305506,-4.781416,1.225704,-5.898382,3.556680,-2.180109,-1.682190,7.903527,3.314327,9.738197,2.090693,9.870379,7.776384,-5.486857,-6.000321,-7.420262,-9.908414,0.949468,-6.821520,7.460583,6.487102,-2.314265,-3.127836,-1.743521,-8.102631,1.452494,-7.408108,8.300321,6.516657,8.530527,-0.935457,-1.277330,-8.407617,-0.881247,0.225342,-2.384968,2.465018,5.247008,-3.162573,5.060585,4.681230,0.799037,-2.393838,-0.176982,-4.140992,8.664231,6.442933,7.560062,-4.835532,6.797843,2.149950,-4.898490,-1.193913,-3.137523,3.709819,-8.114121,1.120300,0.267453,-1.465834,0.878045,2.569439,1.189958,-1.201280,-5.411807,-6.273351,-4.414344,-3.668466,3.718411,-8.473676,9.941506,4.401292,9.308697,6.814687,-3.127137,-7.904280,8.937505,2.647032,-2.997418,6.068130,-0.948865,-5.759960,-6.736602,5.027474,-6.731840,5.927704,-8.125050,2.875183,0.465540,-7.085874,-2.644066,0.135311,-2.758966,-5.535679,-6.672608,8.842073,6.723980,-3.464039,-2.327183,4.954593,6.721234,4.382338,-3.023012,2.996243,5.462687,5.525502,-1.897088,9.233665,0.902902,-2.335774,-0.515843,-0.372519,8.093975,9.175420,7.248290,-4.149917,5.213404,-6.982296,-1.036674,-4.898592,2.501265,7.996425,-2.264418,-5.121324,-4.936918,-2.094621,-1.357794,5.207842,3.852919,-4.090734,3.389937,0.344799,-4.027268,-4.448761,-6.758804,-7.574481,5.587642,3.634582,3.723324,6.478748,-8.620206,-9.016153,2.174330,3.351873,-2.765213,9.952039,-8.008175,-1.082504,-7.777197,-3.701168,1.233859,-0.356795,-9.087579,4.387759,8.225222,-6.391670,-8.544703,-3.133661,-8.120783,-9.792229,6.092525,-3.237368,-3.256510,-3.137507,-8.831624,5.915178,-8.416571,-4.221108,-9.126595,-0.762311,-4.032301,6.023169,0.546669,-7.608729,2.002065,-3.913592,-4.049216,5.080142,1.911693,9.030439,-3.328630,-5.780411,-7.215929,6.898501,-2.451628,-0.498565,-8.353790,8.518682,-4.710442,2.812760,-4.005751,-5.359153,9.571983,6.043379,-7.890909,-6.265481,-4.588487,7.065099,4.620659,7.822237,-5.257003,-7.231071,0.848747,-1.811660,-7.255133,-6.166300,9.204681,4.832006,-1.474634,5.979693,-9.012746,8.787295,-9.114962,0.115147,8.024875,9.925242,9.731489,1.369144,4.082314,-4.404030,9.714813,-0.759766,0.298949,2.701877,7.522719,-0.049843,-9.254158,-8.884682,-7.878003,-2.102814,-8.960795,5.455041,-4.441773,-1.145427,-6.067963,5.347849,9.379598,-7.562487,8.725338,-3.242062,0.240178,-1.632343,-5.484703,-0.617438,0.895394,2.334885,4.054878,2.263195,1.484366,3.452222,-1.396337,7.505519,7.138464,-9.449335,-0.069212,3.691975,-0.570750,8.952121,-2.590539,1.682846,0.208774,1.218102,-1.828682,-6.520251,-7.896793,3.250603,-4.550957,8.868951,9.515699,-9.807198,-2.847584,9.256857,-4.742960,-9.447021,-3.426472,-8.185348,-2.148570,-1.859911,-8.370078,-4.283078,8.310369,6.966179,-2.518837,7.834763,-1.728854,1.888472,8.631287,7.886106,-1.625831,-6.176025,-6.395018,-0.379257,-8.930590,3.890245,3.568707,6.206740,7.194353,-0.957439,0.658111,1.588857,9.285827,3.387557,1.843847,-2.300607,-5.441921,1.083195,3.662311,0.211706,-5.753259,-5.820153,-4.957665,-4.170941,-8.880263,2.704748,-1.414749,-2.449775,-5.911721,-7.624015,-2.221943,0.283410,3.617967,4.713764,-7.742555,-0.466073,1.646951,-3.597973,0.490665,-1.298321,0.334730,6.122999,-6.261448,7.359456,7.774111,1.311933,0.378830,-2.604925,1.123636,0.489930,-2.413065,-9.315632,4.332168,0.335998,-6.637198,-7.416829,-0.941968,4.678348,5.328167,1.284274,8.201053,5.688962,0.993991,6.452667,3.673277,-6.624383,4.917561,-7.175496,9.190551,4.063371,4.110769,3.424888,3.028457,-9.141625,4.693000,-1.261784,-0.123834,1.826102,2.714354,-1.549620,-8.226226,5.416483,-1.049037,-8.148941,4.895703,2.787852,0.018967,-9.925188,8.454118,-5.391379,-6.959310,1.421073,-3.961471,-4.642276,-9.348648,-3.358797,7.818811,-5.464420,2.161516,1.722364,-6.412133,5.014197,4.959955,-2.025100,4.027245,-2.597238,8.144330,-5.840052,-7.602643,-1.376224,-9.129351,4.194287,-4.331370,0.523887,-5.851874,-7.095839,2.495951,0.212021,-1.373931,4.764683,-5.647823,7.302027,-2.156451,3.060617,4.115634,0.755500,-8.158411,8.577117,-1.738734,0.090141,-0.145652,3.639615,8.978411,-8.646910,-5.079718,8.515993,9.669188,2.061874,9.854611,5.286714,-5.073703,-8.504119,0.403350,5.245051,-6.484065,0.230229,-2.476740,-1.754360,3.727271,5.564389,-2.504315,-5.144330,-4.212346,1.790498,-6.594826,-8.459270,3.994170,6.698669,-7.236847,-1.383312,2.262672,4.884226,-8.249082,-5.076630,9.196971,-5.281270,-1.264982,7.067029,-0.746102,-5.033858,2.967602,4.184949,1.164985,-3.923835,8.742896,-8.295461,-5.063098,-5.476739,1.588352,-8.489473,4.188490,1.571145,4.565414,-0.353238,4.618383,-2.853748,4.755299,-2.565273,-4.890944,-6.530281,7.615469,1.907331,8.942077,9.648957,-9.785163,9.230694,-6.613153,0.746193,5.766026,4.449233,0.951330,-9.005272,6.208404,9.561631,2.469992,6.743270,2.055209,-6.424832,-3.079597,5.218569,7.196818,-3.325679,5.059737,2.271950,6.287711,-1.612008,-2.419289,7.164744,5.516661,9.656997,8.820442,7.524744,2.870136,6.697602,5.455090,-2.989031,0.261978,-3.063102,4.534656,8.477323,-2.695826,6.452100,-5.880253,-9.258819,4.904817,-5.769855,-4.197239,3.152228,7.667061,-4.019959,-0.826348,3.266505,6.282724,-9.780506,6.755077,-6.972242,4.361423,-5.409009,-0.562870,6.970947,7.463657,-2.864132,-1.101693,7.735829,-0.265934,-1.162827,1.490689,-1.028224,-8.546095,4.638192,2.258797,9.200841,8.313298,-7.935090,2.839287,7.233240,-3.131720,-3.012854,-0.833200,-7.183207,5.330875,6.186556,7.598851,-0.210598,-7.506228,8.692136,6.463585,8.201118,7.905822,-0.877134,8.804307,2.091008,-9.465409,-4.305432,0.775198,3.837608,-2.271813,0.190796,0.365251,7.417335,8.810647,5.107332,7.957379,1.267077,-3.361637,0.293953,-0.090882,2.845166,5.550885,5.180989,0.552114,9.121504,8.081305,0.057285,-8.327532,-7.312252,3.185087,-6.066364,-1.170492,3.405804,-5.540081,4.087174,9.968051,5.730708,-3.900621,-9.194745,4.290364,3.661533,-3.549052,3.774597,9.382390,7.916624,4.512659,-0.091309,2.105010,2.702973,-6.558321,-8.481098,4.867108,-1.703199,-3.411434,1.138995,5.224221,-0.117435,9.980238,-2.121285,-2.144334,-7.941438,-6.075683,9.887384,-7.626427,0.889025,9.847292,6.529283,0.632784,5.971417,-5.586295,2.529917,9.852267,2.984982,-3.163876,-9.645896,6.106551,-3.891900,3.503440,-5.459557,-3.870914,-1.149621,5.138755,8.072868,-8.997482,6.167143,6.528765,-8.917184,-9.034577,-6.546175,5.389435,7.638410,9.019553,-1.722047,-4.748263,-5.804838,-8.974993,-9.642391,-3.862392,-4.538879,-2.061183,9.618141,4.622424,3.301447,-8.178428,-5.892537,-9.915194,-1.255297,6.159122,-5.173853,3.760946,7.572754,3.588053,-0.668211,5.988882,-3.737359,-5.442957,1.409917,2.013854,4.735500,-7.973907,-0.740044,-6.869084,-7.921252,5.209313,5.898210,-6.760077,6.745444,-5.632667,1.776779,-6.438567,-4.428270,-4.449905,-2.759934,-8.410217,5.498564,9.302541,1.997426,-6.386913,-6.162516,-1.346573,0.566412,-1.640722,-6.800519,-4.928741,-0.147642,-3.126363,8.090339,-7.922219,-7.174793,4.474416,-6.367843,4.181270,-2.582819,0.637082,-0.842886,-0.729730,-3.787458,-7.629974,-3.713841,4.655635,8.184050,8.688742,-0.103525,6.486755,-5.683740,-5.518372,2.487503,-2.339326,9.227231,-4.889872,4.709494,4.705130,2.090555,-6.399516,-8.156873,-7.489013,9.656409,-6.514040,-3.493165,7.003776,3.540068,6.552358,4.865995,-7.985520,6.918780,-1.831238,-1.682098,0.806025,8.861608,7.105645,6.292232,-0.232578,4.794390,-6.779191,-4.161321,-2.402682,3.636659,-0.891772,1.401731,1.587015,-4.351414,1.117893,-0.654412,-9.595076,-0.286049,3.522302,-0.876588,6.280118,3.661053,8.455195,1.232340,3.994151,1.659547,0.815175,-3.029092,8.916172,2.290587,9.440734,7.472705,8.635273,5.228531,9.689771,-7.211168,7.481833,-1.032680,6.452778,-2.999119,-9.576929,9.096699,-1.260141,0.682530,-6.288940,-4.916806,-0.271929,5.121449,-8.391596,-1.862818,-4.483152,-5.807371,-4.496095,-1.776072,-8.537066,-9.270808,-4.700006,-1.332463,-2.537603,0.939513,-5.996684,-3.938471,8.462288,6.329713,5.179826,-7.613777,-5.365200,3.795768,4.371597,4.377207,2.716736,1.427364,6.471420,-9.666593,0.842747,-5.469868,-9.702899,-2.608537,-5.964077,4.205720,2.793767,-2.481436,-0.828638,1.978924,3.905792,1.665748,-4.674886,4.236026,-6.852417,4.304114,0.833193,-0.771235,8.131488,9.951790,-9.264872,1.325488,-6.742550,1.070777,2.073517,5.614090,5.762857,9.162287,8.265655,0.455634,9.008194,6.821820,-1.151536,-6.392025,-5.882961,-9.568950,-8.185231,-4.992364,0.400736,6.126882,-5.845941,8.403219,3.378022,-4.591432,5.496448,-6.086633,-7.059259,9.658597,1.623063,-5.408979,-3.624271,-7.813726,-7.086682,6.780040,6.030360,4.716442,5.198175,1.222902,9.440870,6.373494,-6.873548,9.968088,9.074078,8.130025,-8.095344,-9.063549,-0.607845,0.418645,-8.196844,-2.504734,0.785723,1.554239,1.396984,8.027953,-2.591591,2.490661,7.622154,-9.440334,-1.378339,5.192180,0.106564,0.795032,1.744207,0.717684,6.763585,0.988267,5.286126,-7.907712,2.153177,1.837284,-3.919719,-6.572999,-2.213614,0.416092,7.580708,0.507288,-8.135507,-4.951665,-3.377687,3.774519,-8.328790,-9.280525,-4.210095,-3.680409,0.393687,1.787166,-9.967444,8.473818,-5.337291,3.192621,1.507636,7.110578,6.160938,2.556709,4.131986,-4.139211,8.981415,7.887383,4.031025,-0.712788,6.386610,-7.676934,4.001552,-4.251362,-8.934039,4.605531,6.893960,-6.604735,6.025123,-1.154406,-8.135695,-1.743870,9.710332,9.972838,4.461009,4.229757,-3.023179,-3.915179,6.754595,6.805089,0.949845,-1.138635,7.194629,5.425118,-8.195909,8.175380,-3.577797,9.366064,7.661845,-2.132033,-2.600735,-8.017502,-1.057545,-3.357961,4.412909,5.090158,6.968859,9.126753,-0.862135,5.408817,-2.752810,-5.124936,-3.962097,6.787712,-3.575007,-3.003691,8.698704,7.577154,0.222037,-0.550975,-3.713046,0.002537,9.168430,-6.891506,-0.503387,-9.511094,5.122990,0.368095,-4.820902,7.369363,6.729214,5.324481,-4.774718,-5.296507,7.646952,5.890830,-8.700627,1.658155,4.450473,-3.691672,3.891073,3.859368,4.683874,-7.056712,7.863376,-6.925536,8.577124,1.897169,3.868266,4.617475,-6.213054,-8.547394,-0.133924,-4.691794,6.130466,5.753866,-0.544278,6.469807,5.630039,7.405722,-9.925763,6.068813,-3.700273,5.653259,-5.055807,-5.399955,5.856237,-4.396869,-6.583426,-3.281330,1.752851,-5.744681,-6.130137,2.955466,9.739004,-3.973125,-9.975548,6.731393,-8.948906,-2.450922,2.388841,-6.105822,5.313402,-9.180787,3.625835,-0.106489,-1.365103,-4.578992,-2.909251,5.388308,9.553843,7.372821,1.819314,-5.090838,-8.035010,1.567102,7.938496,-8.494887,-6.386288,-5.911637,2.280113,-9.375237,3.991062,-0.720805,-2.852439,1.334021,2.268165,3.038595,5.395712,9.730550,3.031760,2.915517,-8.443580,4.619551,8.698542,-6.251940,-8.158845,-0.728375,-4.164259,-0.801192,-1.104909,-4.927830,-8.070785,8.900503,3.635979,8.394745,7.529217,6.805983,6.755954,-0.360839,-7.261825,8.687216,3.970647,-3.734048,6.087318,-0.707878,-0.416451,0.993794,-4.983935,-0.301912,7.691914,-4.688098,-3.801025,-2.817324,1.899629,-6.950671,-4.101396,-1.352357,-1.043308,9.064670,2.238966,8.660644,-9.147763,0.451156,0.887491,-0.127253,4.938925,2.014915,-9.936010,6.978379,-7.871366,6.042831,-4.326673,-1.433968,-1.896608,-8.060202,3.067433,1.897775,-9.346927,0.341066,-2.364601,9.647386,-4.579025,3.877164,-7.873274,-4.474911,4.526353,9.809225,-8.019246,-5.378940,6.099097,-0.180114,-1.821883,-7.431813,-5.403628,9.716643,7.054907,4.385998,3.705551,-1.741760,5.477318,6.581404,-5.887725,-5.993246,-5.404049,5.540307,6.220365,6.208993,8.649801,0.907268,2.957833,-4.813922,2.669170,-7.555581,2.849695,-7.811046,-2.658848,9.520800,3.112125,0.840662,-5.957953,5.079763,-0.388830,4.664754,1.305653,-1.101818,6.967486,7.778109,-3.910925,-7.948981,7.155207,-7.247814,-2.144045,-6.937033,-2.883666,9.369084,0.597778,-1.871394,4.808626,0.741945,-9.894627,5.661591,6.227998,-8.964170,3.814061,6.159211,-7.679595,-0.268917,2.201505,-9.753831,-5.265674,-5.485703,-2.013043,6.745919,-4.602715,-5.995388,-0.527814,1.841254,6.541569,8.513109,-9.306299,3.395162,4.563054,8.340259,-9.934229,-8.821484,4.282331,-5.872437,1.888531,-8.167732,8.805828,7.205583,-3.537958,1.852199,-9.096209,-3.243948,3.851280,3.088189,4.510351,3.226068,-4.268620,-5.043582,-1.458397,-5.179614,0.136620,4.894111,9.764697,-5.288499,1.400873,6.020312,8.145224,-3.514125,3.093486,1.180437,-0.824603,6.562277,-0.031789,0.453443,-8.702275,-1.719561,-8.386014,-0.376897,-0.674601,8.880248,-5.696840,-1.326602,3.104316,-6.654396,-0.583235,6.212922,-2.491258,-4.677651,7.746425,9.330465,2.274342,7.725997,-3.257303,0.457209,-8.357555,-7.508697,-4.754942,-2.973883,-5.212017,-4.071738,-8.059291,9.719765,-3.371634,5.406763,2.407156,-9.955697,5.466828,-1.746636,9.389457,-3.146708,8.269211,2.788556,8.046431,2.606962,-6.728648,5.513638,7.815548,-8.955353,-8.577558,9.788506,-5.538267,-3.493365,5.191069,9.803915,-9.428650,0.300314,6.258430,6.262655,-0.769656,-3.217173,0.032035,-1.489976,-4.247734,-8.091679,-3.881222,8.380780,1.407283,-5.884053,-4.672792,-3.847919,-3.873080,-5.447140,-2.690120,-0.455098,-5.982519,5.521637,-8.506687,8.308579,-3.807728,1.694321,3.584100,-4.807271,-3.112175,-4.509593,-0.915008,-3.820698,-1.279172,-4.547691,-4.812079,2.491841,1.832812,-2.305427,-6.760492,7.466860], dtype = "float64")#candidate|5314|(3840,)|const|float64
call_5312 = relay.TupleGetItem(func_4839_call(relay.reshape(var_5313.astype('float32'), [360,]), relay.reshape(const_5314.astype('float64'), [3840,]), ), 2)
call_5315 = relay.TupleGetItem(func_4842_call(relay.reshape(var_5313.astype('float32'), [360,]), relay.reshape(const_5314.astype('float64'), [3840,]), ), 2)
var_5323 = relay.var("var_5323", dtype = "float64", shape = (3840,))#candidate|5323|(3840,)|var|float64
bop_5324 = relay.right_shift(const_5314.astype('uint64'), relay.reshape(var_5323.astype('uint64'), relay.shape_of(const_5314))) # shape=(3840,)
bop_5363 = relay.greater_equal(var_5313.astype('bool'), relay.reshape(call_5312.astype('bool'), relay.shape_of(var_5313))) # shape=(180, 2)
bop_5366 = relay.greater_equal(var_5313.astype('bool'), relay.reshape(call_5315.astype('bool'), relay.shape_of(var_5313))) # shape=(180, 2)
output = relay.Tuple([call_5286,call_5302,var_5303,bop_5324,bop_5363,])
output2 = relay.Tuple([call_5287,call_5304,var_5303,bop_5324,bop_5366,])
func_5370 = relay.Function([var_5303,var_5313,var_5323,], output)
mod['func_5370'] = func_5370
mod = relay.transform.InferType()(mod)
var_5371 = relay.var("var_5371", dtype = "float32", shape = (16, 6))#candidate|5371|(16, 6)|var|float32
var_5372 = relay.var("var_5372", dtype = "float32", shape = (180, 2))#candidate|5372|(180, 2)|var|float32
var_5373 = relay.var("var_5373", dtype = "float64", shape = (3840,))#candidate|5373|(3840,)|var|float64
output = func_5370(var_5371,var_5372,var_5373,)
func_5374 = relay.Function([var_5371,var_5372,var_5373,], output)
mutated_mod['func_5374'] = func_5374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5457 = relay.var("var_5457", dtype = "float64", shape = (15, 11, 6))#candidate|5457|(15, 11, 6)|var|float64
var_5458 = relay.var("var_5458", dtype = "float64", shape = (15, 11, 6))#candidate|5458|(15, 11, 6)|var|float64
bop_5459 = relay.not_equal(var_5457.astype('bool'), relay.reshape(var_5458.astype('bool'), relay.shape_of(var_5457))) # shape=(15, 11, 6)
output = bop_5459
output2 = bop_5459
func_5464 = relay.Function([var_5457,var_5458,], output)
mod['func_5464'] = func_5464
mod = relay.transform.InferType()(mod)
mutated_mod['func_5464'] = func_5464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5464_call = mutated_mod.get_global_var('func_5464')
var_5466 = relay.var("var_5466", dtype = "float64", shape = (15, 11, 6))#candidate|5466|(15, 11, 6)|var|float64
var_5467 = relay.var("var_5467", dtype = "float64", shape = (15, 11, 6))#candidate|5467|(15, 11, 6)|var|float64
call_5465 = func_5464_call(var_5466,var_5467,)
output = call_5465
func_5468 = relay.Function([var_5466,var_5467,], output)
mutated_mod['func_5468'] = func_5468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_5481 = relay.TupleGetItem(func_2765_call(), 0)
call_5482 = relay.TupleGetItem(func_2766_call(), 0)
func_1608_call = mod.get_global_var('func_1608')
func_1609_call = mutated_mod.get_global_var('func_1609')
call_5500 = relay.TupleGetItem(func_1608_call(), 0)
call_5501 = relay.TupleGetItem(func_1609_call(), 0)
output = relay.Tuple([call_5481,call_5500,])
output2 = relay.Tuple([call_5482,call_5501,])
func_5512 = relay.Function([], output)
mod['func_5512'] = func_5512
mod = relay.transform.InferType()(mod)
mutated_mod['func_5512'] = func_5512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mutated_mod.get_global_var('func_5512')
call_5513 = func_5512_call()
output = call_5513
func_5514 = relay.Function([], output)
mutated_mod['func_5514'] = func_5514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
call_5520 = relay.TupleGetItem(func_1707_call(), 0)
call_5521 = relay.TupleGetItem(func_1709_call(), 0)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_5534 = relay.TupleGetItem(func_4154_call(), 0)
call_5535 = relay.TupleGetItem(func_4155_call(), 0)
func_4783_call = mod.get_global_var('func_4783')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_5536 = relay.TupleGetItem(func_4783_call(), 0)
call_5537 = relay.TupleGetItem(func_4785_call(), 0)
output = relay.Tuple([call_5520,call_5534,call_5536,])
output2 = relay.Tuple([call_5521,call_5535,call_5537,])
func_5538 = relay.Function([], output)
mod['func_5538'] = func_5538
mod = relay.transform.InferType()(mod)
mutated_mod['func_5538'] = func_5538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5538_call = mutated_mod.get_global_var('func_5538')
call_5539 = func_5538_call()
output = call_5539
func_5540 = relay.Function([], output)
mutated_mod['func_5540'] = func_5540
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5565 = relay.var("var_5565", dtype = "float64", shape = (14, 5, 10))#candidate|5565|(14, 5, 10)|var|float64
uop_5566 = relay.log2(var_5565.astype('float64')) # shape=(14, 5, 10)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_5569 = relay.TupleGetItem(func_4154_call(), 0)
call_5570 = relay.TupleGetItem(func_4155_call(), 0)
func_3462_call = mod.get_global_var('func_3462')
func_3464_call = mutated_mod.get_global_var('func_3464')
call_5578 = relay.TupleGetItem(func_3462_call(), 0)
call_5579 = relay.TupleGetItem(func_3464_call(), 0)
output = relay.Tuple([uop_5566,call_5569,call_5578,])
output2 = relay.Tuple([uop_5566,call_5570,call_5579,])
func_5583 = relay.Function([var_5565,], output)
mod['func_5583'] = func_5583
mod = relay.transform.InferType()(mod)
mutated_mod['func_5583'] = func_5583
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5584 = relay.var("var_5584", dtype = "float64", shape = (14, 5, 10))#candidate|5584|(14, 5, 10)|var|float64
func_5583_call = mutated_mod.get_global_var('func_5583')
call_5585 = func_5583_call(var_5584)
output = call_5585
func_5586 = relay.Function([var_5584], output)
mutated_mod['func_5586'] = func_5586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1683_call = mod.get_global_var('func_1683')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_5668 = relay.TupleGetItem(func_1683_call(), 0)
call_5669 = relay.TupleGetItem(func_1684_call(), 0)
output = relay.Tuple([call_5668,])
output2 = relay.Tuple([call_5669,])
func_5670 = relay.Function([], output)
mod['func_5670'] = func_5670
mod = relay.transform.InferType()(mod)
mutated_mod['func_5670'] = func_5670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5670_call = mutated_mod.get_global_var('func_5670')
call_5671 = func_5670_call()
output = call_5671
func_5672 = relay.Function([], output)
mutated_mod['func_5672'] = func_5672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_5699 = relay.TupleGetItem(func_2902_call(), 0)
call_5700 = relay.TupleGetItem(func_2904_call(), 0)
func_2223_call = mod.get_global_var('func_2223')
func_2224_call = mutated_mod.get_global_var('func_2224')
call_5712 = relay.TupleGetItem(func_2223_call(), 0)
call_5713 = relay.TupleGetItem(func_2224_call(), 0)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_5735 = relay.TupleGetItem(func_1381_call(), 0)
call_5736 = relay.TupleGetItem(func_1382_call(), 0)
func_1381_call = mod.get_global_var('func_1381')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_5743 = relay.TupleGetItem(func_1381_call(), 0)
call_5744 = relay.TupleGetItem(func_1382_call(), 0)
output = relay.Tuple([call_5699,call_5712,call_5735,call_5743,])
output2 = relay.Tuple([call_5700,call_5713,call_5736,call_5744,])
func_5745 = relay.Function([], output)
mod['func_5745'] = func_5745
mod = relay.transform.InferType()(mod)
mutated_mod['func_5745'] = func_5745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5745_call = mutated_mod.get_global_var('func_5745')
call_5746 = func_5745_call()
output = call_5746
func_5747 = relay.Function([], output)
mutated_mod['func_5747'] = func_5747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_5765 = func_1417_call()
call_5766 = func_1417_call()
var_5772 = relay.var("var_5772", dtype = "float64", shape = (15, 4, 16))#candidate|5772|(15, 4, 16)|var|float64
bop_5773 = relay.subtract(call_5765.astype('int64'), var_5772.astype('int64')) # shape=(15, 4, 16)
bop_5776 = relay.subtract(call_5766.astype('int64'), var_5772.astype('int64')) # shape=(15, 4, 16)
output = bop_5773
output2 = bop_5776
func_5777 = relay.Function([var_5772,], output)
mod['func_5777'] = func_5777
mod = relay.transform.InferType()(mod)
mutated_mod['func_5777'] = func_5777
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5778 = relay.var("var_5778", dtype = "float64", shape = (15, 4, 16))#candidate|5778|(15, 4, 16)|var|float64
func_5777_call = mutated_mod.get_global_var('func_5777')
call_5779 = func_5777_call(var_5778)
output = call_5779
func_5780 = relay.Function([var_5778], output)
mutated_mod['func_5780'] = func_5780
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_5795 = func_3060_call()
call_5796 = func_3060_call()
func_4951_call = mod.get_global_var('func_4951')
func_4952_call = mutated_mod.get_global_var('func_4952')
call_5797 = relay.TupleGetItem(func_4951_call(), 0)
call_5798 = relay.TupleGetItem(func_4952_call(), 0)
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_5808 = relay.TupleGetItem(func_3366_call(), 0)
call_5809 = relay.TupleGetItem(func_3368_call(), 0)
output = relay.Tuple([call_5795,call_5797,call_5808,])
output2 = relay.Tuple([call_5796,call_5798,call_5809,])
func_5824 = relay.Function([], output)
mod['func_5824'] = func_5824
mod = relay.transform.InferType()(mod)
mutated_mod['func_5824'] = func_5824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5824_call = mutated_mod.get_global_var('func_5824')
call_5825 = func_5824_call()
output = call_5825
func_5826 = relay.Function([], output)
mutated_mod['func_5826'] = func_5826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_5843 = func_3060_call()
call_5844 = func_3060_call()
output = relay.Tuple([call_5843,])
output2 = relay.Tuple([call_5844,])
func_5858 = relay.Function([], output)
mod['func_5858'] = func_5858
mod = relay.transform.InferType()(mod)
output = func_5858()
func_5859 = relay.Function([], output)
mutated_mod['func_5859'] = func_5859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_5909 = relay.TupleGetItem(func_2156_call(), 0)
call_5910 = relay.TupleGetItem(func_2158_call(), 0)
func_3105_call = mod.get_global_var('func_3105')
func_3108_call = mutated_mod.get_global_var('func_3108')
var_5942 = relay.var("var_5942", dtype = "float32", shape = (96,))#candidate|5942|(96,)|var|float32
call_5941 = func_3105_call(relay.reshape(var_5942.astype('float32'), [12, 1, 8]))
call_5943 = func_3105_call(relay.reshape(var_5942.astype('float32'), [12, 1, 8]))
output = relay.Tuple([call_5909,call_5941,var_5942,])
output2 = relay.Tuple([call_5910,call_5943,var_5942,])
func_5970 = relay.Function([var_5942,], output)
mod['func_5970'] = func_5970
mod = relay.transform.InferType()(mod)
mutated_mod['func_5970'] = func_5970
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5971 = relay.var("var_5971", dtype = "float32", shape = (96,))#candidate|5971|(96,)|var|float32
func_5970_call = mutated_mod.get_global_var('func_5970')
call_5972 = func_5970_call(var_5971)
output = call_5972
func_5973 = relay.Function([var_5971], output)
mutated_mod['func_5973'] = func_5973
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5995 = relay.var("var_5995", dtype = "float32", shape = (2, 14, 12))#candidate|5995|(2, 14, 12)|var|float32
uop_5996 = relay.atan(var_5995.astype('float32')) # shape=(2, 14, 12)
uop_5999 = relay.cosh(var_5995.astype('float64')) # shape=(2, 14, 12)
func_4604_call = mod.get_global_var('func_4604')
func_4606_call = mutated_mod.get_global_var('func_4606')
call_6001 = func_4604_call()
call_6002 = func_4604_call()
bop_6030 = relay.right_shift(uop_5996.astype('uint32'), relay.reshape(uop_5999.astype('uint32'), relay.shape_of(uop_5996))) # shape=(2, 14, 12)
output = relay.Tuple([call_6001,bop_6030,])
output2 = relay.Tuple([call_6002,bop_6030,])
func_6042 = relay.Function([var_5995,], output)
mod['func_6042'] = func_6042
mod = relay.transform.InferType()(mod)
var_6043 = relay.var("var_6043", dtype = "float32", shape = (2, 14, 12))#candidate|6043|(2, 14, 12)|var|float32
output = func_6042(var_6043)
func_6044 = relay.Function([var_6043], output)
mutated_mod['func_6044'] = func_6044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_6063 = relay.TupleGetItem(func_4107_call(), 0)
call_6064 = relay.TupleGetItem(func_4108_call(), 0)
func_4438_call = mod.get_global_var('func_4438')
func_4441_call = mutated_mod.get_global_var('func_4441')
const_6083 = relay.const([[True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,False],[True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,True,True],[True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False],[False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False],[True,False,True,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True],[False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True],[True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False],[False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False],[True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,True,True,True,True],[True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False],[True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,False],[False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,True,True,False]], dtype = "bool")#candidate|6083|(12, 60)|const|bool
call_6082 = relay.TupleGetItem(func_4438_call(relay.reshape(const_6083.astype('bool'), [15, 3, 16])), 1)
call_6084 = relay.TupleGetItem(func_4441_call(relay.reshape(const_6083.astype('bool'), [15, 3, 16])), 1)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_6090 = relay.TupleGetItem(func_4154_call(), 0)
call_6091 = relay.TupleGetItem(func_4155_call(), 0)
func_2632_call = mod.get_global_var('func_2632')
func_2634_call = mutated_mod.get_global_var('func_2634')
call_6111 = relay.TupleGetItem(func_2632_call(), 0)
call_6112 = relay.TupleGetItem(func_2634_call(), 0)
func_3313_call = mod.get_global_var('func_3313')
func_3314_call = mutated_mod.get_global_var('func_3314')
call_6136 = func_3313_call()
call_6137 = func_3313_call()
output = relay.Tuple([call_6063,call_6082,const_6083,call_6090,call_6111,call_6136,])
output2 = relay.Tuple([call_6064,call_6084,const_6083,call_6091,call_6112,call_6137,])
func_6139 = relay.Function([], output)
mod['func_6139'] = func_6139
mod = relay.transform.InferType()(mod)
output = func_6139()
func_6140 = relay.Function([], output)
mutated_mod['func_6140'] = func_6140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_6143 = relay.TupleGetItem(func_1561_call(), 0)
call_6144 = relay.TupleGetItem(func_1563_call(), 0)
var_6174 = relay.var("var_6174", dtype = "float64", shape = (15, 1, 16))#candidate|6174|(15, 1, 16)|var|float64
bop_6175 = relay.logical_and(call_6143.astype('bool'), relay.reshape(var_6174.astype('bool'), relay.shape_of(call_6143))) # shape=(15, 1, 16)
bop_6178 = relay.logical_and(call_6144.astype('bool'), relay.reshape(var_6174.astype('bool'), relay.shape_of(call_6144))) # shape=(15, 1, 16)
func_4997_call = mod.get_global_var('func_4997')
func_4999_call = mutated_mod.get_global_var('func_4999')
var_6181 = relay.var("var_6181", dtype = "float64", shape = (1920,))#candidate|6181|(1920,)|var|float64
call_6180 = relay.TupleGetItem(func_4997_call(relay.reshape(var_6181.astype('float64'), [1920,])), 1)
call_6182 = relay.TupleGetItem(func_4999_call(relay.reshape(var_6181.astype('float64'), [1920,])), 1)
func_2788_call = mod.get_global_var('func_2788')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_6186 = relay.TupleGetItem(func_2788_call(), 0)
call_6187 = relay.TupleGetItem(func_2789_call(), 0)
output = relay.Tuple([bop_6175,call_6180,var_6181,call_6186,])
output2 = relay.Tuple([bop_6178,call_6182,var_6181,call_6187,])
func_6196 = relay.Function([var_6174,var_6181,], output)
mod['func_6196'] = func_6196
mod = relay.transform.InferType()(mod)
var_6197 = relay.var("var_6197", dtype = "float64", shape = (15, 1, 16))#candidate|6197|(15, 1, 16)|var|float64
var_6198 = relay.var("var_6198", dtype = "float64", shape = (1920,))#candidate|6198|(1920,)|var|float64
output = func_6196(var_6197,var_6198,)
func_6199 = relay.Function([var_6197,var_6198,], output)
mutated_mod['func_6199'] = func_6199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_6207 = relay.TupleGetItem(func_2765_call(), 0)
call_6208 = relay.TupleGetItem(func_2766_call(), 0)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_6220 = relay.TupleGetItem(func_2034_call(), 2)
call_6221 = relay.TupleGetItem(func_2035_call(), 2)
output = relay.Tuple([call_6207,call_6220,])
output2 = relay.Tuple([call_6208,call_6221,])
func_6227 = relay.Function([], output)
mod['func_6227'] = func_6227
mod = relay.transform.InferType()(mod)
mutated_mod['func_6227'] = func_6227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mutated_mod.get_global_var('func_6227')
call_6228 = func_6227_call()
output = call_6228
func_6229 = relay.Function([], output)
mutated_mod['func_6229'] = func_6229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5824_call = mod.get_global_var('func_5824')
func_5826_call = mutated_mod.get_global_var('func_5826')
call_6248 = relay.TupleGetItem(func_5824_call(), 0)
call_6249 = relay.TupleGetItem(func_5826_call(), 0)
output = call_6248
output2 = call_6249
func_6255 = relay.Function([], output)
mod['func_6255'] = func_6255
mod = relay.transform.InferType()(mod)
output = func_6255()
func_6256 = relay.Function([], output)
mutated_mod['func_6256'] = func_6256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1274_call = mod.get_global_var('func_1274')
func_1275_call = mutated_mod.get_global_var('func_1275')
call_6285 = relay.TupleGetItem(func_1274_call(), 0)
call_6286 = relay.TupleGetItem(func_1275_call(), 0)
output = call_6285
output2 = call_6286
func_6355 = relay.Function([], output)
mod['func_6355'] = func_6355
mod = relay.transform.InferType()(mod)
mutated_mod['func_6355'] = func_6355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6355_call = mutated_mod.get_global_var('func_6355')
call_6356 = func_6355_call()
output = call_6356
func_6357 = relay.Function([], output)
mutated_mod['func_6357'] = func_6357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1109_call = mod.get_global_var('func_1109')
func_1110_call = mutated_mod.get_global_var('func_1110')
call_6372 = relay.TupleGetItem(func_1109_call(), 0)
call_6373 = relay.TupleGetItem(func_1110_call(), 0)
const_6374 = relay.const([[[1.876468,4.189457,7.513307,-1.619916,-4.767895,-3.433412,1.890907,9.641907,-9.301815,0.929415,8.383201,8.142413,0.528253,0.117639,7.703791,2.602976],[-4.009535,5.438675,-9.645420,-3.704285,-2.400872,3.916798,-8.325031,-8.767431,1.461577,7.296540,-2.727241,-0.421898,-8.219469,-6.892126,-8.315636,0.828248],[-9.735739,8.327282,-1.951647,4.908558,-2.528729,2.134636,3.605668,6.387524,0.881505,8.478933,-3.024357,3.667325,0.154165,-0.984058,2.605764,5.478960],[5.696197,9.261738,-5.788127,-5.070058,2.973899,7.725555,5.323491,8.119942,-0.153311,-0.833356,0.997410,4.651956,1.342520,-6.870676,5.570230,-3.166020]],[[-3.953857,8.022031,-3.138536,-0.917842,6.565700,-0.930465,-1.505192,4.064083,-3.060380,0.570585,3.402460,6.748936,9.837834,-9.389249,7.630676,0.985281],[-1.923161,-9.937435,-0.310547,-7.981434,-3.347782,-5.921753,-6.564029,8.676390,3.275819,-3.739993,-7.442567,-3.438389,-7.722301,-8.366586,9.926706,2.857468],[-4.458598,3.163912,-5.823766,-1.462384,-8.197738,-8.205452,-0.409145,-5.608754,-0.071341,8.557392,-8.865014,-1.007194,-8.121357,-5.221329,-0.066397,5.466236],[2.433071,7.525347,-8.787858,-6.916157,-9.069886,1.599616,9.489640,0.746125,7.295895,-7.954315,-6.072957,-1.827021,8.839901,-8.093028,-7.819018,4.313581]],[[-0.572561,-1.449324,-6.811797,-4.631996,6.761183,-6.871274,5.835050,-0.121173,-3.330768,-2.082739,-4.496280,1.048375,3.507436,7.970186,9.015048,0.906422],[-0.261263,-5.378423,-2.720558,9.915578,-7.305723,-3.410320,1.589229,-4.653011,2.458990,-7.234248,5.596077,-0.032412,-5.501417,6.367590,-6.465070,2.927616],[-9.506068,1.248264,-7.887719,-7.495149,-9.530152,-5.820515,7.538907,8.359943,6.633543,-0.391150,7.858181,3.871919,4.432734,8.430102,2.217652,-7.072431],[-6.248516,6.343049,-7.017939,-1.845316,-8.209381,7.173388,1.933605,1.254318,-8.872065,-2.463404,-7.181376,7.992109,-4.231907,6.585652,-8.346426,4.004224]],[[6.267439,7.655826,-7.047301,3.705773,6.065712,-1.948900,7.733366,6.818079,-4.617473,-0.641655,-1.397548,-1.521252,-4.259115,-1.457638,1.865382,-4.990008],[-6.403298,-7.577982,5.130934,-8.050053,-9.596030,5.673273,-5.515843,-7.596519,-8.134683,9.582036,-0.317827,1.191517,6.802727,2.330477,2.745973,6.259784],[-6.187807,-8.165362,3.105967,-5.315204,-0.936628,-6.610823,-5.742757,1.288442,8.138465,4.290407,-2.162571,-3.259248,9.334174,-0.097079,6.052304,-3.052830],[4.981341,4.681454,2.850496,2.923139,-5.676788,-4.187212,-9.722984,7.773619,-9.271011,1.531159,-1.937545,-3.932010,-7.252963,-3.111392,6.864783,8.823491]],[[-2.017378,3.974165,-6.009760,9.940844,-3.744268,5.545524,3.524572,-6.301834,-4.826266,-0.126714,-0.474820,-3.197808,9.524113,-7.912403,2.683073,9.306666],[0.831702,-8.647817,1.131099,-5.065927,6.332420,-4.062432,-2.761946,6.287573,1.527669,0.758719,-8.133338,-1.094357,6.038920,-5.531936,-5.339344,-5.934535],[4.468025,0.022382,-6.287042,-5.264218,2.217956,-0.070917,-9.966441,-4.391217,4.832547,2.625196,0.885296,1.649900,-1.553110,-1.703609,8.333213,-4.682708],[1.725247,-4.717387,7.204452,7.732115,8.140475,3.175516,6.662113,9.466914,7.803529,9.761955,-8.034260,3.450001,-5.564664,8.019329,-6.477018,-9.615215]],[[1.763607,5.341611,-7.714895,-7.855765,-9.882418,7.800136,8.503557,-5.516279,2.793247,-7.199619,-8.237652,-7.440146,8.804208,3.900082,-5.853641,1.900160],[-4.774784,-5.709422,7.671267,-3.253436,-5.853956,-7.464724,7.958693,0.642524,-0.892051,-1.029835,0.810214,5.181444,8.705238,6.992587,3.407133,4.159964],[9.942924,-4.918814,-3.796573,4.328100,-7.804981,8.690931,-0.768047,-9.806321,-8.822683,-8.109547,7.948569,-1.056798,-3.506741,-3.987090,-8.590310,3.394335],[-9.534655,-6.959933,-7.852129,7.119103,3.080286,-6.781970,3.283459,-0.701363,-8.429979,-3.836610,0.028522,-1.431905,-2.455719,9.605556,-6.486095,-5.986077]],[[-0.326468,-1.831453,-4.627352,5.699843,-6.296602,-5.725753,-7.814542,4.577424,1.782767,-3.612653,-6.233343,-4.807565,-9.525082,3.008067,-2.259132,7.557467],[-1.224154,2.512380,9.192337,5.191015,6.885484,-6.460332,-6.364550,-6.642118,2.782785,-4.704780,3.509251,-1.137254,-5.961502,-3.749778,6.082626,2.494001],[7.599575,7.830730,8.191390,-5.591847,-1.671697,-9.436225,-6.924250,-1.215926,-6.635288,6.617530,2.146062,4.556525,7.133635,-6.816532,7.630771,7.394244],[-2.370273,1.924187,9.569208,-3.052822,-8.210709,-3.372188,4.372179,-1.978809,-1.483427,1.077951,4.653396,8.852073,9.280788,-1.005942,-3.340339,6.723385]],[[-6.646608,-3.411532,9.822251,9.807411,-1.807643,-9.732687,-1.398702,5.964463,3.232106,-3.708833,9.457115,9.191168,4.575406,6.132999,9.665353,-8.701021],[9.552295,6.881283,-8.243137,9.638331,3.785798,-3.504025,-4.731369,-5.018734,5.631265,1.204481,-2.586930,4.419372,-2.602292,1.556245,8.860776,8.835738],[1.629237,2.729604,1.660062,-1.646556,9.038571,-6.081067,-2.455087,3.056306,8.196680,-4.317468,0.048299,6.040839,-4.812005,-0.426130,-8.636100,-2.142797],[-0.648488,9.671029,-6.437127,-2.376773,3.056470,-8.032052,8.139048,8.410352,-2.034759,8.442920,4.328731,5.233054,7.901824,5.672652,2.952377,5.163484]],[[-7.405922,6.396206,-2.418179,-1.355391,-0.171052,6.013751,-4.251787,-5.309384,-5.421200,-7.083357,-8.541798,1.428986,2.902408,6.403942,2.252766,2.262422],[-0.568558,-5.369052,-0.018808,-0.173336,4.094178,4.603861,-4.827236,-4.715757,2.251147,-8.542318,-2.700672,1.709092,-5.988470,-6.984039,-0.345371,0.608204],[-2.036145,4.744580,-3.500793,0.527951,-1.119918,9.402755,-0.503735,2.501494,8.757974,5.376029,-8.505893,9.208823,-9.515295,-9.361930,9.096063,9.351445],[1.437149,1.274720,-1.629977,-6.248035,9.842991,3.172055,1.148832,6.536154,-6.898772,4.563019,1.292545,6.555904,-6.528399,-4.133111,-3.614037,-3.776269]],[[4.913980,3.245827,-1.160370,-7.037625,-5.462632,-6.409781,-9.318484,-0.669841,-9.121004,4.494382,-9.718775,9.074442,-5.453428,9.645425,1.226692,5.134896],[3.454865,-2.294195,-7.264392,6.669357,-0.222607,-9.241475,3.111186,3.788961,-8.192283,1.651707,-9.554367,-5.841077,7.828577,1.480943,4.700318,4.755855],[1.706598,-3.092588,-4.980125,-0.512202,6.086942,5.573722,0.651570,2.152983,-4.382508,2.180534,5.671025,0.198342,6.860410,-4.948045,2.584967,5.746366],[1.638662,-5.263528,7.424353,7.231902,-2.177257,3.654137,4.463115,9.917269,8.984791,-0.026823,-7.095510,6.589454,-5.236863,-2.565447,6.882851,1.982907]],[[-1.907226,-7.752368,-3.808475,-2.128519,0.351703,3.865687,-3.748155,-9.720692,0.579317,0.213799,-6.469744,4.581443,-5.329132,6.512536,4.224772,-1.787339],[-9.745125,3.547368,-3.497596,0.110720,4.693852,0.247800,-3.857299,7.170993,-8.142992,4.232027,-6.296900,-6.853281,7.627435,-6.455401,-4.442427,-6.410928],[-4.783327,8.634414,5.009634,-1.544225,1.181888,7.597057,0.635915,5.780122,8.785302,-6.468036,5.306595,-8.794754,-8.701191,3.807002,9.400016,-8.322158],[2.903115,0.262894,-3.808962,2.284641,5.494534,9.318044,-6.686299,-7.299792,-9.274116,4.980692,2.601506,-1.526994,-8.987974,-8.646620,5.418697,9.212883]],[[9.263186,3.224347,-1.438350,8.430751,7.679012,-6.226028,-9.460951,6.063701,-4.347151,-2.254304,-1.354344,4.570910,5.086820,2.535143,-3.094729,2.900169],[9.597361,-4.888802,-9.943638,6.859205,-7.927557,2.099178,-2.993872,1.027607,8.245517,6.267773,-1.927790,-1.543533,-5.998783,-0.358956,3.198085,-4.367057],[3.058476,-8.573801,9.971390,6.869294,-3.078932,-4.537314,-2.496780,3.480253,5.358412,3.991398,9.695107,8.800765,0.600845,9.345895,-0.405001,0.687840],[-0.191336,4.669274,0.921013,1.900611,5.614510,3.197493,-3.938282,1.407716,8.957415,4.141155,-6.041889,-0.590307,7.361914,-1.273678,-0.281612,2.402853]],[[-2.754394,-7.323269,4.394541,8.112506,2.130643,-9.258793,3.145431,9.986041,5.949404,7.842827,-3.411570,2.226444,1.256122,7.141069,-9.123123,-2.402165],[2.472808,-2.273308,4.381289,4.226393,-2.478255,-0.584188,5.471928,-2.301564,-9.408507,-7.999320,-9.005010,-5.490607,-5.666056,5.518385,-9.180953,6.677416],[-6.781113,0.952559,4.058785,-9.415954,-5.175784,8.762197,-2.378772,-4.591639,9.231554,5.456772,5.247203,-3.905655,7.218787,-1.725712,6.949630,1.192793],[8.405825,3.335874,2.228927,1.343157,-3.561136,7.910390,-1.970609,-1.044020,6.167581,1.085110,4.433706,-5.699693,4.086825,4.555325,-2.630116,-2.168696]],[[7.661012,-2.167166,5.796366,-7.967527,-5.419866,5.906780,-5.849905,-1.007856,6.332458,-7.676512,2.141696,-5.415376,5.705498,-6.551310,-5.594592,6.497427],[-0.789547,7.334642,2.219184,-8.001030,7.755937,2.236558,3.336628,4.998039,6.051620,3.158632,-4.830983,-5.211747,5.089755,9.046556,9.776119,0.855676],[-5.256770,-1.971878,7.373125,1.097747,-2.546816,-9.967457,0.799641,-4.533727,5.014534,7.417963,9.350379,0.132646,-2.175486,3.442546,6.464917,-7.916351],[8.093287,-5.606593,3.113508,2.440307,-4.777402,4.123331,-7.728182,-4.093497,1.505453,9.275561,3.231200,-9.143037,-7.891153,-6.661615,-5.402018,5.919010]],[[1.080411,-0.245556,-3.657125,-6.526973,9.511626,-7.624865,2.771422,9.995117,-4.783706,-5.237054,9.461595,-6.049087,-4.854466,-8.654355,7.380819,-6.167487],[4.781887,3.670205,-5.641445,-8.305997,3.123756,1.417497,4.451427,8.374041,-8.007521,-1.654111,-6.854587,6.968415,0.257226,-0.787243,9.277114,0.345929],[8.557791,-0.815300,-8.446547,-5.741273,7.674313,-4.882046,-8.728805,3.619144,7.233869,3.320636,-3.653273,-7.835171,-7.033806,-2.229969,1.062739,-8.435607],[-0.949066,4.768398,3.042587,-1.938698,4.304364,2.688153,-8.135680,-9.515993,-4.702224,-9.950656,-3.826034,-6.253858,0.963865,1.936808,-5.958307,6.154345]]], dtype = "float64")#candidate|6374|(15, 4, 16)|const|float64
bop_6375 = relay.less_equal(call_6372.astype('bool'), const_6374.astype('bool')) # shape=(15, 4, 16)
bop_6378 = relay.less_equal(call_6373.astype('bool'), const_6374.astype('bool')) # shape=(15, 4, 16)
func_1235_call = mod.get_global_var('func_1235')
func_1238_call = mutated_mod.get_global_var('func_1238')
call_6391 = relay.TupleGetItem(func_1235_call(relay.reshape(call_6372.astype('float64'), [15, 1, 16])), 1)
call_6392 = relay.TupleGetItem(func_1238_call(relay.reshape(call_6372.astype('float64'), [15, 1, 16])), 1)
func_4951_call = mod.get_global_var('func_4951')
func_4952_call = mutated_mod.get_global_var('func_4952')
call_6397 = relay.TupleGetItem(func_4951_call(), 0)
call_6398 = relay.TupleGetItem(func_4952_call(), 0)
func_6227_call = mod.get_global_var('func_6227')
func_6229_call = mutated_mod.get_global_var('func_6229')
call_6413 = relay.TupleGetItem(func_6227_call(), 0)
call_6414 = relay.TupleGetItem(func_6229_call(), 0)
uop_6418 = relay.erf(const_6374.astype('float64')) # shape=(15, 4, 16)
output = relay.Tuple([bop_6375,call_6391,call_6397,call_6413,uop_6418,])
output2 = relay.Tuple([bop_6378,call_6392,call_6398,call_6414,uop_6418,])
func_6424 = relay.Function([], output)
mod['func_6424'] = func_6424
mod = relay.transform.InferType()(mod)
mutated_mod['func_6424'] = func_6424
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6424_call = mutated_mod.get_global_var('func_6424')
call_6425 = func_6424_call()
output = call_6425
func_6426 = relay.Function([], output)
mutated_mod['func_6426'] = func_6426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4604_call = mod.get_global_var('func_4604')
func_4606_call = mutated_mod.get_global_var('func_4606')
call_6432 = func_4604_call()
call_6433 = func_4604_call()
var_6446 = relay.var("var_6446", dtype = "float64", shape = (15, 6, 16))#candidate|6446|(15, 6, 16)|var|float64
bop_6447 = relay.left_shift(call_6432.astype('int16'), var_6446.astype('int16')) # shape=(15, 6, 16)
bop_6450 = relay.left_shift(call_6433.astype('int16'), var_6446.astype('int16')) # shape=(15, 6, 16)
func_4951_call = mod.get_global_var('func_4951')
func_4952_call = mutated_mod.get_global_var('func_4952')
call_6452 = relay.TupleGetItem(func_4951_call(), 0)
call_6453 = relay.TupleGetItem(func_4952_call(), 0)
func_3496_call = mod.get_global_var('func_3496')
func_3498_call = mutated_mod.get_global_var('func_3498')
call_6456 = func_3496_call()
call_6457 = func_3496_call()
output = relay.Tuple([bop_6447,call_6452,call_6456,])
output2 = relay.Tuple([bop_6450,call_6453,call_6457,])
func_6458 = relay.Function([var_6446,], output)
mod['func_6458'] = func_6458
mod = relay.transform.InferType()(mod)
var_6459 = relay.var("var_6459", dtype = "float64", shape = (15, 6, 16))#candidate|6459|(15, 6, 16)|var|float64
output = func_6458(var_6459)
func_6460 = relay.Function([var_6459], output)
mutated_mod['func_6460'] = func_6460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5745_call = mod.get_global_var('func_5745')
func_5747_call = mutated_mod.get_global_var('func_5747')
call_6467 = relay.TupleGetItem(func_5745_call(), 0)
call_6468 = relay.TupleGetItem(func_5747_call(), 0)
output = call_6467
output2 = call_6468
func_6486 = relay.Function([], output)
mod['func_6486'] = func_6486
mod = relay.transform.InferType()(mod)
mutated_mod['func_6486'] = func_6486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6486_call = mutated_mod.get_global_var('func_6486')
call_6487 = func_6486_call()
output = call_6487
func_6488 = relay.Function([], output)
mutated_mod['func_6488'] = func_6488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6229_call = mutated_mod.get_global_var('func_6229')
call_6534 = relay.TupleGetItem(func_6227_call(), 0)
call_6535 = relay.TupleGetItem(func_6229_call(), 0)
output = relay.Tuple([call_6534,])
output2 = relay.Tuple([call_6535,])
func_6546 = relay.Function([], output)
mod['func_6546'] = func_6546
mod = relay.transform.InferType()(mod)
output = func_6546()
func_6547 = relay.Function([], output)
mutated_mod['func_6547'] = func_6547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5858_call = mod.get_global_var('func_5858')
func_5859_call = mutated_mod.get_global_var('func_5859')
call_6600 = relay.TupleGetItem(func_5858_call(), 0)
call_6601 = relay.TupleGetItem(func_5859_call(), 0)
func_3105_call = mod.get_global_var('func_3105')
func_3108_call = mutated_mod.get_global_var('func_3108')
const_6605 = relay.const([[0.366184,-5.830164,-9.580960,-4.834438,2.797719,1.023661],[2.485716,4.483767,-1.562968,0.816116,-5.266726,-9.630874],[7.297296,-4.031977,0.115258,0.150774,-8.833231,9.304134],[-5.259064,-5.372426,-0.722624,-8.760842,8.183552,-2.677558],[-4.925173,-2.484409,-8.707055,-8.092182,7.455240,7.670347],[-2.537251,9.943177,8.028945,9.179925,6.589688,1.199844],[-5.579003,2.257151,7.197861,9.506574,-5.286044,-3.889465],[-4.688983,-1.585355,6.589428,-7.397570,5.495452,-7.763206],[8.417903,-0.182661,-7.005940,-9.467075,5.919350,-1.818387],[-7.753269,-4.355788,6.065365,8.502674,9.761502,6.370982],[-2.807864,7.856871,-6.625864,-9.820978,3.489611,-9.271628],[-0.379297,-5.391917,-4.313031,-4.196386,2.743014,0.246818],[9.121944,-9.302676,9.722069,-5.010778,-4.810210,8.722932],[0.134271,-6.672642,-1.903284,-5.618876,1.853713,-4.162431],[7.283895,-4.207427,4.558535,-4.157822,5.276220,-4.140550],[-5.997349,-1.994263,-6.337990,4.067202,7.445774,-2.004949]], dtype = "float32")#candidate|6605|(16, 6)|const|float32
call_6604 = func_3105_call(relay.reshape(const_6605.astype('float32'), [12, 1, 8]))
call_6606 = func_3105_call(relay.reshape(const_6605.astype('float32'), [12, 1, 8]))
output = relay.Tuple([call_6600,call_6604,const_6605,])
output2 = relay.Tuple([call_6601,call_6606,const_6605,])
func_6621 = relay.Function([], output)
mod['func_6621'] = func_6621
mod = relay.transform.InferType()(mod)
mutated_mod['func_6621'] = func_6621
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6621_call = mutated_mod.get_global_var('func_6621')
call_6622 = func_6621_call()
output = call_6622
func_6623 = relay.Function([], output)
mutated_mod['func_6623'] = func_6623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5514_call = mutated_mod.get_global_var('func_5514')
call_6629 = relay.TupleGetItem(func_5512_call(), 1)
call_6630 = relay.TupleGetItem(func_5514_call(), 1)
func_2788_call = mod.get_global_var('func_2788')
func_2789_call = mutated_mod.get_global_var('func_2789')
call_6635 = relay.TupleGetItem(func_2788_call(), 0)
call_6636 = relay.TupleGetItem(func_2789_call(), 0)
func_1683_call = mod.get_global_var('func_1683')
func_1684_call = mutated_mod.get_global_var('func_1684')
call_6656 = relay.TupleGetItem(func_1683_call(), 1)
call_6657 = relay.TupleGetItem(func_1684_call(), 1)
output = relay.Tuple([call_6629,call_6635,call_6656,])
output2 = relay.Tuple([call_6630,call_6636,call_6657,])
func_6660 = relay.Function([], output)
mod['func_6660'] = func_6660
mod = relay.transform.InferType()(mod)
mutated_mod['func_6660'] = func_6660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6660_call = mutated_mod.get_global_var('func_6660')
call_6661 = func_6660_call()
output = call_6661
func_6662 = relay.Function([], output)
mutated_mod['func_6662'] = func_6662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_6668 = relay.TupleGetItem(func_1561_call(), 0)
call_6669 = relay.TupleGetItem(func_1563_call(), 0)
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_6672 = relay.TupleGetItem(func_3366_call(), 0)
call_6673 = relay.TupleGetItem(func_3368_call(), 0)
output = relay.Tuple([call_6668,call_6672,])
output2 = relay.Tuple([call_6669,call_6673,])
func_6674 = relay.Function([], output)
mod['func_6674'] = func_6674
mod = relay.transform.InferType()(mod)
mutated_mod['func_6674'] = func_6674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6674_call = mutated_mod.get_global_var('func_6674')
call_6675 = func_6674_call()
output = call_6675
func_6676 = relay.Function([], output)
mutated_mod['func_6676'] = func_6676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_6679 = relay.TupleGetItem(func_2765_call(), 0)
call_6680 = relay.TupleGetItem(func_2766_call(), 0)
output = relay.Tuple([call_6679,])
output2 = relay.Tuple([call_6680,])
func_6695 = relay.Function([], output)
mod['func_6695'] = func_6695
mod = relay.transform.InferType()(mod)
mutated_mod['func_6695'] = func_6695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6695_call = mutated_mod.get_global_var('func_6695')
call_6696 = func_6695_call()
output = call_6696
func_6697 = relay.Function([], output)
mutated_mod['func_6697'] = func_6697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
call_6741 = relay.TupleGetItem(func_1707_call(), 1)
call_6742 = relay.TupleGetItem(func_1709_call(), 1)
func_5583_call = mod.get_global_var('func_5583')
func_5586_call = mutated_mod.get_global_var('func_5586')
var_6747 = relay.var("var_6747", dtype = "float64", shape = (1, 700))#candidate|6747|(1, 700)|var|float64
call_6746 = relay.TupleGetItem(func_5583_call(relay.reshape(var_6747.astype('float64'), [14, 5, 10])), 2)
call_6748 = relay.TupleGetItem(func_5586_call(relay.reshape(var_6747.astype('float64'), [14, 5, 10])), 2)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_6753 = relay.TupleGetItem(func_2765_call(), 0)
call_6754 = relay.TupleGetItem(func_2766_call(), 0)
output = relay.Tuple([call_6741,call_6746,var_6747,call_6753,])
output2 = relay.Tuple([call_6742,call_6748,var_6747,call_6754,])
func_6764 = relay.Function([var_6747,], output)
mod['func_6764'] = func_6764
mod = relay.transform.InferType()(mod)
var_6765 = relay.var("var_6765", dtype = "float64", shape = (1, 700))#candidate|6765|(1, 700)|var|float64
output = func_6764(var_6765)
func_6766 = relay.Function([var_6765], output)
mutated_mod['func_6766'] = func_6766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5538_call = mod.get_global_var('func_5538')
func_5540_call = mutated_mod.get_global_var('func_5540')
call_6811 = relay.TupleGetItem(func_5538_call(), 1)
call_6812 = relay.TupleGetItem(func_5540_call(), 1)
func_1159_call = mod.get_global_var('func_1159')
func_1160_call = mutated_mod.get_global_var('func_1160')
call_6825 = relay.TupleGetItem(func_1159_call(), 1)
call_6826 = relay.TupleGetItem(func_1160_call(), 1)
output = relay.Tuple([call_6811,call_6825,])
output2 = relay.Tuple([call_6812,call_6826,])
func_6836 = relay.Function([], output)
mod['func_6836'] = func_6836
mod = relay.transform.InferType()(mod)
output = func_6836()
func_6837 = relay.Function([], output)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_6840 = func_1470_call()
call_6841 = func_1470_call()
output = call_6840
output2 = call_6841
func_6845 = relay.Function([], output)
mod['func_6845'] = func_6845
mod = relay.transform.InferType()(mod)
output = func_6845()
func_6846 = relay.Function([], output)
mutated_mod['func_6846'] = func_6846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4708_call = mod.get_global_var('func_4708')
func_4709_call = mutated_mod.get_global_var('func_4709')
call_6887 = relay.TupleGetItem(func_4708_call(), 0)
call_6888 = relay.TupleGetItem(func_4709_call(), 0)
var_6891 = relay.var("var_6891", dtype = "float64", shape = (3, 6, 16))#candidate|6891|(3, 6, 16)|var|float64
bop_6892 = relay.divide(call_6887.astype('float64'), relay.reshape(var_6891.astype('float64'), relay.shape_of(call_6887))) # shape=(3, 6, 16)
bop_6895 = relay.divide(call_6888.astype('float64'), relay.reshape(var_6891.astype('float64'), relay.shape_of(call_6888))) # shape=(3, 6, 16)
output = relay.Tuple([bop_6892,])
output2 = relay.Tuple([bop_6895,])
func_6933 = relay.Function([var_6891,], output)
mod['func_6933'] = func_6933
mod = relay.transform.InferType()(mod)
mutated_mod['func_6933'] = func_6933
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6934 = relay.var("var_6934", dtype = "float64", shape = (3, 6, 16))#candidate|6934|(3, 6, 16)|var|float64
func_6933_call = mutated_mod.get_global_var('func_6933')
call_6935 = func_6933_call(var_6934)
output = call_6935
func_6936 = relay.Function([var_6934], output)
mutated_mod['func_6936'] = func_6936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_6988 = relay.TupleGetItem(func_4107_call(), 0)
call_6989 = relay.TupleGetItem(func_4108_call(), 0)
output = call_6988
output2 = call_6989
func_6998 = relay.Function([], output)
mod['func_6998'] = func_6998
mod = relay.transform.InferType()(mod)
output = func_6998()
func_6999 = relay.Function([], output)
mutated_mod['func_6999'] = func_6999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mod.get_global_var('func_4783')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_7009 = relay.TupleGetItem(func_4783_call(), 0)
call_7010 = relay.TupleGetItem(func_4785_call(), 0)
output = relay.Tuple([call_7009,])
output2 = relay.Tuple([call_7010,])
func_7017 = relay.Function([], output)
mod['func_7017'] = func_7017
mod = relay.transform.InferType()(mod)
output = func_7017()
func_7018 = relay.Function([], output)
mutated_mod['func_7018'] = func_7018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
call_7027 = relay.TupleGetItem(func_1650_call(), 1)
call_7028 = relay.TupleGetItem(func_1652_call(), 1)
var_7029 = relay.var("var_7029", dtype = "float64", shape = (15, 10, 16))#candidate|7029|(15, 10, 16)|var|float64
bop_7030 = relay.divide(call_7027.astype('float64'), var_7029.astype('float64')) # shape=(15, 10, 16)
bop_7033 = relay.divide(call_7028.astype('float64'), var_7029.astype('float64')) # shape=(15, 10, 16)
uop_7038 = relay.exp(bop_7030.astype('float32')) # shape=(15, 10, 16)
uop_7040 = relay.exp(bop_7033.astype('float32')) # shape=(15, 10, 16)
output = uop_7038
output2 = uop_7040
func_7050 = relay.Function([var_7029,], output)
mod['func_7050'] = func_7050
mod = relay.transform.InferType()(mod)
mutated_mod['func_7050'] = func_7050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7051 = relay.var("var_7051", dtype = "float64", shape = (15, 10, 16))#candidate|7051|(15, 10, 16)|var|float64
func_7050_call = mutated_mod.get_global_var('func_7050')
call_7052 = func_7050_call(var_7051)
output = call_7052
func_7053 = relay.Function([var_7051], output)
mutated_mod['func_7053'] = func_7053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3959_call = mod.get_global_var('func_3959')
func_3961_call = mutated_mod.get_global_var('func_3961')
call_7055 = func_3959_call()
call_7056 = func_3959_call()
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
call_7094 = relay.TupleGetItem(func_1650_call(), 0)
call_7095 = relay.TupleGetItem(func_1652_call(), 0)
func_4805_call = mod.get_global_var('func_4805')
func_4807_call = mutated_mod.get_global_var('func_4807')
const_7101 = relay.const([3.376444,8.217018,7.325830,0.522596,-6.756382,3.811664,-0.034646,2.274521,4.641540,-7.920966,-5.051251,0.372363,7.074759,-5.779631,0.160893,-0.090811,-8.195015,3.091913,-6.746147,-5.524608,1.325239,-9.950473,3.599549,1.464536,-0.220929,9.585170,8.359415,-9.016126,6.005446,5.882594,-2.754118,-4.686802,3.574744,8.633446,-0.561960,7.612127,6.361487,8.300749,7.063489,3.862158,9.943542,-0.608158,-8.218023,8.550665,4.890617,-1.800797,-8.256439,-0.283779,-5.625853,9.683177,1.128257,-5.867873,-1.258616,-1.084831,-8.256033,-8.540486,-4.906707,-7.447410,7.614320,-0.353887,0.820330,-6.400292,2.586280,0.873841,-2.175204,8.982868,6.671674,-7.276538,4.289441,4.350966,7.481960,3.821506,-5.723599,-2.256139,0.063909,-1.059993,9.199502,-4.618490,-1.671077,-7.167281,-8.156521,-0.335188,-6.655041,-7.820187,2.831390,2.505011,3.467387,-7.686883,1.452269,6.765131,-2.485179,5.923711,-7.864687,-1.025083,9.426663,-3.158273,-8.768467,-4.215766,5.994750,0.407504,-0.374047,5.595329,1.562241,-3.074747,-5.047072,-8.598333,1.620463,-7.663287,3.591767,-7.927938,-7.165320,1.715610,-2.978421,3.532732,-2.658675,-7.705491,7.132928,-9.797986,-9.287836,0.916234,-6.636288,3.063288,5.615854,3.859640,-3.218376,-0.198365,-6.326185,-1.955547,7.289332,2.111910,-8.448767,-8.942603,5.220436,-5.450416,2.588957,4.608652,1.605609,-7.142313,-6.058550,-4.828236,5.939736,1.481154,-5.854945,-7.154249,8.200371,8.299620,-4.246396,-9.920693,-8.894385,3.616387,-9.166974,0.424215,1.545523,2.305827,4.635190,-9.316695,-1.868764,6.637730,8.399857,-2.068529,6.594787,-7.721089,0.908516,0.213826,-2.621999,-6.070217,5.730432,-3.237231,2.056218,2.441737,9.243081,8.228382,6.947623,-9.870895,2.068230,-0.010436,-3.811314,-2.553169,4.686712,6.206674,-1.310902,-6.453619,5.256866,-3.006253,-3.896037,-1.207924,6.549541,6.255473,-3.479763,-7.926866,-6.464175,-9.483291,4.926428,6.565444,-2.031760,-9.868235,-1.897049,0.102747,-3.274487,-3.317864,9.054495,-1.242919,-7.215892,2.230193,-2.663503,-9.290417,-1.547677,7.626478,2.665039,-4.214332,-0.413854,-3.660570,-3.015726,-0.803937,9.661855,5.587463,6.248517,-3.393777,-9.604596,-4.101879,7.831719,9.010658,4.100363,7.946397,1.964293,1.626973,4.327663,-4.693621,2.724204,-7.941240,9.974565,0.344798,4.915791,1.780392,7.498925,-2.252894,-8.940548,4.131066,5.755182,7.038399,-6.561083,-0.704591,-0.738550,0.014703,6.480579,8.424878,-7.723913,-5.325591,-4.623233,1.511982,2.496463,-3.275441,2.904649,-9.996746,-0.536217,-0.995444,-2.219929,-8.181468,4.373806,-2.441865,5.577363,-1.787862,-6.448271,-9.560674,-7.358016,-5.281740,6.982899,9.594299,-4.879525,6.722126,9.024857,-4.333355,-5.822680,1.928992,-7.111609,0.774885,7.021779,7.620700,-6.874881,-2.419363,6.377529,-4.145187,3.441407,-3.639809,2.059537,-6.437352,5.307857,-5.064584,-2.246290,1.172897,0.093221,-0.482543,-2.572442,-0.246117,2.610027,6.085462,-6.838821,-8.071743,-6.191134,0.804927,-6.423991,-8.011182,-4.332729,-3.831576,-4.718597,-4.577454,-8.857510,-9.768484,-2.920817,9.931787,4.611462,6.297328,-5.577257,4.382118,-4.302200,3.472533,4.532599,-6.632468,-3.944144,-3.518347,-7.895545,4.683878,1.400836,-6.984284,-8.300278,-7.562300,-2.742649,0.725414,3.981427,8.085335,-3.653914,-7.311032,6.870238,8.637732,0.525953,-6.241481,-1.814483,-7.719330,-3.992914,-6.019767,-5.654316,-1.685355,-5.376479,-1.925312,1.981373,2.213471,-0.230867,4.782448,-5.020187,3.997298,-1.726767,1.781648,0.167070,-5.221964,-9.658122,9.690536,5.226634,-6.273933,1.792237,7.605853,-4.092083,-8.219567,1.937624,-9.659825,7.100964,7.033128,-7.978467,-6.620661,0.324692,6.706570,6.319319,-6.718293,-0.001397,-4.213474,0.503045,-0.241042,-6.421341,-2.312164,-7.620321,2.548933,4.694433,2.425931,-0.330598,3.813352,0.645460,8.971099,7.495079,6.591611,-9.429610,-7.635978,-9.733424,-8.382588,1.087945,-3.061250,0.781905,4.522684,-6.572623,-3.535662,3.552032,-9.786955,-3.920723,5.737517,-3.331995,-7.872115,8.906643,-8.814688,5.868471,-3.392245,-9.378782,9.285781,6.852075,-1.225209,3.526226,-3.673971,-4.037361,5.172906,-8.332400,2.441179,-0.169878,-0.141242,-9.718948,6.848564,1.413913,-0.916106,-2.741860,9.965966,2.573989,3.121830,1.708781,8.477205,6.855355,-1.808840,0.284862,-7.915563,9.833380,0.139377,6.994176,-2.079628,0.362347,-4.615909,-8.158703,4.583953,2.886402,-1.685948,-9.756362,7.018388,7.884969,6.536934,9.183964,-3.414817,-2.289441,-5.182670,-6.314007,-3.938369,1.072671,6.760514,2.845041,4.886030,5.233351,0.676635,1.253622,3.854105,-0.948173,-4.013039,-8.992715,6.997571,-8.417440,4.022344,-5.317052,-6.025773,-8.858699,1.207918,-0.783713,5.354312,-4.346072,2.347582,1.027844,-2.855296,-3.152401,2.639631,2.064297,1.757933,-7.099566,-9.665495,4.469285,-0.052607,-9.469715,9.586080,0.210882,9.094674,2.086666,7.051039,3.587603,-3.631376,-6.433448,8.041291,-6.101687,-6.792379,7.665162,3.775923,3.282037,-0.757322,1.384932,5.016964,-0.423890,2.741293,8.736685,-2.924641,-3.376686,-7.986392,-9.346126,5.124336,9.687245,4.001348,-3.837409,7.229867,1.525785,-5.089842,5.456245,4.419946,-7.212218,7.711878,7.875131,-9.842497,-9.614578,7.853487,-5.596587,-9.308948,-4.125661,-5.520042,-2.212532,-6.441974,-6.010677,8.255765,-7.470573,6.733073,9.721386,5.665166,4.986788,-1.988413,-8.750289,-1.050982,-0.954370,-1.734821,0.026099,-8.749668,-4.519769,6.308053,8.977216,-0.136073,4.689006,-1.315111,-3.248344,7.543296,7.580134,-8.848666,0.892218,3.554083,9.518395,-6.253015,-5.899456,-4.423856,-9.906795,9.915484,-1.908042,6.577712,-1.781223,-0.935478,0.467463,-8.726412,-5.174343,4.961305,0.627156,2.067192,-7.676380,0.728533,-9.670399,-6.901451,1.513228,-8.355167,9.001139,4.802438,4.613648,0.872388,-7.401256,-6.652116,-2.837418,-5.671284,-7.781830,-0.164425,-9.303595,6.502664,4.768983,8.399180,-2.548702,2.369694,7.609135,7.616094,-4.620841,-8.885599,-1.613678,6.964228,-9.007176,-1.989819,-6.785269,5.253950,5.217818,8.472038,-8.533223,8.011174,5.138648,3.322573,-3.538460,3.909461,6.710412,4.254946,-2.841762,-3.488772,-6.441947,7.138305,6.238964,6.980095,-7.050128,8.494819,3.991028,0.514969,1.086179,-8.373936,3.123841,7.029553,2.997194,-0.989580,9.141313,-1.179301,5.543095,-9.421667,-2.213117,9.455171,9.741067,-6.132564,-2.906106,2.000150,-6.195679,3.648089,9.842784,-0.875445,2.397017,9.910005,2.151909,-5.331138,8.658516,6.982849,8.891336,-7.011285,0.870543,1.084302,-5.450595,-2.791596,-1.200277,-3.077678,-2.254752,-4.592724,9.220206,-4.316215,7.487636,-8.387990,-4.178010,5.889901,-0.459599,-6.955316,-5.484130,8.534290,-3.144989,1.843621,8.591314,-3.255267,-9.282927,3.821066,-6.587562,-0.782795,4.859875,5.996169,-7.452961,7.214471,-3.558898,-5.197888,5.443725,-1.583631,4.372925,6.004397,8.283848,-3.403154,-5.661631,-4.063437,-3.675909,3.365846,6.240113,6.931932,7.699214,-6.389862,-9.604368,-8.960857,5.366708,9.304933,-9.585758,6.886210,-8.177661,0.449808,-7.291913,-5.286423,-7.219213,-6.953355,-7.325736,7.114095,-7.118244,5.993523,-0.019996,-7.861298,-0.860251,6.552082,-2.955848,0.976431,-1.276567,-4.047119,-7.888296,5.596364,-7.950376,-4.253253], dtype = "float64")#candidate|7101|(728,)|const|float64
call_7100 = relay.TupleGetItem(func_4805_call(relay.reshape(const_7101.astype('float64'), [728,])), 0)
call_7102 = relay.TupleGetItem(func_4807_call(relay.reshape(const_7101.astype('float64'), [728,])), 0)
output = relay.Tuple([call_7055,call_7094,call_7100,const_7101,])
output2 = relay.Tuple([call_7056,call_7095,call_7102,const_7101,])
func_7106 = relay.Function([], output)
mod['func_7106'] = func_7106
mod = relay.transform.InferType()(mod)
output = func_7106()
func_7107 = relay.Function([], output)
mutated_mod['func_7107'] = func_7107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2593_call = mod.get_global_var('func_2593')
func_2594_call = mutated_mod.get_global_var('func_2594')
call_7122 = relay.TupleGetItem(func_2593_call(), 1)
call_7123 = relay.TupleGetItem(func_2594_call(), 1)
func_3047_call = mod.get_global_var('func_3047')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_7124 = func_3047_call()
call_7125 = func_3047_call()
func_1470_call = mod.get_global_var('func_1470')
func_1471_call = mutated_mod.get_global_var('func_1471')
call_7137 = func_1470_call()
call_7138 = func_1470_call()
output = relay.Tuple([call_7122,call_7124,call_7137,])
output2 = relay.Tuple([call_7123,call_7125,call_7138,])
func_7156 = relay.Function([], output)
mod['func_7156'] = func_7156
mod = relay.transform.InferType()(mod)
mutated_mod['func_7156'] = func_7156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7156_call = mutated_mod.get_global_var('func_7156')
call_7157 = func_7156_call()
output = call_7157
func_7158 = relay.Function([], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_7171 = func_1417_call()
call_7172 = func_1417_call()
const_7202 = relay.const([[[-6.005103,8.034991,-8.001864,-2.070114,8.118286,1.827856,-7.998315,6.033139,4.716693,9.729301,9.769399,-9.084394,-2.385985,-5.100853,9.579003,-0.489688],[2.987417,-4.357052,-0.868286,-8.692723,3.348660,-9.472994,6.694011,-5.753122,0.179594,-4.027045,-4.080026,9.225305,2.188858,-8.270722,6.076933,-7.024558],[-2.600018,2.348203,4.436999,-0.836922,6.900441,5.095791,3.027609,5.632024,7.918412,3.493057,-3.120757,-0.781744,-4.673214,-9.951597,-3.733169,-5.739741],[-1.272588,6.669894,0.105126,-7.297057,-4.149214,-6.447051,5.244029,2.030902,9.049056,-2.272974,1.544538,-7.192087,9.204959,8.545304,3.000820,4.155161],[9.454612,-8.109221,-1.045567,8.874304,-9.646298,-9.178161,2.562188,-4.382841,-9.958750,-9.957304,3.526065,4.293977,-3.831055,-6.193371,1.368756,3.369063],[5.928703,9.687826,-2.025330,-4.400332,-8.741202,5.869117,-0.082614,2.520070,-3.473960,-7.454829,-4.122230,7.444595,9.408154,-9.392793,7.814686,9.136005],[5.223540,-2.314788,-9.707334,-2.423179,-7.426048,-7.783948,5.007193,6.371558,-2.034185,-3.953186,-9.394972,9.830428,4.797174,-7.490296,5.245898,2.058409],[-8.130402,-3.738690,8.627516,-2.404359,-3.554908,-3.752097,-5.523509,-7.813710,-1.679799,2.996378,-2.278324,-6.253759,-5.960135,-1.547366,-6.726715,9.197634],[0.480255,7.015233,-3.525195,-2.842089,6.217521,2.169708,7.955481,-4.881518,-3.554925,-0.026610,-5.974320,-1.579471,3.192250,-0.992914,9.800776,-0.438888],[3.185128,5.442840,0.191869,2.479762,-5.575174,-0.080897,-7.148322,5.547022,-2.684845,7.079168,-9.252764,-1.891338,-1.721155,-4.250833,-4.187853,-6.482337],[-3.147483,3.819953,-3.564371,-3.896936,6.163132,-3.094233,0.859477,-3.817862,3.383527,-8.317481,-9.589638,5.113416,2.931991,-7.673475,-0.263746,-3.288640],[-5.695955,4.839650,-8.441387,4.767084,-7.089042,7.549406,-7.518825,-0.139507,6.776695,1.892683,5.920932,-4.646213,-9.782620,-1.274359,9.926036,-1.630020],[-5.354868,-6.137737,0.663825,0.872560,1.138761,-4.164991,-3.597395,0.637602,9.269560,2.680908,1.329982,-1.147085,-3.600454,6.676669,8.389091,7.408698],[1.026119,-1.314113,-0.042388,-7.302848,-3.962713,2.678011,5.365959,-5.446778,9.327277,4.645304,6.192970,7.941818,-5.683632,8.708219,-0.753690,-5.310798],[9.834328,-5.001587,-3.804178,9.237584,7.201627,7.967341,-4.161303,-0.175213,-5.156708,-9.977953,4.144726,3.001054,-6.613907,4.176339,-9.325596,-1.396651]],[[-4.708704,6.242332,-4.860240,3.472815,3.448251,-2.905390,-8.098252,1.975306,9.027908,-2.629199,1.305010,-3.617292,-9.857348,-8.369886,7.338116,-5.351265],[-1.304818,-7.214562,2.057612,-2.927868,9.347090,-2.947713,1.701413,-7.765497,7.399683,5.984606,-3.377892,8.709365,8.765035,5.701087,-7.680154,-1.885211],[8.753921,0.737030,-9.301838,8.315867,7.448578,3.701855,-4.901917,2.474825,-6.016454,-8.766132,-7.125778,-2.911407,-0.020559,0.369461,1.250823,8.478157],[-8.460000,4.814695,-7.385711,-9.920996,-1.447436,9.077375,2.080059,0.842159,3.411497,3.058249,9.296835,-3.365474,4.123297,-5.918052,3.626692,-1.444136],[2.802360,1.468803,-9.115392,2.240726,3.543913,0.941876,4.347900,5.981798,7.998994,-8.059034,-3.424889,-7.042410,-1.225644,-1.100263,-9.662017,-8.406255],[3.357862,4.853392,4.689836,-3.849584,0.597729,-3.318254,-8.916858,-9.805338,-4.174359,-8.042765,9.428071,-8.701888,-4.691848,1.958470,5.542385,-6.708937],[3.792883,2.711654,-1.380927,-2.833565,4.180535,-2.332922,-5.299993,2.883869,4.240146,9.868084,-4.548960,6.336966,-2.559631,9.371392,-3.565546,-1.981749],[-2.398714,-1.554742,-5.718357,-6.756563,2.570583,9.331435,8.691411,-4.597150,1.587568,4.380526,-1.644705,-3.939791,-5.298543,-7.896901,2.845274,-3.826618],[-3.797442,-0.586179,2.831087,9.740843,4.782491,-7.184697,4.393029,3.308314,-4.256485,1.318877,0.638206,-0.119393,7.524309,-6.936430,0.864107,-0.139762],[-8.204899,-0.958677,-3.677530,-2.182761,2.980606,-9.365762,-9.202266,5.315711,3.637194,4.324414,-8.359211,-9.197661,-8.170702,-9.640017,6.860627,-0.810339],[7.045559,-9.829501,-8.725625,7.438798,3.573366,-8.582411,5.937393,8.497818,-3.634081,-0.568763,-7.368090,5.925900,4.895051,-2.934498,-3.872675,-1.184615],[-4.986748,6.959124,-0.099101,-6.790339,9.980069,9.452794,-9.699911,2.184852,3.162040,6.491647,-7.690273,-4.511513,-7.964231,-2.093929,2.323759,-4.235701],[7.771525,-1.185357,-1.078612,-7.851957,-8.641715,-7.402897,-5.378069,2.136454,9.613556,5.624436,2.925397,-5.517297,-1.360372,0.259701,2.456511,1.920413],[2.166533,-9.444382,-6.495968,3.370874,-9.919025,8.331624,4.515835,-0.014313,0.820745,-1.953463,-8.337443,-7.162167,-2.545260,-7.134125,6.353476,-6.782724],[-0.488094,-8.424193,0.689359,4.903015,-8.363877,-4.711706,3.703567,-0.510482,-3.074144,-1.441072,0.589492,-4.362276,-7.101751,-2.587409,-7.107235,-9.541938]],[[0.237333,-5.531454,8.318243,7.128039,-1.714569,1.083426,-8.634518,9.993855,9.305783,5.481639,-4.260586,-6.197154,9.925203,1.789380,7.955114,-7.683892],[-1.041228,-5.064579,-9.867066,4.257587,8.345589,-7.701544,9.433579,8.203784,4.223986,6.007626,-4.814840,-0.664530,-7.884752,5.428910,-4.028076,9.220049],[-3.318220,-8.514882,6.089057,-9.146344,-2.614493,-6.171018,-9.793105,-0.122587,9.845703,2.584094,7.170795,8.676057,1.737064,-5.008108,-4.945032,9.872811],[3.500046,1.647706,9.624728,5.173846,-0.891687,5.294302,8.861215,0.107307,-6.353941,-5.941891,-7.492829,3.724342,0.806996,2.753113,4.857108,-8.026086],[-7.511410,1.187173,2.849297,-4.218694,6.108453,-8.997202,0.787242,4.856880,5.890992,-9.692612,0.465156,4.952830,7.301080,-6.381787,3.947695,9.476833],[-7.085813,-1.110832,9.917717,2.653433,-6.527443,-4.535365,9.924202,7.446044,9.081909,7.239037,-5.977673,9.396961,2.203364,-7.988566,5.789921,8.400156],[7.913043,6.956836,-5.909821,7.543663,7.075306,-0.868665,6.330685,4.341534,2.161850,5.688911,1.511086,7.180194,-7.109401,-8.189867,2.632022,8.653104],[7.029282,-8.820036,2.824726,-5.216065,0.693851,-4.767285,3.497222,6.432144,-1.917663,-8.648588,-7.557147,-2.059133,1.551115,-6.247650,-9.516295,5.925133],[-1.394607,6.254245,1.576894,-1.249008,4.821498,0.871710,-6.604059,8.274143,7.994452,0.778567,-7.897307,-0.086487,-9.985384,-2.164528,-1.010789,-9.951972],[2.969394,6.217678,7.219475,2.943308,-4.767562,1.252135,-5.664168,9.424040,-4.237308,7.755695,-7.979086,3.148034,-5.685843,-8.999881,5.654634,5.114684],[-0.512570,-3.760694,3.888031,-1.806159,-5.377923,-7.056893,9.151418,5.702885,-6.594495,-5.308429,-7.762082,4.801473,9.413974,-5.015011,-1.159245,-1.666361],[-0.481313,7.599872,-5.260833,4.128500,6.607822,1.062031,9.448174,5.843908,4.788767,-7.071847,0.544059,-9.185770,5.989674,4.612037,8.846058,2.866198],[-6.629228,8.820149,-3.348341,-5.022297,-0.741377,-3.173653,-3.873201,-5.953815,9.128504,3.005609,-2.038765,-0.498991,-0.878285,-2.660132,5.686485,3.371327],[-3.021598,-1.149740,5.721085,-1.853949,9.251356,2.103352,-1.947235,6.729712,3.379618,-3.104081,5.940109,1.506160,4.643570,4.408980,5.477032,-7.410820],[8.843908,6.852512,4.768510,-8.241728,-5.140057,-0.371140,7.996310,4.384965,0.590926,1.362640,-1.664831,-5.479825,-2.755168,-5.835880,5.511950,4.777089]],[[3.900091,7.749196,-1.357236,2.278275,-8.394711,-0.647407,-5.475181,-7.416333,4.850799,-7.763245,-2.883926,1.562768,-9.176000,2.955919,9.315002,-0.953243],[8.930012,5.611060,4.838657,-8.821026,6.380000,-3.328604,-0.043405,6.403106,-2.978989,3.887786,-8.982172,5.683782,-2.480114,-3.059982,8.478337,1.338768],[3.171573,-3.085463,3.961584,-3.852992,5.118639,-4.326621,0.723724,-2.807085,0.945992,-0.037199,-8.728577,-0.905551,-7.812164,-8.647611,8.700159,-9.283375],[5.661788,-3.765432,-1.436315,7.658283,5.308191,9.087087,1.867541,-0.344061,-1.450035,-5.521623,-3.843280,7.790573,-3.215790,-5.160903,4.200558,-6.162631],[2.645318,-1.963257,9.871460,-6.178205,5.537184,3.423356,0.457053,-5.760583,-7.009148,-1.218118,0.243680,-9.128368,-3.960798,-7.242934,0.326255,-7.841648],[9.442728,-2.236091,-7.631476,5.508868,7.435322,-2.031748,-9.214940,-8.866569,4.077366,3.677445,-1.348297,-9.418046,-9.789841,7.734908,4.453100,-5.070977],[-9.756804,7.644335,7.145186,-1.871387,5.255285,4.059476,5.329318,8.205119,4.571181,-3.476667,-7.821778,-8.615370,5.881515,-5.538232,1.927933,0.769930],[-3.245023,-0.910847,1.207529,-5.775100,1.770396,-0.123542,5.470947,4.070232,-5.047385,-1.391013,6.362670,5.240327,-1.706676,9.123906,-6.085626,2.820513],[-7.720733,9.685618,2.108871,-7.074458,8.105427,6.942767,-1.845553,8.131541,-0.131263,5.654611,-7.132473,-0.112327,3.284143,-8.258286,-0.569368,-7.015007],[5.095828,-8.350973,0.992245,2.205212,1.089162,5.818838,-0.771576,-3.282903,-5.895555,-7.776686,-5.848277,-4.038595,-9.855878,-7.394277,-0.149109,5.466980],[-1.170397,-5.840253,0.893191,-5.130722,6.771518,-7.832424,1.078680,-0.448775,4.100422,-9.865895,-2.816368,5.876473,-3.698247,1.585017,-0.119586,-5.394021],[3.318515,-2.902999,1.927669,5.202715,-2.522008,-9.006814,1.939068,0.790504,9.006883,-3.141899,-6.045586,-8.090948,5.293418,-3.476941,9.084574,-2.072055],[6.005441,5.839085,-2.209359,8.208566,-9.152491,-2.687746,7.200472,-7.992937,8.575632,-2.377498,-4.740004,-4.299563,-4.961967,9.425392,-1.529068,-1.393949],[-6.547427,-2.563000,5.827230,3.846902,6.262442,7.588146,-2.628441,5.805410,-6.373910,1.024824,-0.514921,2.321445,-2.727763,-6.919026,-5.877262,4.587137],[-2.641326,9.753939,4.254020,-7.250729,-0.913184,1.949848,1.957065,4.496119,-4.680103,7.116640,-3.026409,-5.699350,1.626627,6.640950,5.827212,1.086308]],[[-1.152773,7.886899,1.161349,-6.116992,0.671095,-0.644967,-0.520094,2.659673,3.767054,-7.523526,7.850592,-5.956577,7.246744,-7.856011,-2.010125,8.718601],[5.407095,0.379380,-8.279258,-5.972920,8.826741,-4.646614,-0.829235,9.585602,-7.827522,-8.865820,-6.041591,7.673811,-1.174250,-4.406463,1.943817,-4.184559],[5.119788,3.351324,4.461980,6.555110,4.651808,4.855996,7.266312,8.756810,-9.830877,0.444136,-3.489113,-7.585415,4.777974,-5.927834,-4.409230,2.724833],[-1.335747,8.572826,-9.299135,-3.735833,9.833428,-4.117858,-0.158457,-8.908993,5.711470,3.148816,-0.227075,-1.454638,3.784227,-6.081691,3.936721,9.423122],[3.423205,-5.641769,8.883686,4.474506,-8.283645,-5.842489,5.654659,6.329757,-3.676833,-6.640433,-0.359422,-5.963190,3.989035,-4.172252,-4.541422,-7.943605],[-7.119702,-2.748906,-5.434225,-9.266418,9.851799,8.903261,-0.571020,3.097748,-7.597098,9.478260,-0.159100,-7.692636,6.053867,7.172122,-1.201293,3.862190],[-6.979308,-4.495535,5.190339,7.377720,3.191966,7.267287,1.544801,8.414856,-2.003791,-3.951207,-3.506411,4.720810,6.095240,-3.391558,-6.297810,9.213199],[6.304388,3.064061,-2.898500,7.282527,-3.169154,1.782714,5.308348,5.319677,-3.230073,-7.357725,-6.415692,-3.385300,-7.671271,3.490482,-6.363370,4.567769],[-3.198229,-2.388385,9.938791,4.986710,-4.012762,8.717807,1.494154,0.234584,0.160408,-8.000181,3.670643,1.815722,8.968463,4.150139,9.765581,8.621388],[2.150841,6.401836,7.863730,-2.989505,5.810454,6.260560,-9.479578,-5.289329,8.058759,3.329115,0.771781,-0.447768,8.111995,-9.547504,4.727464,1.974353],[6.588353,2.885486,1.693377,-9.712857,-1.682526,1.174996,4.704127,-5.423965,-0.853248,7.401717,-2.865433,5.252752,7.425213,7.627879,2.690508,-6.410162],[3.574466,-0.123380,4.024411,0.117205,-6.685178,3.996806,9.870780,-3.532804,6.889257,8.822064,-7.324594,-9.685905,6.128655,-6.004633,-4.584849,9.007555],[-7.459611,-8.754264,4.443815,9.274932,-7.435068,8.516583,-5.480055,6.243047,3.068494,-5.497135,9.641348,-7.430319,-8.589731,-1.687158,4.348185,-6.160244],[6.040297,2.473348,-7.608895,-8.047249,8.165703,-0.077350,-7.324416,-8.152126,1.790257,7.339723,8.276539,9.571549,-9.759662,-9.450446,3.153990,7.917517],[1.143138,4.817238,-4.639902,-8.696725,0.474769,8.328586,-9.924009,-2.022646,-1.669064,7.346845,5.270416,4.722256,-5.694212,0.281037,-4.355695,-6.441711]],[[5.221548,-8.643131,5.719646,-7.374412,4.917585,-1.962429,7.537282,1.875983,-9.840085,0.040543,1.867858,6.041342,-8.925558,-4.313013,-2.474237,-5.628280],[-0.200213,0.776427,5.997160,6.125177,6.044424,-6.561364,-8.465842,5.690521,-8.026326,-1.274350,9.562332,1.339140,-6.882312,2.676226,-9.174723,-6.503103],[-1.203150,3.184248,3.335900,-9.418227,-3.338305,2.468707,7.716855,-0.931428,9.529371,0.272752,-4.596918,-9.835322,-3.532574,4.941387,6.414192,-8.422642],[7.295005,1.444319,-4.812585,-9.347802,9.126762,8.012677,-6.087210,-7.146188,-9.293987,-1.873781,6.695187,9.429017,-0.680095,-6.643589,-8.731237,6.915636],[-6.999574,2.547568,7.064730,-9.886588,0.862655,8.243817,6.551845,-5.678209,4.860527,-1.172820,0.269100,2.896750,7.217863,-5.889152,-6.266166,0.359061],[-9.605380,9.052470,-0.252862,-6.433656,9.659121,1.319335,-2.282358,-4.258336,7.569037,-4.177410,-3.141799,-3.457732,2.043905,3.367293,0.728743,7.065853],[6.622462,9.855307,-1.143250,-8.856811,4.478210,-5.300380,2.466066,0.291373,0.971190,5.987971,2.116513,6.047824,-4.777993,-9.640815,-3.255214,-0.248838],[-5.906940,1.576793,8.955319,-7.525751,-8.123321,-7.281594,9.401400,-2.903288,5.095868,-5.129824,5.316906,-0.873493,6.546501,8.059674,-1.728106,5.775464],[6.443536,7.753960,-2.179023,2.866715,-0.148215,-7.194162,-8.635542,-1.512817,7.509046,-4.187808,2.945015,-7.714083,-0.896256,-5.451858,6.955104,7.510225],[-4.584836,-9.441920,0.918252,4.302475,4.247462,6.008113,-6.214704,-4.398340,0.765338,5.225163,2.766635,5.954607,5.438408,-6.495285,7.177968,-5.502704],[-8.129816,7.385030,-5.175091,7.434763,-5.679337,4.678232,-5.626386,-4.520419,4.556907,-6.804306,-1.498071,-5.564505,2.928334,-6.229549,-2.746387,1.087814],[1.005932,-3.933215,7.857995,-3.551528,5.122080,3.512826,2.877835,6.631447,3.795025,4.725000,6.994780,2.737307,-0.747799,0.130352,-4.642738,5.475595],[6.134088,-0.349058,8.015693,6.820593,-1.028014,-5.290367,-3.824617,-4.479686,-0.070299,7.265212,8.287359,-1.329995,3.230121,3.894676,-4.562956,2.949740],[-5.037718,4.455560,-3.397212,-6.681787,3.660919,-2.828942,-9.194019,9.348190,-8.092075,-9.575935,4.518589,6.794613,7.946569,5.817340,3.728774,2.534324],[-6.616958,3.282070,2.180019,4.384438,8.128903,0.744943,2.128287,-7.938660,6.636683,7.692324,7.753370,1.362061,4.585105,6.826644,-1.859654,8.697057]],[[8.372234,4.960483,-0.776199,4.179735,2.683786,-5.043131,1.254519,-7.891295,9.158996,2.888778,0.049252,7.497548,5.811511,8.086657,-9.607183,-8.089948],[-6.125804,-8.224262,8.474224,-9.895319,-0.694894,2.720257,0.832687,9.031229,4.774851,9.976648,5.850879,-7.089781,2.750030,-2.757817,-8.741556,4.623128],[9.682106,4.149454,6.419817,2.312547,-1.720358,8.228308,-8.595841,7.331379,-4.743342,-4.427186,4.719560,-1.922096,2.793124,-0.004210,-6.835898,-3.444579],[-3.567448,-6.062300,8.529055,9.919682,-3.611865,5.129371,3.032954,-8.741863,9.000330,-3.108940,0.171040,-7.571984,5.714482,-0.576294,-3.209843,7.229558],[6.828482,0.063426,4.500756,-2.647815,6.494414,9.937309,-6.873281,-6.253409,-7.753807,0.825344,-1.840273,-5.441643,-7.990612,8.246411,0.625235,5.993752],[-0.473029,4.478398,-6.506177,1.121714,0.231700,-6.079643,-3.531213,-5.551764,8.086623,7.221183,7.543877,-0.945024,-4.359150,-0.473217,-4.763089,-8.512590],[-2.185160,4.150499,-7.336535,0.285052,6.917654,5.990192,-5.146462,-8.099049,4.019036,4.319899,-2.623108,0.353714,1.800114,-0.978865,6.106446,-9.299425],[4.953748,-0.869519,-7.520923,5.814766,-3.008834,-1.001641,-4.666342,-3.559791,-7.561199,-9.907502,2.096226,3.987081,-3.550278,0.748381,9.213635,9.309319],[5.136240,-4.698423,7.640034,1.619609,-1.258827,9.039625,-0.639853,2.165800,7.528379,3.887424,9.510331,-0.942627,7.899470,1.473686,6.269157,8.091072],[1.780258,9.297535,7.530850,-7.343606,-4.361875,3.310500,6.008428,6.889386,-1.877274,-2.154805,8.514301,5.403714,-3.211226,1.990868,-4.260743,-0.839129],[-4.038227,-1.349428,-8.222885,-0.214213,-7.506337,7.192911,-3.406205,1.431296,-2.361478,-0.451277,-3.228424,-0.332659,-3.021450,-4.861988,-8.283585,-5.906703],[-9.001720,-1.194993,5.889687,3.963480,-7.107949,-1.202669,3.115115,-5.775421,5.576606,-0.556810,-9.342926,-3.514096,-3.506225,7.422788,9.114025,-3.716842],[1.892821,-0.033270,6.952713,-0.524562,-0.001287,-8.945539,-5.455546,4.187892,1.578316,1.444187,-8.592192,-7.329079,6.411175,8.677482,-2.379774,-4.063629],[7.733317,-6.381985,1.468866,-8.045344,7.032321,1.130418,9.575100,5.531607,-1.348101,8.653387,-7.992639,-1.635674,8.655177,-9.112816,1.390306,7.764253],[3.942849,5.725537,3.208932,8.338788,-4.992955,-8.205675,4.734896,-0.085628,1.093051,3.537369,3.498160,1.981463,3.443677,-6.838587,-1.755322,5.870596]],[[-9.465631,-6.323314,3.703870,-7.080567,1.581250,5.854578,2.007641,-0.017895,8.505813,-6.691181,2.014967,-1.502787,-5.122996,0.418760,-0.318361,-0.445759],[2.911483,-6.045493,-8.346019,-3.474792,-2.472925,1.801916,1.824783,-7.824134,8.723770,-6.502978,-1.099693,0.821698,6.485637,1.489662,-5.466892,-8.515334],[9.562797,-2.116707,-7.737685,2.169609,-9.425676,-3.553371,-4.660281,4.659820,4.257533,8.512438,-2.775237,-8.558387,0.470994,9.645613,-6.680902,-5.516216],[3.019256,9.691201,4.524987,-7.609026,2.896172,-8.386644,8.344582,7.440656,6.353452,-4.265484,-5.189651,6.333298,-0.991382,2.611396,5.620080,-1.093578],[-1.002557,-3.647117,-3.657965,8.579950,2.306998,-4.178018,6.326504,6.638615,-7.022469,-1.184544,1.485516,-9.186664,5.229694,-9.462613,5.869796,3.320802],[-7.487690,-8.986952,-9.368552,1.453026,6.832459,-4.123474,9.445428,5.009889,1.582079,-9.339423,7.376008,-2.487235,-9.730385,1.969845,-9.369918,1.436552],[-5.017812,7.972611,-7.335333,-3.915822,-2.212388,-7.184940,8.950445,6.140741,-0.483120,2.208203,3.221262,-4.648146,-0.556924,1.025438,-1.610354,1.461713],[-3.857394,3.322695,5.139523,-4.465649,-1.900990,-6.226113,-5.579085,-2.898352,7.134969,2.513954,6.151511,9.173430,1.660039,-4.580017,0.820692,0.114529],[6.287217,-5.470924,-1.764113,-3.269253,-7.236774,-3.388309,9.315787,6.254024,-4.545534,3.244362,-2.367201,3.804787,2.091641,6.344219,-8.196423,9.402190],[3.550942,-4.541421,-9.598078,-9.101212,6.451779,-0.649615,1.963895,-2.529437,-4.633763,0.439671,-3.588168,-2.745338,5.326524,-1.190908,-7.426824,6.895563],[-2.315014,-4.690903,-5.728583,1.797440,0.208512,-0.841635,8.323223,5.833636,-1.677074,-0.993093,8.741228,8.375817,-7.806103,-9.521459,3.098260,-0.990414],[-0.918819,-7.164524,0.010714,-1.009759,2.519247,8.994762,1.569665,-0.826954,5.358688,-5.767409,-2.226251,1.630333,-7.816233,3.729884,7.454500,3.591776],[-1.073224,8.753213,0.640252,1.518979,-9.629522,2.344405,5.193155,-1.790825,-2.404080,5.592683,-2.763507,5.143923,7.934441,-8.212584,-8.128933,-6.840727],[9.812746,-1.489793,2.876221,-4.890667,-9.144225,-7.240196,5.909212,-8.383135,3.771991,-3.164413,9.603696,-9.590901,8.250840,4.737984,-7.771726,-9.106871],[2.661447,-2.340603,-0.143703,2.093514,-2.253117,-1.635362,-0.463476,3.591980,1.788854,2.735413,3.968709,2.902288,-8.739326,-9.269846,-5.542366,-3.829514]],[[7.455020,-4.881324,7.108519,-1.905161,8.859880,-3.766153,-4.351078,-5.012339,5.595510,-5.187163,6.462107,9.924326,-1.441076,2.578332,5.983121,9.623093],[-0.490878,-0.536171,9.301926,-8.709185,-4.440489,-5.981250,-7.240285,-1.541854,-5.943874,4.268450,-5.352982,8.427365,-7.629553,0.823356,-0.684961,9.249992],[-6.126682,1.722657,-5.852199,0.093384,-9.486837,0.074101,-6.615423,-1.895960,-2.285363,-7.161373,7.023971,-5.439169,-0.694008,8.962368,-5.473615,-1.738321],[-4.038145,-4.851306,2.226197,4.989150,6.409486,-7.055422,-3.138873,-8.379190,-8.647289,3.045495,-3.294685,-4.933980,5.604584,3.770336,-5.178765,6.929428],[3.206306,8.860594,8.307502,-8.493089,-5.029542,-8.388146,-7.787970,5.772471,7.048082,-5.080007,-5.485117,1.601444,-7.528269,4.567364,-1.176047,6.871684],[-0.994772,-8.609236,-2.622093,-1.486954,1.789360,2.379599,6.502958,7.305267,-7.688747,-7.847759,-2.155733,-2.072803,7.954518,3.654505,-9.520805,2.055667],[0.744745,-5.588021,0.081015,-5.351409,0.182427,-6.139647,0.370772,-0.085152,3.680068,-6.852124,-9.901824,-1.144148,5.955359,0.256305,-3.238270,-0.966194],[-3.857194,0.266409,-2.498087,-3.251025,-1.164135,-4.470688,-9.504761,1.780169,-1.848898,0.324726,-4.955944,-6.174878,4.522092,-9.125582,-4.699101,-4.094586],[4.286399,-1.163549,0.865553,-4.836859,9.756050,9.656082,8.987210,8.598587,8.641344,-2.931841,-3.234808,7.687328,-0.436635,-9.640984,-6.117981,4.965404],[-7.155113,5.888127,-5.798182,9.552310,3.092163,-9.154083,9.216474,-2.269090,-4.066139,9.410767,1.087907,2.269084,-3.608359,-9.979243,-9.386659,-6.229825],[-4.079503,-5.383489,2.464017,-6.309687,7.784196,8.497647,6.049159,4.214562,-0.492604,-1.293316,9.828357,3.779610,9.592145,-6.572778,8.251770,5.714732],[2.077685,2.123015,8.101072,5.457787,-7.696602,-8.679238,-8.798315,9.154072,-8.504024,-0.450926,6.125132,3.877331,2.575284,-1.279700,-7.986014,-7.532889],[-0.168571,7.087846,-3.115514,-4.917214,9.867257,-2.095906,-9.416804,6.281821,3.828977,-6.480233,9.605676,-9.714404,9.369945,-7.918590,-2.058779,3.931626],[-5.519053,-5.625904,4.047803,4.420488,4.755837,-2.199934,6.897167,-3.720080,7.286554,-8.359629,-1.837304,-6.884542,1.036223,-1.306647,1.592319,-8.960915],[-7.648335,-1.123294,9.306835,-2.366210,6.513884,-0.545445,-9.008448,-5.872179,7.271887,4.751076,2.426570,-8.724803,-7.794348,-5.503689,-8.672583,5.667778]],[[3.468210,1.922870,6.664880,-2.083500,-6.472088,8.577934,1.676779,5.879127,-6.460455,5.212629,-2.647879,5.832546,-5.823633,-9.660753,-7.181390,6.484993],[-7.838621,9.918060,-2.788662,-8.523912,-5.705668,-2.738237,7.988866,7.961587,-4.239820,5.354684,-2.444778,5.564116,-7.077548,7.678022,3.426257,3.089831],[1.095830,6.660680,-3.936033,6.624102,5.521875,-2.251658,6.671032,8.815454,-4.412701,-1.902500,9.230847,3.861373,1.877474,-1.023867,1.627511,-3.321946],[-8.056092,3.750176,-2.887276,-8.258489,-2.115722,-9.942759,-8.899685,8.833108,2.253506,5.066075,3.287569,-8.991249,3.584226,8.494237,-3.757703,-4.690321],[9.554309,4.421254,-4.471111,4.952278,2.891459,-3.958494,9.989615,-1.242773,0.923619,8.222452,2.480417,4.326521,0.318907,7.168513,8.580954,-0.558414],[5.409906,-4.419500,8.938222,-3.975826,7.737727,-0.968162,-3.811630,5.840345,-4.929645,-8.048935,4.225338,6.550139,-9.527986,-8.524161,-3.010603,-8.799794],[5.325746,0.088375,7.460624,0.873909,-0.158431,2.288394,-0.949625,-9.136237,-6.193716,-1.943889,-5.886151,-6.028051,8.637409,-4.965432,8.378362,4.242181],[2.780311,-7.947486,6.496894,-8.641768,9.440481,-5.278278,-6.094249,8.026037,-6.434812,-8.290413,1.713522,5.555234,-6.776175,-0.559613,7.511353,-9.956461],[-4.847734,2.575506,-3.104097,6.679298,8.582472,2.135309,-3.124515,-6.155656,5.265038,6.951363,8.095879,4.486510,1.437705,-1.763928,1.133463,6.676067],[6.850166,8.145101,-7.567983,9.705927,0.229081,-9.644356,1.591913,-4.498356,8.986329,1.324908,-6.064524,-8.018132,-9.158881,-6.556149,0.003725,4.781999],[-7.188118,-1.826369,7.964604,9.202810,9.855385,-4.000866,-2.008613,7.956836,9.343508,3.052608,6.180521,0.300296,-2.090558,2.452150,1.869155,-9.852240],[-2.606376,3.437337,-9.671417,-0.077664,-1.699602,3.586306,7.922894,-8.865173,0.693464,-1.548830,-0.229883,2.027443,-3.560480,-1.514185,9.942590,4.934120],[-0.672887,-7.523889,9.050029,-7.000721,0.936551,0.760080,-1.832931,5.774765,5.061845,-4.198092,5.788453,-7.340863,-7.143896,-9.952072,4.712056,5.406785],[-6.949470,-7.412738,-4.361332,1.160689,-2.662071,-9.586609,-0.138795,5.422844,-5.003093,1.856763,8.471987,8.521111,9.834688,4.130600,6.514299,-2.923234],[-9.826521,-2.381718,4.222099,3.086579,-1.424572,-4.689920,8.802643,-0.626772,8.726344,-0.857394,6.843381,-7.667112,7.464390,3.745812,1.315265,-3.499439]],[[-7.273668,-3.950889,-1.928848,-6.132716,-2.502463,9.646107,-1.533585,6.655060,-7.718463,-2.476155,6.881328,-6.558583,-8.974129,1.227466,2.613919,-0.447381],[-8.990195,3.161067,-3.818988,2.191939,-0.975961,-2.042925,-1.534940,-7.478505,0.655358,-4.911233,1.414824,3.119257,-4.145047,2.698254,-6.921681,-8.638209],[2.499809,6.575683,5.087007,-7.415814,-6.214846,-8.371968,-5.201017,8.606704,9.220202,-2.076556,-8.535867,-8.019630,-8.465235,-5.120878,4.060996,-6.660357],[-8.003008,-2.773445,-8.490118,2.148071,-2.127426,-1.971569,-4.445475,-7.218477,6.191710,-7.157083,3.590527,4.206122,8.443684,-9.888680,-7.392155,8.151016],[7.975649,-9.424384,-7.885353,-1.922128,5.740508,6.218994,-6.850378,4.205568,-0.823059,4.651857,-6.750103,6.022699,-2.646894,5.724308,-8.015760,6.278441],[-6.748155,-8.689283,9.266907,4.110951,9.518189,-3.520550,5.870077,0.641117,7.915892,7.106085,7.124380,1.195083,-4.058252,-9.356023,1.411812,-5.475929],[6.588202,-1.948468,7.658836,0.180908,-1.353494,-9.535201,3.415655,8.374671,-4.256717,0.788405,-7.637923,0.983893,0.454260,9.424322,3.593069,-5.527549],[-3.084595,6.040474,5.724415,-2.924389,-2.860875,8.671983,1.043110,6.459333,0.163010,3.686076,2.308499,-5.008792,3.346496,-8.186440,-7.178011,0.978521],[1.157446,-0.318550,-8.281666,8.500938,-8.414811,-9.713471,3.344606,6.039802,-2.566858,-1.956435,-6.959565,-3.915616,6.864942,-3.293589,-0.161361,-8.457578],[6.546892,-8.788980,-4.931453,-5.085517,-7.653760,-7.490688,-9.142308,-5.362797,-2.785975,9.405126,5.235772,-6.423285,-6.666344,-7.500556,2.352262,-1.470163],[-0.865717,-7.158055,-2.483494,7.024248,7.483385,3.630176,1.452129,2.937345,-2.756972,-6.501066,-1.549018,-4.226747,-6.401013,1.180709,-0.452239,-3.577193],[-6.802610,8.636557,3.853994,2.608640,-5.802903,4.491638,-6.459291,6.090676,3.905594,3.568840,0.022499,-3.248686,-1.344342,6.247286,5.191862,4.023594],[-8.155553,9.011892,7.165911,-5.123867,5.468452,-7.835085,-6.036704,-6.545707,0.185647,-4.780588,-9.499213,-2.595098,-6.854900,8.406085,6.842835,-9.195336],[7.829540,-7.174897,-3.812359,-6.687491,-6.271783,-7.063774,-4.421723,-1.086964,-3.217617,-0.010940,9.016017,8.628864,-0.324748,6.945852,-4.501016,9.894799],[2.760182,-6.030596,3.860667,3.113085,9.558007,-5.637769,7.486630,-2.916627,6.508521,-7.546359,2.647189,9.230418,-8.540495,-8.112521,-7.368003,-0.457562]],[[4.542847,8.321554,3.762987,-9.592590,-9.388858,-1.335095,4.115618,2.580943,-4.258644,2.365299,-8.492305,1.311117,7.190114,8.218624,-8.682642,-3.718110],[-7.355291,-2.027646,-4.212036,5.628728,6.071169,-7.953812,-5.258537,-6.222146,6.003717,-6.403923,-7.757987,-0.939501,9.378670,3.076198,0.516975,9.058828],[3.470831,6.862766,-2.068230,5.895575,3.521792,-4.169834,6.989484,-3.666612,-3.216478,-9.378181,-0.323399,4.903882,-5.911624,5.516093,-7.922100,-9.317477],[-8.773467,8.675076,-8.721377,5.684853,6.951018,3.433648,-8.760173,5.471564,-4.449912,0.165420,4.054393,6.741346,7.749022,2.058017,1.725573,6.912079],[-4.327881,9.745221,4.472161,-0.804934,-4.609914,-2.220865,5.008881,-1.860215,6.725326,-8.016551,-4.316930,6.526295,9.484556,5.780162,-6.784975,-4.299790],[7.482302,7.725800,-8.263478,6.819469,6.392293,0.596730,-2.158092,-9.059220,5.347921,-5.116231,-3.124663,8.602011,-2.728554,5.540194,-0.549590,8.358632],[7.613389,-8.402313,-4.106361,-1.439068,1.183439,-6.231815,5.337103,-0.209008,-2.730304,-5.680731,-0.621873,-5.381461,-0.468590,9.791662,8.934519,8.164641],[0.146588,3.089892,4.024219,8.531150,5.671960,-1.748645,-8.469552,-9.466179,0.983411,-1.423811,-8.847419,1.690027,-0.541521,9.656335,7.046680,-9.516565],[8.449234,4.948793,2.905500,3.930473,-1.763833,-9.588315,-9.578693,2.821476,4.614317,3.354668,-5.221111,5.723004,3.918327,3.721934,4.377213,7.307874],[1.962132,1.587366,5.222164,5.479740,8.657869,8.850110,-8.940255,6.016620,-1.305611,-4.804796,0.574286,9.859942,-8.470402,-2.170112,-9.871374,-6.709811],[-4.637487,-3.548197,5.295801,2.381324,7.943434,-4.273671,-0.501333,-1.010510,1.608623,9.724003,-8.387753,4.658478,8.992027,-6.550533,-3.566772,0.951342],[-6.978831,-7.217988,-4.233044,-0.750824,-9.691558,2.015331,6.350246,2.571426,-2.648296,6.095326,8.949884,-8.874025,-6.699477,-3.155462,0.412699,0.400600],[-5.271876,2.228465,-4.815681,-8.406533,0.768946,1.276364,4.291579,6.333409,6.946211,-4.580068,3.890730,-2.751895,7.573911,-4.155477,-9.480404,0.483086],[-4.915430,3.319691,-8.879932,8.668880,-5.501762,-2.576507,-5.131796,7.424170,3.016968,-5.399897,-0.174426,-9.021573,-2.870311,5.333135,9.112931,1.703979],[8.266467,-5.439610,-9.580248,0.512997,-0.639977,0.417310,9.148441,-4.777093,-3.591150,-3.509263,1.353774,8.483611,6.112021,3.707650,7.968344,-0.009934]],[[2.375724,-2.404860,8.161309,-8.816003,-1.379824,-0.050249,0.106646,-1.047785,8.143584,-2.004163,4.681688,-0.403902,-8.937361,9.477818,-1.916853,3.026053],[-1.104611,-4.831695,2.504877,1.354998,-9.460779,-8.720224,6.702609,3.739422,5.914500,6.114416,7.113777,0.825955,0.675002,7.228012,7.937848,-3.725501],[8.497857,8.735683,0.687809,-5.853600,-6.229847,5.612410,7.452052,-3.324690,2.023429,2.597532,-2.915076,-7.052341,-8.359131,3.938288,-5.202167,7.935669],[-5.968512,8.518878,-1.912001,6.688465,-3.178216,-7.928756,-8.745955,-5.240605,-5.131284,-7.347833,-7.069230,9.008192,0.892996,-8.000424,-3.453837,9.847638],[-8.862597,-3.816191,-8.604841,1.613977,0.368912,-1.195306,9.547129,3.582345,-4.343112,-4.655860,-9.023059,2.808449,-3.416852,-9.380513,-5.801434,-4.463681],[-8.070689,1.042573,-7.500380,5.257192,-0.862064,7.651182,-4.389431,3.728610,6.274468,0.048178,2.535152,9.625558,4.096124,-2.877270,7.069480,-1.803685],[-9.448609,-9.833133,3.805770,-2.912607,1.883882,7.878379,-5.085870,-3.244251,-4.045578,7.789419,3.141717,6.091513,-9.484906,-3.828514,-6.367093,1.959731],[-9.593843,-4.151710,9.264776,7.515464,-4.775815,-9.505701,5.413767,-0.006502,4.205184,-3.216678,-5.824399,0.421346,4.319451,-5.954430,-0.127929,-8.741337],[2.671245,-7.158650,6.714970,1.683338,-0.261713,-4.223132,6.214281,2.796076,3.013948,9.104231,-2.374654,-9.281705,-6.564533,0.210053,0.563069,6.676558],[-0.043204,8.329322,3.032159,-5.347988,5.580910,0.072580,6.607240,4.609402,-4.091983,4.476207,7.179867,1.358018,-7.630246,-0.726906,-8.725483,7.085713],[-4.405384,9.198167,5.770429,0.877038,-2.799622,0.250058,-8.096515,-7.621737,4.235959,2.822859,-2.540067,-6.797872,3.163546,-0.573584,-4.241008,2.184655],[-2.038852,-8.953002,-1.150688,-2.328703,2.614765,-7.589010,-4.850531,-7.769578,-5.448439,-9.305866,-9.103584,-3.916352,-4.010377,-3.411405,-3.979856,7.148334],[-4.687875,-6.265910,1.532049,7.000413,8.861867,-5.185024,7.017713,4.565586,-0.134024,-6.973416,6.845323,6.200046,0.448079,-9.666077,7.346202,-4.705902],[-1.687525,-3.399141,-2.889513,-7.627799,1.780550,4.464776,9.580611,0.973935,1.376961,7.735086,-3.934839,-4.558772,-5.937953,8.198596,-7.741541,5.925532],[-9.649730,-9.702501,9.261917,-9.853389,-0.256869,6.273624,5.426618,9.025958,-8.633549,8.759546,2.937766,-1.452090,-5.001089,5.526899,-5.139558,0.069349]],[[-4.880469,5.198348,-0.195498,2.498009,4.968593,0.235734,5.497234,0.494627,0.332096,-2.489579,-4.498748,-4.246798,-4.509580,7.489868,-4.944425,1.851480],[3.681092,-0.851945,3.568867,-3.484584,0.877219,6.838741,-9.120346,-2.466286,2.871423,7.820516,-3.578639,-1.316178,2.343631,2.594450,3.840682,5.060443],[5.807853,-2.978221,3.934467,0.932080,-9.543512,4.180405,-0.557226,-3.375102,-3.340314,7.202661,6.007720,5.635004,-4.554366,-9.674106,8.742467,-4.662055],[-5.957410,6.126427,2.206020,-5.618820,6.515414,-9.229374,3.025401,6.656745,-7.717284,-1.923443,6.940229,5.780625,-9.798078,5.733326,5.979267,-2.039902],[-1.094096,0.342242,5.113870,-1.664530,5.685452,-0.594027,0.467110,-2.013043,-2.644398,-8.546620,-5.212001,5.473109,5.902997,-5.659618,-9.214923,-9.929158],[5.127718,-5.242755,9.330847,3.807450,-9.223425,-5.855870,-7.999119,5.968833,3.878723,-3.572273,8.649982,1.766703,-9.824449,9.013688,-6.102400,4.150232],[5.581328,-0.018355,-2.151685,6.688287,7.582263,5.158247,-0.236591,2.229095,-9.236737,5.064863,0.795686,-2.056144,0.110510,5.112161,-6.799134,3.969281],[-0.371671,-9.107053,3.872718,2.140979,7.531804,-7.557103,-1.771388,-8.467575,8.903313,-9.082697,-2.110774,-8.245525,7.861070,4.892010,8.273403,1.835769],[0.250974,-7.867824,-3.350289,6.558969,-4.893642,1.007616,3.402218,6.029408,-1.363438,-6.568132,8.150937,-2.928255,-8.758203,-6.252352,-3.769904,7.939475],[2.871849,-3.820881,-1.406928,-8.961154,-0.819188,8.821409,2.622887,-8.198387,-0.730318,-6.112504,-6.236301,-7.951647,-2.320477,-7.727372,6.124711,-2.664486],[8.795428,-6.456224,5.256694,2.554025,-7.897219,6.087157,6.859054,9.995144,-7.868296,0.948717,-0.354672,9.388645,-9.824519,7.590936,-6.152972,2.247561],[7.021392,7.592966,-2.895461,-3.397661,1.804551,-2.158464,3.340747,-0.456302,2.935967,-3.754970,-7.077424,-8.297480,3.211447,-9.429571,-3.128445,-1.109474],[1.598070,-5.213655,-7.573803,-6.128960,-8.770009,-9.487658,3.188925,-2.018887,9.138072,-3.555229,-2.281401,-0.843050,8.560214,1.898433,-3.708379,4.754760],[3.103631,5.364489,-1.018322,5.647425,-5.000624,-2.117088,4.471577,-9.856153,-9.774321,-5.017506,-9.581786,-8.597428,9.243059,4.900474,4.779609,3.131418],[-9.440353,-4.873728,-7.551171,7.142692,-5.694768,-0.923150,-6.708809,-5.810917,-8.442416,-8.489362,3.517018,-0.127369,-8.178405,2.841414,-9.195692,5.382259]],[[6.330473,0.243577,8.418227,2.057531,-3.371200,7.878852,-3.281166,0.067702,-8.092611,7.207302,9.327976,-0.602479,6.468128,7.572538,-1.171155,-5.596119],[8.973821,-7.396137,1.069318,-4.897215,9.486400,-2.935123,1.929292,-5.985711,6.105726,8.027449,9.927115,8.102774,5.986421,-6.863492,6.723317,-6.978413],[-6.213750,1.568634,-7.840216,-3.789139,-5.730774,0.362898,-3.124626,9.567441,-3.677979,-9.826837,7.964743,-9.540096,4.533730,-2.372390,-5.226269,0.493901],[4.843424,-8.308338,-6.086897,-2.648179,0.774001,-5.629692,6.330800,-0.377481,-7.047159,-1.701441,-4.138029,6.756903,0.272394,-7.520312,-5.149043,6.169192],[-0.617390,5.435384,-6.951311,0.125254,7.069787,8.445010,-7.305496,-6.921037,2.618992,-2.251050,-1.608174,3.198519,7.975760,6.028908,8.868355,-9.173619],[-0.765484,-1.347635,6.526406,-0.588776,8.695377,1.594405,2.005279,-3.712438,-4.098188,-6.172143,-5.421601,2.837106,9.617786,1.770173,8.340644,5.243376],[7.778582,-2.775293,0.748281,-6.324579,-0.881362,-2.042387,3.854323,-1.354240,0.028131,-3.264861,-8.401158,-6.813833,-6.919409,-0.904413,1.346198,7.399933],[2.497176,2.838952,9.618740,7.103219,0.181254,1.359867,8.466272,7.261571,3.927080,-7.912318,5.740998,9.486510,1.844434,9.132884,5.419553,1.596973],[-5.040432,-9.759398,-2.282580,3.684683,6.623732,6.436055,0.403333,-4.099932,-0.141012,-8.746294,5.517985,-2.960821,-7.025517,4.355207,-8.725289,-1.009165],[3.352693,-2.812531,7.128001,2.648348,6.991839,7.268266,8.344176,4.872885,-1.435713,6.681416,1.865620,-0.122503,6.594612,-7.091225,6.049975,-2.423118],[5.923324,-4.967279,0.319191,0.068884,-0.701347,6.452374,-6.306981,-3.901296,-5.943845,-5.204674,6.409803,7.133388,-9.154993,-0.122817,2.327510,-0.161266],[-5.077585,9.516066,5.914827,-0.035558,3.761086,4.098062,-4.264642,-6.532447,-2.421698,-6.402112,-1.566595,-8.825466,1.841361,-8.081344,-2.742766,2.592251],[9.912336,-6.803798,-3.971345,7.596169,-0.321206,6.877838,-2.745071,7.389236,3.978286,-3.129483,-5.039439,-0.815877,6.051087,-0.033343,-7.509714,-7.534485],[-7.705737,-0.949672,9.467829,-3.864118,-5.927222,-2.725238,8.699688,4.671281,-7.896722,-2.116403,9.164367,-6.907246,3.735298,-5.903242,8.513523,-1.113032],[1.466138,-3.212880,-5.865676,-1.157975,-9.733404,9.461168,-9.458365,-2.961825,-8.109288,7.794244,-0.323992,-7.766128,-4.041214,8.544830,-2.338679,4.189894]]], dtype = "float64")#candidate|7202|(15, 15, 16)|const|float64
bop_7203 = relay.bitwise_and(call_7171.astype('uint16'), const_7202.astype('uint16')) # shape=(15, 15, 16)
bop_7206 = relay.bitwise_and(call_7172.astype('uint16'), const_7202.astype('uint16')) # shape=(15, 15, 16)
func_5464_call = mod.get_global_var('func_5464')
func_5468_call = mutated_mod.get_global_var('func_5468')
const_7225 = relay.const([[5.557644,1.664955,1.091505,0.384485,5.508510,-4.792299,-9.071762,-1.366824,-5.485261,-2.313800,1.647818,4.226041,6.705715,1.600752,-3.319593,-9.929620,-3.040849,-3.958851,-4.641117,5.141654,9.114222,7.675849,-3.440903,7.249927,9.492432,5.498237,-6.734118,-6.721380,-6.497640,-9.123901,-4.120659,-6.313979,-9.546084,-1.137936,-7.747158,-0.052903,3.065558,9.043030,3.773402,-8.680925,-6.854430,-8.631499,0.792486,4.816026,-7.024370,-4.386074,-1.965369,-4.798927,5.402212,9.787191,-1.770407,8.315886,6.243670,7.246807,6.063066,3.419560,-8.284814,6.847413,-2.390951,7.187997,-6.169889,2.943442,-0.863697,0.866378,9.932359,6.651518,-3.334916,0.382829,-0.553644,-7.049277,2.593249,8.160980,6.459708,7.698900,1.577559,0.572764,-7.981093,5.207784,-4.404540,-0.446191,9.114465,4.549110,-1.140619,-6.736860,3.016384,-6.620448,-4.548722,-8.490263,-4.131780,-0.002439,-7.597471,9.407112,-6.774076,9.457179,0.485699,-6.539354,-7.257619,-7.092849,9.715211],[6.006221,-1.052534,1.885003,7.269082,-1.989186,8.248636,-7.586038,-0.050864,-6.170946,-0.023868,0.593740,0.396393,-3.527861,0.064696,-3.359254,7.396375,-2.117480,0.595651,9.377266,1.462315,4.449960,-6.513045,3.619604,4.717989,8.421999,3.153026,-7.419694,7.917392,-3.403794,8.805454,8.011183,-2.474035,-6.472555,8.400418,9.302515,-8.769020,6.868015,-3.548254,0.146935,-7.388811,7.641768,-0.022373,-6.725005,-1.540229,-2.214537,7.737033,6.693634,5.003025,6.710769,6.787755,-6.537713,3.852119,-0.024794,-9.114846,-2.744725,-9.551636,-9.872282,0.495304,-2.705698,-1.061718,0.327053,-8.926847,5.111414,0.659677,-8.425371,7.013749,-7.129273,-4.740733,-1.481727,-5.036589,8.002271,-2.898420,1.050567,-4.476758,-6.779155,1.005719,-0.905275,-1.435367,5.430952,4.063111,-2.742659,-4.735498,0.150156,5.943011,9.873803,-3.858868,-6.495577,0.991338,-1.533864,-1.608773,-0.332164,4.467058,0.901900,-0.729478,7.870707,0.470846,6.155488,-7.686829,-7.675818],[-8.092972,0.731384,1.346140,-5.603120,-8.524459,-4.006087,2.648449,-2.867070,-9.675469,-1.864881,-6.964361,-5.889479,5.170322,-5.972369,-3.664105,4.415807,-4.675909,-9.193336,-0.159484,-4.671256,2.129577,5.971778,9.628331,7.782041,-8.458760,4.533510,6.296668,-2.360600,6.122447,-2.500159,3.760107,-5.273544,9.055729,2.198700,8.763930,-5.022880,1.798915,4.095415,6.826826,-5.860739,-6.877581,-7.349173,1.835172,-9.800846,9.596162,-4.771855,-1.696293,7.135259,3.695288,-4.810239,-5.302970,-6.091223,-4.992036,3.248013,-5.775719,0.393732,6.302948,1.866802,-7.279206,6.365857,-6.650301,9.819032,-2.964595,-0.649616,1.038301,7.697117,5.576385,0.689299,1.302770,5.979722,-5.314993,1.316656,4.709551,-1.210947,-7.578865,8.556988,-6.324468,-2.247821,5.965493,-7.448811,0.329197,6.474357,1.718798,-3.492937,9.909334,9.270529,4.276518,2.526067,2.477412,-7.858981,4.481182,-7.487146,-8.615380,-9.418214,-1.717239,2.249176,-6.251350,-9.670538,3.644084],[5.550235,3.355849,2.197723,4.377123,5.580354,-4.416065,-5.449857,4.426651,8.060568,5.825415,-8.326004,7.440218,9.562197,-3.364678,6.080364,9.142501,-9.710598,1.345467,2.170066,-3.087755,9.181119,-8.946386,-4.306434,2.194992,-2.063959,2.949081,-1.025142,-9.256457,5.581772,0.864892,-3.395832,0.913476,4.655493,-9.225929,7.460031,0.882109,-7.203158,-0.570246,-3.964446,-2.824051,3.543355,1.556272,-1.749514,4.415962,-0.444094,7.353457,8.695207,5.721006,9.851497,4.461689,-1.388918,-9.560483,9.894013,9.913655,-9.740351,-8.858791,2.250113,6.311882,9.769773,8.486417,8.827569,-9.844758,5.153206,-0.303284,-3.674378,5.489125,-5.483909,6.923402,8.715408,9.578903,-8.292927,6.886218,9.526660,-1.969472,9.103025,-1.168040,-4.466506,-1.141137,-1.365458,-1.614421,-6.842280,5.930563,2.846397,-6.065325,9.649769,-2.291215,6.312375,-1.863431,-3.223895,3.212526,-9.522416,7.338571,5.925431,2.592426,-4.700804,-6.019242,0.747113,1.759043,-1.260544],[4.397033,-8.536945,6.135706,2.893913,-9.672604,-4.433526,-6.130181,-8.960326,4.296678,9.159292,3.736217,9.394279,-4.002334,-5.717606,8.455249,-5.045055,-3.887531,5.120406,-9.046299,6.184864,-5.595903,4.436998,2.939971,-0.018575,6.290916,7.763628,4.268764,-7.898243,0.373559,-8.405166,3.791988,-7.667062,1.412323,8.497825,-7.086181,-7.346498,4.113570,6.581550,5.724855,3.866913,8.924993,-0.080543,0.876544,3.820322,9.452856,-2.929227,-3.240419,-3.461344,-3.574655,3.900379,9.975163,1.501895,6.374268,2.389147,9.558618,4.400846,5.502845,9.402636,-4.968817,4.882956,-7.872359,-2.098630,-2.247862,-4.904826,5.473391,-4.849359,-8.756406,7.936108,-8.831769,-9.555779,8.504516,9.689199,6.392795,-9.105235,8.356082,8.492597,5.875522,-0.941440,1.020234,-3.182966,-7.117253,2.723659,-8.874297,6.294306,2.158060,-7.966325,6.514269,4.751575,3.591191,8.386673,9.866799,-6.254025,-7.553787,1.451899,-3.063776,-0.386910,-0.645816,3.529500,-9.651185],[4.499330,-3.904397,1.168533,1.934264,7.107601,-3.630390,9.102157,4.705231,-5.948387,-6.607239,5.435621,1.985167,-6.125819,6.182091,-8.572005,-7.495621,4.581476,-4.160107,-5.182986,0.686127,-2.805555,-9.803812,-7.364692,3.313766,-1.094941,-2.541413,-2.543845,8.467877,3.220760,-3.317824,4.096441,1.199864,-2.421306,0.299837,-0.111413,-2.262933,-6.215958,-9.640630,-1.925425,9.526955,-4.282433,1.833421,6.947250,0.682648,6.727245,-3.895456,-9.056590,-4.271777,2.908540,3.224712,-5.753290,-3.340494,8.411179,1.659340,5.096099,-0.480749,-8.321126,-2.289102,-3.764871,-8.130270,-1.867428,-3.472947,5.903766,5.376512,-6.449427,-1.610557,-3.400585,5.369925,0.775460,9.503161,5.594872,-0.034286,8.239539,3.220609,-7.010146,-4.101350,6.439517,8.758856,2.201205,5.893242,-6.831835,-3.577961,2.856009,-4.920391,6.491840,1.751575,7.474802,-2.190740,-8.330737,-4.523094,-4.075136,3.768966,-5.034554,-5.850276,3.628259,2.285789,9.299793,-1.295373,-5.225551],[9.898835,8.318538,-5.770625,5.884355,4.210493,7.612152,-5.615016,-4.495120,7.644685,4.339717,-6.803582,0.603742,-1.223482,-3.476550,7.883086,2.868731,-1.648429,3.825279,2.208724,0.635317,6.036160,-6.572721,-6.019790,4.367346,8.618921,4.775613,-3.345427,-1.600587,0.267873,1.605953,1.455889,-9.573809,6.214218,-9.087416,-1.423841,-7.976205,-0.026221,0.297173,3.617177,-1.955847,4.148686,9.779852,5.847847,-9.382190,-4.946205,6.809007,-0.190286,2.870524,-3.322491,-2.438936,1.362051,-0.705262,-6.790104,5.301252,-5.261917,-5.918032,7.328593,8.385735,4.957237,-6.602918,-6.380331,1.204242,2.851747,-1.464709,8.291030,-0.876655,0.530593,-4.608821,-7.118710,-8.599284,-3.673717,6.056898,-2.939818,-0.450905,-1.635712,9.752116,-3.045019,-6.498637,5.583779,9.537443,6.621763,6.524283,-3.419409,-1.091701,7.211809,-4.122781,-4.730395,-4.855481,-7.707686,-4.631253,6.186182,3.834480,0.250805,2.680239,8.422169,1.514180,-4.153649,5.999022,-3.455588],[3.606528,-1.979884,3.708027,3.670220,5.532658,-2.596808,1.174040,9.297831,-6.552308,-6.011669,9.897089,-5.503602,-0.809378,-9.956757,-7.668935,-2.396288,-8.173222,1.415467,2.635937,5.462723,-7.270326,-8.447527,7.901018,6.272754,-1.085519,1.222278,8.953181,-6.014247,-6.805178,6.860815,-5.982864,4.206629,0.050483,-7.086409,2.805533,4.321006,-7.911624,3.957585,-9.125726,4.120061,-4.543091,-9.770492,-7.186374,-2.150965,9.722843,7.661234,8.526113,5.188472,5.457875,7.544478,9.590961,5.502403,-7.689321,-4.333526,4.779904,-7.738039,-5.533518,8.314146,2.159379,-0.150198,3.712696,-9.077772,-0.604889,0.807123,-7.132994,-2.323134,-3.293970,5.555069,7.555633,8.201246,6.721336,-8.527370,-2.683401,-3.427257,1.705527,5.039743,0.362631,1.944893,6.378197,6.158269,6.506979,2.360059,6.440329,1.802185,-9.247143,3.859104,-2.780172,-2.739591,0.176374,-6.618504,3.137072,-5.072024,-8.051009,-9.373032,-3.231130,6.474218,2.097112,9.470207,7.802655],[5.739848,9.189971,7.683949,2.040690,3.771084,-0.100025,4.421906,4.011014,-8.343819,-2.923354,4.112937,6.428896,-2.492763,4.427565,5.044597,-0.850026,3.521304,-4.179923,6.324051,-1.072632,-5.007684,4.800400,-6.432691,5.920422,-4.562716,1.537492,9.536248,-1.824493,6.824969,8.950671,-0.233803,-4.268627,-9.304336,-9.649012,-3.013314,-1.428945,9.720989,-9.761597,-7.953260,5.707278,6.121212,-5.339261,9.921125,0.018484,-5.342395,1.243554,-5.397171,-8.244501,-0.703694,0.988248,8.990085,-6.222681,0.513335,-0.102614,-9.325364,-4.238502,-4.513255,-0.983087,2.593026,9.426084,6.182002,-3.979443,-2.740683,-5.326393,9.638759,2.964436,3.603988,3.807321,-0.659429,-3.794344,6.674517,2.363996,9.475497,8.432992,6.606353,-6.139770,-5.559981,-5.505223,-8.785449,2.399949,-2.107535,-5.436141,-8.768559,-8.571186,-4.789103,-0.669731,9.283470,6.158592,3.703593,5.482920,4.750425,8.364260,-4.876275,-0.356393,-8.111259,-7.453229,-8.576139,-4.544977,9.786790],[-9.954487,5.686153,6.976067,-5.720031,4.222634,-7.079986,-1.046020,1.341964,5.884309,0.846545,-4.574468,8.649951,4.138659,4.190677,1.749036,-0.172706,-7.673859,-4.096004,4.967466,4.882077,-8.622552,5.192435,0.650972,4.704428,8.659762,8.351347,-9.822314,-1.444364,-4.974694,-6.571888,-1.744444,6.859604,-5.555205,7.234611,-9.996677,6.699997,-6.796220,1.991946,5.029281,-3.304211,-1.162247,-7.110074,-8.743090,-7.235897,-7.090376,-5.421997,5.584653,-7.985184,7.620253,3.507699,-3.429140,1.519801,-9.987257,-2.090550,5.442545,-2.965064,-5.882736,-5.689988,3.782518,-8.618527,8.834113,0.779845,-1.060828,8.279471,3.573325,-7.888232,8.611396,-1.586545,-0.091080,1.488624,0.564724,8.007113,-1.998010,-4.121395,-4.653548,0.347092,-0.738291,1.040717,-3.999201,-2.457746,9.491182,1.150508,-3.065522,-2.191400,2.539428,-6.579602,1.720730,-9.744467,-5.356660,-2.570936,9.535693,-6.183574,-9.728811,2.115312,-8.309803,-8.945874,-6.833962,-2.761830,6.366607]], dtype = "float64")#candidate|7225|(10, 99)|const|float64
call_7224 = func_5464_call(relay.reshape(const_7225.astype('float64'), [15, 11, 6]), relay.reshape(const_7225.astype('float64'), [15, 11, 6]), )
call_7226 = func_5464_call(relay.reshape(const_7225.astype('float64'), [15, 11, 6]), relay.reshape(const_7225.astype('float64'), [15, 11, 6]), )
func_6660_call = mod.get_global_var('func_6660')
func_6662_call = mutated_mod.get_global_var('func_6662')
call_7233 = relay.TupleGetItem(func_6660_call(), 2)
call_7234 = relay.TupleGetItem(func_6662_call(), 2)
output = relay.Tuple([bop_7203,call_7224,const_7225,call_7233,])
output2 = relay.Tuple([bop_7206,call_7226,const_7225,call_7234,])
func_7239 = relay.Function([], output)
mod['func_7239'] = func_7239
mod = relay.transform.InferType()(mod)
output = func_7239()
func_7240 = relay.Function([], output)
mutated_mod['func_7240'] = func_7240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6139_call = mod.get_global_var('func_6139')
func_6140_call = mutated_mod.get_global_var('func_6140')
call_7273 = relay.TupleGetItem(func_6139_call(), 0)
call_7274 = relay.TupleGetItem(func_6140_call(), 0)
func_2006_call = mod.get_global_var('func_2006')
func_2008_call = mutated_mod.get_global_var('func_2008')
call_7283 = relay.TupleGetItem(func_2006_call(), 0)
call_7284 = relay.TupleGetItem(func_2008_call(), 0)
func_1707_call = mod.get_global_var('func_1707')
func_1709_call = mutated_mod.get_global_var('func_1709')
call_7288 = relay.TupleGetItem(func_1707_call(), 1)
call_7289 = relay.TupleGetItem(func_1709_call(), 1)
bop_7307 = relay.minimum(call_7288.astype('uint8'), relay.reshape(call_7283.astype('uint8'), relay.shape_of(call_7288))) # shape=(15, 1, 16)
bop_7310 = relay.minimum(call_7289.astype('uint8'), relay.reshape(call_7284.astype('uint8'), relay.shape_of(call_7289))) # shape=(15, 1, 16)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_7321 = relay.TupleGetItem(func_2765_call(), 0)
call_7322 = relay.TupleGetItem(func_2766_call(), 0)
output = relay.Tuple([call_7273,bop_7307,call_7321,])
output2 = relay.Tuple([call_7274,bop_7310,call_7322,])
func_7324 = relay.Function([], output)
mod['func_7324'] = func_7324
mod = relay.transform.InferType()(mod)
mutated_mod['func_7324'] = func_7324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7324_call = mutated_mod.get_global_var('func_7324')
call_7325 = func_7324_call()
output = call_7325
func_7326 = relay.Function([], output)
mutated_mod['func_7326'] = func_7326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6139_call = mod.get_global_var('func_6139')
func_6140_call = mutated_mod.get_global_var('func_6140')
call_7330 = relay.TupleGetItem(func_6139_call(), 3)
call_7331 = relay.TupleGetItem(func_6140_call(), 3)
output = call_7330
output2 = call_7331
func_7334 = relay.Function([], output)
mod['func_7334'] = func_7334
mod = relay.transform.InferType()(mod)
mutated_mod['func_7334'] = func_7334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7334_call = mutated_mod.get_global_var('func_7334')
call_7335 = func_7334_call()
output = call_7335
func_7336 = relay.Function([], output)
mutated_mod['func_7336'] = func_7336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6674_call = mod.get_global_var('func_6674')
func_6676_call = mutated_mod.get_global_var('func_6676')
call_7370 = relay.TupleGetItem(func_6674_call(), 0)
call_7371 = relay.TupleGetItem(func_6676_call(), 0)
output = relay.Tuple([call_7370,])
output2 = relay.Tuple([call_7371,])
func_7393 = relay.Function([], output)
mod['func_7393'] = func_7393
mod = relay.transform.InferType()(mod)
mutated_mod['func_7393'] = func_7393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7393_call = mutated_mod.get_global_var('func_7393')
call_7394 = func_7393_call()
output = call_7394
func_7395 = relay.Function([], output)
mutated_mod['func_7395'] = func_7395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6486_call = mod.get_global_var('func_6486')
func_6488_call = mutated_mod.get_global_var('func_6488')
call_7460 = func_6486_call()
call_7461 = func_6486_call()
output = relay.Tuple([call_7460,])
output2 = relay.Tuple([call_7461,])
func_7465 = relay.Function([], output)
mod['func_7465'] = func_7465
mod = relay.transform.InferType()(mod)
mutated_mod['func_7465'] = func_7465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7465_call = mutated_mod.get_global_var('func_7465')
call_7466 = func_7465_call()
output = call_7466
func_7467 = relay.Function([], output)
mutated_mod['func_7467'] = func_7467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4783_call = mod.get_global_var('func_4783')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_7483 = relay.TupleGetItem(func_4783_call(), 0)
call_7484 = relay.TupleGetItem(func_4785_call(), 0)
func_3959_call = mod.get_global_var('func_3959')
func_3961_call = mutated_mod.get_global_var('func_3961')
call_7497 = func_3959_call()
call_7498 = func_3959_call()
func_2426_call = mod.get_global_var('func_2426')
func_2429_call = mutated_mod.get_global_var('func_2429')
var_7500 = relay.var("var_7500", dtype = "float32", shape = (36, 10))#candidate|7500|(36, 10)|var|float32
const_7501 = relay.const([[-5.191663,-1.430117,-6.518562,-6.109714],[8.823820,2.029426,-2.227343,-2.321302],[5.239545,-0.145326,-8.304139,-6.555479],[0.509263,-7.358306,-0.958084,5.123787],[5.617935,7.228356,-4.042499,8.392682],[-5.157671,1.057215,-6.957298,-0.971008],[-4.172780,6.746956,2.207093,-4.244648],[8.107961,-0.445666,1.724358,-7.225744],[6.664944,-2.968878,4.280923,3.548039],[-6.257588,-4.114303,3.765762,-0.924585],[-1.810360,-1.558101,7.352245,-4.746237],[2.030338,-6.646476,3.395020,2.150094],[-3.153679,-3.419709,8.764479,-5.165700],[-0.149969,-4.536560,9.108668,-5.985237],[-8.610768,-1.606338,8.523877,-2.856311],[4.953424,8.395294,9.762674,-8.009887],[-9.893549,5.738054,-1.189596,0.270373],[9.165164,-7.782460,-4.997817,-0.719003],[4.708220,2.016568,1.019415,1.560832],[-6.315633,0.768799,5.336413,-3.193472],[-9.402034,-9.387205,9.614327,-6.328257],[5.277375,8.084088,6.331965,5.484357],[-2.239056,0.341442,-7.947872,9.110723],[2.612243,1.259824,-7.846943,-1.017208],[2.604652,3.731336,-4.499779,4.405652],[1.957435,3.488789,-1.273941,0.767332],[0.219761,3.601512,-7.455761,1.340792],[1.268639,-3.583786,-3.041658,5.239337],[7.935579,-5.091001,-2.989169,-7.056722],[-8.171942,-1.253078,-6.502844,-0.421688],[-9.132495,5.736654,-5.202240,-8.607264],[4.819355,4.002854,7.469814,-0.019285],[4.091161,-8.194344,-6.614750,1.399743],[-9.735728,-1.474236,-7.592399,0.826154],[-1.244625,4.902532,8.794214,-8.854574],[-4.620194,-0.125823,-5.709680,2.755401],[4.254520,9.267979,-5.628640,-1.617573],[-1.651409,4.146207,7.794832,4.591111],[5.264539,-3.065249,-0.612500,-0.484437],[-5.015879,-1.988365,7.566377,5.785919],[6.837502,-0.792843,3.461251,8.670340],[8.492953,-4.796574,7.544387,-3.322659],[-6.914004,0.880187,-3.491743,-4.825401],[-6.811569,0.762863,-7.233685,-4.267256],[-9.632531,7.793536,8.736828,2.378546],[4.573701,-6.718080,-6.751470,4.057414],[6.267676,9.581260,-7.932237,4.106230],[5.649260,-2.270665,6.635884,8.802805],[-4.395636,2.939611,9.618106,-4.117185],[3.629793,8.179429,-0.274823,-2.969497],[1.034107,4.274276,7.461890,-2.024605],[7.788193,-9.008006,8.245376,-9.685480],[-1.226892,-4.618328,1.291174,-0.066027],[8.171311,-1.202091,4.791125,2.173620],[-1.911338,-4.158127,4.558658,-0.779665],[-7.886360,1.833613,2.289057,1.188167],[-7.412878,6.334788,-4.941052,-2.029077],[-5.236566,0.478918,5.053408,-4.428976],[8.391843,-5.225094,-3.678288,-1.855505],[9.854006,-7.166523,0.086616,3.833642],[3.780790,3.183160,-9.302475,8.169096],[-8.599780,-3.865060,-2.359227,-3.927241],[-8.630840,-2.212161,2.762940,0.064227],[5.973651,8.981208,5.496307,-4.160220],[-3.610998,-0.120736,3.598513,1.797484],[2.955025,2.857517,-0.565290,0.003630],[-1.471170,9.092937,-2.081761,8.550744],[2.181026,8.656579,1.061532,5.434513],[4.141195,-6.011909,-8.302706,5.613265],[-0.660159,4.147925,-9.673016,7.047761],[-7.597775,-2.785903,4.943129,-1.114345],[6.212466,3.747954,0.869102,-0.010865],[-2.189945,1.722261,-3.312289,-4.688397],[-3.700147,5.673898,2.421326,1.877596],[-5.189957,-3.116164,1.774568,-6.083551],[-6.523334,5.523018,-2.862695,4.024254],[8.927295,2.107336,9.338739,-3.549758],[6.262497,-1.583496,-1.970652,0.168220],[6.122182,-3.529524,-9.616309,7.559037],[-9.586823,7.133365,-2.697209,4.244670],[5.443326,3.324980,5.823686,-3.154275],[-7.222744,7.195675,6.506763,3.366980],[-3.550949,8.646263,-1.009557,-9.474197],[-4.658442,7.049729,-3.078430,-8.659421],[-7.477251,-7.600138,1.291177,-6.481924],[0.840098,-1.328259,-3.402151,9.926469],[5.397227,-5.884406,-7.926354,-1.318645],[-4.666511,5.268742,-1.080277,-0.382992],[-7.337927,-8.873719,-9.371950,1.640319],[-1.205487,-2.704628,0.230490,-1.792768],[-8.254364,-0.665698,7.486761,7.114611],[-7.784547,-9.387048,-9.172787,4.692581],[4.640266,-4.080956,4.322348,6.051145],[8.272536,-7.700723,4.118056,1.493009],[1.538143,-5.331884,-2.066111,-9.621782],[0.988412,-8.012666,-6.123927,-9.556732],[8.836526,0.858381,-6.462171,0.623019],[-3.871276,-6.057892,-4.495038,8.064387],[2.015436,-3.652623,-1.763568,-0.311246],[6.694707,3.398462,8.696702,2.189167],[1.999880,7.658823,2.946267,1.332159],[-3.326302,2.614841,-9.611229,5.069042],[3.814635,8.186939,-7.841289,3.983372],[-9.409856,4.256834,-8.516475,5.185206],[9.517588,5.062563,9.784851,-0.292739],[-5.963463,-4.867487,0.931883,-4.725850],[1.526261,-6.342128,0.054540,7.736863],[-0.947468,1.134523,3.380802,-2.209001],[8.721903,4.548818,4.655708,6.304790],[4.626762,-0.947836,7.971782,8.639305],[-6.467696,-5.870646,7.514377,-2.272318],[9.274820,-3.233702,-1.065028,9.948513],[-8.719081,-9.199368,6.946826,3.936133],[5.141121,4.798254,-9.370489,6.177399],[-6.538608,2.360941,8.547956,0.153928],[0.526156,5.859910,7.348942,-7.699621],[6.737510,3.555124,-2.836615,0.971963],[-7.193326,-2.963217,-7.372468,9.131413],[0.436460,-7.557938,-0.127790,1.965516],[-7.457695,4.791281,-2.912867,7.247905],[-6.880406,-0.442115,-4.857467,-4.345407],[-2.343790,7.066887,-0.371614,7.358179],[9.988048,-4.970666,8.728740,-9.462131],[-2.893909,5.198522,4.797924,-4.366954],[4.338937,-3.105271,8.042190,-1.873768],[1.383213,-4.776939,7.969240,6.420483],[2.409186,-9.841408,-3.097621,-6.101121],[7.261074,2.366564,7.641687,-9.068128],[-8.791954,-7.428158,-3.019231,2.818753],[-2.439859,2.584609,4.492594,2.949169],[3.561710,0.757266,-5.558888,-4.517670],[-6.487443,-5.879745,-0.113833,-2.744944],[3.182089,-8.421829,-4.561702,4.197677],[9.874395,-6.899112,4.907999,2.596893],[9.376189,-1.513110,6.607882,2.794027],[-2.624184,9.689700,9.600036,1.224919],[-6.348343,-2.416128,4.948696,2.561636],[-9.463159,4.237594,9.488192,-2.861425],[-7.106783,-5.097823,-4.501658,8.285230],[6.158940,5.675908,-4.021258,0.986522],[-5.054125,3.474435,4.553866,-4.120252],[-5.524636,-2.918202,-2.752980,5.571513],[0.280281,-1.505106,9.766998,1.287440],[-1.341862,1.814031,7.254334,4.863075],[-4.039612,-2.701723,-9.864196,-4.563782],[-7.125150,-3.190937,9.928519,7.692782],[-8.872865,-9.103270,0.652441,-8.605598],[-1.931353,9.223748,4.064542,6.568514],[2.228545,6.801900,-4.471756,5.653696],[-2.916062,-3.565651,4.367980,8.095690],[3.146158,9.171034,3.593087,1.571930],[-9.798835,9.513315,8.662284,5.586486],[-0.933429,-6.416570,-9.251215,-7.685955],[-4.808703,5.512353,-9.185469,5.491361],[-1.275683,0.535041,-4.854248,-5.411893],[0.851171,-0.718566,-2.855654,9.773047],[3.522449,-9.490389,4.509166,-7.142130],[6.607341,1.286390,-2.035796,9.023398],[-5.575123,-6.528431,0.861853,4.294355],[4.885433,-9.656916,6.059700,-5.159405],[2.124216,9.929726,2.153173,-7.311912],[9.950696,8.415061,-9.529818,-1.832433],[9.278491,-6.250888,4.075288,2.923173],[2.536178,8.237861,3.781705,5.235269],[-8.562809,-0.010780,0.612722,-2.624798],[-7.774737,-5.798007,-1.650441,4.302692],[-2.193581,9.787060,8.290980,-4.860929],[-3.851320,-7.255620,7.493783,-8.315414],[-1.271764,-3.451926,-4.179801,-6.157599],[-9.946704,3.543524,0.745725,-4.000509],[-0.973331,-5.040819,-1.342661,6.186569],[-7.241723,-8.225629,9.792209,7.547276],[1.235497,8.408393,-1.663686,4.016340],[8.635118,1.480356,3.241383,-6.399757],[4.415606,-4.608231,9.648588,-7.397294],[5.830774,3.870157,-7.405006,-8.057444],[-8.066492,1.040017,7.120342,3.102705],[1.704425,8.995517,-5.406308,4.554272],[-9.074926,1.489374,8.559469,4.028164],[6.686845,7.504760,9.059533,0.081812],[-1.334163,-5.182577,6.588331,-2.357620],[3.949407,-3.964914,7.200827,2.748498],[1.396438,9.122999,8.247017,5.367768],[0.595555,-0.726633,-6.546711,5.089486],[-4.985466,-0.192013,2.456134,-6.923808],[-7.065607,7.803778,-4.146225,-4.407541],[5.678916,-4.042182,-7.919979,0.259961],[3.143145,8.313101,-1.558941,-6.701641],[-8.068003,-0.576350,3.793192,-9.120142],[5.901507,7.919892,5.744729,3.736647],[5.144222,0.229340,3.675598,9.649825],[-6.994124,-7.190413,4.740752,1.131311],[9.632781,-5.754500,-1.483245,6.056071],[-7.832150,-0.169681,-5.949647,-8.108003],[6.901518,8.705437,6.467553,8.084382],[7.640846,-1.463131,-7.763667,3.051827],[4.890495,-4.671314,-0.120147,-4.730577],[-7.049905,-2.427909,-3.001619,-1.399315],[-8.671308,4.233610,8.443426,4.559081],[-0.517632,3.494350,9.189247,5.053221],[-3.971390,8.538736,5.639717,1.034611],[-0.937551,-9.303200,1.986192,-2.285043],[-6.451845,4.043324,3.620868,8.763572],[-2.980985,-2.001300,5.284711,-2.004984],[-6.893478,-5.815396,7.673841,0.668355],[-4.614815,0.065719,1.894155,0.209819],[3.450858,1.097665,-8.636215,-9.536380],[5.116210,-6.569249,-5.954941,5.725142],[-8.462716,-7.153348,9.809142,2.549863],[8.071950,9.258019,1.014111,2.351526],[1.506311,2.212256,1.294770,-0.881714],[-9.735081,8.710283,-6.720709,5.278901],[-2.823770,-6.055593,-0.576564,5.912556],[-1.102332,-4.973892,-8.999730,-6.806453],[-1.997942,6.014608,-6.311605,-0.669351],[-6.880058,2.287320,-3.695055,-1.273490],[3.699579,2.585924,-4.168405,1.942080],[9.203719,-5.905639,5.999134,-3.878490],[-2.726041,2.669603,5.347673,-9.659939],[6.411254,-3.479141,-9.033099,2.091322],[-6.296718,5.750413,4.144117,4.584554],[-7.324591,-0.882669,7.257973,3.818237],[-1.010636,-3.590047,7.573233,-3.462773],[-1.541293,-8.343218,2.523879,-9.094413],[-9.181899,-9.572440,0.340582,9.423471],[-0.074220,3.168811,-9.393351,1.733375],[-3.985375,-3.361695,-0.240009,-7.836865],[-2.425717,-7.574465,-7.799633,4.643436],[-0.658222,8.250203,9.059273,-0.504951],[-7.228370,2.799577,-0.603972,-9.207972],[-2.138933,-1.615453,7.593286,-6.369514],[-7.235203,4.906228,1.792428,3.331191],[-9.820539,3.613495,9.534098,4.774332],[-1.859170,-9.993351,-0.927101,5.121094],[-5.407528,9.892223,-1.898955,6.183080],[-5.565423,-5.305538,5.570043,-6.791542],[-1.504848,1.193016,3.304919,0.014599],[-7.638912,-1.632913,-6.403282,9.476261],[-2.080940,-9.922379,-0.017378,4.876598],[-6.983409,3.225572,5.263379,-8.314068],[3.757814,-8.415653,-0.137258,-9.572706],[8.783925,0.184502,-9.201332,-3.932000],[-7.153926,-2.505033,-7.285768,2.791598],[3.184964,-8.094259,-7.089590,-5.999807],[3.818063,-6.229939,-6.607894,-5.521949],[-8.227759,-6.494869,-9.343322,9.492586],[0.609481,-4.334905,4.134051,1.832779],[-0.630962,1.419194,-3.058406,-2.696635],[-6.293539,7.822659,-2.764904,6.761813],[-5.418709,9.958235,-9.253381,5.241077],[-6.291078,-7.866528,6.505772,-6.345862],[8.253247,6.975056,4.135246,2.293019],[-0.540169,8.936239,-5.544656,8.784457],[-4.651343,-4.893409,7.517587,-3.014947],[1.601722,9.996172,-0.193788,-5.483967],[-0.102605,2.900059,8.725493,7.079425],[-6.140259,-8.685469,2.014772,7.920600],[5.752192,7.231583,7.156556,-9.215581],[-2.027613,2.070773,-3.984051,-5.808060],[8.126320,-0.636041,7.899697,1.272674],[-3.948481,-3.313822,9.816660,8.635038],[3.114070,-1.633159,2.112061,6.385968],[-1.817284,-2.385592,-8.123330,7.690519],[8.479631,7.990917,-7.800119,-8.153834],[-7.242438,-8.442793,-8.296321,-4.952804],[-0.657350,-8.227067,-8.564741,4.624234],[-1.028822,6.409766,5.899954,1.646304],[-3.386399,9.201305,7.698688,-0.644474],[-8.823228,1.265802,-0.375950,3.715804],[-0.586575,-5.749007,6.317504,-3.517151],[-4.016448,2.268410,-6.059882,-8.563793],[2.771420,3.959569,1.129472,-7.037694],[0.993990,-9.552844,-6.249036,-4.900117],[8.273346,6.273057,3.668721,-2.231986],[8.351195,8.998873,-7.229102,-1.199622],[7.744507,-8.278025,8.596900,-0.137930],[3.818154,1.051926,-5.209508,-6.616692],[-2.887528,7.677257,9.809698,3.690375],[9.647754,3.841719,-9.744019,7.061497],[4.309673,-1.306663,-9.701718,4.488566],[3.159740,1.061276,3.618666,6.517289],[6.602792,0.523568,6.497664,9.057630],[7.338171,-1.141422,6.864441,2.548302],[-2.303365,5.612863,-4.610271,-3.515469],[3.230746,-5.887746,2.387257,8.427569],[-4.101050,-1.822948,9.863711,-4.951849],[-8.551172,0.005616,-3.979731,-5.928834],[-6.898435,8.335328,9.051056,8.282551],[-7.168690,4.962999,8.946756,-4.302265],[4.401959,2.089772,5.247028,4.800082],[2.049498,6.548179,9.073745,-6.216126],[0.825149,-7.641171,8.257248,-2.142779],[8.109061,2.611907,-7.200488,-8.158599],[-7.537694,-7.281628,1.274464,8.874171],[-3.169098,-3.971787,7.807286,-4.387569],[1.900657,9.030962,-0.379276,-1.062697],[6.194795,-0.755973,1.418378,9.348954],[4.071185,4.717121,4.286791,4.597491],[9.309817,4.242230,-5.320930,-9.575689],[-6.215218,-3.554199,8.687165,7.659902],[-0.927076,-8.481618,-6.842551,-4.191558],[6.013499,4.507798,-3.968945,9.998203],[-3.044727,-3.014920,-5.536870,-7.451050],[-1.110747,5.909119,8.581900,-7.851081],[-2.020132,-3.749711,-7.794917,-2.927640],[-9.156799,-9.244075,-3.765728,3.087799],[-6.658117,7.409527,-3.230703,-4.333184],[-4.291497,-1.732790,-7.392191,-9.144724],[1.201827,7.774061,9.674095,8.297372],[3.148325,-7.383731,1.663760,8.417267],[-4.109415,-6.667997,-5.583021,4.374746],[-9.884158,6.040588,0.854830,-6.028118],[-2.591053,-6.144493,8.579673,7.491387],[-5.149111,1.733035,0.400079,2.236719],[2.319424,-5.826490,-6.170653,5.192788],[5.712610,6.287924,-5.844207,1.741344],[-8.438188,-0.464520,-7.092900,-4.703800],[6.895952,-6.450362,-3.711667,-8.970602],[-3.906723,-4.755673,5.994146,0.434864],[-7.163888,7.641822,-6.557080,7.103594],[-8.088214,8.981163,8.562446,7.428353],[0.588915,-2.180100,-4.806280,4.458841],[6.826645,3.422442,5.414061,-1.860429],[-6.264809,-7.135476,-7.898258,1.996554],[6.429931,1.020123,-4.398472,-5.770532],[5.313351,-8.942752,8.177003,-4.850334],[8.787261,4.415736,-8.809842,-6.739110],[5.266620,-9.747523,-5.058406,1.820763],[-2.187567,-7.020817,3.420589,-8.821710],[9.346198,-8.879076,-1.430070,-8.409330],[9.452935,9.321075,4.698172,-3.375940],[-4.675854,-3.623798,-8.964436,6.705333],[2.150111,4.427113,-4.367325,1.139894],[-0.840564,-8.108367,-8.340033,-6.084092],[5.434262,8.292092,0.645565,5.799938],[-5.552428,-6.979605,6.150724,4.351657],[-0.992814,-2.878172,-4.405300,-0.710386],[5.078199,-6.003562,1.171725,3.096875],[-6.055001,3.278344,-6.839761,0.366830],[2.943053,2.567415,0.053809,1.368125],[-8.058224,-7.428578,1.283894,6.286726],[-9.534620,-9.892523,7.944506,-7.996081],[-8.790553,9.534596,-0.702075,-4.536373],[2.778578,5.435750,-5.693949,-6.881843],[-3.565321,-2.375525,9.410775,-1.157458],[2.088400,-9.378387,2.435094,-2.424452],[-3.219937,-5.819422,-5.507206,-1.858984],[7.266862,5.415602,-2.918730,-3.813651],[-2.667073,-6.397706,-8.647486,3.332633],[3.299942,-0.754919,-5.664716,3.847771],[3.825030,-4.041638,-8.194533,3.983297],[-0.300945,9.701017,-9.090586,5.900204],[-3.830571,-7.044925,-3.235871,-5.781563],[4.049800,-0.522364,8.758284,7.644749],[-5.108423,5.639178,-3.350743,-4.552822],[9.622619,-6.485739,1.814497,-1.680825],[1.514902,-3.786764,4.875733,-3.558365],[-5.223201,-6.119406,-4.539416,-3.375253],[5.882490,4.152818,-9.475869,-5.851255],[9.586875,7.320824,-8.290722,9.970181],[-0.430431,-5.493341,-9.393771,1.681196],[4.309713,2.937603,7.200425,-4.947480],[2.387390,-8.940901,8.727579,2.289969],[4.656543,5.069280,-4.693188,-5.191814],[6.467623,-0.445113,1.901860,-4.715918],[-6.326004,-5.178737,2.516978,-0.314177],[-9.770861,-1.896205,-0.738954,-2.771566],[-0.504162,1.686633,-9.497435,0.048072],[-8.675304,-5.674303,6.506624,8.278646],[-7.345958,4.666178,-3.880435,-9.040798],[6.496846,1.597203,-0.963224,2.085376],[1.263111,6.855464,-7.194078,7.677729],[5.415991,-6.492598,-7.493425,-6.621028],[4.837402,-9.097167,1.076150,-9.846897],[3.973905,-7.003572,-8.197822,-9.149573],[8.703484,1.913462,8.326781,-9.585743],[-0.589705,6.346750,-8.545311,7.583897],[-3.431388,-4.854456,-7.805680,-2.811427],[-5.316428,0.419786,-9.973818,-9.402317],[-0.786896,-9.522029,2.642998,-7.677993],[5.013689,-0.915053,4.134202,-1.711397],[-7.182665,1.830940,2.851377,-1.813237],[3.892005,-3.035434,-5.821326,2.564992],[9.494519,-7.241796,-4.651539,-7.259489],[-8.093668,-9.928579,2.933110,7.426888],[0.933409,-9.265935,-3.822337,-2.616003],[6.205637,-7.924121,5.774942,-0.570295],[7.197579,1.533028,0.780659,8.368691],[9.477371,8.956614,-2.806824,-4.356968],[5.562071,1.101105,7.958770,6.598397],[-7.746704,-3.017474,1.786652,-6.066892],[2.298423,7.418756,-4.106545,2.334860],[-0.022404,-3.838410,7.251711,-9.590686],[8.485461,1.944515,0.197034,4.612473],[-7.097948,8.526852,-7.564566,-8.963100],[-8.706891,-7.384379,-7.777636,-1.971428],[-9.925796,-9.466889,9.839744,1.983441],[-6.886097,9.551981,0.426470,1.190248],[6.672593,-4.941765,3.278232,6.322246],[-0.931532,-5.521027,3.642792,8.815982],[1.804207,-6.535315,-3.802358,9.518775],[-0.417378,-7.897556,-2.804732,8.877195],[-8.061447,2.841598,-3.284922,5.363665],[4.607584,3.225761,-8.581725,-8.371390],[-8.041224,-0.632121,-5.123074,6.520682],[1.132894,3.810042,-8.359277,2.439140],[-5.354423,-4.141808,0.415559,3.371640],[0.176168,-3.873274,0.134930,6.503668],[0.780089,-4.002785,6.685730,-7.915873],[7.332301,-4.779892,-3.876739,-3.636267],[5.109432,0.367192,6.790511,3.717560],[8.979246,-9.287256,-6.369988,5.527681],[-4.712035,-8.277592,3.429351,-0.818701],[-6.030818,-5.984842,-5.507905,6.372197],[4.975146,-2.566500,1.509124,1.910009],[5.437906,4.202001,2.851676,3.698799],[-2.896532,-1.608667,-8.558664,-0.565390],[6.952924,0.448876,7.313786,9.062608],[0.713268,3.241711,8.090478,-1.742032],[1.816556,5.110244,-3.306066,-7.363699],[-7.425587,-3.446134,8.145784,6.150291],[-8.051379,-5.053820,9.703559,-5.744146],[9.246260,9.423171,6.282844,-4.306509],[9.398787,0.599423,-2.776370,-1.148124],[-6.484231,-5.834183,1.138692,8.511654],[-0.634494,1.641881,6.624382,9.435511],[-4.920607,-0.949046,-2.051914,-4.539952],[-7.658069,2.563672,6.171260,8.964259],[-1.580922,4.825162,9.477431,3.625493],[-9.266693,8.341918,9.585828,-2.419029],[7.568914,2.696140,9.042651,5.356935],[8.874102,0.944006,-4.395743,8.399670],[-2.874668,-1.444948,8.661544,6.773858],[-0.320780,4.927062,7.739758,1.451624],[-8.436166,-5.044780,-6.985970,3.256995],[-7.422487,-2.052833,4.398920,-1.174572],[-0.882951,1.428106,-6.566861,8.946068],[9.872090,-7.485946,3.514537,9.455874],[-1.167532,4.522321,6.753167,3.796346],[7.489497,-5.740204,0.181270,-5.980815],[2.472844,7.103756,0.507240,0.390280],[0.352335,7.987863,0.730533,5.175696],[1.439746,3.246212,4.999407,-1.877133],[-7.242930,-7.737268,9.270787,-1.119097],[-8.345558,1.121160,-6.436325,3.223227],[-5.279773,-9.091764,1.351990,-1.725988],[3.020336,-9.241581,-7.897383,7.707713],[7.679139,-5.342598,3.367855,-3.845466],[-4.503883,2.237940,-8.121864,-7.120404],[2.735688,-9.983969,-5.475326,5.996666],[-0.871672,4.736473,2.405028,-1.402703],[-9.244751,2.815726,3.781927,7.159774],[1.626485,-8.296943,1.032771,9.870356],[-6.658022,-9.707287,-8.408421,-2.219233],[1.644416,9.012030,-6.036325,5.534182],[-4.761660,-0.442283,-5.659426,4.482760],[-7.404326,3.469916,-5.063256,3.791359],[3.541708,-3.100720,4.484332,-8.795086],[-3.998470,6.977127,1.444766,8.547278],[-1.276106,1.498496,3.544002,-2.910728],[7.658199,-0.356046,-1.059802,-8.398006],[0.402188,9.721350,4.394393,9.715491],[4.972121,-7.737697,6.939575,-7.929997],[-0.683479,5.464007,-1.107403,8.517443],[9.067774,-9.301467,7.475848,9.102696],[8.540705,-1.762898,5.715517,-1.729289],[-0.027067,7.666890,-9.892926,9.855085],[-7.797112,-7.749561,2.551580,-4.678717],[7.974064,-2.804606,3.619203,9.202229],[1.030797,3.486780,9.944311,6.499961],[-3.689966,-3.208254,8.408864,9.340740],[-6.139121,-6.499438,-5.409259,-4.564715],[1.986164,-5.040422,6.415292,6.835839],[2.682114,2.755591,-2.413472,7.889850],[2.251066,0.731375,5.898332,-8.832115],[4.334290,0.896528,8.106515,7.048093],[0.768834,5.545957,-6.320320,1.145037],[3.075611,-9.147631,1.275017,7.329815],[3.251528,1.287771,4.055892,-0.406055],[1.558429,-1.711540,-5.124092,6.475333],[-6.518849,-5.491588,-8.877325,-9.159400],[-4.158743,9.811868,-7.017748,-5.915874],[-0.608845,3.550489,-4.215589,-8.651897],[9.109513,-6.858597,-5.495432,6.040390],[7.283266,6.844110,1.703815,7.258393],[0.645553,-6.127838,1.767461,3.500341],[-3.517440,-0.821152,6.168265,-5.678991],[5.376137,-3.696754,6.188889,-3.323031],[7.974307,-8.293662,-9.663072,-7.340352],[-0.605565,0.368764,1.312116,8.415270],[9.939558,-9.559866,-2.039527,-6.079527],[-9.689747,-9.603168,-5.421221,-6.664924],[-3.147740,4.662944,-4.280221,-8.969370],[-1.349353,1.422027,8.776993,4.157011],[-9.216814,6.109622,0.404686,-1.626988],[-3.664626,9.742032,-9.874809,-8.346348],[-6.568924,9.987674,4.512178,3.319471],[2.839760,2.874580,-6.737294,-0.423481],[3.178160,6.869623,1.886297,-4.363852],[-3.295470,-3.387362,1.609462,-0.580977],[-1.110001,-2.789129,7.427775,6.450572],[-7.279149,8.437540,-5.530128,3.746045],[4.171076,-5.850792,5.283813,-4.454135],[-8.254296,-3.546398,5.142461,2.754456],[-9.965926,6.905744,1.675565,-3.178683],[-2.632336,-1.497587,8.933195,-2.835228],[0.733310,7.788615,5.510629,-4.242971],[2.571950,7.152423,5.661635,-4.850708],[-0.628455,-9.347013,4.116960,-5.519006],[-0.904182,-7.395104,-0.679911,7.677355],[5.872482,-6.105647,-0.746046,-6.764498],[3.845871,6.884572,-6.376070,-4.416845],[7.211618,-9.649931,-2.259050,-3.974939],[-6.339220,-0.237804,5.469969,-2.019507],[0.442176,2.851110,9.076952,2.879988],[7.936025,-4.244168,-5.050041,1.415215],[8.540436,-4.776195,-1.343283,-0.776410],[4.312605,0.736381,-3.989740,0.231882],[0.904981,-3.548207,-0.744047,1.052381],[-9.040003,2.180954,8.961751,-1.106384],[2.963523,-3.423407,-1.467480,-2.502910],[9.434097,-0.477844,6.836708,0.633280],[7.292522,3.081297,1.707620,1.885490],[-0.433946,2.264587,3.106127,-2.883390],[-2.043298,-2.859269,-7.324648,4.884969],[8.606935,4.134495,4.590135,3.547986],[-7.843112,1.166459,0.454546,4.820681],[0.616262,6.136927,0.275892,1.477325],[-0.147658,-6.464608,-5.681821,0.565797],[8.335575,-3.150123,9.849722,7.035462],[3.221926,-8.206447,-3.275846,-7.736761],[-3.923060,-2.313743,-9.593371,7.571612],[-4.496751,4.152399,5.852907,-8.239889],[8.881218,-5.947529,-4.344193,9.599025],[-3.975500,-0.875134,1.267526,-0.432529],[5.403201,4.442702,8.271168,-0.328127],[-3.947769,-9.137139,-9.184606,3.641764],[-4.291531,1.080944,1.676325,-4.158510],[-3.570311,-6.628121,0.513585,8.700574],[-8.267870,-7.934937,9.888419,8.440250],[-2.408588,-1.615589,-5.194092,9.115387],[2.223343,1.925505,2.595630,-1.006143],[-7.749245,0.357788,0.388773,-0.112177],[-1.965700,4.279081,-0.535342,6.041209],[3.484068,9.151755,1.711156,-3.013427],[7.741507,-8.853482,5.443795,-8.823555],[8.388550,0.279970,-2.480272,-1.939262],[2.621821,1.772713,-5.214154,-9.043684],[-9.500402,6.386868,-8.039052,-7.273917],[5.019579,-7.613206,9.229555,3.362795],[5.661787,7.644572,-9.792328,-7.639380],[-2.360638,3.325893,-0.183053,-8.852683],[-5.600305,4.145292,4.489549,-1.789175],[-8.404800,9.281359,-9.846514,-9.856698],[7.974994,9.611981,-9.205098,4.195361],[0.273917,0.220562,4.453540,-5.998153],[-4.864664,-7.540688,2.046537,-7.857031],[-6.309123,3.513791,-8.646396,-8.166734],[-8.238640,-2.864777,1.139494,2.622038],[-9.964637,-5.130019,-5.291806,1.076780],[-2.389186,-8.914344,1.048177,8.187465],[-3.097802,-9.648247,4.284810,-5.845633],[-8.728862,-1.640419,7.286655,2.091847],[-1.981124,3.289950,-4.144662,0.417301],[-2.108314,4.860707,5.509539,3.261654],[5.356553,-8.854114,-8.688231,-6.935831],[9.134887,-0.671160,-3.169323,8.347937],[-3.871033,2.209316,3.242622,7.615546],[-7.070510,3.081656,-5.781458,1.200834],[-6.940980,-2.015115,1.108488,-5.789381],[7.809092,0.845550,-2.374255,-8.541917],[9.963759,1.035779,7.092069,-4.171095],[9.497931,5.523632,7.574198,-2.603380],[-3.655948,-9.185141,3.829337,2.138130],[-6.658790,6.662422,7.428390,5.463166],[7.105532,8.187610,3.727417,8.143662],[-8.071350,-8.630103,6.099411,2.656303],[9.939343,0.061876,-3.141641,5.378703],[2.411051,7.168632,6.579604,6.467561],[-2.670300,3.396413,5.938130,-2.824881],[9.741987,1.222310,4.207674,-4.968209],[-2.295766,-1.067566,-8.918572,2.076357],[-1.037423,-4.084269,5.131477,-7.675769],[8.561220,-7.412653,-9.909868,-4.636947],[9.868064,6.594912,-7.242898,-7.428589],[7.552164,-7.782493,-2.655974,-1.855705],[-9.061511,-6.729018,-0.955389,5.330036],[-8.966454,-5.946994,5.454263,-3.758910],[-9.081475,8.345878,-1.933228,-4.983018],[-5.778442,7.513622,-1.498839,1.729824],[9.374748,5.158097,4.256690,4.325425],[-0.171785,-3.380738,-8.045429,-2.747619],[-8.337397,6.852771,3.852026,1.514544],[-1.158739,1.421839,-7.154983,-6.627074],[-5.269336,1.605464,-8.357030,-3.561148],[9.138443,-8.511545,6.824297,-1.122642],[4.173024,-8.662714,7.896595,-8.497859],[5.610881,7.289324,1.824591,9.024668],[4.859022,0.673207,6.153542,-9.753406],[-1.014213,-4.790036,8.972546,-1.416322],[-5.904469,-9.446766,-2.628458,-6.150320],[-1.727101,9.198195,9.480509,1.408570],[1.506502,-7.431609,-9.972391,3.292389],[-0.481008,0.084377,5.901616,-5.076846],[-2.233642,8.795291,3.836843,-4.657832],[9.355240,3.357817,-1.355578,1.891916],[7.855270,-4.153228,-1.617915,4.100756],[7.329322,8.444983,-5.277305,4.959207],[-0.856310,3.147287,-6.869036,9.783775],[8.069381,-8.211649,4.847453,3.804975],[4.663644,4.319312,-5.612713,-7.402442],[0.871089,-4.787127,1.961402,-8.244221],[-7.466422,-0.433632,-3.478228,6.212199],[-3.248846,4.845400,3.140181,8.798253],[3.955189,2.514581,6.200899,4.717510],[3.311569,-9.922026,0.948728,-9.242138],[-8.178962,-5.018518,-9.483834,-5.098687],[4.145186,-2.740737,-1.491025,-6.231482],[-9.433763,6.091441,5.714546,-5.665646],[-4.335078,-0.321329,-5.988318,-1.043200],[0.897725,5.435384,-2.628618,-4.141242],[7.383695,-5.477422,-2.195848,6.779658],[-4.347197,-4.301612,-2.679827,-4.009877],[0.480670,-1.421446,9.402720,-3.422085],[-0.988661,-9.434584,9.536883,-3.337870],[-3.299160,9.937225,7.385717,8.576083],[1.937295,-0.697635,2.073959,5.115950],[4.802104,-8.456887,-4.844654,8.280170],[-9.438883,8.749804,-9.972549,-2.582343],[-5.653001,-2.384967,1.858806,-6.099070],[8.359026,-9.796556,7.254214,-5.094023],[2.538456,-7.630080,1.611397,-6.501034],[5.812893,-7.035923,-0.966532,-3.487061],[-0.850242,-0.222847,2.985125,-6.878897],[9.174550,1.543312,-4.859922,2.102930],[-7.924696,3.230926,8.150259,3.966995],[6.539426,8.846084,-0.619998,8.924641],[-2.169234,-2.824015,-7.240590,-1.636287],[4.545819,-6.725038,6.598956,-9.811529],[2.310667,-7.570757,2.555676,-2.687487],[3.087638,-3.259909,6.878970,-6.357369],[-8.871033,4.074658,9.664022,-7.538750],[1.586895,9.692824,5.560360,-3.761011],[4.510180,7.580849,-6.222901,-0.591877],[5.184742,-4.337037,-7.781214,-6.671088],[3.712299,3.375466,-4.521021,-7.529609],[-0.643110,-4.925985,8.497836,4.185960],[2.252164,0.381879,-3.162177,4.975631],[4.692310,-9.462179,-5.965306,-1.221514],[6.466217,2.293108,8.886534,6.843556],[3.990929,1.534931,0.917821,4.215575],[-9.353151,-1.419146,-7.827615,-3.694853],[3.382791,2.086956,-0.381013,-6.257927],[2.677755,2.965870,5.750963,4.534889],[-9.544072,7.764563,6.306514,0.306065],[1.610140,-9.211016,4.667529,0.840320],[1.398707,3.323428,-6.095392,2.364243],[1.224537,7.239010,-8.822234,6.344917],[0.773012,-2.438106,9.213704,-6.701380],[5.237113,3.025035,-5.355827,-4.763939],[5.134318,3.804721,4.397663,-6.793759],[1.677023,7.160059,-1.859236,-4.696756],[1.028959,-1.457359,-6.085714,5.285173],[0.529610,5.312055,-0.385051,4.006976],[6.482862,4.765440,-6.696183,3.616473],[4.684680,0.735814,3.972169,-4.404040],[-6.056635,5.715665,2.180588,-0.919976],[5.757484,-1.457898,1.380544,-0.601716],[-6.523183,9.741098,4.115716,-8.575168],[6.326597,-0.394461,-6.568839,9.442627],[8.692104,3.781861,-5.959363,9.859861],[3.814745,6.569841,7.377533,9.098585],[1.371642,-5.906834,3.719552,-1.570140],[-6.857833,4.947391,0.460886,3.281221],[-1.782537,2.150557,9.474546,-2.409866],[6.870514,4.301851,9.748388,-9.573477],[-5.696688,3.545658,-7.320752,-5.304699],[-6.101682,1.788443,9.442011,-5.263000],[6.086428,-5.982201,-6.652110,-3.743566],[-8.171548,3.974601,-6.366985,-1.687266],[-8.197372,1.194575,6.219068,-0.684662],[3.555084,5.206656,-3.709775,-7.444904],[-6.399716,-3.083247,-9.368359,-4.448647],[3.763312,-1.974677,6.440532,-9.874405],[8.151671,-9.225074,7.736658,-1.909522],[-1.987951,1.297786,-1.185225,8.602468],[-8.373290,3.297590,-4.121022,8.106439],[7.958342,1.946632,0.272052,0.469426],[0.882890,3.817347,-1.537154,-2.636259],[-1.379317,8.539525,1.529963,2.346989],[0.094608,-8.929655,-5.083561,9.149987],[-8.410434,-8.708605,-5.666805,-1.016430],[-9.956033,-4.194527,9.667490,6.072305],[3.600000,-6.992301,0.684488,-1.303396],[8.418307,-4.725447,4.427591,8.721285],[9.755097,1.783386,5.788030,7.434203],[7.013018,-4.499127,-4.048966,-7.378305],[3.310650,6.180626,-3.488574,2.832264],[-4.371399,2.777029,8.456818,7.478972],[0.956553,-5.467098,-6.763796,-7.528327],[8.222780,5.208782,-3.978983,7.759365],[-5.419966,0.714779,8.767980,-4.553029],[-0.976889,9.120188,6.828947,-0.314209],[6.191420,5.461479,9.036614,5.477034],[4.693428,-8.878686,6.200024,7.913352],[-6.469386,-1.724710,5.871402,-1.933020],[3.008159,7.772276,-6.696570,0.437414],[-1.323333,-3.449660,-1.934865,-4.101575],[-1.620871,3.983877,4.068172,5.644791],[3.609086,3.454125,2.199496,6.449197],[6.020963,1.403966,-2.603003,4.698959],[6.558222,-6.345019,0.232990,6.846460],[-0.402732,6.111228,5.432846,1.961311],[1.416346,6.100698,-9.484840,5.965261],[3.013915,-7.044587,1.300019,-8.501889],[6.454182,-9.923717,-7.489406,-1.223736],[-8.462345,-3.694084,-1.474340,9.158735],[-7.861033,-5.990301,6.728048,-4.233171],[-2.375623,-7.308889,-2.508214,8.848073],[-0.875035,-2.078118,5.261336,9.703132],[9.711519,-9.958182,5.299419,6.906130],[-7.085584,6.904669,4.471868,7.841269],[-8.282921,4.624442,-9.831518,-8.425581],[-7.796267,3.654929,6.723172,0.618767],[-2.721820,-3.155797,4.317184,6.227188],[-9.419764,8.188056,-1.814944,7.487137],[1.205957,2.630293,1.761031,-2.348425],[8.305096,-6.375506,-8.385488,7.453777],[7.773914,-0.830565,5.016610,-6.081562],[-5.508324,6.439573,-6.455773,1.183891],[0.355446,-3.929642,-6.041061,-5.690931],[-8.332179,-5.390241,-2.584815,-1.249713],[-7.655289,2.016543,-3.924286,3.275151],[5.291287,-8.572676,7.859995,7.984208],[-6.824057,-6.352994,-5.457540,-6.283407],[4.271951,9.002600,-4.436097,0.877505],[9.035343,-2.545931,-6.959550,-6.890240],[-5.172606,-8.439188,6.976468,-7.685654],[8.152950,-2.263519,7.110734,-8.926530],[-6.490911,5.652722,5.890722,1.352725],[0.620610,2.888371,8.549067,5.040672],[-0.832800,3.754278,-4.252688,0.518982],[-9.754525,2.324280,0.370416,-3.154771],[-1.839074,-9.508323,-1.117433,-1.123862],[-1.664554,-1.186615,2.209413,4.826401],[9.626238,4.368974,4.331765,0.084346],[7.820362,5.780254,-9.497363,-7.441234],[4.574005,1.052904,-7.081485,7.746885],[6.490089,-3.904629,-8.696149,-0.572630],[-8.602385,1.128079,-3.117361,-5.016913],[5.276416,-7.245101,2.272640,-2.225660],[-7.558026,4.168109,9.782893,1.303919],[-5.151838,-2.343442,3.808375,-8.167809],[-7.427959,5.767311,-8.647509,-3.282030],[-5.416749,8.452332,1.650774,-6.485571],[5.920565,-7.572832,3.342757,0.288254],[0.788534,-7.993052,-3.163746,0.428246],[-9.087154,-4.322202,-6.283437,-4.817861],[9.191125,-3.109950,-5.037461,-3.271083],[-6.098042,-5.398388,-2.310019,7.599311],[7.554728,1.599113,-4.648823,1.154339],[4.797632,3.496817,-6.622103,-6.003916],[-4.243784,2.400061,-8.441731,-1.502802],[-4.156717,-6.688510,8.223411,9.081973],[3.060445,-5.849881,4.965616,-6.247665],[7.995988,-7.093355,5.162168,-2.153932],[4.557814,-6.268692,3.344543,3.836737],[-1.657791,6.935734,7.080467,-6.535456],[9.036086,0.338912,-4.572852,6.557419],[1.268093,-2.005757,7.752984,-6.378891],[-2.557639,-8.826032,-4.790342,7.354342],[5.745496,-9.480721,1.648624,2.856136],[6.742299,1.144320,-4.452847,-7.593388],[-3.144935,-8.934524,2.348319,0.287734],[-7.069655,8.884960,5.841282,7.565176],[7.814644,1.232230,-0.406025,6.425385],[1.295172,-1.629382,-8.678553,-2.755621],[8.802080,-9.176447,0.073711,-6.005631],[4.326000,-1.342966,-3.229005,0.990359],[5.260570,6.382568,1.692761,-9.199776],[7.476888,-4.067127,7.276914,7.680406],[6.094684,5.884184,8.166858,-0.574029],[4.672815,9.231081,-0.570946,-5.361601],[2.407219,-0.861756,-5.916161,-0.892790],[9.005093,0.650353,2.437757,8.182492],[-3.965563,9.103639,-7.581698,-2.800839],[9.632627,3.195732,-0.055855,1.533824],[6.650302,-4.556433,-2.575066,-7.475127],[1.718044,-6.828971,-4.473639,-6.922958],[-0.042423,-2.452493,1.998915,5.657358],[-8.269571,6.889618,-6.719196,-6.977786],[-1.014218,4.170433,5.770770,-3.199439],[-7.536694,4.358093,-2.232972,9.119499],[-2.729053,7.403621,5.414442,-5.734515],[0.241270,-8.867938,-9.272685,-0.939555],[-4.041087,-9.157607,4.932488,-8.313364],[0.461905,-8.169676,6.618878,5.375905],[0.175184,-9.432600,1.973937,-6.189935],[-9.700071,-2.280177,3.519011,0.910743],[-0.863976,-4.271825,-4.722539,6.757380],[-5.521474,7.915274,-3.288490,1.871182],[8.981753,-3.124016,-2.365359,8.872032],[1.333617,-5.388484,-7.615950,-6.298853],[4.143690,-1.438500,-9.373519,0.568280],[9.849528,-9.519174,3.154082,6.306213],[0.062421,0.822794,-3.518527,-8.544792],[-5.248611,7.012663,-0.194544,-4.529967],[-0.438908,1.432790,-2.638973,6.638329],[1.455483,7.177074,-0.105348,6.950172],[-5.657899,4.537687,-7.231355,2.114330],[-7.545189,8.963242,-8.848021,-7.850730],[1.421219,4.293972,8.629168,1.141326],[7.912583,2.541176,-9.583052,9.885653],[-2.040964,5.684076,1.475176,0.777256],[7.082815,-0.713602,-3.327454,-1.728024],[5.015263,-8.578577,8.847038,2.015233],[-9.451661,-5.007623,-6.074532,-3.177145],[-4.603572,6.081471,-2.630363,-2.958995],[4.669164,3.278919,6.831872,2.015473],[-8.709069,1.749106,-5.400927,-7.687007],[-0.621703,8.800433,-1.569460,6.930135],[8.693950,-4.823330,7.185570,-5.143661],[-3.247305,0.464648,3.221781,-9.370418],[-4.982044,3.124243,-2.619657,9.009196],[-3.650150,7.454171,-8.283460,-6.415825],[0.315204,4.324294,3.460999,-9.625495],[-5.492949,4.252384,-5.489299,7.098950],[-9.813669,6.502590,-6.678156,1.474434],[3.584489,1.591735,0.740546,-2.176484],[5.760697,8.283844,4.868113,-8.753407],[5.345690,6.246890,0.620271,-7.354528],[-5.324859,-0.367625,0.725877,9.969014],[4.295157,-1.465475,-7.439275,0.756842],[7.213820,-0.552852,-0.791114,-1.540547],[7.303206,-9.469181,-7.553427,-2.706443],[-3.117593,8.464818,-1.262320,9.147397],[0.638311,-3.043825,-4.958334,5.914421],[-1.709987,-8.578164,-1.093617,0.141826],[-0.905340,-6.283131,-8.142550,9.724240],[-0.570590,-4.967038,-3.151736,-5.459479],[-9.964487,4.038562,-6.102762,-1.377802],[4.188836,-0.651353,4.948407,4.950582],[3.298526,-7.645119,-6.303130,-9.325294],[-0.480731,7.364804,-3.406742,-4.410125],[-4.417173,7.607231,4.134556,0.115378],[-2.128356,-0.198596,7.662369,-8.649233],[-0.084510,7.977222,-3.515363,9.493621],[-0.117151,7.944162,-0.912673,3.027617],[-2.178126,2.454659,-5.169152,-7.302181],[-7.759305,-0.421639,-9.719101,-1.107507],[2.690567,8.413875,-9.225116,-7.120338],[8.601859,7.623622,-6.322536,-2.660294],[-3.062635,-0.014627,-3.262070,9.857263],[1.352440,8.616664,-1.094789,-5.888884],[0.902639,-5.818111,-4.175658,-0.081578],[-4.978675,2.443842,1.957561,7.734974],[-2.620664,-3.758870,-1.690555,1.397110],[-3.503121,6.577780,9.164098,-1.409804],[1.390698,-1.305951,-8.432133,3.648866],[-6.396647,8.295180,-6.965407,7.418849],[-3.645961,-8.674575,-5.050044,-3.105936],[-8.958923,8.881593,-2.664662,-2.037797],[-7.156015,3.010081,8.447153,-2.460216],[-1.183868,4.168319,-4.031916,3.656421],[3.630484,-5.262683,9.615462,-7.150438],[-1.237263,2.830215,0.959006,3.320071],[-6.217075,-8.954889,2.134684,-5.250957],[-9.730120,4.905346,-4.893435,5.255061],[-8.528750,9.277988,7.954332,5.118274],[-4.806495,-5.932352,-8.842790,5.901861],[-2.120536,-9.666955,-0.922307,0.001515],[5.428020,-1.299956,0.353966,1.814041],[8.393534,-9.595405,-3.560293,-2.551529],[-0.347858,-8.079715,-1.896344,-0.780834],[-6.260353,8.489016,6.693545,0.429341],[1.636933,-2.469793,-4.426161,-7.494942],[3.727134,-5.321415,-5.078687,-4.503072],[0.402317,7.616947,-3.645578,-7.233093],[-4.766113,-2.857150,0.942845,-7.536570],[3.879102,7.228271,-1.622085,9.327417],[-6.279921,2.374175,-5.992772,-6.718540],[6.349503,-1.672383,5.268496,-3.786471],[-5.498501,1.323574,-8.370472,-5.337099],[-5.541209,4.189015,4.615796,-4.081162],[-2.275521,-6.272859,5.880609,-6.057282],[-6.675162,6.590856,-0.131370,1.089637],[-9.385720,-9.575226,3.939706,-6.324862],[-5.069558,-8.722657,-0.829197,-5.087169],[9.054126,1.639925,2.466481,4.075472],[-7.906787,4.492434,-1.866882,1.496644],[2.992072,8.565247,-4.896894,-9.596757],[-0.090723,-9.972379,-3.879083,2.946584],[8.672628,-8.666138,0.147433,-0.614327],[-3.223290,-9.063898,8.916901,6.987238],[4.240416,6.554105,-4.519095,-1.177112],[-2.359629,1.269094,0.728356,-2.946847],[-4.798845,3.262187,-2.334719,6.706652],[1.421260,1.747635,-2.027913,4.000284],[-7.288602,4.870596,9.090402,2.400980],[6.022744,-3.659010,2.768196,0.375648],[1.405887,2.094953,3.349253,3.551084],[-8.051070,3.662405,5.381582,-0.658126],[8.288032,6.165872,-1.634220,-8.377252],[6.645386,-2.233470,-4.429186,-4.007173],[4.952385,0.775023,2.114364,0.856626],[-2.899811,-4.193954,-4.848300,3.768900],[-9.930516,-5.770947,1.611891,-7.262292],[2.799853,6.965135,9.894031,8.706061],[-1.948287,2.313393,0.121910,0.252179],[1.406408,-4.242316,2.123337,2.288545],[-0.377530,-0.981828,-9.744090,-7.322266],[7.115288,5.150459,-9.841841,9.366468],[-0.079923,-4.611466,-0.008249,4.591382],[8.078669,4.376756,0.147263,-0.693357],[-6.578390,6.333881,-1.377315,-7.120149],[1.146934,-8.403137,-6.213944,-7.509626],[-7.147054,8.876112,3.351140,-9.750360],[-2.176897,6.833715,-6.769449,5.774589],[-1.750757,1.948752,-1.926201,-7.107059],[-9.665319,1.713048,1.033171,4.787569],[-7.898710,-1.971046,6.499680,-4.351623],[-4.420426,1.209384,-9.094465,5.057476],[9.140484,9.967366,-1.863529,2.157156],[-2.798372,9.062029,6.549865,6.314897],[7.572585,1.492007,-4.409400,-5.099529],[6.348716,2.229289,-6.800492,-9.282752],[9.126893,-3.815380,9.208519,-2.067719],[-3.336179,5.872441,-7.250819,-7.789719],[-5.246709,-3.711169,7.481230,9.797539],[-9.044066,-1.470929,9.572454,-0.648136],[-9.658052,-0.445426,0.875616,1.078922],[3.280874,4.397890,7.569590,2.838078],[0.662608,-1.927897,5.183344,8.742562],[-2.323173,-9.465210,-7.902971,5.117951],[1.802145,-7.737802,-2.285435,0.432995],[4.914933,-6.941447,-8.185855,-6.573546],[2.556524,-8.276760,0.991664,6.509329],[-4.405922,3.649356,-0.102660,1.780559],[6.227721,-5.541780,-1.986075,5.706712],[-2.272733,-5.204685,4.543815,-7.542911],[-9.829873,1.436297,-2.890428,5.570450],[8.649862,7.547770,5.506557,5.229665],[9.285038,9.632131,9.765676,1.106058],[-4.601131,-4.750668,-2.538938,-1.479380],[-3.676904,-3.188250,-7.519817,5.621849],[8.850406,-2.199550,7.619584,0.960989],[2.561027,-7.471081,8.585374,0.217016],[-8.159189,1.989039,-7.945646,4.710426],[-6.983085,-9.030133,7.166329,-8.228668],[-6.241637,-0.600004,-5.546536,-9.783399],[-7.897387,9.398638,-3.972961,5.361146],[-2.004880,-6.599372,-4.742631,6.199802],[1.660986,-7.780226,5.507998,2.701947],[6.643766,-1.114161,3.042428,6.904779],[4.172818,9.968902,4.605727,-0.860724],[-5.274027,2.204516,-0.653520,7.644966],[-7.062409,0.246485,-2.886037,3.614252],[-4.384802,3.817647,3.632444,8.882997],[2.769285,-3.063539,5.963610,5.925855],[1.686737,-4.029108,5.283309,-6.966458]], dtype = "float64")#candidate|7501|(960, 4)|const|float64
call_7499 = relay.TupleGetItem(func_2426_call(relay.reshape(var_7500.astype('float32'), [360,]), relay.reshape(const_7501.astype('float64'), [15, 16, 16]), ), 5)
call_7502 = relay.TupleGetItem(func_2429_call(relay.reshape(var_7500.astype('float32'), [360,]), relay.reshape(const_7501.astype('float64'), [15, 16, 16]), ), 5)
output = relay.Tuple([call_7483,call_7497,call_7499,var_7500,const_7501,])
output2 = relay.Tuple([call_7484,call_7498,call_7502,var_7500,const_7501,])
func_7529 = relay.Function([var_7500,], output)
mod['func_7529'] = func_7529
mod = relay.transform.InferType()(mod)
var_7530 = relay.var("var_7530", dtype = "float32", shape = (36, 10))#candidate|7530|(36, 10)|var|float32
output = func_7529(var_7530)
func_7531 = relay.Function([var_7530], output)
mutated_mod['func_7531'] = func_7531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
call_7558 = relay.TupleGetItem(func_1650_call(), 1)
call_7559 = relay.TupleGetItem(func_1652_call(), 1)
func_1524_call = mod.get_global_var('func_1524')
func_1525_call = mutated_mod.get_global_var('func_1525')
call_7560 = relay.TupleGetItem(func_1524_call(), 0)
call_7561 = relay.TupleGetItem(func_1525_call(), 0)
func_5464_call = mod.get_global_var('func_5464')
func_5468_call = mutated_mod.get_global_var('func_5468')
var_7567 = relay.var("var_7567", dtype = "float64", shape = (990,))#candidate|7567|(990,)|var|float64
call_7566 = func_5464_call(relay.reshape(var_7567.astype('float64'), [15, 11, 6]), relay.reshape(var_7567.astype('float64'), [15, 11, 6]), )
call_7568 = func_5464_call(relay.reshape(var_7567.astype('float64'), [15, 11, 6]), relay.reshape(var_7567.astype('float64'), [15, 11, 6]), )
bop_7573 = relay.maximum(call_7560.astype('uint8'), relay.reshape(call_7558.astype('uint8'), relay.shape_of(call_7560))) # shape=(15, 1, 16)
bop_7576 = relay.maximum(call_7561.astype('uint8'), relay.reshape(call_7559.astype('uint8'), relay.shape_of(call_7561))) # shape=(15, 1, 16)
output = relay.Tuple([call_7566,var_7567,bop_7573,])
output2 = relay.Tuple([call_7568,var_7567,bop_7576,])
func_7578 = relay.Function([var_7567,], output)
mod['func_7578'] = func_7578
mod = relay.transform.InferType()(mod)
var_7579 = relay.var("var_7579", dtype = "float64", shape = (990,))#candidate|7579|(990,)|var|float64
output = func_7578(var_7579)
func_7580 = relay.Function([var_7579], output)
mutated_mod['func_7580'] = func_7580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6255_call = mod.get_global_var('func_6255')
func_6256_call = mutated_mod.get_global_var('func_6256')
call_7622 = func_6255_call()
call_7623 = func_6255_call()
func_3242_call = mod.get_global_var('func_3242')
func_3244_call = mutated_mod.get_global_var('func_3244')
var_7633 = relay.var("var_7633", dtype = "float64", shape = (396,))#candidate|7633|(396,)|var|float64
call_7632 = func_3242_call(relay.reshape(var_7633.astype('float64'), [3, 11, 12]))
call_7634 = func_3242_call(relay.reshape(var_7633.astype('float64'), [3, 11, 12]))
bop_7655 = relay.divide(call_7632.astype('float64'), relay.reshape(var_7633.astype('float64'), relay.shape_of(call_7632))) # shape=(3, 11, 12)
bop_7658 = relay.divide(call_7634.astype('float64'), relay.reshape(var_7633.astype('float64'), relay.shape_of(call_7634))) # shape=(3, 11, 12)
uop_7682 = relay.exp(call_7632.astype('float32')) # shape=(3, 11, 12)
uop_7684 = relay.exp(call_7634.astype('float32')) # shape=(3, 11, 12)
output = relay.Tuple([call_7622,bop_7655,uop_7682,])
output2 = relay.Tuple([call_7623,bop_7658,uop_7684,])
func_7690 = relay.Function([var_7633,], output)
mod['func_7690'] = func_7690
mod = relay.transform.InferType()(mod)
var_7691 = relay.var("var_7691", dtype = "float64", shape = (396,))#candidate|7691|(396,)|var|float64
output = func_7690(var_7691)
func_7692 = relay.Function([var_7691], output)
mutated_mod['func_7692'] = func_7692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6255_call = mod.get_global_var('func_6255')
func_6256_call = mutated_mod.get_global_var('func_6256')
call_7742 = func_6255_call()
call_7743 = func_6255_call()
func_4895_call = mod.get_global_var('func_4895')
func_4896_call = mutated_mod.get_global_var('func_4896')
call_7747 = func_4895_call()
call_7748 = func_4895_call()
func_4107_call = mod.get_global_var('func_4107')
func_4108_call = mutated_mod.get_global_var('func_4108')
call_7760 = relay.TupleGetItem(func_4107_call(), 0)
call_7761 = relay.TupleGetItem(func_4108_call(), 0)
func_6139_call = mod.get_global_var('func_6139')
func_6140_call = mutated_mod.get_global_var('func_6140')
call_7772 = relay.TupleGetItem(func_6139_call(), 3)
call_7773 = relay.TupleGetItem(func_6140_call(), 3)
func_2632_call = mod.get_global_var('func_2632')
func_2634_call = mutated_mod.get_global_var('func_2634')
call_7778 = relay.TupleGetItem(func_2632_call(), 0)
call_7779 = relay.TupleGetItem(func_2634_call(), 0)
func_1195_call = mod.get_global_var('func_1195')
func_1197_call = mutated_mod.get_global_var('func_1197')
var_7785 = relay.var("var_7785", dtype = "float64", shape = (300, 12))#candidate|7785|(300, 12)|var|float64
call_7784 = relay.TupleGetItem(func_1195_call(relay.reshape(var_7785.astype('float64'), [15, 15, 16])), 2)
call_7786 = relay.TupleGetItem(func_1197_call(relay.reshape(var_7785.astype('float64'), [15, 15, 16])), 2)
output = relay.Tuple([call_7742,call_7747,call_7760,call_7772,call_7778,call_7784,var_7785,])
output2 = relay.Tuple([call_7743,call_7748,call_7761,call_7773,call_7779,call_7786,var_7785,])
func_7807 = relay.Function([var_7785,], output)
mod['func_7807'] = func_7807
mod = relay.transform.InferType()(mod)
var_7808 = relay.var("var_7808", dtype = "float64", shape = (300, 12))#candidate|7808|(300, 12)|var|float64
output = func_7807(var_7808)
func_7809 = relay.Function([var_7808], output)
mutated_mod['func_7809'] = func_7809
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7828 = relay.const([[[9,-9,-9,-4,-6,6],[10,3,1,6,10,4],[-8,6,10,-7,2,-6],[6,-7,-2,6,-5,9],[10,-7,-7,-10,-8,10],[-2,8,5,-4,6,3]],[[4,-10,-8,-4,6,7],[-4,8,-5,1,7,3],[5,-5,9,-9,-9,2],[1,4,-9,9,-7,-5],[-5,-2,-6,-6,-2,-2],[-9,4,1,5,-3,-7]],[[9,-4,-3,9,-5,-10],[-5,2,7,8,4,-6],[-9,-6,8,-5,-1,3],[7,-4,2,5,-10,7],[-8,5,-9,4,-10,10],[-6,-4,1,-3,-9,3]],[[10,-3,3,-8,-6,-3],[-4,1,-9,-1,-4,-6],[-4,7,5,-7,10,-5],[-9,-5,8,10,-7,7],[1,-3,-4,-4,-7,2],[-3,-6,10,-7,6,5]],[[-10,-7,5,-4,-9,3],[-7,2,8,-5,6,3],[5,-6,-1,-5,4,-9],[4,-5,-2,10,5,-3],[-7,-3,2,-8,7,-9],[5,-1,-8,9,-4,8]],[[-5,5,-10,5,7,-2],[-6,-9,6,-1,-2,3],[-3,-1,-9,4,7,3],[6,-7,-6,5,1,4],[1,-10,10,-2,-6,-1],[-4,-8,-2,6,-9,-4]],[[-2,-8,2,10,-9,-6],[-6,1,3,-4,7,-6],[2,-9,-7,-5,-10,3],[7,5,6,3,10,-1],[-8,-8,8,3,7,1],[3,-4,3,6,1,-3]],[[3,-8,-2,5,-7,-4],[-6,4,-9,9,5,8],[1,5,7,10,8,4],[8,-1,-2,-9,-1,4],[-10,-3,-6,-4,-7,10],[8,6,7,-5,1,9]],[[10,2,3,-5,-8,-9],[-1,1,1,-4,3,-7],[3,-5,-10,8,4,-3],[-5,-9,9,9,-10,-10],[4,-4,-5,7,-2,2],[9,-4,-1,10,-7,1]],[[7,-6,10,10,1,1],[2,3,10,-8,7,-2],[8,6,-10,-1,-7,-4],[4,-3,7,-10,3,4],[1,4,3,6,-7,7],[9,6,5,-5,3,4]]], dtype = "int64")#candidate|7828|(10, 6, 6)|const|int64
const_7829 = relay.const([[[-3,7,2,-7,-7,7],[1,-2,-5,5,5,-5],[7,8,8,-9,-8,9],[10,-5,10,1,-1,8],[-1,5,-5,2,-6,6],[-2,4,-5,8,-9,-4]],[[-6,-4,-7,10,-5,6],[7,-10,10,8,-4,10],[5,7,-4,5,-6,-6],[1,-3,-2,6,8,-2],[-1,2,5,5,3,-6],[-2,6,9,-3,7,9]],[[-6,7,-9,2,-1,9],[8,8,7,6,-4,-9],[4,3,9,-9,7,7],[-8,9,-5,7,-2,3],[-6,9,3,3,2,-7],[10,-4,-5,-4,-1,-4]],[[1,8,-6,-3,1,-2],[-1,-2,-3,-2,8,-1],[-6,-5,9,-3,-1,-6],[-3,-1,2,-1,-10,-6],[1,-9,3,-1,6,5],[-5,6,1,-5,10,1]],[[1,4,2,-8,7,3],[7,8,1,-1,-6,-4],[-8,1,7,1,-1,-1],[3,9,7,10,7,-9],[5,-7,-6,6,-2,-3],[9,8,9,7,1,3]],[[-10,-3,-3,9,4,-7],[-9,-6,3,1,-3,4],[-10,-3,-6,10,9,7],[8,10,-10,-2,-1,1],[10,-6,2,-3,10,5],[2,6,-9,-3,-6,8]],[[-9,6,-3,-4,10,-3],[1,-5,4,8,5,9],[-6,-2,-3,-2,-3,2],[7,8,-7,8,-9,-10],[-4,10,4,-3,2,-5],[-8,-7,7,-8,7,-10]],[[6,-2,-2,9,3,-5],[-1,-9,6,7,-3,6],[4,-4,9,-5,3,-2],[-2,-9,2,-3,-4,5],[-8,-3,-9,-3,-2,-5],[-1,6,10,9,8,-10]],[[-3,3,-5,9,-3,6],[-3,6,-4,-6,1,-10],[-9,4,6,8,-5,7],[1,5,8,7,-8,7],[-2,-8,-7,4,5,5],[-2,-3,6,-8,5,3]],[[5,-7,1,-5,-8,-5],[-1,-1,7,-10,-1,-5],[-4,-5,8,-4,-8,-4],[-8,-3,5,-1,7,5],[-10,-2,-9,-9,1,1],[4,2,10,-2,-6,5]]], dtype = "int64")#candidate|7829|(10, 6, 6)|const|int64
bop_7830 = relay.subtract(const_7828.astype('int64'), relay.reshape(const_7829.astype('int64'), relay.shape_of(const_7828))) # shape=(10, 6, 6)
uop_7836 = relay.cos(bop_7830.astype('float32')) # shape=(10, 6, 6)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_7853 = func_1417_call()
call_7854 = func_1417_call()
func_4752_call = mod.get_global_var('func_4752')
func_4754_call = mutated_mod.get_global_var('func_4754')
var_7863 = relay.var("var_7863", dtype = "float64", shape = (2640,))#candidate|7863|(2640,)|var|float64
call_7862 = relay.TupleGetItem(func_4752_call(relay.reshape(var_7863.astype('float64'), [132, 20])), 1)
call_7864 = relay.TupleGetItem(func_4754_call(relay.reshape(var_7863.astype('float64'), [132, 20])), 1)
func_6845_call = mod.get_global_var('func_6845')
func_6846_call = mutated_mod.get_global_var('func_6846')
call_7885 = func_6845_call()
call_7886 = func_6845_call()
bop_7894 = relay.less(uop_7836.astype('bool'), relay.reshape(const_7828.astype('bool'), relay.shape_of(uop_7836))) # shape=(10, 6, 6)
output = relay.Tuple([call_7853,call_7862,var_7863,call_7885,bop_7894,])
output2 = relay.Tuple([call_7854,call_7864,var_7863,call_7886,bop_7894,])
func_7901 = relay.Function([var_7863,], output)
mod['func_7901'] = func_7901
mod = relay.transform.InferType()(mod)
var_7902 = relay.var("var_7902", dtype = "float64", shape = (2640,))#candidate|7902|(2640,)|var|float64
output = func_7901(var_7902)
func_7903 = relay.Function([var_7902], output)
mutated_mod['func_7903'] = func_7903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7944 = relay.var("var_7944", dtype = "float64", shape = (4, 1, 15))#candidate|7944|(4, 1, 15)|var|float64
uop_7945 = relay.sinh(var_7944.astype('float64')) # shape=(4, 1, 15)
func_3026_call = mod.get_global_var('func_3026')
func_3029_call = mutated_mod.get_global_var('func_3029')
var_7953 = relay.var("var_7953", dtype = "float64", shape = (2, 1320))#candidate|7953|(2, 1320)|var|float64
call_7952 = relay.TupleGetItem(func_3026_call(relay.reshape(var_7953.astype('float64'), [15, 11, 16])), 0)
call_7954 = relay.TupleGetItem(func_3029_call(relay.reshape(var_7953.astype('float64'), [15, 11, 16])), 0)
output = relay.Tuple([uop_7945,call_7952,var_7953,])
output2 = relay.Tuple([uop_7945,call_7954,var_7953,])
func_7956 = relay.Function([var_7944,var_7953,], output)
mod['func_7956'] = func_7956
mod = relay.transform.InferType()(mod)
var_7957 = relay.var("var_7957", dtype = "float64", shape = (4, 1, 15))#candidate|7957|(4, 1, 15)|var|float64
var_7958 = relay.var("var_7958", dtype = "float64", shape = (2, 1320))#candidate|7958|(2, 1320)|var|float64
output = func_7956(var_7957,var_7958,)
func_7959 = relay.Function([var_7957,var_7958,], output)
mutated_mod['func_7959'] = func_7959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_7983 = relay.TupleGetItem(func_1561_call(), 0)
call_7984 = relay.TupleGetItem(func_1563_call(), 0)
var_8001 = relay.var("var_8001", dtype = "float64", shape = (15, 7, 16))#candidate|8001|(15, 7, 16)|var|float64
bop_8002 = relay.bitwise_or(call_7983.astype('uint8'), var_8001.astype('uint8')) # shape=(15, 7, 16)
bop_8005 = relay.bitwise_or(call_7984.astype('uint8'), var_8001.astype('uint8')) # shape=(15, 7, 16)
output = relay.Tuple([bop_8002,])
output2 = relay.Tuple([bop_8005,])
func_8008 = relay.Function([var_8001,], output)
mod['func_8008'] = func_8008
mod = relay.transform.InferType()(mod)
mutated_mod['func_8008'] = func_8008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8009 = relay.var("var_8009", dtype = "float64", shape = (15, 7, 16))#candidate|8009|(15, 7, 16)|var|float64
func_8008_call = mutated_mod.get_global_var('func_8008')
call_8010 = func_8008_call(var_8009)
output = call_8010
func_8011 = relay.Function([var_8009], output)
mutated_mod['func_8011'] = func_8011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_8040 = func_3060_call()
call_8041 = func_3060_call()
func_4708_call = mod.get_global_var('func_4708')
func_4709_call = mutated_mod.get_global_var('func_4709')
call_8047 = relay.TupleGetItem(func_4708_call(), 1)
call_8048 = relay.TupleGetItem(func_4709_call(), 1)
output = relay.Tuple([call_8040,call_8047,])
output2 = relay.Tuple([call_8041,call_8048,])
func_8049 = relay.Function([], output)
mod['func_8049'] = func_8049
mod = relay.transform.InferType()(mod)
mutated_mod['func_8049'] = func_8049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8049_call = mutated_mod.get_global_var('func_8049')
call_8050 = func_8049_call()
output = call_8050
func_8051 = relay.Function([], output)
mutated_mod['func_8051'] = func_8051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8049_call = mod.get_global_var('func_8049')
func_8051_call = mutated_mod.get_global_var('func_8051')
call_8068 = relay.TupleGetItem(func_8049_call(), 0)
call_8069 = relay.TupleGetItem(func_8051_call(), 0)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_8072 = relay.TupleGetItem(func_2034_call(), 1)
call_8073 = relay.TupleGetItem(func_2035_call(), 1)
func_7334_call = mod.get_global_var('func_7334')
func_7336_call = mutated_mod.get_global_var('func_7336')
call_8088 = func_7334_call()
call_8089 = func_7334_call()
var_8093 = relay.var("var_8093", dtype = "float64", shape = (15, 13, 16))#candidate|8093|(15, 13, 16)|var|float64
bop_8094 = relay.equal(call_8088.astype('bool'), var_8093.astype('bool')) # shape=(15, 13, 16)
bop_8097 = relay.equal(call_8089.astype('bool'), var_8093.astype('bool')) # shape=(15, 13, 16)
func_1872_call = mod.get_global_var('func_1872')
func_1873_call = mutated_mod.get_global_var('func_1873')
call_8100 = relay.TupleGetItem(func_1872_call(), 3)
call_8101 = relay.TupleGetItem(func_1873_call(), 3)
func_2593_call = mod.get_global_var('func_2593')
func_2594_call = mutated_mod.get_global_var('func_2594')
call_8104 = relay.TupleGetItem(func_2593_call(), 0)
call_8105 = relay.TupleGetItem(func_2594_call(), 0)
func_4783_call = mod.get_global_var('func_4783')
func_4785_call = mutated_mod.get_global_var('func_4785')
call_8126 = relay.TupleGetItem(func_4783_call(), 0)
call_8127 = relay.TupleGetItem(func_4785_call(), 0)
output = relay.Tuple([call_8068,call_8072,bop_8094,call_8100,call_8104,call_8126,])
output2 = relay.Tuple([call_8069,call_8073,bop_8097,call_8101,call_8105,call_8127,])
func_8136 = relay.Function([var_8093,], output)
mod['func_8136'] = func_8136
mod = relay.transform.InferType()(mod)
var_8137 = relay.var("var_8137", dtype = "float64", shape = (15, 13, 16))#candidate|8137|(15, 13, 16)|var|float64
output = func_8136(var_8137)
func_8138 = relay.Function([var_8137], output)
mutated_mod['func_8138'] = func_8138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_8155 = relay.TupleGetItem(func_4154_call(), 0)
call_8156 = relay.TupleGetItem(func_4155_call(), 0)
func_5824_call = mod.get_global_var('func_5824')
func_5826_call = mutated_mod.get_global_var('func_5826')
call_8161 = relay.TupleGetItem(func_5824_call(), 2)
call_8162 = relay.TupleGetItem(func_5826_call(), 2)
func_6458_call = mod.get_global_var('func_6458')
func_6460_call = mutated_mod.get_global_var('func_6460')
var_8171 = relay.var("var_8171", dtype = "float64", shape = (1440,))#candidate|8171|(1440,)|var|float64
call_8170 = relay.TupleGetItem(func_6458_call(relay.reshape(var_8171.astype('float64'), [15, 6, 16])), 2)
call_8172 = relay.TupleGetItem(func_6460_call(relay.reshape(var_8171.astype('float64'), [15, 6, 16])), 2)
output = relay.Tuple([call_8155,call_8161,call_8170,var_8171,])
output2 = relay.Tuple([call_8156,call_8162,call_8172,var_8171,])
func_8176 = relay.Function([var_8171,], output)
mod['func_8176'] = func_8176
mod = relay.transform.InferType()(mod)
mutated_mod['func_8176'] = func_8176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8177 = relay.var("var_8177", dtype = "float64", shape = (1440,))#candidate|8177|(1440,)|var|float64
func_8176_call = mutated_mod.get_global_var('func_8176')
call_8178 = func_8176_call(var_8177)
output = call_8178
func_8179 = relay.Function([var_8177], output)
mutated_mod['func_8179'] = func_8179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_8196 = relay.TupleGetItem(func_2765_call(), 0)
call_8197 = relay.TupleGetItem(func_2766_call(), 0)
func_3292_call = mod.get_global_var('func_3292')
func_3295_call = mutated_mod.get_global_var('func_3295')
var_8201 = relay.var("var_8201", dtype = "uint64", shape = (1, 72))#candidate|8201|(1, 72)|var|uint64
call_8200 = relay.TupleGetItem(func_3292_call(relay.reshape(var_8201.astype('uint64'), [3, 3, 8])), 1)
call_8202 = relay.TupleGetItem(func_3295_call(relay.reshape(var_8201.astype('uint64'), [3, 3, 8])), 1)
uop_8239 = relay.exp(var_8201.astype('float32')) # shape=(1, 72)
output = relay.Tuple([call_8196,call_8200,uop_8239,])
output2 = relay.Tuple([call_8197,call_8202,uop_8239,])
func_8251 = relay.Function([var_8201,], output)
mod['func_8251'] = func_8251
mod = relay.transform.InferType()(mod)
mutated_mod['func_8251'] = func_8251
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8252 = relay.var("var_8252", dtype = "uint64", shape = (1, 72))#candidate|8252|(1, 72)|var|uint64
func_8251_call = mutated_mod.get_global_var('func_8251')
call_8253 = func_8251_call(var_8252)
output = call_8253
func_8254 = relay.Function([var_8252], output)
mutated_mod['func_8254'] = func_8254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3366_call = mod.get_global_var('func_3366')
func_3368_call = mutated_mod.get_global_var('func_3368')
call_8271 = relay.TupleGetItem(func_3366_call(), 0)
call_8272 = relay.TupleGetItem(func_3368_call(), 0)
output = relay.Tuple([call_8271,])
output2 = relay.Tuple([call_8272,])
func_8279 = relay.Function([], output)
mod['func_8279'] = func_8279
mod = relay.transform.InferType()(mod)
mutated_mod['func_8279'] = func_8279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8279_call = mutated_mod.get_global_var('func_8279')
call_8280 = func_8279_call()
output = call_8280
func_8281 = relay.Function([], output)
mutated_mod['func_8281'] = func_8281
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8354 = relay.var("var_8354", dtype = "uint64", shape = ())#candidate|8354|()|var|uint64
var_8355 = relay.var("var_8355", dtype = "uint64", shape = (3, 9, 4))#candidate|8355|(3, 9, 4)|var|uint64
bop_8356 = relay.greater(var_8354.astype('bool'), var_8355.astype('bool')) # shape=(3, 9, 4)
var_8362 = relay.var("var_8362", dtype = "bool", shape = (3, 9, 4))#candidate|8362|(3, 9, 4)|var|bool
bop_8363 = relay.logical_xor(bop_8356.astype('int64'), relay.reshape(var_8362.astype('int64'), relay.shape_of(bop_8356))) # shape=(3, 9, 4)
func_6845_call = mod.get_global_var('func_6845')
func_6846_call = mutated_mod.get_global_var('func_6846')
call_8379 = func_6845_call()
call_8380 = func_6845_call()
output = relay.Tuple([bop_8363,call_8379,])
output2 = relay.Tuple([bop_8363,call_8380,])
func_8409 = relay.Function([var_8354,var_8355,var_8362,], output)
mod['func_8409'] = func_8409
mod = relay.transform.InferType()(mod)
mutated_mod['func_8409'] = func_8409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8409_call = mutated_mod.get_global_var('func_8409')
var_8411 = relay.var("var_8411", dtype = "uint64", shape = ())#candidate|8411|()|var|uint64
var_8412 = relay.var("var_8412", dtype = "uint64", shape = (3, 9, 4))#candidate|8412|(3, 9, 4)|var|uint64
var_8413 = relay.var("var_8413", dtype = "bool", shape = (3, 9, 4))#candidate|8413|(3, 9, 4)|var|bool
call_8410 = func_8409_call(var_8411,var_8412,var_8413,)
output = call_8410
func_8414 = relay.Function([var_8411,var_8412,var_8413,], output)
mutated_mod['func_8414'] = func_8414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7393_call = mod.get_global_var('func_7393')
func_7395_call = mutated_mod.get_global_var('func_7395')
call_8431 = relay.TupleGetItem(func_7393_call(), 0)
call_8432 = relay.TupleGetItem(func_7395_call(), 0)
output = call_8431
output2 = call_8432
func_8484 = relay.Function([], output)
mod['func_8484'] = func_8484
mod = relay.transform.InferType()(mod)
mutated_mod['func_8484'] = func_8484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8484_call = mutated_mod.get_global_var('func_8484')
call_8485 = func_8484_call()
output = call_8485
func_8486 = relay.Function([], output)
mutated_mod['func_8486'] = func_8486
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8516 = relay.const([[[-6.513990,-0.818039,7.367987,-8.833498,2.920191,6.447908,-9.631651,2.709585,-6.326087],[-1.123122,-2.537884,6.511310,-5.765465,-7.312007,-8.543869,7.622558,9.660083,-6.367175],[-3.806690,9.172738,7.777077,-6.647786,6.457452,1.307998,-4.390035,1.634214,-3.737202],[-3.534446,-2.742478,6.804981,-4.581315,0.051436,-9.952742,-5.111388,-7.087568,-8.259234],[0.053370,-1.172003,4.122715,-7.860558,3.359383,-6.948695,-3.300138,-6.513095,5.630967],[1.241208,-2.976264,5.144953,-5.536652,0.251934,5.221804,-9.243531,-1.025930,-9.772241],[-8.432451,-3.772754,-5.958418,-5.538232,2.646629,9.939981,-6.860801,-5.264487,8.647669],[5.056026,-3.501848,-1.641218,8.433429,-2.948221,3.918923,6.678293,1.489821,8.794897],[-5.603619,-7.572555,8.136358,-4.709894,-0.593708,-6.981008,0.224796,4.668490,8.762095],[1.521963,3.434260,-8.510040,-8.320798,-4.853231,2.269867,3.515669,5.675392,1.495816]],[[3.357888,-6.176374,4.473347,2.322400,0.831497,-5.947382,9.824162,2.628643,6.693645],[2.416707,6.122891,5.302732,-2.790677,-1.128487,-3.336285,-1.404841,2.494737,6.307957],[3.401610,2.168677,1.947515,1.793923,-0.411259,9.327271,4.503529,6.762074,4.012424],[3.253739,-6.131470,0.459564,-1.205248,-8.929691,7.705770,-8.144224,2.535024,9.187422],[8.755755,2.540377,5.942157,8.517340,5.225611,9.717443,7.640999,-3.446823,-0.052757],[-8.621373,9.337745,-6.641974,-2.110402,-1.066023,8.706328,-5.618972,-5.464032,-7.626686],[8.571903,-6.791397,-6.264003,7.286398,8.270568,9.021170,6.849884,-9.661889,0.893814],[9.919690,1.489544,7.569546,6.516901,9.786853,0.844509,2.558836,8.091459,3.837746],[3.190219,6.244221,9.545522,-6.755251,-2.148665,7.953357,-7.751811,5.495353,-8.936768],[-2.967618,-0.777019,-5.017814,6.737331,-4.746166,5.952212,-6.249134,-6.056802,2.648135]],[[5.530806,9.737693,-2.279851,9.693466,3.635957,-1.843839,9.732079,-3.458999,-6.741121],[9.544686,-8.791287,-2.047542,5.303650,4.903891,-5.918239,7.497186,-7.956829,6.583890],[-0.309124,7.039294,7.915203,0.162040,-1.283313,2.919629,-2.393002,-4.982483,-0.300574],[4.442634,-5.095087,-4.481647,0.279691,-3.474557,-6.292219,3.855557,-0.623687,-5.805501],[-3.069771,-4.156999,0.461323,-9.078998,-5.997663,3.404212,5.597031,-8.170886,3.669972],[4.202780,0.597014,-0.858076,9.098500,-6.499619,0.872072,-1.621282,-4.485364,-9.663146],[-7.449829,-1.008379,-9.516973,0.328917,-1.299010,9.675875,-2.177307,-3.843029,-7.413968],[7.907206,-0.009843,8.267097,5.723956,-3.828122,-9.475235,6.617983,1.443045,6.961284],[9.229025,6.559820,-2.170738,0.157429,8.777023,-7.085398,2.453513,-2.074826,6.035879],[6.044474,8.672525,6.652540,-0.109769,-1.384123,-5.559165,6.053388,-1.214035,6.525952]],[[0.692729,-4.006379,-8.410512,-0.916620,-6.699123,-6.395544,-1.741078,-7.267670,2.077056],[9.792019,7.092342,7.319449,7.474655,5.470269,4.411071,4.349969,-7.819809,-1.326217],[-9.017898,-1.885116,1.449685,1.840627,-4.942889,1.023165,8.783956,5.179227,-6.634027],[-8.905345,-4.402850,0.538694,-8.710239,-3.657985,-3.956605,5.614053,-0.412223,-8.293252],[-0.561217,4.055252,2.156474,-2.330100,-7.121739,6.969386,-6.908593,-5.498042,-6.533688],[1.032417,-1.494234,6.946276,-1.526026,-8.242095,-2.952103,-9.383309,-0.435013,3.028799],[-0.752421,-3.462362,0.018466,5.533157,0.249528,-5.804149,6.978076,-7.551636,-5.659398],[0.538969,-8.483818,2.713063,-6.918168,-7.552133,1.950152,-1.018135,5.467525,-6.980357],[2.670763,7.242295,-2.526224,-1.822476,8.211924,6.644983,-8.345738,-5.898731,-4.525976],[5.727741,8.902745,1.281688,7.316248,-5.272517,-6.865078,4.434317,-6.183275,-9.028697]],[[4.961819,-2.270163,7.351592,-2.564179,-1.286193,5.938767,-0.065614,6.699362,-2.832637],[-9.747184,8.659627,-9.629407,-0.847721,2.570359,-2.806252,6.770794,-8.536997,-6.423710],[1.974314,7.906887,0.514239,0.068926,0.618683,4.709400,8.658226,6.019544,-4.149210],[6.958971,6.084031,8.299287,-3.283085,2.986716,7.727557,4.034822,-5.048800,-0.621893],[3.182172,1.755465,1.476609,-2.892826,3.511394,4.714336,5.539743,-5.797327,9.631549],[4.561008,-9.428560,-7.667577,-9.844210,-0.067279,-3.988627,3.364831,-3.038539,-6.439377],[2.524369,8.294190,-9.683266,3.461704,3.713420,-1.018317,4.560223,-3.659525,1.954889],[7.998744,-5.290840,-0.535023,1.427081,-7.338918,5.651024,5.299035,1.504551,5.879077],[1.726277,-8.864249,-6.481085,3.500754,-3.016265,7.989853,-5.355919,0.283843,-6.147559],[6.503418,8.131673,-3.321625,-1.424651,-7.367939,-8.978915,7.267254,-4.955931,-7.266091]],[[-8.730518,-5.191814,5.937595,-3.443176,6.194443,9.490128,-7.316586,7.570607,-4.557984],[-3.969880,4.590775,1.145619,-2.038706,9.608752,-1.106509,3.963587,1.492182,8.916499],[2.480302,-9.027714,7.441597,-9.756131,-7.359112,-0.770586,5.313872,6.050359,6.355521],[-3.204286,5.798310,-6.969815,2.885680,-1.495974,7.110222,-4.928574,-9.941117,4.691797],[-1.164098,4.727210,3.386860,0.330916,-0.884786,6.355003,8.930120,8.257585,6.890925],[-8.008082,5.581308,7.285850,-4.899909,5.279175,-5.180987,6.645238,-8.219920,5.721005],[-0.473917,0.511259,2.118798,-3.770379,-6.225497,9.608777,9.844240,3.238826,9.265072],[8.317841,-6.456062,-0.793237,-1.373630,9.143625,-7.476229,-8.126450,5.401909,2.348313],[3.607584,-6.439437,5.413200,2.326029,7.156307,0.231447,-0.540582,5.019249,3.090710],[8.602013,9.893633,-3.508943,-3.271811,-9.881149,-1.710514,-9.000652,6.934373,-9.253986]],[[7.056752,9.986762,-6.806431,5.415554,1.388884,6.303924,-2.154306,-9.931601,4.948561],[3.267085,-8.211522,1.514272,2.060277,-8.975967,-5.562574,9.051159,-5.747419,8.567436],[5.784886,3.448407,5.165727,8.648063,-6.920465,0.067104,-2.404661,6.141539,-6.104803],[-3.743787,-9.246567,-4.165483,0.701596,-7.565135,-3.889146,-8.377096,-4.990077,-2.417837],[-6.208801,6.173065,-1.137648,-1.234742,2.887639,2.091349,-4.731574,7.381347,-0.183786],[-0.679556,3.385731,7.617617,-4.747081,4.549725,-5.867767,-0.196974,0.250691,0.281388],[-3.319457,4.935683,0.857779,4.130625,-5.407778,-5.650590,-5.786446,-5.541960,-3.152901],[6.228957,0.362454,2.105402,-7.352810,-5.630813,-5.803184,4.752053,2.302657,-2.344832],[4.844988,-3.413512,3.640364,-2.343833,1.977788,4.673192,1.617880,-8.245853,-6.589969],[-2.334742,3.966355,-8.049768,-5.736440,-3.860073,-1.657655,-6.898128,-8.892171,6.626156]],[[5.740168,5.850162,-4.050638,-1.629147,8.955667,-3.945482,8.458810,1.968807,5.036500],[-6.217513,9.563016,2.676652,2.924267,-6.580850,5.998064,6.896029,4.142240,4.722664],[-4.784825,7.112610,3.048800,2.882520,-6.294596,1.541424,-4.740074,4.080029,4.461905],[-1.775006,-1.476423,-9.194006,-9.119489,6.078863,9.942201,-1.134431,-7.549264,4.872236],[8.014096,-4.255411,7.804480,-7.534859,8.882716,-7.051899,-0.070234,-5.252190,2.571624],[-0.840864,-7.769431,5.575616,7.880305,3.492302,-2.658466,5.747271,5.022513,0.246202],[2.973229,6.819875,-5.849286,1.631374,-7.332326,8.144304,0.103133,6.502899,7.996025],[5.923632,-3.360975,2.142874,5.402723,7.471767,-9.266107,-2.662560,-5.759135,6.585294],[1.657465,8.986071,-9.370896,1.840196,4.270963,2.382005,3.969993,9.355533,-7.903073],[-4.354641,9.588833,-5.053236,8.988511,0.154817,-3.784176,-5.991766,-6.970214,4.246104]],[[-9.977309,-5.224605,-8.734430,4.146265,-9.999309,3.856406,8.030533,-4.654842,5.135691],[-6.125872,9.178048,-8.463632,-5.069249,7.779505,2.853908,5.251212,5.671984,5.419547],[-5.524300,-0.992214,9.630068,5.077938,5.438894,7.478795,-8.644239,9.820164,6.349113],[-9.395956,-8.140983,-8.957581,-9.901916,-4.125385,1.482676,6.056594,-0.707379,-0.717397],[-4.830728,-0.979152,-6.185555,-3.306825,4.479612,-4.348341,-2.381642,5.285518,4.785256],[-7.706840,7.426842,8.063649,-4.696045,-5.509346,-3.721675,-1.057167,-6.167105,8.360469],[-5.735526,-0.081430,0.828866,-1.875549,7.046362,1.847169,-3.580049,-4.881075,-5.115443],[-6.504235,1.857306,8.960030,-0.682028,-3.512845,-0.931952,8.172426,1.429423,-3.187983],[-8.771809,-7.849512,-6.976830,-5.215356,8.579958,5.203700,0.843131,-5.032799,-7.213246],[-3.351132,6.392805,-0.271437,-5.060080,-6.324561,0.042984,7.059110,-1.732005,8.458442]],[[1.035356,9.240333,-3.766025,-2.856388,-8.000733,-5.703881,-8.541318,2.030431,4.894661],[3.514797,2.092541,-4.501312,-3.251352,8.936654,1.743876,-4.899084,-3.739624,-8.109393],[-1.143132,-7.200660,7.881515,8.395262,-5.903657,-2.948437,-8.776121,4.221168,7.370133],[-0.406158,4.158163,-3.352159,-4.017953,9.091811,-7.769577,-4.894436,-8.664203,-1.523030],[8.959242,4.153828,-8.847662,-4.060067,3.086462,7.581864,7.755747,6.918009,6.991965],[2.072735,-9.110177,-5.126632,-2.649502,5.261304,-7.074232,0.123646,7.124833,0.063299],[-7.184073,0.453365,9.537514,-6.569613,-5.008601,-8.489700,-6.110218,-7.898974,-2.671671],[8.810410,3.501971,-3.159085,-3.982232,3.654444,-0.747483,-7.902365,-6.810040,1.946597],[-4.145607,-3.741210,3.583666,-1.938957,7.296696,-2.242432,0.995024,-1.990961,-9.818261],[-6.804775,-2.875992,-2.968840,-4.167568,9.267702,-3.594982,2.494764,7.147813,-2.976446]]], dtype = "float32")#candidate|8516|(10, 10, 9)|const|float32
uop_8517 = relay.log(const_8516.astype('float32')) # shape=(10, 10, 9)
output = relay.Tuple([uop_8517,])
output2 = relay.Tuple([uop_8517,])
func_8521 = relay.Function([], output)
mod['func_8521'] = func_8521
mod = relay.transform.InferType()(mod)
output = func_8521()
func_8522 = relay.Function([], output)
mutated_mod['func_8522'] = func_8522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_8536 = relay.TupleGetItem(func_7106_call(), 1)
call_8537 = relay.TupleGetItem(func_7107_call(), 1)
var_8541 = relay.var("var_8541", dtype = "float64", shape = (15, 7, 16))#candidate|8541|(15, 7, 16)|var|float64
bop_8542 = relay.divide(call_8536.astype('float32'), var_8541.astype('float32')) # shape=(15, 7, 16)
bop_8545 = relay.divide(call_8537.astype('float32'), var_8541.astype('float32')) # shape=(15, 7, 16)
output = relay.Tuple([bop_8542,])
output2 = relay.Tuple([bop_8545,])
func_8547 = relay.Function([var_8541,], output)
mod['func_8547'] = func_8547
mod = relay.transform.InferType()(mod)
var_8548 = relay.var("var_8548", dtype = "float64", shape = (15, 7, 16))#candidate|8548|(15, 7, 16)|var|float64
output = func_8547(var_8548)
func_8549 = relay.Function([var_8548], output)
mutated_mod['func_8549'] = func_8549
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8568 = relay.const([[[-0.374065,-8.632363,2.586034,5.828122,6.893334,-6.212674,-8.263764,-0.056857,-5.158309,1.743796,8.414393,-3.001821],[-0.159468,-5.248701,2.495973,5.437806,-2.852170,-2.881408,2.191491,3.030709,-6.711116,-3.730341,-2.450210,-2.108359],[3.277836,3.457444,8.043477,-4.073296,-9.060029,7.301558,-1.426322,-8.912025,-7.396924,-6.221604,-5.634726,-0.748467],[0.359449,-2.712099,1.888631,-3.730347,-7.093640,-9.612924,0.738217,3.710078,4.099282,2.961778,1.328499,-5.902589],[-4.800646,1.892437,-3.982783,-5.021751,2.454736,3.140996,7.035320,4.380544,-6.914567,8.640858,-6.529111,9.803926],[5.557910,2.370843,-4.824289,3.577723,-6.130904,-6.258995,-9.745035,-0.397537,9.990225,7.599047,2.642219,-7.712974],[-6.344523,-3.711552,-0.604012,-2.057614,-2.813459,-0.661863,-0.795333,-3.214569,5.904034,0.369741,5.289102,1.692452],[-7.470907,9.189036,2.420533,4.549306,3.289565,-8.084777,8.592356,-4.398471,-6.380137,0.490399,-9.722168,7.677239],[-2.404634,5.359921,-1.660860,-1.190294,6.881164,-3.274947,5.430358,-5.002068,9.022018,-4.963788,-3.276468,2.381207],[3.076684,4.088887,-5.927126,0.822452,6.908516,-7.167658,1.268840,-8.073894,-8.194150,6.510280,-5.991003,-9.547895],[-9.272819,8.615263,1.470445,3.417200,5.983155,-5.240759,1.499232,-8.053483,6.506285,-2.224551,2.729598,5.533062],[-9.257513,2.000502,0.507230,-7.187464,-8.502335,-7.209241,-0.449732,-5.498584,-0.957226,2.248650,2.702617,-5.196335]],[[-5.851115,6.584785,-4.319557,0.768235,-7.446541,8.749299,9.763913,7.589447,1.130200,6.333329,-0.445244,9.326049],[8.018693,-6.118138,-4.846719,7.242565,-8.249308,-9.762499,1.010172,7.555311,-5.758140,1.340785,-4.745496,3.815880],[-8.321499,-9.704367,7.622415,7.273429,-9.611014,6.347634,2.117098,-3.480645,0.937735,-6.162850,-6.089977,-2.857360],[-6.375549,-8.552840,8.585673,5.705372,7.109375,-0.894054,6.531271,7.607717,4.763078,9.348378,4.251396,-7.989702],[-7.766031,0.154221,-8.041325,-8.676257,-1.942231,-5.704302,-6.956007,5.901572,1.209179,-0.676810,-9.825105,-7.703316],[-8.213832,-6.835029,4.588797,5.060534,6.031216,0.896856,-2.651396,-1.725025,-1.720708,-0.382285,-7.795800,-3.819696],[1.994117,5.965050,-2.955725,-6.147638,3.612381,-5.328043,8.259276,-2.033813,8.366242,2.509647,3.945351,-9.558367],[-9.803476,7.622356,-1.163952,-4.346424,-8.482358,8.219069,9.040747,-7.305889,-9.951251,-8.678144,-3.237427,-0.209866],[-1.091255,7.541862,-6.532183,8.270231,7.227266,2.703888,8.858249,6.703244,4.205101,-5.373854,-3.029655,9.754157],[-1.191317,9.302816,0.412218,-9.633358,1.085054,0.183449,3.878438,-5.212241,8.836524,-4.856977,5.559398,6.440073],[2.379370,1.285285,-2.435165,-8.401051,-1.376350,8.927779,-3.684174,7.131965,1.286106,3.704456,-8.035857,6.986031],[3.338846,-8.615580,-1.711699,-2.555311,7.080088,0.756641,-1.759084,-4.617451,5.283606,-6.125276,4.783539,0.139216]],[[1.047072,0.767328,-0.533311,6.035344,3.025347,-0.056465,8.284035,2.049196,3.633202,-3.302065,-1.457642,-6.931844],[-9.818450,9.824954,0.420364,2.304554,2.526072,-7.692858,9.012456,-4.198376,8.772386,-2.040593,5.712768,2.694022],[2.686600,-4.485576,4.173166,2.783393,-3.831348,5.046320,-7.038695,-7.715884,-7.279137,3.568895,-9.517824,-9.383735],[9.856303,8.285361,-7.282271,5.435885,-4.943641,2.944242,-0.259316,-5.730069,-3.773546,-4.641525,-4.150408,-8.569994],[0.739186,-3.678117,2.299718,5.825986,-9.743418,0.586359,-0.389299,-6.507539,6.059228,-5.866958,-1.906692,-1.221078],[-5.737091,7.052613,4.560164,4.907217,-5.820164,-5.102020,-0.329681,-0.167064,-8.047604,1.668697,-5.043116,-8.069890],[-4.644776,8.617406,5.143227,3.036752,0.994376,-0.337292,-2.698819,0.065007,8.216934,0.760607,-3.759269,-7.250963],[0.178746,0.943128,1.102907,5.436605,-1.539373,0.091350,-8.652587,0.124308,6.833877,-6.234819,-1.556280,-3.002819],[-0.378171,3.076124,3.294927,5.929646,-2.861371,-9.733293,-3.468589,9.647118,7.587501,-0.171901,7.537907,1.584604],[6.009766,-4.630556,9.055175,-9.375484,-0.079640,-1.286758,4.880459,2.075756,-3.185685,-4.707039,4.620258,8.921298],[-6.138433,5.911485,-6.212861,-3.675003,-4.293512,2.828597,-9.544069,4.556610,6.153489,-4.769666,-4.311611,-6.617088],[-4.784641,8.665544,-8.405216,-9.428525,3.295989,-1.361264,-6.515780,9.220182,-8.045923,-6.503368,-4.804670,3.873285]],[[-6.345919,0.601503,9.359538,4.924941,-5.069237,-0.779952,-6.167716,8.883372,-9.486671,5.464013,-9.761371,2.717338],[0.102568,8.843658,-7.549725,7.434324,7.572064,6.751256,2.803256,-9.527314,0.212539,-7.842743,7.612063,8.483833],[-8.145482,-3.883756,-2.615138,4.721373,1.809789,7.897204,9.554016,-1.696467,7.840792,-3.996485,9.310537,-1.753451],[0.223139,-0.549426,-7.466832,-8.979576,-7.632197,-5.124194,-1.080004,-2.313122,-0.903183,7.316669,-5.739105,-7.039682],[5.089284,-5.899876,0.265213,-9.849200,-1.770453,0.640764,-7.263432,4.054492,-3.892675,2.856869,2.392315,7.345892],[-6.358564,7.165768,-2.255931,-3.522127,-7.807213,-5.029781,-0.132507,-6.611283,2.772281,3.961448,1.536490,-1.250817],[-5.699881,1.404652,0.702741,-1.264351,5.135902,8.902779,3.384849,-3.708578,-8.033603,-8.777996,9.351174,3.743054],[-8.265842,-3.080279,5.382331,-5.615243,1.460641,7.942512,-2.610333,-2.326328,-0.472916,4.977681,1.953559,0.420375],[3.906706,-8.293634,4.284218,9.536287,0.843875,7.335859,1.615460,-0.104500,6.889312,2.329777,4.947578,-3.125841],[5.474644,-4.018436,4.990370,2.776981,0.986584,3.260138,4.576376,-0.667259,-9.887948,-1.485578,7.184534,-8.433954],[-1.147402,-1.096700,4.055829,5.578883,7.778955,-4.227012,-0.745314,6.402678,0.598611,-6.637833,8.968428,8.484587],[-0.481451,0.202893,1.417649,5.967164,-7.561491,6.178291,-2.933664,-3.007722,-7.916470,-3.065084,-1.847344,-4.226689]],[[-7.041811,2.152120,-0.726456,1.672551,-1.600790,-4.803643,3.940575,9.148760,-0.705413,7.800039,-5.347505,-4.231928],[-3.184952,8.468714,-2.449352,9.247552,-8.283409,-3.336201,3.914498,5.405190,9.685211,4.423668,5.483846,-1.963250],[-7.466040,-7.251015,5.606011,1.112900,8.997351,1.644728,0.057487,-2.111806,2.416550,-2.209446,5.902328,-6.272712],[2.722670,9.064094,-2.026238,-9.985635,0.968260,8.488377,7.509239,7.338209,6.376838,-8.674655,4.577309,-2.430416],[-5.535987,5.166863,9.107671,-6.655874,-1.753146,3.835292,0.117681,1.174568,3.215744,1.517407,9.754519,2.553888],[9.922670,0.557040,1.473713,9.258009,-0.563932,4.103456,-6.117708,8.956788,3.855095,-3.645987,-2.621966,8.908786],[-8.200241,5.708931,8.129855,3.922078,-6.330160,6.796282,-7.108170,0.974134,-6.310668,-7.914939,-8.941306,9.814382],[5.902224,-3.555860,5.736785,3.808769,4.009491,8.138385,0.448112,2.386259,-0.999808,1.897376,-8.346003,3.857453],[6.099585,5.783507,3.981283,3.709327,-4.350882,2.627217,-7.705532,-6.313658,2.723878,-9.664363,-9.612853,-8.756095],[2.816201,0.154372,2.929047,-8.422732,3.431274,-9.310923,-2.198176,3.536396,-9.839423,-8.210443,0.236922,-3.011076],[-0.646618,7.406880,-8.438781,0.209327,-8.581069,8.930316,-7.064869,-1.246443,-6.474628,-8.730935,1.687684,7.145811],[-7.633753,-0.232316,-1.036316,-2.970066,8.137069,8.865437,-4.204715,9.348900,-9.610800,-7.502277,-6.010729,-2.979309]],[[0.413098,7.948582,-0.737230,-7.900873,-3.062678,-5.336048,3.517097,-1.345425,-6.972543,2.444418,-0.765921,5.319045],[6.580149,6.364305,3.206681,-9.172274,6.687906,4.392669,8.543968,-3.548305,-9.772273,-9.288191,-2.954786,-2.303696],[6.518189,0.595898,4.074145,-1.779549,-5.300246,-0.224945,4.518511,-4.471258,3.657291,-8.218776,-2.627312,-7.667838],[2.830362,-4.895254,0.090490,-1.621299,-1.312880,2.103939,4.337381,9.249386,8.562073,7.531411,-3.402406,1.975962],[6.967333,-2.788332,5.066358,-9.372106,-6.195407,-2.219582,3.195959,-8.128882,-0.079136,8.140616,9.585451,8.644656],[1.210471,8.736206,-0.520412,1.127391,-5.792912,2.894088,-6.825129,-4.929426,3.686469,7.437490,9.687836,-9.798364],[3.556518,7.265058,-7.532154,1.373757,8.167273,-2.507892,-5.983022,7.065116,9.310851,-3.035954,-9.854299,-5.202888],[7.351766,8.765983,1.955484,-3.724032,1.296904,3.742739,-2.336396,4.352779,0.618347,9.007358,3.748875,-6.080702],[-5.452353,9.149851,5.235222,-5.788218,1.110817,-3.004467,2.010559,5.700567,-3.844734,0.167893,7.756643,7.005355],[-0.053551,-9.088674,5.745201,-4.792709,9.463806,4.634771,-3.695604,5.218345,1.536995,-1.232384,-5.666860,6.827232],[2.237939,3.620021,-4.488184,7.974430,-2.084047,-1.150656,1.785636,2.159528,-4.580739,3.724159,-0.537426,-6.116459],[-3.307937,-9.888618,-4.989228,-0.707333,-1.374421,5.930570,-4.695075,8.171443,-2.176970,-8.940040,7.370591,7.734431]],[[-6.666921,-8.798153,7.364183,-8.724443,7.119596,8.324975,1.555189,1.877442,1.268553,-9.147770,-6.709489,-7.599515],[0.568453,-4.777061,-6.180870,8.446362,-9.533625,1.103273,-4.613163,-7.003970,7.539081,-0.721424,6.177005,-3.902353],[-6.993299,-9.665233,2.391663,1.802954,7.941924,0.852406,9.220407,5.706288,-5.127166,-5.168343,-3.043007,-1.126563],[-7.436030,-1.273003,1.892931,-9.300626,9.419480,-9.779098,-3.325583,-3.443343,6.961548,7.469201,-3.445413,-7.263921],[-5.666037,8.155265,9.612737,-4.487366,-2.273022,2.487097,2.821193,0.709622,-8.249470,0.368113,-2.703187,6.865010],[5.208203,-9.941540,9.669108,-5.825444,4.114898,-6.165396,-6.252846,-1.580112,-7.649552,-2.792024,-2.555269,-3.769485],[7.429553,9.368130,5.144351,0.190092,5.691590,-0.957401,-6.634473,-0.185746,3.649943,7.776359,3.627490,-5.336866],[1.253676,-0.151504,2.984014,3.539364,-6.203359,-5.183452,0.694628,9.816250,5.217392,2.429641,-8.065456,-3.024536],[-1.970767,1.903920,4.331608,1.431343,-1.104079,-6.484341,4.566731,-6.306504,-5.191222,8.216889,-6.509397,2.784775],[2.385619,-2.037551,-3.336654,7.946491,-6.468048,4.932299,-5.910188,-1.665277,-0.838464,-2.583439,-0.175894,6.706019],[9.692521,-1.972600,5.007570,-8.542974,-3.124987,6.376326,6.976441,-6.238507,8.567522,2.093182,-6.633608,8.186522],[6.742693,-6.827538,-6.618325,-1.682356,8.366223,-4.005883,-9.491394,5.086592,9.932266,-0.962850,2.487605,-5.017936]],[[-3.200108,-1.253169,8.488162,3.022496,-5.778100,1.156913,2.862723,-2.714333,-2.461623,-4.830412,7.305394,-9.525399],[-7.521891,3.092161,3.842904,-8.927421,-6.449129,-1.493460,-3.752404,-8.450834,-3.343879,-9.028321,1.585940,-5.477747],[3.541856,3.068221,-6.097928,5.366322,-4.259305,-9.678687,-3.544679,2.025665,1.976316,-7.775609,9.015708,-8.576112],[-4.649479,3.908022,-4.325803,-2.236658,-9.327658,-2.644675,6.222218,3.859345,2.411607,0.977540,5.478391,-6.439731],[-4.428177,-1.124696,0.699860,5.737875,5.201183,6.129320,-0.127225,5.720061,9.708974,4.602362,2.079669,-0.454671],[-5.042384,-4.228167,-5.506026,6.311349,-1.462318,-0.582773,-7.020556,4.780169,9.041394,7.808820,-7.766980,-9.809189],[7.722715,-8.090834,3.278113,2.518842,-4.579875,4.896893,-7.386522,-2.318987,-9.460222,-7.471068,-9.079933,4.875875],[-4.838548,-0.166840,1.410301,6.806393,-9.024911,-5.617236,-5.953252,-7.578719,6.617162,-8.047779,-3.652688,-8.833271],[1.387728,1.072243,0.562568,9.940750,-3.591654,-8.059111,2.579091,-2.937780,-0.619218,7.981760,-0.280140,6.233716],[4.172853,8.839132,-6.646792,-5.246303,-6.713138,-1.169825,-6.308512,9.529866,3.589645,3.677692,2.480788,-0.832746],[-3.582587,4.308054,7.817143,-2.160036,-5.641212,-0.296461,-6.012088,-1.098656,0.716646,-0.222176,3.251160,-8.190238],[2.427489,5.702572,7.225008,-4.858408,3.571280,-2.441875,1.795684,1.523577,-3.335119,-1.660143,-1.668245,0.384659]]], dtype = "float32")#candidate|8568|(8, 12, 12)|const|float32
const_8569 = relay.const([[[-6.782043,7.939184,7.008590,-2.798570,-1.406211,8.930094,0.043665,-6.239592,3.941565,-4.707535,1.489721,7.141537],[3.448517,-4.045174,8.747181,-7.559355,-7.431529,-7.942934,3.856575,-6.871271,-0.746410,-7.529200,-7.040353,5.970463],[-8.468706,-8.610617,-0.362350,-4.694647,-3.098569,-8.929008,-1.753553,0.580512,-5.473831,9.240094,-0.954621,1.559253],[6.172667,-0.564627,-3.639769,7.092724,5.245509,-8.248939,0.413455,-2.886317,-3.558027,9.057575,7.296821,4.203206],[-4.793597,8.652164,4.164948,8.444912,1.090629,-5.305331,5.137069,-4.875832,-4.549697,-2.094329,5.273249,6.074474],[1.907607,4.886856,7.541196,2.842445,1.940411,-4.420123,8.562348,7.898501,2.171771,4.978585,4.631408,3.850243],[-1.644691,-9.509945,-2.052471,0.512957,-0.763853,8.981897,-1.408819,-5.107895,6.593296,-8.199636,-3.165368,4.322811],[0.241059,6.002596,8.165918,-3.795536,-6.646538,6.109346,-1.678089,6.453456,4.747597,-4.112599,9.602358,9.680536],[2.181860,0.224536,4.249395,1.059903,4.486636,-0.971353,-8.362595,1.651646,0.239658,2.733470,4.785014,-9.257666],[6.943583,-2.282147,6.197166,-4.453037,8.931017,2.811886,-5.515505,-2.337126,7.954066,-8.451463,4.899247,-9.302052],[7.374910,9.711461,-3.619294,2.169565,-2.608530,-8.683964,-4.752949,2.343639,6.276623,-7.814593,1.928022,6.007622],[6.670351,-6.777682,7.654080,8.886320,2.922787,-6.362662,7.882937,6.549969,2.408410,1.671409,-6.346710,-4.350574]],[[7.961399,-4.282501,3.542914,8.979866,7.529408,6.267109,6.397469,3.550209,1.052883,-0.922739,-6.894100,8.177338],[-1.578112,6.578993,2.702726,-9.263293,-0.045449,9.974604,-7.065833,1.186505,8.613729,7.914656,4.436329,1.021419],[-3.182904,0.447725,7.372762,-7.280427,-8.733321,5.761792,5.433358,-7.443858,-4.212506,8.337072,1.255838,-1.842112],[-4.279665,6.843885,5.527062,-0.395471,-2.051280,-8.894264,-2.945940,0.982200,-6.081368,-7.625159,-1.101132,3.426391],[0.859239,-8.193316,3.463079,9.165131,-2.616572,-1.234692,7.493725,4.513708,-2.249267,1.340048,-7.893987,8.490168],[5.961938,4.400251,1.163426,-8.766689,8.391297,5.674743,-6.769900,-6.016769,8.448371,-4.047458,-0.606597,-8.830941],[6.385858,2.799175,3.734876,-0.413607,9.599749,-5.686104,-8.091709,0.474111,7.680186,4.215816,2.492895,-1.099125],[-5.302258,4.882926,-1.354608,6.607808,2.789353,-9.753785,-5.210629,-5.613438,-0.817700,-4.361575,1.838814,-8.292552],[-8.355955,-8.055532,-2.643318,-0.960239,2.316660,2.901340,5.606400,9.328000,2.135979,7.164219,-2.915192,5.870215],[4.241303,-9.447667,5.069936,4.025481,-5.560635,1.905933,8.959754,1.222307,6.599429,-4.986649,6.245825,-5.641422],[8.303341,-1.734100,7.319639,-1.861861,3.413409,5.095940,-3.952490,-0.186269,4.759583,0.628896,6.597419,1.548264],[6.974685,-8.046633,-4.965822,5.175339,-9.285853,1.484029,-9.951081,-1.411276,-6.524892,-6.114459,9.317803,1.106942]],[[1.047358,6.328539,9.579682,0.290153,-3.309942,-0.121692,-2.723959,0.165416,4.293221,-5.497614,-3.707605,-8.191780],[0.526658,2.973989,0.517305,4.959873,7.598580,-8.131618,0.410864,2.563168,2.016878,-4.175675,-8.707640,-0.893380],[4.387029,5.757624,-2.659158,-1.925636,-9.402079,-6.544470,0.804195,-8.605079,-4.272949,5.644623,8.568875,4.803704],[-9.445848,-0.675705,6.308980,0.918349,-4.545750,9.174232,-4.080345,-3.337955,0.145585,-2.101124,-9.715923,-2.864728],[1.362451,-4.964532,-9.844311,0.081677,-6.715914,8.274249,8.199071,-1.932044,6.550983,-5.066517,5.800386,1.639266],[5.433699,1.651032,-6.978378,-4.076033,-7.318598,-8.641070,-2.187436,8.290817,-7.820670,7.969753,2.115159,4.210270],[2.158423,-2.669743,-2.517919,9.710015,-5.814542,1.211989,-0.767381,-8.485198,-5.116077,-4.289479,3.885195,9.728711],[-2.721488,7.570257,-8.748953,8.845826,-7.893178,8.525528,4.065186,-8.323264,1.270982,-1.428846,4.866102,-9.370403],[-0.547659,-3.128711,0.679511,3.486396,-7.795818,1.001982,2.710044,-4.046919,0.771781,-8.315150,2.123409,-4.414508],[-0.833251,-8.284907,6.016322,2.992825,5.574031,0.579906,-9.539822,8.876537,0.645931,0.876809,6.738180,-5.941857],[0.363918,1.593205,1.617695,-8.420553,-0.289127,1.027234,2.082147,3.833558,9.710068,4.812348,5.594448,-5.052837],[-2.912762,1.479666,-3.211036,-3.627321,-3.720839,-3.423971,3.075266,3.056053,2.546884,1.929440,-0.741803,-2.968985]],[[-4.266356,9.900197,-9.837192,-6.981398,1.414556,-8.017348,-9.078226,-7.861554,-1.440263,-0.881515,3.697811,0.857155],[1.192608,2.281496,-3.594200,3.665274,-7.128331,-1.862657,-2.346818,1.426766,6.845418,4.799764,-2.120478,-9.857137],[-3.931441,-6.245934,8.693591,1.958707,-8.440294,-8.557692,-3.537302,0.270282,-3.003213,0.621503,2.554435,-0.184804],[-8.865827,-9.732038,5.118087,4.776348,6.483192,9.726351,3.064507,0.431419,-0.300359,-9.441922,4.313438,6.445419],[-0.596433,4.091408,5.942004,-2.221121,2.654007,-4.187662,6.708910,9.027473,2.935239,8.345362,6.193804,-5.770275],[-0.474530,-7.832443,5.609445,3.299057,-6.015884,4.887062,1.707148,2.734717,-4.294906,3.189239,1.330794,-6.029232],[-5.263789,4.460723,0.308499,9.934825,0.966583,4.475475,5.629335,-9.111986,2.142807,4.490332,5.651318,-8.205494],[-5.729813,2.994252,-5.361758,-5.931470,-5.670127,-2.242530,5.789659,5.175644,8.757029,7.201475,-3.534089,-4.590135],[8.636407,-0.397021,-0.452334,-5.363799,-3.112983,-7.570241,-5.531856,3.529159,-4.968900,-7.625654,8.066359,-3.570660],[-9.351063,7.242971,3.261036,0.022703,8.956698,8.466059,-1.316638,-6.889805,-7.398995,2.693348,2.403376,2.646735],[-8.829238,-7.941143,1.889007,-6.964701,-6.483712,-0.079064,3.461523,4.338589,2.767409,-6.897479,-3.047283,2.871029],[0.148409,5.825394,8.721062,-5.574923,-5.365575,-8.903294,-4.841992,-0.287756,-4.019595,-6.257393,-0.665547,6.750795]],[[0.612561,5.189081,-2.004427,-6.488530,1.541513,0.938853,-3.565574,-9.952324,-8.718040,-2.642130,8.235713,0.625010],[-1.973602,5.110234,9.689162,-3.021849,-8.138750,3.053406,-1.787333,-1.636233,8.506624,6.011276,1.557829,8.775307],[-1.177251,-9.896701,-1.278475,7.540949,-6.802817,1.110479,4.492140,-3.306121,1.837926,5.126207,7.801341,9.317012],[8.371209,-0.143335,-2.567074,-0.056063,8.330975,-1.735759,-8.161304,-9.563719,-5.338593,2.572636,-2.786091,5.520837],[5.097388,0.539857,-1.616364,2.768961,9.308546,-0.439695,5.839571,-0.742398,-1.332417,-0.131955,4.257031,8.610096],[-6.730827,3.579920,-9.424398,-2.208763,1.227574,-8.888322,-2.218988,2.307447,8.442074,3.326495,-3.978764,1.934412],[-4.218283,-7.352994,0.650301,5.876749,-1.913674,-0.156637,3.891675,-0.112238,-1.582184,-0.079211,-8.479417,6.356670],[-7.587506,2.792636,-0.219793,7.382388,-8.503855,-0.992765,1.465940,-1.441734,6.166998,-1.922880,5.779762,8.440130],[5.818690,7.660751,-2.902542,4.851843,2.700512,7.248739,7.875352,0.248865,-9.829997,1.650570,7.713988,8.267036],[-1.756574,-7.575825,-0.231956,-1.398058,3.734429,-1.954116,-3.027913,-8.210531,-6.843832,4.315105,-1.513389,9.650401],[8.380452,-5.858261,-2.413380,8.735839,9.770548,6.786267,6.706540,6.322132,7.202303,-2.875065,3.085984,7.602438],[7.629119,-3.460716,7.421478,-8.047569,-0.340367,-4.733449,1.972547,-9.613295,4.965573,-8.516500,0.937388,3.874266]],[[5.914501,-9.423430,1.070821,-0.445688,-2.995667,-4.972806,4.949891,-5.913169,-3.615701,-6.582506,-1.540167,-9.962414],[-9.478444,2.598915,0.287831,-3.777161,-4.017720,0.672750,1.450918,-0.700806,-4.023313,4.241051,-6.533653,-0.407050],[-7.947518,-6.552901,7.237073,-6.901432,6.412514,4.394756,2.455295,-9.445412,-6.932131,9.711736,3.757549,4.081366],[-9.510492,3.894949,0.853028,7.342525,6.957065,-2.227578,7.108974,-6.351730,-3.607254,6.081352,-0.874715,-7.701845],[0.449840,-1.293423,1.266396,7.837858,-5.691261,-3.035477,-2.645903,-2.716260,5.024848,-4.025980,9.287871,-0.178905],[-1.672650,1.689356,0.345039,9.022473,2.388814,6.951201,8.509879,8.683104,-8.952822,3.891831,0.436739,-9.600971],[7.416513,3.631008,7.708427,-6.530476,0.766537,-5.827971,9.312855,-1.681644,2.064113,-1.293508,-2.275144,3.935655],[5.070620,7.348769,-5.746758,-8.034797,-4.842537,-8.976277,4.272967,4.633047,2.361350,7.324716,3.997923,2.856480],[3.726782,0.984973,3.092449,-2.152089,-6.593571,-5.291501,7.898541,-6.324958,-1.640745,-1.808207,3.618829,7.801661],[8.617271,-4.164539,-3.994678,-7.281755,2.813104,9.889537,-3.740539,2.186166,4.791777,6.846946,-0.047330,-2.253994],[-5.689697,-8.232044,-7.797832,-8.402392,-2.819140,-9.409565,7.596106,4.160540,-9.736691,3.959722,-9.080327,9.566663],[-1.377155,6.883523,-5.056497,-9.448246,-8.393562,6.095048,-2.794545,-8.969212,-3.996021,2.649272,2.377551,-8.149150]],[[6.679030,-3.806525,-0.615437,2.202258,-6.640747,-5.899954,-6.802563,-9.961122,5.786530,4.410794,5.734168,9.669008],[-8.405366,1.152651,1.930456,3.597057,-1.683303,-2.963578,-1.131474,0.181302,-1.773949,2.836104,-8.253976,2.543047],[2.983457,5.354438,9.123196,-0.563830,6.771097,0.430106,7.774734,7.272779,7.983689,6.396035,5.125988,-7.221770],[-1.380414,-7.235303,1.493340,-1.776956,-6.810509,-9.928707,-4.864517,4.119531,-4.013269,-8.924961,-1.973175,8.362135],[-0.018325,5.341206,-2.245554,7.357133,1.510640,6.691506,-9.452139,-5.752019,-5.489606,-9.395621,6.872630,-6.848417],[-6.625200,-8.365409,0.460997,-0.657939,-5.266490,5.486581,-9.695866,3.167293,2.018019,-5.057713,-3.312615,-1.625937],[9.327641,-6.407800,4.965677,0.635279,9.951977,-7.199164,3.149186,-9.922893,-3.130448,-2.849906,4.005227,-1.975507],[0.330947,-9.225607,4.424125,-2.786911,3.116816,-1.322706,5.174716,-8.478050,0.901914,4.902922,-0.409351,-4.728429],[-9.886820,6.753584,-1.968569,-0.765694,-4.055847,5.230436,3.745039,5.216583,-6.029228,2.456996,8.461359,1.166025],[-4.490714,0.375501,-9.434590,7.565193,8.836529,-9.098213,0.185740,8.366032,4.185630,3.659221,-2.892463,5.333565],[-5.522648,-2.733772,8.159759,-2.412947,6.933730,-0.247091,7.423054,-1.849567,-1.743571,-4.051722,2.743832,0.883605],[7.808060,8.265059,0.979419,-3.050855,-7.851182,2.212066,-4.188044,1.397551,-3.452884,-9.768325,-2.710614,-5.996313]],[[7.833779,-4.674552,-4.487649,-9.293377,-5.468941,7.072254,-9.722907,-2.048994,-1.183716,-0.139351,2.981640,-9.213979],[4.465594,-6.554760,0.333880,-4.467246,2.986142,1.283878,7.673418,1.670939,-5.619057,3.184107,5.800396,6.690826],[-3.458519,-6.071532,4.381209,1.068319,6.454028,-2.282905,-3.386749,-4.332997,7.216519,9.484244,4.796804,1.514288],[2.068602,-7.986734,-3.293447,-0.410115,-9.196850,-9.084430,-8.282062,-3.806125,3.507854,-9.941148,-0.254728,-1.799422],[0.748882,-4.244473,-9.454431,-8.396643,-2.756953,-4.894733,-3.618168,2.777192,-5.855380,-2.385325,9.831650,-1.905388],[-0.290409,-5.844907,7.991630,-3.331279,-2.475584,7.169401,-8.595547,-7.575566,8.287906,8.330439,-1.448492,-8.364137],[7.262671,6.001123,0.685404,5.265638,-2.021990,-7.219884,-7.008866,-4.451103,4.460926,-9.923211,4.652863,0.115127],[5.039128,-7.771982,5.702275,-8.491256,-5.844911,-5.123550,-9.883479,7.793052,6.920386,-9.917531,-9.996012,6.190361],[1.264112,-9.299274,-5.158233,5.297627,-7.109415,3.574658,-1.154440,-4.292680,0.044707,-5.114605,8.603976,5.527265],[-6.920882,-6.562364,-0.137492,-9.045887,5.963556,2.170993,-6.139845,-3.234829,-5.198171,6.129637,6.037586,7.060330],[-4.263769,-0.754098,8.876538,-3.922375,-1.670784,0.883225,-4.943868,-0.070926,-6.842085,-0.176253,-0.636946,6.247503],[-9.919295,0.271883,7.244307,1.333701,-1.885909,5.981875,3.589062,5.048438,-3.118314,-2.684966,1.535039,2.389675]]], dtype = "float32")#candidate|8569|(8, 12, 12)|const|float32
bop_8570 = relay.floor_divide(const_8568.astype('float32'), relay.reshape(const_8569.astype('float32'), relay.shape_of(const_8568))) # shape=(8, 12, 12)
output = bop_8570
output2 = bop_8570
func_8596 = relay.Function([], output)
mod['func_8596'] = func_8596
mod = relay.transform.InferType()(mod)
output = func_8596()
func_8597 = relay.Function([], output)
mutated_mod['func_8597'] = func_8597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2765_call = mod.get_global_var('func_2765')
func_2766_call = mutated_mod.get_global_var('func_2766')
call_8601 = relay.TupleGetItem(func_2765_call(), 0)
call_8602 = relay.TupleGetItem(func_2766_call(), 0)
func_6933_call = mod.get_global_var('func_6933')
func_6936_call = mutated_mod.get_global_var('func_6936')
var_8609 = relay.var("var_8609", dtype = "float64", shape = (288,))#candidate|8609|(288,)|var|float64
call_8608 = relay.TupleGetItem(func_6933_call(relay.reshape(var_8609.astype('float64'), [3, 6, 16])), 0)
call_8610 = relay.TupleGetItem(func_6936_call(relay.reshape(var_8609.astype('float64'), [3, 6, 16])), 0)
func_4895_call = mod.get_global_var('func_4895')
func_4896_call = mutated_mod.get_global_var('func_4896')
call_8629 = func_4895_call()
call_8630 = func_4895_call()
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
call_8645 = relay.TupleGetItem(func_1650_call(), 0)
call_8646 = relay.TupleGetItem(func_1652_call(), 0)
func_1872_call = mod.get_global_var('func_1872')
func_1873_call = mutated_mod.get_global_var('func_1873')
call_8658 = relay.TupleGetItem(func_1872_call(), 0)
call_8659 = relay.TupleGetItem(func_1873_call(), 0)
var_8661 = relay.var("var_8661", dtype = "bool", shape = (15, 7, 16))#candidate|8661|(15, 7, 16)|var|bool
bop_8662 = relay.subtract(call_8629.astype('float32'), var_8661.astype('float32')) # shape=(15, 7, 16)
bop_8665 = relay.subtract(call_8630.astype('float32'), var_8661.astype('float32')) # shape=(15, 7, 16)
uop_8671 = relay.asin(bop_8662.astype('float32')) # shape=(15, 7, 16)
uop_8673 = relay.asin(bop_8665.astype('float32')) # shape=(15, 7, 16)
func_5583_call = mod.get_global_var('func_5583')
func_5586_call = mutated_mod.get_global_var('func_5586')
var_8678 = relay.var("var_8678", dtype = "float64", shape = (700,))#candidate|8678|(700,)|var|float64
call_8677 = relay.TupleGetItem(func_5583_call(relay.reshape(var_8678.astype('float64'), [14, 5, 10])), 1)
call_8679 = relay.TupleGetItem(func_5586_call(relay.reshape(var_8678.astype('float64'), [14, 5, 10])), 1)
uop_8685 = relay.sigmoid(bop_8662.astype('float32')) # shape=(15, 7, 16)
uop_8687 = relay.sigmoid(bop_8665.astype('float32')) # shape=(15, 7, 16)
func_5858_call = mod.get_global_var('func_5858')
func_5859_call = mutated_mod.get_global_var('func_5859')
call_8700 = relay.TupleGetItem(func_5858_call(), 0)
call_8701 = relay.TupleGetItem(func_5859_call(), 0)
func_6424_call = mod.get_global_var('func_6424')
func_6426_call = mutated_mod.get_global_var('func_6426')
call_8702 = relay.TupleGetItem(func_6424_call(), 0)
call_8703 = relay.TupleGetItem(func_6426_call(), 0)
func_8251_call = mod.get_global_var('func_8251')
func_8254_call = mutated_mod.get_global_var('func_8254')
var_8711 = relay.var("var_8711", dtype = "uint64", shape = (72,))#candidate|8711|(72,)|var|uint64
call_8710 = relay.TupleGetItem(func_8251_call(relay.reshape(var_8711.astype('uint64'), [1, 72])), 1)
call_8712 = relay.TupleGetItem(func_8254_call(relay.reshape(var_8711.astype('uint64'), [1, 72])), 1)
func_7017_call = mod.get_global_var('func_7017')
func_7018_call = mutated_mod.get_global_var('func_7018')
call_8713 = relay.TupleGetItem(func_7017_call(), 0)
call_8714 = relay.TupleGetItem(func_7018_call(), 0)
output = relay.Tuple([call_8601,call_8608,var_8609,call_8645,call_8658,uop_8671,call_8677,var_8678,uop_8685,call_8700,call_8702,call_8710,var_8711,call_8713,])
output2 = relay.Tuple([call_8602,call_8610,var_8609,call_8646,call_8659,uop_8673,call_8679,var_8678,uop_8687,call_8701,call_8703,call_8712,var_8711,call_8714,])
func_8717 = relay.Function([var_8609,var_8661,var_8678,var_8711,], output)
mod['func_8717'] = func_8717
mod = relay.transform.InferType()(mod)
mutated_mod['func_8717'] = func_8717
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8717_call = mutated_mod.get_global_var('func_8717')
var_8719 = relay.var("var_8719", dtype = "float64", shape = (288,))#candidate|8719|(288,)|var|float64
var_8720 = relay.var("var_8720", dtype = "bool", shape = (15, 7, 16))#candidate|8720|(15, 7, 16)|var|bool
var_8721 = relay.var("var_8721", dtype = "float64", shape = (700,))#candidate|8721|(700,)|var|float64
var_8722 = relay.var("var_8722", dtype = "uint64", shape = (72,))#candidate|8722|(72,)|var|uint64
call_8718 = func_8717_call(var_8719,var_8720,var_8721,var_8722,)
output = call_8718
func_8723 = relay.Function([var_8719,var_8720,var_8721,var_8722,], output)
mutated_mod['func_8723'] = func_8723
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8725 = relay.var("var_8725", dtype = "float64", shape = (13, 12, 8))#candidate|8725|(13, 12, 8)|var|float64
uop_8726 = relay.atan(var_8725.astype('float64')) # shape=(13, 12, 8)
var_8732 = relay.var("var_8732", dtype = "float64", shape = (13, 12, 8))#candidate|8732|(13, 12, 8)|var|float64
bop_8733 = relay.power(var_8725.astype('float32'), relay.reshape(var_8732.astype('float32'), relay.shape_of(var_8725))) # shape=(13, 12, 8)
func_5670_call = mod.get_global_var('func_5670')
func_5672_call = mutated_mod.get_global_var('func_5672')
call_8740 = relay.TupleGetItem(func_5670_call(), 0)
call_8741 = relay.TupleGetItem(func_5672_call(), 0)
output = relay.Tuple([uop_8726,bop_8733,call_8740,])
output2 = relay.Tuple([uop_8726,bop_8733,call_8741,])
func_8747 = relay.Function([var_8725,var_8732,], output)
mod['func_8747'] = func_8747
mod = relay.transform.InferType()(mod)
var_8748 = relay.var("var_8748", dtype = "float64", shape = (13, 12, 8))#candidate|8748|(13, 12, 8)|var|float64
var_8749 = relay.var("var_8749", dtype = "float64", shape = (13, 12, 8))#candidate|8749|(13, 12, 8)|var|float64
output = func_8747(var_8748,var_8749,)
func_8750 = relay.Function([var_8748,var_8749,], output)
mutated_mod['func_8750'] = func_8750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6255_call = mod.get_global_var('func_6255')
func_6256_call = mutated_mod.get_global_var('func_6256')
call_8787 = func_6255_call()
call_8788 = func_6255_call()
output = relay.Tuple([call_8787,])
output2 = relay.Tuple([call_8788,])
func_8795 = relay.Function([], output)
mod['func_8795'] = func_8795
mod = relay.transform.InferType()(mod)
mutated_mod['func_8795'] = func_8795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8795_call = mutated_mod.get_global_var('func_8795')
call_8796 = func_8795_call()
output = call_8796
func_8797 = relay.Function([], output)
mutated_mod['func_8797'] = func_8797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3047_call = mod.get_global_var('func_3047')
func_3048_call = mutated_mod.get_global_var('func_3048')
call_8883 = func_3047_call()
call_8884 = func_3047_call()
output = call_8883
output2 = call_8884
func_8888 = relay.Function([], output)
mod['func_8888'] = func_8888
mod = relay.transform.InferType()(mod)
output = func_8888()
func_8889 = relay.Function([], output)
mutated_mod['func_8889'] = func_8889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5858_call = mod.get_global_var('func_5858')
func_5859_call = mutated_mod.get_global_var('func_5859')
call_8944 = relay.TupleGetItem(func_5858_call(), 0)
call_8945 = relay.TupleGetItem(func_5859_call(), 0)
func_2156_call = mod.get_global_var('func_2156')
func_2158_call = mutated_mod.get_global_var('func_2158')
call_8965 = relay.TupleGetItem(func_2156_call(), 0)
call_8966 = relay.TupleGetItem(func_2158_call(), 0)
bop_8971 = relay.floor_mod(call_8965.astype('float32'), relay.reshape(call_8944.astype('float32'), relay.shape_of(call_8965))) # shape=(15, 1, 16)
bop_8974 = relay.floor_mod(call_8966.astype('float32'), relay.reshape(call_8945.astype('float32'), relay.shape_of(call_8966))) # shape=(15, 1, 16)
output = relay.Tuple([bop_8971,])
output2 = relay.Tuple([bop_8974,])
func_8975 = relay.Function([], output)
mod['func_8975'] = func_8975
mod = relay.transform.InferType()(mod)
output = func_8975()
func_8976 = relay.Function([], output)
mutated_mod['func_8976'] = func_8976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_9146 = relay.TupleGetItem(func_4154_call(), 0)
call_9147 = relay.TupleGetItem(func_4155_call(), 0)
output = call_9146
output2 = call_9147
func_9149 = relay.Function([], output)
mod['func_9149'] = func_9149
mod = relay.transform.InferType()(mod)
mutated_mod['func_9149'] = func_9149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9149_call = mutated_mod.get_global_var('func_9149')
call_9150 = func_9149_call()
output = call_9150
func_9151 = relay.Function([], output)
mutated_mod['func_9151'] = func_9151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4685_call = mod.get_global_var('func_4685')
func_4687_call = mutated_mod.get_global_var('func_4687')
call_9184 = relay.TupleGetItem(func_4685_call(), 0)
call_9185 = relay.TupleGetItem(func_4687_call(), 0)
func_6695_call = mod.get_global_var('func_6695')
func_6697_call = mutated_mod.get_global_var('func_6697')
call_9194 = relay.TupleGetItem(func_6695_call(), 0)
call_9195 = relay.TupleGetItem(func_6697_call(), 0)
output = relay.Tuple([call_9184,call_9194,])
output2 = relay.Tuple([call_9185,call_9195,])
func_9196 = relay.Function([], output)
mod['func_9196'] = func_9196
mod = relay.transform.InferType()(mod)
mutated_mod['func_9196'] = func_9196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9196_call = mutated_mod.get_global_var('func_9196')
call_9197 = func_9196_call()
output = call_9197
func_9198 = relay.Function([], output)
mutated_mod['func_9198'] = func_9198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8484_call = mod.get_global_var('func_8484')
func_8486_call = mutated_mod.get_global_var('func_8486')
call_9199 = func_8484_call()
call_9200 = func_8484_call()
output = relay.Tuple([call_9199,])
output2 = relay.Tuple([call_9200,])
func_9207 = relay.Function([], output)
mod['func_9207'] = func_9207
mod = relay.transform.InferType()(mod)
mutated_mod['func_9207'] = func_9207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9207_call = mutated_mod.get_global_var('func_9207')
call_9208 = func_9207_call()
output = call_9208
func_9209 = relay.Function([], output)
mutated_mod['func_9209'] = func_9209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2902_call = mod.get_global_var('func_2902')
func_2904_call = mutated_mod.get_global_var('func_2904')
call_9232 = relay.TupleGetItem(func_2902_call(), 0)
call_9233 = relay.TupleGetItem(func_2904_call(), 0)
output = relay.Tuple([call_9232,])
output2 = relay.Tuple([call_9233,])
func_9252 = relay.Function([], output)
mod['func_9252'] = func_9252
mod = relay.transform.InferType()(mod)
output = func_9252()
func_9253 = relay.Function([], output)
mutated_mod['func_9253'] = func_9253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4154_call = mod.get_global_var('func_4154')
func_4155_call = mutated_mod.get_global_var('func_4155')
call_9312 = relay.TupleGetItem(func_4154_call(), 0)
call_9313 = relay.TupleGetItem(func_4155_call(), 0)
var_9314 = relay.var("var_9314", dtype = "float64", shape = (15, 6, 16))#candidate|9314|(15, 6, 16)|var|float64
bop_9315 = relay.logical_xor(call_9312.astype('uint64'), var_9314.astype('uint64')) # shape=(15, 6, 16)
bop_9318 = relay.logical_xor(call_9313.astype('uint64'), var_9314.astype('uint64')) # shape=(15, 6, 16)
uop_9319 = relay.rsqrt(bop_9315.astype('float32')) # shape=(15, 6, 16)
uop_9321 = relay.rsqrt(bop_9318.astype('float32')) # shape=(15, 6, 16)
func_2223_call = mod.get_global_var('func_2223')
func_2224_call = mutated_mod.get_global_var('func_2224')
call_9326 = relay.TupleGetItem(func_2223_call(), 0)
call_9327 = relay.TupleGetItem(func_2224_call(), 0)
output = relay.Tuple([uop_9319,call_9326,])
output2 = relay.Tuple([uop_9321,call_9327,])
func_9335 = relay.Function([var_9314,], output)
mod['func_9335'] = func_9335
mod = relay.transform.InferType()(mod)
mutated_mod['func_9335'] = func_9335
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9336 = relay.var("var_9336", dtype = "float64", shape = (15, 6, 16))#candidate|9336|(15, 6, 16)|var|float64
func_9335_call = mutated_mod.get_global_var('func_9335')
call_9337 = func_9335_call(var_9336)
output = call_9337
func_9338 = relay.Function([var_9336], output)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3650_call = mod.get_global_var('func_3650')
func_3651_call = mutated_mod.get_global_var('func_3651')
call_9357 = func_3650_call()
call_9358 = func_3650_call()
output = relay.Tuple([call_9357,])
output2 = relay.Tuple([call_9358,])
func_9361 = relay.Function([], output)
mod['func_9361'] = func_9361
mod = relay.transform.InferType()(mod)
output = func_9361()
func_9362 = relay.Function([], output)
mutated_mod['func_9362'] = func_9362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5858_call = mod.get_global_var('func_5858')
func_5859_call = mutated_mod.get_global_var('func_5859')
call_9374 = relay.TupleGetItem(func_5858_call(), 0)
call_9375 = relay.TupleGetItem(func_5859_call(), 0)
func_1872_call = mod.get_global_var('func_1872')
func_1873_call = mutated_mod.get_global_var('func_1873')
call_9394 = relay.TupleGetItem(func_1872_call(), 3)
call_9395 = relay.TupleGetItem(func_1873_call(), 3)
func_6546_call = mod.get_global_var('func_6546')
func_6547_call = mutated_mod.get_global_var('func_6547')
call_9408 = relay.TupleGetItem(func_6546_call(), 0)
call_9409 = relay.TupleGetItem(func_6547_call(), 0)
func_7578_call = mod.get_global_var('func_7578')
func_7580_call = mutated_mod.get_global_var('func_7580')
const_9411 = relay.const([-0.789735,-6.134819,1.229954,0.243486,6.107607,5.487829,3.871922,5.171155,-9.801710,-6.170129,1.843333,1.132590,3.063525,1.278229,5.689332,6.523131,2.648737,6.082727,1.104611,-0.820160,-8.690485,-2.748999,2.767572,-3.001677,0.502328,-2.035008,6.326055,8.657309,2.449102,7.872142,7.719253,-8.146386,-5.203078,9.827095,-9.907291,-8.696409,8.888172,-1.362998,-3.462016,0.399583,-9.779419,1.445136,1.384670,-1.347742,6.197557,-2.796858,1.159593,-0.718197,-9.419490,0.386072,0.429290,6.706766,-9.856099,5.069052,0.467463,9.290690,-1.746045,0.855702,6.179430,-9.226768,8.902101,1.565835,2.419576,-2.540057,-1.770284,2.753206,1.064525,-5.031161,-9.996108,7.487546,-3.550261,2.852960,7.093943,3.323221,3.009213,9.862643,-1.846256,5.229519,-4.215873,5.906356,5.912764,-6.694862,-3.482164,-9.078629,-3.773686,-4.776367,-8.743927,-4.781785,-3.071452,3.175672,5.376774,-8.939475,2.552811,-7.904027,0.485677,-0.758389,-1.765927,1.187986,-8.540724,0.934592,9.071813,5.402740,-1.468014,9.340010,0.773492,-2.893775,-9.972387,-7.434662,-9.390052,2.243813,2.294853,-1.621288,8.020714,-0.657237,8.003604,-7.360362,3.711904,4.176748,2.461311,-5.298932,0.839010,-5.732839,0.982909,1.398162,2.840274,7.011699,5.470051,-1.846409,5.207631,-6.712937,-7.060540,-2.857691,-7.194247,5.936298,-6.060104,3.023477,-0.599237,5.399736,-8.246582,7.066434,-6.597907,-2.592590,-2.619496,-0.974897,1.716723,5.302584,2.009801,9.789845,0.489969,-5.883859,-8.377783,4.561693,3.733576,-3.024143,2.777823,3.412150,-7.182653,3.948122,-8.143967,8.911844,-5.799985,9.811737,-1.341845,-6.867009,-2.446988,1.782079,-8.202996,6.325137,-3.738714,3.420321,-8.494920,7.644687,1.691231,3.074048,-8.253975,7.360723,0.051285,-4.787933,-7.054543,7.464213,9.034400,3.406571,4.107629,6.453048,9.792282,-8.233087,7.848356,-9.603419,-3.736872,-9.965667,-3.697450,-4.425820,4.944936,7.770707,3.032189,-0.898323,-3.566175,-0.220681,-4.743862,3.012080,-4.329831,6.661594,5.654317,-5.268705,-0.632616,-5.121276,6.203987,-5.115204,7.658124,-1.810311,3.614477,-3.283122,-7.971350,9.355338,-8.538098,-8.274925,-2.250775,8.109396,-3.682187,-8.838112,-2.082371,7.891766,7.311019,-4.103861,-5.563497,2.933580,8.454450,6.803932,-0.399977,9.801266,5.500222,5.807583,0.102360,9.851584,4.348965,-2.628534,-4.013005,7.764013,-6.378332,-7.439440,-8.561762,-3.406033,2.098430,4.888125,-8.615540,4.590019,0.746855,-4.680266,8.351478,-7.904766,4.299954,-3.102813,-5.649751,9.779047,-8.021474,4.937099,5.359832,-7.584265,6.555514,-7.482857,-0.751457,2.381515,-8.582730,2.574889,9.320114,-1.837346,-3.969279,-8.015603,-9.919990,1.989346,-8.691420,0.706823,-3.749286,-5.569161,-4.284958,-5.624641,-5.767630,-3.310682,9.451900,-1.679858,1.726834,9.800471,-7.918311,-7.853010,8.282020,0.210013,6.716322,8.515661,-0.979091,9.785404,-5.220480,-9.340038,-9.837248,8.577165,-4.264904,-1.923059,4.332890,4.361197,-2.027661,-2.777534,-6.786065,5.641350,4.073656,7.408224,-8.404907,-6.884313,-4.259462,-0.584380,8.596592,-5.127091,1.974751,5.767920,-3.544719,-6.078595,-2.184606,-5.134536,-4.666727,-4.159698,-1.561614,-4.848523,0.836149,0.877361,1.459453,-1.000363,-3.288728,-2.304926,0.268439,-7.206938,-7.141078,-8.917078,3.340225,5.918245,-7.021246,7.587706,-6.345035,-3.908956,-4.999729,3.067391,6.697622,-6.338090,3.153731,4.416394,-6.237536,-8.362462,4.149442,-1.423958,-0.516406,-8.814226,8.765662,1.723732,7.071002,8.712089,-4.118202,0.549367,-2.179286,9.767870,-2.088589,8.862059,-6.318500,-1.078992,-7.284040,-3.555019,-1.019071,-4.042165,6.163858,7.104518,7.561137,-2.547317,-0.864270,9.119766,-5.718086,-1.609374,2.875575,2.671871,4.513172,6.021333,-9.710331,-2.897302,9.088824,6.370561,7.931232,1.115961,5.590108,-2.253031,-6.296057,9.446893,-1.944978,3.582680,7.666385,9.678748,-3.930190,-2.489967,-0.823991,-5.860397,6.944990,-6.673312,-7.063580,3.588934,-0.798400,4.459114,8.794927,7.879646,-2.079419,-8.218463,0.300284,1.870044,-3.577615,8.959424,-9.163020,-8.314929,9.940689,-8.240431,5.237324,7.471503,2.160270,-2.332310,7.752974,-0.221047,-6.344234,5.115166,-4.609357,-0.837286,1.922839,-6.799506,7.288937,2.930758,8.271952,-2.927028,-9.596994,-5.203832,7.453336,-6.435971,-6.606418,-4.458267,7.477549,3.067881,-4.135598,2.678934,2.331621,-0.826218,-0.151032,7.496900,8.479905,-8.271530,8.554443,-9.075433,5.379533,-6.648904,5.893577,0.634117,-4.241176,3.555921,-8.708805,-9.619572,-8.829624,-6.195240,2.988962,-1.367478,1.125906,-4.738349,-6.910770,7.355470,6.142783,3.388098,6.313848,-4.720170,8.679937,-3.600949,-2.245254,7.641179,0.102534,2.912746,8.145601,-3.037813,8.292684,-9.930376,5.693631,4.936153,8.731465,6.288488,4.773550,-9.713783,6.432955,-3.465942,-8.981588,-3.704159,3.289979,-3.237924,-9.954435,-3.540997,2.142260,0.277479,-5.641731,3.453415,7.244003,-4.201437,-4.551702,-9.485023,-9.773244,0.042346,-4.658292,-0.024615,-8.784384,2.870445,5.365129,-1.062115,-4.722469,3.234557,-9.471771,-6.944223,-4.809525,6.885133,6.002029,-1.055781,-1.093146,-2.893924,-6.844089,5.661723,2.864820,7.701751,-3.974378,1.103376,8.218618,9.442691,-5.803100,3.909440,4.477374,8.897805,-5.343219,-7.808505,-5.504688,-2.834415,2.489213,7.932931,-0.885744,-6.096087,-9.159593,4.470133,-9.416093,9.898812,-5.688162,8.381263,2.584635,-4.914830,8.796054,8.296575,-0.038080,-6.982567,2.720074,-5.452358,-1.385568,-9.820841,2.882060,-3.195710,-7.773220,-2.383090,-0.113772,-1.258843,-4.875948,-5.541281,4.838164,9.455613,2.577415,-3.353730,4.080457,-8.541319,2.823134,-5.424199,-7.694978,-7.988411,0.423369,8.585033,4.431385,2.239246,-6.707874,7.082642,1.420298,1.835066,-0.903933,4.026801,2.230764,7.468453,-6.083103,7.594727,-8.479876,-0.558899,-5.603766,5.748091,1.729505,4.313806,-5.773446,-7.646934,-8.169488,-6.733539,4.498090,-8.502567,7.041105,6.822996,-9.612296,-9.496538,-2.117357,-0.220247,-2.720867,-1.637280,-4.414632,-9.191821,-9.297468,8.096866,-0.002510,1.348422,4.963842,-6.144481,8.785371,8.909891,-2.359604,-6.209535,-9.200475,1.454164,7.839673,-7.729610,-8.653216,-0.121232,5.796640,4.024812,-0.780618,4.071975,-2.353472,-5.092679,5.047289,1.495483,-6.877976,6.694704,-6.315321,8.186355,-4.138411,-0.581237,-0.656439,-6.823245,-5.193910,-6.843705,-8.656272,-1.248778,7.816724,5.817469,-0.087653,3.722202,-6.010689,6.706602,2.216878,-7.015218,3.603015,-4.000318,-0.633430,5.913125,-2.282079,7.812875,-5.277856,-5.877177,-1.437621,-6.933838,-2.415541,2.602184,-0.404482,-3.914775,-6.469754,-7.545443,3.313037,2.987979,5.163698,-6.499954,-9.124081,-6.100163,6.118098,5.962788,-5.913346,6.407648,1.341954,-8.244562,6.149490,7.621609,0.326969,7.032442,1.201955,-1.210079,-8.905417,-8.253318,-7.396656,7.483418,5.927935,-5.662619,-2.206084,2.244100,-3.018408,-5.868266,-4.163346,9.815333,9.600126,-7.774953,-8.280528,9.464770,0.700657,2.622022,-9.739606,2.330116,8.606160,-5.611951,9.792143,2.047795,7.939606,-4.024819,-6.582879,8.740164,-7.885292,-2.965534,8.740640,8.707413,2.048834,-1.150300,7.066643,-5.479844,6.269471,1.912847,-0.029915,5.255599,-7.099576,6.118203,2.482440,-9.919471,-7.048353,-4.869631,-0.121625,-7.686803,5.324629,0.631660,-3.896946,3.595351,-4.057078,6.611588,-8.966394,-3.364753,-3.705020,8.146391,9.834141,3.693531,-9.971767,5.469327,-6.148235,-0.276749,-9.179072,-7.528883,0.545926,2.014819,-7.726790,-5.102233,4.795148,4.184889,-5.759692,5.008188,-5.437839,2.593317,1.235290,4.932099,-8.605563,9.629169,-6.421167,-6.716746,4.874365,2.577375,-5.058577,-2.480405,3.683467,5.119059,-4.759249,1.388216,9.565856,9.089078,2.575525,-3.767703,6.210525,-1.259713,-2.638363,5.064787,-7.107174,8.878214,1.163540,-4.410079,-0.825684,-8.570774,0.899559,8.659171,4.409398,7.206541,-1.562736,-7.775723,4.106858,2.872415,6.327470,2.635699,5.214187,-0.909891,8.869919,5.656920,-4.368206,-4.676874,0.904937,1.662191,0.609791,8.532033,-5.120241,1.347891,5.707552,6.237511,8.640884,-0.058219,-2.942515,6.919155,-9.260036,6.725173,8.397421,-4.614578,6.676700,3.965053,-5.922764,-0.179926,-6.767040,-5.973813,-6.649224,6.026277,-4.062832,9.184876,-6.784658,-5.215542,5.904757,-1.826587,-5.452537,-2.893915,-9.047468,-1.138918,-2.355086,3.246142,-7.326717,-1.740702,-0.742226,-7.529760,-5.071869,5.709582,5.789608,2.794850,7.713669,6.740953,-1.367041,3.359458,8.123830,1.129744,8.755116,-2.930413,-4.910850,-9.659830,-3.681639,7.222627,-1.821773,-5.687928,3.190675,2.579300,7.118806,-6.353659,-5.374935,-2.196335,4.057329,6.275770,-2.702558,-8.797443,0.795002,5.586354,0.713919,-3.101191,9.719705,8.753360,-2.639112,6.397343,4.812452,7.987125,-7.873460,3.885495,0.215323,-0.983844,8.120908,-7.539463,1.427910,-0.129875,-3.725767,2.097933,7.722138,-2.115294,2.020977,6.131138,8.068723,-2.180208,-0.834346,1.216492,-6.894956,-7.912412,-6.723944,-5.106816,-6.582352,0.373669,1.732133,2.989322,6.131874,-1.727154,7.009659,-9.335634,-7.754212,-9.522195,-9.633366,-1.726409,1.607615,-5.751524,9.212530,-7.255114,-7.607406,4.980974,-2.250859,-4.505723,-5.723918,-0.678432,5.347535,8.356636,0.388047,-3.242426,2.887549,-0.486311,4.661972,3.184091,-9.574639,3.840217,6.115949,-8.388665,2.820013,1.081430,-8.448239,2.998852,-5.948308,0.489452,6.791303,-2.620162,0.690559,2.345402,0.765118,2.606966,-4.710345,-1.505448,9.121226,9.617398,-4.974902,5.510041,-7.611393,-6.384705,2.331337,-0.006127,9.384361,9.260569,-7.968691,-9.207754,3.708213,1.273107,-4.322661,4.872624,-5.915092,-8.851297,-9.380077,3.486290,-8.001632,4.730661,-5.827916,-5.666209,-7.918346,-0.340808,9.523000,4.938394,-1.269923,-5.533452,-2.154236,3.681177,7.630781,2.022013,7.585046,-4.296326,-7.936713,1.259324], dtype = "float64")#candidate|9411|(990,)|const|float64
call_9410 = relay.TupleGetItem(func_7578_call(relay.reshape(const_9411.astype('float64'), [990,])), 1)
call_9412 = relay.TupleGetItem(func_7580_call(relay.reshape(const_9411.astype('float64'), [990,])), 1)
func_6227_call = mod.get_global_var('func_6227')
func_6229_call = mutated_mod.get_global_var('func_6229')
call_9421 = relay.TupleGetItem(func_6227_call(), 1)
call_9422 = relay.TupleGetItem(func_6229_call(), 1)
func_9149_call = mod.get_global_var('func_9149')
func_9151_call = mutated_mod.get_global_var('func_9151')
call_9424 = func_9149_call()
call_9425 = func_9149_call()
func_4805_call = mod.get_global_var('func_4805')
func_4807_call = mutated_mod.get_global_var('func_4807')
var_9430 = relay.var("var_9430", dtype = "float64", shape = (728,))#candidate|9430|(728,)|var|float64
call_9429 = relay.TupleGetItem(func_4805_call(relay.reshape(var_9430.astype('float64'), [728,])), 2)
call_9431 = relay.TupleGetItem(func_4807_call(relay.reshape(var_9430.astype('float64'), [728,])), 2)
output = relay.Tuple([call_9374,call_9394,call_9408,call_9410,const_9411,call_9421,call_9424,call_9429,var_9430,])
output2 = relay.Tuple([call_9375,call_9395,call_9409,call_9412,const_9411,call_9422,call_9425,call_9431,var_9430,])
func_9438 = relay.Function([var_9430,], output)
mod['func_9438'] = func_9438
mod = relay.transform.InferType()(mod)
mutated_mod['func_9438'] = func_9438
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9439 = relay.var("var_9439", dtype = "float64", shape = (728,))#candidate|9439|(728,)|var|float64
func_9438_call = mutated_mod.get_global_var('func_9438')
call_9440 = func_9438_call(var_9439)
output = call_9440
func_9441 = relay.Function([var_9439], output)
mutated_mod['func_9441'] = func_9441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5512_call = mod.get_global_var('func_5512')
func_5514_call = mutated_mod.get_global_var('func_5514')
call_9508 = relay.TupleGetItem(func_5512_call(), 0)
call_9509 = relay.TupleGetItem(func_5514_call(), 0)
output = relay.Tuple([call_9508,])
output2 = relay.Tuple([call_9509,])
func_9511 = relay.Function([], output)
mod['func_9511'] = func_9511
mod = relay.transform.InferType()(mod)
mutated_mod['func_9511'] = func_9511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9511_call = mutated_mod.get_global_var('func_9511')
call_9512 = func_9511_call()
output = call_9512
func_9513 = relay.Function([], output)
mutated_mod['func_9513'] = func_9513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6845_call = mod.get_global_var('func_6845')
func_6846_call = mutated_mod.get_global_var('func_6846')
call_9518 = func_6845_call()
call_9519 = func_6845_call()
const_9532 = relay.const([[[-2.015042,-1.161424,-4.879832,-3.908814,-4.813980,8.827864,8.781732,-9.334513,7.628412,3.568280,5.748928,1.723195,-1.690983,-4.678056,2.028774,8.950487],[-3.719994,-9.002731,2.441755,-1.205899,0.096334,-9.304932,8.369831,5.232066,-1.185410,-9.310900,6.581770,0.205228,2.015866,-0.657132,-5.746946,-2.724974],[-9.916628,1.320813,-2.966940,6.262844,2.409887,-1.391190,8.993243,3.834133,3.159527,9.120964,3.800446,-7.960405,4.330927,5.884359,-0.653026,-0.456699],[-7.712130,-7.317997,-4.774995,3.367901,-9.835432,-0.276690,6.755529,7.768688,6.212217,5.527731,5.958403,4.839068,4.711901,-6.413166,-7.430178,-4.246540],[1.942461,7.656416,-8.086684,7.185435,9.738561,-5.575966,-3.673524,8.595844,2.036921,-3.586535,-7.206569,0.466971,0.489796,5.848500,-0.854160,-8.643637],[-2.205592,9.733862,-0.665244,8.858714,-6.075481,3.917948,4.486056,-0.768320,2.860958,-2.880026,-8.858439,7.266942,9.088883,-0.207876,-4.088134,5.903742],[-7.727850,-2.807544,-6.260692,-1.734345,1.573993,4.397261,-1.040096,8.665905,-4.965730,7.505499,6.633032,-2.674462,6.953032,1.688977,-5.867826,3.168996],[8.272047,2.746804,0.666271,9.118008,4.812088,-2.328085,-7.831133,-2.052522,2.106048,-5.127249,-5.828107,3.728368,5.553591,-1.323362,-7.919721,-2.573959],[4.930883,5.201336,-7.238925,2.185079,4.934930,8.723249,-1.988375,-2.169467,-5.174119,-9.541577,-3.395110,-7.616377,-4.837942,9.761004,-0.949584,8.904466],[2.134814,1.227941,3.184212,-9.179135,-4.193919,-0.618187,4.716540,-8.721403,8.948220,-0.044778,-8.799057,3.214176,2.950280,8.707248,3.796800,8.143491],[8.404825,-5.178387,-0.925328,9.717435,-3.911549,5.571305,7.972231,0.760344,-0.555296,-7.227748,4.816023,-5.901149,-2.903177,-2.989933,-7.655629,-5.226052],[-1.151054,-7.357931,5.039586,3.675889,7.895273,0.879703,-0.695232,-9.725657,2.982462,-2.096770,-0.980555,7.458603,-6.291545,-8.198936,-8.199535,9.733413],[6.768460,2.667316,3.529157,4.305634,8.222240,3.114690,7.353846,-2.465794,-0.498614,0.287894,3.436886,9.735515,0.170886,-5.219484,9.246538,-0.532658],[8.262658,7.812948,8.916531,-9.399472,-3.876320,-9.595422,4.358728,-4.959759,2.958226,-0.261097,-7.367911,2.787157,-3.156980,3.769383,8.600551,-3.845014],[5.134124,7.047332,-6.722573,1.524947,-5.050717,6.209115,7.910033,8.867698,7.516281,4.884438,-6.482973,7.489446,9.998129,-4.621633,0.066748,6.301092],[-9.506727,3.084757,-8.906487,5.258782,-6.745698,-2.891781,-0.680445,7.962351,-7.122799,-3.035049,6.321201,7.853999,-1.240940,4.311655,-1.565224,0.542926]],[[2.651570,-8.904976,4.106810,-6.478657,-0.961743,5.809422,0.282098,-4.417368,-4.390893,-5.666029,9.155738,-4.880988,7.657596,1.381963,-8.995480,-8.414503],[9.472588,-2.828031,4.914145,-0.222287,8.443544,-1.989962,-1.383406,-7.302795,1.426049,-6.318012,-0.372601,8.409143,-8.498612,-6.315195,3.919750,7.191131],[6.487703,9.158551,-6.712065,-5.800191,-5.133339,-7.142733,4.485242,9.861567,1.936559,8.217576,-5.134013,0.075387,5.172283,2.743973,5.030636,0.203867],[-1.636086,4.485892,4.488511,1.718149,-5.096211,-2.680489,-6.231198,1.621095,-5.567286,-4.157110,6.747723,7.394281,2.378607,4.643926,2.278557,1.256553],[4.651610,4.751054,-2.270012,-2.433706,-8.882683,-8.613513,-2.870978,6.270931,4.901368,1.433771,6.472969,2.799985,-9.959825,3.725355,-8.001624,9.653472],[4.827475,-2.251662,6.843961,7.490145,6.982741,6.142699,5.827688,-7.036961,-0.771898,0.050819,1.936585,-8.113614,0.119411,5.722480,-0.527747,3.734777],[1.600070,3.572347,8.988594,9.866540,-2.499903,-8.401339,0.982651,-9.682354,0.043603,2.269214,0.668207,-4.104137,-7.962535,-3.716157,-8.043087,-9.266882],[3.814125,4.861779,-6.183982,8.003546,2.795680,-8.502838,0.573646,-4.072324,-5.950126,3.068930,2.430862,-7.162917,8.051497,-5.814059,4.576983,-4.655962],[-5.853766,4.959922,-9.743527,8.137793,-5.700013,-0.384134,7.837316,-4.516121,-9.191547,0.631738,1.876942,3.849969,-2.475241,4.397712,7.454922,-7.886537],[9.222765,-6.221050,-2.798642,0.285186,-5.619378,-2.053199,-9.260157,3.180426,-0.555200,-3.986762,0.995770,3.730757,7.505777,1.968288,-7.591312,-3.842687],[8.492938,7.749506,-9.576358,-8.606354,-0.199317,-6.236781,-7.659461,7.335504,-7.478277,-3.654714,-7.876855,9.400108,-2.714607,-0.774122,-1.108666,-6.987699],[1.726616,-6.119435,-8.124554,-4.286745,4.529273,0.467075,9.315807,0.693401,-4.910970,1.705275,8.840629,-7.643103,9.509182,-6.341524,0.019557,4.751247],[-9.470258,8.456979,-1.658395,4.165803,-3.775408,3.234680,5.890611,-9.171242,9.574275,-4.271613,-2.564348,-0.474018,9.034129,-1.254101,-8.087541,-9.051125],[6.199745,3.664383,2.245852,4.629149,-9.961357,0.474346,1.154536,1.762440,6.208335,2.052996,7.284632,8.671895,-8.320860,3.909220,3.004313,3.179017],[4.333748,3.174768,9.518786,9.737218,0.414786,-5.225583,-8.450229,7.434834,4.335155,0.866993,5.087999,-5.948726,-4.988531,-8.571580,9.863052,-2.461520],[-0.933045,0.539360,7.579569,9.354749,-4.644665,3.207566,-4.910763,-2.369386,-5.760464,-4.602383,9.589082,0.528975,-1.364035,2.050111,-9.405514,4.263532]],[[9.580773,-0.433260,4.929406,-0.349056,6.951644,-1.320353,-4.569008,-0.614808,-5.360343,-7.519824,0.453886,-8.493864,7.622508,4.577818,5.481701,1.527449],[1.534816,2.268274,0.173144,-1.712986,-8.760739,-6.463324,-7.912607,3.970615,8.452737,-2.423187,0.330786,1.368799,-6.114948,-1.404038,4.728191,0.311687],[-7.093356,1.587299,-3.573930,-6.222113,-7.236127,3.788331,6.913105,7.351734,5.565815,2.209110,-8.298682,4.895003,4.309596,8.775281,4.340417,-6.064163],[8.828623,-2.299592,5.575505,-5.389083,6.769278,-1.114526,-5.077872,-2.149521,6.899981,0.641512,-8.915654,4.955201,-4.593026,-7.454211,9.013067,8.937430],[-8.607957,-6.242191,2.960889,5.254000,-7.599006,1.407359,0.873130,-0.530450,-2.457158,9.901397,3.802572,-8.378776,0.168660,4.796853,0.410319,3.645443],[-5.841412,-8.051507,6.852374,3.156615,3.618141,-1.471560,-6.420143,-9.204523,-7.785558,9.270414,-5.659507,-4.452340,-9.670298,-4.377764,-2.816402,5.515956],[5.283335,-2.864783,6.658800,-1.307591,0.713666,2.712208,-1.399067,-8.779670,6.616325,-9.240507,4.358930,6.540187,-1.338939,-0.407644,-7.788389,-4.036549],[5.197769,-9.453154,-9.296441,2.314519,9.165639,0.569831,-2.683601,7.082100,9.240983,9.292875,-0.143211,-3.588600,-7.411718,2.918164,-9.858242,-4.077059],[2.699992,-3.360173,-5.071430,9.163844,-5.943799,1.949840,-9.712157,3.059808,-7.395021,-5.643997,2.413190,9.198817,0.229241,-0.679533,-1.325870,3.469562],[8.617075,3.094080,-5.607145,-4.725083,1.363514,9.163302,-5.318641,4.341274,-7.781140,6.436577,-8.342954,2.784823,4.534717,7.459323,2.375548,2.849968],[-7.427698,-6.434482,2.644523,-2.109042,-0.621770,-3.783838,-4.320592,9.922841,-2.807191,-8.820312,3.038631,-2.450705,-1.441993,5.221524,9.064774,-3.777054],[6.137715,-4.322241,8.756084,-2.906552,-9.024394,-6.682732,-1.615709,6.005706,-0.879745,-8.647879,-8.746539,8.430510,-3.151087,-7.789983,2.860190,-9.082118],[3.964848,-6.250742,0.491454,-0.996037,4.831887,-0.235271,-4.026908,-8.388883,1.372532,-8.209370,-2.965420,-1.406224,-4.823432,-8.360385,-0.864219,7.208223],[6.498994,-6.846199,-0.945435,-2.542855,-6.939422,6.307617,5.315555,1.841335,-8.821409,-7.892358,9.632029,-5.528274,5.984404,-9.887322,9.959539,9.583774],[2.607461,3.783747,-7.461661,6.646264,-3.121701,6.764327,9.531591,-9.124327,-9.472713,-4.139382,-9.311284,-4.914606,5.756663,8.940248,-0.978882,1.129768],[-4.084898,3.143314,-0.128027,3.052048,0.328018,-6.932339,-4.783859,3.847767,0.073426,-3.073332,-7.699090,4.890504,1.222016,-1.855013,9.121160,9.422656]],[[-5.471312,-0.196803,-3.945559,4.558246,-1.551807,-1.151535,-1.601835,-3.292089,8.754946,5.620562,0.343566,4.705788,1.735206,-4.085572,5.664683,9.486011],[-8.223477,-3.653569,2.863532,-3.252401,-1.529103,-1.838530,-1.632089,-0.639859,-4.491930,8.261489,3.131677,-0.774915,-6.711380,8.428576,0.892157,5.315711],[2.333758,-6.257967,0.036901,-1.671414,2.929304,6.855105,3.891036,1.452178,9.795508,2.233960,0.115829,-6.290550,-8.917000,7.868318,-8.986411,8.612218],[-8.883605,-0.181005,0.478700,0.894318,-6.832283,-4.774178,3.442107,4.873826,8.626673,8.471186,-7.670904,-5.046555,0.008968,-7.321006,7.271448,1.086880],[1.325686,3.207912,6.575548,6.292539,3.689318,5.564085,9.481831,-0.568491,-7.610252,0.392627,5.202483,5.402864,8.764333,-9.983104,-4.097669,5.889197],[9.757291,-0.865092,9.282000,-1.416049,1.335599,9.684153,-7.708381,4.960662,5.978716,-0.113230,2.107644,-0.578762,2.774832,6.872532,-2.245044,-1.574910],[5.217292,-4.257104,-3.308611,-4.624527,5.025919,0.693819,9.867793,-3.450620,1.363381,1.731192,-2.511687,-6.268409,-0.086671,6.574706,-5.792592,-1.224876],[-8.669918,-5.097040,-8.493068,6.671042,3.861484,3.960905,6.912514,6.646340,-0.850035,4.853307,-7.602633,0.407905,0.253096,-7.448442,-2.234273,-5.880247],[9.489731,1.166748,3.352646,6.011581,7.399387,2.481729,-9.363810,-7.883405,6.207840,-2.798314,9.160541,-9.508140,-5.009878,-3.456449,5.964658,-3.255150],[8.221819,-6.751134,-5.904099,0.229962,7.491085,-4.599677,-3.662861,-5.423215,5.529121,2.261200,-8.529811,5.436041,-9.373873,1.095923,-3.255282,0.972656],[-6.395550,-3.445932,2.548763,-8.698415,-5.916643,4.594735,3.382688,-7.125363,-3.877752,3.056259,8.898590,7.693113,-3.064760,-4.829632,-2.034521,0.952546],[2.090066,6.731514,2.875831,1.269856,0.430312,-3.519346,7.420543,5.142513,6.234128,-8.207716,7.551282,-1.806637,7.337061,7.639740,-1.182148,-2.044461],[-1.925257,0.312592,5.514209,-0.664405,7.143785,-1.955560,7.628746,-8.267660,-0.565084,-6.742085,-4.150050,-5.624781,8.635015,-8.700820,-1.719155,7.940090],[-6.683332,-2.140746,-8.584787,-4.890249,-5.313180,-3.960937,-2.317681,-4.662884,2.645320,4.869886,3.217709,0.181765,2.252399,6.887284,-3.670754,-8.530759],[5.184316,2.960436,7.664347,0.779830,-8.265893,-0.208885,-3.245511,4.047158,2.607840,5.791815,-9.206608,5.107171,-4.396797,6.952528,0.428045,-9.803558],[4.385140,-8.746427,3.800626,-4.402583,2.709716,9.623722,3.903803,-7.893230,4.013040,9.375141,-6.818253,0.011055,5.699809,-4.306840,-1.875955,1.257447]],[[-0.838904,2.758569,1.473822,6.998770,-7.418111,-5.527685,3.623800,-0.008633,5.659078,3.552170,-9.582031,-2.468844,2.818680,-7.304971,9.626251,2.161046],[-1.712910,-7.352873,-1.418752,-0.912570,-4.392147,-0.021400,9.611801,-9.386494,2.245368,3.104029,-4.114825,6.705247,-1.797502,7.253819,-7.133301,3.421497],[7.365336,-7.058218,2.198984,-9.099836,-6.740470,2.144122,6.898930,-3.644810,6.614424,-7.865349,1.383817,-4.058358,-0.919633,-7.544761,-9.578716,6.951527],[7.228678,-1.858507,-4.208375,-6.643847,8.594413,1.865972,3.040444,4.907054,6.881547,-8.061831,-2.677324,-6.912930,-3.519828,5.184889,-2.199526,3.771059],[-9.070759,-5.649576,-2.802484,5.324129,-6.244954,8.068652,-1.109950,8.499220,-6.381292,0.488652,-0.210513,9.871489,-1.943762,0.649688,4.189405,-8.608033],[-3.979196,0.883205,4.976180,0.861638,0.282568,5.914550,3.122178,2.328266,-4.416151,-2.234614,-2.359081,4.971742,-3.511771,9.542830,0.489950,-3.668891],[-8.480962,3.319287,-3.723600,7.337508,1.672715,-7.619309,5.641524,-2.781641,-0.149753,-3.813330,8.268204,0.114627,4.065447,8.690426,-1.274320,-0.614937],[9.873792,-5.289332,-4.078484,9.696334,-9.831715,3.567056,8.266971,6.085361,-3.217077,-9.971303,4.924715,-4.605627,-9.951565,-5.775512,0.918894,6.916219],[-6.403578,-5.682899,-4.021612,-5.938418,0.005649,-3.032098,9.253583,-1.242265,-5.062058,8.450614,-0.002133,-2.851310,-2.382840,3.208729,4.076989,-8.693495],[-1.811618,0.130363,5.962867,8.055211,3.219633,6.741759,6.078122,-4.948174,8.392496,-6.157043,8.959400,-3.843835,5.316412,1.357432,6.997372,-5.082237],[7.508775,-5.141628,4.004540,9.786824,6.571526,7.503251,1.955648,-6.002061,-8.592231,-6.434408,0.525913,9.731079,3.295935,-1.950973,-8.838282,-7.433483],[-6.073166,-8.538389,3.625687,-2.175405,8.626142,1.420863,9.460522,7.225700,-1.978747,-7.145288,-2.790444,-1.713899,-9.904622,-7.637877,8.802154,-9.906542],[3.793694,4.709273,6.667598,-2.256032,-5.738160,2.134255,3.215849,4.615140,-6.560481,-8.285927,8.456519,-9.230447,3.031972,-5.714910,-4.415133,-0.017211],[-7.747077,-2.652963,0.757377,-0.566604,-2.213756,8.845142,-7.938218,-9.389041,-2.866926,3.179285,1.404574,-1.781907,8.891238,-6.037178,9.111305,2.247050],[-2.173520,2.248011,-7.203022,6.967565,8.594882,6.489575,2.348991,1.487160,-6.762956,0.006500,-3.840332,-5.044659,8.507061,3.012307,2.336862,-4.359716],[-8.907899,8.853427,8.593270,-7.937440,5.736543,-5.240342,7.010182,5.427420,-5.559724,7.082800,-6.981879,-2.590572,-6.182427,-2.180050,7.094855,-9.282493]],[[5.904817,-7.701866,-3.215098,1.952633,-0.883394,0.272084,0.301532,5.201905,6.811472,2.178408,-7.561464,0.529369,7.355936,-7.650205,-0.411693,0.374107],[-9.020404,-4.318451,-4.966996,5.983708,3.962028,-3.080412,9.868517,3.112234,-5.517408,-7.502599,-7.670633,-7.448937,0.854088,-8.896403,1.212489,7.119672],[-7.692290,-2.959825,-9.008300,3.369479,-4.537847,-3.704853,-2.793941,3.631897,-7.990637,2.892275,2.300940,3.762164,9.381233,2.136840,7.423769,-4.014774],[-2.374346,-4.049957,-8.324205,5.316219,6.428379,-6.805426,5.489477,-9.305484,8.456165,-7.562897,5.006671,-9.475401,-6.187144,9.028481,-8.277740,2.295434],[0.461701,8.429708,7.424268,-4.996284,0.370300,-7.216307,-6.296486,-2.627512,6.340065,5.026304,-2.705408,5.376705,8.604468,-3.083247,-0.003743,-3.838474],[8.288425,-7.596312,-5.651047,3.675260,6.206235,-2.491814,3.767021,-0.059809,-4.632106,1.982338,6.185111,3.443928,-8.990411,-8.734244,9.477804,-6.397039],[9.128991,0.261709,3.881719,0.627567,5.862277,9.572289,-9.799625,9.356356,8.737208,-8.876588,2.547438,5.323505,5.909121,-7.897730,-9.165482,-3.487598],[4.994375,-7.038970,-5.457516,-1.689016,0.759883,-2.348447,1.394509,-5.136064,3.750915,2.436795,-8.192994,-8.884147,-1.238937,-9.818544,7.155333,-5.423971],[7.262878,3.731243,-4.941397,6.927037,9.407593,-3.210480,0.577981,2.776950,3.698438,4.328929,0.215340,7.140944,-9.794470,6.354885,-8.010982,4.507271],[-5.997115,-0.161450,-6.852126,-4.333019,9.742556,-9.008930,-0.588900,9.215193,-9.412455,7.994285,-6.974798,5.081210,9.892610,-3.541140,1.510521,1.505824],[7.318257,-0.707932,0.314901,0.328519,3.655269,9.236225,-9.811800,2.468862,0.782019,-7.269506,-5.009566,-1.306423,-8.037772,8.982858,-9.143257,6.203928],[-3.134381,9.693002,2.726980,1.380232,-1.115717,-5.201491,5.462961,4.687107,-0.984011,6.975327,-4.323034,-1.130927,-0.128791,-4.229782,-1.882865,-1.946051],[7.609152,-1.431759,2.303196,-5.446570,-8.391461,-6.961570,-7.453498,-7.697096,8.108863,5.379204,-9.798550,4.895581,-1.938275,1.508785,7.891638,9.344448],[-7.319143,7.248293,7.254430,2.715013,-0.268281,-5.918124,-8.065069,-1.561426,-9.585956,5.388798,6.208308,1.122218,-3.987891,5.265476,8.177187,-7.853153],[-4.513817,5.411980,7.204671,-0.030733,-7.752968,2.234641,9.509107,-5.419633,0.368186,-7.928939,-6.645636,-9.963154,9.392636,0.212405,3.934426,-0.855087],[9.114912,5.742494,-9.321975,3.105444,-7.335235,1.021609,-4.225397,7.083678,3.876025,-3.956948,-3.653710,-6.018140,-1.464110,-4.711907,-7.529056,-0.881012]],[[-9.190651,-3.492729,0.223998,6.886484,-4.372416,2.245533,-1.309239,2.661344,2.484513,-5.034214,-0.807912,0.225829,-2.330933,-7.358116,-4.560931,-5.183068],[8.708271,0.065762,-8.820806,-2.359632,-2.833039,7.893178,2.477354,-8.735569,7.711319,-2.384955,-8.013993,-3.116263,0.044379,2.349098,9.249388,-9.039810],[-7.661902,4.174320,-2.123333,-8.382039,-4.497083,1.727726,-4.920860,-6.468101,-2.685148,8.745779,-7.670668,0.122274,2.086800,6.298874,9.317159,6.610174],[6.142394,-7.484624,-7.641464,-0.465896,8.327489,-8.543787,-3.063754,0.446130,2.393111,1.988353,-6.131125,2.511337,4.487106,5.016112,-5.768514,-8.852238],[2.148282,9.898484,4.684585,-0.766571,-8.826795,-2.694625,5.590403,8.087417,6.718811,-2.486616,-3.052363,3.117558,-9.043412,-3.777171,4.634849,3.494417],[3.924577,-0.071120,-2.504767,5.779629,-6.072523,6.794593,2.833638,-2.909132,8.104088,8.357326,5.970251,0.314432,1.181646,-7.341093,8.854698,6.260597],[1.504437,3.252261,2.628883,-9.283365,2.590319,1.740325,-9.056586,5.966173,2.267963,8.271060,0.938127,-6.916493,-1.992215,7.904985,-6.210055,4.804229],[-3.390894,-1.859386,6.794624,7.449015,-9.900217,-1.948689,7.746255,1.421062,-6.547792,9.894092,5.766510,-0.047172,-3.358324,5.401821,-9.686288,-8.372254],[-8.946725,-6.743555,7.804876,-9.235675,6.677589,0.872898,-0.811245,4.419234,5.904427,-7.369113,-0.201795,0.711392,-2.706493,-6.193115,7.745317,1.570137],[6.036677,7.934535,-1.560733,-1.643067,-5.372167,-9.990204,-8.200208,9.071674,-6.525621,4.511731,-5.164281,0.798264,6.603754,-7.627392,8.640328,-9.455298],[2.705095,6.931675,9.549094,4.523738,5.126005,-1.255015,4.565645,-1.329922,3.578425,4.615309,-1.263112,-3.441065,-5.321534,-5.618756,9.239058,-6.504610],[-6.123433,-2.526754,7.310806,-8.800452,0.831633,6.680511,-6.905962,-2.548811,4.724918,-1.684345,-4.650689,0.216914,4.424437,-8.069853,8.607079,2.995501],[2.940392,8.959155,-5.170346,1.695320,6.478522,-9.576079,-1.448534,2.900649,-8.565935,5.688864,9.598620,5.918428,-4.129334,6.202462,-6.439023,-6.925533],[-2.701094,9.552600,0.449588,-7.075904,7.985357,-5.170484,9.912701,8.520652,0.532471,-6.388706,6.897800,7.214267,-6.180190,4.089755,-8.386627,-3.221520],[-9.015414,6.618670,-9.119432,-9.298065,-5.215609,-2.443865,-9.228658,-3.121262,-2.175639,-2.206522,-6.185420,-6.303557,-4.701830,-1.746410,0.720801,2.778341],[-6.285578,8.348964,-0.557534,-0.272382,-0.698185,-7.525013,-1.834115,0.317172,-0.570455,-5.039739,7.605804,7.557353,4.256656,-5.081520,-6.395419,-6.236889]],[[-9.602495,6.707762,9.364718,-7.921198,-7.401265,-4.102415,0.580856,-2.774039,-5.494182,-4.347893,1.296333,1.441235,5.318915,4.740517,-1.845613,-7.375729],[3.036738,4.845561,7.678361,-8.299849,7.510853,-2.261631,-7.772352,-7.052910,-6.943537,0.928215,-8.945114,-0.847943,-4.075402,0.366938,3.611122,-7.818847],[2.174630,5.297422,2.291983,6.292140,-3.302621,8.459035,-6.409687,7.187611,-7.037807,-6.472897,-8.791071,9.083238,-1.173598,7.142699,-4.168457,-4.104598],[2.236421,9.355946,0.136745,2.845837,-9.523860,8.479528,-7.931885,2.914110,9.857551,6.094215,-9.301655,-1.602324,3.526566,-8.867084,2.282142,-7.988674],[-2.872411,9.727999,-3.092704,-8.776262,2.987250,9.175784,-5.664192,3.815439,-4.718572,5.123209,3.363139,3.921682,0.313400,-6.375589,-0.954861,-1.349730],[-4.126393,-1.766360,-5.450830,-0.884577,-3.866008,-5.386824,-0.536569,-8.145992,-1.041929,-7.382486,-4.486063,7.334683,3.052528,-5.732732,-6.759569,1.420657],[6.933658,0.143354,-9.414390,4.934571,6.766528,7.267257,3.756262,-1.223764,-6.283238,2.921290,-8.023352,-8.347925,3.996554,3.051211,0.204040,-9.771080],[-0.180206,4.421905,0.971261,-9.521483,-3.284577,7.749923,5.686224,3.001369,-7.882835,-7.004365,6.306449,-1.498258,-9.664579,-8.661409,-9.532282,-9.734217],[-3.391604,8.987219,-7.133499,-1.197044,-0.701543,4.368264,2.105335,1.577367,7.585132,-5.683962,-8.976022,7.617052,-8.423360,9.130041,5.154447,-2.076417],[8.254925,8.410702,0.639157,-6.905721,1.808082,4.306675,-2.655520,-4.725496,6.708548,6.532551,-0.491964,-2.225918,-1.716095,1.709159,1.043091,-8.903642],[-7.013718,-9.131610,5.114648,9.387520,-6.964409,-1.006870,4.874385,6.210827,3.565028,-1.240297,9.116484,6.255467,-2.722867,1.073597,-3.428820,-9.599615],[-2.427506,-7.103860,8.278150,-5.474830,-7.136819,1.561725,-8.437339,-3.081953,9.243550,7.940688,8.879021,-8.219685,1.847831,4.572737,0.801899,-3.557159],[0.692791,-7.366396,-7.646611,-8.679664,7.525122,-3.510853,-7.581001,4.419438,-1.256416,3.901427,5.857566,9.381801,6.305594,-4.146384,1.868530,-7.731188],[8.352641,9.794949,-1.287476,7.212475,7.116787,1.349905,-8.100646,3.800295,1.793880,8.918919,3.710213,4.566019,4.388323,0.065997,5.905191,9.952664],[-1.060600,-4.199602,1.064437,-3.069525,-8.015425,-3.952634,3.646388,6.850389,-7.946258,7.537023,4.661451,6.174562,3.895697,7.610726,-2.888939,9.179821],[-1.730856,9.663618,2.386436,-5.499803,4.629967,7.023985,5.307190,0.874314,0.860165,1.192378,-9.080943,9.409593,0.866140,-8.879394,-3.340181,3.897172]],[[8.792217,-4.455822,-9.802865,-4.909308,8.811473,-9.712485,-8.346532,7.068657,7.527245,8.678524,0.732847,2.966629,5.588161,-3.037122,0.134020,-4.924265],[0.852711,-1.327807,-9.811407,9.612579,-0.885805,-0.508916,-9.861917,-4.873867,-7.626247,4.312698,-2.557046,-2.026665,-3.008189,2.899305,-7.632381,-5.844798],[-3.527650,-3.317828,-8.395842,8.604297,3.818676,2.626139,5.698884,0.659784,9.408630,9.401045,1.382449,-2.407994,-8.055520,-8.652001,8.999324,-7.281070],[5.576601,-0.985190,7.425238,-6.066305,1.623630,-8.406242,4.095004,-7.211415,-6.588022,-8.456825,-0.770596,8.270122,5.025796,7.446113,-0.633152,-4.255693],[-0.475015,9.935235,-4.562774,8.059893,-7.170434,-6.021745,5.735771,-4.415771,-3.721306,-0.815631,9.156613,-7.569929,0.955112,-7.512206,7.203216,5.935189],[1.843612,0.761269,-3.714477,-4.689413,-6.482012,-7.558112,1.212830,8.350967,5.971019,-0.554025,4.395897,0.616531,7.077980,5.272643,4.650473,-4.378416],[2.873283,-4.167840,-8.514161,-3.462485,-0.139238,5.680395,-8.601388,0.468726,-9.612348,-2.955778,-4.353103,-6.220760,8.337280,3.110415,-3.077848,-7.762291],[5.701123,4.563974,0.329605,0.249748,-7.055276,3.470823,1.425039,-4.487653,1.265529,-4.070302,0.211543,0.625501,-8.081094,0.815097,-4.115776,-9.608659],[-8.692076,-8.571561,-5.877222,4.813621,-1.933306,8.036918,-2.479131,2.465744,-6.143536,6.078575,-4.013680,1.880250,2.361183,4.704017,-4.152865,-4.769597],[5.927311,-2.871461,-0.065955,-2.194475,-3.123560,-4.451672,5.322104,-7.617259,4.588421,9.686188,-9.820605,-9.378516,5.950200,-1.951245,-2.760427,4.818074],[6.539312,3.819140,7.810848,-2.314901,7.638590,-7.618397,-4.163384,-0.702796,4.928206,9.546928,-8.108391,6.320704,5.752036,4.920096,-5.279702,9.457056],[-5.832957,1.778485,-0.688657,-2.923101,0.687359,-1.880786,0.963676,1.317531,2.849225,9.133848,9.084968,3.715183,-1.179516,-3.508026,6.134947,-0.075955],[-4.514220,-9.132253,1.015653,-5.835968,1.192532,-1.418920,2.076552,2.977959,-4.198809,9.467136,-8.719172,-1.615027,8.533692,0.196932,-8.962264,7.354017],[-1.124478,7.727751,-5.771792,-6.877046,-4.966092,-1.540463,-9.616584,-1.663374,-2.655092,-2.831586,9.633775,6.616238,1.332545,2.131209,-3.683901,-8.307750],[-7.321533,-5.037439,9.917221,9.733286,0.347154,-3.891822,7.917154,-6.478507,-6.513176,-2.650784,1.065875,-3.326972,6.589723,-7.096158,-2.412383,-9.484428],[-5.660965,1.703731,7.808107,-6.302395,9.365100,-4.482610,8.897327,-0.014196,-0.089760,2.145495,5.334114,-7.228782,-7.180366,-0.103921,-1.086979,9.932849]],[[-4.227887,-4.679195,3.188535,-7.384490,0.643994,-5.456031,-4.724250,-5.244770,1.390040,-7.645676,-4.131389,8.481690,-8.106038,5.058966,-7.199132,0.024680],[-7.131247,-1.667878,-6.903177,-4.033633,-2.227744,9.769466,2.359719,6.189175,6.455682,3.373734,-2.955274,-5.627640,3.157193,4.817364,1.271755,-9.607593],[0.658112,5.450068,0.652450,5.265868,-3.711446,-9.493587,3.694173,8.472400,-5.749118,-5.900113,4.009336,0.691371,-7.288567,0.379846,8.750568,3.793831],[-7.768772,1.307962,-3.178546,4.594053,3.516234,7.434833,9.510860,1.225140,2.915231,5.966075,3.253221,3.250533,2.523940,2.396170,-8.478686,9.706039],[5.472494,6.791919,-8.429598,3.554897,-2.922117,-9.061723,7.551926,3.612631,9.520092,3.179716,6.256133,-5.868028,4.271134,-3.544190,7.698703,2.550665],[-0.662325,-7.866584,1.657451,-8.271934,-8.095954,-2.926770,-8.479539,2.499753,-7.830675,-2.824801,8.583249,-6.973919,-8.346886,4.611518,5.604523,9.220560],[3.032681,-8.426841,2.451820,-7.705387,4.572499,9.761189,9.616364,5.706349,9.215206,4.368952,-5.285444,-8.662147,-5.654432,-5.948705,-6.281737,9.779325],[-3.497934,-0.201590,-3.607830,7.664551,0.788143,-1.090603,1.806339,-6.710425,8.455298,-7.445453,-3.591920,1.500665,-8.634323,-8.566401,6.934781,-4.307064],[8.856785,8.020163,8.746384,4.420079,2.821331,6.831170,7.936569,7.752813,-7.435827,-8.385630,-0.761256,9.927352,-6.953575,3.784505,-9.609238,3.935209],[3.180291,8.434565,8.131679,1.063266,-9.241739,-2.717801,0.633603,4.093347,7.412863,-9.273629,3.098643,-1.104129,9.580854,8.147010,9.270308,5.327374],[0.602181,1.739233,1.813130,0.254428,-8.149397,0.033011,0.855398,1.191041,-9.758043,5.600798,6.451773,6.745649,8.079237,-1.172164,7.359103,9.786600],[6.316715,-4.180114,-8.979716,-9.430059,5.372197,-1.650018,-7.999426,4.708514,4.032675,-4.155956,-9.627574,5.344385,-7.830324,-6.487555,2.455656,-0.455314],[-5.683869,7.223186,-5.468518,8.032324,4.206979,9.981633,9.933720,-8.035959,9.173334,-4.018922,0.662399,5.443940,7.699284,6.754117,-0.585003,9.050152],[-5.800797,7.044837,0.317383,-5.057322,-7.712195,-9.349903,-5.841427,-7.158626,-2.681625,8.451638,-2.972938,7.862967,-2.090655,-4.288638,6.133029,-5.353678],[-4.878375,-2.221177,-8.449656,-9.727349,-0.589274,6.827397,5.874912,-8.661441,-9.524492,1.448909,9.885275,-4.053962,-5.176327,-9.134948,6.537289,1.007342],[-0.588267,6.604337,2.122617,6.849201,-7.609723,-3.554202,-8.124609,1.470592,5.514726,5.820551,-8.205389,-8.898770,-0.050680,-7.093277,8.109976,9.430999]],[[2.997682,9.345906,-9.042150,1.552035,2.462040,-0.021249,-8.879693,-7.584274,1.890550,-4.562205,8.657527,-5.513414,3.302760,1.173201,-8.369687,-1.320868],[1.447512,-4.787072,-9.471065,5.014112,-3.539355,3.914882,2.455050,-6.540717,4.394107,-0.061725,7.337602,-5.075254,6.282394,-1.063642,-4.836191,-3.332681],[-5.773905,8.340208,-4.222466,-1.789857,8.635728,8.705919,9.262808,0.206830,1.813148,5.061625,-2.558666,9.224769,-7.448496,6.162538,8.954294,-4.953061],[9.723683,-9.679841,-2.855272,-3.943188,9.112273,1.239218,4.151059,8.935947,-2.493342,7.454050,2.305285,6.424613,-7.069811,-4.945062,-6.900489,4.050436],[8.395772,8.744834,-5.541658,0.649229,0.266342,-6.913202,1.458871,4.083812,1.560227,-6.427998,-9.202500,-5.470038,-5.043610,-1.950939,2.494440,-9.234046],[7.080884,9.337523,7.042301,1.011238,8.304602,2.951113,-9.144774,-5.953259,-4.140774,-9.782088,-1.667599,7.198066,1.653897,0.628143,-9.579530,1.637317],[4.462583,1.050551,0.057350,-7.977746,5.776383,3.056843,-9.919687,2.445296,-0.129275,9.740162,-8.671535,-3.206706,-2.225916,-4.314003,6.008248,9.235584],[-5.570749,-2.396267,8.934582,-9.006823,-2.862718,-3.302895,-2.048420,3.850105,3.993681,4.669124,-8.740023,-9.377655,-2.127379,0.002117,-6.908353,-9.388557],[7.862347,8.766323,0.585921,6.982433,8.008604,6.915101,3.055177,9.991675,4.694895,-7.376143,-8.920278,4.419099,-3.658548,-8.531775,1.963875,0.173770],[8.243465,4.427203,7.381975,6.660002,7.483459,-2.086767,5.498291,3.884092,-9.943539,-1.537841,-3.291553,4.932633,-4.064344,-4.153441,3.172148,3.673976],[-0.192780,6.389946,5.209371,-8.688446,5.665152,-7.421043,-8.485953,-1.018705,4.586859,0.956125,-2.158882,-3.649692,3.299250,-0.251000,0.126669,2.213307],[-7.867500,3.183500,2.046637,-1.522223,-7.079367,-3.764647,0.673147,4.804270,0.573164,-1.153775,-9.833798,4.241243,5.496562,-4.679195,7.223624,-2.989543],[-5.650302,4.747638,-9.757966,7.119755,-6.813986,7.376154,-9.805843,4.869189,-3.327007,9.897419,-9.099054,-9.602024,-3.423563,-9.716111,-1.857619,3.294793],[-5.914489,2.745175,1.080075,7.652497,-7.171615,4.134419,-3.342029,-3.149020,-0.544097,0.024646,-4.009749,6.790221,-4.637430,-3.185318,-8.803763,1.760008],[0.357586,5.805604,9.300661,-5.272950,-5.307721,-3.273887,-6.472734,1.754848,-8.446258,-8.156690,-6.168880,8.388848,8.383180,0.783887,-5.321230,6.719109],[5.042913,-0.619299,1.557465,-7.850963,-3.782338,-9.556906,-8.967177,6.891197,-4.301746,0.147445,5.439850,8.530068,3.986266,8.360933,-3.054323,6.811565]],[[4.614861,-2.844969,-1.123061,-5.467684,-7.688719,-7.394589,-1.702699,7.067844,6.122186,1.888030,-7.462559,0.362627,-6.486933,7.915418,3.528758,-6.394590],[-2.467504,-0.790884,-7.372151,2.505635,0.968873,4.818995,6.795556,0.160710,9.703655,-1.188083,9.511997,0.964681,-0.778453,-4.753618,0.463548,-6.298084],[-0.061842,1.379740,-3.464564,8.522937,-6.301339,6.346299,6.216297,-1.497490,-0.964107,-2.278434,-0.041529,4.701693,-5.313599,8.746031,-8.477042,6.365619],[-3.878952,2.148651,0.245774,-7.894394,7.844957,-9.591531,-8.943407,-7.622167,0.083017,7.144657,-5.624489,-8.127868,-1.639563,4.131847,8.594144,7.061363],[1.447020,-0.213195,3.995187,-5.375118,7.225230,-5.021530,9.611205,-0.362320,9.603472,-6.645849,-0.920473,3.117922,-8.891786,0.687674,1.723608,1.276553],[-4.600575,-6.173729,1.666902,-8.572069,5.167819,-6.636738,9.917559,5.592683,-1.859622,2.165432,-4.723336,-3.391771,0.917491,-1.137951,-0.983859,1.694901],[-5.343406,4.063780,-1.376940,-4.914454,-8.459498,-4.765392,8.904485,-8.165860,8.758895,-6.604695,-2.891348,2.722015,-4.324504,1.038317,6.673829,7.565982],[-6.298132,9.716421,2.847381,-5.388670,5.099591,4.415694,-3.407334,-4.751209,7.904310,7.211647,5.274343,3.282041,-1.785210,9.321948,5.630860,7.923385],[1.579059,-5.669541,-2.307663,-7.946033,6.765555,-6.753345,4.709610,-7.923278,4.861541,3.324907,-6.161898,7.063414,7.370235,-2.532920,5.023294,-9.231214],[6.901057,7.020533,2.954453,6.780960,-2.080121,-8.731433,-3.702133,-2.564482,-1.475805,7.733677,5.468312,8.755928,2.390537,9.426986,-4.852520,5.551769],[7.808808,0.952744,-9.028334,6.723679,6.044538,-2.737034,-7.347929,0.074527,-9.950038,0.283335,6.697206,-7.850530,6.287707,-0.649951,5.645852,3.298107],[-8.079980,0.411644,7.839150,5.219243,-3.544626,-4.595407,6.817159,1.313549,-1.351848,7.149493,-9.927829,-1.533213,1.049506,5.654253,-8.891503,3.910354],[3.576710,3.250053,-9.037523,3.574181,3.842923,5.865155,-6.959867,-7.001167,-8.516353,-9.181143,-0.410516,-9.298816,2.572336,-9.123242,-8.382382,6.563309],[1.081095,-1.874861,9.596923,-5.884525,7.003083,1.894348,0.895916,8.320287,4.841766,-9.490589,-2.455054,-1.899099,-2.382301,-0.010181,-7.714385,-0.539533],[-8.924760,6.213916,0.214279,-4.615482,-2.154034,-4.324392,-8.360156,7.362621,6.418868,6.400231,-1.196906,-1.097972,-0.132550,7.017230,-4.943309,-3.879313],[-9.194307,-7.471615,-0.201997,-4.901361,0.919826,-3.788360,-4.388300,8.341637,5.415903,-3.383359,-6.201560,-9.395840,8.719245,-7.750938,0.164672,-5.939231]],[[-7.414931,0.135581,-2.272760,8.546626,-2.582718,8.440342,9.842475,4.279854,5.909662,-9.841610,-3.614295,-6.219039,-9.213277,9.831845,-9.492220,7.272378],[-0.420443,3.205644,9.811840,-0.768145,-0.433756,-9.428478,6.019620,-0.460526,5.480523,-7.255412,3.749026,3.525606,0.575060,5.595432,9.189656,1.392239],[-2.599545,-2.122683,8.373694,8.570899,-4.132794,-3.429727,6.008713,-3.625713,8.511053,-5.017990,6.844218,0.727287,-9.797563,-5.083111,9.816683,-0.136193],[-1.233043,8.892341,3.928408,3.737359,5.581268,0.527480,-1.565749,5.474659,3.836437,-3.377816,-5.742164,4.435728,8.460205,-6.734087,8.605074,-8.010129],[3.151421,-1.797532,-0.339639,-5.892161,5.873049,4.472865,2.935890,3.152405,-7.392324,7.494242,9.796379,-8.446685,9.164548,-9.510709,1.573069,-9.627912],[-7.508918,6.781069,5.184157,-7.221748,-0.149840,-4.644355,8.526642,-3.080773,-5.171312,-2.405822,-5.609500,-5.146858,2.255600,6.384303,9.982062,8.361204],[-0.101888,-5.513510,-8.717134,-5.776124,-6.645509,-7.108293,-8.641967,-6.403200,-5.640183,6.996015,0.068664,-1.116998,-6.825978,6.934166,-7.376404,7.412330],[6.534390,-0.192742,7.377426,-1.721058,2.521607,9.821290,9.943824,-8.452557,-3.781567,9.398201,4.499228,-5.255677,2.514507,5.992865,-6.189016,-3.018756],[4.831872,1.106438,5.776695,-9.433751,-9.997588,-7.938614,9.507731,1.361495,-8.423773,7.161867,8.461664,7.239435,0.708474,-9.252522,-9.004754,-8.878160],[3.007212,-6.096211,8.654672,3.803967,-4.881970,-6.102748,4.939257,8.752784,-3.255595,1.424055,-6.231787,-6.041904,-3.898277,9.172979,2.758501,-3.158114],[0.222503,9.124221,8.351416,-8.724628,-4.541888,-2.763944,-9.993559,-0.842555,-0.849381,-7.965470,-8.853579,2.988914,6.080956,6.159592,-5.857920,0.436682],[-0.203341,-8.511906,-4.104670,7.057363,4.253740,-2.057177,2.143734,-2.387424,-3.923801,-4.061333,6.124079,8.084043,-1.261706,7.801807,-3.667318,-5.504981],[5.900710,6.698111,0.874074,2.548271,-8.247883,7.030006,-3.953420,5.341016,-7.741804,9.709894,8.626114,1.697371,-5.087329,-2.140494,5.901498,0.543100],[-3.811370,-0.495002,-1.123529,-9.429467,9.737690,-4.457856,-2.692010,6.369957,-0.525433,-7.876129,0.284342,3.233474,4.777362,8.072255,7.154265,0.217649],[9.477560,3.602018,2.576266,-9.661379,7.064603,-5.982660,-5.433103,3.283867,5.928103,9.056245,4.496723,-1.076824,-8.758419,3.949908,-8.861243,8.825650],[7.655526,6.335422,6.114820,0.439241,1.661145,-8.541267,5.611441,-6.913058,4.388756,-5.896915,-4.651545,3.524680,-9.775127,-1.749889,-4.917303,-9.110680]],[[2.653024,-2.452799,6.878551,0.482879,-2.226758,-4.594487,0.593983,-5.155525,-1.466988,7.052822,6.017753,-1.713025,-5.905769,-1.795736,-2.253633,-3.173735],[7.793576,-5.272706,-9.061548,3.640852,4.681517,6.917023,-9.236294,-8.352425,-5.595015,6.916884,-9.941896,3.126668,6.849959,3.966616,-7.118671,1.224840],[5.411166,-4.794562,7.786473,-3.963446,8.765671,-0.396233,2.381588,8.893520,-2.108289,8.585457,-6.075170,9.684690,-8.884303,4.649126,-9.269875,-4.167596],[6.594056,-6.351159,-0.528104,3.391744,-1.617759,8.030964,-7.187965,0.765439,-7.978866,-9.516632,4.189922,-0.178690,-1.780683,-8.949538,-2.574671,-4.269190],[7.646602,-7.023907,6.852665,2.561509,8.964229,9.593532,6.531317,5.830440,5.215910,-8.566028,9.943462,7.556325,8.456633,6.674292,-9.312936,3.666463],[-9.176581,-5.069290,6.626350,9.153103,-2.076557,4.361574,7.665627,3.443300,-9.101466,8.887141,-1.293460,3.738766,-7.496959,0.369882,0.190392,-1.031408],[9.672734,1.244741,-9.684492,2.022767,-4.665277,0.203739,4.408269,-8.608990,-2.455430,-4.795344,-9.219807,-8.157949,-9.245613,-3.802001,-6.991041,2.612274],[2.073093,2.693243,7.524129,-2.182831,8.949062,5.528583,4.662261,-3.130364,2.246287,-1.570990,-8.280213,-6.274141,3.735002,-7.149741,0.620711,1.977720],[0.683516,-7.187891,7.294853,-9.446120,-1.191975,-8.829825,0.763237,-6.372283,4.874951,9.397350,3.156234,-8.292498,-6.508509,2.972258,-6.995422,-6.999290],[3.111374,-1.042457,1.598191,9.064262,-5.343940,5.988719,-9.266877,-4.024033,0.170755,0.860285,8.007591,0.151996,0.212031,1.585029,0.394789,8.606569],[-3.283877,3.466249,-6.086240,-0.035880,-7.803703,-5.399575,5.007291,-1.965832,-9.167706,7.330883,5.811235,7.944924,4.010851,-9.738346,-9.250461,5.600863],[9.546769,5.996739,1.118745,-2.822974,7.808539,-8.561900,4.999519,6.217240,5.826555,1.594738,0.616529,3.204830,1.377886,1.598748,6.437856,9.302634],[-6.499169,-6.285439,-7.265924,3.451269,7.569635,-3.919406,6.095684,3.241659,-2.142132,9.014825,6.944945,1.163820,3.417665,9.148886,8.249993,3.050084],[3.699731,-9.369205,1.400177,1.767506,7.526247,8.880075,-6.210341,6.410402,-5.860266,-8.166051,4.449948,-2.120860,2.196367,8.390366,-0.848866,-6.921640],[-5.961960,3.913119,-8.380115,1.526464,-5.797163,-5.706851,7.632070,-7.742529,0.001263,5.430917,-8.227777,6.401096,2.391225,-1.623236,9.539139,1.603161],[7.381962,2.030511,-3.940738,-4.346647,-8.001016,5.520697,-1.873473,8.808878,-5.392431,2.546079,-6.714647,-2.071275,3.635858,-5.026275,2.095995,8.893855]],[[-4.762093,2.053092,4.111503,-5.860151,-2.052344,9.678583,3.761562,-0.662577,6.250626,-6.607965,-0.997845,-2.343425,1.947290,6.718904,-9.572670,-3.771269],[0.764490,3.186303,6.342603,-1.421818,8.880590,-0.336840,-5.782487,5.997086,-7.050527,-5.337587,-1.674518,7.510188,3.738963,9.029877,6.902478,-7.195261],[4.204428,5.228951,1.865990,-7.739042,5.174676,8.471047,-9.244355,7.877298,-7.415366,9.864057,-9.488752,6.405128,7.856189,-6.165872,-4.723305,-8.176662],[-4.032993,-0.772884,3.483768,1.401224,7.544407,1.331519,3.060699,9.992396,-7.873844,-9.457433,7.086474,-6.078189,-8.192864,6.908945,3.737312,-2.212382],[1.967921,-1.788816,-3.534720,1.593426,-2.042355,4.476848,4.034653,-8.541389,2.745995,2.723330,-5.760777,-7.490556,-5.657172,2.863164,5.725003,7.585776],[-5.638643,8.932848,8.248221,-3.058100,4.322463,1.833930,-0.970504,-0.781862,9.690142,-9.116163,9.998560,-8.633865,-6.540941,-3.924377,-1.268646,-4.317617],[2.658508,2.165420,-3.818301,-5.617435,7.751888,5.779965,5.090885,4.922521,0.299038,-1.081735,-4.375426,-8.314963,-6.401008,-9.508679,-9.709412,1.015309],[4.581973,8.942902,6.239279,9.591047,3.776109,-3.351474,3.905027,1.554469,-3.323374,3.658380,0.609021,7.641830,-9.096899,-4.641572,0.643127,-4.176418],[-3.029605,-3.115440,-5.288774,-0.402951,-6.211780,-4.694615,-9.168823,-9.580473,-7.233580,-4.181439,5.021270,5.359840,6.410009,5.593324,-2.742672,0.754080],[9.355350,-5.103923,-1.565755,2.427091,1.477565,-3.475050,-6.797391,-2.942868,-2.489892,-9.255134,1.731694,-2.217319,5.849757,7.974089,5.720000,-5.720622],[-6.327300,-3.671279,2.915921,-4.061221,-4.419895,-4.724465,6.168452,3.741227,5.564409,-4.706462,9.952441,-0.020499,-3.335575,-1.276463,-4.581566,-8.883530],[4.291691,0.442545,-9.178149,-8.591575,-1.346699,4.035368,9.258261,-8.340217,-7.550868,0.820924,5.157573,-7.635631,7.200426,3.524027,1.973248,1.555644],[7.817294,2.640856,-3.955295,-4.085324,0.093775,-4.574277,-4.679305,1.747598,5.199617,-2.235473,-4.711657,-1.880188,-8.264634,-5.115680,0.921040,-7.738385],[-5.856393,8.517911,7.045415,-7.846418,9.135963,-3.248323,3.371828,8.045804,-3.645331,5.437298,-8.350401,9.821487,4.236394,8.490988,8.004686,3.833585],[3.048186,-5.148107,-0.114883,4.975255,5.560603,8.170430,-8.064962,-8.593152,0.112557,3.010186,9.006691,-5.652077,-4.070992,-2.121431,9.086583,-5.986384],[-4.745486,-7.547453,0.108242,-8.347588,8.139611,3.014113,-2.202400,-2.315546,6.457867,-4.254745,-3.176166,3.906749,-6.971814,-5.558357,-9.299427,-9.003971]]], dtype = "float64")#candidate|9532|(15, 16, 16)|const|float64
bop_9533 = relay.logical_or(call_9518.astype('bool'), const_9532.astype('bool')) # shape=(15, 16, 16)
bop_9536 = relay.logical_or(call_9519.astype('bool'), const_9532.astype('bool')) # shape=(15, 16, 16)
uop_9537 = relay.asin(bop_9533.astype('float64')) # shape=(15, 16, 16)
uop_9539 = relay.asin(bop_9536.astype('float64')) # shape=(15, 16, 16)
func_7050_call = mod.get_global_var('func_7050')
func_7053_call = mutated_mod.get_global_var('func_7053')
const_9545 = relay.const([9.256645,-2.152814,-5.853773,8.679745,9.131770,-3.860165,-3.881356,-6.598185,7.088996,-8.025969,9.488087,-9.496110,7.865752,1.018468,7.464843,-0.191354,6.127835,1.633389,2.287243,9.716273,7.141559,6.210294,-0.105499,3.776537,-2.562243,1.835172,6.260465,3.978045,-8.170403,-3.251822,-7.759572,-7.730076,3.584182,3.865905,-6.243903,7.530859,-7.665488,-1.694551,-0.939243,-0.402529,6.687232,-5.391321,-9.344012,9.535060,-0.342472,-8.434053,0.589314,3.965415,8.114443,0.841923,7.001127,8.610360,4.916614,-5.951777,-2.393043,-3.874394,6.818212,-0.277630,-7.450255,-7.044506,8.357259,-7.505875,7.745008,-9.720939,-6.016717,-2.880812,-9.664313,-4.624350,1.745934,-6.680951,1.816060,-7.990857,4.913048,-1.114276,-9.894830,6.413457,-0.664393,-0.204098,5.361166,-7.135919,-7.731473,3.512554,-8.915978,-7.858744,-7.624272,8.936826,-2.905886,-2.207844,5.307379,7.080403,9.708723,5.530536,-3.230802,6.998083,-7.192783,-4.685241,0.760341,-2.081728,1.203077,6.423006,6.913107,5.717197,-3.190137,8.560707,9.123678,-5.760775,7.267461,-5.530248,8.567370,5.621417,0.944792,6.055696,9.928181,-9.557684,-0.153801,2.593668,9.931530,9.759155,-8.068691,5.184027,-3.681037,6.187583,9.064455,1.638212,6.317909,4.685961,-5.031593,2.430023,-8.125485,-2.957414,-2.220885,-9.919670,9.892585,3.821119,-8.537410,8.979152,-1.955317,1.510984,-4.243729,6.904485,8.941256,-0.357525,0.101945,-0.599176,0.955505,-6.846062,-8.112593,9.245404,5.892569,4.763013,9.857465,-5.348969,9.580912,-7.478972,-1.544258,-5.994958,-1.322228,-5.652661,-2.502834,9.728507,8.274715,4.659430,-1.158242,9.659531,-7.016271,6.811880,7.615728,9.023297,8.925335,-0.608980,3.167869,-2.199183,2.550426,7.830736,7.589698,-4.710126,2.817172,-4.480010,-6.806005,3.474124,-4.236832,6.001826,-7.879804,8.591195,-6.641467,1.853297,-3.184204,5.051044,-9.759863,9.747282,5.862008,5.826037,-5.652721,-2.048758,4.337945,3.535864,-7.093925,-4.585113,7.981139,4.370089,8.133956,-6.479100,-3.528159,-1.428783,-7.412663,-5.669509,3.932509,-7.987467,8.582611,-8.466411,-3.236993,-8.900827,-0.946070,1.622381,-0.547609,6.776332,-8.932677,8.786024,5.230737,2.340037,-9.635041,8.650941,9.667657,9.150231,-5.223738,-0.779356,9.068662,-1.258256,2.114852,9.223386,-9.231770,3.811524,-6.908091,5.165535,-7.287989,-3.000965,-7.626257,-3.068689,1.265082,-2.219969,-9.158912,1.521750,6.104183,9.431850,7.842420,2.452862,-1.457378,-9.454931,2.421114,-5.683224,3.364665,-5.794269,3.594093,7.882678,-1.063233,-8.763664,-8.537075,-7.096909,9.450674,-4.409813,2.973277,-7.624819,5.693956,-0.551454,-9.667647,-9.531528,9.519633,4.392462,-3.922035,-5.923124,-6.486337,0.376199,-7.739793,9.583648,5.271082,-8.686832,2.564171,-1.631694,-3.190071,3.818424,-7.582833,-4.117149,5.390323,-4.282611,-4.036144,-6.895204,0.834394,-7.578517,-8.124226,-9.415321,5.221530,-4.562241,1.971022,4.839825,8.360562,5.068436,1.639917,-4.069816,5.519349,-0.269742,0.615190,0.474845,-8.043494,-7.496246,4.489132,-2.263639,3.973490,9.237240,-9.718591,-5.944348,4.893396,8.904234,7.993355,8.917161,-9.831858,6.957466,4.658195,-1.782490,-1.412973,-1.803165,2.217937,-6.840611,3.218887,-0.865483,1.020387,7.446427,-6.279268,9.988395,-7.713582,-8.117934,-3.236897,-0.143335,-2.507743,1.563469,8.437827,-1.245613,-2.378117,-8.148357,-5.068132,4.072384,0.413915,9.014442,6.548279,-8.214985,8.478335,-7.726778,-3.862982,7.735306,-9.290714,6.355662,-9.275413,-7.870367,-8.170067,-4.130131,6.977418,-7.473293,2.160322,-8.032826,-5.440643,-4.659887,-7.757346,3.319145,-6.335850,5.250397,2.272831,-3.043114,6.216630,5.913507,3.546704,-4.525758,8.849452,-0.107272,-4.799176,-9.659639,2.221457,0.683314,5.293308,-3.623675,6.616311,-2.201447,-3.978641,9.330158,-0.345851,4.081743,-4.082232,-7.648691,4.528200,-4.453604,-6.299102,-5.146118,-8.270675,4.388957,8.622154,8.904775,6.847457,0.287616,-4.999607,8.228815,6.297969,7.890141,5.551866,-9.398733,-6.256237,-4.586596,6.672606,-4.835434,-0.828611,5.481302,5.044035,0.717783,0.648858,-7.800192,3.131883,-3.222364,-3.069453,-2.886055,8.482476,-9.060256,-6.102592,-6.073298,-8.230471,1.969511,-3.438142,-7.258810,8.321811,2.451573,-4.706072,-5.364791,7.963758,3.714697,-5.220586,9.119007,-4.921569,8.668099,9.364394,-7.523771,-3.248870,-6.513615,-5.952342,-3.738202,-6.561480,-1.196613,6.428288,-5.046450,2.254613,2.617977,-6.303417,-4.839363,-1.469717,6.677704,3.377563,1.447780,2.689104,0.589675,-0.210504,4.820240,1.020551,-5.419194,-5.142167,6.927849,-4.628424,-6.517088,-2.340148,7.571664,-9.833593,-5.132945,-1.637122,-0.493324,4.732795,0.181280,5.612632,5.060023,9.111720,-8.537557,-3.188518,3.723194,-4.298580,3.001457,-7.270592,4.968598,8.248370,8.976674,-1.964876,9.982482,7.441842,7.090747,6.736595,8.036650,-9.651820,3.749416,2.790938,6.663480,-0.040935,-9.710437,4.522282,1.117584,3.142167,-2.898289,-5.335788,-7.693418,1.480151,0.379553,-3.472653,0.932206,-1.311229,8.315520,4.579358,2.677774,-6.362871,1.007289,9.431582,-3.245877,3.251956,-4.026423,3.468738,4.949448,0.439790,0.039567,5.318143,-8.418503,4.694368,5.069260,3.918848,-5.484961,8.569414,7.941139,4.399647,4.870210,8.662510,-1.146517,-1.146056,8.721152,-2.016660,3.906106,3.288245,6.580976,-0.517637,9.883994,6.964106,9.695688,7.290249,-1.454537,-7.092434,8.710624,6.101442,-6.132379,3.369373,6.457561,6.410647,5.673041,1.221863,0.022339,-6.364141,7.442165,0.210367,-7.204229,3.017538,8.074373,-8.271016,9.751127,-4.921588,-4.697763,2.412604,-1.187507,-5.937750,3.215325,-0.433361,8.344859,-6.115085,3.873990,5.789880,-1.714775,-7.867091,3.753643,6.402509,-9.126192,-7.499344,5.218518,4.881551,-0.740626,-0.769675,5.593287,0.409233,8.652138,5.583778,8.445252,-7.298344,3.231590,3.112421,0.394688,-1.504103,-3.448781,-8.233527,-8.400610,3.556203,-5.622867,4.706692,1.801231,-3.551717,-5.410345,5.224217,3.775976,0.200210,-3.863803,9.606984,8.298806,9.854097,-3.138898,-0.918476,6.634588,-8.515460,7.783020,0.576218,-1.287682,4.214259,7.633684,-6.581856,-4.292057,-6.239419,-6.262812,-8.170502,1.705155,4.782444,-2.197104,-3.601039,-8.406555,2.928320,-8.285685,-4.271441,-0.791172,6.963364,-9.222626,-5.452516,-0.401521,2.772694,-1.466815,-3.891501,4.073787,-2.594336,3.907599,-4.343193,4.207462,0.333506,-9.386404,-9.945578,4.771722,3.096024,0.438729,-0.935033,-4.715992,-9.675438,-2.988623,-4.164213,-6.196607,7.446423,3.144442,3.370394,0.543447,4.199079,-4.671486,-5.510267,2.222898,5.301808,-7.434444,-4.869185,9.205182,5.799323,-4.585856,-6.827018,-0.511887,-8.643979,2.707849,-8.861723,5.446864,-1.016684,3.393849,6.767876,-9.498913,3.535475,2.643447,3.640453,-3.296442,-7.667758,-0.823068,-9.422463,-4.125715,6.147630,-3.457049,-6.192582,8.292318,-7.820716,9.523295,0.329760,-8.927077,-1.770033,8.029313,3.662695,9.270514,-7.052077,-2.878756,-6.453278,4.388686,-7.372685,-1.898477,3.847360,4.492166,-6.601667,-5.367473,3.789153,6.781800,-6.121803,4.134695,-4.673799,1.083081,6.240897,2.845445,-5.680824,1.264738,2.155604,6.565463,4.885213,-3.072315,5.601157,5.314428,0.357976,6.064956,8.799164,0.550862,6.551133,-3.154393,-5.901816,-6.898771,5.980419,5.043886,2.385621,4.034748,-7.730423,6.571708,-1.979325,-1.377300,0.228062,6.949015,-9.102899,-5.309149,3.694161,-7.135810,9.583153,-5.464354,-8.144987,2.331168,-4.703164,-1.478510,-7.702999,6.720365,8.113169,-7.238868,2.971848,9.094476,7.072273,8.527759,5.678914,-9.157322,-0.253961,4.902991,6.321878,8.721307,6.309971,-3.224892,5.933765,6.516311,1.304541,2.598931,5.192936,-1.124065,-7.155618,-1.122508,-4.993523,-5.546571,9.899928,4.386761,-4.373564,4.564753,3.312579,8.002102,2.829817,2.668753,8.724061,2.893858,0.907306,3.321630,2.818760,5.138470,-8.985466,-8.616305,3.198809,-2.529340,-6.656068,-4.611441,5.846859,-5.335378,-7.726515,9.202142,-5.418047,-8.658121,0.390879,-8.150291,7.559835,-7.517177,6.253256,-6.248840,-4.618919,5.180222,-2.192660,-8.192911,3.887941,-2.472580,-6.002614,1.589856,-3.991226,4.325856,4.642240,-2.041019,7.181344,2.084911,9.124274,-0.464725,-4.219979,4.761696,6.553532,7.890334,-6.389887,-2.236745,4.935240,-8.575923,8.091921,0.936499,9.683070,-5.889221,-0.748941,0.035325,5.525632,-9.546462,6.240285,-7.511537,3.231694,-8.733983,8.952489,9.087129,-8.075624,-0.175506,4.697456,4.490670,9.413873,8.514757,5.842955,8.827727,-7.225329,-7.812972,2.428134,-4.841691,-8.083161,4.666516,6.545854,5.806172,-8.503858,-0.227316,9.162538,-3.353348,1.945067,2.814905,-3.476531,6.824694,-4.220934,1.063487,-5.411007,-8.684172,-9.277243,-4.314963,-6.971259,4.135341,0.947693,-9.930275,7.560946,8.135162,0.599996,0.145987,5.080334,-8.233165,5.536051,-4.263318,-2.619051,-2.118006,-4.678917,-2.411948,-4.168829,5.374308,8.670724,3.683901,-4.841743,8.002792,9.817453,4.227409,5.853037,-9.691534,7.831129,-5.442258,2.839424,-9.787153,5.122908,3.030314,2.996605,2.869345,-8.992538,5.517139,6.942965,-8.738014,-0.712664,-8.931890,-2.919505,-5.690769,7.201919,0.919569,5.219218,-8.079415,-4.719384,8.093821,-1.804746,1.841022,4.116065,6.420539,0.272528,5.979173,9.704934,-6.322645,-9.814526,-2.219489,2.598471,-8.961727,2.434660,-2.774295,-1.759582,0.453621,-3.764471,-8.892965,-5.850610,3.055004,8.146186,5.902649,-5.104986,-3.558658,-1.064107,-6.153357,-2.169611,-9.869065,9.872710,-0.991410,-2.683341,-8.314770,-6.480824,-2.488940,-0.564767,-9.512501,-4.958912,-9.581380,1.746289,0.098248,8.859232,-0.453983,2.913481,-4.682290,5.575383,-3.207129,-2.388335,-4.478575,8.915607,9.917809,-3.150915,-7.678208,2.557516,8.279498,9.051237,-3.229577,-4.977110,0.127133,-9.762237,-9.339867,-1.672461,4.224226,9.090361,7.695545,9.587491,-8.217115,-4.035456,-4.830189,-8.937923,9.085866,6.214543,-0.482523,-5.951706,6.583984,4.449468,-5.734845,-9.742088,6.535714,6.619850,5.603387,1.638305,8.891215,-4.294159,-2.820868,0.896398,-2.862107,1.297545,8.947871,-4.432718,-8.876125,-4.181324,1.082399,2.246626,5.489712,3.299220,8.330117,-2.466925,0.588192,-9.887216,4.985804,5.167041,-9.370528,5.810142,-9.549060,-2.769643,0.298401,0.923210,-7.740495,6.053395,2.448728,-7.313269,-8.810683,4.923829,8.771740,5.316754,-3.148479,-9.439423,3.614338,-9.001073,-2.097046,0.199119,9.652557,-7.566649,1.730187,0.931947,7.054790,3.533831,2.944650,9.065818,-3.929529,8.795020,6.147374,-5.990584,1.767845,-1.417383,6.436814,-8.168620,-7.066198,-0.345243,-9.456546,-9.000346,2.050587,3.488352,3.915965,9.487411,3.703171,-6.509482,2.209530,-1.298272,5.906590,-9.125914,-1.929057,4.264283,8.699264,-0.094119,-1.508368,6.159056,-1.030067,-7.296350,9.605725,5.938923,-0.638990,2.464227,-7.967271,3.158095,-9.090055,2.991136,-1.415897,4.595187,-0.380740,0.944664,5.639218,4.678631,-9.058541,7.068153,8.993732,-3.274410,-7.484164,9.481792,2.598624,-4.108449,-5.027668,-4.811323,-4.094674,9.737941,6.695386,1.539381,3.889434,-4.591927,-8.569785,-1.909833,5.871081,-3.039503,-0.231138,-6.625232,-3.633270,-2.444438,-1.710371,5.674544,-3.165982,-0.510777,7.640473,-8.462598,-7.982300,-0.136679,-5.665836,-9.475762,-4.444623,0.750057,3.381501,-2.108047,-7.739080,-5.099753,-1.446734,-4.597275,-9.880541,-5.374986,-0.083494,4.338070,-0.397902,-5.177658,-5.476008,-5.946578,3.992135,1.560937,9.681200,-1.836463,-8.234364,6.566460,-8.953336,-4.606484,-4.136093,-0.520282,9.782597,4.747273,-8.166874,8.697019,-0.261933,6.908548,3.654118,-4.624927,-1.185845,2.845875,-0.408581,8.180104,-7.629260,7.623622,7.301400,1.532484,2.376548,-5.236431,-2.548274,-0.116966,1.604882,-8.377959,3.248606,3.944436,2.898276,-1.268346,9.772629,-6.925542,0.839665,-5.480891,-0.867175,-4.614887,-0.797864,4.533875,-9.405317,-3.607748,3.787061,-4.788995,3.379817,-9.107458,-9.510858,-3.774820,1.445568,2.801083,5.302053,6.499333,-5.269472,0.406662,-0.876940,0.073804,4.321010,-4.854191,4.008815,8.878370,-3.448988,0.225060,-3.943947,5.408156,6.510818,2.414011,-2.703145,-9.370845,-3.073449,-8.597932,-6.070240,3.504265,9.535411,-0.035433,-8.113353,2.044828,5.507457,-8.392968,7.055414,6.849345,-8.184122,3.519649,5.782505,4.227240,4.212048,-9.280117,-4.283160,4.746824,8.402728,-5.468242,8.937686,3.472282,-9.575361,9.818787,0.725462,-7.651860,7.694951,-6.120856,9.442509,-6.828723,7.710830,-7.323843,-4.444171,5.440362,2.429064,7.651297,-5.093756,-4.518820,-0.784093,-0.805472,-1.552934,-7.543693,-5.939843,7.825879,-6.170153,-0.117358,-5.952863,5.754827,8.876329,8.374447,-6.703010,0.765546,4.249524,-2.869475,4.349567,0.374942,2.709674,3.061201,-5.059916,-4.059232,-7.835626,9.327269,0.534027,2.496346,6.564635,-0.504442,-3.718459,-1.714158,2.618894,6.674181,6.445470,-0.640079,-9.795350,-8.109414,-2.083507,-4.872164,-6.825421,-2.229347,-0.362828,-0.126842,-6.062596,-5.377611,-5.600668,-1.056180,2.492838,4.742806,-0.139908,2.080796,8.096661,7.119540,-5.640696,0.673467,8.940120,0.087735,0.314998,-8.028674,-5.053858,-6.091888,2.557029,-8.900782,9.064835,-1.206223,8.126275,-0.293754,2.374030,8.243487,6.411788,-6.628398,-9.511004,8.349681,3.314714,2.829451,-7.078647,0.976887,-0.682074,-7.050217,7.542342,3.136194,-0.853672,8.764356,3.943344,-3.238942,6.774942,-4.097311,-5.465338,-1.622707,1.002425,6.729661,0.634187,3.850249,-1.849440,4.890953,-0.558748,-0.819901,2.779650,4.813671,-9.038932,7.112268,-4.463616,9.534538,6.152162,0.899055,0.207966,-8.370001,7.901969,-6.672432,2.488769,9.080476,-6.552460,5.049226,9.429300,1.185967,-8.037218,-9.596912,-4.703694,7.913014,1.884131,-9.917550,4.963767,2.782601,-2.929598,-2.570582,-6.815095,-2.757084,9.670578,-6.673426,-0.699308,5.831459,-1.484733,2.414319,1.107508,4.240443,8.976838,-6.404656,-3.219192,2.974933,0.424815,0.652842,0.339724,8.333803,7.418614,-1.358704,2.063058,-6.569842,3.081853,-5.679568,-2.514214,9.888970,2.824669,-1.733069,6.421222,-2.858371,6.826985,-4.336039,3.931036,4.528938,1.684130,-9.755594,2.230822,3.819509,7.336499,-9.920141,1.021090,7.840971,2.665860,-4.015690,-5.421703,6.435363,-0.308844,-5.719230,3.435871,-1.245965,9.961308,9.273574,7.357161,3.434216,-7.057528,-8.116366,2.015972,-3.001273,6.767569,-4.340754,-5.420842,6.075445,9.287609,-6.819417,-2.209085,-6.501278,-9.811849,-0.235779,-1.265682,-9.503691,0.146812,-6.044613,-0.625137,5.765843,8.593254,9.534616,-7.451749,6.114920,9.237597,-6.904872,-1.862041,8.617202,1.396874,4.995590,-8.341285,-5.560862,-8.116150,-5.243828,-4.851294,0.053168,4.026554,8.693460,4.141529,-2.592118,-9.827607,-7.629207,5.623955,6.815138,-5.372366,-0.208926,-1.554972,-8.979776,0.218219,-7.481808,2.581289,4.539105,-2.966166,-0.656365,5.438528,-4.142984,7.455882,9.694517,5.813346,0.357313,0.718862,-2.594114,1.119332,-8.529158,4.497905,-0.411729,-1.119143,-2.676664,-7.450504,2.576173,7.161267,7.621250,-4.523517,9.037628,-4.470028,7.235390,-0.772819,6.589661,1.018543,-8.002366,-9.417833,7.184729,-6.828014,-7.952168,-4.027940,3.465116,3.570533,-3.189593,9.682697,7.817560,0.397767,9.612559,-1.460825,1.503282,-4.017011,8.037674,-2.633455,-7.578265,-1.939439,6.654948,-7.194492,-0.489055,0.467204,4.047881,-2.264632,-7.937109,-1.508699,2.697179,7.748112,-5.040469,-8.988428,-8.254562,-5.377480,0.207570,1.781151,6.140048,8.114477,-6.609531,-0.920283,0.570976,-8.699521,-4.659304,1.278400,-6.327946,-5.941753,9.658142,-4.471029,0.686513,-7.785730,2.292304,8.720322,4.357563,-6.176747,-6.541339,8.127961,0.850582,0.495370,-0.069903,7.092606,5.086266,6.463134,-2.638966,8.523444,-3.676787,-2.248830,2.565627,-6.426644,0.422606,-4.409483,-4.285668,1.020821,-3.717326,7.601265,-4.428247,6.872048,4.689781,-3.684687,-5.200567,8.964060,2.284287,-1.537764,-5.608550,4.128541,5.527719,7.304941,2.049744,0.502860,2.629631,1.314302,5.041239,-0.390777,3.137549,-4.643716,-8.752100,5.210471,0.775621,-3.373068,-0.770720,1.987624,-8.915691,8.860533,-6.038141,6.683558,-9.200259,6.572492,2.279365,-8.538530,-2.807886,-2.640147,-6.832474,-3.631404,1.570557,0.292676,-3.578355,1.506228,1.225166,-0.587663,1.134846,-8.716744,-1.836043,3.736277,0.463129,3.610234,-2.845802,-4.854136,3.409487,-8.126892,6.451910,-0.140154,7.254536,-6.009110,9.583294,-5.273173,-5.062015,-5.504899,-5.083241,-0.113819,2.485483,0.774941,7.359787,-5.016262,-1.042410,1.549511,3.023099,9.940178,4.280722,6.797772,-4.749042,8.883112,-1.587594,-5.743952,6.962365,-8.659237,-4.680522,-3.840263,5.039867,-9.920627,-0.952789,-5.966222,0.938349,-6.741524,6.633049,7.988092,2.394846,6.063082,-2.857251,-2.950658,-0.153536,-0.677722,-9.325511,5.821231,-4.426064,6.390826,4.013158,-8.375136,4.871276,-0.338262,-4.938082,-4.755650,-9.151137,-4.444306,9.878149,4.319353,0.027425,-7.805451,-6.833187,-3.043012,3.467353,9.853682,1.448010,-1.466892,-1.108221,1.684232,-4.020594,-1.562559,6.270908,-8.453384,3.405484,7.919202,1.613482,-0.400997,3.818345,-2.743921,-0.806045,0.363399,9.971375,-0.466508,-6.447311,4.715411,-7.925383,-6.378432,-3.556018,-0.221136,-6.709865,-7.412827,-2.851180,7.725614,9.070642,-0.450943,-8.526541,2.093046,9.494738,2.329445,-6.689052,8.780163,8.193814,-7.048468,-0.292807,0.042839,-6.095172,-5.571884,2.873178,-5.045598,-0.819647,-7.147293,3.007838,-5.856856,-8.957364,-6.062022,-7.014349,6.091698,6.136261,4.118609,-8.355260,-4.091364,4.036881,4.103675,8.343753,5.819486,0.990266,-1.471469,-4.024624,4.455654,-5.431947,0.338646,3.441525,-0.488891,-8.364583,-1.081708,4.728755,-1.947879,-6.504092,3.257431,5.941489,4.608278,-7.803083,5.004185,-7.252910,1.446532,8.396242,-4.756831,4.312654,7.001108,-6.274853,9.692457,0.773798,-5.079238,0.872471,9.680494,0.671443,3.488075,-7.195080,-9.758042,-5.307885,3.924297,-7.652301,-8.778807,2.568173,4.892549,-2.860532,2.622459,-0.815514,9.964715,0.570683,4.022472,9.213369,-0.959877,1.960588,-8.798989,1.396080,9.198483,1.247071,4.567427,-6.350083,2.491151,6.798370,-7.250939,-9.785643,-6.512126,-9.823159,-1.515993,-8.902898,2.773189,3.587055,3.676116,8.462527,-4.970724,8.873428,2.322754,1.339691,-0.803902,7.519203,-4.839814,-1.239709,7.069408,-2.064035,-0.005889,0.173398,0.342725,8.683093,4.820511,8.525814,-9.712951,3.158049,-5.533615,-4.456058,-5.139631,3.038330,5.935711,4.664831,-6.395340,2.917936,-7.371849,-8.503096,0.302067,9.222259,3.901253,9.802759,5.031322,4.914757,5.127308,-7.489808,-9.437719,-0.059872,0.556863,-2.726556,-4.355999,-7.338732,-5.984036,-9.027447,-6.725785,-5.583349,-6.517505,1.223160,1.764458,-4.860599,-0.591914,-9.787203,-5.504806,7.897210,-6.319978,-5.235710,5.200227,0.615154,0.515250,8.397205,9.386138,2.666474,8.790242,9.149378,-7.486964,3.347125,-4.039672,0.310644,0.946051,-7.033358,-4.257750,-3.169643,5.826696,-3.975952,0.182273,5.394363,5.855919,-3.846784,9.411598,0.923748,0.370103,2.966165,-6.886358,9.646262,5.017704,5.546229,-1.795797,4.373155,-7.971684,-2.882976,0.766179,-9.987538,2.660751,-5.488517,9.889904,-0.207819,-5.042727,-2.646621,-1.899521,-2.328144,-5.052592,5.918886,0.551393,-4.667632,-8.216767,5.185073,-7.767798,1.954027,1.576706,8.004090,3.230879,4.211371,1.230912,5.426554,4.454439,0.941001,2.595136,-7.096510,4.220967,-0.751564,-7.504063,9.111067,-8.318165,-9.683731,-2.710733,-4.221527,6.053829,-9.473758,9.829435,-9.593450,3.965394,-3.238911,-5.996506,-7.252228,-3.959969,-7.685969,-5.847468,1.909561,-1.919970,-6.364416,1.844168,-5.829633,8.194611,4.502934,-9.755002,8.338439,6.128149,4.945926,9.151048,8.969643,-6.562381,-8.377938,-6.757232,5.609932,3.956399,5.107368,-5.700246,3.945620,-8.850227,1.495105,-8.231862,7.162339,-6.687066,8.928724,-9.580601,9.545953,-5.970573,8.756722,-0.412199,2.636679,4.780532,-0.950436,0.961300,5.458719,1.402010,-6.554099,2.075085,1.901836,-0.286172,6.447403,-6.323733,-7.937099,-2.162864,2.044484,-1.186349,-3.987773,1.394419,-1.278585,-7.486102,3.404078,-4.689330,7.346138,1.906665,4.521807,-6.711585,-2.825006,-9.852115,6.845590,-8.385287,7.862950,-4.471892,-7.442371,-7.857242,-0.391361,-9.048009,-3.052969,5.073545,4.840082,6.348429,8.557637,3.411735,-7.775678,-3.337426,8.662139,-0.682532,8.539250,-7.549817,-8.454107,-9.162174,-9.392295,-0.580374,0.995830,-2.524780,-6.991471,-6.188879,9.917173,8.749147,9.761396,-4.149060,0.012842,3.827454,0.998908,-0.225802,-1.096942,-2.023376,-7.123870,-3.411006,-1.450850,-2.550803,-0.676320,-6.959893,-1.744186,5.025495,8.280018,-7.638432,-7.295808,-5.679083,-7.128244,2.589420,5.374645,4.491506,9.099987,-1.561922,-0.956249,-3.318476,9.972102,3.488161,5.609190,3.215322,-2.402357,9.261306,6.554464,-5.138627,-5.936401,-6.651459,4.005635,7.783487,0.493311,-9.124695,-0.489882,-8.206945,-8.651463,-4.267695,-7.935486,-7.701020,2.728411,6.936050,0.036170,-6.150667,-9.813867,-0.313190,-9.269171,-4.291638,0.017672,-4.780682,1.112274,9.779251,-8.658793,6.402775,3.932425,3.211952,8.650291,0.010575,-8.772507,0.655425,-6.398533,-3.103954,7.142919,2.621175,4.465455,7.645425,-5.270982,-6.948433,-3.421477,-6.540390,-7.566162,-2.537210,-7.387275,-4.534048,-4.013230,3.839660,9.801695,3.319231,-8.262228,4.074148,-0.138900,7.257580,3.713718,8.141795,0.640793,4.485288,8.408693,-7.787139,9.591461,-4.458769,-4.675010,1.034283,9.277096,-8.624745,9.507617,-7.342356,-0.363567,-9.824091,8.938410,4.070916,1.082143,-5.801418,1.923692,6.943033,-6.700745,-5.741700,0.086525,-3.829888,-2.227292,3.520317,0.668744,-4.903604,4.964792,0.158347,-8.663762,4.866886,-6.903802,9.612415,-4.914246,-0.468950,-3.266714,9.280961,-4.090612,4.291552,8.006928,-6.936309,-3.497306,-6.289670,-2.302591,-0.863069,9.016401,-0.967036,-8.121949,9.780683,-8.079943,7.484517,-1.493141,9.971418,-0.568398,8.150967,5.799725,-9.454491,-0.703976,9.469142,4.404673,-2.129938,5.017407,-5.339290,-5.627489,1.291834,8.360845,3.456471,4.052850,8.630750,0.360459,2.807307,-2.537174,-2.671233,6.531287,3.368367,-2.108412,5.921071,2.307539,3.753377,6.501226,-4.829085,6.849157,-9.164144,-2.826890,-0.033044,-9.438397,-2.506369,-9.134749,-9.142193,-1.930214,-8.388400,3.022789,0.163187,9.642322,-1.973874,9.675805,2.482390,-6.032324,5.754840,8.920444,8.581896,-2.916933,1.328901,-4.928206,-9.475501,8.548385,0.709743,-6.258498,4.724457,9.108219,-3.174417,9.201779,0.977233,6.346034,-8.604755,4.624721,-4.550540,-3.766672,-1.015668,7.225153,2.555746,5.672741,1.901757,7.516964,4.300377,-3.030537,7.030411,8.855452,-7.505054,-7.928462,-7.337326,-7.460748,4.765000,-3.943580,8.717166,-0.650200,-3.797011,-0.770312,8.941641,4.908497,-0.566696,-7.192615,8.685826,0.145171,-2.950069,-8.543824,3.359882,0.134128,9.219707,-0.802615,-6.919254,-2.928929,-3.088448,-5.988540,-9.311856,-7.676190,-2.173940,0.708671,-2.463191,8.334293,-6.663618,0.365303,-8.910828,-4.505607,-6.441684,-5.143943,7.776707,-8.576941,6.305808,4.276586,-8.256339,4.605523,-3.767690,-6.008943,9.944628,1.264178,9.515993,3.318916,4.403122,-1.694488,-8.867390,-8.968721,7.886761,0.560739,-2.383246,-2.197767,-1.108151,4.100525,-4.904344,6.314291,7.191988,7.684749,-6.741698,-5.568779,-0.272047,6.183932,4.325390,-8.549737,-5.940214,-9.997175,-6.792515,9.115941,-5.946108,0.539729,-3.671694,-1.554710,4.057156,8.044784,-2.191288,-1.314279,-1.957835,2.784914,3.496351,-5.636776,1.316016,-8.127221,9.806225,-0.926309,-6.949311,7.225859,-2.605898,-2.569123,1.452531,7.099459,8.483899,4.142657,-3.881478,-5.814833,-3.271436,8.282091,1.547761,-4.442462,-8.602709,-9.979153,-1.836522,2.337962,5.547628,5.241028,6.517946,-8.093709,-4.244819,-8.788133,-2.966844,-8.202794,7.494780], dtype = "float64")#candidate|9545|(2400,)|const|float64
call_9544 = func_7050_call(relay.reshape(const_9545.astype('float64'), [15, 10, 16]))
call_9546 = func_7050_call(relay.reshape(const_9545.astype('float64'), [15, 10, 16]))
uop_9555 = relay.rsqrt(const_9532.astype('float32')) # shape=(15, 16, 16)
func_9252_call = mod.get_global_var('func_9252')
func_9253_call = mutated_mod.get_global_var('func_9253')
call_9565 = relay.TupleGetItem(func_9252_call(), 0)
call_9566 = relay.TupleGetItem(func_9253_call(), 0)
func_7901_call = mod.get_global_var('func_7901')
func_7903_call = mutated_mod.get_global_var('func_7903')
const_9579 = relay.const([-6.911888,-0.542153,7.471039,-2.916088,-3.050858,-7.805555,-0.867914,-1.184660,1.256006,-7.248519,3.538208,-0.853931,9.617564,-9.846728,9.110866,-1.631110,-9.870261,-5.211863,-6.053610,1.701480,4.142931,2.360152,5.281504,5.640838,-3.541534,6.071399,0.924875,-8.213732,-8.907944,4.893083,-6.821292,-6.103025,-1.725548,7.528531,4.212022,-3.416591,-6.687743,-4.379307,5.549322,5.203409,-4.160476,-0.648015,-3.629350,-4.866410,1.240651,-3.295070,-8.718165,7.424954,8.593934,5.487543,5.928961,8.815987,8.590458,2.770978,-0.710194,1.852318,2.975799,-6.275406,-5.011307,2.763946,-9.557663,2.265939,-5.053806,-1.068481,7.519153,-0.449383,3.893856,2.096625,1.388838,1.475279,2.763203,-0.609746,-1.543903,-0.069728,-7.455655,6.999749,1.238310,9.332571,4.719701,-0.438715,5.802183,0.802811,-0.656423,6.988290,-5.838717,4.733072,2.996551,-4.864880,-1.372915,-2.575466,-2.673456,-4.819735,6.976499,5.690827,4.788483,5.006357,-4.750111,3.386461,5.406245,9.980028,2.805540,3.338758,-2.734344,6.929781,-9.169308,0.140180,7.692842,6.693796,5.538611,5.400043,-7.695430,5.525026,7.325557,4.932177,-8.746446,-3.659082,-6.429617,-0.903088,-3.260044,0.372081,-1.153418,5.105881,-7.186559,-2.150334,-0.440707,-0.692681,-6.690098,7.784168,-2.051879,0.794725,1.944641,5.666644,9.340487,3.023166,6.946247,6.811769,6.701317,3.645343,4.999449,-0.235274,2.537999,-3.906398,-6.170078,2.047635,-7.749488,2.442683,8.703489,8.591054,6.080041,-5.960004,-0.563384,-4.498136,-8.674108,2.399879,4.963441,6.584110,5.622838,-9.510229,-0.266730,-4.430300,-6.929617,-6.545225,-9.385796,9.545057,-0.033373,-8.609938,0.062696,8.604248,-5.115407,0.779026,-0.009929,-4.150871,-5.648872,0.418527,1.614159,3.476475,-5.538228,3.541624,-3.420140,-2.622618,-4.472454,4.366178,7.900344,1.774058,3.423015,5.895599,-1.331642,2.109961,-2.864923,7.565803,4.334772,-6.353328,-3.812073,-3.706506,-4.006815,-4.652724,-6.301284,-6.592051,-5.594704,4.780746,-9.543752,3.131565,6.345520,1.274282,5.298065,9.915064,1.336344,-4.471746,4.439711,-5.485535,6.682626,-1.365227,-2.792332,5.378184,-5.019089,0.505862,5.050179,4.744750,9.872255,1.912184,1.905102,0.587139,-0.345744,1.658696,8.186530,4.294927,-3.352061,-6.095442,-2.777550,8.682900,-4.264596,9.717714,0.567395,-9.516042,2.011721,6.817480,-1.269560,6.456403,5.692415,-0.279264,1.248880,2.746662,7.235596,-5.138111,-4.768333,9.902838,-6.182587,-5.829612,7.587113,5.814800,-4.938268,-8.293635,3.595051,0.627119,-7.724781,9.497841,4.262548,5.736060,-3.065677,-6.784582,2.844582,-0.557683,-0.021619,3.574813,6.415120,-0.009335,3.497015,7.750533,4.168418,2.438983,-8.150832,8.963722,-1.324228,2.671340,-8.248521,3.828562,4.206843,-0.979559,-7.787062,7.004677,-4.318448,-4.192369,-0.310506,-6.605678,-2.402357,7.747681,0.263519,2.594196,3.851974,-7.833796,-5.388955,7.700117,4.274621,-9.432456,5.309937,-2.162429,5.411216,-1.010946,-5.639859,9.493760,-0.251971,1.340950,7.601473,0.633338,3.662060,3.348746,5.529703,4.363262,-0.621115,5.266965,-2.159000,6.662824,-8.050235,1.054491,-2.714077,2.440166,-1.638157,-5.949317,0.630282,-6.819056,-9.410473,0.519403,2.737616,-2.114466,-8.440249,8.689781,7.555412,-8.774603,-7.838889,-0.005400,9.450553,-2.633280,9.043366,7.822334,-5.092618,9.766455,6.037797,5.787972,-1.283962,-1.103568,6.920080,1.876395,-6.772686,-9.071657,7.976577,-8.730514,-8.917517,-2.785142,8.938569,3.272829,-5.396190,-0.882141,7.024099,-1.679963,-2.995027,-7.271305,-9.307392,-3.478060,8.054007,-5.402879,-3.813156,0.924051,1.458588,-4.824895,-8.322441,-0.732028,-6.424143,-6.343545,-0.143831,1.470055,-4.254156,-5.441510,0.965594,3.402620,5.430352,-4.963051,-5.506315,7.013740,2.485437,4.978591,9.326065,-1.743573,-4.464532,2.261280,6.134663,7.021326,-6.449389,2.676775,0.205717,-5.224355,-0.308820,-6.985700,0.974271,-6.213050,0.343837,-8.711442,0.727876,-9.406461,7.405340,9.196468,2.114860,-7.305014,-8.165628,0.177856,1.400108,1.902213,-8.202682,-1.207693,4.682138,0.427350,-1.536367,3.613705,-9.987821,-2.751373,0.671903,6.108019,-0.030287,-3.008076,4.569632,-4.276984,6.803925,-6.458804,3.703496,8.403876,3.863344,3.524087,-1.405995,3.611150,3.857442,7.386478,5.716608,5.912302,-2.414146,1.245663,2.200193,-6.124540,3.205813,2.513029,-6.572188,4.922297,5.837850,8.442000,9.728474,-0.073546,-0.082190,6.897689,-5.249668,-2.739668,-5.495206,-3.151260,7.984690,-1.151719,6.013960,-4.571735,6.710783,9.810489,-1.104448,-5.209644,-2.715811,-7.556731,-7.684771,-9.047355,-1.882053,-7.265201,-2.204235,8.116104,1.103731,-4.790759,0.064393,-7.202682,-0.844719,4.610307,7.100009,-8.297122,-6.031946,-1.985387,-0.519472,-1.060613,7.104203,9.942365,6.962559,-0.081086,5.950263,-7.518281,8.776338,2.674917,-1.272030,-1.636532,-5.587101,3.254194,-3.098367,-9.403411,7.770711,3.462278,6.104314,-3.797687,5.012317,7.980227,-3.508180,2.526852,7.360499,3.233502,6.718952,9.830575,8.002200,0.503604,-5.294911,-2.681414,-6.730434,8.216343,6.284957,-6.713405,-1.240663,1.029762,4.511727,-8.759646,4.102727,6.606218,6.034314,-9.462315,1.895469,-9.076474,3.969165,6.033701,8.643033,9.396664,2.219911,2.709473,-3.873931,-7.844936,-7.596598,-2.636817,-9.912183,-1.415272,-3.013980,-9.498970,-4.237011,2.608669,-9.821565,6.524693,1.675768,-5.394184,7.352475,-9.711402,-6.999167,6.881121,5.500025,-7.569167,2.012472,-8.561759,8.634783,-8.570000,5.585892,-6.965631,-2.835546,5.876871,-4.177459,-6.707696,-4.977451,3.078814,8.818315,8.013400,-7.335012,8.707290,-9.936909,2.306917,-7.427823,-5.831823,-4.044093,0.537348,-0.462426,-7.139312,-4.123175,-2.783973,-1.874330,8.627957,3.554887,-4.182418,-4.931015,6.061219,9.324620,9.466729,-9.098449,-1.378911,-2.741279,-2.261075,-8.500148,9.335245,0.932896,1.611896,-8.122490,-3.782426,2.995873,7.304286,-3.166478,8.777422,-7.037764,0.962094,-4.916278,0.921470,-6.896954,3.126815,-6.255067,5.969129,6.042165,3.778547,-1.702263,6.297153,6.487456,8.688979,2.825353,3.271739,4.866596,1.160946,-3.134707,-4.082492,-2.536591,-4.571566,1.049661,-6.619100,-6.200381,-7.168874,0.626660,8.471693,-9.470123,-3.494828,6.712678,4.431058,2.043978,-2.377468,4.048143,-4.919886,-3.295810,6.822392,-0.701459,-0.188436,9.367408,4.766864,-9.660381,2.230270,-7.590379,5.991123,-8.231234,-9.105978,1.786516,4.952620,-3.943718,-8.833421,-5.412691,-5.648061,0.553327,-1.033912,4.016866,-6.347340,-0.104934,-7.439288,0.377570,-2.105209,9.206528,9.425206,2.810626,3.060189,-3.897524,-3.977456,6.439121,-3.432954,-6.690924,-8.111740,-3.220738,9.301379,-7.736677,6.437460,0.540801,2.700149,4.705810,2.364658,-5.247570,-6.476049,-2.294898,3.838220,5.448879,3.679216,-5.145022,3.220924,-6.474818,3.513426,-8.198473,-9.726617,-3.693710,-1.002606,5.557924,-8.104483,3.008722,-7.385304,-4.302368,0.232664,5.149058,5.618553,-9.926571,9.266692,3.977173,-3.334774,4.177244,-1.624362,-4.340748,0.303017,-6.005476,1.012529,-1.783574,-0.219871,-7.273299,-7.380240,-4.968151,3.060995,-0.896091,7.970934,-4.080287,-2.582662,-3.406533,4.225640,7.628627,-2.223313,9.461781,3.596262,-8.546428,-5.883841,-9.661011,-8.577099,-1.345774,8.032677,-7.781436,-4.263625,-3.314518,2.524084,4.381149,-5.565626,5.023262,2.441717,-2.688925,8.730302,-0.261735,0.178394,-1.082845,7.357990,-2.384857,-5.727401,7.843174,5.726084,3.986719,-1.165711,8.843390,9.219358,-9.650195,0.413602,-6.028226,5.390895,-8.509561,4.221563,-2.868111,0.108880,0.385327,-2.619096,7.688287,9.647771,-4.455131,4.416591,-1.706621,-2.669968,1.040576,2.622108,-6.735760,-8.057480,-4.958265,-5.667634,-3.543902,8.985556,9.308357,-8.242203,2.208352,8.846527,-1.077651,4.648009,4.521260,9.019313,-6.650306,-8.418333,3.686752,7.975848,-9.984241,-7.483733,-3.297826,3.612387,1.129439,-2.134039,8.484122,-6.747281,-1.095846,-1.293754,-9.449688,1.774119,-0.835515,4.953562,-9.927743,4.383387,-1.542648,-1.159085,3.031857,-0.648536,3.963543,5.354508,-4.932059,-5.353508,-9.313121,1.532277,-2.904317,2.053705,-9.123209,-5.796697,2.879942,-3.545303,-4.512624,-7.088448,-0.384669,-2.675705,4.106584,-5.907966,-4.957947,6.073057,0.973241,6.453285,9.048824,-9.313795,5.298403,-0.949543,1.921778,7.786872,5.698187,1.887030,-6.551964,-3.711414,-6.275758,-4.945175,1.284103,5.533848,-1.974225,6.864817,7.802684,0.337273,-5.943915,1.910448,-2.541381,7.520053,8.423899,7.889911,3.924533,3.996604,-1.113640,-4.009453,6.130031,-6.599518,-8.588376,5.430877,-0.763269,-5.613647,3.123760,-2.598584,-2.040463,1.580706,-4.293219,-6.454256,-7.917352,7.075254,5.651998,7.037893,5.460690,-6.509824,9.035299,6.457563,-7.794682,-9.046532,-7.655906,-1.335461,6.304017,-9.969660,-0.467354,3.047328,-8.772670,-1.922129,-4.386314,5.026332,8.770976,8.426000,3.932984,-3.619825,-1.831728,2.719772,9.464686,-4.528052,-4.370916,3.904433,9.066576,8.368077,7.529276,4.971121,3.519970,-6.566413,-2.119107,6.897642,-6.654183,9.322359,0.738826,1.039998,-9.722422,3.379632,-2.768651,-1.798126,3.860540,-0.166474,2.253103,-9.501732,-3.799746,9.563536,-3.230276,-0.452928,7.758466,8.624484,9.009116,8.512775,-2.895368,-2.114635,9.499063,-1.368242,-1.215639,-4.016354,-2.280177,8.533206,8.948757,3.996837,8.971616,-8.787440,-1.302863,5.084104,2.287496,1.827600,8.502036,-4.925332,-0.972166,7.250529,8.716443,-3.623053,-5.244689,-9.748785,9.858947,2.604392,-0.934157,9.452487,-8.798003,-8.672902,9.014945,8.368601,1.278111,-5.369417,9.812828,-7.586154,4.676468,-4.734459,-2.869837,9.017345,7.636833,4.643280,-8.119741,-7.308511,6.076982,-6.661839,-4.664659,-0.147873,-2.530094,-6.381477,-4.761021,-4.815970,1.361503,-9.692600,-5.911406,0.879388,-2.206986,5.500112,7.465855,4.333729,-1.673507,-0.561412,-7.300005,-5.617852,5.634314,-5.033186,9.946285,4.452367,2.317599,9.292626,8.290909,2.916948,2.074436,-6.474485,-6.832366,4.339254,-4.120662,-8.481352,-5.843670,8.044086,9.621151,-0.624715,-7.401024,2.332758,8.847071,4.810391,-2.368075,-1.815377,5.870275,-2.181711,7.052275,-3.351057,5.620631,-0.107605,4.663754,6.959835,0.068534,-6.140262,1.745030,2.486193,-5.572259,5.234972,-3.529170,-1.842515,9.603503,7.599501,-6.884977,-1.424595,-9.278176,-0.338617,-9.371631,-3.615541,2.751751,2.272215,1.661368,1.932261,-2.556731,-0.425737,-6.688715,-5.781106,4.529643,-1.679788,-3.047346,-4.046352,9.241842,-1.107107,-8.928142,7.655008,9.349593,8.592895,-8.141604,-9.239773,5.654016,3.977968,9.874337,0.876685,5.493545,8.713752,-1.023123,9.578373,-5.144688,3.003389,-0.467234,-9.082346,-4.280799,-5.375146,-9.504947,2.348382,0.154836,2.992490,-0.321910,-6.944888,4.463714,9.689045,6.150289,6.542943,5.012058,-8.386013,-4.913238,2.737590,-5.538059,0.480620,5.878229,2.419873,5.079981,5.240281,4.275661,6.623019,2.501304,4.190486,5.504471,-0.855542,0.439032,3.153018,6.494628,-4.967384,-2.913466,-5.678829,-2.988769,0.295655,4.706151,-9.677013,-7.906942,2.131111,-3.844105,-7.030925,7.239616,-7.421554,6.797140,-0.559996,9.750301,1.636335,-5.236474,9.961964,2.044345,-2.748062,5.970106,8.575149,7.886651,-2.100669,0.863927,0.680592,4.539998,-0.344491,3.885821,-2.015384,3.373833,5.032548,3.919633,4.586509,6.869121,6.369840,-1.704439,-2.139135,5.354602,1.669697,3.607899,-0.530614,6.210678,2.682397,3.788066,6.521753,3.353598,9.553702,3.758585,3.324559,-0.804571,0.744349,-1.409509,-4.921801,-1.940844,-4.744323,1.596375,4.948404,1.662058,2.696425,-6.691331,-4.068725,3.558648,-3.694856,-4.611102,0.668273,1.125774,0.288683,-8.586700,0.120904,9.511602,-1.291890,-3.106289,2.348311,7.444490,2.822511,9.561073,3.462963,1.472817,6.818401,-7.193729,-6.644256,-6.977390,7.462494,-6.915766,4.308523,-5.482047,-8.824809,3.004222,5.232700,-6.569123,-2.900678,-5.564337,3.380029,-7.899018,3.262197,6.962999,-8.225242,0.038344,2.051171,-7.584792,4.708533,-0.670737,-9.384395,-4.488016,-8.229745,-5.622111,-3.182881,5.400965,-6.581051,4.508084,-4.711007,6.793479,-3.394297,-3.817859,-2.655751,-0.351846,0.331034,6.883989,0.849760,0.982650,7.014699,-2.729621,-9.695238,7.821524,5.932511,-1.780140,1.523079,-1.305374,-2.032388,9.730631,-3.986020,3.638855,4.658378,3.743312,-5.504118,-0.963013,-0.659902,8.275710,-0.031831,3.912671,9.223163,9.866130,5.827178,-2.062382,-5.006162,7.627251,-0.505576,0.026114,1.423875,-4.668046,4.581609,4.074133,9.152706,7.172288,5.237131,-6.628037,-3.440701,-8.889049,8.912055,-4.459297,-5.833703,-1.427562,-4.925634,-6.997071,-4.097242,3.424232,-1.984843,5.973887,5.656214,7.068266,9.546894,-1.333102,-5.507262,-1.998724,4.167876,5.273088,-0.302183,-4.001626,4.407198,-2.868951,6.808509,-8.210437,7.622752,-0.714734,-3.250319,1.803503,6.647724,6.331844,-3.845487,6.127994,-2.305630,-6.121358,7.283662,6.349448,8.836754,-7.250579,1.474074,-6.480131,9.823648,-8.849276,2.014805,1.803385,7.626378,-5.264989,-6.844592,8.215332,-9.474682,6.519123,5.107854,8.629934,8.825797,1.596615,-4.779275,2.223359,-9.386322,4.783642,7.798385,-3.887693,5.213811,2.063620,9.656509,2.451680,-2.096307,6.781277,4.285791,-4.365321,-8.782549,-1.795011,-1.991294,-4.543380,3.075588,-8.315273,6.342070,7.921424,7.335774,-4.651927,5.268805,-8.656936,8.478572,9.485161,-2.111563,5.365161,-7.529823,2.932409,8.829477,0.333168,7.464423,5.851005,5.092702,-2.604755,6.696822,7.163541,-5.574147,-7.799976,0.300917,-1.814918,-4.851217,-0.842945,5.970319,6.356799,-6.533967,5.892348,-2.494762,-8.867147,8.811528,-2.022860,4.650240,-2.149514,2.985341,2.129195,-6.196791,3.359795,2.907338,4.260569,0.418986,1.930945,-7.959752,-5.467420,-9.897741,-7.423075,9.217315,-1.127766,-7.468227,-6.258851,-9.769420,-9.284363,1.531741,3.406211,5.472357,-6.190631,5.789280,-2.846532,-1.665902,-5.445679,7.203837,9.658666,2.670248,-3.976053,-3.813220,4.842612,-6.103095,8.015030,2.121042,8.124534,-0.265381,-1.405742,3.452911,0.530518,5.041201,-8.003740,-6.601542,9.891297,-9.641166,2.588965,-6.628723,2.112177,-2.562324,-7.209463,9.273539,-6.114854,9.816649,0.681959,-7.266816,3.773884,-3.606635,-6.581135,5.287763,-8.771839,8.258877,-8.875068,-0.809353,0.539945,-8.726963,1.128888,4.707372,7.093375,-8.234955,5.397649,6.211061,-3.953337,6.911893,-2.898944,-5.599346,-0.500779,-0.348407,8.513410,-5.768724,3.445639,-6.685691,-5.583742,7.750774,0.479206,-8.781838,-4.833278,5.057554,0.431643,0.154174,8.567839,-8.863428,-0.605823,-8.627756,6.284640,-3.887644,5.228566,9.370162,-1.910278,-2.910727,-6.857215,-1.972476,-3.760821,0.354990,-9.346390,-4.696812,-0.099738,0.760676,6.504312,-0.090813,-1.970174,-7.498358,-9.165203,5.904822,-6.086840,-7.187350,-1.143976,6.807591,-6.786941,-6.883756,8.145838,-4.928663,8.535787,-9.344371,2.084020,-3.542053,5.926841,0.166415,-4.262329,-6.905558,-1.966951,-1.937092,-7.541333,-8.988819,-2.102006,3.859651,1.123616,-3.961090,-3.953245,6.115527,4.667168,9.581371,-7.086604,-4.448708,-6.754422,2.122434,7.465922,6.640806,1.891834,-0.645927,2.959167,-7.456404,3.352085,0.180590,7.133528,5.977878,-3.771517,-5.649964,-5.111390,-3.806000,7.393323,8.630486,3.329747,-5.685645,-7.750443,-3.649905,5.053019,-6.423816,6.301207,-3.998419,2.688350,-1.602085,-0.842229,-8.804514,1.420942,5.505699,7.586206,-7.575955,-6.081632,3.510256,8.244577,-7.268650,-9.014565,-1.433884,-9.207999,1.577629,-7.247371,-7.608715,-3.886442,5.810533,1.175326,-4.420218,-7.226959,2.795626,-6.503511,5.953632,-9.443310,-9.519493,1.322141,6.924325,0.862671,2.781183,-0.680101,-9.241047,-8.282984,-3.708698,2.159051,-0.153405,6.725966,-8.502857,1.063361,-1.148949,1.866280,-0.899072,0.490871,-8.462831,-7.207423,-1.016274,0.071840,5.844067,5.221827,9.197211,1.070892,-9.667588,8.376766,-5.900383,-5.933797,7.356935,5.862914,-8.556288,4.746341,5.725507,-5.537538,-3.045171,-7.874132,-8.751779,1.541335,-8.102925,3.875513,-4.038033,1.462093,0.461528,4.723302,0.461922,0.279061,8.650714,6.110573,-8.443134,-1.930763,8.741606,7.210011,-1.916908,-9.890028,6.032367,8.036499,-9.458328,-0.014488,3.477336,-3.480665,-3.095596,-3.842272,-5.384871,-3.525855,-0.005683,0.251612,2.426550,8.637961,-4.835533,1.356378,4.428338,7.362882,9.993652,-7.662060,2.138636,-9.522785,-6.127225,1.311284,-0.970594,9.779923,-5.664681,-5.051790,1.955734,-1.776238,6.763258,4.607751,-0.387250,3.543500,-7.673934,-6.399118,-9.222740,2.590224,-5.515399,-0.165395,-3.924797,5.156336,-6.553605,7.149029,9.521389,3.632213,7.721295,1.737074,1.264394,2.708029,-2.983845,9.042992,-4.683102,8.557499,6.851893,4.189835,-4.282058,1.791561,5.582059,-5.633555,-4.879520,6.776150,8.331438,9.429114,9.087656,-6.238237,2.811950,3.184073,5.304594,-2.160390,-4.783044,-1.974144,-4.882676,6.323590,-7.773171,-5.177293,-5.878968,-2.961209,-4.220062,-3.036701,0.952196,-5.628430,1.649849,-4.846627,-8.079612,4.883297,3.585782,9.967935,6.490076,2.104599,0.076694,-9.415846,9.576825,8.790008,7.610737,-2.091157,-5.374048,4.404628,-0.177284,-2.729035,-8.875477,6.323928,-6.281082,0.491728,2.187117,9.797777,-5.912055,-4.159061,3.220761,7.028286,-2.361592,2.983160,-9.326671,-8.104858,-7.370135,-0.042619,-2.819205,-9.965733,-2.749976,4.574961,-4.097089,-1.061863,-7.257854,4.847981,-5.756708,-3.118882,-6.141922,-8.080762,-2.961108,7.166091,5.260014,6.744615,1.724097,-5.141226,2.297732,1.745367,6.648456,-6.916788,5.182297,8.791745,0.265777,-5.695403,3.702130,-2.575676,2.325923,-0.571935,8.639386,-0.492791,-2.694529,3.304072,-7.686040,9.863149,-2.456213,-9.925738,3.568426,-4.772909,1.548894,-2.429480,1.935171,8.918801,-2.995278,9.616020,8.944065,-5.165086,6.345565,-8.289279,2.474688,0.817486,2.242366,8.137073,5.971959,0.680305,-5.549430,2.160866,2.833051,-8.752703,-5.158891,6.615869,2.816350,8.368408,9.688974,1.568004,-9.967287,7.916727,-2.409866,-9.032596,-1.376830,-2.857620,-7.831418,-2.099359,-8.860142,2.119181,-8.075422,8.361296,0.430308,-1.487698,-8.319415,1.696027,-5.255158,-9.569627,5.515072,-6.358792,4.914933,-5.159421,-2.129070,3.894642,1.491968,-9.866641,8.173912,7.638877,-8.525525,-7.401545,1.065074,3.585258,-8.581217,-5.435287,2.659179,9.907204,-1.283065,-0.510920,-3.045006,5.144253,-7.896102,2.063451,6.879927,-7.677398,9.176146,-0.222392,-7.272758,-4.960298,-9.030218,-7.614023,-2.204053,-7.693174,4.331281,0.381225,-6.290497,8.801461,-3.607189,-9.860450,-9.697109,-3.021356,1.957291,-4.237275,-0.081425,-2.074455,-8.394335,-9.412268,-2.370323,3.490983,2.794858,4.051039,1.618579,4.080317,-7.282648,-3.607925,-8.608662,-7.152304,0.678333,-6.098261,3.798785,-0.841876,0.235124,-7.071959,2.611026,-4.370391,1.746311,-4.934671,-3.977318,-5.700464,-4.672162,3.270254,3.678910,-7.551500,9.805612,4.658605,-4.085540,-4.012659,-2.487934,3.548385,-0.172607,6.807497,-1.553907,-3.598154,4.116538,2.962670,9.126582,-4.445439,-0.074865,-3.827313,0.635984,-0.148106,9.534008,-3.893605,-5.391412,-4.986686,6.575607,-6.626024,2.143756,-0.140614,4.528092,-4.938922,8.486378,-7.039041,-7.320638,1.064134,-5.112716,6.048965,-4.981400,7.767847,1.569847,6.297889,2.073164,-6.393994,-5.952120,0.546073,-2.724341,3.444966,0.963255,9.539591,-3.446015,7.656148,0.283229,-9.149738,-3.614612,-5.959061,8.565220,-5.771989,8.573395,-8.976408,-9.291320,4.717850,1.428656,-6.652390,-3.550788,-6.133137,-2.131482,6.779960,-6.529473,7.935738,-4.023479,9.624952,1.764012,-3.218523,-5.240705,-3.090748,7.255689,-0.309619,-5.402146,7.580448,-0.919600,0.792061,9.888382,-0.832689,2.784372,1.850117,9.280770,3.820659,-5.418668,5.442371,-9.064981,5.460262,-9.803642,3.144744,-2.189487,9.219192,-7.139075,8.444010,-6.798621,-4.029913,9.220545,8.617469,-8.970616,3.044214,-4.046233,3.486080,1.175801,-8.205920,-5.480614,-8.793140,-7.715208,-9.729806,5.449697,9.171902,7.276956,8.384543,7.141171,-1.694265,9.482716,-8.807095,-9.748907,3.733715,2.913540,7.674922,2.453454,-5.921921,-2.260819,-9.128110,7.857969,0.346296,6.353118,3.514567,9.966170,-5.103800,-4.235763,-7.766034,3.658088,-2.963824,-7.082569,-3.212094,7.855573,1.982668,1.031255,7.661545,7.908278,-4.377805,7.892264,4.257508,0.013790,-2.022015,1.372812,-4.467156,-7.554319,9.369539,8.533983,-3.208992,-4.074619,-9.908896,2.386458,-8.890477,-8.582248,-6.274030,5.198475,-9.598116,3.525408,-8.382064,2.983892,4.265062,8.269958,-6.735634,3.106790,3.255147,7.311408,6.641416,-2.003896,0.341888,-1.426186,-4.518313,-4.873129,-1.331630,3.303910,-4.391835,-5.097830,-2.544268,-3.887995,-8.762120,1.841316,5.516999,0.440400,-6.282267,9.635615,-7.765517,8.031720,9.962833,7.304354,6.570785,-5.548578,8.335385,-9.674017,-0.749852,9.345128,-0.824808,-7.391221,3.999311,-6.564750,9.369426,0.174706,-4.491102,8.927604,-5.974063,6.848959,6.631574,5.955701,-9.398699,3.367417,-0.485670,9.509149,1.862895,9.576771,7.018595,-2.992056,6.060574,-4.643249,-3.614213,3.778388,-2.842384,8.418188,-2.828672,7.997536,-2.617431,3.467416,4.874996,8.012778,-0.012302,5.601605,-9.705873,8.719351,0.115251,2.469085,0.927253,7.456808,-5.565100,2.931662,6.122093,0.207907,1.417179,0.675242,-9.829237,-5.198908,0.546325,-1.331373,4.655062,6.338206,-2.217329,5.701273,8.688021,0.818192,5.019727,-1.985167,5.288597,-8.939374,-3.216681,4.437627,-5.992196,0.955742,3.434700,1.066205,5.160010,-8.020538,-8.120216,9.040496,-7.364027,8.849617,-8.901376,-1.108104,4.417169,-0.033807,-9.486958,-9.599760,7.908957,-8.946521,-5.137323,-3.054952,-6.423977,5.968837,-7.176697,-3.827533,7.009569,-8.768315,2.387632,-7.906866,4.867550,-7.410697,-2.979885,-2.547745,0.475510,2.686120,-0.491243,4.856137,-9.262535,3.519783,-1.269903,8.478125,4.119455,7.496667,-5.430208,-0.147180,-7.145704,-1.120016,0.241371,0.354663,3.221328,-3.025917,-2.200183,4.126496,-8.610075,5.871187,-0.914708,9.147949,-9.648247,1.091850,-7.547583,-6.264704,-9.167421,1.567951,5.435479,-3.568858,1.617471,-9.792831,6.001699,-7.037292,8.033911,-7.688706,-1.002506,9.096871,-0.992394,-8.251604,-4.905831,7.728545,3.710801,8.601222,2.713418,5.864547,-8.191408,-1.165431,5.183891,-3.065106,-7.514904,0.424797,-9.324932,2.228686,8.634465,9.640886,-9.976513,-5.721064,3.063128,-9.275198,-0.469923,-9.665570,-8.447002,-2.378311,3.120379,-6.352849,6.813133,6.314518,-1.915802,-4.867817,-0.180922,-2.644910,-7.992295,-6.524213,-9.437351,4.384832,-2.558008,3.328293,-7.654446,6.770716,-8.527373,-1.423223,3.088043,0.646469,-0.136293,6.013755,5.434880,-1.528046,-7.676502,-3.741546,0.474641,2.185962,6.863888,-6.754723,-3.977057,7.019764,7.130323,-3.795256,4.973623,6.313798,7.060754,-5.461845,-0.488596,4.169763,1.564600,7.628441,8.458829,2.605064,9.744973,-9.939958,9.462830,1.088721,1.438362,2.758946,0.339120,7.391987,4.339823,-4.561172,-4.598287,-3.712727,1.511001,-6.698275,1.912350,1.626362,-6.873580,-4.659748,9.485042,-7.162339,-3.393241,-5.883005,-2.355216,-4.750250,0.515609,1.933736,-3.800346,-5.799152,2.685376,-6.724244,-7.937826,-1.366715,-9.017609,-7.168247,-0.786963,-0.391081,-6.712147,-9.217285,-7.324967,-9.895309,9.001008,7.998497,4.902474,8.666772,2.301081,5.593808,5.395310,-4.384076,7.537735,-7.060802,7.379806,-2.632356,4.491555,1.825264,4.979081,5.030268,9.438599,0.701631,-2.734370,-3.436283,-9.222329,1.354868,0.964695,2.022274,-9.382988,-2.976016,0.301937,0.499186,4.270949,-2.745596,-2.147656,-9.979339,2.900695,5.922137,-1.967766,8.500359,4.493115,2.196286,-4.435955,2.788107,-0.140123,-0.067911,-7.947861,-6.084549,-6.810378,5.508112,-5.065841,4.725877,3.298659,-3.940041,-6.771661,-0.594575,-4.838565,-3.097576,8.569882,-7.533939,0.292574,6.704508,-9.710936,1.749261,-0.588295,-6.063483,-8.197353,-1.548878,-7.111284,-2.368956,-4.425185,-5.082147,-7.944855,0.314860,9.734043,5.738556,7.207294,-4.175067,-8.221340,-4.909081,-6.702678,5.293426,-8.336002,-3.364874,-8.608233,0.958935,-2.822581,-8.575795,-6.376881,-5.563476,3.718910,-3.416892,-6.317145,-4.043466,8.461003,9.424529,0.177905,-1.298257,4.617378,-1.078567,5.086483,-4.785901,-3.779519,-0.624115,1.958130,-2.646549,-2.291074,5.715201,6.953342,6.386711,-1.165588,2.096243,-4.763221,-8.178301,-3.914958,2.733529,-8.058466,1.346530,-8.632084,-4.630514,-6.443053,-5.670853,5.111356,4.130418,-2.009795,9.794502,-0.540005,-2.962558,0.970479,-8.547374,-9.344754,1.436332,3.687110,9.870332,3.031932,9.577119,-2.768185,-7.789008,5.456000,-2.237574,9.674462,7.563140,-4.776656,-7.999953,-2.003701,-5.534340,-9.801631,1.492795,-5.750339,-5.001447,-6.975524,-6.778789,7.888001,3.006087,-0.448714,-5.500399,9.420076,4.168710,-1.260892,1.500612,-7.138579,0.061619,-8.483503,9.884906,6.267734,-3.375923,3.217867,-9.047995,1.296265,-5.532972,2.470753,7.197782,-8.953311,7.403815,-4.228538,2.181630,-4.946026,-2.910042,9.284992,7.104751,2.432564,7.040147,-5.153531,6.165331,1.630381,-8.512740,5.904114,3.811690,-5.480525,-5.686229,-2.555267,-7.113837,-7.714159,6.743932,-3.323417,-9.219386,-5.413438,-8.525553,6.547113,-4.827300,3.295032,6.177955,1.474450,-6.475134,4.924420,-3.447539,-6.165961,-5.435204,0.459462,9.823732,1.455676,5.946904,6.516107,-6.485195,-8.830881,9.697152,3.034543,-2.990103,0.168427,5.836905,1.803687,-5.940322,-5.064354,-8.809788,-3.389466,0.311788,4.000699,0.298985,-7.277846,3.505355,1.031530,4.711379,7.042372,5.239216,-8.050856,-1.979521,-5.382206,-1.884214,9.258319,8.348963,-9.910722,5.236890,8.954691,-8.452898,8.331477,-2.813828,-4.982504,4.155351,8.982399,-7.766726,9.997367,7.842840,-7.353757,-3.961812,-1.605659,6.473783,-6.453211,-4.406851,-8.887800,-3.125208,-7.941216,-6.354102,-2.187980,3.275336,-1.175381,0.374296,-5.496997,9.142607,-8.024463,-9.961258,6.259857,8.151966,8.568379,-3.842302,-1.475528,4.963068,6.384387,3.711104,7.072268,-6.185936,6.367121,-0.322478,-5.753470,-8.889427,6.442113,-4.127758,-6.494435,1.436264,7.431022,3.111211,-3.998820,5.244306,-0.221508,4.790022,8.035459,6.699199,2.608002,-3.706096,-5.540463,8.094798,1.239304,-9.156227,9.027605,1.844456], dtype = "float64")#candidate|9579|(2640,)|const|float64
call_9578 = relay.TupleGetItem(func_7901_call(relay.reshape(const_9579.astype('float64'), [2640,])), 2)
call_9580 = relay.TupleGetItem(func_7903_call(relay.reshape(const_9579.astype('float64'), [2640,])), 2)
func_7578_call = mod.get_global_var('func_7578')
func_7580_call = mutated_mod.get_global_var('func_7580')
const_9588 = relay.const([-5.522467,-8.272232,-3.926314,3.833730,-0.151906,-6.769318,2.763388,-3.470193,-7.076268,-5.934170,-0.205639,5.381390,-6.744431,6.978978,-2.953405,-6.945698,-1.429413,8.913746,5.455620,0.229085,1.645281,4.384863,4.366484,7.199903,9.755231,-6.838122,5.850592,-0.996972,7.798427,-1.040285,-7.190520,-3.375901,5.439096,5.757741,2.655029,1.882338,0.202425,7.780795,-7.345828,-4.470937,-6.546973,7.825227,-8.318877,-7.999963,-4.200090,8.569176,0.018164,5.970219,-9.489973,5.701540,-6.685336,-8.862815,-1.508779,-0.493860,-4.351729,-1.293477,4.935479,0.389047,2.199537,1.822271,-4.162426,0.808853,3.170277,-4.967898,5.225800,7.658107,-8.118721,0.054620,3.549308,3.813412,-9.017181,5.210438,-5.529363,7.705245,-6.554043,1.207754,-1.612654,-9.372327,8.507129,9.843685,-7.224863,-1.171630,-4.990664,4.561189,-8.771990,7.729389,6.053427,-2.763220,2.349015,1.248487,0.832361,-5.424579,8.551762,4.827297,-7.892844,-4.063868,4.116608,1.687389,-6.256724,7.982802,-2.784961,-6.161167,8.565049,9.610419,-2.572834,-3.085177,4.154538,2.664643,4.363554,4.413779,6.043130,5.628843,0.361624,-0.035312,8.383079,-2.687175,7.461209,9.350520,0.322370,3.259532,-8.878729,0.896371,1.687943,-7.755511,0.261640,-7.954651,7.115418,3.347193,-0.353452,1.043824,-5.845584,4.975517,-7.997171,-0.192599,6.768999,8.686261,-3.092407,3.110759,-2.586770,-1.285310,-9.796567,-3.814312,-0.174792,-7.949535,-6.084150,3.965696,5.047221,-5.945959,4.819829,8.278050,-0.533399,-6.791366,-5.017262,-8.922370,-8.571054,-3.119341,8.906509,-1.425773,0.326060,8.353556,-0.155969,-7.143982,2.088614,9.779311,7.341070,-6.110698,-2.191354,-4.237316,-8.362677,0.928739,-5.340728,1.433776,-6.721978,9.813757,-2.995578,9.201743,8.783469,-6.489785,-1.721276,-6.432500,9.854546,-2.731479,4.725104,-4.670305,9.973508,-1.745729,1.817406,-2.827814,-9.677824,2.673840,-1.833377,0.520955,-0.085409,-4.325384,-4.307586,5.120932,2.174659,4.785336,-5.275161,0.755903,9.108415,2.611876,2.942121,-4.898361,-4.187875,4.904679,8.308688,-6.898595,-0.402582,-6.490430,8.067724,-0.681743,9.493192,-3.959089,2.629949,-0.446072,0.490460,-5.867225,1.615829,-8.666082,-4.452042,-3.196620,3.696948,-9.057450,8.411373,-1.500277,-6.121314,-2.177920,-6.179509,5.710520,-0.125198,-5.149285,-7.746863,-5.118641,9.078878,0.649820,-9.924296,1.544744,-7.713277,-5.485672,4.325134,6.351152,4.616601,4.607966,-0.859188,-5.573985,-4.386915,-9.090884,4.526293,-3.094761,-1.784588,-9.908521,5.772293,-5.643352,5.399459,-7.946666,8.299308,-0.198975,4.948005,-6.742892,9.749453,-2.121966,5.791878,-8.897318,2.719094,1.742674,-3.778016,5.510850,-1.880465,0.814651,-7.854665,-5.446893,2.169342,-2.133406,-2.726728,-2.542934,4.075991,-8.197407,-3.338577,1.079990,7.582684,7.340671,0.097535,-7.017922,-4.765093,8.116229,3.918638,-9.833349,0.484130,1.321657,9.203223,1.964713,-0.991755,4.119552,-6.606197,-6.925794,1.965485,7.275717,-3.357646,-7.823632,8.578400,1.827175,8.945581,-1.342608,7.091925,6.837465,7.341737,6.639599,-5.512318,-9.272150,-0.285856,-0.403870,-8.396211,-4.441951,5.294418,8.743296,-9.277346,6.590240,-6.295124,-5.342613,0.152266,-8.022775,-9.328210,-9.787295,-4.605316,3.165812,-2.345518,9.589777,2.855110,1.919606,-7.828627,-4.427794,-8.706349,9.722120,6.309094,-8.523005,7.983284,3.514908,-3.221397,-6.849659,4.081157,7.196274,0.660694,-6.609954,-7.571837,-7.385739,7.140382,-0.806428,-6.000848,-6.412241,2.752885,6.210321,-7.783464,6.025747,-7.215506,7.962136,0.998785,3.896946,8.110247,-7.197159,-3.360795,0.745963,4.909530,6.882212,0.758507,1.605222,-4.485200,7.747925,5.447664,2.413836,-3.414699,7.088135,-4.055793,-2.129688,6.444026,9.356630,5.179235,8.005554,-2.770564,5.505081,-2.539264,4.899530,7.160465,3.999536,0.011577,-3.831441,-3.681986,6.451399,5.951327,-8.421545,-7.292517,-3.953627,-3.033073,-0.754371,-0.322138,-8.307780,-3.024616,2.018402,-7.654695,5.622401,4.271023,7.453696,5.464095,-3.196061,5.392314,6.537692,4.002477,7.168787,9.360325,-9.082123,2.753776,5.516380,-4.134579,1.509530,5.422027,-7.606226,8.822548,-0.535434,3.411537,4.003013,-1.135426,-6.870642,-0.644607,9.817439,-2.053406,6.722508,1.729310,0.029699,7.789893,-7.603681,9.994355,2.422975,2.585001,-2.866378,3.998245,2.436624,-5.241270,4.833086,3.028484,3.264746,-0.183103,-9.426614,7.041289,-7.775309,-9.538706,5.358052,6.669763,-2.104850,7.318667,1.157035,-0.791533,-1.070115,1.565200,1.361978,-3.686893,-2.423245,3.023268,-6.022187,-8.886326,3.341588,-6.935739,5.116897,-2.679621,-7.355050,-4.753990,-2.035494,-4.581038,2.759450,-8.800612,-9.084416,7.065309,2.374751,8.039017,8.321695,-4.137549,9.641681,-2.137050,5.325234,-5.807976,-7.330227,6.244371,-3.713467,1.842911,1.255782,-0.529900,-0.077022,-9.764537,0.963571,-9.730451,-9.004136,0.109467,7.799362,-5.007075,-4.516209,-3.283365,0.724769,4.600746,2.825939,2.945624,-4.695737,-7.181285,-9.343858,8.113273,6.864262,-4.859747,-4.133519,5.006983,4.287140,-0.129199,-6.513373,-7.655481,7.102813,6.676595,-6.108928,0.021645,0.001465,-4.955241,3.569139,6.562132,2.972603,-8.241875,4.183134,5.467459,6.887117,4.561807,-5.040760,9.985626,0.576384,-6.139173,7.268307,4.093891,5.968240,-4.335303,1.886024,2.978371,-6.290230,-1.242695,9.152146,-2.731627,-6.467210,7.040771,-0.261074,-6.378366,6.854092,1.230204,-1.527840,9.762834,-1.307811,-9.419373,6.124084,-8.769425,7.152323,-0.415204,-3.841393,7.427426,-4.394616,0.978654,6.687711,-2.146587,-1.574341,-0.729212,-6.663311,3.065318,3.392390,-8.859591,3.603319,-3.374780,-5.508803,-7.226881,-6.760635,4.551301,-2.977853,9.714436,-9.180666,-4.426988,5.247782,7.512304,3.097798,1.374919,1.887754,4.751224,-7.527776,3.225056,-2.506135,-7.968953,-1.709844,0.759545,-8.514972,-2.474476,0.129641,-0.829634,7.103986,-2.462409,-8.454481,-2.034743,-8.529712,-6.849616,7.003341,9.593194,9.500400,-4.513281,5.761506,-6.125885,-5.250424,-7.986266,-2.414422,9.287255,-5.395272,-9.848579,5.530336,-0.585884,-0.509432,-6.487246,3.275529,-5.196335,3.497063,-1.744477,-3.445763,3.281831,6.459212,-8.651073,-8.062660,-4.132646,-0.144815,6.191505,2.118161,5.938300,-9.895989,1.594063,1.576576,3.491448,8.967828,2.340736,-5.188459,-3.222598,-6.445614,6.063361,-9.657338,7.662745,-4.818903,-9.217872,8.027209,-3.276731,-8.270178,9.790701,2.295515,-0.043625,-6.680554,-0.241456,-8.862400,-7.141471,-2.646907,8.334331,2.288980,1.784984,4.115707,9.553419,3.251164,7.100202,-3.121741,7.168155,8.541145,-5.430498,3.387900,-0.997262,4.313773,-3.681507,9.767688,8.036982,-6.847364,-6.769496,-6.643955,-8.574066,5.839125,2.259929,-7.311150,9.833797,0.422890,8.228579,8.977436,-4.831915,9.480854,-1.651477,6.907740,8.798861,-7.704741,7.726929,-4.743647,-4.781669,1.874950,8.246118,-9.984451,3.891551,-0.531189,-3.367414,5.097821,-9.686692,8.551631,9.031008,-9.680597,-6.696598,-1.764182,-6.427154,-8.881621,4.914699,-0.965391,8.584539,8.999923,-4.694098,-6.202038,6.054515,-7.724924,-3.024441,-6.941757,-3.528114,-8.149919,6.628926,-0.978674,4.419105,-0.002378,9.844818,9.608642,5.979690,8.824547,-6.466501,-7.274457,9.809190,-9.238093,-2.284319,1.976369,8.314256,-0.329817,1.288899,-4.328162,3.356520,8.886861,-4.328469,2.325366,2.308953,6.246218,-9.553540,-6.573182,-8.685134,0.069225,1.598748,4.000478,7.073695,-7.626863,6.661330,5.551209,2.849259,0.504576,-9.517351,-6.917884,9.645733,5.365963,5.877934,-1.167579,-1.587443,3.199090,-4.934720,6.345488,-9.021502,-8.953096,-4.447399,-6.685585,-6.039269,6.173306,-1.417953,4.996394,-8.210470,-9.669674,-1.377557,7.161730,-8.100451,-3.881597,-4.552976,-6.366023,1.618832,-4.900218,1.079829,-4.357955,-2.350744,-5.153689,3.153110,-4.771665,-5.783906,5.714084,0.788085,-9.460495,4.175637,0.036293,-2.066930,-4.207386,-2.843029,0.721657,7.526584,-2.859807,-5.553557,1.816728,-2.297144,6.388085,-6.127365,6.414917,6.742050,0.132627,-2.016286,-2.005798,9.676864,7.260793,4.107074,3.322922,-5.850120,-7.552826,-9.473825,-7.979909,-1.493444,2.449202,-2.150012,-8.099785,-9.401773,6.667765,-4.721190,4.759203,-3.374341,-7.561743,-3.871801,5.792198,4.178348,3.727446,1.243955,-3.550371,2.561138,-9.645039,-4.459418,7.231403,-5.275035,0.013494,6.389228,-0.157546,4.597366,4.060682,-8.129672,-2.657549,7.513887,2.653411,7.313393,-4.665531,-7.905376,6.146856,5.950734,1.854780,7.418513,9.673814,-3.775324,-7.897371,-9.803610,5.171519,-7.442007,-2.262931,0.056815,-1.296929,3.068281,7.708078,4.881315,-8.647690,1.606877,1.510638,-4.928462,4.086536,-0.626731,8.439324,-7.886039,-9.086623,-2.786721,-3.388292,-4.131101,2.600809,5.900959,3.976903,4.668224,5.416956,-1.885415,7.390148,6.657686,1.461524,-5.531445,-8.701458,8.246206,-2.277044,2.698466,6.968727,7.463546,5.138059,1.794495,-5.894559,-7.708960,8.351431,-9.429970,-9.754105,-2.305440,1.446778,-6.412750,8.895478,-5.188684,3.879892,-4.198667,-1.594720,7.140337,-3.652413,-8.651006,3.987677,-6.943037,1.022793,9.317950,3.437974,2.170863,9.247331,-9.039962,5.578785,-2.351066,5.481528,7.994436,-7.949414,1.495288,0.228850,4.549089,8.423313,-2.968624,-0.057336,-3.514219,0.549416,3.306129,7.063832,6.068709,-1.532695,9.901389,-6.944414,0.799908,-3.332813,0.370750,6.615449,-1.708040,-5.719654,2.476297,2.212531,-1.867464,-8.229923,8.816408,-4.947215,-3.346291,-7.152096,-1.846014,0.589984,4.988576,-0.310905,5.488402,-1.306602,-9.395768,-0.926831,5.268480,4.488597,-0.395783,7.301138,5.656995,-3.212436,4.540766,-6.193811,6.473273,6.847554,2.123108,3.572904,3.697038,-1.423571,7.186076,-8.820612,-1.382693,-9.648488,4.266930,-1.339173,0.192617,-4.085415,4.992966,-2.384355,-1.138241,-4.608613,-3.027467,9.389060,0.270044,9.996912], dtype = "float64")#candidate|9588|(990,)|const|float64
call_9587 = relay.TupleGetItem(func_7578_call(relay.reshape(const_9588.astype('float64'), [990,])), 2)
call_9589 = relay.TupleGetItem(func_7580_call(relay.reshape(const_9588.astype('float64'), [990,])), 2)
func_1417_call = mod.get_global_var('func_1417')
func_1418_call = mutated_mod.get_global_var('func_1418')
call_9593 = func_1417_call()
call_9594 = func_1417_call()
uop_9601 = relay.asinh(call_9544.astype('float64')) # shape=(15, 10, 16)
uop_9603 = relay.asinh(call_9546.astype('float64')) # shape=(15, 10, 16)
func_3835_call = mod.get_global_var('func_3835')
func_3838_call = mutated_mod.get_global_var('func_3838')
const_9615 = relay.const([-8,3,-8,7,-8,-2,-4,5,6,5,10,-1,4,-7,8,4,4,9,-4,10,9,10,8,-7,9,-10,-8,3,2,4,-1,-5,-10,9,-3,9,-2,-5,-6,7,-4,6,9,5,9,-3,-10,7,3,5,6,-7,-2,-1,5,-6,4,-3,1,-6,9,-3,8,-10,-8,8,-8,-4,-5,1,-2,1,10,1,-1,-2,-6,1,6,6,4,-10,7,5,1,-4,-4,1,10,-5,-10,-3,-3,2,-4,7,-2,-4,-3,5,-6,6,-5,-6,-10,-7,-8,-9,-5,-2,1,10,-8,-4,-3,4,-7,3,-9,8,8,2,-4,-6,-3,-9,-10,10,3,-7,-3,8,-5,-4,10,6,5,-3,-2,-9,9,-1,-9,5,5,8,4,7,-9,-6,1,6,-1,-5,7,-7,-4,-3,9,4,-9,9,-2,-5,-7], dtype = "int8")#candidate|9615|(165,)|const|int8
call_9614 = relay.TupleGetItem(func_3835_call(relay.reshape(const_9615.astype('int8'), [11, 5, 3]), relay.reshape(const_9579.astype('float64'), [15, 11, 16]), ), 1)
call_9616 = relay.TupleGetItem(func_3838_call(relay.reshape(const_9615.astype('int8'), [11, 5, 3]), relay.reshape(const_9579.astype('float64'), [15, 11, 16]), ), 1)
func_3835_call = mod.get_global_var('func_3835')
func_3838_call = mutated_mod.get_global_var('func_3838')
call_9617 = relay.TupleGetItem(func_3835_call(relay.reshape(const_9615.astype('int8'), [11, 5, 3]), relay.reshape(call_9614.astype('float64'), [15, 11, 16]), ), 1)
call_9618 = relay.TupleGetItem(func_3838_call(relay.reshape(const_9615.astype('int8'), [11, 5, 3]), relay.reshape(call_9614.astype('float64'), [15, 11, 16]), ), 1)
func_8521_call = mod.get_global_var('func_8521')
func_8522_call = mutated_mod.get_global_var('func_8522')
call_9619 = relay.TupleGetItem(func_8521_call(), 0)
call_9620 = relay.TupleGetItem(func_8522_call(), 0)
output = relay.Tuple([uop_9537,const_9545,uop_9555,call_9565,call_9578,const_9579,call_9587,const_9588,call_9593,uop_9601,call_9614,const_9615,call_9617,call_9619,])
output2 = relay.Tuple([uop_9539,const_9545,uop_9555,call_9566,call_9580,const_9579,call_9589,const_9588,call_9594,uop_9603,call_9616,const_9615,call_9618,call_9620,])
func_9622 = relay.Function([], output)
mod['func_9622'] = func_9622
mod = relay.transform.InferType()(mod)
mutated_mod['func_9622'] = func_9622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9622_call = mutated_mod.get_global_var('func_9622')
call_9623 = func_9622_call()
output = call_9623
func_9624 = relay.Function([], output)
mutated_mod['func_9624'] = func_9624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3060_call = mod.get_global_var('func_3060')
func_3062_call = mutated_mod.get_global_var('func_3062')
call_9674 = func_3060_call()
call_9675 = func_3060_call()
output = relay.Tuple([call_9674,])
output2 = relay.Tuple([call_9675,])
func_9676 = relay.Function([], output)
mod['func_9676'] = func_9676
mod = relay.transform.InferType()(mod)
mutated_mod['func_9676'] = func_9676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9676_call = mutated_mod.get_global_var('func_9676')
call_9677 = func_9676_call()
output = call_9677
func_9678 = relay.Function([], output)
mutated_mod['func_9678'] = func_9678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9715 = relay.var("var_9715", dtype = "float64", shape = (4, 9, 3))#candidate|9715|(4, 9, 3)|var|float64
uop_9716 = relay.sigmoid(var_9715.astype('float64')) # shape=(4, 9, 3)
output = relay.Tuple([uop_9716,])
output2 = relay.Tuple([uop_9716,])
func_9731 = relay.Function([var_9715,], output)
mod['func_9731'] = func_9731
mod = relay.transform.InferType()(mod)
mutated_mod['func_9731'] = func_9731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9732 = relay.var("var_9732", dtype = "float64", shape = (4, 9, 3))#candidate|9732|(4, 9, 3)|var|float64
func_9731_call = mutated_mod.get_global_var('func_9731')
call_9733 = func_9731_call(var_9732)
output = call_9733
func_9734 = relay.Function([var_9732], output)
mutated_mod['func_9734'] = func_9734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7393_call = mod.get_global_var('func_7393')
func_7395_call = mutated_mod.get_global_var('func_7395')
call_9736 = relay.TupleGetItem(func_7393_call(), 0)
call_9737 = relay.TupleGetItem(func_7395_call(), 0)
var_9740 = relay.var("var_9740", dtype = "float64", shape = (15, 5, 16))#candidate|9740|(15, 5, 16)|var|float64
bop_9741 = relay.less_equal(call_9736.astype('bool'), var_9740.astype('bool')) # shape=(15, 5, 16)
bop_9744 = relay.less_equal(call_9737.astype('bool'), var_9740.astype('bool')) # shape=(15, 5, 16)
bop_9746 = relay.bitwise_and(call_9736.astype('int64'), var_9740.astype('int64')) # shape=(15, 5, 16)
bop_9749 = relay.bitwise_and(call_9737.astype('int64'), var_9740.astype('int64')) # shape=(15, 5, 16)
func_6355_call = mod.get_global_var('func_6355')
func_6357_call = mutated_mod.get_global_var('func_6357')
call_9758 = func_6355_call()
call_9759 = func_6355_call()
output = relay.Tuple([bop_9741,bop_9746,call_9758,])
output2 = relay.Tuple([bop_9744,bop_9749,call_9759,])
func_9762 = relay.Function([var_9740,], output)
mod['func_9762'] = func_9762
mod = relay.transform.InferType()(mod)
mutated_mod['func_9762'] = func_9762
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9763 = relay.var("var_9763", dtype = "float64", shape = (15, 5, 16))#candidate|9763|(15, 5, 16)|var|float64
func_9762_call = mutated_mod.get_global_var('func_9762')
call_9764 = func_9762_call(var_9763)
output = call_9764
func_9765 = relay.Function([var_9763], output)
mutated_mod['func_9765'] = func_9765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6227_call = mod.get_global_var('func_6227')
func_6229_call = mutated_mod.get_global_var('func_6229')
call_9799 = relay.TupleGetItem(func_6227_call(), 1)
call_9800 = relay.TupleGetItem(func_6229_call(), 1)
output = call_9799
output2 = call_9800
func_9813 = relay.Function([], output)
mod['func_9813'] = func_9813
mod = relay.transform.InferType()(mod)
output = func_9813()
func_9814 = relay.Function([], output)
mutated_mod['func_9814'] = func_9814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4685_call = mod.get_global_var('func_4685')
func_4687_call = mutated_mod.get_global_var('func_4687')
call_9839 = relay.TupleGetItem(func_4685_call(), 0)
call_9840 = relay.TupleGetItem(func_4687_call(), 0)
func_7690_call = mod.get_global_var('func_7690')
func_7692_call = mutated_mod.get_global_var('func_7692')
var_9845 = relay.var("var_9845", dtype = "float64", shape = (396,))#candidate|9845|(396,)|var|float64
call_9844 = relay.TupleGetItem(func_7690_call(relay.reshape(var_9845.astype('float64'), [396,])), 1)
call_9846 = relay.TupleGetItem(func_7692_call(relay.reshape(var_9845.astype('float64'), [396,])), 1)
const_9849 = relay.const([[[6.375799,6.297051,6.999328,0.063985,-1.558339,-7.013484,-1.326516,-9.734172,-9.182336,3.507916,6.294133,-7.676527,8.228694,4.252589,3.846851,2.326311],[2.601058,3.152194,9.522463,3.425454,0.385541,-7.651974,0.690685,-8.967129,-9.333887,8.608318,7.904707,7.416054,-1.920137,7.590288,1.336155,-2.818149],[-7.682336,8.491816,8.102837,2.093935,-3.665745,-2.091436,-5.015754,6.568911,-8.839905,-4.218669,-9.083975,-1.946909,8.447405,-7.451306,1.001352,8.752286],[0.461924,5.098492,5.810545,2.388089,-0.385590,5.386229,-3.505685,-9.411364,7.058205,-1.604896,-5.220517,-2.811232,4.358252,-0.569048,-3.598567,-6.950938],[-0.842884,-9.672207,-5.471575,3.424282,8.582519,5.179466,6.223272,9.902021,0.792594,-1.988708,-6.721730,9.253130,2.319058,-9.801208,2.244803,0.138181],[-3.937577,2.074319,5.062777,-0.445742,0.264384,9.688690,9.869634,0.596192,-3.250249,-6.463346,4.781966,-6.012411,6.480460,-9.713060,7.247582,-6.790216],[1.910749,-4.805594,-4.251732,2.128075,2.339371,-8.654430,5.281984,2.432657,6.801120,5.923026,3.860989,2.894791,-2.842384,0.813660,-6.907229,-8.568174],[0.802058,-3.890197,4.274778,9.604734,-2.846742,3.298155,1.108532,-4.674355,-9.833218,7.460527,9.732511,-0.770316,-5.763755,-2.726681,3.801028,-6.988850],[2.912158,-4.312763,8.258428,5.761799,9.981344,9.774714,8.942682,2.035810,6.458788,2.115874,7.516896,6.558821,4.757995,-8.514386,-2.236363,3.180681],[-7.635536,-6.497313,1.142920,9.327880,-7.126106,-7.431797,-0.475069,6.743572,-4.170431,5.844329,-1.331531,-3.042518,-2.042902,-5.885864,3.800039,-3.974314],[9.264170,8.523189,4.848163,1.343553,-4.846272,4.049140,9.124859,-4.481875,-8.026113,2.602398,-6.306778,-6.018638,4.172018,5.286743,1.180547,-8.687303]],[[-1.982190,5.293664,-3.980402,8.577965,-4.586956,-3.898591,2.323924,-6.033917,-9.130232,-3.929591,4.757995,1.044214,9.651802,7.035887,-4.842244,1.920146],[-5.319945,-1.219503,8.455018,3.987880,8.044966,6.111706,-7.635955,-7.059209,-6.385375,-2.953896,4.164327,-4.233759,-2.573471,3.425037,4.439750,-4.849837],[-8.940422,-1.154450,-6.424561,9.640613,9.503815,4.634186,-0.505625,-8.109047,-4.373114,-8.332051,-2.803921,4.717469,6.585329,-4.591205,1.016444,-7.438327],[2.060061,-6.608419,-2.033759,5.720985,-6.377123,7.049251,-8.454802,0.227023,-9.201241,6.385770,-2.211671,-3.482444,7.639524,-0.425283,8.323028,-9.200690],[-5.711370,-0.173825,7.302812,-2.799869,-1.454906,-1.939062,-5.473284,-2.503302,-2.166136,3.289672,-3.320053,-2.075891,-2.498074,-2.015128,5.959490,1.135064],[0.771340,-0.699267,7.886494,9.596129,-3.124374,8.102351,9.369578,-3.630277,1.373100,5.593705,8.733806,2.772529,-2.185710,9.109684,4.339969,1.456354],[-1.529332,4.406558,7.669580,-4.143118,-8.723220,-9.367548,5.664045,3.973409,-6.756954,-8.545415,-0.457100,-6.375288,9.304411,-3.228607,-2.826070,-1.652260],[9.384837,-3.513846,-2.730403,9.513282,-0.495419,-0.010668,-8.588617,-8.463739,-3.317779,-9.222724,9.907167,-3.801622,-1.203854,9.118511,-7.474581,9.348199],[2.175110,-2.910226,-9.915794,-5.799850,4.450582,-8.072434,3.966259,5.710809,2.105730,-6.322871,-0.798835,-9.254827,-1.566309,0.781588,3.312285,-2.052173],[-8.412607,-3.024370,-5.620454,-0.239720,2.719089,3.697923,2.745886,7.910616,-0.697613,0.875776,-6.882146,1.620210,6.971541,9.570608,-4.657712,7.469108],[7.055315,3.244196,8.646326,3.176432,9.235664,4.654704,6.422478,0.364829,-1.131480,-5.753215,-3.272304,8.257201,-0.638912,-2.321566,5.791137,-4.076698]],[[7.117583,-0.370982,5.788990,-1.580633,8.199536,4.299571,-5.504271,-5.920996,-7.061067,8.501466,3.272374,-4.127496,5.702047,-3.396481,6.341896,5.799805],[-6.077155,0.792913,-0.290738,-2.864960,0.137546,-8.807724,8.741269,-3.447911,-9.063256,-0.008751,1.747365,7.352078,-3.939970,4.857777,-8.238891,-0.901789],[-3.696913,-7.011455,0.215713,-6.122312,2.087986,-5.349318,-0.660479,-5.154939,-5.546313,-2.265833,8.825148,5.453287,0.858487,3.543971,3.737312,-5.263883],[1.569802,-6.877099,-4.174012,9.282590,-9.052327,-1.602126,2.421798,4.760827,0.610328,3.502933,5.825735,-5.056602,3.118122,8.491602,-4.914334,-1.243464],[-2.581884,-4.154365,-4.297082,-4.330158,-7.150468,1.589552,0.329850,6.255432,-3.655213,-2.898688,4.200068,-5.345191,-4.159953,-6.183336,0.349209,1.843703],[5.325722,-5.428482,0.980949,-5.013845,7.366009,5.504515,-0.046258,-4.696591,6.451927,4.784707,1.199270,3.363283,8.681570,-8.248028,4.651807,-3.107727],[-5.693179,-9.116631,-3.443524,5.927952,-5.620243,-6.523348,7.323092,2.931942,9.658860,-4.177810,-0.794511,1.487827,4.385459,-3.069156,1.441529,5.000994],[-1.366614,0.780334,0.957531,-9.197901,-2.031353,-8.661652,2.197609,-5.337180,-9.202890,-8.056129,7.838984,-6.946028,0.225236,7.040828,-7.113947,-4.850382],[-3.874029,9.212346,-3.950637,5.795616,-0.890829,0.511708,6.391162,5.686299,-7.328150,-3.502786,1.913651,-8.001492,4.189585,7.365690,-6.892693,-6.497742],[1.150583,-5.086028,-5.409941,-4.818140,-3.846069,-1.318062,-1.302414,1.545245,8.005015,-2.405393,6.073677,-5.199167,-4.155185,-8.297821,5.074787,2.136618],[-1.473169,7.339399,4.628103,0.824241,8.985267,3.378242,9.220417,-4.801857,-9.122115,6.763461,9.870569,-3.677469,6.922017,-6.447002,-5.278569,-9.168978]],[[-0.658010,1.522588,0.446010,0.702774,-9.852968,-0.754462,4.455359,3.100158,2.171140,1.159250,-4.405695,-4.751952,-0.129652,-4.500356,-3.998969,8.099853],[-9.551347,-9.855203,-5.735751,-3.325337,-5.582578,-6.606692,0.768652,8.825612,9.888405,9.534728,3.148899,9.029985,4.712294,-7.055555,-5.620664,-0.375764],[-3.918591,2.117628,-2.703851,8.441482,-4.822474,-4.416618,8.522906,0.794028,6.842935,-3.164771,-2.507705,-2.356024,-0.538589,-6.752512,2.909467,7.224611],[1.929695,-7.032606,4.318409,6.501087,2.657259,3.715435,4.599877,4.490256,-8.877725,5.548001,-9.551989,-8.068342,-2.228674,8.910985,0.887419,0.199469],[9.729243,-5.085134,-0.785157,8.294084,2.412956,-5.418932,6.901651,1.670776,-5.527570,-8.089467,8.821348,1.464694,0.177209,6.575895,2.711215,-0.803613],[-8.248106,0.150738,-1.863663,-2.697457,-5.526807,-3.478889,5.450520,7.209625,8.060795,-0.268558,-7.612405,-4.404672,-9.170612,-1.303418,4.764773,9.317338],[4.149248,-4.660249,5.570098,4.041366,0.432382,1.039050,-6.222543,-8.255842,-2.136700,-8.786427,-6.818603,6.864227,-2.324840,9.233706,-2.300448,9.032966],[9.772407,8.543039,-8.647233,-2.953046,-5.134228,-7.415253,-4.574007,-5.994955,9.252995,2.259491,-0.871485,8.279158,-4.302782,-8.547560,0.284047,-3.835479],[1.696456,1.457393,8.827706,1.329764,6.106742,-9.211760,2.966273,-7.012791,0.187253,-6.916664,-5.744376,-7.392145,-3.505655,8.150437,-8.728264,7.399663],[3.547042,4.441976,-6.674963,1.877608,2.336803,-7.611150,-0.670633,1.690537,-8.255021,0.616823,7.504009,-0.423419,-6.609329,9.886599,4.524643,-9.250554],[0.850827,6.357501,2.170187,4.982108,-0.363457,7.225396,3.850690,-9.339506,-2.753831,-0.893196,4.672816,-1.142820,0.352808,-5.007669,-6.791560,0.276880]],[[8.729338,5.326542,4.854564,1.091962,-5.212125,6.660399,6.509589,-8.716203,8.573360,-8.770980,9.857292,6.655419,-1.592499,8.609400,-0.749361,0.882964],[-1.413736,-9.608662,3.231835,3.794401,-1.697022,8.537282,9.062171,-8.156491,5.347031,5.754444,5.816932,5.818321,5.066641,-4.138784,8.397202,5.999295],[-3.903057,-2.036022,9.767891,-0.680240,-4.953509,7.354456,5.402015,-0.997952,-6.329020,2.284851,-5.205907,-4.644960,6.584743,-9.810813,-2.083412,-3.601365],[2.339019,-5.867792,6.190206,4.318663,4.728193,9.460775,-3.572193,1.300862,9.744912,-9.520585,8.224047,8.606303,7.820324,2.968888,3.820973,-1.495608],[-1.345383,8.452921,9.280069,4.777385,-5.466049,2.642003,5.016542,8.950259,5.360353,-2.228121,-6.147496,-0.481316,6.768860,5.601428,7.513414,-8.765795],[7.997821,3.822819,-9.209715,1.622842,2.208613,5.320525,9.469709,-3.281136,-8.757951,3.534681,-1.957302,-5.757057,6.881290,2.074181,5.465385,1.096099],[6.393664,-6.706584,2.812457,-4.121348,-4.288221,7.825703,2.625649,1.482721,5.396807,-7.138966,-6.720039,5.095706,4.418089,-5.699994,-9.329612,8.924302],[5.066852,1.713621,1.374118,1.165060,0.729882,0.963638,-4.405625,-7.522296,8.621313,-9.388261,0.219722,3.740056,-4.833240,-9.061387,1.522141,-0.315889],[4.865975,-5.196070,-3.845455,-6.229007,-5.660388,-7.555534,-7.134650,-0.900432,8.008804,6.349891,3.695718,1.718512,1.068959,-7.963108,7.878589,3.948076],[7.067996,0.631231,9.487523,6.000571,5.677939,5.039962,2.036989,0.003631,-2.091699,9.182752,-0.242943,5.780951,-6.617278,-4.237714,-2.924384,-3.853763],[6.583450,4.797946,-5.279528,4.813907,-9.466532,7.025728,-7.746385,0.139364,-9.233844,-3.053742,3.081320,-5.630098,-4.393320,-4.918663,-1.473610,-2.488491]],[[-4.352344,-0.213764,-4.206509,7.913664,-8.308567,-9.870715,0.911638,2.394990,6.620895,-9.901638,2.614612,-2.560786,-1.272992,0.676943,-1.990279,-2.352201],[9.261383,1.867061,-8.411014,6.124437,4.117568,-3.105057,2.891388,-3.608755,1.330438,7.379655,9.706125,-4.895334,-5.848580,-6.826484,1.161689,-0.020807],[-3.325037,0.128869,-2.459804,1.426944,-2.926567,-7.177023,-7.200506,-6.165620,-9.111904,-0.466991,-9.847534,5.279147,-9.574714,6.907335,-4.435889,5.517983],[8.285260,-8.631438,8.112768,4.716399,7.391509,7.359331,1.294821,8.108293,4.395636,8.858527,9.115714,0.965699,9.733919,5.973566,-5.527839,-2.761254],[1.847504,9.326258,-5.227110,3.197543,-9.357593,5.253467,-5.862578,3.008540,7.566550,6.034924,2.525372,-7.006788,3.208992,0.668658,-7.318174,2.368200],[-8.042274,-9.830205,-2.071186,-1.292102,-6.527604,-6.464559,-4.145226,6.873226,-4.148929,-4.648805,9.947156,-6.500656,0.751008,-6.684738,0.904220,9.653310],[-8.304240,5.410850,8.879056,7.513579,9.299171,9.298498,-7.899772,7.306936,8.545338,-4.829114,6.623091,-8.851794,-5.354035,-1.021839,-6.027669,5.762120],[-6.478607,4.538241,-6.106048,1.148826,-4.959504,-4.074038,9.038815,-8.220862,3.134157,9.429688,5.822906,8.430495,-3.276007,-3.495406,-0.388875,7.997486],[-0.742636,-7.090634,-6.850081,-5.753623,-3.988734,6.690704,9.864992,7.038633,-3.366628,7.390530,-5.239416,-0.177990,-2.797501,5.927561,-8.002756,2.905777],[-2.452855,-3.717570,-6.866511,5.228479,8.973743,-0.669644,-3.635151,6.159330,6.721284,0.389575,-9.892213,-7.402145,-1.822751,2.686650,2.841613,7.080821],[-1.466054,-9.211987,-1.535301,-0.842548,-5.426335,-9.338262,-4.365795,9.989179,-1.128733,0.826256,-1.334516,-1.877962,0.332152,-5.128839,-4.969599,-6.936045]],[[4.376020,9.632464,9.019163,2.461617,8.387141,-5.099459,1.517487,3.209916,-2.199093,-4.031011,-4.691395,5.476632,-1.215744,-3.502257,1.803155,-8.247975],[2.362442,7.934320,8.862657,-1.393201,-7.168026,-5.896447,5.251143,-0.006182,-6.458239,-6.849979,9.325689,-3.188360,5.332078,-5.463550,-8.482132,4.259537],[0.248002,-0.890219,1.171466,9.570418,8.089934,-7.196501,3.557797,3.477781,2.944304,-0.384065,7.212495,3.638989,-8.566799,-8.788897,-0.685304,-4.199083],[-0.801486,-1.717240,-2.635423,0.798490,4.293288,-4.305759,-9.373595,-5.117659,8.600952,-5.106227,4.787241,-2.890170,-7.252676,-9.346297,-2.846429,-2.202539],[1.018423,2.708855,-9.929353,-2.189854,-1.048275,-9.951373,-0.848831,-6.372836,5.598713,-6.626786,-7.716744,-9.755043,5.218349,4.141010,-8.988342,-5.258478],[-3.227759,2.105028,8.821556,-3.490521,-4.761146,-7.492790,5.691865,-8.281135,-5.517775,-8.403245,5.565085,2.884834,4.317712,5.632678,-9.194494,-5.727392],[1.496213,6.896098,9.999052,-8.023182,-7.751737,-3.242396,2.659023,-7.015227,6.384182,2.440490,-3.282913,-7.593498,6.072277,4.377620,9.132205,0.610843],[8.811702,9.284154,-2.272074,-4.386787,5.891816,7.958580,2.020902,-0.383689,-5.559532,-7.823308,-2.403525,-8.053395,-3.654014,5.100456,5.680380,-0.814414],[8.459348,5.193125,1.351857,-9.302746,-2.758770,3.398114,6.466658,3.678872,1.366833,-0.256447,-0.313121,-9.966355,-3.760274,-9.692876,-9.151851,-1.679588],[8.593860,9.801175,0.806523,7.750580,9.214211,-7.850166,-2.853045,-5.421399,7.185283,4.204762,-5.957759,-7.142375,2.849360,-5.023786,3.168254,3.289930],[1.560168,4.396131,-9.261072,-3.547294,2.583425,-7.704860,-1.493494,-5.724744,-2.345424,1.947063,2.342637,6.639760,1.359976,-2.702669,8.641734,6.817925]],[[-7.156596,6.721051,0.386067,5.612186,-2.810447,-1.877983,-9.677350,-2.535797,-3.189560,8.229565,5.437707,-5.404209,5.492336,3.073781,-0.913919,7.335098],[4.385147,0.597867,-4.180086,-6.677550,-4.913150,-4.274126,2.996576,3.098850,-6.658755,5.099764,-3.911732,-0.986396,-4.242688,-0.289437,-9.505870,3.934873],[-2.851087,-1.435421,4.798437,-2.739834,6.452040,9.231495,4.322798,-7.508434,6.571369,-0.531238,4.523940,0.083073,-3.645677,-9.978275,3.457112,4.058552],[-1.569074,0.379470,-5.561452,-7.332423,-5.518054,-9.550203,-8.430696,9.046057,-8.394813,2.760507,4.779672,8.171664,-0.230903,-0.229569,3.357154,-4.827571],[-5.408660,-5.234810,4.343383,-4.381906,-2.149571,8.892082,-1.721668,-8.657531,-0.207976,-1.132890,8.821384,-3.075838,-5.948672,4.578174,-6.016430,7.275146],[5.235769,6.294825,-4.317736,-7.500327,-8.972763,-1.465333,2.872485,0.565112,-9.161570,1.530633,0.026061,-2.495826,-7.704916,9.043493,4.295432,0.936871],[-9.633342,2.771209,8.145630,4.795182,3.777912,-8.956247,8.715638,9.798212,3.352161,4.443025,-3.271383,-1.962505,9.335001,9.587682,7.013910,-4.415019],[9.718269,-2.442475,1.548256,-0.339971,4.462949,7.477113,-9.734974,2.920798,9.730310,-7.183421,-9.701291,1.081335,-8.462498,-4.637190,8.845436,-2.593439],[-9.636477,3.482025,-0.805941,-2.715858,-3.259279,-2.992185,-6.267098,5.279090,-2.120811,9.808344,-1.065104,7.502632,4.915709,-4.981324,-2.735129,4.399420],[-4.174269,-7.982168,-7.397805,-3.570465,6.260666,5.415984,-0.989232,9.650599,-5.005470,4.874817,3.712447,-0.835732,-3.474039,-3.155552,7.225110,1.547302],[-6.023046,-3.013647,7.558318,-2.215515,-3.070010,-2.553580,-4.732037,4.127807,3.596354,9.453882,5.225701,0.877917,1.924284,-1.848438,-4.274997,-4.722453]],[[-7.485887,9.663612,4.470988,-7.739227,-4.213889,8.438957,-4.688402,6.152891,9.462193,7.357603,-3.771297,2.245935,-6.537069,-8.396189,4.272108,1.548523],[-9.987371,5.248679,-2.735706,3.589537,8.427042,1.849581,9.654479,4.031753,-1.217520,-2.638543,2.963412,-8.770852,1.715345,-0.033081,8.303574,-6.791401],[3.776321,2.513891,1.810365,-1.689009,3.274601,5.732561,-1.672246,-6.370596,9.409589,-4.414268,-6.868409,-0.809022,0.030760,-5.829883,-3.628520,-3.839746],[1.194841,-6.473689,-0.224885,2.440145,-5.835521,3.227752,7.646313,0.160058,-8.802291,6.678545,-8.416589,-6.924203,0.305568,-2.837261,-1.047666,5.678217],[4.263976,-5.350088,-0.713521,9.376212,-2.588248,4.598185,-5.778278,-6.439050,-3.613712,4.325989,5.293665,7.165037,2.904268,1.281621,-2.202823,9.256111],[-2.223221,-4.929605,7.763587,3.985068,-9.050559,0.140810,-9.819289,9.018196,8.725296,9.076092,-6.939136,2.010129,4.993897,4.845079,4.065644,7.971202],[9.580807,-2.729202,6.349557,-1.658050,7.676728,7.201203,-7.149647,-0.098470,7.360140,-8.382417,-2.140099,4.531443,-1.537465,-8.920878,0.016969,5.276528],[0.291507,3.952073,-3.018248,-9.775434,5.476619,4.390878,-2.670171,-1.418885,2.942528,8.309680,-0.453762,2.606774,-9.616423,8.271036,4.408668,-9.814367],[-2.418025,-3.981006,7.677585,-5.545868,-7.184162,-7.951077,-2.956735,-5.300281,-9.172844,5.085540,5.801958,7.094384,-6.433853,6.629166,-6.215880,-0.359036],[-1.338168,9.066145,8.585652,-7.901419,2.494301,-6.503167,9.608316,3.219872,4.285849,5.791166,-3.690225,-3.743968,4.065245,-4.993807,1.559660,-4.863081],[5.749623,5.157303,-8.225683,-9.354796,3.851441,8.388730,-5.976239,-4.771279,6.197507,-3.112930,-1.827600,5.495211,-8.597338,1.647440,-1.066224,1.610333]],[[6.896185,4.316444,9.480904,8.582923,-8.641123,7.870329,-2.146887,-5.928752,9.721684,6.053372,0.608844,6.793295,-3.370850,5.575424,0.929836,1.363377],[-0.789600,-8.803555,-1.855226,-1.358876,-9.692201,5.851234,5.303760,-6.022793,-3.715372,-6.392298,-0.153586,-7.170109,8.417869,-6.324693,-0.678104,4.503133],[-0.240129,-6.620352,-7.934618,0.123767,2.058957,0.188563,3.215840,0.596908,4.894963,8.992549,-7.009404,-5.817050,-1.312680,-3.135806,-3.434664,0.679828],[1.331116,-2.317591,-1.753642,-9.949142,-3.663704,-1.741525,5.501233,-7.101524,0.519284,9.268926,4.940642,4.995249,-0.555130,-8.982567,-2.106839,2.611067],[-6.410882,7.928755,6.366792,-6.327231,1.507466,1.442916,-4.088057,8.226312,-0.312169,5.882714,-5.792252,1.108005,-9.025769,-2.507110,7.093862,-3.218929],[0.350947,-5.957771,3.994822,-6.618639,2.011665,-6.748313,0.942975,9.612997,-7.626422,6.403696,-0.343101,3.115434,1.275310,8.814820,4.062863,-4.465882],[5.803505,7.623929,2.553383,6.856298,-8.261101,-5.394190,1.405536,1.258828,4.364947,-4.587686,8.950997,-0.444776,8.942954,9.145894,-3.347607,9.972506],[-2.749667,-8.514675,4.869371,-8.903452,4.201253,7.471384,-3.698843,-1.550395,-4.347816,3.690419,-0.432372,-6.844908,6.653247,-6.263710,9.475151,5.932938],[0.796579,2.673496,8.037952,-2.705671,-2.434826,4.177388,-7.289938,-0.117872,0.067095,-3.342356,-0.605463,4.332206,-4.051681,5.772806,-4.035076,1.209848],[-4.420837,-8.567954,-2.162094,7.601364,-4.924303,1.104071,-6.133070,2.483639,-7.226063,-6.933268,-5.212189,-7.292999,6.614393,-2.029445,2.353995,8.809077],[-2.266676,3.834525,-3.776600,-4.426163,-3.402132,3.384416,9.089502,-7.562312,-9.300770,-2.377403,-8.008517,5.374447,-1.697713,8.147940,5.883685,-1.156151]],[[-7.944448,-0.558258,-1.556111,-3.714368,1.673526,4.685364,-4.146208,-2.843179,-4.303244,-4.950324,7.014879,8.217672,8.925825,0.998861,8.816053,8.785874],[-0.704723,3.965371,-9.378029,3.687518,9.184463,-2.494175,-3.101992,7.126723,-6.670410,8.123519,7.274765,8.019988,-8.901215,-3.302009,-1.129337,4.641351],[2.175326,1.839041,-3.820683,9.050493,-6.786032,-4.409248,-7.005057,1.147257,0.055265,9.440843,7.264281,1.696718,3.250095,-9.457134,8.179979,-9.605830],[-3.569306,-7.941285,-7.040848,-3.760877,-2.785493,0.666099,-3.127331,2.242711,-6.415869,9.221872,2.369388,0.338454,-2.788594,3.504924,7.345386,-6.228781],[9.475609,3.588156,8.528592,-7.385224,-6.829526,-4.014576,3.143684,-2.903312,-4.931414,9.603966,-5.628910,5.730963,-8.919554,7.375800,-7.976135,2.124632],[-9.616597,-9.853932,6.881468,0.473117,-6.259613,-8.171668,8.385226,0.712128,-9.362955,-7.911164,0.732659,7.165345,-8.854133,-5.959389,9.791545,-8.645443],[-5.584958,6.605492,-0.647498,9.259538,-2.029588,-1.287962,-2.641205,-2.708223,-7.793871,2.227209,-8.216538,-5.900659,5.485905,8.188965,-8.490290,5.153944],[-4.351858,-5.825506,0.236765,-5.378563,-1.767711,-1.292978,-6.860839,8.093020,0.410343,4.683388,-8.565795,-5.809675,-4.710816,-2.778401,0.512940,2.344913],[-4.808669,-3.121621,4.109271,2.485867,0.533944,-1.513594,-1.494056,9.802488,-8.100671,2.265859,-3.276560,0.144151,-5.876409,0.675780,3.387535,3.034402],[8.754759,3.477897,-6.134446,-8.479489,-2.370855,-4.097035,-0.882907,-9.016089,-3.322704,6.319022,5.161840,9.784855,-1.331139,-8.382350,0.594532,9.719242],[8.339390,3.768081,-8.378614,-6.232713,-1.928220,1.668545,-1.237078,2.392053,-6.873232,5.702346,7.251865,2.125525,4.441810,4.540308,2.622869,1.797446]],[[-9.358913,3.027695,-8.038542,7.167454,-1.323216,-7.266007,9.361888,5.914382,-1.861199,9.740445,3.566757,-3.514654,-7.825825,9.790608,-6.014360,5.250286],[0.084196,8.530820,-1.767645,-6.402609,-4.065147,4.180350,-7.679361,5.641558,0.687528,0.403519,2.476457,4.605529,9.845877,9.368752,-1.516399,-8.729705],[6.776703,6.467620,0.769851,-6.115421,-2.102446,5.954724,-3.811783,-1.658788,0.650970,-4.547427,2.170076,0.400906,-6.888808,-1.212778,8.174498,-6.794926],[9.380515,-8.436965,0.148101,-7.752463,-9.770312,6.727540,-9.395240,-9.391425,1.328735,-1.169009,-3.848634,3.108340,-3.909949,5.336575,8.838569,7.474226],[-6.707995,4.606227,-8.796692,7.352237,4.910108,-9.756821,-0.219327,7.667829,6.375604,-1.158440,8.165938,5.877855,-9.582977,0.421801,-5.665153,-0.946075],[-5.565561,5.319720,5.385835,0.841432,2.111109,-4.599765,-9.356009,3.019259,6.299286,-6.721904,5.172641,-2.917574,-7.090866,5.180233,-4.085578,2.984121],[1.580466,-2.462819,-6.809433,1.897856,6.332922,5.678783,-5.959740,1.878427,8.525445,-6.299194,9.344891,-3.970962,7.274478,6.924049,7.458476,-1.763069],[4.325806,9.716474,4.739194,8.299364,-6.276919,-5.621187,6.106148,-3.995485,1.172514,2.390675,4.065288,8.123056,-3.426640,1.291010,6.622929,-6.538680],[-7.600231,-5.824219,8.903704,-1.806622,4.729773,-2.209742,-8.495261,8.360924,2.024488,6.305970,-7.268237,8.261261,9.163354,-2.564601,7.284478,5.745659],[-8.775888,2.191042,2.938521,3.638737,-0.983514,2.370767,-9.588888,2.816784,1.820462,-4.685557,8.107253,-7.092593,-0.704991,2.493568,-4.835908,1.429157],[1.180615,-6.328639,-2.115464,4.108639,8.738884,-3.558231,3.349282,4.495286,-2.853818,-8.777794,-9.378926,-8.948904,0.707388,-6.731216,-7.550063,-2.587886]],[[-5.666078,-0.125609,-9.901317,6.679728,-4.937056,0.946629,4.497624,-0.457760,-9.596686,6.479116,-7.592695,-8.098320,-8.335328,0.122855,-3.798695,-8.931951],[-1.326715,-7.690003,-7.009347,-4.726151,4.074017,-0.028186,-5.278939,-1.551026,4.677968,3.034947,7.752239,1.132244,-3.693888,-3.188300,-2.419577,9.784557],[6.917227,4.376876,-0.620410,-9.580405,5.379557,-5.839222,1.333178,-5.245933,3.516013,-6.636142,9.521957,-1.453293,-0.973564,7.677467,9.559715,9.944842],[-6.426831,-5.445142,-7.601302,-5.496245,3.494302,-1.791070,2.819124,3.120659,-9.480113,4.510677,9.312462,-0.931834,-4.964120,-4.112493,-5.649149,-3.095925],[-4.302777,4.382759,0.664134,-9.225464,3.685084,7.955348,9.646923,2.215088,7.103955,-0.752163,-9.706886,-8.981767,-1.584334,-2.886271,9.810867,1.613738],[2.975263,-3.708296,-8.031848,5.975832,3.338667,-9.125203,2.549472,4.052143,-7.527436,4.665837,-7.235427,8.686792,-7.361214,8.289397,-4.831682,3.752115],[-7.232480,-0.773817,-8.638060,-2.843868,-6.361521,-1.514975,-8.768263,-3.988599,6.022938,7.013440,-6.435713,-6.460687,-5.348467,-9.360510,-9.106860,-0.402945],[0.135914,7.325552,-6.209231,-3.281293,-4.627771,-9.036655,-4.180918,1.200867,-4.788937,2.370823,4.749373,6.565529,2.786785,-5.672960,0.363314,-0.809717],[0.862838,-1.961841,0.315348,4.423019,9.227686,-5.334320,-2.267321,-4.886189,-6.527430,7.926569,1.821089,9.349717,-5.285340,2.182705,-8.532536,5.347714],[9.281756,1.428023,-0.475100,6.128921,-5.237002,7.560556,4.060655,4.899183,9.299884,-8.968186,7.531718,5.963182,3.792034,1.357365,3.948200,-9.519843],[-6.525476,3.894027,-3.548282,1.625202,5.022899,8.928195,-5.317489,-7.574782,-1.326820,-1.341729,8.214761,1.118909,-5.159318,-9.350422,7.890654,1.656361]],[[9.649713,-5.486778,2.077572,-0.667986,-4.517863,4.608792,5.779178,-8.419850,-6.601174,7.400086,8.528533,1.020638,-9.469711,0.910807,-8.725465,1.230033],[6.067822,3.920416,1.326783,1.144290,5.773073,-4.617764,7.240313,-5.761271,-1.777798,4.240149,9.734066,2.442869,-6.605194,2.163507,3.263499,-3.150173],[9.358051,6.594190,-1.469226,-7.036907,-3.099887,-0.731655,-4.782723,9.531375,-1.466354,-4.639664,5.387134,1.971964,-6.286009,-2.123073,-5.980818,-6.802234],[-8.482282,-9.655927,6.802508,6.033369,-0.631065,7.932336,-4.211989,3.189425,9.609710,-0.983954,4.449832,-6.123336,0.866261,-5.053264,-4.085076,4.134226],[-3.982578,9.425332,-9.591631,0.899703,-4.812116,8.015354,-3.309303,7.458626,-6.648512,-8.419571,-2.171107,6.606041,-7.062826,5.962889,6.655942,2.176639],[-8.763781,8.688249,8.356885,8.376469,2.027730,6.067012,7.049748,5.120551,-3.728640,-2.012132,-2.444730,-6.560895,3.165279,6.806924,-6.535849,-8.248993],[8.719896,-7.537308,7.039803,-3.094436,-3.210519,-3.050295,9.167278,-4.168186,7.184300,-0.946557,-6.270887,-6.451464,-2.764191,-2.091525,4.166857,7.792092],[-6.396451,5.120737,-7.142459,-4.994401,7.834697,-7.533389,-2.766510,4.405134,9.960592,-2.262398,-6.247246,4.654825,-6.473194,-2.113173,7.160287,8.110945],[4.586542,1.656233,-6.894052,-4.124620,-1.367472,-0.922829,4.678345,-9.662978,1.478068,2.262776,-7.647838,-5.519618,-1.635919,-0.062447,6.782161,-3.602550],[-7.149117,-0.789448,9.899349,3.505954,4.607474,9.281441,7.320278,-7.232199,-4.694154,-8.330491,-8.470583,6.179135,4.246620,-9.332936,8.277783,4.121780],[-3.099916,7.857028,4.197186,9.468345,-0.891116,0.590957,4.194347,3.450386,4.717774,-5.266913,-7.644318,2.104199,4.999096,-0.893322,-4.053033,-0.327659]],[[0.287791,-2.831306,-2.011616,-7.577965,-6.996192,-5.734266,4.866787,1.816840,-4.451275,-7.748928,-9.530230,-8.057992,-2.984390,-0.506574,5.534250,9.051372],[-4.528844,7.517993,-1.729092,-0.412335,4.579963,-4.507576,-7.088800,-2.584433,7.521352,2.447648,-6.537633,6.987938,1.634288,8.996315,-3.615878,1.185171],[-8.727119,-2.805571,-0.195942,-8.330415,4.550222,-1.900182,-5.790770,-8.229596,-8.309301,5.633226,-1.048619,5.225728,7.338386,-8.143407,8.853818,-6.470682],[-7.362955,-8.335847,8.254757,-6.371321,8.816221,-4.056166,3.750192,2.704537,2.937892,-1.976488,2.703524,2.234788,-4.721489,2.061785,0.251075,-4.551061],[-4.092980,5.287270,0.187537,-9.684202,-4.718319,-3.747224,-6.673567,4.995517,8.678537,8.686087,1.411049,5.007235,-7.754370,-0.593533,-0.938507,6.216990],[9.006422,5.483103,-8.567103,-7.566273,-2.782961,0.784867,-6.313101,-1.421384,-4.777286,7.789092,-3.519148,-8.188924,5.996235,4.630324,3.485636,-1.686165],[6.873968,1.313571,9.644340,-5.426099,-9.210759,-2.264417,5.637509,-4.127116,-6.250407,3.903508,-6.809856,0.939712,-1.109939,-6.258532,4.835563,0.101708],[-2.379829,8.600233,-8.020850,4.696409,4.339094,1.994597,0.706552,-6.042804,0.765260,-7.380998,2.619930,9.447636,-5.105639,7.448079,-6.285609,-9.186356],[9.938131,2.233784,-2.165396,2.174011,-5.949520,-7.843919,-3.327321,-7.739736,-2.837643,-6.639033,-8.510392,-3.646978,9.860296,2.769571,-4.979639,-0.843105],[7.605972,2.532544,-2.741551,3.643311,8.745256,-5.046462,-0.936654,-4.424242,-3.244912,0.339473,-0.933339,6.045504,3.172179,-6.109030,3.499952,-6.433108],[-1.653128,-7.595254,-5.200770,9.912261,6.266227,0.019392,-5.475298,-8.585360,-5.927844,-2.522247,5.297874,-1.993351,-9.165342,-8.610744,2.022463,-1.843151]]], dtype = "float64")#candidate|9849|(15, 11, 16)|const|float64
bop_9850 = relay.subtract(call_9839.astype('int64'), const_9849.astype('int64')) # shape=(15, 11, 16)
bop_9853 = relay.subtract(call_9840.astype('int64'), const_9849.astype('int64')) # shape=(15, 11, 16)
output = relay.Tuple([call_9844,var_9845,bop_9850,])
output2 = relay.Tuple([call_9846,var_9845,bop_9853,])
F = relay.Function([var_9845,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9845,], output2)
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
	relay.transform.InferType(),
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
