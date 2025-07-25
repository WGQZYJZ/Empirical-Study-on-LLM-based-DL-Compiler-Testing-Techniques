import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_161 = relay.var("var_161", dtype = "uint8", shape = (8, 14, 5))#candidate|161|(8, 14, 5)|var|uint8
var_162 = relay.var("var_162", dtype = "uint8", shape = (8, 14, 5))#candidate|162|(8, 14, 5)|var|uint8
bop_163 = relay.less_equal(var_161.astype('bool'), relay.reshape(var_162.astype('bool'), relay.shape_of(var_161))) # shape=(8, 14, 5)
output = relay.Tuple([bop_163,])
output2 = relay.Tuple([bop_163,])
func_172 = relay.Function([var_161,var_162,], output)
mod['func_172'] = func_172
mod = relay.transform.InferType()(mod)
mutated_mod['func_172'] = func_172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_172_call = mutated_mod.get_global_var('func_172')
var_174 = relay.var("var_174", dtype = "uint8", shape = (8, 14, 5))#candidate|174|(8, 14, 5)|var|uint8
var_175 = relay.var("var_175", dtype = "uint8", shape = (8, 14, 5))#candidate|175|(8, 14, 5)|var|uint8
call_173 = func_172_call(var_174,var_175,)
output = call_173
func_176 = relay.Function([var_174,var_175,], output)
mutated_mod['func_176'] = func_176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_457 = relay.var("var_457", dtype = "float32", shape = (1, 12, 12))#candidate|457|(1, 12, 12)|var|float32
uop_458 = relay.sinh(var_457.astype('float32')) # shape=(1, 12, 12)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
var_463 = relay.var("var_463", dtype = "uint8", shape = (560,))#candidate|463|(560,)|var|uint8
call_462 = relay.TupleGetItem(func_172_call(relay.reshape(var_463.astype('uint8'), [8, 14, 5]), relay.reshape(var_463.astype('uint8'), [8, 14, 5]), ), 0)
call_464 = relay.TupleGetItem(func_176_call(relay.reshape(var_463.astype('uint8'), [8, 14, 5]), relay.reshape(var_463.astype('uint8'), [8, 14, 5]), ), 0)
output = relay.Tuple([uop_458,call_462,var_463,])
output2 = relay.Tuple([uop_458,call_464,var_463,])
func_477 = relay.Function([var_457,var_463,], output)
mod['func_477'] = func_477
mod = relay.transform.InferType()(mod)
mutated_mod['func_477'] = func_477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_477_call = mutated_mod.get_global_var('func_477')
var_479 = relay.var("var_479", dtype = "float32", shape = (1, 12, 12))#candidate|479|(1, 12, 12)|var|float32
var_480 = relay.var("var_480", dtype = "uint8", shape = (560,))#candidate|480|(560,)|var|uint8
call_478 = func_477_call(var_479,var_480,)
output = call_478
func_481 = relay.Function([var_479,var_480,], output)
mutated_mod['func_481'] = func_481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_980 = relay.var("var_980", dtype = "uint64", shape = (16, 11, 4))#candidate|980|(16, 11, 4)|var|uint64
var_981 = relay.var("var_981", dtype = "uint64", shape = (16, 11, 4))#candidate|981|(16, 11, 4)|var|uint64
bop_982 = relay.maximum(var_980.astype('uint64'), relay.reshape(var_981.astype('uint64'), relay.shape_of(var_980))) # shape=(16, 11, 4)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
var_987 = relay.var("var_987", dtype = "uint8", shape = (560,))#candidate|987|(560,)|var|uint8
call_986 = relay.TupleGetItem(func_172_call(relay.reshape(var_987.astype('uint8'), [8, 14, 5]), relay.reshape(var_987.astype('uint8'), [8, 14, 5]), ), 0)
call_988 = relay.TupleGetItem(func_176_call(relay.reshape(var_987.astype('uint8'), [8, 14, 5]), relay.reshape(var_987.astype('uint8'), [8, 14, 5]), ), 0)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
call_992 = relay.TupleGetItem(func_172_call(relay.reshape(call_986.astype('uint8'), [8, 14, 5]), relay.reshape(call_986.astype('uint8'), [8, 14, 5]), ), 0)
call_993 = relay.TupleGetItem(func_176_call(relay.reshape(call_986.astype('uint8'), [8, 14, 5]), relay.reshape(call_986.astype('uint8'), [8, 14, 5]), ), 0)
func_477_call = mod.get_global_var('func_477')
func_481_call = mutated_mod.get_global_var('func_481')
const_1000 = relay.const([1.490448,-1.359387,-1.437539,-6.559387,-8.460796,9.255764,-6.295764,-0.605582,6.024928,7.938023,-4.398678,4.041101,-9.555277,-7.519966,-9.240623,-8.807713,5.323936,8.685414,-9.980960,-8.450571,9.094939,6.149695,-5.009108,9.858286,-3.201306,-4.663439,3.820844,6.892872,6.388630,2.731670,-0.823902,9.168497,4.494343,0.900401,-3.583003,-5.503613,9.976438,-3.214136,6.980422,-6.187935,-3.017187,5.148548,-2.352411,-6.014377,-5.982695,1.933196,5.875410,-2.546588,-7.130712,-7.336073,8.239586,-3.013527,-6.581653,-7.893817,2.174251,9.395915,-8.115962,9.863978,5.716601,-1.135275,-0.461456,7.356967,-5.920449,-2.563962,9.941591,8.231686,2.718648,-8.644515,-2.517671,1.382104,4.853079,-2.178455,9.278788,-6.531027,1.865513,-5.907336,-7.061141,4.199179,1.068064,1.992039,-4.556907,-4.954216,0.568753,0.952412,6.419695,6.235423,-7.898774,-6.211012,5.508465,-4.208100,6.943773,-4.530983,-7.642543,-2.051378,6.615928,8.883006,1.705426,9.226463,-9.402552,-3.801861,-4.465307,-3.883371,5.493411,-8.558157,6.141901,3.594991,-4.741937,-4.593875,8.711385,-9.407803,2.416237,-6.181345,9.788788,4.340141,5.095817,-5.364159,6.784539,-4.478880,3.708583,4.849509,3.265309,-4.770131,3.019911,2.230799,5.184826,7.002437,9.724002,0.410960,-7.677268,-2.358677,1.409868,6.200594,5.362301,6.132397,-5.049306,2.485935,-7.497951,2.975783,-3.743831,-9.516328,0.698741,-5.425793,-5.422995,6.805727], dtype = "float32")#candidate|1000|(144,)|const|float32
call_999 = relay.TupleGetItem(func_477_call(relay.reshape(const_1000.astype('float32'), [1, 12, 12]), relay.reshape(call_992.astype('uint8'), [560,]), ), 2)
call_1001 = relay.TupleGetItem(func_481_call(relay.reshape(const_1000.astype('float32'), [1, 12, 12]), relay.reshape(call_992.astype('uint8'), [560,]), ), 2)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
call_1004 = relay.TupleGetItem(func_172_call(relay.reshape(call_986.astype('uint8'), [8, 14, 5]), relay.reshape(var_987.astype('uint8'), [8, 14, 5]), ), 0)
call_1005 = relay.TupleGetItem(func_176_call(relay.reshape(call_986.astype('uint8'), [8, 14, 5]), relay.reshape(var_987.astype('uint8'), [8, 14, 5]), ), 0)
bop_1017 = relay.logical_xor(call_1004.astype('uint16'), relay.reshape(call_992.astype('uint16'), relay.shape_of(call_1004))) # shape=(8, 14, 5)
bop_1020 = relay.logical_xor(call_1005.astype('uint16'), relay.reshape(call_993.astype('uint16'), relay.shape_of(call_1005))) # shape=(8, 14, 5)
func_477_call = mod.get_global_var('func_477')
func_481_call = mutated_mod.get_global_var('func_481')
call_1026 = relay.TupleGetItem(func_477_call(relay.reshape(const_1000.astype('float32'), [1, 12, 12]), relay.reshape(call_999.astype('uint8'), [560,]), ), 1)
call_1027 = relay.TupleGetItem(func_481_call(relay.reshape(const_1000.astype('float32'), [1, 12, 12]), relay.reshape(call_999.astype('uint8'), [560,]), ), 1)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
call_1032 = relay.TupleGetItem(func_172_call(relay.reshape(call_1026.astype('uint8'), [8, 14, 5]), relay.reshape(call_992.astype('uint8'), [8, 14, 5]), ), 0)
call_1033 = relay.TupleGetItem(func_176_call(relay.reshape(call_1026.astype('uint8'), [8, 14, 5]), relay.reshape(call_992.astype('uint8'), [8, 14, 5]), ), 0)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
call_1038 = relay.TupleGetItem(func_172_call(relay.reshape(call_992.astype('uint8'), [8, 14, 5]), relay.reshape(bop_1017.astype('uint8'), [8, 14, 5]), ), 0)
call_1039 = relay.TupleGetItem(func_176_call(relay.reshape(call_992.astype('uint8'), [8, 14, 5]), relay.reshape(bop_1017.astype('uint8'), [8, 14, 5]), ), 0)
output = relay.Tuple([bop_982,call_986,var_987,call_999,const_1000,bop_1017,call_1026,call_1032,call_1038,])
output2 = relay.Tuple([bop_982,call_988,var_987,call_1001,const_1000,bop_1020,call_1027,call_1033,call_1039,])
func_1041 = relay.Function([var_980,var_981,var_987,], output)
mod['func_1041'] = func_1041
mod = relay.transform.InferType()(mod)
mutated_mod['func_1041'] = func_1041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1041_call = mutated_mod.get_global_var('func_1041')
var_1043 = relay.var("var_1043", dtype = "uint64", shape = (16, 11, 4))#candidate|1043|(16, 11, 4)|var|uint64
var_1044 = relay.var("var_1044", dtype = "uint64", shape = (16, 11, 4))#candidate|1044|(16, 11, 4)|var|uint64
var_1045 = relay.var("var_1045", dtype = "uint8", shape = (560,))#candidate|1045|(560,)|var|uint8
call_1042 = func_1041_call(var_1043,var_1044,var_1045,)
output = call_1042
func_1046 = relay.Function([var_1043,var_1044,var_1045,], output)
mutated_mod['func_1046'] = func_1046
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1192 = relay.const([[[3.756073,9.138688]],[[-3.988950,-7.976936]],[[-6.961621,9.841527]]], dtype = "float32")#candidate|1192|(3, 1, 2)|const|float32
uop_1193 = relay.exp(const_1192.astype('float32')) # shape=(3, 1, 2)
bop_1204 = relay.equal(uop_1193.astype('bool'), relay.reshape(const_1192.astype('bool'), relay.shape_of(uop_1193))) # shape=(3, 1, 2)
uop_1213 = relay.cos(bop_1204.astype('float64')) # shape=(3, 1, 2)
output = relay.Tuple([uop_1213,])
output2 = relay.Tuple([uop_1213,])
func_1215 = relay.Function([], output)
mod['func_1215'] = func_1215
mod = relay.transform.InferType()(mod)
mutated_mod['func_1215'] = func_1215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mutated_mod.get_global_var('func_1215')
call_1216 = func_1215_call()
output = call_1216
func_1217 = relay.Function([], output)
mutated_mod['func_1217'] = func_1217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_1245 = relay.TupleGetItem(func_1215_call(), 0)
call_1246 = relay.TupleGetItem(func_1217_call(), 0)
var_1255 = relay.var("var_1255", dtype = "float64", shape = (3, 11, 2))#candidate|1255|(3, 11, 2)|var|float64
bop_1256 = relay.add(call_1245.astype('uint32'), var_1255.astype('uint32')) # shape=(3, 11, 2)
bop_1259 = relay.add(call_1246.astype('uint32'), var_1255.astype('uint32')) # shape=(3, 11, 2)
const_1270 = relay.const([[[-7.250116,2.606380],[-5.387186,3.932599],[-7.479050,-2.270735]],[[7.491026,7.738806],[9.489365,6.511336],[3.631293,3.461814]],[[-0.281694,4.902833],[-2.940122,5.665877],[5.009678,0.445026]]], dtype = "float64")#candidate|1270|(3, 3, 2)|const|float64
bop_1271 = relay.less(call_1245.astype('bool'), const_1270.astype('bool')) # shape=(3, 3, 2)
bop_1274 = relay.less(call_1246.astype('bool'), const_1270.astype('bool')) # shape=(3, 3, 2)
output = relay.Tuple([bop_1256,bop_1271,])
output2 = relay.Tuple([bop_1259,bop_1274,])
func_1284 = relay.Function([var_1255,], output)
mod['func_1284'] = func_1284
mod = relay.transform.InferType()(mod)
mutated_mod['func_1284'] = func_1284
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1285 = relay.var("var_1285", dtype = "float64", shape = (3, 11, 2))#candidate|1285|(3, 11, 2)|var|float64
func_1284_call = mutated_mod.get_global_var('func_1284')
call_1286 = func_1284_call(var_1285)
output = call_1286
func_1287 = relay.Function([var_1285], output)
mutated_mod['func_1287'] = func_1287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_1294 = relay.TupleGetItem(func_1215_call(), 0)
call_1295 = relay.TupleGetItem(func_1217_call(), 0)
output = call_1294
output2 = call_1295
func_1299 = relay.Function([], output)
mod['func_1299'] = func_1299
mod = relay.transform.InferType()(mod)
mutated_mod['func_1299'] = func_1299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mutated_mod.get_global_var('func_1299')
call_1300 = func_1299_call()
output = call_1300
func_1301 = relay.Function([], output)
mutated_mod['func_1301'] = func_1301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_1324 = relay.TupleGetItem(func_1215_call(), 0)
call_1325 = relay.TupleGetItem(func_1217_call(), 0)
output = relay.Tuple([call_1324,])
output2 = relay.Tuple([call_1325,])
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
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_1330 = func_1299_call()
call_1331 = func_1299_call()
output = relay.Tuple([call_1330,])
output2 = relay.Tuple([call_1331,])
func_1333 = relay.Function([], output)
mod['func_1333'] = func_1333
mod = relay.transform.InferType()(mod)
output = func_1333()
func_1334 = relay.Function([], output)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1333_call = mod.get_global_var('func_1333')
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1373 = relay.TupleGetItem(func_1333_call(), 0)
call_1374 = relay.TupleGetItem(func_1334_call(), 0)
var_1394 = relay.var("var_1394", dtype = "float64", shape = (3, 10, 2))#candidate|1394|(3, 10, 2)|var|float64
bop_1395 = relay.less_equal(call_1373.astype('bool'), var_1394.astype('bool')) # shape=(3, 10, 2)
bop_1398 = relay.less_equal(call_1374.astype('bool'), var_1394.astype('bool')) # shape=(3, 10, 2)
func_477_call = mod.get_global_var('func_477')
func_481_call = mutated_mod.get_global_var('func_481')
var_1409 = relay.var("var_1409", dtype = "float32", shape = (1, 144))#candidate|1409|(1, 144)|var|float32
var_1410 = relay.var("var_1410", dtype = "uint8", shape = (560,))#candidate|1410|(560,)|var|uint8
call_1408 = relay.TupleGetItem(func_477_call(relay.reshape(var_1409.astype('float32'), [1, 12, 12]), relay.reshape(var_1410.astype('uint8'), [560,]), ), 0)
call_1411 = relay.TupleGetItem(func_481_call(relay.reshape(var_1409.astype('float32'), [1, 12, 12]), relay.reshape(var_1410.astype('uint8'), [560,]), ), 0)
bop_1420 = relay.less_equal(var_1409.astype('bool'), relay.reshape(call_1408.astype('bool'), relay.shape_of(var_1409))) # shape=(1, 144)
bop_1423 = relay.less_equal(var_1409.astype('bool'), relay.reshape(call_1411.astype('bool'), relay.shape_of(var_1409))) # shape=(1, 144)
uop_1431 = relay.asinh(bop_1420.astype('float32')) # shape=(1, 144)
uop_1433 = relay.asinh(bop_1423.astype('float32')) # shape=(1, 144)
output = relay.Tuple([bop_1395,var_1410,uop_1431,])
output2 = relay.Tuple([bop_1398,var_1410,uop_1433,])
func_1438 = relay.Function([var_1394,var_1409,var_1410,], output)
mod['func_1438'] = func_1438
mod = relay.transform.InferType()(mod)
mutated_mod['func_1438'] = func_1438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1438_call = mutated_mod.get_global_var('func_1438')
var_1440 = relay.var("var_1440", dtype = "float64", shape = (3, 10, 2))#candidate|1440|(3, 10, 2)|var|float64
var_1441 = relay.var("var_1441", dtype = "float32", shape = (1, 144))#candidate|1441|(1, 144)|var|float32
var_1442 = relay.var("var_1442", dtype = "uint8", shape = (560,))#candidate|1442|(560,)|var|uint8
call_1439 = func_1438_call(var_1440,var_1441,var_1442,)
output = call_1439
func_1443 = relay.Function([var_1440,var_1441,var_1442,], output)
mutated_mod['func_1443'] = func_1443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_1525 = relay.TupleGetItem(func_1215_call(), 0)
call_1526 = relay.TupleGetItem(func_1217_call(), 0)
func_1284_call = mod.get_global_var('func_1284')
func_1287_call = mutated_mod.get_global_var('func_1287')
const_1528 = relay.const([7.841860,-3.445225,4.302731,-7.160134,9.637383,8.255745,3.997800,-3.546644,8.973454,-2.354788,1.929903,-2.327754,5.246347,8.860842,-5.250971,-2.647618,-4.169793,2.500118,5.300921,5.111648,6.804080,5.965621,-9.280455,-9.964669,-7.933164,-1.677400,9.210577,4.639732,7.271131,9.391492,7.057242,5.123985,-7.163060,-5.582515,3.460254,-7.409545,-5.138148,3.372779,5.875987,-5.288674,-0.880815,8.517977,9.138117,-5.924506,9.165862,-4.554012,9.688186,-2.533157,6.809027,3.585959,-4.416637,0.651787,-7.831450,2.953899,8.826113,8.955384,-2.382022,8.060024,3.484194,4.267062,9.617599,7.680905,8.447039,-1.862334,-8.746658,7.537616], dtype = "float64")#candidate|1528|(66,)|const|float64
call_1527 = relay.TupleGetItem(func_1284_call(relay.reshape(const_1528.astype('float64'), [3, 11, 2])), 1)
call_1529 = relay.TupleGetItem(func_1287_call(relay.reshape(const_1528.astype('float64'), [3, 11, 2])), 1)
output = relay.Tuple([call_1525,call_1527,const_1528,])
output2 = relay.Tuple([call_1526,call_1529,const_1528,])
func_1536 = relay.Function([], output)
mod['func_1536'] = func_1536
mod = relay.transform.InferType()(mod)
output = func_1536()
func_1537 = relay.Function([], output)
mutated_mod['func_1537'] = func_1537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_1538 = relay.TupleGetItem(func_1327_call(), 0)
call_1539 = relay.TupleGetItem(func_1329_call(), 0)
var_1547 = relay.var("var_1547", dtype = "float64", shape = (3, 15, 2))#candidate|1547|(3, 15, 2)|var|float64
bop_1548 = relay.add(call_1538.astype('uint32'), var_1547.astype('uint32')) # shape=(3, 15, 2)
bop_1551 = relay.add(call_1539.astype('uint32'), var_1547.astype('uint32')) # shape=(3, 15, 2)
var_1554 = relay.var("var_1554", dtype = "float64", shape = (3, 15, 2))#candidate|1554|(3, 15, 2)|var|float64
bop_1555 = relay.power(var_1547.astype('float32'), relay.reshape(var_1554.astype('float32'), relay.shape_of(var_1547))) # shape=(3, 15, 2)
func_1438_call = mod.get_global_var('func_1438')
func_1443_call = mutated_mod.get_global_var('func_1443')
var_1568 = relay.var("var_1568", dtype = "float64", shape = (1, 60))#candidate|1568|(1, 60)|var|float64
var_1569 = relay.var("var_1569", dtype = "float32", shape = (144,))#candidate|1569|(144,)|var|float32
const_1570 = relay.const([[-5,1,-1,-3,-6,-2,8,-9,-5,-7,5,-1,10,1,-1,-5,-4,-8,-3,10,2,4,-9,7,7,5,1,6,-10,-7,-1,-1,-9,2,2,1,-5,-5,9,8,-7,-9,-1,-10,-1,-5,-9,9,-5,-10,-2,2,10,-2,9,-5,5,7,-9,10,-3,-4,3,-10,2,-7,5,-2,7,1,7,4,-10,-9,-5,-2,-6,-1,-10,7,-3,8,4,-10,-5,-6,-7,-4,9,-9,-4,5,5,-9,6,-7,-2,6,7,6,-9,4,-3,4,-4,8,-3,-10,-8,-3,6,-5,7,4,-9,5,3,5,-10,9,1,-3,-2,-5,3,9,10,-6,7,-10,-10,-6,4,8,10,9,-7,-8,-7,-1,10,8,6,-6,5,1,9,-6,-9,-9,4,-10,10,1,-10,-10,4,10,-3,5,10,-1,3,4,-4,1,-8,-10,-1,-10,5,3,7,1,2,7,-2,-3,-8,9,9,-3,-2,-7,-3,-8,-6,-10,-6,2,5,-10,-8,5,9,1,3,4,6,-2,10,-9,-1,-7,8,-3,-9,-1,5,6,-10,-1,-10,2,-8,-6,2,-5,2,10,-3,2,-5,2,1,-3,4,5,8,-3,2,7,3,-7,-5,-5,-9,2,-4,-5,2,-5,3,-4,9,-9,5,3,7,-4,-8,-1,-10,4,-7,8,-6,-8,4,1,-9,2,-6,3,8,6,-8,4,1,-1,-6,2,1,2,1,-9,-2,4,8,1,-7,-4,7,-3,6,9,-1,6,10,-7,9,-1,9,-1,5,2,1,6,-4,8,-3,1,-9,-7,-5,10,-2,-9,8,-7,3,4,-7,-4,1,2,9,7,-10,-5,-1,-3,7,4,-1,10,-4,8,7,2,-1,2,-8,6,-5,7,9,9,-9,3,7,1,-10,-3,-10,4,9,-1,-7,9,9,10,-3,6,-3,1,4,1,1,-2,-1,2,6,-1,10,7,-3,9,-5,9,6,9,-1,6,6,-3,-6,-9,8,-5,7,8,-6,-7,4,10,5,9,-4,8,-3,-9,5,9,-7,2,6,-7,8,5,1,1,-7,-1,-3,2,-9,-5,8,-8,8,-2,-1,-7,4,-3,9,2,2,6,-2,3,9,10,4,6,-9,6,-7,8,-7,8,-5,-2,4,4,6,1,-7,-5,-8,-3,-9,-6,-6,-10,7,10,8,9,-10,10,-4,5,10,2,-3,7,-8,2,9,-6,2,8,-8,2,2,7,-2,9,4,-2,-8,1,-1,-9,-5,-7,-1,-6,2,10,-1,9,-9,5,-10,2,-5,-6,-6,-7,10,-7,-8,1,-3,3,-7,-5,-3,-2,9,-2,7,-1,1,-3,3,-1,4,-1,2,-9,8,-5,-6,3,1,10,-3,2,-2,-6,-6,5,10,7,10,9,3,9,3,5,-9,-5,-9,-8,-3,-5,3,10,-6,3,4,3,10,-7,6,-8,-10,-7,9,1,10,-10,3,-6,9,-4]], dtype = "uint8")#candidate|1570|(1, 560)|const|uint8
call_1567 = relay.TupleGetItem(func_1438_call(relay.reshape(var_1568.astype('float64'), [3, 10, 2]), relay.reshape(var_1569.astype('float32'), [1, 144]), relay.reshape(const_1570.astype('uint8'), [560,]), ), 2)
call_1571 = relay.TupleGetItem(func_1443_call(relay.reshape(var_1568.astype('float64'), [3, 10, 2]), relay.reshape(var_1569.astype('float32'), [1, 144]), relay.reshape(const_1570.astype('uint8'), [560,]), ), 2)
func_1438_call = mod.get_global_var('func_1438')
func_1443_call = mutated_mod.get_global_var('func_1443')
call_1572 = relay.TupleGetItem(func_1438_call(relay.reshape(var_1568.astype('float64'), [3, 10, 2]), relay.reshape(var_1569.astype('float32'), [1, 144]), relay.reshape(const_1570.astype('uint8'), [560,]), ), 2)
call_1573 = relay.TupleGetItem(func_1443_call(relay.reshape(var_1568.astype('float64'), [3, 10, 2]), relay.reshape(var_1569.astype('float32'), [1, 144]), relay.reshape(const_1570.astype('uint8'), [560,]), ), 2)
output = relay.Tuple([bop_1548,bop_1555,call_1567,var_1568,var_1569,const_1570,call_1572,])
output2 = relay.Tuple([bop_1551,bop_1555,call_1571,var_1568,var_1569,const_1570,call_1573,])
func_1574 = relay.Function([var_1547,var_1554,var_1568,var_1569,], output)
mod['func_1574'] = func_1574
mod = relay.transform.InferType()(mod)
var_1575 = relay.var("var_1575", dtype = "float64", shape = (3, 15, 2))#candidate|1575|(3, 15, 2)|var|float64
var_1576 = relay.var("var_1576", dtype = "float64", shape = (3, 15, 2))#candidate|1576|(3, 15, 2)|var|float64
var_1577 = relay.var("var_1577", dtype = "float64", shape = (1, 60))#candidate|1577|(1, 60)|var|float64
var_1578 = relay.var("var_1578", dtype = "float32", shape = (144,))#candidate|1578|(144,)|var|float32
output = func_1574(var_1575,var_1576,var_1577,var_1578,)
func_1579 = relay.Function([var_1575,var_1576,var_1577,var_1578,], output)
mutated_mod['func_1579'] = func_1579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1333_call = mod.get_global_var('func_1333')
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1599 = relay.TupleGetItem(func_1333_call(), 0)
call_1600 = relay.TupleGetItem(func_1334_call(), 0)
uop_1605 = relay.log10(call_1599.astype('float64')) # shape=(3, 1, 2)
uop_1607 = relay.log10(call_1600.astype('float64')) # shape=(3, 1, 2)
output = relay.Tuple([uop_1605,])
output2 = relay.Tuple([uop_1607,])
func_1609 = relay.Function([], output)
mod['func_1609'] = func_1609
mod = relay.transform.InferType()(mod)
mutated_mod['func_1609'] = func_1609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mutated_mod.get_global_var('func_1609')
call_1610 = func_1609_call()
output = call_1610
func_1611 = relay.Function([], output)
mutated_mod['func_1611'] = func_1611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_1612 = relay.TupleGetItem(func_1609_call(), 0)
call_1613 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([call_1612,])
output2 = relay.Tuple([call_1613,])
func_1627 = relay.Function([], output)
mod['func_1627'] = func_1627
mod = relay.transform.InferType()(mod)
mutated_mod['func_1627'] = func_1627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1627_call = mutated_mod.get_global_var('func_1627')
call_1628 = func_1627_call()
output = call_1628
func_1629 = relay.Function([], output)
mutated_mod['func_1629'] = func_1629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1333_call = mod.get_global_var('func_1333')
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1643 = relay.TupleGetItem(func_1333_call(), 0)
call_1644 = relay.TupleGetItem(func_1334_call(), 0)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_1645 = relay.TupleGetItem(func_1215_call(), 0)
call_1646 = relay.TupleGetItem(func_1217_call(), 0)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_1659 = func_1299_call()
call_1660 = func_1299_call()
bop_1677 = relay.greater_equal(call_1659.astype('bool'), relay.reshape(call_1643.astype('bool'), relay.shape_of(call_1659))) # shape=(3, 1, 2)
bop_1680 = relay.greater_equal(call_1660.astype('bool'), relay.reshape(call_1644.astype('bool'), relay.shape_of(call_1660))) # shape=(3, 1, 2)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
var_1682 = relay.var("var_1682", dtype = "uint8", shape = (560,))#candidate|1682|(560,)|var|uint8
call_1681 = relay.TupleGetItem(func_172_call(relay.reshape(var_1682.astype('uint8'), [8, 14, 5]), relay.reshape(var_1682.astype('uint8'), [8, 14, 5]), ), 0)
call_1683 = relay.TupleGetItem(func_176_call(relay.reshape(var_1682.astype('uint8'), [8, 14, 5]), relay.reshape(var_1682.astype('uint8'), [8, 14, 5]), ), 0)
output = relay.Tuple([call_1645,bop_1677,call_1681,var_1682,])
output2 = relay.Tuple([call_1646,bop_1680,call_1683,var_1682,])
func_1686 = relay.Function([var_1682,], output)
mod['func_1686'] = func_1686
mod = relay.transform.InferType()(mod)
mutated_mod['func_1686'] = func_1686
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1687 = relay.var("var_1687", dtype = "uint8", shape = (560,))#candidate|1687|(560,)|var|uint8
func_1686_call = mutated_mod.get_global_var('func_1686')
call_1688 = func_1686_call(var_1687)
output = call_1688
func_1689 = relay.Function([var_1687], output)
mutated_mod['func_1689'] = func_1689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_1691 = func_1299_call()
call_1692 = func_1299_call()
output = call_1691
output2 = call_1692
func_1694 = relay.Function([], output)
mod['func_1694'] = func_1694
mod = relay.transform.InferType()(mod)
output = func_1694()
func_1695 = relay.Function([], output)
mutated_mod['func_1695'] = func_1695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_1699 = relay.TupleGetItem(func_1536_call(), 2)
call_1700 = relay.TupleGetItem(func_1537_call(), 2)
output = call_1699
output2 = call_1700
func_1704 = relay.Function([], output)
mod['func_1704'] = func_1704
mod = relay.transform.InferType()(mod)
output = func_1704()
func_1705 = relay.Function([], output)
mutated_mod['func_1705'] = func_1705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1333_call = mod.get_global_var('func_1333')
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1758 = relay.TupleGetItem(func_1333_call(), 0)
call_1759 = relay.TupleGetItem(func_1334_call(), 0)
func_1438_call = mod.get_global_var('func_1438')
func_1443_call = mutated_mod.get_global_var('func_1443')
var_1768 = relay.var("var_1768", dtype = "float64", shape = (60,))#candidate|1768|(60,)|var|float64
var_1769 = relay.var("var_1769", dtype = "float32", shape = (144,))#candidate|1769|(144,)|var|float32
const_1770 = relay.const([[-1,8],[-8,-7],[-4,10],[-10,-5],[-10,4],[-9,-8],[5,7],[7,9],[-8,1],[-1,6],[3,-1],[9,-3],[-9,1],[-3,6],[2,-7],[9,-6],[-2,10],[-7,-9],[2,-5],[-7,2],[-7,-5],[1,-6],[7,3],[-9,10],[9,-7],[6,-9],[5,1],[-4,2],[-5,4],[10,-10],[-5,-10],[5,-8],[-10,1],[8,-4],[5,8],[8,3],[-7,-1],[8,4],[6,8],[4,6],[-10,9],[8,-2],[1,-4],[-10,-4],[5,5],[-7,-7],[-5,-6],[2,2],[-10,7],[-6,-3],[-10,10],[4,-8],[1,4],[-2,-3],[-5,-5],[-1,-8],[-10,9],[5,7],[-8,7],[10,3],[-9,-1],[8,-10],[-5,2],[4,8],[-5,3],[8,-7],[-6,-8],[-8,-10],[-8,9],[-7,10],[4,7],[-10,-1],[2,4],[4,6],[-6,6],[7,-10],[-7,2],[-8,3],[4,7],[4,10],[-3,-6],[8,5],[-8,7],[-7,4],[-5,-5],[1,-4],[-7,-9],[-2,9],[-5,-10],[-8,-4],[-6,-4],[7,-6],[-4,-7],[8,-10],[-4,-7],[7,-2],[10,-3],[9,-5],[-8,7],[-6,-10],[-3,-5],[-10,-7],[3,-1],[-2,3],[4,-2],[-5,9],[5,1],[-10,-2],[-9,3],[2,-4],[-6,5],[7,-9],[6,-6],[-8,8],[-1,-5],[-1,-6],[-5,-8],[1,-2],[-6,-4],[-5,-5],[-4,-3],[8,-6],[-2,1],[-9,4],[6,-3],[-5,-1],[-9,5],[7,6],[3,-2],[3,-9],[10,-8],[5,-4],[-5,7],[9,-10],[-2,-6],[-7,10],[4,-10],[-1,-3],[10,-1],[3,-7],[4,6],[-1,-4],[3,4],[4,1],[-8,-6],[3,2],[-9,8],[10,-10],[-7,-8],[5,1],[-3,2],[-9,-5],[6,-7],[-1,10],[-4,1],[4,-10],[10,-1],[-3,-6],[7,4],[-1,-4],[10,-5],[10,10],[6,10],[7,-2],[10,-3],[-8,-9],[-5,3],[-2,2],[-6,-5],[-2,2],[10,-9],[4,3],[5,-8],[3,7],[10,5],[-7,-8],[-3,3],[9,5],[-7,-6],[6,-6],[-5,3],[2,7],[2,-6],[10,5],[-6,-1],[2,-6],[-2,4],[4,-8],[-6,9],[3,-10],[8,7],[9,-3],[10,9],[4,3],[-10,2],[8,-2],[-1,2],[7,-2],[-9,6],[10,-10],[5,-4],[-9,-3],[-5,2],[4,-10],[7,2],[6,-2],[4,-1],[-7,-7],[-4,-9],[8,-1],[-6,-8],[9,9],[10,1],[-7,10],[-10,8],[-4,10],[-5,-1],[1,-8],[5,1],[-4,7],[2,-1],[-10,10],[2,7],[-2,5],[6,-2],[8,-7],[-6,4],[-9,-7],[10,1],[10,1],[-1,9],[-5,-1],[-2,9],[-3,-4],[5,10],[-10,6],[-6,3],[-10,8],[-5,5],[3,1],[10,-7],[6,-1],[-9,6],[9,-3],[-3,-1],[-3,6],[-7,-7],[8,-8],[-10,1],[-6,9],[-5,-7],[1,9],[8,-8],[-8,6],[7,8],[1,-6],[-10,-9],[1,-2],[-6,-3],[10,-2],[-4,9],[5,9],[-9,9],[-2,-3],[2,-7],[-3,-1],[1,-8],[8,9],[-10,-7],[-4,-9],[5,4],[-3,-8],[-2,-1],[-7,6],[6,6],[5,9],[-6,4],[-3,4],[3,5],[-7,-4]], dtype = "uint8")#candidate|1770|(280, 2)|const|uint8
call_1767 = relay.TupleGetItem(func_1438_call(relay.reshape(var_1768.astype('float64'), [3, 10, 2]), relay.reshape(var_1769.astype('float32'), [1, 144]), relay.reshape(const_1770.astype('uint8'), [560,]), ), 0)
call_1771 = relay.TupleGetItem(func_1443_call(relay.reshape(var_1768.astype('float64'), [3, 10, 2]), relay.reshape(var_1769.astype('float32'), [1, 144]), relay.reshape(const_1770.astype('uint8'), [560,]), ), 0)
output = relay.Tuple([call_1758,call_1767,var_1768,var_1769,const_1770,])
output2 = relay.Tuple([call_1759,call_1771,var_1768,var_1769,const_1770,])
func_1789 = relay.Function([var_1768,var_1769,], output)
mod['func_1789'] = func_1789
mod = relay.transform.InferType()(mod)
var_1790 = relay.var("var_1790", dtype = "float64", shape = (60,))#candidate|1790|(60,)|var|float64
var_1791 = relay.var("var_1791", dtype = "float32", shape = (144,))#candidate|1791|(144,)|var|float32
output = func_1789(var_1790,var_1791,)
func_1792 = relay.Function([var_1790,var_1791,], output)
mutated_mod['func_1792'] = func_1792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_1794 = relay.TupleGetItem(func_1536_call(), 0)
call_1795 = relay.TupleGetItem(func_1537_call(), 0)
output = relay.Tuple([call_1794,])
output2 = relay.Tuple([call_1795,])
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
func_1627_call = mod.get_global_var('func_1627')
func_1629_call = mutated_mod.get_global_var('func_1629')
call_1836 = relay.TupleGetItem(func_1627_call(), 0)
call_1837 = relay.TupleGetItem(func_1629_call(), 0)
func_477_call = mod.get_global_var('func_477')
func_481_call = mutated_mod.get_global_var('func_481')
const_1851 = relay.const([[-9.828859,8.966630,0.991539,3.729410,3.202803,-3.134833,8.889922,-1.757737,-9.346477,-6.934411,-6.646699,-2.223449,-5.626179,1.639324,6.327716,7.413489,-1.750230,8.043356,-5.357696,-5.789878,1.795238,-2.741496,-2.186960,4.292167,6.284089,8.026184,-4.803204,-4.469846,-0.901332,-0.168876,-1.264447,5.514113,-0.851175,5.010330,4.593111,5.883750,-2.913997,-7.920958,-2.950808,5.260713,7.233272,7.809584,-0.793714,-0.117357,7.618414,7.540208,-7.540083,-7.582916,5.708205,1.764169,1.711077,7.468115,-9.407675,-7.484998,6.582523,-6.719544,9.484781,-7.672838,5.240706,-0.774407,9.512824,6.679124,-5.164779,2.124399,4.806223,-8.388774,6.297261,-3.916064,7.114302,-2.911802,1.703900,2.092050,-7.320087,-4.959364,-9.393270,-2.796412,-2.721835,3.686619,0.127701,-7.916500,2.503644,5.951236,-6.677131,-5.155928,-6.043952,-8.506349,-1.022238,-2.881509,-6.325841,-1.227590,4.038754,-8.674581,-7.371373,-1.505490,-2.417151,-4.064565,-5.207941,-0.886012,-9.839848,-8.272297,3.666815,-1.775462,1.695073,-2.638070,8.206645,-9.839234,1.862732,5.754675,6.532344,7.860782,-5.157928,0.095259,2.757712,-0.377153,4.289664,8.771562,4.683045,-4.933501,-3.250874,-3.530203,7.277446,3.887884,-5.137720,0.127883,-1.648247,6.439815,-2.409434,1.770655,9.207552,3.610818,2.367305,1.687180,-6.215944,3.884573,7.744075,4.664728,-1.943708,0.171432,4.872535,-4.980141,-9.745253,-8.341688,8.163903,-4.844537]], dtype = "float32")#candidate|1851|(1, 144)|const|float32
const_1852 = relay.const([-4,-10,-5,-6,8,-3,10,-6,-1,6,10,-2,3,1,-8,-9,-7,3,-7,1,4,8,5,8,4,10,4,-8,7,-4,-4,-7,1,6,-10,-5,-8,-8,-5,-7,-2,5,-8,-4,2,9,-10,-10,-8,-9,1,3,-7,2,-9,2,-5,-7,10,7,-9,10,5,-10,-6,1,5,9,-7,5,-8,-7,-4,6,-6,-7,-1,6,-9,-9,7,4,-6,-5,2,6,7,-4,8,6,-7,2,-2,-2,-5,7,2,8,-4,10,-3,7,2,2,5,7,-2,8,7,6,2,6,5,-4,6,-7,2,10,7,-5,3,4,9,1,5,-8,1,3,-7,-6,-10,-4,9,8,8,-10,-5,6,10,10,5,2,-3,5,-1,6,6,-8,4,2,-9,-2,-9,-10,6,-4,-1,10,-1,-5,5,-8,9,-3,1,-4,-10,-9,-5,-7,1,3,-10,-6,-5,5,-2,1,10,6,-1,-6,-7,9,-1,4,-10,4,1,10,8,-7,2,-4,2,-4,10,-4,-4,-8,9,-9,-10,-6,-10,6,6,10,1,-10,4,6,3,-9,-10,2,-3,-8,-3,-4,3,-2,-3,-6,-6,7,-10,4,-2,-2,1,4,6,-7,-6,-1,10,7,6,10,-8,2,10,1,10,-6,7,5,2,2,4,5,7,-9,-3,-6,6,1,5,-9,5,-6,-7,-8,4,5,3,1,-3,-2,-7,-9,6,10,2,-6,7,3,-2,3,3,3,-9,6,5,10,8,-7,-9,-8,8,-10,-4,9,4,-4,-1,4,3,3,10,10,-3,4,5,3,-6,8,-7,-7,-8,-9,10,-10,3,-9,-5,5,-7,1,1,-7,8,8,-2,-8,8,3,1,10,-5,9,9,9,2,-2,-6,3,-4,-9,8,1,5,5,-5,9,6,-1,3,5,-2,10,3,1,-4,6,-8,-9,10,8,-1,-7,-9,1,8,7,2,7,-9,-5,-9,-5,7,-9,-8,-4,7,5,8,8,-4,10,-10,-1,5,2,-6,-10,-10,2,7,-6,-5,-2,7,-3,-5,-4,9,-8,3,6,-8,4,5,-6,2,-1,-3,2,-5,10,7,8,1,-8,-5,-4,1,3,-4,2,-10,-2,6,-4,10,-10,8,-3,-4,-5,-7,6,-7,-6,7,-6,1,-2,2,7,-10,9,6,8,2,3,-4,-7,-5,3,-1,10,7,-6,-8,10,-1,-7,-10,-9,10,-2,-8,-7,-10,-6,9,2,10,4,-2,-5,5,9,6,-8,7,-1,8,9,-8,10,3,-3,1,-10,-4,-5,-8,4,2,10,-1,6,1,-7,2,-6,9,-5,-9,-3,-1,-1,3,-3,-9,-6,-8,-10,-10,7,6,7,7,8,-7,8,-9,7,6,9,-4,6,7,-10,4,-9,5,8,7,7,-4,4,-3,5,2,3,-9,10,6,5,9,10,9,5,1,10,6,1,6,9,10,-7,-2,6,-9,7], dtype = "uint8")#candidate|1852|(560,)|const|uint8
call_1850 = relay.TupleGetItem(func_477_call(relay.reshape(const_1851.astype('float32'), [1, 12, 12]), relay.reshape(const_1852.astype('uint8'), [560,]), ), 0)
call_1853 = relay.TupleGetItem(func_481_call(relay.reshape(const_1851.astype('float32'), [1, 12, 12]), relay.reshape(const_1852.astype('uint8'), [560,]), ), 0)
var_1857 = relay.var("var_1857", dtype = "float32", shape = (1, 144))#candidate|1857|(1, 144)|var|float32
bop_1858 = relay.subtract(const_1851.astype('uint8'), relay.reshape(var_1857.astype('uint8'), relay.shape_of(const_1851))) # shape=(1, 144)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_1867 = relay.TupleGetItem(func_1803_call(), 0)
call_1868 = relay.TupleGetItem(func_1805_call(), 0)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_1869 = relay.TupleGetItem(func_1536_call(), 2)
call_1870 = relay.TupleGetItem(func_1537_call(), 2)
func_172_call = mod.get_global_var('func_172')
func_176_call = mutated_mod.get_global_var('func_176')
call_1878 = relay.TupleGetItem(func_172_call(relay.reshape(const_1852.astype('uint8'), [8, 14, 5]), relay.reshape(const_1852.astype('uint8'), [8, 14, 5]), ), 0)
call_1879 = relay.TupleGetItem(func_176_call(relay.reshape(const_1852.astype('uint8'), [8, 14, 5]), relay.reshape(const_1852.astype('uint8'), [8, 14, 5]), ), 0)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
const_1890 = relay.const([-6.367186,-3.513947,-0.060009,-5.411014,2.640426,-4.057215,0.740479,3.639958,9.134112,-8.756089,2.074566,-2.772420,-2.673170,-9.306265,-1.844274,-0.070328,2.025738,7.074118,9.975998,6.288536,-7.355545,8.111733,7.877683,-2.188650,5.182239,8.075945,-6.841361,2.007819,1.437326,-6.505018,1.969567,9.560911,4.814215,7.797729,-7.844117,-4.232345,-6.289755,-3.304085,-5.466995,-5.049014,0.838807,7.824142,5.323875,6.113815,-7.215417,-2.842254,-4.424140,-3.880236,-0.114690,-6.421814,-1.915101,6.015468,6.119087,9.384977,4.083908,9.031703,5.452380,-0.869419,1.993900,8.538155], dtype = "float64")#candidate|1890|(60,)|const|float64
call_1889 = relay.TupleGetItem(func_1789_call(relay.reshape(const_1890.astype('float64'), [60,]), relay.reshape(const_1851.astype('float32'), [144,]), ), 2)
call_1891 = relay.TupleGetItem(func_1792_call(relay.reshape(const_1890.astype('float64'), [60,]), relay.reshape(const_1851.astype('float32'), [144,]), ), 2)
var_1893 = relay.var("var_1893", dtype = "uint8", shape = (12, 144))#candidate|1893|(12, 144)|var|uint8
bop_1894 = relay.add(bop_1858.astype('int16'), var_1893.astype('int16')) # shape=(12, 144)
output = relay.Tuple([call_1836,call_1850,const_1852,call_1867,call_1869,call_1878,call_1889,const_1890,bop_1894,])
output2 = relay.Tuple([call_1837,call_1853,const_1852,call_1868,call_1870,call_1879,call_1891,const_1890,bop_1894,])
func_1907 = relay.Function([var_1857,var_1893,], output)
mod['func_1907'] = func_1907
mod = relay.transform.InferType()(mod)
var_1908 = relay.var("var_1908", dtype = "float32", shape = (1, 144))#candidate|1908|(1, 144)|var|float32
var_1909 = relay.var("var_1909", dtype = "uint8", shape = (12, 144))#candidate|1909|(12, 144)|var|uint8
output = func_1907(var_1908,var_1909,)
func_1910 = relay.Function([var_1908,var_1909,], output)
mutated_mod['func_1910'] = func_1910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_1959 = relay.TupleGetItem(func_1327_call(), 0)
call_1960 = relay.TupleGetItem(func_1329_call(), 0)
output = relay.Tuple([call_1959,])
output2 = relay.Tuple([call_1960,])
func_1966 = relay.Function([], output)
mod['func_1966'] = func_1966
mod = relay.transform.InferType()(mod)
mutated_mod['func_1966'] = func_1966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1966_call = mutated_mod.get_global_var('func_1966')
call_1967 = func_1966_call()
output = call_1967
func_1968 = relay.Function([], output)
mutated_mod['func_1968'] = func_1968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_2001 = relay.TupleGetItem(func_1609_call(), 0)
call_2002 = relay.TupleGetItem(func_1611_call(), 0)
uop_2003 = relay.tan(call_2001.astype('float64')) # shape=(3, 1, 2)
uop_2005 = relay.tan(call_2002.astype('float64')) # shape=(3, 1, 2)
func_1041_call = mod.get_global_var('func_1041')
func_1046_call = mutated_mod.get_global_var('func_1046')
const_2012 = relay.const([6,-4,-1,10,10,7,-9,9,-7,8,-3,1,-3,5,-10,10,10,4,3,-9,3,-8,-6,4,1,-5,9,10,-4,-10,5,4,-5,9,4,2,5,8,6,5,4,-2,5,6,6,8,5,-9,10,-10,-7,2,10,-5,3,-2,9,-1,5,-8,3,-2,-7,1,-10,-4,3,9,7,10,4,-9,7,1,-7,-2,-4,1,7,3,-4,4,-4,-1,-9,-2,-2,-7,-1,10,7,8,-8,7,2,-3,-6,4,-2,-10,3,-3,3,3,-8,1,2,-1,8,-6,-9,-9,-5,-4,9,5,7,6,-8,5,-1,-5,4,5,-5,6,-9,-8,9,1,-5,-9,-6,4,5,4,-4,9,7,3,5,8,4,8,8,-1,-8,7,7,-2,1,-8,-4,-4,-1,5,-8,-9,6,8,-1,-9,1,-4,7,1,-9,4,8,-4,-7,-6,-1,9,-4,-1,8,-3,8,-7,3,-3,-9,-8,7,5,-3,8,7,1,-6,8,4,1,1,7,8,-8,8,-3,8,-8,-10,-4,6,8,-8,6,-10,-4,-6,4,-2,2,-6,7,-4,6,-5,-1,-4,5,-7,-3,-7,-7,9,-9,-2,3,8,4,6,8,-8,4,-1,-3,-9,7,-5,-9,4,5,8,3,-1,8,5,-1,-6,-5,4,-5,-6,7,5,-6,-5,-6,-1,1,-6,-1,4,5,7,-6,10,3,4,-7,-7,9,-4,-7,3,-6,6,3,-9,1,-10,8,10,6,-1,-4,-4,10,-9,-2,4,5,-7,-1,5,-4,-9,-5,-2,-5,-5,-3,4,-6,2,-7,-8,-6,1,5,9,2,-2,9,9,-8,4,3,5,-3,9,-3,4,-4,-7,2,-8,6,-1,-5,10,5,5,4,-9,-6,10,-5,-9,1,10,3,-8,-10,-5,-9,8,-1,-4,-4,-5,-1,-10,-9,-7,-8,-4,5,-2,-10,1,6,-5,-2,-3,4,-7,-2,9,-9,-4,5,9,-9,-6,10,10,7,-2,-8,7,2,5,2,-5,-2,7,-6,-7,7,-8,1,4,5,6,2,5,9,10,-6,4,4,7,-10,-7,-10,-6,2,10,6,5,1,-2,2,2,6,7,-9,-2,-1,-6,5,-3,-1,-8,-8,5,-3,-10,10,4,-1,-8,9,9,-10,-2,-6,3,7,4,-4,-7,-5,-3,-10,-3,-10,-1,-2,9,-5,8,-6,-1,-2,-10,-4,-5,-5,-6,-5,-6,-1,-6,-9,-4,7,-8,-2,-8,5,-3,5,8,4,5,-4,-6,1,-5,-8,5,-2,8,5,8,-4,-7,-9,-10,-10,4,-7,-6,-4,-9,9,-10,10,-4,-6,2,-5,10,5,-7,-7,6,3,2,-2,-2,6,3,1,-8,-2,-8,1,-3,2,-9,10,2,-7,3,-5,2,8,-7,5,-8,8,-5,8,3,-7,6,10,-5,2,8,-2,1,8,-10,5,-1,6,10,-6,-1,-7,-2,-4,-4,4,8,-2,7,8,4,-5,-6,3,-2,-1,1,1,3,-2,-6,8,-4,2,2,-7,5,1,3,-9,2,10,-8,-1,-8,9,-9,7,-9,5,1,8,-5,9,-3,-5,-10,2,-7,10,-4,-1,-6,-8,-9,6,6,8,-3,9,7,4,-8,5,7,-3,4,8,2,7,-1,-3,-7,6,10,-9,-9,6,9,-3,7,-9,-9,1,5,5,10,-10,-9,-8,-4,-7,10,-10,-7,5,-8,6,-3,1,4,-1,3,3,10,10,10,6,-5,9,9,7,-8,9,10,7,-5,10,2,8,5,-5,-7,5,7,-3,7,6,-3,-7,4,-6,-4,6,10,-9,4,-1,7,5,9,-2,10,-4,-4,5,-6,-6,-9,-10], dtype = "uint64")#candidate|2012|(704,)|const|uint64
const_2013 = relay.const([3,8,-3,-1,5,-1,-8,7,-5,-5,5,-9,-5,10,-10,-1,-4,8,-6,-8,-9,-5,9,-9,2,-9,9,-8,1,-2,-6,5,4,9,-2,-2,-4,-10,-10,9,2,10,6,-8,3,-7,2,9,5,7,-5,-10,5,-5,-10,-4,-4,6,2,6,-5,-6,-7,5,5,1,1,10,-3,9,-9,8,9,5,7,9,-6,-8,-10,-5,5,4,9,-9,8,8,3,3,9,3,9,5,-7,-8,-8,-1,-9,8,-10,10,5,7,3,9,-10,-7,4,-4,-7,-7,5,7,-4,4,1,4,-4,-3,-3,-1,5,-3,2,-2,-10,-3,9,-3,-4,-9,-10,1,3,3,8,-10,3,-4,1,-3,6,-7,5,-10,-6,-4,-1,2,-10,-2,10,1,-3,8,2,-4,7,-7,-3,1,-5,8,1,4,5,-8,-7,-8,-6,6,-8,-10,6,-7,-4,8,5,-7,-6,-6,8,5,4,8,10,2,4,2,7,9,-2,-3,5,-3,-3,-9,4,-4,9,-2,6,6,-4,-10,-2,4,-7,8,7,10,-2,-10,-5,9,-6,3,-3,-2,1,-9,2,-4,-2,-9,-8,8,-2,-8,-5,-2,-6,-3,-6,-7,8,10,1,8,-8,4,-8,6,3,6,9,-6,-3,-3,5,-5,-7,-4,-9,-2,9,-3,-8,-6,10,-8,-2,-3,5,-3,7,-5,5,3,-2,-8,-2,-10,9,3,10,8,8,-6,-9,-5,-10,-1,2,6,-10,6,7,-4,2,6,1,-5,-5,-1,-3,-3,7,-6,9,-2,8,2,-4,2,8,-9,1,-7,8,-1,4,-1,-9,9,-1,-6,1,-4,8,2,-3,-4,-6,1,9,-4,-7,4,-4,-3,-8,-3,10,-5,-5,-4,-9,-3,1,10,7,5,-10,1,3,-10,4,1,3,4,-4,-8,-9,9,-6,-2,-4,-10,-5,10,-6,1,8,-6,10,10,-8,-7,1,9,-7,-2,-5,5,3,9,10,1,-4,10,7,-7,8,4,-10,-9,-1,7,-3,-7,10,6,-6,9,-4,-3,6,-7,-4,8,-1,2,-5,-9,3,-5,-2,4,-7,-7,9,1,-9,-4,9,-8,6,-2,9,9,7,-5,-6,6,-2,-4,4,8,6,-8,-3,-5,6,-4,-9,7,9,-5,-2,6,-4,7,-10,5,9,10,10,5,-5,1,1,9,9,-3,-3,-7,3,-8,8,-8,-7,-3,4,-10,-4,-2,-6,-5,5,8,-8,8,8,2,-9,5,9,-10,-3,-3,-1,3,7,6,5,3,-8,5,-9,2,-7,4,6,-10,-8,7,9,-1,-8,-10,1,-8,-6,-5,-10,-3,-7,-5,-4,-1,2,-4,-9,-9,1,2,5,-1,3,-6,-6,-1,7,-5,3,-3,-7,5,-1,-5,-6,-4,-8,-1,-2,3,-7,2,-2,-5,6,-1,-7,9,3,-10,-4,1,9,3,1,1,2,-4,-2,-1,-8,-1,1,3], dtype = "uint8")#candidate|2013|(560,)|const|uint8
call_2011 = relay.TupleGetItem(func_1041_call(relay.reshape(const_2012.astype('uint64'), [16, 11, 4]), relay.reshape(const_2012.astype('uint64'), [16, 11, 4]), relay.reshape(const_2013.astype('uint8'), [560,]), ), 2)
call_2014 = relay.TupleGetItem(func_1046_call(relay.reshape(const_2012.astype('uint64'), [16, 11, 4]), relay.reshape(const_2012.astype('uint64'), [16, 11, 4]), relay.reshape(const_2013.astype('uint8'), [560,]), ), 2)
func_1686_call = mod.get_global_var('func_1686')
func_1689_call = mutated_mod.get_global_var('func_1689')
call_2018 = relay.TupleGetItem(func_1686_call(relay.reshape(call_2011.astype('uint8'), [560,])), 0)
call_2019 = relay.TupleGetItem(func_1689_call(relay.reshape(call_2011.astype('uint8'), [560,])), 0)
output = relay.Tuple([uop_2003,call_2011,const_2012,const_2013,call_2018,])
output2 = relay.Tuple([uop_2005,call_2014,const_2012,const_2013,call_2019,])
func_2023 = relay.Function([], output)
mod['func_2023'] = func_2023
mod = relay.transform.InferType()(mod)
output = func_2023()
func_2024 = relay.Function([], output)
mutated_mod['func_2024'] = func_2024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1627_call = mod.get_global_var('func_1627')
func_1629_call = mutated_mod.get_global_var('func_1629')
call_2136 = relay.TupleGetItem(func_1627_call(), 0)
call_2137 = relay.TupleGetItem(func_1629_call(), 0)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_2139 = relay.TupleGetItem(func_1327_call(), 0)
call_2140 = relay.TupleGetItem(func_1329_call(), 0)
output = relay.Tuple([call_2136,call_2139,])
output2 = relay.Tuple([call_2137,call_2140,])
func_2153 = relay.Function([], output)
mod['func_2153'] = func_2153
mod = relay.transform.InferType()(mod)
output = func_2153()
func_2154 = relay.Function([], output)
mutated_mod['func_2154'] = func_2154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_2218 = relay.TupleGetItem(func_1215_call(), 0)
call_2219 = relay.TupleGetItem(func_1217_call(), 0)
output = call_2218
output2 = call_2219
func_2231 = relay.Function([], output)
mod['func_2231'] = func_2231
mod = relay.transform.InferType()(mod)
output = func_2231()
func_2232 = relay.Function([], output)
mutated_mod['func_2232'] = func_2232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2257 = relay.var("var_2257", dtype = "float32", shape = (11, 16, 11))#candidate|2257|(11, 16, 11)|var|float32
var_2258 = relay.var("var_2258", dtype = "float32", shape = (11, 16, 11))#candidate|2258|(11, 16, 11)|var|float32
bop_2259 = relay.less_equal(var_2257.astype('bool'), relay.reshape(var_2258.astype('bool'), relay.shape_of(var_2257))) # shape=(11, 16, 11)
uop_2262 = relay.rsqrt(var_2257.astype('float32')) # shape=(11, 16, 11)
output = relay.Tuple([bop_2259,uop_2262,])
output2 = relay.Tuple([bop_2259,uop_2262,])
func_2264 = relay.Function([var_2257,var_2258,], output)
mod['func_2264'] = func_2264
mod = relay.transform.InferType()(mod)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2264_call = mutated_mod.get_global_var('func_2264')
var_2266 = relay.var("var_2266", dtype = "float32", shape = (11, 16, 11))#candidate|2266|(11, 16, 11)|var|float32
var_2267 = relay.var("var_2267", dtype = "float32", shape = (11, 16, 11))#candidate|2267|(11, 16, 11)|var|float32
call_2265 = func_2264_call(var_2266,var_2267,)
output = call_2265
func_2268 = relay.Function([var_2266,var_2267,], output)
mutated_mod['func_2268'] = func_2268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_2438 = relay.TupleGetItem(func_1327_call(), 0)
call_2439 = relay.TupleGetItem(func_1329_call(), 0)
var_2443 = relay.var("var_2443", dtype = "float64", shape = (3, 4, 2))#candidate|2443|(3, 4, 2)|var|float64
bop_2444 = relay.bitwise_and(call_2438.astype('int16'), var_2443.astype('int16')) # shape=(3, 4, 2)
bop_2447 = relay.bitwise_and(call_2439.astype('int16'), var_2443.astype('int16')) # shape=(3, 4, 2)
output = relay.Tuple([bop_2444,])
output2 = relay.Tuple([bop_2447,])
func_2460 = relay.Function([var_2443,], output)
mod['func_2460'] = func_2460
mod = relay.transform.InferType()(mod)
var_2461 = relay.var("var_2461", dtype = "float64", shape = (3, 4, 2))#candidate|2461|(3, 4, 2)|var|float64
output = func_2460(var_2461)
func_2462 = relay.Function([var_2461], output)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_2536 = func_1299_call()
call_2537 = func_1299_call()
output = relay.Tuple([call_2536,])
output2 = relay.Tuple([call_2537,])
func_2563 = relay.Function([], output)
mod['func_2563'] = func_2563
mod = relay.transform.InferType()(mod)
mutated_mod['func_2563'] = func_2563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2563_call = mutated_mod.get_global_var('func_2563')
call_2564 = func_2563_call()
output = call_2564
func_2565 = relay.Function([], output)
mutated_mod['func_2565'] = func_2565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_2578 = relay.TupleGetItem(func_1609_call(), 0)
call_2579 = relay.TupleGetItem(func_1611_call(), 0)
var_2581 = relay.var("var_2581", dtype = "float64", shape = (3, 11, 2))#candidate|2581|(3, 11, 2)|var|float64
bop_2582 = relay.divide(call_2578.astype('float64'), var_2581.astype('float64')) # shape=(3, 11, 2)
bop_2585 = relay.divide(call_2579.astype('float64'), var_2581.astype('float64')) # shape=(3, 11, 2)
func_1041_call = mod.get_global_var('func_1041')
func_1046_call = mutated_mod.get_global_var('func_1046')
const_2594 = relay.const([-7,-7,9,-7,-9,6,-1,-9,-3,8,1,-9,5,-4,-2,-6,-8,-4,-4,-3,2,-6,4,-9,-10,-9,7,7,-7,-4,8,2,4,2,8,2,-9,-2,4,1,8,-8,9,9,-6,7,-3,-1,4,7,-1,2,7,-2,-7,8,-5,10,-2,10,-2,-2,-7,-3,6,-4,1,6,2,-1,-1,4,-5,-9,-3,-5,-7,3,-1,6,-8,-4,-8,5,10,-9,-4,8,5,-6,-8,7,-9,-1,7,-8,8,2,-4,-6,-4,5,5,-9,1,-3,6,4,10,-6,3,-10,7,6,8,6,-6,1,-4,-6,-6,4,8,-9,-5,5,-10,8,-6,9,-8,-7,-5,8,7,-4,2,6,10,-10,2,-3,-2,-8,-9,2,1,2,8,-5,5,-9,-1,-8,-2,-6,-6,5,-3,-6,-1,10,10,7,-3,6,-2,-4,1,4,2,8,-10,-8,7,3,-4,1,6,-5,-8,4,7,-3,-2,4,6,4,6,-8,7,2,-6,-7,-10,-9,1,-10,-3,-9,-9,-9,-6,2,-6,-6,2,4,2,10,2,-2,-5,3,5,-1,6,3,4,5,-6,10,-10,7,6,6,7,10,10,9,7,2,-9,-5,-10,2,-3,5,-9,-9,-10,-2,5,-10,-7,-2,9,10,-1,-3,-7,-9,9,6,-8,2,10,-8,8,-1,7,1,-7,5,8,-1,3,7,-3,10,8,1,8,4,-7,10,8,9,-4,5,2,-7,5,-9,-7,-2,-2,6,2,7,6,-1,-1,-2,-5,-7,5,4,-7,10,1,-2,5,-5,9,4,9,2,8,-5,2,-3,-5,7,-7,10,9,5,2,-10,-3,-6,4,4,-1,6,-10,-10,-6,-1,-6,-3,4,8,9,5,-4,4,-7,1,-7,1,8,4,-2,8,-7,2,10,-5,10,9,-1,4,-1,-7,-4,8,4,5,-9,2,4,7,-6,1,4,-1,-4,6,10,6,4,5,5,1,-2,2,-9,-2,-1,10,-4,2,-6,5,-2,1,2,1,7,-3,-7,7,-2,-2,1,-10,-2,4,1,-3,8,-8,-9,8,-2,-7,6,6,2,-4,-9,7,-7,1,-8,-2,8,7,-10,5,7,-5,-5,-2,-1,7,9,3,-7,-7,-9,-1,10,8,4,5,5,-4,-1,7,-3,3,-10,-9,9,4,-6,6,-5,-9,10,-2,-4,-7,-3,8,-1,-7,7,10,3,-5,8,-8,-8,4,10,4,10,-2,6,-10,-3,9,-4,-8,-2,-7,-6,3,-1,1,3,-7,9,-8,3,3,5,-8,3,-6,-6,-7,-6,-6,9,10,5,5,-9,10,-10,-10,6,-4,1,-6,-2,1,5,-7,-7,4,-4,-7,-1,7,-1,-6,4,-6,9,1,-6,9,10,-4,1,-10,-9,8,-5,3,1,-2,1,-9,1,10,-4,9,-5,2,2,-2,10,-5,6,-10,-9,-1,10,1,-2,9,1,2,10,3,10,7,7,7,-9,-2,7,9,5,-1,2,-5,-7,-1,2,10,-1,-10,-8,4,3,-6,-9,-10,-4,3,10,-10,-4,-5,-7,6,2,6,4,7,-6,-10,7,-1,-2,8,-2,-10,-9,1,-7,-4,5,-1,4,6,9,6,5,-9,-2,8,7,-10,-10,2,10,-10,-10,1,7,3,-3,-3,6,7,9,6,3,2,-9,-5,-4,3,6,-7,3,-10,-9,-7,7,7,-9,-1,8,-10,-2,3,3,-10,-2,-3,-9,1,8,-4,-4,-10,-1,7,-8,6,5,-6,7,-7,-4,-4,-3,-2,-5,-5,-7,-1,-6,10,9,-4,5,-3,5,-1,-10,4,2,-6,10,5,4,8,6,6,3,-10,-1,1], dtype = "uint64")#candidate|2594|(704,)|const|uint64
const_2595 = relay.const([[9,-10,4,7,7,5,-5,3,-10,7,-2,-2,-1,-8,-4,-1,-2,3,7,4,-9,-7,-2,8,-1,5,-1,4,-7,6,7,-6,10,-7,-7,-3,9,-1,-10,3,3,7,-3,7,-3,3,2,-1,9,1,8,-2,-4,10,-3,7,10,-3,5,7,5,-10,-1,1,-8,4,8,6,1,6,-8,-2,-9,3,7,3,-10,-10,5,-1,-6,2,-2,-4,2,-9,-6,-9,9,8,4,7,6,6,-9,-8,-1,6,7,-8,-3,9,1,-2,-2,4,2,9,-9,1,2,-2,8,-8,-2,-5,-5,-2,-4,7,-5,-3,4,-6,7,-2,9,-3,2,3,8,-8,-2,-1,7,4,1,-10,9,10,5,6,6,2,-1,-3,-3,-1,-1,5,10,-9,-7,10,7,4,1,-8,1,6,-7,8,10,-8,4,9,3,7,-1,7,-8,-1,-5,8,3,8,3,-9,-7,-5,2,-5,4,-6,8,2,-8,-6,4,-9,-8,-6,-4,5,3,2,-4,10,-8,2,2,3,8,5,3,-8,10,3,10,5,8,9,-4,-1,-7,-2,8,1,7,8,9,-1,10,4,4,3,7,-5,1,7,10,7,5,3,-1,1,5,-10,8,4,3,5,9,3,9,-6,-9,8,-10,-7,-10,-2,2,3,-5,-1,4,10,-9,3,-5,6,3,-10,-3,-7,-3,1,2,5,-10,-6,6,8,-1,1,10,-1,-1,10],[-6,-10,-6,6,4,-5,-10,9,-9,9,-7,-7,10,-4,9,-7,-8,5,8,4,-3,-6,-2,-8,1,-4,-2,9,-8,-2,-4,-1,-8,8,6,-9,3,-1,-2,7,-8,4,-1,-1,4,6,-6,4,-1,-1,-6,-7,8,3,9,-3,-10,-9,10,2,5,3,4,5,-10,6,7,-5,1,4,8,9,4,3,-7,-7,-2,4,-10,5,5,5,5,8,-10,6,-10,9,2,-8,-4,9,-7,-6,-2,-6,2,-1,-3,-3,-3,-2,3,-7,-1,1,-1,-5,-5,-7,2,6,-7,1,7,-5,-2,-3,8,7,4,7,10,6,-3,-4,6,-10,-8,5,4,6,-8,-10,-9,-6,-7,-10,6,-4,-1,-5,8,-2,-6,-2,10,8,-6,-4,5,10,4,-9,-8,-9,-1,7,-10,6,9,-8,-5,-7,-5,8,3,-2,-7,-9,-3,-5,-5,-4,3,-10,-7,9,7,4,9,9,-9,-10,3,-3,-10,-1,-1,9,-4,-6,1,2,3,7,-6,-3,9,-3,-5,-9,5,1,4,1,2,8,5,9,-3,-10,-7,6,-10,-10,-3,1,10,5,-5,1,-4,-9,6,6,8,-10,3,-1,-5,8,-10,8,-5,4,-1,-5,4,5,6,3,1,7,1,7,-8,8,5,8,10,10,-6,8,1,-4,-9,10,-2,4,-8,-1,-5,4,4,-2,3,8,6,-3,-1,5,6,10,6,-3,-2,-1,-3,6]], dtype = "uint8")#candidate|2595|(2, 280)|const|uint8
call_2593 = relay.TupleGetItem(func_1041_call(relay.reshape(const_2594.astype('uint64'), [16, 11, 4]), relay.reshape(const_2594.astype('uint64'), [16, 11, 4]), relay.reshape(const_2595.astype('uint8'), [560,]), ), 7)
call_2596 = relay.TupleGetItem(func_1046_call(relay.reshape(const_2594.astype('uint64'), [16, 11, 4]), relay.reshape(const_2594.astype('uint64'), [16, 11, 4]), relay.reshape(const_2595.astype('uint8'), [560,]), ), 7)
bop_2598 = relay.not_equal(const_2595.astype('bool'), relay.reshape(call_2593.astype('bool'), relay.shape_of(const_2595))) # shape=(2, 280)
bop_2601 = relay.not_equal(const_2595.astype('bool'), relay.reshape(call_2596.astype('bool'), relay.shape_of(const_2595))) # shape=(2, 280)
output = relay.Tuple([bop_2582,const_2594,bop_2598,])
output2 = relay.Tuple([bop_2585,const_2594,bop_2601,])
func_2608 = relay.Function([var_2581,], output)
mod['func_2608'] = func_2608
mod = relay.transform.InferType()(mod)
mutated_mod['func_2608'] = func_2608
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2609 = relay.var("var_2609", dtype = "float64", shape = (3, 11, 2))#candidate|2609|(3, 11, 2)|var|float64
func_2608_call = mutated_mod.get_global_var('func_2608')
call_2610 = func_2608_call(var_2609)
output = call_2610
func_2611 = relay.Function([var_2609], output)
mutated_mod['func_2611'] = func_2611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_2626 = func_1299_call()
call_2627 = func_1299_call()
func_477_call = mod.get_global_var('func_477')
func_481_call = mutated_mod.get_global_var('func_481')
const_2634 = relay.const([3.697313,-6.194440,-8.412198,7.734578,3.764016,-1.608081,-2.824210,7.440336,9.256790,-2.969794,-7.717207,9.190360,2.286443,5.979301,-8.724954,6.174593,-3.380536,3.871707,-3.855144,-2.845954,-6.472056,2.179529,3.739011,-5.688296,-2.751323,-3.240828,-9.474102,-3.497430,-3.540299,-7.298930,-8.399697,-2.436533,3.148312,4.703144,-5.372342,-8.785381,-7.388390,-6.480040,-3.378945,3.026372,3.430269,-2.311405,4.396448,2.157928,-1.617508,-7.722972,7.219867,1.401442,-1.438574,-5.812111,-2.255840,6.723766,-6.155491,-4.454188,-5.755341,2.344487,0.310527,8.555279,8.239977,-9.245882,-3.905056,-7.874576,-4.021413,0.561944,-2.161906,6.583467,-3.206128,4.918091,-0.468784,3.212177,1.958038,-2.662968,-0.774194,7.880085,-9.705315,6.063304,-1.198866,7.547558,8.933031,-5.870817,-2.780208,-2.755563,-9.937825,-0.221660,6.951637,-2.547184,-8.754559,0.802885,-2.044075,-9.385400,0.397465,-7.443419,2.087948,-6.688366,-6.982091,-6.970277,-0.704005,9.069536,0.156565,-3.478628,9.112554,9.306357,3.524455,0.721484,-0.711169,8.731025,8.528925,6.283893,0.772146,-0.825582,-0.734433,-4.336876,6.763859,-3.714006,0.840070,-5.981311,6.296891,4.700066,-7.189246,-5.655646,-8.826056,-4.810803,2.656613,9.104894,1.845851,-2.398266,-7.005215,9.771876,-2.371897,-4.614685,-5.939407,0.480981,8.490484,-8.870440,0.493577,-9.647993,-9.291536,8.511762,-9.725889,-9.316994,-2.242184,-6.107763,-0.439071,1.083945], dtype = "float32")#candidate|2634|(144,)|const|float32
const_2635 = relay.const([10,10,-10,3,6,8,-7,-7,8,-10,4,10,-1,-10,-8,7,6,-1,2,10,2,-5,4,2,3,-10,-5,9,-9,-10,6,4,-7,-10,9,-8,-8,3,-5,6,8,5,6,-1,4,1,-1,4,2,-6,4,3,6,-5,-1,-1,9,-4,1,-10,-9,7,-6,7,-4,8,-6,1,-8,-5,9,10,3,3,-1,8,-3,-1,5,6,10,5,-8,-10,-5,7,-2,-2,-3,6,9,6,-1,3,-5,-3,-5,-3,-7,9,-9,-5,-3,3,-5,2,6,-8,-4,-3,1,6,-8,-9,3,8,2,2,-2,3,-5,-3,-2,-8,-1,-7,-8,-10,-3,1,5,-7,-3,-4,5,4,10,-1,-8,1,1,-4,3,5,-1,2,-8,-4,-10,-9,6,7,1,-2,-8,-8,1,9,-8,-1,-5,-6,6,5,10,2,-5,6,6,5,-9,4,9,-7,10,-5,-3,-5,4,-4,3,-2,3,-4,-4,-3,-4,-6,-2,9,10,-6,-6,1,-2,4,-1,4,4,2,-9,-2,4,7,10,-8,9,-3,-5,-6,-9,10,7,-3,2,-1,-2,3,3,-2,5,5,-1,10,3,1,-4,-2,-5,-6,-10,-5,1,6,9,9,5,-7,-4,-2,-10,-9,-4,-7,-5,3,9,-8,9,6,-2,-9,9,-5,2,10,-10,6,1,2,-8,3,-4,-8,5,-10,-9,7,-6,10,10,10,10,-6,9,9,5,-5,-5,4,8,-8,-5,-6,-7,-9,-8,-9,-4,9,2,-1,4,-6,2,8,3,1,-8,9,3,4,-6,10,-7,3,9,-4,3,-1,-9,-7,2,2,-4,7,10,9,-4,6,-9,9,-5,2,-5,5,1,-8,-9,-5,1,10,-5,7,-9,-1,4,-10,-6,-8,-5,-7,-4,-1,7,-6,10,-2,-7,8,-4,6,-10,-10,9,1,1,-4,5,8,1,-2,9,10,3,-4,7,-6,6,-5,-3,3,-6,-1,-2,3,-4,-6,7,1,-2,-6,4,-7,-7,7,1,-4,-7,-6,-5,-4,-3,3,6,1,-6,-8,8,-1,8,-5,-10,-3,-5,7,9,-10,-2,6,5,-6,4,-1,7,-7,2,3,-10,-8,-7,-6,6,1,-9,4,4,-8,3,-3,1,-5,-2,4,7,7,-7,-10,-1,1,-8,7,-4,-2,-4,7,-5,-10,-1,6,-6,-1,10,-8,-2,4,-1,-6,7,1,-3,9,-1,2,5,1,5,-6,3,7,-10,-7,-3,7,-1,1,7,1,-1,1,2,-7,3,-1,5,4,-8,-6,4,-1,2,-10,-2,-8,-5,-6,10,-4,-5,1,-5,-5,6,4,-7,-8,6,9,-10,-8,-7,-1,-8,-1,-2,-4,7,-9,-5,4,9,2,-1,-3,9,3,-10,6,-9,-2,1,-7,-9,3,1,-7,-1,-6,-1,1,-4,7,-1,1,-2,-1,1,1,-6,6,-4,-8,2,-9,-4,-5,7,2,7,-7], dtype = "uint8")#candidate|2635|(560,)|const|uint8
call_2633 = relay.TupleGetItem(func_477_call(relay.reshape(const_2634.astype('float32'), [1, 12, 12]), relay.reshape(const_2635.astype('uint8'), [560,]), ), 0)
call_2636 = relay.TupleGetItem(func_481_call(relay.reshape(const_2634.astype('float32'), [1, 12, 12]), relay.reshape(const_2635.astype('uint8'), [560,]), ), 0)
bop_2642 = relay.left_shift(call_2633.astype('uint16'), relay.reshape(const_2634.astype('uint16'), relay.shape_of(call_2633))) # shape=(1, 12, 12)
bop_2645 = relay.left_shift(call_2636.astype('uint16'), relay.reshape(const_2634.astype('uint16'), relay.shape_of(call_2636))) # shape=(1, 12, 12)
func_1627_call = mod.get_global_var('func_1627')
func_1629_call = mutated_mod.get_global_var('func_1629')
call_2649 = relay.TupleGetItem(func_1627_call(), 0)
call_2650 = relay.TupleGetItem(func_1629_call(), 0)
output = relay.Tuple([call_2626,const_2635,bop_2642,call_2649,])
output2 = relay.Tuple([call_2627,const_2635,bop_2645,call_2650,])
func_2658 = relay.Function([], output)
mod['func_2658'] = func_2658
mod = relay.transform.InferType()(mod)
mutated_mod['func_2658'] = func_2658
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mutated_mod.get_global_var('func_2658')
call_2659 = func_2658_call()
output = call_2659
func_2660 = relay.Function([], output)
mutated_mod['func_2660'] = func_2660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_2703 = func_1694_call()
call_2704 = func_1694_call()
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
const_2708 = relay.const([-2.205567,3.737490,8.707703,6.020946,-8.894584,7.918139,1.459599,7.438805,1.038431,9.578407,-5.510609,9.368403,2.322193,-8.989013,3.466852,1.860182,-1.253758,1.435889,-6.602440,9.714504,1.675940,9.830576,0.151070,-0.228372,-8.764391,4.700217,-4.130765,-9.825762,-2.241444,-4.648377,0.715447,4.881965,-9.567031,9.237037,1.413397,2.956035,-0.130391,-6.976345,-5.441509,-2.995100,-4.643532,7.814063,-8.723145,-8.705459,-1.730320,0.368812,-7.068992,3.803254,6.783162,-0.416146,2.912780,1.363689,-8.182195,3.848655,-8.582268,-6.180866,7.700727,6.529310,6.995316,2.148278], dtype = "float64")#candidate|2708|(60,)|const|float64
var_2709 = relay.var("var_2709", dtype = "float32", shape = (144,))#candidate|2709|(144,)|var|float32
call_2707 = relay.TupleGetItem(func_1789_call(relay.reshape(const_2708.astype('float64'), [60,]), relay.reshape(var_2709.astype('float32'), [144,]), ), 4)
call_2710 = relay.TupleGetItem(func_1792_call(relay.reshape(const_2708.astype('float64'), [60,]), relay.reshape(var_2709.astype('float32'), [144,]), ), 4)
bop_2739 = relay.bitwise_and(call_2703.astype('int16'), call_2707.astype('int16')) # shape=(3, 280, 2)
bop_2742 = relay.bitwise_and(call_2704.astype('int16'), call_2710.astype('int16')) # shape=(3, 280, 2)
bop_2756 = relay.less(bop_2739.astype('bool'), call_2703.astype('bool')) # shape=(3, 280, 2)
bop_2759 = relay.less(bop_2742.astype('bool'), call_2704.astype('bool')) # shape=(3, 280, 2)
output = relay.Tuple([const_2708,var_2709,bop_2756,])
output2 = relay.Tuple([const_2708,var_2709,bop_2759,])
func_2760 = relay.Function([var_2709,], output)
mod['func_2760'] = func_2760
mod = relay.transform.InferType()(mod)
mutated_mod['func_2760'] = func_2760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2761 = relay.var("var_2761", dtype = "float32", shape = (144,))#candidate|2761|(144,)|var|float32
func_2760_call = mutated_mod.get_global_var('func_2760')
call_2762 = func_2760_call(var_2761)
output = call_2762
func_2763 = relay.Function([var_2761], output)
mutated_mod['func_2763'] = func_2763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_2788 = relay.TupleGetItem(func_1327_call(), 0)
call_2789 = relay.TupleGetItem(func_1329_call(), 0)
output = relay.Tuple([call_2788,])
output2 = relay.Tuple([call_2789,])
func_2790 = relay.Function([], output)
mod['func_2790'] = func_2790
mod = relay.transform.InferType()(mod)
output = func_2790()
func_2791 = relay.Function([], output)
mutated_mod['func_2791'] = func_2791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_2824 = relay.TupleGetItem(func_1609_call(), 0)
call_2825 = relay.TupleGetItem(func_1611_call(), 0)
func_1686_call = mod.get_global_var('func_1686')
func_1689_call = mutated_mod.get_global_var('func_1689')
var_2832 = relay.var("var_2832", dtype = "uint8", shape = (560,))#candidate|2832|(560,)|var|uint8
call_2831 = relay.TupleGetItem(func_1686_call(relay.reshape(var_2832.astype('uint8'), [560,])), 2)
call_2833 = relay.TupleGetItem(func_1689_call(relay.reshape(var_2832.astype('uint8'), [560,])), 2)
output = relay.Tuple([call_2824,call_2831,var_2832,])
output2 = relay.Tuple([call_2825,call_2833,var_2832,])
func_2845 = relay.Function([var_2832,], output)
mod['func_2845'] = func_2845
mod = relay.transform.InferType()(mod)
var_2846 = relay.var("var_2846", dtype = "uint8", shape = (560,))#candidate|2846|(560,)|var|uint8
output = func_2845(var_2846)
func_2847 = relay.Function([var_2846], output)
mutated_mod['func_2847'] = func_2847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_2854 = func_1704_call()
call_2855 = func_1704_call()
uop_2857 = relay.sin(call_2854.astype('float32')) # shape=(66,)
uop_2859 = relay.sin(call_2855.astype('float32')) # shape=(66,)
func_2608_call = mod.get_global_var('func_2608')
func_2611_call = mutated_mod.get_global_var('func_2611')
call_2862 = relay.TupleGetItem(func_2608_call(relay.reshape(call_2854.astype('float64'), [3, 11, 2])), 1)
call_2863 = relay.TupleGetItem(func_2611_call(relay.reshape(call_2854.astype('float64'), [3, 11, 2])), 1)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_2865 = relay.TupleGetItem(func_1609_call(), 0)
call_2866 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([uop_2857,call_2862,call_2865,])
output2 = relay.Tuple([uop_2859,call_2863,call_2866,])
func_2870 = relay.Function([], output)
mod['func_2870'] = func_2870
mod = relay.transform.InferType()(mod)
output = func_2870()
func_2871 = relay.Function([], output)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_2882 = func_1299_call()
call_2883 = func_1299_call()
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
const_2892 = relay.const([[4.300716,9.090740],[9.221785,5.191805],[6.800265,-8.611970],[0.558900,0.048638],[1.262283,9.195249],[-0.060674,-7.770465],[-5.520691,-2.755991],[-6.045624,7.049534],[4.790601,-0.952376],[-9.682202,-7.911008],[3.346898,7.143911],[-6.527957,3.522340],[2.454420,-1.130286],[0.195615,-5.137670],[-2.663522,-8.039292],[-0.336720,0.514163],[-1.151874,-3.850649],[5.001674,6.473254],[1.384450,0.231119],[1.290281,5.412804],[3.591966,-8.479415],[3.697049,9.274452],[4.706810,-0.099307],[5.198045,2.615145],[-6.853825,-1.733381],[0.439216,-0.061806],[6.334817,-5.773443],[-7.298584,3.850840],[8.037094,-0.923826],[-0.204325,6.975938]], dtype = "float64")#candidate|2892|(30, 2)|const|float64
var_2893 = relay.var("var_2893", dtype = "float32", shape = (144,))#candidate|2893|(144,)|var|float32
call_2891 = relay.TupleGetItem(func_1789_call(relay.reshape(const_2892.astype('float64'), [60,]), relay.reshape(var_2893.astype('float32'), [144,]), ), 1)
call_2894 = relay.TupleGetItem(func_1792_call(relay.reshape(const_2892.astype('float64'), [60,]), relay.reshape(var_2893.astype('float32'), [144,]), ), 1)
output = relay.Tuple([call_2882,call_2891,const_2892,var_2893,])
output2 = relay.Tuple([call_2883,call_2894,const_2892,var_2893,])
func_2908 = relay.Function([var_2893,], output)
mod['func_2908'] = func_2908
mod = relay.transform.InferType()(mod)
mutated_mod['func_2908'] = func_2908
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2909 = relay.var("var_2909", dtype = "float32", shape = (144,))#candidate|2909|(144,)|var|float32
func_2908_call = mutated_mod.get_global_var('func_2908')
call_2910 = func_2908_call(var_2909)
output = call_2910
func_2911 = relay.Function([var_2909], output)
mutated_mod['func_2911'] = func_2911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_2962 = relay.TupleGetItem(func_2870_call(), 1)
call_2963 = relay.TupleGetItem(func_2871_call(), 1)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_2972 = relay.TupleGetItem(func_1609_call(), 0)
call_2973 = relay.TupleGetItem(func_1611_call(), 0)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_2980 = relay.TupleGetItem(func_1609_call(), 0)
call_2981 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([call_2962,call_2972,call_2980,])
output2 = relay.Tuple([call_2963,call_2973,call_2981,])
func_2983 = relay.Function([], output)
mod['func_2983'] = func_2983
mod = relay.transform.InferType()(mod)
output = func_2983()
func_2984 = relay.Function([], output)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3025 = relay.const([[[-6.237481,7.218377,6.127050,-7.186164,-0.646162,-8.306987,5.271057,-8.073989,-3.171690,7.598092,-6.639389,5.310002,5.670961],[9.086532,3.339893,1.744823,8.115438,-9.164507,9.811853,6.444167,-6.284424,-4.783024,8.070866,6.259695,-6.181304,-8.230447],[-4.828335,-2.947471,6.098372,-2.130737,4.644747,8.865131,-4.452065,2.654033,-4.416941,-4.549621,4.618038,-1.890601,3.436054],[-6.224767,8.235774,9.592949,3.454067,3.067794,9.918787,6.028327,-8.359250,-8.255053,3.769485,-1.743711,-3.837968,-2.639955],[-9.610055,2.486561,-7.147350,4.212108,-3.205505,4.491054,-6.159379,7.136799,0.264190,-2.676577,5.798926,-3.138231,5.674030],[-0.746404,6.515624,7.356309,-6.264876,-0.716065,-6.406129,-4.724053,-3.306555,-1.637772,-9.696795,-0.272679,4.842834,2.126428],[5.956534,7.302476,1.584809,9.273759,-7.581327,-5.618722,1.201458,-4.554262,-6.940252,-8.527552,-4.424349,2.871858,-3.440376],[-7.951474,2.116578,-5.921199,-1.113760,8.225417,-3.016096,-6.557694,9.533756,8.945001,5.432830,-3.014548,-6.815220,-8.123741],[-8.345910,9.924999,-9.242413,-2.032777,-0.903451,-3.859460,-2.577534,-4.996297,-2.098909,9.944475,3.751902,-2.748959,-4.267833],[-5.225605,-7.875743,-0.229821,-7.900952,2.450212,6.974634,-7.569017,3.663823,-6.182112,-8.615417,-2.238450,-6.448430,-3.110445]],[[-9.747461,-2.990119,-3.787199,1.075512,-8.273903,9.240544,6.192425,6.963751,-6.179740,-8.852115,-1.715309,0.817636,0.689889],[-8.727573,1.016883,5.848049,3.273402,7.906760,-9.857939,-1.329809,-8.543870,-3.968720,5.293944,-9.877055,2.874404,5.210759],[-8.671052,2.092898,-5.540112,4.948132,-9.724743,4.871218,-2.441762,1.073621,1.709773,0.176478,9.407372,5.605227,8.242297],[-5.062470,4.513006,5.454513,-2.789893,5.255478,-1.074149,2.556132,-8.797548,-3.771228,9.243643,0.952658,-1.092985,-3.132585],[-8.955344,-6.683699,9.530463,8.955809,-4.714219,-8.784360,4.012262,6.986716,-5.053868,-6.402406,8.361933,-3.275946,0.620544],[5.670265,-2.376216,7.673835,1.712109,6.494749,7.701433,5.982329,5.331020,-6.983703,-9.359986,-4.342996,-3.321050,0.230696],[5.986998,-7.187827,0.541534,-7.062106,7.255774,8.906269,9.472649,-2.885607,1.021769,-7.410954,7.821491,1.128781,-2.375187],[0.970222,-7.718474,-3.986670,-1.913367,-2.528467,-1.319342,0.267416,0.015526,8.325277,0.350415,5.669786,6.107628,3.127110],[-5.116971,-4.063569,-7.488132,-2.990803,-3.496711,9.421141,2.264334,3.400758,-8.072298,-4.586131,3.969391,5.327072,5.955527],[0.622422,-2.755789,3.460832,7.123572,-6.534575,0.759841,-9.380314,2.602835,-5.634378,-4.941577,2.799187,2.578442,-1.456332]],[[6.151155,5.525504,-4.121349,6.284851,-9.360499,5.705178,5.506184,6.835498,-7.542264,-8.103777,0.744323,8.790340,-0.523272],[5.169344,-4.786607,-0.518246,4.276052,-8.004876,-7.094025,-2.795562,-6.262057,-1.133057,3.181751,2.039549,-0.708454,-9.569706],[-5.649504,8.858664,-6.434716,-2.685001,-7.194432,-0.013590,3.218717,3.130758,-2.517252,-9.250495,5.262517,-3.051144,-9.435552],[1.719519,-5.720883,7.468317,9.860394,3.031922,4.245379,-9.368441,4.214087,4.431362,0.928696,-6.802860,-0.707398,-3.615275],[-7.184850,4.391182,-5.346123,0.097760,-9.650752,-0.925803,9.411867,3.458087,4.866244,-9.796219,-4.640025,8.876548,-5.976908],[9.258344,-9.478981,-6.046816,3.991888,-0.251522,-9.696085,-7.406933,-8.453794,-7.355735,-5.484263,-3.303970,9.703068,-2.422323],[-6.810072,0.815549,-4.620353,5.867896,1.483638,0.319284,8.894439,-2.946632,2.177020,-3.948202,3.793889,2.336315,-0.166215],[-2.388039,-8.294784,3.922624,-0.969600,2.071837,-5.951738,-3.520797,-8.556553,-3.348068,2.091050,-7.415292,5.638623,-5.962361],[2.655066,-2.423025,0.371617,-5.774635,-8.511133,-6.007422,-7.953997,1.034191,-2.601569,-0.446824,5.813358,7.559847,-8.051170],[9.841648,-4.992176,-2.300174,3.030515,-9.699848,6.350807,-5.509346,-5.427233,7.764510,-3.557926,1.736148,-6.769531,2.236259]],[[-8.051812,-2.068821,-0.302551,-4.652071,8.909913,7.394514,-7.735800,2.762283,-6.772238,7.650440,-3.555471,6.494995,7.092264],[1.200279,2.200765,1.022657,7.913181,-7.389135,1.547365,4.320176,8.314251,9.941170,-9.925655,-9.835457,-4.518968,4.195906],[-4.302313,2.967583,-6.652586,9.752612,5.404614,7.386717,-2.531901,9.368074,7.546846,-9.452287,6.920617,-8.217803,-7.627328],[-5.515760,-1.159952,5.315688,-5.713662,-6.677997,1.523167,-3.870794,-8.518817,-6.476598,4.951191,-2.699130,-0.726601,-3.867973],[-4.525929,6.214447,3.342899,8.156899,3.050346,-6.848742,7.907622,-7.808992,-0.556354,6.907460,1.906689,0.750066,7.965437],[4.947623,-0.880749,4.072188,-3.168636,3.573558,-7.507299,3.898879,7.861268,-7.907635,-8.966407,0.132069,5.746241,3.507898],[-5.883282,-7.000110,-4.582733,8.867789,4.671965,1.711008,2.020121,2.564140,2.488874,-9.036310,-9.980020,8.713122,5.460254],[4.372091,4.797011,0.023987,9.771390,-1.078752,0.012659,-4.009081,-5.640339,-0.299490,-9.742212,-2.838654,-7.555911,-2.352998],[6.896505,2.918398,-1.817445,7.484867,9.164679,-5.687350,-2.815377,-8.315387,-6.657716,-3.288617,-4.756269,0.507708,-4.199196],[-1.274031,-0.020433,4.407044,-1.740467,-7.291747,2.906946,9.275151,9.364187,6.134484,-0.084355,1.130896,-2.621042,2.361536]],[[9.475734,0.994156,-3.002259,-1.576010,-1.479850,-5.498824,6.450438,-8.117516,9.892242,6.306631,5.195404,-2.060669,5.331497],[-1.979494,-3.051444,-3.943888,-8.527165,8.396930,-7.751921,5.519924,-5.997039,1.164537,1.304969,-8.780213,6.908119,9.152331],[1.987791,-0.502705,0.118628,-3.524903,3.983798,5.938195,8.979042,-4.862617,2.753254,-8.211365,-1.575958,7.365778,2.265578],[-3.602385,0.878236,3.624149,5.406395,9.229652,5.604198,-0.944105,4.431268,-7.317545,9.234758,-5.919018,7.182851,-1.553424],[-6.794878,0.490099,1.346176,7.385031,0.067199,4.750204,-2.569894,7.052478,1.964255,-5.508592,-6.107947,1.760501,-7.602905],[-2.832494,-1.313658,6.327196,-8.039816,6.873294,-5.551687,-9.975438,7.466589,-5.370907,6.848597,1.919039,-3.492887,8.051833],[8.806048,-8.001655,-8.658109,1.853947,2.072409,1.480232,3.990393,5.987323,5.063242,2.175610,-5.642832,3.421486,9.288025],[-6.190007,-0.524572,-1.659616,-8.078889,9.478345,8.781835,4.037080,2.940853,-6.669020,8.064143,-3.055164,-1.167717,-5.290920],[-8.532973,-2.862550,-1.633478,3.021970,-6.500941,-3.929390,-0.995614,6.879288,-8.560960,-6.724039,7.246428,-4.709089,-0.037537],[-0.942231,-4.068169,6.352730,-1.049522,2.389293,-5.724249,6.515574,-4.371333,5.614699,-5.338509,0.806262,-7.921180,-5.324786]],[[-7.622418,-4.975746,-4.262658,6.168382,9.749662,3.037441,-3.166356,7.116116,6.751740,8.634447,-9.121135,-1.843513,8.009714],[-5.864673,2.825822,-3.979209,1.837499,-2.770654,9.914467,7.803228,6.982507,-4.975656,9.882574,-8.631181,-9.919280,-9.071041],[1.059909,8.361316,-5.524078,-5.056648,7.340557,-4.385221,2.311966,-0.117889,-8.236809,-3.258459,-4.049589,-9.513696,-2.191319],[-5.120138,-7.856954,3.760750,3.549955,3.446855,-1.511563,5.940878,-0.765213,3.398481,-2.932254,-3.913352,0.827826,-9.906710],[0.315049,2.211159,-1.320157,-9.419333,-4.335255,-0.182865,3.260896,-6.862234,2.826661,9.927100,4.886153,5.440264,-0.975578],[-2.506787,-7.127833,9.806596,8.067202,7.861074,-8.394560,1.301951,-9.074818,-3.786095,9.486041,9.159415,-7.259693,-8.494803],[0.249576,4.029375,8.815286,3.007922,3.284180,1.003114,9.534760,-2.405975,-9.948844,6.239947,4.277697,-0.452485,-7.485362],[7.146309,-5.350571,-8.275517,1.505138,5.378516,8.200344,2.931841,7.179694,-5.934755,8.132148,-6.317985,-2.034684,-7.549800],[2.407245,-1.278900,8.437176,-7.142266,6.365420,9.066661,0.247817,6.994046,-0.925235,8.509919,7.877645,-4.388751,-9.769243],[-2.673024,-0.913689,-4.312264,-8.258931,8.296140,-0.644619,6.022017,-4.841193,-6.216229,-5.729043,2.882279,-1.146614,-8.570103]],[[-5.498541,4.362080,-2.880913,4.994910,-7.315690,-2.975313,-9.013588,-9.227422,-1.844383,-6.409310,5.834078,-1.828602,-9.853027],[-3.233073,-2.537241,-7.417539,9.603366,1.682059,5.452868,4.276289,-4.366645,-0.794361,7.202033,0.369025,4.933893,1.209706],[-2.222233,-0.147202,1.843344,-7.268751,7.771877,-2.069285,-0.652307,-2.028204,-5.408599,4.046354,-2.026063,1.439618,1.403328],[8.858483,-4.801867,5.168601,-9.880133,3.455711,-1.238345,0.388478,-6.381229,-4.135109,4.375116,-4.454176,-3.790908,-2.277169],[-6.811063,0.927921,-7.432341,-2.295478,2.699950,3.794494,2.814298,0.494639,-2.600481,1.109474,-3.486256,0.779407,5.186816],[4.640152,-7.176959,-6.812600,4.587023,-1.392820,-7.986047,-1.129313,-0.954873,5.500051,-9.623732,5.958422,6.460882,4.822195],[-0.299262,4.517074,-5.020017,-9.682173,-4.966289,5.309887,-6.035591,2.484943,-0.487436,-6.692184,1.655323,-3.461688,-9.393464],[8.699507,9.219887,6.599523,0.362393,0.758819,0.715374,-6.610139,-6.050630,7.603411,2.720165,9.033358,-5.703259,-4.048243],[4.375750,0.969135,-7.607818,1.070784,3.364628,-4.571142,9.825645,-7.409733,4.943760,-0.302508,3.589567,-5.113622,-1.290167],[-5.832784,2.104490,-2.717743,-9.715546,-7.899032,-8.122362,-8.862771,-9.386474,8.955749,-3.598650,-8.504667,-2.624578,3.871028]],[[-1.185997,6.598715,6.745952,1.791355,-8.261027,7.108842,2.615337,-3.965845,5.364318,2.254296,8.473993,0.675131,-8.815338],[2.168079,-8.390707,-3.977802,-6.636627,0.765552,-7.322442,-8.401295,-3.115660,8.486453,3.083105,-5.239185,-3.134377,-3.031931],[-4.966145,0.302997,9.839970,9.201436,5.423929,-3.810742,7.637327,5.654370,-3.384373,2.682893,8.693682,-7.517919,-1.963223],[5.402936,-5.327165,-0.237893,0.562138,7.908251,-0.035277,-2.732392,4.184334,4.272684,-1.323167,-7.798126,-5.501973,8.014497],[-5.623237,-2.739114,-0.180006,2.650282,0.742883,2.700569,2.391912,1.835571,-0.892156,6.990469,-2.066755,-2.945452,8.201377],[0.011987,-7.799901,0.737119,-7.399682,8.870728,7.933096,4.727300,-6.247127,9.926484,1.491257,2.871211,-4.374392,4.788816],[8.934957,0.785446,-2.299826,-4.502769,8.317272,4.562582,0.141156,8.678154,3.709556,2.023163,3.487932,3.577427,2.560289],[-3.457042,8.116896,-6.902203,-7.153165,1.147879,-5.917199,0.259591,1.045586,1.514539,-3.910578,7.638694,7.054903,5.817819],[4.650774,-7.728263,-8.104964,-8.975576,-6.383006,-0.657503,-8.704523,-7.570340,-3.147734,6.902403,-7.987243,-5.407679,1.051037],[6.540389,5.354974,4.548689,4.078700,9.093496,8.337727,-8.140976,5.353004,-5.027717,-6.919964,-2.198869,-3.822046,4.132457]],[[4.394911,6.518253,6.733364,0.562959,-7.571456,-6.353773,-9.721066,7.956623,5.678183,-0.452505,-2.934507,5.613182,2.593540],[2.830076,3.198433,-2.557347,2.249491,6.570211,-1.858032,7.733913,7.456755,6.407784,3.707507,2.541704,-5.863833,5.597950],[-8.932414,4.178757,9.180990,-2.852802,5.129932,3.517166,-4.572127,-6.452649,4.121979,2.244933,3.852569,9.517603,7.814035],[1.416478,-7.111560,0.767798,3.280303,-2.046290,7.461593,6.485853,2.850248,7.284408,9.407123,9.790613,1.369795,-9.410726],[2.720900,-2.887980,-0.176227,-3.821231,-3.488798,-9.188315,-6.141967,-5.658135,4.784733,7.256369,-3.600265,-4.243020,-2.190524],[1.703343,0.096945,-9.677663,3.855876,4.148483,-6.099478,-9.239090,4.175028,0.211296,5.524592,-8.647459,2.130621,4.343227],[-1.117366,-7.390362,8.169240,4.326853,9.620911,2.006089,-1.384581,-6.358209,-6.435219,2.425769,1.440250,-2.004886,3.788220],[7.829496,-4.223855,-9.787412,4.330718,2.319796,-3.639280,5.508546,-2.308252,-5.581982,2.041518,2.207780,0.803238,-3.508156],[7.575495,3.508722,6.704493,-0.401357,-3.254841,-4.461124,7.059785,-5.431740,-9.803543,5.131451,2.245518,1.561709,-9.422275],[-3.488916,-9.634725,3.759383,3.210442,-4.564621,5.717594,-8.781387,1.148075,8.190312,-3.920548,2.594406,0.248273,2.563680]]], dtype = "float32")#candidate|3025|(9, 10, 13)|const|float32
var_3026 = relay.var("var_3026", dtype = "float32", shape = (9, 10, 13))#candidate|3026|(9, 10, 13)|var|float32
bop_3027 = relay.power(const_3025.astype('float32'), relay.reshape(var_3026.astype('float32'), relay.shape_of(const_3025))) # shape=(9, 10, 13)
bop_3043 = relay.logical_or(const_3025.astype('bool'), relay.reshape(var_3026.astype('bool'), relay.shape_of(const_3025))) # shape=(9, 10, 13)
func_1686_call = mod.get_global_var('func_1686')
func_1689_call = mutated_mod.get_global_var('func_1689')
var_3047 = relay.var("var_3047", dtype = "uint8", shape = (560,))#candidate|3047|(560,)|var|uint8
call_3046 = relay.TupleGetItem(func_1686_call(relay.reshape(var_3047.astype('uint8'), [560,])), 3)
call_3048 = relay.TupleGetItem(func_1689_call(relay.reshape(var_3047.astype('uint8'), [560,])), 3)
output = relay.Tuple([bop_3027,bop_3043,call_3046,var_3047,])
output2 = relay.Tuple([bop_3027,bop_3043,call_3048,var_3047,])
func_3056 = relay.Function([var_3026,var_3047,], output)
mod['func_3056'] = func_3056
mod = relay.transform.InferType()(mod)
mutated_mod['func_3056'] = func_3056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3056_call = mutated_mod.get_global_var('func_3056')
var_3058 = relay.var("var_3058", dtype = "float32", shape = (9, 10, 13))#candidate|3058|(9, 10, 13)|var|float32
var_3059 = relay.var("var_3059", dtype = "uint8", shape = (560,))#candidate|3059|(560,)|var|uint8
call_3057 = func_3056_call(var_3058,var_3059,)
output = call_3057
func_3060 = relay.Function([var_3058,var_3059,], output)
mutated_mod['func_3060'] = func_3060
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3089 = relay.var("var_3089", dtype = "uint8", shape = ())#candidate|3089|()|var|uint8
var_3090 = relay.var("var_3090", dtype = "uint8", shape = (6, 12, 12))#candidate|3090|(6, 12, 12)|var|uint8
bop_3091 = relay.less_equal(var_3089.astype('bool'), var_3090.astype('bool')) # shape=(6, 12, 12)
const_3094 = relay.const([[[10,10,-1,6,-8,7,-1,8,5,-3,-2,-6],[2,3,-6,3,-7,4,7,-9,-1,7,-3,10],[-10,-5,-3,7,10,-7,7,2,2,3,-4,-6],[-9,8,2,1,8,6,8,-1,5,3,-7,-5],[-9,-10,-3,7,-3,-5,3,-9,-4,4,-8,8],[-2,-5,-6,-8,1,9,8,5,10,-6,-7,-4],[10,3,-3,-3,-2,4,9,4,-1,3,8,3],[-9,1,-4,7,2,-3,-10,8,5,1,-5,3],[7,-7,3,3,9,-9,6,8,-5,3,-7,7],[-4,-5,3,-6,3,5,1,9,-9,-4,4,5],[3,7,10,4,-4,2,7,10,-1,-8,-1,2],[-5,9,8,-1,1,-3,-3,4,7,7,-3,-6]],[[9,7,-10,4,-7,7,6,-8,-7,9,-9,-9],[8,-2,2,7,1,5,-5,9,3,-9,5,7],[2,3,-8,8,10,-1,8,-6,-2,-2,-2,-8],[8,-4,-9,-6,9,-2,6,7,10,10,5,-6],[-7,-1,9,3,-1,2,-10,-8,-10,9,10,3],[5,-7,7,5,-2,-4,8,-8,-4,6,9,-4],[6,-8,-1,-6,2,5,7,-7,8,9,7,-4],[10,-7,-6,9,-6,8,-7,6,-8,-1,2,-5],[9,6,-1,-1,10,9,10,-10,6,6,4,3],[4,8,-3,-6,-7,2,-3,-1,10,-1,-10,7],[-8,-9,6,6,-7,-5,9,7,-4,-6,-4,9],[8,4,-10,-6,-5,-1,-9,8,3,-8,-5,-10]],[[6,7,6,-5,6,4,10,4,-5,4,-6,-9],[8,-3,4,3,1,1,-7,-2,6,1,-6,-1],[4,6,-10,8,4,-10,-7,10,4,-7,-8,4],[-5,-9,-9,-3,-8,2,-3,5,-4,-6,9,-10],[7,-1,-4,-10,1,-1,4,5,10,1,8,1],[-10,-2,2,1,9,6,-9,4,8,2,9,5],[3,-3,1,-4,10,1,7,-3,3,10,8,4],[9,-9,1,8,-7,6,6,8,-7,-9,-10,-3],[-2,9,-8,5,8,8,7,5,8,3,-3,-1],[1,-7,2,5,4,3,6,-9,-3,6,-4,7],[4,7,10,-10,-8,3,-8,4,-4,-3,-7,7],[-1,4,-3,7,-9,-7,-10,4,-7,-10,7,4]],[[-2,-6,-9,-3,-7,6,-5,9,5,7,-6,-5],[-7,-5,-10,-8,8,-5,8,-9,-4,4,8,-7],[3,10,6,2,2,-10,8,9,3,-5,4,5],[-9,-9,-4,9,2,-7,-7,-2,6,-3,9,2],[-10,2,-9,1,-7,4,-9,-1,10,-9,-8,-8],[-2,-1,-5,-6,10,-8,-6,6,1,7,2,-3],[7,-1,-5,-1,10,-2,7,-9,-6,7,-7,-5],[4,8,-9,10,5,1,10,8,8,-4,-6,3],[3,-1,-4,9,-8,3,10,-3,5,-6,10,5],[-2,2,-6,-7,4,9,6,-5,5,-2,-3,1],[-3,-5,8,10,2,7,6,9,4,9,6,-6],[5,-7,7,10,-4,10,6,-2,-1,-10,-3,-10]],[[-7,-10,-4,-5,6,-9,1,-2,4,-4,3,1],[-5,2,2,-8,10,3,4,-5,1,5,3,6],[9,-8,-8,-6,-3,-2,2,-3,7,8,-7,4],[-9,1,-6,9,-7,-10,9,-7,-6,-5,-8,-3],[-6,8,8,-1,-3,-8,9,6,4,2,-4,6],[-7,-10,-1,2,8,3,4,-2,8,7,7,5],[1,-7,-6,7,-5,-2,2,4,-6,7,-2,-6],[-8,10,-8,9,2,-4,-8,-6,8,9,-2,3],[1,7,-6,4,7,1,8,-5,-5,-1,-10,6],[-4,1,8,-3,1,-2,4,4,1,7,5,-2],[-10,1,-1,-1,2,3,5,10,-8,6,-2,3],[4,-5,-1,7,-1,5,-9,-8,-8,2,-7,-9]],[[7,-4,6,4,-9,-8,5,4,-8,-1,5,8],[8,-7,4,-9,3,-2,3,6,-3,2,2,8],[-7,6,8,-7,6,3,-10,-1,-8,-2,8,-2],[-4,3,-2,-7,1,3,9,-8,-4,5,3,-8],[10,1,8,1,10,10,-6,-3,2,6,5,-6],[-5,2,-8,1,10,8,-5,-2,4,7,10,-6],[-5,2,4,-7,-9,-7,1,9,-9,-1,-9,-1],[6,-2,7,7,-8,-10,-6,-1,7,-6,-7,-10],[-3,3,4,4,2,-4,-3,9,-1,6,-5,6],[7,10,8,-10,-1,-2,7,-4,-1,-7,1,-8],[4,-2,10,-3,-10,1,-5,9,-6,-2,7,3],[6,4,6,2,3,1,1,-8,-10,-9,2,2]]], dtype = "uint8")#candidate|3094|(6, 12, 12)|const|uint8
bop_3095 = relay.logical_xor(var_3090.astype('int16'), relay.reshape(const_3094.astype('int16'), relay.shape_of(var_3090))) # shape=(6, 12, 12)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_3107 = relay.TupleGetItem(func_1536_call(), 0)
call_3108 = relay.TupleGetItem(func_1537_call(), 0)
output = relay.Tuple([bop_3091,bop_3095,call_3107,])
output2 = relay.Tuple([bop_3091,bop_3095,call_3108,])
func_3116 = relay.Function([var_3089,var_3090,], output)
mod['func_3116'] = func_3116
mod = relay.transform.InferType()(mod)
mutated_mod['func_3116'] = func_3116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3116_call = mutated_mod.get_global_var('func_3116')
var_3118 = relay.var("var_3118", dtype = "uint8", shape = ())#candidate|3118|()|var|uint8
var_3119 = relay.var("var_3119", dtype = "uint8", shape = (6, 12, 12))#candidate|3119|(6, 12, 12)|var|uint8
call_3117 = func_3116_call(var_3118,var_3119,)
output = call_3117
func_3120 = relay.Function([var_3118,var_3119,], output)
mutated_mod['func_3120'] = func_3120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_3176 = relay.TupleGetItem(func_1215_call(), 0)
call_3177 = relay.TupleGetItem(func_1217_call(), 0)
var_3189 = relay.var("var_3189", dtype = "float64", shape = (3, 16, 2))#candidate|3189|(3, 16, 2)|var|float64
bop_3190 = relay.logical_and(call_3176.astype('bool'), var_3189.astype('bool')) # shape=(3, 16, 2)
bop_3193 = relay.logical_and(call_3177.astype('bool'), var_3189.astype('bool')) # shape=(3, 16, 2)
output = relay.Tuple([bop_3190,])
output2 = relay.Tuple([bop_3193,])
func_3199 = relay.Function([var_3189,], output)
mod['func_3199'] = func_3199
mod = relay.transform.InferType()(mod)
var_3200 = relay.var("var_3200", dtype = "float64", shape = (3, 16, 2))#candidate|3200|(3, 16, 2)|var|float64
output = func_3199(var_3200)
func_3201 = relay.Function([var_3200], output)
mutated_mod['func_3201'] = func_3201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_3221 = relay.TupleGetItem(func_2658_call(), 2)
call_3222 = relay.TupleGetItem(func_2660_call(), 2)
output = call_3221
output2 = call_3222
func_3258 = relay.Function([], output)
mod['func_3258'] = func_3258
mod = relay.transform.InferType()(mod)
mutated_mod['func_3258'] = func_3258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mutated_mod.get_global_var('func_3258')
call_3259 = func_3258_call()
output = call_3259
func_3260 = relay.Function([], output)
mutated_mod['func_3260'] = func_3260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3300 = relay.var("var_3300", dtype = "bool", shape = (16, 8, 15))#candidate|3300|(16, 8, 15)|var|bool
var_3301 = relay.var("var_3301", dtype = "bool", shape = (16, 8, 15))#candidate|3301|(16, 8, 15)|var|bool
bop_3302 = relay.logical_or(var_3300.astype('bool'), relay.reshape(var_3301.astype('bool'), relay.shape_of(var_3300))) # shape=(16, 8, 15)
output = bop_3302
output2 = bop_3302
func_3308 = relay.Function([var_3300,var_3301,], output)
mod['func_3308'] = func_3308
mod = relay.transform.InferType()(mod)
var_3309 = relay.var("var_3309", dtype = "bool", shape = (16, 8, 15))#candidate|3309|(16, 8, 15)|var|bool
var_3310 = relay.var("var_3310", dtype = "bool", shape = (16, 8, 15))#candidate|3310|(16, 8, 15)|var|bool
output = func_3308(var_3309,var_3310,)
func_3311 = relay.Function([var_3309,var_3310,], output)
mutated_mod['func_3311'] = func_3311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_3338 = func_1704_call()
call_3339 = func_1704_call()
const_3347 = relay.const([8.285296,-2.041917,3.880046,-3.990597,-7.696625,7.978901,3.432447,5.745967,0.636154,-3.921466,-9.507419,9.793573,6.963738,-9.013805,7.906791,-9.925568,8.491688,1.053853,-4.798191,-6.875275,4.633196,-4.202582,2.753965,9.653260,-7.851275,-2.134768,3.967071,-6.123889,-9.577319,2.293227,-5.636095,8.735787,-9.643410,-5.119744,-9.466014,2.008971,9.687667,5.844481,7.830242,7.428166,-1.620541,-1.085817,-7.727157,-6.957773,4.160346,-9.434903,4.374034,9.155799,-0.737101,-9.678412,8.450087,7.792447,-6.945679,0.700857,9.363421,4.788384,-4.309123,3.342210,-9.108050,-6.788749,5.070551,2.300323,-5.109461,-3.736637,-0.614745,4.620201], dtype = "float64")#candidate|3347|(66,)|const|float64
bop_3348 = relay.power(call_3338.astype('float64'), relay.reshape(const_3347.astype('float64'), relay.shape_of(call_3338))) # shape=(66,)
bop_3351 = relay.power(call_3339.astype('float64'), relay.reshape(const_3347.astype('float64'), relay.shape_of(call_3339))) # shape=(66,)
output = bop_3348
output2 = bop_3351
func_3363 = relay.Function([], output)
mod['func_3363'] = func_3363
mod = relay.transform.InferType()(mod)
output = func_3363()
func_3364 = relay.Function([], output)
mutated_mod['func_3364'] = func_3364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_3420 = func_1299_call()
call_3421 = func_1299_call()
output = relay.Tuple([call_3420,])
output2 = relay.Tuple([call_3421,])
func_3429 = relay.Function([], output)
mod['func_3429'] = func_3429
mod = relay.transform.InferType()(mod)
mutated_mod['func_3429'] = func_3429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3429_call = mutated_mod.get_global_var('func_3429')
call_3430 = func_3429_call()
output = call_3430
func_3431 = relay.Function([], output)
mutated_mod['func_3431'] = func_3431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3449 = relay.var("var_3449", dtype = "int8", shape = ())#candidate|3449|()|var|int8
const_3450 = relay.const([[[-7,2,2,-8,-6,4,-1,-7,5,7,8],[-9,1,-1,7,2,-3,-1,-6,-9,-8,-2],[8,-7,5,-8,7,1,9,8,3,10,-6],[-10,2,9,-2,10,-10,-3,-10,-9,2,-8],[1,-7,-7,2,-9,-8,-4,4,7,8,-10],[4,3,8,5,-6,-1,-3,-1,-4,9,-5],[8,-1,-3,4,-9,5,4,-7,1,-7,8]],[[3,-7,2,-10,1,6,4,-8,-5,7,-8],[7,-1,-1,-1,10,-10,10,3,1,-7,-3],[-8,-9,7,-5,8,10,-10,-10,2,4,7],[6,-3,3,7,3,8,-10,-10,9,7,-9],[-2,8,1,6,6,-7,10,-3,5,-2,-9],[-7,7,7,7,1,-7,1,-10,5,10,7],[9,9,-5,6,-3,-3,10,6,-7,5,5]],[[3,7,-1,7,9,7,1,-10,6,-1,6],[6,-9,9,9,1,9,-10,-5,10,5,3],[-9,-5,6,1,-9,2,-4,-3,-4,4,2],[-6,1,2,-3,-3,8,7,-6,-6,9,-5],[8,3,10,-7,-1,1,9,9,-10,6,2],[2,4,-5,5,-4,-5,6,6,2,-8,-1],[-8,-1,-5,-6,2,7,7,7,-1,6,-1]],[[5,-8,7,10,5,8,-8,-4,-2,-4,2],[-10,-3,1,-10,4,10,-4,9,4,-4,3],[7,-8,-4,7,-4,-5,1,6,10,9,-3],[-8,-9,-8,7,4,-9,-7,7,-8,-3,7],[3,-9,5,-5,-3,3,-7,4,4,-2,-2],[-7,2,-9,-2,-3,2,-8,-10,-9,7,-4],[5,-10,5,4,-10,-6,6,-9,4,3,-4]],[[6,5,-8,7,1,-9,3,-5,-1,5,9],[-5,-2,-2,4,6,-1,-5,-7,2,-4,-9],[7,3,-8,5,2,8,8,8,8,-2,-7],[2,1,2,-7,4,4,9,-8,3,-6,-5],[-1,-6,7,9,-7,9,-5,3,1,-3,5],[-1,10,-4,-5,9,-1,6,-5,3,-4,-9],[-5,-10,-10,-5,6,-9,-10,-3,1,10,8]],[[-2,-10,6,1,-2,10,5,6,-6,-6,9],[9,8,3,-3,-5,-4,4,-9,-5,-1,5],[-4,6,3,6,-5,-3,4,4,-9,-4,5],[4,3,7,4,-2,4,2,-9,1,-3,8],[2,-5,-2,-5,9,1,9,-7,-3,-5,6],[-6,6,-8,4,4,-1,-9,2,-10,-3,2],[-10,-9,8,1,1,-9,-7,-4,5,8,-1]],[[-7,-1,3,-9,-6,-3,-3,8,5,1,6],[8,-10,-2,-9,5,5,4,-10,2,-3,10],[6,-7,-7,4,10,-3,-7,1,7,3,-2],[1,-1,7,-10,7,2,8,6,-3,5,7],[3,7,3,-6,-6,-6,-2,10,-7,1,-3],[-1,2,-5,9,7,9,-4,4,9,6,9],[-8,3,8,-7,2,1,-9,9,10,4,1]],[[-6,-9,-7,10,-5,6,4,-2,8,8,-8],[-8,6,6,-1,-9,2,-2,3,6,8,5],[-8,4,1,-5,-8,-7,-5,6,7,-3,-1],[9,-4,-1,-7,-6,-3,8,2,-2,-8,-5],[-1,-9,6,9,-4,9,-3,2,-7,4,-1],[-4,10,3,5,3,1,-4,3,-4,4,-6],[-4,-9,-7,10,9,-10,10,-9,3,2,-3]]], dtype = "int8")#candidate|3450|(8, 7, 11)|const|int8
bop_3451 = relay.multiply(var_3449.astype('int8'), const_3450.astype('int8')) # shape=(8, 7, 11)
bop_3460 = relay.logical_or(var_3449.astype('bool'), bop_3451.astype('bool')) # shape=(8, 7, 11)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_3464 = relay.TupleGetItem(func_1536_call(), 0)
call_3465 = relay.TupleGetItem(func_1537_call(), 0)
uop_3467 = relay.sin(bop_3460.astype('float32')) # shape=(8, 7, 11)
func_2760_call = mod.get_global_var('func_2760')
func_2763_call = mutated_mod.get_global_var('func_2763')
const_3472 = relay.const([-7.762613,-5.405723,7.843735,-1.856687,6.300683,-5.181705,1.276191,-9.338124,1.940715,9.921600,-5.837947,-7.285023,-7.316562,1.811579,-4.508791,1.707213,2.544665,-7.780966,3.700150,5.271891,-8.158835,-7.136284,2.028043,3.683583,9.874802,7.880167,-9.039830,9.435383,8.421012,-2.006238,-5.921437,3.324952,-4.593224,-5.966665,-3.080229,-4.167021,5.906977,-7.548401,3.217316,3.098802,-1.253832,-9.319631,9.365837,-1.967739,-8.689523,-1.495924,-1.254406,2.218389,3.880458,2.183482,1.890231,-2.187326,-2.847755,4.793949,8.644734,-1.673092,2.315518,-2.669574,2.721218,-9.265397,3.285482,-0.425482,-9.174385,-3.475515,3.561892,0.055986,-0.964513,4.650740,1.381940,-7.431906,4.663994,-3.125952,-2.736061,7.847551,5.967897,1.240407,3.520714,3.704256,8.176183,5.651998,7.505551,9.475356,1.406807,-1.792613,-3.797010,7.646501,-3.491142,-8.880768,-7.303908,-6.031287,2.612621,-3.530840,3.441810,-6.199810,-6.764555,9.130280,5.324662,9.961911,1.615714,1.888081,-1.056353,0.371551,-0.136226,5.229181,-4.939517,4.439543,-6.500210,-5.177060,2.086111,-5.935773,-8.515009,7.196598,4.764111,-7.883346,-9.043806,-5.340451,-3.263167,5.045364,7.761267,6.361297,-8.423444,-1.039314,8.124696,-4.509170,8.323128,-4.876034,-6.591265,5.344445,-3.516983,-0.890272,2.565645,1.597117,3.079216,7.489340,-2.524979,-7.765781,9.494714,1.789097,1.352196,1.711111,-2.238417,-8.120486,0.149195,-6.662627], dtype = "float32")#candidate|3472|(144,)|const|float32
call_3471 = relay.TupleGetItem(func_2760_call(relay.reshape(const_3472.astype('float32'), [144,])), 0)
call_3473 = relay.TupleGetItem(func_2763_call(relay.reshape(const_3472.astype('float32'), [144,])), 0)
uop_3486 = relay.log2(uop_3467.astype('float64')) # shape=(8, 7, 11)
output = relay.Tuple([call_3464,call_3471,const_3472,uop_3486,])
output2 = relay.Tuple([call_3465,call_3473,const_3472,uop_3486,])
func_3494 = relay.Function([var_3449,], output)
mod['func_3494'] = func_3494
mod = relay.transform.InferType()(mod)
var_3495 = relay.var("var_3495", dtype = "int8", shape = ())#candidate|3495|()|var|int8
output = func_3494(var_3495)
func_3496 = relay.Function([var_3495], output)
mutated_mod['func_3496'] = func_3496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1215_call = mod.get_global_var('func_1215')
func_1217_call = mutated_mod.get_global_var('func_1217')
call_3569 = relay.TupleGetItem(func_1215_call(), 0)
call_3570 = relay.TupleGetItem(func_1217_call(), 0)
output = call_3569
output2 = call_3570
func_3580 = relay.Function([], output)
mod['func_3580'] = func_3580
mod = relay.transform.InferType()(mod)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mutated_mod.get_global_var('func_3580')
call_3581 = func_3580_call()
output = call_3581
func_3582 = relay.Function([], output)
mutated_mod['func_3582'] = func_3582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2563_call = mod.get_global_var('func_2563')
func_2565_call = mutated_mod.get_global_var('func_2565')
call_3622 = relay.TupleGetItem(func_2563_call(), 0)
call_3623 = relay.TupleGetItem(func_2565_call(), 0)
var_3624 = relay.var("var_3624", dtype = "float64", shape = (3, 2, 2))#candidate|3624|(3, 2, 2)|var|float64
bop_3625 = relay.maximum(call_3622.astype('int16'), var_3624.astype('int16')) # shape=(3, 2, 2)
bop_3628 = relay.maximum(call_3623.astype('int16'), var_3624.astype('int16')) # shape=(3, 2, 2)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_3629 = func_1704_call()
call_3630 = func_1704_call()
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
const_3648 = relay.const([[-7,-2,5,-8,2,-1,-7,4,6,9,-9,5,7,10,7,6,6,-8,-5,-7,-2,-2,7,-9,6,-8,2,-8,1,6,3,4,1,2,10,-5,-10,-1,10,10,8,2,-3,9,-10,4,9,5,-1,8,-10,4,-7,-7,-5,-5,-4,2,-9,3,-6,-5,4,4,10,-9,-4,-8,-7,2],[-1,6,-5,-5,9,-6,-5,-9,2,6,-7,10,-9,-4,5,-10,-2,6,-5,2,8,-9,10,4,3,-3,7,2,6,-4,-4,9,-1,5,-5,1,4,8,8,-5,-4,-1,-6,8,-1,-2,7,2,6,5,4,-7,-6,2,9,-6,8,3,-10,-3,-3,7,8,-9,9,-8,-4,3,1,5],[-3,-2,-8,-4,-8,-9,-3,3,10,-6,8,3,-8,-3,10,-9,-8,-5,-6,5,9,4,-2,5,-9,-10,4,10,-10,3,10,4,-10,4,-1,9,3,-3,-10,-7,-1,9,-2,9,3,-3,-1,1,-7,9,-6,-9,-2,3,3,5,1,-1,-5,7,4,1,7,9,8,4,-6,2,7,4],[-7,6,-2,-3,9,7,7,1,1,-8,7,5,-6,1,-4,5,-3,1,10,-6,-3,-4,-10,-4,4,10,-5,3,3,7,1,1,3,-3,8,-5,10,-1,6,-1,-1,-2,-9,-10,-10,-2,-6,-9,6,5,-1,5,10,4,-5,-6,10,-3,-2,-1,-9,-7,5,8,-10,-7,1,-4,10,-9],[-7,-1,5,-5,-8,-3,-1,-4,6,10,-4,9,-9,-8,-3,5,-4,-8,-10,-9,-1,-7,-3,-9,-2,-7,7,2,8,-6,9,-2,8,3,3,6,4,-8,-4,-6,-7,-5,-8,2,-8,-9,-2,9,3,7,6,1,9,-7,-6,1,5,-10,2,-10,-2,5,-4,-3,-10,4,-6,-8,-6,-9],[-7,8,6,-6,9,9,7,-7,-2,-9,-1,-10,7,3,10,-6,2,-8,1,9,2,-5,-3,1,1,10,2,-10,-6,2,6,-3,-1,1,7,-6,-9,9,3,9,-1,-7,-7,-9,1,10,-1,-8,-4,-6,8,-3,5,8,3,2,-6,-6,-6,-7,8,4,10,2,10,6,-2,-2,-2,-2],[10,8,3,-1,9,-3,7,4,1,1,6,9,8,-4,4,5,2,-1,5,3,2,-1,-5,-4,3,-8,-5,-8,10,3,-9,-7,-2,-5,2,3,4,-1,-8,-7,-2,-3,-2,2,-2,6,-5,-4,3,6,-9,-9,10,4,-7,-3,8,10,7,-1,-10,10,-2,-4,6,-2,6,8,3,8],[-4,1,-6,-1,-2,2,3,-7,6,2,1,7,-7,-7,-8,10,-5,4,-1,-4,1,-7,8,9,-7,-8,-7,8,-1,-2,-2,-2,3,-8,-5,9,10,8,10,-2,10,-7,-6,-9,-2,7,-3,-10,-7,3,5,-7,6,1,-5,-6,6,10,-10,10,-1,-5,7,3,8,-5,-7,-7,10,-2]], dtype = "uint8")#candidate|3648|(8, 70)|const|uint8
call_3647 = relay.TupleGetItem(func_2845_call(relay.reshape(const_3648.astype('uint8'), [560,])), 0)
call_3649 = relay.TupleGetItem(func_2847_call(relay.reshape(const_3648.astype('uint8'), [560,])), 0)
func_3580_call = mod.get_global_var('func_3580')
func_3582_call = mutated_mod.get_global_var('func_3582')
call_3650 = func_3580_call()
call_3651 = func_3580_call()
uop_3654 = relay.sqrt(call_3622.astype('float32')) # shape=(3, 1, 2)
uop_3656 = relay.sqrt(call_3623.astype('float32')) # shape=(3, 1, 2)
output = relay.Tuple([bop_3625,call_3629,call_3647,const_3648,call_3650,uop_3654,])
output2 = relay.Tuple([bop_3628,call_3630,call_3649,const_3648,call_3651,uop_3656,])
func_3670 = relay.Function([var_3624,], output)
mod['func_3670'] = func_3670
mod = relay.transform.InferType()(mod)
mutated_mod['func_3670'] = func_3670
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3671 = relay.var("var_3671", dtype = "float64", shape = (3, 2, 2))#candidate|3671|(3, 2, 2)|var|float64
func_3670_call = mutated_mod.get_global_var('func_3670')
call_3672 = func_3670_call(var_3671)
output = call_3672
func_3673 = relay.Function([var_3671], output)
mutated_mod['func_3673'] = func_3673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1627_call = mod.get_global_var('func_1627')
func_1629_call = mutated_mod.get_global_var('func_1629')
call_3682 = relay.TupleGetItem(func_1627_call(), 0)
call_3683 = relay.TupleGetItem(func_1629_call(), 0)
var_3686 = relay.var("var_3686", dtype = "float64", shape = (3, 3, 2))#candidate|3686|(3, 3, 2)|var|float64
bop_3687 = relay.right_shift(call_3682.astype('int32'), var_3686.astype('int32')) # shape=(3, 3, 2)
bop_3690 = relay.right_shift(call_3683.astype('int32'), var_3686.astype('int32')) # shape=(3, 3, 2)
output = bop_3687
output2 = bop_3690
func_3696 = relay.Function([var_3686,], output)
mod['func_3696'] = func_3696
mod = relay.transform.InferType()(mod)
mutated_mod['func_3696'] = func_3696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3697 = relay.var("var_3697", dtype = "float64", shape = (3, 3, 2))#candidate|3697|(3, 3, 2)|var|float64
func_3696_call = mutated_mod.get_global_var('func_3696')
call_3698 = func_3696_call(var_3697)
output = call_3698
func_3699 = relay.Function([var_3697], output)
mutated_mod['func_3699'] = func_3699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2790_call = mod.get_global_var('func_2790')
func_2791_call = mutated_mod.get_global_var('func_2791')
call_3701 = relay.TupleGetItem(func_2790_call(), 0)
call_3702 = relay.TupleGetItem(func_2791_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3260_call = mutated_mod.get_global_var('func_3260')
call_3713 = func_3258_call()
call_3714 = func_3258_call()
const_3715 = relay.const([[[-8,3,9,10,-4,10,1,8,-2,7,-1,-8],[1,4,6,5,8,-3,9,-5,-10,1,-10,3],[-1,1,7,-10,7,-10,-1,6,2,8,-3,-6],[-9,4,5,9,-8,-7,-2,-5,-2,1,-1,7],[-8,-7,-10,-4,8,-8,7,-9,10,2,-7,-8],[-4,-4,-5,8,-6,4,6,6,-8,-6,-2,10],[3,3,-10,8,-1,9,-3,-1,10,6,-7,-1],[-7,-10,2,-2,-3,-4,7,9,4,7,-2,10],[-6,-7,9,8,5,-4,1,3,-2,-8,-8,-8],[-2,-2,5,-6,8,-6,3,4,5,4,-3,-9],[-3,5,-4,6,10,-10,-1,8,10,-8,-1,1],[-8,1,4,-10,6,10,10,4,3,-5,-10,4]],[[10,-5,2,-6,-10,6,6,3,-1,10,7,1],[9,6,2,1,2,2,9,8,2,5,2,-10],[1,4,7,9,1,5,-7,-5,2,7,-3,3],[9,-5,-8,-3,6,-6,-3,7,2,7,-10,-10],[-8,-6,-4,-8,8,5,10,-4,5,7,7,-2],[-8,2,-1,-2,1,-2,8,-7,7,4,-8,-2],[-2,-3,-3,-10,3,-2,-4,5,-2,-8,1,9],[-7,-3,-3,2,-6,-4,7,1,-6,6,7,7],[2,-2,-3,1,5,-7,-3,-6,1,7,6,9],[2,3,-9,-1,-6,-4,-3,10,-2,-8,3,3],[6,3,-9,5,8,-1,8,7,-4,-4,-9,6],[-1,-8,10,10,3,-7,8,4,-10,4,-6,6]],[[6,-8,6,8,-8,-4,10,-4,9,-5,-1,-4],[3,-3,-1,-10,8,-3,2,2,10,8,-1,-2],[4,-9,6,8,-3,10,-9,-10,8,1,-5,-8],[10,4,10,2,-5,9,-4,5,-7,3,5,2],[9,1,-8,-8,9,-8,1,-1,10,-10,-6,-4],[-7,-10,2,-8,-5,2,2,-10,5,-7,9,-3],[-9,-5,-5,1,-8,8,1,9,-5,-9,-5,5],[8,-4,-4,-6,-9,10,-2,8,10,-7,10,-10],[9,1,10,-3,1,-5,-6,8,4,9,-8,5],[3,-2,-10,-7,10,2,-7,8,4,-1,-6,6],[-8,5,2,-6,2,5,8,10,3,2,6,-5],[5,3,-8,3,-1,-2,8,5,5,1,-5,5]],[[-2,-7,-7,1,10,-5,-10,-4,5,-4,-5,-3],[3,6,-5,-6,-8,-5,7,6,9,-8,10,-2],[10,-9,6,-5,-6,-7,-4,7,-7,-8,8,2],[5,-10,1,-1,-9,6,-2,4,-4,8,7,-1],[-8,1,-4,5,2,-6,7,-6,6,2,4,6],[1,7,9,-2,-8,-3,5,-4,3,-4,7,-5],[-1,-1,-4,-3,10,1,-10,6,-6,-2,9,2],[8,-2,-5,8,-5,10,-5,-2,-5,-6,-8,6],[-3,8,6,4,5,9,-5,5,5,9,10,-8],[-8,1,9,3,10,6,1,-2,-5,4,7,2],[-5,-3,-6,-10,-5,10,10,8,5,6,3,2],[-8,-10,6,-6,-4,-3,-9,-5,-6,10,10,-6]],[[1,3,-9,-2,1,-1,-5,-7,-7,1,5,-2],[-1,-7,-2,8,-4,-5,-5,-9,2,-3,-6,-8],[-3,10,-3,1,7,-6,2,10,4,10,-6,-6],[-10,5,-1,10,10,-4,-2,-8,4,6,6,1],[-5,7,-1,-8,-4,-6,6,1,-5,8,1,-6],[7,-10,-10,-3,3,6,5,-2,7,-5,5,8],[2,-7,3,7,-7,-5,9,4,9,3,-6,-6],[4,-7,-7,9,2,-4,1,-6,-10,9,-8,1],[-5,-3,1,3,1,6,-6,9,3,4,7,-4],[1,-6,8,-8,4,-3,3,2,-5,-3,-3,8],[8,-2,2,-9,1,3,3,-4,3,1,3,-9],[2,-9,6,3,-1,-8,2,7,-5,5,-10,-4]],[[-8,10,-10,2,-2,-1,10,4,-10,6,10,-5],[4,2,1,-8,4,-10,8,8,-3,-2,-4,6],[-7,-6,-6,1,-3,3,-10,4,-10,8,-6,-9],[9,4,8,-7,-2,3,6,-5,10,4,8,3],[2,-7,-2,-9,-10,4,3,-4,-6,3,4,10],[8,3,2,6,-1,-2,1,-4,6,-2,1,6],[-4,9,6,3,5,-2,4,-3,-10,8,8,-6],[-3,-3,-4,-4,-7,10,6,9,-9,-8,-8,-8],[8,2,9,10,8,-8,2,3,-7,-7,6,2],[-7,-8,3,-3,-1,7,-7,-4,10,-7,4,-4],[-3,-1,6,-4,-8,-6,-8,4,-6,-1,-5,7],[-5,-10,4,-9,4,8,7,-3,-4,-8,9,-2]],[[-10,-9,-8,-2,9,-3,5,-2,3,-3,9,7],[-6,-8,6,2,-2,3,-5,4,-7,9,-8,5],[10,-4,-1,-4,6,1,-1,10,-4,-5,9,5],[6,-8,-6,6,10,-4,-10,7,10,2,3,-7],[4,-5,1,9,-7,-2,1,-6,-9,-1,9,-9],[-7,10,-2,6,1,10,-3,-3,-7,3,2,-10],[-10,-2,-10,7,1,-7,8,-8,7,5,9,2],[3,-6,5,-8,7,-5,2,-4,1,5,-7,10],[-2,-5,3,9,-3,10,10,-2,-9,-6,8,3],[3,1,-2,-5,-8,-7,8,-8,10,-8,8,-9],[-6,8,-5,5,9,-2,-9,-5,-9,-1,-8,-7],[-6,9,6,9,-5,6,-7,9,-5,7,8,-4]],[[-6,-4,-1,-3,10,1,1,6,8,-7,-10,-3],[7,-2,3,4,8,-4,-2,6,-10,-8,8,9],[5,-10,-2,4,2,6,2,5,-1,9,-5,-5],[-3,-7,6,-6,2,10,1,-5,9,-10,-3,-1],[3,8,-6,-4,6,1,-7,-7,-6,-3,10,-2],[9,-10,-9,7,-2,2,9,-10,-7,-9,9,-1],[2,10,10,-10,5,1,10,6,4,3,-3,-8],[-1,5,2,3,-2,3,8,-2,3,7,-3,7],[-2,-1,-3,-7,4,4,-10,10,-3,-5,-6,4],[-2,5,3,-3,2,9,-2,10,8,2,5,1],[6,-9,-3,-4,-5,10,-2,-2,-8,-2,9,4],[7,7,-1,10,-4,-2,1,2,4,3,-7,-2]],[[9,-3,5,-8,-7,-4,3,6,2,-2,1,-8],[-6,-2,-9,-7,-6,7,-10,-4,7,-3,-10,8],[4,-5,-6,3,8,-6,-10,5,3,-7,-4,10],[-7,-4,4,10,-1,-5,10,10,5,-4,9,9],[1,7,-7,9,-9,-4,4,-3,9,-4,7,-8],[2,-5,3,-4,-2,-10,-7,-6,3,-1,1,3],[-1,-10,5,-9,10,-7,-10,7,-2,-4,9,9],[-7,10,4,10,2,-4,-10,3,10,4,1,-3],[-10,5,-6,-1,5,-3,-7,-4,6,8,-4,-5],[1,4,1,-8,-4,-2,7,3,7,9,-10,-4],[3,-2,3,1,5,9,-3,-10,-1,-7,-8,-8],[-6,-10,2,-5,-6,-3,-2,-6,-10,-6,-1,9]],[[-9,-10,-7,-3,-7,-1,6,5,-3,-2,5,-4],[2,-7,6,-5,-2,-3,5,-2,-6,-1,-9,4],[-7,4,4,-6,-10,7,8,-3,1,9,-2,6],[4,-10,-6,-2,3,-6,8,1,-6,5,2,-6],[4,7,-6,3,2,10,10,-2,10,7,-9,-5],[7,-9,-8,4,-10,-5,5,4,-3,-7,8,5],[-5,-7,1,9,10,8,3,-9,4,9,3,-9],[10,1,-3,-8,-9,5,7,-9,-4,-6,-1,-9],[-10,-6,-4,1,-1,1,-7,4,-6,-7,5,-1],[-2,-5,1,-8,4,3,-9,1,-5,5,3,-9],[10,-3,9,-3,8,-4,4,9,-7,8,-5,7],[-3,-1,4,7,-5,1,2,-4,4,1,-3,-7]],[[-1,6,4,-7,8,3,-7,9,3,-5,-6,7],[-9,7,9,2,-7,-7,6,7,-3,7,5,1],[4,2,6,-9,10,-9,-7,2,-3,-6,4,-10],[-6,-6,-1,-6,2,6,-9,-3,10,-9,-2,1],[-9,-4,-10,9,-1,4,9,-10,10,-9,10,10],[-3,-7,2,-2,-4,-6,-9,2,-10,-4,8,2],[-10,9,-2,-10,-1,-1,4,6,8,-6,-6,8],[5,-7,-8,5,9,-1,-4,-7,9,-8,1,-3],[-5,-7,7,9,1,-9,4,-10,7,-7,2,7],[-3,-4,-10,-5,-8,-6,-2,-9,10,4,1,8],[-7,2,-8,-1,-8,5,-6,3,-5,-8,-5,-1],[-6,-8,1,8,10,7,1,-8,7,-6,-6,-4]],[[9,9,1,-10,5,6,5,-3,-4,-10,-10,-1],[-2,9,-6,-10,-7,1,-8,-6,9,10,6,9],[-6,4,-7,-5,1,-6,7,4,-4,-5,-3,9],[3,-6,-5,-10,3,-8,-8,-1,7,8,5,9],[4,-4,-4,-1,-2,-7,-3,9,10,8,2,-9],[-9,4,-6,5,-6,-6,-2,9,-3,5,5,4],[3,7,1,4,-10,4,-9,5,8,8,-10,7],[5,-1,-6,-10,-5,2,-3,-6,3,1,10,1],[-9,9,-8,-5,8,5,-9,3,-4,-1,-3,9],[10,-10,-6,-8,10,6,-6,2,5,10,-4,9],[9,-2,9,-8,1,-7,9,-4,5,-8,1,4],[7,1,4,9,1,6,3,1,2,-3,-5,1]]], dtype = "uint16")#candidate|3715|(12, 12, 12)|const|uint16
bop_3716 = relay.power(call_3713.astype('float64'), const_3715.astype('float64')) # shape=(12, 12, 12)
bop_3719 = relay.power(call_3714.astype('float64'), const_3715.astype('float64')) # shape=(12, 12, 12)
output = relay.Tuple([call_3701,bop_3716,])
output2 = relay.Tuple([call_3702,bop_3719,])
func_3730 = relay.Function([], output)
mod['func_3730'] = func_3730
mod = relay.transform.InferType()(mod)
mutated_mod['func_3730'] = func_3730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3730_call = mutated_mod.get_global_var('func_3730')
call_3731 = func_3730_call()
output = call_3731
func_3732 = relay.Function([], output)
mutated_mod['func_3732'] = func_3732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_3803 = func_1299_call()
call_3804 = func_1299_call()
uop_3805 = relay.log2(call_3803.astype('float64')) # shape=(3, 1, 2)
uop_3807 = relay.log2(call_3804.astype('float64')) # shape=(3, 1, 2)
bop_3818 = relay.divide(uop_3805.astype('float64'), relay.reshape(call_3803.astype('float64'), relay.shape_of(uop_3805))) # shape=(3, 1, 2)
bop_3821 = relay.divide(uop_3807.astype('float64'), relay.reshape(call_3804.astype('float64'), relay.shape_of(uop_3807))) # shape=(3, 1, 2)
output = relay.Tuple([bop_3818,])
output2 = relay.Tuple([bop_3821,])
func_3827 = relay.Function([], output)
mod['func_3827'] = func_3827
mod = relay.transform.InferType()(mod)
mutated_mod['func_3827'] = func_3827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mutated_mod.get_global_var('func_3827')
call_3828 = func_3827_call()
output = call_3828
func_3829 = relay.Function([], output)
mutated_mod['func_3829'] = func_3829
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3841 = relay.var("var_3841", dtype = "float64", shape = (4, 6, 3))#candidate|3841|(4, 6, 3)|var|float64
uop_3842 = relay.asin(var_3841.astype('float64')) # shape=(4, 6, 3)
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
var_3853 = relay.var("var_3853", dtype = "uint8", shape = (4, 140))#candidate|3853|(4, 140)|var|uint8
call_3852 = relay.TupleGetItem(func_2845_call(relay.reshape(var_3853.astype('uint8'), [560,])), 2)
call_3854 = relay.TupleGetItem(func_2847_call(relay.reshape(var_3853.astype('uint8'), [560,])), 2)
output = relay.Tuple([uop_3842,call_3852,var_3853,])
output2 = relay.Tuple([uop_3842,call_3854,var_3853,])
func_3857 = relay.Function([var_3841,var_3853,], output)
mod['func_3857'] = func_3857
mod = relay.transform.InferType()(mod)
var_3858 = relay.var("var_3858", dtype = "float64", shape = (4, 6, 3))#candidate|3858|(4, 6, 3)|var|float64
var_3859 = relay.var("var_3859", dtype = "uint8", shape = (4, 140))#candidate|3859|(4, 140)|var|uint8
output = func_3857(var_3858,var_3859,)
func_3860 = relay.Function([var_3858,var_3859,], output)
mutated_mod['func_3860'] = func_3860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_3873 = func_1299_call()
call_3874 = func_1299_call()
func_3494_call = mod.get_global_var('func_3494')
func_3496_call = mutated_mod.get_global_var('func_3496')
var_3888 = relay.var("var_3888", dtype = "int8", shape = ())#candidate|3888|()|var|int8
call_3887 = relay.TupleGetItem(func_3494_call(relay.reshape(var_3888.astype('int8'), [])), 3)
call_3889 = relay.TupleGetItem(func_3496_call(relay.reshape(var_3888.astype('int8'), [])), 3)
func_3730_call = mod.get_global_var('func_3730')
func_3732_call = mutated_mod.get_global_var('func_3732')
call_3900 = relay.TupleGetItem(func_3730_call(), 1)
call_3901 = relay.TupleGetItem(func_3732_call(), 1)
output = relay.Tuple([call_3873,call_3887,var_3888,call_3900,])
output2 = relay.Tuple([call_3874,call_3889,var_3888,call_3901,])
func_3915 = relay.Function([var_3888,], output)
mod['func_3915'] = func_3915
mod = relay.transform.InferType()(mod)
mutated_mod['func_3915'] = func_3915
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3916 = relay.var("var_3916", dtype = "int8", shape = ())#candidate|3916|()|var|int8
func_3915_call = mutated_mod.get_global_var('func_3915')
call_3917 = func_3915_call(var_3916)
output = call_3917
func_3918 = relay.Function([var_3916], output)
mutated_mod['func_3918'] = func_3918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_4042 = relay.TupleGetItem(func_1327_call(), 0)
call_4043 = relay.TupleGetItem(func_1329_call(), 0)
output = call_4042
output2 = call_4043
func_4052 = relay.Function([], output)
mod['func_4052'] = func_4052
mod = relay.transform.InferType()(mod)
output = func_4052()
func_4053 = relay.Function([], output)
mutated_mod['func_4053'] = func_4053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2983_call = mod.get_global_var('func_2983')
func_2984_call = mutated_mod.get_global_var('func_2984')
call_4057 = relay.TupleGetItem(func_2983_call(), 2)
call_4058 = relay.TupleGetItem(func_2984_call(), 2)
output = call_4057
output2 = call_4058
func_4065 = relay.Function([], output)
mod['func_4065'] = func_4065
mod = relay.transform.InferType()(mod)
output = func_4065()
func_4066 = relay.Function([], output)
mutated_mod['func_4066'] = func_4066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2023_call = mod.get_global_var('func_2023')
func_2024_call = mutated_mod.get_global_var('func_2024')
call_4113 = relay.TupleGetItem(func_2023_call(), 0)
call_4114 = relay.TupleGetItem(func_2024_call(), 0)
output = relay.Tuple([call_4113,])
output2 = relay.Tuple([call_4114,])
func_4115 = relay.Function([], output)
mod['func_4115'] = func_4115
mod = relay.transform.InferType()(mod)
mutated_mod['func_4115'] = func_4115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4115_call = mutated_mod.get_global_var('func_4115')
call_4116 = func_4115_call()
output = call_4116
func_4117 = relay.Function([], output)
mutated_mod['func_4117'] = func_4117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2790_call = mod.get_global_var('func_2790')
func_2791_call = mutated_mod.get_global_var('func_2791')
call_4218 = relay.TupleGetItem(func_2790_call(), 0)
call_4219 = relay.TupleGetItem(func_2791_call(), 0)
func_3696_call = mod.get_global_var('func_3696')
func_3699_call = mutated_mod.get_global_var('func_3699')
const_4242 = relay.const([8.396401,4.332678,3.504073,6.986673,-8.556739,-0.900816,-1.438777,9.633665,9.949151,3.893437,-0.758321,-4.725473,-2.407954,8.884679,2.319142,9.282168,6.344401,-9.155313], dtype = "float64")#candidate|4242|(18,)|const|float64
call_4241 = func_3696_call(relay.reshape(const_4242.astype('float64'), [3, 3, 2]))
call_4243 = func_3696_call(relay.reshape(const_4242.astype('float64'), [3, 3, 2]))
func_1284_call = mod.get_global_var('func_1284')
func_1287_call = mutated_mod.get_global_var('func_1287')
var_4248 = relay.var("var_4248", dtype = "float64", shape = (11, 6))#candidate|4248|(11, 6)|var|float64
call_4247 = relay.TupleGetItem(func_1284_call(relay.reshape(var_4248.astype('float64'), [3, 11, 2])), 1)
call_4249 = relay.TupleGetItem(func_1287_call(relay.reshape(var_4248.astype('float64'), [3, 11, 2])), 1)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_4255 = relay.TupleGetItem(func_2658_call(), 2)
call_4256 = relay.TupleGetItem(func_2660_call(), 2)
func_3915_call = mod.get_global_var('func_3915')
func_3918_call = mutated_mod.get_global_var('func_3918')
var_4260 = relay.var("var_4260", dtype = "int8", shape = ())#candidate|4260|()|var|int8
call_4259 = relay.TupleGetItem(func_3915_call(relay.reshape(var_4260.astype('int8'), [])), 2)
call_4261 = relay.TupleGetItem(func_3918_call(relay.reshape(var_4260.astype('int8'), [])), 2)
func_3116_call = mod.get_global_var('func_3116')
func_3120_call = mutated_mod.get_global_var('func_3120')
var_4266 = relay.var("var_4266", dtype = "uint8", shape = (864,))#candidate|4266|(864,)|var|uint8
call_4265 = relay.TupleGetItem(func_3116_call(relay.reshape(call_4259.astype('uint8'), []), relay.reshape(var_4266.astype('uint8'), [6, 12, 12]), ), 2)
call_4267 = relay.TupleGetItem(func_3120_call(relay.reshape(call_4259.astype('uint8'), []), relay.reshape(var_4266.astype('uint8'), [6, 12, 12]), ), 2)
func_2264_call = mod.get_global_var('func_2264')
func_2268_call = mutated_mod.get_global_var('func_2268')
const_4274 = relay.const([-2.813535,7.424524,-5.022548,-5.171162,-0.117648,7.629805,4.169558,7.425938,3.648176,-1.600617,7.127704,-9.909976,-5.864549,-7.283744,5.955919,4.360465,-4.139779,-2.766002,-6.043443,7.279563,-1.769426,-2.885827,-5.514836,6.301714,-2.756322,2.904569,1.296436,6.173396,-6.450895,-1.730623,5.563205,9.345708,-3.340728,-5.408837,-9.325501,7.334437,-4.700783,-9.238079,-6.779970,0.310465,-1.792631,-6.508568,-4.537687,4.560283,0.180140,-8.396924,-8.383135,-0.160045,6.609144,5.172201,6.895110,1.537581,-0.907845,-7.199451,2.918473,2.150971,-3.634242,-2.088139,2.775103,8.834103,9.797278,1.982486,-3.126657,-1.651520,5.972503,4.386217,-3.323249,-0.525393,9.496809,0.450291,-1.173128,-1.842504,-4.336853,4.898537,-0.688537,7.981719,-8.640235,8.995880,-7.771728,1.425824,0.166673,-3.677920,5.329552,2.287289,-2.920966,0.092459,5.139218,1.886573,-8.565948,-0.357208,-2.945195,-4.670620,-6.416916,7.472330,9.343603,-5.501636,0.039265,6.277067,-3.939823,0.540728,2.934540,2.683272,-8.799437,0.238578,-1.273766,-1.985327,5.351133,7.015779,-6.340516,-8.767216,0.566020,5.555929,-2.661364,2.002933,5.335210,6.274997,-8.473788,5.118828,9.146369,1.838877,-8.229828,-2.697487,9.275164,-3.960736,-0.429386,8.869500,8.507857,0.157796,5.194945,-3.215906,7.991548,-0.416947,4.269224,7.095301,-9.138466,-2.076303,-0.965705,-6.965724,-4.042145,1.154589,1.272052,2.941332,5.260586,-0.371892,7.136869,6.736801,-0.375669,-5.931923,-0.904031,9.134829,3.267712,6.909637,-5.438054,1.072705,-1.572092,-5.201837,9.250514,1.591797,-5.599429,-3.102713,-6.593516,-1.463061,6.456940,-3.666413,-6.130559,-7.125847,2.215040,8.629249,7.693032,1.264055,-5.161054,3.191649,9.795041,-1.901802,6.978331,9.145137,2.298891,-7.321270,9.143668,-8.285627,-2.451764,4.709375,-9.915553,-3.144312,5.914745,-1.607317,2.485359,5.934525,-4.804697,-8.220772,-0.975811,9.834769,3.158143,-2.664343,0.542267,7.095570,4.822038,7.395382,2.621876,1.424350,1.658983,-8.130912,-9.866949,3.706832,-5.476351,-0.904470,-4.120632,-6.048853,7.846127,-3.429973,4.099917,2.037559,-7.206488,-4.175223,-4.325483,-2.117465,7.309286,-4.431599,-0.368938,-7.379155,4.098618,-2.962722,4.399984,4.533329,9.562578,7.470156,2.050077,-2.717168,5.859204,-6.352101,-3.744180,-5.719799,1.774575,0.632254,-1.822729,-5.225501,-5.148283,5.039344,3.515510,3.967425,-6.340975,3.943913,8.758532,9.854862,8.060862,-5.752968,-8.189561,3.832056,5.006079,-4.644483,1.355911,4.414764,7.055617,9.671286,6.467487,0.396787,1.495140,-8.220503,-7.684621,7.041396,3.506556,-0.533230,-8.631316,2.406807,-7.851578,-8.910299,9.707161,-3.999252,-5.653267,7.808847,-7.245599,-4.738037,-4.841587,-6.853874,-7.097656,-7.255913,1.571449,-6.343991,-7.528914,3.366247,7.187405,-1.895990,3.690906,9.756676,-9.376577,1.214812,3.010197,-4.240129,-2.823954,3.211137,1.801726,-2.191643,-9.860280,-9.776376,1.478132,4.436155,9.401842,4.102822,-0.894825,0.003425,2.584083,1.947600,-7.819866,-6.514821,-9.038491,0.264467,3.118630,-5.401234,-2.275047,1.432403,-9.866292,-3.439820,-0.457557,-4.814410,-6.173831,-6.002361,1.928755,2.929526,8.732013,-1.619523,5.369205,3.647974,-9.130345,-7.233804,1.219283,-6.854735,-9.605379,7.824302,-2.690220,-8.530871,0.898081,-1.501713,-5.370770,-7.798450,-1.142597,-4.936027,3.684704,-0.082431,0.078434,-1.777470,-7.758786,3.113958,-2.946647,-2.410266,-4.767568,5.639207,0.743964,-8.526550,4.000862,8.082525,-8.438591,7.260842,-6.521706,8.176565,-7.966839,-5.341097,-5.836894,-2.568107,-0.036992,4.097206,3.042054,9.957359,-2.534155,-0.581012,-8.193920,5.983303,5.070817,-7.274930,7.107658,-3.385346,-0.451997,-8.824712,-3.872680,4.087093,1.890840,3.038698,3.923708,4.219649,4.875090,-9.620859,-8.081276,-4.966755,-3.695504,5.730812,-7.268988,-9.112838,-4.281181,3.204966,6.614617,9.072994,2.584590,9.359975,1.212372,-3.439990,-9.165167,5.389126,5.247254,4.285741,-3.574854,6.684653,-8.729279,1.258559,-7.401590,2.048311,9.816617,8.379269,1.908435,-7.103531,1.118637,5.845151,7.076878,-8.832716,-1.978964,-3.848219,-8.081346,5.213398,9.855657,1.843891,5.640857,0.296641,-9.248692,7.084530,8.187185,-2.938168,9.229661,3.703441,-3.019640,8.182447,0.189703,-1.047745,3.139668,-8.750437,-4.763653,-0.987604,-6.852708,9.412925,-2.568880,-9.727458,-2.039748,5.730721,5.806450,-9.694451,-8.227591,-9.189375,1.523526,-5.424835,1.879403,-7.020102,-3.968325,9.398358,-2.236190,8.134158,-2.580596,5.032178,2.241472,-8.011832,4.683854,-5.915583,-5.442403,9.016363,7.971003,-2.886172,-0.309338,7.849936,3.611503,5.309157,5.235621,1.837966,-1.621929,-9.428605,2.083802,-5.378802,5.150768,-6.806633,-8.298561,8.912112,1.822808,-6.693829,-2.623139,2.267204,-8.461652,-7.003139,4.036090,0.283342,-2.250645,2.665514,-6.722808,-5.699682,5.457624,5.532770,-8.111957,4.383567,-0.685321,2.759554,6.677692,6.965557,4.955762,6.107922,7.927284,-3.533619,-1.590383,3.665558,-9.788176,-5.881303,-5.986488,8.400388,4.533521,4.409065,-7.948014,-6.568006,4.118308,5.287205,6.822895,7.449720,-1.992120,-4.552878,-6.729837,1.619395,3.747059,-8.727144,-7.286241,-3.698584,-0.649990,8.182209,-7.638298,8.539006,5.594124,-7.349666,1.629943,9.253448,-7.382178,1.501190,6.622081,0.288942,-4.813664,8.132465,5.878530,-2.659561,0.952151,-1.879778,-0.024408,0.246441,-9.271767,-3.435541,9.763601,1.042571,-3.551661,-4.144507,-2.744380,-4.636563,7.347851,5.424775,-8.412248,7.352648,6.870308,0.135370,6.636903,-8.749922,7.744481,1.169245,-9.880539,-5.042206,9.978935,6.236214,-6.313857,8.950571,2.639481,-7.972780,-4.797984,0.993379,6.068517,5.145079,3.230275,-2.677632,8.346631,5.874272,1.021288,-4.554939,5.115045,-3.229113,2.541440,9.340357,-9.570914,-5.561261,9.857019,-2.664718,7.309835,9.895283,8.235731,0.539473,-9.037641,6.924815,-1.837826,-8.444028,4.565787,8.019351,-8.578835,7.880095,-8.262837,-3.118893,0.138217,-9.691601,-2.114551,5.931348,5.109142,-5.674157,4.183520,6.753857,1.204676,2.072571,-6.568519,-0.691449,-6.023305,2.036889,9.962027,-6.226147,7.233137,5.045265,2.666721,9.934428,4.720173,-0.471239,2.197643,-6.583765,3.610190,0.951400,-9.642829,3.530725,8.294039,1.212145,-6.670352,5.788865,-1.122018,0.879877,2.810918,2.510426,5.218088,-0.169455,0.692067,8.737853,-8.406178,1.688282,-9.189668,7.971048,6.045255,0.747138,9.005507,8.241185,8.180743,1.227691,-0.425965,-7.771645,-3.645103,-7.166077,9.613057,-1.553438,6.283096,5.526230,-2.438064,5.303729,4.084450,8.743452,-1.655496,2.782755,-3.504767,-2.017424,2.524243,-4.543587,7.994674,6.411349,-8.992534,2.301284,2.538017,-4.672374,1.870259,-2.560162,-6.691954,6.025156,-1.078619,-6.279543,5.484339,8.229792,8.210270,-5.697612,6.689246,-1.627462,-8.307530,0.019390,-6.073828,5.767127,6.859955,-9.985133,-1.085745,-0.843825,-5.359650,0.650198,-9.116866,-4.118273,-1.139779,-5.776701,2.476382,8.303152,-7.723891,0.708935,-2.526780,4.529049,-9.457469,5.806621,7.659762,-2.115706,0.288344,-1.492061,-4.417145,7.610638,4.822084,-1.338752,-7.472773,-4.890704,-3.645373,6.342641,6.802341,4.252526,3.245873,-3.048803,-6.405648,-3.498004,-3.914290,1.811823,-6.337151,0.449961,3.065913,-1.918476,0.717369,-9.342707,-3.700324,4.911731,-5.926287,-2.226249,3.169605,7.832730,3.397989,2.937326,-0.359929,-5.152488,-3.988357,-3.169628,-7.816654,0.583175,-3.954697,4.353501,-9.076944,-1.096887,2.578921,-6.998591,0.001054,0.182767,0.709748,-0.903472,3.839363,-5.745039,-8.080110,2.542382,5.134824,-9.603999,0.700068,1.651049,-8.401784,-1.993697,-7.842278,1.437140,-0.272139,-1.426985,3.517594,3.902632,8.753203,-4.573146,1.459541,-8.701746,2.266228,-2.264623,6.263373,-5.629134,4.534815,7.464184,2.106787,1.806190,6.247995,2.006110,-5.987838,-5.577967,3.329364,6.421966,-4.761246,6.669478,-8.705371,-7.873818,8.387107,-9.830539,-2.954364,-0.703648,-2.859850,8.368727,5.904657,-9.796982,-5.543476,-5.839347,-0.015458,-2.211255,4.665222,-7.700721,2.490292,7.176771,2.744014,2.475307,-9.626629,8.677247,0.768934,-8.801151,0.523769,-2.968447,1.555458,1.156918,-6.372467,9.354201,-9.064601,2.311949,-5.224167,-7.659026,-9.967842,8.240338,-7.457044,8.591703,-6.336192,-8.545675,8.394051,2.255977,4.712820,-7.079668,-8.254419,-6.017578,2.248236,-7.072082,-7.475325,2.172877,-6.444892,3.464260,2.246704,-5.804335,4.534267,4.240237,3.021864,6.331669,-3.349727,-1.032287,7.070872,8.587993,-7.780981,1.434898,-7.504956,-9.697101,2.613222,4.749749,-2.595866,-7.949752,1.889488,-1.271554,-0.494259,3.833167,5.510704,8.281272,-4.066608,7.804375,-0.221583,-7.893183,3.849876,2.676029,-5.885087,4.951382,-0.925823,-7.973077,-6.807248,-3.901217,1.675145,2.572337,0.037018,1.572173,6.764495,1.816281,4.612867,-0.904119,-5.431448,-8.941990,7.135087,4.545606,7.753371,4.526249,9.553158,8.861956,4.978227,6.349062,2.213002,8.495161,-3.058684,8.217052,-2.659888,-5.788358,4.370440,2.447347,9.340223,7.674732,2.110196,-5.367881,-5.306980,3.605589,-3.119705,1.458921,0.641104,-8.830194,7.869914,-5.646352,8.514261,-6.484256,1.611379,5.643806,-1.168499,0.114204,2.972189,-2.817375,3.256877,-5.322508,4.681268,-0.015559,-6.855953,-5.211507,-2.347929,9.798810,1.903134,-6.758197,2.450170,8.325955,-5.499620,3.810683,-5.824088,-5.031211,6.262194,8.409038,-1.623083,-3.733435,-9.255945,-0.052378,2.265455,0.744235,4.135235,9.488268,8.547550,-3.567704,2.981846,-3.960444,-7.148749,-0.142173,1.062181,-3.558965,1.679126,-2.685231,2.008271,-7.227741,-0.790320,3.959361,2.039608,-0.254656,-1.404611,6.565867,1.083235,4.374863,-8.289201,1.238291,-2.926951,0.379466,-9.724201,3.216010,-2.875232,-5.161141,6.040771,-5.415860,-4.950551,-1.764584,0.553824,1.553171,9.183205,-4.490152,-5.426511,9.652848,0.913166,-4.295797,-7.785798,8.068162,0.380516,3.053118,-4.028414,3.188998,-3.499537,9.259196,4.036091,-4.639374,6.928248,-6.821947,5.976247,-6.838257,-0.793683,-0.440728,0.902232,3.651294,-6.021232,9.434365,-0.029126,9.198372,-0.837400,8.082965,2.924565,-3.071263,-5.462138,-6.354138,-4.227078,3.803846,2.723687,7.265998,1.524300,1.971714,1.904717,-6.935665,-4.927301,0.525608,-6.768060,-1.782833,-7.901617,5.332421,-5.502654,-6.613021,-1.217516,1.021305,-6.255518,-2.273489,-3.296661,2.136593,7.800135,6.540411,9.418044,-8.622970,4.703919,-4.532814,-7.425549,1.986201,3.730031,1.755306,9.716267,-2.934024,-9.030186,6.121331,-5.819698,-8.963591,5.033870,1.030190,-2.302864,-6.192038,1.546290,-6.639459,-6.975259,-6.230161,2.790784,-4.799826,-2.049484,-3.977250,0.261257,0.411271,-0.992315,9.652099,-5.949310,4.883088,1.449509,-2.158589,-2.638381,-0.890226,-3.407588,-4.739519,-1.028539,-4.062538,3.840648,9.555882,0.319336,4.457163,8.598400,4.317135,9.880857,-1.939722,-0.494907,4.961307,0.749805,-5.910956,-5.643672,-2.545106,1.191115,-0.886573,3.752697,1.682441,-1.050222,7.756333,-2.151277,3.035115,4.488487,-1.056376,1.330270,-5.915312,2.703724,-2.831202,3.536885,-9.356550,-8.333942,-3.765165,7.877313,-8.460060,-9.869275,0.613351,-3.030071,-1.814685,-4.294638,2.012212,3.108366,8.659505,-6.378015,-0.421511,-0.126557,-8.659938,8.152336,-7.952645,4.093409,3.694620,-9.183815,-8.527870,8.520537,-5.006832,7.329438,6.758516,7.896571,4.614365,5.543405,-0.090388,-3.593545,-1.990760,4.848723,-6.722395,1.358140,-2.617032,-0.055542,-0.203501,8.281796,-1.481496,-6.776155,1.819254,-3.000724,-1.528288,2.465538,3.513042,8.010806,8.491716,-5.833365,6.362658,3.544160,-1.406306,-4.694112,-7.962858,1.989811,-3.541764,-9.006394,-2.279108,-5.487398,-4.432677,4.528844,-6.664255,0.956149,0.086242,6.097502,3.849437,-4.904125,5.108075,-5.145154,-9.919003,-9.399368,-8.782454,0.099968,8.824282,4.466343,0.927949,5.838131,5.288003,6.886146,-6.969069,-4.703687,-8.006348,1.562609,1.744695,7.325313,-8.992320,6.302402,-6.396032,8.679245,-9.805499,-6.888537,9.140814,5.357943,-0.219778,3.607977,-1.740161,3.759700,-3.859425,-1.722169,-0.071737,3.894278,9.752770,3.914148,3.627265,3.641739,4.322205,4.202666,2.546242,-8.048593,-0.833142,-3.528760,8.378490,0.752780,6.611675,2.232769,3.246912,-0.580144,4.141566,-7.123020,-9.337984,0.420804,8.019100,-4.045361,8.037224,3.841092,-4.141162,-3.690414,0.797609,5.591615,9.159791,-6.615324,3.325742,1.646599,6.848414,-1.793383,1.621932,9.868188,-1.510242,3.354197,-9.245709,1.085928,5.478621,-0.824848,7.497176,8.085707,5.948324,8.770453,-3.088275,7.251215,6.700402,6.846366,2.665752,7.683016,-0.120354,-8.351529,2.230172,2.871225,2.459347,2.418742,8.997263,-8.477646,7.097598,4.857714,-2.565637,2.073653,-8.843913,4.581669,7.888301,-3.830478,0.237309,4.747696,-7.289539,8.772790,-9.577721,8.228840,5.723976,-3.157986,5.560134,-6.607272,2.201065,1.398428,-7.884753,4.509353,-8.413409,8.763339,-4.799978,-7.279924,1.072985,7.496820,8.567404,7.493482,-7.495554,6.184992,-4.472356,2.148551,1.763796,0.960602,4.379630,2.319402,-1.061521,-7.529166,0.073465,-0.119549,-1.168013,0.334486,-4.306610,1.141727,-4.524945,-7.396486,-9.823774,-5.221390,9.291490,-1.972260,5.403229,-1.126034,-1.577447,-3.916385,1.682227,3.247317,-6.182672,2.033599,5.470281,2.142667,2.699026,-1.585151,-8.848559,5.380286,2.877753,-4.917594,-4.422404,-9.055792,0.560364,-5.169360,9.528156,3.522972,-6.998887,-7.983211,4.045371,-3.176326,-5.270055,-2.371146,0.288987,-3.859509,2.694544,0.654525,0.436062,5.053185,3.879152,6.321890,0.135887,-4.884495,-6.769090,6.091452,4.378484,-4.885915,2.920891,-6.459431,5.072908,9.089214,0.604390,-6.498629,-8.900977,-1.536758,5.523074,5.341244,-7.353348,4.009438,-5.054347,-5.263583,-5.970938,0.684298,9.741932,-6.381563,-1.505713,-8.201378,5.970441,-4.882005,-1.886414,4.192076,4.927967,-2.059091,-7.788951,-0.499972,-4.626774,-9.169081,7.498143,-5.445842,7.427851,6.661198,-1.077078,-6.794647,-5.610820,-0.911547,3.711776,1.896812,-1.350308,-4.906490,9.602617,2.477840,6.065701,-6.204474,-6.124127,5.184130,7.077688,0.130103,-7.559380,5.827773,8.088899,1.033755,7.816638,0.349739,-3.962299,5.292666,-5.076740,-4.439328,-4.928965,-9.693670,9.870598,4.188555,4.444157,9.295494,-7.157025,-7.523006,-8.387277,-1.336930,-1.002447,0.840973,8.511887,-7.458834,0.492065,3.630147,9.243048,-6.988874,1.784418,-5.410178,4.568700,8.209822,-1.756987,0.251645,7.020894,6.546693,8.246811,0.752838,9.135374,-9.154995,-7.299297,-4.437813,1.966000,-2.061805,-1.308582,3.500232,-6.275957,1.950848,7.957463,7.021455,-1.325482,-6.811415,5.703258,-2.789974,-7.773312,-1.253072,-0.362316,-0.415388,6.279514,6.544375,9.143577,8.966850,9.764869,1.951766,3.485837,0.324059,5.016457,2.188684,7.569437,3.732901,-1.471805,-6.168152,-9.968820,6.838773,-6.095408,-6.450647,1.408914,3.850009,-8.897895,2.073960,-2.610428,-1.718555,4.560554,-4.906216,4.557863,-7.947489,6.854319,1.765032,7.514398,-9.008893,9.686476,-8.662163,-8.896191,6.780357,-5.990403,4.846353,2.521122,-8.613144,2.005644,-4.998842,-4.336308,0.052358,1.458118,5.873867,5.325287,-7.176264,-5.305123,7.818549,5.440611,-3.650275,-0.279957,-6.784241,2.130562,-3.318398,6.568029,5.573724,5.454241,-3.220209,3.017775,0.805391,5.837713,8.090304,-7.504403,-6.851783,4.810006,8.201058,-6.977785,-2.315034,-0.351155,4.039503,8.263737,5.675667,6.355365,7.391546,-7.159986,2.981083,3.697852,0.353051,9.845722,8.581489,-7.144327,-4.171961,-1.074759,-6.637917,2.713902,-1.435865,2.433790,9.505784,2.417066,3.811800,-3.570618,0.617473,-8.687637,5.197330,7.232841,-1.324208,-6.562860,-4.153535,7.834500,1.297890,-2.096146,9.733859,-4.798712,-6.285666,-4.789570,9.249455,-8.946247,-2.740636,4.477077,7.844284,-2.602734,4.228537,-1.099413,4.511065,-6.574478,2.962514,-6.088977,-9.192446,0.888712,3.749388,8.529510,-9.854345,3.127563,-6.734937,1.668625,1.374479,1.270855,-9.069350,2.757333,-8.570843,-6.119422,-6.357228,-7.359959,6.904851,-5.296094,5.427242,0.247913,8.499297,-0.102032,-9.418458,9.446449,7.102299,-4.585476,5.084712,3.673582,3.674456,2.940163,6.351073,0.049768,9.053102,7.965896,8.316097,5.432023,9.205859,-2.706203,1.829098,-9.962342,-7.024548,-4.539998,-7.764997,1.320556,6.551225,6.730353,7.702513,-7.250694,-1.903431,1.523916,-4.493309,3.821484,1.055482,1.792152,1.862403,4.722293,-5.024827,9.947924,-4.283727,7.298933,3.054519,-0.494801,3.339844,-6.013969,-9.271624,1.186454,-4.263792,-6.078126,-4.773144,-0.943823,5.387952,8.813016,5.056373,-0.062814,-7.565441,4.243016,8.585331,-8.483180,-3.524841,-3.496613,-0.223150,-8.464864,-4.629088,-8.156927,-3.319718,7.497112,1.917457,-3.436035,1.499102,-4.016127,-1.723484,-5.288125,4.148324,-2.966362,8.866095,-8.864527,-0.853484,-0.712466,1.016786,2.487447,1.249003,-7.180369,1.701329,9.614886,0.399058,-1.514370,6.846193,1.053628,9.610396,1.820982,8.547950,8.703656,-2.120553,-3.171068,-6.747208,2.605133,-3.196239,-1.030165,-3.920188,7.815083,0.807730,2.402391,-2.483670,8.789037,-6.879699,-4.260233,-4.924074,5.015600,6.767866,2.770240,6.183469,6.615831,-5.237806,-8.654978,7.992693,-3.234872,0.433292,7.021090,7.167644,-3.717553,5.001707,1.653020,-9.568244,-8.841371,-2.760438,3.634955,4.627036,-7.245842,8.795461,-4.089753,-0.544143,7.581066,0.952683,3.531895,-6.633010,-8.595384,-0.412531,9.643332,9.230144,-0.483552,4.318822,8.837413,-2.592715,-4.372387,-6.892102,-4.648697,-2.275799,7.033379,-7.855167,-0.828426,-4.337894,4.183385,-3.801260,1.055325,-6.304686,8.308736,7.345309,-8.054152,-7.660550,4.364650,-3.529652,9.911570,-5.651670,-0.799242,1.086093,8.397360,5.018148,-0.297108,0.047071,1.847894,6.947972,-6.132243,-1.240294,-1.870817,1.332109,4.959878,2.520625,-9.659322,1.427187,5.660209,4.939807,-9.096490,7.730637,-6.468932,-6.176509,-6.353457,1.279485,9.219544,-6.625976,-3.229731,5.814038,4.509945,7.425108,-3.616520,-3.821812,2.335516,-4.154708,-6.395085,7.545766,3.567210,7.142518,1.672544,-4.440942,-3.647307,8.706337,-1.411668,-4.905689,4.656486,-3.118720,7.332334,0.058164,-4.324007,-5.403160,4.064975,-0.578630,-9.739888,3.231987,-6.129275,-1.271911,-2.151074,6.933877,-4.367881,-2.235118,5.902382,-3.801567,0.287082,-2.347993,6.188783,-3.886035,-5.586855,2.302477,-3.416419,-6.800822,-3.608734,8.782389,-4.728616,-7.276573,8.446780,1.381282,8.604210,1.356363,8.683789,-1.959583,-7.742826,-9.254780,9.138489,9.754180,-1.047496,-8.325293,-2.060249,0.534118,6.912673,-2.747337,-4.307153,3.405001,9.450395,-6.320476,-1.133330,6.349902,2.820248,3.532308,-3.623865,7.074120,3.718350,9.747964,2.830981,-8.144056,-1.344639,7.652861,-7.017870,-6.594795,0.501983,2.970041,-7.695368,0.752076,-8.250546,-0.413463,0.352173,6.662416,-1.159651,9.314522,5.575164,-9.115483,-6.648274,-8.044067,-0.395945,-9.855538,1.601517,-1.915506,-5.353467,8.191025,-4.578178,6.717080,4.215792,-1.482210,-3.675876,-6.614085,-2.945306,8.154835,-8.063129,7.459918,6.962200,6.746274,6.051494,-9.338130,9.005065,-6.294228,1.703950,5.801500,-4.738807,-1.051157,4.329496,-9.122670,7.611853,-0.652244,4.919590,9.339477,2.905299], dtype = "float32")#candidate|4274|(1936,)|const|float32
call_4273 = relay.TupleGetItem(func_2264_call(relay.reshape(const_4274.astype('float32'), [11, 16, 11]), relay.reshape(const_4274.astype('float32'), [11, 16, 11]), ), 1)
call_4275 = relay.TupleGetItem(func_2268_call(relay.reshape(const_4274.astype('float32'), [11, 16, 11]), relay.reshape(const_4274.astype('float32'), [11, 16, 11]), ), 1)
uop_4282 = relay.log(call_4241.astype('float64')) # shape=(3, 3, 2)
uop_4284 = relay.log(call_4243.astype('float64')) # shape=(3, 3, 2)
uop_4287 = relay.atan(uop_4282.astype('float64')) # shape=(3, 3, 2)
uop_4289 = relay.atan(uop_4284.astype('float64')) # shape=(3, 3, 2)
uop_4294 = relay.log2(uop_4287.astype('float32')) # shape=(3, 3, 2)
uop_4296 = relay.log2(uop_4289.astype('float32')) # shape=(3, 3, 2)
func_2790_call = mod.get_global_var('func_2790')
func_2791_call = mutated_mod.get_global_var('func_2791')
call_4298 = relay.TupleGetItem(func_2790_call(), 0)
call_4299 = relay.TupleGetItem(func_2791_call(), 0)
uop_4300 = relay.log10(uop_4282.astype('float32')) # shape=(3, 3, 2)
uop_4302 = relay.log10(uop_4284.astype('float32')) # shape=(3, 3, 2)
func_3116_call = mod.get_global_var('func_3116')
func_3120_call = mutated_mod.get_global_var('func_3120')
call_4311 = relay.TupleGetItem(func_3116_call(relay.reshape(var_4260.astype('uint8'), []), relay.reshape(var_4266.astype('uint8'), [6, 12, 12]), ), 2)
call_4312 = relay.TupleGetItem(func_3120_call(relay.reshape(var_4260.astype('uint8'), []), relay.reshape(var_4266.astype('uint8'), [6, 12, 12]), ), 2)
output = relay.Tuple([call_4218,const_4242,call_4247,var_4248,call_4255,call_4259,var_4260,call_4265,var_4266,call_4273,const_4274,uop_4294,call_4298,uop_4300,call_4311,])
output2 = relay.Tuple([call_4219,const_4242,call_4249,var_4248,call_4256,call_4261,var_4260,call_4267,var_4266,call_4275,const_4274,uop_4296,call_4299,uop_4302,call_4312,])
func_4317 = relay.Function([var_4248,var_4260,var_4266,], output)
mod['func_4317'] = func_4317
mod = relay.transform.InferType()(mod)
var_4318 = relay.var("var_4318", dtype = "float64", shape = (11, 6))#candidate|4318|(11, 6)|var|float64
var_4319 = relay.var("var_4319", dtype = "int8", shape = ())#candidate|4319|()|var|int8
var_4320 = relay.var("var_4320", dtype = "uint8", shape = (864,))#candidate|4320|(864,)|var|uint8
output = func_4317(var_4318,var_4319,var_4320,)
func_4321 = relay.Function([var_4318,var_4319,var_4320,], output)
mutated_mod['func_4321'] = func_4321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_4330 = relay.TupleGetItem(func_2658_call(), 3)
call_4331 = relay.TupleGetItem(func_2660_call(), 3)
var_4333 = relay.var("var_4333", dtype = "float64", shape = (3, 2, 2))#candidate|4333|(3, 2, 2)|var|float64
bop_4334 = relay.logical_or(call_4330.astype('bool'), var_4333.astype('bool')) # shape=(3, 2, 2)
bop_4337 = relay.logical_or(call_4331.astype('bool'), var_4333.astype('bool')) # shape=(3, 2, 2)
uop_4344 = relay.sqrt(bop_4334.astype('float64')) # shape=(3, 2, 2)
uop_4346 = relay.sqrt(bop_4337.astype('float64')) # shape=(3, 2, 2)
func_2460_call = mod.get_global_var('func_2460')
func_2462_call = mutated_mod.get_global_var('func_2462')
const_4355 = relay.const([[8.358487],[-5.019333],[6.992520],[-4.826633],[6.624373],[-5.497525],[-6.299313],[5.801894],[1.655843],[-3.942261],[1.821509],[-1.726939],[-8.774663],[2.884377],[-8.541662],[7.320489],[3.856997],[-9.977015],[-6.369717],[-4.356405],[8.591956],[-9.149256],[-7.101696],[-0.797835]], dtype = "float64")#candidate|4355|(24, 1)|const|float64
call_4354 = relay.TupleGetItem(func_2460_call(relay.reshape(const_4355.astype('float64'), [3, 4, 2])), 0)
call_4356 = relay.TupleGetItem(func_2462_call(relay.reshape(const_4355.astype('float64'), [3, 4, 2])), 0)
const_4362 = relay.const([[[6.547640,9.057928],[-6.777635,6.742584]],[[4.479291,2.533839],[3.035874,-8.271145]],[[2.519042,-5.881973],[1.702700,-3.544205]]], dtype = "float64")#candidate|4362|(3, 2, 2)|const|float64
bop_4363 = relay.logical_xor(uop_4344.astype('int64'), relay.reshape(const_4362.astype('int64'), relay.shape_of(uop_4344))) # shape=(3, 2, 2)
bop_4366 = relay.logical_xor(uop_4346.astype('int64'), relay.reshape(const_4362.astype('int64'), relay.shape_of(uop_4346))) # shape=(3, 2, 2)
func_3670_call = mod.get_global_var('func_3670')
func_3673_call = mutated_mod.get_global_var('func_3673')
call_4380 = relay.TupleGetItem(func_3670_call(relay.reshape(const_4362.astype('float64'), [3, 2, 2])), 1)
call_4381 = relay.TupleGetItem(func_3673_call(relay.reshape(const_4362.astype('float64'), [3, 2, 2])), 1)
output = relay.Tuple([call_4354,const_4355,bop_4363,call_4380,])
output2 = relay.Tuple([call_4356,const_4355,bop_4366,call_4381,])
func_4383 = relay.Function([var_4333,], output)
mod['func_4383'] = func_4383
mod = relay.transform.InferType()(mod)
var_4384 = relay.var("var_4384", dtype = "float64", shape = (3, 2, 2))#candidate|4384|(3, 2, 2)|var|float64
output = func_4383(var_4384)
func_4385 = relay.Function([var_4384], output)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1627_call = mod.get_global_var('func_1627')
func_1629_call = mutated_mod.get_global_var('func_1629')
call_4431 = relay.TupleGetItem(func_1627_call(), 0)
call_4432 = relay.TupleGetItem(func_1629_call(), 0)
func_2608_call = mod.get_global_var('func_2608')
func_2611_call = mutated_mod.get_global_var('func_2611')
var_4435 = relay.var("var_4435", dtype = "float64", shape = (22, 3))#candidate|4435|(22, 3)|var|float64
call_4434 = relay.TupleGetItem(func_2608_call(relay.reshape(var_4435.astype('float64'), [3, 11, 2])), 0)
call_4436 = relay.TupleGetItem(func_2611_call(relay.reshape(var_4435.astype('float64'), [3, 11, 2])), 0)
uop_4438 = relay.rsqrt(var_4435.astype('float32')) # shape=(22, 3)
bop_4440 = relay.floor_divide(uop_4438.astype('float64'), relay.reshape(call_4434.astype('float64'), relay.shape_of(uop_4438))) # shape=(22, 3)
bop_4443 = relay.floor_divide(uop_4438.astype('float64'), relay.reshape(call_4436.astype('float64'), relay.shape_of(uop_4438))) # shape=(22, 3)
func_2760_call = mod.get_global_var('func_2760')
func_2763_call = mutated_mod.get_global_var('func_2763')
var_4449 = relay.var("var_4449", dtype = "float32", shape = (144,))#candidate|4449|(144,)|var|float32
call_4448 = relay.TupleGetItem(func_2760_call(relay.reshape(var_4449.astype('float32'), [144,])), 0)
call_4450 = relay.TupleGetItem(func_2763_call(relay.reshape(var_4449.astype('float32'), [144,])), 0)
output = relay.Tuple([call_4431,bop_4440,call_4448,var_4449,])
output2 = relay.Tuple([call_4432,bop_4443,call_4450,var_4449,])
func_4470 = relay.Function([var_4435,var_4449,], output)
mod['func_4470'] = func_4470
mod = relay.transform.InferType()(mod)
mutated_mod['func_4470'] = func_4470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4470_call = mutated_mod.get_global_var('func_4470')
var_4472 = relay.var("var_4472", dtype = "float64", shape = (22, 3))#candidate|4472|(22, 3)|var|float64
var_4473 = relay.var("var_4473", dtype = "float32", shape = (144,))#candidate|4473|(144,)|var|float32
call_4471 = func_4470_call(var_4472,var_4473,)
output = call_4471
func_4474 = relay.Function([var_4472,var_4473,], output)
mutated_mod['func_4474'] = func_4474
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4507 = relay.var("var_4507", dtype = "float32", shape = (3, 11, 14))#candidate|4507|(3, 11, 14)|var|float32
uop_4508 = relay.sinh(var_4507.astype('float32')) # shape=(3, 11, 14)
func_3494_call = mod.get_global_var('func_3494')
func_3496_call = mutated_mod.get_global_var('func_3496')
var_4523 = relay.var("var_4523", dtype = "int8", shape = ())#candidate|4523|()|var|int8
call_4522 = relay.TupleGetItem(func_3494_call(relay.reshape(var_4523.astype('int8'), [])), 3)
call_4524 = relay.TupleGetItem(func_3496_call(relay.reshape(var_4523.astype('int8'), [])), 3)
output = relay.Tuple([uop_4508,call_4522,var_4523,])
output2 = relay.Tuple([uop_4508,call_4524,var_4523,])
func_4525 = relay.Function([var_4507,var_4523,], output)
mod['func_4525'] = func_4525
mod = relay.transform.InferType()(mod)
var_4526 = relay.var("var_4526", dtype = "float32", shape = (3, 11, 14))#candidate|4526|(3, 11, 14)|var|float32
var_4527 = relay.var("var_4527", dtype = "int8", shape = ())#candidate|4527|()|var|int8
output = func_4525(var_4526,var_4527,)
func_4528 = relay.Function([var_4526,var_4527,], output)
mutated_mod['func_4528'] = func_4528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_4617 = relay.TupleGetItem(func_1536_call(), 0)
call_4618 = relay.TupleGetItem(func_1537_call(), 0)
output = call_4617
output2 = call_4618
func_4633 = relay.Function([], output)
mod['func_4633'] = func_4633
mod = relay.transform.InferType()(mod)
output = func_4633()
func_4634 = relay.Function([], output)
mutated_mod['func_4634'] = func_4634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_4683 = func_1299_call()
call_4684 = func_1299_call()
uop_4707 = relay.cosh(call_4683.astype('float32')) # shape=(3, 1, 2)
uop_4709 = relay.cosh(call_4684.astype('float32')) # shape=(3, 1, 2)
func_2153_call = mod.get_global_var('func_2153')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_4719 = relay.TupleGetItem(func_2153_call(), 1)
call_4720 = relay.TupleGetItem(func_2154_call(), 1)
output = relay.Tuple([uop_4707,call_4719,])
output2 = relay.Tuple([uop_4709,call_4720,])
func_4725 = relay.Function([], output)
mod['func_4725'] = func_4725
mod = relay.transform.InferType()(mod)
output = func_4725()
func_4726 = relay.Function([], output)
mutated_mod['func_4726'] = func_4726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_4730 = func_4065_call()
call_4731 = func_4065_call()
output = relay.Tuple([call_4730,])
output2 = relay.Tuple([call_4731,])
func_4744 = relay.Function([], output)
mod['func_4744'] = func_4744
mod = relay.transform.InferType()(mod)
mutated_mod['func_4744'] = func_4744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4744_call = mutated_mod.get_global_var('func_4744')
call_4745 = func_4744_call()
output = call_4745
func_4746 = relay.Function([], output)
mutated_mod['func_4746'] = func_4746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4812 = relay.var("var_4812", dtype = "int64", shape = (5, 16, 7))#candidate|4812|(5, 16, 7)|var|int64
var_4813 = relay.var("var_4813", dtype = "int64", shape = (5, 16, 7))#candidate|4813|(5, 16, 7)|var|int64
bop_4814 = relay.subtract(var_4812.astype('int64'), relay.reshape(var_4813.astype('int64'), relay.shape_of(var_4812))) # shape=(5, 16, 7)
func_4470_call = mod.get_global_var('func_4470')
func_4474_call = mutated_mod.get_global_var('func_4474')
const_4829 = relay.const([-2.704389,-7.245224,6.379900,-1.502160,3.283592,-3.959951,-4.478137,-3.013114,6.576449,7.913558,4.543900,-2.706904,0.178954,-8.999010,-9.171547,-0.699344,6.875137,4.269933,-0.069447,-4.173780,7.186216,9.504888,2.084108,-3.356986,-6.825504,4.006184,5.284104,-9.258282,-3.481160,9.755723,0.246805,-1.679845,5.065179,4.189312,7.009217,6.931008,5.975686,-7.113176,-7.851381,4.391485,5.226253,-4.668963,-6.466860,2.487817,-6.332406,1.488765,-5.923570,-9.877862,9.452471,0.576224,0.885807,8.223009,0.821543,3.997325,-7.788629,1.012169,3.694218,-4.957656,-0.977163,2.134939,6.605449,-8.424362,-4.942830,2.671053,-1.984254,-0.238130], dtype = "float64")#candidate|4829|(66,)|const|float64
const_4830 = relay.const([[-8.719262,-6.072204,-0.862799,0.598315,5.145897,-5.013359,-8.743574,5.278129,-2.706014,6.844886,0.805827,-8.307787,7.435321,2.302614,6.454014,-4.668029,-0.522771,9.690143,-0.624955,-7.326568,-6.501585,-2.280309,-8.329623,6.687211,9.409707,-7.532195,-7.765629,1.181305,-7.774311,-9.690912,-0.876641,8.984122,2.915905,7.304121,4.649652,-9.383132,-9.372035,3.896503,-2.662266,3.538788,1.000614,9.918825,8.909432,-1.462970,8.005619,9.940782,2.514095,1.323986,8.615852,-4.336006,-8.078306,-0.913799,-4.560412,3.290163,-3.893702,-6.382163,-0.460311,3.075134,-9.713041,6.244864,-0.682864,8.306313,3.131238,8.385631,2.282566,2.907375,-6.111940,1.619115,3.076885,5.131280,9.709119,-4.323274],[3.783960,6.520758,3.279081,-4.844148,2.965818,4.401696,-2.186598,3.845206,-6.567296,3.383852,-0.716742,6.816916,3.411308,8.614892,8.165009,-4.204092,-2.453376,-0.856016,-0.959728,5.259558,7.380630,-5.513423,5.817254,2.874640,-6.909760,-4.438695,7.485282,9.809752,5.459367,-9.535259,-6.188283,2.383503,-8.994274,-6.094634,-9.338516,9.686709,-0.665332,5.846449,8.178014,8.455598,8.739021,4.682885,-4.335191,6.804741,2.714802,-5.767319,-1.923211,-2.364482,7.103708,8.543281,4.506587,8.959600,-0.763825,3.188954,-4.585001,-8.209460,3.315990,-4.528872,-8.112798,0.665710,2.328723,9.976568,6.739103,0.794060,-5.604563,9.999028,8.883661,1.204753,9.688740,9.951303,6.711205,-3.315716]], dtype = "float32")#candidate|4830|(2, 72)|const|float32
call_4828 = relay.TupleGetItem(func_4470_call(relay.reshape(const_4829.astype('float64'), [22, 3]), relay.reshape(const_4830.astype('float32'), [144,]), ), 3)
call_4831 = relay.TupleGetItem(func_4474_call(relay.reshape(const_4829.astype('float64'), [22, 3]), relay.reshape(const_4830.astype('float32'), [144,]), ), 3)
output = relay.Tuple([bop_4814,call_4828,const_4829,const_4830,])
output2 = relay.Tuple([bop_4814,call_4831,const_4829,const_4830,])
func_4850 = relay.Function([var_4812,var_4813,], output)
mod['func_4850'] = func_4850
mod = relay.transform.InferType()(mod)
mutated_mod['func_4850'] = func_4850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4850_call = mutated_mod.get_global_var('func_4850')
var_4852 = relay.var("var_4852", dtype = "int64", shape = (5, 16, 7))#candidate|4852|(5, 16, 7)|var|int64
var_4853 = relay.var("var_4853", dtype = "int64", shape = (5, 16, 7))#candidate|4853|(5, 16, 7)|var|int64
call_4851 = func_4850_call(var_4852,var_4853,)
output = call_4851
func_4854 = relay.Function([var_4852,var_4853,], output)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_4898 = relay.TupleGetItem(func_1536_call(), 2)
call_4899 = relay.TupleGetItem(func_1537_call(), 2)
output = relay.Tuple([call_4898,])
output2 = relay.Tuple([call_4899,])
func_4900 = relay.Function([], output)
mod['func_4900'] = func_4900
mod = relay.transform.InferType()(mod)
output = func_4900()
func_4901 = relay.Function([], output)
mutated_mod['func_4901'] = func_4901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_4905 = relay.TupleGetItem(func_1609_call(), 0)
call_4906 = relay.TupleGetItem(func_1611_call(), 0)
func_1299_call = mod.get_global_var('func_1299')
func_1301_call = mutated_mod.get_global_var('func_1301')
call_4916 = func_1299_call()
call_4917 = func_1299_call()
func_2790_call = mod.get_global_var('func_2790')
func_2791_call = mutated_mod.get_global_var('func_2791')
call_4920 = relay.TupleGetItem(func_2790_call(), 0)
call_4921 = relay.TupleGetItem(func_2791_call(), 0)
output = relay.Tuple([call_4905,call_4916,call_4920,])
output2 = relay.Tuple([call_4906,call_4917,call_4921,])
func_4929 = relay.Function([], output)
mod['func_4929'] = func_4929
mod = relay.transform.InferType()(mod)
mutated_mod['func_4929'] = func_4929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4929_call = mutated_mod.get_global_var('func_4929')
call_4930 = func_4929_call()
output = call_4930
func_4931 = relay.Function([], output)
mutated_mod['func_4931'] = func_4931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_4995 = func_1694_call()
call_4996 = func_1694_call()
output = relay.Tuple([call_4995,])
output2 = relay.Tuple([call_4996,])
func_5002 = relay.Function([], output)
mod['func_5002'] = func_5002
mod = relay.transform.InferType()(mod)
mutated_mod['func_5002'] = func_5002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5002_call = mutated_mod.get_global_var('func_5002')
call_5003 = func_5002_call()
output = call_5003
func_5004 = relay.Function([], output)
mutated_mod['func_5004'] = func_5004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_5103 = relay.TupleGetItem(func_2658_call(), 1)
call_5104 = relay.TupleGetItem(func_2660_call(), 1)
output = call_5103
output2 = call_5104
func_5118 = relay.Function([], output)
mod['func_5118'] = func_5118
mod = relay.transform.InferType()(mod)
mutated_mod['func_5118'] = func_5118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5118_call = mutated_mod.get_global_var('func_5118')
call_5119 = func_5118_call()
output = call_5119
func_5120 = relay.Function([], output)
mutated_mod['func_5120'] = func_5120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_5157 = relay.TupleGetItem(func_1609_call(), 0)
call_5158 = relay.TupleGetItem(func_1611_call(), 0)
func_1966_call = mod.get_global_var('func_1966')
func_1968_call = mutated_mod.get_global_var('func_1968')
call_5163 = relay.TupleGetItem(func_1966_call(), 0)
call_5164 = relay.TupleGetItem(func_1968_call(), 0)
const_5176 = relay.const([[[9.605013,-6.477585],[5.339355,-5.755115],[8.464848,-0.508043],[9.370046,-4.945925],[8.538282,4.627543],[1.346680,2.246608],[9.269182,6.205249],[0.317205,9.020334],[-0.439223,-4.255008],[-7.306794,-1.115374],[-7.501322,-9.716045],[9.782189,-1.725902]],[[-7.181134,-9.589647],[-7.760145,4.664365],[-7.147564,-6.329737],[2.619583,-7.703205],[9.872545,-8.380620],[1.446277,5.017491],[2.095741,6.406172],[-1.300063,2.969598],[8.916109,-9.107681],[8.218831,-3.178107],[9.652500,6.309527],[-1.787542,-3.163066]],[[-3.854024,-4.054116],[5.140751,2.879494],[5.257019,8.995025],[2.735377,-8.701699],[-0.626996,-5.848013],[3.872125,-5.727048],[5.754618,0.777055],[2.430503,5.481440],[-3.919629,-8.864157],[1.246892,-0.153067],[-7.998360,0.988430],[-6.802245,0.219332]]], dtype = "float64")#candidate|5176|(3, 12, 2)|const|float64
bop_5177 = relay.logical_or(call_5163.astype('bool'), const_5176.astype('bool')) # shape=(3, 12, 2)
bop_5180 = relay.logical_or(call_5164.astype('bool'), const_5176.astype('bool')) # shape=(3, 12, 2)
func_1041_call = mod.get_global_var('func_1041')
func_1046_call = mutated_mod.get_global_var('func_1046')
const_5184 = relay.const([-6,-9,7,-7,-4,-7,-8,10,-10,3,-9,-6,4,-4,-1,1,3,-8,-7,-1,8,2,10,-9,-2,10,7,-4,10,-3,8,10,-3,-2,-3,-3,-2,4,9,-2,-6,-2,-10,3,6,-5,-2,-6,1,-7,-2,5,7,7,5,-7,-4,3,9,6,-3,-10,5,-10,-5,-3,9,-2,-9,2,-10,4,-2,-8,6,6,6,-6,3,1,5,6,2,-8,-7,-7,-1,-1,-10,4,6,5,6,-4,9,7,-9,-8,1,4,-8,6,-1,-4,7,-7,8,6,-5,-4,-6,-8,6,-6,2,6,2,-1,1,6,-3,-3,-6,6,-9,-4,5,-10,8,7,-7,-9,-9,3,-4,-9,1,10,1,7,-6,7,-4,2,2,-3,-4,-9,3,-2,1,5,-5,1,1,-8,-10,-10,-1,-10,2,3,6,-1,-5,5,6,10,-5,9,-9,-4,-1,7,5,-4,-1,-6,-10,3,10,1,-9,7,-4,-1,3,-3,-8,-6,-10,-3,-1,5,4,7,7,1,-3,-4,-5,9,10,4,-6,4,-5,4,-4,5,8,-5,2,-3,-4,-1,3,9,-3,3,5,5,4,4,-8,-7,3,-1,10,9,2,5,9,9,8,1,-1,3,-6,5,-8,-2,6,7,9,2,-5,7,2,7,-1,-5,-5,-10,-7,-8,-9,5,6,-3,-7,8,-1,-7,-2,5,3,8,8,10,2,10,8,9,9,-1,-5,10,4,9,10,-1,-3,2,6,-9,-1,2,-6,5,10,-4,3,-1,9,-4,3,3,-6,-7,8,3,-5,-9,3,-8,8,-10,-4,-9,-2,-6,-2,-10,6,1,3,1,10,-1,-4,7,-1,-4,-7,-9,-7,3,6,8,-3,5,-4,6,-8,6,-5,3,-10,-10,7,-6,-6,4,4,-5,-10,3,-9,-7,-5,9,5,-8,7,4,9,10,10,-1,-5,-1,9,8,-4,-6,-7,-3,-7,9,-8,9,2,-7,5,-9,4,-5,6,2,-8,1,5,10,-2,9,-10,1,10,-4,-6,5,-5,-5,-2,10,-7,-7,-4,8,4,10,-6,7,9,-2,6,-2,-6,1,4,-9,-4,-7,3,-6,1,-2,7,4,3,-10,3,-2,-9,-8,4,-7,-6,-9,-8,-6,3,9,-9,5,-10,3,-6,-2,-7,9,-8,2,-1,-2,5,9,6,-7,2,1,6,-3,8,-9,-6,6,7,7,-8,6,-7,-9,-4,9,8,-7,-3,-9,8,8,8,-9,4,2,4,-3,-6,5,-9,-5,-4,3,7,-10,10,8,-4,3,-2,7,-7,-7,3,1,8,-10,2,-2,5,-3,-2,5,7,-1,6,-5,8,-4,-5,4,-4,-6,10,-5,-1,-2,-9,-8,-8,5,9,-7,-5,-2,5,-6,2,5,-1,9,-9,5,-1,-6,4,-2,-5,-1,-9,3,-9,-5,10,-5,2,-10,-6,-1,-10,5,-10,6,-4,-6,-2,-9,7,-3,3,7,-3,-8,-4,5,6,7,-5,-1,-1,-3,7,3,-5,-10,-6,6,6,10,5,-5,3,8,6,-8,8,10,-5,-9,3,3,-8,1,-2,-5,4,9,1,-7,7,-4,1,2,8,8,-3,-1,9,9,10,-10,4,-6,-5,2,10,-8,-9,-7,-2,-6,-6,-9,8,-6,-4,7,-4,-2,3,10,1,4,-8,9,-6,8,4,4,-7,-2,-7,-6,-9,-9,-6,8,8,-9,3,-8,-3,-2,4,-8,-8,-10,7,-5,8,-1,-4,-4,-10,-9,-1,5,-3,-2,3,-8,10,6,-7,6,-5,-2,5,-1,10,-10,-9,6,10,-9,-8,3,-6,-5,-10,-10,9,5,-1,9,-8,-4,-3,-7,8,7,-4,4], dtype = "uint64")#candidate|5184|(704,)|const|uint64
var_5185 = relay.var("var_5185", dtype = "uint8", shape = (560, 1))#candidate|5185|(560, 1)|var|uint8
call_5183 = relay.TupleGetItem(func_1041_call(relay.reshape(const_5184.astype('uint64'), [16, 11, 4]), relay.reshape(const_5184.astype('uint64'), [16, 11, 4]), relay.reshape(var_5185.astype('uint8'), [560,]), ), 5)
call_5186 = relay.TupleGetItem(func_1046_call(relay.reshape(const_5184.astype('uint64'), [16, 11, 4]), relay.reshape(const_5184.astype('uint64'), [16, 11, 4]), relay.reshape(var_5185.astype('uint8'), [560,]), ), 5)
func_1438_call = mod.get_global_var('func_1438')
func_1443_call = mutated_mod.get_global_var('func_1443')
var_5193 = relay.var("var_5193", dtype = "float64", shape = (60,))#candidate|5193|(60,)|var|float64
const_5194 = relay.const([1.687702,7.106480,-1.431355,7.289749,-0.523508,5.904517,-3.473210,4.481851,6.403675,8.831787,-3.120818,-8.149161,0.858823,5.836815,2.022499,5.740807,3.268067,-2.454217,3.591437,4.218230,7.391141,-0.581323,7.021683,1.199921,-1.978799,4.481325,-7.713258,7.919650,6.902341,-5.148410,4.912329,9.596775,-6.476001,-3.321026,3.044734,-9.856377,2.811544,4.277407,-8.225944,8.137211,8.644243,-1.901196,-5.295972,9.927864,-8.688171,-4.080469,3.646514,1.545211,8.562998,3.997419,3.450422,5.322492,-4.420795,3.518575,-3.785191,5.960511,-1.211559,9.898851,-8.206559,-6.076165,7.429561,-4.672155,3.012647,-9.564350,9.727750,9.112197,3.604333,5.304730,3.763540,6.760394,7.966500,7.825945,-3.064090,-6.356857,4.730293,5.697952,-2.323623,-4.143490,3.413141,-0.223196,-6.614875,-5.617214,5.278992,-3.504610,-8.930193,-3.115884,-6.741031,9.181666,-8.052745,1.583882,0.538511,-7.102209,-3.423303,7.572298,-2.392464,5.319574,9.637144,-2.720512,9.368434,-9.199789,-4.187249,-2.459935,-4.746316,3.740331,3.455190,2.216815,-7.486745,-3.985059,-2.813011,-5.518130,-3.461506,3.230901,5.901043,-7.859808,-3.467819,6.185620,2.460658,-6.549806,9.044774,-7.926586,-2.108769,8.568406,-9.068826,-7.498519,6.709558,4.599472,-0.418533,-8.196139,-3.698908,-8.309325,6.598408,-5.457284,0.976203,-5.911556,-8.591825,-0.812682,-6.672185,7.309970,8.328938,1.681973,8.627586,-2.267699,-1.259712,3.125121], dtype = "float32")#candidate|5194|(144,)|const|float32
call_5192 = relay.TupleGetItem(func_1438_call(relay.reshape(var_5193.astype('float64'), [3, 10, 2]), relay.reshape(const_5194.astype('float32'), [1, 144]), relay.reshape(var_5185.astype('uint8'), [560,]), ), 1)
call_5195 = relay.TupleGetItem(func_1443_call(relay.reshape(var_5193.astype('float64'), [3, 10, 2]), relay.reshape(const_5194.astype('float32'), [1, 144]), relay.reshape(var_5185.astype('uint8'), [560,]), ), 1)
output = relay.Tuple([call_5157,bop_5177,call_5183,const_5184,var_5185,call_5192,var_5193,const_5194,])
output2 = relay.Tuple([call_5158,bop_5180,call_5186,const_5184,var_5185,call_5195,var_5193,const_5194,])
func_5222 = relay.Function([var_5185,var_5193,], output)
mod['func_5222'] = func_5222
mod = relay.transform.InferType()(mod)
mutated_mod['func_5222'] = func_5222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5222_call = mutated_mod.get_global_var('func_5222')
var_5224 = relay.var("var_5224", dtype = "uint8", shape = (560, 1))#candidate|5224|(560, 1)|var|uint8
var_5225 = relay.var("var_5225", dtype = "float64", shape = (60,))#candidate|5225|(60,)|var|float64
call_5223 = func_5222_call(var_5224,var_5225,)
output = call_5223
func_5226 = relay.Function([var_5224,var_5225,], output)
mutated_mod['func_5226'] = func_5226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_5251 = func_1704_call()
call_5252 = func_1704_call()
func_3116_call = mod.get_global_var('func_3116')
func_3120_call = mutated_mod.get_global_var('func_3120')
var_5264 = relay.var("var_5264", dtype = "uint8", shape = ())#candidate|5264|()|var|uint8
const_5265 = relay.const([9,4,-7,6,5,5,7,-4,-4,7,1,-6,3,2,8,-10,3,8,6,-6,-3,-8,10,5,6,3,9,-8,9,-6,3,3,-10,6,4,-7,-4,9,-5,-10,-8,8,2,-2,6,-7,4,7,-10,9,6,3,1,5,-10,-6,-10,8,10,3,9,-7,10,8,8,6,-5,5,4,-1,7,-3,-4,8,-4,-2,-1,-6,2,10,3,-3,8,-2,9,7,3,-10,-2,2,9,8,2,10,-10,-1,10,-1,3,-1,9,8,-7,-10,9,6,6,8,10,10,-10,-4,7,7,9,2,-3,1,-1,10,2,9,-9,-4,5,-10,-6,-5,2,-5,-9,10,-9,3,-1,-1,-8,1,-7,8,-8,7,5,-7,4,-9,-8,5,1,7,-1,-6,-7,6,-1,-6,-3,3,6,6,-1,-3,7,6,7,1,-4,-7,-6,-4,7,10,-4,-1,-4,-2,-3,5,2,7,9,-7,9,-3,-7,3,-9,-8,-5,-5,6,-5,-10,-1,6,-2,-8,-7,3,1,6,-5,-9,8,-2,5,2,-8,-4,7,-9,-4,-9,5,10,-3,-1,1,-3,-6,-6,4,-2,-10,-3,8,-7,-10,-5,8,10,4,-2,-3,-8,2,1,9,8,2,6,5,6,10,10,-9,-1,-4,-9,-10,8,-10,7,4,1,-9,8,2,1,7,10,-4,8,6,6,4,-7,5,-4,-9,7,-3,2,-10,5,-4,1,8,7,9,-9,9,9,-7,-3,9,-4,6,6,-1,-1,-8,5,6,-1,5,-9,-5,6,-3,-10,-10,5,-4,-10,-1,-2,-7,-8,-6,9,-8,-6,7,9,-3,-10,-5,7,-5,-4,1,-9,10,-3,-6,-10,9,9,5,5,7,1,2,1,6,-6,-1,5,-2,-8,1,5,3,7,4,-8,-9,4,6,1,-3,6,3,3,-2,-6,-10,-2,-4,3,-2,10,-9,-5,2,-4,2,-6,3,-10,4,-9,-6,-9,1,8,-2,-5,3,-3,-5,-9,-9,1,6,-9,7,5,9,6,6,5,4,-7,9,1,7,10,5,-9,3,1,6,-5,-10,8,5,-3,3,-6,-2,-8,-7,6,-10,-4,3,-4,9,-7,-2,-6,6,6,1,-2,8,-3,-8,10,-6,-2,-8,-9,10,10,8,-7,-5,-6,6,9,-9,1,-3,-7,5,-5,8,2,9,7,5,-4,8,9,7,10,-2,5,-3,-2,2,1,-3,-7,4,4,10,4,-7,4,10,-1,-6,-8,9,-7,-7,-10,-3,5,-10,1,-8,-10,9,-10,-7,-3,-9,1,-1,8,9,10,-6,-1,5,-6,8,-7,-1,6,-2,-2,8,-1,-2,-8,-9,-2,3,-1,7,3,-7,-2,7,-8,-7,-2,-6,5,-1,10,9,-7,7,-5,7,-2,6,3,-4,-4,3,-5,8,6,2,9,10,-8,-4,-3,-8,-5,1,-2,9,5,2,1,-1,-9,-5,-6,6,1,-4,-3,3,9,-8,-10,-6,8,-6,-10,-6,-10,1,5,8,1,4,4,-4,3,3,8,8,-7,-5,-9,-10,-5,5,-8,7,4,-3,-1,1,-6,7,2,-2,-10,-10,9,10,-8,-3,7,-8,-3,7,-8,8,-3,-10,10,5,-8,-1,-2,-2,-7,9,-6,2,7,-3,-10,-9,-6,9,8,8,-9,-4,9,3,10,9,-8,7,-4,8,-1,-8,-7,-3,-9,2,9,8,1,-5,3,9,6,-7,-6,4,-4,-6,-7,8,1,5,6,-9,5,10,-7,9,6,-2,3,-4,8,7,-9,5,-5,-10,-6,-9,-3,10,9,3,-7,2,3,-6,5,10,8,-4,6,3,-4,-2,3,-9,1,-10,9,8,-9,4,-10,6,8,3,5,-5,-10,6,-8,6,6,-2,1,6,-6,1,-3,-4,-8,-6,-4,-4,7,-8,4,8,3,5,-10,3,1,10,3,-4,2,6,10,-2,9,-4,7,2,-2,3,10,-5,-10,-5,-2,5,-1,-2,10,-10,8,-1,5,-5,2,10,6,3,2,-10,-8,-10,6,10,8,5,3,10,-9,7,-7,-3,2,-10,3,1,-4,2,5,-8,-1,8,8,4,-5,9,9,2,10,-10,-3,-6,-3,9,-10,8,9,-5,-6,-4,-3,-10,7,-4,5,9,4,-4,-4,3,-9,5,-9,-5,-1,-5,-4,-7,-8,-7,4,10,3,-6,-7,3,2,-4,-8,7,5,-6,-6,9,5,-4,6,-8,9,8,-5,-2,8,-9,2,-10,7,-8,-8,-6,5,-1,-5,9], dtype = "uint8")#candidate|5265|(864,)|const|uint8
call_5263 = relay.TupleGetItem(func_3116_call(relay.reshape(var_5264.astype('uint8'), []), relay.reshape(const_5265.astype('uint8'), [6, 12, 12]), ), 0)
call_5266 = relay.TupleGetItem(func_3120_call(relay.reshape(var_5264.astype('uint8'), []), relay.reshape(const_5265.astype('uint8'), [6, 12, 12]), ), 0)
func_3116_call = mod.get_global_var('func_3116')
func_3120_call = mutated_mod.get_global_var('func_3120')
call_5268 = relay.TupleGetItem(func_3116_call(relay.reshape(var_5264.astype('uint8'), []), relay.reshape(const_5265.astype('uint8'), [6, 12, 12]), ), 0)
call_5269 = relay.TupleGetItem(func_3120_call(relay.reshape(var_5264.astype('uint8'), []), relay.reshape(const_5265.astype('uint8'), [6, 12, 12]), ), 0)
func_4470_call = mod.get_global_var('func_4470')
func_4474_call = mutated_mod.get_global_var('func_4474')
var_5272 = relay.var("var_5272", dtype = "float32", shape = (144, 1))#candidate|5272|(144, 1)|var|float32
call_5271 = relay.TupleGetItem(func_4470_call(relay.reshape(call_5251.astype('float64'), [22, 3]), relay.reshape(var_5272.astype('float32'), [144,]), ), 0)
call_5273 = relay.TupleGetItem(func_4474_call(relay.reshape(call_5251.astype('float64'), [22, 3]), relay.reshape(var_5272.astype('float32'), [144,]), ), 0)
bop_5274 = relay.right_shift(call_5263.astype('int32'), relay.reshape(call_5268.astype('int32'), relay.shape_of(call_5263))) # shape=(6, 12, 12)
bop_5277 = relay.right_shift(call_5266.astype('int32'), relay.reshape(call_5269.astype('int32'), relay.shape_of(call_5266))) # shape=(6, 12, 12)
output = relay.Tuple([call_5251,var_5264,const_5265,call_5271,var_5272,bop_5274,])
output2 = relay.Tuple([call_5252,var_5264,const_5265,call_5273,var_5272,bop_5277,])
func_5279 = relay.Function([var_5264,var_5272,], output)
mod['func_5279'] = func_5279
mod = relay.transform.InferType()(mod)
mutated_mod['func_5279'] = func_5279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5279_call = mutated_mod.get_global_var('func_5279')
var_5281 = relay.var("var_5281", dtype = "uint8", shape = ())#candidate|5281|()|var|uint8
var_5282 = relay.var("var_5282", dtype = "float32", shape = (144, 1))#candidate|5282|(144, 1)|var|float32
call_5280 = func_5279_call(var_5281,var_5282,)
output = call_5280
func_5283 = relay.Function([var_5281,var_5282,], output)
mutated_mod['func_5283'] = func_5283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1966_call = mod.get_global_var('func_1966')
func_1968_call = mutated_mod.get_global_var('func_1968')
call_5311 = relay.TupleGetItem(func_1966_call(), 0)
call_5312 = relay.TupleGetItem(func_1968_call(), 0)
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
const_5318 = relay.const([[-8,6,7,8,8,-5,-1,2,-7,-5,1,4,2,-1],[-5,10,10,-3,7,-6,-5,-6,3,4,-7,9,-4,-9],[2,-3,-7,-2,8,3,-5,2,10,-10,-6,-3,3,2],[-2,4,-2,-10,-2,5,8,-7,1,-4,-9,-5,9,1],[-9,-1,-5,8,-4,6,1,-7,-1,3,-6,-2,1,2],[-7,-4,-6,-1,2,6,-8,-1,6,-9,2,9,-10,1],[-10,3,-3,-6,-4,10,4,9,10,2,-7,3,2,-7],[6,-6,-10,4,6,4,6,-5,10,2,-3,6,-5,1],[-2,2,6,-4,6,2,9,1,10,8,9,1,-4,4],[-7,-9,-3,7,-8,6,1,6,-3,-7,-3,6,5,-6],[6,10,-6,4,-3,-9,-4,-5,-2,-6,9,10,8,-8],[3,2,5,-5,-5,10,-2,9,1,-2,6,-8,3,1],[-3,-4,2,-8,-10,-7,1,-2,-4,8,6,8,2,-1],[3,-6,-2,3,-8,2,-1,4,-6,-5,-1,8,7,-1],[4,-3,5,-1,4,2,2,-2,3,-7,4,1,-8,-3],[7,-3,-6,-7,-10,8,2,-3,-2,-1,1,-5,-1,2],[-9,4,9,-6,8,5,-4,9,1,-4,9,1,5,-6],[-4,6,3,9,1,-4,1,-6,-2,-2,-9,7,2,-9],[-4,3,-5,-3,-3,10,-10,-3,-6,7,-4,-3,7,-2],[-8,8,-9,-1,-2,-5,-9,-10,-3,-9,4,1,6,4],[3,-4,8,-4,3,-3,2,-3,-7,9,8,3,5,-1],[-5,6,-10,1,-2,-6,2,1,9,4,-7,-10,-2,-6],[-4,-10,1,-8,-8,-8,2,5,-3,-10,2,-2,7,-3],[-2,6,5,6,-3,6,1,-10,-8,-9,-5,5,4,-6],[7,2,8,5,3,1,6,-5,-1,-2,-4,-10,-1,-6],[-10,6,2,9,5,5,-7,-3,-4,-10,7,-4,4,-2],[8,-9,-10,8,-2,-4,-2,6,9,-2,10,-8,5,-10],[5,-3,-9,3,-9,3,-7,8,-10,-9,-4,10,7,2],[1,3,1,-10,10,10,-4,9,-10,1,1,-8,2,-10],[-7,1,4,7,9,6,1,-7,10,6,-4,1,6,-2],[-7,-9,5,-6,5,-4,1,6,-7,4,-10,9,-7,3],[8,-6,-10,-1,7,3,9,8,1,-1,-6,8,-7,-4],[-7,-10,2,2,-2,-6,10,-3,-1,10,-5,-2,8,-9],[-7,1,-9,9,-8,-1,1,9,9,2,-1,1,5,-8],[-3,8,-1,-2,-2,10,-1,8,10,-5,7,8,2,-5],[3,10,2,6,6,4,8,-8,6,-2,1,-7,5,-10],[7,3,-1,-7,-8,-8,10,4,7,8,-8,-2,-6,-9],[6,-9,7,4,3,-10,-4,-9,10,2,-5,-1,-1,-2],[-3,9,2,-4,-9,4,-10,5,5,-8,-7,-2,-3,5],[-7,-2,-10,10,10,-9,-4,1,9,10,1,-7,-2,-3]], dtype = "uint8")#candidate|5318|(40, 14)|const|uint8
call_5317 = relay.TupleGetItem(func_2845_call(relay.reshape(const_5318.astype('uint8'), [560,])), 0)
call_5319 = relay.TupleGetItem(func_2847_call(relay.reshape(const_5318.astype('uint8'), [560,])), 0)
bop_5328 = relay.less(call_5311.astype('bool'), relay.reshape(call_5317.astype('bool'), relay.shape_of(call_5311))) # shape=(3, 1, 2)
bop_5331 = relay.less(call_5312.astype('bool'), relay.reshape(call_5319.astype('bool'), relay.shape_of(call_5312))) # shape=(3, 1, 2)
func_1574_call = mod.get_global_var('func_1574')
func_1579_call = mutated_mod.get_global_var('func_1579')
const_5337 = relay.const([8.400736,-8.320488,-4.253375,2.334564,-2.068144,-5.740735,6.523150,-5.998821,-9.600939,-8.186430,3.825338,2.991840,-3.105526,0.635040,-2.517181,2.911923,4.768347,-9.921798,-4.540275,0.992971,0.510507,-1.861493,-7.328796,9.364357,-6.829958,-0.072750,2.924750,-9.898886,8.581311,-8.457847,-2.175667,3.195822,6.185974,8.024995,8.989691,-5.983619,7.859175,-2.801355,8.765189,-1.625196,8.864495,7.754183,9.922239,-7.892181,3.927887,-1.938090,-4.008957,-6.005235,7.600421,1.847018,-4.298804,0.060971,8.378269,-4.862139,1.908886,-1.563063,9.944292,-9.506811,-0.026696,2.677437,9.642759,9.720514,-5.503789,7.149994,-3.959565,-6.208364,-0.010148,-1.019638,9.619851,-9.898708,4.837042,4.694930,-7.415938,5.360464,5.447370,4.640234,-8.091764,-1.336761,-9.451640,2.895904,6.992392,3.735167,9.930946,5.429147,-2.683352,-0.899346,-2.070088,-5.901291,0.857091,7.006541], dtype = "float64")#candidate|5337|(90,)|const|float64
const_5338 = relay.const([-3.213297,7.225181,0.871618,5.630024,-4.832424,-5.820618,-5.831655,2.993703,-1.793777,-4.817673,-9.791199,7.404964,-6.042403,-1.252621,-0.685399,-5.111943,7.172899,-2.738534,-1.234360,-8.100056,1.540645,-3.919750,0.756339,-7.386558,7.191124,2.637202,-6.841271,-8.208479,6.236541,-9.374007,2.099003,-2.323705,-0.982764,0.493849,-3.674283,9.893825,-4.722637,9.257523,8.521290,4.052459,8.283024,-4.741414,5.745482,-8.470251,-9.334235,3.203771,6.792868,-5.687039,-5.067540,-8.393051,4.173886,-0.802653,4.931669,-4.504051,1.018875,-5.065069,-5.450583,-7.661542,0.287898,-9.938386], dtype = "float64")#candidate|5338|(60,)|const|float64
const_5339 = relay.const([2.167196,-1.351576,3.160342,-8.248006,-6.442154,-8.395206,4.536440,-2.656141,-5.038858,2.822247,-8.604370,4.111077,-6.536534,2.301900,1.962977,6.138974,-1.771774,-2.271548,-3.753911,1.308526,-0.305180,7.960435,-8.907267,-9.260296,-7.066363,6.422126,-5.090468,-5.417026,-6.860272,-0.096809,-1.753241,-3.249947,-5.993004,-2.281026,8.808975,5.742373,0.366873,1.121910,3.561003,-5.477941,2.798270,-1.585364,-2.220452,5.402419,-4.825308,-9.571395,8.414696,7.168401,-2.595204,-5.574005,3.566731,8.355614,-4.814461,-9.918533,-3.699135,6.762187,-3.852008,4.895959,-9.595279,2.702165,9.402314,0.059596,-0.694670,-5.247716,-7.012152,1.852800,-6.119653,-3.193267,2.398497,-0.930480,-2.145600,-4.979778,4.278636,7.143749,-9.443262,-1.043499,7.570160,-1.932563,4.617060,-3.132010,1.459560,4.966899,-4.963936,0.540453,5.633641,1.941990,2.965428,-3.547510,-1.737181,7.738523,5.928218,-0.719784,7.712362,-3.840480,4.163796,3.509114,-9.296483,-9.267780,-6.180991,0.205389,-4.822043,7.651338,-0.746570,-0.598172,-2.210756,1.830999,-1.798630,-5.443602,-2.839288,-6.669175,2.659537,-1.444425,-9.012539,-8.699167,-7.418035,-7.656883,-7.678065,9.579718,-5.920722,7.777011,9.853068,-7.699548,-1.498503,7.848804,9.117301,-8.080301,3.609827,3.631391,-4.066983,3.765790,8.263929,0.513102,4.750523,-1.879503,-7.933975,-1.222354,-7.519680,9.519154,1.651983,1.488205,-9.988358,0.090723,-7.652859,-7.017914], dtype = "float32")#candidate|5339|(144,)|const|float32
call_5336 = relay.TupleGetItem(func_1574_call(relay.reshape(const_5337.astype('float64'), [3, 15, 2]), relay.reshape(const_5337.astype('float64'), [3, 15, 2]), relay.reshape(const_5338.astype('float64'), [1, 60]), relay.reshape(const_5339.astype('float32'), [144,]), ), 5)
call_5340 = relay.TupleGetItem(func_1579_call(relay.reshape(const_5337.astype('float64'), [3, 15, 2]), relay.reshape(const_5337.astype('float64'), [3, 15, 2]), relay.reshape(const_5338.astype('float64'), [1, 60]), relay.reshape(const_5339.astype('float32'), [144,]), ), 5)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_5357 = relay.TupleGetItem(func_1803_call(), 0)
call_5358 = relay.TupleGetItem(func_1805_call(), 0)
func_4725_call = mod.get_global_var('func_4725')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_5377 = relay.TupleGetItem(func_4725_call(), 0)
call_5378 = relay.TupleGetItem(func_4726_call(), 0)
output = relay.Tuple([const_5318,bop_5328,call_5336,const_5337,const_5338,const_5339,call_5357,call_5377,])
output2 = relay.Tuple([const_5318,bop_5331,call_5340,const_5337,const_5338,const_5339,call_5358,call_5378,])
func_5380 = relay.Function([], output)
mod['func_5380'] = func_5380
mod = relay.transform.InferType()(mod)
mutated_mod['func_5380'] = func_5380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5380_call = mutated_mod.get_global_var('func_5380')
call_5381 = func_5380_call()
output = call_5381
func_5382 = relay.Function([], output)
mutated_mod['func_5382'] = func_5382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_5523 = relay.TupleGetItem(func_2870_call(), 0)
call_5524 = relay.TupleGetItem(func_2871_call(), 0)
func_3258_call = mod.get_global_var('func_3258')
func_3260_call = mutated_mod.get_global_var('func_3260')
call_5540 = func_3258_call()
call_5541 = func_3258_call()
func_2845_call = mod.get_global_var('func_2845')
func_2847_call = mutated_mod.get_global_var('func_2847')
const_5568 = relay.const([5,1,7,-8,2,3,10,2,1,-7,9,7,1,-5,4,-3,-7,-7,-4,9,-10,4,6,-3,1,-10,-4,-8,-4,10,-5,6,-9,-8,7,-9,-10,1,8,3,-4,8,1,-4,1,4,7,7,3,7,3,-1,10,8,-5,-7,-3,6,-3,8,4,-1,2,-5,3,8,-1,-10,-2,8,7,-6,-10,-6,-5,-8,-8,10,-7,8,-10,-10,5,1,-6,5,-4,-8,5,9,10,-1,-6,-10,-9,-7,-5,9,4,-7,8,-6,5,7,9,10,-3,8,1,4,-6,-8,-7,1,6,4,2,-8,-5,6,3,3,-6,-7,1,-8,4,10,-2,3,-2,4,8,-2,-1,6,4,-1,-10,-9,2,2,1,5,4,3,-6,2,1,4,-10,-5,10,5,4,3,-1,-2,-6,8,-5,-5,-8,-5,-9,-8,-9,-5,8,-9,6,-10,4,1,-9,9,10,6,-1,4,10,-2,6,8,-1,-10,-8,6,-10,-3,6,4,-5,3,-1,-9,10,10,9,3,4,7,-4,5,1,-5,-9,2,-9,-4,-3,-1,-2,-10,8,3,9,-5,4,-6,-7,2,2,-4,1,1,-8,-7,-3,5,2,-3,-9,-3,8,10,2,3,-7,7,2,-10,-10,3,5,5,6,-10,6,-10,5,-10,-1,3,8,4,7,2,-2,-3,1,-4,-7,3,-10,-10,2,-3,2,3,-5,-4,2,2,-9,10,-4,-8,-1,-8,6,5,7,3,4,-3,-2,3,-1,9,-9,-1,-5,8,9,-8,-4,-5,1,-2,3,-5,-2,-10,-1,-4,-7,-7,-3,-10,-1,-9,1,7,1,6,7,-10,8,-4,10,3,-3,2,5,8,10,2,1,-3,9,8,-1,-6,10,-1,-8,-8,5,6,-3,10,2,-5,9,5,9,5,10,10,3,-10,6,-3,9,-4,4,4,-4,-8,8,5,5,-7,3,-6,-9,-9,-4,9,-4,6,5,-3,-10,5,4,-5,-2,-3,10,-3,-6,5,5,-7,-6,-6,-4,1,-1,4,-6,4,1,-3,9,-1,8,-8,9,3,-8,-6,1,-8,6,8,1,10,-9,5,10,-4,-2,-3,-8,6,-7,-8,-2,1,-8,-9,-8,3,3,9,3,-2,-8,6,3,-3,4,9,10,3,-6,9,1,-5,-9,8,8,7,-6,3,4,-10,-7,-2,6,5,8,-7,-5,3,-5,-7,4,-10,-8,-2,8,9,-10,4,-8,7,2,-5,4,-4,3,-3,-7,1,-7,6,-4,1,-7,9,4,1,2,7,-8,-7,2,9,-7,3,-3,7,5,3,-5,-9,-10,6,-8,8,-2,8,8,-3,10,-9,6,-2,6,-5,8,1,-4,-8,10,2,-4,5,-10,9,6,-4,-5,-5,2,3,4,5,-1,-2,-2,2,-7,-10,-7,8,6,-6,-10,2,-3,-1,-9,6,-1,10,5,3,-10,8,1,-1,-9,8,9,1], dtype = "uint8")#candidate|5568|(560,)|const|uint8
call_5567 = relay.TupleGetItem(func_2845_call(relay.reshape(const_5568.astype('uint8'), [560,])), 0)
call_5569 = relay.TupleGetItem(func_2847_call(relay.reshape(const_5568.astype('uint8'), [560,])), 0)
func_3308_call = mod.get_global_var('func_3308')
func_3311_call = mutated_mod.get_global_var('func_3311')
var_5571 = relay.var("var_5571", dtype = "bool", shape = (1920,))#candidate|5571|(1920,)|var|bool
call_5570 = func_3308_call(relay.reshape(var_5571.astype('bool'), [16, 8, 15]), relay.reshape(var_5571.astype('bool'), [16, 8, 15]), )
call_5572 = func_3308_call(relay.reshape(var_5571.astype('bool'), [16, 8, 15]), relay.reshape(var_5571.astype('bool'), [16, 8, 15]), )
output = relay.Tuple([call_5523,call_5540,call_5567,const_5568,call_5570,var_5571,])
output2 = relay.Tuple([call_5524,call_5541,call_5569,const_5568,call_5572,var_5571,])
func_5584 = relay.Function([var_5571,], output)
mod['func_5584'] = func_5584
mod = relay.transform.InferType()(mod)
mutated_mod['func_5584'] = func_5584
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5585 = relay.var("var_5585", dtype = "bool", shape = (1920,))#candidate|5585|(1920,)|var|bool
func_5584_call = mutated_mod.get_global_var('func_5584')
call_5586 = func_5584_call(var_5585)
output = call_5586
func_5587 = relay.Function([var_5585], output)
mutated_mod['func_5587'] = func_5587
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5670 = relay.var("var_5670", dtype = "float32", shape = (9, 5, 15))#candidate|5670|(9, 5, 15)|var|float32
uop_5671 = relay.log(var_5670.astype('float32')) # shape=(9, 5, 15)
output = uop_5671
output2 = uop_5671
func_5677 = relay.Function([var_5670,], output)
mod['func_5677'] = func_5677
mod = relay.transform.InferType()(mod)
mutated_mod['func_5677'] = func_5677
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5678 = relay.var("var_5678", dtype = "float32", shape = (9, 5, 15))#candidate|5678|(9, 5, 15)|var|float32
func_5677_call = mutated_mod.get_global_var('func_5677')
call_5679 = func_5677_call(var_5678)
output = call_5679
func_5680 = relay.Function([var_5678], output)
mutated_mod['func_5680'] = func_5680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_5682 = relay.TupleGetItem(func_3827_call(), 0)
call_5683 = relay.TupleGetItem(func_3829_call(), 0)
func_4725_call = mod.get_global_var('func_4725')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_5689 = relay.TupleGetItem(func_4725_call(), 1)
call_5690 = relay.TupleGetItem(func_4726_call(), 1)
output = relay.Tuple([call_5682,call_5689,])
output2 = relay.Tuple([call_5683,call_5690,])
func_5693 = relay.Function([], output)
mod['func_5693'] = func_5693
mod = relay.transform.InferType()(mod)
output = func_5693()
func_5694 = relay.Function([], output)
mutated_mod['func_5694'] = func_5694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_5719 = relay.TupleGetItem(func_3827_call(), 0)
call_5720 = relay.TupleGetItem(func_3829_call(), 0)
func_1686_call = mod.get_global_var('func_1686')
func_1689_call = mutated_mod.get_global_var('func_1689')
var_5726 = relay.var("var_5726", dtype = "uint8", shape = (560,))#candidate|5726|(560,)|var|uint8
call_5725 = relay.TupleGetItem(func_1686_call(relay.reshape(var_5726.astype('uint8'), [560,])), 2)
call_5727 = relay.TupleGetItem(func_1689_call(relay.reshape(var_5726.astype('uint8'), [560,])), 2)
output = relay.Tuple([call_5719,call_5725,var_5726,])
output2 = relay.Tuple([call_5720,call_5727,var_5726,])
func_5730 = relay.Function([var_5726,], output)
mod['func_5730'] = func_5730
mod = relay.transform.InferType()(mod)
mutated_mod['func_5730'] = func_5730
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5731 = relay.var("var_5731", dtype = "uint8", shape = (560,))#candidate|5731|(560,)|var|uint8
func_5730_call = mutated_mod.get_global_var('func_5730')
call_5732 = func_5730_call(var_5731)
output = call_5732
func_5733 = relay.Function([var_5731], output)
mutated_mod['func_5733'] = func_5733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4900_call = mod.get_global_var('func_4900')
func_4901_call = mutated_mod.get_global_var('func_4901')
call_5760 = relay.TupleGetItem(func_4900_call(), 0)
call_5761 = relay.TupleGetItem(func_4901_call(), 0)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_5769 = relay.TupleGetItem(func_1609_call(), 0)
call_5770 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([call_5760,call_5769,])
output2 = relay.Tuple([call_5761,call_5770,])
func_5776 = relay.Function([], output)
mod['func_5776'] = func_5776
mod = relay.transform.InferType()(mod)
output = func_5776()
func_5777 = relay.Function([], output)
mutated_mod['func_5777'] = func_5777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_5837 = func_2231_call()
call_5838 = func_2231_call()
func_5693_call = mod.get_global_var('func_5693')
func_5694_call = mutated_mod.get_global_var('func_5694')
call_5846 = relay.TupleGetItem(func_5693_call(), 1)
call_5847 = relay.TupleGetItem(func_5694_call(), 1)
func_1907_call = mod.get_global_var('func_1907')
func_1910_call = mutated_mod.get_global_var('func_1910')
const_5861 = relay.const([[-8.278953,2.252258,9.832092,0.205723,9.898479,8.152211,-8.221530,-7.273448,0.212712,-7.202113,4.027526,9.935051,9.414395,-0.621681,4.319479,-9.837797,-1.437679,2.462235,1.642006,-5.570407,8.336888,-4.951884,6.374724,5.283530,-7.763169,4.682673,5.364493,1.342977,7.241842,5.908669,-9.025445,1.060901,2.784836,-4.483581,6.196332,-9.499870,4.539588,-2.254840,4.687212,2.383507,-5.743256,-7.205671,8.041922,-2.024153,7.199376,8.484746,5.887340,5.447858,4.378475,7.106556,-5.617024,9.487252,4.406194,-9.976963,4.489900,-6.833696,-3.622300,-8.302793,-0.748225,1.650557,-9.949382,-3.608291,6.412031,-3.901287,3.085611,9.124758,4.784850,3.832810,8.833673,-0.801767,3.161768,-8.417465,6.828339,0.237658,4.075959,8.579723,6.432129,3.367511,7.837124,0.825474,-9.472915,5.637635,6.223006,-3.351490,-0.645026,-4.082387,1.109556,-0.972008,7.347821,4.370753,-7.224602,-8.586508,-1.864029,-1.357493,0.396671,-1.449647,-3.505948,-0.689294,3.548841,-3.378589,2.913833,8.155650,2.726269,3.457427,-4.280560,4.811170,4.769828,-9.623080,-3.615904,-7.952750,0.125164,1.165466,-9.248140,2.741266,-3.120475,1.929495,-4.483521,-0.020862,-3.811611,-0.253035,-9.210161,5.748405,8.675717,8.339824,-3.112043,-6.487138,0.717196,-8.483779,1.409533,4.620385,2.903517,1.589299,4.697557,-8.454004,4.374418,-1.071548,-6.763959,2.411589,-0.999917,5.521612,-1.858175,-1.101856,4.706562,9.850861]], dtype = "float32")#candidate|5861|(1, 144)|const|float32
var_5862 = relay.var("var_5862", dtype = "uint8", shape = (1728,))#candidate|5862|(1728,)|var|uint8
call_5860 = relay.TupleGetItem(func_1907_call(relay.reshape(const_5861.astype('float32'), [1, 144]), relay.reshape(var_5862.astype('uint8'), [12, 144]), ), 8)
call_5863 = relay.TupleGetItem(func_1910_call(relay.reshape(const_5861.astype('float32'), [1, 144]), relay.reshape(var_5862.astype('uint8'), [12, 144]), ), 8)
output = relay.Tuple([call_5837,call_5846,call_5860,const_5861,var_5862,])
output2 = relay.Tuple([call_5838,call_5847,call_5863,const_5861,var_5862,])
func_5864 = relay.Function([var_5862,], output)
mod['func_5864'] = func_5864
mod = relay.transform.InferType()(mod)
var_5865 = relay.var("var_5865", dtype = "uint8", shape = (1728,))#candidate|5865|(1728,)|var|uint8
output = func_5864(var_5865)
func_5866 = relay.Function([var_5865], output)
mutated_mod['func_5866'] = func_5866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2658_call = mod.get_global_var('func_2658')
func_2660_call = mutated_mod.get_global_var('func_2660')
call_5916 = relay.TupleGetItem(func_2658_call(), 2)
call_5917 = relay.TupleGetItem(func_2660_call(), 2)
output = relay.Tuple([call_5916,])
output2 = relay.Tuple([call_5917,])
func_5918 = relay.Function([], output)
mod['func_5918'] = func_5918
mod = relay.transform.InferType()(mod)
output = func_5918()
func_5919 = relay.Function([], output)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1966_call = mod.get_global_var('func_1966')
func_1968_call = mutated_mod.get_global_var('func_1968')
call_5946 = relay.TupleGetItem(func_1966_call(), 0)
call_5947 = relay.TupleGetItem(func_1968_call(), 0)
output = relay.Tuple([call_5946,])
output2 = relay.Tuple([call_5947,])
func_5956 = relay.Function([], output)
mod['func_5956'] = func_5956
mod = relay.transform.InferType()(mod)
output = func_5956()
func_5957 = relay.Function([], output)
mutated_mod['func_5957'] = func_5957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3730_call = mod.get_global_var('func_3730')
func_3732_call = mutated_mod.get_global_var('func_3732')
call_6047 = relay.TupleGetItem(func_3730_call(), 0)
call_6048 = relay.TupleGetItem(func_3732_call(), 0)
output = call_6047
output2 = call_6048
func_6051 = relay.Function([], output)
mod['func_6051'] = func_6051
mod = relay.transform.InferType()(mod)
mutated_mod['func_6051'] = func_6051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6051_call = mutated_mod.get_global_var('func_6051')
call_6052 = func_6051_call()
output = call_6052
func_6053 = relay.Function([], output)
mutated_mod['func_6053'] = func_6053
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4900_call = mod.get_global_var('func_4900')
func_4901_call = mutated_mod.get_global_var('func_4901')
call_6062 = relay.TupleGetItem(func_4900_call(), 0)
call_6063 = relay.TupleGetItem(func_4901_call(), 0)
func_4317_call = mod.get_global_var('func_4317')
func_4321_call = mutated_mod.get_global_var('func_4321')
const_6069 = relay.const(-2, dtype = "int8")#candidate|6069|()|const|int8
const_6070 = relay.const([8,4,10,6,7,-2,5,7,3,3,-2,-1,-10,6,-1,-10,8,-10,8,-10,1,-9,-6,-10,-2,2,2,6,10,-3,-2,-9,-7,-7,-6,1,1,-6,8,7,-1,-3,-4,2,-2,-4,-8,-3,3,1,8,-7,-1,5,8,-1,-1,-1,-3,9,-10,10,-6,-2,-4,8,-2,-1,7,4,10,-6,10,-5,2,10,5,-7,-4,1,1,-2,-4,8,10,9,-7,-10,4,-2,9,6,4,6,4,6,9,-8,2,6,-8,-2,2,2,9,-2,-7,-4,-4,9,-10,-3,2,3,5,-5,-6,10,1,6,7,10,-8,5,7,-2,-6,7,6,1,1,6,5,7,-7,7,3,-8,-4,-5,-6,7,3,1,5,-5,-9,4,-7,3,-4,-10,10,9,2,4,-2,1,6,-7,5,7,-2,-2,-10,7,-5,-2,-8,8,7,-9,2,6,-1,1,6,-3,-7,-1,8,-2,6,8,6,-3,6,2,1,10,-5,-9,-6,-1,-5,-1,-8,-6,8,-8,9,-7,-3,-5,-9,6,5,-4,8,-4,-6,6,10,10,-7,10,10,-1,6,-7,2,-8,-9,-7,-8,9,-8,9,8,-3,10,1,3,-2,1,-6,3,9,8,8,-1,-9,-2,6,-10,7,4,-7,-1,6,10,-4,-7,4,10,-1,-7,-9,-9,-10,-6,8,-6,-7,-5,8,6,-8,-4,-8,4,-7,-10,-1,3,-9,-10,-9,1,1,10,3,1,10,-4,4,-10,9,9,-2,-1,3,7,6,-7,-5,-8,4,-8,5,-5,-9,9,-6,8,-3,6,-10,8,-2,-7,-4,3,-2,-4,-4,5,-3,-1,-5,6,10,5,-6,8,-10,5,9,3,1,-10,6,10,2,-10,-4,6,-2,-4,6,8,-6,-1,1,6,-9,10,-2,9,-6,2,7,2,10,8,7,-3,9,7,6,-5,-2,2,-7,-7,-10,-1,-6,6,10,-4,-2,-9,9,-4,-3,-1,3,-8,-4,3,5,-3,-10,9,-5,-6,-9,9,-3,2,3,1,-7,-8,4,-5,7,2,-8,-7,5,1,8,-2,4,-7,5,3,-4,3,2,9,-7,-7,3,10,-5,1,-1,-4,-7,2,-8,-4,-5,4,-8,-7,5,1,-7,-7,-10,-6,1,7,-3,-10,5,-7,4,8,-4,6,-8,-7,-6,7,-5,10,-5,4,6,-10,9,-1,-7,-4,3,-2,6,6,-6,-1,-8,-4,8,10,3,4,7,6,4,7,-9,8,8,1,-9,-4,-3,-7,-8,4,-8,5,6,9,1,-7,7,-8,-1,9,-1,-4,-3,5,9,5,10,3,1,-7,-10,-5,-2,-1,3,-5,-5,1,2,-1,7,-8,-6,-4,5,-1,8,9,8,6,-2,-6,-10,6,2,4,-3,-8,-5,10,-8,4,-5,-9,-5,-4,6,3,-6,-7,-6,10,5,-2,2,10,-1,7,7,8,-9,-8,-2,-10,-8,7,-9,-5,6,-3,-7,10,7,-5,3,6,-6,8,3,-6,-4,7,1,6,-9,-6,3,-6,5,-5,-5,-10,-3,-10,-6,-9,1,-4,10,-10,2,-7,3,-5,7,7,-9,6,5,8,2,2,3,-8,7,-4,-5,1,-8,-6,-4,-8,8,-5,-10,4,10,7,-1,10,4,-4,7,-5,-2,2,4,1,6,4,-10,-7,-4,8,3,1,2,-4,-1,-5,-2,10,-9,-5,-8,-10,-9,1,-3,-9,6,4,3,8,9,-6,-2,-4,-9,5,-1,-8,-2,-4,-9,-3,-10,5,-5,9,6,-2,4,-9,-8,-10,7,-9,-8,-6,-5,2,-4,-3,9,2,9,-6,-3,-10,1,-9,-8,9,-1,-3,-4,2,-1,8,8,9,-5,4,2,-8,-4,3,-5,-7,7,-3,-4,-8,1,-9,5,6,-5,-9,-2,1,-4,-7,-7,5,6,-3,-4,-9,7,2,6,-4,-8,-9,2,8,4,-6,2,3,1,2,10,-10,9,-1,-10,7,9,-2,-6,6,-6,1,4,-9,1,-10,-1,8,-2,7,5,4,8,3,-6,5,1,-3,-9,2,2,-3,-4,-6,-1,10,5,-9,2,8,-3,10,-9,9,-5,-10,-2,-1,5,3,-8,-3,9,-7,-6,-8,10,-10,-1,6,7,3,8,-6,-3,8,-3,6,3,-4,-2,5,-10,-2,-4,-9,4,-2,7,-5,6,4,4,-3,7,5,10,3,5,-1,4,9,3,2,9,2,1,-7,10,-4,-9,-8,7,7,9,-10,-9,2,-8,3,4,-3,3,-1,-1], dtype = "uint8")#candidate|6070|(864,)|const|uint8
call_6068 = relay.TupleGetItem(func_4317_call(relay.reshape(call_6062.astype('float64'), [11, 6]), relay.reshape(const_6069.astype('int8'), []), relay.reshape(const_6070.astype('uint8'), [864,]), ), 1)
call_6071 = relay.TupleGetItem(func_4321_call(relay.reshape(call_6062.astype('float64'), [11, 6]), relay.reshape(const_6069.astype('int8'), []), relay.reshape(const_6070.astype('uint8'), [864,]), ), 1)
output = relay.Tuple([call_6062,call_6068,const_6069,const_6070,])
output2 = relay.Tuple([call_6063,call_6071,const_6069,const_6070,])
func_6072 = relay.Function([], output)
mod['func_6072'] = func_6072
mod = relay.transform.InferType()(mod)
output = func_6072()
func_6073 = relay.Function([], output)
mutated_mod['func_6073'] = func_6073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2563_call = mod.get_global_var('func_2563')
func_2565_call = mutated_mod.get_global_var('func_2565')
call_6074 = relay.TupleGetItem(func_2563_call(), 0)
call_6075 = relay.TupleGetItem(func_2565_call(), 0)
var_6091 = relay.var("var_6091", dtype = "float64", shape = (3, 12, 2))#candidate|6091|(3, 12, 2)|var|float64
bop_6092 = relay.bitwise_or(call_6074.astype('int32'), var_6091.astype('int32')) # shape=(3, 12, 2)
bop_6095 = relay.bitwise_or(call_6075.astype('int32'), var_6091.astype('int32')) # shape=(3, 12, 2)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_6108 = relay.TupleGetItem(func_1609_call(), 0)
call_6109 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([bop_6092,call_6108,])
output2 = relay.Tuple([bop_6095,call_6109,])
func_6111 = relay.Function([var_6091,], output)
mod['func_6111'] = func_6111
mod = relay.transform.InferType()(mod)
var_6112 = relay.var("var_6112", dtype = "float64", shape = (3, 12, 2))#candidate|6112|(3, 12, 2)|var|float64
output = func_6111(var_6112)
func_6113 = relay.Function([var_6112], output)
mutated_mod['func_6113'] = func_6113
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6129 = relay.var("var_6129", dtype = "int64", shape = (8, 10, 13))#candidate|6129|(8, 10, 13)|var|int64
var_6130 = relay.var("var_6130", dtype = "int64", shape = (8, 10, 13))#candidate|6130|(8, 10, 13)|var|int64
bop_6131 = relay.less(var_6129.astype('bool'), relay.reshape(var_6130.astype('bool'), relay.shape_of(var_6129))) # shape=(8, 10, 13)
output = bop_6131
output2 = bop_6131
func_6148 = relay.Function([var_6129,var_6130,], output)
mod['func_6148'] = func_6148
mod = relay.transform.InferType()(mod)
mutated_mod['func_6148'] = func_6148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6148_call = mutated_mod.get_global_var('func_6148')
var_6150 = relay.var("var_6150", dtype = "int64", shape = (8, 10, 13))#candidate|6150|(8, 10, 13)|var|int64
var_6151 = relay.var("var_6151", dtype = "int64", shape = (8, 10, 13))#candidate|6151|(8, 10, 13)|var|int64
call_6149 = func_6148_call(var_6150,var_6151,)
output = call_6149
func_6152 = relay.Function([var_6150,var_6151,], output)
mutated_mod['func_6152'] = func_6152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5776_call = mod.get_global_var('func_5776')
func_5777_call = mutated_mod.get_global_var('func_5777')
call_6181 = relay.TupleGetItem(func_5776_call(), 0)
call_6182 = relay.TupleGetItem(func_5777_call(), 0)
func_6072_call = mod.get_global_var('func_6072')
func_6073_call = mutated_mod.get_global_var('func_6073')
call_6199 = relay.TupleGetItem(func_6072_call(), 0)
call_6200 = relay.TupleGetItem(func_6073_call(), 0)
func_5776_call = mod.get_global_var('func_5776')
func_5777_call = mutated_mod.get_global_var('func_5777')
call_6219 = relay.TupleGetItem(func_5776_call(), 1)
call_6220 = relay.TupleGetItem(func_5777_call(), 1)
func_4317_call = mod.get_global_var('func_4317')
func_4321_call = mutated_mod.get_global_var('func_4321')
const_6250 = relay.const(-10, dtype = "int8")#candidate|6250|()|const|int8
const_6251 = relay.const([6,5,-4,1,-4,6,-2,9,5,4,8,-1,-4,-8,-9,-8,-2,-7,5,-8,8,6,2,-2,9,-10,-7,1,1,8,2,-7,9,1,-1,-3,-2,1,-6,10,10,2,9,1,-3,-2,-4,-1,2,-9,8,3,2,-3,-6,-6,1,6,-1,1,-5,-1,3,-6,-4,7,-6,4,-2,-6,10,-5,-10,-4,-7,9,10,-2,3,-6,-2,1,-3,8,3,-6,-8,5,-3,10,-4,1,-10,6,3,-10,-7,7,-7,-7,-10,1,-3,7,5,-5,6,-2,-3,10,10,-4,-1,7,7,8,7,7,-6,-8,-10,2,3,2,10,-1,-2,-9,8,-2,-2,-2,10,2,4,8,5,1,4,3,5,-6,10,1,3,-3,-6,3,4,3,-7,1,-1,-1,6,-8,-9,2,-2,-9,8,8,-7,-9,8,9,3,7,-4,8,4,5,-4,7,9,9,-8,-3,-9,7,4,-3,10,10,10,-6,-8,10,-7,6,-2,7,-3,6,3,-3,3,-2,8,9,-2,4,7,9,-10,-3,-3,4,-9,10,-6,-8,9,-4,-2,8,-7,3,8,-9,9,1,-10,-8,7,-2,-2,-4,10,9,8,-5,2,10,-2,-8,-10,-2,6,-1,9,4,4,4,5,-6,-1,-1,-1,-2,-1,-5,-9,-1,-9,8,10,1,1,7,-9,8,-8,-4,9,3,6,10,6,-10,6,7,9,9,3,3,-3,-5,-1,1,5,-9,3,-4,-1,-6,-2,4,-10,1,-2,-7,-9,-5,1,10,9,5,-9,3,-7,8,1,-3,6,4,2,3,4,-2,6,-1,1,9,6,9,-10,-3,10,1,1,6,-7,-5,-8,7,8,1,3,1,-3,-5,9,5,5,7,-1,9,3,10,10,-7,5,-8,-9,10,-1,-6,-4,-10,-9,4,2,-10,7,8,9,-8,5,-5,-6,8,-1,-6,7,3,-4,6,10,1,-7,-9,-4,1,2,4,10,-5,-8,5,8,-9,-4,-8,-4,6,-10,8,-9,-3,-6,10,1,-8,-6,-4,8,9,-10,-6,8,6,6,-9,-4,7,1,7,-3,-3,-5,-5,10,-6,-1,-5,-6,-4,-6,7,-9,-9,4,-4,-10,-7,-2,1,-6,-2,-9,5,-9,-6,-4,-2,-9,-3,8,9,-4,6,-9,-10,2,-2,-1,6,8,3,-9,4,8,1,7,-6,8,-1,-9,-2,2,-3,2,3,5,3,10,2,-7,8,4,-6,-7,9,-7,6,6,-2,-1,10,8,-8,1,10,4,1,-1,-8,6,-4,-8,-10,-10,-7,-5,4,10,-6,5,-8,-4,-7,-8,3,2,-4,-8,9,9,8,2,-9,-8,-5,1,-10,-4,7,-1,7,10,8,-8,-7,-4,10,8,10,4,-9,-1,-9,-7,9,9,-5,-7,-8,-1,-3,1,-1,-5,-7,6,-6,-4,-2,-1,10,6,10,8,10,4,-4,-7,6,-6,10,8,1,-1,4,3,-4,9,4,-4,9,-8,-3,-8,8,1,-7,6,-10,10,-8,9,-4,8,8,-4,9,1,-8,2,-2,4,1,-7,6,6,2,8,4,4,7,10,-10,8,10,2,5,3,-5,-9,-10,6,10,6,9,7,-9,-10,10,7,-9,1,-6,-10,-7,-3,-1,8,1,7,-5,-4,3,-1,5,2,8,8,10,-4,-6,-3,-6,-10,5,6,4,-4,7,10,3,6,7,-5,1,-5,8,3,9,10,-3,-5,8,3,-5,7,-7,3,-6,-1,10,3,-4,-2,2,-8,-10,-3,4,-6,-1,1,6,9,2,9,6,10,10,2,3,8,-6,-4,7,1,2,3,6,10,-4,10,8,-7,-1,10,-10,9,-9,6,2,-1,1,-2,8,5,-10,-9,6,-9,-6,2,9,-1,6,-2,5,5,-7,-3,1,-6,-6,1,10,8,9,1,-1,4,-2,-8,-2,-4,-9,4,6,3,5,-3,-2,-1,1,10,-6,1,-3,-4,-9,-3,-5,2,-7,5,-7,-4,-1,1,-9,-8,-5,3,-6,-10,3,-7,10,-2,-2,-8,-9,-7,9,4,9,3,1,-2,2,5,-7,6,2,4,-6,3,5,6,10,-4,-4,-4,4,3,10,-1,-8,4,-6,-4,-1,8,8,3,-5,-8,-5,-5,8,5,4,3,-5,-4,7,3,-6,7,-6,4,7,-2,4,-3,3,-10,-6,-3,-4,-3,-6,9,7,5,-6,5,-1,-8,-2,9,1,-4,-4,9,5,-9,8,4,3,9,8,-5,-8,-6,-5], dtype = "uint8")#candidate|6251|(864,)|const|uint8
call_6249 = relay.TupleGetItem(func_4317_call(relay.reshape(call_6199.astype('float64'), [11, 6]), relay.reshape(const_6250.astype('int8'), []), relay.reshape(const_6251.astype('uint8'), [864,]), ), 11)
call_6252 = relay.TupleGetItem(func_4321_call(relay.reshape(call_6199.astype('float64'), [11, 6]), relay.reshape(const_6250.astype('int8'), []), relay.reshape(const_6251.astype('uint8'), [864,]), ), 11)
func_4850_call = mod.get_global_var('func_4850')
func_4854_call = mutated_mod.get_global_var('func_4854')
var_6259 = relay.var("var_6259", dtype = "int64", shape = (4, 140))#candidate|6259|(4, 140)|var|int64
call_6258 = relay.TupleGetItem(func_4850_call(relay.reshape(var_6259.astype('int64'), [5, 16, 7]), relay.reshape(var_6259.astype('int64'), [5, 16, 7]), ), 2)
call_6260 = relay.TupleGetItem(func_4854_call(relay.reshape(var_6259.astype('int64'), [5, 16, 7]), relay.reshape(var_6259.astype('int64'), [5, 16, 7]), ), 2)
output = relay.Tuple([call_6181,call_6199,call_6219,call_6249,const_6250,const_6251,call_6258,var_6259,])
output2 = relay.Tuple([call_6182,call_6200,call_6220,call_6252,const_6250,const_6251,call_6260,var_6259,])
func_6261 = relay.Function([var_6259,], output)
mod['func_6261'] = func_6261
mod = relay.transform.InferType()(mod)
var_6262 = relay.var("var_6262", dtype = "int64", shape = (4, 140))#candidate|6262|(4, 140)|var|int64
output = func_6261(var_6262)
func_6263 = relay.Function([var_6262], output)
mutated_mod['func_6263'] = func_6263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2983_call = mod.get_global_var('func_2983')
func_2984_call = mutated_mod.get_global_var('func_2984')
call_6268 = relay.TupleGetItem(func_2983_call(), 0)
call_6269 = relay.TupleGetItem(func_2984_call(), 0)
func_2908_call = mod.get_global_var('func_2908')
func_2911_call = mutated_mod.get_global_var('func_2911')
var_6274 = relay.var("var_6274", dtype = "float32", shape = (144, 1))#candidate|6274|(144, 1)|var|float32
call_6273 = relay.TupleGetItem(func_2908_call(relay.reshape(var_6274.astype('float32'), [144,])), 2)
call_6275 = relay.TupleGetItem(func_2911_call(relay.reshape(var_6274.astype('float32'), [144,])), 2)
output = relay.Tuple([call_6268,call_6273,var_6274,])
output2 = relay.Tuple([call_6269,call_6275,var_6274,])
func_6284 = relay.Function([var_6274,], output)
mod['func_6284'] = func_6284
mod = relay.transform.InferType()(mod)
mutated_mod['func_6284'] = func_6284
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6285 = relay.var("var_6285", dtype = "float32", shape = (144, 1))#candidate|6285|(144, 1)|var|float32
func_6284_call = mutated_mod.get_global_var('func_6284')
call_6286 = func_6284_call(var_6285)
output = call_6286
func_6287 = relay.Function([var_6285], output)
mutated_mod['func_6287'] = func_6287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mod.get_global_var('func_2870')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_6320 = relay.TupleGetItem(func_2870_call(), 2)
call_6321 = relay.TupleGetItem(func_2871_call(), 2)
func_4725_call = mod.get_global_var('func_4725')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_6325 = relay.TupleGetItem(func_4725_call(), 0)
call_6326 = relay.TupleGetItem(func_4726_call(), 0)
func_3730_call = mod.get_global_var('func_3730')
func_3732_call = mutated_mod.get_global_var('func_3732')
call_6332 = relay.TupleGetItem(func_3730_call(), 0)
call_6333 = relay.TupleGetItem(func_3732_call(), 0)
func_4317_call = mod.get_global_var('func_4317')
func_4321_call = mutated_mod.get_global_var('func_4321')
const_6357 = relay.const([[-9.401697],[-6.165917],[-9.431692],[-0.924565],[2.737099],[-6.447184],[-4.628210],[2.883632],[0.809805],[3.516756],[-1.426140],[-3.838059],[1.232599],[7.944924],[-4.128544],[-1.010569],[7.804579],[-5.932857],[-2.497290],[-4.698686],[8.209513],[-9.436672],[-6.678441],[-8.558793],[9.438746],[5.670845],[7.169191],[8.950679],[9.263323],[-0.364912],[0.806612],[1.314315],[5.990093],[-0.969312],[-5.539465],[-2.769658],[8.431847],[-3.773818],[-7.242857],[4.712380],[-7.774704],[-9.639629],[-9.184224],[-0.686393],[-6.769031],[-6.415898],[3.235217],[-2.615541],[5.196249],[-8.083806],[3.829163],[4.090856],[6.511787],[6.628707],[-9.030243],[-0.623504],[0.284845],[-2.573836],[-9.404746],[9.022088],[5.709461],[-2.160362],[3.315767],[-9.776214],[0.748901],[9.003892]], dtype = "float64")#candidate|6357|(66, 1)|const|float64
const_6358 = relay.const(-2, dtype = "int8")#candidate|6358|()|const|int8
var_6359 = relay.var("var_6359", dtype = "uint8", shape = (864,))#candidate|6359|(864,)|var|uint8
call_6356 = relay.TupleGetItem(func_4317_call(relay.reshape(const_6357.astype('float64'), [11, 6]), relay.reshape(const_6358.astype('int8'), []), relay.reshape(var_6359.astype('uint8'), [864,]), ), 5)
call_6360 = relay.TupleGetItem(func_4321_call(relay.reshape(const_6357.astype('float64'), [11, 6]), relay.reshape(const_6358.astype('int8'), []), relay.reshape(var_6359.astype('uint8'), [864,]), ), 5)
output = relay.Tuple([call_6320,call_6325,call_6332,call_6356,const_6357,const_6358,var_6359,])
output2 = relay.Tuple([call_6321,call_6326,call_6333,call_6360,const_6357,const_6358,var_6359,])
func_6363 = relay.Function([var_6359,], output)
mod['func_6363'] = func_6363
mod = relay.transform.InferType()(mod)
mutated_mod['func_6363'] = func_6363
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6364 = relay.var("var_6364", dtype = "uint8", shape = (864,))#candidate|6364|(864,)|var|uint8
func_6363_call = mutated_mod.get_global_var('func_6363')
call_6365 = func_6363_call(var_6364)
output = call_6365
func_6366 = relay.Function([var_6364], output)
mutated_mod['func_6366'] = func_6366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5002_call = mod.get_global_var('func_5002')
func_5004_call = mutated_mod.get_global_var('func_5004')
call_6373 = relay.TupleGetItem(func_5002_call(), 0)
call_6374 = relay.TupleGetItem(func_5004_call(), 0)
const_6396 = relay.const([[[1.424561,2.029230],[-2.936285,-7.025824],[-5.693695,-0.214220],[-7.350852,3.083113],[-5.227929,6.394064],[-2.588984,-4.629576],[7.879015,-8.917692],[4.832363,7.270158],[9.998012,7.337720],[0.824282,-1.272103],[-9.264711,8.849685],[4.183198,1.599577],[8.997642,3.627742],[-3.415836,-4.679638],[-8.551672,2.894728],[-8.353493,-0.509716]],[[9.694699,7.182609],[5.325574,-0.714527],[-5.374894,5.351555],[6.076793,9.817570],[6.798022,-8.412213],[1.862901,3.743647],[5.507100,6.192978],[-4.901283,-9.761815],[4.683359,-3.482993],[9.376598,-6.402460],[-1.562924,-1.734940],[-3.478048,-3.582422],[-1.058851,-8.130502],[5.469157,0.975914],[-1.732284,-0.917936],[3.892002,0.733231]],[[-7.894684,4.023923],[-4.341412,4.812922],[3.873811,-2.235872],[-2.763154,-6.118793],[-9.305310,-0.183642],[-6.812174,-2.151196],[-5.575450,6.075481],[2.416697,-6.674300],[-5.600504,-2.694612],[-7.130385,5.225442],[1.215607,4.255396],[-8.039813,-1.038885],[-6.072443,-0.602532],[-7.311128,-1.658044],[6.787775,-5.339031],[-3.813695,-9.788868]]], dtype = "float64")#candidate|6396|(3, 16, 2)|const|float64
bop_6397 = relay.power(call_6373.astype('float32'), const_6396.astype('float32')) # shape=(3, 16, 2)
bop_6400 = relay.power(call_6374.astype('float32'), const_6396.astype('float32')) # shape=(3, 16, 2)
uop_6410 = relay.cos(const_6396.astype('float64')) # shape=(3, 16, 2)
bop_6414 = relay.multiply(uop_6410.astype('uint32'), call_6373.astype('uint32')) # shape=(3, 16, 2)
bop_6417 = relay.multiply(uop_6410.astype('uint32'), call_6374.astype('uint32')) # shape=(3, 16, 2)
func_1686_call = mod.get_global_var('func_1686')
func_1689_call = mutated_mod.get_global_var('func_1689')
const_6423 = relay.const([-1,-3,-10,8,5,-2,-6,9,-5,-4,-3,6,3,-6,-1,10,10,2,-2,-3,-2,9,4,-9,-1,5,7,10,1,6,-1,-8,10,10,2,10,2,9,9,4,2,6,3,9,1,9,-2,4,-7,-7,-2,3,8,10,2,9,-5,3,-2,3,-10,7,9,5,8,7,10,-3,-1,-8,-7,7,4,2,-2,9,-7,-3,10,4,-1,7,8,8,5,4,-2,3,-1,-2,-10,-5,7,-5,8,-4,-10,-8,3,10,3,9,5,3,-9,-8,-4,-7,-3,-6,2,9,3,10,5,-3,4,-6,-5,4,4,2,5,8,2,8,-6,-7,4,4,-9,-8,10,-3,-4,9,-9,5,10,1,-9,-7,-5,5,-4,-1,-5,-10,-4,8,-10,-6,-7,2,-2,1,-3,8,5,-1,2,3,-10,10,6,4,6,6,8,-5,2,-4,6,-4,5,3,-7,5,-1,-3,-7,-2,6,-8,-5,-7,-9,-1,4,8,-1,7,9,-5,-8,-5,5,8,7,-6,-1,9,-3,-6,8,-6,-7,8,6,-4,4,-9,-9,2,7,8,2,-9,-8,2,1,6,5,-5,7,-7,-3,2,5,7,2,9,3,-9,-3,8,10,-3,7,-8,-9,7,-1,-3,-3,-8,8,-8,-3,5,-9,1,8,-6,2,-1,-9,5,7,6,-8,4,-2,-10,-3,-3,7,-4,8,10,-6,-2,-9,-4,-5,-6,-5,-1,-7,3,6,-2,10,8,10,9,-8,2,8,-6,6,-7,6,-7,-1,-3,-6,9,-5,-5,6,-2,5,-4,9,7,5,6,4,-4,-6,3,6,-10,-1,-5,-9,1,-10,-8,-6,6,-10,3,-10,2,-8,9,-9,2,-6,-6,5,-10,2,-5,6,10,-6,2,1,-1,9,2,9,-7,-2,-1,-8,-3,-2,1,-2,3,-5,3,9,7,-1,5,3,-6,-2,-4,-1,-1,5,-10,2,-4,-6,-4,-8,2,-10,-3,6,-9,-8,9,10,-4,-3,-2,6,3,-3,-9,-8,2,8,4,-5,-2,-8,4,-10,-4,3,-9,4,-2,-9,-7,4,8,3,3,4,10,-6,-1,3,1,-3,-4,2,-3,-9,-1,-10,-2,-8,-10,10,-4,4,-5,1,10,6,-1,2,-1,-6,3,-1,8,1,2,8,10,-3,7,-10,-8,-5,-9,4,-9,4,6,-6,-5,-4,10,6,2,-4,-1,-9,5,9,10,-5,4,10,5,8,-5,-10,2,5,-3,-4,7,7,-7,7,-10,6,-2,-5,2,-10,6,2,-3,-4,7,-5,3,-8,8,10,8,1,-2,-8,10,1,-5,3,-1,-8,-5,3,-5,-8,6,1,4,3,-8,10,8,-5,-6,5,-7,6,-8,-10,3,7,8,3,-10,9,1,6,-3,-4,-1,-8,4,10,6,6,-10,9,1,-1,10,6,9,1,-5,1,-8,4,-3,-3,-4,8,-1,3,7,-2,-4], dtype = "uint8")#candidate|6423|(560,)|const|uint8
call_6422 = relay.TupleGetItem(func_1686_call(relay.reshape(const_6423.astype('uint8'), [560,])), 0)
call_6424 = relay.TupleGetItem(func_1689_call(relay.reshape(const_6423.astype('uint8'), [560,])), 0)
output = relay.Tuple([bop_6397,bop_6414,call_6422,const_6423,])
output2 = relay.Tuple([bop_6400,bop_6417,call_6424,const_6423,])
func_6438 = relay.Function([], output)
mod['func_6438'] = func_6438
mod = relay.transform.InferType()(mod)
output = func_6438()
func_6439 = relay.Function([], output)
mutated_mod['func_6439'] = func_6439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6454 = relay.var("var_6454", dtype = "uint32", shape = (2, 5, 9))#candidate|6454|(2, 5, 9)|var|uint32
var_6455 = relay.var("var_6455", dtype = "uint32", shape = (2, 5, 9))#candidate|6455|(2, 5, 9)|var|uint32
bop_6456 = relay.multiply(var_6454.astype('uint32'), relay.reshape(var_6455.astype('uint32'), relay.shape_of(var_6454))) # shape=(2, 5, 9)
output = bop_6456
output2 = bop_6456
func_6461 = relay.Function([var_6454,var_6455,], output)
mod['func_6461'] = func_6461
mod = relay.transform.InferType()(mod)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6461_call = mutated_mod.get_global_var('func_6461')
var_6463 = relay.var("var_6463", dtype = "uint32", shape = (2, 5, 9))#candidate|6463|(2, 5, 9)|var|uint32
var_6464 = relay.var("var_6464", dtype = "uint32", shape = (2, 5, 9))#candidate|6464|(2, 5, 9)|var|uint32
call_6462 = func_6461_call(var_6463,var_6464,)
output = call_6462
func_6465 = relay.Function([var_6463,var_6464,], output)
mutated_mod['func_6465'] = func_6465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_6556 = relay.TupleGetItem(func_1609_call(), 0)
call_6557 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([call_6556,])
output2 = relay.Tuple([call_6557,])
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
func_6072_call = mod.get_global_var('func_6072')
func_6073_call = mutated_mod.get_global_var('func_6073')
call_6716 = relay.TupleGetItem(func_6072_call(), 1)
call_6717 = relay.TupleGetItem(func_6073_call(), 1)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_6730 = func_1694_call()
call_6731 = func_1694_call()
output = relay.Tuple([call_6716,call_6730,])
output2 = relay.Tuple([call_6717,call_6731,])
func_6738 = relay.Function([], output)
mod['func_6738'] = func_6738
mod = relay.transform.InferType()(mod)
mutated_mod['func_6738'] = func_6738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6738_call = mutated_mod.get_global_var('func_6738')
call_6739 = func_6738_call()
output = call_6739
func_6740 = relay.Function([], output)
mutated_mod['func_6740'] = func_6740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3827_call = mod.get_global_var('func_3827')
func_3829_call = mutated_mod.get_global_var('func_3829')
call_6754 = relay.TupleGetItem(func_3827_call(), 0)
call_6755 = relay.TupleGetItem(func_3829_call(), 0)
output = call_6754
output2 = call_6755
func_6773 = relay.Function([], output)
mod['func_6773'] = func_6773
mod = relay.transform.InferType()(mod)
mutated_mod['func_6773'] = func_6773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6773_call = mutated_mod.get_global_var('func_6773')
call_6774 = func_6773_call()
output = call_6774
func_6775 = relay.Function([], output)
mutated_mod['func_6775'] = func_6775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6773_call = mod.get_global_var('func_6773')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_6797 = func_6773_call()
call_6798 = func_6773_call()
output = relay.Tuple([call_6797,])
output2 = relay.Tuple([call_6798,])
func_6804 = relay.Function([], output)
mod['func_6804'] = func_6804
mod = relay.transform.InferType()(mod)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6804_call = mutated_mod.get_global_var('func_6804')
call_6805 = func_6804_call()
output = call_6805
func_6806 = relay.Function([], output)
mutated_mod['func_6806'] = func_6806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_6821 = func_4065_call()
call_6822 = func_4065_call()
output = relay.Tuple([call_6821,])
output2 = relay.Tuple([call_6822,])
func_6823 = relay.Function([], output)
mod['func_6823'] = func_6823
mod = relay.transform.InferType()(mod)
mutated_mod['func_6823'] = func_6823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6823_call = mutated_mod.get_global_var('func_6823')
call_6824 = func_6823_call()
output = call_6824
func_6825 = relay.Function([], output)
mutated_mod['func_6825'] = func_6825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6438_call = mod.get_global_var('func_6438')
func_6439_call = mutated_mod.get_global_var('func_6439')
call_6886 = relay.TupleGetItem(func_6438_call(), 0)
call_6887 = relay.TupleGetItem(func_6439_call(), 0)
uop_6898 = relay.cosh(call_6886.astype('float64')) # shape=(3, 16, 2)
uop_6900 = relay.cosh(call_6887.astype('float64')) # shape=(3, 16, 2)
output = relay.Tuple([uop_6898,])
output2 = relay.Tuple([uop_6900,])
func_6913 = relay.Function([], output)
mod['func_6913'] = func_6913
mod = relay.transform.InferType()(mod)
output = func_6913()
func_6914 = relay.Function([], output)
mutated_mod['func_6914'] = func_6914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1536_call = mod.get_global_var('func_1536')
func_1537_call = mutated_mod.get_global_var('func_1537')
call_6955 = relay.TupleGetItem(func_1536_call(), 2)
call_6956 = relay.TupleGetItem(func_1537_call(), 2)
func_6363_call = mod.get_global_var('func_6363')
func_6366_call = mutated_mod.get_global_var('func_6366')
var_6964 = relay.var("var_6964", dtype = "uint8", shape = (864,))#candidate|6964|(864,)|var|uint8
call_6963 = relay.TupleGetItem(func_6363_call(relay.reshape(var_6964.astype('uint8'), [864,])), 1)
call_6965 = relay.TupleGetItem(func_6366_call(relay.reshape(var_6964.astype('uint8'), [864,])), 1)
output = relay.Tuple([call_6955,call_6963,var_6964,])
output2 = relay.Tuple([call_6956,call_6965,var_6964,])
func_6980 = relay.Function([var_6964,], output)
mod['func_6980'] = func_6980
mod = relay.transform.InferType()(mod)
var_6981 = relay.var("var_6981", dtype = "uint8", shape = (864,))#candidate|6981|(864,)|var|uint8
output = func_6980(var_6981)
func_6982 = relay.Function([var_6981], output)
mutated_mod['func_6982'] = func_6982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_7016 = relay.TupleGetItem(func_1803_call(), 0)
call_7017 = relay.TupleGetItem(func_1805_call(), 0)
func_2231_call = mod.get_global_var('func_2231')
func_2232_call = mutated_mod.get_global_var('func_2232')
call_7031 = func_2231_call()
call_7032 = func_2231_call()
bop_7036 = relay.mod(call_7016.astype('float64'), relay.reshape(call_7031.astype('float64'), relay.shape_of(call_7016))) # shape=(3, 1, 2)
bop_7039 = relay.mod(call_7017.astype('float64'), relay.reshape(call_7032.astype('float64'), relay.shape_of(call_7017))) # shape=(3, 1, 2)
func_3308_call = mod.get_global_var('func_3308')
func_3311_call = mutated_mod.get_global_var('func_3311')
const_7047 = relay.const([True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False], dtype = "bool")#candidate|7047|(1920,)|const|bool
call_7046 = func_3308_call(relay.reshape(const_7047.astype('bool'), [16, 8, 15]), relay.reshape(const_7047.astype('bool'), [16, 8, 15]), )
call_7048 = func_3308_call(relay.reshape(const_7047.astype('bool'), [16, 8, 15]), relay.reshape(const_7047.astype('bool'), [16, 8, 15]), )
func_6773_call = mod.get_global_var('func_6773')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_7052 = func_6773_call()
call_7053 = func_6773_call()
output = relay.Tuple([bop_7036,call_7046,const_7047,call_7052,])
output2 = relay.Tuple([bop_7039,call_7048,const_7047,call_7053,])
func_7057 = relay.Function([], output)
mod['func_7057'] = func_7057
mod = relay.transform.InferType()(mod)
mutated_mod['func_7057'] = func_7057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7057_call = mutated_mod.get_global_var('func_7057')
call_7058 = func_7057_call()
output = call_7058
func_7059 = relay.Function([], output)
mutated_mod['func_7059'] = func_7059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4725_call = mod.get_global_var('func_4725')
func_4726_call = mutated_mod.get_global_var('func_4726')
call_7084 = relay.TupleGetItem(func_4725_call(), 0)
call_7085 = relay.TupleGetItem(func_4726_call(), 0)
func_1574_call = mod.get_global_var('func_1574')
func_1579_call = mutated_mod.get_global_var('func_1579')
var_7106 = relay.var("var_7106", dtype = "float64", shape = (90,))#candidate|7106|(90,)|var|float64
var_7107 = relay.var("var_7107", dtype = "float64", shape = (60,))#candidate|7107|(60,)|var|float64
var_7108 = relay.var("var_7108", dtype = "float32", shape = (144, 1))#candidate|7108|(144, 1)|var|float32
call_7105 = relay.TupleGetItem(func_1574_call(relay.reshape(var_7106.astype('float64'), [3, 15, 2]), relay.reshape(var_7106.astype('float64'), [3, 15, 2]), relay.reshape(var_7107.astype('float64'), [1, 60]), relay.reshape(var_7108.astype('float32'), [144,]), ), 3)
call_7109 = relay.TupleGetItem(func_1579_call(relay.reshape(var_7106.astype('float64'), [3, 15, 2]), relay.reshape(var_7106.astype('float64'), [3, 15, 2]), relay.reshape(var_7107.astype('float64'), [1, 60]), relay.reshape(var_7108.astype('float32'), [144,]), ), 3)
func_2264_call = mod.get_global_var('func_2264')
func_2268_call = mutated_mod.get_global_var('func_2268')
const_7111 = relay.const([7.598039,6.552576,6.554257,-8.300177,-4.208530,-8.513410,-9.912015,-1.108725,7.644494,3.466464,-3.719372,-5.604318,6.699231,3.902222,1.826260,5.036358,-7.107347,1.979759,-4.403627,4.017580,4.500314,3.678312,-3.231544,6.486301,0.352055,-4.688893,-6.222177,-5.356003,-3.222599,-6.806729,-1.979965,8.092099,-9.295046,-7.195059,-1.067194,-6.530844,5.924657,7.980001,1.675118,7.786672,-0.363550,-5.450449,-7.686324,-6.420109,1.587851,2.363524,8.118108,-1.669389,1.713708,-0.512077,-2.625796,7.854996,1.106576,5.015572,6.908511,4.003621,-2.830036,9.615068,-7.232524,-4.475718,-4.335312,3.010091,-0.577947,-0.505699,-8.214900,6.805629,3.013386,-6.472718,-1.443186,0.382480,5.272442,6.854581,4.291715,-5.826123,-6.842469,1.326055,-9.695845,-7.098173,-9.902160,-9.664743,-9.468334,4.517208,0.968229,-9.206206,5.204990,0.604626,-0.128727,4.224751,1.961511,8.901431,-1.744396,8.220808,9.439584,5.940836,-4.182895,-2.715185,4.678518,-6.711406,3.371379,-4.407292,-2.769478,8.289548,-7.416672,-6.026640,9.092124,-2.115079,-3.635698,-7.465964,9.199936,2.341221,-0.825893,-9.145219,1.569183,-0.411012,3.639987,-8.416831,-8.682163,-6.634605,-8.123678,8.796784,-8.380197,9.427740,5.470671,-1.055425,0.580388,-9.508005,2.220786,9.067482,4.875584,-3.548208,8.613425,-9.520048,-2.171727,-0.771440,-3.517455,-0.130205,5.028721,2.598232,-3.030202,-5.743556,-6.219371,9.459069,7.695868,-6.373065,-1.473491,-8.385448,3.692646,3.066300,2.494642,-4.338752,8.610291,5.207066,-6.895103,6.603687,-9.545450,-6.414588,-6.675892,3.310785,8.756924,-3.761956,-0.790635,2.767763,-3.740690,0.001571,-8.162131,1.469483,1.898191,1.281814,1.137472,-3.153342,-7.016208,-5.962035,-3.253880,-1.992498,-3.548739,2.128984,9.240247,-6.727032,8.813429,-3.926717,-2.509376,-9.841413,-0.391292,5.044167,-1.099189,1.419843,9.673250,-1.696942,4.086753,2.966286,0.189374,-4.575328,3.690730,-5.447843,5.753535,-1.555119,-2.108959,8.706110,-0.220621,5.186136,-9.658674,1.340285,-0.819565,6.617409,7.231565,8.504546,4.795734,7.851177,2.850788,6.350104,-4.706889,-8.781106,-5.424407,1.038659,-2.312051,-5.833675,-2.266161,-5.596320,5.736430,-5.070739,-7.748598,1.577795,-3.429294,-4.035793,0.787454,-2.768470,-9.919842,-9.711632,-1.622570,1.436467,-4.819325,8.404547,-8.552710,-0.932884,0.245186,-9.912965,-9.231773,2.272167,-9.307628,-1.794128,8.499892,-2.615055,4.145371,1.712851,-1.644499,0.794376,-7.239428,2.906295,-0.072183,-0.446277,6.172176,-2.650110,-4.241097,-3.744500,1.993811,-1.701214,3.117261,-6.955824,-9.558320,-4.695224,9.472289,2.669534,-9.604994,-5.136192,-5.140626,-6.849257,8.667654,-7.969562,-2.608962,-5.076692,5.829745,-0.231427,0.350742,-3.130613,-2.914531,8.015029,-3.664696,8.140473,2.376424,8.244351,-5.502773,4.319511,-2.181429,-3.260315,-7.049583,3.179053,7.810127,-6.086515,-9.059623,-0.229313,9.540650,-7.353557,2.633370,-8.053172,2.984991,-3.569591,6.168562,4.861711,8.305408,-8.818255,9.332275,-4.489888,-8.957421,8.198987,1.944207,8.580797,4.774083,-2.671085,-0.119792,-0.865559,-0.046756,8.538022,-4.391627,-3.439875,-5.060533,-0.951582,-5.629244,0.971648,9.417096,0.315455,-3.109764,-0.632594,8.009550,-1.843002,8.775467,4.303721,-6.986596,-9.405513,-3.992379,-4.645712,2.211741,-0.497882,8.549128,-8.603204,-6.329207,6.265971,5.085162,3.979424,-4.740993,-4.672441,-0.236821,-7.685710,-8.164055,2.028745,0.987293,-6.000664,-8.407208,-3.186395,-4.629935,7.628763,-4.236952,5.495040,-7.766326,-2.739447,6.324076,-5.365615,8.219054,-3.062568,7.235925,-7.592898,6.253271,-5.443163,7.433959,-0.367635,0.023723,-4.168675,-5.866917,1.905670,-0.156354,-5.566132,-4.464060,3.266311,8.481177,-3.770874,-9.285439,9.203734,7.197115,0.738606,-4.591328,-7.005920,4.288212,3.467305,-5.004109,-9.116613,2.822739,-5.369139,-5.141548,6.370738,0.773588,-9.217602,-2.101626,-0.595854,0.634470,-8.491263,5.399637,-7.529704,7.575090,-1.292190,-6.323294,9.283522,3.500887,-3.614047,6.670520,4.973205,5.672398,-4.860998,5.635713,7.359401,0.105145,-1.887806,-1.090116,5.586870,1.219622,6.268023,2.785539,3.066767,0.564564,-3.366627,1.609274,5.478929,2.717089,-7.829442,-3.628699,-6.709116,1.086086,-0.900374,5.882335,9.464608,-0.511054,-4.765710,2.696585,-0.648776,6.655760,-5.048827,2.766320,0.731273,1.810215,0.428460,3.975723,1.486033,1.667972,-9.667866,-4.325610,9.334133,7.120727,-4.627211,9.233160,3.249134,5.245213,4.666841,1.717737,9.700027,-8.727424,9.948513,-2.843260,-6.611572,-2.354124,-7.083441,-7.444699,4.603381,-3.809208,4.187604,6.289843,-5.160876,-5.992473,1.746732,9.726845,-0.356090,2.990796,3.012222,4.542491,3.056450,8.206553,-2.377302,3.888695,3.388023,4.855751,5.343882,6.567545,4.273782,1.657852,8.872535,1.484665,-2.745698,4.066158,3.134890,0.086400,8.547958,-3.036119,3.539788,2.536680,6.429726,3.235139,3.105217,6.323996,-9.971414,6.205999,8.489232,4.308783,-9.701187,1.283277,3.139194,-8.237801,4.527759,-4.990858,4.922032,7.288982,-4.191386,9.870118,4.137260,-1.128266,-7.208597,-3.244924,4.603158,2.361783,-9.613389,4.789993,-8.211837,-6.891509,-4.339926,-4.587067,2.203612,6.937753,-3.582906,3.543291,3.618116,7.080123,-9.834315,7.363736,4.279993,8.181204,5.935074,-1.125780,-2.087585,-2.227562,3.592829,-2.497383,-9.072692,2.834542,4.798865,0.687424,-4.636168,-2.871787,-3.742890,-3.669107,-3.983050,7.081514,-2.335301,2.324408,2.213607,-1.186492,-1.819589,3.495875,-9.741393,1.866772,7.917160,-5.003643,4.679600,-9.681133,-9.350557,-7.965866,-5.895504,-8.892030,5.569010,-5.863455,2.015174,9.676004,2.327493,6.767672,9.336835,8.962629,2.120444,7.136146,-2.568666,-8.351250,-9.136099,-3.977306,-6.293287,-9.634822,-0.486306,-1.346837,2.478906,-4.799299,-0.715757,-1.418084,-7.109343,1.984099,4.882051,4.053144,-2.004887,-4.876641,-2.836824,-9.722373,3.010614,-4.607288,0.787958,-2.194549,-1.629079,4.560821,-1.107811,6.189512,-4.384482,-6.773771,7.120467,2.032097,7.979053,-8.405094,-4.578098,-1.983000,0.888453,-3.205584,-7.024809,8.234524,1.177867,8.894062,-6.955549,-8.802310,7.065648,-0.699008,-1.341860,9.931277,7.012552,7.224045,-4.731881,-8.185896,-9.453728,-5.980629,3.791971,-8.775448,-3.320307,-5.424748,-6.058470,2.143373,0.074686,-6.337188,-8.433470,2.900653,3.488294,0.697730,-2.011405,-4.086751,-6.290330,9.815591,-2.633079,-4.154825,-3.089942,-9.037927,-9.492837,-8.542170,8.238809,9.430429,-2.393830,-7.261968,-3.570678,2.274470,1.847190,6.606442,-6.560945,4.967141,-5.235647,-8.228888,-2.646812,7.304567,-6.815226,-1.962874,-9.149776,4.907038,-7.227255,7.534544,-1.214772,0.854350,-4.978021,1.661130,-1.297527,1.142281,8.718503,4.147333,-9.414572,-9.985704,-3.768082,4.812943,-7.648987,-8.279061,-2.347155,2.480161,-0.389965,-0.813168,-1.442821,-3.971149,-6.156047,5.165661,0.050551,5.346629,-0.971313,-9.511893,-5.204522,5.021531,2.939595,6.882621,8.925981,-4.130063,1.010463,-3.279203,-4.253444,-4.117230,9.885589,-8.657909,-5.492540,-6.697695,6.942923,-1.642528,-0.249947,7.236509,3.969557,7.775852,1.096488,-3.550256,-5.997142,-9.464721,7.176246,4.340687,9.776183,1.608236,3.458971,-6.291812,7.917385,-6.998849,-7.634317,6.820754,-6.159073,4.467160,-9.649683,7.286711,-3.343912,0.559412,-9.497731,-4.734113,2.870770,-3.649413,-3.532971,0.898520,2.564711,3.478336,2.112353,6.303940,-8.803368,-4.302480,-5.014053,4.548912,4.413668,0.444540,-9.965890,5.004078,9.510549,-9.579090,-7.510102,5.337987,-3.532374,-8.699091,5.164431,3.822880,-7.714640,-9.772420,6.426331,3.101209,5.384220,6.337986,9.974581,6.779129,-9.429438,-7.658885,4.724950,-6.458543,-9.178305,-7.758820,-6.842586,1.948789,6.871083,1.216008,-5.096376,3.317833,6.651597,2.253152,-1.170668,-0.554156,-5.108907,7.372669,-1.343074,4.036060,-7.531177,1.685562,-6.641243,9.028281,-6.403395,-1.231413,-0.919365,-8.133443,-6.536692,-7.204750,-0.667207,8.073552,5.392281,9.429837,-4.595614,-3.346560,-7.883399,0.201774,1.565310,-4.129548,-1.906350,-8.631063,-0.066770,-7.846614,-1.267203,7.506750,2.144786,2.312648,-9.885333,5.696329,-2.747278,2.078185,9.213256,1.658090,-9.890707,-8.581707,-2.379625,0.423927,-9.772336,-8.692014,-9.479835,3.179642,-6.207881,-5.148751,4.068178,-6.088804,4.690396,-7.588544,-3.580530,9.419319,6.598574,6.938701,-7.934437,9.279535,1.057547,9.383374,5.519507,0.207606,-7.447979,-1.850374,9.484519,1.684736,1.225619,1.872748,2.198205,-9.293244,5.239509,-9.657147,-1.561261,-3.980848,1.586664,5.616200,-7.348662,7.717379,-0.314035,3.136272,-2.700534,-3.932475,-4.794038,2.093498,3.869767,5.741595,-6.244943,-8.427070,3.426457,-0.012626,9.988799,8.281370,-3.193518,-1.956861,5.597255,1.165142,-7.225102,0.402724,3.990572,-7.275561,-6.724627,3.650683,6.379487,7.888337,-9.232010,-9.878331,1.624383,-8.774999,-5.543615,-3.852316,-5.312269,5.108058,8.819860,6.354078,3.385587,5.697610,1.218447,-2.933384,4.066644,1.630040,4.696677,4.509122,-1.722967,4.365884,-9.551608,-7.749860,7.452986,4.594219,-6.445986,4.582546,-7.813931,5.119465,-7.110012,-2.382061,4.531308,9.492631,6.817262,7.949115,-0.672234,-0.582229,-4.378927,0.575796,-5.866963,-4.335780,-9.022981,6.477584,0.900574,-5.426001,-6.390372,3.598698,6.230794,1.224255,2.041436,-7.540957,3.144028,-3.401137,8.217711,2.554633,-6.250014,-0.407104,8.095166,3.981411,-0.026959,-7.742283,-7.733137,-8.574063,4.125635,4.847673,-1.567692,-9.379608,-6.327526,9.536203,7.246179,-8.805967,-7.851883,-2.017388,-8.991687,-0.367553,4.149441,0.863697,-1.958073,1.979163,8.347590,-8.518518,-9.085193,8.646852,6.527508,-7.225052,0.623205,-7.363685,5.285586,-5.151961,-8.947393,-3.820937,0.567206,-4.844006,4.827029,2.272483,-6.196548,-7.653268,0.157238,8.149199,-2.451015,5.954472,-7.953246,-9.440934,-1.113488,6.546751,3.996200,-2.700635,-4.179140,6.777796,2.707959,-4.929256,-2.419157,-5.477193,1.394131,2.788497,-7.793280,0.734927,-8.554078,-0.160750,-3.697690,-1.868136,-3.790065,4.934850,2.306552,-6.409757,9.093262,-7.013656,-8.333171,8.779021,-1.671581,8.357244,2.703492,-5.675256,-7.783184,-2.230904,-0.738468,5.393936,-6.985359,2.123954,9.933650,-9.047837,0.329602,-9.564469,7.934708,8.884802,-9.050119,-5.642983,0.485677,-1.868706,-2.984628,4.940940,6.341472,8.155351,1.639905,4.205610,-3.989148,2.807485,-3.774352,0.075636,-0.823871,5.211422,-7.064702,-6.650543,-2.198927,2.760050,-0.807117,-6.639121,7.310399,8.193779,-0.645055,9.736638,-3.958200,-4.963771,1.400676,-2.672519,-6.385430,-8.265659,-4.722057,4.908638,1.018887,6.367165,0.092852,8.157574,9.087300,0.773856,6.052531,-3.131453,2.500689,-4.878864,5.370302,-4.838726,1.133837,-8.987815,-0.212827,-5.196228,-0.328116,5.296388,5.829295,7.553092,8.247678,7.840533,8.025419,-5.902383,-7.416866,9.561377,3.191832,-6.026057,1.688188,-3.909390,-4.314814,0.524516,-5.776853,-7.618331,-2.011745,-0.698318,-1.040414,-9.436342,-3.489984,-1.477723,-9.331865,-2.481717,-8.574370,-5.842156,5.070471,0.674785,9.920198,-8.497437,5.911330,-4.850628,-8.118641,3.561218,-2.680559,6.301240,-1.213526,4.435178,2.009661,-6.038240,-0.874487,5.508635,-0.843770,9.918667,-7.235082,6.663722,-7.242249,1.420465,0.726067,9.012989,-8.044458,-2.830760,4.820142,0.695439,5.573754,-4.740917,-9.019449,7.080767,-4.211406,5.511261,-1.993845,-9.588123,-9.918794,-2.554235,-8.054467,0.429554,-9.475602,4.015406,5.646885,-6.229355,-1.645565,3.031746,5.110621,7.941205,5.062598,-7.532980,-8.726907,7.133285,-6.017740,-6.112304,5.370709,4.663896,7.024355,0.097282,-3.472498,0.209690,-3.332870,0.349382,2.054974,8.036458,5.822969,-2.394168,-0.407729,-2.231835,3.557066,1.098411,-8.697849,-9.352048,7.409353,8.272689,-7.422134,8.983859,7.208875,-9.664143,1.685237,5.807426,7.901191,-4.103682,3.178859,-7.608388,4.558538,-2.362614,-3.180518,9.211828,-4.218147,6.955981,5.880732,-9.953567,-5.257909,1.611326,-4.049599,-9.717307,4.693596,-3.981384,-4.503837,0.658966,-9.900397,0.361443,0.723648,0.070517,4.306488,-3.605256,8.646350,3.352204,0.628394,6.509122,-1.172384,3.083911,3.136558,-4.609121,-3.387990,8.693493,9.663014,2.633465,-5.551135,8.676276,-8.498864,-9.601971,-5.261181,4.386827,2.125571,0.300526,-4.299495,4.181852,-1.354497,4.636664,1.754323,-7.815828,-6.450577,4.888310,-3.249677,-1.528302,-9.056542,-2.976855,3.537047,-0.769065,-2.888822,-4.102760,-9.702570,-6.455846,6.334720,0.774264,5.928133,-4.486386,-8.027698,-0.876893,-4.509088,0.923801,3.239989,9.462846,2.758390,8.649021,0.876818,-0.365725,3.608704,2.899890,3.483133,-1.792971,-9.705274,-8.485921,-1.141390,1.236243,8.868011,-1.505341,-0.836169,8.050583,3.726981,9.089882,-7.996348,7.870830,7.556484,7.655375,1.468140,1.489785,-2.059967,-4.781561,-6.727161,2.259034,-7.996383,-4.967767,3.240831,-3.679789,3.260635,1.702102,-6.982529,9.771447,6.197299,-1.653689,-2.645229,-0.294002,5.808884,-5.439539,-4.708843,5.714380,3.462614,2.665380,-0.650412,7.808946,-9.411351,6.784943,8.004311,-9.141719,8.894747,-2.535127,-5.232470,-0.393161,6.361182,4.385118,-5.961141,8.698953,-1.721861,-7.984943,-3.175967,-1.398309,9.029570,6.366599,6.028672,3.096152,-3.801489,-4.262395,9.257129,-2.769079,4.393825,-8.225372,3.257854,8.581683,5.535392,-0.673760,-5.473954,-2.803717,-0.455614,-6.568930,5.869411,2.508328,6.912244,-3.569704,-7.297258,-7.459055,-3.787184,-0.549682,-0.550517,6.725059,6.702308,7.174835,3.267007,9.626123,-1.990290,9.950718,-6.141900,4.653734,-5.841201,-4.827829,5.189504,4.788260,7.429680,6.175341,4.234505,5.389750,-4.940020,-8.855761,-1.020012,4.876633,-4.228496,-4.279461,7.230068,-6.038148,8.727303,3.661606,2.105132,-8.221683,-6.215910,-9.951876,6.330293,-2.938106,5.774871,6.332438,4.536050,-7.556787,7.203953,-0.916837,-9.111964,-1.851271,2.116785,-7.366630,-5.039513,5.221039,-3.931709,0.797233,-1.912579,0.336817,-1.626265,1.899997,-4.042540,7.684542,7.885707,-1.090253,5.217208,2.802682,-0.965490,9.159215,9.012569,3.278506,3.399502,1.681313,0.783538,5.570928,9.966182,4.415023,-5.630903,2.825156,-3.124914,0.967987,-9.283353,-9.813939,1.827397,-9.926599,-7.401752,-9.228873,-7.368690,0.530902,2.502158,9.830219,-5.917493,-3.306982,-7.495980,-5.019298,9.555380,-3.638145,-7.178768,1.085754,-1.975925,-3.196300,0.214412,-8.228467,-3.282181,1.991245,-5.164591,-9.030123,7.978617,3.902983,-2.043558,-5.333328,-7.361971,-9.410298,0.238194,-5.480469,5.720045,6.461353,2.231537,-0.829531,0.156770,0.622496,-4.727714,-3.889977,-0.884701,2.789850,1.221085,3.847752,-1.465100,7.576471,1.589525,-2.602462,-4.704404,2.526789,4.733354,-8.324623,-0.442510,1.515358,5.907220,-4.809453,2.182974,9.636587,-6.831637,-4.266376,-4.020740,-3.432162,3.415876,-4.894830,-9.762665,-5.079320,7.889743,9.567654,-3.212048,-3.898532,-4.489183,-6.006010,1.417015,7.514430,-5.779171,-9.327633,9.294779,-6.377755,8.474016,-9.324681,-9.188394,-6.162411,5.709281,6.578349,-2.425166,-7.222850,5.153734,-8.122662,-3.050309,-0.841993,-0.895236,4.881907,1.941757,-8.484808,-4.273834,2.948418,9.594109,-9.213769,3.817809,3.625815,9.574667,-0.624437,-5.430129,4.903056,-4.746734,5.723106,2.121605,-1.517704,-2.186911,5.935126,-4.253274,2.220001,-7.670401,-9.300898,-4.930676,0.519505,0.152262,-1.865189,0.184659,-7.113520,0.016683,-0.355595,-5.302866,2.554851,2.174031,3.037777,7.509826,-3.778510,-3.286616,5.349337,-2.249102,5.178187,9.768048,5.288872,7.314835,-0.436956,5.899986,7.577304,-4.297767,-2.137383,-9.368466,0.535650,-8.517166,6.765006,-2.220554,0.986677,-0.801458,4.579607,-2.148305,-2.006411,-3.659125,-6.867986,0.453584,-6.473270,6.883944,7.783096,-3.572368,8.737980,-9.585908,-7.217563,-0.789418,4.963469,-4.133329,-9.207233,5.462137,-6.391406,0.778047,4.851235,5.128437,-9.589638,-1.575176,-0.021103,-0.384924,-3.274607,-8.644033,-5.121403,-6.346881,2.654549,-8.700595,-0.661595,-2.142405,2.693974,4.253525,-4.973906,-7.519943,5.804797,9.696878,-3.690870,-0.583884,-3.828650,6.155198,2.576972,5.958490,-8.036805,-5.679560,2.224015,5.015824,-4.107459,-6.256633,4.917185,-2.826126,9.280543,-4.460767,6.761341,-2.273988,-6.829238,-1.497004,-6.564315,-7.634704,4.910145,7.756237,-7.651032,-8.770817,0.631205,8.325013,5.950753,-5.022993,1.132300,-5.203715,8.119434,3.581479,-1.724940,0.251257,9.268406,8.297026,-7.276075,0.634091,-1.863511,8.241948,-4.547594,-1.448201,-9.284223,6.477482,-4.523884,5.967069,-6.533123,7.194031,-4.120056,5.877674,-1.263758,8.356575,7.323320,2.699119,-7.148444,-2.189329,-5.050306,-7.290376,8.180789,-0.517740,-4.059461,7.120884,-1.971163,0.783210,7.295110,-7.047982,-6.436400,-5.462127,1.438285,5.599735,-3.071877,-9.759490,-6.759412,-3.343331,-6.112391,4.428931,-8.790847,-5.188965,2.372540,1.475702,-6.354310,6.471580,9.965098,0.188019,4.381833,-9.697166,-1.941619,-7.707829,-3.979333,-9.088110,-8.321120,6.973850,-8.639582,1.677123,3.762925,-4.863732,0.389176,-2.470735,1.917528,9.101231,-1.225124,-6.533095,-0.643932,-4.505243,4.616247,-7.267741,-3.783326,-4.131968,0.361213,6.561957,9.301048,-5.061065,4.857407,8.120336,-1.392317,0.356967,8.450165,5.625181,7.569174,-3.112058,-6.062862,-2.457508,-9.103007,1.801906,-0.346331,-2.950736,-4.091811,-3.949562,-2.452169,-6.034734,-8.199705,3.534379,-4.879142,-5.919842,-2.361873,-8.776110,6.339542,-7.425576,-0.459159,9.098668,-5.978941,-6.878739,-1.128439,-7.663554,-0.075734,-5.131578,-6.796374,-3.463198,-4.988293,-6.216686,5.767759,-7.074733,1.880520,-5.966070,-8.768805,0.432006,-2.035217,-3.438552,-8.677637,9.641652,5.205765,-4.624576,5.083925,-9.783567,1.962447,4.507589,-5.742540,6.603705,-7.846271,9.771766,0.546078,5.324581,-1.161806,-6.428965,-6.915164,2.197735,0.103315,8.547099,2.611630,5.227745,5.160815,5.109746,-3.433101,4.074252,0.191728,5.351238,6.972532,-9.107406,-9.056445,8.886903,-9.350551,6.332828,-7.485001,-6.150557,-5.824777,-7.088071,-9.061365,2.639235,-2.752568,0.365182,4.238314,-1.069971,3.617904,-4.943495,5.944501,-1.150399,3.288621,-2.156225,0.297673,1.348723,-2.458331,6.033926,8.319248,5.256868,8.340221,3.325490,3.396231,-1.660063,-7.300474,8.445367,-9.354516,1.246941,5.388645,5.085040,1.882137,-0.118465,-3.623630,-4.975248,3.385321,5.229471,6.625313,0.934069,-8.438754,4.921653,9.908223,-9.781335,4.636965,4.198540,0.380065,3.232933,8.258181,-7.051668,6.268092,1.338935,-6.797250,0.783787,-1.276680,8.716865,-4.798133,7.678109,1.594553,9.943458,-6.815314,4.287245,1.028975,-8.825411,-1.468739,-8.567296,1.033677,-2.988704,-7.093861,2.998460,3.001585,2.632611,-0.207683,5.203262,7.780295,-9.658191,4.009926,8.301449,-7.034060,5.531094,8.191891,-6.460922,0.325323,-2.744426,-3.406000,-0.821556,-7.632126,-4.995041,0.869530,-9.791690,-7.596722,-1.265322,-8.324822,8.730679,7.126241,-8.767040,-8.245151,7.055928,2.480308,-2.680544,-9.367978,5.261647,-6.859211,5.655521,6.683898,-7.915650,-9.465783,8.229374,3.103802,3.392990,1.615109,7.801136,-1.890020,-4.310267,-3.694127,6.722990,4.789673,-4.343786,-9.341958,9.819389,4.866647,-5.124193,-6.737716,4.838188,-4.496619,-7.670527], dtype = "float32")#candidate|7111|(1936,)|const|float32
call_7110 = relay.TupleGetItem(func_2264_call(relay.reshape(const_7111.astype('float32'), [11, 16, 11]), relay.reshape(const_7111.astype('float32'), [11, 16, 11]), ), 0)
call_7112 = relay.TupleGetItem(func_2268_call(relay.reshape(const_7111.astype('float32'), [11, 16, 11]), relay.reshape(const_7111.astype('float32'), [11, 16, 11]), ), 0)
func_6363_call = mod.get_global_var('func_6363')
func_6366_call = mutated_mod.get_global_var('func_6366')
const_7115 = relay.const([-3,3,2,6,-3,-2,-2,8,-8,6,-3,3,-8,3,5,5,-6,-1,-2,-4,8,9,3,-9,-8,2,1,-9,2,8,1,7,-4,8,7,-1,2,-4,-9,5,-7,-1,10,-9,1,2,-3,-9,-7,-10,-3,-1,3,9,10,9,8,-8,-9,3,-4,-2,-5,-1,10,-9,6,-7,7,1,7,-5,-2,-5,7,3,-4,10,7,-2,-7,-1,2,10,-3,7,2,7,4,-7,2,4,-6,-5,-8,-4,-1,5,-5,3,7,2,-3,-5,2,7,1,-10,-8,2,6,-8,-10,-10,-10,-5,-4,-8,5,-1,-5,-1,-2,3,-7,-3,-8,-8,7,-3,3,-6,4,-4,-5,-6,-5,-7,9,4,-5,-9,-9,-1,-6,-3,-4,-6,3,5,-4,10,-9,6,-7,4,-9,-4,3,-7,2,8,1,2,5,-3,2,10,-10,-9,-9,8,-7,8,-8,9,-7,5,4,-3,9,-9,7,10,6,-4,-4,4,-5,-1,9,6,-10,5,10,-2,4,-8,1,-10,-7,3,-9,3,9,-8,8,6,4,-2,1,-1,-5,8,7,4,-4,-7,4,-6,8,3,9,1,-1,8,-9,9,-10,-10,4,-4,1,-1,5,-9,-1,-6,2,-6,4,-6,-6,7,-1,6,-10,-6,-4,-7,-4,2,7,-8,7,3,-7,-4,-4,-1,-7,2,7,-10,5,-10,2,-4,9,-9,5,10,10,7,5,1,-2,9,3,10,5,-6,-1,-5,2,1,-5,-1,4,-9,3,1,4,-5,-9,6,-7,10,-5,-10,-10,-6,3,10,-3,-8,-10,4,-1,3,-5,6,1,2,5,-5,-7,10,8,7,8,10,6,-3,2,-7,-5,3,-10,-4,-8,-10,9,3,9,-9,-7,6,-10,8,-3,2,-9,3,-9,6,5,-2,-5,2,-7,2,9,-7,7,2,2,9,9,3,-1,7,7,2,6,-8,4,-9,2,-1,-1,8,-9,5,10,-7,-10,-7,-4,9,-3,-5,10,8,-7,-10,4,-2,-4,-10,-8,5,1,-5,9,5,2,8,3,4,7,-10,2,3,-10,2,9,-4,-7,5,2,9,1,7,-5,4,5,-2,-6,4,-9,-2,2,-1,6,7,10,-5,3,-3,-3,10,-10,6,9,-2,8,9,1,-1,7,-8,-3,-8,-4,-7,-9,-6,1,-7,-6,9,2,-4,-9,3,-2,-3,-3,-5,1,4,9,10,-4,10,-5,-3,-8,-3,1,-3,8,-2,-8,-6,7,8,1,-5,7,4,4,-1,4,9,2,10,7,-9,-9,3,-8,-1,1,4,3,1,5,10,-6,7,-1,5,9,3,2,3,9,7,-1,-9,10,2,2,5,10,-5,8,-9,8,6,-7,8,-4,9,7,-10,10,2,-5,-9,10,-4,-7,-7,4,-3,-2,-1,9,4,10,4,-7,1,5,4,7,4,-2,9,6,-1,4,-7,-1,-10,4,-2,-10,10,6,-1,-4,7,7,4,-7,-4,-4,-5,-1,-8,6,-5,-5,-2,-8,6,-7,8,8,-9,-4,9,5,6,8,2,-6,-10,1,5,-6,-3,-3,-9,2,7,3,7,9,-6,7,-1,-5,7,-7,-5,-1,-6,-9,5,-2,-1,-8,5,-10,-4,-10,-2,-10,-1,1,-7,-6,7,7,9,4,-6,-8,2,3,7,-5,-8,-9,-1,7,-1,1,10,-9,7,1,-8,6,7,9,3,-4,-8,-2,-3,7,1,3,-5,-2,-8,8,4,-5,3,6,8,7,-2,3,7,1,-9,1,7,-10,8,10,-2,-2,10,1,7,4,-8,-5,8,-4,2,-2,-3,-5,-8,3,-1,7,3,9,-7,-9,9,-1,-4,3,2,-5,6,6,-5,6,-5,5,-2,-8,-5,-5,5,-1,-10,-4,-10,9,-9,9,-3,-9,-1,-6,1,1,3,2,9,6,8,6,-9,3,8,-1,1,1,8,-3,1,5,-8,-1,-2,10,5,7,9,-1,4,-9,-3,6,-8,-10,-3,-3,4,1,1,6,-5,9,7,-2,3,5,-4,7,10,-2,-4,5,1,4,7,-7,6,-6,-7,3,4,5,-1,-1,-2,5,10,-2,7,-2,-7,-5,-8,-6,-3,-4,-9,4,-3,-2,-10,1,-8,-10,10,-7,4,9,-5,6,4,-5,-10,2,4,8,-10,3,-1,-10,4,7,-1,9,-3,-6,-6,1,-9,-7,4,8,-4,1,3,-6,1,6,-4,-10,1,-6,-6,-1,8,10,5,8,-9,7,-10,-1,-8,5,-4,-9,-8], dtype = "uint8")#candidate|7115|(864,)|const|uint8
call_7114 = relay.TupleGetItem(func_6363_call(relay.reshape(const_7115.astype('uint8'), [864,])), 6)
call_7116 = relay.TupleGetItem(func_6366_call(relay.reshape(const_7115.astype('uint8'), [864,])), 6)
output = relay.Tuple([call_7084,call_7105,var_7106,var_7107,var_7108,call_7110,const_7111,call_7114,const_7115,])
output2 = relay.Tuple([call_7085,call_7109,var_7106,var_7107,var_7108,call_7112,const_7111,call_7116,const_7115,])
func_7123 = relay.Function([var_7106,var_7107,var_7108,], output)
mod['func_7123'] = func_7123
mod = relay.transform.InferType()(mod)
var_7124 = relay.var("var_7124", dtype = "float64", shape = (90,))#candidate|7124|(90,)|var|float64
var_7125 = relay.var("var_7125", dtype = "float64", shape = (60,))#candidate|7125|(60,)|var|float64
var_7126 = relay.var("var_7126", dtype = "float32", shape = (144, 1))#candidate|7126|(144, 1)|var|float32
output = func_7123(var_7124,var_7125,var_7126,)
func_7127 = relay.Function([var_7124,var_7125,var_7126,], output)
mutated_mod['func_7127'] = func_7127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4065_call = mod.get_global_var('func_4065')
func_4066_call = mutated_mod.get_global_var('func_4066')
call_7142 = func_4065_call()
call_7143 = func_4065_call()
func_3199_call = mod.get_global_var('func_3199')
func_3201_call = mutated_mod.get_global_var('func_3201')
const_7145 = relay.const([6.558501,4.963936,1.919900,2.667821,-9.335690,-5.541181,7.334214,0.853577,-6.701101,-9.447088,-3.933102,-4.100774,5.548948,6.998601,9.170426,6.518265,-1.498413,7.393385,5.997009,5.968531,-7.456021,0.248559,6.138629,8.225530,-7.519013,-9.095476,5.492413,6.299712,4.598891,2.731765,2.293466,7.036471,-9.306161,-1.604617,-5.517803,1.836556,4.245013,-0.945295,0.111320,-6.435381,3.672953,-4.885420,2.649762,9.939840,-7.988626,-5.839553,-8.569530,-7.518257,-2.659991,-6.663303,-7.772875,7.210163,-4.891381,-9.697005,5.519021,0.081959,9.132519,1.987789,2.692551,-7.793761,-9.505078,-5.214519,-1.189130,4.238900,6.389375,5.083941,3.005723,4.694648,-4.548911,-7.634131,6.416837,-9.003306,6.883334,6.042075,2.695462,5.502798,-7.768391,-7.418892,-1.737776,-4.163014,7.941523,5.637378,-4.411842,-1.719760,-4.375657,5.075797,4.632799,4.673423,7.627643,0.902182,-9.246959,-9.312955,-4.703210,2.674754,-9.995113,-7.771958], dtype = "float64")#candidate|7145|(96,)|const|float64
call_7144 = relay.TupleGetItem(func_3199_call(relay.reshape(const_7145.astype('float64'), [3, 16, 2])), 0)
call_7146 = relay.TupleGetItem(func_3201_call(relay.reshape(const_7145.astype('float64'), [3, 16, 2])), 0)
bop_7149 = relay.minimum(call_7142.astype('int8'), call_7144.astype('int8')) # shape=(3, 16, 2)
bop_7152 = relay.minimum(call_7143.astype('int8'), call_7146.astype('int8')) # shape=(3, 16, 2)
const_7169 = relay.const([[[False,False],[False,True],[True,False],[True,True],[True,True],[True,True],[True,False],[False,True],[True,True],[True,True],[True,True],[False,False],[True,True],[True,False],[False,True],[True,False]],[[True,True],[True,True],[True,False],[False,False],[True,True],[True,True],[False,True],[False,True],[False,False],[False,True],[True,False],[True,True],[False,True],[True,False],[False,False],[False,True]],[[True,False],[False,False],[False,True],[False,False],[False,True],[True,False],[False,True],[True,False],[True,True],[False,True],[False,True],[False,False],[False,True],[False,False],[False,False],[False,True]]], dtype = "bool")#candidate|7169|(3, 16, 2)|const|bool
bop_7170 = relay.floor_mod(call_7144.astype('float32'), relay.reshape(const_7169.astype('float32'), relay.shape_of(call_7144))) # shape=(3, 16, 2)
bop_7173 = relay.floor_mod(call_7146.astype('float32'), relay.reshape(const_7169.astype('float32'), relay.shape_of(call_7146))) # shape=(3, 16, 2)
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_7176 = relay.TupleGetItem(func_1609_call(), 0)
call_7177 = relay.TupleGetItem(func_1611_call(), 0)
func_3857_call = mod.get_global_var('func_3857')
func_3860_call = mutated_mod.get_global_var('func_3860')
const_7181 = relay.const([-4.297447,5.122780,-7.064202,-5.352660,-2.941228,-2.820131,-7.739934,8.392425,-4.635148,4.572491,2.181926,0.461226,8.592770,4.815513,-1.354350,3.064925,7.526669,2.268332,6.234159,6.453088,-6.332998,3.980999,-4.952856,-5.184325,-6.167251,0.526085,4.622614,3.704554,-4.242278,9.351237,9.674006,4.973096,1.150591,5.586156,-5.452643,-3.057541,-5.717067,0.601022,-8.507370,3.618676,-0.758428,-3.259420,8.402788,-9.819625,-7.207158,-8.087018,-2.691733,-2.346531,1.991986,7.755198,4.437925,-2.546035,5.063066,-0.611520,0.966572,-7.957622,4.436881,6.057804,-8.657365,-9.830785,6.200631,-8.838638,8.195715,8.738696,-4.410431,-2.690816,-0.338624,9.558800,8.800552,-7.729575,-0.074253,-9.725487], dtype = "float64")#candidate|7181|(72,)|const|float64
const_7182 = relay.const([3,-6,-10,-8,-1,2,-5,-2,-5,8,9,-3,2,1,-4,-4,2,1,8,-1,-2,1,-7,10,5,6,-6,9,4,1,-6,4,-7,-4,-6,-2,-7,8,5,7,-8,4,-1,-3,2,-10,8,-8,9,-10,4,-3,-4,-4,9,-8,4,10,-6,-8,-8,9,-4,-3,-7,-8,-6,2,4,-8,9,9,-8,7,-5,-4,-5,10,-8,-2,7,-7,-3,-2,5,1,4,7,10,-7,1,9,-2,7,6,-6,1,8,2,-2,-8,1,2,5,2,-8,-1,10,10,5,9,8,5,-6,6,4,-1,-7,2,7,-3,-6,-4,2,-4,-9,-10,-2,5,-4,6,-4,-2,9,4,-8,3,-5,-10,2,-4,8,-1,1,-8,6,2,2,2,9,-7,5,3,-8,7,-1,-10,4,-9,7,9,-3,5,6,7,5,6,-6,2,-4,-2,9,-3,-5,-10,-4,-8,-4,2,-2,7,5,-9,-2,2,9,2,8,-5,-10,7,-7,-10,-2,1,5,1,-1,10,-3,-3,8,2,-3,-3,3,-8,9,-9,2,2,8,-7,8,-4,4,5,5,10,-6,2,4,-10,-7,3,9,-9,3,-5,5,-1,-9,1,-4,1,-5,-9,-2,-4,-6,-8,-4,-1,3,7,-7,9,5,-1,2,-8,6,9,-6,7,-2,8,-4,-3,7,6,-8,-2,-4,1,7,-2,9,-9,4,9,-2,2,-6,-2,-6,-8,3,7,-3,3,2,-2,-7,-5,8,-9,-3,-6,-9,-1,-9,7,-9,1,-5,-3,-10,-7,8,9,8,-8,-10,-9,7,2,-8,-9,-5,2,-3,-6,-10,9,5,-5,6,3,10,-7,-1,-4,-9,-8,1,4,-5,-6,-1,4,-5,-8,-4,8,-2,-2,3,-2,7,7,-9,4,1,-8,9,10,-1,-2,1,1,-5,6,9,8,-7,-5,-6,-8,-3,1,8,-3,-2,-4,-6,-6,-7,7,-10,1,-10,2,7,6,8,-9,1,-5,-8,-5,7,-3,4,10,5,-1,-10,-4,5,-7,7,9,-10,10,7,-2,7,-9,-7,6,2,8,10,-3,2,-8,-7,-9,-3,-5,-4,-3,4,3,2,-1,5,-8,-3,-8,2,8,-2,6,-3,6,-10,8,2,3,-1,10,-6,-10,1,8,5,3,-2,-3,-10,4,-1,-1,-6,-8,-1,-2,7,9,-2,-1,2,2,-3,-1,-7,2,-7,-2,-9,1,-9,8,5,-5,-4,-3,2,-10,-4,5,-6,-9,2,-6,-2,-3,-10,-8,-8,-3,9,9,-3,6,10,9,10,8,1,-7,1,-3,-10,-9,4,-1,9,-6,-6,10,-4,1,8,10,-3,10,6,8,-6,4,-10,3,-2,-4,1,-8,2,3,-9,7,7,-10,3,-8,-7,-9,7,8,2,10,5,-2,-7,9,5,10,5,4,-9,9,5,7,-1,-1,-7,8,-1,1,5,-4,5,-4,-5,10,-3,4,-8], dtype = "uint8")#candidate|7182|(560,)|const|uint8
call_7180 = relay.TupleGetItem(func_3857_call(relay.reshape(const_7181.astype('float64'), [4, 6, 3]), relay.reshape(const_7182.astype('uint8'), [4, 140]), ), 2)
call_7183 = relay.TupleGetItem(func_3860_call(relay.reshape(const_7181.astype('float64'), [4, 6, 3]), relay.reshape(const_7182.astype('uint8'), [4, 140]), ), 2)
output = relay.Tuple([const_7145,bop_7149,bop_7170,call_7176,call_7180,const_7181,const_7182,])
output2 = relay.Tuple([const_7145,bop_7152,bop_7173,call_7177,call_7183,const_7181,const_7182,])
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
func_6913_call = mod.get_global_var('func_6913')
func_6914_call = mutated_mod.get_global_var('func_6914')
call_7246 = relay.TupleGetItem(func_6913_call(), 0)
call_7247 = relay.TupleGetItem(func_6914_call(), 0)
func_5918_call = mod.get_global_var('func_5918')
func_5919_call = mutated_mod.get_global_var('func_5919')
call_7254 = relay.TupleGetItem(func_5918_call(), 0)
call_7255 = relay.TupleGetItem(func_5919_call(), 0)
var_7272 = relay.var("var_7272", dtype = "float64", shape = (3, 16, 2))#candidate|7272|(3, 16, 2)|var|float64
bop_7273 = relay.divide(call_7246.astype('float32'), relay.reshape(var_7272.astype('float32'), relay.shape_of(call_7246))) # shape=(3, 16, 2)
bop_7276 = relay.divide(call_7247.astype('float32'), relay.reshape(var_7272.astype('float32'), relay.shape_of(call_7247))) # shape=(3, 16, 2)
func_3730_call = mod.get_global_var('func_3730')
func_3732_call = mutated_mod.get_global_var('func_3732')
call_7280 = relay.TupleGetItem(func_3730_call(), 1)
call_7281 = relay.TupleGetItem(func_3732_call(), 1)
output = relay.Tuple([call_7254,bop_7273,call_7280,])
output2 = relay.Tuple([call_7255,bop_7276,call_7281,])
func_7284 = relay.Function([var_7272,], output)
mod['func_7284'] = func_7284
mod = relay.transform.InferType()(mod)
var_7285 = relay.var("var_7285", dtype = "float64", shape = (3, 16, 2))#candidate|7285|(3, 16, 2)|var|float64
output = func_7284(var_7285)
func_7286 = relay.Function([var_7285], output)
mutated_mod['func_7286'] = func_7286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4900_call = mod.get_global_var('func_4900')
func_4901_call = mutated_mod.get_global_var('func_4901')
call_7331 = relay.TupleGetItem(func_4900_call(), 0)
call_7332 = relay.TupleGetItem(func_4901_call(), 0)
output = call_7331
output2 = call_7332
func_7335 = relay.Function([], output)
mod['func_7335'] = func_7335
mod = relay.transform.InferType()(mod)
mutated_mod['func_7335'] = func_7335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7335_call = mutated_mod.get_global_var('func_7335')
call_7336 = func_7335_call()
output = call_7336
func_7337 = relay.Function([], output)
mutated_mod['func_7337'] = func_7337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_7367 = relay.TupleGetItem(func_1327_call(), 0)
call_7368 = relay.TupleGetItem(func_1329_call(), 0)
func_5002_call = mod.get_global_var('func_5002')
func_5004_call = mutated_mod.get_global_var('func_5004')
call_7371 = relay.TupleGetItem(func_5002_call(), 0)
call_7372 = relay.TupleGetItem(func_5004_call(), 0)
bop_7376 = relay.bitwise_or(call_7367.astype('uint16'), relay.reshape(call_7371.astype('uint16'), relay.shape_of(call_7367))) # shape=(3, 1, 2)
bop_7379 = relay.bitwise_or(call_7368.astype('uint16'), relay.reshape(call_7372.astype('uint16'), relay.shape_of(call_7368))) # shape=(3, 1, 2)
func_3580_call = mod.get_global_var('func_3580')
func_3582_call = mutated_mod.get_global_var('func_3582')
call_7407 = func_3580_call()
call_7408 = func_3580_call()
func_5956_call = mod.get_global_var('func_5956')
func_5957_call = mutated_mod.get_global_var('func_5957')
call_7409 = relay.TupleGetItem(func_5956_call(), 0)
call_7410 = relay.TupleGetItem(func_5957_call(), 0)
var_7425 = relay.var("var_7425", dtype = "float64", shape = (3, 11, 2))#candidate|7425|(3, 11, 2)|var|float64
bop_7426 = relay.subtract(call_7407.astype('uint64'), var_7425.astype('uint64')) # shape=(3, 11, 2)
bop_7429 = relay.subtract(call_7408.astype('uint64'), var_7425.astype('uint64')) # shape=(3, 11, 2)
func_6363_call = mod.get_global_var('func_6363')
func_6366_call = mutated_mod.get_global_var('func_6366')
const_7434 = relay.const([-7,-2,1,-6,-3,4,3,5,4,-9,-4,2,2,5,-7,1,3,10,-1,8,7,9,2,3,8,2,9,-6,-4,-10,3,-6,7,2,-4,-3,6,3,5,-3,8,-7,-7,-7,-3,-5,-8,-5,-9,-2,-9,6,-6,3,-4,4,-10,-10,-1,-10,-4,3,8,-9,-2,9,-8,9,5,3,8,1,8,7,-8,6,-1,-6,-4,5,-5,-1,1,-7,2,6,-7,6,-8,-7,-9,8,1,-1,8,2,4,8,-3,-2,5,3,-6,-9,3,3,-8,-5,7,-5,6,8,-3,5,-1,1,4,-8,-6,-7,5,-2,-10,-4,-5,-2,10,-8,8,9,10,-5,-7,-7,2,-1,-1,-1,-1,10,6,6,-3,9,8,3,1,4,-5,-8,-4,-5,3,8,1,-8,9,2,-10,5,10,-8,6,-8,5,-7,4,-4,7,9,-7,4,-4,-7,-9,2,10,10,-6,-6,-4,-9,-6,7,4,-1,6,-8,2,-3,-10,10,-9,-6,1,-5,9,-7,-9,-8,2,-8,5,-9,5,-7,10,-5,-2,-3,4,-1,-4,-8,3,-9,-5,5,5,6,5,5,5,-4,10,1,5,-7,-10,-5,-10,10,-3,5,9,10,-9,9,4,10,-1,9,2,-9,10,-5,-10,8,-10,-3,-6,-2,7,-6,7,6,8,-7,3,1,10,6,3,-5,-8,-1,-1,-9,6,-1,3,2,5,10,-5,-3,-8,-7,4,-3,8,7,9,-10,-1,-10,8,-6,3,-3,8,5,5,-7,4,9,4,-3,-2,-9,-2,7,-5,5,10,8,3,4,-5,-5,10,1,2,8,7,-6,10,-10,-6,-3,-4,4,6,3,8,-10,-4,4,-7,7,-4,2,6,-9,9,-1,-4,-10,3,-2,1,-1,7,8,-10,7,-10,9,4,-8,-1,6,4,-8,9,-9,-5,5,6,5,2,3,4,-6,10,-1,-7,-10,5,9,1,-6,8,8,9,-3,9,1,-6,2,-2,-8,-10,-9,8,10,-8,6,10,-2,-7,-7,9,-10,4,-2,4,7,-10,-10,-8,8,7,-2,5,-5,8,-1,-2,3,-2,4,7,-2,2,5,-2,-6,4,7,3,-6,-6,10,-7,-5,10,-6,3,-5,-10,4,3,1,7,9,-2,1,-1,7,5,-8,3,5,-2,2,-1,3,8,3,4,5,6,-5,6,6,5,-10,2,4,-4,-5,5,-8,4,6,3,3,7,8,-1,9,-2,2,-2,7,3,10,-2,10,-10,-1,10,-4,-3,2,-9,-7,8,5,6,-8,4,8,8,9,6,1,-5,3,-7,1,6,7,9,-5,-3,-5,-3,-2,-3,-9,4,-5,4,8,-2,7,9,3,-7,-5,3,7,5,7,2,-8,-7,-7,10,-2,6,-2,7,-5,6,-5,9,7,3,5,1,4,-6,-8,-8,-1,-4,-1,8,5,5,-5,2,-10,7,2,9,-5,-9,-5,5,-3,-9,-10,-10,3,5,-10,1,3,7,7,3,5,6,9,6,-10,6,-3,7,2,7,10,-5,-7,10,10,-7,5,5,-7,-8,7,1,10,8,-7,-5,-3,9,5,-4,-5,10,-8,-8,7,6,-9,3,-2,-3,-6,-5,1,8,5,10,5,-2,6,-10,5,8,10,5,-2,2,-9,6,-2,5,-6,-9,-7,-6,2,-8,1,-1,7,6,2,-7,4,10,-8,5,-2,-7,-7,1,-8,-4,-3,3,-9,-9,-6,4,4,5,-3,-5,5,3,4,1,3,4,-10,-5,-7,-2,5,-10,1,8,-6,-8,-7,-2,7,7,-7,-5,10,-8,6,-10,7,7,-7,-4,2,-1,5,1,5,1,9,-2,7,5,-9,4,7,6,10,5,3,10,1,1,1,9,7,-10,1,-6,2,-8,3,1,7,-5,3,-10,7,10,3,-10,3,3,-5,6,-10,4,-10,9,2,10,7,8,9,-6,9,3,3,-6,6,6,8,-3,9,-8,4,-6,5,-9,-4,-9,8,-7,-7,-1,-4,-2,9,3,-5,-8,-6,-2,-8,7,5,-7,9,5,-6,2,-3,4,-8,-9,5,-4,2,4,-8,-2,-1,5,2,6,6,9,2,1,-8,5,-8,6,8,7,-3,10,-1,-1,-4,-2,7,-10,-3,-9,1,-6,-4,6,2,-9,-4,8,3,-8,-10,-9,-10,-6,-10,-7,10,8,6,7,7,5,-2,-9,-4,-3,-7,-1,-3,-1,-3,-4,2,8,-7,-7,10,8,-7,-8,3,-5,-6,-7,-5], dtype = "uint8")#candidate|7434|(864,)|const|uint8
call_7433 = relay.TupleGetItem(func_6363_call(relay.reshape(const_7434.astype('uint8'), [864,])), 5)
call_7435 = relay.TupleGetItem(func_6366_call(relay.reshape(const_7434.astype('uint8'), [864,])), 5)
bop_7438 = relay.maximum(const_7434.astype('float64'), call_7433.astype('float64')) # shape=(864,)
bop_7441 = relay.maximum(const_7434.astype('float64'), call_7435.astype('float64')) # shape=(864,)
func_5693_call = mod.get_global_var('func_5693')
func_5694_call = mutated_mod.get_global_var('func_5694')
call_7442 = relay.TupleGetItem(func_5693_call(), 0)
call_7443 = relay.TupleGetItem(func_5694_call(), 0)
func_2760_call = mod.get_global_var('func_2760')
func_2763_call = mutated_mod.get_global_var('func_2763')
var_7448 = relay.var("var_7448", dtype = "float32", shape = (144,))#candidate|7448|(144,)|var|float32
call_7447 = relay.TupleGetItem(func_2760_call(relay.reshape(var_7448.astype('float32'), [144,])), 2)
call_7449 = relay.TupleGetItem(func_2763_call(relay.reshape(var_7448.astype('float32'), [144,])), 2)
func_1327_call = mod.get_global_var('func_1327')
func_1329_call = mutated_mod.get_global_var('func_1329')
call_7451 = relay.TupleGetItem(func_1327_call(), 0)
call_7452 = relay.TupleGetItem(func_1329_call(), 0)
output = relay.Tuple([bop_7376,call_7409,bop_7426,bop_7438,call_7442,call_7447,var_7448,call_7451,])
output2 = relay.Tuple([bop_7379,call_7410,bop_7429,bop_7441,call_7443,call_7449,var_7448,call_7452,])
func_7461 = relay.Function([var_7425,var_7448,], output)
mod['func_7461'] = func_7461
mod = relay.transform.InferType()(mod)
var_7462 = relay.var("var_7462", dtype = "float64", shape = (3, 11, 2))#candidate|7462|(3, 11, 2)|var|float64
var_7463 = relay.var("var_7463", dtype = "float32", shape = (144,))#candidate|7463|(144,)|var|float32
output = func_7461(var_7462,var_7463,)
func_7464 = relay.Function([var_7462,var_7463,], output)
mutated_mod['func_7464'] = func_7464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6051_call = mod.get_global_var('func_6051')
func_6053_call = mutated_mod.get_global_var('func_6053')
call_7484 = func_6051_call()
call_7485 = func_6051_call()
output = call_7484
output2 = call_7485
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
var_7539 = relay.var("var_7539", dtype = "int8", shape = (6, 10, 5))#candidate|7539|(6, 10, 5)|var|int8
var_7540 = relay.var("var_7540", dtype = "int8", shape = (6, 10, 5))#candidate|7540|(6, 10, 5)|var|int8
bop_7541 = relay.bitwise_and(var_7539.astype('int8'), relay.reshape(var_7540.astype('int8'), relay.shape_of(var_7539))) # shape=(6, 10, 5)
uop_7544 = relay.exp(bop_7541.astype('float32')) # shape=(6, 10, 5)
uop_7546 = relay.log(var_7540.astype('float64')) # shape=(6, 10, 5)
func_1789_call = mod.get_global_var('func_1789')
func_1792_call = mutated_mod.get_global_var('func_1792')
var_7549 = relay.var("var_7549", dtype = "float64", shape = (1, 60))#candidate|7549|(1, 60)|var|float64
var_7550 = relay.var("var_7550", dtype = "float32", shape = (144,))#candidate|7550|(144,)|var|float32
call_7548 = relay.TupleGetItem(func_1789_call(relay.reshape(var_7549.astype('float64'), [60,]), relay.reshape(var_7550.astype('float32'), [144,]), ), 1)
call_7551 = relay.TupleGetItem(func_1792_call(relay.reshape(var_7549.astype('float64'), [60,]), relay.reshape(var_7550.astype('float32'), [144,]), ), 1)
func_5380_call = mod.get_global_var('func_5380')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_7553 = relay.TupleGetItem(func_5380_call(), 4)
call_7554 = relay.TupleGetItem(func_5382_call(), 4)
output = relay.Tuple([uop_7544,uop_7546,call_7548,var_7549,var_7550,call_7553,])
output2 = relay.Tuple([uop_7544,uop_7546,call_7551,var_7549,var_7550,call_7554,])
func_7558 = relay.Function([var_7539,var_7540,var_7549,var_7550,], output)
mod['func_7558'] = func_7558
mod = relay.transform.InferType()(mod)
var_7559 = relay.var("var_7559", dtype = "int8", shape = (6, 10, 5))#candidate|7559|(6, 10, 5)|var|int8
var_7560 = relay.var("var_7560", dtype = "int8", shape = (6, 10, 5))#candidate|7560|(6, 10, 5)|var|int8
var_7561 = relay.var("var_7561", dtype = "float64", shape = (1, 60))#candidate|7561|(1, 60)|var|float64
var_7562 = relay.var("var_7562", dtype = "float32", shape = (144,))#candidate|7562|(144,)|var|float32
output = func_7558(var_7559,var_7560,var_7561,var_7562,)
func_7563 = relay.Function([var_7559,var_7560,var_7561,var_7562,], output)
mutated_mod['func_7563'] = func_7563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3258_call = mod.get_global_var('func_3258')
func_3260_call = mutated_mod.get_global_var('func_3260')
call_7580 = func_3258_call()
call_7581 = func_3258_call()
func_1803_call = mod.get_global_var('func_1803')
func_1805_call = mutated_mod.get_global_var('func_1805')
call_7588 = relay.TupleGetItem(func_1803_call(), 0)
call_7589 = relay.TupleGetItem(func_1805_call(), 0)
var_7597 = relay.var("var_7597", dtype = "float64", shape = (3, 6, 2))#candidate|7597|(3, 6, 2)|var|float64
bop_7598 = relay.minimum(call_7588.astype('int32'), var_7597.astype('int32')) # shape=(3, 6, 2)
bop_7601 = relay.minimum(call_7589.astype('int32'), var_7597.astype('int32')) # shape=(3, 6, 2)
output = relay.Tuple([call_7580,bop_7598,])
output2 = relay.Tuple([call_7581,bop_7601,])
func_7602 = relay.Function([var_7597,], output)
mod['func_7602'] = func_7602
mod = relay.transform.InferType()(mod)
var_7603 = relay.var("var_7603", dtype = "float64", shape = (3, 6, 2))#candidate|7603|(3, 6, 2)|var|float64
output = func_7602(var_7603)
func_7604 = relay.Function([var_7603], output)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6804_call = mod.get_global_var('func_6804')
func_6806_call = mutated_mod.get_global_var('func_6806')
call_7649 = relay.TupleGetItem(func_6804_call(), 0)
call_7650 = relay.TupleGetItem(func_6806_call(), 0)
func_5584_call = mod.get_global_var('func_5584')
func_5587_call = mutated_mod.get_global_var('func_5587')
var_7652 = relay.var("var_7652", dtype = "bool", shape = (1920,))#candidate|7652|(1920,)|var|bool
call_7651 = relay.TupleGetItem(func_5584_call(relay.reshape(var_7652.astype('bool'), [1920,])), 1)
call_7653 = relay.TupleGetItem(func_5587_call(relay.reshape(var_7652.astype('bool'), [1920,])), 1)
var_7668 = relay.var("var_7668", dtype = "float64", shape = (3, 16, 2))#candidate|7668|(3, 16, 2)|var|float64
bop_7669 = relay.mod(call_7649.astype('float64'), var_7668.astype('float64')) # shape=(3, 16, 2)
bop_7672 = relay.mod(call_7650.astype('float64'), var_7668.astype('float64')) # shape=(3, 16, 2)
output = relay.Tuple([call_7651,var_7652,bop_7669,])
output2 = relay.Tuple([call_7653,var_7652,bop_7672,])
func_7675 = relay.Function([var_7652,var_7668,], output)
mod['func_7675'] = func_7675
mod = relay.transform.InferType()(mod)
mutated_mod['func_7675'] = func_7675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7675_call = mutated_mod.get_global_var('func_7675')
var_7677 = relay.var("var_7677", dtype = "bool", shape = (1920,))#candidate|7677|(1920,)|var|bool
var_7678 = relay.var("var_7678", dtype = "float64", shape = (3, 16, 2))#candidate|7678|(3, 16, 2)|var|float64
call_7676 = func_7675_call(var_7677,var_7678,)
output = call_7676
func_7679 = relay.Function([var_7677,var_7678,], output)
mutated_mod['func_7679'] = func_7679
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7824 = relay.var("var_7824", dtype = "float32", shape = (3, 14, 11))#candidate|7824|(3, 14, 11)|var|float32
uop_7825 = relay.sqrt(var_7824.astype('float32')) # shape=(3, 14, 11)
uop_7830 = relay.asin(uop_7825.astype('float64')) # shape=(3, 14, 11)
output = uop_7830
output2 = uop_7830
func_7839 = relay.Function([var_7824,], output)
mod['func_7839'] = func_7839
mod = relay.transform.InferType()(mod)
var_7840 = relay.var("var_7840", dtype = "float32", shape = (3, 14, 11))#candidate|7840|(3, 14, 11)|var|float32
output = func_7839(var_7840)
func_7841 = relay.Function([var_7840], output)
mutated_mod['func_7841'] = func_7841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2153_call = mod.get_global_var('func_2153')
func_2154_call = mutated_mod.get_global_var('func_2154')
call_7845 = relay.TupleGetItem(func_2153_call(), 0)
call_7846 = relay.TupleGetItem(func_2154_call(), 0)
func_6051_call = mod.get_global_var('func_6051')
func_6053_call = mutated_mod.get_global_var('func_6053')
call_7851 = func_6051_call()
call_7852 = func_6051_call()
func_1609_call = mod.get_global_var('func_1609')
func_1611_call = mutated_mod.get_global_var('func_1611')
call_7861 = relay.TupleGetItem(func_1609_call(), 0)
call_7862 = relay.TupleGetItem(func_1611_call(), 0)
output = relay.Tuple([call_7845,call_7851,call_7861,])
output2 = relay.Tuple([call_7846,call_7852,call_7862,])
func_7864 = relay.Function([], output)
mod['func_7864'] = func_7864
mod = relay.transform.InferType()(mod)
mutated_mod['func_7864'] = func_7864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7864_call = mutated_mod.get_global_var('func_7864')
call_7865 = func_7864_call()
output = call_7865
func_7866 = relay.Function([], output)
mutated_mod['func_7866'] = func_7866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6051_call = mod.get_global_var('func_6051')
func_6053_call = mutated_mod.get_global_var('func_6053')
call_7867 = func_6051_call()
call_7868 = func_6051_call()
output = relay.Tuple([call_7867,])
output2 = relay.Tuple([call_7868,])
func_7869 = relay.Function([], output)
mod['func_7869'] = func_7869
mod = relay.transform.InferType()(mod)
mutated_mod['func_7869'] = func_7869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7869_call = mutated_mod.get_global_var('func_7869')
call_7870 = func_7869_call()
output = call_7870
func_7871 = relay.Function([], output)
mutated_mod['func_7871'] = func_7871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7877 = relay.var("var_7877", dtype = "uint64", shape = (12, 11, 13))#candidate|7877|(12, 11, 13)|var|uint64
var_7878 = relay.var("var_7878", dtype = "uint64", shape = (12, 11, 13))#candidate|7878|(12, 11, 13)|var|uint64
bop_7879 = relay.not_equal(var_7877.astype('bool'), relay.reshape(var_7878.astype('bool'), relay.shape_of(var_7877))) # shape=(12, 11, 13)
func_5677_call = mod.get_global_var('func_5677')
func_5680_call = mutated_mod.get_global_var('func_5680')
const_7887 = relay.const([6.921393,4.952496,-5.239806,-6.143724,-9.544979,-7.540281,-4.434248,3.083244,6.293558,8.785361,6.590918,-2.600171,-3.585022,-0.699322,-0.552426,-2.633755,-8.665878,-1.433355,-0.537828,-2.570386,7.051796,4.283192,-5.241204,0.019609,0.669158,-1.171378,-7.787838,-2.102993,-6.222232,-2.245065,-5.963103,-6.085900,-3.962118,7.524256,8.019644,1.322402,-3.091008,4.552141,4.476527,0.571948,3.594110,7.624634,-1.138846,9.655740,0.290547,-6.356872,-3.435817,-8.400503,5.019872,6.460599,5.958380,5.167789,4.990470,-5.654615,4.372513,5.350049,9.329614,-4.003904,3.267955,3.894091,9.760295,-9.984497,-1.809729,-7.149707,6.550805,5.830717,-9.955262,-3.722441,6.596845,8.244447,-3.217495,9.224469,4.113663,-3.402379,8.571463,1.373334,6.054068,-7.409549,-3.643159,4.012529,-9.264646,-9.047651,1.043142,-5.464852,-1.573845,5.658150,3.061273,-3.666561,4.365472,4.544301,-4.502865,8.393623,-7.728970,-2.934817,6.302911,-0.310403,-4.128564,-1.910360,-8.430411,-1.667877,-4.286454,2.928068,-3.850437,0.117852,-9.698569,8.427452,0.337632,-8.986689,-3.152022,8.396095,-7.664556,-1.685351,-3.868133,-5.544986,1.742588,3.040421,5.513291,7.701130,3.477599,6.879762,7.752699,-8.794234,0.505160,1.705937,2.706938,2.435372,-3.344889,-4.550256,4.716944,8.890476,6.795775,-6.733060,-7.374475,3.134433,-4.686072,1.656818,6.448258,2.823215,8.825591,-0.677714,9.946780,-9.183807,7.300728,-5.966351,-6.013527,-9.061683,9.670783,-4.002417,-0.225611,1.700052,-9.502131,6.019148,-8.798420,-4.598606,7.948201,9.592339,1.577685,-5.823934,-0.336297,1.762345,9.957638,9.162444,-2.862090,-3.136174,3.941436,-9.328673,-7.860047,8.940575,-8.081342,-0.118972,-3.637100,-0.122330,-1.192361,2.223639,5.583625,7.571389,-7.056039,0.307795,-2.408009,3.704279,0.751408,4.351524,4.302954,6.485835,-2.010726,6.742127,5.696042,-1.311048,5.246099,-4.764371,-8.145334,1.967195,-1.413835,-4.684438,-6.261914,-6.217777,8.264242,3.728623,-5.813467,-5.013381,9.889329,-1.601277,5.438870,-5.669969,-2.878414,9.158542,-5.858043,8.033042,-2.830177,1.245614,9.283366,-0.275438,6.750353,-1.681958,-1.442250,-0.218475,-7.248110,-6.601996,-9.863044,-7.841436,-2.485487,4.667715,-0.277885,0.414220,-0.303336,1.685923,9.994542,-6.450459,-8.822511,-0.791405,2.544617,-6.458417,5.658546,8.901643,9.624427,-4.321111,-3.277287,-7.209897,-5.290227,8.897282,-0.502025,8.156335,-4.497176,-0.279827,-6.465825,-1.126108,0.373001,1.405125,9.068141,-4.516442,4.763474,-9.925637,1.394352,-3.182324,9.746187,-4.610944,6.743701,4.188617,-3.233229,-0.998162,-7.678343,-0.152832,7.423934,1.088331,8.778066,9.856314,-0.404447,-3.325609,-7.274744,-3.946945,-7.383088,6.709556,-6.695119,4.064614,-7.548877,7.930766,-5.014994,-8.145233,1.317697,5.554931,-5.317121,3.957856,-3.367396,-4.052521,2.755219,-9.255129,9.484743,8.176264,-2.784263,-3.808687,-9.009235,-0.133690,-1.114715,-0.392066,-3.548641,-0.444351,-1.653622,6.375552,4.307796,2.029246,-2.326280,-5.220110,9.823739,3.869848,-2.098007,-0.582691,7.786075,-6.399338,7.909682,-8.871778,-5.894384,-2.492631,-8.707188,9.770309,3.080732,-2.754576,4.975613,-2.571253,-5.824667,-2.932186,0.608377,5.218087,2.111527,-3.607196,-2.037425,-7.365126,4.701120,1.837914,0.690910,9.104164,4.534768,-7.300428,-6.064800,3.422709,2.444613,-2.726611,-0.114393,6.720382,6.460375,0.808176,-3.785728,-0.086820,-3.778650,-2.570934,-5.386712,7.642706,1.858798,-1.900016,-2.156490,0.437575,-6.270570,-2.778264,0.577788,-9.913818,-8.738966,8.320225,-3.617289,-6.494476,8.072572,-6.342659,1.874185,-5.620597,5.248060,-9.300082,-6.777465,4.604038,5.635694,-5.774076,-5.490361,1.400131,-1.664554,0.764485,-0.238791,9.714377,-5.478469,-0.990616,5.719481,9.332397,0.954965,-0.425323,9.148547,-6.373849,-4.200130,7.277060,-6.268552,1.498739,0.726852,5.106283,-0.226026,-3.170864,-9.776273,-0.023743,6.014762,-5.312402,-2.634677,-2.160132,9.890464,-8.727901,0.658946,-0.787036,8.685023,-8.065185,-1.831582,-1.346392,0.525997,-6.916446,7.856557,9.700957,-5.719686,-7.526791,7.792049,-3.452719,0.861709,-6.995629,-6.781656,-4.218368,-0.916232,7.750617,-1.576335,3.559871,-8.677349,4.399818,3.188326,-8.546157,2.612010,-7.542027,8.579298,7.230493,5.647669,-9.809652,-8.955487,0.849936,0.309035,6.840796,3.304199,9.357006,-0.445826,2.036819,-8.272890,5.705450,-9.231749,-0.604232,-6.066160,4.963668,3.666516,-6.020140,-2.277523,-1.393241,-4.247331,-5.012598,-5.845237,1.802053,-0.750491,-0.317496,-8.681382,-3.259646,6.217620,-5.634303,-4.855169,-5.987032,3.453735,6.851748,-4.439926,-4.365779,-3.139152,-7.197706,-7.633081,4.073325,1.661708,5.012710,-6.725457,-5.236926,-5.407119,4.822147,-2.130846,-2.323780,-6.830317,-2.461144,2.462214,8.828156,0.570490,4.860798,3.158552,-8.955603,-2.057628,-9.344335,-0.882331,7.868988,-0.190429,4.019932,-2.180330,-3.252591,-6.581483,7.370313,3.902624,9.469811,2.949703,3.200286,3.598376,5.696434,4.319390,-9.760607,-9.606745,0.257915,0.101409,-5.330471,-0.725927,-5.764331,5.632075,3.399004,2.081713,3.706350,2.131546,4.026284,-1.373875,-2.205792,5.737992,0.529209,-6.117959,-8.219828,-4.329112,7.251925,2.437649,7.680889,-2.365360,-1.576786,8.031393,-1.495002,-5.917549,8.371619,-3.714644,-3.940798,1.326497,7.516847,-8.101006,2.869817,-5.454584,-3.807488,-0.876867,-8.986773,-4.211071,-5.307412,-3.017128,-0.951511,8.692025,-2.202626,0.042710,1.529448,-5.066915,9.512786,-8.197398,4.756661,5.311743,-7.015110,3.918062,-3.781642,2.608524,2.289388,6.386407,-4.479803,-1.274945,-9.905133,-6.523683,-0.423839,1.382891,6.534075,-0.837200,-7.952224,-9.492064,6.453557,-8.205287,8.351941,8.647818,9.974702,-8.503511,8.044317,-9.305090,1.282690,7.558766,-6.709414,4.196348,-2.863229,-6.288042,1.004534,5.302478,2.674757,4.035303,-5.492640,2.584627,6.072449,6.051094,-5.418727,4.104874,-0.138331,4.876652,1.527560,4.312400,-2.620070,-0.428992,-1.435581,3.606294,3.189347,1.033396,6.332844,-2.653999,-9.201630,5.074754,3.791486,-2.796146,4.449823,-7.413166,-0.309433,-2.368584,-6.435578,4.076317,-9.811884,-9.507851,7.280428,3.697191,-3.272174,0.775848,-0.557731,-9.734951,5.423445,7.204088,-4.387659,9.095035,0.082014,-0.494678,6.801959,7.935518,-3.188607,8.621218,3.698895,-4.473812,-2.692711,-5.234940,-3.459926,6.720732,-0.584738,-5.262487,-5.659859,9.339157,3.391045,1.862789,3.249576,-2.000883,-3.961488,0.998378,0.408393,-2.891245,-4.455289,-4.372370,2.311706,-7.371721,-7.164028,-4.296073,6.764440,1.196269,7.059929,0.682609,0.634731,-7.776533,0.641903,2.999445,0.329724,9.748293,-8.345459,-4.010337,4.052275,2.262594,6.643771,-2.530189,-9.999824,8.838698], dtype = "float32")#candidate|7887|(675,)|const|float32
call_7886 = func_5677_call(relay.reshape(const_7887.astype('float32'), [9, 5, 15]))
call_7888 = func_5677_call(relay.reshape(const_7887.astype('float32'), [9, 5, 15]))
func_3580_call = mod.get_global_var('func_3580')
func_3582_call = mutated_mod.get_global_var('func_3582')
call_7891 = func_3580_call()
call_7892 = func_3580_call()
bop_7896 = relay.power(call_7886.astype('float64'), relay.reshape(const_7887.astype('float64'), relay.shape_of(call_7886))) # shape=(9, 5, 15)
bop_7899 = relay.power(call_7888.astype('float64'), relay.reshape(const_7887.astype('float64'), relay.shape_of(call_7888))) # shape=(9, 5, 15)
func_1041_call = mod.get_global_var('func_1041')
func_1046_call = mutated_mod.get_global_var('func_1046')
const_7915 = relay.const([5,-1,-5,-5,9,-1,-10,10,-7,-2,-10,-6,2,-9,-9,-2,-2,-5,1,-3,4,5,-8,5,-4,4,3,-8,1,-7,-10,5,10,-9,2,3,-8,9,5,-1,4,-3,-5,-9,2,7,2,6,-1,-5,8,10,-8,2,-4,2,-6,2,-10,8,-6,-4,6,-2,-6,2,7,-10,3,-8,-2,-5,-9,-2,10,9,-6,6,-4,8,7,3,-4,-1,-2,-3,3,-7,-7,-9,10,4,-4,5,-1,9,-7,-4,-5,9,5,-6,-10,-1,9,-5,-2,4,-1,4,-3,2,7,-10,-2,-2,1,-7,8,-9,10,5,-4,7,-7,7,-6,-8,6,3,-7,7,2,10,-4,6,-4,5,1,3,-3,-8,1,9,-5,7,9,9,-10,9,7,-9,8,7,5,7,-2,8,10,3,2,-7,-8,4,3,-3,1,-1,7,8,10,2,8,-5,9,-4,-10,4,7,-5,1,3,1,1,-2,9,-2,-1,-3,1,-6,3,-5,-5,2,3,9,5,9,-7,-5,-2,7,9,2,10,-6,6,-9,-6,-1,6,6,-8,-9,6,1,-5,1,-10,6,3,-4,-7,-7,6,3,-8,7,-4,2,2,-7,-6,1,-1,6,10,2,5,-10,9,-4,2,4,-8,7,-2,9,3,3,-8,8,1,7,1,-4,3,-7,9,-3,10,7,4,-9,5,-1,-1,2,10,7,-9,2,-8,6,-10,4,-1,-1,6,-10,-4,-5,1,-8,-7,2,5,-7,-3,-2,-6,-5,9,9,-10,8,1,10,3,5,-2,-7,3,1,10,10,-2,-2,3,-8,-2,6,4,-5,3,-8,-7,3,10,7,-9,-8,2,-4,1,9,-10,7,10,-10,4,-7,2,2,-3,-4,5,-5,-1,-5,3,-6,-8,7,-8,10,-5,-4,6,1,-4,4,-6,-10,10,-7,-7,5,7,3,1,7,10,-2,-7,8,5,-5,-2,8,-8,4,10,-1,3,4,7,9,3,6,4,5,5,-2,3,-9,-7,-8,-4,7,5,3,-3,1,-6,9,-10,-9,4,-2,-3,10,5,8,1,9,5,7,-6,7,5,10,-2,-10,4,3,-2,7,5,7,9,1,7,5,8,5,-9,9,-6,6,-9,-7,-6,-10,-8,-4,-4,2,-2,-5,8,-4,-5,-8,9,10,5,-3,-2,1,-2,8,1,-5,8,5,-10,-2,-1,-7,-4,-2,-4,1,8,7,-8,-3,-6,4,-2,9,10,-6,-2,5,10,5,2,2,-8,9,-4,7,-5,-4,-1,-9,-4,6,-8,2,-6,-3,-4,10,6,8,-4,-1,-7,3,8,1,-7,-10,5,6,-10,2,6,6,1,-3,10,-1,-1,-6,-8,-2,1,-1,-3,-10,8,7,-3,-5,10,9,-3,8,7,-2,-1,2,-6,8,2,4,-9,-3,7,-9,7,8,8,-4,10,-2,2,-2,-6,10,10,7,7,4,-9,1,-10,-8,7,-3,-7,9,-6,-10,3,2,3,3,-3,-6,-9,-10,7,7,-9,-2,-5,8,4,-8,7,10,-3,-2,9,9,-4,-9,7,7,-10,4,2,1,-1,4,-10,10,7,-10,-7,-8,-9,3,5,-2,1,-10,-2,-2,9,3,-10,3,-2,-8,3,3,3,6,8,-4,-7,-3,-7,-4,-10,-6,-7,-2,3,9,5,7,-7,-5,2,3,6,-10,2,-9,-10,-7,-5,5,8,-5,-7,-1,5,9,-7,-1,-2,-6,-7,-7,10,-4,-2,5,7,2,-2,8,1,7,4,1,-8,-10,-1,-2,10,8,-4,-3,4,-5,-8,-4,-2,7,8,10,4,-1,-7,-6,8,3,8,5,1,8,2,-8,-4], dtype = "uint64")#candidate|7915|(704,)|const|uint64
const_7916 = relay.const([[10,-2,-1,-3,-7,2,4,-6,-9,8,-6,-1,5,-1,7,-5,-1,7,5,10,2,-2,1,-5,4,-10,-4,-7,6,1,3,-10,2,-10,-1,9,-2,2,-10,6,2,4,-6,-6,1,6,5,2,-5,-2,-3,-10,3,-10,10,-7,-3,10,-4,-2,6,-2,-3,-6,-7,5,-1,-6,-8,7],[4,2,-7,-9,-1,-9,-8,-7,7,9,4,-5,10,1,-2,8,6,-5,6,-5,4,3,-7,1,6,10,-6,6,8,4,10,8,-3,9,5,-6,8,-1,2,8,3,-5,-5,-3,-10,5,-10,-6,-3,2,-8,9,10,8,-1,7,6,-1,4,-4,-2,6,1,4,-8,-4,-5,-10,-2,-4],[-9,-6,-4,6,2,2,-10,-5,2,-6,6,-7,-4,7,-9,10,-3,-1,-5,2,-6,3,-7,-8,8,1,4,4,-7,6,1,4,-4,10,1,-7,10,-4,8,8,-5,-9,-7,9,-5,1,-10,-1,-9,4,-3,-10,2,-10,7,-6,6,-1,10,8,4,-3,-4,9,-5,7,3,-3,-3,-7],[10,1,1,-9,-4,8,8,-2,-6,-10,-1,9,4,1,2,8,-1,9,2,5,-7,-2,4,1,-5,9,8,2,-9,-1,-10,4,-9,7,3,7,-7,-6,5,1,8,7,-9,2,-1,8,6,-7,4,-6,6,-6,-6,-3,2,2,3,8,6,7,-6,3,6,-7,-3,-7,8,-1,-6,9],[6,7,-9,-3,-8,-6,-7,4,-8,6,-4,10,4,10,6,7,-9,3,-3,6,-9,4,3,1,-1,-3,-8,8,-6,4,-8,-6,-7,-6,7,2,6,4,-5,1,2,2,-10,-3,-1,-10,2,-5,-5,1,-4,-8,8,2,-6,1,8,9,-4,-6,-3,-3,10,-6,-10,5,-10,6,4,3],[-10,10,-8,8,5,-8,-8,-3,-8,3,4,3,2,3,-7,10,1,-5,-10,4,5,-4,-2,3,-4,9,6,-3,1,-6,2,-6,-5,3,-4,-1,-10,5,-1,-3,5,-4,-6,-9,3,-7,-1,-10,-4,4,-2,10,-9,4,-3,5,-3,-9,8,-7,-5,-7,-7,-5,-10,2,5,3,-7,3],[8,-10,-9,-9,8,9,2,2,-3,-2,-7,6,-6,-5,8,5,-6,-6,-5,-1,2,-6,5,4,6,-2,8,-4,-9,-9,5,-2,10,-5,2,8,7,10,2,2,8,1,-6,-2,2,-1,-7,9,10,6,1,9,8,9,-1,-9,9,-7,-5,-9,2,5,2,1,-7,7,9,-5,5,-8],[-9,7,9,2,-3,-4,-8,4,-2,-3,10,-8,-5,-7,-8,-7,3,2,8,-9,-4,5,1,-3,4,3,-7,-2,-3,5,5,-8,-7,-2,4,-5,-4,10,10,8,1,-8,6,1,1,1,-9,6,-9,1,10,2,8,9,7,-2,1,-5,1,8,-3,8,8,-9,2,2,8,6,-8,-6]], dtype = "uint8")#candidate|7916|(8, 70)|const|uint8
call_7914 = relay.TupleGetItem(func_1041_call(relay.reshape(const_7915.astype('uint64'), [16, 11, 4]), relay.reshape(const_7915.astype('uint64'), [16, 11, 4]), relay.reshape(const_7916.astype('uint8'), [560,]), ), 2)
call_7917 = relay.TupleGetItem(func_1046_call(relay.reshape(const_7915.astype('uint64'), [16, 11, 4]), relay.reshape(const_7915.astype('uint64'), [16, 11, 4]), relay.reshape(const_7916.astype('uint8'), [560,]), ), 2)
output = relay.Tuple([bop_7879,call_7891,bop_7896,call_7914,const_7915,const_7916,])
output2 = relay.Tuple([bop_7879,call_7892,bop_7899,call_7917,const_7915,const_7916,])
func_7924 = relay.Function([var_7877,var_7878,], output)
mod['func_7924'] = func_7924
mod = relay.transform.InferType()(mod)
mutated_mod['func_7924'] = func_7924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7924_call = mutated_mod.get_global_var('func_7924')
var_7926 = relay.var("var_7926", dtype = "uint64", shape = (12, 11, 13))#candidate|7926|(12, 11, 13)|var|uint64
var_7927 = relay.var("var_7927", dtype = "uint64", shape = (12, 11, 13))#candidate|7927|(12, 11, 13)|var|uint64
call_7925 = func_7924_call(var_7926,var_7927,)
output = call_7925
func_7928 = relay.Function([var_7926,var_7927,], output)
mutated_mod['func_7928'] = func_7928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1704_call = mod.get_global_var('func_1704')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_7939 = func_1704_call()
call_7940 = func_1704_call()
var_7968 = relay.var("var_7968", dtype = "float64", shape = (66,))#candidate|7968|(66,)|var|float64
bop_7969 = relay.floor_divide(call_7939.astype('float64'), relay.reshape(var_7968.astype('float64'), relay.shape_of(call_7939))) # shape=(66,)
bop_7972 = relay.floor_divide(call_7940.astype('float64'), relay.reshape(var_7968.astype('float64'), relay.shape_of(call_7940))) # shape=(66,)
output = bop_7969
output2 = bop_7972
func_7984 = relay.Function([var_7968,], output)
mod['func_7984'] = func_7984
mod = relay.transform.InferType()(mod)
mutated_mod['func_7984'] = func_7984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7985 = relay.var("var_7985", dtype = "float64", shape = (66,))#candidate|7985|(66,)|var|float64
func_7984_call = mutated_mod.get_global_var('func_7984')
call_7986 = func_7984_call(var_7985)
output = call_7986
func_7987 = relay.Function([var_7985], output)
mutated_mod['func_7987'] = func_7987
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8055 = relay.var("var_8055", dtype = "float32", shape = (2, 12, 4))#candidate|8055|(2, 12, 4)|var|float32
uop_8056 = relay.sinh(var_8055.astype('float32')) # shape=(2, 12, 4)
func_6823_call = mod.get_global_var('func_6823')
func_6825_call = mutated_mod.get_global_var('func_6825')
call_8058 = relay.TupleGetItem(func_6823_call(), 0)
call_8059 = relay.TupleGetItem(func_6825_call(), 0)
output = relay.Tuple([uop_8056,call_8058,])
output2 = relay.Tuple([uop_8056,call_8059,])
func_8061 = relay.Function([var_8055,], output)
mod['func_8061'] = func_8061
mod = relay.transform.InferType()(mod)
var_8062 = relay.var("var_8062", dtype = "float32", shape = (2, 12, 4))#candidate|8062|(2, 12, 4)|var|float32
output = func_8061(var_8062)
func_8063 = relay.Function([var_8062], output)
mutated_mod['func_8063'] = func_8063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5918_call = mod.get_global_var('func_5918')
func_5919_call = mutated_mod.get_global_var('func_5919')
call_8071 = relay.TupleGetItem(func_5918_call(), 0)
call_8072 = relay.TupleGetItem(func_5919_call(), 0)
func_3308_call = mod.get_global_var('func_3308')
func_3311_call = mutated_mod.get_global_var('func_3311')
var_8074 = relay.var("var_8074", dtype = "bool", shape = (1920,))#candidate|8074|(1920,)|var|bool
call_8073 = func_3308_call(relay.reshape(var_8074.astype('bool'), [16, 8, 15]), relay.reshape(var_8074.astype('bool'), [16, 8, 15]), )
call_8075 = func_3308_call(relay.reshape(var_8074.astype('bool'), [16, 8, 15]), relay.reshape(var_8074.astype('bool'), [16, 8, 15]), )
output = relay.Tuple([call_8071,call_8073,var_8074,])
output2 = relay.Tuple([call_8072,call_8075,var_8074,])
func_8076 = relay.Function([var_8074,], output)
mod['func_8076'] = func_8076
mod = relay.transform.InferType()(mod)
mutated_mod['func_8076'] = func_8076
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8077 = relay.var("var_8077", dtype = "bool", shape = (1920,))#candidate|8077|(1920,)|var|bool
func_8076_call = mutated_mod.get_global_var('func_8076')
call_8078 = func_8076_call(var_8077)
output = call_8078
func_8079 = relay.Function([var_8077], output)
mutated_mod['func_8079'] = func_8079
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8110 = relay.var("var_8110", dtype = "float32", shape = ())#candidate|8110|()|var|float32
var_8111 = relay.var("var_8111", dtype = "float32", shape = (1, 6, 16))#candidate|8111|(1, 6, 16)|var|float32
bop_8112 = relay.power(var_8110.astype('float32'), var_8111.astype('float32')) # shape=(1, 6, 16)
uop_8115 = relay.cos(var_8111.astype('float32')) # shape=(1, 6, 16)
output = relay.Tuple([bop_8112,uop_8115,])
output2 = relay.Tuple([bop_8112,uop_8115,])
func_8118 = relay.Function([var_8110,var_8111,], output)
mod['func_8118'] = func_8118
mod = relay.transform.InferType()(mod)
var_8119 = relay.var("var_8119", dtype = "float32", shape = ())#candidate|8119|()|var|float32
var_8120 = relay.var("var_8120", dtype = "float32", shape = (1, 6, 16))#candidate|8120|(1, 6, 16)|var|float32
output = func_8118(var_8119,var_8120,)
func_8121 = relay.Function([var_8119,var_8120,], output)
mutated_mod['func_8121'] = func_8121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3580_call = mod.get_global_var('func_3580')
func_3582_call = mutated_mod.get_global_var('func_3582')
call_8147 = func_3580_call()
call_8148 = func_3580_call()
uop_8151 = relay.rsqrt(call_8147.astype('float32')) # shape=(3, 1, 2)
uop_8153 = relay.rsqrt(call_8148.astype('float32')) # shape=(3, 1, 2)
output = relay.Tuple([uop_8151,])
output2 = relay.Tuple([uop_8153,])
func_8156 = relay.Function([], output)
mod['func_8156'] = func_8156
mod = relay.transform.InferType()(mod)
mutated_mod['func_8156'] = func_8156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8156_call = mutated_mod.get_global_var('func_8156')
call_8157 = func_8156_call()
output = call_8157
func_8158 = relay.Function([], output)
mutated_mod['func_8158'] = func_8158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6438_call = mod.get_global_var('func_6438')
func_6439_call = mutated_mod.get_global_var('func_6439')
call_8165 = relay.TupleGetItem(func_6438_call(), 1)
call_8166 = relay.TupleGetItem(func_6439_call(), 1)
uop_8176 = relay.sin(call_8165.astype('float32')) # shape=(3, 16, 2)
uop_8178 = relay.sin(call_8166.astype('float32')) # shape=(3, 16, 2)
output = relay.Tuple([uop_8176,])
output2 = relay.Tuple([uop_8178,])
func_8188 = relay.Function([], output)
mod['func_8188'] = func_8188
mod = relay.transform.InferType()(mod)
mutated_mod['func_8188'] = func_8188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8188_call = mutated_mod.get_global_var('func_8188')
call_8189 = func_8188_call()
output = call_8189
func_8190 = relay.Function([], output)
mutated_mod['func_8190'] = func_8190
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8205 = relay.var("var_8205", dtype = "float64", shape = (8, 8, 5))#candidate|8205|(8, 8, 5)|var|float64
uop_8206 = relay.atan(var_8205.astype('float64')) # shape=(8, 8, 5)
func_2760_call = mod.get_global_var('func_2760')
func_2763_call = mutated_mod.get_global_var('func_2763')
const_8214 = relay.const([7.016764,-5.560455,-1.296338,5.162335,7.806043,-6.342762,-3.230946,-0.684630,-7.035786,2.969715,5.781730,8.484307,-2.474418,-5.681867,-6.831633,-8.203484,-1.309472,3.235378,3.912486,-6.965291,-2.490859,-8.543782,-6.655841,5.597378,0.012646,0.157098,-4.592482,-9.072784,7.262333,-6.120643,3.388684,2.236022,8.352990,-0.074004,-4.051659,8.757824,3.209694,0.790547,7.048289,6.657887,3.976044,3.822737,1.137559,9.345018,1.812433,-4.129472,-1.369693,-5.714802,-0.254939,-2.221894,3.831873,-7.614498,-4.715105,7.867373,-9.813818,-6.447300,8.525870,-8.420306,-3.838926,-8.436459,8.303430,-4.283722,-4.455477,-0.434497,4.407291,0.731051,-3.497328,2.952507,-1.320968,-4.365220,7.523607,-2.954728,1.546035,1.934944,-7.035589,1.335565,9.898427,2.518685,-8.188134,-3.796437,1.252334,8.540771,3.206429,-4.178178,5.363252,1.526602,5.074121,5.065416,-8.382130,-1.960219,-5.698264,-9.148836,6.989796,-4.353879,2.948007,1.088607,-7.030242,4.231594,-1.914115,3.439957,-3.473196,-2.652174,5.070047,-3.837837,5.482731,-2.590642,-6.274263,7.352090,9.731686,-9.693801,-4.202211,8.401363,-5.974752,9.328769,-4.236299,-1.247135,8.845433,-5.958228,-8.424141,-1.649975,-8.739110,-5.933352,4.559303,-8.677251,7.523875,-7.182120,0.472273,-4.302963,-7.183128,-1.801885,7.848139,1.971099,6.658062,0.567228,1.921455,5.167375,-4.250979,-9.514512,1.701232,-1.804732,6.216860,3.839956,-2.810131,-6.635126], dtype = "float32")#candidate|8214|(144,)|const|float32
call_8213 = relay.TupleGetItem(func_2760_call(relay.reshape(const_8214.astype('float32'), [144,])), 1)
call_8215 = relay.TupleGetItem(func_2763_call(relay.reshape(const_8214.astype('float32'), [144,])), 1)
func_1907_call = mod.get_global_var('func_1907')
func_1910_call = mutated_mod.get_global_var('func_1910')
const_8221 = relay.const([9,-2,4,-6,-4,8,-6,9,-9,-8,5,8,-4,-6,-10,-6,-10,-5,-2,1,-7,-7,4,-10,-10,-1,8,1,-4,1,-9,4,7,-6,-2,7,5,-4,-2,2,-5,-7,2,6,-6,-9,6,-6,5,-4,-8,6,-6,2,7,10,-5,-6,8,3,1,-10,-7,1,-10,-9,-5,2,7,7,-8,-5,-7,-9,5,8,-6,-4,-7,-5,8,-3,-2,2,9,-3,-10,9,1,2,-4,1,-1,2,-8,2,2,-8,-10,-6,-4,5,9,-1,4,6,6,-7,-10,2,8,5,9,6,8,10,1,5,-1,-10,-4,4,-2,4,10,2,-9,-1,2,8,9,1,-3,-10,5,-1,6,8,4,4,9,5,-4,-6,4,-6,4,-5,-4,-3,-6,-7,-8,2,6,-10,-1,2,-1,-2,6,10,-3,-9,9,-7,8,9,8,10,7,-10,-6,6,3,-2,7,-1,6,-9,-5,10,-10,-9,-10,6,-10,-10,9,4,7,4,-8,4,6,9,-10,5,7,10,-5,-7,-3,1,-4,-7,-3,-2,-6,6,-4,3,3,-5,2,-10,-4,-1,-3,-2,-9,7,-9,-4,-9,-9,5,-6,2,1,-9,-10,-7,3,-7,-8,-3,10,-7,-9,5,9,9,-10,-9,6,1,4,-9,9,-9,2,-3,-3,9,7,9,-5,5,1,8,5,-3,9,-5,10,5,-7,-6,-9,4,10,3,-2,-5,-4,10,4,8,9,-2,-9,-3,-5,7,-6,1,-4,3,5,-1,-1,-8,-6,10,2,-4,-9,7,8,8,-7,-1,-3,7,2,-7,-8,-2,3,-2,4,-4,-5,-6,7,6,-3,2,-1,6,-8,-8,9,-5,-10,7,-2,-4,4,-9,-4,-2,2,-4,7,-4,-2,3,10,4,-4,-3,-4,3,-1,-8,7,-3,-7,10,7,-9,8,-10,2,10,7,-2,2,-8,10,-7,7,6,9,6,-1,4,-8,8,2,-6,1,9,-5,-8,4,-2,7,3,-5,1,7,-3,-2,7,-9,1,2,5,9,-2,9,4,-3,2,-9,4,-8,10,-10,-4,-1,10,6,-1,-7,8,9,5,-10,-2,2,2,4,10,1,4,-10,5,8,-1,-1,4,-10,3,-6,6,2,-7,-3,2,-2,8,-1,-8,-1,7,-7,-1,9,-6,9,-4,1,7,2,-8,6,-6,10,-7,2,-2,-4,-5,-7,10,2,-6,7,7,-5,-4,2,9,6,3,-9,-7,8,-5,-1,-10,9,8,-3,3,-1,-10,-7,-4,-4,-10,-2,5,-7,4,5,4,1,-8,-6,-2,-10,-9,1,9,-2,10,6,-3,-6,-2,10,5,-8,8,7,-1,4,1,5,3,-1,-3,-10,9,-3,9,8,7,-10,-10,-6,-2,-2,6,-5,7,3,2,-6,1,3,-3,5,-7,-6,10,7,-10,6,-8,-6,6,5,-7,8,-10,-10,-10,-6,2,3,4,5,-8,-2,2,1,1,4,9,-6,3,-4,10,1,2,3,1,-9,-9,-5,-1,8,4,-8,4,-4,9,-9,9,-3,3,6,4,-2,8,-3,-6,1,-3,-5,-4,-5,10,-3,5,2,2,1,-3,10,-2,10,-5,10,-1,-6,-7,-7,-4,-5,-6,6,-5,5,-10,9,9,-10,10,4,-4,-6,3,7,6,8,-1,10,-9,-3,-2,-1,-4,9,10,7,6,-4,-7,-6,-4,-4,7,8,1,-7,6,7,-8,3,-10,1,-4,-2,-7,-3,-1,4,3,7,5,-10,-3,-8,3,-8,-2,6,-5,8,-7,1,-9,9,8,7,-2,-2,-4,-6,4,8,5,5,-4,-2,-3,2,-7,-4,-9,-8,-8,5,-3,-6,7,4,-2,3,-9,9,-7,5,-4,-9,-10,5,7,1,-1,6,3,-1,8,-10,-9,10,2,10,-4,2,-5,-5,4,-2,-3,4,-8,-2,9,3,3,-3,-9,-4,1,-1,10,9,-10,-3,-1,10,4,-6,-3,2,-2,-2,6,-6,-1,-3,2,7,7,4,6,7,-5,-2,2,4,-9,-7,-2,1,-1,-4,-10,-5,-8,-5,3,4,-5,-6,-2,-10,-5,-5,-1,8,-5,-7,3,4,-10,-8,10,-3,-10,-1,7,3,-2,9,-7,7,1,-6,5,8,8,-2,-9,5,-4,-4,-10,5,7,5,-2,3,8,10,9,1,-5,6,-8,3,-7,-2,-6,-1,10,-5,10,-8,9,-2,-7,8,5,-5,-4,2,-7,-2,-1,4,-9,-4,8,9,-1,8,3,-9,1,-1,4,8,-10,-4,5,2,6,-5,7,4,5,5,9,8,10,4,-5,-5,5,5,7,6,-3,-10,4,-10,9,9,-1,-7,-8,-7,7,7,-9,-4,10,-10,10,3,5,7,9,1,4,-3,2,3,-1,-1,-3,-9,-4,5,-10,-2,-4,-10,-4,4,-10,8,8,1,-6,-2,-7,3,9,-9,-6,5,-9,-4,-5,-1,-7,6,4,5,-10,-8,-5,10,7,-4,-10,5,-1,2,-7,-10,2,10,-5,-6,9,4,3,9,-5,6,-1,5,-2,-9,-10,3,-6,9,-7,8,9,1,6,-3,-4,-6,-10,8,-8,2,5,1,8,5,-5,3,-5,-5,6,-1,6,5,8,9,10,5,7,-9,6,-10,6,-4,-10,1,-6,6,10,10,-5,-6,-8,-10,-5,-10,4,-1,-5,-3,-3,-1,-9,-10,8,-6,7,-8,3,2,9,-8,-1,-5,-1,3,5,2,1,-2,2,-10,10,-5,-7,10,8,9,6,-8,-6,-2,7,4,5,-4,4,7,-3,-8,9,6,-5,-9,-3,-9,-9,8,2,-1,8,6,-3,-7,-7,-7,-2,-4,-10,-7,1,1,-4,4,-3,-6,4,2,-5,4,-3,-8,5,-9,6,-9,-3,-7,-9,4,7,10,2,-9,-2,-10,-5,7,4,-7,5,7,4,4,6,5,10,5,9,2,8,-6,2,-2,-1,-9,7,-4,-2,6,10,1,7,3,-1,-9,9,-1,9,9,4,-8,-6,4,5,-5,-9,3,2,4,-3,4,6,-2,1,-9,-9,-8,1,2,9,-9,4,6,1,1,3,-3,1,6,-7,6,1,-1,-3,-10,-10,3,-2,4,-9,7,-10,-2,6,-4,-2,6,-4,10,10,2,-9,-6,5,6,4,-5,4,9,7,2,4,5,-5,-7,-4,-6,7,-6,1,6,7,-2,-1,10,4,7,10,-8,-8,-1,-8,-7,-9,7,9,5,-5,7,-10,1,-7,-4,10,-3,6,3,8,-9,7,7,9,9,1,-9,-3,4,1,-8,-9,1,2,1,6,-9,8,-8,-7,1,3,6,-2,-7,-8,6,-5,-5,1,-8,-6,9,-2,10,-3,7,3,-3,6,10,4,-3,2,-5,2,1,10,-1,-6,4,-4,-5,-4,5,-8,-6,-2,-9,-7,-9,-8,8,-8,-2,1,-4,-5,-5,-9,1,-7,10,-7,4,-5,-4,3,1,-10,8,9,6,10,4,-2,-9,-5,-8,9,-6,-9,7,2,-3,-3,4,2,-5,-1,-4,-8,-4,1,5,8,-4,4,6,1,6,2,-3,10,-9,-9,-8,7,9,-5,-7,8,9,3,7,9,-8,-5,-7,1,8,10,-8,-9,6,3,-9,5,2,5,3,-3,5,2,-3,-8,4,8,-7,-10,10,-6,-6,-7,10,8,-6,-4,10,-10,2,5,-8,-9,9,7,7,-8,-4,-1,-7,-8,9,3,-2,4,3,-10,-2,5,2,-1,-5,10,-4,-2,10,-5,5,-10,-10,-9,-4,3,9,7,10,-10,7,-4,1,-5,7,-9,7,-9,4,10,-8,3,-1,-1,-8,-5,1,9,5,-2,-3,7,2,7,-6,7,-7,5,3,-8,7,8,-5,9,-1,6,-5,4,-9,-5,-5,10,3,2,1,6,5,7,3,2,8,9,-1,1,1,6,10,-10,5,-10,-1,-6,4,-8,9,10,10,-1,2,2,1,1,-5,-6,-2,7,-5,-4,6,6,4,3,7,4,7,5,3,1,7,-10,-6,-6,2,9,-2,3,5,1,-9,3,10,-6,-4,-2,-4,3,1,-10,9,-1,8,-8,-10,-7,5,-9,-10,9,1,8,-6,-5,10,4,-7,-10,-10,10,-9,-1,8,1,-4,-1,-2,2,10,8,5,9,6,-8,2,-4,-4,-7,-4,10,9,-5,-2,8,6,-4,-8,4,-6,8,-2,-1,9,1,-8,-3,6,-5,-5,-2,1,-2,1,-2,-2,-7,5,5,7,1,-8,-10,2,-3,-2,-10,1,1,1,10,-4,-10,-2,6,10,5,-2,4,-2,-5,-2,-7,-8,-4,2,2,1,-8,6,4,-9,-8,4,9,7,-2,8,1,-10,4,-10,-9,-8,-4,10,2,5,-4,-10,-8,-4,7,10,7,4,3,8,3,-10,10,-4,-1,4,9,6,-2,-8,4,8,9,3,-6,-3,-6,-7,-2,1,-2,-9,-9,-10,7,2,7,3,2,9,6,6,-4,-10,-5,-2,-6,-8,7,-9,-6,-6,-1,-3,6,10,4,5,10,-8,8,10,10,10,7,-2], dtype = "uint8")#candidate|8221|(1728,)|const|uint8
call_8220 = relay.TupleGetItem(func_1907_call(relay.reshape(const_8214.astype('float32'), [1, 144]), relay.reshape(const_8221.astype('uint8'), [12, 144]), ), 5)
call_8222 = relay.TupleGetItem(func_1910_call(relay.reshape(const_8214.astype('float32'), [1, 144]), relay.reshape(const_8221.astype('uint8'), [12, 144]), ), 5)
output = relay.Tuple([uop_8206,call_8213,const_8214,call_8220,const_8221,])
output2 = relay.Tuple([uop_8206,call_8215,const_8214,call_8222,const_8221,])
func_8238 = relay.Function([var_8205,], output)
mod['func_8238'] = func_8238
mod = relay.transform.InferType()(mod)
var_8239 = relay.var("var_8239", dtype = "float64", shape = (8, 8, 5))#candidate|8239|(8, 8, 5)|var|float64
output = func_8238(var_8239)
func_8240 = relay.Function([var_8239], output)
mutated_mod['func_8240'] = func_8240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1694_call = mod.get_global_var('func_1694')
func_1695_call = mutated_mod.get_global_var('func_1695')
call_8247 = func_1694_call()
call_8248 = func_1694_call()
output = relay.Tuple([call_8247,])
output2 = relay.Tuple([call_8248,])
func_8264 = relay.Function([], output)
mod['func_8264'] = func_8264
mod = relay.transform.InferType()(mod)
mutated_mod['func_8264'] = func_8264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8264_call = mutated_mod.get_global_var('func_8264')
call_8265 = func_8264_call()
output = call_8265
func_8266 = relay.Function([], output)
mutated_mod['func_8266'] = func_8266
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8288 = relay.const([[[-7.978373,-4.226464,9.040158,3.545644,-4.908632,9.436036,9.423723,4.722181,-3.782175,4.418066],[6.265740,4.716258,-8.381812,-0.944026,9.482261,-7.588555,0.883240,9.054843,1.060149,4.923594],[-9.828828,-2.034919,-2.209667,-5.528775,8.173748,8.464139,-5.641699,-1.919760,6.260720,5.100268],[-9.453709,-4.619036,-3.490168,3.787859,-6.502457,7.979441,3.990628,5.369169,3.616790,-8.467747],[1.705614,7.303819,-9.046529,-6.503809,3.780597,-2.248111,7.297147,1.555580,9.563474,7.439485],[8.057388,-2.459637,-6.802392,7.832630,4.275001,7.398559,2.069649,-6.476285,-0.764661,4.425534],[-9.658752,6.952511,4.842082,8.122188,5.966798,-4.676783,-1.404617,9.519699,-8.573892,-7.060323],[-5.584436,-8.341426,9.128191,3.690521,-1.950619,6.615143,2.293257,-5.515795,9.402778,7.289357],[0.170042,-7.304819,-5.330059,-9.679443,-5.698178,-5.280617,-4.459988,-0.139223,-3.560838,0.205818]]], dtype = "float64")#candidate|8288|(1, 9, 10)|const|float64
uop_8289 = relay.atanh(const_8288.astype('float64')) # shape=(1, 9, 10)
bop_8291 = relay.logical_xor(uop_8289.astype('uint64'), relay.reshape(const_8288.astype('uint64'), relay.shape_of(uop_8289))) # shape=(1, 9, 10)
func_4383_call = mod.get_global_var('func_4383')
func_4385_call = mutated_mod.get_global_var('func_4385')
const_8300 = relay.const([3.428493,-9.918897,7.109295,-7.544183,-6.009627,5.170731,-2.655679,2.356329,-1.552271,-7.682368,1.413940,-4.240339], dtype = "float64")#candidate|8300|(12,)|const|float64
call_8299 = relay.TupleGetItem(func_4383_call(relay.reshape(const_8300.astype('float64'), [3, 2, 2])), 3)
call_8301 = relay.TupleGetItem(func_4385_call(relay.reshape(const_8300.astype('float64'), [3, 2, 2])), 3)
bop_8302 = relay.floor_divide(bop_8291.astype('float32'), relay.reshape(uop_8289.astype('float32'), relay.shape_of(bop_8291))) # shape=(1, 9, 10)
const_8309 = relay.const([-7.749704,-9.867645,8.592113,-3.351641,-0.203278,-3.547895,6.136854,1.775556,8.197311,6.238713,4.220584,-1.751075,2.076873,-9.424974,0.522609,-5.526222,8.388750,-4.426927,1.725667,-2.808038,3.134347,-6.080920,8.108976,4.742779,7.718298,-1.015945,-7.703127,-8.761521,6.009819,6.524277,8.205977,-9.353158,-8.786071,0.255449,6.799859,-5.104059,-0.306480,2.984628,-9.684555,-9.593241,-4.352618,-5.827495,3.308168,-0.114841,-9.842913,3.558074,2.070734,-8.525816,-2.537649,-7.892170,5.872849,-7.899706,4.479245,1.525295,-9.873773,9.372200,5.390530,-4.746433,4.773661,9.018530,-4.534292,4.426506,6.638946,3.700236,5.933792,6.061520], dtype = "float64")#candidate|8309|(66,)|const|float64
bop_8310 = relay.greater(call_8299.astype('bool'), relay.reshape(const_8309.astype('bool'), relay.shape_of(call_8299))) # shape=(66,)
bop_8313 = relay.greater(call_8301.astype('bool'), relay.reshape(const_8309.astype('bool'), relay.shape_of(call_8301))) # shape=(66,)
bop_8321 = relay.multiply(bop_8291.astype('uint32'), relay.reshape(const_8288.astype('uint32'), relay.shape_of(bop_8291))) # shape=(1, 9, 10)
func_2790_call = mod.get_global_var('func_2790')
func_2791_call = mutated_mod.get_global_var('func_2791')
call_8325 = relay.TupleGetItem(func_2790_call(), 0)
call_8326 = relay.TupleGetItem(func_2791_call(), 0)
bop_8328 = relay.logical_or(bop_8321.astype('bool'), relay.reshape(bop_8291.astype('bool'), relay.shape_of(bop_8321))) # shape=(1, 9, 10)
func_5677_call = mod.get_global_var('func_5677')
func_5680_call = mutated_mod.get_global_var('func_5680')
var_8339 = relay.var("var_8339", dtype = "float32", shape = (675,))#candidate|8339|(675,)|var|float32
call_8338 = func_5677_call(relay.reshape(var_8339.astype('float32'), [9, 5, 15]))
call_8340 = func_5677_call(relay.reshape(var_8339.astype('float32'), [9, 5, 15]))
bop_8355 = relay.right_shift(bop_8321.astype('uint16'), relay.reshape(uop_8289.astype('uint16'), relay.shape_of(bop_8321))) # shape=(1, 9, 10)
uop_8359 = relay.asinh(bop_8321.astype('float32')) # shape=(1, 9, 10)
output = relay.Tuple([const_8300,bop_8302,bop_8310,call_8325,bop_8328,call_8338,var_8339,bop_8355,uop_8359,])
output2 = relay.Tuple([const_8300,bop_8302,bop_8313,call_8326,bop_8328,call_8340,var_8339,bop_8355,uop_8359,])
F = relay.Function([var_8339,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8339,], output2)
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
