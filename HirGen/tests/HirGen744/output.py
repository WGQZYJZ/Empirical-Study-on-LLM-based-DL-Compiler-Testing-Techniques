import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_1297 = relay.var("var_1297", dtype = "float32", shape = (16, 4, 5))#candidate|1297|(16, 4, 5)|var|float32
uop_1298 = relay.acos(var_1297.astype('float32')) # shape=(16, 4, 5)
output = relay.Tuple([uop_1298,])
output2 = relay.Tuple([uop_1298,])
func_1319 = relay.Function([var_1297,], output)
mod['func_1319'] = func_1319
mod = relay.transform.InferType()(mod)
mutated_mod['func_1319'] = func_1319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1320 = relay.var("var_1320", dtype = "float32", shape = (16, 4, 5))#candidate|1320|(16, 4, 5)|var|float32
func_1319_call = mutated_mod.get_global_var('func_1319')
call_1321 = func_1319_call(var_1320)
output = call_1321
func_1322 = relay.Function([var_1320], output)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1419 = relay.var("var_1419", dtype = "float32", shape = (6, 5, 7))#candidate|1419|(6, 5, 7)|var|float32
uop_1420 = relay.sigmoid(var_1419.astype('float32')) # shape=(6, 5, 7)
output = relay.Tuple([uop_1420,])
output2 = relay.Tuple([uop_1420,])
func_1426 = relay.Function([var_1419,], output)
mod['func_1426'] = func_1426
mod = relay.transform.InferType()(mod)
mutated_mod['func_1426'] = func_1426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1427 = relay.var("var_1427", dtype = "float32", shape = (6, 5, 7))#candidate|1427|(6, 5, 7)|var|float32
func_1426_call = mutated_mod.get_global_var('func_1426')
call_1428 = func_1426_call(var_1427)
output = call_1428
func_1429 = relay.Function([var_1427], output)
mutated_mod['func_1429'] = func_1429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1449 = relay.var("var_1449", dtype = "uint64", shape = (5, 12, 11))#candidate|1449|(5, 12, 11)|var|uint64
var_1450 = relay.var("var_1450", dtype = "uint64", shape = (5, 12, 11))#candidate|1450|(5, 12, 11)|var|uint64
bop_1451 = relay.less(var_1449.astype('bool'), relay.reshape(var_1450.astype('bool'), relay.shape_of(var_1449))) # shape=(5, 12, 11)
bop_1479 = relay.divide(var_1450.astype('float32'), relay.reshape(var_1449.astype('float32'), relay.shape_of(var_1450))) # shape=(5, 12, 11)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_1483 = relay.var("var_1483", dtype = "float32", shape = (1, 320))#candidate|1483|(1, 320)|var|float32
call_1482 = relay.TupleGetItem(func_1319_call(relay.reshape(var_1483.astype('float32'), [16, 4, 5])), 0)
call_1484 = relay.TupleGetItem(func_1322_call(relay.reshape(var_1483.astype('float32'), [16, 4, 5])), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
call_1501 = relay.TupleGetItem(func_1319_call(relay.reshape(call_1482.astype('float32'), [16, 4, 5])), 0)
call_1502 = relay.TupleGetItem(func_1322_call(relay.reshape(call_1482.astype('float32'), [16, 4, 5])), 0)
bop_1507 = relay.add(call_1501.astype('uint16'), relay.reshape(call_1482.astype('uint16'), relay.shape_of(call_1501))) # shape=(16, 4, 5)
bop_1510 = relay.add(call_1502.astype('uint16'), relay.reshape(call_1484.astype('uint16'), relay.shape_of(call_1502))) # shape=(16, 4, 5)
uop_1522 = relay.exp(bop_1451.astype('float64')) # shape=(5, 12, 11)
output = relay.Tuple([bop_1479,var_1483,bop_1507,uop_1522,])
output2 = relay.Tuple([bop_1479,var_1483,bop_1510,uop_1522,])
func_1524 = relay.Function([var_1449,var_1450,var_1483,], output)
mod['func_1524'] = func_1524
mod = relay.transform.InferType()(mod)
var_1525 = relay.var("var_1525", dtype = "uint64", shape = (5, 12, 11))#candidate|1525|(5, 12, 11)|var|uint64
var_1526 = relay.var("var_1526", dtype = "uint64", shape = (5, 12, 11))#candidate|1526|(5, 12, 11)|var|uint64
var_1527 = relay.var("var_1527", dtype = "float32", shape = (1, 320))#candidate|1527|(1, 320)|var|float32
output = func_1524(var_1525,var_1526,var_1527,)
func_1528 = relay.Function([var_1525,var_1526,var_1527,], output)
mutated_mod['func_1528'] = func_1528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1697 = relay.var("var_1697", dtype = "float32", shape = (12, 1, 11))#candidate|1697|(12, 1, 11)|var|float32
uop_1698 = relay.asin(var_1697.astype('float32')) # shape=(12, 1, 11)
bop_1703 = relay.logical_xor(var_1697.astype('int64'), relay.reshape(uop_1698.astype('int64'), relay.shape_of(var_1697))) # shape=(12, 1, 11)
func_1524_call = mod.get_global_var('func_1524')
func_1528_call = mutated_mod.get_global_var('func_1528')
var_1709 = relay.var("var_1709", dtype = "uint64", shape = (660,))#candidate|1709|(660,)|var|uint64
const_1710 = relay.const([[4.063672,3.820193,-8.359143,-9.272788,-6.574705,-9.037213,2.771454,5.295041,-7.088589,5.529253,7.939983,6.557460,-3.594310,-2.893417,9.351018,7.749534,-7.446290,7.803463,-8.608895,4.990506,7.669835,2.208126,7.593354,-6.696477,2.313559,-6.500531,9.354106,6.022680,-8.118517,-6.173855,1.133080,7.277669,0.579028,-7.595142,-2.723932,-3.649045,9.954570,7.257946,-5.016101,-2.266966,0.691366,-0.655711,-3.135090,7.183714,4.553327,-1.929759,7.331678,-6.629575,8.811095,-3.757207,7.350075,1.688173,9.015720,9.418215,-1.535549,6.641122,-9.683529,6.408684,3.005805,5.430257,-5.097174,6.339497,4.578632,-9.952022,-1.638195,6.603006,-0.360846,5.268723,4.127621,6.791513,-1.092362,4.234430,4.506449,-7.907758,6.506215,5.001877,0.682710,8.812026,1.222278,9.797428,4.651904,1.570458,-9.751452,3.711753,7.769961,5.053519,5.815862,-5.641291,0.098419,-0.330227,-9.186561,9.485028,-0.916729,8.820441,-0.463494,-4.101082,8.936497,0.737557,-1.176198,4.217459,-8.176811,7.329055,8.529897,-2.932074,-9.473094,-3.684825,-8.652722,9.036029,-0.509013,-8.854087,5.282051,-4.907040,-9.550751,-3.250405,-5.243787,-8.329650,2.017376,1.201313,3.521847,3.173949,-1.639434,7.567696,4.579709,9.661942,3.335300,7.624133,-0.172605,4.190387,1.383094,1.805156,3.432312,-6.166461,-6.187124,1.344393,7.982369,8.402335,-9.687483,1.284072,1.965131,-1.827662,-5.980264,-6.085381,6.699312,-2.480641,1.379760,5.078640,5.173658,0.969738,4.838967,-8.633186,-0.181231,-8.771037,-4.102063,-1.465983,-0.275588,-8.511690,-9.155876,-0.071343,-8.930844,3.271736,-0.391837,-5.891978,-6.411769,6.030973,-8.208562,8.036874,-0.150793,-1.390402,2.419436,-0.045408,1.943696,-8.526194,8.975235,6.937819,8.434555,-4.477279,5.222068,-5.581701,-3.543673,6.014439,3.888113,5.929370,-8.149818,-0.340158,8.929422,-7.437008,9.790753,-4.383091,4.501017,-2.042322,-4.427082,-5.900059,7.274932,-6.917938,5.416287,-2.944681,-2.308405,-1.056296,7.824336,-2.318471,7.833892,4.554187,8.175531,-0.440699,-9.492939,-8.844630,9.117908,-7.096553,3.937122,-1.317426,8.261813,3.791686,4.802469,-8.018295,-4.725713,2.227252,7.625940,-4.080554,-1.084248,0.497861,4.222301,-4.073034,5.606237,9.578198,2.847940,1.554851,-2.462868,-8.190400,-6.443732,0.359331,0.823666,-0.090424,6.239710,4.875067,4.533139,-2.748403,-1.448468,8.688339,-8.923679,-0.743441,7.833065,-6.939408,-2.375404,9.951559,2.468260,4.819351,9.476701,-0.647344,-3.697810,-6.301778,-1.691275,-0.854588,9.707120,-2.804658,-9.412491,6.009682,-1.241886,-5.169110,-2.530097,2.675232,-0.206768,-0.301171,1.097207,-9.567937,0.777308,4.482427,-7.204705,-9.719897,-8.078535,4.252299,-3.030158,-7.737046,-8.141660,9.747815,-8.620602,-6.124514,-5.884906,-5.814670,9.787406,2.182590,9.543990,4.167361,6.056161,-4.695592,-4.937671,-0.749740,-7.332521,-7.952616,1.229613,-2.793200,-7.450494,-6.546585,3.696128,-7.281189,-4.077351,2.801225,7.446765,7.317705,5.036351,-3.803688,4.721547,-1.316684,6.903390,-1.568781,-5.081704,-5.728168,8.655067,7.681817,5.719174,-5.942761,-7.127251,7.757096,-6.870136,-3.265125,-8.430950,3.763035,5.906623,-4.209870,-0.068179,-6.607702]], dtype = "float32")#candidate|1710|(1, 320)|const|float32
call_1708 = relay.TupleGetItem(func_1524_call(relay.reshape(var_1709.astype('uint64'), [5, 12, 11]), relay.reshape(var_1709.astype('uint64'), [5, 12, 11]), relay.reshape(const_1710.astype('float32'), [1, 320]), ), 0)
call_1711 = relay.TupleGetItem(func_1528_call(relay.reshape(var_1709.astype('uint64'), [5, 12, 11]), relay.reshape(var_1709.astype('uint64'), [5, 12, 11]), relay.reshape(const_1710.astype('float32'), [1, 320]), ), 0)
output = relay.Tuple([bop_1703,call_1708,var_1709,const_1710,])
output2 = relay.Tuple([bop_1703,call_1711,var_1709,const_1710,])
func_1719 = relay.Function([var_1697,var_1709,], output)
mod['func_1719'] = func_1719
mod = relay.transform.InferType()(mod)
mutated_mod['func_1719'] = func_1719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1719_call = mutated_mod.get_global_var('func_1719')
var_1721 = relay.var("var_1721", dtype = "float32", shape = (12, 1, 11))#candidate|1721|(12, 1, 11)|var|float32
var_1722 = relay.var("var_1722", dtype = "uint64", shape = (660,))#candidate|1722|(660,)|var|uint64
call_1720 = func_1719_call(var_1721,var_1722,)
output = call_1720
func_1723 = relay.Function([var_1721,var_1722,], output)
mutated_mod['func_1723'] = func_1723
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1877 = relay.var("var_1877", dtype = "float32", shape = (10, 1, 4))#candidate|1877|(10, 1, 4)|var|float32
uop_1878 = relay.atanh(var_1877.astype('float32')) # shape=(10, 1, 4)
output = relay.Tuple([uop_1878,])
output2 = relay.Tuple([uop_1878,])
func_1886 = relay.Function([var_1877,], output)
mod['func_1886'] = func_1886
mod = relay.transform.InferType()(mod)
var_1887 = relay.var("var_1887", dtype = "float32", shape = (10, 1, 4))#candidate|1887|(10, 1, 4)|var|float32
output = func_1886(var_1887)
func_1888 = relay.Function([var_1887], output)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1911 = relay.var("var_1911", dtype = "float32", shape = (12, 15, 14))#candidate|1911|(12, 15, 14)|var|float32
uop_1912 = relay.log10(var_1911.astype('float32')) # shape=(12, 15, 14)
uop_1924 = relay.acos(uop_1912.astype('float64')) # shape=(12, 15, 14)
output = uop_1924
output2 = uop_1924
func_1926 = relay.Function([var_1911,], output)
mod['func_1926'] = func_1926
mod = relay.transform.InferType()(mod)
var_1927 = relay.var("var_1927", dtype = "float32", shape = (12, 15, 14))#candidate|1927|(12, 15, 14)|var|float32
output = func_1926(var_1927)
func_1928 = relay.Function([var_1927], output)
mutated_mod['func_1928'] = func_1928
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2470 = relay.var("var_2470", dtype = "bool", shape = (9, 13, 1))#candidate|2470|(9, 13, 1)|var|bool
var_2471 = relay.var("var_2471", dtype = "bool", shape = (9, 13, 6))#candidate|2471|(9, 13, 6)|var|bool
bop_2472 = relay.logical_or(var_2470.astype('bool'), var_2471.astype('bool')) # shape=(9, 13, 6)
bop_2485 = relay.left_shift(bop_2472.astype('uint64'), relay.reshape(var_2471.astype('uint64'), relay.shape_of(bop_2472))) # shape=(9, 13, 6)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_2490 = relay.var("var_2490", dtype = "float32", shape = (320,))#candidate|2490|(320,)|var|float32
call_2489 = relay.TupleGetItem(func_1319_call(relay.reshape(var_2490.astype('float32'), [16, 4, 5])), 0)
call_2491 = relay.TupleGetItem(func_1322_call(relay.reshape(var_2490.astype('float32'), [16, 4, 5])), 0)
bop_2507 = relay.logical_and(var_2490.astype('bool'), var_2470.astype('bool')) # shape=(9, 13, 320)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
var_2522 = relay.var("var_2522", dtype = "float32", shape = (132,))#candidate|2522|(132,)|var|float32
var_2523 = relay.var("var_2523", dtype = "uint64", shape = (330, 2))#candidate|2523|(330, 2)|var|uint64
call_2521 = relay.TupleGetItem(func_1719_call(relay.reshape(var_2522.astype('float32'), [12, 1, 11]), relay.reshape(var_2523.astype('uint64'), [660,]), ), 0)
call_2524 = relay.TupleGetItem(func_1723_call(relay.reshape(var_2522.astype('float32'), [12, 1, 11]), relay.reshape(var_2523.astype('uint64'), [660,]), ), 0)
output = relay.Tuple([bop_2485,call_2489,bop_2507,call_2521,var_2522,var_2523,])
output2 = relay.Tuple([bop_2485,call_2491,bop_2507,call_2524,var_2522,var_2523,])
func_2538 = relay.Function([var_2470,var_2471,var_2490,var_2522,var_2523,], output)
mod['func_2538'] = func_2538
mod = relay.transform.InferType()(mod)
var_2539 = relay.var("var_2539", dtype = "bool", shape = (9, 13, 1))#candidate|2539|(9, 13, 1)|var|bool
var_2540 = relay.var("var_2540", dtype = "bool", shape = (9, 13, 6))#candidate|2540|(9, 13, 6)|var|bool
var_2541 = relay.var("var_2541", dtype = "float32", shape = (320,))#candidate|2541|(320,)|var|float32
var_2542 = relay.var("var_2542", dtype = "float32", shape = (132,))#candidate|2542|(132,)|var|float32
var_2543 = relay.var("var_2543", dtype = "uint64", shape = (330, 2))#candidate|2543|(330, 2)|var|uint64
output = func_2538(var_2539,var_2540,var_2541,var_2542,var_2543,)
func_2544 = relay.Function([var_2539,var_2540,var_2541,var_2542,var_2543,], output)
mutated_mod['func_2544'] = func_2544
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2970 = relay.var("var_2970", dtype = "int16", shape = (15, 3, 7))#candidate|2970|(15, 3, 7)|var|int16
var_2971 = relay.var("var_2971", dtype = "int16", shape = (15, 3, 7))#candidate|2971|(15, 3, 7)|var|int16
bop_2972 = relay.less_equal(var_2970.astype('bool'), relay.reshape(var_2971.astype('bool'), relay.shape_of(var_2970))) # shape=(15, 3, 7)
func_1524_call = mod.get_global_var('func_1524')
func_1528_call = mutated_mod.get_global_var('func_1528')
var_2982 = relay.var("var_2982", dtype = "uint64", shape = (660,))#candidate|2982|(660,)|var|uint64
var_2983 = relay.var("var_2983", dtype = "float32", shape = (320,))#candidate|2983|(320,)|var|float32
call_2981 = relay.TupleGetItem(func_1524_call(relay.reshape(var_2982.astype('uint64'), [5, 12, 11]), relay.reshape(var_2982.astype('uint64'), [5, 12, 11]), relay.reshape(var_2983.astype('float32'), [1, 320]), ), 1)
call_2984 = relay.TupleGetItem(func_1528_call(relay.reshape(var_2982.astype('uint64'), [5, 12, 11]), relay.reshape(var_2982.astype('uint64'), [5, 12, 11]), relay.reshape(var_2983.astype('float32'), [1, 320]), ), 1)
uop_2985 = relay.log2(call_2981.astype('float32')) # shape=(1, 320)
uop_2987 = relay.log2(call_2984.astype('float32')) # shape=(1, 320)
output = relay.Tuple([bop_2972,var_2982,var_2983,uop_2985,])
output2 = relay.Tuple([bop_2972,var_2982,var_2983,uop_2987,])
func_2993 = relay.Function([var_2970,var_2971,var_2982,var_2983,], output)
mod['func_2993'] = func_2993
mod = relay.transform.InferType()(mod)
mutated_mod['func_2993'] = func_2993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mutated_mod.get_global_var('func_2993')
var_2995 = relay.var("var_2995", dtype = "int16", shape = (15, 3, 7))#candidate|2995|(15, 3, 7)|var|int16
var_2996 = relay.var("var_2996", dtype = "int16", shape = (15, 3, 7))#candidate|2996|(15, 3, 7)|var|int16
var_2997 = relay.var("var_2997", dtype = "uint64", shape = (660,))#candidate|2997|(660,)|var|uint64
var_2998 = relay.var("var_2998", dtype = "float32", shape = (320,))#candidate|2998|(320,)|var|float32
call_2994 = func_2993_call(var_2995,var_2996,var_2997,var_2998,)
output = call_2994
func_2999 = relay.Function([var_2995,var_2996,var_2997,var_2998,], output)
mutated_mod['func_2999'] = func_2999
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3004 = relay.const([[[-4,2,-10,-9,-8],[7,6,3,9,-1],[-9,8,6,10,-2],[1,-9,-10,-8,9],[8,3,4,-7,10]]], dtype = "uint8")#candidate|3004|(1, 5, 5)|const|uint8
var_3005 = relay.var("var_3005", dtype = "uint8", shape = (1, 5, 5))#candidate|3005|(1, 5, 5)|var|uint8
bop_3006 = relay.less(const_3004.astype('bool'), relay.reshape(var_3005.astype('bool'), relay.shape_of(const_3004))) # shape=(1, 5, 5)
bop_3020 = relay.greater(const_3004.astype('bool'), relay.reshape(var_3005.astype('bool'), relay.shape_of(const_3004))) # shape=(1, 5, 5)
output = relay.Tuple([bop_3006,bop_3020,])
output2 = relay.Tuple([bop_3006,bop_3020,])
func_3025 = relay.Function([var_3005,], output)
mod['func_3025'] = func_3025
mod = relay.transform.InferType()(mod)
var_3026 = relay.var("var_3026", dtype = "uint8", shape = (1, 5, 5))#candidate|3026|(1, 5, 5)|var|uint8
output = func_3025(var_3026)
func_3027 = relay.Function([var_3026], output)
mutated_mod['func_3027'] = func_3027
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3397 = relay.const([[[7.332678],[7.223608]],[[8.612422],[-6.841089]],[[-9.629197],[0.211660]],[[-5.259973],[9.034075]],[[-1.526881],[5.786199]],[[7.820129],[-6.038433]],[[-8.391725],[-4.853243]]], dtype = "float64")#candidate|3397|(7, 2, 1)|const|float64
uop_3398 = relay.log10(const_3397.astype('float64')) # shape=(7, 2, 1)
uop_3400 = relay.asin(const_3397.astype('float32')) # shape=(7, 2, 1)
var_3406 = relay.var("var_3406", dtype = "float64", shape = (7, 2, 1))#candidate|3406|(7, 2, 1)|var|float64
bop_3407 = relay.left_shift(const_3397.astype('uint8'), relay.reshape(var_3406.astype('uint8'), relay.shape_of(const_3397))) # shape=(7, 2, 1)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_3411 = relay.var("var_3411", dtype = "float32", shape = (320,))#candidate|3411|(320,)|var|float32
call_3410 = relay.TupleGetItem(func_1319_call(relay.reshape(var_3411.astype('float32'), [16, 4, 5])), 0)
call_3412 = relay.TupleGetItem(func_1322_call(relay.reshape(var_3411.astype('float32'), [16, 4, 5])), 0)
bop_3416 = relay.less_equal(uop_3400.astype('bool'), var_3411.astype('bool')) # shape=(7, 2, 320)
output = relay.Tuple([uop_3398,bop_3407,call_3410,bop_3416,])
output2 = relay.Tuple([uop_3398,bop_3407,call_3412,bop_3416,])
func_3419 = relay.Function([var_3406,var_3411,], output)
mod['func_3419'] = func_3419
mod = relay.transform.InferType()(mod)
mutated_mod['func_3419'] = func_3419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3419_call = mutated_mod.get_global_var('func_3419')
var_3421 = relay.var("var_3421", dtype = "float64", shape = (7, 2, 1))#candidate|3421|(7, 2, 1)|var|float64
var_3422 = relay.var("var_3422", dtype = "float32", shape = (320,))#candidate|3422|(320,)|var|float32
call_3420 = func_3419_call(var_3421,var_3422,)
output = call_3420
func_3423 = relay.Function([var_3421,var_3422,], output)
mutated_mod['func_3423'] = func_3423
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3438 = relay.var("var_3438", dtype = "float64", shape = (4, 16, 5))#candidate|3438|(4, 16, 5)|var|float64
uop_3439 = relay.log(var_3438.astype('float64')) # shape=(4, 16, 5)
uop_3445 = relay.log10(uop_3439.astype('float32')) # shape=(4, 16, 5)
output = uop_3445
output2 = uop_3445
func_3454 = relay.Function([var_3438,], output)
mod['func_3454'] = func_3454
mod = relay.transform.InferType()(mod)
mutated_mod['func_3454'] = func_3454
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3455 = relay.var("var_3455", dtype = "float64", shape = (4, 16, 5))#candidate|3455|(4, 16, 5)|var|float64
func_3454_call = mutated_mod.get_global_var('func_3454')
call_3456 = func_3454_call(var_3455)
output = call_3456
func_3457 = relay.Function([var_3455], output)
mutated_mod['func_3457'] = func_3457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3552 = relay.var("var_3552", dtype = "float64", shape = ())#candidate|3552|()|var|float64
const_3553 = relay.const([[-9.540097],[-4.727102],[-2.718827],[-9.347130],[-9.806255],[-7.335671],[3.957167],[-8.442797],[7.290978],[-3.895736],[6.893800]], dtype = "float64")#candidate|3553|(11, 1)|const|float64
bop_3554 = relay.floor_mod(var_3552.astype('float64'), const_3553.astype('float64')) # shape=(11, 1)
func_2993_call = mod.get_global_var('func_2993')
func_2999_call = mutated_mod.get_global_var('func_2999')
var_3574 = relay.var("var_3574", dtype = "int16", shape = (105, 3))#candidate|3574|(105, 3)|var|int16
var_3575 = relay.var("var_3575", dtype = "uint64", shape = (660,))#candidate|3575|(660,)|var|uint64
var_3576 = relay.var("var_3576", dtype = "float32", shape = (80, 4))#candidate|3576|(80, 4)|var|float32
call_3573 = relay.TupleGetItem(func_2993_call(relay.reshape(var_3574.astype('int16'), [15, 3, 7]), relay.reshape(var_3574.astype('int16'), [15, 3, 7]), relay.reshape(var_3575.astype('uint64'), [660,]), relay.reshape(var_3576.astype('float32'), [320,]), ), 3)
call_3577 = relay.TupleGetItem(func_2999_call(relay.reshape(var_3574.astype('int16'), [15, 3, 7]), relay.reshape(var_3574.astype('int16'), [15, 3, 7]), relay.reshape(var_3575.astype('uint64'), [660,]), relay.reshape(var_3576.astype('float32'), [320,]), ), 3)
bop_3588 = relay.logical_xor(bop_3554.astype('int16'), var_3575.astype('int16')) # shape=(11, 660)
output = relay.Tuple([call_3573,var_3574,var_3576,bop_3588,])
output2 = relay.Tuple([call_3577,var_3574,var_3576,bop_3588,])
func_3591 = relay.Function([var_3552,var_3574,var_3575,var_3576,], output)
mod['func_3591'] = func_3591
mod = relay.transform.InferType()(mod)
mutated_mod['func_3591'] = func_3591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3591_call = mutated_mod.get_global_var('func_3591')
var_3593 = relay.var("var_3593", dtype = "float64", shape = ())#candidate|3593|()|var|float64
var_3594 = relay.var("var_3594", dtype = "int16", shape = (105, 3))#candidate|3594|(105, 3)|var|int16
var_3595 = relay.var("var_3595", dtype = "uint64", shape = (660,))#candidate|3595|(660,)|var|uint64
var_3596 = relay.var("var_3596", dtype = "float32", shape = (80, 4))#candidate|3596|(80, 4)|var|float32
call_3592 = func_3591_call(var_3593,var_3594,var_3595,var_3596,)
output = call_3592
func_3597 = relay.Function([var_3593,var_3594,var_3595,var_3596,], output)
mutated_mod['func_3597'] = func_3597
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4836 = relay.var("var_4836", dtype = "float64", shape = (10, 10, 9))#candidate|4836|(10, 10, 9)|var|float64
var_4837 = relay.var("var_4837", dtype = "float64", shape = (10, 10, 9))#candidate|4837|(10, 10, 9)|var|float64
bop_4838 = relay.floor_mod(var_4836.astype('float64'), relay.reshape(var_4837.astype('float64'), relay.shape_of(var_4836))) # shape=(10, 10, 9)
output = bop_4838
output2 = bop_4838
func_4843 = relay.Function([var_4836,var_4837,], output)
mod['func_4843'] = func_4843
mod = relay.transform.InferType()(mod)
var_4844 = relay.var("var_4844", dtype = "float64", shape = (10, 10, 9))#candidate|4844|(10, 10, 9)|var|float64
var_4845 = relay.var("var_4845", dtype = "float64", shape = (10, 10, 9))#candidate|4845|(10, 10, 9)|var|float64
output = func_4843(var_4844,var_4845,)
func_4846 = relay.Function([var_4844,var_4845,], output)
mutated_mod['func_4846'] = func_4846
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5617 = relay.var("var_5617", dtype = "bool", shape = ())#candidate|5617|()|var|bool
const_5618 = relay.const([[[False],[True],[False],[False],[False],[False],[True],[False],[False]],[[True],[True],[False],[False],[True],[True],[True],[True],[True]],[[False],[False],[True],[True],[False],[True],[True],[True],[False]],[[False],[False],[False],[False],[False],[True],[False],[False],[False]],[[False],[True],[False],[True],[False],[True],[True],[True],[False]],[[False],[False],[False],[True],[True],[False],[True],[False],[False]],[[False],[False],[True],[False],[False],[True],[False],[False],[True]],[[False],[False],[True],[False],[False],[True],[False],[True],[True]],[[False],[False],[False],[False],[True],[True],[False],[False],[False]],[[False],[True],[False],[False],[True],[False],[False],[True],[False]],[[True],[False],[False],[True],[False],[False],[False],[False],[True]]], dtype = "bool")#candidate|5618|(11, 9, 1)|const|bool
bop_5619 = relay.logical_or(var_5617.astype('bool'), const_5618.astype('bool')) # shape=(11, 9, 1)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_5634 = relay.var("var_5634", dtype = "bool", shape = (13, 9))#candidate|5634|(13, 9)|var|bool
var_5635 = relay.var("var_5635", dtype = "bool", shape = (702,))#candidate|5635|(702,)|var|bool
const_5636 = relay.const([3.254811,9.573285,4.736589,7.912143,-5.344461,-2.342833,6.025637,1.711519,4.526957,-1.527366,-1.392340,-2.605026,5.152950,3.975979,-0.627490,-7.272245,6.778578,-6.728080,2.440988,0.801907,-9.830570,-0.303340,-2.749585,7.729124,1.333812,1.812564,-7.341801,-8.048701,9.445969,5.789133,-1.678669,0.797162,4.366818,4.961470,3.351403,-0.431443,-7.058720,6.239860,4.283954,-7.321887,8.178543,-4.170171,6.127750,9.461642,8.992822,-1.831779,-7.774565,8.387812,-0.262694,-4.278475,3.738301,7.295798,-2.929648,-3.860781,-1.873822,-0.612216,-9.018538,5.514327,-1.536566,5.059273,2.718315,3.219958,5.415565,-7.454456,7.781801,-6.968118,2.124947,-6.097474,-7.377740,0.083248,6.514889,-4.651309,2.932817,-9.159062,-2.408013,5.035958,8.854370,-3.238574,3.180869,-6.219662,1.789722,7.252723,7.477584,-1.239195,9.263249,-9.094912,-2.070963,-7.144729,-8.931829,3.777513,-4.833007,6.874082,0.101022,8.427798,-7.136163,-0.914959,-6.420735,-7.488634,6.620635,6.837719,6.298220,-0.389613,8.424237,2.939537,2.166609,-6.926564,5.336625,5.130185,4.326163,6.823509,2.370264,-8.845533,4.448208,0.689885,5.941552,8.741091,-7.171708,-5.109367,5.384635,9.022598,-3.103791,-9.783207,9.058096,7.366214,-3.756969,-0.306585,-3.560750,6.724454,-9.895378,-2.219105,-3.539967,-5.796376,0.647570,-8.557151,-2.540888,4.235609,2.450854,-1.591889,-5.433170,-3.484488,-3.418013,-5.780814,1.243608,-4.714935,-2.798684,0.507646,1.025394,5.208741,2.733492,8.997416,5.913855,-1.662050,-9.299804,-7.826561,-6.343136,-7.978086,3.928584,8.210812,-1.236859,-9.261782,6.735538,2.904742,9.546462,2.408654,-4.369845,-5.198868,-8.152973,4.497179,9.675354,2.696914,-3.612922,-5.356447,-6.719782,-5.067121,-5.928833,7.382482,-4.025515,-9.346602,9.549779,-9.580751,-9.508189,1.590228,-3.659212,9.847856,-3.948280,5.427673,-4.787418,3.725893,-1.206892,-2.373896,-6.639242,-5.747794,-2.087810,3.891733,-6.148621,-0.773648,-0.810689,3.969634,-4.076578,9.222675,6.689952,6.518312,-6.594419,-2.452080,-7.920874,1.572330,-1.508187,0.099390,-1.622096,-3.345922,9.098737,5.139100,4.078378,-3.074247,-0.805126,-0.411840,-9.247233,6.043168,-0.499783,5.794921,-3.482026,-9.376927,-0.039640,-6.982806,-6.750390,-3.561726,0.542178,1.086176,-9.687752,-4.791008,9.938597,5.761615,-8.142783,1.764518,-3.884076,6.886046,1.615699,-0.939918,2.964419,0.502833,1.317094,9.655966,3.758672,7.235716,-2.624794,-1.971366,4.701793,-8.149490,5.420717,-4.768008,-7.695764,-1.090014,2.864938,-9.626101,5.078481,-9.820254,6.639705,5.466064,5.685163,-4.473554,-3.309305,2.100062,-7.108031,2.972837,1.796620,-4.469373,6.626269,-3.790134,1.892639,-2.979383,-9.143429,4.427837,-5.529168,-7.830618,-5.715875,-2.185999,-5.602032,-4.797475,2.932537,-8.359873,2.278717,-6.560047,7.495632,-3.613180,2.986981,-1.729743,8.561465,7.105376,-9.953499,6.898786,2.892270,-1.502013,-6.057763,-3.103200,-5.018618,-7.327588,5.006529,0.506598,9.101259,8.271420,-6.381550,-9.129577,-5.207221,0.144847,-7.116740,5.404299,-9.908151,6.050902,-1.992053,-4.369477,-2.228664,-3.514648,-9.822797,-7.084048,3.548800,-6.619489,7.639845,-1.042378,8.089253,6.492947], dtype = "float32")#candidate|5636|(320,)|const|float32
var_5637 = relay.var("var_5637", dtype = "float32", shape = (132,))#candidate|5637|(132,)|var|float32
var_5638 = relay.var("var_5638", dtype = "uint64", shape = (660,))#candidate|5638|(660,)|var|uint64
call_5633 = relay.TupleGetItem(func_2538_call(relay.reshape(var_5634.astype('bool'), [9, 13, 1]), relay.reshape(var_5635.astype('bool'), [9, 13, 6]), relay.reshape(const_5636.astype('float32'), [320,]), relay.reshape(var_5637.astype('float32'), [132,]), relay.reshape(var_5638.astype('uint64'), [330, 2]), ), 3)
call_5639 = relay.TupleGetItem(func_2544_call(relay.reshape(var_5634.astype('bool'), [9, 13, 1]), relay.reshape(var_5635.astype('bool'), [9, 13, 6]), relay.reshape(const_5636.astype('float32'), [320,]), relay.reshape(var_5637.astype('float32'), [132,]), relay.reshape(var_5638.astype('uint64'), [330, 2]), ), 3)
output = relay.Tuple([bop_5619,call_5633,var_5634,var_5635,const_5636,var_5637,var_5638,])
output2 = relay.Tuple([bop_5619,call_5639,var_5634,var_5635,const_5636,var_5637,var_5638,])
func_5642 = relay.Function([var_5617,var_5634,var_5635,var_5637,var_5638,], output)
mod['func_5642'] = func_5642
mod = relay.transform.InferType()(mod)
var_5643 = relay.var("var_5643", dtype = "bool", shape = ())#candidate|5643|()|var|bool
var_5644 = relay.var("var_5644", dtype = "bool", shape = (13, 9))#candidate|5644|(13, 9)|var|bool
var_5645 = relay.var("var_5645", dtype = "bool", shape = (702,))#candidate|5645|(702,)|var|bool
var_5646 = relay.var("var_5646", dtype = "float32", shape = (132,))#candidate|5646|(132,)|var|float32
var_5647 = relay.var("var_5647", dtype = "uint64", shape = (660,))#candidate|5647|(660,)|var|uint64
output = func_5642(var_5643,var_5644,var_5645,var_5646,var_5647,)
func_5648 = relay.Function([var_5643,var_5644,var_5645,var_5646,var_5647,], output)
mutated_mod['func_5648'] = func_5648
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6111 = relay.var("var_6111", dtype = "float32", shape = (3, 10, 8))#candidate|6111|(3, 10, 8)|var|float32
uop_6112 = relay.cosh(var_6111.astype('float32')) # shape=(3, 10, 8)
func_4843_call = mod.get_global_var('func_4843')
func_4846_call = mutated_mod.get_global_var('func_4846')
var_6118 = relay.var("var_6118", dtype = "float64", shape = (18, 50))#candidate|6118|(18, 50)|var|float64
call_6117 = func_4843_call(relay.reshape(var_6118.astype('float64'), [10, 10, 9]), relay.reshape(var_6118.astype('float64'), [10, 10, 9]), )
call_6119 = func_4843_call(relay.reshape(var_6118.astype('float64'), [10, 10, 9]), relay.reshape(var_6118.astype('float64'), [10, 10, 9]), )
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_6122 = relay.var("var_6122", dtype = "float32", shape = (40, 8))#candidate|6122|(40, 8)|var|float32
call_6121 = relay.TupleGetItem(func_1319_call(relay.reshape(var_6122.astype('float32'), [16, 4, 5])), 0)
call_6123 = relay.TupleGetItem(func_1322_call(relay.reshape(var_6122.astype('float32'), [16, 4, 5])), 0)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
var_6132 = relay.var("var_6132", dtype = "float32", shape = (40,))#candidate|6132|(40,)|var|float32
call_6131 = relay.TupleGetItem(func_1886_call(relay.reshape(var_6132.astype('float32'), [10, 1, 4])), 0)
call_6133 = relay.TupleGetItem(func_1888_call(relay.reshape(var_6132.astype('float32'), [10, 1, 4])), 0)
output = relay.Tuple([uop_6112,call_6117,var_6118,call_6121,var_6122,call_6131,var_6132,])
output2 = relay.Tuple([uop_6112,call_6119,var_6118,call_6123,var_6122,call_6133,var_6132,])
func_6139 = relay.Function([var_6111,var_6118,var_6122,var_6132,], output)
mod['func_6139'] = func_6139
mod = relay.transform.InferType()(mod)
mutated_mod['func_6139'] = func_6139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6139_call = mutated_mod.get_global_var('func_6139')
var_6141 = relay.var("var_6141", dtype = "float32", shape = (3, 10, 8))#candidate|6141|(3, 10, 8)|var|float32
var_6142 = relay.var("var_6142", dtype = "float64", shape = (18, 50))#candidate|6142|(18, 50)|var|float64
var_6143 = relay.var("var_6143", dtype = "float32", shape = (40, 8))#candidate|6143|(40, 8)|var|float32
var_6144 = relay.var("var_6144", dtype = "float32", shape = (40,))#candidate|6144|(40,)|var|float32
call_6140 = func_6139_call(var_6141,var_6142,var_6143,var_6144,)
output = call_6140
func_6145 = relay.Function([var_6141,var_6142,var_6143,var_6144,], output)
mutated_mod['func_6145'] = func_6145
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6484 = relay.var("var_6484", dtype = "int8", shape = (15, 15, 5))#candidate|6484|(15, 15, 5)|var|int8
const_6485 = relay.const([[[5,6,-8,5,-4],[-10,-3,-6,-1,6],[-2,-3,-2,8,-3],[5,-2,3,1,-1],[-6,-10,7,4,10],[4,-4,10,-1,7],[-7,-3,7,-10,-6],[1,-9,3,-8,8],[8,3,6,-5,-2],[-1,7,9,-2,10],[7,1,6,-3,-2],[6,10,9,-3,-5],[9,3,3,-9,8],[-2,5,-10,-7,9],[4,9,-7,4,-5]],[[4,-8,-1,10,6],[1,4,3,-1,8],[10,-5,8,7,1],[-10,5,5,-8,6],[-4,2,-7,3,3],[-5,-3,-2,-2,10],[1,10,9,2,8],[-9,-8,-10,6,-10],[5,4,8,9,-6],[-3,1,5,-9,-7],[-6,9,7,-9,-7],[2,8,9,3,-8],[-7,6,-6,-9,-7],[-2,-1,10,-2,-1],[-2,10,10,-8,9]],[[1,-8,-5,-7,7],[-9,10,-2,9,9],[-3,-4,3,-4,6],[6,9,-6,6,9],[9,4,9,10,-10],[-10,2,-7,10,3],[-7,5,2,-10,-5],[4,6,-3,-6,5],[-4,10,-8,2,-10],[-4,-5,-3,-10,-5],[-4,9,9,-7,7],[-2,6,10,10,-2],[6,-9,6,-7,-7],[-1,3,2,-4,-6],[10,5,-9,10,4]],[[10,-9,-2,-1,9],[-1,-8,2,6,-1],[-10,-10,9,-9,-9],[-2,-6,7,3,-5],[5,-5,-10,-5,7],[-9,-6,-4,-10,-5],[-8,7,-5,-2,-4],[3,4,-4,-8,-1],[4,-4,10,-7,-2],[9,-9,-6,3,-5],[4,6,-7,-2,-9],[10,2,-6,-1,-3],[7,-5,-8,-1,6],[6,5,7,2,6],[2,-7,-1,9,7]],[[-7,3,1,2,10],[9,9,10,7,-5],[3,1,6,-2,6],[-8,-4,-4,2,-6],[-5,10,8,-9,-10],[-9,6,3,-2,6],[2,10,4,-10,1],[9,-10,7,1,-4],[2,5,3,-9,-1],[-4,10,-1,-9,9],[5,-5,10,-5,-10],[3,-10,2,-4,-10],[-10,2,-10,2,-1],[1,-2,-3,10,3],[-4,-4,5,-2,10]],[[6,8,-8,8,-8],[-3,-7,3,9,-7],[-5,-9,9,-8,-2],[3,-8,7,-7,-8],[-6,-4,-7,-2,-2],[1,1,-6,-3,-9],[3,-5,3,7,-7],[-7,-7,5,-7,2],[-5,7,-2,-4,7],[10,-7,9,8,-2],[-2,-7,9,6,-8],[-7,3,1,-7,10],[10,4,-6,-9,-10],[9,-9,4,10,-6],[-8,3,7,7,-1]],[[-9,-7,-10,5,-9],[-2,10,9,-1,-4],[7,-10,-3,6,-10],[-7,8,2,-10,9],[4,2,-3,8,7],[-1,-3,-5,-7,-10],[-8,5,-4,-5,-4],[6,6,-3,-8,-2],[-2,1,3,6,9],[-4,5,-4,-8,3],[-3,-1,-8,7,5],[3,2,5,-10,-3],[8,-5,-1,-10,-7],[-3,4,7,-8,8],[-6,1,2,5,-8]],[[10,-10,-9,-3,-9],[1,-1,6,7,-4],[7,3,-10,-5,-7],[-3,-1,2,-3,-8],[-7,4,6,-6,4],[-5,10,9,2,-4],[9,6,2,1,-6],[10,9,-1,-6,7],[7,-10,-9,8,5],[2,3,5,9,3],[-4,-9,10,8,-7],[7,7,4,8,-1],[5,-6,-1,-4,-6],[6,-3,-5,-6,-1],[9,8,5,4,-3]],[[-6,-8,9,-3,2],[1,3,2,8,-10],[3,-7,7,-3,5],[6,6,-4,-5,-7],[8,4,3,9,6],[-10,-1,9,9,9],[-8,7,-10,9,8],[2,-6,-9,-4,10],[-10,-8,7,10,-7],[-4,-5,1,2,9],[-5,-9,-9,8,7],[-3,10,9,-7,5],[-8,-3,8,8,-3],[1,10,-7,-8,-10],[6,-3,5,4,-3]],[[-7,8,5,3,7],[2,4,-7,1,-7],[-10,6,-9,-7,2],[2,2,1,-5,1],[-10,9,5,4,-1],[8,-6,-7,5,8],[4,9,1,3,4],[-7,5,8,-3,-5],[-5,-10,-7,-8,10],[2,-7,2,-10,-3],[7,1,-7,3,3],[-8,2,9,-4,-4],[2,-10,6,6,-7],[4,-8,-7,6,-7],[-7,-7,-1,-10,3]],[[1,1,-6,-3,5],[-1,3,6,6,-7],[10,8,-5,-4,-5],[-1,6,-8,-1,7],[1,6,9,4,-3],[10,9,9,-8,10],[-1,2,5,2,-2],[-3,-6,1,-1,1],[-7,5,1,-1,8],[6,4,-9,-9,6],[-9,-8,-10,-10,-5],[-4,4,-8,5,5],[1,-7,9,-6,6],[-4,3,-9,3,3],[-10,10,-8,8,8]],[[-1,5,3,-1,-6],[3,3,4,-8,-9],[6,-1,3,5,-5],[7,1,3,7,5],[2,-5,-5,-4,7],[5,5,10,-7,9],[9,7,7,-7,5],[-8,-1,1,4,-8],[-3,6,9,3,-2],[-8,-8,4,7,2],[3,-1,4,8,-9],[9,-1,7,-1,-6],[5,-6,2,-10,3],[-1,3,1,-3,-5],[7,-4,9,8,4]],[[-4,1,3,4,-2],[-9,-3,6,10,-7],[4,1,2,-1,-3],[-8,7,-1,-3,-6],[-1,-2,7,-8,-7],[-4,-9,-1,6,-5],[1,5,5,8,10],[4,9,6,4,-5],[-1,6,-3,-2,10],[-7,3,1,-10,5],[-3,1,-7,-9,3],[3,-10,-1,-7,3],[2,-10,-4,2,-10],[-5,-8,-6,-5,7],[9,-9,1,6,-7]],[[-5,9,-6,8,10],[-5,-2,3,-9,5],[6,5,4,9,4],[-9,5,-8,-2,8],[-6,-6,5,8,-10],[7,-8,-5,-10,2],[-10,-5,-8,5,1],[1,6,6,1,-5],[-9,-8,9,-7,10],[5,10,-5,2,10],[3,1,-1,3,2],[-2,2,-8,-5,-10],[-6,-3,4,9,-9],[-1,10,-4,-10,-2],[6,-7,-4,-9,-2]],[[4,-5,-8,-6,-9],[4,7,-4,5,-7],[8,1,-2,-2,5],[-4,-2,5,-10,-7],[-4,-8,4,-2,-6],[8,-4,1,5,9],[-7,-9,3,-9,5],[-1,8,1,-1,-3],[-4,3,3,4,-7],[-9,7,3,4,-3],[9,-9,3,-9,3],[-1,6,-6,8,-6],[-4,-9,-5,-1,8],[7,7,-6,-5,7],[8,6,-2,2,4]]], dtype = "int8")#candidate|6485|(15, 15, 5)|const|int8
bop_6486 = relay.maximum(var_6484.astype('int8'), relay.reshape(const_6485.astype('int8'), relay.shape_of(var_6484))) # shape=(15, 15, 5)
output = bop_6486
output2 = bop_6486
func_6489 = relay.Function([var_6484,], output)
mod['func_6489'] = func_6489
mod = relay.transform.InferType()(mod)
mutated_mod['func_6489'] = func_6489
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6490 = relay.var("var_6490", dtype = "int8", shape = (15, 15, 5))#candidate|6490|(15, 15, 5)|var|int8
func_6489_call = mutated_mod.get_global_var('func_6489')
call_6491 = func_6489_call(var_6490)
output = call_6491
func_6492 = relay.Function([var_6490], output)
mutated_mod['func_6492'] = func_6492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6912 = relay.var("var_6912", dtype = "float32", shape = (10, 8, 13))#candidate|6912|(10, 8, 13)|var|float32
uop_6913 = relay.cos(var_6912.astype('float32')) # shape=(10, 8, 13)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
var_6917 = relay.var("var_6917", dtype = "float32", shape = (132, 1))#candidate|6917|(132, 1)|var|float32
var_6918 = relay.var("var_6918", dtype = "uint64", shape = (660,))#candidate|6918|(660,)|var|uint64
call_6916 = relay.TupleGetItem(func_1719_call(relay.reshape(var_6917.astype('float32'), [12, 1, 11]), relay.reshape(var_6918.astype('uint64'), [660,]), ), 3)
call_6919 = relay.TupleGetItem(func_1723_call(relay.reshape(var_6917.astype('float32'), [12, 1, 11]), relay.reshape(var_6918.astype('uint64'), [660,]), ), 3)
var_6921 = relay.var("var_6921", dtype = "float32", shape = (5, 320))#candidate|6921|(5, 320)|var|float32
bop_6922 = relay.add(call_6916.astype('int32'), var_6921.astype('int32')) # shape=(5, 320)
bop_6925 = relay.add(call_6919.astype('int32'), var_6921.astype('int32')) # shape=(5, 320)
output = relay.Tuple([uop_6913,var_6917,var_6918,bop_6922,])
output2 = relay.Tuple([uop_6913,var_6917,var_6918,bop_6925,])
func_6932 = relay.Function([var_6912,var_6917,var_6918,var_6921,], output)
mod['func_6932'] = func_6932
mod = relay.transform.InferType()(mod)
var_6933 = relay.var("var_6933", dtype = "float32", shape = (10, 8, 13))#candidate|6933|(10, 8, 13)|var|float32
var_6934 = relay.var("var_6934", dtype = "float32", shape = (132, 1))#candidate|6934|(132, 1)|var|float32
var_6935 = relay.var("var_6935", dtype = "uint64", shape = (660,))#candidate|6935|(660,)|var|uint64
var_6936 = relay.var("var_6936", dtype = "float32", shape = (5, 320))#candidate|6936|(5, 320)|var|float32
output = func_6932(var_6933,var_6934,var_6935,var_6936,)
func_6937 = relay.Function([var_6933,var_6934,var_6935,var_6936,], output)
mutated_mod['func_6937'] = func_6937
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7685 = relay.var("var_7685", dtype = "uint16", shape = ())#candidate|7685|()|var|uint16
var_7686 = relay.var("var_7686", dtype = "uint16", shape = (5, 12, 10))#candidate|7686|(5, 12, 10)|var|uint16
bop_7687 = relay.left_shift(var_7685.astype('uint16'), var_7686.astype('uint16')) # shape=(5, 12, 10)
func_6139_call = mod.get_global_var('func_6139')
func_6145_call = mutated_mod.get_global_var('func_6145')
var_7699 = relay.var("var_7699", dtype = "float32", shape = (240,))#candidate|7699|(240,)|var|float32
const_7700 = relay.const([-7.050333,5.860313,-8.292618,2.560654,-7.406691,8.344038,-7.089533,-3.855919,3.097836,6.372809,-2.939391,-2.170252,2.483143,4.201497,7.051473,5.935556,6.656415,6.139424,9.613930,-7.971383,-4.426473,7.377276,-4.988824,2.591780,-6.565789,0.944277,-0.921240,6.899929,2.095551,-0.966606,3.461090,-0.154730,-0.923832,4.127175,-3.142768,-3.998124,6.895033,-2.199995,7.512115,8.543021,-3.024498,-6.061911,-1.680783,-6.964792,-7.191244,2.416579,8.147108,-5.274787,1.909070,0.906800,9.248851,6.843916,6.567573,-3.669686,1.780212,-6.597264,9.825295,-5.522651,-1.145202,8.080442,5.233410,-3.348147,-4.631070,1.008098,-0.144556,4.761773,-8.314200,2.130444,-3.136701,-1.180252,7.088403,-5.266886,-5.621464,7.847008,0.282363,6.213736,2.680059,8.861602,0.182314,0.691395,7.689880,9.998739,7.398763,9.896991,7.464803,-1.955848,-2.887617,5.655958,3.470748,9.067454,7.197300,-3.424529,8.625750,-6.373536,-9.279634,-4.693319,-6.656794,0.446944,-7.281252,-8.857932,-9.910901,1.710882,3.804860,3.833236,0.061815,7.749703,-4.079069,7.188417,-8.052448,-6.511293,2.154656,-2.223812,-7.116966,-4.866104,9.901894,-6.471841,6.352225,-0.519016,-9.626849,1.115247,1.626494,-7.035132,-4.779583,7.723399,9.392603,0.509791,-3.955685,9.567113,9.200745,-8.185540,-5.836264,0.558840,-7.967339,-3.865769,9.660581,-9.634043,-4.268275,-1.779733,-2.084107,4.037023,7.762039,-8.172786,9.769783,4.683887,1.110723,2.667793,-4.247820,2.145264,-7.539607,-9.297734,-2.920809,-3.413947,2.928542,6.462783,-2.949650,-9.941556,-3.961673,-5.851884,-3.430686,-5.885599,2.082715,8.471840,-8.035829,-7.923908,-3.989313,1.179165,8.678235,7.764141,-6.971710,-1.584782,-0.949371,1.531139,0.742622,-8.307968,8.608897,-8.940404,-9.316140,-0.628179,-8.133100,1.797923,0.248130,5.375212,3.135268,-3.373593,-5.932988,-8.257025,1.368376,5.435461,2.624556,-6.290167,-1.189269,5.657113,-3.658628,-5.075090,-6.609147,6.569825,-2.407515,-2.435355,1.428651,3.338914,4.197503,-8.046991,2.587594,-0.081076,3.077545,0.701455,5.388238,-1.759677,1.182317,-4.184189,4.470793,8.981550,5.764329,9.017756,-7.790176,-9.640773,-5.041973,-6.192365,-6.304215,6.151018,2.620562,8.615014,5.250314,-6.268846,-4.546369,4.499738,-3.393641,1.749393,-8.416332,5.243582,-1.748108,7.295043,-0.645686,-3.515125,-3.687764,9.357812,8.232320,-6.987896,-0.090389,6.720981,4.155305,-0.128649,6.674342,9.334487,-8.790645,4.176955,-8.625345,-9.855753,-1.692050,5.113043,-1.306475,5.923132,-9.461017,-7.809619,-8.201995,4.362231,-4.784822,-5.419539,-2.002838,-4.205660,-9.084104,1.756009,-6.195113,3.639137,-8.850699,6.617172,2.278797,-9.534095,-3.624979,1.058463,-6.274625,-3.759040,-2.232634,5.620145,1.188227,-3.244535,3.286754,-3.511006,1.696544,-7.453811,8.615860,-8.550763,-4.512077,-1.505655,2.280191,-5.488109,-3.185586,3.211742,7.361076,0.503566,-5.164329,-3.737372,2.740497,1.241329,-2.126622,9.510197,2.644774,4.184860,-7.016505,-5.303623,6.013560,-4.573762,2.051854,-6.730510,-9.952583,0.522737,8.723703,-5.872568,1.988134,3.374457,5.271947,5.660813,-4.921146,0.242640,-0.026500,3.293620,-1.129777,3.949291,0.537232,-8.405008,-6.795132,-4.157464,1.946623,-1.628771,-6.944618,-0.260321,-1.851696,-8.223332,-5.244739,-2.370369,2.786006,-4.969125,2.199208,5.790657,-6.498164,-9.596179,-0.785243,-0.879738,7.155685,-3.796739,3.290461,1.640372,-6.923493,-8.557964,1.619581,7.562512,-1.446697,-1.543306,6.965367,-0.862076,9.343756,-6.933841,0.761968,7.937643,-1.872184,-0.840652,6.644887,5.685939,5.545834,-2.293275,-9.466392,3.552126,-0.089700,-1.660126,-6.369649,0.302096,4.205700,7.948757,-4.873904,7.177982,-6.401072,-5.208841,-9.084920,7.683543,-6.923593,-7.197034,6.796406,3.489592,-1.771358,1.278804,0.781206,-9.598134,8.716610,7.144637,0.670575,-2.651422,7.009752,5.968825,-4.269953,9.046719,-4.728883,-6.840877,-6.107786,8.744088,1.356701,5.714338,9.810362,-5.226722,1.691715,2.142561,-0.496624,-3.490820,-4.973524,2.674048,-2.791367,0.931023,1.013205,-4.003173,-0.519128,-5.171298,-9.021833,-2.522512,6.672628,-3.009287,-4.809484,4.057066,6.024119,-5.263732,0.180222,8.520143,2.315995,5.239226,-6.910640,-2.320715,4.879583,-6.619651,-1.286763,-0.674356,4.847814,-9.125769,-0.649649,9.323134,2.431309,1.568946,9.960543,-0.990063,-1.383649,1.835276,2.114499,3.136223,-5.818729,-0.915920,-6.904722,3.994144,-3.889198,1.701674,3.438779,-0.547076,9.975130,-2.013703,-9.858594,4.748234,-0.132960,9.020425,-6.886673,-0.194787,1.791949,3.864158,0.860298,5.289545,-1.351017,-5.365286,2.827959,-9.074211,5.042459,-1.609986,3.062118,-2.721508,-7.914123,4.233773,-0.537991,-4.677407,-6.339835,2.921384,-7.348151,8.655518,8.867247,-1.081660,6.607202,4.294414,2.796201,-2.574516,8.773189,-8.745195,7.612705,-3.635090,-9.955045,1.089186,-0.768144,-7.763999,0.768184,7.326617,-5.963675,-0.024327,-2.795555,-4.769850,8.208653,-0.353286,4.940327,-5.167439,-5.894923,-7.714273,5.902104,-3.508410,-7.621795,-6.025174,-1.663278,-4.705793,-2.034706,-7.651651,2.847108,-6.568467,-9.459454,6.080087,-0.148975,-7.298973,7.653825,2.028440,-7.913606,-2.153812,-6.775762,-3.889641,8.782975,5.096353,0.348676,-5.511080,-0.241985,6.257871,-5.653825,-8.047506,1.913954,8.404616,6.829211,2.431641,-3.522259,-4.429466,1.609649,-0.378164,-5.837698,-5.063404,9.545316,-1.521217,1.230477,-8.710158,-9.115865,-8.335756,1.098481,-1.118581,-5.770484,-5.120429,-7.981818,-2.888344,-5.147585,-0.755916,-8.323868,-7.822482,3.864839,-7.783593,5.006162,-6.351691,5.749716,0.461896,4.816722,-8.749187,8.002666,-0.410648,1.571770,6.053780,4.808305,-3.546831,-4.535319,-4.754746,6.645492,6.300524,3.941283,7.281837,-8.211108,-7.825173,-1.870357,-3.356901,7.790456,9.467341,6.766045,-3.456361,-4.857936,-8.718623,-4.830158,1.680757,4.520745,-0.680335,-5.685914,-8.063332,-7.171501,-1.183014,6.681539,-4.894328,-4.038574,6.112156,0.599757,-8.935344,3.456911,-0.139108,7.535235,7.595205,-2.693538,-0.513196,0.579842,-7.450893,4.340626,0.845432,7.846621,9.646685,2.189570,2.162410,8.479451,8.478390,-1.945384,-5.217632,7.285452,9.917589,8.191338,-8.084448,-5.965095,-3.139642,-8.280555,-2.186160,6.180531,5.446504,-1.887169,1.129382,-5.609201,-8.778094,0.424547,7.677345,5.579008,-6.603518,-6.115441,0.797140,5.064755,-6.960409,7.290302,6.342203,-4.865195,-6.120429,4.267520,-9.198547,-8.326657,4.801893,5.236195,-7.763627,5.113768,3.864475,2.482124,-4.258354,-4.332357,-2.279092,9.759733,7.278980,-1.368938,-2.972288,5.485216,-2.698363,-5.188651,8.677522,-1.662673,-7.624976,5.053675,3.688167,-6.428200,0.337239,-9.386566,9.765451,-1.017150,3.769951,-8.881523,-0.705118,6.710524,5.073037,-4.573544,2.087434,-0.322205,-3.459307,-9.711907,-1.891405,5.048975,6.064702,-0.357866,0.789302,0.961023,8.535912,2.916059,-3.971808,-0.857981,-6.747743,-8.779569,5.118453,1.970907,-3.781310,7.297642,-4.059138,9.421720,-9.827546,-2.060223,-7.506520,3.974849,4.867485,1.647235,6.468145,8.231610,3.646329,4.015435,-9.098576,-4.475672,-9.142512,-2.468335,1.926376,7.287157,9.974072,6.416722,4.589677,1.814833,7.707438,-3.101790,4.869364,-6.471350,-7.600682,4.783609,-7.162350,3.455324,-0.660265,-5.507287,9.951782,6.813748,4.184154,-2.327045,8.922115,-4.638175,8.199477,7.272031,-7.115761,3.583087,-6.091279,-9.846374,-1.587449,0.448072,7.620132,-0.893693,2.475214,0.109676,2.158759,-3.096196,1.937059,7.233897,3.790696,9.692628,4.108605,-9.106032,-6.767107,-5.414202,7.196981,9.556615,3.125881,8.171246,8.753982,-4.595629,0.253362,-2.355794,1.940628,6.384815,-9.495635,-3.576751,7.113181,3.986590,2.085591,-6.581626,-1.729976,7.431271,-6.374460,-9.504869,9.411642,-4.036041,4.689830,-1.759290,-8.286591,-4.325540,-7.486574,-8.931406,2.094860,3.181878,-5.589847,2.705368,4.057267,-1.887830,-7.796583,-4.810800,0.974800,-2.007280,2.803198,0.442662,-6.455549,-6.952541,1.118730,-6.004029,0.746703,4.349024,4.962807,-6.247819,-7.862328,-8.917931,7.064901,-8.196558,3.351079,-5.062845,0.999687,2.077638,4.554743,7.849968,-6.961286,7.569848,8.732787,7.341335,-5.477512,-9.379790,8.552562,8.027847,7.544689,9.364985,-6.451480,5.226414,-3.054217,0.397606,-3.334451,-6.866440,-2.307790,-2.331197,-8.201562,-9.336482,3.768496,7.788874,-4.558921,-0.019874,3.327659,-2.170321,4.918207,1.744172,-2.506884,2.568860,2.570945,-4.876439,2.294115,-9.504587,-5.542925,-9.926493,3.289552,-5.881329,-4.948104,5.226322,2.807432,0.159602,7.921493,-8.299023,3.589955,-7.352759,5.614052,-0.825900,-9.002477,-0.685685,-8.676717,-7.181195,4.205718,3.656102,6.171692,4.018740,-4.767998,7.293920,7.982485,-3.130740,7.587889,-8.445497,4.574643,-4.943874,7.678420,-5.624967,3.060288,1.394200,-9.288636,3.631775,6.928033,-8.410435,4.068729,9.373649,4.342337,-5.870235,-2.339312,7.056750,1.214388,4.557845,-7.539495,-2.584412,7.426714], dtype = "float64")#candidate|7700|(900,)|const|float64
var_7701 = relay.var("var_7701", dtype = "float32", shape = (1, 320))#candidate|7701|(1, 320)|var|float32
var_7702 = relay.var("var_7702", dtype = "float32", shape = (40, 1))#candidate|7702|(40, 1)|var|float32
call_7698 = relay.TupleGetItem(func_6139_call(relay.reshape(var_7699.astype('float32'), [3, 10, 8]), relay.reshape(const_7700.astype('float64'), [18, 50]), relay.reshape(var_7701.astype('float32'), [40, 8]), relay.reshape(var_7702.astype('float32'), [40,]), ), 2)
call_7703 = relay.TupleGetItem(func_6145_call(relay.reshape(var_7699.astype('float32'), [3, 10, 8]), relay.reshape(const_7700.astype('float64'), [18, 50]), relay.reshape(var_7701.astype('float32'), [40, 8]), relay.reshape(var_7702.astype('float32'), [40,]), ), 2)
bop_7705 = relay.logical_xor(var_7701.astype('uint64'), var_7702.astype('uint64')) # shape=(40, 320)
func_3419_call = mod.get_global_var('func_3419')
func_3423_call = mutated_mod.get_global_var('func_3423')
const_7712 = relay.const([-1.019438,5.142415,2.994967,0.994628,-0.707391,-9.205343,-3.978539,9.715482,3.427306,3.832725,5.410332,-2.378433,8.591069,8.496907], dtype = "float64")#candidate|7712|(14,)|const|float64
call_7711 = relay.TupleGetItem(func_3419_call(relay.reshape(const_7712.astype('float64'), [7, 2, 1]), relay.reshape(var_7701.astype('float32'), [320,]), ), 3)
call_7713 = relay.TupleGetItem(func_3423_call(relay.reshape(const_7712.astype('float64'), [7, 2, 1]), relay.reshape(var_7701.astype('float32'), [320,]), ), 3)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_7719 = relay.var("var_7719", dtype = "bool", shape = (117,))#candidate|7719|(117,)|var|bool
const_7720 = relay.const([True,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,True], dtype = "bool")#candidate|7720|(702,)|const|bool
var_7721 = relay.var("var_7721", dtype = "float32", shape = (132,))#candidate|7721|(132,)|var|float32
var_7722 = relay.var("var_7722", dtype = "uint64", shape = (1, 660))#candidate|7722|(1, 660)|var|uint64
call_7718 = relay.TupleGetItem(func_2538_call(relay.reshape(var_7719.astype('bool'), [9, 13, 1]), relay.reshape(const_7720.astype('bool'), [9, 13, 6]), relay.reshape(var_7701.astype('float32'), [320,]), relay.reshape(var_7721.astype('float32'), [132,]), relay.reshape(var_7722.astype('uint64'), [330, 2]), ), 0)
call_7723 = relay.TupleGetItem(func_2544_call(relay.reshape(var_7719.astype('bool'), [9, 13, 1]), relay.reshape(const_7720.astype('bool'), [9, 13, 6]), relay.reshape(var_7701.astype('float32'), [320,]), relay.reshape(var_7721.astype('float32'), [132,]), relay.reshape(var_7722.astype('uint64'), [330, 2]), ), 0)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
call_7740 = relay.TupleGetItem(func_1886_call(relay.reshape(var_7702.astype('float32'), [10, 1, 4])), 0)
call_7741 = relay.TupleGetItem(func_1888_call(relay.reshape(var_7702.astype('float32'), [10, 1, 4])), 0)
output = relay.Tuple([bop_7687,call_7698,var_7699,const_7700,bop_7705,call_7711,const_7712,call_7718,var_7719,const_7720,var_7721,var_7722,call_7740,])
output2 = relay.Tuple([bop_7687,call_7703,var_7699,const_7700,bop_7705,call_7713,const_7712,call_7723,var_7719,const_7720,var_7721,var_7722,call_7741,])
func_7743 = relay.Function([var_7685,var_7686,var_7699,var_7701,var_7702,var_7719,var_7721,var_7722,], output)
mod['func_7743'] = func_7743
mod = relay.transform.InferType()(mod)
var_7744 = relay.var("var_7744", dtype = "uint16", shape = ())#candidate|7744|()|var|uint16
var_7745 = relay.var("var_7745", dtype = "uint16", shape = (5, 12, 10))#candidate|7745|(5, 12, 10)|var|uint16
var_7746 = relay.var("var_7746", dtype = "float32", shape = (240,))#candidate|7746|(240,)|var|float32
var_7747 = relay.var("var_7747", dtype = "float32", shape = (1, 320))#candidate|7747|(1, 320)|var|float32
var_7748 = relay.var("var_7748", dtype = "float32", shape = (40, 1))#candidate|7748|(40, 1)|var|float32
var_7749 = relay.var("var_7749", dtype = "bool", shape = (117,))#candidate|7749|(117,)|var|bool
var_7750 = relay.var("var_7750", dtype = "float32", shape = (132,))#candidate|7750|(132,)|var|float32
var_7751 = relay.var("var_7751", dtype = "uint64", shape = (1, 660))#candidate|7751|(1, 660)|var|uint64
output = func_7743(var_7744,var_7745,var_7746,var_7747,var_7748,var_7749,var_7750,var_7751,)
func_7752 = relay.Function([var_7744,var_7745,var_7746,var_7747,var_7748,var_7749,var_7750,var_7751,], output)
mutated_mod['func_7752'] = func_7752
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8010 = relay.const([[[3.888430,-9.674158,-9.962064,-1.711287,3.318368,2.789388,1.404098,7.047027,3.010407,1.938275,1.975820],[4.209171,-8.220339,-9.305294,-8.118710,-1.941344,5.370508,-0.976550,-9.228425,4.941833,5.922292,7.749360],[-0.711390,5.122934,-7.723052,7.528367,-5.853210,6.452603,2.693426,-7.460580,4.186360,3.871967,1.208462],[1.969385,-5.835490,2.619561,8.364513,1.533153,0.435282,1.644764,0.404103,4.099291,6.995342,-4.690900],[-1.562084,-0.660797,-6.720831,4.759682,1.111666,1.231307,9.503690,-8.840005,3.623136,-4.137543,-9.913782],[-5.016253,-3.658768,3.712630,-3.512062,5.227644,-4.045346,6.525501,1.306230,-1.256671,2.047848,6.162845],[-9.688948,2.297693,5.540068,-5.657931,7.474400,5.431544,-9.372251,3.254846,9.172439,-9.481663,-5.075221],[-5.848397,-1.661744,-2.148993,-9.529277,-8.144229,2.567166,-2.868607,-4.916114,-9.396193,-4.423900,1.254735],[-2.726545,9.654700,6.152569,0.363685,2.988360,-5.999912,-8.677205,8.904815,-4.327708,6.396667,7.288018],[-4.498147,-7.349664,5.184935,-2.675954,-7.395810,1.289651,-8.589056,5.507887,-3.466666,3.587525,-2.747987],[-9.202910,-6.058755,1.505987,-5.770612,-3.247627,-3.999305,-0.332244,4.940359,4.519738,3.454497,0.099032],[6.267265,-0.362086,-4.253543,-1.400665,3.965132,-9.854594,9.991471,-1.530457,9.106994,-9.702163,2.624063],[5.186747,-1.750100,-8.585379,-0.854865,8.032813,-1.988023,8.140598,-2.209278,6.469455,-2.264971,7.460920],[-8.216439,-3.610063,-1.305097,7.344887,8.682083,-4.339562,6.883747,2.319624,3.883323,-8.635340,-0.617636],[-1.590380,3.914359,4.372662,7.639475,-1.027218,-1.297381,5.496709,1.560328,-2.044408,-2.182556,-5.643693]],[[-0.112797,8.624432,2.473575,8.717225,0.420856,-5.896674,-7.876781,9.619525,-4.158384,0.458780,-7.404203],[-9.749583,1.941437,-7.584616,0.524237,-3.927356,-2.651638,9.046634,6.438869,-2.756044,-9.891166,4.345431],[-3.003674,7.453635,-4.622340,5.159829,1.366859,8.672856,-2.924591,-7.778116,-8.355877,9.882628,-4.773463],[-4.067383,-0.408954,6.282712,7.807935,3.911876,3.926393,9.180922,5.378530,-5.925843,-9.657845,0.352088],[1.491816,-7.376640,-8.584370,-0.435164,5.839568,-4.453876,8.787505,-3.518207,8.530999,-1.560081,-5.648480],[-6.297308,-5.030316,7.549710,-3.350481,-7.110461,-3.093114,-2.495198,-8.764170,-1.803462,3.196234,7.826745],[-7.595695,-3.810447,5.560280,-1.240510,-6.821562,8.260707,0.932203,3.922897,-1.338134,1.289142,-0.810742],[1.733619,-3.264226,-9.380615,9.310881,6.193170,-8.414964,1.902857,-2.642981,2.538585,-9.159432,-2.831367],[5.447375,-5.470347,8.729039,8.916890,7.160490,-4.904122,-0.436660,3.369109,6.590122,6.973009,-3.119535],[5.362605,-5.863161,5.396854,-1.590467,-3.841480,3.242788,5.343818,-0.179620,8.813339,5.949583,6.385497],[-9.668700,0.114285,2.100481,4.273617,9.579283,0.345565,-5.465242,7.770055,-4.397956,-6.060250,-4.554069],[-3.498907,-9.979227,-1.599749,8.348293,7.496228,-9.249048,7.566361,5.040836,-2.549033,-0.430385,-9.776227],[-2.158582,9.744993,7.377742,4.352670,6.868131,-7.144879,6.450406,2.094168,1.957810,-5.131540,-8.023155],[1.297527,8.510651,-6.386960,5.047065,-6.302777,-1.954046,-3.971551,4.348038,1.247410,8.410906,0.621986],[-3.466209,-8.464539,1.898920,-4.260124,-4.082695,-0.505548,8.838294,8.538294,2.621981,-0.726651,6.339009]]], dtype = "float32")#candidate|8010|(2, 15, 11)|const|float32
uop_8011 = relay.sigmoid(const_8010.astype('float32')) # shape=(2, 15, 11)
output = relay.Tuple([uop_8011,])
output2 = relay.Tuple([uop_8011,])
func_8014 = relay.Function([], output)
mod['func_8014'] = func_8014
mod = relay.transform.InferType()(mod)
mutated_mod['func_8014'] = func_8014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mutated_mod.get_global_var('func_8014')
call_8015 = func_8014_call()
output = call_8015
func_8016 = relay.Function([], output)
mutated_mod['func_8016'] = func_8016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8022 = relay.TupleGetItem(func_8014_call(), 0)
call_8023 = relay.TupleGetItem(func_8016_call(), 0)
func_6489_call = mod.get_global_var('func_6489')
func_6492_call = mutated_mod.get_global_var('func_6492')
const_8025 = relay.const([10,-2,4,-7,3,-4,9,9,-5,-10,2,-8,-8,2,-3,7,-8,-6,-3,1,-10,-6,4,-9,-8,-7,2,7,-4,-7,-1,-2,3,9,10,-10,9,-1,5,2,-10,4,-6,2,-1,9,-5,-8,9,-2,1,1,-2,-5,-2,-8,5,6,4,-1,9,6,-3,2,-4,-10,6,7,4,5,-6,-10,-9,-4,6,-8,7,1,-8,1,7,9,3,-1,5,-4,-1,5,3,-2,7,8,-6,4,-3,-8,-6,-4,-2,-9,3,9,10,-5,-1,3,-9,-4,3,-10,2,-5,-6,1,-3,2,-2,1,5,6,-3,6,2,-8,7,-1,8,9,-4,2,9,-3,-7,4,8,-7,-8,4,2,-7,4,8,-4,7,-5,5,-5,6,3,-1,9,4,3,-9,4,4,6,1,8,7,-7,9,9,1,5,-2,3,4,-8,1,-1,-9,6,6,-5,7,-5,3,4,-5,9,-5,-7,-6,-4,-4,-1,-3,-10,3,3,-9,-8,2,8,3,7,8,9,-9,-3,1,6,5,4,-5,-7,5,7,-9,7,2,10,-9,8,-1,1,-6,-5,-6,8,7,-6,-3,2,-9,2,4,-3,-10,-1,1,2,-2,10,-7,1,-6,-8,1,-8,10,2,-1,-7,6,-1,-1,-4,-1,2,5,-6,10,9,-6,2,9,10,-8,1,6,-9,-7,1,-1,8,6,-8,-7,-8,4,-1,-3,-2,-7,-3,7,9,8,3,-4,-5,4,7,-10,8,-4,-8,-9,5,7,10,-1,9,-10,-1,3,3,1,1,-6,7,8,-6,-8,-5,-1,7,4,3,8,6,-10,-9,10,4,10,7,-7,-5,4,-7,2,6,2,10,5,-1,7,-8,3,5,1,9,5,-10,3,3,-1,-3,-10,5,9,10,8,-4,-8,-4,1,9,-9,-4,-6,10,-5,2,-6,-9,-5,-10,7,-3,3,5,3,1,-3,-6,9,8,-1,-9,9,3,-9,6,6,-2,-9,4,-1,3,7,4,-7,4,-5,4,-3,10,9,9,-7,6,-9,9,-5,-5,2,-10,2,-7,-7,4,8,-3,10,-4,-4,-5,1,5,6,8,-9,-9,2,-1,6,10,-7,-3,-6,8,-7,5,6,-4,1,-2,-2,-5,-6,-5,10,-8,-10,-8,10,-8,-8,7,-6,6,-6,-10,-9,5,9,-8,7,10,1,-8,1,-9,1,-2,-8,-4,7,3,9,3,-9,-9,-9,6,4,-10,-9,5,-5,-9,-5,9,9,2,-9,-5,6,-5,-2,6,6,-4,-6,-7,6,-6,-2,-5,-5,10,1,-4,-9,5,-1,-9,8,-2,-2,5,-6,1,6,-1,-4,-6,-6,4,-9,-1,2,5,-3,4,7,-5,2,5,1,-8,-6,-10,5,2,-4,4,2,6,8,3,1,10,-2,-1,10,-8,6,-3,-3,-6,-7,-3,-2,6,-10,7,7,-5,4,-1,-7,-3,10,-3,2,-2,-10,9,5,-1,-6,-8,-10,9,-1,8,-3,9,8,6,1,-10,4,-2,7,-6,4,6,-7,7,7,-3,8,-4,6,-10,-8,8,2,-1,-5,-3,-8,-4,4,-10,7,-3,-7,-5,7,-10,6,6,-9,-8,-3,5,8,6,-1,4,2,-4,6,-2,5,-9,1,8,2,6,6,9,-1,5,3,-1,-9,-4,6,-8,-7,3,-2,-7,8,-4,-5,8,7,-9,7,5,-6,-10,2,-7,-7,-6,3,5,-7,6,1,-9,1,9,9,-3,3,-1,-3,6,9,9,5,3,-3,5,7,2,-3,6,-7,9,2,6,8,-5,6,-9,10,-5,3,8,-4,-9,-1,1,2,9,1,1,-9,-6,-2,8,-7,6,-4,3,5,9,5,-6,-9,4,10,9,2,8,10,-6,10,-10,-6,-6,-3,7,-4,-8,7,1,7,-1,-5,5,-5,-2,-4,-1,3,1,2,-7,-10,9,7,9,2,-5,6,-10,-2,8,-7,4,8,-8,-3,7,2,-5,8,4,-3,-4,-10,2,1,6,8,-7,-5,-7,2,6,-1,-4,4,-8,-9,-7,-1,9,-10,-7,4,5,1,-10,9,8,8,9,-1,8,-1,7,6,1,10,4,-4,-3,-4,-1,-2,3,2,-9,-8,3,4,1,-5,-7,10,8,10,-2,-8,-7,3,-8,1,8,-8,1,2,-3,-2,-3,-2,10,-6,-6,7,-5,-3,-5,-4,-6,-5,-4,6,-5,10,5,-1,-3,9,-1,7,7,3,-4,7,9,4,-1,5,-1,6,-6,-10,1,-2,-4,-2,-7,-2,-10,-1,-5,4,-9,1,-3,-5,3,-10,5,-9,-9,1,-4,8,-4,-6,-8,-4,-9,-7,4,-1,-9,1,3,4,-1,-9,-8,2,8,2,8,2,-2,10,-3,1,4,-6,4,-8,-5,-1,-3,-6,10,-6,-5,-6,1,3,10,6,7,-8,3,7,2,10,10,-4,-5,9,-3,7,2,8,7,4,9,7,10,8,10,5,6,-10,-4,-1,3,-10,9,7,-3,9,6,4,8,8,-1,-9,4,8,-8,6,-6,-8,-6,10,-7,3,-5,-1,-8,2,-4,6,8,-10,2,10,2,-4,3,8,-3,5,-8,2,9,-7,4,-5,-9,1,-8,-1,6,-7,-9,1,5,-1,-4,9,8,-8,-1,-5,5,2,-8,4,-10,3,7,3,-1,5,7,1,-9,-8,-2,-1,-10,2,7,1,8,-7,1,-5,2,10,-3,7,-1,-2,-7,-10,7,-6,-8,2,-3,1,6,-6,7,10,-6,3,1,2,10,8,6,2,10,-9,10,7,-7,6,9,-3,-4,-4,-4,4,10,1,-5,9,-4,8,-10,10,10,-1,-4,5,1,-5,-8,8,3,2,-10,-3,1,8,8,9,6,4,4,-7,1,-1,3,4,1,-1,-9,5,8,1,5,-2,2,10,7,5,1,4,-7,9,-6,-9,7,-5,1], dtype = "int8")#candidate|8025|(1125,)|const|int8
call_8024 = func_6489_call(relay.reshape(const_8025.astype('int8'), [15, 15, 5]))
call_8026 = func_6489_call(relay.reshape(const_8025.astype('int8'), [15, 15, 5]))
uop_8029 = relay.rsqrt(const_8025.astype('float64')) # shape=(1125,)
func_2993_call = mod.get_global_var('func_2993')
func_2999_call = mutated_mod.get_global_var('func_2999')
var_8032 = relay.var("var_8032", dtype = "int16", shape = (315,))#candidate|8032|(315,)|var|int16
const_8033 = relay.const([6,-3,-4,-9,-1,2,10,-7,5,5,-8,2,7,4,9,-5,-9,6,-5,6,3,-5,-8,-3,10,8,4,9,7,7,-3,1,-1,5,-1,3,9,-6,-2,-1,-5,-10,10,10,5,5,10,-9,-2,-6,-5,6,6,-10,-1,1,-1,6,-2,-9,6,4,2,6,8,-7,-10,7,-7,4,-10,-5,-8,2,-7,-7,-7,-8,2,2,-5,-3,4,-1,-8,10,-2,1,-5,-9,4,-7,7,-9,-9,-1,10,9,5,-6,7,-3,8,-8,-6,7,-5,2,-10,-2,-2,5,-6,-7,-4,-6,-8,7,-4,10,4,-2,4,10,5,-4,5,-8,-4,2,9,-9,8,4,5,-1,-3,-7,-7,10,-8,-8,6,4,2,-9,3,-7,-6,-2,-4,9,6,-2,-2,4,1,-5,-7,-8,-2,-1,7,-7,-8,5,3,-7,9,-3,-4,-2,-8,-3,-3,-5,7,3,3,-8,-10,1,4,-2,9,-5,4,-9,4,9,-4,6,2,7,9,6,-6,-3,-7,5,-2,-9,8,9,2,1,4,-9,-5,2,2,5,5,10,5,-7,8,5,8,9,-4,7,-8,-4,5,-8,4,-6,-3,2,-4,7,9,-9,8,6,-8,1,9,8,-1,-10,-2,-7,-5,-3,10,-10,-3,-5,-6,-4,3,-8,-1,8,-5,-9,5,3,5,-8,7,-3,8,1,8,-8,-1,5,5,3,4,-8,-8,-10,7,7,7,-4,9,-8,-1,9,-3,1,8,7,-8,2,5,8,-9,8,6,-10,9,3,6,-1,6,6,-8,7,-9,-1,-10,-8,5,-2,8,-7,2,7,1,7,-2,3,-8,-7,9,3,6,-6,-7,-3,4,2,-1,4,-8,1,-7,-1,5,4,-5,-3,6,3,2,10,9,2,10,-4,-8,-8,1,10,5,-2,-10,-3,-8,2,4,6,4,3,-3,-2,-4,-7,-8,-3,-10,-5,-9,7,-5,-7,-10,10,10,-8,2,5,-8,3,9,1,8,-10,-4,-6,7,-6,6,-1,-1,1,-6,-1,9,2,-9,-9,-1,-6,7,4,5,3,7,-10,-10,4,-7,2,-1,8,-1,7,-8,-9,-4,1,4,-3,-7,-1,-5,-4,-2,-2,5,2,-7,-10,-1,1,1,-5,7,7,-2,-10,-5,-9,5,1,1,5,-2,2,3,9,7,-8,3,-6,-6,-1,-5,2,-4,-9,8,-5,-1,6,-2,8,8,-2,3,-7,6,-4,2,10,-10,-3,7,1,-4,-3,-9,-4,9,1,5,3,-7,2,-2,5,5,10,-5,1,-7,6,3,6,-5,6,-4,1,5,-9,10,-10,-2,-7,3,-6,10,6,-1,7,-7,8,-1,3,4,4,-7,-7,7,8,1,8,-6,-9,9,5,-9,9,3,6,3,-9,6,-1,-1,-1,-3,-8,-7,7,2,-2,-6,1,-3,5,10,-6,4,-7,6,-9,-1,7,-5,2,10,-10,-4,-6,-9,3,-6,6,-8,-5,3,3,-5,1,-7,-7,6,-3,-8,9,9,9,-3,-7,7,5,-8,-5,-1,2,9,6,7,-8,-8,4,-9,5,9,-2,4,8,6,-6,10,-6,7,4,9,1,-9,7,10,-1,-1,-7,2,8,9,-6,4,-7,2,-7,5,2,-4,3,8,3,7,-6,-5,9,-2,2,7,-7,3,3,1,-2,-2,-9,9,2,1,-6,-4,-10,-2,-10,-2,-9,2,-10,5,10,-7,8,10,-3], dtype = "uint64")#candidate|8033|(660,)|const|uint64
const_8034 = relay.const([3.592323,4.938688,-3.200818,5.803681,-2.225065,7.376491,-7.373379,6.414993,-0.246408,9.632791,0.734443,-1.136716,-7.402033,-1.392307,-1.022604,3.295513,-5.758718,2.377086,-7.242990,6.117766,5.528266,-9.999547,-4.718166,-0.321932,-5.543397,4.711271,-1.693934,-6.830900,-4.600679,-6.258218,0.356953,3.409765,-8.308235,-8.630936,4.283640,0.037840,-5.510539,-6.952424,-9.201743,8.512866,-7.634967,-0.610699,-5.030423,6.991425,4.562525,-8.413758,3.806301,-6.173005,-0.581643,-9.797705,-6.931267,-2.984246,4.434132,7.585963,1.613373,-6.899958,6.426485,-9.710000,5.233230,9.634409,3.509500,-6.186239,7.254869,2.308906,8.441282,8.225089,8.465230,4.259409,-4.242936,-0.724585,0.605930,7.429647,9.973258,2.720375,1.390119,-5.972499,-4.306726,7.180174,1.778085,0.122806,4.418862,5.904579,-4.764354,4.008208,5.715770,-4.777935,6.409938,-0.407966,8.603944,3.381458,-5.252406,8.653206,-4.148775,-2.910300,8.068906,0.352811,-0.985771,-5.479858,1.042084,5.588189,4.180441,9.852762,8.938995,-1.471131,0.624170,0.460102,3.622975,-4.917677,6.745176,7.445728,-6.958943,3.829732,0.052460,8.482931,-1.648728,-3.262526,-5.578130,-0.457545,2.654985,-4.609656,-3.105563,-0.979729,4.207381,-9.174661,5.920107,5.368907,-5.203732,-4.834103,-9.559563,-2.616386,-2.327390,7.506736,-5.628754,-7.988827,-3.098496,3.822839,-1.196607,-3.579924,-5.686607,-3.458575,-0.866664,-8.153059,7.125227,2.488700,-7.941180,-0.675647,-9.972044,-0.454031,9.433166,-4.930066,6.262575,-8.200154,1.109703,4.863121,1.198896,3.031009,-2.115859,-2.952986,-8.688115,7.454776,2.909581,9.928803,7.088285,5.696852,-9.967351,-7.190162,3.978501,5.450692,5.358622,-0.289782,-3.772979,1.587578,9.762271,-7.938381,8.370020,6.445161,8.928982,-3.248367,-2.983291,3.154923,1.029738,-5.860526,1.749679,5.956408,1.127975,9.090215,9.887497,-2.772692,1.521880,-7.210864,-5.088448,3.993080,-0.884769,5.463020,4.126270,7.860552,-0.149892,3.056381,8.653385,0.373560,9.545004,-0.921438,4.849416,4.958961,-1.280211,2.799329,4.788315,-5.310290,-4.853550,-5.984690,3.984269,-3.262457,-5.571443,1.061379,-4.014995,-2.664904,1.187028,-2.793973,7.435372,6.129635,4.932816,-7.165380,-1.601131,-8.662902,-4.341871,-5.023305,-3.188282,-2.061624,1.306820,-6.306990,-3.379336,1.876068,2.901718,-5.395743,9.232388,-5.224882,-9.359223,-0.310198,-3.608674,7.636741,9.284331,-1.571061,-6.199014,-9.687691,-4.866931,8.197520,3.030937,-6.433476,-7.384339,3.182892,4.743153,-7.252725,8.508464,-5.075678,8.286986,-2.946750,1.075460,-6.842144,3.397693,9.443370,5.452009,-8.111579,2.026792,7.894503,4.115326,-6.716973,1.604813,-3.407264,0.663342,-5.141216,-7.976977,1.840088,4.537752,2.535604,6.665762,-6.284740,7.847532,6.356987,2.286229,-4.632439,-5.665238,9.172662,5.807138,-1.859545,-3.726036,9.462033,4.279683,8.782476,-3.634700,-7.266182,1.961447,-8.905661,1.700408,-8.849165,0.734994,-2.337811,5.953223,2.349047,5.478662,0.589344,-8.626883,0.657185,2.255289,-3.173317,2.331739,1.089142,9.817146,-9.213645,-3.584878,4.497463,5.957818,6.867817,-3.167816,-2.461518,-9.634496,5.315973,-6.332203,-8.529617,2.528945,-1.029039], dtype = "float32")#candidate|8034|(320,)|const|float32
call_8031 = relay.TupleGetItem(func_2993_call(relay.reshape(var_8032.astype('int16'), [15, 3, 7]), relay.reshape(var_8032.astype('int16'), [15, 3, 7]), relay.reshape(const_8033.astype('uint64'), [660,]), relay.reshape(const_8034.astype('float32'), [320,]), ), 0)
call_8035 = relay.TupleGetItem(func_2999_call(relay.reshape(var_8032.astype('int16'), [15, 3, 7]), relay.reshape(var_8032.astype('int16'), [15, 3, 7]), relay.reshape(const_8033.astype('uint64'), [660,]), relay.reshape(const_8034.astype('float32'), [320,]), ), 0)
output = relay.Tuple([call_8022,call_8024,uop_8029,call_8031,var_8032,const_8033,const_8034,])
output2 = relay.Tuple([call_8023,call_8026,uop_8029,call_8035,var_8032,const_8033,const_8034,])
func_8036 = relay.Function([var_8032,], output)
mod['func_8036'] = func_8036
mod = relay.transform.InferType()(mod)
var_8037 = relay.var("var_8037", dtype = "int16", shape = (315,))#candidate|8037|(315,)|var|int16
output = func_8036(var_8037)
func_8038 = relay.Function([var_8037], output)
mutated_mod['func_8038'] = func_8038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8056 = relay.TupleGetItem(func_8014_call(), 0)
call_8057 = relay.TupleGetItem(func_8016_call(), 0)
func_8036_call = mod.get_global_var('func_8036')
func_8038_call = mutated_mod.get_global_var('func_8038')
const_8081 = relay.const([3,6,1,4,-7,-3,-10,10,-10,-1,-2,-3,-8,1,1,5,8,-1,-9,2,-10,9,-7,-4,-4,3,5,-9,5,10,3,-9,7,1,-5,-6,-7,8,5,-4,-9,7,7,9,-3,7,4,-7,3,9,-3,6,-1,6,6,-5,9,1,7,5,10,-7,5,7,4,-10,10,-6,10,-7,2,-3,5,6,-5,3,2,-2,-4,8,5,-2,4,6,-2,10,6,-6,9,-4,-2,2,4,2,2,-5,-8,2,7,-5,2,4,9,2,3,-4,2,10,9,6,-1,-6,10,-10,5,-5,-1,8,2,-9,3,-9,-9,-3,-2,-8,9,-4,4,-5,1,8,10,3,-4,-6,-6,-4,-5,-3,-5,10,7,-3,9,-9,-8,2,3,-10,10,7,-3,10,7,5,-4,-6,-10,-1,-6,1,9,2,1,-2,9,6,10,2,-9,9,-3,-6,3,3,-8,-3,-8,-1,-8,7,-2,-3,-8,10,-1,3,-4,-6,6,8,4,3,8,-10,-8,-6,-9,-3,-2,-6,-3,-7,-8,6,4,8,-7,9,-6,2,5,4,-6,5,-1,-3,10,1,-2,-1,-3,4,9,-5,-4,7,-6,-7,10,-10,-3,-5,-2,-2,-5,3,-2,-10,-2,-6,-4,8,-5,-2,-7,8,-7,6,9,-4,-10,2,5,5,-7,-8,7,10,-2,-9,-7,10,7,-1,-3,9,-5,-7,3,10,6,-10,3,-5,2,-4,8,-3,8,-1,3,6,3,8,7,5,-5,6,-4,-3,-4,7,2,9,6,-3,-2,-4,-2,10,-2,5,-9,-5,4,1,-8,-4,-8,10,-2,2,-10], dtype = "int16")#candidate|8081|(315,)|const|int16
call_8080 = relay.TupleGetItem(func_8036_call(relay.reshape(const_8081.astype('int16'), [315,])), 6)
call_8082 = relay.TupleGetItem(func_8038_call(relay.reshape(const_8081.astype('int16'), [315,])), 6)
output = relay.Tuple([call_8056,call_8080,const_8081,])
output2 = relay.Tuple([call_8057,call_8082,const_8081,])
func_8088 = relay.Function([], output)
mod['func_8088'] = func_8088
mod = relay.transform.InferType()(mod)
output = func_8088()
func_8089 = relay.Function([], output)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8125 = relay.TupleGetItem(func_8014_call(), 0)
call_8126 = relay.TupleGetItem(func_8016_call(), 0)
uop_8131 = relay.log(call_8125.astype('float64')) # shape=(2, 15, 11)
uop_8133 = relay.log(call_8126.astype('float64')) # shape=(2, 15, 11)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
const_8140 = relay.const([[3.259460,-1.099502,-2.891638,-3.755829],[0.148789,8.297592,-9.294152,2.921261],[6.897228,-3.581543,-7.069880,-9.545264],[-2.859010,3.395576,-8.154448,-9.070015],[8.755982,4.873181,7.432203,0.624091],[-9.989712,-7.023524,0.002048,-7.937411],[9.310353,-1.732193,-5.833010,-9.355448],[-1.360641,2.675756,9.220984,-0.722227],[1.311821,6.831401,5.228150,4.959929],[6.954460,-6.006970,-1.674904,8.229714]], dtype = "float32")#candidate|8140|(10, 4)|const|float32
call_8139 = relay.TupleGetItem(func_1886_call(relay.reshape(const_8140.astype('float32'), [10, 1, 4])), 0)
call_8141 = relay.TupleGetItem(func_1888_call(relay.reshape(const_8140.astype('float32'), [10, 1, 4])), 0)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8151 = relay.TupleGetItem(func_8014_call(), 0)
call_8152 = relay.TupleGetItem(func_8016_call(), 0)
output = relay.Tuple([uop_8131,call_8139,const_8140,call_8151,])
output2 = relay.Tuple([uop_8133,call_8141,const_8140,call_8152,])
func_8161 = relay.Function([], output)
mod['func_8161'] = func_8161
mod = relay.transform.InferType()(mod)
output = func_8161()
func_8162 = relay.Function([], output)
mutated_mod['func_8162'] = func_8162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8188 = relay.TupleGetItem(func_8014_call(), 0)
call_8189 = relay.TupleGetItem(func_8016_call(), 0)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8190 = relay.TupleGetItem(func_8014_call(), 0)
call_8191 = relay.TupleGetItem(func_8016_call(), 0)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
var_8194 = relay.var("var_8194", dtype = "float32", shape = (132,))#candidate|8194|(132,)|var|float32
const_8195 = relay.const([[-6,-7],[-5,-9],[5,-8],[6,-8],[-2,-4],[-6,5],[-7,6],[6,-10],[-2,7],[1,-10],[9,-7],[-2,4],[3,-2],[-6,5],[-6,9],[-1,-6],[-7,-10],[8,5],[8,4],[6,5],[6,10],[-4,3],[-6,-10],[3,-1],[1,-9],[1,-6],[-7,-8],[8,4],[-1,-6],[-1,-3],[-1,-5],[-10,-5],[8,-10],[9,10],[8,-8],[-3,2],[7,9],[7,5],[6,4],[-4,9],[-2,-3],[-6,-4],[-10,3],[-5,7],[1,7],[7,-5],[2,1],[6,-8],[-8,9],[3,-8],[-8,-6],[4,-2],[-9,-2],[-1,-1],[6,-10],[3,-3],[10,-7],[-7,-6],[6,7],[-7,-8],[8,-7],[8,-3],[-2,-9],[1,-8],[-5,-4],[1,-7],[-5,-10],[3,-3],[7,3],[9,-10],[-1,8],[10,-2],[2,-5],[-9,-10],[9,7],[8,-5],[9,8],[4,-9],[-6,6],[2,9],[8,-6],[8,-9],[6,1],[7,8],[-1,-4],[-6,-1],[-9,-8],[-7,-4],[1,-9],[-6,10],[-6,7],[-4,-9],[-3,4],[-3,2],[2,-2],[7,1],[6,8],[10,-5],[8,10],[-4,9],[-2,-9],[-7,-9],[-10,-5],[9,-4],[-8,8],[-2,-4],[4,2],[-3,-7],[5,-1],[6,-9],[-1,3],[2,6],[2,8],[8,6],[-8,-9],[-1,-7],[10,-7],[8,-3],[2,-10],[5,-6],[1,-3],[-8,10],[-7,-8],[-5,3],[2,4],[-7,6],[4,4],[3,6],[-6,4],[8,-1],[-5,5],[3,-9],[-9,-3],[-3,6],[7,7],[-9,-6],[2,10],[-6,-8],[7,4],[1,-5],[8,7],[-8,-7],[10,-7],[-6,6],[4,1],[7,2],[-3,6],[-10,4],[-10,9],[1,-3],[1,2],[2,9],[-5,8],[2,-8],[8,6],[-6,8],[-9,-1],[5,3],[-3,-7],[-4,3],[-9,-3],[-10,-3],[-6,6],[1,-5],[-3,3],[2,5],[-1,-2],[-1,6],[5,10],[-10,-4],[3,-6],[6,-7],[2,8],[-5,3],[7,3],[-10,5],[-8,-1],[-9,-3],[-6,9],[4,2],[5,2],[-3,8],[-10,-8],[-9,8],[-10,-6],[-5,-1],[1,5],[-5,3],[-7,2],[2,9],[-2,-4],[10,10],[2,-8],[6,2],[-9,-1],[3,6],[1,-1],[-9,-4],[-7,-6],[2,-10],[-2,3],[-8,-5],[1,-3],[2,-6],[7,-3],[-10,-9],[-5,6],[1,-2],[-4,10],[10,-3],[1,-7],[5,-3],[1,-1],[3,9],[-5,3],[-3,-6],[10,1],[3,-10],[1,-7],[-3,1],[8,-6],[-3,9],[10,-1],[-7,-9],[5,8],[3,-2],[7,3],[2,3],[-7,1],[2,8],[-3,4],[-6,-8],[1,8],[-4,-2],[-10,1],[10,-1],[3,-9],[-5,-8],[5,-8],[-4,-1],[2,1],[-8,7],[10,9],[3,9],[6,-4],[6,-7],[5,10],[-4,4],[-8,2],[-10,5],[8,-9],[4,9],[-7,-10],[5,4],[3,-9],[4,-2],[10,10],[2,9],[-9,-3],[10,4],[-4,-2],[2,-1],[9,3],[-3,8],[9,-3],[-3,-3],[3,-7],[7,-10],[-6,2],[-6,4],[-2,1],[-1,9],[6,3],[4,-4],[-1,8],[2,8],[10,-5],[-2,-6],[-5,-2],[-5,-6],[-4,-2],[2,-5],[-7,-2],[-3,-9],[2,-1],[-5,1],[-3,4],[-3,-9],[-9,5],[-7,6],[-5,6],[-1,-1],[1,7],[9,5],[10,-10],[-2,-2],[-9,2],[-7,-1],[9,8],[-2,-2],[3,10],[7,3],[-5,-2],[1,-5],[1,6],[8,-10],[-7,-6],[9,4],[7,-5],[-7,4],[1,-8],[8,-3],[-3,-6],[-6,-7],[-7,2],[10,8],[-9,-2],[1,-8],[-1,-9],[2,-9],[10,-7],[2,-1],[-8,4],[10,5],[-7,6],[4,4],[-2,4],[2,-10],[-1,-1],[2,3]], dtype = "uint64")#candidate|8195|(330, 2)|const|uint64
call_8193 = relay.TupleGetItem(func_1719_call(relay.reshape(var_8194.astype('float32'), [12, 1, 11]), relay.reshape(const_8195.astype('uint64'), [660,]), ), 1)
call_8196 = relay.TupleGetItem(func_1723_call(relay.reshape(var_8194.astype('float32'), [12, 1, 11]), relay.reshape(const_8195.astype('uint64'), [660,]), ), 1)
bop_8201 = relay.logical_xor(const_8195.astype('int16'), relay.reshape(call_8193.astype('int16'), relay.shape_of(const_8195))) # shape=(330, 2)
bop_8204 = relay.logical_xor(const_8195.astype('int16'), relay.reshape(call_8196.astype('int16'), relay.shape_of(const_8195))) # shape=(330, 2)
output = relay.Tuple([call_8188,call_8190,var_8194,bop_8201,])
output2 = relay.Tuple([call_8189,call_8191,var_8194,bop_8204,])
func_8206 = relay.Function([var_8194,], output)
mod['func_8206'] = func_8206
mod = relay.transform.InferType()(mod)
var_8207 = relay.var("var_8207", dtype = "float32", shape = (132,))#candidate|8207|(132,)|var|float32
output = func_8206(var_8207)
func_8208 = relay.Function([var_8207], output)
mutated_mod['func_8208'] = func_8208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8224 = relay.var("var_8224", dtype = "uint8", shape = ())#candidate|8224|()|var|uint8
var_8225 = relay.var("var_8225", dtype = "uint8", shape = (7, 2, 6))#candidate|8225|(7, 2, 6)|var|uint8
bop_8226 = relay.multiply(var_8224.astype('uint8'), var_8225.astype('uint8')) # shape=(7, 2, 6)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
var_8239 = relay.var("var_8239", dtype = "float32", shape = (132,))#candidate|8239|(132,)|var|float32
var_8240 = relay.var("var_8240", dtype = "uint64", shape = (10, 66))#candidate|8240|(10, 66)|var|uint64
call_8238 = relay.TupleGetItem(func_1719_call(relay.reshape(var_8239.astype('float32'), [12, 1, 11]), relay.reshape(var_8240.astype('uint64'), [660,]), ), 2)
call_8241 = relay.TupleGetItem(func_1723_call(relay.reshape(var_8239.astype('float32'), [12, 1, 11]), relay.reshape(var_8240.astype('uint64'), [660,]), ), 2)
uop_8243 = relay.log10(bop_8226.astype('float64')) # shape=(7, 2, 6)
output = relay.Tuple([call_8238,var_8239,var_8240,uop_8243,])
output2 = relay.Tuple([call_8241,var_8239,var_8240,uop_8243,])
func_8256 = relay.Function([var_8224,var_8225,var_8239,var_8240,], output)
mod['func_8256'] = func_8256
mod = relay.transform.InferType()(mod)
var_8257 = relay.var("var_8257", dtype = "uint8", shape = ())#candidate|8257|()|var|uint8
var_8258 = relay.var("var_8258", dtype = "uint8", shape = (7, 2, 6))#candidate|8258|(7, 2, 6)|var|uint8
var_8259 = relay.var("var_8259", dtype = "float32", shape = (132,))#candidate|8259|(132,)|var|float32
var_8260 = relay.var("var_8260", dtype = "uint64", shape = (10, 66))#candidate|8260|(10, 66)|var|uint64
output = func_8256(var_8257,var_8258,var_8259,var_8260,)
func_8261 = relay.Function([var_8257,var_8258,var_8259,var_8260,], output)
mutated_mod['func_8261'] = func_8261
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8281 = relay.var("var_8281", dtype = "float64", shape = (4, 14, 7))#candidate|8281|(4, 14, 7)|var|float64
uop_8282 = relay.log(var_8281.astype('float64')) # shape=(4, 14, 7)
output = uop_8282
output2 = uop_8282
func_8298 = relay.Function([var_8281,], output)
mod['func_8298'] = func_8298
mod = relay.transform.InferType()(mod)
var_8299 = relay.var("var_8299", dtype = "float64", shape = (4, 14, 7))#candidate|8299|(4, 14, 7)|var|float64
output = func_8298(var_8299)
func_8300 = relay.Function([var_8299], output)
mutated_mod['func_8300'] = func_8300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8088_call = mod.get_global_var('func_8088')
func_8089_call = mutated_mod.get_global_var('func_8089')
call_8305 = relay.TupleGetItem(func_8088_call(), 2)
call_8306 = relay.TupleGetItem(func_8089_call(), 2)
output = relay.Tuple([call_8305,])
output2 = relay.Tuple([call_8306,])
func_8318 = relay.Function([], output)
mod['func_8318'] = func_8318
mod = relay.transform.InferType()(mod)
output = func_8318()
func_8319 = relay.Function([], output)
mutated_mod['func_8319'] = func_8319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8326 = relay.TupleGetItem(func_8014_call(), 0)
call_8327 = relay.TupleGetItem(func_8016_call(), 0)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8334 = relay.TupleGetItem(func_8014_call(), 0)
call_8335 = relay.TupleGetItem(func_8016_call(), 0)
func_6139_call = mod.get_global_var('func_6139')
func_6145_call = mutated_mod.get_global_var('func_6145')
var_8337 = relay.var("var_8337", dtype = "float32", shape = (240,))#candidate|8337|(240,)|var|float32
const_8338 = relay.const([-5.834343,8.383255,5.402871,1.447234,-2.924929,3.263641,2.433920,-3.269478,1.219359,-2.644981,-8.053289,2.213856,3.296973,-6.070237,4.772666,-5.481301,8.917422,-4.905704,9.622519,9.048552,2.793395,-1.841350,0.695541,1.171952,-7.676144,7.018748,0.371039,8.568703,3.289675,-0.294079,-9.234332,8.533467,-7.104403,-3.641093,3.799651,-2.352807,-0.096540,0.462205,5.454663,-3.133312,-7.484586,-8.488346,2.387852,-8.099499,2.205871,1.617202,-5.073274,0.775679,1.790471,-7.250112,1.749215,5.996778,9.130170,-1.358605,0.019607,6.983289,-0.987520,4.875380,3.706354,9.981402,-5.151651,-7.479006,5.085346,-8.039342,8.330906,8.609041,8.742397,-2.518111,3.727389,6.912692,-4.565109,-0.461591,6.689947,-2.170922,0.832936,1.231936,-9.047021,-9.900920,-0.390570,-2.682657,0.615332,-8.684945,-0.753742,-2.448825,5.629752,-5.640016,-6.932912,7.884847,7.225641,-0.418781,4.861977,-6.455700,-6.246900,6.407823,3.363642,-6.165404,6.597007,6.348294,-2.821961,6.700188,-0.212703,9.276206,-2.290887,-1.357522,-3.087460,-2.886823,-5.754130,7.787989,-6.511067,8.739072,8.529511,-3.321342,8.035146,-8.659339,6.886458,0.460791,-2.529668,-3.609275,1.877911,-0.042444,-8.855607,5.798488,3.424543,0.964807,3.498881,-6.853004,-8.589760,9.896240,-7.644328,6.001923,3.622650,1.263968,2.623031,-0.560249,-0.767362,-3.744690,-7.110475,-1.349956,3.732066,9.289379,-1.941686,9.152992,-3.340804,-3.015897,-2.650394,4.008692,8.770225,1.079683,-3.682963,0.503811,-8.647834,4.246706,-5.577166,7.505981,9.497604,-9.802429,-2.421457,3.247077,8.386614,7.356565,1.461313,0.648378,-9.090663,-3.685303,4.926418,6.077386,8.769497,-9.114053,-0.765853,6.456526,-3.368240,-4.600758,3.280045,3.964505,0.879070,8.146498,2.067989,2.006690,2.735572,2.827572,-7.307226,8.586576,0.229767,6.989652,3.202454,-3.752061,-6.601076,-3.657188,-8.437608,-2.215878,-2.408045,-3.250740,2.305813,8.704469,6.005544,7.286855,-0.014961,-9.864304,-6.034419,0.832693,-1.383372,0.396735,-3.625674,9.336309,7.372761,4.794952,9.987070,-7.216639,8.075964,8.378282,-2.876561,-2.319331,7.902889,-8.592335,-0.917526,5.432212,3.832131,-8.549715,-0.622857,-0.938603,5.561320,-4.970420,-2.233403,3.031547,-4.339203,-1.855503,1.074288,6.268739,4.833529,-8.271828,-2.779711,4.713207,-3.417106,4.919606,2.834487,5.137681,5.811351,8.798397,-4.227315,-1.172495,0.629987,3.511253,5.135547,-8.600962,-0.262614,8.691460,-0.645539,0.267139,-0.829883,-2.996479,-7.248231,-1.453213,1.299439,3.243766,7.398157,-3.221307,1.612533,9.835193,9.969108,1.294228,8.419067,-6.373542,5.793722,-4.026922,-0.665841,0.323722,-5.046668,7.858088,4.783232,7.012599,-0.066107,-6.982505,7.234900,-8.028577,8.965140,0.224353,-8.551915,-4.619689,4.160958,4.323419,7.148160,-4.237579,9.324087,9.137360,0.400010,0.175236,2.558840,3.758375,3.662916,5.134358,6.101324,3.145398,-9.315990,-0.055735,7.804090,8.366729,-2.635980,-0.482472,4.944707,7.201550,5.338806,-3.537051,-4.673519,9.698593,-1.132142,-8.984980,8.323569,7.995855,2.314245,8.389938,-0.929300,-3.569946,0.817223,-0.457206,-9.072964,8.209562,-8.016324,-1.707898,1.024187,-7.599700,-4.549254,8.665704,6.607736,8.256674,-1.963621,2.660388,-0.248868,-1.206356,-8.380997,-1.960680,-0.361572,-0.865207,-4.052903,9.133737,9.063523,4.810502,-2.658819,7.932199,6.367723,-1.284655,-7.827093,-6.680517,1.828608,-9.200280,7.160909,2.663681,-2.747636,-1.538040,-0.417369,-7.270177,-5.892535,-5.059748,-7.819842,-4.224900,-3.210305,-7.487857,-6.668503,8.812446,4.594876,3.589051,0.902839,-2.077845,0.401963,-3.383858,-1.676055,0.543383,-3.070816,5.191901,9.130308,-4.972846,-6.730121,-6.778539,-7.315609,9.445918,3.251909,-2.845684,4.882311,-3.764565,-4.352280,-8.748022,0.964331,8.270235,8.196840,1.543473,-9.563060,5.959507,-6.472940,6.051088,2.563742,-8.128871,0.081492,1.879810,5.607601,3.083424,-7.120980,-4.024831,5.244709,6.647191,-6.097946,-8.335871,3.154877,4.312572,8.556848,-7.382809,5.404478,-2.190192,9.429461,4.103163,8.420671,-7.339257,7.850238,-9.850476,-9.890455,7.765956,-8.744799,3.082994,8.804756,5.136290,2.453990,-5.284732,-6.256883,-8.509424,-5.681327,-0.151149,-2.794953,-7.618045,5.307734,9.512156,-4.484720,-2.166651,-3.226743,-0.372239,-1.714584,-7.990003,3.265046,6.527344,7.026198,-6.901769,7.438004,-9.775097,2.621354,6.329687,1.439315,5.718315,-0.462693,-0.831896,5.700006,-1.299679,-5.362902,-1.807416,6.883685,0.177314,4.836617,0.896452,-0.455961,-4.855048,-5.546998,-2.816746,-4.805067,1.986278,1.381347,9.181369,9.655354,-4.143510,0.226555,1.448432,-3.620801,5.849985,-8.894172,6.198035,-6.234651,1.077507,3.709056,-9.447236,1.103217,-6.228589,9.145755,8.117843,-0.364887,-1.428777,-9.789916,-0.653766,-0.558403,-3.387993,-2.051119,8.686252,-3.535092,5.409621,-6.724361,3.768316,-5.447869,-4.630616,-4.819792,-6.537859,-7.785714,-7.954127,-7.910147,9.049571,-8.756280,-5.385043,7.358387,-1.334894,-2.445076,-6.174877,5.128349,-9.045107,8.278302,-1.601543,-4.935283,-5.702331,3.659815,-9.748083,-6.644943,2.282304,9.693130,5.649789,0.187816,-7.283884,-8.413495,8.837659,9.415826,1.329950,-6.592537,-9.223881,-8.952817,8.459859,9.978812,4.769214,-3.725652,-1.226333,-7.137184,-8.584971,0.359966,8.232224,1.388662,-6.427403,-4.270204,-5.385604,2.932600,-0.582581,2.580944,4.563493,7.429109,-5.498816,2.805771,0.966265,7.815136,-5.857203,9.002768,-2.896005,-9.929034,2.579848,-1.460856,5.376518,-4.925342,8.773960,-6.479960,-8.580237,3.015493,6.457035,6.462427,4.149833,-3.317525,-5.059643,1.680167,0.873069,9.743729,1.884152,-4.584069,5.482255,-7.880366,-3.995849,4.844100,-4.635662,-2.199053,-2.391775,-9.155510,-9.878305,5.609423,-7.012279,2.392721,-5.961074,-3.132910,-4.541091,-7.064121,3.927646,-4.546899,3.590943,-6.478230,-1.521159,7.928379,4.492370,-3.260747,4.552289,-7.351996,0.529827,5.040045,-6.052461,0.427640,-7.636657,-7.592572,-5.318682,6.185906,-5.968548,0.751945,-9.085424,1.069073,-8.223698,3.966131,8.509374,-1.834912,5.852286,-0.823940,7.770208,-0.212413,-0.313177,-6.859209,6.163769,-6.148342,3.149292,3.018427,5.625879,8.300390,-1.807361,9.649462,-3.364808,-4.915103,7.906059,0.327747,-4.544949,-5.077784,-5.073987,6.324998,-6.020085,-9.919037,4.035852,-9.929868,-6.488265,2.866078,-3.393550,2.618850,-1.033211,8.384986,-4.456908,-8.975491,-7.473959,5.854739,4.667737,4.923345,9.813723,-1.410901,1.165664,0.791695,-0.403879,-1.980727,4.483172,-6.785272,-4.531264,7.060600,-3.327327,0.803453,-5.645758,-8.525762,-5.681589,3.681376,0.342375,-2.511267,-4.698024,-9.214882,-5.488921,-5.085580,-1.551469,0.985088,-6.968713,-7.412665,9.664329,3.482344,-2.395879,6.524149,9.633676,-0.160270,-3.841475,5.359322,-7.637361,-5.327378,4.807697,-0.580128,3.699227,-2.166778,-1.211410,-3.102457,-1.002515,3.710913,8.905481,0.486726,-6.037355,6.382783,9.836441,7.740430,6.640518,-9.960958,-0.765179,-4.073932,7.632764,7.339706,5.564268,5.409533,-2.284854,5.167319,7.073703,-0.850118,-8.093874,6.040471,0.090351,-5.757924,-5.860167,8.481177,8.630129,-2.932296,-2.623769,6.485240,1.118712,1.924888,4.702403,-0.720406,-7.431580,-0.981193,-8.118130,-2.080634,3.115072,-5.789424,8.840799,-5.146814,-3.060195,5.978463,4.312978,-0.293533,3.215276,-4.138363,-4.683904,-5.292763,1.931241,-8.110053,-7.593697,2.287541,5.270564,5.595042,8.349587,3.570029,-0.662125,-2.526961,6.366843,-1.932777,2.353767,-2.763069,7.934258,-6.814995,1.768751,8.477040,5.759087,7.888787,-3.383831,0.945612,1.893945,3.338770,-8.729111,1.553073,8.741436,-6.431390,-7.721704,-7.492354,0.579397,-2.232732,4.669816,-1.052432,2.402148,5.969701,-7.005485,5.923075,-8.167798,7.571659,1.917624,-1.191099,0.526983,0.698538,0.727576,7.166876,-2.328370,-8.903275,6.045513,-3.939191,-7.971125,1.371953,-8.643559,-6.798640,3.201651,8.560916,-1.187980,1.210448,4.961153,9.984943,9.439532,1.471695,7.806651,9.784658,4.492380,3.912461,-8.164680,-0.120839,2.023039,6.636382,9.247660,9.791716,-4.272287,7.444910,4.078687,6.287362,3.616279,-9.987471,-4.074567,-5.107711,7.444531,2.154092,-8.001496,1.377179,7.893165,-3.280022,5.414881,-9.868765,7.120576,8.175278,5.855208,8.606992,-0.575053,6.920359,2.972331,-3.990080,4.024328,-6.947297,0.735604,5.380756,-4.571641,6.547551,-6.702350,-9.907960,9.210919,-5.317725,-7.532363,-6.352922,-1.102826,5.630062,5.892390,-8.034547,6.310036,-3.241116,-1.325403,8.565974,4.488413,6.322140,4.044895,2.427445,1.893243,8.709229,2.961281,-4.046049,2.432553,-3.106737,5.093971,8.890610,4.724744,-4.274005,7.452632,4.180507,-4.934553,-4.328978,-6.374794,4.905466,-0.543688,0.971430,-8.906388,4.378394,8.666142,-1.223877,-6.031959,1.161261,5.315043,-8.234981,-1.089078,9.907806,-2.478864,-2.851272,-1.089197,-9.839266,-3.409359,-3.455010,-4.865103,-1.226414,9.323362,-9.853037,-2.414013], dtype = "float64")#candidate|8338|(900,)|const|float64
var_8339 = relay.var("var_8339", dtype = "float32", shape = (320,))#candidate|8339|(320,)|var|float32
var_8340 = relay.var("var_8340", dtype = "float32", shape = (40,))#candidate|8340|(40,)|var|float32
call_8336 = relay.TupleGetItem(func_6139_call(relay.reshape(var_8337.astype('float32'), [3, 10, 8]), relay.reshape(const_8338.astype('float64'), [18, 50]), relay.reshape(var_8339.astype('float32'), [40, 8]), relay.reshape(var_8340.astype('float32'), [40,]), ), 1)
call_8341 = relay.TupleGetItem(func_6145_call(relay.reshape(var_8337.astype('float32'), [3, 10, 8]), relay.reshape(const_8338.astype('float64'), [18, 50]), relay.reshape(var_8339.astype('float32'), [40, 8]), relay.reshape(var_8340.astype('float32'), [40,]), ), 1)
func_6139_call = mod.get_global_var('func_6139')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_8358 = relay.TupleGetItem(func_6139_call(relay.reshape(var_8337.astype('float32'), [3, 10, 8]), relay.reshape(const_8338.astype('float64'), [18, 50]), relay.reshape(var_8339.astype('float32'), [40, 8]), relay.reshape(var_8340.astype('float32'), [40,]), ), 4)
call_8359 = relay.TupleGetItem(func_6145_call(relay.reshape(var_8337.astype('float32'), [3, 10, 8]), relay.reshape(const_8338.astype('float64'), [18, 50]), relay.reshape(var_8339.astype('float32'), [40, 8]), relay.reshape(var_8340.astype('float32'), [40,]), ), 4)
var_8362 = relay.var("var_8362", dtype = "float32", shape = (40, 8))#candidate|8362|(40, 8)|var|float32
bop_8363 = relay.right_shift(call_8358.astype('int8'), relay.reshape(var_8362.astype('int8'), relay.shape_of(call_8358))) # shape=(40, 8)
bop_8366 = relay.right_shift(call_8359.astype('int8'), relay.reshape(var_8362.astype('int8'), relay.shape_of(call_8359))) # shape=(40, 8)
func_6139_call = mod.get_global_var('func_6139')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_8416 = relay.TupleGetItem(func_6139_call(relay.reshape(var_8337.astype('float32'), [3, 10, 8]), relay.reshape(call_8336.astype('float64'), [18, 50]), relay.reshape(bop_8363.astype('float32'), [40, 8]), relay.reshape(var_8340.astype('float32'), [40,]), ), 5)
call_8417 = relay.TupleGetItem(func_6145_call(relay.reshape(var_8337.astype('float32'), [3, 10, 8]), relay.reshape(call_8336.astype('float64'), [18, 50]), relay.reshape(bop_8363.astype('float32'), [40, 8]), relay.reshape(var_8340.astype('float32'), [40,]), ), 5)
output = relay.Tuple([call_8326,call_8334,call_8336,var_8337,const_8338,var_8339,var_8340,bop_8363,call_8416,])
output2 = relay.Tuple([call_8327,call_8335,call_8341,var_8337,const_8338,var_8339,var_8340,bop_8366,call_8417,])
func_8421 = relay.Function([var_8337,var_8339,var_8340,var_8362,], output)
mod['func_8421'] = func_8421
mod = relay.transform.InferType()(mod)
mutated_mod['func_8421'] = func_8421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8421_call = mutated_mod.get_global_var('func_8421')
var_8423 = relay.var("var_8423", dtype = "float32", shape = (240,))#candidate|8423|(240,)|var|float32
var_8424 = relay.var("var_8424", dtype = "float32", shape = (320,))#candidate|8424|(320,)|var|float32
var_8425 = relay.var("var_8425", dtype = "float32", shape = (40,))#candidate|8425|(40,)|var|float32
var_8426 = relay.var("var_8426", dtype = "float32", shape = (40, 8))#candidate|8426|(40, 8)|var|float32
call_8422 = func_8421_call(var_8423,var_8424,var_8425,var_8426,)
output = call_8422
func_8427 = relay.Function([var_8423,var_8424,var_8425,var_8426,], output)
mutated_mod['func_8427'] = func_8427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8431 = relay.TupleGetItem(func_8014_call(), 0)
call_8432 = relay.TupleGetItem(func_8016_call(), 0)
uop_8434 = relay.log10(call_8431.astype('float64')) # shape=(2, 15, 11)
uop_8436 = relay.log10(call_8432.astype('float64')) # shape=(2, 15, 11)
output = uop_8434
output2 = uop_8436
func_8443 = relay.Function([], output)
mod['func_8443'] = func_8443
mod = relay.transform.InferType()(mod)
output = func_8443()
func_8444 = relay.Function([], output)
mutated_mod['func_8444'] = func_8444
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8466 = relay.var("var_8466", dtype = "float64", shape = (4, 10, 7))#candidate|8466|(4, 10, 7)|var|float64
uop_8467 = relay.log2(var_8466.astype('float64')) # shape=(4, 10, 7)
uop_8478 = relay.log10(uop_8467.astype('float64')) # shape=(4, 10, 7)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_8496 = relay.TupleGetItem(func_8318_call(), 0)
call_8497 = relay.TupleGetItem(func_8319_call(), 0)
output = relay.Tuple([uop_8478,call_8496,])
output2 = relay.Tuple([uop_8478,call_8497,])
func_8508 = relay.Function([var_8466,], output)
mod['func_8508'] = func_8508
mod = relay.transform.InferType()(mod)
var_8509 = relay.var("var_8509", dtype = "float64", shape = (4, 10, 7))#candidate|8509|(4, 10, 7)|var|float64
output = func_8508(var_8509)
func_8510 = relay.Function([var_8509], output)
mutated_mod['func_8510'] = func_8510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_8596 = relay.TupleGetItem(func_8318_call(), 0)
call_8597 = relay.TupleGetItem(func_8319_call(), 0)
output = call_8596
output2 = call_8597
func_8644 = relay.Function([], output)
mod['func_8644'] = func_8644
mod = relay.transform.InferType()(mod)
output = func_8644()
func_8645 = relay.Function([], output)
mutated_mod['func_8645'] = func_8645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_8690 = relay.TupleGetItem(func_8318_call(), 0)
call_8691 = relay.TupleGetItem(func_8319_call(), 0)
func_4843_call = mod.get_global_var('func_4843')
func_4846_call = mutated_mod.get_global_var('func_4846')
const_8693 = relay.const([-2.840169,-9.884889,-3.341948,-5.903695,2.200944,1.433652,-9.832806,-3.095516,5.079976,-6.118682,-7.575271,8.147244,-1.383975,2.345562,-3.464101,-2.524607,3.586239,-3.152315,7.818352,5.310890,3.980360,4.645544,3.567669,-4.542954,-9.720988,-6.898178,-8.233861,-0.858973,-5.278085,-1.352505,-8.631563,-4.122468,1.998676,8.846801,5.636707,-7.901564,0.857411,-4.477518,9.630206,2.249384,7.299350,3.109172,-2.068889,-9.926338,1.590247,5.026982,-4.063287,2.728565,-3.038411,-9.657262,-7.926947,-3.347654,-5.088837,-6.390661,4.991725,4.885656,-6.293661,2.365760,-3.045870,0.576145,-2.688560,9.760336,-7.036320,2.115456,-0.734086,3.246272,-2.553341,-2.544167,-4.434518,-5.956538,0.692187,4.707386,-7.253419,-6.928820,-5.428074,-9.291346,-4.326236,3.901264,8.005665,0.916880,-5.172445,-4.537893,3.740171,2.291777,9.417885,2.507817,-5.509049,-4.844142,6.563657,3.775059,2.760617,7.463779,-7.835538,-3.862187,8.189664,7.250598,-0.636694,-9.454909,-4.241580,-1.267516,2.717551,-6.584853,-6.497378,7.265309,9.196897,3.001887,-9.548181,-2.411180,-5.435316,-2.303935,0.595944,6.227468,2.287017,2.045287,-3.650450,-9.062161,1.442439,4.959684,3.686218,-0.543745,6.102507,3.062093,-8.499603,-3.944377,3.586004,-4.033227,-9.869555,-2.106209,9.065181,-6.633380,0.006523,4.619880,0.557348,-7.853478,1.248390,-1.374529,0.047688,4.073764,1.786785,-0.966033,-2.349072,6.382448,-0.704583,3.301192,5.271629,4.615225,-9.863197,-1.045122,5.028097,-9.796799,2.837342,-4.214285,8.724064,-4.435526,9.800751,0.724811,5.919390,5.730034,-5.571361,8.447137,-7.437705,6.344503,0.494861,-6.890553,-3.337913,-1.968032,2.220318,-7.045622,-7.814777,-8.043750,9.232175,8.177032,-2.369549,5.235137,6.180714,6.860397,9.192136,-5.277003,-0.951555,-9.701321,-1.419047,-0.507306,4.611937,-1.895773,5.641416,5.699955,-7.825982,0.647165,8.273670,0.350985,9.964782,-5.877766,5.209905,0.310704,-7.955451,2.410022,-0.267742,-3.851146,-3.423603,5.898133,8.244877,4.765750,-4.717618,9.215774,1.459029,-8.641891,0.033026,4.355857,-8.700958,-7.236820,-9.914649,5.505576,9.069669,-5.458310,-6.640597,5.364360,3.476608,8.121767,9.641676,6.209177,9.018443,1.266745,4.163084,-6.542830,6.849781,-2.025931,-6.608960,1.575018,9.677430,3.322720,7.860153,-1.243290,9.754107,-4.659478,-3.924964,6.706166,-0.574652,-3.252855,-0.936973,7.613157,7.084819,9.772895,7.790056,4.344678,7.177411,-3.716325,8.241118,3.729899,-3.662226,4.384062,4.154342,-1.506229,6.523132,4.556845,1.777362,5.237425,-5.385695,-2.398041,4.970882,2.374841,1.889167,-7.399236,-8.651646,4.540690,9.064715,0.700574,-7.180505,-8.534125,-2.623998,5.726332,-5.420907,-5.233031,1.243937,-2.524436,-2.146981,5.175563,5.792955,-2.804831,4.913227,-6.206678,-5.235696,-7.279910,-9.393735,-8.425941,-0.225951,-0.007692,-0.518839,-7.768472,-8.454417,4.424880,-4.863487,-7.452481,-1.493217,4.462758,-1.238032,-2.336240,5.506638,7.508179,-6.549624,-5.053542,2.708004,1.249965,8.154097,-0.012071,8.329705,-6.384603,-4.122295,0.173238,7.966514,3.643606,1.129042,-0.193293,-1.956637,-8.050352,7.036585,2.531750,2.849488,-4.447924,-1.793130,-3.523484,-3.511120,5.384593,9.742368,0.445092,9.994120,1.218168,5.699670,4.424054,3.337487,-2.956382,-5.267358,-3.333392,-2.735372,-3.546432,5.979766,-2.168404,4.047612,-5.120158,3.344405,2.261297,-8.597021,4.988810,-8.701780,6.881949,-3.593499,-6.217033,-0.256280,-4.225592,-1.364897,8.327625,-0.817339,5.822184,-1.627260,-7.894450,-8.095209,-1.791856,-3.694560,-6.275770,7.064322,4.126123,0.147779,-3.298241,-0.302313,-1.763251,-5.705551,-0.636568,-0.702183,-1.746295,9.648669,-5.538440,6.560700,1.113273,-2.505575,-3.830510,6.939374,3.436551,-3.194211,-7.588639,-2.331160,5.770741,8.041525,9.564440,0.669643,-7.003437,3.517782,-1.594909,4.161852,-1.181666,2.160392,6.205785,-8.291607,4.965431,3.727068,3.080316,2.384650,-0.579227,-9.504863,-4.876895,9.854768,6.689194,0.291524,6.844613,2.803481,-1.910921,9.843786,9.858544,-5.088723,-1.982267,2.198483,2.304836,-8.950767,3.098344,-5.900459,-5.900129,-9.510749,-2.623692,-7.304312,-5.491802,6.773102,-9.267182,2.144531,5.968164,7.987056,4.536256,9.823092,4.665354,-5.603841,1.020617,-4.219622,-7.005880,9.538239,-6.317301,7.950919,4.618553,9.337470,6.561898,6.314640,-6.879977,-2.511014,7.302572,-4.000795,4.906339,5.165646,9.941035,-6.995133,-7.451728,-5.737838,6.724619,-4.201482,3.735264,9.626812,-1.940811,6.806607,9.908268,-9.781872,2.013907,7.813941,7.481894,5.980273,-4.374791,-9.438160,5.922382,5.642181,-8.185096,3.681349,9.780521,-1.949967,-1.868867,-0.626653,2.910501,-0.281499,9.061175,8.298163,2.002063,-6.037823,4.690479,-6.075321,1.594360,2.644548,5.930226,6.071005,9.927055,-6.629719,8.551667,3.834388,0.729346,-3.453952,6.977687,4.617097,-6.051593,-0.656637,1.778691,0.277659,-4.290370,-5.891667,5.778220,-9.233994,-1.423211,-2.002066,9.909391,-8.248801,-7.175740,-8.771844,1.734602,-8.002739,7.267490,3.150434,8.537978,0.001644,5.143350,-5.551449,-9.539669,-7.697324,3.524879,-7.277758,-9.587744,-4.660668,5.617745,6.353469,-4.524499,4.688452,-3.115553,-2.049000,3.625006,-1.295063,-5.901950,2.881132,7.234587,2.295479,6.583520,-1.771178,-2.812721,-3.942920,8.933326,-3.535584,6.331407,1.690767,-7.526309,0.284335,3.620844,9.944234,-0.490219,-2.448352,-3.538030,5.967783,-4.507493,0.139318,-6.147932,-7.614711,4.918301,4.824629,-7.624171,5.356420,3.455100,-1.307014,-7.401029,-5.305211,5.117678,-6.366583,-8.980317,5.473816,6.256698,0.814369,-8.271791,4.006073,1.667590,-2.176120,8.433345,-1.795722,-6.968225,-4.114651,-6.103700,-2.355795,4.371738,1.416140,-2.864148,-1.399202,-8.438054,9.382945,-6.511625,-7.012751,7.362597,1.056370,-2.738738,8.452029,1.089775,1.498703,-5.755845,4.261256,6.328613,3.067170,5.319478,6.096031,-0.364608,-7.976517,-9.210477,-1.743983,4.084718,-6.398844,2.637614,-0.696459,8.891546,3.674828,9.399789,-5.772985,9.318385,-7.884009,0.501219,-1.712093,-2.220741,-0.559773,-5.786229,9.660439,2.045118,5.887491,8.074244,4.968252,-7.015177,2.374876,5.632086,-0.554628,9.573000,7.819158,-7.126991,-5.211855,-6.781056,8.621047,0.584018,-2.580584,6.726089,-5.534549,8.075517,2.839986,-4.472636,-9.628968,-3.224330,-2.991811,8.116258,1.638343,-1.390241,4.907962,-3.241426,1.832457,5.082332,-1.254658,0.681724,9.193343,-9.447960,-1.390414,9.866371,-1.619328,8.873884,-5.994518,-8.653068,8.059411,7.332560,5.719286,3.166201,-6.153895,-3.449706,5.238897,7.061665,2.982235,-1.931315,-8.994602,-0.025571,3.884829,3.100059,-1.694123,0.160143,-0.566218,-3.118821,9.512245,-4.603730,-7.678049,-4.714533,8.352160,2.326001,-3.025932,-0.472360,6.857104,4.670780,2.271028,-1.501385,2.370044,1.275029,1.264531,6.245670,3.908893,-7.049649,9.435119,-9.113821,-7.408279,8.066159,2.734346,4.647470,-7.690033,7.398700,9.422331,7.978260,-4.242207,8.647055,4.077589,-6.196578,-9.228380,-6.560531,9.161634,-8.451886,-0.482203,-3.360876,-0.514374,0.862410,8.790162,-4.563849,-1.147634,1.544557,-7.799992,-7.969960,0.357996,-3.965524,8.766719,8.129458,2.558787,-9.795271,1.946577,6.121440,-4.727534,-3.127269,-3.064169,9.088214,4.081558,2.121380,4.969781,0.951680,-7.004978,-6.791813,-0.576350,-2.778785,-9.264013,-3.264545,-3.821485,3.753354,-4.037443,-3.984681,-2.126082,2.126811,-3.863440,2.349658,3.756945,-1.895057,-6.241445,0.418728,5.002546,7.793207,9.270169,0.201731,0.387143,-3.857248,3.222069,-4.846905,-8.246830,6.709030,-4.291181,-4.776908,0.276453,7.969651,-3.239665,-0.417972,2.889499,6.465632,5.529336,-7.850975,5.733167,-9.410206,0.174877,-7.572421,2.535151,-0.398525,-8.187157,8.105334,0.968661,2.344701,4.002846,4.493860,7.495834,1.180386,-7.517219,-7.353471,9.972320,-4.228100,0.232959,-2.913201,-8.279625,0.613940,-7.444259,-6.519199,0.423875,3.335953,2.627598,7.601256,7.446205,-8.123636,-8.892479,9.333782,5.387332,-2.179391,-0.257644,9.784570,0.244722,8.872244,1.954265,-8.482292,0.094774,-6.672076,-1.223214,-3.014359,-5.398288,4.260082,6.715459,-5.976011,-1.239246,6.257464,-7.634896,2.503917,9.462428,7.144522,-9.582085,-6.933046,0.849029,7.761818,-7.618013,5.306960,-9.663900,-2.910892,5.142667,-3.442426,3.399419,-6.625477,1.887976,-9.473598,-1.825038,4.581087,7.778999,-4.386262,-4.299164,-4.801584,8.890361,-0.295107,9.613701,6.941403,3.853972,-4.169230,-2.694600,-8.630563,9.344091,-3.175931,-2.233245,-7.817586,5.743374,-6.798969,-5.998976,1.603200,-9.700200,3.625878,-5.999191,-4.478239,3.098539,-5.189154,5.616051,4.185280,6.858498,-7.472942,9.736510,5.748205,-8.637312,4.595735,3.915306,-9.126073,-2.654959,1.102975,4.745731,-1.984091,-1.504202,-7.078435,-6.552926,-0.359595,0.382331,0.284570,-4.249589,-4.557145,0.959599,6.945491,-2.880632,-4.598867,-9.459552,2.657034,-8.254296,-5.571506,-0.890668,-2.324945], dtype = "float64")#candidate|8693|(900,)|const|float64
call_8692 = func_4843_call(relay.reshape(const_8693.astype('float64'), [10, 10, 9]), relay.reshape(const_8693.astype('float64'), [10, 10, 9]), )
call_8694 = func_4843_call(relay.reshape(const_8693.astype('float64'), [10, 10, 9]), relay.reshape(const_8693.astype('float64'), [10, 10, 9]), )
func_1926_call = mod.get_global_var('func_1926')
func_1928_call = mutated_mod.get_global_var('func_1928')
var_8696 = relay.var("var_8696", dtype = "float32", shape = (2520,))#candidate|8696|(2520,)|var|float32
call_8695 = func_1926_call(relay.reshape(var_8696.astype('float32'), [12, 15, 14]))
call_8697 = func_1926_call(relay.reshape(var_8696.astype('float32'), [12, 15, 14]))
func_3591_call = mod.get_global_var('func_3591')
func_3597_call = mutated_mod.get_global_var('func_3597')
var_8699 = relay.var("var_8699", dtype = "float64", shape = ())#candidate|8699|()|var|float64
const_8700 = relay.const([[5,-2],[-8,3],[-6,-4],[-7,-5],[-9,9],[-1,4],[-4,-9],[-1,8],[9,-2],[1,-4],[8,-3],[4,-3],[3,1],[-4,10],[-1,3],[-3,9],[3,6],[9,-10],[1,-3],[3,6],[-9,-10],[1,3],[10,-4],[-8,-5],[-6,-4],[-5,1],[8,-1],[-9,7],[-5,3],[8,7],[-3,-10],[-6,4],[10,-7],[2,10],[-2,-1],[9,9],[6,9],[-7,3],[-1,-10],[10,9],[2,4],[3,-6],[-5,6],[-6,6],[-6,-9],[3,-2],[4,1],[4,3],[-7,-1],[-1,7],[-5,-9],[-9,-6],[-10,-9],[-4,-7],[-3,-4],[10,4],[-6,-10],[-2,-2],[4,-10],[6,10],[-9,-1],[2,-5],[8,-3],[-9,-6],[3,-6],[6,4],[1,3],[-1,5],[1,-5],[6,9],[9,2],[2,7],[-5,2],[10,1],[1,-9],[4,2],[-2,10],[7,1],[3,6],[-1,-1],[-7,-10],[-1,8],[-3,-6],[-3,-4],[-7,2],[-6,-2],[6,4],[-2,-4],[8,-5],[4,-2],[-2,-6],[9,9],[-4,2],[4,9],[-3,-7],[-8,3],[6,-8],[3,7],[-10,-10],[3,-7],[-2,9],[2,-8],[-2,1],[8,7],[-1,-4],[5,-10],[4,-6],[-1,4],[-3,-9],[-10,1],[2,2],[-5,3],[4,-2],[9,-7],[-2,-10],[7,6],[6,8],[-4,5],[-2,-7],[-8,5],[-8,-2],[-9,-9],[-4,-3],[2,3],[-9,-3],[-2,1],[7,-1],[8,8],[2,-2],[1,-1],[-2,-5],[8,-2],[9,-9],[4,-4],[-6,8],[10,-10],[6,-3],[-3,9],[9,-10],[2,-3],[7,-1],[-2,4],[8,3],[-5,-10],[5,7],[8,-3],[-2,5],[5,4],[-7,-3],[-7,-8],[6,-5],[-2,-4],[-10,5],[1,-6],[-3,6],[6,9],[2,-4],[-8,6],[-2,7],[-7,3],[3,7],[5,6],[6,-5],[-9,-8],[6,-2],[6,10],[-10,-4],[-9,-6],[2,-8],[-1,-7],[6,9],[-6,-8],[1,-9],[-9,-5],[-6,-8],[5,-9],[9,5],[2,5],[4,5],[1,4],[-3,-8],[-2,1],[-1,4],[3,4],[1,-4],[-3,-2],[4,-9],[-1,8],[-8,6],[9,-7],[-6,-10],[-4,-3],[-4,-9],[5,-6],[-1,6],[7,-5],[8,4],[-9,-2],[2,4],[-4,3],[3,7],[-3,8],[7,5],[-6,9],[-10,-5],[-6,3],[-7,-5],[3,3],[10,-5],[2,-9],[7,-2],[-4,9],[6,2],[1,9],[2,10],[-2,3],[-4,4],[-4,-6],[-7,-4],[-1,-5],[-8,-8],[-4,-6],[-3,-4],[-3,6],[5,-3],[5,10],[8,-2],[-10,6],[8,7],[-3,10],[1,-10],[1,2],[-7,7],[-6,3],[2,5],[-4,9],[4,-4],[1,2],[10,-6],[9,-8],[-5,-10],[3,-7],[9,-8],[2,5],[-5,3],[-4,8],[9,4],[-2,-8],[-9,-9],[10,-1],[7,-3],[9,3],[10,-10],[4,-8],[-1,-3],[-7,3],[-9,-10],[8,9],[-3,4],[-2,-7],[-4,-7],[-4,1],[5,2],[7,8],[8,5],[1,3],[6,-5],[-4,-1],[9,9],[10,3],[-6,-9],[-10,8],[-7,6],[-7,-2],[-6,-1],[9,-1],[7,6],[-1,-5],[3,3],[1,1],[-6,-5],[-6,6],[-6,-2],[-9,5],[-6,3],[9,-6],[2,-4],[-1,-10],[-4,10],[2,1],[2,-4],[8,-9],[2,2],[10,2],[9,4],[2,9],[-8,5],[-6,9],[2,1],[5,-6],[1,-8],[8,-4],[7,9],[3,7],[-6,1],[-1,-1],[4,-4],[-1,-5],[8,5],[3,-3],[9,-2],[-9,-2],[-1,10],[-5,-6],[-3,9],[-1,-6],[10,-5],[3,3],[-1,2],[4,-8],[9,9],[-8,-5],[5,5],[-2,5],[6,-5],[1,9],[-5,-3],[-7,5],[10,1],[1,9]], dtype = "uint64")#candidate|8700|(330, 2)|const|uint64
var_8701 = relay.var("var_8701", dtype = "float32", shape = (320,))#candidate|8701|(320,)|var|float32
call_8698 = relay.TupleGetItem(func_3591_call(relay.reshape(var_8699.astype('float64'), []), relay.reshape(call_8690.astype('int16'), [105, 3]), relay.reshape(const_8700.astype('uint64'), [660,]), relay.reshape(var_8701.astype('float32'), [80, 4]), ), 0)
call_8702 = relay.TupleGetItem(func_3597_call(relay.reshape(var_8699.astype('float64'), []), relay.reshape(call_8690.astype('int16'), [105, 3]), relay.reshape(const_8700.astype('uint64'), [660,]), relay.reshape(var_8701.astype('float32'), [80, 4]), ), 0)
output = relay.Tuple([call_8690,call_8692,const_8693,call_8695,var_8696,call_8698,var_8699,const_8700,var_8701,])
output2 = relay.Tuple([call_8691,call_8694,const_8693,call_8697,var_8696,call_8702,var_8699,const_8700,var_8701,])
func_8732 = relay.Function([var_8696,var_8699,var_8701,], output)
mod['func_8732'] = func_8732
mod = relay.transform.InferType()(mod)
var_8733 = relay.var("var_8733", dtype = "float32", shape = (2520,))#candidate|8733|(2520,)|var|float32
var_8734 = relay.var("var_8734", dtype = "float64", shape = ())#candidate|8734|()|var|float64
var_8735 = relay.var("var_8735", dtype = "float32", shape = (320,))#candidate|8735|(320,)|var|float32
output = func_8732(var_8733,var_8734,var_8735,)
func_8736 = relay.Function([var_8733,var_8734,var_8735,], output)
mutated_mod['func_8736'] = func_8736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8758 = relay.TupleGetItem(func_8014_call(), 0)
call_8759 = relay.TupleGetItem(func_8016_call(), 0)
func_3591_call = mod.get_global_var('func_3591')
func_3597_call = mutated_mod.get_global_var('func_3597')
const_8779 = relay.const(4.151529, dtype = "float64")#candidate|8779|()|const|float64
var_8780 = relay.var("var_8780", dtype = "int16", shape = (5, 63))#candidate|8780|(5, 63)|var|int16
const_8781 = relay.const([5,-6,6,6,-1,4,4,-10,2,-9,-2,5,6,2,-5,3,-2,6,4,9,-7,-7,-9,-9,-9,-5,1,4,2,-1,-8,4,-5,7,-2,-7,1,4,-3,2,-1,-4,-7,-2,-8,-5,-9,-8,1,8,-4,-4,10,-5,-1,4,-6,-6,9,-1,5,5,8,10,9,-5,-2,-7,7,5,1,-1,10,-9,9,7,-9,-8,4,-6,-8,5,10,-2,6,-6,-9,-5,6,9,7,9,-8,2,-7,-6,-9,-6,-5,-7,-8,-9,2,7,9,3,-3,1,-9,7,3,-2,-6,-3,-9,-3,5,-5,9,5,9,3,2,7,-9,9,10,6,2,-9,2,-1,6,-4,-9,3,8,-1,-2,-2,-5,-4,-4,8,-10,8,-1,-8,4,-1,2,-10,2,1,-2,-8,5,9,-2,7,6,-3,6,-3,3,3,10,6,-9,-7,-3,7,6,-9,-6,10,4,8,-7,10,7,-7,-1,10,-3,10,-1,-6,-4,5,1,-2,1,7,-3,1,-4,-8,1,-4,4,-10,2,1,-1,8,2,-1,9,4,-4,-3,-1,-3,8,1,-3,6,7,5,-2,3,10,10,9,3,-8,4,-7,6,-6,7,7,7,9,-3,-5,-8,8,6,1,-5,-8,-10,5,10,10,3,9,1,-3,8,1,-3,-3,8,-10,2,-1,-1,-8,-10,-8,-4,-2,-2,9,3,7,9,-6,-3,2,-2,-10,3,-6,4,5,-9,-3,4,-5,2,-6,2,-9,-8,-2,8,-5,-10,4,-5,4,-8,6,-10,2,3,-2,9,9,4,8,-5,-5,-4,-1,-9,-4,3,-10,3,3,-9,-8,-8,-4,10,6,-6,10,-7,-10,7,3,6,-3,7,-2,2,-7,-8,-3,-4,2,8,-10,5,3,-4,4,-2,-8,4,7,1,-6,-4,5,-6,8,3,10,7,-1,-10,2,1,-2,1,1,-5,1,4,9,-7,5,-4,7,10,6,-3,3,10,9,9,7,4,3,-8,-9,1,4,-1,-9,-10,-3,5,9,5,1,7,-6,-8,9,3,-10,4,-10,-6,5,5,-9,6,-8,-5,5,-8,2,-9,-9,-1,-7,-2,9,9,4,-6,6,2,-4,-4,-10,7,-8,5,1,6,-2,-6,-8,6,8,-6,5,10,-6,6,7,-8,-2,-2,-10,4,9,-2,6,9,-2,-10,-5,-6,-5,7,-8,8,-9,-4,3,2,9,-10,-5,-8,-6,-4,9,1,2,7,-6,-9,-9,5,-2,-3,2,3,4,4,2,-2,10,4,-3,2,-7,-6,8,6,10,-1,7,-10,7,-3,-4,7,-8,5,-3,-5,-10,7,-2,-7,4,-7,-2,-2,-10,8,-9,5,-8,-3,9,-1,6,-6,1,-3,1,-8,6,2,4,-10,-6,10,-7,-5,10,-5,4,-7,7,1,-9,-3,-8,10,6,5,-5,6,-10,8,8,6,-7,6,10,-3,6,-3,2,4,-1,10,8,10,10,7,3,8,6,-5,-1,5,-6,-2,2,-8,7,-3,-5,-2,-10,3,-2,-5,-6,5,1,-7,-10,7,4,-7,3,-5,-2,5,6,7,-10,-4,-3,4,-1,-10,9,-3,3,6,-9,-8,10,2,3,3,2,-8,8,-8,4,-8,-7,7,-10,-10,4,1,-3,-1,2,8,3,8,1,-8,4,-9,8,5,-9,-8,-2,8,-2,10,10,8,7,5,-2,2,-1,-8,-6,-9,-7,7,-10,5,-1,7], dtype = "uint64")#candidate|8781|(660,)|const|uint64
var_8782 = relay.var("var_8782", dtype = "float32", shape = (320,))#candidate|8782|(320,)|var|float32
call_8778 = relay.TupleGetItem(func_3591_call(relay.reshape(const_8779.astype('float64'), []), relay.reshape(var_8780.astype('int16'), [105, 3]), relay.reshape(const_8781.astype('uint64'), [660,]), relay.reshape(var_8782.astype('float32'), [80, 4]), ), 0)
call_8783 = relay.TupleGetItem(func_3597_call(relay.reshape(const_8779.astype('float64'), []), relay.reshape(var_8780.astype('int16'), [105, 3]), relay.reshape(const_8781.astype('uint64'), [660,]), relay.reshape(var_8782.astype('float32'), [80, 4]), ), 0)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
var_8847 = relay.var("var_8847", dtype = "float32", shape = (40,))#candidate|8847|(40,)|var|float32
call_8846 = relay.TupleGetItem(func_1886_call(relay.reshape(var_8847.astype('float32'), [10, 1, 4])), 0)
call_8848 = relay.TupleGetItem(func_1888_call(relay.reshape(var_8847.astype('float32'), [10, 1, 4])), 0)
func_6932_call = mod.get_global_var('func_6932')
func_6937_call = mutated_mod.get_global_var('func_6937')
var_8853 = relay.var("var_8853", dtype = "float32", shape = (1040,))#candidate|8853|(1040,)|var|float32
var_8854 = relay.var("var_8854", dtype = "float32", shape = (132,))#candidate|8854|(132,)|var|float32
const_8855 = relay.const([-6.381664,-7.194202,-5.393999,0.386942,-9.905385,-5.546141,-0.420415,-3.563594,3.266424,-8.605799,4.783959,-1.134151,-8.224344,-6.535179,-6.821350,4.349277,-4.286855,-7.186950,6.291711,-3.306672,1.421235,-0.448358,6.348908,9.572753,-4.212040,3.867302,-5.452006,-3.700377,8.139470,8.487040,3.787519,-4.476500,-2.562031,-0.730959,-5.916543,-7.811946,-1.755114,7.850294,5.663952,-2.420370,-2.984862,-1.946512,2.376676,3.578862,5.796245,-0.744360,6.433705,-7.097255,3.678455,9.263408,6.876535,2.316024,0.016083,2.232617,6.996139,-2.569173,5.369878,-6.676996,6.591190,1.042619,-0.487064,7.422223,-6.194626,-9.634462,5.184797,5.946556,0.828989,-2.260219,-1.780959,1.153216,5.591462,9.349743,-8.196820,4.074104,-8.914680,8.146541,-9.576856,-9.812117,-9.819259,-3.214752,5.377762,1.528383,-5.032719,7.000079,1.178565,-4.540142,-9.561448,-3.174716,8.904288,-2.250628,-6.587710,6.206137,8.174087,-3.879275,-9.935830,7.094649,-2.720814,-7.840271,-9.146799,1.854754,-2.869159,-9.344800,-9.476555,-3.240891,-2.409053,5.051991,-4.232386,2.844558,-1.936979,9.606988,-5.833712,-2.375354,7.882807,3.607450,-6.501137,-8.511527,-0.483071,2.268887,1.304399,-9.096657,1.594160,-4.797280,-2.480739,7.992119,4.116145,9.263786,0.542880,7.567557,-6.926114,-2.532266,5.024487,-0.738799,3.043363,-2.040271,6.939829,-0.190773,-6.473080,-1.175794,-6.608098,-6.746452,-5.595936,3.643120,3.257464,3.766917,6.850631,1.329370,-4.587521,-6.918482,1.594327,-0.913124,4.314488,6.834473,6.555504,4.980290,0.823102,-4.219051,3.650333,9.675446,-2.110181,8.451513,-8.206501,-7.330549,-9.092166,-6.359071,-4.633257,-6.531585,4.632687,8.970670,2.432449,-7.995934,-5.793938,-3.780738,-4.927933,6.951454,-6.051148,-1.318658,0.992102,1.414579,7.132440,7.874344,-9.363987,-7.718484,-1.603202,5.861567,-4.137432,-9.614956,-2.814476,-0.475746,8.809833,3.641237,-1.130864,-8.719478,-0.122463,0.956508,-3.571537,1.196837,-7.128014,-0.280477,-5.010697,-2.218715,-1.176291,0.300649,-3.630216,7.899708,6.475563,3.604856,8.477684,0.413535,-0.631786,3.657210,-7.630872,5.154524,-4.578185,9.239383,1.931872,4.471732,-4.899791,-4.358828,5.600820,-3.809644,-9.062855,-9.847976,-4.343325,-7.847867,2.237291,3.436461,-4.331667,-7.131018,-8.303004,2.615783,-0.249764,7.792783,-9.432979,1.812680,-5.450568,-8.879805,1.783313,-4.197765,4.740445,-8.489833,-3.440446,-6.755969,5.032483,-1.321756,-8.041799,9.898123,-4.568429,9.012070,7.890848,-2.619274,4.979920,-0.598258,-7.342123,-3.907478,7.864352,-9.628310,-8.969902,7.616494,7.646423,6.279250,7.092291,-3.233193,-9.346565,-1.442102,-3.210913,7.231535,-8.877838,1.173650,-0.483238,-8.320663,-5.397315,7.578526,7.191558,-1.420260,-3.740170,-1.566286,0.519433,-0.280233,-2.183710,3.406653,6.219426,-0.421119,-5.641289,-5.176306,5.116577,6.158748,4.603659,-6.857445,5.712094,-2.921417,3.826195,9.495865,2.714628,-5.136499,3.892549,3.377820,-3.450875,-0.615665,7.877496,4.840940,3.029254,-7.381884,4.429333,2.242596,-5.451492,2.914834,-7.117032,-5.432296,-3.521767,3.868384,-7.302770,-5.345556,6.726208,1.152334,-4.186373,8.084394,7.908749,-3.587897,5.199797,6.640061,3.499003,9.836512,-1.143102,-3.223447,-5.592965,-5.770287,-1.250765,9.094310,0.772079,-9.856474,8.117777,5.908713,5.128162,2.832046,4.535143,-2.106436,6.737328,-1.024124,5.328768,-0.692083,-2.237459,-8.720602,-2.190549,-0.037499,2.033069,0.271643,4.415560,4.051017,-4.183342,5.653986,-7.137057,2.545140,4.249170,8.714008,-2.683863,-8.044724,-9.509981,5.329698,-8.630241,-9.291073,-4.598050,-3.338355,-1.443071,-1.002417,-7.845559,-0.943973,-2.426105,2.745259,4.973232,-3.857295,-1.196171,-7.097399,-1.145503,1.653060,-6.738750,-2.576656,9.350319,-5.269040,-7.375382,0.093300,-6.191806,2.817050,9.653837,-3.015940,1.098053,-0.169393,9.340525,-4.434258,-7.039757,-1.973774,0.227720,8.129723,5.266401,-3.439352,-8.674456,-5.396668,5.724153,0.761416,-4.287949,0.669225,1.851198,-4.767274,5.811537,-1.275846,-7.677154,-0.930844,6.617718,2.962741,5.131096,-7.420872,9.260909,-6.157223,6.264552,7.590213,0.673456,2.764820,-5.718999,8.907434,3.606472,5.317453,-1.456025,0.298383,5.462204,-6.240618,4.357218,-2.724414,2.429279,9.842519,3.035193,5.650874,-0.353031,3.142394,-5.623949,-3.108597,-4.453318,7.588210,7.079466,-9.335365,2.810014,5.618940,5.900368,7.147679,-5.759655,7.306151,5.895403,-1.221203,-3.645055,-1.925076,-5.732923,-0.623057,-5.693138,2.575179,-4.039055,-9.903187,-4.038560,-9.822310,-6.074243,-5.987769,0.942645,-7.801759,-9.461086,-7.591269,-2.200127,9.560531,1.380618,1.927044,-6.504483,3.077719,-8.606427,-2.789807,1.856306,-7.609826,9.841075,-1.930185,4.852995,0.348329,0.039935,-3.833675,5.248241,-4.199686,2.115931,-7.886479,-9.923311,-2.577529,-2.277207,0.046319,-7.315474,7.148452,-5.512589,-3.225247,-5.073977,-8.651619,8.338915,8.456502,-6.004322,3.699847,6.984554,3.898499,7.794771,-0.122428,5.490727,8.232217,6.096369,0.644703,-0.975627,8.595282,9.582453,-3.747071,-2.593303,2.497101,3.216878,-0.198264,3.568208,-8.483056,-6.248951,-9.270887,-0.720267,0.693017,-0.571911,2.797463,-6.264544,2.506293,-7.216690,-8.193934,3.113319,-2.435822,-6.972691,2.685176,-7.040259,-5.498239,-8.016855,-6.129180,-0.608366,-2.665169,-5.961378,9.008428,3.938593,2.300891,-4.292052,-6.472420,9.874229,-7.714195,-3.906715,8.834314,7.112132,2.725287,-8.867177,-9.179455,5.698953,0.286682,-1.484754,-3.832063,4.203813,-9.856507,0.692290,7.604774,2.587044,-3.787675,4.395333,-6.446250,7.926855,-7.872667,-8.455716,-9.846133,-3.412806,2.963059,-4.617151,-4.539286,5.518723,0.183012,2.689415,-2.372732,-0.076352,-8.493942,-7.527949,-0.666087,-4.676379,-0.774017,1.925284,-9.004186,-2.422409,-7.744572,3.958410,3.300536,6.601976,1.623585,8.625271,3.479950,-8.020106,-3.286742,2.618628,-7.516562,0.393004,-7.282181,5.791770,-9.361566,-6.042510,-4.467729,1.919151,1.356476,-3.679820,-0.657012,-0.922462,2.465407,6.521228,5.681560,-8.264456,9.249082,-7.983540,-0.939088,-2.722004,-4.836281,-1.013763,1.966364,-8.648922,-3.292381,1.174354,-4.594870,0.689249,9.925617,3.904948,5.956312,-0.765031,-4.476592,-1.754322,1.677204,8.099219,4.738203,-7.742036,-5.747143,4.817753,-6.381039,5.680188,-4.488817,-2.251470,6.194267,6.403435,-1.672153,9.892340,-6.755022,5.306467,7.189874,5.139310,-5.891885,7.478921,-6.690205,-7.206261,4.802636,-7.084692,-8.317417,2.073418,-0.177872,-0.135808,4.109262,8.848661,7.973096,3.040691,-2.853099,4.823041,-2.949542,0.303241,-3.532025,7.250369,4.138510,7.984219,7.704122,4.687993,6.255460,-6.639665,-9.634835,0.662191,-8.408395,-5.596496,6.162590,-0.857780,-8.128094,9.285135,2.703722,-1.549519,-8.684937,-3.744968,1.024252,3.690141,9.477649,1.240748,-1.466164,5.008387,6.757626,1.713122,1.058671,-4.776986,7.264489,-6.337101,1.876182,8.451934,9.621262,1.623502,6.356652,9.350681,-8.858771,-5.263589,5.206204,2.314043,9.768011,-1.639406,-4.666624,-2.126425,-8.732033,-6.766285,-7.316843,0.376492,3.877365,-8.266918,2.199537,2.849757,-4.538737,-7.847573,0.586331,-6.154898,-0.459328,-8.900088,3.150311,-4.155134,5.509675,2.040133,-5.085268,5.626595,6.397378,8.444466,-9.415504,-9.925362,-3.214773,-6.728168,0.018036,9.436625,1.556469,-5.637694,-0.506313,-7.067702,-0.363511,8.119247,-4.723010,-9.713896,-1.395612,8.694515,0.621760,0.116858,-9.860952,5.211286,-4.025165,-9.762397,-2.936020,3.813144,3.105863,9.915392,0.734222,9.028596,1.300720,-2.583441,9.348619,-9.796264,1.625079,-3.098206,-7.893266,3.605102,-2.316256,-4.074113,7.518452,-6.224728,-7.562498,-4.543916,-3.192339,2.389856,6.582729,-4.188265,8.450532,3.130338,-3.238504,7.295820,-3.558437,-1.953809,-4.245543,2.651724,-0.326345,-3.099099,1.482053,-8.571412,-9.167585,-2.844806,9.958066,-0.464943,5.351054,-3.513600,-0.846168,-8.288556,-5.869087,5.171431,-7.232639,-2.616245,-0.151677,2.309151,9.598189,-9.277069,2.712687,-9.928208,5.740612,-7.560539,-3.666452,-5.688045,-9.746300,6.937307,4.463234,3.142275,-4.814994,-7.936968,-8.529964,-4.619254,-6.363994,-0.641935,2.446832,-5.798737,0.852953,-2.657655,9.467683,-5.723067,9.629955,3.596664,3.274659,-5.242604,-2.315428,-6.178568,-6.372860,1.018781,1.987191,5.647028,-7.721814,9.999466,-1.918936,6.657745,0.027539,1.140484,-9.090017,6.826700,6.387045,3.902806,7.060672,-6.335884,-9.703599,-3.642140,9.464596,1.330678,1.018841,-2.911410,-9.647524,-2.169678,6.848821,-6.238128,-9.497881,0.626739,-0.048166,8.221554,3.735339,3.484642,3.653521,2.032428,5.873845,-9.048079,-6.264168,-1.242857,8.197104,-1.505272,-0.402483,-8.075707,-0.427165,-4.578114,-1.315919,-7.389198,-5.242097,6.194209,5.615126,-6.126696,7.376627,-5.652559,0.973130,-8.028889,8.153425,-0.786882,-3.235755,-2.570345,-1.334952,4.211273,-7.995604,-6.351460,2.761261,5.038565,5.980632,-8.491578,-5.768841,-3.262415,5.579098,-8.478292,7.797295,5.097409,3.283093,-2.011876,-2.536183,-2.004359,-8.171669,3.790075,1.134184,-1.918474,6.094923,4.447451,2.538859,4.508967,4.395762,2.505673,-9.928039,-4.501186,-4.127284,-3.860261,-2.945524,-2.851571,0.281162,-8.533355,-4.547813,1.998258,3.099221,2.219952,-4.786250,-8.059700,6.594190,-9.750992,-3.577617,3.911627,-3.540405,4.373219,3.499640,8.219195,-0.152743,4.555257,-4.454327,-8.490923,8.999852,6.536650,-1.905598,7.144079,7.441075,-6.985016,-0.917932,1.983922,8.791964,8.157731,-5.069600,3.018137,7.183888,4.057654,-7.842740,5.322346,5.737696,8.813508,-0.777940,9.807377,0.460388,1.726613,-6.740425,-0.606046,-3.546192,-0.807440,-1.113628,9.610280,-1.833431,9.702015,-6.551421,-8.054612,7.423494,7.533916,1.535614,-9.890034,-7.878621,-4.399377,-3.956629,-6.904223,1.754712,9.932146,7.336638,6.065118,7.764390,-3.775562,3.587224,9.065174,-7.463609,5.182380,-8.407245,-1.841181,1.653869,7.902502,8.320620,-9.938368,-9.622690,-9.650844,-4.892719,0.118523,0.604792,6.282083,-7.388781,2.129256,-2.274886,-3.703561,-3.416194,5.877959,-2.666799,7.163659,7.926580,-1.872808,1.152405,8.908201,-3.269500,9.451571,-9.652985,-2.783124,-2.728957,7.806694,-1.588422,3.826611,1.377315,6.558692,0.254677,4.955841,-4.967976,-2.286326,0.774020,-8.918587,-0.487507,3.329511,-3.731746,7.749607,2.394101,9.050707,8.788790,6.758169,-4.213555,-9.988671,7.732940,-4.853119,3.853196,-0.619233,-7.679170,-6.542141,-1.055087,0.378507,3.170339,2.403107,7.474879,8.693115,7.159638,9.274137,0.761419,5.339809,-3.851841,-9.428466,-3.355031,-2.899179,2.570256,0.369101,-0.109713,6.852040,-2.734362,-5.057381,0.676845,-7.218610,-8.469132,-2.213980,9.430755,4.453273,1.570325,8.553746,-8.933332,-2.216606,-6.219311,0.736113,-4.063840,-4.454484,-1.687570,9.180377,-2.074954,-7.677639,7.689277,-7.527020,4.905425,-4.154760,-7.560263,-3.518716,5.392497,-7.157028,1.872943,-4.494850,-1.992699,-1.607066,-6.654840,8.733548,2.726008,5.695192,-3.041092,3.921715,9.172314,8.463680,8.346299,-8.208383,-3.220929,-3.799522,4.296899,-6.181856,0.966490,-3.793982,-0.609979,1.995385,1.929904,-7.792132,-7.800514,7.892958,-0.752544,9.713971,9.591198,-7.776558,7.851357,7.019341,-3.085380,-6.888913,-3.161927,3.074089,-9.242058,-7.552840,9.490205,-3.681686,-7.470974,-0.344487,-1.804642,-6.796072,8.107349,2.255435,6.728457,7.258769,-4.385695,8.977593,-7.547922,4.494668,6.395349,5.247592,1.097252,2.311157,1.988583,-7.496444,7.879862,1.466843,3.886757,7.247983,4.866812,-4.850464,4.934882,-6.784497,-4.013772,-3.583315,9.634349,5.328611,9.335085,-7.192174,-3.908028,-1.257534,3.086803,-3.603429,1.391803,1.424882,5.435808,-8.726434,-6.563970,-3.425682,0.294067,-0.524011,-6.926251,5.877729,-0.609553,5.010943,-1.564262,0.201567,0.637596,-9.214113,5.004292,-3.884938,-0.615923,7.373461,8.683950,0.144329,3.414829,-1.721151,2.999067,4.121012,8.924945,-1.719174,5.473875,-0.317494,-8.836042,5.094538,-0.922113,-2.796241,-5.100072,0.848624,9.619893,-7.837247,5.258844,2.499822,-8.783075,-0.831282,8.327160,5.466619,-3.886443,0.659525,7.771309,8.120702,-7.761196,-5.941411,7.412726,1.255168,-9.809082,2.130927,-1.598082,6.224940,-6.476249,-0.526571,-3.155312,-6.444964,9.996574,1.763987,-4.106101,6.928663,-8.437047,4.438991,5.807573,9.581633,6.296036,6.022385,3.849078,-7.815509,6.819086,9.531107,0.351304,-0.367159,8.138684,8.281388,-8.323502,8.168670,-1.415669,7.030660,2.267530,1.951684,8.135987,-5.941776,0.663324,-0.902379,8.943092,9.151737,6.394422,-2.409543,9.641596,-3.150190,-6.477166,5.824970,7.096643,-3.198263,5.496136,8.175504,1.606931,1.958548,-0.016212,9.473266,0.064894,-8.507521,-7.441130,8.249397,-8.955683,-1.253633,9.756230,7.936461,-3.653421,3.719926,-4.634450,-1.342776,-6.965441,-9.413657,-3.820611,4.636654,-6.515802,-5.389469,-8.506739,2.960783,-4.786643,9.963153,3.704015,-2.787010,-5.034445,8.318106,-8.327363,-7.855425,9.349684,3.115772,-0.710566,4.975287,6.260712,-3.093488,7.703227,-2.835996,4.421892,-0.273664,0.970829,-5.821160,-8.098667,-6.304909,9.557956,-8.576138,8.590067,-5.384301,-6.655043,6.842392,-7.030313,4.335588,2.644118,6.436648,7.430338,6.707453,-3.324911,-5.135771,8.237256,1.318763,-4.194609,4.287332,5.146482,9.253913,7.580859,0.758524,-6.614187,9.521280,3.280534,-5.358180,-3.790035,6.511047,5.449616,-5.718027,-9.306161,-4.012685,0.937469,-6.042850,8.782849,-5.090829,-0.602436,-0.010166,-4.577569,-9.732114,-6.570962,-5.819968,-8.917518,4.097025,0.602163,-7.394101,5.094627,-0.975651,-1.644874,-6.346636,7.973218,-6.000799,-4.962615,-4.385896,2.883043,-4.133128,-5.867285,-0.955120,-3.670978,-6.648609,6.867303,0.329461,0.213449,9.933909,4.386055,-1.051724,-1.510011,-0.438340,5.931112,2.303467,-3.343275,0.634786,-1.489134,7.600997,2.009630,8.322187,1.109431,-5.504229,-0.369562,-5.612145,9.977854,-9.532599,-6.289029,-5.292132,-2.962010,-8.540277,-6.137051,9.472989,3.783053,6.638874,-7.559530,-2.768359,-4.834128,0.802075,-5.242577,-2.131643,-2.738985,-5.202420,3.524548,-3.309563,-2.020049,-0.721175,-4.286283,-3.865356,8.182633,4.748234,-8.742403,6.748845,-8.378271,1.905594,-5.146956,-7.524839,5.235631,4.991186,6.695730,-1.728286,-4.031341,-6.800031,-4.957984,1.972360,4.698044,3.857642,-6.667194,-9.847913,1.029643,8.305133,6.980128,-4.408762,-5.240685,6.345571,-7.605656,-9.867306,2.918319,9.372368,5.855060,0.834028,1.302791,-0.030958,3.624514,-2.064852,-2.613356,-1.075809,5.228580,-9.607840,3.065120,-2.305794,9.564955,-0.316180,4.926710,-3.340583,-5.816222,6.127896,2.950472,3.560776,-8.575681,2.004351,-0.387735,-5.776655,9.212819,9.027075,6.669222,-9.298326,-7.910205,1.178987,-5.685522,-9.796779,1.764227,9.247082,3.115380,8.434823,-0.327081,2.509084,-4.909211,6.150547,-5.284555,-3.211413,-6.443105,0.097257,-3.631709,-6.580684,-3.628276,6.528763,3.637905,-3.681332,-4.715864,-0.707050,3.205715,4.923599,-2.517811,2.503947,1.903731,-2.387703,-9.219483,2.493758,-3.100300,6.593321,-0.647370,-5.096476,9.764385,5.237151,-7.315862,4.367564,4.476819,4.009310,0.451283,-4.748335,7.335859,-2.813483,-2.692730,-8.045127,1.932510,-4.552856,-2.320968,2.644239,0.379450,2.691122,4.865659,3.094644,0.981191,-9.304083,2.780379,-8.032036,0.903658,-6.048945,-2.264415,-0.028465,6.210364,8.238284,7.917266,7.284636,5.866250,-7.310147,8.743132,8.448808,-4.443429,1.178863,0.796530,-5.180755,-9.704869,-5.090730,1.586682,0.701907,6.401308,5.648149,1.690274,-9.532343,5.763503,9.138693,-9.617603,-6.167573,-8.070860,6.437447,5.169577,-2.957684,-7.960285,-0.108648,0.066943,-4.658735,-5.569975,2.994053,1.105514,8.392513,-4.841547,8.534840,6.454654,-6.838301,-7.520430,1.911295,8.277312,0.772745,4.309467,-5.665472,5.191508,0.862334,-3.600146,-9.510247,-7.710716,-4.101330,-4.089331,-4.533529,5.424029,-2.353048,-5.325525], dtype = "float32")#candidate|8855|(1600,)|const|float32
call_8852 = relay.TupleGetItem(func_6932_call(relay.reshape(var_8853.astype('float32'), [10, 8, 13]), relay.reshape(var_8854.astype('float32'), [132, 1]), relay.reshape(const_8781.astype('uint64'), [660,]), relay.reshape(const_8855.astype('float32'), [5, 320]), ), 0)
call_8856 = relay.TupleGetItem(func_6937_call(relay.reshape(var_8853.astype('float32'), [10, 8, 13]), relay.reshape(var_8854.astype('float32'), [132, 1]), relay.reshape(const_8781.astype('uint64'), [660,]), relay.reshape(const_8855.astype('float32'), [5, 320]), ), 0)
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
var_8860 = relay.var("var_8860", dtype = "float64", shape = (392,))#candidate|8860|(392,)|var|float64
call_8859 = func_8298_call(relay.reshape(var_8860.astype('float64'), [4, 14, 7]))
call_8861 = func_8298_call(relay.reshape(var_8860.astype('float64'), [4, 14, 7]))
func_8644_call = mod.get_global_var('func_8644')
func_8645_call = mutated_mod.get_global_var('func_8645')
call_8862 = func_8644_call()
call_8863 = func_8644_call()
func_3419_call = mod.get_global_var('func_3419')
func_3423_call = mutated_mod.get_global_var('func_3423')
var_8870 = relay.var("var_8870", dtype = "float64", shape = (14,))#candidate|8870|(14,)|var|float64
call_8869 = relay.TupleGetItem(func_3419_call(relay.reshape(var_8870.astype('float64'), [7, 2, 1]), relay.reshape(var_8782.astype('float32'), [320,]), ), 1)
call_8871 = relay.TupleGetItem(func_3423_call(relay.reshape(var_8870.astype('float64'), [7, 2, 1]), relay.reshape(var_8782.astype('float32'), [320,]), ), 1)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
call_8875 = relay.TupleGetItem(func_1319_call(relay.reshape(call_8778.astype('float32'), [16, 4, 5])), 0)
call_8876 = relay.TupleGetItem(func_1322_call(relay.reshape(call_8778.astype('float32'), [16, 4, 5])), 0)
output = relay.Tuple([call_8758,call_8778,const_8779,var_8780,const_8781,var_8782,call_8846,var_8847,call_8852,var_8853,var_8854,const_8855,call_8859,var_8860,call_8862,call_8869,var_8870,call_8875,])
output2 = relay.Tuple([call_8759,call_8783,const_8779,var_8780,const_8781,var_8782,call_8848,var_8847,call_8856,var_8853,var_8854,const_8855,call_8861,var_8860,call_8863,call_8871,var_8870,call_8876,])
func_8887 = relay.Function([var_8780,var_8782,var_8847,var_8853,var_8854,var_8860,var_8870,], output)
mod['func_8887'] = func_8887
mod = relay.transform.InferType()(mod)
var_8888 = relay.var("var_8888", dtype = "int16", shape = (5, 63))#candidate|8888|(5, 63)|var|int16
var_8889 = relay.var("var_8889", dtype = "float32", shape = (320,))#candidate|8889|(320,)|var|float32
var_8890 = relay.var("var_8890", dtype = "float32", shape = (40,))#candidate|8890|(40,)|var|float32
var_8891 = relay.var("var_8891", dtype = "float32", shape = (1040,))#candidate|8891|(1040,)|var|float32
var_8892 = relay.var("var_8892", dtype = "float32", shape = (132,))#candidate|8892|(132,)|var|float32
var_8893 = relay.var("var_8893", dtype = "float64", shape = (392,))#candidate|8893|(392,)|var|float64
var_8894 = relay.var("var_8894", dtype = "float64", shape = (14,))#candidate|8894|(14,)|var|float64
output = func_8887(var_8888,var_8889,var_8890,var_8891,var_8892,var_8893,var_8894,)
func_8895 = relay.Function([var_8888,var_8889,var_8890,var_8891,var_8892,var_8893,var_8894,], output)
mutated_mod['func_8895'] = func_8895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_8956 = relay.TupleGetItem(func_8318_call(), 0)
call_8957 = relay.TupleGetItem(func_8319_call(), 0)
output = relay.Tuple([call_8956,])
output2 = relay.Tuple([call_8957,])
func_8959 = relay.Function([], output)
mod['func_8959'] = func_8959
mod = relay.transform.InferType()(mod)
mutated_mod['func_8959'] = func_8959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8959_call = mutated_mod.get_global_var('func_8959')
call_8960 = func_8959_call()
output = call_8960
func_8961 = relay.Function([], output)
mutated_mod['func_8961'] = func_8961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_8997 = relay.TupleGetItem(func_8014_call(), 0)
call_8998 = relay.TupleGetItem(func_8016_call(), 0)
output = relay.Tuple([call_8997,])
output2 = relay.Tuple([call_8998,])
func_9004 = relay.Function([], output)
mod['func_9004'] = func_9004
mod = relay.transform.InferType()(mod)
output = func_9004()
func_9005 = relay.Function([], output)
mutated_mod['func_9005'] = func_9005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8161_call = mod.get_global_var('func_8161')
func_8162_call = mutated_mod.get_global_var('func_8162')
call_9008 = relay.TupleGetItem(func_8161_call(), 0)
call_9009 = relay.TupleGetItem(func_8162_call(), 0)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_9011 = relay.const([2.872597,-9.549881,1.602767,-9.373705,5.483486,0.549722,-9.508173,5.118886,-4.517509,-9.487189,6.434028,-6.721049,-9.507858,4.338144,7.856005,9.621385,8.684572,-9.601717,-5.343758,3.795912,-9.326877,9.583174,-4.131563,0.920711,-5.832982,-0.204058,7.095039,-5.938040,7.794200,2.499611,-0.925022,0.495921,0.762438,2.541629,-0.016251,9.385084,2.287229,-9.362244,-3.728997,-8.314077,3.189074,-5.803772,-9.369578,-4.061305,-5.099774,-0.288762,-6.072305,-7.878004,9.314272,-2.832933,-9.489218,-5.179040,-0.554464,-5.282933,6.663052,2.292126,2.454787,0.367723,8.091623,8.704261,-7.297152,-4.743951,-3.834112,-4.664303,-1.243210,0.762517,-5.969788,7.506619,-7.644091,9.174709,-9.606063,1.311879,-6.528878,8.304686,-9.029864,-5.774498,-8.842326,-5.610030,9.611790,5.232463,7.452789,4.081060,-1.113987,-1.396591,-7.739148,-1.806775,3.640954,-1.493674,7.804731,7.607304,1.638875,-2.772968,-3.742366,-5.985061,3.008910,-4.206051,-5.662838,-2.124120,-9.158250,-1.786079,7.505687,5.534488,-9.673846,-1.066665,-0.660519,3.925809,7.677197,0.090079,-1.286674,-1.402655,3.264090,-4.285089,-6.238296,6.309394,-8.254852,5.542161,-0.640067,-3.745838,-8.659612,-0.967401,-6.820386,-5.558400,1.697767,5.951654,1.237864,0.382716,-7.780831,8.292833,5.390913,1.468178,-6.621504,7.320819,-8.732512,3.478530,-6.244757,1.523589,7.334205,2.385595,0.734396,3.510007,-6.371152,-8.495824,-1.858515,0.650063,-8.963553,4.161168,3.661877,9.548230,-3.277009,-1.931248,0.838402,0.261463,-3.776174,7.792715,-2.896567,-8.847641,-4.558135,5.577182,-4.628819,-5.516895,-6.284410,6.662404,-7.430405,0.324279,1.727189,1.930141,4.123260,-0.437396,1.085355,7.385833,-1.767400,-8.684485,-9.322714,2.818156,-8.808323,9.083304,-6.294220,-4.956037,-1.889759,6.416663,-4.684190,-7.177492,-3.757696,0.282668,-9.135121,2.960586,-2.367568,0.289803,9.688580,-3.818445,-7.287946,-7.813744,-8.880798,9.715933,-5.650149,9.443932,-1.202076,-8.850585,-9.613352,-5.130989,9.055947,4.310511,-9.812204,-3.587018,8.461930,1.574087,4.095710,-5.262958,0.314791,-7.464525,1.641833,-2.857086,3.586641,-2.293618,-7.566505,-8.641731,-2.184586,5.982585,1.698081,-2.572217,-2.447897,-9.754154,-3.778069,-2.968077,4.798976,4.638903,-2.251938,-9.891903,7.064514,3.751152,2.734456,3.527344,4.789032,-5.498311,-0.985311,0.862852,0.889532,-7.535749,2.818777,1.004969,4.732131,8.900449,-8.598898,8.966851,-7.043502,3.004508,1.094868,2.724214,7.843177,8.321022,-7.673379,2.465426,-8.547722,7.846603,-8.021156,-6.308317,-1.239225,6.779565,7.319465,-7.707008,6.622929,-8.067752,-5.133847,6.289780,3.487412,2.413933,1.738151,9.013630,6.102917,6.607131,7.749078,3.766691,1.783707,-1.103833,-3.441607,-6.270369,-2.385640,-2.497172,-5.398745,5.105831,-8.246602,-4.043365,5.078208,7.226131,-7.158682,-4.093279,4.592377,7.977079,-6.078500,8.545405,-6.638318,-6.336953,-8.781662,1.417674,-0.519863,0.968801,-2.469163,-7.826016,0.378800,-1.078356,9.348039,-4.416848,-3.691086,0.851482,3.372630,7.552199,3.944057,0.954331,-4.991965,-9.399465,3.719436,4.448317,0.005927,0.276209,-6.377935,3.494199,-8.519960,-0.707724,6.834310,7.844844], dtype = "float32")#candidate|9011|(320,)|const|float32
call_9010 = relay.TupleGetItem(func_1319_call(relay.reshape(const_9011.astype('float32'), [16, 4, 5])), 0)
call_9012 = relay.TupleGetItem(func_1322_call(relay.reshape(const_9011.astype('float32'), [16, 4, 5])), 0)
output = relay.Tuple([call_9008,call_9010,const_9011,])
output2 = relay.Tuple([call_9009,call_9012,const_9011,])
func_9014 = relay.Function([], output)
mod['func_9014'] = func_9014
mod = relay.transform.InferType()(mod)
mutated_mod['func_9014'] = func_9014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9014_call = mutated_mod.get_global_var('func_9014')
call_9015 = func_9014_call()
output = call_9015
func_9016 = relay.Function([], output)
mutated_mod['func_9016'] = func_9016
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9095 = relay.var("var_9095", dtype = "float64", shape = ())#candidate|9095|()|var|float64
var_9096 = relay.var("var_9096", dtype = "float64", shape = (4, 12, 1))#candidate|9096|(4, 12, 1)|var|float64
bop_9097 = relay.floor_mod(var_9095.astype('float64'), var_9096.astype('float64')) # shape=(4, 12, 1)
bop_9101 = relay.less_equal(var_9095.astype('bool'), bop_9097.astype('bool')) # shape=(4, 12, 1)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_9105 = relay.TupleGetItem(func_8318_call(), 0)
call_9106 = relay.TupleGetItem(func_8319_call(), 0)
func_8036_call = mod.get_global_var('func_8036')
func_8038_call = mutated_mod.get_global_var('func_8038')
call_9108 = relay.TupleGetItem(func_8036_call(relay.reshape(call_9105.astype('int16'), [315,])), 1)
call_9109 = relay.TupleGetItem(func_8038_call(relay.reshape(call_9105.astype('int16'), [315,])), 1)
output = relay.Tuple([bop_9101,call_9105,call_9108,])
output2 = relay.Tuple([bop_9101,call_9106,call_9109,])
func_9121 = relay.Function([var_9095,var_9096,], output)
mod['func_9121'] = func_9121
mod = relay.transform.InferType()(mod)
mutated_mod['func_9121'] = func_9121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9121_call = mutated_mod.get_global_var('func_9121')
var_9123 = relay.var("var_9123", dtype = "float64", shape = ())#candidate|9123|()|var|float64
var_9124 = relay.var("var_9124", dtype = "float64", shape = (4, 12, 1))#candidate|9124|(4, 12, 1)|var|float64
call_9122 = func_9121_call(var_9123,var_9124,)
output = call_9122
func_9125 = relay.Function([var_9123,var_9124,], output)
mutated_mod['func_9125'] = func_9125
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8088_call = mod.get_global_var('func_8088')
func_8089_call = mutated_mod.get_global_var('func_8089')
call_9374 = relay.TupleGetItem(func_8088_call(), 1)
call_9375 = relay.TupleGetItem(func_8089_call(), 1)
func_1524_call = mod.get_global_var('func_1524')
func_1528_call = mutated_mod.get_global_var('func_1528')
var_9379 = relay.var("var_9379", dtype = "uint64", shape = (110, 6))#candidate|9379|(110, 6)|var|uint64
call_9378 = relay.TupleGetItem(func_1524_call(relay.reshape(var_9379.astype('uint64'), [5, 12, 11]), relay.reshape(var_9379.astype('uint64'), [5, 12, 11]), relay.reshape(call_9374.astype('float32'), [1, 320]), ), 3)
call_9380 = relay.TupleGetItem(func_1528_call(relay.reshape(var_9379.astype('uint64'), [5, 12, 11]), relay.reshape(var_9379.astype('uint64'), [5, 12, 11]), relay.reshape(call_9374.astype('float32'), [1, 320]), ), 3)
output = relay.Tuple([call_9374,call_9378,var_9379,])
output2 = relay.Tuple([call_9375,call_9380,var_9379,])
func_9383 = relay.Function([var_9379,], output)
mod['func_9383'] = func_9383
mod = relay.transform.InferType()(mod)
mutated_mod['func_9383'] = func_9383
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9384 = relay.var("var_9384", dtype = "uint64", shape = (110, 6))#candidate|9384|(110, 6)|var|uint64
func_9383_call = mutated_mod.get_global_var('func_9383')
call_9385 = func_9383_call(var_9384)
output = call_9385
func_9386 = relay.Function([var_9384], output)
mutated_mod['func_9386'] = func_9386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8161_call = mod.get_global_var('func_8161')
func_8162_call = mutated_mod.get_global_var('func_8162')
call_9471 = relay.TupleGetItem(func_8161_call(), 1)
call_9472 = relay.TupleGetItem(func_8162_call(), 1)
func_1426_call = mod.get_global_var('func_1426')
func_1429_call = mutated_mod.get_global_var('func_1429')
var_9474 = relay.var("var_9474", dtype = "float32", shape = (210,))#candidate|9474|(210,)|var|float32
call_9473 = relay.TupleGetItem(func_1426_call(relay.reshape(var_9474.astype('float32'), [6, 5, 7])), 0)
call_9475 = relay.TupleGetItem(func_1429_call(relay.reshape(var_9474.astype('float32'), [6, 5, 7])), 0)
func_9121_call = mod.get_global_var('func_9121')
func_9125_call = mutated_mod.get_global_var('func_9125')
var_9491 = relay.var("var_9491", dtype = "float64", shape = ())#candidate|9491|()|var|float64
const_9492 = relay.const([[-7.011298],[5.116613],[7.239257],[-1.449459],[8.793366],[-4.997935],[9.356274],[-4.730671],[8.573294],[-3.131078],[-1.793819],[9.942463],[-5.693182],[0.461043],[9.185327],[-6.329239],[4.228567],[-7.199537],[4.015418],[-3.083344],[8.691190],[5.477438],[2.738306],[4.618242],[6.645256],[-5.135893],[-3.713709],[-3.385067],[-2.839884],[1.734569],[3.528476],[3.590179],[-3.160201],[9.794486],[-5.048749],[-1.933677],[-5.378804],[-4.434785],[5.408292],[6.857682],[3.360081],[-8.658357],[3.302648],[1.663911],[0.991221],[3.476318],[-4.963140],[0.311826]], dtype = "float64")#candidate|9492|(48, 1)|const|float64
call_9490 = relay.TupleGetItem(func_9121_call(relay.reshape(var_9491.astype('float64'), []), relay.reshape(const_9492.astype('float64'), [4, 12, 1]), ), 1)
call_9493 = relay.TupleGetItem(func_9125_call(relay.reshape(var_9491.astype('float64'), []), relay.reshape(const_9492.astype('float64'), [4, 12, 1]), ), 1)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_9498 = relay.const([-0.548263,-6.493523,-0.754035,-0.601167,-6.951012,-3.121738,-5.090386,0.809372,-9.730278,-6.979291,9.401107,-8.911639,-8.280116,0.518701,6.563338,-7.006094,1.521958,-8.245996,9.581090,-2.039800,3.793529,-2.460807,7.586135,5.727535,8.841938,-5.607237,-1.066930,-3.095954,6.660407,-9.679037,-9.515384,-1.627167,2.247607,7.491086,0.505708,-1.331324,-4.056049,8.712770,0.074306,1.871945,-8.000964,1.424852,2.859083,8.826568,7.301420,6.225394,-7.196564,1.191520,-1.030745,-0.820273,-2.844589,2.928254,6.865257,-9.382407,0.037514,0.156618,8.936422,-2.310455,3.077718,-1.941009,6.970159,-1.279789,1.376546,-3.089774,-5.992258,-1.976802,8.594250,2.632138,-0.184458,3.848651,4.034016,3.850022,2.359706,6.132686,1.932696,2.807518,7.588822,-4.530093,6.241708,2.423197,5.489389,-9.478541,5.572125,3.398850,7.502455,0.527841,-7.262340,-8.125420,-2.412059,-8.717952,6.232123,-3.924387,9.675830,8.919812,7.469592,-8.118946,-1.911107,-7.821113,-0.052484,7.726577,-6.651578,-1.307362,5.031770,5.748872,6.654230,8.304724,6.248559,0.530420,-7.104189,-3.046045,4.167752,-0.405492,0.480155,0.372328,1.237937,-6.837804,8.249548,-0.247891,5.053117,-2.761777,3.361625,6.995069,-3.204768,6.584678,6.281375,-2.024111,-5.221846,0.063917,6.883994,5.561150,7.909183,7.305434,-6.135074,-4.943381,0.933274,-6.105748,-2.337327,4.160950,8.339771,-5.274364,-8.071150,7.772092,2.178259,9.842285,-6.647440,5.496230,-5.003318,-0.487734,-2.024557,-3.717952,-6.859523,-5.321472,-5.299562,3.434416,-4.718983,-8.004765,-9.954055,6.202360,-8.286762,5.299178,9.469430,0.156779,8.925054,9.804710,-5.262059,2.494209,-3.701248,2.785849,9.945505,-3.001905,-4.788443,8.044648,6.734417,3.421072,7.000660,-3.516249,6.305120,-4.369913,5.926876,7.554809,7.219837,-2.132032,-6.273147,-6.018011,-7.376993,-3.754565,5.755682,-8.448182,-4.809951,4.168983,-5.183438,0.448420,2.440142,-3.186324,2.831069,-8.849599,-6.107134,-6.222008,-9.282535,-9.695598,-5.717546,-9.538803,-0.898279,-1.966712,-9.796471,-4.791876,2.106435,-0.554223,8.152307,0.745637,-8.510254,2.835038,1.899632,-9.491713,-3.004566,-2.816963,1.716116,8.590362,6.432176,-2.391001,3.937176,-8.751380,-5.997758,7.491738,1.030105,-1.398949,-7.235161,-1.525890,-8.248953,5.216797,-3.345397,2.071292,-5.085717,8.952193,-6.623798,5.506391,2.178584,-7.671850,8.485158,0.721420,-6.205020,-1.259890,-6.268172,-2.515223,2.676360,1.796590,-5.618850,3.986902,4.090569,-3.173458,1.346302,1.589511,-4.180819,-3.669880,3.930818,-7.463752,-3.902779,-0.203604,-8.672518,7.749102,9.041636,8.599742,4.445440,-0.685586,2.974650,-8.731255,7.394649,4.635233,7.260530,2.496863,-1.401765,-9.046163,-5.703002,7.968672,-4.923910,1.601578,5.616865,0.996669,8.744558,-9.712562,-0.499400,5.778030,-9.015912,7.759709,3.926635,0.963092,7.743076,-5.093015,-1.793138,-2.586999,-8.864719,-5.339657,-3.271042,-0.390137,-9.357578,-8.750429,7.378834,-9.436348,2.674191,2.876080,-7.099744,-6.303577,-0.491439,2.326602,-9.048474,8.521947,8.956844,-4.647938,8.045569,-8.458753,5.512768,6.096932,-4.651542,9.094716,7.830588,-3.087747,0.049106,0.347456,1.642241,-6.181212], dtype = "float32")#candidate|9498|(320,)|const|float32
call_9497 = relay.TupleGetItem(func_1319_call(relay.reshape(const_9498.astype('float32'), [16, 4, 5])), 0)
call_9499 = relay.TupleGetItem(func_1322_call(relay.reshape(const_9498.astype('float32'), [16, 4, 5])), 0)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
const_9505 = relay.const([True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True], dtype = "bool")#candidate|9505|(117,)|const|bool
var_9506 = relay.var("var_9506", dtype = "bool", shape = (702,))#candidate|9506|(702,)|var|bool
const_9507 = relay.const([-4.241456,1.481957,3.003509,-7.986440,4.074988,-5.625284,0.710935,-2.458998,-8.324912,-0.520331,-9.663225,-9.631386,6.218848,-3.511514,-7.049198,6.750180,6.313406,6.762863,4.290489,7.229383,5.381653,7.208047,-7.655142,-1.443965,-4.962103,-2.426870,-1.831408,-9.923503,-9.701547,-9.665164,-2.105191,-5.857744,2.629092,-5.090475,4.015449,5.693390,6.868840,3.822916,-1.677184,8.230299,-6.143970,2.373011,-9.302759,6.887863,-4.170447,8.931787,2.851611,3.531286,3.650883,-3.043036,2.538944,-2.905288,-2.961579,-4.385999,4.392247,5.559828,3.083827,-4.768424,7.920625,2.253904,-3.503292,-5.141450,-2.315606,-7.446987,-4.488431,-1.059048,-4.467599,-9.846424,-3.145942,7.033053,-6.931428,-2.867090,-8.283853,-4.703180,-4.896895,0.490599,-7.813629,-0.891337,7.851635,3.633232,6.002922,8.535574,-7.079262,2.874713,4.907760,-7.339469,4.729298,0.919734,-0.073208,9.742141,0.499697,7.306360,1.689688,-8.409058,-0.746773,-3.640198,0.742158,6.371505,3.975091,3.763540,2.116675,7.624905,-3.834130,-7.277531,-0.522225,7.643036,3.102842,6.017575,-3.506605,9.011245,6.091531,0.617630,-3.062684,-5.161692,3.875889,-7.027629,-3.186743,5.309237,-1.826847,9.542624,-8.197528,5.275229,1.562110,-5.719005,-8.852285,-8.158565,1.318005,3.750344,-6.233525,4.672105,6.510381,-5.146805], dtype = "float32")#candidate|9507|(132,)|const|float32
const_9508 = relay.const([[-10,6,-9,7,3,-3],[-6,-10,-9,-6,3,2],[-8,5,-9,-8,7,-6],[1,10,1,-1,-6,-5],[-7,5,-10,4,-7,3],[4,-7,-5,7,6,-10],[-1,-5,3,3,2,9],[-6,-9,-4,9,2,-10],[8,-3,-7,3,-5,4],[-8,-7,6,10,1,-4],[-2,6,10,-2,-3,5],[9,7,-8,-1,9,-7],[-6,-8,-6,3,-7,3],[4,8,-8,7,-4,-3],[-7,-7,2,5,2,-4],[-8,-8,7,4,5,-1],[8,-2,4,3,8,10],[-5,-8,10,5,3,3],[-5,3,3,-2,-2,3],[8,7,-7,7,-4,1],[1,2,-1,3,-3,3],[8,7,10,6,-6,-5],[2,9,1,9,-7,-3],[7,-4,4,-6,-7,-4],[3,-4,-5,-5,4,-2],[-3,-4,-4,-1,-7,-3],[6,-3,4,-9,-7,9],[-3,8,8,2,-5,-4],[-5,1,-1,3,8,8],[3,-1,10,4,-4,-3],[-6,-4,3,-1,-2,-2],[-1,-10,-1,10,-8,6],[-3,-3,5,-9,-3,4],[-2,4,-9,9,-9,8],[-7,-4,9,3,10,-9],[4,-8,3,-10,-8,1],[3,7,6,2,2,-10],[-7,3,1,-6,9,9],[-5,7,7,1,7,-2],[3,-8,-1,8,-1,9],[2,-6,-9,-3,6,-10],[-9,3,-8,10,-8,-10],[7,8,10,2,1,3],[5,-4,5,5,4,-9],[-10,8,7,6,-6,6],[2,-8,-7,4,-6,-2],[4,-6,-3,3,-3,-3],[8,8,6,2,1,-2],[10,10,-4,-6,10,-7],[6,-8,10,1,1,-4],[3,-4,5,-5,-1,8],[5,-6,-5,-8,4,9],[-7,3,-10,-4,4,-9],[5,-1,-7,6,2,-7],[-6,7,-2,5,7,-7],[9,-1,-1,-10,-6,-5],[-10,7,2,1,2,9],[4,-3,-5,9,-4,-5],[-5,-3,5,-4,-10,9],[8,1,5,1,-5,-2],[7,-2,-6,-7,-3,-1],[-10,-3,7,-2,1,-2],[3,-8,10,-9,-5,-7],[8,-1,-4,-9,-7,-3],[-6,9,8,4,9,-10],[-3,-5,9,-9,-5,10],[-1,2,-1,4,9,5],[-7,9,-10,-4,-7,1],[-10,-3,-1,2,1,-1],[10,2,-1,7,5,-5],[-6,-7,-7,-6,-1,1],[3,-3,9,7,-9,1],[3,9,5,-2,-4,-3],[-9,9,-2,-1,6,-7],[6,-6,-2,-7,6,-2],[2,3,5,7,7,-6],[-6,3,-9,-9,-4,-1],[2,1,4,1,7,3],[10,-8,6,7,10,-6],[-10,-3,-9,-9,10,1],[3,-1,-5,-6,4,3],[7,6,10,6,6,-2],[-4,8,-3,10,-8,-10],[-7,8,-8,3,-3,-5],[-10,2,-10,3,-7,8],[9,-10,10,1,-4,-1],[2,-10,-5,-7,-7,3],[3,-1,-6,-2,8,-1],[10,8,-1,-8,4,-7],[4,4,-10,1,2,4],[3,-10,-8,3,-2,-3],[9,7,1,2,7,9],[2,3,-3,1,-2,9],[5,1,-3,2,8,-5],[5,-6,-5,2,-4,3],[-9,-3,9,-5,4,-2],[10,8,5,-7,-5,3],[-8,9,-9,1,-9,10],[-8,4,1,-8,-2,-7],[2,-7,6,6,6,-6],[-10,-4,-1,10,-1,1],[10,1,6,1,1,-6],[10,1,-9,-3,-3,-9],[3,-2,-2,4,-2,6],[-4,-7,-6,2,-7,4],[-9,5,5,-4,3,-3],[-1,-9,-2,3,1,-3],[-3,3,-9,5,7,9],[4,-10,-3,2,-10,7],[7,9,9,4,-8,-1]], dtype = "uint64")#candidate|9508|(110, 6)|const|uint64
call_9504 = relay.TupleGetItem(func_2538_call(relay.reshape(const_9505.astype('bool'), [9, 13, 1]), relay.reshape(var_9506.astype('bool'), [9, 13, 6]), relay.reshape(const_9498.astype('float32'), [320,]), relay.reshape(const_9507.astype('float32'), [132,]), relay.reshape(const_9508.astype('uint64'), [330, 2]), ), 1)
call_9509 = relay.TupleGetItem(func_2544_call(relay.reshape(const_9505.astype('bool'), [9, 13, 1]), relay.reshape(var_9506.astype('bool'), [9, 13, 6]), relay.reshape(const_9498.astype('float32'), [320,]), relay.reshape(const_9507.astype('float32'), [132,]), relay.reshape(const_9508.astype('uint64'), [330, 2]), ), 1)
func_8206_call = mod.get_global_var('func_8206')
func_8208_call = mutated_mod.get_global_var('func_8208')
call_9511 = relay.TupleGetItem(func_8206_call(relay.reshape(const_9507.astype('float32'), [132,])), 3)
call_9512 = relay.TupleGetItem(func_8208_call(relay.reshape(const_9507.astype('float32'), [132,])), 3)
uop_9519 = relay.exp(call_9511.astype('float64')) # shape=(330, 2)
uop_9521 = relay.exp(call_9512.astype('float64')) # shape=(330, 2)
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
var_9523 = relay.var("var_9523", dtype = "float64", shape = (14, 28))#candidate|9523|(14, 28)|var|float64
call_9522 = func_8298_call(relay.reshape(var_9523.astype('float64'), [4, 14, 7]))
call_9524 = func_8298_call(relay.reshape(var_9523.astype('float64'), [4, 14, 7]))
uop_9529 = relay.sin(uop_9519.astype('float32')) # shape=(330, 2)
uop_9531 = relay.sin(uop_9521.astype('float32')) # shape=(330, 2)
bop_9532 = relay.power(uop_9529.astype('float64'), relay.reshape(call_9511.astype('float64'), relay.shape_of(uop_9529))) # shape=(330, 2)
bop_9535 = relay.power(uop_9531.astype('float64'), relay.reshape(call_9512.astype('float64'), relay.shape_of(uop_9531))) # shape=(330, 2)
bop_9541 = relay.add(uop_9519.astype('float32'), relay.reshape(uop_9529.astype('float32'), relay.shape_of(uop_9519))) # shape=(330, 2)
bop_9544 = relay.add(uop_9521.astype('float32'), relay.reshape(uop_9531.astype('float32'), relay.shape_of(uop_9521))) # shape=(330, 2)
func_6139_call = mod.get_global_var('func_6139')
func_6145_call = mutated_mod.get_global_var('func_6145')
const_9550 = relay.const([-1.388341,1.210256,-1.032947,-9.373287,2.883673,-0.011369,7.551931,0.210310,1.215402,2.574734,-6.313457,6.036576,2.148925,-6.186285,8.975813,-4.029417,4.352163,-3.104461,-9.461947,5.210353,4.505699,-2.221601,9.728650,-8.665742,-0.608875,-4.247292,-4.839664,-3.404986,8.489804,-0.089002,-1.428789,-1.839537,4.567675,9.976464,2.158132,1.697230,-6.164062,4.731108,4.790570,-4.642245,5.795019,-4.793335,-5.884839,6.792495,-0.485249,3.256440,-9.293619,-4.444466,-2.819302,-1.863638,-1.955384,-7.907775,7.827910,-8.120468,-4.264780,1.717519,2.619882,1.788615,-9.408990,3.455344,4.244434,0.508527,-8.269380,3.325416,2.633568,-3.269445,4.385153,-1.185050,-6.994924,9.205026,3.306837,-4.326331,-7.308473,5.440892,6.372903,0.211847,6.483768,-4.329865,5.895415,-0.422151,6.523701,-7.369919,9.004962,-6.772229,-4.905515,-3.569427,-9.221533,-2.589675,5.078729,8.966053,2.140933,5.886944,-0.152262,-0.106325,7.819962,-8.316555,-2.419700,8.106914,-5.241530,0.391189,7.936751,-3.652898,0.032551,-7.988627,-6.548293,6.695520,0.288610,-7.894614,-6.503944,8.424274,9.440127,2.117624,-4.505696,-1.654016,-5.934566,5.613240,5.692758,5.134971,9.079188,7.575423,6.416915,8.387023,9.807683,-2.957485,-4.880384,1.548937,-8.608144,9.735894,9.202730,2.039681,-3.572865,2.839645,-6.857354,-7.662561,9.792616,-4.715535,-3.619074,3.189222,5.473289,6.536368,4.920917,-7.266834,0.289031,-1.643390,7.758708,-5.676215,9.179251,5.738202,-9.499717,5.909351,-1.463268,7.223078,3.107126,-3.752060,-4.110744,-6.508255,9.781977,3.352368,2.871868,3.939832,6.249203,-0.053926,-0.412342,6.828404,1.699604,-5.039441,-7.832874,-9.759661,-7.633019,-2.247396,-9.094572,-8.724929,3.591808,5.552632,6.784108,8.075153,-1.092484,5.359175,-1.498036,-0.087955,1.613706,5.752444,-2.314703,9.126867,-8.560610,4.249275,0.629888,-4.639881,-9.987013,8.902806,5.356053,-6.887418,-5.346526,-6.451352,-6.767633,-8.387315,9.877532,2.980575,5.566288,-2.011486,9.738099,-1.089008,3.272878,4.790099,-8.569846,3.952212,-5.678477,-8.306479,-7.454837,7.956906,1.859693,-3.042328,6.524022,-1.421687,4.789929,-6.899714,-3.701122,4.534145,-4.897442,3.123642,2.888900,-1.563631,9.457631,-6.304104,5.523175,-7.931554,5.642709,4.321052,7.257287,9.491169,-3.590984,7.650843,-3.561534,-5.700134,9.678580,-8.027259,-4.189764,-4.468943,9.047861,9.226898], dtype = "float32")#candidate|9550|(240,)|const|float32
var_9551 = relay.var("var_9551", dtype = "float64", shape = (900,))#candidate|9551|(900,)|var|float64
call_9549 = relay.TupleGetItem(func_6139_call(relay.reshape(const_9550.astype('float32'), [3, 10, 8]), relay.reshape(var_9551.astype('float64'), [18, 50]), relay.reshape(const_9498.astype('float32'), [40, 8]), relay.reshape(call_9471.astype('float32'), [40,]), ), 6)
call_9552 = relay.TupleGetItem(func_6145_call(relay.reshape(const_9550.astype('float32'), [3, 10, 8]), relay.reshape(var_9551.astype('float64'), [18, 50]), relay.reshape(const_9498.astype('float32'), [40, 8]), relay.reshape(call_9471.astype('float32'), [40,]), ), 6)
output = relay.Tuple([call_9471,call_9473,var_9474,call_9490,var_9491,const_9492,call_9497,const_9498,call_9504,const_9505,var_9506,const_9507,const_9508,call_9522,var_9523,bop_9532,bop_9541,call_9549,const_9550,var_9551,])
output2 = relay.Tuple([call_9472,call_9475,var_9474,call_9493,var_9491,const_9492,call_9499,const_9498,call_9509,const_9505,var_9506,const_9507,const_9508,call_9524,var_9523,bop_9535,bop_9544,call_9552,const_9550,var_9551,])
func_9555 = relay.Function([var_9474,var_9491,var_9506,var_9523,var_9551,], output)
mod['func_9555'] = func_9555
mod = relay.transform.InferType()(mod)
mutated_mod['func_9555'] = func_9555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9555_call = mutated_mod.get_global_var('func_9555')
var_9557 = relay.var("var_9557", dtype = "float32", shape = (210,))#candidate|9557|(210,)|var|float32
var_9558 = relay.var("var_9558", dtype = "float64", shape = ())#candidate|9558|()|var|float64
var_9559 = relay.var("var_9559", dtype = "bool", shape = (702,))#candidate|9559|(702,)|var|bool
var_9560 = relay.var("var_9560", dtype = "float64", shape = (14, 28))#candidate|9560|(14, 28)|var|float64
var_9561 = relay.var("var_9561", dtype = "float64", shape = (900,))#candidate|9561|(900,)|var|float64
call_9556 = func_9555_call(var_9557,var_9558,var_9559,var_9560,var_9561,)
output = call_9556
func_9562 = relay.Function([var_9557,var_9558,var_9559,var_9560,var_9561,], output)
mutated_mod['func_9562'] = func_9562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_9601 = relay.TupleGetItem(func_8014_call(), 0)
call_9602 = relay.TupleGetItem(func_8016_call(), 0)
func_5642_call = mod.get_global_var('func_5642')
func_5648_call = mutated_mod.get_global_var('func_5648')
var_9613 = relay.var("var_9613", dtype = "bool", shape = ())#candidate|9613|()|var|bool
var_9614 = relay.var("var_9614", dtype = "bool", shape = (117,))#candidate|9614|(117,)|var|bool
const_9615 = relay.const([False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False], dtype = "bool")#candidate|9615|(702,)|const|bool
const_9616 = relay.const([[-6.959409,-9.927060,2.162319,-0.564802],[-0.489148,-5.754142,-8.469904,-8.645456],[-4.829663,0.032465,4.655585,-5.396227],[8.524213,2.408814,2.030465,-9.785955],[-0.070754,-9.706415,-8.790316,-9.372387],[-7.425176,-3.156394,-2.608588,-7.573267],[-2.107223,4.802224,-6.173228,-9.733501],[4.225862,-0.897076,2.503733,2.805358],[6.860112,2.968538,-3.264596,7.479412],[-6.351661,-1.519645,-3.839632,5.717759],[-1.996251,-7.451730,0.748776,0.349356],[-8.663924,6.904913,-3.008164,-3.428173],[-2.753200,0.167602,6.390601,-1.894401],[5.925809,-8.802541,5.626012,-6.109818],[-7.155834,9.593980,3.842817,9.837019],[-5.340336,6.578390,7.509270,-0.948567],[9.367187,-6.731892,-8.679777,-7.542023],[4.018662,0.123862,0.714703,8.520980],[-8.600247,9.771680,0.065093,-1.219372],[1.291280,-0.922093,2.042954,-2.495208],[-2.368168,0.730259,1.303365,-8.310442],[-0.653989,-0.818886,2.427366,-4.928083],[-2.160188,5.709437,-4.088262,2.577773],[9.881387,-2.972589,-7.252171,1.137348],[7.558624,-5.295290,4.935969,-8.362492],[-5.383628,5.558434,-7.070947,-5.395516],[6.754120,-5.414061,4.480710,2.960539],[4.626811,4.830980,-2.280397,-0.383137],[9.074023,9.907908,-1.604145,-4.826591],[-3.567064,-4.670474,4.346163,9.114522],[2.216424,-7.987390,8.261213,1.789857],[2.949417,-5.633587,-6.003880,-4.964820],[1.855820,-2.644907,2.828326,2.701042]], dtype = "float32")#candidate|9616|(33, 4)|const|float32
var_9617 = relay.var("var_9617", dtype = "uint64", shape = (5, 132))#candidate|9617|(5, 132)|var|uint64
call_9612 = relay.TupleGetItem(func_5642_call(relay.reshape(var_9613.astype('bool'), []), relay.reshape(var_9614.astype('bool'), [13, 9]), relay.reshape(const_9615.astype('bool'), [702,]), relay.reshape(const_9616.astype('float32'), [132,]), relay.reshape(var_9617.astype('uint64'), [660,]), ), 4)
call_9618 = relay.TupleGetItem(func_5648_call(relay.reshape(var_9613.astype('bool'), []), relay.reshape(var_9614.astype('bool'), [13, 9]), relay.reshape(const_9615.astype('bool'), [702,]), relay.reshape(const_9616.astype('float32'), [132,]), relay.reshape(var_9617.astype('uint64'), [660,]), ), 4)
output = relay.Tuple([call_9601,call_9612,var_9613,var_9614,const_9615,const_9616,var_9617,])
output2 = relay.Tuple([call_9602,call_9618,var_9613,var_9614,const_9615,const_9616,var_9617,])
func_9630 = relay.Function([var_9613,var_9614,var_9617,], output)
mod['func_9630'] = func_9630
mod = relay.transform.InferType()(mod)
mutated_mod['func_9630'] = func_9630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9630_call = mutated_mod.get_global_var('func_9630')
var_9632 = relay.var("var_9632", dtype = "bool", shape = ())#candidate|9632|()|var|bool
var_9633 = relay.var("var_9633", dtype = "bool", shape = (117,))#candidate|9633|(117,)|var|bool
var_9634 = relay.var("var_9634", dtype = "uint64", shape = (5, 132))#candidate|9634|(5, 132)|var|uint64
call_9631 = func_9630_call(var_9632,var_9633,var_9634,)
output = call_9631
func_9635 = relay.Function([var_9632,var_9633,var_9634,], output)
mutated_mod['func_9635'] = func_9635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_9651 = func_8443_call()
call_9652 = func_8443_call()
uop_9667 = relay.sin(call_9651.astype('float32')) # shape=(2, 15, 11)
uop_9669 = relay.sin(call_9652.astype('float32')) # shape=(2, 15, 11)
func_2993_call = mod.get_global_var('func_2993')
func_2999_call = mutated_mod.get_global_var('func_2999')
const_9673 = relay.const([-4,1,4,3,-9,3,-3,-10,8,-10,6,5,-9,-9,-4,6,-1,3,5,3,10,9,-8,-8,2,-7,1,-2,-8,3,7,-1,-8,-6,-10,-9,6,4,9,-8,9,1,-7,2,4,-1,-5,-1,-5,-8,-5,-5,-6,-7,-2,-8,-2,3,-2,7,8,-8,10,-8,6,2,-4,4,-8,9,-8,3,5,-9,10,-6,-6,3,-6,3,-8,5,1,-6,-2,1,9,10,-9,-3,-7,-9,-3,-10,-3,1,5,-5,-9,7,5,1,-1,8,-10,-1,1,-1,-10,5,2,-9,4,-7,-7,4,2,6,6,5,6,-6,-4,3,-8,1,4,8,4,-1,-10,2,2,-9,-1,-8,-10,4,-9,-2,-5,8,-3,-9,2,7,-7,-7,-5,9,9,-3,-10,-7,-3,-8,1,8,-2,10,-7,7,-8,-2,9,10,-9,-10,-9,-7,-5,-3,-1,-2,-7,7,1,-9,8,-3,3,6,-6,10,-1,-10,-4,-5,-3,7,9,-6,-8,9,-6,-3,-6,2,3,-9,-1,-1,9,1,2,4,2,10,-4,-5,3,-9,7,3,5,4,-1,2,-2,-4,1,-6,9,-4,-6,1,-9,2,-6,-5,9,7,-6,-9,-2,-5,-2,-7,-6,4,-1,3,7,-5,-2,-4,-2,8,7,-8,-2,-1,1,-5,-8,1,4,-1,-9,6,9,-10,-8,-10,-6,6,-1,-4,7,-1,8,8,6,-5,-6,-6,-10,9,-5,-4,7,-2,-1,5,6,4,-10,6,-2,10,-3,-4,-5,10,1,-4,8,-1,10,6,1,-10,2,8,-10,-1,-7,5,-7,-3,-10,1,10,-6,5], dtype = "int16")#candidate|9673|(315,)|const|int16
const_9674 = relay.const([9,5,-8,6,10,-5,3,-4,7,-2,-5,4,8,-1,-4,3,-10,1,7,-6,-9,-3,7,3,-1,-9,-6,10,2,4,2,1,-8,-1,-2,-3,-10,-5,-4,-2,-3,-1,7,-2,-5,-5,4,8,-10,6,-8,5,5,-4,8,2,-1,8,-4,-7,7,-5,-7,2,4,1,6,9,-6,8,2,-5,5,-1,4,-8,-9,1,-8,5,-10,3,4,7,8,6,-7,3,4,9,-1,10,-1,-7,-5,-8,-1,-3,6,7,-5,-2,-3,2,-8,-7,9,-8,-2,7,7,4,-8,-5,5,8,4,-2,-6,6,7,-4,5,-7,7,4,-3,4,-3,8,10,2,6,4,-10,8,6,-6,-6,-7,10,6,10,-5,-8,3,-6,3,8,-8,8,8,9,-6,-8,5,4,9,3,7,4,-3,-6,6,4,4,9,-7,-7,-1,-5,1,2,-3,6,8,1,-2,-8,3,-2,5,1,8,-4,-1,9,-8,5,-6,1,-1,-7,-9,1,8,-9,5,-6,5,5,-1,-1,-5,-10,5,7,2,-1,9,-1,7,2,9,6,10,-4,-6,-7,1,-2,-7,-4,-2,-1,9,10,3,8,1,-8,7,-9,-6,4,6,-4,2,3,3,5,-8,-7,-8,-3,-3,10,-2,3,-7,-5,-10,5,7,7,4,3,10,10,-7,9,-5,-9,1,-7,8,1,-1,3,-8,9,4,-1,1,2,-6,9,-1,-8,-2,-1,7,2,2,-9,6,10,9,4,-7,-10,-7,-4,-9,1,1,2,5,7,9,-6,5,5,-1,6,7,-3,-6,5,1,-7,-9,2,4,1,-7,-8,-7,6,6,-6,-9,7,7,-1,9,3,-8,4,-4,5,4,-2,10,8,2,-9,4,6,-10,-2,-6,7,-7,8,-5,-3,-8,-9,4,4,-5,7,-9,-1,-2,7,7,4,4,5,6,-8,2,-3,-7,2,-10,-1,2,7,6,-3,-8,7,10,-1,2,1,1,10,-10,1,-1,-8,-6,-6,7,-7,8,-8,10,5,1,5,9,-1,10,-9,-4,-4,2,-5,1,5,-10,8,-2,-1,10,-6,-3,-5,7,-2,1,-1,7,-1,2,10,6,-1,2,3,9,-8,-4,-3,-9,2,-2,2,-1,-10,8,4,-7,-4,8,-10,5,-7,-2,-2,7,10,8,-1,-4,1,-10,-6,1,-5,-5,6,-4,1,-3,-9,-6,8,-1,-3,9,-7,-3,5,2,3,-8,9,1,-9,2,3,-7,2,-1,6,-2,-8,-5,9,6,5,2,-5,4,5,2,-4,8,-8,2,8,7,7,10,9,9,-7,8,1,-6,5,-4,-6,4,3,7,10,-9,8,-4,-5,-1,-1,4,8,-8,-7,-4,7,8,6,3,-1,-4,2,-6,-8,-9,5,-2,-5,-7,-5,5,3,-3,-9,6,9,-9,-7,-7,-1,5,-2,-10,-5,7,-10,-3,-8,-3,-5,8,-10,-6,-3,1,1,-1,-2,8,-8,9,-1,-4,-1,5,7,-1,-2,5,1,-1,-3,-5,-5,-2,2,-4,4,-2,-4,-10,-2,-1,9,2,-3,2,9,-1,-2,7,4,7,-9,4,5,6,6,-4,5,-5,-10,6,-6,-4,-2,4,-2,6,7,-5,-8,2,2,1,1,-6,4,-2,1,-3,-7,-8,8,-8,-6,9,-6,9,6,-5,-7,10,5,6,-8,-8,5,-1,2,2,-4,3,2,10,-2,-7,-8,-2,8,10], dtype = "uint64")#candidate|9674|(660,)|const|uint64
var_9675 = relay.var("var_9675", dtype = "float32", shape = (320,))#candidate|9675|(320,)|var|float32
call_9672 = relay.TupleGetItem(func_2993_call(relay.reshape(const_9673.astype('int16'), [15, 3, 7]), relay.reshape(const_9673.astype('int16'), [15, 3, 7]), relay.reshape(const_9674.astype('uint64'), [660,]), relay.reshape(var_9675.astype('float32'), [320,]), ), 0)
call_9676 = relay.TupleGetItem(func_2999_call(relay.reshape(const_9673.astype('int16'), [15, 3, 7]), relay.reshape(const_9673.astype('int16'), [15, 3, 7]), relay.reshape(const_9674.astype('uint64'), [660,]), relay.reshape(var_9675.astype('float32'), [320,]), ), 0)
output = relay.Tuple([uop_9667,call_9672,const_9673,const_9674,var_9675,])
output2 = relay.Tuple([uop_9669,call_9676,const_9673,const_9674,var_9675,])
func_9685 = relay.Function([var_9675,], output)
mod['func_9685'] = func_9685
mod = relay.transform.InferType()(mod)
mutated_mod['func_9685'] = func_9685
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9686 = relay.var("var_9686", dtype = "float32", shape = (320,))#candidate|9686|(320,)|var|float32
func_9685_call = mutated_mod.get_global_var('func_9685')
call_9687 = func_9685_call(var_9686)
output = call_9687
func_9688 = relay.Function([var_9686], output)
mutated_mod['func_9688'] = func_9688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8161_call = mod.get_global_var('func_8161')
func_8162_call = mutated_mod.get_global_var('func_8162')
call_9831 = relay.TupleGetItem(func_8161_call(), 1)
call_9832 = relay.TupleGetItem(func_8162_call(), 1)
func_8887_call = mod.get_global_var('func_8887')
func_8895_call = mutated_mod.get_global_var('func_8895')
var_9837 = relay.var("var_9837", dtype = "int16", shape = (315,))#candidate|9837|(315,)|var|int16
var_9838 = relay.var("var_9838", dtype = "float32", shape = (2, 160))#candidate|9838|(2, 160)|var|float32
var_9839 = relay.var("var_9839", dtype = "float32", shape = (2, 520))#candidate|9839|(2, 520)|var|float32
var_9840 = relay.var("var_9840", dtype = "float32", shape = (132,))#candidate|9840|(132,)|var|float32
const_9841 = relay.const([-4.787522,-2.738152,3.884714,3.933367,-5.696225,4.525771,4.052382,0.288747,0.122933,5.900843,-7.351358,-8.500894,-8.736818,3.748821,8.462853,5.166138,-0.409734,4.948933,-3.815715,3.400522,4.780646,6.250316,-0.964693,7.568376,-3.484458,3.615948,2.648816,-1.220771,-0.893490,-1.663697,-9.141749,3.274100,1.059705,-6.586533,3.814297,-7.351633,-9.561670,3.093277,-6.211376,-2.485775,4.245981,9.832394,-0.958219,3.855516,7.117461,-8.482011,9.455813,2.757739,3.267418,-0.214612,7.352413,1.438607,-2.680844,-9.711142,1.293142,8.107633,-2.860348,3.240561,-8.283902,8.248840,-2.134981,9.560256,-1.270442,-2.293365,-3.035467,-4.363045,7.619972,-0.907090,5.751758,2.692624,5.634991,1.713020,6.507319,-4.881146,4.537213,-3.487757,-0.869076,9.408527,-8.958892,-3.159902,-6.427575,-8.620303,-9.255730,0.343146,6.970788,-6.009078,-6.314806,-2.533190,-7.228922,4.864745,-1.405419,-4.619573,-5.706616,5.640377,0.393341,6.360280,7.731970,-4.791433,-2.027456,6.408698,-5.038116,6.792783,4.181302,-8.351071,-3.888185,-3.704308,3.292625,6.796399,-1.400258,-1.011537,-3.521582,-7.725162,0.676315,0.542008,-7.944552,1.969305,-9.594494,8.074957,-1.546382,-6.451724,-6.460297,-5.601861,2.407588,4.989323,-0.837235,0.793911,5.528617,-5.031742,-4.010713,6.204117,-3.205730,8.108669,9.061399,7.495254,3.814822,-1.131217,-3.972154,0.143836,4.016421,0.094664,0.317294,-9.215626,-0.912148,2.385696,4.047974,-8.210983,-7.155373,-4.518969,-1.703456,9.292923,2.101536,2.255788,-3.625125,2.950499,5.071661,-8.911530,-8.152033,-8.091582,2.596834,7.651593,-9.171732,2.449469,-6.498296,-2.198571,0.906982,-9.889940,2.615327,-1.965701,-2.792158,0.780827,-2.540461,-2.821083,7.896139,-7.554012,7.847376,0.722506,6.906137,-9.305127,-9.140804,-7.770402,-0.596183,7.026129,7.677756,-9.120859,7.884191,4.601488,3.840561,-8.454850,-3.310153,6.684144,6.873134,0.315451,2.502505,-7.579178,-1.903373,9.695352,9.723539,9.712569,-8.031557,-3.989574,0.844409,-5.010839,-4.440015,6.045162,7.244601,-5.243848,6.034234,5.587783,8.133093,1.362463,-8.819691,-4.975575,2.060195,-9.784092,9.259044,6.548138,0.823431,1.312352,3.593155,-0.515663,-5.479440,3.638450,9.722495,-7.074962,-5.742275,-6.174356,4.321649,-5.550577,-6.299102,-5.849792,1.758191,5.735638,0.946211,-4.859289,8.082314,6.747496,4.829282,-5.844670,2.603034,7.170195,-3.703873,7.005399,7.544333,-8.905619,-1.966112,5.818396,-6.929936,-1.220457,-6.385748,-2.750356,-7.865179,3.623767,-1.635679,-5.488846,-3.751742,8.063201,9.541264,-0.143194,-2.294680,0.334546,-5.988175,9.831055,5.061527,-5.892432,-1.826223,4.021992,5.717331,4.709620,-5.654093,5.483366,9.704345,0.877410,7.099752,3.376592,-2.255493,1.078829,-5.866348,-4.363896,-5.349765,7.900904,6.459144,1.985128,0.414015,4.775964,-4.609476,-9.681400,7.658959,6.096198,-2.928763,4.377642,3.466172,1.496062,8.916487,3.954507,-4.315085,-8.647078,1.565898,-6.128913,-5.245929,2.832780,4.487724,5.763959,5.738966,1.994573,2.786903,1.793769,1.775699,-8.274608,-5.505765,7.951948,-4.473224,-9.810887,8.828590,-2.138529,-8.382436,4.830366,-2.703689,2.875793,0.744364,6.956070,9.076889,8.852353,4.733814,5.005549,6.377022,-7.904446,-4.133264,1.527863,-5.243287,-6.099361,9.205493,-9.721343,-9.605147,-8.686139,-6.388861,-7.363568,-4.680886,9.318254,-6.781525,6.696490,7.123951,3.786373,-8.496316,1.562137,1.595887,-8.727308,9.283428,-0.702642,-6.985974,9.179937,-3.524521,-8.293413,9.858653,-0.429147,-7.247536,5.673303,6.166671,1.771785,-3.055227,-8.847728,-3.260564,-4.337220,0.252206,6.518686,6.323114,6.594939,8.729185,-2.231683,0.412709,-4.254263,-4.163125,5.988704,-7.175848,-2.831492,8.187707,-4.032786,3.484216,-3.480449,6.841477,-7.491043,-1.869133,-9.468924,4.021805,7.335785,0.014925,-2.106081,4.730777,-3.966000,-5.839984,-8.279911,0.355791,-4.169046], dtype = "float64")#candidate|9841|(392,)|const|float64
var_9842 = relay.var("var_9842", dtype = "float64", shape = (14,))#candidate|9842|(14,)|var|float64
call_9836 = relay.TupleGetItem(func_8887_call(relay.reshape(var_9837.astype('int16'), [5, 63]), relay.reshape(var_9838.astype('float32'), [320,]), relay.reshape(call_9831.astype('float32'), [40,]), relay.reshape(var_9839.astype('float32'), [1040,]), relay.reshape(var_9840.astype('float32'), [132,]), relay.reshape(const_9841.astype('float64'), [392,]), relay.reshape(var_9842.astype('float64'), [14,]), ), 14)
call_9843 = relay.TupleGetItem(func_8895_call(relay.reshape(var_9837.astype('int16'), [5, 63]), relay.reshape(var_9838.astype('float32'), [320,]), relay.reshape(call_9831.astype('float32'), [40,]), relay.reshape(var_9839.astype('float32'), [1040,]), relay.reshape(var_9840.astype('float32'), [132,]), relay.reshape(const_9841.astype('float64'), [392,]), relay.reshape(var_9842.astype('float64'), [14,]), ), 14)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_9863 = relay.TupleGetItem(func_8014_call(), 0)
call_9864 = relay.TupleGetItem(func_8016_call(), 0)
var_9868 = relay.var("var_9868", dtype = "float32", shape = (2, 160))#candidate|9868|(2, 160)|var|float32
bop_9869 = relay.less(var_9838.astype('bool'), relay.reshape(var_9868.astype('bool'), relay.shape_of(var_9838))) # shape=(2, 160)
uop_9872 = relay.tan(bop_9869.astype('float64')) # shape=(2, 160)
func_9004_call = mod.get_global_var('func_9004')
func_9005_call = mutated_mod.get_global_var('func_9005')
call_9881 = relay.TupleGetItem(func_9004_call(), 0)
call_9882 = relay.TupleGetItem(func_9005_call(), 0)
var_9890 = relay.var("var_9890", dtype = "float64", shape = (2, 160))#candidate|9890|(2, 160)|var|float64
bop_9891 = relay.left_shift(uop_9872.astype('uint8'), relay.reshape(var_9890.astype('uint8'), relay.shape_of(uop_9872))) # shape=(2, 160)
func_6932_call = mod.get_global_var('func_6932')
func_6937_call = mutated_mod.get_global_var('func_6937')
var_9896 = relay.var("var_9896", dtype = "uint64", shape = (660,))#candidate|9896|(660,)|var|uint64
const_9897 = relay.const([5.416496,6.164039,-0.069229,9.087808,2.249959,6.026017,0.979071,-4.588923,-9.633367,-0.115746,-2.632023,2.082122,-7.059755,-0.013616,-7.003368,-3.259684,7.927636,-9.165222,-8.585180,-1.440422,6.467850,-0.320009,5.368212,1.591397,3.937715,-0.279333,7.624650,9.149795,-3.792167,7.226408,8.272524,-6.702786,9.041511,-3.697424,-3.341960,2.586376,-2.407283,8.743817,-9.106824,1.612367,-6.870493,3.738718,6.501368,8.906227,-1.795355,8.056056,-2.628585,2.034294,-7.629218,-3.372156,-4.501181,-7.815857,1.551297,-1.094067,-9.642166,7.979682,0.176522,-6.108262,4.280355,-5.454129,-3.681091,8.999133,-9.213276,5.087387,6.465984,4.709403,0.857762,-3.925811,0.056617,7.874867,3.388118,0.194306,5.997047,0.162310,9.926988,2.634057,1.203052,4.248062,5.382137,-1.138419,-0.751414,-3.363109,6.149594,-9.426241,3.845054,-5.843487,-5.120985,-5.929107,1.554299,0.749827,8.391462,8.206737,8.365058,-6.764718,0.945332,7.834052,1.468211,9.389244,3.648529,3.404611,1.554995,6.057547,7.085668,-4.283894,2.910934,-8.600688,-8.563054,-8.425174,-1.399005,-4.710202,1.254061,8.512433,5.460616,-4.858935,-9.829210,4.216624,9.811474,3.956825,-2.295767,-1.237630,3.214692,2.002293,-3.314502,-0.548053,-3.252632,-2.017976,-4.000149,-3.201385,-7.533762,-5.538659,8.284278,3.756093,-9.103147,2.965088,-6.792220,7.011943,-6.447243,4.966826,-8.215845,1.667912,-0.370348,-1.726553,6.986794,-4.995525,7.620153,-5.480259,-7.093548,-9.656602,5.684356,-0.784189,0.579828,9.329888,-1.004081,-7.327142,-4.925545,9.290848,8.496853,-7.193961,0.547016,-4.556736,1.188135,8.159541,-7.939527,5.860199,7.124878,9.795067,9.553263,0.820407,0.772029,-9.831752,6.113019,-9.150066,6.040552,-2.528796,5.891374,-1.277881,6.962013,6.679650,1.512427,9.718075,-4.858406,6.043801,-9.160313,9.665275,-0.538181,1.763294,9.694279,-5.140359,-9.080179,8.375047,2.825876,8.907318,6.412931,3.129244,9.189522,-8.386584,4.310506,9.749508,-0.062818,-0.734998,-4.303189,-3.634614,1.010108,-7.111995,4.036835,-5.158672,9.422415,-6.503661,-4.709040,6.992229,-7.207033,7.210396,8.691790,2.015363,8.505658,-2.968426,-4.959373,6.015081,6.637197,5.791000,-7.452389,-0.959430,0.743363,-4.144295,-1.226272,4.278281,7.336813,-9.307295,3.343502,-9.566948,2.700585,-7.348392,-4.201278,-8.920788,-9.668198,-9.520998,1.883863,-6.710727,6.790233,-8.242832,5.698070,0.563384,-6.416934,7.765745,0.866290,-3.571017,4.580941,-9.218020,-7.614104,7.413347,6.482319,7.658637,-7.363136,7.809402,8.014131,6.566856,-3.929407,1.077363,1.315233,-0.588213,5.479478,1.998773,-2.166921,-5.356066,-9.543828,1.197965,5.228036,-3.735019,-8.154055,-6.567415,6.167731,-0.391608,-2.415703,-1.698657,9.865584,-5.794273,4.223266,3.117051,-0.971295,8.591025,5.664353,-4.300502,8.915590,3.840146,-7.472941,9.120994,2.598012,9.222636,-4.933373,4.231606,9.785678,-0.617965,-8.077634,-8.566682,6.061147,1.762011,-8.839303,3.583213,2.835165,0.884110,-9.757450,4.762884,2.284265,2.289499,8.081998,5.767917,6.197565,5.047980,7.976833,-6.284565,3.846774,4.232651,5.057421,-0.379084,8.665938,-9.228506,-9.257686,-0.590750,9.130036,3.963592,-1.012309,8.807665,-1.862248,5.454491,-2.736617,-1.717468,-9.490853,4.511922,5.342229,-1.681178,6.782242,-7.361234,-0.540399,4.708579,5.401353,-0.443368,4.457941,0.375225,0.472767,5.081453,-3.893280,6.853966,-1.636064,-2.116969,-3.096712,-8.306284,8.378476,-5.933084,3.782399,9.186798,-7.343545,1.872093,1.196760,-9.319704,9.685454,-1.600299,8.833923,-2.252198,-4.774064,4.465285,2.332846,0.249174,0.945973,8.955908,9.400457,5.220752,-6.863327,-7.652743,7.128446,-9.315003,-3.598182,-0.767033,5.107668,0.893010,8.154485,-5.708930,7.642411,9.593574,3.278857,4.954131,-8.575868,4.531661,0.368864,-7.763960,-0.526644,-8.576279,-6.953321,-7.078389,6.740441,1.483263,1.356144,-6.501866,9.439977,3.137701,-1.390949,-1.347859,9.045764,9.190123,3.320165,4.926304,1.519997,-5.926267,-7.023293,9.219327,8.428483,-1.285631,-3.619953,5.009317,-6.350456,2.684518,5.838787,7.488352,7.660603,-8.700596,8.870561,-5.897350,9.582939,-4.951121,9.600387,2.886954,-2.532342,7.242392,-0.928105,6.229747,2.369654,1.820950,-6.663276,7.560505,-5.529902,-9.568069,3.682231,-7.987635,6.157123,-2.810163,-3.171927,5.955212,5.728104,2.399384,9.544960,8.889933,9.955811,-9.199036,9.948344,0.639440,1.909181,1.306801,-4.195921,8.865549,-6.616065,1.480231,9.726945,-5.114351,6.282404,1.021129,-5.813316,-3.756715,3.071866,2.587930,-5.320944,-6.952102,-2.170670,6.357044,6.210477,-9.175375,-8.171348,-2.017016,3.832971,8.938487,7.782079,4.911979,9.418065,4.376093,-7.134622,4.229755,-6.065809,-5.368074,-9.620897,2.650514,-5.105590,1.760167,6.136148,5.150809,-3.651071,-1.850444,6.652740,9.758024,3.211439,4.555668,1.204960,-3.599775,2.129336,-3.261449,-2.349787,6.545367,-9.884281,-6.011775,0.245680,-2.570252,-4.533959,5.115352,-5.477710,-0.395064,4.886962,-6.970681,-0.222788,-0.921422,0.413589,5.034781,3.397008,9.860822,-7.628841,6.223279,5.171025,5.050731,-3.364986,8.183293,-1.980384,-7.271617,3.210803,-1.005449,-1.455858,0.480730,-7.139430,5.858760,-3.289302,1.918919,-2.981025,-6.922324,-2.642737,9.837891,-2.123987,7.646814,-1.952872,-7.439549,-9.291896,-2.090795,-7.829386,0.510525,-5.968754,-0.846504,7.646372,2.585707,-1.175542,2.331898,-4.189555,-2.086394,2.100325,3.181721,8.333567,9.283954,-2.102855,-7.246918,-4.053234,8.271886,8.619929,0.790853,9.259459,-4.074314,-4.643243,-3.737795,4.060630,7.847588,0.632063,-2.857673,-3.821960,-0.393055,1.013354,9.075948,-3.421206,4.768197,-0.913761,-7.147341,8.996947,-4.585159,-2.566088,-6.304778,4.472132,-0.746897,-0.155549,0.781299,9.498981,-8.566881,5.984583,-3.571355,-5.538525,4.209247,-3.356344,5.337387,-5.766557,8.728625,-4.733296,-3.398722,1.416897,-9.650794,-5.155437,-2.789431,-2.271448,-9.818546,6.845364,5.720949,-8.903974,-4.923269,2.755325,3.322262,2.627344,-5.113221,-4.644480,5.275470,-7.908677,-2.829964,-7.798320,-6.830150,3.874675,-7.883373,6.006062,-0.542890,-5.727188,-5.967248,-5.743836,7.225709,-1.032552,-8.461408,5.673987,-3.349280,3.173787,-2.015348,4.368631,-1.242016,5.495498,8.601557,9.240304,4.610000,7.490904,9.729441,8.220813,4.555342,-2.374577,-6.923761,-8.432231,0.554665,0.703402,4.825163,-2.583431,5.129711,-7.488322,-5.200797,9.692647,4.904292,3.714606,-7.168085,9.996734,-8.405971,7.761084,1.413844,8.107951,-3.619228,-9.725726,-8.027320,2.565264,5.010914,-4.999291,4.074622,5.002296,-8.343329,8.658418,0.893749,1.801441,5.285511,-2.573883,-9.954110,7.559578,3.733191,-8.726343,3.920048,7.420406,2.771358,-5.839967,4.857471,4.524856,6.767676,1.889496,1.762056,-8.903883,0.533064,-0.539174,4.949260,-3.192181,5.033385,-3.995531,0.184851,5.031334,7.142527,6.828665,0.578912,8.162061,-3.488130,1.988105,5.238593,-3.042059,4.232358,-0.140113,-4.033824,1.742303,3.387979,-0.942693,1.889078,2.375984,-1.888880,-2.776922,5.107081,-6.986599,-6.246285,9.755842,0.138922,-0.428796,-2.141664,7.442361,-0.416174,4.581353,-9.580168,-7.857818,1.899669,9.386949,-8.375741,-0.955240,0.412782,6.386189,-5.335268,0.988565,-8.471279,-1.347929,-8.213831,-7.337351,-1.204690,-8.934463,1.651405,7.196301,-2.772664,-0.839385,-4.159709,-3.251958,1.784447,8.156943,-5.066416,-5.224289,-3.330869,-0.487928,-2.227803,0.109099,-5.325859,-3.403060,-5.396348,-3.101397,-1.169469,-9.846370,6.946489,-1.569737,-7.253322,6.276600,-5.161879,-6.832856,-6.814097,6.384079,9.204527,-5.770688,-0.449146,7.463773,-8.137089,8.666904,6.730143,6.380131,-6.393377,4.757645,1.712901,3.495626,-0.002092,-7.562734,-0.690996,-9.319438,7.622282,8.028914,0.710539,-1.961000,3.339770,-8.297856,1.891753,4.480744,0.538407,5.787902,1.116227,-2.237659,-5.937691,7.620539,-3.616744,-0.770438,-7.718043,3.636314,-2.036008,9.898327,8.678871,-5.440558,8.526410,-6.503997,5.217121,2.375957,-4.691987,-0.161936,-3.568246,-4.223619,8.372849,-4.587489,-7.609516,5.171551,-2.716879,-6.991046,-9.856584,-8.842173,5.380218,-5.396546,-4.312371,2.425030,0.089589,7.197856,7.468565,-7.391516,-0.222468,-8.800592,-8.508393,-7.383499,-5.886343,-7.404218,7.483467,-9.022700,9.917628,0.353261,-2.066942,8.674219,9.315707,-8.440585,-3.416873,5.115132,1.475466,4.241002,-6.269082,-1.864563,6.379829,4.756839,-8.870870,1.941186,8.515573,6.151109,2.428948,6.649198,-3.855306,-2.397730,1.228425,8.836212,2.121727,-7.119947,-0.478496,6.693145,-8.972010,5.776366,-1.255742,-1.751795,4.294449,-7.621410,-7.990380,0.202241,5.687314,1.010641,-8.840032,6.409721,-5.470490,4.718138,0.898784,-7.809810,0.982001,-7.400371,-0.258582,2.189843,-7.505933,-8.186594,-2.800120,1.014286,6.791540,-4.555969,-2.449991,-3.776189,7.413494,7.183241,-4.002320,-0.859116,5.785152,9.331148,-0.261492,-5.107392,-0.174306,8.698332,-8.342059,-0.943593,-7.425494,6.448627,6.606833,5.541676,6.658842,3.745313,-4.209117,-9.495391,-1.708511,3.351947,-7.382657,1.754558,-3.055532,6.147949,-7.230649,6.377951,-2.824132,4.459093,-0.141290,2.546662,2.347643,4.368917,-7.859567,-1.895476,3.398111,1.316304,3.912738,4.212268,-1.019693,-1.885648,-8.302905,0.697000,8.438704,-7.003199,7.295197,5.038088,-2.428661,-8.525261,-3.820628,3.307539,-7.997402,-5.766753,-4.144390,1.363786,-3.218523,0.519414,5.561894,-6.874374,2.383258,-2.089623,-1.037155,3.980122,-6.097144,4.052422,-1.283446,7.294062,-9.011873,-3.692931,6.076516,5.265780,-0.696045,-3.290707,1.444212,-8.280337,-7.364986,4.204882,-7.707219,7.728867,-2.747521,-9.284326,-3.713681,6.724739,1.851513,2.310039,8.584651,-8.800157,2.466478,-9.267842,5.695128,7.220632,6.056795,-7.204329,8.133755,3.462613,1.436184,3.309126,7.840165,-0.426099,-4.824504,6.208694,-5.770745,9.233351,-7.084464,-2.979883,-9.961290,7.649166,-0.131178,-2.700366,-3.747428,8.025056,2.158100,2.509074,3.325115,3.364401,6.818240,9.113912,-7.842889,4.584220,-0.340678,1.209853,9.202326,4.533210,-4.824486,3.914779,9.907389,-2.699691,0.430731,6.954800,0.197897,3.243926,8.801864,-1.440253,3.680772,-6.507520,9.051173,2.164331,9.259426,-5.696806,-9.453069,-3.196049,-1.610433,-3.329887,-3.974906,-1.056421,-4.929523,-6.691328,8.782938,5.024605,-6.146616,-6.257407,2.534868,-9.413204,-4.171605,1.131696,-6.711163,-4.900250,-5.461539,8.956963,-7.924034,3.812365,6.056755,-5.166698,-7.253392,0.090278,-3.281155,6.465451,0.697835,-9.623720,-2.879647,-4.269818,2.951398,-8.273755,8.218643,-8.272793,4.939934,-9.923115,6.690949,3.549940,6.594589,-9.229669,4.042572,0.500265,4.648250,-1.887452,5.687029,-3.882073,-6.791526,3.038940,-2.629355,4.294226,8.654901,-6.917483,6.202476,-1.301877,9.236865,-5.533494,-6.938270,3.685510,1.878226,-8.055851,0.107276,1.180672,5.742156,0.767380,-0.937867,5.535517,5.086692,-8.607529,-8.819927,9.062482,1.114995,-2.842962,8.904885,9.888217,5.496511,-5.478744,-2.621274,-3.679923,-5.454850,-6.750970,4.079540,-4.505446,3.448467,8.922350,0.415294,2.742323,-9.875276,5.259022,-6.815750,-3.518279,-4.450739,-4.853043,-5.042275,-0.676750,-0.706134,6.672858,-3.148411,-1.755520,-9.572799,3.262605,-4.346281,-2.202202,-8.327334,5.223983,-0.980991,3.847275,-9.729887,3.887748,-6.370622,3.752757,-8.363659,-7.063837,-1.018190,3.397417,-7.703544,-0.605433,0.148703,6.025184,-8.224493,-6.307898,-2.598010,4.449932,0.605055,2.044707,-2.177267,5.496417,8.095306,-3.348923,-8.181516,-1.028058,-2.567723,-9.229020,0.041328,-4.471391,-4.254469,-9.852386,-0.878607,7.475751,6.910718,0.778982,9.547968,-4.817859,9.825753,-6.795648,-7.240880,-5.495173,2.955784,2.315815,0.992103,1.665018,-3.665666,-5.213953,1.437812,1.611224,9.542484,9.638325,2.402991,6.774862,-1.384216,-1.738728,4.827082,0.576642,9.970503,6.356023,-6.347704,-7.701669,1.934483,8.640798,-6.195511,2.648517,-8.762782,-0.508694,-8.015503,-8.918690,0.598407,-7.293867,9.821771,-5.043109,-4.484100,0.147659,-3.381183,3.844552,6.204866,-2.526233,1.648728,2.324287,-4.704901,6.162385,0.984933,4.430906,5.783153,6.573825,-4.212918,1.701408,-6.635913,9.418800,4.699894,-2.882514,-4.958639,-0.785187,-9.678558,5.505048,-9.758225,1.415701,-7.149065,-1.400082,-4.129638,-4.471038,8.163599,4.854270,7.862608,-6.403605,-9.538954,4.651875,-0.837996,-5.118995,6.953331,3.216060,1.146608,8.840761,-7.619349,3.666329,-7.557512,7.411009,4.688856,1.617920,8.766124,2.516348,-1.390791,-6.090572,7.182035,6.781207,-7.644099,-8.112708,1.617083,4.716885,6.360650,0.219455,1.075172,-8.039885,3.274456,6.691425,3.177961,-5.225325,5.820982,-4.693864,-3.914229,4.525750,4.465873,-3.680006,4.695343,-8.769257,-0.434211,-5.748913,-1.209083,-0.611854,-3.267953,-4.905802,9.166624,7.800218,-2.368560,9.508482,1.817193,7.816764,-6.940623,-5.222627,-0.393396,-2.917283,-1.404708,-1.667023,0.970264,-2.963308,-1.908044,-9.810298,-0.669514,-0.385792,5.552073,3.486902,-9.605776,2.970941,-8.464386,-4.963972,-2.440902,5.997763,-3.508192,6.190232,-2.785783,1.450737,6.618291,-9.164965,-0.416301,-5.388182,-7.602519,-6.926329,-8.293856,7.203033,3.752826,2.078832,8.245400,-3.514614,-2.794289,4.512816,-0.922452,6.342624,-7.869325,2.925209,-3.038014,9.698884,4.978075,2.463538,4.278411,-3.106563,5.742847,4.079610,-7.634535,-8.463763,4.525888,1.802290,-4.005197,0.356487,4.467827,4.579013,-2.798773,-5.925757,7.471790,-0.225414,5.685041,5.541046,-3.693676,1.673601,4.348372,-3.903988,5.151670,-4.675392,-7.760061,3.764009,-2.030200,-0.481898,2.632710,-0.391306,-3.371686,8.645003,0.614617,-5.860690,6.876173,-5.618301,0.240806,-8.426097,-2.281610,2.220575,-3.131708,-2.502248,5.838489,-5.544330,-1.895495,2.789892,5.328867,-4.614307,-1.166884,-3.363671,-4.732178,-6.750900,5.766057,-8.601889,6.865171,2.905064,-4.946858,-0.209100,-1.158125,-5.957649,7.878389,2.526402,6.865926,4.647866,5.602389,3.502153,-3.199238,5.110553,-5.599609,1.996920,2.838664,-8.009635,8.854731,-5.632946,9.140913,-7.414041,-0.270954,2.891339,9.312477,6.295721,-6.793822,-3.569563,-1.999477,3.121699,5.500145,-4.851361,6.047722,0.393109,5.224769,-8.550483,-1.585650,7.895654,-8.931666,-1.178919,3.435813,-3.727280,4.468322,-8.077551,6.778966,-2.778810,4.415957,4.734252,0.382532,2.573087,-7.145133,6.034632,-7.308505,-2.243536,0.437612,-1.504378,-0.834611,6.400619,8.452948,-7.945755,1.983255,4.319885,5.201863,4.499982,0.259580,-3.839677,-9.272313,2.531136,-5.001047,4.482687,-3.162085,6.940317,7.211482,-0.751231,-3.649473,9.158449,-8.183082,-3.229174,1.054673,-6.581672,-2.953184,7.881649,8.266117,0.591215,-5.664478,1.326582,-9.100856,2.160569,6.395412,-1.644398,-9.521144,9.192703,9.612964,0.496887,0.417294,7.962016,-6.316886,-6.471305,4.575554,1.233036,1.458054,9.169084,0.928275,7.396390,-3.014837,9.187454,0.404209,2.757103,-2.790149,9.316639,1.717609,-7.218594,4.986074,4.122725,-0.630797,-3.814312,7.127751,-8.344754,5.097533,-3.735525,0.428495,-1.206219,-1.547903,7.404035,-4.336615,8.722379,-1.874423,6.029064,-5.986224,-2.620457,-4.542939,-4.106126,-0.178792,-0.047048,-8.699542,-4.157638,-7.330295,-0.634724,-9.976080,-2.803567,9.037026,-4.247367,8.814898,4.216137,-0.912539,-6.571298,5.997986,9.842976,1.729748,4.304714,-2.036190,-8.434862,-6.911641,3.072529,-6.847355,-9.048054,7.084839,8.231881,-8.586476,7.860382,2.760961,7.107737,-2.343435,-4.158970,5.912695,-5.837046,3.148207,-5.970711,8.730388,9.693751,4.118239,6.394096,-8.835195,8.318458,-9.285146,-0.351354,0.988131,-7.729507,-2.392772,3.641441,-0.429042,4.886137,-4.056765,7.750899,0.542002,-9.763606,-7.093018,-2.501997,-7.871652,-0.978998,-5.455531,-5.370497,-0.436986,8.982711,-7.471858,-8.789524,-2.454545,-3.768178,-7.041551,5.121289,-0.009401,-1.149977,7.087813,-1.258520,4.507136], dtype = "float32")#candidate|9897|(1600,)|const|float32
call_9895 = relay.TupleGetItem(func_6932_call(relay.reshape(var_9839.astype('float32'), [10, 8, 13]), relay.reshape(var_9840.astype('float32'), [132, 1]), relay.reshape(var_9896.astype('uint64'), [660,]), relay.reshape(const_9897.astype('float32'), [5, 320]), ), 3)
call_9898 = relay.TupleGetItem(func_6937_call(relay.reshape(var_9839.astype('float32'), [10, 8, 13]), relay.reshape(var_9840.astype('float32'), [132, 1]), relay.reshape(var_9896.astype('uint64'), [660,]), relay.reshape(const_9897.astype('float32'), [5, 320]), ), 3)
uop_9899 = relay.rsqrt(uop_9872.astype('float64')) # shape=(2, 160)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
call_9902 = relay.TupleGetItem(func_1719_call(relay.reshape(var_9840.astype('float32'), [12, 1, 11]), relay.reshape(var_9896.astype('uint64'), [660,]), ), 3)
call_9903 = relay.TupleGetItem(func_1723_call(relay.reshape(var_9840.astype('float32'), [12, 1, 11]), relay.reshape(var_9896.astype('uint64'), [660,]), ), 3)
output = relay.Tuple([call_9831,call_9836,var_9837,var_9839,var_9840,const_9841,var_9842,call_9863,call_9881,bop_9891,call_9895,var_9896,const_9897,uop_9899,call_9902,])
output2 = relay.Tuple([call_9832,call_9843,var_9837,var_9839,var_9840,const_9841,var_9842,call_9864,call_9882,bop_9891,call_9898,var_9896,const_9897,uop_9899,call_9903,])
func_9909 = relay.Function([var_9837,var_9838,var_9839,var_9840,var_9842,var_9868,var_9890,var_9896,], output)
mod['func_9909'] = func_9909
mod = relay.transform.InferType()(mod)
var_9910 = relay.var("var_9910", dtype = "int16", shape = (315,))#candidate|9910|(315,)|var|int16
var_9911 = relay.var("var_9911", dtype = "float32", shape = (2, 160))#candidate|9911|(2, 160)|var|float32
var_9912 = relay.var("var_9912", dtype = "float32", shape = (2, 520))#candidate|9912|(2, 520)|var|float32
var_9913 = relay.var("var_9913", dtype = "float32", shape = (132,))#candidate|9913|(132,)|var|float32
var_9914 = relay.var("var_9914", dtype = "float64", shape = (14,))#candidate|9914|(14,)|var|float64
var_9915 = relay.var("var_9915", dtype = "float32", shape = (2, 160))#candidate|9915|(2, 160)|var|float32
var_9916 = relay.var("var_9916", dtype = "float64", shape = (2, 160))#candidate|9916|(2, 160)|var|float64
var_9917 = relay.var("var_9917", dtype = "uint64", shape = (660,))#candidate|9917|(660,)|var|uint64
output = func_9909(var_9910,var_9911,var_9912,var_9913,var_9914,var_9915,var_9916,var_9917,)
func_9918 = relay.Function([var_9910,var_9911,var_9912,var_9913,var_9914,var_9915,var_9916,var_9917,], output)
mutated_mod['func_9918'] = func_9918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_9952 = func_8443_call()
call_9953 = func_8443_call()
output = call_9952
output2 = call_9953
func_9974 = relay.Function([], output)
mod['func_9974'] = func_9974
mod = relay.transform.InferType()(mod)
output = func_9974()
func_9975 = relay.Function([], output)
mutated_mod['func_9975'] = func_9975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8959_call = mod.get_global_var('func_8959')
func_8961_call = mutated_mod.get_global_var('func_8961')
call_10033 = relay.TupleGetItem(func_8959_call(), 0)
call_10034 = relay.TupleGetItem(func_8961_call(), 0)
output = call_10033
output2 = call_10034
func_10035 = relay.Function([], output)
mod['func_10035'] = func_10035
mod = relay.transform.InferType()(mod)
mutated_mod['func_10035'] = func_10035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10035_call = mutated_mod.get_global_var('func_10035')
call_10036 = func_10035_call()
output = call_10036
func_10037 = relay.Function([], output)
mutated_mod['func_10037'] = func_10037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_10046 = relay.TupleGetItem(func_8014_call(), 0)
call_10047 = relay.TupleGetItem(func_8016_call(), 0)
const_10049 = relay.const([[[1.425822,-6.551949,-3.108435,5.977241,-1.485582,-4.027068,-3.640826,6.756061,-4.899435,-7.816553,-3.664670],[-3.644129,6.897029,-5.825397,6.167945,6.385970,3.981477,-4.238426,-1.717460,5.228686,-1.574742,-5.619912],[3.492172,4.314353,2.315778,-9.346120,4.526951,9.334576,9.538401,-0.216374,7.639073,8.928601,2.043824],[-7.356139,5.018092,2.297488,-3.575844,4.647416,5.943419,0.703468,-6.370852,-5.002488,-1.288235,-2.576483],[9.904352,-2.029215,4.031881,8.623952,-9.728241,-6.412572,1.155669,7.545820,3.108928,-2.887676,1.488997],[4.645368,3.862659,-9.473797,-9.549772,9.068565,3.831643,-5.856092,-2.885282,-2.446200,-5.644427,-7.525905],[-5.813982,9.547476,-3.591002,-8.365034,7.058256,-7.395563,-1.605781,-6.894107,9.308625,-7.754319,3.578220],[3.669304,3.635868,-2.989349,-7.591170,2.941701,-4.698180,-7.944621,-0.324963,0.021556,4.187751,-6.214888],[-3.694475,-7.612548,0.746532,-6.330971,1.477724,-9.922054,7.976609,-0.494564,5.699805,-0.091623,-5.370108],[1.775877,-6.356144,-5.595231,-1.612468,3.447907,5.727646,-3.701178,-2.106509,-5.482685,1.292477,-5.348959],[2.098267,-9.269443,6.059188,8.362192,-7.833628,-7.236563,0.772256,-2.528120,-4.223613,-6.382302,3.488565],[-6.033076,4.593827,5.193603,9.791797,-3.897238,1.134018,3.859444,1.047755,-5.350071,2.796241,-5.235161],[-3.234122,-7.873309,-9.433806,-6.514442,-8.596533,-3.056366,9.736112,-0.531239,8.629028,-5.538545,1.171088],[6.854353,-7.141870,-8.720491,6.436655,-8.481228,1.684750,-5.617466,7.468383,5.153454,0.627140,5.858629],[-7.471598,9.673241,-6.771298,-9.362929,4.318892,2.175245,8.780126,-7.728759,-3.511226,-9.421203,3.027934]],[[-0.857123,-1.969835,-3.069299,5.723075,-0.603929,9.457744,2.125206,1.531759,-1.995291,-4.103451,-8.021652],[2.221492,-7.580247,8.727011,-4.327777,5.793666,0.241945,-8.437697,4.742401,-4.467232,3.623479,2.927477],[4.842216,-1.162894,3.288446,1.590117,9.309108,-8.937033,2.768808,-5.902505,2.450941,-3.944967,0.228016],[-1.054472,-1.238591,1.374271,1.838855,-7.281356,4.987568,-8.216615,2.520789,1.333098,-1.551690,-4.052760],[5.591814,6.944936,-9.602011,-4.479969,4.088760,-5.074885,1.623995,5.958697,-4.923403,6.029378,2.882941],[1.520617,-0.624940,7.916003,-9.040536,-3.607995,-5.502564,-1.510074,5.337774,6.790751,-8.174813,-4.615839],[2.359160,-2.503820,9.246954,5.824404,5.785191,-0.567358,1.968100,-4.683044,1.762636,-9.497771,1.821779],[1.666391,6.372644,3.030442,-2.228046,6.076832,0.600119,-4.497444,2.986907,6.182545,-1.456007,-2.833228],[6.429074,3.651479,3.639265,1.623698,8.758428,8.664886,2.369135,-1.768071,-1.059543,2.616598,8.764554],[3.497332,5.944263,2.609645,-2.295429,-1.790462,-3.538756,-8.748599,5.904256,-2.502528,-9.420442,7.814715],[-1.194505,-2.420420,4.527188,2.544940,6.771741,1.069681,1.672910,-1.825641,4.018729,-6.448335,-8.018981],[8.718951,-1.547344,-7.326877,-7.259751,-7.380841,8.079073,3.535984,-1.145364,1.272224,7.173498,-0.448947],[1.825655,-0.129174,9.651314,6.848824,-3.409553,6.852856,-2.012272,8.927143,4.586621,-8.494261,-7.586523],[4.738163,-6.383321,-0.357542,-1.744329,-5.272800,8.516769,-2.160473,7.731110,6.493057,-7.841636,-1.928903],[-6.438711,4.673351,8.396629,2.615436,-4.347506,-0.100541,6.290488,-9.422581,-8.566122,-5.885844,-0.528954]]], dtype = "float32")#candidate|10049|(2, 15, 11)|const|float32
bop_10050 = relay.equal(call_10046.astype('bool'), relay.reshape(const_10049.astype('bool'), relay.shape_of(call_10046))) # shape=(2, 15, 11)
bop_10053 = relay.equal(call_10047.astype('bool'), relay.reshape(const_10049.astype('bool'), relay.shape_of(call_10047))) # shape=(2, 15, 11)
func_5642_call = mod.get_global_var('func_5642')
func_5648_call = mutated_mod.get_global_var('func_5648')
const_10057 = relay.const(False, dtype = "bool")#candidate|10057|()|const|bool
const_10058 = relay.const([[False,False,False],[True,True,False],[True,False,False],[False,True,True],[True,False,False],[False,False,False],[False,True,True],[False,True,False],[False,False,False],[False,False,True],[True,False,True],[True,False,False],[True,True,False],[True,True,False],[False,False,False],[True,False,True],[True,True,False],[False,True,True],[False,True,True],[False,False,False],[True,True,False],[True,False,False],[True,True,False],[False,True,True],[False,True,False],[False,False,False],[True,False,True],[True,False,False],[False,True,False],[False,True,False],[False,True,True],[False,False,True],[True,True,False],[True,True,True],[False,True,True],[False,False,True],[True,True,True],[False,True,False],[True,True,True]], dtype = "bool")#candidate|10058|(39, 3)|const|bool
var_10059 = relay.var("var_10059", dtype = "bool", shape = (1, 702))#candidate|10059|(1, 702)|var|bool
var_10060 = relay.var("var_10060", dtype = "float32", shape = (33, 4))#candidate|10060|(33, 4)|var|float32
const_10061 = relay.const([-2,-6,6,-7,5,-1,-7,-3,4,-3,6,1,4,-4,-1,-2,9,7,-9,10,-10,-8,-7,-3,-7,-3,10,1,-8,-10,6,-3,-7,2,5,-4,4,1,3,4,2,2,-3,-8,8,3,-10,-8,-7,5,-2,-10,-10,-2,6,-2,-5,-2,7,-1,-8,8,-1,6,-9,-3,-9,9,-3,-4,-7,7,1,8,9,-3,-4,-6,-1,4,-3,-9,7,4,9,8,2,-7,7,1,7,-5,-8,5,-3,-7,5,1,-6,-1,-2,-2,-4,-9,4,-9,5,9,6,3,4,-10,-6,10,-5,-8,10,3,-6,-7,4,9,-1,-7,6,-8,9,-1,8,-8,2,10,-5,6,-7,2,-8,-5,3,5,1,10,-1,5,-2,-2,1,8,7,7,-8,9,4,-6,5,6,7,6,-7,-9,5,5,5,2,-9,8,-10,3,1,10,-1,4,2,-7,-10,-2,-8,-1,-10,5,-1,-7,1,6,-9,10,3,-9,-5,-6,3,-1,4,-3,4,6,-2,8,-4,7,-1,5,-2,-10,1,3,-3,4,-8,-6,7,-8,6,4,10,-3,-10,-6,-3,1,-4,7,-1,-9,-7,1,-6,5,-7,-1,-10,-10,3,5,4,-1,2,-8,-8,-2,-1,-3,4,-8,-6,-7,-3,9,5,-3,9,7,-1,-4,3,8,-1,-10,6,7,9,2,-3,2,-4,6,1,5,-2,3,-7,9,1,-4,-9,2,-8,-2,5,8,-10,-5,2,3,8,-9,-10,-2,8,-7,-8,-7,-3,-9,2,10,-4,3,4,9,-5,-7,-5,-5,7,-1,2,3,-8,6,2,4,-2,3,4,-7,10,-3,5,9,-1,-8,10,-8,4,8,1,-3,8,8,7,10,-1,4,2,-5,8,6,5,-6,-2,-6,-6,-6,4,-8,-9,-8,-5,6,8,10,7,1,4,2,4,6,4,6,-8,-8,-5,9,1,-7,7,2,-7,-5,-4,4,-2,8,4,5,-10,-9,1,7,3,8,5,-3,7,-1,4,7,-6,3,2,-2,-3,1,10,6,4,-3,-8,-9,-6,-3,8,6,8,-5,-9,5,9,8,2,5,9,-4,6,-1,-8,3,-6,-9,10,7,1,3,-5,-3,4,4,-8,2,6,6,-8,7,10,2,-9,9,-8,2,-3,2,-3,-5,-7,-4,-10,6,-1,-4,10,-1,5,-1,-4,6,-9,7,7,2,-8,-8,1,6,10,3,8,-10,-5,3,5,-7,2,-6,-7,-4,7,5,9,-9,3,-10,7,-3,-3,2,-8,4,-4,-10,3,5,-7,7,4,-4,10,-8,-5,1,-7,-10,3,-6,6,-7,-7,8,-5,-1,-3,-5,-10,1,-2,-5,-9,-6,9,-1,-6,-6,3,1,1,6,-7,-6,-4,4,3,-6,4,-7,4,10,8,-6,-1,10,7,5,-7,-2,-10,-6,6,7,6,5,-2,1,-2,-1,-4,-3,7,6,1,-6,4,5,-5,-10,-4,10,-9,-6,-8,1,9,10,4,-1,-3,7,8,7,-2,-2,-1,4,3,-10,8,10,7,-5,-7,-7,3,8,-6,3,-2,-6,-9,-3,-2,-1,4,2,-5,-6,3,-3,-9,-6,-7,-5,-7,-4,-3,7,1,10,3,-9,-6,9,10,6,6,-4,-2,-4,10,-3,6,-10,2,-4,-9,3,10,7,-5,-1,4,4,4,6,7,-9,-1,-9,9,10,-6,5,5,8,-6,1,-4,-7,6,-6,-5,7], dtype = "uint64")#candidate|10061|(660,)|const|uint64
call_10056 = relay.TupleGetItem(func_5642_call(relay.reshape(const_10057.astype('bool'), []), relay.reshape(const_10058.astype('bool'), [13, 9]), relay.reshape(var_10059.astype('bool'), [702,]), relay.reshape(var_10060.astype('float32'), [132,]), relay.reshape(const_10061.astype('uint64'), [660,]), ), 0)
call_10062 = relay.TupleGetItem(func_5648_call(relay.reshape(const_10057.astype('bool'), []), relay.reshape(const_10058.astype('bool'), [13, 9]), relay.reshape(var_10059.astype('bool'), [702,]), relay.reshape(var_10060.astype('float32'), [132,]), relay.reshape(const_10061.astype('uint64'), [660,]), ), 0)
output = relay.Tuple([bop_10050,call_10056,const_10057,const_10058,var_10059,var_10060,const_10061,])
output2 = relay.Tuple([bop_10053,call_10062,const_10057,const_10058,var_10059,var_10060,const_10061,])
func_10091 = relay.Function([var_10059,var_10060,], output)
mod['func_10091'] = func_10091
mod = relay.transform.InferType()(mod)
mutated_mod['func_10091'] = func_10091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10091_call = mutated_mod.get_global_var('func_10091')
var_10093 = relay.var("var_10093", dtype = "bool", shape = (1, 702))#candidate|10093|(1, 702)|var|bool
var_10094 = relay.var("var_10094", dtype = "float32", shape = (33, 4))#candidate|10094|(33, 4)|var|float32
call_10092 = func_10091_call(var_10093,var_10094,)
output = call_10092
func_10095 = relay.Function([var_10093,var_10094,], output)
mutated_mod['func_10095'] = func_10095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9974_call = mod.get_global_var('func_9974')
func_9975_call = mutated_mod.get_global_var('func_9975')
call_10112 = func_9974_call()
call_10113 = func_9974_call()
output = relay.Tuple([call_10112,])
output2 = relay.Tuple([call_10113,])
func_10119 = relay.Function([], output)
mod['func_10119'] = func_10119
mod = relay.transform.InferType()(mod)
output = func_10119()
func_10120 = relay.Function([], output)
mutated_mod['func_10120'] = func_10120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8088_call = mod.get_global_var('func_8088')
func_8089_call = mutated_mod.get_global_var('func_8089')
call_10155 = relay.TupleGetItem(func_8088_call(), 0)
call_10156 = relay.TupleGetItem(func_8089_call(), 0)
output = relay.Tuple([call_10155,])
output2 = relay.Tuple([call_10156,])
func_10157 = relay.Function([], output)
mod['func_10157'] = func_10157
mod = relay.transform.InferType()(mod)
mutated_mod['func_10157'] = func_10157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10157_call = mutated_mod.get_global_var('func_10157')
call_10158 = func_10157_call()
output = call_10158
func_10159 = relay.Function([], output)
mutated_mod['func_10159'] = func_10159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_10163 = func_8443_call()
call_10164 = func_8443_call()
output = relay.Tuple([call_10163,])
output2 = relay.Tuple([call_10164,])
func_10165 = relay.Function([], output)
mod['func_10165'] = func_10165
mod = relay.transform.InferType()(mod)
mutated_mod['func_10165'] = func_10165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10165_call = mutated_mod.get_global_var('func_10165')
call_10166 = func_10165_call()
output = call_10166
func_10167 = relay.Function([], output)
mutated_mod['func_10167'] = func_10167
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9004_call = mod.get_global_var('func_9004')
func_9005_call = mutated_mod.get_global_var('func_9005')
call_10226 = relay.TupleGetItem(func_9004_call(), 0)
call_10227 = relay.TupleGetItem(func_9005_call(), 0)
output = call_10226
output2 = call_10227
func_10237 = relay.Function([], output)
mod['func_10237'] = func_10237
mod = relay.transform.InferType()(mod)
mutated_mod['func_10237'] = func_10237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10237_call = mutated_mod.get_global_var('func_10237')
call_10238 = func_10237_call()
output = call_10238
func_10239 = relay.Function([], output)
mutated_mod['func_10239'] = func_10239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_10257 = relay.TupleGetItem(func_9014_call(), 1)
call_10258 = relay.TupleGetItem(func_9016_call(), 1)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_10267 = relay.var("var_10267", dtype = "bool", shape = (1, 117))#candidate|10267|(1, 117)|var|bool
var_10268 = relay.var("var_10268", dtype = "bool", shape = (702,))#candidate|10268|(702,)|var|bool
var_10269 = relay.var("var_10269", dtype = "float32", shape = (132,))#candidate|10269|(132,)|var|float32
var_10270 = relay.var("var_10270", dtype = "uint64", shape = (660,))#candidate|10270|(660,)|var|uint64
call_10266 = relay.TupleGetItem(func_2538_call(relay.reshape(var_10267.astype('bool'), [9, 13, 1]), relay.reshape(var_10268.astype('bool'), [9, 13, 6]), relay.reshape(call_10257.astype('float32'), [320,]), relay.reshape(var_10269.astype('float32'), [132,]), relay.reshape(var_10270.astype('uint64'), [330, 2]), ), 2)
call_10271 = relay.TupleGetItem(func_2544_call(relay.reshape(var_10267.astype('bool'), [9, 13, 1]), relay.reshape(var_10268.astype('bool'), [9, 13, 6]), relay.reshape(call_10257.astype('float32'), [320,]), relay.reshape(var_10269.astype('float32'), [132,]), relay.reshape(var_10270.astype('uint64'), [330, 2]), ), 2)
uop_10292 = relay.log2(var_10268.astype('float64')) # shape=(702,)
output = relay.Tuple([call_10257,call_10266,var_10267,var_10269,var_10270,uop_10292,])
output2 = relay.Tuple([call_10258,call_10271,var_10267,var_10269,var_10270,uop_10292,])
func_10300 = relay.Function([var_10267,var_10268,var_10269,var_10270,], output)
mod['func_10300'] = func_10300
mod = relay.transform.InferType()(mod)
var_10301 = relay.var("var_10301", dtype = "bool", shape = (1, 117))#candidate|10301|(1, 117)|var|bool
var_10302 = relay.var("var_10302", dtype = "bool", shape = (702,))#candidate|10302|(702,)|var|bool
var_10303 = relay.var("var_10303", dtype = "float32", shape = (132,))#candidate|10303|(132,)|var|float32
var_10304 = relay.var("var_10304", dtype = "uint64", shape = (660,))#candidate|10304|(660,)|var|uint64
output = func_10300(var_10301,var_10302,var_10303,var_10304,)
func_10305 = relay.Function([var_10301,var_10302,var_10303,var_10304,], output)
mutated_mod['func_10305'] = func_10305
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10318 = relay.const([[[9.018814,-0.670056,-3.629713,7.243817,-7.551635,5.624564,2.544012],[-2.346033,-2.444311,-8.348645,-1.884569,1.321122,5.199990,-3.805565],[3.685478,7.774117,-9.146204,8.396503,-2.834309,3.660590,-4.515308],[1.465714,-4.360424,9.424556,-9.699161,-7.467905,7.137188,-6.420321],[2.610757,4.842777,7.882270,3.267809,-1.383152,-4.691833,8.026305],[-4.406989,-7.413623,-9.672182,0.456571,-7.013046,4.273481,-0.447882]],[[-4.150628,2.691003,-8.043983,6.745175,2.655173,3.517158,9.612745],[-4.408363,-4.248424,-4.328281,-0.987795,6.681142,7.448147,-8.285143],[-9.080870,3.264596,6.188637,-3.686644,4.960873,6.745716,4.646381],[-5.455384,4.981387,9.630420,5.394516,-8.939600,-8.157371,-4.726283],[2.944394,-2.709988,6.784526,5.767512,1.289349,-1.704948,1.872150],[9.357832,4.502126,9.510039,5.074656,-5.767751,7.945591,-1.167352]],[[-4.383783,4.279953,5.406144,1.533972,8.449586,-6.824122,-2.194207],[0.833627,-2.658105,-2.212412,-3.354036,-3.716724,1.532415,7.708598],[-2.813937,-9.614937,-7.187951,-8.475215,-0.043870,-3.835029,-0.946112],[-3.340102,-0.062328,-7.816663,-4.153572,-0.106278,5.951988,-2.731950],[5.187817,4.140110,-4.475275,-7.029445,2.063899,-2.228145,-5.113224],[9.847049,7.452178,1.751176,0.656730,7.774612,0.135805,-3.743879]],[[-9.546140,2.215545,-3.833071,6.391645,-4.668020,2.167796,2.612072],[0.080440,3.462826,-7.262143,-3.417854,-8.272112,-3.931609,-5.567425],[6.211875,-7.957555,8.188181,6.685099,-9.187141,-5.289583,-8.106244],[-2.771928,-1.538112,3.748464,-9.096480,-1.615916,9.787901,-4.220316],[-9.786992,2.269728,6.689758,-5.833880,4.688609,7.250940,-2.872432],[0.489746,7.710355,-0.141472,6.638889,0.014156,-8.156244,3.632570]],[[-5.018835,8.589830,-6.464089,-5.408075,-8.359965,-4.924087,-7.257938],[5.433986,-0.544365,3.407177,-7.126254,9.130483,7.776758,7.714294],[-2.359745,-5.385409,-4.637263,-9.610739,-4.616731,-2.409926,6.823174],[7.974757,-3.406716,-6.022787,5.941980,6.271694,-4.362667,0.516072],[7.533869,6.690650,5.226272,3.802401,7.946770,-2.667571,-8.729668],[-6.829534,-4.910066,-3.948221,-3.678119,9.966960,-1.829036,2.761009]]], dtype = "float64")#candidate|10318|(5, 6, 7)|const|float64
uop_10319 = relay.sinh(const_10318.astype('float64')) # shape=(5, 6, 7)
output = relay.Tuple([uop_10319,])
output2 = relay.Tuple([uop_10319,])
func_10325 = relay.Function([], output)
mod['func_10325'] = func_10325
mod = relay.transform.InferType()(mod)
output = func_10325()
func_10326 = relay.Function([], output)
mutated_mod['func_10326'] = func_10326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10237_call = mod.get_global_var('func_10237')
func_10239_call = mutated_mod.get_global_var('func_10239')
call_10351 = func_10237_call()
call_10352 = func_10237_call()
output = call_10351
output2 = call_10352
func_10374 = relay.Function([], output)
mod['func_10374'] = func_10374
mod = relay.transform.InferType()(mod)
mutated_mod['func_10374'] = func_10374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10374_call = mutated_mod.get_global_var('func_10374')
call_10375 = func_10374_call()
output = call_10375
func_10376 = relay.Function([], output)
mutated_mod['func_10376'] = func_10376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_10385 = relay.TupleGetItem(func_8014_call(), 0)
call_10386 = relay.TupleGetItem(func_8016_call(), 0)
func_7743_call = mod.get_global_var('func_7743')
func_7752_call = mutated_mod.get_global_var('func_7752')
const_10410 = relay.const(-9, dtype = "uint16")#candidate|10410|()|const|uint16
const_10411 = relay.const([8,10,4,4,3,7,-2,-9,6,10,10,-3,-1,7,5,-4,5,-6,2,-7,7,-5,3,-4,4,2,-7,8,-1,1,6,-10,1,-8,-7,8,-8,-2,8,9,-8,-5,5,7,10,-1,-5,-5,-8,-9,-7,8,-3,6,4,3,-8,1,10,1,-7,-6,5,9,4,8,-7,7,-9,-1,-10,-9,3,-4,-7,4,-9,-8,-2,10,7,9,6,-5,-1,-10,-3,1,-8,-8,2,-10,-2,7,-7,10,-7,-7,-5,10,1,6,8,1,-2,2,10,-5,2,4,1,3,-3,10,5,5,-9,-1,8,-4,10,4,-10,2,-3,3,-2,-9,-7,4,-1,9,10,9,-1,-10,-1,-10,-5,4,9,-1,4,-8,1,2,-1,-1,10,-10,-5,3,-7,8,5,10,-9,-7,-3,5,-6,-5,7,-9,10,-9,2,-10,5,10,9,-8,-1,3,-7,-9,3,-10,-3,-9,-2,5,-2,-2,-2,1,-2,-10,-1,8,-9,-2,2,5,3,-6,6,-9,-8,-7,3,10,4,-10,-2,4,-7,6,-8,-5,-6,-6,-4,-1,5,-3,-6,6,4,7,-8,7,-5,7,3,4,4,-4,-6,1,4,2,10,10,-7,9,-7,-1,1,-6,9,-6,4,1,6,3,-7,-10,4,10,8,-7,10,-7,-7,5,-7,-8,10,10,3,-6,8,-9,9,-2,-3,-1,-6,-1,-3,8,7,10,-9,-5,-4,5,10,-4,7,5,-6,2,9,6,2,-4,2,-8,4,5,8,-10,6,-7,-2,3,-1,10,10,3,-10,1,-1,-4,4,-3,-9,-9,8,10,-10,-8,9,2,3,-1,10,-4,-1,-6,-8,-5,3,-4,2,3,-8,-3,-6,-6,10,-2,9,1,-6,3,7,9,-4,5,6,7,6,2,-7,-2,8,-7,-2,7,9,-10,-9,-8,-3,-10,10,6,9,9,8,3,7,-3,2,7,-9,8,9,3,-1,-4,2,5,7,9,7,-9,2,3,1,5,-10,-10,-1,2,7,10,-5,-3,1,6,-4,4,9,1,-9,10,1,8,-4,-1,4,2,-8,-2,9,-1,-2,-8,-2,1,-7,-1,-2,8,7,8,-5,-3,-7,6,-10,8,9,5,7,3,6,2,-2,5,-4,-1,5,-1,-8,8,-3,-1,4,-6,-9,-5,-4,4,-9,-3,4,-9,-9,-1,9,-4,8,5,-1,-5,1,-9,8,8,4,10,9,-5,2,-7,7,-3,9,9,10,-10,5,-3,3,-10,-5,5,10,4,5,-2,3,7,3,9,9,4,1,7,-9,2,-7,-9,6,8,-5,4,-6,-7,9,2,-9,4,-4,-5,7,-8,-6,-3,10,-4,2,2,-10,-8,-7,7,-9,-8,-1,7,-4,-4,3,1,-9,-8,-2,8,1,1,8,-6,10,-9,10,-10,-10,3,4,-7,-10,3,-7,-5,8,-8,5,-3,-9,3,8,-4,-10,2,-2,6,-7,-5,1,-3,-8,-7,-5,6,-3,-3,-4,9,-3,-7,-1,-8,-1,1,5,-5,6,-3,-2,-5,8,6,-5,8,-6,-3,-8,-3,4,-3,1,9,9,8], dtype = "uint16")#candidate|10411|(600,)|const|uint16
const_10412 = relay.const([[-6.813580],[4.632010],[2.125055],[-1.418730],[8.871437],[1.172942],[0.857400],[9.940473],[-2.112261],[9.836872],[5.609393],[8.876045],[-2.380392],[1.492173],[-9.693797],[7.748570],[-6.626060],[-6.267611],[4.141466],[6.749286],[5.325458],[1.645690],[9.627779],[6.636059],[-8.422861],[1.562963],[-1.212338],[-6.455784],[3.019876],[-4.808286],[1.464675],[-1.237649],[-8.361926],[-1.771869],[-4.962161],[-9.575346],[-9.371914],[-8.719322],[-3.846482],[9.679450],[-2.421081],[8.089290],[6.184332],[6.764830],[3.183823],[-5.828419],[-4.849416],[-6.158512],[-2.956562],[-6.710747],[-4.076577],[-7.990476],[9.072852],[-6.230522],[-4.105177],[-9.057955],[-5.876250],[1.574317],[5.246103],[2.142359],[-7.761569],[6.448232],[-6.152960],[5.580240],[-9.496031],[8.770699],[-3.036367],[6.355507],[6.929523],[-0.144141],[8.618795],[-8.840860],[-9.149305],[-8.854817],[9.159755],[-0.506052],[5.430013],[-7.344648],[3.290785],[-4.101202],[6.929915],[-6.117899],[1.744316],[1.907919],[6.316414],[-0.780298],[-6.779473],[-2.485743],[4.550174],[-2.554475],[-5.156816],[-0.272229],[5.326602],[-3.477633],[6.268221],[-3.791776],[-2.071350],[-3.202883],[9.525683],[-3.175832],[4.522970],[4.809980],[-4.762679],[-0.828643],[-9.195036],[-3.993238],[1.389589],[2.484916],[8.338945],[5.216881],[-0.394757],[7.944397],[-6.989233],[8.104045],[-4.418531],[-2.018962],[-6.501571],[6.076012],[-7.004245],[-7.500889],[2.948952],[2.683662],[-5.215329],[2.025895],[-4.860188],[-4.151188],[-5.039503],[-8.068122],[1.814048],[-3.645064],[0.773714],[-6.578260],[5.343701],[-7.875425],[3.741178],[-7.642077],[3.282295],[-8.525558],[-0.630146],[4.844603],[-9.749719],[-5.350517],[-2.716012],[-2.459941],[-8.046999],[1.896142],[0.266225],[3.851602],[5.070766],[-1.254421],[6.026109],[9.750024],[0.859773],[-7.881332],[5.751490],[-2.961171],[2.627852],[1.307551],[1.654247],[4.289125],[-9.146689],[-8.953399],[-1.704680],[-6.623072],[8.661596],[7.125269],[-8.158525],[-6.478411],[-9.114949],[3.867373],[-8.377130],[5.343711],[-8.984676],[4.670578],[-0.254763],[0.106967],[2.173065],[6.310481],[-4.872026],[-6.331976],[-6.940147],[-0.775875],[-6.464232],[-8.940459],[4.532744],[3.541158],[-5.493023],[6.946783],[3.368815],[-3.986596],[4.735580],[-6.908865],[8.953681],[8.889176],[-4.289512],[-5.593525],[4.070260],[1.849111],[1.543218],[-8.416272],[1.927892],[-9.025793],[-4.639680],[8.809489],[0.175727],[-6.747408],[2.574421],[7.672368],[-7.777529],[-6.211529],[-0.064533],[6.490799],[9.645563],[-9.048151],[9.622782],[7.295957],[-0.411736],[-6.802106],[5.617900],[-5.549740],[5.177831],[-2.390723],[6.998905],[-7.293922],[-2.793240],[-3.863233],[8.780933],[-0.698699],[-2.521310],[0.753932],[2.038850],[4.701403],[-7.121705],[-0.658439],[8.603717],[-5.253721],[5.130691],[6.201169],[9.519982],[-9.909477]], dtype = "float32")#candidate|10412|(240, 1)|const|float32
const_10413 = relay.const([[3.120043,4.805939],[9.957288,-3.998422],[-4.517975,-8.202761],[-7.229143,2.432565],[-8.187415,8.095773],[-8.549200,3.788535],[-7.714733,0.658440],[9.518162,9.467252],[3.512221,9.250288],[4.719693,2.865500],[6.195056,1.893478],[7.016514,-8.547978],[9.961808,4.941208],[-6.867287,1.938591],[4.097987,-1.430988],[8.264408,-1.983098],[-1.925839,4.461406],[6.859330,-2.081888],[-0.546559,-7.086127],[-3.594843,5.505266],[5.005953,9.931218],[-0.383565,-2.351194],[-9.867565,-8.408919],[5.403879,-0.701036],[6.380523,4.172417],[-0.613844,2.084724],[9.654915,-0.313257],[-7.368814,-5.047630],[-9.293322,-4.113958],[-1.770728,3.185144],[4.745725,-8.499783],[-6.041704,-9.259989],[-7.466771,-7.350643],[8.830911,5.070223],[0.946146,9.520596],[4.868004,0.117735],[8.405830,-9.989730],[2.267949,-2.303225],[-2.542339,0.846010],[6.220519,-9.493132],[2.093147,-1.475269],[-6.977162,-4.106894],[3.141515,3.809565],[8.678593,9.384970],[-3.480604,-2.610655],[6.231683,-4.286757],[6.959554,-9.201160],[-9.250060,-7.673102],[5.967853,-3.143397],[-6.939616,6.363285],[-3.610811,-3.582819],[-7.142921,3.746383],[-6.540191,-9.490929],[-4.842745,9.054907],[-6.901941,7.830779],[-4.190568,-1.901047],[-8.737102,6.235860],[1.408075,7.617175],[7.939543,1.115911],[7.018214,3.723425],[-9.407692,4.027281],[-1.231271,-8.441605],[-9.403174,8.206529],[4.389044,-5.479747],[2.367114,-3.905446],[-8.028339,-7.204963],[-2.626318,0.826412],[-8.128277,1.976853],[-6.775555,-2.302356],[0.374540,9.744663],[-8.937847,-5.640258],[4.578995,8.047535],[-1.007058,2.899822],[0.001846,-8.243074],[-2.774641,0.086747],[-0.958790,1.599841],[6.487497,-7.734859],[6.345053,-5.143183],[-6.778742,6.546393],[7.694425,-9.180053],[3.045333,7.530672],[-1.263999,-2.619022],[8.291527,7.568010],[-5.916938,4.175710],[-8.010627,-0.304711],[1.276529,7.165078],[5.067043,0.417332],[-0.500383,-0.358236],[-0.220248,-2.886530],[2.575454,6.153551],[2.449854,2.062289],[3.802742,4.504467],[-6.256470,9.647369],[0.438030,3.049995],[-0.969543,7.672894],[6.690788,-6.054013],[1.555959,-2.378623],[3.537161,-3.500301],[-5.640288,-5.978941],[-7.495648,-1.847605],[4.334452,-0.432170],[-7.506950,6.472719],[4.721754,7.603700],[-1.351799,-8.645405],[3.108633,-8.412187],[-9.724074,7.438368],[-8.848880,-9.576857],[2.061509,1.617021],[3.445008,1.808981],[-1.290683,-1.688120],[-3.101868,-4.427393],[8.603137,-7.681980],[6.955634,0.760296],[1.620887,-4.052264],[-4.109053,-0.563518],[3.244502,-6.582751],[-5.703477,3.092160],[-7.209364,-0.465550],[5.229963,9.282838],[5.015974,8.939108],[-8.338131,-3.713032],[1.199387,-6.923498],[7.261375,-7.329915],[-9.282331,0.492250],[-6.761069,8.644965],[-5.267763,0.311228],[-4.671738,-3.942304],[1.980778,-7.660429],[-4.757882,3.792205],[-3.436502,1.996672],[5.753735,-9.900098],[-9.956180,-3.397592],[-1.402078,1.250475],[4.408492,3.691463],[6.754468,0.747612],[7.881640,2.219125],[-3.578869,-7.396305],[-1.784642,-6.750809],[5.346886,8.576685],[4.357843,-7.055336],[-7.956596,-9.138314],[5.475990,8.683882],[-3.435161,2.502862],[5.768831,1.275120],[5.768139,-7.674394],[-0.917235,1.416347],[7.889989,5.682196],[-0.913093,0.584978],[-6.780797,-5.263819],[9.920586,-8.914970],[-1.878087,6.914073],[-8.215447,3.237321],[-2.382068,7.484113],[2.335538,-7.985154],[-5.740590,4.043125],[-3.587681,2.694094],[-5.451706,-2.797844],[0.212589,8.391935],[-7.249065,8.415200],[-1.397686,-2.172074]], dtype = "float32")#candidate|10413|(160, 2)|const|float32
var_10414 = relay.var("var_10414", dtype = "float32", shape = (40,))#candidate|10414|(40,)|var|float32
const_10415 = relay.const([False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,True,True,False], dtype = "bool")#candidate|10415|(117,)|const|bool
const_10416 = relay.const([[-3.107435,-6.746005],[-5.230361,8.052360],[-6.221115,1.012690],[7.131023,-3.165353],[-2.272084,4.849505],[0.795393,-6.971121],[-7.291523,8.621754],[1.487484,1.578240],[4.573436,-6.000031],[-6.121049,8.204119],[2.474573,5.262865],[3.472569,3.386674],[-4.585392,-7.230742],[-7.432406,-9.121454],[-3.474173,7.034621],[-7.582721,-4.813562],[8.485638,3.632966],[-0.873564,-2.447193],[-8.289565,-9.040488],[-0.052914,8.551340],[-8.092036,-4.678724],[-5.707483,9.067605],[-1.598546,-3.347847],[7.311397,7.248054],[-8.491449,-6.983397],[9.684556,-6.500549],[5.948576,-9.021241],[-4.413467,-2.858368],[4.551792,1.211092],[-2.808257,7.965407],[2.731994,9.499688],[-6.094283,2.014355],[-3.724489,7.343220],[5.262117,0.045295],[-4.980870,-7.841944],[4.842519,8.650095],[7.387369,-6.609764],[1.525814,0.965936],[-8.034770,6.151448],[9.822935,0.640378],[-2.024268,4.733145],[-1.057275,-9.073124],[-4.467799,7.960757],[-5.941596,4.054275],[7.127174,8.344179],[6.144752,6.453227],[6.795982,-6.560500],[-6.790989,-9.063534],[-0.120291,-9.632082],[-8.394411,3.801578],[9.285769,-4.331531],[9.908578,0.924625],[-7.732420,5.628195],[1.551679,5.095445],[8.255481,5.269657],[4.464907,-5.782723],[-1.799936,-6.077327],[-9.167364,2.832184],[-7.075714,0.492901],[1.219054,-7.365301],[0.621334,7.109668],[-1.993853,5.228591],[-9.458812,5.166356],[7.445970,5.236393],[-8.383108,-6.865449],[2.527905,-6.367963]], dtype = "float32")#candidate|10416|(66, 2)|const|float32
var_10417 = relay.var("var_10417", dtype = "uint64", shape = (660,))#candidate|10417|(660,)|var|uint64
call_10409 = relay.TupleGetItem(func_7743_call(relay.reshape(const_10410.astype('uint16'), []), relay.reshape(const_10411.astype('uint16'), [5, 12, 10]), relay.reshape(const_10412.astype('float32'), [240,]), relay.reshape(const_10413.astype('float32'), [1, 320]), relay.reshape(var_10414.astype('float32'), [40, 1]), relay.reshape(const_10415.astype('bool'), [117,]), relay.reshape(const_10416.astype('float32'), [132,]), relay.reshape(var_10417.astype('uint64'), [1, 660]), ), 7)
call_10418 = relay.TupleGetItem(func_7752_call(relay.reshape(const_10410.astype('uint16'), []), relay.reshape(const_10411.astype('uint16'), [5, 12, 10]), relay.reshape(const_10412.astype('float32'), [240,]), relay.reshape(const_10413.astype('float32'), [1, 320]), relay.reshape(var_10414.astype('float32'), [40, 1]), relay.reshape(const_10415.astype('bool'), [117,]), relay.reshape(const_10416.astype('float32'), [132,]), relay.reshape(var_10417.astype('uint64'), [1, 660]), ), 7)
output = relay.Tuple([call_10385,call_10409,const_10410,const_10411,const_10412,const_10413,var_10414,const_10415,const_10416,var_10417,])
output2 = relay.Tuple([call_10386,call_10418,const_10410,const_10411,const_10412,const_10413,var_10414,const_10415,const_10416,var_10417,])
func_10419 = relay.Function([var_10414,var_10417,], output)
mod['func_10419'] = func_10419
mod = relay.transform.InferType()(mod)
mutated_mod['func_10419'] = func_10419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10419_call = mutated_mod.get_global_var('func_10419')
var_10421 = relay.var("var_10421", dtype = "float32", shape = (40,))#candidate|10421|(40,)|var|float32
var_10422 = relay.var("var_10422", dtype = "uint64", shape = (660,))#candidate|10422|(660,)|var|uint64
call_10420 = func_10419_call(var_10421,var_10422,)
output = call_10420
func_10423 = relay.Function([var_10421,var_10422,], output)
mutated_mod['func_10423'] = func_10423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_10475 = relay.TupleGetItem(func_8014_call(), 0)
call_10476 = relay.TupleGetItem(func_8016_call(), 0)
func_8644_call = mod.get_global_var('func_8644')
func_8645_call = mutated_mod.get_global_var('func_8645')
call_10477 = func_8644_call()
call_10478 = func_8644_call()
func_9555_call = mod.get_global_var('func_9555')
func_9562_call = mutated_mod.get_global_var('func_9562')
var_10486 = relay.var("var_10486", dtype = "float32", shape = (210,))#candidate|10486|(210,)|var|float32
var_10487 = relay.var("var_10487", dtype = "float64", shape = ())#candidate|10487|()|var|float64
const_10488 = relay.const([[False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False],[True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,True,False,False,True],[False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,False],[True,False,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False],[False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,False,True,True],[True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True]], dtype = "bool")#candidate|10488|(6, 117)|const|bool
var_10489 = relay.var("var_10489", dtype = "float64", shape = (392,))#candidate|10489|(392,)|var|float64
var_10490 = relay.var("var_10490", dtype = "float64", shape = (900,))#candidate|10490|(900,)|var|float64
call_10485 = relay.TupleGetItem(func_9555_call(relay.reshape(var_10486.astype('float32'), [210,]), relay.reshape(var_10487.astype('float64'), []), relay.reshape(const_10488.astype('bool'), [702,]), relay.reshape(var_10489.astype('float64'), [14, 28]), relay.reshape(var_10490.astype('float64'), [900,]), ), 18)
call_10491 = relay.TupleGetItem(func_9562_call(relay.reshape(var_10486.astype('float32'), [210,]), relay.reshape(var_10487.astype('float64'), []), relay.reshape(const_10488.astype('bool'), [702,]), relay.reshape(var_10489.astype('float64'), [14, 28]), relay.reshape(var_10490.astype('float64'), [900,]), ), 18)
output = relay.Tuple([call_10475,call_10477,call_10485,var_10486,var_10487,const_10488,var_10489,var_10490,])
output2 = relay.Tuple([call_10476,call_10478,call_10491,var_10486,var_10487,const_10488,var_10489,var_10490,])
func_10498 = relay.Function([var_10486,var_10487,var_10489,var_10490,], output)
mod['func_10498'] = func_10498
mod = relay.transform.InferType()(mod)
mutated_mod['func_10498'] = func_10498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10498_call = mutated_mod.get_global_var('func_10498')
var_10500 = relay.var("var_10500", dtype = "float32", shape = (210,))#candidate|10500|(210,)|var|float32
var_10501 = relay.var("var_10501", dtype = "float64", shape = ())#candidate|10501|()|var|float64
var_10502 = relay.var("var_10502", dtype = "float64", shape = (392,))#candidate|10502|(392,)|var|float64
var_10503 = relay.var("var_10503", dtype = "float64", shape = (900,))#candidate|10503|(900,)|var|float64
call_10499 = func_10498_call(var_10500,var_10501,var_10502,var_10503,)
output = call_10499
func_10504 = relay.Function([var_10500,var_10501,var_10502,var_10503,], output)
mutated_mod['func_10504'] = func_10504
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10520 = relay.var("var_10520", dtype = "int8", shape = (7, 3, 6))#candidate|10520|(7, 3, 6)|var|int8
var_10521 = relay.var("var_10521", dtype = "int8", shape = (7, 3, 6))#candidate|10521|(7, 3, 6)|var|int8
bop_10522 = relay.not_equal(var_10520.astype('bool'), relay.reshape(var_10521.astype('bool'), relay.shape_of(var_10520))) # shape=(7, 3, 6)
output = bop_10522
output2 = bop_10522
func_10527 = relay.Function([var_10520,var_10521,], output)
mod['func_10527'] = func_10527
mod = relay.transform.InferType()(mod)
var_10528 = relay.var("var_10528", dtype = "int8", shape = (7, 3, 6))#candidate|10528|(7, 3, 6)|var|int8
var_10529 = relay.var("var_10529", dtype = "int8", shape = (7, 3, 6))#candidate|10529|(7, 3, 6)|var|int8
output = func_10527(var_10528,var_10529,)
func_10530 = relay.Function([var_10528,var_10529,], output)
mutated_mod['func_10530'] = func_10530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10165_call = mod.get_global_var('func_10165')
func_10167_call = mutated_mod.get_global_var('func_10167')
call_10579 = relay.TupleGetItem(func_10165_call(), 0)
call_10580 = relay.TupleGetItem(func_10167_call(), 0)
func_8161_call = mod.get_global_var('func_8161')
func_8162_call = mutated_mod.get_global_var('func_8162')
call_10588 = relay.TupleGetItem(func_8161_call(), 2)
call_10589 = relay.TupleGetItem(func_8162_call(), 2)
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_10613 = relay.TupleGetItem(func_10157_call(), 0)
call_10614 = relay.TupleGetItem(func_10159_call(), 0)
func_3419_call = mod.get_global_var('func_3419')
func_3423_call = mutated_mod.get_global_var('func_3423')
var_10622 = relay.var("var_10622", dtype = "float64", shape = (14,))#candidate|10622|(14,)|var|float64
var_10623 = relay.var("var_10623", dtype = "float32", shape = (320,))#candidate|10623|(320,)|var|float32
call_10621 = relay.TupleGetItem(func_3419_call(relay.reshape(var_10622.astype('float64'), [7, 2, 1]), relay.reshape(var_10623.astype('float32'), [320,]), ), 3)
call_10624 = relay.TupleGetItem(func_3423_call(relay.reshape(var_10622.astype('float64'), [7, 2, 1]), relay.reshape(var_10623.astype('float32'), [320,]), ), 3)
func_5642_call = mod.get_global_var('func_5642')
func_5648_call = mutated_mod.get_global_var('func_5648')
var_10628 = relay.var("var_10628", dtype = "bool", shape = ())#candidate|10628|()|var|bool
var_10629 = relay.var("var_10629", dtype = "bool", shape = (117,))#candidate|10629|(117,)|var|bool
var_10630 = relay.var("var_10630", dtype = "bool", shape = (702,))#candidate|10630|(702,)|var|bool
var_10631 = relay.var("var_10631", dtype = "float32", shape = (132,))#candidate|10631|(132,)|var|float32
const_10632 = relay.const([7,-7,-9,-1,2,4,-6,4,9,6,5,-4,1,-6,-7,10,-7,7,10,10,4,7,-2,-8,3,4,5,6,-2,-10,3,7,8,5,-3,-3,8,7,-3,10,8,-3,-2,8,3,-6,-7,-6,8,7,6,-8,-10,-2,-1,-8,-6,3,-1,-1,6,-1,-10,-10,-8,-10,6,7,-5,8,1,7,8,5,-1,-4,-6,2,1,4,10,4,-4,-4,1,-4,-10,10,-1,9,-1,-10,9,-3,-5,-2,5,-3,-8,-7,-8,1,-4,-6,-4,-8,8,-4,-2,-7,-5,4,-4,8,-3,-9,6,1,-1,-4,3,-1,-9,-10,-3,-8,6,8,-10,-2,-1,-5,2,-4,4,7,-1,-10,5,-3,-7,-7,-4,4,1,-8,8,-9,1,1,-3,-7,-9,7,7,2,-3,-8,6,-1,-8,1,-4,4,6,-5,6,-3,8,-8,-2,-10,3,-1,8,8,-3,-1,1,-4,-1,-6,-10,-3,-1,-3,3,-7,1,-5,-10,-6,4,-9,3,2,4,-2,-6,-5,5,-1,3,-5,4,5,5,-6,-9,3,-2,-5,-10,-3,1,5,-9,-4,-2,9,1,9,-5,4,-4,5,10,2,-10,-8,6,7,-8,8,-2,-8,-10,10,4,9,-10,3,8,-2,4,-9,3,-4,9,-3,-8,7,-9,-3,-10,2,1,-2,1,-9,-5,-5,-4,-1,2,7,6,10,-10,8,-7,2,6,-9,7,1,-4,-10,5,5,-5,9,-8,-7,-2,-2,7,-9,7,9,-3,6,7,10,-9,-1,-9,8,-1,-8,1,-4,-4,-1,-10,-5,-1,4,8,1,-9,2,7,7,-4,-1,-7,-3,-9,-1,5,1,6,-3,9,2,8,-10,-3,-1,4,-3,-8,-1,1,5,8,9,3,-10,7,2,7,8,-9,-8,2,3,8,-8,-5,-2,-1,7,-6,-6,-9,6,-10,-6,5,1,5,-9,9,-9,-4,-7,5,-1,-1,4,7,5,-4,6,5,9,3,-3,7,7,5,6,-8,-1,-4,-8,-4,-8,-4,-10,-2,-8,-6,9,3,5,-2,9,8,8,6,-10,-8,9,-3,-8,-7,-1,-7,6,-8,9,-2,9,-8,-9,-2,-5,9,10,-2,-8,7,1,2,6,-8,10,-3,9,6,6,-1,8,-6,2,9,8,-1,-1,-6,-5,-4,-6,1,-10,5,5,-8,6,1,1,-9,-5,-8,7,5,-10,-4,6,4,-2,-2,5,-10,-2,-10,-9,2,3,-2,3,10,-4,2,2,6,6,-1,-7,-3,-1,4,4,-4,3,5,3,7,-2,7,-6,-7,2,3,-10,8,9,-1,-7,10,-1,4,-2,3,-2,7,-5,10,4,-7,-10,-4,-7,2,10,-4,6,-6,10,2,10,-10,4,2,-3,-10,4,-2,9,-6,5,-1,-5,1,6,7,-3,-3,-9,4,-4,5,-10,-10,10,-9,4,-7,-7,-6,10,-1,4,-9,-2,5,9,5,-6,10,1,-10,-7,5,5,-9,7,-9,7,-4,-3,5,8,3,5,9,-1,10,-7,-4,-8,-7,-2,-6,6,-7,10,3,10,-3,7,10,4,-8,6,-3,-2,9,-9,-4,-6,4,-3,-5,2,9,-3,-9,-8,8,-6,8,1,5,-2,-5,-2,-6,7,-7,3,-10,4,3,-6,-5,10,-4,1,-1,8,3,6,-4,-5,1,6,4,1,-1,-8,1,2,-1,5,-7,-1,-3,-4,-9,10,6,-3,8,-10,3,7], dtype = "uint64")#candidate|10632|(660,)|const|uint64
call_10627 = relay.TupleGetItem(func_5642_call(relay.reshape(var_10628.astype('bool'), []), relay.reshape(var_10629.astype('bool'), [13, 9]), relay.reshape(var_10630.astype('bool'), [702,]), relay.reshape(var_10631.astype('float32'), [132,]), relay.reshape(const_10632.astype('uint64'), [660,]), ), 1)
call_10633 = relay.TupleGetItem(func_5648_call(relay.reshape(var_10628.astype('bool'), []), relay.reshape(var_10629.astype('bool'), [13, 9]), relay.reshape(var_10630.astype('bool'), [702,]), relay.reshape(var_10631.astype('float32'), [132,]), relay.reshape(const_10632.astype('uint64'), [660,]), ), 1)
func_9630_call = mod.get_global_var('func_9630')
func_9635_call = mutated_mod.get_global_var('func_9635')
call_10637 = relay.TupleGetItem(func_9630_call(relay.reshape(var_10628.astype('bool'), []), relay.reshape(var_10629.astype('bool'), [117,]), relay.reshape(const_10632.astype('uint64'), [5, 132]), ), 1)
call_10638 = relay.TupleGetItem(func_9635_call(relay.reshape(var_10628.astype('bool'), []), relay.reshape(var_10629.astype('bool'), [117,]), relay.reshape(const_10632.astype('uint64'), [5, 132]), ), 1)
func_5642_call = mod.get_global_var('func_5642')
func_5648_call = mutated_mod.get_global_var('func_5648')
call_10648 = relay.TupleGetItem(func_5642_call(relay.reshape(var_10628.astype('bool'), []), relay.reshape(var_10629.astype('bool'), [13, 9]), relay.reshape(var_10630.astype('bool'), [702,]), relay.reshape(var_10631.astype('float32'), [132,]), relay.reshape(const_10632.astype('uint64'), [660,]), ), 5)
call_10649 = relay.TupleGetItem(func_5648_call(relay.reshape(var_10628.astype('bool'), []), relay.reshape(var_10629.astype('bool'), [13, 9]), relay.reshape(var_10630.astype('bool'), [702,]), relay.reshape(var_10631.astype('float32'), [132,]), relay.reshape(const_10632.astype('uint64'), [660,]), ), 5)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_10650 = func_8443_call()
call_10651 = func_8443_call()
output = relay.Tuple([call_10579,call_10588,call_10613,call_10621,var_10622,var_10623,call_10627,var_10628,var_10629,var_10630,var_10631,const_10632,call_10637,call_10648,call_10650,])
output2 = relay.Tuple([call_10580,call_10589,call_10614,call_10624,var_10622,var_10623,call_10633,var_10628,var_10629,var_10630,var_10631,const_10632,call_10638,call_10649,call_10651,])
func_10653 = relay.Function([var_10622,var_10623,var_10628,var_10629,var_10630,var_10631,], output)
mod['func_10653'] = func_10653
mod = relay.transform.InferType()(mod)
mutated_mod['func_10653'] = func_10653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10653_call = mutated_mod.get_global_var('func_10653')
var_10655 = relay.var("var_10655", dtype = "float64", shape = (14,))#candidate|10655|(14,)|var|float64
var_10656 = relay.var("var_10656", dtype = "float32", shape = (320,))#candidate|10656|(320,)|var|float32
var_10657 = relay.var("var_10657", dtype = "bool", shape = ())#candidate|10657|()|var|bool
var_10658 = relay.var("var_10658", dtype = "bool", shape = (117,))#candidate|10658|(117,)|var|bool
var_10659 = relay.var("var_10659", dtype = "bool", shape = (702,))#candidate|10659|(702,)|var|bool
var_10660 = relay.var("var_10660", dtype = "float32", shape = (132,))#candidate|10660|(132,)|var|float32
call_10654 = func_10653_call(var_10655,var_10656,var_10657,var_10658,var_10659,var_10660,)
output = call_10654
func_10661 = relay.Function([var_10655,var_10656,var_10657,var_10658,var_10659,var_10660,], output)
mutated_mod['func_10661'] = func_10661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10374_call = mod.get_global_var('func_10374')
func_10376_call = mutated_mod.get_global_var('func_10376')
call_10673 = func_10374_call()
call_10674 = func_10374_call()
output = relay.Tuple([call_10673,])
output2 = relay.Tuple([call_10674,])
func_10683 = relay.Function([], output)
mod['func_10683'] = func_10683
mod = relay.transform.InferType()(mod)
output = func_10683()
func_10684 = relay.Function([], output)
mutated_mod['func_10684'] = func_10684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8161_call = mod.get_global_var('func_8161')
func_8162_call = mutated_mod.get_global_var('func_8162')
call_10721 = relay.TupleGetItem(func_8161_call(), 1)
call_10722 = relay.TupleGetItem(func_8162_call(), 1)
output = call_10721
output2 = call_10722
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
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_10734 = relay.TupleGetItem(func_9014_call(), 2)
call_10735 = relay.TupleGetItem(func_9016_call(), 2)
func_8508_call = mod.get_global_var('func_8508')
func_8510_call = mutated_mod.get_global_var('func_8510')
var_10753 = relay.var("var_10753", dtype = "float64", shape = (280,))#candidate|10753|(280,)|var|float64
call_10752 = relay.TupleGetItem(func_8508_call(relay.reshape(var_10753.astype('float64'), [4, 10, 7])), 0)
call_10754 = relay.TupleGetItem(func_8510_call(relay.reshape(var_10753.astype('float64'), [4, 10, 7])), 0)
output = relay.Tuple([call_10734,call_10752,var_10753,])
output2 = relay.Tuple([call_10735,call_10754,var_10753,])
func_10760 = relay.Function([var_10753,], output)
mod['func_10760'] = func_10760
mod = relay.transform.InferType()(mod)
var_10761 = relay.var("var_10761", dtype = "float64", shape = (280,))#candidate|10761|(280,)|var|float64
output = func_10760(var_10761)
func_10762 = relay.Function([var_10761], output)
mutated_mod['func_10762'] = func_10762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_10785 = func_8443_call()
call_10786 = func_8443_call()
func_1926_call = mod.get_global_var('func_1926')
func_1928_call = mutated_mod.get_global_var('func_1928')
const_10796 = relay.const([-0.784829,-2.129053,-8.632356,0.765182,0.795181,5.641227,-0.495320,2.206809,-3.276985,1.742740,2.367494,-7.902064,-5.082275,-7.414199,7.382175,9.350452,-9.313866,-7.879436,-5.928380,-1.196593,-0.469440,2.995691,9.223794,6.133146,0.564095,2.186187,5.082162,2.102165,-8.679048,7.025770,-3.952172,1.881711,2.211529,8.281164,-2.187432,5.273542,-5.201845,8.930761,-3.447888,9.207898,3.650230,-0.671699,-2.345479,-3.011348,8.017258,-7.848845,-9.957120,4.588851,8.028095,-2.313161,-9.195800,-4.844226,-7.064980,-0.276369,4.970583,-5.883375,-5.644749,7.527449,8.237811,-3.122429,-1.293507,-6.000184,-4.514800,-7.396813,-0.164007,1.170420,-4.024079,0.468544,9.853650,1.986210,8.858100,-3.062567,4.518885,-9.004726,3.189503,0.060101,7.898200,6.275224,5.588793,2.421136,-6.577460,-3.635045,5.223830,6.138732,8.266758,1.786392,-6.366722,9.282333,4.520703,-2.656525,-8.952957,-2.734187,2.644303,3.685264,7.996705,6.085722,-7.713155,7.079123,5.279728,-9.149758,6.166080,-5.016496,2.064941,3.398565,5.159294,-1.591298,-9.281316,-0.816124,-7.965062,-8.320798,-3.323528,2.995804,-2.683254,-3.127385,9.433492,-4.451490,-1.250305,-0.385481,-4.118910,1.683920,-3.237315,2.958424,-5.295218,-3.297837,-5.467250,5.032883,-7.939355,3.316099,2.534259,6.324793,-9.311024,7.174839,-7.234658,5.622476,-8.941329,-1.973456,-7.761080,9.471450,2.860783,5.222723,-8.908636,1.637208,8.602113,4.044846,-7.287608,2.385134,2.955192,-3.938014,-5.745845,-8.816821,-8.849495,2.589825,3.029833,5.447948,5.020755,-9.792442,9.589022,-0.426006,-5.563352,4.221765,-7.785536,8.110352,-3.705793,3.669024,0.620892,2.180990,7.214732,-8.064988,7.185040,9.790714,-6.855744,-9.171511,8.070650,-0.868769,3.494516,0.281206,-2.270688,0.889943,-5.056175,-5.719238,-1.801308,2.389296,-2.912972,-2.919318,4.311938,-5.670713,2.931212,-9.488861,-3.750121,-7.948893,-5.246600,7.875506,6.004783,2.549960,-2.748043,7.167436,5.695019,-2.188865,1.917132,4.213647,-5.593029,-8.992917,8.441203,4.388667,-9.791822,9.749620,8.517389,2.862698,9.170783,-8.901564,-0.791531,-6.708060,-6.846097,-5.510918,-3.866002,-2.653208,9.448462,-9.180235,3.292184,-0.688408,-9.895875,5.720345,5.986226,-5.994534,7.305096,-4.422700,-8.199306,-4.998207,9.268958,-2.881195,-4.437947,-8.276502,-8.321283,-8.021557,-6.243942,2.840590,-5.923976,-7.031580,6.816280,-6.921740,7.090228,6.851454,-9.920254,-7.665949,-2.150119,6.852171,-7.210190,-0.656090,-1.056665,-5.857613,-3.570138,1.113258,-2.338932,-9.885795,-6.733548,2.421115,8.844802,-2.894840,-7.341635,7.417748,4.276284,0.888478,-3.811934,-4.448779,0.288886,-7.778080,-4.836364,-8.838114,3.322213,5.095512,-3.967724,-0.322892,3.302236,5.456172,4.541988,-7.835205,3.567095,-2.495391,8.007547,-0.028795,-7.408421,-9.065939,6.143180,4.653669,6.713498,-2.352633,6.388984,0.874964,5.032967,-2.610847,8.334454,-5.968613,5.602049,8.383054,6.166925,0.495088,-9.265369,7.021993,-1.822553,-6.063073,2.506025,5.841291,8.192578,2.711413,9.662231,-8.259974,-2.752276,1.318124,0.614006,-4.924768,6.386038,-5.655970,-7.698241,1.270267,6.566759,-5.821221,-8.077754,4.982061,9.317711,8.787657,4.831979,3.911282,-0.239944,7.827946,3.574627,-1.019589,3.344227,-8.954301,-1.164432,-7.418216,-5.032082,-2.657177,6.847065,-1.364481,-4.566545,0.005757,2.335532,7.071307,-1.991220,-5.553333,4.110142,-9.969296,4.834421,-9.611142,-3.959148,8.357846,4.800661,6.638283,-0.174964,5.238645,1.442143,-6.617263,-9.361925,-1.658718,-6.074858,-3.159122,-1.464801,-7.719318,-9.962510,3.152788,8.306176,7.284546,6.914867,9.147518,-4.541317,-9.755116,-4.299457,1.075029,8.998902,9.963372,-3.416902,9.660225,-1.580888,-6.111939,-1.600139,3.623259,0.212406,-0.559112,6.577420,-8.561891,4.544906,-3.891202,4.494528,-2.131708,6.260286,-1.823296,1.157308,-1.280373,4.453089,-4.508103,9.669054,1.766114,-0.272074,7.798808,-8.696479,-5.837043,-2.151654,7.170512,-6.731471,-8.986012,4.981336,5.928593,-7.458780,-0.019968,-9.123511,8.617317,-0.305939,-4.753117,5.330761,-5.197739,9.676620,8.025064,7.507202,0.243867,-5.930939,-1.911816,-8.167810,-7.093519,2.693135,-8.791267,-0.944559,2.418150,3.296196,5.502212,9.057230,-1.752909,-3.534702,3.377360,-1.438019,6.431723,-5.873236,-2.066107,4.998998,-0.726908,1.639297,1.748983,-0.757637,-3.317096,-3.198319,-7.630658,3.523338,9.281402,-8.586201,-2.183358,2.971301,1.963377,8.929681,0.637879,7.734617,0.623855,-7.471788,-9.560369,-8.212324,-1.972973,-5.538515,-2.817920,0.487519,-0.992929,-4.192657,-7.146466,-3.496936,-1.765354,3.607541,9.556499,2.447273,4.541429,7.387280,-4.166125,-0.562132,-8.237397,-0.158452,4.182512,-7.094655,1.892625,-5.452206,2.140197,-6.012356,-0.587396,9.090223,-4.707475,-3.643921,-6.953232,1.928699,9.718269,-6.078826,-6.800558,6.879284,-3.868329,5.388478,-1.866902,-8.051990,9.979066,2.716038,-3.635532,4.087088,8.587140,3.589985,7.691013,2.385164,-5.728558,-6.809294,-2.938924,-7.346924,-6.005525,-7.278603,5.881831,-8.077225,1.821424,-1.562805,-8.317660,-9.141800,-3.344494,6.564722,-0.505649,-0.472257,-5.900441,-7.439835,-1.470632,-1.659995,-0.683892,-3.355681,8.346901,-5.671942,-4.237475,-8.098524,-0.363859,3.410836,-0.108586,-7.394346,5.684447,-1.210975,-3.967152,-2.587101,0.262022,6.452478,7.127333,-1.922432,-9.852685,-4.806985,4.435753,9.101149,9.668716,-0.305226,7.210372,5.082883,-4.914234,5.284344,-8.546501,4.730269,-7.063181,7.091082,-1.121520,-4.032668,1.614472,-5.171227,1.644888,-3.174079,-7.908887,8.990639,-3.725315,-4.431891,-9.998230,1.020998,5.804919,-5.009479,5.323900,8.203723,5.705933,-3.121485,-4.776932,-5.501225,-4.239400,5.006660,7.138479,-4.527186,0.318634,-1.879627,-8.656617,-8.538397,9.792307,8.478586,-1.262908,-5.267668,-4.766106,-0.694589,2.371660,7.710044,-1.867773,-2.843116,6.121269,8.438482,3.618752,-6.784956,5.908479,5.298329,9.607330,3.797538,-8.531541,-8.571526,-3.745496,6.184667,2.346436,2.956304,7.040013,2.958331,-0.469428,9.340534,3.624611,-2.661793,-7.294260,7.550650,-7.430870,-0.536062,-8.426138,-9.853272,2.992680,2.016048,-1.892085,-9.746041,-4.211437,-6.435556,-9.926741,7.906706,3.971291,-6.540739,9.199862,5.399965,-3.921129,-3.924724,-9.675593,0.497029,2.683760,-1.783815,7.269282,4.907544,9.559146,5.706267,-5.111846,3.906604,-3.876030,8.445360,7.537689,4.768259,-8.082390,-8.931945,-6.588888,7.488341,-7.044174,2.503236,-9.416213,-6.225582,-1.384588,-4.849105,-9.730757,-8.963224,7.041194,-1.650578,7.602111,3.387786,-6.959106,-8.365122,4.798263,-0.213490,-4.001706,-7.384185,-4.725604,-0.240845,-3.049690,2.685385,-0.969055,7.492538,-7.221529,-6.069737,2.501104,9.827503,5.807599,4.775209,4.824350,1.075736,0.655741,6.034523,-5.799250,4.028230,-7.451920,4.985285,-8.759527,-3.636429,-2.040283,-4.580898,-5.930060,4.182987,-6.719272,2.474872,-5.580248,8.415934,-9.822239,-4.554677,-9.706500,6.202314,-9.289964,0.924130,0.971117,1.410757,-7.202914,7.973695,-9.391293,-1.219078,5.027417,-6.571073,-9.594829,-7.666847,-3.305622,2.379243,-6.868891,3.535687,6.663612,3.747093,2.806526,8.972781,7.717514,-2.454565,3.858569,-1.925287,-9.377321,2.545364,-6.970604,7.895148,-4.922812,5.266171,9.909220,3.199479,7.320891,9.766476,-8.627745,-3.020192,-0.498691,5.168383,4.069087,-1.194906,-7.247619,8.160558,0.911953,-5.669372,8.617578,-0.617007,-5.055095,-8.088985,0.840688,-0.492828,-5.838884,3.744064,-0.452937,-7.838653,-7.467427,0.146089,-3.176823,1.933191,-4.447696,9.230984,5.790894,-9.886182,-5.706044,7.675848,6.324925,5.593012,-3.157121,-1.937863,1.818364,-4.969885,0.229962,-1.513465,-1.100645,-0.900425,7.884582,4.438914,8.255000,4.476830,-6.764008,2.811352,-7.512559,1.182548,6.304831,9.383422,-4.274257,-9.160060,-2.577089,-1.976327,-9.264886,5.556400,-7.609632,-0.715006,-8.134379,0.097913,-7.508014,-9.045088,2.423285,9.334474,7.467490,8.570871,9.776717,-8.995049,8.708298,-3.424093,2.202968,5.908950,-3.328737,2.904527,0.060624,3.342089,-8.075615,2.851577,5.196182,-4.083432,7.020309,8.792381,-2.976469,-6.547681,-9.522153,1.658001,-6.585317,7.973360,3.478528,-9.404183,-8.859594,-4.321595,6.259393,-4.675301,7.983115,-0.027439,3.952087,3.231034,5.715725,1.950888,-4.197865,4.477581,4.517919,-5.049469,0.649268,-3.737080,-1.291735,-8.145754,-6.781940,4.227145,-6.392619,-0.074356,2.136332,0.627016,-1.895219,-3.607990,3.349175,3.849481,-2.628334,0.997965,-4.303529,9.953402,9.272528,8.956051,4.741276,2.065452,-9.846978,4.642611,4.038927,-4.699531,7.229086,-7.050925,-3.858779,1.909338,7.914350,-3.579072,-8.890305,4.226380,-0.417386,6.951536,3.196295,6.443123,1.841705,1.697371,1.104523,-5.701705,-8.140807,3.381240,-7.033174,2.806970,-9.917661,-6.968794,-1.397488,-3.980976,-4.067594,-3.580437,-3.018696,0.560007,-2.252515,-6.692346,-9.508507,-9.359391,6.540591,4.936493,-6.747174,-4.945120,-1.737217,-9.028571,-3.572534,7.293877,-3.559183,-8.985487,8.348891,-9.228807,-1.508764,8.208984,1.219724,8.588965,-7.947031,0.351633,3.445675,9.705888,-8.973732,-0.646739,-0.471198,5.661348,9.650420,6.937533,7.022341,-1.619473,-8.538921,-6.512845,6.397974,-5.619653,-4.800812,3.608100,1.562851,2.586213,-2.910556,-9.586167,-5.500595,8.027268,7.509476,-6.637769,2.200071,-9.703064,2.471717,8.551026,-7.799438,-8.103953,9.304197,0.383202,-3.579711,-9.590130,-8.052377,5.928797,-9.075575,6.089854,5.681181,-2.698963,-4.321042,-1.276250,0.501157,1.035902,3.411742,-3.602070,4.253045,-9.183282,2.897618,-2.999940,9.324691,-9.989063,-5.330313,-8.225630,5.905577,-0.414539,4.528973,6.068428,4.087738,5.673334,-1.043315,0.439848,9.452767,2.753964,9.737057,-9.516062,7.113374,-5.091438,-3.487716,8.356039,-3.991048,-7.042160,-9.299725,-6.791935,-6.630884,2.302971,-5.158936,-9.755842,-6.319983,-6.442649,4.923094,-7.798357,1.764447,-2.409978,2.161808,5.748580,-9.925610,-7.512306,-9.134911,-4.053733,-0.206912,1.477862,-5.688146,-3.619324,-3.180110,-3.286377,0.512334,-6.395732,-5.321070,0.810334,1.055609,7.605355,-9.595929,-1.318726,-8.294702,4.981686,-3.225412,5.974224,-1.512005,6.161585,-8.883072,-5.977535,1.975025,-7.070616,1.241895,9.689852,2.625608,-2.314190,-9.007389,-0.736561,7.369770,2.127756,-5.064932,2.995540,-7.959309,3.441676,-0.527246,6.527412,6.203022,2.468495,4.520637,9.832130,2.726260,-7.213338,-5.864598,1.581553,-2.035068,-5.979726,3.062260,8.421956,-8.325503,3.978751,-0.315745,-4.942385,-6.485571,-4.928157,9.116648,-8.111833,-9.027085,-6.633417,7.310820,-8.267564,5.061104,5.376414,-7.227664,-1.368126,5.016136,-1.736474,-4.209672,4.224581,-0.208804,-1.679243,5.493873,0.066714,4.362083,3.881227,0.919823,-7.275360,-4.035734,6.731713,-6.718993,5.065300,5.598750,4.220263,3.391262,8.760378,3.310147,9.553852,-6.594843,-2.510493,-6.745433,8.232299,8.979870,-4.414056,9.154786,3.212373,-6.016149,7.032007,-4.038692,7.589049,-5.415696,6.939898,5.175176,-5.218911,1.568618,3.769863,-6.656100,1.230840,3.260405,6.381800,-5.532510,-7.675192,-0.264093,-7.421616,9.536149,-3.493437,-8.140718,2.484379,-2.815043,-6.569622,-9.862226,7.921360,-4.234999,-8.306449,1.372053,-4.691602,-7.393780,-5.783902,-9.976816,6.093414,-9.133974,7.509245,-1.137624,-0.319055,7.187368,-2.148429,2.674421,-9.502236,7.617383,4.233598,6.256368,-0.615184,-5.120876,-6.405585,4.975974,-2.128815,2.226303,3.342060,-3.995563,-1.962835,-4.215103,0.098249,-2.822543,5.917127,3.020407,-5.960826,-6.305939,-2.402964,3.314135,8.040222,7.104280,9.687021,-4.818503,-4.300092,-5.280420,-1.887526,8.613270,-4.732859,1.592398,3.834277,-2.666182,1.256666,-2.660998,-3.357722,-0.800247,1.409725,4.219958,-6.209270,3.564603,9.465253,1.315378,-4.846941,6.180415,7.826707,-1.033698,9.161299,-7.976996,8.344183,7.499405,0.220792,2.187033,6.998111,6.618328,-6.656223,-8.117833,-8.354545,6.325881,-4.228132,-1.021638,-5.109996,4.624265,7.929114,-1.682998,-7.399202,-0.898566,-5.788351,-1.884479,6.689919,4.774436,-3.610101,8.575763,-4.648556,4.986991,8.028110,-8.005470,-6.581184,-7.025225,1.563385,-9.913297,-9.899600,7.512717,1.733387,-4.960071,3.450415,-1.900107,0.098112,4.166723,6.024132,-5.188895,-5.229630,-2.020320,-4.586368,-2.819769,3.219164,-1.951790,-4.627929,-7.703913,7.089472,-3.650955,2.291856,8.222198,-7.359488,-4.912101,5.884589,-0.145218,4.146253,6.492994,6.947224,2.585333,-7.297433,-3.836115,-5.892072,-7.848872,6.731556,-7.628395,-1.082218,9.718840,-6.339148,-1.065005,4.095049,3.947520,6.202845,-7.561791,9.607161,0.228736,9.506383,-8.025987,1.533614,-7.628278,0.141314,6.184236,-5.077083,-1.906783,-1.611849,-2.299743,2.351494,-7.490710,-8.291499,-4.467001,-9.551785,-1.989992,7.364908,1.766069,9.471529,-6.408830,6.392561,-7.131374,-7.357155,-6.880536,2.791585,-0.274318,4.763105,4.963034,-3.254914,7.342566,-3.505698,-2.243478,-8.317655,-7.944556,0.525007,-0.451405,-7.197286,-8.052526,2.239157,3.868300,-7.694891,3.028675,-9.584333,1.686554,-2.354974,5.633458,-4.563092,7.154395,-7.272632,2.369789,-0.867033,-5.659300,-7.049117,4.512289,0.197399,0.965603,5.408472,9.519949,4.926282,-2.709558,9.479924,-1.702046,0.330215,-9.858011,4.816784,-9.998670,8.177126,-5.168277,9.763312,4.232124,-1.218103,-8.484761,-9.928958,0.507107,6.625843,4.498384,-4.757623,-8.850339,5.363608,4.305703,-9.794468,-2.196321,-4.758316,-9.730866,1.747766,-1.301179,-4.798491,7.185997,8.752629,-2.406688,-6.868928,9.906721,-0.710740,-5.573023,1.648178,-2.777696,8.588015,2.718248,-7.997874,-8.622645,-1.770607,6.718293,6.298170,2.077625,-2.904024,4.993381,6.120131,5.798231,5.056820,-5.882274,1.161801,-2.258889,0.553069,-2.344062,1.353578,2.772244,3.069353,-2.956769,9.434251,7.602489,-1.464980,-8.629754,-4.038385,3.101976,-4.874466,-8.777408,-0.454557,-1.673830,-2.009252,6.619210,0.264037,5.141348,-7.697616,-2.161842,0.848935,3.851499,-1.044677,-3.919191,2.744449,-1.867580,4.506388,1.169395,-4.922661,3.142255,-8.515500,-2.970416,-0.634752,-1.142052,-2.094602,-8.969865,7.258324,5.710892,-0.515779,-2.836384,8.707348,4.107866,8.247289,-4.520324,-6.885399,-3.795466,7.460994,7.870858,5.339319,-8.740271,-0.771342,1.790608,-8.167271,0.317536,-1.902692,-4.549486,4.157427,-8.169281,-6.729280,-6.946078,7.048807,7.503291,6.073956,-7.264635,-8.079315,-8.962224,3.669767,-0.428440,-0.058681,-7.397190,6.504253,-9.721434,-0.430262,0.315667,-5.015095,-9.632580,3.316464,-5.200544,-5.916204,7.096315,7.104445,0.450083,0.403817,-9.738826,5.626231,8.806182,5.726794,6.984586,-8.957800,-4.168972,-8.438736,-2.847583,-9.361513,3.462712,5.707583,2.108038,-3.562552,-8.742990,5.109619,-5.364069,3.961640,9.966430,9.890359,9.407328,-1.793174,-4.445937,-8.487165,-3.893910,4.494079,0.606179,-6.551646,9.854617,4.597770,-4.485137,-4.786875,9.403781,-1.366051,-4.228194,-2.300185,-7.379647,2.874594,5.379020,9.098315,-3.342458,8.660736,-2.276319,2.088804,4.971158,3.310269,8.505890,-5.499951,4.131838,1.117700,-9.959301,0.129579,-6.598170,-4.162553,-5.051007,9.080024,-1.868553,-0.227730,-5.895930,1.728817,-7.449674,-8.189243,-7.702971,0.005372,3.722216,-2.469152,-6.566441,-9.475591,-6.760207,-9.685989,8.325784,-3.982405,7.051348,-3.039323,-5.496938,2.830603,-7.189437,-8.282304,-4.170251,-9.179071,-2.976059,0.583663,6.243434,-4.249745,-4.808816,-4.721217,-4.016732,-2.655589,-3.081146,-5.839060,-9.073567,1.865491,4.855603,9.811542,6.597685,7.380565,-7.669829,-8.452059,4.063985,-5.901759,-1.985306,3.112087,1.935901,-1.878654,-7.601350,-9.413563,-2.247770,0.508524,3.269502,4.243166,-6.413155,-8.228643,6.109980,-5.644805,8.372021,5.966139,-0.469339,7.581398,-9.598709,4.309172,-0.259558,4.442524,9.953715,-9.673203,9.886759,-6.213476,-9.901726,0.212092,8.070466,-9.835503,-8.765261,-5.741009,-4.594765,-3.822728,1.668984,5.167944,8.805200,-3.697770,4.364266,0.766788,-3.122202,0.987393,-4.241646,5.669215,-9.891536,2.330886,8.130522,5.847964,0.686523,-7.530319,4.590723,-3.208999,-8.070508,-3.622616,8.968948,-1.068172,3.070687,-6.334945,-9.406271,8.913257,-1.843551,4.347595,4.614699,0.817888,-0.709237,7.334091,-5.609669,-9.013451,9.934476,-0.002322,-7.127256,-7.972746,-3.974462,-9.909694,-8.533962,-3.397980,-1.659284,-1.246675,-8.718256,-5.275863,4.410630,0.366422,3.403068,-8.331971,-4.096900,8.470647,-7.003855,-8.130470,-6.436751,4.975439,-5.743885,9.254187,-8.132260,-7.440979,-8.642340,2.004036,8.937412,8.892869,7.333741,3.785713,-7.806613,-9.353294,-3.229386,-0.040785,0.824054,-4.707415,5.898212,-3.513324,7.728646,-6.880001,2.164320,-7.001037,-7.519579,5.260283,3.768389,3.171795,2.612698,-9.884905,-5.231827,5.270254,9.242393,-9.511495,4.757213,-0.531208,8.369883,-9.155762,-8.354199,1.224371,-7.769850,-2.508343,1.273148,-5.534301,-9.511567,6.889321,4.330236,-2.817696,-9.535646,0.526554,-1.386867,-7.415707,-7.117118,-7.639050,1.465183,-3.235976,9.326609,-2.946985,-9.117441,8.241640,0.309570,-8.087081,5.582755,2.487316,2.698013,-2.883557,-6.887809,7.449194,1.191426,-1.534597,-0.327147,4.273359,2.420945,-0.643693,-6.121232,-8.645888,-9.133650,-5.701481,-9.253854,9.130640,-8.642909,6.509669,9.459173,9.035669,-2.465927,8.726316,-5.812449,-3.760676,-4.377921,-5.738514,2.172515,2.452284,0.658219,3.089639,0.678438,8.423831,-5.408122,0.108085,3.462878,3.608950,-3.539239,-3.327428,2.832720,-4.960337,-7.787036,-1.879884,-4.572808,1.797137,6.159466,9.318486,-8.314370,-4.736814,4.209491,-3.964181,-4.122621,-5.579224,-3.740753,-2.500297,-3.094222,-5.384660,8.836160,-1.222577,-5.349791,3.263335,-1.032044,-1.718385,3.792256,-7.000170,-0.150347,4.772520,-0.921141,7.437829,5.444648,-0.338596,9.660714,-5.698704,7.566339,-4.341136,-9.499623,2.914987,-2.271560,6.578652,-9.584257,-3.464223,-5.668613,9.271188,9.887907,-6.699358,-0.295818,-5.143738,0.525945,-0.632035,5.364734,-6.068584,-7.754670,7.289703,7.275216,-1.395303,-5.462101,0.899967,8.794218,4.880932,6.190962,2.436542,-2.108333,0.720960,-6.294352,-1.500720,-3.732765,5.705687,-0.321027,1.545551,-5.639418,7.033657,-6.947527,3.341957,9.877998,1.617837,-8.622119,8.599996,-7.495334,-2.268099,-9.276942,6.363261,8.183628,-7.959055,6.002314,-1.409677,2.008857,-7.011108,-3.911477,1.428877,-8.782228,-2.237834,9.956007,4.036679,8.333678,-3.765571,-2.991172,-8.072636,1.780267,7.220210,1.624901,-9.880975,6.952486,-6.685166,-6.729415,7.259761,-1.524186,-7.953851,8.541572,-9.340932,0.166110,6.079951,-1.063322,-6.685280,-7.067427,-0.534405,3.114927,-0.546496,0.892504,-5.742862,3.631042,-8.162141,1.211484,0.326679,-1.620158,2.657601,9.192606,2.623746,0.619661,3.012792,1.653985,4.074754,-6.357129,1.373116,-8.278760,3.588171,0.820725,-6.517468,-5.432653,-4.056700,8.571129,3.852682,-2.881153,-1.568747,-7.968168,1.777442,7.874134,-9.374886,-9.896663,3.471424,6.808439,-4.078273,-6.866004,3.847506,3.442820,4.208506,-7.896070,6.260161,2.743461,-1.880005,1.204352,4.595448,-8.282206,-0.433925,7.345233,2.086357,-3.235495,0.226705,-4.224120,-8.217215,-6.955085,-0.806161,-4.286859,6.008524,5.590834,8.126761,4.109113,5.153111,-0.017868,9.023443,3.449364,-3.128098,-4.386561,-5.474109,-1.326020,-3.061388,-5.479986,9.305078,-8.954447,-2.704085,-9.399865,-4.515002,-1.854454,5.310771,8.313352,-5.754089,-1.515728,9.636257,8.490128,0.413014,-4.647625,-1.246212,9.252941,4.804828,5.437284,4.041148,3.827013,3.816657,-9.562244,-8.408532,4.292523,-9.791755,4.564874,9.943284,-2.319337,-9.614731,-4.502375,3.695149,6.641153,-3.028695,4.636736,-3.249675,3.517340,-9.548914,6.818097,-7.403918,-2.657865,-3.482065,-4.815504,-4.718635,-6.128215,8.657134,6.365691,-7.655186,6.894934,8.473965,2.426997,6.264795,-3.047851,-1.844235,-1.217847,-4.936265,5.808474,-1.132060,-1.317482,-7.307603,6.759820,-2.491809,1.431951,2.256021,3.866231,3.461295,0.348373,8.788403,-2.394814,6.810254,-3.236009,4.104298,-2.470166,9.357398,-4.392274,8.569880,3.507710,7.432004,4.805329,7.897308,0.008891,4.433827,8.897624,-3.072928,-8.310054,-2.020308,-1.123924,-8.752875,3.903131,1.534019,-3.362052,-3.289880,-9.624176,-1.174517,-9.193186,-5.681154,-0.936348,-2.335832,8.033686,1.549388,-5.065340,-9.586734,-3.347169,8.717353,7.126219,7.951580,-1.350977,7.551894,4.438190,-9.330212,-9.639328,-6.111785,-0.531431,-6.440184,2.982963,3.311310,-0.263100,-0.617815,-0.979713,-0.149799,4.053122,2.511979,5.954592,-6.684717,-4.580680,5.530537,-1.956421,1.668022,-4.277580,-9.823185,-9.487493,-1.879643,4.839751,3.163133,-1.472490,3.372819,1.098605,4.796992,-4.457209,-4.204749,-7.311440,8.260830,9.446367,6.632672,-7.799669,0.755084,6.426306,1.809424,9.377456,5.370722,4.851585,1.337346,5.177068,9.710556,-9.319650,0.300576,2.577395,3.985751,0.834886,6.448500,-1.015861,-2.244682,-2.079075,2.825817,-0.418981,1.955774,0.893115,4.198373,-8.792290,-5.018689,-8.388787,8.919548,-4.752730,-4.512175,-1.827619,-1.255864,-0.174640,-1.666933,-7.586890,-3.121194,-3.532797,-9.307214,-8.930669,6.221368,0.694418,-3.734563,1.852092,3.257421,-8.804593,0.133531,9.597728,-9.936327,7.685361,-4.548621,-8.559252,-7.457708,3.615372,-3.211782,-2.224149,-7.510317,-5.834578,9.509177,-8.934575,2.748612,-2.816476,2.248530,-7.864977,-1.050723,3.823425,-7.404582,1.233714,-0.722466,6.608258,0.642879,-9.327927,0.510456,-3.580817,-8.342028,-6.518973,6.933935,0.273802,-5.643105,-7.953721,9.683978,-5.524066,0.097662,-5.112102,-4.418795,9.832128,-7.145672,9.928468,-4.676624,-0.672110,-4.735058,-8.989292,-0.377267,0.348192,-2.657871,9.606104,6.441648,4.446618,8.263098,-5.661233,9.721064,7.957611,-2.189235,-4.727763,-5.185380,3.967954,2.564575,2.620446,7.915732,-1.906223,-5.486214,5.775104,4.612726,0.716601,7.217614,-9.483336,5.006316,-8.537225,-6.499053,-8.340824,3.061666,-4.248965,9.740259,-8.169393,-6.533739,-0.490409,-3.556614,-1.328503,-5.203439,3.126782,7.451704,5.469679,0.492204,-5.122815,-9.770549,3.168110,5.357097,-4.653426,7.804412,8.084893,4.315252,-0.339861,-6.820380,-6.272571,-5.009295,-4.557618,6.897527,-5.719040,7.432193,2.152892,4.203703,8.015156,-6.042116,-5.266563,8.247823,0.853533,7.938412,-3.491886,-9.042041,2.483846,-2.139171,-9.186337,4.362707,6.163541,-2.196023,-7.765950,3.195836,-2.497480,8.752296,7.548906,-8.689475,2.078047,-6.169352,0.517299,-6.216976,-5.303940,-3.907648,4.452889,4.914633,-7.510877,7.816771,-7.004820,3.993748,-5.330940,1.670603,2.652127,-0.994241,1.653766,-8.509019,1.525707,4.626029,-3.834910,-1.366690,2.470178,-5.504213,1.119654,-8.852606,-2.461171,-5.757809,-0.244262,-6.002417,-3.994217,5.790195,0.747547,-0.008528,-7.180898,-4.349851,-4.014115,-5.562712,6.370624,0.756387,-7.678466,-9.688356,9.578995,6.206816,-8.800358,7.416844,-0.104533,-8.648663,6.470501,-1.885414,4.417883,-4.781346,-5.932437,2.166767,0.225546,-0.756909,2.920566,-4.483090,-6.148177,-6.058964,3.867383,4.603365,-5.529122,1.846435,-5.027551,-7.761918,6.031046,7.173801,0.405536,0.338181,-7.377802,6.678403,-3.389924,-7.598832,6.031180,9.177143,1.706367,3.904085,-0.802642,0.827928,-2.126685,-4.646724,-3.204161,2.290014,2.784928,-8.013494,7.749691,4.119731,5.241968,-8.922373,-3.165650,5.268165,-9.112891,-2.413283,0.559301,3.119700,3.881037,0.247124,-7.031831,8.452279,8.725308,9.766234,9.909527,-7.387824,-6.209164,-8.905923,-5.773320,-2.313053,-8.123040,-0.214270,-7.915482,9.554414,4.289221,7.939580,-0.068694,6.461828,-6.693210,-7.188703,2.572781,-8.881782,4.723252,3.151790,-9.843422,-8.381007,-5.161976,7.988486,-1.501257,-7.306417,4.209460,5.838638,-2.771590,-4.124169,4.839004,7.089546,3.427416,3.436414,-1.133297,5.536884,-5.613207,1.477157,-4.515457,-7.528896,7.334101,-7.776271,-6.485631,-5.394598,4.455097,-1.903430,2.034404,6.262051,7.914541,7.881270,3.658500,2.304946,-4.526154,-9.786553,2.716520,-3.682289,9.051054,6.382581,-8.426976,7.062139,-9.947155,8.308849,0.238576,4.999532,0.324676,-1.378837,8.461487,-5.246918,-7.211823,-6.113176,7.704079,-3.967678,2.846127,9.562194,-8.382721,8.195307,-3.784400,-8.164260,-6.766516,-6.627929,0.046217,-1.565273,-0.445036,-5.947411,-6.194497,-2.526401,2.479823,-1.127494,5.408309,2.399376,-3.183998,-7.544958,8.989031,-8.940860,-3.004194,3.804429,9.422435,-6.613696,-3.302280,-0.561292,5.241630,0.687134,-8.481096,-1.311780,8.117467,5.592292,-5.214038,-6.524850,-6.816752,8.278652,2.531995,-8.017362,4.639177,4.674081,-6.329574,-0.715406,-3.995345,-2.207361,8.268705,-6.962511,-8.324813,7.730655,-6.946861,-3.776511,-4.107380,0.046139,-3.966513,1.199855,6.727040,-8.052242,-7.393779,6.639037,-2.879822,7.435439,-7.305439,-0.520422,8.936248,-3.885627,2.941575,6.119619,-8.994322,8.478090,-9.746109,-0.811231,8.806209,5.259904,0.829314,4.944771,1.189699,-0.734210,-9.777102,-2.791653,-3.892179,6.637166,-3.571999,9.756452,-2.080865,5.517583,8.334976,-6.027124,-7.454483,5.316737,-6.274663], dtype = "float32")#candidate|10796|(2520,)|const|float32
call_10795 = func_1926_call(relay.reshape(const_10796.astype('float32'), [12, 15, 14]))
call_10797 = func_1926_call(relay.reshape(const_10796.astype('float32'), [12, 15, 14]))
func_8508_call = mod.get_global_var('func_8508')
func_8510_call = mutated_mod.get_global_var('func_8510')
var_10799 = relay.var("var_10799", dtype = "float64", shape = (280,))#candidate|10799|(280,)|var|float64
call_10798 = relay.TupleGetItem(func_8508_call(relay.reshape(var_10799.astype('float64'), [4, 10, 7])), 1)
call_10800 = relay.TupleGetItem(func_8510_call(relay.reshape(var_10799.astype('float64'), [4, 10, 7])), 1)
func_10527_call = mod.get_global_var('func_10527')
func_10530_call = mutated_mod.get_global_var('func_10530')
const_10806 = relay.const([[5,4,1,-8,2,-4],[6,-4,-10,-3,-5,10],[-3,-7,2,-8,-3,5],[-8,2,6,2,6,8],[5,8,-2,-3,7,-10],[1,-5,4,8,-4,4],[8,5,2,-2,5,-10],[-10,-2,2,7,-1,8],[6,-7,-6,-2,7,-8],[1,9,-2,4,9,-1],[9,-4,4,-6,-8,1],[-6,-6,-2,-5,6,2],[-10,-8,-4,1,8,-4],[7,-3,6,7,-8,-6],[-9,7,4,1,-6,2],[9,3,-9,2,-10,-1],[8,10,-2,10,9,7],[5,-5,9,10,3,7],[-2,-7,5,-9,-5,1],[-5,-9,8,-8,-3,5],[2,-4,-1,-6,2,-3]], dtype = "int8")#candidate|10806|(21, 6)|const|int8
call_10805 = func_10527_call(relay.reshape(const_10806.astype('int8'), [7, 3, 6]), relay.reshape(const_10806.astype('int8'), [7, 3, 6]), )
call_10807 = func_10527_call(relay.reshape(const_10806.astype('int8'), [7, 3, 6]), relay.reshape(const_10806.astype('int8'), [7, 3, 6]), )
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
var_10810 = relay.var("var_10810", dtype = "float64", shape = (392,))#candidate|10810|(392,)|var|float64
call_10809 = func_8298_call(relay.reshape(var_10810.astype('float64'), [4, 14, 7]))
call_10811 = func_8298_call(relay.reshape(var_10810.astype('float64'), [4, 14, 7]))
bop_10823 = relay.right_shift(var_10810.astype('uint32'), relay.reshape(call_10809.astype('uint32'), relay.shape_of(var_10810))) # shape=(392,)
bop_10826 = relay.right_shift(var_10810.astype('uint32'), relay.reshape(call_10811.astype('uint32'), relay.shape_of(var_10810))) # shape=(392,)
func_2993_call = mod.get_global_var('func_2993')
func_2999_call = mutated_mod.get_global_var('func_2999')
var_10842 = relay.var("var_10842", dtype = "uint64", shape = (660,))#candidate|10842|(660,)|var|uint64
const_10843 = relay.const([-9.683659,-9.500230,4.301192,-4.428198,-0.642928,5.272361,-9.212991,4.836417,-4.885531,6.768964,1.087562,5.376722,-3.703842,-8.882545,-8.425283,-1.171680,1.162433,6.965508,-1.174866,8.847155,-3.346947,5.057880,3.301160,9.567450,-8.336404,7.933611,1.823322,1.549456,-7.206773,0.551377,2.397015,0.858497,-4.595787,-2.641295,-9.079805,-7.508027,-1.399149,-9.736713,-4.249353,6.157630,-3.898090,-6.140748,9.685194,4.108918,2.189452,1.014003,9.369906,1.105588,3.028559,-6.412217,-2.271002,0.402385,-7.065016,-5.836683,6.953666,9.915690,6.063488,-7.839481,6.973633,-2.640180,-3.043590,9.761765,4.095617,-0.545639,-4.386021,-5.163125,7.507850,7.457706,5.249081,-2.696857,9.310320,7.418398,4.552638,-7.559154,5.426727,-8.149209,-2.790651,6.975100,-9.561954,-1.775868,-1.611671,8.665990,-6.281608,9.798023,9.189193,6.863884,0.731537,5.448619,-7.062112,9.194435,-7.039446,3.148785,-5.695556,-7.507008,-4.727620,1.410428,-7.268974,-6.414446,-6.794471,-8.997917,1.369053,-1.866085,-0.014959,-0.834013,5.344134,7.176548,5.478155,-8.388340,7.199230,-0.175155,-5.989939,2.780505,1.646113,7.210912,1.844017,3.999704,4.871761,-8.825695,8.528785,-5.050387,-2.295159,-5.886922,0.759356,1.111389,-3.765749,-2.362286,-0.071340,3.042231,-6.291748,6.687316,-8.757499,-5.941734,-5.344904,-2.347174,6.118929,2.390075,-0.699360,6.067613,-9.927389,-8.863747,9.875886,5.194674,-4.843597,5.010768,-5.115105,2.240283,4.217455,-7.157113,-3.105301,0.864127,-9.499151,5.639380,-7.207734,-3.431150,-5.761129,2.590553,4.267280,4.685274,0.450790,-8.756243,1.144617,5.386472,-5.235587,-6.908772,-7.042612,-1.320835,-7.148927,0.804018,2.436633,-4.909838,-3.626175,8.759718,-0.453994,-8.990882,1.259509,7.838767,-6.777641,1.382263,3.480161,6.891180,5.779357,-8.913849,5.853210,-9.239812,4.315333,-0.427906,6.326742,0.192483,-9.184131,1.821086,2.463870,-6.747941,5.397509,-5.878607,-1.264588,-7.358824,8.739131,0.289135,-2.656253,5.873242,-3.619491,-4.852083,2.076394,-4.350161,9.244280,9.441068,-8.787716,-5.473482,2.099426,-7.317557,-8.566767,2.854034,0.703945,-8.089215,3.021132,1.095656,-1.495880,8.295073,-1.980255,5.897689,1.075209,-3.369260,9.183189,-4.463861,5.564336,-0.958380,2.839262,5.816118,-8.142519,9.699336,-7.726148,-3.690229,-3.586700,-1.901171,8.891483,-9.942337,7.151468,-0.752653,0.758166,2.617966,-4.042053,-5.483674,-9.653990,-5.545762,8.658049,-2.433796,4.495654,-0.456873,-0.499159,-1.808867,3.587753,-2.438821,0.889611,9.952745,7.672814,5.713613,-7.390981,-4.554157,9.432655,4.013109,-3.985375,-1.935589,-1.702452,1.742827,-6.176364,-5.746852,-7.249597,-1.510971,-6.950576,-4.414695,-0.784964,4.199797,3.452165,5.232437,-2.666989,8.108065,-7.000762,-4.750403,5.291719,1.943711,2.398734,3.333139,8.579904,0.754374,2.202534,4.131477,9.729812,-8.455505,-5.908519,-4.126157,-5.293579,8.574804,5.444266,-3.953885,8.450341,-5.417487,9.524346,-1.732523,8.095166,-6.512419,9.684764,9.626742,-7.011561,9.972281,9.566254,-5.952609,-5.326527,1.181878,5.865788,-9.427028,5.879877,-7.132927,-3.086902,6.597471,-4.910216,-2.603034,-7.192969,5.602020,7.290960,7.029120], dtype = "float32")#candidate|10843|(320,)|const|float32
call_10841 = relay.TupleGetItem(func_2993_call(relay.reshape(call_10798.astype('int16'), [15, 3, 7]), relay.reshape(call_10798.astype('int16'), [15, 3, 7]), relay.reshape(var_10842.astype('uint64'), [660,]), relay.reshape(const_10843.astype('float32'), [320,]), ), 3)
call_10844 = relay.TupleGetItem(func_2999_call(relay.reshape(call_10798.astype('int16'), [15, 3, 7]), relay.reshape(call_10798.astype('int16'), [15, 3, 7]), relay.reshape(var_10842.astype('uint64'), [660,]), relay.reshape(const_10843.astype('float32'), [320,]), ), 3)
bop_10857 = relay.mod(const_10796.astype('float64'), relay.reshape(call_10795.astype('float64'), relay.shape_of(const_10796))) # shape=(2520,)
bop_10860 = relay.mod(const_10796.astype('float64'), relay.reshape(call_10797.astype('float64'), relay.shape_of(const_10796))) # shape=(2520,)
func_10165_call = mod.get_global_var('func_10165')
func_10167_call = mutated_mod.get_global_var('func_10167')
call_10864 = relay.TupleGetItem(func_10165_call(), 0)
call_10865 = relay.TupleGetItem(func_10167_call(), 0)
output = relay.Tuple([call_10785,call_10798,var_10799,call_10805,const_10806,bop_10823,call_10841,var_10842,const_10843,bop_10857,call_10864,])
output2 = relay.Tuple([call_10786,call_10800,var_10799,call_10807,const_10806,bop_10826,call_10844,var_10842,const_10843,bop_10860,call_10865,])
func_10896 = relay.Function([var_10799,var_10810,var_10842,], output)
mod['func_10896'] = func_10896
mod = relay.transform.InferType()(mod)
var_10897 = relay.var("var_10897", dtype = "float64", shape = (280,))#candidate|10897|(280,)|var|float64
var_10898 = relay.var("var_10898", dtype = "float64", shape = (392,))#candidate|10898|(392,)|var|float64
var_10899 = relay.var("var_10899", dtype = "uint64", shape = (660,))#candidate|10899|(660,)|var|uint64
output = func_10896(var_10897,var_10898,var_10899,)
func_10900 = relay.Function([var_10897,var_10898,var_10899,], output)
mutated_mod['func_10900'] = func_10900
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10955 = relay.var("var_10955", dtype = "float32", shape = (2, 7, 15))#candidate|10955|(2, 7, 15)|var|float32
uop_10956 = relay.atan(var_10955.astype('float32')) # shape=(2, 7, 15)
uop_10958 = relay.cos(var_10955.astype('float64')) # shape=(2, 7, 15)
func_10498_call = mod.get_global_var('func_10498')
func_10504_call = mutated_mod.get_global_var('func_10504')
const_10966 = relay.const(8.812894, dtype = "float64")#candidate|10966|()|const|float64
var_10967 = relay.var("var_10967", dtype = "float64", shape = (392,))#candidate|10967|(392,)|var|float64
var_10968 = relay.var("var_10968", dtype = "float64", shape = (450, 2))#candidate|10968|(450, 2)|var|float64
call_10965 = relay.TupleGetItem(func_10498_call(relay.reshape(uop_10958.astype('float32'), [210,]), relay.reshape(const_10966.astype('float64'), []), relay.reshape(var_10967.astype('float64'), [392,]), relay.reshape(var_10968.astype('float64'), [900,]), ), 1)
call_10969 = relay.TupleGetItem(func_10504_call(relay.reshape(uop_10958.astype('float32'), [210,]), relay.reshape(const_10966.astype('float64'), []), relay.reshape(var_10967.astype('float64'), [392,]), relay.reshape(var_10968.astype('float64'), [900,]), ), 1)
func_8206_call = mod.get_global_var('func_8206')
func_8208_call = mutated_mod.get_global_var('func_8208')
const_10982 = relay.const([[-8.043866,-6.059760,5.372142,1.329400,-3.729157,-1.557522,-9.912403,0.228865,-5.535402,4.782201,5.335156,7.511319,-4.878910,7.246323,2.217562,3.325231,-1.739185,-6.702829,-9.059204,7.657630,-1.288922,-5.031545,0.762445,-6.294531,2.030847,2.540650,-1.347429,-6.014270,9.239028,7.370127,6.355160,-2.335322,-7.222768,6.511839,3.231299,0.128445,-3.743272,-8.544384,1.733353,5.179918,-7.431460,-9.248598,-9.833406,7.874825],[-4.280522,-7.100352,7.902182,-8.312629,-9.106897,8.490879,-6.769815,5.193154,-6.052648,-5.675135,-2.934766,-4.823659,-7.520241,1.454868,-1.047784,-4.360808,6.348988,-0.299786,9.574655,-5.734331,0.672543,5.519999,-1.889116,-1.230469,6.371500,1.096489,3.966902,-1.716230,-6.034785,-0.393717,9.032661,6.125348,9.979261,1.972233,-0.127867,-2.754285,7.691606,2.418495,-1.232599,-8.611151,-7.103888,-6.371468,-1.385709,1.186216],[-8.651254,3.908567,-8.495335,2.159363,-0.635787,7.179090,-0.526416,-6.210828,5.008361,-1.925282,-2.188847,6.515764,-1.072115,-8.819468,8.796717,4.777718,1.453854,8.648831,4.302670,0.787416,6.456334,2.767539,1.384397,-4.959112,5.294101,-0.526328,3.418677,4.095043,3.396984,-6.091442,8.928672,7.553107,-4.588267,4.661182,7.278237,-6.052279,0.250781,-9.438158,4.409227,6.926706,5.684199,-5.906481,-8.739352,-0.231428]], dtype = "float32")#candidate|10982|(3, 44)|const|float32
call_10981 = relay.TupleGetItem(func_8206_call(relay.reshape(const_10982.astype('float32'), [132,])), 3)
call_10983 = relay.TupleGetItem(func_8208_call(relay.reshape(const_10982.astype('float32'), [132,])), 3)
var_10988 = relay.var("var_10988", dtype = "float32", shape = (2, 7, 15))#candidate|10988|(2, 7, 15)|var|float32
bop_10989 = relay.logical_or(uop_10956.astype('bool'), relay.reshape(var_10988.astype('bool'), relay.shape_of(uop_10956))) # shape=(2, 7, 15)
func_10091_call = mod.get_global_var('func_10091')
func_10095_call = mutated_mod.get_global_var('func_10095')
const_11003 = relay.const([False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,True], dtype = "bool")#candidate|11003|(702,)|const|bool
call_11002 = relay.TupleGetItem(func_10091_call(relay.reshape(const_11003.astype('bool'), [1, 702]), relay.reshape(const_10982.astype('float32'), [33, 4]), ), 6)
call_11004 = relay.TupleGetItem(func_10095_call(relay.reshape(const_11003.astype('bool'), [1, 702]), relay.reshape(const_10982.astype('float32'), [33, 4]), ), 6)
output = relay.Tuple([uop_10958,call_10965,const_10966,var_10967,var_10968,call_10981,const_10982,bop_10989,call_11002,const_11003,])
output2 = relay.Tuple([uop_10958,call_10969,const_10966,var_10967,var_10968,call_10983,const_10982,bop_10989,call_11004,const_11003,])
func_11006 = relay.Function([var_10955,var_10967,var_10968,var_10988,], output)
mod['func_11006'] = func_11006
mod = relay.transform.InferType()(mod)
var_11007 = relay.var("var_11007", dtype = "float32", shape = (2, 7, 15))#candidate|11007|(2, 7, 15)|var|float32
var_11008 = relay.var("var_11008", dtype = "float64", shape = (392,))#candidate|11008|(392,)|var|float64
var_11009 = relay.var("var_11009", dtype = "float64", shape = (450, 2))#candidate|11009|(450, 2)|var|float64
var_11010 = relay.var("var_11010", dtype = "float32", shape = (2, 7, 15))#candidate|11010|(2, 7, 15)|var|float32
output = func_11006(var_11007,var_11008,var_11009,var_11010,)
func_11011 = relay.Function([var_11007,var_11008,var_11009,var_11010,], output)
mutated_mod['func_11011'] = func_11011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_11036 = relay.TupleGetItem(func_8318_call(), 0)
call_11037 = relay.TupleGetItem(func_8319_call(), 0)
output = call_11036
output2 = call_11037
func_11040 = relay.Function([], output)
mod['func_11040'] = func_11040
mod = relay.transform.InferType()(mod)
mutated_mod['func_11040'] = func_11040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11040_call = mutated_mod.get_global_var('func_11040')
call_11041 = func_11040_call()
output = call_11041
func_11042 = relay.Function([], output)
mutated_mod['func_11042'] = func_11042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_11058 = relay.TupleGetItem(func_10157_call(), 0)
call_11059 = relay.TupleGetItem(func_10159_call(), 0)
output = call_11058
output2 = call_11059
func_11087 = relay.Function([], output)
mod['func_11087'] = func_11087
mod = relay.transform.InferType()(mod)
mutated_mod['func_11087'] = func_11087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11087_call = mutated_mod.get_global_var('func_11087')
call_11088 = func_11087_call()
output = call_11088
func_11089 = relay.Function([], output)
mutated_mod['func_11089'] = func_11089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10237_call = mod.get_global_var('func_10237')
func_10239_call = mutated_mod.get_global_var('func_10239')
call_11095 = func_10237_call()
call_11096 = func_10237_call()
output = call_11095
output2 = call_11096
func_11122 = relay.Function([], output)
mod['func_11122'] = func_11122
mod = relay.transform.InferType()(mod)
output = func_11122()
func_11123 = relay.Function([], output)
mutated_mod['func_11123'] = func_11123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_11129 = relay.TupleGetItem(func_9014_call(), 1)
call_11130 = relay.TupleGetItem(func_9016_call(), 1)
func_10896_call = mod.get_global_var('func_10896')
func_10900_call = mutated_mod.get_global_var('func_10900')
var_11135 = relay.var("var_11135", dtype = "float64", shape = (70, 4))#candidate|11135|(70, 4)|var|float64
var_11136 = relay.var("var_11136", dtype = "float64", shape = (392,))#candidate|11136|(392,)|var|float64
var_11137 = relay.var("var_11137", dtype = "uint64", shape = (660,))#candidate|11137|(660,)|var|uint64
call_11134 = relay.TupleGetItem(func_10896_call(relay.reshape(var_11135.astype('float64'), [280,]), relay.reshape(var_11136.astype('float64'), [392,]), relay.reshape(var_11137.astype('uint64'), [660,]), ), 4)
call_11138 = relay.TupleGetItem(func_10900_call(relay.reshape(var_11135.astype('float64'), [280,]), relay.reshape(var_11136.astype('float64'), [392,]), relay.reshape(var_11137.astype('uint64'), [660,]), ), 4)
func_10165_call = mod.get_global_var('func_10165')
func_10167_call = mutated_mod.get_global_var('func_10167')
call_11142 = relay.TupleGetItem(func_10165_call(), 0)
call_11143 = relay.TupleGetItem(func_10167_call(), 0)
output = relay.Tuple([call_11129,call_11134,var_11135,var_11136,var_11137,call_11142,])
output2 = relay.Tuple([call_11130,call_11138,var_11135,var_11136,var_11137,call_11143,])
func_11169 = relay.Function([var_11135,var_11136,var_11137,], output)
mod['func_11169'] = func_11169
mod = relay.transform.InferType()(mod)
mutated_mod['func_11169'] = func_11169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11169_call = mutated_mod.get_global_var('func_11169')
var_11171 = relay.var("var_11171", dtype = "float64", shape = (70, 4))#candidate|11171|(70, 4)|var|float64
var_11172 = relay.var("var_11172", dtype = "float64", shape = (392,))#candidate|11172|(392,)|var|float64
var_11173 = relay.var("var_11173", dtype = "uint64", shape = (660,))#candidate|11173|(660,)|var|uint64
call_11170 = func_11169_call(var_11171,var_11172,var_11173,)
output = call_11170
func_11174 = relay.Function([var_11171,var_11172,var_11173,], output)
mutated_mod['func_11174'] = func_11174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_11183 = func_8443_call()
call_11184 = func_8443_call()
output = call_11183
output2 = call_11184
func_11191 = relay.Function([], output)
mod['func_11191'] = func_11191
mod = relay.transform.InferType()(mod)
output = func_11191()
func_11192 = relay.Function([], output)
mutated_mod['func_11192'] = func_11192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8644_call = mod.get_global_var('func_8644')
func_8645_call = mutated_mod.get_global_var('func_8645')
call_11224 = func_8644_call()
call_11225 = func_8644_call()
output = relay.Tuple([call_11224,])
output2 = relay.Tuple([call_11225,])
func_11236 = relay.Function([], output)
mod['func_11236'] = func_11236
mod = relay.transform.InferType()(mod)
mutated_mod['func_11236'] = func_11236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11236_call = mutated_mod.get_global_var('func_11236')
call_11237 = func_11236_call()
output = call_11237
func_11238 = relay.Function([], output)
mutated_mod['func_11238'] = func_11238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_11261 = func_11087_call()
call_11262 = func_11087_call()
output = call_11261
output2 = call_11262
func_11269 = relay.Function([], output)
mod['func_11269'] = func_11269
mod = relay.transform.InferType()(mod)
mutated_mod['func_11269'] = func_11269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11269_call = mutated_mod.get_global_var('func_11269')
call_11270 = func_11269_call()
output = call_11270
func_11271 = relay.Function([], output)
mutated_mod['func_11271'] = func_11271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10325_call = mod.get_global_var('func_10325')
func_10326_call = mutated_mod.get_global_var('func_10326')
call_11275 = relay.TupleGetItem(func_10325_call(), 0)
call_11276 = relay.TupleGetItem(func_10326_call(), 0)
output = call_11275
output2 = call_11276
func_11299 = relay.Function([], output)
mod['func_11299'] = func_11299
mod = relay.transform.InferType()(mod)
mutated_mod['func_11299'] = func_11299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11299_call = mutated_mod.get_global_var('func_11299')
call_11300 = func_11299_call()
output = call_11300
func_11301 = relay.Function([], output)
mutated_mod['func_11301'] = func_11301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11040_call = mod.get_global_var('func_11040')
func_11042_call = mutated_mod.get_global_var('func_11042')
call_11327 = func_11040_call()
call_11328 = func_11040_call()
func_8644_call = mod.get_global_var('func_8644')
func_8645_call = mutated_mod.get_global_var('func_8645')
call_11348 = func_8644_call()
call_11349 = func_8644_call()
output = relay.Tuple([call_11327,call_11348,])
output2 = relay.Tuple([call_11328,call_11349,])
func_11361 = relay.Function([], output)
mod['func_11361'] = func_11361
mod = relay.transform.InferType()(mod)
output = func_11361()
func_11362 = relay.Function([], output)
mutated_mod['func_11362'] = func_11362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11236_call = mod.get_global_var('func_11236')
func_11238_call = mutated_mod.get_global_var('func_11238')
call_11453 = relay.TupleGetItem(func_11236_call(), 0)
call_11454 = relay.TupleGetItem(func_11238_call(), 0)
output = call_11453
output2 = call_11454
func_11478 = relay.Function([], output)
mod['func_11478'] = func_11478
mod = relay.transform.InferType()(mod)
mutated_mod['func_11478'] = func_11478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11478_call = mutated_mod.get_global_var('func_11478')
call_11479 = func_11478_call()
output = call_11479
func_11480 = relay.Function([], output)
mutated_mod['func_11480'] = func_11480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10237_call = mod.get_global_var('func_10237')
func_10239_call = mutated_mod.get_global_var('func_10239')
call_11510 = func_10237_call()
call_11511 = func_10237_call()
output = call_11510
output2 = call_11511
func_11516 = relay.Function([], output)
mod['func_11516'] = func_11516
mod = relay.transform.InferType()(mod)
output = func_11516()
func_11517 = relay.Function([], output)
mutated_mod['func_11517'] = func_11517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_11589 = func_11516_call()
call_11590 = func_11516_call()
output = relay.Tuple([call_11589,])
output2 = relay.Tuple([call_11590,])
func_11604 = relay.Function([], output)
mod['func_11604'] = func_11604
mod = relay.transform.InferType()(mod)
output = func_11604()
func_11605 = relay.Function([], output)
mutated_mod['func_11605'] = func_11605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9974_call = mod.get_global_var('func_9974')
func_9975_call = mutated_mod.get_global_var('func_9975')
call_11606 = func_9974_call()
call_11607 = func_9974_call()
output = call_11606
output2 = call_11607
func_11610 = relay.Function([], output)
mod['func_11610'] = func_11610
mod = relay.transform.InferType()(mod)
mutated_mod['func_11610'] = func_11610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11610_call = mutated_mod.get_global_var('func_11610')
call_11611 = func_11610_call()
output = call_11611
func_11612 = relay.Function([], output)
mutated_mod['func_11612'] = func_11612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_11689 = relay.TupleGetItem(func_9014_call(), 1)
call_11690 = relay.TupleGetItem(func_9016_call(), 1)
func_10035_call = mod.get_global_var('func_10035')
func_10037_call = mutated_mod.get_global_var('func_10037')
call_11699 = func_10035_call()
call_11700 = func_10035_call()
func_11299_call = mod.get_global_var('func_11299')
func_11301_call = mutated_mod.get_global_var('func_11301')
call_11701 = func_11299_call()
call_11702 = func_11299_call()
func_8256_call = mod.get_global_var('func_8256')
func_8261_call = mutated_mod.get_global_var('func_8261')
var_11712 = relay.var("var_11712", dtype = "uint8", shape = ())#candidate|11712|()|var|uint8
const_11713 = relay.const([-1,-7,2,-4,-7,4,3,-6,-10,10,-5,-3,-9,6,-1,-4,-10,7,2,9,-8,-9,-10,5,-6,-1,3,-10,2,4,7,-6,-8,-2,-4,4,-3,2,-10,5,-1,-6,2,-9,-2,-8,3,-9,-8,-3,-2,-6,-10,8,5,-5,-10,5,7,-8,10,-9,1,6,-10,2,8,5,-6,9,6,2,-2,-10,10,7,4,-3,-7,2,7,-7,2,4], dtype = "uint8")#candidate|11713|(84,)|const|uint8
const_11714 = relay.const([[-2.545823,-3.162179,-5.511890,9.140655,-9.836181,2.283555,-9.711814,5.194696,-6.151333,-7.188299,-9.911598,3.727918,6.513977,-2.889451,1.382368,9.110855,9.801658,-1.406302,-8.068192,6.774355,-4.177296,0.726251,0.887995,-0.046386,-1.356213,-0.933445,8.311780,-9.227686,-8.163158,2.554771,5.544341,4.546543,-0.633513,-4.464681,6.542398,8.200181,7.069156,-6.394068,-0.803561,-6.032055,-7.171744,3.826464,-4.057896,-5.503507,-3.987199,-5.881911,-2.317331,-0.981893,4.772436,-4.010512,-6.816494,5.754687,-7.484390,2.505648,-8.546325,1.348601,-1.512578,-5.440296,-5.220667,9.808442,-5.632691,-1.462984,4.160984,-8.198015,-2.298107,-8.386011,-3.502546,-9.955164,8.315095,1.905100,8.912045,-5.299172,9.589371,3.407538,-0.786546,8.416713,-3.191028,1.149671,-4.900109,6.328267,-6.277378,-3.811791,0.750887,3.850065,-4.193686,-2.819177,5.026642,0.356675,7.515985,8.728751,7.390527,7.573216,-2.651822,3.989856,-7.285887,6.018394,-6.923047,8.671909,-1.542992,3.815836,-6.962261,6.750422,-1.848681,-0.054077,4.480200,9.073859,-4.276426,-1.621186,-6.926690,-9.293519,-3.399273,7.067478,2.915748,-6.168332,-6.734024,-6.881387,6.701927,-7.214271,-9.229068,-2.711724,-9.479208,-6.379351,-6.937676,-7.198604,-9.279545,9.114626,-1.961472,-5.822403,7.617980,-3.935847,-1.027266,-5.614527]], dtype = "float32")#candidate|11714|(1, 132)|const|float32
var_11715 = relay.var("var_11715", dtype = "uint64", shape = (660,))#candidate|11715|(660,)|var|uint64
call_11711 = relay.TupleGetItem(func_8256_call(relay.reshape(var_11712.astype('uint8'), []), relay.reshape(const_11713.astype('uint8'), [7, 2, 6]), relay.reshape(const_11714.astype('float32'), [132,]), relay.reshape(var_11715.astype('uint64'), [10, 66]), ), 0)
call_11716 = relay.TupleGetItem(func_8261_call(relay.reshape(var_11712.astype('uint8'), []), relay.reshape(const_11713.astype('uint8'), [7, 2, 6]), relay.reshape(const_11714.astype('float32'), [132,]), relay.reshape(var_11715.astype('uint64'), [10, 66]), ), 0)
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
call_11722 = relay.TupleGetItem(func_1719_call(relay.reshape(const_11714.astype('float32'), [12, 1, 11]), relay.reshape(call_11711.astype('uint64'), [660,]), ), 2)
call_11723 = relay.TupleGetItem(func_1723_call(relay.reshape(const_11714.astype('float32'), [12, 1, 11]), relay.reshape(call_11711.astype('uint64'), [660,]), ), 2)
func_8732_call = mod.get_global_var('func_8732')
func_8736_call = mutated_mod.get_global_var('func_8736')
const_11739 = relay.const([-3.055656,-3.345392,9.278383,-0.210355,7.582973,-8.699192,-5.189283,1.387951,4.187771,-4.385130,-0.643401,-6.711354,5.637359,2.201651,-1.373609,-6.982691,-9.066819,1.398421,-4.775844,5.942476,-5.351952,-7.465841,1.733707,7.649559,4.441906,-2.740383,-8.244454,-1.985294,4.275977,-5.239786,-7.764985,-2.145243,3.725277,-6.821146,8.730296,2.198042,0.504399,7.819076,1.241063,1.108997,-6.540952,-4.468218,6.895908,-7.874394,4.315952,-0.747966,-2.504559,-9.095694,-2.226370,0.193833,-0.515543,3.384435,-1.653243,-8.514714,-1.767728,0.933794,3.042064,6.146381,-6.725014,9.067912,-1.592177,7.756068,-2.514687,-7.344333,-4.352227,-7.201364,1.181999,5.884785,-1.246727,4.288403,8.698990,0.215222,7.002147,0.044702,2.160820,6.727825,-8.424461,-2.457412,-2.760905,-3.782916,-0.893420,4.607588,-3.624955,8.671429,-7.666090,9.222299,9.032612,-8.746930,2.003537,-7.746869,-4.401535,-3.836932,-3.017910,9.029849,-4.793497,-6.711840,-6.131156,-5.498268,-7.430538,-0.066857,-3.660401,-9.040455,-7.751734,-2.646875,0.537631,-5.279568,-0.137307,-1.925667,7.759303,7.127966,8.873432,-6.834746,5.385340,4.474716,3.109565,-8.441605,3.162010,6.331403,8.312438,-9.662929,1.913814,-7.011374,9.730929,-7.287106,-3.646604,-4.046417,2.412893,-8.403879,9.986500,-3.692128,4.969328,5.172044,-7.693054,-6.163627,-3.168772,-5.731056,-1.117035,-7.900138,8.364815,-2.314444,-8.647383,-4.450890,-7.620368,4.046894,-8.359317,-9.510606,-0.266240,-5.525087,-0.750173,7.591787,7.415688,-2.472215,-7.937663,-5.259346,-7.989798,-4.005504,5.785845,-4.674787,2.470137,-4.948287,-4.486291,2.818463,-4.532947,9.937269,-1.662614,0.475058,-3.108496,9.776982,-3.570697,-0.150657,6.823595,-7.631572,0.549164,-9.221415,-1.893953,-0.604499,6.293157,4.449242,-3.034265,-7.235331,8.152082,-9.232261,-5.577816,3.363391,5.471121,2.520330,-9.420759,-3.704186,-2.120093,-5.929679,9.625359,6.682149,-7.600794,-6.728671,1.044143,7.760198,-0.683836,-3.073539,-0.671159,-6.525545,-8.403332,-9.936683,3.951514,-5.989205,1.391902,-0.562297,-4.561075,8.993682,-6.490812,4.320565,-5.789318,4.070776,-3.918671,9.133579,4.497559,9.103709,6.780136,-4.747052,-5.605611,5.050153,6.011522,-1.064048,1.657238,-7.939332,4.393598,-7.048831,-8.400200,-0.271936,0.435783,2.377687,9.391168,-7.043138,-6.253937,7.312058,-5.752131,-7.039563,-3.700466,8.748427,-3.399354,-2.381801,6.426271,-6.646716,-7.112568,-5.755127,-1.013957,-2.755271,-6.760123,9.318101,9.577072,3.800689,3.943186,5.490353,-8.457518,2.555425,-6.348066,-7.846865,-4.358353,4.332900,-9.792016,5.799652,-3.186439,-0.506288,-3.243552,3.844656,4.367656,3.670380,0.983783,-1.659771,3.610869,-9.688081,2.167917,0.566812,2.800069,-2.987734,6.658805,9.326919,1.112989,-2.918250,6.731224,2.891793,4.381399,5.551895,0.317788,-1.125107,0.310965,-2.232145,-6.310107,2.679997,1.596257,7.425978,9.885755,-8.193799,-6.913723,-1.629745,-0.631123,-4.588301,1.948584,-1.871786,-2.714353,4.893490,-9.495361,-1.752941,-6.741205,-4.363387,-8.523443,-8.244401,-2.210509,-1.617412,7.505474,-1.535262,7.397998,8.056179,-0.841195,0.445509,9.706337,4.333829,0.826503,-1.820745,0.414510,7.248451,-2.511678,7.577700,-0.369498,7.968503,-3.608738,7.961934,2.109447,-1.076538,0.837666,-1.651837,7.488446,-3.054810,2.262606,-5.022914,3.174901,-6.674126,0.722291,7.369068,-7.449198,8.001254,-0.710674,-0.431207,-1.282837,-6.591289,-7.161269,-1.264025,-1.199305,-0.496063,0.390892,-9.587633,-6.096147,-6.268969,-7.984603,7.152386,-1.186650,0.787745,-2.298504,-3.989317,9.982781,-3.165791,0.799609,2.716654,7.722329,-3.475160,-4.732022,4.681272,9.356172,-1.110672,1.783380,-7.852545,-1.630183,2.402606,3.128977,1.627340,-3.041908,9.283646,-3.252097,6.657112,-0.710987,-5.039045,-5.914594,-9.947863,2.996114,9.604210,-5.466633,5.810875,2.961734,1.068556,-9.302103,6.500817,-0.995153,7.926702,1.990525,-8.222356,-8.601880,-1.610898,2.794678,-2.159885,3.864256,8.850561,-5.642585,5.581905,4.700715,-3.608060,3.529596,-9.801156,-5.744731,4.752608,-8.648698,-0.397646,-1.327150,5.962836,5.327760,1.546503,8.928301,-1.102784,5.482773,-3.349326,8.227862,-9.293131,-8.573798,-4.877954,-8.931788,6.975046,-0.525504,9.091585,-6.390188,-8.773568,3.709454,3.611054,-9.091194,-5.102206,9.281106,9.484878,8.389635,4.067985,-6.335972,4.903562,3.109570,-4.552526,-0.617257,5.290996,-4.810746,-5.503020,3.426315,5.152175,0.188357,6.042738,-8.491452,2.420864,-5.551735,7.148592,2.743139,-9.557286,5.165773,-0.459978,-0.388656,2.486880,9.487010,-4.767781,9.093822,-3.060765,2.305318,5.636244,-5.728230,-3.605879,0.958390,-1.240529,-8.500436,-8.906439,5.630700,8.190160,-9.596348,-0.693979,-1.636346,-1.193369,-4.770166,-7.464427,-4.287241,3.802097,3.985774,8.567410,-6.656975,7.107056,-1.204652,-2.941628,-7.020898,-8.230198,-2.321125,-7.265748,1.826891,-0.915151,1.362201,-9.058599,-5.243339,6.300825,4.743034,8.263125,-3.531507,-8.309191,-2.295406,-6.082277,-4.786134,3.115289,8.109101,2.639348,-1.621454,0.363443,-9.566745,4.804136,3.413155,-9.954232,6.265141,-6.892874,-5.481604,7.957815,-3.426483,8.036890,-2.940338,8.384333,-0.596429,-7.034681,3.375990,7.499964,9.000100,-9.596891,4.361625,4.568584,-8.808314,-8.602127,-2.997554,0.224320,2.092927,2.530229,7.979649,4.084643,9.450453,-1.453721,7.074948,4.031419,-5.216934,-2.169292,-0.577777,5.830178,1.384642,-8.898961,6.755236,-2.620322,-2.553365,-5.445286,9.106609,-3.030105,3.701149,2.179329,-2.590479,-8.596413,-0.318859,-1.484959,-2.192833,-4.635823,2.157368,-5.060016,-2.003220,2.360908,-1.395653,9.012701,2.325984,8.399742,-7.262331,-4.522815,5.258305,-3.282849,1.797803,-4.928748,-8.124194,7.533587,3.414349,-2.748139,0.695399,0.504277,8.448765,4.383878,-3.804974,6.774323,1.568097,0.715214,-9.770074,-5.290624,-1.188785,-3.491660,0.669754,-8.993657,7.922102,1.733398,-7.195232,-1.966636,4.416055,-9.430258,-6.457487,-9.113088,5.287106,-9.474387,3.761671,9.564419,-3.269920,-4.251563,-8.768481,-2.970838,3.289893,-6.643090,-4.295841,4.290003,-1.590251,2.298099,-2.259360,-3.294216,6.150644,4.672566,7.833202,-0.105783,-4.334996,-5.910396,1.063744,-5.454753,-3.457661,-0.055979,-9.957658,-0.157936,-2.366975,7.881154,1.971671,-3.512585,8.530341,-6.005528,0.698690,-8.212721,7.045716,-2.419812,5.388007,-7.309853,0.035699,6.505682,-7.005708,-9.248266,9.239040,7.848860,1.710579,-6.354469,-5.813432,3.428609,4.736328,8.493177,-8.724702,-2.018552,5.314443,2.694990,2.658681,-0.380187,-2.995869,-3.541494,-0.510169,3.243948,-2.279399,-6.515973,-7.178344,-5.914120,6.203570,-7.559590,1.125025,-3.443579,0.511507,0.672395,-2.549104,6.463126,-0.721856,-8.829544,9.503482,-6.643047,2.592857,-1.578019,-7.272748,-0.430407,9.624236,-2.363517,9.063187,6.848681,-1.094584,0.672358,-7.980920,-6.173021,9.927824,3.665946,-5.430128,-9.321271,7.502067,1.899954,6.254228,5.684767,-8.369654,6.620508,-1.188790,2.012890,2.466364,4.736412,1.804486,-7.233303,2.746143,1.234717,5.544795,8.083004,5.347546,-4.726896,-8.602926,0.388127,1.468417,-8.966497,3.172311,6.404017,6.510269,-3.632699,-0.651524,0.372303,-6.409447,6.037000,-9.977877,-1.883040,2.876828,-2.394025,2.747777,-1.382991,-5.988128,-7.119695,-3.095505,-4.630559,2.634671,-7.125777,9.166896,2.176961,3.754008,0.219856,8.163684,2.286742,-6.881344,7.719343,8.779921,1.889785,-4.241092,2.522983,1.918118,-7.724838,-5.750597,-4.583135,-2.543188,7.953344,-3.008301,3.287557,0.076360,-0.079468,-1.964391,6.670053,5.223452,4.150997,-0.166858,0.775554,-7.818864,-5.082004,-2.782832,-1.809916,-5.704433,-3.454887,-6.406966,3.679388,-2.835138,-1.583178,9.417159,-1.529402,-0.353242,-5.325715,-3.388703,-3.131809,-0.090772,0.175524,3.020724,4.243642,-3.480032,-0.680600,-5.032436,-4.198369,2.625919,1.855085,-2.778781,2.085341,-8.007567,0.435301,8.090725,3.198811,7.728797,9.679296,2.468879,-1.684753,-4.247136,-4.185038,-7.605154,-6.775290,2.485508,-6.614974,3.873770,-9.166408,-8.825319,6.582731,4.193649,6.305756,2.156083,5.527388,1.075622,-7.264169,-1.380841,-0.295061,7.533638,-8.597520,0.412761,-9.050497,5.081973,-2.205915,3.215294,3.428341,-0.287553,3.283417,0.332390,-3.479360,-4.685577,1.783510,-9.663544,-4.064143,-5.587348,-0.379745,9.579638,-1.995996,-1.273719,-7.200519,-7.887271,-2.074619,-6.890856,2.389328,8.743341,5.243505,-3.603534,-3.597409,-1.633243,6.739909,-4.175842,-9.009577,-5.371416,-1.332107,6.447475,-4.194218,-3.420164,5.726094,-0.188107,2.132928,-8.417185,-9.780154,2.731848,5.758262,5.998693,-7.088916,7.252200,1.810433,4.496256,-0.565496,0.098568,7.034601,2.984164,-1.875352,9.909306,1.306313,-3.853827,-9.244013,0.430876,-1.221594,-3.075092,-5.484904,3.991746,-8.872320,0.093064,-3.019560,3.933836,-1.535018,-8.130159,5.498018,-8.042764,8.199780,-8.301266,-1.103766,-0.204101,-4.546315,0.459241,-1.911867,-2.527328,-9.004826,6.190858,-7.665922,-2.368823,0.149065,-3.619355,-2.705778,-7.439421,8.952718,3.481868,-0.196071,-2.202119,4.773724,8.797850,8.121761,-9.331788,6.495276,-9.114467,-9.953743,-7.377676,5.442756,-8.931475,-1.095895,4.703192,0.202379,7.407504,-4.723575,-9.027170,-4.046424,0.404060,-6.015340,2.935872,1.746727,9.168164,-7.618366,-4.845767,-2.870165,7.504439,5.613792,8.392315,1.315354,-3.839291,-2.999577,8.766143,-9.135253,-5.141036,-1.204066,-2.659539,4.390582,-5.719717,2.258195,1.468697,9.888130,-1.872738,-8.675416,-5.557476,0.773423,9.803494,5.297871,-0.336494,-2.738592,-9.725098,-6.797533,-2.569329,3.507798,3.681406,5.526567,-1.825206,5.218301,3.022699,-2.731626,8.933186,-5.697989,-0.366303,-4.264669,8.614618,3.681849,0.505793,-7.862489,-9.062627,-9.738763,8.109475,-7.686206,0.069126,-2.144187,6.010807,-1.632042,-1.141761,-5.958884,-1.585468,0.854137,1.386663,-1.902950,-2.972400,-3.300322,-0.086491,-9.540607,3.854365,4.376312,-2.247283,1.416623,9.596661,7.479384,3.113382,-1.853604,-2.075525,2.951580,-7.364374,-8.059576,4.259581,8.451880,-5.781015,5.899251,1.612197,-5.575594,-0.365071,4.740296,9.129707,-0.552653,-4.435337,-9.560738,-5.622943,-3.449016,2.786586,-9.320069,-4.340094,-2.031568,2.834257,-8.746959,9.486205,7.882490,-6.117703,3.915614,6.983785,-4.015082,-7.802937,-5.108131,1.110076,8.367587,2.979374,7.721688,-9.554649,-2.208729,1.951968,-5.650359,7.578384,-2.099800,-2.527932,4.521039,2.642565,-8.568942,1.291610,4.849267,2.766980,2.121713,-7.517965,-3.647455,6.990288,-7.335979,5.873808,8.205512,-0.170148,6.309615,3.167023,-7.047635,-8.927409,-8.079350,1.696786,-4.574480,-1.407630,-2.213363,-8.018960,6.734567,3.204913,-5.816786,-2.558600,-2.922112,-5.032150,-0.506438,-6.483334,-0.755685,1.363884,-7.862156,-7.699770,2.619893,2.825323,1.606398,5.400181,1.965078,9.392700,9.414252,1.605275,-0.480296,2.343499,7.542743,-2.632758,6.965714,-0.559114,-5.834216,-0.441406,9.170231,2.989806,-3.881516,-0.445881,-8.482503,7.160126,0.915544,6.385728,-0.633665,-6.044918,-9.344379,-3.189939,-3.809432,-9.760206,3.177941,6.620051,-8.552251,-5.559494,9.267324,-7.853787,-7.983706,7.067686,-8.855307,9.683410,-6.300575,-5.509138,-1.437832,-3.040520,6.793696,-9.094173,6.972332,4.586985,-0.385815,-0.050749,-2.910902,8.960354,6.812590,5.848518,6.122965,-0.569113,-2.621484,9.052889,2.108040,-9.377407,-0.987959,-9.074831,-7.511573,1.071783,3.009625,-9.287167,-5.914142,-8.523618,-6.979358,1.348331,-1.264004,5.084821,-2.810193,-4.882413,-2.494842,-5.524537,5.970600,3.964791,-0.664947,-4.047018,-3.830336,-9.267834,5.176411,-1.171952,-4.857267,9.234943,-8.266035,4.519013,3.094814,-5.944362,-6.198899,-8.166063,6.099243,9.679669,-9.564087,3.027197,-5.809285,0.413696,-2.236751,-8.222326,3.197266,-6.039689,-9.661025,-5.767267,7.879799,-9.622457,2.486796,4.468771,-6.172911,7.188453,-3.919248,4.265528,-5.556895,-8.205262,6.180265,9.760630,4.148032,-8.018121,2.101311,5.787391,3.705292,9.017228,7.268079,-1.166733,4.700032,-4.145090,-1.111592,8.575801,1.402990,-2.447970,-7.534726,1.405474,4.572701,4.993600,4.364756,6.262312,-5.356673,7.317168,8.061466,8.763142,4.229346,-5.078632,-3.742467,-2.070916,-0.804757,-1.838898,-4.800251,-5.082628,5.886135,9.398917,-9.207105,3.948371,8.307842,-4.095811,-8.122983,8.071916,-1.050710,-7.386083,2.769311,-8.332693,1.986470,-4.765366,-2.847727,5.466004,6.135595,-4.553965,9.397197,-5.043995,3.628187,3.450478,1.934070,7.070286,-0.271614,-1.284553,3.791603,9.677012,2.345685,-6.071333,-4.370019,1.240280,-3.341136,-2.878148,2.020864,-1.394053,8.289383,3.672153,8.889965,-0.420422,-6.773959,0.098356,4.904707,-1.150231,7.083262,5.974210,-6.986977,7.550405,-5.973259,-8.059034,-2.532395,-6.152343,-4.803062,-7.915177,2.634386,8.127090,4.555207,4.861358,-4.785255,4.232196,-2.376875,3.088232,6.575479,-4.779795,-4.567440,-5.074313,5.717933,2.217923,-3.331688,7.033822,-6.996575,2.114330,-5.798434,2.466478,-3.924415,-3.390822,5.829988,3.894509,-0.379363,-2.624678,-4.301277,5.232125,-1.344411,3.432717,4.887143,-4.734781,4.275539,3.424645,-4.102657,-5.780994,-0.310138,9.824389,8.783006,-2.311982,-0.662511,-0.079480,2.031888,6.866148,-5.757960,-0.188226,1.578725,-0.560923,-8.614291,-4.660635,-3.698710,5.462003,3.112481,-1.068314,8.568481,-9.712063,3.448897,-2.652171,3.178817,-1.551336,-7.571814,9.694922,7.877791,8.218539,6.221302,-8.396650,-3.427200,-0.282615,8.376459,-4.358177,-9.785189,-2.874893,-3.018188,-8.420364,-1.557381,8.924542,-6.989372,9.721666,-1.487519,5.484630,-0.603146,6.889115,-1.979916,7.879298,-1.693809,-0.226702,-7.812449,5.274809,-4.810687,-7.291892,-5.148602,3.884754,-7.345585,8.984509,4.822982,5.207511,-6.932019,1.796577,-6.301143,-5.372925,-1.097641,1.225682,-3.815354,4.764098,5.771615,3.528976,-6.447688,-9.515555,7.604872,2.876385,-5.923359,7.164984,-6.541049,9.334363,9.284320,3.161369,4.176099,-8.869773,5.184907,-8.536071,-9.491729,8.787587,-7.825339,5.687329,0.986333,6.170148,7.329521,-2.311318,1.131388,9.315839,-1.383459,-0.453994,2.481559,1.732134,4.485839,0.826922,9.006868,-1.281268,-2.984362,-2.731962,-3.095715,-0.461295,-5.363853,8.690559,-2.987700,-7.255004,-6.727901,-2.056729,1.398098,-4.117125,3.172969,-3.914996,-2.925264,8.689635,5.286454,-9.939808,5.106821,0.829343,-4.160442,4.793239,5.501919,0.169544,-1.054689,-0.909316,9.117455,-2.155470,-6.849352,2.127891,8.297758,-0.675099,-6.364454,0.776849,0.942497,5.077000,1.665905,-2.784993,-5.468413,-7.530776,-1.437079,1.108018,-4.915543,-2.027909,-7.094381,5.755132,-5.681051,-5.704627,9.164471,-4.122786,5.505164,-9.404008,-4.332408,2.026935,-6.167374,-6.056698,-2.602601,-2.933143,4.965269,-8.418331,-0.825813,-4.732825,5.630745,-6.600162,-5.482416,6.857754,-2.419499,-9.534640,-9.582061,-7.778200,-1.421674,3.732746,-2.774446,5.435616,7.842715,2.695838,7.774436,-6.904264,1.607518,0.040157,-5.967723,2.584147,-2.007345,1.835430,2.040664,8.131301,-5.564382,6.684076,-3.622754,2.311000,-2.910394,-8.262624,-8.248127,-6.992982,4.608583,4.159050,-2.598007,-6.797294,-6.517704,0.397301,6.435822,1.134970,-7.225886,-4.758218,5.527317,-3.151183,5.606430,-8.387824,4.009960,2.495424,-8.918408,-1.820734,1.744109,-1.691049,9.844115,9.386474,-3.215171,-7.074784,8.349467,-1.908058,-1.286342,-9.967040,1.145154,9.789335,4.117668,1.339337,5.061070,-4.828352,-2.169286,3.602080,5.808605,2.223348,3.242247,-7.655765,-1.288683,-6.023697,1.177255,-7.427750,4.462581,1.087343,-8.385206,-3.566149,7.094216,-1.406482,7.074017,5.472860,1.830859,9.096843,-9.879515,6.193785,-7.750073,-0.115169,1.557812,-0.488458,-1.019258,6.839039,-0.039399,8.961204,1.882546,3.669474,3.975355,8.025796,3.457371,8.572763,-7.218235,8.820999,-0.897545,-1.216040,-9.790758,-1.076722,-5.629817,-3.597973,-0.007573,-4.691184,5.791280,-9.534422,-3.946555,7.929468,-2.973906,-9.078682,-8.227254,0.720511,4.283858,-6.566282,-6.091707,-4.399305,-5.206206,1.265705,-3.979661,-6.523416,-5.739357,-9.386877,-7.402379,-1.964052,7.045564,8.005599,-4.172974,-0.288426,-4.892322,-5.177440,-8.289388,-8.722690,0.411625,6.682818,2.850654,2.766107,-2.533247,1.923062,-2.539937,-2.303422,-5.526922,4.635260,-4.203117,-1.303352,-8.388896,-9.310398,0.169509,6.968291,-2.318165,5.311080,8.398053,6.230375,-7.415619,-8.647721,0.356079,-4.780126,7.159608,-6.751835,-4.644584,-2.319333,5.323654,9.916304,5.917454,9.092727,6.234090,-1.085317,-6.511494,-5.629738,-0.480710,5.622893,3.277721,9.821438,1.894733,0.779546,-9.480521,-4.766452,-5.938803,-5.700719,-4.466337,5.811082,-4.939687,-2.901307,-9.187549,-6.597555,-1.319261,-8.942086,6.507430,-4.497358,5.218834,-1.792775,2.199808,-1.785401,-0.395134,-6.041349,-2.319119,-4.048265,4.025879,3.622027,-8.233311,-0.610182,7.326214,-7.906799,-3.740297,9.952029,-0.953558,8.529879,-4.577119,6.712535,-3.915781,-3.942251,-1.240261,-1.843139,2.181829,1.423089,0.515257,-7.111426,-3.601058,8.962895,3.809707,-6.681469,2.042609,-6.456003,8.050036,-3.451971,6.085975,4.458142,-8.242093,3.403213,0.246819,3.655232,-1.061410,-9.611501,-9.637349,9.099066,-2.390475,-2.161151,9.714711,-0.668883,-3.847176,-9.117587,0.882666,5.381226,6.400315,4.562111,7.732305,9.003937,9.639531,-6.267319,-8.651872,3.605461,-5.696934,-1.580118,-9.500192,-1.146283,8.496921,-1.318136,-0.157124,-2.583667,-8.927071,6.187909,-7.981952,1.036072,-6.285709,-0.999856,7.925970,6.414756,8.235509,1.961200,-2.967139,-9.346334,4.795787,-1.725466,3.797184,0.015381,9.437097,0.340275,-1.833817,0.965408,7.749927,8.412625,7.376844,-9.641373,-2.255647,9.854738,5.091931,-9.113819,-2.398055,0.944020,-2.224126,-8.578066,5.735681,8.806282,-6.136252,-8.804083,-9.809525,3.910161,-6.834824,-0.731441,0.006505,-6.261183,-2.207200,6.736988,3.608762,-0.446184,-5.287233,6.315218,-9.743161,0.148690,7.092153,-2.906561,0.463779,-4.378542,5.311777,-8.418908,-8.053935,-1.211551,7.612497,0.283070,-9.274666,-8.760146,-9.465954,-7.006986,0.106929,-3.383169,5.579211,-1.107270,-2.921034,-8.599053,-1.959551,-3.639215,5.154631,7.368119,7.581270,-4.482597,-1.869999,-7.099230,-8.382617,0.054726,-9.390978,7.864789,2.277943,-8.708389,-2.500216,6.567599,1.739344,7.163500,-7.830075,8.806289,2.568986,9.066158,1.516657,4.602026,-6.694645,0.106753,-2.739871,-9.895490,-6.028057,3.447528,-6.216854,5.652852,-6.434005,-6.820776,6.384871,-4.189406,7.159456,-4.855851,9.617647,6.813598,4.460984,-2.585693,4.059231,9.374571,4.799866,-5.479756,6.216446,3.005941,-3.402559,4.441848,-5.210951,-3.747337,9.020288,-8.432081,-3.692863,9.112271,-8.909799,4.907597,-1.441531,5.757341,2.064942,1.405405,-7.829046,8.792094,5.476296,-0.446897,-5.952573,0.445257,-8.239575,0.105156,3.739483,-3.093070,-3.581568,4.425027,-9.978343,0.920006,-2.048343,-2.086527,9.508446,9.312484,-4.417817,-9.072346,6.955392,1.117456,9.817795,-9.811348,5.345526,-1.479368,9.425674,-1.744356,8.086987,8.267545,6.961576,-3.066039,1.924805,5.163039,4.198034,1.424834,7.074072,-8.556589,1.975659,-5.075740,8.882931,-0.403081,-4.377714,-0.812620,-2.753242,-8.768321,-6.470679,8.285868,-5.260924,5.081665,-5.998112,-2.011575,6.102400,7.489064,-5.772559,9.898577,-6.062402,-0.370233,6.713292,-0.987687,-0.100768,6.173905,4.816321,9.718807,1.555575,-3.555933,1.229296,5.882181,5.545730,7.275992,-2.256905,-0.461926,-7.088335,-2.587432,8.194129,-2.285110,2.415066,-6.919334,-0.413767,-3.815112,2.200708,1.428063,-2.783678,5.217325,2.883864,1.187698,-1.212975,0.974631,-7.394922,-4.216587,-8.710419,6.336902,-2.650317,2.925101,6.415172,-0.060675,-1.904831,7.597101,-6.700659,-8.429266,1.419320,-9.111323,2.873315,9.333450,9.428346,-6.993264,-9.989876,0.887315,1.643101,7.543863,-2.260929,9.002010,3.913356,8.838223,-6.868761,-5.143359,8.356241,6.391678,-8.327396,-1.915294,-4.819228,5.093123,7.259502,2.250249,3.502360,9.469361,-1.954750,-0.332358,-4.010039,4.254688,-0.842036,-0.002001,-3.442972,-1.659256,-2.212161,-9.702843,0.597623,4.614747,-7.756753,-4.589623,5.575067,-8.904585,-6.369207,-3.092016,-1.370638,8.786076,7.727443,1.979937,4.311036,-3.821108,-4.212137,-1.941224,-6.112764,-4.871411,-9.080523,4.522763,1.810616,4.155922,-5.247582,-7.516067,-1.164004,2.316116,4.254788,6.798578,5.516816,2.724812,1.891034,4.394047,7.742494,-8.881002,-2.403637,-7.976830,3.062998,-0.666172,7.726485,3.128024,-8.463984,7.463699,2.884726,9.251174,-0.877241,-8.151964,-4.607387,1.773764,-6.362873,-2.181308,8.829687,-6.083373,-1.331092,0.839045,2.543376,8.784730,5.986460,8.144677,-5.793935,2.358489,1.535106,-8.990578,-6.660961,-4.204382,4.626026,0.544885,5.985402,-8.568599,-4.094610,1.338589,-5.263254,-6.827622,0.185428,-9.565743,-5.239925,-7.517945,9.009253,1.955466,-8.371725,-5.876475,-7.970634,7.805312,3.022629,-1.607573,4.854196,4.389869,-7.679275,8.230735,-0.255307,8.130853,-5.790974,-8.918521,-6.173916,3.298359,7.528466,8.963761,0.017983,2.757810,-9.030850,4.029234,3.245023,2.898312,-4.175815,7.806143,-9.337641,7.657658,-0.406161,-0.924978,1.541444,-2.228830,-7.591921,3.519194,-6.661926,-2.085481,-0.995643,-4.913670,2.290652,9.416134,-7.320473,-7.735741,-5.493333,6.517376,4.702763,1.850002,6.203693,-6.083478,6.109592,-2.460082,-4.734143,-6.673045,-4.680723,0.402135,-6.288385,7.898666,6.671429,6.478923,6.672176,6.183850,2.882826,5.274061,-3.866839,-3.743684,4.218149,4.574902,8.271798,-5.349161,-2.227347,8.427574,7.101449,8.203326,-1.575796,-8.026445,-7.704707,1.628098,-5.239103,-9.284920,-7.788669,4.762964,5.124812,3.295518,-8.882311,-5.423888,1.691729,-4.614015,-2.439855,-5.918610,-8.570565,-6.669437,-0.143118,-8.353360,4.968446,9.225550,3.968282,0.040356,2.716169,-2.559868,0.174678,-9.145350,-8.840288,6.318430,-1.352961,-4.230588,-2.689425,5.250866,-7.119588,0.757845,8.931859,0.357138,9.947718,0.480218,6.284274,5.139760,4.167930,-8.298995,-7.508435,-6.732219,2.814974,4.862855,-9.522901,-6.002906,4.732233,-3.456200,-6.278088,6.351310,-7.469838,-6.639678,-3.435473,-7.827491,9.832848,-0.086696,-8.025294,-4.460545,1.484004,9.093493,9.277196,-8.995667,-3.007365,2.477657,-4.806194,-1.998646,0.420732,-8.232934,-3.349674,9.897640,8.226067,7.293857,6.151507,8.396468,-5.250747,-5.832121,-4.127112,-8.327303,9.046280,9.937235,-9.869432,-3.638116,-4.169401,-8.952923,-8.642712,-7.078665,9.790227,3.697399,-1.363254,0.280098,-7.970229,-5.764102,-7.972552,3.899616,-0.812938,0.286250,-3.350287,-6.369542,-0.241428,-0.257348,0.482947,9.516660,-8.916965,7.985249,7.724613,1.002878,-3.913743,5.104619,-0.050904,-2.657526,7.782718,-5.891130,5.867652,2.334287,0.033085,-6.761840,-2.897094,6.503722,4.106074,0.540474,4.159403,-5.835670,-2.611567,-1.178165,-7.766762,3.816119,-5.123116,6.457444,8.890420,0.862244,-0.151823,5.051466,2.886193,-1.465292,9.240037,-6.582011,-1.070985,-0.963950,-8.698686,-9.346980,3.898346,-7.015759,9.173703,6.259279,-2.932813,5.705662,9.564281,-0.912772,3.953202,9.631649,-7.342647,1.257690,-4.730749,-3.551070,-7.249324,6.879915,-6.703994,3.729287,0.711677,-0.364802,5.026040,9.022343,-5.162045,-7.662135,-3.999479,-8.558133,9.366003,5.890496,5.020248,-7.304754,-2.425956,0.758264,6.446408,-1.711797,-0.458657,6.572122,-1.869062,-2.681640,-9.252045,-0.385099,-0.642299,5.988202,-2.124534,7.437056,-7.900010,6.552643,7.012221,-1.569053,7.233396,8.825796,1.803555,-4.045869,3.603971,2.749280,6.704717,-5.397860,-0.726085,5.597031,5.557272,2.317946,-1.904664,-1.729346,9.881099,-7.681612,-9.673365,-9.340027,-4.855011,2.724092,5.273122,9.499663,5.378239,-7.809638,-7.996494,-5.129329,-5.613936,2.808982,1.402584,-9.436237,-6.671741,3.133523,7.408840,4.227347,-3.276048,6.378838,1.443460,-9.046826,7.988095,-5.802633,-6.873582,9.956391,-2.027297,4.458106,-6.985723,8.231360,6.734448,0.677472,-3.265961,-1.326678,-9.365665,0.175909,0.095719,-5.854077,-2.436500,-0.304491,7.764258,-5.225396,-3.839492,2.983948,1.933055,-4.222300,-3.775698,7.982615,-9.033545,6.155303,-7.765794,-3.132119,2.289117,-4.353819,6.994067,-6.263114,-7.820132,8.872093,1.664544,9.981222,5.239897,5.917696,-2.896668,-4.785977,-6.108393,8.498400,-5.428782,-7.923497,-5.400083,-3.060591,0.546737,-5.912707,3.667150,6.350840,3.582882,0.293514,-6.151255,-3.886322,-9.283559,6.376466,-1.765777,6.248973,-9.079578,-4.539358,-8.187597,-4.997985,-4.721911,6.143396,-1.163927,-8.070380,5.566073,-0.116372,-3.293459,-3.771214,-7.896671,3.396784,-4.947535,3.777172,4.043486,2.350588,-7.394751,8.415795,8.754939,-5.281721,5.066993,3.288915,7.012112,-8.146630,-8.633492,-0.395724,-9.665332,2.651474,-7.771242,9.699266,4.563286,6.285956,7.730867,-9.452502,4.033931,-3.735968,8.979259,1.053680,-5.451392,-2.716272,9.226729,5.897996,-9.551436,-3.812757,1.184875,-3.861806,9.432339,7.991287,8.873227,9.273041,-1.440494,8.764519,6.666332,-7.674102,7.235747,-2.457403,0.969474,-4.126487,-3.299925], dtype = "float32")#candidate|11739|(2520,)|const|float32
call_11738 = relay.TupleGetItem(func_8732_call(relay.reshape(const_11739.astype('float32'), [2520,]), relay.reshape(var_11712.astype('float64'), []), relay.reshape(call_11689.astype('float32'), [320,]), ), 1)
call_11740 = relay.TupleGetItem(func_8736_call(relay.reshape(const_11739.astype('float32'), [2520,]), relay.reshape(var_11712.astype('float64'), []), relay.reshape(call_11689.astype('float32'), [320,]), ), 1)
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_11745 = func_11087_call()
call_11746 = func_11087_call()
func_8036_call = mod.get_global_var('func_8036')
func_8038_call = mutated_mod.get_global_var('func_8038')
call_11751 = relay.TupleGetItem(func_8036_call(relay.reshape(call_11699.astype('int16'), [315,])), 0)
call_11752 = relay.TupleGetItem(func_8038_call(relay.reshape(call_11699.astype('int16'), [315,])), 0)
output = relay.Tuple([call_11689,call_11699,call_11701,call_11711,var_11712,const_11713,const_11714,var_11715,call_11722,call_11738,const_11739,call_11745,call_11751,])
output2 = relay.Tuple([call_11690,call_11700,call_11702,call_11716,var_11712,const_11713,const_11714,var_11715,call_11723,call_11740,const_11739,call_11746,call_11752,])
func_11756 = relay.Function([var_11712,var_11715,], output)
mod['func_11756'] = func_11756
mod = relay.transform.InferType()(mod)
mutated_mod['func_11756'] = func_11756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11756_call = mutated_mod.get_global_var('func_11756')
var_11758 = relay.var("var_11758", dtype = "uint8", shape = ())#candidate|11758|()|var|uint8
var_11759 = relay.var("var_11759", dtype = "uint64", shape = (660,))#candidate|11759|(660,)|var|uint64
call_11757 = func_11756_call(var_11758,var_11759,)
output = call_11757
func_11760 = relay.Function([var_11758,var_11759,], output)
mutated_mod['func_11760'] = func_11760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9004_call = mod.get_global_var('func_9004')
func_9005_call = mutated_mod.get_global_var('func_9005')
call_11762 = relay.TupleGetItem(func_9004_call(), 0)
call_11763 = relay.TupleGetItem(func_9005_call(), 0)
output = relay.Tuple([call_11762,])
output2 = relay.Tuple([call_11763,])
func_11771 = relay.Function([], output)
mod['func_11771'] = func_11771
mod = relay.transform.InferType()(mod)
mutated_mod['func_11771'] = func_11771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11771_call = mutated_mod.get_global_var('func_11771')
call_11772 = func_11771_call()
output = call_11772
func_11773 = relay.Function([], output)
mutated_mod['func_11773'] = func_11773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_11802 = func_8443_call()
call_11803 = func_8443_call()
func_9974_call = mod.get_global_var('func_9974')
func_9975_call = mutated_mod.get_global_var('func_9975')
call_11807 = func_9974_call()
call_11808 = func_9974_call()
output = relay.Tuple([call_11802,call_11807,])
output2 = relay.Tuple([call_11803,call_11808,])
func_11809 = relay.Function([], output)
mod['func_11809'] = func_11809
mod = relay.transform.InferType()(mod)
output = func_11809()
func_11810 = relay.Function([], output)
mutated_mod['func_11810'] = func_11810
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11828 = relay.const([[[-3.069366,-7.309993,-3.054546,1.164106,0.067172,3.436956,-8.632572],[0.230000,6.476055,7.868261,0.470587,8.567182,1.985725,-5.230551],[-1.812414,-0.339255,1.969604,3.764689,4.586850,0.360644,2.129963],[6.775455,2.083977,7.999615,-7.577019,1.296588,-3.430931,8.443480],[-1.058824,-5.904684,-5.654852,5.869492,9.422998,9.343248,2.186894],[8.211139,0.240419,0.933810,-5.737535,7.116976,4.168017,-8.783012],[2.166847,6.711173,-3.702570,-2.880878,-3.813017,-0.238240,-8.174984],[-2.088104,-3.619529,1.860671,-6.388555,4.880936,8.272467,1.161244],[5.703357,-7.158953,0.884968,-5.982716,-3.492126,-6.142367,-0.680400],[-9.449882,1.688222,-3.199943,3.038167,6.840146,-1.571108,-6.982402]],[[-2.077591,-0.547093,0.298476,-1.126806,-1.660823,-9.188600,-1.989730],[9.587725,8.684651,8.709432,-6.434792,1.077955,4.256144,0.650871],[6.741571,6.683080,6.166721,3.825830,0.773152,-5.960850,-0.873282],[-6.774856,5.030222,9.888311,2.582363,9.097769,-8.941127,1.044978],[-8.489626,-2.256661,-8.718844,7.112031,6.778410,0.363760,-8.262442],[6.815523,-2.723466,2.052755,1.418336,5.757340,-5.015406,0.103984],[6.132278,-7.220750,1.597491,4.632775,8.358069,-4.638886,3.206392],[7.826124,5.509862,-3.318517,-7.265572,9.155646,-6.589372,-0.047483],[-3.410538,5.052301,6.435957,4.540510,-0.039561,-6.065512,6.158085],[0.255441,-4.175363,-9.931725,5.788961,-7.889304,4.747161,7.602934]],[[-6.104688,-4.989687,9.003816,-5.148945,4.633017,-3.973366,-9.340154],[7.647879,0.178115,-9.379723,4.726802,9.897127,2.738740,-7.858752],[9.538132,-1.939437,-3.326290,-6.308058,-8.537806,-0.183014,-4.937998],[-0.640287,9.926158,-1.160232,-3.290113,8.273503,-7.299572,-2.677298],[-5.847924,-5.808128,-4.155712,4.896911,3.178020,4.495735,-6.129005],[7.516223,-5.659734,3.907295,-1.432610,-1.589802,-2.108155,-8.366951],[-0.537928,-7.908021,-1.517765,-7.598496,2.521061,1.473285,-0.992290],[-8.086068,-1.831719,7.183131,5.646139,-7.313971,0.413724,-4.488733],[-8.626708,-4.714253,3.840974,9.215050,0.215477,5.298211,0.137100],[1.018799,1.666273,-8.476623,3.010514,-5.171380,-8.960121,-2.580335]],[[7.821218,1.243375,-2.670710,-5.238860,-5.156941,8.903155,6.472763],[-4.163189,1.850265,-4.089651,-5.302597,-3.709944,8.150498,-1.265550],[4.217636,8.526114,-6.650810,6.230558,-8.087958,-9.847630,4.028849],[-6.342694,-4.922698,-3.704169,-8.172270,-4.886741,4.239838,-6.210361],[8.208982,0.529621,-0.645027,8.896127,9.579643,5.126017,-8.019019],[8.078424,1.610838,2.259499,-9.977768,9.278020,-8.863427,7.341918],[-1.185800,-2.183849,5.833908,-8.821106,-4.534394,-0.881027,-1.152145],[3.705598,5.090257,8.962522,-1.201332,2.041784,-0.997355,6.001665],[-4.355864,-5.375777,0.420338,3.891619,-1.286958,-4.055820,5.054007],[6.048167,-9.639164,7.877270,6.810489,-2.439034,2.035699,-5.761964]],[[-0.284930,-0.097544,7.606886,6.495008,-3.035364,1.928725,-9.664939],[1.629750,-8.605224,-8.458911,-0.681177,-9.158358,-9.084342,6.942906],[-8.435986,2.706155,-3.809589,-8.150134,-2.105115,-7.818119,-6.429842],[-4.530417,5.632107,-1.846370,-2.454353,-4.507615,-7.752786,-0.993146],[9.793777,-2.704482,8.599754,-2.223590,-3.798748,8.727748,-2.496927],[9.883734,6.447623,6.108762,5.366225,-2.789640,-5.536997,-3.580968],[-2.455271,1.170963,7.870854,8.197977,1.924794,-2.192707,-6.794820],[6.924834,2.385749,3.065292,-9.554005,1.338629,9.334575,1.623017],[-0.611769,-6.888602,-1.971159,-8.038143,-7.935545,-2.943102,2.870094],[8.550844,7.669461,-2.337921,0.641827,8.286812,-5.602240,6.308543]],[[5.884370,-8.296603,7.737736,-8.135338,-0.069113,1.084123,-9.335209],[1.325066,-3.930445,-9.276913,3.909457,-9.611674,-4.664180,-7.915862],[-2.771915,-1.836702,-3.333324,5.387375,-4.048071,5.198813,-1.686325],[2.140426,-0.779934,-9.169742,8.409734,-1.464739,8.479452,7.932985],[2.844788,-4.865917,3.516579,4.594144,2.842736,5.915864,-8.088055],[5.663192,8.087755,7.601414,2.250117,-6.671860,-3.546599,2.424581],[0.611405,-4.600777,-8.797277,-9.501323,0.055934,6.799383,-8.294222],[-1.635331,9.460410,6.523337,-0.464674,-5.965534,-1.800326,-7.881704],[-0.608926,-7.993546,-6.502852,-7.798881,-0.411801,9.103100,-1.359075],[-0.499342,2.618943,1.726897,-0.224218,-0.445183,2.622366,-5.298399]],[[9.719206,2.766895,-9.180146,-8.729527,-6.805633,0.697774,6.556573],[-8.384673,3.721892,5.898167,-1.175148,7.751019,2.521922,8.499820],[7.621491,8.771644,6.183070,-3.503315,-6.421494,-4.362209,7.882420],[9.440425,-3.500156,-2.140718,6.910418,1.747503,-4.062837,-3.363022],[-3.644117,-0.357325,-7.960804,-2.234679,-0.793047,0.517747,3.762135],[9.676763,-6.224793,-5.740648,4.524989,-8.065568,-6.815294,-6.090555],[5.913267,-2.019664,-5.756855,1.088033,-9.989161,-4.967181,-6.141564],[-3.006005,-5.652034,-7.784224,-8.655630,3.179287,8.414893,-2.491901],[9.270867,-9.027498,-7.730797,-6.322847,4.039914,1.883648,-7.533182],[5.616074,8.211421,-0.144654,5.458750,-7.022499,1.500875,6.563313]],[[-7.792217,-8.949017,-4.336769,-4.733661,-8.579596,-3.088387,-2.796742],[9.606136,6.803809,4.639017,-1.877999,-6.548142,-2.552430,-8.777545],[8.433332,-4.596564,5.336464,9.406192,6.356907,-4.438082,7.639190],[5.798043,-7.555033,-1.225644,8.520282,8.131521,0.001384,-8.195628],[-1.402782,-5.938162,-1.979087,5.597967,0.901647,-9.479848,-1.988935],[-8.501409,6.093622,7.501078,3.064738,8.361858,9.798793,-8.267538],[5.837924,-8.836547,3.081588,7.572617,6.976586,-8.626101,4.919236],[0.881239,9.647843,7.916300,-6.952638,2.302966,-7.910219,-2.024239],[9.108501,7.463921,5.641953,-3.967737,-7.096364,5.000985,8.236972],[-5.494379,-4.049519,-1.087081,-3.170465,-8.035061,0.310527,-4.571639]],[[-3.398498,4.968069,9.428706,-0.755350,6.994657,-7.360822,-8.445293],[1.846128,4.454436,1.332200,-4.862123,4.483225,3.530273,5.678851],[1.094912,1.983304,-3.079218,6.921563,5.650665,8.765866,9.791146],[-5.727759,5.462146,0.032246,3.055877,-2.457192,-7.580838,-4.677110],[3.684565,-3.918298,6.110009,-7.122786,9.245548,-3.935161,-9.957190],[6.947416,2.777247,6.818230,9.140271,7.460118,1.397441,-8.436368],[4.524983,-8.498603,-4.978360,-2.014536,-6.019013,-2.347955,-7.544607],[-9.799322,-6.678584,-7.471945,7.430491,-5.397735,-9.437102,5.152484],[0.704563,-0.633610,3.069600,5.438390,5.903978,3.541865,-0.691630],[7.787266,-7.672774,3.650722,5.238591,-8.038735,-7.721930,-4.383881]],[[-1.682805,-1.076735,7.184984,8.267198,3.636663,9.159324,-0.311358],[-5.706952,-9.434516,2.957136,9.730981,4.599601,6.645709,9.348561],[-5.158914,-0.549102,-1.045934,-8.516241,8.603059,-0.805342,-0.973074],[-3.268745,-1.166141,6.156086,-9.985444,-2.137643,-9.803838,4.960371],[4.685461,2.498326,-9.437525,5.760998,-0.308326,-2.054868,6.783667],[2.015263,-9.178634,-1.817747,-8.686303,1.138783,-4.377649,8.485912],[1.745266,-0.785058,8.041092,-7.635718,-8.535991,-6.354292,2.508619],[-3.754044,3.689804,-1.362879,4.122891,3.122259,6.628911,5.528903],[-0.361928,-3.527189,6.914480,-4.025301,-8.073432,-6.580569,-0.739754],[4.528016,2.401858,-4.872460,3.370694,4.093376,0.922670,5.696819]],[[7.161088,1.708033,4.063633,-2.493650,-2.525708,4.598091,3.525247],[7.466111,2.472682,-6.524541,2.306082,4.249430,8.617089,3.235361],[5.593336,8.187262,0.645843,-3.869957,-6.015730,7.079292,-3.101046],[8.651108,-9.407142,3.401497,-1.272621,2.361784,0.687511,-2.930348],[4.522192,9.648297,-5.468083,7.115653,7.477659,-9.518214,-5.850923],[0.087227,0.021003,5.092170,1.800475,9.421845,-6.707620,4.520606],[9.651828,-6.376575,-7.222473,-5.782788,8.224663,-1.822666,9.391400],[-3.969523,9.262373,-2.128298,0.409537,-1.271548,4.846900,-2.413567],[-8.057496,7.235072,4.719010,-5.928630,0.253584,7.846134,2.371925],[-4.537871,-7.764639,-3.386024,-8.663611,-5.459430,-0.322877,-8.972978]],[[-7.122908,5.675908,6.776566,7.190030,2.873679,-3.922234,-2.548428],[3.628818,5.565108,-0.817766,-9.155207,9.813966,-8.082176,-6.493531],[7.465743,-0.907438,7.681611,-6.785507,-6.740714,-9.249512,-6.871254],[-1.595859,-4.070643,-4.330817,1.221912,1.178730,9.677371,-5.383055],[5.989226,1.542737,-6.413427,-3.405178,8.364328,-1.147827,-6.183759],[5.469708,1.787774,0.398157,8.913121,7.966182,2.757372,2.784997],[-0.262735,-1.763459,-0.920410,-8.258779,8.544821,4.499022,5.207030],[-0.507175,-4.306556,-8.279565,5.368278,1.589683,1.366539,-4.582340],[3.901393,-9.537938,3.726142,3.752785,-1.196761,-3.868858,6.186744],[-3.068867,4.398837,-2.076540,6.304759,3.094073,2.502689,6.521841]]], dtype = "float32")#candidate|11828|(12, 10, 7)|const|float32
uop_11829 = relay.asin(const_11828.astype('float32')) # shape=(12, 10, 7)
bop_11831 = relay.greater(const_11828.astype('bool'), relay.reshape(uop_11829.astype('bool'), relay.shape_of(const_11828))) # shape=(12, 10, 7)
uop_11839 = relay.sinh(bop_11831.astype('float32')) # shape=(12, 10, 7)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_11841 = func_11516_call()
call_11842 = func_11516_call()
output = relay.Tuple([uop_11839,call_11841,])
output2 = relay.Tuple([uop_11839,call_11842,])
func_11849 = relay.Function([], output)
mod['func_11849'] = func_11849
mod = relay.transform.InferType()(mod)
mutated_mod['func_11849'] = func_11849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11849_call = mutated_mod.get_global_var('func_11849')
call_11850 = func_11849_call()
output = call_11850
func_11851 = relay.Function([], output)
mutated_mod['func_11851'] = func_11851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11604_call = mod.get_global_var('func_11604')
func_11605_call = mutated_mod.get_global_var('func_11605')
call_11876 = relay.TupleGetItem(func_11604_call(), 0)
call_11877 = relay.TupleGetItem(func_11605_call(), 0)
output = call_11876
output2 = call_11877
func_11878 = relay.Function([], output)
mod['func_11878'] = func_11878
mod = relay.transform.InferType()(mod)
mutated_mod['func_11878'] = func_11878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11878_call = mutated_mod.get_global_var('func_11878')
call_11879 = func_11878_call()
output = call_11879
func_11880 = relay.Function([], output)
mutated_mod['func_11880'] = func_11880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10119_call = mod.get_global_var('func_10119')
func_10120_call = mutated_mod.get_global_var('func_10120')
call_11923 = relay.TupleGetItem(func_10119_call(), 0)
call_11924 = relay.TupleGetItem(func_10120_call(), 0)
func_11771_call = mod.get_global_var('func_11771')
func_11773_call = mutated_mod.get_global_var('func_11773')
call_11926 = relay.TupleGetItem(func_11771_call(), 0)
call_11927 = relay.TupleGetItem(func_11773_call(), 0)
output = relay.Tuple([call_11923,call_11926,])
output2 = relay.Tuple([call_11924,call_11927,])
func_11928 = relay.Function([], output)
mod['func_11928'] = func_11928
mod = relay.transform.InferType()(mod)
output = func_11928()
func_11929 = relay.Function([], output)
mutated_mod['func_11929'] = func_11929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_11978 = func_11516_call()
call_11979 = func_11516_call()
output = call_11978
output2 = call_11979
func_11991 = relay.Function([], output)
mod['func_11991'] = func_11991
mod = relay.transform.InferType()(mod)
output = func_11991()
func_11992 = relay.Function([], output)
mutated_mod['func_11992'] = func_11992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_12058 = func_11087_call()
call_12059 = func_11087_call()
output = call_12058
output2 = call_12059
func_12062 = relay.Function([], output)
mod['func_12062'] = func_12062
mod = relay.transform.InferType()(mod)
mutated_mod['func_12062'] = func_12062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12062_call = mutated_mod.get_global_var('func_12062')
call_12063 = func_12062_call()
output = call_12063
func_12064 = relay.Function([], output)
mutated_mod['func_12064'] = func_12064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11991_call = mod.get_global_var('func_11991')
func_11992_call = mutated_mod.get_global_var('func_11992')
call_12070 = func_11991_call()
call_12071 = func_11991_call()
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_12086 = func_11087_call()
call_12087 = func_11087_call()
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_12093 = relay.var("var_12093", dtype = "bool", shape = (117,))#candidate|12093|(117,)|var|bool
const_12094 = relay.const([[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True]], dtype = "bool")#candidate|12094|(702, 1)|const|bool
var_12095 = relay.var("var_12095", dtype = "float32", shape = (320,))#candidate|12095|(320,)|var|float32
const_12096 = relay.const([7.477516,-8.784081,1.641078,-7.312024,9.026896,-5.156194,8.459436,-4.186160,-8.861237,-2.287928,4.045447,-9.664668,-9.854880,-6.677559,-4.734647,7.001092,1.454634,1.915464,-0.826062,-7.296409,7.237422,-5.854578,-0.190013,0.457379,-2.566547,2.869876,0.793526,-7.996276,4.334590,1.856901,-1.342235,-6.266514,9.240123,-1.381001,3.734081,1.937218,-4.420842,7.192219,-2.357988,5.303175,0.527282,-8.564872,-7.055932,-4.676575,6.556794,5.552425,3.666241,6.839293,0.290388,-9.461318,5.260526,3.796844,-4.261142,-0.501785,-6.495784,7.616968,5.965932,-6.982119,-9.253826,4.616329,-9.122428,7.250887,-9.870148,-0.529740,8.139029,-4.090353,-5.743340,-4.128924,6.784951,-8.479437,-6.669432,7.864644,7.088593,5.062385,-0.883056,-1.157339,-1.987779,-7.578681,-8.482746,-4.206468,-7.258109,-1.350579,7.859168,1.701207,-9.827332,-2.234532,8.295330,-5.373483,8.172673,1.105160,-6.344895,-2.248656,4.492310,-7.416484,-4.719511,7.401633,1.006914,8.966336,-3.393174,7.894361,-5.331113,0.295026,8.093389,4.745350,-0.263073,0.491775,-7.328007,3.348951,-3.586708,1.760590,-5.199715,0.108634,2.713502,-9.243012,4.145798,-1.933988,2.225510,-0.567061,9.940787,2.532064,-5.941155,-7.713824,3.932935,-7.004377,7.824820,-3.470503,9.061336,-1.064172,-5.104314,-5.182051,-4.555885,-3.965860], dtype = "float32")#candidate|12096|(132,)|const|float32
const_12097 = relay.const([-2,1,-6,1,7,3,8,-6,4,-4,-5,3,-1,10,-5,-7,9,-6,10,-1,7,9,-5,-2,5,3,5,1,-1,9,4,-5,-5,10,-8,2,-4,-3,-6,-8,-3,2,-5,5,-5,-5,2,4,1,-3,-6,6,-6,8,8,-4,7,10,-10,-9,1,6,4,-3,5,-5,10,10,2,7,-4,-10,6,4,-7,3,-8,1,8,-8,7,3,-5,-3,-8,9,-9,6,9,3,6,-3,-4,8,-8,6,-10,-3,9,3,6,3,1,1,1,7,10,4,4,-8,8,10,-5,2,8,-5,-9,10,-10,-3,4,10,2,10,6,10,5,2,2,-4,-1,-7,-9,-2,7,-2,7,-9,-6,5,-8,-5,-5,-3,-1,7,7,-2,-10,-5,-10,-2,-9,-6,-1,-8,-5,1,8,-7,10,8,-10,6,-7,-1,-10,-3,-3,5,-9,-2,-3,-6,-7,-9,1,-8,10,-2,-5,-3,5,3,5,1,-2,-10,-8,-8,-3,3,4,4,-3,10,-9,-2,-1,2,4,1,8,1,-10,-10,3,7,-3,3,1,-6,10,-7,-3,-6,4,-3,9,-6,-2,-3,10,-4,5,10,5,-6,-4,-6,2,5,1,8,-3,-10,1,-10,7,3,-5,8,1,-7,-9,-1,6,6,-4,-9,9,2,5,2,-7,-4,9,4,-5,2,-5,4,-1,-9,5,3,-7,5,-8,4,1,10,9,8,7,10,7,3,4,-4,-10,-4,-2,9,-5,5,-2,-6,1,4,5,9,-8,9,-2,5,-10,9,8,-1,-2,9,-3,4,8,-1,-4,7,1,-7,1,-7,1,-2,-7,-3,9,-4,8,6,7,-1,10,-6,5,5,5,6,9,8,9,4,5,2,-5,-9,10,7,9,-8,-9,2,-7,4,6,-2,3,-5,-4,-2,-9,-5,-5,6,8,-10,-9,4,1,-1,-8,-2,-1,-1,-7,-5,-6,-3,5,-4,-7,3,-7,3,-5,-4,9,5,-6,4,9,-10,-2,-5,4,3,4,-9,-2,-10,7,9,-2,6,1,3,-1,-5,6,1,9,-5,-9,5,-7,6,9,-1,-10,-10,9,10,-4,7,7,4,-2,-1,3,2,-9,3,-4,8,3,6,9,4,-5,7,-8,9,10,-3,-4,-3,3,-10,10,4,5,-5,-10,-2,-1,6,-10,1,3,-2,-9,1,-3,-1,-10,-6,5,-3,-2,9,-2,5,9,3,-10,-10,-2,-10,-5,-5,6,-4,-5,-7,10,4,-2,-5,5,-5,-2,5,-8,-8,8,10,7,8,-8,10,-2,1,3,4,-5,4,-4,1,6,4,3,9,-7,1,-1,-5,-7,-6,4,8,-9,-7,9,-4,9,8,-4,-1,3,8,7,6,10,4,-2,-5,3,3,-4,-9,-6,3,6,-1,-10,-3,-2,10,-1,-10,-5,3,9,-3,2,5,1,-8,-4,7,9,10,1,5,-4,-6,-10,-8,4,3,3,1,-6,10,9,-5,-7,10,-6,-9,-8,9,3,-10,-1,10,8,8,2,5,5,-10,4,-10,4,1,6,1,-9,6,-3,4,2,7,-9,-5,-2,-9,-6,-9,2,-2,9,-8,4,10,2,9,5,-8,-8,-1,2,7,10,-6,-5,1,-2,6,-4,-1,2,2,4,4,-5,-2,-6,4,-6,-8,-9,-7,-7,6,9,10,5,-1,-2,-3,-3,-5,-6,4,-1,3,9,-10,-4,10,4,-7,1,-2,-4,-1,1,-5], dtype = "uint64")#candidate|12097|(660,)|const|uint64
call_12092 = relay.TupleGetItem(func_2538_call(relay.reshape(var_12093.astype('bool'), [9, 13, 1]), relay.reshape(const_12094.astype('bool'), [9, 13, 6]), relay.reshape(var_12095.astype('float32'), [320,]), relay.reshape(const_12096.astype('float32'), [132,]), relay.reshape(const_12097.astype('uint64'), [330, 2]), ), 5)
call_12098 = relay.TupleGetItem(func_2544_call(relay.reshape(var_12093.astype('bool'), [9, 13, 1]), relay.reshape(const_12094.astype('bool'), [9, 13, 6]), relay.reshape(var_12095.astype('float32'), [320,]), relay.reshape(const_12096.astype('float32'), [132,]), relay.reshape(const_12097.astype('uint64'), [330, 2]), ), 5)
uop_12109 = relay.atanh(const_12096.astype('float32')) # shape=(132,)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_12111 = relay.TupleGetItem(func_8318_call(), 0)
call_12112 = relay.TupleGetItem(func_8319_call(), 0)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_12115 = relay.TupleGetItem(func_8318_call(), 0)
call_12116 = relay.TupleGetItem(func_8319_call(), 0)
output = relay.Tuple([call_12070,call_12086,call_12092,var_12093,const_12094,var_12095,const_12097,uop_12109,call_12111,call_12115,])
output2 = relay.Tuple([call_12071,call_12087,call_12098,var_12093,const_12094,var_12095,const_12097,uop_12109,call_12112,call_12116,])
func_12119 = relay.Function([var_12093,var_12095,], output)
mod['func_12119'] = func_12119
mod = relay.transform.InferType()(mod)
mutated_mod['func_12119'] = func_12119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12119_call = mutated_mod.get_global_var('func_12119')
var_12121 = relay.var("var_12121", dtype = "bool", shape = (117,))#candidate|12121|(117,)|var|bool
var_12122 = relay.var("var_12122", dtype = "float32", shape = (320,))#candidate|12122|(320,)|var|float32
call_12120 = func_12119_call(var_12121,var_12122,)
output = call_12120
func_12123 = relay.Function([var_12121,var_12122,], output)
mutated_mod['func_12123'] = func_12123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8644_call = mod.get_global_var('func_8644')
func_8645_call = mutated_mod.get_global_var('func_8645')
call_12136 = func_8644_call()
call_12137 = func_8644_call()
output = call_12136
output2 = call_12137
func_12145 = relay.Function([], output)
mod['func_12145'] = func_12145
mod = relay.transform.InferType()(mod)
mutated_mod['func_12145'] = func_12145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12145_call = mutated_mod.get_global_var('func_12145')
call_12146 = func_12145_call()
output = call_12146
func_12147 = relay.Function([], output)
mutated_mod['func_12147'] = func_12147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12194 = relay.var("var_12194", dtype = "float32", shape = ())#candidate|12194|()|var|float32
const_12195 = relay.const([[[2.995477,-7.447458,1.081887,0.503708,-8.658560,0.603627,2.884399],[6.902891,-4.868839,2.575998,8.387805,6.234762,6.235007,5.896323],[5.333793,1.431481,3.844601,9.934169,3.119088,-3.431225,-6.033070],[5.669059,7.804321,1.187457,-1.608485,-6.876208,5.131308,-0.684387],[-3.200285,2.373144,-9.785891,0.167100,9.878215,-2.782828,8.062913]],[[-7.183839,1.811551,2.659264,6.324888,-8.330892,7.834783,0.315395],[-3.666501,-0.471676,6.578488,6.909190,-2.664777,4.840023,8.847433],[-8.459114,-8.377098,-4.007290,5.096217,8.655561,1.355697,-4.863043],[-0.711926,4.102910,5.593733,-2.613577,2.573702,-4.541015,-3.868921],[8.309655,1.737821,-2.480153,1.187780,6.285416,-5.536916,7.603590]],[[-7.581932,-3.091793,7.730820,-6.766455,2.222137,4.860492,-4.213558],[-1.407625,9.295720,-3.947889,-6.219127,-8.684746,-7.708670,-1.272600],[-7.723729,-7.442729,9.669886,-6.095661,-0.339971,3.265247,2.001639],[-6.437774,-5.215902,-4.030455,9.269110,-9.542343,5.388843,7.240222],[0.901417,-8.927014,7.007253,-0.708353,8.526731,4.486057,9.457625]],[[-9.180397,8.750959,-5.271014,7.976969,1.173976,-3.587287,-2.092847],[-4.871615,8.907844,4.116819,-5.964102,-2.338614,2.243037,7.664372],[4.055561,7.550582,2.021240,-3.113463,-7.338596,-7.267651,-7.869177],[-0.581835,-7.871081,-2.940613,-0.267746,8.948092,-3.834604,6.009331],[4.285684,-1.795425,-2.303174,-6.066677,-7.090071,2.375988,4.149347]],[[-5.326656,-2.009195,-1.429564,-7.600790,-6.623373,7.704633,7.165067],[7.950792,3.908178,9.408187,3.997461,-7.493374,8.376313,7.260305],[1.028029,-1.224971,-7.241880,-2.383281,7.775193,-7.472333,3.044643],[5.336688,1.234879,-2.777656,7.348614,9.874319,6.284184,4.794883],[-8.111637,2.644584,7.465328,-5.727031,3.469054,-0.953136,6.775112]],[[-8.184105,-0.238222,0.151798,3.901438,0.193976,1.920573,2.230335],[-0.517886,2.630162,4.722369,-5.173926,-3.504757,9.026545,-1.997530],[-9.755483,-7.705422,-3.315091,-4.277702,-0.368540,9.094806,-7.719334],[-2.189404,5.900355,-1.525634,-3.055245,-3.055222,-5.197221,3.092695],[-4.362663,-8.553213,4.586649,9.619422,0.139081,9.375643,3.645896]],[[2.310510,3.747481,-8.380499,-6.055576,1.860842,-6.939361,-8.138413],[-1.014097,-8.511734,8.741804,3.211621,2.684170,-0.127820,-7.354363],[6.794463,3.226808,0.242031,-5.181091,9.815920,7.926066,1.232874],[-6.447493,-9.352447,9.699388,1.521850,4.757397,1.836871,-8.219820],[-7.390407,3.215125,-9.929324,-6.174271,3.761598,2.051168,-3.723889]],[[7.284037,4.515801,8.090309,-3.584236,-1.899560,7.366719,-8.662391],[3.207276,-8.475246,9.231154,6.115725,-3.147005,-2.504748,-8.360156],[8.270320,-3.325089,8.654625,-9.664166,2.500049,5.109351,9.989273],[-9.252148,-4.355058,-3.673575,9.732578,-0.427542,0.058031,-6.669298],[5.885361,-5.592260,6.538530,2.840878,-2.038112,2.539691,6.530615]],[[4.879871,8.851370,-9.520194,4.388273,3.433169,3.307166,2.874465],[-3.158082,-6.871962,0.302976,-1.696172,1.062121,6.886486,-2.662209],[7.671673,4.449902,-3.041658,-2.707067,-9.445256,2.573545,-5.896759],[-9.692929,6.314218,-9.568601,-5.740793,-9.834080,-7.049274,-0.952898],[0.616434,5.252590,-2.199648,-6.312235,4.924331,-9.912974,-6.109443]],[[6.155027,-9.839364,8.029944,2.698497,3.652575,2.034460,-8.255733],[0.966835,0.684252,6.847432,9.839740,7.293030,-8.856156,5.284156],[6.918918,-1.296658,-5.753993,-0.985807,3.646458,8.941483,2.088366],[-8.288838,1.176410,-7.234741,1.379725,1.130197,-5.095231,-4.818927],[5.438254,2.559551,5.071877,-0.748151,-5.137073,5.783935,-1.001660]],[[-2.381878,5.372212,0.110874,-3.255243,5.045410,-6.500514,-2.161835],[-7.382747,5.357271,-3.839317,-9.384282,2.674712,-3.772397,8.202293],[7.425064,-9.273126,2.645923,-8.268691,-0.959323,-5.906371,-1.412434],[-7.559480,7.156223,5.855259,2.605466,1.923003,-9.098115,-2.438867],[-7.786618,-8.695215,9.125663,1.176667,2.222812,5.894358,-3.462906]],[[8.546193,-7.459074,-7.386361,-0.732524,0.957994,2.066541,1.343157],[6.330842,-6.784192,4.406800,6.669505,-8.024866,2.276213,-6.398276],[5.041087,1.263286,-8.993131,6.741232,7.866003,-1.795797,6.371923],[-6.524902,3.636567,-7.869903,3.167315,0.911826,-0.021388,-6.980862],[9.446986,-9.368187,6.425982,2.848053,-8.203210,-8.290002,0.173323]],[[-3.718839,5.565371,5.256979,-7.843593,-4.694796,-4.856967,-6.817053],[1.861711,-9.110279,3.423930,-6.149985,-3.997354,-0.172111,-2.170021],[3.881390,-9.583027,-2.231876,-2.235980,-9.131507,4.046640,-0.099081],[-7.665023,-2.844924,8.714012,-4.009640,8.692080,-4.503540,7.102243],[-0.012184,6.812927,3.810645,4.198226,8.010487,7.160146,-0.796657]]], dtype = "float32")#candidate|12195|(13, 5, 7)|const|float32
bop_12196 = relay.floor_mod(var_12194.astype('float32'), const_12195.astype('float32')) # shape=(13, 5, 7)
output = relay.Tuple([bop_12196,])
output2 = relay.Tuple([bop_12196,])
func_12202 = relay.Function([var_12194,], output)
mod['func_12202'] = func_12202
mod = relay.transform.InferType()(mod)
var_12203 = relay.var("var_12203", dtype = "float32", shape = ())#candidate|12203|()|var|float32
output = func_12202(var_12203)
func_12204 = relay.Function([var_12203], output)
mutated_mod['func_12204'] = func_12204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11478_call = mod.get_global_var('func_11478')
func_11480_call = mutated_mod.get_global_var('func_11480')
call_12206 = func_11478_call()
call_12207 = func_11478_call()
output = relay.Tuple([call_12206,])
output2 = relay.Tuple([call_12207,])
func_12217 = relay.Function([], output)
mod['func_12217'] = func_12217
mod = relay.transform.InferType()(mod)
output = func_12217()
func_12218 = relay.Function([], output)
mutated_mod['func_12218'] = func_12218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_12255 = relay.TupleGetItem(func_8318_call(), 0)
call_12256 = relay.TupleGetItem(func_8319_call(), 0)
func_10419_call = mod.get_global_var('func_10419')
func_10423_call = mutated_mod.get_global_var('func_10423')
const_12262 = relay.const([-2.443396,-5.913120,8.056008,2.806373,-2.661551,-7.318332,7.718096,2.471501,-0.099231,-3.297275,7.520472,2.587256,-9.706525,6.414071,5.838532,-7.452179,8.875234,5.943815,8.531216,2.647131,-8.871542,-3.635666,-2.572812,-2.804228,-6.229979,-2.728441,-8.190682,-3.602189,5.738194,-2.386107,8.816572,-7.420020,-6.322153,-6.310982,2.696907,9.723886,3.812839,4.341076,5.116198,-8.945444], dtype = "float32")#candidate|12262|(40,)|const|float32
const_12263 = relay.const([[-6,-1],[2,-4],[-6,8],[7,-6],[-3,4],[9,1],[9,8],[5,1],[4,4],[10,9],[-4,-8],[2,5],[10,-1],[9,-7],[-3,-4],[-2,10],[6,3],[3,6],[8,-6],[9,8],[-3,8],[-2,-10],[1,-3],[-8,-8],[8,2],[3,7],[-1,-4],[8,-10],[10,5],[-5,6],[9,-9],[-4,-9],[10,4],[-9,-7],[-7,3],[-10,8],[-2,-1],[-8,-3],[8,-1],[-10,-7],[-4,-4],[-5,3],[1,-9],[8,-10],[-10,5],[9,4],[1,2],[-8,2],[1,4],[8,-9],[-3,7],[-4,4],[-9,4],[9,7],[-3,-1],[-9,2],[-8,7],[-6,-2],[-5,-4],[7,4],[7,6],[-6,-5],[-4,-2],[7,7],[2,1],[2,-9],[-4,5],[1,9],[-7,-1],[10,2],[2,6],[-7,5],[7,-9],[9,6],[-3,7],[10,1],[3,-10],[9,6],[7,-9],[7,8],[-9,-4],[7,4],[-1,-5],[8,-10],[-7,5],[-6,7],[5,10],[1,-7],[-4,-1],[-3,2],[-7,-6],[-10,-6],[-1,-7],[2,-2],[2,-10],[-9,5],[7,4],[-2,-5],[1,2],[10,-2],[-10,7],[3,-10],[1,-7],[-6,4],[8,-5],[-4,9],[-2,9],[-10,-2],[-10,-4],[-10,7],[6,-2],[8,-8],[-1,7],[3,-3],[9,-6],[4,1],[9,-8],[-4,8],[1,-2],[5,-5],[1,4],[-10,-9],[-8,9],[-3,8],[10,8],[-1,1],[8,10],[3,2],[7,-10],[-2,5],[-1,1],[-7,-5],[5,10],[-2,7],[-6,5],[-10,3],[-2,4],[1,-5],[-8,-8],[5,3],[-9,-7],[5,2],[1,-1],[6,-10],[-9,4],[8,2],[-6,-10],[-4,-3],[3,5],[-4,-9],[6,-7],[6,-5],[-4,2],[-8,5],[-7,-9],[7,5],[3,-9],[-6,-1],[-8,7],[6,6],[-2,-1],[5,6],[-2,-2],[-8,8],[-6,8],[5,8],[-8,7],[8,-3],[4,-1],[-9,-10],[4,7],[-10,5],[1,-1],[3,-2],[-4,-4],[-4,1],[10,-8],[8,9],[1,-6],[-2,-10],[4,-1],[-1,-7],[-2,7],[9,-4],[9,9],[10,-1],[-3,-4],[10,10],[-5,3],[4,3],[3,1],[-8,-3],[9,-6],[10,-9],[-8,10],[9,2],[-2,2],[-4,-3],[-2,3],[1,7],[-9,-8],[2,-4],[10,-8],[5,-5],[-4,-5],[1,-9],[2,3],[7,-3],[4,-5],[-9,-7],[-2,-10],[-7,-8],[-1,1],[-8,-4],[-2,6],[-8,-4],[-10,-1],[8,8],[4,-9],[-4,-2],[-9,-6],[5,9],[-7,-5],[-2,7],[7,-9],[-5,5],[8,2],[2,-4],[9,7],[-9,1],[9,-1],[6,3],[6,-10],[-2,2],[-10,9],[-8,-2],[4,-1],[6,-9],[10,6],[-5,-1],[2,4],[8,-1],[10,-2],[-4,7],[6,10],[-2,6],[8,9],[-2,4],[4,9],[6,10],[-1,-6],[9,-4],[-1,-6],[3,8],[8,5],[-10,6],[-9,-5],[7,10],[-10,-3],[-10,-5],[-1,-8],[4,6],[-3,-4],[9,6],[6,-4],[-7,-1],[1,-7],[2,3],[-2,8],[7,10],[4,-3],[-5,-3],[-10,-2],[-1,5],[8,4],[3,-1],[-10,-5],[-2,9],[10,-1],[2,-3],[-8,1],[-1,-1],[8,7],[3,-10],[-1,-2],[-9,-1],[4,1],[-3,-10],[3,-2],[8,3],[9,1],[10,-4],[4,5],[8,2],[7,10],[10,-3],[-1,-7],[-6,-7],[2,6],[-9,4],[8,-9],[-5,-10],[4,2],[-10,-7],[8,10],[-6,-1],[-6,2],[-9,1],[4,-8],[8,-1],[6,6],[-6,6],[1,-10],[-4,-7],[9,-8],[-4,10],[6,8],[5,-8],[-3,-6],[-1,5],[-10,-1],[7,5],[-7,-6],[9,-10],[-3,-2],[-10,-9],[7,1],[10,2],[-10,-4],[-10,5]], dtype = "uint64")#candidate|12263|(330, 2)|const|uint64
call_12261 = relay.TupleGetItem(func_10419_call(relay.reshape(const_12262.astype('float32'), [40,]), relay.reshape(const_12263.astype('uint64'), [660,]), ), 4)
call_12264 = relay.TupleGetItem(func_10423_call(relay.reshape(const_12262.astype('float32'), [40,]), relay.reshape(const_12263.astype('uint64'), [660,]), ), 4)
uop_12287 = relay.asin(call_12261.astype('float32')) # shape=(240, 1)
uop_12289 = relay.asin(call_12264.astype('float32')) # shape=(240, 1)
output = relay.Tuple([call_12255,const_12262,const_12263,uop_12287,])
output2 = relay.Tuple([call_12256,const_12262,const_12263,uop_12289,])
func_12290 = relay.Function([], output)
mod['func_12290'] = func_12290
mod = relay.transform.InferType()(mod)
output = func_12290()
func_12291 = relay.Function([], output)
mutated_mod['func_12291'] = func_12291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_12322 = relay.TupleGetItem(func_10157_call(), 0)
call_12323 = relay.TupleGetItem(func_10159_call(), 0)
output = call_12322
output2 = call_12323
func_12326 = relay.Function([], output)
mod['func_12326'] = func_12326
mod = relay.transform.InferType()(mod)
mutated_mod['func_12326'] = func_12326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12326_call = mutated_mod.get_global_var('func_12326')
call_12327 = func_12326_call()
output = call_12327
func_12328 = relay.Function([], output)
mutated_mod['func_12328'] = func_12328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11122_call = mod.get_global_var('func_11122')
func_11123_call = mutated_mod.get_global_var('func_11123')
call_12353 = func_11122_call()
call_12354 = func_11122_call()
func_12290_call = mod.get_global_var('func_12290')
func_12291_call = mutated_mod.get_global_var('func_12291')
call_12355 = relay.TupleGetItem(func_12290_call(), 3)
call_12356 = relay.TupleGetItem(func_12291_call(), 3)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_12361 = relay.var("var_12361", dtype = "bool", shape = (117,))#candidate|12361|(117,)|var|bool
var_12362 = relay.var("var_12362", dtype = "bool", shape = (702,))#candidate|12362|(702,)|var|bool
const_12363 = relay.const([-6.536310,0.335873,0.966591,-9.980303,-9.529864,4.323727,-1.852665,3.364155,-5.146547,-5.145413,-5.436582,-3.106570,-0.962595,-1.024840,-1.262771,5.682080,0.308503,-4.294658,2.049994,0.281121,1.825932,-9.609734,-0.812927,-1.319521,-8.502912,-8.135750,-4.136988,-8.978685,2.666303,1.014575,9.526350,2.854041,6.471411,-1.171337,-3.344144,5.425588,-6.294696,0.331325,8.851266,4.621632,3.276098,-7.960275,0.064934,-8.199310,2.120332,-3.809381,-0.902990,5.515757,2.283058,-4.259135,-2.509300,8.973631,3.327492,9.537107,-0.170293,0.757862,-9.319767,6.458602,-4.892921,5.340802,9.980223,-3.907368,2.710214,-0.857117,0.757339,-0.906365,-9.382388,-0.216753,-0.894387,-8.615740,1.848950,-3.500281,4.938027,0.751291,4.042353,-0.396514,-4.859094,-2.239798,-2.425500,-8.408934,6.605261,9.538787,-6.246221,-2.824407,-3.874336,5.280479,-3.906229,9.139772,8.985865,7.941701,5.319846,-2.826586,-1.318947,5.610764,7.788205,3.172173,-3.648572,-7.645755,-0.588643,-0.815297,6.441655,-2.271558,6.879278,4.768036,-3.061872,-8.888341,-0.834899,8.489118,4.521285,-9.572901,-1.212887,-8.447006,-9.495414,0.400130,7.482213,4.995747,7.117302,-2.400365,-6.934620,-0.345971,-8.920356,-0.132750,3.411133,0.464337,2.752347,2.334120,8.248486,-2.856574,-5.272927,6.456486,8.315778,-2.156302,-6.046949,-2.746352,-6.750358,-8.609881,0.843706,-1.846632,-9.578644,4.003638,5.001727,-6.132501,-0.171922,-1.177213,-6.735738,-8.776593,2.605038,8.840971,7.240653,-4.195483,-2.190318,-6.308214,2.219062,-1.503470,1.049886,1.883762,-9.110924,1.155935,1.734545,2.421576,8.331193,2.376593,-7.339215,3.095433,-1.958619,6.179986,-1.601993,-7.856810,-5.875734,9.472303,5.034214,-0.005683,-7.336036,-5.794984,-7.742923,-4.558801,-6.911145,-5.890843,-7.395472,-2.219768,7.334081,1.639158,-0.059352,9.705609,-3.704014,-0.399628,-8.519925,3.073987,-7.985363,-0.160630,7.434547,1.214829,-6.313190,-6.214451,2.639779,-8.183888,-5.087057,-9.655815,2.587268,-7.125015,-6.192863,1.057367,3.023932,-0.833842,7.684231,-4.140641,8.944983,-4.498972,8.204425,-2.390348,3.723205,5.399383,-9.579931,-5.151773,-7.712042,7.326861,1.559302,9.293325,4.965183,2.910479,-6.764049,0.623108,4.230234,7.986005,-9.777554,2.355408,-4.775756,1.216641,-4.262382,1.480812,-5.289162,2.755209,5.863774,8.259535,-5.050526,7.614853,-8.745605,-5.722041,-5.445972,1.291316,4.838905,0.162487,4.269722,-4.086441,-4.378498,-0.784832,-1.564111,0.718596,-3.599366,-9.608759,5.823937,9.991437,-5.141452,9.602755,-0.642044,6.653616,9.114744,9.234981,-9.224763,-2.341826,3.598152,1.036839,-9.550063,-1.973016,8.029826,-7.416617,-3.036433,0.055420,6.446265,-9.101687,4.470847,-2.846366,-2.177805,2.189794,2.318232,4.245905,7.807936,9.858158,7.988463,-2.883041,-2.902178,7.677641,2.780534,-7.739144,0.151462,-6.928481,-4.526905,2.525673,-8.865222,4.293113,-5.852878,3.239706,-5.555219,-2.881269,-6.636768,-4.338515,3.698741,5.183440,-7.630253,5.863536,-3.633042,-3.083207,-6.690485,2.144777,8.529121,4.170601,-2.818851,3.340660,7.843168,-4.866308,-2.212628,-8.625191,8.477849,-6.422505,6.119079,0.473168,8.706338,7.565692,-8.203084,2.058938], dtype = "float32")#candidate|12363|(320,)|const|float32
const_12364 = relay.const([1.956964,-3.338488,-7.562165,-9.228094,-3.421147,-1.224580,-7.058244,1.045082,3.761077,-9.792614,9.156290,-9.442656,-3.152931,7.085528,-6.573632,8.920554,9.356823,-8.840219,6.583273,-3.634292,-3.106839,8.471037,-6.610730,-0.417041,2.197332,-8.725319,-4.443371,-8.272571,-7.265081,2.899708,8.279988,-9.113235,-6.721330,-7.355672,1.906835,9.733022,-2.957920,6.106865,-2.825624,-7.621411,-9.718898,-2.243634,4.030118,1.264611,-1.238643,0.668003,-5.949423,-6.190465,-1.007036,-2.859884,9.998734,8.380296,-5.381527,-9.614193,8.883608,-9.629614,-9.803642,-7.939858,-1.196783,4.783834,-2.354013,-9.026779,0.620110,-1.658154,3.030370,5.554081,-3.386549,-7.543290,1.693034,8.605221,8.640028,-8.896621,-2.901283,-3.208182,5.283681,8.638039,-9.142006,-6.854667,-2.776201,7.394479,7.907729,2.441220,-3.101594,-0.800472,-8.774394,-9.981028,9.248507,9.410624,3.371687,-8.406804,-6.631145,7.530657,3.728609,-7.990924,-7.487190,-6.630619,-7.624027,9.436264,0.182413,8.232455,-8.919642,-1.773615,-2.130070,9.064692,0.543614,-0.136225,-1.228814,-4.106104,7.674048,0.804574,-0.705376,3.823088,3.220958,2.086314,-1.375870,6.995756,-4.404518,2.929630,1.461196,1.186197,-0.655551,-6.430774,3.560240,9.850148,0.034077,-8.738907,-9.380741,1.564194,-2.676233,-2.708044,3.518398,5.131418], dtype = "float32")#candidate|12364|(132,)|const|float32
const_12365 = relay.const([10,2,-10,-1,-3,-6,-6,-4,-6,-2,-2,5,-2,-10,7,-6,7,8,-10,-4,1,-8,4,8,4,6,-4,-3,4,-1,-3,1,-6,-7,-7,-9,-5,-7,-9,-9,-8,-3,8,1,9,4,-1,-2,-3,3,-2,-2,1,5,6,-7,1,-9,5,-10,1,6,2,-9,7,-6,-8,5,10,3,6,-2,-9,-5,-10,9,-10,3,3,6,6,8,-2,5,-6,8,8,6,-1,-2,-5,-2,7,8,7,-9,-10,7,3,4,8,-9,1,4,8,3,-8,-2,-10,5,6,2,-5,10,1,-7,-5,7,-6,2,-8,9,9,3,4,9,-5,8,8,-8,-1,9,-3,-5,-9,3,1,-5,3,-10,-7,-7,-7,-2,2,-5,-7,10,-3,9,2,-1,-3,-3,-6,3,1,-8,6,5,-2,-2,7,8,-9,-1,-10,5,-9,-10,-1,-8,5,-3,6,1,-2,-8,9,8,5,-2,-4,-10,5,-7,5,1,3,-2,-5,8,10,-4,-2,-6,4,3,4,10,-3,6,-4,9,2,-6,-6,4,-8,4,3,-8,7,6,3,1,-4,-4,-5,-6,6,-5,4,-8,-10,-4,-2,1,-4,-3,6,4,2,-8,1,-5,4,9,1,-2,-8,3,1,-1,4,1,-7,-10,3,7,2,2,6,-7,9,-8,-8,-8,7,-5,3,-1,-10,-1,-10,10,-4,1,-4,-5,-10,1,-5,8,-8,3,10,2,-8,5,-3,4,-5,-7,5,-3,6,4,3,-3,6,2,1,-6,-9,9,-3,-9,-7,-1,-8,-7,8,-6,-3,2,5,5,-8,-7,1,-10,8,-5,6,7,-10,-10,4,-9,-5,6,5,-7,2,3,-1,-8,-2,4,-10,-4,5,-9,8,-8,1,2,-7,2,-5,1,-7,5,-3,-7,-1,-3,5,-9,-4,-7,-3,2,9,9,10,-10,-10,-6,5,6,-6,-6,5,-5,2,-5,-2,5,2,5,-6,8,-1,9,-10,4,7,9,3,10,-8,2,-1,-9,-5,-4,-1,-4,-9,-8,9,-8,-10,-10,-3,-10,-5,-8,3,1,6,-6,-2,-9,7,-1,-7,-5,-8,-10,5,-1,-6,1,10,7,9,-3,8,-3,7,-3,5,-1,-3,5,5,-10,-8,-2,3,4,-5,-7,9,9,-4,-10,2,-3,4,-5,-5,-2,8,-1,3,6,-4,-2,1,-1,-6,5,4,-5,7,9,-6,6,3,4,-5,-6,3,4,-9,-10,-7,5,4,-2,-9,-4,-2,-7,-10,-2,3,-5,-4,-2,-5,-2,-7,4,4,-6,-6,7,3,-2,-7,7,10,6,-3,1,-1,10,7,-3,9,5,2,-1,6,-7,8,2,-7,6,-7,8,9,7,-10,-10,-10,4,6,6,-1,-4,-8,-10,5,3,-4,-1,8,2,10,9,-6,-1,-8,-4,-1,-9,5,4,-7,3,7,-6,-1,3,8,-1,-4,-9,-1,-3,-3,3,-6,-7,3,4,-3,-7,7,-6,-3,-3,1,-1,-7,7,9,-8,-7,7,5,2,-2,-2,10,-7,-7,1,-2,-10,-9,9,-7,2,-1,5,-2,4,7,-6,6,-1,-4,10,-5,7,1,1,-10,-3,-5,7,-3,-3,8,7,-5,-8,-1,6,-1,1,8,10,-6,-9,9,-8,8,5,3,2,2,-8,8,-10,-9,-1,-2,5,3,-9,-3,-9,2,-8,7,4,10,2,-10,-9,3,7,2,-5,7,9,3,-2,-3,-2,2,10], dtype = "uint64")#candidate|12365|(660,)|const|uint64
call_12360 = relay.TupleGetItem(func_2538_call(relay.reshape(var_12361.astype('bool'), [9, 13, 1]), relay.reshape(var_12362.astype('bool'), [9, 13, 6]), relay.reshape(const_12363.astype('float32'), [320,]), relay.reshape(const_12364.astype('float32'), [132,]), relay.reshape(const_12365.astype('uint64'), [330, 2]), ), 2)
call_12366 = relay.TupleGetItem(func_2544_call(relay.reshape(var_12361.astype('bool'), [9, 13, 1]), relay.reshape(var_12362.astype('bool'), [9, 13, 6]), relay.reshape(const_12363.astype('float32'), [320,]), relay.reshape(const_12364.astype('float32'), [132,]), relay.reshape(const_12365.astype('uint64'), [330, 2]), ), 2)
uop_12386 = relay.erf(var_12361.astype('float32')) # shape=(117,)
uop_12388 = relay.exp(uop_12386.astype('float64')) # shape=(117,)
func_10091_call = mod.get_global_var('func_10091')
func_10095_call = mutated_mod.get_global_var('func_10095')
call_12393 = relay.TupleGetItem(func_10091_call(relay.reshape(var_12362.astype('bool'), [1, 702]), relay.reshape(const_12364.astype('float32'), [33, 4]), ), 3)
call_12394 = relay.TupleGetItem(func_10095_call(relay.reshape(var_12362.astype('bool'), [1, 702]), relay.reshape(const_12364.astype('float32'), [33, 4]), ), 3)
output = relay.Tuple([call_12353,call_12355,call_12360,var_12362,const_12363,const_12364,const_12365,uop_12388,call_12393,])
output2 = relay.Tuple([call_12354,call_12356,call_12366,var_12362,const_12363,const_12364,const_12365,uop_12388,call_12394,])
func_12397 = relay.Function([var_12361,var_12362,], output)
mod['func_12397'] = func_12397
mod = relay.transform.InferType()(mod)
var_12398 = relay.var("var_12398", dtype = "bool", shape = (117,))#candidate|12398|(117,)|var|bool
var_12399 = relay.var("var_12399", dtype = "bool", shape = (702,))#candidate|12399|(702,)|var|bool
output = func_12397(var_12398,var_12399,)
func_12400 = relay.Function([var_12398,var_12399,], output)
mutated_mod['func_12400'] = func_12400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11122_call = mod.get_global_var('func_11122')
func_11123_call = mutated_mod.get_global_var('func_11123')
call_12415 = func_11122_call()
call_12416 = func_11122_call()
output = call_12415
output2 = call_12416
func_12424 = relay.Function([], output)
mod['func_12424'] = func_12424
mod = relay.transform.InferType()(mod)
output = func_12424()
func_12425 = relay.Function([], output)
mutated_mod['func_12425'] = func_12425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8318_call = mod.get_global_var('func_8318')
func_8319_call = mutated_mod.get_global_var('func_8319')
call_12465 = relay.TupleGetItem(func_8318_call(), 0)
call_12466 = relay.TupleGetItem(func_8319_call(), 0)
output = call_12465
output2 = call_12466
func_12470 = relay.Function([], output)
mod['func_12470'] = func_12470
mod = relay.transform.InferType()(mod)
mutated_mod['func_12470'] = func_12470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12470_call = mutated_mod.get_global_var('func_12470')
call_12471 = func_12470_call()
output = call_12471
func_12472 = relay.Function([], output)
mutated_mod['func_12472'] = func_12472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_12492 = func_11087_call()
call_12493 = func_11087_call()
func_12397_call = mod.get_global_var('func_12397')
func_12400_call = mutated_mod.get_global_var('func_12400')
var_12498 = relay.var("var_12498", dtype = "bool", shape = (117,))#candidate|12498|(117,)|var|bool
var_12499 = relay.var("var_12499", dtype = "bool", shape = (702,))#candidate|12499|(702,)|var|bool
call_12497 = relay.TupleGetItem(func_12397_call(relay.reshape(var_12498.astype('bool'), [117,]), relay.reshape(var_12499.astype('bool'), [702,]), ), 1)
call_12500 = relay.TupleGetItem(func_12400_call(relay.reshape(var_12498.astype('bool'), [117,]), relay.reshape(var_12499.astype('bool'), [702,]), ), 1)
output = relay.Tuple([call_12492,call_12497,var_12498,var_12499,])
output2 = relay.Tuple([call_12493,call_12500,var_12498,var_12499,])
func_12503 = relay.Function([var_12498,var_12499,], output)
mod['func_12503'] = func_12503
mod = relay.transform.InferType()(mod)
var_12504 = relay.var("var_12504", dtype = "bool", shape = (117,))#candidate|12504|(117,)|var|bool
var_12505 = relay.var("var_12505", dtype = "bool", shape = (702,))#candidate|12505|(702,)|var|bool
output = func_12503(var_12504,var_12505,)
func_12506 = relay.Function([var_12504,var_12505,], output)
mutated_mod['func_12506'] = func_12506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_12540 = func_11087_call()
call_12541 = func_11087_call()
output = relay.Tuple([call_12540,])
output2 = relay.Tuple([call_12541,])
func_12542 = relay.Function([], output)
mod['func_12542'] = func_12542
mod = relay.transform.InferType()(mod)
mutated_mod['func_12542'] = func_12542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12542_call = mutated_mod.get_global_var('func_12542')
call_12543 = func_12542_call()
output = call_12543
func_12544 = relay.Function([], output)
mutated_mod['func_12544'] = func_12544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11809_call = mod.get_global_var('func_11809')
func_11810_call = mutated_mod.get_global_var('func_11810')
call_12549 = relay.TupleGetItem(func_11809_call(), 1)
call_12550 = relay.TupleGetItem(func_11810_call(), 1)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
var_12552 = relay.var("var_12552", dtype = "float32", shape = (40,))#candidate|12552|(40,)|var|float32
call_12551 = relay.TupleGetItem(func_1886_call(relay.reshape(var_12552.astype('float32'), [10, 1, 4])), 0)
call_12553 = relay.TupleGetItem(func_1888_call(relay.reshape(var_12552.astype('float32'), [10, 1, 4])), 0)
func_8206_call = mod.get_global_var('func_8206')
func_8208_call = mutated_mod.get_global_var('func_8208')
const_12562 = relay.const([-0.687744,-4.154764,3.798506,-5.564328,7.021654,9.640552,4.533944,-2.581771,1.105697,7.974157,-1.625341,-6.867785,4.756057,4.702958,-6.096555,0.617372,1.947564,-5.219078,4.539955,3.051584,1.388759,5.878332,9.309395,-0.885049,1.924883,2.585102,9.916703,4.620198,-2.885492,4.929068,3.605383,3.788628,5.397259,-0.907308,6.330936,9.644078,-2.556904,5.920160,9.377284,0.454293,8.207299,-5.769962,-8.867510,9.142238,-5.753093,2.829559,7.491690,-9.339029,1.689898,4.808066,1.267952,8.656171,0.836281,1.271530,-9.668382,6.314165,1.572781,-9.519005,7.160034,-6.619768,-8.943299,-5.264668,4.773809,-3.381549,0.544207,5.840661,7.314398,-3.210549,7.299847,7.349022,-4.669866,1.128906,-2.127027,2.378424,1.216628,-4.330764,-1.910504,-3.501950,1.515176,-4.375580,-5.840503,7.653134,-4.262707,5.917563,0.502095,6.250218,3.441708,2.952285,-1.793595,-8.429362,9.539886,5.348982,7.585841,1.561008,9.682985,7.515272,3.448397,9.796890,-4.173794,5.140647,9.368096,-9.298842,1.927799,-3.634903,-3.669845,8.807501,4.378674,4.226231,-3.461879,-5.582328,-1.629816,-2.586314,-6.434386,8.607273,-0.053886,0.995359,1.417077,-1.496514,3.104712,-5.364227,6.751307,1.646611,8.952264,4.739408,4.869759,8.588552,7.123832,6.338952,0.797911,4.658413,2.616254,8.238839], dtype = "float32")#candidate|12562|(132,)|const|float32
call_12561 = relay.TupleGetItem(func_8206_call(relay.reshape(const_12562.astype('float32'), [132,])), 1)
call_12563 = relay.TupleGetItem(func_8208_call(relay.reshape(const_12562.astype('float32'), [132,])), 1)
output = relay.Tuple([call_12549,call_12551,var_12552,call_12561,const_12562,])
output2 = relay.Tuple([call_12550,call_12553,var_12552,call_12563,const_12562,])
func_12570 = relay.Function([var_12552,], output)
mod['func_12570'] = func_12570
mod = relay.transform.InferType()(mod)
mutated_mod['func_12570'] = func_12570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12571 = relay.var("var_12571", dtype = "float32", shape = (40,))#candidate|12571|(40,)|var|float32
func_12570_call = mutated_mod.get_global_var('func_12570')
call_12572 = func_12570_call(var_12571)
output = call_12572
func_12573 = relay.Function([var_12571], output)
mutated_mod['func_12573'] = func_12573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12470_call = mod.get_global_var('func_12470')
func_12472_call = mutated_mod.get_global_var('func_12472')
call_12593 = func_12470_call()
call_12594 = func_12470_call()
func_11991_call = mod.get_global_var('func_11991')
func_11992_call = mutated_mod.get_global_var('func_11992')
call_12611 = func_11991_call()
call_12612 = func_11991_call()
output = relay.Tuple([call_12593,call_12611,])
output2 = relay.Tuple([call_12594,call_12612,])
func_12630 = relay.Function([], output)
mod['func_12630'] = func_12630
mod = relay.transform.InferType()(mod)
mutated_mod['func_12630'] = func_12630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12630_call = mutated_mod.get_global_var('func_12630')
call_12631 = func_12630_call()
output = call_12631
func_12632 = relay.Function([], output)
mutated_mod['func_12632'] = func_12632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_12666 = relay.TupleGetItem(func_10157_call(), 0)
call_12667 = relay.TupleGetItem(func_10159_call(), 0)
output = relay.Tuple([call_12666,])
output2 = relay.Tuple([call_12667,])
func_12674 = relay.Function([], output)
mod['func_12674'] = func_12674
mod = relay.transform.InferType()(mod)
output = func_12674()
func_12675 = relay.Function([], output)
mutated_mod['func_12675'] = func_12675
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12721 = relay.var("var_12721", dtype = "bool", shape = (7, 14, 12))#candidate|12721|(7, 14, 12)|var|bool
var_12722 = relay.var("var_12722", dtype = "bool", shape = (7, 14, 12))#candidate|12722|(7, 14, 12)|var|bool
bop_12723 = relay.logical_or(var_12721.astype('bool'), relay.reshape(var_12722.astype('bool'), relay.shape_of(var_12721))) # shape=(7, 14, 12)
output = relay.Tuple([bop_12723,])
output2 = relay.Tuple([bop_12723,])
func_12743 = relay.Function([var_12721,var_12722,], output)
mod['func_12743'] = func_12743
mod = relay.transform.InferType()(mod)
var_12744 = relay.var("var_12744", dtype = "bool", shape = (7, 14, 12))#candidate|12744|(7, 14, 12)|var|bool
var_12745 = relay.var("var_12745", dtype = "bool", shape = (7, 14, 12))#candidate|12745|(7, 14, 12)|var|bool
output = func_12743(var_12744,var_12745,)
func_12746 = relay.Function([var_12744,var_12745,], output)
mutated_mod['func_12746'] = func_12746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12290_call = mod.get_global_var('func_12290')
func_12291_call = mutated_mod.get_global_var('func_12291')
call_12759 = relay.TupleGetItem(func_12290_call(), 3)
call_12760 = relay.TupleGetItem(func_12291_call(), 3)
func_8508_call = mod.get_global_var('func_8508')
func_8510_call = mutated_mod.get_global_var('func_8510')
var_12762 = relay.var("var_12762", dtype = "float64", shape = (280,))#candidate|12762|(280,)|var|float64
call_12761 = relay.TupleGetItem(func_8508_call(relay.reshape(var_12762.astype('float64'), [4, 10, 7])), 0)
call_12763 = relay.TupleGetItem(func_8510_call(relay.reshape(var_12762.astype('float64'), [4, 10, 7])), 0)
const_12765 = relay.const([-9.011700,4.785977,7.918720,-2.381200,3.496782,8.995827,4.349709,-8.614218,-1.052274,-2.807192,-9.442267,-1.321928,5.250279,-3.172334,-8.026459,-1.864814,-5.263413,-9.196728,-3.794626,-0.013743,3.723278,-2.368189,1.334367,0.785122,-0.609600,-8.507198,1.875882,-1.364123,-1.663720,4.413969,-1.962904,4.877864,7.801814,-5.800621,1.656827,3.817629,-7.800230,3.363748,-1.408056,0.404111,8.387085,-4.162783,4.984998,5.609468,3.087389,-4.166403,2.013592,-1.937921,1.914606,-0.495790,-5.236983,9.095122,5.753718,-4.568988,-4.875333,-3.780565,-5.418364,-2.204927,5.298421,7.091057,-3.048950,-6.848562,-0.333624,-9.925142,2.974458,-3.094641,4.149279,-7.092856,-9.436611,-9.502672,7.158381,-2.362615,4.968075,8.616824,0.507745,2.209065,-4.464515,5.798347,6.571827,-4.932772,-8.824387,-3.075171,-4.353170,-0.541912,2.631514,1.435433,-8.241638,-9.481578,-6.688890,-7.351099,3.001228,9.184258,-7.267461,-4.607400,9.133494,-0.728707,8.390156,5.690022,-1.193641,-2.044213,-1.034967,-5.683986,-0.063617,0.363057,-4.188121,-2.412894,1.957404,5.757160,-6.827267,3.295247,-9.734076,4.327242,-2.934267,4.841456,-0.072919,8.247752,-7.494933,0.667871,-5.867574,1.036505,1.999509,-3.365244,-9.504639,-1.710994,0.374251,-1.601054,1.916048,1.859882,-1.542580,-8.823061,4.634458,3.424946,9.569237,-1.154823,1.564656,-7.158405,7.353660,-6.002459,-3.246632,-6.409799,-6.202494,0.408866,-3.272615,-4.500408,-0.889915,1.382167,-1.708545,5.373894,-1.540125,9.036772,1.682358,-1.865198,4.132428,-1.668805,6.930255,7.405266,9.679485,8.772367,-8.082387,-3.293955,0.076796,-6.724957,5.088590,8.690074,0.717641,8.409092,3.069567,9.630052,-0.003584,-9.347933,-8.163450,-6.293807,0.850684,8.418779,4.222920,-4.191433,7.090750,-2.137396,-2.800125,-5.858446,-8.907979,-5.532856,0.401030,-3.293857,-1.379936,9.776355,9.969987,-8.693751,-4.116946,-1.559595,-8.303990,-4.929126,0.908568,-7.315186,-5.271717,5.863999,-3.142214,-5.856349,0.941643,-1.974958,-6.680244,-5.436817,1.150033,-7.309162,-4.907196,1.838967,8.305013,-2.843355,-1.914472,-9.277354,-3.100923,9.277917,0.042647,-9.234874,2.081758,-0.134835,8.313607,4.040271,-2.395083,-3.721991,-1.663589,3.517676,7.250969,-6.343084,-9.256483,-1.271427,-7.157829,2.585586,-6.643482,-3.922206,-0.355403,0.984128,7.490261,-6.737066,-0.648643,-5.735635,-0.851739,-4.787949,5.859387,4.299504,6.395656,-9.589575,-7.247081,5.816788,-8.002276,-4.486686,7.711284,-7.681688,-0.479135,-9.535765,0.668930,9.993282,-3.009196,8.008088,-3.368187,6.890657,-4.993772,1.512259,3.111381,1.973535,-2.903883,5.705833,4.457788,-7.479248,-4.461958,-8.463185,6.053258,-6.026729,7.362152,1.877497,-2.217943,0.109356,8.243823,1.333104,-7.509951,-9.397859,-7.739940,-8.574575,2.243660,2.006350], dtype = "float64")#candidate|12765|(280,)|const|float64
bop_12766 = relay.subtract(var_12762.astype('int32'), relay.reshape(const_12765.astype('int32'), relay.shape_of(var_12762))) # shape=(280,)
func_10653_call = mod.get_global_var('func_10653')
func_10661_call = mutated_mod.get_global_var('func_10661')
var_12772 = relay.var("var_12772", dtype = "float64", shape = (14,))#candidate|12772|(14,)|var|float64
var_12773 = relay.var("var_12773", dtype = "float32", shape = (320,))#candidate|12773|(320,)|var|float32
const_12774 = relay.const(False, dtype = "bool")#candidate|12774|()|const|bool
var_12775 = relay.var("var_12775", dtype = "bool", shape = (1, 117))#candidate|12775|(1, 117)|var|bool
const_12776 = relay.const([True,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False], dtype = "bool")#candidate|12776|(702,)|const|bool
const_12777 = relay.const([6.752069,7.879539,-1.773675,-6.736261,-6.068127,-1.552792,-6.703885,-7.358272,1.884012,2.439148,-2.686281,-6.579061,6.212702,8.147440,-2.113078,7.698127,-7.796369,-9.372122,-7.504120,9.780191,-7.259349,9.306414,-2.567510,5.939293,0.864208,2.862500,-1.973445,-4.933854,0.111538,-7.407602,9.302982,7.482144,-3.068077,-7.895872,-4.285469,-6.554539,-4.411435,2.099859,5.196998,-1.819922,-9.551887,-3.150126,3.287069,-9.459628,0.182969,-6.434707,-4.000157,-1.475555,2.496645,1.924781,-4.137977,-9.401972,-0.870771,-5.766447,5.740454,-8.218785,-9.402727,-1.954711,4.049524,-1.766861,1.776352,6.120963,-3.256225,0.170809,6.835785,-7.296661,-7.913479,-6.963135,-5.562418,-5.359937,2.063693,7.776849,5.549366,8.875981,-2.932911,9.335744,-5.713878,-6.280910,4.492379,-4.141716,-5.272761,-0.142041,9.837798,4.343821,8.066777,8.001652,-4.251302,-4.704142,-6.748712,-8.300121,5.541822,7.626349,9.628797,6.505830,4.006576,7.153849,-2.037256,-7.563023,-6.663921,9.900743,6.579962,-5.091917,-3.832218,8.428280,-9.406426,7.321094,-9.046898,2.660780,-0.352425,-1.611003,-5.600958,-3.028568,0.206984,-3.060420,-6.926728,-6.882481,5.205498,-7.737756,2.901211,-5.191223,7.598396,-2.486042,-9.565219,3.990512,-1.923482,-7.259462,7.567561,4.864875,5.119441,-0.804019,1.002495,5.295238], dtype = "float32")#candidate|12777|(132,)|const|float32
call_12771 = relay.TupleGetItem(func_10653_call(relay.reshape(var_12772.astype('float64'), [14,]), relay.reshape(var_12773.astype('float32'), [320,]), relay.reshape(const_12774.astype('bool'), []), relay.reshape(var_12775.astype('bool'), [117,]), relay.reshape(const_12776.astype('bool'), [702,]), relay.reshape(const_12777.astype('float32'), [132,]), ), 7)
call_12778 = relay.TupleGetItem(func_10661_call(relay.reshape(var_12772.astype('float64'), [14,]), relay.reshape(var_12773.astype('float32'), [320,]), relay.reshape(const_12774.astype('bool'), []), relay.reshape(var_12775.astype('bool'), [117,]), relay.reshape(const_12776.astype('bool'), [702,]), relay.reshape(const_12777.astype('float32'), [132,]), ), 7)
func_10419_call = mod.get_global_var('func_10419')
func_10423_call = mutated_mod.get_global_var('func_10423')
const_12781 = relay.const([-5.935584,1.863517,8.861360,1.640806,5.325382,-9.151667,-2.305230,-9.627544,-3.150324,9.039573,-1.253450,8.236989,-8.619015,8.481974,1.673362,-0.127841,-6.108875,5.987132,-8.395709,-9.339972,2.458995,-9.854084,1.862898,5.951645,-6.674497,8.562904,-1.276143,7.778155,-5.690248,4.627535,-4.341719,-6.717121,3.620665,-4.322310,-0.339052,5.447225,8.108008,3.418154,-7.880427,-7.704055], dtype = "float32")#candidate|12781|(40,)|const|float32
const_12782 = relay.const([-4,8,1,3,2,4,5,9,3,-5,2,9,7,-8,-9,-5,-4,-4,-8,6,7,9,-7,-5,10,1,-3,5,-8,-7,6,10,2,6,-9,9,-4,9,-7,-4,-6,10,-7,9,10,4,5,-5,-6,-8,3,4,-6,-1,-9,9,-3,-5,5,-6,10,-10,-4,2,6,-4,9,-6,-10,7,5,-7,4,9,-7,-4,-6,2,9,-9,-5,-4,10,-7,-9,4,-2,-2,-2,-8,5,6,6,1,-1,10,3,10,4,-8,2,6,-10,10,9,-2,10,8,-5,1,9,-2,5,-10,9,-1,7,-5,-8,-2,5,-3,-2,-2,2,-1,-7,7,-4,1,2,-4,-1,-7,-8,-6,-3,-9,-2,9,8,-6,4,-7,10,-2,1,-1,-7,-3,-7,9,10,2,10,-9,-5,3,8,-10,1,-1,7,7,10,8,-1,-5,4,-4,-1,5,7,5,-10,-6,-6,5,8,-9,2,-6,-4,-5,-10,-7,1,7,9,-5,-7,-10,-9,8,7,-8,3,-3,6,-9,6,-7,5,-6,6,-3,-4,7,10,-3,-1,9,4,4,9,-6,9,-3,-7,-1,2,-7,-9,-10,-2,-5,3,-8,5,6,-7,-10,-6,-3,1,6,-7,10,9,-2,-4,-3,-10,-5,-5,10,3,-8,-2,2,4,7,-10,5,10,10,6,-10,-4,-1,5,-3,-1,7,-4,7,6,-9,-2,6,6,5,-9,8,1,6,-3,6,10,7,4,-3,-9,-7,-1,-4,-8,8,-3,5,-6,-2,8,4,1,5,5,-6,-2,-7,5,-9,10,4,-4,9,-10,10,9,9,3,-7,-1,5,5,8,5,7,-5,-1,2,8,3,9,1,-3,-9,5,5,-5,5,-4,-1,8,-4,6,10,-5,1,6,1,8,-2,-3,-4,9,10,-10,4,8,6,1,7,1,-1,1,8,5,-10,-7,5,-4,7,7,-1,-9,-8,-4,-8,2,-4,3,-10,-10,-5,7,-2,8,-6,-3,9,-7,-4,-9,-8,4,-3,3,-5,6,-9,1,-5,-3,3,9,9,10,-6,6,1,-5,-6,8,1,-1,-10,-4,-1,-5,2,-8,-9,-4,7,-1,9,3,-4,7,8,6,10,10,-6,8,2,-8,-2,7,2,8,-2,7,3,-1,-9,6,8,3,-4,3,4,-6,-6,8,9,-9,10,-8,9,-3,-10,-10,-6,4,1,-5,-3,-5,-1,6,2,2,-3,-2,-4,3,-3,-4,-5,10,-8,-4,3,-7,-2,-6,-10,4,-1,-6,-3,-8,-3,7,1,-5,-10,9,8,-10,10,-7,-6,-4,9,-3,10,-1,6,-10,-3,7,3,9,-1,-2,-6,-3,-9,-1,-8,3,10,10,9,-4,-4,8,-6,-7,-7,-9,-9,5,-9,8,-3,-3,2,10,1,8,4,3,4,-8,-10,-1,-9,-6,-5,4,-5,2,10,3,-5,-9,6,8,3,-10,-2,1,-1,8,3,-5,-10,-8,-10,-4,-1,-3,-6,-10,6,-1,2,10,2,9,-1,-6,3,1,-6,-8,9,-7,-4,-3,6,1,-7,1,-10,-5,-7,1,-8,5,7,-2,-7,-9,-5,-1,6,10,4,3,4,-4,10,4,8,-3,-5,1,-5,10,5,-2,7,4,-5,-7,6,1,9,-5,7,1,-2,-1,-5,4,6,2,-10,-5,5,4,-3,7,-2,-10,10,-8,-6,-7,2,2,9,-1,2,4,8,-9,2,-5,-10,-1,6,3,8,4], dtype = "uint64")#candidate|12782|(660,)|const|uint64
call_12780 = relay.TupleGetItem(func_10419_call(relay.reshape(const_12781.astype('float32'), [40,]), relay.reshape(const_12782.astype('uint64'), [660,]), ), 1)
call_12783 = relay.TupleGetItem(func_10423_call(relay.reshape(const_12781.astype('float32'), [40,]), relay.reshape(const_12782.astype('uint64'), [660,]), ), 1)
output = relay.Tuple([call_12759,call_12761,bop_12766,call_12771,var_12772,var_12773,const_12774,var_12775,const_12776,const_12777,call_12780,const_12781,const_12782,])
output2 = relay.Tuple([call_12760,call_12763,bop_12766,call_12778,var_12772,var_12773,const_12774,var_12775,const_12776,const_12777,call_12783,const_12781,const_12782,])
func_12784 = relay.Function([var_12762,var_12772,var_12773,var_12775,], output)
mod['func_12784'] = func_12784
mod = relay.transform.InferType()(mod)
mutated_mod['func_12784'] = func_12784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12784_call = mutated_mod.get_global_var('func_12784')
var_12786 = relay.var("var_12786", dtype = "float64", shape = (280,))#candidate|12786|(280,)|var|float64
var_12787 = relay.var("var_12787", dtype = "float64", shape = (14,))#candidate|12787|(14,)|var|float64
var_12788 = relay.var("var_12788", dtype = "float32", shape = (320,))#candidate|12788|(320,)|var|float32
var_12789 = relay.var("var_12789", dtype = "bool", shape = (1, 117))#candidate|12789|(1, 117)|var|bool
call_12785 = func_12784_call(var_12786,var_12787,var_12788,var_12789,)
output = call_12785
func_12790 = relay.Function([var_12786,var_12787,var_12788,var_12789,], output)
mutated_mod['func_12790'] = func_12790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10325_call = mod.get_global_var('func_10325')
func_10326_call = mutated_mod.get_global_var('func_10326')
call_12811 = relay.TupleGetItem(func_10325_call(), 0)
call_12812 = relay.TupleGetItem(func_10326_call(), 0)
func_11006_call = mod.get_global_var('func_11006')
func_11011_call = mutated_mod.get_global_var('func_11011')
const_12816 = relay.const([[6.407151,3.847962,3.053853,-1.524858,3.087587,2.975085,9.557622,-7.939634,-0.385163,-6.891945,6.094666,-8.586029,-1.323828,7.952047,-2.475878,-0.010182,7.290689,1.664331,8.235372,7.398239,8.449183,5.788153,-9.011409,5.736648,-1.026159,-2.741476,-0.221224,7.467391,-5.595420,0.191329,-3.492261,-0.966128,2.966564,-1.187636,0.593107,7.776364,5.452411,9.028624,-8.026221,-0.678114,7.648973,1.402073,3.901430,-2.324893,2.531528,-2.437428,0.787278,5.817100,-2.126892,2.057930,-7.470078,-1.355748,2.376733,2.085584,-0.925573,-3.451604],[-4.541429,0.317135,-2.032306,-7.715549,0.247675,5.476395,9.823943,4.439278,0.563138,-6.971959,1.621897,3.786552,-9.404277,5.948771,-0.948320,-7.576197,5.828320,6.723623,2.531120,1.304385,-4.339194,1.140873,9.133931,-4.069357,-5.288241,-7.567037,0.806492,-2.458948,-6.801156,6.053360,-1.015354,-2.006347,1.661007,7.955390,7.169564,-1.043546,-3.617563,2.370116,-0.214836,-8.473903,-6.449039,1.992253,-8.994942,-3.941732,8.193171,4.989150,8.881481,7.962132,4.758653,-7.192687,3.167718,7.188024,-7.765534,4.266642,-9.124264,5.686084],[3.093123,-9.282327,9.304003,-3.631711,-4.127213,-5.719313,5.604506,3.698019,-5.396100,4.873840,-9.273445,6.261943,-1.811545,7.718984,-7.634108,1.124148,9.121450,0.102871,-7.293212,8.894757,-0.403220,6.213285,3.853813,-1.588575,-3.965664,0.437724,-1.929355,6.801033,-9.833928,6.710490,-3.633235,-2.505678,0.418673,-6.555541,3.417525,-6.234722,9.693849,-9.262286,-4.492160,-8.952210,-0.194616,9.784237,1.006755,4.447978,-9.953808,-6.445791,-2.197052,-3.600466,9.966467,6.916234,4.717708,-1.652159,2.247783,4.719827,1.794005,-0.112396],[-1.076297,9.596839,4.484014,0.950484,4.480714,-0.646965,-6.572637,9.170164,5.469465,-8.664600,2.104926,2.733964,0.375173,-9.786126,-6.024238,5.849428,5.674449,-6.552212,1.585394,-5.402914,-6.588965,-5.352813,8.506363,-7.362738,2.919824,9.299142,3.437333,9.539663,-3.517201,4.968303,4.235604,4.988931,5.241737,4.707814,2.137718,-1.806347,-3.844560,-4.327591,-2.279444,-1.485695,3.783335,-0.380444,-7.843934,-4.924884,-6.599206,7.812185,-7.609671,-4.784026,2.570216,-7.797679,0.351819,-9.864816,-9.123015,9.254974,5.031741,-0.396382],[-7.769311,3.308374,-6.113969,6.296221,3.284088,-4.952621,0.898568,-1.158051,-3.791922,5.852792,0.032036,0.730577,-5.144177,-2.026036,-1.818267,-1.473049,-5.985437,5.233187,0.362633,4.857067,-1.511309,-7.286516,-3.176794,-6.151111,-8.726442,-6.258000,5.940877,8.789923,-9.457882,3.205750,-3.335874,0.435882,0.324176,1.109825,2.865905,2.234123,3.481709,8.903730,-8.169486,-0.330997,2.988470,-4.403410,4.055704,-8.543237,-6.983505,-5.381852,-7.255338,6.410351,5.075505,-4.947490,4.252195,-8.251253,-8.859650,-0.814205,0.509393,6.373022],[4.099327,4.507281,7.477361,-6.564706,2.210750,-6.572420,0.962835,1.807038,-7.897874,7.533276,2.648412,-2.563577,-2.253875,0.927775,-2.958343,-0.474174,-2.756372,-1.602512,-7.396784,1.711550,8.342334,2.417405,2.935871,6.061347,-1.873602,3.653180,-3.625764,9.583939,-3.694418,-2.682679,0.122524,-9.598481,-0.083551,8.649612,-3.186103,-9.691006,-9.376452,-1.258957,-1.617468,-6.571788,-8.172884,4.461788,7.246763,3.293640,3.685777,-3.217400,8.730941,-7.513688,5.102744,-6.013299,0.417585,-5.364478,-4.002024,6.277230,-6.337387,9.250871],[-7.638539,-1.576622,-9.849708,8.328967,8.428977,-1.463945,3.573216,4.020639,0.072214,-4.624911,-8.704304,-2.241784,1.320433,-6.262525,0.404029,-4.266200,-5.886742,-2.739298,7.877647,-8.154287,4.814990,0.569104,4.088434,-0.741838,-7.301051,9.001896,7.509556,3.137182,-2.052695,-8.057323,2.170879,7.352268,5.069525,-4.562814,7.545861,-6.907511,-5.567341,6.979474,-7.265341,-1.964222,-0.130612,3.657420,6.439448,-0.219924,-0.258284,-5.839922,-1.701046,3.241855,5.111570,-5.691104,-1.915343,5.192697,-1.494236,6.268319,-9.677178,6.489149]], dtype = "float64")#candidate|12816|(7, 56)|const|float64
const_12817 = relay.const([9.913735,-5.207678,-4.055598,8.062932,-9.400772,-4.590016,5.337400,8.252906,9.029168,-0.323340,0.568193,-5.831052,0.524347,8.551086,6.586131,1.447226,-7.532906,-8.482429,-7.066430,2.358722,3.431757,-1.347866,-8.497600,-6.264919,3.783174,3.617242,-6.029400,-6.540741,8.961321,9.583697,-4.191286,6.506783,-2.912312,0.462814,-4.648226,-4.585397,-2.657089,-8.314231,-4.436949,1.539464,8.520699,-1.686387,-8.363244,4.337893,-0.284807,-8.994037,1.104196,-8.020910,-0.220617,4.882978,-7.905197,-1.046740,-4.962632,-6.817640,9.354691,-4.330412,-1.470765,4.054172,-1.457570,5.735264,0.085863,3.868284,5.418357,-4.866886,5.231300,-8.485328,4.814208,-5.446753,1.302690,-6.540311,-2.214053,0.355313,-4.817182,-0.472504,2.352409,4.433931,2.185886,-8.546598,-0.088730,-9.929124,-1.428190,-7.249838,3.601501,5.430147,0.832269,-4.382010,7.389433,-1.214329,-4.325177,-5.104666,-3.374479,-6.610172,-9.373670,7.340230,9.712626,-5.657632,-4.630108,-9.922605,3.385410,1.057970,9.958761,2.623808,0.624871,-3.572299,-3.829241,-7.910158,2.045072,-0.778647,7.177995,-9.791961,-0.159970,-5.398662,8.523183,-0.428142,-2.992652,2.250515,4.086783,-6.757713,6.736392,-2.733412,2.182639,-0.130014,3.947669,-9.731871,-7.881967,-2.282532,3.600290,-3.956279,9.063134,-5.009872,-3.956642,6.762412,-6.960453,-1.772598,0.283003,6.670773,9.911748,4.914831,-4.898150,4.930411,-5.899069,0.112015,-0.102711,4.705843,0.290054,-5.945942,4.895595,2.746518,3.025184,7.834431,7.132910,-9.676655,4.190169,5.162273,4.319749,-8.335027,-6.722984,-9.560349,6.349145,-6.465842,6.229744,-6.199079,5.247054,-4.672367,-7.805607,6.804481,-6.693120,-9.862623,8.161501,0.108140,9.915339,-4.290703,-4.744342,-6.489194,-9.547761,-3.462812,5.506453,2.071787,-6.425043,-7.979524,5.337740,-4.126338,6.545423,1.103797,3.504150,1.788563,2.635441,-4.664683,-7.428938,2.471332,-9.222184,-8.853160,4.259264,-9.902645,7.027804,-0.948007,-2.526196,-4.645786,1.711674,-7.725921,8.876236,8.527805,8.288900,-8.344343,7.524626,0.674898,4.648933,5.279267,4.857061,-1.138066,-6.281446,8.860058,-7.955780,-5.890813,-9.292661,-2.033950,1.629700,-6.423958,6.508774,-9.717950,-6.990652,-1.052071,-3.540774,-3.728955,0.599366,-8.466706,2.133276,-4.179106,-9.208426,-8.496866,2.009987,-1.599274,-4.634859,-0.873712,5.130591,-2.009896,-9.916510,7.768753,2.213916,-2.085236,-6.891005,-1.070039,-0.906553,9.861838,-0.748650,0.461348,-2.316793,-4.783186,-4.075085,7.496229,3.791060,-0.109626,-2.199161,-5.310086,1.287681,2.013161,-7.903618,-2.544862,-8.146986,3.866720,6.860693,6.078778,-8.407366,-4.550904,-8.946014,-0.327191,-3.056573,9.388424,-7.225648,-2.646731,-9.571195,7.353958,4.492933,0.299132,-3.983425,-3.343025,-8.186512,8.275587,9.663161,7.977201,6.610333,-6.912972,-6.100695,3.880518,4.290482,8.760091,2.095659,-6.756033,-5.153532,-7.092124,-5.549088,-9.429611,-1.944399,8.779210,2.126372,7.240974,-7.092737,-1.123688,4.419995,9.108125,2.434047,-0.932080,-7.649178,-3.686568,3.116425,2.761641,4.807923,-2.411213,2.985700,-0.223202,-5.650329,-3.459392,6.281095,-3.174425,-8.185243,1.251111,-3.474891,-0.297374,1.919248,4.025452,4.470892,-8.018421,-5.524781,4.008042,9.755186,-5.802637,4.124482,-7.921868,-8.859363,-4.044722,1.887738,-4.466252,0.344904,-7.326486,5.701047,1.021248,-4.828019,-2.732912,-6.482499,-9.748378,7.148999,-9.357137,9.106772,2.075374,4.028255,-5.724644,1.626140,-6.822062,6.017578,9.556588,-4.895356,-9.929898,2.060940,1.982038,-1.531483,8.015656,-1.786173,-8.282830,-1.828939,9.389605,2.185886,-0.596235,8.107791,-0.972949,4.732310,9.897530,-7.638795,-0.576676,-5.917113,-5.393340,-0.226167,-1.565071,4.867867,-9.612110,-3.157906,1.426860,-8.070915,4.393866,-5.170358,-6.177691,3.447085,1.105508,0.756177,2.394400,4.035776,-0.986396,4.704233,-5.276802,-9.756314,7.776988,7.294796,-9.129016,-4.289752,6.782392,4.058583,9.983299,9.686749,7.197121,-5.058931,3.607757,-5.289614,9.724968,-9.635422,-4.799057,5.423909,-1.439689,-7.476542,-3.396372,-6.579826,3.363403,9.297084,-1.935153,6.247202,-6.216320,6.334790,3.263084,5.005184,5.446108,-9.003303,-4.485920,0.638835,-3.754215,-4.591382,0.596797,-6.228145,-3.909791,2.992580,1.696387,-0.483769,-4.278722,8.776721,6.690911,3.008634,-5.175984,-4.842327,8.427577,4.132120,1.009200,-9.966968,-6.405495,7.069991,-8.684931,-1.185745,3.744925,9.975797,-7.887214,1.611362,-1.834210,-1.100841,8.609224,1.007361,3.872038,-4.768943,-1.475142,8.775254,-4.783616,-5.110937,1.650658,-4.271651,9.031264,-2.748979,-8.493573,-3.305179,-3.416612,4.237234,1.343505,-3.887181,-2.649455,-0.548090,5.291111,5.370602,-6.206572,5.922273,-8.318271,1.425508,5.284581,8.221429,5.106436,-8.371159,7.251501,5.309818,7.621219,8.456226,6.269316,-5.282286,0.936351,-7.944511,0.595750,0.701764,3.940625,-9.784389,-3.517420,-3.314509,1.942257,-3.716114,-4.151960,7.701765,4.731904,7.790890,-9.203874,-7.574879,-0.774797,-8.403600,-6.316885,3.715134,-5.551976,-0.784837,-9.681494,-2.103079,-9.010489,-7.024190,0.437857,-0.029154,-8.312459,7.181402,5.455538,-5.127573,-9.545941,-3.126260,-0.373994,-2.528085,2.257879,9.493374,9.346469,2.343788,-8.949141,-7.562643,1.507744,3.509382,1.638269,5.333633,-1.636280,-7.843417,-0.509533,8.834445,-5.752774,1.843032,-1.351567,5.354631,-8.277329,8.674292,-9.151536,-5.627361,-2.326051,5.022613,-9.206675,9.384788,-8.909872,9.059793,-8.534759,7.532260,-3.450438,-0.228953,-3.329053,-0.479241,-0.216151,8.628799,-1.135965,-9.734438,9.417276,-1.246329,-0.083027,-1.071722,4.936997,3.562635,-8.397132,-9.917234,5.980872,-7.779762,9.977200,5.717586,-9.036125,-8.144885,-8.251547,-7.533200,3.896550,-8.830015,-3.812069,-0.862348,-5.443196,0.010293,5.554155,-9.888730,-2.322380,-1.664176,0.972581,4.581032,-6.647628,-1.561134,-0.114266,3.985670,6.362189,-4.984828,-5.952005,9.947179,-6.046382,-6.186271,3.536496,0.529893,2.782413,1.071486,7.448027,-0.366253,-1.764973,-1.542207,4.298961,-5.533402,0.788915,-7.852064,-9.647772,7.705401,-4.936019,-5.643118,-8.609085,9.009180,5.033118,-7.904828,2.329554,-0.928216,-2.082101,0.753754,-6.916160,-8.483133,-0.856787,-3.113348,0.504078,4.856996,0.481267,3.589934,2.232790,7.243717,1.669636,5.728532,-4.047598,-5.397403,3.095238,4.409863,-5.844957,6.525781,-1.151343,5.258470,8.599983,-7.335283,-4.837633,-7.033880,-9.091125,-2.076344,-0.527830,6.243787,9.593391,8.361191,9.653939,5.737695,-3.341005,-3.536798,-6.494064,-9.366830,-6.398281,-6.131880,-7.027626,7.233376,-8.927282,-1.885718,5.674183,5.447065,-0.999965,6.237861,8.679371,7.894618,-2.175625,9.780283,3.501740,-1.809382,-0.104185,-3.769007,-7.971906,2.135151,5.441615,5.732763,1.976436,1.890435,1.280019,5.791351,3.713493,-4.601912,-9.999734,-9.703450,-3.534952,-3.528879,1.302316,7.485102,-5.442200,-6.327939,6.298476,-1.312431,5.066728,-9.027036,9.122656,8.748387,-1.368385,-1.465683,4.689993,-0.116657,9.636418,-0.715458,7.896449,-3.883961,4.261312,8.976432,-7.002204,5.800624,0.672769,-9.891934,-7.367660,-6.347592,-2.121568,4.997042,7.145880,1.426950,-6.115318,-6.371134,4.482464,9.617130,0.749296,1.624492,9.578417,3.195259,-0.949634,3.969399,-1.001742,7.053037,-7.567861,-7.812620,-1.126692,-5.422631,-0.452181,-6.735973,-0.220351,-1.593055,-0.666141,0.440129,-8.310734,0.588746,7.615346,7.587712,-0.453359,-5.155568,-3.197594,-2.096922,-8.536161,8.424847,3.823411,-5.729265,-4.271421,-9.241910,6.705422,-0.843117,-9.324861,-2.937883,-8.243914,4.162474,9.575651,3.415595,3.070548,-4.433055,-1.781746,-3.064303,-0.325916,0.566461,0.859112,4.800812,-7.283505,-4.452479,8.918687,-6.759295,3.961261,-8.570221,3.580741,-2.934167,-3.535628,-5.064558,-3.123825,-9.290688,6.708299,4.648270,4.306295,0.298335,-6.512618,5.331251,7.455975,9.875178,4.729043,2.624744,5.889604,0.329698,-0.542169,3.866893,-2.818571,1.150776,1.108392,-7.552301,-3.339455,-8.006390,-9.905770,-8.007050,4.090302,-4.218952,-7.472696,9.970006,4.542360,3.706110,-2.135381,-8.777982,-3.823975,8.965348,3.902770,4.065100,1.789418,-4.482778,6.780005,6.332796,9.704815,4.126317,4.172454,6.961811,-4.638425,3.174037,3.943686,8.645169,6.454918,-1.136838,8.140005,-7.057947,2.622373,-3.600566,-2.750251,-4.072439,7.667302,5.383709,-6.741064,2.927119,4.026978,-2.240202,-8.150682,-1.427129,-7.758660,-1.210181,-0.679033,-6.281608,-5.062072,-6.964287,8.326912,-9.004887,1.095596,0.563114,-4.447429,-1.468269,0.982667,3.049384,-7.377167,-2.982596,-2.739236,-2.037160,5.756990,-7.118907,5.980799,-7.129697,5.197297,5.317728,-0.183494,7.321455,3.829543,-8.209784,-1.698539,6.745649,-1.663989,9.498393,-1.516724,3.766984,-5.320014,2.576437,0.071928,-1.273353,-4.183415,1.905161,8.756976,-4.915082,-2.250207,6.896138,-5.812120,6.395334,-9.575018,6.794598,7.422011,0.104435,-4.008245,6.673083,-0.230482,2.722138,-7.436995], dtype = "float64")#candidate|12817|(900,)|const|float64
call_12815 = relay.TupleGetItem(func_11006_call(relay.reshape(call_12811.astype('float32'), [2, 7, 15]), relay.reshape(const_12816.astype('float64'), [392,]), relay.reshape(const_12817.astype('float64'), [450, 2]), relay.reshape(call_12811.astype('float32'), [2, 7, 15]), ), 9)
call_12818 = relay.TupleGetItem(func_11011_call(relay.reshape(call_12811.astype('float32'), [2, 7, 15]), relay.reshape(const_12816.astype('float64'), [392,]), relay.reshape(const_12817.astype('float64'), [450, 2]), relay.reshape(call_12811.astype('float32'), [2, 7, 15]), ), 9)
const_12821 = relay.const([[-3.721023,1.488937,4.418587,4.891419,-4.154748,5.766411,-3.118768,-2.565036,6.185423,-3.897808,-4.316075,5.776505,6.775730,6.632627,-2.821779,1.043400,-2.667826,9.539267,3.347757,0.300955,-8.242664,-7.670445,5.749370,9.920899,6.364911,-5.010209,1.095427,-5.780550,7.489552,3.355095,-7.107445,-2.878247,7.637607,-5.549318,-8.126281,-0.228351,-0.198801,8.856916,-8.843485,-5.530231,-7.545655,5.935877,-7.993538,5.037701,6.298587,-6.618539,7.135680,-9.141201,-5.671216,-5.249838,8.982017,7.415883,9.226849,1.457403,-6.749186,-0.014451],[-5.422360,-9.419752,6.767963,-5.726276,3.686446,-1.585163,-9.175998,7.899374,0.042600,0.174723,9.383828,-6.983961,-6.514093,-5.124728,-1.209126,4.733089,-5.368961,5.959421,7.991107,8.856252,-2.354771,-2.841103,-5.292360,-6.016634,0.860957,-6.019990,-0.177848,6.670202,-2.738830,1.826588,-4.702723,2.179933,5.090842,-2.004451,1.839190,6.380902,4.842279,-1.359132,0.727660,6.146550,-0.756044,7.853028,3.245679,8.171710,-0.743198,-7.123282,-5.269777,-5.929635,-4.894543,-2.583208,-4.438550,-1.888229,3.017455,0.515213,1.277190,3.957448],[5.991761,-6.459860,-9.046528,-7.114557,9.900555,9.666817,4.242004,5.304701,4.786116,5.659907,1.843667,2.605220,-1.742264,8.483830,-5.065379,9.489739,-1.512194,-0.318786,-1.824483,3.962985,0.065404,2.128593,-2.860152,-7.368233,-4.207036,4.262290,8.976749,5.487975,-0.241709,0.741586,5.078030,-8.775728,0.224373,-9.738995,4.985946,4.184221,9.022917,7.334994,6.137776,0.265603,3.183752,6.669777,3.524107,-8.262805,8.186650,-5.933066,2.230146,-2.489660,3.693878,-5.230873,8.237020,0.101596,-6.223212,-9.390497,4.324649,6.527158],[8.154388,2.748589,5.950594,-7.514851,-1.892434,-5.300582,5.995783,-2.779422,5.395516,3.849066,-2.440063,2.615902,-0.314190,-8.457625,5.049381,-9.149115,-8.167944,-3.195180,-9.598532,-0.703496,8.013334,-3.400189,-4.644071,-7.053888,1.345443,-5.245915,-8.296402,-0.336666,9.867064,-0.084747,-7.566172,2.826962,8.526678,7.740123,-7.545139,-4.823337,-1.293123,-1.322385,1.497392,-9.797684,4.117463,-6.727070,1.156149,-5.222452,5.902336,8.660527,7.889519,-0.693829,-9.764174,-0.289128,0.414185,5.369484,2.635434,-0.360356,-2.111181,5.690650],[2.697849,4.824012,-7.854937,-2.922334,8.237802,-6.184234,-3.411932,2.435872,-3.716210,-6.386738,-1.216950,2.794661,8.236433,-0.535723,-8.552966,0.964420,7.970762,-9.754306,-0.369077,2.241041,9.391791,8.604990,-7.143762,-9.235784,-5.675155,-1.204812,-0.095197,2.309080,-1.873240,9.953222,7.163811,-6.649056,-0.995338,6.452267,8.213347,-0.548347,-2.510514,4.747298,-9.773502,7.705647,-9.112375,7.950582,7.023758,-5.586641,-7.971732,-6.123523,7.301185,-2.359568,-6.286647,-1.271844,-5.303026,-2.080997,-6.454713,1.793248,6.881634,-6.690435],[-3.305254,9.581710,-1.493275,7.577662,0.988431,-7.922066,2.841328,-1.433960,-6.988980,1.649544,9.183891,2.220366,4.870131,-8.398155,5.443104,-8.231659,-4.718366,5.037035,-7.545172,7.907894,4.938408,-2.415401,-6.055066,-2.714755,5.778266,9.206092,0.495910,8.963707,9.673559,3.867370,-9.172055,1.435743,0.155275,7.032712,3.975610,-5.317400,-0.879373,5.780944,4.729311,-5.817128,-0.946204,-8.710052,-0.353425,-2.035779,8.590110,1.138505,-6.003468,8.827958,8.814682,0.583966,0.522171,7.515607,-7.375555,4.987380,-1.390126,-4.013503],[6.984364,-5.303377,-6.510361,-4.220239,9.725799,3.772623,-0.558532,9.427049,1.067105,-5.579061,-7.200419,4.660328,6.759678,4.866632,-3.098666,-2.500783,-3.988239,5.570091,7.414207,-4.606307,9.304029,-8.674001,-4.903482,-0.510004,-8.971237,0.792543,-4.615639,1.042006,2.351228,-0.307844,5.701349,2.443552,3.588601,-8.685574,-9.049394,0.857589,5.458065,8.213661,-7.628586,0.068262,2.155326,9.366635,2.117989,4.620004,6.809766,-7.418947,-9.381050,-6.854463,0.972876,-3.628726,-1.381945,6.327310,-6.022216,2.950263,-2.782884,8.880999]], dtype = "float64")#candidate|12821|(7, 56)|const|float64
bop_12822 = relay.maximum(const_12816.astype('float64'), relay.reshape(const_12821.astype('float64'), relay.shape_of(const_12816))) # shape=(7, 56)
func_10419_call = mod.get_global_var('func_10419')
func_10423_call = mutated_mod.get_global_var('func_10423')
const_12835 = relay.const([[-3.476964,-9.458008],[2.840980,-9.136720],[-9.259507,4.095445],[0.033711,0.174511],[-3.489441,1.766258],[6.009055,8.562265],[-9.992300,-2.026897],[-9.401654,3.827638],[-6.483414,2.211100],[7.140245,-2.518417],[8.395760,6.176177],[3.955379,4.409816],[1.027213,-5.295117],[-4.023115,-1.289847],[7.405486,8.123125],[7.400840,-7.048545],[-4.401166,8.609518],[5.939541,-4.657886],[3.010657,-5.874923],[-5.856420,6.289962]], dtype = "float32")#candidate|12835|(20, 2)|const|float32
var_12836 = relay.var("var_12836", dtype = "uint64", shape = (1, 660))#candidate|12836|(1, 660)|var|uint64
call_12834 = relay.TupleGetItem(func_10419_call(relay.reshape(const_12835.astype('float32'), [40,]), relay.reshape(var_12836.astype('uint64'), [660,]), ), 6)
call_12837 = relay.TupleGetItem(func_10423_call(relay.reshape(const_12835.astype('float32'), [40,]), relay.reshape(var_12836.astype('uint64'), [660,]), ), 6)
output = relay.Tuple([call_12811,call_12815,const_12817,bop_12822,call_12834,const_12835,var_12836,])
output2 = relay.Tuple([call_12812,call_12818,const_12817,bop_12822,call_12837,const_12835,var_12836,])
func_12843 = relay.Function([var_12836,], output)
mod['func_12843'] = func_12843
mod = relay.transform.InferType()(mod)
var_12844 = relay.var("var_12844", dtype = "uint64", shape = (1, 660))#candidate|12844|(1, 660)|var|uint64
output = func_12843(var_12844)
func_12845 = relay.Function([var_12844], output)
mutated_mod['func_12845'] = func_12845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11087_call = mod.get_global_var('func_11087')
func_11089_call = mutated_mod.get_global_var('func_11089')
call_12876 = func_11087_call()
call_12877 = func_11087_call()
output = call_12876
output2 = call_12877
func_12879 = relay.Function([], output)
mod['func_12879'] = func_12879
mod = relay.transform.InferType()(mod)
mutated_mod['func_12879'] = func_12879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12879_call = mutated_mod.get_global_var('func_12879')
call_12880 = func_12879_call()
output = call_12880
func_12881 = relay.Function([], output)
mutated_mod['func_12881'] = func_12881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10165_call = mod.get_global_var('func_10165')
func_10167_call = mutated_mod.get_global_var('func_10167')
call_12971 = relay.TupleGetItem(func_10165_call(), 0)
call_12972 = relay.TupleGetItem(func_10167_call(), 0)
func_12290_call = mod.get_global_var('func_12290')
func_12291_call = mutated_mod.get_global_var('func_12291')
call_12979 = relay.TupleGetItem(func_12290_call(), 1)
call_12980 = relay.TupleGetItem(func_12291_call(), 1)
output = relay.Tuple([call_12971,call_12979,])
output2 = relay.Tuple([call_12972,call_12980,])
func_12984 = relay.Function([], output)
mod['func_12984'] = func_12984
mod = relay.transform.InferType()(mod)
mutated_mod['func_12984'] = func_12984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12984_call = mutated_mod.get_global_var('func_12984')
call_12985 = func_12984_call()
output = call_12985
func_12986 = relay.Function([], output)
mutated_mod['func_12986'] = func_12986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12470_call = mod.get_global_var('func_12470')
func_12472_call = mutated_mod.get_global_var('func_12472')
call_12990 = func_12470_call()
call_12991 = func_12470_call()
output = relay.Tuple([call_12990,])
output2 = relay.Tuple([call_12991,])
func_13002 = relay.Function([], output)
mod['func_13002'] = func_13002
mod = relay.transform.InferType()(mod)
output = func_13002()
func_13003 = relay.Function([], output)
mutated_mod['func_13003'] = func_13003
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13031 = relay.var("var_13031", dtype = "float32", shape = (6, 14, 1))#candidate|13031|(6, 14, 1)|var|float32
uop_13032 = relay.asinh(var_13031.astype('float32')) # shape=(6, 14, 1)
bop_13044 = relay.logical_xor(uop_13032.astype('uint64'), relay.reshape(var_13031.astype('uint64'), relay.shape_of(uop_13032))) # shape=(6, 14, 1)
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
var_13052 = relay.var("var_13052", dtype = "float32", shape = (320,))#candidate|13052|(320,)|var|float32
call_13051 = relay.TupleGetItem(func_1319_call(relay.reshape(var_13052.astype('float32'), [16, 4, 5])), 0)
call_13053 = relay.TupleGetItem(func_1322_call(relay.reshape(var_13052.astype('float32'), [16, 4, 5])), 0)
func_11991_call = mod.get_global_var('func_11991')
func_11992_call = mutated_mod.get_global_var('func_11992')
call_13054 = func_11991_call()
call_13055 = func_11991_call()
uop_13057 = relay.acosh(bop_13044.astype('float32')) # shape=(6, 14, 1)
func_12843_call = mod.get_global_var('func_12843')
func_12845_call = mutated_mod.get_global_var('func_12845')
const_13076 = relay.const([7,6,-2,5,-2,-6,-7,4,9,5,8,2,10,-3,8,6,-1,1,7,-7,-6,-6,6,-6,-4,1,-9,-2,-2,-9,3,8,-8,-7,7,-5,-7,-4,1,-7,3,8,2,-4,-7,5,-8,5,-3,10,6,-1,-6,-7,-8,-5,4,-4,7,3,3,-5,-2,-7,-5,-5,2,-6,-2,9,-7,3,-10,-10,-7,3,10,10,-8,-6,-4,4,6,8,2,10,-2,1,-1,10,-3,-9,1,-4,6,2,1,-8,7,-5,-5,-8,-7,10,-9,6,-1,6,4,-1,-10,-10,10,-7,6,-5,4,-10,2,9,-10,5,9,5,1,-4,10,1,-4,8,10,-2,7,-5,2,10,6,5,-7,1,-6,-9,8,8,-10,-5,2,-5,1,-7,2,7,5,7,2,-1,10,-9,-2,2,5,-4,-5,3,-9,-9,2,-2,9,10,-5,4,-1,-6,9,-6,-7,9,-9,8,-5,-10,-6,-5,-10,-6,3,2,10,6,-10,-4,-5,9,-5,4,7,-8,-4,7,5,-1,-5,4,-5,-7,-5,1,1,-3,-10,-8,-9,-9,-1,-1,2,-7,-6,-2,-1,7,-9,-5,-8,-9,-5,5,-5,-1,3,-5,3,-3,4,2,-6,3,-7,6,-9,4,-3,-10,-7,7,2,-6,5,-3,-5,-6,4,-6,8,-6,8,2,3,10,-4,10,8,-10,5,1,10,3,-7,-7,-1,-3,-7,10,9,-7,-6,9,-5,8,2,-10,-7,8,-3,10,-10,-3,-9,6,-3,-1,2,-5,-8,-6,2,-5,-10,4,2,7,6,8,5,5,8,8,-5,6,-6,8,-8,-7,-7,-2,-3,-10,1,6,3,5,-7,-9,6,8,6,9,10,-4,5,6,7,8,-6,-5,6,-8,4,5,-3,-1,-10,4,-6,-5,-8,-8,-8,4,-1,-1,-8,-7,-6,-2,7,9,6,5,4,3,-2,-7,-9,2,-10,8,4,10,-10,-9,10,2,3,-9,9,9,7,2,8,8,1,-6,1,-2,-10,8,1,5,-9,-1,8,-2,7,-1,-9,3,-2,4,-4,-6,9,4,6,-4,-6,3,-6,-9,10,9,6,1,10,-5,2,-1,-5,-3,-8,4,-1,-8,-4,9,6,3,-10,1,-10,4,-6,-4,-2,2,3,4,6,10,-10,6,-7,-7,5,-6,-4,6,-7,-3,-7,-1,-2,4,-8,8,5,1,4,8,-5,4,-7,9,3,5,6,2,-10,6,3,3,9,-8,1,2,-2,-5,-7,5,6,-1,3,-2,2,-8,-3,10,6,-7,-6,4,7,9,4,5,-1,6,-10,8,6,6,8,3,6,10,1,1,3,-2,-3,1,-3,-9,-3,6,2,1,10,1,-6,-9,5,4,10,-7,3,7,2,3,-1,-7,5,-3,1,-10,-5,3,6,9,5,1,1,8,-3,1,1,9,5,8,5,5,6,-3,-7,-10,-6,2,8,1,10,7,9,7,7,-9,5,4,4,-6,8,3,9,-1,5,8,3,7,1,-5,-9,-1,-10,6,10,5,9,4,-3,-5,-9,4,-10,4,-2,8,-5,8,3,7,5,5,-10,-2,-4,-3,-9,4,7,9,-9,3,-9,9,-4,-7,-8,2,1,-3,10,7,3,9,9,1,8,-2,-2,6,7,4,-6,-5,2,-2,-6,-2,-10,10,10,7,-5,2,2,-3,3,-6,6,8,1,-10,10,-5,2,10,-7,9,-8,1], dtype = "uint64")#candidate|13076|(660,)|const|uint64
call_13075 = relay.TupleGetItem(func_12843_call(relay.reshape(const_13076.astype('uint64'), [1, 660])), 0)
call_13077 = relay.TupleGetItem(func_12845_call(relay.reshape(const_13076.astype('uint64'), [1, 660])), 0)
uop_13086 = relay.log2(bop_13044.astype('float64')) # shape=(6, 14, 1)
bop_13090 = relay.minimum(uop_13086.astype('int32'), relay.reshape(uop_13032.astype('int32'), relay.shape_of(uop_13086))) # shape=(6, 14, 1)
func_11756_call = mod.get_global_var('func_11756')
func_11760_call = mutated_mod.get_global_var('func_11760')
const_13107 = relay.const(9, dtype = "uint8")#candidate|13107|()|const|uint8
call_13106 = relay.TupleGetItem(func_11756_call(relay.reshape(const_13107.astype('uint8'), []), relay.reshape(const_13076.astype('uint64'), [660,]), ), 6)
call_13108 = relay.TupleGetItem(func_11760_call(relay.reshape(const_13107.astype('uint8'), []), relay.reshape(const_13076.astype('uint64'), [660,]), ), 6)
var_13109 = relay.var("var_13109", dtype = "uint64", shape = (6, 14, 14))#candidate|13109|(6, 14, 14)|var|uint64
bop_13110 = relay.equal(bop_13044.astype('bool'), var_13109.astype('bool')) # shape=(6, 14, 14)
output = relay.Tuple([call_13051,var_13052,call_13054,uop_13057,call_13075,const_13076,bop_13090,call_13106,const_13107,bop_13110,])
output2 = relay.Tuple([call_13053,var_13052,call_13055,uop_13057,call_13077,const_13076,bop_13090,call_13108,const_13107,bop_13110,])
func_13119 = relay.Function([var_13031,var_13052,var_13109,], output)
mod['func_13119'] = func_13119
mod = relay.transform.InferType()(mod)
var_13120 = relay.var("var_13120", dtype = "float32", shape = (6, 14, 1))#candidate|13120|(6, 14, 1)|var|float32
var_13121 = relay.var("var_13121", dtype = "float32", shape = (320,))#candidate|13121|(320,)|var|float32
var_13122 = relay.var("var_13122", dtype = "uint64", shape = (6, 14, 14))#candidate|13122|(6, 14, 14)|var|uint64
output = func_13119(var_13120,var_13121,var_13122,)
func_13123 = relay.Function([var_13120,var_13121,var_13122,], output)
mutated_mod['func_13123'] = func_13123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_13151 = relay.TupleGetItem(func_9014_call(), 0)
call_13152 = relay.TupleGetItem(func_9016_call(), 0)
output = relay.Tuple([call_13151,])
output2 = relay.Tuple([call_13152,])
func_13153 = relay.Function([], output)
mod['func_13153'] = func_13153
mod = relay.transform.InferType()(mod)
mutated_mod['func_13153'] = func_13153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13153_call = mutated_mod.get_global_var('func_13153')
call_13154 = func_13153_call()
output = call_13154
func_13155 = relay.Function([], output)
mutated_mod['func_13155'] = func_13155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11604_call = mod.get_global_var('func_11604')
func_11605_call = mutated_mod.get_global_var('func_11605')
call_13273 = relay.TupleGetItem(func_11604_call(), 0)
call_13274 = relay.TupleGetItem(func_11605_call(), 0)
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_13280 = relay.TupleGetItem(func_10157_call(), 0)
call_13281 = relay.TupleGetItem(func_10159_call(), 0)
output = relay.Tuple([call_13273,call_13280,])
output2 = relay.Tuple([call_13274,call_13281,])
func_13294 = relay.Function([], output)
mod['func_13294'] = func_13294
mod = relay.transform.InferType()(mod)
mutated_mod['func_13294'] = func_13294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13294_call = mutated_mod.get_global_var('func_13294')
call_13295 = func_13294_call()
output = call_13295
func_13296 = relay.Function([], output)
mutated_mod['func_13296'] = func_13296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10325_call = mod.get_global_var('func_10325')
func_10326_call = mutated_mod.get_global_var('func_10326')
call_13307 = relay.TupleGetItem(func_10325_call(), 0)
call_13308 = relay.TupleGetItem(func_10326_call(), 0)
uop_13327 = relay.cos(call_13307.astype('float64')) # shape=(5, 6, 7)
uop_13329 = relay.cos(call_13308.astype('float64')) # shape=(5, 6, 7)
uop_13338 = relay.log2(uop_13327.astype('float32')) # shape=(5, 6, 7)
uop_13340 = relay.log2(uop_13329.astype('float32')) # shape=(5, 6, 7)
output = uop_13338
output2 = uop_13340
func_13356 = relay.Function([], output)
mod['func_13356'] = func_13356
mod = relay.transform.InferType()(mod)
output = func_13356()
func_13357 = relay.Function([], output)
mutated_mod['func_13357'] = func_13357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11191_call = mod.get_global_var('func_11191')
func_11192_call = mutated_mod.get_global_var('func_11192')
call_13386 = func_11191_call()
call_13387 = func_11191_call()
func_13002_call = mod.get_global_var('func_13002')
func_13003_call = mutated_mod.get_global_var('func_13003')
call_13388 = relay.TupleGetItem(func_13002_call(), 0)
call_13389 = relay.TupleGetItem(func_13003_call(), 0)
func_11928_call = mod.get_global_var('func_11928')
func_11929_call = mutated_mod.get_global_var('func_11929')
call_13392 = relay.TupleGetItem(func_11928_call(), 1)
call_13393 = relay.TupleGetItem(func_11929_call(), 1)
output = relay.Tuple([call_13386,call_13388,call_13392,])
output2 = relay.Tuple([call_13387,call_13389,call_13393,])
func_13417 = relay.Function([], output)
mod['func_13417'] = func_13417
mod = relay.transform.InferType()(mod)
mutated_mod['func_13417'] = func_13417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13417_call = mutated_mod.get_global_var('func_13417')
call_13418 = func_13417_call()
output = call_13418
func_13419 = relay.Function([], output)
mutated_mod['func_13419'] = func_13419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8443_call = mod.get_global_var('func_8443')
func_8444_call = mutated_mod.get_global_var('func_8444')
call_13434 = func_8443_call()
call_13435 = func_8443_call()
output = call_13434
output2 = call_13435
func_13459 = relay.Function([], output)
mod['func_13459'] = func_13459
mod = relay.transform.InferType()(mod)
output = func_13459()
func_13460 = relay.Function([], output)
mutated_mod['func_13460'] = func_13460
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13486 = relay.var("var_13486", dtype = "int64", shape = (8, 1, 14))#candidate|13486|(8, 1, 14)|var|int64
var_13487 = relay.var("var_13487", dtype = "int64", shape = (8, 6, 14))#candidate|13487|(8, 6, 14)|var|int64
bop_13488 = relay.add(var_13486.astype('int64'), var_13487.astype('int64')) # shape=(8, 6, 14)
const_13494 = relay.const([[[1,-9,2,1,2,-1,9,1,8,-8,-1,6,4,-8],[8,6,-1,-2,-4,6,-1,2,6,5,-7,2,4,7],[3,4,5,-5,-7,-7,10,-9,-2,-10,-2,4,-9,-9],[-6,5,-10,-3,1,9,-4,10,-2,2,8,4,-10,1],[-7,-4,-5,-2,-8,-9,-2,-8,7,-8,-7,-4,-4,-6],[9,4,8,-10,-7,-9,9,7,-8,-10,2,-5,10,-7],[10,-1,-3,-8,2,-5,2,7,3,7,-6,-8,4,-1],[-3,-9,2,-3,-4,5,8,-9,7,6,-8,3,7,-6],[3,5,4,10,-5,-10,-3,-7,8,-3,-1,-4,1,5],[-7,1,6,7,-2,-5,-1,6,-1,-4,8,-1,4,10]],[[-3,5,3,1,2,1,-6,-8,3,-8,8,1,-9,7],[-8,-1,1,10,-10,5,-8,5,-3,2,1,-10,1,-5],[4,6,-8,-4,10,2,6,3,4,-9,-5,4,-10,-2],[-6,3,-10,5,-3,6,-4,7,-6,3,10,-8,2,10],[-6,4,1,3,4,9,8,3,2,1,2,-7,-5,-9],[6,-10,-4,-4,2,6,7,5,1,-7,-10,2,-2,4],[3,-8,-5,-9,3,-3,3,2,9,5,-7,-4,3,-9],[-4,-4,-8,-5,-1,9,-10,-10,6,-2,1,-4,2,-3],[3,-9,7,-5,8,-6,-6,4,1,-8,-7,-1,-10,5],[2,-8,-4,-3,4,3,-8,10,4,-10,1,-2,-10,7]],[[10,5,-3,-7,2,5,-8,6,7,-9,-4,-8,7,-3],[4,7,1,-6,-5,-1,-4,10,5,7,-6,3,-5,2],[2,7,5,-10,7,1,8,10,-8,-6,-8,5,9,-3],[8,4,-3,5,-8,6,-10,9,9,-2,2,10,-10,6],[-2,4,8,-9,1,-1,-9,-6,4,-9,-7,-9,-8,10],[3,-9,-7,-4,-1,6,-9,2,-3,-6,-6,-9,-5,-3],[-9,-3,9,9,3,10,10,-9,-4,6,-1,-4,7,-1],[6,-7,7,9,-2,-1,-6,2,-9,-5,-1,-10,-3,-9],[-2,7,6,-2,6,10,-4,4,4,-7,6,-5,3,1],[-4,8,-3,-3,-9,-4,8,4,5,-3,-5,-3,10,-9]],[[-5,-9,-3,4,-2,-6,4,5,-2,-6,-6,-7,7,3],[9,-2,-4,-3,10,2,-6,2,-6,2,7,-8,-4,5],[6,3,-1,10,-8,2,-4,-9,-3,-10,9,1,-9,10],[-4,9,4,-7,-6,2,-2,1,1,4,-10,-2,-8,6],[2,3,2,7,-3,-3,-1,-3,9,7,-2,3,7,5],[-10,5,9,-9,-9,9,1,2,-6,5,9,-7,-2,4],[-10,7,2,-2,-1,1,7,3,-3,10,-10,-7,6,9],[-8,9,4,6,9,4,-8,1,7,3,-9,-9,7,-7],[4,1,10,10,8,-7,-5,-9,10,-8,4,-8,4,1],[5,-4,-3,-1,-5,-7,8,-3,9,-5,2,7,-7,-10]],[[-10,4,-10,-6,-3,5,7,-2,6,-7,-7,-3,8,-8],[4,-5,10,2,10,-2,5,3,-9,-9,10,1,10,10],[-5,2,6,-6,9,-6,-3,1,8,-2,-9,-4,-6,-8],[-3,6,-7,-9,-8,-1,10,5,8,3,-10,-2,5,9],[3,10,6,-3,-4,7,-7,8,-6,1,9,-9,-9,7],[7,7,-3,-7,5,-3,-4,1,-1,-7,2,-10,-3,9],[9,8,-1,-7,2,-3,-4,7,9,9,9,-6,5,-3],[4,-10,9,1,3,-2,2,1,4,-5,-8,-10,8,7],[1,-2,1,1,10,-9,10,7,9,-9,7,-5,-8,-1],[2,-10,7,9,5,-9,-2,9,10,-5,5,-3,9,7]],[[-2,4,6,6,-7,3,-4,9,1,-9,4,-1,9,-1],[-1,-6,9,-6,5,8,8,7,4,-10,-4,5,5,8],[1,2,10,-4,9,3,5,-7,-5,-4,10,1,5,3],[3,1,1,-7,-3,-9,2,-6,3,9,-8,6,-9,2],[-6,-1,6,-4,-9,-7,1,-7,-8,-9,8,1,-1,4],[4,3,2,-9,-9,-7,-4,-3,2,8,-4,-1,5,10],[8,7,1,4,-5,4,-7,-2,-7,6,4,-9,10,-1],[-3,2,-5,5,-10,-1,-1,-1,-8,-9,-8,4,6,-8],[-5,-3,10,-10,-8,-10,4,-5,8,3,-9,-1,-7,6],[-2,2,-5,-6,4,-1,4,3,5,-3,4,-9,10,9]],[[-6,-3,-1,-6,3,3,-1,-2,-8,-1,4,5,1,2],[-3,1,8,-8,10,-9,-7,2,9,-10,-10,-9,6,4],[-10,-1,9,-2,7,-8,-5,7,9,9,3,6,-2,-10],[9,-8,-2,1,4,-8,5,-5,3,2,3,-2,1,-2],[3,3,-5,2,-3,-9,-8,5,3,6,4,-9,-1,5],[-1,7,8,7,-3,3,1,3,8,-5,-2,6,10,4],[8,-5,8,-2,-4,-4,-7,-4,-8,2,-9,-5,-9,-8],[10,-10,3,9,7,-10,2,9,10,10,4,-1,8,-3],[-9,-5,3,7,-1,7,-8,3,2,9,-7,9,-2,2],[8,-8,8,-8,-9,7,3,-1,3,-3,6,-9,3,-4]],[[-8,-7,-4,5,-8,-3,10,-10,5,4,-5,-5,8,-6],[1,8,-8,8,-1,4,-6,8,-8,-8,10,-1,6,-8],[9,7,-5,9,-1,-5,-10,4,9,-1,-10,10,-1,-7],[-6,-3,-8,-4,7,-6,2,5,-2,7,2,-8,7,4],[-8,6,3,-8,-2,-6,10,1,5,4,-4,-9,-1,9],[-5,-7,-2,-7,-2,10,1,-5,7,-3,-2,10,-7,2],[-7,5,6,7,7,-4,8,5,9,-10,-5,-9,-9,-3],[-9,4,8,2,-3,3,-10,9,1,7,3,4,-10,5],[3,6,4,10,9,-9,8,4,-7,7,-8,-5,4,9],[4,3,-3,-1,-9,3,2,2,-4,-9,-1,8,-3,-10]]], dtype = "int64")#candidate|13494|(8, 10, 14)|const|int64
bop_13495 = relay.logical_xor(var_13486.astype('uint64'), const_13494.astype('uint64')) # shape=(8, 10, 14)
func_7743_call = mod.get_global_var('func_7743')
func_7752_call = mutated_mod.get_global_var('func_7752')
const_13511 = relay.const(9, dtype = "uint16")#candidate|13511|()|const|uint16
var_13512 = relay.var("var_13512", dtype = "uint16", shape = (600,))#candidate|13512|(600,)|var|uint16
var_13513 = relay.var("var_13513", dtype = "float32", shape = (240,))#candidate|13513|(240,)|var|float32
var_13514 = relay.var("var_13514", dtype = "float32", shape = (320,))#candidate|13514|(320,)|var|float32
var_13515 = relay.var("var_13515", dtype = "float32", shape = (40,))#candidate|13515|(40,)|var|float32
const_13516 = relay.const([False,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,True,True], dtype = "bool")#candidate|13516|(117,)|const|bool
var_13517 = relay.var("var_13517", dtype = "float32", shape = (66, 2))#candidate|13517|(66, 2)|var|float32
const_13518 = relay.const([9,-5,7,-9,-8,-2,-8,9,2,-4,5,-7,-2,3,-3,9,2,6,8,2,6,-4,8,-6,5,-7,9,-3,2,-3,2,-8,-5,-4,10,8,-1,-10,8,-3,-6,-1,4,-6,-4,3,10,-2,8,8,3,5,10,5,3,-9,8,-4,8,3,10,9,9,-4,9,-8,2,6,-9,10,-9,-9,-10,3,2,1,-4,-1,-4,-4,1,-5,5,6,2,-6,-4,-2,-9,-6,3,-4,-10,3,-3,6,9,8,-3,-8,8,-8,8,-1,-6,-9,-4,9,-7,7,9,4,7,2,4,-6,1,-7,5,7,4,-2,6,-10,6,-4,3,3,-8,9,-4,-6,-9,7,10,-7,9,-3,-3,-9,-10,-3,1,-2,-2,2,-4,-2,-3,8,2,-10,-5,7,5,6,-3,10,-5,-2,3,-5,-6,1,6,5,-5,3,5,9,-10,-7,3,4,10,-7,3,2,-8,9,2,-6,-8,-8,-8,2,1,-8,7,-4,-9,-9,-4,-2,-4,10,4,7,-4,-4,2,-8,-7,7,10,10,6,-4,2,7,-6,4,-3,-9,-5,-7,8,10,-6,9,10,-5,-1,-9,4,9,-2,-7,5,2,-10,-7,-6,4,-3,8,-4,-2,-4,8,-8,8,-1,7,-3,-5,9,1,-10,9,-2,9,-2,1,-3,-5,-7,4,-10,-3,9,-5,-4,4,-5,-7,10,3,8,-1,6,-3,9,-10,-8,1,2,6,6,8,-4,10,-3,-7,8,2,-4,-6,2,-3,8,-8,1,8,3,-1,-3,1,4,6,8,8,3,-4,-10,3,-10,-2,-4,-2,-6,-4,-6,4,-4,3,-6,-3,-5,-4,-3,-6,-8,8,7,-9,-5,-2,7,-2,-4,-5,8,-1,-5,9,-10,5,-3,9,4,-1,-10,-9,-8,-2,-8,5,2,-8,-9,-7,1,-10,-4,4,-9,-7,9,8,9,-10,-4,10,10,-5,2,-1,-1,-9,10,-10,-8,7,-3,5,-6,8,1,-8,-3,-2,-2,-1,-4,7,-2,4,-4,-9,8,10,8,-4,3,2,4,4,-8,8,-3,-9,-1,-7,4,3,-8,5,-10,-7,-2,2,6,1,-9,8,-1,-7,10,9,-9,-5,7,5,3,-4,-2,1,2,-3,-1,3,8,6,5,1,8,-1,7,4,-9,-7,3,-10,-9,6,-2,2,10,-9,3,-6,-7,6,4,-6,-6,-3,-10,-6,4,9,-10,7,8,4,7,2,9,-9,-8,4,-7,-5,-8,4,-2,7,3,-1,-1,2,-4,-1,10,4,5,2,-4,7,-9,-5,5,2,-7,8,-7,-7,5,-4,10,-3,-7,-6,-5,5,5,2,2,-9,8,-9,10,-3,-8,9,4,-10,8,-2,-9,6,4,6,-3,-7,4,5,-3,-8,7,8,1,2,4,-4,-10,-8,8,2,-3,-4,4,3,-10,-10,-10,6,-6,1,-4,-6,-5,1,-10,-9,-2,10,-2,7,3,7,-6,5,5,6,2,6,-6,-5,9,-1,-8,-9,5,-2,-3,-2,-6,-5,-4,10,2,-7,2,9,7,2,-3,6,7,6,9,-1,8,5,6,10,-3,8,-9,7,-7,1,-2,-7,3,10,-5,6,-6,5,-8,2,2,-7,9,8,4,5,4,-6,-9,-10,7,8,-9,-7,-8,10,-1,2,2,-3,7,4,-3,-8,-7,7,-6,-7,-5,-6,5,2,5,-5,2,-7,7,-2,-2,-5,1,-4,6,-4,8,-6], dtype = "uint64")#candidate|13518|(660,)|const|uint64
call_13510 = relay.TupleGetItem(func_7743_call(relay.reshape(const_13511.astype('uint16'), []), relay.reshape(var_13512.astype('uint16'), [5, 12, 10]), relay.reshape(var_13513.astype('float32'), [240,]), relay.reshape(var_13514.astype('float32'), [1, 320]), relay.reshape(var_13515.astype('float32'), [40, 1]), relay.reshape(const_13516.astype('bool'), [117,]), relay.reshape(var_13517.astype('float32'), [132,]), relay.reshape(const_13518.astype('uint64'), [1, 660]), ), 10)
call_13519 = relay.TupleGetItem(func_7752_call(relay.reshape(const_13511.astype('uint16'), []), relay.reshape(var_13512.astype('uint16'), [5, 12, 10]), relay.reshape(var_13513.astype('float32'), [240,]), relay.reshape(var_13514.astype('float32'), [1, 320]), relay.reshape(var_13515.astype('float32'), [40, 1]), relay.reshape(const_13516.astype('bool'), [117,]), relay.reshape(var_13517.astype('float32'), [132,]), relay.reshape(const_13518.astype('uint64'), [1, 660]), ), 10)
output = relay.Tuple([bop_13488,bop_13495,call_13510,const_13511,var_13512,var_13513,var_13514,var_13515,const_13516,var_13517,const_13518,])
output2 = relay.Tuple([bop_13488,bop_13495,call_13519,const_13511,var_13512,var_13513,var_13514,var_13515,const_13516,var_13517,const_13518,])
func_13525 = relay.Function([var_13486,var_13487,var_13512,var_13513,var_13514,var_13515,var_13517,], output)
mod['func_13525'] = func_13525
mod = relay.transform.InferType()(mod)
mutated_mod['func_13525'] = func_13525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13525_call = mutated_mod.get_global_var('func_13525')
var_13527 = relay.var("var_13527", dtype = "int64", shape = (8, 1, 14))#candidate|13527|(8, 1, 14)|var|int64
var_13528 = relay.var("var_13528", dtype = "int64", shape = (8, 6, 14))#candidate|13528|(8, 6, 14)|var|int64
var_13529 = relay.var("var_13529", dtype = "uint16", shape = (600,))#candidate|13529|(600,)|var|uint16
var_13530 = relay.var("var_13530", dtype = "float32", shape = (240,))#candidate|13530|(240,)|var|float32
var_13531 = relay.var("var_13531", dtype = "float32", shape = (320,))#candidate|13531|(320,)|var|float32
var_13532 = relay.var("var_13532", dtype = "float32", shape = (40,))#candidate|13532|(40,)|var|float32
var_13533 = relay.var("var_13533", dtype = "float32", shape = (66, 2))#candidate|13533|(66, 2)|var|float32
call_13526 = func_13525_call(var_13527,var_13528,var_13529,var_13530,var_13531,var_13532,var_13533,)
output = call_13526
func_13534 = relay.Function([var_13527,var_13528,var_13529,var_13530,var_13531,var_13532,var_13533,], output)
mutated_mod['func_13534'] = func_13534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8959_call = mod.get_global_var('func_8959')
func_8961_call = mutated_mod.get_global_var('func_8961')
call_13546 = relay.TupleGetItem(func_8959_call(), 0)
call_13547 = relay.TupleGetItem(func_8961_call(), 0)
output = call_13546
output2 = call_13547
func_13550 = relay.Function([], output)
mod['func_13550'] = func_13550
mod = relay.transform.InferType()(mod)
output = func_13550()
func_13551 = relay.Function([], output)
mutated_mod['func_13551'] = func_13551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13002_call = mod.get_global_var('func_13002')
func_13003_call = mutated_mod.get_global_var('func_13003')
call_13566 = relay.TupleGetItem(func_13002_call(), 0)
call_13567 = relay.TupleGetItem(func_13003_call(), 0)
output = relay.Tuple([call_13566,])
output2 = relay.Tuple([call_13567,])
func_13568 = relay.Function([], output)
mod['func_13568'] = func_13568
mod = relay.transform.InferType()(mod)
mutated_mod['func_13568'] = func_13568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13568_call = mutated_mod.get_global_var('func_13568')
call_13569 = func_13568_call()
output = call_13569
func_13570 = relay.Function([], output)
mutated_mod['func_13570'] = func_13570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_13577 = func_11516_call()
call_13578 = func_11516_call()
output = call_13577
output2 = call_13578
func_13583 = relay.Function([], output)
mod['func_13583'] = func_13583
mod = relay.transform.InferType()(mod)
output = func_13583()
func_13584 = relay.Function([], output)
mutated_mod['func_13584'] = func_13584
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_13591 = func_11516_call()
call_13592 = func_11516_call()
output = call_13591
output2 = call_13592
func_13595 = relay.Function([], output)
mod['func_13595'] = func_13595
mod = relay.transform.InferType()(mod)
mutated_mod['func_13595'] = func_13595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13595_call = mutated_mod.get_global_var('func_13595')
call_13596 = func_13595_call()
output = call_13596
func_13597 = relay.Function([], output)
mutated_mod['func_13597'] = func_13597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11809_call = mod.get_global_var('func_11809')
func_11810_call = mutated_mod.get_global_var('func_11810')
call_13614 = relay.TupleGetItem(func_11809_call(), 1)
call_13615 = relay.TupleGetItem(func_11810_call(), 1)
func_13294_call = mod.get_global_var('func_13294')
func_13296_call = mutated_mod.get_global_var('func_13296')
call_13626 = relay.TupleGetItem(func_13294_call(), 1)
call_13627 = relay.TupleGetItem(func_13296_call(), 1)
func_13002_call = mod.get_global_var('func_13002')
func_13003_call = mutated_mod.get_global_var('func_13003')
call_13634 = relay.TupleGetItem(func_13002_call(), 0)
call_13635 = relay.TupleGetItem(func_13003_call(), 0)
output = relay.Tuple([call_13614,call_13626,call_13634,])
output2 = relay.Tuple([call_13615,call_13627,call_13635,])
func_13640 = relay.Function([], output)
mod['func_13640'] = func_13640
mod = relay.transform.InferType()(mod)
mutated_mod['func_13640'] = func_13640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13640_call = mutated_mod.get_global_var('func_13640')
call_13641 = func_13640_call()
output = call_13641
func_13642 = relay.Function([], output)
mutated_mod['func_13642'] = func_13642
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12145_call = mod.get_global_var('func_12145')
func_12147_call = mutated_mod.get_global_var('func_12147')
call_13728 = func_12145_call()
call_13729 = func_12145_call()
output = relay.Tuple([call_13728,])
output2 = relay.Tuple([call_13729,])
func_13733 = relay.Function([], output)
mod['func_13733'] = func_13733
mod = relay.transform.InferType()(mod)
output = func_13733()
func_13734 = relay.Function([], output)
mutated_mod['func_13734'] = func_13734
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11928_call = mod.get_global_var('func_11928')
func_11929_call = mutated_mod.get_global_var('func_11929')
call_13740 = relay.TupleGetItem(func_11928_call(), 1)
call_13741 = relay.TupleGetItem(func_11929_call(), 1)
func_9974_call = mod.get_global_var('func_9974')
func_9975_call = mutated_mod.get_global_var('func_9975')
call_13742 = func_9974_call()
call_13743 = func_9974_call()
func_12119_call = mod.get_global_var('func_12119')
func_12123_call = mutated_mod.get_global_var('func_12123')
var_13749 = relay.var("var_13749", dtype = "bool", shape = (117,))#candidate|13749|(117,)|var|bool
const_13750 = relay.const([[1.375535,-5.685577],[6.174332,-7.325358],[9.392918,-4.309361],[3.897333,4.920306],[2.251551,3.700488],[-1.112593,8.110734],[-3.984086,-4.724322],[-8.946174,8.978495],[-9.028567,-0.728393],[-1.046607,-9.820816],[-6.722532,-3.129396],[-6.839694,-9.424005],[5.951132,-8.561604],[0.753485,-4.385678],[4.037156,-5.002541],[-7.524522,6.007184],[7.886034,-0.215848],[-8.163982,6.543226],[-8.228191,-3.920145],[6.553197,-8.529582],[-2.972262,9.645232],[-1.654638,-8.774063],[-1.469262,-2.234570],[-2.473485,3.883256],[0.104875,5.654194],[1.711796,2.920946],[-8.346340,-6.003812],[-2.028796,-9.185601],[0.292333,-7.696481],[-6.061797,5.944076],[6.380401,7.786609],[6.930064,8.393792],[3.755414,-9.805565],[8.405051,-6.440514],[7.226306,-5.177731],[9.048489,0.122316],[-9.104720,7.353637],[-8.121544,1.924415],[-4.122706,3.024099],[-6.299443,-0.897321],[-3.430353,-5.651437],[-2.208617,9.020182],[6.812130,4.677862],[5.016067,5.375998],[-1.626335,-3.931663],[-6.925897,-8.697903],[-7.438836,-3.584877],[-9.564574,-8.928946],[-7.459865,7.005752],[4.898805,-3.974137],[-8.355711,-1.962635],[-2.732977,7.865890],[-4.962979,5.433749],[2.729222,4.750090],[-0.021562,-7.522837],[-9.997122,4.326509],[4.247525,-3.957475],[9.815017,6.807395],[-5.983714,3.537369],[-5.637198,-5.669183],[-1.257786,8.929852],[2.430206,-1.166591],[-5.091104,4.803196],[6.660367,7.382557],[4.908769,-5.329149],[4.974031,-0.983815],[9.752173,-4.837249],[-4.792077,-2.587237],[1.188561,-1.953827],[-1.222930,-2.759333],[-6.720678,3.572215],[-8.825328,-5.140133],[-0.452995,-5.757296],[6.043493,-9.224922],[1.128873,-3.642116],[8.991882,-1.447969],[-8.308386,3.655290],[3.629834,2.499637],[7.231541,-1.673453],[-6.322362,6.082778],[0.624544,-3.284062],[-0.681679,0.857428],[0.290045,0.236571],[-3.536463,6.655824],[8.298876,0.976109],[-4.402498,-8.976841],[5.031625,4.947478],[1.887320,7.201911],[3.662910,8.531494],[-3.413919,2.455402],[-0.772196,-5.167787],[-2.542969,2.476593],[-5.020430,8.628566],[-1.333382,5.655392],[-2.631149,0.053928],[7.755903,-9.634216],[-9.494234,2.551711],[-3.830399,-2.237548],[5.895465,4.860466],[1.732647,4.797757],[2.852461,-8.259536],[-4.536903,9.762938],[0.398113,2.254907],[8.230854,4.369582],[7.826596,-4.522353],[9.840241,3.587028],[0.623052,-4.664538],[5.746416,9.925817],[-8.959399,-8.814560],[1.232433,2.762457],[-0.016230,9.057034],[-8.647843,5.064785],[9.484010,7.216971],[0.486690,-7.966740],[6.625111,0.140633],[-7.670639,2.097207],[-8.516573,-8.873555],[-0.499349,-6.134984],[-6.487370,-5.150215],[-7.534459,-6.248502],[-6.150601,-7.261197],[-8.576636,-7.509401],[-8.058128,9.255410],[-6.141052,2.867700],[-0.341885,-0.372939],[-1.149111,-0.390289],[4.239560,6.461664],[-6.919752,7.187375],[-4.236873,-4.565604],[-0.469911,-7.351411],[-5.113591,-6.768722],[4.930886,-2.601617],[4.022010,-2.903374],[4.772916,-3.156908],[7.889900,6.681009],[0.929237,-4.084529],[-7.672400,4.306939],[-1.903738,6.084365],[4.159924,2.863394],[-8.128064,-3.044522],[5.319927,7.515734],[3.998181,9.402769],[5.232813,6.272132],[7.746691,-4.692143],[-1.358966,9.068549],[-5.015746,-6.471690],[-7.817880,-8.764429],[5.835375,-0.768689],[3.143258,1.985857],[4.901165,2.588481],[8.382535,0.238906],[8.581596,8.816282],[8.663456,-1.533399],[4.488531,0.906408],[-0.120229,-6.942375],[8.151947,-5.064778],[-8.373919,2.637308],[-5.835367,4.149314],[9.159205,4.276541],[-9.091704,6.488245]], dtype = "float32")#candidate|13750|(160, 2)|const|float32
call_13748 = relay.TupleGetItem(func_12119_call(relay.reshape(var_13749.astype('bool'), [117,]), relay.reshape(const_13750.astype('float32'), [320,]), ), 6)
call_13751 = relay.TupleGetItem(func_12123_call(relay.reshape(var_13749.astype('bool'), [117,]), relay.reshape(const_13750.astype('float32'), [320,]), ), 6)
func_13153_call = mod.get_global_var('func_13153')
func_13155_call = mutated_mod.get_global_var('func_13155')
call_13756 = relay.TupleGetItem(func_13153_call(), 0)
call_13757 = relay.TupleGetItem(func_13155_call(), 0)
func_11299_call = mod.get_global_var('func_11299')
func_11301_call = mutated_mod.get_global_var('func_11301')
call_13774 = func_11299_call()
call_13775 = func_11299_call()
output = relay.Tuple([call_13740,call_13742,call_13748,var_13749,const_13750,call_13756,call_13774,])
output2 = relay.Tuple([call_13741,call_13743,call_13751,var_13749,const_13750,call_13757,call_13775,])
func_13778 = relay.Function([var_13749,], output)
mod['func_13778'] = func_13778
mod = relay.transform.InferType()(mod)
mutated_mod['func_13778'] = func_13778
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13779 = relay.var("var_13779", dtype = "bool", shape = (117,))#candidate|13779|(117,)|var|bool
func_13778_call = mutated_mod.get_global_var('func_13778')
call_13780 = func_13778_call(var_13779)
output = call_13780
func_13781 = relay.Function([var_13779], output)
mutated_mod['func_13781'] = func_13781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9974_call = mod.get_global_var('func_9974')
func_9975_call = mutated_mod.get_global_var('func_9975')
call_13882 = func_9974_call()
call_13883 = func_9974_call()
output = relay.Tuple([call_13882,])
output2 = relay.Tuple([call_13883,])
func_13903 = relay.Function([], output)
mod['func_13903'] = func_13903
mod = relay.transform.InferType()(mod)
output = func_13903()
func_13904 = relay.Function([], output)
mutated_mod['func_13904'] = func_13904
mutated_mod = relay.transform.InferType()(mutated_mod)
const_13912 = relay.const([[[-6.004300,6.665886,9.453277,9.862449,2.605136,-1.680606,-5.169279,-0.674389,-7.862179,-0.655847,-6.453987,8.270648,5.173357,-3.450775,-9.300082],[-7.296871,6.587077,-9.933561,7.814157,9.934655,6.726196,2.258501,0.078893,8.122852,9.238936,1.770088,5.199644,2.612859,-9.947526,6.630736],[-3.392518,6.852565,6.643819,-9.361303,0.402660,8.121328,6.481071,-0.617711,2.374532,-1.484166,-8.733892,-0.069944,-0.794479,-1.927400,-4.637949]],[[-9.085520,0.917998,-5.976028,2.772624,3.139553,-0.141536,0.973576,5.893825,1.642965,-7.175004,1.307306,4.599758,-1.721455,-4.434597,-7.137136],[-8.391311,4.290408,-4.346077,-3.393637,-1.826957,-9.409828,0.824169,-5.781454,-7.150242,2.633741,4.993761,9.650424,-5.281364,-6.525370,-3.084514],[1.250991,4.180850,-6.365162,3.141141,5.179060,-9.531270,-0.326158,-3.131834,-6.857446,-1.938861,3.140352,-4.022122,6.424200,-2.782181,3.311780]],[[-5.132098,3.481589,2.418333,-6.566510,-4.424389,-9.830620,7.869886,-3.403231,2.524773,-6.743166,-0.018161,1.385450,-8.792403,-0.153334,2.646624],[5.447274,-4.744296,5.371395,-8.918322,-8.547847,-0.117225,3.143908,-9.531251,6.332853,-8.981316,8.644950,7.215976,-4.825233,0.445009,-6.074439],[-2.788746,1.001984,-8.678097,3.300921,-3.957914,1.327947,-9.262195,-9.351918,4.988471,9.659209,-5.646534,-3.644492,3.472649,3.483706,0.729277]]], dtype = "float64")#candidate|13912|(3, 3, 15)|const|float64
uop_13913 = relay.sin(const_13912.astype('float64')) # shape=(3, 3, 15)
func_1524_call = mod.get_global_var('func_1524')
func_1528_call = mutated_mod.get_global_var('func_1528')
const_13916 = relay.const([[6,1,8,-8,-8,8,4,9,9,-3,-3,4,8,5,8,1,9,-7,3,-6,6,4,8,-3,-1,9,-5,-2,-5,-3,2,6,-6,-10,10,2,10,7,-9,-6,-9,2,7,4,-3,-4,1,-8,-5,-5,-4,3,1,3,-10,-10,-5,-2,-6,-2,-5,8,6,-10,6,-6,-2,-8,6,-3,-2,7,5,10,8,-4,8,-9,-10,5,-6,-8,-9,1,8,6,-7,7,-2,7,9,-3,3,-3,-10,-9,-1,-3,1,-10,8,-1,8,-10,7,2,-9,4,6,-5,6,-3,10,9,-1,-2,-4,-5,3,5,-3,5,-2,3,6,6,-3,9,8,5,-7,-10,10,-5,1,4,-7,-7,9,10,-10,-7,7,6,-4,-5,-8,1,-10,-2,6,-8,-6,-5,7,-10,10,-1,1,-4,-6,7,-4,3,-7,-7,-2,8,-10,-3,-6,3,8,7,-1,6,10,3,-2,-7,3,3,-9,-5,4,5,1,-8,-3,-2,-3,-4,-4,6,5,-6,-7,6,-8,4,-9,1,-6,10,-3,-4,3,-1,4,2,1,8,6,4,4,-7,-5,-2,-9,-10,7,1,1,4,9,7,-5,-8,10,5,9,7,-10,7,-3,2,-3,9,-4,1,10,-5,-2,4,-8,6,-10,-3,1,-8,9,4,2,5,-8,-1,-4,-5,-3,8,7,9,8,8,4,-6,3,-4,-5,10,5,4,-10,-8,8,-6,-2,4,7,-1,-7,3,-7,6,-5,-7,-10,2,2,6,-7,-6,-7,1,4,6,-7,3,5,-7,-8,5,-7,-1,-8,-10,-7,-4,-9,-8,-4,-6,3,-6,1,-1,10,-8,-4,8,3,-6,4,-5,-4,-10,9,-1,7,1,3,-8,9,-1,-4,4,9,-2,-10,8,1,-4,5,-3,5,2,-7,10,-8,-10,2,-4,3,-3,-2,-9,-2,3,8,-10,9,10,4,-3,-5,-9,-8,9,8,6,-5,-2,10,4,1,-3,-8,6,7,8,-4,-8,-9,-4,10,-4,-7,-4,2,-6,-2,3,4,-3,1,-2,6,5,-6,2,-1,3,-3,-6,2,9,-3,-5,-4,-7,-2,7,-8,5,5,1,4,-5,-8,-5,5,8,6,6,-4,4,9,-3,-8,-10,-6,9,3,-8,-7,3,6,-1,-5,-4,-9,4,-2,4,9,-10,-4,-6,3,10,-6,-5,6,-7,-2,-1,-9,-8,4,-10,-5,-8,9,8,8,3,4,-8,-3,-9,-8,-7,-5,-10,6,-4,8,2,7,-9,-1,-3,-8,3,-8,8,5,4,10,-3,-4,9,-2,-9,-4,-6,-3,-10,-9,-4,-7,2,-6,4,-10,2,5,-8,-2,-5,-7,1,-9,-1,-4,-5,5,-5,-4,7,-5,10,10,-6,-6,9,2,-3,3,-7,-9,7,10,7,2,-1,-2,-8,8,-7,5,-8,-7,5,-5,4,7,-7,7,2,-7,6,-4,4,-8,-8,6,-9,-7,1,-7,5,10,2,4,-5,-6,2,7,6,4,8,2,-1,2,-10,-8,-4,6,6,-9,-3,-3,-7,-9,-6,8,3,1,-10,7,-3,-4,-5,-10,-2,-5,-6,-8,-1,-9,-1,2,7,-9,8,7,-3,6,-3,1,9,-8,6,-9,4,5,5,9,-3,-8,-4,-2,-8,-5,9,4,-5,3,10,-8,10,-10,-1,8,7,4,-1,-8,-5,9,2,9,8,9,-6,2,10,-2,1,2,-5,9,3,6,4,-9,3,-4,-2]], dtype = "uint64")#candidate|13916|(1, 660)|const|uint64
const_13917 = relay.const([-9.500412,5.077566,9.074574,-1.114770,-5.588700,-8.153982,-1.271082,-9.971235,-6.635693,9.980386,-9.369566,3.269314,1.407586,2.352451,1.987182,0.349089,-1.628414,6.188048,6.328840,-5.401893,6.521883,-8.397728,-0.908800,9.911214,2.417087,9.999880,-5.278165,-7.883807,5.864667,-3.778490,-3.775771,-0.197482,-0.158189,-6.709940,8.378755,6.885290,-4.399686,1.695974,-5.942327,0.150645,2.226763,-7.099587,2.211212,5.535848,-0.766479,7.723583,-0.459188,2.169399,2.555778,-8.849927,0.367593,8.615671,2.921785,-1.103663,9.399572,9.159362,3.144636,1.148604,-9.313767,2.593068,-8.837726,0.131029,-6.509877,-4.360511,1.806035,-0.338770,-9.241028,-8.020733,-6.488019,-5.975761,-1.079104,-0.191659,8.046648,-0.648649,3.698211,-0.733809,-3.173309,-8.345223,-8.943668,-2.727180,9.793999,-8.001627,-6.729489,7.561289,-9.454308,-7.623835,6.679138,-8.434800,-6.958401,-8.649550,-1.536667,-7.257382,-9.579661,0.772586,2.894772,-0.156980,-3.654096,-2.121652,7.515574,-8.704260,6.198040,-4.731990,2.794423,7.606059,2.360306,5.061906,-0.935671,-8.828434,-2.607557,-2.762329,3.928424,-7.459019,4.345047,-4.983253,-3.395424,-1.123217,-7.745850,-4.359839,8.720556,9.557848,7.528145,-6.743033,-3.196186,7.444259,-7.204748,-5.715455,-7.892257,-4.761562,-5.038293,5.786248,2.996089,-9.313245,-6.518953,5.486807,7.771359,0.598104,-2.097397,-4.639970,-4.192672,8.248672,3.686346,0.009756,1.398148,-5.146439,-5.909578,-5.554543,0.715057,1.869755,-7.962764,-3.347435,-9.143500,-3.897313,7.208384,8.546379,-0.480657,8.665749,5.219564,-4.843449,-6.655956,-5.197636,-1.776993,-5.623720,6.976504,2.734742,-9.915546,2.250194,0.934951,9.329246,2.216490,4.481408,-4.885029,4.393031,2.442782,-5.392812,-2.311037,-4.762203,3.761211,5.628901,4.264271,-1.952806,-5.086143,-2.858713,-8.825354,-3.376273,-8.236673,4.334950,-1.222094,-6.924287,-0.282546,7.295397,2.435569,9.889239,-3.361218,-2.625653,-6.906166,-9.718117,-7.841161,-9.912540,-5.085784,-8.148124,-9.890328,0.696561,7.821831,-1.257567,-4.227864,-7.761925,-2.089498,2.073735,-6.550585,-1.989009,-2.332387,5.922205,5.972655,6.727880,7.254404,-8.835110,-1.280299,-6.744190,-0.089089,4.613852,9.302412,-0.363417,-1.809701,-4.074299,8.611435,0.321242,7.573495,1.014722,-8.037642,9.105370,-1.885464,-7.126576,4.195261,-1.633852,8.925841,6.396396,-0.204423,-7.036393,2.741634,4.209736,8.683690,-4.925805,-8.302293,7.463402,4.322959,-2.389914,9.131099,-7.371992,1.353556,-2.929544,-9.333130,5.839807,5.535677,1.785132,3.092299,-1.023373,7.011075,1.299354,-2.809739,4.607502,2.208094,2.319284,-5.496838,-7.069464,4.077192,-9.502990,-6.028977,-6.709324,-1.761592,-0.239313,-9.835408,-2.240695,8.527528,7.144912,9.010421,9.898919,-4.390128,8.666150,-7.126731,6.005358,-2.075779,-8.489202,6.154946,-0.945694,-5.251822,4.965868,1.932594,9.311082,-0.045329,-2.987911,0.258750,-5.639401,4.178061,-9.442920,1.820509,7.755152,5.882807,-8.332869,-0.457934,-6.420760,8.773082,2.933165,-1.414398,-6.978553,-3.273649,-9.467890,-4.592339,9.898150,-7.921444,-6.605008,6.505248,2.241999,8.595975,-5.717595,-0.702204,-8.494736,-7.975254,2.053849,-5.984514,2.976154], dtype = "float32")#candidate|13917|(320,)|const|float32
call_13915 = relay.TupleGetItem(func_1524_call(relay.reshape(const_13916.astype('uint64'), [5, 12, 11]), relay.reshape(const_13916.astype('uint64'), [5, 12, 11]), relay.reshape(const_13917.astype('float32'), [1, 320]), ), 1)
call_13918 = relay.TupleGetItem(func_1528_call(relay.reshape(const_13916.astype('uint64'), [5, 12, 11]), relay.reshape(const_13916.astype('uint64'), [5, 12, 11]), relay.reshape(const_13917.astype('float32'), [1, 320]), ), 1)
func_11191_call = mod.get_global_var('func_11191')
func_11192_call = mutated_mod.get_global_var('func_11192')
call_13940 = func_11191_call()
call_13941 = func_11191_call()
func_10300_call = mod.get_global_var('func_10300')
func_10305_call = mutated_mod.get_global_var('func_10305')
var_13943 = relay.var("var_13943", dtype = "bool", shape = (117,))#candidate|13943|(117,)|var|bool
var_13944 = relay.var("var_13944", dtype = "bool", shape = (702,))#candidate|13944|(702,)|var|bool
const_13945 = relay.const([2.282806,8.634566,-0.386919,-0.405705,2.814395,-6.711462,4.413995,-5.868724,-6.138136,3.943446,4.257802,3.116739,8.383670,-4.468771,7.821461,5.180367,-8.983782,7.001596,2.695816,-0.110407,-7.622348,7.563791,-7.728743,-4.683290,9.912894,1.124365,-8.262108,7.353793,-2.683741,5.757628,-2.420773,-9.186510,6.187364,6.669233,2.533218,8.420733,2.070116,-1.502977,1.668263,-2.286908,-6.016833,0.936379,-2.547134,3.129059,7.372615,-8.518961,1.676410,-5.494665,-1.447221,9.422303,8.680771,6.347902,2.860019,4.830190,-5.472225,-8.301925,4.898970,-8.026193,-2.577465,8.800787,-2.996238,4.090484,-9.595702,-5.160774,-4.546991,6.392207,2.993603,-3.138881,-7.432328,1.964352,8.108303,0.786506,7.463641,-0.196600,0.253305,1.703464,-7.279437,4.555368,2.230565,2.550342,6.609960,4.985719,-8.573841,-7.197978,4.279476,4.228106,7.737564,-8.516970,-7.085137,-4.748826,-4.618361,9.943825,-8.455526,1.604014,0.529390,8.068465,6.816520,5.084204,-2.583062,-6.513268,0.702863,-9.932821,7.232417,8.550269,-2.625302,9.680899,-1.221799,0.735853,-9.254531,-9.535213,6.995666,-8.108665,-9.237111,-2.090982,4.447015,0.476236,9.770158,5.434730,-4.912750,-5.370509,-4.705687,9.181571,2.445497,-6.176794,7.046834,9.628170,-2.429035,-7.639278,0.628901,-2.291609,4.305027,1.250553], dtype = "float32")#candidate|13945|(132,)|const|float32
call_13942 = relay.TupleGetItem(func_10300_call(relay.reshape(var_13943.astype('bool'), [1, 117]), relay.reshape(var_13944.astype('bool'), [702,]), relay.reshape(const_13945.astype('float32'), [132,]), relay.reshape(const_13916.astype('uint64'), [660,]), ), 2)
call_13946 = relay.TupleGetItem(func_10305_call(relay.reshape(var_13943.astype('bool'), [1, 117]), relay.reshape(var_13944.astype('bool'), [702,]), relay.reshape(const_13945.astype('float32'), [132,]), relay.reshape(const_13916.astype('uint64'), [660,]), ), 2)
func_11299_call = mod.get_global_var('func_11299')
func_11301_call = mutated_mod.get_global_var('func_11301')
call_13951 = func_11299_call()
call_13952 = func_11299_call()
output = relay.Tuple([uop_13913,call_13915,const_13916,const_13917,call_13940,call_13942,var_13943,var_13944,const_13945,call_13951,])
output2 = relay.Tuple([uop_13913,call_13918,const_13916,const_13917,call_13941,call_13946,var_13943,var_13944,const_13945,call_13952,])
func_13954 = relay.Function([var_13943,var_13944,], output)
mod['func_13954'] = func_13954
mod = relay.transform.InferType()(mod)
var_13955 = relay.var("var_13955", dtype = "bool", shape = (117,))#candidate|13955|(117,)|var|bool
var_13956 = relay.var("var_13956", dtype = "bool", shape = (702,))#candidate|13956|(702,)|var|bool
output = func_13954(var_13955,var_13956,)
func_13957 = relay.Function([var_13955,var_13956,], output)
mutated_mod['func_13957'] = func_13957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10165_call = mod.get_global_var('func_10165')
func_10167_call = mutated_mod.get_global_var('func_10167')
call_14069 = relay.TupleGetItem(func_10165_call(), 0)
call_14070 = relay.TupleGetItem(func_10167_call(), 0)
output = relay.Tuple([call_14069,])
output2 = relay.Tuple([call_14070,])
func_14077 = relay.Function([], output)
mod['func_14077'] = func_14077
mod = relay.transform.InferType()(mod)
output = func_14077()
func_14078 = relay.Function([], output)
mutated_mod['func_14078'] = func_14078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13583_call = mod.get_global_var('func_13583')
func_13584_call = mutated_mod.get_global_var('func_13584')
call_14104 = func_13583_call()
call_14105 = func_13583_call()
output = relay.Tuple([call_14104,])
output2 = relay.Tuple([call_14105,])
func_14119 = relay.Function([], output)
mod['func_14119'] = func_14119
mod = relay.transform.InferType()(mod)
mutated_mod['func_14119'] = func_14119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14119_call = mutated_mod.get_global_var('func_14119')
call_14120 = func_14119_call()
output = call_14120
func_14121 = relay.Function([], output)
mutated_mod['func_14121'] = func_14121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11191_call = mod.get_global_var('func_11191')
func_11192_call = mutated_mod.get_global_var('func_11192')
call_14135 = func_11191_call()
call_14136 = func_11191_call()
func_13568_call = mod.get_global_var('func_13568')
func_13570_call = mutated_mod.get_global_var('func_13570')
call_14170 = relay.TupleGetItem(func_13568_call(), 0)
call_14171 = relay.TupleGetItem(func_13570_call(), 0)
output = relay.Tuple([call_14135,call_14170,])
output2 = relay.Tuple([call_14136,call_14171,])
func_14174 = relay.Function([], output)
mod['func_14174'] = func_14174
mod = relay.transform.InferType()(mod)
output = func_14174()
func_14175 = relay.Function([], output)
mutated_mod['func_14175'] = func_14175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12470_call = mod.get_global_var('func_12470')
func_12472_call = mutated_mod.get_global_var('func_12472')
call_14191 = func_12470_call()
call_14192 = func_12470_call()
output = call_14191
output2 = call_14192
func_14195 = relay.Function([], output)
mod['func_14195'] = func_14195
mod = relay.transform.InferType()(mod)
mutated_mod['func_14195'] = func_14195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14195_call = mutated_mod.get_global_var('func_14195')
call_14196 = func_14195_call()
output = call_14196
func_14197 = relay.Function([], output)
mutated_mod['func_14197'] = func_14197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13568_call = mod.get_global_var('func_13568')
func_13570_call = mutated_mod.get_global_var('func_13570')
call_14236 = relay.TupleGetItem(func_13568_call(), 0)
call_14237 = relay.TupleGetItem(func_13570_call(), 0)
func_8088_call = mod.get_global_var('func_8088')
func_8089_call = mutated_mod.get_global_var('func_8089')
call_14251 = relay.TupleGetItem(func_8088_call(), 0)
call_14252 = relay.TupleGetItem(func_8089_call(), 0)
func_11191_call = mod.get_global_var('func_11191')
func_11192_call = mutated_mod.get_global_var('func_11192')
call_14256 = func_11191_call()
call_14257 = func_11191_call()
func_1319_call = mod.get_global_var('func_1319')
func_1322_call = mutated_mod.get_global_var('func_1322')
const_14277 = relay.const([[-9.415933,-3.364215,-1.284038,0.679306,2.176106,9.371544,0.852652,6.870028],[8.123309,1.135689,-2.856591,2.918504,4.312019,-9.838392,0.975304,1.888627],[1.628736,5.778199,2.586937,4.084056,4.803885,2.854249,2.263101,3.261902],[-5.314235,6.126304,-9.681925,7.818791,2.196052,1.562280,1.987292,0.943330],[-0.889356,-1.523529,3.542370,-2.949358,-9.413756,4.318117,4.522013,8.903246],[1.221597,-1.219355,1.949727,4.453382,7.456376,-6.503191,7.443695,-0.615220],[-1.844653,7.566084,-4.751357,-5.542839,-1.477406,-1.563111,-5.515077,8.794664],[-7.422371,4.961267,1.295195,-7.232884,-0.229197,9.973107,-7.492247,8.629928],[-9.645053,-3.651739,7.735344,4.056672,-1.892412,7.516192,4.879493,-1.664525],[-7.004209,-9.537041,-7.357648,-4.267328,1.430713,5.985719,8.534999,-9.039799],[6.189166,-0.093447,3.027594,-7.220257,6.691934,4.948140,-0.187357,-2.106156],[7.730391,-3.687014,-3.926669,-1.801571,-2.238508,0.908405,4.225147,0.070816],[0.905968,0.282196,-5.341005,-0.323458,0.132806,-7.480607,-1.184386,-9.291910],[0.531676,4.251297,5.192900,6.871866,7.243898,-2.606949,-0.737500,-5.660625],[0.781481,5.231349,0.394021,-3.976277,5.143516,3.512813,1.518871,0.565779],[-1.336921,-9.347321,3.652241,-4.044921,3.662742,1.155376,-2.761948,1.562470],[4.866877,2.791494,-1.571208,3.641547,2.871546,7.235652,-0.070463,4.352523],[-0.947199,-4.554571,-6.430351,-1.394052,0.436581,6.694138,3.317810,-5.377151],[1.511372,-1.993723,4.502445,3.434886,-1.651348,5.336428,-9.701306,0.437201],[6.335107,-7.035929,-3.708871,9.233072,-6.520651,-5.827727,4.716762,-3.578449],[-9.835781,-7.523193,-8.790698,-3.667338,0.028346,7.830232,0.283369,-0.664278],[-2.073031,-1.993958,1.241488,2.485225,-6.498192,-7.792727,-1.269622,3.190265],[9.404675,-7.794587,3.321662,-9.839527,-7.887990,-3.601931,-3.109118,-5.621423],[0.068230,-1.877699,-2.214247,-9.250336,2.520168,-9.867128,7.233800,-7.385472],[-5.610922,-1.899531,-8.764605,-3.324828,-9.892010,-4.388524,3.709323,-7.119838],[3.927111,2.004523,-4.828883,-0.376224,-3.475513,0.090649,-9.303414,-9.501373],[-8.710384,1.506950,3.194498,3.779067,-1.451632,8.591397,7.774563,1.512611],[-4.075269,-9.085157,-9.389890,-2.930268,-9.711587,4.244218,3.512328,3.774808],[-8.749167,-4.254499,-3.522549,-0.153602,2.388937,-8.505646,2.070949,9.790930],[-1.696452,-8.661711,1.720998,-6.518412,-6.945314,-7.994593,9.703227,7.065975],[-5.583945,-6.323545,0.938032,-9.221840,-0.873088,3.666878,-8.310145,5.656198],[1.299711,3.291198,-1.559885,-0.759124,6.709331,-9.351596,-9.900176,7.426466],[-5.911497,5.820482,-0.371929,-3.778241,-4.933032,-4.916823,6.843303,3.705395],[4.113487,5.583026,-0.837547,-5.772056,-6.785831,4.609359,-5.555459,-4.728275],[-1.239859,-0.142073,0.022573,0.498297,5.570776,-5.573982,7.784879,4.446393],[-4.593268,-2.148603,-8.142158,7.381912,4.954320,1.774123,4.920044,-9.977295],[8.647692,-0.048039,-6.908658,-3.062089,0.870847,-9.973636,-9.755135,0.256784],[-2.138067,-4.064092,-3.296920,7.939971,-3.466025,0.234880,-6.883507,0.322809],[-0.662342,-9.197820,5.857838,-3.699572,4.270931,7.919205,-6.741023,4.595623],[-5.912439,0.259908,6.847016,-6.436978,3.999383,7.916224,-4.500596,6.047537]], dtype = "float32")#candidate|14277|(40, 8)|const|float32
call_14276 = relay.TupleGetItem(func_1319_call(relay.reshape(const_14277.astype('float32'), [16, 4, 5])), 0)
call_14278 = relay.TupleGetItem(func_1322_call(relay.reshape(const_14277.astype('float32'), [16, 4, 5])), 0)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_14280 = relay.var("var_14280", dtype = "bool", shape = (117,))#candidate|14280|(117,)|var|bool
var_14281 = relay.var("var_14281", dtype = "bool", shape = (702,))#candidate|14281|(702,)|var|bool
const_14282 = relay.const([0.657517,-7.951607,8.733013,5.509071,-2.799414,-5.139571,-4.392585,-4.341078,-3.312386,5.268410,-9.426230,5.616544,4.803408,6.606559,-8.411855,1.106762,-4.589801,-7.572976,2.766750,7.300659,8.437674,-7.209292,6.889143,-4.524747,0.632377,-3.511912,0.517020,-2.057264,-2.113712,8.334089,-2.028308,9.886143,-5.581978,-6.079768,9.219698,4.614471,5.637191,-2.263545,-0.760208,-7.958317,-2.069836,5.898968,5.186213,-3.524306,1.022409,-8.558651,-9.855108,8.495113,8.652806,-0.283384,9.426797,7.190275,4.080923,-1.009315,6.710570,2.637255,4.803282,9.201942,-8.187286,4.578320,-2.782329,7.038739,3.097033,6.961502,-1.454758,6.331157,-0.195088,0.093766,-8.968124,4.413121,-1.045454,-5.645065,-2.567794,-6.548771,4.123248,-4.514740,4.456821,8.016337,-6.685812,-5.673281,-2.039599,5.220446,-1.076206,1.893105,-9.909521,-9.324046,4.523110,-2.633792,8.668428,1.277017,-2.983924,-5.631220,0.604062,-5.012399,-5.635423,8.410168,-7.973511,7.440241,1.909778,-3.409310,-5.603246,-2.802769,4.379715,6.941316,-7.042667,2.719722,-3.380485,-6.459771,0.688704,-3.145006,0.393408,1.766486,-4.664632,8.227819,2.282596,4.862658,-4.656871,0.131251,-3.363853,-8.523788,9.807095,-9.463803,3.811415,-5.476290,3.924297,9.892440,-1.394216,8.527663,7.178332,-1.364865,-8.664495,-3.168337], dtype = "float32")#candidate|14282|(132,)|const|float32
const_14283 = relay.const([[-8,-6,1,6,-6,-1,4,7,-2,10,-3,2,4,-2,5,3,-6,-6,10,2,-7,-8,3,-4,8,-8,6,-4,9,5,5,7,-9,-10,-5,7,-9,4,2,-6,2,1,3,6,-5,-6,-9,4,6,-8,-10,4,2,1,5,-6,1,-3,-5,6,10,-2,5,-10,2,3,-5,-1,-4,-2,-10,-6,-6,-5,9,-10,-3,9,-8,10,-7,2,-9,-8,5,-4,8,6,-8,-4,-2,6,-9,-3,6,-9,-6,2,5,-10,9,9,-5,-9,8,10,2,-5,-4,9,2,10,10,5,3,-10,-1,-8,-6,9,-4,3,-8,-6,7,-10,-5,8,4,3,-9,10],[3,-4,8,-2,4,-10,-4,-5,-2,-9,-7,2,-10,-3,-1,-7,-2,3,4,-4,-3,-3,1,-7,4,1,4,-7,10,1,2,6,-7,-5,6,-3,6,-5,5,3,7,3,7,4,-1,-1,-3,8,-5,4,6,10,3,-10,-7,-10,-7,8,4,-3,8,-9,-2,10,-9,1,-2,-7,8,5,-2,-4,9,-5,3,-9,4,2,4,3,4,1,7,-1,7,4,1,8,-7,5,1,-1,-2,10,4,-9,9,6,-8,-5,-5,4,-5,7,5,4,-6,2,-9,-3,-8,-3,2,7,8,-7,-8,-10,5,-7,-9,-8,-7,2,5,-6,8,1,9,-10,-7,10],[9,-10,-7,-7,-9,3,5,9,3,-2,7,10,1,-2,10,4,2,-4,-3,7,-5,-8,-8,-2,-4,-1,-10,-6,-5,-7,-10,2,9,1,6,5,-8,2,10,4,-8,5,-8,-7,7,5,7,7,5,9,6,1,-9,-8,4,-2,-9,-10,-6,-9,1,10,3,-7,7,-8,-1,5,-1,-8,-6,-7,7,-1,4,-8,6,-6,-7,-7,-8,7,3,7,6,-9,8,-9,-5,10,2,6,-9,-7,3,3,9,9,2,6,-3,-2,2,8,2,7,-7,2,-5,-4,-4,-10,-5,-3,-8,6,-3,-4,10,2,-9,5,-4,-2,7,9,-3,4,-1,6,7,3],[-2,7,-7,3,-10,2,7,-6,1,8,6,1,-1,9,1,-8,-6,-5,5,-1,-10,10,-8,-2,2,1,1,9,1,10,9,4,-4,-10,-1,-4,5,-6,10,2,-9,-4,-6,-4,1,6,-3,-7,1,6,10,3,-5,8,9,1,-2,-2,-8,-3,2,10,4,-2,7,-7,9,-4,-10,-10,-2,-9,-6,3,9,2,9,-7,-9,6,-7,5,-6,10,1,5,1,-8,-8,10,6,9,3,-8,6,-8,-8,1,-2,-10,-1,6,10,10,4,-5,3,6,1,10,-8,4,-3,-2,6,-8,6,10,6,3,-1,10,2,1,2,5,-10,-9,-4,6,4,6],[7,-7,-9,5,-9,-5,5,-8,-7,-8,-2,10,8,5,-1,4,-10,-3,1,10,-4,-3,-2,5,-6,8,8,3,3,9,-10,4,-2,-8,8,5,2,1,10,3,9,-3,7,-6,-5,-8,8,4,2,4,-9,-2,-6,-5,10,-2,9,-9,-5,-9,-10,7,1,-5,-5,-3,-8,5,9,-2,-8,-10,-4,-3,2,9,-1,7,10,-6,-2,9,-3,6,2,9,-6,7,7,-9,2,-10,-6,4,2,-1,9,6,4,-4,-4,8,-3,8,-3,-9,-4,-7,-8,6,-2,-6,-7,-5,-8,7,1,10,8,-3,4,7,1,-8,-6,-2,-1,1,1,-7,2,-1]], dtype = "uint64")#candidate|14283|(5, 132)|const|uint64
call_14279 = relay.TupleGetItem(func_2538_call(relay.reshape(var_14280.astype('bool'), [9, 13, 1]), relay.reshape(var_14281.astype('bool'), [9, 13, 6]), relay.reshape(const_14277.astype('float32'), [320,]), relay.reshape(const_14282.astype('float32'), [132,]), relay.reshape(const_14283.astype('uint64'), [330, 2]), ), 3)
call_14284 = relay.TupleGetItem(func_2544_call(relay.reshape(var_14280.astype('bool'), [9, 13, 1]), relay.reshape(var_14281.astype('bool'), [9, 13, 6]), relay.reshape(const_14277.astype('float32'), [320,]), relay.reshape(const_14282.astype('float32'), [132,]), relay.reshape(const_14283.astype('uint64'), [330, 2]), ), 3)
output = relay.Tuple([call_14236,call_14251,call_14256,call_14276,const_14277,call_14279,var_14280,var_14281,const_14282,const_14283,])
output2 = relay.Tuple([call_14237,call_14252,call_14257,call_14278,const_14277,call_14284,var_14280,var_14281,const_14282,const_14283,])
func_14292 = relay.Function([var_14280,var_14281,], output)
mod['func_14292'] = func_14292
mod = relay.transform.InferType()(mod)
mutated_mod['func_14292'] = func_14292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14292_call = mutated_mod.get_global_var('func_14292')
var_14294 = relay.var("var_14294", dtype = "bool", shape = (117,))#candidate|14294|(117,)|var|bool
var_14295 = relay.var("var_14295", dtype = "bool", shape = (702,))#candidate|14295|(702,)|var|bool
call_14293 = func_14292_call(var_14294,var_14295,)
output = call_14293
func_14296 = relay.Function([var_14294,var_14295,], output)
mutated_mod['func_14296'] = func_14296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11878_call = mod.get_global_var('func_11878')
func_11880_call = mutated_mod.get_global_var('func_11880')
call_14351 = func_11878_call()
call_14352 = func_11878_call()
output = call_14351
output2 = call_14352
func_14360 = relay.Function([], output)
mod['func_14360'] = func_14360
mod = relay.transform.InferType()(mod)
mutated_mod['func_14360'] = func_14360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14360_call = mutated_mod.get_global_var('func_14360')
call_14361 = func_14360_call()
output = call_14361
func_14362 = relay.Function([], output)
mutated_mod['func_14362'] = func_14362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12145_call = mod.get_global_var('func_12145')
func_12147_call = mutated_mod.get_global_var('func_12147')
call_14366 = func_12145_call()
call_14367 = func_12145_call()
func_1719_call = mod.get_global_var('func_1719')
func_1723_call = mutated_mod.get_global_var('func_1723')
var_14382 = relay.var("var_14382", dtype = "float32", shape = (3, 44))#candidate|14382|(3, 44)|var|float32
const_14383 = relay.const([[-7],[6],[-7],[7],[-9],[-8],[2],[-4],[5],[2],[3],[9],[-7],[-3],[-4],[-2],[8],[-2],[-2],[-7],[-6],[9],[4],[-10],[9],[3],[7],[1],[8],[1],[-1],[-2],[-4],[7],[3],[-6],[10],[8],[-9],[5],[2],[1],[9],[-1],[6],[-8],[8],[9],[4],[5],[2],[6],[-7],[6],[-5],[-3],[8],[-4],[5],[-3],[-1],[1],[2],[-9],[-8],[4],[6],[-9],[-6],[-10],[-5],[-8],[8],[-1],[9],[-6],[-6],[-8],[-9],[-5],[-1],[-4],[-10],[-1],[-10],[-7],[-3],[-10],[-7],[6],[7],[-4],[10],[-1],[9],[5],[-6],[-9],[6],[3],[1],[2],[3],[9],[-5],[5],[8],[4],[1],[9],[3],[2],[-7],[-8],[-2],[-10],[10],[-9],[6],[-4],[2],[4],[1],[7],[5],[-4],[2],[-10],[8],[1],[-10],[3],[2],[7],[-1],[-2],[4],[-4],[-4],[-7],[-9],[-9],[-8],[9],[8],[7],[2],[2],[-5],[4],[1],[10],[2],[10],[-5],[4],[7],[-4],[-4],[-2],[4],[2],[9],[-1],[-4],[10],[-3],[-3],[-4],[-10],[8],[-4],[9],[2],[2],[6],[3],[-5],[-4],[9],[-1],[5],[1],[10],[9],[-8],[-6],[-3],[-10],[-8],[1],[2],[4],[8],[-4],[-7],[-6],[-1],[-10],[-6],[-1],[-7],[-7],[-1],[7],[1],[5],[-2],[1],[-8],[5],[-9],[10],[1],[1],[9],[10],[-8],[-6],[3],[-10],[9],[-10],[-6],[-1],[5],[2],[10],[-6],[-9],[8],[8],[4],[4],[8],[-3],[-6],[4],[5],[6],[-6],[3],[-4],[9],[-2],[6],[8],[8],[1],[2],[-3],[-8],[9],[-2],[3],[10],[8],[-5],[-4],[4],[-5],[-6],[4],[5],[-9],[-7],[-1],[-9],[6],[-3],[-1],[8],[6],[-4],[8],[-8],[6],[-5],[9],[-8],[-6],[9],[9],[-6],[-1],[-5],[3],[4],[7],[-2],[5],[9],[4],[-4],[4],[1],[8],[-5],[-2],[-5],[3],[-7],[-3],[8],[8],[8],[-9],[-7],[-1],[-6],[-6],[4],[9],[-2],[-4],[3],[-6],[6],[1],[3],[3],[5],[8],[-5],[-4],[5],[9],[3],[-3],[-8],[1],[-4],[4],[-10],[1],[6],[-5],[-8],[-2],[4],[-5],[3],[10],[-4],[2],[-10],[5],[-10],[2],[-6],[3],[1],[-1],[-1],[-3],[9],[5],[3],[-10],[8],[9],[5],[-10],[5],[-6],[6],[-10],[-7],[5],[6],[-2],[5],[-8],[3],[-3],[10],[-7],[-8],[-1],[-8],[3],[-4],[1],[8],[9],[2],[-10],[1],[3],[-8],[2],[-10],[4],[-5],[-10],[-9],[9],[8],[7],[5],[-1],[-1],[4],[-8],[3],[5],[5],[-4],[3],[1],[-6],[-8],[8],[-4],[3],[4],[8],[4],[-5],[-1],[10],[4],[3],[-4],[1],[2],[8],[2],[-8],[-4],[10],[7],[-1],[-10],[-5],[5],[-8],[1],[-8],[10],[10],[9],[-1],[-7],[-9],[-4],[-7],[5],[-1],[-4],[-7],[-4],[-9],[8],[9],[9],[9],[-1],[-8],[3],[-7],[6],[-7],[-4],[9],[7],[-9],[5],[-5],[7],[1],[7],[-5],[2],[5],[3],[-10],[8],[4],[-6],[-9],[1],[3],[6],[-8],[-3],[-3],[9],[-9],[3],[4],[-7],[-9],[-4],[8],[7],[4],[-5],[-3],[6],[-8],[-10],[-1],[8],[10],[3],[-9],[10],[9],[10],[5],[-5],[3],[-5],[-3],[-8],[2],[-1],[-7],[-3],[10],[10],[-8],[7],[6],[5],[3],[8],[1],[4],[6],[6],[-2],[-3],[6],[3],[-3],[5],[-5],[1],[8],[-1],[-5],[10],[-6],[-10],[8],[2],[-3],[-8],[-10],[2],[6],[-7],[10],[2],[-1],[10],[4],[9],[-6],[-2],[-5],[4],[-9],[4],[3],[-5],[7],[-10],[7],[6],[7],[-5],[8],[10],[-5],[8],[-9],[7],[-7],[7],[10],[1],[-3],[4],[-4],[-9],[6],[1],[8],[-8],[6],[-2],[-10],[-2],[1],[-9],[3],[-10],[-2],[8],[3],[-7],[3],[-3],[-9],[-5],[-6],[-9],[7],[3],[1],[1],[-1],[-10],[-5],[9],[8],[-9],[3],[-2],[-10],[9],[-4],[-2],[2],[-1],[9],[-6],[-4],[5],[7],[-7],[1],[-5],[-7],[-9],[2],[5],[-6],[8],[-4],[10],[-10],[-6],[-7],[4],[-5],[8],[-7],[10],[-10],[1],[7],[-9],[-2],[-1],[-4],[2]], dtype = "uint64")#candidate|14383|(660, 1)|const|uint64
call_14381 = relay.TupleGetItem(func_1719_call(relay.reshape(var_14382.astype('float32'), [12, 1, 11]), relay.reshape(const_14383.astype('uint64'), [660,]), ), 2)
call_14384 = relay.TupleGetItem(func_1723_call(relay.reshape(var_14382.astype('float32'), [12, 1, 11]), relay.reshape(const_14383.astype('uint64'), [660,]), ), 2)
bop_14385 = relay.less(call_14366.astype('bool'), const_14383.astype('bool')) # shape=(660, 315)
bop_14388 = relay.less(call_14367.astype('bool'), const_14383.astype('bool')) # shape=(660, 315)
func_9121_call = mod.get_global_var('func_9121')
func_9125_call = mutated_mod.get_global_var('func_9125')
const_14390 = relay.const(0.244448, dtype = "float64")#candidate|14390|()|const|float64
var_14391 = relay.var("var_14391", dtype = "float64", shape = (4, 12))#candidate|14391|(4, 12)|var|float64
call_14389 = relay.TupleGetItem(func_9121_call(relay.reshape(const_14390.astype('float64'), []), relay.reshape(var_14391.astype('float64'), [4, 12, 1]), ), 1)
call_14392 = relay.TupleGetItem(func_9125_call(relay.reshape(const_14390.astype('float64'), []), relay.reshape(var_14391.astype('float64'), [4, 12, 1]), ), 1)
output = relay.Tuple([call_14381,var_14382,bop_14385,call_14389,const_14390,var_14391,])
output2 = relay.Tuple([call_14384,var_14382,bop_14388,call_14392,const_14390,var_14391,])
func_14395 = relay.Function([var_14382,var_14391,], output)
mod['func_14395'] = func_14395
mod = relay.transform.InferType()(mod)
var_14396 = relay.var("var_14396", dtype = "float32", shape = (3, 44))#candidate|14396|(3, 44)|var|float32
var_14397 = relay.var("var_14397", dtype = "float64", shape = (4, 12))#candidate|14397|(4, 12)|var|float64
output = func_14395(var_14396,var_14397,)
func_14398 = relay.Function([var_14396,var_14397,], output)
mutated_mod['func_14398'] = func_14398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13153_call = mod.get_global_var('func_13153')
func_13155_call = mutated_mod.get_global_var('func_13155')
call_14406 = relay.TupleGetItem(func_13153_call(), 0)
call_14407 = relay.TupleGetItem(func_13155_call(), 0)
func_14119_call = mod.get_global_var('func_14119')
func_14121_call = mutated_mod.get_global_var('func_14121')
call_14409 = relay.TupleGetItem(func_14119_call(), 0)
call_14410 = relay.TupleGetItem(func_14121_call(), 0)
uop_14411 = relay.log2(call_14406.astype('float32')) # shape=(2, 15, 11)
uop_14413 = relay.log2(call_14407.astype('float32')) # shape=(2, 15, 11)
output = relay.Tuple([call_14409,uop_14411,])
output2 = relay.Tuple([call_14410,uop_14413,])
func_14415 = relay.Function([], output)
mod['func_14415'] = func_14415
mod = relay.transform.InferType()(mod)
output = func_14415()
func_14416 = relay.Function([], output)
mutated_mod['func_14416'] = func_14416
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14427 = relay.var("var_14427", dtype = "float32", shape = (1, 13, 15))#candidate|14427|(1, 13, 15)|var|float32
uop_14428 = relay.acos(var_14427.astype('float32')) # shape=(1, 13, 15)
output = relay.Tuple([uop_14428,])
output2 = relay.Tuple([uop_14428,])
func_14433 = relay.Function([var_14427,], output)
mod['func_14433'] = func_14433
mod = relay.transform.InferType()(mod)
mutated_mod['func_14433'] = func_14433
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14434 = relay.var("var_14434", dtype = "float32", shape = (1, 13, 15))#candidate|14434|(1, 13, 15)|var|float32
func_14433_call = mutated_mod.get_global_var('func_14433')
call_14435 = func_14433_call(var_14434)
output = call_14435
func_14436 = relay.Function([var_14434], output)
mutated_mod['func_14436'] = func_14436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10683_call = mod.get_global_var('func_10683')
func_10684_call = mutated_mod.get_global_var('func_10684')
call_14438 = relay.TupleGetItem(func_10683_call(), 0)
call_14439 = relay.TupleGetItem(func_10684_call(), 0)
func_3419_call = mod.get_global_var('func_3419')
func_3423_call = mutated_mod.get_global_var('func_3423')
var_14448 = relay.var("var_14448", dtype = "float64", shape = (14,))#candidate|14448|(14,)|var|float64
const_14449 = relay.const([-9.642329,6.206865,4.257405,2.626899,-5.291538,0.204170,1.172571,-5.465448,1.621721,-5.343840,-4.136385,-3.858757,6.049456,-6.571704,-7.171397,1.029756,1.869327,-2.206437,8.327894,5.431611,0.272374,7.397191,9.541049,9.506265,4.418396,-8.936314,-4.733793,3.449135,-3.845491,-0.135463,-6.772547,5.625997,4.768192,-2.543120,5.339681,-0.875802,-5.562284,-1.823853,5.194660,-6.135828,0.250571,8.769748,-2.423847,-0.382778,-0.283224,0.034111,-1.082099,5.281160,-8.130332,-4.138756,0.919263,-8.210227,-9.722532,5.992394,-3.323719,-1.084195,-0.063450,7.562568,-5.566910,-0.569377,9.953021,7.540020,-9.017627,2.593517,-7.891810,4.890735,-2.477585,5.480391,-5.371204,8.279042,9.455080,-3.124264,9.527127,-1.537851,6.571327,-8.642536,-2.988200,-3.292487,-3.300412,9.687112,5.965978,-5.175382,-6.664468,-7.590079,-1.373610,3.123652,-0.745128,-5.469321,6.658807,2.177331,2.953228,2.407707,-9.148096,-7.243607,4.202563,5.730575,-5.751071,7.373647,-4.316334,9.444137,8.709298,-2.452684,3.295469,4.040422,3.184841,1.059733,-1.669274,-0.119073,8.750637,-0.171540,-5.401923,0.535261,6.832726,1.923914,0.341672,3.749883,8.774047,-8.429878,-8.075966,1.088685,-2.808483,-5.353807,-2.890251,2.133452,0.607809,-9.876463,-2.234794,0.319007,-5.465017,0.034801,2.430821,-5.903236,-3.910547,9.968802,-8.267895,-8.132635,-6.034127,-5.483288,9.451577,-3.168991,8.993564,-2.363334,-9.331342,7.811328,-1.937802,-3.913233,4.836508,-6.497460,0.005590,-3.026419,-7.092963,6.379492,2.605040,0.831017,5.247945,-2.360882,8.075381,-1.543312,-4.525654,-4.427444,-7.938354,-9.159811,-4.173923,1.008972,3.633400,3.796480,-0.470011,-8.508683,-0.825381,-2.755987,8.932026,-3.595239,1.737000,-4.726095,2.294436,-1.996738,-8.818707,7.301269,7.700788,-0.810544,7.978792,1.270565,-3.285316,0.743671,9.312427,9.333816,-0.564602,1.120726,-1.791699,8.186559,1.659818,-7.954476,5.495245,-9.270080,-9.127239,9.306496,-6.050203,-7.169400,-1.226558,-9.573174,7.461140,-1.670328,9.718458,-5.077877,3.332193,6.995533,8.160528,-4.682066,-6.786071,-9.504118,-2.034251,-4.076867,-3.498456,6.453360,-7.137899,-6.591590,9.377835,-5.307350,6.398427,2.007297,-4.971423,6.204890,-1.154334,-7.454157,-8.468734,2.159781,-7.935203,2.787176,-9.164667,5.176053,-2.898660,7.476206,-2.396882,1.606613,-8.883326,1.343592,7.181947,-0.519378,-6.912813,-9.963542,1.075346,0.924297,8.027256,-6.177804,-6.744824,2.664516,-3.563204,-1.449125,-6.666872,-8.632670,-3.844967,6.916697,-0.049333,4.215680,4.706234,0.856571,-0.502592,-7.312703,5.696461,9.848487,8.638109,9.985933,0.675300,-8.557231,0.731124,-4.810144,-1.296459,2.702583,-4.580626,-7.433616,3.157419,-9.099331,-3.169742,6.488910,-7.985811,0.168583,1.963271,0.485061,0.799709,-4.950613,-2.593695,-6.999723,1.627356,6.494964,0.951049,4.422505,5.938322,-6.610685,-5.646006,8.997235,-6.939641,-7.220774,1.911328,6.697778,-8.977808,3.222764,-3.823452,4.384995,-6.032654,3.632894,-2.615661,-5.593443,4.914928,-0.785573,-1.100767,-5.859363,-3.131767,3.877563,-1.697180,-3.072850,-5.246226,9.813988,-3.329426,-4.200096,4.239849,-0.831252,-1.343972,8.441624,2.823836,-2.313600], dtype = "float32")#candidate|14449|(320,)|const|float32
call_14447 = relay.TupleGetItem(func_3419_call(relay.reshape(var_14448.astype('float64'), [7, 2, 1]), relay.reshape(const_14449.astype('float32'), [320,]), ), 1)
call_14450 = relay.TupleGetItem(func_3423_call(relay.reshape(var_14448.astype('float64'), [7, 2, 1]), relay.reshape(const_14449.astype('float32'), [320,]), ), 1)
func_13733_call = mod.get_global_var('func_13733')
func_13734_call = mutated_mod.get_global_var('func_13734')
call_14453 = relay.TupleGetItem(func_13733_call(), 0)
call_14454 = relay.TupleGetItem(func_13734_call(), 0)
func_9685_call = mod.get_global_var('func_9685')
func_9688_call = mutated_mod.get_global_var('func_9688')
call_14463 = relay.TupleGetItem(func_9685_call(relay.reshape(const_14449.astype('float32'), [320,])), 3)
call_14464 = relay.TupleGetItem(func_9688_call(relay.reshape(const_14449.astype('float32'), [320,])), 3)
func_10325_call = mod.get_global_var('func_10325')
func_10326_call = mutated_mod.get_global_var('func_10326')
call_14479 = relay.TupleGetItem(func_10325_call(), 0)
call_14480 = relay.TupleGetItem(func_10326_call(), 0)
output = relay.Tuple([call_14438,call_14447,var_14448,const_14449,call_14453,call_14463,call_14479,])
output2 = relay.Tuple([call_14439,call_14450,var_14448,const_14449,call_14454,call_14464,call_14480,])
func_14495 = relay.Function([var_14448,], output)
mod['func_14495'] = func_14495
mod = relay.transform.InferType()(mod)
var_14496 = relay.var("var_14496", dtype = "float64", shape = (14,))#candidate|14496|(14,)|var|float64
output = func_14495(var_14496)
func_14497 = relay.Function([var_14496], output)
mutated_mod['func_14497'] = func_14497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11191_call = mod.get_global_var('func_11191')
func_11192_call = mutated_mod.get_global_var('func_11192')
call_14556 = func_11191_call()
call_14557 = func_11191_call()
func_1524_call = mod.get_global_var('func_1524')
func_1528_call = mutated_mod.get_global_var('func_1528')
var_14575 = relay.var("var_14575", dtype = "uint64", shape = (660,))#candidate|14575|(660,)|var|uint64
var_14576 = relay.var("var_14576", dtype = "float32", shape = (320,))#candidate|14576|(320,)|var|float32
call_14574 = relay.TupleGetItem(func_1524_call(relay.reshape(var_14575.astype('uint64'), [5, 12, 11]), relay.reshape(var_14575.astype('uint64'), [5, 12, 11]), relay.reshape(var_14576.astype('float32'), [1, 320]), ), 0)
call_14577 = relay.TupleGetItem(func_1528_call(relay.reshape(var_14575.astype('uint64'), [5, 12, 11]), relay.reshape(var_14575.astype('uint64'), [5, 12, 11]), relay.reshape(var_14576.astype('float32'), [1, 320]), ), 0)
func_12984_call = mod.get_global_var('func_12984')
func_12986_call = mutated_mod.get_global_var('func_12986')
call_14591 = relay.TupleGetItem(func_12984_call(), 1)
call_14592 = relay.TupleGetItem(func_12986_call(), 1)
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_14610 = relay.TupleGetItem(func_10157_call(), 0)
call_14611 = relay.TupleGetItem(func_10159_call(), 0)
output = relay.Tuple([call_14556,call_14574,var_14575,var_14576,call_14591,call_14610,])
output2 = relay.Tuple([call_14557,call_14577,var_14575,var_14576,call_14592,call_14611,])
func_14620 = relay.Function([var_14575,var_14576,], output)
mod['func_14620'] = func_14620
mod = relay.transform.InferType()(mod)
mutated_mod['func_14620'] = func_14620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14620_call = mutated_mod.get_global_var('func_14620')
var_14622 = relay.var("var_14622", dtype = "uint64", shape = (660,))#candidate|14622|(660,)|var|uint64
var_14623 = relay.var("var_14623", dtype = "float32", shape = (320,))#candidate|14623|(320,)|var|float32
call_14621 = func_14620_call(var_14622,var_14623,)
output = call_14621
func_14624 = relay.Function([var_14622,var_14623,], output)
mutated_mod['func_14624'] = func_14624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10325_call = mod.get_global_var('func_10325')
func_10326_call = mutated_mod.get_global_var('func_10326')
call_14759 = relay.TupleGetItem(func_10325_call(), 0)
call_14760 = relay.TupleGetItem(func_10326_call(), 0)
output = call_14759
output2 = call_14760
func_14778 = relay.Function([], output)
mod['func_14778'] = func_14778
mod = relay.transform.InferType()(mod)
output = func_14778()
func_14779 = relay.Function([], output)
mutated_mod['func_14779'] = func_14779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13595_call = mod.get_global_var('func_13595')
func_13597_call = mutated_mod.get_global_var('func_13597')
call_14809 = func_13595_call()
call_14810 = func_13595_call()
func_13002_call = mod.get_global_var('func_13002')
func_13003_call = mutated_mod.get_global_var('func_13003')
call_14811 = relay.TupleGetItem(func_13002_call(), 0)
call_14812 = relay.TupleGetItem(func_13003_call(), 0)
output = relay.Tuple([call_14809,call_14811,])
output2 = relay.Tuple([call_14810,call_14812,])
func_14827 = relay.Function([], output)
mod['func_14827'] = func_14827
mod = relay.transform.InferType()(mod)
mutated_mod['func_14827'] = func_14827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14827_call = mutated_mod.get_global_var('func_14827')
call_14828 = func_14827_call()
output = call_14828
func_14829 = relay.Function([], output)
mutated_mod['func_14829'] = func_14829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14360_call = mod.get_global_var('func_14360')
func_14362_call = mutated_mod.get_global_var('func_14362')
call_14857 = func_14360_call()
call_14858 = func_14360_call()
output = relay.Tuple([call_14857,])
output2 = relay.Tuple([call_14858,])
func_14860 = relay.Function([], output)
mod['func_14860'] = func_14860
mod = relay.transform.InferType()(mod)
mutated_mod['func_14860'] = func_14860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14860_call = mutated_mod.get_global_var('func_14860')
call_14861 = func_14860_call()
output = call_14861
func_14862 = relay.Function([], output)
mutated_mod['func_14862'] = func_14862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11610_call = mod.get_global_var('func_11610')
func_11612_call = mutated_mod.get_global_var('func_11612')
call_14910 = func_11610_call()
call_14911 = func_11610_call()
func_8298_call = mod.get_global_var('func_8298')
func_8300_call = mutated_mod.get_global_var('func_8300')
const_14915 = relay.const([7.939330,6.194961,7.339386,-7.227873,4.187143,9.117754,-9.214134,-5.722656,8.058061,-4.163657,-8.377319,-1.793057,5.398954,4.174397,-5.996230,8.157070,8.754364,-3.831023,5.244827,4.811728,8.237709,6.703909,9.351088,2.994687,6.679106,2.467215,6.268972,9.335175,-4.818598,8.518629,9.104239,6.960672,5.373590,1.617996,-3.361006,1.047928,4.168306,8.285981,7.911066,5.808217,-7.202787,-2.032412,-6.053378,0.273950,-7.011817,4.936165,3.506834,-7.438189,-1.358414,5.596105,4.174236,0.077147,-9.600103,9.266614,7.410348,-0.471577,-2.433480,4.667071,0.408506,8.902746,-0.051227,1.479324,3.008479,-0.757519,2.664266,-8.640941,6.529669,9.616641,-4.305065,3.729926,3.037194,-3.810275,-8.356219,-1.987613,-7.423355,1.735975,-6.327335,-3.998899,2.141747,7.971538,8.257127,8.485695,8.561912,-2.381419,0.282381,9.916379,3.461670,-6.627215,-8.551414,6.096754,0.030450,9.351209,8.465643,6.475307,-0.714853,9.976877,4.076387,-5.451998,7.030258,-8.742368,-6.587756,7.762018,3.190405,1.084942,-0.370528,-7.329944,-5.574308,8.245593,-1.774960,-5.936236,-4.490856,-7.236412,-5.090605,-3.954269,8.336729,-7.815342,6.593181,0.085666,-0.422665,-2.039632,-9.606243,-5.108349,-7.592972,-6.177786,-1.829723,7.436880,4.051575,-7.476842,1.367464,3.373041,-3.185095,-7.980772,-5.324921,-9.781322,3.134147,2.576646,-0.993662,-6.882854,-0.372931,7.601001,4.136501,6.573816,-3.276807,-6.402962,-1.275320,-4.117302,4.199919,-7.356628,-2.856828,-0.885697,6.349001,7.247376,7.905113,-8.782939,4.898876,9.190827,0.297794,6.747590,-2.400931,9.391535,1.147022,9.532568,-6.601563,-8.445148,9.992121,-3.995755,4.877918,-5.035736,0.610552,-4.242321,-0.294367,3.971657,-2.626525,1.534581,-6.472371,6.887087,-6.959466,1.560958,4.165287,4.499294,-5.391220,8.543645,-9.317428,3.383796,5.273773,-8.164537,4.407634,9.430326,-9.186505,-6.523247,9.834210,-0.233103,2.241004,-9.325017,-8.010170,0.002822,-1.594981,-9.895225,-9.110692,-7.709552,0.657416,8.988155,5.302882,-3.996987,6.145622,-8.222823,-2.394593,-9.809573,-0.150711,-3.355255,-3.319175,-7.832357,7.486749,0.281959,-4.092804,9.101787,-3.259113,-8.817975,7.762841,3.052045,0.546940,8.480770,7.676586,8.027133,-3.564805,-5.345819,2.042339,0.594525,4.686103,-7.400084,6.166300,9.872738,-8.054419,3.407856,-3.623499,-1.992573,-7.365839,5.719200,7.335063,-5.582371,1.547780,2.321803,7.855549,8.134675,4.418220,-4.276834,1.635413,3.182796,2.851176,8.545086,2.423871,7.694870,3.967040,5.946407,-7.745336,-7.108156,-2.858699,-3.150503,6.158257,-7.682998,-8.726233,4.819958,-6.575395,7.619288,1.948955,7.981212,6.438145,-3.850424,-3.861546,5.626444,4.562515,-8.117081,3.978123,2.920081,-7.342940,-4.717252,-2.846573,-4.690336,-0.478472,-4.075167,-0.438045,-0.378124,5.433517,-4.121238,2.054134,-2.981867,3.731694,-9.131218,5.884175,4.654566,-3.840974,-1.344797,9.339637,5.045360,7.965139,6.084599,-8.272042,6.366815,8.656792,2.310609,1.268407,9.387599,-9.009842,-7.916093,-4.777258,2.608088,9.656979,3.739341,-3.156229,-0.573696,3.580895,8.688143,8.304019,2.951055,-1.983252,3.702950,-0.199851,-8.468002,5.071843,-5.097855,9.473754,-5.206222,-6.587392,1.793163,-2.205262,-3.770144,-4.516137,7.523473,-4.082774,-2.376793,8.296414,-3.350661,-2.960590,-4.898176,7.790161,4.548658,-3.349051,3.452729,-3.652896,9.713671,-7.599625,-8.544583,8.615285,5.741250,-6.760934,-9.754454,0.565265,4.264316,-2.219407,0.909589,-3.021537,-0.034387,-0.769942,4.676025,-0.189325,-1.586327,-8.453600,7.428689,-6.948760,6.380558,-2.332976,2.780474,6.893462,-4.573815,-3.779415,1.958496,-5.375380,-6.930313,-2.846169,5.081787,-9.736065,1.791536,-6.164975,5.657206,2.127805,0.035921,-4.859451,-9.519408,8.015356,5.981476,-8.486498,1.335445,-7.255204,-0.878909,9.777262,-7.579957,5.526774,2.318276,-7.471060,-1.254385,0.496899,-3.541573], dtype = "float64")#candidate|14915|(392,)|const|float64
call_14914 = func_8298_call(relay.reshape(const_14915.astype('float64'), [4, 14, 7]))
call_14916 = func_8298_call(relay.reshape(const_14915.astype('float64'), [4, 14, 7]))
output = relay.Tuple([call_14910,call_14914,const_14915,])
output2 = relay.Tuple([call_14911,call_14916,const_14915,])
func_14969 = relay.Function([], output)
mod['func_14969'] = func_14969
mod = relay.transform.InferType()(mod)
mutated_mod['func_14969'] = func_14969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14969_call = mutated_mod.get_global_var('func_14969')
call_14970 = func_14969_call()
output = call_14970
func_14971 = relay.Function([], output)
mutated_mod['func_14971'] = func_14971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13153_call = mod.get_global_var('func_13153')
func_13155_call = mutated_mod.get_global_var('func_13155')
call_14977 = relay.TupleGetItem(func_13153_call(), 0)
call_14978 = relay.TupleGetItem(func_13155_call(), 0)
func_13733_call = mod.get_global_var('func_13733')
func_13734_call = mutated_mod.get_global_var('func_13734')
call_14995 = relay.TupleGetItem(func_13733_call(), 0)
call_14996 = relay.TupleGetItem(func_13734_call(), 0)
func_10760_call = mod.get_global_var('func_10760')
func_10762_call = mutated_mod.get_global_var('func_10762')
const_15014 = relay.const([-8.897381,-4.489140,-1.267200,-9.917189,9.660437,-5.371177,5.200801,2.643751,6.000750,-1.248670,-1.607639,-5.864373,5.304339,5.428354,-6.458322,8.285469,-4.822601,9.856423,1.991040,8.325227,2.433225,-1.616750,-2.546159,-1.478262,-9.801324,-0.043550,5.626780,7.978431,2.800292,7.973353,6.480489,-1.200352,8.718187,-9.219276,9.020003,0.920117,-8.417136,4.396016,9.849285,-1.512235,-4.653809,-0.112388,1.132755,5.276322,-0.530274,9.466820,8.986391,1.146108,6.548700,-3.401258,1.743565,8.025678,6.598997,5.168205,-5.982102,-2.274000,-3.143920,9.898860,1.050325,-6.780508,8.169973,5.555854,6.592010,2.788386,-1.027385,-6.683636,0.747796,0.372156,-7.229414,2.927432,2.602481,-7.662021,-6.004466,6.738679,-0.572662,9.682073,2.757198,-5.119132,7.892184,4.384060,6.526808,-4.775659,7.661412,8.817383,-0.950762,7.286441,8.967859,9.418542,4.024631,5.172504,-4.807898,0.565630,7.200481,-6.748949,-4.512614,-7.156504,4.755762,-2.002045,9.429531,9.891318,3.342147,9.489409,-2.378280,-6.140692,3.449782,3.587600,1.002266,-2.514948,-0.793808,9.079749,-1.772628,1.904058,-4.241784,0.730659,4.035485,1.303525,0.621915,3.349709,6.835337,3.113106,1.829782,-4.018630,0.124102,4.380769,-5.460450,-5.090814,4.346546,-6.609365,-8.166310,0.475113,-4.761676,-4.331378,4.036668,7.471716,5.104105,4.707398,6.647448,0.999946,-4.174705,0.344619,-5.661246,-8.794998,5.544645,0.376441,-3.658197,1.632936,-7.054242,-3.112300,-4.651206,-7.709198,-3.075842,-0.484929,-8.140390,-1.125406,0.700744,8.944777,-8.306566,5.262274,-2.011498,2.782389,8.041774,-4.813167,-1.565406,8.709717,-9.792999,-9.540591,8.406977,8.183942,9.171341,0.368689,4.563877,-2.009398,-4.727609,9.190552,-0.110130,1.787740,0.405677,5.800274,-2.342314,-8.624497,5.575473,2.292217,-0.732424,-4.502096,-9.279776,-7.168113,-0.081616,9.606987,-3.535739,8.545600,2.480212,-9.735157,-3.757308,-7.227702,-7.295911,-4.848528,-3.700549,-2.007954,-5.476607,-6.259054,-3.380181,-8.398787,3.198922,3.623347,-6.864669,-1.201339,8.541414,-3.907095,2.901142,-1.645207,-4.307887,5.144059,-3.395146,8.485155,-8.488949,-2.808333,-0.821901,5.282258,-6.352120,3.765726,7.691042,9.785687,-4.360284,9.078892,-4.775122,1.218338,-7.322332,0.960982,-6.512946,0.866973,-4.920843,-6.292495,-9.278845,-7.820212,-6.650336,7.698843,-4.667217,7.159734,-7.117159,-3.353116,-4.631062,9.445970,-0.820986,-4.186943,8.295343,0.407627,6.324119,-1.789240,8.974883,-4.128093,-5.785507,9.514617,-4.121400,7.687299,6.477927,-1.865525,8.098431,-1.942623,-0.934505,3.493418,-0.522475,-4.482410,-1.325945,6.678553,8.783952,6.561265,2.243768,-3.451735,4.577425,6.559925,6.142340,1.731843,3.360027,-8.510998,-9.911961,-4.220275,-2.437315,-1.402299,2.844280,-9.809167], dtype = "float64")#candidate|15014|(280,)|const|float64
call_15013 = relay.TupleGetItem(func_10760_call(relay.reshape(const_15014.astype('float64'), [280,])), 1)
call_15015 = relay.TupleGetItem(func_10762_call(relay.reshape(const_15014.astype('float64'), [280,])), 1)
output = relay.Tuple([call_14977,call_14995,call_15013,const_15014,])
output2 = relay.Tuple([call_14978,call_14996,call_15015,const_15014,])
func_15016 = relay.Function([], output)
mod['func_15016'] = func_15016
mod = relay.transform.InferType()(mod)
mutated_mod['func_15016'] = func_15016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15016_call = mutated_mod.get_global_var('func_15016')
call_15017 = func_15016_call()
output = call_15017
func_15018 = relay.Function([], output)
mutated_mod['func_15018'] = func_15018
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15130 = relay.var("var_15130", dtype = "float64", shape = ())#candidate|15130|()|var|float64
const_15131 = relay.const([[[8.540435,6.229989,-6.334802,-3.604446,8.306969],[2.539987,2.245251,-4.386561,-4.472978,5.143693],[-6.642022,-1.351415,7.855638,8.843021,5.738030],[-6.616144,-4.840742,0.967043,-8.381630,1.715803],[-2.464611,-5.820830,-3.502297,-4.999530,-0.365615],[3.709855,-5.256248,5.755827,-4.610605,-8.008900],[5.417465,-8.767087,-4.494768,6.208830,5.840393],[3.570492,7.404869,1.383162,-7.454650,-5.425433],[8.968254,8.391466,3.086196,9.123917,8.186602],[-4.672771,-6.493586,-3.349734,-7.298538,9.292679],[6.121984,0.684516,-1.170433,-4.111981,-3.549019]],[[-1.778313,-1.129179,8.913163,-2.420318,5.536152],[0.467334,-1.620220,-0.263061,-6.773975,-7.202065],[-4.091733,-4.205392,-6.975385,-5.740709,0.167786],[4.522160,8.615685,2.532209,-9.948513,9.376827],[0.426825,5.899318,6.083285,6.389673,-3.940836],[0.963030,1.489205,-4.230839,1.123285,-4.706604],[6.368980,-8.633991,2.880067,-5.247406,1.546553],[-7.812326,-8.516097,-7.085771,3.190117,2.607682],[-3.689130,1.350718,7.867869,9.216015,-2.903443],[9.206146,-6.747459,-1.890079,-6.870701,1.322710],[8.015433,-7.157143,3.399314,0.449386,-7.805772]],[[-6.664401,9.650473,-4.300259,6.480162,0.357619],[0.777757,7.532086,-1.121465,-2.418973,-4.354121],[-6.654627,6.460771,1.277810,-7.757032,1.221689],[-4.469389,1.956931,2.775303,-8.673932,6.215190],[0.581175,-8.667103,-2.293293,-4.390704,3.685644],[-5.603136,-6.491327,2.473784,-8.368272,-0.625763],[-1.481057,4.995864,4.967613,-9.641228,6.135980],[9.212513,-9.012019,-4.933755,2.797323,9.014034],[9.550317,-9.636500,5.549314,-4.229690,5.733790],[-1.324448,2.666160,2.221283,-2.019586,-5.726937],[-7.603939,-9.036680,7.115758,6.185125,-6.833203]],[[-6.385147,3.290800,0.608501,-0.263427,-6.654007],[0.514716,6.715028,2.126958,3.409307,-5.544562],[0.530297,8.304744,-3.834593,-4.949621,3.704014],[-2.170266,1.173215,6.297453,1.650280,-2.537885],[0.681269,-9.914451,-7.437360,-1.194432,9.638176],[5.591823,8.985976,7.737253,4.614888,5.305446],[-5.267040,-8.731451,6.936270,-6.216997,1.453663],[3.034344,-0.062988,-0.301721,9.091571,-8.092594],[8.615388,6.621810,0.457362,-7.628685,8.702125],[1.378337,-0.031550,5.170908,6.548450,-0.140063],[-9.515952,-3.951266,3.858579,8.197956,8.118315]],[[9.186494,1.070839,1.107637,8.173324,7.158863],[7.087989,-0.013095,2.438920,-6.194188,-0.650490],[2.216127,-2.749374,6.297089,-9.766953,-1.795461],[9.005634,2.049156,-5.442877,2.547918,-9.992333],[-2.593977,8.081790,0.459163,-3.775727,-1.357338],[-0.836125,5.551328,5.043179,-8.745847,4.034147],[2.330349,1.971536,8.045510,9.510892,7.881788],[-3.844987,4.996022,3.926869,-0.321001,-1.585183],[-7.690129,-2.397396,9.466131,-2.272840,-8.221424],[-1.388147,-5.071847,-7.973305,-7.750780,-5.091363],[2.708312,9.539546,3.112527,-4.741990,0.288617]],[[-1.097921,1.633298,0.805881,-7.834686,1.160719],[-7.687245,-1.043383,0.483022,-0.983006,-6.173679],[9.467416,7.867578,-6.513951,3.073437,-7.029355],[-3.879646,-5.051554,-5.613168,-6.737714,-3.997664],[9.524048,-0.290360,0.870468,-0.491070,9.440057],[9.811299,-3.270591,4.272253,1.521286,9.804921],[0.505374,-7.322843,-9.709318,-8.041182,2.530533],[-6.037970,1.241360,-4.073645,-5.049520,-1.972454],[5.957406,-4.496695,6.699065,-5.250947,4.053286],[-5.263440,9.310961,-0.264307,8.275624,0.036520],[8.859843,4.262644,-0.843522,-2.769200,-8.664589]],[[-4.094251,-0.686039,-1.524409,-7.179136,-6.723819],[-4.522575,9.824553,4.546554,5.710561,-6.000934],[5.677869,-5.717132,-7.422200,-5.552637,8.058547],[2.509407,-2.180355,8.543954,6.324875,5.014017],[0.986294,6.525231,-2.805965,-1.671998,5.967396],[-4.781956,0.046627,-3.127718,3.692157,-1.852915],[1.047276,-9.022861,3.730968,-6.061050,7.086727],[-2.578828,-5.416360,6.645634,-4.335668,-5.939825],[-8.477297,-7.633329,-6.161701,3.788038,1.833971],[-3.347223,-2.848624,-6.170892,-4.112977,-1.493480],[-4.229437,-1.725432,-5.263513,8.762439,-9.889665]],[[1.967904,-4.763745,-5.164078,-2.775853,-1.860551],[9.383098,-6.777683,6.906779,3.568367,-2.738050],[-5.003132,-8.416976,0.130268,-8.468603,2.962253],[-0.983887,-4.360136,-7.250453,5.337229,-7.924189],[-8.062087,8.583825,3.925842,1.389269,-2.783919],[8.987748,-8.604942,-1.665354,-4.795622,6.175583],[3.211430,-4.279237,-9.627901,-0.414175,4.422473],[-2.178619,-3.379731,2.224585,-4.132538,-0.504011],[-6.910462,3.517097,0.229084,-8.586611,2.631653],[8.760298,0.168781,-5.991997,-1.405830,-2.375522],[5.187902,8.144797,-5.241660,-8.023038,6.605622]],[[1.470151,-3.162231,-5.899035,-0.174431,0.556480],[-0.865593,-4.523151,6.585470,-2.489232,7.631932],[6.467864,6.526129,-9.462401,9.105375,-0.684996],[9.236372,-9.517056,7.858300,9.330287,3.787451],[7.610375,6.873625,-6.130575,-5.551419,-1.175394],[9.263817,-0.977501,-1.164724,-5.220293,2.093880],[-5.618359,-2.953579,-9.435317,-9.002048,-9.271352],[6.138325,3.573574,0.667533,3.511469,-5.018891],[-0.267724,7.334919,-4.723442,7.466293,-2.211015],[-1.030111,-7.625740,3.152866,-1.958722,-6.752971],[-1.577071,-0.363158,6.551637,3.167109,6.771213]]], dtype = "float64")#candidate|15131|(9, 11, 5)|const|float64
bop_15132 = relay.divide(var_15130.astype('float64'), const_15131.astype('float64')) # shape=(9, 11, 5)
func_12743_call = mod.get_global_var('func_12743')
func_12746_call = mutated_mod.get_global_var('func_12746')
const_15140 = relay.const([True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,False,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,False], dtype = "bool")#candidate|15140|(1176,)|const|bool
call_15139 = relay.TupleGetItem(func_12743_call(relay.reshape(const_15140.astype('bool'), [7, 14, 12]), relay.reshape(const_15140.astype('bool'), [7, 14, 12]), ), 0)
call_15141 = relay.TupleGetItem(func_12746_call(relay.reshape(const_15140.astype('bool'), [7, 14, 12]), relay.reshape(const_15140.astype('bool'), [7, 14, 12]), ), 0)
output = relay.Tuple([bop_15132,call_15139,const_15140,])
output2 = relay.Tuple([bop_15132,call_15141,const_15140,])
func_15158 = relay.Function([var_15130,], output)
mod['func_15158'] = func_15158
mod = relay.transform.InferType()(mod)
mutated_mod['func_15158'] = func_15158
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15159 = relay.var("var_15159", dtype = "float64", shape = ())#candidate|15159|()|var|float64
func_15158_call = mutated_mod.get_global_var('func_15158')
call_15160 = func_15158_call(var_15159)
output = call_15160
func_15161 = relay.Function([var_15159], output)
mutated_mod['func_15161'] = func_15161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9974_call = mod.get_global_var('func_9974')
func_9975_call = mutated_mod.get_global_var('func_9975')
call_15171 = func_9974_call()
call_15172 = func_9974_call()
output = call_15171
output2 = call_15172
func_15177 = relay.Function([], output)
mod['func_15177'] = func_15177
mod = relay.transform.InferType()(mod)
mutated_mod['func_15177'] = func_15177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15177_call = mutated_mod.get_global_var('func_15177')
call_15178 = func_15177_call()
output = call_15178
func_15179 = relay.Function([], output)
mutated_mod['func_15179'] = func_15179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12424_call = mod.get_global_var('func_12424')
func_12425_call = mutated_mod.get_global_var('func_12425')
call_15245 = func_12424_call()
call_15246 = func_12424_call()
output = call_15245
output2 = call_15246
func_15247 = relay.Function([], output)
mod['func_15247'] = func_15247
mod = relay.transform.InferType()(mod)
output = func_15247()
func_15248 = relay.Function([], output)
mutated_mod['func_15248'] = func_15248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11849_call = mod.get_global_var('func_11849')
func_11851_call = mutated_mod.get_global_var('func_11851')
call_15343 = relay.TupleGetItem(func_11849_call(), 1)
call_15344 = relay.TupleGetItem(func_11851_call(), 1)
output = relay.Tuple([call_15343,])
output2 = relay.Tuple([call_15344,])
func_15345 = relay.Function([], output)
mod['func_15345'] = func_15345
mod = relay.transform.InferType()(mod)
output = func_15345()
func_15346 = relay.Function([], output)
mutated_mod['func_15346'] = func_15346
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15016_call = mod.get_global_var('func_15016')
func_15018_call = mutated_mod.get_global_var('func_15018')
call_15403 = relay.TupleGetItem(func_15016_call(), 3)
call_15404 = relay.TupleGetItem(func_15018_call(), 3)
func_11299_call = mod.get_global_var('func_11299')
func_11301_call = mutated_mod.get_global_var('func_11301')
call_15407 = func_11299_call()
call_15408 = func_11299_call()
output = relay.Tuple([call_15403,call_15407,])
output2 = relay.Tuple([call_15404,call_15408,])
func_15414 = relay.Function([], output)
mod['func_15414'] = func_15414
mod = relay.transform.InferType()(mod)
mutated_mod['func_15414'] = func_15414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15414_call = mutated_mod.get_global_var('func_15414')
call_15415 = func_15414_call()
output = call_15415
func_15416 = relay.Function([], output)
mutated_mod['func_15416'] = func_15416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11040_call = mod.get_global_var('func_11040')
func_11042_call = mutated_mod.get_global_var('func_11042')
call_15494 = func_11040_call()
call_15495 = func_11040_call()
func_10157_call = mod.get_global_var('func_10157')
func_10159_call = mutated_mod.get_global_var('func_10159')
call_15504 = relay.TupleGetItem(func_10157_call(), 0)
call_15505 = relay.TupleGetItem(func_10159_call(), 0)
output = relay.Tuple([call_15494,call_15504,])
output2 = relay.Tuple([call_15495,call_15505,])
func_15522 = relay.Function([], output)
mod['func_15522'] = func_15522
mod = relay.transform.InferType()(mod)
output = func_15522()
func_15523 = relay.Function([], output)
mutated_mod['func_15523'] = func_15523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15016_call = mod.get_global_var('func_15016')
func_15018_call = mutated_mod.get_global_var('func_15018')
call_15621 = relay.TupleGetItem(func_15016_call(), 0)
call_15622 = relay.TupleGetItem(func_15018_call(), 0)
output = relay.Tuple([call_15621,])
output2 = relay.Tuple([call_15622,])
func_15627 = relay.Function([], output)
mod['func_15627'] = func_15627
mod = relay.transform.InferType()(mod)
mutated_mod['func_15627'] = func_15627
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15627_call = mutated_mod.get_global_var('func_15627')
call_15628 = func_15627_call()
output = call_15628
func_15629 = relay.Function([], output)
mutated_mod['func_15629'] = func_15629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12630_call = mod.get_global_var('func_12630')
func_12632_call = mutated_mod.get_global_var('func_12632')
call_15672 = relay.TupleGetItem(func_12630_call(), 0)
call_15673 = relay.TupleGetItem(func_12632_call(), 0)
output = relay.Tuple([call_15672,])
output2 = relay.Tuple([call_15673,])
func_15678 = relay.Function([], output)
mod['func_15678'] = func_15678
mod = relay.transform.InferType()(mod)
mutated_mod['func_15678'] = func_15678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15678_call = mutated_mod.get_global_var('func_15678')
call_15679 = func_15678_call()
output = call_15679
func_15680 = relay.Function([], output)
mutated_mod['func_15680'] = func_15680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14827_call = mod.get_global_var('func_14827')
func_14829_call = mutated_mod.get_global_var('func_14829')
call_15696 = relay.TupleGetItem(func_14827_call(), 1)
call_15697 = relay.TupleGetItem(func_14829_call(), 1)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_15710 = func_11516_call()
call_15711 = func_11516_call()
func_13153_call = mod.get_global_var('func_13153')
func_13155_call = mutated_mod.get_global_var('func_13155')
call_15722 = relay.TupleGetItem(func_13153_call(), 0)
call_15723 = relay.TupleGetItem(func_13155_call(), 0)
output = relay.Tuple([call_15696,call_15710,call_15722,])
output2 = relay.Tuple([call_15697,call_15711,call_15723,])
func_15740 = relay.Function([], output)
mod['func_15740'] = func_15740
mod = relay.transform.InferType()(mod)
mutated_mod['func_15740'] = func_15740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15740_call = mutated_mod.get_global_var('func_15740')
call_15741 = func_15740_call()
output = call_15741
func_15742 = relay.Function([], output)
mutated_mod['func_15742'] = func_15742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10035_call = mod.get_global_var('func_10035')
func_10037_call = mutated_mod.get_global_var('func_10037')
call_15773 = func_10035_call()
call_15774 = func_10035_call()
output = call_15773
output2 = call_15774
func_15788 = relay.Function([], output)
mod['func_15788'] = func_15788
mod = relay.transform.InferType()(mod)
output = func_15788()
func_15789 = relay.Function([], output)
mutated_mod['func_15789'] = func_15789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_15826 = func_11516_call()
call_15827 = func_11516_call()
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
const_15853 = relay.const([9.410850,9.890505,-8.492070,4.046828,-4.068924,9.896901,4.576095,2.162236,2.253463,-8.131459,-5.910637,-9.052892,-4.001096,-5.582639,2.138966,4.443172,-4.234909,-2.158588,-2.706335,-6.784327,6.247818,-9.683492,-4.532559,-2.430888,0.135335,-0.033747,-7.498408,8.171577,6.760557,-0.624659,7.326667,8.914912,8.099148,7.632129,2.299869,-9.143257,1.602049,4.548668,0.157977,9.640611], dtype = "float32")#candidate|15853|(40,)|const|float32
call_15852 = relay.TupleGetItem(func_1886_call(relay.reshape(const_15853.astype('float32'), [10, 1, 4])), 0)
call_15854 = relay.TupleGetItem(func_1888_call(relay.reshape(const_15853.astype('float32'), [10, 1, 4])), 0)
output = relay.Tuple([call_15826,call_15852,const_15853,])
output2 = relay.Tuple([call_15827,call_15854,const_15853,])
func_15860 = relay.Function([], output)
mod['func_15860'] = func_15860
mod = relay.transform.InferType()(mod)
output = func_15860()
func_15861 = relay.Function([], output)
mutated_mod['func_15861'] = func_15861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_15901 = relay.TupleGetItem(func_8014_call(), 0)
call_15902 = relay.TupleGetItem(func_8016_call(), 0)
output = call_15901
output2 = call_15902
func_15915 = relay.Function([], output)
mod['func_15915'] = func_15915
mod = relay.transform.InferType()(mod)
output = func_15915()
func_15916 = relay.Function([], output)
mutated_mod['func_15916'] = func_15916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13294_call = mod.get_global_var('func_13294')
func_13296_call = mutated_mod.get_global_var('func_13296')
call_15935 = relay.TupleGetItem(func_13294_call(), 1)
call_15936 = relay.TupleGetItem(func_13296_call(), 1)
output = relay.Tuple([call_15935,])
output2 = relay.Tuple([call_15936,])
func_15937 = relay.Function([], output)
mod['func_15937'] = func_15937
mod = relay.transform.InferType()(mod)
mutated_mod['func_15937'] = func_15937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15937_call = mutated_mod.get_global_var('func_15937')
call_15938 = func_15937_call()
output = call_15938
func_15939 = relay.Function([], output)
mutated_mod['func_15939'] = func_15939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13417_call = mod.get_global_var('func_13417')
func_13419_call = mutated_mod.get_global_var('func_13419')
call_15992 = relay.TupleGetItem(func_13417_call(), 1)
call_15993 = relay.TupleGetItem(func_13419_call(), 1)
output = relay.Tuple([call_15992,])
output2 = relay.Tuple([call_15993,])
func_16021 = relay.Function([], output)
mod['func_16021'] = func_16021
mod = relay.transform.InferType()(mod)
output = func_16021()
func_16022 = relay.Function([], output)
mutated_mod['func_16022'] = func_16022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15247_call = mod.get_global_var('func_15247')
func_15248_call = mutated_mod.get_global_var('func_15248')
call_16080 = func_15247_call()
call_16081 = func_15247_call()
func_10165_call = mod.get_global_var('func_10165')
func_10167_call = mutated_mod.get_global_var('func_10167')
call_16083 = relay.TupleGetItem(func_10165_call(), 0)
call_16084 = relay.TupleGetItem(func_10167_call(), 0)
func_4843_call = mod.get_global_var('func_4843')
func_4846_call = mutated_mod.get_global_var('func_4846')
var_16104 = relay.var("var_16104", dtype = "float64", shape = (3, 300))#candidate|16104|(3, 300)|var|float64
call_16103 = func_4843_call(relay.reshape(var_16104.astype('float64'), [10, 10, 9]), relay.reshape(var_16104.astype('float64'), [10, 10, 9]), )
call_16105 = func_4843_call(relay.reshape(var_16104.astype('float64'), [10, 10, 9]), relay.reshape(var_16104.astype('float64'), [10, 10, 9]), )
output = relay.Tuple([call_16080,call_16083,call_16103,var_16104,])
output2 = relay.Tuple([call_16081,call_16084,call_16105,var_16104,])
func_16109 = relay.Function([var_16104,], output)
mod['func_16109'] = func_16109
mod = relay.transform.InferType()(mod)
var_16110 = relay.var("var_16110", dtype = "float64", shape = (3, 300))#candidate|16110|(3, 300)|var|float64
output = func_16109(var_16110)
func_16111 = relay.Function([var_16110], output)
mutated_mod['func_16111'] = func_16111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11040_call = mod.get_global_var('func_11040')
func_11042_call = mutated_mod.get_global_var('func_11042')
call_16137 = func_11040_call()
call_16138 = func_11040_call()
func_12503_call = mod.get_global_var('func_12503')
func_12506_call = mutated_mod.get_global_var('func_12506')
const_16175 = relay.const([False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True], dtype = "bool")#candidate|16175|(117,)|const|bool
const_16176 = relay.const([False,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,False,True], dtype = "bool")#candidate|16176|(702,)|const|bool
call_16174 = relay.TupleGetItem(func_12503_call(relay.reshape(const_16175.astype('bool'), [117,]), relay.reshape(const_16176.astype('bool'), [702,]), ), 0)
call_16177 = relay.TupleGetItem(func_12506_call(relay.reshape(const_16175.astype('bool'), [117,]), relay.reshape(const_16176.astype('bool'), [702,]), ), 0)
output = relay.Tuple([call_16137,call_16174,const_16175,const_16176,])
output2 = relay.Tuple([call_16138,call_16177,const_16175,const_16176,])
func_16180 = relay.Function([], output)
mod['func_16180'] = func_16180
mod = relay.transform.InferType()(mod)
mutated_mod['func_16180'] = func_16180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16180_call = mutated_mod.get_global_var('func_16180')
call_16181 = func_16180_call()
output = call_16181
func_16182 = relay.Function([], output)
mutated_mod['func_16182'] = func_16182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15345_call = mod.get_global_var('func_15345')
func_15346_call = mutated_mod.get_global_var('func_15346')
call_16217 = relay.TupleGetItem(func_15345_call(), 0)
call_16218 = relay.TupleGetItem(func_15346_call(), 0)
func_8421_call = mod.get_global_var('func_8421')
func_8427_call = mutated_mod.get_global_var('func_8427')
var_16224 = relay.var("var_16224", dtype = "float32", shape = (240,))#candidate|16224|(240,)|var|float32
const_16225 = relay.const([-3.236677,-8.289839,-0.685218,3.310109,-5.127925,-3.446367,-9.963438,7.913029,-2.955682,-3.991986,0.858988,4.652329,-0.730525,6.576557,9.955460,-6.340768,-5.059333,6.632825,2.696537,6.272960,9.679418,1.708189,-1.863642,-2.751251,9.820730,1.525686,5.550390,4.627176,-6.208865,6.062614,5.863259,4.082501,-6.731700,-7.186368,4.211594,-3.120244,9.827397,-3.646303,-4.261988,-2.502447,-0.194802,-7.650728,0.832363,9.907288,0.246679,7.553821,-9.950976,-8.011250,1.345327,1.372187,8.413437,0.457304,3.685560,-1.767578,-3.974258,3.557584,-6.006272,-9.257923,6.515301,2.176175,-5.139522,5.343250,7.670403,-9.432704,-0.696274,-8.758405,5.041943,7.690710,1.516016,-2.871472,-9.356107,-3.671537,-8.756423,-8.327492,7.067492,-4.904783,-7.103283,-1.219722,2.714636,7.403744,-3.983313,1.633709,8.637578,-3.729535,-2.482127,9.120269,8.998989,-5.240674,-9.633001,0.942170,-7.887180,-4.927344,-4.745034,4.280781,1.365374,8.296851,-1.953719,7.301727,1.762927,-5.734330,-3.443426,7.734854,-2.371552,0.440203,-3.000843,-5.215782,-2.386438,-8.880192,0.668034,5.434045,-8.710280,1.964853,6.037619,-5.328496,-6.659320,9.919534,-9.943781,-8.092172,-6.812282,-1.242396,2.667240,8.265400,5.878875,-3.848136,7.260277,1.203465,-9.859247,-3.028335,1.207259,1.892100,-0.255904,-0.118483,7.301134,8.570659,1.329639,-3.466285,-0.447239,-0.100607,9.939591,-9.720602,-9.819791,-1.254508,-1.337543,6.703708,-2.286104,-9.588683,4.363926,0.972171,7.423775,-1.766000,-0.116792,4.572753,-0.171301,-7.400230,-1.235059,9.133880,-2.347875,-6.803046,-1.343078,-9.430821,-7.411224,2.864706,-3.605114,-0.966720,5.084726,-1.305560,2.847948,-1.817531,0.272663,-0.203580,-5.645788,1.981930,2.081657,2.883028,1.993234,-1.135482,-9.574648,4.641156,4.207358,2.160063,-9.229560,-2.777910,3.763691,3.233082,-1.961839,2.539603,0.127242,8.877239,-9.315128,7.915802,9.276523,8.523844,1.984868,-4.383653,-5.565705,-0.403637,6.394836,-9.100249,7.870455,2.385859,5.537702,-1.497158,9.134857,-7.910658,5.677121,1.874315,3.525927,-5.308558,5.894961,5.274356,-8.977102,-5.245719,5.137409,1.542570,3.892430,-1.669010,3.272212,8.486824,-1.907751,-3.052162,7.478210,-8.805642,-2.525596,-2.025214,0.477990,9.388662,5.472418,7.100086,-4.577238,3.608818,-5.450032,0.283642,6.654385,-0.131629,-3.002861,5.615664,3.260968,-7.509747,-0.273499,6.385381,6.434126,-7.769329,9.916937,4.459978,-3.656419,3.340102,-8.028998,-6.020645,3.490989,7.302833,9.194985,-6.195422,9.834720,-2.515748,6.420041,7.921040,-5.372626,5.806897,-9.477617,8.839240,8.771803,0.184567,7.180730,4.524321,-1.143314,-6.714520,6.018367,-5.097484,-0.681170,7.426145,8.133036,-8.905674,-3.561197,4.377356,-8.870293,1.190966,5.529526,4.274233,-9.212739,2.400137,0.244116,-5.067056,-6.781947,9.751435,5.419064,-8.230923,-9.231764,-9.470738,-8.461226,2.543975,-5.678475,8.464781,0.402503,9.946066,7.096955,-5.894447,-6.065717,-6.161217,-5.592319,9.108282,-3.824443,-1.984706,-1.327188,3.496017,-6.489773,2.508403,2.996214,-8.406450,8.282341,-4.788753,-6.113315,-9.487872,0.422504,-3.999655,-0.274299,3.436575,5.305177,9.390290,-1.381699,0.758087], dtype = "float32")#candidate|16225|(320,)|const|float32
const_16226 = relay.const([1.266269,9.727319,5.965867,0.661821,7.413495,8.028430,-4.521950,-4.171044,3.133241,8.859738,0.880503,0.188706,1.954538,-3.271010,7.620165,2.288559,3.126606,-1.826918,-7.383852,-5.514346,7.346687,-6.468355,8.094787,-5.292276,-9.448327,-5.238133,9.114630,6.097824,-4.476337,5.814797,-0.833952,-3.737153,-1.645538,-5.209990,-8.716101,-8.201290,-0.989935,-0.707554,8.520443,2.076363], dtype = "float32")#candidate|16226|(40,)|const|float32
call_16223 = relay.TupleGetItem(func_8421_call(relay.reshape(var_16224.astype('float32'), [240,]), relay.reshape(const_16225.astype('float32'), [320,]), relay.reshape(const_16226.astype('float32'), [40,]), relay.reshape(const_16225.astype('float32'), [40, 8]), ), 0)
call_16227 = relay.TupleGetItem(func_8427_call(relay.reshape(var_16224.astype('float32'), [240,]), relay.reshape(const_16225.astype('float32'), [320,]), relay.reshape(const_16226.astype('float32'), [40,]), relay.reshape(const_16225.astype('float32'), [40, 8]), ), 0)
output = relay.Tuple([call_16217,call_16223,var_16224,const_16225,const_16226,])
output2 = relay.Tuple([call_16218,call_16227,var_16224,const_16225,const_16226,])
func_16276 = relay.Function([var_16224,], output)
mod['func_16276'] = func_16276
mod = relay.transform.InferType()(mod)
mutated_mod['func_16276'] = func_16276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16277 = relay.var("var_16277", dtype = "float32", shape = (240,))#candidate|16277|(240,)|var|float32
func_16276_call = mutated_mod.get_global_var('func_16276')
call_16278 = func_16276_call(var_16277)
output = call_16278
func_16279 = relay.Function([var_16277], output)
mutated_mod['func_16279'] = func_16279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14195_call = mod.get_global_var('func_14195')
func_14197_call = mutated_mod.get_global_var('func_14197')
call_16332 = func_14195_call()
call_16333 = func_14195_call()
output = call_16332
output2 = call_16333
func_16334 = relay.Function([], output)
mod['func_16334'] = func_16334
mod = relay.transform.InferType()(mod)
output = func_16334()
func_16335 = relay.Function([], output)
mutated_mod['func_16335'] = func_16335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11849_call = mod.get_global_var('func_11849')
func_11851_call = mutated_mod.get_global_var('func_11851')
call_16352 = relay.TupleGetItem(func_11849_call(), 1)
call_16353 = relay.TupleGetItem(func_11851_call(), 1)
func_12503_call = mod.get_global_var('func_12503')
func_12506_call = mutated_mod.get_global_var('func_12506')
const_16361 = relay.const([True,False,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,True,True,False,False,False,True], dtype = "bool")#candidate|16361|(117,)|const|bool
const_16362 = relay.const([[False,False,False,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True]], dtype = "bool")#candidate|16362|(1, 702)|const|bool
call_16360 = relay.TupleGetItem(func_12503_call(relay.reshape(const_16361.astype('bool'), [117,]), relay.reshape(const_16362.astype('bool'), [702,]), ), 1)
call_16363 = relay.TupleGetItem(func_12506_call(relay.reshape(const_16361.astype('bool'), [117,]), relay.reshape(const_16362.astype('bool'), [702,]), ), 1)
output = relay.Tuple([call_16352,call_16360,const_16361,const_16362,])
output2 = relay.Tuple([call_16353,call_16363,const_16361,const_16362,])
func_16364 = relay.Function([], output)
mod['func_16364'] = func_16364
mod = relay.transform.InferType()(mod)
output = func_16364()
func_16365 = relay.Function([], output)
mutated_mod['func_16365'] = func_16365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11991_call = mod.get_global_var('func_11991')
func_11992_call = mutated_mod.get_global_var('func_11992')
call_16403 = func_11991_call()
call_16404 = func_11991_call()
func_16334_call = mod.get_global_var('func_16334')
func_16335_call = mutated_mod.get_global_var('func_16335')
call_16405 = func_16334_call()
call_16406 = func_16334_call()
output = relay.Tuple([call_16403,call_16405,])
output2 = relay.Tuple([call_16404,call_16406,])
func_16411 = relay.Function([], output)
mod['func_16411'] = func_16411
mod = relay.transform.InferType()(mod)
mutated_mod['func_16411'] = func_16411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16411_call = mutated_mod.get_global_var('func_16411')
call_16412 = func_16411_call()
output = call_16412
func_16413 = relay.Function([], output)
mutated_mod['func_16413'] = func_16413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15678_call = mod.get_global_var('func_15678')
func_15680_call = mutated_mod.get_global_var('func_15680')
call_16414 = relay.TupleGetItem(func_15678_call(), 0)
call_16415 = relay.TupleGetItem(func_15680_call(), 0)
func_15627_call = mod.get_global_var('func_15627')
func_15629_call = mutated_mod.get_global_var('func_15629')
call_16431 = relay.TupleGetItem(func_15627_call(), 0)
call_16432 = relay.TupleGetItem(func_15629_call(), 0)
func_13903_call = mod.get_global_var('func_13903')
func_13904_call = mutated_mod.get_global_var('func_13904')
call_16438 = relay.TupleGetItem(func_13903_call(), 0)
call_16439 = relay.TupleGetItem(func_13904_call(), 0)
output = relay.Tuple([call_16414,call_16431,call_16438,])
output2 = relay.Tuple([call_16415,call_16432,call_16439,])
func_16443 = relay.Function([], output)
mod['func_16443'] = func_16443
mod = relay.transform.InferType()(mod)
mutated_mod['func_16443'] = func_16443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16443_call = mutated_mod.get_global_var('func_16443')
call_16444 = func_16443_call()
output = call_16444
func_16445 = relay.Function([], output)
mutated_mod['func_16445'] = func_16445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_16521 = relay.TupleGetItem(func_8014_call(), 0)
call_16522 = relay.TupleGetItem(func_8016_call(), 0)
output = relay.Tuple([call_16521,])
output2 = relay.Tuple([call_16522,])
func_16525 = relay.Function([], output)
mod['func_16525'] = func_16525
mod = relay.transform.InferType()(mod)
mutated_mod['func_16525'] = func_16525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16525_call = mutated_mod.get_global_var('func_16525')
call_16526 = func_16525_call()
output = call_16526
func_16527 = relay.Function([], output)
mutated_mod['func_16527'] = func_16527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15915_call = mod.get_global_var('func_15915')
func_15916_call = mutated_mod.get_global_var('func_15916')
call_16535 = func_15915_call()
call_16536 = func_15915_call()
output = call_16535
output2 = call_16536
func_16542 = relay.Function([], output)
mod['func_16542'] = func_16542
mod = relay.transform.InferType()(mod)
output = func_16542()
func_16543 = relay.Function([], output)
mutated_mod['func_16543'] = func_16543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16411_call = mod.get_global_var('func_16411')
func_16413_call = mutated_mod.get_global_var('func_16413')
call_16547 = relay.TupleGetItem(func_16411_call(), 1)
call_16548 = relay.TupleGetItem(func_16413_call(), 1)
output = relay.Tuple([call_16547,])
output2 = relay.Tuple([call_16548,])
func_16553 = relay.Function([], output)
mod['func_16553'] = func_16553
mod = relay.transform.InferType()(mod)
mutated_mod['func_16553'] = func_16553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16553_call = mutated_mod.get_global_var('func_16553')
call_16554 = func_16553_call()
output = call_16554
func_16555 = relay.Function([], output)
mutated_mod['func_16555'] = func_16555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11122_call = mod.get_global_var('func_11122')
func_11123_call = mutated_mod.get_global_var('func_11123')
call_16565 = func_11122_call()
call_16566 = func_11122_call()
func_14778_call = mod.get_global_var('func_14778')
func_14779_call = mutated_mod.get_global_var('func_14779')
call_16567 = func_14778_call()
call_16568 = func_14778_call()
func_6489_call = mod.get_global_var('func_6489')
func_6492_call = mutated_mod.get_global_var('func_6492')
const_16572 = relay.const([-3,3,-3,-8,7,8,-10,4,-3,7,2,-8,-9,-3,-9,1,3,10,2,-10,-9,-1,-1,-3,3,-2,9,4,-3,5,9,-5,-1,-8,-4,-1,7,2,-8,4,-4,-8,4,-4,-1,2,4,-2,-2,-7,-1,9,-2,-5,5,-2,6,3,2,-1,-6,-2,-8,-7,-7,7,5,-3,7,9,-7,-1,1,-5,9,5,-6,-6,-3,5,9,5,7,3,6,-6,-3,8,-8,6,-8,5,-9,-10,-3,-2,6,6,-5,-7,-1,6,9,7,-4,9,3,7,4,-6,-10,-1,6,-10,-8,-2,2,-4,-9,-10,-3,6,-2,10,8,-5,4,7,-3,1,-7,-2,-2,-10,7,-5,-1,-8,3,9,6,2,-9,-2,-9,8,7,-3,-6,1,6,-6,6,-2,-4,2,6,-1,-6,-9,-5,9,7,-2,-6,8,8,1,-6,5,-5,-9,5,-5,-1,6,-3,2,8,5,-9,-7,5,-1,2,-2,-4,-5,-8,-2,9,9,-4,4,-6,-7,1,2,-4,8,8,1,10,-3,-8,-1,4,9,-2,-7,3,3,-9,-10,7,-7,10,9,5,8,8,10,-9,9,3,10,-1,10,8,-1,1,-10,-7,9,-2,3,6,3,6,7,-7,7,-9,-7,8,2,7,8,-10,4,-6,3,4,-7,7,10,-10,3,4,8,8,-1,1,-9,-8,4,-3,6,-2,-6,9,-2,-10,2,-5,-6,-8,9,8,-2,-2,10,3,3,-3,4,-2,4,-1,8,5,-8,10,-4,-7,5,-3,7,5,3,6,9,-4,-3,-9,1,-2,-7,-8,3,9,7,4,-10,-1,-4,-10,8,-8,-9,10,1,8,-6,-10,2,-6,-3,-10,-9,6,9,-10,10,-7,-5,10,1,-5,-4,8,4,2,6,10,4,-9,-2,1,-7,4,5,9,1,3,-8,-1,6,-10,7,6,-6,6,3,1,-8,-3,8,-9,7,4,4,8,9,10,9,-9,2,4,-5,-7,-1,-5,4,8,5,-7,-7,9,-6,-4,-7,-2,8,-4,3,5,-4,3,-4,9,4,10,-2,7,-8,-3,-2,3,10,-5,9,-9,2,-10,4,6,7,9,-5,-7,7,-7,6,-1,7,1,7,8,-3,-6,10,-5,7,6,10,4,-5,6,-1,8,-6,6,1,5,-4,1,2,-3,-9,3,-4,7,-2,-9,-4,2,7,3,2,2,-6,2,-8,-1,5,8,-2,7,10,6,-4,-3,-6,1,-2,-6,5,-8,-2,-1,4,-6,-4,2,-8,9,-9,-3,9,-3,-6,-1,8,5,8,-8,-3,1,-5,5,-1,7,9,7,5,-10,10,1,1,-7,-2,-3,7,-6,7,8,-8,-10,-5,6,6,1,7,1,10,9,2,8,-6,-4,6,10,6,-10,4,3,3,-5,9,-8,-5,2,-9,-7,-3,-5,-2,2,5,-1,9,9,9,4,-2,-7,-1,4,-9,2,-1,-2,4,-1,5,7,5,6,2,1,4,2,-9,3,7,-2,4,1,6,-6,5,5,-1,-3,-2,-10,-4,-2,-9,1,-2,-6,4,6,-1,-1,8,-6,8,4,6,6,6,-3,3,-3,-8,3,6,4,-4,4,2,10,9,-9,10,5,3,3,3,-3,6,-10,5,-10,8,10,-1,-9,-4,5,6,-2,-7,7,2,8,-5,-10,4,-9,5,-4,10,9,4,10,4,-8,-6,1,-4,7,9,2,-9,-8,2,3,7,-8,5,-8,-1,-2,-3,6,-3,-9,-2,8,1,6,-9,-7,-2,-5,4,-8,2,-3,-6,-4,-2,3,-3,-5,-10,10,-1,-4,-4,10,4,5,9,-5,-7,-3,-2,-4,1,1,-2,9,-10,6,3,3,5,7,6,-8,1,-3,-2,-9,-6,-4,-3,-2,7,-10,4,-2,-1,-3,-1,9,4,6,-9,-9,-7,-3,-6,-7,3,-5,-1,7,6,-1,3,-10,4,-3,10,7,-2,8,-7,3,2,-10,3,-7,7,7,-1,-7,2,9,-9,-9,-9,3,4,8,1,1,5,-4,-9,2,-7,-7,6,-1,4,-10,-7,-1,-6,-8,-6,3,-6,-4,8,-5,5,-4,-5,10,4,-2,-2,3,1,6,-8,-1,-6,9,2,-10,3,-10,8,-10,9,-5,-7,10,8,7,7,-10,4,-8,3,-3,-4,7,-4,-4,10,-5,-8,5,3,3,2,4,5,2,1,-4,-10,-7,-9,7,-2,4,-9,5,-3,-3,-2,-2,-8,4,-10,6,-1,-4,6,8,6,-10,-3,7,5,-2,7,-5,8,6,-10,-8,5,-1,-7,-3,-3,8,-9,-1,-6,-1,-6,-10,6,2,8,6,6,-8,-8,-4,3,-6,-8,7,1,5,-4,4,2,-5,8,8,9,-6,7,8,3,-2,-3,3,7,-3,-4,3,3,-8,9,4,10,-7,-10,-8,-8,-4,-1,5,6,1,3,7,1,-6,9,-10,-1,-7,1,6,6,-10,-6,7,3,3,3,3,-5,-4,-10,-3,-3,-2,6,6,7,-10,-3,6,-4,-3,10,1,-6,10,-1,-6,5,-1,-5,4,-2,-6,3,2,-4,-6,-2,10,4,-5,4,1,1,-2,-8,-10,-3,5,2,-3,4,-1,-6,4,2,5,1,7,8,8,-8,-6,7,-8,9,-5,1,-9,6,7,5,4,-9,-7,2,1,-6,-2,-8,-1,-2,-2,-2,-1,6,-6,1,-6,1,-5,1,-5,-5,-1,7,-2,10,-1,-6,-1,-2,3,7,2,-5,2,-5,4,-2,-2,6,-8,-9,9,3,8,-6,-7,-2,-2,-7,4,1,-3,4,-4,1,-9,2,6,9,-1,4,-10,8,-5,10,1,1,8,1,-6,-5,3,-4,-5,2,9,-5,-4,3,-9,1,6,-4,-7,-6,7,9,-1,10,7,-3,8,5,10,-3,3,-9,-8,-1,9,-10,-1,8,-6,-7,10,7,-7,-4,-10], dtype = "int8")#candidate|16572|(1125,)|const|int8
call_16571 = func_6489_call(relay.reshape(const_16572.astype('int8'), [15, 15, 5]))
call_16573 = func_6489_call(relay.reshape(const_16572.astype('int8'), [15, 15, 5]))
uop_16593 = relay.cos(const_16572.astype('float32')) # shape=(1125,)
output = relay.Tuple([call_16565,call_16567,call_16571,uop_16593,])
output2 = relay.Tuple([call_16566,call_16568,call_16573,uop_16593,])
func_16603 = relay.Function([], output)
mod['func_16603'] = func_16603
mod = relay.transform.InferType()(mod)
output = func_16603()
func_16604 = relay.Function([], output)
mutated_mod['func_16604'] = func_16604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14360_call = mod.get_global_var('func_14360')
func_14362_call = mutated_mod.get_global_var('func_14362')
call_16620 = func_14360_call()
call_16621 = func_14360_call()
func_11809_call = mod.get_global_var('func_11809')
func_11810_call = mutated_mod.get_global_var('func_11810')
call_16624 = relay.TupleGetItem(func_11809_call(), 0)
call_16625 = relay.TupleGetItem(func_11810_call(), 0)
output = relay.Tuple([call_16620,call_16624,])
output2 = relay.Tuple([call_16621,call_16625,])
func_16633 = relay.Function([], output)
mod['func_16633'] = func_16633
mod = relay.transform.InferType()(mod)
mutated_mod['func_16633'] = func_16633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16633_call = mutated_mod.get_global_var('func_16633')
call_16634 = func_16633_call()
output = call_16634
func_16635 = relay.Function([], output)
mutated_mod['func_16635'] = func_16635
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8014_call = mod.get_global_var('func_8014')
func_8016_call = mutated_mod.get_global_var('func_8016')
call_16662 = relay.TupleGetItem(func_8014_call(), 0)
call_16663 = relay.TupleGetItem(func_8016_call(), 0)
func_15740_call = mod.get_global_var('func_15740')
func_15742_call = mutated_mod.get_global_var('func_15742')
call_16681 = relay.TupleGetItem(func_15740_call(), 2)
call_16682 = relay.TupleGetItem(func_15742_call(), 2)
output = relay.Tuple([call_16662,call_16681,])
output2 = relay.Tuple([call_16663,call_16682,])
func_16683 = relay.Function([], output)
mod['func_16683'] = func_16683
mod = relay.transform.InferType()(mod)
mutated_mod['func_16683'] = func_16683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16683_call = mutated_mod.get_global_var('func_16683')
call_16684 = func_16683_call()
output = call_16684
func_16685 = relay.Function([], output)
mutated_mod['func_16685'] = func_16685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13294_call = mod.get_global_var('func_13294')
func_13296_call = mutated_mod.get_global_var('func_13296')
call_16688 = relay.TupleGetItem(func_13294_call(), 0)
call_16689 = relay.TupleGetItem(func_13296_call(), 0)
output = relay.Tuple([call_16688,])
output2 = relay.Tuple([call_16689,])
func_16690 = relay.Function([], output)
mod['func_16690'] = func_16690
mod = relay.transform.InferType()(mod)
mutated_mod['func_16690'] = func_16690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16690_call = mutated_mod.get_global_var('func_16690')
call_16691 = func_16690_call()
output = call_16691
func_16692 = relay.Function([], output)
mutated_mod['func_16692'] = func_16692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13417_call = mod.get_global_var('func_13417')
func_13419_call = mutated_mod.get_global_var('func_13419')
call_16734 = relay.TupleGetItem(func_13417_call(), 1)
call_16735 = relay.TupleGetItem(func_13419_call(), 1)
output = relay.Tuple([call_16734,])
output2 = relay.Tuple([call_16735,])
func_16741 = relay.Function([], output)
mod['func_16741'] = func_16741
mod = relay.transform.InferType()(mod)
output = func_16741()
func_16742 = relay.Function([], output)
mutated_mod['func_16742'] = func_16742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14174_call = mod.get_global_var('func_14174')
func_14175_call = mutated_mod.get_global_var('func_14175')
call_16746 = relay.TupleGetItem(func_14174_call(), 0)
call_16747 = relay.TupleGetItem(func_14175_call(), 0)
output = call_16746
output2 = call_16747
func_16749 = relay.Function([], output)
mod['func_16749'] = func_16749
mod = relay.transform.InferType()(mod)
mutated_mod['func_16749'] = func_16749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16749_call = mutated_mod.get_global_var('func_16749')
call_16750 = func_16749_call()
output = call_16750
func_16751 = relay.Function([], output)
mutated_mod['func_16751'] = func_16751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13002_call = mod.get_global_var('func_13002')
func_13003_call = mutated_mod.get_global_var('func_13003')
call_16818 = relay.TupleGetItem(func_13002_call(), 0)
call_16819 = relay.TupleGetItem(func_13003_call(), 0)
func_11809_call = mod.get_global_var('func_11809')
func_11810_call = mutated_mod.get_global_var('func_11810')
call_16826 = relay.TupleGetItem(func_11809_call(), 1)
call_16827 = relay.TupleGetItem(func_11810_call(), 1)
output = relay.Tuple([call_16818,call_16826,])
output2 = relay.Tuple([call_16819,call_16827,])
func_16835 = relay.Function([], output)
mod['func_16835'] = func_16835
mod = relay.transform.InferType()(mod)
output = func_16835()
func_16836 = relay.Function([], output)
mutated_mod['func_16836'] = func_16836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13640_call = mod.get_global_var('func_13640')
func_13642_call = mutated_mod.get_global_var('func_13642')
call_16848 = relay.TupleGetItem(func_13640_call(), 1)
call_16849 = relay.TupleGetItem(func_13642_call(), 1)
output = call_16848
output2 = call_16849
func_16875 = relay.Function([], output)
mod['func_16875'] = func_16875
mod = relay.transform.InferType()(mod)
mutated_mod['func_16875'] = func_16875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16875_call = mutated_mod.get_global_var('func_16875')
call_16876 = func_16875_call()
output = call_16876
func_16877 = relay.Function([], output)
mutated_mod['func_16877'] = func_16877
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16886 = relay.var("var_16886", dtype = "uint32", shape = (9, 14, 13))#candidate|16886|(9, 14, 13)|var|uint32
var_16887 = relay.var("var_16887", dtype = "uint32", shape = (9, 14, 13))#candidate|16887|(9, 14, 13)|var|uint32
bop_16888 = relay.less_equal(var_16886.astype('bool'), relay.reshape(var_16887.astype('bool'), relay.shape_of(var_16886))) # shape=(9, 14, 13)
output = bop_16888
output2 = bop_16888
func_16892 = relay.Function([var_16886,var_16887,], output)
mod['func_16892'] = func_16892
mod = relay.transform.InferType()(mod)
mutated_mod['func_16892'] = func_16892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16892_call = mutated_mod.get_global_var('func_16892')
var_16894 = relay.var("var_16894", dtype = "uint32", shape = (9, 14, 13))#candidate|16894|(9, 14, 13)|var|uint32
var_16895 = relay.var("var_16895", dtype = "uint32", shape = (9, 14, 13))#candidate|16895|(9, 14, 13)|var|uint32
call_16893 = func_16892_call(var_16894,var_16895,)
output = call_16893
func_16896 = relay.Function([var_16894,var_16895,], output)
mutated_mod['func_16896'] = func_16896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11516_call = mod.get_global_var('func_11516')
func_11517_call = mutated_mod.get_global_var('func_11517')
call_16917 = func_11516_call()
call_16918 = func_11516_call()
output = relay.Tuple([call_16917,])
output2 = relay.Tuple([call_16918,])
func_16937 = relay.Function([], output)
mod['func_16937'] = func_16937
mod = relay.transform.InferType()(mod)
output = func_16937()
func_16938 = relay.Function([], output)
mutated_mod['func_16938'] = func_16938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15247_call = mod.get_global_var('func_15247')
func_15248_call = mutated_mod.get_global_var('func_15248')
call_16983 = func_15247_call()
call_16984 = func_15247_call()
func_8421_call = mod.get_global_var('func_8421')
func_8427_call = mutated_mod.get_global_var('func_8427')
var_16993 = relay.var("var_16993", dtype = "float32", shape = (240,))#candidate|16993|(240,)|var|float32
var_16994 = relay.var("var_16994", dtype = "float32", shape = (320,))#candidate|16994|(320,)|var|float32
const_16995 = relay.const([[-0.343379],[6.382923],[-5.093581],[0.689931],[-8.653605],[2.899258],[4.436288],[0.336506],[-2.053896],[-6.627319],[-0.598596],[-9.212333],[-3.583496],[3.711216],[8.807989],[-6.093001],[-3.452008],[6.392292],[-8.957489],[1.511435],[-8.092672],[-4.868934],[7.981837],[-0.362902],[5.182203],[-1.246506],[5.521641],[6.308708],[-8.964418],[5.291272],[2.226379],[1.097251],[1.272519],[-0.124067],[2.942987],[9.527086],[0.910975],[1.920920],[3.049832],[-6.338575]], dtype = "float32")#candidate|16995|(40, 1)|const|float32
call_16992 = relay.TupleGetItem(func_8421_call(relay.reshape(var_16993.astype('float32'), [240,]), relay.reshape(var_16994.astype('float32'), [320,]), relay.reshape(const_16995.astype('float32'), [40,]), relay.reshape(var_16994.astype('float32'), [40, 8]), ), 6)
call_16996 = relay.TupleGetItem(func_8427_call(relay.reshape(var_16993.astype('float32'), [240,]), relay.reshape(var_16994.astype('float32'), [320,]), relay.reshape(const_16995.astype('float32'), [40,]), relay.reshape(var_16994.astype('float32'), [40, 8]), ), 6)
func_15414_call = mod.get_global_var('func_15414')
func_15416_call = mutated_mod.get_global_var('func_15416')
call_17008 = relay.TupleGetItem(func_15414_call(), 0)
call_17009 = relay.TupleGetItem(func_15416_call(), 0)
func_16633_call = mod.get_global_var('func_16633')
func_16635_call = mutated_mod.get_global_var('func_16635')
call_17013 = relay.TupleGetItem(func_16633_call(), 0)
call_17014 = relay.TupleGetItem(func_16635_call(), 0)
output = relay.Tuple([call_16983,call_16992,var_16993,var_16994,const_16995,call_17008,call_17013,])
output2 = relay.Tuple([call_16984,call_16996,var_16993,var_16994,const_16995,call_17009,call_17014,])
func_17020 = relay.Function([var_16993,var_16994,], output)
mod['func_17020'] = func_17020
mod = relay.transform.InferType()(mod)
var_17021 = relay.var("var_17021", dtype = "float32", shape = (240,))#candidate|17021|(240,)|var|float32
var_17022 = relay.var("var_17022", dtype = "float32", shape = (320,))#candidate|17022|(320,)|var|float32
output = func_17020(var_17021,var_17022,)
func_17023 = relay.Function([var_17021,var_17022,], output)
mutated_mod['func_17023'] = func_17023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11771_call = mod.get_global_var('func_11771')
func_11773_call = mutated_mod.get_global_var('func_11773')
call_17063 = relay.TupleGetItem(func_11771_call(), 0)
call_17064 = relay.TupleGetItem(func_11773_call(), 0)
output = call_17063
output2 = call_17064
func_17077 = relay.Function([], output)
mod['func_17077'] = func_17077
mod = relay.transform.InferType()(mod)
output = func_17077()
func_17078 = relay.Function([], output)
mutated_mod['func_17078'] = func_17078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13640_call = mod.get_global_var('func_13640')
func_13642_call = mutated_mod.get_global_var('func_13642')
call_17090 = relay.TupleGetItem(func_13640_call(), 0)
call_17091 = relay.TupleGetItem(func_13642_call(), 0)
output = call_17090
output2 = call_17091
func_17092 = relay.Function([], output)
mod['func_17092'] = func_17092
mod = relay.transform.InferType()(mod)
mutated_mod['func_17092'] = func_17092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17092_call = mutated_mod.get_global_var('func_17092')
call_17093 = func_17092_call()
output = call_17093
func_17094 = relay.Function([], output)
mutated_mod['func_17094'] = func_17094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17123 = relay.var("var_17123", dtype = "uint8", shape = (13, 13, 4))#candidate|17123|(13, 13, 4)|var|uint8
var_17124 = relay.var("var_17124", dtype = "uint8", shape = (13, 13, 4))#candidate|17124|(13, 13, 4)|var|uint8
bop_17125 = relay.logical_xor(var_17123.astype('uint8'), relay.reshape(var_17124.astype('uint8'), relay.shape_of(var_17123))) # shape=(13, 13, 4)
func_16603_call = mod.get_global_var('func_16603')
func_16604_call = mutated_mod.get_global_var('func_16604')
call_17128 = relay.TupleGetItem(func_16603_call(), 1)
call_17129 = relay.TupleGetItem(func_16604_call(), 1)
output = relay.Tuple([bop_17125,call_17128,])
output2 = relay.Tuple([bop_17125,call_17129,])
func_17134 = relay.Function([var_17123,var_17124,], output)
mod['func_17134'] = func_17134
mod = relay.transform.InferType()(mod)
mutated_mod['func_17134'] = func_17134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17134_call = mutated_mod.get_global_var('func_17134')
var_17136 = relay.var("var_17136", dtype = "uint8", shape = (13, 13, 4))#candidate|17136|(13, 13, 4)|var|uint8
var_17137 = relay.var("var_17137", dtype = "uint8", shape = (13, 13, 4))#candidate|17137|(13, 13, 4)|var|uint8
call_17135 = func_17134_call(var_17136,var_17137,)
output = call_17135
func_17138 = relay.Function([var_17136,var_17137,], output)
mutated_mod['func_17138'] = func_17138
mutated_mod = relay.transform.InferType()(mutated_mod)
const_17140 = relay.const([[[-4.007774,8.897636,3.355699,-1.586236,-9.444782,0.809426,6.039905,-1.427310,3.910191,5.119055,-7.826293,7.691493,9.157837],[-3.517759,3.841664,-2.127338,7.448485,5.902342,0.684480,-7.201258,-1.665002,-9.593886,0.282467,0.013409,4.566928,-5.133660],[-9.834976,-7.530873,4.065052,-6.521491,-9.491688,1.947928,-5.742052,-7.535065,-0.255245,-7.700534,-1.402605,-2.463202,4.088639],[7.163787,8.744166,-0.970990,1.468041,7.931372,8.707214,-1.466963,-2.176554,8.539986,-5.271530,-6.885686,-6.855995,-5.129496],[-4.142620,-2.965537,-6.102737,-1.618601,-3.413179,3.672789,6.189766,-5.106615,-1.855328,6.587646,-0.746186,-7.147271,-8.436921],[1.466535,6.432270,-3.196882,0.642981,7.699832,-2.918561,2.227330,-7.607841,-0.602200,0.471739,-2.188153,2.435617,-4.609990],[-6.720231,5.102947,-2.778481,-9.461505,-7.006895,6.829263,4.304778,8.053613,-7.725850,-0.476177,9.522747,0.685888,-5.890897],[-3.618818,3.282908,4.136051,2.805813,-3.634653,-6.332533,7.187616,9.827604,-0.469714,7.134103,-8.291973,-8.465412,-0.464550],[-6.055726,-0.369275,1.404995,-9.637769,1.735756,5.471503,-2.636187,-4.118790,-9.669041,2.534808,-4.750724,-3.369316,6.064200],[-1.178376,-7.283693,9.275219,-6.693484,2.274991,9.724195,-2.095231,1.398766,1.048715,5.783318,-8.805111,-2.981418,-5.702188],[6.340759,-3.680157,2.586319,-5.213426,-1.052582,-7.262987,5.724838,-8.356368,-7.280894,-0.971487,-2.254247,9.659711,6.773289],[2.803925,-4.335969,2.132836,6.325711,-3.965317,-3.989774,-2.266044,3.462139,6.626061,-6.241454,9.237916,-1.490167,-3.253322]]], dtype = "float32")#candidate|17140|(1, 12, 13)|const|float32
var_17141 = relay.var("var_17141", dtype = "float32", shape = (5, 12, 13))#candidate|17141|(5, 12, 13)|var|float32
bop_17142 = relay.mod(const_17140.astype('float32'), var_17141.astype('float32')) # shape=(5, 12, 13)
func_16603_call = mod.get_global_var('func_16603')
func_16604_call = mutated_mod.get_global_var('func_16604')
call_17145 = relay.TupleGetItem(func_16603_call(), 1)
call_17146 = relay.TupleGetItem(func_16604_call(), 1)
output = relay.Tuple([bop_17142,call_17145,])
output2 = relay.Tuple([bop_17142,call_17146,])
func_17156 = relay.Function([var_17141,], output)
mod['func_17156'] = func_17156
mod = relay.transform.InferType()(mod)
var_17157 = relay.var("var_17157", dtype = "float32", shape = (5, 12, 13))#candidate|17157|(5, 12, 13)|var|float32
output = func_17156(var_17157)
func_17158 = relay.Function([var_17157], output)
mutated_mod['func_17158'] = func_17158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15937_call = mod.get_global_var('func_15937')
func_15939_call = mutated_mod.get_global_var('func_15939')
call_17160 = relay.TupleGetItem(func_15937_call(), 0)
call_17161 = relay.TupleGetItem(func_15939_call(), 0)
output = relay.Tuple([call_17160,])
output2 = relay.Tuple([call_17161,])
func_17174 = relay.Function([], output)
mod['func_17174'] = func_17174
mod = relay.transform.InferType()(mod)
output = func_17174()
func_17175 = relay.Function([], output)
mutated_mod['func_17175'] = func_17175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_17181 = relay.TupleGetItem(func_9014_call(), 2)
call_17182 = relay.TupleGetItem(func_9016_call(), 2)
func_14969_call = mod.get_global_var('func_14969')
func_14971_call = mutated_mod.get_global_var('func_14971')
call_17185 = relay.TupleGetItem(func_14969_call(), 2)
call_17186 = relay.TupleGetItem(func_14971_call(), 2)
func_9014_call = mod.get_global_var('func_9014')
func_9016_call = mutated_mod.get_global_var('func_9016')
call_17198 = relay.TupleGetItem(func_9014_call(), 0)
call_17199 = relay.TupleGetItem(func_9016_call(), 0)
output = relay.Tuple([call_17181,call_17185,call_17198,])
output2 = relay.Tuple([call_17182,call_17186,call_17199,])
func_17260 = relay.Function([], output)
mod['func_17260'] = func_17260
mod = relay.transform.InferType()(mod)
mutated_mod['func_17260'] = func_17260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17260_call = mutated_mod.get_global_var('func_17260')
call_17261 = func_17260_call()
output = call_17261
func_17262 = relay.Function([], output)
mutated_mod['func_17262'] = func_17262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17174_call = mod.get_global_var('func_17174')
func_17175_call = mutated_mod.get_global_var('func_17175')
call_17271 = relay.TupleGetItem(func_17174_call(), 0)
call_17272 = relay.TupleGetItem(func_17175_call(), 0)
output = relay.Tuple([call_17271,])
output2 = relay.Tuple([call_17272,])
func_17275 = relay.Function([], output)
mod['func_17275'] = func_17275
mod = relay.transform.InferType()(mod)
mutated_mod['func_17275'] = func_17275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17275_call = mutated_mod.get_global_var('func_17275')
call_17276 = func_17275_call()
output = call_17276
func_17277 = relay.Function([], output)
mutated_mod['func_17277'] = func_17277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16411_call = mod.get_global_var('func_16411')
func_16413_call = mutated_mod.get_global_var('func_16413')
call_17306 = relay.TupleGetItem(func_16411_call(), 1)
call_17307 = relay.TupleGetItem(func_16413_call(), 1)
output = relay.Tuple([call_17306,])
output2 = relay.Tuple([call_17307,])
func_17312 = relay.Function([], output)
mod['func_17312'] = func_17312
mod = relay.transform.InferType()(mod)
output = func_17312()
func_17313 = relay.Function([], output)
mutated_mod['func_17313'] = func_17313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16875_call = mod.get_global_var('func_16875')
func_16877_call = mutated_mod.get_global_var('func_16877')
call_17335 = func_16875_call()
call_17336 = func_16875_call()
output = call_17335
output2 = call_17336
func_17340 = relay.Function([], output)
mod['func_17340'] = func_17340
mod = relay.transform.InferType()(mod)
mutated_mod['func_17340'] = func_17340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17340_call = mutated_mod.get_global_var('func_17340')
call_17341 = func_17340_call()
output = call_17341
func_17342 = relay.Function([], output)
mutated_mod['func_17342'] = func_17342
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17358 = relay.var("var_17358", dtype = "float32", shape = (6, 1, 16))#candidate|17358|(6, 1, 16)|var|float32
uop_17359 = relay.cos(var_17358.astype('float32')) # shape=(6, 1, 16)
output = relay.Tuple([uop_17359,])
output2 = relay.Tuple([uop_17359,])
func_17361 = relay.Function([var_17358,], output)
mod['func_17361'] = func_17361
mod = relay.transform.InferType()(mod)
var_17362 = relay.var("var_17362", dtype = "float32", shape = (6, 1, 16))#candidate|17362|(6, 1, 16)|var|float32
output = func_17361(var_17362)
func_17363 = relay.Function([var_17362], output)
mutated_mod['func_17363'] = func_17363
mutated_mod = relay.transform.InferType()(mutated_mod)
const_17372 = relay.const([[[3.227748,7.779279,8.465735,3.866588,6.712401,2.258427,8.521634,5.665732,-7.068619,3.651052,8.026271,2.674210,8.962988,-9.625921,1.979868,4.815090],[-4.041140,3.860791,5.172260,6.629667,-0.790199,-9.681505,1.450602,-3.673325,9.159640,-5.655903,4.823706,-3.378138,9.813283,-7.050929,-3.364381,0.663250],[-4.405754,-3.579929,-8.783301,8.606625,-2.102706,-4.808400,9.463014,-8.343483,2.585758,4.648588,-3.550487,8.378205,8.493776,-3.871890,0.621071,-1.050671],[3.242404,6.016758,-0.499999,-6.238799,-5.916705,4.699017,-1.456093,-9.852051,-8.600928,-0.693396,-1.432885,5.645192,-4.231679,0.816339,1.849360,3.877780],[7.920238,-0.934029,8.188532,-4.768624,-1.251136,0.444274,7.030971,-0.289880,-3.544269,-8.191287,-5.413234,-6.005531,-8.107357,-2.591087,2.130407,-3.561841],[-5.007791,-2.481288,3.811321,2.478573,-7.331809,-2.764560,2.939273,-4.110484,-0.121736,-2.369750,-7.800204,0.311596,-5.498786,-2.122216,2.761291,-2.463074],[-2.873346,-1.244407,-0.746607,1.901324,-4.858419,-9.074476,-4.527601,3.900005,-5.054715,0.827030,-3.452827,3.986667,-3.044632,-9.773964,-3.171102,2.096949],[-5.886843,-4.668388,0.134464,1.156155,-2.983664,5.681998,-8.325990,3.757577,-4.150668,0.500913,7.854940,-6.600523,4.123176,1.002409,4.862321,-2.971858]],[[-7.081509,-0.923290,-0.733509,-4.116479,-8.141863,9.600730,-3.902807,6.181987,1.922963,-3.370602,1.349685,-6.625900,0.330653,-9.667342,-6.348908,-6.774394],[4.039922,-7.197990,4.131744,-9.029792,9.404779,-6.090120,-1.124119,-0.423871,9.032523,-5.319038,4.441257,8.177839,7.045168,-3.719096,-3.377508,-2.754647],[9.002265,8.634764,9.391823,-2.627690,0.061239,0.079201,-5.853420,3.019521,-0.513379,-3.112354,-8.826039,-4.150348,1.629707,9.250483,-4.521878,-0.494860],[-0.461377,-0.380151,8.416879,-4.476593,3.255152,5.248675,-3.530973,7.531714,-7.390859,-9.902522,2.635951,-9.528009,0.257107,-6.300327,-4.923228,-4.101223],[-9.689256,-6.280261,7.567902,-1.628592,-1.677834,8.537949,-6.791472,6.148746,-9.450508,4.317111,4.453123,3.401888,1.354363,-5.045117,-6.576638,4.277107],[5.483457,-3.460782,-2.161822,2.591941,-0.489188,0.526323,-5.439024,-0.053509,8.871380,-9.411639,3.131321,8.700915,-1.582566,-8.700703,-5.182722,3.943663],[-3.663404,0.440573,7.577038,5.192617,7.581993,-2.859000,-8.672517,-5.632062,3.835133,-8.629512,-8.332194,1.607697,2.697970,2.896504,1.071190,4.330469],[0.931751,1.939226,2.003819,-7.128333,8.256474,-0.538701,9.427010,5.559890,-7.997085,-8.187241,-9.576444,8.621897,5.964132,4.044291,8.922670,-4.305615]],[[2.358101,5.646874,4.463276,8.256543,4.477025,-8.028259,5.768706,7.812346,7.895459,-3.138433,1.936190,6.837873,9.040017,-1.673140,4.043318,9.550612],[-0.240315,1.947412,-5.114181,-3.608114,1.352821,3.936175,0.698064,-8.485347,-2.363952,-8.435981,-4.490775,-0.150497,-9.470456,-5.947429,-4.169212,5.280515],[0.850648,-6.417313,7.689204,6.276234,2.779037,0.614350,8.308066,3.856340,1.094194,0.299971,2.001492,6.916882,-3.701645,8.113957,9.916234,6.924212],[7.452031,-8.311107,9.983753,0.692929,-0.926018,2.524486,-1.731266,8.070014,-6.829310,9.649555,4.267390,2.811137,8.246103,-5.741497,6.035484,3.378403],[4.901658,-2.421895,4.338521,5.528545,-9.913520,7.309062,1.876836,-8.992071,6.112224,4.123998,-0.830685,3.874359,3.193956,-9.720940,2.907866,2.404152],[-6.382100,9.292413,-2.543141,1.174914,0.712555,4.477337,-5.690476,-6.821766,-9.395742,-6.912313,3.167013,-8.830310,9.102055,2.290244,-2.031146,2.132412],[-9.272185,-3.300278,6.825552,-8.726954,-4.106025,9.422874,2.926493,-4.476774,6.719019,8.814534,-9.938224,5.807830,-9.317437,9.241934,0.835181,3.287117],[7.451408,-6.289264,-3.521869,-7.282367,9.699252,9.359631,4.249453,-0.071584,-8.255566,1.385287,3.404249,-8.813157,-8.697769,-1.906727,-2.239112,7.109904]],[[2.057075,-2.065328,-2.042005,-9.318339,-1.677870,2.841281,2.019009,-3.274123,3.808348,3.371830,-7.243490,-4.398989,8.604349,-2.256040,8.045800,0.308882],[-1.584728,-1.831935,-6.147307,-4.095155,-1.592949,4.631235,8.335187,3.421318,0.853717,1.075810,-8.302026,-8.457898,-9.956563,1.933323,9.139354,-5.237069],[-5.113219,-5.763282,8.782283,6.503131,-5.731139,4.671829,-5.229183,-7.258463,3.799272,7.580056,-3.374996,2.358918,-8.468147,-1.873184,-5.967968,8.960917],[7.800005,4.054105,-7.082360,-7.886859,9.978954,-6.691154,-2.980225,-1.289035,-8.437778,8.266446,9.910633,9.607717,4.444034,9.886539,-2.827962,-3.000129],[6.806267,-1.390956,-1.507693,-7.573045,7.648404,9.923801,-1.939709,0.379748,1.084727,9.858509,-2.739838,-8.376056,-7.929884,5.792061,9.954417,-7.804555],[2.916715,-4.059595,9.155617,-5.428174,-2.098906,-3.847638,6.867734,3.686733,-1.338996,7.399819,-4.617524,-1.268202,-3.823407,9.338332,6.540414,-9.984350],[4.181540,-8.835668,6.438793,3.665615,-5.038711,-4.311922,5.525222,-0.513587,-0.545841,-5.967592,1.384691,0.055859,-5.530407,1.482478,-7.379364,7.495233],[1.038844,-1.397692,-7.611951,-6.568111,3.246773,-6.969786,-5.426412,-7.908651,-0.800034,1.399078,6.254540,6.586582,-0.941349,7.889337,-4.221039,-1.793689]],[[-0.061072,2.114819,-8.035061,1.458559,-0.510056,-6.512836,-9.646444,-2.256360,-2.963646,8.416940,-4.472163,4.755239,9.604337,-3.653415,6.380111,0.905741],[2.535142,-1.632349,-9.793778,-6.815325,5.694456,-6.488047,7.856437,6.739669,-0.597978,-3.245050,5.201731,0.486623,-9.241108,4.711753,-7.902561,-6.938569],[4.625117,6.537401,-5.365516,-4.175106,3.056800,-2.722129,7.418549,-8.067977,-2.513982,8.490983,-0.966761,-3.517903,-2.435391,9.529580,5.330816,-5.400690],[-2.559139,-0.951261,1.467626,0.580457,8.645693,-9.956042,4.546053,0.022141,2.881257,3.329815,1.578631,-9.545333,3.477573,7.574326,1.305200,8.407129],[6.261748,7.693502,9.675490,2.069304,-4.530662,4.275490,-4.780506,6.153652,1.427123,-0.403456,-7.758997,-2.515054,-1.527228,-2.628345,-2.820013,0.391264],[-6.676776,-0.009352,3.319643,-6.451495,8.124601,5.184594,-7.304929,0.032698,-3.607382,5.992571,8.479190,-8.459520,9.474168,2.031575,0.184991,3.242116],[5.028118,4.660989,-5.078311,-9.053395,4.845068,6.416647,-8.252257,-1.929091,-5.395882,-0.108592,5.007155,5.247751,5.686438,-7.504608,-4.067281,-0.446764],[-7.576727,-0.225702,-7.995771,-6.023674,3.064273,0.556724,0.488309,-3.158042,0.043759,5.141713,9.267550,5.100539,1.670932,1.292957,-6.298849,-8.666522]],[[9.467683,4.416120,0.249112,-1.338002,1.558568,0.133687,5.351245,4.699915,-4.820211,0.576933,1.364751,-4.018430,7.692000,-0.537833,-6.143315,-1.896931],[-4.754373,3.115430,2.583387,-1.012212,8.589646,2.371619,0.370444,-4.417304,9.611414,5.223999,-3.153901,-6.837950,-6.776887,2.967635,0.909938,-3.558996],[1.321969,5.303039,8.091830,-9.706964,0.383595,8.959357,-1.343821,-7.586162,-3.925384,-0.342691,-5.389005,-6.043797,-2.874766,0.397840,1.634010,1.534037],[2.942469,8.634154,-8.025382,1.895444,-1.641363,-1.225705,-0.247023,-1.908002,-2.281174,-5.440633,6.768788,4.314102,-6.715151,1.115713,1.891360,1.637847],[-7.650995,3.542481,-2.935339,-0.339884,-7.230882,3.295880,-3.726996,0.382440,-8.930470,2.356091,-8.242766,7.362899,6.595295,-5.619964,0.138757,1.956127],[-3.841657,-4.843427,4.940781,0.553662,8.598194,4.036686,8.571689,5.647478,-7.241035,3.624566,9.848609,2.929477,-8.620191,9.800828,9.731532,6.309850],[-0.467679,-2.395518,-7.609049,6.874483,-7.709105,6.244905,0.442388,-1.297396,1.908759,-3.868440,-3.185325,4.377946,6.140207,8.170294,3.509466,-4.386174],[-2.543846,-4.653220,1.207091,8.953471,-6.990055,8.705321,4.936044,9.639623,7.413350,9.281455,3.385089,-1.220685,-8.238613,-7.435653,-5.514098,2.640123]]], dtype = "float32")#candidate|17372|(6, 8, 16)|const|float32
uop_17373 = relay.log10(const_17372.astype('float32')) # shape=(6, 8, 16)
func_2538_call = mod.get_global_var('func_2538')
func_2544_call = mutated_mod.get_global_var('func_2544')
var_17386 = relay.var("var_17386", dtype = "bool", shape = (117,))#candidate|17386|(117,)|var|bool
const_17387 = relay.const([[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True]], dtype = "bool")#candidate|17387|(702, 1)|const|bool
const_17388 = relay.const([-6.218390,8.066355,7.569794,3.059800,3.287073,5.734263,-5.517023,-6.986619,3.591590,5.570344,2.637967,-0.197309,5.135978,3.230432,2.319774,-2.400405,-6.653595,-1.718796,-2.100221,-8.780833,-3.417818,4.458850,4.559215,-5.529133,1.604504,5.513110,0.209060,-4.548317,-3.209337,5.037804,-9.252488,9.190166,2.869640,-2.533382,-8.124371,2.112277,-5.145682,4.897665,9.763152,-6.067708,3.626969,3.998067,-0.546935,9.459971,1.592606,-4.244321,2.024562,-9.466619,-6.461875,-8.979494,-7.277976,7.857666,-6.721515,-6.347030,5.123169,-3.355664,-9.658723,3.001568,8.532464,6.287719,5.971833,-5.342922,-2.940399,0.709934,0.339321,6.421685,1.834351,4.698748,9.581862,3.457111,-7.950361,0.375219,9.799660,5.520902,-4.040264,3.411632,1.748447,-6.807383,4.269523,-1.346916,4.373751,-9.863927,-4.613955,-5.550075,8.052020,-4.629927,3.284331,-2.778935,-6.912897,9.217663,-6.120473,-1.635943,5.408465,7.209688,-1.443429,2.824870,9.816481,5.353053,9.210537,4.951998,7.710684,3.164514,-6.971957,-9.414161,2.450267,1.115897,-2.038421,5.381224,-1.136827,-4.139262,-6.208673,-4.749469,3.459465,-2.637198,0.457497,6.814819,7.678447,9.614189,-7.595134,5.813447,5.699140,-6.457378,-3.846100,2.162011,-9.442429,-6.452201,-3.231120,9.191048,-0.953152,-4.476415,7.407786,-9.171056,-8.223942,-5.530057,4.730614,7.733858,-6.538687,5.868837,7.162653,9.598104,-1.422262,9.197390,-5.433592,8.069755,-5.502530,-6.767965,4.367020,-9.628882,-8.300882,7.491948,-4.912827,7.493965,-4.085512,-3.578606,7.634765,2.071597,4.990487,-0.420698,2.868573,-8.260347,-5.046667,-2.944783,1.800539,4.818051,9.877479,-9.546770,6.202233,3.362871,-4.899035,-7.889896,8.926070,5.096637,-6.806941,6.592125,3.452289,7.568925,-5.217434,-1.024894,-0.023131,-0.240195,-0.688383,-6.268284,-7.065947,1.533833,0.607216,-6.784430,1.451715,6.889961,-5.316047,-6.539873,-9.603780,5.037117,4.391149,-0.950867,1.146786,1.115260,7.663203,-7.515069,6.593892,-4.311910,3.664196,-3.170174,4.868913,-9.059451,-8.470036,8.408408,-2.473305,2.738717,-1.648139,7.250793,-1.875497,0.651288,-7.933014,9.264576,9.815796,-1.453064,1.014557,-0.432576,-2.530322,-0.944430,0.935500,5.046865,-0.788530,6.061410,4.825932,-4.094256,5.954172,6.418798,2.564648,-8.347363,3.286756,5.649391,6.978299,3.435393,-0.709960,-7.892008,5.854868,3.973444,-7.905715,0.328112,-7.658934,-3.299355,0.410606,7.207863,-1.546464,-0.127957,6.311284,-9.240319,6.381816,-6.811870,4.445460,3.449163,4.656548,-2.328224,9.632096,1.560774,-5.093370,4.402629,3.904132,-6.590854,-9.419174,8.747924,1.762842,-3.853829,7.049867,-3.490904,7.195706,-1.935025,8.101608,3.021543,-5.231917,-5.962213,-8.607497,-5.755133,-9.980066,9.226107,4.924032,-4.533585,0.707264,7.965505,-2.967830,2.597390,7.014665,-8.523305,7.894631,9.143739,-2.441935,-5.864649,-6.934773,-3.307351,6.808674,0.366161,1.065278,4.470702,5.188451,8.154239,8.813467,2.713251,-3.154190,7.214609,4.939503,4.272102,-3.035067,-5.084278,3.189620,5.365310,1.361193,3.511533,5.968828,8.510394,-1.993024,-0.380858,2.667359,-9.943082,9.990287,1.658974,0.904043,-9.081331,-2.591651,-8.533248], dtype = "float32")#candidate|17388|(320,)|const|float32
const_17389 = relay.const([-8.605738,4.947585,3.607679,-8.406673,-5.993643,5.347182,4.231363,4.966361,3.093164,1.351783,-8.039809,-9.363148,6.725387,-8.133211,0.955660,0.055688,-2.287350,4.990389,7.307472,2.124774,-1.451944,4.927770,5.619908,-9.708480,-5.321549,7.589335,6.878663,6.065695,-4.250506,0.608239,2.987754,0.962106,-7.654565,-9.699813,4.248972,4.540871,-0.020591,5.627021,2.862821,3.268381,8.372659,-7.452955,-0.449569,3.972206,2.634951,-5.865329,3.395360,0.841240,-9.045139,2.950497,0.191571,2.752285,-4.175858,7.984310,-0.071540,2.333991,5.923714,-2.161073,3.690220,-5.449027,7.837077,-4.978798,8.829806,-0.904575,1.335793,2.574457,-6.806453,-2.091168,7.332323,-9.056837,-0.371893,5.880803,-9.423517,-4.511212,-3.214647,-3.290241,6.560152,-5.388211,-4.211127,2.585177,7.998354,8.782555,5.797530,-7.848533,3.531739,9.264763,-6.913987,-0.493198,-7.162057,-0.893992,7.085645,-7.323552,7.191786,3.126912,7.440782,1.942346,1.321628,-1.807166,4.282776,2.788463,-9.803354,-9.027973,-2.036089,5.058862,4.360090,6.972580,-4.357763,-7.984112,-4.328281,-0.322642,-9.982025,-9.622838,-2.519229,-7.213755,7.840370,-4.499677,-9.710249,-6.038556,1.535378,-8.888636,-4.131818,-9.898385,4.786483,-6.071401,-7.472849,-4.602145,8.428816,5.412531,2.224153,4.684400,7.745280,-1.640688], dtype = "float32")#candidate|17389|(132,)|const|float32
var_17390 = relay.var("var_17390", dtype = "uint64", shape = (660, 1))#candidate|17390|(660, 1)|var|uint64
call_17385 = relay.TupleGetItem(func_2538_call(relay.reshape(var_17386.astype('bool'), [9, 13, 1]), relay.reshape(const_17387.astype('bool'), [9, 13, 6]), relay.reshape(const_17388.astype('float32'), [320,]), relay.reshape(const_17389.astype('float32'), [132,]), relay.reshape(var_17390.astype('uint64'), [330, 2]), ), 4)
call_17391 = relay.TupleGetItem(func_2544_call(relay.reshape(var_17386.astype('bool'), [9, 13, 1]), relay.reshape(const_17387.astype('bool'), [9, 13, 6]), relay.reshape(const_17388.astype('float32'), [320,]), relay.reshape(const_17389.astype('float32'), [132,]), relay.reshape(var_17390.astype('uint64'), [330, 2]), ), 4)
func_13903_call = mod.get_global_var('func_13903')
func_13904_call = mutated_mod.get_global_var('func_13904')
call_17393 = relay.TupleGetItem(func_13903_call(), 0)
call_17394 = relay.TupleGetItem(func_13904_call(), 0)
output = relay.Tuple([uop_17373,call_17385,var_17386,const_17387,const_17388,const_17389,var_17390,call_17393,])
output2 = relay.Tuple([uop_17373,call_17391,var_17386,const_17387,const_17388,const_17389,var_17390,call_17394,])
func_17417 = relay.Function([var_17386,var_17390,], output)
mod['func_17417'] = func_17417
mod = relay.transform.InferType()(mod)
var_17418 = relay.var("var_17418", dtype = "bool", shape = (117,))#candidate|17418|(117,)|var|bool
var_17419 = relay.var("var_17419", dtype = "uint64", shape = (660, 1))#candidate|17419|(660, 1)|var|uint64
output = func_17417(var_17418,var_17419,)
func_17420 = relay.Function([var_17418,var_17419,], output)
mutated_mod['func_17420'] = func_17420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11122_call = mod.get_global_var('func_11122')
func_11123_call = mutated_mod.get_global_var('func_11123')
call_17446 = func_11122_call()
call_17447 = func_11122_call()
func_14495_call = mod.get_global_var('func_14495')
func_14497_call = mutated_mod.get_global_var('func_14497')
var_17473 = relay.var("var_17473", dtype = "float64", shape = (14, 1))#candidate|17473|(14, 1)|var|float64
call_17472 = relay.TupleGetItem(func_14495_call(relay.reshape(var_17473.astype('float64'), [14,])), 0)
call_17474 = relay.TupleGetItem(func_14497_call(relay.reshape(var_17473.astype('float64'), [14,])), 0)
func_10683_call = mod.get_global_var('func_10683')
func_10684_call = mutated_mod.get_global_var('func_10684')
call_17479 = relay.TupleGetItem(func_10683_call(), 0)
call_17480 = relay.TupleGetItem(func_10684_call(), 0)
func_11878_call = mod.get_global_var('func_11878')
func_11880_call = mutated_mod.get_global_var('func_11880')
call_17483 = func_11878_call()
call_17484 = func_11878_call()
func_14077_call = mod.get_global_var('func_14077')
func_14078_call = mutated_mod.get_global_var('func_14078')
call_17485 = relay.TupleGetItem(func_14077_call(), 0)
call_17486 = relay.TupleGetItem(func_14078_call(), 0)
func_8161_call = mod.get_global_var('func_8161')
func_8162_call = mutated_mod.get_global_var('func_8162')
call_17499 = relay.TupleGetItem(func_8161_call(), 1)
call_17500 = relay.TupleGetItem(func_8162_call(), 1)
output = relay.Tuple([call_17446,call_17472,var_17473,call_17479,call_17483,call_17485,call_17499,])
output2 = relay.Tuple([call_17447,call_17474,var_17473,call_17480,call_17484,call_17486,call_17500,])
func_17502 = relay.Function([var_17473,], output)
mod['func_17502'] = func_17502
mod = relay.transform.InferType()(mod)
mutated_mod['func_17502'] = func_17502
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17503 = relay.var("var_17503", dtype = "float64", shape = (14, 1))#candidate|17503|(14, 1)|var|float64
func_17502_call = mutated_mod.get_global_var('func_17502')
call_17504 = func_17502_call(var_17503)
output = call_17504
func_17505 = relay.Function([var_17503], output)
mutated_mod['func_17505'] = func_17505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15016_call = mod.get_global_var('func_15016')
func_15018_call = mutated_mod.get_global_var('func_15018')
call_17564 = relay.TupleGetItem(func_15016_call(), 1)
call_17565 = relay.TupleGetItem(func_15018_call(), 1)
output = call_17564
output2 = call_17565
func_17567 = relay.Function([], output)
mod['func_17567'] = func_17567
mod = relay.transform.InferType()(mod)
output = func_17567()
func_17568 = relay.Function([], output)
mutated_mod['func_17568'] = func_17568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8644_call = mod.get_global_var('func_8644')
func_8645_call = mutated_mod.get_global_var('func_8645')
call_17607 = func_8644_call()
call_17608 = func_8644_call()
output = relay.Tuple([call_17607,])
output2 = relay.Tuple([call_17608,])
func_17611 = relay.Function([], output)
mod['func_17611'] = func_17611
mod = relay.transform.InferType()(mod)
output = func_17611()
func_17612 = relay.Function([], output)
mutated_mod['func_17612'] = func_17612
mutated_mod = relay.transform.InferType()(mutated_mod)
const_17621 = relay.const([[[-0.538944,-0.672792,4.163787,8.955925,8.405626,3.903842,1.321452,1.562385,9.978940,-8.231231],[-6.668143,5.211737,-9.784112,5.085563,0.510433,8.558710,9.797043,-1.302427,8.199922,-4.188140],[0.688310,3.051028,-2.421582,-3.582697,-2.554865,5.018991,-3.379897,-1.808026,7.812738,7.181700],[-9.092966,5.690358,-9.557378,6.958022,4.272020,4.824056,4.706983,5.876980,0.025160,1.520235],[-8.545287,-7.437007,7.186825,7.489971,9.231005,3.462781,2.824952,7.531285,7.122869,6.653033],[-0.518205,5.040568,-1.116223,6.869239,-5.530471,0.330700,-4.107412,1.435827,-0.039891,-5.627934],[8.828316,-8.553147,-4.885835,6.891802,-9.941195,-3.391279,5.791190,-9.569416,-8.696133,1.911788],[-8.544867,5.853496,-2.130335,0.652581,3.161516,-6.954372,0.419788,8.759571,-0.300792,9.759600],[-7.881073,6.626817,7.239701,6.678527,-1.260692,0.211495,0.319145,8.839549,2.221919,-1.904213],[-6.916565,-9.308414,2.708029,-4.530555,-7.746577,-5.690648,5.371044,-6.987911,6.843262,8.189451],[-6.815968,7.545564,4.239781,7.429279,4.304999,-8.391155,9.171967,8.758676,-7.766406,-3.807548]],[[-4.604007,4.321000,5.276475,-3.635381,5.391196,-9.808699,-0.275497,5.334815,-2.526480,9.618296],[0.078349,0.082012,-3.641913,2.952221,-6.291603,3.606704,3.548807,9.667149,-7.480450,1.308287],[9.619456,1.052188,1.238714,5.851732,4.487992,0.506442,-4.746169,1.025178,-1.654661,-7.069645],[6.419747,8.646206,-6.661428,4.755637,-4.695152,1.614138,-8.990507,-5.019350,0.042536,8.386217],[-1.347082,4.483759,3.122834,0.780562,-4.714940,9.367481,9.222977,-2.398068,4.654400,-5.558071],[-9.861646,8.976359,-0.162827,7.203377,7.733328,-1.020560,2.832730,1.375576,2.524105,-5.086153],[-9.613815,9.019871,-7.918015,4.942379,4.188198,-4.037007,7.902825,-8.928460,1.871464,-7.971263],[-3.524853,-3.099452,-8.159206,-7.151067,-8.668757,2.850141,-8.284457,-1.286117,-1.269788,-5.398890],[1.860626,-1.762755,-3.485239,-6.387818,-0.109540,4.660136,3.445386,-2.699213,9.890804,9.673513],[-0.156770,-4.033094,8.713232,1.586103,-5.356537,4.569398,-4.361399,1.026469,-0.607186,-3.476536],[-9.056314,3.049679,8.076946,1.012289,9.411050,-5.399873,-9.517890,-2.367693,9.238602,0.883616]],[[-4.233140,6.807517,-2.669924,4.800018,-1.462541,1.613347,7.223732,9.330842,9.140606,8.016994],[0.175391,-5.483485,-0.158391,-3.406755,-3.769347,-7.465230,-0.310326,-9.250288,-0.638325,-7.675983],[9.848488,2.994809,-0.329579,-2.778331,8.325563,-7.080350,0.668322,-5.732347,-7.710800,-6.128503],[6.787908,0.138789,-6.528864,-4.380419,4.536641,-6.519501,7.616198,-4.546422,-7.982951,1.937864],[-3.072063,-2.369202,-1.395800,-8.570031,6.965869,1.257717,2.585163,1.361057,-7.703551,-9.303435],[-6.040361,6.587340,-9.446292,2.250957,-6.722615,-9.916165,3.600660,-0.743184,-3.586720,-5.025173],[8.161169,-9.565209,-8.993468,7.330116,5.853464,-0.263526,-9.100231,5.894510,8.887500,2.197014],[6.389286,8.677028,-0.761867,-6.970576,-0.135809,0.240285,8.062079,-9.058405,9.907467,-6.981550],[8.288010,-6.600301,-3.976550,-3.701709,-4.454015,2.959411,1.035058,-3.444445,3.666644,-6.612530],[0.835171,2.054935,9.033105,-2.647604,9.830199,-5.196613,-1.420799,-8.160153,-2.814707,-6.560549],[-0.985360,6.325283,-5.083508,-4.341484,-1.093075,7.238317,-6.685142,-1.658509,-3.367699,-2.323194]],[[-3.780150,-9.100387,8.903116,1.963479,4.543511,-9.795211,-5.676910,-1.747083,-8.038661,-7.400475],[6.242013,-8.789893,-2.771687,-9.981086,-7.945538,5.214614,8.829511,3.185007,-1.993916,-6.484311],[-5.943803,-1.981096,-9.462720,-1.208570,8.698680,-7.944698,-8.259960,-3.930042,2.979171,-6.674437],[6.803395,-4.669169,0.230513,6.571797,8.314829,-4.716773,-7.737249,-6.887392,5.482230,2.466962],[9.650102,2.820409,7.091677,-3.188231,-0.271347,-2.920292,-5.761977,-0.068093,-0.500975,-8.783615],[-2.310793,7.000201,2.179490,6.863796,-4.469901,3.298601,-7.646272,-4.324686,-3.915316,3.935196],[5.311437,-5.261528,-6.944914,9.799345,-4.140375,-1.543830,-5.634006,7.905131,2.979314,-9.889647],[-1.804508,0.960741,7.585818,-7.386704,1.849851,-6.964462,4.533451,-5.359895,-6.887342,-0.559983],[3.077968,6.260495,-4.522139,2.524556,9.345287,-4.387153,0.452466,5.734800,8.165719,-8.996818],[1.046792,1.007249,8.846677,-4.409177,5.220394,-4.188318,-3.896310,8.327732,6.154142,-0.497537],[-3.465125,-9.622652,2.555051,-2.225214,0.712950,6.153569,-6.854285,8.419078,-6.945023,8.810235]],[[-7.438051,2.636796,5.482484,9.025331,6.963536,1.254254,-1.487195,-0.211826,1.820617,-0.848030],[5.345997,5.216203,-8.636289,-4.470929,7.227258,9.038297,2.141414,-4.253568,7.818302,6.302188],[2.668470,-8.931058,-0.902005,1.163150,-6.151402,-7.333969,4.570265,7.218254,-0.090091,4.070632],[5.473311,4.303764,9.072126,1.555762,-1.454832,5.591564,2.895312,9.098933,-7.917522,-6.980760],[3.099330,2.631675,-6.561265,-6.277280,-5.747369,-7.503628,-7.614275,-3.803154,4.727011,-4.894916],[7.575442,-9.506001,-6.334642,-5.938589,-2.563062,2.433003,-9.595717,0.483586,7.370869,4.782884],[8.514428,3.565815,-6.551382,1.358113,2.714985,3.018997,1.861868,0.219280,9.459866,0.990259],[-0.676255,3.844289,0.465393,-0.581655,4.712401,-5.939637,2.402465,-8.190073,2.034759,-8.171294],[-3.459082,6.751596,3.016879,4.250635,0.161678,-7.290597,7.288871,-1.974371,-2.498985,5.189698],[-0.362087,-9.186290,2.703497,3.261949,-4.221758,6.810921,1.473512,7.912537,3.570514,-0.664555],[8.167437,8.338267,-0.072836,9.677726,-2.062449,-2.349901,-6.502476,-4.758183,-4.971927,-4.454842]],[[3.405962,1.499959,6.214844,0.628032,5.625488,8.388085,1.271462,4.559220,-7.827398,-8.695393],[8.167126,4.257362,-1.172095,0.160269,-3.352505,2.219046,4.047883,-5.931865,8.803589,2.018228],[3.116091,9.283816,3.955630,5.130870,8.666472,-9.247303,-9.881845,-7.968180,-2.239537,1.017394],[-6.161796,-1.589599,3.440244,-1.951095,1.297176,8.347455,-7.094987,7.773448,9.548520,2.435350],[-4.154728,9.332848,1.011395,4.339230,3.379864,-7.824413,-7.978743,4.175502,-1.069439,-7.079949],[-6.018195,-8.710648,3.199158,-1.124394,-5.456660,5.135278,-6.779091,-3.446946,1.360567,8.682420],[-7.798393,-0.981859,-2.349920,9.592443,4.673294,-2.843090,0.026243,-6.104179,-9.699253,-1.793405],[-5.113719,-7.598973,-6.053132,-3.972368,-2.597330,2.061106,-4.039742,5.848772,7.860957,3.669286],[0.061764,-1.067980,-8.185480,4.859367,-2.167349,-5.353095,0.370323,9.821271,9.719844,2.872342],[2.018990,-4.574794,-6.373932,-5.644298,-3.009618,-6.358392,-1.382683,8.126720,5.172401,0.560307],[-4.097280,-9.924474,-4.363201,1.410415,-0.787066,-0.831370,9.896389,6.643473,-6.433789,-0.553607]],[[1.659011,-0.605951,7.480522,-8.865254,-2.233146,-9.593602,1.861697,0.008598,-2.644012,9.461873],[0.767306,-4.056479,7.994521,5.980056,-6.715182,-9.812380,-9.328271,5.496275,-2.931216,9.513024],[5.459516,3.377276,-9.725966,1.784648,-7.011503,3.471501,-3.068851,-4.965890,5.020278,5.433750],[0.680600,5.591359,0.955193,-1.035120,2.308543,-2.159704,2.152099,4.018772,-2.190299,6.002674],[-4.269904,0.164846,-8.911509,-2.966412,8.337043,4.189480,4.544739,-4.010270,7.737375,0.379952],[-8.523522,-5.744232,7.082269,-9.391176,-1.678777,-8.160201,-0.891322,2.152159,-0.515375,3.660655],[2.474425,-1.225420,7.010562,0.079893,4.239299,5.671666,0.667985,-7.266074,-9.170783,-3.146793],[-0.868055,3.324328,-3.668748,5.867615,-2.013722,-8.769431,-7.999140,-1.618907,-4.521669,-8.793438],[-2.423298,8.564238,1.609473,5.414896,-9.307204,-1.944965,-5.674075,-8.435244,-7.586284,9.725623],[-9.319577,6.098735,7.496808,-2.286183,5.691793,6.011512,1.144610,1.472730,-6.374418,-1.935963],[8.878376,8.181239,-0.769534,-4.669394,-6.665325,3.976974,-5.633444,0.955409,-2.653265,0.959107]],[[-5.884144,-1.757257,6.096735,7.514355,-5.071726,7.524915,-8.202751,1.766742,-9.182197,-6.760659],[-1.680689,3.242063,-9.626196,-4.464215,-8.338301,-7.599601,-2.435957,-7.841227,4.487446,-4.272993],[2.606487,7.835085,-2.639472,-3.689259,-7.634379,7.931076,-7.115089,0.482143,5.597628,-0.099352],[6.020355,4.942031,7.645124,-7.882526,1.026620,-0.617803,-7.002058,-2.826061,-1.202346,6.644414],[5.250749,6.166655,3.598022,-0.211965,-5.346528,-8.291524,-5.134893,-5.943618,-1.811629,-9.914778],[2.036369,-3.713739,-2.303917,-6.758773,-9.272066,9.344495,1.247207,0.240465,-2.615739,6.062048],[-6.191347,-4.529160,3.995400,-1.389033,5.142259,1.517418,4.115480,-4.465687,4.621406,6.960391],[-8.320610,2.114453,4.224720,-6.837282,4.707623,0.753804,-3.287161,-1.341520,-2.476490,6.562851],[6.076932,-3.003192,-5.966843,-0.716369,7.039688,6.224686,-7.886346,7.326779,-6.990528,6.212789],[-4.255507,5.968205,0.482899,-4.050729,1.374791,9.419490,3.348736,0.637260,7.329024,2.145860],[3.004504,-4.904930,6.297640,-7.112417,-2.119319,9.588773,-1.464083,6.365947,-1.847729,4.468895]],[[9.590946,-1.946569,-4.497316,-0.114633,4.050695,-4.677499,7.358340,6.220202,2.331238,-6.792572],[6.071017,-0.686517,-2.768833,0.783124,6.522769,-4.558330,-8.742797,1.721127,7.041561,-4.210030],[9.525194,5.906324,9.622550,-2.232786,-2.751506,-2.330059,-7.395689,3.153284,-1.454676,-9.551677],[8.663779,-8.745808,7.051270,-1.191684,-9.905852,-5.380963,-4.155314,-1.558685,-8.623007,-6.325514],[9.355521,-1.575252,4.274095,-9.097957,0.894448,2.073424,-0.439516,-4.253181,-9.432403,-8.190802],[5.528755,-3.302600,-4.903277,0.539520,8.746676,-0.744094,0.723711,0.787948,-7.967381,-7.168631],[-4.272381,9.754000,-1.314027,-1.193933,-9.492219,0.013749,7.447450,6.760200,-6.283278,-1.472064],[-0.511795,-7.177675,-5.941703,-8.409683,9.052224,-6.293321,9.978526,-8.184499,4.276269,-1.641278],[0.518580,8.963028,7.961552,0.460543,6.363794,-4.166361,-3.776147,1.756423,-5.090393,5.190343],[8.161113,4.181707,8.446152,-5.492352,-8.414662,1.820225,-0.828923,7.378080,0.360771,8.614405],[-9.191999,5.309750,-9.302492,6.140000,-3.425421,-2.634317,-3.913209,-5.940287,-0.394661,-2.063058]],[[0.364615,-2.008438,-7.118692,-7.874017,-5.526185,2.779638,1.541234,4.828738,0.381726,-4.716167],[-4.263187,1.471001,-5.762092,-1.127365,-9.338859,2.779055,-6.544571,2.761290,9.734859,8.490138],[1.309818,2.380095,0.809078,-4.869529,9.126384,-0.093746,-8.208985,1.442884,-2.112844,2.047797],[-8.676892,-8.807439,-4.801869,-2.376720,3.012388,-5.305459,-2.569037,3.609222,-8.953724,-8.612737],[-5.451684,4.166858,3.213762,8.203281,5.778015,-5.745061,-6.647208,-1.369455,6.982344,-3.762213],[-2.347720,7.669639,-8.884204,-7.652492,6.059184,0.600611,-8.124428,-9.533880,6.852222,7.320801],[-5.535819,-5.422440,-2.886851,6.314310,7.125157,7.312939,-7.467559,-8.183249,9.242491,-7.756661],[-3.059530,4.558210,-9.666355,-4.975230,5.652570,-6.311802,0.509121,-2.476673,-4.469457,2.970238],[-4.102393,5.333471,-4.098764,1.436230,6.578926,-7.671096,6.837823,-1.689789,3.911569,1.161180],[-9.232268,-8.317372,1.312272,7.876788,-3.820142,0.018328,8.990136,-2.316128,2.417688,-6.506647],[1.821587,-3.264317,-0.360488,-1.272314,1.026420,-5.413357,-0.306470,6.134313,-0.448081,3.749048]],[[-6.860710,6.716919,6.896524,9.081279,9.282378,2.226975,-5.308673,-0.709146,-5.200541,-0.550349],[-6.791544,1.639123,5.167581,-1.856073,-2.765094,-9.617874,0.595439,-3.765625,8.798915,6.340906],[7.523334,9.976021,-4.425922,-7.094824,2.489910,-3.026297,-6.199502,-8.289857,-0.067159,2.827225],[-5.671568,8.475329,6.415601,-5.958899,6.270014,4.078696,4.194722,-7.276850,-6.385566,-7.838669],[5.293867,-3.030541,7.753968,3.733771,2.991052,-1.987136,5.048723,9.692670,7.272277,5.382512],[3.993704,-6.673660,-9.011874,-4.625620,9.149410,-3.363657,2.169747,-4.168375,8.211318,9.840861],[-7.156750,-5.651841,5.339576,-1.099722,7.447011,-2.252002,5.080227,6.394340,5.524029,-9.734139],[2.258797,-4.284963,5.371509,0.119265,-0.849427,-9.130968,-3.795714,-7.662539,-8.075543,-4.237073],[4.307958,1.974630,3.872849,-4.593761,-0.125275,-1.254778,5.856137,2.249906,2.736709,3.364105],[3.092404,7.896497,-9.694903,3.531115,-3.599633,-3.463559,-6.741197,-2.269669,5.889295,0.299704],[-2.414000,2.241385,-1.669053,-8.641579,1.073925,5.257167,5.048886,-7.054629,3.636445,6.926147]]], dtype = "float32")#candidate|17621|(11, 11, 10)|const|float32
uop_17622 = relay.asinh(const_17621.astype('float32')) # shape=(11, 11, 10)
output = uop_17622
output2 = uop_17622
func_17628 = relay.Function([], output)
mod['func_17628'] = func_17628
mod = relay.transform.InferType()(mod)
output = func_17628()
func_17629 = relay.Function([], output)
mutated_mod['func_17629'] = func_17629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11236_call = mod.get_global_var('func_11236')
func_11238_call = mutated_mod.get_global_var('func_11238')
call_17655 = relay.TupleGetItem(func_11236_call(), 0)
call_17656 = relay.TupleGetItem(func_11238_call(), 0)
output = relay.Tuple([call_17655,])
output2 = relay.Tuple([call_17656,])
func_17697 = relay.Function([], output)
mod['func_17697'] = func_17697
mod = relay.transform.InferType()(mod)
output = func_17697()
func_17698 = relay.Function([], output)
mutated_mod['func_17698'] = func_17698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14174_call = mod.get_global_var('func_14174')
func_14175_call = mutated_mod.get_global_var('func_14175')
call_17855 = relay.TupleGetItem(func_14174_call(), 1)
call_17856 = relay.TupleGetItem(func_14175_call(), 1)
output = call_17855
output2 = call_17856
func_17857 = relay.Function([], output)
mod['func_17857'] = func_17857
mod = relay.transform.InferType()(mod)
output = func_17857()
func_17858 = relay.Function([], output)
mutated_mod['func_17858'] = func_17858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13583_call = mod.get_global_var('func_13583')
func_13584_call = mutated_mod.get_global_var('func_13584')
call_17868 = func_13583_call()
call_17869 = func_13583_call()
func_14620_call = mod.get_global_var('func_14620')
func_14624_call = mutated_mod.get_global_var('func_14624')
const_17874 = relay.const([2,-2,-7,10,-9,-6,-6,-10,-1,10,-8,-3,6,7,10,-1,-1,-7,9,-4,-2,7,-1,4,7,-2,-3,-10,-8,-5,2,1,2,4,5,-10,-10,-7,-3,3,-5,7,-7,-8,-3,-1,8,-10,10,-2,4,4,-8,-5,3,10,-2,-5,1,3,-4,-1,-8,7,-5,-7,-10,2,-3,6,4,2,-3,4,10,-10,-4,1,1,2,-6,4,-7,1,-3,5,-4,-5,6,5,-7,-2,-5,2,10,2,10,-1,2,8,10,-7,4,5,1,8,2,-8,-5,-5,-4,-1,2,-5,4,2,-9,-2,8,3,-5,9,10,-8,-10,10,-7,2,2,6,1,4,6,2,-3,-5,-3,8,2,8,9,7,8,-7,-7,8,10,5,-10,-2,-2,-1,-1,-10,-7,6,4,-3,-3,3,-3,7,5,-9,-10,7,-8,-9,-9,2,5,3,-3,2,-7,7,5,3,-5,4,3,-7,10,-10,5,7,1,-1,-8,-2,5,-3,3,-2,-8,4,-8,2,9,6,-5,-5,-7,-5,-7,-8,-6,7,-8,-8,5,-10,6,-8,-6,-10,1,1,2,-1,-3,-3,1,-10,9,5,-3,7,-9,-4,-3,-9,-10,2,-6,-2,1,10,7,1,10,-2,-5,2,-5,-10,-1,-1,-9,4,6,-6,3,-1,8,8,9,10,-8,7,-9,10,-6,-10,3,-10,-1,-8,-4,5,-10,-1,3,-3,4,-6,9,-2,8,9,7,2,10,10,-6,8,-10,-5,10,7,9,8,9,4,3,1,-5,-6,1,-10,3,-3,7,-7,7,3,-7,-6,3,4,-5,6,5,6,-9,5,4,-8,-7,8,-9,1,-5,2,9,6,8,6,3,1,6,-8,5,1,-1,5,-1,-5,5,6,1,8,1,7,3,10,6,-2,-5,3,2,-5,-4,1,6,-3,-9,-8,-4,6,3,-9,-7,-1,5,-6,4,2,-2,9,-10,4,-3,10,9,7,6,-2,8,-3,7,-10,1,-9,4,-10,10,4,8,3,1,-9,5,-8,-5,7,-10,-5,8,-3,-1,7,-7,-7,4,-2,1,10,5,10,-8,-3,4,1,-1,-4,-7,6,-3,-9,-4,-2,4,-2,1,-8,8,9,-7,-4,5,1,-1,8,-1,-1,-9,1,-4,-10,-4,5,-8,-2,5,3,3,3,-10,-8,-7,-7,9,-8,10,9,8,6,10,-3,3,4,10,2,6,3,6,-10,10,9,7,4,5,5,7,10,-6,7,-2,7,8,3,-2,10,-2,1,-8,7,4,-9,-10,10,3,-3,8,-7,10,10,-5,-3,9,6,-7,-3,7,-2,10,4,-1,2,-6,6,1,9,8,2,-4,-9,3,3,-5,-6,1,10,-4,-1,-1,8,7,-7,9,-4,-10,-5,-4,-3,-7,6,9,-10,-8,5,2,-3,-1,3,2,3,10,-4,-10,5,-6,-5,-7,-9,-6,6,8,-6,-10,8,-8,-3,-1,-5,4,10,1,6,-10,4,-9,-5,-2,5,2,5,4,-8,-4,8,1,1,-1,1,-2,-9,-9,-8,-7,-4,-4,-9,-8,-3,-8,-2,9,2,-10,3,-1,-5,-9,9,5,5,4,-10,-10,7,-6,-8,4,-4,6,6,-10,-6,-3,-6,-10,-8,4,-7,2,4,-2,-10,-4,-1,-2,8,10,-4,10,-1,-1,-7,8,-1,7,-8,-10,7,5,-6,7,-2,9,7,-3,2,-7,9,2,-6,7,-9], dtype = "uint64")#candidate|17874|(660,)|const|uint64
var_17875 = relay.var("var_17875", dtype = "float32", shape = (40, 8))#candidate|17875|(40, 8)|var|float32
call_17873 = relay.TupleGetItem(func_14620_call(relay.reshape(const_17874.astype('uint64'), [660,]), relay.reshape(var_17875.astype('float32'), [320,]), ), 1)
call_17876 = relay.TupleGetItem(func_14624_call(relay.reshape(const_17874.astype('uint64'), [660,]), relay.reshape(var_17875.astype('float32'), [320,]), ), 1)
output = relay.Tuple([call_17868,call_17873,const_17874,var_17875,])
output2 = relay.Tuple([call_17869,call_17876,const_17874,var_17875,])
func_17880 = relay.Function([var_17875,], output)
mod['func_17880'] = func_17880
mod = relay.transform.InferType()(mod)
mutated_mod['func_17880'] = func_17880
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17881 = relay.var("var_17881", dtype = "float32", shape = (40, 8))#candidate|17881|(40, 8)|var|float32
func_17880_call = mutated_mod.get_global_var('func_17880')
call_17882 = func_17880_call(var_17881)
output = call_17882
func_17883 = relay.Function([var_17881], output)
mutated_mod['func_17883'] = func_17883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15177_call = mod.get_global_var('func_15177')
func_15179_call = mutated_mod.get_global_var('func_15179')
call_17908 = func_15177_call()
call_17909 = func_15177_call()
func_12503_call = mod.get_global_var('func_12503')
func_12506_call = mutated_mod.get_global_var('func_12506')
const_17928 = relay.const([[False],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False]], dtype = "bool")#candidate|17928|(117, 1)|const|bool
var_17929 = relay.var("var_17929", dtype = "bool", shape = (234, 3))#candidate|17929|(234, 3)|var|bool
call_17927 = relay.TupleGetItem(func_12503_call(relay.reshape(const_17928.astype('bool'), [117,]), relay.reshape(var_17929.astype('bool'), [702,]), ), 0)
call_17930 = relay.TupleGetItem(func_12506_call(relay.reshape(const_17928.astype('bool'), [117,]), relay.reshape(var_17929.astype('bool'), [702,]), ), 0)
uop_17934 = relay.cos(const_17928.astype('float64')) # shape=(117, 1)
uop_17944 = relay.log10(uop_17934.astype('float32')) # shape=(117, 1)
output = relay.Tuple([call_17908,call_17927,var_17929,uop_17944,])
output2 = relay.Tuple([call_17909,call_17930,var_17929,uop_17944,])
F = relay.Function([var_17929,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_17929,], output2)
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
